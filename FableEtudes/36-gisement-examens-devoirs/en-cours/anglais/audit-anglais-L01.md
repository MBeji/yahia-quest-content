# Audit indépendant — anglais 9ᵉ, lot L01 (gisement, étude 36)

Périmètre : `content/english/09-reading-comprehension-writing/exercices/06-` à `10-exam-*.json` (m001–m005) et la
ligne `sources[]` du `chapter.json`, branche `wip/gisement-anglais-9eme` (worktree `/home/user/wt-en`).
Sources lues : les cinq transcriptions de session ; les cinq PDF officiels, téléchargés en http depuis
`9web.edunet.tn` (sha256 identiques à ceux des transcriptions), page 1 lue en vision ; les `cours.md` 09 et 04
sur `origin/main` ; `misconceptions.json` sur `origin/main` ; PLAN.md § R2 et R8.
Moteur : `content:check` vert, `content:qa:strict` 0 erreur et aucun avertissement sur `english`,
`content:tranche --chapters 09` : 4/72 clés strictement les plus longues, toutes des « False » (voir § 4).

Chaque question a été résolue avant lecture de la clé. **39 questions auditées, 0 clé fausse.**
Toutes les citations ont été comparées mot à mot au PDF : **aucune citation infidèle**. Aucune question ne
reprend un passage long. Le seul cas limite est m005 Q3, traité au § 3.

## 1. Re-résolution à l'aveugle

### m001 — `06-exam-2026-g-reading-money-values.json` (2026 G)

| Q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 idée générale | taught his children money values | b | OK* | 3 options officielles ; explication qui fuit vers Q8 (M2) |
| 2 V/F 2a | False | b | réserve | l'énoncé souffle le verdict (M3) ; l'explication désigne la preuve (M1) |
| 3 preuve 2a | they didn't just get money if they asked | b | OK | citations conformes au PDF |
| 4 V/F 2b | True | a | réserve | l'explication désigne la preuve (M1) |
| 5 preuve 2b | daughter giving half of her $20 bill | c | OK | « money should be used in three ways » est nécessaire mais pas suffisant : défendable seulement à moitié, et l'explication le dit (acceptable) |
| 6 luxurious | lavish | c | réserve | la citation ne montre que la clé (M4) |
| 7 them | the doors | b | OK | « the squeaks » n'est pas dans le texte (m3) |
| 8 multi OUI | a, c | a, c | OK | b, d, e démentis par le texte |

### m002 — `07-exam-2025-g-reading-bike-bus.json` (2025 G)

