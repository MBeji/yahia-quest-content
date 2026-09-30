"""Passe 2 des étiquettes : libellés élargis, corrections de deux étiquettes publiées. Usage : tags-pass2.py <racine> [--write]"""
import json, sys, glob
root = sys.argv[1]; write = '--write' in sys.argv
mp = root + '/content/misconceptions.json'
raw = open(mp, encoding='utf-8').read(); reg = json.loads(raw)
ind = 2 if '\n  "' in raw else 1
assert json.dumps(reg, ensure_ascii=False, indent=ind) + ('\n' if raw.endswith('\n') else '') == raw
W = {
 'math.num.racine-distribuee-sur-somme': {
  'fr': ("Tu distribues la racine sur une somme : la règle ne vaut que pour un produit ou un quotient, jamais pour une addition",
         "Tu distribues la racine sur une somme ou une différence (ou tu fusionnes deux racines ainsi) : la règle ne vaut que pour un produit ou un quotient, jamais pour une addition ni une soustraction"),
  'en': ("You spread the root across a sum: the rule only holds for a product or a quotient, never for an addition",
         "You spread the root across a sum or a difference (or merge two roots that way): the rule only holds for a product or a quotient, never for an addition or a subtraction"),
  'ar': ("توزّع الجذر على مجموع: القاعدة لا تصحّ إلّا مع الجداء أو خارج القسمة، لا مع الجمع",
         "توزّع الجذر على مجموع أو فرق (أو تدمج جذرين بهذه الطريقة): القاعدة لا تصحّ إلّا مع الجداء أو خارج القسمة، لا مع الجمع ولا مع الطرح")},
 'math.stat.effectif-cumule-non-cumule': {
  'fr': ("Tu donnes l'effectif de la valeur au lieu de son effectif cumulé : le cumulé additionne tous les effectifs jusqu'à elle",
         "Tu confonds l'effectif d'une classe (ou d'une valeur) et son effectif cumulé : le cumulé additionne tous les effectifs jusqu'à elle, l'effectif ne compte qu'elle"),
  'en': ("You give the value's own count instead of its cumulative count: the cumulative adds up every count down to it",
         "You mix up a class's (or a value's) own count with its cumulative count: the cumulative adds up every count up to it, the count covers only itself"),
  'ar': ("تعطي تكرار القيمة بدل تكرارها المجمّع: المجمّع يجمع كلّ التكرارات إلى غاية تلك القيمة",
         "تخلط بين تكرار الفئة (أو القيمة) وتكرارها المجمّع: المجمّع يجمع كلّ التكرارات إلى غايتها، والتكرار يعدّها وحدها")},
}
for tid, langs in W.items():
    for lg, (old, new) in langs.items():
        assert reg[tid]['labels'][lg] == old, (tid, lg, reg[tid]['labels'][lg])
        reg[tid]['labels'][lg] = new
print('libellés élargis :', list(W))
# corrections de deux étiquettes publiées
g = glob.glob(root + '/content/math/14-annales-sujets-types/exercices/03-*.json')[0]
d14 = json.load(open(g, encoding='utf-8')); raw14 = open(g, encoding='utf-8').read()
q = d14['questions'][5]; o = {x['id']: x for x in q['options']}
assert o['c']['text'] == '32 كم' and o['c'].get('misconceptionTag') == 'math.alg.transposition-sans-changer-signe' and o['d']['text'] == '36 كم' and 'misconceptionTag' not in o['d']
o['c'].pop('misconceptionTag'); o['d']['misconceptionTag'] = 'math.alg.transposition-sans-changer-signe'
gq = root + '/content/math/03-calcul-litteral/quiz.json'
dq = json.load(open(gq, encoding='utf-8')); rawq = open(gq, encoding='utf-8').read()
q = dq['questions'][1]; o = {x['id']: x for x in q['options']}
assert o['b']['text'] == 'a − b' and o['b'].get('misconceptionTag') == 'math.alg.moins-devant-parenthese'
o['b'].pop('misconceptionTag')
print('14/03 Q6 : étiquette de c (32 كم) déplacée sur d (36 كم) ; quiz 03 Q2 b rendue muette')
if write:
    open(mp, 'w', encoding='utf-8').write(json.dumps(reg, ensure_ascii=False, indent=ind) + ('\n' if raw.endswith('\n') else ''))
    for p, dd, rr in [(g, d14, raw14), (gq, dq, rawq)]:
        i2 = 2 if '\n  "' in rr else None
        open(p, 'w', encoding='utf-8').write(json.dumps(dd, ensure_ascii=False, indent=i2) + ('\n' if rr.endswith('\n') else ''))
    print('écrit.')
