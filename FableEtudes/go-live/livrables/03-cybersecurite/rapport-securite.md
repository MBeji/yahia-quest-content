# C3 — Rapport d'audit cybersécurité (final, 2026-06-10)

> Livrable de clôture du chantier [03-audit-cybersecurite](../../03-audit-cybersecurite.md).
> S'appuie sur [findings-log.md](./findings-log.md) (sondes dynamiques sur TEST + S2),
> [rls-rpc-review.md](./rls-rpc-review.md) (revue statique RLS/RPC) et le [plan](./plan-audit-securite.md).
> Méthode : revue de code/SQL + **sondes d'exploit réelles** (PostgREST authentifié) sur le projet
> Supabase **TEST** ; conformité & backup analysés sur pièces. Findings → backlog 90 (GAP-NNN).

---

## 1. Synthèse exécutive

**La sécurité applicative est globalement solide — bien meilleure que la moyenne d'un POC.** Les
vecteurs d'attaque graves ont été testés en conditions réelles et sont **tous bloqués** : pas
d'élévation de privilège, pas d'auto-octroi du premium (donc pas de contournement de paiement), pas
d'accès aux données d'autres utilisateurs (IDOR), pas de mint d'XP/coins, secrets serveur protégés,
dépendances sans vulnérabilité connue, XSS sanitizé, CSRF actif, RLS et RPCs SECURITY DEFINER
correctement durcis (`search_path`, REVOKE des fonctions sensibles, aucune injection SQL).

**Trois zones à traiter avant l'ouverture grand public :**
1. **Intégrité du gameplay et du contenu (technique, P1)** — quelques tables de gameplay sont restées
   inscriptibles en direct et le corrigé des questions est lisible par le client. Un utilisateur peut
   tricher (leaderboard, quiz gate) et lire la banque de réponses. **Correctif simple et groupé.**
2. **Conformité données personnelles de mineurs (juridique/produit, P1)** — le produit cible des
   11-15 ans mais ne collecte aucun consentement parental, n'a pas de politique de confidentialité,
   ni de mécanisme d'effacement/export de compte. **Obligation avant ouverture (INPDP loi 2004-63).**
3. **Durcissement de configuration (P2)** — aucun en-tête de sécurité HTTP ; réglages Auth prod et
   stratégie de sauvegarde/restauration à finaliser sur les dashboards (→ C4).

**Verdict** : **aucun P0 de compromission**. Les risques sont des trous d'intégrité (cheap à corriger)
et des obligations de conformité/config. La base sécurité est saine ; il reste un sprint de
remédiation ciblé, sans refonte.

---

## 2. Registre des risques (P0–P3)

| ID | Risque | Sév. | État | Domaine |
|----|--------|------|------|---------|
| GAP-020 | Banque de réponses (`questions.correct_option`) lisible par tout user ; contenu premium lisible sans entitlement | **P1** | 🔴 | Intégrité contenu |
| GAP-016 | Forge directe de `attempts` (xp/score) → leaderboard, quiz gate, prérequis donjon | **P1** | 🔴 | Intégrité gameplay |
| GAP-003 | Conformité mineurs/INPDP : pas de consentement parental, registre des traitements absent | **P1** | 🔴 | Conformité |
| GAP-024 | Pas de politique de confidentialité/CGU, ni effacement/export de compte (droits des personnes) | **P1** | 🔴 | Conformité/produit |
| GAP-021 | Écritures gameplay non révoquées (`exercise_sessions`, `daily/weekly`, `difficulty`, `spaced_rep`) | P2 | 🔴 | Intégrité gameplay |
| GAP-022 | Aucun en-tête de sécurité HTTP (CSP/HSTS/X-Frame…) | P2 | 🔴 | Config |
| GAP-023 | Hardening Auth prod à vérifier (mdp, HIBP, SMTP, OAuth, MFA) — dashboard | P2 | 🔴 | Config (→C4) |
| GAP-004 | Backup/restore/DR non formalisé ni testé (PITR ?) | P2 | 🔴 | Continuité (→C4) |
| GAP-015 | Alliance Code = UUID brut de l'élève (identifiant interne exposé) | P3 | 🔴 | Vie privée |
| GAP-014 | Rate-limit fail-open local (par instance) en cas de panne du RPC | P3 | 🔴 | Robustesse |