| Q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 idée générale | travel to school in a different way | b | OK | 4ᵉ option ajoutée au sujet (m2) ; étiquettes justes |
| 2 matching | physical activity–Health, community–Social life, pollution–environment | idem | OK | appariement unique ; la case « environment » donnée par le sujet devient une paire à trouver (m5) |
| 3 mot défini | ritual | c | réserve | la citation ne montre que la clé (M4) |
| 4 them | the children | d | OK | `referent-le-plus-proche` sur « their bikes » : exact (nom pluriel le plus proche) |
| 5 multi OUI | a, b, e | a, b, e | OK | c et d démentis (vélos donnés à d'autres écoles ; le mercredi seulement) |

### m003 — `08-exam-2024-g-reading-young-blind-pianist.json` (2024 G)

| Q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 idée générale | used music to affect people's lives | d | réserve | l'explication fuit vers Q5 (preuve 2b) et Q8 (M2) ; 4ᵉ option ajoutée (m2) |
| 2 V/F 2a | False | b | réserve | l'explication désigne la preuve (M1) |
| 3 preuve 2a | he taught himself to play the piano | c | OK | |
| 4 V/F 2b | True | a | réserve | « He wants more than an audience » paraphrase la preuve (M1) |
| 5 preuve 2b | set an example to other children who have learning difficulties | b | OK | |
| 6 flying colors | He had excellent exam results. | b | OK | 3 options officielles |
| 7 it | music | d | OK | référent défendable, voir § 3 |
| 8 multi OUI | a, c | a, c | OK | |

### m004 — `09-exam-2026-t-reading-gardening-course.json` (2026 T)

| Q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 idée générale | improve her skills | c | OK | 4ᵉ option ajoutée (m2) |
| 2 V/F 2a | True | a | réserve | « Count them » désigne la preuve (M1) |
| 3 preuve 2a | one night a week after work and every Saturday | c | OK | |
| 4 V/F 2b | False | b | réserve | l'explication désigne la preuve (M1) |
| 5 preuve 2b | that's completely fun | d | réserve | clé la plus courte (m1) ; l'explication fuit vers Q10 (M5) |
| 6 could | possibility | d | OK | « a polite request » est ajouté (m2) ; la possibilité est enseignée au cours 04 |
| 7 exchanging | swapping | c | OK | citation à deux options : sain |
| 8 difficult | tough | b | OK | « terrible » ne veut pas dire « difficult » : clé unique |
| 9 which | plant identification | c | OK | |
| 10 it | my job | c | OK | |

### m005 — `10-exam-2024-t-reading-woman-car-mechanic.json` (2024 T)

| Q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 titre | A young female mechanic | b | réserve | l'explication donne la clé de Q8, « unpaid » (M2) ; sur « young », voir § 3 |
| 2 V/F 2a | False | b | réserve | l'explication désigne la preuve (M1) |
| 3 preuve 2a | Working in many garages was not a good experience | c | OK | |
| 4 V/F 2b | True | a | réserve | l'explication désigne la preuve (M1) |
| 5 preuve 2b | where more women can train to be mechanics | b | OK | |
| 6 matching dates | lessons–1999, company–2006, seller–1992 | idem | OK | dates conformes au PDF ; citations : § 3 ; phrase d'explication sans objet (m4) |
| 7 used to | a habit in the past | d | OK | ajout « a single event… » (m2) ; aucune règle sur « used to » : conforme au plan |
| 8 receiving no money | unpaid | c | OK | la phrase officielle n'est pas citée (m6) |

## 2. Défauts et correctifs

### Majeurs

**M1 — Le découpage vrai/faux : l'explication du verdict désigne la preuve (8 questions).** Le compilateur garde
l'ordre du fichier (même étage d2), donc le verdict précède toujours sa preuve sur la route. Chaque explication de
verdict paraphrase ou situe la phrase qui prouve : « Count them » (m004 Q2), « He wants more than an audience »
(m003 Q4), « how Caroline felt about working in garages » (m005 Q2), « what she hopes to see across the country »
(m005 Q4), « what she does with a $20 bill » (m001 Q4), etc. La question suivante devient alors un simple
repérage. Dans l'autre sens, l'énoncé de chaque preuve est neutre (« settles whether this statement is true or
false ») : il ne donne pas le verdict. Seule l'option clé le révèle, et l'identifier est justement la compétence
évaluée. Le donjon tire au hasard dans tout le parcours, donc il peut montrer la preuve avant le verdict. C'est le
reste inévitable du découpage voulu par le pilote, et il n'appelle pas de correctif.
Correctif : l'explication du verdict donne le verdict et la méthode, sans dire de quoi parle la phrase. Le
contenu reste dans l'explication de la preuve, qui l'enseigne déjà.

| fichier · Q | `explanation` de remplacement |
| --- | --- |
| m001 Q2 | The statement is false: a sentence of paragraph 2 says the opposite. Judge a statement by the words of the paragraph, not by what seems likely for the children of a rich father. |
| m001 Q4 | The statement is true: paragraph 3 gives an example that agrees with it. Judge a statement by the words of the paragraph, not by what seems likely. |
| m003 Q2 | The statement is false: a sentence of paragraph 1 says the opposite. Judge a statement by the words of the paragraph, not by what seems likely for a young pianist. |
| m003 Q4 | The statement is true: a sentence of paragraph 3 says the same in other words. Judge a statement by the words of the paragraph, not by what seems likely. |
| m004 Q2 | The statement is true: a sentence of paragraph 1 says the same in other words. Judge a statement by the words of the paragraph, not by what seems likely. |
| m004 Q4 | The statement is false: a sentence of paragraph 3 says the opposite. Judge a statement by the words of the paragraph, not by what seems likely. |
| m005 Q2 | The statement is false: a sentence of paragraph 2 says the opposite. Judge a statement by the words of the paragraph, not by what seems likely. |
| m005 Q4 | The statement is true: a sentence of paragraph 3 says the same in other words. Judge a statement by the words of the paragraph, not by what seems likely. |

Les clés et les options sont inchangées : aucun effet sur les longueurs.

**M2 — L'explication de Q1 donne la clé d'une question suivante (3 missions).**
- m001 Q1 : « teaches them to give, save and spend » est l'option clé c de Q8, et « a salary for chores » dément le
  distracteur d. Remplacement : `All three paragraphs show how David teaches his children to deal with money: that is teaching money values. He says he would gladly pay for his children's needs, so refusing them is wrong, and nobody in the text raises funds for anyone.`
- m003 Q1 : « to set an example for children with difficulties » donne le verdict ET la preuve de 2b (Q4, Q5), et
  « build his own confidence » donne la clé a de Q8. Remplacement : `Every paragraph shows what Chapman's music does for him and for other people: that is using music to affect people's lives. He started the piano at five, not as a baby, his music is not only for himself, and no competition against adults is mentioned.`
- m005 Q1 : « an unpaid apprentice » livre la clé de Q8 (« receiving no money »). Remplacement, qui règle aussi
  « young » (§ 3) : `The text follows Caroline from her love of cars to her work as a mechanic and her own business, where she trains women and men. A title about a female mechanic covers all of it: "young" is the exam's wording, and "female mechanic" is the part the text proves. Selling cars and training as an apprentice are two early steps of her career, true details that cannot be the title of the whole text.`

**M3 — m001 Q2 (verdict 2a) : l'énoncé souffle le verdict.** « describes what his children must do to be paid »
pose une condition au paiement, donc l'énoncé dément « whenever they want it ». Remplacement de la ligne de
contexte : `The father of the family, a multimillionaire, explains how his children get money. Is the statement below true or false, going by paragraph 2?`

**M4 — Questions « pick out » dont la citation ne contient que la clé (m001 Q6, m002 Q3).** Seule l'option clé
figure dans la phrase citée, ce qui la désigne à vue. Correctif : citer la ou les phrases officielles (deux au
plus) qui contiennent aussi des distracteurs. Ces textes ont été vérifiés sur le PDF.
- m001 Q6, `prompt` : `(Exam 2026, general — reading, question 3, paragraph 1)\nParagraph 1 says: "David Ciccarelli, a multimillionaire, has made it clear that he won't be letting his kids live a lavish life." and "However, I refuse to spend funds on their wants, like a pair of trendy sneakers."\n\nWhich word from paragraph 1 means nearly the same as "luxurious"?`
  Trois options sur quatre sont dans la citation ; « gladly » est ailleurs dans le paragraphe. Ni clé ni
  explication ne changent, et rien ne fuit vers Q8, car « wants » appartient déjà à l'explication de Q8 (b est
  faux).
