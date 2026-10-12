# Audit indépendant — tranche T23-G2 (maths 9ᵉ, devoirs T2′ salle blanche, ch. 04-equations-inequations, missions 29 → 33)

Auditeur indépendant (consigne `content-ingest/references/gisement-auditeur.md`, skill `content-audit`).
Périmètre : `/home/user/wt-m22`, `content/math/04-equations-inequations/exercices/29…33-devoir-*.json` (5 missions, 38 questions).
Cartes lues : `plan/assign-T23-G2.md` (aucun texte source). Aucune source de devoir, aucune note d'auteur ouverte. Rien n'est modifié.
Rapport écrit au fil de l'eau.

## 1. Réponses à l'aveugle (posées AVANT lecture des clés, explications et étiquettes ; vérifiées par sympy)

- 29 : Q1 −15 · Q2 (x − 7)(x + 1) · Q3 {−1 ; 7} · Q4 {−2 ; 8} · Q5 [−1 ; 5[ · Q6 {0 ; 7} · Q7 11 (13 naturels 0…12, solutions 0 et 7) · Q8 9 (racines 2 et 7) · Q9 k = 8 (racine double 7).
- 30 : Q1 (2x − 5)(2x + 5) · Q2 {−5/2 ; 5/2} · Q3 « négatif car 3 < 4 donc √3 < 2 » · Q4 {−3 ; 1/3} · Q5 x ≤ −2 − √3 · Q6 4 ((√11 + 3)/2 ≈ 3,16).
- 31 : Q1 (√7 + 2)/3 · Q2 2√7/3 · Q3 2 ≤ x ≤ 5 · Q4 −1/2 ≤ 1/x ≤ −1/5 · Q5 1/(√7 − 3) < 1/(√7 − 1) (≈ −2,82 < 0,61 ; les trois autres fausses) · Q6 10/7 ≤ … ≤ 5/3 · Q7 ]−∞ ; −2] ∪ ]3 ; +∞[ · Q8 2 (n = 1 et 2).
- 32 : Q1 3 · Q2 x ≤ 3 · Q3 (x − 4)(x + 2) · Q4 {−2 ; 4} · Q5 −4 ≤ x − 4 ≤ −1 · Q6 premier négatif, second positif · Q7 {−2} · Q8 −20 ≤ T(x) ≤ −2 (produits −8, −20, −2, −5 ; encadrement exact −9 ≤ T ≤ −5) · Q9 ∅.
- 33 : Q1 x² + 3x − 18 · Q2 {−6 ; 3} · Q3 x > 1 · Q4 (x + 4)(x − 1) = 14 · Q5 2 m et 7 m (x = 3) · Q6 3 m et 8 m (x = 4).

**Comparaison aux clés** (lues après) : 38/38 identiques. **Aucune clé fausse.**

Outils : sympy (clés + chaque distracteur + chaque correctif), `dupscan.py` adapté au ch. 04 (publié `origin/main` + intra-lot), `git grep` des
expressions sur tout `content/math` de `origin/main`, `content:qa` (0 erreur) et `content:tranche --chapters 04` (clé jamais strictement la plus
longue dans le lot), banc Chromium `dir=rtl` (`bench-rtl.mjs` sur le `bidi.ts` de `/home/user/eng-m22` = `origin/main` 7cd50eb) + mesure
caractère par caractère (Range.getBoundingClientRect) des intervalles en ligne.

## 2. Tableaux par fichier

### 29-devoir-evaluation-factorisation-et-parametre (d3 boss 120/30 ✓ ; rampe 1,2,2,2,2,3,3,3,3 ✓)

| Q | d | ma réponse | clé | verdict | motif |
|---|---|---|---|---|---|
| 1 | 1 | −15 | b −15 | OK | −23 = 4² lu 4 × 2 (étiquette exacte) |
| 2 | 2 | (x − 7)(x + 1) | b | OK | énoncé « forme canonique donnée » ✓ ; gabarit du publié 04/12 Q1 (m4) |
| 3 | 2 | {−1 ; 7} | b | OK | l'énoncé redonne la clé de Q2 (émise avant) : convention, accepté |
| 4 | 2 | {−2 ; 8} | c | OK | parallèle du publié 04/06 Q2 « (x − 4)² = 9 » (autres données) : accepté |
| 5 | 2 | [−1 ; 5[ | d | réserve (M4) | option a ]−5 ; 1] : étiquette et mécanisme d'explication faux |
| 6 | 3 | {0 ; 7} | b | réserve (M3) | vote par élément : 7 ×3, 0 ×2 → reconstruit {0 ; 7} |
| 7 | 3 | 11 | b | ERREUR de forme (M1) | doublon de Q6 (même équation, n pour x) ; l'explication de Q6 livre 13 − 2 |
| 8 | 3 | 9 | d | réserve (M2) | non autonome : il faut factoriser x² − 6x − 7, que rien ne donne |
| 9 | 3 | k = 8 | d | réserve (M2) | idem ; option c (7) sans explication ; b mérite une étiquette |

### 30-devoir-produit-nul-et-coefficient-radical (d3 boss 120/30 ✓ ; rampe 2,2,2,3,3,3 ✓)

| Q | d | ma réponse | clé | verdict | motif |
|---|---|---|---|---|---|
| 1 | 2 | (2x − 5)(2x + 5) | b | OK | |
| 2 | 2 | {−5/2 ; 5/2} | c | OK | énoncé redonne la clé de Q1 : convention |
| 3 | 2 | « négatif, car 3 < 4 » | b | OK | point auteur : c conclut juste mais déduit « < 1 ⟹ < 0 » : non défendable, l'explication le nomme |
| 4 | 3 | {−3 ; 1/3} | b | OK | point auteur : {3 ; −1/3} exécute bien la transposition (vérifié), « لا حلّ » l'erreur (x − 2)² = x² − 4 |
| 5 | 3 | x ≤ −2 − √3 | c | OK (m5) | plan 2×2 propre ; a mériterait `inequation-sens-non-inverse` |
| 6 | 3 | 4 | c | ERREUR de doublon (M5) | même calcul, même encadrement 3 < … < 3,5, mêmes pièges que publié 03/14-devoir Q7 |

### 31-devoir-comparaison-de-inverses-et-reunion-d-intervalles (d4 challenge 300/60 ✓ ; rampe 2,2,2,3,3,3,3,3 ✓)

| Q | d | ma réponse | clé | verdict | motif |
|---|---|---|---|---|---|
| 1 | 2 | (√7 + 2)/3 | b | réserve (m10) | gabarit proche du publié 02/06-defi Q4 « 3/(√7 − 2) » (mêmes pièges /5, division oubliée) |
| 2 | 2 | 2√7/3 | a | OK | |
| 3 | 2 | 2 ≤ x ≤ 5 | d | réserve (M6) | b « 1/2 ≤ x ≤ 1/5 » n'exécute PAS « l'inverse garde l'ordre » (qui donne 5 ≤ x ≤ 2) : étiquette + explication fausses |
| 4 | 3 | −1/2 ≤ 1/x ≤ −1/5 | c | OK (m9) | b encadrement vide (fidèle à l'erreur étiquetée) |
| 5 | 3 | a | a | réserve (M7) | point auteur confirmé : a et c négations l'une de l'autre → on garde a/c sans calcul |
| 6 | 3 | 10/7 ≤ … ≤ 5/3 | d | OK (m9) | |
| 7 | 3 | ]−∞ ; −2] ∪ ]3 ; +∞[ | c | OK (m11) | réunion d'intervalles au programme (manuel ch. 7 p. 102) mais enseignée par aucun cours |
| 8 | 3 | 2 | a | réserve (M8) | point auteur : posée comme « المتراجحة 1/n ≥ 1/2 » = inéquation-quotient à inconnue (hors programme) |

### 32-devoir-trinome-produit-nul-et-encadrement-de-produit (d3 boss 120/30 ✓ ; rampe 1,2,2,2,2,2,3,3,3 ✓)

| Q | d | ma réponse | clé | verdict | motif |
|---|---|---|---|---|---|
| 1 | 1 | 3 | c | réserve (m3) | même expression que Q2 : l'explication livre la borne 3 de Q2 |
| 2 | 2 | x ≤ 3 | d | réserve (m1) | étiquette `transposition` sur a (x ≥ 3/2 = DEUX erreurs) ; c (x ≤ 3/2) est la transposition seule |
| 3 | 2 | (x − 4)(x + 2) | b | réserve (m4, m5) | miroir du publié 08/17-examen-2010 Q3 (options partagées, clé ↔ distracteur) ; a muette (étiquette exacte existe) |
| 4 | 2 | {−2 ; 4} | b | OK | |
| 5 | 2 | −4 ≤ x − 4 ≤ −1 | c | OK (m9) | d vide |
| 6 | 2 | c | c | OK (m13) | |
| 7 | 3 | {−2} | c | réserve (m2) | l'énoncé donne les clés de Q2 et Q4 : question d2 réelle sous d3 |
| 8 | 3 | −20 ≤ T ≤ −2 | d | OK | point auteur : vrai mais non serré (exact −9 ≤ T ≤ −5) ; méthode imposée par l'énoncé, enseignée (cours 17, 🗡️ « الجداءات الأربعة ») ; seule option vraie |
| 9 | 3 | ∅ | d | ERREUR de forme (M9) | T non défini dans l'énoncé ; clé livrée par Q6 et Q8 ; ∅ seule de sa forme ; « رأينا » ; mêmes options que Q7 |

### 33-devoir-verifier-la-forme-puis-modeliser-une-aire (d3 boss 120/30 ✓ ; rampe 2,2,2,3,3,3 ✓)

| Q | d | ma réponse | clé | verdict | motif |
|---|---|---|---|---|---|
| 1 | 2 | x² + 3x − 18 | c | OK | |
| 2 | 2 | {−6 ; 3} | d | OK (m5) | a {3} mériterait `produit-nul-une-seule-solution` |
| 3 | 2 | x > 1 | c | réserve (m6) | d « x ≥ 1 » porte `intervalle-borne-mal-incluse` (libellé sur les crochets) |
| 4 | 3 | (x + 4)(x − 1) = 14 | d | réserve (m7, M10) | vote : produit ×2, « = 14 » ×3 → d ; l'explication « تحقّق بـ x = 3 » livre la clé de Q5 |
| 5 | 3 | 2 m et 7 m | b | ERREUR de forme (M10) | non autonome (x² + 3x − 18 à factoriser sans aide) ; option à longueurs négatives éliminée à vue ; jumeau de Q6 |
| 6 | 3 | 3 m et 8 m | a | réserve (M10) | même gabarit que Q5 (14 → 24) ; « مستطيلًا آخر » renvoie à une autre question ; option négative éliminée à vue |

## 3. Défauts classés et correctifs exacts

Tous les textes ci-dessous ont été re-résolus par sympy, mesurés (longueurs, votes), cherchés dans le publié (`git grep` sur
`origin/main:content/math`) et rendus dans Chromium `dir=rtl` (banc : « aucune formule brouillée »).

### Critiques
Aucune (0 clé fausse, aucune explication qui valide un distracteur, aucune double réponse).

### Majeurs

**M1 — 29 Q7 : doublon de 29 Q6, livré par l'explication de Q6.** Même équation (n pour x) ; l'explication de Q6 donne {0 ; 7}, d'où 13 − 2
sans calcul (et la consigne de 9ᵉ « ℕ commence à 0 ou à 1 » donne 11 dans les deux cas, le piège de division s'y dilue). Remplacement (même
étage d3, pièges de la carte : sens et transposition, plan 2×2) :
- énoncé : `ما مجموعة حلول المتراجحة التالية؟\nx² − 6x − 7 ≤ x² − 7`
- options : a `x ≤ 0` [`math.alg.inequation-sens-non-inverse`] · b `x ≥ 0` (clé) · c `x ≥ 7/3` [`math.alg.transposition-sans-changer-signe`] · d `x ≤ 7/3` (muette, deux erreurs)
- explication : `نطرح x² من الطرفين فيزول الحدّ التربيعي: −6x − 7 ≤ −7، ثمّ نضيف 7 إلى الطرفين: −6x ≤ 0. نقسم على −6 وهو سالب فتنقلب الإشارة: x ≥ 0 ✓. تحقّق: x = 1 يعطي −12 ≤ −6 وهي صحيحة، وx = −1 يعطي 0 ≤ −6 وهي خاطئة ✓. الخطأ الشائع: القسمة على −6 دون قلب الإشارة، فيخرج x ≤ 0. ومن نقل −7 إلى الطرف الأيمن دون تغيير إشارتها كتب −6x ≤ −14 فوجد x ≥ 7/3، ومن جمع الخطأين وجد x ≤ 7/3.`
- vérifs : sympy x ≥ 0 ; −14/(−6) = 7/3 ; votes 0 ×2, 7/3 ×2, ≥ ×2, ≤ ×2 ; longueurs 5/5/7/7 ; aucune occurrence publiée de « ≤ x² − 7 ».

**M2 — 29 Q8 et Q9 : non autonomes.** Les deux exigent la factorisation de x² − 6x − 7 (ou d'un trinôme x² − 9x + 14), qu'aucune forme
canonique ni factorisation de l'énoncé ne fournit (règle du lot : la forme est donnée). Tirées seules au donjon, elles sont hors programme.
Ajouter en tête des deux énoncés : `نعلم أنّ x² − 6x − 7 = (x − 7)(x + 1) لكلّ عدد حقيقي x.\n` (redonne la clé de Q2, émise avant : convention).
- Q8 devient : `نعلم أنّ x² − 6x − 7 = (x − 7)(x + 1) لكلّ عدد حقيقي x.\nما مجموع حلول المعادلة التالية؟\nx² − 6x − 7 = 3(x − 7)`
- Q9 devient : `نعلم أنّ x² − 6x − 7 = (x − 7)(x + 1) لكلّ عدد حقيقي x.\nنتأمّل المعادلة التالية ذات المجهول x، حيث k عدد حقيقي:\nx² − 6x − 7 = k(x − 7)\nما قيمة k التي تجعل لها حلًّا واحدًا فقط؟`
- (mineur lié, m8) Q9 : poser `math.alg.transposition-sans-changer-signe` sur b (6 : « k + 1 = 7 », exact) et ajouter à la fin de l'explication : ` ومن ظنّ أنّ k يساوي الحلّ 7 أجاب 7، لكنّ المعادلة تصير حينئذ (x − 7)(x − 6) = 0 ولها حلّان.` (vérifié : k = 7 → {6 ; 7}).

**M3 — 29 Q6 : la clé se reconstruit par vote.** Options {7}, {0 ; 7}, {−7 ; 0}, {−1 ; 7} : 7 trois fois, 0 deux fois → {0 ; 7}. Plan 2×2
(division × signe) : d `{−1 ; 7}` → `{−7}` (muette, deux erreurs) ; c `{−7 ; 0}` reçoit `math.alg.produit-nul-racine-signe-non-oppose` (lit
(x − 7) comme nul en −7 : exact). Dans l'explication, remplacer `ومن أهمل الطرف الأيمن حلّ A(x) = 0 فوجد {−1 ; 7}.` par
`ومن قرأ العامل (x − 7) على أنّه يُعدم عند −7 وجد {−7 ; 0}، ومن جمع الخطأين وجد {−7}.` Votes après : 7 ×2, 0 ×2, −7 ×2 ; longueurs 3/7/8/4.

**M4 — 29 Q5 a `]−5 ; 1]` : étiquette et mécanisme faux.** Diviser −10 < −2x ≤ 2 par −2 sans inverser donne 5 < x ≤ −1 (vide), pas
]−5 ; 1] ; cette option vient d'une division par +2 suivie de l'oubli du signe de −x. Retirer l'étiquette (`inequation-sens-non-inverse`) et,
dans l'explication, remplacer `الخطأ الشائع: القسمة على −2 دون قلب الإشارتين، فيخرج ]−5 ; 1].` par
`الخطأ الشائع: قسمة الأطراف الثلاثة على 2 بدل −2، فيخرج −5 < −x ≤ 1، ثمّ إسقاط الإشارة السالبة أمام x فيُكتب ]−5 ; 1].` (le piège du sens reste
testé en 31 Q7, 32 Q2 et M1).

