# Audit indépendant — tranche L14 du gisement (maths 9ᵉ, chapitre 09, missions 36 à 41)

Auditeur indépendant (aucune ligne écrite de ce qui est audité). Consigne suivie :
`content-ingest/references/gisement-auditeur.md` (lue en entier), skill `content-audit` invoqué,
références `quality-bar.md`, `math-and-notation.md`, `course-quality.md`, `course-figures.md`,
`content-schema.md`, `rewards-and-modes.md`, `audit-correction.md`.

Périmètre : `content/math/09-triangle-rectangle-trigo/exercices/36…41-*.json` (arbre de travail tel
quel, 6 fichiers, 62 questions, 56 figures). Comparaisons et libellés lus sur `origin/main`
(contenu `d8af0b75`, moteur `a6fc5400` : `bidi.ts` à jour de #1150 et #1152).

Méthode :
- **À l'aveugle** : énoncés et options imprimés SANS `correctOption`, `answerKey`, étiquettes ni
  explications ; chaque question résolue jusqu'au bout et ma réponse notée AVANT la lecture de la clé.
  Chaque figure refaite par script (coordonnées des points, milieux, alignements, angles droits,
  échelle) et confrontée à la transcription officielle de la session.
- **Rendu** : chaque champ passé dans `splitMathRuns` / `isDisplayEquation` / `isMathExpression`
  du moteur `origin/main`, rendu dans Chromium (`dir="rtl"`, carte de 380 px, SVG passés par le
  même DOMPurify que l'app) ; l'ordre visuel de chaque glyphe est relevé (Range API) et comparé au
  texte source ; captures inspectées à l'œil.
- **Gates** (moteur `origin/main` sur l'arbre de travail) : `content:check` vert (120 matières) ;
  `content:qa --subject math` : 0 erreur, aucun avertissement sur 36–41 ; `content:tranche --chapters
  09` : aucune clé strictement la plus longue dans 36–41, aucune paire proche (≥ 0,45) qui les
  implique.
- Lint statique des 56 SVG : `viewBox` partout, aucun `width`/`height`, aucun élément ni attribut
  interdit, arabe seulement dans `<title>` ; boîtes englobantes mesurées dans Chromium : voir chaque
  fichier (débordements relevés fichier par fichier). 80 lignes de formule seule : toutes acceptées
  par `isDisplayEquation`.
  Toutes les options sans arabe sont rendues LTR (`isMathExpression`). Aucun chiffre indo-arabe,
  aucun LaTeX, aucun groupe de chiffres à espace simple, aucune virgule arabe dans une notation.
  Aucune occurrence restante de « على الشكل التالي » (piège de passe) ; « من الشكل a² − 2ab + b² »
  (38 Q6, explication) n'est pas pris par la regex du gate.

Convention : « clé lisible à l'échelle » = la figure est dessinée exactement à l'échelle des
données ; la longueur demandée se lit en reportant une longueur étiquetée (signalé comme demandé,
classé mineur et systémique : les missions publiées, ex. 35 Q10, font de même).

---

## 36 — 2003 ex. 4 (problème, filière unique) · d4 challenge 300/60 · displayOrder 36

Titre : « 🏛️ مناظرة 2003 · التمرين 4 ⭐⭐⭐⭐: مسألة الموسّط العمودي والدائرة المرسومة على قطر —
فيثاغورس والمستقيم الرابط بين منتصفين وعلاقة المساحة وطاليس » — conforme au patron, nomme des
notions, aucun résultat. Rampe 2,2,2,2,2,2,3,3,3,3,3 conforme (non décroissante).

Fidélité (transcription `2003.md`, exercice 4) : BC = 8, O milieu, Δ médiatrice, OA = 3, E = S_A(B),
cercle de diamètre [BC] recoupant (AB) = (BE) en D, F = Δ ∩ (CD) — toutes les données sont
celles du sujet. Résultats officiels recalculés (B(−4;0), C(4;0), A(0;3), E(4;6), D(1,12;3,84),
F(0;16/3)) : AB = 5, CE = 6, (EC) ⊥ (BC), CD = 4,8, ED = 3,6, AD = 1,4, AF = 7/3. Les 11 étapes
couvrent 1c, 2a (×2), 2b, 3a (×2), 3b, 4a, 4b, 5a, 5b : aucune sous-question perdue (1a, 1b = tracés).

| Q | d | ma réponse (aveugle) | clé | verdict | motif |
|---|---|---|---|---|---|
| 1 | 2 | a (5) | a | OK | OB = 4, AB² = 9 + 16 ; clé lisible à l'échelle (AB = 157,5 px = 5 × 31,5) |
| 2 | 2 | d (BCE) | d | réserve | `<title>` de la figure = « المثلّث BCE … » : nomme la clé (info-bulle, lecteur d'écran) |
| 3 | 2 | d (6) | d | OK | droite des milieux ; clé lisible à l'échelle |
| 4 | 2 | b | b | réserve | étiquette approximative `hypotenuse-mal-choisie` sur a et c (voir § Étiquettes) |
| 5 | 2 | c ([CD]) | c | OK | [CA] muette (médiane prise pour hauteur, voir § Familles) |
| 6 | 2 | d | d | **ERREUR de forme** | vote terme à terme : la clé se reconstruit (voir M-36-1) |
| 7 | 3 | c (24/5) | c | OK | plan 2×2 propre (15/4 muette) ; clé lisible à l'échelle (CD = 4,80) |
| 8 | 3 | b (3,6) | b | réserve | « 10,8 » = deux erreurs mais étiquetée ; 10,8 et 12,96 > CE = 6 (hypoténuse de CDE) s'éliminent à vue ; clé lisible à l'échelle |
| 9 | 3 | a (1,4) | a | OK | plan 2×2 propre (10,6 muette) ; clé lisible à l'échelle (AD = 40,9 px = 1,40) |
| 10 | 3 | a | a | OK | plan 2×2 propre (DA/AE = EC/AF muette), aucun vote possible |
| 11 | 3 | c (7/3) | c | OK | 6 × 7/18 = 7/3 ; options triées ; clé lisible à l'échelle |

Clés fausses : 0 / 11. Explications : toutes les égalités recalculées justes (6 × 10 ÷ (2 × 8) =
15/4, 48/10 = 24/5, 36 − 23,04 = 12,96, 1,4/3,6 = 7/18, 6 × 7/18 = 7/3…) ; chaque mécanisme d'erreur
produit bien la valeur de son option (3,4 = 7 − 3,6 avec BE = 14 ; 19/5 = 6 − 2,2 ; 42/25 = 6 × 1,4 ÷ 5).
Coche ✓ toujours après la clé. Aucune clé strictement la plus longue.

Fuites : aucune fuite EN AVANT (aucune explication ne donne la clé d'une question suivante ; Q7 donne
BE = 10, étape interne de Q9, pas sa clé). Données reprises EN ARRIÈRE (nécessaires à chaque énoncé
autonome) : Q6 « (CD) ⊥ (BE) » = clé de Q5 ; Q6–Q9 « BCE قائم في C » = clé de Q4 ; Q7–Q9, Q11
« CE = 6 » = clé de Q3 ; Q8 « CD = 4,8 » = clé de Q7 ; Q9 « ED = 3,6 » = clé de Q8 ; Q11 « DA = 1,4 »
= clé de Q9. Aucune n'est gratuite (chacune sert au calcul) ; aucune ne livre la clé d'une question
qui n'est pas sa source. Risque résiduel donjon seulement (deux questions du même fichier tirées dans
le même run, dans l'ordre inverse) — inhérent à la décomposition, accepté.

Rendu arabe : aucune chaîne brouillée dans Chromium ; seules les chaînes purement numériques
(« 3 + 4 = 7 », « 6 − 4,8 = 1,2 », « 6 × 7/18 = 7/3 ») se lisent de droite à gauche, comportement voulu
du moteur (natif, non isolé). Figures : 11, toutes vraies (milieux, alignements, D sur le cercle et
sur (BE) à t = 0,64, F sur Δ et sur (CD), angles droits marqués seulement là où ils sont donnés),
aucune ne marque la clé ; rendues en `dir=rtl` sans défaut.

Étage : 5 vraies d3 sur 11 (Q7 cercle → angle droit → Pythagore → relation d'aire ; Q8 cercle +
Pythagore décimal ; Q9 Pythagore + milieu + position relative ; Q10 papillon après déduction du
parallélisme ; Q11 Thalès décimal). En ligne avec les d4 publiées (04/28 : 4 d3/11 ; 20/19–21 :
5 d3/8–10). **Challenge d4 honnête.**

Défauts 36 :
- **M-36-1 (majeur)** Q6 — vote terme à terme : membres gauches CD × CB, CD × CE, CD × BE, CD × BE ;
  membres droits CE × BE, CB × BE, (CE × CB) ÷ 2, CE × CB → la majorité reconstruit la clé, c n'en
  diffère que par « ÷ 2 ». Correctif (plan 2×2, option à deux erreurs muette) :
  - option b : « CD × CE = CB × BE » → « CD × CB = (CE × BE) ÷ 2 », **retirer l'étiquette** ;
  - explication, fin : « … كما في CD × CB = CE × BE أو CD × CE = CB × BE ، مع أنّ … فنكتب
    CD × BE = (CE × CB) ÷ 2. » → « … كما في CD × CB = CE × BE ، مع أنّ [CD] هو ارتفاع الوتر [BE] وحده
    فيقابله الوتر في المساواة ؛ أو نسيان القسمة على 2 في أحد الحسابين فنكتب CD × BE = (CE × CB) ÷ 2 ؛
    أو الجمع بين الخطأين فنكتب CD × CB = (CE × BE) ÷ 2. »
  - Vérifié : 4,8 × 8 = 38,4 ≠ 6 × 10 ÷ 2 = 30 (fausse) ; votes 2–2 sur chaque membre et sur « ÷ 2 » ;
    longueurs 17 / 23 / 23 / 17 (la clé n'est pas la plus longue) ; option LTR (`isMathExpression`).
- **m-36-2 (mineur)** Q8 option c « 10,8 » (= 6 + 4,8 : somme des longueurs là où il faut une
  DIFFÉRENCE de carrés = deux erreurs) porte `pythagore-sans-carres` → retirer l'étiquette (muette).
- **m-36-3 (mineur)** Q2 — `<title>` « المثلّث BCE والنقطتان A و O » → « النقاط B و C و E والمنتصفان A و O ».
- **m-36-4 (mineur)** Q4 a, c — `hypotenuse-mal-choisie` sur « angle droit au mauvais sommet » :
  inexact, traité au § Étiquettes (nouvelle étiquette proposée).
- Observation (mineur systémique) : Q1, Q3, Q7, Q8, Q9, Q11 — clé lisible à l'échelle ; Q8 est le cas
  le plus net (10,8 et 12,96 plus longs que CE = 6 et même que BE = 10 sur la figure).

Verdict partiel 36 : **11 questions, 0 clé fausse, 1 question à reprendre (Q6), 3 retouches mineures.**

---

## 37 — 2007 ex. 4 (problème, filière unique) · d4 challenge 300/60 · displayOrder 37

Titre : « 🏛️ مناظرة 2007 · التمرين 4 ⭐⭐⭐⭐: مسألة المنتصف والدائرة المرسومة على قطر — فيثاغورس
والمستقيم الرابط بين منتصفين ومركز الثقل وطاليس والمركز القائم » — conforme, aucune valeur. Rampe
2,2,2,2,2,2,2,3,3,3,3,3 conforme.

Fidélité (`2007.md`, exercice 4) : AB = 8, O milieu, Δ médiatrice, P ∈ Δ avec OP = OA, 𝒞 de diamètre
[AB], parallèle à (AP) par O coupant (PB) en M, G = (AM) ∩ Δ, perpendiculaire à (AB) par M coupant
(AP) en H, N second point de (AM) ∩ 𝒞 — toutes les données sont celles du sujet. Recalcul exact
(A(−4;0), B(4;0), P(0;4), M(2;2), K(2;0), H(2;6), N(16/5;12/5)) : AP = 4√2, PAB rectangle isocèle
en P, P ∈ 𝒞, M milieu de [BP], OM = 2√2, G centre de gravité (OG = 4/3), AP/AH = 2/3, AH = 6√2,
(AP) ⊥ (BM), (BN) ⊥ (AM), B, N, H alignés. Les 12 étapes couvrent 2a, (médiatrice, ajoutée), 2b,
2c, 3a, 3b, (N sur 𝒞, ajoutée), 4a, 4b, 4c, 5a, 5b : rien de perdu. Adaptation NON déclarée : Q8
remplace « بيّن أنّ G مركز ثقل » par le calcul de OG (OG n'est pas demandé par le sujet) ; la
reconnaissance du centre de gravité reste indispensable à la réponse → acceptable, à déclarer.

| Q | d | ma réponse (aveugle) | clé | verdict | motif |
|---|---|---|---|---|---|
| 1 | 2 | d (4√2) | d | réserve | plan 2×2 propre ; mais les trois distracteurs (4√5 ≈ 8,9, 16√2, 16√5) dépassent AB = 8 étiqueté, et AP < AB se voit : clé lisible à l'échelle (cas le plus net de la tranche) |
| 2 | 2 | c | c | réserve | b (cercle) et a (bissectrice) portent sur des objets absents de l'énoncé ; seule la clé reprend « الموسّط العمودي » de l'énoncé (m-37-3) |
| 3 | 2 | b (étape 2) | b | OK | erreur unique et plausible (angle droit en A au lieu de P) ; étapes 1 et 3 vraies ; option « لا يوجد خطأ » : voir § systémique |
| 4 | 2 | {a, b} | {a, b} | réserve | a et b valides, c et d invalides ; nombre de clés non annoncé ; c et d seules portent une glose « أي أنّ … » (m-37-4) |
| 5 | 2 | d (1/2) | d | réserve | explication donne OM/AP = 1/2 : méthode de Q6 (m-37-5) |
| 6 | 2 | a (2√2) | a | OK | droite des milieux ; étiquettes exactes ; clé lisible à l'échelle |
| 7 | 2 | c | c | **ERREUR de forme** | d « (BN) ∥ (AM) » nie l'énoncé : les deux droites passent par N (M-37-1) ; le vote reconstruit aussi la clé |
| 8 | 3 | b (4/3) | b | OK | centre de gravité ; trois étiquettes exactes ; clé lisible à l'échelle |
| 9 | 3 | b (2/3) | b | OK | K milieu de [OB], AK = (3/2)AO, Thalès ; « 4/3 » muette mériterait `segment-mal-choisi` (m-37-8) |
| 10 | 3 | c (6√2) | c | OK | plan 2×2 propre (16/3 muette) ; figure : « 4 » collé au trait de codage (m-37-9) |
| 11 | 3 | a | a | **ERREUR de forme** | la clé est la seule à donner deux raisons, réunion de celle de b et de celle de d (M-37-2) ; « المركز القائم » sans glose (M-37-6) |
| 12 | 3 | d | d | réserve | R-3 : « المركز القائم » porte la réponse et n'est enseigné dans aucun cours (M-37-6) |

Clés fausses : 0 / 12. Toutes les égalités des explications recalculées justes (√32 = 4√2, √80 =
4√5, (3/2) × 4√2 = 6√2, (2/3) × 8 = 16/3, AB/AK = 4/3…), chaque mécanisme d'erreur produit la valeur
de son option. Coche ✓ toujours après la clé. Aucune clé strictement la plus longue. `multi` Q4 :
chaque énoncé jugé seul (a : OP = OA = AB/2 = rayon, valide ; b : cercle circonscrit d'un triangle
rectangle, valide ; c : équidistance de A et B ⇒ médiatrice, pas cercle ; d : AOP droit ≠ APB droit).

Fuites : en avant, une seule (Q5 → Q6, méthode). Q7 établit (BN) ⊥ (AM), prémisse commune de c et d
en Q12 : décomposition voulue, acceptable. En arrière (toutes nécessaires) : Q3 « PA = PB = 4√2 »
(clé de Q1), Q4 et Q11 « PAB قائم في P » (conclusion de Q3), Q6 « M منتصف [BP] » (clé de Q5) et
« AP = 4√2 », Q7–Q9 « M منتصف », Q10 « AP/AH = 2/3 » = clé de Q9 (donnée nécessaire au calcul de AH,
elle ne livre aucune AUTRE clé ; risque résiduel donjon seulement), Q12 « H مركز قائم » (but de Q11).

Rendu : aucune chaîne brouillée. Figures : 12, toutes vraies (milieux, N sur 𝒞 et sur (AM), G sur
(OP) au tiers, H sur (AP) avec AH = 1,5 AP, B, N, H alignés en Q12), aucune ne marque la clé.
Débordement : Q2, « Δ » à y = 9,65 sort du `viewBox` (boîte −4,1) — sommet du glyphe rogné.

Étage : 5 vraies d3 (Q8 deux étapes, Q9 quatre, Q10 deux avec radicaux, Q11 argument d'orthocentre,
Q12 cercle + hauteur + orthocentre). **Challenge d4 honnête.**

Défauts 37 :
- **M-37-1 (majeur)** Q7 — d « المستقيمان (BN) و (AM) متوازيان » est contredit par l'énoncé (N ∈ (AM)
  et N ∈ (BN)) : s'élimine à vue ; en prime, (BN) et (AM) figurent chacune dans 3 options et
  « متعامدان » dans 3 : le vote rend c. Correctif :
  - d → « المستقيمان (AM) و (BP) متعامدان », **retirer** `perpendiculaire-et-parallele-confondus`
    (muette : médiane prise pour hauteur) ; vérifié faux (AM·BP = −16 ≠ 0), 31 caractères comme la clé ;
    vote ramené à b/c ;
  - explication, fin « ؛ أو الخلط بين التعامد والتوازي ، مع أنّ (BN) و (AM) يتقاطعان في N. » →
    « ؛ أو اعتبار الموسّط (AM) ارتفاعًا فنقول (AM) ⊥ (BP) ، مع أنّ M منتصف [BP] وليست المسقط العمودي
    للنقطة A عليه. »
- **M-37-2 (majeur)** Q11 — forme « nombre de conditions » : la clé seule donne deux raisons, qui
  sont la raison de b (« PAB قائم في P ») plus celle de d (« M من [PB] »). Correctif :
  - d → « (AP) عمودي على (AM) ، لأنّ PAB قائم في P و M من (PB) » (muette ; même double raison que la
    clé, mauvais côté) ; vérifié faux (AP·AM = 32 ≠ 0) ; longueurs 52 / 48 / 55 / 52 ;
  - explication, fin « ؛ أو اعتبار (AP) عموديًّا على (AM) لمجرّد أنّ M من [PB]. » → « ؛ أو الانطلاق من
    الحجّة الصحيحة ثمّ الخطأ في الضلع: الزاوية القائمة في P تجعل (AP) عموديًّا على (PB) أي على (BM) ،
    لا على (AM). »
- **M-37-6 (majeur, R-3)** Q11, Q12 — « المركز القائم » n'apparaît dans AUCUN cours (7ᵉ : « الارتفاعاتُ
  الثلاثة | نقطةٌ واحدة » sans nom ; 8ᵉ, 9ᵉ : rien), alors que 39 Q8 le glose et que les publiées 35 Q8,
  devoirs 11 et 15 le rappellent. Correctifs :
  - Q11 énoncé : « نريد إثبات أنّ H هي المركز القائم للمثلّث ABM. » → « نريد إثبات أنّ H هي المركز
    القائم للمثلّث ABM (نقطة تلاقي ارتفاعاته). » (aucune option ne contient « ارتفاع » : pas d'indice) ;
  - Q12 : la même glose désignerait la clé (« ارتفاعاته » ↔ seule d dit « الارتفاع ») — NE PAS gloser
    l'énoncé ; nommer le point dans le cours, ligne du tableau de `math-7eme/11-triangles/cours.md` :
    « | الارتفاعاتُ الثلاثة | نقطةٌ واحدة | » → « | الارتفاعاتُ الثلاثة | نقطةٌ واحدة، تُسمّى **المركزَ
    القائم للمثلّث** | » (calque de la ligne du centre de gravité ; hors des six fichiers, à router).
    En attendant, Q12 reste soluble par élimination (N n'est pas milieu de [AM], (BN) hors de l'angle
    ABM) mais la conclusion « إذن يمرّ من H » repose sur un terme non enseigné.
- **m-37-3 (mineur)** Q2 — b « كلّ نقطة من دائرة تبعد المسافة نفسها عن مركزها » (cercle absent de
  l'énoncé) → « كلّ نقطة من مستقيم يمرّ من منتصف قطعة تبعد المسافة نفسها عن طرفيها » (muette,
  symétrique de d : milieu sans perpendicularité ; fausse) ; longueurs 52 / 66 / 62 / 62. Explication :
  remplacer « وخاصية الدائرة تعطي بعد النقطة عن المركز لا عن A و B ، وأمّا العمودي على القطعة فلا يكفي
  أن يكون عموديًّا عليها ، بل يجب أن يمرّ من منتصفها. الخطأ الشائع: الاكتفاء بأنّ Δ عمودي على (AB) دون
  التحقّق من أنّه يمرّ من المنتصف O ، فنطبّق خاصية لا تصحّ إلّا مع الموسّط العمودي. » par « والمستقيم
  المارّ من منتصف القطعة لا يكفي إن لم يكن عموديًّا عليها ، والعمودي على القطعة لا يكفي إن لم يمرّ من
  منتصفها. الخطأ الشائع: الاكتفاء بأحد الشرطين ، التعامد أو المرور من المنتصف O ، مع أنّ الخاصية لا تصحّ
  إلّا مع الموسّط العمودي الذي يجمعهما. » (l'appariement résiduel « الموسّط العمودي » énoncé ↔ clé est
  inhérent à la question.)
- **m-37-4 (mineur)** Q4 — homogénéiser : c → « PA = PB ، إذن P تنتمي إلى الدائرة » ; d → « (OP) عمودي
  على (AB) في O ، إذن P تنتمي إلى الدائرة » (longueurs 47 / 58 / 33 / 50 : plus de partition par la forme).
- **m-37-5 (mineur, fuite en avant)** Q5 explication : « فبنظرية طاليس BM/BP = BO/BA = OM/AP. » →
  « فبنظرية طاليس BM/BP = BO/BA. » (OM/AP = 1/2 est la clé de méthode de Q6).
- **m-37-7 (mineur)** Q2 figure : `<text … y="9.65" …>Δ</text>` → `y="14"`.
- **m-37-8 (mineur)** Q9 c « 4/3 » (AB/AK : AB pris pour AO) muette → `math.geo.segment-mal-choisi`.
- **m-37-9 (mineur)** Q10 figure : le « 4 » de OP (x = 204,64) touche le trait de codage (188,64–198,64) et
  se lit « −4 » → `x="214"`.
- Cosmétique : Q9, le trait de codage de [OB] tombe sur K et disparaît sous (KH).
- Observation : Q1, Q6, Q8, Q10 — clé lisible à l'échelle (Q1 le cas le plus net).

Tous les remplacements ci-dessus ont été appliqués à une copie hors dépôt, rendus dans Chromium
(`dir=rtl`) et repassés au contrôle d'ordre visuel : aucune chaîne brouillée.

Verdict partiel 37 : **12 questions, 0 clé fausse, 3 questions à reprendre (Q7, Q11, Q12 via le cours),
7 retouches mineures.**

---

## 38 — 2012 générale ex. 4 (5 points) · d4 challenge 300/60 · displayOrder 38

Titre : « 🏛️ مناظرة 2012 · التمرين 4 ⭐⭐⭐⭐: مثلّث ونقطة متحرّكة على ضلعه — فيثاغورس وعكسه ومساحة
بدلالة متغيّر والمتطابقات الشهيرة والحصر » — conforme, aucune valeur. Rampe 2,2,2,2,2,2,3,3,3 conforme.

Fidélité (`2012-generale.md`, exercice 4) : AB = AC = 8, BC = 8√2, F ∈ [AB] distincte de A et B,
BF = x (0 < x < 8), perpendiculaire à (AB) en F coupant (BC) en E, a = aire de AEF — données
fidèles. Résultats officiels recalculés : ABC rectangle en A, EF = x, a = x(8 − x)/2, 8 − a = (x − 4)²/2,
0 < a ≤ 8, a = 8 ⟺ x = 4, F milieu de [AB]. « 12 → 9 » : aucune sous-question officielle perdue —
1 → Q1 ; 2b → Q3 ; 2c → Q2 (AF, étape) + Q4 ; 3a → Q5 + Q6 ; 3b → Q7 (signes, étape) + Q8 ;
4a + 4b → Q9 (x = 4 devient étape interne, repli déclaré) ; 2a = tracé.

| Q | d | ma réponse (aveugle) | clé | verdict | motif |
|---|---|---|---|---|---|
| 1 | 2 | a | a | réserve | `hypotenuse-mal-choisie` approximatif sur b, c (§ Étiquettes) ; la figure montre l'angle droit en A (non codé) |
| 2 | 2 | c (8 − x) | c | réserve | « قائم في A » de l'énoncé inutile au calcul (redonne la clé de Q1) ; question presque d1 |
| 3 | 2 | b (x) | b | OK | 45° ou Thalès ; trois étiquettes exactes |
| 4 | 2 | d | d | réserve | plan 2×2 propre ; la figure ne trace pas [AE] : le triangle AEF dont on demande l'aire n'est pas dessiné |
| 5 | 2 | c (étape 3) | c | OK | erreur unique et plausible (signe), étapes 1, 2 vraies, 4 = réarrangement fidèle ; « أوّل خطأ » et pas d'option « aucune erreur » : modèle à suivre |
| 6 | 2 | b ((x − 4)²) | b | OK | c « (x + 4)² » muette mériterait `carre-difference-signes` (m-38-5) |
| 7 | 3 | {b, d, e} | {b, d, e} | OK | chaque expression jugée seule ; nombre de clés non annoncé ; « الحصر السابق » renvoie au même énoncé |
| 8 | 3 | d | d | **ERREUR (ambiguïté)** | c « 0 ≤ a ≤ 8 » est VRAI pour tout x ∈ ]0 ; 8[ : deux options justes (B-38-1) |
| 9 | 3 | b (1/2) | b | OK | (x − 4)² = 0 ⇒ x = 4 ⇒ BF/AB = 1/2 ; chaque mécanisme d'erreur vérifié (1/4, 1, 2) |

Clés fausses : 0 / 9, mais **une question à deux réponses justes (Q8)**. Explications recalculées :
(8√2)² = 128, (x − 8)² = x² − 16x + 64, (x − 4)(x + 4) = x² − 16, EF = 8x/(8√2) = x/√2 — justes ; en
Q8, la phrase « إدراج الصفر في الحصر فنكتب 0 ≤ a ، مع أنّ a لا تنعدم » présente comme faux un
encadrement vrai. Aucune clé strictement la plus longue. `multi` Q7 : a (x − 4, signe variable) et c
((x − 4)², nul en 4) faux, b, d, e vrais.

Fuites : aucune en avant (Q5 donne (16 − 8x + x²)/2, que Q6 factorise sans en donner la forme ; Q7
donne x(8 − x) > 0, demi-étape de Q8 : décomposition). En arrière : Q4 « EF = x » (clé de Q3), Q8 et
Q9 « 8 − a = (x − 4)²/2 » (résultat de Q5 + Q6), Q8 « a = x(8 − x)/2 » (clé de Q4) — nécessaires.
Q2 et Q4 redonnent « قائم في A » (clé de Q1) sans en avoir besoin (seule Q3 s'en sert).

Rendu : aucune chaîne brouillée (« 45° » s'affiche « °45 » en RTL, rendu natif que `bidi.ts` déclare
correct, comme « 90° »). Figures : 4, vraies (BF = EF = 3 unités, E sur (BC) à t = 0,375), aucune ne
marque la clé, aucun débordement.

Étage : **challenge d4 NON honnête.** 3 d3 sur 9 (33 %, sous toutes les d4 publiées : 36 % à 63 %),
dont Q9 est molle ((x − 4)² = 0 puis un rapport) ; les d2 sont du calcul de routine (Q2 quasi d1) ;
exercice à 5 points (pas le problème à 8 points de 2003/2007) ; ses pareils publiés — 23 (2015 ex. 3,
trinôme/factorisation/réciproque), 24 (2018 ex. 2), 28 (2021 ex. 4, trinôme/aires/paramètre) — sont
tous boss d3. **Repli : boss d3 120/30** (`difficulty: 3`, `mode: "boss"`, `xpReward: 120`,
`rewardCoins: 30`, titre « ⭐⭐⭐ » au lieu de « ⭐⭐⭐⭐ ») ; rampe interne inchangée.

Défauts 38 :
- **B-38-1 (critique)** Q8 — « ما الحصر الصحيح للعدد a ؟ » : c « 0 ≤ a ≤ 8 » est un encadrement vrai
  (a ∈ ]0 ; 8]), au même titre que la clé ; la donnée « استنتج أنّ 0 < a ≤ 8 » du sujet, retirée, rendait
  la cible unique. Correctif (vérifié sur 799 valeurs de x : seule d reste vraie) :
  - c « 0 ≤ a ≤ 8 » → « 0 < a ≤ 4 », étiquette `math.alg.reponse-a-l-autre-inconnue` (la valeur x = 4,
    où le carré s'annule, prise pour borne de a) ;
  - explication, fin « الخطأ الشائع: اعتبار المربّع موجبًا تمامًا فنكتب a < 8 ؛ أو إدراج الصفر في الحصر
    فنكتب 0 ≤ a ، مع أنّ a لا تنعدم لأنّ x و 8 − x موجبان تمامًا. » → « الخطأ الشائع: اعتبار المربّع موجبًا
    تمامًا فنكتب a < 8 ، مع أنّ a = 8 عند x = 4 ، وهذا يُسقط الحصرين 0 < a < 8 و 0 ≤ a < 8 ؛ أو أخذ
    القيمة x = 4 التي ينعدم عندها المربّع حدًّا أعلى لـ a فنكتب a ≤ 4 ، مع أنّ a = 8 عندها. »
  - Ne PAS prendre « 0 < a ≤ 16 » (oubli du ÷ 2) : vrai lui aussi. Longueurs 9/9/9/9 ; vote : la
    majorité désigne a (distracteur), plus la clé.
- **M-38-2 (majeur, étage)** repli boss d3 120/30 ci-dessus.
- **m-38-3 (mineur)** Q4 figure : ajouter le côté [AE] du triangle dont on demande l'aire, juste avant le
  premier `<path` : `<path d="M65 226 L183.75 154.75" fill="none" stroke="#0f6e56" stroke-width="2"
  stroke-linecap="round"/>` (rendu vérifié).
- **m-38-4 (mineur)** Q2 énoncé : « ABC مثلّث قائم في A حيث AB = AC = 8 ، » → « ABC مثلّث حيث AB = 8 ، »
  et retirer de sa figure le codage d'angle droit en A (`<path d="M76 226 L76 215 L65 215" …/>`) ; même
  allègement possible en Q4 (« قائم في A » inutile, seul « AB = 8 » sert).
- **m-38-5 (mineur)** Q6 c « (x + 4)² » muette → `math.alg.carre-difference-signes`.
- Observation : Q1, la figure montre l'angle droit qu'il faut démontrer (non codé : pas un défaut de
  codage) ; Q3, EF = BF se voit.

Verdict partiel 38 : **9 questions, 0 clé fausse, 1 question à reprendre (Q8, critique), étage à
replier en boss d3, 3 retouches mineures.**

---

## 39 — 2015 générale ex. 4 (5 points) · d4 challenge 300/60 · displayOrder 39

Titre : « 🏛️ مناظرة 2015 · التمرين 4 ⭐⭐⭐⭐: مسألة الدائرة المرسومة على قطر — فيثاغورس وعلاقة المساحة
والمركز القائم وطاليس » — conforme. Rampe 2,2,2,2,2,2,2,3,3,3,3 conforme.

Fidélité (`2015-generale.md`, exercice 4) : cercle de centre I et de diamètre [AB], AB = 5, C sur le
cercle avec AC = 3, H projeté de C sur (AB), M ∈ [AB) avec AM = 6, perpendiculaire à (AB) par M
coupant (AC) en E et (BC) en F, K = (EB) ∩ (AF) — fidèles. Recalcul exact (A(0;0), B(5;0),
C(9/5;12/5), H(9/5;0), M(6;0), E(6;8), F(6;−3/4), K(64/13;−8/13)) : ACB = 90°, BC = 4, CH = 12/5,
BH = 16/5, BM = 1, B orthocentre de AEF, K sur le cercle (IK = 5/2), BF/BC = 5/16, BF = 5/4.
« 14 → 11 » : rien de perdu — 1b → Q1 ; 1c → Q2, Q3 ; 1d → Q4 ; 2 → Q5 (BM, ajoutée, déclarée) ;
2a → Q6 (étape) + Q8 ; 2b → Q9 ; 3 → Q7 (égalité) + Q10 (valeur) ; BF → Q11 ; 1a = tracé.

| Q | d | ma réponse (aveugle) | clé | verdict | motif |
|---|---|---|---|---|---|
| 1 | 2 | b (90°) | b | OK | angle inscrit dans un demi-cercle ; étiquettes exactes |
| 2 | 2 | c (4) | c | OK | trois étiquettes exactes (16, 2, √34) ; clé lisible à l'échelle |
| 3 | 2 | a (12/5) | a | réserve | les trois distracteurs (15/4, 6, 20/3) dépassent AC = 3 : le contrôle « العمودي أقصر من كلّ مائل », enseigné par le cours du chapitre, désigne la clé (m-39-1) |
| 4 | 2 | d (16/5) | d | OK | étiquettes exactes (AH, 4 − 12/5, oubli de la racine) |
| 5 | 2 | a (1) | a | OK | seule question de géométrie sans figure : justifié (dessiner M au-delà de B donnerait la clé) |
| 6 | 2 | d | d | OK | E ∈ (AC) et angle droit en C ; angle en C non codé sur la figure (il donnerait la clé) |
| 7 | 2 | b | b | OK | plan 2×2 (HM/BM muette), aucun vote |
| 8 | 3 | c (B) | c | OK | glose « (نقطة تلاقي ارتفاعاته) » suffisante, options = des points, aucun appariement de mots |
| 9 | 3 | a | a | réserve | plan 2×2 propre, mais « المركز القائم » sans glose dans l'énoncé (R-3, § transversal) ; options de 131 à 136 caractères |
| 10 | 3 | d (5/16) | d | OK | plan 2×2 (16/55 muette) |
| 11 | 3 | b (5/4) | b | OK | trois erreurs simples, étiquettes exactes ; 64/5 et 55/4 dépassent AM = 6 sur la figure |

Clés fausses : 0 / 11. Égalités des explications recalculées justes (16 − 144/25 = 256/25 ; 9 − 144/25
= 81/25 ; 11 ÷ (16/5) = 55/16 ; 4 × 5/16 = 5/4 ; √34 × 5/16). Coche ✓ toujours après la clé. Aucune
clé strictement la plus longue.

Fuites : aucune en avant (Q6 donne (BC) ⊥ (AE), demi-étape de Q8 ; Q7 donne BF/BC = BM/BH, que Q10
chiffre : décomposition). En arrière, toutes nécessaires : Q3 « BC = 4 » (Q2), Q4 « CH = 12/5 » (Q3),
Q6–Q8, Q10, Q11 « ABC قائم في C » (Q1), Q9 « B هو المركز القائم » (Q8), Q10–Q11 « BH = 16/5 » (Q4 :
donnée indispensable au rapport, elle ne livre aucune autre clé).

Rendu : aucune chaîne brouillée (« 90° » → « °90 » natif, déclaré correct). Figures : 10, vraies
(C sur le cercle, AC = 3 à 46,4 px/unité, B sur (CF) à t = 16/21, K sur le cercle et sur (EB)),
aucune ne marque la clé, aucun débordement. Q9 : B et K très proches (16 px) mais lisibles.

Étage : 4 vraies d3 sur 11 (Q8 orthocentre, Q9 argument cercle, Q10 papillon + position de M, Q11
Pythagore + Thalès). Au niveau des d4 publiées (04/28 : 4/11). **Challenge d4 honnête, à la limite
basse** (exercice à 5 points ; mais orthocentre + papillon + relations métriques en font le plus riche
des exercices à 5 points de la tranche).

Défauts 39 :
- **m-39-1 (mineur)** Q3 — d « 20/3 » → « 6/5 » (demi d'un seul côté : AB × CH = (AC × BC) ÷ 2),
  étiquette `math.mes.aire-triangle-sans-moitie` ; explication : « فنكتب CH × BC = AB × AC ومنه CH = 15/4 ،
  أو CH × AC = AB × BC ومنه CH = 20/3 ، وكلتاهما أطول من [AC] ، وهذا مستحيل لأنّ العمودي أقصر من كلّ
  مائل ؛ » → « فنكتب CH × BC = AB × AC ومنه CH = 15/4 ، وهو أطول من [AC] ، وهذا مستحيل لأنّ العمودي
  أقصر من كلّ مائل ؛ أو القسمة على 2 في أحد الحسابين فقط فنكتب AB × CH = (AC × BC) ÷ 2 ومنه CH = 6/5 ؛ »
  (vérifié : 6 ÷ 5 = 6/5 ≠ 12/5 ; rendu Chromium propre ; longueurs 4/4/1/3).
- **R-3 (renvoi au § transversal)** Q9 : « B هو المركز القائم للمثلّث AEF » sans glose ; une glose ici
  ne trancherait que la moitié « ارتفاع / الموسّط العمودي » du plan 2×2 (a et b la portent) : acceptable
  si le cours n'est pas corrigé.
- Optionnel (lisibilité) Q9 : retirer des quatre options la queue commune « ، إذن K تنتمي إلى الدائرة التي
  قطرها [AB] » (c'est le but posé par l'énoncé) ; options ramenées à ~95 caractères.
- Observation : Q2, Q3, Q4, Q11 — clé lisible à l'échelle.

Verdict partiel 39 : **11 questions, 0 clé fausse, 0 question à reprendre au fond (Q9 suit le correctif
R-3 transversal), 1 retouche mineure.**

---

## 40 — 2017 générale ex. 4 (5 points) · d4 challenge 300/60 · displayOrder 40

Titre : « 🏛️ مناظرة 2017 · التمرين 4 ⭐⭐⭐⭐: مسألة دائرة مركزها رأس مثلّث قائم — فيثاغورس والدائرة
المرسومة على قطر ومنتصف الوتر وطاليس » — conforme. Rampe 2,2,2,2,2,3,3,3,3 conforme.

Fidélité (`2017-generale.md`, exercice 4) : AOB rectangle en A, AB = 4, AO = 3, 𝒞 de centre O passant
par A coupant [OB] en E, D second point de (AO) ∩ 𝒞, Δ ⊥ (AB) en B coupant (AE) en F, I milieu de
[DF], H projeté de E sur (AB) — fidèles. Recalcul exact (A(0;0), B(4;0), O(0;3), E(12/5;6/5),
D(0;6), F(4;2), H(12/5;0)) : OB = 5, BE = 2, AD = 6, (AE) ⊥ (DE), BF = 2 = BE, IE = IF, (IB) ∥ (DE),
EH = 6/5, BH = 8/5. « 9 → 9 » : 1b → Q1 ; 2 → Q2 ; AD = 6 (ajoutée, déclarée) → Q3 ; IE = IF (ajoutée,
déclarée) → Q4 ; 5a → Q5 ; 3a → Q6 ; 3b → Q7 (calcul de BF = BE au lieu de « بيّن أنّ B تنتمي للموسّط
العمودي » : adaptation, la conclusion d'équidistance est dans l'explication) ; 4 → Q8 ; 5b → Q9.

| Q | d | ma réponse (aveugle) | clé | verdict | motif |
|---|---|---|---|---|---|
| 1 | 2 | c (5) | c | réserve | options {√7, 5, 7, 25}, pièges et explication identiques à la publiée 31 Q1 (§ Doublons) |
| 2 | 2 | a (2) | a | OK | OE = rayon ; « 4 » muette (Pythagore sur trois points alignés) |
| 3 | 2 | d (6) | d | réserve | d1 de fait (diamètre = 2 × rayon) étiquetée d2 |
| 4 | 2 | b | b | OK | `mediane-hypotenuse-demi` exacte sur « IE = DF » |
| 5 | 2 | c | c | OK | plan 2×2 propre (BE/EO = BA/BH muette) |
| 6 | 3 | a | a | OK | [AD] diamètre ⇒ E droit ; droites équilibrées (AE, DE, AD, OE : 2 chacune) |
| 7 | 3 | d (2) | d | OK | papillon de sommet E, OE = 3, BE = 2 ; plan 2×2 propre (9/8 muette) ; BF = BE se voit |
| 8 | 3 | b (étape 2) | b | OK | étape 1 vraie, étape 2 fausse (équidistance prise pour milieu), étape 3 déduction valide de l'étape 2 : erreur unique ; la conclusion vraie rend « لا يوجد خطأ » tentante (voir § systémique) |
| 9 | 3 | c (6/5 ; 8/5) | c | OK | paires étiquetées « EH = … ; BH = … » ; chaque option garde EH/BH = 3/4, aucun vote |

Clés fausses : 0 / 9. Égalités des explications recalculées (16 − 9 = 7, 3 × 2/3 = 2, 3 × 3/2 = 9/2,
3 × 8/3 = 8, 3 × 3/8 = 9/8, 3 × 2/5 = 6/5, 4 × 2/5 = 8/5, 3 × 3/5 = 9/5, 4 × 3/5 = 12/5) : justes. Aucune
clé strictement la plus longue.

Fuites : aucune en avant (Q7 conclut BF = BE, prémisse de Q8 mais pas sa clé). En arrière, toutes
nécessaires : Q2, Q7, Q9 « OB = 5 » (Q1), Q9 « BE = 2 » (Q2), Q8 « B على الموسّط العمودي » (conclusion de
Q7). Énoncés abstraits de Q4 et Q8 (triangle DEF) : ils évitent bien de livrer la clé de Q6/Q7.

Rendu : aucune chaîne brouillée (chaînes numériques lues de droite à gauche, natif). Figures : 9,
vraies (E sur 𝒞 et sur [OB] à t = 0,6 ; F sur Δ et (AE) ; I milieu de [DF] ; B équidistant de E et F et
hors de (EF) ; (IB) passe par le milieu de [EF]), aucune ne marque la clé, aucun débordement.
Cosmétique Q9 : l'étiquette « 2 » de [EB] (217,29 ; 179,57) est à 16 px de [EB] et à 20 px de [HB] —
on peut la lire comme BH = 2, valeur d'un distracteur ; la placer au-dessus de [EB], vers (235 ; 155).

Étage : 4 d3 sur 9 (Q7 et Q8 solides, Q6 et Q9 moyennes) ; base d2 très facile (Q2, Q3). **Challenge
d4 honnête de justesse** (au niveau numérique des d4 publiées) ; Q3 est une d1.

Défauts 40 : aucun critique ni majeur propre au fichier ; Q1 relève du § Doublons ; Q8 du § systémique
(« لا يوجد خطأ ») ; Q3 étiquetée d2 pour une d1 (mineur) ; Q9 cosmétique ci-dessus.

Verdict partiel 40 : **9 questions, 0 clé fausse, 0 question à reprendre au fond (Q1 selon § Doublons),
2 retouches mineures.**

---

## 41 — 2021 générale ex. 3 (5,5 points) · d4 challenge 300/60 · displayOrder 41

Titre : « 🏛️ مناظرة 2021 · التمرين 3 ⭐⭐⭐⭐: معيّن متعامد ومتجانس — المسافات والمناظرة والمنتصف وطاليس
وعكس فيثاغورس والإحداثيّات » — conforme. Rampe 2,2,2,2,2,3,3,3,3,3 conforme.

Fidélité (`2021-generale.md`, exercice 3) : repère orthonormé, I(1 ; 0), J(0 ; 1), A(2 ; 4), B(2 ; 0),
C symétrique de B par rapport à O, K = (AC) ∩ (OJ), M = (BJ) ∩ (OA), H projeté de M sur (OB) —
fidèles. Recalcul exact : OAB rectangle en B, OA = 2√5, C(−2 ; 0), K milieu de [AC], K(0 ; 2),
BJ = √5, MJ/MB = MO/MA = 1/4, MO = 2√5/5, MB = 4√5/5, OM² + MB² = 4 = OB², MH = 4/5, OH = 2/5,
M(2/5 ; 4/5) (intersection de y = 2x et y = 1 − x/2). « 12 → 10 » : rien d'important perdu — 1a → Q1 ;
1b → Q2 ; 2a → Q3 ; 2b → Q4 ; 2c → Q5 ; 3a (BJ = √5) donnée dans Q7 (repli déclaré : calcul immédiat,
acceptable) ; 3b → Q6 (rapport MJ/MB ; MO/MA est redonné en Q7) ; 3c + 3d (calcul) → Q7 ; 3d (angle
droit) → Q8 ; 4a → Q9 ; 4b (OH) étape de Q10, repli déclaré ; 4c → Q10. Données ajoutées à Q10 :
« فاصلة M وترتيبتها موجبتان » (lu sur la figure du sujet : légitime, sans quoi deux points
conviennent) et OM, MB (résultats officiels de 3d).

| Q | d | ma réponse (aveugle) | clé | verdict | motif |
|---|---|---|---|---|---|
| 1 | 2 | b | b | OK | plan 2×2 (relation × raison) ; « الترتيبة نفسها » cible exactement l'inversion abscisse/ordonnée ; « متوازيان » pour deux droites qui se coupent en B (remarque, cf. M-37-1, ici implicite) |
| 2 | 2 | d (2√5) | d | OK | trois étiquettes exactes |
| 3 | 2 | c (−2 ; 0) | c | OK | plan 2×2 (règle × point) ; « (2 ; 0) » = B elle-même |
| 4 | 2 | a | a | OK | plan 2×2 (centre × position relative), aucun vote |
| 5 | 2 | d (0 ; 2) | d | OK | plan 2×2 (somme/différence × moitié) ; la figure montre (AC) couper (OJ) à 2 unités : clé lisible |
| 6 | 3 | c (1/4) | c | OK | papillon de sommet M ((OJ) ∥ (AB)) ; plan 2×2 (5 muette) |
| 7 | 3 | a | a | **ERREUR de forme** | les trois distracteurs ont MB = MO/2, la clé seule MB = 2MO, et la figure montre MB ≈ 2MO ; c et d donnent en outre MO > OA (M-41-1) |
| 8 | 3 | b | b | OK | seule égalité vraie (4/5 + 16/5 = 4) ; plan 2×2 |
| 9 | 3 | c (4/5) | c | réserve | 8/5, 1 et 4 dépassent OM ≈ 0,89 : le contrôle du cours « العمودي أقصر من كلّ مائل » désigne la clé (m-41-2) |
| 10 | 3 | b (2/5 ; 4/5) | b | OK | plan 2×2 (inversion × BH pour OH) ; vote (4/5 ; 4/5) absent des options |

Clés fausses : 0 / 10. Égalités des explications recalculées (√20 = 2√5, (2√5/5)² = 4/5, (4√5/5)² =
16/5, (8/5) ÷ 2 = 4/5, 4/5 − 16/25 = 4/25, (4/5)√5, (1/5)·2√5, (5/4)·2√5 = 5√5/2) : justes ; chaque
mécanisme produit la valeur de son option. Coche ✓ toujours après la clé. Aucune clé strictement la
plus longue. Étiquettes `math.vec.*` : libellés sans vocabulaire vectoriel (coordonnées, distance,
milieu, symétrique) ✓.

Fuites : Q9 donne MH = 4/5, ordonnée de M, moitié de la clé de Q10 (étape officielle 4a → 4c :
décomposition, acceptable). En arrière, toutes nécessaires : Q2 « OAB قائم في B » (Q1), Q5 « C(−2 ; 0) »
(Q3) et « K منتصف [AC] » (Q4), Q7 « MJ/MB = MO/MA = 1/4 » (Q6) et « OA = 2√5 » (Q2), Q8–Q10 « OM, MB »
(Q7), Q9–Q10 « OMB قائم في M » (Q8).

Rendu : aucune chaîne brouillée ; « (O, I, J) » en tête de phrase arabe bien placé. Figures : 10,
vraies (unité 48,22 px en x et en y : repère orthonormé ; A(2 ; 4), B(2 ; 0), C(−2 ; 0), M(2/5 ; 4/5)
sur (OA) et (BJ), H pied de la perpendiculaire), aucune ne marque la clé, aucun débordement.
Vocabulaire : « معيّن متعامد ومتجانس » (terme du sujet) alors que le cours 12 dit « المعلّم » — usage
établi des missions publiées (08/16, 09/19, 09/27, 12/10–12) : remarque systémique, pas un défaut.

Étage : 5 vraies d3 sur 10 (papillon dans un repère, calcul de MO et MB, réciproque avec radicaux,
relation d'aire avec radicaux, coordonnées en trois étapes). **Challenge d4 honnête.**

Défauts 41 :
- **M-41-1 (majeur)** Q7 — marqueur de forme et contradiction avec la figure : b, c, d appliquent un même
  facteur à BJ et à OA, d'où MB = MO/2 dans les trois ; seule la clé a MB = 2MO, ce que la figure montre.
  Correctif :
  - b « MO = √5/2 ; MB = √5/4 » → « MO = √5/2 ; MB = 3√5/4 » (même méprise « partie sur tout » prise
    jusqu'au bout : MJ = √5/4 donc MB = 3√5/4 ; étiquette `thales-formes-melangees` conservée) ; deux
    options ont désormais MB > MO (a, b), deux MB < MO (c, d) ; longueurs 23/22/23/19 ;
  - explication : « الخطأ الشائع: اعتبار النسبة 1/4 حصّة من القطعة الكاملة فنجد MB = (1/4) × √5 و MO =
    (1/4) × 2√5 ، » → « الخطأ الشائع: اعتبار النسبة 1/4 حصّة الجزء الصغير من القطعة الكاملة فنجد MJ =
    (1/4) × √5 ومنه MB = √5 − √5/4 = 3√5/4 ، و MO = (1/4) × 2√5 = √5/2 ، ».
  - Reste (mineur, sans correctif imposé) : c et d donnent MO > OA = 2√5, que l'énoncé fournit.
- **m-41-2 (mineur)** Q9 — d « 4 » → « 2/5 » (OB × MH = (OM × MB) ÷ 2), étiquette
  `math.mes.aire-triangle-sans-moitie` ; explication : « فنكتب MH × MB = OM × OB ومنه MH = 1 ، أو MH × OM =
  MB × OB ومنه MH = 4 ؛ » → « فنكتب MH × MB = OM × OB ومنه MH = 1 ، وهو أطول من [OM] ، وهذا مستحيل لأنّ
  العمودي أقصر من كلّ مائل ؛ أو القسمة على 2 في أحد الحسابين فقط فنكتب OB × MH = (OM × MB) ÷ 2 ومنه
  MH = 2/5 ؛ » (vérifié : (8/5 ÷ 2) ÷ 2 = 2/5 ; 2/5 < OM ; rendu Chromium propre).
- Observation : Q2, Q5, Q9, Q10 — clé lisible à l'échelle.

Verdict partiel 41 : **10 questions, 0 clé fausse, 1 question à reprendre (Q7), 1 retouche mineure.**
