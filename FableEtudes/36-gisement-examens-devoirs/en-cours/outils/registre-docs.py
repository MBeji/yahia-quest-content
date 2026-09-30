"""Synchronise les documents d'un registre (étude 36, D-3) avec le dossier de travail.
Usage : registre-docs.py <gisement.json> <dossier-couple>
Pour chaque examen ayant une transcription officielle (officiel/<id>.md) : statut « lu »,
sha256 / lecture pris de l'en-tête, pages / programme du .meta si présent, lignes = nombre de
lignes du .tsv, transcription « versionnee »."""
import json, sys, os, re
p, G = sys.argv[1], sys.argv[2]
raw = open(p, encoding='utf-8').read(); d = json.loads(raw)
assert json.dumps(d, ensure_ascii=False, indent=1) + '\n' == raw, 'format non reproduit'
def header(md):
    t = open(md, encoding='utf-8').read()
    m = re.match(r'---\n(.*?)\n---', t, re.S)
    return dict(l.split(':', 1) for l in m.group(1).split('\n') if ':' in l) if m else {}
def meta(path):
    return dict(l.split(':', 1) for l in open(path, encoding='utf-8').read().split('\n') if ':' in l) if os.path.exists(path) else {}
n = 0
for x in d['documents']:
    if x['nature'] != 'examen': continue
    md = f"{G}/officiel/{x['id']}.md"
    if not os.path.exists(md): continue
    h = {k.strip(): v.strip() for k, v in header(md).items()}
    m = {k.strip(): v.strip() for k, v in meta(f"{G}/lines/{x['id']}.meta").items()}
    x['sha256'] = h.get('sha256', x.get('sha256'))
    x['lecture'] = h.get('lecture', x.get('lecture'))
    if m.get('pages'): x['pages'] = int(m['pages'])
    if m.get('programme'): x['programme'] = m['programme']
    tsv = f"{G}/lines/{x['id']}.tsv"
    if os.path.exists(tsv): x['lignes'] = len([l for l in open(tsv, encoding='utf-8').read().split('\n') if l.strip()])
    x['statut'] = 'lu'; x['transcription'] = 'versionnee'
    order = ['id', 'nature', 'examen', 'filiere', 'session', 'page', 'fichier', 'sha256', 'pages', 'lecture', 'programme', 'statut', 'lignes', 'transcription']
    new = {k: x[k] for k in order if k in x}; new.update({k: v for k, v in x.items() if k not in new})
    x.clear(); x.update(new); n += 1
open(p, 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, indent=1) + '\n')
import collections
print(n, 'examens synchronisés ;', dict(collections.Counter((x['nature'], x.get('statut')) for x in d['documents'])))
