# Carte d'affectation M4 — maths 6ᵉ, chapitres `19`, `20`, `25` (missions du gisement)

> Lot auteur du passage unique (PLAN-gisement.md § 4). 11 missions, 108 questions. Skills : `content-ecole-tn`, puis `prof-math-6eme` (calibre les étages, jamais plus que le programme) ; consignes `content-ingest/references/gisement-auteur-examen.md` (missions 🏛️ : la transcription de la session citée, `content/programmes-officiels/examens-nationaux/6eme-base/math/<année>-unique.md`) et `gisement-auteur-devoir.md` (missions 📝 : la carte seule, jamais le devoir). Écris en arabe (`contentLanguage` du sujet). Ne touche à aucun autre chapitre que les tiens ; les autres lots écrivent en parallèle. Nom de fichier : `exercices/<fichier>` ci-dessous.

**Règles communes** (PLAN-gisement.md § 1) : une mission d'examen reprend UN problème entier d'une session, découpé en étapes notées ; chaque question dit sa session (« مناظرة 2023 ») et redonne les données et la phrase OFFICIELLES de la transcription qu'elle lit (valeurs, unités, décimaux à trois chiffres tels qu'imprimés, tableau refait lisible) ; un « أثبتُ أنّ… » devient « quelle valeur / quelle justification » (jamais la clé dans le titre ni dans l'énoncé) ; types natifs : `numeric` pour les valeurs, QCM pour le choix d'étape, la justification et la décision, `ordering` pour un raisonnement ou les étapes d'une construction ; une CONSTRUCTION n'est pas notable : on note les longueurs du plan (échelle) et l'ordre des étapes ; figures refaites en SVG, vraies, sans donner la clé ; π = 3,14 ; aucune algèbre littérale, ni Pythagore, ni somme des angles d'un triangle, ni calcul d'intérêt, ni partage « somme et écart / somme et rapport » (◐) ; jamais de corrigé de site tiers : l'explication est la tienne, re-résolue par deux chemins ; au plus 12 questions ; étage d3 = `boss` 120/30, d2 = `practice` 75/15. Étiquettes : `misconceptionTag` du registre `math.*` sur le distracteur qui EXÉCUTE l'erreur du « piège » de la ligne, jamais sur un multi, un ordering ni un matching ; un id qui manque se signale (on ne touche ni `content/misconceptions.json` ni `content/competences/`). `chapter.json` : ajoute à `sources[]` — missions d'examen : « Sujets officiels du concours d'entrée aux collèges pilotes (6ᵉ année de base), Ministère de l'Éducation (corpus officiel, reprise citée, étude 36) — transcriptions : programmes-officiels/examens-nationaux/6eme-base/math/ » ; missions de devoir : « Calibré sur des devoirs publics (étude 36, T2′, aucune reprise) — carte : programmes-officiels/sources-externes/web-6eme-base-math/fiche.md ». Numéros de fichiers : à la suite de `05-entrainement` (06, 07, …), `displayOrder` à la suite ; les missions de chaque chapitre dans l'ordre de la carte. Gates à chaque chapitre : `content:check`, `content:qa -- --subject math-6eme` (0 erreur), `content:tranche -- --subject math-6eme --changed --fresh --strict-longest`.

**Étiquettes déjà en usage dans tes chapitres** : `19` : `math.geo.quadrilatere-mal-identifie` (Reprends les deux critères : les angles sont-ils droits ? le); `math.geo.paires-de-cotes-paralleles-mal-comptees` (Compte les paires parallèles : le trapèze n'en a qu'UNE, le ); `math.geo.parallelogramme-sommets-mal-ordonnes` (Tu ordonnes mal les sommets du parallélogramme : dans ABCD, ); `math.geo.condition-suffisante-supposee` (Tu prends une seule propriété pour une preuve : il faut tout); `math.mes.perimetre-nombre-de-cotes-errone` (Tu multiplies par le mauvais nombre de côtés : un carré et u); `math.geo.diagonales-proprietes-mal-attribuees` (Tu attribues à un quadrilatère les diagonales d'un autre : m) | `20` : `math.mes.aire-et-perimetre-confondus` (Tu confonds l'aire et le périmètre : le périmètre s'addition); `math.mes.conversion-aire-facteur-errone` (Une unité d'aire se convertit par 100, pas par 10 : 1 m² = 1); `math.mes.aire-triangle-sans-moitie` (Tu oublies de diviser par 2 l'aire du triangle : c'est la mo); `math.num.chiffres-juxtaposes-au-lieu-du-produit` (Tu écris les deux nombres l'un à côté de l'autre au lieu de ); `math.mes.aire-division-par-deux-appliquee-a-tort` (Tu divises par 2 une aire de rectangle ou de parallélogramme); `math.mes.aire-trapeze-sans-demi-somme` (L'aire d'un trapèze est la DEMI-somme des deux bases multipl) | `25` : .

## ⚠️ Chapitres encore en écriture (lot B5) — à revérifier au lancement

État relevé par le planificateur le **2026-10-19 23:37 UTC** (`b5-etat-au-plan.json` : empreintes par fichier). B5 travaille dans l'ordre 20 → 21 → 23 → 25 (`auteurs-notes/B5/NOTES.md`). À ce relevé : `20-aires-polygones` mis à niveau (cours, quiz 7 q, exercices +3/+4 questions, rien d'autre à attendre) ; `21-cercle-disque` en cours (exercices 01–05 réécrits à 23 h 36 : les indices de « ne pas redemander » ci-dessous sont vérifiés contre cet état, mais B5 peut y revenir) ; `23-solides-cube-pave` mis à niveau (exercices modifiés à 21 h 25 ; aucune mission du gisement n'y va : aucun solide dans les 17 sujets ni les 9 devoirs) ; `25-perimetre-figure-composee` **est apparu pendant le plan** (relevé à 21 h 35 : quiz à 5 q, exercices `01`–`05` de 6 q chacun, cours et résumé ; B5 peut encore le retoucher) : les listes « ne pas redemander » des missions du `25` en tiennent compte (contour extérieur, côté commun, demi-cercles, échelle, plantations sur contour fermé), les missions partent de `06`.

**Au lancement de ce lot** : (1) relire le rapport B5 et refaire l'inventaire des chapitres 20, 21 et 25 (`NN/fichier#n`) ; (2) comparer aux empreintes ; (3) rouvrir chaque liste « Ne pas redemander » concernée (indices décalés, questions ajoutées ou retirées) et, pour le `25`, relire ses exercices 01–05 (leçon 24 : contour extérieur, côté commun qui disparaît, arc retranché, contour fermé, échelle, arrondi par excès) ; (4) vérifier le plus grand `NN` existant de chaque chapitre : si B5 a ajouté un fichier 06+, décaler la plage. Les listes ci-dessous sont valables pour l'état relevé, pas pour un état ultérieur ; les missions concernées sont marquées 🔁.


## Chapitre `19-quadrilateres`

### m028 → `exercices/06-devoir-construire-trapeze-rectangle-et-losange.json` · d3 boss 120/30 · 7 questions · régime **devoir (salle blanche)**

- Titre de travail (arabe : « ⭐ تمرين موجّه / ⚔️ زعيم الفرض ⭐⭐⭐: … ») : Construire un trapèze rectangle et un losange à partir de leurs données ⭐⭐⭐
- Registre : id `D02#6` ; sources `D02#6, D02#12b, D03#5a, D04#4a, D04#4c, D05#3a`
- Cartes : devoir B (T1, école primaire), exercice(s) 6, 12b ; devoir C (T1, école primaire), exercice(s) 5a ; devoir D (T2, école primaire), exercice(s) 4a, 4c ; devoir E (T2, école primaire), exercice(s) 3a — cartes anonymes
- Gestes lus (archétype des lecteurs, sans nombre) :
  - D02#6 (d3) : construire un trapèze rectangle depuis ses deux bases et sa hauteur
  - D02#12b (d3) : construire un trapèze rectangle depuis ses bases et sa hauteur sur plan
  - D03#5a (d3) : construire un trapèze rectangle depuis des dimensions réelles et une échelle
  - D04#4a (d3) : construire un trapèze rectangle depuis une hauteur, une somme et une différence de bases
  - D04#4c (d3) : construire un losange depuis ses deux diagonales
  - D05#3a (d3) : dessiner un trapèze rectangle depuis ses quatre côtés avec règle et compas
- Étapes prévues :
  - Un trapèze rectangle à partir de ses deux bases et de sa hauteur : QCM du côté perpendiculaire aux bases, ordering des étapes (base, perpendiculaire à l'extrémité, report de la hauteur, parallèle, côté oblique) — 2 q.
  - Un trapèze rectangle à partir de la SOMME et de la DIFFÉRENCE des bases et de la hauteur (les deux bases se retrouvent avant de construire) : numérique des bases, QCM de l'étape de report au compas du côté oblique — 2 q.
  - À l'échelle : les dimensions réelles données en mètres, le plan en centimètres : QCM de conversion — 1 q.
  - Un losange à partir de ses deux diagonales : QCM « les diagonales se coupent en leur milieu et perpendiculairement », ordering — 2 q.
- Pièges (étiquette à porter par un distracteur) :
  - tracer la hauteur sans perpendicularité à la base — ligne D02#6 (d3)
  - tracer la hauteur sans perpendicularité à la base — ligne D02#12b (d3)
  - se tromper de conversion entre mètres et centimètres — ligne D03#5a (d3)
  - traiter la somme des bases comme une base — ligne D04#4a (d3)
  - ne pas faire couper les diagonales en leur milieu — ligne D04#4c (d3)
  - placer le côté oblique sans reporter sa longueur au compas — ligne D05#3a (d3)
- Ne pas redemander : `19/05-entrainement#2`, `19/05-entrainement#3`, `19/04-defi#8`, `19/04-defi#5`, `16/02-boss#7`, `16/02-boss#8`, `16/05-entrainement#4`, `17/02-boss#7`, `17/04-defi#8`, `18/02-boss#8`
- Note : Salle blanche. Une construction n'est pas notable en QCM : la mission fait porter les questions sur le CHOIX et l'ORDRE des étapes et sur les mesures à reporter. Gestes absents des missions d'examen : trapèze rectangle (données directes ou par somme et différence des bases), losange par ses diagonales. Les constructions à l'échelle des examens (2022, 2018, 2016…) sont prises par les missions d'examen de leur problème. Piège : tracer la hauteur sans perpendicularité à la base ; ne pas reporter le côté oblique au compas ; ne pas faire couper les diagonales en leur milieu.

### m029 → `exercices/07-devoir-construire-avec-un-angle-donne.json` · d3 boss 120/30 · 7 questions · régime **devoir (salle blanche)**

- Titre de travail (arabe : « ⭐ تمرين موجّه / ⚔️ زعيم الفرض ⭐⭐⭐: … ») : Construire avec un angle donné : parallélogramme, losange, triangle ⭐⭐⭐
- Registre : id `D01#10` ; sources `D01#10, D04#4b, D07#8c, D08#7b, D03#5b, D08#7c`
- Cartes : devoir A (T1, école primaire), exercice(s) 10 ; devoir C (T1, école primaire), exercice(s) 5b ; devoir D (T2, école primaire), exercice(s) 4b ; devoir F (T3, école primaire), exercice(s) 8c ; devoir G (T3, école primaire), exercice(s) 7b, 7c — cartes anonymes
- Gestes lus (archétype des lecteurs, sans nombre) :
  - D01#10 (d3) : construire un losange depuis une diagonale et un angle puis un carré sur un côté
  - D04#4b (d2) : construire un parallélogramme depuis deux côtés et un angle
  - D07#8c (d2) : construire un triangle depuis deux côtés et l’angle compris
  - D08#7b (d2) : construire un parallélogramme depuis deux côtés et un angle
  - D03#5b (d3) : construire un triangle depuis deux côtés réels, une échelle et un angle donné
  - D08#7c (d2) : construire un triangle rectangle dont deux côtés sont égaux
- Étapes prévues :
  - Un parallélogramme à partir de deux côtés et de l'angle compris : QCM du sommet où poser l'angle, ordering des étapes (côté, angle au rapporteur, report du second côté, parallèles) — 2 q.
  - Un losange à partir d'une diagonale et d'un angle, puis un carré sur un de ses côtés : QCM du sommet de l'angle, du report des longueurs — 2 q.
  - Un triangle à partir de deux côtés et de l'angle compris (à l'échelle), puis un triangle rectangle dont les deux côtés de l'angle droit sont égaux : QCM des longueurs sur le plan, QCM de l'égalité à reporter — 3 q.
- Pièges (étiquette à porter par un distracteur) :
  - placer l’angle au mauvais sommet — ligne D01#10 (d3)
  - placer l’angle au mauvais sommet — ligne D04#4b (d2)
  - placer l’angle au mauvais sommet — ligne D07#8c (d2)
  - placer l’angle au mauvais sommet — ligne D08#7b (d2)
  - mal convertir les longueurs réelles à l’échelle — ligne D03#5b (d3)
  - ne pas reporter l’égalité des côtés de l’angle droit — ligne D08#7c (d2)
- Ne pas redemander : `17/01-pratique#8`, `17/02-boss#7`, `17/02-boss#8`, `17/04-defi#7`, `17/04-defi#8`, `17/05-entrainement#3`, `17/05-entrainement#4`, `18/01-pratique#7`, `18/01-pratique#9`, `18/03-revision#7`, `18/02-boss#8`, `19/05-entrainement#3`, `19/05-entrainement#2`
- Note : Salle blanche. Placement au `19` (chapitre le plus avancé parmi 17, 18, 19) : exception déclarée pour les triangles, déjà bien servis au `17` et au `18` par le patron. Geste neuf : l'angle du rapporteur posé au bon sommet, avec la longueur déjà reportée sur l'autre côté. Piège : placer l'angle au mauvais sommet ; ne pas reporter l'égalité des côtés de l'angle droit. La somme des angles d'un triangle n'est JAMAIS demandée (arbitrage M3).


## Chapitre `20-aires-polygones` 🔁 (B5)

### m030 → `exercices/06-exam-2025-p2-voilier-en-cuivre-et-carre.json` · d3 boss 120/30 · 9 questions · régime **examen** · 🔁

- Titre de travail (à écrire en arabe : « 🏛️ مناظرة 2025 · المسألة 2 ⭐⭐⭐: … ») : Concours 2025 · problème 2 · le voilier en cuivre : masse, aire, un carré y tient-il ? ⭐⭐⭐
- Registre : id `C02#2a` ; sources `C02#2a, C02#2b`
- Source : C02 (session 2025), problème 2 — transcription `2025-unique.md`
- Phrases officielles à reprendre (questions numérotées du sujet) :
  - 1) أثبتُ أنّ قيس مساحة الجزء ① يساوي 4000 صم² علما أنّ قيس مساحة الجزأين ② و ③ معًا يُمثّل 45% قيس مساحة الجزء ①.
  - 2) هل يُمْكِنُهُ ذلك علما أنّ قيس طول القاعدة الكبرى [أ ب] يساوي 140 صم وهو يُمثّل 7/3 قيس طول القاعدة الصّغرى [د ج]؟ علّل جوابك.
