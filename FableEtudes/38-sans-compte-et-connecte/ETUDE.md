# Étude 38 — Sans compte et connecté : les deux modes d'usage, de bout en bout (entrée, passage, retour, réseau)

> **Statut** : **validée** (2026-10-30) — rédigée le même jour depuis une session cloud, sur un
> relevé du code du jour (`main` du moteur à #1204, `main` du corpus à privé#754) ; Q-1 à Q-3
> arbitrées par le propriétaire, toutes sur les recommandations (§7). **Aucun lot démarré** : le
> premier chantier (lots 0, 1, 3) est prêt à lancer, les lots 2, 4 et 5 attendent une place de code.
> **Priorité** : 38 · **Valeur** : 🚪 le visiteur qui lit un cours ou finit un entraînement et
> crée son compte **revient exactement là où il était**, au lieu d'atterrir au Hall des Héros puis
> dans un assistant de trois écrans ; l'élève dont la session expire en pleine quête **retrouve sa
> quête** ; les deux modes **disent le réseau** quand il manque, au lieu d'un squelette muet sans
> fin ; un connecté ne lit plus jamais « Connexion · Créer mon compte » ; et le tunnel
> « sans compte → compte », aujourd'hui aveugle avant `signup`, **se mesure** · **Complexité** :
> moyenne — zéro migration, zéro RPC ; un module partagé (`return-to`), un hook réseau, une page
> statique, trois événements produit et des retouches de routes ; le lot 2 touche une garde
> (onboarding) et le lot 4 le service worker (`smoke:shell` obligatoire)
> **Architecte** : Fable (session Claude Code), 2026-10-30 · **Exécuteur cible** : Sonnet (ou équiv.)
> **Dépend de** : go-live C8 (plateforme publique, live depuis le 2026-06-22) · é14/é15 (registres,
> gabarits, primitives) · é22 (parcours, garde d'onboarding) · é31 (liste fermée d'événements,
> R-19 « l'accueil finit sur une victoire », R-20 « l'invitation dit le gain, jamais la perte ») ·
> é34 (`anonPromise`) · guide intégré (#1179) · **Bloque** : rien ; **informe** é06 (gelée) sans la
> dégeler — voir § Hors périmètre
> **Docs normatifs liés** : AGENTS.md, ARCHITECTURE.md, `docs/doctrine-verticale.md`,
> `docs/content-voice-and-composition.md` (§1 registres, §5 erreurs), `docs/design-surfaces.md`,
> `docs/xss-rendering-policy.md`, `docs/inventaire-traitements-inpdp.md`, `e2e/README.md` ;
> antécédents : [`go-live/livrables/08-refonte-publique/audit-coexistence-public-connecte.md`](../go-live/livrables/08-refonte-publique/audit-coexistence-public-connecte.md)
> (2026-06-23) et [`plan-execution-L2-harmonisation.md`](../go-live/livrables/08-refonte-publique/plan-execution-L2-harmonisation.md)
>
> **Fiche de verticalité** (doctrine verticale, é26 D-2) :
> **Verticale** : V1 « apprendre & maîtriser » — **approfondissement** de deux capacités LIVE :
> « Plateforme publique sans login » (STATUS §3, 🟢 M2) et la coquille connectée avec sa boucle
> quête (🟢 M3). Aucune capacité nouvelle, aucun écran métier nouveau : l'entrée, le passage et le
> retour sont des jobs déjà ouverts et laissés incomplets (critère 1 de la DoE, « job complet, cas
> dégradés compris (déconnecté…) ») ·
> **Maturité visée** : **M3** pour la plateforme publique (le plancher de tout ce qui est LIVE) ;
> M3 maintenu côté connecté, où manquent les états dégradés que la DoE nomme. Pas de M4 : rien
> ici n'est une capacité signature ·
> **Boucles** : l'étude ne fait **que** refermer. (a) Les recommandations #2 (`returnTo`), #4
> (valeur du compte au bon moment) et #8 (onboarding non bloquant) de l'audit de coexistence du
> 2026-06-23, écrites, chiffrées, puis laissées « hors lot » par le plan L2 (§6) et jamais
> reprises — une analyse déjà payée qui n'a jamais atteint un écran. (b) Le funnel produit de é31,
> qui **commence à `signup`** : rien n'est mesuré avant le compte, alors que le visiteur sans compte
> est l'audience principale depuis le pivot ; trois événements neufs, consommés dès le lot 0 par
> PostHog et par la console `/admin/engagement` (qui lit le catalogue). (c) Le filet de l'élève —
> brouillon local et file d'envoi (`outbox.ts`) — qui existe depuis #938 mais que l'écran ne
> raconte pas quand le réseau tombe. **OUVRE** : rien ·
> **Apport IA** : **rejeté** — tout ici est déterministe (où revenir, quoi garder, quel registre,
> quoi dire quand le réseau manque) ; la bulle « El Ostedh » reste connectée-only et inchangée.
> Rien n'appelle un modèle.

## 0. TL;DR

**Les mots, d'abord.** Dans ce projet, « déconnecté » et « connecté » désignent l'état du
**compte**, pas celui du réseau : le tier e2e `public-anon` est décrit comme « déconnecté + vrai
backend TEST », et le chantier 08 parle de « donner de la valeur au mode connecté ». Cette étude
prend donc pour objets le **mode sans compte** (visiteur anonyme — élève, parent, enseignant) et le
**mode connecté** (élève, parent). Le réseau absent (« hors ligne ») n'est pas un troisième mode :
c'est un **état dégradé** de chacun des deux, que la DoE exige de traiter — sans rouvrir la lecture
hors-ligne, qui est l'étude 06, gelée par le propriétaire le 2026-07-20.

**Ce que le relevé dit** (§1.2, chaque ligne a sa preuve dans le code) :

1. Le parcours sans compte est fluide et sûr — lire, s'entraîner, se corriger, sans jamais heurter
   un mur de connexion (e2e `public-anon`). L'invitation à créer un compte existe aux bons endroits
   et au bon ton (é31 R-20). **Le passage au compte, lui, casse encore tout** : `auth.tsx` navigue
   en dur vers `/dashboard` (quatre fois), le lien de confirmation d'e-mail y mène aussi, la garde
   de `_authenticated` renvoie à `/auth` sans retenir d'où l'on vient, et un élève sans parcours est
   envoyé dans l'assistant d'accueil (trois écrans) avant d'atteindre quoi que ce soit. Le
   sous-titre de l'écran de connexion promet pourtant « Reprends là où tu t'étais arrêté. »
2. Un connecté voit, à **chaque chargement à froid**, le header public lui dire « Connexion ·
   Créer mon compte » pendant que la session se lit (`public-header.tsx` ignore `loading`, là où le
   lecteur et l'écran de résultat l'attendent). Sur une page de cours, il ne peut pas se
   déconnecter (le menu réglages de la coquille publique n'a pas de bloc compte).
3. Quand une session meurt (jeton refusé), l'élève est bien sorti — #938 l'a garanti — mais il
   atterrit sur `/auth` sans explication, puis sur `/dashboard` : sa quête, dont le brouillon est
   pourtant gardé sur l'appareil, est à retrouver à la main.
4. Sans réseau, **rien ne le dit** : aucun `networkMode` (défaut `online`), donc les requêtes se
   mettent en pause et les routes rendent leur squelette **sans fin** (`matiere`, `dashboard`) ;
   `navigator.onLine` n'est lu que par la file d'envoi ; la page de repli du service worker est en
   français seul, sombre seul. Le travail de l'élève est en sécurité (`outbox`, brouillon) — mais
   seul le lecteur de quête le montre.
5. La mesure s'arrête au seuil : la liste fermée de é31 compte 14 événements et le premier est
   `signup`. Aucun fait n'existe sur l'entraînement anonyme, l'invitation cliquée, la connexion, la
   session expirée. Le `distinct_id` PostHog (navigateur, `na9ra.ph_did`) survit pourtant à
   l'inscription : le tunnel est lisible dès qu'on l'instrumente.

**Ce que l'étude décide** : six lots, chacun une PR verte utile seule — **0** la mesure d'abord
(trois événements) · **1** le retour au point de départ (`return-to`, header neutre, déconnexion
depuis le contenu) · **2** l'accueil n'est plus un péage (la garde épargne la quête, choix de
classe en un geste) · **3** la session qui meurt revient au même endroit · **4** le réseau se voit
(bandeau, états « en attente du réseau », page de repli trilingue) · **5** la continuité du
visiteur sur son appareil. Zéro SQL. Trois questions, arbitrées le 2026-10-30 (§7).

## 1. Contexte & objectif produit

### 1.1 Lecture du besoin

Le besoin exprimé : « améliorer l'expérience utilisateur en mode déconnecté et en mode connecté ».
Les deux modes, dans le vocabulaire du projet (go-live 08, tier e2e `public-anon`, STATUS §3
« contenu praticable sans compte ») :

| Mode            | Qui                                                              | Ce qu'il peut faire aujourd'hui                                                                                                                                                                              | Coquille                                                         |
| --------------- | ---------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------- |
| **Sans compte** | visiteur anonyme : élève, parent (`/suivi` par code), enseignant | lire le catalogue, les cours et résumés, le manuel officiel ; s'entraîner avec correction immédiate (`check_answers`, `score_quiz`) ; passer le quiz de compréhension (porte en `sessionStorage`) ; imprimer | `_public` (registre Référence)                                   |
| **Connecté**    | élève (student), parent, admin                                   | tout ce qui précède **plus** : quêtes scorées, XP, séries, étoiles, badges, révisions, donjon, duels, examens, tuteur, rapport parent, paramétrage                                                           | `_authenticated` (registre Jeu) **et** `_public` pour le contenu |

Les deux modes partagent le **même contenu et les mêmes composants** (`SubjectHub`, `LessonReader`,
`ExercisePlayer`), rendus sous la coquille publique quel que soit l'état du compte — acquis du
chantier 08 et de son lot L2 (thème global, header auth-aware, HUD compte). Ce qui diffère est
**autour** : l'entrée, le passage de l'un à l'autre, le retour après une interruption, et ce que
chaque mode fait quand quelque chose manque (réseau, serveur, session).

L'étude traite donc **trois moments** et **un axe transverse** :

- **Entrée** — le premier contact dans chaque mode (landing, header, hall) ;
- **Passage** — sans compte → compte (inscription, connexion, confirmation d'e-mail, Google) et
  compte → sans compte (déconnexion) ;
- **Retour** — revenir après une pause : le visiteur le lendemain, l'élève connecté après une
  session expirée, l'un et l'autre après une coupure réseau ;
- **États dégradés** — réseau absent, serveur en erreur, contenu vide, dans les deux modes (DoE
  critère 1 et 3).

Le réseau est traité **dans la limite de l'étude 06** : on **dit** l'état et on **ne perd rien** ;
on ne met en cache ni cours ni données, on n'écrit rien hors-ligne de plus que ce que `outbox.ts`
fait déjà. Lire hors-ligne reste é06, gelée.

### 1.2 Le relevé — l'état réel du code au 2026-10-30

#### Ce que l'audit du 2026-06-23 recommandait, et ce qui en est livré

| #   | Recommandation de l'audit de coexistence                   | État         | Preuve dans le code                                                                                                                                                                                                                                                                              |
| --- | ---------------------------------------------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1   | Coquille adaptative + HUD compte persistant sur le contenu | ✅ livré     | `AccountHud` rendu par `public-header.tsx` pour un connecté ; thème global porté par `<html>`, pas par la coquille (`_public.tsx`)                                                                                                                                                               |
| 2   | `returnTo` au signup/login + reprise du contexte           | ❌           | `auth.tsx` : `navigate({ to: "/dashboard" })` après inscription **et** connexion, `emailRedirectTo: …/dashboard` ; `_authenticated.tsx` : `navigate({ to: "/auth", search: { mode: "login" } })` sans origine ; `/login` et `/signup` redirigent sans origine                                    |
| 3   | Activer la répétition espacée (UI)                         | ✅ livré     | é22 lot 2, `DailyReviewPanel`, `dashboard.reviewOverline`                                                                                                                                                                                                                                        |
| 4   | Récompense fantôme après l'entraînement anonyme            | 🟠           | l'invitation existe (`public.practice.inviteDesc`, é31 R-20) mais sans valeur concrète ; le résultat anonyme est neutre (`xpEarned: 0`)                                                                                                                                                          |
| 5   | Extraire un `<QcmQuestionCard>` partagé                    | ✅ autrement | un seul `ExercisePlayer` + une stratégie par registre (`/exercice` anonyme, `/quest` connecté)                                                                                                                                                                                                   |
| 6   | Nav mobile publique                                        | ✅ livré     | rangée `sm:hidden` du `PublicHeader` : Programme · Extras · Suivi parent · Connexion                                                                                                                                                                                                             |
| 7   | Trois vocabulaires dorés, `theme-color` dynamique          | 🟠           | deux thèmes depuis é14 Q-1 ; `theme-color` toujours figé `#0a0a0a` (`__root.tsx`, `offline.html`)                                                                                                                                                                                                |
| 8   | Onboarding **non bloquant**                                | ❌           | `shouldRedirectToOnboarding` : tout élève sans parcours est renvoyé à l'assistant (intention → classe → célébration) dès qu'il touche une route connectée                                                                                                                                        |
| 9   | Rate-limit anonyme distribué                               | 🟠           | connectés : RPC `check_rate_limit` ; **anonymes : limiteur mémoire par IP** (`isRateLimitedLocal`), non distribué sur Vercel — « a Transverse follow-up », dit le commentaire de `quest.practice.server.ts` ; le refus lève un français en dur (« Trop de requêtes. Réessaie dans un instant. ») |
| 10  | Badges, rotation d'objectifs, social                       | ✅ é31       | hors périmètre ici                                                                                                                                                                                                                                                                               |

Les deux ❌ sont les deux moments du **passage** ; le plan L2 (§6) les a explicitement versés au
« backlog » le 2026-06-27 et aucune étude ne les a repris depuis. C'est la boucle (a) de la fiche.

#### Le mode sans compte, écran par écran

- **Landing `/`** (`_public/index.tsx`, `public-landing.tsx`) : promesse famille, trois portes
  (élève, parent, enseignant), bande de preuve (chiffres réels du catalogue), bloc « Apprends en
  jouant » auth-aware (`gameCta` / `gameCtaAuthed`). Pour un visiteur qui revient, **rien ne
  reprend** : pas de « dernier chapitre lu ».
- **Catalogue → matière → cours** : le hub (`subject-hub.tsx`) fusionne la porte quiz serveur et
  la porte anonyme (`anon-quiz-gate.ts`, clé `na9ra.anonQuizPassed` en **`sessionStorage`**) ; les
  étoiles sont dessinées vides avec `anonPromise` « Connecte-toi pour garder tes étoiles. » ; la
  ligne Rappel est verrouillée avec sa raison (`recallLockedHintAnon`). Le lecteur
  (`lesson-reader.tsx`) porte l'invitation douce, **gardée tant que la session se lit**
  (`!authLoading && !isAuthenticated`, l. 482) — le bon réflexe, absent du header.
- **Entraînement `/exercice/$id`** : même lecteur que la quête, stratégie anonyme (ni XP, ni indice,
  ni boss), correction immédiate ; le quiz réussi (score **et** rythme, `MIN_SECONDS_PER_QUESTION`)
  marque la porte en session et propose la première mission ; l'écran de résultat porte
  l'invitation (« Sans compte, tes XP, ta série et tes badges ne sont pas conservés… ») vers
  `/signup` — **sans origine**. Une porte réussie meurt avec l'onglet.
- **Parent sans compte `/suivi`** : code Alliance, mémorisé sur l'appareil (case cochée par
  défaut), deep-link `?code=`. Le lien « Suivi parent » est dans le header public **pour tout le
  monde**, élève connecté compris.
- **Ce que l'anonyme ne voit jamais** : la bulle IA (`AiLauncher` rend `null`), le guide garde ses
  cartes de première visite (`guide-storage.ts`, `localStorage`) — un précédent de **continuité
  locale sans compte** déjà accepté.
- **Sécurité** : inchangée et saine — clé de réponse jamais servie (`check_answers` stateless,
  `scoreQuizPublic` agrégé), `profiles`/`attempts` fermés à l'anonyme (e2e `public-anon/security`).

#### Le passage sans compte → compte

- `/signup` et `/login` sont des redirections vers `/auth?mode=…` **sans** paramètre d'origine
  (`login.tsx`, `signup.tsx`).
- `auth.tsx` : après `signUp` avec session → `/dashboard` ; après `signInWithPassword` →
  `/dashboard` ; `onAuthStateChange(session)` → `/dashboard` (couvre Google) ; `emailRedirectTo` →
  `/dashboard` (le lien de confirmation **et** le renvoi). Le sous-titre de connexion dit
  « Reprends là où tu t'étais arrêté. » — l'écran fait le contraire.
- La garde de `_authenticated.tsx` envoie un visiteur sans session sur `/auth?mode=login` et oublie
  la route demandée : un lien `/quest/<id>` partagé, ou une quête tapée depuis un hub public par un
  visiteur, se termine au Hall.
- `shouldRedirectToOnboarding` (`onboarding-guard.ts`) : élève avec profil et sans
  `current_parcours_id` ⇒ `/onboarding`, assistant à trois pas (intention, classe, célébration avec
  pack de bienvenue é31 R-19). Rien ne permet de **différer** ; or `start_exercise_session`
  (migration `20260929120000`) ne connaît **aucune** porte « parcours » : premium (dormant), quiz,
  rappel — un élève sans parcours peut jouer une quête scorée, l'assistant n'est qu'un préalable
  d'affichage.
- La porte quiz anonyme (`sessionStorage`) n'est **ni lue ni migrée** à l'inscription : le chapitre
  déverrouillé en anonyme se referme pour le compte neuf (la porte connectée lit `attempts`).

#### Le mode connecté — coquille, hall, retour

- **Header public pour un connecté** : `public-header.tsx` lit `user` sans `loading` ; à chaque
  chargement à froid le connecté voit « Connexion · Créer mon compte » puis le HUD. Le
  `SettingsMenu` public n'a pas de `onSignOut` : pas de déconnexion depuis un cours.
- **Landing pour un connecté** : la page marketing complète ; seuls le logo (→ `/dashboard`) et
  deux CTA sont auth-aware. Aucune reprise (« ta dernière mission… »).
- **Hall `/dashboard`** : dense et complet (é15, é22, é30, é31, é34), squelette de chargement,
  état d'erreur avec « Réessayer », sortie sur refus de session. **Sans réseau** :
  `isLoading || !data` ⇒ `DashboardSkeleton` indéfiniment, aucun message.
- **Quête** : brouillon local toutes les 20 s et à `pagehide` (étage 1), file d'envoi avant la
  tentative (étage 2, `outbox.ts`, flush à `online`), indicateur `savePending` / `saveDone`,
  reprise « Reprendre ma copie » ; `client_errors` reçoit `quest-submit`, `outbox-*`,
  `public-submit`. **C'est solide, et invisible hors du lecteur.**
- **Session expirée** : `useExitOnRefusedSession` (racine et hall) → `signOut({ scope: "local" })`
  → garde → `/auth?mode=login` → connexion → `/dashboard`. Le message `errors.sessionExpired`
  (« Ta session a expiré. Reconnecte-toi pour enregistrer ta progression. ») n'est affiché que par
  `error-message.ts` dans un toast de mutation — jamais sur l'écran de connexion où l'élève arrive.
- **Déconnexion volontaire** : `signOut()` dans `_authenticated.tsx` → toast → `/`.

#### Le réseau, dans les deux modes

- `router.tsx` ne pose pas de `networkMode` : défaut `online` de TanStack Query 5 — hors-ligne,
  une requête neuve reste `pending` avec `fetchStatus: "paused"` ; `isLoading` retombe à `false`
  mais `data` est `undefined`, et toutes nos routes rendent alors leur squelette ou `LoadingState`
  (`programme`, `extras`, `niveau`, `matiere`, `chapitre`, `dashboard`, `parcours`). Au retour du
  réseau, la requête repart seule — l'écran n'a juste jamais dit pourquoi il attendait.
- `public/sw.js` : assets `/assets/*` en cache-first, navigation **réseau seul** avec repli
  `/offline.html` (jamais de HTML en cache — bon choix, conservé). `offline.html` : français seul,
  sombre seul, un bouton « Réessayer ».
- `navigator.onLine` et l'événement `online` ne sont écoutés que par `outbox.ts`. Aucun bandeau,
  aucun état « hors connexion » dans l'UI.
- Côté anonyme, l'échec de correction donne `practice.checkError` (« Impossible de corriger pour le
  moment. Réessaie dans un instant. ») — le même mot pour un réseau coupé et pour un refus du
  rate-limit, que le serveur lève d'ailleurs en **français en dur** dans un `throw`
  (`quest.practice.server.ts`, « Trop de requêtes. Réessaie dans un instant. ») : un bug au sens de
  la charte §5, qui veut des codes stables traduits côté client.

#### La mesure

- `product-events.ts` : liste fermée de 14 événements, catalogue lu par `/admin/engagement`
  (`live` par événement). Le premier est `signup` (`role`, `needs_confirmation`). Rien avant :
  ni entraînement anonyme terminé, ni invitation cliquée, ni connexion, ni session expirée.
- PostHog : `distinct_id` par navigateur (`na9ra.ph_did`, `localStorage`), profils de personne
  désactivés (D-1 de é31, protection des mineurs). Le même identifiant porte les événements d'avant
  et d'après l'inscription : un **funnel par navigateur** est lisible sans aucune PII.
- La rétention se lit dans Postgres (`admin_engagement_overview`, cohortes d'inscription). Aucune
  de ces lectures ne voit le visiteur **avant** le compte.

### 1.3 Résultat attendu

Un visiteur et un élève traversent les trois moments **sans rupture ni cul-de-sac**, et chaque
mode dit son état dégradé :

- **Passage** : après inscription ou connexion (mot de passe, Google, lien de confirmation ouvert
  dans le même navigateur), on revient **à l'URL de départ** ; l'assistant d'accueil ne s'interpose
  plus entre un élève et la quête qu'il a tapée — le choix de classe se fait en **un geste**, là où
  il est, ou plus tard.
- **Retour** : une session expirée mène à un écran de connexion qui **dit** pourquoi et qui
  **ramène** à la page quittée ; le visiteur retrouve son dernier chapitre (Q-1).
- **Cohérence** (DoE 5) : aucun libellé n'affirme un état de compte avant que la session soit lue ;
  la déconnexion est possible partout où le HUD est visible.
- **Réseau** (DoE 1 et 3) : un bandeau unique dans les deux coquilles, des écrans qui disent « en
  attente du réseau » au lieu d'un squelette, une page de repli trilingue dans les deux thèmes, et
  le compte des missions en attente d'envoi visible hors du lecteur.
- **Mesure** (P-6) : le tunnel sans compte → compte se lit dans PostHog, et son instrumentation
  s'affiche dans `/admin/engagement`.

### 1.4 Indicateurs (P-6 — « mesurer ou ne pas prétendre »)

| KPI       | Définition                                                                                                             | Où on le lit                                | Cible                                                                                                                                                    |
| --------- | ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **KPI-1** | tunnel : navigateurs avec ≥ 1 `public_practice_completed` qui émettent `signup` sous 7 jours                           | PostHog, insight « funnel » (lot 0 le pose) | **instrument d'abord** : la valeur se fixe après quatre semaines de relevé — KPI-1 de STATUS §1bis est à zéro, il n'y a pas encore de trafic à convertir |
| **KPI-2** | contexte gardé : `signup` et `login` partis d'une page de contenu (`from_content = true`) avec `return_to_kept = true` | PostHog (propriétés des deux événements)    | ≥ 90 % (le reste = confirmation d'e-mail ouverte dans un autre navigateur, RISK-2)                                                                       |
| **KPI-3** | sortie sans cul-de-sac : `login{reason: "expired"}` avec `return_to_kept = true`                                       | PostHog                                     | ≥ 90 %                                                                                                                                                   |

L'invariant « aucun squelette sans fin » n'est pas un KPI : il se **prouve** par l'e2e hors-ligne
du lot 4, pas par une courbe.

### 1.5 Ce que l'étude ne cherche PAS à faire

- **Lire hors-ligne** (cache de cours, persistance de requêtes, précache) : étude 06, gelée.
  Réversible par le seul propriétaire ; cette étude n'y touche pas et ne la contourne pas.
- **Écrire hors-ligne** au-delà de l'existant : aucune file nouvelle, aucune tentative différée de
  plus que `outbox.ts`.
- **Donner plus de valeur au compte** (badges, objectifs, social) : é31, livrée ; ni paywall ni
  vocabulaire commercial (phase gratuite, é01 gelée).
- **Refondre** le hall, le lecteur ou l'assistant d'accueil : é14/é15/é22, livrées. On déplace la
  porte, on ne redessine pas la maison.
- **SEO, performance, accessibilité** : couverts par leurs propres documents
  (`performance-audit.md`, e2e `a11y`) ; l'étude n'y régresse pas (budget du chunk d'entrée,
  RISK-6).
- Le **parent connecté** au-delà de deux redirections de bon sens (R-14).

## 2. Spécification fonctionnelle

### 2.1 Acteurs & parcours

Acteurs : **V** visiteur sans compte (élève, parent, enseignant) · **E** élève connecté · **P**
parent connecté · **A** admin (inchangé, hors périmètre).

- **US-1** (V → E, contexte gardé) — Visiteur qui lit un chapitre ou termine un entraînement, je
  crée mon compte (e-mail ou Google, avec ou sans confirmation d'e-mail) et je **reviens
  exactement sur la page où j'étais**, avec le HUD de mon compte neuf.
- **US-2** (E, accueil différable) — Élève sans classe choisie, je tape une quête depuis un hub de
  matière : je **joue la quête** ; une carte me propose la classe du chapitre (« Tu es en 9ᵉ ? ») en
  un geste, ou « plus tard ». L'assistant complet reste là où je n'ai rien demandé de précis (le
  hall).
- **US-3** (E, session expirée) — Ma session meurt pendant une quête : j'arrive sur l'écran de
  connexion avec « Ta session a expiré… », je me reconnecte et je **retrouve ma quête**, avec les
  réponses que l'appareil a gardées (« Reprendre ma copie »).
- **US-4** (E, cohérence) — Connecté, je ne lis **jamais** « Connexion · Créer mon compte », ni une
  invitation à créer un compte, même une demi-seconde au chargement ; je peux me déconnecter depuis
  n'importe quelle page où mon HUD est affiché.
- **US-5** (V et E, réseau) — Le réseau tombe : un bandeau le dit, les écrans qui ne peuvent pas
  charger disent « en attente du réseau » avec un bouton, et tout repart seul au retour du réseau,
  sans recharger. Si une mission attend d'être envoyée, le bandeau le compte.
- **US-6** (V, continuité — Q-1) — Je reviens le lendemain sur le même appareil : l'accueil et le
  programme me proposent « Reprendre : {chapitre} », et les quiz que j'avais réussis sont toujours
  réussis.
- **US-7** (E → V, déconnexion) — Je me déconnecte depuis un cours : je **reste sur le cours**, en
  visiteur ; depuis mon espace : j'arrive sur l'accueil. Aucune donnée de compte ne reste à
  l'écran.
- **US-8** (V, erreur honnête) — Ma correction anonyme échoue : le message distingue « pas de
  réseau » de « trop d'essais, patiente une minute ».
- **US-9** (A, mesure) — Dans `/admin/engagement`, je vois les trois événements neufs **live**, et
  je sais où lire le tunnel.

#### Flux écran par écran (états vide / chargement / erreur / verrouillé-avec-raison)

| Écran                                                 | Aujourd'hui                                               | Cible                                                                                                                                                                                                                    |
| ----------------------------------------------------- | --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Header public, session en lecture                     | « Connexion · Créer mon compte » (flash pour un connecté) | **bloc neutre** (réglages + aide seuls) jusqu'à `loading = false`, puis CTA ou HUD — SSR identique (R-6)                                                                                                                 |
| Header public, connecté                               | HUD, pas de déconnexion                                   | HUD + menu réglages avec bloc compte (« Tous les paramètres », « Se déconnecter ») (R-11)                                                                                                                                |
| Invitations (lecteur, résultat, hub, landing, header) | lien `/signup` ou `/login` nu                             | lien avec `returnTo` = page courante ; sur le résultat d'entraînement, la **valeur** du compte en gain futur : « Avec un compte, cette mission vaut jusqu'à {xp} XP » (R-8, D-6)                                         |
| `/auth`                                               | formulaire ; après succès → `/dashboard`                  | lit `?returnTo`, le mémorise (R-2) ; bandeau d'explication si `reason=expired` (R-7) ; après session → destination R-3 ; `emailRedirectTo` → `/auth`                                                                     |
| `/auth`, confirmation d'e-mail envoyée                | interstitiel « Confirme ton email »                       | inchangé + une ligne : « Ouvre le lien sur cet appareil pour revenir à {page} » quand un retour est mémorisé                                                                                                             |
| `/quest/$id`, élève sans parcours                     | redirigé vers `/onboarding` (3 pas)                       | la quête se joue ; **carte `ParcoursQuickPick`** au-dessus du lecteur : « Ce chapitre est en {parcours} — c'est ta classe ? » [Choisir] [Plus tard] (R-5) ; après [Choisir] : pack de bienvenue, toast « C'est parti ! » |
| `/dashboard`, élève sans parcours                     | redirigé vers `/onboarding`                               | **inchangé** (l'assistant est le bon écran quand on n'a rien demandé de précis)                                                                                                                                          |
| `/auth` après refus de session                        | formulaire muet                                           | « Ta session a expiré. Reconnecte-toi pour enregistrer ta progression. » + retour mémorisé (R-7)                                                                                                                         |
| Toute route, requête en pause réseau                  | squelette / « Chargement… » sans fin                      | `EmptyState` « En attente du réseau » (icône `WifiOff`) + « Réessayer » ; au retour du réseau, la requête repart et l'état disparaît (R-9)                                                                               |
| Toute page, hors connexion                            | rien                                                      | **bandeau** sous le header : « Hors connexion — en attente du réseau. » ; si `pendingCount > 0` : « · {n} mission en attente d'envoi » (R-9, R-12)                                                                       |
| Navigation complète hors-ligne                        | `/offline.html` FR, sombre                                | page trilingue (FR · EN · AR empilés, `dir="rtl"` sur le bloc arabe), `prefers-color-scheme`, « Réessayer » (R-10)                                                                                                       |
| `/` et `/programme`, visiteur revenant                | rien                                                      | carte « Reprendre : {chapitre} › » + « oublier » ; visiteur sans session seulement (R-13, Q-1, Q-2)                                                                                                                      |
| Hub de matière, visiteur revenant                     | portes quiz perdues avec l'onglet                         | portes réussies conservées 30 jours (R-13, Q-1)                                                                                                                                                                          |
| Résultat anonyme, correction en échec                 | « Impossible de corriger pour le moment. »                | hors-ligne : « Pas de réseau — réessaie quand il revient. » ; `429` : « Trop d'essais — patiente une minute. » ; sinon l'actuel (R-15)                                                                                   |

Mobile-first (la coquille publique est lue d'abord sur téléphone) et **RTL vérifié au rendu** pour
le bandeau, la carte `ParcoursQuickPick`, la carte « Reprendre » et la page de repli.

### 2.2 Règles métier

**Le retour (`returnTo`)**

- **R-1** — Un chemin de retour est **interne** : commence par un seul `/`, pas de `//`, pas de
  `\`, pas de schéma, ≤ 512 caractères ; le fragment (`#…`) est **retiré** ; les chemins `/auth*`,
  `/login`, `/signup` sont refusés (ils boucleraient). Tout chemin invalide ⇒ **ignoré en
  silence**, destination par défaut (R-3). Fonction pure `isSafeReturnPath`, testée (cas :
  `//evil.tn`, `https://…`, `/auth?mode=login`, `javascript:`, chemin avec `?variant=recall`).
- **R-2** — Le retour voyage **dans l'URL** (`/auth?mode=signup&returnTo=/chapitre/x`) et se
  **mémorise sur l'appareil** à l'arrivée sur `/auth` (`localStorage`, clé `na9ra.returnTo.v1`,
  `{ path, reason?, at }`, TTL **24 h**). L'URL sert les liens et le partage ; la mémoire sert la
  confirmation d'e-mail et l'aller-retour Google, qui reviennent sur `/auth` sans paramètre. Une
  seule source au moment de décider : la mémoire (l'URL n'y fait qu'écrire).
- **R-3** — Destination après qu'une session existe : le retour mémorisé s'il est valide et non
  périmé, **sinon** `hubRouteForRole` (le hall ; le hall renvoie déjà un parent à son rapport). La
  mémoire est **consommée** (effacée) à la première navigation, succès ou non.
- **R-4** — Qui écrit un retour : toutes les invitations (lecteur, résultat d'entraînement, raison
  du Rappel verrouillé, bloc « Apprends en jouant », CTA du header), la garde de `_authenticated`
  (la route demandée, `pathname + search`), et la sortie sur refus de session (R-7). Personne
  d'autre.

**L'accueil différé**

- **R-5** — `shouldRedirectToOnboarding` n'envoie **pas** à l'assistant un élève dont la route
  demandée commence par `/quest/`. Sur la quête, un élève `student` sans `current_parcours_id` voit
  la carte `ParcoursQuickPick` (le parcours du chapitre, un seul bouton d'adoption, un « plus
  tard » qui ferme la carte pour la session de navigation). « Choisir » appelle `setCurrentParcours`
  puis `claimWelcomePack` — les **mêmes** server fns que l'assistant, le même pack de bienvenue
  (é31 R-19) : l'élève ne perd rien à ne pas passer par l'assistant. `onboarding_completed` part
  avec `source: "quest_card"` (l'assistant émet `source: "wizard"`). Le hall garde sa redirection.

**La cohérence du compte à l'écran**

- **R-6** — Aucun libellé qui **affirme un état de compte** (« Connexion », « Créer mon compte »,
  « Mon espace », une invitation) n'est rendu tant que `useAuth().loading` est vrai. Le SSR rend
  l'état neutre ; l'hydratation ne change rien avant la lecture de session. La règle s'applique au
  header public, à la landing et à toute invitation (le lecteur et le résultat l'appliquent déjà).

**La session qui meurt**

- **R-7** — Quand un refus de session atteint l'écran (`useExitOnRefusedSession`), **avant**
  `signOut`, la route courante est mémorisée avec `reason: "expired"`. `/auth` affiche alors
  `errors.sessionExpired` en tête de formulaire, et `login` part avec `reason: "expired"`.
  Rien ne change au mécanisme de sortie lui-même (#938, #969) : une seule règle de redirection,
  la garde.

**L'invitation**

- **R-8** — L'invitation du résultat d'entraînement porte la **valeur** de la mission :
  `exercises.xp_reward` est déjà servi aux deux registres (`getExercise` renvoie la ligne
  `exercises` entière) et le lecteur le transmet au pied de résultat (§3.2) ; la phrase est un
  **gain futur** (« Avec un compte, cette mission vaut
  jusqu'à {xp} XP »), jamais une perte ni un reproche (é31 R-20 inchangée). Pas de chiffre quand
  `xp_reward` est nul ou absent — la phrase actuelle reste. Chaque invitation cliquée émet
  `account_invite_clicked{surface}`.

**Le réseau**

- **R-9** — Une seule source de vérité réseau côté client : `onlineManager` de TanStack Query
  (celui qui met déjà les requêtes en pause) — pas un second écouteur `online`/`offline`. Hors
  connexion : bandeau unique sous le header des **deux** coquilles ; toute route qui attend une
  requête `fetchStatus === "paused"` sans `data` rend l'état « en attente du réseau » (jamais un
  squelette). Au retour : rien à faire, TanStack relance ; le bandeau disparaît. Le bandeau affiche
  `pendingCount()` de l'outbox quand il est > 0.
- **R-10** — `offline.html` est **statique et sans script** (la CSP par nonce ne le couvre pas) :
  texte FR, EN, AR empilés, le bloc arabe en `dir="rtl"` et `lang="ar"`, couleurs par
  `prefers-color-scheme` (pas nos thèmes : la page vit hors de React), un seul bouton « Réessayer »
  (`location.reload()` en attribut `onclick` est interdit par la CSP ⇒ un **lien** vers `/`).
  `sw.js` passe `VERSION` à `v2` pour invalider la page cachée.
- **R-11** — Rien n'est mis en cache de plus. Aucune requête n'est persistée. Aucune mutation
  nouvelle n'est différée. (Le stop-point de é06 vaut ici comme invariant.)

**Registres & i18n**

- **R-12** — Le bandeau réseau et les états « en attente » sont lus par les deux audiences : ils
  sont écrits **sans pronom** (« Hors connexion — en attente du réseau. »). La carte
  `ParcoursQuickPick` tutoie (élève connecté) ; la carte « Reprendre » vouvoie ou reste neutre
  (public, Référence) — `content-voice-and-composition.md` §1. Toutes les clés existent en FR/EN/AR
  (§2.3) ; la page de repli est trilingue par construction.

**La continuité du visiteur (Q-1)**

- **R-13** — Sur l'appareil seulement, jamais au serveur : les portes quiz réussies passent de
  `sessionStorage` à `localStorage` avec un horodatage et un TTL de **30 jours** (Q-1, arbitrée) ; le dernier
  chapitre lu est mémorisé (`{ chapterId, subjectId, title, locale, at }`) et proposé sur `/` et
  `/programme` ; un bouton « oublier » efface les deux. Aucun score, aucune réponse, aucune donnée
  personnelle ; `localStorage` indisponible ⇒ comportement actuel (porte « fermée », pas de
  reprise) — le sens sûr, comme `anon-quiz-gate.ts` le fait déjà. La déconnexion d'un compte ne
  touche pas cette mémoire (un identifiant de chapitre n'est pas une donnée de compte). La carte
  « Reprendre » ne s'adresse qu'au visiteur **sans session** : la landing d'un connecté reste telle
  quelle (Q-2).

**Le parent**

- **R-14** — Un parent **connecté** qui ouvre `/suivi` est renvoyé sur `/parent-report` (son
  espace a plus que le rapport public) ; le lien « Suivi parent » du header public n'est pas rendu
  pour un **élève** connecté (son header est celui d'un élève). Le parent sans compte ne change pas.

**L'erreur honnête**

- **R-15** — Les erreurs de correction anonyme se distinguent **par leur cause**, pas par un mot
  unique : hors-ligne (R-9) ⇒ « Pas de réseau — réessaie quand il revient. » ; rate-limit ⇒
  `checkAnswersPublic` et `scoreQuizPublic` lèvent le **code stable** `RATE_LIMITED` (à la place du
  français en dur d'aujourd'hui) et le client dit « Trop d'essais — patiente une minute. » ; sinon
  `practice.checkError` actuel. Codes stables traduits côté client (charte §5), jamais de français
  en dur dans un `throw`.

**La mesure**

- **R-16** — Trois événements rejoignent la **liste fermée** (`ProductEventName`) et le catalogue :
  `public_practice_completed{exercise_id, is_quiz, passed}` (succès de `scoreQuizPublic` ou
  `checkAnswersPublic`), `account_invite_clicked{surface: "reader" | "practice" | "hub" |
"landing" | "header"}`, `login{method: "password" | "google", reason: "fresh" | "expired",
return_to_kept, from_content}`. `signup` gagne `return_to_kept` et `from_content`.
  `onboarding_completed` gagne `source`. **Zéro PII** (D-1 de é31) : identifiants de catalogue et
  booléens, rien d'autre ; `$process_person_profile: false` inchangé.

### 2.3 i18n

Clés neuves (FR/EN/AR, RTL vérifié au rendu) : `offline.banner`, `offline.bannerPending` (`{n}`),
`offline.waiting`, `offline.retry`, `offline.checkError`, `practice.rateLimited` (dans `public`),
`auth.expiredHint`, `auth.returnHint` (`{page}`), `onboarding.quickPickTitle` (`{parcours}`),
`onboarding.quickPickCta`, `onboarding.quickPickLater`, `public.resume.title`,
`public.resume.cta`, `public.resume.forget`, `public.practice.inviteValue` (`{xp}`),
`settings.signOut` réutilisée dans la coquille publique. Les `TranslationKeys` font échouer `tsc`
sur toute langue manquante ; le catalogue `public.*` reste dans son chunk (budget `i18n`).

### 2.4 Hors périmètre (v1)

Tout le §1.5, plus : un `returnTo` **inter-appareils** (confirmation d'e-mail ouverte sur un autre
appareil — fallback hall, mesuré par KPI-2) ; la migration serveur des portes quiz anonymes
(D-2) ; une refonte de l'assistant d'accueil (il reste, pour le hall) ; une bibliothèque PWA
(`vite-plugin-pwa` est le lot 1 de é06, gelé) ; le `theme-color` dynamique (ligne 7 de l'audit —
une ligne de `__root.tsx`, à prendre en passant dans le lot 4 si le smoke le permet, sinon rien).

## 3. Architecture technique (décisions fermées)

### 3.1 Modèle de données

**Aucune table, aucune colonne, aucune migration, aucune RPC.** Tout vit côté client et dans les
server fns existantes. La seule donnée nouvelle est **locale** (R-2, R-13) : deux clés
`localStorage` versionnées, lues et écrites de façon défensive (SSR, navigation privée, quota —
même discipline que `outbox.ts` et `guide-storage.ts`).

| Clé                     | Contenu                                                                                     | TTL        | Écrite par                                                                      | Lue par                           |
| ----------------------- | ------------------------------------------------------------------------------------------- | ---------- | ------------------------------------------------------------------------------- | --------------------------------- |
| `na9ra.returnTo.v1`     | `{ path: string, reason?: "expired", at: number }`                                          | 24 h       | `/auth` (depuis `?returnTo`), garde `_authenticated`, `useExitOnRefusedSession` | `/auth` (consommé une fois)       |
| `na9ra.anonQuizPassed`  | **existante** — passe de `sessionStorage` à `localStorage` au lot 5 : `{ [chapterId]: at }` | 30 j (Q-1) | `exercice.$exerciseId` (quiz réussi)                                            | hub, chapitre, exercice (anonyme) |
| `na9ra.anonLastChapter` | `{ chapterId, subjectId, title, locale, at }`                                               | 30 j (Q-1) | `chapitre.$chapterId` (anonyme, après chargement)                               | `/`, `/programme` (anonyme)       |

### 3.2 Server

**Une server fn nouvelle, en lecture seule** (`getExerciseParcours`), **une forme d'erreur** à
corriger, **zéro RPC nouvelle** et zéro migration. Relevé du 2026-10-30, sur le `main` du moteur
après #1207 :

- **`xp_reward` est déjà servi.** `getExercise` (`quest.server.ts`) lit l'exercice en
  `select("*, subjects(…), chapters(…)")` et renvoie `exercise: ex.data` : la ligne `exercises`
  entière, colonne `xp_reward` comprise (types générés), aux DEUX registres. R-8 ne demande donc
  aucune retouche serveur : `exercise-player.tsx`, qui lit déjà `data.exercise`, passe `xpReward`
  au contexte de `renderResultFooter` ; la route anonyme en fait sa phrase.
- **Le parcours du chapitre n'est PAS servi** par `getExercise` : l'embed `subjects` ne porte pas
  `theme_id`. `getSubject` le dérive déjà — RPC existante `resolve_subject_parcours(theme, grade)`,
  puis lecture de la ligne `parcours`. Le lot 2 extrait cette dérivation en un helper partagé (une
  seule définition) et ajoute `getExerciseParcours({ exerciseId })` — `requireSupabaseAuth`, zod
  `.validator`, rend `{ id, name_fr, name_en, name_ar } | null` —, que la route `quest` n'appelle
  **que** si l'élève n'a pas de parcours (R-5) : aucun surcoût pour les autres chargements. La
  fonction vit dans un module `quest.*.server.ts`, au choix de l'exécuteur.
- **`checkAnswersPublic` / `scoreQuizPublic`** vivent désormais dans `quest.practice.server.ts`
  (déplacées à l'identique par #1207) : le refus du limiteur (`isRateLimited` /
  `isRateLimitedLocal`) lève un **code stable** `RATE_LIMITED` via `failWithClientError` à la place
  de `new Error("Trop de requêtes. Réessaie dans un instant.")` ; le client traduit (R-15). Le
  limiteur anonyme lui-même (mémoire par IP) ne change pas — c'est la ligne 9 du relevé, hors
  périmètre.

### 3.3 Client

```
src/shared/lib/return-to.ts              isSafeReturnPath · rememberReturnTo · consumeReturnTo
                                         · resolvePostAuthDestination — purs, testés (R-1 à R-3)
src/shared/lib/anon-continuity.ts        rememberLastChapter · readLastChapter · forget (lot 5) ;
                                         anon-quiz-gate.ts y déplace son stockage (R-13)
src/hooks/use-online-status.ts           useOnlineStatus() ← onlineManager (famille use-mobile)
src/components/ui/network-banner.tsx     NetworkBanner — les deux coquilles ; lit pendingCount()
src/components/ui/query-wait-state.tsx   WaitingForNetwork + isWaitingForNetwork(query) (R-9)
src/components/game/parcours-quick-pick.tsx  la carte de classe (R-5) — présentation pure
src/components/public/public-header.tsx  neutre pendant loading (R-6) ; déconnexion (R-11) ;
                                         Suivi parent masqué pour un élève (R-14)
src/components/public/public-landing.tsx R-6 ; returnTo sur gameCta ; carte Reprendre (lot 5)
src/components/public/resume-card.tsx    la carte « Reprendre » (lot 5)
src/routes/auth.tsx                      ?returnTo → mémoire ; reason=expired → hint ; R-3 ;
                                         emailRedirectTo → /auth ; signup/login → R-16
src/routes/_authenticated.tsx            garde : rememberReturnTo(pathname + search) ; bandeau
src/routes/_public.tsx                   bandeau
src/features/auth/onboarding-guard.ts    exclusion /quest/ (R-5)
src/features/auth/use-exit-on-refusal.ts rememberReturnTo(location, "expired") avant signOut
src/routes/_authenticated/quest.$exerciseId.tsx  compose la carte + setCurrentParcours
                                         + claimWelcomePack (@/features/auth) — la ROUTE compose
src/routes/_public/exercice.$exerciseId.tsx      public_practice_completed ; inviteValue ;
                                         erreurs R-15 ; returnTo sur l'invitation
src/features/quest/components/lesson-reader.tsx  returnTo ; account_invite_clicked
src/features/quest/components/subject-hub.tsx    returnTo sur la raison Rappel ; événement
src/routes/_public/{programme,extras,niveau,matiere,chapitre}.tsx
src/routes/_authenticated/{dashboard,parcours}.tsx   WaitingForNetwork quand paused (R-9)
src/features/quest/quest.server.ts       helper partagé de dérivation du parcours (lot 2)
src/features/quest/quest.*.server.ts     getExerciseParcours, lecture seule (lot 2)
src/features/quest/quest.practice.server.ts  RATE_LIMITED à la place du français en dur (lot 4)
src/features/quest/components/exercise-player.tsx  renderResultFooter reçoit xpReward (lot 1)
src/shared/lib/product-events.ts         3 événements + catalogue (R-16)
public/offline.html · public/sw.js       trilingue, prefers-color-scheme, VERSION v2 (R-10)
```

Frontières (AGENTS.md) : une feature n'importe jamais une autre. La carte `ParcoursQuickPick` est
donc une **primitive de présentation** (`src/components/game/`, à côté de `seal-mark` et
`gold-progress`) qui reçoit le nom du parcours et deux callbacks ; c'est la **route** `quest` qui
la monte et lui passe `setCurrentParcours` et `claimWelcomePack` de `@/features/auth` — comme elle
compose déjà `TutorPanel` et `ReportErrorButton`. `NetworkBanner` et `WaitingForNetwork` sont des
primitives (`src/components/ui`) qui n'importent que `@/shared` et `@/lib`. Les routes restent
minces : elles composent.

États TanStack Query : aucune option nouvelle sur le `QueryClient` ; `isWaitingForNetwork(q)` =
`q.fetchStatus === "paused" && q.data === undefined`. Le `retry` des mutations (`shouldReplaySessionRefusal`)
ne bouge pas.

### 3.4 Sécurité & anti-triche

- **Pas d'open redirect** : R-1, fonction pure, testée sur les formes connues (`//`, schéma,
  `\`, `javascript:`, boucle `/auth`). La destination finale passe par `navigate({ to })` du
  routeur, jamais par `window.location = …`.
- **Aucun jeton dans un `returnTo`** : les URL `/auth*` sont refusées, et le fragment — où Supabase
  dépose ses jetons sur le callback — est retiré avant mémorisation.
- **La porte quiz connectée reste serveur** : D-2 refuse toute migration de la porte anonyme
  (client-trust) vers `attempts` ; un élève rejoue le quiz, cette fois scoré.
- **La carte `ParcoursQuickPick` n'ouvre rien** : `start_exercise_session` ne gate pas sur le
  parcours (relevé §1.2) ; choisir une classe est un réglage de profil, par la server fn
  authentifiée existante (`requireSupabaseAuth`, zod).
- **Rien de nouveau n'atteint le serveur hors-ligne** (R-11). Le bandeau et la page de repli ne
  lisent aucune donnée de compte.
- **Vie privée** : les deux clés locales ne portent ni nom, ni e-mail, ni identifiant Supabase ;
  rien n'en part. L'inventaire INPDP n'a pas à bouger (une mémoire locale non transmise n'est pas
  un traitement du responsable) — l'exécuteur du lot 5 **le relit** et ajoute une ligne « mémoire
  locale de navigation » si l'inventaire décrit déjà `localStorage` ailleurs, pour rester vrai.

### 3.5 Intégrations & env

Aucune variable d'environnement, aucun secret, aucun service nouveau. Supabase Auth : les URL de
redirection déjà autorisées (`/auth`, `/auth/reset`, `/dashboard`) suffisent — `emailRedirectTo`
passe de `/dashboard` à `/auth`, qui est déjà la cible de Google. Rien à cliquer dans une console
(zero-intervention).

### 3.6 Observabilité

- Logger partagé : `auth.return-to.remembered{reason}`, `auth.return-to.consumed{kept}`,
  `auth.exit.expired` (déjà couvert par `client_errors` stage `token-attach` quand c'est un refus) ;
  `network.offline`/`network.online` en `debug` seulement (pas de bruit en prod).
- `client_errors` : aucun stage nouveau ; `public-submit` cesse de compter les simples absences de
  réseau (R-9 les reconnaît avant l'appel : pas d'appel, pas de ligne).
- Produit : R-16, catalogue affiché par `/admin/engagement` (`live: true` dès le lot 0).

### 3.7 Décisions d'architecture (ADR)

- **D-1 — Le retour vit dans l'URL ET dans une mémoire locale à TTL, décidé depuis la mémoire.**
  L'URL seule meurt sur la confirmation d'e-mail et l'aller-retour Google (qui reviennent sur
  `/auth` nu) ; la mémoire seule rendrait impartageable un lien d'invitation. Rejeté : un
  `redirectTo` Supabase paramétré (`/auth?returnTo=…`) — dépend de l'allowlist des URL de
  redirection dans la console Supabase, un mur zero-intervention pour zéro gain par rapport à la
  mémoire locale.
- **D-2 — La porte quiz anonyme n'est pas migrée vers le compte ; le quiz se rejoue, scoré.**
  La porte anonyme est client-trust (`sessionStorage`, rythme mesuré côté client) ; la porte
  connectée est serveur (`attempts`, « porte du quiz définie une fois », #1005). Y verser la
  première revient à laisser un `sessionStorage` forgé ouvrir des missions. Rejoué connecté, le
  quiz de cinq questions devient la **première quête**, rapporte les premiers XP (é31 R-19/R-20 :
  l'arrivée est une victoire) et réarme la porte honnêtement ; le hub le dit déjà (« quiz à
  passer »). Rejeté : un jeton HMAC signé par `scoreQuizPublic` et réclamé à l'inscription — juste,
  mais une table insert-only, une RPC, une extension de `chapter_quiz_cleared`, pgTAP, et une clé
  dérivée d'un secret serveur, pour épargner cinq questions qui rapportent des XP. Réversible si
  le relevé montre un jour que le replay fait fuir (KPI-1 lu par `is_quiz`).
- **D-3 — L'assistant d'accueil reste pour le hall et s'écarte de la quête.** Rejeté : le
  supprimer (il porte l'intention, la section lycée et le pack de bienvenue — é22, é16, é31) ; le
  rendre « plus tard » partout (le hall sans parcours est un hall vide, la redirection y est le bon
  écran). La seule chose qui change : il ne s'interpose plus entre un élève et la quête qu'il a
  demandée, et le choix de classe existe là, en un geste, avec le même pack.
- **D-4 — Le réseau se lit dans `onlineManager`, et nulle part ailleurs.** TanStack Query met
  déjà les requêtes en pause sur sa propre lecture de l'état réseau ; un second écouteur
  (`navigator.onLine` dans un hook maison) produirait deux vérités qui diffèrent sur un portail
  captif. Le bandeau et les états « en attente » suivent **la même** source que la pause. Rejeté :
  `useOnlineStatus` autonome (c'était la proposition de é06 lot 2, écrite avant que la pause
  TanStack soit comprise comme la cause du squelette).
- **D-5 — La page de repli reste statique et sans script.** Elle est servie depuis le cache du
  service worker sous la CSP par nonce de l'application : tout `<script>` inline y est mort-né, et
  lire le cookie de langue demanderait du script. Trois langues empilées coûtent trois lignes et
  marchent partout. Rejeté : une page de repli React (`/offline` route — é06 US-5) : hors
  périmètre, et une navigation SSR qui échoue ne rend aucune route.
- **D-6 — L'invitation chiffre le gain, jamais la perte.** « Jusqu'à {xp} XP » est un fait du
  barème (`xp_reward`), pas une promesse de score ; la formulation en gain respecte é31 R-20, qui
  interdit « tu viens de tout perdre », pas le chiffre. Rejeté : « tu aurais gagné +X XP »
  (reproche) et un compte à rebours (pression — public d'enfants).
- **D-7 — Six lots, zéro SQL, la mesure en premier.** Le lot 0 pose les trois événements avant
  tout changement de tunnel : sans lui, KPI-1/2/3 n'auraient pas de « avant ». Rejeté : fusionner 0
  et 1 (on perdrait la ligne de base) ; mettre le réseau en premier (il ne dépend de rien, mais le
  passage est la rupture que l'audit nomme depuis juin).

## 4. Plan d'exécution en lots

| lot | contenu (résumé)                                                                                      | fichiers/objets créés ou touchés                                                                                                                                                                                                                             | tests exigés                                                                                                                                                                                                                                                                                 | dépend de |
| --- | ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| 0   | La mesure d'abord : 3 événements + propriétés, catalogue, émetteurs                                   | `product-events.ts`, `exercice.$exerciseId.tsx`, `lesson-reader.tsx`, `subject-hub.tsx`, `public-landing.tsx`, `public-header.tsx`, `auth.tsx`, `onboarding.tsx`                                                                                             | Vitest : catalogue complet et typé, chaque émetteur (mock `captureProductEvent`), zéro PII (test de propriétés)                                                                                                                                                                              | —         |
| 1   | Le retour au point de départ + header neutre + déconnexion depuis le contenu + valeur de l'invitation | `return-to.ts` (+ tests), `auth.tsx`, `login.tsx`/`signup.tsx` (passent `returnTo`), `_authenticated.tsx` (garde), `public-header.tsx`, `settings-menu.tsx`, `public-landing.tsx`, invitations, `exercise-player.tsx` (`xpReward` au pied de résultat), i18n | Vitest : R-1 (formes hostiles), TTL, `resolvePostAuthDestination`, header neutre pendant `loading` ; e2e `public` : header neutre sans CTA avant hydratation ; e2e `authed/signup` étendu : invitation depuis `/chapitre/x` → inscription → `/chapitre/x` (skip hérité si pas d'autoconfirm) | 0         |
| 2   | L'accueil n'est plus un péage : garde épargne `/quest/`, carte `ParcoursQuickPick`                    | `onboarding-guard.ts` (+ tests), `src/components/game/parcours-quick-pick.tsx`, `quest.$exerciseId.tsx`, `getExerciseParcours` + helper partagé avec `getSubject`, i18n                                                                                      | Vitest : garde (pathname `/quest/…` ⇒ false ; `/dashboard` ⇒ true), carte (adopter / plus tard / sans parcours seulement) ; e2e `authed` : compte neuf sans parcours ouvre `/quest/<id>` et joue sans assistant                                                                              | 1         |
| 3   | La session qui meurt revient au même endroit                                                          | `use-exit-on-refusal.ts`, `auth.tsx` (hint), i18n                                                                                                                                                                                                            | Vitest : mémoire écrite avant `signOut` ; e2e `authed/session-invalidation` **étendu** : après reconnexion, l'URL quittée                                                                                                                                                                    | 1         |
| 4   | Le réseau se voit : bandeau, états « en attente », page de repli trilingue, SW v2                     | `use-online-status.ts`, `network-banner.tsx`, `query-wait-state.tsx`, 7 routes, `_public.tsx`, `_authenticated.tsx`, `offline.html`, `sw.js`, i18n `offline.*`, erreurs R-15                                                                                 | Vitest : hook (onlineManager), bandeau (pending count), `isWaitingForNetwork` ; e2e `public` : `context.setOffline(true)` ⇒ bandeau + état d'attente, `setOffline(false)` ⇒ reprise sans reload ; **`build:check` + `smoke:shell`** ; `check-rtl-classes` sur le bandeau                     | 0         |
| 5   | La continuité du visiteur (Q-1 : 30 jours) : portes quiz en `localStorage` + TTL, carte « Reprendre » | `anon-continuity.ts` (+ tests), `anon-quiz-gate.ts`, `resume-card.tsx`, `index.tsx`, `programme.tsx`, `chapitre.$chapterId.tsx`, `subject-hub.tsx` (`resumeHere` anonyme), i18n `public.resume.*`                                                            | Vitest : TTL, oubli, `localStorage` absent ⇒ sens sûr ; e2e `public-anon` : lire un chapitre, revenir sur `/` ⇒ carte, « oublier » ⇒ plus de carte ; quiz réussi, nouvel onglet ⇒ porte ouverte                                                                                              | 1         |

**Ordre arbitré (Q-3, 2026-10-30).** Chantier 1, ouvert dès la validation : lots **0 → 1 → 3** (la
mesure, le retour au point de départ, la session expirée). En file, au rythme des places de code
libres : lots **2**, puis **4**, puis **5** — l'ordre du tableau. Chaque lot = une PR sur `main`,
gate verte (`npm run verify` ; `ci:verify` pour le lot 4, qui touche le bundle prod et le service
worker).

- [ ] **Lot 0 — La mesure d'abord.** Périmètre : R-16 intégralement, `live: true` au catalogue,
      propriétés `return_to_kept: false` / `from_content` déduits de la route courante,
      `source: "wizard"` sur l'assistant. Critères : US-9 ; `/admin/engagement` affiche les
      trois lignes.
      **Stop-point** : aucun changement d'écran, aucun `returnTo`.
- [ ] **Lot 1 — Le retour au point de départ.** Périmètre : R-1 à R-4, R-6, R-8, R-11 (coquille
      publique), US-1, US-4, US-7 ; `signup`/`login` renseignent `return_to_kept`. Critères :
      depuis `/chapitre/x`, inscription par mot de passe ⇒ retour sur `/chapitre/x` avec HUD ;
      depuis `/exercice/y`, résultat ⇒ invitation avec `{xp}` ⇒ Google ⇒ retour ; `/quest/z` sans
      session ⇒ `/auth?mode=login&returnTo=/quest/z` ⇒ connexion ⇒ `/quest/z` ; `//evil` ⇒ hall ;
      header public sans CTA pendant `loading` ; déconnexion depuis `/chapitre/x` ⇒ même page,
      HUD disparu, mémoire locale intacte. **Stop-point** : pas de carte de classe, rien sur le
      réseau.
- [ ] **Lot 2 — L'accueil n'est plus un péage.** Périmètre : R-5, US-2, D-3. Critères : élève
      `student` sans parcours sur `/quest/<id>` joue ; carte présente ; « Choisir » ⇒
      `setCurrentParcours` + `claimWelcomePack` + `onboarding_completed{source:"quest_card"}` ;
      « Plus tard » ⇒ carte fermée pour la session ; `/dashboard` sans parcours ⇒ assistant,
      inchangé ; parent/admin jamais la carte. **Stop-point** : l'assistant n'est pas modifié.
- [ ] **Lot 3 — La session qui meurt revient au même endroit.** Périmètre : R-7, US-3. Critères :
      `session-invalidation.spec` étendu — après corruption du jeton et reconnexion, l'URL quittée
      est de nouveau à l'écran et `login{reason:"expired", return_to_kept:true}` part ; le hint
      est visible sur `/auth`. **Stop-point** : aucune modification de `auth-attacher`,
      `session-freshness`, `auth-refusals`.
- [ ] **Lot 4 — Le réseau se voit.** Périmètre : R-9, R-10, R-11, R-12, R-15, US-5, US-8, D-4,
      D-5. Critères : hors-ligne, bandeau dans les deux coquilles ; `/matiere/x` neuf ⇒ « En
      attente du réseau » et jamais le squelette ; retour en ligne ⇒ contenu sans reload ; une
      mission en file ⇒ « 1 mission en attente d'envoi » ; `/offline.html` trilingue, lisible dans
      les deux schémas de couleur, zéro script ; `sw.js` `VERSION = "v2"` ; `smoke:shell` vert,
      budget `index-` tenu (RISK-6). **Stop-point** : aucun cache, aucune persistance, pas de
      `vite-plugin-pwa`, pas de route `/offline`.
- [ ] **Lot 5 — La continuité du visiteur** (Q-1 tranchée : 30 jours, portes quiz + dernier chapitre ; en file, après les lots 2 et 4). Périmètre : R-13, US-6 ;
      carte « Reprendre » sur `/` et `/programme` ; `resumeHere` anonyme sur le hub. Critères :
      lecture d'un chapitre ⇒ carte au prochain `/` ; TTL échu ⇒ rien ; « oublier » ⇒ rien ;
      porte quiz réussie ⇒ ouverte dans un nouvel onglet ; `localStorage` jeté ⇒ comportement
      d'aujourd'hui. **Stop-point** : rien n'atteint le serveur ; aucun score mémorisé.

## 5. Stratégie de test

- **Vitest co-localisés** (`__tests__/`) : `return-to.ts` (R-1 sur toutes les formes hostiles ;
  TTL ; consommation unique ; `resolvePostAuthDestination` par rôle), `onboarding-guard.ts`
  (exclusion `/quest/`, parent/admin), `use-exit-on-refusal.ts` (mémoire **avant** `signOut`),
  `product-events.ts` (liste fermée, catalogue complet, aucune propriété PII — test qui échoue si
  une clé contient `email`, `name`, `user_id`), `anon-continuity.ts` (TTL, oubli, stockage
  absent), `network-banner` et `use-online-status` (sur `onlineManager.setOnline(false)`),
  `public-header` (neutre pendant `loading`, CTA ensuite, HUD pour un connecté, lien Suivi masqué
  pour un élève), `parcours-quick-pick` (rendu seulement pour un `student` sans parcours).
- **pgTAP** : sans objet — aucune ligne de SQL.
- **Playwright, tier `public`** (sans backend) : header neutre avant hydratation (assertion sur
  `data-testid`, jamais sur une langue) ; `auth-redirects.spec` **inchangé** (l'invariant « les
  routes contenu ne redirigent jamais vers `/auth` » reste la clé de voûte du pivot) ; hors-ligne
  via `context.setOffline(true)` sur `/programme` ⇒ bandeau + état d'attente, puis
  `setOffline(false)` ⇒ reprise.
- **Playwright, tier `public-anon`** (backend TEST) : `content-journey` et `navigation` restent
  verts ; lot 5 ajoute la carte « Reprendre » et la porte quiz dans un nouvel onglet.
- **Playwright, tier `authed`** : `signup.spec` étendu (retour au chapitre — garde son `skip` si
  le projet TEST exige la confirmation sans autoconfirm) ; `session-invalidation.spec` étendu
  (retour à l'URL quittée) ; nouveau scénario « compte neuf sans parcours joue une quête sans
  assistant » ; `logout.spec` gagne « se déconnecter depuis un cours reste sur le cours ».
- **`smoke:shell`** (lot 4, obligatoire) : le seul tier qui exécute le bundle prod et le service
  worker ; `build:check` tient le budget du chunk d'entrée (RISK-6).
- **Non-régression** : aucune server fn ne change de contrat ; aucune migration ; les suites
  existantes (`quest-anon`, `dashboard-anon`, `optional-auth-middleware`, `outbox`) restent telles
  quelles. La règle `local/require-server-fn-auth` et `check-rtl-classes` courent dans `lint`.

## 6. Risques & mitigations

- **RISK-1 — Open redirect par `returnTo`.** _Prob. faible, impact haut._ R-1 pure et testée sur
  les formes connues ; navigation par le routeur ; refus de `/auth*` ; fragment retiré. Revue
  `code-review` axe sécurité obligatoire sur le lot 1.
- **RISK-2 — Le lien de confirmation d'e-mail s'ouvre ailleurs** (autre appareil, app mail qui
  ouvre un autre navigateur) : pas de mémoire ⇒ hall. _Prob. moyenne, impact faible._ Fallback
  propre (R-3), mesuré par KPI-2 ; l'interstitiel dit d'ouvrir le lien « sur cet appareil ».
- **RISK-3 — Un élève sans parcours sur une quête fausse des écrans qui supposent un parcours**
  (objectif « 2 exercices de ton parcours », donjon scopé, « Ma classe »). _Prob. moyenne, impact
  moyen._ D-3 : seul `/quest/` est épargné ; `getDashboard` traite déjà `parcoursId = null`
  (parents, admins) ; la carte propose la classe dès la première quête ; l'exécuteur du lot 2
  relit `dashboard.server.ts` l. 316–430 et ajoute un test « élève sans parcours » sur le hall
  s'il manque.
- **RISK-4 — Le service worker sert l'ancienne page de repli.** _Prob. haute sans action, impact
  faible._ `VERSION = "v2"` purge `xp-offline-v1` à l'activation (code existant) ; `smoke:shell`
  vérifie l'enregistrement ; aucune autre stratégie de cache ne change.
- **RISK-5 — Faux « hors connexion »** (portail captif, `navigator.onLine` menteur). _Prob.
  moyenne, impact faible._ D-4 : une seule source, celle qui met les requêtes en pause — le
  bandeau ne peut pas dire autre chose que ce que l'écran fait ; libellé sans accusation
  (« en attente du réseau ») ; « Réessayer » toujours présent.
- **RISK-6 — Le chunk d'entrée déborde** (`index-` à 456 Ko, ~6 Ko de marge mesurés le
  2026-09-09). _Prob. haute, impact haut (PR rouge)._ `return-to.ts` et `use-online-status.ts`
  sont minuscules ; le **corps** du bandeau et la carte « Reprendre » sont `lazy()` ; les clés
  `offline.*` vont au catalogue déjà découpé ; `build:check` à chaque lot touchant l'index.
- **RISK-7 — Une mémoire locale sur un appareil partagé** (salle informatique) montre à un élève le
  chapitre d'un autre. _Prob. moyenne, impact faible._ Rien d'identifiant (un titre de chapitre),
  bouton « oublier » visible, TTL de 30 jours (Q-1).
- **RISK-8 — Le lot 2 contredit la règle « cours → quiz → missions » du guide intégré** (#1179).
  _Prob. faible._ Non : la porte quiz reste serveur et le hub la dit ; seul l'assistant de
  **classe** s'écarte, pas la porte de **chapitre**. Le `GuideIntroCard` de la quête ne change pas.

## 7. Questions ouvertes (pour l'humain) — arbitrées le 2026-10-30

Les trois questions ont été posées une par une au propriétaire et tranchées **sur les
recommandations**. Plus rien n'est ouvert : l'étude est `validée`.

- **Q-1 — Continuité du visiteur sur l'appareil** (lot 5) : **arbitrée** — portes quiz réussies +
  dernier chapitre lu, **30 jours**, mémoire locale à l'appareil, jamais de score ni de réponse,
  bouton « oublier » (R-13). Écartées : « quiz seulement » (moins de raisons de revenir) et « statu
  quo » (tout meurt avec l'onglet).
- **Q-2 — `/` pour un élève connecté** : **arbitrée** — on **garde la landing** (référencement,
  parents, enseignants, lien partagé devant un parent). Précision de rédaction : la recommandation
  évoquait une carte qui, pour un connecté, pointerait sa prochaine action du hall ; elle n'est
  **pas** retenue en v1 — elle demanderait une requête connectée depuis une page publique, et
  « Continuer à jouer » (`gameCtaAuthed`) mène déjà au hall. La carte « Reprendre » du lot 5 ne
  s'adresse qu'au visiteur sans session ; la landing d'un connecté reste telle quelle (R-13).
- **Q-3 — La place dans la file** : **arbitrée** — un **chantier court** ouvert dès la validation :
  lots **0, 1 et 3** (zéro SQL, trois PR). Les lots **2, 4 et 5** prennent la file ensuite, un par
  un, dès qu'une place de code se libère (§4). Rien ici ne précède la campagne 1 de §6.1 ni ne
  touche au contenu.

## 8. Journal d'exécution

- **2026-10-30 — validation.** Q-1 à Q-3 arbitrées par le propriétaire (§7), toutes sur les
  recommandations. Aucun lot démarré. Correction de l'étude avant validation, relevée en relisant le
  `main` du moteur (#1207) : `exercises.xp_reward` est **déjà servi** (`getExercise` renvoie la
  ligne entière — l'étude affirmait le contraire à partir d'un `grep` qui ne voit pas un
  `select("*")`) ; la correction publique vit désormais dans `quest.practice.server.ts` ; le
  parcours du chapitre, lui, n'est pas servi (§3.2).

_(la suite est remplie au fil des lots par l'exécuteur : date, lot, PR, écarts acceptés, dettes
notées)_
