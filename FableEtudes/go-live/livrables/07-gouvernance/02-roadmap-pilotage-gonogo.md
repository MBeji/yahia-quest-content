# S2 — Roadmap, pilotage & Go/No-Go finalisé — Na9ra Nal3ab

> Livrable S2 (clôture du programme) du chantier [07](../../07-gouvernance-exploitation-roadmap.md).
> Date : 2026-06-13. **Synthèse de C1→C6.** Referme le go-live : roadmap 3-12 mois, tableau de bord
> de pilotage, rituel d'amélioration continue, et **Go/No-Go finalisé à 2 portes + dates**.

---

## 1. Roadmap produit 3-12 mois (consolidée)

Fil narratif (C5/C6) : **beta gratuite → lancement public à la rentrée → bascule premium au pic
concours → scale.** Chaque horizon a ses **must-do gating**.

### Horizon 1 — Maintenant → rentrée (juin-août 2026) · *préparer le lancement gratuit*
- **Fermer la Porte 1 (beta)** : monitoring (UptimeRobot/Sentry/PostHog), ruleset `main`, hardening
  Auth — *~45 min Mohamed + mes lots code* (GAP-002/008/023).
- **Domaine + SMTP** : réserver `na9ranal3ab.tn` + dérouler la [checklist domaine/SMTP](../04-architecture-prod/checklist-domaine-smtp.md) (GAP-006).
- **Légal minimal** : pages **CGU + confidentialité** + bases conformité **mineurs/INPDP**
  (GAP-024/003) — prérequis d'un site public visant des collégiens.
- **Contenu** : compléter/auditer les parcours **9ème** (prêt) et **6ème** (à compléter).
- **Beta** : landing + liste d'attente + playbook **école pilote** (C5).

### Horizon 2 — Rentrée → décembre 2026 (sept-déc) · *grandir gratuitement*
- **Lancement public gratuit** (rentrée) + tag **v1.0.0**.
- **Rétention** : push-notifs (déjà en prod), défis, contenu régulier ; mesurer l'entonnoir (PostHog).
- **Préparer le payant** : ouvrir **auto-entrepreneur**, **tester 2-3 prix** en beta, exécuter
  `close-premium.sql` (retirer l'override test-phase), décider PSP (manuel d'abord).
- **Dette tech (idéalement ici)** : **migration Nitro** (GAP-007, sort de l'adaptateur custom,
  débloque Vite 8) — fenêtre calme avant le pic.

### Horizon 3 — Janvier → mars 2027 · *lancement premium (pic concours)*
- **Bascule premium** : offre de lancement « Fondateurs », conversion preview→premium.
- **Sortir de Vercel Hobby** dès la 1ʳᵉ vente (ToS) : Vercel Pro **ou** Cloudflare natif (dossier C4 §3).
- **Supabase Pro** quand premiers payants/données clients (palier 2).
- **PSP en ligne** (Konnect/Flouci) **si** le volume manuel le justifie.

### Horizon 4 — Avril → juin 2027 · *scale & preuve*
- **Témoignages de réussite** au concours de juin → carburant de la cohorte suivante.
- **Élargir l'académie** : langues / culture G / muscle-cerveau (rétention hors-saison, LTV).
- **B2B** : pilotes écoles/centres (revente) après preuve B2C.
- Préparer la **rentrée 2027** (cohorte suivante).

