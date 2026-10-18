# Audit B1 — anglais 6ᵉ, chapitres 01 et 02

Auditeur indépendant (opus), 2026-10-18, sur l'arbre `wip/anglais-6eme-un-passage` au commit `2aa89cc4`.
Je n'ai modifié aucun fichier de `content/` et je n'ai fait aucune écriture git. J'ai d'abord re-résolu à l'aveugle
les 36 + 15 questions des six missions (sans clé ni explication), puis j'ai comparé. J'ai ensuite relu
les 70 questions existantes (quiz, 01–05) contre `origin/main` : réécritures, étiquettes, paires d'éléments.
Sources relues : les transcriptions 2008, 2009, 2010, 2012, 2013, 2015–2021 et 2023–2026, ainsi que le PDF 2023 p. 1
(texte du reading, cité fidèlement). J'ai lu le rapport de l'auteur (§ 6) seulement après.

Gates relancés depuis `/home/user/eng-deliver` :
- `content:check` : vert ;
- `content:qa -- --subject english-6eme` : aucune clé suspecte ;
- `content:tranche --chapters 01,02 --strict-longest` : clé strictement la plus longue 0/110,
  positions 27/27/25/21 %, aucune paire proche, 2 groupes de gabarits (jugés au § 4).

## 1. Re-résolution — missions neuves (51 questions)

### 01 / 06 — m001 (Exams 2008–2025 · like + -ing, how often, -s), 12 q.

| q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | always | d | OK | 2023 L1 blanc 1, banque fidèle (many, stomachache, never) |
| 2 | sometimes | a | réserve | « to collect » n'est pas dans la banque 2024 (« collect ») alors que l'énoncé dit « from the box » (m-1) |
| 3 | swimming | b | OK | 2018 L2 |
| 4 | goes | c | OK | 2013 L2 |
| 5 | likes | d | réserve | « like » ajouté hors banque, énoncé « from the box » (m-1) |
| 6 | in | a | OK | 2010 L1 |
| 7 | Emma usually walks her dog on the weekends | c e b d a | **ordre non unique** | « On the weekends, Emma usually walks her dog » est juste ; seule la minuscule l'écarte (M-6) |
| 8 | Children like eating sandwiches | b d a c | OK | « Children » imprimé en gras, début fixé |
| 9 | Alex likes playing the guitar | c b d a | OK | |
| 10 | I go to the zoo on Sundays | b d c a | **ordre non unique** | « On Sundays I go to the zoo » est juste ; seule la minuscule l'écarte (M-6, doute 3) |
| 11 | He lives in Paris | b | OK | 2017 W1 |
| 12 | I usually drink milk or juice | c | OK | 2015 W1 |

### 01 / 07 — m002 (Exams 2008–2021 · possessives and linkers), 9 q.

| q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | because | a | **deux réponses** | « …different bedrooms **and** they like different colours » est juste, et le cours dit lui-même que « and joins two ideas that go together » (C-1) |
| 2 | his | c | OK | |
| 3 | and | d | OK | |
| 4 | His | b | OK | |
| 5 | but | a | OK | doute 4 : « and » a bien fait de sortir ; because, then et so ne sont pas défendables |
| 6 | Their | d | OK | |
| 7 | but | b | OK (réserve) | « and » est grammatical, mais le cours (l. 91) enseigne « the second idea is the opposite, so but joins it, not and » : clé unique selon le cours |
| 8 | his | a | OK | |
| 9 | His | c | OK | |

### 01 / 08 — m003 (Exams 2023, 2026 · dialogues), 8 q.

| q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | invites | a | réserve | b « suggestion for the two of them » est littéralement vrai de « …with me » ; la clé est unique selon le cours (m-3, doute 2) |
| 2 | refuses politely | c | OK | |
| 3 | b e d a c | b e d a c | OK | ordre unique ; la ligne 1 est donnée par le sujet |
| 4 | suggests another activity | b | OK | |
| 5 | accepts and proposes | d | réserve | « At the end of the conversation » livre la place de c dans l'ordering q3 (m-4) |
| 6 | 1→r2, 2→r3, 3→r1 | idem | OK | appariement unique ; 3 paires sans intrus (doute 6, § 5) |
| 7 | What about the party invitations? | a | OK | |
| 8 | Can you help with the food? | c | OK | |

