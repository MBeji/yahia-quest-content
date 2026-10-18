# Carte d'affectation B2 — anglais 6ᵉ, chapitres 03, 04 (gisement + étiquettes + défauts)

> Lot auteur du passage unique (PLAN.md, lots B ; PLAN-gisement.md § 3). Un seul auteur sur ces chapitres. Skills : `content-ecole-tn` puis `content-langue-anglais` ; consignes `content-ingest/references/gisement-auteur-examen.md` (missions d'examen, avec la transcription de chaque session citée) et `gisement-auteur-devoir.md` (missions 📝 : la carte seule, jamais le devoir). Ne touche à aucun autre chapitre ; les autres lots écrivent en parallèle.

**Ordre de travail** : (1) les ids neufs et les libellés élargis que tu poses → `content/misconceptions.json` (textes exacts dans `vocab-english-6eme.json`) ; (2) partie 2 et partie 3 sur les fichiers existants ; (3) partie 1, les missions ; (4) `coursePitfalls` en dernier. Gates à chaque chapitre : `content:check`, `content:qa -- --subject english-6eme` (0 erreur), `content:tranche -- --subject english-6eme --changed --fresh --strict-longest`, rendu `renderLesson` si un cours est touché.


## Chapitre `03-having-fun-in-the-seasons`

### Partie 1 — missions (gisement)

#### m007 → `exercices/06-exams-2008-2026-weather-seasons-will.json` · d2 practice 75/15 · 9 questions · régime **examen**

- Titre : « 🏛️ Exams 2008–2026 · weather words, seasons and will ⭐⭐ »
- Registre : id `C01#2` ; sources `C01#2, C02#4, C04#3, C04#4, C17#3, C09#5, C19#4, C08#3`
- Sources (base en premier) : C01 (2026) ex. 2 ; C02 (2025) ex. 4 ; C04 (2023) ex. 3 ; C04 (2023) ex. 4 ; C17 (2010) ex. 3 ; C09 (2018) ex. 5 ; C19 (2008) ex. 4 ; C08 (2019) ex. 3
- Items :
  - 2026 L1 blanc 1 : the air was ___ (warm) — QCM
  - 2025 L3 : The sky is clear ≠ ___ (cloudy) — QCM
  - 2023 L2 : Tomorrow … We (have) ___ a big party (will have) — QCM
  - 2023 L3 : playing outside ≠ ___ (inside) — QCM
  - 2010 L2 : The weather is sunny / funny ; in the beach / sea — deux QCM
  - 2018 W1 : cold and (a y r i n) → rainy — short_answer (acceptedAnswers : rainy)
  - 2008 L3 : It's winter. It's ___ (rainy ; l'image du nuage de pluie est décrite en mots) — QCM
  - 2019 L2 : It's very cold ≠ ___ (hot) — QCM
- Ne pas redemander : `03/quiz#2`, `03/quiz#3`, `03/quiz#4`, `03/01-pratique#2`, `03/01-pratique#4`, `03/02-boss#1`, `03/02-boss#2`, `03/03-revision#3`, `03/03-revision#4`, `03/05-entrainement#3`, `03/05-entrainement#4`
- Note : Écartés : swings, sliding (2026, lexique de parc hors guide), the most (HP:the-most), will choose / chose (2026 L2 → m012, passé).

#### m008 → `exercices/07-exam-2022-writing-winter-holiday.json` · d3 boss 120/30 · 7 questions · régime **examen**

- Titre : « 🏛️ Exam 2022 · writing prepared: my winter holiday ⭐⭐⭐ »
- Registre : id `C05#6` ; sources `C05#6`
- Sources (base en premier) : C05 (2022) ex. 6
- Items :
  - la tâche (un courriel à un ami sur les vacances d'hiver : lieu, vêtements, nourriture, activités) — QCM
  - les vêtements d'hiver qui conviennent (multi)
  - le temps qu'il fait en hiver : It's + adjectif en -y (QCM)
  - les activités d'hiver nommées par Verb + ing (QCM)
  - l'ordre du courriel (ordering) et sa formule de clôture (QCM)
- Ne pas redemander : `03/03-revision#2`, `03/04-defi#5`, `03/05-entrainement#5`
- Note : Session 2022 (programme ancien) gardée : chaque contenu imposé est dans l'unité III (saisons, vêtements de saison, Verb + ing).

#### m020 → `exercices/08-devoir-a-seasons-letter.json` · d2 practice 75/15 · 6 questions · régime **devoir**

- Titre : « 📝 A seasons letter: read and check ⭐⭐ »
- Registre : id `D09#1` ; sources `D09#1`
- Cartes : devoir D (contrôle de 3ᵉ trimestre, école primaire), exercice 1 — carte anonyme
- Items :
  - lire une lettre de vacances neuve (écrite par l'auteur) sur une saison : cocher, puis corriger des affirmations fausses par le détail juste (saison, temps, vêtements, activités en Verb + ing) — 6 QCM
- Ne pas redemander : `03/quiz#1`, `03/03-revision#2`
- Note : Salle blanche : la carte ne donne que le geste ; texte, noms, lieux et nombres neufs.

### Partie 2 — étiquetage des options existantes (objectif ≥ 60 %)

- 105 distracteurs, 0 étiqueté aujourd'hui → **au moins 63** à étiqueter. Les missions neuves s'étiquettent aussi, au même seuil.
- Étiquettes à employer (vocabulaire du lot A ; un distracteur qui ne dit aucune de ces erreurs reste muet) :
  - `english.comp.double-marque` (existant)
  - `english.comp.forme-selon-longueur` (existant)
  - `english.comp.that-au-lieu-de-than` (neuf)
  - `english.modal.s-sur-le-modal` (existant)
  - `english.modal.to-en-trop` (existant)
  - `english.question.mot-interrogatif-inadapte` (existant)
  - `english.sound.lettre-pour-son` (neuf)
  - `english.spell.suffixe-sans-regle-orthographique` (élargi)
  - `english.verb.base-verbale-deformee` (existant)
  - `english.verb.be-avec-base-verbale` (existant)
  - `english.verb.ing-oublie` (élargi)
  - `english.vocab.mot-voisin-du-meme-champ` (neuf)
  - `english.word.nom-au-lieu-de-l-adjectif` (neuf)
- `english.vocab.mot-voisin-du-meme-champ` seulement quand un indice de l'énoncé tranche (décision E7) ; jamais sur un distracteur absurde.
- Contrôle : `git diff --stat` après chaque fichier (un script qui réécrit le JSON gonfle le diff : ne changer que les `misconceptionTag`).

### Partie 3 — `coursePitfalls` et défauts `content:tranche`

- `coursePitfalls` proposés (chacun porté par au moins un distracteur du chapitre, C-5) : `english.word.nom-au-lieu-de-l-adjectif`, `english.verb.base-verbale-deformee`, `english.comp.forme-selon-longueur`, `english.comp.that-au-lieu-de-than`, `english.spell.suffixe-sans-regle-orthographique`
- **Clé strictement la plus longue** (4) — rallonger un distracteur ou resserrer la clé, sans changer la réponse : `03-having-fun-in-the-seasons/quiz#3`, `03-having-fun-in-the-seasons/01-pratique#6`, `03-having-fun-in-the-seasons/05-entrainement#1`, `03-having-fun-in-the-seasons/05-entrainement#6`
- **Paires proches** (1) — réécrire l'une des deux (autre contexte, autre geste) ou la déclarer exercice parallèle voulu au rapport :
  - 0.47 `03-having-fun-in-the-seasons/01-pratique#1` ↔ `03-having-fun-in-the-seasons/03-revision#1`
- **Gabarits inter-chapitres** (à l'auditeur ; l'auteur varie la consigne du sien) :
  - « three of these suggestions are correct which one is correct » : `03-having-fun-in-the-seasons/04-defi#1`
  - « read which sentence about is completely correct » : `03-having-fun-in-the-seasons/05-entrainement#5`


## Chapitre `04-caring`

### Partie 1 — missions (gisement)

#### m009 → `exercices/06-exams-2023-2025-superlative-and-jobs.json` · d2 practice 75/15 · 6 questions · régime **examen**

- Titre : « 🏛️ Exams 2023–2025 · the cleanest, the coldest — and the people who help ⭐⭐ »
- Registre : id `C03#2` ; sources `C03#2, C04#4, C03#4, C02#3, C02#2`
- Sources (base en premier) : C03 (2024) ex. 2 ; C04 (2023) ex. 4 ; C03 (2024) ex. 4 ; C02 (2025) ex. 3 ; C02 (2025) ex. 2
- Items :
  - 2024 L1 : We ___ rubbish (collect) ; the ___ one in the city (cleanest, piège cleaner) — deux QCM
  - 2023 L3 : Summer is the hottest one ≠ Winter is the ___ one (coldest) — QCM
  - 2024 L3 : he works as a [wait] ___ (waiter) — QCM
  - 2025 L2 : She is a good [cook] ___ (cook ; distracteur cooker → english.word.nom-d-agent-force) — QCM
  - 2025 L1 : to feel loved and ___ for (cared) — QCM
- Ne pas redemander : `04/quiz#3`, `04/quiz#4`, `04/02-boss#1`, `04/02-boss#3`, `04/02-boss#4`, `04/03-revision#2`, `04/03-revision#4`, `04/04-defi#1`, `04/04-defi#3`, `04/05-entrainement#3`, `04/05-entrainement#5`
- Note : Écarté : the most (2026 L1, HP:the-most).

#### m010 → `exercices/07-exam-2026-reading-world-caring-day.json` · d2 practice 75/15 · 7 questions · régime **examen**

- Titre : « 🏛️ Exam 2026 · reading: World Caring Day ⭐⭐ »
- Registre : id `C01#1` ; sources `C01#1`
- Sources (base en premier) : C01 (2026) ex. 1
- Items :
  - Q1 vrai/faux ×2 (dont « all the students bought presents ») → QCM + phrase qui prouve
  - Q2 un mot du paragraphe 1 et un du paragraphe 3 — QCM
  - Q3 référent de « they » — QCM (english.read.referent-le-plus-proche)
  - Q4 synonyme de very happy (thrilled) — QCM (english.read.sens-du-mot-sans-contexte)
- Ne pas redemander : rien d'équivalent dans le chapitre
- Note : Texte résumé ; la citation « she looked thrilled and said… » est celle de la transcription.

#### m011 → `exercices/08-exams-2023-2026-writing-caring.json` · d3 boss 120/30 · 9 questions · régime **examen**

- Titre : « 🏛️ Exams 2023, 2026 · writing prepared: helping at home, caring for a pet ⭐⭐⭐ »
- Registre : id `C01#6` ; sources `C01#6, C04#6`
- Sources (base en premier) : C01 (2026) ex. 6 ; C04 (2023) ex. 6
- Items :
  - 2026 W2 : la tâche (paragraphe de 6 à 8 phrases au passé : le temps, le chat, au moins 4 soins) — QCM ; les soins qui conviennent à un animal (multi) ; le temps du récit (QCM, passé) ; l'ordre (ordering)
  - 2023 W2 : qui fait quelle tâche ménagère (matching) ; la tâche exacte (4 idées, présent) — QCM
- Ne pas redemander : `04/quiz#5`, `04/01-pratique#1`, `04/01-pratique#6`, `04/02-boss#6`, `04/03-revision#5`, `04/05-entrainement#6`
- Note : Placement D2 : thème « prendre soin d'un animal » (U-IV L5) et « tâches partagées » (U-IV L1) → 04 ; le passé du récit est seulement nommé.

### Partie 2 — étiquetage des options existantes (objectif ≥ 60 %)

- 105 distracteurs, 0 étiqueté aujourd'hui → **au moins 63** à étiqueter. Les missions neuves s'étiquettent aussi, au même seuil.
- Étiquettes à employer (vocabulaire du lot A ; un distracteur qui ne dit aucune de ces erreurs reste muet) :
  - `english.comp.comparatif-et-superlatif-confondus` (existant)
  - `english.comp.superlatif-sans-the` (existant)
  - `english.modal.to-en-trop` (existant)
  - `english.pron.possessif-du-mauvais-possesseur` (neuf)
  - `english.pron.sujet-au-lieu-du-possessif` (neuf)
  - `english.sound.lettre-pour-son` (neuf)
  - `english.verb.base-verbale-deformee` (existant)
  - `english.verb.imperatif-mal-forme` (neuf)
  - `english.vocab.mot-de-sens-inverse` (neuf)
  - `english.vocab.mot-voisin-du-meme-champ` (neuf)
  - `english.word.nom-d-agent-force` (neuf)
- `english.vocab.mot-voisin-du-meme-champ` seulement quand un indice de l'énoncé tranche (décision E7) ; jamais sur un distracteur absurde.
- Contrôle : `git diff --stat` après chaque fichier (un script qui réécrit le JSON gonfle le diff : ne changer que les `misconceptionTag`).

### Partie 3 — `coursePitfalls` et défauts `content:tranche`

- `coursePitfalls` proposés (chacun porté par au moins un distracteur du chapitre, C-5) : `english.pron.sujet-au-lieu-du-possessif`, `english.comp.comparatif-et-superlatif-confondus`, `english.word.nom-d-agent-force`, `english.verb.base-verbale-deformee`, `english.verb.imperatif-mal-forme`, `english.sound.lettre-pour-son`
- **Clé strictement la plus longue** (8) — rallonger un distracteur ou resserrer la clé, sans changer la réponse : `04-caring/quiz#3`, `04-caring/02-boss#1`, `04-caring/02-boss#3`, `04-caring/03-revision#2`, `04-caring/03-revision#3`, `04-caring/04-defi#1`, `04-caring/04-defi#2`, `04-caring/04-defi#4`
- **Paires proches** (2) — réécrire l'une des deux (autre contexte, autre geste) ou la déclarer exercice parallèle voulu au rapport :
  - 0.64 `04-caring/quiz#4` ↔ `04-caring/04-defi#1`
  - 0.57 `04-caring/02-boss#6` ↔ `04-caring/05-entrainement#6`


## Rapport attendu

`FableEtudes/campagnes/anglais-6eme/rapports/rapport-B2.md`, écrit au fil de l'eau : fichiers créés et modifiés, ids neufs posés, part étiquetée par chapitre (avant / après), clé la plus longue et paires (avant / après), items écartés en cours d'écriture et pourquoi, doutes pour l'auditeur. Registre : missions `planifiee` → `en-ecriture` → `en-audit` (l'orchestrateur les passe).
