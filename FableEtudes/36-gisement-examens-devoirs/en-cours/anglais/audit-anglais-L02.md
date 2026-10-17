# Audit indépendant — lot L02, anglais 9ᵉ (gisement, étude 36)

> Auditeur indépendant, 2026-10-17. Périmètre : les cinq missions de `assign-anglais-L02.md`, branche
> `wip/gisement-anglais-9eme` (`/home/user/wt-en`, commit `f5aa1801`, fichiers du lot non modifiés depuis) :
>
> - `content/english/01-present-tenses/exercices/06-exams-2001-2021-present-simple-or-continuous.json` (m006)
> - `content/english/02-past-tenses/exercices/06-exams-2006-2026-present-perfect-or-simple-past.json` (m007)
> - `content/english/02-past-tenses/exercices/07-exams-2001-2026-simple-past-or-past-progressive.json` (m008)
> - `content/english/02-past-tenses/exercices/08-exams-2002-2023-writing-telling-a-past-event.json` (m009)
> - `content/english/05-conditionals/exercices/06-exams-2008-2021-will-and-if.json` (m010)
>
> Sources lues : transcriptions officielles des 30 sessions citées
> (`content/programmes-officiels/examens-nationaux/9eme-base/english/`), `cours.md` des chapitres 01, 02, 04, 05, 07 et 10
> sur `origin/main`, `content/misconceptions.json` sur `origin/main`, `PLAN.md`, et les affectations des
> autres lots (L01, L03, L04, L06) **pour les seules fuites** croisées. Aucune note d'auteur n'a été ouverte. Aucun
> fichier audité n'a été modifié.
>
> Contrôles moteur : `content:check` / `content:tranche` n'ont pas pu tourner sur le lot. `/home/user/eng-en` est un
> lien vers `eng-svtses`, et son `content/` contient un fichier en cours d'écriture d'un autre lot
> (`09/…/13-exams-2018-2026-the-right-word-in-context.json`, `questions.10.correctOption` invalide) qui fait échouer le
> chargement du sujet. Ce fichier n'est pas dans ce lot. Les mesures de forme (clé la plus longue ou la plus courte) ont
> été faites par script sur les cinq fichiers.

## 0. Bilan

| mission | questions | clés fausses | critiques | majeurs | mineurs |
| --- | ---: | ---: | ---: | ---: | ---: |
| m006 (01/06) | 12 | 0 | 0 | 3 | 2 |
| m007 (02/06) | 12 | 0 | 0 | 3 | 2 |
| m008 (02/07) | 12 | 0 | 0 | 3 | 2 |
| m009 (02/08) | 8 | 0 | 0 | 3 | 4 |
| m010 (05/06) | 6 | 0 | 0 | 2 | 1 |
| **total** | **50** | **0** | **0** | **14** | **11** |

J'ai re-résolu les 50 questions à l'aveugle. Je trouve la même clé que le fichier pour toutes, les `multi` et les
`ordering` compris, et chaque `ordering` n'admet qu'un ordre. Tous les défauts sont des **fuites** et des **notions
non enseignées**. Il y a aussi deux corrections de fidélité. Douze questions sont à reprendre (texte ci-dessous) et
deux sont à retirer (m007 Q10, m009 Q7).

**Verdict : à corriger avant livraison.** Les correctifs sont courts, mais les fuites croisées vers L03, L04 et L06
sont réelles.

## 1. Tableaux de re-résolution

### m006 — present simple or continuous (d2, practice 75/15)

| Q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | remains | b remains | OK | sujet « the issue » ; banque 2021 G fidèle |
| 2 | gather | d | OK | |
| 3 | provides | a | OK | |
| 4 | is | c | OK | |
| 5 | is | b | OK | |
| 6 | downloads | a | **réserve** | fuite vers m013 (L03) par « who is 15 » (D-3) |
| 7 | check | d | OK | |
| 8 | places | c | OK | |
| 9 | trains | b | OK | |
| 10 | take | a | OK | |
| 11 | meets | d | OK | |
| 12 | is leaving | a | **réserve** | contexte ajouté : fuite vers m007 Q8 et modèle de la clé (D-1, D-2) ; ⓓ non fidèle (d-1) |

