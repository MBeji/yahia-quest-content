"""Écrit une affectation par lot d'examen (étude 36, G5) à partir du plan et des transcriptions."""
import json, sys, os, glob, re
SP = '/tmp/claude-0/-home-user/b03814da-e5f9-5a74-bf03-e7c23b20207a/scratchpad'
plan = json.load(open(sys.argv[1], encoding='utf-8'))
lots = sys.argv[2].split(',')
off = f'{SP}/gisement/9eme-math/officiel'
name = {}
for f in glob.glob(f'{off}/*.md'):
    t = open(f, encoding='utf-8').read()
    y = re.search(r'^session:\s*(\S+)', t, re.M).group(1)
    fl = re.search(r'^filiere:\s*(\S+)', t, re.M).group(1)
    name[os.path.basename(f)[:-3]] = y if fl == 'unique' else f'{y}-{fl}'
M = {m['id']: m for m in plan['missions']}
for L in plan['lots']:
    if L['id'] not in lots: continue
    out = []
    for mid in L['missions']:
        m = M[mid]
        (src,) = m['sources']
        cid, ex = src.split('#')
        sess = name[cid]
        out.append(f"- session **{sess}** (`content/programmes-officiels/examens-nationaux/9eme-base/math/{sess}.md`), "
                   f"exercice **{ex}** → chapitre `{m['chapter']}`, fichier `exercices/{m['nn']:02d}-examen-{sess}-ex{ex}-<slug>.json`, "
                   f"`displayOrder` {m['nn']} — étage **{m['etage']}**, {m['etapes']} étapes ; compétences `{'+'.join(m['competences'])}` ; "
                   f"archétype (du lecteur) : « {m['archetype']} » ; piège (du lecteur) : « {m['piege']} »")
    p = f"{SP}/author/exam/assign-{L['id']}.md"
    open(p, 'w', encoding='utf-8').write('\n'.join(out) + '\n')
    print(p, len(out))
