# Dossier d'architecture de production — yahia-quest-arena

> Livrable S1 du chantier [04](../../04-architecture-prod-deploiement.md). Date : 2026-06-12.
> Inputs Mohamed : Vercel **Free** + Supabase **Free**, prod = `https://yahia-quest-arena.vercel.app/`,
> pas de domaine, budget « limité au démarrage, scalable si l'usage monte ».
> Les prix cités sont ceux connus à date — **à re-vérifier au moment de chaque achat**.

## 1. Décision d'infrastructure (D1 — actée)

**On reste sur Vercel + Supabase managé.** Critères :
- **Éprouvé par la mesure** : les tests de charge C2/S2 ont tenu les cibles beta avec 9–17× de
  marge… **sur un projet Supabase Free** (le projet TEST est du même tier que la prod actuelle).
  Le palier gratuit porte donc la beta — fait mesuré, pas supposé.
- **Zéro migration risquée avant lancement** ; la seule contrainte dure est contractuelle
  (ToS Vercel Hobby, §3) et se traite au moment d'ouvrir les ventes.
- **Lock-in faible** : le build est portable (et le devient encore plus avec Nitro, §4) ; la donnée
  est du Postgres standard (`pg_dump` suffit à sortir).

### Architecture actuelle (état mesuré, C2)

```
Élève (Tunisie)
   │ HTTPS
   ▼
Vercel CDN ── assets hashés (Cache-Control: immutable) + headers sécu statiques (HSTS/XFO/CSP)
   │
   ▼
Fonction serverless SSR — Node 22, région épinglée arn1 (Stockholm), maxDuration 30 s
   build : Vite (cible CF Worker) → re-packagé par scripts/build-vercel.mjs (adaptateur custom)
   39 server fns · middleware auth JWT · logger JSON
   │ PostgREST / RPC (intra-région)
   ▼
Supabase eu-north-1 (Stockholm) — Postgres + RLS + ~47 fn SQL (SECURITY DEFINER) · Auth · Storage
```

Points forts : co-localisation fonction↔DB (un seul saut intra-région) ; gates server-authoritative.
Points faibles connus : adaptateur de build custom (SPOF logiciel, §4), mono-région loin de la
Tunisie (TTFB à mesurer, GAP-029), CSP `unsafe-inline` (§6), aucun backup géré en Free (§7).

## 2. Modèle de coûts par paliers (D2 amendée — « démarrage ~0 €, scalable »)

| Palier | Déclencheur | Stack | Coût/mois |
|---|---|---|---|
| **0 — Beta gratuite** *(maintenant)* | — | Vercel Free + Supabase Free + Sentry/UptimeRobot/PostHog free + **backups DIY** (§7) | **~0 $** |
| **1 — Ouverture des ventes** | 1er parcours vendu (même par téléphone) | Quitter Vercel Hobby (ToS) : **option A** Vercel Pro **ou option B** Cloudflare natif (§3) + **domaine** (~12 $/an) + SMTP Resend free | **0–20 $** selon A/B |
| **2 — Données clients réelles** | Premiers payants actifs OU DB > ~350 Mo OU besoin de backups gérés | + **Supabase Pro** (backups quotidiens 7 j, pas de pause, ressources stables) | **25–45 $** |
| **3 — Échelle** | ~1 000+ actifs OU p95 submit > 600 ms soutenu (seuil issu de C2/GAP-027) | + compute add-on Supabase, PITR si RPO < 24 h exigé, cache HTTP (C2 §3.2.5) | **~60–120 $** |

**Limites du palier 0 à surveiller** (alertes à poser en S2) : Supabase Free = 500 Mo DB / 5 Go
egress/mois / **pas de backup géré** / pause après ~7 j d'inactivité (improbable avec du trafic
réel, mais à savoir pour les périodes mortes) ; Vercel Free = 100 Go bande passante/mois.
Les déclencheurs de palier sont **mesurables** — pas d'upgrade au feeling.

## 3. Le point dur du palier 1 : ToS Vercel Hobby (décision à prendre AVANT la 1ère vente)

Le plan Hobby est contractuellement réservé à un **usage non commercial**. Vendre les parcours
premium (même paiement hors-ligne par téléphone) sur Hobby = violation des ToS → risque de
suspension du site au pire moment. Deux options, **décision via PoC (§4)** :

