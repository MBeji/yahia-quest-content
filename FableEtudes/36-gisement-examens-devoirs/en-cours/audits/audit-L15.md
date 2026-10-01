# Audit indépendant — tranche L15 · maths 9ᵉ · ch. 18 `18-quadrilateres` · missions 22 à 28 (examens nationaux)

Auditeur indépendant (étude 36, G6). Arbre de travail de `yahia-quest-content` tel quel ; registres et
missions publiées lus sur `origin/main` (f84ccdaf) ; moteur `yahia-quest-arena` `origin/main` (96bada8f)
pour `bidi.ts`. Aucun fichier du dépôt modifié.

Méthode : vue aveugle (énoncés + options, sans clé ni explication) → résolution de chaque question
→ recalcul par script (Fraction / sympy) → comparaison aux clés ; explications, étiquettes (libellés
`origin/main`), figures (rendu Chromium + vérification numérique des coordonnées), rendu arabe
(`splitMathRuns`/`isDisplayEquation` + Chromium `dir=rtl`, ordre visuel extrait caractère par
caractère), doublons (option-sets et données contre les 1 978 questions publiées de `content/math`),
fuites (ordre d'émission recalculé), programme (cours `origin/main` des chapitres 12, 08, 09, 18).

**Résultat d'ensemble : 50/50 clés justes (aucune divergence avec la résolution aveugle).** Aucune
erreur critique. Les défauts sont de forme (clé reconstructible par vote), de doublon, de figure,
d'étage et de rendu.

---

## 1. Tableaux par fichier

### 22 — مناظرة 2008 · ex. 3 (d2 practice 75/15, displayOrder 22) — titre au format ✓

| Q | d | ma réponse | clé | verdict | motif |
|---|---|---|---|---|---|
| 1 | 1 | d (Q = (−1 ; −3)) | d | OK | plan 2×2 propre : M échange, P signe, N les deux (muette) ; figure exacte |
| 2 | 1 | a | a | réserve (M2, M5) | clé = (b) « ⊥ » ∪ (c) « milieu sur (OJ) » ; (c) et l'explication donnent (0 ; 3) = clé de Q4, émise après |
| 3 | 1 | c | c | réserve (M1) | « وهي كلّها صحيحة » contredit par (a) et (d) (inférences fausses) ; doublon de fait de 23 Q4 |
| 4 | 1 | b (0 ; 3) | b | OK | 2×2 propre ; quasi-jumeau de la publiée 08/16-examen-2003 Q3 (même clé (0 ; 3)) — note |
| 5 | 2 | a | a | OK | réserve légère : seule la clé dit « في الجهة الأخرى » (les trois autres « في جهة H ») |
| 6 | 2 | d (0 ; −3) | d | OK | |
| 7 | 2 | b | b | réserve (M2) | vote terme à terme : « [AC] و [HK] » (a, b) × « المنتصف نفسه » (b, c) → b |

### 23 — مناظرة 2005 · ex. 3 (d3 boss 120/30, displayOrder 23) — titre ✓

| Q | d | ma réponse | clé | verdict | motif |
|---|---|---|---|---|---|
| 1 multi | 1 | {b, d, e, f} | {b, d, e, f} | réserve mineure (m2) | paires contradictoires (a)/(d) et (c)/(e) : une juste par paire se déduit |
| 2 | 1 | a | a | réserve (M2) | vote : « العمودي على (OI) » (a, d) × « نمدّه إلى الجهة الأخرى » (a, b, c) → a |
| 3 | 1 | d (2 ; −3) | d | réserve (M4) | la figure trace le pointillé de A à (2 ; 0) : seule (2 ; −3) a l'abscisse 2 |
| 4 multi | 2 | {b, d} | {b, d} | réserve (M2) | union : (d) = (c) « OB = OC » ∪ (e) « alignées » → seule union, donc suffisante |
| 5 | 2 | c | c | réserve (M2, M4) | vote « نظيرة C » (b, c) × « منتصف » (a, c, d) → c ; la figure trace la diagonale [AO] en pointillé |
| 6 | 3 | b (0 ; 6) | b | OK | d3 honnête (diagonales selon l'ordre ACOD + milieu + symétrique) |

### 24 — مناظرة 2006 · ex. 3 (d3 boss 120/30, displayOrder 24) — titre ✓ (cache « معيّن »)

| Q | d | ma réponse | clé | verdict | motif |
|---|---|---|---|---|---|
| 1 | 1 | a | a | réserve (M10) | explication : « أمّا الوصف الأخير » = renvoi ordinal à une option mélangée |
| 2 | 1 | b | b | réserve (M3) | vote (2 ; 3)×2 & (OJ)×3 → b ; (c) nie la prémisse (énoncé : (OJ)) ; figure montre A, B en miroir ; explication livre la clé de Q3 |
| 3 | 1 | c (2 ; −3) | c | OK | même clé que 23 Q3, 3 options sur 4 communes (données recyclées) — note |
| 4 | 2 | d (2 ; 0) | d | OK | |
| 5 | 2 | c (4 ; 0) | c | OK | |
| 6 | 2 | a | a | OK | (d) s'élimine sur la figure (OBC isocèle visible) — faible, sans fuite |
| 7 | 3 | b | b | réserve (M8) | rappel direct du critère du losange (cours ch. 18 §3) = d2 ; la mission n'a plus aucun d3 réel |

### 25 — مناظرة 2016 (تقني) · ex. 3 (d3 boss, displayOrder 25) — titre ✓

| Q | d | ma réponse | clé | verdict | motif |
|---|---|---|---|---|---|
| 1 | 1 | c | c | réserve (M2) | vote : « ADF » (c, d) × « لأنّ ABCD مستطيل » (a, c) → c |
| 2 | 2 | b (5) | b | OK | muettes (a) et (c) méritent une étiquette existante (§3) |
| 3 | 2 | d (2,4) | d | OK | (a) mérite `reponse-a-l-autre-inconnue` (§3) |
| 4 | 2 | a | a | réserve (M2) | vote : « ∥ » (a, c) × « طاليس مباشرة » (a, b) → a |
| 5 | 2 | c (2/3) | c | OK | étiquette de (d) à corriger (m1) |
| 6 num | 2 | 3,6 cm | 3.6 cm | OK | unité fixée ; 3,6/3.6 acceptés |
| 7 | 2 | d (6) | d | OK | « و AF = 5 cm » inutile à la clé, livre 25 Q2 au donjon (m4) |
| 8 | 3 | b (600) | b | réserve (M9) | rendu « 1 m² = 10 000 cm² » à moitié inversé |
| 9 num | 3 | 17 | 17 | réserve (M9) | chaîne « 6 000 000 cm² = 6 000 000 ÷ 10 000 = 600 m² » : égalité mal écrite + coupée au rendu |

### 26 — مناظرة 2017 (تقني) · ex. 3 (d3 boss, displayOrder 26) — titre ✓

| Q | d | ma réponse | clé | verdict | motif |
|---|---|---|---|---|---|
| 1 | 1 | c | c | réserve (M2) | vote : « ABC قائم في A » (a, c) × « فيثاغورس المباشرة » (c, d) → c |
| 2 num | 1 | 5 cm | 5 cm | réserve (M7) | doublon de 28 Q1 (même SVG au pixel près, mêmes AB = 4, AC = 3) ; l'explication contient 25 = clé de 28 Q1 |
| 3 | 2 | d | d | réserve (M2) | vote/union : « ∥ » (b, d) × « A من [BE] » (a, d) × « طاليس مباشرة » (a, d) → d |
| 4 num | 2 | 12,5 cm | 12.5 cm | OK | |
| 5 | 2 | b (7,5) | b | OK | (c) 4,5 mérite `position-relative-ignoree` (§3) |
| 6 | 2 | a (31,5) | a | réserve (M9) | explication : « (مجموع القاعدتين) × الارتفاع/2 = … » — « /2 » rejeté à l'autre bout de la ligne |
| 7 | 3 | c (0,315) | c | réserve (M9) | rendu « 1 m² = 10 000 cm² » |

### 27 — مناظرة 2018 (تقني) · ex. 3 (d3 boss, displayOrder 27) — titre ✓

| Q | d | ma réponse | clé | verdict | motif |
|---|---|---|---|---|---|
| 1 num | 1 | 10 cm | 10 cm | OK | |
| 2 | 2 | a | a | OK | conséquence commune aux 4 options : pas de vote possible |
| 3 | 2 | c (4,5) | c | OK | (a) 3,6 mérite `segment-mal-choisi` (§3) |
| 4 num | 2 | 7,5 cm | 7.5 cm | OK | |
| 5 num | 2 | 13,5 cm² | 13.5 | réserve (M6) | même nombre que la clé de Q7 (1/100) ; son explication livre Q7 en avant |
| 6 | 3 | d (10,5) | d | réserve (M6) | même nombre que la clé de Q8 ; son explication livre Q8 en avant |
| 7 | 3 | b (13,5 m²) | b | réserve (M6) | compensation 1/100 : refaire Q5 suffit ; d2 réel ; étiquette de (d) ambiguë (m1) |
| 8 num | 3 | 10,5 m² | 10.5 m² | réserve (M6, M9) | 24 et 13,5 donnés : une soustraction (d1) étiquetée d3 ; rendu « 1 m² = … » |

### 28 — مناظرة 2023 (تقني) · ex. 3 (d3 boss, displayOrder 28) — titre ✓

| Q | d | ma réponse | clé | verdict | motif |
|---|---|---|---|---|---|
| 1 num | 1 | 25 | 25 | OK | doublon avec 26 Q2 réglé côté 26 (M7) |
| 2 | 2 | a | a | réserve (M2) | vote : « ∥ » (a, d) × « طاليس مباشرة » (a, b, c) → a ; étiquette de (c) inexacte |
| 3 | 2 | d (10) | d | OK | figure à l'échelle : DE ≈ 2 BC se lit à l'œil (note m14) |
| 4 | 2 | b | b | OK | 2×2 propre ; d1 réel (m5) |
| 5 | 3 | c (54) | c | OK | aire par les 4 triangles rectangles (enseigné) |
| 6 | 3 | b (0,54) | b | réserve (M9) | rendu « 1 m² = 10 000 cm² » ; « S = 5 400 ÷ 10 000 » (m) |

---

## 2. Défauts classés et correctifs exacts

### Critiques — aucun

0 clé fausse, 0 double réponse défendable, 0 figure fausse (toutes vérifiées numériquement :
alignements, parallèles, angles droits et proportions exacts ; 22–24 aux nœuds entiers de la grille).

### Majeurs

**M1 — 22 Q3 : prémisse contredite + doublon de 23 Q4.** L'énoncé affirme « وهي كلّها صحيحة », or
(a) « … وهذا يميّز النقطتين المتناظرتين » et (d) « … وهذا يُعيّن موضع النقطة O » sont fausses : un
lecteur qui croit l'énoncé peut défendre (a). Et 22 Q3 répète 23 Q4 (mêmes trois pièges : une seule
coordonnée opposée, OB = OC, alignement ; même clé « O milieu » ; explications quasi mot pour mot).
→ **Supprimer 22 Q3** (22 passe à 6 questions, rampe 1,1,1,2,2,2). À défaut seulement (le doublon
resterait) : énoncé « في معلّم متعامد ومتجانس (O, I, J)، النقطتان A(1 ; 3) و C(−1 ; −3).\nأيّ الحجج التالية تُثبت أنّ A و C متناظرتان بالنسبة إلى النقطة O ؟ ».

**M2 — Clé reconstructible par vote terme à terme ou par union (10 questions).** Le standard publié
pour ces « pourquoi » est le plan 2×2 (08/14-2011T Q1, 08/19-2013T Q2 : {condition juste/fausse} ×
{théorème direct/réciproque}). Remplacements vérifiés par script (vérité sous les données, clé jamais
strictement la plus longue, vote neutralisé) :

| Q | option remplacée | nouveau texte | étiquette | phrase d'explication à remplacer → nouvelle |
|---|---|---|---|---|
| 22 Q2 | (c) | `A و B على البعد نفسه من المستقيم (OJ)، و OA = OB` (vraie, insuffisante : (1 ; −3) vérifie les deux avec A) | muette | « ومنتصف [AB] هو ((1 + (−1))/2 ; (3 + 3)/2) = (0 ; 3) وفاصلته 0، فهو نقطة من (OJ) ✓ » → « ومنتصف [AB] فاصلته (1 + (−1))/2 = 0، فهو نقطة من (OJ) ✓ » ; « أو الاكتفاء بمرور (OJ) من المنتصف وحده، فقد يكون مائلًا على (AB) » → « أو الاكتفاء بتساوي بُعدَي A و B عن (OJ) مع OA = OB، فالنقطة (1 ; −3) تحقّق الشرطين مع A وهي مناظرتها بالنسبة إلى (OI) لا إلى (OJ) » |
| 22 Q7 | (a) | `قطرا الرباعي [AK] و [HC] متقايسان، فهو متوازي أضلاع` | muette (2 erreurs) | « أو نسبة تقايس القطرين إلى متوازي الأضلاع وهي خاصيّة المستطيل، وهنا AC² = 40 و HK² = 36 » → « أو الجمع بين الخطأين: [AK] و [HC] ضلعان متقابلان لا قطران، وتقايسهما (AK = HC = √37) لا يُثبت وحده أنّ الرباعي متوازي أضلاع » |
| 23 Q2 | (c) | `نرسم من A العمودي على (OJ) ونعيّن C عند تقاطعه مع المستقيم (OJ)` | muette | supprimer « أو استعمال التناظر المركزي الذي مركزه O فنصل إلى نقطة أخرى؛ » et remplacer la fin « لا صورتها. » par « لا صورتها؛ أو الجمع بين الخطأين فنتوقّف عند المسقط العمودي لـ A على (OJ). » |
| 23 Q4 (multi) | ajouter (f) | `ترتيبتا النقطتين B و C متقابلتان و OB = OC` (vraie, insuffisante) ; clé inchangée {b, d} | — | ajouter avant la dernière phrase : « واجتماع تقابل الترتيبتين مع OB = OC لا يكفي أيضًا: النقطة (−2 ; −3) تحقّقهما مع B، وهي مناظرتها بالنسبة إلى (OI) لا إلى O. » |
| 23 Q5 | (b) | `D نظيرة A بالنسبة إلى النقطة O` | muette | « أمّا نظيرة C بالنسبة إلى O فلا علاقة لها بمنتصف القطرين » → « أمّا نظيرة A بالنسبة إلى O فتجعل O منتصف [AD]، و O رأس من رؤوس الرباعي لا مركزه » |
| 25 Q1 | (d) | `المثلّث ADF قائم في A لأنّ ABCD مستطيل، و [DF] وتره، فنطبّق نظرية فيثاغورس` | garder `hypotenuse-mal-choisie` | « وضع الزاوية القائمة في A لأنّ A رأس من رؤوس المستطيل » → « وضع الزاوية القائمة في A بحجّة أنّ ABCD مستطيل » |
| 25 Q4 | (d) | `D و H و K على استقامة واحدة وكذلك D و F و C، فنطبّق عكس مبرهنة طاليس في المثلّث DKC` | muette (2 erreurs) | « أو استعمال فيثاغورس وهو يربط مربّعات الأطوال لا نسبها » → « أو الجمع بين الخطأين: الاكتفاء بالاستقامة مع استعمال العكس » |
| 26 Q1 | (b) | `BDE قائم في E، فنطبّق عكس نظرية فيثاغورس لإثبات هذه المساواة` | muette (2 erreurs) | « أو استعمال طاليس وهو يربط النسب لا المربّعات؛ » → « أو الجمع بين الخطأين: العكس في المثلّث BDE؛ » |
| 26 Q3 | (c) | `A من [BE] و C من [BD] في المثلّث BDE، فنطبّق عكس مبرهنة طاليس` | muette (2 erreurs) | « أو استعمال فيثاغورس الذي يربط مربّعات الأطوال لا نسبها » → « أو الجمع بين الخطأين: وقوع النقاط على الضلعين مع استعمال العكس » |
| 28 Q2 | (c) | `(BD) و (CE) يتقاطعان في A، فنطبّق عكس مبرهنة طاليس في وضعية الفراشة` | muette (supprime l'étiquette inexacte, m1) | « أو الاستناد إلى التعامد (BD) ⟂ (CE) وهو معطى صحيح لكنّه لا يعطي النسب، وإنّما نستعمله لفيثاغورس وللمساحة؛ » → « أو الجمع بين الخطأين: التقاطع وحده مع استعمال العكس؛ » |

Longueurs après correctif (clé jamais strictement la plus longue) : 22 Q2 [65, 68, 48, 62] ;
22 Q7 [51, 57, 57, 58] ; 23 Q2 [70, 70, 63, 63] ; 23 Q5 [39, 30, 39, 39] ; 25 Q1 [74, 69, 74, 74] ;
25 Q4 [70, 87, 73, 83] ; 26 Q1 [60, 60, 57, 57] ; 26 Q3 [77, 73, 61, 73] ; 28 Q2 [77, 79, 67, 81].

Vérification des correctifs (script + Chromium) : chaque option et chaque phrase de remplacement de
ce rapport (26 textes) a été recalculée (Fraction/sympy : (1 ; −3) vérifie les deux conditions de
22 Q2 (c) et vaut S(OI)(A) ; AK = HC = √37 ; (−2 ; −3) vérifie les deux conditions de 23 Q4 (f) et vaut
S(OI)(B) ; AB = 4 ≠ 2 ; D = S_O(A) ne rend pas ACOD parallélogramme ; 27 Q8 : 24, 13,5, 10,5,
105 000 cm² = 10,5 m², 1 050 cm² = 0,105 m², 37,5), segmentée par `splitMathRuns` et rendue en
`dir=rtl` : 0 nombre inversé, 0 signe détaché, ordre visuel conforme à la source.

**M3 — 24 Q2 : format « coordonnées + conclusion » irréparable.** Vote ((2 ; 3) ×2, (OJ) ×3 → b) ;
(c) conclut sur (OI) alors que l'énoncé pose (OJ) (s'élimine sans calcul) ; la figure dessine A et B
en miroir (la conclusion se lit) ; l'explication (« تغيير الإشارتين معًا، وهذا تناظر مركزي بالنسبة إلى O »
+ option (d) (2 ; −3)) livre en avant la clé de Q3, émise après. La sous-question « A, B symétriques
par rapport à (OJ) » est déjà couverte par 22 Q2 et 23 Q1. → **Supprimer 24 Q2.** Repli si l'auteur
la garde : énoncé « في معلّم متعامد ومتجانس (O, I, J)، النقطة A(−2 ; 3).\nما إحداثيّتا مناظرة A بالنسبة إلى المستقيم (OJ) ؟ »
+ figure de 24 Q3 (A seule) ; options `(−2 ; −3)` · `(2 ; 3)` (clé) · `(3 ; 2)` (`coordonnees-point-inversees`)
· `(2 ; −3)` ; explication « المناظرة بالنسبة إلى المستقيم (OJ)، أي محور الترتيبات، تُبقي الترتيبة وتغيّر إشارة الفاصلة: مناظرة A(−2 ; 3) هي (2 ; 3) ✓، ولذلك فالنقطة B(2 ; 3) هي مناظرة A بالنسبة إلى (OJ). الخطأ الشائع: تغيير إشارة الترتيبة بدل الفاصلة فنجد (−2 ; −3)؛ أو تغيير الإشارتين معًا فنجد (2 ; −3)، والمناظرة بالنسبة إلى محور لا تغيّر إلّا إشارة واحدة؛ أو كتابة الزوج بترتيب معكوس فنجد (3 ; 2). »
(vote : abscisse 2 ×2, ordonnée −3 ×2 → (2 ; −3), un distracteur).

