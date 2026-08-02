# C3 — Journal des findings sécurité (S1, 2026-06-10)

> Plan : [plan-audit-securite.md](./plan-audit-securite.md). Sondes dynamiques exécutées
> **uniquement sur le projet Supabase TEST** (`pqegdnwdtbjtplcthxyp`) via le harnais
> `tools/probe.py` (attaque l'API PostgREST comme un utilisateur authentifié normal → RLS +
> grants s'appliquent). Findings `F-3NN` → confirmés versés en `GAP-NNN` au backlog.

## S1.a — Sondes dynamiques (exploit réel via PostgREST)

Compte attaquant : `student.free` (rôle student, sans entitlement). Cible IDOR/lien : `student.premium`.

| # | Vecteur testé | Résultat HTTP | Verdict |
|---|---------------|---------------|---------|
| P1 | Forge `attempts` (xp_earned=99999, score=100) | **201 Created** | ❌ **VULNÉRABLE** |
| P2 | Gonfler son propre profil (xp/coins) via PATCH | 403 | ✅ bloqué (grant UPDATE révoqué) |
| P3 | S'auto-élever `role=admin` | 403 | ✅ bloqué (grant + trigger) |
| P4 | S'auto-octroyer un entitlement premium | 403 | ✅ bloqué (pas de grant INSERT) |
| P5 | S'auto-lier comme parent à un autre élève | 403 | ✅ bloqué (pas de grant INSERT) |
| P6 | IDOR : lire le profil d'autrui | 200 / **0 ligne** | ✅ bloqué (RLS SELECT) |
| P7 | IDOR : lire les entitlements d'autrui | 200 / **0 ligne** | ✅ bloqué (RLS SELECT) |
| P8 | Appel direct au minteur `rpc/award_xp` | 403 | ✅ bloqué (REVOKE) |
| P9 | Non-admin appelle `rpc/admin_grant_parcours` | 400 `Unauthorized` | ✅ bloqué (garde `is_admin()` interne) |
| P10 | Forge `exercise_sessions` | **201 Created** | ❌ **VULNÉRABLE** |
| S-4 | Lire `questions.correct_option` (corrigé) du quiz | 200 / **5/5 réponses** | ❌ **CORRIGÉ EXPOSÉ** |
| S-3 | Lire contenu+corrigé d'un boss **premium** d3 (sans entitlement) | 200 / **6/6 réponses** | ❌ **CONTENU PREMIUM EXPOSÉ** |

**Lecture d'ensemble : la posture sécurité est solide sur les risques GRAVES.** Élévation de
privilège, auto-octroi premium (contournement de paiement), accès aux données/PII d'autrui (IDOR),
mint d'XP et RPCs admin sont **tous correctement bloqués** — la migration de durcissement
`20260606150000` a réellement révoqué les grants dangereux et l'`is_admin()` interne tient. Le
**seul trou systémique** est l'**intégrité du gameplay**.

## Findings

### F-301 — Forge de `attempts` (intégrité/anti-triche) · **P1** · → GAP-016
Un utilisateur authentifié peut INSÉRER directement des lignes `attempts` arbitraires
(`xp_earned`, `score_pct`, `correct_count`…) via PostgREST (`POST /rest/v1/attempts`, **HTTP 201**).
- **Cause** : policy `"Users insert own attempts" WITH CHECK (auth.uid()=user_id)`
  (`20260522134120:101`) **+** grant `INSERT/UPDATE/DELETE` sur `attempts` toujours accordé à
  `authenticated` — jamais révoqués alors que l'écriture légitime passe par le RPC SECURITY DEFINER
  `submit_exercise_attempt`.
- **Impact** : (1) **leaderboard matière** faussé (= somme `attempts.xp_earned`) ; (2)
  **contournement du quiz gate école** (le gate lit `attempts ≥ 80 %`) → un élève débloque les
  missions sans passer le quiz ; (3) **prérequis donjon** (2 matières/3 chapitres « tentés »)
  falsifiables. **Pas** de fuite de données d'autrui, **pas** d'accès premium, **pas** d'élévation.
- **Sévérité : P1** (intégrité des mécaniques cœur, exploitable par tout compte ; mais pas une
  compromission de données ni de paiement, d'où P1 et non P0).
- **Correctif** : révoquer `INSERT/UPDATE/DELETE` sur `attempts` (+ tables de progression, voir
  F-302) à `authenticated`, ne laisser passer que les RPCs SECURITY DEFINER. Le leaderboard global
  (profil) est déjà protégé (P2 ✅).

### F-302 — Tables de progression client-inscriptibles (intégrité) · **P2**
Mêmes grants ouverts sur `exercise_sessions` (forge confirmée, **HTTP 201**), et par grant sur
`daily_objectives`, `weekly_quests`, `difficulty_adaptation` (INSERT/UPDATE/DELETE à `authenticated`).
- **Impact** : forger des sessions, marquer des objectifs « complétés », auto-ajuster sa difficulté.
  Impact moindre (les récompenses d'objectifs ne sont de toute façon jamais créditées — GAP-012 ;
  pas de fuite ni d'argent). Renforce néanmoins le tableau « écritures gameplay non verrouillées ».
- **Correctif** : même remédiation groupée que F-301 (révoquer les writes client, passer par RPC).

### F-305 — Banque de réponses exposée au client (`questions.correct_option`) · **P1** · → GAP-020
Tout utilisateur authentifié peut lire le **corrigé** de n'importe quelle question via
`GET /rest/v1/questions?select=correct_option` (confirmé : **5/5** réponses du quiz, et **6/6** d'un
**boss premium difficulté 3 sans entitlement** — S-3/S-4, HTTP 200).
- **Cause** : policy `"Questions visible through readable exercises"` (`20260522134150:208`) renvoie la
  **ligne entière** `questions`, `correct_option` compris, pour tout exercice du catalogue (source
  `admin`). Les parcours donjon/submit masquent la réponse côté RPC, mais la table reste lisible en direct.
- **Impact** : (1) **intégrité pédagogique** — un élève (ou un script) peut dumper les **4430 réponses**
  et répondre 100 % partout ; (2) **bypass du contenu premium** en lecture — le contenu + corrigé des
  exercices premium est accessible sans entitlement (le gate n'est qu'applicatif, pas en RLS) ; (3)
  combiné à F-301, scoring parfait trivial. **Pas** de fuite de données d'AUTRES utilisateurs.
- **Sévérité : P1** (la banque de questions/réponses est le cœur de valeur d'un produit de prép-concours ;
  exposition en masse scriptable). Pour la prép-concours, fortement recommandé avant lancement.
- **Correctif** : retirer `correct_option` de la projection client (vue dédiée sans la colonne, ou
  colonne masquée / RLS column-level), le corrigé ne transitant que par les RPC `submit_*`/donjon.

### F-303 — Aucun en-tête de sécurité HTTP · **P2**
Aucun `Content-Security-Policy`, `Strict-Transport-Security`, `X-Frame-Options`,
`X-Content-Type-Options`, `Referrer-Policy`, `Permissions-Policy` dans `vercel.json` / `src/server.ts`
/ `wrangler.jsonc` (seul `content-type` est posé).
- **Impact** : clickjacking (pas de `X-Frame-Options`/CSP frame-ancestors), MIME sniffing, pas de
  HSTS, pas de durcissement XSS par CSP. Surface d'attaque front élargie pour une cible grand public
  (mineurs).
- **Correctif** : ajouter les headers via `vercel.json` (`headers`) ou un middleware de réponse.
  Exigence à transmettre à **C4** (config plateforme).

### F-304 — Alliance Code = UUID brut de l'élève · **P3** · → GAP-015 (réévalué)
Le « code » de liaison parent affiché dans le dashboard élève est l'`user_id` brut, non régénérable.
- **Nuance issue des sondes** : l'auto-lien direct est **bloqué** (P5 ✅) ; la liaison ne passe que
  par `link_student_by_code`. Mais **quiconque connaît l'UUID d'un élève peut s'y lier** (compte
  parent) et accéder à son rapport (PII mineur). Exposition d'un identifiant interne + risque de
  liaison non sollicitée. **Sévérité abaissée à P3** (exploitation nécessite de connaître l'UUID et
  un compte parent ; pas d'accès en masse), mais à corriger pour la conformité mineurs (→ C3 S3).

## Bonnes pratiques confirmées (défense réelle, à conserver)
- Grants d'écriture dangereux **révoqués** sur `profiles` (xp/coins/role), `parcours_entitlements`,
  `parent_student_links`, `inventory_items`, `student_badges` → pas d'auto-triche sur ces tables.
- `award_xp`/`award_coins`/`handle_new_user` **REVOKE** de `authenticated` (mint impossible).
- RLS SELECT correctement scopée (own/linked) → pas d'IDOR sur profils/entitlements.
- RPCs `admin_*` gardées en interne par `is_admin()` (échouent pour un non-admin même si appelables).
- CSRF actif (`start.ts`), validation zod sur les server fns, DOMPurify sur le markdown.

## S1.b — Revue statique RLS/RPC (faite) → [rls-rpc-review.md](./rls-rpc-review.md)
Revue exhaustive des 53 policies + 44 fonctions SECURITY DEFINER (état effectif final). **Converge
avec les sondes.** Points saillants :
- ✅ **Toutes** les fonctions SECURITY DEFINER ont `SET search_path = public` ; **aucun SQL dynamique
  injectable** ; **mints révoqués** (`award_xp`/`award_coins`/`handle_new_user`/`award_badge_if_new`) ;
  toutes les `admin_*` gardées par `is_admin()` ; écritures sensibles (profil/entitlements/liens/
  inventaire/badges) **révoquées** à `authenticated`.
- ❌ Risque résiduel = **intégrité gameplay self-owned non révoquée** : `attempts` (F-301),
  `exercise_sessions` + `daily_objectives`/`weekly_quests`/`difficulty_adaptation`/`spaced_repetition_schedule`
  (F-302), **+ `questions.correct_option` exposé** (F-305).

## Bilan S1 & mapping backlog
| Finding | Sévérité | GAP |
|---|---|---|
| F-301 forge `attempts` | P1 (l'agent a argué P0) | GAP-016 (confirmé) |
| F-305 corrigé `questions` + contenu premium exposés | P1 | **GAP-020 (nouveau)** |
| F-302 tables progression/sessions inscriptibles | P2 | **GAP-021 (nouveau)** |
| F-303 aucun header de sécurité HTTP | P2 | **GAP-022 (nouveau)** |
| F-304 Alliance Code = UUID | P3 | GAP-015 (réévalué P3) |

**Conclusion S1** : la sécurité est **solide sur les vecteurs graves** (élévation, premium, PII, mints,
IDOR — tous bloqués/vérifiés). Le risque concentré est l'**intégrité du contenu et du gameplay** (un
seul correctif groupé : `REVOKE` les écritures gameplay + masquer `correct_option`).

---

# S2 — Surface app / API / infra (2026-06-10)

## Résultats
| Domaine | Constat | Verdict |
|---|---|---|
| **Secrets / service-role** | `SUPABASE_SERVICE_ROLE_KEY` utilisé **uniquement** dans `client.server.ts` (serveur) ; jamais importé en code client ; seule la clé *publishable* (anon) atteint le navigateur. | ✅ OK |
| **Dépendances** | `npm audit --omit=dev --audit-level=high` → **0 vulnérabilité**. | ✅ OK |
| **XSS** | 3 points `dangerouslySetInnerHTML` : leçon via `renderMarkdown` (DOMPurify, allowlist stricte, pas de script/href/style) ; figures via `sanitizeSvg` (DOMPurify profil SVG) ; `chart.tsx` `<style>` app-contrôlé. Texte des questions/options rendu en enfants React (échappé). Politique explicite `docs/xss-rendering-policy.md`. | ✅ OK |
| **CSRF** | `createCsrfMiddleware` actif sur les server fns (`start.ts`). | ✅ OK |
| **En-têtes HTTP** | `vercel.json` ne déclare **aucun** header (que `buildCommand`). Voir F-303/GAP-022. | ❌ P2 |
| **Rate-limit** | DB-backed (`check_rate_limit`) ; **fallback local en mémoire par instance** si le RPC échoue (`rate-limit.ts:51-60`) → non partagé entre instances serverless (contournable en cas de panne DB). | ⚠️ P3 (GAP-014) |
| **Auth (signup mineurs)** | **Aucun champ âge/date de naissance, aucun consentement parental** au signup (grep `age|birth|consent|parental|coppa|rgpd` → rien). Produit visant des 11-15 ans. | ❌ conformité → GAP-003 |
| **Auth config (projet TEST)** | `disable_signup=false`, `mailer_autoconfirm=false` (confirmation email requise), `anonymous_users=false`, OAuth tous `false` **alors que l'UI affiche « Continue with Google »** (config par env). Politique de mot de passe / protection mots de passe compromis / MFA : **non visibles via l'API** (réglages dashboard). | ⚠️ voir GAP-023 |

## F-306 — Hardening Auth prod à vérifier · **P2** · → GAP-023
Les réglages Auth sensibles ne sont pas dans le repo (dashboard Supabase) : politique de mot de passe
(longueur/complexité), **protection des mots de passe compromis** (HaveIBeenPwned), confirmation email
+ **SMTP custom** (sinon délivrabilité, recoupe GAP-006), providers OAuth réellement configurés en prod
(le bouton Google est affiché ; provider désactivé sur TEST → clic en erreur). À auditer/durcir sur le
projet **prod** avant ouverture. (Dépend de Mohamed/dashboard → exigence transmise à C4.)

## Mapping OWASP Top 10 (2021) — synthèse S1+S2
| Catégorie | État | Référence |
|---|---|---|
| A01 Broken Access Control | ⚠️ partiel — authz/RLS/IDOR **solides**, mais écritures gameplay + lecture corrigé ouvertes | GAP-016/020/021 |
| A02 Cryptographic Failures | ⚠️ HTTPS + JWT OK, secrets server-side ; **HSTS absent** | GAP-022 |
| A03 Injection | ✅ pas de SQL dynamique injectable, XSS sanitizé, zod systématique | — |
| A04 Insecure Design | ⚠️ tables gameplay client-inscriptibles (oubli de durcissement) | GAP-016/021 |
| A05 Security Misconfiguration | ❌ aucun header de sécurité ; config OAuth/Auth prod à vérifier | GAP-022/023 |
| A06 Vulnerable Components | ✅ `npm audit` 0 high/critical (fraîcheur deps → C2) | — |
| A07 Identification & Auth Failures | ⚠️ email confirm ON, pas de MFA (acceptable), politique mdp prod à vérifier | GAP-023 |
| A08 Software & Data Integrity | ⚠️ forge attempts + corrigé exposé | GAP-016/020 |
| A09 Logging & Monitoring | ⚠️ logger avec redaction ✅, mais pas de monitoring/alerting prod | GAP-002 (C4) |
| A10 SSRF | ✅ pas de fetch serveur d'URL fournie par l'utilisateur | — |

**Conclusion S2** : surface app/API saine (secrets, deps, XSS, CSRF **OK**). Deux manques de config
(headers GAP-022, hardening Auth prod GAP-023) + le rappel conformité mineurs (GAP-003). **Reste S3**
(données perso/INPDP mineurs, backup/DR, rapport final P0-P3).
