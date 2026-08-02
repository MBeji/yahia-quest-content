# Tri des branches distantes — proposition keep/delete (D3)

> Livrable S1 du chantier [02](../../02-audit-technique-architecture.md). État au 2026-06-11 après
> `git fetch --prune`. **Aucune suppression ne sera faite sans validation explicite de Mohamed** (décision D3).

> **✅ EXÉCUTÉ le 2026-06-12** (« Go D3 » Mohamed) : **35 branches supprimées** (catégories A+B+C+D,
> en 2 lots `git push origin --no-verify --delete` — `--no-verify` car une suppression de ref ne
> pousse aucun commit, et `verify` était 585-vert sur l'arbre courant). **7 branches restantes** :
> `claude/app-focus-regression-bs0vey` (gardée — PR draft #87 ouverte ; sa suppression la fermerait)
> + les 6 `dependabot/*` (laissées au bot, sort = décision D2). Inventaire ci-dessous = état avant
> exécution.

Inventaire : **41 branches** distantes hors `main` = 29 `claude/*` + 3 `content/` + 2 `test/` +
1 `feat/` + 6 `dependabot/`.

**Recommandation globale : tout supprimer (35 branches, catégories A→D) + laisser dependabot gérer les siennes (E).**
Preuves par catégorie ci-dessous ; aucune branche ne contient de travail non livré.

## A — Mergées dans `main` au sens git (7) — suppression triviale

`git branch -r --merged origin/main` :

- `claude/skills-content-audit-rq1r70` (PR #84/#86 — audit contenu + bidi arabe, mergée le 11/06)
- `content/iq-training-fr` · `content/iq-training-domains` · `content/iq-training-multilang`
- `feat/quiz-gate-school-only`
- `test/e2e-coverage-phase1` · `test/e2e-phase2-coverage`

## B — Patch-équivalentes à `main` (20) — 0 commit unique (`git cherry`)

Chaque branche porte 1 commit dont le patch-id existe déjà dans `main` (merge effectué) :

`claude/backfill-profiles-grade` · `claude/ci-branch-protection` · `claude/ci-doc-e2e-reconcile` ·
`claude/ci-migration-guardrail` · `claude/consumables-shields` · `claude/content-theme-grade-aware` ·
`claude/dashboard-grade-scope` · `claude/docs-truth-fix` · `claude/e2e-quality` ·
`claude/explain-tooltips` · `claude/fix-quest-toast-spam` · `claude/gitignore-agent-worktrees` ·
`claude/light-theme-design-O2Htd` · `claude/nightly-playwright-tests-Kj32t` ·
`claude/perf-hot-path-indexes` · `claude/rename-xp-coins` · `claude/security-p0-hardening` ·
`claude/themes-grades-nav` · `claude/themes-grades-ui` · `claude/visible-skins`

## C — Retravaillées puis intégrées à `main` sous une autre forme (6) — preuves vérifiées

| Branche | Contenu | Preuve que c'est dans `main` |
|---|---|---|
| `claude/consumables-hints` | migration hints + UI | `supabase/migrations/20260606140000_consumable_hints.sql` présent dans `main` (et corrigé depuis par GAP-014) |
| `claude/consumables-potions` | arm/consume potions | `…120000_consumable_potions_arm_consume.sql` présent (verrou `FOR UPDATE OF inv` inclus) |
| `claude/fix-e2e-ci` | e2e verte + `subjects_is_premium` | suite e2e verte en CI ; le modèle premium est passé aux *parcours entitlements* (approche caduque) |
| `claude/skill-harness-code-review-xYE6d` | skill revue de code | `.claude/skills/code-review/` présent dans `main` |
| `claude/db-integration-tests` | pgTAP | `supabase/tests/` (5 fichiers) + `db-tests.yml` présents dans `main` |
| `claude/docs-consumables` | docs CLAUDE.md | la section « Consumables (shop items) » est dans le CLAUDE.md actuel |

## D — Branches d'historique divergées, fonctionnalité en prod (2) — dernier regard puis suppression

| Branche | Commits uniques | Pourquoi obsolète |
|---|---|---|
| `claude/account-charges-inquiry-Yscq0` (06-04) | 41 | Historique pré-refonte ; le durcissement du quiz gate (score ≥ 80 % + durée) est en prod (réutilisé par GAP-021) |
| `claude/themes-grades-model` (06-06, PR #53) | 43 | Le modèle themes→grades ET la suite e2e canonique vivent dans `main` depuis (e2e/, workflows, pages objects) ; la branche n'est plus la référence |

## E — Dependabot (6) — ne pas toucher à la main

`dependabot/npm_and_yarn/{vite-8.0.16, zod-4.4.3, recharts-3.8.1, types/node-25.9.1, vitejs/plugin-react-6.0.2, lovable.dev/vite-tanstack-config-2.2.0}`
— le bot supprime sa branche quand sa PR est fermée/mergée. Le sort de chaque PR est la décision
D2, documentée dans le [rapport v2 §4](./rapport-v2.md).

## Exécution (après validation Mohamed)

```bash
# Catégories A+B+C+D (35 branches) :
git push origin --delete \
  claude/skills-content-audit-rq1r70 content/iq-training-fr content/iq-training-domains \
  content/iq-training-multilang feat/quiz-gate-school-only test/e2e-coverage-phase1 \
  test/e2e-phase2-coverage claude/backfill-profiles-grade claude/ci-branch-protection \
  claude/ci-doc-e2e-reconcile claude/ci-migration-guardrail claude/consumables-shields \
  claude/content-theme-grade-aware claude/dashboard-grade-scope claude/docs-truth-fix \
  claude/e2e-quality claude/explain-tooltips claude/fix-quest-toast-spam \
  claude/gitignore-agent-worktrees claude/light-theme-design-O2Htd \
  claude/nightly-playwright-tests-Kj32t claude/perf-hot-path-indexes claude/rename-xp-coins \
  claude/security-p0-hardening claude/themes-grades-nav claude/themes-grades-ui \
  claude/visible-skins claude/consumables-hints claude/consumables-potions claude/fix-e2e-ci \
  claude/skill-harness-code-review-xYE6d claude/db-integration-tests claude/docs-consumables \
  claude/account-charges-inquiry-Yscq0 claude/themes-grades-model
```

Si les PRs GitHub associées sont encore ouvertes (#53 notamment), les fermer avec un commentaire
« superseded — contenu intégré à main » avant la suppression.
