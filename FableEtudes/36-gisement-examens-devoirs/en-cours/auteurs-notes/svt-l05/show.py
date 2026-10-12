import json, sys, re
def short(s, n=300):
    s = s.replace('\n', ' / ')
    s = re.sub(r'<svg.*?</svg>', '<SVG>', s, flags=re.S)
    return s if len(s) <= n else s[:n] + '...'
for path in sys.argv[1:]:
    d = json.load(open(path))
    print('=' * 100)
    print(path.split('/')[-1], '|', d['title'], '| d', d['difficulty'], d['mode'], d['xpReward'], d['rewardCoins'], 'order', d['displayOrder'], '| nQ', len(d['questions']))
    for i, x in enumerate(d['questions']):
        t = x.get('type', 'mcq')
        print(f"--- Q{i+1} [{t}] d{x.get('difficulty')}")
        print('  P:', short(x.get('prompt', ''), 500))
        if t == 'mcq':
            for o in x['options']:
                print('    ', o['id'], ('*' if o['id'] == x['correctOption'] else ' '), short(o['text'], 220), ('{' + o['misconceptionTag'] + '}' if 'misconceptionTag' in o else ''))
        elif t in ('multi',):
            for o in x['options']:
                print('    ', o['id'], ('*' if o['id'] in x['answerKey']['correct'] else ' '), short(o['text'], 220))
        elif t == 'ordering':
            for o in x['options']:
                print('    ', o['id'], short(o['text'], 220))
            print('    ORDER', x['answerKey']['order'])
        elif t == 'matching':
            for o in x['options']:
                print('    ', o['id'], short(o['text'], 220))
            print('    PAIRS', x['answerKey']['pairs'])
        else:
            print('    KEY', x.get('answerKey'))
        if '-e' in sys.argv[0:1] or True:
            print('  E:', short(x.get('explanation', ''), 400))
