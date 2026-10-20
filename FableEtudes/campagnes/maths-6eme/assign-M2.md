# Carte d'affectation M2 — maths 6ᵉ, chapitres `14`, `15` (missions du gisement)

> Lot auteur du passage unique (PLAN-gisement.md § 4). 9 missions, 74 questions. Skills : `content-ecole-tn`, puis `prof-math-6eme` (calibre les étages, jamais plus que le programme) ; consignes `content-ingest/references/gisement-auteur-examen.md` (missions 🏛️ : la transcription de la session citée, `content/programmes-officiels/examens-nationaux/6eme-base/math/<année>-unique.md`) et `gisement-auteur-devoir.md` (missions 📝 : la carte seule, jamais le devoir). Écris en arabe (`contentLanguage` du sujet). Ne touche à aucun autre chapitre que les tiens ; les autres lots écrivent en parallèle. Nom de fichier : `exercices/<fichier>` ci-dessous.

**Règles communes** (PLAN-gisement.md § 1) : une mission d'examen reprend UN problème entier d'une session, découpé en étapes notées ; chaque question dit sa session (« مناظرة 2023 ») et redonne les données et la phrase OFFICIELLES de la transcription qu'elle lit (valeurs, unités, décimaux à trois chiffres tels qu'imprimés, tableau refait lisible) ; un « أثبتُ أنّ… » devient « quelle valeur / quelle justification » (jamais la clé dans le titre ni dans l'énoncé) ; types natifs : `numeric` pour les valeurs, QCM pour le choix d'étape, la justification et la décision, `ordering` pour un raisonnement ou les étapes d'une construction ; une CONSTRUCTION n'est pas notable : on note les longueurs du plan (échelle) et l'ordre des étapes ; figures refaites en SVG, vraies, sans donner la clé ; π = 3,14 ; aucune algèbre littérale, ni Pythagore, ni somme des angles d'un triangle, ni calcul d'intérêt, ni partage « somme et écart / somme et rapport » (◐) ; jamais de corrigé de site tiers : l'explication est la tienne, re-résolue par deux chemins ; au plus 12 questions ; étage d3 = `boss` 120/30, d2 = `practice` 75/15. Étiquettes : `misconceptionTag` du registre `math.*` sur le distracteur qui EXÉCUTE l'erreur du « piège » de la ligne, jamais sur un multi, un ordering ni un matching ; un id qui manque se signale (on ne touche ni `content/misconceptions.json` ni `content/competences/`). `chapter.json` : ajoute à `sources[]` — missions d'examen : « Sujets officiels du concours d'entrée aux collèges pilotes (6ᵉ année de base), Ministère de l'Éducation (corpus officiel, reprise citée, étude 36) — transcriptions : programmes-officiels/examens-nationaux/6eme-base/math/ » ; missions de devoir : « Calibré sur des devoirs publics (étude 36, T2′, aucune reprise) — carte : programmes-officiels/sources-externes/web-6eme-base-math/fiche.md ». Numéros de fichiers : à la suite de `05-entrainement` (06, 07, …), `displayOrder` à la suite ; les missions de chaque chapitre dans l'ordre de la carte. Gates à chaque chapitre : `content:check`, `content:qa -- --subject math-6eme` (0 erreur), `content:tranche -- --subject math-6eme --changed --fresh --strict-longest`.

**Étiquettes déjà en usage dans tes chapitres** : `14` : `math.prop.pourcentage-recopie-comme-resultat` (Tu recopies un nombre de l'énoncé au lieu de calculer : 20 %); `math.num.operation-inverse-appliquee` (Tu fais l'opération contraire de celle demandée : une additi); `math.prop.additive-au-lieu-de-multiplicative` (Tu ajoutes la différence au lieu de multiplier : dans une si); `math.prop.pourcentage-base-erronee` (Tu calcules le pourcentage sur la mauvaise base : une baisse); `math.frac.fraction-d-un-nombre-etape-oubliee` (Tu n'as fait qu'une moitié du calcul : prendre 3/5 d'un nomb); `math.mes.perimetre-rectangle-somme-non-doublee` (Tu additionnes la longueur et la largeur sans doubler : le r) | `15` : `math.num.operation-inverse-appliquee` (Tu fais l'opération contraire de celle demandée : une additi); `math.prop.vitesse-grandeurs-additionnees` (Tu additionnes la distance et la durée : ce sont deux grande); `math.prop.formule-vitesse-inversee` (Tu inverses la formule : la vitesse est la distance DIVISÉE ); `math.mes.duree-convertie-en-base-cent` (Le temps ne se convertit ni par 10 ni par 100 : la minute va); `math.prop.additive-au-lieu-de-multiplicative` (Tu ajoutes la différence au lieu de multiplier : dans une si).


## Chapitre `14-proportionnalite-pourcentage`

### m010 → `exercices/06-exam-2026-p1-marchand-caisses-hausse-5-pourcent.json` · d3 boss 120/30 · 7 questions · régime **examen**

- Titre de travail (à écrire en arabe : « 🏛️ مناظرة 2026 · المسألة 1 ⭐⭐⭐: … ») : Concours 2026 · problème 1 · rapport entre deux genres, puis hausse de 5 % des recettes ⭐⭐⭐
- Registre : id `C01#1a` ; sources `C01#1a, C01#1b`
- Source : C01 (session 2026), problème 1 — transcription `2026-unique.md`
- Phrases officielles à reprendre (questions numérotées du sujet) :
  - 1) أثبتُ أنّ التّاجر يحقّق مداخيل من بيع الغلال قدرها 9000 د.
  - 2) أحسبُ عدد الصّناديق من النّوع الأوّل بعد التّعويض.
