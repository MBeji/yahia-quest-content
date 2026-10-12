# Audit indépendant — tranche L21 (maths 9ᵉ, ch. 09 triangle rectangle, missions 47 à 51)

Auditeur indépendant (consigne `content-ingest/references/gisement-auditeur.md`, skill `content-audit`).
Périmètre : `content/math/09-triangle-rectangle-trigo/exercices/47…51` (arbre de travail `/home/user/wt-m21`),
28 questions. Rien n'est modifié dans le dépôt. Rapport écrit au fil de l'eau.

## Méthode (rappel court)

- Clés re-résolues À L'AVEUGLE : transcriptions officielles lues d'abord (`examens-nationaux/9eme-base/math/
  2019-technique.md`, `2020-technique.md`, `2021-technique.md`, `2022-technique.md`), réponses posées, puis
  énoncés et options extraits SANS clé, explication ni étiquette (script `blind.py`), réponses fixées, puis
  seulement comparaison aux `correctOption`. 28/28 concordent.
- Figures refaites avec de vraies coordonnées AVANT lecture de celles de l'auteur (47 : A, B, C à 16 px/cm ;
  48 : 40 px/cm, H = B + (AB²/BC)·u ; 50 : 25 px/m, M au paramètre 0,3 de [AS] ; 51 : C(0,0) A(6,0) D(4,0)
  B(0,9) E(4,3)), puis comparées pixel à pixel aux SVG ; rendu Chromium (`/opt/pw-browsers/chromium-1194`)
  de toutes les figures distinctes.
- Registre des étiquettes, des compétences, cours et missions publiées : `origin/main` 9a3090c9.
- Rendu arabe : `splitMathRuns` / `isDisplayEquation` / `isMathExpression` de `src/shared/lib/bidi.ts` et
  `utils.ts` du moteur (`/home/user/eng-m21` 618147d, `bidi.ts` identique à `origin/main` d'arena 7cd50eb),
  empaquetés et rendus dans Chromium `dir=rtl` (classes `.math-run` / `.math-equation` du moteur) ;
  contrôle automatique de l'ordre affiché de chaque unité non arabe contre la source.
- Gates : `content:check` vert ; `content:qa:strict` 0 erreur, aucun avertissement sur 47-51 ;
  `content:tranche --chapters 09` : clé strictement la plus longue 0/28 sur la tranche, aucune paire proche
  qui touche 47-51 (les 18 paires signalées sont entre missions publiées 01-05).

---

## Fichier 47 — `47-examen-2019-technique-ex1-qcm-proportion-valeur-numerique-pythagore-perimetre-demi-cercle.json`

En-tête : d2 · practice · 75/15 · displayOrder 47 · rampe 1,1,2,3 (non décroissante). Fidélité : 10 g/ℓ,
1500 g, x = −1 et A = (x − 2)x, AB = 8, AC = 6, demi-cercle de diamètre [BC] extérieur, options officielles
toutes présentes (150/1500/15 ; −3/1/3 ; 14 + 5π / 24 + 5π / 14 + 10π). Coupure déclarée de 3) en Q3 (BC)
et Q4 (périmètre) : fidèle, rien de perdu.

| Q | ma réponse (aveugle) | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | 150 | b (150) | OK | 1500 ÷ 10 |
| 2 | 3 | d (3) | OK · réserve mineure | (−3)(−1) ; −1 et 1 muets sans chemin dans l'explication |
| 3 | 10 | b (10) | OK | √(64 + 36) ; trois distracteurs exacts (14, 100, 2√7 = √28) |
| 4 | 14 + 5π | c (14 + 5π) | OK · **majeur** | l'énoncé énumère le contour : 24 + 5π et 24 + 10π tombent à la lecture |

Figures : Q3/Q4 exactes (AB = 128 px = 8 × 16, AC = 96 px, BC = 160 px, rayon 80 px = 5 cm, I(120 ; 88)
milieu de [BC], arc `sweep=1` qui passe à droite et en bas, loin de A, comme l'officiel ; [BC] en pointillé
comme l'officiel) ; rien ne déborde du `viewBox` (arc jusqu'à y = 168 < 190) ; arabe seulement dans
`<title>`. L'arc vert désigne l'objet de la question, pas la clé.

