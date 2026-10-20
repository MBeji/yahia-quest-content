# Carte d'affectation M3 — maths 6ᵉ, chapitres `21`, `22` (missions du gisement)

> Lot auteur du passage unique (PLAN-gisement.md § 4). 9 missions, 80 questions. Skills : `content-ecole-tn`, puis `prof-math-6eme` (calibre les étages, jamais plus que le programme) ; consignes `content-ingest/references/gisement-auteur-examen.md` (missions 🏛️ : la transcription de la session citée, `content/programmes-officiels/examens-nationaux/6eme-base/math/<année>-unique.md`) et `gisement-auteur-devoir.md` (missions 📝 : la carte seule, jamais le devoir). Écris en arabe (`contentLanguage` du sujet). Ne touche à aucun autre chapitre que les tiens ; les autres lots écrivent en parallèle. Nom de fichier : `exercices/<fichier>` ci-dessous.

**Règles communes** (PLAN-gisement.md § 1) : une mission d'examen reprend UN problème entier d'une session, découpé en étapes notées ; chaque question dit sa session (« مناظرة 2023 ») et redonne les données et la phrase OFFICIELLES de la transcription qu'elle lit (valeurs, unités, décimaux à trois chiffres tels qu'imprimés, tableau refait lisible) ; un « أثبتُ أنّ… » devient « quelle valeur / quelle justification » (jamais la clé dans le titre ni dans l'énoncé) ; types natifs : `numeric` pour les valeurs, QCM pour le choix d'étape, la justification et la décision, `ordering` pour un raisonnement ou les étapes d'une construction ; une CONSTRUCTION n'est pas notable : on note les longueurs du plan (échelle) et l'ordre des étapes ; figures refaites en SVG, vraies, sans donner la clé ; π = 3,14 ; aucune algèbre littérale, ni Pythagore, ni somme des angles d'un triangle, ni calcul d'intérêt, ni partage « somme et écart / somme et rapport » (◐) ; jamais de corrigé de site tiers : l'explication est la tienne, re-résolue par deux chemins ; au plus 12 questions ; étage d3 = `boss` 120/30, d2 = `practice` 75/15. Étiquettes : `misconceptionTag` du registre `math.*` sur le distracteur qui EXÉCUTE l'erreur du « piège » de la ligne, jamais sur un multi, un ordering ni un matching ; un id qui manque se signale (on ne touche ni `content/misconceptions.json` ni `content/competences/`). `chapter.json` : ajoute à `sources[]` — missions d'examen : « Sujets officiels du concours d'entrée aux collèges pilotes (6ᵉ année de base), Ministère de l'Éducation (corpus officiel, reprise citée, étude 36) — transcriptions : programmes-officiels/examens-nationaux/6eme-base/math/ » ; missions de devoir : « Calibré sur des devoirs publics (étude 36, T2′, aucune reprise) — carte : programmes-officiels/sources-externes/web-6eme-base-math/fiche.md ». Numéros de fichiers : à la suite de `05-entrainement` (06, 07, …), `displayOrder` à la suite ; les missions de chaque chapitre dans l'ordre de la carte. Gates à chaque chapitre : `content:check`, `content:qa -- --subject math-6eme` (0 erreur), `content:tranche -- --subject math-6eme --changed --fresh --strict-longest`.

**Étiquettes déjà en usage dans tes chapitres** : `21` : `math.geo.rayon-et-diametre-confondus` (Tu confonds rayon et diamètre : le diamètre passe par le cen); `math.geo.facteur-pi-omis` (Tu as oublié de multiplier par π : sans lui, tu ne calcules ); `math.geo.formules-cercle-perimetre-et-aire-confondues` (Tu confonds les deux formules : le périmètre vaut 2 × π × r,); `math.geo.perimetre-cercle-facteur-deux-omis-ou-en-trop` (Le 2 va avec le RAYON, pas avec le diamètre : périmètre = 2 ); `math.geo.valeur-de-pi-erronee` (La valeur approchée retenue est π ≈ 3,14 — ni 3, ni 3,41); `math.geo.cercle-et-disque-confondus` (Le cercle est la ligne courbe — il a un périmètre ; le disqu) | `22` : `math.mes.duree-convertie-en-base-cent` (Le temps ne se convertit ni par 10 ni par 100 : la minute va); `math.mes.constante-de-temps-attribuee-a-la-mauvaise-unite` (Chaque unité de temps a SA constante : 60 pour la minute et ); `math.mes.duree-retenue-de-soixante-non-faite` (Une durée ne garde jamais 60 minutes ou plus : 3 h 75 min s'); `math.num.soustraction-colonne-petit-du-grand` (Dans chaque colonne tu retranches le petit chiffre du grand ); `math.num.operation-inverse-appliquee` (Tu fais l'opération contraire de celle demandée : une additi).

## ⚠️ Chapitres encore en écriture (lot B5) — à revérifier au lancement

État relevé par le planificateur le **2026-10-19 23:37 UTC** (`b5-etat-au-plan.json` : empreintes par fichier). B5 travaille dans l'ordre 20 → 21 → 23 → 25 (`auteurs-notes/B5/NOTES.md`). À ce relevé : `20-aires-polygones` mis à niveau (cours, quiz 7 q, exercices +3/+4 questions, rien d'autre à attendre) ; `21-cercle-disque` en cours (exercices 01–05 réécrits à 23 h 36 : les indices de « ne pas redemander » ci-dessous sont vérifiés contre cet état, mais B5 peut y revenir) ; `23-solides-cube-pave` mis à niveau (exercices modifiés à 21 h 25 ; aucune mission du gisement n'y va : aucun solide dans les 17 sujets ni les 9 devoirs) ; `25-perimetre-figure-composee` **est apparu pendant le plan** (relevé à 21 h 35 : quiz à 5 q, exercices `01`–`05` de 6 q chacun, cours et résumé ; B5 peut encore le retoucher) : les listes « ne pas redemander » des missions du `25` en tiennent compte (contour extérieur, côté commun, demi-cercles, échelle, plantations sur contour fermé), les missions partent de `06`.

**Au lancement de ce lot** : (1) relire le rapport B5 et refaire l'inventaire des chapitres 20, 21 et 25 (`NN/fichier#n`) ; (2) comparer aux empreintes ; (3) rouvrir chaque liste « Ne pas redemander » concernée (indices décalés, questions ajoutées ou retirées) et, pour le `25`, relire ses exercices 01–05 (leçon 24 : contour extérieur, côté commun qui disparaît, arc retranché, contour fermé, échelle, arrondi par excès) ; (4) vérifier le plus grand `NN` existant de chaque chapitre : si B5 a ajouté un fichier 06+, décaler la plage. Les listes ci-dessous sont valables pour l'état relevé, pas pour un état ultérieur ; les missions concernées sont marquées 🔁.


## Chapitre `21-cercle-disque` 🔁 (B5)

### m019 → `exercices/06-exam-2023-p2-cerf-volant-fil-demi-cercles.json` · d3 boss 120/30 · 7 questions · régime **examen** · 🔁

- Titre de travail (à écrire en arabe : « 🏛️ مناظرة 2023 · المسألة 2 ⭐⭐⭐: … ») : Concours 2023 · problème 2 · le cerf-volant et sa queue de demi-cercles ⭐⭐⭐
- Registre : id `C04#2a` ; sources `C04#2a, C04#2b`
- Source : C04 (session 2023), problème 2 — transcription `2023-unique.md`
- Phrases officielles à reprendre (questions numérotées du sujet) :
  - 1) أثبتُ أنّ قيس طول القطر [ج هـ] يساوي 0,5 م، علما أنّ كلفة المتر الواحد من السّلك المعدنيّ تساوي 20 د.
  - 2) أحسبُ بالدّينار كلفة المتر المربّع الواحد من الرّخام المستعمل.
