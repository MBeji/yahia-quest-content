import sys
exec(open('/home/user/wt-arabe/FableEtudes/_campagne-9eme-au-patron/arabe-9eme/etiquettes/work-F/fusion.py').read())
by=collections.defaultdict(list)
for a in FIN: by[a['id']].append(a)
def sh(t,n): t=t.replace('\n',' '); return t if len(t)<=n else t[:n]+'…'
want=sys.argv[1:]
for i in sorted(by):
    if want and not any(w in i for w in want): continue
    print(f'### {i} [{origin(i)}] — {label(i)["fr"]}')
    for a in sorted(by[i],key=lambda a:(a['ch'],a['f'],a['q'],a['o'])):
        Q=qs(a['ch'])[(a['f'],a['q'])]
        key=[x['text'] for x in Q['options'] if x['id']==Q['correctOption']][0]
        opt=[x['text'] for x in Q['options'] if x['id']==a['o']][0]
        print(f"  {a['ch']}:{a['f']}#{a['q']}→{a['o']} | {sh(Q['prompt'],110)} | ✓ {sh(key,70)} | ✗ {sh(opt,90)}")
