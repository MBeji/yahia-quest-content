# Gisement 6ᵉ × français : plan des missions d'examen et de devoirs (G3–G4, étude 36) — v1

Écrit le 2026-10-19 par le planificateur (lot D2 de [`PLAN.md`](./PLAN.md)). Entrées : les 17 sujets lus (`C01`–`C19`, sans `C13` 2014 et `C16` 2011, introuvables), leurs transcriptions (`content/programmes-officiels/examens-nationaux/6eme-base/french/`), les 185 lignes d'examen et les 53 lignes de devoirs (`lecture-gisement/lines/`), les trois journaux de lecture et `signatures-devoirs.tsv`, les 288 questions de `content/french-6eme/` (8 chapitres × 36), et les décisions F1–F9 de `PLAN.md`. Modèle : le plan de l'anglais 6ᵉ (`FableEtudes/campagnes/anglais-6eme/PLAN-gisement.md`).

Sorties :

- carte et écart : `content/programmes-officiels/sources-externes/web-6eme-base-french/fiche.md` § 3 ;
- plan machine : [`plan-missions-v1.json`](./plan-missions-v1.json) — 33 missions (`m001`–`m033`), les écartés, la mesure des devoirs, les décisions à soumettre ;
- registre : `…/web-6eme-base-french/gisement.json` — 33 missions `planifiee` (id = la source de base, `sources` = toutes les sources fusionnées, `note` = l'id du plan) ; `D06` en `ecarte` ;
- cartes d'affectation = lots d'auteurs : [`assign-M1.md`](./assign-M1.md) (01, 02), [`assign-M2.md`](./assign-M2.md) (03, 04), [`assign-M3.md`](./assign-M3.md) (05, 06), [`assign-M4.md`](./assign-M4.md) (07, 08).

Les étages des 238 lignes sont ceux des lecteurs (échelle du portail, aucun `d4`) ; rien n'a été harmonisé en amont : les conventions des deux journaux d'examens sont déjà communes.

## 1. Règles retenues (adaptées du plan de l'anglais 6ᵉ et des décisions du pilote)

**R1 — Langue : une mission par famille et par chapitre, sessions fusionnées, au grain de l'item.** Un item est une sous-question de grammaire ou de conjugaison. Il devient un QCM de formes (« quelle réécriture est correcte ? »), un matching (tableau de fonctions) ou un ordering ; **la question dit sa session** (« Concours 2023 ») et **redonne la phrase officielle** de la transcription avec sa consigne. Chapitre = la notion visée (F4) ; un tableau ou un exercice qui cumule les chapitres 05 à 08 va au plus avancé. La forme d'un verbe d'un chapitre ultérieur est donnée dans les options quand elle n'est pas la cible. Un blanc `HP:` du même exercice (tout, -if/-ive, imparfait, pronom complément) est **donné rempli**, jamais demandé. Base : la session la plus récente. Deux familles minces (moins de cinq questions) d'un même chapitre sont fusionnées (m009, m025).

**R2 — Compréhension : une mission par texte, au plus cinq textes récents et représentatifs.** 2026 (défi sans écrans → `02`), 2024 (phoque → `05`), 2023 (handicap et opération → `06`), 2022 (club de théâtre → `07`), 2025 (site maya → `08`). Une ou deux phrases officielles par question, prises dans le PDF officiel (`/tmp/claude-0/fr6g/src/<année>-francais.pdf`, sha256 au registre), jamais le texte entier. **Questions ouvertes converties en fermées** : « relève deux détails » → QCM du détail, puis multi ; « justifie » → la réponse puis la phrase qui la prouve ; « synonyme / contraire » → un QCM par mot, le leurre est un mot de nature différente (c'est le piège de presque toutes les lignes de lexique) ; « donne ton avis / imagine » → QCM de l'argument qui s'appuie sur le texte. Les questions suivent l'ordre imprimé. Le texte de 2021 est écarté (E1).

**R3 — Production : préparation fermée, regroupée par archétype.** Six missions `d3` (une par archétype), qui redonnent chacune la **situation et la consigne officielles** de leur session et ne demandent que ce qui se décide **avant** d'écrire : les éléments exigés (multi : au moins huit phrases, un dialogue, la réaction décrite…), l'ordre du récit (ordering des cinq temps), la ponctuation du dialogue et le verbe introducteur (QCM), un passage descriptif (QCM), une première réplique, une phrase de fin. Archétypes : dispute à propos des écrans (`02`), faire accepter un camarade (`03`), s'entraider du début à la fin (`04`), émotions et lieu décrits (`05`), réactions et gardien (`06`), suite ou réalisation d'une scène (`07`). Les dix-sept consignes de rédaction (une par session) sont toutes reprises.

**R4 — Rien de ce que le patron pose déjà.** Croisement question par question contre les 288 questions ; chaque mission nomme celles à ne pas redemander (`neDemandePas`). Le patron est écrit en phrases de l'auteur, au niveau de la fiche ; ce qui lui manque partout est la phrase officielle, la réécriture sous consigne, le tableau de fonctions à quatre colonnes, la lecture d'un texte, la consigne de rédaction.

**R5 — Placement (F4).** Langue : chapitre de la notion (R1). Lecture : chapitre du thème du texte. Production : chapitre de l'**archétype**, la consigne officielle redonnée portant le thème ; deux écarts au thème, déclarés (E5) : C02#11 (thème 08, rangée au `06`) et C19#10 (thème 02, rangée au `07`).

**R6 — Types natifs.** `ordering` (ordre des événements, des répliques, des étapes), `matching` (tableaux de fonctions, personnage ↔ énoncé), `multi` (relevés, éléments exigés), `short_answer` seulement pour une forme unique avec ses `acceptedAnswers`. Une réécriture libre ne se corrige pas : elle devient un QCM de réécritures.

**R7 — Taille, étage, en-tête.** 12 questions au plus ; étage = celui de la ligne la plus haute ENTIÈREMENT reprise (une ligne `d3` dont on ne reprend qu'une réponse compte `d2`, E2), jamais `d1`, `d3` au plus ; en-tête `d2` practice 75 / 15, `d3` boss 120 / 30 (consigne `gisement-auteur-examen.md`). Bilan : 25 `d2`, 8 `d3`. Fichiers : `NN` à la suite de `05-entrainement`, les missions d'examen d'abord (`06-exams-…`), puis les devoirs (`NN-devoir-<slug>.json`). Titre : « 🏛️ Concours <années> · <sujet> » puis les étoiles de l'étage ; « 📝 <sujet> » pour un devoir. `chapter.json` : une ligne ajoutée à `sources[]` (voir les cartes).

**R8 — Étiquettes.** Le vocabulaire `fr.*` du lot A (`vocab-french-6eme.json`, 43 ids neufs, 9 élargis, déjà dans `content/misconceptions.json`). Le « piège » de chaque ligne (colonne 9 du lecteur) est repris dans la carte : l'auteur le fait porter par un distracteur étiqueté, jamais sur un multi, un ordering ni un matching.

**R9 — Devoirs, salle blanche (T2′).** Une mission par signature distincte au niveau gabarit, **sur des gestes absents des examens** : appariement, remise en ordre, titre, nature des mots, son/sont, correction d'erreurs, lettre, plus la présentation d'un métier (le `01` n'a aucune production). L'auteur ne reçoit que la carte (le geste, le piège, ce qu'il ne redemande pas) : texte, noms, nombres et contexte sont neufs. Plafond de deux devoirs par auteur : `D06` écarté.

**R10 — Hors guide (F1, F5, F8).** Faits de langue du seul Fichier-classe (pronoms compléments, démonstratifs au-delà du cours, gérondif, relatives, ne… rien) : ni cours ni question qui les cible ; l'accord du participe avec avoir est ⛔ (F5) ; l'impératif négatif est enseigné au `02` (F8) mais aucun item ne le cible en examen.

## 2. Carte et écart, par chapitre

Lignes d'examen portant le chapitre (une ligne peut en porter plusieurs) : sessions 2021–2026 (69 lignes) · sessions 2008–2020 (116 lignes) · devoirs (53 lignes).

| chapitre | 2021–2026 | 2008–2020 | devoirs | ce que testent les sujets | écart avec le patron |
| --- | ---: | ---: | ---: | --- | --- |
| `01-travailler-pour-sepanouir` | 12 | 31 | 8 | le temps de la phrase (présent, passé composé, futur) avec un repère de temps ; verbes en -er et verbes hors liste ; pronoms personnels ; infinitif après préposition (une fois) ; nature des mots dans les devoirs ; aucun texte d'examen, aucune consigne de production | le patron (36 questions) a les classes de mots, les pronoms, les trois temps, l'infinitif, les mots-outils et le récit en trois parties, en phrases de l'auteur. **Manque** : la phrase officielle, la réécriture « mets au futur / au présent » sous consigne, le classement des mots d'un même texte, toute consigne de production |
| `02-communiquer-avec-les-autres` | 15 | 22 | 22 | démonstratifs et possessifs (changer le nom, changer la personne), **impératif d'un ordre rapporté (onze lignes)**, pluriel des noms ; textes 2026, 2020, 2013, 2008 (écrans, Internet, portable) ; quatre lectures de devoir sur la communication | le patron a les démonstratifs, les possessifs, l'impératif, a/à et le schéma du récit. **Manque** : la réécriture « remplace X par Y et fais les changements », la lecture d'un texte (aucune), l'appariement dans un texte, la consigne de rédaction |
| `03-accepter-les-autres` | 5 | 18 | 10 | épithète / attribut (tableau), être au futur et au passé composé, accord des adjectifs épithètes ; peu de langue, trois textes anciens (2017, 2016, 2009) et deux productions « faire accepter » | le patron a l'épithète, l'attribut, être/avoir, son/sont et le dialogue. **Manque** : le tableau de fonctions officiel, la lecture d'un récit (ordre, titre, portrait), la consigne de rédaction avec dialogue |
| `04-sentraider-pour-reussir` | 13 | 20 | 5 | négation ne… plus / ne… jamais (huit lignes), verbes comme finir au passé composé et au futur, récits d'entraide (2021, 2020, 2019, 2015) ; « et / est » jamais testé | le patron a la négation, finir, et/est, les cinq temps du récit et le texte documentaire. **Manque** : la phrase officielle, le sens inverse (négatif → affirmatif), la consigne de rédaction ; aucune lecture d'examen retenue |
| `05-sauver-la-nature` | 19 | 27 | 13 | complément essentiel / non essentiel (relever, supprimer, déplacer), **prendre et mettre** (le verbe le plus fréquent), accord du verbe avec son sujet ; textes 2024, 2018, 2012 ; deux devoirs de lecture sur la nature | le patron a le complément essentiel, prendre/mettre, l'accord, l'économie d'eau, le portrait et le récit avec passage descriptif. **Manque** : la réécriture de sujet avec pronoms et pronominaux, la lecture d'un texte avec lexique, la consigne de rédaction |
| `06-etre-en-forme` | 16 | 24 | 1 | aller et faire (présent, passé composé, futur), accord de l'adjectif avec le nom ; le complément de lieu seulement dans un tableau ; texte 2023 ; **aucune lettre en examen** | le patron a le lieu, aller/faire, l'accord de l'adjectif, la santé, la lettre et le lieu décrit. **Manque** : les phrases officielles, la lecture d'un texte, la correction d'erreurs (devoir), la consigne de rédaction avec réactions |
| `07-profiter-du-temps-libre` | 11 | 18 | 1 | complément de temps (en tableau), consonne doublée (nul/nulle, bon/bonne), dire/lire/écrire presque jamais (deux lignes) ; texte 2022 ; trois « suites » de scène (2010, 2009, 2008) | le patron a le temps, dire/lire/écrire, l'adjectif et la lettre. **Manque** : les phrases officielles, la lecture d'un texte, la consigne de « suite » |
| `08-autres-modes-de-vie` | 13 | 23 | 1 | complément de manière (en tableau), vouloir/pouvoir, passé composé avec être ; texte 2025 ; une lettre à un ami lointain dans les devoirs | le patron a la manière, vouloir/pouvoir, le participe, la description et la lecture documentaire. **Manque** : les tableaux à quatre colonnes de phrases officielles, l'enrichissement / le déplacement des compléments, la lecture d'un texte, la lettre à préparer |

**Format de l'épreuve** (17 sessions) : une heure, 20 points, quatre pages, un texte narratif en page 1 ; Compréhension 6 + Grammaire 3 + Conjugaison 3 + Production écrite 8. Ni orthographe-dictée ni exercice de vocabulaire : le lexique est dans la question « synonymes puis contraires » de la compréhension.

**Archétypes d'examen** (185 lignes) : compréhension 67 lignes (relevé et justification, lexique et avis ou hypothèse dans chaque session), langue 101 (réécriture sous consigne, tableau de fonctions, passage à l'impératif d'un ordre rapporté, changement de temps), production 17 (récit d'au moins huit phrases avec dialogue ou répliques, dans les 17 sessions).

**Hors guide** : 7 lignes de langue sur 101 sont entièrement ou principalement hors guide (§ 5) ; 11 lignes d'examen sur 185 portent un jeton `HP:` (jamais seul). Aucune session n'est « ancienne » au sens fort : l'épreuve a peu varié de 2008 à 2026.

**Jamais testé en examen** : l'homophonie (a/à, son/sont, et/est), l'orthographe-dictée, le complément de lieu isolé, dire/lire/écrire (deux lignes), les textes documentaires. Les devoirs ajoutent son/sont, la nature des mots, l'appariement, la remise en ordre, le titre, la correction d'erreurs, la lettre.

## 3. Missions par chapitre

| chapitre | NN | mission | sources (base en premier) | étage | q. |
| --- | ---: | --- | --- | --- | ---: |
| `01-travailler-pour-sepanouir` | 06 | m001 🏛️ hier, aujourd'hui, demain : le temps de la phrase | 2025 ; 2024, 2020, 2019, 2017, 2009 | d2 | 8 |
| `01-travailler-pour-sepanouir` | 07 | m002 📝 Classer les mots : noms propres, noms communs, pronoms | devoir D01#7 | d2 | 6 |
| `01-travailler-pour-sepanouir` | 08 | m003 📝 Présenter un métier en quelques phrases | devoir D03#1 | d2 | 6 |
| `02-communiquer-avec-les-autres` | 06 | m004 🏛️ ce, cet, cette, ces — mon, son, leur : changer le nom, changer le possesseur | 2025 ; 2024, 2023, 2022, 2020, 2015 | d2 | 10 |
| `02-communiquer-avec-les-autres` | 07 | m005 🏛️ fais parler : de l'ordre rapporté à l'impératif | 2026 ; 2024, 2023, 2022, 2020, 2019, 2017, 2016, 2012, 2009 | d2 | 12 |
| `02-communiquer-avec-les-autres` | 08 | m006 🏛️ lecture : dix jours sans écrans | 2026 | d2 | 10 |
| `02-communiquer-avec-les-autres` | 09 | m007 🏛️ préparer un récit : une dispute à propos des écrans | 2026 ; 2020, 2013 | d3 | 8 |
| `02-communiquer-avec-les-autres` | 10 | m008 📝 Lire un petit texte : relier, énumérer, rédiger | devoir D02#5, D09#4, D01#4 | d2 | 7 |
| `03-accepter-les-autres` | 06 | m009 🏛️ l'adjectif épithète ou attribut — le verbe être | 2023 ; 2020, 2016, 2010 | d2 | 8 |
| `03-accepter-les-autres` | 07 | m010 🏛️ préparer un récit : faire accepter un camarade, avec un dialogue | 2017 ; 2016 | d3 | 7 |
| `03-accepter-les-autres` | 08 | m011 📝 Lire un récit : ordre des événements, titre et portrait | devoir D05#5, D05#7, D05#3 | d2 | 8 |
| `04-sentraider-pour-reussir` | 06 | m012 🏛️ ne… plus, ne… jamais : dire le contraire d'une phrase | 2024 ; 2021, 2019, 2018 | d2 | 6 |
| `04-sentraider-pour-reussir` | 07 | m013 🏛️ finir, saisir, grandir, envahir : passé composé et futur | 2025 ; 2022, 2021, 2020 | d2 | 8 |
| `04-sentraider-pour-reussir` | 08 | m014 🏛️ préparer un récit : s'entraider, du début à la fin | 2021 ; 2019, 2015 | d3 | 8 |
| `05-sauver-la-nature` | 06 | m015 🏛️ supprimer, relever : complément essentiel ou non essentiel | 2026 ; 2024, 2012, 2010, 2008 | d2 | 8 |
| `05-sauver-la-nature` | 07 | m016 🏛️ prendre, mettre et leurs dérivés : présent, passé composé, futur | 2023 ; 2021, 2020, 2010, 2008 | d2 | 8 |
| `05-sauver-la-nature` | 08 | m017 🏛️ changer de sujet : l'accord du verbe | 2025 ; 2022, 2015, 2013, 2012 | d2 | 9 |
| `05-sauver-la-nature` | 09 | m018 🏛️ lecture : une fin tragique | 2024 | d2 | 9 |
| `05-sauver-la-nature` | 10 | m019 🏛️ préparer un récit : décrire les émotions et le lieu | 2024 ; 2018, 2012 | d3 | 8 |
| `06-etre-en-forme` | 06 | m020 🏛️ aller et faire : présent, passé composé, futur | 2026 ; 2018, 2015, 2013, 2010, 2009, 2008 | d2 | 11 |
| `06-etre-en-forme` | 07 | m021 🏛️ changer le nom, changer le sujet : l'accord de l'adjectif | 2025 ; 2022, 2018, 2017, 2013, 2012, 2009 | d2 | 10 |
| `06-etre-en-forme` | 08 | m022 🏛️ lecture : un combat victorieux | 2023 | d2 | 9 |
| `06-etre-en-forme` | 09 | m023 🏛️ préparer un récit : décrire les réactions et rapporter les répliques | 2025 ; 2023 | d3 | 8 |
| `06-etre-en-forme` | 10 | m024 📝 Corriger les erreurs : son ou sont, est ou et, accords | devoir D04#4, D04#3 | d3 | 8 |
| `07-profiter-du-temps-libre` | 06 | m025 🏛️ le complément de temps — dire et écrire | 2018 ; 2017, 2016, 2012 | d2 | 7 |
| `07-profiter-du-temps-libre` | 07 | m026 🏛️ nul / nulle, bon / bonne, gros / grosse : la consonne qui double | 2026 ; 2019, 2015, 2010 | d2 | 8 |
| `07-profiter-du-temps-libre` | 08 | m027 🏛️ lecture : Lucile sur les planches | 2022 | d2 | 9 |
| `07-profiter-du-temps-libre` | 09 | m028 🏛️ préparer un récit : imaginer la suite ou la réalisation d'une scène | 2022 ; 2010, 2009, 2008 | d3 | 9 |
| `08-autres-modes-de-vie` | 06 | m029 🏛️ lieu, temps, manière : remplir le tableau, enrichir, déplacer | 2025 ; 2023, 2022, 2021, 2019, 2017, 2015, 2013, 2009 | d2 | 10 |
| `08-autres-modes-de-vie` | 07 | m030 🏛️ vouloir et pouvoir : présent, passé composé, futur | 2026 ; 2021, 2018, 2016, 2008 | d2 | 10 |
| `08-autres-modes-de-vie` | 08 | m031 🏛️ le passé composé avec être : l'accord du participe | 2024 ; 2019, 2015, 2012 | d2 | 8 |
| `08-autres-modes-de-vie` | 09 | m032 🏛️ lecture : à la découverte de la pyramide maya | 2025 | d2 | 9 |
| `08-autres-modes-de-vie` | 10 | m033 📝 Écrire une lettre à un ami lointain : préparer | devoir D08#1 | d3 | 8 |

**27 missions d'examen et 6 de devoirs, 278 questions** : 17 lignes de production sur 17, 22 lignes de compréhension sur 67 (cinq textes), 94 lignes de langue sur 101. Le détail item par item (session, exercice, phrase officielle, forme de question, piège) est dans `plan-missions-v1.json` (`items`) et dans chaque carte.

## 4. Lots d'auteurs (une carte par lot)

| lot | chapitres | missions | auteurs | parallélisme |
| --- | --- | --- | --- | --- |
| M1 | 01, 02 | m001, m002, m003, m004, m005, m006, m007, m008 (8) | 1 | avec les trois autres lots ; un chapitre = un auteur à la fois |
| M2 | 03, 04 | m009, m010, m011, m012, m013, m014 (6) | 1 | avec les trois autres lots ; un chapitre = un auteur à la fois |
| M3 | 05, 06 | m015, m016, m017, m018, m019, m020, m021, m022, m023, m024 (10) | 2 (un par chapitre) | avec les trois autres lots ; un chapitre = un auteur à la fois |
| M4 | 07, 08 | m025, m026, m027, m028, m029, m030, m031, m032, m033 (9) | 2 (un par chapitre) | avec les trois autres lots ; un chapitre = un auteur à la fois |

Skills : `content-ecole-tn`, puis `content-langue-francais` (registre de langue) ; pas de `prof-francais-6eme` : `prof-francais-college` sert à calibrer les étages `d3`, sans en reprendre le programme. Consignes : `content-ingest/references/gisement-auteur-examen.md` (examens, avec la transcription de chaque session citée) et `gisement-auteur-devoir.md` (devoirs : la carte seule). **Ordre dans un lot** : (1) les ids d'étiquette neufs ; (2) les missions du chapitre ; (3) gates ; les missions de lecture et de production viennent après la langue du même chapitre (elles s'appuient sur ses notions).

## 5. Ce qui est écarté, et pourquoi

| écarté | pourquoi |
| --- | --- |
| Sept lignes de langue qui ne portent que des notions hors guide : C01#7 (« plus personne ne rit » → forme affirmative), C04#7 et C06#6 (changer le genre du sujet : participe pronominal), C09#7 (tableau avec le « complément d'objet direct »), C17#5 (accord dans une phrase passive), C19#5 (ordre rapporté → parole directe), C19#6 (pronoms personnels pour éviter une répétition) | `HP:negation-personne` (⛔ § 2.10 D), `HP:pc-pronominal`, `HP:cod`, `HP:voix-passive`, `HP:discours-indirect`, `HP:pronom-complement` : la cible de l'item est hors guide ; leur part au programme est reprise ailleurs quand il y en a une (C04#6, C05#8, C12#5 : le blanc HP est donné rempli) |
| Les 45 lignes de compréhension de douze sessions (2008–2021) ; seuls cinq textes sont repris | R2 : une mission par texte, au plus cinq, récents et représentatifs (2022–2026). Le texte de 2021 (chat adopté) est le sixième des textes récents : son thème n'est annoncé par aucun module et ses gestes (relever, idée, oui/non + indices, lexique, paroles) sont déjà dans 2022 et 2023 — décision à soumettre E1 |
| `D06` (production du 2ᵉ trimestre) — statut `ecarte` | troisième devoir du même auteur que `D04` et `D05` (plafond de deux, D-4) ; aucune signature neuve (mesure mixte : 0 sur 1), le récit avec description et dialogue est couvert par les productions d'examen (m014, m019, m023) |
| Quarante-deux lignes de devoirs sur cinquante-trois | gestes déjà dans les examens (vrai/faux justifié, relevé, lexique, avis, négation, impératif, compléments) ou déjà dans le patron ; onze lignes sont reprises (dix signatures neuves au niveau gabarit + la présentation d'un métier, neuve au `01`) |
| D04#2 (conjuguer au temps imposé par le contexte) | signature neuve seulement par combinaison de chapitres, et `HP:imparfait` (le repère de temps du contexte appelle l'imparfait) : le geste « choisir le temps d'après un repère » est déjà repris au `01` (C02#9, C08#9, C10#7) |
| D01#9 (articles ou possessifs), D07#9 (pc avec pronom complément) | articles/possessifs : le leurre « article à la place du possessif » est un distracteur de la mission des déterminants (`02`) ; D07#9 : `HP:pronom-complement` |
| Orthographe-dictée, vocabulaire en exercice, a/à, et/est, lettre en examen | aucune ligne d'examen (l'épreuve n'a ni dictée ni exercice de vocabulaire ; a/à, et/est : jamais testés). Ils restent servis par le patron (`02` a/à, `04` et/est) ; son/sont (devoir) est repris dans m024 (correction d'erreurs) |
| Accord de « tout » (C04#6, blanc « toutes »), pronominaux dans l'accord du verbe (C12#7, C14#7, C15#9) | `HP:accord-tout` : blanc donné rempli. Pronominaux (nous nous approchons) : le pronom réfléchi sert à l'accord du verbe, il n'est jamais la cible (F1) |

## 6. Les devoirs : ce qu'ils apportent vraiment

La vague 1 (neuf devoirs, 53 lignes) recoupe la fiche : seules 2 lignes sur 53 portent un jeton `HP:`, aucun devoir n'est « ancien » au sens fort. Mesure de la **règle des 30 %** (journal des devoirs § 6, famille d'archétype × chapitres de la ligne, jetons `HP:` ôtés, contre les 185 lignes d'examen) :

| mesure | lignes neuves | signatures distinctes neuves |
| --- | ---: | ---: |
| strict (famille + chapitres) | 19 sur 53 (35 %) | 16 sur 34 |
| **mixte** (compréhension : famille seule) — retenue | **15 sur 53 (28 %)** | 14 sur 27 |
| gabarit (famille seule) | 10 sur 53 (19 %) | 8 sur 20 |

La mesure mixte est la plus juste (en compréhension, le chapitre ne dit que le thème du texte) : **28 %, sous le seuil de 30 %**. **Pas de vague 2** (décision du pilote). Les dix lignes à signature neuve au niveau gabarit portent huit familles, toutes reprises : appariement (m008), remise en ordre et titre (m011), nature des mots (m002, m011), son/sont et correction d'erreurs (m024), court paragraphe (m008), lettre (m033) ; s'y ajoute la présentation d'un métier (m003, neuve au `01` parce que l'épreuve n'y a aucune production). **Onze lignes de devoirs reprises sur 53** ; après ce plan, plus aucune signature neuve ne reste.

Plafond par auteur : `D04`, `D05` et `D06` portent la même main (deuxième trimestre) ; on garde `D04` et `D05` (m024, m011), `D06` est écarté.

## 7. Décisions du pilote déjà prises (2026-10-19)

`D06` écarté (plafond de deux par auteur) ; pas de vague 2 de devoirs ; compréhension : une mission par texte, au plus cinq ; langue : une mission par famille et par chapitre, sessions fusionnées ; production : préparation fermée regroupée par archétype ; placement F4 ; plafond de 12 questions ; étages d2/d3 ; rien de ce que le patron pose déjà ; missions de devoirs en salle blanche sur les gestes absents des examens.

## 8. Décisions à soumettre au pilote

| # | question et proposition |
| --- | --- |
| E1 | lecture du `04`. Le `04` n'a pas de texte d'examen (le seul récent, 2021, est écarté) ; le `03` a sa lecture dans la mission de devoir (m011). Proposition : garder cinq textes. Option : repêcher 2021 pour le `04` (une mission de plus, environ neuf questions, thème « chat adopté » rattaché au `04` par défaut). |
| E2 | étage d'une mission = celui de la ligne la plus haute ENTIÈREMENT reprise ; une ligne `d3` dont on ne reprend qu'une réponse (C02#7, C03#6, C10#5…) compte `d2`. Bilan : 25 missions `d2`, 8 `d3` (six productions et deux devoirs). Alternative stricte (ligne la plus haute) : 8 missions de langue passeraient en `d3`. |
| E3 | volume. 33 missions, 278 questions (environ 35 par chapitre, soit presque le double des 36 questions du patron). Si le pilote veut alléger, l'ordre de coupe conseillé est : familles de langue minces (m012 phrase négative, m026 adjectifs au féminin) puis la seconde mission de langue du `05`. Aucune lecture ni production n'est à couper. |
| E4 | lots M3 (dix missions) et M4 (neuf missions) au-dessus de la fourchette de huit : un auteur par chapitre (05 / 06 ; 07 / 08), chapitres disjoints, donc en parallèle ; chaque auteur a cinq missions au plus. |
| E5 | placement des productions par archétype, pas par thème, pour C02#11 (thème 08, rangée au `06` avec C04#11) et C19#10 (thème 02, rangée au `07` avec les « suites » de 2008–2010) ; C05#12 (projet de festival) est rangée avec les suites au `07`. Le thème étant déjà donné par la consigne officielle redonnée, l'archétype porte l'apprentissage. |
| E6 | le cours du `07` ne cite pas « nul / nulle » (il cite bon, gros, vieux, gentil, beau) : m026 reprend C01#8 (« complètement nulle ») ; l'auteur ajoute ce mot à l'exemple du cours du `07` ou donne la forme. |
| E7 | C11#8 (2016, « La veille, vous … tristes ») : l'imparfait est possible (`HP:imparfait`) ; la mission propose le passé composé sans l'imparfait dans les options. Clé non publiée : à confirmer par l'auditeur. |
| E8 | sujets sensibles : 2024 (mort d'un petit phoque, m018), 2023 (handicap et opération, m022), 2017 et 2016 (accepter un camarade handicapé ou muet, m010). Les missions gardent le ton du texte, sans détail ajouté. |


### Décisions du pilote (2026-10-19)

| | Décision |
| --- | --- |
| **E1** | **Non** : 2021 n'est pas repêché (profondeur avant volume ; le 04 garde ses missions de langue et de production, la lecture du thème « entraide » est travaillée par son cours et ses exercices). |
| **E2** | Règle retenue telle que proposée : l'étage d'une mission suit les lignes réellement reprises (une ligne d3 dont on ne reprend qu'une réponse compte d2). |
| **E3** | Volume gardé (≈ 35 questions de mission par chapitre) ; pas de coupe. |
| **E4** | Un auteur par lot de deux chapitres : les auteurs des chapitres (B1→M1, B2→M2, B3→M3, B4→M4) écrivent leurs missions. |
| **E5** | Accepté : C02#11 au 06 et C19#10 au 07, rangés par archétype, déclaré dans la note de la mission. |
| **E6** | Le cours du 07 n'est pas rouvert : la forme *nul → nulle* est **donnée dans l'énoncé** ou l'item est écarté. |
| **E7** | C11#8 **écarté** (clé ambiguë, l'imparfait se défend). |
| **E8** | Accepté : le ton des textes officiels est gardé, aucun détail ajouté. |
