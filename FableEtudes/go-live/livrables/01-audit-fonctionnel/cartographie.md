# C1 — Cartographie fonctionnelle (S1, 2026-06-10)

> Livrable du chantier [01-audit-fonctionnel](../../01-audit-fonctionnel.md), produit en S1 par
> analyse statique du code (2 passes parallèles : écrans/features, processus/règles SQL).
> Les « constats candidats » (A-* et B-*) seront vérifiés en conditions réelles (S2) puis triés
> en findings définitifs → GAP au backlog (S3). **Ne pas traiter ces candidats comme confirmés.**

---

## A. Cartographie des écrans (routes)

| Route | Accès | Rôle fonctionnel | Features utilisées | Points UX notables (guards, redirections, états) |
|---|---|---|---|---|
| `__root.tsx` (shell) | public | Document HTML SSR (locale/dir/thème depuis cookies), providers (Query, i18n, thème), Toaster, enregistrement du service worker PWA, écrans 404 et erreur globaux | — | `notFoundComponent` + `errorComponent` avec retry (`__root.tsx:22-71`) ; lang/dir RTL corrects au premier paint |
| `/` (`index.tsx`) | public | Landing marketing (hero 3D, features, matières, rangs, CTA signup/login) | — (composants `landing/`) | Toggle "réduire les animations" ; 3D désactivée mobile/reduced-motion ; contenu matières figé à 5 matières type 9ème (`index.tsx:101-132`) |
| `/login` | public | Alias → redirection | — | `beforeLoad` → `redirect /auth?mode=login` (`login.tsx:4-6`) |
| `/signup` | public | Alias → redirection | — | `beforeLoad` → `redirect /auth?mode=signup` (`signup.tsx:4-6`) |
| `/auth` | public | Connexion / inscription email+mdp et Google OAuth, choix de rôle (élève/parent), liaison Alliance Code parent au signup, écran "confirme ton email" | auth (`bootstrapProfile`), parent-report (`linkStudentByCode`) | Redirige vers `/dashboard` si déjà connecté (`auth.tsx:70-75`) ; gestion erreurs OAuth dans l'URL (`auth.tsx:46-91`) ; **logique métier dans la route** : signUp/signIn/OAuth Supabase + bootstrap profil + liaison parent (`auth.tsx:112-210`) ; textes EN/FR mélangés, TODO i18n (`auth.tsx:120`) |
| `_authenticated.tsx` (layout) | connecté | Shell de navigation (header, liens conditionnels par rôle, badges compteurs admin, sign-out, switchers langue/thème) | auth (`useAuth`), subscription (`getPendingBetaCount`), content-report (`getOpenReportsCount`) | **Guard auth en `useEffect`** → `/auth?mode=login` (`_authenticated.tsx:80-84`), rend `null` en attendant ; **guard onboarding** : profil sans `current_parcours_id` → `/onboarding` (`:89-94`) ; requête rôle directe au client Supabase (`:44-56`) ; liens parent (`/parent-report`) et admin (`/parent-report`, `/admin/*`) conditionnels (`:149-184`) |
| `/dashboard` | élève (parent/admin redirigés) | Heroes Hall : profil/XP/streak, objectifs quotidiens & quêtes hebdo, raccourcis (retry/continuer/donjon), grille matières du parcours actif + autres thèmes, radar, inventaire, badges, **boutique**, récupération de streak, Alliance Code copiable | dashboard, shop, progression, parent-report (`formatStudentAllianceCode`) | Redirection client parent/admin → `/parent-report` (`dashboard.tsx:191-195`) ; état erreur avec retry (`:255-271`) ; skeletons + sections secondaires différées (350 ms) ; **route très chargée** : 804 lignes, 4 mutations (achat/équip/activation/streak) + ciblage de quête `runQuestAction` (`dashboard.tsx:320-339`) ; `dailyGoal={100}` codé en dur (`:445`) |
| `/parcours` | élève | Carte d'aventure (journey map) des matières du parcours actif | dashboard (`getDashboard`), parcours (`JourneyMap`, `buildSubjectNodes`) | Pas de branche erreur : `isLoading \|\| !data` → loader infini en cas d'échec (`parcours.tsx:27-33`) |
| `/parcours/$subjectId` | élève | Chemin de chapitres (zigzag) d'une matière | quest (`getSubject`), dashboard (`getDashboard`), parcours (`SubjectPath`, `buildChapterNodes`) | Même absence de branche erreur (`parcours.$subjectId.tsx:28-34`) |
| `/themes` | élève | Explorer = hub des parcours (concours + libres) et **switcher de parcours actif** | dashboard (`getParcours`, `ParcoursHub`), auth (`setCurrentParcours`) | Route mince exemplaire ; invalidation + atterrissage `/dashboard` après switch (`themes.tsx:36-48`) |
| `/subject/$subjectId` | élève | Page matière : chapitres, quiz de compréhension (gate), missions avec étoiles, badges Boss/Élite, verrous premium | quest (`getSubject`) | État erreur avec retour hall (`subject.$subjectId.tsx:37-53`) ; mini-table i18n locale ad hoc `L` (`:70-83`) ; verrou premium calculé client (`:215-219`), le serveur restant autoritatif |
| `/lesson/$chapterId` | élève | Lecture du cours (markdown sanitisé), résumé togglable, TOC, navigation précédent/suivant + liste des chapitres | quest (`getChapterLesson`) | État "Lesson coming soon" si pas de contenu (`lesson.$chapterId.tsx:66-83`) ; pas de branche erreur (`:37`) ; chrome UI en arabe codé en dur quel que soit le contenu (`:129,139,247,272,284,300`) |
| `/quest/$exerciseId` | élève (gates serveur) | Moteur de quête QCM : session sécurisée, mode boss chronométré (HP/timer), indices consommables, écran résultat (XP/coins/badges/level-up/correction), signalement d'erreur | quest, subscription (`SubscriptionPaywall`), content-report (`ReportErrorButton`) | Écran paywall si le serveur rejette "Parcours premium" (`quest.$exerciseId.tsx:377-397`) ; écran quiz-lock si quiz non passé (`:399-411`) ; raccourcis clavier 1-4/A-D ; **route la plus lourde** : 819 lignes de logique de jeu (timer boss `:205-236`, anti-double-réponse, refs anti-stale) |
| `/dungeon` | élève avec entitlement concours + prérequis | Mode survie infini : lobby (règles, accès), jeu 1 vie, game-over avec stats et question fatale | dungeon, subscription (`SubscriptionPaywall`) | Paywall si `reason === "SUBSCRIPTION"` (`dungeon.tsx:294-295`) ; messages verrou (limite quotidienne / niveau / prérequis `:296-326`) en FR codé en dur ; pas de branche erreur sur la query d'accès (`:292`) ; 646 lignes, machine d'état lobby/playing/gameover dans la route |
| `/leaderboard` | élève | Classement global XP + onglets par matière, podium top 3, carte "mon rang" | dashboard (`getLeaderboard`, `getSubjects`, `getSubjectLeaderboard`) | Aucun `useT` — textes EN/FR codés en dur (`leaderboard.tsx:67-78,246-248`) ; pas de branche erreur ; anti-fuite UUID : lignes keyées par `rank`/`isMe` (`:18-28`) |
| `/onboarding` | connecté sans parcours | Wizard 2 étapes : intention (concours/explorer) puis choix du parcours → `set_current_parcours` → `/dashboard` | dashboard (`getParcours`), auth (`setCurrentParcours`) | États pending/error/vide gérés (`onboarding.tsx:223-240`) ; tout en FR codé en dur ; composants wizard inline dans la route (`:65-263`) ; accessible même avec parcours déjà choisi (pas de redirect inverse) |
| `/parent-report` | parent/admin (refus côté serveur) | Rapport de suivi : liaison Alliance Code, sélecteur d'élèves (pagination admin), verdict d'assiduité, métriques, activité 30 j, perfs par matière | parent-report | **Pas de guard rôle dans la route** : le refus élève vient de `getLinkedStudents` (`parent-report.server.ts:135-137`) → un élève voit le formulaire de liaison sans message d'erreur ; sert aussi de console admin "Suivi des élèves" ; UI (VerdictCard, MetricCard…) inline (`parent-report.tsx:374-497`) |
| `/admin/subscriptions` | admin | Gestion des **entitlements parcours** : liste des accès, octroi (source/durée), révocation, rappel téléphone contact | subscription, dashboard (`getParcours`), auth (`useAuth`) | Guard rôle client (`admin.subscriptions.tsx:84-96`, "accès refusé" si rôle chargé ≠ admin) + RPC admin-only serveur ; nom de route hérité ("subscriptions") |
| `/admin/beta-requests` | admin | File des demandes d'accès bêta (approuver/rejeter) | subscription (`BetaRequestsAdmin`), auth | Même guard rôle dupliqué (`admin.beta-requests.tsx:18-40`) |
| `/admin/content-reports` | admin | Triage des signalements d'erreurs de contenu | content-report (`ContentReportsAdmin`), auth | Même guard rôle dupliqué (`admin.content-reports.tsx:18-40`) |

