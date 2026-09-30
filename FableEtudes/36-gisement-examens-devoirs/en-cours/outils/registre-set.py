"""Statuts du registre d'un couple (étude 36, D-3). Usage : registre-set.py <gisement.json> <spec.json>
spec = {"missions": {"<id>": {"fichier": "...", "statut": "...", "pr": "..."}}, "lots": {"<lot>": "<statut>"}}"""
import json, sys, collections
p, spec = sys.argv[1], json.load(open(sys.argv[2], encoding='utf-8'))
raw = open(p, encoding='utf-8').read(); d = json.loads(raw)
assert json.dumps(d, ensure_ascii=False, indent=1) + '\n' == raw, 'format du registre non reproduit'
ORDER = ['id', 'origine', 'sources', 'chapitre', 'fichier', 'etage', 'etapes', 'lot', 'statut', 'pr']
M = {m['id']: m for m in d['missions']}
for mid, kw in spec.get('missions', {}).items():
    m = M[mid]; m.update(kw)
    new = {k: m[k] for k in ORDER if k in m}; new.update({k: v for k, v in m.items() if k not in new})
    m.clear(); m.update(new)
for lot, st in spec.get('lots', {}).items():
    n = 0
    for m in d['missions']:
        if m.get('lot') == lot and m['id'] not in spec.get('missions', {}):
            m['statut'] = st; n += 1
    assert n, lot
open(p, 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, indent=1) + '\n')
print(dict(collections.Counter(m['statut'] for m in d['missions'])))
