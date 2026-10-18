# Audit B3 — anglais 6ᵉ, chapitres 05-celebrations et 06-going-shopping

Auditeur indépendant, 2026-10-18. Branche `wip/anglais-6eme-un-passage`, commit `cfc19d7c` (B3 écrit). Périmètre : `assign-B3.md`, soit 6 missions neuves, quiz et exercices 01–05 des deux chapitres, ainsi que les deux `chapter.json`. Toutes les questions ont été re-résolues à l'aveugle avant la lecture de `rapport-B3.md`. Sources : les transcriptions 2010, 2012, 2018, 2021 et 2023 à 2026, contrôlées sur les PDF officiels (scans rendus en PNG, pages lues).

**Correctifs** : `audit-B3-correctifs.diff` (même dossier). Il contient 46 remplacements. Chaque `old_str` est unique dans son fichier. Le diff a été appliqué sur une copie complète de `content/`, puis contrôlé dans cet état : `content:check` vert, `content:qa -- --subject english-6eme` vert, `content:tranche --chapters 05,06 --strict-longest` sans clé la plus longue (0/106) et sans paire proche (0). `git apply --check` passe sur la branche. Rien n'a été écrit dans `content/` et aucune écriture git n'a été faite.

## Chiffres

| | questions | clés fausses | majeurs | mineurs |
| --- | ---: | ---: | ---: | ---: |
| 05 (quiz + 01–05 + m012–m014) | 57 | 0 | 4 | 9 |
| 06 (quiz + 01–05 + m015–m017) | 59 | 0 | 6 | 4 |
| **total** | **116** | **0** | **10** | **13** |

Gates sur la branche telle quelle : `content:check` vert, `content:qa` vert, `content:tranche` donne 0 clé strictement la plus longue et 0 paire proche.

## Re-résolution, mission par mission

Ma réponse est égale à la clé partout. Le tableau ne liste que les verdicts autres que OK.

| fichier · question | ma réponse = clé | verdict | motif |
| --- | --- | --- | --- |
| m012 Q1–Q6, Q8–Q10 | chose, sang, right, thanked, took, wrote, ordre c-b-e-d-a, found, drank | OK (Q3 réserve) | Fidèles au PDF. Q3 : « wishing » est inventé alors que la banque officielle offre « celebrated » |
| m012 Q7 | preferred | **réserve, MAJEUR** | Le prompt a perdu « Last year ». Sans lui, « My friends prefer fast food, but I liked… » est défendable, et l'étiquette `present-avec-marqueur-passe` n'a plus de marqueur |
| m013 Q1–Q6 | party, b, True (c), d, False (b), 10 o'clock | OK, avec réserves d'étiquettes | Citations fidèles au PDF 2021. Q3 : la déduction est justifiée (doute 3) |
| m014 Q1–Q6 | b, c, appariement 1-4/2-3/3-1/4-2, a-c-e-f, c, d | Q3 et Q4 **MAJEUR** | Q3 : Sami est un garçon (« his », « him »), mais « I wear my best red dress ». Q4 : « fitting room » n'est enseigné qu'au 06 |
| m015 Q1–Q8 | a, d, d, on, bookshop, d, appariement 1-2/2-1/3-3, wear | OK, avec réserves | Le titre livre les clés (MAJEUR). Q2 : le prompt règle Q1. Q6 : deux distracteurs portent la même erreur |
| m015 Q9 | l1-r4… | **réserve, MAJEUR** | l1 « The customer says what he wants to buy » s'apparie aussi bien à r1 « I want story books for children » : la paire n'est unique que par élimination |
| m016 Q1–Q3, Q5–Q7 | funzone/coffee, by car, b, afraid, c, d | OK | Citations fidèles au PDF 2024 |
| m016 Q4 | Alex | **réserve, MAJEUR** | « Alex's mother » est éliminé par le genre de « him ». Les deux autres options sont inventées. Le référent est trivial |
| m017 Q1–Q6 | b, b, appariement, c, c, a-c-f | OK (Q6 réserve) | Voir la fuite Q7 → Q6 |
| m017 Q7 | b-e-d-a-c | OK, ordre unique (doute 4) | Mais le texte affiche « chose » et « tried on » : il règle les énoncés f et e du multi Q6 (MAJEUR) |
| m017 Q8 | c | **réserve, MAJEUR** | « spented » n'exécute pas `ed-sur-verbe-irregulier` (la forme visée est « spended »). Vote terme à terme : la clé est l'intersection des majorités (« spent » ×2, « hundred and » ×3) |

