# Re-vérification ciblée — tranche L15 (ch. 18, missions 22 à 28), après correctifs

Base : arbre de travail (fichiers datés 15:28) ; registres lus sur `origin/main` ; moteur `origin/main`
(`bidi.ts`). Aucun fichier du dépôt modifié. Rapport mis à jour après chaque fichier.

## En-têtes (contrôle global)

| mission | titre | étage | xp/coins | displayOrder | questions |
|---|---|---|---|---|---|
| 22 | « 🏛️ مناظرة 2008 · التمرين 3 ⭐⭐: … ونقطة تقاطع ومتوازي أضلاع » ✓ | d2 practice ✓ | 75/15 ✓ | 22 ✓ | 6 |
| 23 | inchangé ✓ | d3 boss | 120/30 | 23 ✓ | 6 |
| 24 | « … ⭐⭐: … » ✓ | d2 practice ✓ (M8) | 75/15 ✓ | 24 ✓ | 6 |
| 25 | inchangé ✓ | d3 boss | 120/30 | 25 ✓ | 9 |
| 26 | inchangé ✓ | d3 boss | 120/30 | 26 ✓ | 6 |
| 27 | inchangé ✓ | d3 boss | 120/30 | 27 ✓ | 6 |
| 28 | inchangé ✓ | d3 boss | 120/30 | 28 ✓ | 6 |

Total 45 questions ✓.

