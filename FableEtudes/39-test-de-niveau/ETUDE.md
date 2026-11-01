# Étude 39 — Test de niveau : le bilan de départ, partageable, sans compte comme avec

> **Statut** : **en exécution** (ouverte et arbitrée le 2026-11-01 par le propriétaire, en
> session : « un sondage initial pour connaître le niveau de l'élève et lui faire un profiling
> initial, un test d'appel partageable sur les réseaux sociaux, que même les parents peuvent
> passer, qui existe aussi dans la plateforme pour les membres et pour les profils anonymes »).
> Rédigée le même jour depuis une session cloud, sur un relevé du code du jour (`main` du
> moteur à #1215, `main` du corpus à privé#760). Les lots 1 à 3 sont **exécutés dans la session
> qui l'a rédigée** ; les questions ouvertes (§7) sont tranchées **sur recommandation, par
> défaut et réversiblement**, comme é02 l'a fait pour sa Q-1 — attendre une validation serait
> une étape manuelle (zéro intervention).
> **Priorité** : 39 · **Valeur** : 🎯 **le premier canal d'acquisition mesurable** (KPI-1 de
> l'étude 28, à zéro depuis le 2026-06-13) : un visiteur, un élève, un parent passe **dix
> questions** sur une matière de sa classe, reçoit un **bilan par chapitre** et une note sur 20
> qu'il peut **partager** (« j'ai eu 14/20 au test de niveau de maths 9ᵉ — et toi ? »), et le
> compte qu'il crée ensuite **hérite du bilan** : c'est le **bilan d'entrée** que l'étude 30
> avait différé (lot 7), livré sous sa forme non adaptative, ouverte à tous · **Complexité** :
> moyenne — une table, quatre RPC `SECURITY DEFINER`, une feature, deux routes publiques, un
> catalogue i18n dans son propre chunk, quatre événements produit ; zéro changement des RPC
> existantes
> **Architecte** : Fable (session Claude Code), 2026-11-01 · **Exécuteur cible** : Sonnet (ou
> équiv.) ; les lots 1-3 par la session architecte elle-même
> **Dépend de** : go-live C8 (plateforme publique, live) · é02 (la note /20, le percentile à
> 20 candidats, le patron « aucune clé pendant l'épreuve ») · é03 (`score_answer`, types
> natifs) · é15 (registres, gabarits) · é22 (parcours, garde d'onboarding) · é30 (le bilan
> d'entrée, §3.5 ; la source `placement` déjà prévue au modèle de croyance) · é31 (liste fermée
> d'événements, R-19/R-20) · é34 (vocabulaire sans perte) · é38 (le tunnel sans compte → compte,
> `return-to`, les événements `account_invite_clicked`/`login`) · **Bloque** : rien ;
> **informe** é30 (son lot 7 trouve ici son socle : la table, la feature, la route) et é08 (le
> bilan au rapport parent, lot 5)
> **Docs normatifs liés** : AGENTS.md, ARCHITECTURE.md §8, `docs/doctrine-verticale.md`,
> `docs/design-surfaces.md`, `docs/inventaire-traitements-inpdp.md`, `docs/xss-rendering-policy.md`
>
> **Fiche de verticalité** (doctrine verticale, é26 D-2) :
> **Verticale** : V1 « apprendre & maîtriser » — son **premier pas** (« où j'en suis ») — **et**
> fondation d'acquisition (é28 KPI-1). La capacité est **ouverte** par arbitrage humain écrit
> (la demande du 2026-11-01, citée en tête) ; elle **approfondit** deux chantiers déjà payés :
> le tunnel sans compte → compte de l'étude 38 (il gagne une entrée qui donne envie, et une
> mesure de conversion) et le bilan d'entrée de l'étude 30 (différé le 2026-08-23 « au volume
> réel » — or c'est précisément ce test qui fait venir le volume) ·
> **Maturité visée** : **M2 au lot 3, M3 au lot 4** — M3 exige la mesure (KPI-1 à KPI-4, §1.4)
> sur un premier trafic ; jamais M4 (le test n'est pas une capacité signature : la
> correction-révision, le tuteur et l'examen blanc le sont) ·
> **Boucles** : **REFERME** (a) le tunnel é38, aveugle entre `public_practice_completed` et
> `signup` — le test rend la conversion **nommable** (`placement_claimed`) ; (b) la question
> « par où commencer ? » d'un compte neuf, à laquelle l'accueil répond aujourd'hui par un
> menu de parcours (é31 constat n° 8 : « le compte naît à zéro ») — il naît désormais avec un
> bilan ; **OUVRE** une donnée, `placement_sessions`, dont les consommateurs sont **datés** :
> l'écran de résultat (lot 2, immédiat), la carte « ton bilan de départ » du Hall (lot 3, même
> session), le modèle de croyance de l'étude 30 (lot 4 — à la réouverture de ses lots 5-9,
> condition inchangée : du volume) et le rapport parent (lot 5, é08). Rien d'autre n'est
> collecté : ni adresse, ni nom, ni adresse IP — un test anonyme n'a **qu'un jeton aléatoire** ·
> **Apport IA** : **rejeté pour l'instant, motivé.** Le bilan est entièrement déterministe
> (`score_answer`, chapitres, étiquettes d'erreur du registre) ; la seule place légitime d'un
> LLM serait une **lecture rédigée** du bilan (« tu tiens les fractions, reprends les angles »),
> rang 5 de la table é26 §5 (« digest en langage naturel sur des agrégats déterministes ») — à
> ouvrir quand `user_misconceptions` cesse d'être vide, c'est-à-dire **après** ce test, pas
> dedans. Aucun LLM ne compose le test, ne corrige, ne classe (P-5a).

---

## 1. Contexte & objectif produit

### 1.1 La commande humaine (2026-11-01)

Un **sondage initial** pour connaître le niveau de l'élève et faire son **profilage initial** ;
un **test d'appel** pour que des utilisateurs viennent sur la plateforme et créent un compte ;
**partageable sur les réseaux sociaux** ; que **les parents peuvent passer** ; une **étape
d'initiation et d'intégration** ; présent **dans** la plateforme pour les membres **et** pour les
profils anonymes, pour les encourager à créer un compte.

Six exigences, et elles ne tirent pas toutes dans le même sens : un test d'appel doit être
**court, comparable et flatteur à partager** ; un profilage doit être **honnête et utile** ; un
parent n'a pas la même suite qu'un élève. Cette étude les tient ensemble en une seule mécanique :
**dix questions, une carte par chapitre, une note sur 20** — la carte est le profilage, la note
est le partage, et le compte est ce qui garde les deux.

### 1.2 L'état réel, mesuré le 2026-11-01

Relevé sur `main` du moteur (#1215), rien n'est déduit :

| Constat                                                                                                                                                                                                                                                                                                                        | Conséquence pour l'étude                                                                                                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Aucun canal d'acquisition actif** — `STATUS.md` §1bis, KPI-1 🔴 « zéro, c'est le goulot du projet » ; le chemin critique écrit en §6.0 passe par GAP-003 (INPDP, humain) et le canal enseignant. « Il ne reste rien de codable sur ce chemin avant GAP-003. »                                                                | Ce test **est** du codable : un canal **organique**, sans démarche vers un établissement (é28 D-5 reste intacte — rien ici ne s'adresse à une école), sans publicité, mesuré dans PostHog dès la mise en ligne.                         |
| **Le bilan d'entrée existe sur le papier et nulle part ailleurs** — é30 §3.5 et lot 7 : `placement_sessions`, `start_placement`, `next_placement_item`, `submit_placement_answer`, `finish_placement`, la feature `placement`, la route `_authenticated/bilan.$subjectId`. 0 occurrence dans `supabase/migrations/` et `src/`. | L'étude **reprend ses noms** (table `placement_sessions`, feature `placement`, source `placement`) et **change sa forme** (§3, D-1) : composé d'avance, pour tous, sans compte, avec une note. Ce qui diverge de é30 est écrit, pas tu. |
| Le modèle de croyance **attend déjà** la source `placement` : `belief_source IN ('evidence','inference','placement')` (20260825100000), mais `question_attempts.source` ne l'admet pas encore (`('exercise','quiz','dungeon','exam')`, différé « avec le lot qui le lit »).                                                    | L'élargissement du CHECK **n'est pas dans cette étude** (lot 4, §4) : il emporterait une suppression de contrainte avec du `src/**`, ce que le hook de pré-commit refuse (DoD §7), et il n'a pas de lecteur avant le volume.            |
| Le **registre public** sait déjà corriger sans compte : `check_answers` (clé jamais rendue, explication retenue pour l'anonyme), `score_quiz`, le lecteur partagé `ExercisePlayer`, la mesure `public_practice_completed` (é38 lot 0).                                                                                         | Le test réutilise `score_answer` (le seul juge) et la **même politique** : la bonne réponse se voit, l'explication et l'erreur nommée sont **la valeur du compte** (D-5).                                                               |
| L'**examen blanc** (é02) a posé le patron de l'épreuve : « aucune clé pendant », note /20, percentile affiché à partir de 20 candidats, JSON construit champ par champ.                                                                                                                                                        | Repris tel quel : `start_placement_session` construit son JSON à la main ; le percentile reprend le seuil 20 et sa constante partagée.                                                                                                  |
| Le **tunnel sans compte → compte** est mesuré depuis le 2026-10-30 (é38 lot 0) mais **n'a pas d'appât** : l'invitation à créer un compte promet « garde ta progression » à quelqu'un qui n'a encore rien à garder.                                                                                                             | Le bilan **est** la chose à garder : « crée ton compte pour garder ton bilan, lire les explications et commencer par ce qui manque ».                                                                                                   |
| Le chunk `i18n-` est à **0,06 Ko** de son plafond (188 Ko) ; é38 lots 2, 4, 5 attendent derrière.                                                                                                                                                                                                                              | Tout le texte du test vit dans **son propre chunk** `i18n-placement` (règle du 2026-08-26) ; seule l'entrée de navigation de l'en-tête public est app-wide (D-8).                                                                       |
| La correction retient l'explication pour l'anonyme ; `distractor_tags` est hors de portée des rôles clients ; `score_answer` et `resolve_misconception_tag` sont `REVOKE`d.                                                                                                                                                    | Aucune nouvelle surface de clé : tout passe par des RPC `SECURITY DEFINER` qui ne rendent jamais ni `correct_option` ni `distractor_tags`.                                                                                              |
| **Onze couples** niveau × matière sont au patron, étiquetés, audités, publiés (9ᵉ : 6 matières ; 6ᵉ : 4 ; `math-6eme`) — `STATUS.md` §6.1.                                                                                                                                                                                     | Le test est **ouvert à toute matière qui a de quoi le composer** (≥ 5 chapitres avec une question éligible) : il ne se limite pas aux onze, mais c'est là qu'il vaut le plus.                                                           |

### 1.3 Ce que l'étude livre, en langage produit

- **Un visiteur** ouvre `/test-de-niveau` (depuis un lien partagé, l'accueil ou l'en-tête),
  choisit sa classe et une matière, répond à **dix questions** sans correction en cours de route,
  et reçoit son **bilan** : une note sur 20, une **phrase de niveau** sans mot de perte, la **liste
  des chapitres testés** avec ce qui tient et ce qui manque, et **par où commencer** (le cours du
  premier chapitre manqué, ouvert sans compte). Il peut **partager** son résultat (texte + lien
  qui rouvre le même test) et **créer un compte** qui hérite du bilan.
- **Un parent** passe le même test (« je suis parent » : il le dit en un geste), reçoit le même
  bilan, et la suite lui parle à lui : ouvrir le suivi, créer le compte de son enfant.
- **Un élève connecté** passe le test depuis le Hall ou depuis `/test-de-niveau` ; son bilan est
  **gardé**, affiché dans le Hall (« ton bilan de départ »), et sa correction porte **les
  explications et les erreurs nommées** du registre.
- **Un compte qui vient de naître** après un test anonyme **retrouve son bilan** : les tests
  passés sur l'appareil lui sont rattachés à la première connexion, et la correction s'ouvre.

### 1.4 Objectif & indicateurs de succès

Tous lisibles dans PostHog (événements de la liste fermée, §3.7) ou dans Postgres, aucun ne
demande de volume pour exister — ils demandent du volume pour **dire** quelque chose.

| KPI       | Mesure                                                                                                                                           | Cible (premier trimestre)                  | Où on la lit                                                                  |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------ | ----------------------------------------------------------------------------- |
| **KPI-1** | **Tests commencés par semaine** sans compte, et **part partagée** (`placement_shared` / `placement_completed`)                                   | > 0, puis croissant ; part partagée ≥ 10 % | PostHog, `placement_started` · `placement_shared`                             |
| **KPI-2** | **Taux d'achèvement** (`placement_completed` / `placement_started`) et **durée médiane**                                                         | ≥ 60 % · médiane ≤ 7 min                   | PostHog ; `placement_sessions.duration_seconds`                               |
| **KPI-3** | **Conversion test → compte** : `placement_claimed` rapporté aux `placement_completed` anonymes                                                   | ≥ 10 %                                     | PostHog ; Postgres : `claimed_at IS NOT NULL`                                 |
| **KPI-4** | Part des **comptes neufs** avec un bilan dans les 7 jours (`placement_sessions` à `user_id` non nul, `started_at` ≤ `profiles.created_at + 7 j`) | ≥ 40 %                                     | Postgres (`/admin/engagement`, bloc à ajouter au lot 3 si la place le permet) |

**KPI-1 est le KPI-1 de l'étude 28** : la ligne « un canal d'acquisition actif » de
`STATUS.md` §1bis passe de 🔴 à 🟠 le jour où `placement_started` compte, et à 🟢 quand KPI-3
est lu une fois sur un mois entier.

### 1.5 Ce que cette étude ne cherche PAS à faire

- **Pas un examen blanc** (é02) : pas de chrono couperet, pas de barème par coefficient, pas de
  multi-matières. Dix questions d'une matière.
- **Pas le diagnostic adaptatif** de é30 §3.5 (un item choisi d'après la réponse précédente,
  arrêt à la frontière stabilisée) : il exige un graphe de compétences que **dix matières sur
  onze** n'ont pas, et une croyance à mettre à jour que l'anonyme n'a pas. Il reste le **lot 5**,
  daté sur la couverture du tagging (≥ 2 matières), et se branchera sur la même table.
- **Pas de récompense** : ni XP, ni pièces, ni badge pour un test (é30 R-12 « ce n'est pas une
  nouvelle économie », é31 R-18 « un bilan qui paye devient une tâche »).
- **Pas de classement** nominatif : un percentile anonyme à partir de 20 participants, jamais de
  « moyenne nationale » (é08 R-5), jamais un podium.
- **Pas de lien parent → enfant** depuis le test (le parent passe le test pour lui ; « tester
  mon enfant » est le lot 5, Q-3).
- **Pas de contenu nouveau** : le test tire dans le corpus publié. Aucune question « de test »
  n'est écrite au privé.

---

## 2. Spécification fonctionnelle

### 2.1 Acteurs & user stories

- **US-1 (visiteur, le test)** — depuis `/test-de-niveau`, je choisis **ma classe** puis **une
  matière** (seules celles qui ont de quoi composer un test sont proposées), je lis ce qui
  m'attend (« 10 questions · environ 7 minutes · ton bilan par chapitre »), je commence. Une
  question à la fois, **sans correction** en cours de route ; je peux revenir à la précédente.
- **US-2 (visiteur, le bilan)** — à la fin je vois **ma note sur 20**, une phrase qui dit où j'en
  suis **sans me rabaisser**, la liste des chapitres testés (✓ tenu / ↻ à revoir), **par où
  commencer** (le cours du premier chapitre à revoir, lisible sans compte), et ma correction :
  pour chaque question, ma réponse et la bonne. Les **explications** et les **erreurs nommées**
  sont annoncées comme ce que le compte débloque — jamais cachées sans le dire.
- **US-3 (visiteur, le partage)** — un bouton **Partager** (feuille de partage du téléphone, ou
  copie du texte) : « J'ai eu 14/20 au test de niveau de Mathématiques (9ᵉ) sur Na9ra Nal3ab 🎯
  Et toi ? <lien> ». Le lien rouvre **le même test** (classe et matière présélectionnées).
- **US-4 (visiteur → compte)** — si je crée un compte **après** le test, depuis l'écran de
  résultat ou plus tard sur le même appareil, mon bilan **m'appartient** : il apparaît dans mon
  Hall et sa correction s'ouvre en entier. Je n'ai rien à refaire.
- **US-5 (parent)** — je dis que je suis parent avant de commencer ; le test et le bilan sont
  les mêmes, la suite me parle à moi : « ouvrir le suivi de mon enfant », « créer son compte ».
  Mon score ne se mélange à aucun classement d'élèves (le percentile ne compte que les élèves).
- **US-6 (élève connecté)** — depuis le Hall (« Fais ton test de niveau — 10 min »), depuis la
  fin de l'accueil, ou depuis `/test-de-niveau`, je passe le test ; mon bilan est gardé, affiché
  dans le Hall avec **par où commencer** (lien vers le chapitre de mon parcours), et je peux le
  **refaire** quand je veux — c'est le dernier qui s'affiche.
- **US-7 (élève connecté, la correction)** — ma correction porte l'**explication** de chaque
  question et, quand je me suis trompé sur un distracteur étiqueté, **l'erreur nommée** du
  registre (é04/é30) — la même phrase que dans mes quêtes.
- **US-8 (élève, la reprise)** — si je ferme l'onglet au milieu, je retrouve mon test là où
  j'en étais en revenant sur la page (même appareil). Un test abandonné n'a aucune conséquence.

### 2.2 Règles métier

**Composition**

- **R-1** — un test = **10 questions** (`PLACEMENT_ITEMS = 10`), `mcq` ou `numeric` seulement
  (les types à planche — `ordering`, `matching` — allongent le test, `multi` brouille la note,
  `short_answer` exige un juge IA, é33). Une matière qui ne peut en fournir **5** n'est pas
  testable : elle n'est **pas proposée** (jamais un test tronqué).
- **R-2** — les questions sont tirées dans les **missions publiées** du catalogue (`source =
'admin'`, `mode <> 'quiz'` — le quiz de compréhension est une porte, pas une épreuve), **une
  par chapitre**, sur des chapitres **répartis** sur toute la matière (si la matière a plus de
  dix chapitres : dix chapitres équidistants dans l'ordre du programme ; moins : une seconde
  question par chapitre, jamais du même exercice). Dans un chapitre, une question de **palier 1
  ou 2** d'abord (socle/pratique), un boss seulement à défaut — le test cherche **où commencer**,
  pas à départager des champions.
- **R-3** — l'ordre de passage est **l'ordre du programme** (le chapitre 1 avant le chapitre 12),
  les options sont mélangées à l'affichage comme partout.
- **R-4** — **aucune correction pendant le test** (patron é02 : « il ne corrige rien »). Le
  bilan est la première fois que la bonne réponse se voit.

**Le bilan**

- **R-5** — la note est **sur 20** (`20 × justes / total`, une décimale), parce que c'est la seule
  échelle que l'élève, le parent et le réseau social lisent pareil (é02). ⚠️ Ceci **révise é30
  R-12** (« aucune note, une carte, pas un score ») pour **ce** test et lui seul, par la commande
  du 2026-11-01 : le partage est la raison d'être du test, et on ne partage pas une carte. La
  carte — ce qui tient, ce qui manque — reste la sortie **pédagogique**, affichée avant la
  correction et après la note.
- **R-6** — quatre **bandes** de niveau, nommées sans mot de perte (é34 R-1, é31 R-20) — jamais
  « faible », « échec », « en retard », « nul » :

  | Note /20 | clé          | FR                         | AR               | EN                          | la suite proposée                                 |
  | -------- | ------------ | -------------------------- | ---------------- | --------------------------- | ------------------------------------------------- |
  | ≥ 16     | `solide`     | Base solide                | أساس متين        | Solid base                  | les chapitres suivants, les missions boss         |
  | 12–15,9  | `en-route`   | En bonne voie              | في الطريق الصحيح | On the right track          | les chapitres à revoir, missions de pratique      |
  | 8–11,9   | `consolider` | À consolider               | يحتاج تثبيتًا    | To consolidate              | relire le cours des chapitres à revoir, puis quiz |
  | < 8      | `reprendre`  | On reprend depuis le cours | نستأنف من الدرس  | Start again from the lesson | le cours du premier chapitre, pas à pas           |

- **R-7** — le bilan montre **d'abord ce qui tient** (é30 RISK-3 : « une sortie qui montre ce
  qu'on sait déjà avant ce qui manque »), puis ce qui est à revoir, dans l'ordre du programme. Un
  chapitre tenu se dit « tenu ✓ », un chapitre manqué « à revoir ↻ » — jamais « raté ».
- **R-8** — **par où commencer** est toujours nommé : le premier chapitre à revoir (ordre du
  programme) → lien vers son cours public (`/chapitre/$chapterId`) ; pour un connecté, le même
  chapitre dans son parcours. Si tout est tenu : la matière (`/matiere/$subjectId`) et un mot
  pour les missions boss.
- **R-9** — le **percentile** (« mieux que 63 % des participants ») n'apparaît qu'à partir de
  **20 tests finis** sur la matière (constante partagée avec é02, `PLACEMENT_MIN_CANDIDATES`),
  compte uniquement les tests d'**élèves** (`audience = 'student'`) **non bâclés**, et n'est
  jamais une « moyenne nationale ».
- **R-10** — un test est **bâclé** (`tooFast`) sous `MIN_SECONDS_PER_QUESTION` (4 s) par
  question — règle du quiz de compréhension, réutilisée : la note s'affiche quand même, avec une
  phrase (« tu as répondu très vite : refais-le en prenant ton temps pour un bilan fiable »), et
  le test ne compte ni dans le percentile ni comme bilan du Hall.

**La correction et la valeur du compte**

- **R-11** — la **clé ne sort jamais** avant la fin : `start_placement_session` sert `prompt`,
  `options`, `questionType`, le chapitre — rien d'autre. Après la fin, la correction rend la
  **bonne réponse** à tout le monde (comme `check_answers`), et **retient pour l'anonyme**
  l'`explanation` et l'erreur nommée — exactement la politique de la correction publique
  (20260713120000). L'écran **le dit** (« les explications et l'erreur nommée s'ouvrent avec un
  compte »), il ne fait pas semblant qu'elles n'existent pas.
- **R-12** — le propriétaire d'un test (`user_id = auth.uid()`) lit tout : explication, erreur
  nommée dans sa langue (`misconceptions.label_*`), compétence. Un test anonyme **rattaché** à la
  connexion devient un test du propriétaire : la correction complète s'ouvre sans rien rejouer.
- **R-13** — ce qu'un test a produit est **enregistré, jamais recalculé** (patron du grand livre
  é34) : le score et les verdicts par question sont figés dans la ligne à la fin ; une
  question qui disparaît du corpus ensuite disparaît de la correction affichée, pas de la note.

