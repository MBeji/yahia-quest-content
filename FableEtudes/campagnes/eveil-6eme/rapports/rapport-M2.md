# Rapport du lot M2 — éveil scientifique 6ᵉ, chapitres `02`, `03`, `10` (missions du gisement)

Auteur unique du lot (3 chapitres). 10 missions, **69 questions** (carte : 90) : 42 QCM, 11 appariements, 10 `multi`, 5 `ordering`, 1 `short_answer`. Étiquettes posées : 20 distracteurs sur des ids existants du registre. Aucune retouche à `content/misconceptions.json`, `content/competences/`, ni aux cours/exercices existants. Seul changement hors des nouveaux fichiers : `sources[]` des trois `chapter.json` (ligne d'examen aux trois ; ligne de devoir aux `03` et `10`).

## Source : les transcriptions n'existent pas dans l'arbre

`content/programmes-officiels/examens-nationaux/6eme-base/eveil/` est **absent** (seuls `english`, `french`, `math`). Comme la consigne le permet en cas de doute, j'ai lu **les PDF `/tmp/claude-0/ev6g/src/<année>-svt.pdf` à l'image** (pdftoppm 130 dpi) pour toutes les sessions reprises (2008, 2010, 2012, 2013, 2015–2026), pas seulement en cas de doute. Les phrases officielles sont donc lues sur l'image, pas sur une transcription versionnée : à vérifier si une transcription arrive. Aucun devoir ni snapshot lu (m020, m022 : la carte seule).

## Fichiers (étage, nombre de questions)

| fichier | étage | q. | sessions reprises |
| --- | --- | ---: | --- |
| `02-respiration/exercices/06-exam-2016-de-lair-aux-cellules-le-trajet-de-loxygene.json` (m013) | d3 boss | 7 | 2016 supports 1 et 2 |
| `02-respiration/exercices/07-exams-2010-2026-alveole-air-expire-et-dioxyde-de-carbone.json` (m014) | d2 | 8 | 2026, 2020, 2018, 2015, 2010 |
| `03-sang-circulation/exercices/06-exam-2025-le-depliant-du-don-de-sang.json` (m015) | d3 boss | 7 | 2025 situation 2 |
| `03-sang-circulation/exercices/07-exams-2015-2024-deux-circuits-deux-couleurs.json` (m016) | d2 | 8 | 2022, 2024, 2015 |
| `03-sang-circulation/exercices/08-exams-2019-2026-vaisseaux-sens-du-sang-et-trajet.json` (m017) | d2 | 7 | 2019, 2020, 2021, 2023, 2026 |
| `03-sang-circulation/exercices/09-exams-2019-2026-composants-du-sang-frottis-et-fonctions.json` (m018) | d2 | 6 | 2019, 2020, 2021, 2026 |
| `03-sang-circulation/exercices/10-exams-2008-2025-globules-coagulation-et-anemie.json` (m019) | d2 | 6 | 2008, 2012, 2013, 2023, 2024, 2025 |
| `03-sang-circulation/exercices/11-devoir-sang-coeur-tubes-et-fonctions.json` (m020, devoir) | d2 | 8 | carte D04/D05 seule |
| `10-microbes-defense/exercices/06-exams-2013-2018-plaie-vaccin-serum-et-defense.json` (m021) | d2 | 5 | 2013, 2015, 2017, 2018 |
| `10-microbes-defense/exercices/07-devoir-plaie-infection-et-conseils.json` (m022, devoir) | d2 | 7 | carte D05–D08 seule |

Numéros de fichiers `06` à suivre : `01`–`05` existent bien dans les trois chapitres, aucun décalage. Rewards d3 120/30, d2 75/15 (carte). Chaque question d'examen dit sa session et reprend la consigne imprimée.

## Revérification E-12 (état au 2026-10-20 après mise à niveau)

Cours et exercices relus question par question. Le cours `03` enseigne bien les plaquettes et le sang décanté ; le `02` et le `01` le monoxyde de carbone ; le `10` le sérum antitétanique, le vaccin et les trois formes de défense. Rien n'arrête un lot. Questions de la carte **non reprises** parce qu'elles doublent un item existant (liste « ne pas redemander » mise à jour) :
- m014 : QCM « résultat de l'eau de chaux » (= `02/02-boss#3`, `02/05#1`) et « qui transporte les aliments ? » (= `03/05#6`) ; l'appariement 2015 devient un appariement à trois lignes (le QCM à blancs se réduisait à un 2×2 sur deux gaz).
- m019 : 2013 (3-1) « le saignement s'arrête » (= `03/01-pratique#6`), 2008 (1) tableau composants ↔ fonctions (= m018 Q2 et `03/05#4`), 2012 « propriété piège : le noyau » (= `03/quiz#3`), 2024 3ᵉ ligne « plasma transporteur de déchets » (= `03/04-defi#4`, remplacée par la ligne « caillot »).
- m015 : l'`ordering` du circuit du sang (= `03/02-boss#8`) est devenu un QCM visuel (quatre dessins) ; pas de 2ᵉ QCM sur la forme du globule rouge (= `03/02-boss#1`).
- m022 : pas de QCM redondant sur les phases (l'ordering seul) ; pas de conseil sur l'eau (renvoyé au `05` comme la carte).
Les doublons restants sont des reprises d'examen voulues (même savoir, forme de l'épreuve) ; voir « paires proches ».

## Défauts d'énoncé corrigés dans la reprise (l'explication le dit quand il y a lieu)

- **2013 (m021 Q5)** : « مصل مضادّ للشلل » pour une plaie : l'énoncé ajoute que le sol a souillé la plaie, la bonne réponse est le sérum antitétanique, l'explication signale l'ajout.
- **2020 (m017 Q6)** : la chaîne imprimée est fausse (« الأذينة اليمنى ») : la mission demande l'ordre juste en quatre temps.
- **2020 et 2024 (« 55 % »)** : remplacé par « سائل مصفرّ يشغل الجزء الأكبر من الدّم » (m018 Q2) et « سائل مصفرّ يعلو الكريّات في الدّم المترسّب » (m019 Q3), V1. 2020 « تتكوّن في نخاع العظم » (ambiguë : toutes les cellules du sang s'y forment) remplacée par « لونها هو الّذي يعطي الدّم لونه الأحمر ».
- **2015 (m021 Q4)** : « العقد اللّمفاويّة » (◐) remplacée par « الكريّات البيضاء وبلعمتها للجراثيم ».
- **2018 (m014 Q7)** : « هواء مشبع بالأكسجين » n'est pas repris comme clé ; la cause retenue (fumée et suie dans les voies respiratoires) ne dit rien du manque d'oxygène.
- **2015 (m016 Q6)** : le premier énoncé est JUSTE ; une option « لا خطأ » est la clé.
- Les pourcentages 21 et 13 de 2016 sont donnés comme lectures du capteur, jamais comme clé ni distracteur. Aucun autre chiffre du ملفّ.

## Écarts à la carte à signaler

1. **Moins de questions** (69 au lieu de 90) : doublons ci-dessus, et des étapes qui se réduisaient à un 2×2 trivial.
2. **m013 Q5** : le schéma (ب) est refait en quatre trajets fléchés (QCM visuel) au lieu d'un `ordering` seul (les deux sont là).
3. **m017 (ordering, chaîne cardiaque)** : exige les noms « أذينة » et « بطين » : ils sont dans le sujet 2020 et la carte les autorise, mais l'anatomie des cavités est un acquis de 5ᵉ (le cours `03` ne les nomme pas). À arbitrer : si le pilote veut la mission « sans anatomie », retirer cette question (Q6) et la mention « الأذين » de Q4.
4. **Cartes d'entête** : 2024 « situation 2 » (m016, m019) est en réalité la situation 1, support 2 (page 1 du PDF). Les missions citent « الوضعيّة الأولى ».
5. **m014** contient une `short_answer` (« ماء الجير »), 1 question sur 8 (< 1/3), `acceptedAnswers` posés.
6. **Pas de question sur le schéma d'œil (2012, 2018)** : hors lot.

## Figures (SVG, vérifiées au rendu Chromium `dir=rtl`)

Toutes refaites : cloche à fenêtre (m013 Q1), trajets fléchés (m013 Q6), échange à la cellule (m013 Q5), alvéole (m014 Q4–Q5), quatre circuits colorés (m015 Q6), deux circuits (m016 Q3), deux tubes (m016 Q1), frottis (m018 Q1, Q3, Q5), schéma du cœur (m020 Q1–Q2), quatre tubes en options (m020 Q3). Étiquettes en ancrage `middle` uniquement (pas de risque d'inversion en RTL). Aucune clé donnée : les couleurs des flèches de m015 Q6 ne sont pas associées à des gaz dans l'énoncé ; les panneaux sont à 2×2 (chaque couleur juste et fausse figure deux fois).

## Étiquettes

Employées (20 distracteurs) : `eveil.resp.sens-echanges-gazeux-inverse` ×4, `eveil.gaz.test-mal-associe` ×2, `eveil.sang.caracteres-globules-inverses` ×2, `eveil.microbes.vaccin-pris-pour-medicament` ×2, `eveil.microbes.eau-suffit-pour-la-plaie` ×2, puis une fois `eveil.resp.coeur-organe-respiration`, `eveil.resp.poumons-fabriquent-oxygene`, `eveil.resp.inspiration-expiration-confondues`, `eveil.sang.roles-globules-rouges-blancs-inverses`, `eveil.sang.plasma-et-serum-confondus`, `eveil.microbes.infection-attribuee-au-dernier-geste`. Aucune sur `multi`, `ordering`, `matching`. Les options à deux erreurs (grilles 2×2) restent muettes.

**Ids manquants à proposer** (non posés) :
- `eveil.sang.nom-du-vaisseau-par-la-couleur` — « tu nommes le vaisseau par la couleur de son sang : artère ou veine se dit selon le sens (du cœur ou vers le cœur) » — ≥ 3 questions (m015 Q2 et Q5, m017 Q2, m020 Q1–Q2).
- `eveil.sang.couleur-selon-le-sens-inversee` — « tu inverses les couleurs : le sang qui va du cœur aux poumons est foncé, celui qui y revient est vif » — m015 Q1 et Q6, m016 Q3 (≥ 3).
- `eveil.sang.coagule-et-decante-confondus` — « tu confonds sang coagulé (caillot + liquide jaune autour) et sang décanté (plasma au-dessus des cellules) » — m016 Q1–Q2, m020 Q3 (≥ 3).
- Sous le seuil (une ou deux occurrences, laissées muettes) : suie qui passe dans le sang (m014 Q7), gaz consommé pris pour le gaz produit (m013 Q1), coagulation attribuée aux globules blancs (m018 Q6).

## Gates (depuis `/home/user/eng-deliver`)

- `content:check` : ✓ (121 sujets, 31 627 questions).
- `content:qa -- --subject eveil-scientifique-6eme` : **0 erreur, 0 avertissement sur mes fichiers**. 3 erreurs « Markdown dans un énoncé » signalées sur `12-dhaw/06-exams-2016-2017-refraction-definition-et-rayons` (Q1–Q3) : **pas de moi**, à corriger par l'auteur du lot M1.
- `content:figures:check` : ✓.
- `content:tranche … --fresh --strict-longest --strict-lessons` : clé strictement la plus longue 0/104 ; positions de clé 20 / 26 / 28 / 27 % ; cours au patron : 0 en recul. Paires proches (Jaccard ≥ 0,45), **trois**, justifiées : m014 Q1 ↔ Q8 (deux moitiés de la même phrase de 2026), m021 Q2 ↔ Q3 (même énoncé de 2018, un QCM de la forme corrigée et un `multi` des erreurs), m015 Q1 ↔ Q5 (deux vaisseaux de la même situation).
- `lot-lint.mjs` : rien à signaler.
- `prettier --write` puis `--check` : ✓ (13 fichiers).
- `content:gisement:controle` (devoirs m020, m022) : 0 plage de 8 mots, 0 exercice dont on reprenne trois données.

## Doute / à regarder

- Les nombreux 2×2 « couleur × gaz » se ressemblent d'une mission à l'autre (m014, m015, m016, m017, m020) : c'est le savoir le plus servi des sujets, mais l'auditeur du gabarit pourra proposer de retirer m016 Q4 (`explication de la couleur`) si le pilote veut alléger.
- `m018 Q2` : « نقل المغذّيات والأدوية » : les « médicaments » ne sont pas au cours `03` (reprise littérale du sujet 2026).
- Aucun commit, aucun push, aucun `git` modifiant l'état.
