# Étude 35 — Comprendre la théorie : chaque notion arrive par le concret, se montre par l'exemple, se fixe par la règle et se vérifie sur place (pilote maths 9ᵉ)

> **Statut** : **en exécution** — écrite ET **validée le 2026-09-16** (Q-1…Q-6 arbitrées le même
> jour, toutes sur la recommandation, §7). **Lots 1 et 2 LIVRÉS** le 2026-09-16 (§8) ; restent la
> campagne (lots 3 à 6), la mesure (lot 7, au premier trafic) et le bilan (lot 8).
> **Priorité** : 35 · **Valeur** : 📖 l'élève de 9ᵉ qui lit une leçon **comprend** la notion au lieu
> de la recevoir — parce qu'elle arrive par une situation qu'il connaît, se montre dans un exemple
> résolu qui dit _pourquoi_ chaque étape, se distingue d'une erreur typique, se fixe en règle, et
> se vérifie **sur place**, avant le quiz. Le cours cesse d'être un manuel qui _énonce_ pour devenir
> un professeur qui _explique_ · **Complexité** : moyenne (un bloc moteur, une doctrine, une
> campagne de 19 cours)
> **Architecte** : Fable / 2026-09-16 · **Exécuteur cible** : Sonnet (ou équiv.) pour le lot
> moteur ; les skills `content-cours` (+ `prof-math-9eme` pour les erreurs typiques) et
> `content-audit` pour les lots de contenu
> **Dépend de** : é18 (livrée — blocs typés, figures, gate ouvert aux leçons : **c'est l'appareil
> que cette étude fait enfin servir au savoir**), é21 (livrée — R-8 « tout encadré du manuel
> devient un bloc », appliquée à sa seule matière pilote `physique-1ere-sec`), é04/é30 (registre
> `content/misconceptions.json`, 241 tags, dont **1 367 posés sur les distracteurs de maths 9ᵉ**),
> suivi parental quotidien (`learning_pulses`, surface `lesson`, depuis le 2026-08-16) ·
> **Bloque** : rien. Informe **é23 lot 5** (même matière pilote, fichiers disjoints : les vidéos
> vivent dans `chapter.json`/`videos.json`, jamais dans `cours.md`) et la campagne de fond des
> cours (§4, après le pilote)
> **Docs normatifs liés** : AGENTS.md, `docs/doctrine-verticale.md`, `docs/xss-rendering-policy.md`,
> `docs/content-voice-and-composition.md`, `METHODE-GENERATION-CONTENU.md`,
> `content-engine/references/{course-quality,style-guide,course-figures,math-and-notation,content-schema}.md`
>
> **Fiche de verticalité** (é26 D-2) :
> **Verticale** : V1 « apprendre & maîtriser » — **approfondissement** de la capacité « lecteur de
> cours » (é18, publique, anonyme compris ; STATUS §3 « catalogue → cours → pratique corrigée »,
> 🟢 M2). Aucune surface nouvelle : un seul type de bloc s'ajoute à une grammaire qui en a huit ·
> **Maturité visée** : **M3** (le plancher de tout ce qui est LIVE — le cours n'est pas une capacité
> signature ; les trois signatures restent correction-révision, tuteur, examen blanc) ·
> **Boucles** : REFERME (a) l'appareil de blocs de é18, livré le 2026-07-14 et **presque inutilisé
> pour le savoir** — sur les 20 cours de maths 9ᵉ : 54 `::: figure`, 1 `::: methode`, **zéro**
> `definition`, `propriete`, `exemple`, `retenir` ; (b) la transcription officielle du manuel de
> 9ᵉ (11 530 lignes, 13 chapitres, 57 activités « نشاط », 7 exercices corrigés « تمرين مرفق بحل »),
> lue aujourd'hui pour le **périmètre** et jamais pour la **séquence pédagogique** qu'elle porte ;
> (c) le registre des misconceptions, qui étiquette les distracteurs des exercices et **n'entre
> dans aucun cours** ; (d) `learning_pulses` (temps et profondeur de lecture), qui n'alimente que
> le rapport parent — le lot 7 le relie enfin au résultat du quiz. OUVRE : un type de bloc
> (`verifie`), consommé par le lecteur (lot 1) et par le gate (lot 1) dès sa livraison ; **aucune
> donnée nouvelle n'est collectée** ·
> **Apport IA** : **retenu, hors ligne** (P-5c) — les cours sont écrits par les skills sous gates,
> audit à l'aveugle et revue humaine ; c'est le modèle qui rédige l'ancrage, l'exemple, l'erreur
> typique et la règle, dans un cadre fermé (§2). **À l'exécution : rien de nouveau** — le tuteur
> (é11) et la Forge (é29) sont déjà montés sous le lecteur ; « explique-moi ce bloc autrement /
> avec un autre exemple », ancré sur le bloc lu, est un candidat **pour é11**, noté et non ouvert
> ici (P-7).

---

## 1. Contexte & objectif produit

### 1.1 La demande

> « Je veux faire une étude sur comment rendre les notions théoriques du cours compréhensibles
> facilement avec illustration des exemples pratiques. Cette étude focalise uniquement sur la
> partie cours, et le pilote c'est la matière mathématique de la classe 9ᵉ année. Utilise les
> méthodes pédagogiques les plus avancées en 2026, prouvées par les études et les
> expérimentations. » — Mohamed, 2026-09-16

Trois bornes sont posées par la demande elle-même, et l'étude les tient : **le cours seul**
(`cours.md`, avec `resume.md` pour son miroir — jamais les quiz, exercices, Rappel, vidéos) ;
**un pilote**, maths 9ᵉ (`content/math`, arabophone, l'année du concours national) ; **des
méthodes prouvées**, c'est-à-dire des méta-analyses et des essais contrôlés, pas des modes
(annexe A — chaque méthode retenue porte sa source vérifiée et sa taille d'effet ; chaque mode
écartée porte le motif).

### 1.2 L'état réel, mesuré (2026-09-16, `main` des deux dépôts)

Cinq constats. Ils se lisent ensemble : l'appareil existe, la règle existe, le manuel montre le
chemin, et pourtant le cours **énonce** au lieu d'**expliquer** — parce que rien, ni doctrine
précise, ni gate, ni mesure, ne demande autre chose.

**Constat A — l'appareil de é18 existe, et le savoir ne s'en sert pas.** Le lecteur rend huit
types de blocs (`definition` · `propriete` · `exemple` · `methode` · `figure` · `piege` · `astuce`
· `retenir`, `src/shared/lib/lesson-blocks.ts`) et promeut quatre callouts emoji. Ce que les 20
cours de maths 9ᵉ en font (annexe B, mesuré sur `content/math/*/cours.md`) :

| appareil disponible                                                         | employé dans maths 9ᵉ       |
| --------------------------------------------------------------------------- | --------------------------- |
| `::: figure` (é18 lot 5, campagne géométrie)                                | **54** (56 `<svg>`)         |
| `::: methode`                                                               | **1** (`19-valeur-absolue`) |
| `::: definition` · `propriete` · `exemple` · `retenir` · `piege` · `astuce` | **0 · 0 · 0 · 0 · 0 · 0**   |
| callouts promus `> ⚠️` · `> 🗡️` · `> 💡` · `> 🏆`                           | 57 · 44 · 29 · 22           |

Le corpus entier dit la même chose : é21 (§8, 2026-09-06) comptait **362 `figure` contre 26 blocs
de savoir**, et sa passe R-8 n'a touché que `physique-1ere-sec` (27 blocs). Au 2026-09-16,
`::: definition` existe dans **17 cours sur 773** (12 de physique 1ʳᵉ sec, 4 de technologie bac,
1 de philosophie), `::: exemple` dans **2**. L'« exemple résolu » — le bloc dont l'étude 18 disait
qu'il est « explicite ou n'en est pas un » (D-1, R-5) — n'a **jamais été écrit** en maths.

**Constat B — la règle « concret avant abstrait » est écrite, pas appliquée, et rien ne la
vérifie.** `course-quality.md` axe 2 pose en une ligne « _Concrete before abstract. Open each
notion with a concrete example or familiar situation, then state the general rule_ » et « _Every
rule has a worked example_ ». Lu sur le corpus pilote :

- `06-fonctions-lineaires-affines` (138 lignes, 7 sections, **zéro bloc de savoir**) ouvre par la
  définition formelle — « الدالة الخطية هي كلّ دالة تكتب على الشكل f(x) = a × x » — puis aligne
  définition, propriété, tableau, tracé. La seule situation concrète du chapitre (le taxi :
  2 dinars + 0,8 dinar/km) arrive **ligne 121 sur 138**, après toutes les règles, comme
  « exemple d'application ». L'ordre est exactement l'inverse de celui que la barre prescrit.
  Aucun **non-exemple** (f(x) = x² n'est pas linéaire), aucune **erreur typique** montrée et
  corrigée, aucun « pourquoi » sur « même coefficient ⟺ parallèles », et la figure, présente,
  n'est pas reliée par le texte à la formule qu'elle illustre.
- `02-racines-carrees` (82 lignes) fait mieux — l'ancrage « le côté du carré d'aire 9 » est dans
  la figure, le contre-exemple √(9 + 16) ≠ √9 + √16 est là — mais le rationalisation du
  dénominateur est une formule suivie d'un calcul, sans exemple jumeau à faire, sans contrôle.

Le gate `auditLesson` (`scripts/content/qa-checks.ts`, é18 lot 4) vérifie cinq choses
structurelles : directive inconnue ou non fermée, figure sans légende, prose qui désigne une
figure absente, chapitre spatial sans figure, plus la notation. **Rien sur l'ordre d'explication,
rien sur la présence d'un exemple après une règle.** Le skill `content-audit` re-résout les
exemples (justesse) et note l'axe 2 en une ligne — un jugement, pas une grille.

**Constat C — le manuel officiel raconte une séquence que l'app saute.** La transcription
`content/programmes-officiels/programme/9eme-base/maths.md` (11 530 lignes, les 13 chapitres du
manuel CNP 102905, lus page à page) montre la séquence **du manuel lui-même**, chapitre après
chapitre : **أستحضر** (rappel des acquis) → **نشاط** (activité concrète : une situation, une
question) → **encadré** (la règle, verbatim) → **أطبق** (application immédiate) → **تمرين مرفق
بحل** (exercice corrigé) → **أحوصل** (bilan). Comptés dans la transcription : **57** activités
« نشاط », **7** exercices corrigés, et des encadrés dans chacun des 13 chapitres. Les cours de
l'app **commencent à l'encadré** : ils reprennent la règle et sautent l'activité qui la fait
naître et l'exercice corrigé qui la fait comprendre. Ce que cette étude installe n'est donc pas
une pédagogie importée : c'est la séquence officielle, **rétablie**, et adossée à ce que la
recherche mesure (annexe A). Le skill `content-cours` lit déjà cette transcription (étape 1 de
son workflow) — pour le **périmètre**, jamais pour la **séquence**.

**Constat D — le contrôle immédiat n'existe pas, et ne peut pas être écrit.** Le renderer
(`src/shared/lib/markdown.ts`, ~15 passes regex, sous-ensemble fermé) n'émet ni `details` ni
`summary`, ni aucun élément dépliable ; la liste `ALLOWED_TAGS` ne les connaît pas. Un cours est
**100 % statique** ; le quiz de compréhension est une route à part. Le couple « exemple résolu →
problème jumeau à faire soi-même » — le résultat le plus robuste de la théorie de la charge
cognitive (annexe A, § A.1) — n'a **aucune syntaxe** pour exister dans une leçon.

**Constat E — rien ne relie la lecture au résultat.** `learning_pulses` (migration
`20260816180000`, surface `lesson`, `active_seconds`, `progress_pct`) sait depuis le 2026-08-16
combien de temps un élève **connecté** a lu et jusqu'où ; le rapport parent en déduit « étudié »
(≥ 120 s et ≥ 60 %). `attempts` sait le score du quiz au premier essai. **Aucune vue ne les
joint**, aucun événement produit ne concerne le cours (14 événements PostHog, aucun de lecture),
et **un lecteur anonyme ne laisse rien**. Enfin le trafic : **5 élèves actifs** sur la semaine
relevée (scorecard STATUS §1bis, 2026-09-03). Toute « preuve d'apprentissage » sur ce volume
serait une fiction ; l'étude le dit (P-6) : la preuve du pilote est un **audit à l'aveugle sur
grille**, et la mesure est **armée** pour le jour où le trafic la rend lisible.

### 1.3 Objectif produit

Qu'un élève de 9ᵉ qui lit une leçon de maths dans l'app en ressorte en **ayant compris** chaque
notion théorique — pas seulement en l'ayant lue. Concrètement, pour chaque notion (définition,
propriété, théorème, méthode), le cours :

1. la fait **naître d'une situation concrète** que l'élève connaît, et de la question qu'elle
   pose (le taxi, le carré d'aire 2, l'ombre du poteau — les activités du manuel d'abord) ;
2. la **nomme** avec le vocabulaire officiel, et l'écrit dans sa notation, seule sur sa ligne ;
3. la **montre** — figure, droite graduée, tableau de valeurs — en disant ce qu'il faut y voir ;
4. la **résout sur un exemple**, étape par étape, chaque étape avec son _pourquoi_ ;
5. la **distingue de l'erreur typique** que les élèves commettent (celle que les distracteurs
   des exercices encodent déjà), montrée puis corrigée ;
6. l'**énonce en règle générale**, après l'exemple, avec ce qui varie et ce qui ne varie pas ;
7. la **vérifie sur place** : un problème jumeau, réponse repliée, à tenter avant de lire.

C'est le **patron de notion** (§2.1). Le résumé en est le miroir (une carte par notion, celle du
« à retenir »). Tout le reste — quiz, exercices, Rappel, vidéos, tuteur — est inchangé.

### 1.4 Indicateurs de succès (P-6 — mesurés, ou dits « dette »)

