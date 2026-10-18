# Carte du vocabulaire d'étiquettes — anglais 6ᵉ (lot A)

Écrit le 2026-10-18. Données : [`vocab-english-6eme.json`](./vocab-english-6eme.json). Rien n'est écrit dans `content/misconceptions.json` : chaque auteur (B1–B4) y ajoute les ids neufs et les libellés élargis **qu'il pose**, dans la PR de son lot ; un id déjà ajouté par un autre lot ne se réécrit pas.

**Bilan** : **19 ids neufs**, **6 libellés élargis** (même id, exemple de 6ᵉ ajouté), **24 ids réutilisés tels quels** (dont 4 `english.read.*` et 2 `english.write.*` pour les missions). Même espace `english.*`, `subject: "english"` (D5). Aucun id neuf ne double un existant : `pron.*` reste l'espace des pronoms et possessifs, la prononciation prend `sound.*`.

## 1. Ids neufs

| id | chapitres | piège du cours | mission d'examen | libellé (fr) |
| --- | --- | --- | --- | --- |
| `english.article.a-an-selon-la-lettre` | 07 | 07 « a amphitheatre », « an cape » | m019 (2013 an old garage) | Tu choisis a ou an d'après la lettre écrite et non d'après le son : an devant un son de voyelle (an amphitheatre, an old garage, an hour), a devant un son de consonne (a cape, a uniform). |
| `english.pron.possessif-du-mauvais-possesseur` | 01, 04 | 01 « Nadia and his kite » | m002 (2009, 2008 his / her) | Tu choisis l'adjectif possessif d'après la chose possédée ou au hasard : il suit le possesseur (Nadia → her kite, Amine → his kite, the cat → its name, Nadia and Amine → their kite). |
| `english.pron.sujet-au-lieu-du-possessif` | 01, 04 | 04 « This is she bag » | m002 (2016 Their / They) | Tu mets un pronom sujet (she, he, they) devant un nom à la place de l'adjectif possessif : she bag ✗ → her bag, They names ✗ → Their names. |
| `english.adv.frequence-mal-placee` | 01 | 01 (section adverbes de fréquence ; quiz#2) | m001 (2025 W1 a, ordering) | Tu places mal l'adverbe de fréquence (goes never) : always, usually, sometimes et never se mettent avant le verbe (she never goes) mais après am, is, are (he is always happy). |
| `english.quant.many-much-confondus` | 02, 06 | 02 (How many / How much) | m005 (2023 much, 2020 How many) | Tu confonds How many et How much : many devant ce qui se compte, au pluriel (How many eggs?), much devant ce qui ne se compte pas (How much milk?) ; How much? demande aussi un prix. |
| `english.health.etre-et-avoir-confondus` | 02 | 02 « I am a headache », « I have sick » | m005 (2023 stomachache) | Tu confonds be et have pour parler de la santé : on a une douleur avec have (I have a headache, she has a stomachache) et on est dans un état avec be (I am sick, he is tired). |
| `english.word.nom-au-lieu-de-l-adjectif` | 03 | 03 « a cloud day » | m007 (2026 warm, 2010 sunny, 2008 rainy) | Tu mets le nom à la place de l'adjectif (a cloud day, It's sun) : l'adjectif se forme avec Noun + y (cloudy, sunny, rainy) et suit It's ou se place devant le nom. |
| `english.word.nom-d-agent-force` | 04 | 04 « a carpent » | m009 (2025 cook / cooker, 2024 waiter) | Tu fabriques le nom du métier en collant -er partout ou sur un mot qui n'est pas un verbe (a carpent, a cooker pour la personne) : Verb + er ne marche qu'avec certains verbes (farm → farmer, build → builder, wait → waiter), les autres métiers s'apprennent tels quels (a doctor, a cook). |
| `english.verb.imperatif-mal-forme` | 04 | 04 « Not close », « You close » | — | Tu formes mal l'impératif : l'ordre commence par la base verbale, sans sujet (Close the door, pas You close the door), et l'interdiction par Don't + base verbale (Don't hit the cat, pas Not hit). |
| `english.sound.ed-toujours-syllabe` | 05 | 05 « talk-ed, play-ed » | — | Tu prononces le -ed final comme une syllabe dans tous les verbes : on n'entend /id/ qu'après t ou d (waited, decorated) ; ailleurs il se dit /t/ (talked, danced) ou /d/ (played, hugged). |
| `english.sound.lettre-pour-son` | 01, 02, 03, 04, 06, 07 | 04 (h muet) ; 06 « usually » | — | Tu prononces le mot d'après ses lettres et non d'après le son appris : un h peut être muet (hour, school), un s peut sonner /z/ (plays, museum), des lettres qui se ressemblent peuvent sonner autrement (usually, jeans). |
| `english.num.centaines-mal-ecrites` | 06 | 06 « four hundreds and sixty-eight » | — | Tu écris mal les centaines : hundred ne prend pas de -s après un nombre (four hundred, pas four hundreds) et and relie les centaines au reste (four hundred and sixty-eight). |
| `english.func.like-au-lieu-de-would-like` | 06 | 06 « I like a croissant, please » | m015 (2018, 2010, 2024 I'd like) | Tu dis I like (= j'aime en général) pour demander poliment ce que tu veux maintenant : au magasin, on dit I would like / I'd like a croissant, please. |
| `english.vocab.mot-de-sens-inverse` | 04, 05, 06 | 06 « The shopkeeper buys me… », « This blazer suits me, but it is too small » | — | Tu prends le mot de la paire au sens inverse : buy / sell, win / lose, fit (la taille) / suit (la couleur, le style), clean / dirty… Relis qui fait l'action et ce qu'on décrit. |
| `english.vocab.mot-voisin-du-meme-champ` | 01, 02, 03, 04, 05, 06, 07 | — | — | Tu choisis un mot du bon thème qui ne nomme pas la chose demandée (bakery pour butcher's, spring pour summer, socks pour gloves) : relis l'indice qui la distingue. |
| `english.prep.on-in-du-temps` | 01 | — | — | Tu te trompes de préposition de temps : on devant un jour (on Monday, on Monday morning, on the weekend), in devant une partie de la journée (in the morning, in the evening), un mois ou une saison (in July, in winter). |
| `english.prep.travel-by-to-confondus` | 07 | 07 « I travel by Italy » | — | Tu confonds by et to après travel : by devant le moyen de transport (travel by plane), to devant le lieu où l'on va (travel to Italy). |
| `english.vocab.directions-confondues` | 07 | 07 « Japan is on the right of the map » | m019 (2018 north), m021 | Tu confonds les directions de la carte : north est en haut, south en bas, east à droite, west à gauche ; right et left ne nomment pas une direction de la carte. |
| `english.comp.that-au-lieu-de-than` | 03, 07 | 03 « warmer that spring » | — | Tu fermes le comparatif avec that (warmer that spring) ou sans rien : après un comparatif, on compare avec than (warmer than spring). |

Les libellés en et ar sont dans le JSON (même sens, même exemples, deuxième personne comme l'existant).

## 2. Libellés élargis (même id)

| id | chapitres | pourquoi | nouveau libellé (fr) |
| --- | --- | --- | --- |
| `english.verb.ing-oublie` | 01, 03, 07 (enjoy to swim, How about go, I enjoy walk) | Ajout de like, love, hate, dislike, prefer, How about (structures de l'unité I, L1 et L3, et de l'unité VII, L3). Note : après like et prefer, to + base est aussi juste (fiche, U-VII L3) ; l'étiquette ne se pose que sur une base nue ou un to après enjoy, hate, dislike, How about, What about. | Tu mets to ou la base verbale après like, love, enjoy, hate, dislike, prefer, How about, What about, mind, regret ou une préposition (of, before) : le verbe prend -ing. |
| `english.verb.auxiliaire-mal-accorde` | 05 (she have the right to, we was) | Le libellé disait « auxiliaire » ; en 6ᵉ, has (the right to, a headache) et was/were sont des verbes pleins : on élargit sans changer d'id. | Tu n'accordes pas be, have ou l'auxiliaire avec le sujet : is, was, has, does avec he/she/it ; are, were, have, do avec you/we/they (she has the right to, we were happy). |
| `english.verb.temps-marque-deux-fois` | 05 (playeds) | Ajout du cas « -ed + -s » (piège du cours 05). | Tu marques le temps ou la personne deux fois : un verbe au passé ne prend pas aussi -s (played, pas playeds), et après do, does ou did (don't, doesn't, didn't) le verbe reste à la base verbale. |
| `english.question.auxiliaire-ou-ordre-oublie` | 06 (How much it is?) | Ajout de l'exemple de 6ᵉ (How much is it?) et de be. | Tu poses la question sans auxiliaire ou avec l'ordre de l'affirmation (How much it is?, When you visited…?) : mot interrogatif + be ou auxiliaire + sujet (+ verbe). |
| `english.spell.suffixe-sans-regle-orthographique` | 03, 05, 06 (suny, swiming, stoped, tryed) | Ajout de -y (Noun + y, U-III L1) et de -ed (U-V L3–L4) ; exemples de 6ᵉ. | Tu colles -y, -ing, -ed, -er ou -est sans la règle d'orthographe : consonne doublée (sunny, swimming, stopped, hotter), y → i (tried, happiest), e muet qui tombe (leaving, nicer). |
| `english.modal.to-oublie` | 06 (I would like buy) | Ajout de would like to (U-I L5, U-VI L2). | Tu oublies le to de would like to, ought to, have to, be able to ou intend to : ces formes le gardent toujours (I would like to buy). |

Un élargissement change le libellé que voient aussi les élèves de 9ᵉ : chacun garde le sens d'origine et n'ajoute que des exemples ou des déclencheurs de 6ᵉ.

## 3. Ids réutilisés tels quels

| id | où en 6ᵉ | piège du cours | mission |
| --- | --- | --- | --- |
| `english.verb.s-oublie-3e-personne` | 01, 05 (She play volleyball ; every child have…) | 01 (he/she/it + verb + s) | m001 (2013 goes, 2017 lives, 2010 likes) |
| `english.verb.base-verbale-deformee` | 02, 03, 04 (can swims, will goes, will cleans, Let's going) | 03 « will goes » ; 04 « will cleans » | m007 (2023 will have) |
| `english.verb.be-avec-base-verbale` | 03, 05 (It will sunny ; We are play) | — | — |
| `english.modal.to-en-trop` | 01, 02, 03, 04 (Let's to go, should to drink, will to go, can to run) | 01 « Let's to go » ; 02 « should to drink », « can to run » | — |
| `english.modal.s-sur-le-modal` | 02, 03 (shoulds, cans, wills) | 02 « shoulds », « cans » | — |
| `english.modal.fonction-confondue` | 02 (should/must/can selon conseil, règle, capacité) | 02 (conseil, règle, capacité) | m005 (2018 can't), m006 |
| `english.comp.forme-selon-longueur` | 03, 07 (more warm, more fast, more cold) — en 6ᵉ seuls les adjectifs courts sont enseignés : poser le tag sur « more + adjectif court » | 03 « more warm » ; 07 « more fast » | — |
| `english.comp.double-marque` | 03, 07 (more colder, the most biggest) | — | — |
| `english.comp.superlatif-sans-the` | 04, 07 (cleanest street, tallest of the three) | — | — |
| `english.comp.comparatif-et-superlatif-confondus` | 04, 07 (the cleaner street, tallest than) | 04 « the cleaner street » ; 07 « tallest than » | m009 (2024 cleanest / cleaner) |
| `english.tense.ed-sur-verbe-irregulier` | 05, 06 (buyed, maked, choosed, selled) | 05 « buyed », « maked » ; 06 « buyed » | m012 (found, drank, took, wrote, chose) |
| `english.tense.present-avec-marqueur-passe` | 05, 06 (Yesterday she play, Last Saturday I buy) | 05 (yesterday / last / ago) | m012 (2024 sang ; 2026 chose) |
| `english.tense.continu-pour-habitude` | 07 (In Spain people are eating paella every year) ; 01 (I am going fishing every Sunday) | 07 « In Spain, people are eating paella » | — |
| `english.tense.verbe-d-etat-au-continu` | 06 (I am liking this sweater) | — | — |
| `english.link.connecteur-de-mauvais-type` | 01 (and / but / because) | — | m002 (2021, 2019, 2012, 2020) |
| `english.func.fonction-mal-identifiee` | 01, 07 (suggestion ou invitation ; Let's / Would you like) | — | m003 |
| `english.func.demande-et-offre-confondues` | 06 (Can I help you? / Can you help me?) | — | m015 (Can I help you?) |
| `english.question.mot-interrogatif-inadapte` | 01, 03, 06 (How is the weather like? → What's ; How many is it?) | — | — |
| `english.read.detail-pris-pour-idee-principale` | missions de reading (m004, m010, m013, m016, m018, m020) | — | — |
| `english.read.referent-le-plus-proche` | missions de reading (référent « they », 2026) | — | m010 (they) |
| `english.read.reponse-sans-appui-dans-le-texte` | missions de reading (vrai/faux justifié) | — | m004, m010, m013, m016, m018, m020 |
| `english.read.sens-du-mot-sans-contexte` | missions de reading (synonyme « very happy », 2026) | — | m010 (thrilled) |
| `english.write.phrase-hors-sujet` | missions de writing préparé (m006, m008, m011, m014, m017, m021) | — | m006, m008, m011, m014, m017, m021 |
| `english.write.ordre-sans-mots-de-liaison` | missions de writing préparé (ordre du plan) | — | — |

## 4. `coursePitfalls` proposés par chapitre

Chaque tag doit être porté par au moins un distracteur du chapitre (C-5) et correspondre à un `::: piege` du cours ; un piège du cours sans tag (07 « une salutation n'est pas plus polie qu'une autre ») reste sans étiquette.

| chapitre | coursePitfalls |
| --- | --- |
| `01-entertaining-myself` | `english.verb.ing-oublie`, `english.modal.to-en-trop`, `english.pron.possessif-du-mauvais-possesseur`, `english.adv.frequence-mal-placee`, `english.verb.s-oublie-3e-personne` |
| `02-keeping-fit` | `english.modal.to-en-trop`, `english.modal.s-sur-le-modal`, `english.health.etre-et-avoir-confondus`, `english.quant.many-much-confondus`, `english.modal.fonction-confondue` |
| `03-having-fun-in-the-seasons` | `english.word.nom-au-lieu-de-l-adjectif`, `english.verb.base-verbale-deformee`, `english.comp.forme-selon-longueur`, `english.comp.that-au-lieu-de-than`, `english.spell.suffixe-sans-regle-orthographique` |
| `04-caring` | `english.pron.sujet-au-lieu-du-possessif`, `english.comp.comparatif-et-superlatif-confondus`, `english.word.nom-d-agent-force`, `english.verb.base-verbale-deformee`, `english.verb.imperatif-mal-forme`, `english.sound.lettre-pour-son` |
| `05-celebrations` | `english.verb.auxiliaire-mal-accorde`, `english.verb.temps-marque-deux-fois`, `english.tense.ed-sur-verbe-irregulier`, `english.tense.present-avec-marqueur-passe`, `english.sound.ed-toujours-syllabe` |
| `06-going-shopping` | `english.vocab.mot-de-sens-inverse`, `english.func.like-au-lieu-de-would-like`, `english.question.auxiliaire-ou-ordre-oublie`, `english.num.centaines-mal-ecrites`, `english.tense.ed-sur-verbe-irregulier`, `english.sound.lettre-pour-son` |
| `07-around-the-world` | `english.vocab.directions-confondues`, `english.verb.ing-oublie`, `english.article.a-an-selon-la-lettre`, `english.prep.travel-by-to-confondus`, `english.comp.forme-selon-longueur`, `english.comp.comparatif-et-superlatif-confondus`, `english.tense.continu-pour-habitude` |

## 5. Ids de la 9ᵉ volontairement non repris

`english.tense.*` du present perfect et du passé continu, `english.cond.*`, `english.rel.*`, `english.future.*` (going to, plan au présent continu), `english.modal.must-pour-possibilite`, `english.modal.must-sans-passe-ni-futur`, `english.comp.*` d'égalité (as … as), `english.func.hope-*`, `kind-*`, `mind-*`, `english.vocab.interesting-interested-confondus` : notions hors du guide de 6ᵉ (fiche, « EXCLU »).
