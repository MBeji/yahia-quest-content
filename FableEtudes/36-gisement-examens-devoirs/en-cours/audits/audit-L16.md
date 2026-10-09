# Audit indépendant L16 — maths 9ᵉ, ch.18 quadrilatères, missions d'examen 29 à 35

> Auditeur indépendant (consigne `content-ingest/references/gisement-auditeur.md`, skill `content-audit`).
> Valide pour : arbre de travail de `/home/user/yahia-quest-content` au 2026-10-02 (fichiers 29 à 35 non suivis),
> registres lus sur `origin/main` = `d8af0b75` ; moteur `origin/main` = `a6fc5400` (bidi.ts, figures, qa).
> Aucun fichier du dépôt modifié. Rapport écrit au fil de l'eau, fichier par fichier ; coupé par une limite de
> session pendant 32, repris le 2026-10-09 (fichiers déclarés inchangés ; empreintes md5 au moment de la reprise :
> 29 `2e97a499` · 30 `02ede86c` · 31 `83dee4bc` · 32 `601bf5bf` · 33 `a2d353f6` · 34 `ae936a46` · 35 `4a4c73a9`).

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

**MINEUR 29 (Q1, Q2, Q4, Q5, Q7, Q8, Q9, Q10) — « شعاعها 4 cm » pour le rayon.** Repris du texte de 2001, mais dans
l'application « شعاع » est le mot du VECTEUR (cours ch.12, 22 occurrences : « إحداثيّات شعاع ») ; les cours ch.08, 09, 18
ne l'emploient jamais pour le rayon et disent « نصف قطر », comme les explications de 29 et les missions 30–35.
Remplacer « وشعاعها 4 cm » / « شعاعها 4 cm » par « ونصف قطرها 4 cm » / « نصف قطرها 4 cm » dans les huit énoncés.

Étage 29 : **d4 honnête** — 5 questions d3 sur 11 (chaîne Pythagore → Thalès avec position relative → losange →
angle → perpendicularité), problème de 8 points ; comparable aux d4 publiés (04/28 : 4 d3 sur 11 ; 20/19-21 : 5 d3).
Difficultés par question : justes (Q2 d1 est à la limite d1/d2 : deux constats, rayons + AO = AB).

Bilan 29 : 11 questions, 0 clé fausse, 1 majeur, 6 mineurs.

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
« KC = 4,5 cm », faux, et dans l'explication « وطولا KB وKC » par « وطول KB »، en ajoutant « أمّا KC فيساوي 6 cm لا 4,5 cm »).

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

## 32 — 2008 ex.4 (المسألة) · d4 challenge 300/60 · displayOrder 32 · 11 questions

Titre : « 🏛️ مناظرة 2008 · التمرين 4 ⭐⭐⭐⭐: مربّع ودائرة مرسومة على قطعة من ضلعه — فيثاغورس وطاليس والمستقيمات الهامة في المثلّث » —
conforme, aucune clé. Données fidèles à 2008.md (côté 6, centre O, I milieu de [BC], J = (AC) ∩ (DI), cercle de
diamètre [BI], K, H = (IK) ∩ (CD), E). Rampe 2,2,2,2,2,3,3,3,3,3,3.
**Sous-questions officielles (13 annoncées → 11)** : rien d'important n'a disparu — 1b, 2a, 2b (en `multi`), 2c, 3a,
3b, 3c, 4a, 4b, 4c, 5 sont tous là. Mais l'ordre logique est inversé : 3c « K milieu de [BO] » (Q5, d2) est émise
AVANT 3b « (IK) ∥ (AC) » (Q6, d3), et Q5 prend le parallélisme pour donnée (voir Q6).

