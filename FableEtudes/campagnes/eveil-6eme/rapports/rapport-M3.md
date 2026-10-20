# Rapport M3 — éveil scientifique 6ᵉ, chapitres 04, 06, 05 (missions du gisement)

Auteur unique (les deux auteurs de la carte faits seul, chapitre après chapitre : 04, 06, 05). Skills : content-ecole-tn, content-engine, content-interactif, prof-eveil-primaire. Pas de git.

## Fichiers (10 missions, 91 questions)

| chapitre | fichier | étage | q. | carte |
| --- | --- | --- | ---: | --- |
| 04 | `exercices/06-exams-2018-2026-le-repas-equilibre-composer-et-justifier.json` | d3 boss 120/30 | 10 | m023 (10) |
| 04 | `exercices/07-exams-2010-2023-classer-les-aliments-et-leurs-roles.json` | d2 practice 75/15 | 9 | m024 (10) |
| 04 | `exercices/08-exams-2008-2024-carences-fer-vitamines-et-malnutrition.json` | d3 boss | 9 | m025 (12) |
| 04 | `exercices/09-devoir-petit-dejeuner-croissance-carence.json` | d2 | 7 | m026 (7) |
| 06 | `exercices/06-exams-2009-2017-pollinisation-abeille-fleur-et-protection.json` | d2 | 9 | m027 (9) |
| 06 | `exercices/07-exams-2009-2018-la-fleur-le-fruit-et-le-cycle.json` | d2 | 9 | m028 (9) |
| 05 | `exercices/06-exams-2016-2026-construire-et-corriger-une-chaine-alimentaire.json` | d3 boss | 11 | m029 (11) |
| 05 | `exercices/07-exams-2013-2024-producteurs-consommateurs-decomposeurs-et-milieu.json` | d2 | 12 | m030 (12) |
| 05 | `exercices/08-exams-2009-2026-eau-polluee-et-maladies-hydriques.json` | d3 boss | 12 | m031 (12) |
| 05 | `exercices/09-devoir-chaines-avec-lhomme-et-protection-du-milieu.json` | d2 | 7 | m032 (7) |

`chapter.json` des trois chapitres : ligne d'examen ajoutée à `sources[]` (04, 05, 06) et ligne devoir (04, 05). Numéros `06`–`09` : les chapitres avaient bien `01`–`05` (mis à niveau, cours au patron), pas de décalage. Les « ne pas redemander » ont été refaits question par question sur le cours et les 6 fichiers de chaque chapitre tels qu'ils sont aujourd'hui.

## Gates (depuis `/home/user/eng-deliver`)

- `content:check` : vert (eveil 12 chapitres, 96 exercices, 794 questions).
- `content:qa -- --subject eveil-scientifique-6eme` : **0 erreur sur mes fichiers** ; 3 erreurs qui nomment `12-dhaw/06-exams-2016-2017-refraction-…` (balises `**` dans un énoncé) — ce n'est pas mon lot.
- `content:figures:check` : vert.
- `content:tranche … --fresh --strict-longest --strict-lessons` : clé la plus longue 0/109 ; positions de clé 23/28/28/21 % ; patron de notion 0 en recul ; **1 paire proche (0,45)** : m023 Q8 ↔ Q9 (même diagramme, deux repas : exercice parallèle voulu, mêmes données officielles, autre question). Aucun gabarit.
- `lot-lint.mjs` : rien à signaler. `prettier --check` : vert. Tous les SVG rendus dans Chromium `dir=rtl` et relus (légendes en `text-anchor="middle"` partout : en page RTL `end` se lit à gauche du point, d'où ce choix).

## ⚠ Constat de départ

Les transcriptions `content/programmes-officiels/examens-nationaux/6eme-base/eveil/<année>-unique.md` **n'existent pas dans le worktree** (dossier absent). Tous les sujets ont donc été relus en vision sur les PDF (`/tmp/claude-0/ev6g/src/<année>-svt.pdf`, 150 dpi, zooms ponctuels) ; les consignes reprises sont celles imprimées. Divergence avec la carte : le support 2023 (m024) liste **sept** aliments (jaune d'œuf compris : جبن، بيض، خبز، زبدة، خسّ، برتقال، زيت زيتون), pas six.

## Lignes reprises (examens)