**M4 — Figures qui désignent la clé.** 23 Q3 : supprimer `<path d="M172 52 L172 142" fill="none" stroke="#0f6e56" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/>`
(le pointillé fixe x = 2 et élimine les trois distracteurs). 23 Q5 : supprimer
`<path d="M172 52 L112 142" fill="none" stroke="#64748b" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/>`
(la diagonale [AO] en pointillé désigne la clé « منتصف القطعة [AO] » ; la figure de Q6 n'en a pas).

**M5 — Fuite en avant 22 Q2 → 22 Q4.** L'option (c), déclarée vraie, et l'explication donnent le
milieu (0 ; 3) de [AB] sur (OJ), c'est-à-dire H, clé de Q4 émise après (d1 = d1, ordre fichier).
Réglé par le remplacement de (c) et la phrase d'explication de M2 (abscisse seule).

**M6 — 27 : compensation 1/100 non acceptable en l'état.** La compensation elle-même est inhérente
au sujet et le raccourci « 1 cm ↔ 1 m donc 1 cm² ↔ 1 m² » est un raisonnement juste ; mais Q5 (13,5 cm²)
et Q7 (13,5 m²), Q6 (10,5 cm²) et Q8 (10,5 m²) clés le même nombre deux fois, l'étape d'échelle y est
invisible, les explications de Q5/Q6 livrent Q7/Q8 en avant, et Q8 (24 et 13,5 donnés) est une
soustraction étiquetée d3. → **Supprimer Q5 et Q6 ; Q7 en d2 ; réécrire Q8 en QCM depuis les longueurs** :
- énoncé : « على تصميم قطعة خشبيّة، ABC مثلّث قائم الزاوية في A حيث AB = 6 cm و AC = 8 cm، والنقطة D من [AB] والنقطة E من [AC] حيث AD = 4,5 cm و AE = 6 cm. القطعة ECBD هي ما يبقى من المثلّث ABC بعد نزع المثلّث ADE. السلّم هو 1/100، أي أنّ كلّ 1 cm على التصميم يمثّل 100 cm في الواقع.\nما مساحة القطعة ECBD الحقيقيّة بالمتر المربّع ؟ » + la figure actuelle de Q6 ;
- options `0,105` (étiquette nouvelle T1) · `10,5` (clé) · `24` (`math.alg.reponse-a-l-autre-inconnue`) · `37,5` (muette), d3 ;
- explication : « المثلّثان ABC و ADE قائمان في A: مساحة ABC = (6 × 8)/2 = 24 cm² ومساحة ADE = (4,5 × 6)/2 = 13,5 cm²، فمساحة ECBD على التصميم = 24 − 13,5 = 10,5 cm². وكلّ طول يُضرب في 100 فتُضرب المساحة في 100 × 100 = 10 000، أي 10,5 × 10 000 = 105 000 cm²، وهي 10,5 m² لأنّ المتر المربّع الواحد يساوي 10 000 cm² ✓. الخطأ الشائع: ضرب المساحة في 100 وحده فنجد 1 050 cm² أي 0,105 m²؛ أو الاكتفاء بمساحة المثلّث الكبير 24 دون نزع ADE؛ أو جمع المساحتين 24 + 13,5 = 37,5 بدل طرحهما. »
(groupes de chiffres en U+00A0). 27 passe à 6 questions, rampe 1,2,2,2,2,3 : le boss redevient honnête.

**M7 — Doublon 26 Q2 / 28 Q1.** Même figure (SVG identique à 1 px près), mêmes données (rectangle en A,
AB = 4, AC = 3) ; 28 Q1 (AB² + AC² = 25) est l'étape de 26 Q2 (BC = 5), et l'explication de 26 Q2
contient 25. Les deux missions sont d3 (même palier de donjon). → **Supprimer 26 Q2** (Q4 donne déjà
BC = 5 cm ; 26 passe à 6 questions, rampe 1,2,2,2,2,3). Supprimer 28 Q1 laisserait 28 à 5 questions.

**M8 — 24 : en-tête boss malhonnête.** Aucune question réellement d3 : Q7 est le rappel du critère
« متوازي أضلاع له ضلعان متتاليان متقايسان » du cours (d2), Q4–Q6 sont d2. → 24 en **d2 practice
75/15**, titre « 🏛️ مناظرة 2006 · التمرين 3 ⭐⭐: … », Q7 `difficulty: 2`. (Après M3 : rampe 1,1,2,2,2,2.)

**M9 — Rendu arabe (Chromium `dir=rtl`, ordre visuel extrait).**
- 26 Q6, explication : mots arabes dans la formule ; « /2 » ouvre l'isolat et s'affiche à l'autre bout
  de la ligne, loin de « الارتفاع ». « مساحة شبه المنحرف = (مجموع القاعدتين) × الارتفاع/2 = (3 + 7,5) × 6/2 = 10,5 × 3 = 31,5 cm² ✓. »
  → « مساحة شبه المنحرف هي نصف مجموع القاعدتين مضروبًا في الارتفاع: (3 + 7,5) × 6/2 = 10,5 × 3 = 31,5 cm² ✓. » (rendu vérifié).
- 25 Q8, 26 Q7, 27 Q8, 28 Q6, explications : « 1 m² = 10 000 cm² » s'affiche « m² = 10 000 cm² 1 »
  (nombre puis unité sans opérateur : hors `DIGIT_FIRST_FORMULA`, formule à moitié inversée). Remplacer
  « ولمّا كان 1 m² = 10 000 cm² » par « ولمّا كان المتر المربّع الواحد يساوي 10 000 cm² » (rendu vérifié).
- 25 Q9, explication : la quantité « 6 000 000 cm² » est coupée à la frontière bidi et
  « 6 000 000 cm² = 6 000 000 ÷ 10 000 » égale des cm² à un nombre. Nouvelle explication (vérifiée) :
  « المساحة الحقيقيّة للرواق = 6 × 1 000 000 = 6 000 000 cm²، أي 600 m² لأنّ المتر المربّع الواحد يساوي 10 000 cm². فكلفة المتر المربّع الواحد = 10 200 ÷ 600 = 17 دينارًا ✓. »
- 28 Q6, explication : en plus, « فإنّ S = 5 400 ÷ 10 000 = 0,54 m² ✓ » → « فإنّ S = 5 400 cm² = 0,54 m² ✓ ».
Contrôles passés : aucun nombre groupé inversé (U+00A0 partout), aucun signe détaché, aucun radical
après son radicande, 8 lignes-équations toutes acceptées par `isDisplayEquation`, aucune paire d'options
à virgule arabe, aucune occurrence piège « على الشكل التالي » (22 Q1 « في الشكل التالي » a bien sa figure).

**M10 — 24 Q1 : renvoi ordinal.** « أمّا الوصف الأخير فيعطي (−3 ; 2) » → « أمّا السير 3 وحدات نحو اليسار ثمّ وحدتين نحو الأعلى فيعطي (−3 ; 2) ».

### Mineurs

- **m1 — Étiquettes.** 27 Q7 (d) `conversion-aire-facteur-errone` ambiguë (13,5 × 100 sans conversion
  donne aussi 1 350) → muette, comme 26 Q7 (b) et 28 Q6 (c). 25 Q5 (d) 1/3 `reponse-a-l-autre-inconnue`
  → `math.geo.segment-mal-choisi` (CF pris pour DF). 28 Q2 (c) `regle-perpendiculaire-parallele-inversee`
  inexacte (aucun parallélisme conclu ; c'est la condition d'entrée de Thalès qui manque) — réglé par
  M2. `condition-suffisante-supposee` sur 22 Q2 (b, c, d) et 22 Q3 (b, d) : la moitié générale du
  libellé convient, mais son exemple (losange) et sa compétence (quadrilatères) sont hors sujet sur une
  symétrie → élargir le libellé : fr « Tu prends une seule propriété pour une preuve : il faut toutes
  les conditions — par exemple, des diagonales perpendiculaires ne suffisent pas au losange, il leur
  faut aussi le même milieu » ; ar « تعدّ خاصيّة واحدة برهانًا: يلزم اجتماع كلّ الشروط — فمثلًا تعامد القطرَين لا يكفي للمعيّن، بل يلزم كذلك أن يكون لهما المنتصف نفسه » ;
  en « You take a single property as proof: every condition is needed — for instance, perpendicular
  diagonals are not enough for a rhombus, they must also share a midpoint ». 25 Q1 (d)
  `hypotenuse-mal-choisie` : réserve acceptée ([DF] est bien un faux choix d'hypoténuse). Cas limite
  déclaré 22 Q3 (a) `symetrie-centrale-un-seul-signe` : exact (sans objet si M1 appliqué).
  `hauteur-confondue-avec-mediane` (25 Q3 c) juste, mais son libellé écrit « AH » (ici DH) — registre.
- **m2 — 23 Q1 (multi)** : (a) → `AB = 2` (fausse : AB = 4 ; 2 est la distance de A à (OJ)), et dans
  l'explication « أمّا O فليست منتصف [AB] لأنّ المنتصف هو (0 ; 3)، وجعلها منتصفًا شأن التناظر المركزي لا المحوري؛ »
  → « أمّا AB فطوله 2 − (−2) = 4 لا 2، والعدد 2 هو بُعد A عن المحور (OJ) فقط؛ ».
- **m3 — Données redonnées (donjon seulement, ordre quête correct).** Énoncés ou figures qui montrent
  une clé antérieure : 22 Q5/Q6/Q7 (H(0 ; 3) sur la grille = Q4), 22 Q7 (K(0 ; −3) = Q6) ; 23 Q4/Q5/Q6
  (C(2 ; −3) = Q3) ; 24 Q4/Q5/Q7 (D(2 ; −3) = Q3), 24 Q6/Q7 (C(4 ; 0) = Q5) ; 25 Q3/Q7 (AF = 5 = Q2),
  Q6 (DH = 2,4 = Q3), Q8/Q9 (6 cm² = Q7) ; 26 Q4 (BC = 5), Q6 (ED = 7,5 = Q5), Q7 (31,5 = Q6) ;
  27 Q4 (BC = 10), Q5–Q7 (AD = 4,5 = Q3) ; 28 Q6 (54 = Q5). Doctrine d'autonomie : acceptés.
- **m4 — 25 Q7** : « و AF = 5 cm » n'est pas nécessaire à la clé (6 = 2 × 3) et livre 25 Q2 au donjon ;
  le retirer ou l'assumer (il nourrit 15 et 14).
- **m5 — Étages et difficultés.** 23 : boss défendable (Q6 d3 honnête, deux multi) mais même exercice
  que 22 (d2) — envisager d2 practice par cohérence. 28 Q4 est d1 (BD = AB + AD, positions données) →
  `difficulty: 1` et le placer en 2ᵉ position (aucune fuite en avant). 25, 26, 28 gardent un vrai d3
  (k² à déduire d'une aire seule) — plus haut que leurs sœurs techniques publiées (08/14, 08/19, 08/20
  en d2 practice), mais justifié. 22 (d2) cohérent avec 12/11-examen-2001.
- **m6 — Échelle.** La glose « أي أنّ كلّ 1 cm على التصميم يمثّل k cm في الواقع » est juste, présente
  dans chaque énoncé qui l'emploie (25 Q8, Q9 ; 26 Q7 ; 27 Q7, Q8 ; 28 Q6), ne donne pas k² et ne livre
  aucune clé ; suffisante en d3 (k² se déduit : un carré de 1 cm figure un carré de k cm). Note : quand
  seule l'aire du plan est donnée (25 Q8, 26 Q7, 28 Q6), la voie « convertir les longueurs d'abord » du
  sujet est fermée — c'est ce qui justifie le d3.
- **m7 — Flèches** « ← » dans 23 Q3, 24 Q2, 24 Q3 (explications) : isolées LTR, « A(2 ; 3) ← C(2 ; −3) »
  se lit « C donne A » (vrai par involution, notation inversée) → « → ».
- **m8 — Groupement incohérent** : 25 Q8 « فنجد 6000 cm² » → « فنجد 6 000 cm² » ; 27 Q7 « فنجد 1350 cm² »
  → « فنجد 1 350 cm² » (U+00A0).
- **m9 — Unité** : « بالصنتمتر » et « بالسنتمتر » alternent dans 25, 26, 27 → unifier (le sujet : الصّنتمتر).
- **m10 — « على التصميم » sans contexte** dans 25 Q7, 26 Q6, 27 Q5, 27 Q6, 28 Q5 (aucun plan introduit
  dans l'énoncé) → introduire « على تصميم قطعة … » en tête ou retirer « على التصميم ».
- **m11 — 28 Q2** : « ⟂ » (U+27C2) → « ⊥ » (U+22A5), seul en usage dans les cours et le corpus (59 contre 1).
- **m12 — Titre 22** : ne nomme pas le parallélogramme testé en Q7 → « … — تناظر محوري وتناظر مركزي ونقطة تقاطع ومتوازي أضلاع ».
- **m13 — Annales recyclées** : 23 Q3 et 24 Q3 ont la même clé (2 ; −3) et 3 options communes (données
  du sujet) ; 22 Q4 ≈ 08/16-examen-2003 Q3 publiée (même clé (0 ; 3), même lecture) ; 22 Q7 est du même
  gabarit que 18/10 Q5 et 18/17 Q5 publiées (mêmes pièges « deux diagonales égales », « une paire de
  côtés parallèles ») — le correctif M2 de 22 Q7 réduit ce recouvrement.
- **m14 — Figures à l'échelle** : exactes au pixel (tests numériques) ; en 28 Q3, DE ≈ 2 BC se lit à
  l'œil (clé 10 devinable) ; inhérent à un « تصميم حسب السلّم ».
- **m15 — 27 Q6** : options 10,5 / 24 / 37,5 en progression (24 ± 13,5) — indice faible (sans objet si M6).

### Observation moteur (hors tranche, non comptée)

Au donjon, la carte de question ne prend `dir="rtl"` que si `color_token === "arabic"`
(`src/routes/_authenticated/dungeon.tsx`, l. 602) ; les maths (`subject-math`) héritent du sens de
l'interface. Tout champ arabe qui commence par une lettre latine (`ABCD مستطيل…`, `(2 ; 3) وهي B…`)
n'obtient pas `dir="rtl"` (`isRtlText` faux) et s'affiche en base LTR pour un élève à l'interface
française ou anglaise : l'ordre des membres de phrase s'inverse. Concerne 19 énoncés et 28 options de
la tranche (et 25 explications), et une part du corpus publié. Correctif côté moteur (dir selon `content_language`) ; contournement contenu
possible : ouvrir le champ par un mot arabe (« ليكن ABCD مستطيلًا … »).

---

## 3. Étiquettes

**Options muettes qui méritent une étiquette EXISTANTE** (porte R1 : l'explication nomme déjà l'erreur) :
- `math.geo.segment-mal-choisi` (« حدّد أوّلًا المثلّث المناسب وأضلاعه ») : 25 Q1 (a) EBC, 26 Q1 (d) BDE,
  25 Q2 (a) √13 (DF pris = 2), 27 Q3 (a) 3,6 (AE/BC, côté non homologue), 25 Q7 (b) 15 (AF × BC),
  25 Q5 (d) (re-étiquetage).
- `math.geo.position-relative-ignoree` : 25 Q2 (c) 3√5 (DF = DC), 26 Q5 (c) 4,5 (BE = AE sans BA),
  28 Q4 (a) et (d) (demi-diagonale) ; (c) reste muette (deux erreurs).
- `math.alg.reponse-a-l-autre-inconnue` (« … أو نتيجة وسيطة ») : 25 Q3 (a) 6 (l'aire au lieu de la
  hauteur), 26 Q6 (b) 37,5 (aire de BDE), 26 Q7 (a) 3 150 et 28 Q6 (d) 5 400 (cm² non convertis ;
  précédent publié 08/19 Q5 a), 27 Q8 réécrite (c) 24.
- 28 Q5 (d) 108 : `aire-losange-sans-moitie` nomme le losange, BCDE n'en est pas un → muette (ou
  élargir le libellé ET l'enseigner : la formule générale n'est pas au cours, l'explication passe par
  les quatre triangles, ce qui est juste et enseigné).

**Familles ≥ 3 questions distinctes → étiquette NOUVELLE méritée** (libellés rendus en Chromium `dir=rtl`, ordre vérifié) :

| id proposé | compétence | fr | en | ar | options |
|---|---|---|---|---|---|
| T1 `math.mes.echelle-aire-rapport-non-carre` | `math.mes.aires` | Tu appliques à une aire le rapport des longueurs : à l'échelle 1/k, chaque longueur est multipliée par k, donc une aire est multipliée par k × k | You apply the length ratio to an area: at a 1/k scale every length is multiplied by k, so an area is multiplied by k × k | تطبّق على المساحة نسبة الأطوال: بالسلّم 1/k يُضرب كلّ طول في k، فتُضرب المساحة في k × k | 25 Q8 (a), 26 Q7 (d), 27 Q7 (a), 28 Q6 (a), 27 Q8 réécrite (a) ; la publiée 08/19 Q6 (c) porte aujourd'hui `conversion-aire-facteur-errone` pour cette erreur |
| T2 `math.geo.parallelogramme-sommets-mal-ordonnes` | `math.geo.quadrilateres` | Tu ordonnes mal les sommets du parallélogramme : dans ABCD, les diagonales joignent les sommets opposés, [AC] et [BD], et ce sont elles qui ont le même milieu | You order the parallelogram's vertices wrongly: in ABCD the diagonals join opposite vertices, [AC] and [BD], and they are the ones that share a midpoint | ترتّب رؤوس متوازي الأضلاع خطأً: في ABCD يصل القطران الرأسين المتقابلين، [AC] و [BD]، وهما اللذان لهما المنتصف نفسه | 22 Q7 (c), 23 Q5 (a, d), 23 Q6 (a, d), 24 Q4 (b, c), 24 Q5 (a, d) ; non vectoriel (le `math.vec.*` homonyme reste aux vecteurs) |
| T3 `math.vec.symetrie-axiale-signe-mal-place` | `math.vec.repere-coordonnees` | Par rapport à un axe, une seule coordonnée change de signe — celle que l'axe ne porte pas : (OI) donne (x ; −y), (OJ) donne (−x ; y) ; changer les deux signes, c'est la symétrie par rapport à O | In an axis only one coordinate changes sign — the one the axis does not carry: (OI) gives (x ; −y), (OJ) gives (−x ; y); changing both signs is the reflection in O | بالنسبة إلى محور تتغيّر إشارة إحداثيّة واحدة هي التي لا يحملها المحور: (OI) يعطي (x ; −y) و (OJ) يعطي (−x ; y)، وتغيير الإشارتين معًا تناظر بالنسبة إلى O | 23 Q3 (b, c) (+ repli de 24 Q2 : a, d) ; famille aussi en 23 Q2 et 12/13-examen-2015 Q3 publiée |
| T4 `math.vec.symetrique-confondu-avec-milieu` | `math.vec.repere-calculs` | Tu t'arrêtes au milieu : le symétrique de A par rapport à K est de l'autre côté de K, à la même distance — K est le milieu de [AA′], pas le point cherché | You stop at the midpoint: the image of A in point K lies on the other side of K at the same distance — K is the midpoint of [AA′], not the point you want | تتوقّف عند المنتصف: نظيرة A بالنسبة إلى K تقع في الجهة الأخرى من K وعلى البعد نفسه، و K منتصف [AA′] لا النقطة المطلوبة | 22 Q5 (c), 23 Q6 (c), 24 Q5 (b) |

Restent muettes (sous le seuil ou ambiguës) : aires composées « somme au lieu de différence » (27 Q6 a /
Q8 réécrite d), aire du rectangle pour celle du parallélogramme (25 Q7 a), projection au lieu d'image
(23 Q2 d), rôle inversé « H milieu de [OK] » (22 Q5 b, 22 Q6 a), sommet pris pour centre (24 Q4 a),
toutes les options à deux erreurs des plans 2×2.

## 4. Programme, fidélité, figures — sans défaut supplémentaire

- **Enseigné** (ordre du manifeste 12 → 08 → 09 → 18) : coordonnées des symétriques par rapport à
  (OI), (OJ), O et à un point (ch. 18, méthode « في المعلّم ») ; milieu, distance ; parallélogramme par
  les diagonales et « فخّ الترتيب » ; critères du losange ; aire du trapèze et du parallélogramme (table
  ch. 18) ; Pythagore direct et réciproque, AH × BC = AB × AC (ch. 09) ; Thalès et papillon (ch. 08).
  Aire de BCDE : par les quatre triangles rectangles (enseigné). Échelle : non enseignée, glosée dans
  chaque énoncé (m6). cm² → m² : acquis des classes antérieures, rappelé dans les explications.
  Ni vecteur ni translation dans la tranche.
- **Fidélité** : toutes les données sont celles des transcriptions (2008, 2005, 2006, 2016T, 2017T,
  2018T, 2023T) ; adaptations déclarées conformes, sauf 22 Q3 (M1) et 24 Q2 (M3). Retraits 28 (BC, AD)
  et remplacements 25 Q2, 27 Q3 : aucun doublon publié résiduel trouvé.
- **Figures** : 49 SVG, `viewBox` partout, encre sombre, arabe seulement dans `<title>`, aucun élément
  interdit, rien hors `viewBox` ; l'attribut `unicode-bidi` des `<g>` n'est pas dans la liste DOMPurify
  (retiré au rendu, sans effet sur des étiquettes latines).
- **Numériques** : valeur et unité justes, unité fixée dans l'énoncé (28 Q1 : nombre pur), aucune
  écriture raisonnable refusée (virgule ou point décimal ; 17,000 accepté pour 17).

## 5. Chiffre final

- Questions auditées : **50** (7 fichiers). Résolution aveugle = clé : **50/50**. **Clés fausses : 0.**
- **Questions à reprendre (majeur) : 25** — 22 Q2, Q3, Q7 ; 23 Q2, Q3, Q4, Q5 ; 24 Q1, Q2, Q7 ;
  25 Q1, Q4, Q8, Q9 ; 26 Q1, Q2, Q3, Q6, Q7 ; 27 Q5, Q6, Q7, Q8 ; 28 Q2, Q6.
  Dont 5 suppressions recommandées (22 Q3, 24 Q2, 26 Q2, 27 Q5, 27 Q6) et une réécriture (27 Q8).
- Mineurs : 15 rubriques (m1–m15) ; étiquettes : 4 nouvelles proposées (T1–T4, 19 options : 5 + 9 + 2 + 3), 14 options
  muettes à étiqueter avec un id existant (dont 27 Q8 réécrite c), 3 re-étiquetages (25 Q5 d, 27 Q7 d,
  28 Q2 c — ce dernier sans objet si M2 est appliqué).
- Étages : 24 → d2 practice (M8) ; 23 à rediscuter (m5) ; 22, 25, 26, 27 (après M6), 28 conformes.