| Q | ma réponse (aveugle) | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | 6√2 | b | réserve | « 3√2 » (= OA, nommé par l'explication) muet : mériterait `segment-mal-choisi` |
| 2 | 3√5 | c | OK | 45, 9, 3√3 : erreurs exactes de leurs étiquettes |
| 3 | {a,b,c,d} | {a,b,c,d} | OK | jugé un à un : [DI] médiane ✓, [CO] médiane ✓, J = intersection des deux ✓, J centre de gravité ✓, J milieu de [DI] ✗, J centre du carré ✗ |
| 4 | a | a | réserve (mineure) | b « قائم الزاوية فقط » étiquetée exactement ; d (angle droit en B, sommet du diamètre) muette : mériterait `hypotenuse-mal-choisie` (voir synthèse § 3) |
| 5 | a | a | OK | d porte aussi deux conditions (mauvais triangle) : le nombre ne désigne pas la clé |
| 6 | d | d | **réserve forte** | a, b et c sont des raisonnements valides à prémisse vraie non justifiée : risque de seconde réponse |
| 7 | 2√5 | c | réserve | « 3√5 » (= DI, « résultat intermédiaire ») muet : mériterait `alg.reponse-a-l-autre-inconnue` |
| 8 | d | d | réserve | la figure montre H au-delà de C : a et c (« H بين D و C ») s'éliminent à l'œil |
| 9 | 9 | b | réserve | 12 et 18 étiquetés alors qu'ambigus ; figure à l'échelle (DH = 1,5 × DC) |
| 10 | a | a | réserve | orthocentre jamais enseigné ni rappelé |
| 11 | c | c | réserve | idem (concours des hauteurs utilisé sans rappel) |

Figures (11) : toutes vraies (côté 180/190/160 unités ; K = milieu de [BO] sur le cercle de diamètre [BI] ; J aux 2/3 de
[DI] et sur (AC) ; DH = 240 = 1,5 × DC ; IH de pente −1 ∥ (AC) ; E sur (DI) prolongé et sur le cercle, B, E, H alignés
sans que la droite soit tracée). Aucun angle droit à démontrer n'est codé. En Q3 les doubles traits de [BO] et [OD]
sont placés au huitième de [BD] et non au milieu de chaque moitié (cosmétique). Rendu Chromium : aucune formule
brouillée ; « DH/DC = DI/DJ » est bien une ligne-équation.

### Défauts — 32

**MAJEUR 32-Q6 — trois distracteurs défendables.** a « (IK) ⊥ (BD) … وكلّ مستقيم عمودي على (BD) يوازي (AC) » et b
« (AC) ⊥ (BD) … وكلّ مستقيم عمودي على (BD) يوازي (IK) » énoncent une affirmation VRAIE dans cette figure (et non une
règle générale fausse comme les autres options « condition manquante » de la tranche) : le raisonnement est valide,
seulement non justifié. c « I منتصف [BC] و K منتصف [BO] … » est déclaré « circulaire » par l'explication, mais K milieu
de [BO] se démontre SANS le parallélisme (Q4 : KBI rectangle isocèle d'hypoténuse BI = 3, donc BK = 3/√2 = BO/2) et
l'élève vient de l'« établir » en Q5 (émise avant) : c est alors un raisonnement juste. Correctif (toutes les prémisses
vraies, chaque inférence fausse par une condition manquante, même gabarit « fait 1، و fait 2، فهما متوازيان ») :
- a → « (IK) ⊥ (BD) لأنّ K من الدائرة التي قطرها [BI]، و (AC) يقطع (BD) في المركز O لأنّ قطرَي المربّع متناصفان، فهما متوازيان » (118 signes, `condition-suffisante-supposee`)
- b → « (AC) ⊥ (BD) لأنّ قطرَي المربّع متعامدان، و (IK) يقطع (BD) في K لأنّ K من الدائرة ومن المستقيم (BD) معًا، فهما متوازيان » (118 signes, `condition-suffisante-supposee`)
- c → « I منتصف [BC] و K نقطة من [BO]، فبخاصيّة المنتصفين يكون المستقيم (IK) موازيًا للمستقيم (OC) وهو نفسه المستقيم (AC) » (113 signes, `condition-suffisante-supposee` : un seul milieu)
- explication, dernière phrase → « أو تطبيق خاصيّة المنتصفين بمنتصف واحد: K في هذه الحجّة نقطة من [BO] فقط، والخاصيّة تشترط منتصفَي ضلعين. »
(clé d inchangée, 103 signes ; chaque fait apparaît dans deux options, aucune règle n'est vraie.)

**MAJEUR 32-Q10 et 32-Q11 — orthocentre (« المركز القائم ») ni enseigné ni rappelé.** Aucun cours de l'application ne le
définit (ch.08, 09, 18 : 0 occurrence ; math-7eme et math-8eme : 0). Les missions publiées le rappellent à chaque
emploi (09/11-Q2 « تذكير: ارتفاعات المثلّث الثلاثة تتلاقى في نقطة واحدة تسمّى المركز القائم للمثلّث », 09/15-Q6-Q7,
09/35-Q8). Q11 : ajouter à l'énoncé, après « المركز القائم للمثلّث DBI »، « (نقطة تلاقي ارتفاعاته الثلاثة) ». Q10 teste la
définition elle-même : le rappel la livrerait (c « موسّطان » et d « حاملا ضلعين » le contrediraient à vue). Deux voies :
(1) préférée — enseigner l'orthocentre dans un cours placé avant ch.18 par le manifeste (ch.08, à côté de « مركز ثقل
المثلّث » : un `::: propriete` + figure), hors des fichiers de la tranche ; (2) sinon, rappel dans l'énoncé de Q10
(« نذكّر بأنّ ارتفاعات أيّ مثلّث تلتقي في نقطة واحدة، تُسمّى المركز القائم للمثلّث. ») et options toutes bâties sur
« deux hauteurs » —
- b → « (IK) عمودي على (BD) فهو ارتفاع صادر من I، و (DC) يمرّ من الرأس D فهو ارتفاع صادر من D، و H نقطة تقاطعهما » (`condition-suffisante-supposee`)
- c → « (DC) عمودي على (BI) فهو ارتفاع صادر من D، و (IK) عمودي على (DI) فهو ارتفاع صادر من I، و H نقطة تقاطعهما » (`segment-mal-choisi` ; faux : IK·DI ≠ 0)
- d → « (DC) عمودي على (DB) فهو ارتفاع صادر من D، و (IK) عمودي على (BD) فهو ارتفاع صادر من I، و H نقطة تقاطعهما » (`segment-mal-choisi` ; faux : angle CDB = 45°)
(clé a inchangée, 103 signes ; b 104, c et d 103.) Faiblesse résiduelle de (2) : c et d sont fausses à l'œil (angles
de 45° et ≈ 108° sur la figure) ; d'où la préférence pour (1).

**MINEUR 32-Q8 — un axe du plan 2×2 se lit sur la figure.** La figure (vraie) place H au-delà de C : les deux options
« H بين D و C أي H من [DC] » (a, c) s'éliminent à l'œil et la question se réduit au sens du rapport (b contre d). Le
plan est sinon propre (a étiquetée `position-relative-ignoree` produit bien DH/DC ; c, position fausse et rapport juste,
muette). Accepter, ou remplacer l'axe « position » par un axe non visible (parallélisme justifié ou non, comme 30-Q9).

**MINEUR 32-Q9 — étiquettes sur des options ambiguës, et figure à l'échelle.** 12 = DC × 2 sort de DH/DC = DJ/JI
(`thales-formes-melangees`, étiquette posée) MAIS aussi du centre de gravité placé au milieu de la médiane
(DI/DJ = 2, `centre-gravite-milieu-mediane`) ; 18 sort de DI/JI = 3 (`segment-mal-choisi`, posée) MAIS aussi du tiers
inversé (DI/DJ = 3, `centre-gravite-tiers-inverse`). Règle d'ambiguïté : rendre 12 et 18 muets (ou choisir les
étiquettes du centre de gravité, l'énoncé donnant « J مركز ثقل »). La figure de Q8/Q9 trace DH = 1,5 × DC : la clé 9 se lit.

**MINEUR 32-Q1 et 32-Q7 — options muettes que l'explication nomme.** Q1 « 3√2 » = OA (explication : « أخذ نصف القطر
3√2 وهو طول [OA] ») → `math.geo.segment-mal-choisi`. Q7 « 3√5 » = la médiane DI entière (« الاكتفاء بطول الموسّط
كاملًا ») → `math.alg.reponse-a-l-autre-inconnue` (« un résultat intermédiaire »).

**MINEUR 32 — prémisses redonnées.** Q9 « DH/DC = DI/DJ » donne la forme juste de Q8 ; Q7 « J مركز ثقل المثلّث BCD »
donne l'énoncé-clé de Q3 ; sans effet en quête (ordre respecté), possible au donjon. Les trois `multi` de la tranche
vues jusqu'ici (31-Q6, 31-Q11, 32-Q3) ont toutes 4 vrais sur 6 : voir la synthèse.

Étage 32 : **d4 honnête** — 6 questions d3 sur 11 (parallélisme par deux perpendiculaires, centre de gravité +
Pythagore, Thalès avec position relative, calcul de DH, orthocentre, alignement par les hauteurs).

Bilan 32 : 11 questions, 0 clé fausse, 2 majeurs (Q6 ; Q10–Q11), 6 mineurs (Q1, Q4, Q7 étiquettes ; Q8 ; Q9 ; prémisses).

---

## 33 — 2009 générale ex.5 · d4 challenge 300/60 · displayOrder 33 · 8 questions

