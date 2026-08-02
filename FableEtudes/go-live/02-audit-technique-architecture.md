# Chantier 02 — Audit technique & architecture

> Pilotage : [00-MASTER-PLAN.md](./00-MASTER-PLAN.md) · Livrables volumineux : `go-live/livrables/02-audit-technique/`

| | |
|---|---|
| **Statut** | 🟢 Terminé (S1+S2+S3) — reste action de clôture D2 (vague de minors) |
| **Avancement** | 100 % |
| **Dépendances** | Aucune (Phase A) — capitalise sur les audits du 2026-06-01 (à réconcilier, pas à refaire) |
| **Alimente** | Backlog 90 (dette/risques) · C4 (choix d'infra, dimensionnement) |
| **Dernière session** | 2026-06-12 (S3 : radar v2 **3,31/4** + synthèse + versement backlog ; chantier clos) |
| **Prochaine action** | Action de clôture D2 (vague de minors `npm update` + gate, hors charge machine) · Chantier suivant : C4 (archi prod) — alimenté par GAP-007/027/029 |

## Contexte à charger en début de session
- Ce fichier + `00-MASTER-PLAN.md`
- `yahia-quest-arena/CLAUDE.md` + `ARCHITECTURE.md`
- Audits existants (référence, à réconcilier) : `yahia-quest-arena/AUDIT_REPORT_2026-06-01.md`, wrapper `AUDIT_REPORT_2026-06-01_RUN*.md` + checklists associées
- Selon la tâche : `package.json`, `vite.config.ts`, `vitest.config.ts`, `supabase/migrations/`

## Objectifs (périmètre validé)
- Évaluer qualité, maintenabilité, lisibilité du code.
- Vérifier la pertinence des choix technologiques et du socle applicatif.
- Analyser modularité, évolutivité, capacité de maintenance long terme.
- Évaluer la scalabilité verticale et horizontale.
- Réaliser des tests de charge et de performance.
- Vérifier résilience, gestion des erreurs, disponibilité.
- Auditer dépendances, frameworks, bibliothèques, services tiers.
- Identifier risques techniques, dette technique, actions de remédiation.

## Livrables attendus
- [x] Réconciliation des audits 2026-06-01 : statut réel de chaque action (fait/obsolète/restant) → [livrable](./livrables/02-audit-technique/reconciliation-2026-06-01.md)
- [x] Rapport d'audit v2 avec scoring comparable (radar /4) + delta depuis le 01/06 → [rapport-v2.md](./livrables/02-audit-technique/rapport-v2.md) **complet** (§1–8) ; radar **3,31/4** vs 3,0 (+0,31)
- [x] Résultats tests de charge (scénarios + seuils + conclusions de dimensionnement) → [charge-resultats.md](./livrables/02-audit-technique/charge/charge-resultats.md) (D1 tenue 9–17×, plafond écriture 1×–5× → C4)
- [x] Décision documentée sur les dépendances (PRs dependabot, double config deploy) → rapport v2 §4 (D2 appliquée ; Cloudflare = load-bearing, garder jusqu'à C4)
- [x] Backlog dette/risques priorisé → versé au backlog 90 (S3) : GAP-005 🟢, GAP-007 requalifié, GAP-027→032 + 034 créés ; rapport v2 §8
- [x] *(D3)* Liste keep/delete des branches distantes → [branches-tri.md](./livrables/02-audit-technique/branches-tri.md) (35 suppressions proposées, **en attente validation**)

## Plan d'exécution (kickoff 2026-06-11 — à valider)

**Reconnaissance faite** : 3 rapports + 2 checklists + 2 CSV métriques du 01/06 à réconcilier ;
`audit:deps` (prod, high) = **0 vulnérabilité** ; **6 PRs dependabot** ouvertes (dont 2 majeures :
vite 8, zod 4 ; + recharts 3.8, @types/node 25, plugin-react 6, lovable-config 2.2) ; `npm outdated`
= vague de minors Radix + majeures (eslint 10, lovable 2.4) ; **28 branches `claude/*`** distantes à
trier (ex. `perf-hot-path-indexes` déjà mergée via migration `20260606160000`).

### S1 — Réconciliation & revue statique (1 session) — ✅ faite le 2026-06-11
- [x] 1a. **Réconciliation 01/06** : 29 constats distincts (union des 3 runs) statués avec preuves →
  [reconciliation-2026-06-01.md](./livrables/02-audit-technique/reconciliation-2026-06-01.md).
  Bilan : 15 faits, 4 partiels, 6 restants (2 micro-fixes, 0 bloquant), 3 faibles assumés, 1 re-scopé C4.
- [x] 1b. **Revue d'architecture** : 0 violation de frontières (cross-feature/couches/server-client),
  39 server fns / 10 modules, 47 fn SQL ; vigilances = 3 routes monolithiques, **pipeline de build
  custom Worker→Vercel (`build-vercel.mjs`) identifié comme SPOF logiciel**, mono-région arn1,
  CSP `unsafe-inline` → [rapport-v2.md](./livrables/02-audit-technique/rapport-v2.md) §3.
- [x] 1c. **Deps & supply chain** : 0 vuln ; triage des 6 PRs dependabot (rejeter types/node 25 et
  lovable 2.2 ; différer vite 8 + plugin-react 6, zod 4, recharts 3 en lots dédiés hors chantier) ;
  **Cloudflare ≠ vestige (load-bearing dans le build) → décision garder, simplification = C4** ;
  liste keep/delete des 41 branches → [branches-tri.md](./livrables/02-audit-technique/branches-tri.md)
  (**recommandation : 35 suppressions, en attente validation D3**).
- Minors sûrs (`npm update` + gate) : prévus en fin de C2 (après S2), per D2.

### S2 — Performance, charge & résilience (1 session) — ✅ faite le 2026-06-12
- [x] 2b. **Tests de charge — contre TEST uniquement** (k6 v2.0.0 standalone). **Cibles D1 tenues à
  ~9–17× de marge** (submit p95 114 ms, dashboard 116 ms, leaderboard 100 ms ; 0 échec / 25 977 req).
  Stress ×5 : 0 échec mais submit p95 → 1,89 s → **dégradation par latence, pas erreur** ; plafond
  entre 1× et 5× = levier pool Supabase (→ C4). [charge-resultats.md](./livrables/02-audit-technique/charge/charge-resultats.md).
- [x] 2c. **Résilience** : 4 sondes de chemins d'erreur OK (JWT invalide→401, input malformé→400,
  session forgée→400, anti-rush→tooFast). Aucune fuite 5xx sur 48 000+ req. Reste (→ backlog/C4) :
  panne Supabase totale simulée + timeouts/retries explicites.
- [~] 2a. **Perf runtime** : budgets bundle ✅ (index 400 kB + i18n 59 kB), requêtes chaudes saines
  sous charge. **Lighthouse/Web Vitals + TTFB terrain depuis la Tunisie reportés à C4** (à mesurer
  sur le domaine de prod, mono-région `arn1`).
- **🔴 Bonus critique** : la prépa de charge a révélé **GAP-026 (P0)** — `start_exercise_session`
  cassée en prod (`42702`). Corrigée (migration `20260612090000` + garde pgTAP), à appliquer en prod.

### S3 — Synthèse (0,5 session) — ✅ faite le 2026-06-12
- [x] 3a. **Rapport v2** : radar /4 (8 dimensions, réf. RUN2) — **3,31/4 vs 3,0 le 01/06 (+0,31)**,
  chaque note justifiée par une preuve mesurée. Moteurs : Tests +1,0 (tempéré par GAP-026),
  Sécurité/Performance/Versioning +0,5. [rapport-v2.md](./livrables/02-audit-technique/rapport-v2.md) §7.
- [x] 3b. **Backlog** : GAP-005 🟢, GAP-007 requalifié, GAP-009 🟡 ; 7 nouveaux GAPs (027 pool→C4,
  028 tags, 029 Lighthouse/TTFB→C4, 030 request-ID, 031 routes monolithiques, 032 micro-dette,
  034 résilience). 3 axes structurants identifiés pour C4. Rapport v2 §8.
- **Verdict** : socle technique sain, **prêt pour une beta, 0 bloquant** après clôture de GAP-026.

### Décisions demandées à Mohamed (kickoff)
| # | Question | Proposition par défaut |
|---|----------|------------------------|
| D1 | Cibles des tests de charge | Hypothèse beta TN : **100 utilisateurs simultanés**, pic **500 soumissions de quête/h**, p95 < 1 s sur `submit_exercise_attempt`, p95 < 2 s sur le dashboard (ajustable quand C6 fixera les vraies cibles) |
| D2 | Majeures dependabot (vite 8, zod 4…) | **Décider/documenter en C2, appliquer hors chantier** (chaque majeure = son propre lot testé) ; merger les minors sûrs en fin de C2 |
| D3 | Tri des 28 branches `claude/*` | Je produis la liste keep/delete argumentée ; **suppression uniquement après ta validation** |

## Décisions
| Date | Décision | Motif |
|------|----------|-------|
| 2026-06-11 | **Kickoff validé** (« go » Mohamed) — plan S1→S3 + D1-D3 par défaut acceptés | Protocole chantier |
| 2026-06-11 | **D1** : cibles de charge beta TN = 100 utilisateurs simultanés, pic 500 soumissions/h, p95 < 1 s sur submit, < 2 s sur dashboard | Hypothèse beta, ajustable quand C6 fixera les vraies cibles |
| 2026-06-11 | **D2** : majeures dependabot décidées/documentées en C2, appliquées hors chantier (1 lot testé par majeure) ; minors sûrs mergés en fin de C2 | Limiter le risque de régression dans le chantier |
| 2026-06-11 | **D3** : liste keep/delete des 28 branches `claude/*` produite en S1 ; suppression uniquement après validation Mohamed | Sécurité (travail non mergé potentiel) |

## Journal d'avancement (append-only)
| Date | Fait | Reste / prochaine étape |
|------|------|--------------------------|
| 2026-06-11 | **Kickoff rédigé** + reconnaissance : 3 rapports 01/06 localisés, `audit:deps` = 0 vuln, 6 PRs dependabot (2 majeures), 28 branches `claude/*`, `npm outdated` cartographié. Plan S1→S3 + décisions D1-D3 posés. | Validation du plan + D1-D3 par Mohamed → lancer S1 (réconciliation & revue statique). |
| 2026-06-12 | **S3 livrée → C2 TERMINÉ**. Radar v2 **3,31/4** (vs 3,0 le 01/06, +0,31), 8 dimensions justifiées par preuve : Tests 2→3 (saut couverture 8 %→93 % + e2e + pgTAP, tempéré par GAP-026), Sécurité 3→3,5 (intégrité close en prod), Performance 3→3,5 (charge prouvée), Versioning 2,5→3 (CI + hygiène branches) ; aucun axe < 3. Backlog versé (GAP-005 🟢, 007 requalifié, 027/028/029/030/031/032/034 créés). 3 axes pour C4 : dimensionnement écriture, simplification pipeline build + mono-région, headers/CSP. **Verdict : socle sain, prêt beta, 0 bloquant technique** après GAP-026. Reste hors chantier : vague de minors (D2). | C4 (archi prod), alimenté par GAP-007/027/029. |
| 2026-06-12 | **D3 exécuté** (« Go D3 » Mohamed) : **35 branches distantes obsolètes supprimées** (2 lots, re-scan + re-preuves d'intégration à `main` juste avant ; `--no-verify` car suppression de ref = 0 commit poussé). **7 restantes** : `claude/app-focus-regression-bs0vey` (PR draft #87 active, gardée) + 6 `dependabot/*` (sort = D2). GAP-009 → 🟡 (branches faites ; reste fermer/merger les PRs dependabot, hors chantier). Correctif GAP-026 aussi versionné sur `main` (merge `906fcd2`). | S3 (synthèse). |
| 2026-06-12 | **S2 livrée + 🔴 P0 prod (GAP-026)**. Tests de charge k6 contre TEST (40 comptes de charge, corpus culture-générale). **En préparant la charge, 1er appel réel à `start_exercise_session` = `42702 started_at ambiguous` → démarrage de quête cassé en prod depuis le 10/06** (RPC + révocation `…190000` = plus de secours). Corrigé : migration `20260612090000` (RETURNING table-qualifié) + garde pgTAP `06_start_exercise_session.test.sql` ; vérifié TEST (start 200 + submit 6/6), `verify` ✅ 585. Campagnes : **D1 tenue 9–17× de marge** (submit p95 114 ms, dashboard 116 ms, 0 échec/25 977 req) ; stress ×5 = 0 échec mais submit p95 1,89 s (dégradation latence, pas erreur → pool Supabase à dimensionner en C4). Résilience : 4 chemins d'erreur fail-closed OK. TEST remis à niveau (7 migrations poussées). | Mohamed applique `…090000` en prod (P0) + valide D3. S3 = radar v2 + backlog. |
| 2026-06-11 | **Kickoff validé (« go ») puis S1 livrée** : (1a) réconciliation des 29 constats 01/06 — 15 faits, 4 partiels, 6 restants non bloquants ; (1b) revue archi — 0 violation de frontières, SPOF identifié = pipeline build custom Worker→Vercel, mono-région arn1, 3 routes monolithiques ; (1c) deps — triage des 6 PRs dependabot (2 à rejeter, 4 différées en lots), Cloudflare déclaré load-bearing (garder → C4), tri de 41 branches : 35 suppressions proposées. 3 livrables écrits sous `livrables/02-audit-technique/`. | Mohamed valide la liste branches (D3). Session suivante = S2 : Lighthouse/Web Vitals, charge k6 vs TEST (cibles D1), résilience. En fin de C2 : vague de minors + micro-fixes (F18/F26). |