- m002 Q3, `prompt` : `(Exam 2025, general — reading, question 3, paragraph 3)\nParagraph 3 says: "Balto started the walking school bus project in 2016." and "Given its success, it quickly became a weekly Wednesday ritual at the school..."\n\nWhich word from paragraph 3 means nearly the same as "a series of actions or habits repeated frequently"?`
  Trois options sur quatre (project, success, ritual) sont dans la citation ; « aim » vient de la dernière phrase.

**M5 — m004 Q5 (preuve 2b) : l'explication donne la clé de Q10.** « The two parts about her job describe the hard
side of her work » dit que le « it » de « I love my job but it's a bit depressing » est le métier.
Remplacement : `The writer calls studying gardening "completely fun": only this part says how she feels about her gardening studies, and it says the opposite of the statement.`
Le même lot de correctifs règle m1, plus bas.

### Mineurs

- **m1 — m004 Q5 : la clé « that's completely fun » (21 caractères) est strictement la plus courte** (39, 30, 47).
  Remplacer l'option c par `I'm trying new things` (21 caractères ; le PDF porte « I'm trying new things with my
  own garden, too. »). La clé est alors à égalité pour la plus courte, sans être la plus longue. Ce leurre ne
  prouve rien sur les cours, et il est compatible avec l'explication de M5.
  Sur les questions de référent, la clé (un nom nu) est la plus courte 3 fois sur 5 (m001 Q7, m003 Q7, m004 Q10).
  C'est naturel pour un référent, l'écart est de 2 à 4 caractères, et la tranche ne le relève pas : à surveiller,
  sans correctif imposé.
- **m2 — Options inventées dans des QCM « tels qu'imprimés ».** m002 Q1 (« learn to repair… bikes »), m003 Q1
  (« won a national piano competition… »), m004 Q1 (« win a prize at a flower show »), m004 Q6 (« a polite
  request ») et m005 Q7 (« a single event… ») ajoutent une 4ᵉ option au sujet. Les cinq sont fausses, et
  aucune ne crée de double réponse. m001 Q1, m003 Q6 et m005 Q1 gardent au contraire les trois options
  officielles. Il faut soit retirer l'ajout, soit le déclarer dans la note de la mission (la consigne dit « tel
  qu'imprimé »).
- **m3 — m001 Q7 : « the squeaks »** ne figure pas dans le texte (on y lit « squeaking »), et « his children »
  n'est pas dans la phrase citée. La consigne demande des leurres pris parmi les noms de la phrase. Remplacement :
  `the funds` (9 caractères) ; le paragraphe 1 dit « spend funds ».
  Le texte de l'option devient alors : a « his children », b « the doors », c « my daughters », d « the funds »,
  et la clé n'est plus strictement la plus courte (égalité à 9). Dans l'explication, remplacer « The children and
  the daughters are the people who do the job, not the things that are fixed. » par `The children and the daughters are people, and the funds are money: none of them is what the daughter fixes.`
- **m4 — m005 Q6 (matching)** : la phrase « The dates are not in the order of the events in the list. » parle d'un
  ordre d'affichage que le moteur mélange. La supprimer.
- **m5 — m002 Q2** : la paire « reduces overcrowding and pollution ↔ The environment », que le sujet donne en
  exemple, est ici à trouver alors que la citation la recopie mot pour mot. Ce n'est pas faux et la mission reste
  au niveau d2. Une option serait de la donner dans l'énoncé et de ne garder que deux paires, mais un `matching` à
  deux paires se résout par élimination. **Garder tel quel**, la déviation déclarée.
- **m6 — m005 Q8** : c'est la seule question du lot qui ne redonne pas la phrase officielle. Proposition, sans
  fuite vers m005 Q6 (dont la citation garde « an … apprentice ») : `(Exam 2024, technical — reading, question 5, paragraph 1)\nParagraph 1 says: "But in 1999, I asked the company's manager to take me on as an unpaid apprentice one day a week."\n\nWhich word from paragraph 1 means nearly the same as "receiving no money"?`
  La citation contient alors trois des quatre options (manager, unpaid, apprentice), sans indice de forme.
- **m7 — Étiquettes.** Celles qui sont posées sont exactes : `detail-pris-pour-idee-principale` (m002 Q1 a, c ;
  m005 Q1 a, c) et `referent-le-plus-proche` (m002 Q4 b). Aucune famille neuve n'est proposée, donc la règle des
  3 questions ne s'applique pas. Un ajout est possible : m001 Q1 « raised funds to help the homeless » →
  `english.read.detail-pris-pour-idee-principale` (le libellé dit « une phrase dont les mots sont dans le texte » :
  « homeless » y est). Les autres distracteurs sont muets à bon droit.
- **m8 — Énoncés `multi` au pluriel** (« Which reasons », « Which arguments ») : ils annoncent « au moins deux »,
  ce qui est vrai pour les trois (2, 3 et 2 clés sur 5). Le pluriel reprend celui du sujet (« Why? ») et ne
  permet pas de deviner le nombre exact : acceptable.

## 3. Faits signalés, tranchés

- **Vrai/faux.** Le découpage ne crée aucune fuite de la preuve vers le verdict par l'énoncé : chaque énoncé de
  preuve est neutre. Il crée en revanche une fuite du verdict vers la preuve par l'explication, sur les 8 verdicts
  (M1), plus une par l'énoncé (m001 Q2, M3). Les clés V/F sont équilibrées : 4 True, 4 False.
- **Titre de m005 Q1, « A young female mechanic ».** C'est l'option officielle, la clé du sujet. Le texte décrit
  une adulte : adolescente avant 1992, gérante en 2006, article de 2013. « Young » n'est donc pas prouvé, mais
  aucun autre choix ne convient : « A mechanic apprentice » et « An experienced car seller » sont des étapes du
  début de sa carrière. La clé reste unique et il faut garder la formulation officielle. L'explication doit
  seulement cesser de s'appuyer sur « young » : c'est le texte proposé en M2.
- **Référent de m003 Q4 (« it » → music) : défendable, clé unique.** Grammaticalement, « it » pourrait aussi
  reprendre « his journey » (« his journey will show … how it can offer… »), mais ce mot n'est pas parmi les
  options. Parmi les options, « the incredible benefits » est pluriel, « Chapman » est une personne et « a unique
  opportunity » est l'objet de « offer ». Le sens confirme « music » : la musique offre un moyen de communiquer.
- **Matching de m005 Q3 : citations au-delà de deux phrases.** Ce sont trois fragments coupés de trois phrases
  (environ 37 mots, moins que deux phrases complètes du texte). Le tableau du sujet couvre deux paragraphes, et
  aucun passage long n'est recopié. **Acceptable**, en déclarant la déviation. Pour revenir à la règle des deux
  phrases, on peut retirer le fragment de 1992 (la date se trouve alors par élimination, comme dans le sujet où
  1992 est donné) :
  `(Exam 2024, technical — reading, question 3, paragraphs 1 and 2)\nCaroline Smith's story says: "in 1999, I asked the company's manager to take me on as an … apprentice" and "in 2006, she set up her own business". Before that, she worked for a car company.\n\nMatch each event, as the exam table words it, with its date.`
  C'est facultatif. La paire de 1992 était de toute façon recopiée mot pour mot.