## Re-résolution, fichiers existants retouchés (étiquettes et réécritures `tranche`)

| fichier · question | verdict | motif |
| --- | --- | --- |
| 05/quiz 1–5 | OK | Q3 réécrite (made) : clé juste ; les options à deux erreurs sont muettes |
| 05/01-pratique 1–6 | OK | Q1 : « the end of school year party » est un mot du même champ, l'étiquette E7 est admissible. Q3 réécrite (I have) : juste |
| 05/02-boss 3 | mineur | « hugeed » « invente un e » : ni doublement, ni y → i, ni e muet. L'étiquette `spell.suffixe-sans-regle-orthographique` est inexacte, à rendre muette |
| 05/02-boss 1, 2, 4–6 | OK | Q2 réécrite (You have / he has) : plan 2×2 correct |
| 05/03-revision 2 | mineur | Le rembourrage uniforme « so very tired / really sick / all alone » laisse la clé seule option nue (marqueur de forme inverse) |
| 05/03-revision 6 | OK | asked |
| 05/04-defi 1–6 | OK | Q2 réécrite (gave/sent/cooked) : juste, fuite levée |
| 05/05-entrainement 4 | mineur | « stopeed » : même défaut que « hugeed » |
| 05/05-entrainement 6 | **MAJEUR** | La réécriture garde « danced ». Or `04-defi#4` a pour clé « danced » et son explication dit « the ending is simply /t/ » : c'est le même fait, livré par une autre question du chapitre (donjon). La paire n'est pas résolue sur le fond |
| 06/quiz 1–5 | OK | |
| 06/01-pratique 1–6 | OK | Q1 réécrite : faible mais juste |
| 06/02-boss 1–6 | OK | |
| 06/03-revision 3 | **MAJEUR** | L'explication cite « shop and shops are present forms » alors que l'option est devenue « will shop ». Elle affirme aussi « Sunday morning has already left behind » sans appui : seule la consigne (« the past of ») exclut le futur |
| 06/04-defi 1–6 | OK | Q1 : consigne variée, gabarit levé. Q3 : vote terme à terme préexistant (réserve) |
| 06/05-entrainement 2 | mineur | `present-avec-marqueur-passe` posé sur « pays » sans aucun marqueur dans la phrase |
| 06/05-entrainement 1, 3–6 | OK | |

## Défauts et correctifs (tous dans `audit-B3-correctifs.diff`)

### Majeurs

1. **m012 Q7** : ajouter le marqueur officiel. Prompt : `"Last year, my friends ___ fast food, but I liked the healthy meals my mother cooked."`. Explication : `"Last year" and "I liked" show that…`.
2. **m014 Q3** : Sami est un garçon qui porte « my best red dress ». Remplacer `red dress` par `red shirt` dans r2 (`My aunt gives me a red shirt and my uncle gives me a bike.`), dans r4 (`I wear my best red shirt and white shoes.`) et dans l'explication (`The red shirt appears twice,`).
3. **m014 Q4** (multi) : `fitting room` (enseigné au 06 seulement) devient `stomachache` (02). Explication : `A stomachache belongs to a visit to the doctor and a shopkeeper to a shop, not to a birthday party at home.`
4. **m015 titre** : « Can I help you?, I'd like, How much is it? » livre les clés de Q1, Q2, Q3 et Q7. Le défaut vient de la carte : `🏛️ Exams 2010–2025 · at the shop: offering, asking and paying ⭐⭐`.
5. **m015 Q9** : l1 devient `The customer answers "Can I help you?"`. Explication : `The customer first answers the offer of help (Yes please, I'd like to buy some books), …`. Après correction, chaque paire est unique sans élimination.
6. **m016 Q4** : la question est remplacée par le référent de « it », qui est un vrai piège du nom le plus proche. Prompt : `From the text: "There, she found a lovely dress at a good price. She went to the fitting room to try it on." What does the word "it" refer to?`. Options : `the fitting room` (`read.referent-le-plus-proche`), `the lovely dress` (clé), `the mall`, `the price` (muettes). La clé n'est pas la plus longue (égalité 16/16). Aucune fuite vers Q3 ni vers Q6.
7. **m017 Q7** : retirer les formes qui règlent le multi Q6. a devient `In the afternoon, my mother picked a silver necklace at the jewellery shop.`, d devient `At noon, my father looked at the blazers in the clothes shop.`. L'ordre reste unique.
8. **m017 Q8** : plan 2×2. Prompt : `In the evening of last Saturday, Sami adds up the money of the day at the mall.`. Options : `We spended three hundred…` (`ed-sur-verbe-irregulier`), `We spended three hundreds…` (muette), `We spent three hundred…` (clé), `We spent three hundreds…` (`centaines-mal-ecrites`). L'explication est ajustée. Chaque forme figure exactement deux fois, et la clé n'est pas la plus longue.
9. **06/03-revision Q3**, fin de l'explication : `The form shoped forgets the double letter, shops is a present form and will shop is the future, and the instruction asks for a past.`
10. **05/05-entrainement Q6** : `danced` devient `helped` (help → /p/ sourd → /t/, verbe vu au 06 comme régulier). Prompt : `Karim reads the verb helped aloud. How does its final -ed sound?`. Explication : `The verb help ends in the quiet sound p, …, so the ending of helped is the quiet /t/.`. Les options sont inchangées.

