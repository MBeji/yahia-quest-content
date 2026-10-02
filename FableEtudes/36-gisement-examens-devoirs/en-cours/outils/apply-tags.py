"""Passe unique de création des étiquettes d'erreur d'un lot d'examens (étude 36).
Usage : apply-tags.py <racine du dépôt corpus> <pending.json> [<pending.json> …] [--write]
Chaque pending.json : {"lot","chapitre","matiere"?,"nouvelles":{id:{competency?,fr,en,ar}},"options":[{file,q,opt,id,remplace?,texte?}]}
`matiere` : « math » (défaut) ou « sciences-vie-terre » (dossier content/<matiere>/, sujet « bio » du registre ; pas de compétence en SVT).
Crée les entrées absentes de content/misconceptions.json (mise en forme identique, ordre alphabétique conservé si le fichier l'est),
puis pose les étiquettes sur les options (file = préfixe à deux chiffres du fichier dans le chapitre du lot)."""
import json, sys, glob, os, collections
# matière du pending -> (sujet du registre d'étiquettes)
REGSUBJ = {'math': 'math', 'sciences-vie-terre': 'bio'}
args = [a for a in sys.argv[1:] if not a.startswith('--')]; write = '--write' in sys.argv
root, pend = args[0], args[1:]
mp = root + '/content/misconceptions.json'
raw = open(mp, encoding='utf-8').read(); reg = json.loads(raw)
ind = 2 if '\n  "' in raw else 1
assert json.dumps(reg, ensure_ascii=False, indent=ind) + ('\n' if raw.endswith('\n') else '') == raw, 'format du registre non reproduit'
def comps(rs):
    f = root + '/content/competences/%s.json' % rs
    return {c['id'] for c in json.load(open(f, encoding='utf-8'))['competencies']} if os.path.exists(f) else set()
keys = list(reg.keys()); sorted_before = keys == sorted(keys)
created, wired, problems = [], 0, []
files = {}
for pj in pend:
    d = json.load(open(pj, encoding='utf-8'))
    mat = d.get('matiere', 'math'); rs = REGSUBJ[mat]; comp = comps(rs)
    for tid, t in d['nouvelles'].items():
        if tid in reg: continue
        if rs != 'math': assert tid.startswith(rs + '.'), ('préfixe inattendu', tid)
        if t.get('competency'): assert t['competency'] in comp, ('compétence inconnue', tid, t['competency'])
        reg[tid] = {'subject': rs, 'labels': {'fr': t['fr'], 'en': t['en'], 'ar': t['ar']}}
        if t.get('competency'): reg[tid]['competency'] = t['competency']   # sans compétence (erreur transversale) : comme reponse-a-l-autre-inconnue
        created.append(tid)
    for o in d['options']:
        g = glob.glob('%s/content/%s/%s/quiz.json' % (root, mat, d['chapitre'])) if o['file'] == 'quiz' else glob.glob('%s/content/%s/%s/exercices/%s-*.json' % (root, mat, d['chapitre'], o['file']))
        if len(g) != 1: problems.append(('fichier', d['lot'], o)); continue
        p = g[0]
        if p not in files: files[p] = json.load(open(p, encoding='utf-8'))
        q = files[p]['questions'][o['q'] - 1]
        op = [x for x in q['options'] if x['id'] == o['opt']]
        if len(op) != 1: problems.append(('option', d['lot'], o)); continue
        op = op[0]
        if o.get('texte') and o['texte'] != op['text']: problems.append(('texte différent', d['lot'], o, op['text'])); continue
        if o.get('remplace') and op.get('misconceptionTag') != o['remplace']: problems.append(('étiquette actuelle différente', d['lot'], o, op.get('misconceptionTag'))); continue
        assert o['id'] in reg, o['id']
        op['misconceptionTag'] = o['id']; wired += 1
if sorted_before: reg = dict(sorted(reg.items()))
print('créées :', len(created), created); print('posées :', wired); print('problèmes :', len(problems))
for pr in problems: print('  ', pr)
if write and not problems:
    open(mp, 'w', encoding='utf-8').write(json.dumps(reg, ensure_ascii=False, indent=ind) + ('\n' if raw.endswith('\n') else ''))
    for p, d in files.items():
        r = open(p, encoding='utf-8').read(); i2 = 2 if '\n  "' in r else None
        open(p, 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, indent=i2) + ('\n' if r.endswith('\n') else ''))
    print('écrit.')