## B. Cartographie des features (capacités)

### features/auth
- **Rôle** : session côté client (`useAuth`) + finalisation du compte : bootstrap du profil au signup et persistance du parcours actif.
- **Server functions** :

| Fonction | Méthode | Entrée (zod) | Ce qu'elle fait (tables/RPCs) |
|---|---|---|---|
| `bootstrapProfile` | POST | `displayName` (1-80), `role` enum `student\|parent` | Upsert `profiles.display_name` + RPC `set_profile_role` (le rôle n'est plus écrivable directement) |
| `setCurrentParcours` | POST | `parcoursId` (min 1) | RPC `set_current_parcours` (self-scoped, synchronise `current_grade_id` pour les concours) ; retourne le profil |
- **Composants** : aucun (pas de `components/`) ; hook `use-auth.ts` (session/user/loading via `onAuthStateChange`).
- **Observations audit** : la quasi-totalité de la logique d'authentification (signUp/signIn/OAuth, messages d'erreur `friendlyAuthError`) vit dans la route `auth.tsx:99-210`, pas dans la feature.

### features/dashboard
- **Rôle** : agrégats du hall (profil, stats par matière, objectifs/quêtes), catalogue des parcours et classements. Fait office de feature "lecture transverse".
- **Server functions** :

| Fonction | Méthode | Entrée (zod) | Ce qu'elle fait (tables/RPCs) |
|---|---|---|---|
| `getDashboard` | GET | — | `profiles` (auto-création si absent), `subjects`, `attempts` (récents + totalité), `parcours` du profil ; RPC `has_parcours_entitlement` → `premiumLockedSubjectIds` ; calcule stats/`nextExerciseId`, scope les matières au parcours actif |
| `getDashboardSecondary` | GET | — | `student_badges` (+`badges`), `inventory_items` (+`shop_items`), `shop_items` actifs ; calcule slots d'armement (next-quest/passive) et consommables d'indice |
| `getLeaderboard` | GET | — | `profiles` top XP (rôle student) + rang du caller (count `xp >`) ; aucune fuite d'UUID |
| `getParcours` | GET | — | `parcours` ordonnés + RPC `has_parcours_entitlement` **par parcours premium** (boucle) |
| `getSubjects` | GET | `themeId?`, `gradeId?` (uuid) | `subjects` filtrables thème/grade |
| `getSubjectLeaderboard` | GET | `subjectId` | RPC `get_subject_leaderboard` (rank/is_me, sans UUID) |
| `getSprint2Dashboard` | GET | — | RPC `ensure_daily_weekly_goals` puis `daily_objectives` (jour UTC), `weekly_quests` (semaine), `spaced_repetition_schedule` pending |
- **Composants** : `dashboard-badges-shop` (badges + boutique), `dashboard-radar-inventory` (radar de maîtrise + inventaire/armement), `hero-avatar` (skin équipé), `hero-stat-chips` (chips niveau/streak/XP/coins avec ExplainHint), `parcours-hub` (hub Explorer présentational), `subject-path-card` (carte matière avec verrou premium).
- **Observations audit** : fourre-tout assumé — leaderboard et catalogue parcours y vivent faute de feature dédiée (documenté CLAUDE.md) ; `pendingSpacedReps` retourné mais jamais affiché par la route (`dashboard.server.ts:492`) ; nom `getSprint2Dashboard` = vocabulaire de sprint historique ; `getParcours` fait un RPC par parcours premium (N+1) (`dashboard.server.ts:367-376`) ; `ParcoursHub` est rangé sous dashboard alors qu'il sert la route `/themes` (sémantique parcours).

### features/quest
- **Rôle** : cœur pédagogique — matière/chapitres/leçons, session d'exercice sécurisée, gates (quiz de compréhension, premium), soumission atomique et indices.
- **Server functions** :