### m007 — present perfect or simple past (d2, practice 75/15)

| Q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | has done | c | **réserve** | « ever since » : notion non enseignée avant le 10 (D-4) ; « he has not stopped » donne le temps |
| 2 | been | a | OK | leurres officiels « worked », « learn » gardés |
| 3 | forgotten | b | OK | |
| 4 | has | a | OK | |
| 5 | learned | d | **réserve** | fuite vers m022 (L06) par « hearing problems » (D-6) |
| 6 | got | b | **réserve** | même gabarit que Q5 (d-3) |
| 7 | has done | a | **réserve** | « for three years » : non enseigné (D-4) |
| 8 | have been | d | **réserve** | « since » : non enseigné (D-4) ; « are » officiel remplacé (d-4) |
| 9 | didn't work | b | OK | |
| 10 | for | c | **ERREUR de périmètre** | for/since n'est enseigné dans aucun chapitre, et la règle n'est que dans l'explication (D-5) |
| 11 | has written | a | **réserve** | « since » (D-4) ; « laughed at her » (D-7) ; « is writing » officiel remplacé (d-4) |
| 12 | have / changed | c | OK | plan 2×2 propre, l'option à deux erreurs est muette |

### m008 — simple past or past progressive (d3, boss 120/30)

| Q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | grew | a | **réserve** | « She began » dans l'énoncé donne la clé de Q4 (D-8) |
| 2 | spent | c | OK | |
| 3 | destroying | b | OK | leurres hors banque (d-5) |
| 4 | began | d | **réserve** | « grew up » donne la clé de Q1 ; « construction », « join » fuient vers m024 et m018 (D-8, D-9) |
| 5 | became | a | OK | leurre officiel « made » gardé |
| 6 | gained | b | OK | |
| 7 | died | d | OK | |
| 8 | lasted | a | OK | « fourty-five [sic] » conforme à R6 |
| 9 | was working | c | **réserve** | « laughed at her » fuit vers m016 (L04) (D-7) ; coquille corrigée sans déclaration (d-6) |
| 10 | founded | b | OK | |
| 11 | were moving | a | OK | « moved » n'est pas proposé ; aucune option ne devient juste (§ 3) |
| 12 | ran / jumped | c | OK | 2×2 propre, « run / jump » est muette |

### m009 — writing prepared: telling a past event (d2, practice 75/15)

| Q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 (multi) | a, c, e | a, c, e | **réserve** | deux distracteurs absurdes (d-7) |
| 2 | c built | c | **réserve** | même geste que m008 Q2 (d-8) ; la clé est donnée par Q3 option d (D-11) |
| 3 (ordering) | b, e, d, a, c | idem | **réserve** | l'option d donne la clé de Q2 (D-11) |
| 4 | b | b | OK | |
| 5 | b | b | **réserve** | clé strictement la plus courte (d-9) |
| 6 (ordering) | c, e, a, d, b | idem | **réserve** | l'option e et l'explication donnent la clé de Q8 (D-10) |
| 7 | so | a | **à retirer** | because/so n'est enseigné qu'au 07 ; règle donnée puis application directe (D-12) |
| 8 | d was playing | d | OK | « has been playing » est une forme non enseignée, mais c'est un leurre et la longueur le justifie (d-10) |

### m010 — will and if (d2, practice 75/15)

| Q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | will regret | b | OK | |
| 2 | d | d | **réserve** | « I advise everyone » fuit vers m024 (L06) ; clé strictement la plus courte (D-13, d-11) |
| 3 | will join | c | OK | |
| 4 | will die | a | OK | |
| 5 | if | d | OK | « unless » est défini au cours 05 (Going further) ; il n'est que leurre (§ 3) |
| 6 | b obligation | b | **réserve** | l'énoncé attribue au garçon une phrase qui n'est pas dans le sujet (D-14) |

## 2. Défauts et correctifs

Chaque correctif a été vérifié par script. Il ne rend pas la clé strictement la plus longue, sauf mention contraire.
Il ne nie aucune prémisse. Il ne fuit ni vers une question du lot, ni vers une mission des lots L01, L03, L04 et L06,
dont j'ai relu les affectations.

### Majeurs

