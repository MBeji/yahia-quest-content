# Journal du lecteur R1 — maths 6ᵉ, concours C01 (2026) à C09 (2018)

Étape G2, lecture du 2026-10-19. Neuf sujets de 2 pages, scans sans couche texte (`pdftotext` rend 2 octets) : lecture en vision, 150 DPI, une fois par page, lisibilité bonne pour les neuf. Les neuf sha256 des copies `/tmp/claude-0/m6g/src/<année>-math.pdf` égalent ceux de `docs.json` et du registre. Aucune écriture git, `gisement.json` et `content/math-6eme/` intacts.

## 0. Conventions

- **Grain** : une ligne par **question notée** (`1a`, `1b`, `2a`…) ; la lettre `a/b/c` est le rang de la question dans le problème imprimé (`1.`/`1)`/`1-`/`1/`), n°exo = `<problème><rang>`. 7 lignes par sujet (2 + 2 + 3), 63 au total.
- **Barème** : le sujet n'imprime que le total par problème (6 + 6 + 8 = 20, 2018 et 2019 : aucun barème). Colonne barème = `-` pour toutes les questions ; les totaux de problème sont au § de chaque document.
- **Compétences** : registre `math` (63 ids), 1 à 3 par ligne ; aucune `hors-registre`.
- **Placement** : chapitre de la dernière étape + chapitres des notions secondaires, rangés dans l'ordre du manifeste. Une construction se note avec le verbe « construire / dessiner » dans l'archétype.
- **Jetons HP** : `HP:interet` (C05 1b, notion « ◐ rencontrée non enseignée » ; le validateur refuse `HP:◐…`, mot-clé kebab seulement) ; `HP:pythagore` (C07 3a, voir ci-dessous).
- **Chapitres neufs 25 et 26 absents du manifeste** (`24 chapitre(s) au manifeste`) : la commande refuse leur slug. Les questions de périmètre d'une figure composée sont donc rattachées au chapitre le plus proche (19, 20 ou 21). Candidates au ch. `25-perimetre-figure-composee` dès que le manifeste l'aura : C01 3c, C03 3c, C06 3c, C07 3a et 3b, C08 3c. **Le ch. `26-diagrammes-batons` n'a aucune occurrence dans ces neuf sessions** (pas un seul diagramme ni tableau statistique à lire).
- **Transcriptions** : `content/programmes-officiels/examens-nationaux/6eme-base/math/<année>-unique.md`, texte tel qu'imprimé (en arabe, voyelles omises sur les sujets vocalisés 2018-2024), figures décrites entre crochets ; aucun texte support, donc rien de résumé.

## Structure commune de l'épreuve

Une heure (de 8 h à 9 h en 2018-2019), coefficient 1, **trois problèmes** : 6 + 6 + 8 points (2020-2026) ; 2018-2019 sans barème. Le 1er problème a 2 questions (pourcentages, fractions, divisibilité, multiples), le 2e 2 questions (vitesse-durée, fractions de quantité), le 3e 3 questions (géométrie : aires et périmètres ou vitesse) dont, selon l'année, une construction à l'échelle (C05, C07, C09). Aucune question à choix : tout est rédigé, souvent « أثبت أنّ… » (prouver une valeur donnée).

## Documents

### C01 (2026) — vision, 2 pages, bonne ; 6 + 6 + 8
- P1 : fraction + répartition (400 objets, recette), puis hausse de 5 % par échange. P2 : camion/voiture, fraction de réservoir, consommation, distance. P3 : figure composée symétrique (cerf-volant et petit quadrilatère intérieur) : aires par différence, base par l'aire, périmètre par écart de périmètres.
- Chapitres : 02, 13, 14, 15, 11, 04, 05, 19, 20. Aucun HP. Figure sans cote : tout vient du texte.

### C02 (2025) — 6 + 6 + 8
- P1 : tableau de trois clients et de trois couleurs de bouquets (raisonnement sur trois sommes), prix unitaire. P2 : voilier en cuivre (trapèze + 2 triangles), masse surfacique, pourcentage, « le carré tient-il ? » avec justification. P3 : bus, durées de tour, arrêts, heure d'arrivée, vitesse réduite.
- Chapitres : 13, 02, 14, 04, 05, 19, 20, 15, 22. Aucun HP.

### C03 (2024) — 6 + 6 + 8
- P1 : course d'obstacles, parcours et pourcentage, comparaison de deux vitesses. P2 : tarif de club avec trois tranches (réduction 9/10, 20 %), un montant puis un nombre d'heures. P3 : plateau de table en trapèze composé de dix parallélogrammes, fraction de l'aire, longueurs, nombre de chaises.
- Chapitres : 02, 14, 15, 22, 13, 05, 20, 04, 19. Aucun HP. Point d'attention : 3c suppose les longueurs des côtés obliques, non portées sur la figure.