### Vision 12 mois+ (différé, non gating)
Mobile natif (la PWA couvre l'essentiel), nouveaux niveaux (Bac ?), marketplace contenu parent,
plus de partenariats B2B.

---

## 2. Tableau de bord de pilotage (3 axes)

> Une **revue mensuelle** + un **coup d'œil hebdo**. Outils : PostHog (produit/funnel), UptimeRobot
> (dispo), Sentry (erreurs), Supabase Reports (DB), suivi manuel des ventes (phase manuelle).

| Axe | KPIs | Source | Cible/seuil (rappel) |
|---|---|---|---|
| **Business** (C5/C6) | clients payants/cohorte · revenu · **conversion preview→premium** · CAC · attach pack famille | suivi manuel + PostHog | conv. **3-7 %** · CAC ~nul |
| **Produit** | activation (onboarding/1ʳᵉ quête) · DAU/WAU · quêtes/sem · **rétention D7/D30** · streak | **PostHog** | activation > 70 % · D7 ≥ 25-30 % · D30 ≥ 15 % |
| **Technique** | uptime · taux d'erreur · p95 (submit/dashboard) · succès déploiement | UptimeRobot · Sentry · C2 | uptime > 99 % · p95 submit < 1 s |

**Seuils d'alerte** (déjà actés) : activation-1 < 50 % → revoir onboarding ; D7 < 15 % → boucle
d'engagement avant de dépenser en acquisition ; p95 submit > 600 ms soutenu → palier infra (C4).

---

## 3. Rituel d'amélioration continue (calibré bande passante variable)

**Boucle : feedbacks → backlog → releases.**
- **Hebdo (léger)** : triage support (WhatsApp/Messenger) + `content_reports` + coup d'œil KPIs.
- **Mensuel (revue)** : funnel + rétention (PostHog) · top `content_reports` · thèmes support ·
  incidents du mois → **re-prioriser le backlog** (valeur/effort) → planifier 1-2 releases.
- **Canaux de feedback** : `content_reports` (erreurs contenu, déjà câblé) · support (besoins,
  objections) · analytics (comportement réel) · beta-fondateurs (retours qualitatifs).
- **Exécution** : Claude Code produit (contenu via skills, code DoD) ; Mohamed valide/merge.

---

## 4. Go/No-Go finalisé — **2 portes**

Le programme distingue **deux lancements** avec des exigences différentes. Détail infra : [checklist
Go/No-Go C4](../04-architecture-prod/checklist-go-no-go.md).

### 🚪 Porte 1 — **Beta publique GRATUITE** (cible : rentrée sept 2026)
*Exigence = technique + légal minimal. Pas de paiement, donc pas de prérequis fiscal.*

| Domaine | État | Reste |
|---|---|---|
| **Infra (A1-A10)** | 6/10 ✅ | A5 ruleset · A6 UptimeRobot · A7 Sentry · A8 auth — *~45 min Mohamed + mes lots* |
| **Sécurité** | solide (C3, 0 P0) · **CSP nonce ✅ en prod** | RAS bloquant |
| **Domaine + SMTP** | nom choisi (`na9ranal3ab.tn`) | réserver + dérouler checklist (GAP-006) |
| **Légal mineurs minimal** | 🔴 | CGU + confidentialité + bases INPDP (GAP-024/003) |
| **Contenu** | 9ème prêt | compléter 6ème ; audit |
| **Tag v1.0.0** | 🔴 | au lancement |

→ **GO beta** réaliste avant la rentrée : il reste surtout des **actions courtes Mohamed** + 2 lots
code (monitoring) + les **pages légales**.

### 🚪 Porte 2 — **Lancement PAYANT** (cible : pic concours jan-mars 2027)
*Ajoute le commercial + le fiscal + le durcissement.*

| Domaine | État | Reste |
|---|---|---|
| **Statut pour encaisser** | 🔴 « pas encore » | ouvrir **auto-entrepreneur** (C6) |
| **Prix figé** | grille proposée | **tester en beta** puis figer (C6) |
| **Flux paiement** | manuel **déjà câblé** | valider le flux D17 + activation ; PSP si volume |
| **`close-premium.sql`** | 🔴 | **retirer l'override test-phase** avant toute vente |
| **Quitter Vercel Hobby** | 🔴 | dès la 1ʳᵉ vente (ToS) — Pro ou Cloudflare (C4 §3) |
| **Conformité mineurs complète** | 🔴 | consentement parental + registre (GAP-003) |

→ **GO payant** = un cran plus exigeant (légal/fiscal). La **beta gratuite achète le temps** de tout
mettre en place d'ici janvier.

### Recommandation de dates
| Jalon | Date recommandée | Condition |
|---|---|---|
| **Beta élargie** | **maintenant → été 2026** | rien de bloquant (gratuit, override test-phase déjà ouvert) |
| **Lancement public gratuit** | **rentrée — début sept 2026** | **Porte 1** ✅ |
| **Bascule premium** | **janvier 2027** (pic révisions) | **Porte 2** ✅ |

---

## 5. Bilan du programme go-live

| Chantier | État |
|---|---|
| C1 Audit fonctionnel · C2 Technique · C3 Sécurité | 🟢 |
| C5 Marketing · C6 Monétisation · **C7 Gouvernance** | 🟢 |
| C4 Architecture prod | 🟡 92 % (Go/No-Go infra : ~45 min Mohamed + lots monitoring) |

**Le socle est prêt.** Ce qui reste pour ouvrir la beta n'est plus de la *conception* mais de
l'**exécution courte** (réglages Mohamed, 2 lots code monitoring, pages légales, domaine). Tout est
outillé, tracé, et séquencé. La **prochaine action concrète** : dérouler le chemin critique de la
**Porte 1** (checklist Go/No-Go) pour viser la rentrée.