### 01 / 09 — m004 (Exam 2023 · reading), 7 q.

Les citations sont fidèles au PDF : « After lunchtime, the competition starts », « In her wheelchair, Zoey comes », « let's welcome the best artist of our school, Zoey! », « we are proud of you, Zoey! ».

| q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | in the afternoon | d | OK | |
| 2 | False, she draws them | a | **réserve majeure** | d « False: her favourite hobby is drawing, so she never plays outside » ne se réfute pas avec la seule citation donnée (M-5) |
| 3 | True, very excited | b | OK | |
| 4 | best … gift | a | OK | « prize » n'est pas dans le § 3. L'énoncé cite les deux mots : la question est facile pour un d2 (mineur) |
| 5 | wheelchair | c | OK | |
| 6 | Zoey wins the school drawing competition | b | OK | |
| 7 | best artist | b | **réserve majeure** | l'énoncé pose la cause dans sa narration (« after the headmistress calls her the best artist ») ; c « because she is sad » et d « because she flew a kite » sont absurdes (M-4) |

### 02 / 06 — m005 (Exams 2010–2025 · should, must, can, How much), 7 q.

| q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | stomachache | a | OK | |
| 2 | much | c | OK | |
| 3 | can | d | OK | 2013 L2 |
| 4 | many, never | b, c | **défaut** | le nombre se compte (5 mots − 3 blancs = 2), et chaque blanc est déjà demandé (q1, q2, m001 q1) (M-2, doute 1) |
| 5 | Jane can't help with cleaning because she has a stomachache | b e d a c | **ordre non unique** | « Because she has a stomachache, Jane can't help with cleaning » est juste (M-6) |
| 6 | can't | a | OK | 2018 L2 |
| 7 | playgrounds→school, milk→fridge, eggs→basket | idem | **défaut** | paires inventées sous l'étiquette « (Exam 2020) » ; elles reprennent le quiz#5 (eggs / milk), sur la liste « ne pas redemander » (M-1) |

### 02 / 07 — m006 (Exam 2024 · writing prepared), 8 q.

| q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 | what Doctor James advised | a | OK | consigne fidèle |
| 2 | a, c, e | a, c, e | **doublon** | e et f sont mot pour mot la clé et un distracteur de `02/03-revision#3` (liste « ne pas redemander ») (M-3) |
| 3 | Dear Sami(a) … Yours, Fadi(a) | b | OK | cadre imprimé fidèle ; plan 2×2, option double muette |
| 4 | Doctor James told us… | b | réserve | la clé emploie « told us to drink », du discours rapporté (HP, E6) (m-6) |
| 5 | c d a b | c d a b | OK | « Give his advice » : « his » renvoie à d (mineur, m-6) |
| 6 | should | a | **doublon** | même phrase-clé que `02/03-revision#3` (M-3) |
| 7 | must | d | OK | phrase-clé reprise de l'exemple du cours (l. 145) : admis |
| 8 | shouldn't | c | **doublon** | clé, sujet (sweets) et distracteur « don't should » repris de `02/quiz#2` (liste « ne pas redemander ») (M-3) |

**Clés fausses : 0 sur 51.**

## 2. Fichiers existants (70 questions) : réécritures et étiquettes