- Étapes prévues :
  - q1 (« أثبتُ أنّ التّاجر يحقّق مداخيل ... قدرها 9000 د ») : 400 caisses ; le nombre du premier genre est le tiers de celui du second, donc le quart du total : 100 et 300 ; recette = 100 × 45 + 300 × 15 = 9000 d — QCM de la part du total (1/4 et non 1/3), numériques des deux effectifs, de la recette — 4 q.
  - q2 (nombre de caisses du premier genre après le remplacement) : +5 % de 9000 d = 450 d de plus ; chaque caisse du second genre remplacée par une du premier genre rapporte 45 − 15 = 30 d de plus ; 450 ÷ 30 = 15 caisses remplacées ; premier genre = 100 + 15 = 115 — QCM du gain par échange, numériques — 3 q.
- Pièges (étiquette à porter par un distracteur) :
  - lire le rapport entre deux types comme un rapport au total — ligne C01#1a (d3)
  - appliquer le pourcentage au nombre de caisses et non à la recette — ligne C01#1b (d4)
- Ne pas redemander : `14/03-revision#9`, `14/02-boss#10`, `14/02-boss#8`, `13/04-defi#7`, `08/02-boss#7`
- Note : Pièges du lecteur : lire « le tiers du second » comme une part du total ; appliquer le pourcentage au nombre de caisses et non à la recette. Le « montrer que » devient « quelle valeur » (9000 d) : la clé de la q1 ne se lit dans aucun titre.

### m011 → `exercices/07-exam-2024-p2-club-musique-trois-tranches.json` · d3 boss 120/30 · 7 questions · régime **examen**

- Titre de travail (à écrire en arabe : « 🏛️ مناظرة 2024 · المسألة 2 ⭐⭐⭐: … ») : Concours 2024 · problème 2 · le tarif d'un club selon le nombre d'heures ⭐⭐⭐
- Registre : id `C03#2a` ; sources `C03#2a, C03#2b`
- Source : C03 (session 2024), problème 2 — transcription `2024-unique.md`
- Phrases officielles à reprendre (questions numérotées du sujet) :
  - 1) أحسبُ بالدّينار المبلغ الّذي دفعه أمين علمًا أنّه اختار أن يتدرّب 136 ساعة.
  - 2) ما هو عدد السّاعات الّتي اخترت ياسمين أن تتدرّبها ؟
