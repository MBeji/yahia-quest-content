# Plan d'exécution — Lots L0 (ouverture de l'accès) & L1 (écrans Référence)

> Livrable du chantier **C8** — fait suite à [`etude-conception-ux.md`](./etude-conception-ux.md)
> (conception) et aux 5 maquettes validées (direction visuelle, étude §6.0).
> **MVP du pivot = L0 + L1.** Rédigé le 2026-06-21. Statut : **à exécuter** (PR par PR).

## Règles du jeu (rappel DoD — CLAUDE.md)

- Chaque PR : **gate vert** (`npm run verify` ; `ci:verify` pour le release-grade), **tests
  co-localisés**, **zéro affaiblissement** (pas de `as any`, pas de règle ESLint désactivée inline,
  pas de `--no-verify`), **pas de dette/shim**, frontières features respectées.
- **Migrations** : additives d'abord (s'appliquent en prod au merge via `db-migrate-prod.yml`) ;
  toute **destructive** (DROP/REVOKE) part dans un merge **séparé et postérieur** au code qui cesse
  d'utiliser l'ancienne forme. Chaque migration ⇒ **garde pgTAP** (applique sur DB fraîche).
- **Nouvelle table/colonne** ⇒ ses **GRANT** explicites (piège connu CI pgTAP).
- **Contenu pédagogique : on n'y touche pas** (produit hors chantier).
- **i18n** : toute chaîne via les 3 catalogues `fr/en/ar` (typés) ; **RTL/AR** préservé.
- **Sécurité — invariants à ne jamais casser** : ne **jamais** exposer `questions.correct_option`
  côté client (acquis GAP-020) ; ne **jamais** ouvrir les RLS de `profiles`/`attempts`/gameplay ;
  n'ouvrir en lecture anonyme que le **contenu `source='admin'`**.

---

## LOT 0 — Ouverture de l'accès (fondations, non visibles UI)

Rend le contenu **techniquement** atteignable par un anonyme, sans encore refondre les écrans.
Ordre de merge **strict** (chaque étape additive et sûre seule).

### PR L0.1 — Middleware d'authentification optionnelle
- **Quoi** : créer `optionalSupabaseAuth` à côté de `requireSupabaseAuth` — si JWT présent →
  client authentifié (comportement actuel) ; sinon → **client `anon`** (clé publishable, sans
  header `Authorization`), `context.userId = null`.