- Étapes prévues :
  - q1 (« أثبتُ أنّ قيس مساحة الجزء ① يساوي 4000 صم² ») : masse du cuivre = 12 − 1,56 = 10,44 kg = 10 440 g ; aire totale des trois pièces = 10 440 ÷ 180 × 100 = 5800 cm² ; les pièces ② et ③ valent 45 % de la pièce ① donc les trois ensemble 145 % de ① : 5800 ÷ 1,45 = 4000 cm² — QCM de la masse du cuivre (sans le tube), numériques de l'aire totale, du pourcentage cumulé, de l'aire ① — 5 q.
  - q2 (le carré de 30 cm y tient-il ?) : petite base = 140 ÷ 7 × 3 = 60 cm ; hauteur = 2 × 4000 ÷ (140 + 60) = 40 cm ; le carré tient (30 < 40 et 30 < 60) — numériques de la petite base et de la hauteur, QCM de la décision avec la justification (hauteur ET petite base) — 4 q.
- Pièges (étiquette à porter par un distracteur) :
  - retrancher le pourcentage de l'aire totale au lieu de retrouver le tout — ligne C02#2a (d4)
  - comparer le carré à la petite base sans passer par la hauteur — ligne C02#2b (d4)
- Ne pas redemander : `20/02-boss#4`, `20/02-boss#8`, `20/04-defi#2`, `20/04-defi#4`, `20/04-defi#9`, `20/05-entrainement#5`, `20/05-entrainement#10`, `20/02-boss#10`, `14/02-boss#10`, `14/04-defi#5`, `05/05-entrainement#6`
- Note : Pièges : retrancher le pourcentage de l'aire totale au lieu de retrouver le tout ; comparer le carré à la petite base sans passer par la hauteur (ou l'inverse). Le trapèze est isocèle. La figure (voilier) est refaite en SVG sans cote (les données sont dans le texte). `20` : état relevé le 2026-10-19 à 21 h 25 (mis à niveau par B5) ; à revérifier au lancement.

