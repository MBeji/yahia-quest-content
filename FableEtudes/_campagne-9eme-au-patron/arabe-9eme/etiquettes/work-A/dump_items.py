import json, sys, os, glob
base = '/home/user/yahia-quest-content/content/arabic'
chap = sys.argv[1]
only = sys.argv[2] if len(sys.argv) > 2 else None
files = [os.path.join(base, chap, 'quiz.json')] + sorted(glob.glob(os.path.join(base, chap, 'exercices', '*.json')))
for f in files:
    name = os.path.relpath(f, os.path.join(base, chap))
    if only and only not in name:
        continue
    d = json.load(open(f))
    qs = d['questions']
    print('#' * 3, name, '|', d.get('title', ''), '| nq =', len(qs))
    for i, q in enumerate(qs, 1):
        t = q.get('type', 'mcq')
        print(f'--- {name}#q{i} [{t}] d={q.get("difficulty")}')
        print('P:', q['prompt'].replace('\n', ' / '))
        if t == 'mcq':
            for o in q['options']:
                mark = '*' if o['id'] == q['correctOption'] else ' '
                tag = ('  <TAG ' + o['misconceptionTag'] + '>') if 'misconceptionTag' in o else ''
                print(f'  {mark}{o["id"]}: {o["text"]}{tag}')
        else:
            print('  (type', t, ')', json.dumps({k: v for k, v in q.items() if k not in ('prompt', 'explanation', 'difficulty', 'type')}, ensure_ascii=False))
        print('E:', q['explanation'].replace('\n', ' / '))
