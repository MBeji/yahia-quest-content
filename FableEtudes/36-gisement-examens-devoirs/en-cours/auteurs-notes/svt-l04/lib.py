#!/usr/bin/env python3
"""Aides communes des générateurs de missions (lot svt-l04).
Écrit des fichiers exercice JSON au format du corpus (type explicite, ids a-d, étiquettes sur les distracteurs mcq).
Contrôles internes : rampe, clé jamais strictement la plus longue, doublons d'options, chiffres arabo-indiens,
lettre d'option citée dans une explication, étiquettes déclarées au registre (copie de origin/main).
"""
import json, os, re, sys

BASE = '/home/user/wt-gis/content/sciences-vie-terre'
WORK = '/tmp/claude-0/-home-user/b03814da-e5f9-5a74-bf03-e7c23b20207a/scratchpad/svt-l04-work'
REG = json.load(open('/tmp/claude-0/-home-user-yahia-quest-content/973107ae-1cd3-5286-9aad-458ef39f3138/scratchpad/misconceptions.main.json', encoding='utf-8'))

DIAC = re.compile('[ً-ٰٟـ]')
AR_INDIC = re.compile('[٠-٩۰-۹]')


def sd(s):
    """texte sans diacritiques (comme lot-lint)"""
    return DIAC.sub('', s)


def nosvg(s):
    return re.sub(r'<svg.*?</svg>', '', s, flags=re.S)


def mcq(prompt, options, key, explanation, difficulty):
    """options : liste de (id, texte[, étiquette])."""
    opts = []
    for o in options:
        d = {'id': o[0], 'text': o[1]}
        if len(o) > 2 and o[2]:
            assert o[0] != key, 'la clé ne porte jamais d\'étiquette'
            assert o[2] in REG, 'étiquette inconnue du registre : ' + o[2]
            d['misconceptionTag'] = o[2]
        opts.append(d)
    return {'type': 'mcq', 'prompt': prompt, 'options': opts, 'correctOption': key,
            'explanation': explanation, 'difficulty': difficulty}


def matching(prompt, left, right, pairs, explanation, difficulty):
    """left/right : listes de textes ; pairs : liste d'indices (i_gauche, j_droite) 0-based."""
    options = [{'id': 'l%d' % (i + 1), 'text': t} for i, t in enumerate(left)] + \
              [{'id': 'r%d' % (j + 1), 'text': t} for j, t in enumerate(right)]
    return {'type': 'matching', 'prompt': prompt, 'options': options,
            'answerKey': {'pairs': [['l%d' % (i + 1), 'r%d' % (j + 1)] for i, j in pairs]},
            'explanation': explanation, 'difficulty': difficulty}


def ordering(prompt, steps, order, explanation, difficulty):
    """steps : liste de (id, texte) ; order : liste d'ids dans le bon ordre."""
    return {'type': 'ordering', 'prompt': prompt,
            'options': [{'id': i, 'text': t} for i, t in steps],
            'answerKey': {'order': order}, 'explanation': explanation, 'difficulty': difficulty}


def multi(prompt, options, correct, explanation, difficulty):
    return {'type': 'multi', 'prompt': prompt,
            'options': [{'id': i, 'text': t} for i, t in options],
            'answerKey': {'correct': correct}, 'explanation': explanation, 'difficulty': difficulty}


