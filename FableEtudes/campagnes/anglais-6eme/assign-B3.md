# Carte d'affectation B3 — anglais 6ᵉ, chapitres 05, 06 (gisement + étiquettes + défauts)

> Lot auteur du passage unique (PLAN.md, lots B ; PLAN-gisement.md § 3). Un seul auteur sur ces chapitres. Skills : `content-ecole-tn` puis `content-langue-anglais` ; consignes `content-ingest/references/gisement-auteur-examen.md` (missions d'examen, avec la transcription de chaque session citée) et `gisement-auteur-devoir.md` (missions 📝 : la carte seule, jamais le devoir). Ne touche à aucun autre chapitre ; les autres lots écrivent en parallèle.

**Ordre de travail** : (1) les ids neufs et les libellés élargis que tu poses → `content/misconceptions.json` (textes exacts dans `vocab-english-6eme.json`) ; (2) partie 2 et partie 3 sur les fichiers existants ; (3) partie 1, les missions ; (4) `coursePitfalls` en dernier. Gates à chaque chapitre : `content:check`, `content:qa -- --subject english-6eme` (0 erreur), `content:tranche -- --subject english-6eme --changed --fresh --strict-longest`, rendu `renderLesson` si un cours est touché.


## Chapitre `05-celebrations`

### Partie 1 — missions (gisement)

#### m012 → `exercices/06-exams-2023-2026-simple-past.json` · d3 boss 120/30 · 11 questions · régime **examen**

- Titre : « 🏛️ Exams 2023–2026 · the simple past: regular and irregular ⭐⭐⭐ »
- Registre : id `C01#4` ; sources `C01#4, C01#3, C02#3, C03#3, C03#4, C04#3, C02#5, C02#2`
- Sources (base en premier) : C01 (2026) ex. 4 ; C01 (2026) ex. 3 ; C02 (2025) ex. 3 ; C03 (2024) ex. 3 ; C03 (2024) ex. 4 ; C04 (2023) ex. 3 ; C02 (2025) ex. 5 ; C02 (2025) ex. 2
- Items :
  - 2026 L3 : I [find] ___ a nice winter coat (found) — short_answer
  - 2026 L2 : they choose / will choose / chose — QCM
  - 2025 L2 : [drink] ___ (drank) ; My friends [prefer] ___ (preferred) — short_answer + QCM
  - 2024 L2 : Students sings / sing / sang — QCM
  - 2024 L3 : he [take] ___ it (took) ; The bag owner [thank] ___ him (thanked) — deux QCM
  - 2023 L2 : Yesterday, my sister (write) ___ (wrote) — QCM
  - 2025 W1 d : Two weeks ago, … prepared a surprise party (ordering)
  - 2025 L1 : giving every child the ___ to feel loved (right) — QCM (have the right to, U-V L1)
- Ne pas redemander : `05/quiz#2`, `05/quiz#3`, `05/01-pratique#4`, `05/01-pratique#5`, `05/01-pratique#6`, `05/02-boss#4`, `05/03-revision#3`, `05/04-defi#1`, `05/05-entrainement#3`, `05/05-entrainement#5`
- Note : Écartés : [two] → twice, [friend] → friendly (2026), (invite) → invitation (2023) : HP:word-formation ; interested / interesting (2026 L2) : HP:ed-ing-adjectives.

#### m013 → `exercices/07-exam-2021-reading-end-of-year-party.json` · d2 practice 75/15 · 6 questions · régime **examen**

- Titre : « 🏛️ Exam 2021 · reading: the end-of-year party ⭐⭐ »
- Registre : id `C06#1` ; sources `C06#1`
- Sources (base en premier) : C06 (2021) ex. 1
- Items :
  - Q1 et Q2 de la session (3 + 3 points) converties : vrai/faux justifié, complétion par des mots du texte — 5 à 6 QCM
- Ne pas redemander : rien d'équivalent dans le chapitre
- Note : Session 2021 (programme ancien) : thème des fêtes de fin d'année (U-V L5) ; la coquille Mr Jack / Mr John n'entre pas dans une option.

#### m014 → `exercices/08-exam-2021-writing-birthday-party.json` · d2 practice 75/15 · 6 questions · régime **examen**

- Titre : « 🏛️ Exam 2021 · writing prepared: a family birthday party ⭐⭐ »
- Registre : id `C06#6` ; sources `C06#6`
- Sources (base en premier) : C06 (2021) ex. 6
- Items :
  - la tâche (courriel à une amie anglaise : vêtements, nourriture, activités, cadeaux) — QCM
  - les idées qui répondent à chaque rubrique (matching rubrique ↔ phrase)
  - les cadeaux et les mots de fête de l'unité (multi)
  - formule d'ouverture et de clôture — QCM
- Ne pas redemander : `05/03-revision#1`, `05/05-entrainement#1`
- Note : La consigne est au présent continu (You are having…) : la mission fait écrire au présent simple ou au passé, sans exiger le continu (HP).

### Partie 2 — étiquetage des options existantes (objectif ≥ 60 %)

- 105 distracteurs, 0 étiqueté aujourd'hui → **au moins 63** à étiqueter. Les missions neuves s'étiquettent aussi, au même seuil.
- Étiquettes à employer (vocabulaire du lot A ; un distracteur qui ne dit aucune de ces erreurs reste muet) :
  - `english.sound.ed-toujours-syllabe` (neuf)
  - `english.spell.suffixe-sans-regle-orthographique` (élargi)
  - `english.tense.ed-sur-verbe-irregulier` (existant)
  - `english.tense.present-avec-marqueur-passe` (existant)
  - `english.verb.auxiliaire-mal-accorde` (élargi)
  - `english.verb.be-avec-base-verbale` (existant)
  - `english.verb.s-oublie-3e-personne` (existant)
  - `english.verb.temps-marque-deux-fois` (élargi)
  - `english.vocab.mot-de-sens-inverse` (neuf)
  - `english.vocab.mot-voisin-du-meme-champ` (neuf)
- `english.vocab.mot-voisin-du-meme-champ` seulement quand un indice de l'énoncé tranche (décision E7) ; jamais sur un distracteur absurde.
- Contrôle : `git diff --stat` après chaque fichier (un script qui réécrit le JSON gonfle le diff : ne changer que les `misconceptionTag`).

### Partie 3 — `coursePitfalls` et défauts `content:tranche`

- `coursePitfalls` proposés (chacun porté par au moins un distracteur du chapitre, C-5) : `english.verb.auxiliaire-mal-accorde`, `english.verb.temps-marque-deux-fois`, `english.tense.ed-sur-verbe-irregulier`, `english.tense.present-avec-marqueur-passe`, `english.sound.ed-toujours-syllabe`
- **Clé strictement la plus longue** (3) — rallonger un distracteur ou resserrer la clé, sans changer la réponse : `05-celebrations/quiz#3`, `05-celebrations/01-pratique#1`, `05-celebrations/03-revision#2`
- **Paires proches** (7) — réécrire l'une des deux (autre contexte, autre geste) ou la déclarer exercice parallèle voulu au rapport :
  - 0.64 `05-celebrations/quiz#1` ↔ `05-celebrations/01-pratique#3`
  - 0.56 `05-celebrations/quiz#5` ↔ `05-celebrations/03-revision#6`
  - 0.54 `05-celebrations/04-defi#4` ↔ `05-celebrations/05-entrainement#6`
  - 0.53 `05-celebrations/01-pratique#3` ↔ `05-celebrations/05-entrainement#2`
  - 0.50 `05-celebrations/quiz#1` ↔ `05-celebrations/02-boss#2`
  - 0.48 `05-celebrations/03-revision#6` ↔ `05-celebrations/05-entrainement#6`
  - 0.45 `05-celebrations/quiz#3` ↔ `06-going-shopping/quiz#5`


## Chapitre `06-going-shopping`

### Partie 1 — missions (gisement)

#### m015 → `exercices/06-exams-2010-2025-at-the-shop.json` · d2 practice 75/15 · 9 questions · régime **examen**

- Titre : « 🏛️ Exams 2010–2025 · at the shop: Can I help you?, I'd like, How much is it? ⭐⭐ »
- Registre : id `C03#5` ; sources `C03#5, C09#4, C17#5, C15#4, C02#4, C06#3`
- Sources (base en premier) : C03 (2024) ex. 5 ; C09 (2018) ex. 4 ; C17 (2010) ex. 5 ; C15 (2012) ex. 4 ; C02 (2025) ex. 4 ; C06 (2021) ex. 3
- Items :
  - 2024 W1 : dialogue de librairie (matching des 4 cercles, une option en trop)
  - 2018 L3 : Can I … / I'd like a kilo of … / How much … (matching)
  - 2010 W1 : dialogue de magasin, 3 blancs (QCM par blanc)
  - 2012 L3 : You can buy postcards at the bookshop ; It's between the bank and the station (matching)
  - 2025 L3 : put on = ___ (wear) — QCM
  - 2021 L2 : a computer in / on / at the teacher's desk — QCM
- Ne pas redemander : `06/quiz#2`, `06/quiz#3`, `06/01-pratique#3`, `06/01-pratique#4`, `06/02-boss#5`, `06/02-boss#6`, `06/03-revision#5`, `06/05-entrainement#4`

#### m016 → `exercices/07-exam-2024-reading-lost-at-the-mall.json` · d2 practice 75/15 · 7 questions · régime **examen**

- Titre : « 🏛️ Exam 2024 · reading: lost at the mall ⭐⭐ »
- Registre : id `C03#1` ; sources `C03#1`
- Sources (base en premier) : C03 (2024) ex. 1
- Items :
  - Q1 Tick : by car — QCM
  - Q2 vrai/faux ×2 → QCM + preuve
  - Q3 deux mots du paragraphe 3 — QCM
  - Q4 Why did Alex leave the clothes shop? → QCM de la raison
- Ne pas redemander : rien d'équivalent dans le chapitre

#### m017 → `exercices/08-exam-2025-writing-shopping-day.json` · d3 boss 120/30 · 8 questions · régime **examen**

- Titre : « 🏛️ Exam 2025 · writing prepared: a shopping day at the mall ⭐⭐⭐ »
- Registre : id `C02#6` ; sources `C02#6`
- Sources (base en premier) : C02 (2025) ex. 6
- Items :
  - la tâche (5 à 7 phrases au passé : magasins visités, achats) — QCM
  - magasin ↔ article acheté (matching)
  - les phrases au passé correctes (multi : bought, went, tried on…)
  - l'ordre du récit (ordering)
- Ne pas redemander : `06/quiz#5`, `06/04-defi#3`, `06/05-entrainement#5`, `06/05-entrainement#6`

### Partie 2 — étiquetage des options existantes (objectif ≥ 60 %)

- 105 distracteurs, 0 étiqueté aujourd'hui → **au moins 63** à étiqueter. Les missions neuves s'étiquettent aussi, au même seuil.
- Étiquettes à employer (vocabulaire du lot A ; un distracteur qui ne dit aucune de ces erreurs reste muet) :
  - `english.func.demande-et-offre-confondues` (existant)
  - `english.func.like-au-lieu-de-would-like` (neuf)
  - `english.modal.to-oublie` (élargi)
  - `english.num.centaines-mal-ecrites` (neuf)
  - `english.quant.many-much-confondus` (neuf)
  - `english.question.auxiliaire-ou-ordre-oublie` (élargi)
  - `english.question.mot-interrogatif-inadapte` (existant)
  - `english.sound.lettre-pour-son` (neuf)
  - `english.spell.suffixe-sans-regle-orthographique` (élargi)
  - `english.tense.ed-sur-verbe-irregulier` (existant)
  - `english.tense.present-avec-marqueur-passe` (existant)
  - `english.tense.verbe-d-etat-au-continu` (existant)
  - `english.vocab.mot-de-sens-inverse` (neuf)
  - `english.vocab.mot-voisin-du-meme-champ` (neuf)
- `english.vocab.mot-voisin-du-meme-champ` seulement quand un indice de l'énoncé tranche (décision E7) ; jamais sur un distracteur absurde.
- Contrôle : `git diff --stat` après chaque fichier (un script qui réécrit le JSON gonfle le diff : ne changer que les `misconceptionTag`).

### Partie 3 — `coursePitfalls` et défauts `content:tranche`

- `coursePitfalls` proposés (chacun porté par au moins un distracteur du chapitre, C-5) : `english.vocab.mot-de-sens-inverse`, `english.func.like-au-lieu-de-would-like`, `english.question.auxiliaire-ou-ordre-oublie`, `english.num.centaines-mal-ecrites`, `english.tense.ed-sur-verbe-irregulier`, `english.sound.lettre-pour-son`
- **Clé strictement la plus longue** (9) — rallonger un distracteur ou resserrer la clé, sans changer la réponse : `06-going-shopping/quiz#2`, `06-going-shopping/quiz#5`, `06-going-shopping/01-pratique#2`, `06-going-shopping/01-pratique#3`, `06-going-shopping/02-boss#5`, `06-going-shopping/03-revision#1`, `06-going-shopping/03-revision#2`, `06-going-shopping/03-revision#3`, `06-going-shopping/05-entrainement#6`
- **Paires proches** (2) — réécrire l'une des deux (autre contexte, autre geste) ou la déclarer exercice parallèle voulu au rapport :
  - 0.46 `06-going-shopping/quiz#1` ↔ `06-going-shopping/01-pratique#1`
  - 0.45 `05-celebrations/quiz#3` ↔ `06-going-shopping/quiz#5`
- **Gabarits inter-chapitres** (à l'auditeur ; l'auteur varie la consigne du sien) :
  - « three of these suggestions are correct which one is correct » : `06-going-shopping/04-defi#1`


## Rapport attendu

`FableEtudes/campagnes/anglais-6eme/rapports/rapport-B3.md`, écrit au fil de l'eau : fichiers créés et modifiés, ids neufs posés, part étiquetée par chapitre (avant / après), clé la plus longue et paires (avant / après), items écartés en cours d'écriture et pourquoi, doutes pour l'auditeur. Registre : missions `planifiee` → `en-ecriture` → `en-audit` (l'orchestrateur les passe).
