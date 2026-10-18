# Rapport de l'auteur B1 — anglais 6ᵉ, chapitres 01 et 02

Écrit le 2026-10-18. Carte : `assign-B1.md`. Pas de git. Gates passés sur mes fichiers : `content:check`, `content:qa -- --subject english-6eme` (0 erreur, 0 avertissement), `content:qa:strict`, `content:tranche -- --subject english-6eme --changed --fresh --strict-longest` (0 clé la plus longue, 0 paire proche), `lot-lint` (rien à signaler), `prettier --check` (tous les fichiers conformes), `programme:check`, `harness:check --corpus`.

## 1. Fichiers

Créés (6 missions, 52 questions) :

- `content/english-6eme/01-entertaining-myself/exercices/06-exams-2008-2025-like-ing-how-often.json` (m001, d2 practice 75/15, 12 q.)
- `…/01-entertaining-myself/exercices/07-exams-2008-2021-possessives-and-linkers.json` (m002, d2, 9 q.)
- `…/01-entertaining-myself/exercices/08-exams-2023-2026-dialogues-suggest-invite.json` (m003, d2, 8 q.)
- `…/01-entertaining-myself/exercices/09-exam-2023-reading-drawing-competition.json` (m004, d2, 7 q.)
- `…/02-keeping-fit/exercices/06-exams-2010-2025-should-must-can-how-much.json` (m005, d2, 7 q. au lieu de 8)
- `…/02-keeping-fit/exercices/07-exam-2024-writing-doctors-advice.json` (m006, d3 boss 120/30, 8 q.)

Modifiés : `quiz.json` et les cinq exercices de chacun des deux chapitres (étiquettes + défauts `tranche`, voir § 3), les deux `chapter.json` (`sources[]` : ligne des examens ; `coursePitfalls` : les cinq tags de la carte, chacun porté par au moins un distracteur du chapitre). `content/misconceptions.json` : non touché (fait par le pilote) ; aucun id neuf posé par moi.

Outils et notes : `/tmp/claude-0/en6-gis/B1/` (`lib.py`, `patch-existants.py`, `missions_ch01.py`, `missions_ch02.py`) ; `auteurs-notes/B1/NOTES.md`.

## 2. Taux d'étiquetage (distracteurs de questions `mcq` ; aucune étiquette sur `multi`, `ordering`, `matching`)

| | avant | existants après | missions neuves | chapitre entier |
| --- | ---: | ---: | ---: | ---: |
| 01 | 0 / 105 | 68 / 105 (64,8 %) | 57 / 90 (63 %) | 125 / 195 (64,1 %) |
| 02 | 0 / 105 | 65 / 105 (61,9 %) | 17 / 30 (57 %) | 82 / 135 (60,7 %) |

Par mission : m001 7/24 (29 %), m002 21/27 (78 %), m003 18/18 (100 %), m004 11/21 (52 %), m005 5/12 (42 %), m006 12/18 (67 %).
m001 et m005 restent bas parce que leurs distracteurs sont des mots de la banque imprimée (many, much, stomachache, cleaner…) qui n'exécutent aucune erreur du registre ; je ne les ai pas étiquetés au jugé. Les deux chapitres passent 60 % tout compris.

Règles que j'ai tenues : une option qui exécute DEUX erreurs reste muette (grilles 2×2 : « in … on », « but … because », « My … their », « much … many »…) ; libellé exact ; `english.vocab.mot-voisin-du-meme-champ` seulement sur un mot du même champ que la clé quand un indice de l'énoncé tranche (activités de loisir avec « rod and river » ; aliments avec « healthy » ; maladies avec « stomach » ; lieux avec « old and beautiful objects » ; « at lunchtime » face à « After lunchtime »).