- Étapes prévues :
  - q1 (somme payée par Amine pour 136 heures) : lire le tableau (136 heures : tranche « de 101 à 149 », neuf dixièmes) ; plein tarif 136 × 8 = 1088 d ; 9/10 → 979,2 d — QCM de la tranche, numériques — 3 q.
  - q2 (nombre d'heures de Yasmine, plus de 136 pour la même somme) : la tranche 101–149 est exclue (plus d'heures ferait payer plus) ; il s'agit de la tranche « plus de 149 » avec 20 % de réduction ; une heure coûte 8 × 0,8 = 6,4 d ; 979,2 ÷ 6,4 = 153 heures — QCM du raisonnement sur les tranches, numériques de l'heure réduite et des heures, QCM de contrôle de la tranche (153 > 149) — 4 q.
- Pièges (étiquette à porter par un distracteur) :
  - choisir la mauvaise tranche du tableau — ligne C03#2a (d2)
  - traduire la réduction par un multiplicateur à l'envers — ligne C03#2b (d4)
- Ne pas redemander : `14/04-defi#2`, `14/04-defi#3`, `14/02-boss#4`, `14/04-defi#11`, `14/04-defi#10`, `14/05-entrainement#10`, `13/quiz#6`
- Note : Pièges : choisir la mauvaise tranche ; traduire « réduction de 20 % » par un multiplicateur à l'envers (× 1,2 ou ÷ 0,8 mal posé). Le tableau des trois tranches est redonné dans chaque question qui le lit.

### m012 → `exercices/08-exam-2021-p1-machine-agricole-contributions.json` · d3 boss 120/30 · 10 questions · régime **examen**

- Titre de travail (à écrire en arabe : « 🏛️ مناظرة 2021 · المسألة 1 ⭐⭐⭐: … ») : Concours 2021 · problème 1 · le prix d'une machine, puis les économies du père ⭐⭐⭐
- Registre : id `C06#1a` ; sources `C06#1a, C06#1b`
- Source : C06 (session 2021), problème 1 — transcription `2021-unique.md`
- Phrases officielles à reprendre (questions numérotées du sujet) :
  - 1- أحسبُ المبلغ الّذي جمعته العائلة.
  - 2- أحسبُ مدّخرات الأب.
- Étapes prévues :
  - q1 (somme réunie par la famille) : option 1 = prix de la machine + 803 d ; option 2 = moitié du prix + semences à 4303 d ; la moitié du prix vaut 4303 − 803 = 3500 d ; prix 7000 d ; somme réunie 7803 d — QCM de la comparaison des deux options, numériques — 4 q.
  - q2 (économies du père) : père = 75 % de ses économies (3/4) ; fils = 1/3 de la contribution du père (1/4 des économies) ; mère = 2 × fils + 150 d = 1/2 des économies + 150 d ; total = 1,5 fois les économies + 150 = 7803 ; 1,5 × économies = 7653 ; économies = 5102 d — QCM de l'écriture de chaque contribution en part des économies, numériques — 6 q.
- Pièges (étiquette à porter par un distracteur) :
  - ajouter les deux restes au lieu de les comparer — ligne C06#1a (d3)
  - appliquer le pourcentage à la contribution au lieu de l'épargne — ligne C06#1b (d4)
