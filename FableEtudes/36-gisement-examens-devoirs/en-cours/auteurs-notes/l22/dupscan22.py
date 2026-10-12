import json,subprocess,re,glob,os
G=['git','-C','/home/user/yahia-quest-content']
files=subprocess.check_output(G+['ls-tree','-r','--name-only','origin/main','content/math/']).decode().split('\n')
files=[f for f in files if f.endswith('.json') and ('/exercices/' in f or f.endswith('quiz.json'))]
pub=[]
for f in files:
    if re.search(r'(07-statistiques/exercices/25|12-repere-plan/exercices/22|18-quadrilateres/exercices/42)-',f): continue
    try: d=json.loads(subprocess.check_output(G+['show','origin/main:'+f]))
    except Exception as e: continue
    qs=d.get('questions',d if isinstance(d,list) else [])
    for i,q in enumerate(qs):
        if isinstance(q,dict): pub.append((f,i+1,q))
def norm(t): return re.sub(r'\s+','',re.sub(r'<svg.*?</svg>','',t,flags=re.S))
def ws(t): return set(re.findall(r'\w+|[^\s\w]',re.sub(r'<svg.*?</svg>','',t,flags=re.S)))
def opts(q): return {norm(o['text']) for o in q.get('options',[])}
def jac(a,b): return len(a&b)/len(a|b) if a|b else 0
mine=[]
for f in sorted(glob.glob("/home/user/wt-m22/content/math/*/exercices/*.json")):
    if re.search(r"/(07-statistiques/exercices/25|12-repere-plan/exercices/22|18-quadrilateres/exercices/42)-",f):
        d=json.load(open(f))
        for i,q in enumerate(d['questions']): mine.append((os.path.basename(f)[:2],i+1,q))
# aussi : intra-lot
for n,i,q in mine:
    if q.get('type')=='numeric': continue
    o=opts(q); p=ws(q['prompt'])
    best=[]
    for f,j,r in pub:
        if r.get('type')=='numeric': continue
        s=len(o&opts(r)); jo=jac(o,opts(r)); jp=jac(p,ws(r['prompt']))
        if (s>=3 and len(o)==4) or jo>=0.5 or jp>=0.55: best.append((s,round(jo,2),round(jp,2),f.split('math/')[1][:40],j))
    if best: print(n,i,sorted(best,reverse=True)[:3])