**M5 — 30 Q6 : doublon du publié `03-calcul-litteral/exercices/14-devoir-comparer-radicaux-et-inverses.json` Q7.** Même nombre 1/(√11 − 3),
même rationalisation, même encadrement « 3 < … < 3,5 », mêmes pièges (11 − 3 = 8 → 0 < … < 1 ; division oubliée → 6 < … < 7). √13 est exclu
(4/(√13 − 3) rationalisé dans le publié 03/13). Remplacement par √15 :
- énoncé : `ما أصغر عدد طبيعي يحقّق المتراجحة التالية؟\n(√15 − 3)x > 1` — options inchangées (0 / 1 / 2 / 7) mais **clé c = 2** ; étiquettes b et d inchangées (exactes).
- explication : `العدد √15 − 3 موجب لأنّ 15 > 9، فنقسم عليه والإشارة تبقى: x > 1/(√15 − 3). نضرب البسط والمقام في (√15 + 3): 1/(√15 − 3) = (√15 + 3)/(15 − 9) = (√15 + 3)/6. بما أنّ 3 < √15 < 4 فإنّ 6 < √15 + 3 < 7، أي 1 < (√15 + 3)/6 < 7/6. فأصغر عدد طبيعي أكبر قطعًا من هذا العدد هو 2 ✓. الخطأ الشائع: كتابة المقام 15 − 3 = 12 بدل 15 − 9 = 6، فيخرج (√15 + 3)/12 وهو بين 0,5 و 0,6، فيكون أصغر عدد طبيعي 1. ومن نسي القسمة على المقام الجديد أخذ √15 + 3 بين 6 و 7 فأجاب 7. ومن قلب الإشارة وهو يقسم على موجب وجد x < (√15 + 3)/6 فأجاب 0.`
- vérifs : (√15 + 3)/6 ≈ 1,145 → 2 ; /12 ≈ 0,573 → 1 ; √15 + 3 ≈ 6,87 → 7 ; inversion → 0 ; « √15 − 3 » absent du publié.

