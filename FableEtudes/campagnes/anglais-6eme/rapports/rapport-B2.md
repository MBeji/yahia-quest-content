# Rapport B2 — anglais 6ᵉ, chapitres 03 et 04

Écrit le 2026-10-18 par l'auteur B2. Pas de git. Gates passés sur l'arbre `wip/anglais-6eme-un-passage` : `content:check` vert, `content:qa -- --subject english-6eme` 0 erreur, `content:tranche --strict-longest` sans défaut, `lot-lint` sans point sur mes 24 fichiers, `prettier --check` vert, `content:gisement:controle` (m020) vert (0 plage de 8 mots, 0 exercice source repris).

## Fichiers

Créés (6 missions, 45 questions) :

- ch03 : `exercices/06-exams-2008-2026-weather-seasons-will.json` (m007, d2, 8 q), `07-exam-2022-writing-winter-holiday.json` (m008, d3, 7 q), `08-devoir-a-seasons-letter.json` (m020, devoir, d2, 6 q).
- ch04 : `exercices/06-exams-2023-2025-superlative-and-jobs.json` (m009, d2, 6 q), `07-exam-2026-reading-world-caring-day.json` (m010, d2, 7 q), `08-exams-2023-2026-writing-caring.json` (m011, d3, 9 q).

Modifiés : `chapter.json` des deux chapitres (`sources[]`, `coursePitfalls`, la ligne devoirs au 03 seulement) ; `quiz.json` et les cinq exercices existants de chaque chapitre (étiquettes, défauts). Aucun `cours.md` ni `misconceptions.json` touché.

## Étiquetage (distracteurs étiquetés / total, QCM seulement)

| chapitre | avant | existants après | avec les missions neuves |
| --- | --- | --- | --- |
| 03 | 0 / 105 | 67 / 105 = 64 % | 103 / 159 = 65 % |
| 04 | 0 / 105 | 54 / 105 = 51 % | 82 / 162 = 51 % |

