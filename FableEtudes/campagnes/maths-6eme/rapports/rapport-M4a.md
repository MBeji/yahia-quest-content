# Rapport — lot M4a (maths 6ᵉ) : 19 (2 missions de devoir) + 20 (4 missions d'examen)

Partie 25 de la carte M4 : non touchée. 6 fichiers, 50 questions, 2 `chapter.json` (une ligne de `sources[]` chacun). Aucun fichier de 01–05 touché.

## Vérification 🔁 de B5 (chapitre 20)
Rapport B5 relu ; cours (9 sections) et exercices 01–05 du 20 relus en entier : les 5 exercices sont à 9–10 questions et leurs indices (`02-boss#4/#8/#10`, `04-defi#2/#4/#5/#7/#9`, `05-entrainement#5/#7/#10`, `quiz#7`, `03-revision#7/#8`) correspondent à ce que la carte annonce. Plus grand `NN` des dossiers `exercices/` au lancement : 05 (19 et 20) ; 25 est à l'autre auteur. Aucune mission ne reprend une question de ces listes (voir « paires proches » : 0 au gate). Ce qui a été évité : conversion m² → ha ou ha → m² seule (`03#7`, `05#6/#7`) fondue dans une question à plusieurs étapes ; trapèze par somme des bases seule (`02#4`, `04#2/#4`) remplacé par lecture d'orientation (2013) ou hauteur retrouvée (2025) ; hauteur retrouvée `04#9` (grande base) ≠ 2025 (hauteur) ; exemples et `verifie` du cours (trapèze 9/4/3, plaque 24 × 10, 80 × 60 − 20 × 20) non repris.

## Fichiers
| fichier | étage | q. | régime |
| --- | --- | ---: | --- |
| `19/exercices/06-devoir-construire-trapeze-rectangle-et-losange.json` | d3 boss 120/30 | 7 | devoir (salle blanche) |
| `19/exercices/07-devoir-construire-avec-un-angle-donne.json` | d3 boss 120/30 | 7 | devoir (salle blanche) |
| `20/exercices/06-exam-2025-p2-voilier-en-cuivre-et-carre.json` | d3 boss 120/30 | 8 (carte : 9) | examen |
| `20/exercices/07-exam-2018-p3-terrain-carre-parallelogramme-triangle.json` | d3 boss 120/30 | 10 (carte : 12) | examen |
| `20/exercices/08-exam-2013-p3-ferme-orangers-triangle-trapeze.json` | d3 boss 120/30 | 9 (carte : 10) | examen |
| `20/exercices/09-exam-2012-p3-trapeze-au-1-sur-500-emprunt.json` | d3 boss 120/30 | 9 (carte : 11) | examen |

`displayOrder` 6 à 9 (19 : 6–7). Formats : mcq, numeric, ordering (19/06 ×2, 19/07 ×1, 20/07 ×1) ; pas de `short_answer` ni de `multi`. Nombres de questions plus bas que la carte : les étapes « QCM + numérique d'une même valeur » ont été fondues (une question avec distracteurs plutôt que deux) ; tous les problèmes sont repris en entier, dans l'ordre du sujet.