**M6 — 31 Q3 b `1/2 ≤ x ≤ 1/5` : l'étiquette `inverse-conserve-l-ordre` et l'explication décrivent une erreur que l'option n'exécute pas**
(inverser en gardant l'ordre donne 5 ≤ x ≤ 2). Remplacer b par `5 ≤ x ≤ 2` (étiquette gardée, désormais exacte) et, dans l'explication,
`الخطأ الشائع: أخذ مقلوب الحدّين دون قلب الترتيب، فتُكتب 1/2 ≤ x ≤ 1/5 وهو حصر فارغ لأنّ 1/2 أكبر من 1/5.` par
`الخطأ الشائع: أخذ مقلوب كلّ حدّ مع الإبقاء على الترتيب، فتُكتب 5 ≤ x ≤ 2، وهو حصر فارغ لأنّ 5 أكبر من 2.` Longueurs 13/9/11/9 : la clé
n'est plus strictement la plus courte.

**M7 — 31 Q5 : a et c sont négations l'une de l'autre** (point de l'auteur confirmé) : l'une est forcément vraie, on écarte b et d sans
calcul. Remplacer c par `1/(√7 + 1) > 1/(√7 − 2)` [`math.num.inverse-conserve-l-ordre` : deux positifs, ordre gardé — exact]. Explication de
remplacement :
`العدد √7 − 3 سالب لأنّ 7 < 9، بينما √7 − 1 و √7 − 2 و √7 + 1 موجبة. إذن 1/(√7 − 3) سالب و 1/(√7 − 1) موجب، فالأوّل أصغر من الثاني: 1/(√7 − 3) < 1/(√7 − 1) ✓. الخطأ الشائع: تطبيق قاعدة «المقلوب يقلب الترتيب» على عددين مختلفَي الإشارة: من √7 − 3 < √7 − 2 يُستنتج خطأً أنّ 1/(√7 − 3) > 1/(√7 − 2)، والصواب أنّ مقلوب السالب يبقى أصغر من مقلوب الموجب. ومن نسي أنّ المقلوب يقلب ترتيب عددين موجبين احتفظ بالترتيب: من √7 − 2 < √7 − 1 كتب 1/(√7 − 2) < 1/(√7 − 1)، ومن √7 − 2 < √7 + 1 كتب 1/(√7 + 1) > 1/(√7 − 2)، والصحيح عكس الاثنين.`
Vérifs : valeurs −2,823 / 0,608 / 1,549 / 0,274 → a seule vraie ; aucune paire de négations ; vote (1er terme √7 − 3 ×2, 2ᵉ terme partagé 2/2,
relation 2/2) ne départage pas a et d ; 4 options de 23 caractères ; l'explication ne livre pas l'encadrement de Q6.

**M8 — 31 Q8 : posée comme inéquation-quotient à inconnue** (« كم قيمة … تحقّق المتراجحة التالية؟ 1/n ≥ 1/2 »), forme hors programme 9ᵉ
(point de l'auteur confirmé). Le savoir visé (comparer des inverses en examinant le signe, cours 17 § « مقارنة مقلوبَي عددين ») se teste sur
des nombres calculés. Énoncé de remplacement (options, clé et étiquettes inchangées) :
`نعتبر الأعداد الصحيحة غير المعدومة n التي تحقّق −6 ≤ n ≤ 6، ونحسب لكلّ منها مقلوبه 1/n.\nكم عددًا n منها يكون مقلوبه أكبر من 1/2 أو مساويًا له؟`
Explication de remplacement :
`مقلوب العدد السالب سالب، فلا يبلغ 1/2 الموجب: لا يصلح أيّ n سالب. أمّا للأعداد الموجبة فالمقلوب يقلب الترتيب: 1/n ≥ 1/2 يعني n ≤ 2، أي n = 1 أو n = 2. العددان المناسبان اثنان ✓. تحقّق: 1/1 = 1 و 1/2 يساويان 1/2 أو يفوقانه، و 1/3 < 1/2. الخطأ الشائع: قلب الترتيب دون فحص إشارة n، فتُكتب n ≤ 2 وتُعدّ كلّ القيم الصحيحة غير المعدومة من −6 إلى 2، أي 8 قيم، ومن أدخل 0 وهو لا مقلوب له وجد 9.`
Si l'orchestrateur juge que même ce cadrage reste une inéquation-quotient, la question est à remplacer (pas de variante du lot qui garde le piège
du signe sans quotient à inconnue, en dehors de 31 Q4 déjà présent).

**M9 — 32 Q9 : à remplacer.** (1) T n'est pas défini dans l'énoncé (donjon) ; (2) sa clé est livrée par Q6 (facteurs de signes contraires sur
[0 ; 3]) et par la clé de Q8 (T ≤ −2) — fuite en avant ; (3) ∅ seule de sa forme (point de l'auteur) ; (4) l'explication renvoie à
« رأينا » ; (5) mêmes quatre options que Q7. Remplacement (d3 conservé en position de bilan ; intervalle sur sa propre ligne) :
- énoncé : `نعلم أنّ T(x) = (x − 4)(x + 2) لكلّ عدد حقيقي x.\nنعتبر المجال التالي:\n]−2 ; 4]\nما مجموعة حلول المعادلة T(x) = 0 التي تنتمي إلى هذا المجال؟`
- options : a `{−2}` (muette, deux erreurs) · b `{4}` (clé) · c `{−2 ; 4}` [`math.num.intervalle-borne-mal-incluse`] · d `∅` [`math.num.intervalle-borne-mal-incluse`]
- explication : `حلّا المعادلة (x − 4)(x + 2) = 0 هما 4 و −2. العدد −2 لا ينتمي إلى المجال لأنّ القوس مفتوح عنده، والعدد 4 ينتمي إليه لأنّ القوس مغلق عنده. المجموعة {4} ✓. تحقّق: T(4) = 0 × 6 = 0 ✓. الخطأ الشائع: الخطأ في قراءة القوسين: من ظنّ أنّ المجال يشمل طرفه −2 أبقى الحلّين معًا، ومن ظنّ أنّه يُقصي طرفه 4 لم يجد أيّ حلّ، ومن عكس القوسين معًا وجد {−2}.`
- vérifs : {4} ; ni Q6 ni Q8 (qui portent sur [0 ; 3]) ne la livrent ; clé ≠ celle de Q7 ; « ]−2 ; 4] » absent du publié ; rendu Chromium correct.

**M10 — 33 Q4–Q6 : Q5 et Q6 sont jumelles** (même rectangle, aire 14 puis 24, même demande, mêmes pièges) ; **Q5 n'est pas autonome** (il faut
factoriser x² + 3x − 18, donné seulement en Q2) ; **l'explication de Q4 livre Q5** (« تحقّق بـ x = 3 » → 2 m et 7 m) ; les options « −7 m و −2 m »
et « −8 m و −3 m » nient la prémisse (des longueurs) et s'éliminent à vue (point de l'auteur, 33 Q5) ; Q6 « مستطيلًا آخر » renvoie à une autre
question. Correctif : Q5 devient une inéquation d'aires (piège de la carte « solution hors contrainte » porté par Q6), Q6 demande x.
- **Q5** énoncé : `x عدد حقيقي أكبر من 1. مستطيل عرضه x − 1 وطوله x + 4، ومربّع ضلعه x، والقياسات بالمتر.\nما مجموعة قيم x التي تكون عندها مساحة المستطيل أكبر من مساحة المربّع أو مساوية لها؟` (sans figure : item algébrique ; « x > 1 » redonne la clé de Q3, émise avant : convention)
  options : a `1 < x ≤ 4/3` (muette : inversion du sens en divisant par un positif) · b `x ≥ 4/3` (clé) · c `x ≥ 4` [`math.alg.coefficient-non-divise`] · d `x > 1` [`math.alg.transposition-sans-changer-signe`]
  explication : `مساحة المستطيل (x − 1)(x + 4) = x² + 3x − 4، ومساحة المربّع x². نريد x² + 3x − 4 ≥ x²، فيزول x² من الطرفين: 3x − 4 ≥ 0، أي 3x ≥ 4. نقسم على 3 وهو موجب فلا تنقلب الإشارة: x ≥ 4/3، وكلّ هذه القيم أكبر من 1 ✓. تحقّق بـ x = 2: مساحة المستطيل 1 × 6 = 6 ومساحة المربّع 4، و 6 ≥ 4 ✓. وبـ x = 1,2: مساحة المستطيل 0,2 × 5,2 = 1,04 ومساحة المربّع 1,44، فالمستطيل أصغر ✓. الخطأ الشائع: نقل −4 دون قلب إشارتها، فتُكتب 3x ≥ −4 وتصير كلّ القيم x > 1 مقبولة. ومن توقّف عند 3x ≥ 4 دون قسمة على المعامل كتب x ≥ 4، ومن قلب الإشارة وهو يقسم على 3 الموجب وجد 1 < x ≤ 4/3.`
  vérifs : sympy x ≥ 4/3 ; 1,04 < 1,44 ; longueurs 12/8/5/5 (clé ni la plus longue ni la plus courte). Cadre voisin du publié 04/07-boss Q6
  (égalité d'aires carré/rectangle, équation du 2ᵈ degré) : ici inéquation qui se réduit au 1ᵉʳ degré — tâche différente.
- **Q6** énoncé : `نريد مستطيلًا عرضه x − 1 وطوله x + 4 ومساحته 24 m²، والقياسان بالمتر. نعلم أنّ x² + 3x − 28 = (x − 4)(x + 7) لكلّ عدد حقيقي x.\nما قيمة x المناسبة لهذا المستطيل؟`
  options : a `x = 4` (clé) · b `x = −7` [`math.alg.solution-hors-contrainte-gardee`] · c `x = 3` [`math.alg.reponse-a-l-autre-inconnue`] · d `x = 7` [`math.alg.produit-nul-racine-signe-non-oppose`]
  explication : `المعادلة (x + 4)(x − 1) = 24 تؤول إلى x² + 3x − 4 = 24، أي x² + 3x − 28 = 0، أي (x − 4)(x + 7) = 0. إذن x = 4 أو x = −7. العرض x − 1 يجب أن يكون موجبًا قطعًا، والحلّ −7 يعطي عرضًا −8 m فيُسقَط. يبقى x = 4 ✓. تحقّق: العرض 3 m والطول 8 m، و 3 × 8 = 24 ✓. الخطأ الشائع: الاحتفاظ بالحلّ −7 دون اختبار إشارة البعدين. ومن قرأ العامل (x + 7) على أنّه يُعدم عند 7 وجد x = 7، ومن أعطى العرض 3 بدل x أجاب x = 3.`
  vérifs : {−7 ; 4} → 4 ; −7 n'est pas éliminable à vue (x peut être négatif a priori) ; longueurs 5/6/5/5.
- **Q4** : avec ce correctif, son « تحقّق بـ x = 3 » ne livre plus rien (à garder) ; s'il est refusé, supprimer cette phrase de l'explication de Q4.

### Mineurs

- **m1 — 32 Q2** : déplacer `math.alg.transposition-sans-changer-signe` de a (`x ≥ 3/2`, deux erreurs → muette) vers c (`x ≤ 3/2`, transposition seule, exacte).
- **m2 — 32 Q7** : l'énoncé donne les clés de Q2 et Q4 (convention acceptée) et réduit la question à un d2. Énoncé proposé : `نعلم أنّ T(x) = (x − 4)(x + 2) لكلّ عدد حقيقي x.\nما مجموعة الأعداد x التي تحقّق معًا المعادلة T(x) = 0 والمتراجحة التالية؟\n3(x + 1) ≥ 7x − 9` ; étiquettes : a `{4}` [`math.alg.inequation-sens-non-inverse`], b `{−2 ; 4}` [`math.alg.solution-hors-contrainte-gardee`] ; explication : `حلّا المعادلة (x − 4)(x + 2) = 0 هما 4 و −2. والمتراجحة: 3x + 3 ≥ 7x − 9 أي 12 ≥ 4x، ومنه x ≤ 3. العدد −2 يحقّق x ≤ 3، أمّا 4 فلا. المجموعة {−2} ✓. تحقّق: 3(−2 + 1) = −3 و 7 × (−2) − 9 = −23، و −3 ≥ −23 صحيحة ✓. الخطأ الشائع: إبقاء حلّي المعادلة معًا دون اختبار المتراجحة. ومن قسم على −4 دون قلب الإشارة وجد x ≥ 3 فاحتفظ بـ 4 وأسقط −2.`
- **m3 — 32 Q1** : même expression que Q2 ; son explication (4x = 12) livre la borne de Q2. Énoncé proposé `ما حلّ المعادلة التالية؟\n3(x + 1) = 7x − 13`, options a `5/2` [transposition] · b `7/2` [distribution-partielle] · c `4` (clé) · d `16` [coefficient-non-divise] ; explication : `ننشر الطرف الأيسر: 3x + 3 = 7x − 13. ننقل: 3 + 13 = 7x − 3x، أي 16 = 4x، ومنه x = 4 ✓. تحقّق: 3(4 + 1) = 15 و 7 × 4 − 13 = 15 ✓. الخطأ الشائع: نشر الحدّ الأوّل وحده، 3x + 1 = 7x − 13، فيخرج 4x = 14 أي x = 7/2. ومن نقل 3 دون قلب إشارتها كتب −4x = −10 فوجد x = 5/2، ومن توقّف عند 4x = 16 وأعلن 16 لم يقسم على المعامل.` (vérifié : 4 ; 5/2 ; 7/2 ; 16).
- **m4 — Gabarit « forme canonique donnée → factoriser → produit nul »** : 29 Q2–Q3, 30 Q1–Q2, 32 Q3–Q4, 33 Q1–Q2 dans le lot, et publiés 04/12 Q1, 08/17 Q3, 04/25, 04/28. Chaîne standard du concours, données distinctes : exercice parallèle accepté. Seule réserve : **32 Q3** partage deux options avec 08/17-examen-2010 Q3 (`A = (x + 1)² − 9`), dont la clé (x − 2)(x + 4) est ici le distracteur d (x + 4)(x − 2) — miroir à signe près. Si l'orchestrateur veut l'écarter : T(x) = x² − 2x − 24 = (x − 1)² − 25 = (x − 6)(x + 4) ; chaîne recalculée sur 0 ≤ x ≤ 3 : x − 6 ∈ [−6 ; −3], x + 4 ∈ [4 ; 7], produits −24, −42, −12, −21 → clé −42 ≤ T ≤ −12 ; piège ordre gardé −24 ≤ T ≤ −21 faux (T(1) = −25) ; −42 ≤ T ≤ −24 faux (T(3) = −21) ; Q7 → {−4} ; Q9 (M9) avec l'intervalle ]−4 ; 6] → {6}. (Non rendu en Chromium : à revérifier si retenu.)
- **m5 — Options muettes qui ont une étiquette EXISTANTE exacte** : 29 Q8 a `−9` → `math.alg.produit-nul-racine-signe-non-oppose` (racines lues −7 et −2) ; 30 Q5 a `x ≥ −2 − √3` → `math.alg.inequation-sens-non-inverse` ; 32 Q3 a `(x − 4)²` → `math.alg.difference-carres-confondue` (comme 29 Q2 a) ; 33 Q2 a `{3}` → `math.alg.produit-nul-une-seule-solution` ; 29 Q9 b (m8, ci-dessus). 29 Q8 b `2` (division par x − 7) reste muette à juste titre : le libellé `division-par-inconnue-perd-solution` parle de « l'inconnue » et de « la solution zéro ».
- **m6 — 33 Q3 d `x ≥ 1`** : `math.num.intervalle-borne-mal-incluse` parle de crochets ; l'option est une inégalité large (largeur nulle acceptée). Rendre muette.
- **m7 — 33 Q4** : vote (produit (x + 4)(x − 1) en b et d, « = 14 » en a, c, d) → d. Remplacer a par `x(x + 4) = 7` (muette, deux erreurs) et la dernière phrase de l'explication par `ومن نسي إنقاص العرض بـ 1 وقسم على 2 معًا كتب x(x + 4) = 7.` Longueurs 12/18/24/19.
- **m9 — Encadrements vides en distracteurs** (31 Q4 b, 31 Q6 c, 32 Q5 d, 31 Q3 b après M6) : ils exécutent exactement l'erreur étiquetée mais un élève attentif les écarte (borne inférieure > borne supérieure). Accepté (forme native de l'erreur), signalé.
- **m10 — 31 Q1** : gabarit proche du publié 02-racines-carrees/06-defi-concours Q4 (`3 / (√7 − 2)`, pièges /5 et division oubliée). Option : énoncé `ما كتابة العدد التالي دون جذر في المقام؟\n1/(√7 + 2)`, options a `√7 − 2` [rationalisation-denominateur-oublie] · b `(√7 − 2)/3` (clé) · c `(√7 − 2)/5` [difference-carres-second-terme-non-eleve-au-carre] · d `(√7 + 2)/3` ; explication : `نضرب البسط والمقام في المرافق (√7 − 2): المقام يصير (√7 + 2)(√7 − 2) = 7 − 4 = 3. إذن 1/(√7 + 2) = (√7 − 2)/3 ✓. الخطأ الشائع: الضرب في المرافق دون القسمة على المقام الجديد، فيخرج √7 − 2. ومن كتب المقام 7 − 2 = 5 لم يرفع 2 إلى المربّع، ومن غيّر إشارة البسط وجد (√7 + 2)/3.` (Q2 reste soluble ; « 1/(√7 + 2) » absent du publié.)
- **m11 — 31 Q7 : réunion d'intervalles** au programme officiel (manuel 9ᵉ ch. 7 p. 102, « Intersection ∩ et réunion ∪ d'intervalles ») mais enseignée par aucun cours de l'app (∪ n'apparaît qu'en 01 : ℝ = ℝ+ ∪ ℝ−). Hors tranche : ajouter un paragraphe au cours 04 (§ تمثيل حلول المتراجحة) ou 17. Une glose dans l'énoncé désignerait les deux options à ∪ : je ne la recommande pas.
- **m12 — Rendu** : banc Chromium sans formule brouillée sur les 5 missions. Signalements du banc 29 Q2, 32 Q3, 32 Q7 = artefacts de saut de ligne (vérifiés à l'œil). « 14 m² », « 24 m² » (33 Q4–Q6) et les options « 2 m و 7 m » s'affichent unité à gauche du nombre ; ordre de LECTURE exact, `splitMathRuns` ne les isole pas : moteur, précédent m-16 (pas de défaut de contenu ; le correctif M10 supprime les options à unités). Les intervalles en ligne (« [−1 ; 5[ », « ]−∞ ; −2] ∪ ]3 ; +∞[ », « [0 ; 3] ») ont été mesurés caractère par caractère : ordre visuel correct.
- **m13 — 32 Q6** : l'explication de Q5 (x − 4 ∈ [−4 ; −1]) donne la moitié de Q6 ; chaîne naturelle d'un devoir, d2 tous deux : accepté.
- **m14 — Étages** : 31 en d4 challenge n'a que des questions d2–d3, comme les défis publiés 04/04 (3 ×7) et 04/06 (2 et 3) : accepté. 32 Q7 et Q9 (avant correctifs) sont des d2 réels étiquetés d3 (traités par m2 et M9).

## 4. Étiquettes (libellés lus sur `origin/main`)

Exactes : 29 Q1 a, Q2 a, Q3 a/d, Q4 b/d, Q6 a, Q7 c, Q9 a ; 30 Q1 a, Q2 b/d, Q3 a/d, Q4 a/c, Q6 b/d ; 31 Q1 a/c, Q2 b/d, Q4 b, Q6 c, Q7 b/d ;
32 Q1 a/b/d, Q4 c/d, Q8 b ; 33 Q2 c, Q3 b, Q4 b/c, Q6 b/c/d.
Fausses : 29 Q5 a (M4), 31 Q3 b (M6), 32 Q2 a (m1), 33 Q3 d (m6). Muettes à étiqueter : m5. Aucune famille nouvelle nécessaire.

## 5. Doublons

- Intra-mission : 29 Q6/Q7 (M1), 33 Q5/Q6 (M10), 32 Q7/Q9 mêmes options (M9), 32 Q1/Q2 (m3).
- Publié : 30 Q6 ↔ 03/14-devoir Q7 (M5) ; 32 Q3 ↔ 08/17-examen-2010 Q3 (m4) ; 31 Q1 ↔ 02/06-defi Q4 (m10) ; 29 Q4 ↔ 04/06-defi Q2 (parallèle accepté).
- `dupscan` (adapté au ch. 04) : aucun recouvrement d'options ≥ 3 avec le publié hors réponses numériques banales (0/1/2/7…).

## 6. Bilan

38 questions auditées · **0 clé fausse** · 0 critique · **10 majeurs** (M1–M10) · 14 mineurs (m1–m14).
Questions à reprendre pour les majeurs : 29 Q5 (étiquette + explication), Q6, Q7, Q8, Q9 ; 30 Q6 ; 31 Q3, Q5, Q8 ; 32 Q9 ; 33 Q5, Q6 (12 questions).
Retouches mineures : 29 Q8 (étiquette), 30 Q5, 31 Q1 (option), 32 Q1, Q2, Q3, Q7, 33 Q2, Q3, Q4.
**Verdict : à corriger avant livraison** ; après application des correctifs ci-dessus (tous vérifiés par sympy, longueurs, votes, `git grep`
du publié et rendu Chromium), la tranche est livrable.
