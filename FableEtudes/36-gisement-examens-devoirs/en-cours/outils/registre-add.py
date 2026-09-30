"""Ajoute (idempotent) des missions d'examen au registre d'un couple (étude 36, D-3).
Usage : registre-add.py <gisement.json> <spec.json>
spec = [{"id","sources":[...],"chapitre","fichier","etage","etapes","lot","statut"}, ...]"""
import json, sys, collections
p, spec = sys.argv[1], json.load(open(sys.argv[2], encoding='utf-8'))
raw = open(p, encoding='utf-8').read(); d = json.loads(raw)
assert json.dumps(d, ensure_ascii=False, indent=1) + '\n' == raw, 'format du registre non reproduit'
ORDER = ['id', 'origine', 'sources', 'chapitre', 'fichier', 'etage', 'etapes', 'lot', 'statut', 'pr']
have = {m['id'] for m in d['missions']}
n = 0
for m in spec:
    assert m['id'] not in have, m['id']
    e = {'origine': 'examen', **m}
    d['missions'].append({k: e[k] for k in ORDER if k in e}); n += 1
open(p, 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, indent=1) + '\n')
print(n, 'mission(s) ajoutée(s) ;', dict(collections.Counter(m['statut'] for m in d['missions'])))