- Ne pas redemander : `14/02-boss#8`, `14/04-defi#11`, `14/04-defi#10`, `13/04-defi#7`, `04/05-entrainement#7`, `02/05-entrainement#6`, `14/02-boss#10`
- Note : Piège de la q2 : appliquer le pourcentage à la contribution (au lieu de l'épargne) ; ajouter les deux restes au lieu de les comparer (q1). Aucun calcul littéral : le raisonnement passe par « la contribution du père vaut les 3/4 de ses économies ». Les 150 d s'ajoutent après avoir doublé la contribution du fils.

### m013 → `exercices/09-exam-2019-p1-tableau-numerique-remise-25.json` · d3 boss 120/30 · 9 questions · régime **examen**

- Titre de travail (à écrire en arabe : « 🏛️ مناظرة 2019 · المسألة 1 ⭐⭐⭐: … ») : Concours 2019 · problème 1 · l'argent restant, puis le prix avant la remise ⭐⭐⭐
- Registre : id `C08#1a` ; sources `C08#1a, C08#1b`
- Source : C08 (session 2019), problème 1 — transcription `2019-unique.md`
- Phrases officielles à reprendre (questions numérotées du sujet) :
  - 1. أحسبُ المبلغ المالي المتبقّي.
  - 2. أحسبُ ثمن اللّوحة الرّقمية قبل التّخفيض.
- Étapes prévues :
  - q1 (montant restant) : avec le reste, on peut acheter 6 chaises et garder 30 d, OU la table (90 d) + 4 chaises, sans reste ; donc 2 chaises + 30 d = 90 d ; 2 chaises = 60 d ; 1 chaise = 30 d ; reste = 90 + 4 × 30 = 210 d — QCM de ce que représente l'écart, numériques — 4 q.
  - q2 (prix avant remise) : ce reste est les 4/7 de la somme initiale ; 1/7 = 52,5 d ; somme = 367,5 d ; la dépense (3/7) = 157,5 d est le prix APRÈS une remise de 25 % ; le prix d'origine est 157,5 ÷ 0,75 = 210 d — QCM de la fraction dépensée, numériques, QCM de la base de la remise — 5 q.
- Pièges (étiquette à porter par un distracteur) :
  - attribuer l'écart à la table plutôt qu'aux chaises — ligne C08#1a (d3)
  - traiter la réduction comme un supplément — ligne C08#1b (d4)
- Ne pas redemander : `14/04-defi#2`, `14/04-defi#3`, `14/04-defi#11`, `14/02-boss#8`, `13/04-defi#7`, `13/02-boss#7`, `14/quiz#7`, `02/04-defi#3`, `02/05-entrainement#6`
- Note : Pièges : attribuer l'écart des deux achats à la table plutôt qu'aux chaises ; traiter la remise de 25 % comme un supplément (prix = 157,5 × 1,25). Le résultat final (210 d) coïncide avec le reste de la q1 : sans lien, l'auteur ne le laisse pas dans les options de la q2 comme distracteur « évident ».

### m014 → `exercices/10-devoir-plan-et-carte-a-l-echelle.json` · d2 practice 75/15 · 7 questions · régime **devoir (salle blanche)**

- Titre de travail (arabe : « ⭐ تمرين موجّه / ⚔️ زعيم الفرض ⭐⭐: … ») : Lire un plan et une carte à l'échelle : longueurs réelles, aller-retour, périmètre ⭐⭐
- Registre : id `D01#6` ; sources `D01#6, D01#7, D05#2a, D05#2b, D05#3b, D05#3c, D02#12a, D08#6`
- Cartes : devoir A (T1, école primaire), exercice(s) 6, 7 ; devoir B (T1, école primaire), exercice(s) 12a ; devoir E (T2, école primaire), exercice(s) 2a, 2b, 3b, 3c ; devoir G (T3, école primaire), exercice(s) 6 — cartes anonymes
- Gestes lus (archétype des lecteurs, sans nombre) :
  - D01#6 (d2) : retrouver une longueur réelle depuis une mesure sur plan et une échelle
  - D01#7 (d2) : retrouver une largeur réelle depuis une mesure sur plan et une échelle
  - D05#2a (d2) : retrouver des distances réelles depuis des longueurs sur une carte et une échelle en kilomètres
  - D05#2b (d2) : calculer une distance totale aller et retour en additionnant des étapes
  - D05#3b (d2) : retrouver des dimensions réelles depuis un plan à l’échelle
  - D05#3c (d2) : calculer un périmètre réel d’un trapèze et l’exprimer en hectomètres
  - D02#12a (d2) : vérifier des longueurs sur plan depuis des longueurs réelles et une échelle
  - D08#6 (d2) : déduire un périmètre réel depuis un périmètre sur plan et une échelle
- Étapes prévues :
  - Une carte à l'échelle donnée en kilomètres : convertir deux longueurs du plan en distances réelles (multiplier, pas diviser), passer des centimètres aux kilomètres — QCM, numériques — 3 q.
  - Additionner les étapes puis tenir compte du retour (distance d'un aller-retour) — numérique, QCM — 2 q.
  - Un plan d'un terrain à quatre côtés : retrouver les dimensions réelles de chaque côté, le périmètre réel, l'exprimer dans l'unité demandée (hectomètres) — numériques — 2 q. Vérifier des longueurs sur plan à partir des longueurs réelles (sens inverse) en un item.
- Pièges (étiquette à porter par un distracteur) :
  - oublier de convertir les unités de longueur — ligne D01#6 (d2)
  - diviser par l’échelle au lieu de multiplier — ligne D01#7 (d2)
  - diviser par l’échelle au lieu de multiplier — ligne D05#2a (d2)
  - oublier le trajet de retour — ligne D05#2b (d2)
  - se tromper de conversion entre centimètres et mètres — ligne D05#3b (d2)
  - convertir de travers vers l’hectomètre — ligne D05#3c (d2)
  - confondre mètres et centimètres — ligne D02#12a (d2)
  - se tromper de conversion de centimètres en mètres — ligne D08#6 (d2)
- Ne pas redemander : `14/quiz#6`, `14/01-pratique#7`, `14/02-boss#7`, `14/03-revision#7`, `14/03-revision#10`, `14/05-entrainement#7`, `15/04-defi#9`, `16/04-defi#8`
- Note : Salle blanche. Le patron du `14` convertit une longueur sur un plan ; les gestes neufs sont l'aller-retour sur carte, le passage cm → km sur une échelle en millions et le périmètre réel d'un quadrilatère lu sur plan avec unité de sortie imposée. Les constructions à l'échelle ne sont pas dans cette mission (voir la mission des constructions au `19`).


## Chapitre `15-vitesse-distance-temps`

### m015 → `exercices/06-exam-2026-p2-camion-voiture-reservoir.json` · d3 boss 120/30 · 8 questions · régime **examen**

- Titre de travail (à écrire en arabe : « 🏛️ مناظرة 2026 · المسألة 2 ⭐⭐⭐: … ») : Concours 2026 · problème 2 · le réservoir du camion, puis la distance entre deux villes ⭐⭐⭐
- Registre : id `C01#2a` ; sources `C01#2a, C01#2b`
- Source : C01 (session 2026), problème 2 — transcription `2026-unique.md`
- Phrases officielles à reprendre (questions numérotées du sujet) :
  - 1) أثبتُ أنّ الشّاحنة قطعت 60 كم في ساعة.
  - 2) أحسبُ المسافة الفاصلة بين المدينتين بالكم.