### C04 (2023) — 6 + 6 + 8
- P1 : multiples communs dans un intervalle ; deux recettes, un prix unitaire par différence. P2 : cerf-volant et fil de trois demi-cercles ; coût au mètre carré. P3 : cycliste, vitesse, pourcentage, durée en montée et descente, justification oui/non.
- Chapitres : 06, 02, 14, 05, 21, 19, 20, 15, 13, 22. Aucun HP.

### C05 (2022) — 6 + 6 + 8
- P1 : projet solaire en pourcentages du coût, crédit remboursé en versements (surcoût en %, notion d'intérêt `HP:interet`). P2 : piscine et deux pompes, durées 2 h 40 + 8 h, débit, avance d'une pompe. P3 : parc en carré + parallélogramme + trois quarts de disque (arc, aire par fraction et excès) ; **construction à l'échelle** d'un parallélogramme (angle, côté, hauteur).
- Chapitres : 14, 05, 22, 15, 13, 21, 20, 17, 19.

### C06 (2021) — 6 + 6 + 8
- P1 : deux options d'achat (même reste et moitié du prix), contributions en pourcentage, fraction, excès. P2 : voiture/camion, 1 h 36 min, distance, pause d'après un retard. P3 : jardin public en trapèze rectangle + demi-disque, aire en ares, longueur par différence de bases, point atteint après 5611 m sur un parcours (tours entiers).
- Chapitres : 02, 13, 05, 14, 15, 22, 20, 21, 19. Aucun HP.

### C07 (2020) — 6 + 6 + 8
- P1 : trajet domicile-travail avec bus toutes les demi-heures (heure d'arrivée, retard au départ). P2 : jouets, fraction + écart, puis intervalle et restes égaux par trois diviseurs. P3 : triangle rectangle de 6 ares et route parallélogramme : clôture, coût du mètre, **construction à l'échelle** ; `HP:pythagore` en 3a (voir ci-dessous).
- Chapitres : 22, 08, 13, 02, 06, 18, 20, 05, 14, 19.
- **HP** : 3a demande de prouver un périmètre de 114 m ; l'aire (6 ares) et la hauteur donnent l'hypoténuse, les deux autres côtés exigent la relation de Pythagore ou la reconnaissance d'un triangle à côtés entiers : à traiter par l'auteur (programme ancien ?). 3b dépend du résultat de 3a et des côtés du parallélogramme (non cotés).

### C08 (2019) — **aucun barème imprimé**, séance de 8 h à 9 h
- P1 : deux achats possibles, reste d'argent, prix avant remise (fraction, pourcentage). P2 : voiture, heure d'arrivée avec aller-retour et arrêt, capacité d'un réservoir. P3 : triangle isocèle + parallélogramme, hauteur et côté cotés, prix de vente au mètre carré, prêt, clôture.
- Chapitres : 02, 05, 13, 14, 15, 22, 18, 19, 20. Aucun HP.

### C09 (2018) — **aucun barème imprimé**, séance de 8 h à 9 h
- P1 : nombre compris entre deux bornes avec restes égaux par 23 et 13, bénéfice fractionnaire, pourcentage du coût. P2 : marche et bus, durée totale, heure d'arrivée à l'arrêt (énoncé ambigu : la demi-heure semble couvrir les deux étapes réunies). P3 : carré + parallélogramme + triangle, aire en hectares, coût de projet avec pourcentage et fraction, **construction à l'échelle**.
- Chapitres : 06, 02, 05, 13, 14, 15, 22, 17, 19, 20, 18. Aucun HP (hectare : unité du ch. 05).

## Bilan R1

- 9 documents lus, 9 sha256 conformes au registre, 9 transcriptions (`2018` à `2026-unique.md`), 63 lignes (7 × 9), 9 `.meta`, `content:gisement:lignes` : **63 valides, 0 fautive**.
- Notions : fractions d'une quantité et pourcentages (13/14, présents dans presque chaque problème), vitesse-durée (15, 22), aires (20, 21) ; aucune question de volume, de solides, d'angles à mesurer, de divisibilité par 3 ou 9 explicite.
- Part HP : 2 lignes sur 63 (interet ◐, pythagore). Programme ancien : aucun signal dans ces neuf sessions.
- Difficultés : questions « montrer que » dont le résultat est donné (l'auteur devra choisir un autre résultat), figures sans cotes (C01, C03), 3a de C07, ambiguïté de C09 2a, chapitres 25/26 hors manifeste.
