import json,collections
exec(open('/home/user/wt-arabe/FableEtudes/_campagne-9eme-au-patron/arabe-9eme/etiquettes/work-F/build.py').read().split("if __name__")[0])
vA=json.load(open(E+'/vocab-arabe9-A.json')); vB=json.load(open(E+'/vocab-arabe9-B.json'))
out=[]; P=out.append
# origin of each final new id
def src(i):
    s=set()
    if i in vA: s.add('A')
    if i in vB: s.add('B')
    if i in NEWC: s.add('compl.')
    if i in NEWD: s.add('fusion')
    for o,n in RENAME.items():
        if R(o)==i:
            if o in vA: s.add('A')
            if o in vB: s.add('B')
            if o in NEWC: s.add('compl.')
    return '+'.join(sorted(s))
cnt=collections.Counter(src(i) for i in new)
P(f"- **Ids neufs retenus : {len(new)}** (origine : " + ', '.join(f'{k} {v}' for k,v in sorted(cnt.items()))+").")
P(f"- **Ids du registre réutilisés : {len(used-set(new))}** : " + ', '.join(f'`{i}`' for i in sorted(used-set(new)))+'.')
dist=sum(len(q['options'])-1 for ch in CHDIR for q in qs(ch).values()); qn=sum(len(qs(ch)) for ch in CHDIR)
P(f"- **Options posées : {len(AFF)}** sur {dist} distracteurs des 19 chapitres (**{100*len(AFF)/dist:.1f} %**), sur {len({(x['chapitre'],x['fichier'],x['q']) for x in AFF})} questions sur {qn}.")
before=len(vA)+len(vB)+len(NEWC)
gone=sorted(o for o in RENAME if o in vA or o in vB or o in NEWC)
P(f"- Avant fusion : A {len(vA)} + B {len(vB)} + compléments 02/03/19 {len(NEWC)} = {before} ids neufs ; {len(gone)} absorbés par fusion, {len(NEWD)} créés par scission → {len(new)}.")
P('')
P('### Répartition par chapitre\n')
P('| chapitre | questions | distracteurs | options posées | % | `piege` du cours | pièges portés | `coursePitfalls` |'); P('| --- | --- | --- | --- | --- | --- | --- | --- |')
for ch in sorted(CHDIR):
    d=sum(len(q['options'])-1 for q in qs(ch).values()); t=sum(1 for x in AFF if x['chapitre']==CHDIR[ch])
    rep=PGREPORT[ch]
    P(f"| {CHDIR[ch]} | {len(qs(ch))} | {d} | {t} | {100*t//d} % | {len(rep)} | {sum(1 for _,_,c in rep if c)} | {len(CPF[CHDIR[ch]])} |")
P('')
P('### Ids neufs retenus seulement par un `piege` (moins de 3 questions)\n')
low=[(i,len(byid[i])) for i in new if len(byid[i])<3]
P(', '.join(f'`{i}` ({n} Q)' for i,n in low)+f' — {len(low)} ids, tous énoncés par un piège du cours et portés dans le chapitre de ce piège (C-5).')
open('/tmp/claude-0/-home-user-yahia-quest-content/973107ae-1cd3-5286-9aad-458ef39f3138/scratchpad/f/tables.md','w').write('\n'.join(out))
# label before/after for LABO
L=[]
for i,(ar,fr,en) in LABO.items():
    olds=[o for o,n in RENAME.items() if R(o)==i]+[i]
    for o in olds:
        lb=(vA.get(o) or vB.get(o) or ({'labels':dict(zip(('ar','fr','en'),NEWC[o]))} if o in NEWC else None))
        if lb: L.append(f"- `{o}` (avant) : {lb['labels']['fr']}")
    L.append(f"  - **après `{i}`** : {fr}")
open('/tmp/claude-0/-home-user-yahia-quest-content/973107ae-1cd3-5286-9aad-458ef39f3138/scratchpad/f/labels.md','w').write('\n'.join(L))
print(open('/tmp/claude-0/-home-user-yahia-quest-content/973107ae-1cd3-5286-9aad-458ef39f3138/scratchpad/f/tables.md').read())
print(len(MUTE),'mutes',len(RETAG),'retags')
