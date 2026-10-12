import json, sys, os, glob, re
base = '/home/user/yahia-quest-content/content/arabic'
pat = re.compile(sys.argv[1])
chaps = sys.argv[2].split(',') if len(sys.argv) > 2 and sys.argv[2] != 'all' else [
 '15-al-alaqat-bayna-al-jumal','04-al-asalib','16-al-istifham','17-ash-shart','18-dalalat-az-zaman','02-an-nawasikh','03-al-mansoubat','19-al-adad-wal-madud']
for chap in chaps:
    files = [os.path.join(base, chap, 'quiz.json')] + sorted(glob.glob(os.path.join(base, chap, 'exercices', '*.json')))
    for f in files:
        name = os.path.relpath(f, os.path.join(base, chap))
        d = json.load(open(f))
        for i, q in enumerate(d['questions'], 1):
            hits = []
            if pat.search(q['prompt']): hits.append('P')
            for o in q.get('options', []):
                if pat.search(o['text']): hits.append('opt-' + o['id'])
            if pat.search(q['explanation']): hits.append('E')
            if hits:
                print(f'{chap[:2]} {name}#q{i} {hits} :: {q["prompt"][:90]}')