Le 04 reste sous 60 %, honnêtement : les distracteurs de lecture, de lexique (farm / farming / farms, help / home) et de sens (reading d'ordre de rangs) n'exécutent aucune erreur du registre. Missions neuves : m007 13/21, m008 9/15, m020 14/18, m009 4/18, m010 11/21, m011 13/18.

`coursePitfalls` posés comme la carte (5 au 03, 6 au 04), chacun porté par au moins un distracteur du chapitre.

Vote terme à terme : plans 2×2 complets (option à deux erreurs muette) aux m008 Q6, m020 Q6, m010 Q2 (mots du texte).

## Défauts `content:tranche` corrigés

| | avant | après |
| --- | --- | --- |
| clé strictement la plus longue | 03 : 4 (quiz#3, 01#6, 05#1, 05#6) ; 04 : 8 | 0 |
| paires proches | 3 (03 : 01#1 ↔ 03#1 ; 04 : quiz#4 ↔ 04-defi#1, 02-boss#6 ↔ 05#6) | 0 |
| gabarits | 3 candidats (03 04-defi#1, 05#5…) | 0 (consignes variées) |

Réécritures : 03 quiz#3 (un distracteur rallongé), 01#6 (« She enjoys ___ »), 03#1 (« In which month does spring begin? »), 05#1 (« just before September »), 05#6 (liste swimming / walking / playing), 04-defi#1 de 03 et 05#5 (consigne), 04 quiz#3, 02-boss#1 et #3, 03-revision#2 et #3, 04-defi#1 (repensé : « who has a job name not built with -er »), #2, #4, 05#6 (affiche du jardin). Les explications suivent.

## Items écartés ou fondus

- Écartés (carte) : swings, sliding (2026, lexique de parc hors guide), the most (HP), will choose / chose (→ m012).
- **2008 L3 (rainy) fondu dans la question short_answer 2018 W1** : deux questions au même mot auraient livré la clé l'une à l'autre. m007 a 8 questions, non 9 ; le titre garde « 2008 », la question cite les deux sessions.
- m010 : « vrai/faux + phrase qui prouve » en une question par affirmation (le verdict et la raison dans les options), pour ne citer qu'une à deux phrases du texte ; deux questions de lecture ajoutées (date de la fête, titre) pour garder 7.

## Notions données dans l'énoncé

- m011 : le passé du récit (saw, decided dans la consigne ; found dans la clé) est seulement nommé, comme le dit la carte ; les phrases du paragraphe à ordonner portent des passés non enseignés (saw, took, gave, bought) qui se lisent sans être demandés.
- m009 Q6 : le sens de « loved and cared for » est donné (feel loved by others and looked after by them) ; le -ed est le seul point testé.
- m010 Q2 : le mot du paragraphe 3 n'est pas lisible dans le sujet (express est au paragraphe 2, show au 3) : la question propose des paires de mots du texte, sans numéro de paragraphe ; « express » est retenu, « show » n'est pas proposé.

## Écarts à la carte

- Étiquettes hors liste mais au registre et exactes : `english.spell.suffixe-sans-regle-orthographique` (04 : bigest, happyest, driveer) ; `english.verb.s-oublie-3e-personne` et `english.verb.be-avec-base-verbale` (m011 Q7) ; `english.write.phrase-cle-trop-etroite` (m011 Q8) ; `english.read.premier-mot-cle-sans-lire-la-phrase` (m010 Q5). Aucun identifiant créé.
- m007 : 8 questions au lieu de 9 (voir plus haut).
- m008 : l'ordre du courriel ne reprend ni la formule d'ouverture ni la clôture (elles sont la clé de la question de clôture) : une phrase d'ouverture et un vœu de fin les remplacent.

## Doutes pour l'auditeur

- m007 Q5 : « The weather is funny » est de l'anglais possible (temps bizarre) ; la phrase donne « the children are swimming » pour trancher.
- m007 Q2 ↔ 03 quiz#2, m009 Q2 ↔ 04 02-boss#1, m009 Q4 ↔ 04 01#4, m011 Q5 ↔ 04 01#1 : même notion que le patron, autre geste ou autre énoncé (la carte liste ces questions en « ne pas redemander » alors que l'item officiel y retombe : « the cleanest one », « a waiter »).
- Étiquettes « mot-voisin » : 22 au 03 (dont 13 sur les questions existantes : mois, saisons, vêtements ; 6 en m007, 3 en m020) et 9 au 04 (jobs et corvées). Posées seulement quand un indice de l'énoncé tranche ; sans elles le 03 tomberait à 51 % et le 04 à 45 %.
- m010 Q3 : la clé « express » vaut pour le texte ; « show » serait aussi défendable pour le sujet officiel.
- `content/CATALOGUE.md` (régénéré par `content:catalogue`) n'est pas touché : à régénérer par l'orchestrateur, les chapitres ayant des exercices en plus.

## Corrections après audit (audit-B2.md)

Relancés verts : `content:check`, `content:qa -- --subject english-6eme`, `content:tranche --fresh --strict-longest` (clé la plus longue 0, paires 0, gabarits 0 ; seul avertissement : positions de clé sur les 59 questions modifiées, d = 13 %), `lot-lint`, `prettier --check`, rendu `renderLesson` / `renderSummary` du cours et du résumé 04 (vitest jetable, supprimé).

| défaut | fait |
| --- | --- |
| C-1 m008 Q7 ordre non unique | phrases b (« In the morning we drink hot milk… ») et f (« In the afternoon we enjoy walking… ») réécrites, ordre e,a,c,b,f,d, explication de l'auditeur |
| M-1 m010 Q3 | citations des paragraphes 1 et 3, paires `decided/organize … show/did`, explication de l'auditeur (le mot « illisible » de mon rapport était faux : show est lisible) |
| M-2 m010 Q6, Q7 | libellé `(Exam 2026 — reading text)` |
| M-3 m011 Q6 | « find becomes found » dans l'énoncé, d2, explication complétée |
| M-4 04/02-boss#1 | réécrit avec « the strongest » (étiquettes a, c, d) |
| M-5 cook / cooker | ajout au bloc `::: piege` et au `::: retenir` de `04-caring/cours.md`, ligne de `resume.md` |
| m-1, m-2 m007 Q6, Q8 | libellés de session corrigés |
| m-3 m007 Q2, Q4 | « Choose the opposite of » |
| m-4 m007 Q4 | option « outside » remplacée par « behind » (mot-voisin), explication ajustée |
| m-5 m007 Q5 | explication de « funny » de l'auditeur |
| m-6 m010 Q4 | « What does the word they refer to? » |
| m-7 m011 Q2 | option c et explication « four things » |
| doute 6 | étiquettes ajoutées : « the most big » (02-boss#3), « the most clean » devenu « the most strong » (02-boss#1), « hottest » (m009 Q3, mot-de-sens-inverse) ; les trois `mot-voisin` de 04/03-revision#1 retirés |

Non appliqués : m-8 (aucune action exigée) ; m-9 m020 Q2–Q4 (l'auditeur ne donne pas de texte de remplacement, seulement une option : réserve laissée à l'orchestrateur) ; m-10 et le libellé `suffixe-sans-regle-orthographique` (déjà faits par le pilote) ; m-11 et m-12 (hors défauts, à déclarer exercices parallèles voulus : 04 quiz#4 ↔ 04-defi#1, 02-boss#6 ↔ 05#6). Tags corrigés : mot-voisin du 04 = 6 ; m010 Q6 (pas Q5) porte `premier-mot-cle`. Taux final : 03 = 104/159 (65 %), 04 = 82/162 (51 %).
- m009 Q6 reformulé (plus de « feel loved » ni « right to », clé de m012 Q3) ; « loved and ___ for » seul ne livre pas « right ».

## Note du pilote (après re-vérification, 2026-10-18)

- **Exercices parallèles voulus** (déclarés) : 04 quiz#4 ↔ 04-defi#1 et 02-boss#6 ↔ 05#6 — même notion, gestes et contextes distincts ; `content:tranche` ne les compte plus comme paires proches.
- m008 Q7 : l'ordre qui fait foi est celui du fichier (e,a,c,f,b,d, lettres b et f permutées par rapport au texte de l'audit), juste et unique selon la re-vérification.
- Verdict de l'auditeur : **B2 prêt à armer**.
