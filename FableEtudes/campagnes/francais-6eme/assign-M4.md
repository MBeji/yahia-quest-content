# Carte d'affectation M4 — français 6ᵉ, chapitres 07, 08 (missions du gisement)

> Lot auteur du passage unique (PLAN.md ; PLAN-gisement.md § 4). 9 missions. Skills : `content-ecole-tn`, puis `content-langue-francais` pour le registre de langue, `prof-francais-college` pour calibrer les étages `d3` seulement (sans en reprendre le programme de 7ᵉ–8ᵉ) ; consignes `content-ingest/references/gisement-auteur-examen.md` (missions d'examen, avec la transcription de chaque session citée : `content/programmes-officiels/examens-nationaux/6eme-base/french/<année>-unique.md`) et `gisement-auteur-devoir.md` (missions 📝 : la carte seule, jamais le devoir). Ne touche à aucun autre chapitre que les tiens ; les autres lots écrivent en parallèle. **Deux auteurs en parallèle** (un par chapitre : 07 / 08), chapitres disjoints.

**Règles communes** (PLAN-gisement.md § 1) : chaque question dit sa session (« Concours 2023 ») et redonne la phrase OFFICIELLE de la transcription (consigne et énoncé tels qu'imprimés, coquilles incluses) ; une réécriture « Réécris … » devient « quelle réécriture est correcte ? » (QCM de formes) ou un matching/ordering ; un blanc `HP:` est DONNÉ rempli, jamais demandé ; une forme d'un verbe d'un chapitre ultérieur est donnée dans les options quand elle n'est pas la cible ; jamais de corrigé de site tiers : l'explication est la tienne, re-résolue. Étiquettes : vocabulaire `fr.*` du lot A (`vocab-french-6eme.json`), sur les distracteurs qui disent l'erreur du « piège » de la ligne, jamais sur multi/ordering/matching ; les ids neufs ou élargis que tu poses vont dans `content/misconceptions.json`. `chapter.json` : ajoute à `sources[]` la ligne « Sujets officiels du concours d'entrée aux collèges pilotes (6ᵉ année de base), Ministère de l'Éducation (corpus officiel, reprise citée, étude 36) — transcriptions : programmes-officiels/examens-nationaux/6eme-base/french/ » (missions d'examen).

**Ordre de travail** : (1) les ids d'étiquette neufs que tu poses ; (2) les missions, dans l'ordre de la carte ; (3) gates à chaque chapitre : `content:check`, `content:qa -- --subject french-6eme` (0 erreur), `content:tranche -- --subject french-6eme --changed --fresh --strict-longest`. Numéros de fichiers : à la suite de `05-entrainement` (06, 07, …) ; `displayOrder` à la suite.


## Chapitre `07-profiter-du-temps-libre`

### Missions (gisement)

#### m025 → `exercices/06-exams-2012-2018-quand-dire-et-ecrire.json` · d2 practice 75/15 · 7 questions · régime **examen**

- Titre : « 🏛️ Concours 2012–2018 · le complément de temps — dire et écrire ⭐⭐ »
- Registre : id `C09#10` ; sources `C09#10, C10#4, C11#6, C15#7`
- Sources (base en premier) : C09 (2018) ex. 10 ; C10 (2017) ex. 4 ; C11 (2016) ex. 6 ; C15 (2012) ex. 7
- Items :
  - 2017 gram. 1 : « Après la lecture de la lettre, quelques élèves ont lancé des regards gênés. » — tableau « le sujet / le complément essentiel / le complément de temps » en matching — 1 q.
    - piège (étiquette à porter par un distracteur) : prendre un complément de temps pour un essentiel — ligne C10#4 (d2)
  - 2016 gram. 2 : « Les crayons de couleurs se disputent. » — « réécris la phrase en ajoutant un complément de temps et un complément de lieu » : QCM de la phrase enrichie, QCM « quel groupe est le complément de temps » (leurre : confondre lieu et temps) — 2 q.
    - piège (étiquette à porter par un distracteur) : confondre complément de lieu et de temps — ligne C11#6 (d2)
  - 2012 gram. 3 : Emir dit : « J'ai réussi à attraper beaucoup d'oiseaux à l'aide de mon filet. » devient « Les enfants … : « … à attraper beaucoup d'oiseaux à l'aide de … filets. » » — QCM « disent », QCM « nos » (« Nous avons réussi » est donné) — 2 q.
    - piège (étiquette à porter par un distracteur) : garder la personne ou le possessif d'origine — ligne C15#7 (d3)
  - 2018 conj. 2 : « Ecoutez puis écrivez la phrase ! dit la maîtresse à ses élèves. » dit à Ousman — QCM « Ecoute puis écris la phrase » (le s de « écris » seul) — 2 q.
    - piège (étiquette à porter par un distracteur) : garder la terminaison du pluriel — ligne C09#10 (d2)
- Ne pas redemander : `07/quiz#1`, `07/quiz#2`, `07/quiz#4`, `07/01-pratique#1`, `07/01-pratique#2`, `07/01-pratique#3`, `07/02-boss#1`, `07/02-boss#2`, `07/02-boss#5`, `07/03-revision#1`, `07/04-defi#1`
- Note : Deux familles minces fusionnées : complément de temps (deux lignes), dire / écrire (deux lignes). Les compléments de manière et de lieu sont dans la mission de tableau du `08` ; C15#7 cumule 01, 02, 04 et 07 (placement le plus avancé).

#### m026 → `exercices/07-exams-2010-2026-adjectifs-au-feminin.json` · d2 practice 75/15 · 8 questions · régime **examen**

- Titre : « 🏛️ Concours 2010–2026 · nul / nulle, bon / bonne, gros / grosse : la consonne qui double ⭐⭐ »
- Registre : id `C01#8` ; sources `C01#8, C08#6, C12#5, C17#6`
- Sources (base en premier) : C01 (2026) ex. 8 ; C08 (2019) ex. 6 ; C12 (2015) ex. 5 ; C17 (2010) ex. 6
- Items :
  - 2026 gram. 3 : « Je sais qui vient de prononcer cette phrase complètement nulle. » devient « … cet énoncé complètement … » — QCM « nul » (« cet » est donné) ; QCM « pourquoi ‹ nulle › dans la phrase d'origine » (accord avec ‹ phrase ›, féminin) — 2 q.
    - piège (étiquette à porter par un distracteur) : oublier la forme devant voyelle ou le féminin de l'adjectif — ligne C01#8 (d2)
  - 2015 gram. 2 : « Claude était attentif en classe et obtenait de bons résultats. » à commencer par « Nadine » — QCM « de bonnes notes » ; « attentive » est DONNÉ (`HP:adjectif-if-ive`) — 2 q.
    - piège (étiquette à porter par un distracteur) : oublier le féminin de l'adjectif — ligne C12#5 (d2)
  - 2019 gram. 2 : « Il était très vieux, car sa figure était couverte de rides profondes. » devient « Elle était très … car … visage était … de plis … » — QCM « vieille », QCM « son visage … couvert » — 2 q.
    - piège (étiquette à porter par un distracteur) : oublier un accord après le changement de genre — ligne C08#6 (d3)
  - 2010 gram. 3 : « Benjamin prend un gros colis emballé dans une vieille couverture. » avec « colis » remplacé par « valise » — QCM « une grosse valise emballée » — 2 q.
    - piège (étiquette à porter par un distracteur) : laisser un adjectif au masculin — ligne C17#6 (d3)
- Ne pas redemander : `07/quiz#5`, `07/01-pratique#5`, `07/02-boss#6`, `07/03-revision#6`, `07/05-entrainement#6`
- Note : Famille « féminin des adjectifs à consonne doublée » du `07` (neuf/neuve, gentil/gentille, beau/belle, bon/bonne). bon/bonne, gros/grosse, vieux/vieille sont dans le tableau du cours du `07` ; nul/nulle relève de la règle « on double la consonne » : si le cours ne le cite pas, l'auteur l'ajoute à l'exemple du cours (un mot).

#### m027 → `exercices/08-exam-2022-lecture-lucile-sur-les-planches.json` · d2 practice 75/15 · 9 questions · régime **examen**

- Titre : « 🏛️ Concours 2022 · lecture : Lucile sur les planches ⭐⭐ »
- Registre : id `C05#1` ; sources `C05#1, C05#2, C05#3, C05#4, C05#5`
- Sources (base en premier) : C05 (2022) ex. 1 ; C05 (2022) ex. 2 ; C05 (2022) ex. 3 ; C05 (2022) ex. 4 ; C05 (2022) ex. 5
- Items :
  - Q1 : « Lucile a exprimé à son professeure exactement ce qu'elle voulait. oui / non — Coche la bonne réponse et relève deux indices pour justifier ton choix. » — QCM oui/non, multi des deux indices — 2 q.
    - piège (étiquette à porter par un distracteur) : relever des indices sans lien avec le choix — ligne C05#1 (d2)
  - Q2 : « Lucile est timide. Relève une phrase qui le montre. » — QCM (leurre : une phrase narrative sans lien avec la timidité) — 1 q.
    - piège (étiquette à porter par un distracteur) : citer une phrase narrative sans lien avec le trait — ligne C05#2 (d2)
  - Q3 : « La mère apprend que Lucile s'est inscrite au club de théâtre. Comment réagit-elle ? Dis pourquoi. » — QCM de la réaction, QCM de la raison — 2 q.
    - piège (étiquette à porter par un distracteur) : décrire la réaction sans la justifier — ligne C05#3 (d2)
  - Q4 a : contraires de « Lucile joue son rôle __avec aisance__ » et de « __Immédiatement__, Mme Leroux interprète ma réponse… » ; Q4 b : synonymes de « Je suis __intéressé par__ son discours » et de « La fille __déclame__ son texte » — un QCM par expression (le leurre est de nature différente) — 3 q parmi les quatre expressions (au choix de l'auteur).
    - piège (étiquette à porter par un distracteur) : proposer un mot de nature différente — ligne C05#4 (d2)
  - Q5 : « D'après toi, comment le théâtre a-t-il permis à Lucile de se transformer ? » — QCM « quelle explication s'appuie sur l'évolution du personnage » (leurre : répondre sans expliquer l'évolution) — 1 q.
    - piège (étiquette à porter par un distracteur) : répondre sans expliquer l'évolution — ligne C05#5 (d2)
- Ne pas redemander : `07/03-revision#3`, `07/03-revision#4`, `07/04-defi#5`, `07/04-defi#6`
- Note : Compréhension d'un texte récent (R2). Texte intégral : PDF officiel `/tmp/claude-0/fr6g/src/2022-francais.pdf` (sha256 au registre) ; citation utile : « Je me suis inscrite, mais c'est une erreur ! » Coquille imprimée « à son professeure » (2022) : l'auteur la corrige en citant. Les lettres courtes du `07` (revision#3, #4, défi#5, #6) sont un autre geste.

#### m028 → `exercices/09-exams-2008-2022-recit-suite-ou-realisation-scene.json` · d3 boss 120/30 · 9 questions · régime **examen**

- Titre : « 🏛️ Concours 2008–2022 · préparer un récit : imaginer la suite ou la réalisation d'une scène ⭐⭐⭐ »
- Registre : id `C05#12` ; sources `C05#12, C17#10, C18#10, C19#10`
- Sources (base en premier) : C05 (2022) ex. 12 ; C17 (2010) ex. 10 ; C18 (2009) ex. 10 ; C19 (2008) ex. 10
- Items :
  - 2022 : « La maison des jeunes organise un festival culturel (danse, chant, dessin, peinture, théâtre, sculpture, ...). Tes amis et toi, vous choisissez un projet afin d'y participer. Rédige un récit de huit phrases au moins pour raconter ce que vous avez fait pour réaliser votre projet en intégrant le dialogue qui s'est passé entre vous. » — ordering des étapes du projet (choix, préparation, répétition, spectacle) ; QCM du dialogue de choix correctement ponctué — 3 q.
    - piège (étiquette à porter par un distracteur) : oublier le dialogue ou la progression du récit — ligne C05#12 (d3)
  - 2010 : « Au milieu du silence général, Benjamin appuie sur un bouton mais le tableau ne s'allume pas. Quelle déception ! Rédige un récit en imaginant comment s'est terminée la scène. (Intègre un court dialogue dans ton récit). » — QCM « quelle fin est cohérente avec l'échec » ; QCM de la réplique d'un camarade — 2 q.
    - piège (étiquette à porter par un distracteur) : oublier le dialogue ou la fin de la scène — ligne C17#10 (d3)
  - 2009 : « Violeta et Adrien présentent leur numéro. Malheureusement, ils ne réussissent pas leur spectacle… Rédige un récit en imaginant comment s'est terminée la scène. » — QCM « quelle fin ne contredit pas l'échec » ; multi « quelles réactions du public conviennent » — 2 q.
    - piège (étiquette à porter par un distracteur) : oublier le dialogue ou la fin de la scène — ligne C18#10 (d3)
  - 2008 : « Rédige une suite à ce récit en imaginant ce que Nicolas dit à ses parents en rentrant à la maison et comment son père et sa mère réagissent. Intègre un court dialogue… » — QCM du premier paragraphe de la suite (le retour à la maison) ; QCM de la réaction d'un parent — 2 q.
    - piège (étiquette à porter par un distracteur) : oublier le dialogue ou la réaction des parents — ligne C19#10 (d3)
- Ne pas redemander : `07/03-revision#5`, `06/04-defi#6`
- Note : Archétype « suite ou fin d'une scène, avec dialogue ». Pour les « suites », seule la situation imprimée est redonnée (le texte support n'est pas cité en entier). C19#10 relève du thème 02 mais l'archétype décide du placement. Question : calibrer en `d3`, ce sont des consignes de récit.


## Chapitre `08-autres-modes-de-vie`

### Missions (gisement)

#### m029 → `exercices/06-exams-2009-2025-complements-tableau-enrichir-deplacer.json` · d2 practice 75/15 · 10 questions · régime **examen**

- Titre : « 🏛️ Concours 2009–2025 · lieu, temps, manière : remplir le tableau, enrichir, déplacer ⭐⭐ »
- Registre : id `C02#5` ; sources `C02#5, C04#5, C05#6, C06#8, C08#5, C10#6, C12#4, C14#4, C18#4, C18#6`
- Sources (base en premier) : C02 (2025) ex. 5 ; C04 (2023) ex. 5 ; C05 (2022) ex. 6 ; C06 (2021) ex. 8 ; C08 (2019) ex. 5 ; C10 (2017) ex. 6 ; C12 (2015) ex. 4 ; C14 (2013) ex. 4 ; C18 (2009) ex. 4 ; C18 (2009) ex. 6
- Items :
  - 2025 gram. 1 : « Un à un, les touristes quittent le lieu avant le coucher du soleil. » — tableau « sujet / complément essentiel / complément de manière / complément de temps » en matching — 1 q.
    - piège (étiquette à porter par un distracteur) : confondre complément de manière et complément essentiel — ligne C02#5 (d2)
  - 2022 gram. 1 : « Au bout de deux mois, mes amis et moi avons présenté la pièce avec succès. » — tableau « groupe nominal sujet / essentiel / temps / manière » — matching — 1 q.
    - piège (étiquette à porter par un distracteur) : confondre complément de temps et de manière — ligne C05#6 (d2)
  - 2021 gram. 3 : « Sur son banc, le chat regarde, toute la journée, les promeneurs d'un air indifférent. » — tableau « essentiel / manière / lieu / temps » — matching — 1 q.
    - piège (étiquette à porter par un distracteur) : confondre manière avec lieu ou temps — ligne C06#8 (d2)
  - 2019 gram. 1 : « À huit heures moins le quart, j'allais vers l'école, les mains dans les poches. » — tableau « sujet / lieu / temps / manière » — matching ; « allais » (imparfait) est présent mais non évalué — 1 q.
    - piège (étiquette à porter par un distracteur) : confondre complément de lieu et de manière — ligne C08#5 (d2)
  - 2015 gram. 1 : « Ce jour-là, François suivit Claude sans se faire voir. » — tableau « sujet / essentiel / temps / manière » — matching ; « suivit » (passé simple) non évalué — 1 q.
    - piège (étiquette à porter par un distracteur) : prendre un complément de manière pour un essentiel — ligne C12#4 (d2)
  - 2013 gram. 1 : « Ce soir-là, Sylvie va vite rejoindre François devant le petit écran. » — tableau « essentiel / lieu / temps / manière » — matching — 1 q.
    - piège (étiquette à porter par un distracteur) : confondre complément de lieu et de manière — ligne C14#4 (d2)
  - 2023 gram. 1 : « Claudine réapprend à marcher. » enrichie « par un complément de temps et un complément de manière » — QCM de la phrase enrichie (leurre : confondre les deux compléments) — 1 q.
    - piège (étiquette à porter par un distracteur) : confondre les deux compléments ou en omettre un — ligne C04#5 (d2)
  - 2017 gram. 3 : « Les élèves ont souhaité la bienvenue à Caroline. » enrichie d'au moins deux compléments non essentiels de sens différents — QCM de la phrase correcte (leurre : deux compléments de même sens) — 1 q.
    - piège (étiquette à porter par un distracteur) : ajouter un complément essentiel ou deux de même sens — ligne C10#6 (d2)
  - 2009 gram. 1 : « Le jour du spectacle, nous entrons sur scène, un peu angoissés » — « relève le complément de manière, le complément de temps » — QCM — 1 q.
    - piège (étiquette à porter par un distracteur) : prendre l'apposition pour le complément de temps — ligne C18#4 (d2)
  - 2009 gram. 3 : « Je me mets à danser, pieds nus, à travers la scène. » — « réécris de deux façons différentes en déplaçant les compléments non essentiels » — QCM des deux réécritures valides — 1 q.
    - piège (étiquette à porter par un distracteur) : déplacer un complément essentiel — ligne C18#6 (d2)
- Ne pas redemander : `08/quiz#1`, `08/01-pratique#1`, `08/01-pratique#2`, `08/02-boss#1`, `08/02-boss#2`, `08/03-revision#3`, `07/quiz#1`, `07/quiz#2`, `07/02-boss#1`, `07/02-boss#2`, `06/quiz#1`, `06/03-revision#1`, `06/03-revision#2`, `05/03-revision#1`
- Note : Famille « les compléments dans la phrase » : cumul des chapitres 05 à 08, placée au `08` (chapitre le plus avancé). Écartés : C09#7 (2018, le tableau demande le « complément d'objet direct », `HP:cod`) ; C19#4 est au `05`. Chaque phrase de tableau est une phrase officielle redonnée telle quelle (coquilles incluses).

#### m030 → `exercices/07-exams-2008-2026-vouloir-et-pouvoir.json` · d2 practice 75/15 · 10 questions · régime **examen**

- Titre : « 🏛️ Concours 2008–2026 · vouloir et pouvoir : présent, passé composé, futur ⭐⭐ »
- Registre : id `C01#11` ; sources `C01#11, C06#11, C09#11, C11#7, C11#9, C19#9`
- Sources (base en premier) : C01 (2026) ex. 11 ; C06 (2021) ex. 11 ; C09 (2018) ex. 11 ; C11 (2016) ex. 7 ; C11 (2016) ex. 9 ; C19 (2008) ex. 9
- Items :
  - 2026 conj. 3 : « Moi, je peux même commencer dès ce soir ! » s'écrie Paloma, en remplaçant Paloma par « les filles » — QCM « nous pouvons », QCM « s'écrient » — 2 q.
    - piège (étiquette à porter par un distracteur) : garder la forme du singulier pour un sujet pluriel — ligne C01#11 (d3)
  - 2021 conj. 3 : « Tu peux garder le chat mais tu t'occuperas de lui. » dit à deux enfants — QCM « Vous pouvez », QCM « vous vous occuperez » — 2 q.
    - piège (étiquette à porter par un distracteur) : garder la forme du singulier — ligne C06#11 (d2)
  - 2016 conj. 1 : « Va où tu veux, ce n'est pas notre affaire. » en remplaçant « tu » par « vous » — QCM « Allez où vous voulez » — 2 q.
    - piège (étiquette à porter par un distracteur) : garder la forme du singulier — ligne C11#7 (d2)
  - 2016 conj. 3 : « Sans mon crayon gris, je ne peux pas dessiner mes animaux préférés. » à commencer par « Dans l'avenir, … » — QCM « je ne pourrai pas » (le radical « pourr- ») — 1 q.
    - piège (étiquette à porter par un distracteur) : laisser le présent ou mal former le radical du futur — ligne C11#9 (d1)
  - 2008 conj. 3 : « Alceste veut voir le portable. » à commencer par « Les copains de Nicolas … » — QCM « veulent » — 1 q.
    - piège (étiquette à porter par un distracteur) : garder la forme du singulier — ligne C19#9 (d1)
  - 2018 conj. 3 : « Le grand-père de Sophie va à l'école mais il ne veut pas raconter ses aventures. » à commencer par « La semaine dernière … » — QCM « est allé … n'a pas voulu » — 2 q.
    - piège (étiquette à porter par un distracteur) : oublier l'auxiliaire être ou mal former le participe — ligne C09#11 (d2)
- Ne pas redemander : `08/quiz#2`, `08/quiz#3`, `08/01-pratique#3`, `08/01-pratique#4`, `08/02-boss#3`, `08/03-revision#4`, `08/04-defi#1`, `08/04-defi#2`, `08/04-defi#4`
- Note : Famille « vouloir / pouvoir » du `08`. Les verbes d'autres chapitres (aller `06`, s'occuper) ont leurs formes données ou déjà vues. C05#9 (2022, « Nous voulons créer ») est au `05` (accord du verbe).

#### m031 → `exercices/08-exams-2012-2024-passe-compose-avec-etre.json` · d2 practice 75/15 · 8 questions · régime **examen**

- Titre : « 🏛️ Concours 2012–2024 · le passé composé avec être : l'accord du participe ⭐⭐ »
- Registre : id `C03#8` ; sources `C03#8, C08#8, C12#8, C15#8`
- Sources (base en premier) : C03 (2024) ex. 8 ; C08 (2019) ex. 8 ; C12 (2015) ex. 8 ; C15 (2012) ex. 8
- Items :
  - 2024 conj. 1 : « La bête est remontée à la surface. Elle a fait de drôles de pirouettes. » en remplaçant « la bête » par « les phoques » — QCM « sont remontés » (masculin pluriel), QCM « ont fait » — 2 q.
    - piège (étiquette à porter par un distracteur) : oublier l'accord du participe avec être — ligne C03#8 (d3)
  - 2019 conj. 1 : « À la fin de la séance, je suis repassé par la place de la gare routière, mais je n'ai pas trouvé le vieillard. » en remplaçant « je » par « nous » — QCM « sommes repassés » (l'accord), QCM « n'avons pas trouvé » (la négation) — 2 q.
    - piège (étiquette à porter par un distracteur) : oublier l'accord du participe ou l'auxiliaire — ligne C08#8 (d3)
  - 2015 conj. 2 : « Claude arrive dans une impasse, il entre dans une vieille maison. » au passé composé — QCM « est arrivé … est entré » — 2 q.
    - piège (étiquette à porter par un distracteur) : oublier l'auxiliaire ou l'accord du participe — ligne C12#8 (d2)
  - 2012 conj. 1 : « Les oiseaux migrateurs arrivent dans notre village. » a. au passé composé, b. au futur — QCM « sont arrivés », QCM « arriveront » — 2 q.
    - piège (étiquette à porter par un distracteur) : oublier l'accord du participe avec être — ligne C15#8 (d2)
