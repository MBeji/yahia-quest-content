# Journal du lecteur R2 — maths 6ᵉ, concours C10 (2017) à C19 (2008)

Étape G2, lecture du 2026-10-19. Huit sujets de 2 pages (C13 2014 et C16 2011 introuvables, non cherchés). Les huit sha256 des copies `/tmp/claude-0/m6g/src/<année>-math.pdf` égalent ceux de `docs.json` et du registre (contrôle `sha256sum`). Aucune écriture git ; `gisement.json` et `content/math-6eme/` intacts. Une seule page lue deux fois : la fin de la page 1 de 2009 (zoom 220 DPI) pour vérifier une fraction imprimée.

## 0. Conventions (identiques à R1)

- **Grain** : une ligne par question notée, n°exo = `<problème><rang>` (`1a`, `1b`, `2a`…). 7 lignes par sujet (2 + 2 + 3), 56 au total.
- **Barème** : aucun barème imprimé, ni par problème ni par question, sur les huit sessions (R1 en trouve un, 6 + 6 + 8, à partir de 2020). Colonne barème = `-`.
- **Compétences** : registre `math`, 1 à 3 ids par ligne, aucune `hors-registre`.
- **Placement** : chapitres de la dernière étape et des étapes intermédiaires, dans l'ordre du manifeste. Une construction se dit « construire / dessiner » dans l'archétype.
- **Jetons HP** : le validateur refuse `HP:◐…` ; trois jetons kebab, tous ◐ (« rencontrée, non enseignée », fiche § 3.2) : `HP:somme-rapport` (partage d'un total selon un rapport fractionnaire, 3 lignes), `HP:somme-difference` (partage selon somme et écart, 2 lignes), `HP:interet` (même jeton que R1 C05 1b, 1 ligne). Aucun ⛔ dans les huit sessions.
- **Chapitre 25 absent du manifeste** (24 chapitres) : la commande refuse son slug. Deux questions de contour d'une figure composée sont rattachées à 20/21 (C10 3c) et 19/21 (C11 3b) ; **candidates au ch. `25-perimetre-figure-composee`** dès qu'il sera au manifeste : C10 3c, C11 3b (et, au sens large, C17 3c, contour d'un trapèze moins une ouverture). Aucune question de diagramme en bâtons dans les huit sessions : le ch. `26` n'a ici aucune ligne.
- **Transcriptions** : `content/programmes-officiels/examens-nationaux/6eme-base/math/<année>-unique.md` (2017, 2016, 2015, 2013, 2012, 2010, 2009, 2008). Énoncés et consignes mot pour mot (voyelles omises), figures décrites entre crochets ; pas de texte support, donc rien de résumé. Format de l'en-tête et des blocs identique à R1 (`lecture: vision`).

## Structure commune de l'épreuve (2008-2017)

Une heure (de 8 h à 9 h), trois problèmes, sans barème imprimé ; la case « الضارب : 1 » n'apparaît qu'en 2016 et 2017. Régularité nette sur les huit sessions : **P1** = argent (fraction d'un prix à retrouver, pourcentage de remise ou d'intérêt, partage de sommes) ; **P2** = trajet (vitesse, durée, horaire, carburant) ou, en 2017 et 2009, tableau de revenus ou de fractions d'une surface ; **P3** = géométrie à enchaînement long (aire de figure composée, rectangle ou losange, trapèze, demi-disque, clôture) qui rejoint l'argent par un prix à l'are, à l'hectare ou au mètre. Les questions sont toutes à réponse numérique ou justifiée par le calcul ; deux constructions à l'échelle (2016 3c : losange ; 2015 3c : rectangle) ; trois demandes de preuve par le calcul (2017 1b, 2013 3a, 2008 3b).

## Documents

### C10 (2017) — vision, 2 pages, bonne ; papier rose
- P1 : trajet avec arrêt, fraction supérieure à un de la distance déjà faite (1a), justification d'une heure d'arrivée (1b). P2 : tableau de revenus (loyer, salaire = 5/4 du salaire de l'épouse) ; puis 65 % du total pour une table et cinq chaises (écart donné) : prix d'une chaise. P3 : triangle rectangle + demi-disque, aire du demi-disque = 40 % de celle du triangle (aire du demi-disque, diamètre, contour).
- Chapitres : 13, 15, 22, 04, 05, 14, 20, 21 ; HP ◐ : somme-rapport (2a), somme-difference (2b).
- Difficultés : (1) figure 3 : l'angle droit n'est pas codé en B (il se lit sur le dessin) et la flèche cotée 39,25 est une hauteur sur [أ ج] qui n'est pas compatible avec 78,5 et le diamètre (le côté [أ ج] se déduit de la 2ᵉ paire base-hauteur, ce que le théorème de Pythagore, hors programme, contredit) : données redondantes, à ne pas reprendre telles quelles ; (2) 2b : « يفوق ثمن الكراسي ثمن الطاولة » compare les cinq chaises à la table (prix d'une chaise : un décimal à deux chiffres après la virgule).
- Programme : en vigueur.

### C11 (2016) — vision, 2 pages, bonne ; papier jaune
- P1 : deux contributions, prix retrouvé par part unité, taux de remise (1b, base inconnue = prix initial). P2 : plein de carburant égal aux 2/3 du reste (capacité), vitesse requise sur la seconde moitié du trajet entre deux horaires. P3 : losange (grande diagonale, petite = 3/4 de la grande, hauteur) : côté par l'aire, contour avec demi-cercle et entrée, construction à l'échelle.
- Chapitres : 04, 13, 05, 14, 15, 22, 19, 20, 21, 16 ; aucun HP.
- Difficultés : 3a se résout sans Pythagore par l'aire du losange (produit des diagonales sur deux = côté × hauteur) ; la figure est lisible, la hauteur 48 m est issue de B sur le côté [أ د].
- Programme : en vigueur.

### C12 (2015) — vision, 2 pages, bonne ; grand format (PDF de 1252 × 1742 pt, rendu à 75 DPI suffisant)
- P1 : deux façons d'obtenir une robe : coût d'achat de tissu + façon égale à 5/2 du prix du tissu, contre prix initial remisé de 15 % ; choix de la moins chère. P2 : tableau d'excursion (aller-retour 300 km, 60 km/h, horaires en format 24 h, visite 4 h 45) : heure de départ, vitesse de retour. P3 : terrain rectangulaire coupé en deux, première part = 2/5 de l'aire totale, marges de 4 m, plan à l'échelle (construction d'un rectangle).
- Chapitres : 05, 13, 03, 14, 15, 22, 20, 19 ; aucun HP.
- Difficultés : le tableau de P2 donne la distance de l'aller-retour (piège voulu) ; la 2ᵉ ligne de la fraction (5/2, supérieure à un) est un coût de façon plus grand que le tissu.
- Programme : en vigueur.

### C14 (2013) — vision, 2 pages, bonne ; scan gris
- P1 : ligne brisée à l'échelle 1/4 000 000 (deux segments cotés en cm) : distance réelle, puis heure de départ avec une pause d'une demi-heure. P2 : deux remises sur un même ordinateur (20 % contre un prix final) : choix argumenté ; puis prix réel d'une imprimante depuis le prix remisé du lot (même taux). P3 : ferme en triangle rectangle + trapèze rectangle (preuve de 4 ha), nombre d'arbres par la surface occupée, recette, revenu net.
- Chapitres : 04, 14, 05, 15, 22, 03, 20, 02 ; aucun HP.
- Difficultés : (1) le prix remisé du problème 2 est celui du lot ordinateur + imprimante (981,200), pas de l'imprimante seule : la question demande de retrancher le prix réel de l'ordinateur ; (2) 3a : le côté de 250 m est une hypoténuse et une base de trapèze : le triangle se calcule par les deux côtés de l'angle droit, le trapèze par ses côtés perpendiculaires à la base.
- Programme : en vigueur (échelle jusqu'à 1/4 000 000, déjà au manuel).

### C15 (2012) — vision, 2 pages, bonne
- P1 : prix retrouvé depuis une somme égale à 3/7 du prix, emprunt à taux de 12 % sur le seul manque : coût de la voiture. P2 : durée 6 h 50 – 11 h 30 à 75 km/h, consommation aux cent kilomètres sur l'aller-retour. P3 : trapèze à l'échelle 1/500 (bases 8,4 et 13,6 cm, hauteur 6 cm) : dimensions réelles, prix à l'are, part empruntée en pourcentage du coût total (le prix du terrain valant 2/7 du coût d'aménagement).
- Chapitres : 04, 13, 14, 15, 22, 05, 20, 11 ; HP ◐ : interet (1b).
- Difficultés : 3c : la fraction est donnée « dans le mauvais sens » (le terrain est 2/7 de l'aménagement, donc l'aménagement vaut 7/2 du terrain) ; résultat rond (12,5 %), données cohérentes.
- Programme : en vigueur.

### C17 (2010) — vision, 2 pages, bonne ; daté du samedi 26 juin 2010
- P1 : cadeau financé en trois parts (mère, frères, père = 5/8) : prix ; remise de 12 % partagée entre deux achats selon somme et écart. P2 : trajet commençant jeudi à 22 h 30 (passage de minuit), carburant restant. P3 : trapèze rectangle (120 m, 100 m + 50 m, côté oblique 130 m) : prix à l'hectare, épargne telle que épargne + vente (moitié de l'épargne) + emprunt = prix, frais d'enregistrement par différence avec 8,3 % du prix.
- Chapitres : 04, 08, 13, 05, 14, 15, 22, 20, 19 ; HP ◐ : somme-difference (1b).
- Difficultés : le côté oblique 130 m n'est pas nécessaire à l'aire (50 et 120 suffisent) mais l'est au contour ; (130 = triple de Pythagore 50-120, sans qu'on le demande).
- Programme : en vigueur.