- Étapes prévues :
  - q1 (« أثبتُ أنّ قيس طول القطر [ج هـ] يساوي 0,5 م ») : le fil mesure 47,100 ÷ 20 = 2,355 m ; trois demi-cercles égaux ; un demi-cercle = 2,355 ÷ 3 = 0,785 m ; sa circonférence entière 1,57 m ; diamètre = 1,57 ÷ 3,14 = 0,5 m — QCM de ce que représente 3 demi-cercles, numériques — 4 q.
  - q2 (coût du m² de marbre) : les deux diagonales du cerf-volant [ب د] et [أ ج] sont perpendiculaires ; ب د = 2 × 0,5 = 1 m (و ب = و د = ج هـ) ; aire = 1,5 × 1 ÷ 2 = 0,75 m² ; 75 ÷ 0,75 = 100 d le m² — QCM de la longueur de la diagonale, numériques — 3 q.
- Pièges (étiquette à porter par un distracteur) :
  - prendre la circonférence entière au lieu du demi-cercle — ligne C04#2a (d4)
  - oublier de diviser le produit des diagonales par deux — ligne C04#2b (d3)
- Ne pas redemander : `21/02-boss#2`, `21/02-boss#3`, `21/01-pratique#8`, `21/02-boss#8`, `21/02-boss#10`, `21/04-defi#7`, `20/quiz#7`, `20/02-boss#7`, `20/04-defi#10`, `05/05-entrainement#6`
- Note : Pièges : prendre la circonférence entière au lieu du demi-cercle ; oublier de diviser le produit des diagonales par deux. La figure (cerf-volant, queue en demi-cercles alternés) est refaite en SVG. π = 3,14. État du `21` relevé le 2026-10-19 à 21 h 25 : le lot B5 y écrit encore (voir la carte M3).

