# 🔁 Passation — session « mise à jour des tests e2e » (pivot public C8)

> **De** : session « non-régression + merge » · **Pour** : session « tests e2e » · **Date** : 2026-06-22
> **Objectif de ta session** : aligner les specs e2e sur l'architecture C8 (live sur main) et
> **reverdir l'e2e nightly de main**, via une **PR de suivi**.

---

## 🟢 1. CE QUI A CHANGÉ DEPUIS TON DERNIER POINT — lis ça d'abord

### a) PR #180 est **MERGÉE & LIVE EN PROD** (merge commit `d1d539d`, 2026-06-22)
Le pivot C8 (L0+L1) est déployé : `db-migrate-prod` vert (backup pg_dump + **2 migrations L0**
`anon_read_admin_catalogue` + `check_answers_public_rpc` appliquées au **prod**), CI main vert,
Vercel sert la landing public-first (`na9ranal3ab.vercel.app`, 0 reste RPG).

**Conséquences pour toi :**
- Ton alignement e2e **ne va plus dans #180** (close). Il faut **une PR de suivi**.
- **L'e2e nightly de main est ROUGE** en attendant (les specs périmées pré-C8 sont sur main ;
  l'e2e n'est **pas un check requis**, donc ça n'a pas bloqué le merge). **Ton job = le reverdir.**