*Aucun P0.* Détail technique de chaque item : [findings-log.md](./findings-log.md).

---

## 3. Ce qui est solide (à préserver)

- **Contrôle d'accès** : RLS sur 27 tables, SELECT scopée (own/linked/admin) → IDOR bloqué (vérifié).
  Écritures sensibles (`profiles` xp/coins/role, `parcours_entitlements`, `parent_student_links`,
  `inventory_items`, `student_badges`) **révoquées** à `authenticated` (vérifié 403 sur 5 sondes).
- **RPCs** : 44 fonctions SECURITY DEFINER, **toutes** avec `search_path` fixé, **aucune injection SQL**,
  mints (`award_xp`/`award_coins`) révoqués, `admin_*` gardées par `is_admin()`.
- **App** : secrets serveur-only, `npm audit` 0 vuln, XSS sanitizé (DOMPurify + profil SVG + React),
  CSRF actif, validation zod systématique, logger avec redaction des secrets.
- **Anti-triche serveur** : scoring/donjon serveur-autoritatifs (correction jamais renvoyée par le
  donjon, anti-double-reward, gates anti-rush) — quand on passe par les RPC.

---

## 4. Données personnelles & conformité (mineurs / INPDP loi 2004-63)

**Inventaire des PII collectées :**
| Donnée | Où | Sensibilité |
|---|---|---|
| Email | `auth.users` | PII directe |
| Nom affiché (`display_name`) | `profiles` | PII (souvent prénom/nom réel) |
| Données d'apprentissage & comportement (xp, niveau, streak, temps total, tentatives, sessions, difficulté) | `profiles`, `attempts`, `exercise_sessions`, `daily/weekly`, `dungeon_*`, `spaced_rep` | **Sensible — profilage de mineurs** |
| Relations familiales (`relation_label`) | `parent_student_links` | PII |
| Demandes beta (nom, email, motivation libre) | `beta_access_requests` | PII |
| Messages libres de signalement | `content_reports` | PII potentielle |
| **Données financières / CB** | — | **Aucune** (paiement manuel hors plateforme) ✅ |

**Constats de conformité (P1) :**
- **Aucun consentement parental** : signup sans champ âge/date de naissance ni recueil de consentement
  (grep exhaustif → rien). Le rôle « parent » existe mais n'est pas un mécanisme de consentement.
- **Aucune politique de confidentialité / CGU / mentions légales** (aucune route /privacy, /terms).
- **Aucun droit des personnes outillé** : pas de suppression de compte (l'app n'a ni page profil ni
  flux de suppression — cf. C1 A-3), pas d'export/portabilité, pas de « droit à l'effacement ».
- **Registre des traitements** : absent.

**Exigences avant ouverture (à instruire en remédiation) :**
1. Page **politique de confidentialité** (FR/AR) + CGU, adaptées aux mineurs, accessibles depuis la
   landing et le signup.
2. **Consentement parental** : onboarding piloté par le parent OU case de consentement explicite +
   âge déclaré ; tracer le consentement (date, par qui).
3. **Effacement & export** : flux de suppression de compte (purge `auth.users` + cascade des données
   liées) et export des données de l'élève sur demande.
4. **Registre des traitements** (finalités, durées de conservation, sous-traitants : Supabase/Vercel).
5. Déclaration/conformité **INPDP** selon le statut juridique du projet.

> Ces points relèvent en partie du **juridique** : ils nécessitent une validation/décision de Mohamed
> (voir §7). L'audit constate et cadre ; il ne se substitue pas à un conseil juridique.

---

## 5. Sauvegarde / reprise (backup / DR)