Titre : « 🏛️ مناظرة 2009 · التمرين 5 ⭐⭐⭐⭐: دائرة ومماسّ — فيثاغورس والنسب المثلثية وإثبات طبيعة رباعي » — conforme
(filière générale sans mention, comme le format le veut), aucune clé. Données fidèles à 2009-generale.md (BC = 6,
O milieu, A sur le cercle de diamètre [BC] avec BA = BO, tangente en B, E sur (OA), D symétrique de A par O,
médiatrice de [BC], I, J). Rampe 1,2,2,2,2,2,3,3. Étapes 8 → 8 : 1b, [ABE = 30°, maillon], 2a remplacée par
BAE = 120° (déclaré), 2b, 2c, 3b-aire, 3a, 3b-losange.

| Q | ma réponse (aveugle) | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | a | a | réserve | clé = réunion de b (OA = OB) et c (BA = BO), seule à deux conditions |
| 2 | 30 | 30 ° | réserve | exige « tangente ⊥ rayon », ni enseignée, ni donnée, ni codée sur la figure |
| 3 | 120 | 120 ° | réserve | juste, mais simple supplément de 60° : la marche officielle de 2a (AEB = 30° dans OBE) disparaît |
| 4 | c | c | réserve | clé = réunion de a (AE = AB) et b (AB = AO) |
| 5 | 3√3 | c | réserve | tangente non enseignée (Pythagore dans OBE rectangle en B) ; « 3 » étiqueté mais ambigu |
| 6 | 6√3 | b | **ERREUR de construction** | la donnée « OI = √3 cm » (d2, émise avant) est la clé de Q7 |
| 7 | √3 | b | réserve | tan 30° = √3/3 bien enseigné (ch.09) ; « ظا 30° = OI/OB » de l'explication s'affiche « OI/OB = °30 » |
| 8 | d | d | réserve | b et c (« diagonales égales ») contredits par la figure ; reste a contre d = réunion |

Figures (8) : toutes vraies (r = 97 ou 90 ; BA = BO = OA ; E = 2A − O donc A milieu de [OE] ; EB = 3√3 ; I et J à
√3 de O ; D = −A). **Aucune ne code l'angle droit en B** entre la tangente et [OB]. Pas d'arabe hors `<title>`.
Programme (R-3) : tan 30° = √3/3 figure au tableau des valeurs remarquables du cours ch.09 (« | 30° | 1/2 | √3/2 | √3/3 | »),
ch.09 précède ch.18 au manifeste : Q7 conforme. Rendu Chromium : voir Q7.

### Défauts — 33

**MAJEUR 33-Q6 → Q7 — fuite en avant (donnée redonnée).** Q6 (d2) pose « قطراه [BC] و [IJ] حيث BC = 6 cm و OI = √3 cm » ;
Q7 (d3, émise après) demande « ما طول [OI] » avec √3 parmi {3/2, √3, 3√3/2, 3√3}. L'ordre officiel (3a OI puis 3b
aire) est inversé par les étiquettes de difficulté, et la donnée de l'étape 3a précède la question qui la demande.
Correctif : Q6 redevient l'étape 3b complète, en d3, placée APRÈS Q8 (calcul de OI puis aire = deux notions) —
énoncé « [BC] قطعة منتصفها O وطولها 6 cm، والنقطة A من الدائرة التي قطرها [BC] بحيث BA = BO، والنقطة D مناظرة A بالنسبة إلى O. الموسّط العمودي للقطعة [BC] يقطع (BD) في I ويقطع (AC) في J، والرباعي CIBJ معيّن مركزه O.\nما مساحة المعيّن CIBJ بالصنتمتر المربّع ؟ »,
options inchangées, explication ouverte par le calcul de OI (« الزاوية OBD = 30°، وظلّ هذه الزاوية يساوي √3/3، فـ OI = OB × √3/3 = √3 cm، و IJ = 2√3 cm »).
(Ne pas donner IJ à la place de OI : IJ = 2√3 livrerait OI tout autant.)

