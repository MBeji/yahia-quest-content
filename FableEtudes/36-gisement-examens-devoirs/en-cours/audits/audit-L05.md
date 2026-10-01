# Audit indépendant — tranche L05 (maths 9ᵉ, ch. 04, missions d'examen 23 à 28)

Statut : **TERMINÉ**. Auditeur indépendant : je n'ai rien écrit de ce que j'audite et je n'ai modifié aucun fichier des dépôts.

## Chiffre final

**45 questions auditées · 0 clé fausse · 9 questions à reprendre (défauts majeurs) · 0 défaut critique.**

- Les 9 questions à reprendre : 24 Q5, 25 Q8, 25 Q9, 26 Q5, 27 Q2, 27 Q3, 27 Q5, 27 Q6, 28 Q8. S'y ajoutent deux questions à déplacer sans retouche de texte : 26 Q4 et 28 Q7.
- Retouches mineures : étiquettes (23 Q5, 24 Q2, 26 Q1, 26 Q7), libellés arabes (23 Q2, 24 Q1, 24 Q6, 25 Q4, 25 Q5, 25 Q6, 26 Q5, 27 Q5), notation ∅ en 25 Q6, rendu bidi de l'explication 26 Q1, étage de la mission 23, titre de la mission 28. En option : 27 Q4.

## Périmètre et méthode

- **Périmètre** : `content/math/04-equations-inequations/exercices/23…28` (6 missions, 45 questions : 38 QCM, 2 multi, 5 numeric ; 114 distracteurs, dont 69 étiquetés et 45 muets, 31 étiquettes) et la ligne `sources[]` de `chapter.json`.
- **Références** : contenu `origin/main` fa035eef (missions publiées 01 à 22, registres, cours) ; moteur `origin/main` 779d982, dont `bidi.ts` avec #1137, #1138 et **#1139, désormais mergée** (aaec43f).
- **Résolution à l'aveugle** : chaque fichier a été extrait sans `correctOption`, `answerKey`, explication ni étiquette. Chaque question a été résolue à la main, puis revérifiée par sympy : développements, factorisations, racines, inéquations, valeurs, et chaque option recalculée. La puissance 2015 de 28 Q9 a été calculée exactement dans ℤ[√5], en grands entiers : composantes de 2 527 chiffres, produit exactement (−1, 0). Les clés n'ont été lues qu'ensuite.
- **Explications** : chaque égalité a été vérifiée par script (277 égalités entre membres consécutifs, toutes justes ; les 57 « écarts » du script sont des équations, pas des identités). Les 18 vérifications numériques en « عند x = … » ont été refaites à la main : toutes justes.
- **Gates en lecture seule** (scripts du moteur local, identiques à origin/main pour qa, build et tranche) : `content:check` valide tout le corpus, `content:qa --strict --subject math` sort à 0 avec 0 erreur, et aucun des 18 avertissements ne vise le chapitre 04. Les mesures de `content:tranche` ont été recalculées avec les fonctions du moteur, sans dossier temporaire.
- **Rendu** : les 152 lignes arabes de la tranche ont été passées dans `isolateLtrRuns` d'origin/main, puis dans bidi-js (paragraphe RTL, une ligne par bloc, lignes-équations exclues), et l'ordre affiché de chaque formule a été comparé au texte source.

## Tableaux par fichier

### 23 — examen 2008, ex. 1 (d3 boss 120/30, ordre 23) — 6/6

