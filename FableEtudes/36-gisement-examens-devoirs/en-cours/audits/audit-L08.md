# Audit indépendant — tranche L08 du gisement (maths 9ᵉ, chapitre 12-repere-plan, missions 10 à 15)

Auditeur indépendant (contexte vierge). Consigne : `.claude/skills/content-ingest/references/gisement-auditeur.md`
+ points d'attention de l'orchestrateur. Aucun fichier du dépôt modifié.

Statut : TERMINÉ — voir § 10 pour le chiffre final.

## 0. Résolution à l'aveugle (consignée AVANT lecture de toute clé)

Énoncés et options extraits par script sans `correctOption`, `explanation` ni `misconceptionTag`,
résolus à la main puis recalculés en arithmétique exacte (sympy, entiers Python exacts pour
3²⁰⁰⁹ + 3²⁰¹¹, 27²⁰¹⁸ − 2 × 27²⁰¹⁷, 11 111 111² − 16 = 123 456 787 654 305).

| fichier | Q1 | Q2 | Q3 | Q4 | Q5 | Q6 |
| --- | --- | --- | --- | --- | --- | --- |
| 10 (2010 ex. 1) | 5/√5 | (OJ) | 4 | x = √5 | 32 | — |
| 11 (2001 ex. 3) | 0, 1, −2, 3 | 1/2 | 3 parts, 2 prises depuis A | 5 | 10/3 | 4/3 |
| 12 (2011 ex. 1) | a = 2 ou 6 | 9 | 15 | (6 ; 0) | (1/2 ; 0) | 2 − √2 |
| 13 (2015 ex. 1) | 3a + 6 | 10, 30, 50, 70, 90 | A et C | 6 | 33 | — |
| 14 (2018 ex. 1) | (1 ; 0) | 13 | 27²⁰¹⁷ × 25 | (−1 ; −2) | 4 | 15 |
| 15 (2021 ex. 1) | 3√3 − 1 | 3 − 4√3 | 2 − √3 | 2√3 | (n − 4)(n + 4) | 15 |

Figure de 11 relevée au pixel : 12 traits en x = 36 + 24k ; A (x = 84) 3ᵉ trait, O (132) 5ᵉ, I (156) 6ᵉ,
B (204) 8ᵉ ; flèche vers la droite ; d'où A = −2, O = 0, I = 1, B = 3 (unité 24 px) — conforme à la
transcription.


## 1. Clés : comparaison avec le fichier (après la résolution à l'aveugle)

**34/34 clés concordent avec ma résolution. Aucune clé fausse.** Verdicts FINAUX ci-dessous (renvois
aux défauts du § 2 : M = majeur, m = mineur).

### 10 — 2010 générale ex. 1 (5 questions)

| Q | d | ma réponse | clé fichier | verdict | motif court |
| --- | --- | --- | --- | --- | --- |
| 1 | 1 | 5/√5 | b 5/√5 | à reprendre (M2) | clé juste ; paire quasi identique avec Q4 (3 distracteurs, pièges et explications communs) |
| 2 | 1 | (OJ) | a (OJ) | réserve (M9, cours ; m9) | juste et fidèle ; notion absente des cours de l'application ; (OA) faible |
| 3 | 1 | rang 4 | c 4 | à écarter (M3) | doublon de 07/2013 Q2 ; « 8 » = rang impossible pour 7 valeurs |
| 4 | 2 | x = √5 | b x = √5 | OK | son explication redonne la clé de Q1 (réglé par M2) ; tags possibles (m3) |
| 5 | 2 | 32 | d 32 | OK (m5) | 33 (officiel) non expliqué ; (c) 34 → nouvelle étiquette acceptée |

### 11 — 2001 ex. 3 (6 questions, figure)

| Q | d | ma réponse | clé fichier | verdict | motif court |
| --- | --- | --- | --- | --- | --- |
| 1 | 1 | 0, 1, −2, 3 | a | à reprendre (M1) | les 3 distracteurs donnent xO ≠ 0 ou xI ≠ 1 : ils nient le repère (O, I) |
| 2 | 1 | 1/2 | b | OK | |
| 3 | 1 | 3 parts, 2 depuis A | a | OK | conversion fermée de 4a valide |
| 4 | 1 | 5 | d | OK (m3) | (a) 1 → `operation-inverse-appliquee` |
| 5 | 2 | 10/3 | c | OK | |
| 6 | 2 | 4/3 | c | réserve (m2) | −16/3 place M hors de [AB] |

### 12 — 2011 générale ex. 1 (6 questions)

| Q | d | ma réponse | clé fichier | verdict | motif court |
| --- | --- | --- | --- | --- | --- |
| 1 | 1 | a = 2 ou 6 | a | réserve (m1, m3) | « كلّ قيم » (pluriel) écarte « a = 2 فقط » |
| 2 | 2 | 9 | c | OK | plan 2×2 (7 muette), remplacement 2 → 7 validé |
| 3 | 2 | 15 | c | OK | |
| 4 | 2 | (6 ; 0) | b | OK | |
| 5 | 2 | (1/2 ; 0) | d | à reprendre (M4) | repère (C, A, D) enseigné nulle part et non donné ; remplacement (1/2 ; 1/2) → (1 ; 1) validé |
| 6 | 2 | 2 − √2 | d | à reprendre (M5, M10) | −2 − √2 : distance négative, s'élimine à vue ; « (بوحدة OI) : AB = … » brouillé au rendu |

### 13 — 2015 générale ex. 1 (5 questions)

| Q | d | ma réponse | clé fichier | verdict | motif court |
| --- | --- | --- | --- | --- | --- |
| 1 | 1 | 3a + 6 | d | OK | plan 2×2 |
| 2 | 1 | 10, 30, 50, 70, 90 | a | réserve (M11) | reste valable seule si Q5 est écartée ; explication brouillée par la régression arena#1141 |
| 3 | 2 | A et C | b | OK (m3) | la règle donnée ne livre pas la clé ; (a) → `moins-devant-parenthese` |
| 4 | 2 | 6 | c | réserve (m4, m7) | exercice parallèle de 03/15-examen-2020 Q4 ; 12 s'exclut par logique (hérité) |
| 5 | 2 | 33 | a | à écarter (M8) | mêmes données et même calcul que 07/11-examen-2012 Q2 |

### 14 — 2018 générale ex. 1 (6 questions)

| Q | d | ma réponse | clé fichier | verdict | motif court |
| --- | --- | --- | --- | --- | --- |
| 1 | 1 | (1 ; 0) | a | OK | |
| 2 | 1 | 13 | b | à reprendre (M7) | « كم قيمة » : au sens du cours, 3 valeurs ; désambiguïsé par les options |
| 3 | 2 | 27²⁰¹⁷ × 25 | d | OK (m3) | (a) → `facteur-commun-signe-change` |
| 4 | 2 | (−1 ; −2) | c | OK | (d) → élargir `parallelogramme-sommets-mal-ordonnes` (§ 3.3) |
| 5 | 2 | 4 | b | OK (m3, m6) | (d) 13 → `effectif-cumule-non-cumule` ; mécanisme de 5 mal nommé |
| 6 | 2 | 15 | d | OK (m3, m7) | (c) → `facteur-commun-signe-change` ; 12 s'exclut par logique (hérité) |

### 15 — 2021 générale ex. 1 (6 questions)