- **Clé en c dans 37 % des questions : pas un défaut.** `shuffleOptions` (`src/shared/lib/question-utils.ts`)
  mélange les options à chaque affichage, sur la route, au donjon, à l'examen et en duel. L'élève ne voit jamais la
  lettre. Au plus une question de rangement, sans correctif.
- **« False » plus long que « True » d'un caractère : pas un défaut.** Les deux options sont toujours les mêmes,
  présentes dans chaque item et mélangées à l'affichage, et les clés sont équilibrées (4/4). La longueur ne dit
  donc rien. Les 4 « clés les plus longues » de `content:tranche` sont ces faux positifs.

## 4. Divers

- **Étages et rampe** : les cinq missions sont en d2 practice 75/15, avec une rampe 1 → 2 → 3 non décroissante, et
  le nombre de questions respecte les plafonds (8, 5, 8, 10, 8). Les titres sont ceux de l'assignation.
- **Notions** : idée générale et titre, scanning et vérification d'un énoncé, transfert d'information,
  référents (y compris « which »), mot en contexte et inférence sont enseignés au cours 09 ; « could » de
  possibilité l'est au cours 04. « used to » n'est pas enseigné, mais l'explication n'en donne que le sens,
  conformément au plan.
- **Langue** : tout le texte visible est en anglais, aucune explication ne désigne une option par sa lettre, et
  les graphies du texte sont gardées (colors, favorite).
