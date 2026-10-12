import json,sys,glob,os,re
ch=sys.argv[1]
base=f'/home/user/wt-arabe/content/arabic/{ch}'
out=[]
cours=open(base+'/cours.md').read()
out.append('=== PIEGES ===')
for m in re.finditer(r'^::: piege.*?\n(.*?)^:::',cours,re.S|re.M):
    out.append('PIEGE: '+m.group(1).strip().replace('\n',' '))
files=[('quiz',base+'/quiz.json')]+[(os.path.basename(f)[:2],f) for f in sorted(glob.glob(base+'/exercices/*.json'))]
for k,f in files:
    d=json.load(open(f))
    out.append(f'=== {k} ({d.get("title")}) ===')
    for i,q in enumerate(d['questions'],1):
        t=q.get('type','mcq')
        out.append(f'-- {k}#{i} [{t}] d{q.get("difficulty")} {q["prompt"].replace(chr(10)," ")}')
        for o in q.get('options',[]):
            c='*' if o['id']==q.get('correctOption') else ' '
            tg=' TAG='+o['misconceptionTag'] if 'misconceptionTag' in o else ''
            out.append(f'  {c}{o["id"]}) {o["text"].replace(chr(10)," ")}{tg}')
        out.append('  EXPL: '+q.get('explanation','').replace('\n',' '))
open(f'/tmp/claude-0/s/{ch[:2]}.txt','w').write('\n'.join(out))
print(ch,len('\n'.join(out)))
