import json,re,os,glob,sys
from collections import defaultdict,OrderedDict
ROOT='/home/user/wt-arabe'
ET=ROOT+'/FableEtudes/_campagne-9eme-au-patron/arabe-9eme/etiquettes'
NEW=OrderedDict(); PG={}; ASSIGN=[]; CP={}; PREC=[]; SANS=[]; LT3=[]; NOTES=[]
def A(i,ch,q,opts,note=''):
    for o in opts: ASSIGN.append((i,ch,q,o,note))
ns=dict(NEW=NEW,PG=PG,ASSIGN=ASSIGN,CP=CP,PREC=PREC,SANS=SANS,LT3=LT3,NOTES=NOTES,A=A)
for f in sorted(glob.glob('/tmp/claude-0/s/data/data_*.py')):
    exec(open(f).read(),ns)
reg=json.load(open(ROOT+'/content/misconceptions.json'))
try: vocA=json.load(open(ET+'/vocab-arabe9-A.json'))
except Exception: vocA={}
chdir={c[:2]:c for c in os.listdir(ROOT+'/content/arabic') if re.match(r'\d\d-',c)}
cache={}
def load(ch):
    if ch in cache: return cache[ch]
    base=ROOT+'/content/arabic/'+chdir[ch]
    qs={}
    for k,f in [('quiz',base+'/quiz.json')]+[(os.path.basename(x)[:2],x) for x in sorted(glob.glob(base+'/exercices/*.json'))]:
        for i,q in enumerate(json.load(open(f))['questions'],1):
            qs[f'{k}#{i}']=q
    cours=open(base+'/cours.md').read()
    pg=[m.group(1).strip().replace('\n',' ') for m in re.finditer(r'^::: piege.*?\n(.*?)^:::',cours,re.S|re.M)]
    cache[ch]=(qs,pg); return cache[ch]
errs=[]
seen={}
byid=defaultdict(list)
for (i,ch,q,o,note) in ASSIGN:
    qs,_=load(ch)
    if q not in qs: errs.append(f'no q {ch}:{q}');continue
    Q=qs[q]
    if o not in [x['id'] for x in Q['options']]: errs.append(f'no opt {ch}:{q}{o}');continue
    if o==Q['correctOption']: errs.append(f'CORRECT option tagged {i} {ch}:{q}{o}');continue
    key=(ch,q,o)
    if key in seen: errs.append(f'double {key}: {seen[key]} / {i}');continue
    seen[key]=i
    byid[i].append((ch,q,o,note))
allids=set(byid)|{x for v in PG.values() for _,ids,_ in v for x in ids}|{x for v in CP.values() for x in v}
for i in sorted(allids):
    if not re.fullmatch(r'arabe\.[a-z0-9]+\.[a-z0-9-]+',i): errs.append('bad id '+i)
    if i in NEW:
        if i in reg: errs.append('NEW already in registry '+i)
        if i in vocA: errs.append('NEW already in A '+i)
    elif i not in reg and i not in vocA: errs.append('unknown id '+i)
for i,(ar,fr,en) in NEW.items():
    for li,l in zip('ar fr en'.split(),(ar,fr,en)):
        if len(l)>160: errs.append(f'label>160 {i} {li} {len(l)}')
for ch,v in CP.items():
    for i in v:
        if not any(c==ch for c,_,_,_ in byid.get(i,[])): errs.append(f'C-5 FAIL {ch} {i}')
def lab(i,l='fr'):
    if i in NEW: return dict(zip(('ar','fr','en'),NEW[i]))[l]
    if i in vocA: return vocA[i]['labels'][l]
    return reg[i]['labels'][l]
def short(s,n=70):
    s=s.replace('\n',' ')
    return s if len(s)<=n else s[:n]+'…'
def status(i): return 'neuf' if i in NEW else ('réutilisé (A)' if i in vocA else 'réutilisé (registre)')
# vocab json
json.dump({i:{'subject':'arabe','labels':dict(zip(('ar','fr','en'),NEW[i]))} for i in NEW},open(ET+'/vocab-arabe9-B.json','w'),ensure_ascii=False,indent=2)
open(ET+'/vocab-arabe9-B.json','a').write('\n')
# note verification (quotes must be literal fragments of the explanation/options, diacritics ignored)
import unicodedata
def norm(t):
    t=unicodedata.normalize('NFKD',t)
    t=''.join(ch for ch in t if not unicodedata.category(ch).startswith('M') and ch not in 'ـ')
    t=re.sub(r'[«»"“”\s\.\,،؛:؟!\(\)\-—…]+',' ',t)
    t=t.replace('أ','ا').replace('إ','ا').replace('آ','ا').replace('ى','ي').replace('ة','ه')
    return t.strip()