| Q | d | ma réponse (aveugle) | clé | verdict |
|---|---|---|---|---|
| 1 | 1 | 2x + 1 | d | OK |
| 2 | 1 | ( 1 ; 2 ) | a | OK (« زوج مرتّب » : mineur m7) |
| 3 | 2 | [−1/2 ; +∞[ | b | OK |
| 4 | 2 | (2x + 1)(2x − 1) | c | OK |
| 5 | 2 | 2x(2x + 1) | a | OK — b et c devraient porter deux étiquettes existantes (m4) |
| 6 | 2 | 0 et −1/2 | b | OK |

### 24 — examen 2009 générale, ex. 3 (d3 boss, ordre 24) — 6/6

| Q | d | ma réponse | clé | verdict |
|---|---|---|---|---|
| 1 | 1 | ( 2 ; 8 ) | c | OK |
| 2 | 1 | 3x² − 1200 | c | OK — étiquette de a inexacte (m4) |
| 3 | 2 | 3(x − 20)(x + 20) | a | OK |
| 4 | 2 | 20 (numeric exact ; −20 refusé à bon droit) | 20 | OK |
| 5 | 2 | 3x² + 2 | b | **À REPRENDRE (M1)** : clé = A, affichée par Q1, Q2 et Q4 émises avant |
| 6 | 3 | ( 19 ; 20 ; 21 ) | b | OK |

### 25 — examen 2011 générale, ex. 3 (d3 boss, ordre 25) — 9/9

| Q | d | ma réponse | clé | verdict |
|---|---|---|---|---|
| 1 | 1 | −9 (numeric) | −9 | OK |
| 2 | 1 | 0 | c | OK |
| 3 | 2 | x² − 30x + 225 | d | OK |
| 4 | 2 | (x − 15)² − 9 | b | OK |
| 5 | 2 | (x − 12)(x − 18) | a | OK |
| 6 | 2 | { 12 ; 18 } | c | OK — option « ∅ » : notation non enseignée (m6) |
| 7 | 2 | 30 − a | a | OK |
| 8 | 2 | x² − 30x + 216 = 0 | d | **À REPRENDRE (M2)** : deux options bâties sur 60, absent de l'énoncé ; clé = A = 0 |
| 9 | 3 | 12 (numeric) | 12 | **À REPRENDRE (M3)** : seule, exige une technique non enseignée |

### 26 — examen 2013 générale, ex. 3 (d3 boss, ordre 26) — 7/7

| Q | d | ma réponse | clé | verdict |
|---|---|---|---|---|
| 1 | 1 | x − 2/3 | b | OK — étiquettes (m4) et rendu de l'explication (m3) |
| 2 | 2 | 3x − 3 | a | OK |
| 3 | 2 | multi {1 ; 3/2 ; 2} | {c, d, e} | OK — ensemble exact |
| 4 | 2 | 0 | b | OK (à déplacer après Q5, voir M4) |
| 5 | 2 | x² − (1 + √2)x + √2 | c | **À REPRENDRE (M4)** : clé = définition de B, affichée par Q4 |
| 6 | 3 | (x − 1)(x − √2 − 3) | a | OK |
| 7 | 3 | { 1 ; 3 + √2 } | d | OK |

### 27 — examen 2017 générale, ex. 3 (d3 boss, ordre 27) — 6/6

| Q | d | ma réponse | clé | verdict |
|---|---|---|---|---|
| 1 | 1 | ( 37/4 ; 37/4 ) | b | OK |
| 2 | 2 | x² − 2x + 8 | a | **À REPRENDRE (M5)** : clé = E, affichée par Q1 |
| 3 | 2 | 4 − a (figure : 45 px/cm, a = 72 px = 8/5, hauteur 108 px = 12/5) | d | **À REPRENDRE (M6)** : « 4 + a » plus long que le côté, éliminé à vue |
| 4 | 2 | a² − 2a + 8 | c | OK — réserve : clé reconnaissable par analogie avec E (m2) |
| 5 | 3 | c (un carré n'est jamais négatif) | c | **À REPRENDRE (M6)** : d s'appuie sur a = 0, que l'énoncé exclut |
| 6 | 3 | { 1 } | b | **À REPRENDRE (M6)** : { −1 } et { 7 } sont hors de ]0 ; 4[, prémisse de l'énoncé |

### 28 — examen 2016 générale, ex. 3 (d4 challenge 300/60, ordre 28) — 11/11

| Q | d | ma réponse | clé | verdict |
|---|---|---|---|---|
| 1 | 2 | 6 − 2√5 | c | OK |
| 2 | 2 | 9 − 4√5 | a | OK |
| 3 | 2 | multi {√45 = 3√5 ; √80 = 2√20 ; √80 = 4√5} | {b, c, e} | OK — « 2√20 », vraie, est bien dans la clé |
| 4 | 2 | 9 + 4√5 | d | OK |
| 5 | 2 | 1 | b | OK |
| 6 | 2 | c | c | OK (les quatre options ont la même longueur, 78) |
| 7 | 2 | −80 (numeric) | −80 | OK (à déplacer après Q8, voir M7) |
| 8 | 2 | x² − 18x + 1 = 0 | a | **À REPRENDRE (M7)** : clé = A = 0, A affichée par Q7 juste avant |
| 9 | 3 | −1 (numeric, calcul exact) | −1 | OK |
| 10 | 3 | (x − 9 − 4√5)(x − 9 + 4√5) | d | OK (titre : m5) |
| 11 | 3 | { 9 − 4√5 ; 9 + 4√5 } | b | OK |

Pour les `numeric` (24 Q4, 25 Q1, 25 Q9, 28 Q7, 28 Q9) : sans tolérance, une seule valeur juste chacune, aucune réponse juste refusée ni fausse acceptée. Pour les `multi` (26 Q3, 28 Q3) : ensembles exacts, aucune option juste exclue ni fausse incluse.

## Défauts classés

### Critiques

Aucun : 45 clés sur 45 justes, aucune explication contradictoire, aucune figure fausse.

### Majeurs (M1 à M7) — 9 questions à reprendre

Motif commun de M1, M2, M4, M5 et M7 : la réponse (a) de l'auteur transforme un « بيّن أنّ » officiel dont la **cible** est l'expression même de l'exercice en « laquelle obtient-on ? ». Or cette expression est affichée par l'énoncé d'une question **émise avant** (tri stable par difficulté = ordre du fichier, toutes les rampes étant non décroissantes). La clé se choisit alors par reconnaissance, sans le calcul testé. C'est une fuite en avant par l'ordre d'émission. Les liens où l'énoncé redonne le résultat **précédent** sont, eux, sans fuite dans la route de quête (voir « Fidélité »).

**M1 — 24 Q5.** La clé « 3x² + 2 » est A, affichée par Q1, Q2 et Q4. Correctif (même calcul, cible non affichée ; la somme complète reste donnée par l'énoncé de Q6, émise après) :
- énoncé : `ننشر ثمّ نبسّط المجموع التالي حيث x عدد حقيقي:\n(x − 1)² + (x + 1)²\nما الكتابة المختصرة التي نحصل عليها ؟`
- options : a `2x²` (`math.alg.carre-difference-signes`) · b `2x² + 2` (clé) · c `2x² + 4x` (muette, deux erreurs) · d `2x² + 4x + 2` (`math.alg.carre-difference-signes`)
- explication : `نستعمل مربّع الفرق ومربّع المجموع: (x − 1)² = x² − 2x + 1 و (x + 1)² = x² + 2x + 1 ؛ فيكون المجموع (x² − 2x + 1) + (x² + 2x + 1) ، والحدّان −2x و 2x متقابلان فيلغي أحدهما الآخر ، ونجمع المربّعين 2x² والثابتين 1 + 1 = 2 ، فنجد 2x² + 2 ✓ ؛ ونتحقّق عند x = 2: 1 + 9 = 10 و 2 × 4 + 2 = 10 ✓. أمّا الخطأ الشائع فهو إعطاء الحدّ الأخير إشارة سالبة في مربّع الفرق (x − 1)² فيُكتب x² − 2x − 1 ، فيخرج المجموع 2x² ؛ أو إعطاء الجداء المضاعف فيه إشارة موجبة فيُكتب x² + 2x + 1 ، فيخرج 2x² + 4x + 2 ؛ وقد يجتمع الخطآن فيُكتب x² + 2x − 1 ويخرج 2x² + 4x.`
- Contrôles : clé non strictement la plus longue (7 signes contre 12) ; aucune prémisse niée ; voisin le plus proche à Jaccard 0,38 ; « (x − 1)² + (x + 1)² » absent du corpus publié.

**M2 — 25 Q8.** Deux défauts. (1) L'énoncé donne déjà les dimensions a et 30 − a et ne contient **pas** le périmètre : les options a `x² − 60x − 216 = 0` et b `x² − 60x + 216 = 0` n'ont aucun chemin depuis l'énoncé (éliminées à vue), et l'étiquette `perimetre-rectangle-somme-non-doublee` de b n'est pas reconstructible. (2) La clé est A = 0, trinôme affiché par Q1, Q2 et Q4. Correctif (on teste la mise en équation et le développement, cœur de 3b ; le passage à x² − 30x + 216 = 0 est donné dans l'explication et dans l'énoncé de Q9) :
- énoncé : `وحدة قياس الطول هي المتر ووحدة قياس المساحة هي المتر المربّع. بعدا مستطيل مساحته 216 هما العددان a و 30 − a. ننشر الجداء a(30 − a) في مساواة المساحة. أيّ مساواة يحقّقها العدد a ؟`
- options : a `30a + a² = 216` (`math.int.produit-signes-negatifs`) · b `30a − a = 216` (`math.alg.distribution-partielle`) · c `30a − 2a = 216` (`math.num.operation-inverse-appliquee` : a × a pris pour a + a) · d `30a − a² = 216` (clé)
- explication : `مساحة المستطيل جداء بعديه ، فنكتب a(30 − a) = 216 ؛ وننشر بضرب a في كلّ حدّ من حدّي القوس: a × 30 = 30a و a × (−a) = −a² ، فنجد 30a − a² = 216 ✓ ؛ وبنقل الحدّين 30a و −a² إلى الطرف الأيمن تنقلب إشارتاهما فنجد 0 = a² − 30a + 216 ، أي أنّ a حلّ للمعادلة x² − 30x + 216 = 0. ونتحقّق بعدد: من أجل a = 8 نجد 8 × 22 = 176 و 30 × 8 − 8² = 240 − 64 = 176 ✓. الخطأ الشائع: اعتبار الجداء a × (−a) موجبًا فيُكتب 30a + a² ؛ أو ضرب الحدّ الأوّل وحده في a وترك −a كما هو فيُكتب 30a − a ؛ أو حساب a × a على أنّه a + a = 2a فيُكتب 30a − 2a.`
- Contrôles : la clé (14 signes) est à égalité avec a et c, donc pas strictement la plus longue ; plus aucune option ne dépend d'une donnée absente ; voisin le plus proche à 0,28 ; rendu bidi vérifié.

**M3 — 25 Q9.** Lue seule (le donjon tire au hasard), la question demande de résoudre a² − 30a + 216 = 0. La complétion du carré n'est enseignée par aucun cours publié (vérifié : 03 et 04 n'enseignent que le facteur commun et les identités reconnues), et la forme utile n'est pas donnée : c'est la règle d'autonomie du gisement. Correctif, en ajoutant la forme donnée par le sujet officiel (2b) ; la question reste d3 (a² − b², produit nul, choix de la dimension) :
- énoncé : `وحدة قياس الطول هي المتر. مستطيل محيطه 60 ومساحته 216 ، وأحد بعديه a يحقّق المعادلة التالية:\na² − 30a + 216 = 0\nونعلم أنّ المساواة التالية صحيحة لكلّ عدد حقيقي a:\na² − 30a + 216 = (a − 15)² − 9\nما البعد الأصغر لهذا المستطيل ؟ اكتب العدد صحيحًا.` (explication inchangée : elle part déjà de (a − 15)² − 9)

**M4 — 26 Q5.** La clé « x² − (1 + √2)x + √2 » est littéralement la définition de B affichée par Q4 (d2, émise juste avant). Correctif minimal : **échanger Q4 et Q5 dans le fichier** (toutes deux d2, les deux sous-questions sont indépendantes). Le développement est alors émis avant tout affichage de B. Dans l'explication du développement, remplacer `و B = √2 ✓` par `و 0² − (1 + √2) × 0 + √2 = √2 ✓`, car B n'est pas encore défini à ce point. Variante qui garde l'ordre officiel : options non réduites, sur le précédent publié 04/21 Q3 (`ننشر الجداء ثمّ نتوقّف قبل جمع الحدود المتشابهة`).

**M5 — 27 Q2.** La clé « x² − 2x + 8 » est E, affichée par Q1 (d1, toujours émise avant). Correctif (la forme canonique est choisie, pas reconnue ; elle n'est affichée qu'après, par Q5 et Q6) :
- énoncé : `لتكن العبارة E حيث x عدد حقيقي:\nE = x² − 2x + 8\nنريد كتابتها على شكل مربّع يُضاف إليه عدد. أيّ كتابة تساوي E لكلّ عدد حقيقي x ؟`
- options : a `(x − 1)² + 7` (clé) · b `(x − 1)² + 9` (`math.alg.carre-difference-signes`) · c `(x − 2)² + 4` (`math.alg.double-produit-sans-facteur-2`) · d `(x − 1)² + 8` (muette)
- explication : `بمتطابقة مربّع الفرق (x − 1)² = x² − 2x + 1 ، فالحدّان x² − 2x يساويان (x − 1)² − 1 ، ومنه E = (x − 1)² − 1 + 8 = (x − 1)² + 7 ✓ ؛ ونتحقّق بالنشر: (x − 1)² + 7 = x² − 2x + 1 + 7 = x² − 2x + 8 ✓. الخطأ الشائع: إعطاء الحدّ الأخير من (x − 1)² إشارة سالبة أي x² − 2x − 1 فيخرج العدد المضاف 8 + 1 = 9 ؛ أو كتابة الجداء المضاعف دون العامل 2 فيُظنّ أنّ (x − 2)² = x² − 2x + 4 فيخرج (x − 2)² + 4 ، وهو ينشر إلى x² − 4x + 8 ؛ أو نسيان طرح 1 فيخرج (x − 1)² + 8.`
- Contrôles : options de même longueur (12) ; les trois distracteurs, recalculés, diffèrent de E ; voisin le plus proche à 0,37.

**M6 — 27 : distracteurs éliminés à vue** (prémisse « a entre 0 et 4, bornes exclues », ou figure) :
- **Q6** : a `{ −1 }` et d `{ 7 }` sont hors de ]0 ; 4[, que l'énoncé pose ; seules `{ 1 }` et `{ 2 }` restent en lice. Remplacer a par `مجموعة فارغة` (le carré cru strictement positif : S = 7 jugé impossible) et d par `{ 1 + √7 }` (on écrit (a − 1)² = 7 ; 1 + √7 ≈ 3,65 est bien dans l'intervalle). Les deux options deviennent muettes et leurs étiquettes actuelles sautent. Nouvelle phrase d'erreurs de l'explication : `الخطأ الشائع: الظنّ أنّ المربّع موجب قطعًا فلا تبلغ S العدد 7 أبدًا فتُكتب مجموعة فارغة ، مع أنّ (a − 1)² ينعدم عند a = 1 ؛ أو إسقاط الحدّ 7 من الطرف الأيسر وكتابة (a − 1)² = 7 فيخرج a = 1 + √7 ؛ أو إهمال الحدّ الثابت 1 والاكتفاء بحلّ a² − 2a = 0 فيخرج a = 2 لأنّ a = 0 خارج المجال.`
- **Q5 d** (`S أصغر ما يمكن عند طرف المجال a = 0 …`) repose sur a = 0, exclu par l'énoncé. Remplacer par `S تساوي 11 عند a = 3 ، و 11 ≥ 7 ، إذن S ≥ 7` (muette : un seul exemple ne prouve rien). S(3) = 11 est juste ; 3 ne figure pas parmi les options de Q6, donc pas de fuite ; 41 signes contre 64 pour la clé. Dans l'explication, remplacer la phrase sur a = 0 par : `أو الاكتفاء بمثال واحد كـ a = 3 التي تعطي S = 11 ، مع أنّ مثالًا واحدًا لا يثبت أنّ S ≥ 7 لكلّ قيم a`.
- **Q3 c** `4 + a` est plus long que le côté du carré, et l'explication l'avoue (`وهو أكبر من ضلع المربّع ABCD فلا يصلح`). Remplacer par `4 − a²` (muette : l'aire a² de APRT prise pour son côté a ; 6 signes contre 5 pour la clé). Retirer `operation-inverse-appliquee`. Dans l'explication : `أو طرح مساحة المربّع APRT أي a² بدل طول ضلعه a فيخرج 4 − a²`.

**M7 — 28 Q8.** La clé « x² − 18x + 1 = 0 » est A = 0, et l'énoncé de Q7 (d2, émise juste avant) affiche A = x² − 18x + 1. Correctif sans texte : **placer Q8 avant Q7 dans le fichier** (toutes deux d2). Avant Q8, aucun énoncé n'affiche alors A. Q7 redonne ensuite le trinôme, ce qui est une restitution arrière, admise. Aucune explication de Q8 ne livre k = −80.

Tous ces correctifs ont été remesurés avec les fonctions du moteur : 0 paire proche, 0 clé strictement la plus longue sur 38 QCM, voisin maximal 0,38. Rendu bidi vérifié. Les cinq calculs ont été refaits par sympy.

### Mineurs (m1 à m10)

- **m1 — Étage de 23.** Aucune question d3 (profil d1 ×2, d2 ×4). C'est le gabarit des exercices 1 publiés 04/17, 18, 19, 21 et 22, tous en **d2 practice 75/15** ; toutes les missions d'examen d3 publiées (03, 04, 07, 09, 17, 20) ont au moins une question d3. Passer 23 en `difficulty: 2`, `mode: practice`, 75/15, titre `⭐⭐`.
- **m2 — 27 Q4 (optionnel).** La clé « a² − 2a + 8 » est E(a) : reconnaissable par analogie avec Q1, plus faiblement que M5. Option : demander l'aire du seul triangle CDR — options `8 − 2a` (clé), `16 − 4a` (`math.mes.aire-triangle-sans-moitie`), `2a` et `4a` (muettes), même énoncé terminé par `ما مساحة المثلّث CDR بدلالة a ؟`. S reste donnée par l'énoncé de Q5.
- **m3 — Rendu arabe, explication de 26 Q1.** `3 × 3x = 9x` s'affiche `3x = 9x × 3` (égalité fausse à la lecture). C'est une quatrième forme, que ne couvre pas DIGIT_FIRST_FORMULA de #1139 : l'opérateur y est suivi de « 3x », pas d'une lettre. Correctif de contenu vérifié par simulation : `3 × (3x) = 9x`. Côté moteur, on pourrait accepter un nombre collé à la lettre après l'opérateur (`[+−–×÷/=^]\s*\d*[A-Za-z]`). C'est le **seul** écart d'affichage sur les 152 lignes simulées.
- **m4 — Étiquettes.** Tâches pour l'auteur :
  - 23 Q5 b `4x(2x + 1)` → `math.alg.facteur-commun-terme-non-divise` (existante ; posée sur l'analogue publié 04/17 Q5 b « (x − 2)(2x) »).
  - 23 Q5 c `(2x + 1)(2x − 1)` → `math.alg.facteur-commun-reste-oublie` (existante sur origin/main).
  - Les deux étiquettes manquent au registre de l'arbre de travail (632 entrées contre 642 sur main) : rebaser avant de les poser.
  - 24 Q2 a `3x² − 1204` : `operation-inverse-appliquee` est inexacte (« une addition au lieu d'une soustraction » ; l'erreur exécutée est l'inverse, 2 soustrait au lieu d'ajouté). **À retirer** (muette), ou élargir le libellé du registre (« … ou l'inverse »).
  - 26 Q1 d `9x − 6` → remplacer `operation-inverse-appliquee` par `math.frac.fraction-d-un-nombre-multipliee-au-lieu-de-divisee`, exacte : multiplier par 3 au lieu de prendre le tiers.
  - 26 Q1 c `x + 2/3` (muette) → `math.int.produit-signes-negatifs` : libellé élargi sur main, signe d'un produit de signes contraires.
  - 26 Q7 b : même geste que c (racine lue avec son signe apparent) sous une autre étiquette. Harmoniser sur `math.alg.produit-nul-racine-signe-non-oppose` (comme 23 Q6 d, 25 Q6 d, 28 Q11 a) ; facultatif.
- **m5 — Titre de 28.** « تعميل بفرق مربّعين » annonce la méthode de Q10 et élimine ses deux distracteurs en carré (b, c). Remplacer par « تعميل بمتطابقة ».
- **m6 — 25 Q6 a `∅`.** Le symbole n'est enseigné par aucun cours publié et n'apparaît dans aucune mission ou aucun quiz de maths 9ᵉ ; le cours 15 dit « المجموعة فارغة » en toutes lettres. Le sujet officiel 2023 l'emploie pourtant. Écrire `مجموعة فارغة` (option et explication : `فتُكتب مجموعة فارغة`), ou ajouter ∅ au cours.
- **m7 — Libellés arabes.**
  - « نعلم أنّه لكلّ عدد حقيقي x المساواة التالية: » est une tournure elliptique, sans prédicat (24 Q6, 25 Q4, 25 Q5, 25 Q6, 27 Q5). Écrire `نعلم أنّ المساواة التالية صحيحة لكلّ عدد حقيقي x:`, comme le font déjà 26 Q6 et 28 Q11.
  - 24 Q1 : « تُعطى A بالكتابة التالية لكلّ عدد حقيقي x كما يلي: » est redondant → `تُعطى العبارة A لكلّ عدد حقيقي x كما يلي:`.
  - « زوج مرتّب » (23 Q2, 24 Q1) est absent des cours ; le cours 04 et les missions publiées 19, 20 et 22 disent « ثنائية ».
  - 26 Q5 : « ثمّ نرتّب حدود النتيجة حسب القوى التنازلية » emploie un terme non enseigné et inutile, puisque toutes les options sont déjà ordonnées : supprimer.
- **m8 — Étage de 28.** d4 est défendable (l'exercice le plus dense de la tranche). Mais 3 questions d3 sur 11, contre 5 d3 sur 8 à 10 dans les d4 d'examen publiées (20/19–21). Q6 (inverses → même signe → b > 0 → comparaison) vaut honnêtement d3 ; la passer en d3 ne crée aucune fuite, puisqu'elle serait émise après Q7/Q8 et avant Q9.
- **m9 — Étiquettes défendables mais ambiguës (à garder, note seulement).**
  - 23 Q2 b `( 1 ; 5/4 )` : aussi (1/2)² lu pour 2x.
  - 24 Q5 a `3x²` : aussi (a − b)² = a² − b² appliqué aux deux carrés.
  - 25 Q2 a `720` : aussi signe du produit (−30) × 12.
  - 23 Q4 d : le libellé dit « devant la parenthèse », alors que 4x² n'en a pas.
- **m10 — 24 Q6 d `( 21 ; 22 ; 23 )`** est un remplissage muet sans chemin d'erreur. À garder : avec lui, la fenêtre centrale (clé) et `( 20 ; 21 ; 22 )` sont à égalité au vote par fréquence. Toute fenêtre « à erreur » (399–401, 199–201) ferait de la clé l'unique consensus.

## Réponses aux points d'attention

**Fidélité au sujet.** Chaque donnée est celle de la transcription : valeurs, expressions, 60 m et 216 m², puissance 2015, a ∈ ]0 ; 4[ ; la figure de 27 correspond à la description transcrite. Aucune sous-question n'est écartée ni « admise ». 25 Q9 ne demande que la plus petite dimension (3c demande les deux) : réduction acceptable pour un `numeric`, l'explication donne 12 et 18.
- (a) Les découpages qui **redonnent le résultat précédent** (23 Q2, Q5, Q6 ; 24 Q3, Q4, Q6 ; 25 Q4, Q5, Q6, Q9 ; 26 Q2, Q6, Q7 ; 27 Q5, Q6 ; 28 Q5, Q6, Q10, Q11) ne fuient pas dans la route de quête. Dans le donjon, un risque résiduel existe (tirage au hasard), inhérent au découpage et identique aux missions publiées 17 à 22. En revanche, les cinq « montrer que » dont la cible est affichée **avant** sont des fuites en avant (M1, M2, M4, M5, M7).
- (b) Les trois intermédiaires sont 24 Q3 (3x² − 1200), 25 Q6 (A = (x − 12)(x − 18)) et 26 Q2 (A développée). Chacun livre la clé de la question précédente (24 Q2, 25 Q5, 26 Q1), en arrière seulement, et aucun ne déforme le sujet. Note : 24 Q3 parle de « A » sans le définir, mais la tâche (factoriser 3x² − 1200) se lit seule.
- (c) Sortir 1c (Q9) et 2b (Q10) après 2a et la première étape de 3 ne perd ni ne déforme rien : 1c est indépendante, Q8 n'utilise pas la factorisation, Q11 vient après Q10. Mais avoir mis Q8 juste après Q7 crée M7 : placer Q8 avant Q7.
- (d) Couverture complète, vérifiée sous-question par sous-question pour les six sujets.

**Étage et rampe.** Rampes non décroissantes dans les six fichiers. Mon avis par mission :
- 23 → d2 (m1).
- 24 → d3 acceptable : même profil que la d3 publiée 09/20 (d1 ×2, d2 ×3, d3 ×1).
- 25, 26 et 27 → d3 justifié (modélisation, radicaux, deux questions d3 en 26 et 27).
- 28 → d4 (m8).

26 Q7 et 27 Q6 sont en d3 pour rester après la question dont leur énoncé ou leur explication découle. C'est défendable (d2 à d3) ; les abaisser créerait une fuite. Avec les options corrigées (M6), 27 Q6 devient réellement d3.

**Programme (R-3).** Rien hors programme : ni vecteur ni translation. Tout ce qui est testé est enseigné en 15, 01, 19, 02, 16, 17, 03 et 04 : intervalles et crochets (cours 04), identités et facteur commun (03), carré positif ou nul (02), inverse de même signe (17), parité de l'exposant (16), nombres consécutifs (04). Il y a trois exceptions : complétion du carré (M3), ∅ (m6), vocabulaire (m7). La valeur absolue n'est pas utilisée.

**Étiquettes.**
- Arbitrage 23 Q1 a `2x − 11` : garder `math.int.produit-signes-negatifs`. L'explication écrit (−3) × (−2), et le libellé élargi sur main (« deux nombres de même signe donnent un résultat positif ») nomme exactement le geste. `moins-devant-parenthese` décrirait un autre chemin, −(3x − 6), que la mission ne suit pas. Pour mémoire, le publié 03/05 Q1 b étiquette ce même geste `moins-devant-parenthese` : incohérence hors périmètre.
- Les 31 étiquettes employées existent sur main. Trois libellés y sont plus larges que dans l'arbre de travail, dont `transposition-sans-changer-signe`, qui couvre désormais les inégalités (23 Q3 d exacte avec le libellé de main). Seules sont inexactes 24 Q2 a, 26 Q1 d et 25 Q8 b (m4, M2).

Les cinq étiquettes nouvelles proposées :

| proposée | questions distinctes (tranche + publié) | libellé | décision |
|---|---|---|---|
| `facteur-commun-reste-oublie` | 04/17 Q5, 04/21 Q4, 04/22 Q5 + 23 Q5 = 4 | exact | **existe déjà** sur origin/main (#604) : ne pas recréer, la poser sur 23 Q5 c |
| `facteur-commun-reste-egal-au-facteur` | 04/17 Q5 + 23 Q5 = 2 | exact | **redondante** avec `facteur-commun-terme-non-divise` (existante, déjà sur l'analogue 04/17 Q5 b) : ne pas créer |
| `substitution-zero-annule-tout` | 23 Q2 + 24 Q1 = 2 ; 0 publiée | exact pour 23 Q2 c | sous le seuil de 3 : muette ; 23 Q2 d et 24 Q1 a sont à deux erreurs, muettes de toute façon |
| `carre-strictement-positif` | 27 Q5 (+ 27 Q6 avec M6) = 1 à 2 ; 0 publiée | exact | sous le seuil : muette |
| `nombres-consecutifs-rang-confondu` | 24 Q6 = 1 ; 0 publiée (les « متتالي » publiés sont hors sujet) | exact | sous le seuil : muette |

**Distracteurs et indices de forme.**
- Clé strictement la plus longue : 0 sur 38 QCM (hasard 25 %). Positions de clé [10, 11, 10, 7].
- Aucune option n'est somme ou différence de deux autres.
- Plans 2×2 complets, avec l'option à deux erreurs muette, sur la plupart des questions (23 Q2–Q4, Q6 ; 25 Q3, Q7, Q8 ; 26 Q5–Q7 ; 28 Q1, Q2, Q4–Q6, Q10, Q11).
- Le vote par composante ne reconstruit aucune clé (24 Q1 reconstruit un distracteur ; 24 Q3 et 25 Q5 sont à égalité entre clé et distracteur).
- Les deux énoncés `multi` n'annoncent pas le nombre de réponses. 28 Q3 casse même le « un juste par radical » grâce à √80 = 2√20.
- Les options qui nient une prémisse sont recensées en M2 et M6.

**Titres.** Format « 🏛️ مناظرة <année> · التمرين N ⭐…: … » respecté, sans suffixe pour la session générale, comme dans les missions publiées. Les étoiles correspondent à l'étage, displayOrder vaut 23 à 28, le barème est canonique. Aucun titre ne livre de résultat. Un seul annonce une méthode discriminante : 28 (m5).

**Doublons.**
- Aucune paire ≥ 0,45 selon la règle du moteur, ni avec 04/01–22, ni avec les chapitres 02, 03 (15–26), 17 (09–16) et leurs quiz, ni entre les six missions. Voisin maximal : 0,39 (26 Q7 ↔ 28 Q11) ; aucun candidat gabarit, ni inter- ni intra-chapitre.
- Parentés de tâche dues aux annales, **pas des doublons** car données et pièges diffèrent : 23 Q4 ↔ 04/17 Q3 (a² − b²), 23 Q3 ↔ 04/19 Q2 (ax + b ≥ 0), 23 Q5 ↔ 04/17 Q5 (terme égal au facteur), 28 Q10/Q11 ↔ 04/14 Q3/Q4 (forme canonique donnée puis résolution).
- Les formulations reprises pour passer sous 0,45 restent naturelles, à la tournure elliptique près (m7).

**Fuites.**
- Aucune explication ne donne la clé d'une question **suivante** au-delà des liens « استنتج » du sujet : 25 Q6 → Q9 et 28 Q5 → Q9 sont voulus par l'officiel.
- Pas de décimale de vérification. Les « secondes méthodes » (28 Q6, 28 Q9, 25 Q4) ne livrent que leur propre clé.
- Chaque énoncé se lit seul : aucun « السؤال السابق » ni « بنفس الطريقة ». Les fuites par l'ordre d'émission sont M1, M2, M4, M5 et M7.

**Rendu arabe.** 152 lignes simulées avec le moteur d'origin/main.
- 12 segments de la forme « nombre puis lettre » (216 = 225 + k, 30 − a, 60 − a, 4 − a…) ne sont justes que grâce à **#1139, désormais mergée** : couverts.
- Aucun signe collé à une lettre hors tronçon isolé, aucun « ∠ ».
- Aucun chiffre arabo-indien, tiret-moins, LaTeX, « $ », espace simple entre groupes, virgule arabe dans une notation, radicande arabe ni renvoi à une option par lettre ou ordinal.
- Seul résidu : m3 (26 Q1).

**Piège de passe.** La regex de `qa-checks.ts` (« الشكل التالي », « الرسم المجاور »…) ne trouve plus aucune occurrence dans la tranche. Les « على شكل » restants ne la déclenchent pas. Les deux renvois réels (27 Q3 « في الشكل المرسوم », 27 Q4 « الشكل أدناه ») portent bien leur figure.

**Figures (27 Q3, Q4 ; SVG identique).**
- Vraie : ABCD carré de 180 px = 4 ; APRT carré de 72 px (a = 8/5) ; P sur [AB], T sur [AD], R intérieur ; hauteur de R sur (CD) = 108 px = 12/5 = 4 − a.
- Les étiquettes « a » sont posées sur les tronçons AP et AT, pas sur un côté coupé.
- La hauteur n'est pas tracée : aucune clé donnée.
- Aucun texte arabe, `viewBox` présent, ni width ni height, primitives permises seulement (path, g, circle, text). Pas de `<title>`, ce qui n'est pas exigé.

**chapter.json.** Identique à origin/main ; la ligne « Sujets officiels de l'examen national… » est présente.