Étiquettes hors des listes de la carte mais présentes au vocabulaire du lot A (`map-vocab.md` § 3) : `english.read.reponse-sans-appui-dans-le-texte` et `english.read.detail-pris-pour-idee-principale` (m004), `english.write.phrase-hors-sujet` (m006), `english.modal.to-en-trop` et `english.modal.s-sur-le-modal` dans les chapitres où elles sont déjà citées. Candidats volontairement laissés muets faute d'être dans la carte (id existant, libellé exact) : `english.modal.to-oublie` (« Would you like come to… », « Would you like join… »), `english.verb.base-verbale-deformee` pour « Let's going » (01), `english.verb.be-avec-base-verbale` (« aren't go », « is sing », « He is live »).

## 3. Défauts `content:tranche` corrigés

Clé strictement la plus longue : 11/70 (16 %) avant → 0/110 après (missions comprises). Les onze, sans changer la réponse :

- 01 `quiz#4` (« How about go » → « How about to go »), `quiz#5` (« its » → « theirs »), `01-pratique#4` (« why » → « because of »), `03-revision#4` (« Yes, I like. » → « Yes, I do, thank you. »), `04-defi#5` (« How about going to the new cinema in town? »), `05-entrainement#2` (« shops » → « to shopping »).
- 02 `02-boss#1` (distracteur allongé), `02-boss#6` (idem), `03-revision#2` (« a bad headache »), `03-revision#4` (« can » → « don't must » ; l'énoncé passe de « medicine » à « a cleaning product » : avec un médicament, « You must drink it » n'était pas faux), `05-entrainement#1` (« milk » → « rabbit »).

Paire proche 0,46 `02/01-pratique#6` ↔ `02/05-entrainement#4` : `05#4` réécrit (autre contexte, « for dinner », autres options). Aucune paire dans le 01. Gabarits : non modifiés (à l'auditeur) ; mes missions ne reprennent aucun des trois cadres.

## 4. Missions : questions, étages, items écartés, adaptations

- **m001** (12 q., d2) : 8 QCM de langue (adverbe, like + -ing, -s de la 3ᵉ personne, in/on), 4 `ordering` (2025 W1 a, 2009 W2 b, 2008 W1 c, 2008 W1 a), 2 QCM de correction (2017 live, 2015 drinking). Ordering en morceaux (le schéma limite à 6 options). La rampe de difficulté (lot-lint) m'a fait ranger les d1 d'abord.
- **m002** (9 q., d2) : conforme à la carte ; « There ___ » (HP) non repris ; « has got / get / go » et « He / She / They » écartés comme dit.
- **m003** (8 q., d2) : ordering de 5 répliques (2023) + 4 QCM de fonction (invitation, refus avec can't, suggestion How about, Let's) + matching 2026 + 2 QCM (What about…? ; Can you help…?).
- **m004** (7 q., d2) : lecture 2023, une à deux phrases citées par question, lues sur le PDF officiel. Voir écarts.
- **m005** (7 q., d2) : voir écarts.
- **m006** (8 q., d3 boss) : tâche, multi (3 justes sur 6), 3 QCM should / must / shouldn't (conseils au style direct, dit dans l'explication de la première question, E6), cadre « Dear … / Yours, … » en 2×2, phrase qui appartient au sujet, ordering du plan. Étage d3 honnête : les deux QCM de modaux les plus fins sont d3.

Items écartés ou non repris (tous conformes à la carte, plus ceux-ci) : la 4ᵉ case du dialogue 2026 (« Great! (…) » : « I will make a playlist » et « What about the party invitations? » y vont tous deux, la clé de l'examen n'est pas décidable sans corrigé) ; l'option en trop du matching 2026 (voir écarts).

Notions données dans l'énoncé : « the exam asks for a 5-sentence e-mail » (m006) ; pour 2018 (m001/m005), le début de phrase est donné sans « like swimming » dans m005 et sans « can't » dans m001, pour qu'aucune des deux ne livre la clé de l'autre (la phrase officielle y est donc scindée).

## 5. Écarts à la carte

1. **m005 : 7 questions au lieu de 8.** La liste d'items de la carte en compte 7 ; je n'ai pas inventé un huitième item hors examen.
2. **m003 : matching à 3 cercles, sans option en trop.** Le schéma exige une bijection (autant de gauches que de droites). Le 4ᵉ cercle (« Great! ») est écarté car deux répliques y vont. Les deux répliques restantes sont reprises dans deux QCM de fonction.
3. **m004 : le vrai/faux et « la phrase qui le prouve » sont fondus** en une seule question par énoncé (réponse = verdict + raison, quatre combinaisons) : séparés, l'énoncé de l'un livrait la clé de l'autre. Deux questions de lecture ajoutées pour garder 7 (titre du texte ; « Why do they hug her? »).
4. **m005 : le matching « How many playgrounds + are there? »** devient un appariement de trois débuts de question (How many playgrounds / How much milk / How many eggs) avec leur fin : « are there » n'est pas « donné », il est à trouver, sinon un appariement n'a qu'une paire.
5. **Libellé d'examen des `sources[]`** : texte du prompt (« concours national de fin d'études… »), non celui de `PLAN-gisement.md` § 1 R7.
6. Les distracteurs non issus de la banque officielle (« stomachache » face à « sick », « unhealthy food », « they're », « theirs », « to swimming »…) sont des erreurs d'élève plausibles que j'ai ajoutées pour la forme à quatre options.

## 6. Doutes pour l'auditeur

- **Fuites internes à une mission, héritées du plan** : m005 Q multi « mots en trop » (many, never) se déduit des deux QCM voisins (stomachache, much) ; m001 Q1 (always) et m005 (Ashley) reprennent le même exercice 2023 dans deux chapitres. Ordre aléatoire du donjon : à juger.
- m003 Q2 : « Would you like to… » (invitation) face à « makes a suggestion for the two of them » : la distinction vient du cours, mais « play football with me » peut se lire comme les deux.
- m001 Q10 (ordering 2008 W1 a, « I go to / the zoo / on / Sundays ») : « On Sundays I go to the zoo » reste correct en anglais ; l'initiale minuscule de « on » et la majuscule de « I go to » l'écartent.
- m002 Q5 : la clé officielle « but » : « and » serait défendable, je l'ai écarté des options.
- m004 Q2 option b : « True: she always draws her friends jumping and swinging with her at school » — la fin « with her at school » est un ajout destiné à rendre l'option fausse.
- Étiquette `english.vocab.mot-voisin-du-meme-champ` posée sur les verbes de loisir, aliments et lieux de 01 `01-pratique#1`, `03-revision#1`, `05-entrainement#1` et 02 `quiz#1`, `03-revision#1` : à valider (E7).
- `english.verb.ing-oublie` posée sur « dislike + base verbale » (01 `05-entrainement#2`) : le libellé du registre nomme like, love, hate, pas dislike.
- 02 `05-entrainement#1` : `english.sound.lettre-pour-son` sur trois mots à voyelle brève (un francophone lit « i » comme /iː/) : lecture honnête mais indirecte.
