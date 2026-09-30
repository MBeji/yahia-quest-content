# Audit du lot L02 : maths 9ᵉ, chapitre 03, missions d'examen 15 à 20

Toutes les clés sont justes : 35 questions sur 35, et aucun défaut critique. La tranche ne part pas en l'état : il y a 7 défauts majeurs. Quatre sont des fuites, dont deux par les titres, deux sont des étiquettes d'erreur fausses, et le dernier est un doublon avec une mission publiée. Il y a aussi 8 groupes de défauts mineurs. Les correctifs portent sur 18 questions et 2 titres. Je n'ai modifié aucun fichier.

**Ce que j'ai audité.** L'arbre de travail, fichiers inchangés depuis ma lecture. Empreintes sha256 (12 premiers caractères) :

| Fichier | Empreinte |
|---|---|
| 15 | 9af48a34710c |
| 16 | b786533fc6db |
| 17 | ffb678a12e9e |
| 18 | f4afe8946f5b |
| 19 | c68ebe2f70e9 |
| 20 | 45f7aa88e586 |
| chapter.json | 32b0d73ef88a |

J'ai relu la mission 17/16 dans sa version réécrite ce matin (06:35).

**Méthode.** J'ai résolu les 35 questions sur énoncés et options seuls, en enregistrant mes réponses avant d'ouvrir les clés et les étiquettes. Chaque donnée a été confrontée aux transcriptions officielles 2020-gén., 2023-tech., 2003, 2005, 2012-gén. et 2017-gén. : toutes sont fidèles.

---

## 1. Tableaux par fichier

### 15 — 2020-gén. ex. 1 (⭐⭐, practice 75/15)

| Q | Ma réponse | Clé | Verdict | Motif |
|---|---|---|---|---|
| 1 | 9/2 | d | réserve | (a) 1/2 porte l'étiquette « carré d'une différence » alors que c'est un carré de somme (M5). (c) 7/2 est un double produit sans son facteur 2 (m1). |
| 2 | 3√2/2 | b | OK | (a) et (d) sont muettes : racine d'un quotient prise sur un seul terme, sans étiquette au registre. |
| 3 | 9 + 3a + 3b | c | OK | |
| 4 | 6 | a | réserve | (c) 12 est muette ; `critere-divisibilite-mal-choisi` la décrit (m2). |
| 5 | 3 < 2√3 < 4 | b | réserve | (d) est muette ; `comparaison-radical-et-entier` la décrit (m2). L'erreur de (c) n'est pas nommée (m3). |
| 6 | 1 | c | réserve | « إشارة ما تحته » est imprécis (m7). |

### 16 — 2023-tech. ex. 1 (⭐⭐, practice 75/15)

| Q | Ma réponse | Clé | Verdict | Motif |
|---|---|---|---|---|
| 1 | 3 + 2√2 | b | réserve | (c) 3 + √2 : double produit sans son 2 (m1). |
| 2 | 240 ألف دينار | d | OK | Le pourcentage est enseigné (voir § 3). (a) et (b) sont muettes. |
| 3 | 10¹² | a | OK | |
| 4 | 270 | c | réserve | La lettre B désigne à la fois un sommet et l'aire de la base ; « المنشور » au lieu de « الموشور » (m4). Question à garder (§ 3). Figure juste. |

### 17 — 2003 ex. 2 (⭐⭐⭐, boss 120/30)

| Q | Ma réponse | Clé | Verdict | Motif |
|---|---|---|---|---|
| 1 | 3√5 − 1 | b | OK | |
| 2 | « 3√5 = √45 ; 1 = √1 ; 45 > 1 » | a | OK | Énoncés jugés un par un. Seul (a) est vrai et suffit. (b) : √(45 − 1) faux. (c) : 2√5 faux. (d) : vrai mais insuffisant. |
| 3 | 54 + 14√5 | b | OK | |
| 4 | 7 + √5 | c | OK | (a) est muette (ordre de la soustraction inversé). |
| 5 | 54 + 14√5 | d | réserve | (b) 54 + 7√5 : double produit sans son 2 (m1). La clé est celle de Q3 : c'est voulu par le sujet, qui demande de montrer (b − a)² = ab. |
| 6 | 1/(b − a) | c | réserve | (b) 1/(a − b) porte « additionner les dénominateurs » alors que l'option les soustrait (M6). |