def verify(ch,q,note):
    qq=load(ch)[0][q]
    hay=norm(qq['explanation'])+' '+norm(' '.join(x['text'] for x in qq['options']))
    ok=True; has=False
    for m in re.finditer(r'«\s*([^»]+?)\s*»',note):
        has=True
        frag=m.group(1)
        parts=[x for x in re.split(r'…|\.\.\.',frag) if len(norm(x))>2] if ('…' in frag or '...' in frag) else [frag]
        for p_ in parts:
            if norm(p_) not in hay: ok=False
    return has,ok
def shownote(ch,q,note):
    if not note: return ''
    has,ok=verify(ch,q,note)
    if has and ok: return note
    if has: return re.sub(r'[«»]','',note).replace('R1 :','R1 (paraphrase de l\'explication) :',1)
    return note

# stats
tot_q=0;tot_d=0
for ch in sorted({c for c,_,_,_ in [x for v in byid.values() for x in v]}|set(CP)):
    qs_,_=load(ch); tot_q+=len(qs_); tot_d+=sum(len(q['options'])-1 for q in qs_.values())
tagged=len(seen); qtag=len({(c,q) for (c,q,o) in seen})
npg=sum(len(v) for v in PG.values()); npg_id=sum(1 for ch_,v in PG.items() for _,ids,_ in v if any(any(c==ch_ for c,_,_,_ in byid.get(i,[])) for i in ids))
STAT=f'Couverture : {tagged} distracteurs taguables sur {tot_d} ({100*tagged//tot_d} %), répartis sur {qtag} questions sur {tot_q} ; {npg_id} pièges sur {npg} ont au moins un id porté par un distracteur du chapitre (les autres : voir § 4).'
# map
chs=sorted({c for c in chdir if c in {x[0] for v in byid.values() for x in v} or c in PG or c in CP})
pgtxt={}
out=[]
out.append('# Carte d\'usage — vocabulaire d\'erreurs de l\'arabe 9ᵉ, PARTIE B (11 chapitres)\n')
done=sorted(set(CP)|set(PG))
out.append(f'> Statut : chapitres traités : {", ".join(done)}. Généré par script à partir d\'un jeu de données unique ; chaque distracteur cité est relu dans le corpus (extrait du JSON). Aucun fichier de `content/` n\'est modifié.\n')
out.append('Livrable jumeau : `vocab-arabe9-B.json` (ids NEUFS seulement).\n')
out.append('## 0. Conventions\n')
out.append('- Référence d\'un distracteur : `CC:F#N→o` = chapitre `CC`, fichier `F` (`quiz` ou le préfixe numérique du fichier de `exercices/`), question `N` (rang 1-based dans le fichier, = `qN` du compilateur), option `o`. Toutes les questions sont `mcq`, aucune option n\'était taguée.')
out.append('- « Q » = nombre de questions DISTINCTES (tous chapitres B confondus) qui ont au moins un distracteur porteur. Un distracteur n\'est cité que pour UN id (le script refuse un doublon).')
out.append('- Notes entre « » après un distracteur : extrait littéral de l\'explication ou des options, vérifié par script (voyelles ignorées) ; « R1 (paraphrase de l\'explication) » = l\'explication dit cela mais sans citation littérale ; sans note = R2/R3 (jeu de distracteurs construit sur l\'erreur, ou calcul juste avec un geste inversé). Tous les distracteurs porteurs sont listés (pas seulement 2 à 5 exemples) pour permettre l\'application mécanique.')
out.append('- Réutilisation : « registre » = id déjà dans `content/misconceptions.json` ; « A » = id de `vocab-arabe9-A.json`.\n')
nnew=len(NEW); nre=len([i for i in allids if i not in NEW])
out.append('## 1. Synthèse des ids\n')
out.append(f'**{nnew} ids neufs, {nre} ids réutilisés** (parmi les ids effectivement utilisés).\n')
out.append(STAT+'\n')
out.append('| id | statut | chapitres | Q | `piege` |'); out.append('| --- | --- | --- | --- | --- |')
pgmap=defaultdict(list)
for ch,v in PG.items():
    for n,ids,why in v:
        for i in ids: pgmap[i].append(f'{ch}: n°{n}')
for i in sorted(allids):
    cs=sorted({c for c,_,_,_ in byid.get(i,[])})
    nq=len({(c,q) for c,q,_,_ in byid.get(i,[])})
    out.append(f'| `{i}` | {status(i)} | {", ".join(cs)} | {nq} | {"; ".join(pgmap.get(i,[])) or "—"} |')