| Q | d | ma réponse | clé fichier | verdict | motif court |
| --- | --- | --- | --- | --- | --- |
| 1 | 1 | 3√3 − 1 | c | à reprendre (M6) | −1 − 3√3 : valeur absolue négative, s'élimine à vue |
| 2 | 1 | 3 − 4√3 | b | OK (m3) | (a) → `racine-et-carre-confondus` |
| 3 | 2 | 2 − √3 | c | OK (m3) | (b) → `racine-et-carre-confondus` |
| 4 | 2 | 2√3 | b | à reprendre (M10) | clé juste ; « (مضروبة في OJ = 1) : AB = … » brouillé au rendu ; (d) 0 → `operation-inverse-appliquee` (m3) |
| 5 | 2 | (n − 4)(n + 4) | a | OK (m3) | (d) → `difference-carres-second-terme-non-eleve-au-carre` |
| 6 | 2 | 15 | d | OK | |

## 2. Défauts classés

### 2.1 Critiques — aucun

Aucune clé fausse, aucun distracteur juste, aucune question à deux réponses défendables, aucune
figure fausse ou manquante. Chaque donnée est celle de la transcription (10 ← 2010 ex. 1 ; 11 ← 2001
ex. 3 ; 12 ← 2011 ex. 1 ; 13 ← 2015 ex. 1 ; 14 ← 2018 ex. 1 ; 15 ← 2021 ex. 1) ; aucun item marqué hors
programme. Toutes les égalités des 34 explications ont été recalculées : aucune n'est fausse.

### 2.2 Majeurs

**M1 — 11 Q1 : les trois distracteurs nient le repère (O, I).** (b) « 0 ، −1 ، 2 ، −3 » donne xI = −1,
(c) « −1 ، 0 ، −3 ، 2 » donne xO = −1 et xI = 0, (d) « 5 ، 6 ، 3 ، 8 » donne xO = 5. Seule (a) a xO = 0
et xI = 1, ce qui est la définition même du repère (l'explication le dit : « فاصلة O هي 0 وفاصلة I هي
1 بتعريف المعيّن (O, I) »). La clé se trouve sans lire la figure. Correctif (figure inchangée, plan
2×2 : sens × origine, l'option à deux erreurs muette ; les quatre options font 6 caractères ; pas de
vote par composante, ni par signe, ni par grandeur ; rendu testé) :
- prompt : `يبيّن الشكل التالي مستقيمًا مدرّجًا بالمعيّن (O, I) حيث OI = 1 cm ، وتدريجاته متتالية ومتساوية البعد.\nما فاصلتا النقطتين A و B على الترتيب ؟\n<svg …inchangé…>`
- options : a `−2 ، 3` (clé) · b `2 ، −3` · c `−3 ، 2` · d `3 ، −2` (toutes muettes)
- explanation : `فاصلة نقطة هي عدد التدريجات التي تفصلها عن الأصل O ، بإشارة موجبة في جهة I (فاصلتها 1) وسالبة في الجهة المعاكسة. النقطة A تبعد عن O بتدريجتين في الجهة المعاكسة لجهة I ففاصلتها −2 ، والنقطة B تبعد عنها بثلاث تدريجات في جهة I ففاصلتها 3 ✓. الخطأ الشائع: عكس الاتّجاه الموجب فنجد 2 ، −3 ؛ أو العدّ انطلاقًا من I بدل O فنجد −3 ، 2 ؛ أو ارتكاب الخطأين معًا فنجد 3 ، −2.`

L'item officiel 1 demande aussi xO et xI : c'est la définition, pas un savoir à tester en QCM.

**M2 — 10 Q1 ≈ 10 Q4 : paire quasi identique dans la mission.** Même équation, trois distracteurs
identiques (√5/5, 5 − √5, 5√5), mêmes pièges et mêmes explications d'erreur. La clé de Q1 (5/√5)
vaut celle de Q4 (√5), et l'explication de Q4 contient mot pour mot la clé de Q1 (« فنجد x = 5/√5 »),
ce qui compte dans le donjon, qui tire au hasard. Correctif : Q1 devient la question de méthode
(plan 2×2 opération × nombre ; clé 19 caractères contre 22/21/18 ; clé non « union » des autres, ses
recouvrements de mots valent 6 contre 7/6/7 ; aucun résultat calculé, donc aucune fuite vers Q4 ;
rendu testé) :
- prompt : `في المعادلة التالية المجهول هو x\nx√5 = 5\nأيّ عمليّة نجريها على طرفي المعادلة لنعزل x وحده ؟`
- options : a `نضرب كلا الطرفين في √5` · b `نقسم الطرفين على √5` (clé) · c `نقسم الطرفين على 5` · d `نضرب كلا الطرفين في 5` (a : `math.num.operation-inverse-appliquee` possible ; c, d muettes, d = deux erreurs)
- explanation : `المجهول x مضروب في √5 ، والعمليّة التي تُلغي الضرب هي القسمة على العدد نفسه ، فنقسم طرفي المعادلة على √5 (وهو عدد غير معدوم) ✓ ، فيبقى x وحده في طرف. الخطأ الشائع: الضرب في √5 بدل القسمة عليه فيصير الطرف الأوّل 5x لا x ؛ أو القسمة على 5 ، العدد الموجود في الطرف الآخر ، فيبقى x√5/5 لا x ؛ أو الجمع بين الخطأين بضرب الطرفين في 5 فيصير الطرف الأوّل 5x√5.`