### 18 — 2005 ex. 2 (⭐⭐⭐, boss 120/30)

| Q | Ma réponse | Clé | Verdict | Motif |
|---|---|---|---|---|
| 1 | 3 − √2 | c | réserve | (d) 3 + √2 est muette ; `math.int.subtract-smaller-from-larger` la décrit (m2). |
| 2 | « موجب … 3 > √2 » | d | réserve | L'explication donne a ≈ 1,59, ce qui livre le verdict de Q6 (M4). L'énoncé se lit de deux façons (m5). |
| 3 | √3 | a | OK | |
| 4 | 2(4 − 3√2) | b | réserve | L'énoncé finit par « b = √3. », qui s'affiche du mauvais côté (m6). |
| 5 | 18 ; 3√2 | d | OK | Réserve : la valeur 18 apparaît dans deux options. |
| 6 | « سالب … a² < b² … a < b » | c | OK | Énoncés jugés un par un : (a) est faux dès la première étape, (b) à la conclusion, (d) à l'étape du milieu. |

### 19 — 2012-gén. ex. 2 (⭐⭐⭐, boss 120/30)

| Q | Ma réponse | Clé | Verdict | Motif |
|---|---|---|---|---|
| 1 | 1 | a | réserve | Le titre « عددان مقلوبان » donne la clé (M1). |
| 2 | (97 + 56√3 ; 97 − 56√3) | c | réserve | (d) : double produit sans son 2 (m1). L'énoncé finit par une formule isolée suivie d'un point (m6). |
| 3 | a/b = a² | d | réserve | L'explication livre la clé de Q4 (M2). (a) est muette ; `numerateur-denominateur-inverses` la décrit (m2). |
| 4 | 194 | b | réserve | L'explication donne c² = 196 et c = 14 sous un autre nom (M3). |
| 5 | 196 | d | réserve | (a) 192 porte « carré d'une différence » sur un carré de somme (M5). (c) 195 : double produit sans son 2 (m1). Coquille « b/a . » (m8). |
| 6 | 14 | b | OK | Réserve : la difficulté 3 sert à tenir la place de la question, pas à mesurer sa difficulté. |

### 20 — 2017-gén. ex. 2 (⭐⭐⭐, boss 120/30)

| Q | Ma réponse | Clé | Verdict | Motif |
|---|---|---|---|---|
| 1 | (3 + √5)/2 | a | OK | |
| 2 | (3 − √5)/2 | d | réserve | (a) est muette alors que la même erreur est étiquetée en Q5 (d) (m2). |
| 3 | a + b = 3 و ab = 1 | a | réserve | Le titre livre ab = 1 (M1). Les options croisées 2×2 sont équilibrées. |
| 4 | 2 ≤ √5 ≤ 5/2 | c | réserve | (a) est muette, et son erreur n'est pas nommée dans l'explication (m2, m3). |
| 5 | 2,5 ≤ a ≤ 2,75 | a | OK | |
| 6 | 4/11 ≤ b ≤ 2/5 | b | OK | Amplitude 2/55 ≈ 0,036 < 0,04. L'option (d) a une amplitude de 0,04 exactement, donc pas strictement inférieure. |
| 7 | 7 | c | réserve | Doublon de la mission publiée 03/06 Q5 (M7). |

Chaque correctif proposé ci-dessous a été re-vérifié : la clé n'est jamais strictement l'option la plus longue, aucune prémisse n'est niée, aucun texte ne contient la clé d'une question servie ensuite, et aucune difficulté ne change (la rampe reste non décroissante).