### m031 → `exercices/07-exam-2018-p3-terrain-carre-parallelogramme-triangle.json` · d3 boss 120/30 · 12 questions · régime **examen** · 🔁

- Titre de travail (à écrire en arabe : « 🏛️ مناظرة 2018 · المسألة 3 ⭐⭐⭐: … ») : Concours 2018 · problème 3 · un terrain en trois pièces, le coût du projet, le plan ⭐⭐⭐
- Registre : id `C09#3a` ; sources `C09#3a, C09#3b, C09#3c`
- Source : C09 (session 2018), problème 3 — transcription `2018-unique.md`
- Phrases officielles à reprendre (questions numérotées du sujet) :
  - 1. أُحسب قيس مساحة كامل الأرض إذا علمت أنّ قيس مساحة القطعة أ ب س د يُساوي 12,5 هـ آ (unité imprimée « ها » : hectares).
  - 2. أُحسب كلاً من ثمن شراء الآلات الفلاحيّة ومعلوم كراء الأرض إذا علمت أنّ كلفة المشروع بلغت 122499 د.
  - 3. إبنِ تصميما للقطعة ن س هـ ج حسب السلّم 1/10000.
- Étapes prévues :
  - q1 (aire de tout le terrain, la pièce carrée valant 12,5 ha) : le triangle ABC a pour base BC = 350 m et pour hauteur la demi-diagonale AN = 250 m (les diagonales du carré sont perpendiculaires) : 43 750 m² ; le parallélogramme BCHS a pour base BC et pour hauteur SN = 250 m : 87 500 m² ; total = 125 000 + 43 750 + 87 500 = 256 250 m² = 25,625 ha — QCM de la hauteur à prendre, numériques, QCM d'unité (m², ha) — 6 q. Figure à relire au PDF officiel avant d'écrire (hauteurs lues sur la figure).
  - q2 (prix des machines et loyer, coût du projet 122 499 d) : loyer = 25 % du prix des machines ; bassin = 1/10 de ce prix ; projet = prix + 1/4 prix + 1/10 prix = 27/20 du prix (1,35) ; prix = 122 499 ÷ 1,35 = 90 740 d ; loyer = 22 685 d — QCM de l'écriture « 27/20 », numériques — 4 q.
  - q3 (plan au 1/10 000 du quadrilatère NSHC, trapèze rectangle de bases CN = 600 m et SH = 350 m, hauteur NS = 250 m) : longueurs sur le plan 6 cm, 3,5 cm, 2,5 cm (mètres → centimètres, puis ÷ 10 000) ; ordering des étapes de la construction — 2 q.