**M3 — 10 Q3 : doublon d'une question publiée, et une option impossible.** C'est la question de
07/12-examen-2013-generale-ex1 Q2 (rang du médian d'une série impaire rangée) : n = 9 là-bas, n = 7
ici, les mêmes quatre mécanismes ((n + 1)/2, n/2, (n − 1)/2, n + 1), et une explication identique
au mot près hors les nombres. De plus, « 8 » est un rang qui n'existe pas dans une série de 7 valeurs :
l'option s'élimine à vue. C'est une étape d'auteur, pas un item officiel : rien ne justifie de la
garder. Correctif : supprimer Q3. Le calcul (7 + 1) ÷ 2 = 4 reste dans l'explication de Q5, et la
mission passe à 4 questions (trois missions d'examen publiées en ont 4).

**M4 — 12 Q5 : le repère (C, A, D) n'est enseigné nulle part et n'est pas donné.** Le cours publié
du chapitre 12 ne définit que (O ; i ; j), par des vecteurs. Le manuel officiel (ch. 9, p. 135–136,
140, 144–146) enseigne le repère défini par trois points non alignés, pas l'application. Les
techniques (a) et (b) sont données dans l'énoncé, celle-ci ne l'est pas. De plus, « المعيّن » veut
dire « losange » dans le cours 18 : à côté d'un parallélogramme, « المعيّن (C, A, D) » peut se lire
« le losange CAD ». Correctif (formulation calquée sur la définition officielle de (O, I, J), sans
écrire les coordonnées de A ; rendu testé) :
- prompt : `ليكن ABCD متوازي أضلاع ، ونذكّر أنّ قطريه [AC] و [BD] لهما المنتصف نفسه وهو مركزه I.\nونذكّر أنّ المعيّن (C, A, D) أصله C ، ومحور فواصله المستقيم (CA) ووحدته الطول CA ، ومحور ترتيباته المستقيم (CD) ووحدته الطول CD.\nما إحداثيّتا I في المعيّن (C, A, D) ؟`
- options, clé et explication inchangées.

Deux points restent notés sans correctif. L'option (1 ; 0), étiquetée `milieu-sans-moitie`, coïncide
avec A : c'est inhérent à une somme non divisée par 2 quand l'autre extrémité est l'origine. L'autre
issue est de compléter le cours 12 (écart connu).

**M5 — 12 Q6 : l'option de remplacement « −2 − √2 » est une distance négative évidente.** Elle
s'élimine à vue (l'explication le dit pour √2 − 2 : « والبعد لا يكون سالبًا »). Avec √2 − 2, négatif
lui aussi (erreur classique étiquetée, à garder), la question se joue à deux options. Le remplacement
n'est pas faux et il évite bien le piège de l'officiel 2√2 (= (2 + √2) − (2 − √2)), mais il échange un
indice de forme contre un autre. Correctif : (b) `−2 − √2` devient (b) `√2`, étiquette
`math.alg.reponse-a-l-autre-inconnue` (même usage que 11 Q4 (c) « 3 = OB »). √2 n'est ni somme ni
différence de deux options, la clé n'est pas strictement la plus longue et il n'y a pas de vote.
Explication complète, qui intègre aussi le correctif de rendu M10 (rendu testé sur le moteur
`origin/main` avec #1141 : 0 défaut) :
`البعد AB ، بوحدة الطول OI ، هو القيمة المطلقة لفرق الفاصلتين : AB = |−2 − (−√2)| = |√2 − 2|. ولمّا كان √2 < 2 (لأنّ 2 = √4 و √2 < √4) فإنّ √2 − 2 عدد سالب، وقيمته المطلقة هي مقابله : AB = 2 − √2 ✓. الخطأ الشائع: ترك الفرق دون قيمة مطلقة فنجد العدد السالب √2 − 2 ، والبعد لا يكون سالبًا ؛ أو توزيع القيمة المطلقة على الحدّين فنجد |−2| + |√2| = 2 + √2 ، وهذا خطأ لأنّ |a + b| لا تساوي |a| + |b| في الحالة العامّة ؛ أو الخلط بين البعد AB وبعد النقطة A عن الأصل O فنجد |−√2| = √2.`

**M6 — 15 Q1 : l'option d'auteur « −1 − 3√3 » est une valeur absolue négative évidente.** Ses deux
termes sont négatifs, elle s'élimine à vue ; avec 1 − 3√3 (erreur classique à garder), la question
se joue à deux options. Correctif, conforme au précédent publié pour ce piège (17/10-examen-2002 Q2 (d)
« √2 » et 03/24-examen-2023-technique Q2 (c) « 5√2 », même étiquette) : (a) `−1 − 3√3` devient
(a) `2√3`, étiquette `math.alg.termes-semblables-par-coefficient`. Le vote par composante donne
(1 ; 3√3) = (d), pas la clé ; la clé n'est pas strictement la plus longue ; aucune somme ni différence
de deux options ; rendu testé. L'écho avec la clé de Q4 (2√3) est sans conséquence : le calcul est
différent. Dans l'explication, remplacer `أو أخذ المقابل للحدّ الأوّل وحده فنجد −1 − 3√3` par
`أو جمع 1 و −3√3 كأنّهما حدّان متشابهان فنجد 1 − 3√3 = −2√3 ثمّ |−2√3| = 2√3`.

**M7 — 14 Q2 : l'énoncé n'est désambiguïsé que par les options.** Dans le vocabulaire du cours 07,
« القيمة » est une valeur du caractère, et son « تكرار » le nombre de fois où elle apparaît. « كم قيمة من
قيم هذه السلسلة لا تتجاوز 0 » vaut donc 3 (−2, −1, 0), qui n'est pas proposé ; 13 compte des
apparitions. L'explication prolonge la confusion (« من أصل 20 قيمة ») et parle d'un « العمود المجاور »
alors que l'énoncé présente deux lignes, pas un tableau. Correctif (rendu testé ; ma première
version écrivait « (من تكرار كلّي 20) ✓ », ce qui laisse « ) » dans l'isolat « 20) ✓ », d'où la
formulation sans parenthèse ci-dessous) :
- dernière ligne du prompt : `كم مرّة تظهر في هذه السلسلة قيمة لا تتجاوز 0 ؟`
- explanation : `التكرار المجمّع الصاعد عند قيمة هو مجموع تكرارات القيم الأصغر منها أو المساوية لها : فالعدد 13 المقابل للقيمة 0 هو عدد مرّات ظهور القيم −2 و −1 و 0 ، من تكرار كلّي قدره 20 ✓ ، أي القيم التي لا تتجاوز 0. الخطأ الشائع: قراءة التكرار المجمّع للقيمة الموالية ، فالعدد 18 يوافق القيمة 1 أي القيم التي لا تتجاوز 1 ؛ أو استعمال الاتّجاه المعاكس فتُعدّ مرّات ظهور القيم التي لا تقلّ عن 0 فنجد 11 ؛ أو إعطاء التكرار الكلّي 20.`

**M8 — 13 Q5 (doublon assumé) : verdict net, ÉCARTER.** Mêmes données (5 classes, effectifs 220,
490, 210, 60, 20), même calcul (moyenne pondérée par les centres, 33 400 ÷ 1 000 = 33,4), même
famille de piège (borne au lieu du centre) et mêmes sommes dans l'explication que 07/11-examen-2012
ex. 5 Q2, publié (clé 33,4). Le QCM de 2015 n'ajoute que l'arrondi à 33. Changer l'angle obligerait à
quitter l'item officiel ; garder la question fait refaire deux fois le même calcul sur les mêmes
données, y compris dans un même donjon. Q2 (centres de classes, sans effectifs) reste une question d1
autonome et valable, et la mission garde 4 questions.

**M9 — 10 Q2 : notion testée non enseignée (défaut du COURS, hors tranche).** « Points de même
abscisse ⟹ droite parallèle à (OJ) » n'est enseigné par aucun cours de l'application : le cours 12
passe par les vecteurs, et le manuel officiel l'enseigne p. 139–140. La donner dans l'énoncé
livrerait la clé ; l'auteur a raison de ne pas la donner. La question est juste et fidèle : c'est au
cours 12 d'ajouter la section, dans l'écart connu déjà remonté au propriétaire. Cette question ne
compte pas parmi les questions à reprendre.

**M10 — Rendu brouillé (autre chaîne, non couverte par #1137 à #1141) : 12 Q6 et 15 Q4,
explications.** Une parenthèse de prose arabe se ferme sur un symbole latin, et une formule suit
dans le même segment : « (بوحدة OI) : AB = |−2 − (−√2)| = |√2 − 2| » et « (مضروبة في OJ = 1) : AB =
|√3 − (−√3)| = |2√3| = 2√3 ✓ ». `splitMathRuns` (`origin/main`, #1141 compris) isole
`OI) : AB = …` et `OJ = 1) : AB = …` : le « ) » reste au MILIEU de l'isolat, alors que #1141 ne retire
une parenthèse qu'au bord d'un segment. Dans Chromium `dir="rtl"`, les deux parenthèses se
dessinent dans le même sens, et le couple enferme « بوحدة … : AB = … » en laissant « OI » (ou
« OJ = 1 ») dehors. Le cas existait avant #1141 et n'a pas changé. Correctifs (rendu testé :
parenthèses, ordre interne, formules mêlées, 0 défaut) :
- 12 Q6 : l'explication complète est donnée en M5 (première phrase
  `البعد AB ، بوحدة الطول OI ، هو القيمة المطلقة لفرق الفاصلتين : AB = |−2 − (−√2)| = |√2 − 2|.`).