---

## 2. Défauts classés et correctifs exacts

### Critique
Aucun.

### Majeurs

**M1 — Les titres de 19 et 20 livrent ab = 1.** C'est toute la clé de 19 Q1 et la moitié de celle de 20 Q3 (deux options tombent sans calcul).
- 19 : « 🏛️ مناظرة 2012 · التمرين 2 ⭐⭐⭐: عددان مقلوبان، ومربّعاهما، ومجموع جذرين » → « 🏛️ مناظرة 2012 · التمرين 2 ⭐⭐⭐: جداء عددين، ومربّعاهما، ومجموع جذرين »
- 20 : « 🏛️ مناظرة 2017 · التمرين 2 ⭐⭐⭐: عددان مقلوبان، وحصر مداه صغير، ومجموع مربّعَي مقلوبَين » → « 🏛️ مناظرة 2017 · التمرين 2 ⭐⭐⭐: مجموع عددين وجداؤهما، وحصر مداه صغير، ومجموع مربّعَين »

**M2 — L'explication de 19 Q3 donne la clé de Q4.** « a/b ≈ 194 » donne 194 directement, et « ونظيرها b/a = b² » donne la méthode. Nouvelle explication complète :
« بما أنّ ab = 1 فإنّ b مقلوب a، أي 1/b = a. ومنه a/b = a × (1/b) = a × a = a² ✓. الخطأ الشائع الخلط بين الجداء والخارج: ab = 1 لا تعني a/b = 1 (لا يتحقّق ذلك إلّا إذا كان a = b)؛ أو تبديل الحرفين فيكتب a/b = b²؛ أو الخلط بين المقلوب والمقابل، فمقابل b هو −b لا 1/b، ولو كان b = −a لكان a/b = −1. »

**M3 — L'explication de 19 Q4 donne les clés de Q5 et Q6.** Elle écrit (a + b)² = 196 et a + b = 14 ; or c = a + b. Nouvelle explication complète :
« نوحّد المقامين: a/b + b/a = (a² + b²)/(ab). وبما أنّ ab = 1 فإنّ a/b + b/a = a² + b² = (97 + 56√3) + (97 − 56√3) = 194 ✓ (الحدّان 56√3 و −56√3 يتلاشيان). الخطأ الشائع جمع البسطين والمقامين كلًّا على حدة: (a + b)/(b + a) = 1؛ أو إبدال a² + b² بمربّع المجموع (a + b)² دون طرح الجداء المضاعف 2ab؛ أو إضافة 2ab بدل طرحه في المتطابقة. »

**M4 — L'explication de 18 Q2 livre le verdict de Q6.** « a ≈ 1,59 », avec b = √3 ≈ 1,73 (clé de Q3), donne a < b.
« ومنه a = 3 − √2 > 0 ✓ (تحقّق: 3 − 1,41 ≈ 1,59). » → « ومنه a = 3 − √2 > 0 ✓. »

**M5 — L'étiquette `math.alg.carre-difference-signes` (carré d'une différence) est posée sur un carré de somme.** Options concernées : 15 Q1 (a) « 1/2 » et 19 Q5 (a) « 192 ». Il faut retirer l'étiquette (les explications décrivent déjà la bonne erreur). Aucune étiquette existante ne convient ; l'orchestrateur doit créer au registre :
- `math.alg.carre-somme-signe-double-produit` (compétence `math.alg.identites-remarquables`)
  - fr « Tu donnes le signe moins au double produit dans le carré d'une somme : (a + b)² = a² + 2ab + b² »
  - en "You give the cross term a minus sign in the square of a sum: (a + b)² = a² + 2ab + b²"
  - ar « تعطي الجداء المضاعف إشارة ناقص في مربّع المجموع: (a + b)² = a² + 2ab + b² »

Une fois l'entrée créée, étiqueter les deux options avec.