### m020 → `exercices/07-exam-2022-p3-parc-carre-parallelogramme-secteur.json` · d3 boss 120/30 · 12 questions · régime **examen** · 🔁

- Titre de travail (à écrire en arabe : « 🏛️ مناظرة 2022 · المسألة 3 ⭐⭐⭐: … ») : Concours 2022 · problème 3 · le parc en trois pièces ⭐⭐⭐
- Registre : id `C05#3a` ; sources `C05#3a, C05#3b, C05#3c`
- Source : C05 (session 2022), problème 3 — transcription `2022-unique.md`
- Phrases officielles à reprendre (questions numérotées du sujet) :
  - 1/ أثبتُ أنّ أ و = 60 م علمًا أنّ قيس طول قوس الدّائرة من القطعة ③ الرّابط بين النّقطتين "أ" و "ج" يُساوي بالمتر 282,6.
  - 2/ أبحث عن قيس مساحة القطعة ② بالمتر المربّع، علمًا أنّه يفوق 1/3 مساحة القطعة ③ بـ 1374 م².
  - 3/ أرسم تصميما للقطعة ② وفقا للسّلّم 1/2000 إذا علمت أنّ أ ب م (angle, le chapeau est sur ب) = 60° وأنّ قيس الارتفاع الموافق للقطعة [أ ب] يُساوي 70 م.
- Étapes prévues :
  - q1 (« أثبتُ أنّ أ و = 60 م ») : l'arc de trois quarts de cercle mesure 282,6 m ; la circonférence entière 282,6 ÷ 3 × 4 = 376,8 m ; diamètre 376,8 ÷ 3,14 = 120 ; rayon = 60 m = côté du carré — QCM de la fraction de la circonférence, numériques — 4 q.
  - q2 (aire du parallélogramme) : aire du disque entier = 3,14 × 60² = 11 304 m² ; trois quarts = 8478 m² ; un tiers = 2826 ; parallélogramme = 2826 + 1374 = 4200 m² — numériques, QCM du « surpasse le tiers de » — 5 q.
  - q3 (construction du parallélogramme au 1/2000) : côté [أ ب] = 60 m → 3 cm ; hauteur 70 m → 3,5 cm ; angle de 60° en ب ; la construction elle-même n'est pas notable : QCM des longueurs sur le plan, ordering des étapes (tracer [أ ب], l'angle, parallèle, hauteur) — 3 q.