Toutes les clés re-résolues concordent, y compris les réécritures `tranche` (01 quiz#4, quiz#5, 01-pratique#4,
03-revision#4, 04-defi#5, 05-entrainement#2 ; 02 02-boss#1, 02-boss#6, 03-revision#2, 03-revision#4,
05-entrainement#1, 05-entrainement#4).

| fichier#q | verdict | motif |
| --- | --- | --- |
| 01/01-pratique#4 | **deux réponses** | « I enjoy gardening **and** I love flowers » est juste, et ce sont des « ideas that go together » selon le cours. Défaut antérieur, mais la question a été réécrite dans ce lot (C-2) |
| 01/quiz#5 | mineur | « theirs » n'est enseigné nulle part (pronom possessif) ; l'élève ne peut pas en juger (m-7) |
| 01/03-revision#4 | mineur | « Yes, I do. » et « Yes, I do, thank you. » tombent ensemble (options recouvrantes) (m-8) |
| 01/03-revision#6 c, d | étiquette | restaurant et let's : l'élève qui les choisit leur prête /z/, ce qui n'est pas lire « d'après les lettres ». `lettre-pour-son` ne nomme pas cette erreur → les rendre muettes (E-1) |
| 01/04-defi#2 c | étiquette | « In both words the s buzzes » : même raison, à rendre muette ; d (« both hiss ») est bien la lecture d'après la lettre et garde l'étiquette (E-1) |
| 01/05-entrainement#2 | étiquette (doute 5) | dislike + to / base : erreur réelle, mais le libellé n'inclut pas dislike → élargir le libellé (E-2) |
| 02/01-pratique#3 d | étiquette | « must to » cumule deux erreurs (must au lieu de mustn't, et to) → muette (E-3) |
| 02/01-pratique#5 c | étiquette | « She cans swim » cumule deux erreurs (can au lieu de can't, et -s) → muette (E-3) |
| 02/01-pratique#6 b | étiquette | « How much apple are there? » cumule deux erreurs (much, et apple sans -s) → muette (E-3) |
| 02/05-entrainement#1 a | étiquette (doute 5) | fit et sit : lire « i » comme le /i/ tendu du français relève bien de la lecture d'après la lettre (acceptable). rabbit : la voyelle accentuée est un a, aucune lecture d'après la lettre n'y mène → muette (E-1) |
| 02/03-revision#4 | OK (doute 7) | « cleaning product » : mustn't est l'unique clé (ni shouldn't ni can parmi les options) ; « don't must » est faux ; âge adapté |
| 02/04-defi#1 d | mineur | « You mustn't eat that, it is bad for you. » est une virgule de jonction, dans une question « correct English » (m-9) |
| 02/05-entrainement#4 | OK | la paire proche avec 01-pratique#6 est levée (pasta indénombrable / apples dénombrables) |

`mot-voisin-du-meme-champ` (doute 5, E7) : toutes les poses relues sont légitimes. L'option est chaque fois un
mot du même champ que la clé, et un indice de l'énoncé tranche :
- 01/01-pratique#1 : loisirs, indice rod + river ;
- 01/01-pratique#5 : adverbes de fréquence, indice every evening ;
- 01/03-revision#1 : loisirs, indice rope ;
- 01/05-entrainement#1 : lieux, indice old objects ;
- 02/quiz#1 : en-cas, indice healthy ;
- 02/01-pratique#1 et 02/03-revision#1 : aliments ;
- 02/01-pratique#4 et 02/03-revision#2 : maux ;
- m001 q1 : never face à always, indice cannot keep fit ;
- m004 q1 : lunchtime face à afternoon, indice After.

Aucune pose sur un distracteur absurde.

Les autres étiquettes relues nomment exactement l'erreur, et les options à deux erreurs sont muettes :
- plans 2×2 : 01/02-boss#2, 05-entrainement#3, 05-entrainement#4, 04-defi#4 ; 02/quiz#5, 02-boss#3, 02-boss#5, 04-defi#6 ;
- m006 q3.

Aucune étiquette ne porte sur un `multi`, un `ordering` ou un `matching`.

`coursePitfalls` (01 : ing-oublie, to-en-trop, possessif-du-mauvais-possesseur, frequence-mal-placee,
s-oublie-3e-personne ; 02 : to-en-trop, s-sur-le-modal, etre-et-avoir, many-much, fonction-confondue) :
chacun est enseigné par le cours (« classic mistake » ou règle avec contre-exemple) et porté par au moins un
distracteur. OK.

## 3. Défauts classés et correctifs (textes vérifiés : longueur de clé, clé unique, aucune fuite)

### Critiques — double réponse défendable (clé non fausse)

**C-1 · `01-entertaining-myself/exercices/07-exams-2008-2021-possessives-and-linkers.json` q1.**
Prompt → `(Exam 2021) A text describes Mary's house in Liverpool, where she lives with her brother Sam, and says why they have different bedrooms. Which word completes the sentence?\n\n"Mary and Sam have different bedrooms ___ they like different colours."`
Les options et la clé restent inchangées. « and » ne répond plus au « why ». « from the box » est retiré, car and, but et because of
ne sont pas dans la banque 2021.

**C-2 · `01-entertaining-myself/exercices/01-pratique.json` q4.**
Prompt → `Your friend asks: "Why do you enjoy gardening?" Complete your answer: "I enjoy gardening ___ I love flowers."`
Début de l'explication → `The question Why asks for a reason, and the reason is opened by because: I enjoy gardening because I love flowers.`
La suite reste inchangée, les options aussi (clé because, 7 lettres, face à « because of » qui en a 10).

### Majeurs

**M-1 · m005 q7 (matching « Exam 2020 »).** Les paires eggs/milk/basket/fridge sont inventées sous une étiquette d'examen
(E4 : « ne convertir que ce qui garde la phrase officielle »). Elles redemandent aussi `02/quiz#5`
(« ___ eggs … ___ milk »), qui figure sur la liste « ne pas redemander ». Le correctif remplace la question par un QCM fidèle
(2020 L1, « How many playgrounds + are there? »), placé en d1 après q3 :
- prompt : `(Exam 2020) A pupil writes a question about his school. Which words complete it?\n\n"___ playgrounds are there?"`
- options : a `How many` · b `How much` {`english.quant.many-much-confondus`} · c `How often` · d `How old` ; clé **a**
  (8 caractères face à 8, 9 et 7 : la clé n'est pas la plus longue) ;
- explication : `Playgrounds carry an -s and you can count them one by one, so the question word is How many: How many playgrounds are there? How much is for things you cannot count, How often asks about a habit, and How old asks about age.`
- vérification : « How much/often/old playgrounds are there? » est agrammatical ; le cours (l. 346) enseigne « How many … are there? ».
  Aucune fuite vers q1–q6.

**M-2 · m005 q4 (multi « extra words »).** Le nombre de bonnes réponses se déduit : 5 mots pour 3 blancs, donc 2 en trop.
Les trois blancs sont déjà demandés : q1 (stomachache), q2 (much) et m001 q1 (always). La question n'apporte donc rien,
sinon la recomposition des trois autres. Correctif : **supprimer q4**. m005 passe à 6 questions (d1 ×4, d2 ×2,
rampe croissante). L'exercice 2023 L1 reste ainsi partagé sans redite : blanc 1 en 01 (fréquence), blancs 2–3 en 02.

**M-3 · m006 q2, q6, q8 (doublons des items « ne pas redemander »).**
- q2 : remplacer e → `You should sleep nine hours every night.` et f → `You should eat crisps for breakfast.`
  La clé reste **a, c, e**.
  Explication → `A doctor who talks about keeping fit advises eating fruit and vegetables, drinking water and sleeping well. Sleeping at three in the morning, eating sweets before every meal and eating crisps for breakfast are the opposite of a healthy life, so they do not belong to this advice.`
- q6 : prompt → `(Exam 2024) In his talk, Doctor James gives a good idea: walking to school every day. It is up to each student to follow it. How do you write this advice in your e-mail?`
  Options :
  - a `You should walk to school every day.` (clé, 36 caractères) ;
  - b `You must walk to school every day.` {fonction-confondue} (34) ;
  - c `You should to walk to school every day.` {to-en-trop} (39) ;
  - d `You shoulds walk to school every day.` {s-sur-le-modal} (37).

  Explication : remplacer « play sport twice a week » par « walk to school every day ».
  q2 corrigé ne contient plus cette idée : pas de fuite.
- q8 : prompt → `(Exam 2024) Doctor James warns about screens: watching TV late at night is a bad idea, although nothing is forbidden. How do you write it in your e-mail?`
  Options :
  - a `You mustn't watch TV late at night.` {fonction-confondue} (35) ;
  - b `You shouldn't watching TV late at night.` {base-verbale-deformee} (40) ;
  - c `You shouldn't watch TV late at night.` (clé, 37) ;
  - d `You don't should watch TV late at night.` (40, muette).

  Explication : remplacer « You shouldn't eat lots of sweets » par « You shouldn't watch TV late at night ».

**M-4 · m004 q7.** Deux distracteurs absurdes, et la cause est donnée par la narration de l'énoncé.
- Prompt → `(Exam 2023, reading) At the end of the text, the headmistress says: "let's welcome the best artist of our school, Zoey!" Then Zoey's teachers and friends hug her and tell her: "we are proud of you, Zoey!" Why are they proud of her?`
- Options :
  - c → `because she plays volleyball very well` {`english.read.reponse-sans-appui-dans-le-texte`} (38) ;
  - d → `because she helps the art teachers get ready for the event` (58, muette).

  La clé b (44) n'est ni la plus longue ni la plus courte ; a est inchangé (59).
- Explication, dernière phrase → `A birthday, playing volleyball very well or helping the teachers are not the reason the text gives: the headmistress has just named her the best artist of the school.`

**M-5 · m004 q2.** d « so she never plays outside » ne se réfute pas avec les deux phrases citées.
- Prompt : ajouter en tête de la citation la 2ᵉ phrase du texte →
  `A text says about Zoey: "She enjoys flying kites and playing volleyball in the playground. But her favourite hobby is drawing. She always draws pictures of her friends jumping and swinging."`
  La suite reste inchangée.
- d → `False: she never plays in the playground, she only draws` (56 ; la clé a fait 66, b 74, c 59).
- Explication, dernière phrase → `The idea that she never plays in the playground is false: the text says that she plays volleyball there.`

Cette phrase ne fuit pas vers q6 : son option a, « Zoey flies kites… », reste un détail vrai et faux comme titre.

**M-6 · ordering à ordre non unique (doute 3) : m001 q7, m001 q10, m005 q5.**
La casse ne suffit pas : l'app compare l'ordre exact, et un élève de 11 ans qui écrit « On Sundays I go to the zoo » a raison.
Le correctif fixe le premier mot, comme le cadre imprimé du sujet 2008 (« I ........ . »), et ferme la phrase par un point :
- m001 q10 : ajouter au prompt ` The sentence starts with I.` ; option a → `Sundays.` ; ordre inchangé (b d c a).
- m001 q7 : ajouter au prompt ` The sentence starts with Emma.` ; option a → `on the weekends.` ; ordre inchangé (c e b d a).
- m005 q5 : ajouter au prompt ` The sentence starts with Jane.` ; option c → `she has a stomachache.` ; ordre inchangé (b e d a c).

Vérification : chaque fois, le premier et le dernier segment sont fixés. Il reste une seule place grammaticale pour
l'adverbe (avant le verbe) et pour « because » (devant la cause).

### Mineurs

- **m-1 · fidélité « from the box ».**
  - m001 q2 : « to collect » n'est pas dans la banque. Garder l'option (« collect » nu rendrait la clé strictement la plus longue, 9 > 7)
    et écrire `Which word completes the sentence?`. Explication : « to collect is a verb form » reste juste.
  - m001 q5 : idem, `Which word completes the sentence?` (« like » est hors banque).
- **m-2 · `sources[]` des deux `chapter.json`.** L'examen n'est pas le « concours national de fin d'études de l'enseignement
  de base ». C'est le concours d'entrée aux collèges pilotes (en-tête de toutes les transcriptions). Remplacer le
  début de la 3ᵉ ligne par
  `Sujets officiels du concours d'entrée aux collèges pilotes (6ᵉ année de base, « مناظرة الدخول إلى المدارس الإعدادية النموذجية »), Ministère de l'Éducation (corpus officiel, reprise citée, étude 36)`.
  La fin reste inchangée.
- **m-3 · m003 q1 (doute 2).** La clé est unique pour qui a lu le cours : « Would you like to » = invitation, et 01/04-defi#5 le dit en toutes lettres.
  Mais b est littéralement vrai de « …with me ». b → `He makes a suggestion, like Let's play.` (39 ; clé 24)
  {fonction-mal-identifiee}. L'explication reste juste.
- **m-4 · m003 q5.** Retirer `At the end of the conversation, ` du prompt → `(Exam 2023) Alex says: "Great idea! Let's play and see who will win." What does Alex do?`
  Ce bout de phrase livre la place de c dans l'ordering q3, que le donjon tire au hasard.
- **m-5 · m004 q4.** L'énoncé cite les deux mots-clés : c'est une question de d1 plutôt que de d2. On peut l'accepter (l'énoncé
  doit se suffire) ou la passer en d1 à la tête du fichier.
- **m-6 · m006.**
  - q4 : clé → `Doctor James says we should drink lots of water.` (48), pour retirer « told us to », du discours rapporté (E6).
    Il faut alors rallonger d → `Last summer I went to the sea with my cousin Ali.` (49), sinon la clé devient la plus longue.
    Explication : « The sentence about the water » reste juste.
  - q5 : a → `Give Doctor James's advice with You should and You must`.
- **m-7 · 01/quiz#5.** d `theirs` → `they're` (7 ; clé « their » 5).
  Fin de l'explication → `and "they're" is the short form of they are, not a possessive.`
- **m-8 · 01/03-revision#4.** c → `Yes, I like it a lot.` (21 ; clé 17).
  Explication, 2ᵉ phrase → `The three other answers echo the wrong verb: the question does not start with Are you or Do you, and "Yes, I like it a lot" talks about a taste, not about an invitation.`
- **m-9 · 02/04-defi#1.** d → `You mustn't eat sweets before you go to bed.` (44 ; la clé fautive fait 24).
- **m-10 · gabarits inter-chapitres.**
  - « Three of these … are correct. Which one is NOT correct? » (01/04-defi#1, 02/04-defi#1) : le geste est le même,
    mais la notion diffère (Let's / How about face à modal + base). Accepté.
  - « Read … which sentence about … is true » : 01/04-defi#6 (goûts) est distinct. 02/02-boss#6 (Sami, unfit → can't) et
    02/05-entrainement#5 (Meriem, fit → can) sont des miroirs dans le même chapitre : exercice parallèle accepté,
    à varier si la vague 2 retouche le 02.

### Étiquettes

- **E-1** : rendre muettes 01/03-revision#6 c et d, 01/04-defi#2 c et 02/05-entrainement#1 a (rabbit).
  Les autres poses de `lettre-pour-son` sont honnêtes : 01/04-defi#2 d, 02/05-entrainement#1 b et d.
- **E-2** (doute 5, dislike) : l'erreur est réelle, car dislike se construit comme enjoy (-ing seul). Il faut élargir le libellé
  de `english.verb.ing-oublie` plutôt que retirer l'étiquette :
  - fr : `Tu mets to ou la base verbale après enjoy, dislike, mind, finish, regret, How about, What about ou une préposition (of, before), ou la base verbale seule après like, love, hate : le verbe prend -ing (I enjoy swimming, How about going, I like reading).`
  - en : `You use to or the base verb after enjoy, dislike, mind, finish, regret, How about, What about or a preposition (of, before), or the bare base verb after like, love, hate: the verb takes -ing (I enjoy swimming, How about going, I like reading).`
  - ar : insérer `وdislike` après `enjoy` dans la première énumération.
- **E-3** : rendre muettes les options à deux erreurs 02/01-pratique#3 d, 02/01-pratique#5 c et 02/01-pratique#6 b.
  Ces trois retraits ramènent l'étiquetage du 02 de quelques points : un chapitre honnête sous 60 % reste
  acceptable (décision E7 du pilote).

## 4. Fuites, doublons, notions, étages

- **Fuites.** Celles que j'ai trouvées sont traitées plus haut : m003 q5 → q3 (m-4) ; m006 q2 → q6 (M-3) ; m005 q4,
  recomposée à partir de q1, q2 et m001 q1 (M-2). Les explications relues ne résolvent aucune question suivante.
- **Notions.** Tout ce qui est testé est enseigné par le cours du chapitre ou par celui du 01 :
  - adverbes, on/in, Let's / How about / What about, Would you like to, possessifs, /s/–/z/ ;
  - should, must, can, have a / be, How many / How much, i / ee.

  Hors guide : « theirs » (m-7). Les répliques en will, should et must de m003 sont lues pour leur fonction seulement
  (placement D2), ce qui est conforme à la note de la carte.
- **Âge.** Les contextes conviennent à 11–12 ans ; le « cleaning product » (doute 7) est adapté.
- **Étages et titres.** m006 est un boss d3 dont les questions sont surtout en d2 : c'est l'étage de la carte, et il est accepté.
  Les titres portent leur ⭐ et ne livrent aucune clé.

## 5. Doutes de l'auteur — tranchés

1. **Ashley (2023 L1).**
   - Le multi de m005 est bien une fuite et une redite : à supprimer (M-2).
   - Le partage blanc 1 → m001 / blancs 2–3 → m005 n'est ni une redite ni une fuite : à garder.
2. **m003 q1.** La clé est unique selon le cours, mais b est littéralement vrai : reformuler (m-3).
3. **m001 q10.** La casse ne suffit pas, et le même défaut touche m001 q7 et m005 q5 : il faut un premier mot imposé
   et un point final (M-6).
4. **m002 q5.** C'était juste de retirer « and » ; les distracteurs restants ne sont pas défendables. En revanche, le même « and »
   reste défendable en m002 q1 et en 01/01-pratique#4 (C-1, C-2). En m002 q7, le cours tranche pour « but ».
5. **Étiquettes.**
   - `mot-voisin-du-meme-champ` : toutes valides.
   - `ing-oublie` sur dislike : erreur exacte, élargir le libellé (E-2).
   - `lettre-pour-son` : honnête sur fit et sit, à retirer sur rabbit et sur les choix /z/ du 01 (E-1).
6. **Écarts à la carte.**
   - m005 à 7 questions (6 après M-2) : accepté.
   - Matching de m003 à 3 paires : accepté. Le 4ᵉ cercle du sujet est ambigu (« I will make a playlist » ou
     « What about the party invitations? » devant « The party will be so cool »), et l'en retirer est le bon choix.
   - Vrai/faux + preuve fondus en m004 : accepté, sous réserve de M-5.
7. **02/03-revision#4.** La clé mustn't est maintenant unique.

## 6. Bilan

| chapitre | questions auditées | clés fausses | critiques (double réponse) | majeurs | mineurs | étiquettes à corriger |
| --- | --- | --- | --- | --- | --- | --- |
| 01 | 71 | 0 | 2 (C-1, C-2) | 3 (M-4, M-5, M-6 ×2) | 7 | 3 options |
| 02 | 50 | 0 | 0 | 4 (M-1, M-2, M-3, M-6 ×1) | 3 | 4 options + libellé ing-oublie |
| **total** | **121** | **0** | **2** | **6 défauts (11 questions)** | **10** | **7 options + 1 libellé** |

**Verdict : à corriger d'abord.** Aucune clé n'est fausse, et les gates sont verts. Mais il y a deux doubles réponses (« and »),
trois ordres non uniques, une matching inventée qui redemande le quiz, un multi déductible et trois doublons d'items
« ne pas redemander » en m006. Tous les correctifs ci-dessus sont des textes de remplacement vérifiés (clé ni la plus longue
ni unique au vote, aucune fuite créée). Une contre-vérification rapide suffira après la correction.

## 7. Re-vérification (commit `f2043dc5`)

J'ai re-résolu à l'aveugle les 25 questions modifiées depuis `2aa89cc4`, et toutes les clés concordent. Les gates passent depuis
`/home/user/eng-deliver` :
- `content:check` : vert ;
- `content:qa -- --subject english-6eme` : aucune clé suspecte ;
- `content:tranche --chapters 01,02 --fresh --strict-longest` : clé la plus longue 0/54, aucune paire proche, mêmes 2 gabarits, acceptés (m-10).

| défaut | état | contrôle |
| --- | --- | --- |
| C-1 m002 q1 | corrigé | le « why » est posé : « because » est la seule réponse, et « from the box » est retiré |
| C-2 01/01-pratique#4 | corrigé | prompt « Why do you enjoy gardening? » et explication conformes |
| M-1 m005 matching | corrigé | QCM 2020 « ___ playgrounds are there? », clé How many (8 / 8 / 9 / 7), en d1 après q3 ; la matching est retirée |
| M-2 m005 multi | corrigé | supprimé ; m005 compte 6 questions (d1 ×4, ordering d2, d2), rampe croissante |
| M-3 m006 q2, q6, q8 | corrigé | textes conformes ; plus de reprise de 02/03-revision#3 ni de 02/quiz#2 ; q2 ne contient plus « walk » ni « TV » |
| M-4 m004 q7 | corrigé | la cause n'est plus dans la narration ; c et d sont plausibles ; clé b (44) au milieu (59 / 38 / 58) |
| M-5 m004 q2 | corrigé | la phrase volleyball est citée ; d se réfute par le texte ; clé 66 < b 74 |
| M-6 ordering m001 q7, q10, m005 q5 | corrigé | premier mot imposé et dernier segment ponctué : ordre unique |
| m-1 « from the box » | corrigé | m001 q2 et q5 |
| m-2 `sources[]` | corrigé (pilote) | « concours d'entrée aux collèges pilotes (6ᵉ année de base) » dans les deux `chapter.json` |
| m-3 m003 q1 | corrigé | b « He makes a suggestion, like Let's play. » |
| m-4 m003 q5 | corrigé | « At the end of the conversation » est retiré |
| m-5 m004 q4 | laissé (accepté) | la question reste d2 : facile, mais l'énoncé doit se suffire |
| m-6 m006 q4, q5 | corrigé | clé 48 < d 49 ; « Doctor James's advice » |
| m-7 01/quiz#5 | corrigé | « they're » et explication |
| m-8 01/03-revision#4 | corrigé | « Yes, I like it a lot. » et explication |
| m-9 02/04-defi#1 | corrigé | d « You mustn't eat sweets before you go to bed. » est correct ; c reste l'unique fautive |
| E-1 | corrigé | 01/03-revision#6 c et d, 01/04-defi#2 c, 02/05-entrainement#1 rabbit sont muets |
| E-2 | corrigé (pilote) | libellé `english.verb.ing-oublie` élargi à « dislike » en fr, en et ar |
| E-3 | corrigé | 02/01-pratique#3 d, #5 c, #6 b sont muets |

Il reste un seul point, mineur et non bloquant : la première phrase de l'explication de m004 q7 dit encore « the reason of the hug »,
alors que la question porte sur la fierté, et la fin répète cette même phrase. Texte proposé :
`They tell her that they are proud of her, and the headmistress has just named her the best artist of the school: that is why they are proud. A birthday, playing volleyball very well or helping the art teachers are reasons that the text does not give.`

**Verdict final : prêt à armer.** Aucune clé n'est fausse, aucun défaut critique ou majeur ne reste, et la retouche de l'explication
de m004 q7 est facultative.
