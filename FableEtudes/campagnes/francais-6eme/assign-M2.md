# Carte d'affectation M2 — français 6ᵉ, chapitres 03, 04 (missions du gisement)

> Lot auteur du passage unique (PLAN.md ; PLAN-gisement.md § 4). 6 missions. Skills : `content-ecole-tn`, puis `content-langue-francais` pour le registre de langue, `prof-francais-college` pour calibrer les étages `d3` seulement (sans en reprendre le programme de 7ᵉ–8ᵉ) ; consignes `content-ingest/references/gisement-auteur-examen.md` (missions d'examen, avec la transcription de chaque session citée : `content/programmes-officiels/examens-nationaux/6eme-base/french/<année>-unique.md`) et `gisement-auteur-devoir.md` (missions 📝 : la carte seule, jamais le devoir). Ne touche à aucun autre chapitre que les tiens ; les autres lots écrivent en parallèle.

**Règles communes** (PLAN-gisement.md § 1) : chaque question dit sa session (« Concours 2023 ») et redonne la phrase OFFICIELLE de la transcription (consigne et énoncé tels qu'imprimés, coquilles incluses) ; une réécriture « Réécris … » devient « quelle réécriture est correcte ? » (QCM de formes) ou un matching/ordering ; un blanc `HP:` est DONNÉ rempli, jamais demandé ; une forme d'un verbe d'un chapitre ultérieur est donnée dans les options quand elle n'est pas la cible ; jamais de corrigé de site tiers : l'explication est la tienne, re-résolue. Étiquettes : vocabulaire `fr.*` du lot A (`vocab-french-6eme.json`), sur les distracteurs qui disent l'erreur du « piège » de la ligne, jamais sur multi/ordering/matching ; les ids neufs ou élargis que tu poses vont dans `content/misconceptions.json`. `chapter.json` : ajoute à `sources[]` la ligne « Sujets officiels du concours d'entrée aux collèges pilotes (6ᵉ année de base), Ministère de l'Éducation (corpus officiel, reprise citée, étude 36) — transcriptions : programmes-officiels/examens-nationaux/6eme-base/french/ » (missions d'examen).

**Ordre de travail** : (1) les ids d'étiquette neufs que tu poses ; (2) les missions, dans l'ordre de la carte ; (3) gates à chaque chapitre : `content:check`, `content:qa -- --subject french-6eme` (0 erreur), `content:tranche -- --subject french-6eme --changed --fresh --strict-longest`. Numéros de fichiers : à la suite de `05-entrainement` (06, 07, …) ; `displayOrder` à la suite.


## Chapitre `03-accepter-les-autres`

### Missions (gisement)

#### m009 → `exercices/06-exams-2010-2023-epithete-attribut-et-etre.json` · d2 practice 75/15 · 8 questions · régime **examen**

- Titre : « 🏛️ Concours 2010–2023 · l'adjectif épithète ou attribut — le verbe être ⭐⭐ »
- Registre : id `C04#8` ; sources `C04#8, C07#8, C11#5, C11#8, C17#8`
- Sources (base en premier) : C04 (2023) ex. 8 ; C07 (2020) ex. 8 ; C11 (2016) ex. 5 ; C11 (2016) ex. 8 ; C17 (2010) ex. 8
- Items :
  - 2023 conj. 1 : « J'ai été hospitalisée ; l'opération a duré plusieurs heures. » à commencer par « La semaine prochaine, … » — QCM « serai hospitalisée », QCM « durera » — 2 q.
    - piège (étiquette à porter par un distracteur) : conserver le passé composé ou mal former être — ligne C04#8 (d2)
  - 2020 gram. 3 : « L'arbre de Samy demeure chétif dans son coin obscur. » — tableau « groupe nominal sujet / groupe verbal / adjectif épithète / adjectif attribut » en matching (leurre : permuter épithète et attribut) — 1 q.
    - piège (étiquette à porter par un distracteur) : confondre adjectif épithète et adjectif attribut — ligne C07#8 (d2)
  - 2016 gram. 1 a : « Mon crayon jaune est bien autoritaire. » — « Souligne l'adjectif attribut et encadre l'adjectif épithète » : QCM de l'attribut, QCM de l'épithète — 2 q. (La partie b, la reprise par un pronom, est `HP:pronom-complement` : écartée.)
    - piège (étiquette à porter par un distracteur) : confondre épithète et attribut ou répéter le groupe nominal — ligne C11#5 (d3)
  - 2010 conj. 2 : « Les enfants sont là. Ils forment un grand cercle autour de la surprise. » au futur — QCM « seront … formeront » — 2 q.
    - piège (étiquette à porter par un distracteur) : laisser le présent ou mal former le futur d'être — ligne C17#8 (d2)
  - 2016 conj. 2 : « Et puis, tu es triste. » à commencer par « La veille, vous … tristes » — QCM « avez été » ; l'imparfait n'est PAS proposé (`HP:imparfait`) — 1 q.
    - piège (étiquette à porter par un distracteur) : laisser le présent ou accorder mal — ligne C11#8 (d2)
- Ne pas redemander : `03/quiz#1`, `03/quiz#2`, `03/quiz#3`, `03/01-pratique#1`, `03/01-pratique#2`, `03/01-pratique#3`, `03/01-pratique#4`, `03/02-boss#1`, `03/02-boss#6`, `03/03-revision#2`, `03/03-revision#6`, `03/04-defi#1`, `03/04-defi#3`, `03/05-entrainement#2`, `03/05-entrainement#6`
- Note : Deux familles minces fusionnées (l'épithète/l'attribut : deux lignes ; être : trois lignes). C15#10 (« soyez ») est dans la mission d'impératif du `02`. Le `03` n'a aucun texte d'examen récent : sa lecture vient de la mission de devoir (ordre, titre, portrait).

#### m010 → `exercices/07-exams-2016-2017-recit-faire-accepter.json` · d3 boss 120/30 · 7 questions · régime **examen**

- Titre : « 🏛️ Concours 2016, 2017 · préparer un récit : faire accepter un camarade, avec un dialogue ⭐⭐⭐ »
- Registre : id `C10#9` ; sources `C10#9, C11#11`
- Sources (base en premier) : C10 (2017) ex. 9 ; C11 (2016) ex. 11
- Items :
  - 2017 : « Dès la sortie de la classe, l'élève à la bouche rouge et aux cheveux roux commence à gêner Caroline. Tu interviens avec quelques-uns de tes amis pour l'amener à accepter sa nouvelle camarade et à la respecter. Rédige un récit de huit phrases au moins … (Ton récit doit intégrer un court dialogue.) » — QCM de la première réplique qui amène à l'acceptation ; QCM « quel dialogue est correctement ponctué » (tirets ou guillemets, verbe introducteur, majuscule) ; ordering des quatre répliques ; multi « quels éléments le récit doit contenir » — 4 q.
    - piège (étiquette à porter par un distracteur) : oublier le dialogue ou la progression vers l'acceptation — ligne C10#9 (d3)
  - 2016 : « Un enfant handicapé habite dans votre immeuble. Tes amis et toi, vous avez remarqué qu'il est toujours seul. Vous avez décidé de l'aider à s'intégrer dans le groupe pour devenir votre ami. Raconte, en huit phrases au moins, ce qui s'est passé en intégrant un dialogue dans ton récit. » — QCM du plan en trois temps (constat, démarche, intégration) ; QCM du verbe introducteur qui convient à une invitation ; QCM d'une phrase de fin qui montre l'intégration — 3 q.
    - piège (étiquette à porter par un distracteur) : oublier le dialogue ou la progression du récit — ligne C11#11 (d3)
- Ne pas redemander : `03/quiz#5`, `03/02-boss#4`, `03/03-revision#4`, `03/04-defi#6`
- Note : Archétype « faire accepter l'autre, avec dialogue » : c'est ici, au `03` (« Faire parler les personnages : le dialogue »), que la ponctuation du dialogue est préparée. Les autres récits à dialogue sont rangés par archétype aux `02`, `04`, `05`, `06`, `07`. Questions fermées : aucune rédaction demandée.

#### m011 → `exercices/08-devoir-devoir-lire-ordre-titre-portrait.json` · d2 practice 75/15 · 8 questions · régime **devoir** (salle blanche)

- Titre : « 📝 Lire un récit : ordre des événements, titre et portrait ⭐⭐ »
- Registre : id `D05#5` ; sources `D05#5, D05#7, D05#3`
- Cartes : devoir E (épreuve de lecture du 2ᵉ trimestre, école primaire), exercice 5 — carte anonyme ; devoir E (même épreuve), exercice 7 — carte anonyme ; devoir E (même épreuve), exercice 3 — carte anonyme
- Items :
  - Un petit récit neuf de quelques phrases sur l'accueil d'un camarade différent (écrit par l'auteur) : ordering des événements dans l'ordre DU TEXTE (leurre : un ordre plausible mais différent) — 2 q.
    - piège (étiquette à porter par un distracteur) : suivre un ordre plausible plutôt que celui du texte — ligne D05#5 (d2)
  - Choisir le titre qui convient au texte (QCM : trois titres, l'un trop partiel, l'autre trop vague, le bon qui résume l'histoire) ; QCM « quel titre ne convient pas et pourquoi » — 2 q.
    - piège (étiquette à porter par un distracteur) : proposer un titre trop partiel ou trop vague — ligne D05#7 (d2)
  - Relever les adjectifs qui décrivent un personnage (multi ; leurre : un nom, un participe passé employé comme adjectif) ; QCM « dans quelle phrase ce mot est-il un adjectif » — 4 q.
    - piège (étiquette à porter par un distracteur) : relever un nom ou un participe à la place — ligne D05#3 (d2)
- Ne pas redemander : `03/01-pratique#1`, `03/02-boss#1`, `03/03-revision#4`, `03/04-defi#4`, `03/05-entrainement#2`, `03/05-entrainement#3`
- Note : Salle blanche : une carte d'un seul devoir, trois gestes de lecture absents des examens (remise en ordre d'événements, titre, relevé des adjectifs d'un portrait). Seul texte à lire du `03`. L'auteur écrit un récit court (≤ 8 phrases, sans rapport avec le devoir) : tout le support de la mission est neuf.


## Chapitre `04-sentraider-pour-reussir`

### Missions (gisement)

#### m012 → `exercices/06-exams-2018-2024-phrase-negative.json` · d2 practice 75/15 · 6 questions · régime **examen**

- Titre : « 🏛️ Concours 2018–2024 · ne… plus, ne… jamais : dire le contraire d'une phrase ⭐⭐ »
- Registre : id `C03#7` ; sources `C03#7, C06#7, C08#7, C09#8`
- Sources (base en premier) : C03 (2024) ex. 7 ; C06 (2021) ex. 7 ; C08 (2019) ex. 7 ; C09 (2018) ex. 8
- Items :
  - 2024 gram. 3 : « La peur nous broie toujours les entrailles. » à la forme négative — QCM « La peur ne nous broie jamais les entrailles » (leurres : garder « toujours », oublier « ne ») — 1 q.
    - piège (étiquette à porter par un distracteur) : oublier ne ou garder l'adverbe d'origine — ligne C03#7 (d2)
  - 2021 gram. 2 : « Le chat est toujours assis sur le même banc. » à la forme négative — QCM — 2 q (ne… jamais ; ne… plus).
    - piège (étiquette à porter par un distracteur) : oublier ne ou garder l'adverbe d'origine — ligne C06#7 (d2)
  - 2018 gram. 3 : « Le désert ne traverse jamais la forêt. » à la forme affirmative — QCM « Le désert traverse toujours / souvent la forêt » (leurre : garder « ne », changer le sens) — 2 q.
    - piège (étiquette à porter par un distracteur) : garder un mot négatif ou changer le sens — ligne C09#8 (d2)
  - 2019 gram. 3 : « Veux-tu du pain ? » — « Réponds à cette question par une phrase à la forme négative : Non, … » — QCM de la réponse (« je ne veux pas de pain », l'article change) — 1 q.
    - piège (étiquette à porter par un distracteur) : répondre par une phrase affirmative ou oublier le changement d'article — ligne C08#7 (d2)
- Ne pas redemander : `04/quiz#1`, `04/quiz#2`, `04/01-pratique#1`, `04/01-pratique#2`, `04/02-boss#1`, `04/03-revision#1`, `04/03-revision#2`, `04/03-revision#6`, `04/04-defi#1`, `04/04-defi#3`
- Note : Écarté : C01#7 (2026, « plus personne ne rit » → forme affirmative) : `HP:negation-personne`, ⛔ au § 2.10 D de la fiche. Le patron a déjà beaucoup de négations : l'apport est la PHRASE OFFICIELLE, la réponse « Non, … » (2019) et le sens inverse (négatif → affirmatif, 2018).

#### m013 → `exercices/07-exams-2020-2025-verbes-comme-finir.json` · d2 practice 75/15 · 8 questions · régime **examen**

- Titre : « 🏛️ Concours 2020–2025 · finir, saisir, grandir, envahir : passé composé et futur ⭐⭐ »
- Registre : id `C02#10` ; sources `C02#10, C05#11, C06#10, C07#9`
- Sources (base en premier) : C02 (2025) ex. 10 ; C05 (2022) ex. 11 ; C06 (2021) ex. 10 ; C07 (2020) ex. 9
- Items :
  - 2025 conj. 3 : « Thierry saisit sa tablette à dessin et ébauche quelques esquisses. » au passé composé — QCM « a saisi … a ébauché » (leurre : le participe en -i mal formé) — 2 q.
    - piège (étiquette à porter par un distracteur) : oublier l'auxiliaire ou mal former le participe en -i — ligne C02#10 (d2)
  - 2021 conj. 2 : « Le chat grimpe sur le banc et finit le goûter. » au passé composé — QCM « a grimpé … a fini » — 2 q.
    - piège (étiquette à porter par un distracteur) : mal former le participe du verbe en -ir — ligne C06#10 (d2)
  - 2020 conj. 1 : « Au printemps, l'arbre grandit et laisse éclater ses bourgeons. » à commencer par « Au printemps prochain, l'arbre … » — QCM « grandira … laissera éclater » — 2 q.
    - piège (étiquette à porter par un distracteur) : laisser le présent ou mal former le futur — ligne C07#9 (d2)
  - 2022 conj. 3 : « Je suis sur scène. Une grande joie m'envahit. » à commencer par « Demain, je … » — QCM « serai … envahira » — 2 q.
    - piège (étiquette à porter par un distracteur) : laisser le présent ou mal former le futur — ligne C05#11 (d2)
- Ne pas redemander : `04/quiz#3`, `04/quiz#4`, `04/01-pratique#3`, `04/01-pratique#4`, `04/01-pratique#5`, `04/02-boss#2`, `04/02-boss#6`, `04/03-revision#5`, `04/04-defi#6`, `04/05-entrainement#3`, `04/05-entrainement#6`
- Note : Verbes du 2ᵉ groupe au passé composé et au futur. Les verbes en -er du même exercice (grimper, laisser, ébaucher) n'ont que des formes données ; « être » (`03`) et « envahir » (`04`) cumulent : placement au `04`, chapitre le plus avancé.

#### m014 → `exercices/08-exams-2015-2021-recit-entraide.json` · d3 boss 120/30 · 8 questions · régime **examen**

- Titre : « 🏛️ Concours 2015–2021 · préparer un récit : s'entraider, du début à la fin ⭐⭐⭐ »
- Registre : id `C06#12` ; sources `C06#12, C08#11, C12#10`
- Sources (base en premier) : C06 (2021) ex. 12 ; C08 (2019) ex. 11 ; C12 (2015) ex. 10
- Items :
  - 2021 : « Claire s'habitue au chat et elle s'en occupe convenablement. Un jour, on frappe à la porte ; c'est le propriétaire du chat. Écris un récit de huit phrases au moins pour raconter ce que fait Claire pour le chat et imagine le dialogue entre la fillette et le propriétaire. » — ordering des cinq temps (situation de départ, élément perturbateur « on frappe à la porte », actions, résolution, fin) ; QCM « quelle phrase est l'élément perturbateur » ; QCM des soins que Claire donne au chat — 3 q.
    - piège (étiquette à porter par un distracteur) : oublier le dialogue ou les soins — ligne C06#12 (d3)
  - 2019 : « … sa mère était mécontente de son comportement. Mais son père n'était pas d'accord avec elle et il a essayé de la convaincre de la nécessité d'aider les autres. Rédige un récit de huit phrases au moins … en intégrant un dialogue. » — QCM « quelle réplique est celle du père » ; multi « quelles répliques défendent l'aide aux autres » — 2 q.
    - piège (étiquette à porter par un distracteur) : oublier le dialogue ou le point de vue du père — ligne C08#11 (d3)
  - 2015 : « François parle à ses parents de la misère du petit aveugle. Les parents décident, eux aussi, d'aider ce garçon pauvre et handicapé. Rédige un récit de huit phrases au moins pour raconter ce qui s'est passé. (Ton récit doit intégrer un court dialogue.) » — ordering de la progression (parler, décider, agir) ; QCM d'une phrase de fin qui montre l'aide — 3 q.
    - piège (étiquette à porter par un distracteur) : oublier le dialogue ou la progression du récit — ligne C12#10 (d3)
- Ne pas redemander : `04/02-boss#3`, `04/02-boss#4`, `04/04-defi#4`, `04/05-entrainement#1`, `04/05-entrainement#4`
- Note : Archétype « raconter une aide, avec la progression des cinq temps ». Le piège récurrent des lignes est d'oublier la progression du récit. Pas de mission de lecture au `04` : le texte d'examen de 2021 (chat adopté) est écarté (décision à soumettre E1).

