# Vérification indépendante des livrables contre le corpus (ne lit que les fichiers produits + content/)
import json,os,re,glob,collections
ROOT='/home/user/wt-arabe'; E=ROOT+'/FableEtudes/_campagne-9eme-au-patron/arabe-9eme/etiquettes'
REG=json.load(open(ROOT+'/content/misconceptions.json'))
VOC=json.load(open(E+'/vocab-arabe9.json')); AFF=json.load(open(E+'/affectations-arabe9.json')); CPF=json.load(open(E+'/coursePitfalls-arabe9.json'))
err=[]
assert list(VOC)==sorted(VOC), 'vocab non trié'
for i,v in VOC.items():
    if i in REG: err.append(f'id neuf déjà au registre {i}')
    if v.get('subject')!='arabe' or set(v['labels'])!={'ar','fr','en'}: err.append(f'forme {i}')
    for l,t in v['labels'].items():
        if len(t)>160: err.append(f'>160 {i} {l}')
seen=set(); tot=collections.Counter(); tag=collections.Counter()
for x in AFF:
    p=f"{ROOT}/content/arabic/{x['chapitre']}/{x['fichier']}"
    Q=json.load(open(p))['questions'][x['q']-1]
    if x['opt'] not in [o['id'] for o in Q['options']]: err.append(f'option absente {x}')
    if x['opt']==Q['correctOption']: err.append(f'CLÉ taguée {x}')
    k=(x['chapitre'],x['fichier'],x['q'],x['opt'])
    if k in seen: err.append(f'doublon {k}')
    seen.add(k)
    if x['tag'] not in VOC and x['tag'] not in REG: err.append(f'tag inconnu {x["tag"]}')
chs=sorted(d for d in os.listdir(ROOT+'/content/arabic') if re.match(r'\d\d-',d))
assert set(CPF)==set(chs), 'coursePitfalls ne couvre pas les 19 chapitres'
dist=0; qn=0
for ch in chs:
    for f in [ROOT+f'/content/arabic/{ch}/quiz.json']+sorted(glob.glob(ROOT+f'/content/arabic/{ch}/exercices/*.json')):
        for q in json.load(open(f))['questions']: dist+=len(q['options'])-1; qn+=1
    for i in CPF[ch]:
        if i not in VOC and i not in REG: err.append(f'CP inconnu {ch} {i}')
        if not any(x['tag']==i and x['chapitre']==ch for x in AFF): err.append(f'C-5 : {ch} {i} non porté')
    if not CPF[ch]: err.append(f'chapitre sans coursePitfalls {ch}')
used=collections.Counter(x['tag'] for x in AFF)
print('erreurs',len(err)); [print(' ',e) for e in err]
print(f"ids neufs {len(VOC)} ; ids du registre réutilisés {len([i for i in used if i in REG])} ; options posées {len(AFF)} / {dist} distracteurs ({100*len(AFF)/dist:.1f} %) ; questions touchées {len({(x['chapitre'],x['fichier'],x['q']) for x in AFF})} / {qn}")
print('neufs non posés :',[i for i in VOC if i not in used])
