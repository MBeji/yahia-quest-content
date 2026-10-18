# Gisement 6ᵉ × anglais : plan des missions d'examen et de devoirs (G3–G4, étude 36) — v1

Écrit le 2026-10-18 par le planificateur (lots D2 et A de [`PLAN.md`](./PLAN.md)). Entrées : les 17
sujets lus (`C01`–`C19`, sans `C13` 2014 et `C16` 2011, introuvables), leurs transcriptions
(`content/programmes-officiels/examens-nationaux/6eme-base/english/`), les 102 lignes d'examen et les 51
lignes de devoirs (`36-…/en-cours/lecture-6eme/anglais/lines/`), les quatre journaux de lecture, les 245
questions de `content/english-6eme/`, [`ETAT.md`](./ETAT.md) et les décisions D1–D8. Modèle : le plan de
l'anglais 9ᵉ (`36-…/en-cours/anglais/PLAN.md`, v2).

Sorties :

- carte et écart : `content/programmes-officiels/sources-externes/web-6eme-base-english/fiche.md` § 4–5 ;
- plan machine : [`plan-missions-v1.json`](./plan-missions-v1.json) — 21 missions (`m001`–`m021`), le
  fichier « Let's pronounce » du 07, les écartés, la mesure des devoirs, les décisions à soumettre ;