- Étapes prévues :
  - q1 (« أثبتُ أنّ الشّاحنة قطعت 60 كم في ساعة ») : le réservoir contient 4/5 de sa capacité au départ ; après 1 heure il en a consommé 1/20 donc il reste 4/5 − 1/20 = 3/4 de la capacité ; ce reste vaut 90 L donc la capacité est 120 L et la consommation d'une heure 6 L ; à 10 L pour 100 km, 6 L correspondent à 60 km — QCM de la fraction restante, numériques de la capacité, des litres consommés, de la distance — 5 q.
  - q2 (distance entre les villes) : la voiture roule à 60 + 20 = 80 km/h ; en 1 heure elle fait 80 km, soit les 2/5 de la distance ; 80 ÷ 2 × 5 = 200 km — QCM de la vitesse, numérique de la distance — 3 q.
- Pièges (étiquette à porter par un distracteur) :
  - confondre fraction de capacité et volume en litres — ligne C01#2a (d4)
  - multiplier par la fraction au lieu de retrouver le tout — ligne C01#2b (d3)
- Ne pas redemander : `15/01-pratique#3`, `15/02-boss#3`, `15/03-revision#7`, `15/04-defi#7`, `15/04-defi#10`, `15/05-entrainement#9`, `13/04-defi#7`, `13/02-boss#9`, `08/04-defi#2`
- Note : Pièges : confondre fraction de capacité et volume en litres ; multiplier par la fraction au lieu de retrouver le tout. Les 90 L, 4/5 et 1/20 sont à redonner dans chaque question qui les utilise.

