# Audit L17 — maths 9e ch.18 quadrilatères, missions 36–41 (examens 2013–2020)

Auditeur indépendant. Rapport écrit au fil de l'eau. Valide pour l'arbre de travail de `wip/gisement-9eme-lots-en-ecriture` (HEAD `b5c5d033`, fichiers 36–41 tels que commités en `bbcb3640` et non modifiés depuis) et `origin/main` `9a3090c9` — ré-auditer si le contenu a bougé.

Périmètre : `/home/user/wt-gis` (branche `wip/gisement-9eme-lots-en-ecriture`), `content/math/18-quadrilateres/exercices/36` à `41`.
Registre lu sur `origin/main` (`git -C /home/user/yahia-quest-content`). Chaque clé re-résolue à l'aveugle (script `blind.py` qui masque
`correctOption`/`answerKey`/`explanation`), coordonnées refaites avant lecture de celles de l'auteur, puis comparaison.

## Mission 36 — 2013 générale ex.4 (12 q.)

Mes coordonnées : O(0,0), A(−3,0), B(3,0), C(0,3), D = 2C − A = (3,6), G = ((−3+3+3)/3 ; 6/3) = (1,2), E(3,3) ;
BD = 6 = 2·OC, AE = √45 = 3√5, AG = 2√5, GE = √5 ; OEDC (O+D = E+C), OECA (O+C = E+A), OBEC (O+E = B+C) parallélogrammes,
OBDC et ABEC trapèzes, OEBC croisé ; G centre de gravité de OEC : ((0+3+0)/3 ; (0+3+3)/3) = (1,2) ✓.
Figures : échelle 30,33 px/u, origine (150,216) : tous les points (A 59,216 ; B 241,216 ; C 150,125 ; D 241,34 ; G 180.33,155.33 ;
E 241,125 ; M 195.5,125) exacts ; codages (tirets sur [AO],[OB] ; doubles sur [BE],[ED] ; triples sur [AC],[CD]) justes ; angle droit
marqué en B seulement quand l'énoncé le donne (Q5, Q9), pas en Q8 (à démontrer) ✓.

| Q | d | ma réponse | clé | verdict | motif |
|---|---|---|---|---|---|
| 1 | 1 | a | a | OK | d (« (OC) موسّط عمودي لـ[AD] ») faux : (AD) de pente 1, (OC) verticale |
| 2 | 2 | a | a | OK | b, c : prémisses vraies, droite mal nommée ; d : règle fausse |
| 3 | 2 | {a,b,c,d} | {a,b,c,d} | réserve | b et c sont équivalents (E ∈ [BD] donné) : vrais ou faux ensemble |
| 4 | 2 | c (6) | c | réserve | étiquette de a inexacte ; BD se lit égal à AB = 6 sur la figure à l'échelle |
| 5 | 2 | b (3√5) | b | OK | 3√3 = √(36 − 9) hypoténuse ; 6√2 = AD ; 45 sans racine |
| 6 | 2 | b | b | OK | d est vraie mais n'apporte aucun milieu sur [EC] ; explication le dit |
| 7 | 2 | a | a | **réserve (fuite)** | l'énoncé pose « (EG) يحمل الموسّط الصادر من E » = clé de Q12 (d3, émise après) ; étiquette de c inexacte |
| 8 | 3 | c | c | OK | a : ⊥ + longueur (manque ∥) ; b : ∥ + longueur (manque ⊥) ; d : règle fausse (isocèle ⇒ droit) |
| 9 | 3 | d (2√5) | d | OK | √5 = AE/3, 3√5/2 = AE/2, 4 = (2/3)·6 |
| 10 | 3 | c | c | **réserve (forme)** | c = réunion de a (∥ seul) et b (= seul) : la clé se reconnaît par vote |
| 11 | 3 | {a,b,c} | {a,b,c} | **réserve (fuite)** | a (OEDC) est posé comme prémisse en Q6 et Q10, émises avant |
| 12 | 3 | d | d | OK | explication cite EO = 3√2, EC = 3 que l'énoncé (générique) ne donne pas — sans effet |

Défauts mission 36 :

