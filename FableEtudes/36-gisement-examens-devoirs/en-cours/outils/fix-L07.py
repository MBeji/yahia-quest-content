import sys, json, re
sys.path.insert(0, '/tmp/claude-0/-home-user/b03814da-e5f9-5a74-bf03-e7c23b20207a/scratchpad')
from fixlib17 import *
SP = '/tmp/claude-0/-home-user/b03814da-e5f9-5a74-bf03-e7c23b20207a/scratchpad'
path, load = mk('/home/user/yahia-quest-content/content/math/07-statistiques/exercices/')
def Q(d, i): return d['questions'][i - 1]

# ===== 24 Q8 (E1) : plan 2×2, toutes les valeurs dans ]2 ; 4[
p, raw, d = load('24'); q = Q(d, 8)
assert opt(q, 'b')['text'] == '(220 − 120) × 2 ÷ (330 − 120)' and opt(q, 'c')['text'] == '4 + (220 − 120) × 2 ÷ (330 − 120)'
assert opt(q, 'b').get('misconceptionTag') == 'math.stat.interpolation-borne-inferieure-oubliee' and 'misconceptionTag' not in opt(q, 'c')
opt(q, 'b')['text'] = '2 + (220 − 120) ÷ (330 − 120)'      # l'étiquette est remplacée par le passage « étiquettes »
opt(q, 'c')['text'] = '4 − (220 − 120) ÷ (330 − 120)'
old_err = q['explanation'][q['explanation'].index('الخطأ الشائع:'):]
assert old_err.endswith('بالجمع.') and old_err.count('الخطأ الشائع:') == 1, old_err
q['explanation'] = q['explanation'].replace(old_err, 'الخطأ الشائع: الاكتفاء بالنسبة (220 − 120) ÷ (330 − 120) دون ضربها في عرض القطعة 2؛ أو الانطلاق من الفاصلة 4 بالطرح بدل الانطلاق من الفاصلة 2 بالجمع، مع الضرب في عرض القطعة أو بدونه.')
vals = {}
for oid in 'abcd':
    t = opt(q, oid)['text'].replace('−', '-').replace('÷', '/').replace('×', '*'); vals[oid] = eval(t)
print('24 Q8 valeurs', {k: round(v, 3) for k, v in vals.items()})
assert all(2 < v < 4 for v in vals.values()) and len({round(v, 6) for v in vals.values()}) == 4
L = {o['id']: len(o['text']) for o in q['options']}; print('longueurs', L)
assert not all(L['a'] > L[x] for x in 'bcd'), 'clé strictement la plus longue'
save(p, raw, d)

# ===== 23 Q6 (R1)
p, raw, d = load('23'); q = Q(d, 6)
assert opt(q, 'a')['text'] == 'أعلى ترتيبة فيه هي 250، لأنّ 250 هو عدد الفوانيس كلّها'
opt(q, 'a')['text'] = 'أعلى ترتيبة فيه هي 250، لأنّ 250 هو التكرار الكلّي'
L = {o['id']: len(o['text']) for o in q['options']}; print('23 Q6 longueurs', L)
assert not all(L['a'] > L[x] for x in 'bcd')
assert q['correctOption'] == 'a'
save(p, raw, d)

# ===== pending-tags/L07.json (E1 b, R2 libellés, R3 placements)
pp = SP + '/pending-tags/L07.json'
pend = json.load(open(pp, encoding='utf8'))
n = pend['nouvelles']
ci = 'math.stat.classes-concernees-incompletes'; cd = 'math.stat.cumul-decale-d-une-classe'
assert 'on the right side' in n[ci]['en']
n[ci]['en'] = n[ci]['en'].replace('on the right side', 'on the required side')
n[cd]['en'] = "You shift the cumulative count by one class: it counts the values strictly below the class's upper bound — neither just those below its lower bound, nor those of the next class as well"
n[cd]['ar'] = "تُزيح التكرار المجمّع بفئة واحدة: هو يعدّ القيم الأصغر قطعًا من الطرف الأكبر للفئة، لا القيم الأصغر من طرفها الأصغر وحدها، ولا قيم الفئة التالية معها"
opts = pend['options']
assert not [o for o in opts if o['file'] == '24' and o['q'] == 8 and o['opt'] == 'b']
opts.append({'file': '24', 'q': 8, 'opt': 'b', 'id': 'math.stat.interpolation-mal-posee', 'remplace': 'math.stat.interpolation-borne-inferieure-oubliee', 'texte': '2 + (220 − 120) ÷ (330 − 120)'})
for f, qq, oo in [('18', 5, 'd'), ('24', 7, 'a')]:
    assert not [o for o in opts if o['file'] == f and o['q'] == qq and o['opt'] == oo]
    opts.append({'file': f, 'q': qq, 'opt': oo, 'id': 'math.stat.effectif-cumule-non-cumule'})
pend['elargir'] = {'math.stat.effectif-cumule-non-cumule': {
    'fr': "Tu confonds l'effectif d'une classe (ou d'une valeur) et son effectif cumulé : le cumulé additionne tous les effectifs jusqu'à elle, l'effectif ne compte qu'elle",
    'en': "You mix up a class's (or a value's) own count with its cumulative count: the cumulative adds up every count up to it, the count covers only itself",
    'ar': "تخلط بين تكرار الفئة (أو القيمة) وتكرارها المجمّع: المجمّع يجمع كلّ التكرارات إلى غايتها، والتكرار يعدّها وحدها"}}
json.dump(pend, open(pp, 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print('pending placements:', len(opts), '| nouvelles:', len(n))
