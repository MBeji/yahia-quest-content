# Notes auteur — lot B5 (20, 21, 23 + neuf 25)

> Ordre de travail : 20 → 21 → 23 → 25. Sources de base des mises à niveau : état du dépôt au commit
> `802e18a1` (avant B5) ; les scripts de génération des exercices sont jetables (scratchpad).

## 20-aires-polygones

### Table des écarts (avant)
- Cours (617 l., 9 sections) déjà aligné sur la fiche : unités (agraires, dam²/hm²), hauteur (hors figure, une hauteur ne sert qu'avec SA base), triangle, parallélogramme, losange (aire par diagonales ou côté × hauteur), trapèze, dimension inconnue (erreur d'أمل), figure composée (somme et différence). Un seul manque de cours : le piège « on oublie le ½ du produit des diagonales » (tag `math.mes.aire-losange-sans-moitie`, aucun distracteur ne le portait).
- Exercices et quiz **très en retrait** du cours : 5 exercices à 6 questions chacun, quasi uniquement « formule directe » (carré, rectangle, triangle, trapèze). Jamais exercés : losange (0 question), hauteur hors figure, côté oblique ≠ hauteur, parallélogramme avec côté oblique donné, unités agraires (une seule conversion par exercice) et dam²/hm², dimension inconnue (0), soustraction d'aires (0), figure composée (une addition triviale de deux aires données), problème à prix, triangle rectangle (ses côtés de l'angle droit comme base et hauteur), comparaison de deux parallélogrammes de mêmes base et hauteur.
- Défauts : 04-defi Q5 (« 30 + 9 = 39 », d3 pour une addition de deux aires données) ; plusieurs figures portent « 5 سم » en toutes lettres dans le dessin (non repris, laissé : lisible, pas d'erreur).
- Errata §6.1 (n° 38–40, 51–55, 57, 59) : aucune donnée fautive dans le chapitre ; aucune reprise de 2 500 / 2 000 (n° 54, Q-E1) ; L50 ex. 4 et 8 (lecture incertaine, incohérence) non repris.
- ⛔/◐ : aucun volume, aucun calcul littéral, aucune échelle sur les aires (◐), aucun 180°, aucun Pythagore (la hauteur d'un triangle isocèle est toujours donnée).

### Fait
- Cours : un second `> ⚠️` dans la section du losange (« 80 × 60 = 4 800 », nommé, expliqué, corrigé) ; `coursePitfalls` + `math.mes.aire-losange-sans-moitie` (porté par 2 distracteurs). Résumé : une phrase ajoutée au losange.
- Quiz 5 → 7 : hauteur lue sur une figure (4 segments, un seul perpendiculaire — figure sans marque d'angle droit pour ne pas fuir la clé), losange.
- Exercices : +3 / +4 / +3 / +4 (+1 remplacée) / +4 questions ; en-têtes, id, ordre et étoiles intacts ; questions ajoutées en fin de tri avec une difficulté ≥ au maximum du fichier (01 : d2 ; 02–05 : d3).
- 04-defi Q5 (d3) remplacée à sa place par une figure composée rectangle + triangle (hauteur donnée, côté oblique 10 dessiné comme leurre).
- Reprises déclarées (`manuel`, mêmes données) : 04-defi ← L38 ex. 1 (maison carrée, 51 دكم²), L33 ex. 12 (périmètre 320 m, 1 600 m²), L41 ex. 5 (trapèze, grande base 6 m), L38 ex. 6 (cerf-volant 25/24, 600 سم²) ; 05-entrainement ← L2 ex. 1 (1,07 كم² = 107 هكتار), L33 ex. 7 (équilatéral 18/5,2 → 15,6), L33 ex. 3 (côté 4, hauteur 3,5 sur un autre côté : calcul impossible), L38 ex. 3 (156 / 20,8 → 7,5).
- chapter.json : source ajoutée (fiche §2 septies, §3.2, §4).
- Ids d'étiquettes proposés (distracteurs laissés muets) : voir le rapport.

## 21-cercle-disque

### Table des écarts (avant)
- Cours (539 l., 8 sections) fidèle à la leçon 20 et à la leçon 46 (centre/rayon/« الشعاع », diamètre lu sur la figure, cercle ≠ disque, π découvert par le tableau des boîtes — sans la coquille 92,4 —, périmètre, aire, choix périmètre/aire, demi-cercle, quart, trois quarts, contour du demi-disque, rayon retrouvé comme cas limite). **Manque M2 : l'aire de la couronne (الإكليل) n'était enseignée nulle part** (le fiche §3.2 la fait passer de ⛔ à ✅ : objectif de la مذكرة 46, ص 135 ex. 10).
- Exercices et quiz : formules directes seulement (diamètre, π, périmètre, aire). Jamais exercés : rayon retrouvé depuis le périmètre ou l'aire (0), demi-cercle / quart / trois quarts (0), contour du demi-disque, couronne (0), diamètre lu sur une figure (cercle dans un carré, deux cercles dans un rectangle), problèmes à plusieurs étapes (aiguille, roue, échelle), position d'un point par rapport à la circonférence.
- Défauts : 04-defi Q3 identique à 05-entrainement Q6 (disque de rayon 4 → 50,24, mêmes options) → remplacée ; 02-boss Q5 (« أيّ مقدار يخصّ القرص ؟ » avec « المحيط فقط » / « نصف القطر فقط » comme distracteurs) est ambiguë — le disque a un rayon et sa propre circonférence ; **non modifiée** (identifiant stable, remplacement non demandé à ce stade) : signalée à l'auditeur.
- Errata §6.1 (n° 21 « قوس هذه الدائرة », n° 22) : le chapitre n'a pas repris le « الجزء الملوّن » ; la coquille 92,4 du tableau de la leçon 20 (94,2) n'est pas reprise ; π n'est jamais écrit 3,41 hors distracteur.
- ⛔/◐ : pas d'angle au centre, pas de secteur quelconque (seulement demi, quart, trois quarts : fractions simples du tout), pas de racine carrée (r × r reconnu par un carré parfait : 25 = 5 × 5, 36 = 6 × 6, 49 = 7 × 7, 900 = 30 × 30), pas de volume.

### Fait
- Cours : **section 9 « الإكليل — قرصٌ كبير ناقصٌ قرصٌ صغير »** au patron (ancrage : la nafoura et la place, 6 m et 4 m ; figure de couronne à deux rayons étiquetés ; exemple 113,04 − 50,24 = 62,8 m² vérifié par 3,14 × (36 − 16) ; piège « la largeur du chemin n'est pas un rayon » 3,14 × 2 × 2 = 12,56 m² ; propriété + cas limite sens inverse R = 10 m, ring 200,96 m² → r = 6 m ; vérifier : piscine 5 m, margelle 2 m → 75,36 m²). Résumé : une puce. Épilogue 🏆 ajusté. chapter.json : description et source (fiche, مذكرة 46).
- **Le chapitre passe à 9 sections (> ~8 notions de course-explanation R-13)** : à signaler en curriculum (scinder « محيط الدائرة » / « مساحة القرص » ? non proposé : les deux se répondent).
- Quiz 5 → 7 (couronne, longueur d'un demi-cercle). Exercices +3 / +4 / +3 / +3 (+1 remplacée) / +4.
- Reprises déclarées : 02 : aucune reprise (la question « aire → rayon » est une variante, 153,86 → 7, donc sans `manuel`) ; 03 ← L20 ex. 6 (deux cercles dans un rectangle de hauteur 5), L20 ex. 9 (aiguille 25 cm, 2 h 30 → 392,5 cm), L46 ex. 6 (3) (périmètre 50,24 → aire 200,96) ; 04 ← L46 ex. 10 (piste, rayon intérieur 30 m), L20 ex. 8 (arc des trois quarts 13,188 — erratum p.200), L46 ex. 9 (porte 8,0208 m², arrondi), L20 ex. 11 (nappe, échelle 1/50, 785 vs 725) ; 05 ← L46 ex. 6 (2) (aire 314 → périmètre 62,8).

## 23-solides-cube-pave

### Table des écarts (avant)
- Cours (640 l., 8 sections) déjà aligné sur les leçons 54 et 58 : critère de reconnaissance (6 faces ET leur forme : le tronc de pyramide et le solide en L en contre-exemples), 6/12/8, perspective cavalière (cachés en pointillés), patron (6 carrés ≠ toujours un patron, faces opposées du dé, patron du pavé), latérale/totale du cube et du pavé, trois cas limites (boîte ouverte, solides accolés, lecture inverse), conversion cm² → m² et coût. Rien à ajouter au cours ; `coursePitfalls` (8 tags) tous portés par un distracteur.
- Exercices : toujours la formule directe sur 3–4 dimensions (5/3/4 revient dans 02-boss, 04-defi Q2 et Q3 : deux questions strictement identiques — « نفسُ متوازي المستطيلات » ne se lit pas seul). Jamais exercés : reconnaissance (pavé vs cube vs tronc de pyramide), patron (valide / invalide), faces opposées du dé, arêtes cachées, boîte ouverte, solides accolés, lecture inverse (arête depuis l'aire, hauteur depuis l'aire totale), conversion cm² → m² et prix, dimensions en unités mélangées.
- Volume ⛔ : aucun item ne le demande (le produit 9 × 6 × 4 apparaît seulement comme distracteur `math.mes.volume-utilise-comme-aire`). Dénombrement de cubes (54-10 : 10 pièces ; 54-12 : 60 savons) ◐ : non repris. Nommer une face par ses 4 sommets (54-4) : non enseigné, non repris. Errata n° 61, 62 : non concernés ; L58 ex. 4, 6, 9 (ambigus) non repris.

### Fait
- Cours/résumé inchangés ; chapter.json : source ajoutée (fiche).
- Quiz 5 → 7 (6 faces ≠ pavé ; boîte ouverte). Exercices +3 / +4 / +3 / +3 (+2 remplacées) / +4 ; 04-defi Q2 et Q3 remplacées à leur place (9 × 6 × 4 → 228 en QCM ; base 7 × 3, aire totale 142 → hauteur 5 en `numeric`).
- Formats : 1 `multi` (reconnaissance, 05), 7 `numeric`, figures SVG (cavalier avec arêtes cachées, patrons de cube valide/invalide, patron du dé, deux cubes accolés, boîtes ouvertes).
- Reprises déclarées (`manuel`, mêmes données) : 04-defi ← L58 ex. 10 (bassin 8 × 6 × 2 ouvert : 104 m² ; dalles 25 cm, boîtes de 24 à 36 d → 2 520 d) et L58 ex. 7 (pavé : largeur 6, base 54, totale 198 → hauteur 3) ; 05 ← L58 ex. 7 (cube de base 25 m², totale 150 → latérale 100).
- Les nombres du cours et de L58 ex. 2/3/5/8 sont déjà dans le cours (cube de verre 30 cm, armoire, plumier, deux cubes de 2,5 dm) : les exercices utilisent d'autres données pour ne pas redemander l'exemple.

## 25-perimetre-figure-composee (neuf, displayOrder 25)

- Fondé sur la leçon 24 (ص 67–69) et le critère مع 4 du T1 (p.153). Six notions, une section chacune au patron : contour extérieur (côté commun exclu), lecture des marques et longueurs manquantes (par propriété du quadrilatère, par marque, par soustraction : L), demi-cercle dans le contour (arc π×d÷2, diamètre commun exclu), arc ajouté / arc retranché / quart de cercle (coin arrondi), contour sur plan à l'échelle (arrondi par excès des rouleaux), contour fermé et plantations (intervalles = plants). 9 figures de cours, toutes dessinées et rendues à l'œil ; aucun exemple des ch. 18–21 repris (vérifié sur 18 `محيط`, 19 `محيط`, 21 porte/stade).
- Quiz 5 ; exercices 01 d1, 02 d3, 03 d2, 04 d4, 05 d3 à 6 questions ; `manuel` : 02 ← ex. 4 (stade 110 × 90 → 502,6 m) et ex. 5 (120 × 60, arc ajouté et retranché → 428,4 m) ; 04 ← ex. 2 (plan 1/750, 356,52 m → 8 rouleaux, figure redessinée, côté commun rectangle/carré non clôturé comme lu par la fiche) et ex. 9 (17 côtés de 5 m → 85 m → 170 plants).
- **Erreur de la fiche relevée** : §2 octies, L24 ex. 7 « 3 + 3 + 3 + 3 + 4,71 = **18,71** » : la somme vaut **16,71** (12 + 4,71). Exercice non repris (lecture « déduite »).
- Non repris : ex. 3 (porte : mêmes données que l'exemple « porte » du ch. 21), ex. 6 (base de la porte non tranchée), ex. 7 (triangle équilatéral déduit), ex. 8 (circuit : cotes et sens des arcs déduits).

## Passe « aucune question ne redonne le cours » (consigne du pilote)

Contrôle par script (nombres de chaque prompt contre les blocs `exemple`, `verifie` et `⚠️` du cours) puis relecture. Corrigés :
- **Cours modifiés** là où une reprise du manuel avait les mêmes données : ch. 20 (vérifier : 120 × 50 / 30 → 80 × 60 / 20, 44 آر, résumé) ; ch. 21 (aiguille 25 → 18 cm ; deux cercles dans un rectangle de hauteur 5 → 6 ; exemple de la méthode d = 8 → d = 26) ; ch. 23 (bassin ouvert 8 × 6 × 2 → 10 × 7 × 2 = 138 m² ; lecture inverse 198/54 → 150/20 ; cube 150 → 96).
- **Anciennes questions refaites en place** (même rang, même difficulté) quand elles reprenaient un exemple : 20/01 Q1 (5 × 3), 21/01 Q5, 21/04 Q1 et Q5 (roue 30), 21/05 Q3, 23/02 Q4 (5/3/4), 23/03 Q3, 23/04 Q5, 23/05 Q5.
- Questions nouvelles dont les nombres sont changés : 21 (02 Q7–Q9, 03 Q9, 05 Q8, Q10, 01 Q8, 03 Q8 manuel), 23 (03 Q7), 25 (quiz Q3, 01 Q3, 02 Q2, 03 Q4, 04 Q4, 05 Q4). Reprises du manuel retirées quand les données ont changé (21/03 : ex. 6 ; 21/05 ; 21/02).
- `؟` dans les figures remplacé par `…` (ch. 20) ; aucun `**` dans les énoncés ; pas de « لا » seul contre « نعم » ×3 (25 quiz Q3 refait en choix de contenu).