Toutes les lignes des cartes M3 sont reprises sauf celles que « Écarts à la carte » nomme : m023 (C03#1, C08#3, C09#4, C01#12, C05#12), m024 (C04#4–#5, C07#11–#12, C17#4a, C06#3), m025 (C04#6, C05#13, C19#3a, C03#4, C07#2, C06#1), m027 (C10#1b, C14#1a, C12#7a, C15#3a, C18#1b), m028 (C17#2a, C18#1a, C09#1–#2, C10#1a), m029 (C01#9, C02#9, C04#12, C11#3a–#3b, C03#12, C08#13), m030 (C05#9, C08#14–#16, C14#1b, C04#13, C06#13, C06#7, C03#13), m031 (C05#8, C03#14–#15, C01#7, C04#14, C08#12, C06#8, C18#2a) ; devoirs m026 (D04#5, #6, #9, #11, D06#1, #2, #8) et m032 (D07#1–#3).

## Défauts d'énoncé corrigés dans la reprise (l'explication ou le texte le dit)

- 2024 chaîne « غذاء لـ » (m029 matching) : normalisée sur « يتغذّى على », l'explication dit que ce sont les mêmes liens, flèche inversée.
- 2016 chaîne (m029) : lue comme imprimée (flèches vers la gauche, bactéries à droite). Avec « يتغذّى على », la correction est l'échange souris/serpent : **بكتيريا ← أفعى ← فأر ← سنبلة** (la bactérie mange les restes du dernier maillon, elle reste en tête dans l'écriture « du mangeur vers l'aliment »). Les bactéries sont de même placées en tête en 2019 (ordering) avec la phrase « elles mangent le cadavre du faucon » dans l'énoncé.
- 2023 chaîne de Chadi (m029) : j'ai relu l'image à 300 dpi : les pointes des flèches vont vers la droite, donc « papillon mange grenouille, grenouille mange serpent, serpent mange ver ». Plusieurs chaînes sont possibles avec les sept êtres : les trois relations observées (criquet / blé, grenouille / criquet, serpent / grenouille) sont **données dans l'énoncé** pour fixer la clé unique.
- 2024 potabilisation (m031) : lecture de schéma (schéma refait, de droite à gauche) ; V4 respecté, aucune question n'exige de connaître l'ordre.
- 2024 symptômes communs (m031) : ni le jaunissement des yeux ni la douleur intestinale ne sont communs (typhoïde et jaunisse partagent fièvre et maux de tête) ; clé fièvre + maux de tête.
- 2021 tableau d'analyses (m025) : relu au PDF : la valeur usuelle de la vitamine D est « 30 ≤ » (**≥ 30**, lecture droite-gauche) et le résultat 20 est sous la norme ; les cinq autres lignes sont dans la norme. Tableau refait en SVG, B1 et B12 uniquement lues, jamais clé.
- 2015 (m027) : dans le sujet le sac enferme toute la fleur, étamines comprises, donc l'autopollinisation resterait possible. Figure refaite : sac autour du pistil seul, fleur 3 sans étamines, fleurs isolées (dit dans l'énoncé) ; une seule situation permet pollinisation et fécondation.
- 2018 : « متبر » écrit « مئبر » (jamais reprise) ; 2021 et 2024 : « الهزال الرزّي » **jamais écrit** (la phrase est refaite avec « فقر الدم » ou « الكساح »). 2023 : le trouble de la vue est donné (« العشى الليلي »), jamais demandé.
- 2013 : la question « quelle fleur est pollinisée » est reprise ; la question de justification est remplacée (voir « Écarts ») pour ne pas redoubler `06/02-boss#7`.

## Écarts à la carte (à lire avant d'armer)

