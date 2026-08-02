# Checklist Go/No-Go infra — yahia-quest-arena

> Livrable S3 du chantier [04](../../04-architecture-prod-deploiement.md). Date : 2026-06-12.
> **Grille de décision binaire avant d'ouvrir la beta publique.** Périmètre = infra/déploiement/
> exploitation (chantier 04). Les volets contenu, légal/INPDP, marketing, paiement ont leurs
> propres Go/No-Go (C5/C6/légal) — non couverts ici. Un seul **NO-GO bloquant** rouge = on
> n'ouvre pas. Statuts : ✅ fait · 🟡 prêt, action Mohamed · 🔴 à faire · ⬜ palier ultérieur.
>
> 🔗 **Version finalisée (programme) :** C7/S2 consolide cette grille en un **Go/No-Go à 2 portes**
> (beta gratuite vs lancement payant) + dates recommandées →
> [07-gouvernance/02-roadmap-pilotage-gonogo.md](../07-gouvernance/02-roadmap-pilotage-gonogo.md) §4.

## A. Bloquants — tous ✅ obligatoires pour ouvrir la beta gratuite (palier 0)

| # | Critère | Statut | Preuve / action |
|---|---|---|---|
| A1 | **Le site répond** en prod (landing + login + quête + dashboard) | ✅ | Smoke §4 du [runbook](./runbook-deploiement.md) ; régression login PR #87 corrigée |
| A2 | **Charge beta tenue** avec marge | ✅ | C2/S2 : cibles tenues 9–17× sur tier Free (`charge-resultats.md`) |
| A3 | **Backups opérationnels** (Free n'en a aucun) | ✅ | Dump PROD réel vert (run 27442412600, 2026-06-12) ; nocturne 02:30 UTC armé (secrets validés) |
| A4 | **Restauration testée** (un backup non restaurable ne vaut rien) | ✅ | Drill PROD vert : restauration + 6 invariants OK (4430 questions, 13 comptes…). À rejouer **mensuellement** |
| A5 | **Protection de `main` active** (pas de code rouge en prod) | 🔴 | Importer le ruleset `main-protection.json` (Settings → Rules) — **réglage Mohamed** |
| A6 | **Monitoring uptime + alerte** (savoir quand ça tombe) | ✅ | UptimeRobot UP sur `na9ranal3ab.vercel.app` (5 min) + alerte e-mail branchée (vérifié API, 14/06) |
| A7 | **Capture des erreurs prod** (sinon elles s'évaporent en ~1 h) | 🟡 | SDK Sentry **codé + mergé** (PR #105, dependency-free, EU, no-op sans DSN). Reste : poser `VITE_SENTRY_DSN` en env Vercel → ✅ |
| A8 | **Hardening Auth** (confirmations email, politique mdp, Site URL) | 🔴 | `checklist-auth-hardening.md` (~15 min, dashboard Supabase) |
| A9 | **Pas de secret critique exposé** (`service_role` jamais côté Vercel/`VITE_*`) | 🟡 | À cocher dans la checklist auth §hors-dashboard |
| A10 | **Env vars runtime présentes** en prod (`SUPABASE_URL`, `SUPABASE_PUBLISHABLE_KEY`) | ✅ | Le site tourne → présentes ; documentées (`docs/environment-variables.md`) |

**Verdict A = GO** seulement quand A1–A10 sont ✅. Au 2026-06-12 soir : **6/10 ✅** (A1-A4, A10 +
A9 quasi) — restent **A5-A8 côté Mohamed** (≈ 45 min cumulées : ruleset, UptimeRobot, Sentry,
checklist auth).

## B. Recommandés — devraient être ✅, un 🟡 résiduel est acceptable avec décision explicite

| # | Critère | Statut | Note |
|---|---|---|---|
| B1 | **Analytics produit** (funnel preview→premium) | 🔴 | PostHog Cloud EU → clé → je câble. Pas bloquant pour *ouvrir*, mais aveugle sans lui |
| B2 | **Bouton Google** : configuré OU retiré | 🔴 | Décision Mohamed (checklist auth) — un bouton mort nuit à la confiance |
| B3 | **Tag `v1.0.0`** posé au lancement | 🔴 | Section §5 runbook — à poser quand A = GO |
| B4 | **Previews Vercel par PR** activées | 🟡 | Confort de validation visuelle (gratuit) |
| B5 | **Vercel Analytics** activé (Web Vitals réels) | 🔴 | 1 clic, onglet Analytics du projet |
| B6 | **TTFB Tunisie** acceptable | ✅ | Landing SSR 327 ms moy, mono-région arn1 validée (GAP-029) |

## C. Hors palier 0 — NE PAS bloquer le lancement beta là-dessus (déclencheurs mesurables)

| # | Critère | Déclencheur | Référence |
|---|---|---|---|
| C1 | **Quitter Vercel Hobby** (ToS non-commercial) | 1ʳᵉ vente (même hors-ligne) | Dossier §3 — Vercel Pro 20 $ **vs** Cloudflare natif 0–5 $ |
| C2 | **Domaine custom + SMTP DKIM** | ouverture des ventes / recrutement actif | `checklist-domaine-smtp.md` (~1 h, ~12 $/an) |
| C3 | **Supabase Pro** (backups gérés, pas de pause) | premiers payants OU DB > ~350 Mo | Dossier §2 palier 2 |
| C4 | ~~**CSP nonce** (durcir `unsafe-inline`)~~ | ✅ **FAIT en prod (2026-06-13, `fa2d31d`)** | nonce par-requête, plus d'`unsafe-inline` ; GAP-022 🟢 |
| C5 | **Migration Nitro** (sortir de l'adaptateur custom) | avant palier 1 idéalement | Dossier §4 — lot ~0,5-1 j, débloque Vite 8 |
| C6 | **HIBP** (mots de passe compromis) | passage Pro | checklist auth (si indispo en Free) |
| C7 | **Staging dédié** | paiements en ligne | la beta = staging au lancement |

## D. Synthèse coûts (rappel décision D2 par paliers)

| Palier | Quand | Coût/mois | Ce qu'on ajoute |
|---|---|---|---|
| **0 — Beta** *(maintenant)* | — | **~0 $** | Free+Free + monitoring gratuit + backups DIY |
| **1 — 1ʳᵉ vente** | parcours vendu | **0–20 $** | sortie Hobby (Pro **ou** Cloudflare) + domaine ~12 $/an + Resend free |
| **2 — Payants réels** | DB > ~350 Mo / clients actifs | **25–45 $** | + Supabase Pro |
| **3 — Échelle** | ~1 000+ actifs / p95 submit > 600 ms | **60–120 $** | + compute Supabase, PITR, cache HTTP |

Déclencheurs **mesurables** — pas d'upgrade au feeling. Détail : [dossier §2](./dossier-architecture.md).

## E. Décision Go/No-Go (à dater au lancement)

> **GO** si tous les A sont ✅ et les écarts B sont explicitement acceptés.
> **NO-GO** si un seul A reste 🔴/🟡.

- [ ] Section **A** entièrement ✅ (10/10)
- [ ] Écarts **B** revus et tranchés (✅ ou accepté-documenté)
- [ ] Tag `v1.0.0` posé (B3)
- [ ] Date de décision : `__________` · Décideur : **Mohamed**

**État au 2026-06-12 (soir)** : **NO-GO** (normal — pré-lancement), **6/10 bloquants ✅**.
~~1. 2 secrets GitHub → drill~~ ✅ **fait** : drills TEST + PROD verts, nocturne armé → **A3/A4 ✅**.
Chemin critique restant (≈ 45 min Mohamed + mes lots code) :
2. **UptimeRobot** (10 min, autonome) → **A6 ✅**.
3. **Checklist auth hardening** (15 min) → **A8 + A9 ✅** + tranche B2.
4. **Importer le ruleset `main`** (5 min) → **A5 ✅**.
5. **Compte Sentry** → DSN → **je câble le SDK** → **A7 ✅**.
6. (Recommandé) **PostHog EU** → clé → je câble → **B1 ✅** ; activer Vercel Analytics → **B5 ✅**.
7. Quand A = 10/10 : **poser `v1.0.0`** → **B3 ✅** → **GO**.
