# 📘 Dossier de passation — Na9ra Nal3ab

> **But de ce document :** permettre à une personne qui rejoint le projet de **tout comprendre et
> tout retrouver seule** — produit, business, technique, accès, exploitation — sans avoir à
> solliciter Mohamed. Document **vivant** : on le complète au fil de l'eau (voir §12 + le changelog
> en bas).
>
> **Comment le lire :** parcours-le de haut en bas une première fois pour la vue d'ensemble, puis
> reviens aux sections au besoin. Les **détails approfondis** sont dans les documents liés (§11) —
> ici on donne l'essentiel + le pointeur.
>
> Dernière mise à jour : **2026-07-11** · Mainteneur : **Mohamed Beji**
>
> ⚠️ **Pivot majeur postérieur à la rédaction initiale (2026-06-21, réaffirmé 2026-07-10/11) :**
> le produit est passé d'« académie payante au concours » à **plateforme publique 100 % gratuite**
> (contenu consultable et praticable sans compte ; migration `20260711100000` : plus aucun parcours
> premium). La machinerie premium (entitlements, paywall) est conservée **dormante et réversible**
> (étude `FableEtudes/01-paiement-en-ligne`, gelée). Les passages « modèle économique / tarifs /
> bascule premium » de ce dossier (§1 fin, §2, §8 Porte 2, glossaire) sont **requalifiés** en ce
> sens ci-dessous. Topo central à jour : `yahia-quest-arena/STATUS.md`.

---