**D-1 · m006 Q12 — fuite vers m007 Q8.** Le contexte ajouté « Dave and Jenny have been friends since they were
children » donne mot pour mot la clé de m007 Q8 (« They ___ neighbours since they were children » → have been). Sur la
route, le chapitre 01 passe avant le 02.

**D-2 · m006 Q12 — le contexte donne la forme de la clé.** « One of them is going away » donne la forme et le sens de
« is leaving ». Remplacer **la phrase de contexte** de l'énoncé :

> `(Exam 2006) Dave and Jenny are old friends and neighbours, and it is time to say goodbye. Which form completes the sentence? "Now, Dave ___ because he found a new job in another city."`

« found » remplace « got » (voir d-1). Les options et la clé ne changent pas : longueurs 10 / 6 / 11 / 4, la clé
n'est pas la plus longue. Dans l'explication, « "Now" and the goodbye show… » reste juste.

**D-3 · m006 Q6 — fuite vers m013 (L03).** m013 pose « My daughter, (who - which - where) is 15 » → who (2012 T). L'énoncé
écrit « her daughter, who is 15 ». Remplacer :

> `(Exam 2012, technical) A mother describes how her 15-year-old daughter uses the Internet every day. Which form completes the sentence? "She chats with her friends, ___ new films and reads newspapers and magazines."`

**D-4 · m007 Q1, Q7, Q8, Q11 — notion non enseignée : since / for avec le present perfect.** Le cours 02 sur
`origin/main` ne contient ni « since » ni « for » de durée. Seul le chapitre 10, plus loin dans l'ordre, cite « since »
dans un tableau. Or la règle du 02 (« finished time → simple past ») pousse l'élève vers « were » devant « since they were
children ». Ces quatre questions tiennent sur le seul repère, ce qui va contre la règle d'audit (« notion donnée dans
l'énoncé »). Correctif dans le périmètre du lot : **donner dans l'énoncé la donnée qui rend la période ouverte**. Le
cours 02 l'enseigne : « her life up to now », « no finished time ». Le repère n'est alors plus indispensable :

- Q1 : remplacer `and he has not stopped.` par `and he still volunteers today.` Cela retire aussi le present perfect
  de l'énoncé, qui servait de modèle à la clé.
- Q7 : `(Exam 2012, general) Tony is a 15-year-old school boy, and he still does voluntary work today. Which form completes the sentence? "He ___ voluntary work for three years."`
- Q8 : `(Exam 2006) Dave and Jenny have known each other for many years, and they still live next to each other. Which form completes the sentence? "They ___ neighbours since they were children."`
- Q11 : `(Exam 2010, technical) Diana has always wanted a job in engineering, and she is still trying to get one. Which form completes the sentence? "Since she left school, she ___ letters to all the engineering firms in her home town."` Cela retire aussi « laughed at her » (D-7).

Suivi pour le pilote, hors lot : une ligne « since + point de départ / for + durée » dans la section present perfect
du cours 02. Le 10 l'utilise déjà.

**D-5 · m007 Q10 — for / since : à retirer.** Ni le 02, ni aucun chapitre antérieur, ni le 10 n'enseignent « for + durée ».
L'affectation (R6) place la règle dans l'**explication** seule. L'élève répond donc avant d'avoir la règle, et la règle
d'audit l'exige dans l'énoncé. Si on la met dans l'énoncé (« for + a length of time; since + a starting point »),
c'est une application directe, qui ne vaut ni d3 ni même un item d'examen. **Retirer Q10.** La mission passe à
11 questions (12 au plus). Si le pilote préfère la garder, l'énoncé commence par `Remember: for + a length of time, since + a starting point.`, la difficulté passe à 2, et la question est déclarée au rapport de
livraison.

**D-6 · m007 Q5 — fuite vers m022 (L06).** m022 pose « He was born with (hear / heard / hearing) problems » → hearing
(2016 T). L'énoncé écrit « Tom is a boy with hearing problems ». Remplacer :

> `(Exam 2016, technical) Tom has problems with his ears, and his friends are helpful. Which form completes the sentence? "They have ___ some signs to communicate with him."`

