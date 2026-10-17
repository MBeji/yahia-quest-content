# Audit indépendant — lot L03 (anglais 9ᵉ, gisement étude 36)

> Auditeur indépendant, 2026-10-17 (reprise après coupure API ; aucun rapport antérieur n'existait).
> Branche `wip/gisement-anglais-9eme`, commit `a99787bc`. Fichiers audités (aucun modifié) :
> `content/english/04-modals/exercices/06-exams-2001-2023-modals-meaning-and-form.json` (m011),
> `…/04-modals/exercices/07-exams-2009-2026-writing-advise-warn-set-rules.json` (m012),
> `…/08-relative-clauses-comparatives/exercices/06-exams-2002-2026-relative-pronouns.json` (m013),
> `…/08-…/exercices/07-exams-2002-2025-comparative-or-superlative.json` (m014),
> `…/08-…/exercices/08-exams-2002-2026-building-the-comparison.json` (m015).
> Sources : transcriptions officielles, `cours.md` / `resume.md` des chapitres sur `origin/main`, missions et quiz
> publiés, registre `content/misconceptions.json` sur `origin/main`. Les lignes `sources[]` des `chapter.json`
> 04 et 08 sont ajoutées par le pilote à la livraison : non comptées.
> Numérotation : Qn = position dans le fichier (ordre `displayOrder` de la route).

---

## m011 — 04/06 « modals in exam texts: meaning and form » (d2 practice 75/15, 11 q.)

| Q | session | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- | --- |
| 1 | 2022 T | use | b use | OK | modal + base ; banque officielle fidèle |
| 2 | 2022 T | spend | c spend | **à retirer** | « would » non enseigné (04 ni avant) ; même geste et même texte que Q1 |
| 3 | 2023 T | Advice | a | OK | options officielles + « Prohibition » ajouté |
| 4 | 2013 G | Obligation | d | OK (expl. à corriger) | l'explication liste may/might/could et should → fuite vers Q3, Q9, Q10 |
| 5 | 2017 T | build | a | OK | options officielles + « builds » |
| 6 | 2015 T | could | c | réserve | clé par élimination sur le sens (enseigné) ; vote « could / could to » |
| 7 | 2012 T | to | b | **à retirer** | « would like + to » enseigné au 07 seulement (L06, C1) ; leurres = réponses des autres blancs, éliminables à vue |
| 8 | 2005 | can | d | réserve | vote : « can » dans 3 options sur 4 |
| 9 | 2017 G | might | b | réserve | vote « might / might to » ; l'explication livre la clé de Q10 |
| 10 | 2009 G | could | a | OK | — |
| 11 | 2001 | could | b | **à retirer** | rejet de « can » et « will » par la concordance des temps, non enseignée ; doublon du geste de Q6 |

Fidélité aux transcriptions : toutes les phrases citées sont conformes (2022 T ex. 1 ; 2023 T Q4 ; 2013 G Q4 ;
2017 G ex. 1 ; 2017 T ex. 3 ; 2015 T ex. 1 ; 2012 T ex. 1 ; 2009 G ex. 1 ; 2005 ex. 3 ; 2001 ex. 1). Les options
ajoutées (« Prohibition » en Q3, « Advice » en Q4) sont fausses et ne changent pas la clé.

### Points tranchés

- **« would » (Q2) et « would like to » (Q7) — retirés.** Le cours 04 n'enseigne pas *would* (il n'apparaît qu'au 05
  « Going further », hors programme, et au 06 dans *Would you mind*). Q2 est en outre le même geste que Q1 (même
  texte 2022 T, modal + base, leurres -s/-ing/to) : les deux questions de 2022 T se ressemblent parce qu'elles
  testent la même chose ; on garde Q1 (« could », enseigné). *Would like + to + base* n'est enseigné qu'au 07 (cours
  C1 du lot L06) ; et les trois leurres de Q7 (have, certainly, is) sont les réponses des autres blancs de la
  banque 2012 T, agrammaticaux à vue (« would like certainly join ») : la clé sort sans savoir. **Suivi pilote :**
  l'item 2012 T ② peut rejoindre `m022` (07/06, « the gerund or to + base »), qui ne le pose pas encore.