## Problèmes repris (vérifiés au PDF officiel : figures 2025, 2018, 2013, 2012)
Toutes les valeurs recalculées par script : 2025 P2 (12 − 1,56 = 10,44 kg → 5800 cm² → 145 % → 4000 cm² ; petite base 60, hauteur 40 ; 30 < 40 et 30 < 60) ; 2018 P3 (43 750 + 87 500 + 125 000 = 256 250 m² = 25,625 ha ; 1,35 × 90 740 = 122 499 ; loyer 22 685 ; plan 6 / 3,5 / 2,5 cm au 1/10 000, CN = 350 + 250 = 600) ; 2013 P3 (15 000 + 25 000 = 40 000 m² = 4 ha ; 1 000 arbres ; 70 000 kg ; 24 500 d ; net 16 000 d) ; 2012 P3 (42, 68, 30 m ; 1 650 m² = 16,5 a ; 39 600 d ; 138 600 d ; total 178 200 ; 12,5 %). Chaque question dit sa session et redonne ses données ; les figures (voilier, terrain 2018 avec marques d'égalité et angle droit en N, ferme 2013, plan 2012) sont redessinées en SVG avec les cotes imprimées sauf le voilier (aucune cote, comme au sujet ; proportions vraies 140 / 60 / 40 ; position du mât au milieu non imprimée : dessinée, non affirmée).

## Données données dans l'énoncé / admises
- Aucun item hors programme ni illisible dans ces quatre problèmes ; aucun Pythagore (2018 : SN = AN par les diagonales du carré ; 2013 : le triplet 150-200-250 n'est jamais utilisé).
- Décision E-4 : ne me concerne pas (2026 P3 est au 25).
- Chaque étape qui suit un résultat intermédiaire reçoit ce résultat comme donnée (précédent M2 : 14/06) : 10,44 kg, 5800, 145 %, 40 et 60 (2025) ; 43 750, 87 500, 1,35, 90 740 (2018) ; 15 000, 25 000, 1 000, 70 000, 24 500 (2013) ; 138 600, 39 600 (2012). Les titres ne donnent aucune clé.

## Adaptations des missions de devoir (◐ / programme)
- 19/06 : « somme et différence des bases » (D04#4a) **non repris** (◐, décision E-7) : la grande base est donnée « plus longue de moitié » (1 question numérique), le côté oblique est donné (5 dm) et placé au compas, sans Pythagore.
- 19/07 : « losange depuis une diagonale et un angle » **adapté** en losange par son côté et l'angle ∠ADC (la bissectrice/isocèle de la diagonale n'est enseignée nulle part avant ce chapitre) ; le carré sur un côté, les lectures d'échelle (triangle 40 m / 30 m, 1/1000, l'angle reste 70°) et le triangle rectangle isocèle sont repris. La somme des angles d'un triangle n'est jamais demandée.

## Étiquettes
Employées (toutes au registre) : `math.mes.aire-trapeze-sans-demi-somme`, `aire-division-par-deux-appliquee-a-tort`, `aire-et-perimetre-confondus`, `conversion-aire-facteur-errone`, `math.num.chiffres-juxtaposes-au-lieu-du-produit`, `operation-inverse-appliquee`, `produit-decimales-mal-comptees`, `virgule-perdue-dans-le-resultat`, `math.prop.pourcentage-base-erronee`, `pourcentage-recopie-comme-resultat`, `math.frac.numerateur-denominateur-inverses`, `math.geo.condition-suffisante-supposee`, `diagonales-proprietes-mal-attribuees`. Aucune sur ordering/multi ; options à deux erreurs laissées muettes.
Jugements à contrôler par l'auditeur : `pourcentage-base-erronee` (2025 Q4 : pourcentage posé sur le total au lieu de la pièce ①, libellé écrit pour « prix de départ ») ; `numerateur-denominateur-inverses` (2012 Q6 : 39 600 ÷ 7 × 2 au lieu de ÷ 2 × 7) ; `operation-inverse-appliquee` pour × au lieu de ÷ par l'échelle (précédent 14/10).
**Identifiants manquants** (rien n'a été inventé) : « échelle appliquée sans uniformiser m/cm ou en sens inverse » (19/06 Q5, 19/07 Q5, 20/07 Q9, 20/09 Q1 : ≥ 4, déjà proposé par B3 sous `math.mes.echelle-unites-non-uniformisees`) ; « côté oblique ou hypoténuse pris pour hauteur » (20/08 Q1) ; « carré comparé à une base sans la hauteur » (20/06 Q7–Q8) ; « côté oblique placé sans reporter sa longueur au compas » (19/06 Q4) ; « angle posé au mauvais sommet » (19/07 Q1, aussi à déclarer) ; « prix à l'are multiplié par l'aire en m² » (20/09 Q5) ; « aire multipliée par la production d'un arbre » (20/08 Q6).

## Doutes pour l'auditeur
- 19/06 Q6 et 20/06 Q8 : options « nous disons oui/non + raison » (une seule justification valide et suffisante ; les raisons fausses portent une prémisse fausse ou une inférence invalide) ; à relire pour la règle « une seule réponse défendable ».
- 20/06 Q7 : la comparaison « hauteur et petite base » est un critère suffisant (énoncé : « pour nous assurer »), pas nécessaire ; l'explication le dit ainsi.
- 20/07 Q10 : classement des 4 étapes d'une conversion à l'échelle (pas de construction détaillée : le trapèze rectangle est déjà ordonné en 19/06 Q2).
- Rendu : aucun navigateur dans la session, les SVG n'ont pas été vus ; coordonnées recalculées (angles, rapports 40/30, 7/3).
- Notation : tous les nombres à milliers portent U+00A0 (le gate `content:qa` l'exige) ; la valeur clé d'une `numeric` à 4+ chiffres est écrite sans groupement une fois dans l'explication pour que « valeur canonique reprise » passe.

## Gates (depuis `/home/user/eng-deliver`, sur mes 6 fichiers + 2 chapter.json)
`content:check` ✓ · `content:qa --subject math-6eme` 0 erreur (5 avertissements restants : 14, 16 ; aucun de mes fichiers) · `content:figures:check` ✓ · `content:tranche --chapters 19,20 --fresh --strict-longest` : clé strictement la plus longue 0/75, positions de clé a 19 · b 21 · c 17 · d 18, paires proches 0, patron de notion 0 en recul · `lot-lint.mjs` rien à signaler (6 fichiers) · `content:gisement:controle` (19/06, 19/07) : 0 plage de 8 mots, 0 exercice source à 3 données · prettier ✓.

## Corrections après audit (audit-M3-M4.md, parties 19 et 20)
Fichiers regénérés (état relu avant : rien n'était appliqué) ; seuls 19/06–07 et 20/06–09 ont changé.
- **M-8** 19/06 : Q2 (ordre du trapèze rectangle) et Q7 (ordre du losange) supprimées → 5 questions (la hauteur 4 dm inutile de Q3 retirée). Le doublon avec 25/09 Q9 disparaît.
- **M-11** 19/07 : Q6 (angle à l'échelle) supprimée → 6 questions ; Q5 : l'option « 0,4 سم و 0,3 سم » est maintenant expliquée.
- **M-10** 20/06 : Q7 supprimée → 7 questions ; Q8 : options b et d et explication aux textes de l'audit (b étiquetée `condition-suffisante-supposee`), plus aucune mention d'un rétrécissement « en haut » ; figure : `و` et ① déplacés.
- **M-9** 20/08 Q6 : option « 1 070 كغ » et explication « يجمع 1 000 و 70 بدل أن يضربهما ».
- **M-14** 20/09 Q6 : étiquette `math.prop.pourcentage-base-erronee` ; explication « هي مصاريف التهيئة والتجهيز » (mineur).
- **M-12/M-13 figures** : plus d'isolat LTR sur les cotes nombre + unité (la fonction de dessin ne l'applique qu'aux nombres nus et aux lettres seules), halo blanc sur tous les textes ; 20/09 : « 6 سم » à x = 82 ; 20/07 : « 250 م » supprimé, `ب` et `ن` déplacés, « 350 م » replacé à gauche de [ب ج] hors des repères d'égalité. Les 11 figures ont été rendues dans Chromium (`/opt/pw-browsers`, page `dir=rtl`, 360 px) et relues : cotes dans le bon sens, aucune étiquette coupée ni barrée.
- Mineurs laissés tels quels : 19/06 Q1 (redit une phrase du cours, assumé : la mission garde 5 questions), 19/07 Q4 (d1 réel, la rampe oblige à la garder en d3), 20/07 Q10.
- Totaux : 19/06 5 q., 19/07 6 q., 20/06 7 q., 20/07 10 q., 20/08 9 q., 20/09 9 q. (aucune mission sous 5).
- Gates : `content:check` ✓ ; `content:qa` 0 erreur (5 avertissements hors lot) ; `content:figures:check` ✓ ; `content:tranche` 19+20 : paires proches 0 (la seule clé « la plus longue » du bilan est `20/05-entrainement#1`, B5, hors lot) ; `lot-lint` rien sur mes 6 fichiers ; `content:gisement:controle` 19/06–07 : 0 plage ≥ 8 mots ; prettier ✓.