### C18 (2009) — vision, 2 pages, bonne ; copie de l'edunet (bandeau violet ajouté, non transcrit) ; couche texte réduite au bandeau
- P1 : dépense d'énergie bimestrielle d'une famille, installation de 240 d valant 2/13 du prix du chauffe-eau (coût total), économie en pourcentage. P2 : terrain municipal partagé en 3/8, 1/3 et un reste de 686 m² (aire totale, aire verte), valeur de l'aire verte financée aux 2/3 par une association. P3 : rectangle de périmètre 360 m dont la longueur vaut 2/3 de la largeur, prix à 2,400 d le m², prix du terrain = 10 % du projet, coût de construction = 5/7 du coût d'équipement.
- Chapitres : 04, 13, 05, 14, 09, 11, 19, 20 ; HP ◐ : somme-rapport (3a, 3c).
- Difficultés : **donnée incohérente en 2b** : « تكفّلت البلديّة بالباقي وهو ما يساوي 4/3 مساهمة الجمعيّة » alors que la part de l'association est 2/3 de la valeur : le reste vaut la moitié de sa part, non 4/3 (fraction vérifiée au zoom 220 DPI, bien imprimée « 4/3 ») ; la question 2b est donc ambiguë (reste = 1/3 de la valeur de l'aire verte, ou 4/3 de la part de l'association) : à ne reprendre qu'après arbitrage de l'auteur. Le raisonnement « somme, rapport » (3a, 3c) se fait par le schéma en barres, sans lettre.
- Programme : en vigueur.

