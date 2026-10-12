# -*- coding: utf-8 -*-
"""Builds the two deliverables of brief-vocab-A from data_A.py (+ the real corpus for excerpts)."""
import json, os, re, glob, sys, collections

W = '/tmp/claude-0/-home-user/8ff73c67-6eab-5a69-a66d-d237b8d69142/scratchpad/ar9/tags'
BASE = '/home/user/yahia-quest-content/content/arabic'
REG = '/home/user/yahia-quest-content/content/misconceptions.json'

CH = {  # short key -> dir
 '15': '15-al-alaqat-bayna-al-jumal', '04': '04-al-asalib', '16': '16-al-istifham', '17': '17-ash-shart',
 '18': '18-dalalat-az-zaman', '02': '02-an-nawasikh', '03': '03-al-mansoubat', '19': '19-al-adad-wal-madud'}
ORDER = ['15', '04', '16', '17', '18', '02', '03', '19']

ns = {}
exec(open(os.path.join(W, 'work-A', 'data_A.py'), encoding='utf-8').read(), ns)
IDS = ns['IDS']
CHAPTERS = ns.get('CHAPTERS', {})
PRECEDENCE = ns.get('PRECEDENCE', [])
PIEGES = ns.get('PIEGES', {})
NOID_REASON = ns.get('NOID_REASON', {})
UNDER3 = ns.get('UNDER3', [])
DOUBTS = ns.get('DOUBTS', [])
STATUS = ns.get('STATUS', '')

registry = json.load(open(REG, encoding='utf-8'))

# label overrides (authoritative when present)
_ovp = os.path.join(W, 'work-A', 'labels_override_A.json')
if os.path.exists(_ovp):
    for _i, _d in json.load(open(_ovp, encoding='utf-8')).items():
        if _i in IDS:
            IDS[_i].update(_d)
        else:
            print('WARNING override for unknown id', _i)

# ---- load corpus
corpus = {}
def load(ch, fk):
    key = (ch, fk)
    if key in corpus: return corpus[key]
    d = CH[ch]
    if fk == 'quiz':
        f = os.path.join(BASE, d, 'quiz.json')
    else:
        g = glob.glob(os.path.join(BASE, d, 'exercices', fk + '-*.json'))
        assert len(g) == 1, (ch, fk, g)
        f = g[0]
    corpus[key] = json.load(open(f, encoding='utf-8'))['questions']
    return corpus[key]

def opt_text(ch, fk, q, o):
    qs = load(ch, fk)
    qq = qs[q - 1]
    for op in qq['options']:
        if op['id'] == o:
            assert qq['correctOption'] != o, f'carrier is the CORRECT option: {ch} {fk}#{q}->{o}'
            return op['text']
    raise KeyError((ch, fk, q, o))

errors = []
# ---- validate ids / labels
idre = re.compile(r'^arabe\.[a-z0-9]+\.[a-z0-9-]+$')
for i, v in IDS.items():
    if not idre.match(i): errors.append('bad id format ' + i)
    if v['new']:
        if i in registry: errors.append('NEW id already in registry: ' + i)
        for l in ('ar', 'fr', 'en'):
            if len(v[l]) > 160: errors.append(f'{i} {l} too long ({len(v[l])})')
            if not v[l].strip(): errors.append(f'{i} {l} empty')
    else:
        if i not in registry: errors.append('REUSED id missing from registry: ' + i)


def pg_text(ch, ks):
    r = []
    for k in ks:
        sec, quote = PIEGES[ch][k]
        r.append(f"n°{k} ({sec}) « {quote} »")
    return ' ; '.join(r)

# every piege must be linked to an id or explicitly declared without id
linked = set()
for i, v in IDS.items():
    for u in v.get('uses', []):
        for k in u.get('pg', []):
            if k not in PIEGES.get(u['ch'], {}): errors.append(f'{i}: unknown piege {u["ch"]}/{k}')
            linked.add((u['ch'], k))
for ch, d in PIEGES.items():
    for k in d:
        if (ch, k) not in linked and (ch, k) not in NOID_REASON:
            errors.append(f'piege {ch}/{k} neither linked nor declared sans-id')
        if (ch, k) in linked and (ch, k) in NOID_REASON:
            errors.append(f'piege {ch}/{k} both linked and declared sans-id')

