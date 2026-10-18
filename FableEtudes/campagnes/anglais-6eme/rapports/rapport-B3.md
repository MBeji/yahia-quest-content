# Rapport B3 — anglais 6ᵉ, chapitres 05-celebrations et 06-going-shopping

Auteur B3, 2026-10-18. Gates : `content:check` 0 erreur ; `content:qa -- --subject english-6eme` 0 erreur sur mes fichiers (une erreur hors lot : `01-entertaining-myself/09-exam-2023-reading-drawing-competition` Q1, explication qui désigne une option par sa place, vue à mi-parcours — lot B1) ; `content:tranche` (chapitres 05, 06, puis `--changed --fresh --strict-longest`) : clé la plus longue 0, paires proches 0 ; `lot-lint` : rien à signaler sur les 6 missions. `content:catalogue` non lancé (fichier partagé, à régénérer par le pilote).

## Fichiers

Créés (6 missions) :
- `05-celebrations/exercices/06-exams-2023-2026-simple-past.json` (m012, boss d3 120/30, 10 questions : 7 QCM, 1 ordering, 2 short_answer)
- `05-celebrations/exercices/07-exam-2021-reading-end-of-year-party.json` (m013, practice d2, 6 QCM)
- `05-celebrations/exercices/08-exam-2021-writing-birthday-party.json` (m014, practice d2, 6 : 4 QCM, 1 matching, 1 multi)
- `06-going-shopping/exercices/06-exams-2010-2025-at-the-shop.json` (m015, practice d2, 9 : 7 QCM dont un à figure SVG, 2 matching)
- `06-going-shopping/exercices/07-exam-2024-reading-lost-at-the-mall.json` (m016, practice d2, 7 QCM)
- `06-going-shopping/exercices/08-exam-2025-writing-shopping-day.json` (m017, boss d3 120/30, 8 : 5 QCM, 1 matching, 1 multi, 1 ordering)