**D-7 · m008 Q9 (et m007 Q11) — fuite vers m016 (L04).** m016 pose « People laughed (at / of / on) her because… » → at
(2019 T, le même texte que m008 Q9). Les énoncés de m008 Q9 et de m007 Q11 écrivent « laughed at her ». Pour m007 Q11,
voir D-4. Pour m008 Q9, remplacer :

> `(Exam 2019, technical) Katie Gillard has always wanted to be a truck driver. Some people did not take her seriously when she passed her first driving test. Which form completes the sentence? "A lot of teasing went on where she ___, but Katie was happy doing her job."`

**D-8 · m008 Q1 ↔ Q4 — fuite entre questions.** L'énoncé de Q1 dit « She began when she was seven », ce qui donne la clé
de Q4 (began). L'énoncé de Q4 dit « grew up », ce qui donne la clé de Q1 (grew). Le donjon tire au hasard, donc les
deux sens comptent.

- Q1 : remplacer `She began when she was seven and a cyclone had destroyed thousands of trees.` par
  `Her journey started at age seven, when a cyclone destroyed thousands of trees.` C'est plus fidèle au sujet, et le
  past perfect, non enseigné, disparaît.
- Q4 : voir D-9.

**D-9 · m008 Q4 — fuites vers m024 (L06) et m018 (L04).** m024 pose « (constructed / constructs / construction)
industry » → construction, et m018 pose « advised her to (enrol / finish / join) » → join (2024 T). L'énoncé écrit
« construction industry » et « advised her to join ». Remplacer l'énoncé et l'explication :

> prompt : `(Exam 2024, technical) Monique Strong's father worked in building in California, and her teachers advised her to study at a technical college. Which form completes the sentence? "After graduating, she ___ a new job in building."`
>
> explanation : `The whole story is told in the past: her father worked in building, her teachers advised her, and then she graduated. Begin is irregular: began. "begins" and "begin" leave the verb in the present; "begun" is the past participle, which needs have before it.`

**D-10 · m009 Q6 → Q8 — fuite entre questions.** L'option e de Q6 (« …was playing on the balcony ») et son explication
(« the little boy was playing on the balcony ») donnent la clé de Q8 (« He was playing on the balcony when… »), qui
vient après sur la route. Remplacer :

> Q6 option e : `His little brother, who is four, was on the balcony with his toys.`
>
> Q6 explanation : `The story follows the order of the facts: first the place and the time, then the cause (the little boy was on the balcony and slipped), then the injury, and last the result (the hospital and the worried parents).`

L'ordre reste unique : c, e, a, d, b.

**D-11 · m009 Q3 → Q2 — fuite entre questions.** L'option d de Q3, « Then we built the walls and put on the roof. »,
donne la clé de Q2 (« we built the walls and the roof »). Le donjon peut tirer Q3 en premier. Remplacer :

> Q3 option d : `Then we raised the walls and put on the roof.`

L'ordre reste unique : b, e, d, a, c. L'explication de Q3 ne cite pas cette phrase et reste juste.

**D-12 · m009 Q7 (Q8 de l'auteur) — connecteurs because / so : à retirer.** Ces connecteurs ne sont enseignés qu'au
07, qui vient après le 02. L'énoncé pose la règle (« because introduces a cause, so introduces a result »), et la
question devient une application directe. Ses deux leurres « but » et « until » s'écartent d'un coup d'œil. Elle ne
porte pas sur la notion du chapitre (le récit au passé). Son énoncé (« slipped off the balcony, ___ he broke his
arm ») donne aussi une partie de l'ordre de Q6. Les connecteurs officiels ont leur mission, m017 (09/12). **Retirer la
question.** m009 passe à 7 questions (8 au plus).

**D-13 · m010 Q2 — fuite vers m024 (L06).** m024 pose « I (advice / advise / advised) everyone to cherish those days »
→ advise. L'énoncé l'écrit en entier. La clé est aussi strictement la plus courte (31 contre 41 à 43). Remplacer
l'énoncé, les options a et d, et l'explication :

> prompt : `(Exam 2018, general) A young adult remembers his first school days. He tells everyone to cherish those days, "because if you don't, then…" What does "if you don't" mean here?`
>
> a : `if you don't tell everyone to do the same` · b (inchangée) : `if you don't spend your first day at school` · c (inchangée) : `if you don't tell anybody about those days` · d (clé) : `if you don't cherish your own school days`
>
> explanation : `In "if you don't", the short form don't stands for the verb that comes just before, which is not repeated: the condition is "if you don't cherish those days". The result comes after "then". The other readings give the condition a verb that the sentence does not use.`

Longueurs : 41 / 43 / 42 / 41. La clé n'est ni la plus longue ni la plus courte. L'énoncé ne contient pas « will
regret » et ne fuit donc pas vers Q1. ⚠️ Pour L06 : si l'énoncé de m024 écrit la fin de la phrase (« you will regret
it »), il donne la clé de m010 Q1. À signaler à son auditeur.