out.append('\n## 2. Fiches par id\n')
dom=None
for i in sorted(allids):
    d=i.split('.')[1]
    if d!=dom: out.append(f'### Domaine `{d}`\n'); dom=d
    out.append(f'#### `{i}` — {status(i).upper()}\n')
    if i in NEW:
        ar,fr,en=NEW[i]; out.append(f'- **AR** : {ar}\n- **FR** : {fr}\n- **EN** : {en}')
    else:
        out.append(f'- **AR** : {lab(i,"ar")}\n- **FR** : {lab(i,"fr")}')
    pp=[]
    for ch,v in sorted(PG.items()):
        for n,ids,why in v:
            if i in ids:
                _,pgs=load(ch)
                pp.append(f'ch{ch} — piège n°{n} « {short(pgs[n-1],110)} »'+(f' ({why})' if why else ''))
    out.append('- **Chapitres / piège** : '+('; '.join(pp) if pp else ', '.join('ch'+c for c in sorted({c for c,_,_,_ in byid.get(i,[])}))+' — (pas de piège ; erreur récurrente dans les items)'))
    out.append(f'- **Q distinctes** : {len({(c,q) for c,q,_,_ in byid.get(i,[])})}')
    out.append('- **Distracteurs porteurs** :')
    for c,q,o,note in byid.get(i,[]):
        Q=load(c)[0][q]; t=[x['text'] for x in Q['options'] if x['id']==o][0]
        out.append(f'  - `{c}:{q}→{o}` « {short(t)} »'+(f' — {shownote(c,q,note)}' if note else ''))
    out.append('')
out.append('## 3. Règles de précédence\n')
out+= [f'- {x}' for x in PREC] or ['- (aucune)']
out.append('\n## 4. Pièges sans id\n')
out+= [f'- {x}' for x in SANS] or ['- (aucun à ce stade)']
out.append('\n## 5. Erreurs vues < 3 fois (non retenues)\n')
out+= [f'- {x}' for x in LT3] or ['- (aucune)']
out.append('\n## 6. `coursePitfalls` proposés par chapitre\n')
out.append('| chapitre | `coursePitfalls` proposés | C-5 (porté par un distracteur du chapitre) |'); out.append('| --- | --- | --- |')
for ch in sorted(CP):
    cells=[];oks=[]
    for i in CP[ch]:
        n=[(q,o) for c,q,o,_ in byid.get(i,[]) if c==ch]
        cells.append(f'`{i}`'); oks.append(f'{"✓" if n else "✗"} ({len(n)})')
    out.append(f'| {chdir[ch]} | {"<br>".join(cells)} | {"<br>".join(oks)} |')
if NOTES:
    out.append('\n## 7. Notes et doutes\n'); out+= [f'- {x}' for x in NOTES]
open(ET+'/map-arabe9-B.md','w').write('\n'.join(out)+'\n')
print('ids new',nnew,'reused',nre,'assigned',len(seen)); print(STAT)
print('\n'.join(errs) if errs else 'OK no errors')
# diagnostics
pg_ids={x for v in PG.values() for _,ids,_ in v for x in ids}
low=[(i,len({(c,q) for c,q,_,_ in byid[i]})) for i in sorted(byid) if len({(c,q) for c,q,_,_ in byid[i]})<3 and i not in pg_ids]
print('LOW (<3 Q, no piege):',low)
print('UNUSED NEW:',[i for i in NEW if i not in byid])
print('NEW by domain:',{d:sum(1 for i in NEW if i.split('.')[1]==d) for d in sorted({i.split('.')[1] for i in NEW})})
# quote validation
import unicodedata
def norm(t):
    t=unicodedata.normalize('NFKD',t)
    t=''.join(ch for ch in t if not unicodedata.category(ch).startswith('M') and ch not in 'ـ')
    t=re.sub(r'[«»"“”\s\.\,،؛:؟!\(\)\-—…]+',' ',t)
    t=t.replace('أ','ا').replace('إ','ا').replace('آ','ا').replace('ى','ي').replace('ة','ه').replace('ّ','')
    return t.strip()
bad=[]
for (i,ch,q,o,note) in ASSIGN:
    for m in re.finditer(r'«\s*([^»]+?)\s*»',note):
        frag=m.group(1)
        if '…' in frag or '...' in frag: parts=[x for x in re.split(r'…|\.\.\.',frag) if len(norm(x))>2]
        else: parts=[frag]
        qq=load(ch)[0][q]
        hay=norm(qq['explanation'])+' '+norm(' '.join(x['text'] for x in qq['options']))
        for p_ in parts:
            if norm(p_) not in hay: bad.append((ch,q,o,i.split('.')[-1],p_[:60]))
print('QUOTE MISMATCH',len(bad))
for b in bad[:400]: print(b)