- **Fichiers** : [`src/shared/integrations/supabase/auth-middleware.ts`](../../../yahia-quest-arena/src/shared/integrations/supabase/auth-middleware.ts) (ajout, ne pas casser
  l'existant — fichier marqué « generated », éditer avec soin) ; helper client anon dans
  [`src/shared/integrations/supabase/client.ts`](../../../yahia-quest-arena/src/shared/integrations/supabase/client.ts).
- **Migration** : aucune. **Tests** : middleware avec/sans JWT (contexte injecté correct).
- **Dépend de** : —. **Visible UI** : non.

### PR L0.2 — RLS : lecture anonyme du contenu admin
- **Quoi** : migration **additive** ajoutant des policies **`anon` SELECT** sur `exercises` et
  `questions` **limitées à `source='admin'`** (rouvre, pour l'anon seulement, ce que
  `20260522153000` avait restreint à `authenticated`). `themes/grades/subjects/chapters` sont déjà
  `USING(true)`. Vérifier/poser les **GRANT SELECT … TO anon** (baseline `20260612221000` les a déjà
  pour la plupart — confirmer pour `questions`).
- **Garde-fou** : `correct_option` reste **non lisible** côté client (la notation se fait via RPC,
  L0.3) — la policy n'expose que prompt/options/explication selon le masquage en place.
- **Fichiers** : `supabase/migrations/<ts>_anon_read_admin_content.sql` + garde
  `supabase/tests/…anon_read.test.sql` (pgTAP).
- **Dépend de** : —. **Visible UI** : non.

### PR L0.3 — RPC publique de notation sans état `check_answers`
- **Quoi** : RPC `SECURITY DEFINER` `check_answers(exercise_id uuid, answers jsonb)` **callable par
  `anon`** : renvoie, par question, correct/incorrect + `explanation`, **sans** créer de
  `exercise_session`/`attempt`, **sans** XP/récompense, **sans** exposer la clé. S'appuie sur la
  logique de correction existante (cf. `submit_exercise_attempt`) en lecture seule. **Rate-limit**
  (réutiliser `src/shared/lib/rate-limit`) + `GRANT EXECUTE TO anon`.
- **Fichiers** : `supabase/migrations/<ts>_check_answers_rpc.sql` + pgTAP ; wrapper server fn (ex.
  `checkAnswersPublic`) en `optionalSupabaseAuth` dans `quest.server.ts`.
- **Dépend de** : L0.2. **Visible UI** : non (consommé en L1.5).

### PR L0.4 — Server fns de contenu en accès optionnel
- **Quoi** : basculer les server fns **de lecture de contenu** de `requireSupabaseAuth` →
  `optionalSupabaseAuth`, et adapter le retour selon `userId` (anon = pas d'étoiles/scores/locks ;
  connecté = comportement actuel). Concerne notamment `getSubject`, `getChapterLesson`,
  `getExercise` ([`src/features/quest/quest.server.ts`](../../../yahia-quest-arena/src/features/quest/quest.server.ts)) et un **module catalogue public** (thèmes/
  grades/matières par niveau — nouvelles server fns publiques ou adaptation de l'existant). **Ne PAS
  toucher** aux fns gameplay (`startExerciseSession`, `submitAttempt`, `revealHint`, dashboard,
  leaderboard) qui restent `requireSupabaseAuth`.
- **Fichiers** : `quest.server.ts` ; nouveau `src/features/catalog/` (ou public fns) ;
  barrels `index.ts`.
- **Migration** : aucune. **Tests** : chaque fn en mode anon (pas de fuite de données compte) + mode
  connecté (inchangé).
- **Dépend de** : L0.1, L0.2. **Visible UI** : pas encore (routes encore gardées).

### PR L0.5 — Restructuration & renommage des routes (2 coquilles)
- **Quoi** : créer la **coquille publique** (sans garde) et y **déplacer + renommer** les routes de
  contenu ; conserver la coquille gardée (renommée `_compte`) pour les surfaces compte ; **retirer
  la redirection globale** `useEffect` de [`_authenticated.tsx`](../../../yahia-quest-arena/src/routes/_authenticated.tsx) pour les routes déplacées.
  Ajouter **redirections 301** des anciens chemins.
  - Public : `/` · `/programme` · `/parcours/$cycle` · `/niveau/$grade` · `/matiere/$subjectId`
    (ex `subject.$subjectId`) · `/chapitre/$chapterId` (ex `lesson.$chapterId`) ·
    `/exercice/$exerciseId` (ex `quest.$exerciseId`) · `/extras` (ex `/themes`) · `/connexion`.
  - Gardé `_compte` : `/tableau-de-bord` · `/classement` · `/donjon` · `/profil` · `/demarrage` ·
    `/admin/*`.
- **Fichiers** : arborescence `src/routes/**` (déplacements/renommages) ; `routeTree.gen.ts` **se
  régénère** (ne pas éditer) ; redirections.
- **Migration** : aucune. **Tests** : e2e public (route contenu accessible **sans** session) +
  e2e authed (routes compte toujours gardées) ; 301 vérifiées.
- **Dépend de** : L0.4 (sinon une route publique appelle une fn qui throw). **Visible UI** : **oui**
  — le contenu devient atteignable sans login (même si le *design* arrive en L1).

### PR L0.6 — Débranchement du premium
- **Quoi** : neutraliser le gate (`resolve_exercise_access` → toujours « autorisé », ou bypass
  côté code) ; **retirer** l'écran paywall ([`subscription-paywall.tsx`](../../../yahia-quest-arena/src/features/subscription/components/subscription-paywall.tsx)) et les cadenas
  premium ([`journey-map.tsx`](../../../yahia-quest-arena/src/features/parcours/components/journey-map.tsx), [`subject-path-card.tsx`](../../../yahia-quest-arena/src/features/dashboard/components/subject-path-card.tsx)) ; **donjon : seuil de niveau** au
  lieu du gate entitlement ([`dungeon.tsx`](../../../yahia-quest-arena/src/routes/_authenticated/dungeon.tsx)). Tables `parcours_entitlements` **laissées dormantes**.
- **Fichiers** : `src/features/subscription/**` (retrait des usages, garder l'admin si utile),
  `dungeon.tsx`, composants à cadenas ; migration **additive** si on remplace la fonction SQL
  (`<ts>_open_access.sql`). **Aucune** brique paiement/soutien.
- **Migration** : additive (remplacement de fonction) ; tout REVOKE/DROP éventuel → **plus tard**,
  séparé. **Tests** : accès mission difficulté ≥2 sans entitlement = ouvert ; donjon gated par
  niveau.
- **Dépend de** : —. **Visible UI** : oui (plus de paywall).

---

## LOT 1 — Écrans Référence (le pivot devient visible et beau)

S'appuie sur L0. Chaque écran suit la **direction visuelle validée** (étude §6.0 : clair + teal).

### PR L1.1 — Coquille publique (chrome) + nav par état
- `PublicHeader` (logo, Programme/Extras/recherche, sélecteurs, **1 CTA « Créer mon compte »**) +
  `PublicFooter` (sitemap 3 parcours × niveaux pour le SEO, « 100 % gratuit »). Bottom-nav mobile
  publique. i18n `layout`.
- **Fichiers** : `src/components/public/**` (nouveau), route racine publique, `src/lib/i18n/*`.

### PR L1.2 — Accueil repositionné
- Hero référence (promesse + recherche + preuve gratuité) · `PersonaDoors` (élève/parent/enseignant)
  · aperçu 3 parcours · **un** bloc doré « apprends en jouant » (passerelle Jeu). Réécriture
  `landing`.
- **Fichiers** : [`src/routes/index.tsx`](../../../yahia-quest-arena/src/routes/index.tsx), [`src/components/landing/**`](../../../yahia-quest-arena/src/components/landing/), i18n `landing`.

### PR L1.3 — Catalogue `/programme` + `/parcours/$cycle` + `/extras`
- `CycleCatalog` (3 parcours → bloc concours doré), `ParcoursOverview` (niveaux ordonnés, états
  **« Bientôt »**), `ExtrasSection` (hors-programme séparé). **Mapping grade→cycle** (Primaire 1re-6e
  / Collège 7e-9e / Lycée 1re-Bac) : dériver d'un champ `cycle` sur `grades` **ou** mapping statique
  (à trancher en implémentation — additif si colonne).
- **Fichiers** : `src/features/catalog/**`, routes publiques `programme` / `parcours.$cycle` /
  `extras`, i18n `catalog`/`cycles`.

### PR L1.4 — Lecteur de cours `/chapitre`
- `LessonReader` registre Référence : typographie de lecture, mode clair, bascule Cours/Résumé,
  **Imprimer/Exporter PDF** + **Partager** (affordance enseignant), invitation douce en bas.
- **Fichiers** : route `chapitre.$chapterId` (ex `lesson.$chapterId.tsx`), `src/features/quest/**`
  (composant lecture), i18n `print`/`share`.

### PR L1.5 — Exercice « mode entraînement » anonyme
- `PracticeRunner` : pour l'anon, jeu de QCM → **`check_answers`** (L0.3) → correction immédiate +
  explication ; écran de fin avec **`AccountInvite`** (« +50 XP », « Plus tard »). Connecté = flux
  jeu actuel inchangé. `AccountInvite` réutilisable.
- **Fichiers** : route `exercice.$exerciseId` (ex `quest.$exerciseId.tsx`), `src/features/quest/**`,
  `src/components/public/AccountInvite.tsx`, i18n `account`/`invite`.

### PR L1.6 — Balayage i18n / fin du lexique premium
- Retirer `subscription`/premium de l'UX, simplifier `onboarding` (retirer intent/concours/explore),
  nettoyer `parcours`/`explorer` (premium/locked), recadrer `auth` (« crée ton compte gratuit »).
  Ajouter `account`/`invite`/`catalog`/`cycles`/`print`/`share`. Vérifier FR/EN/AR + RTL.
- **Fichiers** : `src/lib/i18n/{fr,en,ar}.ts` + `types.ts`, et les composants concernés.

> **Onboarding « parcours + classe »** et la **resignification data du concept `parcours`** (cycles
> multi-grades, `profiles.current_parcours_id`) appartiennent à **L2** (couche jeu) — voir étude §12.
> En L1, le catalogue présente les 3 cycles **sans** dépendre de ce refactor (dérivation grade→cycle).

---

## Séquencement & ordre de merge

```
L0.1 ─┐
L0.2 ─┼─► L0.4 ─► L0.5 ─► (contenu public atteignable)
L0.3 ─┘                         │
L0.6 (indépendant) ─────────────┤
                                ▼
L1.1 ─► L1.2 / L1.3 / L1.4 / L1.5 (parallélisables) ─► L1.6 (balayage final)
```

- **Bloquant** : ne pas merger L0.5 (routes publiques) avant L0.4 (fns en accès optionnel), sinon
  une page publique appelle une fn qui `throw` pour l'anon.
- L0.3 (`check_answers`) avant L1.5 (UI entraînement anon).
- L0.6 (premium off) peut avancer en parallèle de L0.1-0.5.
- **~12 PRs** au total (6 L0 + 6 L1), chacune petite et réversible.

## Vérification de bout en bout (avant de déclarer le MVP fait)

1. Visiteur **sans compte** : ouvre `/programme` → parcours → matière → **lit un cours** → **fait un
   exercice avec correction** → voit l'invitation compte (non bloquante). **0 redirection login.**
2. **SEO** : page `/chapitre/...` rendue en SSR, `<title>`/OG corrects, présente dans le sitemap.
3. Élève **connecté** : tout le mode jeu (XP, dashboard, donjon par niveau) **inchangé** ; aucun
   paywall nulle part.
4. **Sécurité** : `GET …/questions?select=correct_option` (anon) ne fuit pas la clé ; RLS
   `profiles`/`attempts` intactes ; `check_answers` rate-limité.
5. **Gate** : `ci:verify` vert ; e2e public (anon) + authed verts ; pgTAP vert sur DB fraîche.

## Hors de ce MVP (rappels)
- **L2** (enhancement jeu, onboarding parcours+classe, resignification `parcours`), **L3** (export
  enseignant), **backlog** (compte parent, reprise essais anon), **production de contenu** (sessions
  dédiées).
