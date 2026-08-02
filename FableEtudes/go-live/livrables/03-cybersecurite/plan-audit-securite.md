# C3 — Plan d'audit de sécurité (kickoff 2026-06-10)

> Artefact opérationnel du chantier [03-audit-cybersecurite](../../03-audit-cybersecurite.md).
> Les findings se logguent dans `findings-log.md` (S1+) ; la synthèse dans
> `rapport-securite.md` (S3). Les actionnables → `GAP-NNN` au [backlog 90](../../90-backlog-remediation.md).

## 0. Cadre & autorisation
Audit de sécurité **autorisé** de l'application de Mohamed (son propre produit, avant ouverture
publique). Toute sonde de type exploit (IDOR, élévation, forge de données) se fait **uniquement
sur le projet Supabase TEST** (`pqegdnwdtbjtplcthxyp`) — **jamais la prod**. Outils réutilisés de C1
(`livrables/01-audit-fonctionnel/tools/` : `q.py`, `fix-test-seed.py`, `dev-on-test`).

## 1. Périmètre chiffré (grounding 2026-06-10)
- **DB** : 91 migrations · **44 fonctions SECURITY DEFINER** · **53 policies RLS** · 27 tables sous RLS.
- **App/API** : middleware CSRF (`start.ts`), middleware auth (`auth-middleware.ts`), ~40 server fns avec zod + rate-limit, rendu markdown DOMPurify.
- **Infra** : Vercel (prod, auto-deploy `main`) + Supabase (Postgres/Auth) ; secrets en env plateforme.
- **Constat immédiat** : **aucun header de sécurité** (CSP/HSTS/X-Frame-Options/X-Content-Type-Options/Referrer-Policy/Permissions-Policy) dans `vercel.json`/`server.ts`/`wrangler.jsonc`.

## 2. Ce que JE peux faire vs ce qui dépend de Mohamed / externe
**Exécutable en autonomie (cœur de l'audit) :**
- Revue statique exhaustive des 53 policies RLS + 44 RPCs SECURITY DEFINER (authz, élévation, injection, `search_path`, GRANT/REVOKE).
- Sondes dynamiques sur TEST : forge `attempts` (GAP-016), IDOR entitlements/rapports, élévation de rôle, abus anti-farm, accès admin.
- Revue front/API : XSS (politique DOMPurify), validation zod, secrets dans le repo, exposition service-role, cookies/JWT, couverture réelle du rate-limiting.
- `npm audit` / lockfile / dépendances. Mapping OWASP Top 10 (2021).
- Analyse conformité données mineurs (INPDP loi 2004-63) **sur pièces** (modèle de données, flux de consentement) + posture backup/DR documentée.

**Hors de ma main → je produis des exigences/recommandations, pas l'exécution :**
- Réglages **Supabase dashboard** (PITR/backups, paramètres Auth : confirmation email, mots de passe, MFA, fuites), **Vercel** (env, accès équipe, config headers), **GitHub** (branch protection).
- **Pentest réseau externe** (hors périmètre/outillage ici) → recommandation Go/No-Go d'un pentest tiers.
- Drill de restauration réel (nécessite accès backups) → je définis la procédure, exécution avec Mohamed.

## 3. Schéma de notation des risques
| Niveau | Sens |
|---|---|
| **P0** | Bloquant go-live : exploitable à distance par un utilisateur, fuite/altération de données, contournement de paiement. |
| **P1** | À corriger avant ouverture publique : durcissement important, exposition limitée ou nécessitant des conditions. |
| **P2** | Important, fenêtre courte post-lancement. |
| **P3** | Bonne pratique / défense en profondeur. |

## 4. Candidats déjà identifiés (à confirmer/instruire)
- **GAP-016 (confirmé statique)** — policy `"Users insert own attempts"` jamais révoquée (`20260522134120:101`) → forge de `attempts` (score/xp arbitraires) via PostgREST. Impacte leaderboard, quiz gate, prérequis donjon. **À confirmer dynamiquement sur TEST → probable P0/P1.**
- **GAP-015** — Alliance Code = UUID brut de l'élève exposé/partagé, non régénérable. **Angle vie privée mineurs.**
- **Nouveau (S2)** — absence totale de headers de sécurité HTTP. **Candidat P1/P2.**
- **GAP-014/B-5 rappel** — `rate-limit` fail-open local en cas de panne RPC (non partagé entre instances serverless).

## 5. Déroulé en sessions
- **S1 — Authz / RLS / RPC (le gros morceau)** : revue des 53 policies + 44 RPCs SECURITY DEFINER ; confirmation dynamique sur TEST des top risques (forge `attempts`, IDOR entitlements & rapports parent, élévation de rôle via `set_profile_role`/insert profil, accès aux RPCs `admin_*`/`award_xp`). → `findings-log.md`
- **S2 — Surface app/API/infra** : headers de sécurité, CSRF (portée réelle), secrets/env & exposition service-role, flux Auth (signup mineurs, reset, sessions, confirmation email), couverture rate-limit, `npm audit`/deps, mapping OWASP Top 10. → `findings-log.md`
- **S3 — Données personnelles, conformité, continuité + synthèse** : inventaire PII, minimisation, droit à l'effacement, **spécificité mineurs/INPDP & consentement parental**, posture backup/DR (exigences → C4), puis **rapport P0–P3** + plan de correction + GAPs versés. → `rapport-securite.md`

## 6. Livrables
- `findings-log.md` (F-3NN, preuves, repro sur TEST), `rapport-securite.md` (risques P0–P3 + plan de correction + exigences C4/C7), GAPs au backlog 90.