**Le jeton, la mémoire de l'appareil, le rattachement**

- **R-14** — un test anonyme n'a **qu'un jeton** (`token`, UUID aléatoire), rendu **une fois** à
  la création. Il est la seule preuve de propriété : lire ou finir le test l'exige. Il ne porte
  aucune identité, et il n'est jamais mis dans l'URL de partage.
- **R-15** — l'appareil retient ses tests (`localStorage`, clé `na9ra.placement.v1`, au plus 5,
  30 jours) pour la reprise (US-8), l'écran « ton dernier résultat » et le rattachement (US-4).
  Les réponses du test en cours vivent en `sessionStorage` : fermer le navigateur les perd,
  recharger l'onglet non.
- **R-16** — **rattachement** : à la première connexion sur l'appareil (inscription, connexion,
  retour de Google, lien de confirmation — tout finit dans la coquille connectée), les jetons
  retenus sont envoyés à `claim_placement_sessions`, qui attache les tests **non encore
  rattachés** (`user_id IS NULL`) au compte ; l'appareil les oublie ensuite. Idempotent, borné
  (10 jetons), silencieux en cas d'échec (le test reste lisible par jeton).
- **R-17** — un test rattaché n'écrit **rien** dans le modèle d'apprentissage dans cette étude
  (D-6) ; il devient **le bilan de départ** du Hall s'il est le dernier fini, non bâclé, de sa
  matière.

