# Journal du lecteur R3 — maths 6ᵉ, devoirs D01 à D09

Étape G2, lecture du 2026-10-19. Neuf devoirs de devoir.tn (rubrique تقييمات), 40 pages, tous des PDF sans couche texte exploitable (l'arabe sort désordonné, les chiffres inversés) : lecture en vision (110 DPI, un zoom à 220 DPI pour l'item 8 de D09), une fois par page. Les neuf sha256 des copies `/tmp/claude-0/m6g/devoirs/D0x.pdf` égalent ceux du registre `gisement.json`. Aucune écriture git ; `gisement.json` et `content/math-6eme/` intacts. Salle blanche : snapshots texte dans `/tmp/claude-0/devoirs-snapshots/math-6eme/D01.txt`…`D09.txt` (hors git), aucune transcription versionnée.

## 0. Conventions

- **Grain** : une ligne par question notée ; n°exo = numéro de la question dans le document (`1`, `2`…) ; une lettre quand le document numérote en sous-questions (D03, D04, D05, D06, D07 fin, D08) ou quand une question compte deux résultats (D02 12a/12b). Le calcul mental est noté item par item (`11a`…, `13a`…, `8a`…) quand ses items sont imprimés.
- **Total** : 124 lignes (D01 18, D02 21, D03 12, D04 10, D05 8, D06 18, D07 12, D08 17, D09 8), `content:gisement:lignes` : 124 valides, 0 fautive.
- **Créneaux** : le registre donne le trimestre (T1, T2, T3), traduit en `DC1`, `DC2`, `DC3` (la 6ᵉ du primaire n'a pas de devoir de synthèse distinct dans ce lot).
- **Barème** : ces devoirs notent **par critère** (مع1 à مع5, grille de maîtrise : minimale, maximale, excellence), pas par question. Colonne barème = `-` partout sauf : calcul mental de D02 et D09 (0,5 par item, imprimé) ; D04 (points du critère imprimés par question : 3, 3, 1, 2, 3, 4) ; D01 question 5 (5, critère d'excellence) ; D08 question 4 (5) ; D01 question 10 et D08 constructions (4, critère de construction) ; D07 constructions et calcul mental (4). Total /20 sauf D09 (4) et D02 calcul mental à part (4).
- **Compétences** : registre `math` (63 ids), 1 à 3 par ligne ; aucune `hors-registre`.
- **Jetons HP** : `HP:somme-difference` (D01 1 et 2 : total et écart donnés, problème « somme/différence » de la liste ◐ de la fiche ; le ◐ va ici, jamais dans le jeton) ; `HP:somme-rapport` (D08 1 : somme de deux dimensions et rapport fractionnaire entre elles, proche cousin ◐ ; à l'auteur de trancher s'il l'assimile à la même ◐). 3 lignes sur 124.
- **Chapitres 25 et 26** : le manifeste les contient (26 chapitres), le validateur les accepte. `25-perimetre-figure-composee` : D04 1, D05 4, D08 5 (contour d'une figure faite d'un polygone et de demi-cercles ou de cercle). `26-diagrammes-batons` : **aucune occurrence** dans les neuf devoirs (pas un diagramme, pas un tableau statistique ; seul un tableau de dimensions en D03 et D04, sans lecture statistique).
- **Échelle** : rattachée à `14-proportionnalite-pourcentage` (leçon 14 du manuel, fiche § 2 sexies) ; unités de masse, d'aire (are, hectare) et monétaires rattachées à `05` ou `04`/`03`.
- **Lisibilité** : trois items ou énoncés manquent dans les scans (voir les documents).

## Structure commune des devoirs

Ils suivent l'évaluation par compétences du manuel : une **situation** (السند) découpée en consignes (التعليمة), évaluée par **critères** : مع1 (sens/pertinence), مع2 (outils de la matière), مع3 (cohérence), مع4 (construction ou production), مع5 (excellence). Une heure, /20 (D01 et D08 : 16 + 4 de calcul mental). Une situation de départ commune (le même agriculteur) enchaîne en général : un multiple commun dans un intervalle (à prouver ou à trouver), un bilan de production ou de prix en décimaux (kg, quintaux, dinars/millimes), une durée à calculer entre deux horaires, une échelle, un périmètre ou une aire, une ou plusieurs constructions. Le calcul mental, quand il existe, est une feuille à part (D01, D02, D08, D09) ou dictée (D07).

## Documents

### D01 — T1 2018/2019, 4 pages, bonne ; 20 (16 + 4 mental)
- Six situations : somme et écart d'effectifs avec multiple commun sous 400 ; productions en kg (décimal × entier, excédent) ; vente avec deux fractions retirées (1/5 et 1/8) à prix décimal ; plan à l'échelle 1/500 (longueur et largeur) ; labour (début en fraction d'heure, pause en minutes, 1/4 de la surface) ; construction d'un losange (diagonale, angle de 30°) puis d'un carré sur un côté. Calcul mental : 8 items (PPCM, reste égal, ×0,001, ÷ décimal, aire du carré par le périmètre, conversions hm²/are/durée).
- Chapitres : 05, 04, 11, 13, 14, 22, 17, 19, 06. HP : somme-difference (×2). Programme en vigueur.
- Difficultés : l'énoncé du 4 parle de pommes alors que le support donne des amandes (incohérence de la source) ; le total des arbres « juste avant 400 » est multiple de 56, ce que le calcul à la main rend lourd ; deux questions dépendent de la précédente (3-4, 8-9).

### D02 — T1 2019/2020, 14 pages, bonne ; 20 par version
- Deux versions A (olives) et B (grenades) du **même gabarit** avec corrigés détaillés, puis la feuille de calcul mental (sujet et corrigé). Chaque version : prouver qu'une masse est l'unique multiple commun dans un intervalle (à partir du PPCM donné en A, à trouver en B) ; vente après dons et transformation (kg, millimes) ; revenu net ; prix unitaire par division ; durée de conduite avec une pause d'un tiers d'heure ; construction d'un trapèze rectangle (A) ou vérification de dimensions sur plan 1/500 puis construction (B). Calcul mental : 8 items (×100, ÷10, ×0,01, ÷ millième, encadrement entre multiples de 4, ha → m², complément à 8, aire d'un carré).
- Chapitres : 06, 07, 02, 04, 05, 13, 22, 16, 19, 14, 20. Aucun HP. Programme en vigueur.
- Difficultés : le fichier contient deux fois le même devoir (les 12 premières lignes sont des paires jumelles, à ne pas compter deux fois dans les statistiques de pondération) ; les corrigés sont imprimés (ne rien en reprendre) ; la question « prouver que la masse est… » donne le résultat à retrouver.

### D03 — T1 2019/2020, 2 pages, bonne ; sans barème par question
- Situation intégrée : même squelette que D02 (multiple commun entre bornes, 252 q à prouver, don d'un dixième, export en dollars converti en dinars à taux donné, revenu net, prix d'un veau, durée de voyage en h-min-s avec pause, puis cinq constructions : trapèze rectangle à l'échelle 1/5000, triangle à l'échelle 1/18000 avec angle de 120° et sa nature, trois hauteurs et leur point commun, triangle équilatéral à l'échelle 1/25000).
- Chapitres : 06, 02, 05, 13, 04, 22, 14, 16, 17, 18, 19. Aucun HP. Programme en vigueur.
- Difficultés : la conversion de devise et le taux décimal (2,850) sont inhabituels ; les hauteurs d'un triangle obtus sortent du triangle (3 hauteurs prolongées) ; le sommet « orthocentre » n'est pas nommé dans l'énoncé.

### D04 — fin de T2 2015/2016, 4 pages, partielle ; 20 (barème par critère)
- Jardin public à l'échelle 1/2000 : périmètre réel d'une figure à demi-cercles (25) ; nombre de dalles de 40 cm de côté sur le triangle ; financement par fractions (2/5, 1/4, reste = montant donné) : fraction, coût total, pourcentage du coût que représentent les dalles ; trois constructions (trapèze rectangle : somme et différence des bases, parallélogramme avec angle, losange par ses diagonales) ; une somme multiple de 2, 3 et 5 entre deux bornes ; prix initial avant 30 % de réduction par deux méthodes.
- Chapitres : 14, 21, 25, 05, 20, 11, 13, 19, 16, 17, 06, 07. Aucun HP. Programme en vigueur.
- Difficultés : cotes de la figure du support 1 peu nettes (le périmètre réel est à lire sur la figure) ; le support 5 est absent (numérotation saute de 4 à 6).

### D05 — T2 2014/2015, 3 pages, bonne ; 20 (grille imprimée en p. 3)
- Multiple commun de 3, 8 et 12 sous 100 (trouver puis encadrer) ; carte à l'échelle 1/2 000 000 : distances réelles puis distance aller-retour ; plan d'un trapèze rectangle à l'échelle 1/2000 : dessiner à la règle et au compas, dimensions réelles, périmètre en hm ; périmètre d'une figure triangle + rectangle + cercle (25).
- Chapitres : 06, 05, 14, 04, 16, 19, 21, 25. Aucun HP. Programme en vigueur (ancien nommé « 2014/2015 » dans l'en-tête, aucune notion hors fiche).
- Difficultés : l'unité attendue du périmètre (hm) est peu lisible ; le registre ne donne pas l'année de ce devoir.

### D06 — T2 2019/2020, 4 pages, partielle ; /20 sans barème par question
- Monnaie et métrique : épargnes en dinars et millimes (retrancher, additionner, représenter avec le moins de coupures) ; liste de courses (prix en millimes × effectif, total, représentation avec pièces imposées) ; reste après billets ; question à inventer sur une réduction et un rendu de monnaie ; conversions de distances en dam ; boîte rectangulaire (largeur moitié de la longueur), aire, périmètre, complétion d'un dessin de cartes.
- Chapitres : 03, 04, 05, 19, 20. Aucun HP. Programme en vigueur.
- Difficultés : devoir presque sans géométrie ; la figure des cartes de vœux et le support 5 manquent ; « formuler puis résoudre » une question est une production libre non convertible telle quelle ; confusion possible entre « مي » (millime) et « م » (mètre).

### D07 — fin de T3, 3 pages, partielle ; 20 (barème par critère)
- Aire d'un rectangle de côtés en dam (largeur = 2/3 de la longueur) ; aire d'une maison composée puis aire restante du terrain ; durée d'un trajet, heure d'arrivée au retour, durée de conduite aller-retour ; consommation aux 100 km avec tableau ; coût du m² de carrelage ; constructions de bassins (cercle de rayon réel 3 m, carré de côté 4 m, triangle avec angle de 45°) ; calcul mental dicté (conversions de masses, aires, durées ; × ÷ 10 à 0,001).
- Chapitres : 05, 13, 20, 04, 22, 14, 21, 19, 17, 18. Aucun HP. Programme en vigueur.
- Difficultés : le troisième bassin n'est pas dans le sujet ; les items du calcul mental ne sont pas imprimés (une seule ligne) ; plusieurs questions s'appuient sur l'aire de la maison (7 et 2b) ; la figure de la maison est mal cotée (cote de 4,7 m sans sommet clair).

### D08 — période 3 de 2018/2019, 4 pages, bonne ; 20 (16 + 4 mental)
- Rectangle dont la somme des dimensions est un multiple de 2, 3, 5, 9 entre deux bornes, largeur = 1/4 de la longueur : aire, production en kg depuis l'emprise d'un arbre, production estimée en ajoutant une hausse en tonnes ; élagage par fractions successives (1/8, 1/2, reste) ; périmètre d'un complexe à l'échelle 1/1000 (trapèze + demi-cercle) sur plan puis réel ; constructions (cercle de circonférence donnée, parallélogramme, triangle rectangle isocèle) ; calcul mental de 8 items (divisibilité, 2/5 + 1/5, reste 2, demi-quintal/tonne/are).
- Chapitres : 07, 13, 20, 05, 04, 11, 21, 25, 14, 17, 19, 18, 06. HP : somme-rapport (1). Programme en vigueur.
- Difficultés : question 1 enchaîne cinq étapes (divisibilité → somme → fraction → dimensions → aire) ; l'énoncé du triangle rectangle isocèle ne donne pas de longueur ; même gabarit que D01 (feuille « صالح »).

### D09 — juin 2015, 2 pages, partielle ; 4 points (huit items à 0,5)
- Ce n'est pas un devoir : une **feuille de calcul mental** à huit items (divisibilité par 2, 5 et 9, soustraction de décimaux, une écriture fractionnaire partielle, plus grande de trois fractions de même numérateur, entier × fraction, 10 % d'un montant, encadrement d'une fraction supérieure à 1, nombre fractionnaire en fraction). Version élève et fiche du maître identiques.
- Chapitres : 07, 04, 09, 10, 13, 14, 24. Aucun HP. Programme en vigueur.
- Difficultés : l'item 3 n'a pas de membre gauche (« ? = 3/8 ») : classé 09 par défaut, à ne pas exploiter sans vérification ; le registre le range en T3 (juin 2015).

## Bilan R3

- 9 documents lus, 9 sha256 conformes au registre, 9 snapshots hors git, 124 lignes, 9 `.meta`, validateur : 124 valides, 0 fautive.
- Notions (occurrences chapitre dans la colonne chapitres) : 05 (37), 04 (19), 13 (18), 14 (16), 19 (15), 06 (12), 22 (11), 20 (10), 07 (8), 18 (6), 21/17/16/02 (5), 11/03 (4), 25 (3), 24 (2), 10, 09 (1). **26 : 0 occurrence.** Pas de 23 (solides), 15 (vitesse), 01 ni 08, 12 : aucun item.
- Part HP : 3 lignes sur 124 (somme-difference ×2, somme-rapport ×1), toutes des problèmes à somme donnée. « Programme ancien » : aucun signal (D04 de 2016 et D05 de 2015 restent dans la fiche). Notions ◐ rencontrées : aucune de moyenne, d'intérêt ni de symétrie.
- Difficultés : lignes jumelles dans D02 (version A/B) ; trois énoncés partiels (D04 support 5, D06 support 5 et figure des cartes, D07 troisième bassin) ; un énoncé inconsistant (D01 4) ; la notation par critère rend le barème par question indisponible.
