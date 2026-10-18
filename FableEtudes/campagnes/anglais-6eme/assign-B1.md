# Carte d'affectation B1 — anglais 6ᵉ, chapitres 01, 02 (gisement + étiquettes + défauts)

> Lot auteur du passage unique (PLAN.md, lots B ; PLAN-gisement.md § 3). Un seul auteur sur ces chapitres. Skills : `content-ecole-tn` puis `content-langue-anglais` ; consignes `content-ingest/references/gisement-auteur-examen.md` (missions d'examen, avec la transcription de chaque session citée) et `gisement-auteur-devoir.md` (missions 📝 : la carte seule, jamais le devoir). Ne touche à aucun autre chapitre ; les autres lots écrivent en parallèle.

**Ordre de travail** : (1) les ids neufs et les libellés élargis que tu poses → `content/misconceptions.json` (textes exacts dans `vocab-english-6eme.json`) ; (2) partie 2 et partie 3 sur les fichiers existants ; (3) partie 1, les missions ; (4) `coursePitfalls` en dernier. Gates à chaque chapitre : `content:check`, `content:qa -- --subject english-6eme` (0 erreur), `content:tranche -- --subject english-6eme --changed --fresh --strict-longest`, rendu `renderLesson` si un cours est touché.


## Chapitre `01-entertaining-myself`

### Partie 1 — missions (gisement)

#### m001 → `exercices/06-exams-2008-2025-like-ing-how-often.json` · d2 practice 75/15 · 12 questions · régime **examen**

- Titre : « 🏛️ Exams 2008–2025 · like + -ing, how often and the -s ⭐⭐ »
- Registre : id `C04#2` ; sources `C04#2, C02#5, C03#2, C09#3, C14#3, C17#2, C17#3, C18#6, C19#5, C10#5, C12#5`
- Sources (base en premier) : C04 (2023) ex. 2 ; C02 (2025) ex. 5 ; C03 (2024) ex. 2 ; C09 (2018) ex. 3 ; C14 (2013) ex. 3 ; C17 (2010) ex. 2 ; C17 (2010) ex. 3 ; C18 (2009) ex. 6 ; C19 (2008) ex. 5 ; C10 (2017) ex. 5 ; C12 (2015) ex. 5
- Items :
  - 2023 L1 blanc 1 : adverbe de fréquence dans la banque (always / never) — QCM
  - 2024 L1 blanc 2 : sometimes (banque) — QCM
  - 2025 W1 a : phrase à remettre en ordre avec usually et le -s (ordering)
  - 2018 L2 : like + swim / swims / swimming — QCM
  - 2013 L2 : Every weekend, she going / go / goes — QCM
  - 2010 L1 : le verbe like à la 3ᵉ personne dans le cloze (banque imprimée) — QCM
  - 2010 L2 : in / on the morning — QCM
  - 2009 W2 b et 2008 W1 a, c : like + -ing, on Sundays (ordering, deux items)
  - 2017 W1 : live → lives (la faute soulignée devient un QCM de correction)
  - 2015 W1 : I usually drinking → drink (idem)
- Ne pas redemander : `01/quiz#1`, `01/quiz#2`, `01/quiz#3`, `01/01-pratique#2`, `01/01-pratique#5`, `01/01-pratique#6`, `01/02-boss#2`, `01/02-boss#6`, `01/03-revision#2`, `01/05-entrainement#2`, `01/05-entrainement#3`, `01/05-entrainement#6`
- Note : R1 : chaque item redonne la phrase officielle avec UN blanc et dit sa session ; les items HP des mêmes exercices (present continuous, have got, there is) ne sont jamais la cible.

#### m002 → `exercices/07-exams-2008-2021-possessives-and-linkers.json` · d2 practice 75/15 · 9 questions · régime **examen**

- Titre : « 🏛️ Exams 2008–2021 · his, her, their — and, but, because ⭐⭐ »
- Registre : id `C06#2` ; sources `C06#2, C07#4, C08#2, C11#4, C15#2, C18#3, C19#3`
- Sources (base en premier) : C06 (2021) ex. 2 ; C07 (2020) ex. 4 ; C08 (2019) ex. 2 ; C11 (2016) ex. 4 ; C15 (2012) ex. 2 ; C18 (2009) ex. 3 ; C19 (2008) ex. 3
- Items :
  - 2021 L1 : because (cause) ; so, ___ bed and desk (his) — deux QCM ; le blanc « There ___ » (HP) est donné rempli
  - 2020 L3 : tall too / and / with slim ; Him / Her / His friend — deux QCM (« has got / get / go » écarté, HP)
  - 2019 L1 : because / then / but — QCM (He / She / They écarté : pronom sujet, HP)
  - 2016 L3 : Their / They names — QCM (pose english.pron.sujet-au-lieu-du-possessif)
  - 2012 L1 : … rooms ___ there isn't a garden (but) — QCM
  - 2009 L2 : his / her favourite cartoon — QCM
  - 2008 L2 : His / Her name — QCM
- Ne pas redemander : `01/quiz#5`, `01/01-pratique#3`, `01/01-pratique#4`, `01/02-boss#4`, `01/03-revision#5`, `01/04-defi#4`, `01/05-entrainement#4`
- Note : Écartés : 2022 L3 (with her / him / their : pronom complément), 2024 L2 (they / them / their : la clé est le complément them) — HP:personal-pronouns.

#### m003 → `exercices/08-exams-2023-2026-dialogues-suggest-invite.json` · d2 practice 75/15 · 8 questions · régime **examen**

- Titre : « 🏛️ Exams 2023, 2026 · dialogues: suggest, invite, answer ⭐⭐ »
- Registre : id `C04#5` ; sources `C04#5, C01#5`
- Sources (base en premier) : C04 (2023) ex. 5 ; C01 (2026) ex. 5
- Items :
  - 2023 W1 : remettre en ordre la conversation (ordering, 5 répliques) puis 3 QCM sur la fonction de chaque réplique (invitation, refus avec can't, suggestion How about, Let's)
  - 2026 W1 : dialogue à compléter (matching des 4 cercles, une option en trop), puis 2 QCM : quelle réplique fait une suggestion (What about…?), laquelle demande de l'aide (Can you help…?)
- Ne pas redemander : `01/quiz#4`, `01/02-boss#1`, `01/02-boss#3`, `01/03-revision#3`, `01/03-revision#4`, `01/04-defi#1`, `01/04-defi#5`, `01/05-entrainement#5`
- Note : Placement déclaré (D2) : dialogue de fonctions → 01 (suggestion, invitation) ; les répliques en will, should, can sont lues pour leur fonction, sans règle nouvelle. « I am going to bring » (2026, HP going-to) reste une réplique donnée.

#### m004 → `exercices/09-exam-2023-reading-drawing-competition.json` · d2 practice 75/15 · 7 questions · régime **examen**

- Titre : « 🏛️ Exam 2023 · reading: the drawing competition ⭐⭐ »
- Registre : id `C04#1` ; sources `C04#1`
- Sources (base en premier) : C04 (2023) ex. 1
- Items :
  - Q1 vrai/faux ×2 → QCM vrai/faux puis QCM « quelle phrase du texte le prouve »
  - Q2 Tick : la compétition commence (afternoon) — QCM
  - Q3 deux mots du paragraphe 3 (best, prize/gift) — QCM de mots du paragraphe
  - Q4 Why can't Zoey jump? → QCM de la raison fondée (fauteuil roulant)
- Ne pas redemander : rien d'équivalent dans le chapitre
- Note : Texte support résumé, une à deux phrases citées par question (R2 du 9ᵉ) ; aucune question existante du 01 n'est une lecture de texte.

### Partie 2 — étiquetage des options existantes (objectif ≥ 60 %)

- 105 distracteurs, 0 étiqueté aujourd'hui → **au moins 63** à étiqueter. Les missions neuves s'étiquettent aussi, au même seuil.
- Étiquettes à employer (vocabulaire du lot A ; un distracteur qui ne dit aucune de ces erreurs reste muet) :
  - `english.adv.frequence-mal-placee` (neuf)
  - `english.func.fonction-mal-identifiee` (existant)
  - `english.link.connecteur-de-mauvais-type` (existant)
  - `english.modal.to-en-trop` (existant)
  - `english.prep.on-in-du-temps` (neuf)
  - `english.pron.possessif-du-mauvais-possesseur` (neuf)
  - `english.pron.sujet-au-lieu-du-possessif` (neuf)
  - `english.question.mot-interrogatif-inadapte` (existant)
  - `english.sound.lettre-pour-son` (neuf)
  - `english.verb.ing-oublie` (élargi)
  - `english.verb.s-oublie-3e-personne` (existant)
  - `english.vocab.mot-voisin-du-meme-champ` (neuf)
- `english.vocab.mot-voisin-du-meme-champ` seulement quand un indice de l'énoncé tranche (décision E7) ; jamais sur un distracteur absurde.
- Contrôle : `git diff --stat` après chaque fichier (un script qui réécrit le JSON gonfle le diff : ne changer que les `misconceptionTag`).

### Partie 3 — `coursePitfalls` et défauts `content:tranche`

- `coursePitfalls` proposés (chacun porté par au moins un distracteur du chapitre, C-5) : `english.verb.ing-oublie`, `english.modal.to-en-trop`, `english.pron.possessif-du-mauvais-possesseur`, `english.adv.frequence-mal-placee`, `english.verb.s-oublie-3e-personne`
- **Clé strictement la plus longue** (6) — rallonger un distracteur ou resserrer la clé, sans changer la réponse : `01-entertaining-myself/quiz#4`, `01-entertaining-myself/quiz#5`, `01-entertaining-myself/01-pratique#4`, `01-entertaining-myself/03-revision#4`, `01-entertaining-myself/04-defi#5`, `01-entertaining-myself/05-entrainement#2`
- **Paires proches** : aucune dans ce chapitre.
- **Gabarits inter-chapitres** (à l'auditeur ; l'auteur varie la consigne du sien) :
  - « three of these suggestions are correct which one is correct » : `01-entertaining-myself/04-defi#1`
  - « read which sentence about is true » : `01-entertaining-myself/04-defi#6`


## Chapitre `02-keeping-fit`

### Partie 1 — missions (gisement)

#### m005 → `exercices/06-exams-2010-2025-should-must-can-how-much.json` · d2 practice 75/15 · 8 questions · régime **examen**

- Titre : « 🏛️ Exams 2010–2025 · should, must, can — have a stomachache — How much ⭐⭐ »
- Registre : id `C02#5` ; sources `C02#5, C04#2, C09#3, C14#3, C07#2`
- Sources (base en premier) : C04 (2023) ex. 2 ; C02 (2025) ex. 5 ; C09 (2018) ex. 3 ; C14 (2013) ex. 3 ; C07 (2020) ex. 2
- Items :
  - 2023 L1 blancs 2 et 3 : has a ___ (stomachache), must drink ___ water (much) — deux QCM
  - 2023 L1 complet : quel mot de la banque est en trop (many, never) — QCM
  - 2025 W1 b : can't … because she has a stomachache (ordering)
  - 2018 L2 : aren't / can't / haven't go — QCM
  - 2013 L2 : She can / are / is sing very well — QCM
  - 2020 L1 : How many playgrounds + are there? (appariement : la partie « are there » est donnée, la cible est How many) — matching
- Ne pas redemander : `02/quiz#2`, `02/quiz#3`, `02/quiz#4`, `02/quiz#5`, `02/01-pratique#3`, `02/01-pratique#4`, `02/01-pratique#5`, `02/02-boss#2`, `02/02-boss#5`, `02/03-revision#2`, `02/03-revision#4`, `02/03-revision#6`, `02/05-entrainement#3`, `02/05-entrainement#4`
- Note : Écartés : How many … have you got? (2019 W1 a, 2020 W1 d : have got, HP), 2015 W1 b (idem). Le must de 2023 est donné : la cible est much.

#### m006 → `exercices/07-exam-2024-writing-doctors-advice.json` · d3 boss 120/30 · 8 questions · régime **examen**

- Titre : « 🏛️ Exam 2024 · writing prepared: the doctor's advice ⭐⭐⭐ »
- Registre : id `C03#6` ; sources `C03#6`
- Sources (base en premier) : C03 (2024) ex. 6
- Items :
  - la tâche exacte (un courriel de 5 phrases à un cousin sur les conseils reçus) — QCM
  - les conseils pertinents pour rester en forme (multi, 3 justes sur 6)
  - conseil ou règle : should ou must pour chaque idée — 3 QCM
  - la formule d'ouverture et de clôture telles qu'imprimées (Dear …, / Yours, …) — QCM
  - l'ordre du plan (ordering, 4 étapes)
- Ne pas redemander : `02/quiz#2`, `02/03-revision#3`, `02/04-defi#2`, `02/04-defi#3`, `02/05-entrainement#2`
- Note : R3 du 9ᵉ : rien ne note la rédaction. La consigne « advised you to… » appelle un discours rapporté (HP) : la mission fait écrire les conseils au style direct (« You should… », « You mustn't… »), dit dans l'explication.

### Partie 2 — étiquetage des options existantes (objectif ≥ 60 %)

- 105 distracteurs, 0 étiqueté aujourd'hui → **au moins 63** à étiqueter. Les missions neuves s'étiquettent aussi, au même seuil.
- Étiquettes à employer (vocabulaire du lot A ; un distracteur qui ne dit aucune de ces erreurs reste muet) :
  - `english.health.etre-et-avoir-confondus` (neuf)
  - `english.modal.fonction-confondue` (existant)
  - `english.modal.s-sur-le-modal` (existant)
  - `english.modal.to-en-trop` (existant)
  - `english.quant.many-much-confondus` (neuf)
  - `english.sound.lettre-pour-son` (neuf)
  - `english.verb.base-verbale-deformee` (existant)
  - `english.vocab.mot-voisin-du-meme-champ` (neuf)
- `english.vocab.mot-voisin-du-meme-champ` seulement quand un indice de l'énoncé tranche (décision E7) ; jamais sur un distracteur absurde.
- Contrôle : `git diff --stat` après chaque fichier (un script qui réécrit le JSON gonfle le diff : ne changer que les `misconceptionTag`).

### Partie 3 — `coursePitfalls` et défauts `content:tranche`

- `coursePitfalls` proposés (chacun porté par au moins un distracteur du chapitre, C-5) : `english.modal.to-en-trop`, `english.modal.s-sur-le-modal`, `english.health.etre-et-avoir-confondus`, `english.quant.many-much-confondus`, `english.modal.fonction-confondue`
- **Clé strictement la plus longue** (5) — rallonger un distracteur ou resserrer la clé, sans changer la réponse : `02-keeping-fit/02-boss#1`, `02-keeping-fit/02-boss#6`, `02-keeping-fit/03-revision#2`, `02-keeping-fit/03-revision#4`, `02-keeping-fit/05-entrainement#1`
- **Paires proches** (1) — réécrire l'une des deux (autre contexte, autre geste) ou la déclarer exercice parallèle voulu au rapport :
  - 0.46 `02-keeping-fit/01-pratique#6` ↔ `02-keeping-fit/05-entrainement#4`
- **Gabarits inter-chapitres** (à l'auditeur ; l'auteur varie la consigne du sien) :
  - « three of these suggestions are correct which one is correct » : `02-keeping-fit/04-defi#1`
  - « read which sentence about is true » : `02-keeping-fit/02-boss#6`, `02-keeping-fit/05-entrainement#5`
  - « read which sentence about is completely correct » : `02-keeping-fit/04-defi#5`


## Rapport attendu

`FableEtudes/campagnes/anglais-6eme/rapports/rapport-B1.md`, écrit au fil de l'eau : fichiers créés et modifiés, ids neufs posés, part étiquetée par chapitre (avant / après), clé la plus longue et paires (avant / après), items écartés en cours d'écriture et pourquoi, doutes pour l'auditeur. Registre : missions `planifiee` → `en-ecriture` → `en-audit` (l'orchestrateur les passe).