**Anti-abus, vie privée, rétention**

- **R-18** — débit : anonyme **6 tests / 10 min par adresse** (limiteur local, patron
  `checkAnswersPublic`), connecté **10 / 10 min** (`check_rate_limit`) ; et une **digue
  globale** en SQL : au-delà de 120 créations anonymes par minute sur toute la plateforme,
  `start_placement_session` refuse (`PLACEMENT_BUSY`) — un robot remplit une table, pas la base.
- **R-19** — un test anonyme **non fini** est effacé après **7 jours**, un test anonyme **fini**
  après **90 jours** (`sweep_placement_sessions`, `pg_cron` quotidien, motif des vues
  matérialisées) ; un test de compte vit **avec le compte** (FK `ON DELETE CASCADE`), part dans
  `export_user_data` (dérivé des FK, GAP-024 — rien à déclarer) et dans la suppression.
- **R-20** — zéro PII : ni e-mail, ni nom, ni IP en base ; les événements produit ne portent que
  des identifiants de catalogue et des booléens (é31 D-1).

**Mesure**

- **R-21** — quatre événements rejoignent la liste fermée (é31 §3.6, amendée par écrit) :
  `placement_started` `{subject_id, audience, signed_in, from_share}` ·
  `placement_completed` `{subject_id, audience, signed_in, band, too_fast}` ·
  `placement_shared` `{subject_id, method}` · `placement_claimed` `{count}` ; et
  `account_invite_clicked` gagne la surface `placement`. Leurs consommateurs : KPI-1 à KPI-4.