# ---- usage index
def qkey(u): return (u[0], u[1], u[2])
usage = collections.defaultdict(lambda: collections.defaultdict(list))  # id -> ch -> carriers
for i, v in IDS.items():
    for u in v.get('uses', []):
        ch = u['ch']
        for c in u.get('carriers', []):
            f, q, o = c[0], c[1], c[2]
            note = c[3] if len(c) > 3 else ''
            try:
                t = opt_text(ch, f, q, o)
            except Exception as e:
                errors.append(f'{i}: {e}')
                t = '???'
            usage[i][ch].append((f, q, o, note, t))

def nq(i):
    s = set()
    for ch, cs in usage[i].items():
        for (f, q, o, n, t) in cs: s.add((ch, f, q))
    return len(s)

def carriers_in(i, ch):
    return usage[i].get(ch, [])

# a tag may be used on one option only once overall
seen = {}
for i in IDS:
    for ch, cs in usage[i].items():
        for (f, q, o, n, t) in cs:
            k = (ch, f, q, o)
            if k in seen and seen[k] != i:
                errors.append(f'option {k} claimed by two ids: {seen[k]} and {i}')
            seen[k] = i

# ---- write JSON (new ids only)
out = {}
for i, v in IDS.items():
    if v['new']:
        out[i] = {'subject': 'arabe', 'labels': {'ar': v['ar'], 'fr': v['fr'], 'en': v['en']}}
