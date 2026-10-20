# Gisement 6ᵉ × maths : plan des missions d'examen et de devoirs (G3–G4, étude 36) — v1

Écrit le 2026-10-19 par le planificateur (lot D2 de [`PLAN.md`](./PLAN.md)). Entrées : les 17 sujets lus (`C01`–`C19`, sans `C13` 2014 et `C16` 2011, introuvables), leurs transcriptions (`content/programmes-officiels/examens-nationaux/6eme-base/math/`), les 119 lignes d'examen et les 124 lignes de devoirs (`lecture-gisement/lines/`, 243 valides), les trois journaux de lecture, la fiche (§ 3.2), `PLAN.md` § 3 (M1–M4) et les 26 chapitres de `content/math-6eme/` **tels qu'ils sont à 23 h 30 le 2026-10-19** (B1–B4 mis à niveau ; B5 en cours : voir § 4). Modèle : le plan du français 6ᵉ (`FableEtudes/campagnes/francais-6eme/PLAN-gisement.md`).

Sorties :

- **lignes reclassées en `25`** (ordre du coordinateur) : C01 3c, C03 3c, C06 3c, C07 3a, C07 3b, C08 3c (R1) ; C10 3c, C11 3b (R2) — colonne chapitres des `.tsv` éditée, `content:gisement:lignes` : 243 valides, 0 fautive ; C17 3c jugée non composée (trapèze rectangle seul, ouverture) : inchangée ;
- plan machine : [`plan-missions-v1.json`](./plan-missions-v1.json) — 38 missions (`m001`–`m038`), les écartés, la mesure des devoirs, les décisions à soumettre ;
- registre : `content/programmes-officiels/sources-externes/web-6eme-base-math/gisement.json` — 38 missions `planifiee` (`id` = la première ligne source, `sources` = les lignes du problème, `fichier`, `etage`, `etapes`, `lot`, `nn`) ; la section `documents` n'est pas touchée ;
- cartes d'affectation = lots d'auteurs : [`assign-M1.md`](./assign-M1.md) (06, 07, 13), [`assign-M2.md`](./assign-M2.md) (14, 15), [`assign-M3.md`](./assign-M3.md) (21, 22), [`assign-M4.md`](./assign-M4.md) (19, 20, 25) ;
- relevé de l'état de B5 au moment du plan : [`b5-etat-au-plan.json`](./b5-etat-au-plan.json) (empreintes des fichiers de 20, 21, 23 ; 25 apparu pendant le plan).

Format de l'épreuve (17 sessions) : une heure, **trois problèmes rédigés** (6 + 6 + 8 points depuis 2020 ; aucun barème imprimé avant), aucun QCM. P1 = argent (fraction, pourcentage, remise, partage) ; P2 = trajet (vitesse, durée, horaire, carburant) ou tableau ; P3 = géométrie longue (aires, contour, échelle) qui rejoint l'argent par un prix. Cinq constructions à l'échelle (2022, 2020, 2018, 2016, 2015). Programme : aucune session n'est « ancienne » au sens fort ; deux notions ◐ reviennent (intérêt, partage somme-écart/somme-rapport).

## 1. Règles retenues (adaptées du plan du français 6ᵉ)

**R1 — Une mission d'examen = un problème entier d'une session**, découpé en étapes notées (`numeric`, QCM du choix d'étape ou de la justification, `ordering` d'un raisonnement). La question dit sa session et redonne les données et la phrase officielles qu'elle lit ; « أثبتُ أنّ… » devient « quelle valeur / quelle justification ». Les données sont gardées telles quelles (décimaux à trois chiffres, unités, tableaux refaits lisibles, figures en SVG).

**R2 — Choix des problèmes : 32 sur 51.** Chaque session saine est reprise au moins une fois (17 sur 17) ; on retient les problèmes de gestes distincts (tranches, fraction supérieure à 1, passage de minuit, retour au départ, restes égaux…), jamais un problème défectueux ni dont la cible est ◐ (§ 5).

**R3 — Placement (F4).** Chapitre de l'étape neuve, c'est-à-dire en général le plus avancé de l'exercice dans l'ordre du manifeste ; exceptions déclarées en E-3.

**R4 — Constructions.** Non notables en QCM : conversions d'échelle + `ordering` des étapes, pas de dessin (E-5).