def check_mission(m, path=''):
    """Contrôles mécaniques maison (en plus de lot-lint et des gates)."""
    errs = []
    qs = m['questions']
    diffs = [q['difficulty'] for q in qs]
    if any(diffs[i] < diffs[i - 1] for i in range(1, len(diffs))):
        errs.append('rampe décroissante : %s' % diffs)
    for n, q in enumerate(qs, 1):
        t = q.get('type', 'mcq')
        ex = q['explanation']
        if len(ex) < 25:
            errs.append('Q%d explication courte' % n)
        for field in ('prompt', 'explanation'):
            if AR_INDIC.search(q[field]):
                errs.append('Q%d chiffres arabo-indiens dans %s' % (n, field))
            if re.search(r'\d \d{3}', nosvg(q[field])):
                errs.append('Q%d espace dans un nombre groupé (%s)' % (n, field))
        for o in q['options']:
            if AR_INDIC.search(o['text']):
                errs.append('Q%d chiffres arabo-indiens dans une option' % n)
        if re.search(r'(?:الخيار|الجواب|option|choix)\s*[abcd]\b', ex) or re.search(r'\(\s*[abcd]\s*\)', ex):
            errs.append('Q%d explication cite une lettre' % n)
        if 'الخطأ الشائع' not in ex and 'الخطأ الشّائع' not in ex:
            errs.append('Q%d pas de « الخطأ الشائع »' % n)
        texts = [sd(o['text']) for o in q['options']]
        if t == 'mcq':
            ids = [o['id'] for o in q['options']]
            if q['correctOption'] not in ids:
                errs.append('Q%d clé hors options' % n)
            if len(set(texts)) != len(texts):
                errs.append('Q%d options en double' % n)
            keytext = sd(next(o['text'] for o in q['options'] if o['id'] == q['correctOption']))
            others = [x for x, o in zip(texts, q['options']) if o['id'] != q['correctOption']]
            if all(len(x) < len(keytext) for x in others):
                errs.append('Q%d clé strictement la plus longue (%d vs %s)' % (n, len(keytext), [len(x) for x in others]))
            # même mesure que content:tranche (longueur BRUTE, diacritiques compris)
            raw = {o['id']: len(re.sub(r'\s+', ' ', nosvg(o['text'])).strip()) for o in q['options']}
            rk = raw[q['correctOption']]
            if all(v < rk for i, v in raw.items() if i != q['correctOption']):
                errs.append('Q%d clé strictement la plus longue en longueur BRUTE (tranche) : %s' % (n, raw))
        if t == 'multi':
            c = q['answerKey']['correct']
            if not (2 <= len(c) <= 5 and len(c) < len(q['options'])):
                errs.append('Q%d multi : sous-ensemble propre 2-5 exigé' % n)
    return errs


def write_mission(chapter, filename, title, difficulty, displayOrder, questions):
    assert difficulty in (2, 3, 4)
    mode, xp, coins = {2: ('practice', 75, 15), 3: ('boss', 120, 30), 4: ('challenge', 300, 60)}[difficulty]
    m = {'title': title, 'difficulty': difficulty, 'mode': mode, 'xpReward': xp, 'rewardCoins': coins,
         'displayOrder': displayOrder, 'questions': questions}
    errs = check_mission(m)
    path = '%s/%s/exercices/%s' % (BASE, chapter, filename)
    if errs:
        print('ERREURS DE CONTRÔLE (%s) :' % filename)
        for e in errs:
            print('  -', e)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(m, f, ensure_ascii=False, indent=2)
        f.write('\n')
    print('écrit :', path, '| questions :', len(questions), '| rampe :', [q['difficulty'] for q in questions])
    return path


# ---------------------------------------------------------------- SVG
def f(x):
    return ('%.1f' % x).rstrip('0').rstrip('.')


def svg(w, h, title, body):
    return '<svg viewBox="0 0 %s %s"><title>%s</title><rect x="0" y="0" width="%s" height="%s" fill="#ffffff"/>%s</svg>' % (
        f(w), f(h), title, f(w), f(h), body)


def label(x, y, txt, size=11, fill='#0f172a', anchor='middle', weight=700):
    return ('<text x="%s" y="%s" text-anchor="%s" font-size="%s" font-weight="%d" fill="%s" paint-order="stroke" '
            'stroke="#ffffff" stroke-width="3" stroke-linejoin="round">%s</text>') % (f(x), f(y), anchor, f(size), weight, fill, txt)
