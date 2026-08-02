# Réconciliation des audits du 2026-06-01 — état au 2026-06-11

> Livrable S1 du chantier [02 — Audit technique & architecture](../../02-audit-technique-architecture.md).
> But : statuer chaque constat des audits du 01/06 (fait / fait autrement / partiel / restant /
> obsolète) avec preuve, pour que le rapport v2 reparte d'une base honnête au lieu de re-auditer à blanc.

## Sources réconciliées (6 fichiers + 3 CSV)

| Run | Rapport | Checklist | CSV métriques | Particularité |
|---|---|---|---|---|
| REPO | `yahia-quest-arena/AUDIT_REPORT_2026-06-01.md` | `audit-actions-checklist-2026-06-01.md` | `audit-metrics-2026-06-01.csv` | Snapshot le plus ancien (pré-CI, lint cassé, 120 tests) |
| RUN | `AUDIT_REPORT_2026-06-01_RUN.md` (wrapper) | `…-run.md` | `…-run.csv` | Post-CI (lint 0/0, 142 tests, couverture 8,11 %) |
| RUN2 | `AUDIT_REPORT_2026-06-01_RUN2.md` (wrapper) | `…-run2.md` | `…-run2.csv` | Le plus détaillé (44 sous-scores), commit audité `21a5042` |

Méthode : union dédupliquée des 3 runs → 29 constats distincts (F01–F29) ; statut au 2026-06-11
vérifié sur le repo (`main`), les workflows CI, les migrations appliquées en prod et les GAPs du
programme go-live.

## Tableau de réconciliation

Légende : ✅ fait · ☑️ fait autrement · 🟠 partiel · ❌ restant · 🟡 restant (faible) · 🔁 obsolète/re-scopé