- **m024 : 9 q au lieu de 10.** La question « pois chiche → protéines » doublait `04/02-boss#1` ; le matching la garde dans l'appariement, la QCM porte le persil. 2021 : une seule QCM à deux blancs (la seconde doublait `04/quiz#1`). L'appariement 2010 est devenu un `multi` (cinq aliments, trois groupes : pas de bijection possible).
- **m025 : 9 q au lieu de 12.** Pas de deuxième question pour 2023, 2022 ni 2024 sans redoubler `04/05-entrainement#5` / `04/04-defi#1` ; 2021 en deux.
- **m026 (devoir)** : recoupe beaucoup le patron (`01-pratique#8`, `quiz#4`, `02-boss#5`, `04-defi#5`) ; j'ai gardé 7 q avec contextes neufs, les gestes neufs étant la correction en deux temps (définition de l'énergie, besoin de l'enfant, vitamines/protéines intervertis). **Candidate à la coupe en premier** (E-1).
- m027 Q4/Q5 recoupent `06/02-boss#7` (sac sur le stigmate) : Q4 est la reprise officielle (la carte l'exige), Q5 prend un autre angle (retrait du plastique). `chapter.json` ne porte aucune étiquette neuve (coursePitfalls inchangés).
- m030 / m028 (« milieu ») : le cours 05 ne définit pas le milieu ni vivant/non vivant : c'est le cours **5ᵉ** (`09-vivants-milieu`) qui les enseigne ; l'énoncé glose « الكائنات الدقيقة » (chapitre 10 plus loin) ; les bactéries sont tenues pour vivantes (cours 05, « الكائنات المفكّكة »).
- Le cours 04 ne dit pas « le fer entre dans les globules rouges » : m025 s'appuie sur « fer manquant → anémie = peu de globules rouges » (cours 03). La distinction « sel minéral / matière organique » (m025 Q2) s'appuie sur le nom « أملاح معدنيّة » ; « عضويّة » n'est enseigné qu'au 05 (suivant). À juger par l'auditeur.

## Étiquettes `eveil.*` employées

`eveil.nutri.` : `origine-et-groupe-confondus`, `quantite-au-lieu-de-variete`, `vitamines-donnent-energie`, `maladies-de-carence-confondues`, `un-seul-groupe-suffit`, `malnutrition-seulement-par-manque` (en `expectedMistakes`). `eveil.sang.roles-globules-rouges-blancs-inverses`. `eveil.flor.` : `pollinisation-et-fecondation-confondues`, `type-pollinisation-par-l-agent`, `fruit-sans-pollinisation`, `fleur-entiere-devient-fruit`, `organes-protecteurs-et-reproducteurs-confondus`. `eveil.eco.` : `fleche-lue-a-l-envers`, `rang-du-consommateur-mal-compte`, `champignon-producteur`, `eau-polluee-seulement-si-bue`, `eau-limpide-donc-potable`, `virus-et-bacterie-confondus`. Aucune sur `multi`, `ordering`, `matching` ; aucune option à deux erreurs étiquetée.

## Ids manquants (non posés, à juger)

Jamais inventés ; laissés muets. Sous le seuil des 3 questions sauf le premier :
- `eveil.nutri.proteines-protegent` — « tu attribues aux protéines le rôle de protection » (C07#12) : options muettes en m024 Q6–Q7 et m026 Q6 (≥ 3 occurrences).
- `eveil.nutri.aliment-pris-pour-groupe` (C08#3), `eveil.flor.protection-ignoree` (C14#1a, m027 Q4), `eveil.eco.sterilisation-avant-filtrage` (C03#15, m031 Q4), `eveil.eco.polluants-air-pris-pour-eau` (C03#14, m031 Q1 en multi).

## Double résolution et passe adversariale

Chaque question a été résolue deux fois : sur le sujet (PDF) puis sur les options du fichier (le contrôle automatique des clés les plus longues et le rendu SVG ont servi de relecture). Les distracteurs ont été relus un à un : chacun est faux pour la raison que son étiquette nomme. Les explications ne citent aucune lettre d'option ni ordinal. Pas de valeur du ملفّ en clé ; les pourcentages du diagramme 2026 et du tableau 2021 ne servent que de support, jamais de réponse. Les « ne pas redemander » 04 (13 refs), 05, 06 ont été remplacés par un croisement sur le contenu réel.

## Doutes pour l'audit

1. 2016 et 2019 : place des bactéries. Si le corrigé officiel les met en fin de chaîne (flèche « غذاء لـ »), ma lecture « en tête » (flèche vers l'aliment) est la même chaîne écrite à l'envers ; elle est dite dans l'énoncé.
2. Les cours 5ᵉ (`09-vivants-milieu`) écrivent la flèche **vers le mangeur**, le 6ᵉ vers l'aliment : chaque énoncé de chaîne pose la convention ; sans correction du 5ᵉ, un élève peut hésiter.
3. m023 Q3 (« quel groupe manque ? ») voisine `04/02-boss#4` : même geste, données officielles de 2019, demandé par la carte.
4. m031 Q1 (multi « polluants des milieux aquatiques ») ajoute deux polluants de l'air comme faux : à valider contre la fiche (aucun ◐).