| KPI                                                                                  | avant (2026-09-16)                             | cible (fin du pilote)                                                                                                    |
| ------------------------------------------------------------------------------------ | ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| Sections théoriques de maths 9ᵉ conformes au patron (audit à l'aveugle, grille §2.4) | 0 / 148 (153 sections moins les 5 des annales) | **100 %** des 19 chapitres                                                                                               |
| Blocs de savoir (`definition` · `propriete` · `methode`) dans `content/math`         | 1                                              | ≥ 1 par section théorique ; **100 % des encadrés du manuel** (é21 R-8)                                                   |
| Exemples résolus typés (`::: exemple`)                                               | 0                                              | ≥ 1 par règle, chacun avec ses _pourquoi_                                                                                |
| Contrôles sur place (`::: verifie`)                                                  | 0 — la syntaxe n'existe pas                    | ≥ 1 par section théorique                                                                                                |
| Erreurs typiques montrées et corrigées, ancrées sur un tag du registre               | 0                                              | ≥ 1 par chapitre (19), chacune citant son `misconceptionTag`                                                             |
| Contrôles mécaniques du patron dans `content:qa`                                     | 0                                              | 6 (§3.5), `[error]` sur `math`, `[warn]` ailleurs                                                                        |
| Réussite du quiz au 1ᵉʳ essai après lecture « étudiée », par chapitre                | **non calculable** (aucune jointure)           | vue `lesson_to_quiz_outcome` + bloc `/admin/engagement` (lot 7) — **dette** tant que < 30 lectures étudiées par chapitre |

### 1.5 Ce que l'étude ne cherche PAS à faire

- **Pas de touche aux questions.** Quiz, exercices, Rappel, donjon, duel : inchangés. Si la
  réécriture d'un cours révèle qu'un item teste une notion hors cours, le lot le **signale**
  (rapport de PR) et ne l'édite pas — c'est le territoire de `content-audit`/`content-engine`.
- **Pas de rendu mathématique** (KaTeX/MathJax). Les formules restent de l'Unicode brut isolé
  LTR (`math-and-notation.md`) ; é18 l'a déjà écarté et rien ici ne le rouvre.
- **Pas de cours interactif.** Aucun JavaScript dans le contenu, aucun item de quiz incrusté,
  aucun widget : un seul élément HTML dépliable (`<details>`), inerte, pour le contrôle sur place
  (D-2). Le contenu porte du **sens**, l'app possède le markup (é18 D-2).
- **Pas d'IA à l'exécution.** Rien de nouveau sous le lecteur ; le candidat « explique autrement »
  est noté pour é11 (fiche).
- **Pas de vidéo, pas de photo.** é23 lot 5 reste une campagne à part sur les mêmes chapitres ;
  SVG seul pour les figures (é18 D-8).
- **Pas d'autre matière dans l'étude.** Le pilote est `math` 9ᵉ, 19 chapitres (le 20ᵉ,
  `14-annales-sujets-types`, n'a pas de théorie). L'extension est une campagne, matière par
  matière, décidée en Q-5 sur le bilan du pilote — « profondeur de génération ».
- **Pas de réécriture du résumé au-delà du miroir.** Une carte par notion, celle du `retenir` ;
  la bijection résumé ↔ cours (`course-quality.md` axe 3) est conservée, pas réinventée.

---

## 2. Spécification fonctionnelle

### 2.1 Le modèle en une image — le patron de notion, en sept temps

Une **notion** est ce que le programme nomme et que le quiz teste : une définition (الدالة
الخطية), une propriété ou un théorème (مبرهنة طالس), une méthode (إنطاق المقام), une formule.
Une section `##` = une notion (axe 1, inchangé). À l'intérieur, l'ordre est **fermé** :

| temps  | ce que l'élève vit                                                                              | bloc / forme                                                                                                                                                         | preuve principale (annexe A)                                                                                                 |
| ------ | ----------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| **T1** | **Ancrer** — une situation qu'il connaît, et **la question** qu'elle pose                       | prose, 2-4 lignes, se termine par la question ; figure d'ancrage si la situation est visuelle                                                                        | multimédia (g = 0,39), pré-question ciblée (g ≈ 0,54-0,66 sur la notion visée, ≈ 0 ailleurs), concret → abstrait (Fyfe 2014) |
| **T2** | **Nommer** — le mot officiel, la notation, seule sur sa ligne                                   | `::: definition` (ou `::: propriete` quand la notion est un énoncé)                                                                                                  | pré-entraînement du vocabulaire ; « petites étapes » (Rosenshine)                                                            |
| **T3** | **Voir** — une représentation, et la phrase qui la relie aux symboles                           | `::: figure` (obligatoire si spatial, é18) · tableau de valeurs · droite graduée · modèle en barres                                                                  | texte + figure intégrés (g = 0,63), signalement (g = 0,52), représentations **reliées** (Rau 2017, GTI 2020)                 |
| **T4** | **Résoudre** — l'exemple, étape par étape, chaque étape avec **son pourquoi** en une demi-ligne | `::: exemple` — 2 à 5 étapes numérotées ; le **premier** exemple reprend les nombres de T1                                                                           | exemples résolus (g = 0,48), exemple → problème (van Gog 2011), étiquette de principe par étape (Atkinson 2003)              |
| **T5** | **Distinguer** — l'erreur typique, montrée, diagnostiquée, corrigée                             | `::: piege الخطأ الشائع` — l'étape fausse, **pourquoi** elle tente, la bonne étape ; cible un tag du registre                                                        | exemples erronés **contrastés** après un exemple correct (Booth 2013, McLaren 2015, revue Dieterich 2025)                    |
| **T6** | **Généraliser** — la règle, après l'exemple, avec ce qui varie et ce qui ne varie pas           | `::: propriete` / `::: methode` (étapes numérotées) + 2-3 cas courts dont **un cas limite**                                                                          | ordre concret → règle ; grammaire de variation (Marton — grammaire de conception, pas d'effet mesuré)                        |
| **T7** | **Vérifier** — sur place, avant de continuer                                                    | `::: verifie` — un exemple **à compléter** (l'étape porteuse du principe est laissée blanche) ou un problème jumeau ; réponse **repliée**, qui redit le raisonnement | rappel avec feedback (g = 0,50 ; 0,54 avec feedback), exemples estompés (Renkl 2002/2004, Miller-Cotto & Medrano 2026)       |
| fin    | **Retenir** — une ligne                                                                         | `::: retenir` — miroir de la carte du résumé                                                                                                                         | résumé en une phrase (d ≈ 0,5, Lawson & Mayer 2024)                                                                          |

Tous les temps ne sont pas obligatoires pour toutes les notions ; **l'ordre, lui, l'est**.

| type de notion       | temps obligatoires                            | temps recommandés | interdit                                                                   |
| -------------------- | --------------------------------------------- | ----------------- | -------------------------------------------------------------------------- |
| définition           | T1 · T2 · T4 · T7 · retenir                   | T3 · T5           | T2 avant T1 (la définition n'ouvre jamais la section)                      |
| propriété / théorème | T1 · T3 (si spatial) · T4 · T6 · T7 · retenir | T5                | T6 avant T4 (la règle générale n'arrive jamais avant son exemple)          |
| méthode / procédure  | T1 · T4 · T6 (`methode`) · T7 · retenir       | T5                | T1 sous forme de « défi » : une procédure s'explique d'abord (Ashman 2020) |
| formule              | T1 · T2 · T4 · T7                             | T3 · T5           | formule dans la phrase (une formule, une ligne — `math-and-notation.md`)   |

> **Pourquoi cet ordre et pas un autre.** Il est celui du manuel (نشاط → encadré → أطبق → تمرين
> مرفق بحل, constat C) et celui que les méta-analyses soutiennent pour des **novices** sur une
> notion nouvelle — et un élève de 9ᵉ est novice sur chaque notion qu'il découvre, année de
> concours ou pas (Tetzlaff 2025 : l'assistance forte gagne d = 0,51 chez les novices, et perd
> d = −0,43 chez ceux qui savent déjà — d'où le résumé en cartes, qui sert la révision sans
> réexpliquer). Ce que l'étude **refuse** délibérément, parce que la preuve dit non ou pas
> encore : les invites de réflexion génériques (nulles sur 1 005 élèves de 7ᵉ, L@S 2025), deux
> méthodes côte à côte au premier contact (pire que l'étude séquentielle chez les novices,
> Rittle-Johnson 2009 ; nul à l'échelle, Star 2015), l'entrelacement dans le texte (≈ 0 sur du
> texte expositif, Brunmair & Richter 2019 — il vit déjà dans le Rappel), le dessin à faire par
> l'élève (nul en ligne sans entraînement, Lawson & Mayer 2024), et toute variante « visuel /
> verbal » par style d'apprentissage (mythe, Pashler 2008).

### 2.2 Analyse comparative — quel vecteur pour le patron ?

| option                                                          | ce qu'elle donne                                                  | verdict                                                                                                                                                               |
| --------------------------------------------------------------- | ----------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **A — statu quo + plus de figures**                             | des cours plus illustrés, toujours énoncés avant d'être expliqués | rejeté : é18 l'a fait ; l'illustration seule ne crée ni l'ancrage, ni l'exemple, ni le contrôle                                                                       |
| **B — le patron en contenu seul, sans lot moteur**              | T1-T6 et `retenir` avec les 8 blocs existants ; pas de T7         | rejeté comme cible, **retenu comme repli** (Q-1) : sans T7, le couple exemple → problème — le résultat le plus solide de tout le corpus de preuves — reste impossible |
| **C — le patron + un bloc `verifie` dépliable (`<details>`)**   | les sept temps ; un élément HTML inerte de plus, aucun script     | **retenu** (D-1, D-2) : le coût moteur est un lot court, la surface XSS n'entre aucun attribut, l'impression et le RTL sont gérés                                     |
| **D — cours interactif** (items de quiz incrustés, widgets, JS) | contrôle riche, scoring dans le cours                             | rejeté : le quiz existe déjà comme porte du chapitre (é22/é34) ; du code dans le contenu casse é18 D-2 ; coût et surface sans preuve d'un gain sur le statique        |
| **E — réexplication IA à l'exécution** (« explique autrement ») | reformulation adaptée, ancrée sur le bloc                         | **différé vers é11** (P-7) : la seule forme d'IA qui a tenu à l'examen est le tuteur à garde-fous (Bastani 2025) — c'est un tuteur, pas un cours                      |

### 2.3 Acteurs & user stories

Le lecteur de cours est **public** (anonyme compris) ; tout vaut pour l'anonyme comme pour l'élève
connecté, sauf la mesure (E), qui ne voit que les connectés.

- **US-1** — En tant qu'élève de 9ᵉ, quand j'aborde une notion, je **commence par une situation
  que je connais** et par la question qu'elle pose, pas par une définition.
- **US-2** — En tant qu'élève, je lis **un exemple résolu où chaque étape dit pourquoi** elle est
  permise, avec les mêmes nombres que la situation de départ.
- **US-3** — En tant qu'élève, je vois **l'erreur que je risque de faire**, pourquoi elle tente, et
  comment la corriger — avant de la commettre au quiz.
- **US-4** — En tant qu'élève, je peux **vérifier sur place** que j'ai compris : un exemple à
  compléter, la réponse cachée tant que je ne l'ai pas demandée, et une réponse qui redit le
  raisonnement, pas seulement le résultat.
- **US-5** — En tant qu'élève arabophone, la prose est en arabe RTL, les formules et les étiquettes
  restent LTR en notation standard, et le libellé « جرّب بنفسك » / « أظهر الإجابة » suit la langue
  du contenu (é18 R-8).
- **US-6** — En tant qu'élève qui révise, le **résumé** me donne une carte par notion, la ligne
  « à retenir » — sans réexpliquer (le résumé sert celui qui sait déjà).
- **US-7** — En tant qu'élève qui imprime, les réponses des blocs « vérifie » sont **dépliées** à
  l'impression (le cours imprimé est complet).
- **US-8** — En tant qu'auteur (`content-cours`), je dispose d'un **gabarit par type de notion**,
  des règles R-1…R-22, et je lis la transcription du manuel pour ses activités, pas seulement
  pour son périmètre.
- **US-9** — En tant qu'auditeur (`content-audit`), je note chaque section sur la **grille du
  patron** (§2.4, « Audit ») et je re-résous chaque exemple, chaque erreur typique et chaque
  contrôle.
- **US-10** — En tant que propriétaire, je lis sur `/admin/engagement`, par chapitre, la réussite
  du quiz au premier essai après une lecture étudiée — et une mention honnête du volume.

### 2.4 Règles métier

**Le patron (contenu)**

- **R-1 — Une section, une notion, les sept temps dans l'ordre** (§2.1). Les temps obligatoires
  dépendent du type de notion ; l'ordre ne dépend de rien.
- **R-2 — L'ancrage est une question, pas un décor.** T1 pose une situation **et la question**
  que la notion va résoudre (« combien paie-t-on pour x kilogrammes ? »). Un T1 qui n'aboutit à
  aucune question est une fioriture (cohérence : les détails séduisants coûtent, g négatif —
  annexe A). La situation vient **d'abord des activités du manuel** (transcription, « نشاط »),
  réécrite — jamais recopiée (garde anti-verbatim de `content:qa`) ; à défaut, du quotidien
  tunisien de l'élève (prix, distances, ombres, factures, notes).
- **R-3 — Les mêmes nombres traversent T1 → T3 → T4.** L'estompage du concret se fait sur une
  seule histoire : le taxi de T1 devient le tableau de T3 et l'exemple de T4, avant que T6
  n'écrive f(x) = ax + b. Deux exemples par règle au minimum : **un habillé** (la situation),
  **un nu** (mathématique pur), dans cet ordre.
- **R-4 — Chaque étape d'un exemple porte son pourquoi**, en une demi-ligne, sous forme
  d'étiquette de principe (« لأنّ الصورة هي الثمن المقابل للكمية ») — jamais un paragraphe. Pas
  d'invite ouverte (« explique pourquoi ») sans réponse : les invites d'auto-explication sans
  feedback dégradent l'effet des exemples en maths (Barbieri 2023).
- **R-5 — L'erreur typique vient après un exemple correct, jamais avant.** Elle est **nommée**
  comme erreur dès sa première ligne, montre l'étape fausse, dit pourquoi elle tente, puis la
  bonne étape. Elle cible une **misconception du registre** que les distracteurs du chapitre
  encodent (`misconceptionTag`), et le `chapter.json` la déclare (`coursePitfalls`, §3.5 C-5).
  Une erreur non corrigée dans le texte, ou reprise dans le résumé, est une non-conformité
  bloquante.
- **R-6 — La règle générale arrive après son exemple**, et avec **un cas limite** (b = 0, a < 0,
  le dénominateur nul, l'égalité) : ce que le programme fait tester, le cours l'a montré (axe 3).
- **R-7 — Une seule méthode au premier contact.** Deux méthodes se présentent **l'une après
  l'autre**, jamais côte à côte dans la section qui introduit la première (Rittle-Johnson 2009).
  La comparaison a sa place dans une section de synthèse, quand les deux sont acquises.
- **R-8 — Le contrôle est un exemple à compléter ou un problème jumeau**, jamais une notion
  nouvelle. Sa réponse **redit le raisonnement** (l'étape et son pourquoi), pas seulement le
  résultat. Un par section théorique, deux au plus. Pour une procédure, l'étape laissée blanche
  est **celle qui porte le principe** (Renkl 2004), pas mécaniquement la dernière.
- **R-9 — Le « à retenir » tient en une ligne** et devient la carte du résumé (bijection, axe 3).
- **R-10 — Le texte reste dans le registre du cours.** Le RPG vit dans le titre `#`, l'épigraphe
  `> 💡` et la clôture `> 🏆` (style-guide) ; **aucun** élément narratif ou décoratif dans les
  blocs T2-T7 (cohérence). Une phrase qui redit ce que la figure montre est supprimée (redondance).
- **R-11 — Représentation reliée.** Toute figure, tableau ou droite graduée de T3 est suivie
  d'**une phrase de pont** qui nomme la correspondance (« la pente de la droite est le a de la
  formule » ; « القطعة AB في الشكل هي a في الصيغة »). Les étiquettes sont **dans** la figure, à
  côté de l'élément, jamais en légende séparée ; le nom d'un objet est **le même** dans le texte,
  la figure et la formule (signalement).
- **R-12 — Une notion nouvelle par section, et une seule ; un bloc tient en 3 à 6 lignes** hors
  étapes numérotées (segmentation). Une section qui dépasse 60 lignes se scinde.
- **R-13 — Budget par notion, pas par cours.** Une section théorique fait 18 à 40 lignes. Un cours
  de 6 notions fait donc 110 à 240 lignes — c'est le budget réel du corpus pilote (82 à 331 lignes
  aujourd'hui), pas les « 50-75 lignes » du style-guide, morts depuis longtemps (D-6). Un cours
  qui dépasse 240 lignes se scinde en deux chapitres — décision humaine, jamais silencieuse.
- **R-14 — Vocabulaire officiel, notation standard, RTL.** Termes du manuel (table « Vocabulaire
  & terminologie officielle » de la transcription), chiffres occidentaux, formules LTR seules sur
  leur ligne, U+00A0 dans les nombres groupés, virgule décimale « 0,8 » — tout `math-and-notation.md`
  s'applique ; rien ici ne l'assouplit.
- **R-15 — Ce qui n'est pas au programme n'entre pas** (axe 3). Le patron n'ajoute jamais une
  notion, il explique celles qui y sont. Un glossaire de termes français en fin de cours est une
  **décision produit** (Q-4), pas une notion.

**Le bloc `verifie` (moteur)**

- **R-16 — Grammaire.** `::: verifie[ <titre libre>]` … `---` … `:::`. Les lignes **avant** le
  premier `---` seul sur sa ligne sont la question (markdown ordinaire, formules `$$` comprises),
  les lignes **après** sont la réponse. Le titre libre est facultatif.
- **R-17 — Fail-safe (é18 R-7 étendu).** Un `verifie` sans séparateur, ou dont l'un des deux côtés
  est vide, est rendu en **bloc neutre** (tout visible, rien de replié) et remonté `[error]` par
  `content:qa`. Le renderer ne jette jamais.
- **R-18 — La réponse est repliée par défaut** dans un `<details>` natif (aucun script) ; le
  libellé du bouton et celui du bloc suivent la **langue du contenu** (é18 R-8) : fr « À toi » /
  « Voir la réponse », en « Your turn » / « Show the answer », ar « جرّب بنفسك » / « أظهر الإجابة ».
- **R-19 — Impression.** Le bouton Imprimer du lecteur **déplie** tous les `details` avant
  `window.print()` et les replie après (US-7). Un `Ctrl+P` direct imprime l'état courant — assumé.
- **R-20 — Sécurité.** `ALLOWED_TAGS` gagne `details` et `summary`, **aucun attribut nouveau**
  (`ALLOWED_ATTR` inchangé ; pas de `open`). Le corps reste échappé avant émission (é18 R-1) ;
  `sanitizeSvg` n'est pas touché (é18 R-2). Les tests XSS existants passent **sans modification**.
- **R-21 — Hors leçon, rien.** `verifie` n'existe pas dans `resume.md` (le résumé ne pose pas de
  question : il sert la révision) ni dans un champ de question. Le renderer du résumé l'ignore
  (bloc neutre) et le gate le remonte `[error]`.

**Le gate et l'audit**

- **R-22 — Le déterministe vérifie la forme, le modèle juge le fond** (D-7). `content:qa` porte
  six contrôles structurels C-1…C-6 (§3.5) — ordre, présence, séparateur, budget — et **aucun
  reniflage de prose** (é18 D-1). `content-audit` note chaque section sur la grille ci-dessous
  et **re-résout** chaque exemple, chaque erreur typique et chaque contrôle.

**Grille d'audit du patron** (`content-audit`, axe 2 « Facilité de compréhension », remplace la
ligne unique actuelle) — sévérités alignées sur `course-quality.md` :

| constat                                                                                                 | sévérité      |
| ------------------------------------------------------------------------------------------------------- | ------------- |
| exemple, erreur typique ou contrôle **faux** (résultat, étape, diagnostic)                              | **[BLOCKER]** |
| erreur typique non signalée comme erreur, ou non corrigée, ou reprise dans le résumé                    | **[BLOCKER]** |
| section théorique qui ouvre sur la définition / la règle (T2 ou T6 avant T1)                            | **[MAJOR]**   |
| règle sans exemple résolu ; exemple sans ses pourquoi ; contrôle absent d'une section théorique         | **[MAJOR]**   |
| erreur typique sans tag du registre, ou sur une misconception qu'aucun distracteur du chapitre n'encode | **[MAJOR]**   |
| deux méthodes côte à côte au premier contact ; notion nouvelle introduite dans un contrôle              | **[MAJOR]**   |
| représentation sans phrase de pont ; étiquette de figure qui diffère du nom dans le texte               | **[MINOR]**   |
| ancrage sans question ; décor narratif dans un bloc ; prose redondante avec la figure                   | **[MINOR]**   |
| bloc > 6 lignes de prose ; section > 60 lignes ; cas limite absent de la règle                          | **[MINOR]**   |

Verdict par chapitre : **ship** (aucun blocker, ≤ 1 major) ou **fix-first** — inchangé.

### 2.5 i18n

- **Libellés de blocs** : hors i18n de l'UI (é18 R-8, D-5). Table close étendue dans
  `src/shared/lib/lesson-blocks.ts` : `verifie` → fr « À toi » · en « Your turn » · ar « جرّب
  بنفسك » ; libellé du bouton de réponse : fr « Voir la réponse » · en « Show the answer » · ar
  « أظهر الإجابة ». Le test « aucun type sans libellé dans les 3 langues » couvre les deux.
- **Chrome du lecteur** : aucune clé nouvelle (le bouton Imprimer existe ; la note de volume de
  US-10 vit dans la console admin, qui est en français comme le reste des `/admin/*`).
- **RTL** : le `<details>` hérite du `dir` du conteneur ; le marqueur natif du `summary` se place
  du côté de départ de la ligne dans les deux sens (à vérifier au rendu, DoE 4 — pas seulement
  traduit).

### 2.6 Hors périmètre (v1)

- Un bloc « défi » d'échec productif (invention avant instruction) : le gain existe (g ≈ 0,36)
  mais **conditionnel** — fidélité au design, notions conceptuelles, jamais les procédures — et
  la phase d'invention demande une correction des tentatives que le statique ne fait pas. T1 en
  garde la partie sûre (la question posée avant la règle). Réexaminable après le pilote.
- Deux figures « en séquence » pour un processus (2-3 planches) : autorisé par la grammaire
  actuelle (plusieurs `::: figure`), pas normé ici.
- Le résumé : miroir seulement (R-9). Pas de « résumé écrit par l'élève » (impossible en statique).
- Les autres matières et les autres classes : après le pilote (Q-5), une matière par campagne.

---

## 3. Architecture technique (décisions fermées)

### 3.1 Modèle de données

**Aucune migration, aucune colonne.** `chapters.lesson_content` et `chapters.summary` restent
des `text` markdown. Deux champs **facultatifs** entrent dans le schéma zod du contenu
(`src/shared/content/schema.ts`), consommés par le gate **seulement** — ni émis en SQL, ni lus à
l'exécution (P-2 : une donnée sans consommateur ne se stocke pas) :

```jsonc
// content/<subject>/subject.json
{ "coursePattern": "notion" }            // enum clos, v1 = "notion" — durcit C-1/C-2/C-3/C-5 en [error]

// content/<subject>/<chapter>/chapter.json
{ "coursePitfalls": ["math.fonction.lineaire-additive-au-lieu-de-multiplicative"] }
//   identifiants du registre content/misconceptions.json, chacun porté par ≥ 1 distracteur du chapitre (C-5)
```

Le DoD §7 ne s'applique qu'au **lot 7** (une fonction SQL de lecture, additive, pgTAP).

### 3.2 Serveur

**Lots 1 à 6 : aucun changement.** Le lecteur consomme `getChapterLesson` (anonyme compris).

**Lot 7 — une fonction de lecture, pour l'admin.** `admin_lesson_to_quiz_outcome(p_subject text,
p_cutoff timestamptz)` — même garde et mêmes grants que `admin_engagement_overview` (é34 lot 3) :
`SECURITY DEFINER`, `is_admin` vérifié dans le corps, `REVOKE` de `anon`/`authenticated` sauf
l'`EXECUTE` que la console appelle. Elle retourne, **par chapitre** de la matière :

| colonne                | définition                                                                                                                                                                                                                                                       |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `chapter_id`, `title`  | —                                                                                                                                                                                                                                                                |
| `readers_studied`      | élèves connectés ayant une **lecture étudiée** du chapitre — `learning_pulses` surface `lesson`, somme `active_seconds` ≥ 120 **et** max `progress_pct` ≥ 60 (constantes du rapport parent, `20260816180100`) — **avant** leur premier essai du quiz du chapitre |
| `quiz_first_pass_rate` | parmi eux, part dont le **premier** `attempts` sur le quiz du chapitre franchit le seuil déjà central de la porte du quiz (`chapter_quiz_cleared`, arena#1005 — la constante n'est pas dupliquée)                                                                |
| `period`               | `before` / `after` `p_cutoff` — la date d'application de la version au patron (`content_releases` de la matière) ; la console passe la dernière par défaut                                                                                                       |
| `n_small`              | `true` si `readers_studied < 30` — la console **affiche le chiffre grisé** avec la mention « volume insuffisant » (P-6 : mesurer, pas prétendre)                                                                                                                 |

Aucune écriture, aucun événement nouveau. Un lecteur anonyme n'apparaît pas : c'est une limite
**dite** sur la console, pas contournée.

### 3.3 Client

**Le renderer — `src/shared/lib/markdown.ts`** (un type de bloc de plus dans le parser par lignes
de é18, aucune regex globale nouvelle) :

- la pré-passe reconnaît `verifie` comme les huit autres types ; pour ce type seul, elle scinde
  les lignes au **premier** `^---[ \t]*$` : `question: string[]`, `answer: string[]` (R-16) ;
- absence de séparateur, ou côté vide → `kind: "block", type: null` (bloc neutre, R-17) ;
- émission (R-18), les deux corps passant par les mêmes passes inline que tout bloc :

```html
<section class="lesson-blk lesson-blk--verifie">
  <span class="lesson-blk__label">جرّب بنفسك</span>
  <p class="lesson-blk__title">…titre libre, s'il existe…</p>
  <div class="lesson-check__question">…question rendue…</div>
  <details class="lesson-check">
    <summary class="lesson-check__toggle">أظهر الإجابة</summary>
    <div class="lesson-check__answer">…réponse rendue…</div>
  </details>
</section>
```

- `finalize` : `ALLOWED_TAGS` gagne **`details summary`** ; `ALLOWED_ATTR` **inchangé** (R-20) ;
- `renderSummary` : un `::: verifie` dans `resume.md` devient un bloc neutre (R-21) ;
- la passe `---` → `<hr>` ne voit jamais le séparateur d'un `verifie` : il est consommé par la
  pré-passe, avant l'échappement et les passes inline (l'ordre du pipeline é18 est conservé).

**`src/shared/lib/lesson-blocks.ts`** : `DIRECTIVE_TYPES` gagne `"verifie"` ; `BLOCK_LABELS.verifie`
et une table `REVEAL_LABELS: Record<ContentLang, string>` (§2.5) ; le test « table close complète »
couvre les deux.

**`src/features/quest/components/lesson-reader.tsx`** : le gestionnaire du bouton Imprimer
**ouvre** tous les `details` du conteneur, appelle `window.print()`, puis **restaure** leur état
(R-19). Rien d'autre : ni écouteur, ni état React — le dépliage est natif.

**`src/styles.css`**, section « Lesson content styling » : `.lesson-blk--verifie` (contour teinté
comme `methode`, bordure **pointillée** pour dire « à faire »), `.lesson-check` /
`.lesson-check__toggle` (curseur, graisse, marqueur natif conservé) / `.lesson-check__answer`
(filet supérieur `--border`). Couleurs **exclusivement** par tokens é14 ; `print:` n'a rien à
masquer de plus.

**Console admin (lot 7)** : un bloc « Cours → quiz » sur `/admin/engagement`, ajouté à la server
fn qui porte déjà `admin_engagement_overview` — aucune route nouvelle ; tableau par chapitre,
deux colonnes de période, chiffres grisés quand `n_small`. `build:check` fait partie du gate.

### 3.4 Le contenu — ce que le dépôt privé gagne (lot 2)

| fichier                                                         | changement                                                                                                                                                                                                                                                                                                           |
| --------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `content-engine/references/course-explanation.md` (**nouveau**) | la doctrine : les sept temps, R-1…R-15, les **gabarits par type de notion** (définition · propriété/théorème · méthode · formule) en **arabe et en français** — celui de l'annexe C en est la graine —, les anti-patrons, le condensé de preuves (annexe A, avec sa réserve de vérification), la check-list avant QA |
| `content-engine/references/course-quality.md`                   | l'axe 2 devient la **grille §2.4** (sévérités) ; la règle de longueur de l'axe 4 est remplacée par R-13 ; « Audit grading » suit                                                                                                                                                                                     |
| `content-engine/references/style-guide.md`                      | le squelette dit « 5-7 sections, **chacune écrite au patron de notion** (`course-explanation.md`) » ; les « ~50-75 lignes » disparaissent au profit de R-13                                                                                                                                                          |
| `content-engine/references/content-schema.md`                   | `verifie`, `coursePattern`, `coursePitfalls`                                                                                                                                                                                                                                                                         |
| `content-engine/SKILL.md`                                       | pointeur vers `course-explanation.md`, à côté de `course-figures.md`                                                                                                                                                                                                                                                 |
| `content-cours/SKILL.md`                                        | étape 1 : lire la transcription **pour ses activités (« نشاط ») et ses encadrés**, et lister les `misconceptionTag` du chapitre (`grep`) ; étape 3 : « écrire chaque section aux sept temps » ; étape 6 : la grille ; le rapport de fin liste `coursePitfalls` par chapitre                                          |
| `content-audit/SKILL.md`                                        | l'item 2 de l'audit de cours (« Ease of understanding ») devient la grille ; l'item 6 (passe factuelle) re-résout aussi erreurs typiques et contrôles ; lecture des résultats C-1…C-6                                                                                                                                |
| `METHODE-GENERATION-CONTENU.md`                                 | une ligne, à l'étape « cours » du LOT B, qui renvoie à la doctrine                                                                                                                                                                                                                                                   |

Aucun skill nouveau : `content-cours` écrit, `content-audit` juge, `prof-math-9eme` fournit sur
demande les erreurs typiques du chapitre à partir de ses propres distracteurs.

### 3.5 Le gate — six contrôles structurels (`scripts/content/qa-checks.ts`, `auditLesson`)

| #       | contrôle                                                                                                                                                                                                                                       | matière **sans** `coursePattern` | matière **avec** `coursePattern: "notion"` |
| ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- | ------------------------------------------ |
| **C-1** | « une règle, un exemple » — toute section `##` contenant un bloc `definition` / `propriete` / `methode` contient ≥ 1 bloc `exemple`                                                                                                            | `[warn]`                         | `[error]`                                  |
| **C-2** | « le concret d'abord » — dans une section, le premier bloc `definition` / `propriete` / `methode` est précédé d'au moins **2 lignes de prose** ou d'une `::: figure`                                                                           | `[warn]`                         | `[error]`                                  |
| **C-3** | « vérifie sur place » — toute section contenant un bloc `exemple` contient ≥ 1 bloc `verifie`                                                                                                                                                  | `[warn]`                         | `[error]`                                  |
| **C-4** | « la réponse est repliée » — un `verifie` a un séparateur `---` et ≥ 1 ligne non vide de chaque côté ; aucun `verifie` dans `resume.md`                                                                                                        | `[error]`                        | `[error]`                                  |
| **C-5** | « l'erreur est nommée » — le chapitre a ≥ 1 bloc `piege` (directive ou `> ⚠️` promu) ; chaque `coursePitfalls` existe dans le registre **et** est porté par ≥ 1 distracteur du chapitre ; un chapitre sous patron déclare ≥ 1 `coursePitfalls` | `[warn]` (tags : `[error]`)      | `[error]`                                  |
| **C-6** | « segmenter » — une section `##` de plus de 60 lignes                                                                                                                                                                                          | `[warn]`                         | `[warn]`                                   |

La liste `LESSON_DIRECTIVES` (miroir du renderer) gagne `verifie` ; le test de synchronisation
avec `DIRECTIVE_TYPES` le garantit. **Aucun** contrôle ne lit la prose (D-7) : C-2 compte des
lignes, il ne juge pas qu'elles sont « concrètes » — c'est l'affaire de l'audit.

**Sur le corpus du jour** (773 cours), le lot 1 ne fait rougir aucun gate : aucune matière ne
porte `coursePattern`, aucun `verifie` n'existe, et C-1/C-2/C-3/C-5/C-6 sortent en `[warn]` —
**budgéter la lecture de ces warns** dans le rapport du lot (D-7 de é18 : attendre des
découvertes). Le durcissement en `[error]` se fait **matière par matière**, au dernier lot de sa
campagne (é18 R-13, même mécanique).

### 3.6 Sécurité & anti-abus

- Le corps reste **échappé avant émission** (é18 R-1) ; deux balises inertes de plus, aucun
  attribut : la surface d'injection est inchangée (R-20). `sanitizeSvg` n'est pas touché.
- `coursePitfalls` est une liste d'identifiants **validés contre le registre** — jamais du texte
  libre, jamais rendu.
- Le cours reste du contenu **public** ; aucune clé de réponse n'y transite : la « réponse » d'un
  `verifie` est celle d'un exemple du cours, pas celle d'une question notée.
- La fonction du lot 7 est en lecture, gardée `is_admin`, sans PII en sortie (agrégats par chapitre).

### 3.7 Observabilité

Rien de nouveau à collecter (fiche : « aucune donnée nouvelle »). Le lot 7 **lit** ce qui existe.
Pas d'événement `lesson_read` dans PostHog — délibéré : « PostHog compte des passages, Postgres
compte des personnes » (`product-events.ts`), et la question posée (« la lecture a-t-elle
préparé le quiz ? ») est une question de personnes.

### 3.8 Décisions d'architecture (ADR)

- **D-1 — Le patron est du contenu ; le moteur gagne un bloc, pas une capacité.** Sept temps
  écrits avec neuf types de blocs, dont huit existent. _Alternatives rejetées_ : cours interactif
  (items incrustés, JS — casse é18 D-2, double le quiz) ; réexplication IA à l'exécution (é11, P-7).
- **D-2 — Le contrôle sur place est un `<details>` natif.** Aucun script, aucun état, imprimable,
  accessible au clavier, RTL natif, et **rien n'entre dans `ALLOWED_ATTR`**. _Alternative rejetée_ :
  un dépliage piloté en React sur du HTML injecté — il faudrait re-parser la chaîne assainie ou
  poser des écouteurs délégués pour un gain nul.
- **D-3 — La séquence est celle du manuel, adossée aux preuves.** نشاط → encadré → أطبق → تمرين
  مرفق بحل est ce que le CNP imprime. Le patron en garde l'ordre — l'activité **avant** l'énoncé,
  l'application **tout de suite après** — et y insère ce que les méta-analyses ajoutent pour des
  novices : l'exemple résolu avant la règle générale, et l'erreur typique contrastée. L'étude ne
  fait pas entrer une pédagogie étrangère : elle **rétablit** la séquence officielle que les cours
  avaient perdue, et la complète.
- **D-4 — L'ancrage vient d'abord des activités du manuel, réécrites.** La transcription porte
  57 activités ; elles sont la source la plus fidèle au programme **et** la plus proche de ce que
  le concours évalue. Réécrites (la garde anti-verbatim de `content:qa` tourne sur les leçons),
  jamais recopiées.
- **D-5 — L'erreur typique s'ancre sur le registre.** Les distracteurs de maths 9ᵉ portent 1 367
  tags ; le cours enseigne **contre les mêmes erreurs** que les exercices mesurent. C'est la boucle
  é04/é30 refermée côté enseignement, et `coursePitfalls` la rend vérifiable (C-5).
- **D-6 — Le budget se compte par notion.** « ~50-75 lignes » (style-guide) n'a jamais décrit le
  corpus pilote (82 → 331 lignes) ; une règle morte n'est pas une règle. R-13 la remplace par un
  budget qui décrit ce qu'on veut : 18-40 lignes par notion, scission au-delà de 240.
- **D-7 — Le déterministe vérifie la forme, le modèle juge le fond.** Six contrôles de
  structure, zéro reniflage de prose (é18 D-1) ; la grille d'audit porte le jugement, et la
  re-résolution à l'aveugle porte la vérité.
- **D-8 — La preuve du pilote est l'audit, la mesure est armée.** Cinq actifs par semaine ne
  prouvent rien ; l'étude ne prétend donc pas mesurer un gain d'apprentissage. Elle livre la
  vue qui le mesurera (lot 7), grisée sous 30 lectures, et nomme l'endroit où on la lit.
- **D-9 — L'opt-in par matière vit dans `subject.json`.** `coursePattern` durcit le gate sans
  éditer le moteur à chaque campagne ; il se pose au **dernier** lot d'une matière, jamais avant.
- **D-10 — Pas d'IA à l'exécution dans cette étude.** « Explique ce bloc autrement, avec un autre
  exemple » — ancré sur le texte vérifié du bloc, interdit de résoudre l'exercice — est la seule
  forme d'IA qui a tenu à l'examen (tuteur à garde-fous, Bastani 2025) ; c'est un tuteur, donc
  é11. Noté dans la fiche, gelé par défaut (P-7).

### 3.9 Ce que l'étude amende, et ce qu'elle réutilise sans y toucher

**Amende** : `course-quality.md` axe 2 (grille) et axe 4 (longueur → R-13) ; `style-guide.md`
(squelette au patron) ; `content-cours` et `content-audit` (workflow et grille) ; é18 R-6 (neuf
types au lieu de huit) et R-7 (fail-safe étendu au séparateur).

**Réutilise tel quel** : les huit blocs et la promotion des callouts (é18) ; les figures et leur
doctrine (é18 lot 4, `course-figures.md`) ; le résumé en cartes (é18 lot 3) ; R-8 de é21
(encadré → bloc) ; le registre des misconceptions (é04) ; `learning_pulses` et les constantes
« étudié » du rapport parent ; la porte du quiz (arena#1005) et le grand livre (é34) ; le
pipeline d'application (`content:emit` → `apply-content.yml` → `content-drift`).

---

## 4. Plan d'exécution en lots

Chaque lot = **une PR mergeable, gate verte, utile seule**. Les lots 1 et 7 vivent dans le dépôt
**moteur** (arena), les lots 2 à 6 et 8 dans le dépôt **privé** (corpus + skills). Les lots de
contenu suivent la méthode (`METHODE-GENERATION-CONTENU.md` : une PR par tranche de ≤ 5
chapitres) et **ne publient pas** : une PR mergée n'est en prod qu'après le dispatch humain de
`apply-content.yml`, et la session vérifie que l'issue `content-drift` est close.

| lot   | contenu (résumé)                                                                                                                                                                                                         | fichiers / objets                                                                                                                                                                                                                                                                          | tests exigés                                                                                                                  | dépend de               |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| **1** | **Moteur** : le bloc `verifie`, les six contrôles, les deux champs de schéma — **0 fichier de contenu**                                                                                                                  | `src/shared/lib/{markdown,lesson-blocks}.ts`, `src/styles.css`, `src/features/quest/components/lesson-reader.tsx`, `src/shared/content/schema.ts`, `scripts/content/{qa,qa-checks}.ts`, `docs/xss-rendering-policy.md`                                                                     | `markdown.test.ts`, `lesson-blocks.test.ts`, `qa-lesson.test.ts`, `lesson-reader.test.tsx`, e2e lecteur public, `smoke:shell` | Q-1                     |
| **2** | **Doctrine + gabarit vivant** (privé) : `course-explanation.md`, amendements des skills, **maquette** `06-fonctions-lineaires-affines`                                                                                   | `content-engine/references/{course-explanation (n),course-quality,style-guide,content-schema}.md`, `content-engine/SKILL.md`, `content-cours/SKILL.md`, `content-audit/SKILL.md`, `METHODE-GENERATION-CONTENU.md`, `content/math/06-*/{cours,resume}.md`, `content/math/06-*/chapter.json` | `content:check` · `content:qa:strict` · `content:figures:check` · `content:audit:strict` · `harness:check --corpus`           | 1, Q-2                  |
| **3** | Pilote, tranche **numérique A** : `01-nombres-reels`, `15-numeration-et-calcul`, `02-racines-carrees`, `16-puissances`, `17-ordre-et-comparaison`                                                                        | `content/math/{01,15,02,16,17}-*/{cours,resume}.md` + `chapter.json`                                                                                                                                                                                                                       | gates contenu ; audit `content-audit` à l'aveugle (grille §2.4 + re-résolution)                                               | 2                       |
| **4** | Pilote, tranche **numérique B** : `19-valeur-absolue`, `03-calcul-litteral`, `04-equations-inequations`, `05-systemes`                                                                                                   | `content/math/{19,03,04,05}-*/…`                                                                                                                                                                                                                                                           | idem                                                                                                                          | 3                       |
| **5** | Pilote, tranche **fonctions · statistiques · repère · Thalès · trigo** : `07-statistiques`, `12-repere-plan`, `08-thales`, `09-triangle-rectangle-trigo`                                                                 | `content/math/{07,12,08,09}-*/…`                                                                                                                                                                                                                                                           | idem                                                                                                                          | 4                       |
| **6** | Pilote, tranche **géométrie B** : `10-angles-cercle`, `11-vecteurs-translation`, `18-quadrilateres`, `13-geometrie-espace`, `20-orthogonalite-espace` — **et** `coursePattern: "notion"` sur `content/math/subject.json` | `content/math/{10,11,18,13,20}-*/…`, `content/math/subject.json`                                                                                                                                                                                                                           | idem ; **C-1…C-5 en `[error]` verts sur les 19 chapitres**                                                                    | 5                       |
| **7** | **Mesure** (moteur) : `admin_lesson_to_quiz_outcome` + bloc « Cours → quiz » sur `/admin/engagement`                                                                                                                     | migration additive `supabase/migrations/…_lesson_to_quiz_outcome.sql`, `types.ts` régénéré, server fn et composant de la console                                                                                                                                                           | pgTAP (garde admin, définitions « étudié » et « premier essai », `n_small`), unit console, `build:check`                      | 6 appliqué en prod, Q-6 |
| **8** | **Bilan & extension** (privé) : rapport du pilote, KPI §1.4, verdict Q-5, étude → `livrée`                                                                                                                               | `ETUDE.md` §8, `README.md` (index), `ROADMAP.md`, STATUS.md (moteur, ligne « cours »)                                                                                                                                                                                                      | `etudes:check`, `roadmap-sync`                                                                                                | 7 (ou 6 si Q-6 = non)   |

- [x] **Lot 1 — Le bloc `verifie` et les contrôles du patron.** ✅ 2026-09-16 (§8)
      _Périmètre_ : R-16 → R-22, C-1 → C-6, §3.1 (deux champs zod), §3.3. Un type de bloc dans
      le parser par lignes (scission au premier `---`), émission `details`/`summary`, libellés
      dans les 3 langues, CSS par tokens, dépliage à l'impression, `renderSummary` neutre,
      allowlist +2 balises, `docs/xss-rendering-policy.md` à jour.
      _Acceptation_ : US-4, US-5, US-7 ; les tests XSS de `markdown.test.ts` passent **sans
      modification** (sinon R-20 est cassé : **STOP**) ; `content:qa:strict` reste **vert sur le
      corpus du jour** (aucune matière sous patron, donc C-1/C-2/C-3/C-5/C-6 en `[warn]`) ;
      le rapport de PR **compte** les warns par matière ; **aucun fichier sous `content/`** dans
      le diff ; `smoke:shell` vert (le renderer est dans le bundle public).
      _Stop-point_ : pas de dixième type, pas d'attribut nouveau, pas de touche à `sanitizeSvg`,
      pas de mesure (lot 7), pas de skill (lot 2).

- [x] **Lot 2 — La doctrine et le gabarit vivant.** ✅ 2026-09-16 (§8)
      _Périmètre_ : §3.4 intégralement, plus la **maquette** : `06-fonctions-lineaires-affines`
      réécrit aux sept temps (R-1 → R-15), `resume.md` en miroir, `coursePitfalls` déclarés — le
      chapitre dont l'ancrage (le taxi) arrive aujourd'hui ligne 121 sur 138 devient le cours de
      référence que les lots 3-6 imitent. Le premier cas traité est celui de l'annexe C.
      _Acceptation_ : US-8, US-9 ; gates contenu verts (`content:qa:strict` y compris C-4 et
      les tags de C-5) ; `harness:check --corpus` vert (budget des skills, Unicode invisible) ;
      audit `content-audit` du chapitre : **ship** ; **validation humaine de la maquette au rendu**
      (aperçu du lecteur, FR et AR — DoE 4) avant d'ouvrir le lot 3.
      _Stop-point_ : un seul chapitre de contenu ; aucune touche aux quiz/exercices du chapitre
      (les notions orphelines, s'il y en a, sont **signalées** dans la PR) ; pas de
      `coursePattern` sur `math` (lot 6).

- [ ] **Lots 3 à 6 — La campagne pilote, quatre tranches.**
      _Périmètre commun_ : chaque chapitre est réécrit par `content-cours` aux sept temps, à
      partir de la transcription du manuel (activités, encadrés, exercices corrigés — D-4), des
      `misconceptionTag` de ses propres exercices (D-5) et des figures é18 existantes, qui sont
      **conservées** (une figure vraie ne se redessine pas ; elle reçoit sa phrase de pont R-11) ;
      `resume.md` en miroir ; `coursePitfalls` déclarés. Audit **à l'aveugle** par `content-audit`
      (l'auditeur ne lit pas la PR avant de noter) : grille §2.4, re-résolution de chaque
      exemple, erreur typique et contrôle.
      _Acceptation_ : gates verts ; verdict **ship** par chapitre ; le rapport de PR donne, par
      chapitre, la carte notion → temps → blocs, les tags ciblés, la longueur avant/après, et
      les notions testées non couvertes s'il y en a (signalées, pas corrigées) ; merge → dispatch
      humain de `apply-content.yml` → issue `content-drift` close.
      _Lot 6 en plus_ : `coursePattern: "notion"` sur `content/math/subject.json`, et
      `content:qa:strict` vert avec C-1 → C-5 en `[error]` sur les 19 chapitres.
      _Stop-point_ : ≤ 5 chapitres par PR ; **une seule matière** ; jamais deux tranches dans une
      PR ; un chapitre qui dépasse 240 lignes remonte (R-13) au lieu d'être tronqué.
      _Avancement_ : lot 3 ✅ (privé#406) · lot 4 ✅ · lots 5-6 à faire. **Quatre** chapitres
      dépassent R-13 et attendent l'arbitrage : `15` (379), `03` (346), `04` (305), `17` (301).
      Le patron ajoute mécaniquement ~40 % de lignes (ancrage + pourquoi + contrôle) : si
      l'arbitrage est « on ne scinde pas », c'est **R-13 qu'il faut recalibrer**, pas les cours.

- [ ] **Lot 7 — La mesure.**
      _Périmètre_ : §3.2, §3.3 (console). La fonction lit `learning_pulses`, `attempts` et
      `content_releases` ; la console la montre, grisée sous 30 lectures.
      _Acceptation_ : US-10 ; pgTAP ; `types.ts` régénéré depuis la chaîne ; `db:check-chain`
      vert ; DoD §7 (additif, un seul merge).
      _Stop-point_ : aucune écriture, aucun événement produit, aucune surface élève.

- [ ] **Lot 8 — Le bilan.**
      _Périmètre_ : KPI §1.4 relus sur `main` et sur la console ; sweep `content-audit` (mer. +
      sam.) sur `math` ; recommandation pour Q-5 ; statut `livrée`, dossier déplacé, index,
      ROADMAP et STATUS.md resynchronisés (`etudes:check`, `roadmap-sync`).

**Après le lot 8** : la campagne de fond sort de l'étude → gouvernance contenu, **une matière par
campagne**, dans l'ordre que Q-5 arrête. Le patron ne s'applique à une matière que par le
`coursePattern` qu'elle pose à la fin de sa propre campagne (D-9).

---

## 5. Stratégie de test

**Unit (Vitest, co-localisés)** — le lot 1 est du rendu et du gate, purs.

- `src/shared/lib/__tests__/markdown.test.ts` : **non-régression XSS** (les tests existants
  passent sans être touchés) ; `verifie` complet → `details`/`summary`, question et réponse
  rendues, libellés par langue de contenu ; sans séparateur → bloc neutre, **pas de crash** ; côté
  vide → neutre ; deux `---` → seul le premier scinde ; `---` hors `verifie` → `<hr>` inchangé ;
  formule `$$` dans la question et dans la réponse ; prose arabe + formule LTR dans la réponse
  (le test « mixed Arabic and math » reste vert) ; `verifie` dans `renderSummary` → neutre.
- `src/shared/lib/__tests__/lesson-blocks.test.ts` : neuf types, libellés et libellés de bouton
  dans les 3 langues, aucun trou.
- `src/features/quest/__tests__/lesson-reader.test.tsx` : Imprimer déplie puis replie les
  `details` ; le reste inchangé.
- `scripts/content/__tests__/qa-lesson.test.ts` : chaque contrôle C-1…C-6 sur fixtures
  minimales, dans les deux modes (`coursePattern` absent / présent) ; `coursePitfalls` inconnu du
  registre → `[error]` ; tag non porté par un distracteur du chapitre → `[error]` ;
  `LESSON_DIRECTIVES` ⇔ `DIRECTIVE_TYPES`.
- Schéma : `schema.test.ts` (ou équivalent) — `coursePattern` hors enum rejeté ; `coursePitfalls`
  facultatif.

**pgTAP** — lot 7 seulement : garde admin (refus pour un non-admin), une lecture « étudiée » avant
le premier essai compte, une lecture après ne compte pas, un anonyme n'apparaît pas, `n_small`
à 29 et 30, la coupure `p_cutoff`.

**Gate contenu** — `content:check`, `content:qa:strict`, `content:figures:check`,
`content:audit:strict`, `programme:check`, `harness:check --corpus` verts à chaque lot privé.
Le lot 1 fait apparaître des `[warn]` C-1…C-6 sur les 773 cours : ils sont **comptés** dans la
PR, pas corrigés (ils sont le backlog de la campagne de fond).

**e2e (Playwright, projet TEST)** — une assertion ajoutée au lot 1 sur le lecteur public : sur un
chapitre de fixture portant un `verifie`, la réponse est **absente du rendu** avant le clic et
**présente** après (`public-chromium` + `public-mobile`).

**`smoke:shell`** — non négociable au lot 1 : le renderer est dans le bundle prod d'une page
publique.

**Non-régression de l'existant** — (1) le diff du lot 1 ne contient **aucun** fichier sous
`content/` ; (2) les tests XSS sont verts sans modification ; (3) `content:qa:strict` est vert
sur le corpus du jour ; (4) les 56 figures de maths 9ᵉ sont **présentes à l'identique** après
chaque tranche (le diff des `<svg>` est vide, ou justifié figure par figure).

**Preuve pédagogique** — l'audit à l'aveugle par chapitre (grille §2.4) est la preuve du pilote ;
la console du lot 7 est la mesure, lisible quand le volume existe (D-8).

---

## 6. Risques & mitigations

- **RISK-1 — Le patron gonfle les cours au-delà du lisible.** _Probabilité forte / impact
  moyen._ Sept temps × six notions = un cours qui double. Mitigation : R-12 (3-6 lignes par
  bloc), R-13 (budget par notion, scission au-delà de 240), C-6, et la grille (`[MINOR]` sur un
  bloc long). Le gabarit de l'annexe C fait **41 lignes** pour une notion complète : c'est la
  référence, pas le plafond.
- **RISK-2 — Des ancrages factices.** _Probabilité moyenne / impact fort._ Un « contexte » plaqué
  (un dragon qui calcule des racines) n'ancre rien ; l'étude vidéo de l'OCDE (GTI 2020) a trouvé
  les liens au réel rares **et** faibles là où ils existaient. Mitigation : R-2 (l'ancrage est
  une question, et vient des activités du manuel), R-10 (pas de décor dans les blocs), grille
  (`[MINOR]` ancrage sans question) — et la maquette validée au rendu avant tout lot de campagne.
- **RISK-3 — L'erreur typique enseigne l'erreur.** _Probabilité faible / impact fort._ La revue
  Dieterich 2025 est nette : l'exemple erroné ne paie que **contrasté, signalé, expliqué**, chez
  un élève qui a déjà vu le correct. Mitigation : R-5 (après un exemple correct, nommée dès la
  première ligne, corrigée, jamais dans le résumé — `[BLOCKER]` sinon), et la re-résolution de
  l'audit.
- **RISK-4 — Le gate crie sur des sections légitimes** (synthèse « خلاصة القواعد », section de
  rappel). _Probabilité certaine / impact faible._ Mitigation : C-1/C-2/C-3 restent `[warn]` tant
  que la matière n'a pas posé `coursePattern` ; une section de synthèse sans bloc de savoir ne
  déclenche rien ; C-6 reste `[warn]` partout.
- **RISK-5 — Reprise verbatim du manuel** (PI, é24/é27). _Probabilité moyenne / impact fort._
  Mitigation : D-4 (réécrit, jamais recopié), la garde anti-verbatim de `content:qa` qui tourne
  déjà sur les leçons (`auditVerbatim`), et le rapport de PR qui cite la page source de chaque
  ancrage.
- **RISK-6 — Rendu RTL du `<details>`** (marqueur, `summary`, réponse avec formule LTR).
  _Probabilité faible / impact moyen._ Mitigation : test « mixed Arabic and math » sur la réponse,
  vérification au rendu de la maquette AR (lot 2, DoE 4), le `dir` du conteneur hérité.
- **RISK-7 — Rien à mesurer.** _Probabilité certaine à court terme / impact nul sur le pilote._
  Mitigation : D-8 — la preuve est l'audit ; la console dit « volume insuffisant » au lieu d'un
  chiffre trompeur ; Q-6 laisse le lot 7 attendre le trafic.
- **RISK-8 — L'exécuteur écrit des « pourquoi » creux** (« لأنّ هذه هي القاعدة »). _Probabilité
  moyenne / impact fort — c'est tout l'objet de l'étude._ Mitigation : R-4 (étiquette de
  principe, pas de tautologie), la grille (`[MAJOR]` exemple sans ses pourquoi), l'audit à
  l'aveugle, et la maquette comme étalon du niveau attendu.
- **RISK-9 — Collision avec é23 lot 5** (même matière). _Probabilité faible._ Les vidéos
  vivent dans `chapter.json` (`videos`) et `videos.json` ; le patron touche `cours.md`,
  `resume.md` et `coursePitfalls`. Deux PR sur le même `chapter.json` se résolvent par un merge
  ordinaire ; aucune règle ne se chevauche.
- **RISK-10 — La preuve citée est plus fragile que son chiffre.** _Probabilité certaine / impact
  sur la crédibilité._ Le proxy de la session a bloqué les sites éditeurs : chaque source de
  l'annexe A est vérifiée au niveau du **résumé** via l'index de recherche, pas de la page
  ouverte ; une méta-analyse trouvée puis **rétractée** (Wang & Fan 2025) est écartée.
  Mitigation : chaque ligne porte son statut de vérification ; la doctrine (lot 2) reprend les
  chiffres **avec** cette réserve ; toute citation externe (blog, dossier de presse) exige
  d'ouvrir la page.

---

## 7. Questions ouvertes (pour l'humain)

> ✅ **Les six arbitrages ont été rendus le 2026-09-16, tous sur la recommandation.** Ils sont
> conservés ci-dessous avec leur motif — une décision qu'on efface est une décision qu'on
> re-prend. Q-1 « oui » a rendu le lot 1 exécutable le jour même ; Q-2 a désigné la maquette ;
> Q-3 a fixé l'ordre des tranches ; Q-4 diffère le glossaire ; Q-5 se tranchera au bilan ;
> Q-6 laisse la mesure attendre le premier trafic.

- **Q-1 — Le lot moteur (bloc `verifie`) : oui ou non ?** ✅ **OUI** (2026-09-16). _Recommandation : **oui**._ C'est le
  seul lot de code, court (un type de bloc, deux balises inertes, six contrôles), et sans lui le
  couple « exemple résolu → à toi » — le résultat le plus solide de tout le corpus de preuves —
  n'a aucune syntaxe. Le repli (option B, §2.2) garde T1-T6 et perd T7.
- **Q-2 — Le chapitre maquette.** ✅ **`06-fonctions-lineaires-affines`** (2026-09-16). _Recommandation : `06-fonctions-lineaires-affines`_ — zéro bloc
  de savoir, l'ancrage réel (le taxi) déjà écrit mais placé à la fin, une figure é18 à relier,
  des tags de misconception sur ses distracteurs, et une notion (la linéarité) où l'erreur
  additive est classique. Alternative : `08-thales` (géométrie, figures maquettées par é18).
- **Q-3 — L'ordre des tranches.** ✅ **l'ordre du manuel** (2026-09-16). _Recommandation : l'ordre du manuel_ (numérique → algèbre →
  fonctions/statistiques → géométrie), tel que §4 le pose : c'est l'ordre dans lequel l'élève
  rencontre les notions dans l'année, et les figures é18 arrivent en dernier, quand la méthode
  est rodée. Alternative : commencer par les chapitres les plus joués (à relever sur `attempts`).
- **Q-4 — Un glossaire arabe → français en fin de cours ?** ✅ **différé** (2026-09-16). La 1ʳᵉ secondaire bascule les maths
  en français ; la transcription porte déjà, chapitre par chapitre, la table « terme arabe →
  traduction ». _Recommandation : **différer**_ — aucune étude trouvée sur ce point précis (annexe
  A § A.5), et le programme de 9ᵉ ne le demande pas (R-15). Si Mohamed le souhaite : un tableau
  de 5-10 termes en fin de cours, **hors blocs**, jamais dans le résumé — un lot de contenu à
  part, après le pilote.
- **Q-5 — La matière suivante, après le bilan.** ⏳ **au lot 8** (2026-09-16). _Recommandation : les deux autres matières
  scientifiques de 9ᵉ_ (physique, puis SVT — même classe de concours, mêmes élèves, doctrine
  déjà rodée sur l'arabe RTL), puis maths 6ᵉ (l'autre concours). À trancher au lot 8, sur le
  bilan.
- **Q-6 — Le lot 7 (mesure) maintenant, ou au premier trafic ?** ✅ **au premier trafic, spécifié maintenant** (2026-09-16). _Recommandation : **au premier
  trafic**_, mais **spécifié maintenant** (§3.2) pour qu'il n'y ait rien à re-décider. Sous 30
  lectures étudiées par chapitre, la console ne dirait que « volume insuffisant » ; le lot se
  déclenche quand KPI-1 (un canal actif) cesse d'être à zéro.

---

## 8. Journal d'exécution

| date       | lot | PR         | écarts acceptés / dettes notées                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ---------- | --- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2026-09-16 | —   | —          | Étude rédigée (Fable). État réel mesuré sur `main` des deux dépôts (annexe B). Quatre recherches documentaires menées depuis la session (annexe A) — **réserve** : sites éditeurs bloqués par le proxy, vérification au niveau du résumé ; une méta-analyse rétractée écartée. Q-1…Q-6 ouvertes. Aucun lot commencé.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 2026-09-16 | —   | —          | **Étude VALIDÉE** : Q-1…Q-6 arbitrées, toutes sur la recommandation. Statut → `en exécution`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| 2026-09-16 | 1   | arena#1050 | **Lot 1 livré — le contrôle sur place existe.** `::: verifie` est le neuvième type du vocabulaire et le seul dont le corps a deux côtés ; sa réponse est repliée dans un `<details>`/`<summary>` **natif** — zéro script, zéro état React, et `open` délibérément **hors** de `ALLOWED_ATTR` : le contenu ne peut pas décider qu'une réponse arrive révélée. Six contrôles structurels dans `content:qa` (C-1…C-6), deux régimes (`warn` sans `coursePattern`, `error` avec), `coursePattern`/`coursePitfalls` au schéma, lus par le gate **seulement**. **Mesuré sur les 999 chapitres : 0 erreur, 332 avertissements** — le backlog de la campagne de fond, dont **3 seulement en maths 9ᵉ**. Les 8 tests XSS passent **sans avoir été touchés** ; gate complet vert (4 379 tests). **Trois écarts assumés** : (a) le résumé n'a **aucune** grammaire de blocs — R-21 est donc tenue par construction, rien à coder, et le gate refuse quand même un `::: verifie` dans un résumé ; (b) C-5a et les contrôles de patron ne s'appliquent qu'à un texte portant au moins une section `##` — un fragment sans `##` n'est pas un cours, et sans cette borne le lot cassait deux tests de é18 sur des fixtures de deux lignes ; (c) **un septième contrôle non prévu** a été ajouté, et il est le plus utile : sous `coursePattern`, un cours sans **aucun** bloc de savoir ni exemple échoue — sans lui le drapeau serait décoratif, puisque tous les autres contrôles se déclenchent en PRÉSENCE d'un bloc. ⚠️ **Le tier E2E n'a pas été exécuté** : l'assertion « réponse cachée avant le clic, visible après » est écrite et la fixture porte désormais une leçon, mais la config Playwright refuse — à raison — de démarrer sans projet Supabase TEST. |
| 2026-09-16 | 2   | privé#403  | **Lot 2 livré — la doctrine, et le cours qui la montre.** `course-explanation.md` (239 lignes) devient la référence normative de l'axe 2, comme `course-figures.md` l'est de l'axe 5 : les sept temps, R-1…R-15, la grammaire du `verifie`, ce que le gate attrape et ce qu'il ne peut pas, dix anti-patrons, une auto-vérification en neuf points. Amendés : `course-quality.md` (axe 2 réécrit, axe 4 → budget par notion, sévérités du patron), `style-guide.md`, `content-schema.md`, les skills `content-engine`, `content-cours` (étape 1 : moissonner les **activités** du manuel et les `misconceptionTag` du chapitre ; étape 3 : écrire aux sept temps), `content-audit` (axe 2 devient une grille par section, **re-résolution obligatoire**), et la méthode. **Maquette** : `06-fonctions-lineaires-affines`, 138 → 273 lignes, 6 notions aux sept temps, 6 `coursePitfalls` déclarés — l'ancrage réel du chapitre (le taxi), qui vivait ligne 121 sur 138, ouvre désormais sa notion. **Preuve** : les **37 calculs du cours re-dérivés indépendamment**, zéro faux ; gates verts (`content:check`, `qa:strict`, `figures:check`, `programme:check`, `harness:check --corpus`) ; et sous `coursePattern` posé **temporairement** pour l'épreuve, le chapitre sort à **zéro constat** quand les 19 autres en produisent 38 — les deux régimes font ce qu'ils annoncent. **Écart assumé** : le chapitre 06 est **hors programme officiel** (son `chapter.json` le dit, et le manuel CNP n'a pas de pages pour lui). La maquette démontre donc la branche « quotidien tunisien » de R-2, pas la branche « activité du manuel » — c'est le lot 3 qui la démontrera. Le flag `coursePattern` n'est **pas** posé : il se pose au lot 6.           |
| 2026-09-16 | 3   | privé#406  | **Lot 3 livré — la tranche numérique, et la branche « activité du manuel » démontrée.** Cinq chapitres réécrits (`01-nombres-reels`, `02-racines-carrees`, `15-numeration-et-calcul`, `16-puissances`, `17-ordre-et-comparaison`) : 35 sections, 41 blocs de savoir, 37 exemples résolus, 34 contrôles `verifie`, 32 pièges, 35 `coursePitfalls` tous tirés des tags que portent les distracteurs **du chapitre lui-même**. Les 12 figures é18 sont conservées **octet pour octet**. Les ancrages viennent d'abord des **activités du manuel** (les divisions 4 ÷ 3 et 3 ÷ 22 qui font apparaître le dor, « quel nombre positif a pour carré 16 ? », le placement de 12/5 et 19/4 sur la droite graduée) — ce que la maquette du lot 2, hors programme, ne pouvait pas démontrer. **Preuve** : 136 calculs re-dérivés indépendamment, zéro faux — dont un **faux échec de mon propre vérificateur** (il testait `100 × a` là où le cours écrit `10 × a`) : le cours avait raison, le contrôle avait tort. Gates verts. ⚠️ **Deux chapitres dépassent le plafond de 240 lignes de R-13** — `15` (379) et `17` (302) — et n'ont **pas** été tronqués : R-13 dit que le chapitre se scinde et que c'est un arbitrage humain. Remontés tels quels. _(Ligne écrite rétrospectivement avec le lot 4 : le lot 3 avait porté son rapport dans le message de commit, pas ici.)_                                                                                                                                                                                                                                                                                                                                                                                   |
| 2026-09-16 | 4   | privé#407  | **Lot 4 livré — la tranche algébrique.** Quatre chapitres réécrits (`19-valeur-absolue` 119 → 208 lignes, `03-calcul-litteral` 135 → 346, `04-equations-inequations` 166 → 305, `05-systemes` 139 → 246) : 28 contrôles `verifie`, 38 exemples résolus, 30 pièges, 23 `coursePitfalls` déclarés, les 5 figures conservées **octet pour octet** (vérifié par extraction et comparaison des blocs `<svg>`). Ancrages du manuel : le nombre deviné du **نشاط 2 p.95** (« j'ai retranché 5/2, multiplié par 6, ajouté 75, trouvé 216 ») ouvre la traduction des problèmes, et l'aire calculée **de deux façons** des نشاط 2 p.79 / نشاط 6 p.83 fait naître les trois identités. Les deux encadrés VERBATIM du manuel (p.95 pour l'équation, p.103 pour l'inéquation) remplacent les définitions maison. **Preuve** : 143 calculs re-dérivés indépendamment, zéro faux ; gates verts (0 erreur sur 999 chapitres) ; et les 28 blocs `verifie` passés dans le **vrai moteur de rendu** — question et réponse repliée émises pour chacun, libellé arabe présent, aucun `open`, aucune figure échappée. **Trois constats remontés, aucun corrigé unilatéralement** : (a) `05-systemes` est **hors programme 9ᵉ** — le registre de transcription l'établit sur les 221 pages (`جملة` et `بمجهولين` absents, les trois encadrés du ch.7 disent « ذات مجهول واحد ») — donc ancré au quotidien, faute d'activité à moissonner ; (b) `03` (346) et `04` (305) **dépassent R-13**, ce qui porte à **quatre** les chapitres au-dessus du plafond ; (c) la section des trois identités remarquables a dû être **scindée en trois sections `##`** — C-6 l'a refusée à 82 lignes, et le gate avait raison : elle portait trois notions.                                    |

---

## Annexe A — État de l'art 2024-2026 : ce qui est prouvé, ce qui ne l'est pas, ce que l'étude en fait

> **Réserve de vérification, à lire d'abord.** Les quatre recherches documentaires de cette étude
> ont été menées depuis la session cloud du 2026-09-16, dont le proxy **bloque les sites
> éditeurs** (Springer, Elsevier, SAGE, Taylor & Francis, APA, ERIC, PubMed, EEF, OCDE). Aucune
> page d'article n'a donc été **ouverte** : chaque ligne ci-dessous a été confrontée au **résumé**
> de la page éditeur tel que l'index de recherche le restitue, en croisant deux sources
> indépendantes quand c'était possible. Statut par ligne : **résumé** (auteurs, année, revue,
> échantillon et chiffre lus dans le résumé de la page citée) · **titre** (existence et titre
> confirmés, chiffre non lu) · **non vérifié** (souvenir non confirmé — ne pas citer sans ouvrir
> la page). Une méta-analyse trouvée en route, Wang & Fan 2025 (_Humanities and Social Sciences
> Communications_, g = 0,87 pour ChatGPT), a été **rétractée le 2026-04-22** : elle est écartée,
> et c'est une raison de plus de ne rien citer de mémoire. **Avant toute citation hors de ce
> dépôt, ouvrir la page.** Les deux chiffres qui divergent entre les deux passes de vérification
> sont signalés tels quels.

### A.1 Exemples résolus et charge cognitive — ce qui fonde T4, T6, T7

| méthode                                                         | effet                                                                                                                                                                  | source                                                                                                                                                              | statut                     | ce que l'étude en fait                                                                      |
| --------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- | ------------------------------------------------------------------------------------------- |
| Exemples résolus en maths (vs résolution seule)                 | **g = 0,48** — 55 études, 181 effets, du primaire au supérieur ; les exemples **corrects** l'emportent ; les invites d'auto-explication ajoutées **réduisent** l'effet | Barbieri, Miller-Cotto, Clerjuste & Chawla 2023, _Educ. Psychol. Rev._ 35:11 — https://link.springer.com/article/10.1007/s10648-023-09745-1                         | résumé                     | T4 obligatoire pour toute règle ; R-4 : le pourquoi est **donné**, pas demandé sans réponse |
| Exemple **puis** problème (jamais l'inverse) chez les novices   | exemples seuls et couples exemple → problème > problème → exemple et résolution seule (secondaire)                                                                     | van Gog, Kester & Paas 2011, _Contemp. Educ. Psychol._ 36 — https://www.sciencedirect.com/science/article/abs/pii/S0361476X1000055X                                 | résumé                     | T4 → T7, jamais T7 → T4 ; R-8                                                               |
| Exemples estompés (étape blanche), et **quelle** étape estomper | transfert proche et lointain moyen à large quand l'étape estompée porte le principe ; sa position importe peu                                                          | Renkl, Atkinson, Maier & Staley 2002 ; Atkinson, Renkl & Merrill 2003, _J. Educ. Psychol._ 95(4) ; Renkl, Atkinson & Grosse 2004 — https://eric.ed.gov/?id=EJ732331 | résumé                     | R-8 : l'étape blanche du `verifie` est **celle qui porte le principe**                      |
| Estompage en devoir de géométrie, 6ᵉ, 2026                      | plus fort gain pré/post que l'exemple complet + invites et que la résolution ; seul le savoir préalable modère (N = 114)                                               | Miller-Cotto & Medrano 2026, _Brit. J. Educ. Psychol._ 96(1) — https://pmc.ncbi.nlm.nih.gov/articles/PMC12879535/                                                   | résumé                     | confirme la forme « à compléter » de T7                                                     |
| Renversement d'expertise, quantifié                             | assistance forte : **d = 0,51** chez les novices ; **d = −0,43** chez ceux qui savent (176 effets, 60 études, N = 5 924)                                               | Tetzlaff, Simonsmeier, Peters & Brod 2025, _Learning and Instruction_ 98 — https://www.sciencedirect.com/science/article/pii/S0959475225000660                      | résumé                     | guidage complet dans le cours (novices) ; le **résumé** sert celui qui sait                 |
| Texte + figure **intégrés** (attention divisée)                 | **g = 0,63** — 58 comparaisons, n = 2 426 ; l'origine est la géométrie au lycée (Tarmizi & Sweller 1988)                                                               | Schroeder & Cenkci 2018, _Educ. Psychol. Rev._ 30(3) — https://eric.ed.gov/?id=EJ1186641                                                                            | résumé                     | R-11 : étiquettes **dans** la figure, phrase de pont, explication à côté de son étape       |
| Signalement (mettre en évidence l'élément dont on parle)        | rétention **g = 0,52**, transfert **g = 0,31** (103 études, N = 12 201) ; aide surtout les faibles connaissances                                                       | Schneider, Beege, Nebel & Rey 2018, _Educ. Research Review_ 23 — https://www.sciencedirect.com/science/article/abs/pii/S1747938X17300581                            | résumé                     | R-11 : même nom, même couleur, dans le texte et la figure ; étape opérante en gras          |
| Détails séduisants (décor intéressant mais inutile)             | effet **négatif** — les deux passes ont lu **g = −0,16** (50 études, 177 effets) et **g = −0,33** (68 études) : chiffre à confirmer                                    | Sundararajan & Adesope 2020, _Educ. Psychol. Rev._ 32 — https://link.springer.com/article/10.1007/s10648-020-09522-4                                                | résumé (chiffre divergent) | R-10 : rien de narratif dans les blocs ; le RPG reste au titre, à l'épigraphe, à la clôture |
| Explications ajoutées à côté des exemples                       | petit (d ≈ 0,16, plutôt conceptuel) ; pas mieux que l'auto-explication                                                                                                 | Wittwer & Renkl 2010, _Educ. Psychol. Rev._ 22 — https://link.springer.com/article/10.1007/s10648-010-9136-5                                                        | résumé                     | R-4 : une **étiquette** de principe par étape, jamais un paragraphe                         |
| Limite : matière à faible interactivité                         | l'effet des exemples tient pour les contenus à forte interactivité ; sinon effet de génération ; il se renverse avec l'expertise                                       | Chen, Kalyuga & Sweller 2015, _J. Educ. Psychol._ 107(3) — https://eric.ed.gov/?id=EJ1071512                                                                        | résumé                     | T4 pèse le plus sur les procédures à plusieurs étapes (équations, Thalès, rationalisation)  |
| Où en est la théorie                                            | le savoir préalable est la différence individuelle qui compte pour un design donné                                                                                     | Sweller 2023, _Educ. Psychol. Rev._ 35 ; Sweller 2024, _Learning and Individual Differences_ — https://www.sciencedirect.com/science/article/pii/S1041608024000165  | résumé                     | —                                                                                           |
| Check-list « exemples résolus pour le transfert », 2026         | revue intégrative + liste praticien                                                                                                                                    | Bourgaux, Tricot & Paas 2026, _Educ. Psychol. Rev._ 38:118, DOI 10.1007/s10648-026-10206-8                                                                          | titre                      | à lire au lot 2 avant d'écrire `course-explanation.md`                                      |

### A.2 Erreurs typiques, auto-explication, comparaison — ce qui fonde T5 et R-7

| méthode                                                   | effet                                                                                                                                                 | source                                                                                                                                                       | statut | ce que l'étude en fait                                                      |
| --------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------ | --------------------------------------------------------------------------- |
| Exemples erronés expliqués (algèbre, tuteur en classe)    | expliquer des exemples > pratique seule ; expliquer des **erronés** > corrects seuls sur la compréhension conceptuelle                                | Booth, Lange, Koedinger & Newton 2013, _Learning and Instruction_ 25 — https://www.sciencedirect.com/science/article/abs/pii/S0959475212000904               | résumé | T5 existe                                                                   |
| Exemples erronés interactifs (décimaux, 390 collégiens)   | rien à l'immédiat, **mieux à une semaine**                                                                                                            | McLaren, Adams & Mayer 2015, _Int. J. AIED_ — https://link.springer.com/article/10.1007/s40593-015-0064-x                                                    | résumé | T5 vise la rétention, pas le quiz du jour                                   |
| Revue systématique 2025 (40 études)                       | bénéfice **conditionnel** : erreur **signalée et expliquée**, **contrastée** avec le correct, savoir préalable ; l'erroné nu ≈ ses témoins            | Dieterich, Rumann & Rodemer 2025, _Educ. Psychol. Rev._ 37(4) — https://link.springer.com/article/10.1007/s10648-025-10071-x                                 | résumé | R-5 : après un correct, nommée, diagnostiquée, corrigée — `[BLOCKER]` sinon |
| Comparer incorrect et correct (décimaux, 4ᵉ-5ᵉ)           | > correct seul, procédural et conceptuel, quel que soit le savoir préalable                                                                           | Durkin & Rittle-Johnson 2012, _Learning and Instruction_ 22(3)                                                                                               | résumé | forme de T5 : l'étape fausse **face** à la bonne                            |
| Auto-explication (invitée)                                | **g = 0,55** (69 effets, 64 rapports) ; plus fort avec invites **spécifiques** et faible savoir préalable                                             | Bisra, Liu, Nesbit, Salimi & Winne 2018, _Educ. Psychol. Rev._ 30 — https://link.springer.com/article/10.1007/s10648-018-9434-x                              | résumé | une seule invite spécifique par notion, **avec** sa réponse (le `verifie`)  |
| Auto-explication en environnement numérique, 2025         | **g = 0,46** (204 effets, 56 études) ; rétention 0,31, transfert 0,33                                                                                 | Tan, Gong, Wang et al. 2025, _Educ. Psychol. Rev._, DOI 10.1007/s10648-025-10001-x                                                                           | résumé | idem                                                                        |
| Auto-explication en maths seulement                       | gains immédiats petits à moyens ; preuve **faible** en rétention différée et en classe ; mieux si l'explication de qualité est étayée                 | Rittle-Johnson, Loehr & Durkin 2017, _ZDM_ 49(4) — https://eric.ed.gov/?id=EJ1149060                                                                         | résumé | R-4 : étayer (l'étiquette de principe), ne pas espérer de miracle           |
| Exemples + invites insérés **dans un manuel** (fractions) | estimation sur droite graduée améliorée ; gains conceptuels seulement à faible savoir préalable                                                       | Barbieri, Booth & Chawla 2023, _Educational Psychology_ 43(1) — https://www.tandfonline.com/doi/abs/10.1080/01443410.2022.2144142                            | résumé | le support « texte de leçon » est bien celui des études                     |
| Comparer deux méthodes côte à côte                        | chez les élèves **sans** méthode au prétest : **moins** appris qu'en séquentiel (236 élèves de 7ᵉ-8ᵉ) ; essai d'un an, 141 profs : **aucun** avantage | Rittle-Johnson, Star & Durkin 2009, _J. Educ. Psychol._ 101(4) ; Star et al. 2015, _Contemp. Educ. Psychol._ 40 — https://dash.harvard.edu/handle/1/12122306 | résumé | R-7 : une méthode au premier contact ; la comparaison en synthèse           |
| Guide WWC algèbre (2015/2018)                             | rec. 1 « problèmes résolus » : preuve **minimale** ; rec. 3 « choisir entre stratégies » : modérée                                                    | https://ies.ed.gov/ncee/wwc/practiceguide/20                                                                                                                 | résumé | guidance, pas preuve — citée comme telle                                    |

### A.3 Concret → abstrait, représentations, figures — ce qui fonde T1, T3, R-11

| méthode                                               | effet                                                                                                         | source                                                                                                                                                                                                     | statut              | ce que l'étude en fait                                                            |
| ----------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- | --------------------------------------------------------------------------------- |
| Mots + images vs mots seuls (compréhension de textes) | **g = 0,39** — 39 expériences, tous niveaux ; schémas, diagrammes et images ne diffèrent pas                  | Guo, Zhang, Wright & McTigue 2020, _AERA Open_ — https://journals.sagepub.com/doi/10.1177/2332858420901696                                                                                                 | résumé              | T3 recommandé partout, obligatoire si spatial (é18)                               |
| Visualisations en maths, 2024                         | **g = 0,50** [0,38 ; 0,63] — 41 études, N = 10 562, durable, tous âges                                        | « Learning with visualizations helps », _Educ. Research Review_ 2024 — https://www.sciencedirect.com/science/article/pii/S1747938X24000484                                                                 | résumé              | idem                                                                              |
| Estompage du concret (concreteness fading)            | revue : partir du concret, puis **estomper explicitement** vers le symbolique ; pas de méta-analyse           | Fyfe, McNeil, Son & Goldstone 2014, _Educ. Psychol. Rev._ 26(1) — https://link.springer.com/article/10.1007/s10648-014-9249-3 ; Fyfe & Nathan 2019, _Educational Review_ 71(4)                             | résumé              | R-3 : les mêmes nombres traversent T1 → T3 → T4 → T6                              |
| Matériel concret / manipulations                      | d petit à modéré, le plus fort en rétention (55 études, N = 7 237)                                            | Carbonneau, Marley & Selig 2013, _J. Educ. Psychol._ 105(2) — https://eric.ed.gov/?id=EJ1007941                                                                                                            | résumé              | l'ancrage concret est fondé ; sa **durée** ne l'est pas — d'où l'estompage        |
| CRA en éducation spécialisée (30 études à cas unique) | Tau-BC ≈ 0,997 — indice de recouvrement, **incomparable** à g                                                 | Ebner, MacDonald, Grekov & Aspiranti 2025, _LDRP_ — https://journals.sagepub.com/doi/10.1177/09388982241292299                                                                                             | résumé              | **non cité** comme effet grand public                                             |
| Représentations multiples : conditions                | n'aident que si l'élève sait **lire** chaque représentation et si les liens sont **enseignés**                | Ainsworth 2006, _Learning and Instruction_ 16(3) ; Rau 2017, _Educ. Psychol. Rev._ 29(4) — https://link.springer.com/article/10.1007/s10648-016-9365-3                                                     | résumé              | R-11 : la phrase de pont est **obligatoire**                                      |
| Comparaison de cas (analogie) comme préparation       | efficace, surtout **avant** l'instruction directe (57 expériences)                                            | Alfieri, Nokes-Malach & Schunn 2013, _Educational Psychologist_ 48(2) — https://www.tandfonline.com/doi/full/10.1080/00461520.2013.775712                                                                  | résumé              | T1 peut poser deux cas contrastés avant T2 (R-2) — jamais deux **méthodes** (R-7) |
| Analogies en classe (vidéos TIMSS)                    | les classes performantes **soutiennent** l'analogie (source visible, alignement, image)                       | Richland, Zur & Holyoak 2007, _Science_ 316 — https://www.science.org/doi/10.1126/science.1142103                                                                                                          | résumé              | R-11 : source et cible côte à côte, correspondances étiquetées                    |
| Animé vs statique                                     | dynamique > statique **g+ = 0,23** (46 études, 5 474 pp.) — petit                                             | Castro-Alonso, Wong, Adesope & Paas 2019, _Educ. Psychol. Rev._ 31(2) — https://link.springer.com/article/10.1007/s10648-019-09469-1                                                                       | résumé              | le SVG statique est un défaut défendable ; 2-3 planches pour un processus         |
| Segmentation                                          | petit à moyen, 56 investigations ; charge plus faible, temps plus long                                        | Rey et al. 2019, _Educ. Psychol. Rev._ 31(2)                                                                                                                                                               | résumé              | R-12                                                                              |
| Contiguïté spatiale (magnitude)                       | « substantiel », 50 études ; d ≈ 0,7 rapporté mais **non lu**                                                 | Ginns 2006, _Learning and Instruction_ 16(6)                                                                                                                                                               | titre / non vérifié | remplacé par Schroeder & Cenkci 2018 (A.1)                                        |
| Double codage **en classe**                           | études positives **et** nulles ; « peut se mettre en œuvre mal » ; effets réels plus petits qu'au laboratoire | EEF 2021, « Cognitive science approaches in the classroom » (Perry et al.) — https://educationendowmentfoundation.org.uk/education-evidence/evidence-reviews/cognitive-science-approaches-in-the-classroom | résumé              | une figure seulement quand elle **porte la structure** (R-10, R-11)               |
| Styles d'apprentissage                                | **aucune** preuve adéquate d'un bénéfice à apparier l'enseignement au « style »                               | Pashler, McDaniel, Rohrer & Bjork 2008, _PSPI_ 9(3) — https://journals.sagepub.com/doi/full/10.1111/j.1539-6053.2009.01038.x                                                                               | résumé              | **aucune** variante « visuel / verbal »                                           |

### A.4 Rappel, pré-questions, apprentissage génératif, « lutter d'abord » — ce qui fonde T1, T7 et ce qu'on écarte

| méthode                                        | effet                                                                                                                               | source                                                                                                                                                                                                                | statut | ce que l'étude en fait                                                                             |
| ---------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | -------------------------------------------------------------------------------------------------- |
| Rappel (se tester) en classe                   | **g = 0,50** (222 études, 48 478 élèves) ; **0,54 avec feedback** vs 0,37 sans                                                      | Yang, Luo, Vadillo, Yu & Shanks 2021, _Psychological Bulletin_ — https://pubmed.ncbi.nlm.nih.gov/33683913/                                                                                                            | résumé | T7 **avec** réponse qui redit le raisonnement (R-8)                                                |
| Rappel : revue des études appliquées           | 50 expériences en classe, 57 % d'effets moyens ou grands                                                                            | Agarwal, Nunes & Blunt 2021, _Educ. Psychol. Rev._ — https://link.springer.com/article/10.1007/s10648-021-09595-9                                                                                                     | résumé | idem                                                                                               |
| Questions **interposées** dans un texte        | mieux au quiz immédiat, **pas** au test différé : la position joue sur l'engagement, pas la rétention                               | Weinstein, Nunes & Karpicke 2016, _JEP: Applied_ 22(1) — https://www.ncbi.nlm.nih.gov/pubmed/26950160                                                                                                                 | résumé | T7 en fin de notion, sans prétendre plus                                                           |
| Pré-questions (tester avant d'apprendre)       | effet **spécifique** g = 0,54 (k = 97) ; **général** g = 0,04 ; méta 2025 : 0,66 sur le contenu visé, 0,01 ailleurs                 | St. Hilaire, Chan & Ahn 2024, _Psychon. Bull. Rev._ 31(2) — https://link.springer.com/article/10.3758/s13423-023-02353-8 ; _Educ. Psychol. Rev._ 2025 — https://link.springer.com/article/10.1007/s10648-025-10075-7  | résumé | R-2 : T1 pose **la** question de la notion ; aucun report attendu sur le reste                     |
| Résumer / dessiner                             | résumer d ≈ 0,5 (26/30 positives) ; dessiner g = 0,69 en méta **mais nul** en ligne sans entraînement                               | Fiorella & Mayer 2016, _Educ. Psychol. Rev._ ; Cromley, Du & Dane 2020 ; Lawson & Mayer 2024, _Frontiers in Psychology_ 15 — https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2024.1452385/full | résumé | `retenir` en une ligne ; **pas** de dessin à faire par l'élève                                     |
| Stratégies génératives selon l'âge             | tester et prédire marchent dès le primaire ; dessiner et questionner « largement inefficaces avant le secondaire »                  | Brod 2021, _Educ. Psychol. Rev._ 33(4) — https://eric.ed.gov/?id=EJ1319498                                                                                                                                            | résumé | à 14-15 ans, tout le patron est dans la fenêtre                                                    |
| Échec productif (résoudre avant l'instruction) | **g = 0,36** [0,20 ; 0,51] — 53 études ; 0,37-0,58 avec fidélité ; **inversé** au primaire ; cible conceptuelle                     | Sinha & Kapur 2021, _Rev. Educ. Res._ 91(5) — https://journals.sagepub.com/doi/10.3102/00346543211019105                                                                                                              | résumé | T1 en garde la part sûre (la question avant la règle) ; le « défi » complet est **hors v1** (§2.6) |
| …et sa limite : forte interactivité            | instruction explicite **d'abord** quand la tâche est complexe (N = 64 / 71)                                                         | Ashman, Kalyuga & Sweller 2020, _Educ. Psychol. Rev._ 32 — https://link.springer.com/article/10.1007/s10648-019-09500-5 ; Zhang & Sweller 2024, _Eur. J. Psychol. Educ._                                              | résumé | R-1 : une **procédure** s'explique d'abord                                                         |
| Entrelacement                                  | g = 0,42 ; maths 0,34 ; **≈ 0 sur du texte expositif** ; ECR 787 élèves : d = 0,83 en **pratique**                                  | Brunmair & Richter 2019, _Psychological Bulletin_ ; Rohrer, Dedrick, Hartwig & Cheung 2020, _J. Educ. Psychol._ 112(1)                                                                                                | résumé | **hors cours** : il vit déjà dans le Rappel et les exercices                                       |
| Théorie de la variation                        | grammaire de conception (contraste → généralisation → fusion) ; preuve **qualitative** et quasi-expérimentale, pas de méta-analyse  | Kullberg, Runesson Kempe & Marton 2017, _ZDM_ 49(4) — https://link.springer.com/article/10.1007/s11858-017-0858-4                                                                                                     | résumé | T6 : « ce qui varie / ce qui ne varie pas » — présenté comme grammaire, pas comme effet            |
| Invites métacognitives                         | g = 0,40 en environnement numérique (méta) **mais** nul dans un ECR préenregistré de 1 005 élèves de 7ᵉ sur une plateforme de maths | Guo 2022, _J. Computer Assisted Learning_ 38(3) ; Learning @ Scale 2025 — https://dl.acm.org/doi/10.1145/3698205.3729547                                                                                              | résumé | **aucune** invite « réfléchis avant » générique ; le contrôle est concret (T7)                     |
| Métacognition **enseignée**                    | + 7 mois (Toolkit EEF) — pour des stratégies enseignées, pas pour des invites dans un texte                                         | EEF 2018/2021, guidance « Metacognition and self-regulated learning »                                                                                                                                                 | résumé | hors périmètre du texte                                                                            |
| Synthèses sobres                               | laboratoire et classes contrôlées : positif et réplicable ; classes réelles : effets « mitigés » et « bien plus petits »            | Perry et al. 2021 (EEF, ci-dessus) ; Dunlosky et al. 2013, _PSPI_ 14(1) (utilité haute : se tester, espacer ; modérée : auto-explication, entrelacement)                                                              | résumé | D-8 : l'étude ne promet pas un gain ; elle installe ce qui a le plus de chances d'en produire      |

### A.5 IA 2024-2026 et guidances d'enseignement des maths — ce qui fonde D-10 et la posture

| source                                                                                                                    | ce qu'elle a prouvé                                                                                                                                                                                                                                                                        | effet                                                                                     | statut         | implication pour un cours statique                                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------- | -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Kestin, Miller, Klales, Milbourne & Ponti 2025, _Sci. Rep._ 15:17458 — https://www.nature.com/articles/s41598-025-97652-6 | un tuteur GPT-4 à garde-fous (**une étape à la fois**, jamais la solution entière, réponses courtes, raisonner avant le résultat) bat la classe active, en moins de temps                                                                                                                  | médiane 4,5 vs 3,5 ; 49 vs 60 min ; N = 194 (d ≈ 0,6-1,0 selon un tiers, **non vérifié**) | résumé         | petites étapes, brièveté, le raisonnement avant le résultat — c'est T4                                                                                         |
| Bastani et al. 2025, _PNAS_ 122(26) — https://www.pnas.org/doi/10.1073/pnas.2422633122 ; dépôt de réplication ouvert      | GPT sans garde-fous : **−17 %** à l'examen sans assistance ; GPT « tuteur » (indices, jamais la réponse) : ≈ témoin ; ≈ 1 000 lycéens turcs, maths                                                                                                                                         | −17 % / ≈ 0                                                                               | résumé         | ne jamais « donner » : l'exemple montre le raisonnement, le contrôle fait faire — et D-10                                                                      |
| Wang, Ribeiro, Robinson, Loeb & Demszky 2024/25, « Tutor CoPilot » — https://arxiv.org/abs/2410.03017                     | l'aide experte aux tuteurs élève la maîtrise, surtout chez les tuteurs faibles ; plus de questions guidantes, moins de réponses données                                                                                                                                                    | + 4 pp ; + 9 pp (tuteurs faibles) ; 900 tuteurs / 1 800 élèves                            | résumé         | les « pourquoi » et les questions guidantes **dans** le texte                                                                                                  |
| Oreopoulos & Low 2026, NBER WP 35620 — https://www.nber.org/papers/w35620                                                 | Khanmigo en mode coach, 18 collèges, deux ans : gains petits, limités par l'engagement                                                                                                                                                                                                     | ≈ 0,06-0,08 SD/an (ITT)                                                                   | résumé         | l'accès ne suffit pas : le texte doit porter le travail lui-même                                                                                               |
| De Simone et al. 2025, Banque mondiale WP 11125                                                                           | sessions guidées par l'enseignant avec GPT-4, anglais, Nigeria : gain réel ; **pas** des maths, **pas** de l'auto-étude                                                                                                                                                                    | + 0,23 SD anglais ; ≈ 800 élèves                                                          | résumé         | ne transfère pas au cas d'un cours de maths lu seul                                                                                                            |
| Google LearnLM 2024 (arXiv 2412.16429 ; cookbook)                                                                         | cinq principes (apprentissage actif, charge cognitive, adaptation, curiosité, métacognition) ; préférence d'experts, **pas** de mesure d'apprentissage                                                                                                                                     | + 31 % de préférence vs GPT-4o                                                            | résumé         | heuristiques de conception, pas preuve                                                                                                                         |
| Wang & Fan 2025 (**rétractée** 2026-04-22)                                                                                | —                                                                                                                                                                                                                                                                                          | g = 0,87 retiré                                                                           | rétractée      | **ne pas citer**                                                                                                                                               |
| EEF « Improving Mathematics in KS2 and 3 » (2017, rév. 2022)                                                              | rec. 2 « manipulations et représentations » : la base de preuve la plus forte ; conditions : raison du choix, échafaudage temporaire, liens explicites au symbole                                                                                                                          | pas d'effet par recommandation                                                            | résumé         | T3 + R-11 ; estompage (R-3)                                                                                                                                    |
| NCTM « Principles to Actions » 2014                                                                                       | « utiliser et **relier** les représentations » ; « la fluidité procédurale se construit sur la compréhension conceptuelle »                                                                                                                                                                | consensus                                                                                 | résumé         | T3 → T4 → T6                                                                                                                                                   |
| OCDE « Global Teaching InSights » 2020 (équations du second degré, 8 systèmes, ≈ 700 profs, ≈ 17 500 élèves)              | les élèves rencontrent les équations « surtout par les équations, parfois par des graphiques, **rarement en reliant les représentations** » ; liens au réel rares et faibles                                                                                                               | qualité observée basse partout                                                            | résumé         | R-11 ; R-2 (un ancrage qui pose une question, pas un décor)                                                                                                    |
| Rosenshine 2012, _American Educator_ ; Stockard et al. 2018, _Rev. Educ. Res._ 88(4)                                      | petites étapes, modèles et exemples, vérifier la compréhension, échafauder ; l'instruction explicite en maths ≈ 0,55 (328 études, programmes scriptés)                                                                                                                                     | ≈ 0,55                                                                                    | résumé         | la séquence T2 → T4 → T7 pour des novices                                                                                                                      |
| Tunisie                                                                                                                   | manuel CNP 102905 en arabe avec notation latine (13 chapitres, 221 p.) ; bascule au français en 1ʳᵉ secondaire (manuel `1ere-sec/mathematiques.md`, en français — vérifié localement) ; concours 2025 : > 33 000 candidats pour 3 750 places (presse) ; TIMSS 2011 : 425 ; PISA 2015 : 367 | —                                                                                         | local / presse | R-14 (arabe RTL, notation standard) ; Q-4 (glossaire) ; **aucune** étude trouvée sur la lecture d'un texte de maths arabe illustré — la question reste ouverte |

### A.6 En une page : ce que chaque temps du patron doit à la preuve

- **T1 Ancrer** ← mots + images (0,39), pré-question ciblée (0,54-0,66 sur la notion visée), estompage du concret (Fyfe 2014), comparaison de cas avant l'instruction (Alfieri 2013), échec productif dans sa part sûre (0,36, conceptuel) — **et** la limite d'Ashman 2020 pour les procédures.
- **T2 Nommer** ← petites étapes (Rosenshine), vocabulaire officiel (programme), une formule par ligne (notation).
- **T3 Voir** ← visualisations en maths (0,50), texte + figure intégrés (0,63), signalement (0,52), représentations reliées (Rau 2017, GTI 2020, EEF rec. 2).
- **T4 Résoudre** ← exemples résolus (0,48), exemple → problème (van Gog 2011), étiquette de principe (Atkinson 2003 ; Wittwer & Renkl 2010, petit mais sûr), brièveté (Kestin 2025).
- **T5 Distinguer** ← erronés **contrastés et expliqués** (Booth 2013, McLaren 2015, Dieterich 2025, Durkin & Rittle-Johnson 2012) — jamais avant le correct.
- **T6 Généraliser** ← concret → abstrait (Fyfe 2014 ; EEF rec. 2), variation comme grammaire (Marton), une méthode à la fois (Rittle-Johnson 2009).
- **T7 Vérifier** ← rappel avec feedback (0,50 / 0,54), estompage de l'étape porteuse (Renkl 2004, Miller-Cotto & Medrano 2026), assistance forte pour les novices (Tetzlaff 2025), jamais la réponse donnée d'avance (Bastani 2025).
- **Retenir** ← résumé en une phrase (≈ 0,5) ; le résumé en cartes sert le renversement d'expertise.
- **Écarté** : styles d'apprentissage (mythe), invites métacognitives génériques (nul à 1 005 élèves), dessin par l'élève (nul en ligne), deux méthodes côte à côte (nuit aux novices), entrelacement dans le texte (≈ 0), IA à l'exécution non gardée (−17 %), décor narratif dans l'explication (négatif).

---

## Annexe B — État du corpus pilote, compté (2026-09-16, `content/math` du dépôt privé)

**Matière** : `math` — `الرياضيات`, `contentLanguage: "ar"`, `gradeSlug: "9eme-base"`, manuel CNP
`102905`, 20 chapitres, 145 fichiers d'exercices portant 1 367 `misconceptionTag`.

| chapitre                       |    lignes | sections `##` | `<svg>` | `::: figure` | `::: methode` | `> ⚠️` | `> 🗡️` | `> 💡` | `> 🏆` |    `$$` | tableaux |
| ------------------------------ | --------: | ------------: | ------: | -----------: | ------------: | -----: | -----: | -----: | -----: | ------: | -------: |
| 01-nombres-reels               |       138 |             5 |       3 |            3 |             0 |      2 |      2 |      1 |      1 |       3 |        0 |
| 02-racines-carrees             |        82 |             6 |       1 |            1 |             0 |      2 |      1 |      1 |      1 |       6 |        0 |
| 03-calcul-litteral             |       136 |             7 |       1 |            1 |             0 |      2 |      3 |      2 |      1 |       7 |        1 |
| 04-equations-inequations       |       167 |             9 |       1 |            1 |             0 |      3 |      2 |      2 |      1 |      10 |        1 |
| 05-systemes                    |       140 |             7 |       1 |            1 |             0 |      2 |      4 |      1 |      1 |      12 |        1 |
| 06-fonctions-lineaires-affines |       138 |             7 |       1 |            0 |             0 |      2 |      1 |      1 |      1 |      11 |        2 |
| 07-statistiques                |       261 |            14 |       3 |            2 |             0 |      9 |      1 |      4 |      1 |       7 |        3 |
| 08-thales                      |       185 |             7 |       3 |            3 |             0 |      3 |      0 |      2 |      1 |      13 |        0 |
| 09-triangle-rectangle-trigo    |       169 |             7 |       3 |            3 |             0 |      5 |      2 |      2 |      1 |       9 |        2 |
| 10-angles-cercle               |       179 |             7 |       3 |            3 |             0 |      1 |      2 |      3 |      1 |      10 |        1 |
| 11-vecteurs-translation        |       168 |             6 |       3 |            3 |             0 |      1 |      2 |      1 |      2 |       9 |        1 |
| 12-repere-plan                 |       221 |             9 |       3 |            3 |             0 |      1 |      5 |      1 |      2 |      11 |        2 |
| 13-geometrie-espace            |       202 |             9 |       4 |            4 |             0 |      3 |      3 |      1 |      1 |      19 |        2 |
| 14-annales-sujets-types        |        70 |             5 |       0 |            0 |             0 |      1 |      1 |      1 |      1 |       2 |        0 |
| 15-numeration-et-calcul        |       191 |            10 |       2 |            2 |             0 |      6 |      2 |      1 |      1 |       0 |        1 |
| 16-puissances                  |       153 |             7 |       1 |            1 |             0 |      3 |      3 |      1 |      1 |      11 |        2 |
| 17-ordre-et-comparaison        |       164 |             7 |       4 |            4 |             0 |      5 |      3 |      1 |      1 |      16 |        0 |
| 18-quadrilateres               |       331 |             9 |       8 |            8 |             0 |      3 |      1 |      1 |      1 |       0 |        2 |
| 19-valeur-absolue              |       120 |             5 |       2 |            2 |             1 |      2 |      2 |      1 |      1 |       8 |        1 |
| 20-orthogonalite-espace        |       169 |            10 |       9 |            9 |             0 |      1 |      4 |      1 |      1 |       3 |        0 |
| **total**                      | **3 384** |       **153** |  **56** |       **54** |         **1** | **57** | **44** | **29** | **22** | **167** |   **22** |

Directives `definition` · `propriete` · `exemple` · `retenir` · `piege` · `astuce` : **0** dans les
20 cours. Résumés : 345 lignes, **186 cartes** (une par puce de premier niveau).

**Le manuel, dans la transcription** (`content/programmes-officiels/programme/9eme-base/maths.md`,
11 530 lignes) : 13 chapitres en 4 domaines ; **57** titres d'activité « نشاط », **7** exercices
corrigés « تمرين مرفق بحل », des encadrés de règle/définition/méthode transcrits **verbatim** dans
chaque chapitre (≈ 350 mentions), une table « Vocabulaire & terminologie officielle » par chapitre
(terme arabe → traduction française → pages), et pour chaque chapitre les bornes « inclus / absent »
du programme. Le chapitre 10 (Thalès) porte, par exemple, 12 notions dans l'ordre réel du corps du
manuel, avec les pages de chaque activité et de chaque encadré.

**Le corpus entier** (773 cours) : `::: definition` dans 17 fichiers (12 `physique-1ere-sec`,
4 `technologie-bac-techniques`, 1 `philosophie-bac`), `::: propriete` dans 13, `::: exemple` dans 2,
`::: methode` dans 4, `::: retenir` dans 3, `::: piege` dans 2, `::: astuce` dans 1.

---

## Annexe C — Gabarit d'une notion aux sept temps (arabe, pilote) : la fonction linéaire

> C'est la **graine** de `course-explanation.md` (lot 2) et le premier cas de la maquette (lot 2,
> Q-2). Prose arabe RTL, chiffres occidentaux, formules LTR seules sur leur ligne, virgule
> décimale — `math-and-notation.md` s'applique. Les libellés (تعريف · مثال محلول · تحذير · خاصّية
> · جرّب بنفسك · للحفظ) sont **émis par le renderer**, jamais écrits par l'auteur. Le `verifie`
> ne rend pas avant le lot 1 ; la maquette l'écrit quand même, pour être complète le jour où le
> lot 1 est sur `main`.

```text
## 🏰 الدالة الخطية — حين يكون الثمن متناسبًا مع الكمية

تبيع البقّالة الطماطم بـ 3 دنانير للكيلوغرام. كم تدفع مقابل 2 kg؟ ومقابل 5 kg؟ ومقابل x كيلوغرام؟
الجواب دائمًا «3 × الكمية»: 6 دنانير، ثمّ 15 دينارًا، ثمّ 3x. هذا الربط بين الكمية والثمن هو ما سنسمّيه **دالة خطية**.

::: definition
الدالة الخطية هي الدالة التي تربط كلّ عدد حقيقي x بالعدد a × x، حيث a عدد حقيقي ثابت غير معدوم يُسمّى **معامل التناسب**. نكتب:
$$ f(x) = ax $$
:::

| الكمية x (kg) | 1 | 2 | 5 | x  |
| ------------- | - | - | -- | -- |
| الثمن f(x)    | 3 | 6 | 15 | 3x |

في الجدول، السطر الثاني هو دائمًا السطر الأوّل مضروبًا في 3: هذا العدد 3 هو a في الصيغة f(x) = 3x.

::: exemple ثمن الطماطم
1. المعامل هو ثمن الكيلوغرام الواحد: a = 3، إذن f(x) = 3x — لأنّ الثمن يُضرب في الكمية.
2. صورة 2 هي f(2) = 3 × 2 = 6 — لأنّ الصورة هي الثمن الذي يقابل الكمية 2.
3. سابقة 12: نبحث عن x بحيث 3x = 12، إذن x = 4 — لأنّ السابقة هي الكمية التي يقابلها الثمن 12.
:::

::: piege الخطأ الشائع
يكتب بعض التلاميذ f(x) = x + 3 «لأنّ الثمن يزيد بـ 3». هذا خطأ: مقابل 2 kg ندفع 6 دنانير لا 5. الثمن **يُضرب** في 3 ولا **يُضاف** إليه 3؛ الدالة الخطية تعبّر عن تناسب، والتناسب ضربٌ في عدد ثابت.
:::

::: propriete
الدالة الخطية تمرّ دائمًا بالأصل O(0 ; 0)، لأنّ f(0) = a × 0 = 0: كمية معدومة ثمنها معدوم. تمثيلها البياني **مستقيم يمرّ بالأصل**، وإذا كان a سالبًا كان المستقيم نازلًا.
:::

::: verifie
ينتج صنبورٌ 4 لترات من الماء في كلّ دقيقة. عبّر عن كمية الماء f(x) بعد x دقيقة، ثمّ احسب f(7)، وأكمل: سابقة 30 هي … لأنّ …
---
f(x) = 4x، لأنّ المعامل هو ما ينتجه الصنبور في دقيقة واحدة.
f(7) = 4 × 7 = 28 لترًا.
سابقة 30 هي 7,5 دقيقة، لأنّ 4x = 30 يعطي x = 30/4 = 7,5.
:::

::: retenir
دالة خطية = تناسب: f(x) = ax، تمرّ بالأصل، ومعاملها a هو صورة العدد 1.
:::
```

| temps | où, dans le gabarit                                                                                                                                                         |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| T1    | les tomates à 3 dinars le kilo, et la question « combien pour x kilogrammes ? »                                                                                             |
| T2    | `::: definition` — le mot officiel (معامل التناسب), la formule seule sur sa ligne                                                                                           |
| T3    | le tableau de valeurs, puis la phrase de pont « ce 3 est le a de la formule »                                                                                               |
| T4    | `::: exemple` — trois étapes, les nombres de T1, chaque étape avec son « لأنّ »                                                                                             |
| T5    | `::: piege الخطأ الشائع` — l'écriture additive f(x) = x + 3, pourquoi elle tente, la correction (tag : erreur additive vs multiplicative, à déclarer dans `coursePitfalls`) |
| T6    | `::: propriete` — passage par l'origine avec son pourquoi, et le cas a < 0                                                                                                  |
| T7    | `::: verifie` — un problème jumeau (le robinet) dont la dernière étape est **à compléter**, réponse repliée qui redit chaque pourquoi                                       |
| fin   | `::: retenir` — une ligne, future carte du résumé                                                                                                                           |

La même notion, aujourd'hui, dans `06-fonctions-lineaires-affines/cours.md` : la définition en
première ligne, un exemple nu (f(x) = 3x ← f(2) = 6) sans pourquoi, aucune erreur typique, aucun
contrôle — et le taxi 110 lignes plus bas.
