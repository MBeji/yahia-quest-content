"""Écrit une affectation par lot d'examen (étude 36, G5) pour une matière quelconque.
Usage : gen-exam-assign-subj.py <plan.json> <lots,…> <dossier-officiel> <matière-dossier-examens> <préfixe> [<classe>]
  dossier-officiel : transcriptions de travail (C01.md …), matière-dossier-examens : nom du dossier sous examens-nationaux/<classe>/.
Le fichier d'affectation est écrit dans author/exam/assign-<préfixe><lot>.md. Une session vaut l'année seule quand
la filière est unique cette année-là, sinon <année>-<filière>."""
import json, sys, os, glob, re, collections
SP = '/tmp/claude-0/-home-user/b03814da-e5f9-5a74-bf03-e7c23b20207a/scratchpad'
plan = json.load(open(sys.argv[1], encoding='utf-8'))
lots = sys.argv[2].split(',')
off, subj, pre = sys.argv[3], sys.argv[4], sys.argv[5]
classe = sys.argv[6] if len(sys.argv) > 6 else '9eme-base'
docs = {}
for f in glob.glob(f'{off}/*.md'):
    t = open(f, encoding='utf-8').read()
    docs[os.path.basename(f)[:-3]] = (re.search(r'^session:\s*(\S+)', t, re.M).group(1), re.search(r'^filiere:\s*(\S+)', t, re.M).group(1))
per_year = collections.Counter(y for y, _ in docs.values())
name = {c: (y if per_year[y] == 1 or fl == 'unique' else f'{y}-{fl}') for c, (y, fl) in docs.items()}
M = {m['id']: m for m in plan['missions']}
for L in plan['lots']:
    if L['id'] not in lots: continue
    out = []
    for mid in L['missions']:
        m = M[mid]
        for src in m['sources']:
            cid, ex = src.split('#')
        cid, ex = m['sources'][0].split('#')
        sess = name[cid]
        out.append(f"- session **{sess}** (`content/programmes-officiels/examens-nationaux/{classe}/{subj}/{sess}.md`), "
                   f"exercice **{ex}** → chapitre `{m['chapter']}`, fichier `exercices/{m['nn']:02d}-examen-{sess}-ex{ex}-<slug>.json`, "
                   f"`displayOrder` {m['nn']} — étage **{m['etage']}**, {m['etapes']} étapes ; "
                   f"archétype (du lecteur) : « {m['archetype']} » ; piège (du lecteur) : « {m['piege']} »")
    p = f"{SP}/author/exam/assign-{pre}{L['id']}.md"
    open(p, 'w', encoding='utf-8').write('\n'.join(out) + '\n')
    print(p, len(out))