- registre : `…/web-6eme-base-english/gisement.json` — 21 missions `planifiee` (id = la source de base,
  `sources` = toutes les sources fusionnées, `note` = l'id du plan) ;
- vocabulaire : [`vocab-english-6eme.json`](./vocab-english-6eme.json) et [`map-vocab.md`](./map-vocab.md)
  (lot A) ;
- cartes d'affectation = lots auteurs : [`assign-B1.md`](./assign-B1.md) (01, 02),
  [`assign-B2.md`](./assign-B2.md) (03, 04), [`assign-B3.md`](./assign-B3.md) (05, 06),
  [`assign-B4.md`](./assign-B4.md) (07 et « Let's pronounce »).

Avant le plan, les étages des lignes de langue de C10, C14, C15, C17, C18 et C19 ont été harmonisés
sur le lot pilote (§ 0 de `JOURNAL-lecture-C01-C06.md`) : 15 lignes de cloze, de choix et d'appariement
passent de `d1` à `d2` ; revalidées (153 valides, 0 fautive).

## 1. Règles retenues (adaptées du plan 9ᵉ)

**R1 — Langue : une mission par famille et par chapitre, sessions fusionnées, au grain de l'item.** Un
exercice de langue mêle les notions (le cloze 2023 teste un adverbe de fréquence, une maladie et
much) : chaque blanc **au programme** rejoint la mission de sa famille, au chapitre de sa notion ; ses
voisins vont ailleurs ou sont écartés. **Base** : la session 2023–2026 la plus riche (programme en
vigueur) ; quand elle sert déjà de base à une autre mission, la suivante. Les sessions 2008–2022
n'apportent **que leurs items au programme** ; un blanc HP du même texte est donné rempli, jamais
demandé. Chaque question **dit sa session** (« Exam 2013 ») et redonne la phrase officielle avec UN
blanc. Titre : « 🏛️ Exams <années> · <sujet en anglais> » (une session : « 🏛️ Exam <année> · … »),
puis les étoiles de l'étage ; tout le texte visible est en anglais.

**R2 — Reading : une mission par texte, cinq textes, un par chapitre de thème (D2).** 2023 (concours de
dessin → `01`), 2026 (journée du soin → `04`), 2021 (fête de fin d'année → `05`), 2024 (centre
commercial → `06`), 2025 (voyage en Tunisie → `07`). Une à deux phrases citées par question, prises
dans le PDF officiel (sha256 au registre), jamais le texte entier. Vrai/faux → choix puis phrase qui le
prouve ; « complete with words from paragraph n » → QCM de mots du paragraphe ; « why…? » → QCM de la
raison que le texte fonde ; remise en ordre d'événements → `ordering`.

**R3 — Writing : converti en préparation fermée.** La rédaction vaut 4 points ; la mission redonne la
consigne officielle et ne demande que ce qui se décide **avant** d'écrire : la tâche exacte, les idées
pertinentes (`multi`), le temps ou le modal attendu, l'ordre du plan (`ordering`), la formule
d'ouverture et de clôture telle qu'imprimée. Six missions : 2024 (conseils du médecin → `02`), 2022
(vacances d'hiver → `03`), 2026 + 2023 (prendre soin d'un animal, tâches à la maison → `04`), 2021
(anniversaire en famille → `05`), 2025 (journée d'achats → `06`).

**R4 — Rien de ce que le patron pose déjà.** Croisement question par question contre les 245 questions ;
chaque mission nomme les questions existantes à ne pas redemander (`neDemandePas` du plan, liste de
chaque carte). Ce qui manque partout au patron : la phrase officielle, le texte lacunaire,
l'appariement, la remise en ordre, la lecture d'un texte, la consigne de production.

**R5 — Placement.** Langue : chapitre de la notion (rangements fixés au § 0 du journal pilote : simple
past → `05`, will → `03`, modaux et How many/much → `02`…). Reading et writing : chapitre du thème
(D2). Dialogues de fonctions : `01` (suggestion, invitation), sauf les dialogues de magasin → `06`.

**R6 — Types natifs.** `ordering` (mots, phrases, répliques, événements), `matching` (appariements,
dialogues à cercles numérotés, magasin ↔ article), `multi` (idées d'une production), `short_answer`
seulement pour une forme unique (found, rainy, north) avec ses `acceptedAnswers`.

**R7 — Taille, étage, en-tête.** 12 questions au plus ; étage = celui de la ligne la plus haute de la
mission, jamais `d1` (→ `d2`), `d3` au plus ; en-tête `d2` practice 75 / 15, `d3` boss 120 / 30. Bilan :
16 `d2`, 5 `d3`. `chapter.json`, `sources[]` de chaque chapitre touché : « Sujets officiels du concours
d'entrée aux collèges pilotes (6ᵉ année de base), Ministère de l'Éducation (corpus officiel, reprise
citée, étude 36) — transcriptions : programmes-officiels/examens-nationaux/6eme-base/english/ ».

**R8 — Étiquettes.** Le vocabulaire du lot A (`vocab-english-6eme.json`) : ids `english.*` réutilisés,
élargis ou neufs ; les auteurs ajoutent à `content/misconceptions.json` les ids neufs et les libellés
élargis **qu'ils posent**, dans la PR de leur lot.

## 2. Missions par chapitre

| chapitre | NN | mission | sources (base en premier) | étage | q. |
| --- | --- | --- | --- | --- | ---: |
| `01-entertaining-myself` | 06 | m001 like + -ing, how often and the -s | 2023 ; 2025, 2024, 2018, 2017, 2015, 2013, 2010, 2009, 2008 | d2 | 12 |
| `01` | 07 | m002 his, her, their — and, but, because | 2021 ; 2020, 2019, 2016, 2012, 2009, 2008 | d2 | 9 |
| `01` | 08 | m003 dialogues: suggest, invite, answer | 2023 ; 2026 | d2 | 8 |
| `01` | 09 | m004 reading: the drawing competition | 2023 | d2 | 7 |
| `02-keeping-fit` | 06 | m005 should, must, can — stomachache — How much | 2025 ; 2023, 2020, 2018, 2013 | d2 | 8 |
| `02` | 07 | m006 writing prepared: the doctor's advice | 2024 | d3 | 8 |
| `03-having-fun-in-the-seasons` | 06 | m007 weather words, seasons and will | 2026 ; 2025, 2023, 2019, 2018, 2010, 2008 | d2 | 9 |
| `03` | 07 | m008 writing prepared: my winter holiday | 2022 | d3 | 7 |
| `03` | 08 | m020 📝 a seasons letter: read and check (devoir) | devoir D09 | d2 | 6 |
| `04-caring` | 06 | m009 the cleanest, the coldest — and the people who help | 2024 ; 2025, 2023 | d2 | 6 |
| `04` | 07 | m010 reading: World Caring Day | 2026 | d2 | 7 |
| `04` | 08 | m011 writing prepared: helping at home, caring for a pet | 2026 ; 2023 | d3 | 9 |
| `05-celebrations` | 06 | m012 the simple past: regular and irregular | 2026 ; 2025, 2024, 2023 | d3 | 11 |
| `05` | 07 | m013 reading: the end-of-year party | 2021 | d2 | 6 |
| `05` | 08 | m014 writing prepared: a family birthday party | 2021 | d2 | 6 |
| `06-going-shopping` | 06 | m015 at the shop: Can I help you?, I'd like, How much is it? | 2024 ; 2025, 2021, 2018, 2012, 2010 | d2 | 9 |
| `06` | 07 | m016 reading: lost at the mall | 2024 | d2 | 7 |
| `06` | 08 | m017 writing prepared: a shopping day at the mall | 2025 | d3 | 8 |
| `07-around-the-world` | 06 | m018 reading: a trip to Tunisia | 2025 | d2 | 6 |
| `07` | 07 | m019 greetings, a and an, north and south | 2013 ; 2025, 2018, 2016, 2015 | d2 | 6 |
| `07` | 08 | m021 📝 a postcard from my town (devoir) | devoirs D07, D08 | d2 | 6 |
| `07` | 09 | « Let's pronounce » (hors gisement, D6) | — | d1 | 4 |

**19 missions d'examen et 2 de devoirs, environ 160 questions.** Le détail item par item (session,
exercice, blanc, forme de question) est dans `plan-missions-v1.json` (`items`) et dans chaque carte.

## 3. Lots auteurs (= lots B1–B4 de `PLAN.md`)

| lot | chapitres | missions | et aussi | parallélisme |
| --- | --- | --- | --- | --- |
| B1 | 01, 02 | m001–m006 (6) | étiquetage 210 distracteurs, `coursePitfalls`, défauts tranche | avec B2, B3, B4 |
| B2 | 03, 04 | m007–m011, m020 (6) | étiquetage 210, idem | idem |
| B3 | 05, 06 | m012–m017 (6) | étiquetage 210, idem | idem |
| B4 | 07 | m018, m019, m021 (3) + section et fichier « Let's pronounce » | étiquetage 105, idem | idem ; cours **avant** les questions de prononciation |

Skills : `content-ecole-tn` puis `content-langue-anglais` (pas de `prof-anglais-6eme` : le niveau n'en a
pas ; `prof-anglais-college` pour la calibration des étages hauts, sans en reprendre le programme).
Consignes : `content-ingest/references/gisement-auteur-examen.md` (examens, avec la transcription de
chaque session citée) et `gisement-auteur-devoir.md` (m020, m021 : l'auteur ne reçoit que la carte,
jamais le devoir). **Ordre dans un lot** : (1) les ids du vocabulaire que le lot pose ;
(2) étiquetage et défauts des items existants ; (3) les missions ; (4) `coursePitfalls` en dernier
(C-5 exige un distracteur qui porte chaque tag).

## 4. Ce qui est écarté, et pourquoi

| écarté | pourquoi |
| --- | --- |
| les textes de reading 2008–2022 sauf 2021 | R2 : un texte par chapitre de thème ; 2021 garde le 05 |
| dérivation (twice, friendly, invitation), adjectifs en -ed / -ing, the most (2023–2026) | hors guide (fiche, « EXCLU ») |
| present continuous, there is / are, have got, wh-questions, going to, pronoms sujet et complément | hors guide ; programme ancien ; formes données quand la phrase sert une autre question |
| les 2 items de pronom complément (2022 « with her », 2024 « them ») | `HP:personal-pronouns` (seuls les possessifs sont au guide) |
| lexique hors guide (maison, pièces, ferme, objets de classe, contraires courants, right / left) | `HP:vocab-hors-guide` (23 lignes) |
| correction de fautes d'orthographe de mots hors guide (hause, speek, brekfast) | orthographe hors guide ; le geste « corriger » est gardé dans m001 sur des fautes au programme |
| lettres en désordre, sauf rainy et north | lexique hors guide ou déjà interrogé |
| rédactions 2020 (l'école) et 2019 (se présenter) | thèmes hors des sept unités |
| devoirs : identité, famille, nationalités, corps, jours, maison, fable, grilles, questions en wh- | hors guide (76 % des lignes de devoirs portent un jeton HP) |
| devoirs : nombres en lettres, How many, vêtements d'après images, articles et prépositions | au programme mais déjà interrogés par le patron (06/quiz#4, 06/01-pratique#5, 02/01-pratique#6, 07/03-revision#6…) |

## 5. Les devoirs : ce qu'ils apportent vraiment

Les neuf devoirs de la vague 1 sont **tous de l'ancien programme** (journal de lecture : datés de 2014 à
2021, thèmes hors des sept unités). **Mesure des signatures neuves** (famille d'archétype + chapitres de
la ligne, jetons HP ôtés, comparée aux 102 lignes d'examen) :

| compte | neuves |
| --- | ---: |
| brut, 51 lignes | 30 (58 %) |
| hors écoute, 49 lignes | 28 (57 %) |
| rattachées à au moins un chapitre | 13 (27 %) |
| après le plan d'examens et le patron | **2 (4 %)** |

Le chiffre brut est trompeur : 15 des 28 signatures neuves hors écoute ne portent **aucun** chapitre
(thèmes et structures hors guide). Des 13 qui en portent un, 11 sont déjà couvertes par le patron
(nombres, How many, vêtements, articles) ou par une mission d'examen (remise en ordre de salutations,
m019) ou ne sont neuves que par leur part HP (présent continu). Restent deux gestes vraiment absents,
une mission chacun en salle blanche : **lire une lettre de saison et corriger des affirmations** (`03`,
m020 ; le `03` n'a pas de texte d'examen récent) et **compléter une carte postale de sa ville** (`07`,
m021 ; aucune production d'examen au `07`). **Pas de vague 2** : sous 30 % dès qu'on ôte les jetons HP,
et une vague 2 sur devoir.tn trouverait très probablement d'autres devoirs d'avant « Learn and Grow » (les
seuls devoirs datés de la rubrique s'arrêtent en 2020-2021 ; les autres ne sont pas datés).

## 6. Décisions à soumettre au pilote

| # | question | proposition |
| --- | --- | --- |
| E1 | Étages des lignes C07–C12 : contraires (C08#3, C11#3, C12#3) et lettres en désordre (C09#5, C11#5) restent `d1`, alors que le pilote met les contraires en `d2` (C02#4, C04#4) ; même cas en C14–C19 pour contraires, lettres en désordre et mots d'après images (C14#4, C15#5, C17#4, C17#6, C18#5, C19#4) | tout passer en `d2` comme le pilote (sans effet sur le plan : R7 n'a jamais de `d1`) |
| E2 | `HP:pronunciation` sur D06#7 (intrus par le son de la voyelle) : la prononciation **est** au guide (35 « Let's pronounce ») | retirer le jeton, ranger au chapitre du son (01 ou 02) ; rien de neuf pour le plan |
| E3 | Reading C17 (2010, petit-déjeuner) en `02`, C18 (2009, vacances) en `07` ; le journal hésite avec `01` | garder `02` et `07` (thème, D2) ; aucun des deux n'est retenu (R2) |
| E4 | Items anciens convertibles : « Jane (is / has / have) twelve years old » (2013) ; « How many … have you got? » (2015, 2019, 2020) ; « with (her / him / their) » (2022) | écarter les trois (to be + âge non enseigné ; have got et pronom complément HP) ; ne convertir que ce qui garde la phrase officielle |
| E5 | Sessions anciennes gardées comme base d'une mission : 2022 (rédaction d'hiver, m008), 2021 (texte et rédaction, m013, m014) | garder : chaque contenu imposé est dans le guide ; sinon le `03` et le `05` n'auraient ni texte ni production |
| E6 | m006 (2024, « advised you to… ») appelle le discours rapporté, hors guide | faire écrire les conseils au style direct (You should…), dit dans l'explication |
| E7 | Objectif d'étiquetage ≥ 60 % : les distracteurs de pur lexique (mois, saisons, boutiques) n'ont pas d'erreur de grammaire | une étiquette générique `english.vocab.mot-voisin-du-meme-champ`, posée seulement quand un indice de l'énoncé tranche ; sans elle l'objectif tombe vers 45–50 % aux 01, 04, 06, 07 |
| E8 | m019 a pour base 2013 (C14#5), parce que la session 2025 la plus riche (C02#5) sert déjà de base à m005 | accepter (l'id du registre doit être unique) |

## Décisions du pilote (2026-10-18)

E1 oui (contraires, lettres en désordre, mots d'après images en d2) ; E2 oui ; E3 oui ; E4 oui (trois items écartés) ;
E5 oui (2021–2022 gardées comme base de m008, m013, m014) ; E6 oui (conseils au style direct) ;
E7 oui **sous condition** : `english.vocab.mot-voisin-du-meme-champ` seulement quand l'option est réellement un mot du même
champ lexical que la clé — jamais pour atteindre le quota ; un chapitre sous 60 % est acceptable s'il est honnête ; E8 oui.
Vocabulaire appliqué par le pilote dans `content/misconceptions.json` (19 neufs, 6 élargis) ; libellé de
`english.verb.ing-oublie` resserré : « like/love/hate + to » est correct en anglais, seule la base nue y est fautive.
Pas de vague 2 de devoirs (4 % de signatures neuves après le plan).