**D-14 · m010 Q6 — fidélité.** « In a text, a boy says to his mother: "… You must die of cancer." » attribue au sujet
de 2008 une phrase qu'il ne contient pas : « must die » n'est qu'une option imprimée, et la clé est « will die ».
Remplacer :

> `(Exam 2008) A boy wants his mother to stop smoking: "Mum, don't smoke." One of the printed options for the next sentence was "You must die of cancer." What would must express in that sentence?`

L'explication (« would order her to die ») reste juste. Effet résiduel, accepté par le plan : tirée avant Q4 dans le
donjon, Q6 écarte le leurre « must die » de Q4 (mineur).

### Mineurs

- **d-1 · m006 Q12, fidélité.** Le blanc ⓓ du sujet 2006 (applied / found / asked) a pour réponse « found ». L'auteur a
  écrit « got ». Le correctif D-2 rétablit « found ». Les options officielles de ⓒ sont is leaving / left / leave, et la
  mission met « leaves » à la place de « leave ». C'est défendable (leurre étiqueté
  `simple-pour-action-en-cours`) ; à déclarer.
- **d-2 · m006, forme.** La clé est strictement la plus courte dans 5 questions sur 12 (Q2, Q4, Q5, Q7, Q10). C'est la
  nature des formes d'un même verbe (base sans -s, « is »), et aucune règle de forme n'en sort : les sept autres clés
  portent -s ou sont plus longues. À déclarer, sans correctif.
- **d-3 · m007 Q5 / Q6, même gabarit** (base / -ing / -s / participe identique au prétérit). Rien ne distingue alors le
  participe du prétérit. Remplacer l'option a de Q6, « get » (inventée), par `getted` (étiquette
  `english.tense.ed-sur-verbe-irregulier`), et l'explication par : `hasn't is has + not, so it is followed by a past participle. Get is irregular: get, got, got. "getting" is the -ing form and "gets" the form with -s, which cannot follow hasn't; "getted" adds -ed to an irregular verb.`
  Les trois options officielles (got / getting / gets) restent. Longueurs 6 / 3 / 7 / 4 : la clé est la plus courte
  (2 questions sur 12 dans la mission, pas une répétition).
- **d-4 · m007 Q8 et Q11, options officielles remplacées.** « are » (Q8) et « is writing » (Q11) sont remplacées par des
  formes inventées. Rétablir l'option officielle rendrait la clé strictement la plus longue (Q8 : have been 9 face à
  has been 8 ; Q11 : has written 11 face à is writing 10). Garder les options du fichier et le déclarer.
- **d-5 · m008 Q3, banque 2024 G.** Les leurres ne viennent pas de la banque officielle, contrairement à la consigne.
  C'est défendable : un leurre de la banque rendrait la question lexicale. À déclarer.
- **d-6 · m008 Q9, coquille.** Le sujet imprime « went on her where she (…), Katie was happy ». La mission écrit « went
  on where she ___, but Katie was happy ». La correction est évidente et juste, mais elle n'est pas signalée comme le
  « [sic] » de Q8. À déclarer au rapport (« coquille corrigée »).
- **d-7 · m009 Q1 (multi).** Les distracteurs d (« The price of bricks and cement in different countries ») et f (« A
  story about a holiday in another town ») s'écartent d'un coup d'œil. Remplacer par `d : Advice to people who want to build a house` (confusion décrire / conseiller) et `f : The history of our town and its old houses`. Longueurs
  42 / 42. Les trois bonnes réponses restent indiscernables par la longueur.