| | Option A — Vercel Pro | Option B — Cloudflare natif |
|---|---|---|
| Coût | **20 $/mois** | **0 $** (Workers Free, usage commercial autorisé, 100 k req/jour) ou **5 $/mois** (Paid) |
| Effort | Zéro (upgrade du plan) | Migration build Nitro (§4) — PoC requis |
| Latence TN | inchangée (arn1) | Edge mondial (PoP Tunis) pour le statique/SSR ; Smart Placement rapproche l'exécution de la DB |
| Risque | Aucun | Plateforme à re-valider (e2e + charge ciblée) |

**Recommandation** : lancer le PoC Nitro (§4) maintenant que la beta tourne ; si le PoC est vert
avant l'ouverture des ventes → **option B (0–5 $/mois)**, sinon → **option A (20 $/mois)** en
attendant, ré-arbitrage ensuite. Dans les deux cas le domaine devient nécessaire (e-mails DKIM).

## 4. Trajectoire du pipeline de build (GAP-007) — finding S1

Recon décisive sur `@lovable.dev/vite-tanstack-config` :

- **1.7.0 (actuel)** : embarque `@cloudflare/vite-plugin` → le build prod EST un Worker, re-packagé
  pour Vercel par l'adaptateur maison `build-vercel.mjs` (~180 lignes, SPOF identifié en C2).
- **2.4.0 (latest)** : **ne dépend plus du tout du plugin Cloudflare** — la 2.x est bâtie sur
  **Nitro** (peer `nitro ≥ 3.x`, `vite 5→8`). Or Nitro a des **presets de déploiement natifs**
  pour Vercel (Build Output API généré proprement) **et** Cloudflare.

**Conséquence** : quelle que soit la plateforme choisie au palier 1, la cible technique est la même —
**passer sur le pipeline Nitro et supprimer `build-vercel.mjs` + `wrangler.jsonc`**. Deux chemins :

1. **Upgrade lovable 2.4** : garde le méta-plugin, gagne Nitro + compat Vite 8 (recoupe le lot
   « Vite 8 » de D2/C2).
