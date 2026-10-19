# Carte d'affectation M1 — français 6ᵉ, chapitres 01, 02 (missions du gisement)

> Lot auteur du passage unique (PLAN.md ; PLAN-gisement.md § 4). 8 missions. Skills : `content-ecole-tn`, puis `content-langue-francais` pour le registre de langue, `prof-francais-college` pour calibrer les étages `d3` seulement (sans en reprendre le programme de 7ᵉ–8ᵉ) ; consignes `content-ingest/references/gisement-auteur-examen.md` (missions d'examen, avec la transcription de chaque session citée : `content/programmes-officiels/examens-nationaux/6eme-base/french/<année>-unique.md`) et `gisement-auteur-devoir.md` (missions 📝 : la carte seule, jamais le devoir). Ne touche à aucun autre chapitre que les tiens ; les autres lots écrivent en parallèle.

**Règles communes** (PLAN-gisement.md § 1) : chaque question dit sa session (« Concours 2023 ») et redonne la phrase OFFICIELLE de la transcription (consigne et énoncé tels qu'imprimés, coquilles incluses) ; une réécriture « Réécris … » devient « quelle réécriture est correcte ? » (QCM de formes) ou un matching/ordering ; un blanc `HP:` est DONNÉ rempli, jamais demandé ; une forme d'un verbe d'un chapitre ultérieur est donnée dans les options quand elle n'est pas la cible ; jamais de corrigé de site tiers : l'explication est la tienne, re-résolue. Étiquettes : vocabulaire `fr.*` du lot A (`vocab-french-6eme.json`), sur les distracteurs qui disent l'erreur du « piège » de la ligne, jamais sur multi/ordering/matching ; les ids neufs ou élargis que tu poses vont dans `content/misconceptions.json`. `chapter.json` : ajoute à `sources[]` la ligne « Sujets officiels du concours d'entrée aux collèges pilotes (6ᵉ année de base), Ministère de l'Éducation (corpus officiel, reprise citée, étude 36) — transcriptions : programmes-officiels/examens-nationaux/6eme-base/french/ » (missions d'examen).

**Ordre de travail** : (1) les ids d'étiquette neufs que tu poses ; (2) les missions, dans l'ordre de la carte ; (3) gates à chaque chapitre : `content:check`, `content:qa -- --subject french-6eme` (0 erreur), `content:tranche -- --subject french-6eme --changed --fresh --strict-longest`. Numéros de fichiers : à la suite de `05-entrainement` (06, 07, …) ; `displayOrder` à la suite.


## Chapitre `01-travailler-pour-sepanouir`

### Missions (gisement)

#### m001 → `exercices/06-exams-2009-2025-temps-de-la-phrase.json` · d2 practice 75/15 · 8 questions · régime **examen**

- Titre : « 🏛️ Concours 2009–2025 · hier, aujourd'hui, demain : le temps de la phrase ⭐⭐ »
- Registre : id `C02#9` ; sources `C02#9, C03#9, C07#6, C08#9, C10#7, C18#7`
- Sources (base en premier) : C02 (2025) ex. 9 ; C03 (2024) ex. 9 ; C07 (2020) ex. 6 ; C08 (2019) ex. 9 ; C10 (2017) ex. 7 ; C18 (2009) ex. 7
- Items :
  - 2025 conj. 2 : « Une voix se met à hurler... Une tête surgit. » à compléter après « Bientôt, … » — le repère de temps impose le futur ; QCM du temps imposé, puis QCM de la forme de « se mettre » (les formes sont données dans les options) — 2 q.
    - piège (étiquette à porter par un distracteur) : laisser le présent malgré l'adverbe de futur — ligne C02#9 (d2)
  - 2024 conj. 2 : « La peur nous a broyé les entrailles, mais nous n'avons pas songé à nous enfuir. » à mettre au présent, négation conservée — QCM de la phrase au présent — 1 q.
    - piège (étiquette à porter par un distracteur) : garder le passé composé ou oublier la négation — ligne C03#9 (d2)
  - 2020 gram. 1 : « Samy et Laura s'occupent de l'arbre ; ils ne se découragent pas. » devient « Samy et Laura continuent à … sans … » — QCM des deux infinitifs (le pronom réfléchi disparaît) — 1 q.
    - piège (étiquette à porter par un distracteur) : garder le pronom réfléchi conjugué — ligne C07#6 (d2)
  - 2019 conj. 2 : « Je lui ai fourré mon goûter dans les mains et je suis parti. » à commencer par « Demain, je … » — QCM de la phrase au futur (la forme de « partir » est donnée) — 1 q.
    - piège (étiquette à porter par un distracteur) : garder le passé composé — ligne C08#9 (d2)
  - 2017 conj. 1 : « Certains m'ont souri et d'autres m'ont lancé des regards gênés. » au futur « en utilisant un terme temporel de ton choix » — QCM du terme temporel compatible avec le futur, puis QCM de la phrase au futur — 2 q.
    - piège (étiquette à porter par un distracteur) : garder le passé composé — ligne C10#7 (d2)
  - 2009 conj. 1 : « Quand j'entends la musique, j'oublie ma peur. » à mettre au passé composé — QCM (la forme de « entendre » est donnée) — 1 q.
    - piège (étiquette à porter par un distracteur) : mal former le participe d'un verbe du troisième groupe — ligne C18#7 (d2)
- Ne pas redemander : `01/quiz#3`, `01/01-pratique#3`, `01/01-pratique#4`, `01/01-pratique#5`, `01/01-pratique#6`, `01/02-boss#1`, `01/02-boss#2`, `01/02-boss#4`, `01/02-boss#5`, `01/04-defi#3`
- Note : Famille « le temps » du `01` : présent, passé composé, futur de verbes en -er, avec l'infinitif après préposition (2020). Les verbes d'un chapitre ultérieur (se mettre `05`, partir, entendre : hors liste) ne sont jamais la cible : leurs formes sont données dans les options. Écartés de la famille : C11#8 (2016, être, placé au `03`), C06#11 (`08`).

#### m002 → `exercices/07-devoir-classer-les-mots.json` · d2 practice 75/15 · 6 questions · régime **devoir** (salle blanche)

- Titre : « 📝 Classer les mots : noms propres, noms communs, pronoms ⭐⭐ »
- Registre : id `D01#7` ; sources `D01#7`
- Cartes : devoir A (épreuve de 1ᵉʳ trimestre, école primaire), exercice 7 — carte anonyme
- Items :
  - Un petit texte neuf de quatre ou cinq phrases (écrit par l'auteur, métiers du `01`) : relier chaque mot relevé à sa colonne — nom propre, nom commun, pronom personnel — (matching) ; puis QCM « quel mot est un nom propre » avec un nom commun en majuscule de début de phrase comme leurre ; QCM « quel pronom remplace le groupe souligné » ; multi « coche les noms communs » ; QCM « dans quelle colonne place-t-on ce mot ». 6 q.
    - piège (étiquette à porter par un distracteur) : confondre nom propre et nom commun — ligne D01#7 (d2)
- Ne pas redemander : `01/quiz#1`, `01/quiz#2`, `01/01-pratique#1`, `01/01-pratique#2`, `01/03-revision#1`, `01/03-revision#2`
- Note : Salle blanche : la carte ne donne que le geste (relever puis classer dans un tableau à trois colonnes) ; texte, noms et pronoms sont neufs. Le geste neuf est de classer des mots TIRÉS D'UN MÊME TEXTE ; le patron classe des mots isolés.

#### m003 → `exercices/08-devoir-presenter-un-metier.json` · d2 practice 75/15 · 6 questions · régime **devoir** (salle blanche)

- Titre : « 📝 Présenter un métier en quelques phrases ⭐⭐ »
- Registre : id `D03#1` ; sources `D03#1`
- Cartes : devoir B (épreuve de production du 1ᵉʳ trimestre, école primaire), consigne unique — carte anonyme
- Items :
  - Préparer un court texte de présentation d'un métier choisi dans une liste (l'auteur invente la liste) : QCM « quel sujet reste dans la consigne » (leurre : un autre sujet) ; ordering des quatre phrases (qui il est, ce qu'il fait, où, pourquoi on l'aime) ; QCM « quelle phrase remplace le nom répété par un pronom sans doute possible » ; QCM du verbe au présent ; multi « quelles phrases sortent du sujet » ; QCM d'une phrase de fin. 6 q.
    - piège (étiquette à porter par un distracteur) : parler d'un autre sujet que le métier choisi — ligne D03#1 (d2)
- Ne pas redemander : `01/03-revision#6`, `01/04-defi#1`, `01/04-defi#5`, `01/04-defi#6`, `01/05-entrainement#5`
- Note : Salle blanche. Seule préparation de production du `01` (aucun sujet d'examen n'y a sa consigne de rédaction). Calibrer en `d2` : un court texte descriptif, pas un récit à dialogue.


## Chapitre `02-communiquer-avec-les-autres`

### Missions (gisement)

#### m004 → `exercices/06-exams-2015-2025-ce-cet-cette-ces-mon-son-leur.json` · d2 practice 75/15 · 10 questions · régime **examen**

- Titre : « 🏛️ Concours 2015–2025 · ce, cet, cette, ces — mon, son, leur : changer le nom, changer le possesseur ⭐⭐ »
- Registre : id `C02#7` ; sources `C02#7, C03#6, C04#6, C05#7, C07#7, C12#6`
- Sources (base en premier) : C02 (2025) ex. 7 ; C03 (2024) ex. 6 ; C04 (2023) ex. 6 ; C05 (2022) ex. 7 ; C07 (2020) ex. 7 ; C12 (2015) ex. 6
- Items :
  - 2025 gram. 3 : « Jeanne couche ses impressions sur son journal de voyage. » devient « Jeanne et son amie couchent … impressions sur … journal de voyage. » — QCM « leurs », QCM « leur » (le verbe « couchent » est donné) — 2 q.
    - piège (étiquette à porter par un distracteur) : garder possessifs et verbe au singulier — ligne C02#7 (d3)
  - 2024 gram. 2 : « Quand nous avons raconté notre aventure à mon père, il nous a dit que les phoques étaient plus nombreux dans cet archipel. » devient « Quand vous avez raconté … aventure à … parents, … » — QCM « votre », QCM « vos » (les autres blancs, dont l'accord de « nombreux », sont donnés) — 2 q.
    - piège (étiquette à porter par un distracteur) : garder les possessifs de la personne d'origine — ligne C03#6 (d3)
  - 2023 gram. 2 : « Cette amie venait à la maison tous les jours pour m'apporter mes leçons et mes devoirs. » devient « … ami venait à la maison … les matinées pour m'apporter … leçon et … devoir. » — QCM « cet », QCM « ma … mon » ; le blanc « toutes » est DONNÉ rempli (`HP:accord-tout`) — 2 q.
    - piège (étiquette à porter par un distracteur) : mal accorder tout avec un nom féminin — ligne C04#6 (d3)
  - 2022 gram. 2 : « Ce soir-là, j'ai demandé à ma mère de me faire sortir de cette situation. » en remplaçant « soir » par « nuit » et « situation » par « embarras » — QCM « Cette nuit-là », QCM « cet embarras » (devant voyelle) — 2 q.
    - piège (étiquette à porter par un distracteur) : oublier la forme devant voyelle — ligne C05#7 (d2)
  - 2020 gram. 2 : « Cette plante perd son feuillage en automne. » avec les noms soulignés au pluriel — QCM de la phrase au pluriel (« Ces plantes perdent leur feuillage / leurs feuillages ») — 1 q.
    - piège (étiquette à porter par un distracteur) : laisser le déterminant au singulier — ligne C07#7 (d2)
  - 2015 gram. 3 : « Ces délices disparaissent dans son sac. » en remplaçant « délices » par « friandise » et « sac » par « poche » — QCM « Cette friandise disparaît dans sa poche » — 1 q.
    - piège (étiquette à porter par un distracteur) : oublier d'adapter le déterminant au nouveau nom — ligne C12#6 (d2)
- Ne pas redemander : `02/quiz#1`, `02/quiz#2`, `02/01-pratique#1`, `02/01-pratique#2`, `02/01-pratique#3`, `02/01-pratique#4`, `02/01-pratique#5`, `02/01-pratique#6`, `02/03-revision#5`, `02/04-defi#5`, `02/04-defi#6`
- Note : Famille « déterminants démonstratifs et possessifs » du `02`. Les lignes d3 (C02#7, C03#6) ne sont reprises que pour leur part possessif/démonstratif, d'où un étage `d2` : accord du verbe (`05`) et de l'adjectif (`06`) sont donnés. C01#8 (2026, « cette phrase … nulle ») est au `07` (mission des adjectifs au féminin).

#### m005 → `exercices/07-exams-2009-2026-imperatif-fais-parler.json` · d2 practice 75/15 · 12 questions · régime **examen**

- Titre : « 🏛️ Concours 2009–2026 · fais parler : de l'ordre rapporté à l'impératif ⭐⭐ »
- Registre : id `C01#10` ; sources `C01#10, C03#10, C04#10, C05#10, C07#10, C08#10, C10#8, C11#10, C15#10, C18#8`
- Sources (base en premier) : C01 (2026) ex. 10 ; C03 (2024) ex. 10 ; C04 (2023) ex. 10 ; C05 (2022) ex. 10 ; C07 (2020) ex. 10 ; C08 (2019) ex. 10 ; C10 (2017) ex. 8 ; C11 (2016) ex. 10 ; C15 (2012) ex. 10 ; C18 (2009) ex. 8
- Items :
  - 2026 conj. 2 : « Tu viens jouer sur ma PlayStation 4 à la sortie ? » à réécrire à l'impératif en commençant par « Louis, Paloma, … » — QCM « Venez jouer… » (la question devient un ordre au pluriel) — 1 q.
    - piège (étiquette à porter par un distracteur) : garder le sujet ou la terminaison du singulier — ligne C01#10 (d2)
  - 2024 conj. 3 : « Le père ordonne à son fils de prendre la piste tortueuse et d'aller à l'école. » → « Prends … et va … » — QCM de « prends » (le s), QCM de « va » (pas de s) — 2 q.
    - piège (étiquette à porter par un distracteur) : garder le sujet ou ajouter un s à aller — ligne C03#10 (d2)
  - 2023 conj. 3 : « Le médecin ordonne à Claudine de finir le traitement et de revenir dans un mois. » → « Finis … et reviens … » — QCM (la forme « finis » est donnée, la cible est « reviens ») — 1 q.
    - piège (étiquette à porter par un distracteur) : garder l'infinitif ou mal former l'impératif — ligne C04#10 (d2)
  - 2022 conj. 2 : « La professeure dit à ses élèves de faire beaucoup de répétitions et d'apprendre les rôles comme il se doit. » → « Faites … et apprenez … » — QCM — 2 q.
    - piège (étiquette à porter par un distracteur) : employer le présent ou l'infinitif — ligne C05#10 (d2)
  - 2020 conj. 2 : « Pour sauver l'arbre, Laura demande à Samy de bien réfléchir et de trouver une solution. » → « Réfléchis bien et trouve une solution » — QCM (« trouve » sans s) — 1 q.
    - piège (étiquette à porter par un distracteur) : conserver l'infinitif ou le sujet — ligne C07#10 (d2)
  - 2019 conj. 3 : « La maîtresse demande à ses élèves de regarder le tableau et de faire attention. » → « Regardez … et faites attention » — QCM — 1 q.
    - piège (étiquette à porter par un distracteur) : conserver l'infinitif ou le sujet — ligne C08#10 (d2)
  - 2017 conj. 2 : « La maîtresse ordonne de souhaiter la bienvenue à Caroline. » dite à Alex puis aux élèves — matching (destinataire ↔ forme : « Souhaite » ↔ « Souhaitez ») — 1 q.
    - piège (étiquette à porter par un distracteur) : garder la même forme pour les deux destinataires — ligne C10#8 (d2)
  - 2012 conj. 3 : « Rami conseille aux enfants de protéger les oiseaux et d'être leurs amis. » → « Protégez … et soyez … » — QCM (« soyez » irrégulier) — 1 q.
    - piège (étiquette à porter par un distracteur) : garder l'infinitif ou mal former l'impératif d'être — ligne C15#10 (d2)
  - 2009 conj. 2 : « Le maître demande à Adrien de prendre le violon et de jouer un morceau de musique. » → « Prends … et joue … » — QCM — 1 q.
    - piège (étiquette à porter par un distracteur) : garder l'infinitif ou la forme du pluriel — ligne C18#8 (d2)
  - 2016 conj. 4 : Alice demande aux crayons de couleur d'accepter le crayon gris (« Écris le conseil d'Alice ») — QCM du conseil à l'impératif pluriel (« Acceptez … ») — 1 q.
    - piège (étiquette à porter par un distracteur) : garder l'infinitif ou le sujet — ligne C11#10 (d1)
- Ne pas redemander : `02/quiz#3`, `02/02-boss#1`, `02/02-boss#2`, `02/02-boss#3`, `02/02-boss#4`, `02/02-boss#6`, `02/03-revision#6`, `02/04-defi#3`, `02/05-entrainement#5`
- Note : Famille la plus fréquente des sujets (onze lignes). L'impératif est la cible ; les verbes dont le chapitre est ultérieur (finir `04`, prendre `05`, aller `06`) n'ont que des formes d'impératif déjà vues au `02` (prends, va) ou données. C09#10 (« écrivez / écris ») est au `07` (écrire). Douze questions : plafond atteint.

#### m006 → `exercices/08-exam-2026-lecture-dix-jours-sans-ecran.json` · d2 practice 75/15 · 10 questions · régime **examen**

- Titre : « 🏛️ Concours 2026 · lecture : dix jours sans écrans ⭐⭐ »
- Registre : id `C01#1` ; sources `C01#1, C01#2, C01#3, C01#4, C01#5`
- Sources (base en premier) : C01 (2026) ex. 1 ; C01 (2026) ex. 2 ; C01 (2026) ex. 3 ; C01 (2026) ex. 4 ; C01 (2026) ex. 5
- Items :
  - Q1 (coche) : « Les personnages qui rejettent l'idée de passer dix jours sans écrans sont : Paloma / Louis / Gordon » — QCM du ou des personnages, puis QCM de la phrase du texte qui le prouve (leurre : la moquerie de l'un n'est pas un rejet de l'autre) — 2 q.
    - piège (étiquette à porter par un distracteur) : confondre rejet franc et simple moquerie — ligne C01#1 (d1)
  - Q2 : « Le narrateur et Gordon sont amis. Ils ont un caractère commun. Relève dans le texte deux détails qui le montrent. » — QCM « quel détail montre le trait commun », multi « coche les deux détails » — 2 q.
    - piège (étiquette à porter par un distracteur) : relever des actions sans lien avec le trait — ligne C01#2 (d2)
  - Q3 : « La maîtresse n'est pas autoritaire. Donne deux éléments du texte qui le montrent. » (elle explique, propose de construire ensemble avec des affiches, propose un vote) — QCM « quel élément montre qu'elle n'est pas autoritaire » (leurre : un élément qui montre un trait d'un élève, pas de la maîtresse) — 1 q.
    - piège (étiquette à porter par un distracteur) : confondre trait de caractère et fonction du personnage — ligne C01#3 (d2)
  - Q4 a : synonymes de « complètement __débile__ » et de « __se mettre au__ travail » ; Q4 b : contraires de « __chouette__ » et de « __ennui__ » (« On sera morts d'ennui », « combles de … ») — 4 QCM (un par mot), le leurre est un mot d'une autre nature — 4 q.
    - piège (étiquette à porter par un distracteur) : proposer un mot de nature grammaticale différente — ligne C01#4 (d2)
  - Q5 : « Certains élèves de la classe de Mme Guégan voient que, privés d'écrans, ils vont mourir d'ennui. Qu'en penses-tu ? Justifie ton point de vue. » — QCM « quel argument justifie le point de vue ‹ je suis d'accord › » (une justification qui s'appuie sur le texte, pas une affirmation sans appui) — 1 q.
    - piège (étiquette à porter par un distracteur) : répondre sans justifier ni lien avec le texte — ligne C01#5 (d2)
- Ne pas redemander : `02/quiz#5`, `02/04-defi#2`
- Note : Compréhension d'un texte récent, une mission par texte (R2). Texte intégral : PDF officiel `/tmp/claude-0/fr6g/src/2026-francais.pdf` (sha256 au registre) — citer une ou deux phrases par question, jamais le texte entier ; citation utile : « Ce serait chouette d'essayer. » Questions ouvertes converties en fermées (QCM, multi). Aucune lecture de texte d'examen dans le `02`. Les deux lignes d'élément perturbateur du patron (quiz#5, défi#2) lisent un mini-récit : autre geste.

#### m007 → `exercices/09-exams-2013-2026-recit-dispute-ecrans.json` · d3 boss 120/30 · 8 questions · régime **examen**

- Titre : « 🏛️ Concours 2013–2026 · préparer un récit : une dispute à propos des écrans ⭐⭐⭐ »
- Registre : id `C01#12` ; sources `C01#12, C07#12, C14#10`
- Sources (base en premier) : C01 (2026) ex. 12 ; C07 (2020) ex. 12 ; C14 (2013) ex. 10
- Items :
  - 2026 : « Gordon accepte de participer au projet … à contrecœur. Le lendemain, Paloma le surprend en train de naviguer sur le net, en cachette. Raconte ce qui s'est passé dans un récit d'au moins huit (8) phrases en y intégrant quelques répliques et en décrivant la réaction des deux personnages. » — multi « quels éléments le récit doit contenir » (répliques, réaction de Paloma, réaction de Gordon, au moins huit phrases) ; QCM « quelle phrase décrit une réaction sans la nommer » ; QCM de la première réplique de Paloma — 3 q.
    - piège (étiquette à porter par un distracteur) : oublier les répliques ou la description des réactions — ligne C01#12 (d3)
  - 2020 : « Comme Laura et Samy, tu veux recourir à Internet … Mais ce dernier préfère les livres comme source d'information. … court dialogue où chacun de vous explique son point de vue et justifie son choix. » — matching « réplique ↔ qui la dit » (Internet / livres) ; QCM « quelle réplique justifie un choix » (avec ‹ parce que ›) — 2 q.
    - piège (étiquette à porter par un distracteur) : oublier le dialogue ou la justification des choix — ligne C07#12 (d3)
  - 2013 : « Ton ami passe tout son temps devant la télé. En classe, il n'est plus attentif aux leçons. Tu interviens et, au bout d'un certain temps, ton ami change de comportement… » — ordering des quatre moments (la télé gêne la classe, tu interviens, il résiste, il change) ; QCM de la phrase qui montre le changement — 3 q.
    - piège (étiquette à porter par un distracteur) : oublier le dialogue ou le changement — ligne C14#10 (d3)
- Ne pas redemander : rien d'équivalent dans le chapitre
- Note : Production : préparation fermée, regroupée par archétype « récit d'une intervention à propos des écrans, avec dialogue ». Aucune rédaction demandée : chaque question redonne la consigne OFFICIELLE de sa session. Aucune consigne de rédaction dans le `02` existant. Placement F4 : les trois thèmes relèvent du module 2 (médias). La ponctuation du dialogue est au `03` (mission de dialogue), pas ici.

#### m008 → `exercices/10-devoir-relier-enumerer-rediger.json` · d2 practice 75/15 · 7 questions · régime **devoir** (salle blanche)

- Titre : « 📝 Lire un petit texte : relier, énumérer, rédiger ⭐⭐ »
- Registre : id `D02#5` ; sources `D02#5, D09#4, D01#4`
- Cartes : devoir C (épreuve de lecture du 1ᵉʳ trimestre, école primaire), exercice 5 — carte anonyme ; devoir D (épreuve de lecture du 3ᵉ trimestre, école primaire), exercice 4 — carte anonyme ; devoir A (épreuve de 1ᵉʳ trimestre, école primaire), exercice 4 — carte anonyme
- Items :
  - Un petit texte neuf (messages, échanges ou scène d'école ; thème de la communication) : matching « relier chaque personnage à l'énoncé qui le décrit » puis matching « relier chaque personnage à l'action qu'il accomplit » (deux appariements, une option en trop, leurre : deux personnages permutés) — 3 q.
    - pièges (étiquette à porter par un distracteur) : relier à l'énoncé contraire à la situation ; permuter deux personnages — lignes D02#5, D09#4 (d1)
  - Énumérer les usages d'un objet de communication (multi : coche les usages cités par le texte) puis QCM « quel paragraphe rédigé enchaîne ces usages en phrases » (leurre : des mots juxtaposés sans phrase) ; QCM d'un début de paragraphe ; QCM d'une phrase qui ne fait pas partie des usages — 4 q.
    - piège (étiquette à porter par un distracteur) : juxtaposer des mots sans phrase rédigée — ligne D01#4 (d2)
- Ne pas redemander : `02/04-defi#1`, `02/05-entrainement#1`, `02/05-entrainement#4`
- Note : Salle blanche. TROIS cartes de TROIS devoirs d'auteurs différents (le plafond de deux par auteur est tenu) fusionnées en une seule mission : même chapitre, même type de texte, deux signatures proches (appariement et paragraphe). Geste neuf : relier des éléments d'un TEXTE (le patron relie des mots à leur définition ou à leur rôle).