- Pièges (étiquette à porter par un distracteur) :
  - utiliser la circonférence entière pour l'arc — ligne C05#3a (d3)
  - appliquer la fraction à l'aire du disque entier — ligne C05#3b (d4)
  - oublier de convertir les mètres en centimètres de dessin — ligne C05#3c (d4)
- Ne pas redemander : `21/01-pratique#8`, `21/02-boss#7`, `21/02-boss#10`, `21/04-defi#7`, `21/05-entrainement#8`, `21/04-defi#3`, `20/01-pratique#5`, `20/03-revision#6`, `20/05-entrainement#10`, `14/01-pratique#7`, `17/02-boss#7`, `19/05-entrainement#3`
- Note : 14 étapes brutes ramenées à 12 questions (la q3 est réduite à 3 questions d'échelle et d'ordre). Pièges : appliquer la fraction à l'aire du disque entier ; oublier de convertir les mètres en centimètres de dessin. Le carré de côté 60 m n'a pas de question propre. π = 3,14. `21` en cours d'écriture (B5) : voir la carte M3.

### m021 → `exercices/08-exam-2008-p2-fontaine-losange-dans-le-disque.json` · d3 boss 120/30 · 7 questions · régime **examen** · 🔁

- Titre de travail (à écrire en arabe : « 🏛️ مناظرة 2008 · المسألة 2 ⭐⭐⭐: … ») : Concours 2008 · problème 2 · la fontaine : losange inscrit dans un disque ⭐⭐⭐
- Registre : id `C19#2a` ; sources `C19#2a, C19#2b`
- Source : C19 (session 2008), problème 2 — transcription `2008-unique.md`
- Phrases officielles à reprendre (questions numérotées du sujet) :
  - ① ما قيس المساحة الحقيقيّة للمُعيّن بالم² ؟
  - ② ما قيس المساحة الحقيقيّة للفضاء المعشّب بالم² ؟
- Étapes prévues :
  - q1 (aire réelle du losange en m²) : plan au 1/150 ; diagonale horizontale 6 cm → 900 cm = 9 m ; diagonale verticale 4 cm → 600 cm = 6 m ; aire = 9 × 6 ÷ 2 = 27 m² — QCM des deux conversions, numérique de l'aire — 3 q.
  - q2 (aire du gazon) : le diamètre du disque est la diagonale horizontale (9 m) donc le rayon 4,5 m ; aire du disque = 3,14 × 4,5² = 63,585 m² ; gazon = 63,585 − 27 = 36,585 m² — QCM du lien diamètre–diagonale, numériques — 4 q.
- Pièges (étiquette à porter par un distracteur) :
  - appliquer l'échelle à l'aire au lieu de la convertir en longueurs — ligne C19#2a (d3)
  - prendre le diamètre pour le rayon — ligne C19#2b (d3)
- Ne pas redemander : `14/01-pratique#7`, `14/02-boss#7`, `14/05-entrainement#7`, `15/04-defi#9`, `20/02-boss#7`, `20/quiz#7`, `21/02-boss#4`, `21/02-boss#9`, `21/05-entrainement#7`
- Note : Piège : appliquer l'échelle à l'aire (l'échelle s'applique aux longueurs ; l'aire du plan n'est jamais convertie directement). Piège 2 : prendre le diamètre pour le rayon. Le problème 2008 est presque identique à celui d'autres sessions (losange et cercle) : l'angle neuf est l'échelle appliquée aux deux diagonales avant l'aire.


## Chapitre `22-durees`

### m022 → `exercices/06-exam-2025-p3-bus-quatre-tours.json` · d3 boss 120/30 · 12 questions · régime **examen**