- Pièges (étiquette à porter par un distracteur) :
  - oublier une parcelle ou confondre les unités d'aire — ligne C09#3a (d4)
  - calculer le pourcentage sur le coût total au lieu du prix d'achat — ligne C09#3b (d3)
  - mélanger mètres et centimètres du dessin — ligne C09#3c (d3)
- Ne pas redemander : `20/02-boss#3`, `20/04-defi#1`, `20/04-defi#5`, `20/02-boss#9`, `20/04-defi#7`, `20/quiz#7`, `20/02-boss#7`, `20/03-revision#7`, `20/05-entrainement#7`, `14/01-pratique#7`, `14/05-entrainement#7`, `19/05-entrainement#3`
- Note : Figure refaite en SVG (carré ABSD de diagonales AN = 250 m, parallélogramme BCHS accolé, triangle ABC au-dessus ; C, B, N alignés). Pièges : oublier une pièce ou confondre les unités d'aire ; calculer la hauteur du triangle avec la mauvaise perpendiculaire ; ajouter 1/4 et 1/10 au lieu de les ajouter à 1. Q3 est un plan (le lecteur le classait 14, 17, 18) : la mission le réduit à deux questions de conversion et d'ordre. `20` en cours de mise à niveau (B5).

### m032 → `exercices/08-exam-2013-p3-ferme-orangers-triangle-trapeze.json` · d3 boss 120/30 · 10 questions · régime **examen** · 🔁

- Titre de travail (à écrire en arabe : « 🏛️ مناظرة 2013 · المسألة 3 ⭐⭐⭐: … ») : Concours 2013 · problème 3 · la ferme d'orangers : aire, recette, revenu net ⭐⭐⭐
- Registre : id `C14#3a` ; sources `C14#3a, C14#3b, C14#3c`
- Source : C14 (session 2013), problème 3 — transcription `2013-unique.md`
- Phrases officielles à reprendre (questions numérotées du sujet) :
  - 1- أُثبتُ أنّ قيس مساحة هذه الضّيعة بالهكتار هو 4.
  - 2- أحسُبُ بالدّينار ثمن بيع كامل محصول البرتقال.
  - 3- أحسُبُ بالدّينار الدّخل الصّافي للفلّاح من هذه الصّابة.