Étiquettes (libellés `origin/main`) : 1a `puissance-de-dix-rangs-mal-comptes` (÷ 100 au lieu de ÷ 10) exacte ;
1c `pourcentage-recopie-comme-resultat` (« Tu recopies un nombre de l'énoncé au lieu de calculer ») exacte ;
1d `operation-inverse-appliquee` (× au lieu de ÷) exacte ; 2a `int.produit-signes-negatifs` exacte ;
3a `hypotenuse-mal-choisie`, 3c `pythagore-sans-carres`, 3d `pythagore-racine-oubliee` exactes.
Q4 : options muettes, voir les familles neuves plus bas (non retenues, elles restent muettes).

Programme : proportionnalité (7ᵉ/8ᵉ), relatifs (ch. 15/01), Pythagore (ch. 09), périmètre du cercle 2 × π × r
(`math-7eme/12` l. 116 ; le demi-cercle en est la moitié, déduction directe) : tout est enseigné.

Défauts :

- **[MAJEUR] Q4 — l'énoncé désigne la clé.** L'énoncé officiel dit « قيس محيط هذا الشكل » ; l'auteur a écrit
  « ما قيس محيط الشكل المحدّد بالقطعتين [AB] و [AC] وبقوس نصف الدائرة » : il énumère le contour, donc
  « compter le diamètre » contredit l'énoncé et 24 + 5π, 24 + 10π s'éliminent à la lecture ; le piège annoncé
  (diamètre en pointillé compté) n'existe plus, il ne reste qu'un choix 5π / 10π. Correctif (définit la figure
  sans en lister le bord ; prémisses vraies ; aucune option ne devient vraie : le bord du disque-plus-triangle
  vaut 8 + 6 + 5π ; rendu vérifié : lignes « AB = 8 », « AC = 6 » en `.math-equation`, aucune unité mal
  ordonnée) — énoncé (figure inchangée, à recoller après) :
  « في الشكل التالي ، المثلّث ABC قائم في A ، ونعلم أنّ الأطوال بالصنتمتر هي:\nAB = 8\nAC = 6\nألصقنا بالمثلّث ، على ضلعه [BC] ومن خارجه ، نصف قرص قطره [BC] ومركزه I.\nما قيس محيط الشكل الناتج بالصنتمتر ؟ »
  et dans l'explication remplacer « حدّ الشكل يتكوّن من [AB] و [AC] والقوس ، فمحيطه » par
  « حدّ الشكل الناتج يتكوّن من [AB] و [AC] والقوس ، أمّا القطعة [BC] فصارت داخله ، فمحيطه ».
- **[MINEUR · facultatif] Q2 — muets sans chemin.** −1 et 1 sont de vraies erreurs mais l'explication ne les
  nomme pas. Correctif : explication remplacée par
  « نعوّض x بالعدد −1 في العاملين: x − 2 = −1 − 2 = −3 ، ثمّ نضرب في x = −1 ، فنجد A = (−3) × (−1) = 3 ✓ ، لأنّ جداء عددين سالبين موجب. الخطأ الشائع: كتابة (−3) × (−1) = −3 بإهمال قاعدة الإشارات ؛ أو نشر العبارة إلى x² − 2x ثمّ الخطأ في إشارة الجداء −2 × (−1) فنجد 1 − 2 = −1 ؛ أو إهمال القوسين وحساب x − 2x فنجد −1 + 2 = 1. »
  (rendu vérifié ; 1 − 2 = −1 et −1 + 2 = 1 recalculés), et poser `math.int.produit-signes-negatifs` sur
  l'option « −1 » (erreur de signe d'un produit, exacte) ; « 1 » reste muette.
- **[MINEUR · cosmétique] Titre.** Les trois QCM d'examen publiés du chapitre (16, 17, 18) portent
  « اختيار من متعدّد — » / « صواب أم خطأ — ». Proposé :
  « 🏛️ مناظرة 2019 (تقني) · التمرين 1 ⭐⭐: اختيار من متعدّد — تناسب وقيمة عدديّة وفيثاغورس ومحيط شكل بنصف دائرة ».

Verdict 47 : 4/4 clés justes ; 1 majeur (Q4 énoncé), 2 mineurs.

---

## Fichier 48 — `48-examen-2020-technique-ex3-terrain-triangle-pythagore-hauteur-aire-echelle.json`

En-tête : d3 · boss · 120/30 · displayOrder 48 · titre « … ⭐⭐⭐: قطعة أرض مقسّمة — فيثاغورس والارتفاع والمساحة
والسلّم » (notions seulement). Rampe 1,1,2,2,2,2,3. Fidélité : 1/1000, AB = 3 cm, AC = 4 cm, H sur [BC] près
de B ; 1a → Q1, 1b → Q2, 2a → Q3, 2b → Q4, 3a → Q5, 3b → Q6 + Q7 (coupure déclarée, fidèle).

| Q | ma réponse (aveugle) | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | Pythagore, AB² | c | OK | plan 2×2 propre (théorème/réciproque × AB/AB²), b à deux erreurs muette |
| 2 | 5 | b (5) | OK | √(9 + 16) |
| 3 | BC × AH ÷ 2 et AB × AC ÷ 2 | d | OK | plan 2×2 propre, c à deux erreurs muette |
| 4 | 2,4 | a (2,4) | OK · **majeur (doublon publié)** | = `18-quadrilateres/25` Q3 |
| 5 | 1,8 | b (1,8) | OK | √(9 − 5,76) = √3,24 |
| 6 | 2,16 | a (2,16) | OK | 1,8 × 2,4 ÷ 2 |
| 7 | 216 | c (216) | OK · réserve mineure | 2,16 cm² × 1000² = 2 160 000 cm² = 216 m² |