**M6 — 17 Q6 (b) « 1/(a − b) » porte `math.frac.add-denominators` (« tu additionnes les dénominateurs ») alors que l'option les soustrait.** Il faut retirer l'étiquette. Entrée à créer :
- `math.frac.soustraction-denominateurs` (compétence `math.frac.add-sous`)
  - fr « Tu soustrais les dénominateurs : 1/a − 1/b ne vaut pas 1/(a − b), il faut d'abord réduire au même dénominateur »
  - en "You subtract the denominators: 1/a − 1/b is not 1/(a − b) — bring both to a common denominator first"
  - ar « تطرح المقامين: 1/a − 1/b لا تساوي 1/(a − b)، بل نوحّد المقامات أوّلًا »

**M7 — 20 Q7 double la mission publiée 03/06 Q5.** C'est le même calcul (a + 1/a = 3 ⇒ a² + 1/a² = 7), avec la même clé, trois options communes (9, 11, 7), les mêmes pièges et la même étiquette sur 9. Je propose une réécriture qui interroge la partie « بيّن أنّ … = (a + b)² − 2ab » du sujet ; la clé reste sur (c) et la difficulté reste à 3.
- Énoncé : « a و b عددان مقلوبان يحقّقان a + b = 3. أيّ الكتابات التالية صحيحة ؟ »
- Options :
  - (a) « 1/a² + 1/b² = (a + b)² + 2ab = 11 » — muette
  - (b) « 1/a² + 1/b² = (a + b)² = 9 » — `math.alg.carre-somme-sans-double-produit`
  - (c) « 1/a² + 1/b² = (a + b)² − 2ab = 7 » — clé
  - (d) « 1/a² + 1/b² = 1/(a² + b²) = 1/7 » — `math.frac.add-denominators`
- Explication : « بما أنّ a و b مقلوبان فإنّ ab = 1 و 1/a = b و 1/b = a، إذن 1/a² + 1/b² = b² + a². ومن المتطابقة (a + b)² = a² + 2ab + b² نجد a² + b² = (a + b)² − 2ab = 3² − 2 × 1 = 7 ✓. الخطأ الشائع إسقاط الجداء المضاعف فيُكتب (a + b)² = 9 مكان a² + b²؛ أو إضافته بدل طرحه فيخرج 9 + 2 = 11؛ أو جمع المقامين فيُكتب 1/a² + 1/b² = 1/(a² + b²) فيخرج 1/7. »
- Vérifié : la clé fait 32 signes et (a) 33, donc la clé n'est pas la plus longue. C'est la dernière question, donc aucune fuite possible. L'énoncé finit par « ؟ ».

**Recouvrement 19 Q1 / 19 Q6 avec 17/16 Q4 / Q7 : résolu.** Les sujets 2011 et 2012 utilisent la même paire 7 ± 4√3. Depuis ta réécriture du chapitre 17, il ne reste en commun que deux pièges en Q1 (37 et 97) et deux options en Q6 (14 et 196). Ce sont des annales voisines, c'est acceptable. Rien n'est demandé au chapitre 17. Si tu veux réduire encore le recouvrement (facultatif) : en 19 Q1, remplacer l'option (b) « 37 » par « 49 − 16√3 », qui garde la même étiquette (seul le 4 est élevé au carré). La clé reste la plus courte et les valeurs restent croissantes (1 ; 21,3 ; 42,1 ; 97).

### Mineurs

**m1 — `math.alg.carre-somme-sans-double-produit` est posée sur un double produit écrit sans son facteur 2.** Le libellé dit que l'élève a oublié le double produit, ce qu'il n'a pas fait. Options concernées : 15 Q1 (c) 7/2, 16 Q1 (c) 3 + √2, 17 Q5 (b) 54 + 7√5, 19 Q2 (d) (97 ± 28√3), 19 Q5 (c) 195. La mission publiée 03/07 Q3 a le même usage. Entrée à créer :
- `math.alg.double-produit-sans-facteur-2` (compétence `math.alg.identites-remarquables`)
  - fr « Tu écris le double produit sans son facteur 2 : dans (a + b)², le terme du milieu vaut 2ab, pas ab »
  - en "You write the cross term without its factor 2: in (a + b)², the middle term is 2ab, not ab"
  - ar « تكتب الجداء المضاعف دون العامل 2: في (a + b)² الحدّ الأوسط هو 2ab لا ab »

