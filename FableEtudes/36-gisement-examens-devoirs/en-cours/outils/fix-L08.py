import sys, json, re
sys.path.insert(0, '/tmp/claude-0/-home-user/b03814da-e5f9-5a74-bf03-e7c23b20207a/scratchpad')
from fixlib17 import *
SP = '/tmp/claude-0/-home-user/b03814da-e5f9-5a74-bf03-e7c23b20207a/scratchpad'
rep = open(SP + '/author/exam/reverif-L08.md', encoding='utf8').read()
def section(a, b): i = rep.index(a); return rep[i:rep.index(b, i)]
def full_after(sec, label):
    i = sec.index(label); m = re.search(r'`([^`]+)`', sec[i:]); return m.group(1)
path, load = mk('/home/user/yahia-quest-content/content/math/12-repere-plan/exercices/')
def Q(d, i): return d['questions'][i - 1]
S1, S2, S3, S4, S5 = (section('### R1', '### R2'), section('### R2', '### R3'), section('### R3', '### R4'), section('### R4', '### R5'), section('### R5', '## 3.'))
DRY = '--dry' in sys.argv

# ===== R1 : 11 Q1 — valeurs étiquetées
p, raw, d = load('11'); q = Q(d, 1)
newopt = dict(re.findall(r'- ([abcd]) `([^`]+)`', S1))
assert sorted(newopt) == list('abcd') and newopt['a'] == 'xA = −2 ، xB = 3', newopt
assert [o['id'] for o in q['options']] == list('abcd') and q['correctOption'] == 'a'
for oid in 'abcd':
    assert 'misconceptionTag' not in opt(q, oid)
    opt(q, oid)['text'] = newopt[oid]
q['explanation'] = full_after(S1, 'explanation, texte complet')
assert q['explanation'].count('xA = 2 و xB = −3') == 1 and q['explanation'].count('xB = 2') == 1
L = {o['id']: len(o['text']) for o in q['options']}; print('11 Q1 longueurs', L); assert not all(L['a'] > L[x] for x in 'bcd')
# ===== R2 : 11 Q3 et Q6 — « AM = 2/3 × AB » (ligne-équation) ; explication de Q3 alignée
q3 = Q(d, 3); q6 = Q(d, 6)
for qq, lab in ((q3, '11 Q3'), (q6, '11 Q6')):
    assert qq['prompt'].count('\nAM = 2/3 AB\n') == 1, lab
    qq['prompt'] = qq['prompt'].replace('\nAM = 2/3 AB\n', '\nAM = 2/3 × AB\n')
exp3 = full_after(S2, '11 Q3, explanation')
chk = q3['explanation']
for a, b in (('الكتابة AM = 2/3 AB تعني', 'الكتابة AM = 2/3 × AB تعني'), ('فنجد AM = 1/3 AB', 'فنجد AM = 1/3 × AB'), ('منتصفها وAM = 1/2 AB', 'منتصفها وAM = 1/2 × AB')):
    assert chk.count(a) == 1, a; chk = chk.replace(a, b)
assert chk == exp3, ('explication 11 Q3 : le texte du rapport diffère des remplacements', chk, exp3)
q3['explanation'] = exp3
# ===== R3 : 11 Q6 (a) → 1/2, explication
assert opt(q6, 'a')['text'] == '−4/3' and 'misconceptionTag' not in opt(q6, 'a')
opt(q6, 'a')['text'] = '1/2'
q6['explanation'] = full_after(S3, 'explanation, texte complet')
L = {o['id']: len(o['text']) for o in q6['options']}; print('11 Q6 longueurs', L, [o['text'] for o in q6['options']]); assert not all(L['a'] > L[x] for x in 'bcd')
assert [o['text'] for o in q6['options']].count('4/3') == 1
if not DRY: save(p, raw, d)

# ===== R4 : 12 Q5 — énoncé
p, raw, d = load('12'); q = Q(d, 5)
old = 'ونذكّر أنّ المعيّن (C, A, D) أصله C ، ومحور فواصله المستقيم (CA) ووحدته الطول CA ، ومحور ترتيباته المستقيم (CD) ووحدته الطول CD.'
new = 'ونذكّر أنّ المعيّن (C, A, D) أصله C ، والنقطة الواحديّة على محور فواصله (CA) هي A ، والنقطة الواحديّة على محور ترتيباته (CD) هي D.'
assert q['prompt'].count(old) == 1
full = full_after(S4, 'prompt complet')
q['prompt'] = q['prompt'].replace(old, new)
assert q['prompt'] == full.replace('\\n', '\n'), (q['prompt'], full)
if not DRY: save(p, raw, d)

# ===== R5 : 14 Q2 — explication
p, raw, d = load('14'); q = Q(d, 2)
old = 'فالعدد 13 المقابل للقيمة 0 هو عدد مرّات ظهور القيم −2 و −1 و 0 ، من تكرار كلّي قدره 20 ✓ ، أي القيم التي لا تتجاوز 0.'
new = 'فالعدد المقابل للقيمة 0 هو عدد مرّات ظهور القيم −2 و −1 و 0 ، أي القيم التي لا تتجاوز 0 ، وهو 13 ✓ من تكرار كلّي قدره 20.'
assert q['explanation'].count(old) == 1
q['explanation'] = q['explanation'].replace(old, new)
full = full_after(S5, 'explanation complète')
assert q['explanation'] == full, (q['explanation'], full)
if not DRY: save(p, raw, d)
print('OK', 'dry-run' if DRY else 'écrit')
