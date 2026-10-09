# Audit indépendant L16 — maths 9ᵉ, ch.18 quadrilatères, missions d'examen 29 à 35

> Auditeur indépendant (consigne `content-ingest/references/gisement-auditeur.md`, skill `content-audit`).
> Valide pour : arbre de travail de `/home/user/yahia-quest-content` au 2026-10-02 (fichiers 29 à 35 non suivis),
> registres lus sur `origin/main` = `d8af0b75` ; moteur `origin/main` = `a6fc5400` (bidi.ts, figures, qa).
> Aucun fichier du dépôt modifié. Rapport écrit au fil de l'eau, fichier par fichier.

## Méthode

- Chaque question re-résolue À L'AVEUGLE (vue extraite sans `correctOption`/`answerKey`/explication/étiquettes,
  réponses consignées avant révélation), à partir de la transcription officielle de la session.
- Figures : coordonnées relues par script (milieux, perpendicularités, rapports, angles), rendu Chromium.
- Contrôles du moteur `origin/main` lancés sur la tranche : `check-figures` ✓, `check-overflow` (71 figures,
  aucun texte hors viewBox) ✓, `content:check` ✓, `content:qa --subject math` : 0 constat sur 29–35,
  `content:tranche --chapters 18 --fresh` : clé strictement la plus longue 0/179, paires proches 0.
- Rendu arabe : banc Chromium `dir=rtl` reproduisant `RichField`/`OptionContent` (découpage `splitMathRuns`,
  lignes `isDisplayEquation`, `.math-run` isolé LTR), mesure de l'ordre visuel de chaque formule à lettres
  latines et opérateur, à 800 px et 400 px.

---

## 29 — 2001 ex.4 (المسألة) · d4 challenge 300/60 · displayOrder 29 · 11 questions