Puis ré-étiqueter les cinq options.

**m2 — Options muettes qu'une étiquette existante décrit :**

| Option | Étiquette à ajouter | Remarque |
|---|---|---|
| 15 Q4 (c) « 12 » | `math.num.critere-divisibilite-mal-choisi` | correspond à l'explication (« le chiffre 4 suffirait pour la division par 4 ») |
| 15 Q5 (d) « 3 = 2√3 < 4 » | `math.num.comparaison-radical-et-entier` | |
| 18 Q1 (d) « 3 + √2 » | `math.int.subtract-smaller-from-larger` | 9 − 10 = +1 |
| 19 Q3 (a) « a/b = b² » | `math.frac.numerateur-denominateur-inverses` | |
| 20 Q2 (a) « (3 − 2√5)/2 » | `math.alg.distribution-partielle` | aligné sur 20 Q5 (d) |
| 20 Q4 (a) « 1 ≤ √5 ≤ 2 » | `math.num.comparaison-radical-et-entier` | |
| 16 Q2 (a) « 204 » (facultatif) | `math.frac.decimale-rang-du-denominateur-errone` | |

**m3 — Deux explications réfutent une option sans nommer l'erreur.**
- 15 Q5 : « أمّا 3 < 4 < 2√3 فتناقضها المقارنة 12 < 16، أي 2√3 < 4. » → « ومن كتب 2√3 = 6 (كأنّ √3 = 3) وجد (2√3)² = 36 > 16 فرتّب 3 < 4 < 2√3، والصواب 12 < 16، أي 2√3 < 4. »
- 20 Q4 : « أمّا 1 ≤ √5 ≤ 2 فيخطئ لأنّ √5 أكبر من √4 = 2. » → « ومن قدّر √5 بالتخمين أصغر من 2 كتب 1 ≤ √5 ≤ 2، والمقارنة بالمربّعات تنفي ذلك: 5 > 4 = 2²، أي √5 > 2. »

**m4 — 16 Q4 : la lettre B sert deux fois, et « المنشور » veut dire « développé » dans ce chapitre.**
- Énoncé : les lignes « حجم الهرم V يُحسب بالقانون التالي، حيث B مساحة القاعدة و h الارتفاع:\nV = (1/3) × B × h » deviennent « حجم الهرم يساوي ثلث جداء مساحة قاعدته في ارتفاعه. » La figure SVG ne change pas.
- Explication, début : « … فمساحتها B = 9 × 9 = 81. إذن V = (1/3) × 81 × 10 = 810/3 = 270 ✓ (الهرم ثلث المنشور …، ومنشوره 81 × 10 = 810). » → « … فمساحتها 9 × 9 = 81. إذن حجم الهرم (1/3) × 81 × 10 = 810/3 = 270 ✓ (الهرم ثلث الموشور الذي له القاعدة والارتفاع نفسهما، وحجم هذا الموشور 81 × 10 = 810). » La suite ne change pas.

**m5 — L'énoncé de 18 Q2 se lit de deux façons.** L'option (a) donne le bon signe avec un argument faux, et l'énoncé actuel ne dit pas lequel des deux compte.
« a = 3 − √2. أيّ الحجج التالية تحدّد إشارة a تحديدًا صحيحًا ؟ » → « نعتبر العدد:\na = 3 − √2\nأيّ الأجوبة التالية يعطي إشارة a مع تعليل صحيح ؟ »

