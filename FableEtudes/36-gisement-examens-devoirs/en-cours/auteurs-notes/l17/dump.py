import json, re, sys, subprocess
def load(path, ref=None):
    if ref:
        txt = subprocess.check_output(['git','-C','/home/user/yahia-quest-content','show',f'{ref}:{path}']).decode()
    else:
        txt = open(path, encoding='utf-8').read()
    return json.loads(txt)
def strip_svg(s):
    def rep(m):
        t = re.search(r'<title>(.*?)</title>', m.group(0))
        return '[SVG:' + (t.group(1) if t else '') + ']'
    return re.sub(r'<svg.*?</svg>', rep, s, flags=re.S)
def dump(d, expl=300):
    print('TITLE', d['title'], '| d', d['difficulty'], d['mode'], d['xpReward'], d['rewardCoins'], 'order', d['displayOrder'], 'nq', len(d['questions']))
    for i,q in enumerate(d['questions']):
        t = q.get('type','mcq')
        print(f'--- Q{i+1} [{t}] d{q.get("difficulty")} comp={q.get("competencies")}')
        print('  P:', strip_svg(q['prompt']).replace('\n','\n     '))
        if t=='mcq':
            for o in q['options']:
                mark = '*' if o['id']==q['correctOption'] else ' '
                tag = o.get('misconceptionTag','')
                print(f'   {mark}{o["id"]}: {strip_svg(o["text"])}  {("<"+tag+">") if tag else ""}')
        elif t=='numeric':
            print('   NUM:', q['answerKey'])
        elif t=='multi':
            for o in q['options']:
                mark = '*' if o['id'] in q['answerKey']['correct'] else ' '
                print(f'   {mark}{o["id"]}: {strip_svg(o["text"])} {o.get("misconceptionTag","")}')
        elif t=='short_answer':
            print('   SA:', q['answerKey'], q.get('acceptedAnswers'))
        else:
            print('   ', {k:v for k,v in q.items() if k not in ('prompt','explanation')})
        e = strip_svg(q['explanation'])
        print('  E:', e if expl is None else e[:expl].replace('\n',' '))
if __name__=='__main__':
    path = sys.argv[1]
    ref = sys.argv[2] if len(sys.argv)>2 and sys.argv[2]!='-' else None
    expl = int(sys.argv[3]) if len(sys.argv)>3 else 300
    if expl < 0: expl=None
    d = load(path, ref)
    dump(d, expl)
