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
  interdit, arabe seulement dans `<title>`, aucun débordement du `viewBox` (boîte englobante
  mesurée dans Chromium). 80 lignes de formule seule : toutes acceptées par `isDisplayEquation`.
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