**MAJEUR 33-Q2 et 33-Q5 — « المماسّ عمودي على نصف القطر » ni enseigné, ni donné, ni codé.** Aucun cours de
l'application ne mentionne la tangente (ch.08, 09, 18, et math-6/7/8eme : 0 occurrence de « مماس ») ; les énoncés
disent seulement « المماسّ للدائرة في النقطة B » ; les figures ne codent pas l'angle droit en B ; seules les
explications l'affirment. Correctif : dans les deux énoncés, écrire « المماسّ للدائرة في النقطة B، وهو عمودي على (OB)، يقطع المستقيم (OA) في النقطة E »
(et coder l'angle droit en B sur les figures de Q2 et Q5) ; ou enseigner la tangente dans un cours antérieur au ch.18.

**MAJEUR 33-Q8 — deux distracteurs éliminés par la figure, clé par réunion.** b et c affirment « قطراه [BC] و [IJ]
متقايسان » alors que BC = 6 et IJ = 2√3 (la figure montre un losange aplati) ; il reste a (perpendiculaires seules)
contre d (perpendiculaires + même milieu). Correctif (prémisses vraies, même gabarit) :
- b → « قطراه [BC] و [IJ] لهما المنتصف نفسه O لأنّ التناظر المركزي الذي مركزه O يحوّل I إلى J، وكلّ رباعي قطراه لهما المنتصف نفسه فهو معيّن، إذن الرباعي CIBJ معيّن » (155 signes, `condition-suffisante-supposee`)
- c → « قطراه [BC] و [IJ] متعامدان لأنّ (IJ) هو الموسّط العمودي للقطعة [BC]، ولهما المنتصف نفسه O لأنّ التناظر المركزي الذي مركزه O يحوّل I إلى J، فهو مربّع وكلّ مربّع معيّن » (165 signes, `description-la-plus-precise-manquee` : « tu en ajoutes une que rien ne prouve »)
(clé d, 161 signes, n'est pas la plus longue ; c porte les deux prémisses de la clé, la réunion ne la désigne plus ;
c est fausse : CIBJ n'est pas un carré.) Explication : remplacer « أو نسبة تقايس القطرين إلى المعيّن، وهو خاصيّة
المستطيل وليس خاصيّة المعيّن » par « أو الاكتفاء بالمنتصف المشترك، وهو يعطي متوازي أضلاع فقط؛ أو القفز إلى « مربّع »، والقطران غير متقايسين (BC = 6 cm و IJ = 2√3 cm) ».

**MAJEUR 33-Q1 et 33-Q4 — clé reconnaissable au nombre de conditions** (synthèse). Correctifs (seconde prémisse
vraie et différente pour chaque distracteur à une condition ; aucune ne cite une clé d'une autre question) :
- Q1 b → « OA = OB = 3 cm لأنّهما نصفا قطر في الدائرة التي قطرها [BC]، و O منتصف [BC]، فللمثلّث OAB ضلعان متقايسان على الأقلّ، إذن هو متقايس الأضلاع » (137)
- Q1 c → « BA = BO = 3 cm بحكم الإنشاء الذي رسمنا به النقطة A، و BC = 6 cm، فللمثلّث OAB ضلعان متقايسان على الأقلّ، إذن هو متقايس الأضلاع » (126 ; clé a 110)
- Q4 a → « AE = AB = 3 cm لأنّ المثلّث ABE متقايس الضلعين رأسه A، و E على المماسّ في B، وA من [OE]، فالنقطة A تبعد عن E مسافة 3 cm، إذن A منتصف [OE] » (137)
- Q4 b → « AB = AO = 3 cm لأنّ المثلّث OAB متقايس الأضلاع، و O منتصف [BC]، وA من [OE]، فالنقطة A تبعد عن O مسافة 3 cm، إذن A منتصف [OE] » (124 ; clé c 130, d 151)
(Une première version de Q4 a citait « 120° » : écartée, c'est la clé numérique de Q3.)

**MINEUR 33-Q7 — rendu de l'explication.** « فـ ظا 30° = OI/OB » : le segment « 30° = OI/OB » s'ouvre par un nombre
suivi de « ° », que `DIGIT_FIRST_FORMULA` (`[\d.,]*` puis opérateur) ne reconnaît pas ; il n'est pas isolé et s'affiche
« OI/OB = °30 » (Chromium, 400 et 800 px). Remplacer « فـ ظا 30° = OI/OB، أي OI = 3 × √3/3 = √3 cm ✓ » par
« وظلّ هذه الزاوية يساوي √3/3، فـ OI = OB × √3/3 = 3 × √3/3 = √3 cm ✓ » (vérifié au banc : aucun brouillage).
À remonter au moteur : la même forme existe dans des missions publiées (09/06 « ظا 60° = … »), un « ° » après le nombre
devrait entrer dans `DIGIT_FIRST_FORMULA`. Les options 3/2 (sin 30°) et 3√3/2 (cos 30°) sont muettes : famille
« mauvaise fonction trigonométrique », voir la synthèse.

**MINEUR 33-Q3 — remplacement de 2a plus pauvre que l'officiel.** BAE = 180° − 60° ne mobilise ni la tangente ni le
triangle OBE ; la marche officielle (AEB = 30° car BOE = 60° et OBE = 90°, donc ABE isocèle) n'est demandée nulle
part, puis « ABE isocèle en A » est donné en Q4. Option : demander « احسب قيس الزاوية AEB بالدرجة » (30°), qui reprend
cette marche — clé égale à celle de Q2, ce qui est le contenu même de 2a (deux angles de base égaux).

**MINEUR 33-Q5 — « 3 » étiqueté `pythagore-sans-carres` mais ambigu** (6 − 3, ou EB pris égal à AB = AE = OB = 3) :
même politique que 29-Q3 et 30-Q1 (muet). L'étiquette `segment-mal-choisi` de « 3√2 » (Pythagore dans ABE, non
rectangle) est exacte : le libellé dit « repère d'abord le bon triangle et ses côtés ».

Étage 33 : **boss d3 (120/30)** — 2 questions d3 sur 8 (Q7 tan 30° après deux déductions d'angles, Q8 losange) ; Q1–Q6
sont des applications en une ou deux étapes (Q3 est même un d1). C'est le profil des boss publiés (25 : 9 q / 2 d3 ;
09/35 : 12 q / 2 d3). Même avec Q6 corrigée (3 d3 sur 8), l'en-tête challenge d4 n'est pas honnête.

Bilan 33 : 8 questions, 0 clé fausse, 4 majeurs (Q6 → Q7 ; Q2/Q5 tangente ; Q8 ; Q1/Q4), 3 mineurs ; étage à baisser.

---

## 34 — 2010 générale ex.4 · d4 challenge 300/60 · displayOrder 34 · 9 questions

Titre : « 🏛️ مناظرة 2010 · التمرين 4 ⭐⭐⭐⭐: مستطيل ومستقيم عمودي على قطره — فيثاغورس ومعادلة وإثبات طبيعة رباعي » —
conforme, aucune clé. Données fidèles à 2010-generale.md (AB = 8, AD = 4, centre O, I et J sur la perpendiculaire à
(BD) en O, K = (JI) ∩ (AD), x = AI). Rampe 2×7 puis 3×2. Étapes 9 → 9 : 1b, 1c, 1d (nature), 3a en deux (BI², DI²),
développement de (8 − x)² (maillon déclaré), 3b-périmètre, 2, 3b-x ; 1a (construction) non reprise, comme déclaré.

| Q | ma réponse (aveugle) | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | c | c | réserve (mineure) | c réunit a (⊥) et b (milieu), mais b et d portent aussi deux prémisses : indice faible |
| 2 | d | d | réserve | le ✗✗ c n'est pas bâti sur le même patron : le vote terme à terme reconstruit d |
| 3 | معيّن | b | OK | étiquettes exactes ; explication juste (pas d'angle droit en I) |
| 4 | (8 − x)² | d | OK | (8 + x)² étiquetée exacte ; 64 − x², 8 − x² muettes à bon droit |
| 5 | x² + 16 | a | OK | trois étiquettes exactes |
| 6 | 64 − 16x + x² | c | OK | 64 + x² → `carre-somme-sans-double-produit` exact (« d'une somme ou d'une différence ») ; 64 + 16x + x² → `carre-difference-signes` exact ; 64 − x² (deux erreurs) muette |
| 7 | 20 | 20 cm | **ERREUR de construction** | « AI = 3 cm » donné (d2, émise avant) = clé de Q9 |
| 8 | b | b | réserve | orthocentre ni enseigné ni rappelé ; clé = réunion de c et d |
| 9 | 3 | 3 cm | réserve | pas de figure pour une mise en équation dans un rectangle |

Figures (7) : toutes vraies (29 px/cm ; I à AI = 3, J à DJ = 5, (IJ) ⊥ (BD) en O, K à AK = 6) ; aucune ne code ce qui
est à démontrer. Elles placent I à sa position de solution (AI = 3/8 de AB), y compris en Q4–Q5 où x est une
inconnue : la clé de Q9 se lit à la règle (mineur, inhérent). Rendu Chromium : aucune formule brouillée ; les lignes
« IB = DJ », « ID = IB », « DI² = x² + 16 », « BI² = (8 − x)² », « (8 − x)² » sont des lignes-équations.

### Défauts — 34

**MAJEUR 34-Q7 → Q9 — fuite en avant (donnée redonnée).** Q7 (d2) écrit « والرباعي DIBJ معيّن حيث AI = 3 cm » ;
Q9 (d3, émise après) demande « احسب x » avec x = AI. Toute longueur donnée en Q7 (IB = 5, ID = 5…) livrerait x de même.
Correctif : Q7 redevient l'officiel 3b complet, en d3, placée APRÈS Q9 — énoncé « ABCD مستطيل مركزه O حيث AB = 8 cm و AD = 4 cm. المستقيم المارّ من O والعمودي على (BD) يقطع (AB) في النقطة I ويقطع (CD) في النقطة J، والرباعي DIBJ معيّن.\nاحسب محيط المعيّن DIBJ بالصنتمتر، ثمّ اكتب قيمته. »,
explication ouverte par « DI = BI، و DI² = x² + 16 و BI² = (8 − x)² مع x = AI، ومنه 16x = 48 أي x = 3 cm، فـ IB = 8 − 3 = 5 cm … ».
(Coïncidence officielle aire = périmètre = 20 : le format `numeric` ne peut pas distinguer l'élève qui calcule l'aire
5 × 4 ; à accepter, c'est la donnée du sujet.)

**MAJEUR 34-Q2 — plan 2×2 incomplet : le vote terme à terme désigne la clé.** a = (B→D par « O منتصف » ✓, I→J par « على
مستقيم مارّ من O » ✗), b = (I→J par « يحوّل (AB) إلى (CD) » ✓, B→D par « على استقامة واحدة » ✗), d = (✓, ✓) ; c parle d'autre
chose (« قطعتان على ضلعين متقابلين »). Chaque justification juste figure donc deux fois (a + d, b + d) et chaque fausse
une seule : le vote reconstruit d. Correctif — c devient la cellule ✗✗ du même patron (muette, 161 signes ; clé 157,
b 171) : « التناظر المركزي الذي مركزه O يحوّل B إلى D لأنّ B و D و O على استقامة واحدة، ونظيرة I هي J لأنّ I و J على مستقيم واحد مارّ من O، فنظيرة [IB] هي [JD]، إذن IB = DJ » ;
et dans l'explication remplacer « أو التعليل بتقايس الضلعين AB و CD اللذين يخصّان الضلعين كاملين لا جزأيهما » par
« أو الجمع بين التعليلين الناقصين ».

**MAJEUR 34-Q8 — orthocentre ni enseigné ni rappelé** (même constat que 32-Q10/Q11 ; la clé b conclut « أي هي المركز
القائم للمثلّث » et suppose le concours des hauteurs). Ici le rappel ne livre pas la clé (c et d s'appuient aussi sur
des hauteurs) : ajouter à l'énoncé, avant la question, « نذكّر بأنّ ارتفاعات أيّ مثلّث تلتقي في نقطة واحدة، تُسمّى المركز القائم للمثلّث. ».
Forme : b = réunion de c (KI hauteur) et d (BA hauteur), seule à deux hauteurs (synthèse) ; a (diagonales du losange
confondues avec (DI) et (BK)) a pour étiquette `segment-mal-choisi`, acceptable.

**MAJEUR 34-Q9 — question spatiale sans figure.** Rectangle, point I de [AB], triangle DIB isocèle : l'élève doit
reconstruire la figure (au donjon, la question arrive seule). Ajouter la figure de Q4 (rectangle et I sur [AB]), I
placé à une abscisse quelconque et non à x = 3 (sinon la clé se lit).

**MINEUR 34 — prémisses redonnées (donjon).** Q6 donne « DI² = x² + 16 » et « BI² = (8 − x)² » (clés de Q5 et Q4) ;
Q7 « DIBJ معيّن » (clé de Q3) ; Q6 expose aussi toute la marche de Q9 (« لحلّ المعادلة DI² = BI² ننشر أوّلًا BI² »), ce qui
rend Q9 très court en route quête — Q9 reste un vrai d3 seule.

**MINEUR 34-Q1** — c (clé) réunit a et b ; b et d portent cependant deux prémisses chacune : indice faible. Pour aligner
sur la synthèse : a → « (OI) ⊥ (BD) والنقطة I من هذا المستقيم ومن الضلع [AB]، فهي تبعد عن D وعن B المسافة نفسها، إذن ID = IB ».

Étage 34 : **boss d3 (120/30)** — 2 questions d3 sur 9 (Q8 hauteurs, Q9 équation) ; Q1–Q7 sont des d2 directs (et Q6,
développement d'une identité, est un d1–d2). Avec Q7 corrigée (d3), 3 d3 sur 9 : profil boss, comme les examens
publiés 25 et 09/35. L'en-tête challenge d4 n'est pas honnête.

Bilan 34 : 9 questions, 0 clé fausse, 4 majeurs (Q7 → Q9 ; Q2 ; Q8 ; Q9 figure), 2 mineurs ; étage à baisser.

---

## 35 — 2011 générale ex.5 · d4 challenge 300/60 · displayOrder 35 · 11 questions

Titre : « 🏛️ مناظرة 2011 · التمرين 5 ⭐⭐⭐⭐: مثلّث قائم وارتفاعه — فيثاغورس والعلاقات القياسية وطاليس وإثبات طبيعة رباعي » —
conforme, aucune clé. Données fidèles à 2011-generale.md (BC = 5, AC = 3, AB = 4, I et J milieux, H pied de la
hauteur, E = (AC) ∩ (IH), K sur (IJ) et la parallèle à (BC) par A). Rampe 1,2,2,2,2,2,2,3,3,3,3.
**Sous-questions officielles (12 annoncées → 11)** : 1b, 2a (AH puis CH), 2b, 3a, 3b, 4-aire sont là, plus trois
maillons déclarés (IJ, AJ, HJ). **Disparue : « بيّن أنّ الرباعي AKBJ معيّن »** — la `multi` Q10 en donne des
ingrédients (I milieu de [KJ], (KJ) ⊥ (AB), AK = BJ) mais ne demande jamais la nature, et Q11 la pose en donnée.

| Q | ma réponse (aveugle) | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | c | c | OK | trois égalités fausses aux étiquettes exactes, options de même longueur |
| 2 | 2,4 | 2.4 cm | OK | AH × BC = AB × AC (cours ch.09) |
| 3 | 1,8 | a | réserve | explication et distracteur 2,25 bâtis sur AC² = CH × CB, relation non enseignée |
| 4 | 2 | d | réserve | « 1,8 » (= CH) étiqueté `reponse-a-l-autre-inconnue` : valeur de remplissage |
| 5 | 1,5 | d | OK | 2, 3, 2,5 : erreurs exactes de leurs étiquettes |
| 6 | 2,5 | a | OK | 5 et 2,4 étiquetés exacts ; 2 (AB/2) muet |
| 7 | 36/7 | b | **ERREUR de construction** | la donnée « HJ = 0,7 cm » (d2, émise avant) est la clé de Q9 |
| 8 | b | b | OK | vrai plan 2×2 (parallélisme × configuration), ✗✗ muet |
| 9 | 0,7 | c | réserve | explication par AB² = BH × BC, non enseignée |
| 10 | {a,c,e,f} | {a,c,e,f} | réserve | jugé un à un : I milieu de [KJ] ✓, KJ = AB ✗ (3 ≠ 4), (KJ) ⊥ (AB) ✓, AKBJ rectangle ✗, AK = BJ ✓, JA = JB ✓ ; 4 vrais sur 6 comme les trois autres `multi` |
| 11 | 6 | c | OK | 10 et 12 étiquetés exacts ; coïncidence officielle aire(AKBJ) = aire(ABC) = 6 |

Figures (11) : toutes vraies (47,2 px/cm ; angle droit en A ; H à BH = 3,2, ordre B, J, H, C ; E sur (AC) au-delà de C,
HE = 36/7 ; K = 2I − J). L'angle droit en A n'apparaît pas en Q1 (à démontrer). Rendu Chromium : aucune formule
brouillée ; « HE/HI = HC/HJ » est une ligne-équation.

### Défauts — 35

**MAJEUR 35-Q7 → Q9 — fuite en avant (donnée redonnée).** Q7 (d2) donne « HI = 2 cm و HC = 1,8 cm و HJ = 0,7 cm » ;
HI et HC sont des clés de Q4 et Q3 émises AVANT (sans effet en quête), mais **HJ = 0,7 est la clé de Q9 (d3), émise
APRÈS**. Correctif : Q7 (officiel 3b) passe en d3, placée après Q9, sans HJ — énoncé « ABC مثلّث قائم الزاوية في A حيث AB = 4 cm و AC = 3 cm و BC = 5 cm. النقطتان I و J منتصفا [AB] و [BC]، والنقطة H المسقط العمودي للنقطة A على (BC)، و E نقطة تقاطع (AC) و (IH). نعلم أنّ HI = 2 cm و HC = 1,8 cm، وأنّ:\nHE/HI = HC/HJ\nما طول [HE] بالصنتمتر ؟ »
(options inchangées) ; explication ouverte par « BH = BC − HC = 3,2 cm و BJ = 2,5 cm، و J بين B و H، فـ HJ = 0,7 cm؛ … ».

**MAJEUR 35-Q3 — relation non enseignée dans l'explication et dans un distracteur.** L'explication calcule
« AC² = CH × CB، أي CH = AC²/BC » ; le cours ch.09 n'enseigne que AH × BC = AB × AC et AH² = BH × CH (et dit
lui-même : « la première donne AH, puis la seconde ou Pythagore les segments »). Le distracteur 2,25 = AC²/AB n'existe
que par cette relation mal appliquée. Correctif sur la voie enseignée — options « 0,6 » (`pythagore-sans-carres` :
3 − 2,4), « 1,8 » (clé), « 3,2 » (`segment-mal-choisi` : BH), « 3,24 » (`pythagore-racine-oubliee` : CH²) ; explication
« AH × BC = AB × AC فـ AH = 12/5 = 2,4 cm. والمثلّث AHC قائم في H ووتره [AC]: CH² = AC² − AH² = 9 − 5,76 = 3,24، إذن CH = 1,8 cm ✓. الخطأ الشائع: طرح الطولين 3 − 2,4 = 0,6؛ أو التوقّف عند CH² = 3,24؛ أو أخذ [BH] = 3,2 بدل [CH]. »
(valeurs vérifiées en fractions : CH² = 81/25 ; clé 3 signes, non la plus longue.)

**MAJEUR 35-Q10 (et tranche) — nombre de bonnes réponses déductible.** Les quatre `multi` de la tranche (31-Q6,
31-Q11, 32-Q3, 35-Q10) ont toutes 6 énoncés dont exactement 4 vrais : l'élève qui a vu une `multi` sait combien
cocher dans les suivantes. Correctif ici, qui rend aussi la sous-question disparue : remplacer d « الرباعي AKBJ مستطيل »
(faux) par « الرباعي AKBJ معيّن » (vrai) → 5 vrais sur 6 ; et dans l'explication remplacer « فقطرا الرباعي غير متقايسين وليس
مستطيلًا » par « والقطران [AB] و [KJ] لهما المنتصف نفسه I ومتعامدان، فالرباعي AKBJ معيّن، وقطراه غير متقايسين ». (Avec le
correctif de 31-Q11 — 3 vrais sur 6 — la tranche aurait 4, 3, 4, 5 vrais.)

**MINEUR 35-Q9** — explication par « AB² = BH × BC » (non enseignée) : remplacer par « المثلّث AHB قائم في H: BH² = AB² − AH² = 16 − 5,76 = 10,24، إذن BH = 3,2 cm ».

**MINEUR 35-Q4** — « 1,8 » (= CH) porte `alg.reponse-a-l-autre-inconnue` ; aucun geste naturel ne mène de IH à CH
(l'explication dit « إعطاء طول آخر من الشكل ») : valeur de remplissage, à rendre muette.

**MINEUR 35 — coïncidences officielles.** Aire(AKBJ) = aire(ABC) = 6 : l'élève qui calcule l'aire du triangle trouve la
clé de Q11 ; inhérent aux données, à accepter. Options numériques non triées (Q3–Q7, Q9, Q11) : sans effet à
l'écran (mélange à l'affichage), simple tenue.

Étage 35 : **d4 limite, défendable** — 4 questions d3 sur 11 (Q8 papillon, Q9 ordre B, J, H, C, Q10 six propriétés,
Q11 aire) ; avec Q7 corrigée (d3), 5 sur 11 comme 29 et 30. En l'état, comparable à 04/28 publié (d4, 4 d3 sur 11).

Bilan 35 : 11 questions, 0 clé fausse, 3 majeurs (Q7 → Q9 ; Q3 ; Q10 / `multi`), 3 mineurs.

---

## Synthèse transversale

### 1. « Lequel de ces arguments » : la clé se reconnaît au nombre de conditions (MAJEUR, systémique)

Quand les deux distracteurs « à une condition manquante » ne portent QUE la moitié de la clé, la clé est la seule
option complète et la réunion exacte des deux autres : un élève qui « prend la réponse la plus complète » la trouve
sans la notion (quality-bar § No form clue, n° 2). Le vote terme à terme, lui, est bien neutralisé partout sauf 34-Q2.
- Nets (majeurs, correctifs donnés fichier par fichier) : 29-Q1, 30-Q3, 30-Q8, 31-Q4, 33-Q1, 33-Q4 ; vote terme à
  terme non neutralisé : 34-Q2 (cellule ✗✗ hors patron).
- Faibles (mineurs) : 29-Q4, 29-Q8, 30-Q6, 34-Q1, 34-Q8 (une autre option porte aussi deux conditions).
- Bien construits, à prendre pour modèle : 29-Q6, 30-Q9, 31-Q5, 31-Q7, 32-Q5, 32-Q8, 35-Q8 (chaque option a la même
  structure ; les cellules fausses sont des conditions FAUSSES, pas absentes).
Principe de correction appliqué partout : chaque distracteur à condition manquante reçoit une seconde prémisse VRAIE
et propre à lui (jamais la même dans trois options, sinon la clé devient l'intruse), sans donnée qui soit la clé
d'une autre question.

### 2. Fuites (prémisses redonnées)

**En avant — majeures** (l'étiquetage de difficulté inverse l'ordre officiel, et le résultat d'une étape est donné
AVANT la question qui le demande) : 31-Q8 → Q11 (« B منتصف [CK] »), 33-Q6 → Q7 (« OI = √3 »), 34-Q7 → Q9
(« AI = 3 »), 35-Q7 → Q9 (« HJ = 0,7 »). Règle pour l'auteur : une prémisse ne redonne un résultat que si la question
qui le calcule est émise avant elle (difficulté inférieure, ou égale et placée plus haut dans le fichier).
**Au donjon seulement** (ordre respecté en quête, mineures, pratique L15) : 29-Q11 → Q9 (60°), 30-Q3 → Q2, 30-Q12 → Q11,
31-Q10 → Q7, 32-Q7 → Q3, 32-Q9 → Q8, 34-Q6 → Q4/Q5, 34-Q7 → Q3, 35-Q7 → Q3/Q4.
Coche ✓ : vérifiée par script sur les 73 explications, elle suit toujours la valeur ou la conclusion-clé. Aucune décimale
de vérification ne livre un verdict. Aucun titre ne livre de clé.

### 3. Étiquettes (registre lu sur `origin/main`)

133 placements, 27 étiquettes distinctes, toutes au registre ; compétences toutes en 9ᵉ (aucune `vec.*` employée ;
`parallelogramme-sommets-mal-ordonnes` est bien la variante `math.geo.*`).
**`condition-suffisante-supposee` (libellé élargi « Tu prends une seule propriété pour une preuve : il faut toutes les
conditions »)** — 31 placements relus un à un : 29 sont des raisons vraies privées d'une condition (29-Q1 a b, Q4 b,
Q8 b d, Q11 b ; 30-Q3 a c, Q6 a, Q8 b c ; 31-Q4 a b, Q5 b d ; 32-Q5 b c, Q10 b ; 33-Q1 b c, Q4 a b, Q8 a ; 34-Q1 a b,
Q2 a b, Q8 c d) ; **2 ne le sont pas : 32-Q6 a et b** énoncent une affirmation vraie dans la figure (raisonnement valide
non justifié) — réécriture donnée.
**Inexactes ou à retirer** : 29-Q8 c (✗✗) ; 30-Q4 a, 33-Q5 a, 32-Q9 c et d (options ambiguës : deux gestes y mènent) ;
35-Q4 b (valeur de remplissage) ; 33-Q8 b (✗✗, remplacée) ; 35-Q3 c (2,25 n'existe que par une relation non enseignée,
remplacée). Toutes les autres nomment exactement l'erreur exécutée (vérifié option par option : 2√5, 3√5, 12, 48, 27,
45, 72, 16√3/3, 9√3/8, 7/9, 4√3 − 2, (3√3 + 3)/2, 31/10, √3, 6√3, 5,7, 3√3, 6, 12, 3, (8 + x)², x² − 16, x² + 64,
(x + 4)², 64 + x², 64 + 16x + x², 10, 12…).
Limites déclarées par l'auteur : « 3√2 » de 33-Q5 sous `segment-mal-choisi` — **exact** (« repère d'abord le bon
triangle ») ; « 64 + x² » de 34-Q6 sous `carre-somme-sans-double-produit` — **exact** (« d'une somme ou d'une différence »).
**Options muettes qui méritent une étiquette EXISTANTE** : 29-Q4 d et 31-Q3 c → `condition-suffisante-supposee` ;
30-Q2 b c et 32-Q4 d (angle droit au mauvais sommet) → `hypotenuse-mal-choisie` (c'est la pratique publiée : 09/09-Q4,
09/35-Q5, 18/19-Q1, 20/02-Q2) ; 32-Q1 a (OA) → `segment-mal-choisi` ; 32-Q7 d (la médiane entière) →
`alg.reponse-a-l-autre-inconnue`. Facultatif : 34-Q4 b et 34-Q6 b (« 64 − x² » : carré de la différence pris pour
la différence des carrés) → `math.alg.difference-carres-confondue` (« Tu confonds une différence de deux carrés avec
un carré ») — la lecture « deux erreurs, muette » de l'auteur se défend aussi.
**Familles muettes à ≥ 3 questions distinctes** :
- **Fonction trigonométrique mal choisie — 4 questions** : 33-Q7 (3/2 = sin 30°, 3√3/2 = cos 30° au lieu de tan 30°),
  et au ch.09 publié 09/03-Q6 (« 1/2 » = cos au lieu de tan, muette), 09/06-Q1 (« 5/12 » = tan au lieu de cos, posée
  sous `trigo-rapport-inverse`, inexact), 09/06-Q6 b (« المقابل/المجاور » = définition de tan donnée pour cos).
  Seuil atteint → étiquette NOUVELLE : id `math.geo.fonction-trigo-mal-choisie`, compétence `math.geo.trigonometrie` ;
  fr « Tu choisis le mauvais rapport : avec les côtés opposé et adjacent à l'angle, c'est la tangente ; le sinus et le
  cosinus font intervenir l'hypoténuse » ; en « You pick the wrong ratio: the sides opposite and adjacent to the angle
  call for the tangent; sine and cosine involve the hypotenuse » ; ar « تختار النسبة غير المناسبة: مع الضلعين المقابل
  والمجاور للزاوية نستعمل الظلّ، أمّا الجيب وجيب التمام فيستعملان الوتر ». À poser sur 33-Q7 a et c (et, hors tranche,
  sur les trois questions publiées).
- **Raisonnement circulaire « pur »** (hors réciproque mal employée, déjà couverte par `…-reciproque-role`) : 09/26-Q4
  et 32-Q11 a, soit 2 questions — **reste muette**. (32-Q6 c, que l'explication dit circulaire, ne l'est pas ; s'il était
  gardé tel quel, le seuil serait atteint et un libellé possible serait « Tu t'appuies sur ce qu'il faut démontrer : une
  preuve part des données, jamais de sa propre conclusion », sans compétence, comme `reponse-a-l-autre-inconnue`.)
- Mauvais sommet de l'angle droit : déjà couvert par `hypotenuse-mal-choisie` (ci-dessus). Options à deux erreurs et
  valeurs de remplissage : muettes par doctrine.

### 4. Programme (R-3) et ordre d'enseignement

Enseignés avant ch.18 (cours `origin/main`) : médiatrice et sa réciproque (ch.18, outil 3), droite des milieux et sa
réciproque (ch.18 outil 1, ch.08), médiane relative à l'hypoténuse et sa réciproque (ch.18 outil 2, qui donne aussi le
triangle inscrit dans un demi-cercle), centre de gravité aux 2/3 (ch.08), diagonales des parallélogramme, rectangle,
losange, carré (ch.18), Pythagore et réciproque (ch.09), Thalès, réciproque et papillon (ch.08), aire du losange par
les diagonales (ch.18), AH × BC = AB × AC et AH² = BH × CH (ch.09), **tan 30° = √3/3 (ch.09, tableau des valeurs
remarquables) : 33-Q7 conforme**. Symétrie centrale, isocèle, équilatéral, somme des angles : classes antérieures.
**Non enseignés et employés** : tangente ⊥ rayon (33-Q2, Q5) ; orthocentre / concours des hauteurs (32-Q10, Q11 ;
34-Q8) ; AC² = CH × CB et AB² = BH × BC (explications de 35-Q3, Q9, et distracteur 2,25). Aucun vecteur, aucune
translation, aucun « on admet », aucun « على الشكل التالي », aucun item hors programme.

### 5. Rendu arabe

Banc Chromium (`dir=rtl`, structure de `RichField`/`OptionContent`, découpage `splitMathRuns` d'`origin/main`) à 800 et
400 px, sur les 73 énoncés, 264 options et 73 explications ; témoin positif validé (« AM = 2/3 AB » détecté brouillé).
**Un seul défaut** : 33-Q7, explication « ظا 30° = OI/OB » affichée « OI/OB = °30 » — lacune du moteur
(`DIGIT_FIRST_FORMULA` n'accepte pas « ° » après le nombre ; même forme dans des missions publiées, 09/06) ; correctif
de texte donné. Pas de virgule arabe entre valeurs, pas de ligne-formule refusée par `isDisplayEquation`, pas de lettre
à apostrophe, pas d'équation « 3 − 2x = … ». Tous mes textes de remplacement passés au même banc : aucun brouillage.

### 6. Doublons

(a) Avec les missions publiées du ch.18 (01–28) : aucun ; aucune des sept sessions n'était déjà exploitée (les publiées
22–24 et 08/17, 09/19, 20/23 prennent d'autres exercices des mêmes années). (c) Avec les examens et devoirs publiés des
ch.03, 04, 08, 09, 12, 20 : aucun quasi-identique (le plus proche, 09/07-Q2, calcule AH dans un 18-24-30, autre format).
Mesures : `content:tranche` 0 paire ≥ 0,45 ; mon balayage par bigrammes, lettres et nombres neutralisés, ne trouve
rien d'autre que des énoncés-cadres répétés (autonomie des questions). (b) Entre les sept missions, **deux gabarits
répétés (mineur)** : 29-Q4 et 30-Q6 ont la clé et le piège principal mot pour mot (« X منتصف … و … = …/2، فبعكس خاصيّة
الموسّط المتعلّق بالوتر … » / « … موسّط … والمثلّث الذي يصل فيه موسّط رأسًا بمنتصف الضلع المقابل يكون قائمًا في ذلك الرأس »),
à lettres près — reformuler l'une (par exemple 30-Q6 par le cercle : « AB = AC = AD = 6 cm فالنقاط B و C و D على
الدائرة التي قطرها [CD]… ») ; 29-Q3 et 30-Q1 (hauteur de l'équilatéral par Pythagore, mêmes trois pièges), venus de
deux sessions : à accepter. Les quatre `multi` au même nombre de vrais (4/6) : voir 35-Q10.

### 7. Étages

| mission | d3 / total | verdict | en-tête honnête |
| --- | --- | --- | --- |
| 29 (2001) | 5 / 11 | d4 honnête | challenge d4 300/60 ✓ |
| 30 (2005) | 5 / 12 | d4 défendable | challenge d4 ✓ |
| 31 (2006) | 3 / 11 | trop peu de d3 | boss d3 120/30, titre ⭐⭐⭐ — ou d4 après le correctif de Q8 (4 / 11) |
| 32 (2008) | 6 / 11 | d4 honnête | challenge d4 ✓ |
| 33 (2009 G) | 2 / 8 (3 après Q6) | profil boss | **boss d3 120/30, titre ⭐⭐⭐** |
| 34 (2010 G) | 2 / 9 (3 après Q7) | profil boss | **boss d3 120/30, titre ⭐⭐⭐** |
| 35 (2011 G) | 4 / 11 (5 après Q7) | d4 limite | challenge d4 ✓ |

Rampes : non décroissantes dans les sept fichiers ; les déplacements proposés (31-Q8, 33-Q6, 34-Q7, 35-Q7 en d3, en fin
de fichier) les gardent non décroissantes. Aucune question d1–d2 n'est gonflée en d3 ; 33-Q3 est un d1 étiqueté d2
(sans effet d'ordre).

---

## Chiffre final

- **Questions auditées : 73** (29 : 11 · 30 : 12 · 31 : 11 · 32 : 11 · 33 : 8 · 34 : 9 · 35 : 11), toutes re-résolues à
  l'aveugle (dont 9 `numeric` et 4 `multi` jugées énoncé par énoncé).
- **Clés fausses : 0.** Aucune figure fausse (71 figures recalculées ; aucune ne porte de nombre, donc aucune valeur
  d'option n'y est écrite), aucune explication qui contredise sa clé.
- **Questions à reprendre pour un défaut majeur : 21** — 29-Q1 ; 30-Q3, Q8 ; 31-Q4, Q8 ; 32-Q6, Q10, Q11 ; 33-Q1, Q2,
  Q4, Q5, Q6, Q8 ; 34-Q2, Q7, Q8, Q9 ; 35-Q3, Q7, Q10.
- **Retouches mineures fermes : 21 autres questions** — 29-Q2, Q3, Q4, Q5, Q7, Q8, Q9, Q10 ; 30-Q2, Q4 ; 31-Q3, Q9, Q11 ;
  32-Q1, Q4, Q7, Q9 ; 33-Q7 ; 34-Q1 ; 35-Q4, Q9. Facultatives : 30-Q6, Q11 ; 32-Q8 ; 33-Q3 ; 34-Q4, Q6.
- **En-têtes à changer : 3** (31 sauf correctif de Q8, 33, 34 → boss d3 120/30, ⭐⭐⭐).
- **Étiquette nouvelle proposée : 1** (`math.geo.fonction-trigo-mal-choisie`). Remontée moteur : « ° » dans
  `DIGIT_FIRST_FORMULA`.
- Verdict : **à corriger avant publication** (fix-first) — aucune erreur de clé, mais quatre fuites en avant, trois
  notions employées sans être enseignées, et l'indice « nombre de conditions » sur six questions-arguments.