- Titre de travail (à écrire en arabe : « 🏛️ مناظرة 2025 · المسألة 3 ⭐⭐⭐: … ») : Concours 2025 · problème 3 · les tours d'une ligne de bus ⭐⭐⭐
- Registre : id `C02#3a` ; sources `C02#3a, C02#3b, C02#3c`
- Source : C02 (session 2025), problème 3 — transcription `2025-unique.md`
- Phrases officielles à reprendre (questions numérotées du sujet) :
  - 1) أثبتُ أنّ الحافلة تصل إلى المحطّة "أ" في نهاية السّفرة الأولى بعد 40 دق من انطلاقها.
  - 2) أحدّدُ ساعة وصول الحافلة إلى المحطّة "أ" في نهاية السّفرة الرّابعة إذا انطلقت في السّفرة الأولى من المحطّة "أ" على السّاعة 6 صباحا.
  - 3) أحسبُ معدّل سرعة الحافلة بين المحطّتين "ج" و "أ" أثناء الاكتظاظ.
- Étapes prévues :
  - q1 (« أثبتُ أنّ الحافلة تصل ... بعد 40 دق ») : le tronçon ج → أ fait 8 km à 48 km/h = 10 min ; durée de roulage 8 + 12 + 10 = 30 min ; deux arrêts de 5 min (en ب et en ج) ; 30 + 10 = 40 min — QCM des durées à compter, numériques — 4 q.
  - q2 (heure d'arrivée à la fin du 4ᵉ tour, départ à 6 h) : quatre tours de 40 min et trois arrêts de 5 min en أ entre les tours ; 160 + 15 = 175 min = 2 h 55 ; 6 h + 2 h 55 = 8 h 55 — QCM du nombre d'arrêts, numériques — 3 q.
  - q3 (vitesse de ج à أ pendant l'embouteillage, arrivée à 9 h 05) : retard de 10 min sur 8 h 55 ; ج → أ dure 10 + 10 = 20 min = 1/3 h ; 8 ÷ 1/3 = 24 km/h — numériques, QCM du retard à ajouter à la durée du tronçon — 5 q.
- Pièges (étiquette à porter par un distracteur) :
  - compter un arrêt de trop ou de moins — ligne C02#3a (d3)
  - oublier l'arrêt entre deux tours — ligne C02#3b (d3)
  - ne pas déduire les arrêts ni convertir minutes et heures — ligne C02#3c (d4)
- Ne pas redemander : `22/02-boss#10`, `22/04-defi#4`, `22/04-defi#9`, `22/05-entrainement#6`, `22/05-entrainement#10`, `22/04-defi#8`, `15/02-boss#4`, `15/03-revision#4`, `15/04-defi#6`, `15/05-entrainement#7`, `15/02-boss#9`
- Note : Pièges : compter un arrêt de trop ou de moins (le dernier arrêt en أ n'existe pas, mais il y en a trois entre les quatre tours) ; ne pas convertir 10 min en 1/6 h ; oublier de déduire les arrêts du temps de roulage. Le secteur de disque de la figure est refait en SVG sans donnée supplémentaire (aucune cote).

### m023 → `exercices/07-exam-2022-p2-piscine-deux-pompes.json` · d3 boss 120/30 · 10 questions · régime **examen**

- Titre de travail (à écrire en arabe : « 🏛️ مناظرة 2022 · المسألة 2 ⭐⭐⭐: … ») : Concours 2022 · problème 2 · remplir une piscine avec deux pompes ⭐⭐⭐
- Registre : id `C05#2a` ; sources `C05#2a, C05#2b`
- Source : C05 (session 2022), problème 2 — transcription `2022-unique.md`
- Phrases officielles à reprendre (questions numérotées du sujet) :
  - 1/ أحسب بالهكتولتر كمّية الماء الّتي تضخّها المضخّة الأولى في السّاعة الواحدة علمًا أنّ كلّ مضخّة قد ساهمت في ملء نصف سعة المسبح.
  - 2/ لو أراد العامل أن يكمل عمليّة ملء المسبح قبل ساعة فكم من الوقت سيقدّم تشغيل المضخّة الثّانية ؟
- Étapes prévues :
  - q1 (débit de la première pompe en hl/h) : la piscine contient 1280 hl ; chaque pompe apporte la moitié : 640 hl ; la première a travaillé 2 h 40 + 8 h = 10 h 40 min = 10 2/3 h ; 640 ÷ 10 2/3 = 60 hl/h (la seconde : 640 ÷ 8 = 80 hl/h, ensemble 140) — QCM de la durée de la première pompe, numériques de la quantité par pompe, du débit — 4 q.
  - q2 (de combien avancer la mise en route de la seconde pompe pour finir une heure plus tôt) : durée visée 9 h 40 = 9 2/3 h ; la première pompe seule pendant 9 2/3 h donne 580 hl ; il reste 700 hl pour la seconde, soit 700 ÷ 80 = 8 h 45 min ; elle démarre donc 55 min après la première, au lieu de 2 h 40 min : 1 h 45 min plus tôt — QCM de la durée visée, numériques, QCM du « de combien plus tôt » — 6 q.
- Pièges (étiquette à porter par un distracteur) :
  - convertir une durée en heures et minutes comme un décimal — ligne C05#2a (d3)
  - réduire la durée totale sans refaire le partage entre pompes — ligne C05#2b (d4)
- Ne pas redemander : `15/01-pratique#7`, `15/01-pratique#9`, `15/05-entrainement#9`, `22/05-entrainement#10`, `22/04-defi#10`, `22/04-defi#7`
- Note : Pièges : ne pas refaire le partage entre pompes (réduire la durée sans recalculer qui fournit quoi) ; écrire 10 h 40 min comme 10,40 h (`math.mes.duree-convertie-en-base-cent`). Dernière étape à lire avec soin : « avancer de combien » = écart entre 2 h 40 et 55 min. Les 140 hl/h de l'énoncé sont donnés tels quels en tête de q2.

### m024 → `exercices/08-exam-2020-p1-ouvrier-bus-toutes-les-demi-heures.json` · d3 boss 120/30 · 9 questions · régime **examen**

- Titre de travail (à écrire en arabe : « 🏛️ مناظرة 2020 · المسألة 1 ⭐⭐⭐: … ») : Concours 2020 · problème 1 · le bus de l'ouvrier, toutes les demi-heures ⭐⭐⭐
- Registre : id `C07#1a` ; sources `C07#1a, C07#1b`
- Source : C07 (session 2020), problème 1 — transcription `2020-unique.md`
- Phrases officielles à reprendre (questions numérotées du sujet) :
  - 1. ابحث عن مدّة سير العامل من محطّة وصول الحافلة إلى مقرّ العمل.
  - 2. حدّد ساعة وصول العامل إلى مقرّ العمل، إذا خرج من منزله متأخّرا بـ 15 دق عن ساعة خروجه المعتادة.
- Étapes prévues :
  - q1 (durée de marche finale) : départ du domicile 6 h 35 ; marche de 15 min : arrivée à la station à 6 h 50 ; le bus passe à 7 h 00 (toutes les demi-heures dès 6 h) ; trajet 36 min : arrivée 7 h 36 ; arrivée au travail 7 h 45 : marche finale 9 min — QCM de l'attente du prochain bus, numériques des heures — 5 q.
  - q2 (arrivée s'il sort 15 min en retard) : 6 h 50 à la maison → 7 h 05 à la station ; le bus suivant est celui de 7 h 30 ; arrivée 8 h 06 ; + 9 min de marche : 8 h 15 — QCM du bus manqué, numériques — 4 q.
- Pièges (étiquette à porter par un distracteur) :
  - ne pas compter l'attente du prochain départ — ligne C07#1a (d3)
  - ajouter le retard directement à l'heure d'arrivée — ligne C07#1b (d3)
- Ne pas redemander : `22/02-boss#6`, `22/02-boss#9`, `22/02-boss#10`, `22/04-defi#4`, `22/04-defi#9`, `22/05-entrainement#6`, `22/05-entrainement#7`, `22/03-revision#8`
- Note : Pièges : ne pas compter l'attente du prochain départ ; ajouter directement le retard à l'heure d'arrivée (15 min de plus à 7 h 45 donne 8 h 00, alors que la bonne réponse est 8 h 15, car le bus de 7 h 30 est en réalité 30 min plus tard). La ligne de bus (cadence, début, fin) est redonnée dans l'énoncé de chaque question.

### m025 → `exercices/09-exam-2019-p2-voiture-retour-au-depart-reservoir.json` · d3 boss 120/30 · 9 questions · régime **examen**

- Titre de travail (à écrire en arabe : « 🏛️ مناظرة 2019 · المسألة 2 ⭐⭐⭐: … ») : Concours 2019 · problème 2 · retour à la station, puis la capacité du réservoir ⭐⭐⭐
- Registre : id `C08#2a` ; sources `C08#2a, C08#2b`
- Source : C08 (session 2019), problème 2 — transcription `2019-unique.md`
- Phrases officielles à reprendre (questions numérotées du sujet) :
  - 1. أحدّد ساعة وصول السّيارة إلى المدينة "ب" علما وأنّ معدّل السّرعة يساوي 70 كم/س.
  - 2. ما هي سعة الخزّان إذا علمت أنّ كمّية البنزين المستهلكة تُمثّل 3/5 الكمّية المتبقّية ؟
- Étapes prévues :
  - q1 (heure d'arrivée) : départ 8 h 45 ; 1 km de route, retour d'1 km à la station, 5 min d'arrêt, puis 124 km ; distance roulée 126 km à 70 km/h = 1,8 h = 1 h 48 ; + 5 min = 1 h 53 ; arrivée 10 h 38 — QCM de la distance totale roulée, numériques — 4 q.
  - q2 (capacité du réservoir, 15 L à l'arrivée) : la quantité consommée est les 3/5 de la quantité restante (15 L), soit 9 L ; départ : réservoir au tiers + 10 L ajoutés − 9 L = 15 L donc le tiers de la capacité vaut 14 L ; capacité = 42 L — QCM du « 3/5 de la quantité restante », numériques — 5 q.
- Pièges (étiquette à porter par un distracteur) :
  - ignorer le trajet d'aller-retour ou l'arrêt — ligne C08#2a (d3)
  - partir d'un réservoir plein au départ — ligne C08#2b (d3)
- Ne pas redemander : `22/04-defi#4`, `22/02-boss#10`, `15/02-boss#9`, `15/05-entrainement#7`, `11/04-defi#7`, `08/02-boss#5`, `13/02-boss#9`
- Note : Pièges : ignorer le trajet d'aller-retour ou l'arrêt ; partir d'un réservoir plein au départ (il est au tiers). 70 km/h donne 126 km en 1,8 h : on convertit 0,8 h en minutes (48), jamais 1,8 en 1 h 80. Les 10 L ajoutés le sont à la station, au retour.

### m026 → `exercices/10-exam-2015-p2-excursion-aller-retour.json` · d3 boss 120/30 · 7 questions · régime **examen**

- Titre de travail (à écrire en arabe : « 🏛️ مناظرة 2015 · المسألة 2 ⭐⭐⭐: … ») : Concours 2015 · problème 2 · l'excursion : heure de départ, vitesse du retour ⭐⭐⭐
- Registre : id `C12#2a` ; sources `C12#2a, C12#2b`
- Source : C12 (session 2015), problème 2 — transcription `2015-unique.md`
- Phrases officielles à reprendre (questions numérotées du sujet) :
  - 1- أحسُبُ ساعة انطلاق الحافلة من المدرسة إلى الموقع الأثريّ.
  - 2- أحسُبُ معدّل السّرعة عند العودة.
- Étapes prévues :
  - q1 (heure de départ de l'école) : le tableau donne 300 km pour l'aller ET le retour : l'aller fait 150 km à 60 km/h = 2 h 30 ; arrivée au site 9 h 10 ; départ 6 h 40 — QCM de la distance à utiliser (150 et non 300), numériques — 3 q.
  - q2 (vitesse au retour) : visite de 4 h 45 min de 9 h 10 à 13 h 55 ; retour à l'école à 16 h 55 : 3 h de route ; 150 ÷ 3 = 50 km/h — numériques de l'heure de fin de visite, de la durée de retour, de la vitesse — 4 q.
- Pièges (étiquette à porter par un distracteur) :
  - utiliser la distance de l'aller-retour pour le trajet aller — ligne C12#2a (d2)
  - garder la distance de l'aller-retour pour le seul retour — ligne C12#2b (d3)
- Ne pas redemander : `22/05-entrainement#6`, `22/05-entrainement#7`, `22/02-boss#9`, `22/04-defi#4`, `15/01-pratique#6`, `15/02-boss#4`, `15/03-revision#3`, `15/03-revision#7`, `15/05-entrainement#3`, `15/03-revision#8`
- Note : Pièges : utiliser la distance de l'aller-retour (300 km) pour le seul aller ; garder cette distance pour le seul retour. Le tableau officiel (distance, vitesse d'aller, heure d'arrivée, heure de retour, durée de visite) est refait en tableau lisible. Heures au format 24 h (16 h 55).

### m027 → `exercices/11-exam-2010-p2-trajet-de-nuit-passage-de-minuit.json` · d3 boss 120/30 · 7 questions · régime **examen**

- Titre de travail (à écrire en arabe : « 🏛️ مناظرة 2010 · المسألة 2 ⭐⭐⭐: … ») : Concours 2010 · problème 2 · un trajet de nuit, du jeudi au vendredi ⭐⭐⭐
- Registre : id `C17#2a` ; sources `C17#2a, C17#2b`
- Source : C17 (session 2010), problème 2 — transcription `2010-unique.md`
- Phrases officielles à reprendre (questions numérotées du sujet) :
  - 1- حدّد يوم وساعة وصول السيارة إلى المدينة "ب" إذا علمت أنّ معدّل سرعتها 80 كم/س.
  - 2- عند الانطلاق كانت كمية الوقود بالخزان 12 لترا. تزوّد السائق في الطريق بـ 15 لترا.
- Étapes prévues :
  - q1 (jour et heure d'arrivée) : départ jeudi 22 h 30 ; 200 km à 80 km/h = 2 h 30 de route, 20 min d'arrêt ; 22 h 30 + 2 h 50 = 25 h 20, soit vendredi 1 h 20 — QCM du changement de jour, numériques — 4 q.
  - q2 (carburant restant) : 12 L au départ + 15 L ajoutés = 27 L ; consommation de 10 L pour 100 km sur 200 km = 20 L ; il reste 7 L — numériques, QCM d'oubli du plein en route — 3 q.
- Pièges (étiquette à porter par un distracteur) :
  - oublier le changement de jour après minuit — ligne C17#2a (d3)
  - ne pas ajouter le ravitaillement en route — ligne C17#2b (d2)
- Ne pas redemander : `22/02-boss#10`, `22/04-defi#4`, `22/04-defi#7`, `22/04-defi#9`, `15/01-pratique#4`, `15/04-defi#4`, `15/05-entrainement#7`
- Note : Piège : oublier le changement de jour après minuit (jeudi 25 h 20 est vendredi 1 h 20). L'arrêt de 20 min est compté dans la durée du trajet mais pas dans la consommation. Passage de minuit absent des exercices actuels hors `22/02-boss#10` (22 h 30 + 6 h 45) : l'auteur varie la forme (jour demandé en plus de l'heure).

