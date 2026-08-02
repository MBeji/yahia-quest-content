# Runbook déploiement & rollback — yahia-quest-arena

> Livrable S3 du chantier [04](../../04-architecture-prod-deploiement.md). Date : 2026-06-12.
> Consolide ce qui existe déjà dans le repo (DoD §7, `migration-gate.yml`, ruleset
> `main-protection.json`, `release-tagging-policy.md`) en **une procédure exécutable**.
> Source de vérité du code/CI : `yahia-quest-arena/CLAUDE.md`. Ce runbook ne réécrit pas les
> règles — il les met bout à bout pour le jour J et les incidents.

## Le fait fondateur (à ne jamais oublier)

**Pousser sur `main` = déploiement automatique en production Vercel.** Il n'y a pas de bouton
« deploy » séparé : le merge EST le déploiement. Tout le reste de ce runbook découle de là.

Corollaire dur (DoD §7) : **une migration Supabase dont dépend le code doit être appliquée à la
prod AVANT que le code soit mergé.** Sinon la prod tourne du code neuf contre un schéma ancien
(c'est exactement ce qui a causé GAP-026 et les incidents de déploiement passés).

## 0. Carte des environnements

| Environnement | Quoi | Déploiement | Données |
|---|---|---|---|
| **Production** | `https://yahia-quest-arena.vercel.app/` (→ domaine custom au palier 1) | auto sur push `main` | Supabase prod `fasrenmmrkqjoobrztbp` |
| **Preview** | URL éphémère par PR (`*-git-<branch>.vercel.app`) | auto sur push de branche / PR | **pointe la prod** (mêmes env vars) — *à activer dans Vercel* |
| **TEST** | pas d'URL web ; cible des e2e authentifiés + charge + drill backup | manuel (`e2e:setup`) | Supabase TEST `pqegdnwdtbjtplcthxyp` |
| **Local** | `npm run dev` | — | `.env` → **prod** (lecture) ; `.env.test` → TEST (e2e) |

⚠️ Pas de staging au lancement : **la beta EST le staging**. Un staging dédié se justifiera avec
les paiements en ligne (C6). ⚠️ Les previews Vercel pointent la prod — utile pour valider le rendu,
**dangereux pour tester des mutations** ; pour ça → dev-on-TEST.

## 1. Déploiement standard (flux nominal d'une PR)

C'est le chemin de 95 % des changements. Le ruleset `main-protection.json` l'impose (pas de push
direct sur `main`).

1. **Brancher** depuis `main` à jour : `git switch -c <type>/<slug>`.
2. **Développer** + respecter la DoD (gate verte localement : `npm run verify`, ou
   `npm run ci:verify` pour du release-grade).
3. **Pousser la branche**, ouvrir la PR. Les 4 checks requis tournent :
   `verify` · `Migration presence` · `pgTAP suite` · `e2e`.
4. **S'il y a une migration** → dérouler la section **§2** AVANT de merger (le check
   `Migration presence` reste rouge tant que le label `migration-applied` n'est pas posé).
5. **PR à jour avec `main`** (strict mode du ruleset) + 4 checks verts → **squash-merge**.
6. **Vercel déploie automatiquement.** Surveiller : dashboard Vercel (build OK) puis **§4 smoke
   prod**.
7. **Si go-live ou jalon** → poser le tag (section **§5**).

> Solo-maintainer : `required_approving_review_count = 0` — c'est le couple *PR + checks verts*
> qui fait foi, pas une revue humaine (cf. `ci-cd-and-branch-protection.md`).

## 2. Déploiement AVEC migration (ordre obligatoire)

Le piège n°1 du projet. L'ordre n'est pas négociable :

1. **Générer/écrire la migration** dans `supabase/migrations/` (contenu → via `content:build` ;
   schéma/RPC → à la main). **Préférer l'additif** (cf. §3 pour le destructif).
2. **Appliquer à la prod D'ABORD** — Mohamed, via **Supabase SQL editor** ou `supabase db push`.
   *(Rappel sécurité : seul Mohamed touche la prod ; jamais d'application auto par le repo.)*
3. **Vérifier** l'application (la fonction/table/colonne existe et se comporte) — idéalement un
   appel réel (cf. la leçon GAP-026 : un test pgTAP sur tout nouveau RPC SECURITY DEFINER).
4. **Poser le label `migration-applied`** sur la PR → le check `Migration presence` repasse vert.
5. **Merger** → Vercel déploie du code contre un schéma qui le supporte déjà.

**Cas multi-migrations / changement de contrat (déploiement 3-temps)** — pour rendre un changement
réversible et sans fenêtre cassée (patron déjà pratiqué, C3/GAP-021) :
- **T1** migration *additive* (nouvelle colonne/fn/grant) + code qui tolère l'ancien ET le nouveau.
- **T2** bascule du code sur le nouveau chemin (l'ancien n'est plus écrit).
- **T3** migration de nettoyage (REVOKE / DROP de l'ancien) une fois T2 stable en prod.

## 3. Rollback

Deux plans distincts selon ce qui a cassé — **ne pas confondre code et données.**

### 3a. Rollback du CODE (régression applicative, build cassé, bug visible)
- **Vercel Instant Rollback** : dashboard Vercel → Deployments → le déploiement précédent connu
  bon → **Promote to Production**. < 1 min, aucun rebuild. **C'est le réflexe par défaut.**
- Puis, à froid : `git revert` du commit fautif sur une branche → PR → re-déploiement propre
  (ne jamais laisser `main` diverger de ce qui tourne réellement en prod).
- ⚠️ **Si le code reverté dépendait d'une migration déjà appliquée** : le rollback de code est sûr
  **si la migration était additive** (le vieux code ignore la nouvelle colonne/fn). Si elle était
  destructive, voir 3b — le revert de code ne suffit pas.

### 3b. Rollback / récupération des DONNÉES (corruption, migration destructive ratée)
- **Migration additive** → rien à défaire côté DB (le vieux code coexiste). Préférable toujours.
- **Migration destructive** → appliquer le **plan de retour écrit** (toute migration destructive
  doit en embarquer un — règle §3 dossier archi). Pas de plan = ne pas l'appliquer.
- **Perte/corruption de données** → procédure de restauration backup : `docs/backup-restore-runbook.md`
  (scénario A même projet / scénario B projet reconstruit ; RPO 24 h / RTO 1 h).

### 3c. Panne d'une dépendance externe
- **Supabase down** → l'app est dégradée (l'auth et toutes les server fns en dépendent) ;
  surveiller la status page Supabase ; rien à « rollback », attendre + communiquer (UptimeRobot
  aura alerté). Pause projet Free après ~7 j d'inactivité : non concerné en trafic réel.
- **Vercel down** → idem, attendre ; le rollback ne change rien à une panne plateforme.

## 4. Smoke test post-déploiement (à faire à CHAQUE déploiement prod)

Le minimum vital, < 3 min, sur l'URL prod réelle :
1. **Landing** charge (HTTP 200, rendu visible).
2. **Connexion** d'un compte de test (le JS tourne — c'est exactement ce que la régression
   PR #87 avait cassé : page rendue mais inerte).
3. **Démarrer une quête + soumettre** une réponse (chemin RPC `start_exercise_session` →
   `submit_exercise_attempt` — le chemin garde-fou pgTAP, celui cassé par GAP-026).
4. **Dashboard** s'affiche avec XP/niveau cohérents.
5. Console navigateur : **zéro erreur** ; (quand Sentry sera câblé : zéro nouvelle issue).

Si un de ces points échoue → **§3a Instant Rollback** immédiat, diagnostic ensuite à froid.

## 5. Releases & tags (GAP-028)

Politique : `docs/release-tagging-policy.md` (semver `vMAJOR.MINOR.PATCH`, tag **après** CI verte
sur `main`).

**Tag de go-live `v1.0.0`** — à poser quand la checklist Go/No-Go (livrable voisin) est ✅ et le
smoke §4 vert sur le commit de lancement :
```bash
git switch main && git pull
git tag -a v1.0.0 -m "Release v1.0.0 — go-live beta publique"
git push origin v1.0.0
```
Puis publier les release notes (changements clés + notes de migration). **Hotfix** : brancher
depuis le dernier tag, fix minimal, bump patch (`v1.0.1`).

## 6. Garde-fous automatiques en place (ne pas contourner)

- **Ruleset `main-protection.json`** : PR obligatoire, 4 checks requis (strict), pas de
  force-push, pas de suppression de `main`, **s'applique aux admins** (pas de merge de code rouge
  en prod, même par Mohamed). Import : Settings → Rules → Rulesets → Import.
- **`migration-gate.yml`** : bloque une PR à migration sans label `migration-applied` (ack humain).
- **`pgTAP suite`** (`db-tests.yml`) : exécute les vraies migrations contre un Postgres local +
  invariants (grants économie verrouillés, RLS, anti-rush). **La seule couche qui exécute le SQL
  réel** — d'où l'obligation d'un test pgTAP par nouveau RPC.
- **`db-backup.yml`** : dump nocturne prod + drill mensuel (cf. `backup-restore-runbook.md`).
- **`--no-verify`** : interdit (DoD §2), sauf suppression de refs sans commit (documenté).

## 7. Ce qui reste manuel (et assumé au lancement)

| Action | Qui | Quand |
|---|---|---|
| Appliquer les migrations à la prod | Mohamed | avant chaque merge à migration |
| Promote/rollback Vercel | Mohamed | incident |
| Poser les tags de release | Mohamed | jalons |
| Activer le ruleset `main` (réglage GitHub) | Mohamed | **avant le go-live** (Go/No-Go) |
| Activer les previews Vercel par PR | Mohamed | quand utile (gratuit) |
| Lancer/lire le drill backup | moi (dispatch) / Mohamed (lecture) | mensuel |