- **d-8 · m009 Q2, même geste que m008 Q2** (marqueur de temps fini → simple past, leurre present perfect). La phrase
  est inventée. Garder la question (le temps du récit est demandé par la consigne de tri), mais remplacer l'option b par
  `Last summer, we were building the walls and the roof in two weeks.` (muette) et retirer de l'explication la mention
  de « have built ». L'explication devient : `The article tells events that are over, and "Last summer" is a finished time: the simple past, built. "build" is a present form; "were building" describes an action in progress, but "in two weeks" gives the whole finished work; "will build" is a future form, but the house is already finished.`
- **d-9 · m009 Q5.** La clé est strictement la plus courte (38 contre 67 à 71), et elle recopie la consigne (« tell her
  what happened »). Remplacer par `Your mother, to tell her about the accident that made you so unhappy` (68, à
  égalité avec a).
- **d-10 · m009 Q8, option b.** « has been playing » (present perfect continu) n'est enseigné nulle part. C'est un
  leurre, son « has » le date (present perfect + « Last Sunday »), et le raccourcir rendrait la clé la plus longue.
  Garder.
- **d-11 · m010 Q2.** La clé était la plus courte : corrigé par D-13.

## 3. Points signalés par l'auteur — tranchés

| point | décision |
| --- | --- |
| **m009 Q8 (fichier Q7) because / so** | **Retirer** (D-12) : notion du 07, règle donnée dans l'énoncé puis application directe, leurres faibles, hors notion du chapitre. m017 couvre les connecteurs officiels. |
| **m007 Q10 for / since** | **Retirer** (D-5). Une explication ne peut pas porter une règle que la question exige. Si on la garde : règle dans l'énoncé et d2. Le même manque touche Q1, Q7, Q8, Q11 (D-4). |
| **m010 Q5 unless** | **Garder.** « unless » est défini au cours 05 (Going further : « it means if … not »). Il n'est que leurre : la clé « if » se trouve avec le seul cours. L'explication est juste. |
| **m008 Q11 « moved »** | **Aucune option ne devient juste.** « was moving » est mal accordé, « move » est un présent dans un récit au passé, « will be moving » est un futur dans un récit au passé. La clé officielle « were moving » est la seule. « moved » n'est pas proposé : rien à faire. |
| **m008 Q9 coquille** | Correction juste (« went on her where » → « went on where », « but » ajouté). La déclarer (d-6). Corriger aussi la fuite « laughed at her » (D-7). |
| **m006 Q12 contexte ajouté** | Le contexte fuit vers m007 Q8 et donne la forme de la clé. Remplacer (D-1, D-2), et rétablir « found » (d-1). |
| **m007 Q1 / Q7 même clé ; quatre questions « participe après have »** | **Pas de doublon pour Q1 / Q7** : le repère n'est pas le même (ever since ou for), ni les leurres (choix du temps en Q1, accord et temps en Q7). Parmi les questions sur le participe, Q2 (been, choix du verbe), Q3 (forgotten, piège du prétérit) et Q12 (2×2) sont distinctes. **Q5 et Q6 partagent le même gabarit** : différencier Q6 (d-3). |
| **Ordre trié par difficulté** | Ce n'est pas un défaut. Les difficultés sont croissantes dans chaque fichier, donc l'ordre d'émission est celui du fichier. La session de base reste en tête partout (2021 G, 2024 G, 2026 G, 2023 T, 2018 G). J'ai relu chaque énoncé et chaque explication dans cet ordre **et** dans l'ordre aléatoire du donjon : les fuites trouvées sont D-8, D-10 et D-11. |
| **Étiquette `english.tense.present-avec-marqueur-passe`** | **Le libellé n'est pas exact quand le repère n'est que le récit.** Il dit « un marqueur du passé (yesterday, last…, ago) ». C'est juste pour m008 Q2 (ago), m009 Q2 et Q8 (last), m007 Q9 (« long ago » dans l'énoncé), et à la limite pour m008 Q5 et Q7 (subordonnée « after he got ill », « when Emma was very young »). C'est faux pour m008 Q1, Q4, Q6, Q8, Q9, Q11 et Q12 (repère : les autres verbes du récit). L'erreur exécutée est la même, ne pas mettre au passé un verbe d'un récit au passé : il faut **élargir le libellé** sur `origin/main` plutôt que de laisser les sept options muettes. Texte proposé : fr `Tu laisses le verbe au présent alors qu'un marqueur du passé (yesterday, last…, ago) ou un récit au passé demande un temps du passé.` · en `You leave the verb in the present although a past time word (yesterday, last…, ago) or a story told in the past calls for a past tense.` · ar `تترك الفعل في المضارع مع أنّ مؤشّر الماضي (yesterday, last…, ago) أو سياق القصّة في الماضي يتطلّب زمنًا ماضيًا.` C'est un élargissement : les usages existants restent justes. Si le pilote refuse, rendre muettes les options des sept questions citées. |

## 4. Étiquettes, doublons, divers

- **Étiquettes.** Les 16 étiquettes du lot existent toutes sur `origin/main` ; il n'y a aucune famille nouvelle. Hors
  `present-avec-marqueur-passe` (§ 3), chacune nomme l'erreur que fait l'option.
  - Réserve sur `auxiliaire-mal-accorde` pour « are » en m006 Q4 : « be » y est verbe principal, mais le libellé
    cite is / are. Acceptable.
  - Les options à deux erreurs sont muettes : m007 Q12 « has / changing », m008 Q12 « run / jump ».
  - L'étiquette `must-pour-possibilite` en m010 Q6 est exacte.
- **Doublons.**
  - Pas de doublon publié repris : les items « ne pas redemander » sont respectés, et les seules phrases inventées
    sont celles de m009, permises par la consigne.
  - Gabarit interne : m007 Q5 / Q6 (d-3).
  - Geste répété d'une mission à l'autre : m008 Q2 / m009 Q2 (d-8).
- **Fuites croisées vers les autres lots** (D-3, D-6, D-7, D-9, D-13). Je les ai trouvées en confrontant chaque
  énoncé du lot aux clés des autres blancs des mêmes textes officiels, puis aux affectations L01, L03, L04 et L06.
  Aucune autre trouvée : « uniform », « difficult », « wood », « active », « apprentice », « wheelchair », « mechanic »
  sont des clés d'autres blancs, mais aucune mission ne les pose.
- **Fidélité.** Toutes les phrases citées correspondent aux transcriptions, aux adaptations déclarées près : d-1, d-6
  et D-14 (corrigé).
- **Étages et rampe.** Les en-têtes sont conformes (d2 75/15, d3 120/30), les difficultés croissantes, la session de
  base en tête. m008 en d3 : Q9 à Q12 (progressif, irrégulier de sens proche, 2×2) le justifient.
- **Titres.** Les cinq titres sont conformes à l'affectation, avec leurs étoiles. Tout le texte visible est en
  anglais, et aucune explication ne désigne une option par sa place.
- **`sources[]`.** Non encore ajoutées aux trois `chapter.json` : c'est le pilote qui le fait à la livraison, ce n'est
  pas un défaut.

## 5. Résumé

- **Clés fausses : 0 sur 50.**
- **Critiques : 0.**
- **Majeurs : 14.**
  - Fuites croisées vers L03, L04 et L06 : m006 Q6, m007 Q5, m007 Q11 et m008 Q9, m008 Q4, m010 Q2.
  - Fuites entre questions : m006 Q12 → m007 Q8, m008 Q1 ↔ Q4, m009 Q6 → Q8, m009 Q3 → Q2.
  - since / for non enseigné : m007 Q1, Q7, Q8, Q11 (donnée ajoutée dans l'énoncé) ; m007 Q10 à retirer.
  - Connecteurs because / so : m009 Q7 à retirer.
  - Fidélité : m010 Q6.
- **Mineurs : 11** (fidélité déclarée, gabarit Q5 / Q6, formes de clé, distracteurs faibles).
- **Étiquettes :** élargir le libellé de `english.tense.present-avec-marqueur-passe` ; les autres sont exactes.
- **Doublons :** m007 Q5 / Q6 (gabarit) ; m008 Q2 / m009 Q2 (geste).
- **Verdict : corriger avant livraison.** Douze questions à reprendre avec le texte fourni, deux à retirer (m007 Q10,
  m009 Q7).
