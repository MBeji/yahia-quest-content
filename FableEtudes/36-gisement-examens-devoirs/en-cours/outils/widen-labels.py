"""Élargit (in place, exactement) trois libellés d'étiquettes existantes. Usage : widen-labels.py <racine du dépôt corpus> [--write]"""
import json, sys
root = sys.argv[1]; write = '--write' in sys.argv
mp = root + '/content/misconceptions.json'
raw = open(mp, encoding='utf-8').read(); reg = json.loads(raw)
ind = 2 if '\n  "' in raw else 1
assert json.dumps(reg, ensure_ascii=False, indent=ind) + ('\n' if raw.endswith('\n') else '') == raw, 'format du registre non reproduit'
W = {
 'math.alg.moins-devant-parenthese': {
  'fr': ("Tu n'appliques le signe moins qu'au premier terme de la parenthèse : il change le signe de tous les termes",
         "Tu n'appliques le signe moins qu'à une partie des termes de la parenthèse : il change le signe de TOUS les termes"),
  'en': ("You apply the minus sign to the first term only: it flips the sign of every term inside the brackets",
         "You apply the minus sign to only some of the terms inside the brackets: it flips the sign of EVERY term inside them"),
  'ar': ("تطبّق إشارة الطرح على الحدّ الأوّل فقط: هي تغيّر إشارة كلّ الحدود داخل القوسين",
         "تطبّق إشارة الطرح على بعض الحدود داخل القوسين فقط: هي تغيّر إشارة كلّ الحدود داخل القوسين")},
 'math.int.produit-signes-negatifs': {
  'fr': ("Tu te trompes sur le signe d'un produit : le produit de deux nombres négatifs est positif",
         "Tu te trompes sur le signe d'un produit ou d'un quotient : deux nombres de même signe donnent un résultat positif, deux nombres de signes contraires un résultat négatif"),
  'en': ("You get the sign of a product wrong: the product of two negative numbers is positive",
         "You get the sign of a product or a quotient wrong: two numbers of the same sign give a positive result, two numbers of opposite signs give a negative one"),
  'ar': ("تخطئ في إشارة الجداء: جداء عددين سالبين موجب",
         "تخطئ في إشارة الجداء أو خارج القسمة: عددان من الإشارة نفسها يعطيان نتيجة موجبة، وعددان مختلفا الإشارة يعطيان نتيجة سالبة")},
 'math.alg.transposition-sans-changer-signe': {
  'fr': ("Tu fais passer un terme de l'autre côté de l'égalité sans changer son signe",
         "Tu fais passer un terme de l'autre côté de l'égalité ou de l'inégalité sans changer son signe"),
  'en': ("You move a term to the other side of the equation without flipping its sign",
         "You move a term to the other side of the equation or inequality without flipping its sign"),
  'ar': ("تنقل حدًّا إلى الطرف الآخر من المساواة دون تغيير إشارته",
         "تنقل حدًّا إلى الطرف الآخر من المساواة أو المتراجحة دون تغيير إشارته")},
}
for tid, langs in W.items():
    for lg, (old, new) in langs.items():
        cur = reg[tid]['labels'][lg]
        assert cur == old, (tid, lg, cur)
        reg[tid]['labels'][lg] = new
print('libellés élargis :', len(W), 'étiquettes × 3 langues')
if write:
    open(mp, 'w', encoding='utf-8').write(json.dumps(reg, ensure_ascii=False, indent=ind) + ('\n' if raw.endswith('\n') else ''))
    print('écrit.')