Titre : « 🏛️ مناظرة 2001 · التمرين 4 ⭐⭐⭐⭐: دائرة وقطر ومستقيم عمودي عليه — فيثاغورس وطاليس وإثبات طبيعة رباعي » —
format conforme, ne livre aucune clé. Données fidèles à 2001.md (rayon 4, H milieu de [OB], (AH) ⊥ (BO), D second
point). Rampe 1,1,2,2,2,2,3,3,3,3,3 non décroissante. Étapes officielles 1a→5c toutes présentes (5b « ACD
équilatéral » devient le calcul de CD, qui avec AC (Q5) et AD = 2·AH (Q3) prouve l'équilatéralité par les longueurs).

| Q | ma réponse (aveugle) | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | d | d | réserve | clé = réunion exacte de a (⊥ seul) et b (milieu seul) : seule option à deux conditions (indice de forme) |
| 2 | 60 | 60 ° | OK | numeric exact, unité dite (« بالدرجة ») |
| 3 | 2√3 | b | réserve | explication du « 2 » au diagnostic faux (le « 2 » reste muet à bon droit : ambiguïté) |
| 4 | a | a | réserve | d (« tout triangle inscrit est rectangle ») = condition manquante comme b, mais muette |
| 5 | 4√3 | c | OK | (voir Q10) |
| 6 | d | d | OK | vrai plan 2×2 (parallélisme justifié ou non × direct/réciproque), même patron pour les 4 options |
| 7 | 3√3 | c | OK | √3, 4√3 − 2, 16√3/3 : erreurs exactes de leurs étiquettes |
| 8 | a | a | réserve | c (diagonales « égales ») porte deux erreurs (prémisse fausse, visible : 4 contre 4√3) et une étiquette |
| 9 | 60 | 60 ° | OK | explication juste (ACB = 30°, HAC = 60°) |
| 10 | 4√3 | b | réserve | quasi-doublon de Q5 : même clé 4√3, 3 options sur 4 communes (4, 4√3, 48) |
| 11 | c | c | réserve | prémisse « ACD متقايس الأضلاع » donne CAD = 60° = clé de Q9 |

Figures (11) : toutes vraies (cercle r = 97, H = (101,5 ; 125) milieu de [OB], A et D à 125 ∓ 84, angles droits
et arcs de 60° exacts, I au quart de [AC] depuis A en Q6/Q7) ; aucune ne marque une clé (l'angle droit en A
n'apparaît qu'en Q5 où il est donné). Pas d'arabe hors `<title>`. Rendu Chromium : aucune formule brouillée.

### Défauts — 29

**MAJEUR 29-Q1 — la clé se reconnaît au nombre de conditions (réunion des moitiés).** a = « عمودي » seul,
b = « يمرّ من منتصف » seul, d (clé) = les deux ; c une seule prémisse. Le vote terme à terme est neutralisé (2/2),
mais la clé reste la seule option à deux conditions, réunion exacte de a et b (quality-bar § No form clue, n° 2).
Correctif (chaque option porte DEUX prémisses vraies ; la clé d inchangée, 97 signes, n'est plus la seule « complète »
et n'est pas la plus longue) :
- a → « (AH) عمودي على [OB] و A من الدائرة، وكلّ نقطة من أيّ مستقيم عمودي على قطعة تبعد البعد نفسه عن طرفَي هذه القطعة » (garde `condition-suffisante-supposee`, 110 signes)
- b → « (AH) يمرّ من منتصف [OB] و OB = 4 cm، وكلّ نقطة من أيّ مستقيم يمرّ من منتصف قطعة تبعد البعد نفسه عن طرفَي هذه القطعة » (garde `condition-suffisante-supposee`, 115 signes)
- c → « A من الدائرة التي مركزها O و [BC] قطر لها، وكلّ نقطة من هذه الدائرة تبعد البعد نفسه عن O وعن B » (muette, 94 signes)
Vérifié : prémisses toutes vraies sous l'énoncé, règles de a/b fausses par une condition manquante, celle de c fausse ;
aucune ne devient juste ; les prémisses ajoutées sont différentes d'une option à l'autre (une prémisse commune aux
trois distracteurs ferait de la clé l'intruse). L'explication reste valable.

**MINEUR 29-Q3 — explication du distracteur « 2 » fausse dans son diagnostic.** « أو أخذ نصف الضلع 4 ÷ 2 = 2 ظنًّا
أنّ الارتفاع ينصّف الضلع » : ici la hauteur [AH] coupe bien [OB] en son milieu, ce n'est pas une croyance fausse.
Le « 2 » sort de deux gestes (4 − 2 = 2 sans les carrés, ou HB pris pour AH) : il reste muet (règle d'ambiguïté),
mais l'explication doit nommer ces gestes. Remplacer par « أو طرح الطولين 4 − 2 = 2 بدل طرح مربّعيهما، أو الخلط بين
[AH] و [HB] ».

**MINEUR 29-Q4 — d muet alors qu'il exécute l'erreur de b.** « كلّ مثلّث رؤوسه الثلاثة على دائرة قائم الزاوية » =
la propriété du cours (ch.18, outil 2) privée de sa condition « un côté est un diamètre ». Ajouter
`math.geo.condition-suffisante-supposee` à d. (Remarque de forme, mineure : la clé a, seule à deux prémisses
« O منتصف [BC] و OA = BC/2 », contient b.)

**MINEUR 29-Q8 — c étiqueté alors qu'il porte deux erreurs.** « قطراه [OB] و [AD] متقايسان » est faux sous les données
(OB = 4, AD = 4√3, visible sur la figure) ET la propriété attribuée est celle du rectangle. Option ✗✗ : retirer
`math.geo.diagonales-proprietes-mal-attribuees` (doctrine : l'option à deux erreurs reste muette). Même remarque de
forme mineure qu'en Q4 : la clé a contient b (AO = AB = 4) et y ajoute DB = DO.

**MINEUR 29-Q10 — quasi-doublon de Q5.** Q5 {48, 4√5, 4√3, 4} et Q10 {4, 4√3, 6 + 2√3, 48} partagent la clé 4√3 et
deux distracteurs ; la valeur 4√3 est en outre redonnée avant Q10 par les explications de Q7 (AC = 4√3) et Q8
(AD = 4√3). La clé commune est inhérente (ACD équilatéral) ; réduire le recouvrement des options :
- remplacer d « 48 » par « 2√6 » (étiquette `math.geo.hypotenuse-mal-choisie` : [CH] pris pour hypoténuse,
  CD² = 36 − 12 = 24) ; options triées : 4 · 2√6 · 4√3 · 6 + 2√3 (clé 3 signes, non la plus longue ; 2√6 ≈ 4,90 ≠ 4√3) ;
- dans l'explication, remplacer « أو التوقّف عند CD² = 48 دون الجذر » par « أو اعتبار [CH] وترًا فنطرح 36 − 12 = 24 فنجد 2√6 ».

**MINEUR 29-Q11 — prémisse redonnée qui livre la clé d'une autre question.** « ACD مثلّث متقايس الأضلاع » donne
immédiatement CAD = 60°, clé numérique de Q9. Sans effet sur la route quête (Q9 précède Q11, tous deux d3, ordre
du fichier) ; possible au donjon (tirage aléatoire). La prémisse est nécessaire aux distracteurs (AC = CD, AD = CD
vrais) : à accepter en connaissance de cause, ou à signaler à l'orchestrateur comme cas d'école de la pratique
« données redonnées ». Les options a et d (deux segments mal choisis chacune) portent `segment-mal-choisi` : une seule
erreur répétée, l'étiquette est exacte — pas de défaut.

Étage 29 : **d4 honnête** — 5 questions d3 sur 11 (chaîne Pythagore → Thalès avec position relative → losange →
angle → perpendicularité), problème de 8 points ; comparable aux d4 publiés (04/28 : 4 d3 sur 11 ; 20/19-21 : 5 d3).
Difficultés par question : justes (Q2 d1 est à la limite d1/d2 : deux constats, rayons + AO = AB).

Bilan 29 : 11 questions, 0 clé fausse, 1 majeur, 5 mineurs.

---

## 30 — 2005 ex.4 (المسألة) · d4 challenge 300/60 · displayOrder 30 · 12 questions

Titre : « 🏛️ مناظرة 2005 · التمرين 4 ⭐⭐⭐⭐: مثلّث متقايس الأضلاع ودائرة قطرها ضلع — طاليس والتناظر المركزي وطبيعة رباعي » —
conforme, aucune clé. Données fidèles à 2005.md (côté 6, O milieu de [BC], cercle de diamètre [BC], F projeté de E,
D = S_A(C), H = (CE) ∩ (BD), I milieu de [BD], K = (AI) ∩ (CE)). Toutes les sous-questions officielles sont reprises
(1b, 2a par la nature de BEC, 2b, 3a, 3b en deux, 4a, 4b, 4c, 5 en deux : AK puis nature) ; AI (Q7) est un maillon
ajouté. Rampe 2×7 puis 3×5, non décroissante.

| Q | ma réponse (aveugle) | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | 3√3 | c | OK | « 3 » muet à bon droit (6 − 3 ou OB : ambiguïté) |
| 2 | قائم في E | a | réserve | deux distracteurs s'éliminent à vue ; explication cite « 3 cm » sans longueur dans l'énoncé |
| 3 | d | d | réserve | clé = réunion de a (hauteur) et c (CA = CB) ; b et l'explication citent « 6 cm » absent de l'énoncé |
| 4 | 3√3/2 | b | réserve | « 3/2 » étiqueté `pythagore-sans-carres` alors qu'il est ambigu (3 − 1,5 ou BF), comme le « 3 » muet de Q1 |
| 5 | 4,5 | 4.5 cm | OK | numeric exact, unité dite |
| 6 | d | d | réserve | clé seule à deux prémisses (A milieu + AB = CD/2) ; a en est la moitié (mineur) |
| 7 | 3 | a | OK | 3√3, 6, 12 : erreurs exactes de `droite-des-milieux-mauvais-cote` ×2 et `…-facteur-deux` |
| 8 | a | a | réserve | clé = réunion de b (milieu seul) et c (parallèle seul) |
| 9 | b | b | OK | vrai plan 2×2 (parallélisme justifié × rapport retourné), longueurs 82/82/67/67 |
| 10 | 2√3 | b | OK | 9√3/8, (3√3 + 3)/2, 6√3 : erreurs exactes de leurs étiquettes |
| 11 | 6 | c | réserve | figure à l'échelle : AK s'y lit égal au côté ; clé redonnée par la prémisse de Q12 |
| 12 | معيّن | c | OK | étiquettes exactes ; explication juste (CK = 6√3 ≠ AB) |

Figures (12) : toutes vraies (côté 145,5 ou 134 unités, E et F milieux exacts, H à 2√3 de B, K = C + 2(E − C) donc E
milieu de [CK], losange ACBK à quatre côtés égaux) ; l'angle droit en E de Q2 n'est pas marqué (clé) ; en Q8 aucun
codage du milieu F (à démontrer). Rendu Chromium : aucune formule brouillée ; « CB/CF = BH/FE » seule sur sa ligne
est bien une ligne-équation.

### Défauts — 30

**MAJEUR 30-Q3 et 30-Q8 — la clé est la réunion des deux options « à une condition manquante »** (même constat que
29-Q1, voir la synthèse « nombre de conditions »). Q3 : d = « CA = CB » (c) + « (CE) ارتفاع » (a). Q8 : a = « E منتصف »
(b) + « (EF) ∥ (AO) » (c). Correctifs (chaque option garde sa règle et porte deux prémisses vraies) :
- Q3 a → « (CE) ارتفاع المثلّث CAB الصادر من C والزاوية CAB قيسها 60°، وكلّ ارتفاع في أيّ مثلّث يمرّ من منتصف الضلع الذي ينزل عليه » (119 signes, garde son étiquette)
- Q3 c → « CA = CB و E من المستقيم (AB)، وفي كلّ مثلّث متقايس الضلعين يمرّ أيّ مستقيم صادر من رأسه من منتصف الضلع المقابل » (≈ 110 signes, garde son étiquette) ; clé d inchangée (107)
- Q8 b → « E منتصف [BA] و F من [BO] و (EF) ⊥ (BC) في المثلّث BAO، والمستقيم المارّ من منتصف ضلع يمرّ من منتصف الضلع الثالث، فـ F منتصف [BO] »
- Q8 c → « (EF) ∥ (AO) في المثلّث BAO و E من [BA] و F من [BO]، والمستقيم الموازي لضلع يقطع الضلع الثالث في منتصفه، فـ F منتصف [BO] »
  (b et c gardent `condition-suffisante-supposee` ; la clé a, 95 signes, reste la plus courte.)

**MINEUR 30-Q2 et 30-Q3 — longueur 6 cm absente des énoncés mais employée.** L'explication de Q2 écrit
« BC/2 = 3 cm », l'option b de Q3 « AB = AC = BC = 6 cm » et l'explication de Q3 « CA = CB = 6 cm », alors que ni
l'énoncé de Q2 ni celui de Q3 ne donnent le côté (distracteur « impossible à obtenir avec les données de l'énoncé »).
Correctif : ouvrir les deux énoncés par « ABC مثلّث متقايس الأضلاع طول ضلعه 6 cm، » comme Q1, Q4–Q7.

**MINEUR 30-Q2 — distracteurs qui s'éliminent à vue.** « قائم الزاوية في B » contredit l'énoncé (B est un angle de
l'équilatéral, 60°) ; « متقايس الأضلاع » contredit la figure (BE ≪ BC). Remplacer d « متقايس الأضلاع » par
« قائم الزاوية في E ومتقايس الضلعين » (33 signes, étiquette `math.geo.description-la-plus-precise-manquee` :
« tu en ajoutes une que rien ne prouve » ; faux : EB = 3, EC = 3√3), et dans l'explication remplacer « أو الظنّ أنّ
BEC متقايس الأضلاع مثل ABC » par « أو إضافة وصف « متقايس الضلعين » لا يُثبته شيء، مع أنّ EB = 3 cm و EC = 3√3 cm ».
La clé (17 signes) n'est pas la plus longue ; la nouvelle option est fausse sous les données.

**MINEUR 30-Q4 — étiquette sur une option ambiguë.** « 3/2 » = 3 − 1,5 (sans les carrés) mais aussi BF pris pour FE ;
la même structure est muette en 29-Q3 (« 2 ») et 30-Q1 (« 3 »). Retirer `pythagore-sans-carres` de a (règle
d'ambiguïté), ou à défaut l'appliquer aux trois : la tranche doit trancher une seule fois.

**MINEUR 30-Q6** — la clé d est la seule à deux prémisses (« A منتصف [CD] و AB = CD/2 ») et a en est la moitié ;
b (BC = CD/2, segment mal choisi) et c (✗✗ muet) n'y ressemblent pas : indice faible, à traiter avec la synthèse.

**MINEUR 30-Q11 — figure à l'échelle qui laisse lire la clé.** AK y mesure exactement le côté AB (133,95 unités) ;
devant {3, 2√3, 6, 6√3}, la clé se lit sans calcul. Ne pas surligner [AK] en vert (le laisser au trait du reste) et
placer K sans tracer le segment [KA] entier (tracer (AI) jusqu'à I seulement, puis K sur (CE)) — ou accepter le défaut.

**MINEUR 30 — prémisses redonnées qui livrent une autre clé (donjon seulement).** Q3 « (CE) عمودي على (AB) » donne la
clé de Q2 (BEC rectangle en E) ; Q12 « E منتصف [CK] » donne celle de Q11 (ACBK parallélogramme, AK = CB = 6). Route
quête sûre (Q2 avant Q3, Q11 avant Q12).

Étage 30 : **d4 défendable** — 5 questions d3 sur 12 dont deux vraies chaînes (Q10 : FE, CF puis rapport ; Q11 :
papillon) ; Q12 est un d3 honnête (critère des diagonales + Pythagore pour écarter le carré). Les d2 sont justes
(Q5, simple addition, serait d1 sans conséquence d'ordre).

Bilan 30 : 12 questions, 0 clé fausse, 2 majeurs (Q3, Q8), 6 mineurs.

---

## 31 — 2006 ex.4 (المسألة) · d4 challenge 300/60 · displayOrder 31 · 11 questions

Titre : « 🏛️ مناظرة 2006 · التمرين 4 ⭐⭐⭐⭐: مستطيل وأشكال داخله — فيثاغورس وطاليس وخاصيّات الرباعيات والمثلّثات » —
conforme, aucune clé. Données fidèles à 2006.md (AB = 9, AD = 3, BF = BC, CE = AF, H projeté de F, M = (AC) ∩ (FH),
K = (EF) ∩ (BC)). Rampe 1,2,2,2,2,2,2,2,3,3,3.
**Sous-questions officielles (12 annoncées → 11)** : rien d'important n'a disparu. 4b (HC, EC puis « H milieu de
[EC] ») est fusionné dans la `multi` Q6 ; AF (Q1) est un maillon ajouté ; 6 est scindé en Q11 (position de K) et Q8
(centre de gravité). Seule perte : 6 demande de montrer que **F** est le centre de gravité ; Q8 le cherche parmi des
points P, Q, R, B définis par des distances (R = F sans être nommé).

| Q | ma réponse (aveugle) | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | 6 | 6 cm | OK | numeric exact, unité dite |
| 2 | 3√10 | c | OK | 6√2, 90 étiquetés exacts ; 2√21 (un seul carré) muet à bon droit |
| 3 | a | a | réserve | b conclut « FBC = BCF », pas l'égalité demandée : s'élimine en lisant ; c (règle privée de « isocèle ») muet |
| 4 | d | d | réserve | clé = réunion de a (égaux) et b (parallèles), seule à deux conditions ; c s'élimine à vue |
| 5 | a | a | OK | c (parallélogramme + 2 côtés consécutifs) porte aussi deux conditions : le nombre ne désigne pas la clé |
| 6 | {a,b,c,d} | {a,b,c,d} | OK | jugé énoncé par énoncé : HC = 3 ✓, EC = 6 ✓, H milieu de [EC] ✓, EH = 3 ✓, H milieu de [CD] ✗ (4,5), HC = 6 ✗ |
| 7 | b | b | OK | vrai plan 2×2 (formes mélangées × parallélisme), 88/88/67/67 |
| 8 | R (AR = 6) | c | **ERREUR de construction** | la prémisse « B منتصف [CK] » (d2, émise avant Q11) livre la clé de Q11 |
| 9 | d | d | réserve | « convergence » : la clé réunit le 1er terme de a et le 1er de b ; c (équilatéral) ne partage rien |
| 10 | √10 | b | OK | 2√2, 4, 9√10 : erreurs exactes de leurs étiquettes |
| 11 | {a,b,c,d} | {a,b,c,d} | réserve | énoncés jugés un à un : (FB) ∥ (EC) ✓, KB = 3 ✓, B milieu de [CK] ✓, KC = 6 ✓, K milieu de [BC] ✗, KB = 1,5 ✗ ; clé déjà donnée par Q8 ; figure à l'échelle |

Figures (11) : toutes vraies (27,1 px/cm ; F, E, H aux abscisses 6, 3, 6 ; M au tiers de [CA] depuis C ; K à BC sous B).
Aucune ne marque une clé (pas d'angle droit en F en Q9). Rendu Chromium : aucune formule brouillée (« 3 + 3 = 6 cm »
de l'explication de Q11 se lit de droite à gauche, comportement voulu du moteur pour l'arithmétique en chiffres).

### Défauts — 31

**MAJEUR 31-Q8 → Q11 — fuite en avant.** Q8 (d2) pose « النقطة K من المستقيم (BC) بحيث B منتصف [CK] » ; Q11 (d3,
émise après) demande de reconnaître parmi ses énoncés « B منتصف [CK] », « KB = 3 cm » et « KC = 6 cm » pour le même
point K. La clé de Q11 est donnée deux questions plus tôt. Correctif préféré (fidèle à l'officiel 6, et honnête en
difficulté) : Q8 redevient la question officielle, en d3, déplacée APRÈS Q11 dans le fichier —
- énoncé : « ABCD مستطيل حيث AB = 9 cm و AD = 3 cm، والنقطة F من [AB] بحيث BF = BC، والنقطة E من [CD] بحيث CE = AF. المستقيمان (EF) و (BC) يتقاطعان في النقطة K.\nأيّ النقاط التالية، وكلّها على القطعة [AB]، هي مركز ثقل المثلّث ACK ؟ » ;
- options : « النقطة P حيث AP = 3 cm » (`centre-gravite-tiers-inverse`), « النقطة Q حيث AQ = 4,5 cm » (`centre-gravite-milieu-mediane`), « النقطة F » (clé), « النقطة B » (muette) ;
- explication : « (FB) ∥ (EC)، فبمبرهنة طاليس في المثلّث KEC: KB/KC = FB/EC = 3/6، ومنه KB = 3 cm = BC، فالنقطة B منتصف [CK] و [AB] هو الموسّط الصادر من A في المثلّث ACK. ومركز الثقل يقع عليه عند ثلثيه انطلاقًا من A: AG = (2/3) × 9 = 6 cm = AF، فهو النقطة F ✓. الخطأ الشائع: عدّ الثلث من الرأس فنجد AP = 3 cm، أو وضعه في منتصف الموسّط فنجد AQ = 4,5 cm، أو أخذ المنتصف B نفسه. » ;
- figure : celle de Q11 (E, F, (EF), K) complétée des segments [AC] et [AK].
Correctif minimal (si la question reste d2) : renommer le point de Q8 (« L » au lieu de « K » dans l'énoncé, le titre
de la figure, l'étiquette et l'explication, « مركز ثقل المثلّث ACL »).

**MAJEUR 31-Q4 — clé reconnaissable au nombre de conditions** (synthèse). d = « متوازيان … ومتقايسان » = réunion de a
(متقايسان) et b (متوازيان). Correctif : donner à a et b une seconde prémisse vraie et différente —
- a → « [AF] و [EC] ضلعان متقابلان في الرباعي AECF، وهما متقايسان و AF = 2 × BF، وكلّ رباعي له ضلعان متقابلان متقايسان فهو متوازي أضلاع »
- b → « [AF] و [EC] ضلعان متقابلان في الرباعي AECF، وهما متوازيان و E من [CD]، وكلّ رباعي له ضلعان متقابلان متوازيان فهو متوازي أضلاع »
(étiquettes inchangées ; AF = 6 = 2 × 3 vrai ; la clé d, 98 signes, reste plus courte.)

**MINEUR 31-Q9 — convergence vers la clé.** d = « قائم » (comme a) + « متقايس الضلعين رأسه F » (comme b) ; c
« متقايس الأضلاع » ne partage aucun terme. Remplacer c par « حادّ الزوايا ومختلف الأضلاع » (✗✗ muet, faux : EFC est
rectangle et isocèle) : chaque terme apparaît alors dans deux options (قائم : a, d ; حادّ : b, c ; متقايس الضلعين : b, d ;
مختلف الأضلاع : a, c) et la clé ne se lit plus par recoupement.

**MINEUR 31-Q11 — figure à l'échelle.** BK y vaut exactement BC (68 unités) et K est dessiné hors de [BC] : « K منتصف
[BC] » et « KB = 1,5 cm » s'éliminent à l'œil, les quatre vrais se lisent. Raccourcir le tracé ou ne pas coder K à
l'échelle exacte (K placé plus bas, sans changer l'alignement E, F, K) — ou l'accepter. Les deux `multi` Q6 et Q11
ont en outre le même gabarit (6 énoncés, 4 vrais : longueur juste / milieu du bon segment vrais, milieu du mauvais
segment / autre valeur faux) : en varier un (par exemple 3 vrais sur 6 en Q11, en remplaçant « KC = 6 cm » par
« KC = 4,5 cm », faux).

**MINEUR 31-Q3** — b conclut « FBC و BCF متقايستان » alors que l'énoncé demande BFC et BCF : elle se rejette à la
lecture attentive. Le piège (sommet compté parmi les angles de base) ne peut pas conclure la paire demandée ; à garder
tel quel (toute réécriture « raison fausse, conclusion juste » qui garderait « متقايس الضلعين رأسه B » deviendrait
défendable). En revanche c (« في كلّ مثلّث قائم زاويتاه الحادّتان … متقايستان » = règle du triangle rectangle isocèle
privée de « isocèle ») mérite `math.geo.condition-suffisante-supposee`.

**MINEUR 31-Q4 c** — « قطراه [AF] و [EC] لهما المنتصف نفسه » : les deux segments sont visiblement deux côtés disjoints
(milieux (3 ; 0) et (6 ; 3)) ; l'option s'élimine à vue. Étiquette exacte, à garder ; mineur.

**MINEUR 31-Q10** — la prémisse « CM/CA = CH/CD » donne la forme juste de Q7 (CH/CD contre CH/HD) : sans effet en
quête (Q7 d2 avant), possible au donjon.

Étage 31 : **en l'état, boss d3 (120/30) est l'en-tête honnête** — 3 questions d3 sur 11 (Q9 nature, Q10 Pythagore +
Thalès, Q11 Thalès + équation) ; les d2 sont des applications directes. C'est le profil des d3 publiés (09/24 : 4 d3
sur 11 en boss). Avec le correctif préféré de Q8 (centre de gravité en d3), 4 d3 sur 11 : le d4 devient défendable.

Bilan 31 : 11 questions, 0 clé fausse, 2 majeurs (Q8 → Q11, Q4), 5 mineurs ; en-tête à revoir.

---