- **État** : non formalisé. La capacité réelle dépend du **plan Supabase** du projet prod (Free =
  sauvegardes quotidiennes à rétention courte, **pas de PITR** ; Pro = PITR + rétention configurable).
  Non vérifiable par le code — **dépend du dashboard / de Mohamed**.
- **Exigences (→ C4)** : (1) confirmer le plan et activer **PITR** (ou exports programmés) ; (2)
  définir RPO/RTO cibles ; (3) **drill de restauration réel** documenté (restaurer un snapshot sur un
  projet jetable, vérifier l'intégrité) ; (4) sauvegarde du contenu (déjà versionné en `content/` + git
  → bon point) et des migrations (git). GAP-004.

---

## 6. Plan de correction priorisé

**Lot 1 — Intégrité (technique, 1 migration + 1 ajustement requête) — avant lancement**
- GAP-020 : retirer `correct_option` de la projection client (vue/colonne masquée ; corrigé via RPC).
- GAP-016 + GAP-021 : `REVOKE INSERT/UPDATE/DELETE … FROM authenticated` sur `attempts`,
  `exercise_sessions`, `daily_objectives`, `weekly_quests`, `difficulty_adaptation`,
  `spaced_repetition_schedule` (écritures via RPC SECURITY DEFINER uniquement — recette déjà appliquée
  à `inventory_items`/`student_badges`). **Vérifier** que les server fns n'écrivent pas ces tables en
  direct avec le JWT user (sinon basculer ces écritures dans des RPC). Effort faible, impact élevé.

**Lot 2 — Conformité mineurs (juridique + produit) — avant lancement**
- GAP-003 + GAP-024 : politique de confidentialité, consentement parental, suppression/export de
  compte, registre. (Décisions Mohamed requises — §7.)

**Lot 3 — Durcissement config (→ C4) — avant/au lancement**
- GAP-022 : en-têtes de sécurité (`vercel.json`). GAP-023 : hardening Auth prod (dashboard). GAP-004 :
  backup/PITR + drill.

**Lot 4 — Défense en profondeur (post-lancement)**
- GAP-015 (régénérer/masquer l'Alliance Code). GAP-014 (rate-limit distribué).

**Ce que je peux exécuter** : Lot 1 (migration + requête, avec DoD repo), GAP-022 (headers vercel.json),
ébauche des pages légales. **Ce qui dépend de Mohamed / externe** : décisions juridiques (Lot 2),
réglages dashboards Supabase/Vercel (GAP-023/004), éventuel **pentest tiers**.

---

## 7. Recommandation Go/No-Go sécurité & questions à Mohamed

**Recommandation** : la sécurité **ne bloque pas** le go-live au sens « faille critique » — aucun P0.
Mais **deux conditions** devraient être remplies avant ouverture publique : (a) le Lot 1 (intégrité,
rapide) ; (b) un socle de conformité mineurs minimal (politique de confidentialité + consentement +
suppression de compte). Le reste (headers, backup, hardening Auth) est à caler avec C4.

**Questions ciblées (pour la remédiation, pas pour l'audit) :**
1. **Statut juridique** du projet (personne physique / société ?) et existe-t-il déjà une politique de
   confidentialité / des CGU, ou faut-il les créer ?
2. **Plan Supabase prod** actuel (Free/Pro) — pour savoir si PITR est disponible (backup/DR).
3. Souhaites-tu un **pentest externe** tiers avant lancement, ou l'audit interne suffit pour la v1 ?
4. Modèle de **consentement** voulu : onboarding piloté par le parent, ou case de consentement + âge ?

---

## 8. Conclusion

C3 est **terminé**. Le code est sécurisé sur les vecteurs graves — c'est une vraie force pour un POC.
Le travail restant est **ciblé et non structurel** : un correctif d'intégrité technique simple (Lot 1),
un socle de conformité mineurs (Lot 2, à décider avec toi), et du durcissement de configuration (Lot 3,
avec C4). Aucun blocage de type « faille critique » ; le programme peut avancer, avec ces lots inscrits
au backlog comme conditions de lancement.