Recalcul : 3,75 = 15/4 (AH × AC = AB × BC), 12, 2,5 (médiane), 0,6, 3,24, √14,76 ; 3,6 = 3 × 2,4 ÷ 2, 4,2, 4,32 ;
21,6 (1 cm → 10 m appliqué tel quel à l'aire), 0,216 (× 1000 puis ÷ 10 000), 2160 : tous faux, chemins justes.

Figures : exactes (A(60 ; 184), B(180 ; 184), C(60 ; 24) à 40 px/cm ; H(136,8 ; 126,4) = pied de la hauteur,
BH = 72 px = 1,8, AH = 96 px = 2,4 ; codages d'angle droit en H recalculés sur les deux côtés). Q4 : AH = 2,4
(96 px) contre l'option 2,5 (100 px) — écart de 4 px, illisible à l'œil ; la médiane n'est pas tracée : la clé
ne se lit pas sur la figure. Observation (comme L14) : Q5 HB ≈ 0,6 × AB se lit à l'échelle ; 3,24 et √14,76
> AB = 3 (hypoténuse de ABH) s'éliminent à vue.

Étiquettes : 1a `pythagore-sans-carres`, 1d `pythagore-reciproque-role`, 2a/2c/2d, 3b `relation-aire-mauvais-cote`
(« la hauteur multiplie un côté de l'angle droit » : AB × AH), 4b `hauteur-confondue-avec-mediane`, 4c
`relation-aire-mauvais-cote` (AH × AC), 4d `alg.coefficient-non-divise`, 5a/5c/5d, 6c `aire-et-perimetre-confondus`
(somme de deux côtés, usage publié 18/25 Q7), 6d `aire-triangle-sans-moitie`, 7a et 7b
`echelle-aire-rapport-non-carre` (deux chemins de la même erreur, tous deux exacts). Muets justifiés : 3a
(BC × AC, aucune entrée exacte), 3c (deux erreurs), 6b 3,6 (hypoténuse prise pour base, aucune entrée exacte ;
nommée dans l'explication), 7d 2160 (voir mineur). Aucune étiquette inexacte.

Programme : AH × BC = AB × AC enseigné au ch. 09 (cours l. 211-275, « المساحة نفسها مرّتين ») ; HB par
Pythagore dans ABH (Q5), la relation HB = AB²/BC n'est pas utilisée ; aire du triangle (acquis). Échelle sur une
aire : le facteur k² n'est enseigné que par `13-geometrie-espace` (hors manifeste 9ᵉ) ; l'échelle des longueurs
l'est (`math-7eme/07`, `math-8eme/05`) ; l'énoncé glose l'échelle des longueurs sans donner k², et l'explication
raisonne par « 1 cm² sur le plan = un carré de 10 m de côté = 100 m² » : acquis par combinaison (échelle des
longueurs + aire du carré), même arbitrage que L15 (M6) et que les cinq missions publiées 18/25-28, 08/19.
Pas un défaut de la mission ; à noter côté cours (ch. 09 ou 08 gagnerait une ligne « les aires sont multipliées
par k × k »).

Fuites : Q4 redonne BC = 5 (clé de Q2), Q5 redonne AH = 2,4 (clé de Q4), Q6-Q7 redonnent HB = 1,8 (clé de Q5) :
ce sont les « استنتج أنّ … » de l'officiel, convention des prémisses (coût connu du donjon) ; aucune explication
ne donne une clé SUIVANTE (ordre d'émission = ordre du fichier). Le correctif de Q4 ci-dessous retire BC = 5.

Défauts :

- **[MAJEUR] Q4 — doublon d'une question publiée du même palier.** `18-quadrilateres/exercices/25-examen-2016-
  technique-…` Q3 (mission d3 boss, comme 48) : « المثلّث ADF قائم في D حيث DA = 3 cm و DF = 4 cm و AF = 5 cm …
  ما طول [DH] » — même triangle 3-4-5 avec l'hypoténuse donnée, même clé 2,4, même piège 2,5 étiqueté
  `hauteur-confondue-avec-mediane`, même explication (aire deux fois, 12 ÷ 5). La mesure de surface ne le voit
  pas (lettres et cadre différents). Correctif : ne plus donner BC (Q4 enchaîne alors Pythagore et la relation,
  ce que l'officiel fait en deux temps, et cesse de redonner la clé de Q2) ; d2 gardé (deux gestes routiniers),
  position inchangée (Q5, qui redonne AH = 2,4, reste après) :
  - énoncé : « في قطعة أرض على شكل مثلّث ABC قائم في A ، النقطة H من القطعة [BC] حيث (AH) ⟂ (BC) ، ونعلم أنّ الأطوال بالسنتمتر هي:\nAB = 3\nAC = 4\nما طول القطعة [AH] بالسنتمتر ؟ » + figure actuelle de Q4 (elle ne porte que 3 cm et 4 cm) ;
  - options : `2,4` (clé) · `2,5` (`math.geo.hauteur-confondue-avec-mediane`) · `12/7` (`math.geo.pythagore-sans-carres` : BC = 3 + 4 = 7) · `0,48` (`math.geo.pythagore-racine-oubliee` : 12 ÷ 25) ;
  - explication : « نحسب أوّلًا الوتر بنظرية فيثاغورس: BC² = AB² + AC² = 9 + 16 = 25 ، إذن BC = 5. ثمّ نحسب مساحة المثلّث ABC بطريقتين: AH × BC = AB × AC ، أي AH × 5 = 3 × 4 = 12 ، ومنه AH = 12 ÷ 5 = 2,4 cm ✓. الخطأ الشائع: اعتبار [AH] ميانة فنجد نصف الوتر 5 ÷ 2 = 2,5 ، مع أنّ H ليس منتصف [BC] ؛ أو جمع الضلعين بدل مربّعيهما فنأخذ BC = 3 + 4 = 7 ونجد AH = 12/7 ؛ أو القسمة على BC² = 25 بدل BC = 5 فنجد 12 ÷ 25 = 0,48. »
  Vérifié : 12/7 ≈ 1,71, 0,48, 2,5 faux et chacun à UNE erreur ; clé non la plus longue (3 caractères contre
  3, 4, 4) ; plus que deux options communes avec 18/25 Q3 (2,4 et 2,5) et un énoncé à deux étapes ; rendu
  Chromium : « AB = 3 », « AC = 4 » en `.math-equation`, aucune unité mal ordonnée ; 2,4 et 2,5 restent
  indiscernables sur la figure. `relation-aire-mauvais-cote` reste portée par Q3 b.
- **[MINEUR] Q7 — 2160 muette et sans chemin.** C'est une vraie erreur (aire du plan × 1000, sans carré ni
  conversion) ; il suffit de la nommer. Correctif : remplacer la fin de l'explication « … بالقسمة على 10 000
  فنجد 0,216. » par « … بالقسمة على 10 000 فنجد 0,216 ؛ أو ضرب 2,16 في 1000 دون تربيع ثمّ الاكتفاء بهذا العدد
  مترًا مربّعًا فنجد 2160. » (espace insécable de « 10 000 » gardée ; rendu vérifié). Observation : le gabarit
  « aire réelle à 1/1000, échelle 0,x / clé / ×10 » est celui de 18/25 Q8 (600 m²) et de 18/26-28 ; données,
  clé et deux options différentes : annales voisines, pas un doublon.
- **[MINEUR · langue] Q1.** « تمثّل الخطّة التالية » : « خطّة » est un plan d'action, pas un dessin ; Q2 dit
  « التصميم ». Remplacer par « يمثّل التصميم التالي ».

Verdict 48 : 7/7 clés justes ; 1 majeur (doublon publié), 2 mineurs. Étage boss justifié (Q4 corrigée = deux
étapes, Q7 = vraie d3 : aire puis échelle au carré puis conversion).

---

## Fichier 49 — `49-examen-2021-technique-ex1-qcm-radicaux-oppose-valeur-absolue-cote-manquant.json`

En-tête : d2 · practice · 75/15 · displayOrder 49 · rampe 1,1,2,2. Fidélité : √2(√8 − √2), 1 − √3,
|1 − √2| − √2, AB = 40 m, BC = 50 m ; options officielles toutes présentes.

| Q | ma réponse (aveugle) | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | 2 | a (2) | OK | √16 − 2 |
| 2 | √3 − 1 | c | OK | −(1 − √3) |
| 3 | −1 | a (−1) | OK | √2 > 1 ⇒ |1 − √2| = √2 − 1 |
| 4 | 30 | b (30) | OK | √(2500 − 1600) |

Étiquettes : 1b `racine-distribuee-sur-somme` (« ou tu fusionnes deux racines ainsi », √8 − √2 → √6) exacte ;
1c `distribution-partielle` exacte ; 2a et 2b `moins-devant-parenthese` (un seul terme changé) exactes ;
2d `oppose-inverse-confondus` exacte ; 3c `valeur-absolue-signe-du-contenu-non-teste` exacte ; 3d
`operation-inverse-appliquee` (+ √2 au lieu de − √2) exacte ; 4a/4c/4d exactes. Muets : 1d 2√2 (officiel),
3b 1 (officiel, signe) : justifiés. Plan 2×2 de Q3 (−1/1 × avec/sans 2√2) sans vote possible.

Programme : radicaux (ch. 02), valeur absolue (ch. 19, avant 09 dans le manifeste), opposé (ch. 15/01),
Pythagore (ch. 09). Rendu : « |1 − √2| − √2 », « √2 × (√8 − √2) », « 1 − √3 » acceptées par `isDisplayEquation`
et rendues dans l'ordre source. Doublons : `12-repere-plan/17` Q4 (√8 − √2 → √2) et `09/18` Q1 (|2π − 6|) :
autres expressions, autres clés, gabarits voisins de sessions différentes — pas des doublons. Q4 sans figure,
comme l'officiel : calcul pur (toutes les données dans l'énoncé), une figure à l'échelle rendrait AC = 30 lisible ;
pas de défaut.

Défaut :

- **[MINEUR · cosmétique] Titre** (même usage que 47). Proposé :
  « 🏛️ مناظرة 2021 (تقني) · التمرين 1 ⭐⭐: اختيار من متعدّد — جذور تربيعيّة ومقابل عدد وقيمة مطلقة وضلع في مثلّث قائم ».

Verdict 49 : 4/4 clés justes ; 0 majeur, 1 mineur cosmétique. Livrable en l'état.

---

## Fichier 50 — `50-examen-2021-technique-ex3-support-mur-pythagore-parallelisme-thales-longueur.json`

En-tête : d3 · boss · 120/30 · displayOrder 50 · titre « … ⭐⭐⭐: دعامة لحائط أثري — فيثاغورس والتوازي وطاليس »
(notions). Rampe 1,1,2,2,2,3,3. Fidélité : AB = 2,5, BS = 6, BN = 1,8, AM = 1,95, ABS rectangle en B, MNS en N ;
1a → Q1, 1b → Q2, 2a → Q3, 2b → Q4, 3a → Q5, 3b-3c → Q6 ; Q7 ajoutée.

| Q | ma réponse (aveugle) | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | Pythagore dans ABS | c | OK | plan 2×2 (triangle × théorème/réciproque), b muette |
| 2 | 6,5 | a (6,5) | OK | √42,25 |
| 3 | parallèles, ⟂ à (SB) | b | OK · réserve (gabarit) | = 33 Q3 / 30 Q4 aux lettres près ; paliers différents tant que 50 reste boss |
| 4 | SM/SA = SN/SB = MN/AB | d | OK · **majeur (vote)** | le vote terme à terme reconstruit la clé |
| 5 | 4,2 | b (4,2) | OK · réserve | 6 − 1,8 ; étiquette de 10,8 inexacte |
| 6 | 1,75 | a (1,75) | OK | 4,2/6 × 2,5 |
| 7 | 4,55 | c (4,55) | OK · réserve | 6,5 − 1,95 ; contrôle 4,55/6,5 = 0,7 = SN/SB |

Recalcul : 8,5, 42,25, √29,75 ; 7,8, 10,8 ; 10,5, 25/7 = 2,5 × 6 ÷ 4,2, 0,75 = 1,8 × 2,5 ÷ 6 ; 1,95, 4,05 = 6 − 1,95,
8,45 : tous faux, chemins justes.

Figures : exactes (B(170 ; 200), S(170 ; 50), A(107,5 ; 200) à 25 px/m ; N(170 ; 155) BN = 45 px ; M(126,25 ; 155)
au paramètre 0,3 de [AS] : AM = 1,95, MN = 43,75 px = 1,75 ; angles droits en B et N du bon côté ; mur hachuré à
droite ; [AB] en pointillé comme l'officiel). Deux défauts de lisibilité (rendu Chromium) — voir mineurs.
Observation : Q6 MN ≈ 0,7 × AB se lit à l'échelle (0,75 et 25/7 s'écartent à vue).

Étiquettes : 1a `segment-mal-choisi` (triangle MNS, usage publié 33 Q1 b), 1d `pythagore-reciproque-role`,
2b/2c/2d, 3c `regle-perpendiculaire-parallele-inversee`, 4a `thales-rapport-inverse`, 4b `thales-formes-melangees`,
5a `segment-mal-choisi`, 5c `operation-inverse-appliquee` (addition au lieu de soustraction, exacte), 6b
`coefficient-non-divise`, 6c `thales-rapport-inverse`, 6d `segment-mal-choisi`, 7a/7b `segment-mal-choisi`, 7d
`operation-inverse-appliquee` : exactes. **5d « 10,8 »** : `operation-inverse-appliquee` dit « une addition au
lieu d'une soustraction (ou l'inverse), une somme au lieu d'un produit, une division au lieu d'une
multiplication » — un produit au lieu d'une différence n'y est pas : à rendre muette (l'explication la nomme
déjà). 4c (deux rapports retournés) muette : justifié.

Programme : Pythagore (ch. 09), deux perpendiculaires à une même droite sont parallèles (`math-6eme/16` l. 183-228),
Thalès (ch. 08) : enseigné. Q7 ajoutée : fidèle à l'esprit du sujet (elle exploite AM = 1,95, donnée officielle
sinon inutilisée, et le contrôle SM/SA = 4,55/6,5 = 0,7 = SN/SB est cohérent) ; elle refait le Pythagore de Q2
(mêmes données) puis soustrait : vraie d3 au sens de l'usage (deux gestes enchaînés + piège BS/AS), mais
redondante avec Q2 — acceptable, à garder.

Fuites : Q4 et Q6 ne redonnent aucune clé ; l'explication de Q6 donne SN = 4,2 (clé de Q5, émise avant) et celle
de Q7 AS = 6,5 (clé de Q2, avant) : convention. Aucune décimale de vérification qui livre un verdict.

Défauts :

- **[MAJEUR] Q4 — vote terme à terme.** Rapport 1 : SM/SA ×2 (c, d), SA/SM, SM/MA ; rapport 2 : SN/SB ×2 (a, d),
  SB/SN, SN/NB ; rapport 3 : MN/AB ×3. Le vote majoritaire de chaque rapport donne exactement la clé d. Correctif
  (chaque distracteur garde UNE erreur, deux rapports cohérents entre eux ; recompté case par case : rapport 1
  SM/SA 1 · SA/SM 2 · SM/MA 1 ; rapport 2 SN/SB 1 · SB/SN 2 · SN/NB 1 ; rapport 3 MN/AB 2 · AB/MN 2 — plus aucune
  majorité sur la clé ; valeurs : a = 10/7, 10/7, 0,7 ; b = 7/3, 10/7, 10/7 ; c = 10/7, 7/3, 10/7 : toutes fausses ;
  longueurs égales, 21 caractères ; rendu `.math-run` LTR vérifié) :
  - option a : `SA/SM = SB/SN = MN/AB` (`math.geo.thales-rapport-inverse` : deux rapports retournés, le troisième non) ;
  - option b : `SM/MA = SB/SN = AB/MN` (`math.geo.thales-formes-melangees`) ;
  - option c : `SA/SM = SN/NB = AB/MN` (`math.geo.thales-formes-melangees`) ;
  - option d (clé) inchangée ;
  - explication : remplacer « الخطأ الشائع: قلب نسبة واحدة فقط ؛ أو مزج نسبة الجزء على الباقي (SM/MA) مع نسبة الجزء على الكلّ (MN/AB) في سلسلة واحدة. » par « الخطأ الشائع: قلب نسبتين وترك الثالثة على حالها ، والنسب الثلاث تُقلب معًا أو لا تُقلب ؛ أو إدخال نسبة الجزء على الباقي (SM/MA أو SN/NB) في سلسلة نسب الكلّ على الجزء. »
- **[MINEUR+] Figure de Q1, Q3, Q4, Q5, Q6, Q7 — le codage de l'angle droit en N est masqué.** L'étiquette « N »
  (x = 158, y = 146) et son halo blanc recouvrent le carré d'angle droit (159-170 × 144-155) : on lit « N- »,
  l'angle droit en N disparaît, alors que c'est l'argument de Q3. Correctif (on déplace l'ÉTIQUETTE, pas le codage
  ni le point ; rendu Chromium vérifié : « N » sous [MN], entre [AS] (x ≈ 119 à y = 172) et le mur, carré
  visible) : dans les six SVG, remplacer
  `<text x="158" y="146" text-anchor="middle" fill="#0f172a">N</text>` par
  `<text x="158" y="174" text-anchor="middle" fill="#0f172a">N</text>`.
- **[MINEUR] Figure de Q2 — « 6 m » posé contre [AS].** L'étiquette (152 ; 118) est entre [AS] (x ≈ 142) et le mur,
  collée à [AS] : on peut lire 6 m comme la longueur demandée [AS]. Correctif (vérifié en rendu : à droite des
  hachures, dans le `viewBox`) : remplacer `<text x="152" y="118" text-anchor="middle" fill="#64748b">6 m</text>`
  par `<text x="206" y="128" text-anchor="middle" fill="#64748b">6 m</text>`.
- **[MINEUR] Q5 — étiquette de « 10,8 »** : retirer `misconceptionTag` (muette).
- **[MINEUR · facultatif] Q5 — difficulté.** Une soustraction 6 − 1,8 est un d1 honnête ; si l'auteur la passe en
  d1, la placer après Q2 (ordre Q1, Q2, Q5, Q3, Q4, Q6, Q7 ; rampe 1,1,1,2,2,3,3 ; aucune fuite : Q3 et Q4 ne
  parlent pas de SN).

Étage : boss justifié (Q6 : soustraction puis Thalès puis division ; Q7 : Pythagore puis soustraction).
Verdict 50 : 7/7 clés justes ; 1 majeur (vote), 4 mineurs (dont la figure, à corriger).

---

## Fichier 51 — `51-examen-2022-technique-ex3-triangle-droite-perpendiculaire-pythagore-parallelisme-thales.json`

En-tête : d3 · boss · 120/30 · displayOrder 51 · titre « … ⭐⭐⭐: مثلّث وعمودي على ضلعه — فيثاغورس والتوازي وطاليس ».
Rampe 1,1,2,2,3,3. Fidélité : AD = 2, DE = 3, AB = 3AE, (CB) ⟂ (AD) ; 1a → Q1, 1b → Q2, 2a → Q3, 2b → Q4,
2c → Q5 + Q6 : fidèle.

| Q | ma réponse (aveugle) | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | Pythagore, AE² = AD² + DE² | c | OK | plan 2×2 (théorème/réciproque × hypoténuse), d muette |
| 2 | √13 | a (√13) | OK | √(4 + 9) ; √10 = vraie erreur (doubler au lieu de carrer), nommée |
| 3 | parallèles, ⟂ à (AD) | b | OK · **majeur (gabarit publié)** | = 30 Q4 / 33 Q3 aux lettres près |
| 4 | AC/AD = AB/AE = CB/DE | d | OK | vote : rapport 2 seul (AB/AE ×2), rapport 1 à quatre valeurs : acceptable |
| 5 | 6 | a (6) | OK · réserve | 2 × 3 ; « 5 » mérite une étiquette existante |
| 6 | 9 | c (9) | OK · réserve | 3 × 3 ; « 4,5 » mérite une étiquette existante |

Recalcul (exact, `Fraction`) : AE = √13, AB = √117 = 3√13, AC = 6, CB = 9 ; distracteurs Q4 : a AC/CD = 3/2 =
AB/BE ≠ CB/DE = 3 ; b CD/AD = 2 = BE/AE ≠ 3 ; c AD/AC = 1/3 ≠ AB/AE = 3 : tous faux. Q5 : 2/3, 4 = CD, 5 = 2 + 3 ;
Q6 : 1 = 3 ÷ 3, 6 = 3 × BE/AE, 4,5 = 3 × AB/BE.

Figures : exactes (C(30 ; 20), A(174 ; 20), D(126 ; 20), B(30 ; 236), E(126 ; 92) à 24 px/cm ; E sur [AB] au tiers
depuis A ; angles droits en C et en D du bon côté ; figure Q1-Q2 cohérente avec la grande). [DE] en vert = donnée,
jamais la clé. Observation : Q5 AC = 3 × AD se lit à l'échelle.

Étiquettes : 1a `hypotenuse-mal-choisie`, 1b `pythagore-reciproque-role`, 2b, 2c, 3a, 4a `segment-mal-choisi`
(CD, BE), 4b `thales-formes-melangees`, 4c `thales-rapport-inverse`, 5b, 5c `segment-mal-choisi` (CD), 6b
`segment-mal-choisi` (BE/AE), 6d `thales-rapport-inverse` : exactes. Muets : 1d (deux erreurs), 2d √10 (aucune
entrée « carré pris pour double » au registre ; erreur réelle, nommée ; elle sert aussi à ne pas laisser √13 seule
la plus longue — légitime ici car l'erreur existe), 3c, 3d : justifiés. **5d « 5 »** : `operation-inverse-appliquee`
(« une somme au lieu d'un produit ») est exacte. **6a « 4,5 »** : CB/DE = AB/BE est exactement `segment-mal-choisi`
(autre segment que celui de la propriété), comme 6b.

Programme : Pythagore (ch. 09), perpendiculaires et parallèles (6ᵉ), Thalès (ch. 08) : enseigné.

Fuites : Q4-Q6 posent (DE) ∥ (CB) (clé de Q3) : convention ; Q6 n'utilise pas AC (clé de Q5) et son explication
ne l'écrit pas ; 6 (clé de Q5) n'est qu'un distracteur de Q6 justifié par BE/AE : pas de fuite.

Défauts :

- **[MAJEUR] Étage — boss annoncé, difficulté d2.** Q5 et Q6 sont une seule application de Thalès avec le rapport
  donné (AB = 3 × AE ⇒ × 3) : d2 honnêtes ; tout le reste est d1-d2. Les missions publiées du même gabarit
  technique ex. 3 (Pythagore + parallélisme + Thalès) sont practice d2 : 30 (2010), 33 (2024), 34 (2026). Correctif :
  `difficulty` 2, `mode` « practice », `xpReward` 75, `rewardCoins` 15, Q5 et Q6 en difficulté 2 (rampe 1,1,2,2,2,2),
  titre « 🏛️ مناظرة 2022 (تقني) · التمرين 3 ⭐⭐: مثلّث وعمودي على ضلعه — فيثاغورس والتوازي وطاليس ».
- **[MAJEUR] Q3 — doublon de gabarit publié (et interne au lot).** « متوازيان ، لأنّ كلًّا منهما عمودي على (AD) » /
  « متعامدان ، لأنّ كلًّا منهما عمودي على (AD) » / « … لأنّ E من [AB] » = 33 Q3 (« … عمودي على (AM) », « … لأنّ B من
  [AM] و C من [AN] ») et 30 Q4, mêmes options aux lettres près, même étiquette, même explication ; 51 passant en d2
  (ci-dessus), les trois tombent dans le même palier, et 50 Q3 est le quatrième exemplaire. On garde 50 Q3 (palier
  boss) et on varie 51 Q3 : même savoir, autre tâche (choisir l'argument suffisant). Correctif vérifié (prémisses
  vraies ; b et c vrais mais insuffisants — démontré : en déplaçant E sur [AB] ils restent vrais et le parallélisme
  tombe ; d faux sur la figure, (CB) vertical et (AB) oblique ; clé 43 caractères, d 58 : clé non la plus longue ;
  rendu : chaque « (DE) », « (CB) », « (AD) », « [AB] » isolé en `.math-run`, ordre conservé) :
  - énoncé : « المثلّث ADE قائم في D ، والنقطة B من نصف المستقيم [AE) ، والمستقيم العمودي على (AD) والمارّ من B يقطع (AD) في C.\nأيّ حجّة تثبت أنّ المستقيمين (DE) و (CB) متوازيان ؟ » + figure actuelle ;
  - options (toutes muettes) : a `كلٌّ من (DE) و (CB) عمودي على المستقيم (AD)` (clé) · b `كلٌّ من (DE) و (CB) يقطع المستقيم (AD)` · c `كلٌّ من (DE) و (CB) يمرّ بنقطة من [AB]` · d `المستقيم (DE) عمودي على (AD) والمستقيم (CB) عمودي على (AB)` ;
  - explication : « المثلّث ADE قائم في D ، فالمستقيم (DE) عمودي على (AD). والمستقيم (CB) عمودي على (AD) بالإنشاء. وكلّ مستقيمين عموديين على مستقيم واحد متوازيان ، إذن (DE) ∥ (CB) ✓ ، وهذا التوازي شرط تطبيق نظرية طاليس. الخطأ الشائع: الاكتفاء بأنّ المستقيمين يقطعان (AD) ، أو بأنّ كلًّا منهما يمرّ بنقطة من [AB] ، فهذا لا يعطي التوازي: لو نقلنا النقطة E على [AB] لبقي الأمران صحيحين ولما بقي (DE) موازيًا لـ (CB) ؛ أو ربط كلّ مستقيم بعمودي مختلف ، والقاعدة تشترط مستقيمًا واحدًا يعمدانه معًا ، و (CB) عمودي على (AD) لا على (AB). »
  (`math.geo.regle-perpendiculaire-parallele-inversee` reste portée par 50 Q3 c.)
- **[MINEUR] Q5 — « 5 » :** poser `math.num.operation-inverse-appliquee` et finir l'explication par « … أو الجمع
  بدل الضرب في النسبة 3 فنجد 2 + 3 = 5. » (au lieu de « … أو الجمع بدل الضرب في النسبة 3. » ; rendu vérifié, chaîne
  de chiffres seuls laissée au sens natif par conception du moteur).
- **[MINEUR] Q6 — « 4,5 » :** poser `math.geo.segment-mal-choisi`.

Verdict 51 : 6/6 clés justes ; 2 majeurs (étage, gabarit de Q3), 2 mineurs.

---

## Partie transversale

### Étiquettes — familles neuves proposées (`en-cours/etiquettes/L21.json`)

`math.mes.diametre-compte-dans-le-contour` et `math.mes.cercle-entier-pour-demi-cercle` : recherche sur
`origin/main` (les 2 291 questions de `content/math/`, plus les 121 exercices et quiz de `content/math*` qui
parlent de « محيط ») : aucune
question publiée de périmètre d'une figure à demi-cercle ; chaque famille n'est portée que par 47 Q4. Moins de
3 questions distinctes ⇒ **non retenues, les options restent muettes** (c'est déjà l'état du fichier).
L'existante `math.geo.perimetre-cercle-facteur-deux-omis-ou-en-trop` (« le 2 va avec le rayon ») ne nomme pas
« le cercle entier au lieu du demi-cercle » : ne pas la poser sur 14 + 10π. Pour mémoire, si la famille revient
(3 questions), les libellés proposés sont justes ; avec le correctif de 47 Q4, celui de
`diametre-compte-dans-le-contour` devrait dire « le diamètre devenu intérieur » plutôt que « tracé en pointillé ».

Bilan étiquettes : aucune étiquette inventée ; inexacte : 50 Q5 d (à rendre muette) ; muettes qui méritent une
étiquette EXISTANTE : 51 Q5 d (`operation-inverse-appliquee`), 51 Q6 a (`segment-mal-choisi`), et, si le correctif
facultatif de 47 Q2 est pris, 47 Q2 « −1 » (`int.produit-signes-negatifs`). Muettes déclarées confirmées : 47 Q2
« 1 », 49 Q1 « 2√2 », 48 Q3 a et c (et 48 Q6 « 3,6 », non déclarée mais justifiée), 51 Q2 « √10 » (erreur réelle,
pas un remplissage) ; 51 Q6 « 4,5 » ne doit PAS rester muette.

### Étages et rampes

47 practice d2 : juste (Q4 d3 = deux gestes). 48 boss d3 : juste. 49 practice d2 : juste. 50 boss d3 : juste (Q6, Q7).
**51 boss d3 : non — practice d2** (majeur ci-dessus). Rampes toutes non décroissantes en ordre de fichier : l'ordre
d'émission est celui du fichier.

### Doublons

- Publiés : **48 Q4 ≈ 18/25 Q3** (3-4-5, hauteur 2,4, piège 2,5, même palier) — majeur ; **51 Q3 ≈ 33 Q3 ≈ 30 Q4**
  (et 50 Q3) — majeur. Gabarits voisins acceptés : 50 Q1 ~ 33 Q1 (paliers différents, 50 restant boss) ; 50 Q4,
  51 Q4 ~ 30 Q5 (chaîne de Thalès, options différentes) ; 48 Q7 ~ 18/25 Q8, 18/26-28 (échelle d'aire : autres données) ;
  47 Q3 (6-8-10) ~ 18/27 Q1 (format numérique) ; 49 Q3 ~ 09/18 Q1 (valeur absolue, autre nombre).
- Entre missions de la tranche : 47 Q3 et 48 Q2 sont le même item à un facteur 2 près (6-8-10 contre 3-4-5, options
  2√7/10/14/100 contre √7/5/7/25) — données officielles, paliers différents (d2 / boss) : observation. Les cinq
  « Pythagore + trio sans-carrés / racine oubliée / hypoténuse » (47 Q3, 48 Q2, 49 Q4, 50 Q2, 51 Q2) sont chacun un
  item officiel. 50 Q3 ↔ 51 Q3 réglé par le correctif de 51 Q3. Aucune paire de missions ne diffère que par ses
  nombres.
- La mesure officielle (`content:tranche`) ne voit aucune de ces paires (énoncés tournés autrement).

### Fuites

Aucune fuite EN AVANT (ordre d'émission = ordre du fichier ; aucune explication ne résout une question suivante).
Les résultats redonnés (48 Q4-Q7, 50 Q4-Q6, 51 Q4-Q6) sont les « استنتج أنّ … » de l'officiel : convention des
prémisses, coût connu du donjon ; le correctif de 48 Q4 en retire un (BC = 5). Coches ✓ toutes après la clé de leur
question ; aucune décimale de vérification qui livre un verdict.

### Rendu arabe, figures, notation

Contrôle Chromium `dir=rtl` de 173 chaînes (titres, énoncés, options, explications) : aucune formule à lettre mal
ordonnée ; seules les chaînes de chiffres seuls (« 8 + 6 = 14 », « 1500 ÷ 10 = 150 ℓ ») et « 10 g », « 1 cm » suivent
le sens arabe, par conception du moteur (commentaire de `DIGIT_FIRST_FORMULA`). Toutes les lignes de formule seules
sont acceptées par `isDisplayEquation` (dont « A = (x − 2)x », « |1 − √2| − √2 », « BC² = … + AC² »,
« AB = 3 × AE », « AE = AB ÷ 3 »). Aucune paire d'options à virgule arabe, aucun « على الشكل التالي », aucun « M' ».
Balayages : chiffres arabo-indiens, LaTeX, `$`, groupes de chiffres à espace simple (les trois « 15 000 »,
« 10 000 » sont en U+00A0), radicande arabe, virgule arabe en notation : 0. Figures : toutes vraies, arabe
seulement dans `<title>`, aucun débordement, aucune ne marque la clé ; deux défauts de lisibilité en 50 (N masquant
l'angle droit, « 6 m » ambigu). Cosmétique non bloquant : « بالصنتمتر » (47, 50) et « بالسنتمتر » (48, 51) coexistent.

---

## Chiffre final

| fichier | questions | clés fausses | critiques | majeurs | mineurs | questions à reprendre |
| --- | --- | --- | --- | --- | --- | --- |
| 47 | 4 | 0 | 0 | 1 (Q4 énoncé) | 2 | Q4 (obligatoire), Q2 et titre (facultatifs) |
| 48 | 7 | 0 | 0 | 1 (Q4 doublon publié) | 2 | Q4 (obligatoire), Q7, Q1 |
| 49 | 4 | 0 | 0 | 0 | 1 | titre (cosmétique) |
| 50 | 7 | 0 | 0 | 1 (Q4 vote) | 4 | Q4 (obligatoire), figure ×6 (N), figure Q2, Q5 |
| 51 | 6 | 0 | 0 | 2 (étage, Q3 gabarit) | 2 | en-tête, Q3 (obligatoires), Q5, Q6 |
| **total** | **28** | **0** | **0** | **5** | **11** | 5 reprises obligatoires (47 Q4, 48 Q4, 50 Q4, 51 en-tête, 51 Q3) + figure 50 |

Verdict de la tranche : **à corriger avant livraison** (aucune clé fausse, aucun critique ; 5 majeurs, tous avec
correctif exact vérifié par calcul et rendu).
