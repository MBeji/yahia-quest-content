"""Génère la spec registre-add d'un lot d'examen : gen-spec-lot.py <lot> <worktree> > spec.json"""
import json, sys, glob, os
SP = '/tmp/claude-0/-home-user/b03814da-e5f9-5a74-bf03-e7c23b20207a/scratchpad'
lot, wt = sys.argv[1], sys.argv[2]
plan = json.load(open(SP + '/gisement/9eme-math/plan-examens-v6.json', encoding='utf8'))
out = []
for m in plan['missions']:
    if m['lot'] != lot: continue
    files = glob.glob('%s/content/math/%s/exercices/%02d-*.json' % (wt, m['chapter'], m['nn']))
    assert len(files) == 1, (m['id'], files)
    d = json.load(open(files[0], encoding='utf8'))
    etage = {2: 'd2', 3: 'd3', 4: 'd4'}[{'practice': 2, 'boss': 3, 'challenge': 4}.get(d['mode'], 0)] if d.get('mode') in ('practice', 'boss', 'challenge') else m['etage']
    out.append({'id': m['sources'][0], 'sources': m['sources'], 'chapitre': m['chapter'], 'fichier': os.path.basename(files[0]),
                'etage': etage, 'etapes': len(d['questions']), 'lot': lot, 'statut': 'mergee'})
print(json.dumps(out, ensure_ascii=False, indent=1))