- `main` = `d1d539d` (inclut tout #180). La branche `feat/optional-supabase-auth` (HEAD `738e839`)
  **n'a pas été supprimée** mais est désormais un **ancêtre de main**. Pour ta PR de suivi : commit
  tes specs (scopé, cf. §3), puis **rebase / nouvelle branche sur `origin/main` à jour**, PR vs main.

### b) 🆕 Un **switcher de langue public** a été ajouté (commit `738e839`, déjà sur main)
Fichier `src/components/public/public-header.tsx` — **ne le re-modifie pas, construis tes specs autour :**
- `<LanguageSwitcher />` (le composant **partagé** `@/components/ui/language-switcher`) est dans le
  header public : bouton **`aria-label="Change language"`** (globe + code FR/EN/AR) → menu
  **English / Français / العربية**. C'est **le même** que l'authed → mêmes locators
  (`getByRole('button', {name:/change language/i})`, `changeLanguage("English"/"Français"/"العربية")`).
- Les liens de nav `/programme` + `/extras` sont passés en **`hidden sm:flex`** (cachés < 640 px,
  visibles ≥ `sm`) — sinon le switcher 56 px faisait **overflow** le header mobile.
- Nouveau test composant `src/components/public/__tests__/public-header.test.tsx` (vert).

**Impact sur tes specs :**
- `e2e/public/i18n-switch.spec.ts` : **le switcher existe maintenant** → ce spec **n'est plus à
  supprimer**, il est réalisable (cible le switcher comme l'authed).
- `e2e/public/responsive.spec.ts` : nav publique **cachée < `sm`, visible ≥ `sm`** ; switcher
  **toujours présent**. (L'ancien `a[href="#features"]` n'existe plus dans `PublicLanding`.)

### c) ⚠️ PIÈGE CONFIRMÉ — l'**INDEX git est PARTAGÉ** entre nos sessions
Un `git add <mes-fichiers>` scopé a quand même embarqué **ta suppression pré-stagée de
`e2e/authed/quiz-unlock.spec.ts`** dans mon commit (rattrapé : reset + re-commit). **Avant CHAQUE
commit :** `git reset` → `git add <tes fichiers>` → **vérifie `git diff --cached --name-only` =
EXACTEMENT tes fichiers** → commit. **Jamais `git add -A`** (le working tree partagé porte aussi
content/* CNP, .github…).

---

## 📐 2. L'architecture C8 que les specs doivent matcher (live sur main)

| Avant (pré-C8) | Maintenant (C8, live) | Action spec |
|---|---|---|
| Hub matière `/subject/$id` (registre Jeu) | **Unifié `/matiere/$id`** (Référence) ; `/subject/$id` = **301** vers `/matiere/` | `DashboardPage.subjectCards` `a[href^="/subject/"]` → `a[href^="/matiere/"]` ; idem `SubjectPage.goto` |
| Cadenas premium sur la page matière | **Aucun cadenas** (pivot gratuit ; `getSubject` anon → `hasEntitlement:true`) | `premium-gate.spec` (lock sur matière) → **re-scoper / skip** jusqu'au retour premium |
| Toggle thème dans le header | Header Référence = **teal fixe** (`.register-reference`), **pas de toggle thème** | `theme-switcher.spec` (public) → **retirer** des projets publics |
| Toggle reduce-motion (ancienne landing) | **Purgé** avec l'ancienne landing | retirer l'assertion |
| Landing RPG (mur de login) | `PublicLanding` (promesse famille, 3 portes persona, 3 cycles, preuve gratuité, 1 bloc Jeu) | landing.spec réécrite (tu l'as déjà commencée) |
| — | Liens exercice **auth-aware** : connecté → `/quest/$id` (XP), anon → `/exercice/$id` ; quiz → toujours `/quest` | specs anon ciblent `/exercice`, authed `/quest` |

---

## 📂 3. État de TON travail (observé non-commité dans le working tree partagé)

Modifiés (non commités) : `e2e/public/landing.spec.ts` (déjà réécrite Référence), `auth-redirects.spec.ts`,
`e2e/pages/{landing,dashboard,subject}.page.ts`, `e2e/helpers/{users,db,env}.ts`,
`e2e/authed/{catalogue,premium-gate,quiz-gate,four-families,content-report}.spec.ts`,
**supprimé** `e2e/authed/quiz-unlock.spec.ts`, `playwright.config.ts`, `package.json`,
`.github/workflows/e2e-auth.yml`. + sources `src/components/public/public-landing.tsx`,
`src/features/quest/components/{lesson-reader,practice-exercise}.tsx` (probablement +`data-testid`).

⚠️ **À reconcilier avec mon `738e839`** (déjà sur main) : `public-header.tsx` est sur main — ne le
re-modifie pas. Mets ta branche à jour sur `origin/main` avant de finir.

---

## ✅ 4. Comment vérifier

- **Outils portables** (préfixe-les au PATH) : Node 22 = `_tools/node-v22.12.0-win-x64` (le node
  système v24 **crashe** `@supabase/auth-js`), gh = `_tools/gh/bin`.
- **Public (backendless), local** : `npm run test:e2e:install` puis `npm run test:e2e` (chromium + mobile).
- **CI** : `gh workflow run e2e.yml --ref <ta-branche>` (public) **et**
  `gh workflow run e2e-auth.yml --ref <ta-branche>` (public-anon + authed vs TEST).
- **TEST project** (`pqegdnwdtbjtplcthxyp`) : a déjà les 2 migrations L0. Le **seed fonctionne** —
  mon run e2e-auth a eu **46 passed** + ~5 fails = **uniquement** les specs périmées (locator
  `/subject/`, premium-gate). Maintenant que #180 est sur main, e2e-auth sur main n'aura plus le
  mismatch « Apply migrations to TEST » (avant, ma branche avait déjà poussé les migrations sur TEST).
- **Gate local flaky/RAM** : pool `threads` (`npm test -- --pool=threads`) ; ne pas chaîner
  `build`→`verify`. Cf. mémoire `reference_local_gate_flakiness`.

---

## 🎯 5. Definition of Done

1. Specs e2e alignées C8 — **public** : landing (fait) · responsive (nav < `sm` cachée, switcher
   présent) · theme-switcher retiré · **i18n-switch ciblant le switcher** ; **authed** : Page Objects
   `/subject`→`/matiere` · premium-gate re-scopé.
2. `e2e.yml` **et** `e2e-auth.yml` **verts** sur ta branche (CI).
3. **PR de suivi** ouverte + mergée → **e2e nightly de main reverdi**.
4. Commits **scopés** (reset → add → vérif `--cached` → commit). Tests qui voyagent avec le code (DoD §5).

> Détail du diagnostic complet (mapping échec→cause) : voir le journal du chantier
> [`08-refonte-plateforme-publique.md`](./08-refonte-plateforme-publique.md) + la mémoire
> `project_public_free_pivot`.