- **Doublons** : aucun des cinq textes ne figure ailleurs dans `content/english/` (recherche par grep). La
  consigne « ne pas redemander » est respectée : seuls des textes officiels sont utilisés. Le gabarit
  vrai/faux → preuve revient dans quatre missions, mais sur quatre textes différents : ce n'est pas un doublon.
- **`chapter.json`** : la ligne `sources[]` d'étude 36 est présente et conforme à R8.

## Résumé

39 questions re-résolues à l'aveugle. **Clés fausses : 0.** Citations fidèles au PDF : 39/39.
**Majeurs : 5**, qui portent sur 15 questions : fuite verdict → preuve dans les 8 explications de verdict ;
explication de Q1 qui donne la clé d'une question suivante (m001, m003, m005) ; énoncé qui souffle le verdict
(m001 Q2) ; citation « pick out » réduite à la clé (m001 Q6, m002 Q3) ; explication de preuve qui donne le
référent (m004 Q5 → Q10).
**Mineurs : 8** : clé la plus courte (m004 Q5), options ajoutées aux QCM officiels, leurre « the squeaks »,
phrase d'explication sans objet, paire d'exemple, phrase non citée (m005 Q8), une étiquette à ajouter, pluriel
des `multi`.
**Étiquettes** : 5 posées, toutes exactes, aucune famille neuve. **Doublons** : aucun.
**Verdict : à corriger avant fusion.** Les correctifs portent sur le texte (explications, énoncés, une option)
et aucune clé ne change.