with open(os.path.join(W, 'vocab-arabe9-A.json'), 'w', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
    f.write('\n')
# re-parse to check validity
json.load(open(os.path.join(W, 'vocab-arabe9-A.json'), encoding='utf-8'))

# ---- write map
def short(t, n=70):
    t = t.replace('\n', ' ')
    return t if len(t) <= n else t[:n - 1] + '…'

L = []
A = L.append
A('# Carte d\'usage — vocabulaire d\'erreurs de l\'arabe 9ᵉ, PARTIE A (grammaire 101908, 8 chapitres)')
A('')
A(f'> Statut : {STATUS}')
A('')
A('Livrable jumeau : `vocab-arabe9-A.json` (ids NEUFS seulement). Ce fichier est généré à partir d\'un jeu de données unique ; chaque distracteur cité a été relu dans le corpus (l\'extrait est celui du JSON, pas une recopie à la main).')
A('')
A('## 0. Conventions')
A('')
A('- **Référence d\'un distracteur** : `CC:F#N→o` = chapitre `CC` (15, 04, 16, 17, 18, 02, 03, 19), fichier `F` (`quiz` = `quiz.json` ; `01`…`06` = le préfixe numérique du fichier de `exercices/`), question `N` (rang **1-based dans le fichier**, qui est aussi le `qN` du compilateur : tous les fichiers sont déjà triés par `difficulty`), option `o` (`a`…`d`).')
A('- Les 8 chapitres ont chacun 35 questions (quiz 5 + 5 exercices × 6), toutes `mcq`, **aucune option n\'est encore taguée**.')
A('- « Porte » : le distracteur est **reconstructible** (portes R1/R2/R3 du schéma) pour cet id. Un distracteur n\'est cité que pour UN id (le script refuse un doublon) ; les cas où deux ids se touchent sont arbitrés au §3.')
A('- « Q » = nombre de questions DISTINCTES qui ont au moins un distracteur porteur (seuil du registre : ≥ 3, ou un `piege` du cours).')
A('- Les libellés sont dans `vocab-arabe9-A.json` ; la colonne « libellé » ci-dessous ne donne que l\'arabe, pour relecture rapide.')
A('')

# synthèse
A('## 1. Synthèse des ids')
A('')
news = [i for i, v in IDS.items() if v['new']]
reus = [i for i, v in IDS.items() if not v['new']]
A(f'**{len(news)} ids neufs, {len(reus)} ids réutilisés** à ce stade ({STATUS}).')
A('')
A('| id | statut | chapitres | Q | `piege` |')
A('| --- | --- | --- | --- | --- |')
def chapters_of(i):
    return sorted({u['ch'] for u in IDS[i].get('uses', [])}, key=lambda c: ORDER.index(c))
def pieges_of(i):
    r = []
    for u in IDS[i].get('uses', []):
        if u.get('pg'): r.append(f"{u['ch']}: n°" + ','.join(str(k) for k in u['pg']))
    return r
for i in sorted(IDS, key=lambda x: (x.split('.')[1], x)):
    v = IDS[i]
    A(f"| `{i}` | {'neuf' if v['new'] else 'réutilisé'} | {', '.join(chapters_of(i))} | {nq(i)} | {'; '.join(pieges_of(i)) or '—'} |")
A('')

# fiches
A('## 2. Fiches par id')
A('')
cur = None
for i in sorted(IDS, key=lambda x: (x.split('.')[1], x)):
    v = IDS[i]
    dom = i.split('.')[1]
    if dom != cur:
        A(f'### Domaine `{dom}`')
        A('')
        cur = dom
    A(f"#### `{i}` — {'NEUF' if v['new'] else 'RÉUTILISÉ'}")
    A('')
    if v['new']:
        A(f"- **AR** : {v['ar']}")
        A(f"- **FR** : {v['fr']}")
        A(f"- **EN** : {v['en']}")
    else:
        A(f"- **AR** (registre) : {registry[i]['labels']['ar']}")
        if v.get('why_reused'): A(f"- **Pourquoi réutilisé** : {v['why_reused']}")
    A(f"- **Chapitres / piège** : " + (' | '.join(
        f"ch{u['ch']} — piège " + pg_text(u['ch'], u['pg']) + (f" [moitié couverte : {u['half']}]" if u.get('half') else '') if u.get('pg') else f"ch{u['ch']} — (pas de piège ; erreur récurrente dans les items)"
        for u in v.get('uses', [])) or '—'))
    A(f"- **Q distinctes** : {nq(i)}")
    A('- **Distracteurs porteurs** :')
    for ch in ORDER:
        for (f, q, o, n, t) in carriers_in(i, ch):
            A(f"  - `{ch}:{f}#{q}→{o}` « {short(t)} »" + (f" — {n}" if n else ''))
    if v.get('note'): A(f"- **Note** : {v['note']}")
    A('')

# precedence
A('## 3. Règles de précédence (quand deux ids se touchent)')
A('')
for p in PRECEDENCE: A(f'- {p}')
A('')

A('## 4. Pièges sans id')
A('')
A('| chapitre | piège | raison |')
A('| --- | --- | --- |')
for ch in ORDER:
    for k in sorted(PIEGES.get(ch, {})):
        if (ch, k) in NOID_REASON:
            sec, quote = PIEGES[ch][k]
            A(f'| {ch} | n°{k} ({sec}) « {quote} » | {NOID_REASON[(ch, k)]} |')
A('')

A('## 5. Erreurs vues < 3 fois (non retenues)')
A('')
for (title, carriers, why) in UNDER3:
    A(f'- **{title}** — {carriers} — {why}')
A('')

# coursePitfalls
A('## 6. `coursePitfalls` proposés par chapitre')
A('')
A('Colonne C-5 : ✓ = au moins un distracteur du chapitre porte l\'id (cité au §2) ; ✗ = aucun.')
A('')
for ch in ORDER:
    if ch not in PIEGES: continue
    cp = []
    for i, v in IDS.items():
        for u in v.get('uses', []):
            if u['ch'] == ch and u.get('pg') and i not in cp: cp.append((min(u['pg']), i))
    cp = [i for (_, i) in sorted(cp)]
    A(f'### Chapitre {ch} — `{CH[ch]}`')
    A('')
    if not cp:
        A('**Aucun candidat** — aucun piège du cours n\'est porté par un distracteur.')
        A('')
        continue
    A('| id | C-5 (porté par un distracteur du chapitre ?) | piège du cours qui l\'énonce | porteurs dans ce chapitre |')
    A('| --- | --- | --- | --- |')
    for i in cp:
        cs = carriers_in(i, ch)
        ok = '✓' if cs else '✗'
        pg = [pg_text(ch, u['pg']) for u in IDS[i]['uses'] if u['ch'] == ch and u.get('pg')]
        A(f"| `{i}` | {ok} | {'; '.join(pg)} | " + ', '.join(f'{ch}:{f}#{q}→{o}' for (f, q, o, n, t) in cs) + ' |')
        if not cs: errors.append(f'C-5 fails: {ch} {i}')
    A('')
    if CHAPTERS.get(ch, {}).get('remark'): A(CHAPTERS[ch]['remark']); A('')

A('## 7. Couverture et doutes')
A('')
for d in DOUBTS: A(f'- {d}')
A('')

open(os.path.join(W, 'map-arabe9-A.md'), 'w', encoding='utf-8').write('\n'.join(L))

# ---- report
print('new ids:', len(news), ' reused:', len(reus))
tot_tagged = len(seen)
print('distinct tagged options so far:', tot_tagged)
if errors:
    print('ERRORS:')
    for e in errors: print('  -', e)
    sys.exit(1)
print('OK')