## Sommaire
1. [Le projet en bref](#1-le-projet-en-bref)
2. [Vision, modèle économique & lancement](#2-vision-modèle-économique--lancement)
3. [Architecture technique](#3-architecture-technique)
4. [🔑 Accès, comptes & outils](#4--accès-comptes--outils)
5. [Exploitation au quotidien](#5-exploitation-au-quotidien)
6. [Le contenu pédagogique](#6-le-contenu-pédagogique)
7. [Sécurité & conformité](#7-sécurité--conformité)
8. [Roadmap & état d'avancement](#8-roadmap--état-davancement)
9. [Décisions clés (et pourquoi)](#9-décisions-clés-et-pourquoi)
10. [Glossaire](#10-glossaire)
11. [Documents détaillés & ressources](#11-documents-détaillés--ressources)
12. [À compléter au fil de l'eau](#12-à-compléter-au-fil-de-leau)

---

## 1. Le projet en bref

**Na9ra Nal3ab** (نقرا نلعب, derja tunisien = « j'apprends, je joue ») est une **académie
d'apprentissage en ligne gamifiée** pour collégiens tunisiens. L'élève fait des « quêtes »
(exercices QCM), gagne de l'XP, monte de niveau, débloque des badges, grimpe dans un classement et
affronte un « donjon » — esthétique manga/RPG, trilingue **FR / AR / EN**.

- **Le problème qu'on règle :** faire réviser un enfant est une bataille, et les cours particuliers
  coûtent cher. Na9ra Nal3ab rend la révision **désirable** → l'enfant révise **seul et avec
  plaisir**, le parent **suit ses progrès**.
- **Le fer de lance :** la préparation aux **concours nationaux** — entrée au **lycée pilote (9ème)**
  et au **collège pilote (6ème)**. L'académie est plus large (langues, culture générale, logique).
- **Double cible :** le **parent** paie (décideur), l'**enfant** utilise (prescripteur). Tout doit
  séduire les deux.
- **Marque :** « Na9ra Nal3ab » (toujours afficher le wordmark **+ le script arabe نقرا نلعب**).
  « XP » n'est PAS la marque — c'est juste la monnaie de points dans l'app. Ancien nom de travail
  abandonné : « XP Scholars ».
- **Marché :** Tunisie. ~169 000 élèves en 9ème, ~97 000 candidats concours (6ème+9ème)/an.

**Hiérarchie du catalogue** (modèle mental clé) :
`thèmes → niveaux (grades) → matières (subjects) → chapitres → exercices → questions`.
Seul le thème « école » a des niveaux. Un **parcours** = la piste où l'élève est inscrit (un couple
thème+niveau). **Tout est gratuit en phase actuelle** (pivot 2026-06-21) ; les parcours concours
(9ème, 6ème, bac-math) sont des jalons, plus des produits payants — le premium est **dormant**.

### 🚀 Par où commencer (ta première semaine)

> Objectif : être **autonome en ~1 semaine** sans solliciter Mohamed — tout est dans ce dossier + les liens.

**Jour 1 — Comprendre**
- Lis **ce dossier en entier** (~1 h) : c'est la carte du projet.
- Va sur la **prod** (`na9ranal3ab.vercel.app`) : crée un compte, fais une quête, regarde le dashboard.
- Parcours le **positionnement** + le **kit commercial** (§11 → `livrables/05-marketing/`).

**Jour 2 — Obtenir tes accès** (à demander à Mohamed, une seule fois — voir §4)
- **GitHub** : être ajouté comme collaborateur du dépôt `MBeji/yahia-quest-arena`.
- **Page Facebook** : être ajouté **admin/éditeur** (Paramètres → Accès à la Page).
- Selon ton rôle : Vercel · Supabase · Sentry · UptimeRobot · PostHog · + le **coffre de mots de passe**.

**Jour 3-4 — Première contribution** (selon ton profil)
- **Technique** : cloner le repo, créer `.env` (valeurs via Mohamed), **Node 22**, `npm install`, `npm run dev`
  (§5 cookbook). Lire `yahia-quest-arena/CLAUDE.md`. Prendre un petit **GAP** du [backlog](./90-backlog-remediation.md) → branche → PR (le gate CI te guide).
- **Contenu** : générer/auditer un chapitre via les **skills `content-*`** (Claude Code) → review → `content:build`.
- **Marketing / support** : répondre à 2-3 messages avec les **réponses-types** (kit commercial), publier un **post** du [kit Facebook](./livrables/05-marketing/04-facebook-page-starter-kit.md).

**Semaine 2 — Rythme de croisière**
- **Rituel hebdo** : support (WhatsApp/Messenger) + signalements `content_reports` + coup d'œil KPIs.
- **Chaque matin** : une **issue `nightly-failure`** ouverte ? une **PR** des guards à valider ? (§5 GitHub Actions)
- Tu sais : **déployer = merger une PR** sur `main` · **rollback = Vercel Instant Rollback** · **drill backup mensuel**.

**Les 5 règles d'or (à ne jamais violer)**
1. **Jamais de code rouge sur `main`** (le ruleset le bloque de toute façon).
2. **Migrations DB : jamais à la main** — elles s'auto-appliquent au merge (`db-migrate-prod.yml`,
   backup + garde + réconciliation horaire) ; un destructif (DROP/REVOKE) part dans un merge
   séparé, après le code (DoD §7).
3. **Aucun secret dans le code** ni dans une variable `VITE_*`.
4. **Public mineur** → prudence données + conformité (§7).
5. **En cas de doute → ce dossier d'abord**, puis Mohamed.

---

## 2. Vision, modèle économique & lancement

**Modèle actuel = 100 % gratuit** (pivot 2026-06-21 « plateforme de référence publique », acté en
base le 2026-07-11) : tout le programme, tous les niveaux, consultation **et** pratique sans
compte ; le compte ajoute la progression (XP, badges, duels, suivi parent). **Aucun tarif, aucun
paiement, aucun vocabulaire « premium/abonnement/payant » dans le produit** (étude 15 D-3).

> 🗄️ **Ancien modèle (dormant, réactivable — étude 01 gelée)** : freemium par parcours — aperçu
> gratuit (quiz + difficulté 1), parcours concours payants avec pack famille, pack one-shot
> « année scolaire » ~69-79 DT catalogue / ~39-49 DT lancement, paiement **manuel d'abord**
> (D17/virement → activation admin), PSP (Konnect/Flouci) au seuil de volume. Détail conservé dans
> `livrables/06-business-model/` (supersédé) — matière première du dégel éventuel.

**Stratégie de lancement** (calée sur l'année scolaire) :
| Phase | Période | Quoi |
|---|---|---|
| Beta gratuite | été 2026 | preuve sociale, liste d'attente, école pilote |
| **Lancement public gratuit** | **rentrée sept 2026** | acquisition, installer l'habitude |
| Croissance/rétention | oct-déc 2026 | usage, contenu, partenariats |
| ~~Bascule premium~~ | ~~jan-mars 2027~~ | **gelée** (pivot gratuité — dégel = décision humaine via l'étude 01) |

**Acquisition** (budget **1000-2000 TND/an** → organique d'abord) :
1. **Partenariats écoles** (canal n°1, commence par l'école des enfants de Mohamed) — playbook prêt.
2. **Facebook** (page + groupes parents, valeur d'abord ; micro-boosts ciblés aux 2 pics).
3. Secondaires : TikTok/Insta (clips), WhatsApp, parrainage « héros fondateurs ».

> Détails complets : `livrables/05-marketing/` (positionnement, acquisition, kit commercial/KPIs) et
> `livrables/06-business-model/` (prix, PSP, business plan 3 ans, KPIs financiers).

---

## 3. Architecture technique

**Stack :** Vite 7 · **TanStack Start** (SSR + routing fichiers + server functions) · React 19 ·
TanStack Query 5 · **Supabase** (Postgres + Auth + RLS) · Tailwind 4 / Radix-shadcn.

**Déploiement :** **push sur la branche `main` = déploiement automatique en production Vercel.**
Le build produit un Worker Cloudflare, repackagé en fonction Node serverless Vercel par
`scripts/build-vercel.mjs` (région **arn1**/Stockholm, co-localisée avec Supabase eu-north-1).

**Dépôt de code :** `github.com/MBeji/yahia-quest-arena` (le code vit dans le sous-dossier
`yahia-quest-arena/` ; le dossier parent contient le pilotage go-live).

**Environnements :**
| Env | URL / cible | Base de données |
|---|---|---|
| **Production** | `https://na9ranal3ab.vercel.app` (→ `na9ranal3ab.tn` à venir) | Supabase PROD |
| **Preview** | URL éphémère par PR | pointe la PROD |
| **TEST** (e2e/charge) | pas d'URL web | Supabase TEST (dédié, jamais la prod) |
| **Local** | `npm run dev` | `.env` → prod (lecture) ; `.env.test` → TEST |

**Règle d'or (DoD §7) :** si un changement de code dépend d'une **migration** Supabase, la migration
doit être **appliquée à la prod AVANT** de merger le code (sinon la prod tourne du code neuf contre
un ancien schéma). Les migrations ne sont PAS appliquées automatiquement.

**Qualité (non négociable) :** chaque changement passe `npm run verify` (lint + typecheck + tests)
avant merge ; un gate CI tourne sur chaque PR. Détails : `yahia-quest-arena/CLAUDE.md` (source de
vérité du code).

> ⚠️ **Le projet est développé avec Claude Code (IA).** Le contenu, le code et les correctifs sont
> produits en grande partie par l'IA, validés/mergés par Mohamed. Voir §5 (qui fait quoi).

---

## 4. 🔑 Accès, comptes & outils

> ⚠️ **Aucun secret (mot de passe, clé, token) n'est écrit dans ce document.** Cette section liste
> **quels accès existent, à quoi ils servent, et OÙ sont les identifiants.** Pour obtenir un accès,
> demande à Mohamed (ou au gestionnaire de mots de passe une fois mis en place — voir §12).

**Référence rapide (identifiants non-secrets)** — à avoir sous la main :
- **Repo** : `github.com/MBeji/yahia-quest-arena`
- **Prod** : **`https://www.na9ranal3ab.tn`** (domaine câblé ; l'apex redirige en 308 vers `www`).
  `https://na9ranal3ab.vercel.app` reste un alias vivant (projet Vercel **`na9ranal3ab`**)
- **Supabase** : PROD ref `fasrenmmrkqjoobrztbp` (eu-north-1) · TEST ref `pqegdnwdtbjtplcthxyp`
- **Sentry** : org `mine-g9` (région EU) · **UptimeRobot** : monitor sur l'URL prod
- **Analytics** : **GA4** `G-H0JRQ7192V` (défaut en dur dans le code) · **PostHog** projet `233369`,
  région **EU** (`https://eu.i.posthog.com`)
- **E-mails** : **Resend**, domaine d'envoi **`send.na9ranal3ab.tn`** (Irlande / eu-west-1),
  expéditeur `no-reply@send.na9ranal3ab.tn`
- **DNS** : la zone `na9ranal3ab.tn` est hébergée chez **TuNet** (`dns1/dns2.tunet.tn`), **pas**
  chez Vercel — tout enregistrement se pose dans l'espace client du registrar
- **Marque / social** : `@na9ranal3ab` (le même partout)
- **Alertes** : envoyées sur l'e-mail de Mohamed (→ à basculer sur un e-mail projet dédié, §12)

| Service | À quoi ça sert | Identifiants connus (non-secrets) | Où sont les secrets | Plan / coût |
|---|---|---|---|---|
| **GitHub** | Code, CI, PRs, secrets CI | dépôt `MBeji/yahia-quest-arena` | compte GitHub de Mohamed | gratuit |
| **Vercel** | Hébergement / déploiement prod | **un seul projet : `na9ranal3ab`** (l'ancien `xpscholars-app` / `yahia-quest-arena.vercel.app` a été **supprimé le 2026-06-15**) | compte Vercel de Mohamed | **Free** (→ Pro/Cloudflare à la 1ʳᵉ vente) |
| **Supabase PROD** | Base de données + Auth de prod | ref `fasrenmmrkqjoobrztbp` (eu-north-1) | dashboard Supabase + `.env` local | **Free** (→ Pro au palier 2) |
| **Supabase TEST** | Base dédiée aux tests e2e/charge | ref `pqegdnwdtbjtplcthxyp` | `.env.test` local + GitHub Secrets | Free |
| **Sentry** | Capture des erreurs prod | org **`mine-g9`**, région **EU** | `VITE_SENTRY_DSN` **posée** en env Vercel (vérifiée dans le bundle prod, 2026-07-27) | gratuit (5k events/mois) |
| **UptimeRobot** | Alerte si le site tombe | monitor sur `na9ranal3ab.vercel.app`, alerte → e-mail de Mohamed | Main API key (chez Mohamed) | gratuit |
| **Google Analytics 4** | Trafic, acquisition, SEO | Measurement ID **`G-H0JRQ7192V`** (public, valeur par défaut en dur dans `analytics.ts`) | aucun secret — l'ID ship dans le bundle | gratuit |
| **PostHog** | Analytics **produit** (funnels, rétention) | projet **`233369`**, région **EU** (`eu.i.posthog.com`) | clé `phc_…` → `VITE_POSTHOG_KEY` en env Vercel | gratuit (1M events/mois) |
| **Domaine** | `na9ranal3ab.tn` | **acheté et câblé** ; zone DNS hébergée chez **TuNet** (`dns1/dns2.tunet.tn`) ; propriété **vérifiée dans Google Search Console** (TXT `google-site-verification` sur l'apex) | espace client registrar (chez Mohamed) | ~12-60 DT/an |
| **Resend** | E-mails transactionnels (auth Supabase) | domaine d'envoi **`send.na9ranal3ab.tn`**, région **Irlande (eu-west-1)**, statut *Verified* | clé API `supabase-auth` → SMTP Supabase | gratuit (3k/mois, 100/j) |
| **Réseaux sociaux** | Acquisition + support | pseudo **`@na9ranal3ab`** (FB en cours, Insta, TikTok) | comptes de Mohamed | gratuit |
| **WhatsApp Business / Messenger** | Support + activation paiement | — | téléphone de Mohamed | gratuit |

**Où vivent les secrets techniques (pour le développeur) :**
- **`.env`** (local, gitignoré) : clés Supabase **PROD** (l'app locale lit la prod en lecture).
- **`.env.test`** (local, gitignoré) : clés Supabase **TEST** (pour les e2e).
- **GitHub → Settings → Secrets → Actions** : `PROD_SUPABASE_DB_URL`, `TEST_SUPABASE_DB_URL`
  (backups), secrets e2e (`TEST_SUPABASE_*`, `E2E_USER_PASSWORD`), et depuis le 2026-07-27
  **`VERCEL_TOKEN` / `VERCEL_PROJECT_ID` / `VERCEL_ORG_ID`** — sans eux `rollback-prod.yml`
  (le kill-switch d'incident) ne peut pas tourner.
- **Vercel → Settings → Environment Variables** (projet `na9ranal3ab`, scope Production) : clés
  Supabase, VAPID (push notifs), `CRON_SECRET`, `VITE_SENTRY_DSN`, `VITE_POSTHOG_KEY`.
  ⚠️ Toute variable `VITE_*` est **inlinée au build** : après l'avoir ajoutée, redéployer **sans
  cache** (« Use existing build cache » décoché), sinon la valeur ne prend pas.
- **Supabase → Authentication → SMTP Settings** : la clé API Resend y vit comme mot de passe SMTP
  (`smtp.resend.com`, port 465, user `resend`). Elle n'existe nulle part ailleurs — Resend ne
  la ré-affiche jamais ; en cas de perte, on en crée une nouvelle et on remplace ici.
- ⚠️ La clé `service_role` Supabase ne doit **jamais** être dans une variable `VITE_*` (elle serait
  embarquée dans le bundle client). Détail : `yahia-quest-arena/docs/environment-variables.md`.

> **À mettre en place (recommandé) :** un **gestionnaire de mots de passe partagé** (Bitwarden,
> 1Password…) pour centraliser proprement tous les accès → voir §12.

---

## 5. Exploitation au quotidien

**Qui fait quoi** (organisation fondateur solo + IA + aide ponctuelle) :
- **Mohamed :** décide, valide, merge les PRs, applique les migrations prod, répond au support,
  fait les achats/réglages dashboard.
- **Claude Code (IA) :** produit le contenu (via des « skills »), le code, les correctifs, les
  brouillons.
- **Automatisation :** backups, CI, alertes (rien à surveiller activement).
- **Aide ponctuelle (le collaborateur) :** visuels/vidéos, relecture de contenu, 1ère réponse
  support, animation des réseaux — voir le RACI détaillé dans `livrables/07-gouvernance/01-exploitation.md`.

**Déploiement & rollback :**
- Déploiement = merger une PR sur `main` (auto-deploy Vercel). Toujours faire un **smoke test**
  après (page charge, connexion, démarrer une quête, dashboard).
- En cas de pépin : **Vercel → Instant Rollback** (re-promouvoir le déploiement précédent, < 1 min).
- Runbook complet : `livrables/04-architecture-prod/runbook-deploiement.md`.

**Sauvegardes (backups) :**
- Automatique : dump de la prod **chaque nuit** (02:30 UTC) → artefact GitHub 14 jours.
- À faire **mensuellement** : un « drill » de restauration (commande dans `91-actions-mohamed.md` E1).
- Runbook : `yahia-quest-arena/docs/backup-restore-runbook.md`.

**Monitoring :**
- **UptimeRobot** : alerte e-mail si le site tombe.
- **Sentry** : erreurs prod (une fois la variable d'env posée).
- **PostHog** : usage/funnel (à créer).

**Support utilisateurs :** **WhatsApp Business** (principal) + **Messenger**. Traiter par lots,
réponse sous 24-48 h annoncée. FAQ + réponses prêtes dans `livrables/05-marketing/03-kit-commercial-kpis.md`.

**Incidents :** sévérités P0-P3 + étapes dans `livrables/07-gouvernance/01-exploitation.md` §3.
Astreinte **best-effort** (pas de 24/7 — acceptable en beta, plateformes managées).

### Commandes utiles (cookbook)

> Toutes les commandes `npm` se lancent **depuis le dossier `yahia-quest-arena/`**.
> ⚠️ **Node 22 requis** (Node 24 casse `@supabase/auth-js`). Gestionnaire de paquets : **npm**
> (le repo a un `bun.lock` mais bun n'est pas requis ; les **deux** lockfiles sont versionnés → après
> avoir ajouté une dépendance, faire `npm install` **et** committer `package-lock.json`, sinon la CI
> casse à `npm ci`).

**Mise en route (1ʳᵉ fois)**
```bash
cp env.example .env      # puis remplir les valeurs (voir docs/environment-variables.md)
npm install
npm run dev              # serveur de dev (SSR) sur http://localhost:8080
```

**Qualité — à passer AVANT de merger** (c'est la Definition of Done)
```bash
npm run verify           # gate rapide : lint + typecheck + tests
npm run ci:verify        # gate complet : + coverage + build/budgets + audit + content QA
npm run format           # prettier --write
```

**Contenu pédagogique** (préférer les skills `content-*` dans Claude Code)
```bash
npm run content:check       # valider le contenu, n'écrit rien
npm run content:build       # compiler content/ -> migrations Supabase (idempotent)
npm run content:qa:strict   # QA contenu (échoue sur warning)
```

**Tests end-to-end** (Playwright — hors gate ; les authentifiés visent le projet **TEST**)
```bash
npm run test:e2e:install    # une fois : installer le navigateur
npm run test:e2e            # parcours publics (chromium + mobile)
npm run e2e:doctor          # vérifier que .env.test est complet
npm run e2e:setup           # provisionner TEST (db push + seed + reset)
npm run test:e2e:auth       # parcours authentifiés
```

**Déploiement & rollback** (pas de commande — c'est du dashboard / git)
- **Déployer** = merger une PR sur `main` → **auto-deploy Vercel** (projet `na9ranal3ab`).
- **Rollback** = Vercel → Deployments → déploiement précédent → **Instant Rollback** (< 1 min).
- ⚠️ Une migration DB dont dépend le code doit être **appliquée en prod AVANT** le merge (DoD §7).

**Exploitation via `gh` CLI** (GitHub CLI ; binaire portable déjà installé sur la machine de Mohamed)
```bash
gh workflow run db-backup.yml -f target=prod -f drill=true   # drill backup mensuel (restauration testée)
gh run list                                                  # derniers runs de workflows
gh run watch <run-id>                                        # suivre un run en direct
gh workflow run nightly.yml                                  # lancer la batterie de tests à la demande
gh pr list                                                   # PR ouvertes (guards nocturnes à valider)
```

### GitHub Actions — workflows & automatisations programmées

> Les workflows vivent dans `.github/workflows/`. La config **Dependabot** est à part :
> `.github/dependabot.yml` (ce n'est **pas** un workflow). Heures en **UTC** (et **Tunis = UTC+1**,
> sans DST). `schedule` et `workflow_run` ne se déclenchent **que depuis `main`** (effectifs une
> fois mergés).

| Workflow (nom) | Fichier | Déclencheur | Rôle |
|---|---|---|---|
| **CI** | `ci.yml` | `pull_request` + `push: main` | Gate rapide : lint, typecheck, tests+coverage, build+budgets, audit deps. **Bloquant** (status check `verify`). |
| **Migration gate** | `migration-gate.yml` | `pull_request` (incl. (un)labeled) | Échoue une PR ajoutant une migration `supabase/migrations/*.sql` sans le label `migration-applied` (appliquer la migration en prod **avant** merge — CLAUDE.md §7). **Bloquant** (`Migration presence`). |
| **DB integration tests (pgTAP)** | `db-tests.yml` | `workflow_call` + `workflow_dispatch` | Suite pgTAP sur un vrai Postgres (Supabase CLI **pin 2.106.0**, **~108 migrations** appliquées — croît avec le contenu). Appelé par le nightly. **Bloquant** (`pgTAP suite`). |
| **E2E** (public) | `e2e.yml` | `workflow_call` + `workflow_dispatch` | Playwright public (chromium + mobile), secrets Supabase factices. **Bloquant** (`e2e`). |
| **E2E (authenticated)** | `e2e-auth.yml` | `workflow_call` + `workflow_dispatch` | Parcours authentifiés sur projet **Supabase TEST** dédié (CLI pin 2.106.0). **Skip gracieux** (vert) si secrets absents ; expose `ran` (true/false). |
| **Nightly tests** | `nightly.yml` | `schedule 0 1 * * *` (01:00 UTC / **02:00 Tunis**) + dispatch | Orchestre E2E public + E2E auth + pgTAP, puis ouvre/maj/ferme une **issue de suivi** `nightly-failure`. |
| **Regression guard** | `regression-guard.yml` | `schedule 0 23 * * *` (23:00 UTC / **00:00 Tunis**) + dispatch | Skill `/regression-guard` (Claude) : réconcilie les tests avec les changements du jour → PR draft de tests + **1 issue par vrai bug**. **Ne push jamais sur `main`.** |
| **Upgrade guard** | `upgrade-guard.yml` | `workflow_run` après **« Nightly tests » réussi** + dispatch | Skill `/upgrade-guard` : montées de stack. Patch/minor en 1 lot → validé (gate+E2E+pgTAP) puis **auto-merge** ; chaque major isolé en PR. |
| **db-backup** | `db-backup.yml` | `schedule 30 2 * * *` (02:30 UTC / **03:30 Tunis**) + dispatch | Dump quotidien PROD (schémas `public`+`auth`) → artefact privé (rétention 14 j). Dispatch avec option **drill** = restauration dans un Postgres 17 jetable + vérif d'invariants. |
| **Dependabot** *(config, pas un workflow)* | `.github/dependabot.yml` | `schedule monthly` | Bumps npm groupés (minor+patch en 1 PR, label `dependencies`) ; majors individuels ; `@types/node` major ignoré (Node 22). |

**Planning nocturne** (ordre chronologique, heure **Tunis**) :

| Heure | Workflow | Effet |
|---|---|---|
| **00:00** | Regression guard | Réconcilie les tests avec les changements du jour → PR draft + issues « vrai bug » (sur une base avant le nightly). |
| **02:00** | Nightly tests | E2E public + E2E auth + pgTAP → met à jour l'issue `nightly-failure` (ouverte si rouge, fermée si vert). |
| **après le Nightly (si vert)** | Upgrade guard | Sur base verte : monte la stack → auto-merge patch/minor, 1 PR par major. |
| **03:30** | db-backup | Dump PROD → artefact 14 j (filet de sécurité, Supabase Free n'a pas de backup géré). |

> En clair : la nuit, le projet **se teste, se répare (tests), se met à jour et se sauvegarde tout
> seul**. Le matin, regarde s'il y a une **issue `nightly-failure`** ouverte ou une **PR**
> (regression-guard / upgrade-guard) à valider. Détail CI/CD : `yahia-quest-arena/docs/ci-cd-and-branch-protection.md`.

**Réutilisation (workflows appelables)** — `e2e.yml`, `e2e-auth.yml` et `db-tests.yml` sont des
**briques `workflow_call`** (input `ref`) :
- appelées par `nightly.yml` sur le ref courant ;
- ré-appelées par `upgrade-guard.yml` en pointant le `ref` sur la branche d'upgrade ; l'auto-merge
  n'a lieu que si E2E public **+** E2E auth (avec `ran == true`) **+** pgTAP sont verts.

**Garde-fous transverses :**
- **Guards Claude (`regression-guard`, `upgrade-guard`)** : nécessitent le secret
  `CLAUDE_CODE_OAUTH_TOKEN` (`claude setup-token`). Absent → **skip gracieux** (reste vert). Un
  parseur dédié (`.github/scripts/check-claude-result.py`) fait échouer le job si Claude a réellement
  erré (évite faux-vert / faux-rouge). Ils **ne pushent jamais sur `main`** et **n'affaiblissent
  jamais le gate**.
- **Concurrence** : groupes `cancel-in-progress` (db-tests / e2e par ref) ; guards et backup en
  `cancel-in-progress: false` (un seul à la fois).
- **Anti-croisement TEST/PROD** : `db-backup` refuse un secret TEST pointant la prod (et inversement)
  en vérifiant le project-ref.

**Secrets du dépôt** (Settings → Secrets → Actions) :

| Secret | Utilisé par | Rôle |
|---|---|---|
| `CLAUDE_CODE_OAUTH_TOKEN` | regression-guard, upgrade-guard | Auth Claude Code Action (abonnement Max, token ~1 an, **à renouveler**). |
| `TEST_SUPABASE_URL` / `TEST_SUPABASE_ANON_KEY` / `TEST_SUPABASE_SERVICE_ROLE_KEY` | e2e-auth (via nightly/upgrade) | Projet **TEST** dédié (jamais la prod) : seed + reset + run. |
| `TEST_SUPABASE_DB_URL` | e2e-auth (option), db-backup | Connexion DB TEST (self-provision / backup test). |
| `E2E_USER_PASSWORD` | e2e-auth | Mot de passe des comptes de test seedés. |
| `PROD_SUPABASE_DB_URL` | db-backup | Connexion DB **PROD** pour le dump nocturne. |
| `GITHUB_TOKEN` (auto) | nightly, guards | Ouvrir/maj issues & PR, auto-merge. |

**Protection de branche `main`** (`.github/rulesets/main-protection.json`) — enforcement **actif** :
pas de suppression, pas de fast-forward (force-push), **PR obligatoire** (0 review requise, dismiss
stale on push), **status checks requis (strict)** : `verify`, `Migration presence`, `pgTAP suite`,
`e2e`. Seul l'`automerge` de l'upgrade-guard merge une PR patch/minor entièrement verte.

---

## 6. Le contenu pédagogique

Le contenu (cours, résumés, quiz, exercices) **n'est pas du SQL écrit à la main** : il vit en
**fichiers** sous `yahia-quest-arena/content/<matière>/<chapitre>/`, validés puis compilés en
migrations Supabase. On l'écrit via des **skills Claude Code** dédiés (un par programme :
école tunisienne, culture générale, langues, muscle-cerveau, QI…).

- Pour générer/auditer du contenu : utiliser les skills (ex. « ajoute un chapitre de maths 9ème »,
  « audite les quiz de culture générale »). Les skills produisent des **fichiers** ; on valide la
  qualité (`content:qa:strict`), on review, puis on build/applique.
- **Notation standard partout** : chiffres occidentaux (0-9), équations LTR — y compris en arabe.
- Détails : `yahia-quest-arena/content/README.md` et `yahia-quest-arena/CLAUDE.md` (§Content pipeline).

---

## 7. Sécurité & conformité

- **Audit sécurité fait (chantier C3) :** aucune faille critique ; RLS sur toutes les tables, RPCs
  privilégiées verrouillées, pas de données financières stockées. Rapport :
  `livrables/03-cybersecurite/`.
- **Headers de sécurité** posés (HSTS, X-Frame-Options, etc.) + **CSP avec nonce par-requête**
  (durcie, plus d'`unsafe-inline`).
- **⚠️ Conformité mineurs (INPDP, loi 2004-63) — À CADRER (GAP-003) :** le public est mineur (11-15
  ans). Avant un lancement à grande échelle / payant : consentement parental, registre des
  traitements, pages légales (CGU + confidentialité). Hébergement des analytics en **UE** (Sentry
  EU, PostHog EU) déjà choisi pour ça.
- **Statut juridique pour encaisser — À OUVRIR :** **auto-entrepreneur** (le plus simple en TN)
  avant la bascule premium. La beta gratuite ne le nécessite pas.

### Plan conformité « données de mineurs » (INPDP) — à dérouler avant l'échelle / le payant

> ⚠️ **Ce n'est PAS un avis juridique.** Le public est **mineur (11-15 ans)** = sujet sensible.
> **Faire valider par un juriste / DPO tunisien** (INPDP, loi organique **2004-63**) avant toute
> collecte à grande échelle et avant la première vente. Ne pas improviser sur les mineurs.

**Contexte** : la loi 2004-63 protège les données personnelles ; traiter celles d'un **mineur**
requiert en principe le **consentement du représentant légal (parent)**. L'**INPDP** est l'autorité ;
certains traitements peuvent nécessiter une **déclaration / autorisation**.

**Déjà en notre faveur** : données **minimisées** (pas de données sensibles ni financières stockées)
· analytics & erreurs hébergés en **UE** (Sentry EU, PostHog EU — choix délibéré) · **aucune revente**.

**Ce qui manque** :

| Élément | Quand | Note |
|---|---|---|
| **Pages légales** : CGU + Politique de confidentialité (+ mentions légales) | avant lancement public | Claude peut les drafter ; à faire **relire par un juriste** |
| **Consentement parental** au signup (case « je suis le parent et j'accepte ») | avant lancement public | aujourd'hui le signup ne recueille **ni âge ni consentement** (GAP-003) |
| **Registre des traitements** (quelles données, pourquoi, durée, qui y accède) | avant l'échelle | document interne |
| **Déclaration INPDP** (si requise) | avant le payant | à confirmer avec le juriste |
| **Revue juridique** (juriste / DPO TN) | avant le payant | **LE** prérequis |

**Par phase** :
- **Beta gratuite** (été→rentrée) : minimum = **CGU + confidentialité publiées** + **case de
  consentement parental** au signup → collecte propre dès le départ.
- **Lancement payant** (jan 2027) : conformité complète (registre, déclaration INPDP si requise,
  revue juridique), couplée à l'ouverture du statut auto-entrepreneur.

**Décisions Mohamed attendues** : (1) consulter un juriste/DPO ? (**recommandé**) ; (2) modèle de
consentement ; (3) statut juridique. → suivi : C3 §4 · GAP-003 · GAP-024 (pages légales).

---

## 8. Roadmap & état d'avancement

Le passage POC → production est piloté par un **programme go-live** en 7 chantiers (voir
`00-MASTER-PLAN.md`). État au 2026-06-14 :

| Chantier | État |
|---|---|
| C1 Audit fonctionnel · C2 Technique · C3 Sécurité | 🟢 terminés |
| C5 Marketing · C6 Monétisation · C7 Gouvernance | 🟢 terminés |
| C4 Architecture prod | 🟡 ~98 % au 2026-07-27 — domaine câblé, ruleset actif, Sentry + GA4 + PostHog en place, SMTP Resend prouvé, secrets du kill-switch posés. **Restent** : le test à blanc de `rollback-prod.yml`, les pages légales et la conformité INPDP (§7) |

**Go/No-Go à 2 portes** (détail : `livrables/07-gouvernance/02-roadmap-pilotage-gonogo.md`) :
- **Porte 1 — beta gratuite (cible rentrée sept 2026)** : infra + monitoring + pages légales + domaine.
- **Porte 2 — lancement payant** : ⏸️ **gelée** (pivot gratuité 2026-06-21 ; dégel = décision
  humaine, véhicule = étude 01). Ses prérequis (auto-entrepreneur, prix, PSP) sont suspendus ;
  la **conformité mineurs (INPDP)** reste due pour le lancement gratuit.

**Roadmap produit 12 mois :** beta → lancement gratuit (rentrée) → croissance/usage →
scale + élargissement (langues, culture G, lycée) + B2B écoles (année 2). (~~premium au pic
concours jan-mars~~ : gelé.)

**Backlog technique :** `90-backlog-remediation.md` (les « GAP-NNN »).
**Tâches en attente côté Mohamed :** `91-actions-mohamed.md` (la liste à dérouler).

---

## 9. Décisions clés (et pourquoi)

| Décision | Choix | Pourquoi |
|---|---|---|
| **Marque** | Na9ra Nal3ab (نقرا نلعب) | Le nom = la proposition de valeur, en derja ; double cible ; 100 % ownable (.tn + .com) |
| **Infra** | Rester Vercel + Supabase | Éprouvé par les tests de charge sur tier gratuit ; lock-in faible |
| **Domaine** | `na9ranal3ab.tn` (principal) | Confiance locale (.tn) + corrige un faux-positif réputation de l'URL `*.vercel.app` |
| **Modèle** | Freemium par parcours | Déjà construit ; aperçu gratuit = essai sans risque |
| **Facturation** | Pack one-shot « année » | Aligné concours + habitudes de paiement TN (paiement unique) |
| **Paiement** | Manuel d'abord (D17) | Valider la disposition à payer avant le lot technique PSP |
| **Lancement** | Gratuit d'abord (été→rentrée), payant au pic concours (jan) | Bâtir l'usage et la preuve avant de monétiser |
| **Monitoring/analytics** | Sentry + UptimeRobot + **GA4 et PostHog en parallèle**, **région EU** | 100 % gratuit + conforme mineurs (UE). GA4 répond « combien de trafic, d'où » (acquisition, SEO) ; PostHog répond aux questions que GA4 ne sait pas traiter (funnels d'activation, rétention par cohorte). Les deux partagent un point d'appel unique côté code, chacun avec sa propre garde — couper l'un ne rend jamais l'autre muet |
| **Analytics : pas de SDK, pas de session replay** | Envoi maison en `fetch` direct (2026-07-27) | Le SDK `posthog-js` coûte ~60 kB pour un plafond de bundle à 450 (437 utilisés) ; et **enregistrer l'écran de mineurs est une décision de protection des données**, pas une case à cocher — elle suppose la politique de confidentialité qui n'existe pas encore (GAP-024) et le cadrage INPDP (GAP-003) |
| **E-mails transactionnels** | Resend, envoi depuis le **sous-domaine** `send.na9ranal3ab.tn` | Le SMTP intégré de Supabase est bridé à quelques mails/heure — inutilisable dès le recrutement des testeurs. Le sous-domaine isole la réputation d'envoi et laisse intacts les MX Ooredoo de la racine, qui reçoivent le courrier du domaine |
| **Statut légal** | Auto-entrepreneur (à ouvrir) | Le plus simple pour facturer/encaisser en TN |

> Toutes les décisions sont tracées dans les tables « Décisions » de chaque chantier
> (`0X-*.md`) et le journal du `00-MASTER-PLAN.md`.

---

## 10. Glossaire

- **Parcours** : la piste d'apprentissage où l'élève est inscrit (couple thème + niveau). Kinds :
  concours / scolaire / libre — **tous gratuits en phase actuelle** (le flag premium est dormant).
- **Concours** : examens nationaux d'entrée au lycée pilote (9ème) / collège pilote (6ème) — places
  très rares → forte pression ; dans le produit, ce sont des **jalons**, plus une offre payante.
- **Entitlement** : le « droit d'accès » à un parcours premium (source : achat / beta / cadeau /
  famille) — machinerie **dormante** en phase gratuite.
- **Pack famille** : un parent équipe plusieurs enfants (remises) — dormant, comme le premium.
- **Aperçu (preview) gratuit** : quiz de compréhension + exercices de difficulté 1 — l'ex-essai
  gratuit du modèle freemium (sans objet tant que tout est gratuit).
- **Quête** : un exercice (mission QCM). **XP** : points gagnés. **Donjon** : mode boss chronométré
  (verrous de progression uniquement — n'est plus un perk premium depuis `20260711100000`).
- **Derja** : dialecte tunisien. **Arabizi** : écriture du derja avec des chiffres (9=ق, 3=ع).
- **DoD** : « Definition of Done » — les règles qualité non négociables (voir CLAUDE.md).
- **GAP-NNN** : un élément du backlog technique (`90-backlog-remediation.md`).
- **D17** : service de paiement mobile de La Poste tunisienne (très répandu).
- **INPDP** : Instance Nationale de Protection des Données Personnelles (Tunisie).
- **ATI** : Agence Tunisienne d'Internet (gère les domaines `.tn`).
- **INNORPI** : l'institut tunisien pour la propriété industrielle (marques).

---

## 11. Documents détaillés & ressources

**Pilotage (dossier `go-live/`) :**
- `00-MASTER-PLAN.md` — tableau de bord du programme + protocole + journal.
- `90-backlog-remediation.md` — backlog technique (GAP-NNN).
- `91-actions-mohamed.md` — **les actions concrètes en attente**.
- `0X-*.md` (01 à 07) — un fichier de pilotage par chantier.
- `livrables/0X-*/` — les livrables détaillés (architecture, marketing, business model, gouvernance…).

**Code (dossier `yahia-quest-arena/`) :**
- `CLAUDE.md` — **source de vérité du code** (stack, commandes, conventions, DoD, pièges).
- `ARCHITECTURE.md` — architecture approfondie.
- `docs/` — politiques par sujet : `environment-variables.md`, `backup-restore-runbook.md`,
  `ci-cd-and-branch-protection.md`, `release-tagging-policy.md`, `logging-standard.md`,
  `xss-rendering-policy.md`, `dependency-maintenance.md`.
- `content/README.md` — comment écrire du contenu.
- `e2e/README.md` — comment lancer les tests end-to-end.

---

## 12. À compléter au fil de l'eau

Cases à cocher quand l'info devient disponible / l'action est faite :

- [ ] **Gestionnaire de mots de passe partagé** créé (Bitwarden/1Password) → y centraliser tous les
      accès du §4, puis remplacer « chez Mohamed » par « dans le coffre ».
- [x] **Domaine `na9ranal3ab.tn`** acheté + branché (DNS/SSL/Auth) — `www` sert l'app en 200,
      l'apex redirige, Site URL + Redirect URLs Supabase alignés (2026-07-27). §4 à jour.
- [ ] **Pseudos sociaux** `@na9ranal3ab` réservés (FB ✅ / Insta / TikTok) → cocher.
- [x] **PostHog** créé (Cloud EU, projet `233369`) — intégration mergée (PR #639), clé
      `VITE_POSTHOG_KEY` posée en env Vercel (2026-07-27).
- [x] **Sentry** activé en prod — DSN posé et **vérifié dans le bundle prod** (2026-07-27).
- [x] **SMTP transactionnel** (Resend, `send.na9ranal3ab.tn`, EU) branché sur Supabase Auth et
      **prouvé de bout en bout** (2026-07-27). Reste à traduire les gabarits d'e-mail en français.
- [x] **Gabarits d'e-mail Supabase en français** (confirmation, mot de passe, changement
      d'adresse) — rédigés et posés le 2026-07-27.
- [x] **Dump prod du baseline archivé hors GitHub** — `baseline/2026-07-25-versionstable` reposait
      sur un artefact GitHub qui **expirait le 2026-08-08** ; copie récupérée le 2026-07-27 dans
      `YahiaAcademy/_baselines/db-prod-20260725-185313/` (5,5 Mo, en-tête `PGDMP` vérifié).
      ⚠️ **Ce dossier est sur le PC de Mohamed et n'est pas sauvegardé** : en faire une copie hors
      machine (disque externe / drive) pour que l'axe « données » du point de retour existe
      vraiment.
- [ ] **Statut auto-entrepreneur** ouvert → noter le n° fiscal / modalités de facturation.
- [ ] **Pages légales** (CGU + confidentialité) publiées → lier ici.
- [ ] **E-mail projet dédié** (ex. `contact@na9ranal3ab.tn`) créé → remplacer l'e-mail perso dans
      les alertes/monitoring.
- [ ] **Compte bancaire / moyen d'encaissement** (D17, RIB) documenté pour la facturation.
- [ ] **Contacts utiles** (registrar, comptable, école pilote…) listés ci-dessous.

**Contacts utiles** *(à remplir)* :
| Rôle | Nom | Coordonnées |
|---|---|---|
| Registrar domaine (.tn) | _à compléter_ | _ _ |
| Comptable / conseil auto-entrepreneur | _à compléter_ | _ _ |
| École pilote (contact) | _à compléter_ | _ _ |

---

## 🗒️ Changelog du document
| Date | Modif |
|------|-------|
| 2026-06-14 | Création du dossier de passation (structure complète + état au 14/06). |
| 2026-06-16 | §5 : ajout complet « GitHub Actions — workflows & automatisations » (vue d'ensemble + planning nocturne + réutilisation `workflow_call` + garde-fous transverses + table des secrets + protection de branche `main`), **vérifié contre `.github/workflows/` et le ruleset** (2 corrections au passage : 108 migrations, dependabot = config). §4 : ancien projet Vercel marqué supprimé. §5 : ajout d'un bloc **« Commandes utiles (cookbook) »** (setup, qualité, contenu, e2e, déploiement/rollback, ops `gh`), scripts vérifiés contre `package.json`. §1 : guide **« Par où commencer (ta première semaine) »** (onboarding J1→S2 + 5 règles d'or). §4 : « référence rapide » des identifiants non-secrets. §7 : **plan conformité mineurs/INPDP** (avec phases + décisions attendues, avertissement « pas un avis juridique »). |
| 2026-07-11 | **Réalignement post-pivot gratuité** (passe de rationalisation) : bannière pivot en tête ; §1 fin + §2 (modèle 100 % gratuit, ancien freemium encadré « dormant/réactivable ») ; §8 Porte 2 gelée + roadmap sans « premium jan-mars » ; glossaire (parcours/concours/entitlement/pack famille/preview/donjon) requalifié « dormant ». Topo central : `yahia-quest-arena/STATUS.md`. |
| 2026-07-27 | **Session « mise en prod sérieuse » — C4 quasiment soldé, et trois affirmations du dossier étaient fausses.** ① §4 refondu : l'URL de prod est **`https://www.na9ranal3ab.tn`** (le domaine était câblé depuis un moment, la doc le disait « non branché »), la propriété **Search Console était déjà vérifiée** (TXT sur l'apex), et le **DSN Sentry était déjà posé** (constaté dans le bundle prod, pas dans un dashboard). Leçon de méthode consignée : une action faite hors du repo n'y laisse aucune trace — on la **sonde** (DNS, bundle, API GitHub), on ne la déduit pas de la doc. ② **Analytics** : GA4 (`G-H0JRQ7192V`) existait déjà et manquait au §4 ; **PostHog** (projet `233369`, EU) ajouté **en complément** — intégration maison sans SDK (budget bundle : 437 kB / 450), sans autocapture ni **session replay** (décision de protection des données pour un public mineur), aucune PII, PR #639. ③ **E-mails transactionnels** : confirmations d'e-mail **activées** côté Supabase (elles étaient désactivées — `mailer_autoconfirm=true`, donc aucune adresse n'était prouvée), puis **Resend** branché (domaine d'envoi `send.na9ranal3ab.tn`, Irlande, DKIM/SPF/return-path vérifiés au DNS) et chaîne **prouvée de bout en bout**. Gabarits FR rédigés, à coller. ④ **Kill-switch prod** : les secrets `VERCEL_*` manquaient — `rollback-prod.yml` était inopérant depuis son écriture ; posés. ⑤ **Politique d'exécution** (PR #640) : un agent peut désormais déclencher `rollback-prod`, `db-backup` et `db-tests`, nommés un par un ; `db-migrate-prod`, `e2e-auth` et `release` sont refusés **avec motif**. ⑥ Reliquat noté : le test à blanc du kill-switch n'a pas encore été joué. |