### m016 → `exercices/07-exam-2023-p3-cycliste-montee-descente.json` · d3 boss 120/30 · 9 questions · régime **examen**

- Titre de travail (à écrire en arabe : « 🏛️ مناظرة 2023 · المسألة 3 ⭐⭐⭐: … ») : Concours 2023 · problème 3 · montée et descente d'un cycliste ⭐⭐⭐
- Registre : id `C04#3a` ; sources `C04#3a, C04#3b, C04#3c`
- Source : C04 (session 2023), problème 3 — transcription `2023-unique.md`
- Phrases officielles à reprendre (questions numérotées du sujet) :
  - 1) أثبتُ أنّ قيس طول الجزء ② يساوي 3,2 كم، علما أنّه يمثّل 40 % من قيس طول الجزء ①.
  - 2) أحدّد معدّل سرعة الدّرّاج بالكم/س أثناء قطع الجزء ② نزولا.
  - 3) هل أنّ قطع الجزء ① نزولا بسرعة معدّلها 12 كم/س يمكّن الدّرّاج من قطع كامل المسلك صعودا ونزولا في 114 دق ؟ أعلّل إجابتي.
- Étapes prévues :
  - q1 (« أثبتُ أنّ قيس طول الجزء ② يساوي 3,2 كم ») : 48 min = 0,8 h ; partie ① = 10 × 0,8 = 8 km ; partie ② = 40 % de 8 = 3,2 km — QCM de la conversion, numériques — 3 q.
  - q2 (vitesse en descente du ②) : 36 min pour la montée et la descente ; la descente dure la moitié de la montée donc le tiers du total : 12 min = 0,2 h ; 3,2 ÷ 0,2 = 16 km/h — QCM du partage de 36 min (2 parts / 1 part), numériques — 3 q.
  - q3 (le tour complet en 114 minutes ?) : ① en descente à 12 km/h : 8 ÷ 12 h = 40 min ; total = 48 + 40 + 36 = 124 min > 114 : non — numérique, QCM de la comparaison avec justification — 3 q.
- Pièges (étiquette à porter par un distracteur) :
  - ne pas convertir les minutes en heures — ligne C04#3a (d3)
  - partager la durée totale en deux parts égales — ligne C04#3b (d4)
  - omettre l'autre portion du parcours dans la durée totale — ligne C04#3c (d3)
- Ne pas redemander : `15/01-pratique#7`, `15/02-boss#7`, `15/02-boss#10`, `15/03-revision#8`, `15/04-defi#2`, `15/04-defi#8`, `15/05-entrainement#10`, `14/04-defi#1`, `22/quiz#3`
- Note : Pièges : ne pas convertir les minutes en heures ; partager les 36 minutes en deux parts égales (6/6) ; oublier la montée de la partie ① dans le total. Parcours en deux parties : la q1 et la q3 réutilisent le 8 km.

### m017 → `exercices/08-exam-2021-p2-voiture-camion-pause.json` · d3 boss 120/30 · 9 questions · régime **examen**

- Titre de travail (à écrire en arabe : « 🏛️ مناظرة 2021 · المسألة 2 ⭐⭐⭐: … ») : Concours 2021 · problème 2 · une voiture, un camion et une pause ⭐⭐⭐
- Registre : id `C06#2a` ; sources `C06#2a, C06#2b`
- Source : C06 (session 2021), problème 2 — transcription `2021-unique.md`
- Phrases officielles à reprendre (questions numérotées du sujet) :
  - 1- أحسبُ طول المسافة الفاصلة بين المدينتين "أ" و "ب" إذا علمت أنّ معدّل سرعة السّيّارة يساوي 80 كم/س.
  - 2- أحسبُ مدّة استراحة صاحب الشّاحنة.
