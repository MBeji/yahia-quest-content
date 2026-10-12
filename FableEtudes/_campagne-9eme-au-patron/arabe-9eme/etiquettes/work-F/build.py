import json,collections
exec(open('/home/user/wt-arabe/FableEtudes/_campagne-9eme-au-patron/arabe-9eme/etiquettes/work-F/fusion.py').read())
errs=[]
# ---- assignments
fileof=lambda ch,f: dict(files_of(ch))[f]
seen={}; AFF=[]
for a in FIN:
    Q=qs(a['ch']).get((a['f'],a['q']))
    if Q is None: errs.append(('noq',a)); continue
    ids=[x['id'] for x in Q['options']]
    if a['o'] not in ids: errs.append(('noopt',a)); continue
    if a['o']==Q['correctOption']: errs.append(('KEY',a)); continue
    k=(a['ch'],a['f'],a['q'],a['o'])
    if k in seen: errs.append(('dup',k,seen[k],a['id'])); continue
    seen[k]=a['id']
    if label(a['id']) is None: errs.append(('nolabel',a['id']))
    AFF.append(dict(chapitre=CHDIR[a['ch']],fichier=fileof(a['ch'],a['f']),q=a['q'],opt=a['o'],tag=a['id']))
order={'quiz.json':0}
AFF.sort(key=lambda x:(x['chapitre'],order.get(x['fichier'],1),x['fichier'],x['q'],x['opt']))
used={x['tag'] for x in AFF}
# ---- coursePitfalls
CPF={}; PGREPORT={}
for ch in sorted(CHDIR):
    pgs=pieges(ch); lst=[]; rep=[]
    for k in range(1,len(pgs)+1):
        ids=sorted(PGF.get((ch,k),set()))
        carried=[i for i in ids if any(x['tag']==i and x['chapitre']==CHDIR[ch] for x in AFF)]
        rep.append((k,ids,carried))
        for i in carried:
            if i not in lst: lst.append(i)
    CPF[CHDIR[ch]]=lst; PGREPORT[ch]=rep
# ---- new vocab
new=sorted(i for i in used|{i for v in CPF.values() for i in v} if i not in REG)
for i in new:
    if not re.fullmatch(r'arabe\.[a-z0-9]+\.[a-z0-9-]+',i): errs.append(('badid',i))
    for l in ('ar','fr','en'):
        if len(label(i)[l])>160: errs.append(('long',i,l))
VOC={i:{'subject':'arabe','labels':{l:label(i)[l] for l in ('ar','fr','en')}} for i in new}
# threshold for new ids
byid=collections.defaultdict(set)
for x in AFF: byid[x['tag']].add((x['chapitre'],x['fichier'],x['q']))
pgids={i for v in PGF.values() for i in v}
low=[i for i in new if len(byid[i])<3 and i not in pgids]
unused=[i for i in new if i not in used]
if __name__=='__main__':
    json.dump(VOC,open(E+'/vocab-arabe9.json','w'),ensure_ascii=False,indent=2); open(E+'/vocab-arabe9.json','a').write('\n')
    with open(E+'/affectations-arabe9.json','w') as f:
        f.write('[\n'+',\n'.join('  '+json.dumps(x,ensure_ascii=False) for x in AFF)+'\n]\n')
    json.dump(CPF,open(E+'/coursePitfalls-arabe9.json','w'),ensure_ascii=False,indent=2); open(E+'/coursePitfalls-arabe9.json','a').write('\n')
    print('errors',len(errs)); [print(e) for e in errs[:30]]
    print('new',len(new),'reused',len(used-set(new)),'aff',len(AFF),'LOW',low,'UNUSED',unused)