Clés : les 21 questions dont l'énoncé, une option, la figure ou le type a changé ont été re-résolues à
l'aveugle avant lecture de la clé (21/21 = clé) ; les 24 autres gardent la clé de mon premier passage
(0 écart). **45/45 clés justes.** Registre relu sur `origin/main` 8cab736f (aucun libellé `math.*` modifié
depuis le premier audit ; `segment-mal-choisi` et `position-relative-ignoree` y sont, absents de l'arbre).

## Par fichier

### 22 (6 questions, rampe 1,1,1,2,2,2) — RAS

| Q (ancienne) | changé | aveugle = clé | contrôle |
|---|---|---|---|
| 1 (1) | — | d = d | — |
| 2 (2) | option c, explication | a = a | (c) vraie et insuffisante ((1 ; −3) vérifie les deux conditions avec A, = S(OI)(A)) ; plus de (0 ; 3) ni dans (c) ni dans l'explication (fuite vers Q3 levée) ; vote/union neutralisés ; longueurs [65, 68, 48, 62] |
| 3 (4) | — | b = b | — |
| 4 (5) | — | a = a | (c) attend T4 |
| 5 (6) | — | d = d | — |
| 6 (7) | option a, explication | b = b | AK = HC = √37 et milieux (0,5 ; 0), (−0,5 ; 0) exacts ; vote → (c), un distracteur ; (c) attend T2 |

Étiquettes : Q1 a `coordonnees-point-inversees` (M(−3 ; −1) = échange) ✓, c `quadrant-signes-confondus` ✓ ;
Q2 b, d `condition-suffisante-supposee` : la moitié générale du libellé convient, l'exemple (losange) reste
hors sujet sur une symétrie — libellé non élargi sur `origin/main` ni dans l'arbre (m1 du premier audit,
toujours ouvert, mineur) ; Q3 a, Q5 c `coordonnees-point-inversees` ((3 ; 0), (−3 ; 0) = échange de la clé) ✓ ;
Q6 d `paires-de-cotes-paralleles-mal-comptees` ✓. Renumérotation : aucune fuite en avant (Q2 ne donne plus
l'ordonnée 3 du milieu ; l'explication de Q6 affirme « A و C متناظرتان بالنسبة إلى O », vérifiable sur les
coordonnées de l'énoncé, sans appui sur la Q3 supprimée).

### 23 (6 questions, rampe 1,1,1,2,2,3) — RAS

| Q | changé | aveugle = clé | contrôle |
|---|---|---|---|
| 1 (multi) | (a) → `AB = 2`, explication | {b,d,e,f} = {b,d,e,f} | (a) fausse (AB = 2 − (−2) = 4 ; 2 = distance de A à (OJ), phrase juste) ; plus de paire exclusive « منتصف [AB] هو O » / « … هو (0 ; 3) » (l'une des deux forcément juste) ; longueurs a6 b37 c41 d35 e41 f7 : clés ≠ 4 plus longues |
| 2 | (c), explication | a = a | 2×2 {(OI)/(OJ)} × {prolonger/s'arrêter} : a = (OI)+prolonger, b = (OJ)+prolonger, c = (OJ)+arrêt, d = (OI)+arrêt → vote 2-2 / 2-2, nul ; longueurs [70, 70, 63, 63] (clé ex aequo avec b) ; plus de « تناظر مركزي » dans l'explication ; « الجمع بين الخطأين » = (c) exact |
| 3 | figure, explication | d = d | figure = repère + grille + A seul en (172 ; 52) = (2 ; 3) : plus de pointillé ni de point (2 ; 0), rien ne désigne C ; les quatre options placent sur la grille (x ∈ [−3 ; 3], y ∈ [−4 ; 4]) ; « A(2 ; 3) → C(2 ; −3) ✓ » = un seul isolat LTR, flèche A → C à l'écran (Chromium) |
| 4 (multi) | (f) ajoutée, explication | {b,d} = {b,d} | (f) vraie pour B, C et insuffisante : (−2 ; −3) a pour ordonnée −3 (opposée de 3) et OB = √13, et c'est S(OI)(B) ; paires (e)/(d) et (a)/(f) cassent l'heuristique « conjonction = suffisante » ; longueurs a40 b48 c52 d52 e38 f42 : {c,d} ≠ clé |
| 5 | (b), figure, explication | c = c | figure = polyligne A–C–O (côtés [AC], [CO]), points A(2 ; 3), C(2 ; −3), O ; plus de diagonale [AO] ; vote : point réfléchi A (b, d), centre « منتصف » (a, c, d) → (d), un distracteur ; longueurs [39, 30, 39, 39] ; (b) fausse : D(−2 ; −3) → milieux (1 ; 1,5) ≠ (0 ; −3) ; explication de (b) vraie |
| 6 | — | b = b | — |

Étiquettes : Q3 a `coordonnees-point-inversees` ((−3 ; 2) = (2 ; −3) aux coordonnées échangées) ✓ exact ;
Q3 b, c en attente de T3 ; Q5 a, d et Q6 a, d de T2 ; Q6 c de T4 ; Q2 b (mauvais axe : T3 parle des signes de
coordonnées, pas d'une construction), c (deux erreurs), d (projection) muettes, comme au premier audit — cohérent. Rendu : `tokcheck` v2 (Chromium, `dir=rtl`) 0 problème ;
segmentation des chaînes changées : `AB = 2` option LTR (`isMathExpression`), ⟦2 − (−2) = 4⟧ et
⟦A(2 ; 3) → C(2 ; −3) ✓⟧ en un isolat chacune ; ordre visuel relu. Le ✓ final inclus dans l'isolat suit la
convention du moteur (`bidi.ts`, `peelEdgePunctuation`), pas un défaut de la tranche.

### 24 (6 questions, rampe 1,1,2,2,2,2, d2 practice 75/15 ⭐⭐) — RAS

| Q (ancienne) | changé | aveugle = clé | contrôle |
|---|---|---|---|
| 1 (1) | explication (M10) | a = a | plus de renvoi ordinal : « أمّا السير 3 وحدات نحو اليسار ثمّ وحدتين نحو الأعلى فيعطي (−3 ; 2) » (texte M10 exact) ; (−3 ; 2) = échange + deux signes, juste ; longueurs 57 × 4 |
| 2 (3) | explication (m7) | c = c | « A(−2 ; 3) → D(2 ; −3) ✓ » un seul isolat ; milieu (0 ; 0) juste ; (−2 ; −3) = S(OI)(A) juste ; figure = A seul en (52 ; 52) = (−2 ; 3), D absent ; rien sur B, C |
| 3 (4) | — | d = d | figure : côtés [OB], [OD] seulement, (2 ; 0) non marqué |
| 4 (5) | — | c = c | figure : O, B, D seulement |
| 5 (6) | — | a = a | — |
| 6 (7) | d3 → d2 | b = b | rappel direct du critère du losange : d2 honnête ; vote « ضلعان متقابلان » (a, d) → distracteurs ; longueurs [32, 32, 37, 36] |

Étiquettes (9) : Q1 b `coordonnees-point-inversees` ((3 ; −2) = A échangé) ✓, c `quadrant-signes-confondus`
((2 ; 3), 1ᵉʳ quadrant au lieu du 2ᵉ) ✓ ; Q2 a `coordonnees-point-inversees` ((−3 ; 2) = clé échangée) ✓,
b `symetrie-centrale-un-seul-signe` ✓ exact ; Q5 b `pythagore-sans-carres` (2 + 3 = 5, écarts additionnés
sans carrés) ✓, c `distance-sans-racine` (13) ✓ ; Q6 c `diagonales-proprietes-mal-attribuees` (même milieu
= tout parallélogramme) ✓ exact ; Q6 a, d `condition-suffisante-supposee` ✓ — même emploi que le publié
(18/01-pratique Q2, 18/13 Q8, 18/17 Q6 : propriété de tout parallélogramme prise pour suffisante).
Muettes cohérentes : Q1 d, Q2 d (deux erreurs), Q3 a (sommet pris pour centre) ; Q3 b/c, Q4 a/d → T2 ;
Q4 b → T4. Renumérotation : aucune fuite en avant (Q2 n'énonce ni B ni C ; Q3 ne donne pas C ; Q5 dit
OB = BC mais Q6 déclare toutes ses options vraies, la clé reste à justifier). Données redonnées (D en Q3/Q4,
C en Q5/Q6) = m3 accepté.

### 25 (9 questions, rampe 1,2,2,2,2,2,2,3,3) — RAS

| Q | changé | aveugle = clé | contrôle |
|---|---|---|---|
| 1 | (d), explication, étiquette a | c = c | 2×2 : triangle ADF (c, d) / EBC (a) / AECF (b) × sommet de l'angle droit D/B/A, une fois chacun → le vote s'arrête sur c ou d ; longueurs [74, 69, 74, 74] ; « زاوية المثلّث ADF في A جزء من زاوية المستطيل » juste |
| 2 | étiquettes a, c | b = b | — |
| 3 | étiquette a | d = d | — |
| 4 | (d), explication | a = a | 2×2 {« ∥ » (a, c) / « استقامة » (b, d)} × {direct (a, b) / réciproque (c, d)} : 2-2 partout ; longueurs [70, 87, 73, 83] (clé la plus courte) ; « الجمع بين الخطأين » = (d) exact |
| 5 | étiquette d | c = c | — |
| 6 (num) | énoncé : « احسب DK بالصنتمتر » | 3,6 = 3.6 cm | unité dans l'énoncé ✓ ; rien de Q6 n'est donné avant (Q5 s'arrête à 2/3) |
| 7 | énoncé : « على تصميم منتزه، … بالصنتمتر المربّع » ; étiquette b | d = d | « و AF = 5 cm » gardé (écart accepté) ; l'énoncé s'ouvre désormais en arabe (`dir=rtl` partout) |
| 8 | explication (M9) | b = b | « ولمّا كان المتر المربّع الواحد يساوي 10 000 cm² فالمساحة = 6 000 000 ÷ 10 000 = 600 m² ✓ » : ordre visuel Chromium conforme (lecture RTL : المساحة = 6 000 000 ÷ 10 000 = 600 m²) |
| 9 (num) | explication (M9) | 17 = 17 دينار | plus de chaîne « … cm² = … ÷ … = … m² » ; « أي 600 m² لأنّ المتر المربّع الواحد يساوي 10 000 cm² » rendu dans l'ordre ; « 17 دينارًا » (tamyīz) juste |

Étiquettes (15), relues contre les libellés `origin/main` : Q1 a `segment-mal-choisi` (mauvais triangle,
« repère d'abord le bon triangle ») ✓, d `hypotenuse-mal-choisie` ✓ ; Q2 a `segment-mal-choisi` (DF pris = AE
= 2) ✓, c `position-relative-ignoree` (DF = DC, FC non retranché) ✓, d `pythagore-sans-carres` (3 + 4) ✓ ;
Q3 a `reponse-a-l-autre-inconnue` (aire 6 = résultat intermédiaire) ✓, c `hauteur-confondue-avec-mediane`
(2,5 = demi-hypoténuse) ✓ ; Q4 b `thales-sans-verifier-parallelisme` ✓, c `thales-reciproque-role` ✓ ; Q5 a
`thales-formes-melangees` (DF/CF « partie sur reste » face à DH/DK « partie sur tout ») ✓, b
`thales-rapport-inverse` ✓, d `segment-mal-choisi` (CF au lieu de DF) ✓ ; Q7 b `segment-mal-choisi` (BC
n'est pas la hauteur relative à [AF]) ✓, c `aire-et-perimetre-confondus` (2 × (2 + 5)) ✓ ; Q8 d
`conversion-aire-facteur-errone` (÷ 100 au lieu de ÷ 10 000) ✓. Muettes : Q1 b (Pythagore sans angle droit :
aucun id existant), Q3 b (DA pris pour DH : `segment-mal-choisi` ou `relation-aire-mauvais-cote`
(DH × DF = DA × DF) — ambiguë, muette fondée), Q4 d, Q7 a, Q8 c (deux erreurs) ; Q8 a → T1.
Renumérotation : sans objet (ordre inchangé) ; données redonnées Q3/Q6/Q8/Q9 = m3 accepté.

### 26 (6 questions, rampe 1,2,2,2,2,3) — 1 mineur (préexistant)

| Q (ancienne) | changé | aveugle = clé | contrôle |
|---|---|---|---|
| 1 (1) | (b), explication, étiquette d | c = c | 2×2 {ABC (a, c) / BDE (b, d)} × {réciproque (a, b) / directe (c, d)} : vote nul ; longueurs [60, 60, 57, 57] |
| 2 (3) | (c), explication | d = d | « A من [BE] و C من [BD] » (a, c, d) écarte seulement b ; « ∥ » 2-2, direct/réciproque 2-2 → pas de clé unique ; longueurs [77, 73, 61, 73] |
| 3 (4) num | énoncé : « احسب BD بالصنتمتر » | 12,5 = 12.5 cm | BC = 5 désormais donné (l'ex-Q2, doublon de 28 Q1, est supprimée) ✓ |
| 4 (5) | étiquette c | b = b | — |
| 5 (6) | énoncé : « على تصميم قطعة معدنية، … » ; explication (M9) ; étiquette b | a = a | « /2 » réglé : ⟦(3 + 7,5) × 6/2 = 10,5 × 3 = 31,5 cm² ✓⟧ un seul isolat ; **mineur ci-dessous** |
| 6 (7) | explication (M9), étiquette a | c = c | « ولمّا كان المتر المربّع الواحد يساوي 10 000 cm² » rendu dans l'ordre ; 3 150 → 0,315 juste |

**m-R1 (mineur, préexistant, manqué au premier passage — l'étiquette posée le rend visible) — 26 Q5 (b) 37,5.**
Ce distracteur est l'aire de BDE, (7,5 × 10)/2. Or ni B ni BE = 10 ne figurent dans l'énoncé autonome, ni dans
la figure (trapèze ACDE seul). Au donjon, l'option est donc inatteignable, et l'explication parle de « المثلّث
الكبير BDE » et de « المثلّث ABC », absents. Correctif vérifié (arithmétique, longueurs [4, 4, 2, 2], Chromium
`dir=rtl` : 0 problème) :
- option (b) : `37,5` → `22,5` ; `misconceptionTag` : `math.alg.reponse-a-l-autre-inconnue` →
  `math.mes.aire-trapeze-sans-demi-somme` (« une seule base … ne convient pas » : exact) ;
- explication : « أو حساب مساحة المثلّث الكبير BDE، (7,5 × 10)/2 = 37,5، دون طرح المثلّث ABC. » →
  « أو نسيان القاعدة الصغرى AC مع الإبقاء على القسمة على 2 فنجد (7,5 × 6)/2 = 22,5. »

Le plan devient 2×2 {somme / une base} × {÷ 2 / sans ÷ 2} : 31,5 (clé), 22,5, 45, 63 ; aucune option n'est somme
ou différence de deux autres ; clé ex aequo la plus longue avec (b).

Étiquettes (10) : Q1 d `segment-mal-choisi` (mauvais triangle BDE) ✓ ; Q2 a `thales-sans-verifier-parallelisme`
✓, b `thales-reciproque-role` ✓ ; Q4 a `thales-longueurs-au-lieu-de-rapports` (3 + 6 = 9) ✓, c
`position-relative-ignoree` (BE = AE = 6, BA non ajouté) ✓, d `thales-rapport-inverse` (1,2) ✓ ; Q5 c, d
`aire-trapeze-sans-demi-somme` ✓ ; Q5 b `reponse-a-l-autre-inconnue` : libellé exact pour l'erreur décrite,
mais l'erreur est inatteignable (m-R1) ; Q6 a `reponse-a-l-autre-inconnue` (3 150 cm² non converti, précédent
08/19 Q5 a) ✓. Muettes : Q1 a (réciproque de Pythagore : aucun id), Q1 b, Q2 c (deux erreurs), Q6 b (31,5 :
÷ 100 ou aire du plan, ambiguë — voulue) ; Q6 d → T1. Orthographe « بالصنتمتر » désormais uniforme dans la
tranche (graphie majoritaire du publié, 87 occurrences).

### 27 (6 questions, rampe 1,2,2,2,2,3) — RAS (+ 1 étiquette facultative)

| Q (ancienne) | changé | aveugle = clé | contrôle |
|---|---|---|---|
| 1 num | — | 10 = 10 cm | — |
| 2 | — | a = a | — |
| 3 | étiquette a | c = c | — |
| 4 num | énoncé : « احسب DE بالصنتمتر » | 7,5 = 7.5 cm | — |
| 5 (7) | énoncé « على تصميم قطعة خشبيّة، … » ; d3 → d2 ; explication ; étiquette d retirée | b = b | d2 honnête (longueurs réelles 4,5 m et 6 m puis demi-produit) ; (d) 1 350 muette : deux dérivations (× 100 en cm² ; ÷ 100 au lieu de ÷ 10 000) ; « 1 350 » désormais groupé (U+00A0) ; figure : triangle ADE seul, sans mesure |
| 6 (8, réécrite) | tout | b = b | 24 − 13,5 = 10,5 cm² ; × 10 000 → 105 000 cm² = 10,5 m² ; 0,105 = × 100 seul ; 24 = ABC seul ; 37,5 = somme au lieu de différence. Longueurs [5, 4, 2, 4] (la plus longue est un distracteur). Vote : sans objet (numérique). Progression 10,5 / 24 / 37,5 : le centre 24 est un distracteur. Le ✓ suit « 10 000 cm² », dans la phrase qui conclut « 10,5 m² » : aucun distracteur à côté (écart accepté). Figure : ECBD grisé = E, C, B, D, échelle exacte (30 px/cm) |

Doublons : les ex-Q5 (13,5 cm²) et ex-Q6 (10,5 cm²) sont supprimées. Q5 et Q6 n'ont plus la même clé, et
aucune clé n'est répétée dans la mission. Aucune fuite en avant : Q5 dit « مساحة التصميم 13,5 cm² »
(aire ADE), une donnée dont Q6 a besoin et qu'elle redonne elle-même ; rien qui livre 10,5.

Étiquettes (7) : Q2 b `thales-sans-verifier-parallelisme` ✓, c `thales-reciproque-role` ✓ ; Q3 a
`segment-mal-choisi` (AE/BC, côté non homologue) ✓, b `thales-longueurs-au-lieu-de-rapports` (AB − CE = 4) ✓,
d `thales-rapport-inverse` ✓ ; Q5 c `aire-triangle-sans-moitie` (27) ✓ ; Q6 c `reponse-a-l-autre-inconnue`
(aire de ABC) ✓. Muettes : Q2 d (« deux triangles rectangles sont semblables » : aucun id), Q5 d (voulue) ;
Q5 a, Q6 a → T1.

**Facultatif (rectifie mon premier audit, qui la laissait muette)** : 27 Q6 (d) 37,5 a un id existant
exact, `math.num.operation-inverse-appliquee`. Son libellé : « Tu fais l'opération contraire de celle
demandée : une addition au lieu d'une soustraction… ». L'énoncé demande « ما يبقى … بعد نزع ». L'id est
employé 69 fois dans le publié de 9ᵉ, dont 08/19 et 08/20 techniques. L'explication nomme déjà l'erreur
(« جمع المساحتين 24 + 13,5 = 37,5 بدل طرحهما »), ce qui satisfait R1.

### 28 (6 questions, rampe 1,1,2,2,3,3) — RAS

| Q (ancienne) | changé | aveugle = clé | contrôle |
|---|---|---|---|
| 1 num | — | 25 = 25 | plus de doublon avec 26 (ex-26 Q2 supprimée) |
| 2 (4) | d2 → d1, placée 2ᵉ ; étiquettes a, d | b = b | d1 honnête (BD = AB + AD, positions données) ; 2×2 {BD 12/8} × {CE 9/6} : vote nul ; longueurs [16, 16, 15, 15] ; aucune fuite en avant : énoncé et explication ne donnent ni BC ni DE (Q4), et l'aire de Q5 reste à calculer |
| 3 (2) | (c), explication, étiquette c retirée | a = a | « (BD) و (CE) يتقاطعان في A » (a, b, c) écarte seulement d ; « ∥ » 2-2, direct/réciproque 2-2 ; longueurs [77, 79, 67, 81] ; « الجمع بين الخطأين: التقاطع وحده مع استعمال العكس » = (c) exact ; plus de « ⟂ » (m11 sans objet) |
| 4 (3) | — | d = d | — |
| 5 | énoncé « على تصميم قطعة رخاميّة، … » | c = c | — |
| 6 | explication (M9), étiquette d | b = b | « ولمّا كان المتر المربّع الواحد يساوي 10 000 cm² فإنّ S = 5 400 cm² = 0,54 m² ✓ » : ordre visuel conforme |

Étiquettes (8) : Q2 a, d `position-relative-ignoree` (une demi-diagonale prise pour la diagonale) ✓ ; Q3 b
`thales-sans-verifier-parallelisme` ✓, d `thales-reciproque-role` ✓ ; Q4 a `thales-rapport-inverse` (2,5) ✓, b
`thales-longueurs-au-lieu-de-rapports` (DE = AE = 6) ✓, c idem (différences : 8) ✓ ; Q6 d
`reponse-a-l-autre-inconnue` (5 400 cm² non converti) ✓. Muettes : Q2 c, Q3 c (deux erreurs, conforme à la
règle 2×2 de `gisement-auditeur.md`) ; Q5 a, b ; Q5 d (`aire-losange-sans-moitie` nomme le losange,
BCDE n'en est pas un) ; Q6 c (voulue) ; Q6 a → T1.

## Contrôles transversaux

- **Ordre d'émission** : les rampes sont non décroissantes dans les 7 fichiers, donc ordre d'émission =
  ordre fichier = `displayOrder` de quête. Script « clé d'une question ultérieure présente dans une question
  antérieure » : deux touches seulement, sans fuite. En 22, (0 ; −3) est un distracteur de Q3, expliqué
  comme « على (OJ) لكنّها ليست على (AB) », sans être nommé image de H. En 25, le nombre 6 figure comme
  donnée ou comme aire de ADF, une autre grandeur que l'aire de AECF.
- **Doublons** : Jaccard sur énoncé + options, dans la tranche et contre le publié (1 978 questions).
  Aucun nouveau doublon. Les paires au-dessus de 0,55 sont des questions sœurs d'un même sujet (inconnues
  différentes) ou les recyclages d'annales déjà notés (m13). Le maximum contre le publié est 0,47.
- **Rendu** : `tokcheck` Chromium `dir=rtl` sur les 7 fichiers, à 2 400 px et à 340 px : 0 nombre inversé,
  0 signe détaché, 0 radical déplacé. Les 8 lignes-formules sont acceptées par `isDisplayEquation`.
  Groupement U+00A0 cohérent (aucun groupe à espace simple) ; « 1000 » reste nu, comme dans l'écriture de
  l'échelle « 1/1000 », ce qui est l'usage majoritaire du publié. « ⟂ » : 0.
- **Coches** : les 49 « ✓ » des explications suivent la clé ou un énoncé vrai, jamais un distracteur (27 Q6 : écart accepté).
  Aucun renvoi par lettre ni par ordinal.
- **Compétences** : toutes présentes au registre `origin/main`.
- **Mineurs du premier audit appliqués** : m1 (sauf l'exemple du libellé, côté registre), m2, m5, m7, m8, m9,
  m10, m11, m12 ✓.

## Chiffre final

- Questions re-vérifiées : **45**. Clés : **45/45 justes**. Les 21 questions changées ont été re-résolues à
  l'aveugle : 21/21.
- Correctifs de l'audit : **tous appliqués conformément**. M1 à M10, mineurs, figures 23 Q3 (repère + A seul)
  et 23 Q5 (sans diagonale) : justes et neutres. Les deux écarts déclarés (25 Q7 « AF = 5 », 27 Q6 ✓) sont
  acceptés.
- Étiquettes : **57 relues**.
  - **56 exactes**. Pour 22 Q2 b/d et 24 Q6 a/d, c'est la moitié générale du libellé qui nomme l'erreur, dans
    l'emploi du publié ; l'exemple « losange » reste le m1 ouvert, côté registre.
  - **1 à reprendre : 26 Q5 b** (voir m-R1).
- **Défauts nouveaux : 0 critique, 0 majeur, 1 mineur.**
  - **m-R1 — 26 Q5 (b)**, préexistant et rendu visible par l'étiquette. Correctif exact : `37,5` → `22,5`,
    étiquette `math.mes.aire-trapeze-sans-demi-somme`, et la phrase d'explication donnée plus haut.
  - **Facultatif** : étiqueter 27 Q6 (d) `math.num.operation-inverse-appliquee`.
