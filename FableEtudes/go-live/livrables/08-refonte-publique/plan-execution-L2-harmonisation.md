# Plan d'exécution — L2 : Harmonisation public ↔ connecté (thèmes + navigation)

> Livrable **kickoff** du lot **L2** du chantier **C8 — Refonte plateforme publique & gratuite**
> (voir [`../../08-refonte-plateforme-publique.md`](../../08-refonte-plateforme-publique.md)).
> Opérationnalise l'[`audit-coexistence-public-connecte.md`](./audit-coexistence-public-connecte.md)
> (reco #1 « coquille adaptative ») pour les **deux axes demandés par Mohamed** : **thèmes** +
> **navigation/menus**. Date kickoff : **2026-06-27**. Statut : 🟠 **plan validé, exécution à lancer**.
> Plan détaillé = ici (le fichier chantier reste court, pilotage).
>
> **✅ ÉTAT 2026-06-27 : CHANTIER LIVRÉ — les 2 axes + correctifs sont EN PROD.** Phase 1 (thèmes
> unifiés, PR #206 `279e74f`) + Phase 2 (convergence nav, PR #207 `689ee95`) + **GAP-047** (a11y
> connecté sous Référence : badge premium-lock `subject-path-card` rendu opaque, PR #208 `3733e05`,
> **e2e-auth 66 passed**) + **suivi UX** (en-tête public auth-aware, PR #209 `f114568` ; CTA accueil
> auth-aware → /dashboard, PR #210 `c4d2e5e`) + **HUD compte persistant** (🔥série·⚡XP, 2 coquilles, PR #212 `b4706b0`) mergés sur `main`. **Restes optionnels (non bloquants)** :
> purge i18n mort `discover` · vote catalogue coming-soon (gardé en onboarding) · veille visuelle Jeu sous reference/light (→ GAP-036/043).

---

## 0. Objectif

Unifier la coexistence « monde public anonyme » ↔ « monde connecté » sur **deux critères**, sans
régression et sans contenu/page dupliqué :

1. **Thèmes** — un **système de thèmes unifié** : 3 thèmes conservés, **un sélecteur unique** présent
   **partout** (public + connecté), choix **persisté**, appliqué **globalement et de façon cohérente**
   (navigation, pages publiques, leçons, exercices, jeux, profil) — **aucun mélange** en navigant.
2. **Navigation** — la nav connectée **converge** sur la nav publique : le menu **« Exploration / Découvrir »**
   pointe sur **« Découvrir le programme »** (`/programme`) et toute la chaîne derrière ; **zéro page ni code dupliqué**.

**Hors périmètre de ce lot** (versés/laissés au backlog, cf. §6) : HUD compte persistant, `returnTo`
au signup, nav mobile publique, valeur dormante (révision espacée, narration, badges). Ils restent
pertinents (audit reco #2/#3/#4/#6) mais **n'appartiennent pas aux deux axes demandés**.

---

## 1. Décisions actées (Mohamed, 2026-06-27)

| # | Décision | Détail / conséquence |
|---|----------|----------------------|
| D1 | **Modèle « thème unique choisi par l'utilisateur »** | Le thème devient `f(choix explicite)`, **pas** `f(auth)` ni `f(route)`. **Supersède** la reco d'audit #1 « registre piloté par l'auth » et nuance la décision C8 du 21/06 (« double registre ») : le double registre devient **défaut + ton éditorial**, plus une bascule visuelle automatique. |
| D2 | **Thème par défaut (visiteur sans préférence) = Référence (teal lecture)** | Préserve la 1ʳᵉ impression public-first / SEO / parents-enseignants. `DEFAULT_THEME = "reference"`. |
| D3 | **Convergence navigation = port complet (zéro perte)** | La nav publique devient **auth-aware** et **récupère toutes** les fonctions du flux connecté (sélection de parcours, cadenas premium/entitlements, vote coming-soon). On supprime ensuite les pages connectées doublonnes. |
| D4 | **Persistance = locale seule** (cookie + localStorage) | Déjà en place et SSR-safe. **Pas** de colonne `profiles.theme` pour l'instant (pas de migration). |
| D5 | **Séquencement = thèmes d'abord**, navigation ensuite | Plus petit, isolé, faible risque ; règle immédiatement le « mélange de thèmes ». |
| D6 | **HUD persistant / nav mobile publique = backlog** | Hors des deux axes demandés ; déjà tracés (audit reco #2/#6, GAP-036/043). |

---

## 2. État des lieux (vérifié sur le code, 2026-06-27)

### 2.1 Thèmes — 3 registres, 2 natures différentes (cause racine du mélange)

| Thème | Mécanisme actuel | Sélectionnable | Appliqué |
|-------|------------------|----------------|----------|
| **Sombre — Arène** (néon violet) | `:root` → `<html class="dark">` | ✅ toggle | shell connecté |
| **Clair — Atome** (lime) | `html.light` ([styles.css:148](../../../yahia-quest-arena/src/styles.css)) | ✅ toggle | shell connecté |
| **Référence** (teal lecture) | `.register-reference` (**wrapper CSS de contexte**, [`_public.tsx:21`](../../../yahia-quest-arena/src/routes/_public.tsx)) — **ignore le toggle** | ❌ **forcé** | shell public |

- Modèle : `Theme = "dark" \| "light"` (2 valeurs), `THEMES`, `DEFAULT_THEME="dark"`, `isTheme`,
  `themeFromCookieHeader` — [`src/lib/theme/context.ts`](../../../yahia-quest-arena/src/lib/theme/context.ts).
- Persistance : `localStorage` + cookie `xp-scholars-theme` + lecture SSR `getShellTheme` →
  `<html class>` ([`__root.tsx:159`](../../../yahia-quest-arena/src/routes/__root.tsx)) — anti-flash OK.
- Sélecteur : **toggle 2 états** (Lune/Soleil), `toggleTheme()`
  ([`theme-switcher.tsx`](../../../yahia-quest-arena/src/components/ui/theme-switcher.tsx)), **uniquement** dans le header connecté.
- **Le mélange = mécanique** : un connecté en « Clair » qui ouvre `/chapitre` → `.register-reference`
  **force le teal** par-dessus son choix.
- Défauts de cohérence relevés par l'audit §3.4 à traiter ici : (a) registre lié au layout,
  (b) **3 vocabulaires dorés** (teal / tokens `--gold` / ambre Tailwind brut dans
  [`public-landing.tsx`](../../../yahia-quest-arena/src/components/public/public-landing.tsx)),
  (c) `theme-color` PWA figé `#0a0a0a`, couleurs de correctness mélangées (`emerald-*` littéral vs `--success`).

### 2.2 Navigation — la lecture est déjà convergée ; le catalogue ne l'est pas

| Chaîne publique | Chaîne connectée | État |
|---|---|---|
| `/programme` (`ProgrammeCatalogue`) | `/themes` « Découvrir » (`ProgramHub`, hub circulaire) | **Dupliqué** (même `getParcours`, 2 UI) |
| `/niveau/$id` (`ParcoursSubjects`) | `/themes_.$familyId` (`ProgramCategory` : sélection + cadenas + vote) | **Dupliqué** |
| `/matiere/$id` (`SubjectHub`) | `/subject/$id` → **301** | ✅ déjà convergé |
| `/chapitre/$id` (`LessonReader`) | `/lesson/$id` → **301** | ✅ déjà convergé |
| `/exercice/$id` (practice anon) | `/quest/$id` (scoré, XP) | différents **par design** (gameplay) — **non fusionnés** ; seule la **carte QCM** est ~80 % dupliquée (audit §3.3) |

Menu connecté `primaryNav` ([`_authenticated.tsx:107`](../../../yahia-quest-arena/src/routes/_authenticated.tsx)) :
`/dashboard` (Hall des Héros) · `/parcours` (Parcours) · **`/themes` (Découvrir)** · `/dungeon` (Donjon) · `/leaderboard` (Classement).
Menu public ([`public-header.tsx`](../../../yahia-quest-arena/src/components/public/public-header.tsx)) :
**`/programme` (Découvrir le programme)** · `/extras` (Extras).

---

## 3. Phase 1 — Thèmes (à exécuter en premier)

> **Branche** : `feat/theme-harmonisation` (worktree depuis `main`). **Tree partagé** entre sessions
> → commits sélectifs (cf. [[reference_shared_tree_selective_commit]]). **Node 22** requis (cf. [[project_local_node_version]]).
>
> ⏸️ **PRÉREQUIS BLOQUANT (décision Mohamed 2026-06-27)** : ne démarrer qu'**après le merge sur `main`**
> de la branche SEO `feat/seo-public-metadata` **et** de l'IP-protection (worktree `_wt-ip`). Raison :
> `styles.css`, `_public.tsx` et `__root.tsx` sont modifiés (non commités/non poussés) dans ces deux
> chantiers — partir d'un `main` post-merge évite les conflits. **Vérifier `git -C yahia-quest-arena log --oneline main`** (présence des commits SEO/IP) avant de créer le worktree.

### 1.1 — Élargir le modèle à 3 thèmes
- `Theme = "dark" | "light" | "reference"` ; `THEMES = ["dark","light","reference"]` ;
  `DEFAULT_THEME = "reference"` ; `isTheme` + `themeFromCookieHeader` mis à jour.
- Fichiers : [`context.ts`](../../../yahia-quest-arena/src/lib/theme/context.ts),
  [`provider.tsx`](../../../yahia-quest-arena/src/lib/theme/provider.tsx) (`applyThemeClass` retire les 3 classes),
  [`__root.tsx`](../../../yahia-quest-arena/src/routes/__root.tsx) (SSR — marche tel quel une fois l'union élargie, à vérifier).
- Tests : [`theme.test.tsx`](../../../yahia-quest-arena/src/lib/theme/__tests__/theme.test.tsx) (défaut → reference, parse 3 valeurs, application/retrait des 3 classes).
- ⚠️ `toggleTheme()` (binaire) devient inadapté → remplacé par `setTheme` via le sélecteur (1.3) ;
  garder ou retirer `toggleTheme` selon usage résiduel (vérifier les références).

### 1.2 — Promouvoir « Référence » en vrai thème `<html>`
- Déplacer le bloc CSS `.register-reference` ([styles.css:530](../../../yahia-quest-arena/src/styles.css)) vers **`html.reference`**
  (conserver les règles `.lesson-content` qui en dépendent ; décider si on garde un alias `.register-reference` transitoire ou si on purge — viser la purge, DoD §3).
- **Retirer le wrapper forcé** `register-reference` de [`_public.tsx:21`](../../../yahia-quest-arena/src/routes/_public.tsx) → la coquille publique hérite du thème global `<html>`.

### 1.3 — Sélecteur 3 choix, présent partout
- Convertir [`theme-switcher.tsx`](../../../yahia-quest-arena/src/components/ui/theme-switcher.tsx) :
  toggle → **dropdown 3 options** (reprendre le pattern de
  [`language-switcher.tsx`](../../../yahia-quest-arena/src/components/ui/language-switcher.tsx) : bouton + menu + click-outside).
- Libellés **i18n fr/en/ar** (namespace existant) — proposition : « Lecture / Référence », « Arène / Sombre », « Atome / Clair ».
- Monté dans **les deux** en-têtes : [`public-header.tsx`](../../../yahia-quest-arena/src/components/public/public-header.tsx) **et** [`_authenticated.tsx`](../../../yahia-quest-arena/src/routes/_authenticated.tsx).

### 1.4 — Audit CSS croisé : 3 thèmes × 2 coquilles
- Chaque thème doit rendre correctement dans **les deux** shells. Réconcilier les overrides scopés
  `html.light .app-shell { … }` ([styles.css:286](../../../yahia-quest-arena/src/styles.css)) — aujourd'hui dark/light
  n'ont été réglés que pour `.app-shell`, et reference que pour le public.
- Vérifier la **lisibilité des cours** (`.lesson-content`) en Arène et Atome (le teal Référence retinte aujourd'hui neon/gold→teal ; sans lui, vérifier le rendu).
- Vérifs visuelles : preview MCP sur build prod (cf. [[project_local_preview_screenshot]] : screenshot KO sur dev-server).

### 1.5 — Cohérence (dette thème audit §3.4)
- Aligner les **3 vocabulaires dorés** (ambre Tailwind brut de `public-landing.tsx` → tokens).
- `theme-color` PWA **dynamique** par thème (figé `#0a0a0a`).
- Tokens de correctness (`emerald-*` littéral → `--success`).

### 1.6 — Tests
- Recréer l'e2e du **sélecteur** (le spec `theme-switcher` avait été supprimé en C8 faute de toggle public — cf. C8 journal nonies).
- Couvrir : choix persisté (reload même thème), pas de mélange public↔connecté (le thème reste constant en traversant `/programme` → `/dashboard`).

**DoD Phase 1** : `npm run verify` vert · pas de mélange constaté (vérif live 3 thèmes × public+connecté) · pas de classe `.register-reference` forcée résiduelle · sélecteur visible et fonctionnel dans les 2 shells.

---

## 4. Phase 2 — Navigation (convergence catalogue, port complet)

> **Branche** : `feat/nav-converge-catalogue` (après Phase 1).

### 2.1 — Rendre le flux public **auth-aware** (port complet des fonctions connectées)
- `/programme` (`ProgrammeCatalogue`), `/niveau/$id` (`ParcoursSubjects`), `/extras` : quand `isAuthenticated`,
  afficher **« entrer / choisir ce parcours »** (`setCurrentParcours`), l'**état entitlement/premium** (cadenas),
  et le **vote coming-soon** (`useParcoursInterest`) ; sinon CTA « découvrir / créer un compte ».
- Pattern déjà éprouvé : `SubjectHub` reçoit `isAuthenticated` via `useAuth` et route `/quest` vs `/exercice`.

### 2.2 — Repointer le menu connecté « Découvrir »
- `primaryNav` ([`_authenticated.tsx:107`](../../../yahia-quest-arena/src/routes/_authenticated.tsx)) : `/themes` → **`/programme`**.
- Aligner le vocabulaire des menus (audit §3.5 : « Découvrir le programme / niveau / matière »).

### 2.3 — Supprimer les doublons (DoD §3 : supprimer ce qu'on remplace)
- **301** : `/themes` → `/programme`, `/themes_.$familyId` → `/niveau/$id` (pattern `/subject`→`/matiere`).
- **Supprimer** les composants devenus morts : `ProgramHub`, `ProgramCategory`, routes `themes.tsx` / `themes_.$familyId.tsx`
  (vérifier `buildPrograms`/`flagshipLabel` : réutilisés par `/programme` — à **conserver**, pas supprimer).

### 2.4 — Dédup code QCM (la seule vraie redondance restante)
- Extraire `<QcmQuestionCard>` partagé (présentation pure, prop `register`) entre
  [`practice-exercise.tsx`](../../../yahia-quest-arena/src/features/quest/components/practice-exercise.tsx) et le bloc inline de
  [`quest.$exerciseId.tsx`](../../../yahia-quest-arena/src/routes/_authenticated/quest.$exerciseId.tsx) (audit §3.3 / reco #5). Recoupe GAP-031 (route monolithique).

### 2.5 — Tests
- Restaurer les e2e du **gate visuel matière** (**GAP-035**) une fois la couche connectée ré-affichée.
- Couvrir le **catalogue auth-aware** (anon = découvrir ; connecté = choisir/entrer/cadenas).

**DoD Phase 2** : `npm run verify` vert · `/themes*` redirigent · `ProgramHub`/`ProgramCategory` supprimés (zéro import mort) · le menu « Découvrir » mène à `/programme` · une session connectée peut choisir/entrer un parcours depuis le catalogue public.

---

## 5. Risques & garde-fous

- **Tree git partagé** entre sessions (+ session SEO `feat/seo-public-metadata` possiblement active) →
  commits **sélectifs** ; ne jamais `checkout`/`rebase` l'arbre partagé sous une autre session. cf. [[reference_shared_tree_selective_commit]].
- **Gate flaky sous charge RAM** → lancer `verify` **seul** (pas en // d'un build/vitest) ; `--no-file-parallelism` si besoin. cf. [[reference_local_gate_flakiness]].
- **Node 22** obligatoire (node 24 casse `auth-js`). cf. [[project_local_node_version]].
- **DB ↔ code** : D4 = pas de migration (persistance locale) → Phase 1 est **code-only**. Phase 2 idem (routes/UI, `getParcours` déjà anon).
- **Régression connecté** : le port auth-aware ne doit rien retirer au connecté (cadenas/sélection) — couverture e2e authed (dépend du seed GAP-011, déjà résolu en CI).
- **Lisibilité contenu** : sans le teal forcé, valider les cours en Arène/Atome avant merge.

---

## 6. Rattachement backlog (GAP)

| GAP | Rôle dans ce lot |
|-----|------------------|
| **GAP-045** (nouveau) | **Phase 1 — Harmonisation des thèmes** (sélecteur 3 thèmes unifié, persisté, appliqué partout, zéro mélange). |
| **GAP-046** (nouveau) | **Phase 2 — Convergence navigation/catalogue** (Exploration→Découvrir le programme, port complet, suppression doublons, dédup QCM). |
| GAP-035 | Restaurer les e2e du gate visuel matière → **Phase 2.5**. |
| GAP-036 | « Public trop fade » → adressé en partie par Phase 1.4/1.5 (cohérence visuelle) ; le reste (design) reste ouvert. |
| GAP-043 | « Refonte page connectée + parité public↔connecté » → Phase 2 contribue (convergence) ; refonte visuelle = ouvert. |
| Backlog (audit reco #2/#3/#4/#6/#10) | HUD persistant, `returnTo`, récompense fantôme, nav mobile publique, valeur dormante — **hors lot**. |

---

## 7. Journal du lot L2 (append-only)
| Date | Fait | Reste / prochaine étape |
|------|------|--------------------------|
| 2026-06-27 | **Kickoff L2 rédigé & validé** (2 axes, 6 décisions D1-D6). Étude code à jour (thèmes + nav). 2 GAP d'exécution créés (045 thèmes, 046 nav). **Tree inspecté** → occupé par SEO + IP-protection ; 3 fichiers thèmes cibles déjà modifiés. | ⏸️ **BLOQUÉ** (décision Mohamed) : attendre merge SEO + IP sur `main`. Au vert → **Phase 1 étape 1.1** (modèle 3 thèmes) en worktree `feat/theme-harmonisation` depuis un `main` à jour. |
| 2026-06-27 | **QA visuelle PUBLIQUE — VERTE** (dev server worktree :8081 Node 22 + preview MCP `preview_inspect`/`eval`). Home + `/programme` : les 3 thèmes s'appliquent **globalement** (reference→teal `rgb(15,110,86)` · light→lime `oklch(0.895 0.2 122)` · dark→violet `oklch(0.66 0.27 295)`) ; **plus de teal forcé** → une page publique honore le thème global = **fin du mélange** ; **sélecteur 3 choix** présent, dropdown OK, libellés Référence/Clair/Sombre, `aria-checked` suit le thème actif, **sélection appliquée + persistée** (localStorage) bout-en-bout (pick Référence/Clair/Sombre → `html.{reference,light,dark}`) ; `/programme` charge la data sous reference. **Scoping 1.5** : theme-color (`__root.tsx:99` figé `#0a0a0a`) **entrelacé au refactor head() SEO** → différer ; `emerald-*` sur 10 fichiers (badges de statut légitimes + correctness) → sweep ciblé, hors cœur ; landing `game-block` (ambre + `#15120d`) = **décision design** (bloc Jeu fixe vs adaptatif). | **Reste Phase 1** : QA visuelle **connecté** (login requis — risque faible, reference partage les overrides shell de light) ; **1.5** (décisions ci-dessus) ; **1.6** e2e sélecteur. Puis **Phase 2**. |
| 2026-06-27 | **Phase 1 cœur COMMITÉ + PR ouverte** : commit `3c1bb94` (13 fichiers, +268/−142) poussé sur `feat/theme-harmonisation` → **PR [#206](https://github.com/MBeji/yahia-quest-arena/pull/206)** (base `main`). Pré-push gate **844 tests verts** (2 faux-échecs écartés : ① flakiness worker-fork vitest sous charge AV+dist → `rm dist` ; ② `.env` prod copié pour la QA déclenchait le garde `assertNotProd` du test e2e-env → `.env` worktree retiré). CI PR en cours. | Revue/merge PR #206 (Mohamed). Puis suites Phase 1 (QA connecté, 1.5, 1.6) + Phase 2. |
| 2026-06-27 | **1.6 — e2e du sélecteur livré** (commit `bc43fb3` → PR #206). Spec backendless `e2e/public/theme-switcher.spec.ts` : défaut reference · pick via le picker → `html.dark` + persistance localStorage · reload persiste · **navigation vers une autre route garde le thème = no-mixing** · round-trip reference. Hooks locale-indépendants (`data-testid="theme-trigger"`, `data-theme-value`) + helper `NavBar.changeTheme()`. Pré-push **844 verts** (la flakiness worker-fork venait du **dev server preview encore lancé** → `preview_stop` puis retry vert). **`e2e.yml` dispatché** (run 28292014905). | Confirmer e2e vert · revue/merge #206 · reste QA connecté + **1.5** + **Phase 2**. |
| 2026-06-27 | **Phase 1 MERGÉE EN PROD** (PR #206 → `main` `279e74f`). **Phase 2 (navigation) LIVRÉE EN PR** (worktree `feat/nav-converge-catalogue`) : « Découvrir » connecté → `/programme` ; `/themes`+`/themes_.$familyId` → **301** vers `/programme` ; **suppression** ProgramHub+ProgramCategory+2 tests (**−1078 l.**) ; **conservé** `program-families` (partagé par le catalogue public) ; `/niveau` gagne le CTA auth-aware **« Choisir ce parcours »** (`setCurrentParcours`→dashboard) = remplacement convergé du switch `/themes` ; `FlagshipConcoursBanner`→`/programme` ; i18n `niveau.choose/choosing` ; spec e2e authed nav repointée. Gate : lint+typecheck verts, **tests 835** (run sériel ; parallèle flake RAM). **Commits `60a0868`+`742aeb0` → PR [#207](https://github.com/MBeji/yahia-quest-arena/pull/207)** ; e2e.yml + e2e-auth.yml dispatchés. | **Différés** (notés) : purge namespace i18n mort `discover` · vote coming-soon sur les cartes catalogue (conservé en onboarding) · QA visuelle connecté. Confirmer e2e + revue/merge #207. |
| 2026-06-27 | **CLÔTURE.** #207 (nav) **mergé** `689ee95`. L'e2e-auth a révélé **GAP-047** (badge premium-lock du dashboard illisible sous Référence — la QA visuelle connecté 1.4 différée, matérialisée ; dormant en prod via override mais bloquant l'e2e + latent). **Corrigé** (chip opaque `bg-card`+`text-foreground`) & **mergé** #208 `3733e05` → **e2e-auth 66 passed**. **🎯 Les 2 axes (thèmes + nav) + la régression a11y = EN PROD.** | **Restes optionnels** : purge i18n mort `discover` · vote catalogue coming-soon (gardé onboarding) · veille visuelle Jeu sous reference/light (GAP-036/043). |
| 2026-06-27 | **Suivi UX post-convergence (signalé par Mohamed).** Un connecté atterrissant sur une page publique (`/programme`, cours…) voyait l'en-tête « déconnecté » qui proposait de se connecter. Cause : `PublicHeader` affichait toujours Connexion/Créer-un-compte sans tenir compte de l'auth (et la convergence Phase 2 route le « Découvrir » connecté vers `/programme`, sous la coquille publique). **Corrigé** : `PublicHeader` rendu **auth-aware** (`useAuth`) — connecté → lien **« Mon espace » → `/dashboard`** (jamais login/signup), anon inchangé ; i18n `public.header.account` (fr/en/ar) ; test composant 2 états. Corrige **toutes** les pages publiques vues en connecté (même en-tête partagé). **Mergé PR [#209](https://github.com/MBeji/yahia-quest-arena/pull/209) `f114568`.** C'est la **tranche minimale** du HUD compte persistant (audit reco #1/#6). | **Restes optionnels** : HUD riche (XP/série sur le contenu) · **landing body** auth-aware (CTA « Créer mon compte » encore visibles pour un connecté sur `/`) · purge i18n `discover` · vote catalogue coming-soon. |
| 2026-06-27 | **Landing body auth-aware (2ᵉ incohérence résiduelle).** Le bloc « Apprends en jouant » de l'accueil proposait « Créer mon compte gratuit » → `/signup` à tout le monde, **même à un connecté** — dernier *pitch inscription* du corps public (tous les autres liens = contenu : `/programme`, `/niveau`, `/extras`). **Corrigé** : `PublicLanding` rendu **auth-aware** (`useAuth`) — connecté → CTA **« Continuer à jouer » → `/dashboard`** ; anon inchangé ; i18n `public.landing.gameCtaAuthed` (fr/en/ar) ; test 2 états. Worktree **isolé** `_wt-landing` off `main` (arbre partagé occupé par WIP // sur `public-landing.tsx` + i18n). Gate vert (lint+typecheck+**837**). **Mergé PR [#210](https://github.com/MBeji/yahia-quest-arena/pull/210) `c4d2e5e`.** | **HUD compte persistant complet** = prochaine étape, **en cadrage** (étude demandée) : données `useMyStats` (queryKey `["me-stats"]`, séparé de `["me-role"]`) · présentation `HeroStatChips` (réutilisable) ou variante compacte · montage `public-header.tsx` branche connectée · garde-fous **D1** + **GAP-047**. |
| 2026-06-27 | **HUD compte persistant — LIVRÉ** (audit reco #1/#6 ; étude validée par Mohamed : **2 coquilles** + compact **série+XP**). Un connecté sur du contenu public ne voyait aucune trace de son compte (XP/série = `/dashboard` only). **Ajouté** : hook **`useMyStats`** (`@/features/auth` ; `["me-stats"]` séparé de `["me-role"]` ; select `xp,current_streak`) + composant **`AccountHud`** (`@/components/account-hud` ; 🔥série·⚡XP cliquable→`/dashboard` ; fallback libellé « Mon espace » avant chargement) **monté dans les 2 coquilles** (`public-header.tsx` connecté — remplace « Mon espace » — + `_authenticated.tsx` groupe actions). **Thème-safe (GAP-047)** : chiffres `text-foreground` sur `bg-card` opaque, tokens or/--flame sur icônes `aria-hidden` seules. Worktree isolé `_wt-hud` ; **verify 864 + e2e-auth (axe 3 thèmes shell connecté) verts** ; restack #211/#213 + re-run avant merge (main bougeait). **Mergé PR [#212](https://github.com/MBeji/yahia-quest-arena/pull/212) `b4706b0`.** | **Reste backlog audit** (hors 2 axes) : récompense fantôme anon (#4) · `returnTo` signup (#2) · UI révision espacée (#3). + restes L2 : purge i18n `discover` · vote catalogue coming-soon. |
| 2026-06-27 | **DÉBLOQUÉ** (SEO #202/#205 + IP #201 mergés sur `main`, HEAD `e9a5625`). **Phase 1 cœur implémenté & vérifié** dans worktree isolé `feat/theme-harmonisation` (depuis `origin/main`) : ① modèle **3 thèmes** (`Theme=dark\|light\|reference`, **défaut `reference`**, `THEMES`/`isTheme`/tests) ; ② **`html.reference`** promu en thème global teal **complet** (placé à côté de `:root`/`html.light` ; tokens gradients/shadows/ambient/subjects/champagne ajoutés) ; ③ **sélecteur 3 choix** (dropdown, pattern `language-switcher`, i18n `theme` fr/en/ar) — déjà rendu dans `_authenticated.tsx`, **ajouté à `public-header.tsx`** ; ④ wrapper forcé retiré de `_public.tsx` → classe **`.public-shell`** (structurelle, découplée du thème : garde IP `img`, watermark print, typo leçon — re-scopées) ; ⑤ overrides in-shell partagés light↔reference via **`html:is(.light, .reference)`** ; ⑥ Toaster `reference/light→light` ; ⑦ `toggleTheme` retiré (plus utilisé). **Gate VERT : lint+typecheck+844 tests ; build prod OK (CSS valide).** **Rien commité** (DoD §6). | **Phase 1.4 QA visuelle** (3 thèmes × public+connecté, via build prod servi — screenshot dev-server KO cf. [[project_local_preview_screenshot]]) · **1.5** cohérence (landing ambre Tailwind→tokens · `theme-color` PWA dynamique · correctness `emerald-*`→`--success`) · **1.6** e2e sélecteur. Puis **Phase 2** (nav). |