- **« could » au passé (Q6, Q11).** Aucun cours ne pose *could* = passé de *can*. **Q6 reste** : elle se résout par
  le sens enseigné (must = obligation et sans passé, can't contredit « amazed », could = possibilité) ; il suffit
  que l'explication dise le passé en une phrase. **Q11 sort** : « can » et « will » n'y sont écartés que par la
  concordance des temps (*believed* → *could*, *will* → *would*), notion non enseignée, et « She believed she can
  change… » se défend en anglais courant ; c'est en outre le même geste que Q6.
- **Indice de forme Q9 (« should » contre « might »).** « should » est le leurre officiel, faux par le sens (un
  inconvénient, pas un conseil) : il reste. Le défaut est ailleurs : « might » figure dans deux options (might,
  might to) et le vote donne la clé. Même défaut en Q6 (could, could to), Q8 (can, cans, can to) et Q11 (retirée) :
  le patron « clé + to » est systémique dans la mission.
- **Ordre.** Les deux items de la session de base (2022 T) restent en tête ; le tri par difficulté ne déplace que
  2017 G et 2009 G vers la fin (d3). Conforme (« la mission garde l'ordre » de la base). Accepté.

### Défauts et correctifs

**[MAJEUR] Q2 — notion non enseignée + doublon de geste.** Retirer la question.

**[MAJEUR] Q7 — notion non enseignée au 04, leurres éliminables à vue.** Retirer la question (renvoi à `m022`).

**[MAJEUR] Q11 — clé qui repose sur la concordance des temps (non enseignée), « can » défendable.** Retirer.

Après retrait : 8 questions (6 d2, 2 d3), étage d2 inchangé, rampe 2→3 honnête.

**[MINEUR] Titre et fichier après retrait** (plus aucune question de 2001 ni de 2012 T ; sessions restantes
2005–2023) : « 🏛️ Exams 2005–2023 · modals in exam texts: meaning and form ⭐⭐ » et
`06-exams-2005-2023-modals-meaning-and-form.json` (fichier neuf) ; la ligne de registre de m011 ne liste plus 2012 T
ni 2001.

**[MAJEUR] Q6 — vote « could / could to » ; passé de could non dit.** Options et explication :

- options : `a` « must » (`english.modal.must-sans-passe-ni-futur`) · `b` « was able » (`english.modal.to-oublie`) ·
  `c` « could » (clé) · `d` « can't » (muet) ;
- explanation : « He tells a story in the past and speaks of the sites that were possible for him to visit. Could +
  base verb says what is possible, and it also works in a past story: the sites I could visit. "Must" has no past
  form and would mean an obligation, "can't" would say he was not able to visit them, which "amazed" contradicts,
  and "was able" loses the "to" that able always keeps. »

  Vérifié : « was able » n'exécute qu'une erreur (le sens « capacité passée » convient, le *to* manque) ; clé
  5 lettres, ni la plus longue (« was able », 8) ni la plus courte (« must », 4) ; « could » n'apparaît qu'une fois.

**[MAJEUR] Q8 — vote : « can » dans trois options.** Options et explication :

- options : `a` « is » (`english.verb.be-avec-base-verbale`) · `b` « may to » (`english.modal.to-en-trop`) ·
  `c` « had to » (`english.modal.fonction-confondue`) · `d` « can » (clé) ;
- explanation : « Can + base verb says what is possible for a giraffe: it can be up to 6 meters. "May to" adds a
  "to" that a modal never takes, and "is be" puts two verbs where one modal is needed. "Had to" would be a past
  obligation, which makes no sense for a fact about giraffes. »

  Vérifié : « may » a le sens juste (possibilité), seule l'erreur *to* reste ; « is » exécute exactement
  « be devant la base verbale » ; clé 3 lettres, pas la plus courte (« is », 2) ; aucune valeur répétée.

**[MAJEUR] Q9 — vote « might / might to » ; l'explication livre la clé de Q10.** Options et explication :

- options : `a` « should » (`english.modal.fonction-confondue`) · `b` « might » (clé) · `c` « are »
  (`english.verb.be-avec-base-verbale`) · `d` « have to » (`english.modal.must-pour-possibilite`) ;
- explanation : « The sentence lists a disadvantage: perhaps the photos do not match the real product. That is a
  possibility, so might + base verb. "Should" would give advice, "have to" would say the photos are obliged to be
  different, and "are be" puts two verbs where one modal is needed. »

  Vérifié : clé 5 lettres, ni la plus courte (« are », 3) ni la plus longue (« have to », 7) ; l'explication ne
  nomme plus « could » (clé de Q10) ; les trois leurres n'exécutent qu'une erreur chacun.

**[MAJEUR] Q4 — l'explication liste les modaux clés d'autres questions** (« may, might or could », « should » :
clés de Q9, Q10 et Q3, tirées au hasard dans le donjon). Explanation : « "Have to" + base verb is one of the two
ways of saying obligation, with must: stopping is necessary, the kids have no choice. A prohibition would forbid
the action, a possibility would only mean "perhaps", and advice would leave the kids free to choose. »

**[MAJEUR] Q1 — fuite vers `m022` (07/06 Q4).** L'énoncé cite « her passion for **working** with her hands », or
`m022` Q4 (même phrase 2022 T) demande justement « passion for ___ » → *working*. Énoncé de remplacement :
« (Exam 2022, technical) A text about a young welder says that she uses her hands "to fabricate works of art and
things people could ___ ." Which word completes the sentence? » (options et clé inchangées).

**[MINEUR] Q1 — explication imprécise** (« A modal takes no -s and no -ing ending » : c'est le verbe après le modal
qui n'en prend pas). Remplacer par : « After the modal "could" the verb stays in its base form: things people could
use. The verb after a modal takes no -s and no -ing ending, so "uses" and "making" are wrong. "Ability" is a noun,
not a verb, so it cannot follow a modal. »

**[MINEUR] Clé la plus courte** en Q1 et Q5 (base verbale nue face à ses formes fléchies) : inhérent au geste
« modal + base », non reconnaissable au vote ; acceptable une fois Q8 corrigée (2 clés sur 8).

Étiquettes de m011 : `base-verbale-deformee`, `to-en-trop`, `s-sur-le-modal`, `must-sans-passe-ni-futur`,
`must-pour-possibilite`, `fonction-confondue` — chacune exacte sur l'option qui la porte (vérifié option par
option ; « making » n'exécute que l'erreur -ing, *could make* étant juste).

---

## m012 — 04/07 « writing prepared: advise, warn, set rules » (d3 boss 120/30, 10 q.)

| Q | session | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- | --- |
| 1 | 2026 G | a (mustn't) | a | réserve | jeu d'options calqué sur 04/05 Q1 (mustn't / … / mustn't to / can) |
| 2 | 2026 T | d | d | OK | consigne citée fidèlement |
| 3 | 2016 T | c | c | réserve | consigne entre guillemets mais paraphrasée ; leurre d nie le sentiment (éliminable) |
| 4 | 2011 T | c | c | OK | lignes inventées, mot d'aide officiel « protective clothes » |
| 5 | 2026 G | b, d, f | b, d, f | **défaut** | la consigne citée (« at least 3 ») annonce le nombre de bonnes réponses ; citation altérée (« warn people ») |
| 6 | 2024 G | c, a, d, b | c, a, d, b | OK (citation) | ordre unique ; citation altérée (« for the association's Facebook page ») |
| 7 | 2022 T | b | b | OK | — |
| 8 | 2019 G | **ambigu** | l1-r4, l2-r2, l3-r1, l4-r3 | **ERREUR** | « Eat less fat… » convient aussi au poids, « Play sport… » au cœur : deux appariements défendables |
| 9 | 2016 T | b | b | réserve | doublon de geste de 04 quiz Q3 et 04/02 Q6 (should to / ought sans to) ; d porte deux erreurs étiquetées |
| 10 | 2011 T | a | a | OK (mineur) | geste de forme déjà publié, mais prévu par l'affectation et adossé à la consigne officielle |

Fidélité : consignes 2026 T, 2022 T, 2019 G, 2011 T citées mot pour mot ; 2016 T, 2024 G et 2026 G altérées entre
guillemets (correctifs ci-dessous).

### Points tranchés

- **Retrait de 2009 G (lettre au correspondant fumeur) — validé.** L'affectation elle-même interdit de reprendre
  le thème du tabac (09/02 Q1, Q5). Conséquence : plus aucune question ne cite 2009. **[MINEUR]** Titre et fichier :
  « 🏛️ Exams 2011–2026 · writing prepared: advise, warn, set rules ⭐⭐⭐ » et
  `07-exams-2011-2026-writing-advise-warn-set-rules.json` (fichier neuf, renommage libre avant livraison) ; la
  ligne de registre de m012 ne doit plus lister 2009 G.
- **Ordre.** La question de la session de base (2026 G, Q1) reste en tête ; le `multi` 2026 G (Q5) passe en d3 par
  le tri. Accepté.

### Défauts et correctifs

**[CRITIQUE] Q8 — appariement non unique.** Moins de gras protège le poids autant que le cœur, le sport aussi.
Remplacer les quatre éléments de droite (gauche inchangée, clé inchangée l1-r4, l2-r2, l3-r1, l4-r3) :
- r1 « Eat less fat to keep your blood vessels clear. »
- r2 « Drink water instead of sugary drinks and brush your teeth after meals. » (inchangé)
- r3 « Go to bed early and eat breakfast to have energy in the morning. »
- r4 « Play sport or walk every day to burn calories. »

Chaque but (vaisseaux sanguins → cœur, calories → poids, dents, énergie → fatigue) désigne un seul risque.
Explanation : « Each way names what it protects. Burning calories with sport or walking stops people gaining too much
weight. Water instead of sugary drinks and brushing protect the teeth. Clear blood vessels look after the heart, so
less fat goes with heart problems. An early bedtime and a good breakfast give energy and fight tiredness in class. »

**[MAJEUR] Q5 — nombre de bonnes réponses annoncé par la consigne (« at least 3 »)** ; les trois clés sont aussi
les trois options les plus longues. Passer à quatre bonnes réponses et rallonger les deux leurres :
- Task : « An increasing number of people rely on online shopping to make their lives easier. Write a 10-line
  article for a local magazine to warn them against the possible dangers of online shopping. State at least 3 sound
  arguments. » (citation exacte) ;
- a « You can compare prices from many shops without leaving your home. » (65 car.) · b inchangé (66) ·
  c « Many shops in the town centre are closed on Sundays and holidays. » (64) · d inchangé (54) ·
  e « Some websites sell fake products that break after a few days. » (61) · f inchangé (66) ;
- answerKey `["b", "d", "e", "f"]` ;
- explanation : « The article must warn, so a sound argument names a real danger of buying online: stolen card
  details, goods paid for but never sent, fake products and overspending. Comparing prices is an advantage, and the
  Sunday closing of shops is off the topic: neither warns anyone of a danger. »

**[MAJEUR] Q1 — option set calqué sur 04/05 Q1** (« ne pas redemander »). Options (clé `a` inchangée) :
`a` « You mustn't give your card number to a website you don't know. » (62) · `b` « Many people give their card
number to websites they don't know. » (63, muet : décrit le danger sans dire quoi faire) · `c` « You can give your
card number to any website you like. » (54, `english.modal.fonction-confondue`) · `d` « You might lose money on a
website you don't know. » (49, muet : dit un possible, ne met pas en garde). Explanation : « A warning tells readers
what not to do, and "mustn't" + base verb forbids the dangerous action. One sentence only describes what many people
do, another only says that something bad is possible, and "can" allows the very thing the article warns against. »

**[MAJEUR] Q9 — doublon de 04 quiz Q3 / 04/02 Q6, et option d à deux erreurs étiquetée** (« might » + « near »).
Nouvel énoncé : « (Exam 2016, technical) After a classmate cut his finger in the carpentry workshop, you give your
schoolmates some advice on how to keep safe. Which piece of advice fits the article? » Options (clé `a`) :
`a` « You should keep your fingers away from the blade. » (49) · `b` « You should buy a bigger saw for the whole
workshop. » (51, muet : conseil hors sujet) · `c` « You might keep your fingers away from the blade. » (48,
`english.modal.fonction-confondue`) · `d` « You mustn't tell the teacher about an accident. » (47, muet).
Explanation : « The task asks for advice on keeping safe, so should + base verb and a safety tip: keep your fingers
away from the blade. A bigger saw does not keep anyone safe, "might" only says that something is possible instead
of advising, and hiding an accident from the teacher is the opposite of safe. »

**[MINEUR] Q3 — citation paraphrasée entre guillemets ; leurre d éliminable à vue.** Task exacte : « While working
in a carpentry workshop at your technical school, one of your classmates had a small accident and cut his finger.
You have decided to write an article for your school magazine to show how sorry you are and to give your
schoolmates some advice on how to keep safe. » Option d : « I hope our classmate will come back to school soon. »
(51, souhait, pas regret). Explanation, dernière phrase : « …and the last one expresses a wish, not regret. »
Note : la clé reprend le mot « sorry » de la consigne ; la question reste un repérage de tâche (d2), acceptable.

**[MINEUR] Q6 — citation altérée.** Task exacte : « As a member of Go Green association, write a 10-line post to be
shared on the association's Facebook page. Suggest at least three ways to reduce pollution and protect the
environment. »

**[MINEUR] Q10 — geste de forme (Don't leaving, must to, mustn't leaves)** déjà présent au 04 (quiz Q1, 04/05 Q1) ;
gardé parce que prévu par l'affectation et adossé à la consigne 2011 T. **[MINEUR] Q1 ↔ Q5** : la clé de Q1 (carte
bancaire) illustre l'argument b de Q5 ; sans effet sur la clé de Q5 (b reste évident), signalé seulement.

Étiquettes m012 : `fonction-confondue`, `to-en-trop`, `to-oublie`, `base-verbale-deformee` — exactes, hormis Q9 d
(deux erreurs, corrigé ci-dessus).

---

## m013 — 08/06 « relative pronouns in exam texts: who, which, that » (d2 practice 75/15, 8 q.)

| Q | session | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- | --- |
| 1 | 2025 T | who | a | réserve | vote « who / who he » |
| 2 | 2024 G | which | d | réserve | relatif **complément** (« which **he** has learned ») : non enseigné, et contraire à la règle du cours « never followed by he, she, it » |
| 3 | 2021 T | which | b | OK (mineur) | « that they » sans étiquette |
| 4 | 2012 T | who | c | réserve | vote « who / who she » ; clé donnée par 01/06 Q6 et 07/07 Q2 (fuite entre lots) |
| 5 | 2011 G | who | a | OK | « those » = réponse officielle de ⓕ, faux ici |
| 6 | 2003 | who | d | réserve | vote « who / who they » |
| 7 | 2002 | that | b | OK | ① caché (« … »), il va à m015 |
| 8 | 2026 G | which | c | réserve | « which » repris sur une idée : non enseigné ; la méthode du cours (le nom à gauche) donne « who » ; vote « which / which it » |

Fidélité : les huit phrases sont celles des transcriptions (2026 G ex. 1, banque avec « who » intrus officiel ;
2025 T, 2024 G, 2012 T options officielles ; 2021 T, 2011 G, 2003, 2002 blancs uniques). Aucun item écarté
(« what », mots interrogatifs) n'est devenu question. Huit questions : conforme (le corpus n'en a pas plus).

### Points tranchés

- **Q8, « which » repris sur une idée.** Le cours 08 n'enseigne que le relatif qui définit le nom placé juste avant ;
  appliqué ici, il donne « who » (*children*), c'est-à-dire le leurre. La clé ne se justifie que par l'accord
  *teaches* (singulier) et par la reprise d'une idée, non enseignée. Garder l'item (c'est la session de base) avec
  une définition dans l'énoncé qui ne nomme pas le pronom, et le passer en d2 pour qu'il reprenne la tête (ordre
  de la base). Nouvel énoncé : « (Exam 2026, general) A text about "democratic learning" groups says: "The groups
  hold meetings where children, along with the teachers, discuss what will be taught. These are chaired by
  children, ___ teaches them to exchange ideas and listen to others' points of view." Tip: after a comma, a
  relative pronoun can stand for the whole idea before it, not only for the last noun. Which word completes the
  sentence? »
- **Q2, relatif complément.** Le choix *which* ne dépend que de « skills = choses » (enseigné), mais la phrase
  montre « which he », que le cours interdit et que trois leurres de la mission (« who he », « who they »,
  « which it ») font juger faux : l'élève est pris entre deux règles. Garder avec une définition dans l'énoncé :
  ajouter après la citation « Here "he" is the subject of "has learned"; the blank stands for the skills he
  learned. » et dans l'explication : « Here the pronoun is not the subject of the verb, "he" is, so "he" may follow
  it — unlike the sentences where who or which is the subject. »
- **Ordre.** Le tri par difficulté renvoyait la session de base (2026 G) en dernière place ; avec Q8 en d2, elle
  revient en tête (`displayOrder` des questions : 2026 G d'abord). Toute la mission est alors d2 : étage d2
  inchangé, titre ⭐⭐ juste.

### Défauts et correctifs

**[MAJEUR] Vote « clé + pronom sujet » (Q1, Q4, Q6, Q8).** Dans quatre questions sur cinq, le leurre « sujet en
double » est construit sur la clé (who he, who she, who they, which it) : la clé est l'option qui revient deux fois.
Remplacer :
- Q1 `d` « who he » → « that he » (`english.rel.sujet-en-double` : *that* convient à une personne, seule erreur le
  second sujet) ; explanation, fin : « …and "that he" adds a second subject after the pronoun. »
- Q4 `d` « who she » → « she » (muet : pronom personnel à la place du relatif ; *that she* aurait deux erreurs dans
  une relative entre virgules) ; explanation, fin : « "She" is an ordinary pronoun: it cannot link the two parts of
  the sentence. »
- Q6 `c` « who they » → « that they » (`english.rel.sujet-en-double`) ; explanation, fin : « "That they" repeats
  the subject, while the pronoun already is the subject of "don't agree". »
- Q8 `d` « which it » → « it » (muet) ; explanation : « The verb "teaches" is singular, so its subject cannot be
  "children": the pronoun stands for the whole idea before the comma — the fact that children chair the meetings.
  An idea is a thing, so the pronoun is "which". "Who" is for people, "what" is not a relative pronoun after a
  noun, and "it" is an ordinary pronoun that cannot link the two parts of the sentence. »

Vérifié : chaque clé n'apparaît plus qu'une fois ; aucune clé n'est la plus longue (who 3 / which 5 face à
« that he », « that they », « which »).

**[MAJEUR] Fuite entre lots vers Q4 (« My daughter, ___ is 15 »).** `01-present-tenses/exercices/06-…` Q6 écrit
« A mother describes how her daughter, **who** is 15, uses the Internet » et `07-…/07-exams-2007-2023-pronouns…` Q2
« A mother writes about her daughter, **who** chats… » : la phrase même de Q4 avec sa clé. À transmettre aux lots
L01 / L06 : 01/06 Q6 → « A mother describes how her 15-year-old daughter uses the Internet every day. » ; 07/07 Q2
→ « A mother writes about her teenage daughter and the Internet: ».

**[MINEUR] Q3 — « that they » sans étiquette** : ajouter `english.rel.sujet-en-double` (seule erreur : second
sujet, *that* convenant à une chose).

**[MINEUR] Clé la plus courte** en Q1, Q5, Q6 (« who », 3 lettres) : inhérent au couple who / which, non
reconnaissable puisque la clé alterne who / which / that dans la mission.

**[MINEUR] Q4 — relative non déterminative.** Le cours dit « that fits always » dans les groupes qui définissent ;
ici la relative est entre virgules, mais *that* n'est pas proposé : sans effet sur la clé.

Étiquettes m013 : `who-et-which-confondus`, `what-comme-relatif`, `sujet-en-double` — exactes sur chaque option qui
les porte (Q7 « who » pour des animaux : le cours range l'animal avec *which*, étiquette juste).

---

## m014 — 08/07 « comparative or superlative: read the clue » (d2 practice 75/15, 9 q.)

| Q | session | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- | --- |
| 1 | 2024 T | **most / more** | b most | **ERREUR (double réponse)** | « one of the more successful women » est de l'anglais standard (« parmi les femmes plutôt réussies ») |
| 2 | 2023 G | more | d | OK | options officielles + « many » |
| 3 | 2021 G | cheaper | a | OK | — |
| 4 | 2017 G | biggest | c | réserve | option officielle « big » retirée (l'affectation demande les options officielles) ; doublon de m015 Q1 |
| 5 | 2016 G | **most / many** | a most | **ERREUR (double réponse)** | « one of the many endangered animals » est grammatical et sensé ; doublon du geste de Q1 |
| 6 | 2011 G | fun | b | OK | — |
| 7 | 2002 | more | a | OK | « faster » leurre officiel de la banque |
| 8 | 2025 G | less | c | OK | clé par le sens (sooner → less), dit dans l'explication |
| 9 | 2008 | the most | d | réserve | le contexte ajouté (« for her children and for herself ») pose DEUX choses : « the more important thing » devient défendable |

Fidélité : phrases et options officielles conformes (sauf Q4, ci-dessous). Le texte 2008 est celui d'une mère qui
arrête de fumer : l'énoncé n'en dit rien (bien), à garder ainsi.

### Points tranchés

- **Trois doublons retirés (2022 T « more time than », 2019 G « one of the most », 2010 G « more than that ») —
  validé.** 2022 T et 2010 G refont le geste de Q2 (« more … than » de quantité) ; 2019 G refaisait celui de Q1 et
  porte en plus le même défaut (« one of the more significant values » est juste en anglais standard).
- **« one of the » + degré (Q1, Q5) — retirer les deux.** Avec les options officielles, chacune garde un leurre
  défendable (« more » en Q1, « many » en Q5) ; Q5 refait de plus le geste de Q1. C'est le cas R6 du plan (consigne
  officielle ambiguë → écartée) : à déclarer au registre comme les autres écarts R6. L'archétype « one of the » n'a
  pas d'item officiel sans double réponse dans le corpus.
- **Ordre.** La base (2025 G, Q8) est d3 et passe après les d2 : le tri par difficulté ne peut pas la placer en
  tête sans mentir sur l'étage. Accepté (l'ordre de la base est gardé à l'intérieur de son étage).

Après retrait : 7 questions (5 d2, 2 d3), étage d2, titre inchangé (2002–2025).

### Défauts et correctifs

**[CRITIQUE] Q1 et Q5 — double réponse.** Retirer (voir ci-dessus).

**[MAJEUR] Q1 — fuite vers L02 (relevée par la re-vérification de L02, confirmée).** L'énoncé « After graduating,
she **began** a new job in building and **became** one of the… » donne la clé de m008 Q4 (*began*) et le prétérit de
m008 Q5 (*became*). Correctif principal : le retrait de Q1 (double réponse, ci-dessus) l'efface. Si le pilote garde
Q1 malgré tout, le texte proposé au § 3 de `reverif-anglais-L02.md` (« she rose to the top of her trade ») est
**refusé** : « the top » annonce le superlatif et désigne la clé. Énoncé de remplacement vérifié (aucun verbe au
passé, aucun mot de degré) : « (Exam 2024, technical) A text about a woman builder describes her place in the
industry: "…one of the (much / more / most) successful women in the industry." Which word completes the
sentence? » — il laisse entier le défaut de double réponse (« more »).

**[MAJEUR] Q9 — contexte ajouté qui rend « the more » défendable.** Nouvel énoncé : « (Exam 2008) A mother has
given up a bad habit. She feels healthier and she saves money, then she adds: "But ___ important thing is that I
want to be around for my kids for as long as possible." Which words complete the sentence? » Trois bienfaits →
superlatif ; « the least » démenti par « But » ; options, clé et explication inchangées (l'explication dit déjà
« the top of all the reasons »). Ne pas écrire « feels better » : *better* est la clé de m015 Q10.

**[MAJEUR] Q4 — option officielle « big » retirée ; doublon de m015 Q1** (même clé « biggest », trois options
sur quatre communes). Options (clé `c`) : `a` « bigger » (`english.comp.comparatif-et-superlatif-confondus`) · `b`
« big » (muet) · `c` « biggest » · `d` « most big » (`english.comp.forme-selon-longueur`). Explanation : « The clue
is "the" in front of the blank and a group of values: the value at the top of all of them takes the superlative of
a short adjective, the + -est, with a double g: biggest. "Bigger" compares only two things, "big" compares nothing,
and "most big" uses "most" with a short adjective. » (L'orthographe « bigest » passe à m015 Q1, ci-dessous.)

Étiquettes m014 : exactes ; nouvelles familles F1 (Q6, Q8) et F2 (Q2, Q7, Q8) ci-dessous.

---

## m015 — 08/08 « building the comparison: -er, -est, more, as … as » (d3 boss 120/30, 12 q.)

| Q | session | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- | --- |
| 1 | 2021 G | biggest | d | réserve | doublon de m014 Q4 (même clé, options communes) |
| 2 | 2016 G | bigger | a | réserve | vote « bigger / more bigger » ; contexte ajouté fidèle (« his town ») |
| 3 | 2015 G | as | b | OK | — |
| 4 | 2011 G | longer | d | OK | « faster » leurre officiel |
| 5 | 2009 G | newest | b | réserve | vote « newest / most newest » |
| 6 | 2005 | tall | c | OK | ⓐ caché (« … »), il va à m011 |
| 7 | 2025 G | more fashionable | more fashionable | réserve | « Type the missing words » annonce deux mots ; variantes acceptées absentes ; explication sans la réponse |
| 8 | 2026 G | wisest | b | réserve | « their own wisest » sans *the* : le cours dit « the is never missing » |
| 9 | 2016 T | larger | c | OK | « smaller » plus haut, « colder » leurre officiel |
| 10 | 2015 G | better | a | réserve | *better* = « Going further, not tested » ; énoncé qui renvoie à Q3 (« At the same camp ») |
| 11 | 2006 | easiest | a | OK | y → i enseigné |
| 12 | 2002 | largest | d | réserve | vote « largest / most largest » |

Fidélité : toutes les phrases sont celles des transcriptions ; les contextes ajoutés (Q2 « his town », Q10 la
journée au camp, Q12 « where they live ») résument fidèlement le texte officiel.

### Points tranchés

- **Q10, « better » irrégulier.** Le cours le range en « Going further (beyond the 9th-grade book, not tested) ».
  Garder l'item officiel (better / worse est un choix de sens), mais donner les formes dans l'énoncé et remplacer
  « gooder » / « more good », éliminables à vue une fois les formes données, par un plan 2×2 sens × degré.
  Énoncé : « (Exam 2015, general) At a summer camp in Germany for children who spend too much time on the internet,
  the children swim, do aerobics and eat a healthy lunch, and many promise to limit the time they spend on their
  computers at home. "Children who attend the camp say they feel much ___ by the end of it." Tip: good → better →
  the best; bad → worse → the worst. Which word completes the sentence? » Options (clé `a`) : « better » (6 car.) · « worse »
  (muet) · « the best » (8, `english.comp.comparatif-et-superlatif-confondus`) · « worst » (muet, deux erreurs) —
  « best » nu aurait laissé la clé strictement la plus longue.
  Explanation : « The camp helps the children, so they feel better than before: better is the comparative of good.
  "The best" is a superlative: it would need a group, and "much" cannot come before it. "Worse" is the comparative of bad and says the opposite
  of what the camp achieves, and "worst" is both the opposite and a superlative. » Difficulté : d2 (le texte donne
  les formes). L'énoncé n'écrit plus « the same camp » (autonomie, défaut majeur ci-dessous).
- **Q2, « bigger » appuyé sur un contexte ajouté.** Le contexte (« for the inhabitants of his town ») est fidèle
  au texte et la clé ne dépend pas de lui : « a ___ city » exclut le superlatif, les autres options sont mal
  formées. Accepté ; seul le vote est à corriger (ci-dessous).
- **Q7, `short_answer` « more fashionable ».** Clé unique (« less fashionable » contredit « they meet-up online »).
  La normalisation du moteur (`normalizeRecallText` : casse, ponctuation, espaces) absorbe « More fashionable. » et
  « morefashionable ». Variante manquante : l'élève qui recopie l'adverbe donné, « far more fashionable ».
  Correctif : `acceptedAnswers: ["far more fashionable"]` ; ajouter à `expectedMistakes` « the most fashionable »
  (`english.comp.comparatif-et-superlatif-confondus`). Rien d'autre n'est juste (*much more* doublerait *far*).
- **Ordre.** La base (2025 G, Q7) est d3 : même jugement qu'en m014, accepté.

### Défauts et correctifs

**[MAJEUR] Q7 — l'énoncé annonce la forme** (« Type the missing **words** » : deux mots → *more* + adjectif).
Remplacer la fin de l'énoncé par : « Type the right form of the word in brackets. » Explanation (elle ne nomme pas
la réponse) : « "Fashionable" has four syllables, so it is a long adjective: it takes "more" before it, and "than"
follows because two ways of meeting are compared: far more fashionable. "Fashionabler" puts an -er ending on a long
adjective, "more fashionabler" marks the comparison twice, and "most fashionable" is a superlative, which cannot go
with "than". »

**[MAJEUR] Q10 — énoncé non autonome** (« At the same camp » renvoie à Q3, tirées au hasard dans le donjon) :
corrigé par le nouvel énoncé ci-dessus.

**[MAJEUR] Q8 — superlatif sans *the*, contraire au cours.** Ajouter après la citation : « Here "their own" takes
the place of "the". » (Clé, options inchangées.)

**[MAJEUR] Vote « clé + double marque » (Q2, Q5, Q12)** : le leurre « double marque » contient la clé (more
bigger, most newest, most largest). Plans 2×2 de remplacement :
- Q2 (clé « bigger ») : « bigger » · « biggest » (`comparatif-et-superlatif-confondus`) · « more big »
  (`forme-selon-longueur`) · « biger » (`english.spell.suffixe-sans-regle-orthographique`). Explanation, fin :
  « "Biggest" is a superlative and cannot follow "a", "more big" uses "more" with a short adjective, and "biger"
  forgets to double the g. »
- Q5 (clé « newest ») : « newer » (`comparatif-et-superlatif-confondus`) · « newest » · « most new »
  (`forme-selon-longueur`) · « more new » (muet, deux erreurs). Explanation, fin : « "Newer" compares only two
  things, "most new" uses "most" with a short adjective, and "more new" is a wrong comparative. »
- Q12 (clé « largest ») : « larger » (`comparatif-et-superlatif-confondus`) · « most large »
  (`forme-selon-longueur`) · « more large » (muet, deux erreurs) · « largest ». Explanation, fin : « "Larger"
  compares two things, "most large" uses "most" with a short adjective, and "more large" is a wrong comparative. »

Vérifié : chaque clé n'apparaît qu'une fois, aucune n'est la plus longue ; la marque double reste représentée par
« biggerest » (Q1) et l'attendu « more fashionabler » (Q7).

**[MAJEUR] Q1 — doublon de m014 Q4.** Faire de Q1 une question de forme (le degré est donné par « The … one » et
« a few problems ») : options (clé `a`) « biggest » · « bigest » (`english.spell.suffixe-sans-regle-orthographique`)
· « most big » (`forme-selon-longueur`) · « biggerest » (`double-marque`). Explanation : « The text speaks of a few
problems and picks the one at the top of the list, so the + superlative. "Big" ends with one vowel + one consonant,
so the g doubles: biggest. "Bigest" forgets the double consonant, "most big" uses "most" with a short adjective,
and "biggerest" marks the degree twice. » Après correctif, m014 Q4 et m015 Q1 ne partagent que « biggest » et
« most big », pour deux gestes distincts (degré / forme) ; m014 Q4 et m015 Q2 ne partagent que « bigger » et
« biggest ».

**[MINEUR] Q5 — « the newer model »** se dit en anglais courant de deux versions ; « of everything » oriente vers
le superlatif : gardé, risque faible.

---

## Les quatre familles d'étiquettes proposées

Registre lu : `origin/main:content/misconceptions.json` (famille `english.*`). Comptes faits APRÈS les correctifs
ci-dessus ; aucune ne porte sur un `multi` ni un `matching`.

**F1 — comparatif ou superlatif sans comparaison : ACCEPTÉE.** Trois questions distinctes, une erreur par option :
m014 Q6 (« funnier », « funniest », « most fun »), m014 Q8 (« least » : superlatif sans groupe), m015 Q6
(« taller », « tallest » ; « more tall » reste muet, deux erreurs). Ne double ni
`comp.comparatif-et-superlatif-confondus` (choix entre deux degrés) ni `comp.inegalite-pour-egalite` (égalité).
Id proposé : `english.comp.degre-sans-comparaison`.
- fr : « Tu mets un comparatif ou un superlatif alors que rien n'est comparé (ni than, ni the avec un groupe) :
  l'adjectif reste simple (It can be fun, 6 meters tall). »
- en : « You use a comparative or a superlative when nothing is compared (no than, no the with a group): the
  adjective stays plain (It can be fun, 6 meters tall). »
- ar : « تستعمل صيغة المقارنة أو التفضيل مع أنّه لا مقارنة في الجملة (لا than ولا the مع مجموعة): تبقى الصفة في
  صيغتها البسيطة (It can be fun, 6 meters tall). »

**F2 — much ou many à la place de more : ACCEPTÉE, libellé élargi à « less ».** Après retrait de m014 Q1 et Q5,
trois questions distinctes : m014 Q2 (« much », « many » au lieu de *more*), m014 Q7 (« much wonderful than »),
m014 Q8 (« much to do » là où la phrase compare : *sooner* → *less*). Une erreur par option. Ne double aucune
`english.*`. Id proposé : `english.comp.much-many-au-lieu-du-comparatif`.
- fr : « Tu mets much ou many là où la phrase compare (than, sooner…) : much et many disent une quantité, la
  comparaison se fait avec more ou less (more than we believe, more wonderful than). »
- en : « You use much or many where the sentence compares (than, sooner…): much and many tell an amount, and a
  comparison takes more or less (more than we believe, more wonderful than). »
- ar : « تستعمل much أو many حيث تقارن الجملة (than، sooner…): ‏much وmany تدلّان على الكمّية، والمقارنة تكون بـ
  more أو less ‏(more wonderful than). »

**F3 — relatif sans lien avec l'antécédent : REJETÉE.** Pour *who / which*, c'est exactement
`english.rel.who-et-which-confondus` ; pour *whose* et *where*, le cours les range en « Going further, not tested »
: un libellé qui les enseigne citerait une notion hors programme. Option de rechange, si le pilote veut étiqueter
« when » et « where » (m013 Q2, Q3, Q4, Q6 : 4 questions distinctes) : élargir le libellé existant
`english.rel.what-comme-relatif` (le cours, § propriété, nomme déjà *what* et *when*) :
- fr : « Tu mets what, when ou where après un nom comme pronom relatif : pour une personne ou une chose, on dit
  who, which ou that. »
- en : « You use what, when or where after a noun as a relative pronoun: for a person or a thing, use who, which or
  that. »
- ar : « تستعمل what أو when أو where بعد الاسم كاسم موصول: للشخص أو الشيء نستعمل who أو which أو that. »

**F4 — sujet après that : REJETÉE (doublon).** C'est l'erreur de `english.rel.sujet-en-double` (« Tu ajoutes un
sujet après who ou which »). Élargir ce libellé à *that* (nécessaire aussi pour les correctifs m013 Q1, Q3, Q6, qui
font porter l'erreur à « that he / that they ») :
- fr : « Tu ajoutes un sujet après who, which ou that (a lorry which it was…) : le pronom relatif est déjà le
  sujet. »
- en : « You add a subject after who, which or that (a lorry which it was…): the relative pronoun is already the
  subject. »
- ar : « تضيف فاعلًا بعد who أو which أو that ‏(a lorry which it was…): الاسم الموصول هو الفاعل أصلًا. »

---

## Bilan

| mission | q. auditées | clés fausses | critiques | majeurs | mineurs | à retirer | après correctifs |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| m011 (04/06) | 11 | 0 | 0 | 8 | 3 | 3 (Q2, Q7, Q11) | 8 q., d2 |
| m012 (04/07) | 10 | 0 | 1 (Q8) | 3 | 5 | 0 | 10 q., d3 |
| m013 (08/06) | 8 | 0 | 0 | 4 | 3 | 0 | 8 q., d2 |
| m014 (08/07) | 9 | 0 (2 doubles réponses) | 2 (Q1, Q5) | 3 | 0 | 2 (Q1, Q5) | 7 q., d2 |
| m015 (08/08) | 12 | 0 | 0 | 6 | 1 | 0 | 12 q., d3 |
| **total** | **50** | **0** | **3** | **24** | **12** | **5** | **45 q.** |

Fuites entre lots à transmettre : 01/06 Q6 et 07/07 Q2 (« her daughter, who… » → clé de m013 Q4) ; m011 Q1 →
m022 Q4 (« passion for working ») ; m014 Q1 → m008 Q4–Q5 (« began », « became », relevée par L02). Suivi pilote : l'item 2012 T ② (« would like to ») peut rejoindre m022.

Contrôle des fuites par script, dans les deux sens (phrase officielle + clé, contre toutes les missions et tous
les quiz de `content/english/`) : seules les deux fuites L03 → m008 et L03 → m022 ressortent ; la fuite vers m013 Q4
(« her daughter, who ») a été trouvée à la lecture.

**Verdict : à corriger avant livraison** (aucune clé fausse, mais un appariement ambigu, deux doubles réponses et
des votes systémiques). Tous les textes de remplacement ci-dessus ont été recomptés (longueur de la clé, unicité de
la valeur, aucune fuite vers une autre question de la tranche).