**m6 — Deux énoncés finissent par une formule suivie d'un point latin (consigne de l'auteur).** J'ai lu `bidi.ts` : il isole en LTR tout segment qui contient √, et la ponctuation collée entre dans l'isolat. Le point s'affiche donc du mauvais côté.
- 18 Q4 : « احسب a² − b² حيث a = 3 − √2 و b = √3. » → « ما قيمة a² − b² علمًا أنّ:\na = 3 − √2\nb = √3 »
- 19 Q2 : « اكتب a² و b² منشورين حيث a = 7 + 4√3 و b = 7 − 4√3. » → « اكتب a² و b² منشورين علمًا أنّ:\na = 7 + 4√3\nb = 7 − 4√3 »
- 17 Q6, facultatif : la formule n'y est pas isolée et s'affiche juste, mais pour suivre la règle : « … عبّر عن 1/a − 1/b بدلالة b − a. » → « … ما كتابة 1/a − 1/b بدلالة b − a ؟ »

**m7 — 15 Q6 :** « فنحدّد إشارة ما تحته: » → « فنحدّد إشارة العدد المربَّع تحت كلّ جذر: »

**m8 — 19 Q5 :** « للعددين a/b و b/a . ما قيمة c² ؟ » → « للعددين a/b و b/a. ما قيمة c² ؟ »

**Libellés approchés, sans correctif exigé** (à signaler au registre si on veut élargir les libellés) :
- `termes-semblables-par-coefficient` en 17 Q2 (c) et 18 Q1 (b) : l'option réunit un nombre et un radical ; la fin du libellé colle, pas le début.
- `ordre-inverse-a-tort` en 18 Q2 (c), Q5 (b) et Q6 (b) : le début du libellé colle, la fin (« ajouter ou soustraire ») est hors sujet.

### Réserves (aucun correctif exigé)
- **15 Q5** : la phrase « ومنه 3 − 2√3 سالب و 4 − 2√3 موجب » donne les signes dont dépend Q6. C'est l'étape prévue par la décomposition, pas la clé.
- **17 Q3 et Q5** ont la même clé, par construction du sujet.
- **18 Q5** : la valeur 18 figure dans deux options (dispositif croisé 2×2).
- **19 Q6** : la difficulté 3 sert à garder la question après Q5. Le passage de 196 à 14 est une étape d'une ligne.
- **16** n'a que 4 questions, mais c'est tout le QCM officiel.

---

## 3. Arbitrages demandés

**Volume de la pyramide (16 Q4) : je la garde.**
- La transcription 2023-technique ne la marque pas. La règle R-3 vise les items marqués, venus d'un programme ancien.
- Sur le fond, ce n'est pas une notion retirée du programme. La session 2026-générale (ex. 5 Q4, « أحسب حجم الهرم ASJHD ») la demande aussi, sans formule et sans marque. Le manuel rappelle V = (1/3)Bh dans un encadré (ch. 5 p. 71) et suppose les volumes connus au ch. 4 et au ch. 13. C'est la marque de 2018-générale qui est isolée.
- Le corpus n'enseigne cette formule que dans 13-geometrie-espace, chapitre hors programme officiel. C'est pourquoi l'auteur a raison de la donner dans l'énoncé : la question teste alors une substitution et l'aire d'un carré, deux notions enseignées.
- Sans Q4, la mission tiendrait formellement (le schéma accepte une question, le seuil anti-précipitation serait de 12 s, et il faudrait 2 bonnes réponses sur 3). Mais elle serait maigre : moitié de la norme de 6 questions, un quart du sujet perdu, et le titre à reprendre. Je le déconseille.

**Pourcentage (16 Q2) : rien à ajouter.** La hausse de p % est enseignée dans le corpus : math-6eme ch. 14, § « التخفيض والزيادة — النسبة تُحسب من الثمن الأصليّ », et math-8eme ch. 05, avec le coefficient multiplicateur. La compétence `math.prop.pourcentages` existe au registre. L'ajout « من قيمته الأولى » lève la seule ambiguïté.

