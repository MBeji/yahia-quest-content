import sys, json, re
sys.path.insert(0, '/tmp/claude-0/-home-user/b03814da-e5f9-5a74-bf03-e7c23b20207a/scratchpad')
from fixlib17 import *
path, load = mk('/home/user/yahia-quest-content/content/math/08-thales/exercices/')
def Q(d, i): return d['questions'][i - 1]
DRY = '--dry' in sys.argv

# ===== D1 : 17 Q2 — plan 2×2 (signe × coefficient), option b muette
p, raw, d = load('17'); q = Q(d, 2)
assert opt(q, 'b')['text'] == 'x² + 1 − 9' and opt(q, 'b').get('misconceptionTag') == 'math.alg.carre-somme-sans-double-produit'
opt(q, 'b')['text'] = 'x² − x + 1 − 9'; opt(q, 'b').pop('misconceptionTag')
sub(q, 'explanation', 'أو نسيان الجداء المضاعف فنكتب x² + 1 − 9 ؛ أو كتابته دون العامل 2 فنكتب x² + x + 1 − 9.',
    'أو كتابة الجداء المضاعف دون العامل 2 فنكتب x² + x + 1 − 9 ؛ أو جمع الخطأين فنكتب x² − x + 1 − 9.')
L = {o['id']: len(o['text']) for o in q['options']}; print('17 Q2 longueurs', L); assert not all(L['d'] > L[x] for x in 'abc')
assert q['correctOption'] == 'd'
# ===== D4 : 17 Q4, Q6, Q7 — figure hors échelle de x = 2 + mention dans l'énoncé
SVG = [('d="M170 202 L58 202"', 'd="M170 202 L86 202"'), ('d="M226 34 L58 202"', 'd="M226 34 L86 202"'),
       ('<circle cx="58" cy="202" r="4.4"/>', '<circle cx="86" cy="202" r="4.4"/>'),
       ('<circle cx="170" cy="90" r="4.6"/>', '<circle cx="170" cy="101.2" r="4.6"/>'),
       ('<text x="185" y="93" text-anchor="middle" fill="#0f172a">A</text>', '<text x="185" y="104" text-anchor="middle" fill="#0f172a">A</text>'),
       ('<text x="45" y="208" text-anchor="middle" fill="#0f172a">F</text>', '<text x="73" y="208" text-anchor="middle" fill="#0f172a">F</text>'),
       ('<text x="156" y="67" text-anchor="middle" fill="#0f6e56">x</text>', '<text x="156" y="73" text-anchor="middle" fill="#0f6e56">x</text>'),
       ('<text x="156" y="151" text-anchor="middle" fill="#0f6e56">4</text>', '<text x="156" y="157" text-anchor="middle" fill="#0f6e56">4</text>'),
       ('<text x="114" y="224" text-anchor="middle" fill="#0f6e56">x + 2</text>', '<text x="128" y="224" text-anchor="middle" fill="#0f6e56">x + 2</text>')]
for n in (4, 6, 7):
    qq = Q(d, n)
    for old, new in SVG: sub(qq, 'prompt', old, new)
    if n == 7: sub(qq, 'prompt', 'd="M170 90 L170 202 L58 202 Z"', 'd="M170 101.2 L170 202 L86 202 Z"')
    sub(qq, 'prompt', 'في الشكل التالي المستقيم (BE)', 'في الشكل التالي ، وهو غير مرسوم بمقياس الرسم ، المستقيم (BE)')
if not DRY: save(p, raw, d)
# ===== D2 : 13 Q1 — « A = (3/21)³ » (ligne-équation)
p, raw, d = load('13'); q = Q(d, 1)
assert q['prompt'] == 'ما قيمة العدد التالي ؟\n(3/21)³', repr(q['prompt'])
q['prompt'] = 'ما قيمة العدد A التالي ؟\nA = (3/21)³'
if not DRY: save(p, raw, d)
# ===== D3 : 19 Q3 — consigne
p, raw, d = load('19'); q = Q(d, 3)
sub(q, 'prompt', 'ما المساواة التي نحصل عليها بتعويض هذه الأطوال ؟', 'ما المساواة التي نحصل عليها بعد تعويض كلّ طول في هذه المساواة بقيمته ؟')
if not DRY: save(p, raw, d)
print('OK', 'dry-run' if DRY else 'écrit')
