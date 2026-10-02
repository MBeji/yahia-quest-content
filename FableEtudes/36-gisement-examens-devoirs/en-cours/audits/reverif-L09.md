# Re-vérification ciblée — tranche L09 (ch.12, missions 16 à 21), après application de l'audit

Arbre de travail tel quel ; registre lu sur `origin/main` ; rendu jugé avec `bidi.ts` d'arena `origin/main` (Chromium `dir=rtl`).
Aucun fichier du dépôt modifié.

**État : TERMINÉ.** Moteur : `bidi.ts` d'arena `origin/main` = dc19a816 (#1150 mergé ; identique au clone `/home/user/eng-gisement`).

## Avancement

- [x] Inventaire des changements (diff contre la version auditée) et étiquettes (64 placements)
- [x] 16
- [x] 17
- [x] 18
- [x] 19
- [x] 20
- [x] 21
- [x] Synthèse

## Inventaire

- **Textes** : comparés un à un à la version auditée. Seuls ont changé, comme déclaré : 18 Q3 (explication), 20 Q4 (option c + explication), 20 Q6 (explication), 21 Q4 (explication), 21 Q5 (énoncé + figure), 21 Q6 (option d + explication), 21 Q7 (énoncé, quatre options, explication). En-têtes, titres, `displayOrder`, rampes et ordre des questions inchangés.
- **Clés** : 31/31 inchangées (a 8 · b 9 · c 7 · d 7). Les 7 questions réécrites ont été re-résolues à l'aveugle avant lecture des clés (18 Q3 c, 20 Q4 a, 20 Q6 c, 21 Q4 b, 21 Q5 d, 21 Q6 c, 21 Q7 a), contrôle par script : toutes conformes.
- **Étiquettes** : 93 distracteurs, **64 étiquetés (32 distinctes), 29 muets**, aucune clé étiquetée ; les 32 étiquettes sont sur `origin/main` et dans l'arbre. Les deux étiquettes nouvelles (`math.vec.symetrie-regle-confondue`, `math.prop.pourcentage-base-erronee`) ne sont pas encore au registre : leurs 8 options cibles sont bien muettes, prêtes pour la pose à la livraison.
- **Rendu** : les 186 champs rendus comme le player (Chromium 141, `dir=rtl`) puis comparés à un rendu de référence : 0 écart d'ordre, 0 ligne de formule seule refusée ; chaque chaîne changée relue ligne par ligne à 340 px : aucune brouillée (les longues formules de corrigé passent à la ligne par conception du moteur, dans le bon ordre). Balayages : 0 chiffre indo-arabe, LaTeX, `$`, virgule arabe en crochet, nombre coupé, tiret-moins, lettre d'option, radicande arabe ; ✓ jamais après un distracteur.

## 16 — RAS

Textes inchangés. Étiquettes ajoutées, chacune exacte : 16 Q1 a « لأنّ 3 < 6 » et b « لأنّ 12 > 3 » → `comparaison-radicaux-partie-par-partie` (coefficients seuls / radicandes seuls) ; 16 Q3 b → `produit-signes-negatifs` (−√5 × √5 pris pour +5, mécanisme écrit dans l'explication). Pose prévue à la livraison : 16 Q4 b « 33,3 % » (50 ÷ 150) → `pourcentage-base-erronee`, exacte ; 16 Q4 d « 133,3 % » (200 ÷ 150) → même étiquette, acceptable (base = nouveau prix ; le numérateur est aussi décalé, mais la base fautive est l'erreur nommée).

## 17 — RAS

Textes inchangés. 17 Q1 d « 1 + √2 » → `moins-devant-parenthese` (seul le signe de √2 changé), exacte ; 17 Q3 d « −5x − 1 = 9 » → `produit-signes-negatifs` (−5 × 2 pris pour +10), exacte.

## 18 — RAS

18 Q3 : explication réécrite = le texte vérifié à l'audit, mot pour mot ; égalités justes (√2 × (−√2) = −2 ; −2 + 2 = 0 ; les deux erreurs sont présentées comme telles, « اعتبار … = +2 », « جمع … بدل ضربهما ») ; ✓ après « −2 + 2 = 0 » ; rendu correct ligne à ligne. Étiquettes : a → `produit-signes-negatifs` (exacte : la phrase nomme √2 × (−√2) = +2) ; b → `operation-inverse-appliquee` (exacte : « une somme au lieu d'un produit », phrase ajoutée). Pose prévue : 18 Q2 b « (−3 ; −5) » (règle de O) et c « (−3 ; 5) » (règle de (OJ)) → `symetrie-regle-confondue`, exactes ; 18 Q4 c « 60 % » (15 ÷ 25) → `pourcentage-base-erronee`, exacte.

## 19 — RAS

Fichier identique à la version auditée (texte, clés, étiquettes ; relu après sa date de modification 15:14 de la veille).

## 20 — RAS

