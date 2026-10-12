import json,sys
p=sys.argv[1]; n=int(sys.argv[2]) if len(sys.argv)>2 else 25
rows=[]
for line in open(p,encoding='utf-8'):
    try: o=json.loads(line)
    except Exception: continue
    m=o.get('message') or {}
    c=m.get('content')
    ts=o.get('timestamp','')
    if isinstance(c,str):
        rows.append((ts,m.get('role'),'TEXT',c[:600])); continue
    for b in c or []:
        t=b.get('type')
        if t=='text': rows.append((ts,m.get('role'),'text',b['text'][:700]))
        elif t=='tool_use':
            inp=b.get('input',{})
            s=json.dumps(inp,ensure_ascii=False)
            rows.append((ts,m.get('role'),'tool_use:'+b.get('name',''),s[:500]))
        elif t=='tool_result':
            cc=b.get('content')
            if isinstance(cc,list): cc=' '.join(x.get('text','') for x in cc if isinstance(x,dict))
            rows.append((ts,m.get('role'),'tool_result',(cc or '')[:300]))
for r in rows[-n:]:
    print(r[0],r[1],r[2]); print('   ',r[3].replace('\n','\n    ')); 