- Étapes prévues :
  - q1 (distance entre les deux villes) : 1 h 36 min = 1,6 h (ou 96 min) ; la voiture a fait 80 × 1,6 = 128 km ; il lui en reste 16 ; distance = 144 km — QCM de la conversion de 1 h 36 min, numériques — 3 q.
  - q2 (durée de la pause du camion) : le camion a fait les 4/5 de 144 = 115,2 km en 1 h 36 min, donc à 72 km/h ; il lui reste 28,8 km (24 min de route) ; la voiture arrive 12 min plus tard (16 km à 80 km/h), le camion 24 min après la voiture, soit 36 min après l'instant 1 h 36 ; sa pause vaut 36 − 24 = 12 min — QCM de la vitesse du camion, numériques du temps de route restant, de l'écart d'arrivée, de la pause — 6 q.
- Pièges (étiquette à porter par un distracteur) :
  - convertir une durée en heures et minutes comme un décimal — ligne C06#2a (d3)
  - compter la pause dans le temps de roulage — ligne C06#2b (d4)
- Ne pas redemander : `15/03-revision#7`, `15/04-defi#7`, `15/05-entrainement#9`, `15/03-revision#9`, `22/04-defi#9`, `13/02-boss#9`
- Note : Pièges : écrire 1 h 36 min comme 1,36 h (`math.mes.duree-convertie-en-base-cent`) ; compter la pause dans le temps de roulage. Le camion garde la même vitesse après la pause (énoncé officiel). Tous les nombres tombent juste en minutes ; en heures décimales le 72 km/h passe par 1,6.

### m018 → `exercices/09-exam-2017-p1-fermier-lait-fraction-du-trajet.json` · d3 boss 120/30 · 8 questions · régime **examen**

- Titre de travail (à écrire en arabe : « 🏛️ مناظرة 2017 · المسألة 1 ⭐⭐⭐: … ») : Concours 2017 · problème 1 · le trajet jusqu'au centre de collecte ⭐⭐⭐
- Registre : id `C10#1a` ; sources `C10#1a, C10#1b`
- Source : C10 (session 2017), problème 1 — transcription `2017-unique.md`
- Phrases officielles à reprendre (questions numérotées du sujet) :
  - 1- أحسبُ المسافة الفاصلة بين الضيعة و مركز تجميع الحليب.
  - 2- أثبتُ حسابيّا أنّ وصولَ الفلّاح إلى المركز كان على السّاعة 7 و 23 دق.
- Étapes prévues :
  - q1 (distance ferme–centre) : départ 5 h 28 à 60 km/h ; 40 min de route = 40 km ; le reste du trajet vaut les 3/2 de la distance déjà faite (fraction supérieure à 1) : 60 km ; distance totale 100 km — QCM de la conversion minutes → km, numériques de la fraction, de la distance totale — 4 q.
  - q2 (« أثبتُ ... على السّاعة 7 و 23 دق ») : la seconde partie dure 60 min ; durée totale = 40 + 15 (arrêt) + 60 = 115 min = 1 h 55 ; 5 h 28 + 1 h 55 = 7 h 23 — QCM des durées à additionner (l'arrêt compte), numériques, QCM du report des minutes au-delà de 60 — 4 q.
- Pièges (étiquette à porter par un distracteur) :
  - confondre minutes et heures dans une vitesse horaire — ligne C10#1a (d3)
  - oublier l'arrêt ou mal reporter les minutes au-delà de soixante — ligne C10#1b (d3)
- Ne pas redemander : `15/04-defi#7`, `15/02-boss#9`, `15/03-revision#7`, `22/04-defi#4`, `22/02-boss#10`, `13/02-boss#9`, `08/04-defi#2`
- Note : Mission « jumelle » du problème 3 du concours 2008 (mêmes gestes, autres nombres, plus la consommation de carburant) : une seule des deux est reprise (2017). Pièges : oublier l'arrêt ou mal reporter les minutes au-delà de 60 ; lire 3/2 comme une part de la distance totale.

