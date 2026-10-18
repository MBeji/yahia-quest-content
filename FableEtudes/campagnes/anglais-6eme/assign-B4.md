# Carte d'affectation B4 — anglais 6ᵉ, chapitres 07 (gisement + étiquettes + défauts)

> Lot auteur du passage unique (PLAN.md, lots B ; PLAN-gisement.md § 3). Un seul auteur sur ces chapitres. Skills : `content-ecole-tn` puis `content-langue-anglais` ; consignes `content-ingest/references/gisement-auteur-examen.md` (missions d'examen, avec la transcription de chaque session citée) et `gisement-auteur-devoir.md` (missions 📝 : la carte seule, jamais le devoir). Ne touche à aucun autre chapitre ; les autres lots écrivent en parallèle.

**Ordre de travail** : (1) les ids neufs et les libellés élargis que tu poses → `content/misconceptions.json` (textes exacts dans `vocab-english-6eme.json`) ; (2) partie 2 et partie 3 sur les fichiers existants ; (3) partie 1, les missions ; (4) `coursePitfalls` en dernier. Gates à chaque chapitre : `content:check`, `content:qa -- --subject english-6eme` (0 erreur), `content:tranche -- --subject english-6eme --changed --fresh --strict-longest`, rendu `renderLesson` si un cours est touché.


## Chapitre `07-around-the-world`

### Partie 1 — missions (gisement)

#### m018 → `exercices/06-exam-2025-reading-trip-to-tunisia.json` · d2 practice 75/15 · 6 questions · régime **examen**

- Titre : « 🏛️ Exam 2025 · reading: a trip to Tunisia ⭐⭐ »
- Registre : id `C02#1` ; sources `C02#1`
- Sources (base en premier) : C02 (2025) ex. 1
- Items :
  - Q1 remettre 4 événements en ordre (ordering)
  - Q2 un mot du paragraphe 1 (countries) et un du paragraphe 2 (won) — QCM
  - Q3 How did Annie know she was the winner? (e-mail) — QCM
- Ne pas redemander : `07/03-revision#2`

#### m019 → `exercices/07-exams-2013-2025-greetings-articles-directions.json` · d2 practice 75/15 · 6 questions · régime **examen**

- Titre : « 🏛️ Exams 2009–2025 · greetings, a and an, north and south ⭐⭐ »
- Registre : id `C14#5` ; sources `C14#5, C02#5, C09#5, C11#3, C12#2`
- Sources (base en premier) : C02 (2025) ex. 5 ; C14 (2013) ex. 5 ; C09 (2018) ex. 5 ; C11 (2016) ex. 3 ; C12 (2015) ex. 2
- Items :
  - 2025 W1 c : People around the world have different ways of greeting each other (ordering)
  - 2013 W1 : (a) old garage → an — QCM (english.article.a-an-selon-la-lettre)
  - 2018 W1 : in the (t n h r o) of England → north — short_answer
  - 2016 L2 : many new ≠ ___ houses (old) — QCM
  - 2015 L1 : I am on / of / from England — QCM
- Ne pas redemander : `07/quiz#1`, `07/quiz#2`, `07/quiz#4`, `07/01-pratique#1`, `07/01-pratique#3`, `07/03-revision#6`, `07/04-defi#1`, `07/05-entrainement#2`
- Note : Écartés : interested / interesting monuments (2026 L2, HP) ; right ≠ left (2015, 2019 : lexique hors guide, et il pousserait english.vocab.directions-confondues à l'envers).

#### m021 → `exercices/08-devoir-a-postcard-from-my-town.json` · d2 practice 75/15 · 6 questions · régime **devoir**

- Titre : « 📝 A postcard from my town ⭐⭐ »
- Registre : id `D07#7` ; sources `D07#7, D08#7`
- Cartes : devoir A (examen de 3ᵉ trimestre, école primaire), exercice 7 — carte anonyme ; devoir B (même créneau), exercice 7 — carte anonyme
- Items :
  - compléter une carte postale neuve par les éléments qui conviennent (lieu, direction sur la carte, monument, temps) — matching ; choisir la formule d'ouverture et de clôture — QCM ; repérer l'élément hors sujet — QCM ; écrire la réponse : quelles informations donner (multi)
- Ne pas redemander : `07/01-pratique#1`, `07/05-entrainement#1`
- Note : Salle blanche (D07 et D08 sont du même auteur : le plafond de deux est tenu, les deux cartes se fusionnent en une signature).

#### Hors gisement (D6) → `exercices/09-…` · d1 · 4 questions

- **Cours d'abord** : une section `## 🔊 Let's pronounce — …` au 07, au patron (ancrer, nommer, exemple, `verifie`, `retenir`) et sa puce au résumé : /s/ et /z/ du pluriel (books, cats, cups ¦ cars, bags, friends — fiche § 3.4, U-VII L2), /i/ et /ai/ du y final (sunny, family ¦ fly, sky — U-VII L4). Le 07 passe à 9 sections (au-delà de ~8 notions : décision D6 du pilote, acceptée).
- Puis « 🔊 Let's pronounce: the plural s and the letter y ⭐ » : 4 QCM d'écoute écrite (quel mot a le son…), étiquette `english.sound.lettre-pour-son` ; notation du guide `/i/`, `/ai/` (fiche § 3.4).

### Partie 2 — étiquetage des options existantes (objectif ≥ 60 %)

- 105 distracteurs, 0 étiqueté aujourd'hui → **au moins 63** à étiqueter. Les missions neuves s'étiquettent aussi, au même seuil.
- Étiquettes à employer (vocabulaire du lot A ; un distracteur qui ne dit aucune de ces erreurs reste muet) :
  - `english.article.a-an-selon-la-lettre` (neuf)
  - `english.comp.comparatif-et-superlatif-confondus` (existant)
  - `english.comp.double-marque` (existant)
  - `english.comp.forme-selon-longueur` (existant)
  - `english.comp.superlatif-sans-the` (existant)
  - `english.comp.that-au-lieu-de-than` (neuf)
  - `english.func.fonction-mal-identifiee` (existant)
  - `english.prep.travel-by-to-confondus` (neuf)
  - `english.sound.lettre-pour-son` (neuf)
  - `english.tense.continu-pour-habitude` (existant)
  - `english.verb.ing-oublie` (élargi)
  - `english.vocab.directions-confondues` (neuf)
  - `english.vocab.mot-voisin-du-meme-champ` (neuf)
- `english.vocab.mot-voisin-du-meme-champ` seulement quand un indice de l'énoncé tranche (décision E7) ; jamais sur un distracteur absurde.
- Contrôle : `git diff --stat` après chaque fichier (un script qui réécrit le JSON gonfle le diff : ne changer que les `misconceptionTag`).

### Partie 3 — `coursePitfalls` et défauts `content:tranche`

- `coursePitfalls` proposés (chacun porté par au moins un distracteur du chapitre, C-5) : `english.vocab.directions-confondues`, `english.verb.ing-oublie`, `english.article.a-an-selon-la-lettre`, `english.prep.travel-by-to-confondus`, `english.comp.forme-selon-longueur`, `english.comp.comparatif-et-superlatif-confondus`, `english.tense.continu-pour-habitude`
- **Clé strictement la plus longue** (5) — rallonger un distracteur ou resserrer la clé, sans changer la réponse : `07-around-the-world/02-boss#1`, `07-around-the-world/03-revision#2`, `07-around-the-world/03-revision#3`, `07-around-the-world/04-defi#2`, `07-around-the-world/05-entrainement#6`
- **Paires proches** (8) — réécrire l'une des deux (autre contexte, autre geste) ou la déclarer exercice parallèle voulu au rapport :
  - 0.68 `07-around-the-world/04-defi#4` ↔ `07-around-the-world/05-entrainement#4`
  - 0.58 `07-around-the-world/01-pratique#1` ↔ `07-around-the-world/05-entrainement#1`
  - 0.52 `07-around-the-world/quiz#2` ↔ `07-around-the-world/01-pratique#3`
  - 0.50 `07-around-the-world/02-boss#4` ↔ `07-around-the-world/05-entrainement#3`
  - 0.48 `07-around-the-world/quiz#5` ↔ `07-around-the-world/04-defi#4`
  - 0.47 `07-around-the-world/quiz#1` ↔ `07-around-the-world/05-entrainement#1`
  - 0.47 `07-around-the-world/quiz#3` ↔ `07-around-the-world/01-pratique#2`
  - 0.45 `07-around-the-world/quiz#1` ↔ `07-around-the-world/01-pratique#1`
- **Gabarits inter-chapitres** (à l'auditeur ; l'auteur varie la consigne du sien) :
  - « three of these suggestions are correct which one is correct » : `07-around-the-world/02-boss#1`, `07-around-the-world/04-defi#1`


## Rapport attendu

`FableEtudes/campagnes/anglais-6eme/rapports/rapport-B4.md`, écrit au fil de l'eau : fichiers créés et modifiés, ids neufs posés, part étiquetée par chapitre (avant / après), clé la plus longue et paires (avant / après), items écartés en cours d'écriture et pourquoi, doutes pour l'auditeur. Registre : missions `planifiee` → `en-ecriture` → `en-audit` (l'orchestrateur les passe).
