# Chantier 04 — Architecture de production & plan de déploiement

> Pilotage : [00-MASTER-PLAN.md](./00-MASTER-PLAN.md) · Livrables volumineux : `go-live/livrables/04-architecture-prod/`

| | |
|---|---|
| **Statut** | 🟡 Conception 100 % (S1+S2+S3 ✅) · **backups prod opérationnels et testés (GAP-004 🟢)** — reste : monitoring câblé + ruleset + lots code |
| **Avancement** | 92 % (reste = wiring : UptimeRobot/Sentry/auth/ruleset ≈ 45 min Mohamed, puis lots code) |
| **Dépendances** | C2 ✅ (GAP-007/027/029 versés) · C3 ✅ (GAP-022/023/004) · C6 (hypothèses volume/coûts — défauts D1 de C2 utilisés en attendant) |
| **Alimente** | Checklist Go/No-Go (livrée ✅) · C7 (runbooks d'exploitation) |
| **Dernière session** | 2026-06-12 (S3 : runbook déploiement & rollback consolidé + checklist Go/No-Go infra + plan tag v1.0.0) |
| **Prochaine action** | **✅ 14/06 — bascule prod sur `na9ranal3ab.vercel.app` TERMINÉE & vérifiée** : git link `na9ranal3ab`→`main` confirmé (API), ancien `xpscholars-app` déconnecté + **cron désactivé** (confirmés API), Redirect URL Supabase Auth posée par Mohamed. **Reste domaine** : brancher `.tn` quand acheté (ATI). · **Go/No-Go 6/10 ✅ — chemin critique restant (≈ 45 min Mohamed + mes lots)** : ① UptimeRobot (10 min, autonome) → A6 ; ② checklist auth hardening (15 min) → A8/A9 + trancher bouton Google ; ③ importer ruleset `main` (5 min) → A5 ; ④ comptes Sentry (DSN) + PostHog EU (clé) → **je câble les SDK** → A7/B1. Puis lots code (CSP nonce · lovable 2.4/Nitro) + tag v1.0.0 quand A=10/10. Drill backup : **rejouer mensuellement** (`gh workflow run db-backup.yml -f target=prod -f drill=true`). Grille : [checklist-go-no-go.md](./livrables/04-architecture-prod/checklist-go-no-go.md) |

## Contexte à charger en début de session
- Ce fichier + `00-MASTER-PLAN.md`
- `yahia-quest-arena/CLAUDE.md` (stack, déploiement Vercel, DoD §7 migrations)
- Conclusions C2 et C3 (synthèses uniquement) quand disponibles
- Selon la tâche : `vercel.json`, `wrangler.jsonc`, `scripts/build-vercel.mjs`, `docs/environment-variables.md`, `docs/release-tagging-policy.md`

## Objectifs (périmètre validé)
- Choisir l'infrastructure cible (Cloud, VPS, PaaS, Serverless…).
- Définir la stratégie de déploiement et d'exploitation.
- Sélectionner nom de domaine, certificats SSL, services réseau.
- Choisir la base de données et l'architecture de stockage adaptées.
- Mettre en place supervision, monitoring, alerting, logging.
- Définir les mécanismes de sauvegarde et restauration.
- Optimiser pour le marché tunisien (latence, coûts, disponibilité).
- Établir un modèle de coûts prévisionnel et les leviers d'optimisation.

## Livrables attendus
- [x] Dossier d'architecture de production (décisions argumentées, schéma) — [dossier-architecture.md](./livrables/04-architecture-prod/dossier-architecture.md)
- [x] Décision infra actée : **rester Vercel + Supabase** (critères mesurés, dossier §1) ; Cloudflare requalifié porteur (pas vestige) → simplification = lot Nitro §4
- [~] Domaine + DNS + SSL + emails transactionnels configurés — **checklist prête** ([checklist-domaine-smtp.md](./livrables/04-architecture-prod/checklist-domaine-smtp.md)), exécution au palier 1 (choix du nom, C5)
- [~] Stack monitoring/alerting/logging opérationnelle — **checklist prête** ([checklist-exploitation.md](./livrables/04-architecture-prod/checklist-exploitation.md)) ; UptimeRobot autonome, Sentry/PostHog = lots code après clés Mohamed
- [x] Stratégie d'environnements + **runbook déploiement & rollback** — [runbook-deploiement.md](./livrables/04-architecture-prod/runbook-deploiement.md)
- [x] Plan backup/restore mis en œuvre et **testé** — drills **TEST + PROD verts** (2026-06-12, invariants validés sur dump prod réel) ; nocturne armé ; runbook repo ; drill mensuel à rejouer (GAP-004 🟢)
- [x] Modèle de coûts prévisionnel (paliers selon trafic) + leviers — dossier §2 ; synthèse [checklist-go-no-go.md](./livrables/04-architecture-prod/checklist-go-no-go.md) §D
- [x] **Checklist Go/No-Go infra** (bonus S3) — [checklist-go-no-go.md](./livrables/04-architecture-prod/checklist-go-no-go.md)

## Plan d'exécution (kickoff 2026-06-12 — à valider)

**Reconnaissance faite** (C2/C3 ont déblayé l'essentiel — C4 décide et outille, il ne ré-audite pas) :
- **Architecture actuelle connue et éprouvée** : fonction serverless Vercel Node 22, région
  **`arn1`/Stockholm épinglée** (co-localisée Supabase eu-north-1), `maxDuration: 30` ; build via
  pipeline custom Worker→Node (`build-vercel.mjs` — **load-bearing**, GAP-007) ; headers sécu déjà
  posés au routing Vercel (HSTS/XFO/Referrer/Permissions + **CSP `unsafe-inline`** à durcir =
  GAP-022) ; assets immutables. Charge validée (C2/S2) : cibles beta tenues 9–17×, **plafond
  d'écriture entre 1× et 5×** → dimensionnement pool/plan (GAP-027).
- **Le repo ne référence aucun domaine custom ni SMTP** → app sur URL `*.vercel.app`, e-mails auth
  = SMTP Supabase par défaut (quota faible, délivrabilité non garantie) → GAP-006.
- Pas de monitoring outillé (GAP-002), backup/DR non formalisé (GAP-004), hardening Auth dashboard
  à vérifier (GAP-023), analytics produit à choisir (GAP-008), releases sans tag (GAP-028).
  Environnements : prod + TEST e2e (pas de staging). Env vars : 5, doc propre.
- ⚠️ **Conformité plateforme** : le build (`.vc-config.json`) suggère un plan Vercel **Hobby** —
  or Hobby est réservé à l'usage **non commercial**. Vendre les parcours premium dessus violerait
  les ToS → passage **Vercel Pro probablement obligatoire au lancement** (à confirmer, input 1).

### S1 — Dossier d'architecture & réseau (1 session) — ✅ faite le 2026-06-12 (PoC 1b restant)
- [x] 1a. **Décision infra actée** : rester Vercel + Supabase managé — critère clé : la charge C2 a
  été tenue 9–17× **sur un projet Supabase Free** (même tier que la prod) → le palier gratuit porte
  la beta. Schéma + analyse → [dossier-architecture.md](./livrables/04-architecture-prod/dossier-architecture.md) §1.
- [~] 1b. **Étude pipeline (GAP-007) — finding décisif** : lovable-config **2.x abandonne le plugin
  Cloudflare et passe sur Nitro** (presets natifs Vercel ET Cloudflare) → l'adaptateur custom
  `build-vercel.mjs` meurt quel que soit le choix de plateforme. **Reco : sortir de Lovable**
  (TanStack Start natif + preset Nitro, objectif « zéro Lovable »). Dossier §4. **Reste : le PoC
  sur branche** (time-boxé, critères de go définis).
- [x] 1c. **Domaine + SMTP** : [checklist-domaine-smtp.md](./livrables/04-architecture-prod/checklist-domaine-smtp.md)
  pas-à-pas (registrar, DNS, Vercel, Resend+DKIM, Supabase SMTP, adresses support). Déroulable dès
  que le nom est choisi (C5) — prérequis du palier 1.
- [x] 1d. **CSP nonce (GAP-022)** : design écrit (nonce par requête dans `src/server.ts`, CSP
  dynamique sur les réponses HTML, retrait de la CSP statique, point de risque = support nonce de
  TanStack Start). Dossier §6 — code en S2.
- [x] 1e. **Environnements/releases + modèle de coûts par paliers** : previews PR, pas de staging,
  rollback Vercel + migrations additives ; **paliers 0→3 avec déclencheurs mesurables** (0 $ beta →
  0-20 $ ventes → 25-45 $ croissance → 60-120 $ échelle) + **arbitrage palier 1 ToS Hobby :
  Vercel Pro 20 $ vs Cloudflare natif 0-5 $** (décision via PoC). Dossier §2/§3/§5.

### S2 — Exploitation outillée (1 session) — ✅ faite le 2026-06-12 (actions Mohamed en attente)
- [~] 2a/2b. **Monitoring + analytics** : [checklist-exploitation.md](./livrables/04-architecture-prod/checklist-exploitation.md)
  — UptimeRobot (autonome, zéro code), Sentry (DSN → je câble le SDK + capture branchée sur
  `logger.error`, les erreurs prod s'évaporent en ~1 h aujourd'hui), PostHog **Cloud EU** (clé →
  je câble events produit sans PII + funnel preview→premium). **Code après réception des 2 clés**
  (lot DoD dédié). + Vercel Analytics à activer (1 clic).
- [x] 2c. **Backup/DR (GAP-004)** : workflow [`db-backup.yml`](../yahia-quest-arena/.github/workflows/db-backup.yml)
  **mergé sur `main`** (merge `e619e97`) — dump nocturne prod (`public`+`auth`, -Fc, artefact 14 j)
  + mode **drill** (restauration dans un Postgres 17 jetable du runner + invariants) + gardes
  anti-croisement test/prod. Runbook complet : `docs/backup-restore-runbook.md` (repo). **1er run
  CI : KO sur le secret `TEST_SUPABASE_DB_URL` (user `postgres` nu — le pooler exige
  `postgres.<ref>` ; le `.env.test` local, correct, fonctionne)** → 2 secrets à (re)poser, puis
  drill à relancer.
- [x] 2d. **Hardening Auth (GAP-023)** : [checklist-auth-hardening.md](./livrables/04-architecture-prod/checklist-auth-hardening.md)
  (confirmations, politique mdp, HIBP, rate limits, rotation refresh token, Site URL, décision
  bouton Google) — à dérouler par Mohamed (~15 min).
- [x] 2e. **Mesures terrain (GAP-029 partiel)** : depuis la Tunisie sur l'URL prod — landing SSR
  TTFB **moy. 327 ms** (min 170 / max ~1 s = cold start), dashboard 366-552 ms, asset edge
  **~120 ms** chaud (692 ms 1er hit). **Mono-région arn1 validée pour la beta** (très large sous
  les 2 s cibles). Lighthouse → sur le domaine final. GAP-027 : rien à faire au palier 0
  (déclencheurs déjà actés au dossier §2).
- [x] **PoC Nitro (1b) — re-scopé** : TanStack Start actuel n'a AUCUN preset de déploiement →
  l'adaptateur custom était inévitable en 1.x ; la sortie passe par **lovable 2.4/Nitro** = vraie
  migration ~0,5-1 j (nitro beta, API config 2.x, portage wrapper 500, env) qui **débloque aussi
  Vite 8**. Dossier §4 mis à jour. Lot dédié à planifier (pré-palier 1 idéalement).
- **Différé volontairement** : code CSP nonce (GAP-022) → lot dédié avec vérif e2e (chemin SSR
  critique) ; design prêt (dossier §6).

### S3 — Runbook & Go/No-Go infra (0,5 session) — ✅ faite le 2026-06-12
- [x] 3a. **Runbook déploiement & rollback** consolidé → [runbook-deploiement.md](./livrables/04-architecture-prod/runbook-deploiement.md) :
  le fait fondateur (push `main` = deploy), flux PR nominal, **ordre migration obligatoire** +
  déploiement 3-temps, **rollback code (Instant Rollback Vercel) vs données (backup)** distingués,
  smoke post-déploiement (le chemin RPC garde-fou pgTAP), garde-fous CI en place. Ancré sur
  `migration-gate.yml` + ruleset `main-protection.json` + DoD §7 (rien de générique).
- [x] 3b. **Checklist Go/No-Go infra** → [checklist-go-no-go.md](./livrables/04-architecture-prod/checklist-go-no-go.md) :
  A bloquants (10, dont 4 ✅ / 2 🟡 secrets posés / 4 actions Mohamed) · B recommandés · C
  hors-palier-0 (déclencheurs mesurables) · D synthèse coûts · E décision datable. **Tag `v1.0.0`
  (GAP-028)** : procédure dans le runbook §5, à poser quand A=10/10.

**Partage des rôles** : les réglages dashboard (Vercel/Supabase) et les achats (domaine, comptes
SaaS) = **toi aux manettes, moi je fournis la checklist exacte pas-à-pas** ; le code (CSP nonce,
instrumentation Sentry/PostHog) = moi, DoD complet du repo.

### Décisions demandées à Mohamed (kickoff)
| # | Question | Proposition par défaut |
|---|----------|------------------------|
| D1 | Infra cible | **Rester Vercel + Supabase managé** pour le lancement (éprouvé par la charge) ; simplification pipeline étudiée en S1, exécutée avant launch **seulement si** gain net + risque faible |
| D2 | Plans & budget | **Vercel Pro (~20 $/mois) + Supabase Pro (~25 $/mois) au go-live** (Hobby = non-commercial ; Pro = backups quotidiens + ressources stables) ≈ **45 $/mois** hors domaine (~15 $/an) |
| D3 | Domaine & e-mail | Nom à choisir (mon défaut : **.com** pour simplicité d'achat/gestion, `.tn` en alias plus tard) + SMTP **Resend** (tier gratuit 3 000 mails/mois, suffisant beta) + adresse support à définir |
| D4 | Observabilité & analytics | **100 % tiers gratuits au lancement** : Sentry (erreurs), UptimeRobot (uptime/alertes), PostHog Cloud (analytics produit — solde GAP-008) |

### Inputs à fournir par Mohamed (avant S1)
1. **Plan Vercel actuel** (Hobby ou Pro ?) + **URL prod exacte**.
2. **Plan Supabase prod actuel** (Free ou Pro ?).
3. **Domaine** : déjà possédé ? Sinon 2-3 noms candidats.
4. **Budget infra mensuel** acceptable.
5. **Adresse e-mail** expéditeur/support souhaitée.

## Décisions
| Date | Décision | Motif |
|------|----------|-------|
| 2026-06-12 | **Inputs Mohamed reçus** : Vercel **Free** + Supabase **Free** actuellement ; URL prod `https://yahia-quest-arena.vercel.app/` ; **pas de domaine** ; budget « limité pour le démarrage, scalable si l'usage monte » | Kickoff |
| 2026-06-12 | **D2 amendée — modèle par paliers** : palier 0 (beta, pas de vente en ligne) = **rester Free+Free ≈ 0 $/mois** + backups DIY ; palier 1 (ouverture des ventes) = quitter Vercel Hobby (ToS non-commercial) via l'arbitrage **Vercel Pro 20 $/mois vs déploiement Cloudflare natif 0-5 $/mois** (étudié en S1/1b) ; palier 2 (croissance/données clients) = + Supabase Pro 25 $/mois (backups gérés) | Contrainte budget Mohamed ; charge beta prouvée sur tier Free (C2/S2) |
| 2026-06-12 | D1/D4 confirmées par défaut (rester Vercel+Supabase au palier 0 ; stack observabilité 100 % gratuite) ; D3 : domaine non possédé — choix du nom différé (lié C5 marketing), achat recommandé tôt (~12 $/an) mais non bloquant pour la beta | Inputs + budget |
| 2026-06-12 | **Secrets backup posés** : `TEST_SUPABASE_DB_URL` (corrigé, user `postgres.<ref>`) + `PROD_SUPABASE_DB_URL` ajoutés dans GitHub Secrets par Mohamed | Débloque le drill GAP-004 (A3/A4 du Go/No-Go) |

## Journal d'avancement (append-only)
| Date | Fait | Reste / prochaine étape |
|------|------|--------------------------|
| 2026-06-15 | **GAP-007 Part 1 — sortie de Lovable + Vite 8 livrée en prod** (de-vendor `5199db4` sur `main` en parallèle + Vite 8 via PR #110 ; PR #109 combinée fermée car redondante). Meta-plugin `@lovable.dev/vite-tanstack-config` de-vendorisé en `vite.config.ts` **inline** (mêmes plugins en direct : tanstackStart + react + tailwind + tsConfigPaths + cloudflare *build-only* ; `define` VITE_*, dedupe, port 8080, manualChunks préservés). Le cap `vite <8` venait des **sous-plugins sandbox Lovable** → **Vite 8 + plugin-react 6** débloqués sur le pipeline actuel (aucun Nitro requis). **bun→npm** : `bun.lock` (qui résolvait via le registre **privé** Lovable) + `bunfig.toml` supprimés, `package-lock.json` régénéré (registre public). Gate local complet vert (typecheck/lint/**683 tests**/build 2 envs/budgets/dev boot 200) + **preview Vercel verte** (parité build output confirmée). **Zéro dépendance Lovable.** | **Part 2 (reste GAP-007)** : tuer `build-vercel.mjs` via cible **Nitro/Vercel native** — recon : TanStack 1.168 n'a **aucun preset de déploiement** (Nitro absent du stack) → vraie R&D, PoC sur branche time-boxé. ✅ Tout mergé en prod (`5199db4` + PR #110) ; dependabot #3/#4/#6/#7 fermées + config dependabot **groupée** (anti-fragmentation). |
| 2026-06-14 | **Bascule prod clôturée & vérifiée.** Contrôles : git propre (working tree = seul `supabase/test-phase/` non suivi ; doublon `.vercel` ajouté par `vercel link` dans `.gitignore` **reverté**) ; la prod sert bien `origin/main` HEAD (`f07b699`). **API Vercel** : `na9ranal3ab` git-link → `MBeji/yahia-quest-arena` branche `main` (✅ `push main` = nouvelle prod), `xpscholars-app` **sans git-link** + **cron `disabledAt` posé** → action 2 Mohamed **confirmée par l'API** ; 5 env Production sur `na9ranal3ab` ; worktree + fichier env temp supprimés. Action 1 (Redirect URL Supabase Auth) **attestée par Mohamed** (non vérifiable hors dashboard). | Reste côté Mohamed : smoke test login/reset sur le nouveau domaine (optionnel) ; achat `.tn` → branchement (DNS+SSL+Auth) ; previews PR à compléter en scope Preview si utilisées. |
| 2026-06-13 | **Prod migrée sur la marque → nouveau projet Vercel `na9ranal3ab`** (demande Mohamed : projet dédié, **pas** un alias sur l'existant). Créé `na9ranal3ab` + 5 env Supabase prod **recopiées** — piège résolu : les clés prod sont *sensibles* donc **illisibles** via `vercel env pull` (renvoyé vide) → sourcées du `.env` local, ref `fasrenmmrkqjoobrztbp` **confirmée = prod** (diff avec `.env.test` `pqegdnwdtbjtplcthxyp` + décodage JWT role/ref/exp). **Bascule git propre** : `na9ranal3ab` connecté à `MBeji/yahia-quest-arena` (`main`), ancien `xpscholars-app` **déconnecté** de git → `push main` ne déploie plus que la nouvelle prod. **Déployé `origin/main` (f07b699)** via worktree dédié → **https://na9ranal3ab.vercel.app** READY (HTTP 200, région arn1, CSP nonce + HSTS/XFO/Referrer/Permissions live, 29 596 b = parité). Ancien `yahia-quest-arena.vercel.app` laissé **en ligne figé** (200, testeurs intacts). Toujours plan **Free** (ToS non-commercial — OK palier 0). | **Mohamed, dashboard (~5 min)** : ① **Supabase Auth** → ajouter `https://na9ranal3ab.vercel.app` aux *Redirect URLs* (+ trancher *Site URL*), sinon signup/reset/magic-link cassés sur le nouveau domaine ; ② **désactiver le cron** de `xpscholars-app` (Settings → Crons) pour éviter le double-envoi quand push-notifs aura ses secrets VAPID/CRON_SECRET. À noter : env posées en **Production** seule (previews PR à compléter si besoin) ; runbook → cible de déploiement = désormais `na9ranal3ab` ; **`.tn`** à brancher quand acheté (checklist domaine/SMTP). |
| 2026-06-13 | **Volet domaine débloqué par C5** : nom de marque tranché = **« Na9ra Nal3ab »** → domaine cible `na9ranal3ab.tn` (principal) + `.com` (libres au sondage DNS). La [checklist domaine/SMTP](./livrables/04-architecture-prod/checklist-domaine-smtp.md) devient déroulable **dès l'achat du domaine** (Mohamed, via registrar ATI). | Acheter le domaine → dérouler checklist domaine/SMTP (DNS Vercel + Resend/DKIM + Supabase Auth Site URL). |
| 2026-06-13 | **CSP nonce (GAP-022) → 🟢 DÉPLOYÉ + vérifié en prod** (`fa2d31d`). Push effectué via stash/rebase/push/restore du WIP concurrent : ① stash -u de la feature push-notifs concurrente ; ② rebase propre de mon commit sur origin/main (les 3 commits #91/#92/#93 ne touchaient aucun de mes 7 fichiers) ; ③ push (gate pre-push : 624 tests verts) → déploiement Vercel ; ④ restauration du WIP (stash pop) avec 2 conflits résolus : `auth-page.spec.ts` → version origin #92 (bilingue, canonique, supérieure à l'édition WIP redondante), `package-lock.json` → version origin (la session concurrente n'avait pas encore `npm install` ses deps web-push → à elle de réconcilier). **Curl prod confirme** : `script-src 'self' 'nonce-…'` live. WIP push-notifs intégralement restauré (17 modifs + 5 untracked). | RAS côté CSP. La session push-notifs doit `npm install` (web-push) avant de committer. |
| 2026-06-13 | **Lot code CSP nonce (GAP-022) — codé, validé, commité local (`92d8224`).** Le design §6 du dossier est implémenté : nonce par-requête généré côté serveur (`src/router.tsx`, `createIsomorphicFn().server()` + `setResponseHeader`), propagé à tous les `<script>` inline via `router.options.ssr.nonce` (recon faite dans `node_modules` : source unique, h3 event dispo dès `getRouter` via `runWithStartContext`/`requestHandler`) ; `script-src` passe à `'self' 'nonce-…'` (plus d'`'unsafe-inline'`) ; CSP statique retirée de `build-vercel.mjs` (autres headers conservés) ; politique centralisée dans `src/shared/lib/csp.ts`. Page d'erreur : `onclick` inline → `href` (non couvert par nonce). **Bug prod latent corrigé** : l'ancienne CSP bloquait Google Fonts (origines absentes) — révélé par l'e2e. Validé : gate unitaire (591) + build prod + e2e public dédié `security-headers.spec.ts` (4/4) + 42 autres specs publics. | **Push/déploiement différé** : l'arbre de travail contient une feature **push-notifications concurrente non commitée** (migration `20260613120000`, `src/features/notifications/`, sw.js, i18n, routes) — le pre-push `verify` tourne sur tout l'arbre. Décision push à valider avec Mohamed. Au passage : `auth-page.spec.ts` cassé depuis le flip locale FR du 11/06 (a3267c6) — flaggé (hors périmètre). |
| 2026-06-12 | **GAP-004 🟢 — backups prod opérationnels et TESTÉS.** Session de mise au vert du drill (4 itérations de debug, toutes côté env/secrets, 0 côté design) : ① outillage `gh` CLI installé (winget bloqué UAC → zip portable + PATH) + auth Mohamed ; ② **drill TEST vert 51 s** après fix wrapper PG16 du runner (PATH forcé `/usr/lib/postgresql/17/bin`, commit `50de2ba`) ; ③ drill PROD : 2 échecs secrets (host `%2` parasite, puis mdp faux — **diagnostic différentiel local** via sondes psycopg sur signatures d'erreur du pooler : suffixe tenant OK, mdp en cause) → reset mdp DB prod (alphanumérique, sans impact app) → **drill PROD vert 1 min 05** (run 27442412600) : dump réel restauré, 6 invariants OK (profiles=13, subjects=31, exercises=756, questions=4430, auth_users=13, RPC présente) ; ④ `upload-artifact` v4→v7 (`3fa1fd8`, échéance Node 24 forcé le 16/06) validé par le run vert. Nocturne 02:30 UTC armé. Go/No-Go : **A3/A4 ✅ → 6/10**. | Mohamed (~45 min) : UptimeRobot → A6 ; checklist auth → A8/A9 ; ruleset `main` → A5 ; Sentry DSN + PostHog clé → je câble → A7/B1. Drill : rejouer mensuellement. Puis lots code (CSP nonce · Nitro) + v1.0.0. |
| 2026-06-12 | **Kickoff rédigé** + reconnaissance : architecture actuelle cartographiée par C2 (Vercel Node 22 `arn1` + pipeline build custom load-bearing + headers posés sauf CSP nonce), repo sans domaine custom ni SMTP, ⚠️ plan Vercel Hobby suspecté (interdit l'usage commercial → Pro requis au lancement). Plan S1 (dossier archi + réseau) / S2 (exploitation outillée) / S3 (runbook + Go/No-Go) + décisions D1-D4 + 5 inputs demandés. | Validation du plan + D1-D4 + inputs par Mohamed → lancer S1. |
| 2026-06-12 | **S2 livrée (exploitation outillée)** : ① **Backups (GAP-004)** — workflow `db-backup.yml` mergé (`e619e97`) : dump nocturne prod public+auth → artefact 14 j, mode drill (Postgres jetable + invariants), gardes anti-croisement ; runbook `docs/backup-restore-runbook.md` (RPO 24 h/RTO 1 h, 2 scénarios de restauration, handoff Pro). 1er run CI KO → **secret `TEST_SUPABASE_DB_URL` invalide** (user `postgres` nu vs `postgres.<ref>` requis par le pooler) — 2 secrets à poser par Mohamed puis drill à relancer. ② **Mesures terrain TN (GAP-029)** : landing SSR TTFB moy 327 ms (max ~1 s cold), dashboard ≤ 552 ms, asset edge ~120 ms chaud → **mono-région arn1 validée pour la beta**. ③ **PoC Nitro re-scopé** : Start actuel sans preset de déploiement → sortie = lot lovable 2.4/Nitro ~0,5-1 j (débloque aussi Vite 8). ④ Checklists **exploitation** (UptimeRobot/Sentry/PostHog EU) et **auth hardening** (GAP-023) écrites. CSP nonce différé en lot dédié (design prêt). | 4 actions Mohamed (secrets, comptes, auth checklist, domaine) → lots code (Sentry/PostHog, CSP nonce, Nitro) → S3. |
| 2026-06-12 | **S3 livrée (runbook & Go/No-Go) → conception du chantier 100 %.** ① [runbook-deploiement.md](./livrables/04-architecture-prod/runbook-deploiement.md) : consolide en procédure exécutable le fait fondateur (push `main` = deploy prod), le flux PR nominal, **l'ordre migration obligatoire** + le déploiement 3-temps, le **rollback code (Instant Rollback Vercel) vs données (restauration backup)**, le smoke post-déploiement (chemin RPC garde-fou pgTAP), les garde-fous CI (ruleset, migration-gate, pgTAP, backup). ② [checklist-go-no-go.md](./livrables/04-architecture-prod/checklist-go-no-go.md) : grille binaire A (10 bloquants) / B (recommandés) / C (hors palier 0, déclencheurs mesurables) / D (coûts) / E (décision datable) — **état au 12/06 : NO-GO (pré-lancement)**, chemin critique ≈ 1 h Mohamed + lots code. Tag `v1.0.0` (GAP-028) = procédure runbook §5, à poser quand A=10/10. **2 secrets GitHub posés par Mohamed ✅** → drill à relancer (A3/A4). | **Reste = exécution, pas conception** : relancer le drill (drill UI ou gh) → A3/A4 ; Mohamed : UptimeRobot/Sentry/PostHog + checklist auth + ruleset `main` ; mes lots code : Sentry/PostHog · CSP nonce · lovable 2.4/Nitro. |
| 2026-06-12 | **Inputs reçus (Free+Free, pas de domaine, budget mini scalable) → D2 re-modelée en paliers → S1 livrée** : [dossier d'architecture](./livrables/04-architecture-prod/dossier-architecture.md) (décision infra actée — la charge C2 ayant tenu sur du tier Free, la beta reste à ~0 $/mois ; modèle de coûts paliers 0→3 à déclencheurs mesurables ; ⚠️ point dur = ToS Vercel Hobby à la 1ère vente → arbitrage Vercel Pro 20 $ vs **Cloudflare natif 0-5 $** ; finding GAP-007 : lovable 2.x = Nitro sans plugin CF → reco **sortir de Lovable**, PoC à faire ; design CSP nonce ; design backups DIY pg_dump) + [checklist domaine/SMTP](./livrables/04-architecture-prod/checklist-domaine-smtp.md) prête à dérouler. | S2 : Sentry/UptimeRobot/PostHog + CSP nonce (code) + workflow backups + drill + GAP-023 (avec Mohamed) + TTFB TN ; PoC Nitro time-boxé. Mohamed : choix du nom de domaine (C5). |
