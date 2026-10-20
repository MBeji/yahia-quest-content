# Rapport — lot B5 (maths 6ᵉ) : 20, 21, 23 + neuf 25

Contrôles (depuis `/home/user/eng-deliver`) : `content:check` ✓ · `content:qa --subject math-6eme` 0 constat sur 20/21/23/25 · `content:figures:check` ✓ · `content:tranche --chapters 20,21,23,25 --fresh --strict-longest --strict-lessons` : clé strictement la plus longue 0/86, patron de notion 0 en recul, 0 groupe gabarit · prettier ✓ · rendu `renderLesson`/`renderSummary` des 4 cours + résumés ✓ (vitest jetable supprimé). Détail et table des écarts : `auteurs-notes/B5/NOTES.md`.

## Écarts trouvés et corrigés
- **20** : cours déjà complet ; manque : piège « oublier le ½ » du losange (tag sans distracteur). Exercices (6 q. × 5) = formules directes : jamais exercés losange, hauteur hors figure / côté oblique, unités agraires, dimension inconnue, soustraction d'aires, figures composées, problèmes à prix. +20 questions, 1 remplacée (04 Q5), 1 ancienne refaite (01 Q1).
- **21** : **couronne (M2) absente du cours** → section 9 (« الإكليل ») ; rayon retrouvé, demi-cercle/quart/trois quarts, contour du demi-disque, diamètre lu sur figure, problèmes multi-étapes jamais exercés ; doublon 04 Q3 = 05 Q6 remplacé. +19 questions.
- **23** : cours aligné ; exercices en formule directe (04 Q2 = 02 Q4, Q3 « نفس… »). Ajoutés : reconnaissance, patrons (valide/invalide, dé), arêtes cachées, boîte ouverte, solides accolés, lecture inverse, cm² → m² et prix ; volume ⛔ jamais demandé, dénombrement de cubes ◐ non repris.
- **25 (neuf)** : leçon 24 + critère مع 4 : 6 sections, 9 figures, quiz 5, 5 exercices à 6 questions.
- Aucune donnée fautive des errata reprise ; aucun ⛔ (volume, calcul littéral, 180°, Pythagore, aire à l'échelle).

## Questions remplacées / ajoutées
20 : +2 quiz, +3/+4/+3/+4 (+1)/+4 · 21 : +2 quiz, +3/+4/+3/+3 (+1)/+4, 5 anciennes refaites · 23 : +2 quiz, +3/+4/+3/+3 (+2)/+4, 4 anciennes refaites · 25 : 5 + 30. Aucun exercice > 12 questions ; en-têtes, id, ordre, étoiles intacts ; ajouts en fin de tri avec difficulté ≥ au maximum du fichier ; formats : `numeric` ×15, `multi` ×2.

## Reprises déclarées (`manuel`)
20/04 L38 ex. 1, L33 ex. 12, L41 ex. 5, L38 ex. 6 · 20/05 L2 ex. 1, L33 ex. 7, L33 ex. 3, L38 ex. 3 · 21/03 L20 ex. 6, ex. 9 · 21/04 L46 ex. 10, L20 ex. 8, L46 ex. 9, L20 ex. 11 · 23/04 L58 ex. 10, ex. 7 · 23/05 L58 ex. 7 · 25/02 ex. 4, ex. 5 · 25/04 ex. 2, ex. 9. Pour garder des questions sans doublon avec le cours, les nombres du cours ont été changés en 20, 21 et 23 (cf. notes).

## Chapitre neuf 25
`displayOrder` 25 (fin de sujet ; 26 = diagrammes). `manuel 102609 ص 67–69`, sources : fiche §2 octies/§3.2/§4, guide p.153 et T1 sit. 3. Section « المحيط على التصميم » : scale + arrondi par excès des lignes de clôture.

## Ids d'étiquettes proposés (aucun inventé dans les fichiers)
`math.mes.aire-cote-oblique-pris-pour-hauteur` (20 ; ≥ 4 q.) · `math.mes.aire-inconnue-moitie-oubliee` (20 : 36 ÷ 9 = 4 pour un triangle) · `math.mes.aire-composee-somme-au-lieu-de-difference` (20 : 396 et 69 آر) · `math.geo.aire-disque-inverse-carre-non-reconnu` (21 : 25 pour 5) · `math.geo.couronne-largeur-prise-pour-rayon` (21 et 25-cours) · `math.mes.perimetre-cote-commun-compte` (25 ; ≥ 8 q.) · `math.mes.perimetre-diametre-interieur-compte` (25 ; ≥ 6 q.) · `math.mes.arc-retranche-compte-en-moins` (25) · `math.mes.plant-ajoute-sur-cercle-ferme` (25) · `math.mes.echelle-unites-non-uniformisees` (déjà proposé par B3).

## Doutes pour l'auditeur
- 21 passe à **9 sections** (> ~8 notions, R-13) ; 02-boss Q5 « أيّ مقدار يخصّ القرص ؟ » reste ambiguë (non modifiée : question ancienne, id stable) — à remplacer si l'auditeur la juge fautive.
- **Fiche, §2 octies L24 ex. 7** : « 18,71 » est faux, la somme est 16,71. À corriger dans la fiche.
- 25/04 Q2 (L24 ex. 2) : le côté commun rectangle/carré non clôturé est une lecture de la fiche (« à confirmer au guide ») ; Q3 (ex. 9) : figure redessinée de 17 côtés (1 triangle, 5 carrés, 2 losanges, lecture R-7).
- Paires proches : 17 avant refonte, restent surtout des questions anciennes entre elles ; positions de clé biaisées vers b (42 %) car options numériques triées ; options « نعم/لا » conservées équilibrées 2/2.
- Anciennes figures de 20 (« 5 سم » en toutes lettres dans le dessin) non retouchées.

## Corrections après audit

Audit `audits/audit-B5.md` (0 bloquant, 13 majeurs, 23 mineurs) appliqué sur 20, 21, 23, 25 (exercices 01–05, quiz, cours, résumé, `chapter.json` ; missions 06+ non touchées, `sources[]` conservées).

- **Questions qui redonnent le cours** (18) : remplacées par de nouveaux énoncés et nombres (ch. 21 : 11, ch. 23 : 4, ch. 25 : 2, ch. 20 : 1). Doublons et miroirs réécrits. Quatre corrections de cours/résumé (trois `::: verifie` du ch. 21, puce « القطر » du résumé). Ch. 21 `02-boss` Q5 remplacée ; quiz Q6 reprise.
- **Compétences** : `competencies` ajoutées aux ~105 questions neuves, alignées sur les ch. 01–19 (`math.mes.aires`, `math.geo.cercle`, `math.esp.cube-pave`, `math.mes.perimetres`).
- **Étiquettes (décisions du pilote)** : côté commun / diamètre compté → `math.mes.perimetre-segment-interieur-compte` (options et `coursePitfalls` du ch. 25) ; rouleaux → `math.num.reste-ignore-dans-le-probleme` ; arc creusé → `math.mes.arc-retranche-compte-en-moins` ; plant de trop → `math.mes.plantations-ferme-et-ouvert-confondus`. `math.mes.volume-utilise-comme-aire` et `math.mes.rayon-non-eleve-au-carre` non utilisées en 6ᵉ (options muettes, retirées des `coursePitfalls`).
- `manuel` retiré de `23/05-entrainement` ; messages de clôture des ch. 21 et 23 corrigés ; rappel « علب كاملة » ajouté au cours 23 (arrondi du 04 Q8) ; explication du distracteur 33,72 corrigée (25 / 02 Q5).
- **Contrôles finaux** : `content:check`, `content:qa` (aucun constat sur le lot), `content:figures:check`, prettier : verts. Tranche avec et sans `--fresh` : aucune paire ≥ 0,6 dans 01–05/quiz du lot (restent seulement des missions 06+/07/08, hors périmètre). Recouvrement cours/questions (`overlap.py`) : nul.
- **Doutes / résidus** : (1) clé strictement la plus longue sur 5 questions numériques (20/05#1, 21/02-boss#4, 21/04-defi#2, 21/05#2, 23/01#1) : artefact de longueur de nombres/unités, 3 % contre 25 % au hasard, laissé tel quel ; (2) 21 `02-boss` Q6 laissée en difficulté 3 pour ne pas décaler les identifiants ; (3) erreur de la fiche : L24 ex. 7 « 18,71 » devrait être 16,71 (non reprise).