### C19 (2008) — vision, 2 pages, bonne ; document traité de texte (non scanné) à couche texte inexploitable (glyphes de présentation), daté du 21 juin 2008 ; intitulé « الالتحاق » ; vision
- P1 : vente à tempérament (acompte + 12 versements) contre remise de 6 % au comptant : prix, écart. P2 : plan à l'échelle 1/150 d'un losange inscrit dans un cercle (diagonales de 6 cm et 4 cm, diamètre de 6 cm) : aire réelle du losange, aire du disque moins losange. P3 : trajet, 36 min parcourues à 50 km/h, panne de 35 min, reste = 3/2 du parcours fait ; arrivée après 8 h ; carburant aller-retour.
- Chapitres : 04, 05, 14, 19, 20, 21, 13, 15, 22 ; aucun HP.
- Difficultés : (1) 3 reprend, avec d'autres nombres, le P1 de C10 (2017) ; (2) 2 : l'échelle s'applique aux longueurs, jamais à l'aire du plan (piège de conversion) ; la diagonale horizontale du losange est le diamètre du cercle.
- Programme : en vigueur.

## Bilan C10-C19

- **8 documents lus, 8 sha256 conformes** au registre ; **8 transcriptions** versionnées sous `examens-nationaux/6eme-base/math/` ; **56 lignes** (`C10.tsv` … `C19.tsv`, 7 chacune) et 8 `.meta`. Validation `content:gisement:lignes --subject math-6eme --grade 6eme-base` : 56 valides, 0 fautive.
- **Étages** : d2 17, d3 33, d4 6. **HP** : 6 lignes ◐ sur 56 (11 %), 0 ⛔ ; « programme ancien » : aucune notion hors fiche, malgré l'ancienneté des sessions.
- **Chapitres les plus sollicités** (lignes) : 14 (23), 04 (19), 13 (17), 05 (17), 20 (12), 15 (10), 22 (10), 19 (7), 21 (4) ; 06, 07, 17, 18, 23, 24, 26 absents ; 25 non rattachable (absent du manifeste).
- **Difficultés à signaler** : figure 2017 P3 (données redondantes et incohérentes avec Pythagore) ; énoncé 2009 P2 (4/3 imprimé) ; 2013 P2 q2 (lot de deux articles) ; 2015 P2 (distance d'aller-retour, format 24 h) ; 2010 P2 (passage de minuit) ; 2016 P2 (capacité par fraction du reste).