**R5 — Taille, étage, en-tête.** 12 questions au plus ; étage = la ligne la plus haute reprise, plafonné à d3 (jamais d4) : d3 `boss` 120/30, d2 `practice` 75/15 (E-2). Fichiers à partir de `06` : `NN-exam-<année>-p<N>-<slug>.json` (examens d'abord, récents d'abord), puis `NN-devoir-<slug>.json`. Titre arabe « 🏛️ مناظرة <année> · المسألة <N> ⭐⭐⭐: … », sans clé.

**R6 — Rien de ce que le patron pose déjà** : croisement question par question contre les chapitres actuels ; chaque mission nomme les questions à ne pas redemander (`neDemandePas`). Pour 20, 21 et 25 (B5) la liste est provisoire (§ 4).

**R7 — Hors programme.** ⛔/◐ jamais ciblés : Pythagore (`HP:pythagore`, écarte 2020 P3 ; piège en 2026 P3 q3, E-4), intérêt, somme-écart, somme-rapport, somme des angles d'un triangle (M3).

**R8 — Étiquettes.** Registre `math.*` : le « piège » de chaque ligne (colonne 9) est repris dans la carte ; l'auteur le fait porter par un distracteur étiqueté. Les ids déjà en usage par chapitre sont rappelés en tête de chaque carte.

**R9 — Devoirs, salle blanche (T2′).** Six missions sur des gestes absents des examens ou peu servis : multiples (unicité, trois nombres), chiffres manquants à plusieurs critères, échelle sur carte et plan, constructions guidées (quadrilatères ; angle donné), périmètre réel d'une figure composée sur plan. L'auteur ne reçoit que la carte. Plafond de deux devoirs par auteur : D01 et D08 (même main possible) = deux ; D06 et D09 sans mission.

**R10 — Un chapitre = un auteur à la fois ; un lot = 2 à 3 chapitres voisins** (§ 4).

## 2. Carte et écart, par chapitre

Lignes portant le chapitre (une ligne peut en porter plusieurs) : sessions 2021–2026 · 2008–2020 · devoirs ; puis les missions et questions planifiées.