- 15 Q4, explanation complète : `للنقطتين A و B الفاصلة نفسها 0 ، فهما على محور الترتيبات. وبما أنّ OJ = 1 فبعدهما هو القيمة المطلقة لفرق الترتيبتين : AB = |√3 − (−√3)| = |2√3| = 2√3 ✓. تحقّق : الترتيبتان متقابلتان ، فـ O منتصف [AB] و AB = 2 × OA = 2 × √3 = 2√3 ✓. الخطأ الشائع: جمع الترتيبتين بدل طرحهما فنجد √3 + (−√3) = 0 ؛ أو ضرب البعدين OA و OB بدل جمعهما فنجد √3 × √3 = 3 ؛ أو الوصول إلى AB² = 12 ثمّ تبسيط √12 بإخراج العامل الخطأ فنجد 3√2 بدل 2√3 ، والصواب أنّ العامل الذي يخرج من الجذر هو المربّع الكامل 4 = 2².`

Seule la première phrase change ; le reste est identique à l'existant.

**M11 — 13 Q2, explication : brouillée par une RÉGRESSION du moteur (arena#1141).** Le texte est
« و (80 + 100) ÷ 2 = 90 ✓ (والفرق بين مركزين متتاليين 20 وهو طول الفئة). » Avant #1141 (`779d982`),
l'isolat était `(80 + 100) ÷ 2 = 90 ✓`, ce qui est juste. Avec #1141 (`ec8c637`), il devient
`80 + 100) ÷ 2 = 90 ✓ (`. La nouvelle boucle d'attaque de `peelEdgePunctuation` voit
count("(") > count(")") et retire la « ( » INITIALE, qui est appariée ; la « ( » finale, qui n'a pas de
compagne, reste dans l'isolat. Dans Chromium, « (80 + 100) » perd sa parenthèse ouvrante et la
parenthèse arabe s'ouvre dans la formule. Ce n'est pas propre à la tranche : sur l'arbre de travail
du corpus (100 104 lignes arabes), #1141 fait passer de 77 à 112 les isolats qui finissent par « ( ».
Cela fait **35 lignes nouvellement cassées** (math 20, math-7eme 11, math-8eme 4, dont des missions
publiées des chapitres 01, 02 et 03, par ex. « (−3) × (−4) = 12 (سالب × سالب = موجب)، … ») et
0 réparée de ce type.
- À remonter au moteur : ne retirer une « ( » initiale que si elle n'a pas de compagne dans le segment
  (compteur de profondeur), ou traiter la queue avant l'attaque.
- Contournement de contenu (rendu testé, 0 défaut), explanation complète de 13 Q2 :
  `مركز الفئة هو معدّل حدّيها : (0 + 20) ÷ 2 = 10 ، و (20 + 40) ÷ 2 = 30 ، و (40 + 60) ÷ 2 = 50 ، و (60 + 80) ÷ 2 = 70 ، و (80 + 100) ÷ 2 = 90 ✓ ؛ والفرق بين مركزين متتاليين 20 ، وهو طول الفئة. الخطأ الشائع: تعويض كلّ فئة بحدّها الأدنى فنجد 0 و 20 و 40 و 60 و 80 بدل مركزها ؛ أو أخذ طول الفئة 20 لكلّ فئة ؛ أو أخذ نصف حدّها الأعلى فنجد 20 ÷ 2 = 10 و 40 ÷ 2 = 20 و 60 ÷ 2 = 30 و 80 ÷ 2 = 40 و 100 ÷ 2 = 50.`

### 2.3 Mineurs

- **m1 — 12 Q1 : énoncé au pluriel.** « كلّ قيم الرقم a » (pluriel) écarte « a = 2 فقط » sans calcul.
  Prompt : `العدد 6b87a مكتوب بخمسة أرقام حيث a و b رقمان. بأيّ شرط على الرقم a يقبل هذا العدد القسمة على 4 ؟`
  (options inchangées ; (c) reste la plus longue ; rendu testé).
- **m2 — 11 Q6 (a) « −16/3 » place M hors de [AB], ce que l'énoncé exclut.** −16/3 < −2 = xA. Correctif
  facultatif : (a) `−4/3` (2/3 pris pour une longueur en cm : xM = −2 + 2/3). Dans l'explication,
  remplacer `أو وضع M على يسار A بدل يمينها ، أي طرح البعد من فاصلة A ، فنجد −2 − 10/3 = −16/3` par
  `أو اعتبار 2/3 طولًا بالسنتمتر بدل كسر من AB فنجد xM = −2 + 2/3 = −4/3`. −4/3 est dans [−2 ; 3],
  la clé 4/3 reste la plus courte, et on obtient une 3ᵉ occurrence de l'erreur de 11 Q3 (d) et Q5 (a).
  Réserve assumée : −4/3 et 4/3 forment une paire d'opposés. Garder 10/3 (> xB), l'erreur « AM pris
  pour xM » étant la plus fréquente.
- **m3 — étiquettes existantes non posées** (détail § 3.2) : 14 Q5 (d), 14 Q3 (a), 14 Q6 (c), 15 Q5 (d),
  15 Q2 (a), 15 Q3 (b), 11 Q4 (a), 15 Q4 (d), 12 Q1 (c), 13 Q3 (a).
- **m4 — 13 Q4 ≈ 03/15-examen-2020-generale-ex1 Q4 (publié).** L'examen de 2020 recycle l'item de
  2015 : même clé 6, trois options communes (6, 12, 15), mêmes pièges, et dans l'explication le même
  argument « a4 ∈ {14, 34, 54, 74, 94} ». Les données diffèrent (a1a1a4 contre 5bababa4). Verdict :
  GARDER comme exercice parallèle voulu (item officiel source, autres données), à justifier au rapport
  de tranche. Harmoniser l'étiquette de l'option « 12 » : `divisibilite-un-seul-critere` ici,
  `critere-divisibilite-mal-choisi` en 03/15. Si le propriétaire refuse tout quasi-doublon, écarter 13 Q4
  laisserait la mission 13 avec deux étapes orphelines : il faudrait alors écarter la mission entière.
- **m5 — 10 Q5 : le distracteur officiel 33 n'est pas expliqué.** Ajouter à l'explication
  `؛ أو أخذ القيمة ذات الرتبة 5 بدل 4 فنجد 33` (33 est bien la 5ᵉ valeur rangée).
- **m6 — 14 Q5 : mécanisme mal nommé pour 5.** « طرح التكرارين بترتيب خاطئ » : 18 − 13 n'est pas
  l'inverse de 13 − 9. Remplacer par
  `أو طرح التكرار المجمّع للقيمة 0 من التكرار المجمّع للقيمة الموالية 1 ، أي 18 − 13 = 5 ، وهو تكرار القيمة 1 لا 0`.
- **m7 — élimination logique héritée des options officielles.** En 13 Q4 et 14 Q6, « 12 » ne peut pas
  être l'unique clé quand « 6 » est proposé (12 | N ⟹ 6 | N). C'est le cas du sujet officiel ; à noter
  seulement.
- **m8 — clé « 15 » répétée.** Trois « يقبل القسمة على » de la tranche ont la clé 15 (12 Q3, 14 Q6,
  15 Q6), comme dans les sujets officiels ; 13 Q4, où 15 est un distracteur, fait contrepoids. À noter
  seulement.
- **m9 — 10 Q2 (d) « (OA) » : distracteur d'auteur faible.** (OA) coupe (AB) en A. L'explication le
  réfute ; on peut le garder.
- **m10 — `chapter.json`.** La ligne ajoutée est identique mot pour mot à celle des chapitres 03, 04,
  07, 09 et 17 : validée. Mais la ligne préexistante « Calibré sur des devoirs et des sujets d'examen
  publics (étude 27, T2′, aucune reprise) » contredit désormais la « reprise citée ». L'aligner sur les
  autres chapitres : `Calibré sur des devoirs publics (étude 36, T2′, aucune reprise) — carte : programmes-officiels/sources-externes/web-9eme-base-math/fiche.md`.
- **m11 — cours 12 (hors tranche, à remonter).** (i) Le cours affirme que « صيغ المسافة والمنتصف تحتاج
  الاثنين معًا » (repère orthonormé), ce qui est faux pour le milieu. 14 Q1, 14 Q4 (repère non dit
  orthonormé, fidèle au sujet) et 12 Q5 sont justes et contredisent le cours. (ii) Le vocabulaire
  officiel « معيّن (O, I, J) » et « مستقيم مدرّج بالمعيّن (O, I) » est absent des cours : le cours 12
  dit « المعلّم (O ; i ; j) », et le cours 18 emploie « معيّن » au sens de losange (homographe que le
  manuel signale). La tranche est cohérente avec les missions d'examen publiées du chapitre 09, qui
  écrivent « (O, I, J) معيّن متعامد » ; au cours 12 d'introduire le terme officiel. (iii) Les
  symétriques par rapport aux axes, donnés dans l'énoncé de 13 Q3, sont à ajouter au cours.

## 3. Étiquettes

### 3.1 Les 43 options étiquetées (18 identifiants, tous au registre d'`origin/main`) : toutes exactes

Pour chaque option, le libellé nomme l'erreur exécutée :

- `numerateur-denominateur-inverses` : 10 Q1 (a), 10 Q4 (a), 11 Q5 (d)
- `milieu-sans-moitie` : 11 Q2 (c), 12 Q5 (b), 14 Q1 (d)
- `signe-ignore-dans-somme` : 11 Q2 (d), 14 Q1 (c)
- `fraction-d-un-nombre-etape-oubliee` : 11 Q3 (c), 11 Q5 (b)
- `reponse-a-l-autre-inconnue` : 11 Q4 (c), 11 Q6 (d), 12 Q2 (d), 14 Q5 (a) (« une autre grandeur que celle demandée »)
- `critere-divisibilite-mal-choisi` : 12 Q1 (d), 13 Q4 (d), 15 Q6 (a)
- `divisibilite-un-seul-critere` : 12 Q4 (a, d), 13 Q4 (a, b), 14 Q6 (a, b), 15 Q6 (b, c)
- `puissance-confondue-avec-produit` : 12 Q2 (a), 12 Q3 (d) (erreur en amont : 3² = 6 ⟹ 7 ⟹ 21)
- `valeur-absolue-signe-du-contenu-non-teste` : 12 Q6 (a), 15 Q1 (b), 15 Q3 (a)
- `valeur-absolue-somme-additive` : 12 Q6 (c), 15 Q1 (d)
- `moins-devant-parenthese` : 13 Q3 (c), 15 Q1 (a)
- `borne-de-classe-au-lieu-du-centre` : 13 Q2 (b), 13 Q5 (c)
- `cumul-croissant-decroissant-confondus` : 14 Q2 (a)
- `mode-mediane-confondus` : 10 Q5 (a)
- `distribution-partielle` : 15 Q2 (c), 15 Q3 (d)
- `racine-extraction-facteur-inversee` : 15 Q4 (a)
- `difference-carres-confondue` : 15 Q5 (b)
- `racine-confondue-avec-moitie` : 15 Q5 (c)

Aucune étiquette `math.vec.*` employée ne cite un vecteur (`milieu-sans-moitie` : « Tu additionnes
les coordonnées sans prendre la moitié… »). Les compétences `math.vec.repere-coordonnees` et
`math.vec.repere-calculs` n'en citent pas non plus. Le choix de ne pas employer
`parallelogramme-sommets-mal-ordonnes`, dont le libellé est vectoriel, est validé. Libellés élargis
vérifiés : `racine-distribuee-sur-somme` couvre désormais « une somme ou une différence » (aucune
option de la tranche n'exécute cette erreur) ; `effectif-cumule-non-cumule` couvre désormais « l'effectif
d'une classe (ou d'une valeur) et son effectif cumulé », ce qui s'applique à 14 Q5 (d) (ci-dessous).

### 3.2 Options muettes qui méritent une étiquette EXISTANTE

| option | erreur exécutée | étiquette existante |
| --- | --- | --- |
| 14 Q5 (d) 13 | effectif cumulé pris pour l'effectif | `math.stat.effectif-cumule-non-cumule` (libellé élargi, exact) |
| 14 Q3 (a) 27²⁰¹⁷ × 29, 14 Q6 (c) 29 | signe changé en mettant en facteur (27 + 2) | `math.alg.facteur-commun-signe-change` (exact) |
| 15 Q5 (d) (n − 16)(n + 16) | l'élève croit (n − 16)(n + 16) = n² − 16 | `math.alg.difference-carres-second-terme-non-eleve-au-carre` (exact ; l'explication le dit : « يساوي … − 16² لا … − 16 ») |
| 15 Q2 (a) −3√3, 15 Q3 (b) −1 | √3 × √3 = √3 | `math.num.racine-et-carre-confondus` (précédent publié pour la même erreur : 03/18-examen-2005 Q3 (c), 03/20-examen-2017 Q1 (d)) |
| 11 Q4 (a) 1, 15 Q4 (d) 0 (et 11 Q2 (a) −5/2) | somme au lieu de différence (ou l'inverse) | `math.num.operation-inverse-appliquee` (« جمعًا بدل الطرح », exact) |
| 12 Q1 (c) a ∈ {0, 4, 8} | critère « dernier chiffre » appliqué à 4 | `math.num.critere-divisibilite-mal-choisi` (cohérence avec 13 Q4 (d), même erreur, déjà étiquetée) |
| 13 Q3 (a) A et B | signe moins appliqué à √2 seul : −(1 − √2) lu 1 + √2 | `math.alg.moins-devant-parenthese` (comme (c)) |
| 10 Q1 (c), 10 Q4 (c) 5 − √5 | x√5 lu x + √5 | `math.num.operation-inverse-appliquee` (« جمعًا بدل الضرب ») |
| 10 Q1 (d), 10 Q4 (d) 5√5 | multiplier au lieu de diviser | `math.num.operation-inverse-appliquee` (« l'opération contraire ») |

Facultatif : 12 Q5 (a) (0 ; 1/2) et 14 Q4 (b) (−2 ; −1) sont aussi la clé aux coordonnées échangées,
donc `math.vec.coordonnees-point-inversees` (sans vecteur) si l'explication cite ce chemin.
Restent muettes à bon droit les options à deux erreurs (10 Q1 d proposé, 12 Q2 (b) 7, 12 Q3 (b) 14,
12 Q4 (c), 12 Q5 (c), 13 Q1 (a), 13 Q5 (b) 40, 14 Q1 (b)) et celles pour lesquelles aucune étiquette
n'est exacte.

### 3.3 Les 16 étiquettes proposées

Tranche = questions distinctes de la tranche actuelle. Publié = missions d'`origin/main` qui exécutent
la même erreur (grep des identifiants : 0 partout, aucun n'existe ; puis grep des explications).

| # | proposée | tranche | publié | libellé exact ? | existante qui couvre | verdict |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | effectif-cumule-pris-pour-effectif | 1 (14 Q5) | — | oui | `effectif-cumule-non-cumule` (élargie) | REJET → existante |
| 2 | mediane-lue-sans-ranger | 1 (10 Q5 c) | 3 (07/12-examen-2013 Q5 « 40 » ; 20/07-devoir Q3 b et Q4 « 15 », muettes) | oui | aucune (`mediane-au-milieu-des-extremes` est une autre erreur) | **ACCEPTÉE** : 4 questions ; phrase d'élève « تأخذ القيمة الوسطى قبل ترتيب السلسلة » ; libellé proposé fr « Tu prends la valeur du milieu sans avoir rangé la série : la médiane se lit sur la série rangée » ; compétence `math.stat.moyenne-mediane` ; rétro-étiqueter les 3 options publiées |
| 3 | rang-de-la-mediane-mal-calcule | 1 (10 Q3) | 1 (07/2013 Q2) | non : couvre trois erreurs distinctes (n/2, (n − 1)/2, n + 1) | — | REJET (et 10 Q3 écartée, M3) |
| 4 | facteur-de-l-inconnue-lu-comme-terme | 2 (10 Q1, Q4 : la paire M2) | 0 | oui | `operation-inverse-appliquee` (« جمعًا بدل الضرب ») | REJET → existante |
| 5 | multiplie-au-lieu-de-diviser-l-inconnue | 2 (idem) | 0 | oui | `operation-inverse-appliquee` | REJET → existante |
| 6 | droite-d-abscisse-constante-confondue | 1 (10 Q2) | 0 | oui | aucune | REJET (< 3), muette |
| 7 | distance-abscisses-additionnees | 3 (11 Q4, 12 Q6, 15 Q4) | 0 | non pour 15 Q4 (ce sont des ordonnées) | `operation-inverse-appliquee` (« جمعًا بدل الطرح », exact) | REJET → existante (et 12 Q6 (b) retirée, M5) |
| 8 | abscisse-comptee-depuis-la-mauvaise-origine | 1 (11 Q1) | 0 | oui | aucune | REJET (< 3), muette |
| 9 | sens-positif-de-l-axe-inverse | 1 (11 Q1) | 0 | oui | aucune (`inequation-demi-droite-sens-inverse` = autre notion) | REJET (< 3), muette |
| 10 | milieu-de-cote-pris-pour-le-centre | 1 (12 Q5) | 0 | oui | chemin alternatif : `coordonnees-point-inversees` | REJET (< 3) |
| 11 | cotes-opposes-pris-pour-diagonales | 1 (14 Q4) | même erreur sous `parallelogramme-sommets-mal-ordonnes` : 12/06 (1 option), 18/02-boss (3 options), dans des chapitres au programme | oui | `parallelogramme-sommets-mal-ordonnes`, libellé vectoriel | REJET du nouvel identifiant ; ÉLARGIR le libellé existant sans vecteur (ex. fr « Tu ordonnes mal les sommets du parallélogramme : dans ABCD les sommets se suivent dans l'ordre du tour, les diagonales sont [AC] et [BD] ») et le rattacher à une compétence au programme (sa compétence `math.vec.translation-vecteur` relève d'un chapitre hors programme), puis étiqueter 14 Q4 (d) |
| 12 | factorisation-difference-en-somme | 2 (14 Q3, Q6) | 0 | oui | `facteur-commun-signe-change` (exact) | REJET → existante |
| 13 | representant-de-classe-amplitude-ou-demi-borne | 1 (13 Q2) | 0 | non : deux erreurs dans un libellé | — | REJET, muettes |
| 14 | racine-fois-elle-meme-egale-racine | 2 (15 Q2, Q3) | 2 (03/18, 03/20, déjà étiquetées `racine-et-carre-confondus`) | oui | `racine-et-carre-confondus` (précédent publié) | REJET → existante |
| 15 | fraction-prise-pour-longueur | 2 (11 Q3, Q5) | 0 | oui | aucune | REJET (< 3 ; 3 dans la même mission si m2 est adopté : seuil atteint de justesse, à trancher) |
| 16 | exposant-supprime | 1 (12 Q3) | 0 | oui | aucune | REJET (< 3), muette |

## 4. Programme (R-3), ordre d'enseignement, vocabulaire

Ordre du manifeste : 15 → 01 → 19 → 02 → 16 → 17 → 03 → 04 → 07 → **12**. Cours lus sur `origin/main`.

| technique testée | questions | statut |
| --- | --- | --- |
| isoler x dans ax = b (diviser par le coefficient) | 10 Q1, Q4 | enseignée (04 : « نقسم الطرفين على معامل x ») |
| 5/√5 = √5 | 10 Q4 | enseignée (02 : (√a)² = a, 1/√2 = √2/2) |
| points de même abscisse ⟹ droite ∥ (OJ) | 10 Q2 | **MANQUANTE** (cours 12 vectoriel ; manuel p. 139–140) → M9, défaut du cours |
| rang du médian (n + 1)/2, ranger d'abord | 10 Q3, Q5 | enseignée (07) |
| droite graduée : abscisse, origine, unité, sens | 11 Q1 | enseignée (01 « وحدة التدريج », 19 « مستقيم مدرّج (OI) : O المبدأ ، OI وحدة الطول ») |
| milieu sur une droite graduée | 11 Q2 | enseignée (12 : formule du milieu ; manuel p. 133) |
| distance sur un axe \|b − a\| | 11 Q4, 12 Q6, 15 Q4 | enseignée (19, « AB = \|b − a\| ») |
| fraction d'une longueur (2/3 de AB) | 11 Q3, Q5, Q6 | acquise (math.frac.sens, cycles antérieurs) |
| critères de divisibilité 2, 3, 4, 5, 9 ; 6, 12, 15 par facteurs premiers entre eux | 12 Q1, Q3, Q4 ; 13 Q1, Q4 ; 14 Q6 ; 15 Q6 | enseignée (15, premier chapitre) |
| mise en facteur d'une puissance (aᵐ⁺ⁿ = aᵐ × aⁿ) | 12 Q2, Q3 ; 14 Q3, Q6 | enseignée (16 ; 03 « إخراج عامل مشترك ») |
| centre du parallélogramme = milieu commun des diagonales | 12 Q5 ; 14 Q4 | **donnée dans l'énoncé** (a) ; ne livre pas la clé (reste le repère et le calcul) |
| repère (C, A, D) défini par trois points | 12 Q5 | **MANQUANTE** → M4 : à donner dans l'énoncé |
| milieu dans un repère non orthonormé | 12 Q5 ; 14 Q1, Q4 | enseignée (12), mais le cours la restreint à tort au repère orthonormé (m11) ; les énoncés sont justes |
| symétrique par rapport à (OJ) : (−x ; y) | 13 Q3 | **donnée dans l'énoncé** (b), juste (repère orthogonal) ; elle ne désigne pas la clé (reste −(1 − √2) = √2 − 1) |
| centre de classe, moyenne pondérée | 13 Q2, Q5 | enseignée (07 « مركز الفئة ») |
| effectif cumulé croissant → effectif | 14 Q2, Q5 | enseignée (07 « التكرار المجمّع ») |
| valeur absolue d'un nombre négatif, comparer 3√3 et 1 | 15 Q1, Q3 | enseignée (19, 17) |
| distributivité avec radicaux | 15 Q2 | enseignée (02, 03) |
| a² − b² = (a − b)(a + b) | 15 Q5 | enseignée (03) |

Aucune notion hors programme : ni vecteur, ni translation, ni « شعاع » ni « انسحاب » dans les six
fichiers. Vocabulaire : « وسيط (موسّط) », « مركز الفئة », « التكرار المجمّع الصاعد (التراكميّة
الصاعدة) », « فاصلة », « ترتيبة » et « الأصل » sont conformes aux cours 07, 12 et 19. Seul le mot
officiel « معيّن » (repère) manque aux cours (m11).

## 5. Doublons

**(a) Avec le chapitre 12 publié (01 à 09).** Pas de question quasi identique. Il y a des exercices
parallèles (même savoir-faire, autres données) :
- 12 Q2/Q3 et 07-devoir Q1/Q2 (7¹³ + 7¹² = 7¹² × k ; divisibilité) : formats et pièges différents ;
- 12 Q1/Q4 et 09-devoir Q1/Q2 (51a4 par 3 puis par 12) ;
- 14 Q4 : sixième « quatrième sommet » du chapitre (02, 03, 04, 05, 06), par le milieu des diagonales
  au lieu des vecteurs ; item officiel ;
- 14 Q1 : septième « milieu » simple du chapitre (saturation, étape d'auteur).

`content:tranche` ne trouve aucune paire proche impliquant 10 à 15.

**(b) Entre les six missions.** Pas de mission qui ne diffère d'une autre que par ses nombres. Les
gabarits recyclés par les sujets eux-mêmes restent des exercices parallèles :
- divisibilité (12 Q3 / 14 Q6 / 15 Q6 : trois clés « 15 », m8) ;
- parallélogramme (12 Q5 ≠ 14 Q4 : tâches différentes) ;
- valeur absolue et distance (12 Q6 / 15 Q1 / 15 Q4 : données et pièges différents).

Dans une même mission, la paire 10 Q1 / 10 Q4 est quasi identique (M2).

**(c) Avec les missions d'examen publiées des chapitres 07, 03, 04, 09 et 17** (08 n'en a aucune sur
`origin/main`) :
- 10 Q3 ≈ 07/12-examen-2013 Q2 : quasi identique → M3, écarter ;
- 13 Q5 ≈ 07/11-examen-2012 Q2 : mêmes données, même calcul → M8, écarter ;
- 13 Q4 ≈ 03/15-examen-2020 Q4 : exercice parallèle (autres données), à garder et justifier → m4.

Les autres rapprochements sont des parallèles acceptables :
- 13 Q1 et 03/15 Q3 (somme des chiffres, un contre deux chiffres-lettres, pièges différents) ;
- 15 Q1 et 17/10-examen-2002 Q2 (\|2√2 − 3\|) ;
- 15 Q3 et 03/24 Q2 ;
- 10 Q5 et 07/12-examen-2013 Q5 (médiane de 9 pointures) ;
- 12 Q4 et 07/12-examen-2013 Q4 (couples de chiffres pour 15) ;
- 15 Q2 et 09/16 Q2, 03/26 Q1, 17/09 Q1 (distribuer un radical).

## 6. Fuites et autonomie

- **Route quête** (`displayOrder`, tri stable par difficulté, ordre du fichier conservé puisque les
  rampes sont croissantes) : aucune fuite en avant. J'ai relu chaque explication en cherchant la clé
  des questions suivantes : aucune ne la donne. En particulier, 12 Q2, 14 Q3 et 15 Q5 posent la
  factorisation sans conclure à « 15 » ; 13 Q1 ne conclut pas à 6 ; 11 Q5 ne calcule pas xM ; 10 Q1
  ne simplifie pas 5/√5.
- **Donjon (tirage au hasard)** : les liens étape → question complète sont inhérents à la
  décomposition des sujets. Les explications de 10 Q4, 10 Q5, 11 Q2/Q4/Q5/Q6, 12 Q3, 12 Q4, 13 Q4,
  13 Q5, 14 Q4, 14 Q5, 14 Q6, 15 Q3 et 15 Q6 redonnent la clé d'une étape antérieure de leur mission.
  C'est acceptable (même pratique que les missions publiées), sauf quand l'étape est quasi la même
  question : c'est 10 Q1/Q4 (M2). Tous les énoncés se lisent seuls, sans « السؤال السابق » ni valeur
  définie ailleurs.
- Aucune décimale de vérification ne livre un verdict. Aucun titre ne livre une clé : les sous-titres
  nomment des notions.

## 7. Étage, rampe, titres

- **Les six missions : `difficulty` 2, `practice`, 75 XP / 15 pièces** (barème canonique),
  `displayOrder` 10 à 15 égal au préfixe du fichier. Titres au format exact « 🏛️ مناظرة <année> ·
  التمرين N ⭐⭐: … », sujet sans résultat. **d2 est juste pour les six** : exercices 1 de QCM
  (3 à 4 points) et 2001 ex. 3 (droite graduée, calculs courts). Aucun n'est d1 (réponses en plusieurs
  étapes, pièges d'examen), aucun n'atteint d3 (pas de chaîne longue ni de démonstration).
- **Rampes internes non décroissantes** :
  - 10 : 1, 1, 1, 2, 2 ;
  - 11 : 1, 1, 1, 1, 2, 2 ;
  - 12 : 1, 2, 2, 2, 2, 2 ;
  - 13 : 1, 1, 2, 2, 2 ;
  - 14 : 1, 1, 2, 2, 2, 2 ;
  - 15 : 1, 1, 2, 2, 2, 2.
- **Difficultés honnêtes** : les d1 sont des lectures ou des étapes uniques ; les d2 combinent deux
  notions ou deux étapes. Après correctifs : 10 → 1, 1, 2, 2 et 13 → 1, 1, 2, 2, toujours croissantes.

## 8. Remplacements d'options et adaptations annoncés par l'auteur

| remplacement | verdict |
| --- | --- |
| 12 Q5 (1/2 ; 1/2) → (1 ; 1) | VALIDÉ : faux, empêche le vote (1/2 majoritaire), deux erreurs donc muette |
| 12 Q6 2√2 → −2 − √2 | faux en valeur mais s'élimine à vue → M5 (remplacer par √2) |
| 10 Q4 « x = 5 » → « x = 5√5 » | VALIDÉ : « 5 » = (5 − √5) + √5 était somme de deux options. Note : « x = 5 » avait une étiquette exacte (`coefficient-non-divise`) |
| 13 Q5 50 → 43 | VALIDÉ (évite des distracteurs tous multiples de 5 ; 43 = bornes supérieures, étiquette exacte) ; sans objet si Q5 est écartée (M8) |
| 14 Q6 10 → 29 | VALIDÉ (évite des distracteurs tous pairs contre une clé impaire ; cohérent avec 14 Q3 (a)) |
| 12 Q2 2 → 7 | VALIDÉ (complète le plan 2×2 ; 7 = 1 + 6, deux erreurs, muette) |
| 2001 ex. 3 item 2 (recopier la figure) non posé | VALIDÉ (ce n'est pas une question) |
| item 4a (construire M) → question fermée de méthode (11 Q3) | VALIDÉ (juste, options homogènes, pas de vote, clé non la plus longue) |
| 2015 ex. 1 : question « règle générale » supprimée | VALIDÉ (la règle est donnée dans 13 Q3) |

Les 4ᵉ options ajoutées par l'auteur sont toutes fausses en valeur. Les réserves portent sur trois
d'entre elles : 10 Q2 (OA) (m9), 10 Q3 « 8 » (M3) et 15 Q1 « −1 − 3√3 » (M6). Pas d'intrus multiple
d'un même nombre : distracteurs 12/14/21 (12 Q3), 15/12/4 (13 Q4), 6/12/29 (14 Q6) et 9/10/12
(15 Q6), de PGCD 1 à chaque fois. Pas d'option somme ou différence de deux autres, pas de vote
reconstruisant une clé (vérifié sur 12 Q4, 12 Q5, 14 Q1, 14 Q4, 13 Q1, 13 Q2 et 15 Q1).

Vérification par script sur les 34 questions : aucune option n'est somme ou différence de deux
autres, et c'est vrai aussi des trois options proposées en M5, M6 et m2. Le vote par composante ne
reconstruit aucune clé : 12 Q4 donne une majorité b = 3 ≠ 0 ; 12 Q5 donne (1 ; 0) = distracteur ;
14 Q4 donne x = −2 ≠ −1. Sur 14 Q1, le 0 de la clé est inhérent (0/2 = 0) : le vote réduit à 50/50
sans reconstruire la clé.

## 9. Rendu arabe, figure, notation, gates

- **Rendu (moteur `origin/main` `ec8c637` : `bidi.ts` avec #1137 à #1141, `isMathExpression`,
  `isRtlText`)**. Premier passage avant #1141, refait après sa fusion. J'ai reproduit dans Chromium
  le chemin du lecteur pour 210 champs (6 titres, 34 énoncés, 34 explications, 136 options) :
  - page `dir="rtl"` ;
  - `RichField` ligne par ligne, avec `.math-equation` pour une ligne de pure notation et `.math-run`
    isolé pour les runs de `splitMathRuns` ;
  - option en `ltr` si `isMathExpression`.

  J'ai ensuite mesuré la position de chaque caractère. Aucun run isolé ni nombre n'est inversé
  intérieurement, et aucune formule n'est affichée dans un ordre mêlé (moitié LTR, moitié RTL). Les
  seuls signalements sont bénins : « ✓ » placé à gauche d'une formule latine (ponctuation RTL) et la
  paire « ⭐⭐ ». Cas vérifiés en particulier :
  - listes à virgule arabe « 0 ، 1 ، −2 ، 3 » et « 10 ، 30 ، 50 ، 70 ، 90 » (lecture RTL dans l'ordre
    source, « −2 » isolé) ;
  - listes d'intervalles « [0 ; 20[ ، [20 ; 40[ … » (chaque intervalle isolé) ;
  - coordonnées « (8 ; 4) », « (0 ; 1/2) » (options LTR) ;
  - valeurs absolues « |1 − 3√3| », « |−2| + |√2| » ;
  - « 11 111 111² − 16 » (U+00A0) et « 60 876 = 12 × 5 073 ».

  Deuxième contrôle, propre aux parenthèses : chaque couple doit encadrer son contenu à l'écran
  (RTL en prose, LTR dans un isolat). Sur tous les couples de la tranche, 3 sont mal placés : 12 Q6 et 15 Q4 (M10, cas
  préexistant) et 13 Q2 (M11, régression de #1141). #1141 modifie 11 lignes de la tranche : 10
  améliorations (« ) » de fin de membre arabe sorti de l'isolat, par ex. « (لأنّ √27 > √1) » en
  15 Q1) et 1 régression (13 Q2).

  Tous les textes de remplacement proposés ici (26 champs) ont été passés aux trois contrôles sur ce
  moteur : 0 défaut.
- **Piège de passe** : les onze « الشكل التالي » sont tous en mission 11, qui porte la figure. Aucun
  « على الشكل التالي » ne renvoie à une figure absente ; « المعادلة التالية », « المجموع التالي » et
  les autres « التالي » sont suivis de la formule en ligne propre. Un point d'attention : 14 Q2 dit
  « العمود المجاور » sans tableau (corrigé en M7).
- **Figure de 11** (identique dans les six questions) :
  - vraie : 12 traits en x = 36 + 24k, A au 3ᵉ, O au 5ᵉ, I au 6ᵉ et B au 8ᵉ, flèche vers la droite,
    d'où A = −2, O = 0, I = 1, B = 3, conforme à la transcription ;
  - ne donne aucune clé : aucun nombre ; A et B en vert, ce qui marque les points de la question et
    rien d'autre ;
  - arabe seulement dans `<title>` ; éléments `path`, `g`, `circle`, `text`, `title` ; aucun
    `width`/`height`/`href`/`style`/`use`/`image` ; `viewBox` 0 0 340 76 ;
  - rien ne déborde : x de 13 à 326, y d'environ 31 à 66 avec le halo des libellés ;
  - aucune question d'une autre mission n'exige de figure dont l'absence serait fautive (10 Q2,
    13 Q3, 14 Q4 : une figure livrerait la clé ; 12 Q5 : la figure montrerait I sur (CA)).
- **Notation** : aucun chiffre arabo-indien, trait d'union-moins, groupe de chiffres à espace simple
  (U+00A0 partout : 2 en 12, 12 en 13, 54 en 15), LaTeX, `$`, virgule arabe dans un groupe entre
  crochets, radicande arabe ou signe espacé.
- **Gates** (moteur, arbre de travail, en lecture seule) : `build.ts`, `qa.ts`, `qa-checks.ts`,
  `qa-inline-equation.ts` et `tranche.ts` sont identiques à `origin/main`. Seuls diffèrent
  `scripts/content/gisement/*` et `src/shared/lib/bidi.ts`, qu'aucune de ces commandes n'importe :
  - `build.ts --check --subject math` : ✓ (20 chapitres, 274 exercices, 1 881 questions) ;
  - `qa.ts --subject math` : 0 erreur, aucun avertissement sur le chapitre 12 ;
  - `tranche.ts --chapters 12` : clé strictement la plus longue 0/34 dans la tranche (17 à égalité),
    aucune paire proche impliquant 10 à 15.

## 10. Chiffre final

- **Questions auditées : 34** (6 missions), plus la ligne `sources[]` du `chapter.json`.
- **Clés fausses : 0** (34/34 concordent avec la résolution à l'aveugle). Critiques : 0.
- **Questions à reprendre (majeurs) : 9** :
  - 10 Q1 (réécrire, M2) ;
  - 10 Q3 (écarter, M3) ;
  - 11 Q1 (réécrire, M1) ;
  - 12 Q5 (compléter l'énoncé, M4) ;
  - 12 Q6 (option b et explication, M5 + M10) ;
  - 13 Q5 (écarter, M8, verdict du doublon assumé) ;
  - 14 Q2 (reformuler, M7) ;
  - 15 Q1 (option a, M6) ;
  - 15 Q4 (explication, rendu, M10).
- **Plus 13 Q2** : explication brouillée par une régression du moteur (arena#1141, M11). Le moteur est
  à corriger : 35 lignes cassées dans le corpus. Un contournement de contenu est fourni.
- **Plus 1 majeur hors tranche** : 10 Q2 dépend d'une notion absente du cours 12 (M9, à régler dans le
  cours).
- **Mineurs : 11** (m1 à m11). Retouches de texte : 12 Q1, 11 Q6, 10 Q5, 14 Q5, `chapter.json`.
  Étiquettes existantes à poser sur 10 options (m3). Pour 13 Q4 : exercice parallèle à justifier et
  étiquette de l'option « 12 » à harmoniser. Le reste sont des notes.
- **Étiquettes proposées : 1 acceptée** (`mediane-lue-sans-ranger`, 4 questions dont 3 publiées).
  **15 rejetées** :
  - 6 couvertes par une étiquette existante (#1, #4, #5, #7, #12, #14) ;
  - 1 à traiter en élargissant `parallelogramme-sommets-mal-ordonnes` (#11, libellé sans vecteur) ;
  - 8 sous le seuil ou au libellé inexact (#3, #6, #8, #9, #10, #13, #15, #16).
- Après correctifs, la mission 10 passe à 4 questions, la mission 13 à 4, les autres restent à 6.
  Étage d2 practice 75/15 validé pour les six ; rampes non décroissantes.

Statut : TERMINÉ.