- Étapes prévues :
  - q1 (« أُثبتُ أنّ قيس مساحة هذه الضّيعة بالهكتار هو 4 ») : triangle rectangle de côtés de l'angle droit 150 m et 200 m : 150 × 200 ÷ 2 = 15 000 m² ; trapèze rectangle de bases 75 m et 125 m et de hauteur 250 m : (75 + 125) ÷ 2 × 250 = 25 000 m² ; total 40 000 m² = 4 ha — QCM du côté à prendre pour hauteur (pas le 250 m du triangle), numériques, QCM de la conversion m² → ha — 4 q.
  - q2 (recette de la vente sur pied) : 40 000 ÷ 40 = 1000 arbres ; 1000 × 70 = 70 000 kg ; × 0,350 d = 24 500 d — numériques — 3 q.
  - q3 (revenu net) : main-d'œuvre 3600 d ; 20 % de 24 500 = 4900 d ; dépenses 8500 d ; net 16 000 d — numériques, QCM du pourcentage pris sur la recette — 3 q.
- Pièges (étiquette à porter par un distracteur) :
  - prendre le plus grand côté du triangle comme hauteur — ligne C14#3a (d3)
  - multiplier l'aire totale par la production d'une unité — ligne C14#3b (d2)
  - prendre le pourcentage d'un mauvais montant — ligne C14#3c (d2)
- Ne pas redemander : `20/02-boss#4`, `20/02-boss#8`, `20/04-defi#4`, `20/03-revision#8`, `20/04-defi#5`, `20/03-revision#5`, `20/03-revision#7`, `20/05-entrainement#6`, `20/05-entrainement#7`, `14/04-defi#7`, `14/04-defi#8`, `14/04-defi#9`, `14/04-defi#10`, `14/04-defi#11`
- Note : Piège de la q1 : prendre le plus grand côté du triangle (250 m) pour hauteur ; piège de la q3 : prendre le pourcentage d'un mauvais montant (de la superficie, du kg). Le prix 0,350 d par kg est gardé. Le `14/04-defi#7`–`#11` parcourt déjà « terrain, prix, frais » : la nouveauté est le triangle + trapèze à angles droits et la production par arbre.

### m033 → `exercices/09-exam-2012-p3-trapeze-au-1-sur-500-emprunt.json` · d3 boss 120/30 · 11 questions · régime **examen** · 🔁

- Titre de travail (à écrire en arabe : « 🏛️ مناظرة 2012 · المسألة 3 ⭐⭐⭐: … ») : Concours 2012 · problème 3 · le trapèze au 1/500, le prix, la part empruntée ⭐⭐⭐
- Registre : id `C15#3a` ; sources `C15#3a, C15#3b, C15#3c`
- Source : C15 (session 2012), problème 3 — transcription `2012-unique.md`
- Phrases officielles à reprendre (questions numérotées du sujet) :
  - 1- أحسب بالمتر الأبعاد الحقيقيّة لقطعة الأرض.
  - 2- أبحثُ عن ثمن شراء قطعة الأرض.
  - 3- أحسبُ النسبة المائويّة للمبلغ المقترَض من جملة تكاليف المشروع.
- Étapes prévues :
  - q1 (dimensions réelles) : sur le plan au 1/500, bases 8,4 cm et 13,6 cm, hauteur 6 cm ; réel : 42 m, 68 m et 30 m — QCM de la conversion cm → m (× 500 ÷ 100), numériques — 3 q.
  - q2 (prix d'achat) : aire = (42 + 68) ÷ 2 × 30 = 1650 m² = 16,5 ares ; × 2400 d = 39 600 d — numériques de l'aire, de la conversion en ares, du prix — 4 q.
  - q3 (part empruntée en pourcentage du coût total) : le prix du terrain vaut 2/7 du coût d'aménagement (donc l'aménagement vaut 7/2 du prix : fraction « dans l'autre sens »), 138 600 d ; coût du projet 39 600 + 138 600 = 178 200 d ; emprunt 22 275 d ; taux = 22 275 ÷ 178 200 = 12,5 % — QCM du sens de la fraction, numériques — 4 q.
- Pièges (étiquette à porter par un distracteur) :
  - diviser par l'échelle au lieu de multiplier — ligne C15#3a (d2)
  - multiplier un prix à l'are par une aire en mètres carrés — ligne C15#3b (d3)
  - appliquer la fraction dans le mauvais sens entre deux coûts — ligne C15#3c (d4)
- Ne pas redemander : `14/01-pratique#7`, `14/02-boss#7`, `14/03-revision#10`, `20/02-boss#4`, `20/02-boss#8`, `20/04-defi#4`, `20/01-pratique#7`, `20/04-defi#7`, `14/04-defi#7`, `14/04-defi#9`, `14/05-entrainement#7`
- Note : Pièges : appliquer la fraction dans le mauvais sens entre les deux coûts (terrain = 2/7 de l'aménagement ≠ aménagement = 2/7 du terrain) ; multiplier un prix à l'are par une aire en m². Le côté oblique n'est pas donné et n'est pas demandé. Résultat final rond (12,5 %).


## Chapitre `25-perimetre-figure-composee` 🔁 (B5)

### m034 → `exercices/06-exam-2026-p3-jardin-ecologique-losanges.json` · d3 boss 120/30 · 10 questions · régime **examen** · 🔁

- Titre de travail (à écrire en arabe : « 🏛️ مناظرة 2026 · المسألة 3 ⭐⭐⭐: … ») : Concours 2026 · problème 3 · le jardin écologique : aires par différence, base, périmètre ⭐⭐⭐
- Registre : id `C01#3a` ; sources `C01#3a, C01#3b, C01#3c`
- Source : C01 (session 2026), problème 3 — transcription `2026-unique.md`
- Phrases officielles à reprendre (questions numérotées du sujet) :
  - 1) أثبتُ أنّ قيس مساحة المثلّث أ ب ج تساوي 12 صم².
  - 2) أحسبُ بالصّم أ ب علما أنّ أ م = 1,4 صم.
  - 3) أحسبُ بالصّم قيس طول محيط الرّباعيّ ب ج د ن علما أنّه يفوق قيس طول محيط الرّباعيّ د ن و ج بـ 6 صم.