| chapitre | 2021–2026 | 2008–2020 | devoirs | ce que testent les sujets | écart avec le patron | missions | q. |
| --- | ---: | ---: | ---: | --- | --- | ---: | ---: |
| `01-entiers-naturels` | 0 | 0 | 0 | aucun item (les grands nombres ne sont jamais le sujet) | patron seul, aucune mission | 0 | 0 |
| `02-operations-naturels` | 7 | 4 | 5 | opérations en contexte : somme, produit, division euclidienne des tours | étape d'arrivée des problèmes ; `02/05-entrainement#7`, `02/02-boss#4` déjà là ; pas de mission | 0 | 0 |
| `03-nombres-decimaux` | 0 | 2 | 4 | comparer des décimaux (remises) ; monnaie en millimes (un devoir partiel) | patron seul | 0 | 0 |
| `04-addition-soustraction-decimaux` | 3 | 19 | 19 | somme et différence de décimaux en contexte (prix, restes) | étape des problèmes ; `04/05-entrainement#7` pose déjà les sommes deux à deux | 0 | 0 |
| `05-multiplication-division-decimaux` | 10 | 24 | 37 | produit et quotient de décimaux, conversions d'unités (ares, quintaux, m²) : dans presque chaque problème | étape des problèmes ; patron riche, pas de mission | 0 | 0 |
| `06-multiples-communs` | 1 | 2 | 12 | multiple commun dans un intervalle avec restes égaux (2018, 2020, 2023) ; en devoir : trois nombres, encadrement, unicité | le patron donne ppcm, intervalle simple, un reste ; manque : reste égal pour 2–3 diviseurs, unicité → 3 missions d'examen + 1 de devoir | 4 | 30 |
| `07-criteres-divisibilite` | 0 | 0 | 8 | jamais en examen ; en devoir : chiffres manquants à plusieurs critères | patron : un chiffre, un critère ; manque : deux chiffres, critères cumulés → 1 mission de devoir | 1 | 6 |
| `08-fractions-sens-lecture` | 0 | 2 | 0 | 2 lignes (fraction d'un effectif) | patron seul | 0 | 0 |
| `09-fractions-equivalentes` | 0 | 1 | 1 | 1 ligne ; 1 de devoir (partiel) | patron seul | 0 | 0 |
| `10-comparaison-fractions` | 0 | 0 | 1 | 1 ligne de devoir (calcul mental) | patron seul | 0 | 0 |
| `11-addition-soustraction-fractions` | 1 | 2 | 4 | fractions successives (fractions de même dénominateur) rares | patron seul | 0 | 0 |
| `12-fractions-decimales` | 0 | 0 | 0 | aucune ligne | patron seul | 0 | 0 |
| `13-multiplication-fraction-entier` | 14 | 24 | 18 | retrouver le tout depuis une fraction, fraction supérieure à 1 d'une quantité, fractions de rapport entre deux effectifs : 14 lignes récentes | patron : fraction × entier, fraction d'un nombre, quelques « retrouver le tout » ; manque : le problème enchaîné à deux ou trois contributions → 4 missions | 4 | 28 |
| `14-proportionnalite-pourcentage` | 13 | 28 | 16 | hausse/baisse en %, tarifs à tranches, pourcentage à base inconnue ; échelle | patron riche en %, un peu d'échelle ; manque : tranches, deux contributions, base inconnue enchaînée ; échelle lue sur carte → 4 missions d'examen + 1 de devoir | 5 | 40 |
| `15-vitesse-distance-temps` | 11 | 12 | 0 | distance retrouvée par fraction/vitesse, comparaison de vitesses, justification oui/non | patron : formule et conversions ; manque : problèmes à fraction du trajet et à deux véhicules → 4 missions | 4 | 34 |
| `16-perpendicularite-parallelisme` | 0 | 1 | 5 | constructions en devoir (perpendiculaire à la base, hauteurs) | patron récent (B4) ; couvert par les missions de constructions du `19` | 0 | 0 |
| `17-angles` | 1 | 1 | 5 | l'angle de la construction (60°, 45°, 30°) | patron récent ; couvert par la mission des constructions avec angle du `19` | 0 | 0 |
| `18-triangles` | 0 | 4 | 6 | constructions de triangles en devoir ; nature selon l'angle | patron récent ; non repris | 0 | 0 |
| `19-quadrilateres` | 7 | 13 | 15 | périmètre de quadrilatères, losange par diagonales, constructions en devoir | patron récent (B4) ; manque : constructions guidées → 2 missions de devoir | 2 | 14 |
| `20-aires-polygones` | 9 | 18 | 10 | aires par somme ou différence, base ou hauteur retrouvée, ares/hectares, prix | patron enrichi par B5 ; manque : le problème enchaîné (production, recette, emprunt) → 4 missions | 4 | 42 |
| `21-cercle-disque` | 5 | 4 | 5 | longueur d'un demi-cercle, aire du disque, secteur de trois quarts, losange inscrit | patron en cours d'enrichissement (B5) ; manque : fil de demi-cercles, secteur + parallélogramme, échelle → 3 missions | 3 | 26 |
| `22-durees` | 11 | 15 | 11 | horaires d'arrivée, pauses, aller-retour, passage de minuit, cadence de bus : 11 lignes récentes | patron : conversions et sommes de durées ; manque : le problème d'horaires à plusieurs étapes → 6 missions | 6 | 54 |
| `23-solides-cube-pave` | 0 | 0 | 0 | aucune ligne (ni solide ni volume) | patron seul, aucune mission | 0 | 0 |
| `24-decomposition-fractions` | 0 | 0 | 2 | 1–2 lignes de devoir (nombre fractionnaire) | patron seul | 0 | 0 |
| `25-perimetre-figure-composee` | 3 | 5 | 3 | périmètre de figure composée : contour fermé, entrée, arc, côté commun | chapitre neuf (B5, écrit pendant le plan, à revérifier) → 4 missions d'examen + 1 de devoir, numérotées à partir de 06 | 5 | 52 |
| `26-diagrammes-batons` | 0 | 0 | 0 | aucune ligne (pas un diagramme dans les 17 sujets ni les 9 devoirs) | patron seul, aucune mission | 0 | 0 |

## 3. Missions par chapitre

| chapitre | NN | mission | sources | étage | q. | lot |
| --- | ---: | --- | --- | --- | ---: | --- |
| `06-multiples-communs` | 06 | m001 🏛️ multiples communs, puis prix d'un billet | C04 (2023) problème 1 | d3 | 6 | M1 |
| `06-multiples-communs` | 07 | m002 🏛️ fraction et écart, puis restes égaux | C07 (2020) problème 2 | d3 | 8 | M1 |
| `06-multiples-communs` | 08 | m003 🏛️ restes égaux, bénéfice fractionnaire, pourcentage du coût | C09 (2018) problème 1 | d3 | 8 | M1 |
| `06-multiples-communs` | 09 | m004 📝 Multiple commun dans un intervalle : trouver, encadrer, prouver l'unicité | devoir A (T1, école primaire), exercice 11a,11b; devoir B (T1, école primaire), exercice 1,7; devoir C (T1, école primaire), exercice 1; devoir D (T2, école primaire), exercice 6a; devoir E (T2, école primaire), exercice 1a,1b; devoir G (T3, école primaire), exercice 8e | d3 | 8 | M1 |
| `07-criteres-divisibilite` | 06 | m005 📝 Compléter les chiffres manquants pour deux, trois ou quatre critères à la fois | devoir G (T3, école primaire), exercice 8a,8b,8d | d2 | 6 | M1 |
| `13-multiplication-fraction-entier` | 06 | m006 🏛️ trois sommes et une fraction du total | C02 (2025) problème 1 | d3 | 8 | M1 |
| `13-multiplication-fraction-entier` | 07 | m007 🏛️ retrouver le prix, puis le taux de remise | C11 (2016) problème 1 | d3 | 7 | M1 |
| `13-multiplication-fraction-entier` | 08 | m008 🏛️ deux façons d'obtenir une robe | C12 (2015) problème 1 | d3 | 6 | M1 |
| `13-multiplication-fraction-entier` | 09 | m009 🏛️ le prix retrouvé par une petite fraction, puis l'économie en pourcentage | C18 (2009) problème 1 | d3 | 7 | M1 |
| `14-proportionnalite-pourcentage` | 06 | m010 🏛️ rapport entre deux genres, puis hausse de 5 % des recettes | C01 (2026) problème 1 | d3 | 7 | M2 |
| `14-proportionnalite-pourcentage` | 07 | m011 🏛️ le tarif d'un club selon le nombre d'heures | C03 (2024) problème 2 | d3 | 7 | M2 |
| `14-proportionnalite-pourcentage` | 08 | m012 🏛️ le prix d'une machine, puis les économies du père | C06 (2021) problème 1 | d3 | 10 | M2 |
| `14-proportionnalite-pourcentage` | 09 | m013 🏛️ l'argent restant, puis le prix avant la remise | C08 (2019) problème 1 | d3 | 9 | M2 |
| `14-proportionnalite-pourcentage` | 10 | m014 📝 Lire un plan et une carte à l'échelle : longueurs réelles, aller-retour, périmètre | devoir A (T1, école primaire), exercice 6,7; devoir B (T1, école primaire), exercice 12a; devoir E (T2, école primaire), exercice 2a,2b,3b,3c; devoir G (T3, école primaire), exercice 6 | d2 | 7 | M2 |
| `15-vitesse-distance-temps` | 06 | m015 🏛️ le réservoir du camion, puis la distance entre deux villes | C01 (2026) problème 2 | d3 | 8 | M2 |
| `15-vitesse-distance-temps` | 07 | m016 🏛️ montée et descente d'un cycliste | C04 (2023) problème 3 | d3 | 9 | M2 |
| `15-vitesse-distance-temps` | 08 | m017 🏛️ une voiture, un camion et une pause | C06 (2021) problème 2 | d3 | 9 | M2 |
| `15-vitesse-distance-temps` | 09 | m018 🏛️ le trajet jusqu'au centre de collecte | C10 (2017) problème 1 | d3 | 8 | M2 |
| `21-cercle-disque` | 06 | m019 🏛️ le cerf-volant et sa queue de demi-cercles | C04 (2023) problème 2 | d3 | 7 | M3 |
| `21-cercle-disque` | 07 | m020 🏛️ le parc en trois pièces | C05 (2022) problème 3 | d3 | 12 | M3 |
| `21-cercle-disque` | 08 | m021 🏛️ la fontaine : losange inscrit dans un disque | C19 (2008) problème 2 | d3 | 7 | M3 |
| `22-durees` | 06 | m022 🏛️ les tours d'une ligne de bus | C02 (2025) problème 3 | d3 | 12 | M3 |
| `22-durees` | 07 | m023 🏛️ remplir une piscine avec deux pompes | C05 (2022) problème 2 | d3 | 10 | M3 |
| `22-durees` | 08 | m024 🏛️ le bus de l'ouvrier, toutes les demi-heures | C07 (2020) problème 1 | d3 | 9 | M3 |
| `22-durees` | 09 | m025 🏛️ retour à la station, puis la capacité du réservoir | C08 (2019) problème 2 | d3 | 9 | M3 |
| `22-durees` | 10 | m026 🏛️ l'excursion : heure de départ, vitesse du retour | C12 (2015) problème 2 | d3 | 7 | M3 |
| `22-durees` | 11 | m027 🏛️ un trajet de nuit, du jeudi au vendredi | C17 (2010) problème 2 | d3 | 7 | M3 |
| `19-quadrilateres` | 06 | m028 📝 Construire un trapèze rectangle et un losange à partir de leurs données | devoir B (T1, école primaire), exercice 6,12b; devoir C (T1, école primaire), exercice 5a; devoir D (T2, école primaire), exercice 4a,4c; devoir E (T2, école primaire), exercice 3a | d3 | 7 | M4 |
| `19-quadrilateres` | 07 | m029 📝 Construire avec un angle donné : parallélogramme, losange, triangle | devoir A (T1, école primaire), exercice 10; devoir C (T1, école primaire), exercice 5b; devoir D (T2, école primaire), exercice 4b; devoir F (T3, école primaire), exercice 8c; devoir G (T3, école primaire), exercice 7b,7c | d3 | 7 | M4 |
| `20-aires-polygones` | 06 | m030 🏛️ le voilier en cuivre : masse, aire, un carré y tient-il ? | C02 (2025) problème 2 | d3 | 9 | M4 |
| `20-aires-polygones` | 07 | m031 🏛️ un terrain en trois pièces, le coût du projet, le plan | C09 (2018) problème 3 | d3 | 12 | M4 |
| `20-aires-polygones` | 08 | m032 🏛️ la ferme d'orangers : aire, recette, revenu net | C14 (2013) problème 3 | d3 | 10 | M4 |
| `20-aires-polygones` | 09 | m033 🏛️ le trapèze au 1/500, le prix, la part empruntée | C15 (2012) problème 3 | d3 | 11 | M4 |
| `25-perimetre-figure-composee` | 06 | m034 🏛️ le jardin écologique : aires par différence, base, périmètre | C01 (2026) problème 3 | d3 | 10 | M4 |
| `25-perimetre-figure-composee` | 07 | m035 🏛️ le jardin public : aires en ares, parcours du coureur | C06 (2021) problème 3 | d3 | 12 | M4 |
| `25-perimetre-figure-composee` | 08 | m036 🏛️ deux terrains voisins : l'aire, le prêt, la clôture | C08 (2019) problème 3 | d3 | 12 | M4 |
| `25-perimetre-figure-composee` | 09 | m037 🏛️ le losange et le demi-disque : côté, mur avec entrée, plan | C11 (2016) problème 3 | d3 | 11 | M4 |
| `25-perimetre-figure-composee` | 10 | m038 📝 Périmètre réel d'une figure composée lue sur un plan à l'échelle | devoir D (T2, école primaire), exercice 1; devoir E (T2, école primaire), exercice 4; devoir G (T3, école primaire), exercice 5 | d3 | 7 | M4 |

**32 missions d'examen et 6 de devoirs, 326 questions** ; 74 sur 119 (32 problèmes sur 51, 17 sessions sur 17) ; 35 sur 111 (hors D09, calcul mental, et la version B de D02, jumelle de A).

**Sessions reprises (17 sur 17)** : 2026 (P1+P2+P3) ; 2025 (P1+P2+P3) ; 2024 (P2) ; 2023 (P1+P2+P3) ; 2022 (P2+P3) ; 2021 (P1+P2+P3) ; 2020 (P1+P2) ; 2019 (P1+P2+P3) ; 2018 (P1+P3) ; 2017 (P1) ; 2016 (P1+P3) ; 2015 (P1+P2) ; 2013 (P3) ; 2012 (P3) ; 2010 (P2) ; 2009 (P1) ; 2008 (P2).

## 4. Lots d'auteurs (une carte par lot)

| lot | chapitres | missions | auteurs | parallélisme |
| --- | --- | --- | --- | --- |
| M1 | 06, 07, 13 | m001–m009 (9 ; 64 q) | 1 | tout de suite, en parallèle de M2 |
| M2 | 14, 15 | m010–m018 (9 ; 74 q) | 1 | tout de suite, en parallèle de M1 |
| M3 | 21, 22 | m019–m027 (9 ; 80 q) | 1 (ou 2 : 21 / 22) | **après** le rapport B5 pour le `21` ; le `22` peut partir seul |
| M4 | 19, 20, 25 | m028–m038 (11 ; 108 q) | 2 (19+20 / 25) | `19` tout de suite ; `20` après B5 ; `25` quand B5 l'a écrit |

Skills : `content-ecole-tn`, puis `prof-math-6eme`. Consignes : `content-ingest/references/gisement-auteur-examen.md` (examens, avec la transcription de chaque session) et `gisement-auteur-devoir.md` (devoirs : la carte seule). **Ordre dans un lot** : les ids d'étiquette neufs, puis les missions du chapitre dans l'ordre de la carte, puis les gates.

**État du lot B5 au moment du plan (2026-10-19, 23 h 30 UTC)** — « ne pas redemander » à REVÉRIFIER au lancement de M3 et M4 :

- `20-aires-polygones` : mis à niveau (cours, résumé, quiz à 7 q, exercices 9–10 q) ; considéré stable ;
- `21-cercle-disque` : en cours (exercices réécrits à 23 h 36 ; B5 peut encore le modifier) ;
- `23-solides-cube-pave` : mis à niveau (exercices à 21 h 25) ; aucune mission n'y va ;
- `25-perimetre-figure-composee` : **apparu pendant le plan** (relevé à 21 h 35 : cours, résumé, quiz à 5 q, exercices `01`–`05` de 6 q) ; les listes « ne pas redemander » de ses missions en tiennent compte, mais B5 peut encore le retoucher : à relire au lancement.
- Les empreintes des fichiers sont dans `b5-etat-au-plan.json` ; les missions concernées sont marquées 🔁 dans les cartes. Les `NN` supposent que les chapitres ont `01`–`05` : si B5 ajoute un fichier, décaler.

## 5. Ce qui est écarté, et pourquoi

| écarté | pourquoi |
| --- | --- |
| 2024 P1 (haies), 2016 P2 (réservoir et vitesse requise), 2013 P1 (ligne brisée à l'échelle 1/4 000 000 et pause), 2012 P2 (distance et coût du carburant), 2010 P3 (trapèze rectangle, prix à l'hectare, épargne), 2015 P3 (rectangle coupé, marges), 2008 P1 (tempérament ou comptant) | Problèmes SAINS mais redondants avec un problème repris (même archétype, mêmes gestes) : réserve de 7 missions possibles si le pilote veut plus de volume (décision E-1). Chaque session reste reprise au moins une fois. |
| 2008 P3 (camion en panne, 3/2 du chemin, carburant) | jumeau de 2017 P1 (mêmes gestes, autres nombres) : un seul des deux est repris. |
| 2017 P3 (triangle, demi-disque, hauteur 39,25 m) | énoncé défectueux (hauteur incompatible avec les autres données), à ne pas reprendre tel quel. |
| 2009 P2 (terrain 3/8, 1/3, 686 m² ; « 4/3 » de la part de l'association) | énoncé ambigu (4/3 imprimé, incohérent avec 2/3). La q1 seule est saine : option de repêchage (E-6). |
| 2013 P2 (deux remises, prix du lot) | la q2 retranche le prix de l'ordinateur d'un prix de LOT : ambigu. La q1 (comparer 20 % à un prix final) est saine : option (E-6). |
| 2020 P3 (triangle de 6 ares, route parallélogramme) | la q1 (périmètre de 114 m) exige les côtés de l'angle droit, c'est-à-dire Pythagore (`HP:pythagore`, écarté) ; q2 en dépend ; la q3 (échelle) est prise ailleurs. Option : donner le périmètre « on admet ». |
| 2024 P3 (plateau de dix parallélogrammes) | la q3 (nombre de chaises autour de la table) suppose les côtés obliques, non portés par la figure ; q1–q2 seules ne font que 5 étapes d'aire déjà bien servies au `20` (E-6). |
| 2022 P1, 2012 P1, 2010 P1, 2017 P2, 2009 P3 (crédit, intérêt, somme et écart, somme et rapport) | cible ◐ « rencontrée, non enseignée » (`HP:interet`, `HP:somme-difference`, `HP:somme-rapport`) : aucune mission ne les cible. Chacune revient dans 2 ou 3 sessions seulement (sous le seuil de 6 proposé pour un cours). |
| 2018 P2 (marche puis bus, demi-heure, panne) | énoncé ambigu signalé par le lecteur (la demi-heure couvre-t-elle les deux étapes ?) ; sain si on lit « marche + bus = 30 min », mais écarté au profit de problèmes plus nets. Option (E-6). |
| Lignes C03#3c (2024) et C17#3c (2010) | C03#3c reste classée `25` sans mission (voir 2024 P3). C17#3c (contour d'un trapèze rectangle avec ouverture) est jugée NON composée et reste en `04`+`14`+`19`. |

## 6. Les devoirs : ce qu'ils apportent vraiment

La vague 1 (neuf devoirs, 124 lignes ; 111 hors calcul mental D09 et jumeau B de D02) recoupe la fiche : 3 lignes sur 124 portent un jeton `HP:` (somme-écart ×2, somme-rapport ×1), aucun devoir n'est « ancien ». Le registre note l'évaluation **par critère** (pas de barème par question). Mesure de la règle des 30 % (famille au niveau gabarit, contre les 119 lignes d'examen) : environ **37 % des lignes (41 sur 111)** relèvent de familles que les examens ne posent pas (constructions guidées 22, divisibilité et multiples sans intervalle 13, monnaie 6, périmètre composé sur plan en partie), au-dessus du seuil de 30 %. Mais les six missions en reprennent 35, et ce qui reste (monnaie en millimes, un seul devoir partiel ; calcul mental) n'est pas mission : **pas de vague 2 proposée** (E-8), le pilote décide.

Plafond par auteur : D01 et D08 portent la même mise en page (même main possible) : deux, respecté.

## 7. Décisions déjà prises (coordinateur, 2026-10-19)

Format du concours (1 h, trois problèmes à étapes, aucun QCM) ; une mission d'examen reprend un problème entier avec la phrase officielle citée et la session dite ; énoncés défectueux non repris tels quels (2017 P3, 2009 P2, 2013 P2, C07 3a) ; D04/D06/D07 partiels, D09 calcul mental sans mission, D02 comptée une fois ; `HP:interet`, `HP:somme-difference`, `HP:somme-rapport` jamais ciblés ; reclassement en `25` des lignes de périmètre de figure composée.

## 8. Décisions à soumettre au pilote

| # | question et proposition |
| --- | --- |
| E-1 | volume : 38 missions, 326 questions ; le `22` reçoit 6 missions (54 q), le `25` 5 (52 q), le `06` 4 (30 q) ; 7 problèmes sains restent en réserve (liste dans « écartés »). Ordre de coupe conseillé si on allège : m027 (2010 P2), m026 (2015 P2), puis m013 (2019 P1) ; ordre d'ajout si on veut plus : 2024 P1 (cadence et vitesses) au `22`, 2016 P2 au `15`. |
| E-2 | étage : les 32 missions d'examen sont d3 (boss 120/30) parce que chaque problème contient au moins une ligne d3 ; beaucoup contiennent aussi une ligne d4, plafonnée à d3 (règle « jamais d4 »). Alternative : d4 `challenge` 300/60 pour les trois plus lourdes (m035 2021 P3, m031 2018 P3, m020 2022 P3). |
| E-3 | placements par exception (règle : chapitre le plus avancé de l'exercice) : 2023 P1, 2020 P2 et 2018 P1 au `06` (étape neuve = multiple commun dans un intervalle, plus avancé = 14 ou 13) ; 2016 P1, 2015 P1, 2009 P1 au `13` (retrouver le tout, fraction > 1 ; plus avancé = 14) ; 2019 P3 au `25` (contour avec ouverture ; le plus avancé serait 20 si l'on suit les chapitres de la ligne) ; la mission des constructions avec angle au `19` (plus avancé de 17, 18, 19). Lignes reclassées en `25` par ordre du coordinateur : C01 3c, C03 3c, C06 3c, C07 3a, C07 3b, C08 3c, C10 3c, C11 3b ; C17 3c jugée non composée ; C03 3c (2024) et C08 3c (2019) sont en réalité des contours simples avec chaises ou entrée : à confirmer. |
| E-4 | 2026 P3 q3 (périmètre de ب ج د ن) : le côté du losange se déduit de ج و = 5 par Pythagore (hors programme). Proposition : donner « ج و = 5 صم » dans l'énoncé (on admet), ce qui rend la q3 solvable (côté = 5 + 3 = 8, périmètre 32 cm) ; sinon écarter la q3 et déplacer la mission au `20`. |
| E-5 | constructions : 5 sessions (2022, 2020, 2018, 2016, 2015) demandent un plan à l'échelle ; elles ne sont pas notables en QCM. Proposition : une question de conversion d'échelle + 1 ou 2 `ordering` d'étapes, pas de dessin. Pas de mission dédiée aux constructions d'examen ; les gestes sont portés par les deux missions de devoir du `19`. |
| E-6 | repêchages possibles (énoncés fragiles) : 2013 P2 q1 (une remise en %, contre un prix final), 2009 P2 q1 (3/8, 1/3 et un reste), 2018 P2 (marche et bus, lecture « 30 min pour les deux étapes »), 2020 P3 avec « on admet que le périmètre vaut 114 m ». Défaut : aucun. |
| E-7 | ◐ : cinq problèmes écartés visent l'intérêt, le partage somme-écart ou somme-rapport (revient dans 2 ou 3 sessions, pas 6). Défaut : aucune ligne de cours, aucune mission. Si le pilote veut enseigner « somme et écart » au `04` ou au `14`, 5 problèmes (2022 P1, 2017 P2, 2012 P1, 2010 P1, 2009 P3) se rouvrent. |
| E-8 | devoirs : 6 missions de salle blanche (06, 07, 14, 19 ×2, 25) pour 35 lignes sur 111. D06 (monnaie et métrique, presque sans géométrie, support manquant) et D09 (feuille de calcul mental) n'ont aucune mission ; proposition : les passer à `ecarte` dans `documents`. Mesure de la règle des 30 % : voir § 6 ; proposition : pas de vague 2. |
| E-9 | lots et auteurs : 4 lots (M1 06·07·13 : 9 missions ; M2 14·15 : 9 ; M3 21·22 : 9 ; M4 19·20·25 : 11). M4 a deux auteurs (19+20 d'un côté, 25 de l'autre) ; M3 et M4 touchent les chapitres 20, 21, 25 encore écrits par B5 : ne lancer M3 et M4 qu'après le rapport B5, M1 et M2 tout de suite, en parallèle. |
| E-10 | `23-solides-cube-pave` et `26-diagrammes-batons` : aucune mission (aucun solide, aucun diagramme dans les 17 sujets ni les 9 devoirs). Le `26` et le `23` restent servis par leur patron. |

## 9. Décisions du pilote (2026-10-19 / 20, sur les propositions E-1 à E-10)

| | Décision |
| --- | --- |
| **E-1** | Volumes acceptés (22 : 54 q., 25 : 52 q.) ; l'ordre de coupe ne sert que si un audit juge un chapitre saturé. Les 7 problèmes sains restent en réserve. |
| **E-2** | Toutes les missions d'examen en **d3** (boss 120/30), comme le français 6ᵉ ; pas de d4. |
| **E-3** | Placements par exception acceptés tels que proposés. |
| **E-4** | 2026 P3 q3 : la donnée manquante **est donnée dans l'énoncé** (« ج و = 5 صم », précédent E6 du français 6ᵉ) — jamais Pythagore. |
| **E-5** | Constructions converties (conversion d'échelle, ordre des étapes, choix de figure), sans dessin demandé. |
| **E-6** | **Aucun repêchage** (précédent E1 du français 6ᵉ) : les problèmes écartés pour défaut le restent. |
| **E-7** | Les problèmes ◐ restent sans cours ni mission. |
| **E-8** | D06 et D09 passent à `ecarte` dans `documents` ; pas de vague 2. |
| **E-9** | M1 et M2 partent tout de suite ; M3 et M4 après le rapport B5 (22 et 19 peuvent partir seuls). |
| **E-10** | Aucune mission pour 23 et 26. |

## 10. Décisions du pilote après l'audit M1 + M2 (2026-10-20)

| | Décision |
| --- | --- |
| **E-11** (M-1) | Les missions 2020 P2 et 2018 P1, placées au 06 par l'exception E-3, **passent au ch. 13** : 10 de leurs 16 questions exigent la fraction d'une quantité et le retour au tout (ch. 08 et 13), non enseignés au 06. Renommage `13/…` (missions non publiées : aucun id servi ne bouge), registre `chapitre`/`fichier` mis à jour. |
| **E-12** (C-1) | Nombres à chiffre manquant (`2▢4`) inversés en RTL : **correctif moteur** (`isolateLtrRuns`, PR moteur), qui couvre aussi le ch. 07 déjà servi ; pas de réécriture en toutes lettres côté contenu. La livraison attend le merge du correctif moteur. |
