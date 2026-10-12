import json,re,collections,sys
exec(open('/home/user/wt-arabe/FableEtudes/_campagne-9eme-au-patron/arabe-9eme/etiquettes/work-F/load.py').read())
WF=E+'/work-F'
exec(open(WF+'/data_compl.py').read())
exec(open(WF+'/decisions.py').read())
for i,l in NEWD.items(): LAB[i]=dict(zip(('ar','fr','en'),l)); ORIG[i]='fusion'
for (i,ch,q,o) in ASC:
    k,n=q.split('#'); ASSIGN.append(dict(id=i,ch=ch,f=k,q=int(n),o=o,note='',src='F'))
for ch,d in PGC.items():
    for k,ids in d.items():
        for i in ids: PGL[(ch,k)].add(i)
for i,l in NEWC.items(): LAB[i]=dict(zip(('ar','fr','en'),l)); ORIG[i]='F'
def R(i):
    seen=set()
    while i in RENAME and i not in seen: seen.add(i); i=RENAME[i]
    return i
# apply renames/drops/mutes/retags
FIN=[]
for a in ASSIGN:
    a=dict(a); a['orig_id']=a['id']; a['id']=R(a['id'])
    key=(a['ch'],f"{a['f']}#{a['q']}",a['o'])
    if key in MUTE: continue
    if key in RETAG: a['id']=RETAG[key][0]
    if a['id'] in DROP: continue
    FIN.append(a)
# retags may target options not in ASSIGN
have={(a['ch'],f"{a['f']}#{a['q']}",a['o']) for a in FIN}
for key,(i,why) in RETAG.items():
    if key not in have and i not in DROP:
        k,n=key[1].split('#'); FIN.append(dict(id=i,orig_id=None,ch=key[0],f=k,q=int(n),o=key[2],note=why,src='F'))
PGF=collections.defaultdict(set)
for (ch,k),ids in PGL.items():
    for i in ids:
        j=R(i)
        if j not in DROP: PGF[(ch,k)].add(j)
def label(i):
    if i in LABO: return dict(zip(('ar','fr','en'),LABO[i]))
    if i in LAB: return LAB[i]
    if i in REG: return REG[i]['labels']
    return None
def origin(i):
    if i in REG: return 'registre'
    srcs={ORIG.get(o) for o,n in RENAME.items() if R(o)==i}|{ORIG.get(i)}
    srcs.discard(None); return '+'.join(sorted(srcs)) or '?'
