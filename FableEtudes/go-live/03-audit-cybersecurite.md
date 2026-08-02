# Chantier 03 — Audit cybersécurité de bout en bout

> Pilotage : [00-MASTER-PLAN.md](./00-MASTER-PLAN.md) · Livrables volumineux : `go-live/livrables/03-cybersecurite/`

| | |
|---|---|
| **Statut** | 🟢 Terminé (S1 + S2 + S3) |
| **Avancement** | 100 % |
| **Dépendances** | Aucune (Phase A) |
| **Alimente** | Backlog 90 (GAP-003/004/014/015/016/020/021/022/023/024) · C4 (headers, Auth prod, backup/DR) · C7 (runbook incident) |
| **Dernière session** | 2026-06-10 — S1+S2+S3, rapport final livré |
| **Prochaine action** | **C3 livré.** [Rapport final](./livrables/03-cybersecurite/rapport-securite.md) : aucun P0, 4 P1 (intégrité GAP-016/020 + conformité GAP-003/024). Conditions sécu de lancement = Lot 1 (intégrité, exécutable) + socle conformité mineurs (décisions Mohamed §7). Réponses attendues de Mohamed : statut juridique, plan Supabase, pentest tiers ?, modèle de consentement. |

## Contexte à charger en début de session
- Ce fichier + `00-MASTER-PLAN.md`
- `yahia-quest-arena/CLAUDE.md` (modèle d'auth, RPCs, RLS) + `docs/xss-rendering-policy.md`
- Selon la tâche : `supabase/migrations/` (policies RLS), `src/shared/integrations/supabase/auth-middleware.ts`, `src/start.ts` (CSRF), branche `claude/security-p0-hardening` (vérifier si mergée)

## Objectifs (périmètre validé)
- Revue complète de la sécurité : application, infrastructure, API.
- Vérifier authentification, autorisation, gestion des accès.
- Tests de vulnérabilité et, si possible, pentest.
- Contrôler la protection des données personnelles et sensibles.
- Vérifier la conformité réglementaire applicable.
- Évaluer sauvegarde, reprise après incident, continuité d'activité.
- Produire un plan de correction des risques **avant ouverture au grand public**.

## Livrables attendus
- [ ] Rapport de risques classés P0–P3 (P0 = bloquant go-live)
- [ ] Revue RLS/authz table par table + revue des RPCs SECURITY DEFINER
- [ ] Résultats tests de vulnérabilité (passe OWASP Top 10) ± pentest
- [ ] Dossier conformité données personnelles (mineurs, INPDP/loi 2004-63, consentement parental)
- [ ] Plan backup/DR validé (exigences transmises à C4) + restore testé
- [ ] Plan de correction priorisé → versé au backlog 90

## Plan d'exécution (kickoff validé — détail : [plan-audit-securite.md](./livrables/03-cybersecurite/plan-audit-securite.md))

- [x] **S1 — Authz / RLS / RPC** : revue exhaustive 53 policies + 44 fonctions SECURITY DEFINER ([rls-rpc-review.md](./livrables/03-cybersecurite/rls-rpc-review.md)) + **sondes d'exploit dynamiques sur TEST** ([findings-log.md](./livrables/03-cybersecurite/findings-log.md), harnais `tools/probe*.py`). Résultat : posture solide sur les vecteurs graves ; risque résiduel = intégrité gameplay/contenu (GAP-016/020/021).
- [x] **S2 — Surface app/API/infra** : ✅ secrets/service-role (server-only), `npm audit` (0 vuln), XSS (DOMPurify + sanitizeSvg + React), CSRF actif → **OK**. ❌ headers (GAP-022), ⚠️ rate-limit fail-open (GAP-014), ⚠️ Auth prod à durcir (GAP-023), conformité mineurs (GAP-003). Mapping OWASP Top 10 dans [findings-log.md](./livrables/03-cybersecurite/findings-log.md).
- [x] **S3 — Données perso, conformité, continuité + synthèse** : ✅ inventaire PII (pas de données financières), conformité mineurs/INPDP (GAP-003 confirmé : ni âge ni consentement), droits des personnes/pages légales (GAP-024), posture backup/DR (GAP-004 → C4). **[Rapport final P0-P3](./livrables/03-cybersecurite/rapport-securite.md)** : aucun P0, plan de correction en 4 lots, questions juridiques/dashboard pour Mohamed.

> Outils d'audit : `livrables/03-cybersecurite/tools/probe.py` + `probe2.py` (sondes PostgREST authentifiées, garde anti-prod), réutilisent l'env TEST de C1.

## Décisions
| Date | Décision | Motif |
|------|----------|-------|
| 2026-06-10 | **Kickoff validé (GO)** par Mohamed : périmètre, sondes d'exploit sur TEST autorisées, découpage S1-S3. | Validation explicite |

## Journal d'avancement (append-only)
| Date | Fait | Reste / prochaine étape |
|------|------|--------------------------|
| 2026-06-10 | Kickoff rédigé ([plan d'audit](./livrables/03-cybersecurite/plan-audit-securite.md)). Grounding : 91 migrations · 44 RPCs SECURITY DEFINER · 53 policies RLS · 27 tables RLS. GAP-016 confirmé en statique (policy insert `attempts` jamais révoquée) ; nouveau candidat : aucun header de sécurité HTTP ; CSRF présent. Périmètre « ce que je peux faire vs ce qui dépend de toi/externe » cadré. | Validation Mohamed → S1 |
| 2026-06-10 | **S1 fait (GO validé).** Revue statique exhaustive (agent) des 53 policies + 44 fonctions SECURITY DEFINER + sondes d'exploit dynamiques sur TEST (`probe.py`/`probe2.py`). **Posture solide** : élévation de rôle, auto-octroi premium, IDOR, mints XP/coins, auto-lien — **tous bloqués/vérifiés** (✅). **5 findings** : F-301 forge attempts (P1), F-305 corrigé/contenu premium exposés (P1), F-302 écritures gameplay (P2), F-303 headers (P2), F-304 alliance code (P3). GAP-020/021/022 ajoutés, GAP-016 confirmé, GAP-015 réévalué. | S2 (surface app/API/infra, OWASP, Auth mineurs) |
| 2026-06-10 | **S2 fait.** Secrets/service-role server-only ✅, `npm audit` 0 vuln ✅, XSS sanitizé (DOMPurify + sanitizeSvg + React) ✅, CSRF ✅. Manques : aucun header HTTP (GAP-022), rate-limit fail-open local (GAP-014), Auth prod à durcir (GAP-023 nouveau), **aucun champ âge/consentement parental au signup** (confirme GAP-003 mineurs). Mapping OWASP Top 10 fait : faiblesses = A01/A04/A08 (intégrité) + A05 (config/headers). | S3 : conformité mineurs/INPDP + backup/DR + rapport final |
| 2026-06-10 | **S3 fait — C3 TERMINÉ.** Inventaire PII (email, display_name, données comportementales mineurs, relations ; **pas de données financières** ✅). Conformité : pas de politique de confidentialité/CGU, pas de consentement parental, pas de suppression/export de compte → GAP-003 confirmé + GAP-024 ajouté (P1). Backup/DR → GAP-004 (dépend plan Supabase). **Rapport final livré** : aucun P0 ; conditions sécu de lancement = Lot 1 (intégrité, exécutable par moi) + socle conformité mineurs (décisions Mohamed). | C3 clos — 4 questions à Mohamed (§7 rapport) |
