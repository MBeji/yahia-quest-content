# Chantier 01 — Audit fonctionnel complet

> Pilotage : [00-MASTER-PLAN.md](./00-MASTER-PLAN.md) · Livrables volumineux : `go-live/livrables/01-audit-fonctionnel/`

| | |
|---|---|
| **Statut** | 🟢 Terminé (S1 + S2 + S3) — reliquat S2 mineur optionnel |
| **Avancement** | 95 % |
| **Dépendances** | Aucune (chantier indépendant — Phase A) |
| **Alimente** | Backlog 90 (GAP-010→019) · C5 (valeur produit, écart marketing A-15) · C6 (funnel premium cassé) · C7 (roadmap) |
| **Dernière session** | 2026-06-10 — S1 cartographie + S2/S2-suite walkthrough complet (8 personas) + S3 rapport final |
| **Prochaine action** | **C1 livré.** Reliquat optionnel (non bloquant) : pack famille e2e, level-up réel, états d'erreur réseau, flux « Signaler une erreur » complet. Sinon → enchaîner un autre chantier (C2/C3/C5/C6). **Action immédiate conseillée hors-chantier : corriger GAP-017 (P0).** |

## Contexte à charger en début de session
- Ce fichier + `00-MASTER-PLAN.md`
- `yahia-quest-arena/CLAUDE.md` (modèle mental : thèmes → grades → subjects → … ; modèle premium)
- Selon la tâche : `src/routes/` (inventaire), barrels `src/features/*/index.ts`, l'app lancée en dev (parcours réels)

## Objectifs (périmètre validé)
- Analyser l'ensemble des fonctionnalités existantes.
- Vérifier la cohérence des parcours utilisateurs et de l'UX.
- Identifier anomalies, incohérences métier et fonctionnalités manquantes.
- Évaluer la valeur apportée par chaque fonctionnalité et les opportunités d'amélioration.
- Valider l'adéquation besoins utilisateurs ↔ vision produit ↔ implémentation.
- Formaliser une cartographie globale de l'application et des processus métier.

## Livrables attendus
- [ ] Cartographie fonctionnelle complète (features × routes × personas × langues)
- [ ] Matrice d'évaluation : fonctionnalité × état (OK/anomalie/incomplet) × valeur (cœur/support/accessoire)
- [ ] Revue des parcours critiques par persona (élève concours, élève exploration, parent, admin, invité)
- [ ] Liste priorisée des anomalies & gaps → versée au backlog 90
- [ ] Recommandations UX/produit priorisées (quick wins vs structurant)

## Plan d'exécution (kickoff 2026-06-10 — détail : [plan-de-tests.md](./livrables/01-audit-fonctionnel/plan-de-tests.md))

Méthode : cartographie depuis le code, puis **walkthrough réel par persona** (8 personas, comptes
seedés du projet Supabase **TEST** — jamais la prod, le `.env` local pointe prod), grille à 4
dimensions (état / UX / valeur / métier), constats `F-NNN` → `GAP-NNN` au backlog 90.
Référentiel « vision produit » drafté en §0 du plan de tests, à corriger par Mohamed.

- [x] **S1 — Cartographie statique** (code → carte fonctionnelle : routes × features × RPCs × processus métier) + setup env TEST → [`cartographie.md`](./livrables/01-audit-fonctionnel/cartographie.md) (19 routes, 10 features, 10 processus, règles chiffrées, 31 candidats A-*/B-*)
- [x] **S2 — Walkthrough complet (8 personas)** → [`walkthrough-log.md`](./livrables/01-audit-fonctionnel/walkthrough-log.md) : onboarding, paywall, boucle IQ libre, **quiz gate école happy-path, boucle succès premium, donjon, boutique, parent, admin (BUG P0), leaderboard, RTL/AR mobile** + bugs métier confirmés en SQL
- [x] **S3 — Rapport final** (matrice valeur, adéquation vision/besoins, recommandations) → [`rapport-audit-fonctionnel.md`](./livrables/01-audit-fonctionnel/rapport-audit-fonctionnel.md). GAP-010→019 au backlog (dont **GAP-017 P0**)

**Outils d'audit créés** (réutilisables en S2-suite) : `scripts/e2e/dev-on-test.mjs` (dev server sur TEST, garde anti-prod) + `.claude/launch.json` (preview `dev-on-test`) dans le repo ; `livrables/01-audit-fonctionnel/tools/` (`ensure-test-users.mjs`, `fix-test-seed.py`, `q.py`) dans le wrapper.

## Décisions
| Date | Décision | Motif |
|------|----------|-------|
| 2026-06-10 | **Kickoff validé (GO)** par Mohamed : env TEST, vision draft §0 acceptée en l'état, découpage S1/S2/S3. | Validation explicite en session |

## Journal d'avancement (append-only)
| Date | Fait | Reste / prochaine étape |
|------|------|--------------------------|
| 2026-06-10 | Kickoff rédigé : plan de tests détaillé (8 personas, env TEST identifié — `.env` local = prod ⚠️, comptes seedés repérés, 19 routes inventoriées), draft vision produit à faire corriger. | Validation Mohamed → puis S1 |
| 2026-06-10 | **GO validé.** S1 fait (cartographie complète via 2 agents). Setup TEST (seed repo cassé → outils de contournement créés). S2 partiel en browser réel sur TEST : onboarding ✅, paywall premium ✅, boucle de quête IQ ✅ (rendu SVG, submit, SM-2, badge). 3 bugs métier confirmés en SQL (objectifs non crédités, récup streak morte, indice ×3→1). 7 GAP promus (GAP-010→016). | S2-suite : quiz gate école happy path, donjon, boutique, parent, admin, RTL/AR, mobile (voir « Prochaine action ») |
| 2026-06-10 | **S2-suite + S3 — C1 livré.** Walkthrough complet (premium, parent, admin, transverse) : quiz gate école ✅, boucle succès premium ✅ (+50 XP réels, compta SQL exacte), donjon ✅ (run+game-over), boutique ✅ (achat/équiper/armer), rapport parent ✅, **admin ❌ BUG P0 (consoles inaccessibles, collision queryKey — cause racine trouvée)**, leaderboard ⚠️, RTL/AR mobile ✅. GAP-017(P0)/018/019 ajoutés. Rapport final S3 écrit (matrice valeur + adéquation + recommandations). | C1 terminé. Reliquat optionnel non bloquant. Action immédiate conseillée : **fix GAP-017**. |
