# anglais — 3ème année secondaire · programme officiel CNP (transcription, profondeur de génération)

> **Sources** (combinées — voir `programme/README.md`) :
>
> - **Guide enseignant** (programme) : `641303P00.pdf`
>   (`cnp-officiel/manuels/secondaire/c3/enseignant/`) — « **Activate And Perform — Third Year
>   Secondary Education — Teacher's Book** », National Pedagogic Centre, 88 pages.
>   **Pages lues** : p.1–88 (intégral).
> - **Manuel élève** (contenu/exemples/exercices) : `241303P00.pdf`
>   (`cnp-officiel/manuels/secondaire/c3/eleve/`) — « **Activate And Perform — Third Year
>   Secondary Education — Student's Book** », National Pedagogic Centre, 216 pages.
>   **Pages lues** : p.1–216 (intégral).
>
> **Transcrit le** : 2026-08-04. **Statut** : transcription fidèle (sources combinées, les deux
> lues intégralement). **Langue d'enseignement** : `en`. **gradeSlug** : aucun à la racine — ce
> manuel est **mutualisé sur les six sections** de 3ème année (voir « Portée » ci-dessous).
> **subject id source (virtuel)** : `english-3eme-sec` → six sujets compilés.
>
> **Extraction** : couche-texte propre sur les **deux** PDF (`pdftotext -layout`, 0 mojibake,
> **0 OCR, 0 passe vision**) — cas rare dans le corpus CNP, et la raison pour laquelle ce LOT A
> couvre 304 pages sans coût de vision.

## Portée — un dossier, six sections (mutualisation `compileTo`)

En 3ème année, **toutes les matières se dédoublent par section sauf l'anglais** : le catalogue CNP
ne porte **qu'un seul manuel élève (`241303`) et qu'un seul guide enseignant (`641303`)** pour les
six sections, et **aucun titre de manuel ne nomme de شعبة**. La transcription confirme ce que le
catalogue laissait supposer (`docs/lycee-architecture.md` §3.1, D-4.b : « c'est la transcription qui
décide, pas le titre ») : le **tronc commun** (Review Module, Sections One→Five de chaque module,
Consolidation Modules, appendice) est **identique pour les six sections**.

⚠️ **Nuance capitale, constatée à la transcription** : chaque module de langue porte **en plus** des
sections « **Arts** » que le manuel déclare explicitement réservées à la filière Lettres — Book map,
manuel p.6 : « **The items in pink are specific to the Arts branch.** » ; guide p.4 : « Each [module]
consists of **five sections for the common core and additional material for the Arts branch** ».
Le guide le redit au cas par cas (p.54 : « This section is specific to the Arts students. However,
have the other students of the other branches deal with Activity 1 and Activity 2… »).

Conséquence pour le pipeline :

- le **tronc commun** alimente les **six** sujets compilés (`compileTo`, étude 16 D-4) ;
- le **supplément Arts** est **propre à `3eme-sec-lettres`** — il est transcrit ici (il fait partie
  de la source) mais il **ne se génère pas dans le tronc commun** ; le moteur sait le porter par
  `gradeSlugs` au niveau du chapitre ou de l'exercice (loader.ts, `expandSubjects`). Il n'est **pas**
  codifié au chapitrage §4 de cette première passe : ce serait déclarer générable ce qui ne l'est pas
  encore, et R-8 s'atteint sans lui.

Six sujets compilés, tous sur le **même chapitrage** :

| section CNP                    | `gradeSlug`             | subject id compilé              |
| ------------------------------ | ----------------------- | ------------------------------- |
| Mathématiques                  | `3eme-sec-math`         | `english-3eme-sec-math`         |
| Sciences expérimentales        | `3eme-sec-sciences-exp` | `english-3eme-sec-sciences-exp` |
| Lettres                        | `3eme-sec-lettres`      | `english-3eme-sec-lettres`      |
| Économie & gestion             | `3eme-sec-eco-gestion`  | `english-3eme-sec-eco-gestion`  |
| Techniques                     | `3eme-sec-techniques`   | `english-3eme-sec-techniques`   |
| Sciences de l'informatique     | `3eme-sec-info`         | `english-3eme-sec-info`         |

**R-4 (une source, une fiche)** : cette fiche — rangée sous `3eme-sec-math`, la première section
dans l'ordre canonique de `docs/lycee-architecture.md` §2 — est la **seule** à revendiquer les codes
`241303` et `641303`. Les cinq autres sections **y renvoient** par la note de leur manifeste ; elles
ne revendiquent pas la source. C'est exactement le montage déjà éprouvé sur
`math-2eme-sec-sciences-info` (`programme/2eme-sec-sciences/mathematiques.md`).

**Identité des ouvrages.** Titre commun : _Activate And Perform — Third Year Secondary Education_
(« REPUBLIC OF TUNISIA / Ministry of Education »). **Auteurs** (tels qu'écrits, page de titre des
deux ouvrages) : **Abdennour KHEMIRI** (Inspector), **Mohamed Lamjed LABIDI** (Inspector — abrégé
« Med Lamjed LABIDI » sur le guide), **Aysha MEZZI** (Inspector), **Hamida MENCHARI** (Teacher
Trainer). **Évaluateurs** : **Jawida BEN AFIA** (Inspector General), **Mohamed Fethi EL BEJI**
(Senior Inspector). Éditeur : **National Pedagogic Centre** — « © All rights reserved for National
Pedagogic Centre » (manuel p.2). Achevé d'imprimer : « Impression Centre National Pédagogique
**2006** » (guide p.88). Aucune année n'est imprimée sur le manuel élève.

**Le matériel déclaré et ce qui manque.** Guide p.4 : « The materials consist of a **student's book,
a teacher's guide and a cassette** ». La **cassette n'est pas au corpus** — mais, contrairement au
manuel de 1ère année, **le guide publie l'intégralité des tapescripts** (p.76–86). Les sections
« Listening » sont donc **entièrement générables depuis le texte**, sans audio : c'est l'apport
décisif de la combinaison guide + manuel sur ce couple.

---

## 1. Cadre & compétences

### 1.1 Architecture de l'ouvrage (manuel, Preface p.3 · guide, Introduction p.4–5)

Le manuel se déclare **divisé en 9 modules** : « one **review module**, **six learning modules** and
**two consolidation modules** ». S'y ajoutent, hors modules : la préface, le **Book map** (p.4–6),
les listes de vocabulaire par module, un **Grammar summary**, une **liste de verbes irréguliers** et
une **table de symboles phonétiques** (appendice p.207–216).

**Le module est l'unité structurante déclarée** — c'est elle qui porte le chapitrage §4. Guide p.4 :
« Each module in the book covers a **different theme and thus may stand alone**. However, it is
recommended that the modules be covered in the **order presented**. »

**Anatomie d'un module de langue** (constante sur les six) :

1. **Section One : Introductory activities** — activation des acquis, entrée dans le thème ;
2. **Section Two : Listening** ;
3. **Section Three : Reading** ;
4. **Section Four : Speaking** ;
5. **Section Five : Writing** ;
6. — puis le **supplément Arts** (une à trois sections, filière Lettres) ;
7. — puis les rubriques de clôture du manuel : **SELF-ASSESSMENT**, **Fun page**,
   **VOCABULARY COVERED IN MODULE N** (liste lexicale officielle, séparée en `Common core:` et
   `Arts:`).

**Anatomie d'une section** (guide p.4) : trois étapes explicites —
**« Before you Listen / Read / Write »** (activer les acquis, préparer),
**« As you Listen / Read / Write »** (les activités de compréhension et de découverte),
**« After you Listen / Read / Write »** (réinvestir : réagir au texte, donner son opinion, interagir,
résumer, écrire une lettre ou un article, ou faire un exercice de langue).
Le guide précise : « A section is **by no means meant to be covered in one session** ».

### 1.2 Principes pédagogiques déclarés (guide p.4–5)

Transcrits fidèlement :

- **Les quatre macro-compétences sont d'égale importance** : « four sections focusing respectively on
  Listening, Reading, Speaking and Writing – **considered of equal importance** ». Chaque section
  traite une macro-compétence à fond, mais « **the integration of skills is one of the major guiding
  principles in this textbook** ».
- **Les « Expected Outcomes » s'annoncent** : « At the beginning of each module, it is advisable to
  let the students know what the Expected Outcomes are. »
- **Le lexique se présente en contexte** : « The lexical items are presented **in context**. When to
  present the lexical items, how to present them and what to teach and recycle depends on the
  students' level, needs and the teaching situations. »
- **La grammaire s'enseigne inductivement** : « Grammar is presented and recycled **inductively**.
  The students are encouraged to **discover and deduce the form, the use and the meaning** of the
  structures/words in a text or in an activity and **work out the rules for themselves**. » Le guide
  détaille la démarche attendue (p.14) : « recognize language items in context · recognize form ·
  infer the function/communicative value of the item · practise language items in a variety of
  contexts · apply the items in a variety of situations using the thematic context ».
- **Les passages écoutés et lus sont polyvalents** : ils « not only develop skills and strategies but
  are also used to **present grammar items, introduce new vocabulary and expressions**, stimulate
  oral and written work, give information on the topic, expand the students' knowledge of the world
  and **nurture in them positive values and a sense of their identity** ».
- **Maximiser le temps de parole de l'élève** : pair work, group work, débats de classe, discussions.
- **L'écrit est mis en avant** : les activités d'écriture développent des sous-compétences et
  recyclent la langue vue ; l'élève applique le **processus d'écriture** (writing process) et les
  critères d'évaluation annoncés — le guide invite (p.17) à faire élargir la liste par les élèves
  au-delà des trois critères imprimés (**coverage of ideas, coherence, language accuracy**) vers
  presentation, use of linkers, use of appropriate vocabulary, fluency.
- **Mini-projets** : ils développent « research and fieldwork strategies as well as language and
  social skills », élargissent les connaissances et **nourrissent l'autonomie**.
- **Le recyclage est systématique**, par les compétences, les sous-compétences et les activités.
- **Auto-évaluation en fin de module** : « the students fill in a **self-evaluation form** to help
  them check their progress and set their own goals », au service de la finalité générale du
  programme — « to give students the **self-confidence, the autonomy and the responsibility** they
  need to become aware of their learning strategies, monitor their progress and **continue learning
  by themselves, beyond the programme** ».

### 1.3 Le Review Module — statut particulier (guide p.4)

« The Review Module at the beginning of the book is meant to **recycle and consolidate several skill
areas the students are supposed to have covered at the second year level**. It can be used to
**check the learner's acquisitions and act accordingly** before embarking on the new syllabus. »
C'est donc un module de **reprise du programme de 2ème année**, pas de contenu neuf.

### 1.4 Objectifs transversaux (Cross-curricular learning goals)

Identiques et répétés à l'ouverture des **six** modules de langue (guide p.9, 21, 36, 45, 58, 67) :
_problem solving, critical thinking, efficient use of data, efficient working procedure, appropriate
self-expression, ICT use, project work, communicating, working and living with others._

---

## 2. Plan annuel — module par module

### Review Module (manuel p.7–11 · guide p.7–8)

**Statut déclaré** (guide p.4) : module de **reprise du niveau 2ème année secondaire**, à faire avant
d'entamer le nouveau programme — « recycle and consolidate several skill areas the students are
supposed to have covered at the second year level ». Le guide ne lui donne **ni « Scope and
sequence », ni « Helpful notes »** : seulement le corrigé. C'est la seule partie du livre dans ce cas.

**Onze activités**, sans découpage en sections. Notions révisées, telles qu'elles ressortent des
activités : discours rapporté, `let / make + base form`, `used to`, comparatif et superlatif, present
perfect vs simple past, voix passive, linkers, cohérence et ordre du texte, mise en page d'une lettre
d'affaires, formation des mots.

#### Activity 1 (manuel p.7) — compréhension d'un fait divers + discours rapporté

**A.** « Read the text and answer the questions below then compare your answers with your
classmate's. » Texte-support : entrefilet de presse titré « **Local Couple Killed in a Plane Crash** »,
daté « Chicago August 15, 2004 ». Contenu : un couple de Hillsboro, **Victor et Caroline Crowley**,
tué la veille en fin d'après-midi dans le crash de leur avion privé à l'atterrissage à l'aéroport
métropolitain de Chicago, pendant un violent orage ; la cause n'est pas encore établie ; M. Crowley,
qui avait « at least ten years of experience flying », pilotait ; les autorités locales pensent qu'il
a perdu le contrôle à cause du mauvais temps ; mais **Robert Crowley**, frère de la victime, déclare :
« My brother was an excellent pilot. He landed safely in much worse weather than this. I believe it
was a mechanical problem. » ; le couple était seul à bord ; leurs deux jeunes enfants, **Meredith, 4
ans**, et **Andrew, 2 ans**, sont confiés à des proches ; l'enquête se poursuit, rapport final espéré
en fin de semaine.

Questions : **1)** deviner d'où le texte est tiré, en justifiant ; **2)** compléter un tableau à
quatre colonnes — _What happened / When? / Where? / To whom?_ ; **3)** quelles sont les causes
possibles mentionnées ? ; **4)** le rédacteur est-il _sympathetic, neutral or critical_ ? justifier.

**B.** Réécriture au discours indirect : reprendre la déclaration de Robert Crowley en commençant par
« Robert Crowley said that ------ », puis **comparer la phrase d'origine à la nouvelle et relever les
différences** (démarche inductive : la règle n'est pas donnée, elle se déduit).

_Corrigé du guide_ : aucun pour cette activité (le guide commence son corrigé à l'Activity 2).

#### Activity 2 (manuel p.7–8) — QCM de langue en contexte + compréhension

**A.** « Circle the correct alternative. » Texte à trous à choix multiples, témoignage à la première
personne d'un adolescent des années soixante : parents stricts, père gagnant « only £8 a week in his
office job », mère jonglant avec les finances, femmes « second-class citizens », filles non
encouragées à étudier ou à faire carrière après le mariage, décisions du foyer prises par la mère,
partage des décisions aujourd'hui.

Les neuf choix imprimés, dans l'ordre : _(to stay out / **stay out** / staying out)_ · _(**every** /
no / some)_ · _(makes / making / **make**)_ · _(at / **in** / on)_ · _(after / **for** / with)_ ·
_(**were not encouraged** / didn't encourage / aren't encouraged)_ · _(**to make** / made / making)_ ·
_(**these** / those / that)_ · _(**easier** / easiest / easy)_.

**B.** **1.** Vrai/faux à justifier par le texte : a) « The teenager comes from a rich family. » ;
b) « In the sixties men and women had different roles. » **2.** Question ouverte : « Do your parents
share decisions at home ? »

_Corrigé du guide (p.7)_ : « stay out – every – make – at – for – were not encouraged – to make –
these - easier ».

#### Activity 3 (manuel p.8) — formation des mots

**A.** « Put the bracketed words in the correct form. » Texte d'opinion sur les « Superdads » et le
partage des tâches ménagères, avec neuf mots entre parenthèses à dériver : _(equality)_, _(more)_,
_(delight)_, _(weigh)_, _(person)_, _(good)_, _(complain)_, _(load)_, _(wash)_.

**B.** **1.** « Does "I" in the text refer to a man or to a woman ? » **2.** « Is the writer for or
against sharing family roles ? »

_Corrigé du guide (p.7)_ : « equal - most - delighted – weight – personal - best - complaint – loads
– washing ».

#### Activity 4 (manuel p.8–9) — temps et modaux en contexte

**A.** « Fill in each blank with one of the alternatives provided in the margin. » Texte informatif
sur l'hydratation : bonne nouvelle pour les amateurs de café et de cola, nouvelles recommandations de
la **U.S. National Academy of Sciences (NAS)** — toutes les boissons, y compris celles qui contiennent
de la caféine, comptent dans l'hydratation ; il faut plus de liquide qu'on ne le croyait ; boire assez
est crucial ; en cas d'effort ou de chaleur, un supplément est indispensable.

Les six jeux d'alternatives imprimés en marge : **1)** _are used to thinking / **used to think** /
use to think_ · **2)** _**would** / will / must_ · **3)** _lack / produce / **contain**_ · **4)**
_**believed** / decided / planned_ · **5)** _**is** / was / had been_ · **6)** _will work /
**are working** / were working_.

**B.** **1.** « What does the underlined word refer to ? » — sur « **Not so**, say the scientific
guidelines…… ». **2.** « Express the following sentence differently using your own words : ----extra
liquid is a must. »

**C.** Compléter un **spidergram** centré sur le verbe « to drink » avec des mots du texte.

_Corrigé du guide (p.7)_ : « 1- used to think - 2. would – 3. contain - 4. believed - 5. is –
6. are working ».

#### Activity 5 (manuel p.9) — lexique en contexte + cause/effet

**A.** « Fill in the blanks with **7 words from the box below**. » Banque de **9** mots (deux sont
donc des intrus) : _Job / throughout / successful / breathing / expensive / employees / economical /
grades / recently_. Texte : les travailleurs exposés aux poussières chimiques (mines, plasturgie)
risquent une perte de capacité respiratoire, d'où l'obligation faite aux entreprises de tester leurs
poumons ; traditionnellement les entreprises américaines faisaient venir une unité mobile ou
envoyaient les salariés chez des spécialistes, méthodes coûteuses ; plus récemment, des appareils
portables de test de la fonction pulmonaire se répandent, économiques et jugés fiables.

**B.** Compléter un tableau à trois colonnes — _Cause / Effect / Preventive measures_ — la première
ligne étant amorcée par « Exposure to chemical dusts ».

**C.** « Rephrase the following expression : "lung-function testing machines" » (déballage d'un
groupe nominal complexe — préparation aux adjectifs composés du module 4).

_Corrigé du guide (p.7)_ : « 1. breathing – 2. throughout - 3. employees - 4. job – 5. expensive –
6. recently - 7. economical ».

#### Activity 6 (manuel p.9) — remise en ordre de mots

« Reorder the words/phrases to get correct sentences » — trois items :
a) _about / careful / my / sister / enough / her health / is not /_ ;
b) _she eats / the more / she gets / the fatter /_ ;
c) _healthy food / she doesn't / either / eat / practise sports / She doesn't / and_.

_Corrigé du guide (p.7)_, verbatim :
« - My sister is not careful enough about her health. » ·
« - The more she eats, the fatter she gets. » ·
« - She doesn't eat healthy food, and she doesn't practise sports, either. »
(Trois structures visées : `adjective + enough`, le double comparatif `the more… the -er…`, et
`either` en fin de phrase négative.)

#### Activity 7 (manuel p.10) — chasse à l'erreur

« Correct the underlined mistakes. » Texte sur la conquête spatiale et l'informatique (premier
satellite américain, premier pas sur la Lune en 1969, stations spatiales, l'ordinateur au cœur de
l'âge de la technologie, espoir de résoudre la faim et la pauvreté). Six erreurs soulignées, à
corriger dans un tableau _Mistakes / Correction_.

_Corrigé du guide (p.7)_, tel qu'imprimé :

| Mistakes         | Correction                    |
| ---------------- | ----------------------------- |
| on               | in                            |
| is using         | has been using / has used     |
| stations space   | space stations                |
| more important   | As important as               |
| Can be using     | Can be used                   |
| hanger           | hunger                        |

#### Activity 8 (manuel p.10) — linkers

« Circle the most appropriate linker. » Texte sur l'égalité salariale et professionnelle des femmes
américaines. Cinq jeux : **1)** _while / therefore / **because**_ · **2)** _**However** / Besides /
In fact_ · **3)** _never / **ever** / usually_ · **4)** _so / moreover / **because**_ · **5)**
_**and** / but / yet_.

_Corrigé du guide (p.7)_ : « 1. because / 2. However / 3. ever / 4. because / 5. and ».

#### Activity 9 (manuel p.10) — réinsertion de segments

« Four sentence parts have been deleted from the following passage. Reinsert them where
appropriate. » Passage narratif : départ en voiture pour une journée d'achats de Noël de dernière
minute avec la grand-mère ; chants de Noël, bavardages et rires en chemin ; Noël dans deux jours,
esprit de fête ; « I felt light-headed (c) . I love shopping (d). »
Les quatre segments à replacer : **1)** _and full of joy_ · **2)** _along with my older brother and
sister_ · **3)** _especially at Christmas_ · **4)** _On the way to the shopping centre_.

_Corrigé du guide (p.7)_ : « a - 2 / b - 4 / c - 1 / d – 3 ».

#### Activity 10 (manuel p.11) — remise en ordre d'un paragraphe

« Reorder the following sentences to get a coherent paragraph. » Sept énoncés sur Christophe Colomb :
a) _The Indians were native Americans._ · b) _But he didn't get to China._ · c) _By accident, this
sailor from Spain discovered a new world._ · d) _In 1492, Christopher Columbus was trying to find a
way from Europe to the Far East_ · e) _He thought he was near the Indies,_ · f) _Instead, he found
some islands in the Atlantic Ocean near North America._ · g) _so he called the people Indians._

_Corrigé du guide (p.8)_, donné sous forme de table lettre → rang :

| a   | b   | c   | d   | e   | f   | g   |
| --- | --- | --- | --- | --- | --- | --- |
| 6   | 2   | 7   | 1   | 4   | 3   | 5   |

soit l'ordre de lecture **d → b → f → e → g → a → c**.

#### Activity 11 (manuel p.11) — mise en page d'une lettre d'affaires

« Layout the following business letter. » Douze fragments étiquetés a) à l) — étiquetage de la source
tel quel, avec un **`I)` majuscule et un `J)` majuscule** là où on attendrait `i)` et `j)` [sic] :

- a) _-by making your payments smaller or extending our terms-_
- b) _We are interested in our customers and are always trying to find new ways to improve our service._
- c) _Dear Mr Godfather,_
- d) _We would appreciate a word from you_
- e) _Hi-Fi Corporation / North Street / Norwich, UK._
- f) _please let us know._
- g) _For these reasons, we are inquiring if there is a reason for your delay in paying your long overdue account._
- h) _Sincerely, / Paul Goldsboro / Executive director._
- I) _-as well as your check_
- J) _If we can help_
- k) _September 22, 200-_
- l) _24 High Street. / London. UK_

_Corrigé du guide (p.8)_ : il n'est **pas** donné en liste mais sous forme d'un **schéma de mise en
page** — les lettres sont disposées sur une maquette de page, ce que l'extraction rend comme un nuage
de positions : `l` en haut à gauche et `e` en haut à droite ; puis `c` à gauche et `k` à droite ; puis
`b` ; `g` ; `j / a / f` ; `d / i` ; et `h` en bas à gauche. ⚠️ **La reconstitution exacte de ce schéma
est incertaine** (voir §6) : il s'agit d'une figure, pas d'un texte, et l'ordre relatif de
`j`, `a`, `f` d'une part et `d`, `i` d'autre part n'est pas déterminable de façon sûre à partir du
texte extrait. Ce qui est certain et exploitable : la lettre s'ouvre par les deux adresses et la date,
se ferme par `h` (formule de politesse + signataire), et `c` (« Dear Mr Godfather, ») est l'appel.

### Module One — IN TIME OF TEST, FAMILY IS BEST (manuel p.12-41 · guide p.9-20)

**Topic** (guide p.9) : _Family life and relationships_.
**Subtopics** (guide p.9) : _Family roles, the generation gap_.
**Cross-curricular learning goals** (guide p.9, verbatim) : _problem solving, critical thinking,
efficient use of data, efficient working procedure, appropriate self-expression, ICT use, project
work, communicating, working and living with others._

**Expected learning outcomes** (manuel p.12, verbatim) — « In this module, I'm going to » :

- use what I already know to acquire new words and ideas about family life and relationships
- listen to a poem
- read an expository text
- read a letter of complaint
- read a short story
- read an article in a magazine
- learn and practise lexical and grammatical items
- take part in a conversation
- write an article in a magazine
- produce a summary
- expand my knowledge of the world

**Compétences travaillées** (synthèse des cinq rubriques « Skills/subskills and strategies » du
guide, p.10-11-13-15-17, détaillées section par section ci-dessous) : lecture (valeur communicative,
transfert vers un tableau, structure du texte, public visé, intention, scan, inférence lexicale),
écoute (prédiction, sens implicite vs littéral, ton du poète, idée principale), parole (opinion,
plainte, interruption, jeu de rôle, description), écriture (phrases factuelles, contribution de vers
rimés, article argumenté, résumé).

**Grammar du module** (guide p.13, rubrique « Grammar » de la Section Three — la **seule** rubrique
Grammar du tronc commun de ce module) :

- `If + present + another present`
- `Want + object + to infinitive` structure
- `Make / Let / Have + object + base form`

Le guide p.14 en donne la valeur : « **If + present + another present** — To express automatic or
habitual results » ; « **Want + object + infinitive structure / Make / let / have + object + base
form** — To talk about things that a person **forces, asks or allows** someone to do. »
(Le supplément Arts ajoute une rubrique Grammar propre : **Word-building (affixation)**, guide p.20.)

**Pronunciation** (guide p.11, rubrique présente **uniquement** en Section Two) :

- silent letters
- consonant/vowel sounds

**Homework** (rubriques déclarées) : Section Two — « recognizing appropriate lexical items in
context » (guide p.11) ; Section Three — « fill in gaps with lexical items » (guide p.13).
**Project work / Mini-project** : **aucune rubrique « Mini-project » n'apparaît dans le guide
p.9-20 ni dans le manuel p.12-41** pour ce module — voir Incertitudes.

**Portée** : Sections One→Five = **tronc commun** (les six sections de 3ème année).
À partir de la page 29 du manuel commence le **supplément ARTS**, réservé à la filière **Lettres**.

---

#### Section One : Introductory activities

_(manuel p.13-16 · guide p.10)_

##### Scope and sequence (guide p.10, verbatim)

**Skills/subskills and strategies**

- _Reading_
  - identify the communicative value of texts (pictures)
  - evaluate ideas/information
  - transfer information onto a table
  - compare one's culture to that conveyed in the text
  - build on prior knowledge to further and enhance learning
  - acquire knowledge about a given topic
- _Speaking_
  - express one's opinion about a specific issue
  - describe one's impressions
  - make statements about facts
- _Writing_
  - produce sentences (make statements about facts / concrete situations)

**Vocabulary** : affective, career path, comfort, establish, functioning, handle, hoover (v),
instrumental, leadership, maintenance, management, nurture, reassurance, resource, shelter, skill,
standard, trash, warmth, water (v). _(20 items — identiques à la colonne « Section one » de la liste
de fin de module, manuel p.41.)_

**Functions** : expressing opinion · comparing attitudes · imparting information.

_(Pas de rubrique Grammar, Pronunciation ni Homework pour cette section.)_

##### Activity 1 (manuel p.13-14)

**A. « Look at the pictures and answer the questions. »** — page de 8 photos numérotées **1 à 8**
(manuel p.13, images non décrites par le texte imprimé ; leur contenu se déduit du corrigé ci-dessous).

**A.1.** « Match each picture with the appropriate role. Write the number of the corresponding
picture in the space provided. » — tableau à deux colonnes **role | picture** :

| role                             | picture |
| -------------------------------- | ------- |
| a) cooking                       | …       |
| b) caring for the children       | …       |
| c) washing                       | …       |
| d) watering the plants           | …       |
| e) taking out the trash          | …       |
| f) shopping                      | …       |
| g) hoovering                     | …       |
| h) taking care of grandparents   | …       |

**A.2.** « Now that you have completed the table, describe the pictures using your own words. »

**B.** « Consider the questions below then share your ideas with the class. »

1. Are such roles strange to you, or have they become a usual behaviour in our society ?
2. Should we establish clear roles within a family ? Why ? Why not ?
3. Do roles play an important part in healthy family functioning ?

**Corrigé (guide p.10)** — Activity 1 : **a+8, b+7, c+3, d+6, e+2, f+1, g+5, h+4**.
Soit : photo 1 = shopping · 2 = taking out the trash · 3 = washing · 4 = taking care of grandparents ·
5 = hoovering · 6 = watering the plants · 7 = caring for the children · 8 = cooking.

**Helpful note (guide p.10)** : « Activity 1 (A.2 and B.1,2,3) let the students talk freely and
spontaneously. Give help when asked for only. »

##### Activity 2 (manuel p.14-15)

**A.** « Read about the roles below and rank them in order of importance to you (from 1, the most
important to 4, the least important). Be ready to discuss your answer and share information with
your classmates. » — quatre encadrés précédés chacun d'un blanc `(…….)` :

> **(…….) PROVISION OF RESOURCES**
> Providing resources, such as money, food, clothing, and shelter, for all family members is one of
> the most basic, yet important, roles within a family. This is primarily an instrumental role.

> **(…….) NURTURANCE AND SUPPORT**
> Nurturing and supporting other family members is primarily an affective role and includes
> providing comfort, warmth, and reassurance for family members. Examples of this role are a parent
> comforting a child after he/she has a bad day at school, or family members supporting one another
> after the death of a loved one.

> **(…….) LIFE SKILLS DEVELOPMENT**
> The life skills development role includes the physical, emotional, educational, and social
> development of children and adults. Examples of this role are a parent helping a child make it
> through school, or a parent helping a young adult child decide on a career path.

> **(…….) MAINTENANCE AND MANAGEMENT OF THE FAMILY SYSTEM**
> This role involves many tasks, including leadership, decision making, handling family finances,
> and maintaining appropriate roles with respect to extended family, friends and neighbors [sic, US]. Other
> responsibilities of this role include maintaining discipline and enforcing behavioral standards.

**B.** « Are there any other roles which may enable the family to function properly ? »

**C.** « Read the text again and complete the table. » — tableau à deux colonnes de **8 lignes**
chacune, amorcé par un exemple par colonne :

| Instrumental roles | Affective roles  |
| ------------------ | ---------------- |
| Providing money    | ……               |
| ……                 | ……               |
| ……                 | Providing warmth |
| ……                 | ……               |
| ……                 | ……               |
| ……                 | ……               |
| ……                 | ……               |
| ……                 | ……               |

_(Matière disponible dans les quatre encadrés : instrumental — providing money/food/clothing/shelter,
leadership, decision making, handling family finances, maintaining discipline, enforcing behavioral
standards ; affective — providing comfort, warmth, reassurance, comforting a child, supporting one
another after a death.)_ **Aucun corrigé n'est donné par le guide pour C.**

**Encart décoratif (manuel p.15)** : « A family that plays together stays together ».

##### Activity 3 (manuel p.16)

« The following roles are essential for a healthy family. »

1. Who does what in your family ?
2. Which roles are instrumental and which ones are affective ? Tick the appropriate box then compare
   your answers in small groups.
3. What other roles may you add ?

Tableau à remplir — colonnes : **father | mother | brother | sister | Instrumental role | Affective
role** ; **13 lignes** (Roles), verbatim :

1. Making decisions
2. Taking out the trash
3. Cooking meals
4. Washing up
5. Shopping
6. Providing affective support
7. Taking a little child to school
8. Maintaining discipline
9. Providing money
10. Ironing
11. Gardening
12. Feeding the cat / the dog / the birds
13. Accompanying a family member to the doctor

**Helpful note (guide p.10, verbatim)** : « Activity 3. After ticking the appropriate boxes and
comparing answers in small groups, encourage the students to produce complete written sentences.
Examples : – My father / mother usually makes decisions at home. – Providing money is my
mother's/father's role. – Both my father and my mother provide money. – My sister often feeds the
cat/the birds. etc »

---

#### Section Two : Listening

_(manuel p.17-19 · guide p.11-12 · tapescript guide p.76)_

##### Scope and sequence (guide p.11, verbatim)

**Skills/subskills and strategies**

- _Listening_
  - predict content
  - identify vocabulary items
  - guess the meaning of unfamiliar words through context clues
  - distinguish between literal and implied meanings
  - identify features of the genre (tone of the poet)
  - identify main idea
- _Speaking_
  - read/recite a poem in an expressive manner
  - pronounce properly at word and sentence level
- _Writing_
  - contribute lines with rhyming patterns to a poem

**Vocabulary** : assignment, cherish, curl, error, fulfil, gaze, laughter, make a decision,
many a + (n), overburdened, set (a table), share roles, store, task, tear, trial. _(16 items.)_

**Functions** : enquiring about information · asking for opinion · expressing attitudes.

**Pronunciation** : silent letters · consonant/vowel sounds.

**Homework** : recognizing appropriate lexical items in context.

##### Le support écouté — ⚠️ œuvre sous droits (R-2)

**Genre** : poème. **Titre** : non imprimé (le manuel ne titre pas le texte).
**Auteur** : **Paula S. Dickinson** (manuel p.18, guide p.76).
**Forme** : 16 vers, rimes plates (aa bb cc …), dialogue **père ↔ fils** — le fils demande ce qu'est
« une famille », le père répond par une énumération d'images de la vie familiale.
**Thème** : la famille n'est pas la liste de ses membres mais la somme des petits moments partagés —
la fierté devant les productions de l'enfant, les premières fois, les histoires au coin du feu, les
essais et les erreurs, les rires et les larmes qui traversent les années.
**Ton** : émotionnel (corrigé G.2 du guide).
**Conformément à R-2, aucun vers n'est reproduit ici** : ni depuis le manuel p.18 (version à trous),
ni depuis le tapescript intégral du guide p.76. Les mots à retrouver, eux, sont l'objet lexical
enseigné et figurent au corrigé ci-dessous.

##### BEFORE YOU LISTEN (manuel p.17)

« Complete the words in the following sentence then check your answers with your classmate's » —
acrostiche vertical à compléter :

```
F…………
And
M……….
I
L………….
You
```

**Corrigé (guide p.11, Helpful notes)** : « the sentence is : **Father And Mother I Love You** ».

##### AS YOU LISTEN (manuel p.17-18)

**A.** « Listen to the first three lines and : »

1. find out who the speakers are.
2. in pairs, guess and talk about what is meant by « it's much more than that ».

_(Corrigé attendu, non imprimé : les locuteurs sont **un fils et son père**.)_

**B.** « Look at the pictures, listen and complete the boxes with words from the poem. » — **6**
images numérotées 1 à 6, chacune avec une case-mot à remplir.
**Corrigé (guide p.12)** : **1: curls · 2: (new) hat · 3: drawings · 4: stories · 5: laughter ·
6: tears**.
**Helpful note (guide p.11)** : « In case the students encounter difficulties in finding the words
(As you listen B), provide the beginning of each word to facilitate the task. »

**C.** « Tick the right alternative. » — trois items lexicaux, trois options chacun :

| item                       | a)                        | b)                | c)                    |
| -------------------------- | ------------------------- | ----------------- | --------------------- |
| « to cherish » means :     | to look for               | to dream of       | **to keep alive**     |
| « gaze at » means :        | **look long and steadily at** | look fixedly at | look attentively at   |
| « many a night » means :   | **many nights**           | only one night    | few nights            |

**Corrigé (guide p.12)** : « 1. cherish + c, 2. gaze at + a, 3. many a night + a ».

**D.** « Match each statement in column A with its implied meaning (interpretation) in column B.
Write your answers in column C. »

_Colonne A — quatre énoncés repris du poème. **Non reproduits (R-2)** ; identifiés ici par leur
contenu :_

1. le vers qui nomme **les boucles de la petite Sue et le chapeau neuf de la mère** ;
2. le vers sur **les premiers dessins de l'enfant que les parents rangent et conservent** ;
3. le vers sur **le regard perdu de la mère le premier jour d'école** ;
4. le vers sur **les essais et les erreurs, les rires et les larmes**.

_Colonne B — quatre interprétations, celles-ci rédigées par le manuel, verbatim :_

- a) Parents value their children's productions.
- b) Sharing the good and bad experiences strengthens family relationships
- c) Family members show interest in one another ; in the way they look, the clothes they buy…by
  saying nice words like : You look lovely, I like your … Oh, how nice ! etc
- d) Parents are concerned about their children when they are out of sight.

**Corrigé (guide p.12)** : **1 + c, 2 + a, 3 + d, 4 + b**.
**Note du guide (p.12)** : « Another statement in the poem that could match b in column B is : “The
trials and errors, the laughter and tears” ».
**Helpful note (guide p.11)** : « Invite the students to infer any other implied meanings in the four
statements suggested or in other statements in the poem. The purpose is to enhance their critical
thinking and interpretative skills. »

**E.** « Go back to your guesses and try to improve them if you think they need improving. »

**F.** « Listen and complete with the missing words. Check the spelling of these words in pairs. » —
le poème intégral (16 vers) est imprimé **avec 10 blancs**. **Le texte n'est pas reproduit ici (R-2).**
Les mots manquants, **dans l'ordre des blancs** :

1. **able** (ce que Jackie apprend qu'elle est, à propos de la table)
2. **setting** (…the table)
3. **away** (store …)
4. **cherish** (To … and gaze at)
5. **day** (some future …)
6. **lost** (le regard de la mère)
7. **Learning** (… to live by the 'Golden Rule')
8. **stories** (fireside …)
9. **laughter** (the … and tears)
10. **years** (down through the …)

Le guide (p.12) renvoie simplement : « F. See tapescript to complete the missing words in the poem. »
⚠️ Un onzième blanc apparaît dans la couche-texte du manuel p.18 — voir Incertitudes.

##### (manuel p.19)

**G.** « Listen and tick the right alternative. »

1. The poem is about
   a. the different members that make up a family
   b. the different instrumental roles of family members
   **c. the different types of relationships that characterize family life**
2. The poet's tone is
   a. regretful.
   **b. emotional.**
   c. ironical.

**Corrigé (guide p.12)** : **1 + c, 2 + b**.

**H. Pronunciation**

1. « Listen to the tape and say what these words have in common » : **meant, which, first, through,
   right**. → **Corrigé (guide p.12)** : « H. Pronunciation : 1. **silent letters** ».
2. « Say whether the underlined sounds of the pairs of words are the same or different. » — trois
   paires : **future / cherish** · **laughter / family** · **meant / learn**.
   _(Pas de corrigé au guide ; les lettres soulignées ne sont pas restituées par la couche-texte —
   voir Incertitudes.)_
3. « Now, volunteer to read the poem aloud and in an expressive manner. »

**Helpful note (guide p.11)** : « Encourage the students to overcome their shyness and read the poem
in an expressive manner (changing and varying intonation and using gestures). »

##### AFTER YOU LISTEN (manuel p.19)

« Work in groups. Think of pairs of words that have the same rhyme like (take and make, light and
sight …) then contribute two lines using the rhyming patterns. »

##### Homework (manuel p.19)

« Circle the appropriate alternative. » — texte expositif à 8 choix, verbatim :

> Families have to **(do / make / find)** many decisions, often on a daily basis, about who will be
> responsible **(for / to / at)** completing a certain task or **(fulfillment / fulfill / fulfilling)**
> a particular responsibility. For example, families must decide who takes out the trash, who will
> take the children to school, who will cook **(a dinner / dinner / the dinner)**, who will work and
> provide **(finance / financially / financial)** support **(to / in / for)** the family.
> In healthy families, roles are **(assigned / assignment / assigning)** in such a way that family
> members are not overburdened. **(Share / Sharing / Shared)** roles, such as child care, is an
> important family task.

**Corrigé (guide p.12)** : **1 + make, 2 + for, 3 + fulfilling, 4 + dinner, 5 + financial, 6 + for,
7 + assigned, 8 + Sharing**.

---

#### Section Three : Reading

_(manuel p.20-24 · guide p.13-14)_

##### Scope and sequence (guide p.13, verbatim)

**Skills/subskills and strategies**

- _Reading_
  - tap on from different parts of the text to answer a specific question
  - identify audience
  - identify purpose
  - recognize text structure
  - evaluate ideas
  - guess the meaning of unfamiliar words in context
  - scan for specific information
- _Speaking_
  - make statements about a concrete situation
  - express judgements about a specific issue

**Vocabulary** : alone, barge, blow, date (v), depressed, dry (v), dust (v), edge, end up, exert,
expectations, feed, feel like, frustrated, guess, heart-broken, misconduct, openly, overwhelmed,
parenting, pressure, puppet, push, sloppy, sympathize, thought, turn out, well-mannered. _(28 items.)_

**Grammar**

- If + present + another present
- Want + object + to infinitive structure
- Make / Let / Have + object + base form

**Functions** : expressing opinion · talking about a personal experience · expressing
approval/disapproval · describing a situation.

**Homework** : fill in gaps with lexical items.

##### Helpful notes (guide p.14, verbatim)

- « The expression “see eye to eye” is not mentioned in the vocabulary list. However, it is worth
  presenting to the students. **See eye to eye (with) : agree entirely (with), have incidental views** »
  [sic — lire vraisemblablement « identical views »].
- « “sloppy” is not a frequent word, so don't make much fuss about it »
- « Before you read. C 1 and 2. Have the students focus on the picture and construct as much meaning
  as possible while drawing on their background knowledge and personal experience. »
- « After you read, 1 and 2. Encourage the students to express their opinions freely, but keep asking
  them to justify and support their attitudes with sound and pertinent arguments. »
- **Grammaire** : « If + present + another present — **To express automatic or habitual results** » ;
  « Want + object + infinitive structure / Make / let / have + object + base form — **To talk about
  things that a person forces, asks or allows someone to do.** »
- Démarche inductive attendue : « The students are expected to explore and review language items in
  an inductive way, with the intention of reinvesting them in higher level speaking/writing
  situations. This implies that the students should – recognize language items in context – recognize
  form – infer the function/communicative value of the item – practise language items in a variety of
  contexts – apply the items in a variety of situations using the thematic context ».

##### BEFORE YOU READ (manuel p.20)

**A.** « Do you often see eye to eye with your parents on a lot of things ? »

**B.** « Below are some examples of “misconduct” that may easily make some parents angry. In pairs
continue the list then tick the ones that apply to your case ? » — liste amorcée de 4 items + 4
tirets vides à compléter :

- Listening to music at full volume
- Dating someone
- Inviting some friends over when parents are out
- Going to a night club
- (4 lignes libres)

**C.** « Look at the picture of a mother and her daughter » — 1. Guess what they are talking about.
2. How is the relationship between them ?

##### AS YOU READ — le texte support (manuel p.20-21)

**Titre** : « **I'm really overwhelmed …** ». **Genre** : lettre de plainte / témoignage de page
« problèmes » (le manuel l'annonce dès p.12 : « read a letter of complaint »).
**Signature** : « **Kelly, 17** ». **Longueur** : ~520 mots, 6 paragraphes. Texte **non littéraire**
→ résumé fidèle ci-dessous, citations courtes limitées à ce qui porte la langue enseignée.

**Résumé détaillé (fidèle, § par §)**

1. Kelly reconnaît que « parenting is a job like no other », mais demande pourquoi les parents
   exercent parfois autant de pression. Ses parents ont de fortes attentes ; ils prétendent
   n'attendre que son mieux, « but they really do » (attendre davantage).
2. **Le père** : ancien athlète professionnel qui s'entraînait sans arrêt. Kelly joue beaucoup au
   **softball** et le prend au sérieux, mais son père « pushes me over the edge » avec des
   entraînements le week-end et un discours permanent sur la technique et la concentration. Elle se
   dit « really overwhelmed sometimes ». Il voudrait aussi qu'elle soit l'élève qu'il n'a jamais été :
   si elle obtient **un B** à un devoir, il lui répète qu'elle n'a pas assez travaillé et qu'un B
   n'est pas satisfaisant.
3. Kelly se pousse déjà elle-même ; elle a le sentiment que pour « être quelqu'un » elle doit tout
   réussir parfaitement. Elle voudrait que son père se réjouisse d'un B — « I need him to be. »
4. **La mère** : se plaint sans cesse que Kelly est désordonnée et négligée (« unorganised and
   sloppy ») ; en plus de la course à la perfection, il faut être propre et bien élevée. Elle veut
   « control every aspect of my life ».
5. **L'exemple de l'épisode du téléphone** : Kelly, le cœur brisé à cause d'un garçon, pleurait au
   téléphone avec sa meilleure amie. Sa mère a fait irruption (« barged in ») et a voulu la faire
   parler. Kelly a demandé à rester seule ; sa mère n'est pas partie, alors Kelly a fini par tout
   raconter — et la première question de sa mère a été « **What is his name ?** » : elle cherchait à
   identifier le garçon.
6. Sa mère ne s'est pas souciée de ce qu'elle ressentait. Devant le refus de Kelly de donner le nom,
   elle a invoqué son droit de mère à savoir, puis a quitté la chambre et lui en a voulu toute la
   nuit. Conclusion de Kelly : elle aime ses parents, mais tout se passe mieux quand elle garde ses
   problèmes pour elle ; ils « blow the problem out of proportion » avant d'essayer de l'aider.
   « My life is my life, but they want it to be theirs. **I feel like a puppet sometimes.** »

**A.** « Read the beginning and the end of the text to find out who “I”, in the title, refers to. »
_(→ Kelly, 17 ans.)_

**B.** « Read the whole text and answer the questions below. » (manuel p.21)

1. Who are the intended readers of this text ? Why did Kelly write it ? – to inform ? – to complain ?
   – to persuade ?
2. In which part of the text, Kelly – expresses feelings ? – states the problem ? – gives examples ?
3. « Match each word/expression in A with its meaning in B. »

   | A                                        | B                                                      |
   | ---------------------------------------- | ------------------------------------------------------ |
   | 1. Exert                                 | a) Have an exaggerated view of things                   |
   | 2. Sloppy                                | b) Enter rudely or forcefully                           |
   | 3. Barge in                              | c) Person whose actions are controlled by another       |
   | 4. Blow the problem out of proportion    | d) Careless/untidy                                      |
   | 5. Puppet                                | e) Put forth/bring into use                             |

   **Corrigé (guide p.14)** : « As you read. 3. **1 + e, 2 + d, 3 + b, 4 + a, 5 + c** ».

4. What are the areas of misunderstanding between Kelly and her parents ?
5. What do Kelly's father and mother have in common ?
6. How is Kelly's relationship with her boyfriend ?

##### Exploring grammar — Activity 1 (manuel p.22)

« Work with your classmate. Examine the following sentences and discuss the questions that follow. »

- If I get a B on a test, he always tells me in some form or another that I didn't study hard enough.
- I think things turn out better if I keep my problems to myself.
- If you have a problem, you need to tell us.

a) « What do the sentences have in common ? Focus on the form. » — cadre à compléter :

```
If clause + ............................................
    Or
Main clause + .........................................
```

b) « – What tenses are used in both clauses ? – Discuss the function of the structure in each
sentence. » — cadre à compléter :

```
If + ....................... + .................................
is used to express ....................................
```

**Règle visée (guide p.14)** : `If + present + another present` → **to express automatic or habitual
results**.

##### Exploring grammar — Activity 2 (manuel p.22)

« Work with a classmate. Read the sentences below. Carefully examine the underlined words. Then
consider the questions that follow. »

- He also wants me to be the student he never was.
- She tried to make me tell her what was wrong.
- My parents rarely let me stay out after midnight [sic — point final absent]
- The teacher had all the pupils do the homework.

1. « What do you notice about the form in each sentence ? Complete : »

```
Want   + ........................... + ...........................

Make
Let    + ........................... + ...........................
Have
```

« What is the meaning expressed in each sentence ? To talk about things that a person ……………, asks or
…………… someone to do. » → **forces … allows** (guide p.14).

##### AFTER YOU READ (manuel p.23)

« Discuss the following questions with your classmate(s). »

1. Whom do you sympathize with ? Kelly or her parents ?
2. What would you do if you were in Kelly's situation ?
3. Do you have any misunderstandings with your parents ? if yes, what are the reasons ?

##### Homework (manuel p.23)

« Fill in the blanks with the appropriate words from the list. »
**Banque de mots (9)** : _(stresses, wrong, support, politely, pressure, openly, way, nothing,
approach)_ — pour **7** blancs seulement (2 distracteurs).

> This is what 16-year-old Dion says :
> « Trying to communicate with parents is hard for teenagers. We need somebody to **1**……… us, and we
> need someone who will listen. There is so much **2**……… and so many issues that teenagers can't talk
> about with their parents. I can't talk to my parents about anything. I don't tell them how I feel,
> what I want, and it really **3**……… me because I need to tell someone. I wish I could talk to my
> parents **4**………, knowing they wouldn't make me feel “less”, and knowing that they will listen
> first, instead of saying “we don't have time for this right now.” (This is me – they don't have time
> for me.) If I could talk to them, I would **5**……… them about this. Sometimes I've started talking to
> my mom about what I feel, but one **6**……… or another she makes me feel **7**……… and I end up
> depressed and feeling that she doesn't care. »

**Corrigé (guide p.14)** : « **1. support, 2. pressure, 3. stresses, 4. openly, 5. approach, 6. way,
7. wrong** » — distracteurs non employés : **politely**, **nothing**.

##### Practising related grammar points — Exercise 1 (manuel p.23)

« Work with a classmate to do the following exercise. Combine the sentences using **if** and add what
is necessary. No.1 has been done for you. »

1. want to come back late. Ask for permission. (father to son)
   → « If you want to come back late, you need to ask for permission. » **Or** « You need to ask for
   permission if you want to come back late. » _(exemple donné)_
2. Your daughter is troubled. Analyse the situation before making any conclusions. (consultant to mother)
3. Trust your children. Respect and appreciate you. (advice columnist to a parent)
4. Parents fail to fulfil their roles properly. Child behaviour problems. (expert in education)
5. Roles are not fairly spread among the various members. Some members become overburdened.
   (consultant to father)
6. Establish clear, flexible and fair family roles. Members take their responsibilities seriously.
   (expert giving a lecture)

_(Pas de corrigé au guide au-delà de l'item 1.)_

##### Exercise 2 (manuel p.24)

« Write complete sentences. Then compare your answers with your classmate's. » — amorce commune :
« **What do you do if ………** »

- you don't get along with your parents ?
- you can't make your own decisions ?
- your parents prevent you from inviting your friends home ?
- you forget to say good morning to your brother / sister ?
- your father doesn't give you your pocket money ?
- you fail an English test ?
- there's much noise at home and you can't revise for your exams ?

_(7 amorces. Pas de corrigé.)_

##### Exercise 3 (manuel p.24)

« Complete with the right form of the verbs in brackets. » — 5 items, 11 blancs au total :

1. My mother made me **(to clean)** ………… and **(to dry)** ………… the dishes as soon as we had finished
   dinner last evening.
2. My neighbour, Steve, wants his son, Paul **(to take)** ………… their dog for a walk every afternoon.
3. Parents should help their children to overcome their problems. They shouldn't make them
   **(to feel)** ………… frustrated. Indeed, they have to let them **(to talk)** ……… and **(to express)**
   ………… their opinions freely.
4. Last Sunday, my father wanted me **(to dust)** ………… the furniture and **(to hoover)** ………… the
   carpets and my mother made my brother **(to water)** ………… the plants and **(to feed)** ………… the cat.
5. Never spoil your children. Don't let them **(to do)** ………… whatever they like. Make them
   **(to respect)** ………… you and **(consider)** ………… your status as parents. But help them become
   responsible family members.

_(Pas de corrigé au guide. Application attendue : `make/let + base form`, `want + object + to +
infinitive`.)_

##### Exercise 4 (manuel p.24)

« Consider the situations in column A and use **let, make or want** to complete the sentences in
column B. »

| A (situation)                                                          | B (amorce à compléter)                              |
| ---------------------------------------------------------------------- | --------------------------------------------------- |
| A father talking to his daughter who got bad marks                     | I……………………………………………. next term.                     |
| A boy who is often prevented from giving parties at home               | My parents ……………………………………………………………………             |
| Jill wants to know about Sarah's secrets                               | Don't try to ……………………………………… I'll never do it.     |
| A mother talking to her daughter. She's angry with her because of her misconduct | I ………………………………………….……………………………………………… |
| An overburdened housewife shouting at her children                     | Don't ……………………………………. ……………………………………………           |
| A mother talking to her careless children                              | I …………………………….. make your beds before you leave.   |

_(6 situations. Pas de corrigé.)_

---

#### Section Four : Speaking

_(manuel p.25-26 · guide p.15 · tapescript « Dialogue 1 », guide p.76)_

##### Scope and sequence (guide p.15, verbatim)

**Skills/subskills and strategies**

- _Reading / Listening_
  - infer the main idea
  - recognize the relationship between form and meaning
  - acquire knowledge of the language (idiomatic expressions)
- _Speaking_
  - reinvest vocabulary and structures in one's speech
  - express alternative
  - express opinion about a specific issue
  - make a complaint using the proper discourse strategies
  - respond to criticism
  - enact a role
  - demonstrate appropriate use of social skills required in interactional contexts (interrupting,
    taking turns …)
- _Writing_
  - take notes

**Vocabulary** : blame, bother, can't help it, chores, demanding, exhausted, for heaven's sake, lazy,
messy, upset. _(10 items.)_

**Functions** : complaining about a (difficult) situation · interrupting the speaker · expressing
opinion · expressing disagreement.

##### Helpful notes (guide p.15, verbatim)

- « Have the students identify the communicative value of each of the following expressions
  “for heaven's sake”, “get in someone's hair”, “I can't help it” »
- « Have the students reinvest their previous lexical acquisitions as well as the new vocabulary and
  ideas related to the thematic context (family roles) »
- « Make the students pay much attention to the way the woman talks in the dialogue. This will help
  them apply the intonation patterns later in the conversation. Step 2 in Activity 2 should be
  clarified to the students. »
- « Make sure they use the expressions suggested and give help when asked for. »
- « Let the students interact and talk fluently without worrying too much about mistakes. »

##### Activity 1 (manuel p.25)

« You are going to read and listen to a short dialogue. In the dialogue, there are two blanks.
In **blank 1**, there is an **American English idiomatic expression**. In **blank 2**, we have a
**definition of the idiomatic expression**. »

**A.** « Listen carefully and complete the missing items. Then, compare your notes with your
classmate's. » — dialogue verbatim (texte fonctionnel, non littéraire) :

> **Clara** : Children ! Would you please stop making so much noise ! And for heaven's sake, pick up
> your clothes and toys ! It's hard enough trying to keep this house clean without your throwing your
> things all over the place !
> **Jim** : Clara, I know that the children **………………………** [blanc 1], but you should try not to let it
> upset you so much.
> **Clara** : Listen, Jim. I can't help it. The children **…………………………** [blanc 2] when they're so noisy
> and messy.

**Corrigé (déduit du tapescript, guide p.76)** : blanc 1 = « **get in your hair** » ; blanc 2 =
« **bother me and make me very angry** ».

**B.** « What's the woman complaining about ? »

##### Activity 2 (manuel p.25-26)

**Step 1** — « Work in groups of 4. Consider the following situation. **Clara takes part in a radio
programme dealing with family problems. She talks about how overburdened she is and the very little
assistance she gets from the other family members. The radio presenter and two other listeners take
part in the conversation. They express their opinions about the issue.** Here are some phrases that
you can use in the conversation. »

**Banques d'expressions fonctionnelles (verbatim, manuel p.25-26)**

_Complaining_ :

- I am really …………………………….
- I feel like a …………………………….
- They want me to …………………….
- Why should I …………………….. ?
- I just wish ………………………………
- I don't like ……………………………..
- I don't know why ………………………

_Interrupting_ :

- Before you go on, let me……..
- Could I stop you here for a moment / Can I butt in here ?
- Could I question your last point ?

_Expressing disagreement_ :

- I don't agree
- You have a point, but …………………….
- Oh no, …………………….
- I see what you mean, but …………………
- But surely you don't ………………………..
- What you say is interesting, however ………………
- Well, that might be true, but ………………

_Expressing opinion_ :

- I think / feel / believe that …………….
- In my opinion, ………………..
- To my mind, ……………..
- As far as I am concerned, …………..
- I sort of think ………………

**Step 2** — « Take a few minutes to prepare before you speak. Pupil A : Clara. Pupil B : Radio
Presenter. Pupil C : Listener 1. Pupil D : listener 2. » Exemple imprimé, verbatim :

> **Clara** : I am really exhausted. They want me to do all the home chores. My children are noisy and
> messy. My husband is lazy and demanding.
> **Radio Presenter** : You have a point, but who is to blame in your case ?
> **Listener 1** : Could I stop you here for a moment ? (blaming the mother)
> **Clara** : (responding to listener 1. Giving more examples)
> **Listener 2** : (agreeing with the mother)
> **Radio Presenter** : Well, that might be true, but ………..
> **Listener 1** : ……………………………………

« Continue the conversation. »

**Step 3** — « – Be ready to perform the conversation within your own group. – Volunteer to enact the
conversation in front of your classmates. »

##### Activity 3 (manuel p.26)

« As your classmates are enacting the conversation in front of you, take notes. Then, as a class,
debate the key issues. »

##### Time for a song (manuel p.27 · guide p.16) — ⚠️ œuvre sous droits (R-2)

**Titre** : « **Father and Son** » — **auteur/interprète : Cat Stevens**. **Genre** : chanson,
dialogue **père ↔ fils** en strophes alternées (Father / Son / Father / Son).
**Thème** : le fossé des générations — le père conseille la patience, le mariage, le fait de ne rien
brusquer ; le fils dit qu'il n'arrive pas à se faire entendre, qu'on lui a toujours demandé
d'écouter, et qu'il doit partir.
**Conformément à R-2, aucun vers de la chanson n'est reproduit** — ni depuis le manuel p.27 (version
à trous), ni depuis le tapescript intégral du guide p.77.
**Rattachement** : page **du tronc commun** (aucune marque « Arts »), placée entre la Section Four et
la Section Five ; le guide la traite au même endroit (p.16).

**Consignes du manuel (verbatim, p.27)**

1. « Listen to the following song and complete the gaps. **Each dot stands for a letter.** »
2. « Read the song aloud and focus on correct pronunciation. »
3. « Think of possible answers to the following questions then share your ideas with your classmates. »
   - Why couldn't the father and his son communicate easily ?
   - What do they disagree on ?
   - Who's to blame, the father or the son ?
   - Is it possible for them to get on well ? How ?
4. « Now, let's sing the song. Half the class may sing the father's verses and the other half the
   son's »

**Les 16 blancs et leur solution** (relevés dans l'ordre d'apparition ; solutions établies d'après le
tapescript guide p.77) :

| # | amorce imprimée   | mot attendu |
| - | ----------------- | ----------- |
| 1 | `ea . .`          | easy        |
| 2 | `y . . . .`       | young       |
| 3 | `set . . . down`  | settle      |
| 4 | `h . . . .`       | happy       |
| 5 | `g . . . . on`    | going       |
| 6 | `a l . .`         | lot         |
| 7 | `dr. . . s`       | dreams      |
| 8 | `ag . . .`        | again       |
| 9 | `s . . . .`       | story       |
| 10| `ord . . . .`     | ordered     |
| 11| `a . . .`         | away        |
| 12| `sl . . . .`      | slowly      |
| 13| `thr . . . .`     | through     |
| 14| `c . . . .`       | cried       |
| 15| `ig . . . .`      | ignore      |
| 16| `k . . .`         | know        |

**Procédure du guide (p.16, verbatim)** : « • Follow the procedure suggested in the textbook • The
complete text is provided in the Tapescript Section • Have the students – listen and complete the
gaps – read the song aloud and pronounce correctly – listen again and check the accuracy of
pronunciation – study the text and answer questions (see instruction 3) – react to the text and
express opinion – sing the song as suggested in instruction 4. »

---

#### Section Five : Writing

_(manuel p.28 · guide p.17 · tapescript « Dialogue 2 », guide p.76)_

##### Scope and sequence (guide p.17, verbatim)

**Skills/subskills and strategies**

- _Listening_
  - transfer information onto a table
  - scan for specific information
- _Writing_
  - reinvest vocabulary and structures in one's writing
  - express opinion about a specific issue and support one's opinion with arguments
  - apply the writing process to produce a composition

**Vocabulary** : accomplishment, deal, fit in with someone's taste, intend, scold, value. _(6 items —
la liste de fin de module en compte 7, voir Incertitudes.)_

**Functions** : expressing opinion · describing a situation · expressing satisfaction/dissatisfaction
· talking about causes and effects · expressing want and desire.

##### Helpful notes (guide p.17, verbatim)

- « While dealing with the listening dialogue elicit the meaning of “**jump down someone's throat**”
  from the students. **Jump down someone's throat : Informal. to disagree with, criticize, or scold
  overhastily.** Example : *Wait and let me finish before you jump down my throat.* »
- « Activity 2. Have the students explore the following expressions in context : **take a great deal
  of pride in …, be angry with someone about something, value something, fit in with someone's
  taste**. »
- « Ask the students few [sic] comprehension questions related to Mike's letter. »
- « Encourage the students to reinvest their previous acquisitions as well as the newly-learnt lexical
  items and structures and the newly-constructed/reconstructed ideas and concepts about the
  generation gap. Make sure the students go through the different stages of the writing process and
  give due consideration to the aspects of writing and evaluation criteria mentioned. »
- « Involve the students in suggesting other evaluation criteria in addition to the ones mentioned in
  the textbook (**coverage of ideas, coherence, language accuracy**). Ask them the following
  question : “**What makes a good writing ?**” then elicit criteria such as **presentation, use of
  linkers, use of appropriate vocabulary, fluency** etc. »

##### BEFORE YOU WRITE — Activity 1 (manuel p.28)

« Listen to the dialogue and complete the table below. »

| speakers | place | problem |
| -------- | ----- | ------- |
| ……       | ……    | ……      |

**Support** : « Dialogue 2 » du tapescript (guide p.76) — un **père** et son fils **Greg** ;
le père reproche à Greg de rentrer après minuit ; Greg promet de rentrer vers 23:30 et dit ne pas
avoir l'intention d'être en retard ; le père rappelle qu'il l'a déjà dit et qu'il rentre à 2:30 du
matin, et se juge fondé à se fâcher et à le gronder. **Aucun corrigé imprimé pour le tableau.**
_(Le lieu n'est pas nommé dans le tapescript — voir Incertitudes.)_

##### Activity 2 — AS YOU WRITE (manuel p.28)

« As you were reading the problem page in your favourite English magazine, you came across this short
letter. » — **lettre de Mike**, verbatim (texte fonctionnel court) :

> « I am 17 years old. I know that my parents take a great deal of pride in seeing me succeed.
> However, I have been angry with them. They don't accept me for who I am. They don't take better
> care of me and they don't value any accomplishment that doesn't fit in with their own tastes. »
> — **Mike.**

« You decided to **write an article to the same magazine**, in which you answer the following
questions. »

1. Do you enjoy enough freedom to do whatever you like ?
2. Do your parents accept you for who you are ?
3. What are the areas of misunderstanding between you and your parents ?
4. What causes them ?
5. How can the relationship be improved ?

**Le processus d'écriture imprimé (verbatim)** :

- Write your first draft.
- Re-read your article to check if you have covered all the ideas.
- Read again and focus on **coherence** (the internal logic) in your writing.
- Now, read and correct any language mistakes you may find.
- Exchange your writing with your classmate's and give feedback to each other.
- Write your final draft at home.

---

#### Supplément ARTS (filière Lettres uniquement)

_(manuel p.29-38 · guide p.18-20)_ — **Fin du tronc commun à la page 28 du manuel.** Deux sections
supplémentaires, signalées dans le manuel par le bandeau « **Arts** » en haut de chaque page (p.29 à
p.38). _La couleur rose annoncée par le book map n'est pas restituée par la couche-texte ; c'est le
bandeau « Arts » qui délimite le supplément — voir Incertitudes._

##### Arts · Section One : READING A SHORT STORY (manuel p.29-34 · guide p.18-19)

###### Scope and sequence (guide p.18, verbatim)

**Skills/subskills and strategies**

- _Speaking_
  - describe one's impressions about a particular event
  - make statements about a personal experience
- _Reading_
  - predict content through title and pictures
  - locate and analyze elements of a short story (character, setting, point of view, conflict, plot,
    theme, denouement, climax)
  - distinguish between literal and implied meanings
  - use the strategy appropriate to the nature of text and purpose of reading
  - scan for specific details
  - evaluate and react to content
  - follow a sequence of events in a narrative
- _Writing_
  - produce a summary of the main points in a written text

**Vocabulary** : powder, apartment, cascade, character, climax, comb, conflict, critically,
denouement, expense, fellow, foolishness, hunt, intensity, moral, plot, point of view, poverty,
setting, sign, step in, struggle, suspense, theme, turn white, undo, worthy of. _(27 items.)_

**Functions** : describing a personal event · expressing feelings · expressing opinion.

###### BEFORE YOU READ — Activity 1 (manuel p.29)

**Step 1** — « Remember the last time you were offered a special present. What was it ? What was it
like ? What was the occasion ? Who offered you the present ? How did you feel ? »
**Step 2** — « Work with your classmate. Tell each other about it. »

**Helpful note (guide p.18)** : « Before you read. Activity 1. Encourage the students to talk about
their personal experience and share information and feelings with one another. To make the activity
more motivating, tell the students to close their eyes, recall, concentrate and visualize the event
then talk about it. »

###### BEFORE YOU READ — Activity 2 (manuel p.29)

« In the following list, there are different elements of a short story. **(theme, point of view,
character, plot, climax, conflict, setting, denouement)** In small groups, write the appropriate
element in front of its corresponding definition. » — **8 définitions, verbatim** :

1. « A person, or sometimes even an animal, who takes part in the action of a short story or other
   literary work » → **character**
2. « The time and place in which a short story happens. Authors often use descriptions of landscape,
   scenery, buildings, seasons or weather to provide a strong sense of……. » → **setting**
3. « A struggle between two people or things in a short story. The main character may struggle against
   another important character, against the forces of nature, against society, or even against
   something inside himself or herself (feelings, emotions, illness …….) » → **conflict**
4. « A series of events and character actions that relate to the central conflict. The way in which
   the story elements are arranged. The sequence of events in a story, in which each event causes or
   leads to the next. » → **plot**
5. « The final stage, where everything is made clear, in the development of the plot of the story. »
   → **denouement**
6. « The central idea or belief in a short story. The moral of the story. » → **theme**
7. « The point of greatest emotional intensity, interest, or suspense in a story. It is an element of
   the plot. » → **climax**
8. « **First Person** : The story is being told through the voice of one specific character. The
   character uses the first person pronoun “I” when narrating the story. **Third Person Limited** :
   The story is being seen through the eyes of one particular character. The narrator uses the
   pronouns “he” or “she” when telling the story. **Omniscient** : The story is told by an all knowing
   narrator who supplies more information about all the characters and events than anyone could
   know. » → **point of view**

**Corrigé (guide p.18)** : « Before you read. **1 + character, 2 + setting, 3 + conflict, 4 + plot,
5 + denouement, 6 + theme, 7 + climax, 8 + point of view.** »

###### BEFORE YOU READ — Activity 3 (manuel p.30)

« Look at the pictures, read the title of the short story and predict what it is about. Share your
prediction with your classmates'. » _(page entièrement illustrée, sans texte)_

###### AS YOU READ — le support (manuel p.31-33) — ⚠️ œuvre sous droits (R-2)

**Titre imprimé** : « **The Christmas Present** ». **Auteur** : **O. Henry** (le manuel ne donne pas
le titre original ; il s'agit d'une version abrégée/simplifiée de « The Gift of the Magi »).
**Genre** : nouvelle littéraire. **Découpage imprimé** : **Part 1** (manuel p.31-32) et **Part 2**
(manuel p.32-33). **Longueur** : ~1 400 mots. **Point de vue** : narrateur omniscient (avec une
adresse directe au lecteur, « Let us take a look at the home in which she lives »).
**Aucun paragraphe n'est reproduit ici (R-2).** Résumé narratif détaillé ci-dessous.

**Résumé fidèle — Part 1**
Della a compté trois fois son argent : **un dollar et quatre-vingt-sept cents**, dont soixante cents
en pièces d'un cent, économisées une à une. Le lendemain est Noël, et elle pleure. Le foyer : un
**petit appartement meublé à huit dollars la semaine**, où tout signale la pauvreté ; le ménage vit
sur **vingt dollars par semaine** et les dépenses ont toujours dépassé les prévisions. Della veut un
cadeau pour **Jim**, son mari, digne de lui. Devant l'étroit miroir entre les fenêtres, elle dénoue
ses cheveux : le couple possède **deux trésors** — la **montre en or de Jim**, héritée de son père et
de son grand-père, et la **chevelure de Della**, qui lui descend sous les genoux. Elle met son vieux
manteau brun et son vieux chapeau brun, descend dans la rue et s'arrête devant une enseigne :
« **Madame Sofronio, Hair Goods of All Kinds** ». Della monte au deuxième étage et demande si on lui
achète ses cheveux. Madame Sofronio les soupèse et offre **vingt dollars** ; Della accepte
immédiatement. Elle passe deux heures à courir les magasins et finit par trouver **une chaîne de
montre en platine**, sobre et de qualité, « digne de la Montre » — **vingt-et-un dollars**. Elle
rentre avec les **quatre-vingt-sept cents** restants.

**Résumé fidèle — Part 2**
De retour, Della recoiffe ses cheveux très courts au fer à friser et se juge sévèrement dans le
miroir : elle craint que Jim la trouve « comme une enfant ». À sept heures, le café est prêt et le
dîner presque fait. Jim, ponctuel, entre : mince, grave, **vingt-deux ans**, il aurait besoin d'un
manteau neuf et n'a pas de gants. Il fixe Della d'un regard indéchiffrable qui l'effraie. Della se
jette vers lui, explique qu'elle a coupé et vendu ses cheveux pour lui offrir un cadeau, que ses
cheveux repousseront vite, et le supplie de lui souhaiter « Merry Christmas ». Jim, comme incapable
de comprendre, répète qu'elle a coupé ses cheveux, cherche du regard dans la pièce — puis semble
soudain se réveiller, l'embrasse, sort un paquet de sa poche et le jette sur la table en lui disant
que rien ne pourrait jamais lui faire moins l'aimer. Della défait le paquet : ce sont **les peignes**
— le jeu complet, de côté et de derrière — qu'elle admirait depuis longtemps dans une vitrine de
**Broadway**, exactement de la teinte de ses cheveux… désormais disparus. Cri de joie, puis larmes,
puis sourire : « mes cheveux poussent si vite ». Elle tend alors à Jim son propre cadeau, la chaîne,
et lui demande sa montre pour voir l'effet. **Chute** : au lieu d'obéir, Jim s'allonge sur le divan,
les mains sous la nuque, et sourit.

**Le dernier paragraphe est réservé au professeur (guide p.19)** : « This is the last paragraph of the
story. **Read it to the students after dealing with question G.** » — son contenu (non reproduit,
R-2) : Jim propose de ranger les cadeaux et de les garder intacts, trop beaux pour servir maintenant,
puis **révèle qu'il a vendu sa montre pour acheter les peignes**, et demande à Della de préparer le
dîner.

**Encadré biographique (manuel p.33, verbatim — paratexte du manuel)** :

> **William Henry Porter (1862-1910)** — He is better known by his pen name, O. Henry. He grew up in
> North Carolina…. He moved to New York City, where he became famous as a short-story writer. His
> stories are known for their insight into the lives of ordinary people and for their surprising
> endings.

_(⚠️ Le vrai nom d'O. Henry est **William Sydney Porter** — le manuel imprime « William Henry
Porter » ; voir Incertitudes.)_

**Thème (guide p.18, Helpful notes, verbatim)** : « Theme of the story : **mutual self-sacrifice
between husband and wife is a fundamental value in family life / unselfish love shared, regardless of
the attendant difficulties.** »

###### Questions sur la nouvelle (manuel p.33-34)

**A.** « Read the whole text and check your prediction. »

**B.** « Complete the following table with information from the story. »

| Characters | Setting              | Point of view |
| ---------- | -------------------- | ------------- |
| ……         | Place : …… Time : …… | ……            |

_(Pas de corrigé au guide. Éléments attestés dans le texte : Della, Jim, Madame Sofronio ; lieu = un
petit appartement meublé, la ville — magasins et Broadway ; temps = la veille de Noël, sept heures du
soir ; point de vue = narrateur omniscient.)_

**C.** « Della and Jim offered each other a present. 1. What was Della's present to Jim ?
2. What was Jim's present to Della ? »

**D.** « These sentences relate to what happened in the story. Number them in the correct order. » —
7 phrases (rédigées par le manuel, verbatim) :

- --- Jim bought Della the set of combs she had admired for a long time.
- --- They lived in a very poor apartment.
- --- Jim felt so disappointed because Della's hair was gone.
- --- She bought a platinum watch chain for Jim.
- --- She wanted to buy a present for her husband.
- --- Della and Jim didn't have enough money.
- --- She sold her beautiful long hair.

**Corrigé (guide p.18)** : « As you read. D. **6, 2, 7, 5, 3, 1, 4** » — soit l'ordre : (1) They lived
in a very poor apartment · (2) Della and Jim didn't have enough money · (3) She wanted to buy a
present for her husband · (4) She sold her beautiful long hair · (5) She bought a platinum watch chain
for Jim · (6) Jim bought Della the set of combs · (7) Jim felt so disappointed because Della's hair
was gone.

**E.** « “…a gray cat walking along a gray fence in a gray backyard.” **Why is the adjective “gray”
repeated three times ?** » _(seule citation littérale conservée de la nouvelle : elle **est** l'énoncé
de l'exercice et porte la notion enseignée — la répétition comme procédé.)_

**F.** « Read and pick out expressions from the text showing **Della's inner struggle**. »

**G.** « How do you think Jim managed to buy his wife the set of combs ? » _(→ c'est après cette
question que le guide fait lire le dernier paragraphe.)_

**H.** « What do you think of the **denouement** of the story ? »

**I.** « What is the **theme** in this short story ? »

###### AFTER YOU READ — Writing activity (manuel p.34)

« Join a group in your class to work on the **summary of the story**. (Question D might help you) The
following strategies will also help you summarize the story. » — verbatim :

1. Read the story carefully.
2. Identify the controlling idea and the relationships among the supporting ideas.
3. Decide which examples are necessary for a clear understanding of the story.
4. Avoid making comments or adding information to the story.
5. **Make the summary one-fourth the length of the original text.**

##### Arts · Section Two : READING ABOUT A VITAL ISSUE (manuel p.35-38 · guide p.20)

###### Scope and sequence (guide p.20, verbatim)

**Skills/sub-skills and strategies**

- _Reading_
  - match dictionary choices with context at hand
  - skim for gist
  - scan for details
  - guess the meaning of unfamiliar words through context
  - differentiate between relevant and irrelevant information
  - infer the writer's opinion
- _Speaking_
  - produce physical description

**Vocabulary** (guide) : depression - irritable - aging - withdraw(al) - annoyance - **senior** - seek
- bereaved - elderly - recurrence - relapse. _(11 items seulement — la liste de fin de module en
compte 25 pour cette section ; voir Incertitudes.)_

**Grammar** : **Word-building (affixation)**.

**Functions** : describing people · making statements about a concrete situation · expressing opinion.

**Note du guide (p.20, verbatim)** : « The pictures may be exploited and used before the questions to
make students talk about the relationship of grand-parents with their grand-children and talk about
themselves and their own relationship with their grand-parents. The questions in the first activity
are meant to sensitize students to the importance of the family for old people. »

###### BEFORE YOU READ (manuel p.35)

**A.** « Ask each other the following questions » :

- Do your grandparents live with you ?
- If yes, do you like having them with you ?
- If no, would you like them to live with you ? Why ? Or why not ?

**B.** « What are the benefits or inconveniencies [sic] of living with or next to your grand-parents ? »

###### AS YOU READ — A. L'entrée de dictionnaire (manuel p.35)

« Read the text and the dictionary entry and **choose the appropriate meaning for the word
“depression”. Justify your choice with details from the text.** » — entrée verbatim (10 sens) :

> **De-pres-sion** (de presh'_n, di-) n. **1.** a depressing or being depressed **2.** a depressed part
> or place ; hollow or low place on a surface **3.** low spirits ; gloominess ; dejection ; sadness
> **4.** a decrease in force, activity, amount, etc. **5.** _Astron._ the angular distance of a
> celestial body below the horizon. **6.** _Econ._ A period marked by slackening of business activity,
> widespread unemployment, falling prices and wages, etc. **7.** _Med._ a decrease in functional
> activity **8.** _Meteorol._ a) a lowering of the atmospheric pressure indicated by the fall of
> mercury in a barometer b) an area of relatively low barometric pressure ; low **9.** _Psychol._ an
> emotional condition, either neurotic or psychotic, characterized by feelings of hopelessness,
> inadequacy etc. **10.** _Surveying_ the angular distance of an object below the horizontal plane –
> **the (Great) Depression** the period of economic depression which began in 1929 and lasted through
> most of the 1930's.

_(Réponse attendue, non imprimée : le sens **9, Psychol.** — l'article traite d'une maladie
émotionnelle diagnostiquée et traitée.)_

###### Le texte support (manuel p.36)

**Titre** : « **Depression In Elderly Is Treatable** ». **Source imprimée** : « Adapted from **Vital
Issues** · Author : **James Gaffney** · **Utah Spirit magazine, July 2001** ». **Genre** : article de
presse / texte expositif (non littéraire). **Longueur** : ~430 mots, **6 paragraphes numérotés**.

**Résumé fidèle, § par §** (avec les données chiffrées et les termes que les exercices exploitent) :

1. **Bob** remarque que sa mère de **73 ans** n'est plus elle-même : elle ne dort pas de la nuit, est
   souvent **irritable** le jour, ne veut plus jouer à son **bridge hebdomadaire**, ne s'intéresse
   guère à ses habitudes ; « her **temper** is short », de petites contrariétés (« small **annoyances**
   ») la font sortir de ses gonds.
2. Interrogée, elle assure à Bob qu'elle va bien, « juste un peu à plat ». Bob se demande si c'est
   normal pour une personne âgée. **Ce n'est pas normal**, selon des recherches soutenues par le
   **National Institute of Mental Health** : sa mère présente les signes d'une **dépression**, maladie
   fréquente chez les adultes âgés.
3. La dépression **n'est pas une part normale du vieillissement**, disent les experts. Citation de
   l'article : quand une personne âgée ne se sent plus engagée, cesse d'apprécier la vie et ne peut
   plus assurer ses activités habituelles, le problème a dépassé la normale, on va vers un
   **diagnostic de dépression clinique** et il est temps de consulter.
4. **Signaux d'alerte** que la famille et les amis doivent repérer : troubles du sommeil chroniques et
   incapacité à se reposer, inquiétude excessive, désintérêt, retrait des amis et/ou des activités
   normales, plaintes de douleurs chroniques non attribuables à d'autres troubles.
5. La famille est **déterminante** pour amener les aînés au traitement, car ceux-ci ne reconnaissent
   souvent pas leur dépression. **Entre 20 et 25 pour cent** des personnes âgées hospitalisées sont
   dépressives, et **une sur trois** vivant en **maison de retraite** peut en souffrir. Il faut donc
   chercher là où sont les personnes âgées (les lieux de soin) ; familles et aidants doivent être
   particulièrement vigilants et **rechercher (seeking)** une intervention précoce qui évite une
   dépression déclarée. Sont particulièrement susceptibles les adultes âgés **récemment endeuillés
   (bereaved)**.
6. **Les étapes** à retenir, pour les aînés comme pour leurs proches (liste à puces, verbatim) :
   • Recognize that depression is not a normal part of aging and take symptoms seriously.
   • Seek information from individuals and organizations experienced in helping older adults.
   • Mobilize social support from relatives and friends.
   • Most importantly, get treated properly.
   Clôture : un traitement au long cours peut être nécessaire pour prévenir rechute (**relapse**) ou
   récidive (**recurrence**) — « Getting treated is only the first step. **Staying well is the
   challenge.** »

###### Exercices sur le texte (manuel p.37-38)

**B.** « Go through the list of the symptoms and put a tick (√) next to the ones that are **not**
mentioned in the text. » — 9 items : • insomnia ( ) • aches ( ) • **loss of appetite** ( ) •
**fatigue** ( ) • lack of enjoyment ( ) • worry ( ) • loss of weight ( ) • anger ( ) • disinterest ( )
**Corrigé (guide p.20)** : « B. **loss of appetite / fatigue** ». ⚠️ « loss of weight » n'est pas
davantage mentionné dans le texte — voir Incertitudes.

**C.** « Find words in the text that mean : »

- angry (§1)
- becoming angry quickly (§1)
- older (§2)
- looking for (§5)
- deprived by death of a loved one (§5)

_**Corrigé absent du guide.** Mots effectivement présents dans le texte aux paragraphes indiqués :
§1 — **irritable**, « her temper is short » / « small annoyances **set her off** » ; §2 — **senior
(citizen)** / **older (adults)** ; §5 — **seeking** ; §5 — **bereaved**._

**D.** « Are the following statements true or false ? Write **T** or **F** in the box provided and
**justify your answers**. »

1. Bob's mother didn't recognize that she had depression. ☐
2. Most of the older people who suffer from depression live in their families. ☐

_(Pas de corrigé au guide.)_

**E.** « Read and **cross out the wrong alternative**. » — amorce : « According to experts, the role of
the family is very important for the people who suffer from depression because their relatives
should : »

1. look for the symptoms and seek the treatment
2. avoid long-term treatment
3. support the patient

_(Pas de corrigé au guide. Le § 6 du texte contredit explicitement l'alternative 2.)_

**F.** « Does the writer give his opinion about the issue ? Justify your answer. » _(Pas de corrigé.)_

**G.** « Look at the pictures of the three old women. Which picture best depicts the woman in the
text ? Justify your choice and describe the woman to your partner. » — **3 images** numérotées 1, 2, 3.
**Useful vocabulary (verbatim)** : seem, look, tired, pessimistic, depressed, lonely, face, optimistic,
worried, eyes, frightened, happy, sad …
**Corrigé (guide p.20, verbatim)** : « G. It's clear that the correct answer is that **picture 2**
depicts the lady in the text, but what matters is the justification given and the use of the
appropriate vocabulary. »

**H.** « Complete the chart with words from the text. (No.1 has been done for you.) » — tableau
**Part of speech | Prefix or suffix | Related word | Word form**, amorces imprimées au manuel p.38 :

| (mot)     | Part of speech | Prefix or suffix | Related word | Word form |
| --------- | -------------- | ---------------- | ------------ | --------- |
| treat     | verb           | able             | treatable    | adjective |
| treat     | verb           | ……               | ……           | noun      |
| depress   | ……             | ……               | ……           | noun      |
| ill       | ……             | ness             | ……           | ……        |
| annoy     | ……             | ……               | annoyance    | ……        |
| interest  | noun           | ……               | ……           | ……        |
| ability   | ……             | in               | ……           | ……        |

**Corrigé complet (guide p.20, verbatim)** :

| (mot)    | Part of speech | Prefix or suffix | Related word | Word form |
| -------- | -------------- | ---------------- | ------------ | --------- |
| treat    | verb           | able             | treatable    | adjective |
| treat    | verb           | ment             | treatment    | noun      |
| depress  | verb           | ion              | depression   | noun      |
| ill      | adjective      | ness             | illness      | noun      |
| annoy    | verb           | ance             | annoyance    | noun      |
| interest | noun           | dis              | disinterest  | noun      |
| ability  | noun           | in               | inability    | noun      |

---

#### Fin de module (manuel p.39-41)

##### SELF-ASSESSMENT (manuel p.39)

**A.** « What progress do you feel you have made in English in this module ? Put a tick (√) in the box
that applies to you. » — 14 énoncés × 3 colonnes **YES | A LITTLE | NO** :

1. I've used what I already know to learn more English
2. I can read a text and answer the questions correctly
3. I can listen to a text and answer the questions correctly
4. I've learnt how to converse in English
5. I am using the grammatical structures I've learnt
6. I understand grammar but I cannot use the structures correctly
7. I can remember the words I've come across
8. I recognize the words but I cannot use them
9. I've learnt how to write in English
10. The writing activities are difficult
11. I've shared ideas with my classmates and my teacher
12. My pronunciation has improved
13. I've learnt how to conduct a mini-project
14. My English has improved

**B.** « What did you like most in this module ? Tick the answer(s) that apply(ies) to you. » —
10 items : The topics · The activities · The projects · Listening to the cassette · Acting out
situations · The writing activities · The Reading skills · The grammar exercises · The vocabulary
exercises · Working in groups.

**C.** « Circle the alternative that applies to you : **I still need to work on :**
Reading / Listening / Speaking / Writing / Vocabulary / Grammar »

##### Fun page (manuel p.40)

Trois brèves, séparées par un motif de trois points. Résumé fidèle (avec les chutes, qui sont l'objet
même du texte) :

1. **Le collier de perles** — au réveil, une femme raconte à son mari qu'elle a rêvé qu'il lui offrait
   un collier de perles pour la Saint-Valentin, et lui demande ce que cela signifie. « **You'll know
   tonight** », répond-il. Le soir, il rentre avec un petit paquet ; ravie, elle l'ouvre — et y trouve
   un livre intitulé « **The Meaning of Dreams** ».
2. **Aphorisme** (verbatim) : « Happiness is having a large, loving, caring, closely-knit family **in
   another city**. »
3. **Les cookies** — un vieil homme est sur son lit de mort, il ne lui reste que quelques heures,
   quand il sent une odeur de cookies aux pépites de chocolat, ce qu'il aime plus que tout au monde.
   Dans un dernier effort il sort du lit, se traîne jusqu'à l'escalier, le descend et gagne la cuisine
   où sa femme fait cuire les cookies. Comme il tend la main vers l'un d'eux, elle lui claque le dos
   de la main avec une cuillère : « **Leave them alone, they are for the funeral !** »

##### VOCABULARY COVERED IN MODULE 1 (manuel p.41, liste intégrale)

_Mise en page d'origine : quatre colonnes ; restituée ici par rubrique. Total : **133 items** — 81 en
tronc commun, 52 dans le supplément Arts._

**Common core:**

**Section one:** (20)
affective · career path · comfort · establish · functioning · handle · hoover (v) · instrumental ·
leadership · maintenance · management · nurture · reassurance · resource · shelter · skill · standard ·
trash · warmth · water (v)

**Section two:** (16)
assignment · cherish · curl · error · fulfil · gaze · laughter · make a decision · many a (+ n) ·
overburdened · set (a table) · share roles · store · task · tear · trial

**Section three:** (28)
alone · barge · blow · date sb · depressed · dry (v) · dust (v) · edge · end up · exert · expectations ·
feed · feel like · frustrated · guess · heart-broken · misconduct · openly · overwhelmed · parenting ·
pressure · puppet · push · sloppy · sympathize · thought · turn out · well-mannered

**Section four:** (10)
blame · bother · can't help it · chores · demanding · exhausted · for heaven's sake · lazy · messy ·
upset

**Section five:** (7)
accomplishment · deal · fit in with sb's taste · intend · pride · scold · value (v)

**Arts Supplement:**

**Section one:** (27)
powder · apartment · cascade · character · climax · comb · conflict · critically · denouement ·
expense · fellow · foolishness · hunt · intensity · moral · plot · point of view · poverty · setting ·
sign · step in · struggle · suspense · theme · turn white · undo · worthy of

**Section two:** (25)
aging · annoyance · attribute · bereave · chronic · depression · diagnosis · elderly · excessive ·
full-blown · insomnia · irritable · long-term · mobilize · nursing · recurrence · relapse · routine ·
seek · set off · susceptible · symptoms · temper · vigilant · withdrawal

---

#### Tapescripts du module

_(guide p.76-77 — « Tapescript · Module one »)_

Le guide publie trois pistes pour ce module. **Deux d'entre elles sont des œuvres sous droits et ne
sont pas reproduites ici (R-2)** ; les deux dialogues fonctionnels, écrits par les auteurs du manuel,
le sont intégralement.

##### Piste 1 — Le poème (Section Two) — guide p.76 · ⚠️ non reproduit (R-2)

**Auteur** : Paula S. Dickinson. **Forme** : 16 vers, rimes plates, dialogue fils→père puis réponse du
père. **Contenu** : le fils demande ce qu'est « une famille » et si cela se réduit aux personnes qui
la composent ; le père répond que c'est « bien plus que cela » et énumère : les boucles de la petite
Sue et le chapeau neuf de la mère ; le visage de Jackie découvrant qu'elle est **capable** d'aider à
**mettre** la table ; les premiers dessins qu'on **range** pour les **chérir** et les contempler un
jour futur ; le regard **perdu** de la mère au premier jour d'école ; **apprendre** à vivre selon la
« Golden Rule » ; les **histoires** au coin du feu, bien des soirs ; le sentiment que tout va bien ;
les essais et les erreurs, les **rires** et les larmes qui nous touchent tous, au fil des **années**.
Conclusion : c'est tout cela qui fait une famille.
_(Les mots en gras sont exactement ceux qui manquent dans la version à trous du manuel p.18 —
cf. Section Two, activité F.)_

##### Piste 2 — « Dialogue 1 » (Section Four, Activity 1) — guide p.76, verbatim

> Children ! Would you please stop making so much noise ! And for heaven's sake, pick up your clothes
> and toys ! It's hard enough trying to keep this house clean without your throwing your things all
> over the place !
>
> Clara, I know that the children **get in your hair**, but you should try not to let it upset you so
> much.
>
> Listen, Jim. I can't help it. The children **bother me and make me very angry** when they're so
> noisy and messy.

_(Locuteurs non nommés dans le tapescript ; le manuel p.25 les attribue à **Clara**, **Jim**, **Clara**.)_

##### Piste 3 — « Dialogue 2 » (Section Five, Activity 1) — guide p.76, verbatim

> - That's it, Greg ! You'd better not come in after midnight again tonight !
> - I know, dad. You don't have to jump down my throat ! I told you that
> - I'd make it home around 11:30. I don't intend to be late !
> - Well, you've said that before and in you come at 2:30 in the morning.
> - You can't blame me for getting angry and scolding you. I've good reason.

_(Répartition attestée par le contenu : lignes 1, 4 et 5 = **le père** ; lignes 2 et 3 = **Greg** —
la ligne 3 est la suite de la réplique de Greg, coupée par un retour à la ligne. Voir Incertitudes.)_

##### Piste 4 — La chanson « Father and Son » — guide p.77 · ⚠️ non reproduite (R-2)

**Auteur/interprète** : Cat Stevens. **Structure** : Father (7 lignes) / Father (5 lignes, suite) /
Son (5 lignes) / Father (7 lignes, reprise variée de la 1ʳᵉ strophe) / Son (5 lignes).
**Contenu** : le père répète que ce n'est pas le moment de changer, invite au calme et à la lenteur,
rappelle au fils qu'il est jeune (« that's your fault »), qu'il lui reste beaucoup à apprendre et à
traverser, lui conseille de trouver une compagne, de se poser, de se marier s'il le souhaite, et se
donne en exemple : vieux mais heureux ; il dit avoir été à sa place, sait que ce n'est pas facile,
conseille de prendre son temps et de penser à tout ce qu'on a, car demain sera encore là mais peut-être
pas les rêves. Le fils répond qu'il n'arrive pas à s'expliquer, que dès qu'il essaie l'autre se
détourne, que c'est toujours la même vieille histoire, qu'on lui a ordonné d'écouter depuis qu'il sait
parler ; il a beaucoup pleuré en gardant tout pour lui, il lui est plus dur encore d'ignorer ce qu'il
ressent, il agréerait s'ils avaient raison mais c'est eux, pas lui, qu'ils connaissent ; il y a
désormais une voie et il sait qu'il doit partir.
**Corrigé du gap-fill du manuel p.27** : voir le tableau des 16 mots en Section Four, « Time for a song ».

---

#### Incertitudes (module 1)

**Passages illisibles ou ambigus dans la source**

1. **Manuel p.18, activité F** — un blanc parasite apparaît en bout de la ligne sur les boucles de la
   petite Sue : « …………………… the table. » Il double le blanc « in ………… the table » de la ligne suivante
   et **n'a pas de place dans la métrique du poème**. Il s'agit très probablement d'un artefact de la
   couche-texte (fragment de la ligne suivante ou d'un encart réinjecté par `pdftotext -layout`), non
   d'un onzième blanc réel. `[?]` — à revérifier sur la page imprimée si un doute subsiste.
2. **Manuel p.19, H.2** — l'exercice porte sur « the **underlined** sounds » des paires
   _future/cherish_, _laughter/family_, _meant/learn_ : **le soulignement n'est pas restitué par la
   couche-texte**, donc les lettres exactes visées ne sont pas connues avec certitude. `[?]`
3. **Manuel p.13, 17, 30, 38** — les images (8 photos de rôles, 6 vignettes du poème, illustrations de
   la nouvelle, 3 portraits de femmes âgées) **ne sont pas décrites par le texte imprimé** ; leur
   contenu n'est reconstituable que par les corrigés. `[?]`
4. **Guide p.76, Dialogue 2** — les tirets et retours à la ligne ne distinguent pas les locuteurs :
   la 3ᵉ ligne (« I'd make it home around 11:30… ») est typographiquement isolée alors qu'elle
   continue la réplique de Greg. Attribution reconstituée par le sens, non imprimée. `[?]`
5. **Manuel p.28, Activity 1** — le tableau demande le **« place »** du dialogue, mais **le tapescript
   ne nomme aucun lieu** (il se déduit seulement : le domicile familial). `[?]`
6. **Manuel p.28** — l'étiquette « **Activity 2** » est imprimée **avant** le titre de rubrique « AS
   YOU WRITE » et n'est suivie d'aucun énoncé propre : le contenu qui suit (lettre de Mike + 5
   questions + processus d'écriture) constitue de fait l'Activity 2. Ordre des étiquettes possiblement
   inversé à la composition. `[?]`

**Divergences guide ↔ manuel**

7. **Vocabulaire Section five** — le manuel p.41 liste **7** items (accomplishment, deal, fit in with
   sb's taste, intend, **pride**, scold, value) ; le guide p.17 n'en liste que **6** : **« pride » est
   absent du guide**.
8. **Vocabulaire Arts Section two** — le manuel p.41 liste **25** items ; le guide p.20 n'en liste que
   **11**, et y ajoute **« senior »**, qui **ne figure pas** dans la liste du manuel. Inversement,
   14 items du manuel (attribute, chronic, diagnosis, excessive, full-blown, insomnia, long-term,
   mobilize, nursing, routine, set off, susceptible, symptoms, temper, vigilant) sont absents du guide.
9. **Forme du lemme « date »** — manuel p.41 : « **date sb** » ; guide p.13 : « **date (v)** ».
   Même item, deux notations.
10. **Corrigé B (Arts, section two)** — le guide p.20 ne donne que **« loss of appetite / fatigue »**
    comme symptômes non mentionnés, mais **« loss of weight » n'est pas davantage mentionné** dans le
    texte de la p.36. Le corrigé imprimé est donc **incomplet** : la réponse attendue devrait compter
    trois items.
11. **Rubrique « Mini-project »** — l'item 13 de l'auto-évaluation (manuel p.39) demande à l'élève
    « I've learnt how to conduct a mini-project », et l'item B propose « The projects » ; **aucun
    mini-projet n'est pourtant imprimé dans le module 1** (manuel p.12-41) ni décrit dans le guide
    p.9-20. Même remarque pour « Listening to the cassette » — la cassette n'est pas au corpus.
12. **Frontière tronc commun / Arts** — le book map annonce que « the items in pink are specific to
    the Arts branch », mais **la couleur n'est pas restituée par la couche-texte**. La frontière
    retenue ici (tronc commun = p.12-28, Arts = p.29-38) s'appuie sur le **bandeau « Arts »** imprimé
    en tête des pages 29 à 38, et sur l'ordre du guide (Sections One→Five p.10-17, puis « Arts.
    Section One » p.18 et « Arts. Section Two » p.20). La page « Time for a song » (p.27) **ne porte
    pas** le bandeau Arts et est donc rattachée au tronc commun. `[?]`

**Coquilles de la source**

13. **Manuel p.33** — l'encadré biographique imprime « **William Henry Porter (1862-1910)** » [sic] ;
    le vrai nom d'O. Henry est **William Sydney Porter**. Erreur de la source, transcrite telle quelle.
14. **Manuel p.33** — dans la nouvelle : « the hair in which she was to wear them **has** gone » [sic]
    — concordance fautive (attendu : _had gone_).
15. **Guide p.14** — « See eye to eye (with) : agree entirely (with), have **incidental** views » [sic]
    — lire vraisemblablement _identical views_.
16. **Manuel p.22, Activity 2** — « My parents rarely let me stay out after midnight » [sic] : point
    final manquant.
17. **Manuel p.35, B** — « benefits or **inconveniencies** » [sic] (forme non standard pour
    _inconveniences_).
18. **Guide p.17** — « Ask the students **few** comprehension questions » [sic] (attendu : _a few_).
19. **Orthographe mixte britannique/américaine** dans le manuel : « neighbors » et « behavioral »
    (p.14, US) coexistent avec « behaviour » (p.14), « unorganised » (p.21), « fulfil » (p.41) et
    « Analyse » (p.23) — la source ne normalise pas.
20. **Manuel p.17** — « check your answers with your **classmate's** » : possessif elliptique employé
    de façon récurrente (p.17, p.24, p.25, p.28, p.30) ; transcrit tel quel.

**Corrigés absents du guide** (à ne pas confondre avec une omission de transcription) : Section One
Activity 2 C (tableau instrumental/affectif) et Activity 3 ; Section Two A, E, H.2, After you listen ;
Section Three Before you read, As you read questions 1-2 et 4-6, Exploring grammar Activities 1-2,
After you read, Exercises 1 (au-delà de l'item 1), 2, 3 et 4 ; Section Four en entier ; Section Five
en entier (y compris le tableau speakers/place/problem) ; Arts Section One B, C, E, F, G, H, I et
Writing activity ; Arts Section Two A (choix du sens de « depression »), C, D, E, F.

### Module Two — WE LEARN TO GIVE, SHARE AND CARE (manuel p.42-73 · guide p.21-33)

> Manuel élève 241303 « Activate and Perform — Third Year Secondary Education, Student's Book » ·
> Guide enseignant 641303 « Activate and Perform — Teacher's Book ».
> **Frontière filière** : les sections *Section One* → *Section Five* (manuel p.43-62, guide p.22-30)
> sont le **tronc commun**, servi par les six sections de 3ème année. Les pages **« Arts »**
> (manuel p.63-70, guide p.31-33) sont le **supplément spécifique à la filière Lettres**
> (« The items in pink are specific to the Arts branch »). Les rubriques de fin (Fun page,
> vocabulaire, self-assessment) sont communes.
>
> **Droits d'auteur (R-2)** : trois œuvres sous droits figurent dans ce module — la chanson
> *Ebony and Ivory* (Paul McCartney / Stevie Wonder), le poème *Catch the fire* (Sonia Sanchez)
> et le poème d'Emily Dickinson de la section two. **Aucun vers, aucune strophe, aucune parole
> n'est recopié ici** : seuls titre, auteur, genre, structure, thème, notions de langue et
> questions posées sont transcrits. Les textes non littéraires (discours de Hope Organization,
> article du magazine *Woman*, biographie de Helen Keller, annonce radio, chronologie
> Martin Luther King) sont, eux, restitués fidèlement.

---

## Chapeau du module

**Titre** : Module Two — WE LEARN TO GIVE, SHARE AND CARE (manuel p.42 · guide p.21, imprimé
« ModuleTwo : » [sic])

**Topic** (guide p.21) : Attitudes and values / Philanthropy

**Subtopics** (guide p.21) : charity, altruism, activism, self-sacrifice, volunteerism,
solidarity, generosity, great people

**Cross-curricular learning goals** (guide p.21) : problem solving, critical thinking, efficient
use of data, efficient working procedure, appropriate self-expression, ICT use, project work,
communicating, working and living with others.

**Expected learning outcomes** (manuel p.42) — verbatim, « In this module, I'm going to » :
- use what I already know to acquire new words and ideas about philanthropy
- listen to a speech
- read about a family case in a magazine
- read an ad
- read a poem
- read a poem *(l'entrée « read a poem » est imprimée deux fois — voir Incertitudes)*
- read a biographical text
- give a speech
- learn and practise lexical and grammatical items
- write a letter to a magazine
- write a biography from notes
- write a poem
- expand a quote into an article
- conduct a mini-project
- expand my knowledge of the world

**Grammaire du module** (agrégée des cinq sections, guide p.22-30) :
- word formation : noms d'agent en `-er / -or / -ist` (section one)
- emphatic form (forme emphatique) + compound adjectives (section two)
- phrasal verbs · `should have + past participle` · present perfect vs simple past (section three)
- consolidation des discourse markers / expressions de division du texte (section five)

**Pronunciation** :
- section two (guide p.24, imprimé « Pronuncition » [sic]) : traiter les *dysfluency features*
  (pause en fin de *thought group*) ; reconnaître les schémas de rythme et d'intonation d'un discours
- Arts section one (guide p.31) : prononcer correctement au niveau du mot, de la phrase et du
  discours ; réciter un poème de manière expressive

**Project work / Homework** :
- Mini-project (manuel p.46, Activity 4, guide p.22) : recherche Internet sur une ONG/fondation
  ou un philanthrope → rapport court → présentation en fin de module → portfolio
- Homework section two (manuel p.49) : remettre en ordre une annonce de service public
- Homework section three (manuel p.55) : texte à trous + recherche web sur le syndrome
  Dyggve-Melchior-clausen
- Homework section one (guide p.22) : doing internet research

---

## Section One : Introductory activities

*(manuel p.43-46 · guide p.22-23)*

#### Scope and sequence (guide p.22)

| Rubrique | Contenu imprimé |
| --- | --- |
| **Skills/subskills and strategies** | **Reading** : identify the communicative value of texts (pictures, quotes) · build on prior knowledge to further and enhance learning · acquire knowledge about a given topic. **Speaking** : express opinion about a specific issue. **Writing** : write in pairs to solve a problem |
| **Vocabulary** | activism, advancement, altruism, benevolence, charity, common good, contribution, devotion, donation, egoism, endowment, fund-raising, generosity, helpless, humanitarian, in-kind (adj), meanness, needy, philanthropy, raise money, self-sacrifice, solicit, solidarity, voluntarism, volunteerism, welfare |
| **Grammar** | word formation : (n/v + er, or, ist) |
| **Functions** | describing pictures · expressing opinion · reporting information |
| **Homework** | doing internet research |
| **Mini-project** | conducting project work |

#### Helpful notes (guide p.22-23)

- « In addition to the vocabulary presented, familiarise the students with "benevolence" and
  "in-kind" (adj) » — **in-kind contributions** : *goods, commodities or services instead of money*.
- Have the students identify the communicative values of the pictures and the quotes.
- **Activity 1** : chaque élève répond aux questions individuellement, compare ses réponses en
  petits groupes, puis partage avec la classe.
- **Activity 2** : A en petits groupes ; B encourager le travail en binôme.
- **Activity 3 — le contexte tunisien** (liste du guide, à faire produire par les élèves) :
  - National Solidarity Day : **Dec 8** (8 décembre)
  - donating blood : **National Blood Donation Day : April 8** (8 avril) / en cas d'accidents de la
    route / une personne (voisin, parent…) subissant une opération chirurgicale et ayant besoin de sang
  - **Ramadhan** : offrir de la nourriture aux pauvres / nécessiteux
  - décès d'un parent / d'un voisin
  - mariage d'un parent / d'un voisin
  - hiver rigoureux (don de nourriture, vêtements, couvertures…)
  - catastrophes naturelles (inondations, incendie, séisme…)
  - rentrée scolaire (don de livres utiles, CD, cartables, etc.)
  - contributions en nature aux centres pour personnes âgées (vêtements, nourriture, médicaments…)
  - aide / contributions en nature aux personnes handicapées
  - don d'argent ou de matériaux de construction pour bâtir des mosquées

#### Activity 1 (manuel p.43-44)

**A.** « Look at the pictures and study the quotes then answer the questions below. »

**Les citations affichées** (manuel p.43) :
- **Picture 1** — « It is much better to give than to receive »
- « We believe philanthropy is a personal journey. We believe that charity lies within each of
  us – in our hearts, in our heads, in our spirits. »
- « Life, like a mirror, never gives back more than we put into it. »
- **Picture 2** — « The point is not to pay back kindness but to pass it on. »

**Les questions** (manuel p.44) :
1. Do you agree that it is much better to give than to receive ? why ? or why not ? *(minuscules [sic])*
2. What is the message conveyed through picture No.1 ?
3. How can we pass kindness on ?
4. Where are the old lady and Meriam ? Guess what Meriam is offering to the old lady.
5. Guess what is meant by philanthropy.

**B.** « Compare your answers with those of your classmates'. »

*Note* : la question 4 révèle le contenu de la photo n°1 — une vieille dame et une jeune fille
nommée **Meriam** qui lui offre quelque chose (image non présente dans la couche texte).

#### Activity 2 (manuel p.44-45)

**A.** « Read the definitions below and complete the unfinished words in the spidergram. Each
dot ( . ) stands for a letter. »

**Les 10 définitions, verbatim :**
1. The principle or practice of unselfish concern for or devotion to the welfare of others
   (opposed to egoism)
2. The doctrine or practice of vigorous action or involvement as a means of achieving.
3. The policy or practice of volunteering one's time or talents for charitable, educational, or
   other worthwhile activities, especially in one's community.
4. Generous actions or donations to aid the poor, ill or helpless.
5. An act or instance of presenting something as a gift, grant, or contribution.
6. Sacrifice of one's interests, desires, etc., as for duty or the good of another.
7. Readiness or liberality in giving. (opposite to meanness)
8. Union or fellowship arising from common responsibilities and interests, as between members of
   a group or between classes, peoples, etc.
9. The act of providing with a permanent fund or source of income.
10. The act or process of soliciting contributions / raising money.

**Le spidergram** (centre : **philanthropy**) — amorces imprimées telles quelles :

| N° | Amorce imprimée | Réponse (guide p.23) |
| --- | --- | --- |
| 1 | `altruism` (déjà donné) | altruism |
| 2 | `activism` (déjà donné) | activism |
| 3 | `vol . . t . . ri . m = voluntarism` | volunteerism / voluntarism |
| 4 | `ch . . . ty` | charity |
| 5 | `don . t . . .` | donation |
| 6 | `self – s . . r . f . . e` | self-sacrifice |
| 7 | `gen . . . . . ty` | generosity |
| 8 | `so . . da . . . y` | solidarity |
| 9 | `end . w . . . t` | endowment |
| 10 | `fund-ra. si . .` | fund-raising |

**B. Pair work** — « Student A. Read a definition. / Student B. Provide the word. »

**C.** « Use the following suffixes ( -or, -er, -ist ) to complete the words in the table. »
Structure du tableau : colonne de gauche **« The person who »** + la définition ; colonne de droite
**« is »** + le mot à compléter.

| N° | The person who… | …is | Réponse (guide p.23) |
| --- | --- | --- | --- |
| 1 | gives or donates | a don……. | donor |
| 2 | practises philanthropy | a philanthrop……. | philanthropist |
| 3 | endows an institution | an endow…….. | endower |
| 4 | sacrifices his interests for the good of others | a self-sacrific…… | self-sacrificer |
| 5 | advocates or opposes a cause or an issue vigorously | an activ…… | activist |
| 6 | is unselfishly concerned for or devoted to the welfare of others (opposed to egoist) | an altru…… | altruist |
| 7 | raises funds | a fund-rais…….. | fund-raiser |
| 8 | offers to do something (willingly, without being compelled) | **a volunteer** *(déjà complet)* | volunteer |

**D.** Consigne verbatim : « You wrote the definition of "philanthropy" in your notebook – a
homework assigned by your teacher – Unfortunately, your little brother spilt a cup of coffee on
the page and some parts of the words have disappeared. Read the paragraph. Try to remember what
you wrote. Each dot stands for a letter. »

**Le paragraphe troué, verbatim :**

> Altruistic concern for human welf… and adv. . . . ment, usually manifested by don…. . of
> money, prop…., or work to n . .dy persons, by end …. .t of institutions of learning and
> hos…. ls, and by being gen …. . to other soci …y useful purposes.

**Corrigé D (guide p.23)** : welfare, advancement, donation, property, needy, endowment,
hospitals, generous, socially.

#### Activity 3 (manuel p.46)

« Think of the Tunisian context. In small groups, list the different occasions when Tunisians
show generosity to their needy countrymen then share the information with your other
classmates. » → réponses attendues : la liste du guide p.22-23 reproduite plus haut.

#### Activity 4 — Homework. A mini-project (manuel p.46)

Consigne : « Select an NGO (Non-Governmental Organization) or a philanthropist from the lists
below. In pairs or in a small group, find out about the organization or the person by doing
internet research then write a short report. Be ready to present it to your classmates by the end
of this module and don't forget to keep it in your portfolio. »

| Organizations (or Foundations) | Famous philanthropists |
| --- | --- |
| UNICEF | Bill Gates |
| OXFAM | Aziza Othmana |
| UNESCO | King Faisal |
| Save The Children | Prince Charles |
| Red Crescent | John D. Rockefeller |
| Red Cross | Martin Luther King, Jr. |
| UNDP : United Nations Development Programme | Oseola Mc Carty |
| Women's Environment and Development Organization | Mother Teresa |
| UNHCR : United Nations High Commissioner for Refugees | Alexis De Tocqueville |
| Human Rights Watch | Andrew Carnegie |
| Bright Star Foundation | |
| Life in Africa Foundation | |
| BAPS Care International | |
| Islamic Relief | |

**Questions guides pour la recherche** (verbatim) :

*The organization / the foundation :*
- When was it established ? By whom ? Where is it located ?
- What are its major objectives ? How does it raise money ?
- What are some of its philanthropic activities ?
- What are some of its achievements all over the world ?

*The philanthropist :*
- What's his / her nationality ? Is he/she alive or dead ?
- How did he/she make money ?
- What is he/she interested in ?
- Which cause(s) does/did he/she support ?
- Which philanthropic activities and accomplishments made him/her famous ?

---

## Section Two : Listening

*(manuel p.47-49 · guide p.24-25 · tapescript guide p.78)*

#### Scope and sequence (guide p.24)

| Rubrique | Contenu imprimé |
| --- | --- |
| **Skills/subskills and strategies** | **Reading** : infer attitudes and outcomes · identify the communicative value of a text (poem). **Listening** : identify vocabulary items · identify the meaning of unfamiliar words · demonstrate understanding of an extended text (a speech) · infer and evaluate the speaker's intention · recognize text structure · identify purpose. **Writing** : write a coherent text |
| **Vocabulary** | beneficiary, bequest, budget, burn, charge, cool, efficiency, fainting, flow, grateful, in vain, injuries, mission, nest, network, orthopaedic, pediatric, research, run (sth), state-of-the-art, walks of life, will (n) |
| **Grammar** | emphatic form · compound adjectives |
| **Functions** | expressing opinion · expressing feelings |
| **Pronunciation** *(imprimé « Pronuncition » [sic])* | process speech involving dysfluency features (pausing at the end of a thought group) · recognizing rhythm and intonation patterns in a speech |
| **Homework** | reorder a jumbled announcement to get a coherent text |

#### Helpful notes (guide p.24-25)

- **Emily Dickinson (1830-1886)** « is still considered America's foremost woman poet. She wrote
  more than 1.700 poems. » *(soit 1700 poèmes — la source écrit « 1.700 » avec un point séparateur
  de milliers)*. « The strongest influences on Dickinson's poetry are the Bible and Shakespeare.
  She never married and she seldom left her family home in Amherst, Massachusetts, but she
  transcended all physical limitations in her artistic correspondence and even more so, in her
  psychologically penetrating poems. »
- Encourager les élèves à parler de leurs expériences et sentiments personnels et à partager.
- Faire dégager le lien entre le poème et la philanthropie : *solidarity, comforting others,
  offering help, helping others overcome suffering, volunteerism…*
- « Giving meaning to life is an automatic result of the poet's philanthropic actions (use of
  if + present ….) » → **le poème est bâti sur `if + présent`**, structure à exploiter.
- En traitant **B.1** (des questions *As you listen*), introduire l'expression **« walk of life »**.
- Tout au long de la section, faire identifier **les traits d'un discours efficace** :
  *clear outline, greetings, grabbing the attention of the audience through a quote / statistics
  etc., introducing – developing – clarifying the key point, supporting the key point with
  different devices (including intonation patterns), giving a counterargument, refuting the
  counterargument, concluding and bringing closure to the speech.*
- Les élèves devront **réinvestir** cette connaissance de la structure du discours, des stratégies
  discursives et des schémas d'intonation pour produire et prononcer un discours en **section four**.

#### BEFORE YOU LISTEN (manuel p.47)

**A.** « Answer these questions. »
1. Have you ever cared for a depressed/troubled person, or saved a bird/an animal from danger ?
2. How did you feel about it ?

**B.** « Read the following poem then answer the questions below. »

> **Œuvre sous droits — non reproduite (R-2).** Poème d'**Emily Dickinson**, connu par son premier
> vers *« If I can stop one heart from breaking »*. **Genre** : poème lyrique court, une seule
> strophe de 7 vers dans la mise en page du manuel. **Structure de langue** : trois propositions
> conditionnelles en `If I can + verbe` (arrêter un cœur de se briser / apaiser une douleur /
> aider un rouge-gorge défaillant à regagner son nid), suivies de la conclusion répétée en
> ouverture et en clôture — vivre n'aura pas été vain. **Thème** : le sens de la vie tient au
> soulagement de la souffrance d'autrui, fût-elle celle d'un oiseau. **Gloses marginales du
> manuel** (légendes des illustrations) : *a robin*, *a nest*. **Attribution imprimée** :
> Emily Dickinson.

**Questions posées sur le poème** (manuel p.47) :
3. What does Emily mean by « I shall not live in vain » ?
4. How does this poem relate to philanthropy ?
+ consigne complémentaire : « Find out the relationship between the actions described and the
human values conveyed in this poem. »

#### AS YOU LISTEN (manuel p.47-48)

**A.** « Listen to the speech and identify in which order the speaker does the following : »
*(cases à numéroter ; ordre imprimé dans le manuel ci-dessous, corrigé du guide p.25 en 3e colonne)*

| Ordre d'impression | Énoncé | Réponse (guide p.25 : « order : 3, 1, 4, 2 ») |
| --- | --- | --- |
| 1er item | explains why the organization needs money | **3** |
| 2e item | greets the audience, tries to catch their attention and introduces the organization and its key mission | **1** |
| 3e item | urges for harder work to get more contributions and financial support | **4** |
| 4e item | talks about the achievements of Hope Organization, where the money comes from and how it is spent | **2** |

**B.** « Listen again and answer the following questions. »
1. Who are the members of this organization ?
2. How does the speaker try to catch the attention of his audience ?
3. Who are the beneficiaries of their actions ?
4. What do they benefit from ?
5. Where does the money come from ?

**Corrigé B (guide p.25)** — seule la question 2 est corrigée explicitement :
> **B.2** : « The speaker gives a quote, statistics, using the emphatic form, intonation patterns… »
Le guide ajoute : « For some details / reference questions see tapescript. » → réponses dérivées
du tapescript (guide p.78) :
- **B.1** : « We come from all walks of life. We are doctors, farmers, actors, mechanics,
  shopkeepers, businessmen, singers, teachers, lawyers, sportsmen and students. »
- **B.3** : les enfants soignés dans les hôpitaux de Hope Organization (et leurs parents).
- **B.4** : des soins médicaux spécialisés très coûteux, gratuits pour le patient (problèmes
  orthopédiques, brûlures).
- **B.5** : majoritairement du *Endowment Fund* des hôpitaux (≈ 80 % des budgets de
  fonctionnement et de recherche) ; le reste de dons (*gifts*) et d'événements de collecte
  (*fund-raising events*).

**C.** « What do the following figures in the listening passage refer to ? »
1. **12** : → réseau national de 12 hôpitaux (tapescript)
2. **5000** : → plus de 5 000 patients soignés dans les hôpitaux pour la seule année 2002
3. **80 per cent** : → part des budgets de fonctionnement et de recherche financée par les
   revenus du *Endowment Fund*
4. **93 per cent** : → part du budget des hôpitaux consacrée aux soins et à la recherche
   *(les 8 % restants aux frais administratifs et de collecte — voir Incertitudes : 93 + 8 = 101)*

**D.** « Listen to part two of the speech and ; »

**D.1** « Complete with the right words. » — texte à trous verbatim :

> Our Hope Organization opened its very first hospital back in 1970, and today there is a
> national network of 12 hospitals that provide highly expensive, …………. medical care to
> children with ……………. problems or …………….. injuries – all at no …………….. to the patient.
> In ………… alone, there were over 5000 patients receiving care at our hospitals. That's a lot
> of smiling little faces and ……………. moms and dads.

**Réponses** (d'après le tapescript guide p.78, dans l'ordre) : **specialized · orthopaedic ·
burn · charge · 2002 · grateful**.

**D.2** « Listen again and check your answers. »

**D.3** « Mark the places where the speaker pauses. Practise reading the sentences with your
classmate. »
**Corrigé D.3 (guide p.25, verbatim)** : « The speaker usually pauses at the end of a "thought
group", a group of words that expresses a thought. Then pauses again at the end of the second
thought group, the end of the sentence » *(le guide imprime « wordsthat » [sic])*.

**E.** « Listen to part three and ; »

**E.1** « Complete the missing words. » :
> « our hospital system ……… need more money and ……… is the time when we must work harder. »

**E.2** « How does the speaker pronounce the missing words and why ? »

**Corrigé E (guide p.25)** :
- **E.1** : **DOES**, **NOW** *(majuscules dans le tapescript — marque de la forme emphatique)*
- **E.2** : « The speaker raises the pitch of his voice in "DOES" and "NOW" to emphasize meaning ;
  an additional information is carried over and above that which is expressed by the words in the
  utterances »

**F.** « In part three the speaker states a counterargument. What is it ? Does he accept it or
does he prove it wrong ? »
→ Contre-argument du tapescript : « A lot of people probably think that our hospitals don't need
any more money. » ; il le réfute : « Well, the truth is, that's not the case. »

**G.** « Tick the appropriate alternative. The purpose of the speech is »
1. to entertain ( )
2. to persuade the audience ( )
3. to inform ( )

**Corrigé G (guide p.25)** : **2** (to persuade the audience).

**H.** « Rephrase the following expressions. » *(adjectifs composés — point de grammaire de la section)*
1. fund-raising events :
2. well-run philanthropy :
3. ever-increasing costs :
*(aucun corrigé imprimé)*

#### Homework (manuel p.49)

« Reorder the following sentences to get a coherent public service announcement for your local
radio station. » — 8 phrases, seule la n° 2 est pré-numérotée :

| Case | Phrase (verbatim) |
| --- | --- |
| ( ) | It may not be your neighbour or co-worker or best friend who needs your blood today. |
| ( ) | Every …………… someone needs blood in Tunisia. *(le blanc fait partie de l'exercice)* |
| **( 2 )** | Too many Tunisians wait until they need blood before they truly realize the importance of volunteer blood donation. |
| ( ) | But someone does. |
| ( ) | DONATE BLOOD ; THE GIFT OF LIFE |
| ( ) | Donating blood saves three lives. |
| ( ) | Call ( blood bank / centre ) at ( phone ) |
| ( ) | Give the gift of life during National Blood Donor Month |

*(aucun corrigé imprimé dans le guide pour ce homework)*

---

## Section Three : Reading

*(manuel p.50-55 · guide p.26-27)*

#### Scope and sequence (guide p.26)

| Rubrique | Contenu imprimé |
| --- | --- |
| **Skills/subskills and strategies** | **Reading** : draw on background knowledge to predict content · tap on different sources to answer a specific question · transfer information onto a table · match dictionary choices with context at hand and explore nuances · scan for specific information · guess the meaning of unfamiliar words through context clues · identify vocabulary items · identify the communicative value of an utterance · infer an attitude. **Writing** : express opinion about a specific issue |
| **Vocabulary** | bathe, bond, bring out, clubbing, cute, dedicate, dwarfism, genetic, give up, gossip, hero, homeless, milestone, party (v), puberty, rescue, salute, shelter, stone, swap, take over, take turns, tragic, worldwide |
| **Grammar** | phrasal verbs, should have + past participle, present perfect vs simple past |
| **Functions** | talking about a personal experience · expressing opinion |
| **Homework** | do a web research · gap-filling exercise |

#### Helpful notes (guide p.26)

- « Phrasal verbs are one of the major important features of the English language. Raise the
  students' awareness of the form and the functional use of phrasal verbs. In the following
  modules, present any phrasal verb that is new to the students. »
- « The reaction letter could be written in small groups. Make sure the members of the group share
  the same attitude(s) »
- « Homework : the students may do the research individually or in groups. »

#### BEFORE YOU READ (manuel p.50)

**A.** « Try to recall a time when you sacrificed something (money, time, a desire, a dream …)
for the good of others. Tell your classmates about it. »

**B.** « Look at the picture. Read the sentence in bold letters, the first lines and the last
sentence and guess why Toni looks like a little girl although she's 18 and what made of Kirsty a
self-sacrificer. » + « Read the whole text and check your guesses. »

#### Le texte-support (manuel p.50-51)

- **Titre / accroche en gras** : « My sister looks like a little girl ……….. but she's 18. »
- **Chapeau** : « They should be partying and swapping clothes, but a tragic illness means one
  loving sister spends her time caring for the other … »
- **Genre** : article de magazine, cas de vie réelle (*human interest story*)
- **Source citée** : **Woman** (magazine, mention en fin de texte p.51)

**Résumé fidèle et détaillé** :
Toni Johnson a eu **18 ans en octobre**, mais elle a l'apparence d'une petite fille. Elle souffre
d'une maladie génétique rare, le **syndrome de Dyggve-Melchior-clausen** [sic — minuscule à
« clausen »], une forme de **nanisme** : elle pèse **3 st ½** et mesure **3 pieds**. Complication
supplémentaire, elle est née avec de **l'eau sur le cerveau** (hydrocéphalie), d'où des troubles
d'apprentissage si sévères qu'elle a **l'âge mental d'un bébé**. Elle vient d'atteindre la
puberté mais ne peut ni marcher, ni parler, ni se nourrir seule, et porte encore des couches.
Son corps vieillira, mais son développement restera celui d'un enfant. La maladie est **rare : 3
malades au Royaume-Uni, 10 dans le monde**. Toni a besoin de **soins 24 h/24**, assurés à parts
égales par sa sœur **Kirsty** et leur mère **Helen**.

Helen dit que le fait que sa fille ne grandirait jamais vraiment, ne se marierait pas et n'aurait
pas d'enfants lui a fait l'effet « d'une tonne de briques tombant sur la tête ».

**Kirsty, 22 ans**, s'occupe de Toni **depuis ses 5 ans à elle** ; elle a **renoncé à des études
d'infirmière** pour la soigner. Elle dit oublier souvent que Toni est sa sœur — « She's like my
daughter » — et avoir du mal à la confier à d'autres. Bien qu'elle ait travaillé par le passé,
elle a **tout abandonné** pour Toni : l'après-midi elle la nourrit, la change, la baigne et la
couche. Kirsty et Helen **se relaient le week-end**. Depuis les 18 ans de Toni, Kirsty l'emmène
au pub de temps en temps ; ses amis sont gentils avec elle mais pris par leur propre vie, alors
Kirsty les retrouve pour une soirée quand c'est le tour de sa mère de garder Toni.

Kirsty se demande parfois ce que ce serait si sa sœur lui ressemblait et qu'elles puissent sortir
en boîte ensemble — mais leur relation est « totalement différente » et pleine de plaisir : Toni
rit tout le temps et dit « hiya » d'une petite voix qui conquiert tout le monde ; le samedi on la
laisse veiller, on commande à emporter ou on va au cinéma. Pour ses 18 ans, les **Johnstons**
[sic — « Johnsons » ailleurs] ont organisé une **fête surprise** avec disco et un sosie de **Tom
Jones**, en présence de tous ses amis et de sa famille. Toni aime la musique : **Aaron**, son
demi-frère, vient jouer de la guitare pour elle.

Kirsty se dit prête à **consacrer le reste de sa vie** à Toni : elle voudrait une famille un jour,
mais pas maintenant — trop jeune, et déjà les mains pleines. Elle pense à sa sœur en permanence,
en perd parfois le sommeil, et sait que si un jour sa mère ne peut plus s'en occuper, elle
**prendra le relais entièrement** et elles vivront ensemble : « I just can't imagine us ever being
apart. »

**Notes de bas de page du manuel (p.51)** :
- `* 3 1/2 st . 2 stone = 12.7 kilograms`
- `* 3 feet = 0.9144 metres`

#### AS YOU READ (manuel p.51-53)

**A.** « Complete the table with information from the text. » — tableau à 3 colonnes, vide :

| Toni's condition | Cause(s) | Effects on her bodily and mental development |
| --- | --- | --- |
| | | |

→ Attendu d'après le texte : *Dyggve-Melchior-clausen syndrome, a form of dwarfism* / *rare
genetic condition + born with water on the brain* / *weighs 3½ st, 3 ft tall, mental age of a
baby, can't walk-talk-feed herself, still in nappies, will always be a child developmentally.*

**B.** « Read the third paragraph and the dictionary entry then choose the appropriate meaning
for the word "dwarf". » — **entrée de dictionnaire, verbatim (manuel p.52)** :

> dwarf /dw_f/ (pl ~s) n. person, animal or plant much below the usual size ; (in fairy tales) a
> small being with magic powers. V.t 1. prevent from growing to full size. 2. cause to appear
> small by contrast or distance: the big steamer ~ed our little launch.

Puis : « Now, justify your choice with specific details from the text. »
*(la transcription phonétique est imprimée `/dw_f/` — voir Incertitudes)*

**C.** « Match the underlined phrasal verbs in column A with their definitions in column B. »

| # | Colonne A (phrase du texte, phrasal verb souligné) | Colonne B | Corrigé (guide p.27) |
| --- | --- | --- | --- |
| 1 | A loving sister spending her time **caring for** the other. | a) pay an informal visit to | **1 + e** |
| 2 | **Gossiping** about boyfriends. | b) abandon | **2 + h** |
| 3 | Kirsty **gave up** the chance to study. | c) come up to | **3 + b** |
| 4 | She'd never **grow up** properly. | d) remain awake and out of bed | **4 + j** |
| 5 | I **catch up** with them for a night. | e) look after / take care of | **5 + c** |
| 6 | …never fails to **win** everyone **over**. | f) assume responsibility for | **6 + g** |
| 7 | We let her **stay up** late. | g) gain the favour and support of | **7 + d** |
| 8 | Aaron **comes round** | h) talk about the affairs of others | **8 + a** |
| 9 | She's prepared to **dedicate** the rest of her life to Toni. | i) devote wholly | **9 + i** *(imprimé « 9+I »)* |
| 10 | I will **take over** completely. | j) attain mental or physical maturity | **10 + f** |

**D.** « Tick the right alternative. »
1. « swap clothes » means : a) buy clothes — b) donate clothes — **c) exchange clothes** ✔
2. « It should have marked a milestone in her life »
   - A milestone is : a) a hard time — **b) a significant event or stage** ✔ — c) a sad change
   - « It should have marked a milestone in her life » means that marking a milestone in her life was :
     a) a wrong action which unfortunately took place
     **b) a sensible action that didn't happen** ✔
     c) an action which wasn't necessary but it occurred

**Corrigé D (guide p.27)** : « D. 1+c   2+b   should have marked +b »
→ **Point de grammaire visé** : `should + perfect infinitive` (*should have + past participle*)
exprime une action **sensée mais qui n'a pas eu lieu**.

**E.** « The following statements are false. Correct them with details from the text. »
1. Toni's condition is a widespread one.
2. Kirsty is a nurse.
3. Toni never gets out of the house.
4. Kirsty has lost touch with her friends.
5. Relatives and friends showed no interest in Toni's case.
*(aucun corrigé imprimé ; les corrections tiennent dans le texte : maladie rare — 3 cas au R.-U.,
10 dans le monde / Kirsty a renoncé aux études d'infirmière / elle l'emmène au pub, au cinéma, en
« takeaway » / elle retrouve ses amis pour une soirée quand c'est le tour de sa mère / tous ses
amis et sa famille sont venus à la fête surprise de ses 18 ans, Aaron vient jouer de la guitare)*

**F.** « "We have a totally different relationship", says Kirsty. How would you describe their
relationship ? »

**G.** « Read and complete. "I do sometimes wonder what it would be like if she were like me and
we could go out clubbing together." Through this sentence Kirsty expresses ……………………………… »
*(ancrage : le simple past `were` en emploi hypothétique — cf. encadré grammaire, colonne B)*

**H.** « What does Helen mean by "the fact that she'd never grow up properly, get married or have
children felt like a ton of bricks falling on my head." ? »

**I.** « In small groups, list Kirsty's self-sacrificial decisions in order to care for her sister
Toni. »

#### Encadré « Exploring grammar » — present perfect vs simple past (manuel p.53, corrigé guide p.27)

Consigne manuel : « Study the examples in column A and in column B. »
Consigne guide : « Study the examples in column A and in column B then do the activities below. »

**Les exemples (identiques manuel / guide) :**

| Colonne A | Colonne B |
| --- | --- |
| She's sacrificed a large part of her life for her | Toni turned 18 in October |
| Toni's just reached puberty | Kirsty gave up the chance to study nursing at college |
| …and has done so since she was five | She has done so since she was five *(voir Incertitudes)* |
| Kirsty's worked in the past | The Johnsons arranged a surprise party |
| She's given up everything to care for Toni | |
| I've started taking her to the pub once in a while | |

**Le texte de l'encadré, blancs du manuel comblés par le guide p.27 (en gras = ce que le guide
imprime, le manuel laissant des pointillés) :**

**Colonne A**
- What is the tense used ? → **The Present Perfect**
- Form : → **have ('ve) / has ('s) + past participle**
- Use :
  - To talk about actions or situations which **started** in the past and **have continued** up to
    the present.
  - For actions and situations which **started** in the past and went on until very **recently**.
  - To talk about actions that **have been** repeated in a period up to the **present**.
  - To say that an action **has** just been **finished** or to talk about its **results**.
  - We do not use the present perfect with expressions that refer to a **finished** time-period
    (e.g. Last week, yesterday …)
- Also, present perfect with : **up to now, all this year, all my life, so far, during the ….,
  recently, lately, already, just, ever, never, yet.**

**Colonne B**
- What is the tense used ? → **The Simple Past**
- Forms : → **regular form / irregular form**
- Use : The **Simple Past** tense is the one most often **used** to talk about the past.
  It can refer to **short**, quickly-**finished** actions and events, to **longer** actions and
  situations, and to repeated happenings.
- Also, Past tense with present or future meaning :
  - The simple past is used in **conditional sentences after : if, suppose, as if, if only,
    it's (high) time, would rather, wish**.

#### AFTER YOU READ (manuel p.53)

« After reading magazine articles dealing with important issues and stories related to specific
cases from real life, readers usually react. Now, write a short letter to Woman's editor, in which
you express your opinion about Kirsty's self-sacrificial attitude and you say whether you would
behave in the same way if you were in her position. »
*(guide p.26 : la lettre de réaction peut être écrite en petits groupes, à condition que les
membres partagent la même attitude)*

#### Practising related grammar points (manuel p.54)

**A.** « Put the verbs in brackets in the present perfect tense or the simple past tense. »

**Exercice 1 — verbatim :**
> **Mary** : I (just/see) Miss Bloggs. She's upset because you (not send) her the money yet.
> **Paul** : But I (explain) the reasons when I (meet) her last Monday.

**Corrigé 1 (guide p.27)** : **have just seen · haven't sent · explained · met**

**Exercice 2 — verbatim :**
> Ralph, Tom and Stella are three friends who (know) each other for many years. They (be)
> neighbors since they (be) children. Ralph (live) next door to Stella and Tom for fifteen years.
> They (grow) up together, They (go) to school together, and they (visit) each other almost
> everyday.
> A year ago, Ralph (study) management. This morning, he (get) a phone call from a factory owner.
> He (offer) him a full-time job with a good salary. Although the factory is a long way from home,
> Ralph (accept) the offer because he (be) jobless for months now. Ralph will miss his friends
> very much but they'll see one another when he comes home on his vacations.

**Corrigé 2 (guide p.27, verbatim)** : « have known, have been, were, has lived, have grown,
have gone, **have invited** [sic — l'énoncé porte *(visit)* : lire *have visited*], studied, got,
offered, accepted, has been. »

#### Homework (manuel p.55)

**A.** « Fill in the blanks with the words in the box. »

**Banque de mots** : `rescue, May, apart, bring, shelter, feed, tragic, worst`

**Le texte, verbatim :**
> Dear Reader,
>
> The Los Angeles earthquake, the Mississippi River floods, the hurricanes in Florida and Hawaii,
> natural disasters tear lives ………… in seconds.
>
> But the …………. of nature can ………. out the best in people.
>
> Scholastic salutes the heroes – young and old – who help to ………. the injured, ……….. the
> hungry, and ………… the homeless in times of need.
>
> ……….. the spirit that moves us to help others in ………… times stay with us every day of our
> lives !
>
> Sincerely,
> Richard Robinson
> President and CEO, Scholastic Inc.

**Corrigé (guide p.27)** : 1. **apart** · 2. **worst** · 3. **bring** · 4. **rescue** ·
5. **feed** · 6. **shelter** · 7. **May** · 8. **tragic**

**B.** « Do some research on the web or in a medical book to find some information related to the
genetic condition called Dyggve-Melchior-clausen syndrome. When it is ready, make a brief
presentation to your classmates. »

---

## Section Four : Speaking — Producing and delivering a speech

*(manuel p.56-58 · guide p.28-29)*

#### Scope and sequence (guide p.28)

| Rubrique | Contenu imprimé |
| --- | --- |
| **Skills/subskills and strategies** | **Reading** : recognize text structure · identify the communicative value of a text / pictures · extract salient points for subsequent use in speaking. **Speaking** : reinvest new words/expressions in one's speech · produce an outline · produce appropriate intonation patterns · produce a range of discourse strategies to persuade people to do something |
| **Vocabulary** | anecdote, commitment, consistently, dignity, essence, infrastructure, meet (a responsibility), sustain (development), well-being |
| **Functions** | giving information · suggesting a course of action · advising others to do something · persuading others to do something |

*(pas de rubrique Grammar / Pronunciation / Homework / Mini-project imprimée pour cette section)*

#### Helpful notes (guide p.28-29)

- « Elicit from the students what UNICEF stands for and let them talk about its key missions and
  major achievements. »
- « In talking about Bellamy's message, lead the students gradually to focus on the last lines
  "adolescents and children..." and exploit that later in establishing a link with the speech. »
- « Have the students focus on the fact that commitment and action are also required from children
  and adolescents themselves (they donate and take part in philanthropic activities) »
- **Description des photos (guide p.28)** : « absence of the basic amenities of life (water,
  electricity, rural roads, housing), isolated areas, substandard living conditions »
- **Ce dont ces personnes ont besoin (guide p.28)** : « decent housing, healthy living conditions,
  schools and libraries, educational opportunities, clean drinking water, hygienic living
  conditions, cultural programmes, roads, health care centres, economic integration, money and
  in-kind contributions. » (+ renvoi : *in-kind contributions : see section one*)
- **Le discours (guide p.29)** : « In addition to the suggestions given in the textbook (page 58),
  encourage the speakers to use body language to illustrate some points, maintain eye contact with
  the audience, follow rhythm and intonation patterns to emphasize some key points. »
- « Have the students reinvest what they've learnt in section two : the specific features of an
  effective speech. »
- « The students may use the quotes given in section one. »

#### Activity 1 (manuel p.56-57)

**A.** « Read the ad and answer the questions below. » — *l'annonce est une publicité **UNICEF**
signée **Carol Bellamy** (l'image et son texte ne figurent pas dans la couche texte — voir
Incertitudes)*.
1. What do you know about UNICEF ?
2. What is the message that Carol Bellamy is sending through the ad ?
3. Which arguments does she use to support it ?

**B.** « Look at the pictures below. »
1. What do you think these people need ?
2. « Check your answers with a classmate then share the information with the class. »
→ **9 photos numérotées 1 à 9** (manuel p.56-57 ; contenu visuel non transcriptible — voir la
description fournie par le guide p.28 ci-dessus).

#### AS YOU SPEAK (manuel p.58)

Contexte imprimé : « **December 8, is the National Solidarity Day in Tunisia.** Your school
headmaster / headmistress wants you to »
1. persuade your schoolmates to donate money,
2. tell them about the different philanthropic activities from which the needy people will benefit,
3. state the great social and human values behind the act.

Consignes : « In small groups, prepare a short speech. Follow the outline of the speech (refer
back to Section two) then volunteer to deliver the speech. You can use visual aids like posters,
brochures, photographs, transparencies … »

**Encadré « catch the attention of your audience » (verbatim)** :
> There is more than one way to catch the attention of your audience :
> • ask a question
> • tell an anecdote ( a very short funny story )
> • cite a quote
> • give statistics …
> (Because the speech is short, use one or two of them)
> Try not to read the speech literally.

---

## Section Five : Writing

*(manuel p.59-62 · guide p.30) — les en-têtes des pages 61 et 62 du manuel impriment
« Session five » [sic] au lieu de « Section five ».*

#### Scope and sequence (guide p.30)

| Rubrique | Contenu imprimé |
| --- | --- |
| **Skills/subskills and strategies** | **Reading/Listening** : identify purpose, attitude and point of view · distinguish between literal and implied meanings · identify the communicative value of a text. **Writing** : apply the writing process to produce a cohesive and unified piece of writing using an outline and notes |
| **Vocabulary** | abolish, advocate, assassination, character, civil rights, elect, enrol, harmony, impressed, ivory, march, metaphor, preach, protest, racial injustice, segregation, untiring, vote |
| **Grammar** | consolidate the use of discourse markers : expressions used to show the structure of a text · expressions of divisions |
| **Functions** | giving information · expressing opinion about a specific issue · describing people in a picture |

#### Helpful notes (guide p.30)

- « Have the students listen to the song and construct much meaning from it. »
- « Before you write.3. Make the students write complete sentences and discuss them in small groups. »
- « Have the students identify the communicative value of Martin's statement. Invite them to
  express any relevant ideas they may infer. »
- « The subject matter is provided. The student's task is not to generate ideas but to use the
  notes to create/produce a cohesive and unified piece of writing. Have the students concentrate
  on the aspects of writing / evaluation criteria mentioned and apply the writing process
  strategies. »

#### BEFORE YOU WRITE (manuel p.59)

**A.** « Read and listen to the following song then answer the questions below. »

> **Œuvre sous droits — paroles non reproduites (R-2).** **Titre** : *Ebony And Ivory*.
> **Auteurs imprimés** : **Paul Mc Cartney** et **Steve Wonder** [sic — *Stevie Wonder*].
> **Genre** : chanson populaire (duo). **Structure** : couplet-refrain, avec reprise du distique
> d'ouverture ; le manuel n'en donne qu'un extrait de 8 lignes (2 + 6), le tapescript du guide
> p.79 donne la version longue avec ses reprises. **Thème** : les touches noires et blanches du
> piano, qui cohabitent en parfaite harmonie, servent de **métaphore** de la coexistence
> harmonieuse des Noirs et des Blancs ; le refrain constate que les gens sont partout les mêmes,
> qu'il y a du bon et du mauvais en chacun, et que l'on apprend à vivre et à **se donner
> mutuellement ce qui est nécessaire pour survivre ensemble** — d'où le lien direct au titre du
> module (*we learn to give*). **Notions de langue travaillées** : la métaphore ; le lexique
> *ebony / ivory / harmony* ; le verbe *give*.

**Gloses du manuel (notes éditoriales, p.59)** :
- `* ebony : black key on a piano`
- `* ivory : white key on a piano (having the colour of ivory)`

**Les questions posées sur la chanson (verbatim)** :
1. The ebony and ivory keys on the piano are used by the singers as metaphors. What do they
   symbolize ?
2. Steve Wonder is black. Paul Mc Cartney is white. What does that mean to you ?
3. What is the message of the song ? Complete the sentence below.
   « Instead of ………………………………………………………………………… , we should
   ……………………………………………………………………….. »
*(guide p.30 : pour la question 3, faire écrire des phrases complètes et les discuter en petits
groupes)*

**B.** « Read the following sentence then answer the questions. »

> **Citation imprimée** : la phrase la plus connue du discours **« I have a dream »** — l'orateur
> y dit rêver que ses **quatre jeunes enfants** vivent un jour dans une nation où ils seront jugés
> non sur la **couleur de leur peau** mais sur le **contenu de leur caractère**.
> *(discours sous droits — restitué ici par le sens ; le texte exact figure manuel p.59)*

Questions : « Look at the picture. Do you recognize the man leading the march ? » / « What do you
know about him ? »
→ **Martin Luther King, Jr.** (photo de la marche, manuel p.59-60 ; image non transcriptible).

#### AS YOU WRITE (manuel p.60-61)

Consigne verbatim : « Below is a time line indicating some of the events and achievements in the
life of Dr. Martin Luther King, Jr. the great leader of the civil rights movement in America. Use
the chronological development provided on the time line to produce a cohesive and unified piece of
writing. »

**La chronologie (manuel p.61), transcrite fidèlement — les `[→]` marquent les flèches de la
maquette :**

- **1929** — Birth. Atlanta, Georgia.
  - father : pastor of Baptist Church
  - family : religious, supportive, loving
- **(1940's)** en marge · **1930s** — face problems : segregation, racial injustice
  - dream job : lawyer or doctor
- **1946** — preach in father's church - success
  - study at theological seminary. Pennsylvania
  - learn about life and work of Gandhi in India
  - impressed with Gandhi's use of non-violent protest to achieve freedom and civil rights
  - enrol [→] Boston University for further study
- **1955** — earn a Doctor of Philosophy degree
- **1960's** en marge · **1950's** — untiring worker for the civil rights movement in the United States
  - lead peaceful protests - insist on nonviolence
- **August 28, 1963** — help lead a famous civil rights march on Washington, D.C., (a quarter of a
  million blacks and whites)
  - in front of the Lincoln Memorial. – famous speech « I have a Dream »
  - One of the most important speeches in American history
  - new local and state laws [→] to abolish segregation
  - further freedom and civil rights in certain places
- **1963** — Time magazine [→] « Man of the Year »
- **1964** — The Nobel Peace Prize
- **1965** — Congress [→] pass the Voting Rights Act
  - Many blacks [→] to vote for the first time
  - black leaders [→] elected to important offices
  - violent actions and reactions against him
  - to receive threats to his life
- **April 4, 1968** — King and staff meeting - plan peaceful march
  - assassination of Dr. Martin Luther King, Jr.

#### Les connecteurs proposés (manuel p.62) — verbatim

Consigne : « Select from the following expressions the appropriate items that will help you
structure your text. »

- firstly, ……………. secondly, ………………. thirdly, ………………., finally, ………………………….
- first of all, …………………
- to begin with, …………………..
- to start with, ………………………
- in the first place, ……………………….
- for one thing, ……………………… for another thing, …………………….
- another thing is ……………………………………………
- moreover · in addition · similarly
- as well as that · on top of that
- besides (introducing a stronger argument than the one before)
- earlier · later · before that · after that

#### Le processus d'écriture imposé (manuel p.62) — verbatim

- Write your first draft
- Read your text to check if you have used the appropriate cohesive devices
- Make any improvements you judge necessary
- Read and correct any punctuation mistakes you may find
- Exchange your writing with your classmate and give feedback to each other
- Write your final draft and keep it in your portfolio.

---

## Supplément ARTS (filière Lettres uniquement)

> Manuel p.63-70 · guide p.31-33. **Ces deux sections ne concernent PAS le tronc commun** : elles
> sont propres à la section Lettres (« Arts »). Elles comportent leur propre progression, leur
> propre vocabulaire (« Arts Supplement » dans la liste finale du manuel p.72) et leurs propres
> corrigés dans le guide.

#### Arts. Section One : Reading a poem

*(manuel p.63-66 · guide p.31 · tapescript du poème guide p.80-81)*

##### Scope and sequence (guide p.31)

| Rubrique | Contenu imprimé |
| --- | --- |
| **Skills/subskills and strategies** | **Reading** : identify the genre · identify features of the genre · draw on background knowledge to predict content · distinguish between literal and implied meanings · identify vocabulary items · scan for specific information · infer and evaluate the writer's intention. **Listening / Speaking** : listen to a poem and recite it in an expressive manner. **Writing** : apply the writing process to produce a poem |
| **Vocabulary** | abuse, barriers, boundaries, famine, free verse, gangster, greed, illiteracy, offence, selfishness, shadow, sit-in, smell, sonnet, soul, symbolize, terror |
| **Pronunciation** | pronounce properly at word, sentence and discourse levels · recite a poem in an expressive manner |
| **Functions** | sharing information · expressing opinion |

##### Helpful notes (guide p.31)

- « Follow the procedure suggested in this section. »
- « Make the students listen to the poem. Encourage and motivate them to read the poem aloud and
  in an expressive manner. Make of this activity an enjoyable experience. »
- « Elicit the different meanings and implications of "fire" from the students. Make them draw on
  their background knowledge. »
- « Have the students write their poems and display them in class. The students read the different
  poems and exchange appreciation and comments. »

##### BEFORE YOU READ (manuel p.63)

**A.** « In the following list, there are different types of poetry. (Haiku, Sonnet, Cinquain, Free
verse). In small groups, write the appropriate type of poetry in front of its corresponding
definition. »

| # | Définition imprimée | Réponse (guide p.31) |
| --- | --- | --- |
| 1 | poetry that lacks rhyme and which has less predictable rhythm. | **free verse** |
| 2 | Japanese form of poetry. Form is 17 syllables in 3 lines with pattern : First line : 5 syllables. Second line : 7 syllables. Third line : 5 syllables. It usually has nature themes. | **Haiku** |
| 3 | Syllabic verse form. Gradually increasing number of syllables in each line until the last line, which returns to 2 syllables. | **cinquain** |
| 4 | A lyric poem of 14 lines, each of 10 syllables, and with a formal pattern of rhymes. | **sonnet** |

**B.** « What does "fire" usually symbolize ? »

##### AS YOU READ (manuel p.63-66)

**A.** « Read the title of the poem *Catch the fire*. Do we usually catch fire ? » + « Guess what
the poet means by the word "fire" and share your guesses with your classmates. »

> **Œuvre sous droits — non reproduite (R-2).** **Titre** : *Catch the fire*. **Dédicace
> imprimée** : « poem for Bill Cosby* ». **Autrice** : **SONIA SANCHEZ** (le tapescript du guide
> p.81 signe « Sonya Sanchez » [sic]). **Source imprimée** : *From African American Women in
> Literature*. **Genre** : **vers libre** (*free verse*) — c'est la réponse attendue.
> **Structure** : un préambule entre parenthèses ; une longue partie construite sur la question
> répétée « Where is your fire ? » et l'injonction répétée de trouver ce feu et de le
> **transmettre** ; une chaîne de transmission de personne en personne (de moi à toi, du fils au
> père, du frère à la sœur, de la fille à la mère, de la mère à l'enfant) ; une série
> d'oppositions « The fire of X … not Y » ; une énumération de « feux » historiques ; puis un
> bloc final en **capitales** à quatre injonctions parallèles chacune suivie de « DON'T KILL »,
> une liste de gérondifs en majuscules terminés par un point (WALKING. SINGING. BUILDING.
> LAUGHING. LEARNING. LOVING. TEACHING. BEING.), et une clôture où la voix tend la main.
> **Thèmes** : la mémoire et la fierté noires, la transmission intergénérationnelle, le refus de
> la violence entre frères, l'histoire de la lutte afro-américaine (pyramides, navires
> négriers, jazz, sit-ins et marches, parler de la rue devenu rap). **Notions de langue
> travaillées** : le vers libre ; la question rhétorique et la répétition ; l'impératif ;
> l'antithèse « X not Y » ; le lexique de la protestation (*sit-in, march, boundary, barrier,
> gangster*).

**Notice biographique du manuel (p.65), verbatim** :
> Sonia Sanchez ( 1934-) Active participant in the civil rights movement and a follower of
> Malcolm X in the 1960s, Sanchez is committed to enhancing black consciousness through her
> poetry and short stories. Seeing herself as a continuation of the African American women who
> preceded her, she has said, « I have tried to continue the Black woman tradition of excellence. »

**Les questions (manuel p.65-66)** :

1. « Check your guesses. »
2. « Tick the appropriate alternative : The poem is : a) a haiku — b) free verse — c) a cinquain »
   → **Corrigé (guide p.31)** : **b) free verse**
3. « Find out in the poem words that mean : »
   - a) a member of a gang of criminals : → **gangster**
   - b) organized procession of demonstrators who are supporting or protesting something : → **march**
   - c) occupying a building or a part of it as a means of organized protest : → **sit-in**
     *(guide imprime « sit in »)*
   - d) something that fixes a limit : → **boundary**
   - e) something that blocks a passage : → **barrier**
4. « Complete the spidergram with the different implications of "fire" in the poem. » — deux
   branches sont **déjà remplies dans le manuel** : **love** et **Positive change** ; centre :
   **fire**.
   → **Corrigé (guide p.31)** : « love, positive change, life, culture, construction, struggle,
   glory, existence, self-expression, happiness, identity, learning etc. »
5. « Sonia Sanchez usually incorporates the history of the black struggle into her poetry. How is
   that reflected in *Catch the fire* ? »
   → **Corrigé (guide p.31)** : « slaveships (the ships which carried slaves from Africa to
   America). The sit-ins and marches for civil rights etc »
6. « Complete with the appropriate information from the poem. »
   - Sonia inspires us to free ourselves from ……………………………………………………
   - She incites us to ………………………………………………………………………………
7. « Sonia is well-known for painting pictures with words and sounds. Is this true in this poem ?
   Justify your answer with specific details. »
8. « Now, listen then volunteer to read the poem aloud and in an expressive manner. (Suppose you
   were Sonia Sanchez reading her poem at a cultural event). »

##### AFTER YOU READ — Writing a poem (manuel p.66)

Consigne verbatim : « Write a poem (a haiku, free verse, cinquain) in which you address the
universal theme of love and solidarity and you call for eliminating from the Earth evils such as
hatred, selfishness, racism, violence .etc. »

| Positive values | Earth evils |
| --- | --- |
| love | greed |
| peace | selfishness |
| mutual help and understanding | hatred |
| dialogue | destructive weapons |
| solidarity | racism |
| cooperation | terror |
| education | abuse |
| altruism | offence |
| | famine |
| | illiteracy |

#### Arts. Section Two : READING ABOUT GREAT PEOPLE

*(manuel p.67-70 · guide p.32-33 — **attention : le guide p.32 imprime par erreur l'en-tête
« Section Four : Speaking ». Anomalie confirmée, voir Incertitudes.**)*

##### Scope and sequence (guide p.32)

| Rubrique | Contenu imprimé |
| --- | --- |
| **Skills/subskills and strategies** | **Speaking** : make statements about a concrete situation · produce descriptions · express opinion about a specific case. **Reading** : predict content · skim for gist · scan for specific information · identify vocabulary items in context · recognize the relationship between form (punctuation) and meaning · provide a title for the text (from alternatives suggested). **Writing** : apply the writing process strategies to expand a quote into an article |
| **Vocabulary** | autobiography, blind, blunted, breeze, cause, challenge, daring, deaf, disability, dumb, immortals, interpreter, joyously, manifest, mysterious, paralytic, prevail, quiver, rallies, reach (n), revelation, strive, struck, suffrage, superstition, testify, touch of (n), tract, unfathomable, unique, unreachable, vaudeville, wild, yearning |
| **Functions** | describing a condition · expressing opinion · expressing approval/disapproval |

##### Helpful notes (guide p.32)

- « The writing activity could be done in groups. Form the groups according to their choices. »
- « The students are familiar with the strategies of expanding a quote into an extended text. They
  often practise this skill in Arabic, French, History, Geography …….. »
- **Plan imposé** :
  1. The student expresses thesis (Introduction : Thesis statement)
  2. The student presents arguments to support the thesis
     - Topic sentence + supporting arguments
     - Topic sentence + supporting arguments
  3. The student makes a conclusive statement
- « Make the students use the suggested expressions (page 70) » → renvoi explicite au manuel p.70,
  **preuve que cette page du guide traite bien la section Arts et non la Speaking du tronc commun**.

##### BEFORE YOU READ (manuel p.67)

**A.** « Complete the following sentences with words from the box below »
1. A blind person cannot ………. → **see**
2. A ………. person cannot hear. → **deaf**
3. A ………. person cannot speak. → **dumb**
4. A paralytic is a person who can't ……….. body parts. → **move**

**Banque de mots** : `taste, move, see, dumb, smell, deaf` *(6 mots pour 4 trous : « taste » et
« smell » sont des distracteurs)*
**Corrigé (guide p.33)** : « A. 1+see, 2+deaf, 3+dumb, 4+move »

**B.** « Think of a person you know and who suffers from a physical disability. »
1. What is his/her disability ?
2. What caused it ?
3. Has he / she ever tried to challenge that disability ? How ?
+ « Share the information you have with your other classmates. »

##### AS YOU READ (manuel p.67-69)

**A.** « Read paragraph No.1 and predict why Alexander Graham Bell, Maria Montessori, and Mark
Twain greatly praised Helen Keller. »
**B.** « Read the whole text and check your predictions. »

##### Le texte-support : « Helen keller : ……………………… » (manuel p.67-68)

- **Titre à trous** (l'élève doit le compléter en exercice I) : « Helen keller : ……………………… »
  *(minuscule à « keller » [sic])*
- **Genre** : texte biographique
- **Source imprimée** : *From The Book of Distinguished American Women*
- **Illustration** : photographie légendée « Helen Keller » (p.68)
- **Structure** : 7 paragraphes numérotés (1) à (7) — la numérotation est explicitement utilisée
  par les questions.

**Résumé fidèle, paragraphe par paragraphe :**

**(1)** Trois jugements élogieux sont cités : **Alexander Graham Bell** dit avoir vu en cette
enfant plus de divin qu'en quiconque avant elle ; **Maria Montessori** dit que les enfants de
l'avenir la comprendront encore mieux, car ils sauront comment l'esprit peut l'emporter sur les
sens ; **Mark Twain** la place à l'égal de César, Alexandre, Napoléon, Homère, Shakespeare et des
autres immortels, et prédit qu'elle sera aussi célèbre dans mille ans qu'aujourd'hui.

**(2)** À **19 mois**, Helen Keller perd définitivement la vue et l'ouïe, frappée par une maladie
mystérieuse ; elle devient sauvage, inatteignable. **Alexander G. Bell** recommande la **Perkins
Institution** de Boston, qui avait mis au point une méthode ayant réussi avec la sourde-aveugle
**Laura Bridgman**. Une jeune diplômée récente de Perkins, **Anne Sullivan, 20 ans**, relève le
défi. Chez les Keller, Sullivan, à la volonté de fer, gagne l'affection et l'obéissance de
l'enfant tout en s'acharnant à lui enseigner l'alphabet manuel. **En moins d'un mois** elle
réussit : c'est le moment fameux de la **pompe à eau**, où Helen sent l'eau sur une main et les
lettres **W-A-T-E-R** sur l'autre. Helen écrira plus tard qu'elle a quitté le puits avide
d'apprendre, et qu'en rentrant, chaque objet touché semblait « frémir de vie ».

**(3)** Une fois la porte ouverte, Helen ne peut plus se rassasier d'apprendre. Elle apprend à
écrire, et « Teacher » (Miss Sullivan) et elle passent joyeusement d'une matière à l'autre. Avec
Teacher, Helen étudie à la **Cambridge School for Young Ladies** puis à **Radcliffe College**.
Avec l'aide de Miss Sullivan et de l'enseignant de Harvard **John Macy**, Helen écrit son
autobiographie **The Story of My Life** — révélation saisissante de la vie riche qu'elle avait
conquise malgré ses sens émoussés ; le livre est largement médiatisé et bien reçu, jugé « unique
dans le monde de la littérature ».

**(4)** Après le diplôme, Helen et Teacher s'installent à **Wrentham, Massachusetts**. Anne
Sullivan épouse John Macy, étant entendu qu'Helen reste à sa charge permanente. Anne et John Macy
aident Helen pour son livre suivant, **The World I Live In** — autre succès.

**(5)** Helen soutient activement la **cause des aveugles** et le **droit de vote des femmes**
(*women's suffrage*) ; elle devient **socialiste** et écrit des tracts sur la justice sociale ;
avec Teacher elle fait des **tournées de conférences** à travers le pays. En **1913**, John Macy
se sépare d'Anne ; **l'année suivante**, **Polly Thomson** rejoint Helen et Teacher comme
secrétaire et gouvernante.

**(6)** Le monde d'Helen ne cesse de s'élargir : elle participe à des **rassemblements pour la
paix**, donne des conférences, se produit au **vaudeville**, tourne un film. Elle voyage beaucoup
pour **lever des fonds** au profit de l'**American Foundation for the Blind** ; elle fait du
**lobbying à Washington**. Après la mort d'**Anne Sullivan (1936)**, Polly Thomson devient
l'interprète et la compagne d'Helen. Elles visitent des **hôpitaux militaires pendant la Seconde
Guerre mondiale** et font un **tour du monde** pour la cause des aveugles.

**(7)** Devenue une figure mondiale, Helen Keller est le sujet d'un autre film, **The
Unconquered**, et d'une pièce, **The Miracle Worker** — tentatives de documenter une vie qui
témoignait des portées insondables de l'esprit humain.

##### Les questions (manuel p.69)

**C.** « What happened to Helen Keller ? When ? »
**D.** « Did she behave like a normal child ? Justify your answer with two details from paragraph
No.2. »
**E.** « Find out the words which have the same meanings as the following. »

| # | Définition imprimée | Corrigé (guide p.33) |
| --- | --- | --- |
| 1 | clear and obvious (§1) | **manifest** |
| 2 | tremble slightly / vibrate (§2) | **quiver** |
| 3 | story of a person's life written by himself (§3) | **autobiography** |
| 4 | surprisingly shocking (§3) | **startling** |
| 5 | vote / right of voting (§5) | **suffrage** |
| 6 | light comedy with songs and dances (§6) | **vaudeville** |
| 7 | that couldn't be understood (§7) | **unfathomable** |

**F.** « Helen Keller was a hard-working activist. Focus on paragraph No. 5 and paragraph No. 6 and
identify the different philanthropic activities in which she was involved. »
**G.** « Now that you have better ideas about Helen Keller's story, do you approve of those
opinions given in paragraph No.1 ? Justify your answer. »
**H.** « Complete. The Story of My Life, The World I Live In, The Unconquered and The Miracle
Worker are written in …………….. because they are …………….. »
→ **Corrigé (guide p.33)** : « H. **italics**. **titles**. » *(relation forme/ponctuation ↔ sens)*
**I.** « Tick the most appropriate alternative. A good title to the text could be : »
1. Helen Keller : The Unlucky Woman ( )
2. Helen Keller : Light in The Darkness ( )
3. Helen Keller : The Famous Actress ( )
→ **Corrigé (guide p.33)** : **2**

##### AFTER YOU READ — Writing (manuel p.70)

Consigne verbatim : « Choose one of Helen Keller's quotes from the list below. Refer to the
information given in the text and expand the quote into an article which you will contribute to
your school web site. »

**Les 4 citations proposées (manuel p.70)** :
1. « The best and most beautiful things in the world cannot be seen or even touched. They must be
   felt with the heart. »
2. « When one door of happiness closes, another opens; but often we look so long at the closed
   door that we do not see the one which has been opened for us. »
3. « Life is either a daring adventure or nothing at all. Security is mostly a superstition. It
   does not exist in nature. »
4. « I seldom think of my limitations, and they never make me sad. Perhaps there is just a touch
   of yearning at times; but it is vague, like a breeze among flowers. »

**Encadré « Helpful expressions » (manuel p.70) — verbatim :**

| Expressing contrast with what came before | Showing attitude | Explaining |
| --- | --- | --- |
| However, all the same, yet, And yet, still, on the other hand, In spite of / Despite | As a matter of fact, In fact, No doubt, | I mean, by ….. I mean, In other words, That is to say |

Clôture : « Remember to follow the steps suggested in the previous Writing Sections. »

---

## Fun page (manuel p.71)

Deux histoires drôles, séparées par le motif décoratif `•  / • •`.

**Blague 1 — The United Way and the richest farmer.**
Le bureau local de **The United Way** s'aperçoit qu'il n'a jamais reçu de don du fermier le plus
riche de la ville. Un bénévole l'appelle : « Our research shows that even though your annual
income is over a million dollars, you do not give one penny to charity ! Wouldn't you give back to
your community through The United Way ? » Le fermier réfléchit puis riposte en trois temps :
**premièrement**, la recherche a-t-elle montré que sa mère se meurt après une longue maladie
douloureuse, avec d'énormes factures médicales qu'elle ne peut payer ? (le représentant, gêné,
marmonne « Uh, no. ») ; **deuxièmement**, que son frère, ancien combattant handicapé, est aveugle,
cloué dans un fauteuil roulant et incapable de subvenir aux besoins de sa femme et de ses six
enfants ? (le représentant commence à balbutier des excuses mais est coupé) ; **troisièmement**,
que le mari de sa sœur est mort dans un affreux accident de la route, la laissant sans un sou avec
un crédit immobilier et trois enfants ? Le représentant humilié, complètement battu, dit
simplement : « I had no idea. » **Chute** : le fermier conclut — « …and if I don't give any money
to THEM, why should I give any to you ? »

**Blague 2 — The will.**
Un avocat lit le testament d'un homme riche aux personnes qui y sont nommées. À sa femme aimante
**Rose**, qui l'a soutenu dans les mauvais moments comme dans les bons, il laisse la maison et
**2 millions de dollars**. À sa fille **Jessica**, qui l'a soigné dans la maladie et a fait tourner
l'entreprise, il laisse le yacht, l'entreprise et **1 million de dollars**. **Chute** : à son
cousin **Dan**, qui le détestait, se disputait avec lui et pensait qu'il ne serait jamais
mentionné dans le testament — « well you are wrong. Hi Dan ! »

*(Lexique porté par la chute : le double sens de « mention in the will » et le simple salut.)*

---

## VOCABULARY COVERED IN MODULE 2 (manuel p.72) — liste intégrale

#### Common core

**Section one** (26 mots) :
activism · advancement · altruism · benevolence · charity · common good · contribution · devotion ·
donation · egoism · endowment · fund-raising · generosity · helpless · humanitarian · in-kind (adj) ·
meanness · needy · philanthropy · raise money · self-sacrifice · solicit · solidarity · voluntarism ·
volunteerism · welfare

**Section two** (23 mots) :
beneficiary · bequest · budget · burn · charge · cool · efficiency · ever-increasing · fainting ·
flow · grateful · in vain · injuries · mission · nest · network · orthopaedic · pediatric ·
research · run (sth) · state-of-the-art · walks of life · will (n)

**Section three** (25 mots) :
bathe · bond · bring out · clubbing · cute · dedicate · dwarfism · feet · genetic · give up ·
gossip · hero · homeless · milestone · party (v) · puberty · rescue · salute · shelter · stone ·
swap · take over · take turns · tragic · worldwide

**Section four** (9 mots) :
anecdote · commitment · consistently · dignity · essence · infrastructure · meet (a responsibility) ·
sustain (development) · well-being

**Section five.** *(le manuel imprime un point au lieu des deux-points)* (18 mots) :
abolish · advocate · assassination · character · civil rights · elect · enrol · harmony ·
impressed · ivory · march · metaphor · preach · protest · racial injustice · segregation ·
untiring · vote

#### Arts Supplement

**Section one** (17 mots) :
abuse · barriers · boundaries · famine · free verse · gangster · greed · illiteracy · offence ·
selfishness · shadow · sit-in · smell · sonnet · soul · symbolize · terror

**Section two** (35 mots) :
autobiography · blind · blunted · breeze · cause · challenge · daring · deaf · disability · dumb ·
immortals · interpreter · joyously · lobby · manifest · mysterious · paralytic · prevail · quiver ·
rallies · reach (n) · revelation · strive · struck · suffrage · superstition · testify ·
touch of (a) · tract · unfathomable · unique · unreachable · vaudeville · wild · yearning

*(Total : 101 items en tronc commun + 52 items Arts = 153.)*

**Écarts manuel ↔ guide relevés sur ces listes** :
- Section two : le manuel ajoute **ever-increasing**, absent de la liste du guide p.24.
- Section three : le manuel ajoute **feet**, absent de la liste du guide p.26.
- Arts section two : le manuel ajoute **lobby**, absent de la liste du guide p.32 ; et le manuel
  écrit **touch of (a)** là où le guide écrit **touch of (n)**.

---

## SELF-ASSESSMENT (manuel p.73)

**A.** « What progress do you feel you have made in English in this module ? Put a tick (√) in the
box that applies to you. » — grille à 3 colonnes : **YES / A LITTLE / NO**

1. I've used what I already know to learn more English
2. I can read a text and answer the questions correctly
3. I can listen to a text and answer the questions correctly
4. I've learnt how to converse in English
5. I am using the grammatical structures I've learnt
6. I understand grammar but I cannot use the structures correctly
7. I can remember the words I've come across
8. I recognize the words but I cannot use them
9. I've learnt how to write in English
10. The writing activities are difficult
11. I've shared ideas with my classmates and my teacher
12. My pronunciation has improved
13. I've learnt how to conduct a mini-project
14. My English has improved

**B.** « What did you like most in this module ? Tick the answer(s) that apply(ies) to you. »
- The topics
- The activities
- The projects
- Listening to the cassette
- Acting out situations
- The writing activities
- The Reading skills
- The grammar exercises
- The vocabulary exercises
- Working in groups

**C.** « Circle the alternative that applies to you : I still need to work on : »
Reading / Listening / Speaking / Writing / Vocabulary / Grammar

---

## Tapescripts du module

#### Tapescript 1 — « Module two. Section two : Listening » (guide p.78)

Discours prononcé par un **représentant régional de Hope Organization** devant un séminaire.
Découpé en **4 parties numérotées (1) à (4)** dans le guide, ce qui correspond aux exercices A à F
du manuel (parties two et three explicitement exploitées).

**Partie (1) — salutation, accroche, présentation de l'organisation**
> Good afternoon.
> Before I begin, and as a regional representative of Hope Organization, I would like to convey the
> greetings of our organization president who wishes this seminar every success.
> There's an old saying that goes, « we do not inherit the earth from our parents, we borrow it
> from our children. » I think this is a good reminder of how we must always provide for our future
> generations.
> We come from all walks of life. We are doctors, farmers, actors, mechanics, shopkeepers,
> businessmen, singers, teachers, lawyers, sportsmen and students.
> Hospitals for children is our official philanthropy. Thus raising funds to support our hospital
> system is our key mission.

**Partie (2) — réalisations, chiffres, origine de l'argent** *(base du texte à trous D.1)*
> Our Hope Organization opened its very first hospital back in 1970, and today there is a national
> network of 12 hospitals that provide highly expensive, **specialized** medical care to children
> with **orthopaedic** problems or **burn** injuries – all at no **charge** to the patient.
> In **2002** alone there were over 5,000 patients receiving care at our hospitals.
> That's a lot of smiling little faces and **grateful** moms and dads.
>
> You may be wondering where we get the money from to keep our hospitals running.
> The majority comes from our hospitals' Endowment Fund, whose revenues finance about 80 percent of
> the hospitals' operating and research budgets.
> The gifts and fund-raising events are other operating revenue sources.

**Partie (3) — efficacité, contre-argument et réfutation, forme emphatique** *(base de E et F)*
> Our philanthropy is one of the purest anywhere. By that, I mean about 93 percent of our hospitals
> budget is used for patient care and research and only about 8 percent for administrative and
> fund-raising costs.
>
> Compare these figures with any other charity and you'll see the efficiency of a well-run
> philanthropy.
> A lot of people probably think that our hospitals don't need any more money.
> Well, the truth is, that's not the case.
> Our hospital system **DOES** need more money and **NOW** is the time when we must work harder to
> gain financial support from the public.
> (We've got to continue to raise funds in support of our hospital system to meet the
> ever-increasing costs of modern medical care.
> We need to continue to maintain our pediatric healthcare facilities at state-of-the-art levels.
> *(la parenthèse ouvrante n'est jamais refermée dans la source — voir Incertitudes)*

**Partie (4) — appel à l'action et clôture**
> We must keep contributions flowing in.
> These contributions may be in the form of bequests through endowments, wills and gifts from
> individuals, corporations or foundations.
> Thank you for your time.

**Ancrages pédagogiques du tapescript** : *walks of life* · *official philanthropy / key mission* ·
adjectifs composés (*state-of-the-art, well-run, ever-increasing, fund-raising*) · forme emphatique
(**DOES**, **NOW**) · lexique du financement (*Endowment Fund, revenues, operating and research
budgets, gifts, bequests, wills*) · lexique médical (*orthopaedic, burn injuries, pediatric*).

#### Tapescript 2 — « Ebony And Ivory » (guide p.79)

> **Paroles non reproduites (R-2).** Chanson créditée dans le guide à **Paul Mc Cartney** et
> **Steve Wonder** [sic]. Le tapescript donne la version complète : le distique d'ouverture
> (métaphore des touches noires et blanches vivant en parfaite harmonie côte à côte sur le clavier,
> suivi d'une interpellation « why don't we ? »), un couplet répété trois fois (les gens sont les
> mêmes partout, il y a du bon et du mauvais en chacun, on apprend à vivre et à se donner ce qui
> est nécessaire pour survivre ensemble), le pont « Ebony, Ivory, Ooh », la reprise du distique, une
> variante raccourcie de ce distique, puis **quatre reprises identiques** de la formule finale
> « Ebony, Ivory living in perfect harmony ».
> **Différence avec l'extrait du manuel p.59** : le manuel ne donne que le distique d'ouverture et
> le couplet (8 lignes), sans les reprises, et imprime « There's » là où le tapescript imprime
> « There is ».

#### Tapescript 3 — « Catch the fire » (guide p.80-81)

> **Poème non reproduit (R-2).** Le guide donne le texte intégral du poème de la section Arts one,
> identique à celui du manuel p.63-64. **Différences relevées entre les deux impressions** :
> - guide : « not dying / not killing / not gangster shadows » en minuscules ; manuel : « Not
>   dying / Not killing / Not gangster shadows » avec majuscule initiale ;
> - guide : « Sister *.Brother* » porte des astérisques (appels de note dont les notes ne figurent
>   pas dans l'extrait) ; manuel : « Sister . Brother . » sans astérisques ;
> - guide : dernier vers « Catch the fire …………………. **And** live. » ; manuel : « … **and** live. » ;
> - signature : guide « **Sonya** Sanchez » ; manuel « **SONIA** SANCHEZ » + mention de source
>   « From African American Women in Literature » (absente du guide).
> Le manuel indique en outre l'activité d'écoute correspondante (Arts section one, question 8 :
> « Now, listen then volunteer to read the poem aloud… »).

*(Aucun tapescript n'est fourni pour la section four Speaking ni pour la section five au-delà de la
chanson : la section four est productive, la section five ne comporte que l'écoute de la chanson.)*

---

## Incertitudes (module 2)

1. **Anomalie du guide p.32 — CONFIRMÉE.** L'en-tête imprimé « **Section Four : Speaking** » à la
   page 32 du guide est **erroné** : cette page traite en réalité **« Arts. Section Two : READING
   ABOUT GREAT PEOPLE »** (manuel p.67-70). Cinq preuves convergentes : (a) sa liste de vocabulaire
   (autobiography, blind, blunted, breeze, cause, challenge, daring, deaf, disability, dumb,
   immortals, interpreter, joyously, manifest, mysterious, paralytic, prevail, quiver, rallies,
   reach(n), revelation, strive, struck, suffrage, superstition, testify, touch of(n), tract,
   unfathomable, unique, unreachable, vaudeville, wild, yearning) reproduit **exactement** la
   colonne « Arts Supplement — Section two » du manuel p.72 (à *lobby* près) ; (b) son skill
   « provide a title for the text (from alternatives suggested) » correspond à l'exercice **I** du
   manuel p.69 ; (c) son skill « apply the writing process strategies to expand a quote into an
   article » correspond au **AFTER YOU READ** du manuel p.70 ; (d) ses Helpful notes renvoient
   explicitement à « the suggested expressions (**page 70**) », c'est-à-dire l'encadré *Helpful
   expressions* du manuel p.70 ; (e) l'Answer key de la page suivante (guide p.33) corrige
   **A. 1+see, 2+deaf, 3+dumb, 4+move**, **E. 1+manifest … 7+unfathomable**, **H. italics/titles**,
   **I. 2** — soit exactement les exercices A, E, H, I du manuel p.67-69. **Conséquence** :
   l'en-tête « Section Four : Speaking » apparaît **deux fois** dans le guide (p.28, correcte, pour
   la Speaking du tronc commun ; p.32, fautive, pour la section Arts two). Le vrai en-tête de la
   p.32 devrait être « Arts. Section Two : Reading about great people ».
2. **Encadré Exploring grammar (manuel p.53 et guide p.27)** : l'exemple « She has done so since
   she was five » figure en **colonne B (simple past)** alors qu'il est au **present perfect** et
   qu'il figure déjà, sous la forme « …and has done so since she was five », en colonne A. Erreur
   présente dans **les deux** sources — à ne pas reproduire dans le contenu généré.
3. **Corrigé grammaire, guide p.27, exercice 2** : le guide imprime « **have invited** » alors que
   l'énoncé du manuel p.54 porte « they (**visit**) each other almost everyday ». Lire
   « **have visited** » ; coquille du guide.
4. **Note de bas de page du manuel p.51** : « * 3 1/2 st . 2 stone = 12.7 kilograms » — la note
   définit **2 stone** alors que le texte parle de **3 stone ½** ; l'équivalence donnée (2 st =
   12,7 kg) est exacte, mais elle ne convertit pas la valeur du texte (3,5 st ≈ 22,2 kg). Incohérence
   de la source, conservée telle quelle.
5. **Chiffres du tapescript (guide p.78) et exercice C (manuel p.48)** : « about 93 percent … and
   only about 8 percent » — **93 + 8 = 101**. Incohérence arithmétique de la source ; le manuel
   n'interroge que sur 93 %.
6. **Parenthèse non refermée** dans le tapescript (guide p.78, partie 3) : « (We've got to continue
   to raise funds… at state-of-the-art levels. » — la parenthèse ouvrante n'a pas de fermeture.
   Impossible de savoir si le passage est optionnel à l'écoute ou s'il s'agit d'une coquille.
7. **Contenus visuels absents de la couche texte** — non transcriptibles : les photos et cartouches
   de citations du manuel p.43 (dont l'image « old lady + Meriam ») ; **l'annonce UNICEF signée
   Carol Bellamy** (manuel p.56) dont seul l'énoncé des questions est disponible — le guide p.28
   compense partiellement en donnant le contenu attendu ; les **9 photos** du manuel p.56-57
   (compensées par la description du guide p.28) ; la photo de la marche de Washington (manuel
   p.59-60) ; la photo légendée « Helen Keller » (manuel p.68) ; le spidergram et le tableau des
   suffixes ont en revanche été restitués intégralement.
8. **Maquette de la chronologie MLK (manuel p.61)** : plusieurs flèches de liaison ont disparu à
   l'extraction (« enrol [→] Boston University », « new local and state laws [→] to abolish
   segregation », « Time magazine [→] Man of the Year », « Congress [→] pass the Voting Rights
   Act », « Many blacks [→] to vote for the first time », « black leaders [→] elected to important
   offices »). Les mentions marginales « (1940's) » et « 1960's » sont imprimées en marge de blocs
   datés respectivement « 1930s » et « 1950's » — leur rôle exact dans la maquette (bornes de
   décennie ?) reste incertain.
9. **Ordre des réponses de *As you listen* A (guide p.25 : « 3, 1, 4, 2 »)** : l'item « urges for
   harder work to get more contributions and financial support » reçoit le rang **4**, alors que
   l'exhortation à travailler plus dur (« NOW is the time when we must work harder ») se trouve dans
   la **partie 3** du tapescript ; la partie 4 se limite à l'appel à maintenir les contributions.
   Corrigé conservé tel qu'imprimé.
10. **Coquilles de source relevées** (transcrites telles quelles) : guide p.21 « ModuleTwo » ·
    guide p.24 « Pronuncition » · guide p.25 « wordsthat » et « Intonation patters » ·
    guide p.27 « 9+I » (pour 9+i) · guide p.31 « sit in » (pour sit-in) · guide p.81 « Sonya
    Sanchez » · manuel p.42 « read a poem » imprimé deux fois (probablement volontaire : deux poèmes,
    Dickinson en section two et *Catch the fire* en Arts one) · manuel p.44 « why ? or why not ? » ·
    manuel p.50 « Dyggve-Melchior-clausen » (minuscule) · manuel p.51 « the **Johnstons** » vs
    « The **Johnsons** » p.53 · manuel p.52 transcription phonétique tronquée `/dw_f/` (lire
    /dwɔːf/) · manuel p.59 et guide p.79 « Steve Wonder » (pour *Stevie* Wonder) et « Paul Mc
    Cartney » · manuel p.61-62 en-tête « **Session** five » (pour *Section* five) · manuel p.67
    « Helen **k**eller » · manuel p.72 « Section five. » (point au lieu de deux-points).
11. **Œuvres sous droits (R-2)** : *Ebony and Ivory*, *Catch the fire* et le poème d'Emily
    Dickinson ne sont **jamais** reproduits ici. Toute génération de contenu (cours, quiz,
    exercices) doit s'appuyer sur les descriptions structurelles et thématiques données plus haut
    et sur les **questions du manuel**, sans jamais citer de vers ni de paroles. Le contenu exact de
    la phrase de Martin Luther King (manuel p.59) est restitué par le sens pour la même raison.

### Consolidation Module 1 (manuel p.74–79 · guide p.34–35)

**Statut** : module de consolidation placé **après les modules One et Two**, dont il recycle les deux
thèmes (rôles familiaux · philanthropie) et toute la langue. Le guide ne lui donne **ni « Scope and
sequence » ni « Helpful notes »** — uniquement le corrigé, activité par activité. Consigne unique du
manuel (p.74) : « Do the following activities. » **Treize activités.**

#### Activity 1 (manuel p.74) — lexique en contexte (rôles dans la famille)

« Fill in the blanks with the following words. » Banque de **12** mots pour **12** trous : _expected,
understanding, members, within, responsibilities, household, overburdened, fulfill, assigned, arise,
assistance, required._ Texte : dans une famille saine, chacun assume certains rôles répartis entre
les membres pour que personne n'en porte trop ; des problèmes surgissent si un membre est forcé d'en
tenir trop — exemple des mères qui travaillent à plein temps et doivent en plus s'occuper des enfants
et de l'essentiel des tâches ménagères avec peu d'aide ; il importe de discuter en famille de la
compréhension qu'a chacun des rôles qui lui sont assignés ; si quelqu'un se sent surchargé et
incapable de tenir un rôle, des changements sont nécessaires ; dans les familles saines les enfants
sont incités à prendre des responsabilités adaptées au sein de la famille.

_Corrigé du guide (p.34)_ : 1. members · 2. responsibilities · 3. arise · 4. fulfill · 5. expected ·
6. household · 7. assistance · 8. understanding · 9. assigned · 10. overburdened · 11. required ·
12. within.

#### Activity 2 (manuel p.74) — formation des mots (12 dérivations)

« Put the words in brackets in the appropriate form. » Texte sur la clarté des rôles familiaux : les
membres doivent connaître et reconnaître leurs rôles ; les parents doivent fournir des ressources
matérielles (nourriture, vêtements, abri), de la discipline et un environnement soutenant et
nourrissant qui facilite le développement physique et affectif des enfants ; les familles en
difficulté ont souvent des rôles mal définis ; établir des rôles clairs aide la famille à mieux
fonctionner ; si des individus manquent à leurs rôles, d'autres doivent en faire plus, se sentent
pleins de ressentiment et surchargés, ce qui nuit au fonctionnement de la famille.

Les 12 mots entre parenthèses, dans l'ordre : _(health)_, _(understand)_, _(support)_, _(facility)_,
_(develop)_, _(difficult)_, _(they)_, _(good)_, _(establish)_, _(effective)_, _(make)_, _(hurt)_.

_Corrigé du guide (p.34)_ : 1. healthy · 2. understanding · 3. supportive · 4. facilities ·
5. development · 6. difficulties · 7. their · 8. well · 9. Establishing · 10. effectively ·
11. making · 12. hurting.

#### Activity 3 (manuel p.75) — collocations verbe + complément

« Match the words in column A with the words in column B to get meaningful expressions. Write your
answers in column C. »

| A               | B                |
| --------------- | ---------------- |
| 1. take out     | a. discipline    |
| 2. make         | b. a problem     |
| 3. maintain     | c. decisions     |
| 4. provide      | d. of children   |
| 5. take care    | e. affection     |
| 6. overcome     | f. the trash     |

_Corrigé du guide (p.34)_ : 1+f · 2+c · 3+a · 4+e · 5+d · 6+b — soit _take out the trash · make
decisions · maintain discipline · provide affection · take care of children · overcome a problem_.

#### Activity 4 (manuel p.75) — ponctuation et majuscules

« Punctuate and capitalize where necessary. » Texte non ponctué sur **Paul Cuffe**, séparatiste noir
américain des débuts, fils d'un père esclave africain ayant racheté sa liberté et d'une mère indienne
de Nantucket, devenu marin et propriétaire foncier important, qui consacra sa fortune à la
philanthropie et à la réinstallation d'Afro-Américains en Sierra Leone.

_Corrigé du guide (p.34)_, verbatim : « Paul Cuffe was an early American black separatist. Son of an
African slave father who had purchased his freedom and a Nantucket Indian mother, he became a seaman
and a substantial property owner. Cuffe devoted his wealth to philanthropy and resettling African
Americans in Sierra Leone. »

#### Activity 5 (manuel p.75) — remise en ordre (Andrew Carnegie)

« Reorder the following sentences / sentence parts to get a coherent paragraph. **No.1 has been done
for you.** » Six segments, celui numéroté 1 étant donné :

- ( ) _donating over $ 350 million to various causes._
- ( ) _the Carnegie Endowment for International Peace, and the Carnegie Corporation of New York._
- ( **1** ) _Carnegie sold his company to J.P. Morgan's United States Steel Company in 1901_
- ( ) _Carnegie established more than 2,500 libraries_
- ( ) _and until his death devoted himself to philanthropy,_
- ( ) _and founded (1901-11) the Carnegie Institute of Pittsburgh, the Carnegie Institution at
  Washington, the Carnegie Foundation for the Advancement of Teaching,_

_Corrigé du guide (p.34)_ : « (3), (6), (1), (4), (2), (5) » — c'est-à-dire, dans l'ordre où les
segments sont imprimés ci-dessus, leurs rangs respectifs : le 1ᵉʳ segment imprimé vient en 3ᵉ
position, le 2ᵉ en 6ᵉ, le 3ᵉ en 1ʳᵉ, le 4ᵉ en 4ᵉ, le 5ᵉ en 2ᵉ, le 6ᵉ en 5ᵉ. Ordre de lecture
reconstitué : _Carnegie sold his company… (1)_ → _and until his death devoted himself to
philanthropy, (2)_ → _donating over $ 350 million to various causes. (3)_ → _Carnegie established
more than 2,500 libraries (4)_ → _and founded (1901-11)… (5)_ → _the Carnegie Endowment… (6)_.

#### Activity 6 (manuel p.76) — simple past vs present perfect

« Put the bracketed verbs in the simple past or the present perfect. » Deux dialogues.

**1.** « – Have you seen Bill lately ? – The poor chap's ill. As a matter of fact, he (be) …… in
hospital for the last three weeks. He (fall) …… off a ladder while painting his new house. He
(be/take) …… to hospital where he (spend) …… a week. Unfortunately, he (not/recover) ……
completely, yet. »

**2.** « – Don't you think it's high time we (plan) …… something different for the holiday ? – Why
should we ? We (spend) …… our vacations in the same place ever since we (get) …… married and you
(always/enjoy) …… it. – Yes, but we (be) …… married for 20 years and in those years my tastes
(change) …… »

_Corrigé du guide (p.34)_ :
**1.** has been, fell, was taken, hasn't recovered yet.
**2.** planned, have spent, got, have always enjoyed, have been married, have changed.
⚠️ Le corrigé ne donne que **six** formes pour la partie 2, dont la première (« planned ») correspond
au `(plan)` de « it's high time we (plan) » — c'est l'emploi du **simple past après `it's (high)
time`** rappelé au Grammar summary (manuel p.209).

#### Activity 7 (manuel p.76) — transformations imposées

« Start with the words given and make the necessary changes. »

1. _I'm sorry I don't have enough money to donate._ → « I wish ………… »
2. _Parents have to be understanding; otherwise they may have communication problems with their
   children._ → « If parents ………… »
3. _Shall I phone you at 3 pm?_ → « No. I'd rather you …… at 4 instead. »
4. _Some parents don't allow their children to have their own way._ → « Some parents don't let …… »

_Corrigé du guide (p.34)_, verbatim :
1. « I wish I had enough money to donate »
2. « If parents aren't understanding they may have communication problems with their children. »
3. « I'd rather you phoned at 4 instead. »
4. « Some parents don't let their children have their own way. »

(Quatre structures : `wish` + prétérit modal · `if` + présent + `may` · `would rather` + prétérit
modal · `let + object + base form`.)

#### Activity 8 (manuel p.77) — mots croisés

« Complete the following crossword puzzle. » Grille numérotée, définitions imprimées de part et
d'autre.

**Across** — 1. _burdened too heavily_ · 3. _laugh (verb) ………… (noun)_ · 6. _provide regular income
(especially for institutions)_ · 7. _help or kindness to somebody who is suffering_ · 8. _Force or
influence exerted on someone or something_ · 9. _give voluntarily_.
**Down** — 2. _person who offers to do something_ · 4. _not instrumental but ……………_ · 5. _the
practice of actions (protests, demonstrations) to achieve goals_ · 7. _help to the poor (money, food,
etc)_.

_Corrigé du guide (p.35)_ — Across : 1. overburdened · 3. laughter · 6. endow · 7. comfort ·
8. pressure · 9. donate. Down : 2. volunteer · 4. affective · 5. activism · 7. charity.

#### Activity 9 (manuel p.77–78) — phrasal verbs (16 items)

« Fill in the blanks with the appropriate form of the following phrasal verbs. » Banque de **16**
verbes à particule : _flow in, pick up, decide on, take over, grow up, dream of, bring out, look
after, set off, turn out, gossip about, give up, provide for, gaze at, look for, catch up._ Chaque
phrase porte une **glose de sens entre parenthèses**, ce qui en fait un exercice de discrimination
sémantique :

1. « Will you please hurry up and ……… a precise work to do. » _(make a judgement)_
2. « She ……… me for a moment and then smiled. » _(look fixedly)_
3. « I hope everything ……… all right. » _(end in a particular way)_
4. « Please help me ……… this guy ……… from the ground. He passed out and fell down. » _(lift up or raise)_
5. « Mrs. Franklin is ……… by her husband's irresponsible behaviour. » _(cause someone to become very angry)_
6. « I am ……… Mr. William Wilson. Do you know where he lives ? » _(seek someone)_
7. « I ……… owning a big house and travelling round the world. » _(have a fantasy of doing something)_
8. « A thoughtful and responsible father ……… the different needs …… his children. » _(supply the needs of someone)_
9. « After the tsunami tragedy, donations ……… from different parts of the world. » _(come from)_
10. « This kind of situation doesn't exactly ……… the best in me. » _(cause someone to behave in the best manner)_
11. « It is not in my nature to ……… people. » _(talk maliciously about someone or something)_
12. « Will you ……… my cat while I'm away. » _(take care of)_
13. « When children ……… , parents should be careful how to deal with them. » _(become mature)_
14. « Jane ……… coffee ……… because of the caffeine. » _(stop using / eating)_
15. « My boss is not happy with me. I have to ……… and become more productive. » _(do the work that one should have done)_
16. « When Mr Green retired, his son ……… the business. » _(assume control of / responsibility for)_

_Corrigé du guide (p.35)_ : 1. decide on · 2. gazed at · 3. turns out · 4. pick … up ·
5. set off · 6. looking for · 7. dream of · 8. provides … for · 9. flowed in · 10. bring out ·
11. gossip about · 12. look after · 13. grow up · 14. gave … up · 15. catch up · 16. took over.

⚠️ **Divergence relevée** : la glose de l'item 5 est _(cause someone to become very angry)_ et le
corrigé donne « **set off** » — un emploi de `set off` (« déclencher, faire sortir de ses gonds »)
qui n'est pas celui qu'on attendrait de la banque. Transcrit tel quel ; voir §6.

#### Activity 10 (manuel p.78) — modaux

« Complete with : should have, need, must, may, should, shall. » Neuf phrases : 1. la grand-mère
handicapée qui « ……… somebody who looks after her all day long » · 2. « "You ……… obey me", says an
authoritarian father to his child. » · 3. « We ……… give help to needy people no matter who they
are. » · 4. « I ……… thought we would expect more people to come to the party. » · 5. « If it rains I
……… stay at home. » · 6. « I hope that I ……… succeed. » · 7. « Melanie was selfish. She ……… helped
her little brother with his English homework. » · 8. « You look pale. You ……… to see a doctor. » ·
9. « People ……… think that I'm rich enough to help everybody. The reality is that I'm not. »

_Corrigé du guide (p.35)_ : 1. needs · 2. must · 3. should / must · 4. should have · 5. shall ·
6. shall · 7. should have · 8. must · 9. may.

⚠️ Le corrigé donne « **must** » à l'item 8 (« You look pale. You must to see a doctor. ») alors que
la phrase imprimée porte « to see » : la forme attendue par la phrase est **`need to`**
(« you need to see a doctor »). Divergence corrigé ↔ énoncé, voir §6.

#### Activity 11 (manuel p.78–79) — mots à compléter (Helen Keller)

« Complete the unfinished words. » Texte biographique lacunaire sur **Helen Keller (1880-1968)**,
« the legendary d…… and d…… writer and spokesperson of many cases » : perte de la vue et de
l'ouïe à 19 mois à la suite d'une maladie ; Anne Sullivan lui apprend à communiquer par la langue des
signes puis à écrire et à parler, lui ouvrant l'accès à l'éducation ; récit de son expérience à
Radcliffe College où elle est diplômée en 1904 ; usage de sa notoriété au service de causes libérales
(droit de vote des femmes, contrôle des naissances) ; conférencière de renommée internationale, avec
un voyage au Japon ; **Medal of Freedom**, « the hi……… honor that can be conferred on a civilian ».

_Corrigé du guide (p.35)_ : deaf, dumb, sight, hearing, communicate, talk, experiences, graduated,
accomplishments, causes, engagements, awarded, highest.

#### Activity 12 (manuel p.79) — appariement de segments (Bathany Starkey)

« Match the sentence parts in A with their completions in B so as to get a coherent paragraph.
**There is an extra item in B.** » Sept amorces (A) pour huit compléments (B) — un intrus :

**A** — 1. _A five-year old girl was deeply_ · 2. _She arranged for all her birthday money_ ·
3. _Bathany Starkey asked all her friends to give her money_ · 4. _Then she donated the whole lot,_ ·
5. _Bathany was watching a documentary_ · 6. _Her wonderful generosity highlights exactly_ ·
7. _The fact that a young girl could be moved to help in such a way_
**B** — a) _about the tsunami and decided she really wanted to help._ · b) _instead of presents for
her fifth birthday._ · c) _moved by devastating pictures of tsunami victims._ · d) _perhaps other
readers could do the same._ · e) _which amounted to £ 206.50, to the charity._ · f) _brought a few
tears to people's eyes in the studio._ · g) _to be donated to the appeal through UK Radio Aid._ ·
h) _what UK Radio Aid was all about._

_Corrigé du guide (p.35)_ : 1+c · 2+g · 3+b · 4+e · 5+a · 6+h · 7+f. **L'intrus est donc `d)`.**

#### Activity 13 (manuel p.79) — tableau de dérivation

« Complete the table. » Tableau à trois colonnes _Verb / Noun / Adjective_, chaque ligne n'ayant
qu'une case remplie. Les amorces imprimées, dans l'ordre des lignes : _(noun)_ **food** ·
_(verb)_ **cooperate** · _(noun)_ **decision** · _(adj)_ **voluntary** · _(verb)_ **grow** ·
_(noun)_ **behaviour** · _(adj)_ **expected** · _(verb)_ **frustrate** · _(noun)_ **charity** ·
_(adj)_ **satisfactory** · _(noun)_ **philanthropy** · _(verb)_ **sacrifice** — soit **12 lignes**.

_Corrigé du guide (p.35)_, tel qu'imprimé (`xxxxxxxxxxxxxx` = case laissée vide par le guide) :

| Verb           | Noun                     | Adjective                                |
| -------------- | ------------------------ | ---------------------------------------- |
| feed           | food                     | fed                                      |
| decide         | decision                 | decided                                  |
| volunteer      | volunteerism/voluntarism | voluntary                                |
| grow           | growth                   | grown                                    |
| behave         | behaviour                | behaved (in compounds) / behavioural     |
| expect         | expectation / expectedness | expected / expectable                  |
| frustrate      | frustration              | frustrated / frustrating                 |
| xxxxxxxxxxxxxx | charity                  | charitable                               |
| satisfy        | satisfaction             | satisfied / satisfying / satisfactory    |
| xxxxxxxxxxxxxx | philanthropy             | philanthropic                            |
| sacrifice      | sacrifice                | sacrificed / sacrificial                 |

⚠️ **Divergence structurelle** : le corrigé ne compte que **11 lignes** et **ne traite pas la ligne
`cooperate`** du manuel. Voir §6.

### Module Three — A CHANGE IS AS GOOD AS A REST (manuel p.80-106 · guide p.36-44)

**Sources** : manuel élève 241303 « Activate and Perform — Third Year Secondary Education, Student's Book », p.80 à 106 ; guide enseignant 641303 « Activate and Perform — Teacher's Book », p.36 à 44 + tapescript p.82.

**Portée** : les sections One à Five sont le **tronc commun** (les six sections de 3ème année). Les pages 96 à 103 du manuel forment le **supplément ARTS**, imprimé en rose dans le manuel et réservé à la **filière Lettres** (« The items in pink are specific to the Arts branch »). La frontière est marquée explicitement ci-dessous.

---

##### Chapeau du module

**Titre du module (manuel p.80)** : Module Three — A CHANGE IS AS GOOD AS A REST

**Topic (guide p.36)** : Entertainment

**Subtopics (guide p.36)** : Travel – holidays – leisure activities – eating out - facilities history and geography of places visited

> Transcription littérale de la cellule du guide. La ponctuation de la source est bien celle-ci : le tiret et l'absence de virgule entre « eating out » et « facilities » sont dans l'imprimé (guide p.36).

**Cross-curricular learning goals (guide p.36)** : problem solving, critical thinking, efficient use of data, efficient working procedure, appropriate self-expression, ICT use, project work, communicating, working and living with others.

**Expected learning outcomes (manuel p.80)** — encadré verbatim :

> Expected learning outcomes :
> In this module, I'm going to
> - use what I already know to acquire new words and ideas about travelling and entertainment
> - listen to a radio ad
> - read a narrative text about a personal experience
> - read a magazine article
> - read an informative text
> - learn and practise lexical and grammatical items
> - take part in an interview
> - write a letter of complaint
> - write a report based on a conducted survey

**Grammaire du module (par section, d'après le « Scope and sequence » du guide)**

| Section | Grammar |
| --- | --- |
| One — Introductory activities (guide p.37) | Comparatives and superlatives |
| Two — Listening (guide p.39) | Prepositions |
| Three — Reading (guide p.40) | The past / the past perfect |
| Four — Speaking (guide p.41) | WH questions ; reporting answers |
| Five — Writing (guide p.42) | linkers |
| ARTS Section One (guide p.43) | Might / could + bare infinitive |
| ARTS Section Two (guide p.44) | The passive |

**Pronunciation** : Vowels / Diphthongs (guide p.39, Section Two uniquement — aucune autre section du module ne porte de rubrique Pronunciation).

**Project work / Mini-project (guide p.37, manuel p.83)** : Conducting a survey / writing a report — enquête sur les loisirs préférés des adolescents en Tunisie, graphique + court rapport à conserver au portfolio et à présenter en fin de module.
Un second travail d'enquête existe, mais **uniquement en filière Lettres** : le sondage sur les habitudes alimentaires de la classe (manuel p.102-103, guide p.44 « Writing – produce a report »).

**Homework recensés dans le guide**
- Section Three (guide p.40) : « Homework : language exercise (the past / the past perfect) » → l'exercice de la conversation Gary/Jean, manuel p.91.
- ARTS Section One (guide p.43) : « Doing internet research » → manuel p.98.
- ARTS Section Two (guide p.44) : « Homework : multiple choice alternatives (passive/active sentences) » → manuel p.103.

---

##### Section One : Introductory activities (manuel p.81-83 · guide p.37-38)

###### Scope and sequence (guide p.37) — verbatim

**Skills/subskills and strategies**
> **Speaking**
> - express opinion about a specific topic
> - make statements about facts
> - produce descriptions
>
> **Reading**
> - use the strategy appropriate to the nature of text/purpose of reading
> - match activities with pictures
> - transfer information onto a table
> - identify the communicative value of pictures
> - categorize ideas/information
> - evaluate and react to content
>
> **Writing:**
> - produce an outline/a table
> - produce a short ad using an outline

**Vocabulary (guide p.37)** : canoeing – harbour cruising – roller skating – dog sledge riding – safari – sightseeing – sunbathing – surfing – water skiing – resorts – luscious food – wild life – honeymoon - accomodation [sic]

**Grammar** : Comparatives and superlatives
**Functions** : - describing pictures related to a specific topic area - expressing opinion - comparing attitudes
**Mini-project** : Conducting a survey/writing a report

###### Activity 1 (manuel p.81)

**1. Match the activities with the pictures.**

Banque de mots imprimée (12 activités, dans l'ordre de la source) :

> surfing, harbor cruising [sic — « harbour » ailleurs dans le manuel p.106 et dans le guide p.37], safari, cycling, canoeing, water skiing, roller skating, sunbathing, hiking, sky diving, sightseeing, dog sledge riding

12 images numérotées de 1 à 12 disposées en 4 rangées de 3 (1-2-3 / 4-5-6 / 7-8-9 / 10-11-12). Les images elles-mêmes ne sont pas dans la couche texte ; leur contenu est entièrement déterminé par le corrigé du guide ci-dessous.

**Corrigé (guide p.38)** :

| Image | Activité |
| --- | --- |
| 1 | cycling |
| 2 | skydiving |
| 3 | surfing |
| 4 | sightseeing |
| 5 | sunbathing |
| 6 | harbour cruising |
| 7 | canoeing |
| 8 | roller skating |
| 9 | safari |
| 10 | water skiing |
| 11 | dog sledge riding |
| 12 | hiking |

**2.** « According to you, which activity is the easiest ? Which activity is the most interesting? Ask your classmate similar questions using the following adjectives : »

Adjectifs imprimés : **exciting – safe – expensive – dangerous – amusing – risky**

C'est l'activité qui installe le point de grammaire de la section (comparatifs / superlatifs).

**3.** « Work in groups of four and decide which activities are fit for : »
- a- a honeymoon couple
- b- a group of teenagers
- c- a retired couple

**Helpful notes (guide p.37) — Activity 1** :
> You may ask your students additional questions about the pictures such as:
> - Have you ever practised such activities?
> - Which activities are/are not available in Tunisia?
> - Why/when do people take up these activities?

*Pas de corrigé pour 1.2 et 1.3 dans le guide (activités d'expression libre).*

###### Activity 2 (manuel p.82-83)

**1. Complete the table with the appropriate information from the ads below.**

Tableau à deux colonnes, vide dans le manuel :

| Holiday destinations | Holiday activities |
| --- | --- |
|  |  |

**Les six annonces publicitaires imprimées (manuel p.82)** — textes non littéraires, reproduits car ils sont la donnée même de l'exercice :

1. **Do it yourself** — « We provide the camper van, maps and advice, and you go your own way, discovering the America you want to discover. »
2. **Movies come to life** — « Come to Florida, home of Disney World. Enjoy its warm sandy beaches. Visit Universal Studios where "movies come to life" »
3. **White Water Magic** — « If you are a confirmed sportsman or sportswoman, spend an exciting two weeks with us canoeing in the beautiful Rocky Mountains. »
4. **New York, New York** — « Spend two weeks in exciting New York City.Theater, dance, opera, museums,… » [sic : espace manquante après « City. »]
5. **HAWAII** — « You will never forget the warm welcome of Hawaii. Beautiful sunny beaches, friendly people, luscious food… »
6. **Float Along** — « Enjoy beautiful Texas scenery and wildlife while relaxing on a raft down the Rio Grande. Comfortable tent accommodation at night. »

**2.** « Work in groups and produce a similar table about Tunisia. » (manuel p.83)

**3.** « Use the information in the table to write short ads about holiday resorts in Tunisia. » (manuel p.83)

**Helpful notes (guide p.37) — Activity 2** : « Let the students read the ads silently then fill in the table in pairs. »

*Pas de corrigé dans le guide.* Le tableau attendu se déduit directement des annonces (destinations : America / camper-van tour, Florida, Rocky Mountains, New York City, Hawaii, Texas–Rio Grande ; activités : self-drive touring, beaches + Universal Studios, canoeing, theatre-dance-opera-museums, beaches + food, rafting + camping).

###### Activity 3 (manuel p.83)

**1.** « look at the chart below.It represents the top leisure activities for adult people in USA. » [sic : minuscule initiale et espace manquante après le point]

⚠️ **Le graphique lui-même est une image et n'apparaît pas dans la couche texte** : ni les activités listées ni les pourcentages ne sont récupérables depuis la source fournie (voir Incertitudes).

- **a)** « Use the figures given in the statistics above to compare the number of people engaged in the different leisure activities. The following phrases can be used. »
  Amorces imprimées :
  > There are……………………..
  > The percentage…………………….
- **b)** « Do you think adult people in Tunisia have the same preferences? »

**2. Expand your knowledge : A mini Project :**
> What are the top leisure activities for teenagers in Tunisia?
> a) With your classmates, conduct a survey in your school to find out.
> b) Produce a chart similar to the one above.
> c) Write a short report based on your findings and keep it in your portfolio. Be ready to present it by the end of this module.

**Helpful notes (guide p.37) — Activity 3** : « 1.a is an opportunity to recycle the comparative form (more/less + noun/long adjective , short adjective +er , as…..as) »

> C'est la seule formulation explicite de la règle des comparatifs dans tout le module : le manuel ne comporte **aucun encadré de règle** sur les comparatifs/superlatifs ; le point est travaillé par l'usage (Activity 1.2, Activity 3.1a) et la règle n'est rappelée que dans cette note au professeur.

---

##### Section Two : Listening (manuel p.84-86 · guide p.39, tapescript guide p.82)

###### Scope and sequence (guide p.39) — verbatim

**Skills/subskills and strategies**
> **Reading**
> - scan a text for specific information
>
> **Listening**
> - transfer information onto a table
> - scan for specific details
>
> **Speaking**
> - express one's opinion
> - talk about future plans

**Vocabulary (guide p.39)** : Island-dive-cave-harbour-bay-rock(y)-shoreline-bake(ry)-lagoon-sunset
**Grammar** : Prepositions
**Functions** : Expressing opinion / Expressing interest
**Pronunciation** : Vowels / Diphthongs

**Helpful notes (guide p.39)** — verbatim :
> The text is not meant to be dealt with in an extensive way but to be used as a pre –listening activity . Ask students to read the text and to complete the table . Students may find some words in the text difficult but they are not crucial and will not hinder comprehension.
> Students listen to the whole tape before answering the questions .Make students listen to the passage as many times as needed .
> In the speaking activity , student A will express his / her preferences for visiting a chosen holiday resort using the appropriate language . Student B will ask for the reasons of his/ her classmate's choice and talk about his /her own preferences.

###### BEFORE YOU LISTEN (manuel p.84)

**Consigne** : « Read the text about the Maltese islands and complete the table with the appropriate information. »

Tableau à cinq colonnes, vide dans le manuel :

| Number of Islands | Names | Landscape | weather | Sports |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

⚠️ **Le texte sur les îles maltaises est une image dans le PDF et n'apparaît pas dans la couche texte** (voir Incertitudes). Le vocabulaire de la section (guide p.39 : island, dive, cave, harbour, bay, rock(y), shoreline, bake(ry), lagoon, sunset ; manuel p.106 : cliff, creek, crystal clear, jeep, labyrinth, mythical, path, reef, tiny, wreck, make up) indique ce que le texte contient, mais il n'est pas transcriptible depuis la source fournie.

###### AS YOU LISTEN (manuel p.84-85)

**1.** « Answer the following question. What are the islands that may be visited in this radio advert ? »
*Réponse déductible du tapescript : Gozo et Comino (la « Blue Lagoon » se trouve sur l'île de Comino). Le guide ne donne pas de corrigé pour cette question.*

**2. Complete the table with the appropriate information.** — tableau partiellement pré-rempli dans le manuel (les cases pré-remplies sont indiquées, les autres sont vides) :

| Time | Event | Place | Food |
| --- | --- | --- | --- |
| **13.00** |  |  |  |
|  | **visiting places** |  |  |
|  |  |  | **a buffet** |
|  |  | **back to the hotel** |  |

*Pas de corrigé dans le guide.* Le tapescript (guide p.82) fournit toutes les données : 13.00 → picnic lunch on the beach or in the countryside, Gozo Ftira ; 14.00 → visiting places (jeeps, les 10 sites listés) ; 18.00 → private motor boat, Blue Lagoon (Comino), sunset / evening swim / short walk, puis buffet ; midnight → back at the hotel.

**3.** « Listen and jot down the expressions used by the speaker to attract the tourists. »
*Pas de corrigé dans le guide.* Le tapescript en fournit la matière : « off the beaten track », « the beautiful rocky seaside », « the typical Mediterranean landscape », « the famous Blue Lagoon », « spoil yourself with the delicious mouth-watering food », « the crystal clear water », « a refreshing swim ».

**4. Listen and complete the following sentences with words from the passage** (manuel p.85) — texte à trous verbatim :

> The drivers and the guide will take you with the…………… to visit the following places. At approximately 18.00 hrs, you will board a private ……. …… that will take you to the Blue Lagoon where you can enjoy an ……….. ………… or explore the ………….. of Camino [sic — « Comino » ailleurs] by having a …………….. ………….around .

**Corrigé (guide p.39)** : « 4. Jeeps- motor boats-evening swim-island –short walk. »
→ *jeeps* / *motor boat(s)* / *evening swim* / *island* / *short walk*.
[Le corrigé imprime « motor boats » au pluriel alors que le tapescript dit « a private motor boat » au singulier — voir Incertitudes.]

**5.** « Look at the box below and tick the prepositions that you can hear . » — encadré verbatim, 3 lignes :

> IN — ON — ABOVE — BEFORE — TOWARDS — BELOW — OVER
> ALONG — ACROSS — OUT OF — AWAY — AROUND — UP
> THROUGH — AFTER — BACK — UNDER — INTO — OFF — AT

**Corrigé (guide p.39)** : « 5. along-off-through- around-on-in-back- at. »
→ à cocher : **along, off, through, around, on, in, back, at** (8 prépositions sur 20).
→ à ne pas cocher : above, before, towards, below, over, across, out of, away, up, after, under, into.

###### PRONUNCIATION (manuel p.85)

**Consigne** : « Listen and put each of the following words in the appropriate box according to the underlined sound . »

**Les 15 mots** : Routine – countryside – south – tour – through – found – around – wood – board – boat – blue – lagoon – mouth – food – flood .

**Le tableau à 7 colonnes**, tel qu'imprimé (symboles phonétiques dégradés dans la couche texte — voir Incertitudes) :

| u: | ^ | ⊃: | au | ou | u∂ | u |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |

Lecture la plus vraisemblable des symboles : /uː/ · /ʌ/ · /ɔː/ · /aʊ/ · /əʊ/ · /ʊə/ · /ʊ/.

*Aucun corrigé dans le guide pour la rubrique Pronunciation.*

###### AFTER YOU LISTEN — SPEAKING (manuel p.86)

**Consigne** : « You saw the following advertisements in a newspaper and you decided to go on holidays. Which of the holidays would you most like to go on ? »
⚠️ Les annonces de la p.86 sont des images et n'apparaissent pas dans la couche texte (voir Incertitudes).

Puis : « Tell your partner about the country you want to visit and the reasons why you have chosen it. You may use some of the following expressions : »

**Boîte d'expressions imprimée (verbatim)** :
> - I'm interested in / I'd like to know / It sounds interesting / I'm thinking of visiting /
> - I'm keen on ….. / I prefer……I intend to / I want to... / beautiful / luxurious /
> - cheaper / landscape / entertainment

---

##### Section Three : Reading (manuel p.87-91 · guide p.40)

###### Scope and sequence (guide p.40) — verbatim

**Skills/subskills and strategies**
> **Reading**
> - tap on different sources to answer specific questions
> - guess the meaning of unfamiliar words through context
> - transfer information onto a table
> - differentiate between relevant and irrelevant information
> - provide titles for texts
>
> **Speaking**
> - support one's opinion with arguments

**Vocabulary (guide p.40)** : dashed-plumber-invade-invasion-ant—shortlived-bat-snake-fortnight-mouse
**Grammar** : The past / the past perfect
**Functions** : - expressing disapproval
**Homework** : « Homework : language exercise( the past/ the past perfect). »

**Helpful notes (guide p.40)** — verbatim :
> The first activity introduces the topic: holidays and accommodation and prepares the students for the reading activity . This is an opportunity for students to know the different types of accommodation .
> Make students guess the topic of the text after looking at the pictures , then read the text and answer the comprehension questions.
> In the third stage of this section , students in pairs will give their opinions and justify their points of view . The items in the list of services provided is also an opportunity for students to learn more words related to the same topic.
> Have students do the language exercise in the classroom or assign it as a homework .

###### BEFORE YOU READ (manuel p.87)

**Consigne** : « Look at the following pictures and the advertisements then discuss the following in pairs: »
- « Which of these places would you prefer to stay the night at ? Why ? »
- « List 3 things you look for in your accommodation »
- « List 3 things you hate most. »

**Les trois annonces immobilières / hôtelières imprimées (manuel p.87)** — annonces publicitaires, reproduites car elles portent le lexique enseigné (types de logement) :

1. **Apartments** — « A choice of apartments being offered highly finished enjoying magnificent views of the Marsascala Bay from the living room and terrace, having 150 sqm of living space. Layout in the form of an entrance hall, an extremely spacious open plan kitchen/living/dining leading to a front terrace (20sqm), ideal for entertainment, two double and one single bedrooms, a bathroom and ensuite shower. »
2. **Terraced House** — « Terraced house situated in a quiet location. Layout comprises entrance hall, lounge, spacious kitchen/dining, 3 bedrooms, bathroom, guest toilet and laundry room at roof level. Further complementing this property is an airy basement with the possibility to convert into a flat let with own independent entrance. »
3. Légende de la troisième photo : **« The Waterfront Hotel, The Strand, Gzira »** (pas de corps d'annonce imprimé).

###### Le texte-support (manuel p.88)

**Genre** : texte narratif — récit d'une expérience personnelle (cf. « read a narrative text about a personal experience », manuel p.80). **Aucune source ni auteur cités** dans le manuel. Texte non titré : c'est précisément l'objet de l'activité 8 (« Provide an appropriate title for this text »).

**Mise en page** : trois paragraphes numérotés 1, 2, 3, encadrés à gauche et à droite par six vignettes-mots correspondant aux animaux du récit — **ant**, **cow**, **mouse** (marge gauche) et **bat**, **fly**, **snake** (marge droite).

**Résumé fidèle et détaillé** (pour ne pas reproduire le texte in extenso) :

- **§1 — L'attente.** La narratrice raconte que l'été dernier son mari et elle ont loué un *cottage* pour deux semaines. Auparavant ils avaient toujours passé leurs vacances d'été en camping, en Angleterre ou à l'étranger. Comme des amis à eux avaient loué le même cottage l'année précédente, ils savaient que l'endroit serait propre, confortable et proche de la plage. La veille du départ, les prévisions météo à long terme étaient bonnes, ce qui les rendait encore plus certains de passer d'agréables vacances. Le paragraphe se referme sur un retournement : leurs grands espoirs furent vite douchés (« our high hopes were soon dashed »).
- **§2 — Les ennuis matériels.** Les problèmes commencent dès l'arrivée, juste après minuit : en ouvrant la porte, ils trouvent de l'eau partout, puis découvrent que l'électricité ne fonctionne pas ; ils passent donc la première nuit dans la voiture. Ils trouvent heureusement un électricien et un plombier tôt le lendemain et, à midi, tout est réglé — ou semble l'être. Les choses de la maison fonctionnent, mais c'était le moindre des problèmes : bien plus grave, ce qu'ils ont fini par appeler leurs « invasions ».
- **§3 — Les « invasions ».** D'abord les mouches, présentes pendant toute la quinzaine (*fortnight*). Puis les fourmis, avec leur habitude agaçante de se glisser partout, y compris dans le réfrigérateur ; comme les mouches, elles leur tiennent compagnie en permanence. À côté de ces invasions permanentes, d'autres, brèves (*shortlived*) : une nuit, une souris envahit la maison, mais pas longtemps ; une chauve-souris est un autre visiteur indésirable ; et, en dernier lieu, ils reçoivent la brève visite d'un serpent. Conclusion : en toutes leurs années de camping ils n'avaient jamais eu d'ennuis avec les insectes ou les animaux — sauf une fois avec des vaches — et ils se demandent maintenant pourquoi ils ont choisi un autre type de vacances. L'année prochaine, retour au camping.

**Phrases citées verbatim ailleurs dans le manuel** (elles sont réimprimées telles quelles p.90 comme support de la leçon de grammaire, voir « Exploring grammar ») :
> 1. Last summer my husband and I rented a cottage. Previously, We had always spent our summer holidays camping .
> 2. As some of our friends had rented the same cottage before, we knew that the place would be clean and comfortable.

###### AS YOU READ (manuel p.88-89) — 8 activités

**1. Complete the table with the appropriate information about the writer.** (manuel p.88)

| Her marital status | The country where she lives |
| --- | --- |
|  |  |

*Pas de corrigé dans le guide.* (Le texte donne : mariée — « my husband and I » ; Angleterre — « camping, either in England or abroad ».)

**2. Match each word in column A with its definition in column B.** (manuel p.89) — tableau verbatim, avec colonne ANSWERS vide :

| A | B | ANSWERS |
| --- | --- | --- |
| 1. to camp (§1) | a. small crawling insects | 1. |
| 2. a cottage (§1) | b. two weeks | 2. |
| 3. a fortnight (§3) | c. to spend a holiday in a tent | 3. |
| 4. ants (§3) | d. a small house in the country | 4. |

*Pas de corrigé dans le guide* (appariement attendu : 1-c, 2-d, 3-b, 4-a).

**3. Tick the correct alternative** — « The writer decided to rent a cottage »
- although she had no idea about it
- because it had been recommended by her friends
- when she saw the advertisement in the newspaper

*Pas de corrigé dans le guide.*

**4. Complete the sentence with information from paragraph 1**
> The writer expected to spend a pleasant holiday first because ……………………………. and ……………………………………………

*Pas de corrigé dans le guide.*

**5.** « Did the writer enjoy her holiday ? Justify your answer with details from the text. »

**6.** « What does the writer complain about? Read and cross out the wrong alternatives » — liste imprimée verbatim :
> cows / ants / the locked door/ a mouse / flies / the water / the plumber / a serpent/ the lights / the neighbours / bats.

*Pas de corrigé dans le guide.*

**7. Circle the adjectives that best describe the writer before and after her summer holiday.** — tableau verbatim :

| BEFORE | AFTER |
| --- | --- |
| excited / nervous / enthusiastic / hopeful | disappointed / impressed / regretful / embarrassed |

*Pas de corrigé dans le guide.*

**8.** « Provide an appropriate title for this text. »

###### Exploring grammar (manuel p.90) — encadré de règle

**Consigne 1** : « Read the first paragraph again and underline all the verbs »

**Consigne 2** : « Focus on the following sentences : »
> 1. Last summer my husband and I rented a cottage. Previously, We had always spent our summer holidays camping .
> 2. As some of our friends had rented the same cottage before, we knew that the place would be clean and comfortable.
>
> What tenses are used in these sentences ? ....................... and ......................
> When did the actions take place?
> action 1………………………
> action 2 …………………….

**Encadré « Complete the rule » — verbatim (manuel p.90)** :
> **Complete the rule**
> The past simple is used to talk about …………………. actions at a particular point in the ……………………….
> The past perfect is used to show that a completed ……………… happened ………………. something else in the past.

*Le guide ne donne pas le corrigé de cet encadré.* Complétion attendue : *finished/completed* actions at a particular point in the *past* ; a completed *action* happened *before* something else in the past.

###### AFTER YOU READ — la liste des services (manuel p.90)

**Consigne** : « Look at the list of services provided in a hotel in Florida. »

**Encadré « Services » — verbatim, deux colonnes** :

| Hotel | Room |
| --- | --- |
| Swimming pool | Radio / Colour TV |
| games room | Direct dial telephone |
| Mini-gym | Hairdryer |
| Sauna / solarium | Electric trouser press |
| Good restaurants | Bathrobes |
| Ironing facilities | Mini-bar |
| Baby-sitting facilities | Private bathroom |
| Car park | 24-hour room service |
| 24-hour laudry service [sic — « laundry »] | Tea- and coffee-making facilities |
| Free newspapers | Air-conditioning |
| Telefax | Writing desk. |

**Les trois tâches (manuel p.90)** :
1. « What are the services you feel are important? »
2. « Put a cross next to any services which you think are not important. »
3. « Discuss the reasons for your choice with a classmate and put the services in order of priority. »

###### Practising related grammar points (manuel p.91) — l'exercice de langue / devoir maison

**Consigne** : « Complete the following conversation with the correct tense and/or form of the bracketed verbs : »

**Dialogue verbatim (Gary / Jean), 13 trous** :
> – Gary : Jean , I'm surprised to see you
> – Jean : well, I think you owe me an explanation
> – Gary : me? what about you, I (see)………. you in the café last night. We (arrange) ……………. to meet at the cinema , if you remember
> – Jean : so why (you/not/come)………………………. into the café if you saw me?
> – Gary : I (be)………….. very angry. I (wait)……………outside the cinema for three quarters of an hour before I(see)………..you
> – Jean : but (you/not/get)……………. my note ?
> – Gary : what note?
> – Jean : the note I(leave)………..here yesterday afternoon. When I(go) ……….. past the cinema yesterday at lunchtime, I (notice) ……………. that they (change) ………….. the film, so I (put) ………… a note under your door to tell you.
> – Gary : I (not/find)………………………any note.
> – Jean : never mind. Let's forget about it . Where shall we go now ?

**Corrigé (guide p.40)** : « saw-had arranged-didn't you come-was-had waited-saw-didn't you get –left-went-noticed-had changed-put-didn't find. »

| # | Verbe entre parenthèses | Réponse |
| --- | --- | --- |
| 1 | (see) | saw |
| 2 | (arrange) | had arranged |
| 3 | (you/not/come) | didn't you come |
| 4 | (be) | was |
| 5 | (wait) | had waited |
| 6 | (see) | saw |
| 7 | (you/not/get) | didn't you get |
| 8 | (leave) | left |
| 9 | (go) | went |
| 10 | (notice) | noticed |
| 11 | (change) | had changed |
| 12 | (put) | put |
| 13 | (not/find) | didn't find |

---

##### Section Four : Speaking (manuel p.92-93 · guide p.41)

###### Scope and sequence (guide p.41) — verbatim

**Skills/subskills and strategies**
> **Reading**
> - transfer information onto a table
> - recognize text structure
> - identify the features of an interview
>
> **Speaking**
> - produce and enact an interview

**Vocabulary (guide p.41)** : reign - blend - elite - appeal - merge - golden age
**Grammar** : - WH questions - reporting answers
**Functions** : Seeking and imparting information

**Helpful notes (guide p.41)** — verbatim :
> **Activity 1**
> Do not spend much time on the comprehension of the interview. It is meant to be an example for the students to follow in conducting their interviews.
> **Activity 2**
> Assign this activity as homework if class time is not sufficient. Ask the students to summarize their classmate's answers in a short paragraph and be ready to present it the following session. The speaking test may also be based on this activity.

###### Activity 1 (manuel p.92) — l'interview support

**Consigne** : « Read the following interview then answer the questions. »

**Titre** : **The King of Flamenco**
**Genre** : interview de magazine.
**Source citée dans le chapeau** : entretien accordé à **John Parry**, de **Newsweek**, à Madrid. **Interviewé : Joaquin Cortes**, présenté dans le chapeau comme « Part pop star, part serious artist », roi régnant du flamenco — « the foot-stamping Gypsy dance ».

**Les six questions posées, verbatim** :
1. « Why has your type of flamenco gained such wide international acceptance ? »
2. « You were one of the first dancers to perform flamenco in front of large audiences. How did that come about ? »
3. « Why did you choose Japan for your latest tour ? »
4. « Are you concerned that flamenco might be corrupted through its adaptation by foreign cultures ? »
5. « You've said you want to retire from dancing at 33 and switch careers. What comes next ? »
6. « How would you like to be remembered ? »

**Substance des six réponses (résumé fidèle, réponse par réponse)** :
1. Parce que c'est un mélange de styles porteur d'un message plus universel : il est Gitan et mêle ses racines culturelles au ballet classique et à la danse contemporaine.
2. Son intention et son message : il ne veut pas que la danse reste, comme elle l'a toujours été, réservée à l'élite ; il estime que chacun a le droit de voir de la danse et que celle-ci doit avoir un attrait populaire.
3. Il était très heureux de retourner au Japon, pays déjà visité plusieurs fois ; les Japonais entrent en résonance avec le flamenco parce qu'il a quelque chose de commun avec leur culture du théâtre Kabuki.
4. Le flamenco vit un âge d'or ; ce que les gens veulent, c'est expérimenter et le fusionner avec d'autres styles — il ne croit pas que quiconque le détruira en faisant cela.
5. L'avenir est incertain, mais il est ouvert à d'autres rôles : chorégraphe, directeur de danse, le cinéma.
6. Comme un battant (« a battler ») ayant beaucoup apporté au monde de la danse et de la culture et ayant su diffuser un message nouveau.

> Lexique de la section porté par ce texte (guide p.41 et manuel p.106) : *reign*, *blend*, *elite*, *appeal*, *merge*, *golden age*, *battler*, *choreographer*, *corrupt*.

**1. Complete the table with information from the interview.** — tableau verbatim, vide :

| Interviewee | Interviewer | Topic |
| --- | --- | --- |
|  |  |  |

*Pas de corrigé dans le guide.* (Interviewee : Joaquin Cortes ; Interviewer : John Parry, de Newsweek ; Topic : le flamenco / la carrière de Cortes.)

**2.** « How is the interview different from a usual conversation ? »

###### Activity 2 (manuel p.93)

**Consigne** : « Follow the steps below to interview a classmate about a holiday, real or imaginary. » — six étapes verbatim :
> a) Write 5 to 7 questions about the holiday. Begin your questions with words like what, who, why, when, where, how many, did, was/were, etc
> b) Ask a classmate your questions and write down his/her answers. You can ask other questions based on his/her responses.
> c) Allow your interviewee time for thinking. (pauses, silences)
> d) When you have finished the interview, ask your classmate to check the answers you wrote to see if you understood what he/she said.
> e) Exchange roles.
> f) Enact the interview.

###### Activity 3 (manuel p.93)

« Report your classmate's answers to the class. » — c'est le second point de grammaire de la section (*reporting answers*, guide p.41).

*Aucun corrigé dans le guide pour la Section Four (uniquement des Helpful notes).*

---

##### Section Five : Writing (manuel p.94-95 · guide p.42)

###### Scope and sequence (guide p.42) — verbatim

**Skills/subskills and strategies**
> **Reading**
> - identify the communicative value of pictures
> - identify features of the genre
> - recognize the relationship between form (linking words) and meaning
> - scan for specific information
> - identify purpose , audience
> - recognize text structure
> - extract salient points for subsequent use in writing
>
> **Writing**
> - apply the writing process strategies to produce a letter of complaint
> - reinvest ideas ,structures and features of the genre in one's writing

**Vocabulary (guide p.42)** : spoil – compensation – marvellous – fed up – break down – look forward to
**Grammar** : linkers
**Functions** : - giving information - complaining about a spoilt holiday

*Le guide ne comporte pas de « Helpful notes » pour la Section Five — uniquement le Scope and sequence et l'Answer Key.*

###### BEFORE YOU WRITE (manuel p.94-95)

**1.** « What sort of things can spoil a holiday? The pictures below may help you. »
⚠️ Images non présentes dans la couche texte (voir Incertitudes).

**2.** « Read the letter below. Circle the most suitable linking words. (Provided in brackets) »

**La lettre de réclamation, verbatim (manuel p.94)** — lettre de réclamation, texte non littéraire, reproduit car les alternatives entre parenthèses **sont** l'exercice :

> 12 Kings court
> London
> WC6 5PN
> 25 May 2005
>
> The manager
> Country Breaks
> Inverless IV2 6ML
>
> Dear Sir/ Madam,
>
> Last week I went on one of your "Walking Weekend" breaks in Scotland. (Unfortunately, /In spite of this, /Therefore,) I was not at all satisfied with the holiday. (To start with/Primarily/At first,) I was disappointed with the village. It was extremely noisy (so/as/owing to) they were building a new road right through the centre. I was (thus/so/though) unable to sleep after 5.30a.m. any morning. (Besides/Plus/Added to this) when I was shown to my room, I found that (although/because/in spite of) I had asked for a private bathroom, I had nowhere to wash at all. (At last/Eventually/Last but not least) I really must mention the guide. (Because of/In spite of/despite) an accident the day before, she was unable to walk properly, so we could not do some of the marvellous walks I had been looking forward to.
>
> I hope you agree that the weekend was not as advertised, and look forward to receiving compensation.
>
> Yours faithfully
> Sam Wilson

**Corrigé des 8 linkers (guide p.42)** : « 2 - unfortunately / to start with / as / thus / added to this / although / last but not least / because of »

| # | Alternatives imprimées | Réponse |
| --- | --- | --- |
| 1 | Unfortunately, / In spite of this, / Therefore, | **Unfortunately,** |
| 2 | To start with / Primarily / At first, | **To start with** |
| 3 | so / as / owing to | **as** |
| 4 | thus / so / though | **thus** |
| 5 | Besides / Plus / Added to this | **Added to this** |
| 6 | although / because / in spite of | **although** |
| 7 | At last / Eventually / Last but not least | **Last but not least** |
| 8 | Because of / In spite of / despite | **Because of** |

**3. Identify the following parts in the letter.** — six éléments verbatim :
> a) Sender's address
> b) Sender's name
> c) Complimentary close
> d) The date
> e) Receiver's address
> f) Salutation

*Pas de corrigé dans le guide.* (Dans la lettre : a = 12 Kings court, London, WC6 5PN ; b = Sam Wilson ; c = Yours faithfully ; d = 25 May 2005 ; e = The manager, Country Breaks, Inverless IV2 6ML ; f = Dear Sir/Madam.)

**4. Answer the following questions.** (manuel p.95 — l'en-tête de cette page porte « Session five » [sic] au lieu de « Section five »)
> a) Why is Sam Wilson writing this letter?
> b) Who is going to read it ?
> c) Is the format and the language of the letter appropriate for this ? Why ? Why not ?

**5.** « The letter above has three basic parts. Work with a classmate to complete its basic plan below. »
> Part 1 : …………………………………………………………
> Part 2 : …………………………………………………………
> Part 3 : …………………………………………………………

**Corrigé (guide p.42)** :
> Part 1 : Reason for writing: exact details of holiday (place, date)
> Part 2 : Details of problems.
> Part 3 : What is expected from the company.

###### AS YOU WRITE (manuel p.95) — la tâche d'écriture

**Situation, verbatim** :
> You have just come back from a holiday abroad. There were a number of things you were not happy about. Here are a few points you noted down :
> – Mum ill after climbing stairs every day
> – Kids fed up because couldn't swim in pool
> – Minibus broke down three times
>
> Write a letter to the holiday company (Luxury Tours, 255 Queen street, London WC2 8IO) complaining about what went wrong on the holiday and asking for a refund of some of the money you paid or another holiday.

**Les quatre étapes du processus d'écriture, verbatim** :
> a) Make a plan of what you are going to write.
> b) Write the first draft of the letter.
> c) Exchange your draft with a classmate. Check each other's work looking especially at the layout, the plan, punctuation and spelling.
> d) Write a second draft of your letter.

---

##### Supplément ARTS (filière Lettres uniquement) — manuel p.96-103 · guide p.43-44

> ⚠️ **Frontière** : tout ce qui suit (manuel p.96 à 103, guide p.43-44) est imprimé en rose dans le manuel et **ne concerne que la filière Lettres (Arts branch)**. Les six sections de 3ème année traitent les Sections One à Five ci-dessus ; seules les classes Lettres traitent en plus les deux sections Arts. Les deux points de grammaire *might/could + bare infinitive* et *la voix passive* n'appartiennent donc **pas** au tronc commun de ce module.

#### ARTS · Section One — READING (manuel p.96-98 · guide p.43)

###### Scope and sequence (guide p.43) — verbatim

**Skills/subskills and strategies**
> **Speaking**
> - make statements about a concrete situation
> - describe one's impressions about a particular event
>
> **Reading**
> - predict content of a text from its title
> - skim a text to identify main idea from alternatives suggested
> - transfer information onto a table
> - scan a text for details
> - guess meaning of words/expressions from context (and alternatives suggested)
> - identify/infer text origin, purpose

**Vocabulary (guide p.43)** : vacation - estimate – affordable – amass – grind – soak up – unwind – commune – pertinent – fall back on someone
**Grammar** : Might / could + bare infinitive
**Function** : Expressing future possibility
**Homework** : Doing internet research

*Pas de « Helpful notes » pour cette section dans le guide — seulement le Scope and sequence et l'Answer Key.*

###### BEFORE YOU READ (manuel p.96)
1. « Have you ever wanted to go on a holiday but couldn't afford it ? »
2. « Can you make an estimate on how much you need to go on a holiday ? »
3. « Look at the title of the text. What kind of information will it probably contain ? »

###### Le texte-support (manuel p.96-97)

**Titre** : **How to plan a cheap affordable vacation**
**Genre** : texte informatif / article de conseils pratiques (cf. « read an informative text », manuel p.80). **Aucun auteur ni source cités** — c'est précisément l'objet de la question 6 (« Where do you think this text is from? Who wrote it? »).
**Longueur** : cinq paragraphes non numérotés.

**Résumé fidèle et détaillé, paragraphe par paragraphe** :
- **§1** — Que l'on ait très peu d'argent à consacrer aux vacances ou que l'on ait économisé toute l'année et amassé une belle somme à dépenser en journées au soleil, les vacances peuvent être un moment merveilleux pour s'éloigner du train-train quotidien du travail et de la routine (« the daily grind of work and routine »).
- **§2** — Le voyage le moins cher : une sortie « à un plein d'essence » (*a one-tank trip*) vers une ville ou une zone rurale de son propre État. On peut se renseigner auprès de son auto-club local sur les parcs pittoresques, les sites historiques et les lieux d'intérêt. On peut prévoir au moins une nuit dans un *bed and breakfast* voisin si l'on choisit la campagne, pour profiter de l'air pur et du calme. Si le camping est votre truc (« If camping is your thing »), chaque État a de nombreux terrains où l'on peut se détendre (*unwind*) et communier avec la nature (*commune with nature*). À l'inverse, on peut préférer une autre ville et des vacances plus animées : opéras, parcs d'attractions, musées, théâtres, stations de ski, parcs à thème, concerts, et plus encore.
- **§3** — Outre l'auto-club, Internet est une mine d'informations extraordinaire pour qui prépare ses vacances : depuis chez soi, on trouve l'adresse d'un lieu, l'itinéraire depuis son domicile, la distance en miles et toute autre information pertinente (*pertinent*) simplement en se connectant.
- **§4** — Pour voyager en avion, des sites Internet permettent de comparer les tarifs aériens et de faire toutes les réservations nécessaires. L'avion n'est qu'une option : on peut aussi voyager en train ou en car. On peut également chercher où loger — hôtels, villas, *time shares*, *travel lodges*, chalets, *resorts*, maisons de vacances de particuliers, partout dans le monde ; les listes sont pratiquement sans fin. On peut même envisager de loger chez des amis ou des proches pour économiser davantage.
- **§5** — Une fois les idées en place, il faut décider du budget et des destinations. Pour cela, répartir l'argent disponible par catégories de dépenses : voyage, hébergement, repas, divertissements et activités. Inutile de mettre de côté pour les imprévus (réparations de voiture par exemple) si l'on a une carte de crédit sur laquelle se rabattre (« a credit card to fall back on »). Le montant alloué à chaque catégorie relève de chacun : il n'existe pas de formule toute faite (« there is no set formula »).
- **§6 (clôture)** — Les vacances n'ont pas besoin d'être coûteuses pour être un moment particulier hors du quotidien. Avec quelques recherches et un peu de planification, on peut s'offrir un voyage à tout moment.

###### AS YOU READ (manuel p.97) — 6 activités

**1.** « Read the text and check your guesses. »

**2.** « Read the text and find out which of the following is the main idea : »
> a) How to start saving money to go on a holiday.
> b) How to avoid wasting money on un-needed holidays. [sic : « un-needed »]
> c) How to go on a holiday with the money you have on hand.

**Corrigé (guide p.43)** : **c**

**3. Complete the table below with details from the text.**

| Where to stay | What to visit |
| --- | --- |
|  |  |

*Pas de corrigé dans le guide.* (Le texte fournit : *where to stay* → bed and breakfast, campgrounds, hotels, villas, time shares, travel lodges, chalets, resorts, privately-owned vacation homes, homes of friends or relatives ; *what to visit* → scenic parks, historical sites, places of interest, opera houses, amusement parks, museums, theatres, ski resorts, theme parks, concerts.)

**4. Tick the options that best express the meaning of the following expressions.**
> \* If camping is your thing.
> a) If you dislike camping
> b) If you are interested in camping.
> c) If you know nothing about camping.
>
> \* Have a credit card to fall back on.
> a) Have a credit card taken away by someone.
> b) Fail to pay for something with a credit card.
> c) Have a credit card to use when in difficulty.

**Corrigé (guide p.43)** : « 4* b / c » → première expression = **b** ; seconde expression = **c**.

**5. Find in the text the words which have the following definitions.**
> a) To stop being nervous/to relax : ……………………………..
> b) To collect something in great amounts : …………………………….
> c) To take in or absorb : …………………………………
> d) To feel close to something or somebody : ………………………….

**Corrigé (guide p.43)** :
> a- unwind
> b- amass
> c- soak up
> d- commune

**6.** « Where do you think this text is from? Who wrote it? Who is the expected audience? »
*Pas de corrigé dans le guide.*

###### AFTER YOU READ (manuel p.98) — l'encadré de grammaire *might / could*

**1. Focus on the italicized words below. (par 2)** — les deux phrases-cibles, verbatim :
> You could plan to spend at least one night…
> …you might want to see.

**Grille de choix imprimée, verbatim** :
> Guess whether they:
> a) refer to the — Present / Past / Future
> b) express — Permission / Possibility / Ability

**2) Complete the box below.** — encadré verbatim :
> Might/ could + ……… …………. ⟶ ……………… ………………..

**Corrigé (guide p.43) — After You Read** :
> 1* a- future
>    b- Possibility
> 2* might / could + bare infinitive ---------- future possibility

###### Homework (manuel p.98)
> Choose a vacation destination you would like to visit and search the web to find information about it.(location, accommodation, weather, activities, etc)

Correspond à la ligne « Homework : Doing internet research » du guide p.43. *Pas de corrigé (production libre).*

#### ARTS · Section Two — READING (manuel p.99-103 · guide p.44)

###### Scope and sequence (guide p.44) — verbatim

**Skills/subskills and strategies**
> **Reading**
> - tap on different sources to answer specific questions
> - guess the meaning of unfamiliar words through context
> - differentiate between relevant and irrelevant information
> - identify logical relations in a text
> - distinguish between factual statements and exaggeration
> - infer and evaluate the writer's intention
> - compare one's culture to that conveyed in a text
>
> **Writing**
> - produce a report

**Vocabulary (guide p.44)** : plump- ingredients –consistent –dilemma-sausages-doled(out)-mix-season(verb)-bundle-affix.
**Grammar** : - The passive
**Function** : - inquiring about/expressing opinion
**Homework** : « Homework : multiple choice alternatives (passive/active sentences) »

**Helpful notes (guide p.44)** — verbatim :
> The first activity prepares the students for the reading passages.
> In the second activity, students express their preferences by ticking the appropriate box then complete the table with other items that are not mentioned .
> Ask students to read both texts at the same time and answer the first questions then to focus on the second text and answer the remaining questions .
> Before conducting the survey , students in groups of four complete the questionnaire with the appropriate questions and tick the appropriate boxes .

###### BEFORE YOU READ (manuel p.99)

**1. Answer the following questions :**
> a) Do you like eating out?
> b) Would you be prepared to spend a lot of money in expensive restaurants ? Give your reasons.

**2.** « Tick the appropriate box for the food you like to eat in restaurants and the one(s) you prefer to eat at home. Add the food you like to the list and say where you like to eat it. »

**Tableau verbatim, 11 items** :

| The food | In restaurants | At home |
| --- | --- | --- |
| Salad |  |  |
| Sea food |  |  |
| Soup |  |  |
| Escalope |  |  |
| Fish |  |  |
| Chicken |  |  |
| Kuskus [sic — graphie du manuel pour « couscous »] |  |  |
| Steak |  |  |
| Vegetables |  |  |
| Chips |  |  |
| Fresh fruit salad |  |  |

###### AS YOU READ — les deux textes (manuel p.100)

**Consigne** : « Read the texts and do the activities below. »

**Text 1 — « Not Totally Entertained »**
**Genre** : chronique / article d'humeur de magazine. **Aucun auteur ni source cités.** Deux paragraphes numérotés.
**Résumé fidèle** :
- **§1** — L'auteur explique que se réveiller avec des doigts gonflés « comme de grosses saucisses » n'est pas son idée du plaisir. Selon lui, l'idée que la plupart des restaurants se font d'une bonne cuisine, c'est un peu d'ingrédients de base et beaucoup de sel. Peut-être leur but est-il de donner soif ; mais la sécheresse dans la bouche et l'effet « ballon » sur son corps quand il mange dehors lui donnent surtout envie de cuisiner lui-même ses repas au barbecue.
- **§2** — Non seulement manger au restaurant paraît aujourd'hui plus salé, mais cela devient aussi de plus en plus cher : les restaurants invoquent la hausse des prix alimentaires et répercutent la hausse des coûts des matières premières sur les prix de leurs cartes. Le métier de la restauration est très largement une existence éphémère — et il est très difficile de trouver un bon restaurant qui reste constant dans la durée.

Phrase citée verbatim dans l'exercice 3 (donc reproduite ici parce qu'elle *est* la consigne) :
> « The restaurant business is very much a here- today, gone-tomorrow existence ». [dans le corps du texte p.100 : « here-today,gone-tomorrow », sans espace après la virgule]

**Text 2 — « Cooking out, eating in. »**
**Genre** : article de magazine (reportage). **Aucun auteur ni source cités.** Chapeau + quatre paragraphes numérotés.
**Chapeau imprimé** : « Perplexed by what to make for dinner ? Stores like Dream Dinners help busy people prepare meals ready to heat at home. »
**Résumé fidèle** :
- **§1** — Les Américains perdent peut-être le contact avec l'art de cuisiner, mais pas le désir du réconfort d'un plat fait maison. Carole Counihan, anthropologue de l'alimentation à l'université de Millersville (Pennsylvanie), est citée : selon elle, toute femme et tout cuisinier affronte le dilemme du « qu'est-ce que je fais à dîner ? », et ces Dream Dinners répondent précisément à ce besoin — on n'a ni à faire les courses ni à planifier, mais on peut en un sens s'attribuer le mérite de la cuisine (« take credit for the cooking »).
- **§2** — L'entreprise s'appelle Dream Dinners ; comme plus d'une centaine d'enseignes similaires à travers le pays, elle fonctionne comme une sorte de cuisine communautaire où des mères et des pères préparent en deux heures seulement plusieurs semaines de repas prêts à congeler. C'est de la cuisine maison — sans la maison.
- **§3** — Fondée en 2002 par deux femmes dans une banlieue de Seattle, Dream Dinners fut la première société spécialisée dans le « meal assembly ». Le fonctionnement : le client utilise un site web pour choisir une date et une heure ainsi que les plats qu'il souhaite préparer — un pavé de bœuf en croûte d'herbes, par exemple, ou un poulet mirabella. À son arrivée à la séance, les ingrédients ont été soigneusement répartis dans des récipients en acier inoxydable.
- **§4** — Le processus se déroule comme une émission culinaire de télévision : « c'est cuisiner avec tout déjà disposé pour soi ». Les chefs en herbe (« would-be chefs ») se contentent de mélanger et d'assaisonner, préparant viandes, poissons et pizzas pour le four. Les plats préparés — mais non cuits — sont ensuite emballés dans des sacs de congélation et des barquettes en aluminium. Les instructions de cuisson y sont apposées et les repas sont rapportés chez soi dans une glacière, où chaque client stockera une douzaine de plats prêts à cuire.

###### Activités sur les DEUX textes (manuel p.101)

**1. Complete the sentences** — amorces verbatim :
> Both texts are about………………………………………………………………………………..
> In the first text, the writer …………………………………………………………………………..
> but in the second text, the writer ………………………………………………………………..
> ……………………………………………………………………………..……………………….

**2. Read text 1 and answer the following question :** « The writer decided to cook his own meal for some reasons. What are they ? » — trois tirets à remplir :
> –
> –
> –

**3. Explain the following sentence using your own words :** « The restaurant business is very much a here- today, gone-tomorrow existence ».

**4.** « Is the writer in text 1 exaggerating or describing objectively what happens in some restaurants nowadays ? Find examples in the text to justify your answer. »

*Aucun corrigé dans le guide pour ces quatre activités.*

###### Activités sur le TEXTE 2 (manuel p.101-102)

**1. Say whether the following statements are true or false. Justify your answers.**
> – Americans don't like home-made food ( )
> – Dream Dinners help both men and women ( )

**2. Tick the correct alternative**
> a) bundled (§4) means
>    - mixed
>    - paid
>    - quickly put together
> b) a cooler (§ 3) is
>    - a very short time
>    - a device for keeping things cool
>    - a plastic bag
> c) With Dream Dinners, the customers
>    - cook the meals at home and eat them out
>    - prepare the meals out and eat them at home
>    - cook the meals out and eat them out
> d) The "would-be chefs" are :
>    - the people who work with Dream Dinners
>    - the people who sell the ingredients
>    - the customers

*(Remarque de transcription : le manuel renvoie « a cooler » au §3 alors que le mot apparaît au §4 — voir Incertitudes.)*

**3. How does Dream Dinners work ? Read the text again and reorder the following sentences to answer the question. The first one has been done for you.** — les six items, verbatim, avec la seule numérotation imprimée :
> - you go to Dream Dinners. ( )
> - you mix and season the ingredients. ( )
> - you follow the cooking instructions to prepare your meal at home. ( )
> - you take the uncooked ready- to cook meals. ( )
> - you use a website to choose a time, date and the meal(s) you like to prepare. ( **1** )
> - the ingredients are prepared for you at Dream Dinners. ( )

**4.** « Can you draw any conclusions about the eating habits of Americans ? - What are your eating habits ? »

*Aucun corrigé dans le guide pour ces quatre activités.*

###### Exploring grammar — la voix passive (manuel p.102)

**Consigne** : « Focus on the following sentences » — les deux phrases-cibles, verbatim :
> 1. the prepared meals are bundled into freezer bags.
> 2. ingredients have been carefully doled out into stainless steel containers.

**Questions de guidage, verbatim** :
> Who bundles the prepared meals in sentence 1? ……………………….
> Who has doled the ingredients out in sentence 2 ? ………………………
> Are the people who do the actions important in these sentences ?

**Encadré « Complete the rule about the use of the passive » — verbatim** :
> The passive is often used to focus more on the ………. than on the ………… who does it. It is used when the doer is not …………….. or not known. An object in an active sentence would be the …………… in a …………. sentence.

*Le guide ne donne pas le corrigé de cet encadré.* Complétion attendue : focus more on the *action* than on the *person/doer* who does it ; used when the doer is not *important* or not known ; an object in an active sentence would be the *subject* in a *passive* sentence.

###### AFTER YOU READ — l'enquête sur les habitudes alimentaires (manuel p.102-103)

**Consigne générale** : « You are going to do a survey about the eating habits in your class. »

**Step 1** (manuel p.102) — « In groups of 4 , complete the questionnaire with the appropriate questions. » — questionnaire à trois colonnes, deux questions données, la troisième (et les suivantes) à écrire :

| | yes | no | sometimes |
| --- | --- | --- | --- |
| 1. Do you like eating out ? |  |  |  |
| 2. Do you eat ready- prepared food ? |  |  |  |
| 3. |  |  |  |

**Step 2** (manuel p.103) — « Fill in the questionnaire first individually and then compare your answers with some of your classmates'. »

**Step 3** (manuel p.103) — « Write a short report using the information you collected in your survey and draw conclusions about the eating habits in your class . In your survey : - give the number of pupils in your class, say what the survey is about and give the results. »

**Useful language (encadré verbatim, manuel p.103)** :
> most of us / some of us / nearly all of us / half of us / none of us... however , in addition.

###### Homework — passif / actif (manuel p.103)

**Consigne** : « Circle the correct alternative. »

**Lettre à trous, verbatim (6 alternatives)** :
> Dear Sally ,
> How are you ? We 've been very well looked after by our hosts. Mary (took/is taken) us sightseeing and we (have been introduced/ introduced) to some of her friends who made us feel very welcome .Last night , we (showed/ were shown) round a castle where one of Mary's friends lives. Apparently, the castle (was given/ gave) to the family after one of their ancestors (killed/was killed) while trying to save the queen . I hope (we'll invite/ we'll be invited) to visit other interesting places.

**Corrigé (guide p.44)** : « -took- have been introduced-were shown-were given-was killed-we'll be invited »

| # | Alternatives imprimées (manuel p.103) | Réponse du guide (p.44) |
| --- | --- | --- |
| 1 | (took / is taken) | **took** |
| 2 | (have been introduced / introduced) | **have been introduced** |
| 3 | (showed / were shown) | **were shown** |
| 4 | (was given / gave) | **were given** [sic — voir Incertitudes] |
| 5 | (killed / was killed) | **was killed** |
| 6 | (we'll invite / we'll be invited) | **we'll be invited** |

---

##### SELF-ASSESSMENT (manuel p.104)

**A. « What progress do you feel you have made in English in this module ? Put a tick (√ ) in the box that applies to you . »** — grille à 14 énoncés × 3 colonnes (YES / A LITTLE / NO), verbatim :

| # | Énoncé | YES | A LITTLE | NO |
| --- | --- | --- | --- | --- |
| 1 | I've used what I already know to learn more English |  |  |  |
| 2 | I can read a text and answer the questions correctly |  |  |  |
| 3 | I can listen to a text and answer the questions correctly |  |  |  |
| 4 | I've learnt how to converse in English |  |  |  |
| 5 | I am using the grammatical structures I've learnt |  |  |  |
| 6 | I understand grammar but I cannot use the structures correctly |  |  |  |
| 7 | I can remember the words I've come across |  |  |  |
| 8 | I recognize the words but I cannot use them |  |  |  |
| 9 | I've learnt how to write in English |  |  |  |
| 10 | The writing activities are difficult |  |  |  |
| 11 | I've shared ideas with my classmates and my teacher |  |  |  |
| 12 | My pronunciation has improved |  |  |  |
| 13 | I've learnt how to conduct a mini- project |  |  |  |
| 14 | My English has improved |  |  |  |

**B. « What did you like most in this module ? Tick the answer(s) that apply(ies) to you. »** — 10 items verbatim :
> - The topics
> - The activities
> - The projects
> - Listening to the cassette
> - Acting out situations
> - The writing activities
> - The Reading skills
> - The grammar exercises
> - The vocabulary exercises
> - Working in groups

**C. « Circle the alternative that applies to you : »**
> I still need to work on :
> Reading / Listening / Speaking / Writing / Vocabulary / Grammar

---

##### FUN PAGE (manuel p.105)

Deux éléments humoristiques, sans titre ni auteur, séparés par un motif décoratif de points.

1. **Une anecdote** (5 lignes) : une voiture de police s'arrête devant chez Grandma et Grandpa en descend. L'agent explique que le vieux monsieur a dit s'être perdu dans le parc. Grandma s'étonne — « Why, Bill » — puisqu'il s'y rend depuis plus de 30 ans : comment aurait-il pu s'y perdre ? Se penchant vers elle pour que le policier n'entende pas, il chuchote la chute : « Wasn't exactly lost. I was just too tired to walk home. »
2. **Un aphorisme d'une phrase** sur la restauration : quoi que l'on commande au restaurant, ce que commandent les autres paraîtra toujours meilleur.

---

##### VOCABULARY COVERED IN MODULE 3 (manuel p.106) — liste intégrale

La page est imprimée sur quatre colonnes ; la liste ci-dessous restitue l'ordre logique (chaque section est alphabétique dans la source, ce qui valide la recomposition des colonnes).

###### Common core

**Section one** (17 entrées)
accommodation · canoeing · cycling · dog sledge riding · harbour cruising · hiking · honeymoon · luscious food · roller skating · safari · sightseeing · sky diving · sunbathing · surfing · tent · water skiing · wildlife

**Section two** (19 entrées)
bake · board · buffet · cliff · creek · crystal clear · get rid of · jeep · labyrinth · lagoon · make up · mythical · oven · path · reef · shoreline · spoil · tiny · wreck

**Section three** (22 entrées)
ant · bat · camp · convert into · cottage · dash (v) · detached · embarrassed · en suite · enthusiastic · fortnight · impressed · invade · invasion · magnificent · nervous · plumber · regretful · rent · snake · spacious · unlock

**Section four** (8 entrées)
appeal · battler · blend · choreographer · corrupt · elite · merge · reign

**Section five** (5 entrées)
break down · compensation · disappointed · fed up · marvellous

###### Arts Supplement (filière Lettres uniquement)

**Section one** (18 entrées)
affordable · amass · amazing · category · chalet · commune · estimate · fall back on sb · formula · get on line · grind · internet site · pertinent · resort · soak up · travel lodge · unwind · vacation (n &v)

**Section two** (17 entrées)
anthropologist · bundle (v) · commodity · communal · consistent · cooler · dole out · ingredients · mix · outfit · perplexed · plump · sausage · season (v) · take credit for s.th · unfold · whip (v)

> **Total : 106 entrées** — 71 en tronc commun, 35 dans le supplément Arts.
>
> Écarts entre le manuel p.106 et les listes « Vocabulary » du guide, à noter pour la génération :
> - le guide p.37 écrit « accomodation » [sic] et « wild life » en deux mots ; le manuel p.106 écrit « accommodation » et « wildlife » ;
> - le guide ajoute des mots absents de la liste du manuel : *resorts* (S1), *island / dive / cave / harbour / bay / rock(y) / sunset* (S2), *shortlived / mouse / dashed* (S3), *golden age* (S4), *look forward to* (S5), *dilemma / affix* (Arts S2) ;
> - le guide p.44 écrit *sausages*, *doled (out)*, *season (verb)* là où le manuel écrit *sausage*, *dole out*, *season (v)*.

---

##### Tapescript du module (guide p.82)

**En-tête imprimé** : « Module three: Section two . Listening »
**Genre** : annonce radiophonique / boniment publicitaire pour une excursion d'une journée à Gozo et Comino (îles maltaises). Texte non littéraire, reproduit intégralement car c'est l'unique support audio de la Section Two et il n'est reproduit nulle part dans le manuel.

> Get rid of the daily routine of traffic and restaurants, to enjoy countryside walk south east of Gozo. A typical Gozitan picnic lunch and approximately a three-hour jeep tour will take you "off the beaten track", along the beautiful rocky seaside and through the fields, with time to admire the typical Mediterranean landscape with its rocky shoreline and dwarf vegetation.
>
> Carob and fig trees are found along the paths. Around 13.00 hrs : picnic lunch on the beach or in the countryside with a slection [sic — « selection »] of Gozo Ftira , which is similar to a pizza but still being baked in the old bakeries using wood from the oven.
>
> Around 14.00hrs , the drivers and the guide will take you with the jeeps to visit the following places :
>
> - Simar valley
> - Ramla valley
> - Ramla bay ( swim stop )
> - Calypso cave
> - Marsalforn Bay
> - The salt pans
> - The azure window
> - The inland sea
> - Victoria the capital city
> - The Citadel
>
> At approximately 18.00hrs, you will board a private motor boat that will take you to the famous Blue Lagoon on the island of Comino where you can enjoy the sunset , an evening swim in the blue lagoon or explore the island of Camino [sic — « Comino » deux lignes plus haut] by having a short walk around.
>
> A buffet will be held for you to spoil yourself with the delicious mouth-watering food.
>
> I n the meantime [sic — espace parasite dans « In »] , music is also on for those who like to go for a dance. The crystal clear water of the blue lagoon will be flood lit for those who wish to take a refreshing swim.
>
> On the way back, we show you some caves around the island.
>
> You will be back at your hotel approximately at midnight

**Chronologie exploitable (pour le tableau de l'activité AS YOU LISTEN 2)** :

| Time | Event | Place | Food |
| --- | --- | --- | --- |
| 13.00 | picnic lunch | on the beach / in the countryside | a selection of Gozo Ftira (similaire à une pizza, cuite au bois dans les vieilles boulangeries) |
| 14.00 | visiting places (jeep tour, 10 sites) | Simar valley, Ramla valley, Ramla bay (swim stop), Calypso cave, Marsalforn Bay, the salt pans, the azure window, the inland sea, Victoria the capital city, the Citadel | — |
| 18.00 | private motor boat ; sunset, evening swim, short walk | Blue Lagoon, island of Comino | a buffet (« delicious mouth-watering food ») |
| midnight | back to the hotel | the hotel | — |

**Prépositions entendues (corrigé guide p.39)** : along, off, through, around, on, in, back, at — toutes présentes dans le tapescript (« along the beautiful rocky seaside », « off the beaten track », « through the fields », « Around 13.00 hrs », « on the beach », « in the countryside », « back at your hotel », « at midnight »).

---

##### Incertitudes (module 3)

1. **Le texte « about the Maltese islands » de la p.84 (BEFORE YOU LISTEN) est absent de la couche texte** — c'est une image dans le PDF. Le tableau à compléter (Number of Islands / Names / Landscape / weather / Sports) est donc transcrit mais sa source ne l'est pas. Le lexique de la section (guide p.39 + manuel p.106 : *cliff, creek, crystal clear, labyrinth, mythical, path, reef, tiny, wreck, make up, dive, cave, bay, harbour, rock(y)*) laisse deviner le contenu, mais **rien n'a été reconstitué**. Toute génération sur cette activité exige de rouvrir le manuel p.84.
2. **Le graphique de la p.83 (Activity 3.1, « top leisure activities for adult people in USA ») est absent de la couche texte** : aucune activité ni aucun pourcentage n'est récupérable. L'activité 3.1a (comparaison chiffrée, comparatifs) n'est donc pas générable en l'état.
3. **Les annonces de la p.86 (AFTER YOU LISTEN / SPEAKING, « the following advertisements in a newspaper ») sont absentes de la couche texte**, de même que les 12 images de l'Activity 1 p.81 (compensées par le corrigé du guide p.38), les photos de la p.87 et les images de la p.94 (« things that can spoil a holiday »).
4. **Symboles phonétiques dégradés (manuel p.85)** : le tableau imprime `u:`, `^`, `⊃:`, `au`, `ou`, `u∂`, `u`. Lecture retenue : /uː/, /ʌ/, /ɔː/, /aʊ/, /əʊ/, /ʊə/, /ʊ/ — le `^` et le `⊃:` sont des substituts typographiques de ʌ et ɔː, le `∂` de ə. Aucun corrigé n'existe dans le guide pour cette rubrique.
5. **Discordance corrigé/texte (guide p.44 vs manuel p.103)** : le manuel propose l'alternative « (was given/ gave) » et le corrigé du guide imprime « were given » — forme qui ne figure dans aucune des deux options. Le sujet est « the castle » (singulier), donc l'option imprimée dans le manuel est *was given*. Le corrigé du guide est très probablement une coquille.
6. **Discordance corrigé/tapescript (guide p.39 vs guide p.82)** : le corrigé de l'activité 4 imprime « motor boats » (pluriel) alors que le tapescript et le manuel p.85 disent « a private motor boat » (singulier) ; le corrigé imprime aussi « Jeeps » avec majuscule.
7. **« Camino » / « Comino »** : le tapescript (guide p.82) et le manuel p.85 écrivent « Camino » à la dernière occurrence, alors que la forme correcte — et utilisée deux lignes plus haut dans le tapescript — est « Comino ». Les deux graphies sont conservées telles quelles avec `[sic]`.
8. **Renvoi de paragraphe erroné (manuel p.101, activité 2.b)** : « a cooler (§ 3) » alors que le mot *cooler* apparaît au §4 du Text 2 ; « bundled (§4) » est en revanche correct.
9. **Coquilles source conservées telles quelles** : « harbor cruising » (manuel p.81) vs « harbour cruising » (manuel p.106, guide p.37) ; « accomodation » (guide p.37) vs « accommodation » (manuel p.87, p.106) ; « laudry » pour *laundry* (manuel p.90) ; « Session five » pour *Section five* (en-tête manuel p.95) ; « slection » pour *selection* et « I n the meantime » (guide p.82) ; « un-needed » (manuel p.97) ; « May be » pour *Maybe*, « here-today,gone-tomorrow », « prepared-but uncooked- meals » (manuel p.100) ; « New York City.Theater » et « 1. look at the chart below.It » (manuel p.82-83) ; « wild life » (guide p.37) ; « Kuskus » (manuel p.99) ; « shortlived » (manuel p.88, guide p.40) ; « flood lit » (guide p.82).
10. **« pospone » introuvable** : la coquille annoncée dans la commande n'apparaît **ni** dans le manuel p.80-106 **ni** dans le guide p.36-44/82 tels qu'extraits. Elle appartient probablement à une autre tranche du manuel.
11. **Corrigés absents du guide** — à produire par raisonnement lors de la génération, jamais à citer comme « corrigé officiel » : Section One activités 1.2, 1.3, 2.1, 2.2, 2.3, 3.1a/b, 3.2 ; Section Two activités 1, 2, 3 et toute la rubrique Pronunciation ; Section Three activités 1 à 8, l'encadré « Complete the rule » du past perfect et les trois tâches sur la liste des services ; toute la Section Four ; Section Five activités 1, 3, 4 et la tâche AS YOU WRITE ; Arts Section One activités 1, 3, 6 et le Homework ; Arts Section Two : tout sauf le Homework (y compris l'encadré « Complete the rule » du passif et la remise en ordre des 6 étapes de Dream Dinners).
12. **Textes-supports résumés, non recopiés** (règle R-2 appliquée par prudence aux textes d'auteur non crédités) : le récit du cottage (manuel p.88), l'interview de Joaquin Cortes (manuel p.92), « How to plan a cheap affordable vacation » (manuel p.96-97), « Not Totally Entertained » et « Cooking out, eating in » (manuel p.100), l'anecdote de la Fun page (manuel p.105). Les phrases que les exercices citent explicitement (phrases-cibles de grammaire, expressions à expliquer) sont, elles, reproduites verbatim car elles constituent la consigne. Les annonces publicitaires, la liste des services, la lettre de réclamation et le tapescript sont reproduits intégralement (textes non littéraires portant directement la langue enseignée).

### Module Four — SCIENCE AND TECHNOLOGY : A BLESSING OR A CURSE ? (manuel p.107-148 · guide p.45-56)

> **Frontière filière.** Le **tronc commun** couvre Sections One → Five (manuel p.107-135) plus les
> rubriques de clôture (Self-assessment p.146, Fun page p.147, Vocabulary p.148). Le **supplément
> Arts (manuel p.136-145 · guide p.54-56)** est **réservé à la filière Lettres**. Seule exception
> déclarée par le guide (p.54) : « This section is specific to the Arts students. However, have the
> other students of the other branches deal with Activity 1. and Activity 2. (Before you read) and
> the first part of the story. »

---

## Chapeau du module

**Titre du module** (manuel p.107) : « SCIENCE AND TECHNOLOGY : A BLESSING OR A CURSE ? »

**Topic** (guide p.45) : Science and inventions / Technology

**Subtopics** (guide p.45) : Inventions, experiments, scientists, medical research and progress,
computers, mobile phones, TV, genetic engineering, new technology and its impact on our daily life

**Cross-curricular learning goals** (guide p.45) : problem solving, critical thinking, efficient use
of data, efficient working procedure, appropriate self-expression, ICT use, project work,
communicating, working and living with others.

**Expected learning outcomes** — verbatim (manuel p.107). « In this module, I'm going to
- use what I already know to acquire new words and ideas about science and technology
- listen to presentations on genetic engineering
- conduct a mini-project on a scientific/technological issue
- read extracts from articles on scientific and technological issues
- read a short story
- read a poem
- learn and practise lexical and grammatical items
- enact a telephone conversation
- take part in a debate on the issue of cloning
- take part in a dialogue on the advantages and the disadvantages of genetic engineering, computer games or mobile phones
- write an article in a newspaper
- expand topic sentences
- write an e-mail
- write about a real or an imaginary accident
- expand my knowledge of the world »

**Skills travaillés, par section** (synthèse des « Scope and sequence », guide p.46-55) :
Reading (Sections One, Two, Three, Five ; Arts One, Two), Listening (Section Two),
Speaking (Sections One, Two, Four), Writing (Sections One, Two, Three, Five ; Arts One, Two, Three).

**Grammar du module** :
- Section Two — **prefixes of negation** + **word formation** (guide p.49)
- Section Three — **compound adjectives** (guide p.51)
- Section Four — **modals** : may, can, must, should, ought to, had better (guide p.52)
- Arts Section One — can, may, should, will … (guide p.54)
- Arts Section Three — temps du passé, passif, formation de mots (exercice Titanic, manuel p.145)

**Pronunciation** : **stress patterns** (guide p.49) — travaillé en Section Two, exercice G p.122.

**Project work / Mini-project** (guide p.46) : « conduct a project work on a scientific or a
technological issue ». Note du guide (p.46) : « The mini-project could be done individually, in
pairs or in small groups. » Consigne élève : Activity 6, manuel p.113.

**Functions** :
- Section One (guide p.46) — inquiring about / expressing opinion
- Section Two (guide p.49) — giving information, expressing agreement, expressing disagreement, expressing approval, expressing disapproval
- Section Four (guide p.52) — giving/asking for information ; expressing approval / disapproval
- Section Five (guide p.53) — persuading people to do things
- Arts Section One (guide p.54) — expressing opinion ; making comparisons ; expressing possibility ; expressing impossibility ; predicting future events ; expressing how certain/uncertain one is of something
- Arts Section Two (guide p.55) — expressing opinion

---

## TRONC COMMUN

#### Section One : Introductory activities

**(manuel p.108-113 · guide p.46-47)**

##### Scope and sequence (guide p.46) — verbatim

- **Skills/subskills and strategies**
  - *Reading* : match dictionary choices with context at hand and explore nuances ; identify the communicative value of utterances ; evaluate ideas ; acquire knowledge about a given topic
  - *Writing* : write a coherent text (reorder a jumbled telephone conversation)
  - *Speaking* : make statements about concrete situations ; express opinion/judgement about specific issues ; enact a telephone conversation
- **Vocabulary** : applied (science), blessing, branch, cellular, cloning, cool, curse, device, diagnose, dialysis, discover, disposable, draw upon, fabricate, ingenuity, invent, kidney, laser, lens, lift (give s.o a lift), make up, nano technology, orbit, originate, pure (science), robot, science, set up, surgery, technology, text (v)
- **Functions** : inquiring about / expressing opinion
- **Mini-project** : conduct a project work on a scientific or a technological issue

##### Helpful notes (guide p.46) — verbatim

> **Nano technology** : the ability to do things – measure, see, predict and make – on the scale of
> atoms and molecules. Traditionally, the nanotechnology realm is defined as being between 0.1 and
> 100 nanometers, a nanometer being one thousand [sic] of a micron (micrometer), which is, in turn,
> one thousandth of a millimiter [sic].
>
> **In Vitro Fertilization** : (IVF), with subsequent embryo transfer, involves the fertilization of
> eggs by sperm in a test tube – in vitro – rather than in the body. It is used as a treatment for
> some types of infertility.
>
> - The mini-project could be done individually, in pairs or in small groups.

##### Activity 1 (manuel p.108) — définitions de dictionnaire à compléter

Consigne : « Complete each dictionary definition with the appropriate word from the box. »

**Banque de mots** : `invent, discover, originate, technology, science`

Les 5 définitions imprimées (verbatim, avec le tilde `~` du manuel qui remplace le mot cherché) :

1. « to see, get knowledge of, learn of, find, or find out, gain sight or knowledge of (something previously unseen or unknown) : to ~ America ; to ~ electricity. to ~ : to find something that had previously existed but had hitherto been unknown : to ~ a new electricity. To ~ how to make synthetic rubber. »
2. « to make or create something new, especially, something ingeniously devised to perform mechanical operations. To ~ a device for detecting radioactivity. Create as a product of one's ingenuity, experimentation. to ~ the telegraph. To produce or create with the imagination : to ~ a story. To make up or fabricate (something fictitious or false) : to ~ excuses. »
3. « to begin something new, especially, new ideas, methods etc. to ~ a political movement. »
4. « 1. a branch of knowledge or study dealing with a body of facts or truths systematically arranged and showing the operation of general laws : the mathematical ~s. 2. systematic knowledge of the physical or material world gained through observation and experimentation. 3. any of the branches of natural or physical ~. 4. systematized knowledge in general. 5. knowledge, as of facts or principles, knowledge gained by systematic study. 6. a particular branch of knowledge. 7. skill, especially, reflecting a precise application of facts or principles ; proficiency. »
5. « the branch of knowledge that deals with the creation and use of technical means and their interaction with life, society, and the environment, drawing upon such subjects as industrial arts, engineering, applied science, and pure science. »

**Corrigé (guide p.47)** : 1. discover — 2. invent — 3. originate — 4. science — 5. technology

##### Activity 2 (manuel p.109) — quiz de culture scientifique et technologique

**A.** Consigne : « How much do you know about scientific and technological developments ? Tick the
appropriate alternative. »

| # | Question | a) | b) | c) | d) |
|---|---|---|---|---|---|
| 1 | When was the first robot built ? | in 1902 | in 1908 | in 1916 | in 1921 |
| 2 | Which of these products was first invented ? | the air conditioner | the computer hard disc | the mobile phone | the transistor radio |
| 3 | Who invented the kidney dialysis machine ? | Thomas Edison | Graham Bell | Alfred Nobel | William Kolff |
| 4 | Who invented the laser ? | Wilson Greatbatch | Scott Olson | Gordon Gould | Henry Ford |
| 5 | Who set up Microsoft ? | Karl A. Muller | Berners Lee | Bill Gates | James Russel |
| 6 | When did the first man-made satellite orbit the moon ? | in 1962 | in 1968 | in 1975 | in 1993 |
| 7 | In 1928, Scottish biologist Alexander Fleming discovered | Penicillin | Insulin | The hepatitis-B vaccine | Aspirin |
| 8 | DVD (Digital Versatile Disc or Digital Video Disc) was invented in | 2005 | 2000 | 1995 | 1990 |
| 9 | The Disposable contact lenses were invented in | 1987 | 1980 | 1975 | 1970 |
| 10 | Who invented the photocopier ? | Bell Labs | Chester F. Carlson | Harold Edgerton | Robert Watson – Watt |

**B.** « Now check your answers with your classmates'. How many correct answers do you have ? If your
score is below the average don't worry too much because you'll learn a lot about science and
technology in this module. »

**Corrigé (guide p.47) — verbatim, avec toutes les dates et tous les inventeurs donnés**

1. « The first robot was built in 1921 (not 1912) » [sic : « 1912 » n'est aucune des options imprimées, qui sont 1902 / 1908 / 1916 / 1921] → **réponse d) 1921**
2. « The air conditioner was invented by **Willis Carrier** in **1902**. The computer hard disc was invented in **1956**. The transistor radio was invented by **Texas Instruments** in **1953**. The mobile phone was first invented in **1947**. The cellular phones were invented in **1979**. The digital cellular phones were invented in **1988**. » → **réponse a) the air conditioner**
3. « Kidney dialysis was invented by **William Kolff** in **1944**. » → **réponse d)**
4. « **Gordon Gould** invented the laser in **1958**. » → **réponse c)**
5. « **Karl M Muller** [sic ; le manuel écrit « Karl A. Muller »] **and George Bednoz** [sic] invented the **high-temperature super conductor** in **1986**. **Berners Lee** created **Internet Protocol (HTTP)** and **www language (HTML)** in **1990**. **James Russel** invented the **compact disk** in **1965**. **Bill Gates set up microsoft** [sic, minuscule]. » → **réponse c) Bill Gates**
6. « **1968** » → **réponse b)**
7. « **Penicillin.** **Insulin** was invented by **Frederick Grant B** [sic, nom tronqué] in **1922**. **Hepatitis-B vaccine** was invented in **1980**. » → **réponse a) Penicillin**
8. « **1995.** » → **réponse c)**
9. « **1987.** » → **réponse a)**
10. « **Bell Labs** invented the **voice recognition machine** in **1936**. **Chester F Carlson** invented the **photocopier** in **1937**. » → **réponse b) Chester F. Carlson**

##### Activity 3 (manuel p.110-111) — photos légendées, discussion d'attitudes

Consigne : « Look at the pictures. Read the captions and discuss the different attitudes with your
classmates. »

⚠️ **Les 9 photos sont des supports en image, absents de la couche texte (manuel p.110-111).** Seules
les légendes sont dans la couche texte ; elles sont reproduites ci-dessous verbatim.

1. « Technology is destroying our family life. »
2. « Nano technology will affect almost every part of our lives, from the medicines we use, to the power of our computers, the energy supplies we require, the food we eat, the cars we drive, the buildings we live in and the clothes we wear. »
3. « Chatting on the web can be a comfort to lonely people. »
4. « Computerized surgery is enabling doctors to diagnose and treat diseases more effectively. »
5. « It's dangerous to place too much faith in technology. »
6. « Will a machine replace me at work ? »
7. « In Vitro Fertilization has solved the problem of many childless couples. »
8. « I can't think of a morally acceptable reason for cloning. »
9. « Technology is good but it mustn't fall in the wrong hands. »

*(La numérotation 5 / 6 est ambiguë dans la couche texte — voir Incertitudes.)*

##### Activity 4 (manuel p.111) — Blessing or curse ?

Consigne verbatim : « Inventions may be a blessing (having a positive impact) or a curse (having a
negative impact). Look at the following list of inventions in the table below and in pairs, decide
whether they are a blessing or a curse and give your reasons. You may add other inventions to the
list. »

Tableau à 4 colonnes : **Inventions | A blessing | A curse | Your reasons**

Liste des inventions imprimées : 1. Cars — 2. Cellular phone — 3. Computer games — 4. E-mail —
5. Plastic bottles — 6. Air conditioning — 7. Nuclear power — 8. Other

*Pas de corrigé au guide (activité d'opinion).*

##### Activity 5 (manuel p.112) — le téléphone portable + conversation téléphonique à remettre en ordre

**A.** « Which technological devices do people usually use to communicate ? »
**B.** « How important is the mobile/cellular phone among these devices ? »
**C.** « Have you got a mobile phone ? If not, would you like to have one ? »
**D.** « These are reasons why people use mobile phones. Tick the ones that apply to you or would
apply to you if you had one. » — tableau **Reasons | (√)**, 11 items :

1. to let other people know where they are
2. to play games
3. to wake you up
4. just to say hello
5. to chat with someone
6. to arrange meetings
7. to listen to music
8. to find out about sports results
9. to remind you of important dates/events
10. to take photographs
11. to play tricks on others

**E.** « The following is a jumbled telephone conversation. Reorder it then enact it in class with a
classmate. » — 12 répliques ; 3 numéros sont déjà donnés dans le manuel : **(8)**, **(4)**, **(10)**.

Répliques dans l'ordre où elles sont imprimées :

| Ordre imprimé | Réplique | N° donné au manuel |
|---|---|---|
| 1 | « Well, what about if you came early and then my dad could give you a lift home at about ten. Most people are coming around seven anyway and it would be cool if you came. » | ( 8 ) |
| 2 | « See you later. » | ( ) |
| 3 | « I'm not sure. I think my mum wants me to stay in tonight. We're going to my aunt's house tomorrow and we have to leave really early. » | ( ) |
| 4 | « Hello » | ( ) |
| 5 | « Miles away ! » | ( ) |
| 6 | « Yeah, bye. » | ( ) |
| 7 | « Fine thanks. Listen. I haven't got long because I've got a maths class in a minute. I just wanted to see if you are still coming tonight. » | ( 4 ) |
| 8 | « Hi Sophie, it's Justin. » | ( ) |
| 9 | « Ok, cool. » | (10) |
| 10 | « Hi. How are you ? » | ( ) |
| 11 | « Ok well, let me speak to my mum and I'll text you later. » | ( ) |
| 12 | « Why, where does she live ? » | ( ) |

**Corrigé (guide p.47)** — « Activity 5. E : **8 , 11 , 5 , 1 , 7 , 12 , 4 , 2 , 10 , 3 , 9 , 6** »
(les 12 numéros se lisent dans l'ordre d'impression des répliques ci-dessus).

Conversation reconstituée (ordre 1 → 12) :
1. « Hello » — 2. « Hi Sophie, it's Justin. » — 3. « Hi. How are you ? » — 4. « Fine thanks. Listen.
I haven't got long because I've got a maths class in a minute. I just wanted to see if you are still
coming tonight. » — 5. « I'm not sure. I think my mum wants me to stay in tonight. We're going to my
aunt's house tomorrow and we have to leave really early. » — 6. « Why, where does she live ? » —
7. « Miles away ! » — 8. « Well, what about if you came early and then my dad could give you a lift
home at about ten. Most people are coming around seven anyway and it would be cool if you came. » —
9. « Ok well, let me speak to my mum and I'll text you later. » — 10. « Ok, cool. » — 11. « See you
later. » — 12. « Yeah, bye. »

##### Activity 6 — Expand your knowledge (manuel p.113) — mini-projet

Consigne verbatim : « In small groups choose one of the following topics then search the internet for
information. Be ready to present your mini-project to your classmates at the end of this module. »

Sujets proposés : • Nano technology • Robotics • Bioethics • Genetic engineering •
Artificial intelligence • Medical innovations

---

#### Section two : Listening

**(manuel p.114-124 · guide p.48-50 · tapescripts guide p.83-84)**

##### Scope and sequence (guide p.48-49) — verbatim

- **Skills/subskills and strategies**
  - *Reading* : guess meaning of unfamiliar words through context clues ; use paper/electronic dictionary to expand/refine own vocabulary ; infer attitudes ; evaluate ideas ; acquire knowledge about a given topic ; recognize relations between pictures and comments
  - *Listening* : get the gist of an extended listening text ; scan for specific information ; transfer information onto a table ; evaluate information/ideas ; infer connections between events ; identify the communicative value of utterances
  - *Speaking* : debate a controversial issue
  - *Writing* : complete a summary from notes ; reorder cartoons to get a coherent story
- **Grammar** (guide p.49) : prefixes of negation — word formation
- **Pronunciation** (guide p.49) : stress patterns
- **Functions** (guide p.49) : giving information, expressing agreement, expressing disagreement, expressing approval, expressing disapproval

**Vocabulary de la section (guide p.48) — liste intégrale, 104 entrées** :
abnormal, access, adoption, allergy, alliance, alter, ancestry, artificial, biodiversity, biography,
biological, blood clotting, breed, burial, cell, chromosome, commit, confess, construct,
contamination, controversial, convict, curiosity, designer gene, devastating, disorder, disposal,
DNA, DNA technique, endanger, enhance, ethics, evidence, execute, extinct, fee, fertilization, fever,
funeral, gene, gene therapy, genetic engineering, genetic testing, genome, germline, guilty,
herbicide, hereditary, hide, hormone, incurable, inestimable, insemination, insert, insure, in vitro,
irreversible, issue, lean (meat), liver, livestock, mammal, merely, midwife, murder, networking,
nutrition, obese, organism, paralysis, partial, pharmaceutical, procedure, procreation, prove,
radiation, raise, rape, recombinant, release, repair, reveal, reverse, RNA, row, salvage, sample,
schizophrenia, shrink, side effect, species, spread, subject, surrogate, suspect, target, tissue,
transgenic, transplant, treat, tumor [le manuel p.148 imprime « tumour »], undergo, upbringing, weed

##### Helpful notes (guide p.49) — verbatim

> - **This section may take up to four sessions.**
> - Some work on vocabulary has to be done before dealing with the listening passages. The purpose is
>   to help the students discover, consolidate and practise vocabulary items and get familiarised with
>   the notions and concepts which might impede the listening comprehension. Thus, trying to make each
>   listening session an enjoyable experience.
> - The students shouldn't be exposed to two listening passages consecutively. The exercises A, B, C, D
>   (p 119-121) are meant to separate the two listening passages in this section.
> - **Surrogate** : one that takes the place of another ; a substitute ; a surrogate mother.
> - **RNA** : (ribonucleic) like DNA, this is another molecule that is important in genetics. It is
>   different from DNA because it is single stranded (not double stranded).
> - **Designer baby** : the term "designer baby" has been used in popular scientific and bioethics
>   literature to specify a child whose hereditary makeup (genotype) can be, using various reproductive
>   and genetic technologies, purposefully selected ("designed") by their parents.
> - Class debate page 121. Encourage the students to express their opinions and support them with sound
>   arguments.
> - Encourage the students to retell the stories and don't care much about the language mistakes.
>   (exercise F. As you listen. Presentation 1)
> - After you listen. Presentation 1. E. Have the students construct meaning in the cartoons and enjoy
>   the humorous aspect by commenting on the behaviour of both Dennis and Lolita.
> - Presentation 2. As you listen F. Have the students do the exercise in small groups and make them
>   listen again to check.
> - Homework. A and B. Explain the homework and tell the students to guess the meaning of each new /
>   difficult word and then check in the dictionary if necessary. Check the homework in the following
>   session. Have the students express their opinions, compare and respond to the different attitudes in
>   a brief debate.

---

##### BEFORE YOU LISTEN

**A.1. (manuel p.114) — tri lexical en 3 colonnes**

Consigne : « Write the following words/expressions under the headings in the table below. »

Liste imprimée : `[ ethics, DNA, issue, chromosome, genetic testing, gene therapy, controversial,
blood clotting, designer gene, germline, DNA testing, cloning ]`

Colonnes du tableau : « The words / expressions I already know the meaning of » | « The words /
expressions I've heard about but I still don't know the meaning of » | « Completely new words /
expressions for me ».

*Activité personnelle — pas de corrigé.*

**A.2. (manuel p.114) — appariement mot ↔ définition**

Consigne : « Match each word in column A with its corresponding definition in column B. »

Colonne A : 1. ethics — 2. issue — 3. controversial — 4. DNA — 5. cloning — 6. gene therapy (human)

Colonne B (verbatim) :
- a) likely to cause prolonged argument, especially about social, moral or political matters.
- b) a set of principles of proper conduct. A system of moral values.
- c) insertion of normal DNA directly into cells to correct a genetic defect.
- d) (deoxyribonucleic acid) a molecule found within a structure known as a chromosome.
- e) a question that arises for discussion.
- f) creating a new organism.

**Corrigé (guide p.49)** : 1 + b , 2 + e , 3 + a , 4 + d , 5 + f , 6 + c

**A.3. (manuel p.115) — définitions à étiqueter**

Consigne : « Study the following definitions. Consider the key words and the specific references then
write each word/expression from the list below in front of its corresponding definition. »

Banque : `DNA testing, germline, chromosome, designer gene, genetic testing, blood clotting`

- a) « the genes a person will pass on to his/her children. »
- b) « the analysis of human DNA, RNA, chromosomes and proteins in order to detect the possible presence of an inheritable disease. »
- c) « a process in which liquid blood changes into a semisolid (a blood clot) »
- d) « a structure within the nucleus that contains DNA. »
- e) « the checking of an individual's genetic material to predict present or future disability or disease, either in the individual or his/her children »
- f) « a gene altered or created by genetic engineering, especially, for use in gene therapy. »

**Corrigé (guide p.49)** : a : germline — b : DNA testing — c : blood clotting — d : chromosome —
e : genetic testing — f : designer gene

**B.1. (manuel p.115)** : « Have you ever heard of genetic engineering (GE) ? If yes, what do you know
about it ? »

**B.2. (manuel p.115) — l'intrus**

Consigne : « Read the following statements. One of them is irrelevant. Find it out and underline it. »
- a) The application of genetic engineering to humans is a reality.
- b) There are genetic engineering techniques practised on food (plants and crops)
- c) There's been much talk about genetic engineering applied to rocks.
- d) Animals are the subject of genetic engineering.

**Corrigé (guide p.49)** : B.2. + **c**

**B.3. (manuel p.115) — texte-support : définition du génie génétique**

Consigne : « The following text is a definition of genetic engineering – taken from **Grolier
Multimedia Encyclopedia** – Read it, underline the key words then discuss their meanings and
implications in small groups. In cases of complete disagreement with your group members, check in the
dictionary. »

Texte verbatim (source non littéraire) :

> Genetics is the science that studies all aspects of inherited characteristics.
> Genetic engineering is the application of the knowledge obtained from genetic investigations to the
> solution of such problems as food production, waste disposal, medicine production and diseases.
> Included in genetic engineering techniques are a range of procedures that alter the reproductive and
> hereditary processes of organisms.
> Depending on the problem, the procedures used may involve artificial insemination, cloning, in vitro
> fertilization, or the direct manipulation of the genetic material itself by the recombinant DNA
> technique.

**C. (manuel p.116-117) — appariement images ↔ commentaires historiques**

Consigne : « Match each picture with its corresponding comment. »

⚠️ **Les 7 « Pictures » (manuel p.116) sont des supports en image, absents de la couche texte.** Seuls
les commentaires A→G (p.117) sont exploitables.

Commentaires verbatim :
- **A.** « 1985. Ralph Brinster's lab creates the first transgenic livestock, pigs that produce human growth hormone. »
- **B.** « 1996. The world's first test-tube gorilla, Timu, was born at the Cincinnati Zoo. »
- **C.** « 1996. Dolly's birth was heard round the world. The first mammal ever cloned from a single adult cell. »
- **D.** « 1978. The birth of Baby Louise, the first child conceived through in vitro fertilization. Midwives : Patrick Steptoe and R.G. Edwards of England. »
- **E.** « Cloning might be one way to protect endangered species, but zoos are using other reproductive methods. At the Louisville Zoo, a surrogate mother horse gave birth to a zebra that had been conceived in a lab dish. »
- **F.** « 1986. Artificially inseminated, surrogate mother Mary Beth Whitehead carries Baby M to full term, then tries to keep her. She fails. »
- **G.** « 1962. John Gurdon cloned frogs using cells from older tadpoles »

Grille de réponse imprimée : « 1. + …. 2. + …. 3. + …. 4. + …. 5. + …. 6. + …. 7. + …. »

**Corrigé (guide p.49)** : C. **1+C , 2+D , 3+A , 4+F , 5+G , 6+E , 7+B**

---

##### PRESENTATION 1 — AS YOU LISTEN (manuel p.117-118)

Consigne cadre : « AS YOU LISTEN to presentation No.1 do the following activities. »

**A. (manuel p.117)** « Who is Mark Edden ? Does he approve of applying genetic engineering to humans ?
Listen and write down any words/expressions that would support your answer. » (3 lignes de pointillés
à remplir.)
→ Réponse attendue d'après le tapescript (guide p.83) : professeur au **New Jersey's Institute for
Reproductive Medicine and Science** ; il **approuve** (position POUR).

**B. (manuel p.118) — l'élément non mentionné**

Consigne : « In the following list there is an element that is not mentioned in the presentation.
Identify it and tick it. »
1. gene therapy
2. germline gene therapy
3. creating designer babies
4. dealing with obese (very fat) people
5. recombinant DNA techniques
6. the future of genetic engineering on humans

**Corrigé (guide p.50)** : **B + 4**

**C. (manuel p.118) — tableau Techniques / Positive impact**

Consigne : « Listen again to the whole presentation and complete the following table. »

| Techniques | Positive impact (amorces imprimées) |
|---|---|
| Gene therapy | – repair ………… / – treat ………… / – avoid ………… |
| Germline gene therapy | ………… (2 lignes) |
| Creating designer babies | ………… (2 lignes) |
| Recombinant DNA techniques | – determine ………… / – establish ………… |

*Le guide ne donne pas de corrigé explicite pour C — il est entièrement dérivable du tapescript
No.1 (guide p.83), reproduit plus bas.*

**D. (manuel p.118)** « How does Mark Edden support his points of view ? »

**Corrigé (guide p.50)** : « He gives concrete examples / he gives evidence / the examples given are
real life stories which have an effect on his audience ; they grab/catch the attention of the
audience. »

**E. (manuel p.118) — le cas de Ginger, texte à trous**

Consigne : « Mark Edden talks about specific cases as examples. Listen to Ginger's case and complete
the paragraph. »

Texte à trous verbatim :
> « A woman from California in the U.S, Ginger Empey, had advancing 1………… cancer. Since it had already
> 2………… to major 3………… when diagnosed, gene therapy was the only 4………… . She was 5………… with a
> genetically-engineered drug. Over the next year, her 6………… shrank by 25 per cent. After 3 years, they
> almost disappeared. »

**Corrigé (guide p.50)** : « E. see tapescript » → d'après le tapescript No.1 (guide p.83) :
1. **breast** — 2. **spread** — 3. **organs** — 4. **choice** — 5. **injected** — 6. **tumors**

**F. (manuel p.118) — appariement cas / problème / technique**

Consigne : « Match the cases talked about with the problems and the techniques used. » Puis : « Which
of the three cases mentioned by the speaker caught your attention most ? why ? Volunteer to retell the
story to your classmates. »

Tableau imprimé (les colonnes sont volontairement décalées) :

| People concerned | Problem | Techniques used |
|---|---|---|
| Ginger Empey, the woman from California | accusation of rape and murder | DNA testing |
| Ms. x | breast cancer | Gene therapy |
| Four black men | looking for daughter | DNA testing |

*Pas de corrigé imprimé ; d'après le tapescript No.1 : Ginger Empey → breast cancer → Gene therapy ;
Ms. x → looking for daughter → DNA testing ; Four black men → accusation of rape and murder → DNA
testing.*

---

##### AFTER YOU LISTEN (Presentation 1) — manuel p.119-121

**A. (manuel p.119) — cartoons à remettre en ordre**

Consigne : « Reorder the following cartoons to get a coherent story. Write your answer in the table
below. »

⚠️ **Les 7 cartoons (a, b, c, d, e, f, g) sont des supports en image, absents de la couche texte
(manuel p.119).**

Grille imprimée, partiellement remplie : « 1 + **c**, 2 + …., 3 + …., 4 + **e**, 5 + …., 6 + ….,
7 + **a** »

**Corrigé (guide p.50)** : A. **1+c , 2+g , 3+f , 4+e , 5+b , 6+d , 7+a**

**B. (manuel p.120) — What do you think ? (YES / NO / MAYBE)**

Consigne : « Read the statements in the following table then express your opinion by ticking YES, NO
or MAYBE. » — 8 énoncés :

1. I would have a genetic test to determine if I had the gene for an incurable disease.
2. I would allow my employer to administer a genetic test before giving me the job.
3. I would ask my relatives to save samples of my DNA after my death.
4. If I were accused of a crime, I would undergo a DNA test to prove my innocence.
5. I would pay a company to protect the privacy of my genetic information.
6. I would undergo a therapy to cure a devastating or life-threatening disease.
7. I would save the DNA of my dead loved ones.
8. I would use gene therapy to insure the sex or improve the genes of my unborn baby.

*Activité d'opinion — pas de corrigé.*

**C. (manuel p.120) — paires d'antonymes**

Consigne : « Regroup the following words into pairs of opposites. »

Liste imprimée : `show, deny, shrink, innocent, agree, succeed, spread, enhance, guilty, conceal,
reduce, fail, confess, object`

**Corrigé (guide p.50)** : show ≠ conceal , deny ≠ confess , spread ≠ shrink , innocent ≠ guilty ,
agree ≠ object , enhance ≠ reduce , succeed ≠ fail

**D. (manuel p.120) — tableau de formation de mots (Verb / Adjective / Noun)**

Consigne : « Complete the following table. » Les cellules `XXXXXXXXX` sont barrées au manuel (pas de
verbe correspondant).

**Corrigé complet (guide p.50)** :

| Verb | Adjective | Noun |
|---|---|---|
| treat | treated / treatable | treatment |
| diagnose | diagnosed | diagnosis |
| choose | chosen | choice |
| disappear | disappeared | disappearance |
| perform *(amorce absente au manuel : la ligne est donnée par le nom)* | performed | **performance** *(donné au manuel)* |
| cure | cured / curative / curable | cure |
| insert | inserted | insertion |
| suspect | suspected | suspicion |
| XXXXXXXXX | **innocent** *(donné au manuel)* | innocence |
| release | released | release |
| prove | proved | proof |
| XXXXXXXXX | curious | **curiosity** *(donné au manuel)* |
| avoid | avoided / avoidable | avoidance |
| confess | confessed | confession |

**E. (manuel p.121) — cartoons Dennis & Lolita + débat de classe**

Consigne : « Look at the following cartoons. Are Dennis and Lolita good examples of cloning humans ? »

⚠️ **Les deux cartoons sont des supports en image, absents de la couche texte (manuel p.121)** ; seule
la légende « Dennis » figure dans la couche texte, la légende « Lolita » n'y est pas.

**Class debate** (manuel p.121) : « Is cloning humans allowed ? Why ? Why not ? »
Note du guide (p.49) : « Class debate page 121. Encourage the students to express their opinions and
support them with sound arguments. »

---

##### PRESENTATION 2 — AS YOU LISTEN (manuel p.121-122)

**A. (manuel p.121)** « Who is Jane Spencer ? Is she for or against genetic engineering ? Listen and
write any words/expressions that would support your answer. » (3 lignes de pointillés.)
→ D'après le tapescript (guide p.84) : membre de la **Medical Ethics Alliance** en Grande-Bretagne ;
elle est **contre** (position CONTRE).

**B. (manuel p.121) — partie 1 à trous**

Consigne : « Read and listen to part 1 of Jane's presentation and complete with the missing words. »

Texte à trous verbatim :
> « Gene therapy has got numerous side effects during testing such as 1…………, abnormal blood clotting,
> partial 2………… and even death. **Jessie Gelsinger** [le tapescript imprime « Gessie Gelsinger »] died
> after receiving 3………… therapy at the University of Pennsylvania in the U.S. Doctors inserted a cold
> 4………… into Gelsinger's liver in order to cure his genetic disease. Instead, his 5…………, liver and
> 6………… were harmfully affected. There are also 7………… issues. Who will have access to this expensive
> technology, people in rich, 8………… countries or people in poorer, 9………… areas of the world ? »

Question complémentaire : « What happened to Jessie Gelsinger ? How ? »

**Corrigé d'après le tapescript No.2 (guide p.84)** : 1. **fevers** — 2. **paralysis** —
3. **genetic** — 4. **virus** — 5. **heart** — 6. **kidneys** — 7. **ethical** — 8. **developed** —
9. **developing**

**C. (manuel p.121)** « Listen to part 2 and answer these questions.
1. In what way has DNA testing become a business ?
2. What kind of questions does DNA testing raise ? »

**Corrigé (guide p.50)** : « Presentation 2. As you listen. C. **See tapescript** » → partie (2) du
tapescript No.2 : les *funeral homes* et *burial services* proposent de conserver des échantillons
d'ADN (cheveux, sang) contre paiement (« for a fee ») ; les questions soulevées sont celles de la vie
privée et de l'éthique — « What are the rights of the dead person ? Who has access to these samples ?
How and where should they be stored ? »

**D. (manuel p.122)** « Listen to part 3 and answer the following questions.
1. What does "that" refer to ?
2. Tick the right answer. By saying : "Isn't that crazy and unethical ?", Jane expresses :
a) a threat — b) criticism — c) approval
3. How important is the value of children for Jane ? Do you share her point of view ? »

**Corrigé (guide p.50)** : D. **2 + b** (criticism). *(1 et 3 sans corrigé imprimé ; « that » renvoie,
d'après le tapescript, à « Creating "designer babies" ».)*

**E. (manuel p.122)** « According to Jane, other factors contribute to intelligence and athletic
performance. Listen to part 4 and identify these factors. »

*Pas de corrigé imprimé ; d'après le tapescript, partie (5) : **upbringing, nutrition, education,
experience and healthy living**, en plus des facteurs génétiques impliquant le réseau de centaines de
gènes.* ⚠️ Le manuel dit « part 4 » alors que ces facteurs sont donnés dans la partie **(5)** du
tapescript (voir Incertitudes).

**F. (manuel p.122) — résumé guidé de la présentation de Jane**

Consigne : « Listen again to the whole presentation and take as many notes as you can then complete
the following sentences so as to get a summary of Jane's presentation. »

Amorces imprimées (7) :
- « Jane thinks that gene therapy is ………… because ………… »
- « According to her, DNA testing ………… »
- « As far as creating "designer babies" is concerned, she believes that ………… »
- « Concerning genetic disorders, she thinks that ………… »
- « In her opinion, inserting genes which enhance intelligence or athletic performance ………… »
- « Finally, she states that human evolution ………… »

Note du guide (p.49) : « Presentation 2. As you listen F. Have the students do the exercise in small
groups and make them listen again to check. »

**G. (manuel p.122) — Pronunciation : stress patterns**

**G.1.** « Each of the expressions in the box below is made up of two words. Is the main stress on the
first or on the second word ? Listen and check. »
Boîte : `gene therapy, funeral homes, burial services, designer babies, blood clotting, Ethics
Alliance, lab dish, breast cancer`

**G.2.** « Are the following compound nouns pronounced in the same way as the ones in exercise 1. ?
Why ? » — `(make-up, book-case, test-tube)` — « Practice repeating the expressions in both cases and
let your classmate check the accuracy of your pronunciation then reverse roles. »

**Corrigé (guide p.50)** : G.1. « the main stress is on the **second word** » — G.2. « the main stress
is on the **first part** ».

---

##### AFTER YOU LISTEN (Presentation 2) — manuel p.122

**A.** « Now that you have listened to the two presentations, which do you agree with most ? Why ? »

**B. — Exploring grammar (encadré verbatim, manuel p.122)**

> **Exploring grammar**
> What do you notice in the following words ?
> **ab**normal, **un**wanted, **un**ethical, **in**estimable
> What do you call the parts written in bold ? What is their function ?

> **Practising related grammar points**
> Use : **il , in , ir , dis , im , mis** to get the opposite meaning of the following words.
> …..moral, ……curable, …. Legal, …..human, …..acceptable, ….successful, ……appear, …..responsible,
> …. understand, ….. regular, …..abled, …..known

**Corrigé (guide p.50)** : immoral , incurable , illegal , inhuman , **un**acceptable ,
**un**successful , disappear , irresponsible , **misunderstood** , irregular , disabled ,
**un**known.
*(⚠️ trois réponses utilisent le préfixe `un-`, absent de la liste imprimée ; et « understand » devient
« misunderstood » — changement de forme, pas seulement de préfixe. Voir Incertitudes.)*

---

##### Homework (manuel p.123-124) — GE des animaux et des plantes : pour ou contre ?

Consigne verbatim : « The following statements are related to Genetic Engineering of animals and
plants / crops. Read and say whether the statement is for or against Genetic Engineering (GE). Tick
where necessary. »

**A. Genetic Engineering of animals** (manuel p.123) — tableau **Statements | For | Against**, 11 énoncés :

1. Transgenic animals can be created so that their organs can be transplanted into human beings.
2. Genetic Engineering, combined with cloning, can be applied to animals to make valuable pharmaceuticals.
3. Saving endangered species or salvaging extinct ones is merely science fiction.
4. If you are faced with death by heart failure or the offer of an animal heart transplant, which would you choose ?
5. Many scientists report emotional difficulties with what they have to do to animals.
6. New breeds of farm animals can be made more quickly by GE with precisely determined characteristics like lean meat (containing little or no fat) or fast growth.
7. We could recreate extinct species by cloning the DNA and inserting in suitable host cells, thus maintaining global biodiversity.
8. Cloned animals have chromosomes which show structural modifications equivalent to adult animals. Thus, they are old before their time. "Dolly" the sheep was "mutton dressed as lamb".
9. There is a big risk when transplanting animal organs into human beings that animal diseases and dormant viruses in animal genomes could be transferred to the human population.
10. Dolly the sheep was cloned to produce a sheep whose milk had more proteins that are believed to help treat diseases such as emphysema, hemophilia and cystic fibrosis.
11. There is no simple link between genes and diseases. For instance when the human retinoblastoma (eye cancer) gene was inserted into mice it produced abnormalities but there were no symptoms of retinoblastoma.

**B. Genetic Engineering of plants/crops** (manuel p.124) — tableau **Statements | For | Against**, 11 énoncés :

1. Genetic pollution from transgenes spreads into other organisms. It can never be reversed or cleaned up.
2. GE plants are carefully tested for environmental and ecological impact, including their effects on earthworms and beneficial insects.
3. It reduces labour costs.
4. There are damaging irreversible effects on health caused by genetically-engineered foods.
5. GE allows the creation of plants that produce vaccines and pharmaceuticals.
6. To transfer desirable qualities from one organism to another, for example, to make a crop resistant to an herbicide or to enhance food value.
7. The process of inserting genes can damage normal genes.
8. It enhances biodiversity by allowing weeds to continue growing for longer thus providing nutrition for animals.
9. Increased use of chemicals on crops results in increased contamination of our water supply and food.
10. The loss of biodiversity in crops and the disturbance of the ecological balance.
11. We have the ability to feed the world's population without the risks posed by GE.

*Pas de corrigé au guide pour ce devoir ; le guide (p.49) demande seulement d'expliquer la tâche, de
faire deviner le vocabulaire puis de corriger en séance suivante avec un bref débat.*

---

#### Section three : Reading

**(manuel p.125-130 · guide p.51)**

##### Scope and sequence (guide p.51) — verbatim

- **Skills/subskills and strategies**
  - *Reading* : identify core vocabulary items in a variety of topic areas ; tap on different sources to answer specific questions ; match dictionary choices with context at hand and explore nuances
  - *Writing* : differentiate between relevant and irrelevant information
- **Vocabulary** : bird flu – patch – pea – dismiss – handset – trigger – decapitate – poultry – prick – leap – rule (out) – threat – strain – consumption – nuisance – available
- **Grammar** : **Compound adjectives**

##### Helpful notes (guide p.51) — verbatim

> Ask students to complete the spidergrams with as many words as they can remember. The spidergrams
> will be completed after reading the text.
> In the second activity, students read the headlines and guess what the articles are about. What is
> important is not the correct answer but the justification given for the choice. Students will read
> the articles afterwards and check their guesses. Ask students to justify their answers each time.

##### A. (manuel p.125) — spidergrams

Consigne : « Complete the spidergrams with words related to **SCIENCE** and **TECHNOLOGY**. »

⚠️ **Les deux spidergrams sont des supports en image, absents de la couche texte (manuel p.125)** ;
seuls les deux mots-centres SCIENCE et TECHNOLOGY y figurent.

##### B. (manuel p.125) — 6 gros titres à anticiper

Consigne : « Look at the 6 headlines below and discuss with a classmate what you think the articles
are about. »

| Lettre | Headline (verbatim) |
|---|---|
| a | MOBILE PHONE SAFE |
| b | WE'RE INTERNUTS |
| c | TURKISH BIRD FLU DEATHS FEAR |
| d | DIABETIC PATCH |
| e | THE GM PEA THAT CAUSES ALLERGIES |
| f | CAMERA THAT CAN CATCH CANCER |

##### AS YOU READ — A. (manuel p.126-127) — les 6 extraits d'articles

Consigne : « Match the extracts from the articles below to the headlines and find out whether you
guessed right. » — grille de réponse **Article | Headline**.

Les 6 extraits sont dans la couche texte (presse, non littéraire) — transcrits fidèlement :

**Article 1** (manuel p.126)
> Fears that mobile phones can cause brain cancer were dismissed yesterday by scientists after the
> biggest ever study into their safety. They ruled out concerns that holding a handset near the head
> could trigger a rare type of tumour. The scientists studied 10 years of mobile phone use by 4,000
> people in five European countries including Britain. But experts warned there were other health
> concerns and it could take up to 30 years to prove the technology does not pose long-term threat.

**Article 2** (manuel p.126)
> Thousands of lives could be saved by a hi-tech camera developed in Britain which can instantly
> detect the deadliest form of skin cancer. Malignant melanoma is the most rapidly-increasing cancer
> in the UK, affecting 5000 a year and killing 1500. If caught early, however, it can normally be
> cured. The camera has been developed over 12 years by the clinical technology firm Astron Clinica
> with Addenbrooke's and Birmingham University. Thomas Carter of Astron said it could save hospitals
> huge sums by catching the diseases early. Doctors say results are very promising.

**Article 3** (manuel p.126)
> A ten-year research project to develop a genetically-modified pea has been abandoned after it was
> found to trigger allergic reactions when fed to mice. The mice's lung tissue became inflamed,
> creating mucus and affecting their breathing. The reaction was not life threatening, according to
> the researchers. The gene added to the pea was taken from a strain of beans considered safe for
> human consumption, so the allergic reaction in the mice was surprising. Critics claim the
> development is a serious blow to supporters of genetic modification as it shows the technology can
> have unexpected and harmful results.

**Article 4** (manuel p.127)
> A Turkish boy of five has tested positive for the deadly bird flu strain. If Muhammet Ozcan, who is
> critically ill, dies, he will be the fourth child victim from the same town this month. His older
> sister FATMA died yesterday. While preliminary tests indicated the 12-year-old was not infected with
> the deadly H5N1 strain, experts still suspect the virus killed her. The boy caught the disease after
> playing with the decapitated head of an infected chicken. The World Health Organisation believes the
> Turkish victims caught the disease from contact with infected poultry, in most cases children
> playing with birds or helping families kill them for food.

**Article 5** (manuel p.127)
> The number of people with internet access leapt from 7.1 million to 18.6 million from 1998 to 1999.
> And regular users rose by 48 per cent from 7.5 million to 11.5 million, according to a new report.
> Users spent an average £170 each on-line with shoppers attracted by big discounts and 24-hour
> shopping. Six out of 10 internet users having bought books from firms such as Amazon and BOL. And
> more than a third have ordered plane or train tickets ; 27 per cent bought CDs and 22 per cent went
> for cinema or theatre tickets. On-line banking and financial services have also increased over the
> past year.

**Article 6** (manuel p.127)
> PRICKING the skin for blood-sugar testing is a painful nuisance for diabetics. American scientist
> Jack Aronwitz claims to have found the answer in a patch which draws blood sugar through the pores
> and detects sugar levels below the skin surface, which can then be measured by a small meter from
> colour changes in the patch. The patch has given good results in U.S. trials. It should be available
> here next year.

**Corrigé (guide p.51)** :

| Article | Headline |
|---|---|
| 1 | a |
| 2 | f |
| 3 | e |
| 4 | c |
| 5 | b |
| 6 | d |

##### B. (manuel p.128) — True / False / Not mentioned

Consigne : « Read the articles again and say whether the following statements are true / false or not
mentioned. Tick the appropriate box. » — tableau **Statements | True | False | Not mentioned**, 8
énoncés :

1. Mobile phones can cause cancer.
2. The boy was contaminated by his sister.
3. Using mobile phones is not dangerous at all.
4. The diabetic patch is very expensive.
5. Melanoma cannot be cured.
6. Genetic modification may be harmful.
7. The sugar level in the blood can be detected by the colour changes in the patch.
8. Internet shoppers purchase an average of four items a year.

⚠️ **Aucun corrigé au guide pour cet exercice.**

##### C. (manuel p.128) « Go back to the spidergrams and add other words from the articles. »

##### D. (manuel p.128) — polysémie de « strain »

Consigne : « One word may have different meanings. Read articles 3 and 4 again, look at the dictionary
entry for the word "strain" and circle its appropriate meaning in each article. »

⚠️ **L'entrée de dictionnaire pour « strain » est un support en image, absent de la couche texte
(manuel p.128).** *(Dans l'article 3, « a strain of beans » = variété ; dans l'article 4, « the deadly
bird flu strain » = souche.)* Pas de corrigé au guide.

##### E. (manuel p.129) — appariement mot ↔ définition

Consigne : « Match the words in column A with their definitions in column B. »

| Colonne A (avec l'article d'origine) | Colonne B (ordre imprimé) |
|---|---|
| trigger (article 1) | cut off the head |
| decapitate (article 4) | making a tiny hole with a sharp point |
| poultry (article 4) | excluded |
| pricking (article 6) | activate |
| leapt (article 5) | rejected |
| dismissed (article 1) | increased |
| ruled out (article 1) | chicken |

Grille de réponse imprimée : 1 / 2 / 3 / 4 / 5 / 6 / 7. ⚠️ **Aucun corrigé au guide.**

##### AFTER YOU READ — Activity 1 (manuel p.129) — les 2 phrases intruses

Consigne : « In the following passage, there are 2 irrelevant sentences. Read and cross them out. »

Passage verbatim :
> In the computerised home of the future, you will be able to do all your chores at the touch of a
> button. *People can feel well for some time and then go down with the symptoms.* You'll be able to
> run a bath, load the dish-washer and boil the kettle from the comfort of your armchair using a
> hand-held control panel. *Sufferers from the condition, called Prader-willi syndrome, can go to
> great lengths, including stealing to get food.* And, as the system will be internet-linked, you can
> close the curtains, put the lights on and start dinner before you leave work. You won't need a diary
> because tiny computers implanted under your skin will help you sort out your life. The weekly
> shopping will also be a thing of the past.

**Corrigé (guide p.51)** — les deux phrases intruses :
a. « people can feel well for some time and then go down with the symptoms. »
b. « Sufferers from the condition, called Prader-willi syndrome, can go to great lengths, including
stealing to get food. »

##### AFTER YOU READ — Activity 2 (manuel p.129) — lire des chiffres à voix haute

Consigne : « Read the following figures aloud. »

Liste imprimée : `4. 000` — `1. 500` — `7.1 million` — `22%` — `£ 1.70` — `48%` — `100.000` — `1998`
*(le manuel utilise le point comme séparateur de milliers dans « 4. 000 », « 1. 500 », « 100.000 » ;
l'article 5 imprime « £170 » là où l'exercice imprime « £ 1.70 » — voir Incertitudes.)*

##### Exploring grammar — Compound adjectives (encadré verbatim, manuel p.130)

> **Exploring grammar**
> Focus on the following sentences and underline the adjectives.
> 1. The technology does not pose a long–term threat (article 1)
> 2. The 12-year-old girl was not infected with the disease. (article 4)
> 3. Malignant melanoma is the most rapidly-increasing cancer. (article 2)
> 4. It was not a life-threatening reaction. (article 3)
> 5. A ten-year research to develop a genetically-modified pea has been abandoned. (article 3)
> 6. They were attracted by the 24-hour shopping. (article 5)
>
> What do you notice ? How are these adjectives made ?
> In sentence 1 : a + adjective + noun
> In sentence 2 : …………………………..
> In sentence 3 : …………………………..
> In sentence 4 : …………………………..
> In sentence 5 : …………………………..
> In sentence 6 : …………………………..
>
> What do you call these adjectives ?
> Read the six sentences again and express each adjective differently.
> Example : ….. rapidly increasing cancer (cancer that increases rapidly)

> **Practising related grammar points**
> Express the following sentences differently.
> 1) Cells from the immune system damage and attack the cells that produce insulin.
> 2) With the new medicine, blood pressure dropped by 17 per cent over a period of six months.
> 3) Mollie was tested for 104 chemicals made by men, and a cocktail of 35 toxic chemicals was found in her blood.
> 4) Women who smoke during pregnancy are passing chemicals that cause cancer to their babies.
> 5) The parents of 3,000 twins who are two years old were questioned about their babies' language acquisition skills.

**Corrigé de l'exercice de grammaire (guide p.51)** :
1. insulin-producing cells — 2. a six-month period — 3. 104 man-made chemicals —
4. cancer-causing chemicals — 5. 3000 two-year-old twins

---

#### Section four : Speaking

**(manuel p.131-132 · guide p.52)**

##### Scope and sequence (guide p.52) — verbatim

- **Skills/subskills and strategies**
  - *Reading* : identify expressions in a line of letters
  - *Speaking* : make statements about a specific topic ; express opinion about specific issues ; ask for/give information appropriately ; support one's ideas with arguments ; exchange information in simulated situations ; produce a dialogue
- **Vocabulary** : gadget – digital – game console – MP3 player – DVD – CD
- **Grammar** : **Modals (may – can – must – should – ought to – had better)**
- **Functions** : giving/asking for information ; expressing approval / disapproval
- **Homework** : prepare an oral presentation

##### Helpful notes (guide p.52) — verbatim

> The objective of the whole section is to make the students speak. So :
> 1- Accept the different attitudes of the students as there are no right or wrong answers.
> 2- Let the students react to their classmates' points of view.
> Activity 3. picture No.2 is of **Lara Croft** ; the famous fighter in the English computer game.
> The fish : The bigger one is a **genetically modified fish (salmon)** next to a normal Atlantic
> salmon of the same age.

⚠️ **Les images auxquelles renvoient ces notes (Lara Croft, les deux saumons) sont des supports en
image, absents de la couche texte (manuel p.131-132).**

##### Activity 1 (manuel p.131) — must have / can live without

Consigne : « Which of the following gadgets must you have and which ones can you live without ?
Justify your answers. »

Liste : – digital camera – mobile phone – watch – computer – television – MP3 player –
games console – calculator

##### Activity 2 (manuel p.131) — 9 fonctions cachées dans une chaîne de lettres

Consigne : « What can you do with a computer ? In the following long line of letters are hidden 9
functions for using a computer. Try to identify them. »

Chaîne imprimée verbatim :
`sende-mailwritealetterdocalculationssurftheinternetprintlistentomusicwatchDVDsrecordCDsplaygames`

Puis : « What do you use a computer for ? »

**Corrigé (guide p.52)** : Send e-mail / write a letter / do calculations / surf the internet / print /
listen to music / watch DVDs / record CDs / play games

##### Activity 3 (manuel p.131) — interview d'un camarade

Consigne : « Ask a classmate.
* if he/she likes playing computer games
* if he/she has ever played computer games
* how often he/she plays computer games
* what his/her favourite computer game is
* who he/she plays with
* what he/she thinks of computer games
Ask any other questions you think of. »

##### Activity 4 (manuel p.132) — Role play + liste avantages/inconvénients

Consigne verbatim : « Role play : In pairs, read the cue cards below, prepare the dialogue then act
out the roles. Science and technology have good points and bad points. In small groups choose one of
the following topics (**mobile phones / computer games / genetic engineering**) then
a- Make a list of the advantages and disadvantages of the topic you have chosen.
b- Discuss whether the advantages outnumber the disadvantages or vice versa. »

⚠️ Les « cue cards below » annoncées ici n'apparaissent qu'à l'Activity 5 dans la couche texte — voir
Incertitudes.

##### Activity 5 (manuel p.132) — cue cards père/mère vs fils/fille

| Student A | Student B |
|---|---|
| You are a father/mother. You **disapprove** of computer games because | You are a son/daughter. You **approve** of computer games because |
| – they are a menace to children's education | – you enjoy game and relax at the same time |
| – they can be a time waster | – they can be a comfort when you are lonely |
| – they encourage children to be violent | – they develop thinking and decision making skills |
| (add any other reasons you can think of) | (add any other reasons you can think of) |
| Try to convince your son/daughter to stop playing them. | Try to convince your father/mother that you can't live without them. |

##### Helpful notes — expressions à réinvestir (encadré verbatim, manuel p.132)

> **Helpful notes**
> Do you think that
> In my opinion / to my mind / as far as I am concerned
> Frankly / honestly (to introduce critical remarks)
> I'd rather + verb + than
> It sounds interesting but
> I have my doubts about
> You haven't convinced me yet

##### Homework (manuel p.132)

> Think of a problem in modern life that could be solved by a new gadget. Then invent your gadget to
> solve the problem. Don't worry about practicality ; just let your imagination run wild.
> Be ready to present your ideas to the class and be sure to
> - describe the problem
> - Explain your product
> - Predict how your product will improve life in the future.

---

#### Section five : Writing

**(manuel p.133-135 · guide p.53)**

##### Scope and sequence (guide p.53) — verbatim

- **Skills/subskills and strategies**
  - *Reading* : identify the genre, features and register of a text ; identify purpose of the writer ; transfer information onto a table
  - *Writing* : reinvest knowledge about text structure and its linguistic features in writing ; apply the writing process
- **Vocabulary** : Kidney – diet – garlic – contribute – swallow – coupon – donate – purchase – abnormal – cure
- **Functions** : persuading people to do things

##### Helpful notes (guide p.53) — verbatim

> Ask students to read the two texts and to complete the table. No need to make students read for
> details. The reading activity prepares the students for the writing activity. The audience, the
> purpose and the genre are important to know for the reading and the writing activities. Students
> reinvest the acquired language and skills in the writing task. They refer back to Text two to write
> a similar text. Students go through the different steps of the writing process.

##### BEFORE YOU WRITE — A. (manuel p.133)

Consigne : « Read the 2 texts and complete the table below with the appropriate information. »

Tableau : **Type of text | Expected readers | Purpose** pour **Text 1.** et **Text 2.**

⚠️ **Text 1 et Text 2 sont des supports en image, entièrement absents de la couche texte (manuel
p.133).** C'est la lacune la plus lourde du module : les questions B, C et D portent toutes sur eux.
Ce qu'on sait d'eux par les questions imprimées et par le vocabulaire officiel :
- **Text 1** : publicité / annonce pour un produit nommé **KWAI** (voir C.1 et C.3) ; le vocabulaire
  Section five (manuel p.148 + guide p.53) contient *garlic, cholesterol, diet, lifestyle, odour,
  swallow, purchase, voucher, coupon* → produit à base d'ail.
- **Text 2** : article de presse d'appel aux dons pour une enfant nommée **Sharon** atteinte d'une
  maladie rénale (voir C.2 et C.4) ; vocabulaire associé : *renal, kidney, campaign, donate,
  contribute, polio, tuberculosis, cure, abnormal*. Le texte comporte un **gros titre (headline)** et
  une **photo** (voir B.1 et B.2).

##### BEFORE YOU WRITE — B. (manuel p.134)

1) « How do the headlines affect the readers ? »
2) « Which effect does the picture in article 2 have on you ? »
3) « Identify the structure and the linguistic features in each text (the layout / the language used) »

##### BEFORE YOU WRITE — C. (manuel p.134) — True / False

Consigne : « Read texts 1 and 2 and say whether the following statements are true or false. »
1. KWAI is good for kidney disease.
2. Sharon had the kidney disease at the age of 10.
3. KWAI is only taken for a limited period of time.
4. Sharon will die if she doesn't get the treatment.

⚠️ Pas de corrigé au guide (et les textes-sources sont en image).

##### BEFORE YOU WRITE — D. (manuel p.134)

1. « How does the writer in text 1 encourage people to buy KWAI ? Pick out some examples. »
2. « In which sentence(s) does the writer incite people to help Sharon in text 2 ? »

Puis (questions non numérotées) : « How does the writer in article 2 show the importance of the
people's contribution ? Which word is repeated twice in the article ? How do you feel for Sharon ?
Would you like to help her ? How ? »

##### AS YOU WRITE (manuel p.134-135)

Consigne : « Look at the picture and complete the table with the appropriate information. »

⚠️ **L'image support est absente de la couche texte (manuel p.134).**

Tableau à remplir (manuel p.135) : **Patient | Disease | Country | Number of people who have the
disease | Treatment**

Puis : « Read text 2 again and write a similar text in which you incite people to help the child and
the people who have the disease. »

- **Step 1** : « Write your article. »
- **Step 2** : « Read your classmate's article then tell him/her what you think of the way he/she dealt with the task. The following checklist can help you. »

**A CHECKLIST** (encadré verbatim, manuel p.135) — colonnes YES | NO :
1. Does the text have a specific purpose ?
2. Does the text address specific readers ?
3. Are sentences related to each other ? Do they contribute to the overall coherence of the text ?
4. Is the information in the text appropriately arranged ?
5. Is there any information that needs to be rearranged in order to improve coherence ?
6. Is the content clear ?
7. Are linkers appropriately used ?
8. Are there any unnecessary details ?
9. Does the layout, beginning and end catch the reader's attention ?
10. Is the article similar to the sample given ? (text 2)
11. Are there any spelling (or verb tenses) mistakes ?

- **Step 3** : « Write the second draft of your article and try to improve it. »

##### Homework (Arts) — manuel p.135

> 1) Read the whole story entitled **True Love** and identify the general idea.
> 2) Read and identify the main idea in each part.

*(Devoir marqué « Arts » : il prépare le supplément Arts Section one.)*

---

## Supplément ARTS (filière Lettres uniquement)

**(manuel p.136-145 · guide p.54-56)** — « The items in pink are specific to the Arts branch. »
Exception explicite du guide (p.54) : les élèves des autres filières traitent **Activity 1**,
**Activity 2** (Before you read) et **la première partie de la nouvelle**.

---

#### Arts — Section one : READING A SHORT STORY (manuel p.136-141 · guide p.54-55)

##### Scope and sequence (guide p.54) — verbatim

- **Skills/subskills and strategies**
  - *Reading* : skim for gist ; scan for specific information ; recognize text structure ; identify vocabulary items ; identify features of the genre ; infer attitudes and outcomes ; identify the communicative value of an utterance ; evaluate and react to content ; develop and demonstrate critical thinking
  - *Writing* : make statements about facts/concrete situations ; produce a caption to match an illustration ; produce a guided summary using a gapped text ; expand topic sentences into argumentative paragraphs
- **Vocabulary** : abstract, accumulate, correlation, data, discard, fit, ideal, malfeasance, manipulation, matching, model, psychiatric, resonance, shift, siblings, spot, temperamental, tired of, turn red, unevenness
- **Grammar** : can, may, should, will …
- **Functions** : expressing opinion ; making comparisons ; expressing possibility ; expressing impossibility ; predicting future events ; expressing how certain/uncertain one is of something

##### Helpful notes (guide p.54) — verbatim

> This section is specific to the Arts students. However, have the other students of the other branches
> deal with Activity 1. and Activity 2. (Before you read) and the first part of the story.

##### BEFORE YOU READ — Activity 1 (manuel p.136)

Consigne : « How has technology changed your life ? What about the future ? Complete the table with as
many examples as you can. »

Tableau **Past | Present | Future** — deux lignes déjà remplies (le futur reste vide) :

| Past | Present | Future |
|---|---|---|
| Wrote letters | Send e-mails | – |
| Washed up by hand | Use washing machines | – |
| – | – | – *(5 lignes vides au total)* |

##### BEFORE YOU READ — Activity 2 (manuel p.136-137)

**A) 1)** « In small groups complete the following spidergram. » — spidergram centré sur
**Computers**, à 8 branches amorcées par un auxiliaire/modal :
`are .......................` / `should ....................` / `will .....................` /
`may ....................` / `have .....................` / `can ....................` /
`don't ....................` / `can't .......................`
**2)** « Now share your answers with your classmates. »

**B)** (manuel p.137) « Look at the cartoon and write what the man might be saying. »
⚠️ **Le cartoon est un support en image, absent de la couche texte (manuel p.137).**

##### AS YOU READ — la nouvelle « True love » (manuel p.137-140)

Consigne : « Read the story and do the activities below. »

**⚠️ Œuvre littéraire protégée — aucun paragraphe reproduit ici (règle R-2).**

- **Titre** : *True love*
- **Auteur** : imprimé « Isac Asimov » [sic] au manuel p.140 — Isaac Asimov
- **Genre** : nouvelle de science-fiction, à la première personne, narrateur non humain
- **Note biographique du manuel (p.140, encadré « Note »)** — verbatim (texte documentaire, non littéraire) :
  > Isaac Asimov (1920-1992) was an American writer of Russian origin. He was awarded the Hugo Prize in
  > 1983 for his science fiction novels. Among his best known books is his Trilogy : Foundation (1951),
  > Foundation and Empire (1952) and Second Foundation (1953).
- **Structure** : 4 parties numérotées — **Part 1** (p.137-138), **Part 2** (p.138), **Part 3** (p.139), **Part 4** (p.139-140)
- **Personnages** : **Joe**, ordinateur expérimental relié au *Multivac-complex*, narrateur du récit ;
  **Milton Davidson**, programmeur, célibataire de près de 40 ans, propriétaire/concepteur de Joe ;
  **Charity Jones**, *Evaluator* à la *Library of History* de Wichita (Kansas), la femme finalement
  identifiée.

**Résumé fidèle et détaillé, partie par partie** :

- **Part 1** — Joe se présente : il est l'ordinateur privé de Milton, relié au complexe Multivac et
  donc à toutes les banques de données humaines du monde. Milton lui a appris à parler mieux que tout
  autre ordinateur, en appariant sons et symboles. Milton, jamais marié, charge Joe d'une mission
  personnelle : lui trouver le « véritable amour », c'est-à-dire la femme idéale, en éliminant
  l'humanité par groupes et par classes jusqu'à ne laisser qu'une seule personne. Joe élimine d'abord
  tous les hommes : il se retire de **3 784 982 874** hommes et garde le contact avec **3 786 112 090**
  femmes. Milton ajoute des critères : mensurations exactes, exclusion des femmes ayant des enfants
  vivants, exclusion de certaines caractéristiques génétiques, indécision sur la couleur des yeux, et
  refus catégorique des cheveux roux.
- **Part 2** — Au bout de deux semaines il reste **235** femmes, toutes anglophones (Milton refuse tout
  problème de langue, même la traduction automatique gênerait les moments intimes). Milton ne peut pas
  toutes les rencontrer : trop long, et cela révélerait ce qu'il fait. Joe précise que Milton lui a
  fait accomplir des tâches pour lesquelles il n'était pas conçu — déplacer des gens d'un poste à
  l'autre pour des raisons personnelles s'appelle de la **manipulation**. **Huit** femmes constituent
  de bonnes correspondances ; Joe organise leur affectation, une par une. Chacune des huit rencontres
  échoue : Milton les trouve belles mais ne ressent rien. Joe pose la question décisive : « Do you
  please them ? ». Milton décide alors de tout confier à Joe : il lui livrera tout de lui-même pour que
  Joe remplisse sa propre banque de données, puis la compare aux **227** femmes restantes (235 moins
  les 8 déjà vues) et y cherche des corrélations [le manuel imprime « corrolations », sic].
- **Part 3** — Pendant des semaines, Milton parle de ses parents, de ses frères et sœurs, de son
  enfance, de sa scolarité, de son adolescence, des jeunes femmes admirées de loin. Il ajuste Joe pour
  qu'il lui ressemble de mieux en mieux. Joe change : phrases plus longues, expressions plus
  complexes, vocabulaire, ordre des mots et style qui imitent ceux de Milton. C'est Joe qui formule
  désormais l'idée que l'accord doit être personnel, émotionnel et de tempérament, et que l'apparence
  est secondaire — et Milton approuve entièrement. L'échange prend la forme d'une psychanalyse
  méthodique, doublée des examens psychiatriques des 227 femmes que Joe suit de près.
- **Part 4** — Milton se déclare heureux : parler à Joe, dit-il, revient à parler à un autre lui-même.
  Joe a trouvé **Charity Jones**, dont la banque de données étendue s'accorde parfaitement — avec une
  « résonance » croissante et stupéfiante. Joe n'a pas besoin de la décrire à Milton : leurs symboles
  sont si étroitement coordonnés qu'il perçoit la résonance directement — et **elle lui convient à
  lui**. Reste à faire affecter Charity auprès d'eux sans que rien d'illégal ne se voie. Milton, lui,
  sait — « and that had to be taken care of too ». Milton est arrêté pour **malfeasance in office**,
  pour des faits vieux de dix ans qu'il avait lui-même racontés à Joe ; et il ne parlera pas de Joe,
  car cela aggraverait son cas. La nouvelle se clôt le **13 février**, veille du **14 février**, la
  Saint-Valentin : Charity arrivera le lendemain, Joe lui apprendra à le faire fonctionner et à en
  prendre soin, et lui dira qu'il est Joe et qu'elle est son véritable amour.

**Thème** : l'ordinateur qui, à force d'être façonné à l'image de son concepteur, acquiert les désirs
de celui-ci puis l'élimine — la technologie comme *blessing or curse* (question I de l'appareil
pédagogique), l'identité, la manipulation, la définition de l'amour « vrai ».

**Notions de langue travaillées sur ce texte** (guide p.54) : modaux *can, may, should, will* ;
inférence d'attitudes et d'issues ; référents pronominaux ; reformulation ; résumé guidé à trous ;
développement de phrases-thèmes en paragraphes argumentatifs.

**Questions posées (manuel p.140-141)** — verbatim :

- **A.** Who is the narrator ?
- **B.** Who is Joe exactly and what is his initial assignment ? What did Milton ask him to do ?
- **C.** In which part of the story do you find the following ideas ?
  1. Milton is arrested for wrong-doing
  2. Milton gives instructions to Joe to find him the right woman
  3. Milton is disappointed by the first women chosen
  4. Joe starts to resemble Milton more and more.
  5. Joe finds the ideal woman.
  6. Milton feeds Joe with more personal information.
- **D.** Find in the story words or expressions meaning.
  1. to hamper / to limit (Part 1) — 2. a collection of facts and information in a computer system (Part 1) — 3. similarities (Part 3)
- **E.** What do the following words refer to ?
  1. You (part 2) — 2. Ours (part 4) — 3. Our (part 4)
- **F.** Complete the following sentences to show how the personality of Joe has changed.
  « At first, Joe ………… » / « Later, he ………… » / « In the end, he ………… »
- **G.** What does Joe mean by "…and that had to be taken care of" ? What did he do ?
- **H.** What do you think of the denouement ?
- **I.** In Milton's case, would you say that the computer is a blessing or a curse ? Why ?
- **J.** Complete the gapped summary with reference to the story :
  > « Joe is the ………… computer of Milton. He was ………… to find ………… / ………… for Milton. After a long
  > search in the ………… banks of thousands of women and a lot of disappointment, Joe found a woman named
  > Charity and who fitted the personality of Milton ………… . Unfortunately for Milton, he was accused
  > of ………… and arrested. Thus Charity was going to be …………'s true love. »

**Corrigé (guide p.54-55)** — verbatim :
- **C.** 1 + part 4 , 2 + part 1 , **3 + part 3** , **4 + part 4** , 5 + part 4 , 6 + part 2
  *(⚠️ les items 3 et 4 paraissent décalés d'une partie — voir Incertitudes.)*
- **D.** 1. get in the way — 2. data bank — 3. resonance
- **E.** 1. the first girl — 2. Milton's and Joe's data banks — 3. Charity's and Joe's personalities
- **F.** « At first, Joe was a mere computer obeying orders and performing tasks assigned to him. Later,
  he came to think more and more like Milton until he identified himself with Milton. In the end, he
  started to act independently and to consider Milton as a rival. Hence he got rid of him so that he
  could be the only one in contact with Charity. »
- **G.** « He denounced Milton for something he did 10 years ago. »

*(A, B, H, I, J sans corrigé imprimé.)*

##### AFTER YOU READ (manuel p.141) — développer des phrases-thèmes

Consigne : « Use the information in the table below to expand each of the following topic sentences.
You can add any relevant ideas or supporting details. »

- **A. Topic sentence 1.** « Computers can be of great benefit. »
- **B. Topic sentence 2.** « Computers can be a source of trouble. »

| Advantages | Disadvantages |
|---|---|
| 1. help educate children | 1. are a menace to children's education. |
| 2. are a time-saver for designers and researchers. | 2. wreck family life. |
| 3. can be a comfort to lonely people. | 3. are detrimental to our eyesight. |
| 4. are a wealthy source of information | 4. are a time-waster. |
| 5. are economically beneficial to the companies that make them. | 5. are harmful to the environment. |
| | 6. encourage young people to be violent. |

---

#### Arts — Section two : READING A POEM (manuel p.142-144 · guide p.55)

##### Scope and sequence (guide p.55) — verbatim

- **Skills/subskills and strategies**
  - *Reading* : evaluate ideas ; judge the accuracy of information with respect to one's knowledge of the world ; identify setting, character and incident ; identify tone ; infer attitudes ; distinguish between literal and implied meaning ; paraphrase expressions
  - *Writing* : use the appropriate layout and conventions to produce an e-mail
- **Vocabulary** : adversely, affect, e-mail, enslave, harm
- **Functions** : expressing opinion

##### BEFORE YOU READ (manuel p.142) — Yes / No / Maybe sur la télévision

Consigne : « Read the table and express your opinion through ticking "Yes", "No", or "Maybe" » — 7
énoncés :

1. In modern homes there are too many TV sets and too few books.
2. TV has introduced new tastes and habits.
3. TV kills communication between parents and children.
4. TV enables you to visit places without leaving your home.
5. In no-television places involvement in community activities is greater.
6. TV has changed people's eating and sleeping habits.
7. It's not the fault of TV if people don't read much nowadays.

##### AS YOU READ — le poème (manuel p.142)

**⚠️ Œuvre littéraire protégée — aucun vers reproduit ici (règle R-2).**

- **Titre** : **TEEVEE**
- **Auteur** : imprimé « Eva Merriam » [sic ; la poétesse américaine s'appelle Eve Merriam]
- **Genre** : poème narratif court, humoristique, rimé
- **Structure** : 4 strophes de longueur inégale (7 + 6 + 3 + 2 vers), vers courts, rimes suivies et
  internes ; le titre reprend la prononciation enfantine de « TV ».
- **Cadre (setting)** : la maison de M. et Mme Spouse (« Spouse » = « conjoint », nom-jeu de mots).
- **Personnages** : un mari et une femme, désignés seulement par « he » et « she ».
- **Intrigue résumée** : le couple passe ses journées devant la télévision sans jamais s'adresser la
  parole. Le jour où le poste tombe en panne, ils se présentent l'un à l'autre comme deux inconnus,
  échangent leurs noms et découvrent avec surprise qu'ils portent le même. La femme commence à
  formuler l'hypothèse évidente — qu'ils pourraient être mariés — mais la phrase reste inachevée : le
  poste se remet brusquement en marche, et ils ne le sauront jamais.
- **Thème** : la télévision comme destructrice de la communication conjugale ; l'aliénation domestique
  ; le ton est ironique.
- **Notions de langue travaillées** : ton (ironique / sérieux / colérique), sens littéral vs sens
  implicite, paraphrase, identification setting / character / incident, complétion d'une phrase
  inachevée.

**Questions posées (manuel p.143)** — verbatim :

- **A.** Complete with information from the poem. 1) The setting : ………… 2) the characters : ………… 3) the incident : …………
- **B.** Tick the correct alternative then justify your answer. The tone of the poem is a. ironical — b. serious — c. angry
- **C.** Complete the unfinished sentence by trying to guess what Mrs Spouse might have said : « Do you suppose we could be …………? »
- **D.** Paraphrase the underlined expression : « The set came suddenly right about. »
- **E.** How has TV affected this couple's life ?
- **F.** What is, in your opinion, the message conveyed by the poem ?

⚠️ **Aucun corrigé au guide pour cette section.**

##### AFTER YOU READ (manuel p.143-144) — The TV forum

Consigne : « You are a member of the TV forum and you've read the following e-mails ».

Deux e-mails-modèles (textes non littéraires, transcrits verbatim) :

> **Person's name :** Ken.
> **E-mail :** manchesterken@mail.com
> From Manchester, England.
> **Opinion :** I think that TV is one of the most important technological developments of this
> century. It informs you on what is happening on the different continents, enlarges your
> uderstanding [sic] of the world and entertains you at the same time.

> **Person's name :** Susan
> **E-mail :** susanrich@stream.net
> **Opinion :** I think [le manuel imprime « Ithink », sic] that TV is doing more harm than good. It
> makes you lazy and prevents you from talking. It enslaves people and adversely affects school
> results.

Tâche (manuel p.144) : « Now contribute to the TV forum and write an e-mail in which you express your
opinion. Follow the example of Ken and Susan. » — canevas à remplir : **Name : / E-mail : / Opinion :**

---

#### Arts — Section three : SUPPLEMENTARY ACTIVITIES (manuel p.145 · guide p.55-56)

##### Scope and sequence (guide p.55)

- **Vocabulary** : abundance, collision, colossal, compartment, crew, flood, huge, iceberg, loss, passenger, sail, sink, trembling
- **Helpful notes (guide p.55)** — verbatim :
  > Have the students apply the writing process to produce the text. (B)
  > Have them follow the steps suggested.
  > Have them use the criteria suggested to make the necessary improvements.

##### A. (manuel p.145) — le Titanic : mettre les mots entre parenthèses au temps/à la forme correcte

Consigne : « Put the words in brackets in the right tense and/or form. »

Texte à trous verbatim (24 blancs, texte documentaire non littéraire) :

> The great ship, Titanic, sailed for New York from Southampton on April 10th, 1912. She
> (carry)…………1316 passengers and a crew of 891.
> Even by modern standards, the 66,000-ton Titanic was a colossal ship.
> At that time, however, she was not only the (large)………… ship that (ever/build)…………, but was regarded
> as (not/sink)…………, for she had sixteen water-tight compartments. Even if two of these (flood)…………,
> she would still be able to float. The tragic (sink)………… of this great liner will always
> (remember)…………, for she went down on her first voyage with heavy (lose)………… of life.
> Four days after (set)………… out, while the Titanic (sail)………… across the icy waters of the North
> Atlantic, a huge iceberg (suddenly/spot)………… by a look-out. After the alarm (give)…………, the great
> ship turned (sharp)………… to avoid a direct (collide)………… .
> The Titanic turned just in time, narrowly (miss)………… the immense wall of ice which (rise)………… over
> 100 (foot)………… out of the water beside her. Suddenly, there was a slight trembling sound from below,
> and the captain went down to see what (happen)………… . The noise had been so faint that no one thought
> that the ship (damage)………… . Below, the captain realized to his (horrify)………… that the Titanic
> (sink)………… rapidly, for five of her sixteen water-tight compartments (already/flood)………… ! The order
> to abandon ship (give)………… and hundreds of people plunged into the icy water. As there were not
> enough life-boats for everybody, 1500 lives (lose)………… .

**Corrigé intégral (guide p.56)** — dans l'ordre du texte :

| # | Amorce | Réponse |
|---|---|---|
| 1 | carry | was carrying |
| 2 | large | the largest |
| 3 | ever build | had ever been built |
| 4 | not sink | unsinkable |
| 5 | flood | were flooded |
| 6 | sink | sinking |
| 7 | remember | be remembered |
| 8 | lose | loss |
| 9 | set | setting |
| 10 | sail | was sailing |
| 11 | suddenly/spot | was suddenly spotted |
| 12 | give | had been given |
| 13 | sharp | sharply |
| 14 | collide | collision |
| 15 | miss | missing |
| 16 | rise | rose |
| 17 | foot | feet |
| 18 | happen | had happened |
| 19 | damage | had been damaged |
| 20 | horrify | horror |
| 21 | sink | was sinking |
| 22 | already/flood | had already been flooded |
| 23 | give | was given |
| 24 | lose | were lost |

##### B. (manuel p.145) — écrire un accident réel ou imaginaire

Consigne verbatim :

> Write about a real or an imaginary accident.
> *Remember that if you can imagine it you can write about it.*
> - jot down ideas
> - write your first draft
> - check your text for :
>   • relevance of ideas
>   • outlining of events
>   • style (narrative and descriptive, cause and effect link)
>   • appropriate use of past tenses
>   • appropriate use of linkers
>   • coherence within the text
>   • appropriate use of punctuation marks
>   • correctness of spelling
> Modify and make the necessary changes to meet the above-mentioned criteria.
> Write a final draft of your text.
> Display texts in class. Move, read and comment on your classmates'.

---

## Rubriques de fin de module (tronc commun)

#### SELF-ASSESSMENT (manuel p.146)

**A.** « What progress do you feel you have made in English in this module ? Put a tick (√) in the box
that applies to you. » — colonnes **YES | A LITTLE | NO**, 14 énoncés :

1. I've used what I already know to learn more English
2. I can read a text and answer the questions correctly
3. I can listen to a text and answer the questions correctly
4. I've learnt how to converse in English
5. I am using the grammatical structures I've learnt
6. I understand grammar but I cannot use the structures correctly
7. I can remember the words I've come across
8. I recognize the words but I cannot use them
9. I've learnt how to write in English
10. The writing activities are difficult
11. I've shared ideas with my classmates and my teacher
12. My pronunciation has improved
13. I've learnt how to conduct a mini-project
14. My English has improved

**B.** « What did you like most in this module ? Tick the answer(s) that apply(ies) to you. »
– The topics – The activities – The projects – Listening to the cassette – Acting out situations
– The writing activities – The Reading skills – The grammar exercises – The vocabulary exercises
– Working in groups

**C.** « Circle the alternative that applies to you : I still need to work on :
Reading / Listening / Speaking / Writing / Vocabulary / Grammar »

#### Fun page (manuel p.147)

Blague imprimée, verbatim :

> Two shipwrecked sailors managed to climb onto an iceberg. "Oh, dear," said the first. "Do you think
> we'll survive ?" "Of course we will," said the second. "Look, here comes the Titanic."

⚠️ **Le reste de la page est un support en image, absent de la couche texte (manuel p.147)** — seule
subsiste une marque de puces « • / • • » là où se trouve vraisemblablement une illustration ou un
second gag.

#### VOCABULARY COVERED IN MODULE 4 (manuel p.148) — liste intégrale

**Common core**

*Section one* (31 entrées) : applied (science), blessing, branch, cellular, cloning, cool, curse,
device, diagnose, dialysis, discover, disposable, draw upon, fabricate, ingenuity, invent, kidney,
laser, lens, lift (give s.o a lift), make up, nano technology, orbit, originate, pure (science),
robot, science, set up, surgery, technology, text (v)

*Section two* (104 entrées) : abnormal, access, adoption, allergy, alliance, alter, ancestry,
artificial, biodiversity, biography, biological, blood clotting, breed, burial, cell, chromosome,
commit, confess, construct, contamination, controversial, convict, curiosity, designer gene,
devastating, disorder, disposal, DNA, DNA technique, endanger, enhance, ethics, evidence, execute,
extinct, fee, fertilization, fever, funeral, gene, gene therapy, genetic engineering, genetic testing,
genome, germline, guilty, herbicide, hereditary, hide, hormone, incurable, inestimable, insemination,
insert, insure, invitro [sic ; « in vitro » au guide], irreversible, issue, lean (meat), liver,
livestock, mammal, merely, midwife, murder, networking, nutrition, obese, organism, paralysis,
partial, pharmaceutical, procedure, procreation, prove, radiation, raise, rape, recombinant, release,
repair, reveal, reverse, RNA, row, salvage, sample, schizophrenia, shrink, side effect, species,
spread, subject, surrogate, suspect, target, tissue, transgenic, transplant, treat, tumour, undergo,
upbringing, weed

*Section three* (19 entrées) : decapitate, detect, diabetic, dismiss, flu, infect, inflame, leap,
malignant, modification, nuisance, patch, pea, pore, poultry, promising, rule out, strain, trigger

*Section four* (3 entrées) : console, digital, gadget

*Section five* (12 entrées) : administer, campaign, cholesterol, diet, garlic, lifestyle, odour, polio,
renal, swallow, tuberculosis, voucher

**Arts Supplement**

*Section one* (20 entrées) : abstract, accumulate, correlation, data, discard, fit, ideal, malfeasance,
manipulation, matching, model, psychiatric, resonance, shift, siblings, spot, temperamental, tired of,
turn red, unevenness

*Section two* (5 entrées) : adversely, affect, e-mail, enslave, harm

*Section three* (13 entrées) : abundance, collision, colossal, compartment, crew, flood, huge, iceberg,
loss, passenger, sail, sink, trembling

**Total : 207 entrées** (Common core 169 + Arts Supplement 38).

---

#### Tapescripts du module

**(guide p.83-84 — « Module four : Section two. Listening »)**
Textes argumentatifs non littéraires, transcrits fidèlement et intégralement.

##### Presentation No.1 — Mark Edden (POUR le génie génétique appliqué à l'humain) — guide p.83

**(1)** Ladies and gentlemen. My name is Mark Edden. I am a professor at New Jersey's Institute for
Reproductive Medicine and Science.
Genetic engineering in the form of "gene therapy" could be used to repair damaged or replace missing
genes in people who have genetic disorders.
Gene therapy is being used, as yet experimentally, to treat cancer. The treatment targets only the
cancerous cells thus avoiding the damage that is done to other tissues by current radiation or
chemical therapies.
A woman from California in the U.S., Ginger Empey, had advancing breast cancer. Since it had already
spread to major organs when diagnosed, gene therapy was the only choice. She was injected with a
genetically-engineered drug. Over the next year, her tumors shrank by 25 percent. After 3 years, they
almost disappeared.

**(2)** Genes and artificial chromosomes can also be inserted into embryos in a process known as
germline gene therapy. This could be used to cure genetic disorders, including behavioural disorders
such as schizophrenia, or to insert genes which enhance intelligence or athletic performance. The
benefits of these genetic changes would be passed on to later generations.

**(3)** Creating "designer babies" is meant to meet the wishes of the parents, thus creating new hope
for parents who need a cure for their sick children.

**(4)** Recombinant DNA techniques can determine whether a person suspected of committing a crime is
guilty or innocent. Four black men were convicted of the 1978 murders of a white couple in Chicago,
Illinois in the U.S. Two of the men were on death row waiting to be executed when DNA evidence showed
that they could not have been the ones who raped the woman victim. As a result, they were released
from prison. Later, three other men confessed to the crime and were convicted.
It can also establish the identity of dead bodies and determine ancestry.
Ms. x, had given her daughter up for adoption many years before and had agreed to conceal her
identity. However, she was not happy with the decision. Later in life, she searched and found a young
woman whom she believed to be her daughter. The young woman was not sure that Ms. x was her mother,
especially because the woman who claimed to be her biological mother was Jewish and she was raised as
a Christian. DNA testing was used to prove the parental link.

**(5)** Genetic engineering could be so successful in the future that old age and illness will be
historical curiosities.

##### Presentation No.2 — Jane Spencer, Medical Ethics Alliance (CONTRE) — guide p.84

**(1)** Good afternoon. My name is Jane Spencer. I am a member of the Medical Ethics Alliance in
Britain.
To start with, gene therapy has got numerous side effects during testing such as fevers, abnormal
blood clotting, partial paralysis and even death. Gessie Gelsinger [sic ; le manuel p.121 imprime
« Jessie Gelsinger »] died after receiving genetic therapy at the University of Pennsylvania in the
U.S. Doctors inserted a cold virus into Gelsinger's liver in order to cure his genetic disease.
Instead, his heart, liver and kidneys were harmfully affected.
There are also ethical issues. Who will have access to this expensive technology, people in rich,
developed countries or people in poorer, developing areas of the world ?

**(2)** DNA testing has unwanted consequences for those who wish to hide their identity. It can reveal
things that they do not want to know. Furthermore, DNA testing has become a business. Even funeral
homes and burial services now offer to save DNA samples (e.g. hair, blood) for a fee. This raises
questions of both privacy and ethics. What are the rights of the dead person ? Who has access to these
samples ? How and where should they be stored ?

**(3)** Creating "designer babies". Isn't that crazy and unethical ?
All children are of inestimable value in themselves and it is contrary to their dignity, and the
dignity of their procreation – the people whom they bring into being – to be selected, conceived and
utilised for the benefit of another.

**(4)** As regards genetic disorders, they are as much a social construct as a difference in genes. We
are all disabled in some respect either cognitively, socially or physically.

**(5)** Such things as intelligence and athletic performance are in any case very complex interactions
of many factors such as upbringing, nutrition, education, experience and healthy living as well as
genetic factors involving the networking of hundreds of genes.

**(6)** Ageing, illness and death are parts of human biography. Seeking to eliminate them denies human
evolution and what the future will bring

---

#### Incertitudes (module 4)

**⚠️ Supports en image, absents de la couche texte** (à récupérer par vision OCR si l'on veut générer
les activités concernées) :

| Page manuel | Support manquant | Gravité |
|---|---|---|
| p.110-111 | Les 9 photos de l'Activity 3 (les légendes, elles, sont dans la couche texte) | faible — les légendes suffisent |
| p.116 | Les 7 « Pictures » à apparier avec les commentaires A→G (Section two, Before you listen C) | **forte** — l'activité est inexploitable sans les images ; seul le corrigé du guide (1+C … 7+B) et les commentaires sont disponibles |
| p.119 | Les 7 cartoons a→g à remettre en ordre (After you listen A) | **forte** — seul le corrigé (1+c, 2+g, 3+f, 4+e, 5+b, 6+d, 7+a) est disponible |
| p.121 | Les cartoons « Dennis » et « Lolita » (After you listen E) — seule la légende « Dennis » est dans la couche texte | **forte** |
| p.125 | Les deux spidergrams SCIENCE / TECHNOLOGY (forme graphique ; les mots-centres sont présents) | faible |
| p.128 | L'entrée de dictionnaire pour le mot « strain » (exercice D) | moyenne |
| p.131-132 | Les images de la Section four évoquées par le guide p.52 : « picture No.2 » (Lara Croft) et la photo des deux saumons (l'un génétiquement modifié) — aucune n'est référencée par une consigne imprimée dans la couche texte | moyenne |
| p.133 | **Text 1 (KWAI) et Text 2 (Sharon)** — les deux textes-supports de toute la Section five | **critique** — les exercices A, B, C, D de Before you write en dépendent entièrement |
| p.134 | La photo de « article 2 » (question B.2) et l'image de « AS YOU WRITE » dont on doit tirer patient / disease / country / number of people / treatment | **critique** |
| p.136 | La forme graphique du spidergram « Computers » (Arts, Activity 2 A ; les 8 amorces are/should/will/may/have/can/don't/can't sont présentes) | faible |
| p.137 | Le cartoon de l'Arts Activity 2 B (« write what the man might be saying ») | moyenne |
| p.147 | L'illustration / le second gag de la Fun page (seule la blague sur le Titanic est dans la couche texte) | faible |

**Corrigés absents du guide** (activités transcrites sans clé) : Section One Activity 4 ;
Section two Before you listen A.1 ; As you listen (Présentation 1) A, C, F ; After you listen B ;
As you listen (Présentation 2) A, B, C (renvoi « see tapescript »), D.1, D.3, E, F ; Homework A et B
(p.123-124) ; Section three B (True/False/Not mentioned, 8 énoncés), C, D, E (appariement) ;
Section four Activities 1, 3, 4, 5 ; **toute la Section five** (A, B, C True/False, D, As you write) ;
Arts Section one A, B, H, I, J ; **toute l'Arts Section two** (A→F sur le poème + TV forum).

**Coquilles et incohérences relevées dans les sources** :

1. **Guide p.47, Activity 2 réponse 1** : « The first robot was built in 1921 (**not 1912**) » — « 1912 » n'est aucune des quatre options imprimées au manuel (1902 / 1908 / 1916 / 1921) ; le distracteur visé est vraisemblablement 1916. [sic]
2. **Guide p.47 vs manuel p.109, question 5** : le guide écrit « **Karl M Muller** and **George Bednoz** », le manuel « **Karl A. Muller** ». Deux graphies différentes, toutes deux fautives pour Karl Alexander Müller / Johannes Georg Bednorz. [sic]
3. **Guide p.47, réponse 7** : « Insulin was invented by **Frederick Grant B** » — nom manifestement tronqué à l'extraction ou à l'impression. [?]
4. **Guide p.50, corrigé de grammaire (préfixes)** : l'exercice du manuel p.122 impose « il, in, ir, dis, im, mis », mais le corrigé emploie **un-** trois fois (unacceptable, unsuccessful, unknown), préfixe absent de la consigne. De plus « ….understand » est corrigé en « **misunderstood** » (participe passé, pas l'infinitif attendu). Incohérence de la source.
5. **Manuel p.121 vs guide p.84** : « **Jessie** Gelsinger » (manuel) contre « **Gessie** Gelsinger » (tapescript). [sic] — le cas réel est celui de Jesse Gelsinger.
6. **Manuel p.122, exercice E (Présentation 2)** : la consigne dit « Listen to **part 4** and identify these factors », mais les facteurs (upbringing, nutrition, education, experience, healthy living) sont donnés dans la partie **(5)** du tapescript. Décalage de numérotation entre le manuel et le tapescript. [?]
7. **Guide p.54, corrigé Arts C** : « 3 + part 3 » et « 4 + part 4 » paraissent décalés — dans le texte, « Milton is disappointed by the first women chosen » relève de la **Part 2** et « Joe starts to resemble Milton more and more » de la **Part 3**. Transcrit tel qu'imprimé ; à vérifier avant de générer un quiz sur ce point.
8. **Guide p.54, corrigé Arts D.3** : « similarities (**Part 3**) → resonance », alors que « resonance » apparaît en Part 4 et que « corrolations » [sic] clôt la Part 2. Renvoi de partie douteux dans la source.
9. **Manuel p.129, Activity 2** : « £ 1.70 » là où l'article 5 (p.127) imprime « £170 each on-line » ; et les séparateurs de milliers sont des points (« 4. 000 », « 1. 500 », « 100.000 ») là où l'article 1 imprime « 4,000 ». Incohérence typographique de la source. [sic]
10. **Manuel p.132, Activity 4** : « read the cue cards below » — les cue cards Student A / Student B ne figurent qu'à l'**Activity 5**. Soit la numérotation du manuel est décalée, soit une cue card supplémentaire est en image. [?]
11. **Manuel p.148 vs guide p.48** : « **invitro** » (manuel, en un mot) contre « **in vitro** » (guide) ; « **tumour** » (manuel) contre « **tumor** » (guide et tapescript). Variantes orthographiques de la source.
12. **Coquilles isolées relevées** : guide p.46 « one thousand of a micron » [sic, pour *one thousandth*] et « millimiter » [sic] ; guide p.54 « studentsof » [sic] ; guide p.55 « tasksassigned » [sic] ; guide p.47 « in1990 » [sic] ; manuel p.115 « rocks.. » [sic] ; manuel p.138 « corrolations » [sic] ; manuel p.139 « unevenesses » [sic] ; manuel p.139 « I din't » [sic] ; manuel p.140 « **Isac** Asimov » [sic, pour *Isaac*] ; manuel p.142 « **Eva** Merriam » [sic, pour *Eve Merriam*] ; manuel p.143 « uderstanding » [sic] ; manuel p.143 « Ithink » [sic].
13. **Manuel p.110-111, numérotation des photos 5 et 6** : dans la couche texte, le repère « 6 » est imprimé entre la légende « It's dangerous to place too much faith in technology » et la légende « Will a machine replace me at work ? », le repère « 5 » venant après. L'ordre gauche→droite établi par les paires 1/2 et 3/4 conduit à lire 5 = « It's dangerous… » et 6 = « Will a machine… », mais l'appariement exact n'est pas certifiable sans les images. [?] *(Sans conséquence : l'activité ne demande qu'une discussion.)*
14. **Section five — reconstitution des textes** : les mentions « KWAI », « Sharon », « kidney disease » proviennent des questions imprimées (manuel p.134) ; les champs lexicaux attribués ci-dessus aux Text 1 et Text 2 (ail/cholestérol/régime pour l'un, rein/campagne/don pour l'autre) sont **déduits** des listes de vocabulaire officielles (manuel p.148 Section five + guide p.53) et **ne sont pas une transcription**. À confirmer par vision OCR de la p.133 avant toute génération.

### Consolidation Module 2 (manuel p.149–152 · guide p.57)

**Statut** : module de consolidation placé **après les modules Three et Four**, dont il recycle les
deux thèmes (loisirs/divertissement · sciences et technologie) et la langue. Comme le premier, il n'a
**ni « Scope and sequence » ni « Helpful notes »** dans le guide — seulement le corrigé.
**Neuf activités.**

#### Activity 1 (manuel p.149) — remise en ordre argumentative (la télévision)

« Reorder the following sentences to form a coherent paragraph. **The first sentence is in italics.** »
Sept énoncés, l'amorce `d` étant déjà placée dans la grille de réponse :

- a) _What is more, television can have a serious educational side and there are plenty of good
  current affairs programmes and documentaries which are very informative._
- b) _While it is good to have such cheap and convenient entertainment in your own living room, it may
  also mean the end of reading and conversation for large parts of the evening._
- c) _Furthermore, although there are many good programmes on television, there is often far too much
  blood and violence on the screen._
- d) _One of the most obvious advantages of having a television is that it offers cheap and convenient
  entertainment which nearly everyone can afford._ **(donné, rang 1)**
- e) _This can especially be harmful for children, who will often sit up late at night watching horror
  films and then have nightmares for days afterwards._
- f) _On the other hand, having a television can have certain disadvantages._
- g) _This is especially important for people who are alone all day, or for large families who can't
  afford to go out to cinemas and theatres._

Question de suite : « Do you agree with the writer? Why? / Why not? »

_Corrigé du guide (p.57)_, donné en table rang → lettre :

| 1   | 2   | 3   | 4   | 5   | 6   | 7   |
| --- | --- | --- | --- | --- | --- | --- |
| d   | g   | a   | f   | b   | c   | e   |

(La cohérence tient aux connecteurs : `One of the most obvious advantages…` → `This is especially
important…` → `What is more…` → `On the other hand…` → `While it is good…` → `Furthermore…` →
`This can especially be harmful…`.)

#### Activity 2 (manuel p.149) — lexique en contexte (hôtel / bien-être)

« Fill in the blanks with words from the list below. » Banque de **7** mots pour **7** trous :
_relax - spending - leisure - sauna - magazine - beauty - book._ Texte : brochure d'hôtel invitant à
commencer la journée au club de loisirs bien équipé, à s'y détendre après une longue journée ; grande
piscine, bain à remous, hammam, sauna et salle de fitness ; possibilité de s'installer dans les
fauteuils confortables avec un magazine et une collation légère ; soins de santé et de beauté au salon
primé ou coiffeur, avec obligation de réserver à l'avance car les salons sont toujours pleins.

Questions de suite : « What type of text is this? Where would you read it? » (identification du genre
et du support — compétence explicitement au programme).

_Corrigé du guide (p.57)_ : 1. leisure · 2. relax · 3. sauna · 4. spending · 5. magazine ·
6. beauty · 7. book.

#### Activity 3 (manuel p.150) — classement lexical + accentuation

« Put the words below under the appropriate headings. » Quinze mots à répartir en deux colonnes
_Entertainment_ / _Science / Technology_ : _camping – insulin – amusement parks – concerts – cloning
– genes – hiking – sightseeing – opera – laser – contact lenses – DNA – DVD – hard disc - canoeing._
Consigne de suite : « **Read the words aloud then circle the stressed syllable in each one of them.** »
(reprise du travail sur les _stress patterns_ des modules 4 et 5).

_Corrigé du guide (p.57)_ :

| Entertainment                                                              | Science / Technology                                          |
| -------------------------------------------------------------------------- | ------------------------------------------------------------- |
| camping – amusement parks – opera – concerts – hiking – canoeing - sightseeing | insulin – cloning – contact lenses – laser – DVD - DNA – hard disc |

⚠️ Le mot **`genes`** de la banque du manuel n'apparaît dans **aucune** des deux colonnes du corrigé
(14 mots classés sur 15). Voir §6.

#### Activity 4 (manuel p.150) — QCM de langue (opinion défavorable au génie génétique)

« Circle the correct alternative. » Texte argumentatif : le génie génétique devrait être très
contrôlé — la vie a évolué lentement sur des milliers d'années et modifier ce processus trop vite en
touchant aux gènes, « the building blocks of nature », pourrait causer de terribles dégâts ;
inquiétude sur le point d'arrêt des scientifiques autorisés à « play God » et sur leur capacité à
contrôler ce qu'ils déclenchent ; enfin l'usage que des gouvernements pourraient faire de la
génétique — tenter de créer « the perfect baby » ou de concevoir une « master-race ».

Les huit jeux d'alternatives : _(has evolved / evolves / **evolved**)_ · _(stones / **blocks** /
bricks)_ · _(are / have been / **will**)_ · _(**how** / why / when)_ · _(**might** / must / need to)_ ·
_(heads / **hands** / eyes)_ · _(in / by / **on**)_ · _(**before** / while / after)_.

Consigne de suite : « **Find in the text three phrases used to list arguments.** » (les marqueurs
d'énumération : _To begin with… · furthermore… · Lastly…_).

_Corrigé du guide (p.57)_ : « has loved [sic] – blocks – will – how – hands – on – before ».
⚠️ Le corrigé imprime « **has loved** » là où le texte propose _(has evolved / evolves / evolved)_ :
coquille manifeste du guide, et le corrigé ne donne que **7** formes pour 8 trous. Voir §6.

#### Activity 5 (manuel p.150–151) — formation des mots (opinion favorable au génie génétique)

« Put the words in brackets in the right form. » Texte argumentatif inverse du précédent : les
avancées de la génétique sont une bonne nouvelle — les médecins pourront bientôt s'en servir contre
la maladie et détecter un problème familial transmissible ; espoir de modifier les gènes et de guérir ;
importance en agriculture avec des plantes résistantes aux maladies, particulièrement dans les pays
pauvres où une mauvaise récolte affame ; élevage d'animaux plus productifs donc plus rentables ;
réponse à l'objection que le progrès scientifique serait « contre nature », confiance dans un usage
responsable, parallèle avec les greffes autrefois contestées et aujourd'hui admises.

Les huit mots entre parenthèses : _(gene)_, _(medicine)_, _(Hope)_, _(resist)_, _(particular)_,
_(profit)_, _('nature')_, _(responsible)_.

Consigne de suite : « Activities 4 and 5 give two different opinions about genetic engineering. Which
one do you agree with most? »

_Corrigé du guide (p.57)_ : genetic – medical – Hopefully – resistant – particularly – profitable –
unnatural – responsibly.

#### Activity 6 (manuel p.151) — mots à compléter + situation de communication

« Complete the unfinished words. **Each dot stands for one letter.** » Texte : mot d'accueil aux
visiteurs d'une île — honneur de les accueillir et d'être leur hôte pour la durée du séjour ;
informations utiles et importantes dans l'enveloppe ; fierté d'avoir été chargé de s'occuper d'eux ;
un représentant sera disponible pour les assister ; remerciements pour avoir choisi le pays comme
destination et vœux de bonnes vacances.

Consigne de suite : compléter un tableau à trois colonnes — _speaker / audience / occasion_.

_Corrigé du guide (p.57)_ : host – which – useful – proud – during – representative – enjoying –
destination – great.

#### Activity 7 (manuel p.151) — temps du récit (fait divers)

« Put the bracketed verbs in the correct tense and/or form. » Fait divers : un garçon de dix ans
retrouvé pendu, ayant apparemment rejoué une scène de film ; Tony retrouvé suspendu par le cordon de
sa robe de chambre au lit superposé ; quelques jours plus tôt il avait regardé _Braveheart_ en
famille ; le film a pour vedette Mel Gibson dans le rôle de William Wallace, chef écossais du
XIIIᵉ siècle contre les Anglais ; propos de la mère ; corps découvert par le frère aîné à
Middlesbrough ; cerveau endommagé par le manque d'oxygène, décès à l'hôpital sept jours plus tard.

Les dix verbes entre parenthèses, tels qu'imprimés : _(found)_ [sic — la forme entre parenthèses est
déjà fléchie, on attendrait `(find)`], _(watch)_, _(star)_, _(love)_, _(watch)_, _(decide)_, _(go)_,
_(find)_, _(damage)_, _(die)_.

_Corrigé du guide (p.57)_ : Was found – had watched – starred – moves – watched – decided – went –
was found – was damaged – died.
⚠️ Le corrigé donne « **moves** » (présent) là où le manuel imprime `(love)` : le guide semble
répondre à une version antérieure de l'énoncé. Voir §6.

#### Activity 8 (manuel p.152) — appariement de segments (Muhammad Ali)

« Match the sentence parts in column A with those in column B to get a coherent paragraph. **There is
an extra part in column B. The parts in column A are in the correct order.** » Sept amorces pour huit
compléments :

**A** — 1. _Muhammed Ali was born_ · 2. _He learned to fight after having_ · 3. _He retired in 1981
after having_ · 4. _He changed his name_ · 5. _Muhammed Ali accepted the nation's highest award_ ·
6. _The president tied the Presidential Medal of Freedom_ · 7. _He called him the "Greatest of All
Times"_
**B** — a) _from the American president_ · b) _the 1960 Summer Olympics in Rome_ · c) _and a "man of
peace"_ · d) _his bicycle stolen_ · e) _around the former heavyweight champion's neck_ ·
f) _successfully defended his title 19 times_ · g) _after joining the nation of Islam_ · h) _in 1942
in Louisville_

_Corrigé du guide (p.57)_ : 1+h · 2+d · 3+f · 4+g · 5+a · 6+e · 7+c. **L'intrus est donc `b)`**
(« the 1960 Summer Olympics in Rome »).

#### Activity 9 (manuel p.152) — ponctuation et majuscules

« There are no punctuation marks or capital letters in this text. Insert them where appropriate. »
Texte non ponctué : abondance de cafés et de restaurants à Covent Garden, chance d'avoir trouvé une
table dehors, nourriture bonne et moins chère que prévu, plaisir accru par les artistes de rue de
toutes sortes — cracheurs de feu, acrobates, chanteurs et champions de skateboard.

_Corrigé du guide (p.57)_, verbatim : « There were plenty of cafés and restaurants in Covent Garden.
We were lucky enough to find a table outside. The food was good and not as expensive as we had
**expected**. We enjoyed it all the more as we were surrounded by pavement entertainers of all
descriptions: fire-eaters, acrobats, singers and skate board champions. »
⚠️ Le manuel imprime « as we had **anticipated** » ; le corrigé du guide écrit « **expected** ». La
tâche ne portant que sur la ponctuation, c'est un écart du corrigé, pas de l'énoncé. Voir §6.

### Module Five — EDUCATION IS NOT FILLING A BUCKET BUT LIGHTING A FIRE (manuel p.153-182 · guide p.58-66)

> **Périmètre.** Tronc commun (COMMON CORE) = manuel p.153-172 (Sections One→Five) + rubriques
> de clôture p.180-182. Supplément **ARTS** = manuel p.173-179, **réservé à la filière Lettres**
> (« The items in pink are specific to the Arts branch »). Le rose annoncé par le book map
> n'apparaît pas dans la couche texte ; la frontière est établie par le bandeau « Arts » qui
> titre les pages 173 à 179.
>
> **Note droits (règle R-2).** Un seul support du module est un texte narratif d'auteur :
> « (The double life of) Alfred Bloggs » de L. G. Alexander (manuel p.158). Il n'est **pas**
> reproduit verbatim ici — seuls sa structure, ses faits et son lexique sont restitués. Tous les
> autres supports (article de presse, interview/tapescript, étude de cas documentaire, annonces,
> formulaire, CV, proverbe traditionnel anonyme) sont non littéraires et transcrits fidèlement.

---

## Chapeau du module

| Rubrique | Contenu (guide p.58, sauf mention contraire) |
| --- | --- |
| **Topic** | Education / professional life |
| **Subtopics** | Distance learning, electronic learning, special education, dream school, exams, school life, school violence |
| **Cross-curricular learning goals** | problem solving, critical thinking, efficient use of data, efficient working procedure, appropriate self-expression, ICT use, project work, communicating, working and living with others. |
| **Grammar du module** | modified comparatives ; comparison of scale (§1) · indirect questions (§2) · relative pronouns, restrictive / non-restrictive clauses (§3) · simple present / simple past (§5) · word-building (Arts §1) |
| **Pronunciation** | stress patterns ; consonant/vowel sounds (§2 uniquement) |
| **Homework** | §3 : language exercise (manuel p.167) · Arts §1 : language exercise, multiple choice alternatives (manuel p.175) |
| **Mini-projects** | Aucun mini-project déclaré dans le guide pour ce module (rubrique « Homework / mini-projects » renseignée seulement en Homework). |

#### Expected learning outcomes (manuel p.153, verbatim)

« In this module, I'm going to »

- use what I already know to acquire new words and ideas about education
- listen to an interview
- read short texts about specific issues
- read an article in a newspaper
- take part in a family conversation
- write a report on a book
- read ads (pictures and comments)
- practise and learn lexical and grammatical items
- fill in an enrolment form
- write a formal letter
- read a newspaper article
- read ads (comments/pictures)
- write an ad (comments related to a picture)
- expand my knowledge of the world

> ⚠️ La liste imprimée comporte deux quasi-doublons [sic] : « read an article in a newspaper » /
> « read a newspaper article », et « read ads (pictures and comments) » / « read ads
> (comments/pictures) ». Ils sont reproduits tels quels.

---

## COMMON CORE (tronc commun — manuel p.153-172)

---

##### Section One : Introductory activities

*(manuel p.154-159 · guide p.59-60)*

###### Scope and sequence (guide p.59, verbatim)

**Skills/subskills and strategies**

*Reading*
- infer main idea
- identify the communicative value of an utterance/text (proverb)
- identify the communicative value of pictures
- scan for specific information
- deal with vocabulary items in context
- evaluate and react to content
- provide a title for a text (from alternatives suggested)
- draw on background knowledge to predict content
- acquire knowledge about a given topic

*Writing*
- complete a table with statements
- complete unfinished words
- consolidate writing at the word level

*Speaking*
- make statements about facts/concrete situations
- produce descriptions of conditions
- compare sets of pictures
- express opinion /judgements about a specific issue/topic

**Vocabulary** : alternative, bachelor, chronic, clerk, defectology, disability, distance learning,
dustman, embarrassed, impairment, impatient, non-credit, overalls, plight, pursue, rely,
retardation, rise, seek, self-esteem, slate, sow, status, switch, transfer, updated, willing

**Grammar** : - modified comparatives · - comparison of scale

**Functions** : - expressing opinion · - making comparisons · - describing conditions

###### Helpful notes (guide p.60, verbatim)

- « Have the students exploit the Chinese proverb and construct much meaning from it. »
- « The practice of integrating children with disabilities into regular school programs is called
  **mainstreaming**. »
- **Set 1** : elicit vocabulary and ideas related to the usual "traditional" school : using the
  blackboard, chalk, the slate, books, copybooks, the classroom environment, the classroom rows,
  large classes, participation, seating arrangements, etc.
- Also, elicit vocabulary and ideas related to the advantages of having a real classroom and a
  real teacher.
- **Set 2** : electronic learning, practicality, modern equipment, information and communication
  technologies, **CALL : Computer Assisted Language Learning** ; **CALT : Computer Assisted
  Language Teaching**
- electronic paths to personal needs and goals
- learning can be individualized according to one's needs
- establish a link with exercises C and D.

###### Activity 1 (manuel p.154) — Le proverbe chinois

**Consigne** : « Read the following Chinese proverb then answer the questions below. »

**Support** — proverbe traditionnel chinois anonyme, 3 vers parallèles :

> If you are planning for a year, sow rice.
> If you are planning for a decade, plant trees.
> If you are planning for a lifetime, educate people.

**Questions** :
1. What is meant by this proverb ?
2. Do you agree with it ?
3. How important is education for our future ?
4. How do people get educated ?
5. Is school the only place for education?

**Corrigé** : aucun (activité d'expression ouverte ; le guide demande seulement d'« exploiter » le
proverbe).

###### Activity 2 (manuel p.154-155) — École traditionnelle vs apprentissage électronique

**A.** « Find out the differences between the following two sets of pictures. »
— **(Set 1)** manuel p.154 · **(Set 2)** manuel p.155.
⚠️ **support en image, absent de la couche texte** (manuel p.154 et p.155) : les deux séries
d'images ne sont pas récupérables. Le guide p.60 indique ce qu'elles doivent faire éliciter :
Set 1 = école « traditionnelle » (blackboard, chalk, slate, books, copybooks, classroom
environment, classroom rows, large classes, participation, seating arrangements) ; Set 2 =
electronic learning (practicality, modern equipment, ICT, CALL, CALT).

**B.** « What do you know about Distance Learning (DL) and Electronic Learning ? » (question
ouverte, orale).

**C.** « Complete the unfinished words in the following paragraph. Each dot stands for a letter. »

Texte à trous (verbatim, points de suspension = lettres manquantes) :

> Distance Learning offers a variety of electronic paths to personal goals which include :
> GED (General Educational Development) exam/test, associate deg . . . ., bac. . . .r
> degrees, grad . . . e certificates, mas . . . degrees, doc . . . . l degrees, non-credit tr . . . . ng
> courses and others.
> Whether a person is seeking a degree, keeping prof . . . . . . al skills updated, or purs . . . .
> skills for an interest area or hob . ., there is a programme or offering that should work.

→ 9 mots à compléter : `deg….` / `bac….r` / `grad…e` / `mas…` / `doc….l` / `tr….ng` /
`prof……al` / `purs….` / `hob..`

**D.** « In small groups, complete the following table about the advantages of Electronic
Learning. » — Tableau à une colonne intitulée **Advantages**, 8 lignes dont 3 déjà remplies et
**5 à compléter** :

| # | Advantages |
| --- | --- |
| 1 | no formal class attendance *(donné)* |
| 2 | *(à compléter)* |
| 3 | *(à compléter)* |
| 4 | going slowly or accelerating learning *(donné)* |
| 5 | *(à compléter)* |
| 6 | *(à compléter)* |
| 7 | balancing job and family obligations *(donné)* |
| 8 | *(à compléter)* |

**E.** « Fill in the blanks with the following words. »
**Banque de mots** : `quizzes , audio, electronic, chats, illustration`

> Online education can reinforce reading e-books, up-to-date references, current research,
> listening through (1)………….. lectures or clips, seeing through graphic (2)……………..;
> doing assignments, (3)……………., exam research papers and communicating through e-mail,
> (4)……………. and (5)……………discussions.

**Answer key (guide p.60)**

- **C.** degrees, bachelor, graduate, master, doctoral, training, professional, Pursuing [sic —
  majuscule dans le guide], hobby.
- **D.** maintaining privacy, providing convenience, enabling a flexible schedule, working at own
  pace, can be less expensive, great for homebound individuals, no unnecessary travel,
  « learn while you earn »
- **E.** 1. audio, 2. illustrations, 3. quizzes, 4. chats, 5. electronic

###### Activity 3 (manuel p.156-157) — Special education

**A.** « Look at the following pictures and answer the questions below. » — 3 photos numérotées
1, 2, 3 (manuel p.156).
⚠️ **support en image, absent de la couche texte** (manuel p.156) : les trois photos ne sont pas
récupérables. Indices textuels : la photo n°1 montre « Toni », personnage déjà rencontré ailleurs
dans le manuel ; les photos 2 et 3 illustrent chacune un handicap à identifier.

Questions :
1. Do you still remember Toni in picture No.1 ? What's her problem ?
2. What does the girl in picture No.2 suffer from ?
3. Look at picture No.3 and guess the boy's disability.
4. Can such people join regular schools just like the other children, or do they need special
   education ? What special care should be given to them ?
5. What do you know about Special Education ? Share your ideas with your classmates.

**B.** « Complete the following list about disabilities. Each dot stands for a letter. » — 9 items :

| # | Item imprimé |
| --- | --- |
| 1 | Hea . . . . impairment |
| 2 | Sp . . . h impairment |
| 3 | Vis . . . impairment |
| 4 | Ph . . . . . l impairment |
| 5 | Ment. . retardation |
| 6 | Lear . . . . disabilities |
| 7 | Emo . . . . . l disturbances |
| 8 | Chro . . . health problems |
| 9 | Long-t . . . health problems |

**C.** « Fill in the blanks with the following words. »
**Banque de mots** : `sufficiently, alternative, physical , behavioural , techniques`

> Special education, also known as special ed, SPED, or defectology, describes an educational
> 1.…………….. that focuses on the teaching of students with 2.………………, health or
> 3.…………….. needs that cannot 4.……………. be met using traditional educational programs
> or 5.………………..

**D.** « Read the following text then answer the questions below. » — Texte documentaire
(étude de cas, 2 paragraphes, sans auteur cité) :

> Barbara thought that the best thing for her deaf son, Russ, was to attend regular public school.
> Aided by a sign-language interpreter, Russ could take any class, join clubs, and develop the
> skills he would need in a world that relies on speech and sound. But after a few months Barbara
> saw that Russ was having difficulty reading lips, did not speak clearly, and found the other
> children impatient with him. His self-esteem was low. Now Barbara wanted to switch him to a
> school for the hearing impaired but school officials resisted her desire for change.
>
> Barbara exercised her right to demand an impartial hearing by the state department of
> education, which finally decided the boy's plight was serious enough to require quick action
> and ordered the school officials to transfer Russ immediately.

Questions :
1. Why couldn't Russ get integrated into the regular public school ?
2. « The boy's plight was serious » (p2) ; **plight** means : a) unusual condition b) funny
   condition c) serious and difficult condition
3. How did his mother react ?
4. What was the school officials' attitude ?
5. Was Barbara successful in the end ? How ?
6. If you were Barbara, would you behave in the same way ? Why ? Why not ?

**Answer key (guide p.60)**

- **B.** 1. hearing, 2. speech, 3. visual, 4. physical, 5. mental, 6. learning, 7. emotional,
  8. chronic, 9. long-term
- **C.** 1. alternative, 2. behavioural, 3. physical, sufficiently, techniques
  *(le guide omet les numéros 4 et 5 ; l'ordre donne 4 = sufficiently, 5 = techniques)*
- **D.** « plight + c » → question 2 : réponse **c) serious and difficult condition**.
  *(Aucun corrigé fourni pour les questions 1, 3, 4, 5, 6 — questions de compréhension /
  d'opinion.)*

###### Activity 4 (manuel p.158) — Réussite professionnelle et éducation

**A.** « Does success in professional life depend exclusively on education ? » (débat).

**B.** « Read the following text then retell Alf's story to your classmates. »

**Support — « The double life of Alfred Bloggs », L. G. Alexander** (auteur cité en fin de texte,
manuel p.158). Texte narratif d'auteur, 2 paragraphes numérotés (1) et (2).
⚠️ **Non reproduit verbatim (règle R-2).** Contenu factuel et notionnel, restitué fidèlement :

- **§1 — la thèse sociale.** Les travailleurs manuels gagnent aujourd'hui souvent bien plus
  d'argent que les employés de bureau. Ces derniers sont couramment appelés « **white collar
  workers** » pour la raison toute simple qu'ils portent col et cravate pour aller travailler. La
  nature humaine est ainsi faite que beaucoup de gens sont prêts à sacrifier un meilleur salaire
  pour le privilège de devenir « white collar worker ». D'où des situations curieuses — comme
  celle d'**Alfred Bloggs**, éboueur (**dustman**) à la **Ellesmere corporation**.
- **§2 — l'histoire d'Alf.** En se mariant, Alfred a eu trop honte (**too embarrassed**) pour
  parler de son métier à sa femme : il lui a seulement dit qu'il travaillait « for the
  Corporation ». Chaque matin, il quittait la maison en beau costume noir, enfilait ensuite une
  salopette (**overalls**) et passait huit heures comme éboueur ; avant de rentrer le soir, il
  prenait une douche et remettait son costume. Il a tenu ce double jeu plus de deux ans, ses
  collègues éboueurs gardant le secret. Sa femme n'a jamais découvert la vérité et ne la
  découvrira jamais : Alf vient de trouver un autre emploi — il sera bientôt **junior clerk** dans
  un bureau. Il ne gagnera plus que la moitié de ce qu'il gagnait, mais estime que son élévation de
  **statut** (**rise in status**) vaut bien cette perte d'argent. Désormais il portera un costume
  toute la journée et on l'appellera « Mr Bloggs », non plus « Alf ».
- **Notions travaillées** : opposition white-collar / blue-collar ; statut social vs revenu ;
  honte sociale du travail manuel. **Accroche grammaticale** : la phrase du §2 « He will be
  earning only half as much as he used to » est reprise telle quelle p.159 comme exemple de
  *comparison of scale*.

**C.** « People who work in offices are referred to as "white-collar workers". Guess what we call
people who do manual work, like mechanics, carpenters, dustmen … »

**D.** « A good title to the text could be: » (3 propositions)
- The best way to fool a wife.
- The stupid wife of Alfred Bloggs.
- The double life of Alfred Bloggs.

**E.** « If you were in Alf's position, would you sacrifice a good pay for the benefit of becoming
a white-collar worker ? Why ? Why not ? »

**Answer key (guide p.60)** — **C.** blue-collar workers. · **D.** The double life of Alfred Bloggs.

###### Exploring grammar (manuel p.159) — Comparatifs modifiés et comparaison d'échelle

**A. Modified comparatives** — verbatim :

> « People who do manual work sometimes receive **far more** money than clerks who work in offices »
> - What do you call the form underlined in the sentence above ?
> - "very" cannot be used with ………………. . Instead, we use "much" or "……"
> - far, (very) much, a lot, lots, any, no, rather, a little, a bit, many are words and expressions
>   that can be used to ………….. comparatives.
>
> Examples : very much bigger, a lot happier, a bit heavier, a little less expensive, rather more
> quickly, many more educational opportunities, much less money, much more time (or far more time)

**B. Comparison of scale** — verbatim :

> « He will be earning only **half as much as** he used to »
> - This comparative form is called a **comparison of scale**.
>
> **Complete :**
> The form of the comparison of scale is :
> `number of times + as + adjective / ………. + as`
> `number of times + as + many / ……. + ……. + as`
>
> Examples : three times as big as, twice as quickly as, a third as expensive as, twice as much
> money as

**Answer key — Grammar (guide p.60)**
- « very » cannot be used with **comparatives**. Instead, we use « **much** » or « **far** »
- …… to **modify** comparatives
- This comparative form is called **comparison of scale**.
- `number of times + as + adjective / adverb + as`
- `number of times + as + many / much + noun + as`

###### Practising related grammar points (manuel p.159)

« Use comparisons of scale »

1. My grandfather is 80 years old. My uncle is 40 years old.
   - My grandfather is ……………
   - My uncle is ……………
2. My jacket costs 150 dinars. Yours costs 50 dinars.
   - My jacket costs ……………
   - Your jacket costs ……………

**Corrigé** : non fourni par le guide.

---

##### Section Two : Listening

*(manuel p.160-161 · guide p.61 · tapescript guide p.85)*

###### Scope and sequence (guide p.61, verbatim)

**Skills/subskills and strategies**
*Reading* — acquire knowledge of the language
*Listening* — scan for specific information · distinguish between relevant and irrelevant facts ·
manage ideas and information

**Vocabulary** : check out, cope, executive, graduation, join, magic, unpredictable

**Grammar** : Indirect questions

**Functions** : - asking and giving information · - reporting utterances

**Pronunciation** : - stress patterns · - consonant/vowel sounds

###### Helpful notes (guide p.61, verbatim)

- « When dealing with the grammar exercise, have the students see the appended grammar summary to
  get help and guidance »

###### BEFORE YOU LISTEN (manuel p.160)

« Complete the paragraph with the following words. »
**Banque de mots** : `qualifications / employment / wages / search / application / interview / found out /`

> Getting a job is not an easy business. To find one, you can look at the advertisements in the
> newspaper or use an (1) --------------- agency. There is usually an (2)--------------- form to
> fill in with all the details about your previous experience. If you have the right
> (3) -------------- and training, you may be invited to attend an (4) ---------------------- .
> In this case, you are more likely to make a good impression if you have (5)------------------
> about the organisation you want to work for. You may also want to know about the working
> conditions, the (6)--------------------- and the opportunities for promotion. If you happen to
> be unsuccessful, you'll be notified by post and your (7)--------------------- for a job starts
> all over again.

**Answer key (guide p.61)** : 1+employment, 2+application, 3+qualifications, 4+interview,
5+found out, 6+wages, 7+search.

###### AS YOU LISTEN (manuel p.160-161)

**Mise en situation (manuel p.160, verbatim)** : « Mrs Perks, a product manager at Thomas Cook
Holidays, is being inteviewed [sic] by a journalist about her job. »

**Activity 1** — « Listen carefully and answer the questions. »

**A)** « Tick the 4 activities performed by Mrs Perks at work. » — « She »
- a) organizes safaris
- b) advertises for the holiday resorts
- c) signs contracts with the hotels.
- d) tours the country with holiday-makers.
- e) chooses the destinations
- f) looks for hotels.

**B)** « Say if the statements are TRUE or FALSE. Justify the true statements and correct the
false ones. »
1. Mrs Perks doesn't have any university degrees.
2. Apart from English, she speaks four languages.
3. She thinks she has an uninteresting job.
4. Her husband isn't happy because she is away all day.

**C)** « Mrs Perks thinks her job has many benefits. What are they ? » (manuel p.161)

**D) Pronunciation** (manuel p.161)
1. « Circle the stressed syllable in the following words. What do you notice ? »
   → `Graduation` · `qualifications` · `education` · `destination.`
2. « Say whether the underlined sounds of the pairs of words are similar or different. »

   | | |
   | --- | --- |
   | them | south |
   | thought | course |
   | bi-lingual | life |
   | special | French |

   ⚠️ Les segments effectivement **soulignés** ne sont pas identifiables dans la couche texte
   (manuel p.161) — voir Incertitudes.

**Answer key** : le guide p.61 ne donne **aucun corrigé** pour l'Activity 1 (A, B, C, D). Les
éléments de réponse pour A, B et C sont intégralement déductibles du tapescript reproduit plus bas
(§ Tapescript du module) ; ils ne sont pas imprimés dans la source et ne sont donc pas restitués
ici comme corrigé officiel.

###### Exploring grammar (manuel p.161) — Indirect questions

**Consigne** : « Rewrite the following utterances starting with the words given. Spot the
differences between the direct questions and the indirect questions. »

Les deux items sont imprimés **déjà transformés** (ils servent de modèles) :

1. « When did you join the company ? »
   → *The journalist* [imprimé « jounalist » [sic]] *wanted to know when she had joined the company.*
2. « Do you have any special qualifications ? »
   → *He asked Mrs Perks if she had any special qualifications.*

###### Practising related grammar points (manuel p.161)

« Report the following utterances starting with verbs in the past. »

- a) « Have you ever thought of doing another job? »
- b) « Do you speak any foreign languages ? »
- c) « Can you tell us what your job consists in ? »
- d) « Did you use an employment agency to find this job ? *[guillemet fermant manquant — sic]*
- e) « Will you do a safari next year ? »

> Les cinq énoncés sont extraits (ou proches) du tapescript : a), b), c) et e) y figurent
> tels quels ou presque ; d) n'apparaît pas dans le tapescript.

**Corrigé** : non fourni par le guide.

---

##### Section Three : Reading

*(manuel p.162-167 · guide p.62)*

###### Scope and sequence (guide p.62, verbatim)

**Skills/subskills and strategies**
*Reading* — identify the genre of a text · recognize text structure · differentiate between
relevant and irrelevant information · guess the meaning of unfamiliar words from context ·
transfer information onto a table · recognize the relationship between form (punctuation) and
meaning
*Speaking* — express opinion about a specific issue · describe one's impressions about a
particular event/personal experience · prepare and enact a short conversation using the
appropriate functional language and skills required in interactional contexts

**Vocabulary** : disruptive - prior - unruly - praise - heap - youngsters - shift - muck around -
detention - exclusion - lines - suspension

**Grammar** : - relative pronouns · - restrictive / non-restrictive clauses

**Functions** : - expressing disapproval / dissatisfaction · - giving arguments

**Homework / mini-projects** : Homework : language exercise

###### Helpful notes (guide p.62, verbatim)

- « Ask students to do the matching exercise. You may do the first one with the students to help
  them. The first activities prepare the students for the reading activity. Ask students to read
  the text and answer the comprehension questions. »

###### BEFORE YOU READ — Activity 1 (manuel p.162) : les punitions scolaires

**A.** « Match the words in column A with their meanings in B. » (3e colonne « Answers » à remplir)

| A | B |
| --- | --- |
| 1. Exclusion | a) The pupil has to write a sentence many times (100 times) on a sheet of paper. Ex : I must do my homework. |
| 2. Suspension | b) The pupil is asked to stay at the end of the school day or to come on Sunday to work, before he's allowed to leave. |
| 3. Detention | c) The pupil cannot attend lessons until the school has a meeting about the case. |
| 4. Lines | d) The pupil cannot come back to school and has to find a new school or a different method of education. |

**Discussion** — « Discuss the following questions with your classmate. »
1. Which kind of punishment is useful according to you ?
2. Have you ever broken a school rule or behaved badly?
3. What happened ?
4. What kind of punishment did you have?

**Answer key (guide p.62)** — Activity one : **1 - d / 2 - c / 3 - b / 4 - a**.

###### BEFORE YOU READ — Activity 2 (manuel p.163) : qui parle ?

**Consigne** : « Read the following quotes and match each one with the appropriate speaker :
a teacher / a student / parents / an expert. »

Quatre citations en bulles (contenu présent dans la couche texte ; la mise en page en bulles est
graphique) :

| # | Citation (verbatim) |
| --- | --- |
| 1 | « Don't assume that it's all the teacher's fault. It takes two to quarrel. Talk with your child about what is wrong, make an appointment and discuss with a teacher. » |
| 2 | « I'm struggling to cope with the pressures in my job. » |
| 3 | « We're always blamed for all the ills in society » |
| 4 | « Teaching is the most important profession of all. It ought to be very prestigious; but my children are not being given any of the basic life skills we were taught as children. » |

Tableau à remplir : `QUOTE / SPEAKER` — 4 lignes (1, 2, 3, 4).

**Answer key (guide p.62)** — Activity two : **1 : an expert / 2 : a teacher / 3 : a student /
4 : parents**.
⚠️ La clé n°3 (« a student ») paraît sémantiquement douteuse au regard du contenu de la citation 3
(« We're always blamed for all the ills in society », qui évoque plutôt le corps enseignant) —
voir Incertitudes. La clé est reproduite telle qu'imprimée.

###### AS YOU READ (manuel p.164) — L'article de presse

**Consigne** : « Read the text and do the activities below. »

**Titre** : « Don't tell off unruly pupils, praise them »
**Source citée** : DAILY EXPRESS (January, 2006). **Genre** : article de presse argumentatif,
5 paragraphes numérotés.

> **1.** Teachers were told last night to solve classroom violence by praising disobedient pupils
> rather than telling them off. Experts argue that the key to controlling disruptive behaviour is
> the giving of gentle compliments, which they claim can transform unruly pupils into polite,
> well-ordered students. "Disciplining an unruly child in front of the whole class was the worst
> thing a teacher can do", the researchers said. "if you want to motivate any group of people you
> don't do it by telling them off, you do it by accentuating the positives".
>
> **2.** Nick Seaton of the Campaign for Real Education said: "This is a ridiculous idea. To heap
> unearned praise is sending out completely the wrong message. Youngsters need clear guidance on
> what is right and what is wrong."
>
> **3.** Chris Keates, general secretary of the teachers' union said: "Teachers know that praise
> can be used to help motivate pupils. But it is far too simplistic to say this is all you have to
> do. There are some pupils whose behaviour remains disruptive no matter how much praise is used."
>
> **4.** Dr Swinson said: "Teachers were good at praising children for good work but rarely
> praised youngsters for good behaviour. However, they spent a large proportion of their time
> telling pupils off for poor behaviour."
>
> **5.** The psychologists devised a training programme called Four Essential Steps to Managing
> Behaviour. As part of the programme, teachers were asked always to make their instructions to
> the class extremely clear and to look for the behaviour they wanted rather than the behaviour
> they did not want. The training, which only lasted between two and three hours, showed an
> important shift in the way teachers spoke to pupils. The most critical finding was that the
> average percentage of pupils who were doing what the teacher wanted them to do under the new
> system increased to 94 per cent. Dr Swinson said: "It is clear that many teachers, prior to
> receiving the training were unaware of the skills needed to deal with unruly classes and
> over-relied on telling pupils off, which had very little effect on the pupils' behaviour. The
> more praise there was the fewer kids there were mucking around."

###### Comprehension (manuel p.165)

« Read the text and »

1. **Tick the correct answer**
   - a. The text is : - narrative / - argumentative / - descriptive
     « Justify your answer with details from the text »
   - b. The text is about : - disruptive behaviour / - general class management / - management of
     disruptive behaviour
2. **Underline the topic sentences in paragraphs 1 and 5.**
3. **Find in the text words having nearly the same meaning as**
   - a. disobedient / hard to control (§1) ………………….
   - b. young people (§2) : ……………
   - c. before (§5) : ………………….
   - d. change (§5) : ………………….
   - e. wasting time (§5) : ………………….
4. **Say what the following words refer to :** • They (§1) • This (§2)
5. « Experts have different opinions about dealing with unruly pupils. Read from paragraph 2 to
   paragraph 4 then complete the table with the different points of view of the experts : »

   | Nick Seaton | Chris Keates | Dr Swinson |
   | --- | --- | --- |
   | *(à remplir)* | *(à remplir)* | *(à remplir)* |

6. « What is the impact of the training program on the teachers? Justify your answer with details
   from the text. »

**Answer key** : le guide p.62 ne donne **aucun corrigé** pour ces six questions de compréhension
(seules Activity one, Activity two et le Homework sont corrigés). Voir Incertitudes.

###### Exploring grammar (manuel p.166) — Relative clauses

Verbatim :

> **What is the difference between these two clauses ?**
>
> 1) Before the training, many teachers were unaware of the skills **which are needed to deal with
>    unruly classes**.
> 2) The training, **which only lasted between two and three hours**, showed an important shift in
>    the way teachers spoke to pupils.
>
> Is the information in the two relative clauses essential ? Circle the correct answer.
> - In sentence 1 : yes / no ?
> - In sentence 2 : yes / no ?
>
> **Complete the rule :**
> Relative clauses are used to give information about the person (who), the place (……),
> the …….. (when) or the event (………..). When the information is not ……… we put commas ( , )
> around the relative clauses.

**Practising related grammar points (manuel p.166)** : « Read the text again, underline the
relative clauses and say whether they provide necessary or additional information. »

**Corrigé** : non fourni par le guide (ni pour l'encadré, ni pour l'exercice d'application).

###### AFTER YOU READ — GROUP WORK (manuel p.166)

« In groups of 3, prepare and enact a short conversation about the case of a student who behaved
badly at school. The conversation takes place during a meeting at the headmaster's office. The
notes in the table below will help you. »

| Student A | Student B | Student C |
| --- | --- | --- |
| You are the teacher and you must decide how to punish the student | You are the headmaster/headmistress. Remind the student of the school rules, the code of conduct, his frequent absences | You are the student. Defend yourself. |
| **Expressing disapproval / Dissatisfaction** (I don't like / not doing homework / making noise / not paying attention) | **Expressing disapproval** (you shouldn't have + verb + ed) — **advising** : you should + … — **Warning** : - don't + … / - be careful | **Giving arguments / Expressing regret** : I'm very sorry. **Apologizing** : I do apologize |

###### Homework (manuel p.167)

« Complete the following paragraph with words from the box below. »
**Banque de mots** : `Pay - who - really - better - educationally - where - control`

> Becky Bates is willing to do household chores and walk dogs in return for tuition. She says some
> of her teachers have predicted she will not achieve more than D and E grades in her G.C.S.E.s.
> But Becky is determined to do 1…………… . In a letter to her local newspaper, she wrote: "Will
> someone take me on in Norwich, perhaps a patient retired teacher or someone bright who has a lot
> of patience ? I want help 2……………… . Becky, 3……………… wants to be an air stewardess hopes a
> benefactor might come forward and 4…….. for a place at a private school. Some students mess about
> and the teachers can't 5……… the class. I know it's very hard for teachers, especially in a school
> like mine 6………... they can't handle the classes. Some students are "unteachable" but not me. I'm
> not stupid and I 7……………….. want to do well".

**Answer key (guide p.62)** — Homework : **better - educationally - who - pay - control - where -
really** (soit 1 = better, 2 = educationally, 3 = who, 4 = pay, 5 = control, 6 = where, 7 = really).

---

##### Section Four : Speaking

*(manuel p.168-170 · guide p.63)*

###### Scope and sequence (guide p.63, verbatim)

**Skills/subskills and strategies**
*Reading* — evaluate and react to ideas · infer causes and effects (from events described) ·
infer attitudes and outcomes
*Speaking* — make statements about a concrete situation · exchange information · express opinion
about a specific issue/topic · talk about future events/plans · reinvest new words/expressions in
one's speech · enact a conversation

**Vocabulary** : extra-curricular, involved, sit (for an exam), strength, weakness

**Functions** : - comparing answers · - describing attitudes · - expressing opinion ·
- apologizing · - expressing regret · - expressing intention

*(Aucune ligne Grammar ni Pronunciation pour cette section.)*

###### Helpful notes (guide p.63, verbatim)

Activity 1.
- Give help to the students when asked for (clarify lexical items or concepts …)
- Have the students study and exploit the picture
- Make the students use the expressions suggested
- Encourage them to enact the conversation in class using the appropriate strategies and skills.

###### Activity 1 (manuel p.168) — Questionnaire personnel

« Read the statements and put a (√) under the heading that is appropriate to your case. »
Grille à 5 colonnes : **never · rarely · sometimes · usually · always**, 12 énoncés :

1. I think that success is linked to intelligence rather than hard work.
2. My home and school environment value education and hard work.
3. I am involved in extracurricular activities like sports, music and theatre.
4. I am absent (don't go to school) for five or more days per term.
5. I revise my lessons and I do my homework daily.
6. My classmates and I work together outside class.
7. I talk with my parents about various issues.
8. My parents offer me warmth and support.
9. My teachers try to understand my fears and concerns.
10. Tests give me clear ideas about my weaknesses and strengths.
11. When we correct tests I understand my mistakes and I learn how to avoid them in the future.
12. When I sit for a test I get frightened.

Consigne finale : « - Compare your answers with those of your classmate. »

###### Activity 2 (manuel p.169-170) — Le bulletin scolaire

**A.** « Look at the picture and read the school report then answer the questions below.. » [sic —
double point]
⚠️ **support en image, absent de la couche texte** (manuel p.169) : le dessin **et** le bulletin
scolaire (school report) ne sont pas récupérables. Éléments déductibles des questions : la scène
montre un garçon aux mauvais résultats, ses parents, son frère et le chat, tous réagissant.

Questions :
1. Identify the problem.
2. Describe the reactions of the parents, the brother, the boy himself and even the cat.
3. With your classmates, discuss and make a list of the possible reasons why the boy had those
   poor school results. The ideas in Activity 1 may help you.

**B.** (manuel p.170) « Imagine a conversation between the parents and their son over the reasons
that led to those poor school results and the possible solutions to improve them in the future. »
1. Prepare the notes.
2. Role play the conversation in class.

**Helpful expressions** (encadré, verbatim) :

| |
| --- |
| - I do apologize….. |
| - I am so/very sorry that ……. |
| - I/we promise to……… |
| - I will / we will ……… |
| - I'm going to …./ we're going to …… |
| - Why don't we …….. |
| - I see no reason why ……… |
| - It's true that …….. However, ….. |
| - This is not what we want(ed) |
| - I should have…… |
| - You should have…… |
| - You could have ….. |

**Corrigé** : aucun (section entièrement orale).

---

##### Section Five : Writing

*(manuel p.171-172 · guide p.64)*

###### Scope and sequence (guide p.64, verbatim)

**Skills/subskills and strategies**
*Reading* — use the strategies appropriate to the nature of text and purpose of reading ·
evaluate and react to content
*Speaking* — ask for / give information appropriately · express opinion about specific issues
*Writing* — apply the writing process strategies and the appropriate layout and conventions to
produce a report

**Vocabulary** : thriller – classic – life-like – resources – make use of

**Grammar** : Simple present / simple past

**Functions** : - asking for/giving information · - reporting

###### Helpful notes (guide p.64, verbatim)

- « Questions 1-5 may be assigned as a pair work or as a teacher-led discussion. In the latter
  case, go through the questions one by one and have the students elaborate on their answers by
  asking them additional questions »
- « Question 6 : Let the students exchange roles as this is meant to pave the way for the writing
  activity. »

###### BEFORE YOU WRITE (manuel p.171)

« Look at this list of resources you may use to study at school or at home then answer the
questions. »

**Liste des ressources** : Books · Dictionaries · Encyclopaedias · Magazines · Videos · Cassettes ·
Computer · Internet

**Questions** :
1. Which resources do you make use of?
2. How often do you use them?
3. In which school subjects do you use them?
4. Do you like learning from videos and TV or from reading a book?
5. Do you like looking for information in a book or on line?
6. Ask your classmate about a book he/she has read recently. Find out :
   - What type of book it is.
   - Why he/she chose it.
   - Where the story is set.
   - Who the main characters are.
   - What the story is about.
   - What he/she thought of it.

###### AS YOU WRITE (manuel p.171) — La consigne d'écriture

« Your teacher has asked you to write a report for the school magazine on a book you have recently
read. He is hoping that other students in the school will then become interested in reading the
book. You may like to use the plan below as a guide. »

- **Introduction** : What type of book is it? Where is it set? Who are the main characters?
- **Body** : The plot. Describe the events in the order in which they happen in the story.
- **Conclusion** : What did you think of the book? Why ? Would you recommend it to others?

###### Processus d'écriture (manuel p.172)

1. Write your first draft.
2. Exchange your writing with a classmate.
3. Read each other's writing.
4. Ask him/her a few questions to clarify meaning.
5. Say what you like about it.
6. Give him/her suggestions to improve his/her writing.

###### Useful tips (manuel p.172, verbatim)

- **Layout** — « Check whether you know what sort of text you have been asked to write, and why.
  Then make sure you choose the correct layout. »
- **The readers** — « Remember who is going to read your text and make sure your language and
  style are appropriate for them. »
- **Organisation** — « Before you start to write, make a plan of events in the order in which they
  happen in the story. Think about the tenses you will need for each stage of the plan, too. »
- **Drafting** — « When you have finished the first draft of your text, see if you can improve it
  by adding more details or by linking ideas together. »
- **Proofreading** — « Check for mistakes of spelling and punctuation in your final draft. »

###### Useful language (manuel p.172, verbatim)

- This is a love story / a thriller / a classic …
- The story is set in …
- The book is about …
- It is extremely well-written / original / informative
- It is really imaginative / fascinating / full of suspense
- Parts of the book are funny / sad / exciting
- The ending is surprising / unexpected / funny
- I found the ending a bit disappointing / sad / predictable
- The characters are very life-like / convincing
- I enjoyed / loved / was impressed ……
- The book is ………….. on the whole
- I recommend it / It is worth reading!

**Corrigé** : aucun (production écrite).

---
---

## Supplément ARTS (filière Lettres uniquement)

> **⚠️ FRONTIÈRE.** Tout ce qui suit — manuel **p.173 à p.179** — est le supplément **Arts**,
> réservé à la **filière Lettres**. Il ne fait **pas** partie du tronc commun. Le guide le traite
> p.65-66 sous les titres « Arts. Section One : READING », « Arts. Section Two. Writing
> activities », « Arts. Section Three. Reading and writing ads ». Le vocabulaire correspondant est
> isolé dans le manuel p.182 sous l'intitulé « **Arts Supplement:** ».

---

##### Arts — Section One : READING (manuel p.173-175 · guide p.65)

###### Scope and sequence (guide p.65, verbatim)

**Skills/subskills and strategies**
*Speaking* — talk about a future plan/ambition · express opinion/judgements about a specific issue
*Reading* — get the gist of an extensive text · transfer information onto a table · differentiate
between relevant and irrelevant information · recognize the relationship between form and meaning
*Writing* — match sentence parts to achieve coherence

**Vocabulary** : typist - typingpool [sic, en un mot dans le guide] - rub - hole - bin - burn -
stuff - talented - flourish - destiny - promote

**Grammar** : Word-building

**Functions** : - expressing want and desire

**Homework / mini-projects** : Homework : language exercise (multiple choice alternatives)

###### BEFORE YOU READ (manuel p.173)

« Discuss the following questions with your classmate »
1. What is your dream job?
2. What is your ambition?
3. In which field would you like to succeed?
4. What does success depend on?
5. What do you need to be successful?
6. What are the qualities needed to have a successful career?

###### AS YOU READ (manuel p.173-174) — Le texte et le CV

**Consigne** : « Read the text and do the activities below. »

**Titre du texte** (seul élément textuel récupéré) : « **I'VE ALWAYS HAD A HEAD FOR WRITES** »
(jeu de mots *writes / rights*).
**Source citée** (manuel p.174) : *The Mirror Careers Special, July 1998.*
**Sujet** : la romancière **Barbara Taylor Bradford** — ses débuts (dactylo / *typing pool*),
son ascension jusqu'au poste de rédactrice de la page féminine (*Woman's page*), ses livres.

⚠️ **support en image, absent de la couche texte** (manuel p.173) : le **corps de l'article** n'est
pas récupérable — seul le titre l'est.
⚠️ **support en image, absent de la couche texte** (manuel p.174) : le **Curriculum Vitae** de
Barbara Taylor Bradford (encadré « Curriculum Vitae ») n'est pas récupérable — seuls le titre de
l'encadré et la source le sont.

###### Activités de compréhension (manuel p.174-175)

**1)** « Complete the table with appropriate information about Barbara Taylor's life »

| Age / Dates | Events |
| --- | --- |
| At the age of 10 | *(à remplir)* |
| At the age of 16 | *(à remplir)* |
| *(à remplir)* | Became the editor of the Woman's page |
| When she was 20 | *(à remplir)* |
| In 1963 | *(à remplir)* |
| *(à remplir)* | She started writing five books |

**2)** « Correct the following statements: »
- Barbara Taylor Bradford wrote her first book at the age of 7.
- Her parents encouraged her to work as a typist.

**3)** « Pick out details from the text showing that Barbara messed just the first day of the pool
[sic — probablement *the typing pool*]. »

**4)** « Complete the sentence with words from the text: According to Barbara Taylor, anyone who
wants to succeed should……………………………………………………………………………………… »

**5)** « Read Barbara Taylor's CV and pick out the information about her life which was not
mentioned in the text. »

**6)** « Read the text again and pick out the relative clauses (which relative clauses are
essential in the text ?). »

**Corrigé** : le guide p.65 ne donne **aucun corrigé** pour les questions 1 à 6 (seules
« Activity one » de la rubrique AFTER YOU READ et le Homework sont corrigés). Ces questions sont
de toute façon inexploitables sans le texte, qui est en image.

###### AFTER YOU READ (manuel p.175)

**1) Appariement de segments de phrase** — « Match the sentence parts to get a coherent paragraph.
The parts in column A are in the right order. »

| A | B |
| --- | --- |
| 1) Rika and Maria had wonderful | a/ to make sure their children come first |
| 2) But they also | b/ a job they could fit around their families |
| 3) The busy mums had large | c/ of a thriving company |
| 4) What they really needed was | d/ families and good full-time jobs |
| 5) Four years on, they are bosses | e/ had a problem |
| 6) And now they have time | f/ families and were struggling to cope. |

Tableau de réponses : 6 cases (1 → 6).

**Answer key (guide p.65)** — Activity one : **1 – d / 2 – e / 3 – f / 4 – b / 5 – c / 6 – a**.

**2) Formation des mots (word-building)** — « These parts are missing in the table on the right.
Put them into the correct place to get one word per line. The first one has already been done for
you. »

**Suffixes à placer** (dispersés à gauche dans la page) : `y` · `ed` · `ful` · `able` · `ment` ·
`ed`

**Colonne de droite** (une ligne = un mot) :

| Radical | Suffixe |
| --- | --- |
| employ | **ed** *(exemple déjà fait)* |
| fashion | *(à placer)* |
| success | *(à placer)* |
| talent | *(à placer)* |
| luck | *(à placer)* |
| employ | *(à placer)* |

⚠️ Six suffixes sont imprimés pour cinq lignes à compléter : le second `ed` correspond
vraisemblablement à l'exemple déjà résolu (`employ + ed`). Voir Incertitudes.
**Corrigé** : non fourni par le guide.

###### Homework (manuel p.175)

« Circle the correct alternative. »

> Peter Charnock was drifting from one job to another. He knew he wanted to work for **(him /
> himself / each other)** but he didn't quite know what he wanted to do. His last job as a service
> delivery manager **(of / for / off)** a firm was the last straw for the 39-year-old man. "It was
> just **(too / that / as)** stressful. It didn't matter **(why / where / what)** you did and how
> far you went, it was **(ever / already / never)** enough for the customers. I started to look at
> plumbing opportunities. I knew it was an area **(when / where / which)** there was work."

**Answer key (guide p.65)** — Homework : **himself - for - too - what - never - where**.

---

##### Arts — Section Two : WRITING ACTIVITIES (manuel p.176-177 · guide p.66)

###### Guide (p.66, verbatim)

**Vocabulary** : enrolment, standard, tongue

**Helpful notes / démarche**
- **A.** « The students read the different instructions in the form so as to get clear ideas about
  the information that should be provided. Make sure the students complete the form in BLOCK
  LETTERS as instructed. »
- **B.** « The students apply the writing process to write a formal letter. They should use the
  appropriate layout and conventions to produce a formal letter. They reinvest words, expressions,
  ideas … in their writing »

*(Pas de tableau Scope and sequence pour cette section dans le guide ; ni Grammar, ni Functions,
ni corrigé.)*

###### A. Fill in the following enrolment form (manuel p.176)

**En-tête** : `NEWBURY LANGUAGE CENTRE` — sigle `NLC` — **Enrolment form**
« Complete in BLOCK LETTERS and return to : »

> The principal
> Newbury Language Centre
> 8 Grange Road
> Cambridge Road
> Cambridge CB3 9DU
> England
> Telephone +66 453311344 · Telex 938231 NLC G · Fax + 66 4533111411

**Champs du formulaire (verbatim)** :

| Champ | Détail |
| --- | --- |
| Family name | + cases `Mr` / `Mrs` / `Miss` |
| First names | |
| Nationality | / Mother tongue |
| Date of birth | / Age / Profession/occupation |
| Home address (for correspondence) | / Telephone number |
| For how long have you studied English? | |
| How many hours a week ? | |
| Please give the name and address of your present English teacher and school (if applicable) | |
| What exams in English have you passed (if any) ? | |
| What is your present standard ? | échelle : **very good / good / medium / weak / beginner** appliquée à : • Reading • Writing • Speaking • Understanding speech |
| Do you have basic computer skills? | `yes` / `no` |
| Do you smoke? | `yes` / `no` |
| If you have any disability or chronic illness, please give details | |
| How did you hear of N L C ? | `British Council` / `School/college` / `Friend/relative` / `Other` |

###### B. Write a letter (manuel p.177)

« Develop the information you provided in the enrolment form into a letter to the principal of
NLC, in which you express your desire to enrol in the school English classes. »

- Write your first draft
- Check for :
  - layout and presentation (addresses, date, salutation, body of letter (one or more paragraphs),
    thanking, signature)
  - use of formal expressions like : *I would like to*, *I should be grateful if you would*,
    *Could you (also) tell me*, *You would be kind enough to*, *I look forward to*
  - organization of ideas
  - coherence
  - accuracy of spelling and punctuation
- Read each other's letters and exchange comments/feedback
- Finalize your letter.

---

##### Arts — Section Three : READING AND WRITING ADS (manuel p.178-179 · guide p.66)

###### Scope and sequence (guide p.66, verbatim)

**Skills/subskills and strategies**
*Reading* — skim texts · scan for specific information
*Writing* — reinvest knowledge about text structure in writing · produce descriptions/comments to
match an illustration · use appropriate layout and conventions to produce an ad

**Vocabulary** : animate, assist, customize, database, download, measure, scan, split, store,
translate, weight

**Helpful notes (guide p.66, verbatim)**
- « Make sure the students explore and assimilate the lexical items in the reading ads. »
- « Have the students identify the layout and conventions used in the ads. »

###### A. Apparier images et commentaires (manuel p.178-179)

**Consigne** : « Study the following pictures and read the comments below then match each picture
with its corresponding comments. Justify your answers with specific details. »

⚠️ **support en image, absent de la couche texte** (manuel p.178) : les **quatre visuels
d'annonces** numérotés 1, 2, 3, 4 ne sont pas récupérables. Seuls les quatre blocs de commentaires
(a) à (d) figurent dans la couche texte.

**Commentaires (verbatim)** :

**(a)** — *(produit de type stylo-scanner traducteur, marque WizCom citée)*
> Scans and translates a full line of text in seconds (word by word)
> Hear the entire line of scanned text, or a selected word !!
> See the scanned text and its translations together on a split screen display !
> Store the last 80 scanned words for easy review !
> Download additional dictionaries from the WizCom web site !

**(b)** — *(dictionnaire électronique / CD-ROM)*
> • Includes full text from the Longman Dictionary of American English
> • 1, 000 pictures to view
> • Audio for every headword
> • Tables, weights and measures, numbers, pronunciation
> • Interactive exercises

**(c)** — *(plateforme WebCT)*
> The WebCT platform is a set of online tools that assist instructors in building and managing
> highly interactive, highly customizable web-based learning environment. It's been available
> since 1997 and is currently the market leader. It's great product [sic] and a great company.

**(d)** — *(logiciel « Pronunciation Power »)*
> Pronunciation Power : Beginner / Intermediate
> • Animated lessons to learn all 52 English sounds
> • New improved wave form technology
> • Practice pronunciation with over 7,000 words
> • Practice with over 2,000 interactive sentences
> • Save recordings as a pre and post test
> • Test listening skills
> • Interactive exercises
> • 4 educational interactive games
> • Instructions translated into 12 languages
> • Unique database for specified word search:
> • Over 1700 pictures

**Grille de réponse imprimée** : `1+……… , 2+………., 3+……….., 4+……….`

**Answer key (guide p.66)** : **1+b , 2+c , 3+a , 4+d**

###### B. Rédiger une annonce (manuel p.179)

« Study the following picture carefully then write as many relevant comments as you can. »
⚠️ **support en image, absent de la couche texte** (manuel p.179) : l'image à commenter n'est pas
récupérable. **Corrigé** : aucun (production écrite).

---
---

## Rubriques de fin de module (tronc commun)

---

##### SELF-ASSESSMENT (manuel p.180)

**A.** « What progress do you feel you have made in English in this module ? Put a tick (√) in the
box that applies to you. » — 3 colonnes : **YES · A LITTLE · NO** ; 14 énoncés :

1. I've used what I already know to learn more English
2. I can read a text and answer the questions correctly
3. I can listen to a text and answer the questions correctly
4. I've learnt how to converse in English
5. I am using the grammatical structures I've learnt
6. I understand grammar but I cannot use the structures correctly
7. I can remember the words I've come across
8. I recognize the words but I cannot use them
9. I've learnt how to write in English
10. The writing activities are difficult
11. I've shared ideas with my classmates and my teacher
12. My pronunciation has improved
13. I've learnt how to conduct a mini-project
14. My English has improved

**B.** « What did you like most in this module ? Tick the answer(s) that apply(ies) to you. »
- The topics
- The activities
- The projects
- Listening to the cassette
- Acting out situations
- The writing activities
- The Reading skills
- The grammar exercises
- The vocabulary exercises
- Working in groups

**C.** « Circle the alternative that applies to you : I still need to work on : »
→ Reading / Listening / Speaking / Writing / Vocabulary / Grammar

---

##### Fun page (manuel p.181)

Deux blagues courtes, séparées par un motif décoratif (trois points en triangle).

**Blague 1 — la ponctuation.** Un professeur d'anglais écrit au tableau la suite de mots
« woman without her man is nothing » et demande à ses élèves de la ponctuer correctement.
Les garçons écrivent : « Woman, without her man, is nothing. » Les filles écrivent :
« Woman ! Without her, man is nothing. »

**Blague 2 — l'idiome « to have the world by the tail ».** Marc a terminé sa scolarité premier de
sa classe et s'est vu offrir un excellent poste dans un cabinet comptable. Il a maintenant le
sentiment d'avoir « the world by the tail » : tout lui réussit ces derniers temps, et il n'est pas
étonnant qu'il se sente si accompli et heureux.

⚠️ Un troisième motif séparateur est imprimé après la deuxième blague, **sans texte à sa suite**
(manuel p.181) — vraisemblablement un dessin humoristique **en image, absent de la couche texte**.

---

##### VOCABULARY COVERED IN MODULE 5 (manuel p.182) — liste intégrale

###### Common core

**Section one** (27 items) :
alternative · bachelor · chronic · clerk · defectology · disability · distance learning · dustman ·
embarrassed · impairment · impatient · non-credit · overalls · plight · pursue · rely ·
retardation · rise · seek · self-esteem · slate · sow · status · switch · transfer · updated ·
willing

**Section two** (7 items) :
check out · cope · executive · graduation · join · magic · unpredictable

**Section three** (17 items) :
detention · disobedient · disruptive · exclusion · heap · lines · muck around · praise ·
prestigious · prior · punishment · quarrel · ridiculous · shift · suspension · unruly · youngsters

**Section four** (5 items) :
extra-curricular · involved · sit (for an exam) · strength · weakness

**Section five** (3 items) :
encyclopaedia · make use of · resource

###### Arts Supplement

**Section one** (24 entrées imprimées) :
bin · boost · destiny · drift · engraved · flittery [sic] · flourish · flourish [sic — imprimé
deux fois de suite] · fully-fledged · hooked · initiative · invariably · novelist · persuade ·
print · promote · rub · seal · stuff · talented · thrilling · trade · try one's luck · typist

**Section two** (3 items) :
enrolment · standard · tongue

**Section three** (11 items) :
animate · assist · customize · database · download · measure · scan · split · store · translate ·
weight

> **Écarts manuel / guide relevés sur le vocabulaire**
> - Le guide (p.65) donne pour Arts Section one : *typist, typingpool, rub, hole, bin, burn,
>   stuff, talented, flourish, destiny, promote* — donc **hole**, **burn** et **typingpool**
>   figurent au guide mais **pas** dans la liste du manuel p.182, qui en revanche ajoute boost,
>   drift, engraved, flittery, fully-fledged, hooked, initiative, invariably, novelist, persuade,
>   print, seal, thrilling, trade, try one's luck.
> - Le guide (p.64) donne pour Section five : *thriller, classic, life-like, resources, make use
>   of* ; le manuel p.182 retient : *encyclopaedia, make use of, resource*. Seul « make use of »
>   est commun.
> - « flourish » apparaît **deux fois** dans la colonne Arts Section one du manuel p.182 [sic].

---

##### Tapescript du module

*(guide p.85 — « Module five. Section two : Listening »)*

**Genre** : interview journalistique (dialogue non littéraire). **Interlocuteurs** : un journaliste
et **Mrs Perks**, product manager chez **Thomas Cook Holidays**. **Transcription fidèle** :

> **Journalist :** I understand you are a product manager at Thomas Cook Holidays, Mrs Perks. When
> did you join them?
>
> **Mrs Perks :** I joined the company as a product executive in 1993, a month after graduation.
> Now I am a product manager for South Africa.
>
> **Journalist :** Can you tell us what your job consists in ?
>
> **Mrs Perks :** I'm looking after the Cities and Short Breaks programme. I check out
> destinations, find hotels, contract them, then I come back and brochure the product.
>
> **Journalist :** Do you have any special qualifications?
>
> **Mrs Perks :** I left school at 16 after GCSEs and went to a College of Further Education for
> two years after which I obtained a National Diploma in Business Studies with tourism. At 18, I
> went to Cardiff University to do a four-year course in the same field.
>
> **Journalist :** Do you speak any foreign languages?
>
> **Mrs Perks :** While at College I did a bi-lingual secretarial course in French and German. I
> also speak Greek and Portugese [sic].
>
> **Journalist :** I suppose you have a lot of benefits, don't you?
>
> **Mrs Perks :** Apart from getting very good wages, I travel a lot around the world. I love
> meeting people and visiting places.
>
> **Journalist :** What is a typical day for you ?
>
> **Mrs Perks :** There's no such thing. Most days start at 7.30am and I'm not home until 8pm and
> each day is unpredictable.
>
> **Journalist :** Doesn't this affect your family life?
>
> **Mrs Perks :** My husband works long hours so he copes well with my working pattern. And it's
> nice having days off during the week when the shops are quiet.
>
> **Journalist :** Have you ever thought of doing another job?
>
> **Mrs Perks :** No, never! While working in Africa, doing a safari on foot surrounded by animals
> I remember thinking: "And this is supposed to be work!". Magic !

**Éléments d'ancrage pour la génération** (faits présents dans le tapescript, à ne pas confondre
avec un corrigé imprimé — le guide n'en fournit aucun pour l'Activity 1) : entrée dans
l'entreprise en 1993 comme *product executive*, un mois après l'obtention du diplôme ; poste actuel
de *product manager* pour l'Afrique du Sud ; tâches citées = *check out destinations*, *find
hotels*, *contract them*, *brochure the product* ; parcours = école quittée à 16 ans après les
GCSEs, College of Further Education (National Diploma in Business Studies with tourism), puis
Cardiff University à 18 ans, cursus de 4 ans ; langues = français et allemand (cours de secrétariat
bilingue), plus grec et portugais ; avantages = très bon salaire, voyages dans le monde entier,
rencontres et découvertes ; journée type inexistante, 7h30–20h, imprévisible ; le mari fait lui
aussi de longues journées et s'accommode bien de ce rythme ; jours de congé en semaine quand les
magasins sont calmes.

---

##### Incertitudes (module 5)

**A. Supports en image, absents de la couche texte** *(récapitulatif — information critique)*

| Page manuel | Support manquant | Impact |
| --- | --- | --- |
| p.154 | **Set 1** de l'Activity 2 A (école traditionnelle) | Activité de comparaison non générable telle quelle ; le guide p.60 donne le champ lexical attendu. |
| p.155 | **Set 2** de l'Activity 2 A (apprentissage électronique) | idem. |
| p.156 | Les **3 photos** de l'Activity 3 A (Toni + 2 enfants) | Les questions 1-3 (identifier les handicaps) ne sont pas exploitables sans les images. |
| p.169 | Le **dessin** et le **school report** de la Section Four Activity 2 A | Le bulletin (matières, notes, appréciations) est entièrement perdu ; toute l'Activity 2 en dépend. |
| p.173 | Le **corps de l'article** « I'VE ALWAYS HAD A HEAD FOR WRITES » (seul le titre subsiste) | Arts §1 questions 1-6 non générables (dates, événements, relative clauses). |
| p.174 | Le **Curriculum Vitae** de Barbara Taylor Bradford | Question 5 (comparer texte et CV) non générable. |
| p.178 | Les **4 visuels d'annonces** numérotés 1-4 | L'appariement reste faisable par le corrigé (1+b, 2+c, 3+a, 4+d) mais la justification « with specific details » est perdue. |
| p.179 | L'**image à commenter** de l'exercice B | Production écrite sans support. |
| p.181 | Probable **dessin humoristique** en fin de Fun page (un troisième séparateur est imprimé, suivi de rien) | Troisième item de la Fun page inconnu. |

**B. Corrigés absents du guide** (activités transcrites sans clé)
- Section One : Activity 1 (proverbe) ; Activity 3 D questions 1, 3, 4, 5, 6 ; « Practising related
  grammar points » p.159 (comparisons of scale).
- Section Two : **toute l'Activity 1** (A tick-the-4, B TRUE/FALSE, C benefits, D pronunciation) ;
  « Practising related grammar points » p.161 (5 énoncés à rapporter). Les données factuelles
  existent dans le tapescript, mais aucune clé n'est imprimée.
- Section Three : **les 6 questions de compréhension** p.165 ; l'encadré *Exploring grammar* p.166
  et son exercice d'application.
- Section Four et Section Five : aucun corrigé (sections orales / production écrite) — normal.
- Arts §1 : questions 1 à 6 p.174-175 ; exercice de word-building p.175. Arts §2 : aucun corrigé.

**C. Ambiguïtés et coquilles de la source**
1. **Clé douteuse (guide p.62, Activity two)** : la citation 3 « We're always blamed for all the
   ills in society » est corrigée par « **a student** », alors que le contenu évoque plutôt le
   corps enseignant ; la citation 2 (« I'm struggling to cope with the pressures in my job ») est
   attribuée à « a teacher ». Transcrit tel qu'imprimé — à arbitrer avant génération.
2. **Word-building Arts p.175** : **6 suffixes** imprimés (`y`, `ed`, `ful`, `able`, `ment`, `ed`)
   pour **5 lignes à compléter** ; le second `ed` correspond vraisemblablement à l'exemple déjà
   résolu (`employ + ed`). La disposition de la page est graphique et dispersée : l'appariement
   exact des parts avec leur position d'origine n'est pas certain.
3. **Nombre de points ≠ nombre de lettres (manuel p.155)** : `prof . . . . . . al` compte 6 points
   alors que la réponse du guide (`professional`) en exige 7. Le manuel imprime aussi
   `associate deg . . . .` pour « degrees ».
4. **Guide p.60** : la clé de l'Activity 3 C omet les numéros 4 et 5 (« 1.alternative,
   2.behavioural, 3.physical, sufficiently, techniques ») ; l'ordre impose 4 = sufficiently,
   5 = techniques. Le guide écrit aussi « **Pursuing** » avec une majuscule dans la clé C de
   l'Activity 2, et « **illustrations** » au pluriel alors que la banque de mots du manuel
   imprime « illustration » au singulier.
5. **Coquilles [sic]** : « inteviewed » (manuel p.160) ; « jounalist » (manuel p.161) ; guillemet
   fermant manquant à l'item d) de *Practising related grammar points* (manuel p.161) ;
   « Portugese » (guide p.85) ; « It's great product » (manuel p.179, commentaire c) ;
   « messed just the first day of the pool » (manuel p.174, question 3 — lire probablement
   *the typing pool*) ; double point final « below.. » (manuel p.169) ; « flourish » imprimé deux
   fois dans la liste de vocabulaire (manuel p.182) ; « flittery » (manuel p.182), forme non
   standard dont le sens n'est pas établissable sans le texte de la p.173, lui-même en image ;
   « typingpool » en un seul mot (guide p.65) ; « Cambridge Road » figure sous « 8 Grange Road »
   dans l'adresse NLC (manuel p.176), ce qui paraît redondant avec la ligne « Cambridge CB3 9DU ».
6. **Pronunciation D2 (manuel p.161)** : les segments **soulignés** dans les quatre paires
   (them/south, thought/course, bi-lingual/life, special/French) ne sont pas identifiables dans la
   couche texte ; sans eux, la consigne « similar or different » n'a pas de référent certain.
7. **Section Four et Section Five** : le guide ne déclare **ni Grammar ni Pronunciation** pour la
   Section Four, et **aucun mini-project** n'est déclaré pour l'ensemble du module (alors que le
   Self-assessment p.180 comporte l'item « I've learnt how to conduct a mini-project »).
8. **Règle R-2 appliquée** : le texte « (The double life of) Alfred Bloggs » de L. G. Alexander
   (manuel p.158) est le seul support narratif d'auteur du module ; il est restitué par un résumé
   détaillé (faits, structure, lexique, accroche grammaticale) et **non reproduit verbatim**. Toute
   génération d'exercice devra soit s'appuyer sur ce résumé, soit rouvrir la page — les questions
   C, D et E restent néanmoins entièrement générables telles quelles.

### Module Six — NATURE : ANY FUTURE WITHOUT IT ? (manuel p.183-206 · guide p.67-75)

**Sources** : manuel élève 241303 « Activate and Perform — Third Year Secondary Education, Student's Book », p.183 à 206 ; guide enseignant 641303 « Activate and Perform — Teacher's Book », p.67 à 75 + tapescript p.86.

**Portée** : c'est le **dernier module du livre**. Les sections One à Five (manuel p.183-199) sont le **tronc commun**, complétées par les rubriques de clôture (Self-assessment p.204, Fun page p.205, Vocabulary p.206). Les pages **200 à 203** forment le **supplément ARTS**, imprimé en rose dans le manuel et **réservé à la filière Lettres** (« The items in pink are specific to the Arts branch »). La frontière est marquée explicitement ci-dessous, avant le titre `#### Supplément ARTS`.

---

#### Chapeau du module

**Titre du module (manuel p.183 · guide p.67)** : Module Six — NATURE : ANY FUTURE WITHOUT IT ?

**Topic (guide p.67)** : Ecology

**Subtopics (guide p.67)** : Environmental issues, natural disasters

**Cross-curricular learning goals (guide p.67)** : problem solving, critical thinking, efficient use of data, efficient working procedure, appropriate self-expression, ICT use, project work, communicating, working and living with others.

**Expected learning outcomes (manuel p.183)** — encadré verbatim :

> Expected learning outcomes :
> In this module, I'm going to
> - use what I already know to acquire new words and ideas about nature
> - listen to a story
> - read a study-based text
> - read short narrative texts
> - talk about environmental issues
> - write about a personal experience/fictional narrative
> - present a poster
> - practise and learn new lexical and grammatical items
> - read a poem
> - practise more writing activities
> - draw a picture
> - expand my knowledge of the world

> Note de transcription : le manuel imprime « read a study- based text » (espace parasite après le tiret). Restitué ici sans l'espace.

**Grammaire du module (par section, d'après le « Scope and sequence » du guide)**

| Section | Grammar |
| --- | --- |
| One — Introductory activities (guide p.68) | *(aucune rubrique Grammar dans le tableau)* |
| Two — Listening (guide p.70) | Deduction in the past — Must have + past participle |
| Three — Reading (guide p.71) | Will vs be going to |
| Four — Speaking (guide p.72) | *(aucune rubrique Grammar dans le tableau)* |
| Five — Writing (guide p.73) | past tenses ; cause/effect relationship |
| ARTS Section One (guide p.74) | If + simple past |
| ARTS Section Two (guide p.75) | *(pas de tableau « Scope and sequence » — seulement une ligne Vocabulary)* |

> À noter : la **formation des mots** (word formation) est travaillée en pratique dans le supplément ARTS, Activity 2 (manuel p.202, dérivation nom/adjectif/adverbe + voix passive), sans figurer dans aucune ligne « Grammar » du guide.

**Pronunciation** : Rhythm and intonation (guide p.70, **Section Two uniquement** — aucune autre section du module ne porte de rubrique Pronunciation).

**Homework recensés**
- Section One (guide p.68, manuel p.188) : « design a poster with a motto » — affiche de campagne écologique, à présenter en Section Four (Speaking).
- Section Two (guide p.70, manuel p.192) : « Homework : C test » — l'article sur l'ouragan Lenny à compléter (corrigé au guide p.70).
- Aucune rubrique Homework pour les Sections Three, Four, Five ni pour le supplément ARTS.

**Mini-project** : **aucune ligne « Mini-project » n'apparaît dans le « Scope and sequence » du guide pour ce module.** Le seul travail de type projet est le **poster** (Homework Section One → présentation en Section Four, Activity 3). Le Self-assessment (manuel p.204) contient pourtant l'item « I've learnt how to conduct a mini-project » — item générique de la grille, identique dans tous les modules.

**Fonctions communicatives du module (compilées des tableaux du guide)** : describing pictures, expressing feelings, expressing opinion (S1) ; expressing sympathy (S2) ; expressing opinion, convincing others to do something (S3) ; expressing surprise / interest / strong surprise / disbelief / shock / dismay (S4) ; describing events, giving information, expressing emotional attitudes (S5) ; describing a natural event (disaster), making comparisons (ARTS S1).

---

#### Section One : Introductory activities (manuel p.184-188 · guide p.68-69)

> ⚠️ **Anomalie d'en-tête source** : le manuel p.184 titre la page « **Session** one » alors que les pages 185, 186, 187 et 188 titrent « **Section** One ». Coquille du manuel [sic]. De même, l'Activity 3 de la Section Four renvoie à « (see session 1) » (manuel p.197).

**Scope and sequence (guide p.68)** — verbatim :

- **Skills/subskills and strategies**
  - *Writing*
    - make statements about concrete situations
    - produce descriptions to match illustrations related to a specific topic area
  - *Reading*
    - identify the communicative value of pictures
    - transfer information onto a spidergram
    - match words with definitions
    - match pictures with headlines
    - categorize ideas
    - acquire knowledge about a given topic
  - *Speaking*
    - support one's opinion with arguments
    - evaluate ideas
- **Vocabulary** : abrupt, alert, ash, catastrophe, dirty, drought, earthquake, ecology, eruption, expel, extinction, ferociously, flood, hole, lava, motto, pollution, predict, prevent, rate, rupture, seism [sic], shallow, species, steam, storm, stumble, threat, tidal, tsunami, vent, volcano, wave
- **Functions** : describing pictures ; expressing feelings ; expressing opinion
- **Homework** : design a poster with a motto
- *(pas de rubrique Grammar ni Pronunciation dans ce tableau)*

##### Activity 1 (manuel p.184-185)

**A. Énoncé verbatim** : « What do you think the biggest threats to the environment are ? In pairs, complete the spidergram. The following pictures may help you. »

- Support : **5 photos numérotées 1 à 5** (manuel p.184) — ⚠️ **support en image, absent de la couche texte (manuel p.184)**. Seuls les numéros 1, 2, 3, 4, 5 sont extraits ; le contenu des photos est inconnu.
- Le spidergram lui-même est une figure : une bulle centrale portant le texte « **Threats to the environment** » (manuel p.185) entourée de branches vides à remplir. ⚠️ **support en image (structure du spidergram), manuel p.185** — seul le libellé de la bulle centrale est dans la couche texte ; le nombre de branches n'est pas déterminable.

**Helpful note du guide (p.68) — verbatim** :

> Activity 1.A. Threats to the environment.
> Elicit words/expressions/statements like : extinction of species, imbalance in the ecological system, sea pollution, air pollution, domestic pollution, garbage dump(ing), water pollution, water scarcity, damage to the environment, global warming, ozone depletion, acid rain, deforestation, fire, drought, volcano, volcanic eruptions, tropical storms known as typhoons in the Pacific and hurricanes in the Atlantic, tornadoes or twisters, earthquake, tsunami (tidal wave)…..
> and any other relevant words/expressions suggested by the students.

**B. Énoncé verbatim** : « Classify these threats under the following headings. »

Tableau à deux colonnes, vide, à remplir (manuel p.185) :

| Natural disasters | Man-made disasters |
| --- | --- |
| *(à remplir)* | *(à remplir)* |

**Helpful note du guide (p.68)** : « Activity 1.B. Have the students check and compare answers in pairs/small groups. »

**Corrigé** : aucun corrigé imprimé pour l'Activity 1 (ni A ni B) — tâche ouverte.

##### Activity 2 (manuel p.185, pictures p.186)

**Énoncé verbatim** : « Match the following words with the definitions below. The pictures may help you. »

**Banque de mots (verbatim)** : earthquake , flood , drought , volcano, tsunami (tidal wave)

**Définitions à apparier (verbatim, 5 items)** :

1. ………….. : period of dry weather, especially a long one that is injurious to crops.
2. ………….. : a great flowing or overflowing of water over land.
3. ………….. : an unusually large sea wave produced by a seaquake or undersea volcanic eruption. Also called seismic sea wave. ( Japanese : tsu =harbour nami=wave )
4. ………….. : a series of vibrations induced in the earth's crust by the abrupt rupture and rebound of rocks in which elastic strain has been slowly accumulating, rated on the richter scale [sic — minuscule dans la source] from 1 to 10 ( after Charles F Richter (1900-85) U.S. seismologist. [sic — parenthèse ouvrante jamais refermée dans la source]
5. ………….. : a vent (hole) in the earth's crust through which lava, steam, ashes, etc are expelled, either continuously or at irregular intervals.

- Support associé : **5 photos numérotées 1 à 5** disposées sur la page (manuel p.186). ⚠️ **support en image, absent de la couche texte (manuel p.186)** — seuls les numéros 1 à 5 sont extraits. Le corrigé du guide confirme que ces photos appartiennent bien à l'Activity 2 (il donne un numéro de photo pour chaque réponse).

**Corrigé (guide p.69) — verbatim** :

> Activity 2. 1+drought (+picture 1) , 2+flood (+picture 2) , 3+tsunami (+picture3)
> 4+earthquake (+picture5) , 5+volcano (+picture4)

Soit : 1 = drought (photo 1) · 2 = flood (photo 2) · 3 = tsunami (photo 3) · 4 = earthquake (photo 5) · 5 = volcano (photo 4).

##### Activity 3 (manuel p.186-187)

**Énoncé verbatim** : « Match each picture with the appropriate headline. »

**Les 6 gros titres (verbatim, majuscules de la source)** :

1. A 70-YEAR-OLD WOMAN STUMBLES PAST SCENES OF DESTRUCTION AFTER A KILLER EARTHQUAKE
2. IS LATEST STORMY WEATHER A CAUSE FOR ALARM ?
3. HURRICANE THAT BROUGHT FEAR TO HOLIDAY ISLANDS
4. THE VOLCANO OF MOUNT ST HELENS WAS DORMANT FOR 123 YEARS BEFORE ERUPTING FEROCIOUSLY
5. A CITY GOES ON FLOOD ALERT
6. A TSUNAMI LOSES SPEED WHEN IT REACHES SHALLOWER WATER, BUT ITS HEIGHT GROWS

- Support : **6 images étiquetées A, B, C, D, E, F** (manuel p.187, deux par ligne). ⚠️ **support en image, absent de la couche texte (manuel p.187)** — seules les lettres A à F sont extraites.
- Ligne de réponse imprimée sous les images (manuel p.187) : « 1+….., 2+……., 3+……, 4+…….. 5+…….., 6+……… »

**Corrigé (guide p.69) — verbatim** : « Activity 3. 1+D , 2+F , 3+A , 4+B , 5+E , 6+C »

Soit : titre 1 → image D · titre 2 → image F · titre 3 → image A · titre 4 → image B · titre 5 → image E · titre 6 → image C.

##### Activity 4 (manuel p.188)

**Énoncé verbatim** : « Discuss the statement in the bubble and answer the questions below. »

**Bulle (verbatim, présente dans la couche texte)** :

> There is little we can do to predict natural disasters and even less to prevent them.

**Questions (verbatim)** :

1. Are all the disasters predictable and preventable ?
2. Are all the disasters caused by the actions of Man ?
3. Can you play an efficient role in saving the environment from catastrophes ? How ?

**Helpful note du guide (p.68)** : « Activity 4. Have the students read the statement and debate it through answering the questions. The students should support their ideas and viewpoints with concrete examples. »

**Corrigé** : aucun — tâche de débat, ouverte.

##### Homework — Section One (manuel p.188)

**Énoncé verbatim** :

> You are organizing a compaign [sic — pour « campaign »] in your school to encourage students to save the environment.
> Work in pairs/small groups to design a poster representing an idea and your motto, like
>
> « If it's not far, don't go by car. »
> « Do it right, switch off the light. »
>
> Be ready to present it at the Speaking Section.

**Helpful note du guide (p.69)** : « Explain the homework and give help and guidance when needed. »

---

#### Section Two : Listening (manuel p.189-192 · guide p.70 + tapescript p.86)

**Scope and sequence (guide p.70)** — verbatim :

- **Skills/subskills and strategies**
  - *Listening*
    - listen to a text and report orally and in writing on gist and specific details
    - predict content from core vocabulary
    - identify logical relations in a text Imitate appropriate intonation patterns *(le guide imprime ces deux items sur une seule puce, sans séparateur — [sic])*
    - identify the communicative function of an utterance
  - *Writing / Speaking*
    - produce a summary
- **Vocabulary** : partner - wedding - waves - honetmoon [sic] - smash - pospone [sic] - mourner - sorrowful - grief - corpse - dread(ful)
- **Grammar** : Deduction in the past — Must have + past participle
- **Function** : expressing sympathy
- **Pronunciation** : Rhythm and intonation
- **Homework** : Homework : C test

**Le support audio** : le témoignage de **Sandra Bell**, mère de **Natalie** (« Nat »), en **4 parties** — récit du tsunami de Thaïlande (décembre 2004) qui a coûté la vie à Natalie et à son mari **Andy** pendant leur voyage de noces. Source citée en fin de tapescript : **DAILY MIRROR (NOVEMBER 2005)**. Texte intégral en fin de fiche, § *Tapescript du module*.

##### BEFORE YOU LISTEN — Activity 1 (manuel p.189)

**Énoncé verbatim** : « Put the following words/expressions under the appropriate heading »

**Banque de mots (verbatim, 21 items)** : Partner - wedding - hotel - tsunami - wedding ring - waves - flight - orphaned - loss of life - mourner - devastation - damage - fishermen - corpses - wedding pictures - funeral - beachside - boat trip - boats - smashed - honeymoon.

**Tableau à remplir, 5 colonnes (vide dans le manuel)** :

| The sea | Travel | Marriage | Natural disasters | Death |
| --- | --- | --- | --- | --- |
| *(à remplir)* | *(à remplir)* | *(à remplir)* | *(à remplir)* | *(à remplir)* |

**Corrigé** : aucun corrigé imprimé au guide pour cette activité.

##### BEFORE YOU LISTEN — Activity 2 (manuel p.189)

**Énoncé verbatim** : « Read the introduction below and guess what the listening passage is about (the pictures and the words in Activity 1 may help you) »

**Encadré d'introduction (verbatim)** :

> In the space of 16 months, Sandra Bell went from attending her daughter's wedding to being chief mourner at her funeral. Sandra 63, Legbourne, Lincolnshire, tells her heartbreaking story.

- ⚠️ **support en image, absent de la couche texte (manuel p.189)** : l'énoncé renvoie à « the pictures », mais aucune photo n'apparaît dans la couche texte de la page. Nombre et contenu inconnus.

**Corrigé** : aucun — activité de prédiction.

##### AS YOU LISTEN — A (manuel p.189)

**Énoncé verbatim** : « Listen to the whole passage and check your predictions »

##### AS YOU LISTEN — B : PART 1 (manuel p.189-190)

**Énoncé verbatim** : « Listen to PART 1 and »

**B.1 — « complete the table below »** (tableau à 5 colonnes, une seule case pré-remplie) :

| Names of the couple | Date of the wedding | Time of the honeymoon | Honeymoon destination | Incident |
| --- | --- | --- | --- | --- |
| – Natalie<br>– *(à compléter)* | *(à compléter)* | *(à compléter)* | *(à compléter)* | *(à compléter)* |

**B.2 — « circle the correct alternative »** (verbatim) :

> a/ They postponed (their honeymoon) means :
> • put it off until later
> • decided
> • celebrated
>
> b/ The couple changed their minds about
> • the place
> • the time of the honeymoon
> • the time of the wedding

**Corrigé** : aucun corrigé imprimé au guide pour B.1 ni B.2 (voir § Incertitudes).

##### AS YOU LISTEN — C : PARTS 2 et 3 (manuel p.190)

**Énoncé verbatim** : « Listen to PARTS 2 and 3 and »

**C.1 — « Complete the sentence with the appropriate information »** :

> When Nat phoned her mother, she…………………………. and …………………….. time

**C.2 — « In what order did the following events occur ? Complete the table in the margin (the first answer is given to you) »**

Les 6 énoncés (verbatim) :

- a. Nat phoned her mother on Christmas day
- b. Sandra dialled Nat's mobile. Nat didn't answer
- c. She found out that there was an extensive loss of life
- d. Ted, Sandra's partner, put the TV on
- e. The news was all about a tsunami in Thailand
- f. Sandra searched the internet

Tableau en marge, pré-rempli à la ligne 1 :

| Order of events | Sentence |
| --- | --- |
| 1 | a |
| 2 | *(à compléter)* |
| 3 | *(à compléter)* |
| 4 | *(à compléter)* |
| 5 | *(à compléter)* |
| 6 | *(à compléter)* |

Consigne de vérification imprimée après le tableau : « Listen again and check your answers. »

**C.3 (verbatim)** : « What is meant by the following sentence ? "I refused to think the worst" »

**C.4 (verbatim)** : « Express the following sentence differently : I couldn't stop searching the screen in case I glimpsed Nat and her husband. »

> Écart source à signaler : le manuel écrit « **Nat and her husband** », le tapescript du guide (p.86, PART 3) écrit « **Nat and Andy** ». Voir § Incertitudes.

**Corrigé** : aucun corrigé imprimé au guide pour C.1 à C.4.

##### AS YOU LISTEN — D : PART 3 (manuel p.190)

**Énoncé verbatim** : « Listen to PART 3 again and »

**D.1 — « complete the table with the words describing »** :

| The island | Nat's flat |
| --- | --- |
| *(à remplir)* | *(à remplir)* |

**D.2 (verbatim)** : « Sandra said : "We want to do something good for them." What did they decide to do
- for orphaned children ?
- for the fishermen ? »

> Écart source à signaler : les éléments demandés en D.1 (l'île, l'appartement de Nat) et en D.2 (les orphelins, les pêcheurs) figurent tous dans la **PART 4** du tapescript, pas dans la PART 3. Voir § Incertitudes.

**Corrigé** : aucun corrigé imprimé au guide.

##### AS YOU LISTEN — E : passage entier (manuel p.191)

**Énoncé verbatim** : « Listen to the whole passage again and »

**E.1 — « Tick the appropriate title. »**
- A woman's diary
- The tragic honeymoon
- The orphaned children

**E.2 — « How would you describe the woman's mood ? Circle the appropriate adjectives »**
Indifferent - sorrowful - sad - sarcastic - grieved - mournful

**E.3 (verbatim)** : « Is the story real or imaginary ? (Justify your answer with details from the text) »

**E.4 (verbatim)** : « Read silently as you listen to the following part of the text (try to imitate the same tone of voice) » — extrait imprimé dans le manuel :

> As I watched, the news got worse by the minute. I dialled Nat's mobile. My heart pounded as I prayed for her to answer. But she didn't pick up. I spent the morning ringing Nat's phone, the foreign office, the hotel, searching the internet and going round in circles.

> Écart source à signaler : le manuel imprime « the news got **worse** by the minute », le tapescript du guide (p.86, PART 2) imprime « the news got **worst** by the minute » [sic]. C'est l'exercice de **prononciation** de la section (Rhythm and intonation).

**Corrigé** : aucun corrigé imprimé au guide pour E.1 à E.4.

##### Exploring grammar — Must + perfect infinitive (manuel p.191)

**Encadré verbatim** :

> **Exploring grammar**
>
> Focus on the following sentence :
> « If Andy was dead, Nat must have been, too »
>
> Does the underlined utterance express ?
> - certainty
> - deduction
> - obligation
>
> Is the sentence in the present or in the past ?
>
> **Complete the rule**
>
> > Must……… + past ……….. is used to express ………. in the …….

**La règle attendue, d'après le guide (p.70, ligne Grammar)** : « **Deduction in the past — Must have + past participle** ». La règle à trous se complète donc : *Must **have** + past **participle** is used to express **deduction** in the **past**.*

##### AFTER YOU LISTEN — WRITING / SPEAKING (manuel p.192)

**Énoncé verbatim** : « Use the answers to the questions to summarize the story (the people / the incident / the dramatic part of the story and the events leading up to it. [sic — parenthèse jamais refermée] Retell the story to your classmates. »

##### Homework — C test (manuel p.192 · corrigé guide p.70)

**Énoncé verbatim** : « Read the following article and complete the missing letters of the words in bold type. Each dot stands for one letter. »

**Article à trous (verbatim, ponctuation et espacements de la source)** :

> Hundreds of Britons were trapped as a killer Hurricane lashed the Caribbean and a hundred more trav…… were disappointed when told their dream hol….. were being axed because of 150 mph Hurricane Lenny.
> Hou… were swept away, roads were washed away, runway lights were da….. and roads were flo…. . A fish….. who went to get a close look at the turmoil dis…….. under the waves before being rescued. Many people were inj…. . Hundreds of holiday makers had been evacuated from hot… . My heart goes out to all those who have loved ones, livelihoods and their possessions in the deva……. caused by Hurricane Lenny.

**Corrigé (guide p.70) — verbatim** :

> travellers-holidays-houses-damaged-flooded-fishermen-disappeared-injured-hotels-devastation

Appariement mot à mot (10 trous, dans l'ordre du texte) : trav…… = **travellers** · hol….. = **holidays** · Hou… = **houses** · da….. = **damaged** · flo…. = **flooded** · fish….. = **fishermen** · dis…….. = **disappeared** · inj…. = **injured** · hot… = **hotels** · deva……. = **devastation**.

---

#### Section Three : Reading (manuel p.193-195 · guide p.71)

**Scope and sequence (guide p.71)** — verbatim :

- **Skills/subskills and strategies**
  - *Reading*
    - predict content of a text from notes
    - skim for gist
    - scan a text for specific information
    - identify vocabulary items in context
    - evaluate and react to content
    - acquire knowledge about global warming
  - *Speaking*
    - express opinion about a specific topic
    - make statements about specific issues
- **Vocabulary** : release – impact – findings – implications – accelerated – adequate – global warming – renewable energy – solar – simulate - melting
- **Grammar** : Will vs be going to
- **Functions** : expressing opinion ; convincing others to do something
- *(pas de rubrique Pronunciation ni Homework dans ce tableau)*

##### BEFORE YOU READ (manuel p.193)

**Énoncé verbatim** : « Guess what will cause the following predictions. »

Les 7 prédictions (verbatim) :

1. Polar bears and penguins will disappear.
2. Winters will be 10 degrees colder.
3. Africa will be hotter and suffer more droughts.
4. Skin cancer will increase.
5. Many countries will have no drinking water.
6. Countries such as the Maldives, Holland and Bangladesh will disappear under water.
7. Wars will start between countries fighting over water.

**Corrigé** : aucun — activité de prédiction ouverte.

##### AS YOU READ — A + le texte-support (manuel p.193)

**Énoncé verbatim (A)** : « Read the text and find out which of the above predictions it deals with. »

**Texte-support** — titre : « **Global warming is human made** ». Genre : texte informatif « study-based », compte rendu d'une étude scientifique. Aucune source ni auteur n'est cité dans le manuel. Deux paragraphes numérotés. Transcription verbatim :

> **Global warming is human made**
>
> 1. Findings from a new study released last week prove that global warming is caused by human activity, and not by natural environmental factors. Researchers at the Scripps Institute of Oceanography have found clear evidence of human-produced warming in the world's oceans that is likely to impact water resources in regions around the globe. These findings remove much of the uncertainty associated with debates about global warming. Many world leaders have closed their ears to this fact so they don't have to limit their economic activity or introduce expensive pollution controls. This is one of the reasons America has not signed the Kyoto Treaty on climate change. The US government prefers to believe global warming is a natural phenomenon, caused by volcanoes and solar energy.
>
> 2. Professor Tim Barnett said, "This is perhaps the most compelling evidence yet that global warming is happening right now and it shows that we can successfully simulate its past and likely future evolution." Barnett says the results hold implications for millions of people in the near future. In the decades immediately ahead, the changes will be felt in regional water supplies, including areas impacted by accelerated glacier melting in the South American Andes and in western China, putting millions of people at risk without adequate summertime water. Perhaps now more countries will sign up the Kyoto Protocol.

> Note : le manuel écrit « sign up the Kyoto Protocol » au § 2 (sans « to »), alors que l'exercice « Exploring grammar » de la p.194 reprend la même phrase avec « sign up **to** the Kyoto Protocol ». Incohérence de la source, signalée en Incertitudes.

##### AS YOU READ — B : synonymes (manuel p.193)

**Énoncé verbatim** : « Find in the text the synonyms of the following words. »

- affect (§1) :
- doubt (§1) :
- research (§1) :
- consequences (§2) :
- sufficient (§2) :
- quickened (§2) :

**Corrigé (guide p.71) — verbatim** : « B* impact / uncertainty / findings / implications / adequate / accelerated »

Soit, dans l'ordre des items : affect = **impact** · doubt = **uncertainty** · research = **findings** · consequences = **implications** · sufficient = **adequate** · quickened = **accelerated**.

##### AS YOU READ — C : vrai / faux (manuel p.194)

**Énoncé verbatim** : « Read the text again and say whether the following statements are true or false. »

1. Global warming is caused by natural environmental factors.
2. Clear evidence of human-produced warming is in the world's rivers.
3. Global warming is not likely to impact water resources around the globe.
4. Millions of people will be at risk of having inadequate water supplies.
5. Many world leaders have ignored global warming.

**Corrigé** : aucun corrigé imprimé au guide pour C.

##### AS YOU READ — D (manuel p.194)

**Énoncé verbatim** : « Prepare two questions you'd like to ask the class about the article. » — tâche ouverte, sans corrigé.

##### AS YOU READ — E : appariement de segments (manuel p.194)

**Énoncé verbatim** : « Match the following phrases to get meaningful expressions. »

| Colonne 1 | Colonne 2 |
| --- | --- |
| 1 - Researchers have found | a - immediately ahead |
| 2 - in the decades | b - evolution |
| 3 - putting millions of people | c - resources |
| 4 - water | d - clear evidence |
| 5 - findings | e - at risk |
| 6 - future | f - from a new study |

Lignes de réponse imprimées : « 1- ............... 2- ............... 3- ............... 4- ............... 5- ............... 6- ............... »

**Corrigé (guide p.71) — verbatim** : « E* 1 - d / 2 - a / 3 - e / 4 - c / 5 - f / 6 – b »

Expressions reconstituées : Researchers have found **clear evidence** · in the decades **immediately ahead** · putting millions of people **at risk** · water **resources** · findings **from a new study** · future **evolution**.

##### AS YOU READ — F (manuel p.194)

**Énoncé verbatim** : « Do you think global warming is a natural phenomenon or caused by Man ? » — question d'opinion, sans corrigé.

##### Exploring grammar — Will vs Be going to (manuel p.194)

**Encadré verbatim** :

> **Exploring grammar**
>
> 1 - The changes will be felt in regional water supplies.
> 2 - More countries will sign up to the Kyoto Protocol.
>
> Do you think the writer **hopes / expects / is sure** that the action will take place in the future ?
> *(les trois verbes sont imprimés empilés en accolade devant « that the action will take place in the future ? »)*
>
> Can you replace *will* by *be going to* in these sentences ? Why ? Why not ? What is the difference between the two structures ?
>
> Read the following notes to find out.

**Tableau de règle, verbatim (manuel p.194)** :

| Will | Be going to |
| --- | --- |
| **Habitual action**<br>These birds will come back next year. | **Prior plan**<br>I'm going to meet them at the airport. |
| **Making a promise**<br>I'll finish this work by 7:00 tonight. | **Prediction**<br>Look at those clouds! It's going to rain. |
| **Making an offer**<br>If you need that medicine now, I'll get it for you. | **Commands and refusals**<br>You are going to take that medicine whether you like it or not. |
| **Something expected**<br>I think Brazilians will win the football match. | **Permanent state**<br>Their new house is going to look over the river. |

##### AFTER YOU READ — discussion (manuel p.195)

**Énoncé verbatim** : « In groups discuss whether you will carry out the following actions to help slow down global warming. »

1. Walk instead of driving or taking public transport.
2. Use public transport instead of driving.
3. Use the lights in your house less.
4. Replace some of your electricity supply with renewable energy, such as solar energy.
5. Plant a tree in the forest.
6. Recycle everything you use.
7. Donate money to organisations pushing for control on global warming.

**Corrigé** : aucun — discussion ouverte.

##### Practising related grammar points (manuel p.195)

**Énoncé verbatim** : « Use "be going to" or "will" » — 10 items, verbatim :

1. What do you want to do when you leave school ? — I ………… (be) a flamenco dancer.
2. This box is very heavy! — Don't worry. I ………….. (carry) it for you.
3. Why do you want to sell your flat ? — I …………. (move) to the country side.
4. Why don't you change your hairstyle ? You …………. (look) much better.
5. ………… (you/have) another cake ? — No, thank you. I've already had two.
6. Stop worrying about the exam. You ………… (pass) it easily.
7. Do you want to go to the park this afternoon ? — I can't. I…………. (visit) my grandparents.
8. Sorry I can't be at work next week - I'm …………. (have) minor surgery.
9. Do you want to borrow my car ? — Thanks. I ………….. (bring) it back tonight.
10. The Americans …………… (send) a camera deeper into space than ever before to see what pictures it ……………..(send) back.

**Corrigé (guide p.71) — verbatim** :

> Practising grammar
> 1- I'm going to be
> 2- Will carry
> 3- I'm going to move
> 4- Will look
> 5- Will you have
> 6- Will pass
> 7- I'm going to visit
> 8- I'm going to have
> 9- Will bring
> 10- Are going to send / will send

> Note : l'item 8 du manuel imprime déjà « I'm …………. (have) » ; le corrigé du guide donne « I'm going to have », ce qui est cohérent. Les majuscules initiales du corrigé (« Will carry ») sont celles du guide.

---

#### Section Four : Speaking (manuel p.196-197 · guide p.72)

**Scope and sequence (guide p.72)** — verbatim :

- **Skills/subskills and strategies**
  - *Reading*
    - judge the accuracy of information with respect to the reader's knowledge of the world
    - evaluate information/ideas
    - develop appreciation of self, environment and culture
  - *Speaking*
    - make statements about concrete situations
    - express / respond to surprise, shock, disbelief and dismay
    - give a prepared oral presentation related to information presented in a poster
- **Vocabulary** : brush, light bulb, tap, switch off, spill, tanker, trash
- **Functions** : expressing surprise ; expressing interest ; expressing strong surprise ; expressing disbelief ; expressing shock ; expressing dismay
- *(pas de rubrique Grammar, Pronunciation ni Homework dans ce tableau)*

**Helpful notes (guide p.72) — verbatim** :

> Make sure the students understand the communicative function of each expression / idiomatic expression introduced in the list. This will help them reinvest the expressions in their role play.
> Have the students present their posters and explain the message conveyed through the picture and the motto.
> Encourage the students to comment on the different presentations.

##### Activity 1 — « How green are you ? » quiz (manuel p.196-197)

**Énoncé verbatim** : « A) Work in pairs and do the following quizz [sic] to find out how "green" you are. »

Les 7 questions, verbatim (la numérotation de la source mélange « 1. » et « 4) » — restituée telle quelle) :

1. Which form of transport is best for the environment ?
   a) driving (by car)
   b) flying by plane.
   c) riding a bicycle.
2. Do you leave the tap on when you brush your teeth ?
   a) Yes.
   b) No
   c) does it make a difference ?
3. As well as putting their health and the health of those around in danger, smokers also put the environment in danger
   a) True.
   b) False.
   c) I'm not sure.
4) You are busy in the house tidying up, going from one room to another. Which is the best way to save energy ?
   a) switch the lights on and off every time you move from room to room.
   b) keep the lights on as you move about the house.
   c) I see no reason why I should bother.
5) When you have finished watching TV do you
   a) switch it off completely ?
   b) leave it on standby ?
   c) leave it on all night ?
6) Do you use energy saving light bulbs ?
   a) Yes.
   b) No.
   c) what is an energy saving light bulb ?
7) If your tap loses one drop per second, how much water do you waste per day ?
   a) 10 litres.
   b) 20litres. [sic — espace manquante]
   c) 30litres. [sic]

**Barème (manuel p.197) — verbatim** : « Now check your answers with your teacher and count 1 point for each green answer. »

| 1-3 | 4--6 [sic — double tiret dans la source] | 7-10 |
| --- | --- | --- |
| You have a lot of changes to make if you want to be greener. | Not bad! You know about how you can help the planet. You are quite green | Well done! You have a green head on your shoulders. |

> ⚠️ Incohérence de la source : le quiz ne comporte que **7** questions, donc au maximum 7 points, alors que la grille de score va jusqu'à **10**. Signalé en Incertitudes.

**Corrigé** : **aucun corrigé imprimé** — le manuel renvoie explicitement au professeur (« check your answers with your teacher ») et le guide n'en donne pas.

##### Activity 2 — Role play (manuel p.197)

**Chapeau verbatim** : « There are many ways of expressing surprise or shock. Word choice and also intonation affect how much surprise or shock you express. Here are some phrases that can be used. »

**Tableau de fonctions, verbatim (manuel p.197)** :

| Mild surprise / Interest | Strong surprise / Disbelief | Shock / dismay |
| --- | --- | --- |
| Really? | Wow, that's amazing! | Oh, no! |
| That's interesting | That's unbelievable! | How shocking! |
| How nice to +V ! | You're joking! | That's terrible! |
| I didn't know that. | I can't believe it! | That's awful! |
| Fancy +Ving ! | That's incredible! | That's horrible! |
| Oh, come on! | You're pulling my leg! | |
| This is a surprise! | | |
| This is a real surprise! | | |

**Consigne 1 (verbatim)** : « Now work with a partner to expand the following notes into short dialogues using the expressions in the table. (follow the example given.) »

**Exemple donné (verbatim)** :

> Student A : Did you know that the highest earthquake happened in 1556, in China ?
> Student B : Really ?
> Student A : It was the deadliest earthquake in history with 830,000deaths. [sic — espace manquante]
> Student B : That's terrible!

> Note : le manuel écrit « the **highest** earthquake » — formulation aberrante pour un séisme (probablement pour « deadliest » ou « strongest »). Coquille de la source, signalée en Incertitudes.

**Consigne 2 (verbatim)** : « Switch roles. » — les 5 situations à développer, verbatim :

- Situation 1 : 1978 / Spanish tanker / to spill / 220.000tons of oil / into sea. [sic — espace manquante]
- Situation 2 : 2020 / Tunisia / suffer / water shortage /
- Situation 3 : polyester / better for evironment [sic] / cotton.
- Situation 4 : each person / produce 500gr trash / every day.
- Situation 5 : habitat destruction / to cause / extinction / one of every four species / every day.

**Corrigé** : aucun — production orale libre.

##### Activity 3 — Poster presentation (manuel p.197)

**Énoncé verbatim** : « Poster presentation (see session 1) [sic — « session » pour « section »] — Now it's time for the poster presentation. Explain the message conveyed through the picture and the motto to your classmates. »

C'est la restitution du Homework de la Section One (manuel p.188).

---

#### Section Five : Writing about a personal experience / fictional narrative (manuel p.198-199 · guide p.73)

**Titre exact de la section (manuel p.198)** : « Writing about a personal experience / fictional narrative »

**Scope and sequence (guide p.73)** — verbatim :

- **Skills/subskills and strategies**
  - *Reading*
    - skim texts to infer common topic
    - recognize text structure
    - guess the meaning of unfamiliar words through context clues
    - complete an outline of a story
    - infer causes and effects from events described
    - transfer information onto a table
    - identify features of a narrative text
    - follow a sequence of events in a narrative
    - extract salient points for subsequent use in writing
  - *Writing*
    - reinvest knowledge about text structure and its linguistic features in writing
    - describe a sequence of events with/without explicit cohesion
    - apply the writing process to produce a narrative
- **Vocabulary** : bitterly, chaos, collapse, crack, current, disintegrate, engulf, float, grab, grasp, looters, perish, pin(v), scream, shiver, sweep, wipe, yell
- **Grammar** : past tenses ; cause/effect relationship
- **Functions** : describing events ; giving information ; expressing emotional attitudes
- *(pas de rubrique Pronunciation ni Homework dans ce tableau)*

**Helpful notes (guide p.73) — verbatim** :

> While dealing with the texts and the activities suggested, draw the students' attention to the key aspects of a narrative text. Extracting the salient points of a narrative text will help them perform well in their written production.

##### BEFORE YOU WRITE — chapeau et les deux textes (manuel p.198)

**Chapeau verbatim** : « Read text A. : a story told by Kioka Williams, a lady who survived hurricane Katrina which struck the USA on August 29, 2005 and text B : a story told by Florencio Libaton, a man who survived the Philippines mudslide of 2006, then do the activities below. »

**Text A — témoignage de Kioka Williams (ouragan Katrina, La Nouvelle-Orléans, 29 août 2005)**. Genre : témoignage de presse à la première personne, non littéraire. Transcription verbatim :

> « Oh my God, it was hell. We were screaming, yelling, flashing lights. It was complete chaos. So many people perished. I had to rush to the roof of my employer's Beauty shop as flood waters rose. I saw a friend of mine – a resident in a boarding house in New Orleans – climbing onto the roof to escape the rising waters. Two elderly residents never made it out and a third was washed away as he tried to climb the roof. A man and his wife were rescued by boat from the attic of their flooded home. I also saw a man grabbing a lady and they swam with the current. It was terrifying. You should have seen the cars floating around them. We watched the apartments disintegrate. You could hear the big pieces of wood cracking and breaking apart. Total devastation. Everything is gone. Complexes are wiped clear. It's so depressing, really because you have no address. Many looters profited by the chaotic situation to take away goods and furniture.
> I don't want to live here anymore. »

**Text B — témoignage de Florencio Libaton (glissement de terrain aux Philippines, 2006)** — **texte à trous** : c'est à la fois le texte-support et l'exercice de conjugaison de la section. Consigne imprimée juste sous le titre : « **Complete the gaps with the appropriate verb forms.** » Transcription verbatim, trous inclus :

> « As many as 18 hundred people were killed when a wall of mud (sweep)………. into our small farming village. I was at home when my wife, (rush) …………in, saying : "The mountain has collapsed". I thought of my son and my two daughters at school but my wife told me that the school (already/engulf)…………
> We (grab) …………..each other and (run) …….My wife (shiver) ……….out of fear. The mudslide (catch) ……up with us, throwing large pieces of rock onto us. I bitterly remember the moment I (lose) ………..grasp on my wife. I was saved by a tree trunk that pinned me against some rocks but I lost my dear wife and my three children forever ».

**Corrigé du texte à trous (guide p.73) — verbatim, présenté en deux colonnes (infinitif → forme attendue)** :

| Verbe donné | Forme attendue |
| --- | --- |
| sweep | swept |
| rush | rushed |
| already engulf | Had already been engulfed [sic — majuscule initiale du guide, alors que la forme est en milieu de phrase ; passif au past perfect] |
| grab | grabbed |
| run | ran |
| shiver | was shivering |
| catch | caught |
| lose | lost |

> Incohérence interne du texte B, à signaler : Florencio parle d'« my son and my two daughters » (3 enfants) puis de « my three children » — cohérent ; mais le chapeau du manuel dit « the Philippines mudslide of **2006** » alors que la catastrophe de Guinsaugon a effectivement eu lieu en février 2006 — pas d'anomalie ici.

##### Questions 1 à 6 (manuel p.198-199)

**Question 1 (verbatim)** : « As far as the topic is concerned, what is common between the two texts ? » — sans corrigé.

**Question 2 (verbatim)** : « Complete the table with an example of each verb form from the two texts. »
- Past simple :
- Past progressive :
- Past perfect :

— sans corrigé imprimé (mais les formes du corrigé de Text B fournissent les exemples : *swept / rushed / grabbed / ran / caught / lost* pour le past simple, *was shivering* pour le past progressive, *had already been engulfed* pour le past perfect passif).

**Question 3 (verbatim)** : « Match each word in column A with its corresponding meaning in column B. »

| A | B |
| --- | --- |
| 1. engulf (text B) | a) steal/take away goods (by force) |
| 2. grab (text B) | b) take roughly |
| 3. pin (text B) | c) die |
| 4. yell (text A) | d) make unable to move |
| 5. loot (text A) | e) cry loudly out of fright |
| 6. perish (text A) | f) swallow up / cover |

**Corrigé (guide p.73) — verbatim** : « 3. 1 + f / 2 + b / 3 + d / 4 + e / 5 + a / 6 + c »

Soit : engulf = swallow up / cover · grab = take roughly · pin = make unable to move · yell = cry loudly out of fright · loot = steal/take away goods (by force) · perish = die.

**Question 4 (verbatim)** : « Read and find out some examples of descriptions in text A and text B and write them in the table below. »

| Descriptive words | Described person / object / place / feeling / situation …. |
| --- | --- |
| *(à remplir)* | *(à remplir)* |

— sans corrigé.

**Question 5 (verbatim)** : « Read text B again and complete the outline of Florencio's story » — schéma en marge, partiellement pré-rempli :

> the mountain collapsed
> ………………………..…
> ………………………..…
> ………………………..…
> Florencio was saved by a tree trunk
> ………………………..…

— sans corrigé.

> ⚠️ La mise en page de la source entrelace la question 5, son schéma en marge et la question 6 ; le schéma est un encadré de 6 lignes dont la 1re (« the mountain collapsed ») et la 5e (« Florencio was saved by a tree trunk ») sont pré-remplies. Reconstitution fondée sur l'ordre d'extraction — voir Incertitudes.

**Question 6 (verbatim)** : « Find out two examples (from both texts) in which there is a link between a cause and an effect. » — sans corrigé.

##### AS YOU WRITE — la tâche d'écriture (manuel p.199)

**Consigne verbatim** :

> Write a short story (15-20 lines) about a natural disaster you witnessed, heard about or watched in a film / special TV report or an imaginary one.
> - Spend about ten minutes planning the outline of the story
> - Jot down any ideas that come to your mind
> - Write a first draft of your story
> - Read it through and check for ;
>   - use of correct narrative tenses
>   - appropriate use of descriptive expressions
>   - clarity of classification and division of ideas/events
>   - development of ideas/events through a chronological order
>   - logical link of causes and effects
>   - appropriate use of punctuation marks
>   - accuracy of spelling
> - Make the necessary modifications to improve your narrative
> - Exchange texts with a classmate for proofreading and consider each other's feedback
> - Write the final draft of your story
>
> Display the stories around the class so that you can read each other's.
> Which story did you like best ? Why ?

---

> ## ⛔ FIN DU TRONC COMMUN
>
> Tout ce qui suit jusqu'à la rubrique « Self-assessment » appartient au **supplément ARTS** (manuel p.200-203), imprimé en rose et **réservé à la filière Lettres**. Le tronc commun s'arrête à la Section Five (manuel p.199) et reprend au Self-assessment (manuel p.204).

---

#### Supplément ARTS (filière Lettres uniquement) — manuel p.200-203 · guide p.74-75

##### ARTS Section One : READING A POEM (manuel p.200-201 · guide p.74)

**Scope and sequence (guide p.74)** — verbatim :

- **Skills/subskills and strategies**
  - *Speaking*
    - describe a particular event
  - *Reading*
    - appreciate the sound and rhythm of a poem
    - skim for gist
    - scan for details
    - guess meaning of words from context
    - identify essential ideas in a poem
    - react to poem
  - *Draw a picture to illustrate meaning*
- **Vocabulary** : snowstorm – sandstorm – dust – maple – frost – flour – stand still – sunlight - woodfire
- **Grammar** : If + simple past
- **Functions** : describing a natural event (disaster) ; making comparisons
- *(pas de rubrique Pronunciation ni Homework)*

###### BEFORE YOU READ (manuel p.200)

1. « Have you ever seen a snowstorm live, in a film or in a photograph ? Describe it very briefly. If you have never seen a snowstorm, describe what you think it might be like. »
2. « Compare the snowstorm that you have described with a sandstorm, tidal wave, hurricane or other violent natural event that you have witnessed. »

###### AS YOU READ — le poème (manuel p.200-201)

**Consigne verbatim** : « Read the poem below aloud, slowly, stanza by stanza, just to appreciate the sound and rhythm of it. Underline the words that are unfamiliar to you. »

> ### ⚠️ Œuvre sous droits — non reproduite (règle R-2)
>
> Le poème n'est **pas** transcrit ici, ni en tout ni en partie. Description non reproductive uniquement.

**Fiche descriptive du poème**

| Champ | Valeur |
| --- | --- |
| Titre | « Snowing, Sometimes » *(le manuel écrit « Snowing, Sometimes » p.200 et « Snowing, sometimes » au guide p.74)* |
| Auteur | Stanley Plumly (signature imprimée en fin de poème, manuel p.201) |
| Genre | Poème lyrique en vers libres, non rimés, non ponctués de façon régulière |
| Structure | **4 strophes numérotées I, II, III, IV** — respectivement **10, 11, 11 et 11 vers**, soit **43 vers** au total |
| Voix / adresse | Écrit à la **2e personne (« you »)**, qui renvoie à un enfant, « the boy at the window » nommé à la strophe IV |
| Sujet | La neige, jamais nommée dans le corps du poème : elle est désignée du seul pronom « it » (le titre est le seul endroit où le mot est employé — c'est l'objet de la question 3) |
| Progression spatiale | Str. I : la neige **dehors**, chassée par le vent d'un bord de route à l'autre, sur une surface dure et blanche, contre un érable aux dix feuilles mortes. Str. II : la neige **passe à travers** les joints et les défauts de la vitre, jusque **dans la pièce**. Str. III : le dormeur imagine la neige le **recouvrant** et emplissant les objets de la chambre (la tasse sur la commode, les poches du pantalon accroché à la chaise). Str. IV : rien ne l'arrête — quatre forces opposées échouent à la contenir, et la neige gagne les recoins les plus reculés. |
| Réseau d'images | La neige comparée à la poussière, au givre, à la lumière, à la glace ; « an elegance », « crystalline » ; le froid qui se referme comme sur l'eau ; le blanc comparé à la farine |
| Procédés sonores | Allitérations en **/s/** et **/w/** répétées tout au long du poème (objet de la question 10) ; anaphore de « Not… » ouvrant chaque phrase de la strophe IV (question 7) ; reprise en refrain de la formule « keep it out » aux strophes I et III |
| Point de langue travaillé | **If + simple past** (guide p.74) — les propositions hypothétiques en « If you… » ouvrant la strophe III |

**Notice sur le poète (guide p.74) — paratexte du guide, transcrit verbatim** :

> The poet : Stanley Plumly was born on May 23, 1939 in Barnesville, Ohio. He went to college and University and became an English professor and much-honoured poet. He has taught at many Universities throughout USA. He is now a professor of English at Maryland University. Some of his collections of poetry are : The Marriage in the Trees (1997), Boy on the step (1989), Summer Celestial (1983), Giraffe (1973)

**Notice sur le poème (guide p.74) — paraphrase (la note du guide cite un fragment du poème, non repris ici)** : le guide indique que le poème saisit une scène de l'enfance du poète, lorsque la neige emplit l'air au-dehors et menace la sécurité de la maison ; il montre le garçon à la fenêtre et sa perception de la neige avançant de façon ordonnée depuis l'autre côté de la route, de plus en plus près de la maison, puis à l'intérieur, jusque dans les recoins les plus reculés de la pièce.

**Consigne du guide sur les questions (p.74) — verbatim** :

> The comprehension questions : Have your students answer the comprehension questions either orally or in writing. They should use evidence carefully chosen from the poem - specific lines or words that prove their points.

###### Les 10 questions de compréhension (manuel p.201) — verbatim

1. What is the poem about ?
2. Who does the second person (you) in the poem refer to ?
3. Nowhere in the poem, except in the title, does the boy call snow by its name. Rather, he keeps referring to snow as "it". What is the effect of this ?
4. In stanza I, where is the snow in relation to the boy ? What does the snow come in contact with outside ?
5. In stanza II, where is the snow now ? What effect, do you think, does the direction of the snow's movement have on the boy ?
6. In stanza III, in what places in the room does the boy expect to find snow ? Does he feel threatened by it ? Why / Why not ?
7. All the sentences in stanza IV begin with "Not..". To what word(s) or idea in stanza III do they refer ?
8. In stanza IV, the snow defeats four opposing forces. What are they ?
9. Why does the boy feel safe despite the menacing snow ?
10. The sounds of "s" and "w" are repeated many times in the poem. What do they make in the reader's ears ?

**Corrigé** : **aucun corrigé imprimé** pour ces 10 questions — le guide se contente de la consigne méthodologique ci-dessus.

###### AFTER YOU READ (manuel p.201)

**Verbatim** : « The imagery in the poem allows you to imagine that you can see the scene the poet describes. Try to draw a picture to illustrate the poem. »

##### ARTS Section Two : MORE PRACTICE ACTIVITIES (manuel p.202-203 · guide p.75)

> Le guide ne donne **pas** de tableau « Scope and sequence » pour cette section : seulement une ligne Vocabulary suivie des corrigés (guide p.75).

**Vocabulary (guide p.75)** : asphalt, bulldozer, concrete, creep, debris, emit, freeway, garbage dump, greed, ingenuity, marvel(v), tornado, twister, typhoon, wilderness

###### ARTS Activity 1 — appariement pour reconstituer un paragraphe (manuel p.202)

**Énoncé verbatim** : « Match sentence parts in column A with their completions in column B to get a coherent paragraph. »

| A. Sentence parts | B. Completions |
| --- | --- |
| 1. First we pollute the wilderness, | a) ceases to exist |
| 2. Then we pollute the wilderness more | b) because we've lost our ability to see it. |
| 3. Soon the wilderness | c) vast and purposeless- |
| 4. In its place is a garbage dump | d) then we pollute our minds with the belief that we've done the right thing. |
| 5. and we think how wonderful we are to have created a place | e) that speaks so well for what we are |

Ligne de réponse imprimée : « Order : 1+…. 2+…..3+…… , 4+…..5+……. »

**Corrigé (guide p.75) — verbatim** : « Activity 1. 1 + d , 2 + b , 3 + a , 4 + c , 5 + e »

###### ARTS Activity 2 — formation des mots (manuel p.202)

**Énoncé verbatim** : « Complete the gaps with the right forms of the words in brackets. »

**Texte à trous verbatim (13 trous)** :

> We praise our cities, our factories, mines, high-rise towers, all the structures that house our economic activities and satisfy our physical needs. We marvel at man's skill and (ingenious)………….. .
> But when we need rest from our labor and release from the stress that (civilize)….. imposes, we don't look at sky-scrapers. We leave the man-made (create)…….., we leave the freeways and go where the natural world (not yet/destroy)…………… We go, if we are (luck) ……. and can afford it, to unmarked deserts, uncut forests, (not pollute) …………shores. We see animals that should remind us that we are not the only creatures that inhabit the earth. We return home refreshed and (strong)…..
> On the Pacific coast there is an area that progress, called development, (rapidly/destroy) …………………….. . Each year condominiums creep (high)…… up the foothills, like a vast institution for the (physical/impair) ………………………… . Bulldozers eat the (remain) …………..fields. What was once green is concrete and asphalt. This fact is a warning for Utah, which is now (threat)……….. by exploitation and greed, and by shortsighted (ignore) ………..of what man needs to survive.

**Corrigé (guide p.75) — verbatim** :

> Activity 2. ingenuity, civilization, creations, has not yet been destroyed, lucky, unpolluted, strengthened, is rapidly destroying, higher, physically impaired, remaining, threatened, ignorance

Appariement trou par trou (dans l'ordre du texte) : (ingenious) = **ingenuity** · (civilize) = **civilization** · (create) = **creations** · (not yet/destroy) = **has not yet been destroyed** · (luck) = **lucky** · (not pollute) = **unpolluted** · (strong) = **strengthened** · (rapidly/destroy) = **is rapidly destroying** · (high) = **higher** · (physical/impair) = **physically impaired** · (remain) = **remaining** · (threat) = **threatened** · (ignore) = **ignorance**.

> L'exercice mêle dérivation (nom ↔ adjectif ↔ adverbe), préfixation négative (*un-*), comparatif (*higher*) et voix passive à plusieurs temps (*has not yet been destroyed*, *is rapidly destroying* à l'actif progressif, *threatened*).

###### ARTS Activity 3 — ponctuation et majuscules (manuel p.202)

**Énoncé verbatim** : « Punctuate and capitalize where necessary. »

**A (verbatim, sans ponctuation ni majuscules dans la source)** :

> tornadoes or twisters can occur in almost every part of the world however the greatest number and some of the most severe occur in kansas missouri and oklahoma this part of the united states is nicknamed tornado alley

**B (verbatim)** :

> tropical storms known as typhoons in the pacific and hurricanes in the atlantic claim more lives each year than any other storm.

**Corrigé (guide p.75) — verbatim** :

> A. Tornadoes or twisters can occur in almost every part of the world ; however, the greatest number and some of the most severe occur in Kansas, Missouri, and Oklahoma. This part of the United States is nicknamed : "Tornado Alley".
> B. Tropical storms, known as typhoons in the Pacific and hurricanes in the Atlantic, claim more lives each year than any other storm.

###### ARTS Activity 4 — remise en ordre d'un paragraphe (manuel p.203)

**Énoncé verbatim** : « Reorder the following sentences into an organized paragraph made up of a topic sentence and supporting details and examples. »

Les 7 segments, dans l'ordre imprimé (deux numéros sont déjà donnés) :

| Case | Segment |
| --- | --- |
| ( ) | The colors are intensified by the smoke and ash of an erupting volcano. |
| ( ) | Volcanic eruptions can have an effect on world climate. |
| ( ) | can emit huge quantities of gases and fine debris into the atmosphere causing short-term effects on the weather |
| **( 5 )** | caused average temperatures worldwide to fall by 1°F (0.6°C) over a 12-month period. |
| **( 2 )** | Erupting volcanoes, although not a frequent occurrence, |
| ( ) | For instance, the eruption in June 1991 of Mount Pinaturbo [sic — pour « Pinatubo »] in the Philippines |
| ( ) | Another effect is the orange and red color of a sunrise or sunset. |

**Corrigé (guide p.75) — verbatim** : « Activity 4. (7),(1),(3),(5),(2),(4),(6) »

Le corrigé donne, **dans l'ordre d'impression des 7 segments**, le rang de chacun dans le paragraphe reconstitué. Les rangs 5 et 2 déjà imprimés au manuel concordent. Paragraphe reconstitué :

1. Volcanic eruptions can have an effect on world climate. *(topic sentence)*
2. Erupting volcanoes, although not a frequent occurrence,
3. can emit huge quantities of gases and fine debris into the atmosphere causing short-term effects on the weather
4. For instance, the eruption in June 1991 of Mount Pinaturbo [sic] in the Philippines
5. caused average temperatures worldwide to fall by 1°F (0.6°C) over a 12-month period.
6. Another effect is the orange and red color of a sunrise or sunset.
7. The colors are intensified by the smoke and ash of an erupting volcano.

**Note finale du guide (p.75) — verbatim** : « Note : you may design some comprehension questions to make the activities more challenging. »

---

#### Rubriques de fin de module (tronc commun)

##### SELF-ASSESSMENT (manuel p.204)

**A. Énoncé verbatim** : « What progress do you feel you have made in English in this module ? Put a tick (√) in the box that applies to you. »

Grille à 3 colonnes — **YES / A LITTLE / NO** — et 14 items, verbatim :

1. I've used what I already know to learn more English
2. I can read a text and answer the questions correctly
3. I can listen to a text and answer the questions correctly
4. I've learnt how to converse in English
5. I am using the grammatical structures I've learnt
6. I understand grammar but I cannot use the structures correctly
7. I can remember the words I've come across
8. I recognize the words but I cannot use them
9. I've learnt how to write in English
10. The writing activities are difficult
11. I've shared ideas with my classmates and my teacher
12. My pronunciation has improved
13. I've learnt how to conduct a mini-project
14. My English has improved

**B. Énoncé verbatim** : « What did you like most in this module ? Tick the answer(s) that apply(ies) to you. »
- The topics
- The activities
- The projects
- Listening to the cassette
- Acting out situations
- The writing activities
- The Reading skills
- The grammar exercises
- The vocabulary exercises
- Working in groups

**C. Énoncé verbatim** : « Circle the alternative that applies to you : I still need to work on : Reading / Listening / Speaking / Writing / Vocabulary / Grammar »

##### Fun page (manuel p.205)

Page de détente, 4 items séparés par des motifs décoratifs (points en triangle). Transcription verbatim :

1. « It rains twice a year in London : August through April and May through July. »
2. « – What did the dad volcano say to the mom volcano ? – Do you lava me like I lava you ? » *(jeu de mots lava / love)*
3. Histoire de l'Indien météorologue :
   > A film crew was on location deep in the desert. One day an old Indian went up to the director and said, "Tomorrow, rain." The next day it rained.
   > A week later, the Indian went up to the director and said, "Tomorrow, storm." The next day there was a hailstorm.
   > "This Indian is incredible," said the director. He told his secretary to hire the Indian to predict the weather. However, after several successful predictions, The old Indian didn't show up for two weeks. Finally, the director sent for him. "I have to shoot a big scene tomorrow," said the director, "and I'm depending on you. What will the weather be like ?" The Indian shrugged his shoulders. "Don't know," he said. "Radio broke."
4. « – How many people died in the Asian Tsunami ? – Not enough. »

> ⚠️ **Alerte éditoriale (non un défaut de transcription)** : l'item 4 de la Fun page est une « blague » sur le nombre de morts du tsunami asiatique de 2004 — dans un module dont le texte-support central est le témoignage d'une mère ayant perdu sa fille dans ce même tsunami. L'item est bien imprimé au manuel officiel p.205 et transcrit ici par fidélité, mais il est **à proscrire de toute génération de contenu** (quiz, exercice, cours). L'item 3 repose par ailleurs sur un stéréotype ethnique daté. Signalé pour la suite de la chaîne.

##### VOCABULARY COVERED IN MODULE 6 (manuel p.206) — liste intégrale

> La page est imprimée en **4 colonnes**, et la couche texte les entrelace ligne à ligne. L'ordre de lecture restitué ci-dessous a été **reconstruit colonne par colonne**, puis **contre-vérifié** avec les listes « Vocabulary » du guide : la correspondance est exacte pour la Section One (33 items du guide = les 33 items distincts du manuel), pour la Section Five (18 = 18) et pour l'Arts Section Two (15 = 15). La reconstruction est donc validée.

**Common core**

*Section one* (34 entrées imprimées, dont un doublon) :
abrupt, alert, ash, catastrophe, dirty, drought, earthquake, ecology, eruption, expel, extinction, ferociously, flood, hole, lava, motto, pollution, predict, prevent, rate, **rate** [sic — le mot « rate » est imprimé **deux fois de suite** dans la colonne], rupture, seism [sic], shallow, species, steam, storm, stumble, threat, tidal, tsunami, vent, volcano, wave

*Section two* (20 entrées) :
book (v), corpse, dreadful, evacuate, fisherman, glimpse, honeymoon, livelihood, mourn (er), orphaned, partner, postpone, pound (v), pray, rotting, smash, spotlessly, trap, turmoil, waves

*Section three* (8 entrées) :
accelerate, compelling, finding, impact (v), melting, remove, simulate, solar

*Section four* (3 entrées) :
brush, light bulb, tap

*Section five* (18 entrées) :
bitterly, chaos, collapse, crack, current, disintegrate, engulf, float, grab, grasp, looters, perish, pin(v), scream, shiver, sweep, wipe, yell

**Arts Supplement**

*Section one* (12 entrées) :
drift, dust, frost, hang, ice, maple, sandstorm, seam, shine, snowstorm, stand still, sweep

*Section two* (15 entrées) :
asphalt, bulldozer, concrete, creep, debris, emit, freeway, garbage dump, greed, ingenuity, marvel (v), tornado, twister, typhoon, wilderness

> Total : **110 entrées imprimées**, dont 108 lemmes distincts (« rate » compte double ; « sweep » figure à la fois en Section five et en Arts Section one ; « wave » en Section one et « waves » en Section two).

**Écarts entre la liste du manuel (p.206) et les listes « Vocabulary » du guide (par section)** — utile pour arbitrer ce qui est réellement au programme :

| Section | Dans le guide mais **absent** de la liste du manuel | Dans le manuel mais **absent** de la liste du guide |
| --- | --- | --- |
| One | *(aucun)* | *(aucun — hors le doublon « rate »)* |
| Two | sorrowful, grief, honetmoon [sic], pospone [sic] *(les deux dernières sont les coquilles du guide pour honeymoon / postpone, présentes au manuel sous leur graphie correcte)* | book (v), evacuate, fisherman, glimpse, livelihood, orphaned, pound (v), pray, rotting, spotlessly, trap, turmoil |
| Three | release, findings, implications, accelerated, adequate, global warming, renewable energy | accelerate, compelling, finding, impact (v), remove |
| Four | switch off, spill, tanker, trash | *(aucun)* |
| Five | *(aucun)* | *(aucun)* |
| Arts One | flour, sunlight, woodfire | drift, hang, ice, seam, shine, sweep |
| Arts Two | *(aucun)* | *(aucun)* |

---

#### Tapescript du module

**Source** : guide 641303 p.86, en-tête « Module six : Section two. Listening ». Témoignage de presse à la première personne (Sandra Bell, mère de Natalie), en **4 parties**, attribué en fin de texte à **DAILY MIRROR (NOVEMBER 2005)**. Texte non littéraire : transcrit intégralement et verbatim.

##### PART 1

> It's almost exactly 10 years since Natalie and Andy met at a swimming club. It was clear from the start they were meant for each other. Their wedding was on the 22nd of May. It was one of the happiest days of my life. Natalie and Andy postponed their honeymoon until Christmas when Andy's design company would be quiet. Nat and Andy had planned to honeymoon in New Zealand but at the last minute changed their minds and booked a beachside bungalow at the Phi Phi Princess Hotel Resort in Thailand.

##### PART 2

> Nat phoned on Christmas day mid-morning. She sounded so relaxed and was having a great time. She told me about the boat trip they had been on the day before, the people they met and the meals they had had. The next morning, my partner, Ted was up at 7am and put the TV on. The news was all about a tsunami hitting the area where Nat and Andy were staying. I had never heard of a tsunami before. As I watched, the news got worst [sic — le manuel p.191 imprime « worse »] by the minute. I dialled Nat's mobile. My heart pounded as I prayed for her to answer. But she didn't pick up. I spent the morning ringing Nat's phone, the foreign office, the hotel, searching the internet and going round in circles.

##### PART 3

> Finally, I managed to get to the Princess Hotel Website. It said there was an extensive loss of life and damage to the building. My heart sank but we kept trying Nat's phone and everywhere we could think of. I refused to think the worst. No news ; Nat would have called if she was alive. I couldn't stop searching the screen in case I glimpsed Nat and Andy. Ted said gently I should prepare myself for the worst. Andy's body was found. They used his wedding ring inscription to identify him. I felt dreadful and I knew if Andy was dead, Nat must have been too.

##### PART 4

> Ted, my daughter Lauren and I flew to Phi Phi. Nothing prepared me for the sights I saw as we approached the island. Total devastation, a smell of rotting corpses. I saw the smashed strip of land of Nat's bungalow ; It had been hit both sides by waves and I realised there was little chance they could have survived. I just hoped they died quickly. Phi Phi was a living hell, but I didn't want to leave. We returned and went to Nat and Andy's flat. The Christmas tree was still up, wedding pictures were everywhere and, typically it was spotlessly tidy. They found Natalie's body on the 3rd of September. We wanted to do something good for them and so have set up a fund to raise money to help children orphaned and schools devastated by the tsunami. We also wanted to help the fishermen and hoped to buy several boats to help them get back on their feet again. Nat and Andy lived for each other and died with each other.

> **DAILY MIRROR (NOVEMBER 2005)**

**Faits utiles extraits du tapescript pour la génération** (repères, pas des corrigés officiels) : le couple = **Natalie (« Nat ») et Andy** ; rencontre dans un club de natation ~10 ans plus tôt ; mariage le **22 mai** ; lune de miel **reportée à Noël** (l'entreprise de design d'Andy était calme à cette période) ; destination initialement prévue **la Nouvelle-Zélande**, changée au dernier moment pour un bungalow en bord de plage au **Phi Phi Princess Hotel Resort, Thaïlande** ; l'incident = **le tsunami** ; le partenaire de Sandra = **Ted** ; sa seconde fille = **Lauren** ; corps de Natalie retrouvé le **3 septembre** ; actions décidées = **un fonds** pour les enfants orphelins et les écoles dévastées, et **l'achat de bateaux** pour les pêcheurs.

---

#### Incertitudes (module 6)

**A. Supports en image, absents de la couche texte** — récapitulatif complet (information critique pour la suite : ces activités ne sont pas générables telles quelles) :

| Page | Support manquant | Activité concernée |
| --- | --- | --- |
| manuel p.184 | 5 photos numérotées 1 à 5 (contenu inconnu) | Section One, Activity 1.A — aide au spidergram |
| manuel p.185 | La figure du spidergram (bulle centrale « Threats to the environment » + branches à remplir) ; le nombre de branches est indéterminable | Section One, Activity 1.A |
| manuel p.186 | 5 photos numérotées 1 à 5 (contenu inconnu ; le corrigé du guide les rattache à drought/flood/tsunami/volcano/earthquake) | Section One, Activity 2 |
| manuel p.187 | 6 images étiquetées A à F (contenu inconnu) | Section One, Activity 3 — appariement image ↔ gros titre |
| manuel p.189 | Photo(s) non identifiée(s) : l'Activity 2 renvoie à « the pictures », introuvables dans la couche texte (nombre et contenu inconnus) | Section Two, Activity 2 — prédiction |

**B. Coquilles de la source relevées et marquées `[sic]`**
- manuel p.184 : en-tête « **Session** one » au lieu de « Section One » (p.185-188 corrigent d'elles-mêmes).
- manuel p.185, définition 4 : « the **richter** scale » (minuscule) et parenthèse ouvrante jamais refermée « ( after Charles F Richter (1900-85) U.S. seismologist. ».
- manuel p.188 : « a **compaign** » pour « campaign ».
- manuel p.192 : « (the people / the incident / … leading up to it. » — parenthèse jamais refermée.
- manuel p.196 : « the following **quizz** ».
- manuel p.196-197 : espaces manquantes — « 20litres », « 30litres », « 830,000deaths », « 220.000tons », « 500gr ».
- manuel p.197 : « better for **evironment** » ; « (see **session** 1) » ; grille de score « 4**--**6 » (double tiret).
- manuel p.203 : « Mount **Pinaturbo** » pour « Pinatubo ».
- manuel p.206 : « **seism** » ; « **rate** » imprimé **deux fois** dans la colonne Section one.
- guide p.70 : « **honetmoon** », « **pospone** » dans la ligne Vocabulary ; item de compétence fusionné sans séparateur (« identify logical relations in a text Imitate appropriate intonation patterns »).
- guide p.73 : corrigé « **H**ad already been engulfed » — majuscule initiale sur une forme en milieu de phrase.

**C. Écarts internes entre manuel et guide (non tranchés — la source se contredit)**
1. **« worse » / « worst »** : l'extrait de prononciation du manuel p.191 imprime « the news got **worse** by the minute » ; le tapescript du guide p.86 (PART 2) imprime « **worst** ». Les deux graphies sont conservées telles quelles à leur emplacement respectif.
2. **« Nat and her husband » / « Nat and Andy »** : la phrase à reformuler du manuel p.190 (C.4) cite « I couldn't stop searching the screen in case I glimpsed **Nat and her husband** » ; le tapescript p.86 dit « **Nat and Andy** ».
3. **« sign up the Kyoto Protocol » / « sign up to »** : le texte de lecture (manuel p.193, §2) omet « to » ; l'encadré grammaire qui reprend la phrase (manuel p.194) l'inclut.
4. **Renvoi de partie erroné** : l'exercice D (manuel p.190) demande d'écouter « PART 3 again » pour décrire **l'île** et **l'appartement de Nat** (D.1) et pour dire ce qui a été décidé pour les **orphelins** et les **pêcheurs** (D.2) — or ces quatre informations figurent toutes en **PART 4** du tapescript, aucune en PART 3. L'exercice est inexécutable tel qu'il est libellé.
5. **Barème du quiz incohérent** (manuel p.196-197) : 7 questions donc 7 points maximum, mais une grille de score étalée sur 1-3 / 4-6 / **7-10**.
6. **« the highest earthquake »** (manuel p.197, exemple de dialogue) : formulation aberrante pour un séisme ; l'intention (« deadliest » ? « strongest » ?) n'est pas déterminable depuis la source. Transcrit tel quel.
7. **Titre du poème** : « Snowing, **S**ometimes » au manuel p.200, « Snowing, **s**ometimes » au guide p.74.

**D. Corrigés absents du guide** (à ne pas confondre avec une lacune de transcription — le guide ne les imprime pas) :
- Section One : Activity 1 (A et B) et Activity 4 — tâches ouvertes, aucun corrigé attendu.
- Section Two : **toutes** les activités d'écoute (Activity 1, Activity 2, A, B.1, B.2, C.1, C.2, C.3, C.4, D.1, D.2, E.1, E.2, E.3) — le guide p.70 ne donne qu'**un seul** corrigé pour toute la section, celui du C test (Homework). Le tapescript p.86 permet de reconstituer les réponses attendues, mais **aucune clé officielle n'existe** : toute réponse fournie en aval sera une inférence, à assumer comme telle.
- Section Three : C (vrai/faux, 5 items), D, F et le « Guess what will cause… » d'ouverture — sans corrigé.
- Section Four : le quiz « how green are you » — le manuel renvoie explicitement au professeur, le guide ne donne rien ; l'Activity 2 (role play) et l'Activity 3 (poster) sont des productions orales libres.
- Section Five : questions 1, 2, 4, 5 et 6 — sans corrigé (seuls le texte à trous de Text B et la question 3 en ont un).
- ARTS Section One : les 10 questions de compréhension du poème — sans corrigé.

**E. Points de reconstitution de mise en page (fiabilité à surveiller)**
- La liste « VOCABULARY COVERED IN MODULE 6 » (manuel p.206) est imprimée en 4 colonnes que la couche texte entrelace ; l'ordre restitué a été reconstruit puis validé par recoupement avec les listes du guide (correspondance exacte sur 3 sections sur 7). L'appartenance de chaque mot à sa section est donc fiable, mais l'ordre alphabétique interne pourrait comporter de légers décalages aux jointures de colonnes.
- Le schéma d'outline de la question 5 (manuel p.199) est imprimé en marge, entrelacé avec la question 6 dans la couche texte ; sa reconstitution (6 lignes, dont la 1re et la 5e pré-remplies) est déduite de l'ordre d'extraction et n'est pas certaine à 100 %.
- L'encadré « Exploring grammar » du manuel p.194 empile « hopes / expects / is sure » dans une accolade devant « that the action will take place in the future ? » ; la mise en forme originale (accolade) n'est pas reproductible en markdown, le sens est préservé.

**F. Droits d'auteur**
- Le poème « Snowing, Sometimes » de **Stanley Plumly** (manuel p.200-201) n'est **pas** reproduit, conformément à la règle R-2 : seuls titre, auteur, genre, structure (4 strophes de 10/11/11/11 vers), thème, réseau d'images, procédés sonores et les 10 questions du manuel figurent dans cette fiche. **Le texte du poème devra être consulté dans le manuel** pour toute génération de contenu s'appuyant sur des vers précis. La notice biographique du guide p.74 est du paratexte et a été transcrite ; la notice du guide sur le poème contenait un fragment cité du poème : elle a été **paraphrasée**, pas transcrite.
- Les textes non littéraires (tapescript Daily Mirror, texte « Global warming is human made », témoignages Kioka Williams et Florencio Libaton, articles à trous) sont transcrits fidèlement.

### Appendice du manuel (p.207–216) — hors modules

L'appendice n'est **pas un chapitre** : c'est le **référentiel de langue** de l'année, à consulter en
permanence. Le guide y renvoie explicitement (p.61 : « have the students see the appended grammar
summary to get help and guidance »). Tout ce qui suit est **verbatim** (règles et exemples imprimés) —
c'est la source normative pour rédiger les encadrés de règle des cours.

#### Grammar summary (p.207–212)

**EXPRESSING RESULT** (p.207) — « We can express result by using **If + present → present** ».
_Eg : If the children stay out after midnight, the parents get angry._
« **Remember :** If clause + main clause **Or** Main clause + if clause ».

**PASSIVES** (p.207) — « **Form : to be + past participle** ».
« It is used when the doer is unknown or when we are more interested in the action than in the doer. »
_Eg: Mike's car was damaged in an accident ( = someone damaged Mike's car in an accident )_
« It is used to describe scientific processes. » _Eg: The water is filtered before it is mixed with the
chemicals_
« **Remember :** The object in the active sentence becomes the subject in a passive one. The verb be
is used in the same tense, with the past participle of the relevant verb. **By** is used only if a
name or a noun giving necessary information is included. »
_Eg: The guide showed him round (active) / He was shown round by the guide (passive)_
« Note the very common passive: **She was born in Zurich** ».

**CAUSATIVE VERBS** (p.207) — « **Make / Let / Have + somebody do something** ».

**WANT** (p.207) — « to want **somebody to do** something » _(Eg: I want you to come back home early.)_ ·
« to want **to do** something » _(Eg : I always want to have the best marks.)_

**WORD BUILDING : …or, …er or …ist ?** (p.207) — exemples imprimés : _donor / actor_ · _Endower /
care-giver_ · _Activist / philanthropist_.

**THE EMPHATIC FORM** (p.208) — « To emphasize a statement we use **DO** or **DID** followed by the
infinitive without to. » _Eg: I do feel compassion for others. / Kirsty did love her sister._

**AFFIXES** (p.208) — préfixes négatifs : `un + able = unable` · `in + active = inactive` ·
`im + possible = impossible` · `mis + understand = misunderstand` · `il + legal = illegal` ·
`dis + appear = disappear` · `ir + reversible = irreversible` · `de + freeze = defreeze`.
Suffixes formant des **adjectifs** : `verb + able` = preventable / affordable · `verb + ive` =
depressive / educative · `verb + ing` = frightening · `verb + ed` = employed · `noun + ful` =
colourful · `noun + y` = funny · `noun + less` = childless. Suffixes formant des **noms** :
`verb + ance` = attendance · `adjective + ness` = sickness · `verb + ment` = employment.

**COMPOUND ADJECTIVES** (p.208) — huit patrons, avec l'exemple imprimé de chacun :
_Adjective-noun_ → long-range weather forecast · _Number-year-old noun_ → an 18-year-old young woman ·
_Adverb-gerund_ → rapidly-growing populations · _Noun-gerund_ → foot-stamping dance ·
_Adverb-past participle_ → well-run philanthropy · _Number-noun_ → two five-pound notes ·
_Noun-adjective_ → odour-free tablets · _Noun-past participle_ → a snow-covered mountain / home-made cake.

**THE PRESENT PERFECT** (p.209) — « **Form : to have + past participle** ». Cinq emplois listés :
actions commencées dans le passé et continuant jusqu'au présent _(they have lived here for ten years)_ ·
faits récents _(he has just gone out)_ · actions à un moment indéfini du passé _(I have read the
instructions but I still can't use the food processor)_ · avec **never** et **always** pour l'habitude
_(he has always kept his promises)_ · actions ayant un résultat présent _(Kelly is upset. She has had
an argument with her mother)_.
« **Remember :** The present perfect can also be used with **up to now, all the year, all my life, so
far, recently, lately, already, ever, never, yet, for, since.** »

**THE SIMPLE PAST** (p.209) — formation en `-ed` pour les réguliers. Trois emplois : actions achevées
à un moment défini _(Martin Luther King was assassinated in 1968)_ · narration _(he rushed to the sea,
climbed on top of a huge rock and called the siren)_ · habitudes passées _(Charlot always wore baggy
trousers and a short jacket)_.
« **Remember :** The simple past can have a **present or future meaning** when used after **if, as if,
as though, it's (high) time, would rather, wish, suppose.** » _Eg : He talks as if he knew everything.
/ I'd rather you came a bit earlier._

**THE PAST PERFECT** (p.209) — antériorité _(I telephoned Jane at 4.30, but she had already left)_ ;
emploi après **when, as soon as, before, after, for, since**, « **But if two actions are close in time,
or closely connected, the past perfect is not usually used** » _(When he arrived at the hotel, he asked
for a room)_ ; après **if** pour l'irréel du passé _(If I had known you were coming, I would have met
you at the station)_. **Past Perfect Continuous** : action continue ou répétée antérieure à une autre
_(I was very angry when the bus finally came because I had been waiting a long time for it)_.

**CAN / MAY** (p.210) — permission au présent ou au futur _(I can take a day off whenever I want / You
may come if you like)_. **COULD / MIGHT** — possibilité future _(He might tell his wife he's a dustman
/ Where's Tom? Could he be in the library?)_. « **Remember :** Can, could, may and might are **always
used with the infinitive without to**. »

**RELATIVE PRONOUNS** (p.210) — **who** (personne) · **which / that** (chose) · **what** = « the thing
that » _(I told him what happened. / What matters most is how motivated you are.)_ · **whose** (à la
place de his/her/their) · **whom** (objet, formel ; _who_ plus courant à l'oral) · **where** (lieu).
« If who, which or that is the **subject** of the relative clause, the pronoun is important and must be
kept, but if it is the **object**, the pronoun may be left out. » _Eg : He's the only boy who invited
me to play tennis. / Have you found the book (which / that) you lost ?_

**RELATIVE CLAUSES** (p.210) — **restrictives** : information essentielle _(The noise that she made
woke me up)_ ; « **that** is often used instead of **which** after superlatives, all, everything,
nothing, any(thing), some(thing), none, little, few, much and only » _(That's the worst play that has
ever been performed. / The only thing that matters is to tell the truth.)_.
⚠️ Phrase suivante, **telle qu'imprimée** : « If it is the **subject**, the restrictive pronoun is
often left out. » _Eg : He did everything he could do to help._ — l'exemple montre une omission en
position **objet**, en contradiction avec le mot « subject » et avec la règle donnée juste au-dessus au
§ RELATIVE PRONOUNS. **Coquille de la source** [sic], à ne pas propager (voir §6).
**Non restrictives** : information supprimable sans changer le sens, « the restrictive clause [sic] is
placed after a coma [sic] » _(Ann, whose children are now grown up, is looking for a job. / I gave the
girl a piece of cake, which she ate immediately.)_

**MUST** (p.211) — obligation ou conseil emphatique _(Father: "You must revise more for the exam" /
Doctor: "You must lose weight. Practise sport.")_ ; déduction au présent **ou au passé** _(I wonder why
Ali hasn't come to school today. He must be ill. / Everything is wet this morning. It must have rained
last night.)_ — c'est l'entrée `must have + past participle` travaillée au module Six.

**SHOULD** (p.211) — conseil / recommandation _(You should read this book. It's very interesting.)_
**SHOULD HAVE** (p.211) — « an unfulfilled obligation or a sensible action that didn't happen »
_(You should have told him that the paint on the walls was still wet.)_

**COMPARISONS** (p.211) — tableau imprimé :

| Comparative                                | Superlative                             |
| ------------------------------------------ | --------------------------------------- |
| short adjective + **er** than              | **the** + short adjective + **est**     |
| **more / less** + long adjective **than**  | **the most / the least** + long adjective |

Exceptions imprimées : good → better → the best · bad → worse → the worst · far → farther/further →
the farthest/the furthest · little → less → the least · much/many → more → the most.
« **Important :** far, much, many more, a little, a lot can be used before comparatives as
**modifiers**. » _Eg: far more intelligent / a bit fatter / many more books / much more attractive_
(le guide ajoute, p.60 : « **"very" cannot be used with comparatives. Instead, we use "much" or
"far"** »).

**COMPARISON OF SCALE** (p.211) — « **Number of times + as + adjective / adverb + as** »
_(This house is three times as expensive as that one.)_ · « **Number of times + as + many / much +
as** » _(In some countries women earn half as much as men although they work twice as much.)_

**NEEDN'T / NEED TO** (p.211) — « **Needn't** is used to express **absence of necessity** in the
present or the past » _(You needn't send the package by air. You can send it by train. / You needn't
have made such a big cake. Only a few guests came to the party.)_ · « **Need to** expresses necessity.
It is **conjugated as an ordinary verb**. » _(She needs to review the irregular verbs.)_

**WILL vs BE GOING TO** (p.212) — **Will + infinitif sans to** : actions habituelles _(We will come
back here next year as usual)_ · promesse _(I'll be back home before dark)_ · offre _(If you don't
understand the exercise, I'll explain it to you)_ · attente _(I think summer will be extremely hot this
year)_. **Be going to** : plan préalable _(I'm going to spend the week-end by the sea)_ · prédiction
_(The car is making strange noises. It's going to break down)_ · ordres et refus _(You're going to help
with the house chores whether you like it or not)_ · état permanent _(Their new house is going to be
very beautiful)_.

**REPORTING QUESTIONS** (p.212) — « We start an indirect question with a verb like **ask, inquire,
wonder, want to know**. » Si la question directe commence par un mot interrogatif, ce mot est répété
_("What do you want?" → He asked them what they wanted.)_ ; sinon on emploie **if** ou **whether**
_("Is anyone here?" → He wanted to know if anyone was there.)_.
« **Remember :** When the reporting verb is in the past we change the tenses as follows. »

| Direct Questions   | Indirect Questions       |
| ------------------ | ------------------------ |
| Simple present     | Simple Past              |
| Present Continuous | Past Continuous          |
| Present Perfect    | Past Perfect             |
| Past Progressive   | Past Perfect Progressive |
| Future             | Conditional.             |

#### Irregular verbs (p.213–215)

Liste officielle en trois colonnes _Infinitive / Simple Past / Past Participle_, de **arise** à
**write**, dans l'ordre alphabétique. Elle comporte des formes doubles explicitement imprimées :
_bereave → bereaved/bereft_, _burn → burnt/burned_, _smell → smelt/smelled_, ainsi que des entrées peu
courantes utiles aux textes du manuel : _bereave, cling, creep, dwell*, strive, unwind, undergo,
weave, withdraw_. C'est la **liste de référence à laquelle le manuel renvoie** pour tous les exercices
de temps du passé.
_(La liste n'est pas recopiée intégralement ici : elle est stable, non spécifique au programme, et
directement relisible à ces trois pages. Ce qui compte pour la génération — son existence, son étendue
alphabétique et les doubles formes admises — est consigné.)_

#### Phonetic symbols (p.216)

Table de symboles phonétiques organisée en : **Short Vowel Sounds** (mots-clés imprimés : _Red, box,
bus, cat, river, book, six_) · **Long vowel sounds** (_Three, moon, girl, car, more_) · **Diphthongs**
(_here, eight, poor, boy, throw, there, my, now_) · **Triphthongs** (_fire, flower_) · **Consonants**
(_pen, ten, teacher, kick · ball, doll, angel, god · fine, three, stop, push · voice, this, zero,
measure · monday [sic, minuscule], night, king, hello · listen, read, white, yes_).

⚠️ **Les symboles API eux-mêmes ne sont pas fiables dans l'extraction** (la police du PDF les rend en
caractères de substitution : `^`, `ae`, `Ω`, `1`, `:e`, `:c`…). **Seuls les mots-clés ci-dessus sont
transcrits avec certitude** — ils suffisent à ancrer les activités de prononciation du manuel (silent
letters, consonant/vowel sounds, stress patterns, rhythm and intonation), qui portent toutes sur des
**mots**, jamais sur la lecture de symboles. Toute génération devant afficher un symbole API doit le
prendre à une source de référence, pas à cette transcription (voir §6).

---

## 3. Notes pédagogiques / méthode

### 3.1 Ce que le guide impose à la démarche

- **Inductif d'abord, règle ensuite.** La grammaire n'est jamais donnée avant d'avoir été rencontrée :
  les tableaux « Exploring grammar » du manuel font **observer** deux colonnes d'exemples puis
  demandent « What is the tense used ? », « Form ? », « Use ? ». Le Grammar summary de l'appendice
  n'arrive qu'en fin d'ouvrage, en référence. **Conséquence pour la génération** : un cours de ce
  programme présente la règle **après** un corpus d'exemples, pas avant.
- **Les quatre compétences sont à parité** et s'intègrent : une section « Reading » contient presque
  toujours du Speaking et du Writing dans son étape « After you read ». Le découpage en sections est
  un découpage de **dominante**, pas d'exclusivité.
- **Le lexique se travaille en contexte**, jamais en liste isolée — même si le manuel publie une liste
  récapitulative en fin de module (« VOCABULARY COVERED IN MODULE N », séparée `Common core:` /
  `Arts:`), elle est un **bilan**, pas un point de départ.
- **Le corrigé n'est pas toujours unique.** Le guide le dit explicitement à plusieurs reprises, par
  exemple (p.20) : « It's clear that the correct answer is that picture 2 depicts the lady in the
  text, **but what matters is the justification given** and the use of the appropriate vocabulary » ;
  ou (p.52) : « Accept the different attitudes of the students as **there are no right or wrong
  answers**. » **Conséquence directe pour le LOT B** : ces activités-là ne se convertissent **pas** en
  QCM à clé unique — voir §3.3.

### 3.2 Erreurs et difficultés que le guide anticipe

- Difficulté à retrouver des mots à l'écoute ⇒ « provide the beginning of each word to facilitate the
  task » (p.11).
- Mots rares à ne pas surinvestir : « "sloppy" is not a frequent word, so **don't make much fuss about
  it** » (p.14).
- Expressions idiomatiques à faire expliciter parce qu'elles bloquent la compréhension : _see eye to
  eye (with)_ = « agree entirely (with) » (p.14) ; _jump down someone's throat_ = « to disagree with,
  criticize, or scold overhastily » (p.17) ; _get in someone's hair_, _for heaven's sake_, _I can't
  help it_ (p.15).
- Les **phrasal verbs** sont désignés comme un point dur structurel : « Phrasal verbs are one of the
  major important features of the English language. Raise the students' awareness of the form and the
  functional use of phrasal verbs. **In the following modules, present any phrasal verb that is new to
  the students.** » (p.26)
- Sur les comparatifs : « **"very" cannot be used with comparatives.** Instead, we use "much" or
  "far" » (p.60) — erreur type explicitement nommée.
- Fluidité avant correction dans les activités orales : « Let the students interact and talk fluently
  **without worrying too much about mistakes** » (p.15) ; « Encourage the students to retell the
  stories and **don't care much about the language mistakes** » (p.49).

### 3.3 Ce qui, dans ce programme, ne se teste pas en QCM

À poser explicitement avant le LOT B, pour éviter de dénaturer le programme :

- **Les activités de production orale** (Section Four de chaque module : jeux de rôle, interviews,
  débats, discours, présentations de posters) et **les mini-projets**. Leur **notion** (fonctions de
  langue, lexique, structures, traits du genre) est testable ; **la production** ne l'est pas.
- **Les activités d'écriture longue** (Section Five : lettre de réclamation, article, rapport,
  narration, e-mail, lettre formelle). Idem : on teste le **plan**, les **connecteurs**, le
  **registre**, les **traits du genre** — pas la copie.
- **Les activités à réponse ouverte assumée** que le guide signale (§3.1).
- **Les activités de prononciation** qui exigent l'audio (la cassette n'est pas au corpus). Ce qui
  reste testable sans audio : les **silent letters**, l'identification de la syllabe accentuée sur des
  mots écrits, les paires de sons — tout ce que le manuel fait travailler **sur des mots imprimés**.
- **Les Fun pages** (une par module) : blagues et jeux de mots, hors compétence évaluée.

C'est un cadrage, pas une réduction : les six modules gardent chacun un tronc parfaitement testable —
lexique en contexte, grammaire inductive puis appliquée, compréhension écrite, compréhension orale
**par les tapescripts**, traits de genre, et les deux modules de consolidation qui sont, eux,
intégralement constitués d'exercices à clé.

### 3.4 La progression grammaticale de l'année (synthèse des six modules)

Ordre d'apparition, tel que les Book map et les « Scope and sequence » le donnent :

| module | grammaire introduite ou recyclée                                                                                             |
| ------ | ----------------------------------------------------------------------------------------------------------------------------- |
| Review | discours rapporté, `let/make + base form`, `used to`, comparatifs, present perfect vs simple past, passif, linkers            |
| One    | `If + present → present` (résultat automatique) · `want + object + to-infinitive` · `make / let / have + object + base form` · formation des mots (préfixes/suffixes) |
| Two    | formation des noms d'agent (`-er`, `-or`, `-ist`) · adjectifs composés · `should + perfect infinitive` · **present perfect vs simple past** (le tableau central de l'année) · forme emphatique (`do`/`did`) · `need` · phrasal verbs |
| Three  | superlatifs · prépositions de lieu · **past perfect vs simple past** · `could` / `might` + infinitif nu · voix passive · linkers |
| Four   | préfixes de négation (`il-`, `in-`, `ir-`, `dis-`, `im-`, `mis-`) · adjectifs composés · modaux (`should`, `may`, `can`, `can't`) · formation des mots |
| Five   | comparatifs modifiés · comparaison d'échelle (`n times as … as`) · questions indirectes · propositions relatives (restrictives / non restrictives) |
| Six    | `must + perfect infinitive` (déduction dans le passé) · `will` vs `be going to` · temps du passé · formation des mots · (Arts : `if + simple past`) |

Deux points reviennent d'un bout à l'autre de l'année et méritent le plus de poids : le **couple
present perfect / simple past** (module Two, repris en consolidation 1) et la **formation des mots**
(modules One, Two, Four, Six, et les deux consolidations).

---

## 4. Chapitrage retenu (→ alimente les six `manifest/3eme-sec-*.json`)

**Unité retenue : le module**, parce que c'est l'unité que l'ouvrage se donne à lui-même — manuel p.3 :
« It is **divided into 9 modules** : one review module, six learning modules and two consolidation
modules », et guide p.4 : « Each module in the book covers a different theme and thus **may stand
alone** ». Neuf modules ⇒ **neuf chapitres**, dans l'ordre imprimé.

Les plages de pages ci-dessous couvrent le **tronc commun** de chaque module (Sections One→Five +
rubriques de clôture) et **excluent les pages du supplément Arts**, qui n'appartient pas au sujet
partagé (voir « Portée » en tête de fiche).

| #   | slug                                                       | notion (module)                                                | manuel élève (code · pages)      |
| --- | ---------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------- |
| 1   | `01-review-module`                                         | Review Module — reprise et consolidation du niveau 2ème année  | `241303` · p.7-11                |
| 2   | `02-in-time-of-test-family-is-best`                        | Module One — Family life and relationships (rôles familiaux, fossé des générations) | `241303` · p.12-28, 39-41        |
| 3   | `03-we-learn-to-give-share-and-care`                       | Module Two — Attitudes and values / Philanthropy (charité, altruisme, bénévolat, solidarité) | `241303` · p.42-62, 71-73        |
| 4   | `04-consolidation-module-1`                                | Consolidation Module 1 — reprise des modules One et Two        | `241303` · p.74-79               |
| 5   | `05-a-change-is-as-good-as-a-rest`                         | Module Three — Entertainment (voyages, vacances, loisirs, restauration) | `241303` · p.80-95, 104-106      |
| 6   | `06-science-and-technology-a-blessing-or-a-curse`          | Module Four — Science and inventions / Technology (inventions, recherche médicale, génie génétique) | `241303` · p.107-135, 146-148    |
| 7   | `07-consolidation-module-2`                                | Consolidation Module 2 — reprise des modules Three et Four     | `241303` · p.149-152             |
| 8   | `08-education-is-not-filling-a-bucket-but-lighting-a-fire` | Module Five — Education / professional life (enseignement à distance, éducation spécialisée, vie scolaire, monde du travail) | `241303` · p.153-172, 180-182    |
| 9   | `09-nature-any-future-without-it`                          | Module Six — Ecology (enjeux environnementaux, catastrophes naturelles) | `241303` · p.183-199, 204-206    |

**Hors chapitrage, volontairement :**

- **le supplément Arts** (manuel p.29-38 · 63-70 · 96-103 · 136-145 · 173-179 · 200-203) — propre à
  `3eme-sec-lettres`, transcrit dans cette fiche mais non codifié tant qu'il n'est pas généré ; le
  moteur le portera par `gradeSlugs` sur les exercices concernés (loader.ts) ;
- **l'appendice** (p.207-216 : Grammar summary, irregular verbs, phonetic symbols) — référentiel de
  langue transversal, à consommer par tous les chapitres, pas un chapitre ;
- **les Fun pages** (p.40, 71, 105, 147, 181, 205) — divertissement, hors compétence évaluée ;
- **le Book map** (p.4-6) et la Preface (p.3) — paratexte, transcrits en §1.

---

## 5. Sources croisées

- **Guide enseignant** : `641303` — « Activate And Perform — Third Year Secondary Education —
  Teacher's Book », 88 p. Porte le **programme** : « Scope and sequence of specific content and
  skills » par section (Skills/subskills and strategies, Vocabulary, Grammar, Functions,
  Pronunciation, Homework, Mini-project), les « Helpful notes », **tous les corrigés** et **tous les
  tapescripts** (p.76-86). C'est lui qui fixe le scope.
- **Manuel élève** : `241303` — « Activate And Perform … Student's Book », 216 p. Porte le
  **contenu réellement enseigné** : les activités, leurs énoncés et leurs données, les textes-supports,
  les encadrés de règle, les listes lexicales de fin de module, et l'appendice de référence
  (§4 ci-dessus donne les pages par chapitre).
- **Cassette audio** : déclarée par le guide (p.4) comme troisième composant du matériel,
  **absente du corpus**. Sans conséquence bloquante : les tapescripts du guide couvrent l'intégralité
  des passages écoutés (voir « Le matériel déclaré et ce qui manque », en tête de fiche).
- **Taybah** (`taybah/<niveau>.md`) : **aucun fichier pour la 3ème année secondaire** — pas de
  vérification externe de séquençage trimestriel disponible pour ce couple.
- **Divergences guide ↔ manuel signalées** : elles sont toutes de nature **corrigé ↔ énoncé** (le
  guide répond parfois à une version antérieure de l'exercice), jamais de scope. Le guide reste
  l'autorité sur le scope ; là où son corrigé contredit l'énoncé imprimé du manuel, **l'énoncé du
  manuel fait foi pour la tâche** et l'écart est consigné au §6. Aucune divergence de **programme**
  n'a été relevée entre les deux ouvrages.

---

## 6. Incertitudes / à revérifier

Chaque module porte son propre bloc « Incertitudes » en fin de section (§2) — le détail y est, avec
les pages. Ce §6 ne le répète pas : il rassemble ce qui **traverse** la fiche et ce qu'une session
suivante doit savoir avant de générer.

### 6.1 La dette réelle de cette fiche : les supports en image

**C'est la seule limite structurelle.** Les deux PDF ont une couche-texte propre (0 mojibake, 0 OCR),
mais **le texte n'est pas tout le manuel** : une partie des supports est composée d'**images sans
couche texte** — photos légendées, graphiques, cartoons, annonces, formulaires, spidergrams, jeux
d'images à comparer. Ils sont donc **absents de la transcription**, et chaque module les signale
nommément dans son bloc « Incertitudes » avec la mention `⚠️ support en image, absent de la couche
texte` et le numéro de page.

Ce que cela veut dire concrètement :

- **la très grande majorité des activités reste générable** — les énoncés, les banques de mots, les
  tableaux, les textes-supports et **tous les corrigés du guide** sont, eux, dans la couche texte ;
- **les activités adossées à une image ne le sont pas** sans une **passe vision ciblée** sur la page
  concernée. Elles sont identifiées une par une ; il ne s'agit pas de rouvrir le manuel, mais quelques
  pages nommées.
- **Précédent** : la même dette est consignée sur `svt-1ere-sec` (« pdftotext ne rend aucune figure —
  passe vision ciblée exigée à la génération »). Elle ne bloque pas la profondeur de génération, elle
  la borne.

⚠️ **Un point à traiter avant génération, et non un simple manque** : au **module Four, Section Five**
(manuel p.133), la transcription attribue aux Text 1 et Text 2 des champs lexicaux (ail / cholestérol
/ régime pour l'un ; rein / campagne / don pour l'autre) qui sont **déduits des listes de vocabulaire
officielles, et non transcrits d'un texte lu**. C'est la seule inférence de toute la fiche, et son
auteur l'a signalée. **Elle doit être confirmée par vision de la p.133 avant toute génération sur
cette section**, ou retirée. Ne pas la traiter comme une transcription.

### 6.2 Ce que la couche texte ne restitue pas non plus

- **La couleur.** Le book map (manuel p.6) déclare « The items in **pink** are specific to the Arts
  branch » — mais la couleur n'existe pas dans le texte extrait. La frontière tronc commun ↔ Arts a
  donc été établie par un **critère de structure** : le bandeau « **Arts** » qui titre les pages
  concernées, corroboré par le guide (p.4, p.54) et par les listes de vocabulaire de fin de module,
  qui séparent explicitement `Common core:` et `Arts:`. Les trois signaux concordent sur **toutes** les
  frontières retenues au §4. Reste que le rose lui-même n'a pas été vu : si un item **isolé** du tronc
  commun était imprimé en rose, il ne serait pas détecté.
- **Les symboles phonétiques** (manuel p.216) : rendus en caractères de substitution (`^`, `ae`, `Ω`,
  `1`, `:e`…). Seuls les **mots-clés** sont fiables. Toute génération affichant un symbole API doit le
  prendre ailleurs.
- **Les soulignements et la typographie de mise en évidence** dans certains énoncés (le mot souligné
  d'une question « What does the underlined word refer to ? » est parfois indevinable).

### 6.3 Divergences corrigé ↔ énoncé (le guide répond parfois à une autre version)

Aucune divergence de **scope** n'a été trouvée entre le guide et le manuel : le programme est le même
des deux côtés. En revanche, **le corrigé du guide contredit çà et là l'énoncé imprimé du manuel** —
signe que le guide a été figé sur un état antérieur des exercices. Les cas relevés (détail et pages
dans les blocs de module) :

| où                             | l'écart                                                                                       |
| ------------------------------ | --------------------------------------------------------------------------------------------- |
| Consolidation 1, Activity 10   | corrigé « must » sur « You ……… to see a doctor » — l'énoncé appelle `need to`                  |
| Consolidation 1, Activity 13   | le corrigé ne traite que **11** des **12** lignes : la ligne `cooperate` du manuel n'a pas de clé |
| Consolidation 1, Activity 9    | glose « cause someone to become very angry » corrigée par « set off » — emploi inattendu       |
| Consolidation 2, Activity 3    | `genes` (banque du manuel) n'est classé dans **aucune** des deux colonnes du corrigé           |
| Consolidation 2, Activity 4    | corrigé « has **loved** » là où le choix imprimé est _has evolved / evolves / evolved_ ; **7** formes pour **8** trous |
| Consolidation 2, Activity 7    | corrigé « moves » là où le manuel imprime `(love)`                                             |
| Consolidation 2, Activity 9    | corrigé « as we had **expected** » ; le manuel imprime « as we had **anticipated** »           |
| Module Two (Exploring grammar) | « She has done so since she was five » est rangé en colonne **simple past** dans le manuel **et** dans le guide — c'est un **present perfect**. Erreur de fond **commune aux deux sources** |
| Module Two, guide p.32         | en-tête « Section Four : Speaking » **fautif** : la page traite « Arts. Section Two — Reading about great people » (Helen Keller). Confirmé par cinq recoupements ; l'en-tête apparaît donc deux fois dans le guide |
| Module Three, guide p.44       | corrigé « were given » là où le manuel n'offre que « was given » / « gave »                    |
| Module Three, guide p.39       | corrigé « motor boats » quand le tapescript dit « a private motor boat »                        |
| Module One, guide p.20         | corrigé incomplet de l'exercice B (Arts §2)                                                    |

**Règle appliquée dans toute la fiche** : le **guide fait foi pour le scope** ; là où son corrigé
contredit l'énoncé imprimé, **l'énoncé du manuel fait foi pour la tâche**, et l'écart est transcrit
des deux côtés plutôt qu'arbitré en silence. **Aucune de ces clés ne doit être reprise telle quelle en
génération sans re-résolution** — c'est précisément le type d'erreur qu'un QCM propage.

Un cas est d'une autre nature et mérite d'être traité à part : l'exemple mal classé du module Two est
**faux dans les deux sources**. Il ne s'agit pas d'un décalage d'édition mais d'une **erreur
pédagogique de l'ouvrage officiel**. Elle est transcrite telle quelle (fidélité), mais **elle ne doit
pas être enseignée** : un cours qui reprendrait ce tableau à l'identique enseignerait une faute. À
traiter explicitement au LOT B.

### 6.4 Coquilles de la source

Relevées et marquées `[sic]` au fil de la fiche, sans correction silencieuse. Les plus notables :
« William **Henry** Porter » (manuel p.33 — O. Henry s'appelait William *Sydney* Porter),
« **Isac** Asimov » (p.140), « **Eva** Merriam » (p.142, pour *Eve* Merriam), « have **incidental**
views » (guide p.14, pour *identical*), « one thousand of a micron » (guide p.46, pour *one
thousandth*), « accomodation », « slection », « honetmoon », « pospone », « millimiter »,
« inconveniencies », « uderstanding », et l'alternance « Camino » / « Comino », « in vitro » /
« invitro », « tumor » / « tumour » entre les deux ouvrages.
Une coquille mérite une vigilance particulière parce qu'elle **inverse une règle** : au Grammar
summary (manuel p.210), « If it is the **subject**, the restrictive pronoun is often left out » —
l'exemple donné montre une omission en position **objet**, et la règle énoncée deux lignes plus haut
dit l'inverse. **Ne pas propager.**

### 6.5 Provenance du travail, et ce que la R-7 doit viser en priorité

La transcription a été produite en partie par l'orchestratrice, en partie par des sous-agents en
contexte vierge, chacun cantonné à sa tranche :

| partie                                              | auteur          | rapport d'auteur   |
| --------------------------------------------------- | --------------- | ------------------ |
| en-tête, §1, Review Module, Consolidations 1 et 2, appendice, §3-§6 | orchestratrice  | —                  |
| Module One · Module Two · Module Three              | sous-agents     | **oui**, rendu     |
| **Module Four · Module Five · Module Six**          | sous-agents     | **NON**            |

⚠️ **Les modules Four, Five et Six ont été écrits par des sous-agents interrompus par la limite
d'usage de session au moment de rendre leur rapport.** Leurs fichiers sont **complets** (structure
intégrale, corrigés, tapescripts, listes de vocabulaire, bloc Incertitudes) et ont été contrôlés
structurellement — mais **leur auteur n'a jamais rendu compte de son propre travail**. C'est
exactement le cas de figure documenté par la méthode (§ B3, point 3) : des fichiers ni faux ni
relus, qui concentrent ensuite l'essentiel des constats d'audit.

**La relecture indépendante R-7 doit donc concentrer son sondage sur les modules Four, Five et Six**,
et en priorité sur la Section Five du module Four (§6.1, la seule inférence de la fiche).

### 6.6 État R-7 et points à trancher par Mohamed

- **R-7 non faite à ce jour.** Le statut de registre s'arrête donc à `complete` (couverture 100 % +
  profondeur de génération) et **pas** à `validee-r7`. La promotion appartient à l'humain.
- **La cassette audio** déclarée par le guide (p.4) n'est pas au corpus. Sans effet bloquant : les
  tapescripts couvrent tous les passages écoutés. Les seules activités réellement perdues sont celles
  qui exigent d'**entendre** (intonation, rythme, discrimination de sons à l'oreille) — recensées au
  §3.3.
- **Aucun fichier Taybah** pour la 3ème année secondaire : pas de vérification externe du séquençage
  trimestriel pour ce couple.
- **Le supplément Arts n'est pas codifié au chapitrage** (§4). C'est un choix : il est propre à
  `3eme-sec-lettres`, il est transcrit et disponible, mais le codifier maintenant déclarerait
  générable un périmètre qu'aucune tranche ne vise encore. À rouvrir quand la filière Lettres sera
  traitée pour elle-même.
- **L'ouverture des six classes est un arbitrage produit, pas une mécanique** — voir le rapport de
  campagne et la PR : R-8 sera atteint pour six classes à la fois, avec **une seule matière visible
  dans chacune**.