- **MAJEUR 36-Q7 → Q12 — fuite en avant.** Q7 (d2) écrit « والمستقيم (EG) يحمل الموسّط الصادر من E فيه » : c'est mot pour mot la clé
  de Q12 (d3, « ماذا يمثّل المستقيم (EG) بالنسبة إلى المثلّث OEC ؟ » → موسّط), émise après. Toute reformulation de Q7 doit dire que G est
  sur le médian issu de E (c'est la prémisse de l'étape 3c), donc la fuite ne se corrige pas par le texte. Correctif : **déplacer Q7
  en fin de fichier et la passer en d3** (c'est l'étape 3c, la dernière de l'officiel ; elle utilise 3a et 3b). Rampe obtenue
  1,2,2,2,2,2,3,3,3,3,3,3 (non décroissante) ; Q7 est alors émise après Q12 : sa prémisse ne redonne plus qu'une clé antérieure
  (convention). Aucun texte à changer.
- **MAJEUR 36-Q11 — clé partiellement donnée avant.** Q6 (« OEDC متوازي أضلاع ») et Q10 (« لماذا الرباعي OEDC متوازي أضلاع ؟ »),
  émises avant Q11, posent l'option a comme vraie ; Q12, émise après, pose l'option b (« OECA متوازي أضلاع ») — dans le donjon les deux.
  Le « اختر كلّ » se réduit à juger 4 options. Correctif : options a « OBEC » ✓, b « OBDC », c « ABEC », d « OEBC », e « ADEO »,
  clé {a} ; vérifié : O+E = B+C (parallélogramme), O+D ≠ B+C, A+E ≠ B+C, OEBC croisé (diagonales [OB] et [EC] de milieux (1,5 ; 0) et (1,5 ; 3) ;
  [OE] et [BC] se coupent en (1,5 ; 1,5)), ADEO : (AD) ∥ (OE) et AD = 2·OE, trapèze. Explication à réduire en conséquence (garder la
  phrase OBEC, ajouter « ADEO : (OE) ∥ (AD) لكنّ OE = AD/2 فهو شبه منحرف »). Une seule bonne réponse sur cinq n'est pas déductible
  de la consigne « اختر كلّ ».
- **MAJEUR 36-Q10 — clé = réunion de deux distracteurs (vote terme à terme).** a ne donne que le parallélisme, b que l'égalité,
  c les deux : on la choisit sans géométrie. Correctif en plan 2×2 (chaque fait dans exactement deux options, toutes à 110 signes) :
  a « (OE) ∥ (DC) لأنّ O و E منتصفا [AB] و [BD]، و OC = ED لأنّ OC = BD/2 و E منتصف [BD]، فالرباعي OEDC متوازي أضلاع »
  (`condition-suffisante-supposee`) ;
  b « (EC) ∥ (AB) لأنّ E و C منتصفا [BD] و [AD]، و OE = DC لأنّ OE = AD/2 و C منتصف [AD]، فالرباعي OEDC متوازي أضلاع »
  (`condition-suffisante-supposee`) ;
  c (clé) « (OE) ∥ (DC) لأنّ O و E منتصفا [AB] و [BD]، و OE = DC لأنّ OE = AD/2 و C منتصف [AD]، فالرباعي OEDC متوازي أضلاع » ;
  d « (EC) ∥ (AB) لأنّ E و C منتصفا [BD] و [AD]، و OC = ED لأنّ OC = BD/2 و E منتصف [BD]، فالرباعي OEDC متوازي أضلاع » (muette,
  deux erreurs). Vérifié dans un triangle ABD quelconque (l'énoncé de Q10 est générique) : toutes les prémisses vraies ; a = un couple
  de côtés parallèles + l'autre couple égal (trapèze isocèle possible) ; b et d s'appuient sur [EC], diagonale de OEDC ; seule c
  donne deux côtés opposés parallèles ET égaux. Explication : remplacer la phrase des erreurs par « الخطأ الشائع: الجمع بين توازي
  ضلعين متقابلين وتقايس الضلعين الآخرين (وشبه المنحرف المتقايس الضلعين كذلك)، أو الاستناد إلى [EC] وهو قطر في OEDC لا ضلع ».
- **MINEUR 36-Q4 — lecture sur la figure (étiquette : facultatif).** a = 3 exécute « BD = OC » (oubli du facteur) ; la première
  phrase du libellé `droite-des-milieux-facteur-deux` (« vaut la MOITIÉ du troisième côté ») le couvre, la seconde décrit plutôt
  « BD = OC/2 » : garder, ou a → « 3/2 » si l'on veut l'exécution exacte de la seconde phrase. La figure dessine BD égal à AB (= 6 donné) : la clé se lit à l'œil. Correctif figure :
  aucune ne peut garder l'échelle sans tromper ; accepter (Q4 est d2) ou retirer la figure du tracé de [BD] (laisser A, B, D, O, C et
  [OC] seulement, sans le triangle) — je recommande d'accepter.
- **MINEUR 36-Q7 c — étiquette.** `segment-mal-choisi` ne décrit pas « transporter le centre de gravité d'un triangle à un autre » :
  rendre l'option muette.
- **MINEUR 36-Q3 — options b et c équivalentes** (E ∈ [BD] donné) : remplacer c par « BE = 2 × ED » (faux, muet) ; nombre de vrais
  devient 3/6.
- **MINEUR 36-Q12 — explication** : « EO = 3√2 cm و EC = 3 cm » ne vient pas de l'énoncé de Q12 (triangle ABD générique). Remplacer par
  « … لأنّ المثلّث OEC ليس متقايس الضلعين رأسه E في هذا الشكل » (ou ajouter AB = BD = 6 cm à l'énoncé).
- Prémisses redonnées (donjon, mineur, convention) : Q5 et Q9 posent BD = 6 cm (clé de Q4, émise avant) — accepté.
- Fidélité : toutes les sous-questions de l'officiel (1, 2a–c, 3a–c) sont présentes (2a en Q3, 2b en Q4+Q8, 2c en Q5+Q9, 3a en
  Q10+Q6, 3b en Q11+Q12, 3c en Q7) ; Q1 ajoutée (définition). Données fidèles (AB = 6, OC = 3). Étage d4 : 5 d3 / 12 → honnête.

**Verdict partiel 36** : 0 clé fausse ; 3 majeurs (Q7→Q12, Q10, Q11) + Q5/Q9 doublons du publié (§ 1) ; mineurs Q3, Q4, Q7c, Q12.

## Mission 37 — 2016 générale ex.4 (12 q.)

Mes coordonnées : A(0,0), B(6,0), C(8,0), I(3,0), O(4,0) ; médiatrice x = 3 ∩ 𝒞₁ : D(3,3) ; (AD) : y = x ∩ 𝒞₂ ((x−4)² + y² = 16) :
E(4,4) ; (BD) : y = 6 − x ∩ [OE] : F(4,2) ; G = (9/3 ; 3/3) = (3,1) ; N(2,0) ; H = projeté de G sur (DN) = (2,4 ; 1,2).
BD = 3√2, EC = EA = 4√2, OF = 2 = OE/2, DG = 2, NF = 2√2, FG = ED = √2, FG/NF = 1/2 ; EFGD : E + G = F + D = (7,5) ✓ ;
N, G, F sur y = x − 2 ✓ ; (DG) ⊥ (NB), (NG) ∥ (AD) ⊥ (DB) ⇒ G orthocentre de DNB ; B, G, H alignés (pente −1/3) ✓.
Figures : échelle 31 px/u, origine (26,157) : A, B, C, O, I, D (119,64), E (150,33), F (150,95), G (119,126), N (88,157),
H (100,4 ; 119,8) exacts ; angle droit marqué en D (Q2, Q5) et en E (Q3, Q4) quand l'énoncé le donne ✓.

| Q | d | ma réponse | clé | verdict | motif |
|---|---|---|---|---|---|
| 1 | 1 | c | c | OK | a incomplet, b angle droit en B, d équilatéral faux |
| 2 | 2 | b (3√2) | b | réserve | gabarit identique à Q4 (voir mineur) |
| 3 | 2 | a | a | réserve | clé par les angles de base de l'isocèle (notion de 7ᵉ, non enseignée en 9ᵉ) |
| 4 | 2 | b (4√2) | b | réserve | même calcul, mêmes trois pièges que Q2 |
| 5 | 2 | c (2) | c | OK | DI = AB/2 = 3 (médiane relative à l'hypoténuse, ch. 18) puis 2/3 |
| 6 | 3 | {a,b,c,d} | {a,b,c,d} | OK | e faux (OF = 2), f faux (milieu de [BD] = (4,5 ; 1,5)) |
| 7 | 3 | d | d | **réserve (forme + gabarit)** | d = réunion de a (∥ seul) et b (= seul) ; même gabarit que 36-Q10 |
| 8 | 3 | b (2√2) | b | OK | 2 = OA/2 (mauvais côté), 4 = OA, 4√2 = AE |
| 9 | 3 | a | a | OK | d suppose (NG) ∥ (AE), ce qu'il faut prouver (circulaire) |
| 10 | 3 | a (1/2) | a | OK | 7/2 somme, 3/2 = DA/NF, 1/4 = FG/EA |
| 11 | 3 | d | d | **réserve (notion)** | concours des hauteurs non enseigné et non rappelé dans l'énoncé |
| 12 | 3 | c | c | OK | énoncé glose « مركزه القائم أي نقطة تلاقي ارتفاعاته الثلاثة » ✓ |

Défauts mission 37 :

- **MAJEUR 37-Q7 — clé = réunion de deux distracteurs, et gabarit de 36-Q10.** a = parallélisme seul, b = égalité seule, d = les deux
  (+ c « قطران » comme 36-Q10 d). Correctif en plan 2×2 (chaque fait dans deux options exactement) :
  a « (EF) ∥ (DG) لأنّ كلًّا منهما عمودي على (AC)، و EF = FO = 2 cm لأنّ F منتصف [OE]، فالرباعي EFGD متوازي أضلاع »
  (`segment-mal-choisi` : l'égalité porte sur un autre segment que celui que demande la propriété) ;
  b « (EF) ⊥ (AC) لأنّ AEC متقايس الضلعين رأسه E و O منتصف [AC]، و EF = DG = 2 cm لأنّ F منتصف [OE] و G مركز ثقل المثلّث ABD،
  فالرباعي EFGD متوازي أضلاع » (`condition-suffisante-supposee` : une seule perpendiculaire, pas de parallélisme) ;
  c « (EF) ⊥ (AC) لأنّ AEC متقايس الضلعين رأسه E و O منتصف [AC]، و EF = FO = 2 cm لأنّ F منتصف [OE]، فالرباعي EFGD متوازي أضلاع »
  (muette, deux erreurs) ;
  d (clé) « (EF) ∥ (DG) لأنّ كلًّا منهما عمودي على (AC)، و EF = DG = 2 cm لأنّ F منتصف [OE] و G مركز ثقل المثلّث ABD، فالرباعي
  EFGD متوازي أضلاع ». Longueurs a 107 · b 146 · c 121 · d 132 : la clé n'est pas la plus longue. Prémisses vérifiées : EF = FO = 2,
  DG = 2, (OE) ⊥ (AC) et (DI) ⊥ (AB). Le gabarit diffère alors de celui de 36-Q10 (autres faits, autre piège).
- **MAJEUR 37-Q11 — notion non enseignée.** Aucun cours du manifeste (08, 09, 18…) n'énonce que les trois hauteurs d'un triangle
  sont concourantes ; la clé exige « G sur deux hauteurs ⇒ G est le point de concours des trois ». Les options glosent la définition,
  pas la propriété. Correctif (ajouter en tête de la question, neutre pour les quatre options) : « نذكّر أنّ موسّطات المثلّث تتلاقى
  في مركز ثقله، وأنّ موسّطاته العموديّة تتلاقى في مركز دائرته المحيطة، وأنّ ارتفاعاته تتلاقى في مركزه القائم. » Le rappel reprend
  a, b et d à égalité : il ne désigne pas la clé.
- **MINEUR 37-Q2/Q4 — gabarit répété dans la mission** : même calcul (triangle rectangle isocèle, hypoténuse donnée), mêmes
  pièges (moitié de l'hypoténuse, ×√2, carré non extrait) et même explication. Les deux viennent de l'officiel (1b, 2b) : à accepter,
  ou varier Q4 par la trigonométrie (ch. 09 : « جتا 45° = EC/8 ») avec un piège de fonction (`fonction-trigo-mal-choisie` n'aide pas
  ici, cos = sin) — je recommande d'accepter.
- **MINEUR 37-Q3 — prérequis de 7ᵉ** (angles à la base de l'isocèle, somme des angles) non enseignés en 9ᵉ mais universels ;
  l'explication les rappelle. Accepter. Étiquette de b : « tout triangle rectangle est isocèle » est une règle fausse plutôt qu'une
  condition insuffisante ; `condition-suffisante-supposee` reste défendable (l'angle droit seul ne suffit pas), garder.
- **MINEUR 37 — prémisses redonnées (donjon)** : Q10 « DA = 3√2، EA = 4√2، NF = 2√2 » redonne les clés de Q2 (DA = DB), Q4 (EA = EC)
  et Q8, toutes émises avant : convention, accepté. Q7 « F منتصف [OE] » = option d de Q6, émise avant : accepté.
- Fidélité : 1a → Q1, 1b → Q2, 2a → Q3 (la moitié « قائم » est donnée en prémisse : l'angle droit inscrit n'est plus demandé nulle part ;
  il est enseigné au ch. 18 et repris par 37-Q1 pour D — acceptable), 2b → Q4, 3 → Q6, 4 → Q7, 5a → Q9, 5b → Q10 (rapport 1/2 au lieu de
  « G منتصف [NF] » : déformation légère, le milieu reste la conclusion de l'explication), 6 → Q11 + Q12. Aucune sous-question perdue.
  Données fidèles (AB = 6, AC = 8). Étage d4 : 7 d3 / 12 → honnête.

**Verdict partiel 37** : 0 clé fausse ; 2 majeurs (Q7, Q11) + Q4 doublon du publié (§ 1) ; mineurs Q2/Q4, Q3, prémisses.

## Mission 38 — 2018 générale ex.4 (9 q.)

Mes coordonnées : A(0,0), B(6,0), I(3,0) ; C : x² + y² = 25 et x² − 6x + y² = 0 ⇒ C(25/6 ; 5√11/6) ; tangente x = 6 ∩ (AC) (y = (√11/5)x) :
D(6 ; 6√11/5) ; perpendiculaire à (AC) en D ∩ (AB) : E(216/25 ; 0) ; F(216/25 ; 6√11/5) ; O = milieu de [DE] = milieu de [BF] ;
H = projeté de B sur (AF) ≈ (4,950 ; 2,280) ; G = (A + B + F)/3 = (A + E + D)/3 (car B + F = D + E) ; K milieu de [AF] ; J milieu de [AD] ;
J, K, O sur y = 3√11/5.
BC = √11 ; CD = BC²/AC = 11/5 (AH² = BH × CH, enseignée ch. 09) ; BD = √(11 + 121/25) = √396/5 = 6√11/5 ; AD = 36/5 ; AJ = 18/5 = 3,6.
Aucune clé n'exige AB² = AC × AD ni AB² = BH × BC ✓ (36/5 n'apparaît qu'en distracteur, obtenu par BC² ↔ AB² dans la relation
enseignée).
Figures : échelle 25,93 px/u, origine (24 ; 137,7) : C (132,02 ; 66,05), D (179,56 ; 34,52), E (248 ; 137,7), F (248 ; 34,52),
O (213,78 ; 86,11), H (152,33 ; 78,59), G (150,52 ; 103,31), K (136 ; 86,11), J (101,78 ; 86,11), rayons 77,78 et 61,91 : tout exact.
Angle droit marqué en B (Q2, donné) et en C (Q3, donné), aucun en Q4 (à prouver) ; Q5 ne trace pas [AF] (l'alignement n'est pas
dessiné) ✓.

| Q | d | ma réponse | clé | verdict | motif |
|---|---|---|---|---|---|
| 1 | 1 | b (√11) | b | OK | 1 = 6 − 5, √61 somme, 11 sans racine |
| 2 | 2 | c (11/5) | c | OK | 36/5 (AB² au lieu de BC²), 6 (somme), 11/6 (AB au lieu de AC) — étiquettes exactes |
| 3 | 2 | b (6√11/5) | b | OK | √154/5 différence, somme des longueurs, 396/25 |
| 4 | 3 | a | a | réserve | « رباعي له ثلاث زوايا قائمة فهو مستطيل » : le cours 18 enseigne « متوازي أضلاع + زاوية قائمة » ; prérequis de 7ᵉ |
| 5 | 3 | d | d | OK | identification cercle [DE] = cercle [BF] exigée (enseignée : diagonales du rectangle) ; a utilise DHE |
| 6 | 3 | a | a | OK | b hauteurs, c un seul médian, d « ثلثه » faux |
| 7 | 3 | d | d | réserve | réciproque « point aux 2/3 d'un médian ⇒ centre de gravité » non énoncée au ch. 08 (dite dans l'explication) ; étiquette de a |
| 8 | 3 | 3,6 cm | 3,6 cm | OK | numeric, tolérance 0 adaptée (valeur décimale exacte) ; prémisse CD = 11/5 = clé de Q2 émise avant (convention) |
| 9 | 3 | a | a | OK | c applique la droite des milieux dans le mauvais triangle (O n'est pas sur un côté de ADF) |

Défauts mission 38 :

- **MINEUR 38-Q4 — règle non enseignée sous cette forme.** Le cours 18 (§ « من متوازي الأضلاع إلى المستطيل ») ne prouve le rectangle
  qu'à partir d'un parallélogramme. « Trois angles droits ⇒ rectangle » est un prérequis de 7ᵉ (somme des angles 360°). Correctif
  minimal (option a, clé) : « … وكلّ رباعي له ثلاث زوايا قائمة فزاويته الرابعة قائمة أيضًا (مجموع زوايا الرباعي 360°)، فهو مستطيل »
  — ⚠️ elle deviendrait la plus longue (≈ 135 > b 108) : préférer ajouter la phrase dans l'explication seulement et laisser l'option.
- **MINEUR 38-Q7 — réciproque implicite.** Ajouter à l'explication : « ومركز ثقل AED يقع هو أيضًا على [AO] عند ثلثيه انطلاقًا من A،
  ولا توجد على [AO] إلّا نقطة واحدة بهذه الصفة، فهما منطبقتان » (rien à changer dans les options). Étiquette de a
  (`segment-mal-choisi` pour « نقل مركز الثقل لاشتراك المثلّثين في رأس ») : inexacte, rendre muette (même famille que 36-Q7 c).
- **MINEUR 38-Q5 — forme** : la clé d est la seule qui ne répète pas la conclusion (« … على استقامة واحدة ») ; indice faible.
  Correctif facultatif : terminer d par « ، فالمستقيمان (HA) و (HF) منطبقان » (d passe à ≈ 150 signes, plus longue que a 126 :
  ⚠️ dans ce cas raccourcir aussi d en « AHB قائمة لأنّ H من الدائرة التي قطرها [AB]، و BHF قائمة لأنّ H من الدائرة التي قطرها [BF]،
  فـ (HA) و (HF) منطبقان » — 114 signes, vérifié). Je recommande ce texte.
- Fidélité : 1 → Q1, 2a → Q2, 2b → Q3, 3a → Q4, 3b → Q5, 4a → Q6, 4b → Q7, 4c → Q9 ; Q8 (AJ) ajoutée. Données fidèles (AB = 6,
  AC = 5) ; adaptation « المماسّ … وهو عمودي على (AB) » sans perte. Étage d4 : 6 d3 / 9 → honnête.

**Verdict partiel 38** : 0 clé fausse ; 0 majeur ; mineurs Q4, Q5, Q7, Q9 b (gabarit de 37-Q9, § 1).

## Mission 39 — 2019 générale ex.3 (10 q.)

Mes calculs : E(5) = 25 − 32 + 16 = 9 ; (x − 16/5)² + 144/25 = x² − (32/5)x + 400/25 ✓ ; A(0,0), B(4,0), C(0,3), BC = 5 ; M ∈ [BC], BM = a :
M = (4 − 4a/5 ; 3a/5) ; HM = 3a/5 ; BH = 4a/5 ; KM = AH = 4 − 4a/5 = (4/5)(5 − a) ; CK = (3/5)(5 − a) ;
HK² = AM² = 9a²/25 + 16(5 − a)²/25 = a² − (32/5)a + 16 = (a − 16/5)² + (12/5)² ≥ 144/25 ⇒ AM ≥ 12/5, égalité pour a = 16/5 = 3,2.
Distracteurs recalculés : 25 + 16(25 + a²)/25 → a² + 16 (sans double produit) ✓ ; 16(25 − a²)/25 → 16 − (7/25)a² ✓ ; HM² − KM² =
−(7/25)a² + (32/5)a − 16 ✓.
Figures : échelle 62 px/u, A (26,218) : M (174,8 ; 143,6) = (2,4 ; 1,2) ∈ [BC] (2,4/4 + 1,2/3 = 1) ✓, soit a = 2 : la figure n'est PAS
dessinée à la position de la solution (a = 3,2 serait le pied de la hauteur) ✓ ; angles droits marqués en A, H, K, M (donnés).
Adaptation « K projeté orthogonal de M sur (AC) » au lieu du cercle tangent : fidèle à la figure officielle, n'enlève aucune sous-question.

| Q | d | ma réponse | clé | verdict | motif |
|---|---|---|---|---|---|
| 1 | 1 | 9 | 9 | OK | numeric sans unité ✓ |
| 2 | 1 | b (5) | b | réserve | 3-4-5 et les trois pièges standard : gabarit le plus usé du corpus (voir doublons) |
| 3 | 2 | d | d | OK | trois étiquettes d'identités exactes |
| 4 | 2 | a (3a/5) | a | OK | 5a/3 inverse, 4a/5 = BH, a − 2 différences |
| 5 | 2 | {b,c,f} | {b,c,f} | OK | a (losange), d (carré), e (somme > hypoténuse) faux pour M quelconque ; 3/6 |
| 6 | 2 | d | d | **ERREUR de construction** | a « HM² = 144/25 » et b « HM = 12/5 » sont équivalentes : elles s'éliminent ensemble ; grille 2×2 non tenue |
| 7 | 3 | c | c | OK | (3/5)(5 − a) = CK, 4 − a, 3a/5 = HM (`reponse-a-l-autre-inconnue` exact) |
| 8 | 3 | a | a | **réserve (fuite)** | la clé « a² − (32/5)a + 16 » est l'expression E de Q1/Q3 (émises avant) : reconnue sans calcul |
| 9 | 3 | c | c | OK | a inégalité inversée (muette), b terme variable oublié, d racine distribuée ✓ |
| 10 | 3 | 3,2 cm | 3,2 cm | OK | AM = HK requis ; tolérance 0 adaptée |

Défauts mission 39 :

- **MAJEUR 39-Q6 — deux distracteurs équivalents.** HM ≥ 0, donc « HM² = 144/25 » ⟺ « HM = 12/5 » : l'élève écarte les deux d'un coup
  (une seule clé), il reste c/d, choix binaire « au carré ou non ». La grille annoncée n'est pas 2×2 (« ² » dans a, c, d ; « 12/5 » sans
  carré dans b seulement). Correctif en vrai 2×2 {HM, HK} × {« ² = 144/25 », « = 144/25 »} :
  a « HM² = 144/25 » (`segment-mal-choisi`) ; b « HM = 144/25 » (muette, deux erreurs) ; c « HK = 144/25 »
  (`math.num.racine-et-carre-confondus` : « Tu confonds la racine carrée et le carré », libellé exact pour HK pris pour HK²) ;
  d (clé) « HK² = 144/25 ». Vérifié : chaque trait deux fois ; aucune paire équivalente (HM = 5,76 ≠ HM² = 5,76) ; toutes fausses
  (HM < AM = 2,4 car AHM rectangle en H ; HK = 2,4) ; longueurs 12/11/10/12 : la clé n'est pas strictement la plus longue.
  Explication : « … الخطأ الشائع: اعتبار [AM] ضلعًا فنكتب HM² = 144/25 (والضلع أقصر دائمًا من القطر)، أو الخلط بين الطول ومربّعه
  فنكتب HK = 144/25 ». Le recoupement avec Q5 b (« AM = HK ») reste : Q6 devient le pas « et au carré », acceptable en d2.
- **MAJEUR 39-Q8 — clé reconnue par sa forme (fuite en avant).** Q1 (d1) et Q3 (d2) affichent « x² − (32/5)x + 16 » ; l'option a de Q8
  est la même écriture en a : l'élève la choisit sans Pythagore. Correctif (Q8 demande l'étape de Pythagore, l'identité étant déjà
  testée en Q3) : énoncé inchangé ; options a (clé) « (9/25)a² + (16/25)(5 − a)² », b « (3/5)a + (4/5)(5 − a) »
  (`math.geo.pythagore-sans-carres`), c « (16/25)(5 − a)² − (9/25)a² » (`math.geo.hypotenuse-mal-choisie`), d « (9/25)a² + (4/5)(5 − a)² »
  (muette : coefficient non élevé au carré). Vérifié : HM² = 9a²/25, KM² = 16(5 − a)²/25 ; longueurs 26/21/26/24 (la clé n'est pas
  strictement la plus longue) ; aucune de ces écritures n'apparaît dans un autre énoncé. Explication : garder le calcul jusqu'à
  « HK² = (9/25)a² + (16/25)(5 − a)² ✓ » et déplacer le développement en remarque (« وبالنشر نجد العبارة E نفسها »). Les étiquettes
  `carre-somme-sans-double-produit` et `carre-difference-ecrit-difference-carres` restent portées par Q3.
- **MINEUR 39-Q9 a — étiquette existante disponible** : « AM ≤ 12/5 » inverse le sens en ajoutant (12/5)² aux deux membres de
  (a − 16/5)² ≥ 0 : `math.num.ordre-inverse-a-tort` (« Tu inverses le sens de l'inégalité sans raison : ajouter ou soustraire le même
  nombre aux deux membres ne le change jamais ») le nomme exactement ; compétence `math.num.ordre-encadrement` (ch. 17, au manifeste).
- Prémisses redonnées (donjon, convention) : Q8 redonne HM et KM (clés de Q4, Q7, émises avant) ; Q10 redonne HK² (clé de Q8 sous forme
  canonique) : accepté. Q9 ajoutée : elle ne livre pas a = 16/5 (son explication ne le nomme pas) ✓.
- Fidélité : 1 → Q1, 2 → Q3 (seul le carré est demandé ; la fin « + (12/5)² = 16 » est dans l'explication — perte légère acceptable),
  3a → Q2, 3b → Q4, 4a → Q7, 4b → Q8, 4c → Q10 ; Q5, Q6, Q9 ajoutées. Données fidèles (AB = 4, AC = 3, a ∈ ]0 ; 5[). Étage d4 :
  4 d3 / 10, dont Q8–Q10 réellement difficiles → d4 défendable ; Q2 (d1) et Q6 (d2) tirent la mission vers le bas.

**Verdict partiel 39** : 0 clé fausse ; 2 majeurs (Q6, Q8) ; mineurs Q2 (doublon publié : voir § doublons, majeur), Q9a.

## Mission 40 — 2019 générale ex.4 (10 q.)

Mes calculs : K = ((−4 + 2)/2 ; 0) = (−1 ; 0) ; OB = 4, OC = 2, BC = 6 ; OA² = 12 − 4 = 8, A(0 ; 2√2) ; AB = √(16 + 8) = 2√6 ;
P(0 ; √2), E = 2P − C = (−2 ; 2√2) ; OCAE : O + A = C + E ✓ ; H(−2 ; 0) ; milieux de [OE] et [AH] : (−1 ; √2), OE = AH = √12 = 2√3 ⇒
rectangle ; KA = √(1 + 8) = 3 ; KE = √(1 + 8) = 3 = KB ⇒ E ∈ 𝒞.
Distracteurs : (−2 ; 0) somme sans moitié, (3 ; 0) demi-différence (et aussi « |−4| pris pour −4 »), (6 ; 0) différence entière ✓ ;
4 = √(12 + 4), 2√3 − 2 ✓ ; (0 ; 4) = 8/2 ✓ ; 2√2 = √(16 − 8), 6√2 facteur inversé ✓ ; (2 ; 2√2) = sommet opposé à O
(parallélogramme OCEA), (1 ; √2/2) milieu de [CP], (4 ; −√2) = symétrique de P par rapport à C ✓.
Figures : repères orientés (flèches), unités recalculées (37,8 ; 43,33 ; 40 ; 40,26 ; 38,73 px) : A à 2,83 u, E(−2 ; 2,83), P(0 ; 1,41),
K(−1 ; 0), cercle de rayon 3 : exacts. Q7 ne place pas E ✓.

| Q | d | ma réponse | clé | verdict | motif |
|---|---|---|---|---|---|
| 1 | 1 | b (−1 ; 0) | b | réserve | figure graduée : le milieu se lit en comptant les carreaux ; c et d hors de [BC] (s'écartent à vue) |
| 2 | 2 | {a,d,f} | {a,d,f} | OK | b et e (abscisse prise pour longueur) muettes ; c faux (2 ≠ 6) |
| 3 | 2 | c (2√2) | c | réserve | A placé à l'échelle d'une unité visible : 2√2 ≈ 2,8 s'estime contre 8, 4, 1,46 |
| 4 | 2 | a | a | réserve | « OA² = 8 » redonne le résultat de Q3 ; question d'une seule étape (racine), d1 réel |
| 5 | 2 | d (2√6) | d | OK | étiquettes exactes |
| 6 | 3 | b | b | OK | c nomme [OC] et [AE] « قطرين » ; a, d insuffisants |
| 7 | 3 | c (−2 ; 2√2) | c | OK | d (rôles inversés) muette |
| 8 | 3 | a | a | OK | b (milieux + côtés : parallélogramme seulement), c (un angle droit), d (périmètre) ; a 114 < b 117 |
| 9 | 3 | 3 cm | 3 cm | OK | numeric exact |
| 10 | 3 | d | d | **réserve (forme)** | d strictement la plus longue (118) et seule à calculer KE |

Défauts mission 40 :

- **MAJEUR 40-Q10 — clé strictement la plus longue** (mesure officielle confirmée : 118 contre 116/108/103). Correctif (option d) :
  « نصف القطر KB = 3، والمثلّث KHE قائم في H حيث KH = 1 وHE = 2√2، فـ KE² = 9، أي KE = KB، إذن E على الدائرة » (104 signes ; b reste
  la plus longue à 116). Vérifié : KH = |−1 − (−2)| = 1, HE = 2√2, KE² = 1 + 8 = 9 ; la phrase commence par un mot arabe (pas
  d'isolat d'ouverture). L'explication garde le détail 1 + 8.
- **MINEUR 40-Q1 — lecture sur la figure + options hors segment.** La grille graduée de −4 à 3 donne (−1 ; 0) au compte des carreaux, et
  (3 ; 0), (6 ; 0) sont hors de [BC]. Q1 est d1 et reprend la figure officielle : accepter, ou ne garder que les graduations −4, 0, 2
  (retirer les étiquettes −3, −2, −1, 1, 3 et leurs traits) — je recommande de retirer ces étiquettes.
- **MINEUR 40-Q3/Q4 — lecture à l'échelle** : OJ = 1 est visible et A est placé à 2√2 ; 2√2 se distingue à l'œil de 4 et 8. Accepter
  (aucune graduation sur [OJ)) ou étirer légèrement [OA] (non : une figure fausse serait pire) → accepter.
- **MINEUR 40-Q10 — prémisse « K(−1 ; 0) »** redonne la clé de Q1 (émise avant) : convention, accepté.
- Familles muettes : « abscisse négative prise pour une longueur » (Q2 b « OB = −4 », Q2 e « BC = −2 », et (3 ; 0) en Q1 selon
  l'explication) ; « symétrique aux rôles inversés » (Q7 d) — voir § étiquettes.
- Programme : milieu, distance, symétrique (« في المعلّم », ch. 12) et rectangle par les coordonnées (ch. 18 § « في المعلّم ») ✓ ;
  aucun vecteur ni translation dans les questions ni les explications ✓ (`math.vec.*` ne sont que des ids de compétence du registre).
- Fidélité : 1a → Q1, 1b → Q2, 2a → Q3 + Q4, 2b → Q5, 3a → Q6, 3b → Q7, 4a → Q8, 4b → Q9 + Q10. Données fidèles (B, C, K, AC = 2√3).
  Étage d4 : 5 d3 / 10 → d4 défendable (Q6, Q8, Q10 sont de vrais choix d'argument).

**Verdict partiel 40** : 0 clé fausse ; 1 majeur (Q10) ; mineurs Q1, Q3/Q4, Q10 (prémisse).

## Mission 41 — 2020 générale ex.5 (10 q.)

Mes calculs : A(0,0), B(8,0), C(8,4), D(0,4), O(4,2), I(6,4) ; BI = √20 = 2√5, AC = √80 = 4√5 ; H = (AC) ∩ (BI) = (6,4 ; 3,2) ;
papillon (CI) ∥ (AB) : HC/HA = HI/HB = CI/AB = 1/4 (partie/reste), HC/AC = 1/5 (partie/tout) ; HC = 4√5/5, HA = 16√5/5, HI = 2√5/5,
HB = 8√5/5 ; HC² + HB² = 16/5 + 64/5 = 16 = BC² ⇒ angle droit en H ; J(8,2), (OJ) : y = 2 ∥ (AB) ; K = (BI) ∩ (OJ) = (7,2), orthocentre
de OBC ; L = projeté de C sur (OB) = (6,4 ; 0,8) ; aire(OBC) = 4 × 4/2 = 8, OB = 2√5, CL = 16/(2√5) = 8√5/5, BL = √(16 − 64/5) =
4√5/5, aire(CLB) = 16/5 = 3,2 cm².
Figures : échelle 34,75 px/u (Q1–Q7), 36 (Q8), 37 (Q9), 32,5 (Q10) : H (248,4 ; 58,3), O (165,100), J (304,100), K (201,100),
L (179,8 ; 144,4), triangle CLB (CL = 3,578, LB = 1,789) exacts ; angle droit en H marqué seulement quand il est donné (Q8), pas en Q6 ;
(CK) en pointillés sans angle droit en Q8 ✓.

| Q | d | ma réponse | clé | verdict | motif |
|---|---|---|---|---|---|
| 1 | 1 | c (2√5) | c | réserve | même gabarit que Q2 (trio d'étiquettes Pythagore) |
| 2 | 1 | b (4√5) | b | réserve | idem |
| 3 | 2 | {a,c,f} | {a,c,f} | OK | b (CI/BC = 1/2), d (partie/tout 1/5), e (inverse) faux |
| 4 | 2 | a (4√5/5) | a | réserve | d = 16√5 = 4 × AC : deux erreurs (inverse + tout) sous une étiquette |
| 5 | 2 | d (8√5/5) | d | réserve | c = 8√5 = 4 × BI : deux erreurs ; b = HI (« autre grandeur ») ; gabarit de Q4 |
| 6 | 3 | b | b | OK | a circulaire, c triangle ABC, d sommet B ; b et d à 106 signes (égalité, pas d'indice) |
| 7 | 3 | d | d | **réserve (forme + prémisse fausse)** | d = c + « (AB) ⊥ (BC) » ; b pose « (AC) ⊥ (BC) », faux et visible |
| 8 | 3 | a | a | OK | rappel « نذكّر » neutre (porte sur a, c, d) ; b médianes, c circulaire, d règle fausse |
| 9 | 3 | c (8√5/5) | c | OK | 4 = OJ, 2√5 = OB, 4√5/5 = aire sans moitié ✓ |
| 10 | 3 | 3,2 cm² | 3,2 cm² | OK | numeric, unité cm² ✓ ; prémisse CL = clé de Q9 émise avant (convention) |

Défauts mission 41 :

- **MAJEUR 41-Q7 — la clé complète un distracteur, et b s'élimine à vue.** c = d moins « (AB) ⊥ (BC) » ; b affirme « (OJ) ∥ (AC) » et
  « (AC) ⊥ (BC) », deux faits faux que la figure dément (O est SUR (AC)). Correctif en plan 2×2, prémisses toutes vraies, préfixe
  commun « O منتصف [AC] و J منتصف [BC]، فبخاصيّة المنتصفين في المثلّث ABC يكون » puis :
  a « … OJ = AB/2 = 4 cm، و (AB) ∥ (DC)، إذن (OJ) ⊥ (BC) » (muette, deux erreurs) ;
  b « … OJ = AB/2 = 4 cm، و (AB) ⊥ (BC)، إذن (OJ) ⊥ (BC) » (`condition-suffisante-supposee` : une longueur ne donne pas une direction) ;
  c « … (OJ) ∥ (AB)، و (AB) ∥ (DC)، إذن (OJ) ⊥ (BC) » (`condition-suffisante-supposee`) ;
  d (clé, inchangée) « … (OJ) ∥ (AB)، و (AB) ⊥ (BC)، إذن (OJ) ⊥ (BC) ».
  Longueurs 116 / 116 / 111 / 111 : la clé n'est pas la plus longue ; chaque fait dans deux options. ⚠️ Ne pas utiliser « OB = OC »
  comme fait « inutile » : avec J milieu de [BC] il prouve (OJ) ⊥ (BC) (médiatrice) — l'option deviendrait juste.
- **MINEUR 41-Q4 d et Q5 c — option à deux erreurs étiquetée.** 16√5 = 4 × AC et 8√5 = 4 × BI cumulent l'inversion et la confusion
  partie/tout. L'inversion pure donne, en Q4, HC/HA = 4 ⇒ HC = 16√5/5 (= HA, option c) et, en Q5, HI/HB = 4 ⇒ HB = 2√5/5 (= HI, option b). Correctif :
  Q4 c → étiquette `math.geo.thales-rapport-inverse` (échanger HC et HA = inverser le rapport) ; Q4 d → muette ; Q5 b → étiquette
  `math.alg.reponse-a-l-autre-inconnue` (HI au lieu de HB, libellé exact) ; Q5 c → muette.
- **MINEUR 41-Q1/Q2 et Q4/Q5 — gabarits répétés dans la mission** (venus de l'officiel 1 et 2b) : accepter ; voir § doublons pour Q1/Q2.
- Programme : papillon (ch. 08 § « وضعية الفراشة ») ✓ ; réciproque de Pythagore ✓ ; aire par deux bases (ch. 09 § « المساحة نفسها
  مرّتين ») ✓ ; concours des hauteurs rappelé par « نذكّر » (Q8) ✓.
- Fidélité : 1 → Q1 + Q2, 2a → Q3, 2b → Q4 + Q5, 2c → Q6, 3 (préalable (OJ) ⊥ (BC)) → Q7, 3a → Q8, 3b → Q9 + Q10. Données fidèles
  (AB = 8, BC = 4, CI = 2). Étage d4 : 5 d3 / 10 → défendable (Q6–Q10 solides).

**Verdict partiel 41** : 0 clé fausse ; 1 majeur (Q7) + Q1 doublon du publié (§ 1) ; mineurs Q2, Q4/Q5 (étiquettes).

---

## Sections transverses

### 1. Doublons

Mesure : comparaison des 63 questions aux 1 452 questions publiées des chapitres 02, 03, 04, 08, 09, 12, 18, 20 (`origin/main`,
missions + quiz) — égalité des jeux d'options normalisés, Jaccard des options et des énoncés — puis lecture de chaque paire retenue.

(a)+(c) **Avec les missions publiées** :

- **MAJEUR 39-Q2 = 09/31-examen-2012-technique Q1** (et 12/06-defi-concours Q1) : mêmes quatre options {√7, 5, 7, 25}, même clé, mêmes
  trois étiquettes ; seul l'habillage change (3-4-5). Correctif : options « √7 » (`hypotenuse-mal-choisie`), « 5 » (clé), « 25/2 »
  (`math.num.racine-confondue-avec-moitie` : la moitié de 25 au lieu de sa racine), « 1 » (`pythagore-sans-carres` : 4 − 3).
  Vérifié : partage 2 options sur 4 avec chaque question publiée ; longueurs 2/1/4/1, la clé n'est pas la plus longue ; toutes fausses.
- **MAJEUR 41-Q1 = 20/10-devoir-cube Q2** : mêmes quatre options {2√3, 2√5, 6, 20}, même clé, mêmes étiquettes (côtés 4 et 2) ;
  et 18/15-devoir Q2 en partage trois. Correctif : options « 2√3 » (`hypotenuse-mal-choisie`), « 2√5 » (clé), « 10 »
  (`math.num.racine-confondue-avec-moitie` : 20/2), « 4 » (`segment-mal-choisi` : BC pris pour BI). Vérifié : 2 options partagées au
  plus ; longueurs 3/3/2/1 (pas de plus longue stricte) ; toutes fausses.
- **MAJEUR 37-Q4 ≈ 18/02-boss Q6** (même chapitre) : même configuration (point d'un demi-cercle de diamètre 8 sur la médiatrice du
  diamètre), même clé 4√2, trois options communes {4, 4√2, 8√2} ; et même gabarit que 37-Q2 (diamètre 6). Correctif (options
  seulement) : « 2√2 » (`segment-mal-choisi` : le rayon 4 pris pour l'hypoténuse), « 4√2 » (clé), « 8√2 » (`hypotenuse-mal-choisie`),
  « 32 » (`pythagore-racine-oubliee`). Vérifié : 2 options partagées avec 18/02 Q6 ; longueurs 3/3/3/2 ; toutes fausses.
- **MAJEUR 36-Q5 + Q9 ≈ 18/32-examen-2008 Q2 + Q7** (même chapitre) : même calcul (médiane de longueur √(6² + 3²) = 3√5, puis 2/3 →
  2√5), trois options communes sur quatre dans chaque paire (Q5 : {3√3, 3√5, 45} ; Q9 : {√5, 3√5/2, 2√5}), mêmes clés, mêmes
  pièges. Les deux sessions recyclent les données, mais les questions sont quasi identiques. Correctifs : 36-Q5 d « 45 » → « 5√3 »
  (`math.num.racine-extraction-facteur-inversee` : √45 = 3√5, pas 5√3 — libellé exact) ; 36-Q9 a « √5 » → « 30 »
  (`math.geo.pythagore-racine-oubliee` : (2/3) × 45). Vérifié : 2 options partagées au plus ; Q5 longueurs 3/3/3/3, Q9 longueurs
  2/5/1/3 (3√5/2 reste la plus longue) ; toutes fausses. Le trio « tiers inversé / milieu / autre segment » de 37-Q5 ne se répète plus
  à l'identique en 36-Q9.
- 36-Q4 partage ses quatre options {3, 3√2, 6, 6√2} avec 20/03-revision Q4, mais la clé diffère (6 contre 3√2) : pas un doublon.
- Aucune autre paire (Jaccard d'options ≥ 0,5 ou d'énoncés ≥ 0,55) n'est une question quasi identique : le reste est le préambule
  répété d'une même mission (autonomie des questions).

(b) **Entre les six missions** :

- Pythagore avec le trio `hypotenuse-mal-choisie` / `pythagore-sans-carres` / `pythagore-racine-oubliee` : 36-Q5, 37-Q2, 37-Q4,
  38-Q1, 38-Q3, 39-Q2, 40-Q3, 41-Q1, 41-Q2 (neuf questions). Les gabarits à varier sont 39-Q2, 41-Q1, 37-Q4 et 36-Q5 (correctifs
  ci-dessus) ; après eux le trio n'est plus complet que dans 37-Q2, 38-Q1, 38-Q3, 40-Q3 et 41-Q2 (valeurs et configurations
  différentes, venues de l'officiel) : à accepter.
- **Majeur (déjà compté)** : 36-Q10 et 37-Q7, même gabarit « لماذا … متوازي أضلاع » (∥ seul / = seul / les deux / « قطران ») — les plans
  2×2 proposés les différencient.
- **MINEUR 37-Q9 / 38-Q9** : même gabarit d'alignement (deux parallèles à une même droite par un point commun) avec les mêmes pièges
  (« … وهذا يكفي » et la règle fausse « المنتصفات … تقع دائمًا على استقامة واحدة »). Correctif : 38-Q9 b → « J و K منتصفا [AD] و [AF]
  و O منتصف [DE]، فالمستقيم (KO) يوازي (AD)، إذن J و K و O على استقامة واحدة » (`segment-mal-choisi` : la droite des milieux appliquée
  à [AF] et [DE], qui ne sont pas deux côtés d'un même triangle ; prémisses vraies, (KO) n'est pas parallèle à (AD) : K(4,32 ; 1,99),
  O(7,32 ; 1,99), (KO) horizontale). ⚠️ Vérifié : l'option affirme un parallélisme FAUX déduit d'une règle mal appliquée, sa
  conclusion n'en découle pas ; longueur 99, la clé a (104) n'est pas strictement la plus longue (c 109, d 109).
- 36-Q7 / 38-Q7 (« centre de gravité d'un second triangle ») : pièges voisins (transfert d'un triangle à l'autre, un seul médian),
  options différentes : à accepter.

### 2. Étiquettes

Libellés lus sur `origin/main`. Toutes les étiquettes posées existent. Corrections :

| question · option | étiquette actuelle | verdict | proposition |
|---|---|---|---|
| 36-Q7 c (transfert du centre de gravité) | `segment-mal-choisi` | inexacte | muette |
| 38-Q7 a (transfert « رأس مشترك ») | `segment-mal-choisi` | inexacte | muette |
| 41-Q4 d (16√5 = 4 × AC, deux erreurs) | `thales-rapport-inverse` | option à deux erreurs | muette ; porter `thales-rapport-inverse` sur 41-Q4 c (16√5/5 = HA, inversion pure) |
| 41-Q5 c (8√5 = 4 × BI, deux erreurs) | `thales-rapport-inverse` | option à deux erreurs | muette ; 41-Q5 b (HI au lieu de HB) → `math.alg.reponse-a-l-autre-inconnue` |
| 40-Q4 d (« (0 ; 8) » : OA² = 8 donné) | `pythagore-racine-oubliee` | voisine (pas de Pythagore ici) | `math.num.racine-et-carre-confondus` |
| 39-Q9 a (≤ au lieu de ≥) | muette | existante exacte | `math.num.ordre-inverse-a-tort` |
| 39-Q6 c (carré oublié) | muette | existante exacte | `math.num.racine-et-carre-confondus` |
| 36-Q4 a, 37-Q8 d (`droite-des-milieux-facteur-deux` pour « côté = segment ») | — | acceptable (1ʳᵉ phrase du libellé) | facultatif |

Familles muettes signalées par l'auteur, comptées sur la tranche + `origin/main` (grep des options et des explications) :
- « abscisse négative prise pour une longueur » : 40-Q2 b, e (options de `multi` : aucune des 47 questions `multi` publiées ne porte
  d'étiquette, convention) ; 40-Q1 c a déjà son étiquette (demi-différence, même valeur 3). Pas 3 questions taggables → **reste muette**.
- « oubli du carré » (39-Q6 c) et « inégalité inversée » (39-Q9 a) : une étiquette EXISTANTE convient (tableau) → pas de nouvelle.
- « symétrique aux rôles inversés » (40-Q7 d) : 1 occurrence (aucune dans le publié) → **reste muette**.
- « centre de gravité pris pour l'orthocentre » (37-Q11 a, 41-Q8 b) : `droites-remarquables-confondues` le nomme (médiane ↔ hauteur) →
  correct, rien à créer.
**Aucune étiquette nouvelle proposée.**

### 3. Programme (R-3) et ordre d'enseignement

Vérifié dans les cours de `origin/main` : droite des milieux et réciproque (ch. 18 § « أدوات البرهان »), médiane relative à
l'hypoténuse et réciproque, cercle de diamètre donné (ch. 18), médiatrice (ch. 18), centre de gravité aux 2/3 (ch. 08), papillon et
réciproque de Thalès (ch. 08), Pythagore et réciproque, AH × BC = AB × AC, AH² = BH × CH, aire de deux façons (ch. 09), diagonales
des parallélogramme/rectangle/losange (ch. 18), rectangle par les coordonnées (ch. 18 § « في المعلّم »), milieu/distance (ch. 12),
carré ≥ 0 et comparaison (ch. 17), identités (ch. 03). Écarts : **37-Q11** (concours des hauteurs, majeur) ; 37-Q3 (angles à la
base de l'isocèle), 38-Q4 (trois angles droits), 38-Q7 (réciproque du 2/3) : prérequis implicites, mineurs. Aucun vecteur ni
translation ; aucun « on admet » non signalé ; aucune clé n'exige AB² = BH × BC.

### 4. Rendu arabe

Toutes les lignes arabes (296) rendues dans Chromium `dir=rtl` avec le découpage de `splitMathRuns` (moteur `origin/main`, identique à
`/home/user/eng-gisement`) et les règles `.math-run` ; ordre gauche-droite des lettres, chiffres et opérateurs comparé au source.
Seuls écarts : calculs purement numériques dans les explications (« 36 − 9 = 27 », « 16 − 4 = 12 », « 32/5 = 6,4 »…), le degré
(« 45° ») et « 6 cm » sans lettre devant — tous lus de droite à gauche **par conception** du moteur (`DIGIT_FIRST_FORMULA` exige une
lettre ; commentaire de `bidi.ts` : « Digit-only arithmetic … keeps reading right to left ») : pas un défaut de contenu. Toutes les
lignes de formule seules (« E = x² − (32/5)x + 16 », « DA = 3√2 », « HC/HA = 1/4 », « AM² = … ») passent `isDisplayEquation`. Toutes
les options sans arabe passent `isMathExpression` (rendues `dir=ltr`). Aucune paire à virgule arabe, aucun chiffre indo-arabe, aucun
LaTeX, aucun `⟂` dans la tranche, aucune lettre à apostrophe, aucun « على الشكل التالي ».

**⟂ publié confirmé** : `content/math/09-triangle-rectangle-trigo/exercices/24-examen-2018-generale-ex2-radicaux-carres-triangle-isocele-aire-deux-facons.json`,
Q9, explication : « … وارتفاعه [EH] لأنّ EH ⟂ (BC) … » → remplacer par « لأنّ (EH) ⊥ (BC) » (U+22A5, et parenthèses de droite).

### 5. Figures

60 figures (Q1 et Q3 de 39 sans figure, algèbre) recalculées point par point (sections par mission) et rendues en planche Chromium :
toutes vraies, aucun élément ni attribut interdit, arabe seulement dans `<title>`, rien hors `viewBox`, angles droits codés seulement
quand ils sont donnés, aucun tracé ne désigne une clé. Figures à l'échelle qui laissent estimer une valeur : 36-Q4 (BD = AB), 40-Q1
(grille graduée), 40-Q3/Q4 (2√2 contre l'unité visible) — mineurs, décrits plus haut. 39 : M dessiné en a = 2, pas à la solution 3,2 ✓.

### 6. Titres, en-têtes, rampes

Titres au patron « 🏛️ مناظرة <année> · التمرين <N> ⭐⭐⭐⭐: … » ; le sujet nomme des notions, aucun résultat ✓. `difficulty` 4,
`challenge`, 300 XP / 60 pièces, `displayOrder` 36 → 41 ✓. Rampes conformes à l'annonce et non décroissantes ✓.

| mission | d3 / total | verdict |
|---|---|---|
| 36 (2013) | 5 / 12 (6 / 12 après déplacement de Q7) | d4 défendable |
| 37 (2016) | 7 / 12 | d4 honnête |
| 38 (2018) | 6 / 9 | d4 honnête |
| 39 (2019 ex.3) | 4 / 10 | d4 limite (Q8–Q10 vraiment difficiles ; Q2, Q6 faciles) |
| 40 (2019 ex.4) | 5 / 10 | d4 défendable |
| 41 (2020) | 5 / 10 | d4 défendable |

Aucune question d1–d2 gonflée en d3. 40-Q4 (racine d'une donnée) est un d1 étiqueté d2 (sans effet d'ordre).

### 7. Indices de forme

Clé strictement la plus longue : **40-Q10 seule** (mesure officielle confirmée) parmi les questions à choix unique ; dans les `multi`,
36-Q3 a et 40-Q2 a (seules phrases parmi des formules) sont justes et les plus longues — mineur, sans effet sur le nombre de vrais.
Vote terme à terme : 36-Q10, 37-Q7, 41-Q7 (majeurs ci-dessus). Paires équivalentes : 39-Q6 (majeur), 36-Q3 b/c (mineur). Nombre de
vrais des `multi` : 4, 3, 4, 3, 3, 3 sur 6 — non déductible.

---

## Chiffre final

- **Questions auditées : 63** (36 : 12 · 37 : 12 · 38 : 9 · 39 : 10 · 40 : 10 · 41 : 10), toutes re-résolues à l'aveugle avant lecture
  des clés (dont 5 `numeric` — valeur, unité, tolérance — et 6 `multi` jugées énoncé par énoncé).
- **Clés fausses : 0.** Aucune explication fausse (chaque égalité recalculée), aucune figure fausse.
- **Questions à reprendre pour un défaut majeur : 14** — 36-Q5, Q7, Q9, Q10, Q11 ; 37-Q4, Q7, Q11 ; 39-Q2, Q6, Q8 ; 40-Q10 ; 41-Q1,
  Q7.
- **Retouches mineures : 36-Q3, Q4, Q7 c, Q12 ; 37-Q2, Q3, Q10 ; 38-Q4, Q5, Q7, Q9 b ; 39-Q9 a ; 40-Q1, Q3, Q4 d ; 41-Q4, Q5** (et le
  `⟂` publié de 09/24 Q9).
- **Étiquettes** : 0 id neuf ; 4 étiquettes à retirer ou déplacer (36-Q7 c, 38-Q7 a, 41-Q4 d, 41-Q5 c), 5 à poser ou changer
  (39-Q6 c, 39-Q9 a, 40-Q4 d, 41-Q4 c, 41-Q5 b), plus celles des options réécrites.
- **Doublons** : 4 avec le publié (39-Q2, 41-Q1, 37-Q4, 36-Q5/Q9), 2 gabarits internes (36-Q10/37-Q7, 37-Q9/38-Q9).
- **Verdict : à corriger avant publication (fix-first).** Aucune clé fausse ; défauts concentrés sur des fuites (36-Q7→Q12, 36-Q11,
  39-Q8), des indices de forme (36-Q10, 37-Q7, 41-Q7, 39-Q6, 40-Q10), une notion non rappelée (37-Q11) et quatre doublons du publié.

Tous les textes de remplacement arabes proposés ci-dessus (19 chaînes) ont été rendus dans Chromium `dir=rtl` avec `splitMathRuns` : 0 inversion ; longueurs et vérité recalculées par script.