### 2.3 i18n & RTL

- Tout le texte du test (`placement.*`) vit dans **`src/lib/i18n/placement/{fr,en,ar}.ts`**,
  isolé dans le chunk `i18n-placement` (règle du 2026-08-26 : une microcopy qui ne sert qu'à une
  surface paresseuse n'entre pas dans `TranslationKeys`), budget posé avec lui. `usePlacementT()`
  fusionne les deux catalogues (patron `useProgressT`).
- **Une seule** clé app-wide : l'entrée **« Test de niveau »** de l'en-tête public
  (`public.header.placement`), parce que l'en-tête n'est pas paresseux ; le plafond `i18n-` est
  relevé **du strict nécessaire** avec sa justification écrite dans
  `scripts/check-bundle-budget.mjs`.
- Les **énoncés** sont dans la langue du **contenu** (la matière), l'**interface** dans celle de
  l'élève : un test d'arabe passé en interface française montre des questions arabes (RTL par
  `content_language`, `dir` sur l'énoncé — `RichField` le fait déjà) dans un écran français.
- Vocabulaire normatif : **test de niveau** · **bilan** (jamais « diagnostic », « examen »,
  « évaluation », « note finale ») · **tenu ✓** / **à revoir ↻** · les quatre bandes de R-6.
  Interdits : tout mot de perte (é34 R-1), « premium / abonnement / payant » (phase gratuite).
- Le texte de partage est **dans la langue de l'interface** ; la note est toujours en chiffres
  occidentaux (politique du projet).

### 2.4 Hors périmètre (v1)

Le test adaptatif par compétence (é30 §3.5) · le bilan au rapport parent (é08) · « tester mon
enfant » (lien d'alliance depuis le test) · une page publique de résultat avec image Open Graph
(un second levier viral : à mesurer d'abord sur KPI-1) · l'e2e Playwright (le décor de test e2e
n'a pas cinq chapitres par matière : à poser avec le lot 5) · le multi-matières.

---

## 3. Architecture technique (décisions fermées)

### 3.1 Décisions

- **D-1 — é39 exécute le lot 7 de é30 sous une forme non adaptative, et c'est écrit.** Mêmes
  noms (`placement_sessions`, feature `placement`, `source = 'placement'`), même posture de
  sécurité, mais **composé d'avance** (dix items servis à l'ouverture) au lieu d'**un item à la
  fois** choisi par la croyance. Trois raisons : dix matières sur onze n'ont pas de graphe de
  compétences ; un test partagé doit être **comparable** (même longueur pour tous) ; l'anonyme
  n'a pas de croyance. L'API de é30 (`next_placement_item`, `submit_placement_answer`) **reste
  disponible** pour le lot 5 sur la même table : elle n'est ni contredite ni préemptée.
- **D-2 — la composition est en SQL, dans la RPC, déterministe à l'aléa près.** Une CTE :
  questions éligibles → chapitres qui en ont → dix chapitres équidistants (`floor((rang−1) ×
N / nombre)`) → une question par chapitre (palier 1-2 d'abord, aléa ensuite) → complément en
  seconde question si moins de dix chapitres. Pas de TypeScript qui tire : le serveur de
  fonctions ne voit jamais la liste des questions d'une matière.
- **D-3 — la note existe (révision de é30 R-12 pour ce test).** Cf. R-5. La carte par chapitre
  reste la sortie pédagogique ; la note est la sortie sociale. Les deux viennent du même
  `score_answer`.
- **D-4 — l'anonyme a une ligne et un jeton, pas une session serveur sans trace.** Une ligne
  `placement_sessions` à `user_id NULL`, un `token` UUID. Pourquoi une ligne : la **reprise**
  (US-8), le **rattachement** (US-4, impossible sans quelque chose à rattacher), le
  **percentile** (il faut compter), la **mesure** (KPI-2 en durée réelle). Pourquoi un jeton :
  c'est le patron du **code d'alliance** (`/suivi`, accès au porteur assumé, 122 bits), en plus
  étroit (128 bits, jamais affiché, jamais dans une URL). Le risque accepté : qui tient le jeton
  lit le bilan — un bilan sans nom.
- **D-5 — l'explication et l'erreur nommée sont la valeur du compte.** Pas une rétention
  nouvelle : c'est la politique de `check_answers` depuis le 2026-07-13 (« hint-economy
  content »), appliquée à l'identique et **annoncée** à l'écran (R-11). Un test rattaché les
  ouvre sans rien rejouer (R-12).
- **D-6 — aucun écrit dans le modèle d'apprentissage dans les lots 1-3.** `question_attempts`
  ne reçoit pas les réponses du test ; `user_misconceptions`, `user_competency_mastery` et les
  croyances ne bougent pas. Pourquoi : é30 R-13 exige que les croyances du bilan portent
  `source = 'placement'` et ne **comptent que pour 1**, ce que les trois triggers actuels ne
  savent pas faire — les brancher tels quels écrirait `evidence` à plein poids, et les amender
  dans la PR d'une surface publique mêlerait deux chantiers. Les réponses sont **gardées** dans
  la ligne (`result.questions`) : le lot 4 les rejouera dans le modèle **sans rien redemander à
  l'élève**, quand é30 rouvre ses lots 5-9.
- **D-7 — le percentile reprend é02** : seuil 20, calcul à la lecture, index partiel sur
  `(subject_id, correct_count) WHERE finished`. Élèves seuls, non bâclés (R-9/R-10).
- **D-8 — un chunk i18n à part, une clé app-wide.** Cf. §2.3.
- **D-9 — la route publique sert tout le monde**, connecté compris — comme `/exercice` et
  `/chapitre`. La route `_authenticated/bilan.$subjectId` prévue par é30 n'est pas créée : elle
  dupliquerait l'écran. L'écran est **auth-aware** (`useAuth`) : invitation pour le visiteur,
  correction complète et « voir dans mon Hall » pour le connecté.
- **D-10 — le parent passe le test pour lui.** `audience` est auto-déclaré (`student` |
  `parent`), n'ouvre aucun droit, change la suite proposée et sort du percentile. Le lien
  parent → enfant depuis le test est hors v1 (Q-3).
- **D-11 — une feature, qui n'importe aucune autre.** `src/features/placement/` ne touche ni
  `quest` (la saisie d'une question est déjà dans `@/components/game/question-input`, le rendu
  d'énoncé dans `@/components/ui/svg-figure`, les libellés dans `@/shared/lib/quest-labels`), ni
  `dashboard` (le catalogue classes × matières est lu par **la route**, qui compose), ni `auth`
  (`useAuth` est lu par la route, l'état passé en prop — patron `AiLauncher`).

### 3.2 Modèle de données (migration additive, une seule)

```sql
CREATE TABLE IF NOT EXISTS public.placement_sessions (
  id               UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  token            UUID NOT NULL UNIQUE DEFAULT gen_random_uuid(),      -- R-14
  user_id          UUID REFERENCES auth.users(id) ON DELETE CASCADE,    -- NULL = anonyme
  subject_id       TEXT NOT NULL REFERENCES public.subjects(id) ON DELETE CASCADE,
  audience         TEXT NOT NULL DEFAULT 'student' CHECK (audience IN ('student','parent')),
  status           TEXT NOT NULL DEFAULT 'running'
                   CHECK (status IN ('running','completed','abandoned')),
  question_ids     UUID[] NOT NULL,                                     -- l'ordre de passage (R-3)
  answers          JSONB NOT NULL DEFAULT '{}'::jsonb,                  -- {questionId: choice}, à la fin
  started_at       TIMESTAMPTZ NOT NULL DEFAULT now(),
  finished_at      TIMESTAMPTZ,
  duration_seconds INT CHECK (duration_seconds >= 0),
  correct_count    INT,
  total_count      INT,
  result           JSONB,              -- le SNAPSHOT (R-13) : questions[{questionId,chapterId,choice,isCorrect}], chapters[{chapterId,title,displayOrder,correct,total,hasLesson}]
  claimed_at       TIMESTAMPTZ         -- R-16 : rattaché à un compte après coup
);
-- Lectures : le Hall (dernier bilan par matière), le percentile, le balayage.
CREATE INDEX idx_placement_sessions_user_recent ON placement_sessions (user_id, finished_at DESC) WHERE user_id IS NOT NULL;
CREATE INDEX idx_placement_sessions_percentile  ON placement_sessions (subject_id, correct_count) WHERE status = 'completed';
CREATE INDEX idx_placement_sessions_sweep       ON placement_sessions (started_at) WHERE user_id IS NULL;
-- RLS : le propriétaire lit ses lignes (le Hall) ; aucune écriture cliente ; l'anonyme ne lit rien par la table.
```

`status = 'abandoned'` est posé par le balayage sur un test de compte jamais fini depuis 7 jours
(un test anonyme non fini est **supprimé**, R-19). Pas de colonne `family` (é30) : la matière
suffit tant que la composition est par chapitre.

### 3.3 Les RPC (toutes `SECURITY DEFINER`, `SET search_path = public`, JSON construit champ par champ)

| RPC                                                                                          | qui                 | rend                                                                                                                                                                                   | refuse                                                                              |
| -------------------------------------------------------------------------------------------- | ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `start_placement_session(p_subject_id TEXT, p_audience TEXT)`                                | anon, authenticated | `{ id, token, subject{id,nameFr,contentLanguage,gradeNameFr,gradeSlug,parcoursId}, questions[{id,chapterId,chapterTitle,prompt,options,questionType}] }` — **jamais** la clé           | `PLACEMENT_SUBJECT_NOT_FOUND` · `PLACEMENT_NOT_ENOUGH_QUESTIONS` · `PLACEMENT_BUSY` |
| `finish_placement_session(p_session_id UUID, p_token UUID, p_answers JSONB, p_duration INT)` | anon, authenticated | le bilan (§3.4) ; **idempotent** : un test déjà fini rend son bilan enregistré                                                                                                         | `PLACEMENT_NOT_FOUND` (id ou jeton faux — même message, pas d'oracle)               |
| `get_placement_session(p_session_id UUID, p_token UUID)`                                     | anon, authenticated | un test fini : le bilan ; un test en cours : `{ status:'running', … les questions }` (reprise). Autorisé par **jeton** ou par **propriété** (`user_id = auth.uid()`)                   | `PLACEMENT_NOT_FOUND`                                                               |
| `claim_placement_sessions(p_tokens UUID[])`                                                  | authenticated       | `{ claimed: [id…] }` — attache les tests `user_id IS NULL` au compte, `claimed_at = now()` ; ignore les jetons inconnus ou déjà rattachés                                              | `Unauthorized` sans session                                                         |
| `get_my_placement_overview()`                                                                | authenticated       | le **dernier bilan fini, non bâclé, par matière** du compte : `[{ sessionId, subjectId, subjectNameFr, scoreOn20, band, finishedAt, chaptersToReview:[{chapterId,title}] }]` (le Hall) | vide sans session                                                                   |
| `sweep_placement_sessions()`                                                                 | service (cron)      | `{ deletedAnon, abandoned }`                                                                                                                                                           | —                                                                                   |

`get_placement_percentile` n'existe pas à part : le percentile est un champ du bilan (D-7),
calculé dans `finish_` et `get_`.

**Invariants** : aucune RPC ne prend d'identifiant d'élève ; `auth.uid()` est lu en dur ;
`correct_option`, `answer_key`, `distractor_tags`, `explanation` n'apparaissent dans aucun JSON
avant la fin, et `explanation` + l'erreur nommée n'apparaissent qu'au propriétaire (R-11/R-12).
Grants : `EXECUTE` à `anon, authenticated` sur `start`/`finish`/`get` ; à `authenticated` seul
sur `claim`/`overview` ; `sweep` à personne (cron, propriétaire).

### 3.4 Le bilan (forme de sortie, validée par zod côté serveur de fonctions)

```ts
{
  id, status: "completed", finishedAt, subject: {...},
  correct, total, scoreOn20, band: "solide"|"en-route"|"consolider"|"reprendre",
  durationSeconds, tooFast,
  chapters: [{ chapterId, title, displayOrder, correct, total, held: boolean, hasLesson }],   // ordre du programme
  firstToReview: { chapterId, title } | null,                                                // R-8
  percentile: { candidates, minCandidates: 20, percentile: number|null },                    // R-9
  review: [{ questionId, chapterId, prompt, options, questionType, selectedChoice, isCorrect,
             correctChoice, explanation: string|null, misconception: {tag, labelFr, labelEn, labelAr}|null }],
  insightsLocked: boolean   // true pour l'anonyme : l'écran annonce ce que le compte ouvre (R-11)
}
```

`band` est calculé **en SQL** (une seule table de vérité, mirrorée dans
`src/shared/constants/placement.ts` pour l'affichage) ; `held` = toutes les questions du
chapitre justes.

### 3.5 Client

```
src/shared/constants/placement.ts            ← PLACEMENT_ITEMS=10, bandes, PLACEMENT_MIN_CANDIDATES=20, TTL mémoire ; zéro import .server
src/lib/i18n/placement/{fr,en,ar,index}.ts    ← le catalogue, son hook usePlacementT() ; placement.types.ts
src/features/placement/
  index.ts · placement.server.ts              ← 5 server fns (zod, débit, codes → phrases)
  placement-memory.ts                         ← mémoire d'appareil (jetons, 30 j) + brouillon de session
  placement-bilan.ts                          ← pur : bande, phrase, texte de partage, lien de partage
  components/placement-runner.tsx             ← la passation (QuestionInput, RichField, GoldProgress)
  components/placement-summary.tsx            ← le bilan (note, bandes, chapitres, correction, partage, invitation)
  components/placement-picker.tsx             ← classe → matière (présentationnel ; la route lit le catalogue)
  components/placement-hall-card.tsx          ← « ton bilan de départ » (Hall, lot 3, lazy)
  use-claim-placement-sessions.ts             ← le rattachement à la connexion (lot 3)
src/routes/_public/test-de-niveau.tsx         ← l'entrée (?matiere=, ?niveau=)
src/routes/_public/test-de-niveau_.$sessionId.tsx ← passation + bilan (une route, deux états)
```

Le lecteur **n'est pas** `ExercisePlayer` (lié à un exercice, à une session de quête, à la
correction immédiate) : le test joue dix questions de dix exercices, sans verdict en cours. Il
partage avec lui les **mêmes primitives** (saisie, énoncé, barre, libellés par langue), ce qui
est la frontière que é30 §3.11 avait prévue.

### 3.6 Sécurité

Même grille que é02/é30 : la clé ne sort d'aucune RPC avant la fin ; `score_answer` et
`resolve_misconception_tag` restent `REVOKE`d et ne sont appelées que dans les corps `DEFINER` ;
le jeton est comparé en SQL (`token = p_token`), jamais rendu après la création, jamais dans une
URL ; l'id d'un test ne suffit à rien sans jeton ou propriété ; `p_answers` est **filtré** (clés
∈ `question_ids`, valeurs ≤ 512 caractères), jamais rejeté-pour-tout ; les textes rendus passent
par `RichField`/`OptionContent` (politique XSS inchangée) ; aucune PII (R-20) ; débit (R-18).

### 3.7 Observabilité

Les quatre événements de R-21 dans la liste fermée (`product-events.ts`), visibles dans
`/admin/engagement` par le catalogue. Côté serveur, `logger` : `placement.started`,
`placement.finished` (durée, score), `placement.claimed` (nombre) — jamais un énoncé, jamais un
nom.

---

## 4. Plan d'exécution en lots

| Lot   | Contenu                                                                                                                                                                                                                                | Preuves                                                                                                          | Dépôt            |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------- |
| **0** | Cette étude, la ligne d'index, `STATUS.md` (§3, §4, §6, §9), le journal des décisions                                                                                                                                                  | `etudes:check`                                                                                                   | privé + moteur   |
| **1** | **Le socle SQL** : `placement_sessions`, les 6 fonctions (§3.3), index, RLS, grants, `pg_cron` du balayage, `types.ts` régénéré                                                                                                        | pgTAP ≥ 12 (attaque : ni clé ni explication pour l'anonyme ; jeton exigé ; rattachement idempotent ; percentile) | moteur           |
| **2** | **La surface publique** : feature, les deux routes, le catalogue `i18n-placement` + budget, les quatre événements, le sitemap, l'entrée d'en-tête et la porte de l'accueil, le partage, la mémoire d'appareil et la reprise            | Vitest (bilan pur, mémoire, server fns, runner, summary, routes) ; `verify` ; `ci:verify` (budgets)              | moteur           |
| **3** | **Le pont vers le compte** : rattachement à la connexion, « ton bilan de départ » dans le Hall, l'invitation en fin d'accueil, la correction complète du propriétaire, AGENTS.md (inventaire), ARCHITECTURE.md §8, inventaire INPDP    | Vitest (hook, carte) ; pgTAP (overview) ; `verify`                                                               | moteur           |
| **4** | **Le modèle apprend du bilan** (é30 lot 7, moitié « croyance ») : `question_attempts.source` admet `placement`, rejeu des `result.questions` des tests rattachés, `belief_source = 'placement'` et poids ≤ 1 (é30 R-13), console KPI-4 | pgTAP (R-13, non-régression é07/é30)                                                                             | moteur           |
| **5** | **Les suites mesurées** : test adaptatif par compétence (é30 §3.5) sur les matières étiquetées · « tester mon enfant » · le bilan au rapport parent (é08) · page publique de résultat (OG) · e2e Playwright                            | selon le volet                                                                                                   | moteur (+ privé) |

- [x] Lot 0 — l'étude (cette PR)
- [ ] Lot 1 — le socle SQL
- [ ] Lot 2 — la surface publique
- [ ] Lot 3 — le pont vers le compte
- [ ] Lot 4 — le modèle apprend du bilan (condition : réouverture des lots 5-9 de é30 — du volume)
- [ ] Lot 5 — les suites mesurées (condition : KPI-1 lu sur un mois)

**Stop-points** : lot 1 — aucune colonne secrète dans aucun JSON (test d'attaque pgTAP) ; lot 2
— le chunk `index-` ne bouge pas, `i18n-` ne monte que de la clé d'en-tête ; lot 3 — la garde
d'onboarding n'est pas modifiée (é38 lot 2 s'en charge) ; lot 4 — ne part pas avant le volume.

---

## 5. Stratégie de test

1. **pgTAP `106_placement_sessions.test.sql`** (décor : une matière de 6 chapitres, 2 exercices
   par chapitre, questions `mcq` et `numeric`, un boss) : composition (10 questions, un chapitre
   ≥ une fois, boss en dernier recours, ordre du programme) · refus sous 5 questions · **attaque**
   : le JSON de départ ne contient ni `correct_option`, ni `answer_key`, ni `explanation`, ni
   `distractor_tags` · `finish` sans jeton refuse · `finish` note, fige, est idempotent · l'anonyme
   ne reçoit pas l'explication, le propriétaire si · `claim` attache une fois, ignore un jeton
   déjà rattaché, exige une session · percentile `null` sous 20, calculé au-delà, parents et
   bâclés exclus · `overview` rend le dernier non bâclé par matière · `sweep` supprime l'anonyme
   périmé et abandonne le test de compte.
2. **Vitest** : `placement-bilan` (bandes aux bornes, texte de partage, lien) ·
   `placement-memory` (TTL, plafond, stockage indisponible) · `placement.server` (zod, débit,
   codes → phrases, forme du bilan) · `placement-runner` (une question à la fois, pas de verdict,
   retour arrière, validation numérique) · `placement-summary` (ce qui tient d'abord, invitation
   pour l'anonyme, correction complète pour le propriétaire, partage) · routes (présélection
   `?matiere=`, événements) · `use-claim-placement-sessions` (une fois, oubli des jetons).
3. **Gate** : `npm run verify` puis `npm run ci:verify` (budgets, coverage, build) ; pgTAP local
   (`npm run db:test:local`).
4. **Ce qui n'est pas testé ici et le dit** : l'e2e (décor insuffisant, lot 5) ; le rendu RTL
   d'un test d'arabe **vérifié à l'œil** sur la preview avant la fin de la session de garde.

---

## 6. Risques & mitigations

- **RISK-1 — le test décourage** (é30 RISK-3, probabilité haute). Mitigation : dix questions,
  palier 1-2 d'abord, ce qui tient avant ce qui manque, aucune phrase de perte, par où commencer
  toujours nommé. Décision prise d'avance : si KPI-2 < 50 % sur un mois, passer à 8 questions.
- **RISK-2 — la note humilie sur les réseaux.** Un 4/20 partagé n'est pas une bonne publicité
  pour l'élève. Mitigation : le texte de partage proposé porte la **bande** et la note ; sous
  8/20 il propose « j'ai fait le test de niveau… et toi ? » sans le chiffre (l'élève peut
  l'ajouter lui-même). Jamais automatique : rien ne part sans un geste.
- **RISK-3 — remplissage de la table par un robot.** Mitigation : R-18 (débit par adresse,
  digue globale), R-19 (balayage), aucune écriture lourde (pas de `question_attempts`).
- **RISK-4 — un test tiré sur un corpus mince dit n'importe quoi.** Mitigation : seuil de 5
  questions, un chapitre par question, les matières testables sont listées depuis la base (pas
  une liste en dur) ; le bilan d'une matière à 5-7 chapitres le dit (« test court »).
- **RISK-5 — divergence avec é30 au lot 5.** Mitigation : D-1 écrit la frontière ; la table
  porte déjà `status` et accepte un `question_ids` de longueur variable, donc un test adaptatif
  s'y range sans migration de schéma.
- **RISK-6 — le budget `i18n-`.** Mitigation : D-8 ; mesuré avant le push, écrit dans le script.

---

## 7. Questions — tranchées sur recommandation, réversibles

- **Q-1 — Une note, ou seulement une carte ?** _Recommandation : la note sur 20 **et** la
  carte_ (D-3). é30 R-12 est révisé pour ce test par la commande elle-même (« test partageable »).
  **Appliqué.** Réversible en masquant la note (une clé de bande suffit au partage).
- **Q-2 — Quelles matières ?** _Recommandation : toutes celles qui ont de quoi composer_ (R-1),
  listées depuis la base, classe par classe. **Appliqué.** Resserrer sur les classes de concours
  est un filtre d'écran, pas une migration.
- **Q-3 — Le parent : pour lui, ou pour son enfant ?** _Recommandation : pour lui en v1_ (D-10),
  avec la suite « ouvrir le suivi » / « créer son compte » ; « tester mon enfant » (le test posé
  au nom d'un enfant lié) au lot 5. **Appliqué.**
- **Q-4 — Le modèle d'apprentissage apprend-il du test dès maintenant ?** _Recommandation : non,
  lot 4_ (D-6), les réponses sont gardées pour le rejeu. **Appliqué.**
- **Q-5 — Une page publique de résultat (lien + image) ?** _Recommandation : pas avant d'avoir
  lu KPI-1 un mois_ ; le partage en texte suffit à mesurer l'appétit. **Différé (lot 5).**

---

## 8. Journal d'exécution

| Date       | Lot | PR         | Note                                                                                                                                               |
| ---------- | --- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2026-11-01 | 0   | (cette PR) | Étude rédigée sur la commande du jour ; Q-1 à Q-4 appliquées sur recommandation, Q-5 différée ; lots 1 à 3 exécutés dans la même session (moteur). |