Modifiés : `chapter.json` des deux chapitres (`coursePitfalls` + ligne `sources[]` des examens ; pas de `coursePitfalls` ajouté au-delà de la carte, ni `coursePattern`, ni `manuel`) ; les `quiz.json` et les 5 exercices existants de chaque chapitre (étiquettes, défauts). `content/misconceptions.json` non touché ; aucun id neuf posé par moi (l'étape (1) était faite).

## Étiquetage (distracteurs QCM étiquetés / distracteurs QCM)

| chapitre | avant | existants après | missions neuves | total après |
| --- | ---: | ---: | ---: | ---: |
| 05 | 0 / 105 | 52 / 105 (50 %) | 28 / 51 (55 %) | 80 / 156 (51 %) |
| 06 | 0 / 105 | 52 / 105 (50 %) | 34 / 57 (60 %) | 86 / 162 (53 %) |

Sous les 60 % des deux chapitres : voulu et honnête (E7 sous condition du pilote). Règles tenues : aucune étiquette sur `multi`/`ordering`/`matching` ; une option à deux erreurs reste muette ; une forme présente sans -s non accordé au sujet (« My father pay ») reste muette (présent + accord) alors que celle qui s'accorde (« My father pays ») prend `present-avec-marqueur-passe` ; `mot-voisin-du-meme-champ` seulement quand l'énoncé tranche (jamais sur « puts on the balloon », « waits for the balloon », « a clown », « tired/sick/alone », « free », « new »). Muets assumés notables : « loveed/lovd/loves », « hugged/played » comme /t/, les trois « Three of these … which does NOT » (l'élève qui les choisit croit un verbe régulier irrégulier : pas d'entrée au registre), les prépositions in/on du coin (`02-boss#3`), les nombres 916/960/9006 et 120/420/920.

Erreur d'élève des muets de mission (une phrase) : m012 « will + passé » (futur avec marqueur du passé, `will choose`, `will sing`, `will thank`, `will prefer`) ; m013 « Adam et Tina échangés » (rôles inversés), « 11 o'clock » (9 h + 2 h) ; m014 « Dear Sami / Yours, Patricia » (destinataire et signataire inversés, plan 2×2) ; m015 « Goodbye, madam / See you tomorrow » (formule de fin au début de l'échange), « at the bank », « between + un seul lieu » ; m016 « Alex told his mother… » ; m017 « The shop is closed for a few days » (confusion offre / fermeture).

## Défauts `content:tranche` corrigés

- 05 : clé la plus longue 3 → 0 (`quiz#3` remplacée par « my grandmother ___ a big cake » made/make/makes/maked ; `01-pratique#1` : distracteur « the end of school year party » ; `03-revision#2` : distracteurs rallongés). Paires proches 7 → 0 : `01-pratique#3` (quatre enfants, sujets I/She/We/They), `02-boss#2` (« You ___ … and he ___ … »), `03-revision#6` (« même son que talked »), `05-entrainement#6` (« comment sonne le -ed de danced ? »), `quiz#3` (voir plus haut).
- 06 : clé la plus longue 9 → 0 (un seul distracteur rallongé par question, `quiz#2` « really do », `quiz#5` « buying », `01-pratique#2/#3`, `02-boss#5`, `03-revision#1/#2/#3`, `05-entrainement#6`). Paires 2 → 0 : `01-pratique#1` (« Which of these is the name of a shop? »), `quiz#3` du 05 réécrite. Gabarit `04-defi#1` : consigne varie (« Four sentences talk about prices and crowds. Which one contains a mistake? »).
- Fuite de clé corrigée au passage : `05/04-defi#2` donnait « wrote » et « prepared » (clés de m012 et de `03#3`/`05-entrainement#3`) et « bought » (clé de `06/quiz#5`) dans son énoncé ; réécrit en gave / sent / cooked.
- Aucune ligne de `difficulty` d'une question existante n'a bougé (les identifiants publiés restent stables).

## Écarts à la carte

- m012 : 10 questions au lieu de 11 (les huit items listés en donnent dix ; rien d'inventé). L'item 2025 « right » (`have the right to`, U-V L1) est la 3ᵉ question.
- m015 : 9 questions comme la carte, mais l'appariement 2012 devient deux QCM (postcards, between) : le `matching` natif exige une bijection (2–6 gauches, autant de droites), l'« option en trop » du sujet n'est donc pas portable. Même raison : 2018 passe à 3 paires (« some sugar » écarté), 2024 passe à 4 paires sur les fonctions de la réplique (ex. : « the customer says which books he wants ») au lieu des quatre cercles numérotés, et l'intrus ③ « Science books are on the right » n'est pas repris.
- m016 : 7 questions dont une, « scared » (sens du mot, `read.sens-du-mot-sans-contexte`), et une, « him » (référent), ne sont pas des items du sujet ; elles prennent la place de « Tick (√) » et des « deux mots » regroupés en une seule question à paires (funzone / coffee). Le vrai/faux a été scindé en deux questions « verdict + preuve » (2×2 : verdict × phrase).
- m013 : le vrai/faux « Mr Jack is our Maths teacher » (coquille du sujet) est remplacé par « Why does the Maths teacher come… » ; « Mr John » n'entre dans aucune option. Le cloze est converti en questions de lecture sur la ou les phrases citées (le texte n'est pas au portail).
- m014 : consigne officielle au présent continu, mission au présent simple (« The e-mail is written on the day of the party, so Sami uses the present simple »), sans exiger le continu.
- Figure SVG (m015 Q4, « computer ___ the teacher's desk ») : ajoutée pour retirer `at` ; sans elle, « at the teacher's desk » est juste en anglais standard et l'item du sujet est ambigu.
- Item officiel adapté pour ne pas livrer de clé voisine : 2024 « found a handbag » devient « saw a handbag » (« found » est la clé de m012 Q9) ; « celebrated Teachers' Day » devient « organised a party » (clé de `03-revision#4`) ; « Children's Day is a special celebration » est retiré du cloze « right » (clé de `01-pratique#1`).

## Notions données dans l'énoncé

- m015 Q8 : `put on` ≈ `wear` : `wear` n'est pas au cours du 06 ; le sens est porté par la phrase (« The children put on their best clothes for the school party ») et les distracteurs (`try on`, `take off`, `buy`) sont des mots du cours.
- m012 Q7 : `preferred` (r doublé) n'est pas dans la règle du cours (verbes courts) ; la question ne teste que le temps (distracteurs sans « prefered »), l'explication note le r double sans en faire un objet.
- m012 Q8/Q10 (`short_answer`) : forme unique et `expectedMistakes` (finded, find / drinked, drink) ; l'explication ne contient pas la réponse.

## Doutes pour l'auditeur

- Fuites de clés entre fichiers du chapitre, tolérées par le plan : les verbes irréguliers du 05 et du 06 sont si peu nombreux que chaque forme réapparaît ailleurs (m012 `wrote`/`drank`/`prepared` vs `02-boss#4`, `05-entrainement#5`, `03-revision#3` ; m017 multi : `bought`, `went`, `chose`, `tried on` vs `quiz#5`, `04-defi#3`, `05-entrainement#5`). Les énoncés, eux, ne livrent plus de clé voisine.
- m012 Q3 (« right ») et `04-caring/…/06-exams-2023-2025-superlative-and-jobs#6` (« cared for ») viennent du même exercice 2025 : le blanc est différent, les distracteurs aussi (« caring » seul commun).
- m013 Q3 : « Tina » est une fille de la classe, donc le vrai du sujet repose sur une déduction (les filles portent jupe rose et chemise jaune) ; la phrase du sujet ne nomme pas Tina.
- m013 Q1, Q4, Q5 et m016 : plusieurs distracteurs `read.reponse-sans-appui-dans-le-texte` sont des affirmations inventées (plausibles mais absentes du texte) ; si l'auditeur juge l'étiquette trop large pour des options contredites par le texte, les passer muettes (−12 environ).
- m017 Q7 (ordering) s'appuie sur les moments de la journée (morning, noon, afternoon, evening), choisis pour qu'une seule suite soit possible (Then / After that ne l'assurent pas).
- m015 Q5 : « at the bookshop » repose sur un savoir de monde (où l'on achète des cartes postales), comme dans le sujet ; « at the bank » reste muet.
- Gabarit inter-chapitres : aucun groupe restant sur mes deux chapitres.