| Fonction | Méthode | Entrée (zod) | Ce qu'elle fait (tables/RPCs) |
|---|---|---|---|
| `getSubject` | GET | `subjectId` | `subjects`/`chapters`/`exercises` ; RPC `get_best_scores_by_exercise` (fallback gracieux loggué) ; `attempts` pour l'état quiz (gate école uniquement, anti-rush ≥4 s/question) ; RPC `resolve_subject_parcours` + `parcours` + `has_parcours_entitlement` → contexte `viewer` (fallback "locked" sûr) |
| `getChapterLesson` | GET | `chapterId` uuid | `chapters` (+`subjects`) + chapitres frères pour la navigation |
| `getExercise` | GET | `exerciseId` uuid | `exercises` (+subjects/chapters), `questions` (sans `correct_option`), `inventory_items` → `hintCharges` |
| `startExerciseSession` | POST | `exerciseId` uuid | `exercises` ; RPC `resolve_exercise_access` (**fail-closed**, messages "Parcours premium…" matchés par l'UI) ; gate quiz école via `attempts` ; insert `exercise_sessions` |
| `revealHint` | POST | `questionId` uuid | Rate-limit (10/10 s) + RPC `consume_hint` (décrément atomique, gratuit si pas d'explication) |
| `submitAttempt` | POST | `sessionId` uuid, `exerciseId` uuid, `answers[]` (1-100) | Rate-limit (5/10 s) ; `questions` (corrigé construit serveur, masqué si quiz), `exercises.mode` ; RPC `ensure_daily_weekly_goals` + RPC atomique `submit_exercise_attempt` (score, XP/coins, potions, retry shield, badges) |
- **Composants** : `confetti` (victoire), `quest-hint-button` (bouton Indice consommable), `quest-result-actions` (rejouer/suivant/retour), `quest-reward-grid` (XP/coins/niveau/streak), `quiz-lock-screen` (chapitre verrouillé par le quiz). Helpers purs : `next-exercise`, `no-xp-reason`, `quest-labels`.
- **Observations audit** : `submitAttempt` retourne `reviewHidden` que l'UI ne lit jamais (la route reteste `mode === "quiz"`) — consommé uniquement par les tests (`quest.server.ts:581`).

### features/dungeon
- **Rôle** : mode survie (1 vie, étages infinis), entièrement piloté par des RPCs serveur-autoritatifs.
- **Server functions** :

| Fonction | Méthode | Entrée (zod) | Ce qu'elle fait (tables/RPCs) |
|---|---|---|---|
| `getDungeonAccess` | GET | — | RPC `get_dungeon_access` (niveau, prérequis matières/chapitres, runs/jour, raison du verrou) |
| `startDungeonRun` | POST | — | Rate-limit (5/30 s) + RPC `start_dungeon_run` (mappe l'erreur `DUNGEON_LOCKED`) |
| `getDungeonQuestions` | GET | `runId` uuid, `batchSize` 1-20 (déf. 5) | Rate-limit + RPC `get_dungeon_questions` (difficulté progressive) |
| `submitDungeonAnswer` | POST | `runId` uuid, `questionId` uuid, `choice` 1-32 | Rate-limit (40/60 s) + RPC `submit_dungeon_answer` |
| `submitDungeonRun` | POST | `runId` uuid, `durationSeconds` ≥0 | Rate-limit (3/30 s) + RPC `finalize_dungeon_run` (XP/coins) |
- **Composants** : aucun — toute l'UI (lobby/jeu/game-over) est dans la route `dungeon.tsx` (646 lignes).
- **Observations audit** : vocabulaire hérité de l'abonnement : `hasSubscription` et `reason: "SUBSCRIPTION"` (`dungeon.server.ts:174,187-189`) alors que le gate est désormais l'entitlement par parcours ; en l'absence de ligne RPC, le fallback retourne `reason "SUBSCRIPTION"` → l'utilisateur voit un paywall plutôt qu'une erreur (`dungeon.server.ts:161-175`) ; `DUNGEON_DIFFICULTY_STEP` exporté mais utilisé nulle part (`dungeon.server.ts:10`).

### features/shop
- **Rôle** : achats et gestion d'inventaire (skins, potions, boucliers) — validations atomiques en RPC SECURITY DEFINER.
- **Server functions** :

| Fonction | Méthode | Entrée (zod) | Ce qu'elle fait (tables/RPCs) |
|---|---|---|---|
| `purchaseShopItem` | POST | `itemCode` | Rate-limit (10/10 s) + RPC `purchase_shop_item` (coins + inventaire atomiques) |
| `equipInventorySkin` | POST | `itemCode` | RPC `equip_inventory_skin` (toggle + `avatar_slug`) |
| `activateInventoryItem` | POST | `itemCode` | RPC `activate_inventory_item` (armement slots next-quest/passive) |
- **Composants** : aucun — l'UI boutique/inventaire vit dans `dashboard/components`.
- **Observations audit** : capacité sans route ni composant propres ; exposée uniquement comme sections du dashboard (pas de page `/shop`).

### features/progression
- **Rôle** : récupération de streak payante en coins.
- **Server functions** :

| Fonction | Méthode | Entrée (zod) | Ce qu'elle fait (tables/RPCs) |
|---|---|---|---|
| `recoverStreak` | POST | — | Rate-limit (3/60 s) ; lit `profiles` (conditions : streak=0, ancien streak>0, coins suffisants) ; RPC `spend_coins` puis `update profiles` (streak=1) |
- **Composants** : aucun (bannière inline dans `dashboard.tsx:452-479`).
- **Observations audit** : feature mono-fonction ; contrairement aux autres écritures gameplay (RPC atomiques), la séquence `spend_coins` → `update profiles` se fait en deux écritures non atomiques (`progression.server.ts:42-58`).

### features/parent-report
- **Rôle** : lien famille (Alliance Code) et rapport d'activité de l'élève pour parents ; sert aussi de vue admin "tous les élèves".
- **Server functions** :

| Fonction | Méthode | Entrée (zod) | Ce qu'elle fait (tables/RPCs) |
|---|---|---|---|
| `getLinkedStudents` | GET | `page` ≥1 (déf. 1), `pageSize` 1-200 (déf. 100) | Lit `profiles.role` (refuse non parent/admin) ; admin → tous les `profiles` student paginés + count ; parent → `parent_student_links` actifs puis `profiles` liés |
| `getStudentReport` | GET | `studentId` uuid | RPC `get_student_report` + parsing zod ultra-défensif (verdict enum avec fallback `average`) |
| `linkStudentByCode` | POST | `studentCode` 8-64, `relationLabel` 2-40 regex | Rate-limit (20/60 s) + RPC `link_student_by_code` (décodage + validation + insert côté SQL) |
- **Composants** : aucun — l'UI rapport est inline dans la route. Helper `family-link.ts` (format/parse Alliance Code).
- **Observations audit** : `parseStudentAllianceCode` exporté du barrel mais utilisé uniquement par les tests (`family-link.ts:9`, `index.ts:5`) ; la pagination de `getLinkedStudents` n'est effective que pour l'admin.

### features/subscription
- **Rôle** : monétisation par **entitlements de parcours** (octroi/révocation admin, paywall hors-bande par téléphone) + programme bêta (demande/triage).
- **Server functions** :

| Fonction | Méthode | Entrée (zod) | Ce qu'elle fait (tables/RPCs) |
|---|---|---|---|
| `listParcoursEntitlements` | GET | — | RPC `admin_list_parcours_entitlements` (admin-only en SQL) |
| `grantParcoursEntitlement` | POST | `userId` uuid, `parcoursId`, `source` enum (déf. `purchase`), `expiresAt?` ISO/null, `months?` 1-120 | RPC `admin_grant_parcours` (expiry dérivée ou perpétuelle) |
| `revokeParcoursEntitlement` | POST | `userId` uuid, `parcoursId` | RPC `admin_revoke_parcours` (soft delete) |
| `getMyBetaRequest` | GET | — | `beta_access_requests` (dernière demande du caller) |
| `requestBetaAccess` | POST | `name` 1-120, `email`, `motivation?` ≤1000 | Vérifie absence de demande pending/approved puis insert `beta_access_requests` |
| `listBetaRequests` | GET | — | RPC `admin_list_beta_requests` |
| `getPendingBetaCount` | GET | — | RPC `admin_pending_beta_count` (0 gracieux pour non-admin) |
| `reviewBetaRequest` | POST | `requestId` uuid, `approve` bool | RPC `admin_review_beta_request` ; si approbation : RPC `admin_grant_parcours` (source `beta`, `BETA_ACCESS_MONTHS`, parcours courant premium sinon flagship) |
- **Composants** : `subscription-paywall` (modèle de vente + téléphone admin + demande bêta), `beta-access-request`, `beta-requests-admin`, `parcours-entitlements-admin`.
- **Observations audit** : nom de feature (et de route `/admin/subscriptions`, et clés i18n `t.subscription.*`) hérité de l'ancien modèle abonnement supprimé en migration `20260609000000`, alors que tout le code manipule des entitlements.

### features/content-report
- **Rôle** : signalement d'erreurs de contenu par les apprenants + triage admin.
- **Server functions** :

| Fonction | Méthode | Entrée (zod) | Ce qu'elle fait (tables/RPCs) |
|---|---|---|---|
| `reportContentError` | POST | `exerciseId?` uuid, `questionId?` uuid, `message` 5-1000 | Rate-limit (5/60 s) + insert `content_reports` (status `open`) |
| `listContentReports` | GET | — | RPC `admin_list_content_reports` |
| `getOpenReportsCount` | GET | — | RPC `admin_open_reports_count` (0 gracieux) |
| `resolveContentReport` | POST | `reportId` uuid, `status` enum `resolved\|dismissed` | RPC `admin_resolve_content_report` |
- **Composants** : `report-error-button` (expander sur l'écran résultat), `content-reports-admin` (file de triage).
- **Observations audit** : RAS.

### features/parcours
- **Rôle** : UI de carte d'aventure (journey map matières + chemin de chapitres) — purement présentationnelle, alimentée par les server fns de dashboard/quest.
- **Server functions** : aucune (helpers purs dans `journey.ts`).
- **Composants** : `journey-header`, `journey-map`, `journey-track`, `path-node` (done/current/open/locked/premium-locked), `subject-path`.
- **Observations audit** : homonymie trompeuse — la feature `parcours` ne gère **pas** l'entité métier "parcours" (catalogue → `dashboard.getParcours`, choix → `auth.setCurrentParcours`, accès → `subscription`) ; elle ne contient que la visualisation du chemin de progression.

### src/components/landing/
- `golden-hero-canvas.tsx` — scène 3D dorée three.js du hero (lazy, jamais chargée sur mobile/reduced-motion).
- `use-lenis.ts` — smooth-scroll Lenis pour la landing.

## C. Constats transverses candidats — écrans & structure (A-*)

- **A-1. Routes non minces malgré la convention "routes thin" (CLAUDE.md)** : `quest.$exerciseId.tsx` 819 lignes, `dashboard.tsx` 804, `dungeon.tsx` 646, `parent-report.tsx` 497 (UI inline `:374-497`), `onboarding.tsx` 348 (wizard inline `:65-263`), `auth.tsx` 450 (toute la logique signup/OAuth `:112-210`).
- **A-2. Requête de rôle dupliquée 4× en accès Supabase direct côté client** : `_authenticated.tsx:44-56`, `admin.beta-requests.tsx:18-26`, `admin.content-reports.tsx:18-26`, `admin.subscriptions.tsx:32-40` ; bloc "accès refusé" copié dans les 3 routes admin.
- **A-3. Écrans manquants évidents** : aucune page profil/paramètres (nom, email, mot de passe, suppression de compte) et **aucun flux "mot de passe oublié"** (`resetPasswordForEmail` absent de `src/`).
- **A-4. `/parent-report` sans guard de rôle côté route** : refus élève silencieux (`parent-report.server.ts:135-137`) → un élève voit le formulaire de liaison sans explication.
- **A-5. Gestion d'erreur absente sur plusieurs routes de lecture** : `lesson.$chapterId.tsx:37`, `parcours.tsx:27-33`, `parcours.$subjectId.tsx:28-34`, `dungeon.tsx:292` → loader infini en cas d'erreur, contrairement à `dashboard.tsx:255-271` et `subject.$subjectId.tsx:37-53` (retry).
- **A-6. Features sans route dédiée** : `shop` (pas de page boutique/inventaire — sections du dashboard), `progression` (bannière streak du dashboard uniquement).
- **A-7. Routes sans feature correspondante** : `/leaderboard` (server fns dans `dashboard.server.ts:286-438`), `/onboarding` (tout inline), `/themes` (`ParcoursHub` vit sous dashboard).
- **A-8. i18n incomplète et mélangée** : `leaderboard.tsx` sans `useT` (EN/FR en dur) ; `lesson.$chapterId.tsx` chrome en arabe codé en dur quel que soit le contenu (`:129,139,247,272,284,300`) ; `onboarding.tsx` FR-only ; toasts hors i18n tracés `TODO(review #32)` (`auth.tsx:120`, `dashboard.tsx:200-252,336-338`, `dungeon.tsx:98-211`) ; `subject.$subjectId.tsx:70-83` mini-table i18n ad hoc.
- **A-9. Vocabulaire "subscription" résiduel après le pivot entitlements** (migration `20260609000000`) : feature `subscription/`, route `/admin/subscriptions`, `hasSubscription`/`reason: "SUBSCRIPTION"` (`dungeon.server.ts:174,187-189` ; `dungeon.tsx:294`).
- **A-10. Code mort / non branché apparent** : `submitAttempt.reviewHidden` jamais lu par l'UI (`quest.server.ts:581`) ; `parseStudentAllianceCode` (tests only) ; invalidation queryKey `["me-parcours"]` sans query correspondante (`onboarding.tsx:297`) ; `pendingSpacedReps` jamais affiché (`dashboard.server.ts:492`) ; filtres de `getSubjects` jamais utilisés (`leaderboard.tsx:39`) ; `DUNGEON_DIFFICULTY_STEP` inutilisé (`dungeon.server.ts:10`).
- **A-11. Duplications UI parcours** : l'étape 2 de l'onboarding (`onboarding.tsx:133-263`) refait une liste de sélection distincte de `ParcoursHub` (`/themes`) ; helper `colorVar` implémenté 3× (`onboarding.tsx:60`, `parcours-hub.tsx:48-49`, `subject-path-card.tsx:28-44`).
- **A-12. Atterrissage parent/admin indirect** : parent/admin arrive sur `/dashboard` puis redirection client → `/parent-report` (`dashboard.tsx:191-195`) — flash possible du dashboard élève ; la nav admin réutilise `/parent-report` sous le libellé "Admin".
- **A-13. Guards en `useEffect` post-rendu (pas de `beforeLoad`/SSR)** : guard auth `_authenticated.tsx:80-84` (rend `null` pendant la redirection) et guard onboarding `:89-94`.
- **A-14. Objectif quotidien codé en dur dans la route** : `dailyGoal={100}` (`dashboard.tsx:445`) hors de `gamification.ts` ; le XP du jour n'additionne que les objectifs `completed` (`:442-444`).
- **A-15. Landing figée sur le périmètre 9ème** : 5 matières fixes type concours (`index.tsx:101-132`), stats "5 matières / 200+ quêtes" en dur (`:236-238`) — écart marketing / catalogue réel (académie multi-thèmes, 6ème + 9ème + thèmes libres).

---

## D. Règles de jeu chiffrées (constantes)

> Précédence : quand une fonction SQL est redéfinie dans plusieurs migrations, **la plus récente fait foi**. Versions faisant foi : `submit_exercise_attempt` et `award_xp` → `20260606130000_consumable_shields.sql` ; `get_dungeon_access` → `20260608123000_dungeon_parcours_gate.sql` ; `start_dungeon_run` → `20260603100000` ; `get_subject_leaderboard` → `20260606150000` ; `admin_review_beta_request` → `20260609000000`.

| Règle | Valeur | Source (fichier:ligne) |
|---|---|---|
| Seuil de réussite d'un exercice | **60 %** (en dessous : 0 XP/0 coins + planification révision) | `gamification.ts:4` ; `20260606130000:252,375` |
| Seuil du quiz de compréhension (gate chapitre, thème école) | **80 %** | `gamification.ts:11` ; `quest.server.ts:189,410` |
| Anti-rush (« tooFast ») | durée < **4 s × nb questions** ⇒ 0 XP/0 coins, et ne valide pas le quiz gate | `gamification.ts:19` ; `20260606130000:251` ; `quest.server.ts:193-198,411-416` |
| Anti-farm (« improved ») | récompense seulement si score **> meilleur score précédent** | `20260606130000:246-252` |
| Calcul XP d'une tentative éligible | `round(xp_reward × score%)` ; coins = `reward_coins` (non proratisés) | `20260606130000:255-256` |
| Barème de contenu (par difficulté) | d1 practice **50 XP/10 c** · d2 practice **75/15** · d3 boss **120/30** · d4 challenge **300/60** · quiz **20/5** | `.claude/skills/content-engine/references/rewards-and-modes.md:45-51` |
| Courbe de niveaux | **200 XP/niveau** ; `level = ⌊xp/200⌋ + 1` | `gamification.ts:41` ; `20260606130000:608` |
| Tiers de hero class | <6 Candidat Civil · ≥6 Aspirant Academicien · ≥11 Guerrier des Equations · ≥21 Maitre des Langues · ≥31 Elite du Concours · ≥50 S-Rank Legend | `20260606130000:611-618` |
| Tier d'avatar | `min(6, ⌊level/8⌋ + 1)` | `20260606130000:620` |
| FREE_PREVIEW_MAX_DIFFICULTY | **1** : parcours premium sans entitlement ⇒ quiz + missions difficulté ≤ 1 gratuits ; ≥ 2 verrouillé | `gamification.ts:117` ; `20260608121000:93-97` |
| Streak | +1 si actif la veille ; inchangé si déjà actif aujourd'hui ; **1 jour raté + bouclier de streak armé ⇒ +1 et conso du bouclier** ; sinon reset à **1** (jamais 0) | `20260606130000:568-605` |
| Coût récupération de streak | **15 coins** (exige `current_streak = 0`) | `gamification.ts:108` ; `progression.server.ts:29-45` |
| Badges attribués par le scoring | `first_quest` (1ʳᵉ tentative) · `perfect_score` (100 %) · `speed_demon` (< **60 s** et ≥ 60 %) · `streak_7` (streak ≥ **7**) | `20260606130000:347-373` |
| Répétition espacée (échec < 60 %) | 3 rappels à **J+1, J+3, J+7** (un seul lot `pending` par exercice) | `gamification.ts:44-48` ; `20260606130000:406-426` |
| Adaptation de difficulté | fenêtre **10** tentatives ; moy. > **75** ⇒ +1 (max **4**) ; < **40** ⇒ −1 (min **1**) | `gamification.ts:51-63` ; `20260606130000:453-474` |
| Objectif quotidien (SQL, faisant foi) | `3_exercises` : cible **3**, récompense affichée **50 XP/10 coins** | `20260604200000:63-66` |
| Quête hebdo (SQL, faisant foi) | `beat_2_bosses` : cible **2** (boss ≥ 60 %), affichée **100 XP/25 coins** | `20260604200000:68-71` ; `20260606130000:496-507` |
| Constantes TS divergentes (jamais lues) | `DEFAULT_DAILY_OBJECTIVES` (3_exercises **75/15**) ; `DEFAULT_WEEKLY_QUESTS` (beat_2_bosses **200/50**) | `gamification.ts:72-81` |
| Timer boss (UI seulement) | **20 s/question** (non vérifié côté serveur) | `gamification.ts:84` ; `quest.$exerciseId.tsx:207` |
| Donjon — prérequis | tentatives dans ≥ **2 matières** et ≥ **3 chapitres** distincts | `gamification.ts:97-100` ; `20260608123000:45-47` |
| Donjon — runs/jour | `min(level, 5)` (niveau 0 ⇒ 0) | `gamification.ts:94,103-105` ; `20260608123000:55` |
| Donjon — accès premium | entitlement vivant sur **≥ 1 parcours `kind='concours'`** (pack famille inclus) | `20260608123000:59-63,87-88` |
| Donjon — difficulté des questions | `min(3, ⌈étage/5⌉)` | `20260601190000:107` |
| Donjon — récompenses | **15 XP/étage** ; **5 coins / 5 étages** ; 1 mauvaise réponse = run `failed` | `20260601190000:327-328,259-271` |
| Boutique — prix (coins) | skin_ninja 80 · skin_samurai 100 · skin_mage 120 · skin_dragon 250 · skin_samourai 500 · potion_xp_boost **50** (XP×2) · potion_xp_mega **120** (XP×3) · shield_retry **60** · booster_hint **30** · potion_rappel **120** (indice) · bouclier_flamme **250** (streak) | `20260522170000:303-311` ; `20260522153000:414-419` |
| Accès bêta approuvé | entitlement source `beta`, **3 mois** | `subscription.ts:34` ; `beta-access.server.ts:173-179` |
| Entitlement | 1 grant vivant max par (user, parcours) ; `expires_at NULL` = perpétuel ; révocation douce | `20260608120000:91-93,87-88` |
| Leaderboards | top **50** ; classement matière = somme `attempts.xp_earned`, vue matérialisée rafraîchie **5 min** (pg_cron) | `gamification.ts:66` ; `20260606150000:207-264` ; `20260604120000:126-139` |
| Rate limits (server fns) | submit **5/10 s** · indice **10/10 s** · achat **10/10 s** · signalement **5/60 s** · lien parent **20/60 s** · récup streak **3/60 s** · donjon start **5/30 s** / questions **10/10 s** / réponses **40/60 s** / finalize **3/30 s** | sources dans les `*.server.ts` respectifs |
| Constantes orphelines (ancien bonus vitesse supprimé par `20260604220000`) | `HALF_COIN_THRESHOLD_PCT` 40, `IDEAL_TIME_PER_QUESTION_S` 30, `MIN_DURATION_FLOOR_S` 15, `SPEED_FACTOR` 0.5–1.4 | `gamification.ts:22-32` |

## E. Processus métier de bout en bout

### 1. Inscription & onboarding
**Acteurs** : visiteur, Supabase Auth, triggers SQL, élève/parent. **Déclencheur** : signup.
**Étapes** : 1. INSERT `auth.users` → trigger `on_auth_user_created` → **`handle_new_user`** (`20260522134120:107-126`) : profil avec `display_name` (métadonnée → préfixe email → « Aspirant »), xp 0, level 1, rôle `student`. 2. `bootstrapProfile` (`auth.server.ts:24-64`) : `display_name` + RPC **`set_profile_role`** (`20260606150000:85-124`) — seul chemin sanctionné (GUC + trigger `prevent_role_escalation`), rôles `student`|`parent`. 3. `/onboarding` : intention → catalogue `getParcours`. 4. `setCurrentParcours` → RPC **`set_current_parcours`** (`20260608120000:224-260`) : `current_parcours_id` + sync `current_grade_id`.
**Garde-fous** : rôle jamais client-writable ; parcours inconnu ⇒ erreur ; un parcours `coming_soon` reste sélectionnable (seul le contenu est gaté).
**Cas limites** : géré — profil manquant recréé par `getDashboard` ; backfill `20260608122000`. **Non géré** — avec confirmation email obligatoire, pas de session au signup ⇒ `bootstrapProfile` jamais appelé : le rôle reste `student` même pour un parent (`auth.server.ts:12-15`).

### 2. Résolution d'accès premium
**Acteurs** : élève, RPC SQL, parent lié (pack famille). **Déclencheur** : `startExerciseSession` ou rendu UI.
**Étapes** : 1. **`resolve_exercise_access`** (`20260608121000:29-111`) : exercice → sujet → parcours `(theme_id, grade_id)`. 2. Sujet non mappé ou parcours non premium ⇒ `allowed=true`. 3. Premium ⇒ **`has_parcours_entitlement`** (`20260608120000:167-192`) : grant vivant détenu par l'utilisateur **ou un parent activement lié** (pack famille). 4. Sinon preview : `difficulty_1` ⇒ quiz OU difficulté ≤ 1 ; `full` ⇒ tout ; `none` ⇒ rien. 5. Refus ⇒ `PARCOURS_COMING_SOON` ou `PARCOURS_LOCKED` ; mapping UI **fail-closed** (`quest.server.ts:364-383`).
**Garde-fous** : catalogue seedé : 2 premium (`concours-9eme`, `concours-6eme`, preview `difficulty_1`) + 6 libres (`full`) ; `concours-6eme` `available` depuis `20260609160000` ; écritures entitlements impossibles côté client.
**Cas limites** : géré — `subjects.is_premium` legacy ignoré par le gate ; ancien gate global supprimé (`20260609000000`). **Non géré** — voir B-5 (INSERT direct `attempts`).

### 3. Boucle quête : quiz gate → session → soumission
**Acteurs** : élève, `quest.server.ts`, RPC `submit_exercise_attempt`. **Déclencheur** : « Commencer » sur une mission.
**Étapes** : 1. `getSubject` : chapitres + meilleurs scores + état quiz gate + contexte parcours. 2. `startExerciseSession` : (a) `resolve_exercise_access` ; (b) **quiz gate école uniquement** (`grade_id` non NULL) : `practice`/`boss` exige quiz du chapitre à **≥ 80 %** ET non rushé (≥ 4 s/question) ; thèmes non scolaires jamais gatés ; (c) INSERT `exercise_sessions` (horodatage serveur). 3. `submitAttempt` → RPC **`submit_exercise_attempt`** (`20260606130000:122-529`) : validation session/payload ; score = bonnes réponses / total questions ; durée serveur ; gates `tooFast`/≥60 %/`improved` ; potion armée appliquée **seulement si éligible** puis consommée ; INSERT `attempts` → `award_xp` → `award_coins` → badges ; échec < 60 % : retry shield consommé ⇒ pas de SM-2, sinon rappels J+1/3/7 ; adaptation difficulté ; daily +1 ; weekly +1 si boss ≥ 60 %. 4. Pour un quiz, la correction est **masquée** dans la réponse (anti-mémorisation du gate).
**Garde-fous** : scoring SECURITY DEFINER atomique ; `award_xp`/`award_coins` révoqués de `authenticated` (`20260606150000:52-55`, fait foi).
**Cas limites** : géré — double soumission, réponses dupliquées, exercice vide. **Non géré** — pas de timeout de session (une session ouverte des heures reste soumissible) ; récompenses des objectifs jamais versées (B-2).

### 4. Attribution XP & streak (`award_xp`, `20260606130000:537-636`)
**Étapes** : garde self-only (sauf service_role) ; verrou `FOR UPDATE` ; streak : actif hier ⇒ +1 ; déjà aujourd'hui ⇒ inchangé ; **trou d'exactement 1 jour + bouclier armé ⇒ +1 et conso** ; trou ≥ 2 j ⇒ reset à 1 **sans** consommer ; niveau/hero class/tier recalculés ; `longest_streak = GREATEST`.
**Garde-fous** : appel 0 XP met quand même à jour le streak (toute activité compte) ; mint client impossible.
**Cas limites** : **non géré** — le streak n'est jamais mis à **0** en base (reset ⇒ 1) ⇒ récupération payante inatteignable (B-3).

### 5. Consommables
**Étapes** : 1. **`purchase_shop_item`** (`20260602130000:13-58`) : déduction atomique, skin non rachetable, consommable quantity +1. 2. **`activate_inventory_item`** (`20260606130000:42-111`) : 2 slots indépendants — next-quest (multiplicateurs + retries, un seul armé) et passif (streakShield). 3. Consommation : potion dans submit (si éligible), retry shield sur échec < 60 %, streak shield dans `award_xp`. 4. **`consume_hint`** (`20260606140000:33-109`) : hint = `questions.explanation` ; **explication vide ⇒ aucune charge dépensée** ; décrément de la plus ancienne unité.
**Garde-fous** : invariant anti-gaspillage ; aucun consommable ne contourne les gates ; verrou ligne d'inventaire contre double consommation.
**Cas limites** : **non géré** — payload `{"hints":3}` du `booster_hint` ignoré : 1 achat = 1 charge (B-13) ; aucune potion `coinMultiplier` au catalogue alors que le code la supporte.

### 6. Progression : objectifs, hebdo, répétition espacée, badges
**Étapes** : 1. **`ensure_daily_weekly_goals`** (`20260604200000:48-76`) : upsert idempotent du daily `3_exercises` et du weekly `beat_2_bosses` (semaine UTC) ; appelé au dashboard et avant chaque submit. 2. Incréments dans `submit_exercise_attempt` (statut `completed` à la cible). 3. SM-2 : créé sur échec (J+1/3/7), affiché (max 3 dues) ; **pas de RPC de complétion** : la ligne reste `pending`. 4. Badges : catalogue **13 codes** seedés ; attribution idempotente par `award_badge_if_new` (`20260601150000:14-53`).
**Cas limites** : **non géré** — `xp_reward`/`coin_reward` des objectifs/quêtes jamais crédités (B-2) ; lignes SM-2 jamais soldées (B-16) ; 9/13 badges sans chemin d'attribution (B-4).

### 7. Donjon
**Étapes** : 1. **`get_dungeon_access`** (`20260608123000:19-105`) : refus dans l'ordre — pas d'entitlement concours (`reason='SUBSCRIPTION'`) → prérequis (2 matières/3 chapitres) → niveau < 1 → limite `min(level,5)` runs/jour (UTC). 2. **`start_dungeon_run`** revérifie le gate. 3. **`get_dungeon_questions`** : lots de 5 (1-20), aléatoires toutes matières, difficulté ≤ `min(3, ⌈étage/5⌉)`, sans `correct_option`, jamais re-servies. 4. **`submit_dungeon_answer`** : ordre d'étage validé ; bonne réponse ⇒ étage +1 ; mauvaise ⇒ `failed` immédiat ; correction renvoyée après coup. 5. **`finalize_dungeon_run`** : **15 XP/étage, 5 coins/5 étages** sur état serveur ; idempotent (`rewarded_at`).
**Garde-fous** : récompenses jamais dérivées du payload client ; rate limits.
**Cas limites** : géré — double finalisation, run inactif. Non géré — `p_duration_seconds` client (borné, décoratif) ; pas de chrono serveur par question.

### 8. Lien famille & rapport parent
**Étapes** : 1. **`link_student_by_code`** (`20260602130000:109-161`) : rôle parent/admin requis, code = UUID élève en hex, cible `role='student'`, pas d'auto-lien ; upsert `is_active=true` ; INSERT direct révoqué. 2. `getLinkedStudents` : parent ⇒ liens actifs ; admin ⇒ tous les élèves paginés. 3. **`get_student_report`** (`20260601173000:88-260`) : admin ou parent activement lié ; score de sérieux = 4 × 25 pts (streak/7, jours actifs 7j/5, score moyen/80, minutes/120) ; verdicts ≥80 excellent / ≥60 good / ≥40 average / >0 needs_improvement / inactive ; activité 30 j. 4. **Pack famille** : l'entitlement du parent ouvre les parcours premium des enfants liés actifs ; le parent voit les entitlements de l'enfant (RLS).
**Cas limites** : géré — re-lien (réactivation). **Non géré** — aucune voie applicative de **déliaison** (B-9) ; le code alliance est l'UUID brut de l'élève (non régénérable).

### 9. Beta access & provisioning admin
**Étapes** : 1. `requestBetaAccess` : INSERT `pending` (refus si pending/approved existant). 2. Admin : liste + badge compteur. 3. **`admin_review_beta_request`** (`20260609000000:27-63`, fait foi : status-only) ⇒ approved/rejected. 4. Si approbation : **`admin_grant_parcours`** source `beta`, **+3 mois**, parcours courant premium sinon flagship `concours-9eme` (`beta-access.server.ts:154-188`). 5. Provisioning manuel : grant/revoke/list (RPCs gardés `is_admin()`). Vente hors-bande : téléphone **+216 55 447 504** (`subscription.ts:6`).
**Cas limites** : géré — re-grant, backfill anciens abonnés. **Non géré** — approbation en 2 écritures non atomiques : échec du grant ⇒ demande `approved` sans accès, non rattrapable par l'UI (`ALREADY_REVIEWED`) (B-11).

### 10. Signalement de contenu
**Étapes** : 1. `reportContentError` : rate limit 5/60 s, message 5-1000, INSERT `open` (RLS self+open). 2. Admin : liste (open d'abord) + compteur. 3. **`admin_resolve_content_report`** (`20260603170000:93-117`) : `resolved`|`dismissed` + horodatage. Correction du contenu via le pipeline `content/` (hors DB applicative).
**Cycle de vie** : `open → resolved | dismissed` ; pas d'état « en cours », pas de réouverture.
**Cas limites** : géré — question/exercice supprimés. **Non géré** — résolution sans vérif du statut courant (un `resolved` peut être réécrit `dismissed`) ; l'utilisateur n'est pas notifié de l'issue.

## F. Constats transverses candidats — processus & règles (B-*)

1. **B-1 — Constantes d'objectifs contradictoires et mortes.** `DEFAULT_DAILY_OBJECTIVES`/`DEFAULT_WEEKLY_QUESTS` (`gamification.ts:72-81`) importées nulle part et contredisant le SQL faisant foi (`20260604200000:63-71`) : 3_exercises 75/15 vs **50/10** ; beat_2_bosses 200/50 vs **100/25** ; types `10_min` et `maintain_streak_5` inexistants en base.
2. **B-2 — Récompenses d'objectifs jamais versées.** `daily_objectives.xp_reward/coin_reward` et `weekly_quests.*` créés, affichés (`dashboard.server.ts:452-468`) et passés `completed` (`20260606130000:485-507`), mais **aucun code ne crédite ces XP/coins**.
3. **B-3 — Récupération de streak (15 coins) inatteignable.** Le banner exige `current_streak === 0` (`progression.server.ts:29-34`), mais `award_xp` ne met jamais le streak à 0 (reset ⇒ **1**, `20260606130000:600-604`) — fonctionnalité morte en pratique.
4. **B-4 — 9 badges sur 13 inattribuables.** Le scoring n'attribue que `first_quest`, `perfect_score`, `speed_demon`, `streak_7`. `streak_30`, `boss_slayer`, `math_master`, `polyglot`, `level_10`, `collector`, `rich_kid`, `night_owl`, `math_blitz` n'ont aucun chemin d'attribution.
5. **B-5 — INSERT direct sur `attempts` toujours ouvert.** Policy « Users insert own attempts » (`20260522134120:101`) jamais révoquée : un utilisateur authentifié peut forger des `attempts` (score, xp_earned arbitraires) via PostgREST, contournant l'anti-farm et faussant : leaderboard matière (somme `attempts.xp_earned`), quiz gate (lecture `attempts` ≥ 80 %), prérequis donjon, meilleurs scores. Seul le profil (XP global) reste protégé. **→ recoupement C3 (sécurité).**
6. **B-6 — RPC orphelin.** `has_parcours_entitlement_for_subject` (`20260608120000:198-213`) appelé nulle part dans `src/`.
7. **B-7 — Tables sans UI.** `theory_scrolls` et `exercise_assignments` (`20260522153000:96-293`) : RLS complètes, aucun server fn/composant ne les utilise.
8. **B-8 — Doc de récompenses en retard sur le gate.** `rewards-and-modes.md:23-27` dit « difficulté 3-4 premium » alors que le gate réel verrouille **≥ 2** (`FREE_PREVIEW_MAX_DIFFICULTY=1`).
9. **B-9 — Aucun chemin de déliaison parent-élève.** UPDATE/DELETE révoqués, aucun RPC d'unlink : un lien actif (rapport + pack famille) ne se désactive que par SQL admin.
10. **B-10 — `speed_demon` incohérent avec l'anti-rush.** Badge exige < 60 s total avec ≥ 60 % ; `tooFast` exige ≥ 4 s/question : pour ≥ 15 questions, fenêtre vide — badge mathématiquement impossible sur ces exercices.
11. **B-11 — Approbation bêta non atomique.** Review (statut) puis grant (accès) en 2 appels : échec du second ⇒ `approved` sans entitlement, non rattrapable (`ALREADY_REVIEWED`).
12. **B-12 — Nommage hérité dans le gate donjon.** `has_subscription`/`'SUBSCRIPTION'` (`20260608123000:28,88`) pour un gate d'entitlement — assumé (commentaire `:9-12`) mais trompeur.
13. **B-13 — Payload d'indices ignoré.** `booster_hint` vendu `{"hints":3}` (`20260522170000:311`) mais `consume_hint` ne lit jamais ce nombre : **1 achat = 1 charge** — l'acheteur reçoit 1 révélation, pas 3.
14. **B-14 — Rate limiting fail-open local en dégradé.** Si `check_rate_limit` échoue, fallback Map mémoire par instance (`rate-limit.ts:38-62`) — non partagé entre instances serverless.
15. **B-15 — Constantes de vitesse orphelines.** `HALF_COIN_THRESHOLD_PCT`, `IDEAL_TIME_PER_QUESTION_S`, `MIN_DURATION_FLOOR_S`, `SPEED_FACTOR_*` (`gamification.ts:22-32`) sans logique depuis `20260604220000`.
16. **B-16 — Répétition espacée jamais soldée.** `spaced_repetition_schedule.status` reste `pending` à vie ; rejouer l'exercice ne marque pas la révision faite — les rappels dus s'affichent indéfiniment.

---

*Prochaine étape (S2) : vérifier ces candidats en conditions réelles (walkthrough personas sur TEST), compléter par les constats UX impossibles à voir dans le code, puis trier en findings définitifs (S3).*