- **Q4** (re-résolue à l'aveugle : a, vrai — milieu (0 ; 0) = O). Nouvelle option c « خطأ ، لأنّ منتصف [AB] هو (0 ; 3) » : fausse sous les données (le milieu est (0 ; 0)), ne nie aucune prémisse, n'est plus une extrémité du segment ; verdicts toujours 2/2 ; longueurs a 47, b 36, c 32, d 66 : clé non la plus longue. Étiquette `signe-ignore-dans-somme` exacte ((3 + (−3))/2 calculé (3 + 3)/2 = 3). Explication : la phrase remplacée est juste (« ((2 + (−2))/2 ; (3 + 3)/2) = (0 ; 3) ») ; ✓ toujours après « النقطة O » ; rendu correct (la formule de 35 signes passe à la ligne dans le bon ordre). **Q4 b laissé muet (écart de l'auteur) : d'accord** — le libellé de `symetrie-centrale-un-seul-signe` dit « c'est un symétrique par rapport à un axe », ce qui est faux ici (B est bien le symétrique de A par O) ; l'option reste muette.
- **Q6** (re-résolue : c, x = 2). Explication = le texte vérifié : l'équation est seule sur sa ligne (bloc `.math-equation`), « 3x = 6 », « 3x = 0 », « 2x + x = 3 », « 3x = 3 » justes, ✓ après « = 2 » ; rendu correct (et, avec #1150, l'ancien texte ne serait plus brouillé non plus).
- Étiquettes ajoutées : Q1 a « 2 » → `reponse-a-l-autre-inconnue` (exacte : arrêt au résultat intermédiaire √2 × √2) ; Q1 d « 8 » → `racine-et-carre-confondus` (racine abandonnée : (√2)³ lu 2³) — approchée, mais conforme à l'usage publié de cette étiquette pour « racine oubliée » (02/01 Q4, option « 36 » = 3 × 12 sans la racine) : acceptée ; Q2 d → `moins-devant-parenthese` (exacte) ; Q3 a et d → `comparaison-radicaux-partie-par-partie` (exactes) ; Q5 a « 8,8 » → `numerateur-denominateur-inverses` (exacte : 22 × 100/250, rapport 250/100 retourné) ; Q5 c « 44 » → `reponse-a-l-autre-inconnue` (huile des 200 kg, résultat partiel, comme 33 : acceptée).

## 21 — RAS (résiduels mineurs notés, sans correctif)

- **Q4** (re-résolue : b, P(−3/2 ; −2)). Explication avec le point E : juste (O milieu de [ME] ⟹ E(−3/2 ; −2) = P), ✓ après « النقطة P », E n'est employé nulle part ailleurs ; rendu correct.
- **Q5** (re-résolue : d, (3/2 ; −2)). Règle retirée de l'énoncé. Figure relue dans le SVG : `viewBox` 0 0 280 284, unité 44 px, O (96 ; 168), I (1 ; 0), J (0 ; 1), M (162 ; 80) = (3/2 ; 2) ; quadrillage jusqu'à y = −2,3, ligne y = −2, graduation « −2 » ; tout dans le `viewBox` ; arabe seulement dans `<title>` ; après DOMPurify (configuration de `figure.ts`) en page `dir=rtl`, « −1 » et « −2 » restent intacts ; **Q n'est pas tracé, aucune option n'est marquée : la figure ne donne pas la clé**, elle donne le quadrillage pour construire Q, comme le 2a officiel « أُرسم النقطة Q ». Résoluble avec des notions enseignées (symétrie axiale, 7ᵉ ch.09 ; (OI) se lit sur la figure, I y est placé). **Vrai d2** (construire le symétrique, puis lire ses coordonnées), et ce n'est plus le gabarit de 18 Q2 : 18 Q2 teste l'identification « (OI) = axe des abscisses » avec les règles données par nom d'axe, 21 Q5 la construction sur figure. Les pièges et l'explication restent ceux de toute question de symétrique, ce qui n'en fait pas un doublon. Pose prévue : Q5 b « (−3/2 ; −2) » et c « (−3/2 ; 2) » → `symetrie-regle-confondue`, exactes.
- **Q6** (re-résolue : c, (0 ; 0)). Option d « (3/2 ; −2) » fausse sous les données ; étiquette `milieu-difference-au-lieu-de-somme` exacte ((xQ − xN)/2 = 3/2, (yQ − yN)/2 = −2) ; a « (3/2 ; 0) » → `reponse-a-l-autre-inconnue` (milieu d'un autre segment : acceptée). Vote par composante : x à égalité (3/2 deux fois, 0 deux fois), y → 0, soit a ou c ; les seules relations linéaires (a = b + d) ne lient que des distracteurs ; clé non la plus longue. Explication juste (« ((3/2 − (−3/2))/2 ; (−2 − 2)/2) = (3/2 ; −2) ، وهي النقطة Q نفسها ») ; ✓ après « النقطة O ». *Résiduel mineur, sans correctif* : en route quête, l'élève qui vient de trouver Q(3/2 ; −2) en Q5 reconnaît d comme Q et peut l'écarter ; le vote sur a, b, c redonne alors (0 ; 0). Aucun jeu d'erreurs naturelles n'y échappe (essai par script lors de l'audit), et quiconque connaît Q et N calcule ce milieu immédiatement : acceptable.
- **Q7** (re-résolue : a). Fidèle au 3) officiel ; données M, N, P et Q = S(OI)(M) inchangées. Résoluble avec des techniques enseignées ou données : critère des diagonales qui se coupent en leur milieu et « parallélogramme + angle droit = rectangle » (8ᵉ ch.08, non rappelés : à bon droit) ; parallèle aux axes et règle de (OI) donnés ; angle droit par parallèles aux axes perpendiculaires (7ᵉ ch.10). Plan 2×2 effectif : « متناصفان » (a, c) contre « يمرّ بمنتصف » (b, d), deux côtés (a, b) contre un seul (c, d) ; chaque composante apparaît deux fois, donc ni vote ni union ne désigne a. Prémisses toutes vraies (O est bien sur [NQ], [MN] est bien parallèle à un axe), seule a est un raisonnement valide. Longueurs a 151, b 158, c 127, d 134. Explication ajustée par l'auteur : juste de bout en bout (milieux (0 ; 0), (MN) ∥ (OI), (NP) ∥ (OJ), angle droit en N), ses deux « الخطأ الشائع » décrivent exactement b et c, ✓ après « مستطيل ». Étiquettes b et c → `condition-suffisante-supposee`, libellé élargi sur `origin/main` depuis l'audit (eb8ca731 : « Tu prends une seule propriété pour une preuve : il faut toutes les conditions — par exemple, … il leur faut aussi le même milieu ») : b exacte (l'exemple même : un seul passage par le milieu au lieu du même milieu), c désormais exacte par la tête du libellé (une seule parallèle prise pour l'angle droit). Rendu correct ligne à ligne.
- **Fuites de la chaîne en ordre inverse (donjon)** : celles des énoncés et des options vers Q3, Q4 et Q6 sont **levées**. Les options de Q7 ne citent plus O ni (OI), donc plus « O منتصف [MP] » (Q4) ni « (MN) ∥ (OI) » (Q3). « متناصفان » n'indique plus O : il faut calculer un milieu pour Q6. Pour Q4 ne reste qu'un indice de nommage : l'énoncé de Q7 donne N(−3/2 ; 2) et P(−3/2 ; −2), qui sont les options a et b de Q4 (noms officiels), sans dire lequel est le symétrique par O : 2 sur 4, plus faible que le calcul direct (définition rappelée). Restent aussi, inhérents à la chaîne et sans correctif demandé : l'énoncé de Q3, qui pose « M و N متناظرتان بالنسبة إلى (OJ) », livre la moitié de Q2 ; les explications de Q6 et Q7, montrées après la réponse, contiennent Q(3/2 ; −2) (clé de Q5) et le milieu O (clé de Q6).
- Autres étiquettes ajoutées : Q2 c « النقطة O فقط » → `symetrie-centrale-un-seul-signe`, exacte (N, symétrique par (OJ), pris pour le symétrique par O : ici le libellé est vrai) ; Q3 c → `perpendiculaire-et-parallele-confondus`, acceptée. Pose prévue : Q2 a « المستقيم (OI) فقط » → `symetrie-regle-confondue`, exacte (règles de (OI) et (OJ) intervertues).