- Étapes prévues :
  - q1 (« أثبتُ أنّ قيس مساحة المثلّث أ ب ج تساوي 12 صم² ») : le grand losange ب ج د ن (quatre côtés égaux) se coupe en deux triangles égaux par [ج ن] : aire = 2 × 30,72 = 61,44 cm² ; il surpasse le quadrilatère ب ج و ن (37,44 cm²) de 24 cm² ; ces 24 cm² forment la partie gauche د ج و ن, que [د و] coupe en deux triangles égaux (base د و, même hauteur [ج م]) ; chacun est égal au triangle أ ب ج (د و = أ ب, même hauteur) : 12 cm² — QCM de la partie à isoler, numériques de l'aire du grand losange, de la différence, du triangle — 4 q.
  - q2 (« أحسبُ بالصّم أ ب علما أنّ أ م = 1,4 صم ») : أ ب × ج م ÷ 2 = 12, donc أ ب × ج م = 24 ; l'aire du triangle ن ج د = د م × ج م = (أ ب + أ م) × ج م = 24 + 1,4 × ج م = 30,72 ; ج م = 6,72 ÷ 1,4 = 4,8 cm ; أ ب = 24 ÷ 4,8 = 5 cm — QCM de l'écriture de د م, numériques de ج م et de أ ب — 3 q.
  - q3 (périmètre de ب ج د ن sachant qu'il surpasse de 6 cm celui de د ن و ج) : P(ب ج د ن) − P(د ن و ج) = 2 × (côté du losange − ج و) = 6 cm ; la figure ne donne ni le côté ni ج و : voir la note — 3 q si la donnée manquante est admise.
- Pièges (étiquette à porter par un distracteur) :
  - ajouter les aires au lieu de les retrancher — ligne C01#3a (d4)
  - confondre la moitié du segment avec le segment entier — ligne C01#3b (d3)
  - reprendre l'écart comme le périmètre lui-même — ligne C01#3c (d3)
- Ne pas redemander : `20/02-boss#7`, `20/quiz#7`, `20/04-defi#10`, `20/02-boss#10`, `19/04-defi#3`, `19/05-entrainement#5`, `19/04-defi#1`, `25/quiz#1`, `25/02-boss#1`
- Note : À VÉRIFIER AVANT D'ÉCRIRE (re-résolution du planificateur le 2026-10-19). Q1 et q2 se résolvent sans Pythagore (grand losange = 2 × 30,72, différence d'aires, ج م = 4,8, أ ب = 5). Q3 : le périmètre de ب ج د ن (quatre côtés égaux) exige la longueur du côté ; elle se déduit de ج و = 5 (triangle ج م أ, côtés 4,8 et 1,4) puis côté = ج و + 3 = 8, c'est-à-dire de Pythagore, HORS programme : DÉCISION E-4 (donner « ج و = 5 صم » dans l'énoncé, ou écarter la q3 et déplacer la mission au `20`). Figure complexe, sans aucune cote : l'auteur la refait en SVG et vérifie que les données se recoupent (symétrie, marques d'égalité). Placement au `25` (ligne C01#3c reclassée par le lecteur).

### m035 → `exercices/07-exam-2021-p3-jardin-public-trapeze-demi-disque.json` · d3 boss 120/30 · 12 questions · régime **examen** · 🔁

- Titre de travail (à écrire en arabe : « 🏛️ مناظرة 2021 · المسألة 3 ⭐⭐⭐: … ») : Concours 2021 · problème 3 · le jardin public : aires en ares, parcours du coureur ⭐⭐⭐
- Registre : id `C06#3a` ; sources `C06#3a, C06#3b, C06#3c`
- Source : C06 (session 2021), problème 3 — transcription `2021-unique.md`
- Phrases officielles à reprendre (questions numérotées du sujet) :
  - 1- أثبتُ أنّ مساحة أ ب ج هـ تساوي 3140 آر.
  - 2- أثبتُ أنّ قيس طول [ب و] يساوي 29 م.
  - 3- في أيّ نقطة من المسلك الصّحّي يوجد العدّاء بعد قطعه 5611 م ؟ أعلّل إجابتي.
- Étapes prévues :
  - q1 (« أثبتُ أنّ مساحة أ ب ج هـ تساوي 3140 آر ») : aire totale 5600,19 a = ABCE + ECD (1478,94 a) + demi-disque ; ABCE = 8/5 du disque et le demi-disque = 1/2 du disque : 8/5 + 1/2 = 21/10 du disque ; 5600,19 − 1478,94 = 4121,25 a = 21/10 du disque ; disque = 1962,5 a ; ABCE = 8/5 × 1962,5 = 3140 a — QCM de la décomposition, numériques — 4 q.
  - q2 (« أثبتُ أنّ قيس طول [ب و] يساوي 29 م ») : 3140 a = 314 000 m² ; ABCE est un parallélogramme de côtés parallèles [AB] et [EC] et de hauteur DC = 628 m (angle droit en D) : base AE = 314 000 ÷ 628 = 500 m = BC ; triangle ECD rectangle en D : ED = 2 × 147 894 ÷ 628 = 471 m = OC (rectangle OCDE) ; BO = BC − OC = 500 − 471 = 29 m — QCM de la conversion a → m², numériques de BC, de ED, de BO — 4 q.
  - q3 (position du coureur après 5611 m) : les diagonales du rectangle OCDE sont égales à EC = AB = 785 m (côtés opposés du parallélogramme) donc OZ = ZC = 392,5 m ; chemin B → O → Z → C = 29 + 392,5 + 392,5 = 814 m ; demi-circonférence de diamètre BC = 3,14 × 500 ÷ 2 = 785 m ; un tour = 1599 m ; 5611 = 3 × 1599 + 814 : le coureur est en C — QCM du contour du tour (le côté [BC] n'en fait pas partie), numériques de la longueur d'un tour, du reste, QCM de la position — 4 q.
- Pièges (étiquette à porter par un distracteur) :
  - oublier que le demi-disque vaut la moitié du disque — ligne C06#3a (d4)
  - oublier de convertir les ares en mètres carrés — ligne C06#3b (d4)
  - ignorer les tours complets ou le sens du parcours — ligne C06#3c (d4)
- Ne pas redemander : `21/02-boss#8`, `21/05-entrainement#8`, `21/05-entrainement#7`, `21/04-defi#8`, `21/04-defi#7`, `20/02-boss#4`, `20/04-defi#9`, `20/03-revision#7`, `20/04-defi#7`, `20/03-revision#5`, `02/02-boss#4`, `02/02-boss#7`, `02/05-entrainement#7`, `25/quiz#3`, `25/quiz#5`, `25/02-boss#3`, `25/02-boss#6`, `25/04-defi#5`, `25/05-entrainement#6`
- Note : Mission la plus lourde du lot (d3, 12 q, trois ensembles de données, nombres à cinq chiffres). Re-résolue par le planificateur à partir de la transcription : ABCE est un parallélogramme (ses côtés [AB] et [EC] sont parallèles, ses côtés [AE] et [BC] sont portés par les deux bases du trapèze), (785 ; 628 ; 471) sont des multiples de (5 ; 4 ; 3) mais on obtient 471 par l'AIRE, jamais par Pythagore. Le tour de piste tombe exactement sur C (reste = 814). L'auteur relit la figure du PDF officiel avant d'écrire. Pièges : ignorer les tours complets ou le sens du parcours (B → O → Z → C puis demi-cercle) ; compter [BC] dans le tour ; oublier de convertir les ares en m².

### m036 → `exercices/08-exam-2019-p3-deux-terrains-pret-et-cloture.json` · d3 boss 120/30 · 12 questions · régime **examen** · 🔁

- Titre de travail (à écrire en arabe : « 🏛️ مناظرة 2019 · المسألة 3 ⭐⭐⭐: … ») : Concours 2019 · problème 3 · deux terrains voisins : l'aire, le prêt, la clôture ⭐⭐⭐
- Registre : id `C08#3a` ; sources `C08#3a, C08#3b, C08#3c`
- Source : C08 (session 2019), problème 3 — transcription `2019-unique.md`
- Phrases officielles à reprendre (questions numérotées du sujet) :
  - 1. أحسبُ مساحة القطعة الأولى (مع التّعليل).
  - 2. أحسبُ بالدّينار قيمة القرض.
  - 3. أحسبُ بالمتر قيس طول السّياج.
- Étapes prévues :
  - q1 (aire de la première pièce) : aire totale 47,355 a = 4735,5 m² ; AD = BC = 82 m (côtés opposés du parallélogramme) ; AD = DM (triangle isocèle) donc DM = 82 m ; aire du triangle = 82 × 33 ÷ 2 = 1353 m² — QCM de la base à prendre, numériques — 4 q.
  - q2 (valeur du prêt) : vente de la première pièce = 1353 × 75 = 101 475 d ; elle couvre les 3/10 du montant nécessaire ; montant = 101 475 ÷ 3 × 10 = 338 250 d ; prêt = 7/10 de 338 250 = 236 775 d — QCM de la fraction couverte par la vente (3/10), numériques — 4 q.
  - q3 (longueur de la clôture, entrée de 6 m) : aire du parallélogramme = 4735,5 − 1353 = 3382,5 m² ; base CD = 3382,5 ÷ 33 = 102,5 m ; périmètre = 2 × (102,5 + 82) = 369 m ; clôture = 369 − 6 = 363 m — numériques, QCM de l'entrée à retrancher — 4 q.
- Pièges (étiquette à porter par un distracteur) :
  - prendre le côté pour la hauteur ou oublier la moitié — ligne C08#3a (d3)
  - prendre la recette de vente pour le montant du prêt — ligne C08#3b (d4)
  - ne pas retrancher la largeur de l'entrée — ligne C08#3c (d4)
- Ne pas redemander : `20/02-boss#3`, `20/03-revision#6`, `20/05-entrainement#10`, `20/03-revision#7`, `19/05-entrainement#4`, `19/05-entrainement#5`, `14/04-defi#7`, `14/04-defi#9`, `13/04-defi#7`, `13/02-boss#9`, `25/01-pratique#1`, `25/01-pratique#2`, `25/03-revision#4`, `25/05-entrainement#1`
- Note : Problème sain et aux nombres propres (re-résolu par le planificateur). Pièges : prendre la recette de la vente pour le montant du prêt ; ne pas retrancher la largeur de l'entrée. La clôture ne longe que le parallélogramme (seconde pièce) : le contour est un périmètre simple avec ouverture ; le lecteur l'a reclassé `25` (C08#3c). Hauteur AE = 33 m lue sur la figure (marquée perpendiculaire à CM). Placement au `25` à titre d'exception déclarée (l'étape neuve est le contour avec ouverture).

### m037 → `exercices/09-exam-2016-p3-losange-et-demi-disque-mur.json` · d3 boss 120/30 · 11 questions · régime **examen** · 🔁

- Titre de travail (à écrire en arabe : « 🏛️ مناظرة 2016 · المسألة 3 ⭐⭐⭐: … ») : Concours 2016 · problème 3 · le losange et le demi-disque : côté, mur avec entrée, plan ⭐⭐⭐
- Registre : id `C11#3a` ; sources `C11#3a, C11#3b, C11#3c`
- Source : C11 (session 2016), problème 3 — transcription `2016-unique.md`
- Phrases officielles à reprendre (questions numérotées du sujet) :
  - 1. أحسُبُ قيس ضلع القطعة المعيّنة أ ب ج د .
  - 2. أحسُبُ بالمتر قيس طول الجدار.
  - 3. أرسُمُ تصميما للجزء أ ب ج د وفق السّلّم 1/1000 .
- Étapes prévues :
  - q1 (côté du losange) : grande diagonale 80 m ; petite = 3/4 de 80 = 60 m ; aire = 80 × 60 ÷ 2 = 2400 m² ; aire = côté × hauteur donc côté = 2400 ÷ 48 = 50 m — numériques de la petite diagonale, de l'aire, du côté — 4 q.
  - q2 (longueur du mur, entrée de 4,5 m) : le terrain réuni = losange + demi-disque de diamètre [ب ج] : le côté [ب ج] devient intérieur et ne fait plus partie du contour ; mur = 3 côtés du losange (150 m) + demi-cercle (3,14 × 50 ÷ 2 = 78,5 m) − entrée 4,5 = 224 m — QCM des côtés conservés, numériques — 4 q.
  - q3 (plan au 1/1000 du losange) : diagonales 80 m → 8 cm, 60 m → 6 cm ; ordering des étapes (diagonale horizontale, médiatrice, report de 3 cm de part et d'autre, les quatre côtés) — 3 q.
- Pièges (étiquette à porter par un distracteur) :
  - confondre hauteur et demi-diagonale dans le calcul de l'aire — ligne C11#3a (d3)
  - compter le côté commun ou oublier de retrancher l'ouverture — ligne C11#3b (d3)
  - convertir les longueurs sans tenir compte de l'unité du plan — ligne C11#3c (d2)
- Ne pas redemander : `20/02-boss#7`, `20/quiz#7`, `20/04-defi#10`, `19/01-pratique#8`, `19/04-defi#4`, `21/02-boss#8`, `21/02-boss#10`, `21/quiz#7`, `16/02-boss#7`, `19/05-entrainement#3`, `18/02-boss#8`, `17/02-boss#7`, `25/quiz#4`, `25/01-pratique#4`, `25/02-boss#4`, `25/03-revision#6`, `25/04-defi#4`
- Note : Pièges : compter le côté commun [ب ج] dans le contour ; ne pas retrancher l'entrée ; confondre la hauteur et la demi-diagonale dans l'aire du losange. La hauteur 48 m est issue de ب sur [أ د]. π = 3,14. La q3 est un plan : on ne note que les longueurs et l'ordre des étapes. Mission-modèle pour le patron du `25` (contour fermé, côté commun qui disparaît).

### m038 → `exercices/10-devoir-perimetre-reel-d-une-figure-composee-sur-plan.json` · d3 boss 120/30 · 7 questions · régime **devoir (salle blanche)** · 🔁

- Titre de travail (arabe : « ⭐ تمرين موجّه / ⚔️ زعيم الفرض ⭐⭐⭐: … ») : Périmètre réel d'une figure composée lue sur un plan à l'échelle ⭐⭐⭐
- Registre : id `D04#1` ; sources `D04#1, D05#4, D08#5`
- Cartes : devoir D (T2, école primaire), exercice(s) 1 ; devoir E (T2, école primaire), exercice(s) 4 ; devoir G (T3, école primaire), exercice(s) 5 — cartes anonymes
- Gestes lus (archétype des lecteurs, sans nombre) :
  - D04#1 (d4) : calculer le périmètre réel d’une figure à demi-cercles et segments depuis un plan
  - D05#4 (d3) : calculer le périmètre d’une figure formée d’un triangle, d’un rectangle et d’un cercle
  - D08#5 (d3) : calculer le périmètre sur plan d’une figure formée d’un trapèze et d’un demi-cercle
- Étapes prévues :
  - Un plan à l'échelle donnée ; une figure formée de segments et de demi-cercles (ou d'un triangle, d'un rectangle et d'un cercle) : lire les longueurs du plan, convertir en longueurs réelles — QCM, numériques — 2 q.
  - Longueur de chaque demi-cercle (diamètre réel × π ÷ 2) ; longueurs qui disparaissent du contour (le diamètre commun, le côté commun de deux pièces accolées) — QCM du contour extérieur, numériques — 3 q.
  - Somme du contour, retour à l'unité demandée (hectomètres ou mètres) — numérique, QCM d'unité — 2 q.
- Pièges (étiquette à porter par un distracteur) :
  - compter le diamètre commun dans le contour — ligne D04#1 (d4)
  - compter un côté commun dans le contour — ligne D05#4 (d3)
  - compter le diamètre du demi-cercle dans le contour — ligne D08#5 (d3)
- Ne pas redemander : `21/02-boss#8`, `21/05-entrainement#8`, `21/04-defi#9`, `21/quiz#7`, `19/04-defi#1`, `19/04-defi#2`, `19/05-entrainement#4`, `18/04-defi#1`, `18/04-defi#3`, `25/01-pratique#6`, `25/03-revision#4`, `25/04-defi#2`, `25/05-entrainement#1`, `25/05-entrainement#4`
- Note : Salle blanche. Geste neuf : le périmètre RÉEL d'une figure composée à partir d'un plan (échelle + demi-cercles + côté commun qui n'est pas dans le contour). Piège : compter le diamètre commun dans le contour. Les missions d'examen du chapitre portent le contour fermé et l'entrée ; celle-ci porte l'échelle.

