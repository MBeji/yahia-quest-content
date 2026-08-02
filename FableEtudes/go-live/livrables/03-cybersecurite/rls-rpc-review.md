# C3 — Revue statique RLS & RPC (S1.b, 2026-06-10)

> Pièce d'audit : revue exhaustive de l'état EFFECTIF FINAL des 53 policies RLS et des 44 fonctions
> SECURITY DEFINER (précédence = définition la plus récente). Produite par analyse des 91 migrations.
> Croisée avec l'état déployé (`pg_policies`, `information_schema.role_table_grants`) et les sondes
> dynamiques (`findings-log.md`). Les verdicts actionnables sont consolidés dans `findings-log.md`.

## Constat transversal
Aucune des tables de gameplay « self-owned » n'a de `REVOKE INSERT/UPDATE/DELETE … FROM authenticated`
ni de `ALTER DEFAULT PRIVILEGES` global. En Supabase, `authenticated` détient les privilèges table par
défaut → **pour ces tables la policy RLS est l'unique barrière**, et toutes utilisent `auth.uid() =
user_id`, ce qui autorise l'écriture de lignes self-owned arbitraires. Les tables **sensibles**
(`profiles`, `parcours_entitlements`, `parent_student_links`, `inventory_items`, `student_badges`,
`parcours`) ont, elles, bien reçu un `REVOKE` ciblé → écritures fermées (confirmé par sondes P2-P5 ✅).

## A. Policies RLS — verdicts clés (table complète : voir transcript d'audit)
- ❌ **`attempts` / "Users insert own attempts"** (INSERT, `WITH CHECK auth.uid()=user_id`, jamais révoqué) → forge (S-1).
- ❌ **`exercise_sessions` / insert+update own** (jamais révoqué) → session pour tout exercice, y c. premium (S-3).
- ❌ **`daily_objectives` / `weekly_quests` "manage own" (ALL)** (jamais révoqué) → auto-complétion (S-7).
- ⚠️ **`spaced_repetition_schedule` "manage own" (ALL)** → annulation de la pénalité anti-farm (S-8).
- ⚠️ **`questions` "visible through readable exercises"** (SELECT) → expose `correct_option` du catalogue entier (S-4).
- ⚠️ `difficulty_adaptation` ALL self (impact faible). `exercise_assignments` update assignee (faible).
- ✅ **Neutralisées par REVOKE** malgré une policy permissive : `parent_student_links` (insert/update),
  `inventory_items` (insert/update), `student_badges` (insert), `parcours_entitlements` (toutes écritures),
  `parcours` (écritures). → pas d'auto-lien, pas d'items gratuits, pas de badge auto, pas d'auto-grant premium.
- ✅ RLS SELECT correctement scopée partout (own/linked/admin) → pas d'IDOR (confirmé P6/P7).
- ✅ Catalogue (`subjects/chapters/themes/grades/parcours/shop_items/badges`) en lecture publique = OK.
- ✅ `rate_limit_events`, `dungeon_runs`, `dungeon_run_questions` : RLS activée, **0 policy** = deny-all client.
- ✅ Vues résumé en `security_invoker=true` ; MV leaderboard `REVOKE ALL FROM anon, authenticated`.

## B. Fonctions SECURITY DEFINER — verdicts clés (44 fonctions)
- ✅ **Toutes** ont `SET search_path = public` → aucun search-path hijack.
- ✅ **Aucun SQL dynamique** (`EXECUTE`/`format … USING`) avec entrée utilisateur → pas d'injection.
- ✅ **Mints révoqués** : `award_xp`, `award_coins`, `handle_new_user`, `award_badge_if_new` non appelables par `authenticated`/`anon`.
- ✅ Toutes les `admin_*` vérifient `is_admin()` en interne (échouent pour un non-admin même si appelables).
- ✅ Les RPC appelables par `authenticated` sont **self-scoppées** (submit, donjon, shop, hints, set_profile_role student|parent, set_current_parcours) avec contrôles de possession/atomicité.
- ⚠️ Réserves mineures sans élévation : `check_rate_limit(p_key)` accepte une clé arbitraire (épuisement d'un quota tiers) ; `has_parcours_entitlement(p_user,…)` accepte un user arbitraire mais ne renvoie qu'un booléen.

## C. Synthèse de risque (détail dans findings-log.md)
Schéma **bien durci sur l'élévation de privilège** (rôle, premium, mints, écritures shop/liens/inventaire/
entitlements — fermés à l'état final). Risque résiduel concentré sur **l'intégrité du gameplay
self-owned non révoqué en écriture** (`attempts`, `exercise_sessions`, `daily_objectives`,
`weekly_quests`, `spaced_repetition_schedule`) **+ l'exposition de `questions.correct_option`**.
**Correctif générique** = même recette déjà appliquée à `inventory_items`/`student_badges`/etc. :
`REVOKE INSERT/UPDATE/DELETE … FROM authenticated` sur ces tables (écritures via RPC uniquement) +
retirer `correct_option` de la policy SELECT `questions` (vue/colonne masquée, le corrigé ne transite
que par les RPC submit/dungeon).