| ID | Constat 01/06 (sévérité) | Statut 11/06 | Preuve |
|---|---|---|---|
| F01 | Baseline lint cassée — 11 919 problèmes (critique) | ✅ | `eslint src --max-warnings=0` vert (gate zéro-warning), husky pre-commit lint-staged + pre-push `verify` ; RUN/RUN2 mesuraient déjà 0/0 |
| F02 | Aucun workflow CI (critique) | ✅ | 6 workflows : `ci.yml` (lint+typecheck+coverage+build:check+audit:deps), `db-tests`, `e2e`, `e2e-auth`, `migration-gate`, `nightly` |
| F03 | 0 tag/release malgré politique documentée (haute) | ❌ | `git tag -l` = 0 ce jour ; `docs/release-tagging-policy.md` existe, jamais exécutée → candidat GAP (tag `v1.0.0` au go-live) |
| F04 | Stratégie de branches non formalisée (basse) | ☑️ | Flux PR réel (42 branches distantes, merges tracés), ruleset branch-protection livré (`claude/ci-branch-protection`, intégré) ; l'hygiène des branches est traitée par le tri D3 (livrable séparé) |
| F05 | Routes monolithiques >300 L (haute) | ❌ | Aggravé en brut : `quest.$exerciseId.tsx` 819 L, `dashboard.tsx` 793 L, `dungeon.tsx` 640 L (vs 491/488/478) ; risque borné par le gate `max-lines: 750` (hors blancs/commentaires) et par l'extraction des server fns vers `features/` — l'UI reste à découper |
| F06 | Garde-fous de complexité absents (critique) | 🟠 | `max-lines: ["error", 750]` actif dans `eslint.config.js:45` ; pas de règle `complexity` — compléter si récidive |
| F07 | Couverture ~8 % (critique) | ✅ | ≈93 % stmts / 93 % lignes / 81 % branches **scopée au code possédé** (`features/ shared/ lib/ hooks/`) ; routes/`components/ui` exclus par design (documenté CLAUDE.md « Coverage is scoped ») |
| F08 | Seuils Vitest 4 %/2,5 % (haute) | ✅ | Seuils à **80 %** sur les 4 métriques dans `vitest.config.ts` ; DoD §2 interdit de les baisser |
| F09 | Tests authz/token manquants (critique) | ✅ | `auth-middleware` couvert à 100 %, suite e2e authentifiée en CI, pgTAP `supabase/tests/` (5 fichiers : economy grants, role escalation, RLS isolation, scoring, entitlements), revue RLS/RPC du chantier C3 |
| F10 | 0 test E2E / intégration (moyenne) | ✅ | Playwright public + authed en CI (`e2e.yml`, `e2e-auth.yml`, `nightly.yml`), page objects typés ; pgTAP = tests d'intégration DB |
| F11 | XSS — pas de DOMPurify (haute) | ✅ | DOMPurify dans `src/shared/lib/markdown.ts` + `docs/xss-rendering-policy.md` + tests de contrat ; les `dangerouslySetInnerHTML` passent par le sanitizer |
| F12 | Sécurité automatisée en CI incomplète (moyenne) | 🟠 | `audit:deps` en CI ✅ ; security headers **déployés** (routing Vercel : HSTS, CSP, XFO…) mais non validés automatiquement en CI, et CSP encore `unsafe-inline` (TODO review #6) → reste porté par GAP-022 (C4) |
| F13 | `npm audit` bloqué par le registry mirror (haute) | ✅ | `npm run audit:deps` fonctionne (local + CI) : « found 0 vulnerabilities » (prod, high) le 11/06 |
| F14 | Pas de cadence de mise à jour deps (moyenne) | ✅ | `docs/dependency-maintenance.md` + dependabot actif (6 PRs ouvertes = la cadence tourne) ; le sort des majeures est l'objet de D2 (rapport v2 §4) |
| F15 | Surface de dépendances large (basse) | 🟡 | Toujours vrai (26 pkgs Radix, three, recharts, motion) — assumé : justifié par le produit, 0 vuln, budgets bundle par chunk |
| F16 | Pas de logging structuré (moyenne) | ✅ | `src/shared/lib/logger.ts` : JSON structuré + redaction des secrets (RUN/RUN2 l'observaient déjà) |
| F17 | Pas de correlation/request ID (moyenne) | ❌ | Aucun `requestId` dans le logger ce jour → candidat GAP (traçabilité prod) |
| F18 | `console.error` au lieu du logger dans ErrorComponent (basse) | ❌ | `src/routes/__root.tsx:45` toujours en `console.error` (+ `start.ts:16`) → micro-fix candidat |
| F19 | Budgets bundle à imposer (moyenne) | ✅ | `scripts/check-bundle-budget.mjs` en CI via `build:check` ; budgets par chunk (index 450, charts 390, supabase 240, motion 150, dashboard 30, i18n 80 kB) ; index réel 399,76 kB |
| F20 | Pas de Lighthouse/télémétrie runtime (haute) | ❌ | Toujours absent de la CI ; mesure manuelle prévue en S2, intégration CI = candidat GAP (P3) |
| F21 | Pas de cache edge KV/Cache API (basse) | 🔁 | Cible Cloudflare KV caduque : la prod est sur Vercel serverless (région `arn1`). Le besoin réel (cache HTTP/CDN des données quasi-statiques) est re-scopé vers C4 ; les assets hashés ont déjà `Cache-Control: immutable` |
| F22 | `defaultPreloadStaleTime: 0` (basse) | ✅ | `src/router.tsx:20` = `30_000` |
| F23 | JSDoc/commentaires d'intention insuffisants (moyenne) | 🟠 | Politique non formalisée ; constantes gameplay documentées (`gamification.ts`), 3 TODO trackés seulement — faible priorité |
| F24 | Duplication non mesurée (basse) | 🟡 | Toujours pas d'outil de mesure ; le scan S1 (0 import cross-feature, barrels) suggère une duplication faible — faible priorité |
| F25 | Pas de scanner de code mort dédié (basse) | 🟡 | Toujours pas d'outil (knip…) ; compensé par DoD §3 (interdiction du dead code) + ESLint unused — faible priorité |
| F26 | `noUnusedLocals/Parameters` désactivés (basse) | ❌ | `tsconfig.json:19-20` toujours `false` (compensé par ESLint) → micro-fix candidat |
| F27 | ADRs manquants (haute au RUN) | 🟠 | Pas d'ADR formels, mais `ARCHITECTURE.md` + `docs/*.md` (5 politiques) + décisions tracées dans `go-live/` couvrent le besoin — reclassé faible |
| F28 | Suivi de remédiation par KPIs (moyenne) | ☑️ | Rôle rempli par le programme go-live : backlog `90-…` (GAP-NNN priorisés), dashboards chantiers, journaux append-only |
| F29 | Exclure les fichiers générés des rapports de dette (moyenne) | ✅ | Couverture/lint excluent générés & vendored (`routeTree.gen.ts`, `components/ui`) ; lint 0/0 avec ces fichiers présents |

## Synthèse

| Statut | Nb | IDs |
|---|---|---|
| ✅ Fait | 13 | F01 F02 F07 F08 F09 F10 F11 F13 F14 F16 F19 F22 F29 |
| ☑️ Fait autrement | 2 | F04 F28 |
| 🟠 Partiel | 4 | F06 F12 F23 F27 |
| ❌ Restant | 6 | F03 F05 F17 F18 F20 F26 |
| 🟡 Restant faible (assumé) | 3 | F15 F24 F25 |
| 🔁 Obsolète / re-scopé | 1 | F21 (→ C4) |

**Lecture** : 15/29 constats sont soldés et 4 largement entamés — l'essentiel du « critique » du
01/06 (lint, CI, couverture, XSS, e2e, authz) est derrière nous. Les 6 restants sont de la dette
ciblée, aucun bloquant lancement : 2 micro-fixes (F18, F26), 2 chantiers d'outillage (F03 tags,
F20 Lighthouse), 1 transverse (F17 correlation ID), 1 structurel de fond (F05 routes monolithiques).
Ils seront versés au backlog 90 en S3 avec le reste du rapport v2.

## Baseline scoring 01/06 (pour le radar v2 de S3)

Échelle /4, 8 dimensions (libellés normalisés) :

| Dimension | REPO | RUN | RUN2 |
|---|---|---|---|
| Versioning | 3,0 | 2 | 2,5 |
| Stack technologique | 3,0 | 3 | 3,5 |
| Architecture | 2,5 | 3 | 3,5 |
| Qualité de code | 2,0 | 2 | 3 |
| Tests & couverture | 3,0¹ | 2 | 2 |
| Performance | 3,0 | 3 | 3 |
| Logging & erreurs | 2,0 | 3 | 3,5 |
| Sécurité | 3,0 | 3 | 3 |
| **Moyenne** | 2,69 | 2,63 | 3,0 |

¹ REPO n'avait pas mesuré la couverture (score optimiste) ; RUN/RUN2 (couverture 8 %) sont la
référence honnête. **Le radar v2 (S3) se comparera à RUN2**, le run le plus détaillé (44 sous-scores
dans `audit-metrics-2026-06-01-run2.csv`).