2. **Sortie de Lovable** (TanStack Start natif : `tanstackStart` + `viteReact` + `tailwindcss` +
   `tsConfigPaths` + preset Nitro directement) : un plugin de moins, plus de dépendance à un
   éditeur tiers — **aligné avec ton objectif « zéro Lovable »**. À peine plus de travail que (1)
   (l'injection `VITE_*`, le tagger dev et la détection sandbox de lovable sont à remplacer/jeter).

**Recommandation : viser (2) directement**, via un PoC time-boxé sur branche. Critères de go avant
launch : `ci:verify` vert + budgets bundle tenus + e2e public vert + `.vercel/output` (ou
`dist` Workers) inspecté + un déploiement preview testé. Sinon : post-launch, sans urgence (le
pipeline actuel marche — il est juste fragile aux majeures).

**Résultat du PoC time-boxé (S2, 2026-06-12)** — recon mécanique concluante, migration re-scopée :
- La version **actuelle** de TanStack Start (plugin-core 1.171) n'a **aucun preset de déploiement**
  (zéro référence vercel/nitro dans le toolchain installé) : le plugin émet `dist/server` (handler
  fetch générique) et l'empaquetage est à la charge de l'hôte. L'adaptateur custom n'était donc pas
  un caprice — c'était le seul moyen en 1.x/lovable 1.7.
- Le chemin (2) « zéro Lovable » **sans** Nitro reproduirait l'adaptateur actuel → aucun gain.
  La sortie réelle passe par **Nitro**, donc en pratique par l'upgrade **lovable 2.4** d'abord
  (qui compose Start + Nitro + presets), la dé-Lovable-isation complète venant ensuite.
- Travail re-scopé (lot dédié ~0,5-1 j, PAS un toggle) : nitro 3 beta à installer, API de config
  2.x à adopter (sans README publié — introspection des types), **portage du wrapper d'erreurs
  500** (`src/server.ts` — Nitro est basé h3, le contrat change), injection env `VITE_*`,
  préservation des manualChunks/budgets, puis critères de go ci-dessus.
- Bonus confirmé : peer `vite >=5 <9` → ce lot **débloque aussi Vite 8** (PR dependabot différée).

## 5. Environnements & releases

- **Environnements** : prod (Vercel, auto-deploy `main`) + TEST Supabase (e2e/charge) + **previews
  Vercel par PR** (à activer pour les PRs — gratuit). **Pas de staging** au lancement : la beta
  EST le staging ; un staging dédié se justifiera avec les paiements en ligne (C6).
- **Rollback** : code = « Instant Rollback » Vercel (re-pointer le déploiement précédent, < 1 min) ;
  DB = politique **migrations additives d'abord** (déjà pratiquée : déploiements 3-temps C3/GAP-021).
  Une migration destructive ne part qu'avec son plan de retour écrit.
- **Releases** : tag `v1.0.0` au go-live + tags sémantiques ensuite (GAP-028, politique déjà
  écrite dans `docs/release-tagging-policy.md`) ; garde-fou `migration-gate.yml` déjà en CI.

## 6. Design CSP nonce (GAP-022) — implémentation en S2

Aujourd'hui la CSP est **statique** (routing Vercel, `script-src 'unsafe-inline'` — TODO review #6)
car TanStack Start émet des scripts d'hydratation inline. Design retenu :

1. `src/server.ts` (notre wrapper fetch, déjà en place) génère un **nonce par requête**
   (`crypto.randomUUID()`), le passe au rendu, et pose le header
   `Content-Security-Policy: script-src 'self' 'nonce-<n>'` **sur les réponses HTML uniquement**.
2. Le nonce doit être porté par les `<script>` inline émis par TanStack Start — vérifier le support
   `nonce` du router/Start (option de rendu) ; c'est **le** point de risque de l'implémentation.
3. La CSP statique est alors retirée du `config.json` pour les routes HTML (les autres headers
   statiques restent) — sinon double header CSP contradictoire.
4. Validation : tests e2e public (hydratation OK, zéro violation console) + en-tête vérifié.

Si le support nonce de TanStack Start s'avère incomplet : fallback `'strict-dynamic'` + hash des
scripts d'amorçage, et on documente. À coder en S2 (DoD complet).

## 7. Backups palier 0 (GAP-004) — design « DIY gratuit » (implémentation S2)

Supabase Free n'a **aucun backup géré**. Tant que le palier 2 n'est pas déclenché :

- **Workflow GitHub Actions planifié** (quotidien, `cron`) : `pg_dump` du Postgres prod (secret
  `PROD_SUPABASE_DB_URL` à ajouter par Mohamed — *connection pooler en mode session*), compressé,
  déposé en **artefact privé** (rétention 30 j) — coût 0.
- **Drill de restauration** : restaurer un dump sur le projet TEST, documenter la procédure
  (`runbook-backup-restore.md`), vérifier 3 invariants (comptes, contenus, entitlements).
- RPO ≈ 24 h, RTO ≈ 1 h — acceptable pour une beta gratuite ; **dès le palier 2, Supabase Pro
  prend le relais** (backups gérés 7 j) et ce workflow devient une ceinture-bretelles.

## 8. Reste à faire — état au 2026-06-12

**Conception du chantier 04 = 100 %** (S1 décisions/dossier · S2 exploitation outillée · S3
runbook + Go/No-Go). Ce qui reste est de l'**exécution**, pas de la conception :

- **S2 (livrée)** : workflow backups + drill (✅ mergé, drill à relancer après secrets posés),
  mesures TTFB TN (✅ mono-région validée), checklists exploitation/auth (✅ écrites). Monitoring
  Sentry/PostHog = **lots code** après réception des clés Mohamed. CSP nonce = lot dédié (§6).
- **S3 (livrée)** : [runbook-deploiement.md](./runbook-deploiement.md) (déploiement & rollback) +
  [checklist-go-no-go.md](./checklist-go-no-go.md) (grille binaire + coûts + plan tag v1.0.0).
- **Lots code restants** (DoD complet, hors « conception ») : Sentry+PostHog · CSP nonce (§6) ·
  **migration lovable 2.4/Nitro** (§4, ~0,5-1 j, débloque Vite 8) — à planifier avant le palier 1.
- **Actions Mohamed** (dashboard/comptes/achat) : secrets ✅, puis UptimeRobot, checklist auth,
  ruleset `main`, comptes Sentry/PostHog, domaine (avec C5). Détail ordonné : checklist Go/No-Go §E.