## Synthèse

| Fichier | Textes changés re-vérifiés | Étiquettes | Verdict |
|---|---|---|---|
| 16 | — | 3 ajoutées, exactes ; 2 poses prévues exactes/acceptée | RAS |
| 17 | — | 2 ajoutées, exactes | RAS |
| 18 | Q3 (explication) | 2 ajoutées, exactes ; 3 poses prévues exactes | RAS |
| 19 | — (inchangé) | — | RAS |
| 20 | Q4 (option c, explication), Q6 (explication) | 8 ajoutées : 6 exactes, 2 acceptées (Q1 d, Q5 c) ; Q4 b laissé muet (d'accord) | RAS |
| 21 | Q4, Q5 (énoncé + figure), Q6 (option d, explication), Q7 (énoncé, options, explication) | 6 ajoutées : 4 exactes, 2 acceptées (Q3 c, Q6 a) ; 3 poses prévues exactes | RAS (résiduels mineurs notés) |

**Bilan : 7 questions réécrites re-résolues à l'aveugle, 0 clé fausse, 0 défaut introduit, 0 correctif à faire. 64 étiquettes posées revues contre le registre d'`origin/main` (65b25590, = distant) : aucune inexacte. Les 21 ajoutées : 17 exactes, 4 acceptées (20 Q1 d, 20 Q5 c, 21 Q3 c, 21 Q6 a). Les 43 autres : options inchangées, libellés inchangés depuis l'audit (registre comparé de 4f72f94b à 65b25590 : seul `condition-suffisante-supposee` a changé, élargi, ce qui renforce 21 Q7 b et c ; `milieu-difference-au-lieu-de-somme` y est entré), toutes relues : exactes ou acceptées comme à l'audit. Poses prévues des deux étiquettes nouvelles (absentes du registre, options cibles muettes) : 8, dont 7 exactes et 1 acceptable (16 Q4 d). Rendu : rien ne reste brouillé avec `bidi.ts` d'`origin/main` (dc19a816).** Tranche livrable, avec les deux étiquettes nouvelles à créer au registre avant leur pose.
