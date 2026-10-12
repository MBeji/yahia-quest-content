# unify A and B data
import json,os,re,glob,collections
ROOT='/home/user/wt-arabe'
E=ROOT+'/FableEtudes/_campagne-9eme-au-patron/arabe-9eme/etiquettes'
CA=ROOT+'/content/arabic'
CHDIR={c[:2]:c for c in os.listdir(CA) if re.match(r'\d\d-',c)}
REG=json.load(open(ROOT+'/content/misconceptions.json'))
def files_of(ch):
    base=CA+'/'+CHDIR[ch]
    r=[('quiz','quiz.json')]+[(os.path.basename(x)[:2],'exercices/'+os.path.basename(x)) for x in sorted(glob.glob(base+'/exercices/*.json'))]
    return r
_c={}
def qs(ch):
    if ch in _c: return _c[ch]
    base=CA+'/'+CHDIR[ch]; d={}
    for k,f in files_of(ch):
        for i,q in enumerate(json.load(open(base+'/'+f))['questions'],1):
            d[(k,i)]=dict(q,_file=f)
    _c[ch]=d; return d
def pieges(ch):
    cours=open(CA+'/'+CHDIR[ch]+'/cours.md').read()
    return [m.group(1).strip().replace('\n',' ') for m in re.finditer(r'^::: piege.*?\n(.*?)^:::',cours,re.S|re.M)]
# ---- A
srcA=open(E+'/work-A/data_A.py').read().replace('/tmp/claude-0/-home-user/8ff73c67-6eab-5a69-a66d-d237b8d69142/scratchpad/ar9/tags/work-A',E+'/work-A')
nsA={}; exec(srcA,nsA)
IDSA=nsA['IDS']
for i,d in json.load(open(E+'/work-A/labels_override_A.json')).items():
    if i in IDSA: IDSA[i].update(d)
vA=json.load(open(E+'/vocab-arabe9-A.json'))
vB=json.load(open(E+'/vocab-arabe9-B.json'))
LAB={}; ORIG={}
for i,v in vA.items(): LAB[i]=v['labels']; ORIG[i]='A'
for i,v in vB.items(): LAB[i]=v['labels']; ORIG[i]='B'
ASSIGN=[]  # dict(id,ch,f,q,o,note,src)
PGL=collections.defaultdict(set) # (ch,k)->ids
for i,v in IDSA.items():
    for u in v.get('uses',[]):
        for k in u.get('pg',[]): PGL[(u['ch'],k)].add(i)
        for c in u.get('carriers',[]):
            ASSIGN.append(dict(id=i,ch=u['ch'],f=c[0],q=c[1],o=c[2],note=(c[3] if len(c)>3 else ''),src='A'))
# ---- B
from collections import OrderedDict
NEW=OrderedDict(); PG={}; AS=[]; CP={}; PREC=[]; SANS=[]; LT3=[]; NOTES=[]
def Af(i,ch,q,opts,note=''):
    for o in opts: AS.append((i,ch,q,o,note))
nsB=dict(NEW=NEW,PG=PG,ASSIGN=AS,CP=CP,PREC=PREC,SANS=SANS,LT3=LT3,NOTES=NOTES,A=Af)
for f in sorted(glob.glob(E+'/work-B/data/data_*.py')): exec(open(f).read(),nsB)
for (i,ch,q,o,note) in AS:
    k,n=q.split('#'); ASSIGN.append(dict(id=i,ch=ch,f=k,q=int(n),o=o,note=note,src='B'))
for ch,v in PG.items():
    for n,ids,why in v:
        for i in ids: PGL[(ch,n)].add(i)
CPB=CP