### Mineurs

- **m012 Q3** : `wishing` devient `celebrated`, le mot officiel de la banque 2025. L'explication est ajustée.
- **m013 Q1 b** (« an English lesson ») : retirer `read.detail-pris-pour-idee-principale`, car la question ne porte pas sur l'idée principale.
- **m013 Q3 b** : le stéréotype national (« Italian girls wear pink skirts ») devient `False: the text never says what Tina is wearing.`, muette. C'est le piège du littéralisme. L'explication devient `the text does not need to name Tina because she is one of the girls`. La clé n'est ni la plus longue ni la plus courte.
- **m013 Q4 b** (« To bring a present… ») : rendre l'option muette, car c'est une invention arbitraire et non une supposition « normale ».
- **m013 Q6**, explication : `Nine o'clock is the time given at the start of the text`. L'ancienne version affirmait que la fête commence à 9 h, ce que Q5 c étiquette comme sans appui.
- **m014 Q2**, prompt : `The questions of the task are in the present simple (What presents do you get?), so Sami answers in the present simple.`. Le lien « jour même → présent simple » n'est pas une règle enseignée.
- **m015 Q2** : « The shopkeeper offers his help » règle Q1 (offre ou demande). Nouveau prompt : `Complete the dialogue in the fruit shop: "Mrs Brown: ___, please. / The shopkeeper: Ok. Here you are."`.
- **m015 Q4** : « picture of the classroom » devient `Look at the picture.` (la figure ne montre qu'un bureau).
- **m015 Q6** : `the bank` devient `the bank or the station`, ce qui donne deux erreurs distinctes au lieu de deux options à un seul lieu. L'explication est ajustée.
- **05/02-boss Q3 b** (« hugeed ») et **05/05-entrainement Q4 b** (« stopeed ») : rendre ces options muettes.
- **05/03-revision Q2** : options `tired`, `sick`, `surprised`, `really bored`. Un seul distracteur est allongé, sans marqueur uniforme. L'explication est ajustée.
- **06/05-entrainement Q2** : `"Last week, my father ___ 60 dinars for my new shoes."`. L'explication commence par `Last week is before now, and pay is irregular`.

### Réserves sans texte imposé

- **m015 Q5** : « postcards », « bookshop » et « bank » ne sont enseignés nulle part. L'item se résout par la règle « shop named after what it sells » et par élimination. C'est un item d'examen, accepté.
- **m015, étage** : 7 questions sur 9 sont en d1 dans une mission practice d2. La rampe est basse mais honnête.
- **Ne pas redemander** : m012 Q6 (« my sister wrote ») est proche de `05/02-boss#4` ; m017 Q6 (went, bought, chose, try on) re-teste `04-defi#3` et `05-entrainement#5`. Ces items sont pourtant prescrits par la carte, qui se contredit. C'est une révision voulue des formes irrégulières : à garder, ou à arbitrer par l'orchestrateur.
- **06/04-defi Q3** : vote terme à terme préexistant (went et bought ×2). Aucun texte n'est imposé.
- **m017 Q8** : après le plan 2×2, la clé est strictement la plus courte. C'est inévitable quand les erreurs ajoutent des lettres, et c'est un cas isolé.
- **Hors lot (B2)** : l'énoncé de `04-caring/exercices/06-exams-2023-2025-superlative-and-jobs#6` contient « every child has the right to feel loved », c'est-à-dire la clé de m012 Q3. À signaler à B2. On peut par exemple retirer cette glose de l'énoncé du 04.
- **coursePitfalls du 05** : `present-avec-marqueur-passe` est enseigné comme règle (« any sentence that lands on them takes the past ») mais n'a pas de bloc `piege`. Admissible, car l'erreur est portée par des distracteurs et enseignée. Les autres pitfalls des deux chapitres ont chacun leur « classic mistake ». `sources[]` : la ligne examens est présente dans les deux `chapter.json`, conforme.

## Doutes de l'auteur, tranchés

1. **Verbes irréguliers d'un fichier à l'autre** (le `multi` de m017, entre autres) : ce ne sont pas des fuites. C'est la même forme re-testée dans une autre phrase, c'est-à-dire une révision espacée des formes que l'unité enseigne. Il y a en revanche **une fuite réelle à l'intérieur de m017** : Q7 affiche « chose » et « tried on » au passé correct et règle deux énoncés du multi Q6 (corrigé, majeur 7). Le chevauchement avec les items « ne pas redemander » est mis en réserve, car il est prescrit par la carte.
2. **`read.reponse-sans-appui-dans-le-texte`** : le libellé (« ce qui te paraît normal ou probable ») couvre bien les suppositions plausibles : bus ou taxi, leçon de maths, voyage scolaire, examen, gâteau d'anniversaire, « she is late ». Il ne couvre pas les inventions arbitraires ni les stéréotypes. Sont donc rendues muettes ou remplacées m013 Q3 b et Q4 b. m016 Q4 c et d disparaissent avec la réécriture. Les autres sont gardées.
3. **m013 Q3** : la déduction est justifiée. Le texte dit « Tina, the Italian girl in our class » et « The girls are wearing pink skirts, yellow shirts… » : vrai, donc la clé est juste.
4. **m017 Q7 (ordering)** : l'ordre est unique (Last Saturday, morning, noon, afternoon, evening), et il le reste après correction.
5. **Figure de m015** : rendue dans Chromium à 232 px de large. Le libellé est lisible (≈ 13 px), l'encre est sombre et la `viewBox` est présente. L'ordinateur posé sur le bureau est la donnée de la question, pas un marqueur ajouté. La figure lève l'ambiguïté de « at the desk » sans désigner une option par sa forme. OK.
6. **Adaptations** : le `matching` du moteur exige une bijection (`schema.ts`), donc l'intrus officiel (2018 « some sugar », 2024 ③) ne peut pas être porté. L'adaptation est acceptée. Une seule a créé un défaut, m015 Q9 l1 (corrigé). Le passage du présent continu au présent simple de m014 est cohérent avec les questions officielles (« What do you wear? ») ; seul le motif donné dans le prompt est reformulé (mineur).
7. **Item 2025 commun avec `04/…/06-exams-2023-2025-superlative-and-jobs`** : ce n'est pas un doublon, puisque le blanc et la notion diffèrent (« right » d'un côté, « cared » de l'autre), et partager « caring » comme distracteur est sans effet. Mais l'énoncé du 04 pose « has the right to feel loved », c'est-à-dire la clé de m012 Q3 : c'est une réserve hors lot, à transmettre à B2. Côté B3, je propose seulement `wishing` → `celebrated`.

## Étiquettes

Toutes les étiquettes existent au registre. Aucune n'est posée sur un `multi`, un `ordering` ou un `matching`. Les options à deux erreurs sont muettes partout. E7 (`mot-voisin-du-meme-champ`) est respecté : chaque option étiquetée est réellement du champ de la clé, et l'énoncé tranche. Part étiquetée (QCM) :

| | branche | après correctifs |
| --- | --- | --- |
| 05 existants | 52/105 (50 %) | 50/105 (48 %) |
| 05 missions | 28/51 (55 %) | 25/51 (49 %) |
| 06 existants | 52/105 (50 %) | 52/105 (50 %) |
| 06 missions | 34/57 (60 %) | 31/57 (54 %) |

Les deux chapitres sont sous 60 %, ce que PLAN-gisement E7 accepte quand le chiffre est honnête. Les muets sont justifiés : erreurs sans entrée au registre (« will » + marqueur passé, in/on du coin, nombres) ou options à deux erreurs.

## Verdict

**Corriger avant l'armement**, puis le lot est **prêt**. Aucune clé n'est fausse sur 116 questions. Il y a 10 majeurs et 13 mineurs, tous corrigés par le diff vérifié. Le titre de m015 vient de la carte, que l'orchestrateur doit aussi corriger. Une réserve reste à arbitrer : la carte se contredit sur « ne pas redemander ». Le diff s'applique tel quel (`git apply`) et laisse les gates verts.