**Les trois écarts à l'ordre du sujet : aucune sous-question perdue.**
- **(a) 2017.** Les sous-questions 2a et 2b sont fusionnées en une question à couples de réponses. Chaque valeur y figure deux fois : pas d'indice de fréquence. La sous-question 2c passe à la fin, parce que la rampe met les parties 3a et 3b (difficulté 2) avant elle (difficulté 3). La partie 3 ne dépend pas de 2c, et 2c ne dépend que de Q3. Le seul manque est la moitié « montrer que … = (a + b)² − 2ab », et M7 la réintroduit.
- **(b) 2012.** Demander a² et b² ensemble est fidèle : le sujet le fait aussi. L'étape « a/b = a² » ajoute une marche sans rien retrancher. Son défaut est ailleurs : son explication fuit vers Q4 (M2).
- **(c) 2005.** Le verdict « le plus grand » reste demandé. L'énoncé impose la méthode (comparer les carrés) alors que le sujet la laisse libre : c'est une aide légère, acceptable à ce niveau. La différence avec 17/12 Q2 (sujet 2007, même comparaison 3√2 et 4) est réelle : un seul piège commun, la valeur 6.

---

## 4. Doublons
- **Avec les missions publiées du chapitre 03 (01 à 14)** : seulement 20 Q7 et 03/06 Q5 (M7). Les autres rapprochements ne partagent qu'une valeur, pas un calcul.
- **Entre les six missions** : aucune paire de missions de même gabarit. Le carré d'un binôme à radicaux revient dans cinq missions (15 Q1, 16 Q1, 17 Q5, 18 Q4, 19 Q2), avec des données différentes : c'est le cœur du chapitre. 17 Q2 et 18 Q2 (signe d'une différence) ont des options différentes.
- **Avec les missions d'examen 09 à 16 du chapitre 17 (arbre à jour)** : 19 Q1/Q6 face à 16 Q4/Q7 est résolu (voir plus haut). 19 Q3-Q4 face à 17/15 Q5-Q6 (sujet 2010 : A/B = A², puis A² + B²), 18 Q5 face à 17/12 Q2, et les questions de signe face à 17/12, 13 et 14 sont des annales voisines, pas des défauts.

## 5. Étiquettes que l'auteur signale absentes du registre : occurrences réelles
Sur 105 distracteurs, 32 sont muets et 73 étiquetés.

| Erreur signalée par l'auteur | Questions | Options | Détail |
|---|---|---|---|
| Fraction à numérateur somme réduite partiellement | 2 | 2 | 20 Q2 (a) muette ; 20 Q5 (d), déjà étiquetée `distribution-partielle` → aligner les deux (m2) |
| Radical oublié à l'extraction d'un carré parfait | 1 | 1 | 18 Q1 (a). L'inverse (facteur oublié), 20 Q2 (c), est aussi muet |
| Racine d'un quotient prise sur un seul terme | 1 | 2 | 15 Q2 (a) et (d) |
| Ordre d'une soustraction inversé | 1 | 1 | 17 Q4 (a) |
| Signe d'une différence déduit du signe de ses termes | 2 | 2 | 17 Q2 (d), 18 Q2 (a) |
| Signe d'un produit jugé sur un seul facteur | 1 | 1 | 18 Q6 (a). Les erreurs de signe *dans* un produit, en 17 Q3 (d) et 18 Q3 (d), sont une autre erreur, aussi muette |
| 20 % lu comme 0,02 | 1 | 1 | 16 Q2 (a) |
| Encadrement trop large | 1 | 2 | 20 Q6 (a) et (c). En 20 Q6 (d), l'erreur est « strictement » : amplitude = 0,04 |
| (√2)² = 4 | 1 | 1 | 18 Q5 (c) |

Les 20 autres options muettes portent des erreurs que la liste de l'auteur ne mentionne pas. Six d'entre elles relèvent d'une étiquette existante (m2).

## 6. Contrôles automatiques, forme, programme
- **Contrôles du moteur** : `content:check` passe (math : 1570 questions). `content:qa` ne relève rien sur les six fichiers ; sa seule erreur porte sur `07-statistiques/15-examen-2019…`, hors tranche. `content:tranche` sur le chapitre 03 : aucune clé strictement la plus longue et aucune paire proche dans la tranche. Mon propre décompte donne aussi 0 clé la plus longue sur 35.
- **Notation** : aucun chiffre arabe-indien, aucun LaTeX, aucun `$`, aucun groupe de chiffres séparé par une espace simple, aucune virgule arabe dans une notation. Le `^` de 16 Q3 suit la convention du corpus (16-puissances l'emploie).
- **Ordre, titres, étages** : l'ordre d'émission est celui des fichiers dans les six missions. La rampe est non décroissante. Étages, récompenses, étoiles, format « 🏛️ مناظرة … (تقني) » et `displayOrder` 15 à 20 sont conformes. Seul le contenu des titres 19 et 20 pose problème (M1).
- **Figure (16)** : elle est juste. Le sommet est à l'aplomb du centre de la base (point commun aux deux diagonales), la longueur 9 est portée sur l'arête [AB] entière, les arêtes cachées sont en pointillés. Elle ne donne pas la clé, et l'arabe n'apparaît que dans `<title>`.
- **Programme** : ni vecteur ni translation. Tout ce qui est testé est enseigné plus tôt dans l'ordre du manifeste, ou donné dans l'énoncé. Une exception, qui ne vient pas de la tranche : la définition « مقلوبان ⟺ ab = 1 » (manuel ch. 3 §II, p. 35-38) n'est enseignée par aucun cours du manifeste jusqu'au chapitre 03. Les missions publiées 03/07, 03/10 et 03/14 s'en servent déjà. C'est un trou de cours, mineur.
- **chapter.json** : la seule différence avec `main` est la ligne `sources[]`, identique à celle du chapitre 20 déjà publié.

## 7. Observations hors périmètre, pour l'orchestrateur
- **Transcriptions** : 2018-générale marque le volume de pyramide « hors programme en vigueur », alors que 2023-technique et 2026-générale ne le marquent pas. Il faut harmoniser, probablement en retirant la marque de 2018.
- **Placement** : l'exercice 2 de 2011-générale (ch. 17, mission 16) utilise (√3 + 2)² et un produit de conjugués, deux notions du chapitre 03. Selon la règle « chapitre le plus avancé », il relèverait du 03, comme 2012 ex. 2. Je ne demande aucun changement au chapitre 17.
- **Moteur** : un point latin collé à une formule isolée s'affiche du mauvais côté même au milieu d'une phrase. C'est le cas de 420 énoncés de maths publiés sur 1394. Cela relève de `bidi.ts` (ponctuation à sortir de l'isolat), pas de la tranche.

## 8. Chiffre final

| | |
|---|---|
| Questions auditées | 35, plus la ligne `sources[]` |
| Clés fausses | 0 |
| Défauts critiques | 0 |
| Défauts majeurs | 7 (7 questions et 2 titres) |
| Défauts mineurs | 8 groupes |
| Questions à reprendre | 18, plus 2 titres |

Les 18 questions à reprendre sont 15 Q1, Q4, Q5, Q6 ; 16 Q1, Q4 ; 17 Q5, Q6 ; 18 Q1, Q2, Q4 ; 19 Q2, Q3, Q4, Q5 ; 20 Q2, Q4, Q7. Sept d'entre elles portent un défaut majeur. Pour cinq retouches d'étiquette, il faut d'abord que l'orchestrateur crée l'entrée de registre correspondante : ce qui est proposé fait trois entrées. Je peux re-vérifier les correctifs de l'auteur une fois appliqués.