- Ne pas redemander : `08/quiz#4`, `08/01-pratique#5`, `08/02-boss#4`, `08/03-revision#1`, `08/03-revision#2`, `08/04-defi#4`
- Note : Famille « passé composé avec être » du `08` (le participe s'accorde avec le sujet). F5 : le participe passé avec AVOIR n'est jamais ciblé (« ont fait », « n'avons pas trouvé » restent des formes sans accord). Écartés : C04#7 et C06#6 (pronominaux, `HP:pc-pronominal`).

#### m032 → `exercices/09-exam-2025-lecture-pyramide-maya.json` · d2 practice 75/15 · 9 questions · régime **examen**

- Titre : « 🏛️ Concours 2025 · lecture : à la découverte de la pyramide maya ⭐⭐ »
- Registre : id `C02#1` ; sources `C02#1, C02#2, C02#3, C02#4`
- Sources (base en premier) : C02 (2025) ex. 1 ; C02 (2025) ex. 2 ; C02 (2025) ex. 3 ; C02 (2025) ex. 4
- Items :
  - Q1 : « Au cours de cette aventure, Xavier se montre plus averti et attentif que ses compagnons. a. Coche vrai ou faux. b. Trouve dans le texte deux détails qui le montrent. » — QCM vrai/faux, multi des deux détails — 2 q.
    - piège (étiquette à porter par un distracteur) : relever un détail qui ne prouve pas l'affirmation — ligne C02#1 (d2)
  - Q2 : « Thierry et Jeanne ont profité différemment de ce voyage. Dis comment. » — matching personnage ↔ ce qu'il fait (écrire, dessiner) ; QCM « quelle phrase compare les deux » (leurre : ne décrire qu'un personnage) — 2 q.
    - piège (étiquette à porter par un distracteur) : décrire un seul personnage ou rester vague — ligne C02#2 (d2)
  - Q3 a : synonymes de « Ils s'engagèrent sur les __sentiers__ de la jungle » et de « Le ciel __s'embrase de mille éclats__ » ; Q3 b : contraires, trouvés dans le texte, de « __haussant le ton__ » et de « __disparait__ » — un QCM par expression — 4 q.
    - piège (étiquette à porter par un distracteur) : choisir un mot de nature grammaticale différente — ligne C02#3 (d2)
  - Q4 : « Jeanne suggère à ses amis de passer la nuit au sommet de la montagne. Es-tu d'accord avec elle ? Dis pourquoi. » — QCM « quel argument justifie le désaccord » (leurre : une réponse sans appui) — 1 q.
    - piège (étiquette à porter par un distracteur) : répondre sans justifier — ligne C02#4 (d2)
- Ne pas redemander : `08/04-defi#5`, `08/04-defi#6`, `08/05-entrainement#3`
- Note : Compréhension d'un texte récent (R2). Texte intégral : PDF officiel `/tmp/claude-0/fr6g/src/2025-francais.pdf` (sha256 au registre) ; citation utile : « Il fera bientôt nuit, dit-il en chuchotant. » Orthographe imprimée « apparait / disparait » (sans circonflexe, orthographe rectifiée de 2025) : l'auteur cite telle quelle. Les extraits du `08` défi (#5, #6) sont des mini-récits de l'auteur : autre geste.

#### m033 → `exercices/10-devoir-devoir-ecrire-une-lettre-lointaine.json` · d3 boss 120/30 · 8 questions · régime **devoir** (salle blanche)

- Titre : « 📝 Écrire une lettre à un ami lointain : préparer ⭐⭐⭐ »
- Registre : id `D08#1` ; sources `D08#1`
- Cartes : devoir G (épreuve de production du 3ᵉ trimestre, école primaire), consigne unique — carte anonyme
- Items :
  - Préparer une lettre à un destinataire éloigné pour lui présenter et lui décrire des lieux (consigne neuve inventée par l'auteur) : ordering des parties de la lettre (lieu et date, appel, corps, formule finale) ; QCM « quelle ouverture convient à un ami » ; QCM « quel passage décrit un lieu » (leurre : un passage qui raconte une action) ; QCM « quelle incitation finale invite à répondre ou à venir » (leurre : l'oublier) ; multi « quels éléments la lettre doit contenir » ; QCM du temps (présent de description) ; QCM d'une phrase hors sujet. 7 à 8 q.
    - piège (étiquette à porter par un distracteur) : oublier la structure de la lettre ou l'incitation finale — ligne D08#1 (d3)
- Ne pas redemander : `06/01-pratique#5`, `06/04-defi#1`, `06/04-defi#2`, `07/01-pratique#6`, `07/03-revision#3`, `07/03-revision#4`, `07/04-defi#3`, `07/04-defi#5`, `07/05-entrainement#1`
- Note : Salle blanche : la carte ne donne que le geste ; le destinataire, les lieux et les formules sont neufs. Geste absent des examens (aucune consigne de lettre en dix-sept sessions). Rangée au `08` par le thème de la consigne (règle F4) ; le prérequis (écrire une lettre) est enseigné aux `06` et `07`.

