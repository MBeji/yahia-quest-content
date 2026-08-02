# 🚀 MASTER PLAN — Go-Live Na9ra Nal3ab (yahia-quest-arena)

> **Source de vérité du programme « POC → production publique ».**
> Point d'entrée obligatoire de toute session de travail sur le go-live.
> Mis à jour à CHAQUE session (tableau de bord + journal).
> Dernière MAJ : **2026-08-02** (versement sous `FableEtudes/`, élagage, re-vérification des P1).
>
> 📍 **Ce programme vit ici depuis le 2026-08-02.** Il était jusque-là dans le wrapper
> `YahiaAcademy/go-live/`, **hors de tout dépôt git** — donc sans historique, sans revue et
> sans sauvegarde autre que sa copie sur un disque. Il rejoint `FableEtudes/` parce que c'est
> le même métier : de la conception qui se planifie, s'arbitre et se journalise, à côté de la
> [ROADMAP](../ROADMAP.md) et des études.
>
> **Topo central côté moteur** (phase, décisions, état features/études) : `STATUS.md` du dépôt
> `MBeji/yahia-quest-arena` (public) — ouvrir une session ici et l'y ajouter en second checkout.
>
> 🆕 **Nouveau sur le projet ?** Commence par le **[dossier de passation](./PASSATION.md)** — tout le
> projet (produit, business, technique, accès, exploitation) en un seul document.

---

## 1. Objectif du programme

Faire passer Na9ra Nal3ab (académie d'apprentissage gamifiée, marché tunisien — **plateforme
publique 100 % gratuite** depuis le pivot du 2026-06-21 ; premium **dormant**, étude 01 gelée)
d'un POC fonctionnel en beta à un **lancement public maîtrisé** : audité (fonctionnel, technique,
sécurité), industrialisé (prod, monitoring, support), et armé pour l'acquisition
(positionnement, SEO, écoles — ~~pricing~~ gelé avec la monétisation, C6 supersédé).

---

## 2. Protocole de travail — traçabilité & optimisation de contexte

**Règle d'or : toute session doit pouvoir s'arrêter à tout moment sans perte de contexte.**

### Démarrage de session
1. Charger ce fichier (`00-MASTER-PLAN.md`) + le fichier du chantier ciblé (`0X-*.md`) —
   et **seulement** les références listées dans sa section « Contexte à charger ».
2. **Un seul chantier par session** (sauf demande explicite). Ne pas charger les rapports
   des autres chantiers hors dépendance déclarée.
3. Reprendre à la ligne « Prochaine action » du fichier chantier.

### Pendant la session
4. **Planifier avant d'exécuter** : chaque chantier démarre par un kickoff = plan
   d'exécution détaillé **validé par Mohamed** avant toute production.
5. Cocher les cases au fil de l'eau ; consigner toute décision dans la table « Décisions »
   du chantier.
6. Tout constat actionnable (anomalie, risque, manque) → une ligne dans
   [`90-backlog-remediation.md`](./90-backlog-remediation.md) (ID + sévérité + source).

### Fin de session (obligatoire avant de s'arrêter)
7. Dans le fichier chantier : journal (date · fait · reste), statut, **« Prochaine action » explicite**.
8. Dans ce fichier : tableau de bord (§3) + journal global (§7) si événement structurant.

### Optimisation de contexte
- Les fichiers chantiers restent **courts** (pilotage). Les gros livrables vont dans
  `go-live/livrables/0X-<nom>/` et sont seulement **référencés**.
- Le code s'analyse dans le repo (`yahia-quest-arena/`) ; seules les synthèses remontent ici.
- Les remédiations techniques vivent dans le repo (branches/PRs conventionnelles),
  référencées depuis le backlog 90.

---

## 3. Tableau de bord des chantiers

> **Compressé le 2026-08-02** (versement sous `FableEtudes/`). Ce tableau donnait 11 KB de prose
> pour des chantiers clos depuis juin ; chaque ligne renvoie désormais à son fichier, qui garde
> le détail intact. Ce qui est **clos ne se raconte plus ici** — seul l'actionnable descend
> en §3bis.

| #     | Chantier                       | Type         | Statut                                                                                                              | Fichier                                        |
| ----- | ------------------------------ | ------------ | ------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| C1    | Audit fonctionnel              | Produit      | 🟢 **Clos** 2026-06-10 — cartographie, plan de tests, walkthrough ; constats versés au backlog                       | [01](./01-audit-fonctionnel.md)                |
| C2    | Audit technique & architecture | Tech         | 🟢 **Clos** 2026-06-12 — radar 3,31/4, campagne de charge k6, réconciliation de l'audit du 2026-06-01                | [02](./02-audit-technique-architecture.md)     |
| C3    | Cybersécurité bout en bout     | Tech         | 🟢 **Clos** 2026-06-10 — 0 P0 ; revue RLS/RPC + sondes ; a produit GAP-003 et GAP-024                                | [03](./03-audit-cybersecurite.md)              |
| C4    | Architecture prod & déploiement | Tech        | 🟢 **Infrastructure soldée** 2026-07-27 — domaine, Sentry, GA4 + PostHog, ruleset `main`, auth hardening, SMTP Resend, secrets du kill-switch. Reste non technique → §3bis | [04](./04-architecture-prod-deploiement.md)    |
| C5    | Plan marketing & commercial    | Business     | 🟢 **Clos** 2026-06-13 — marque **Na9ra Nal3ab**, positionnement, GTM ; volet prix caduc, réorienté SEO             | [05](./05-plan-marketing-commercial.md)        |
| C6    | Modèle économique & monétisation | Business   | ⚪ **Supersédé** par le pivot gratuit du 2026-06-21 — conservé comme archive de dégel ; véhicule = étude 01 (gelée) | [06](./06-modele-economique-monetisation.md)   |
| C7    | Gouvernance, exploitation & roadmap | Mixte   | 🟢 **Clos** 2026-06-13 — Go/No-Go à 2 portes (§6)                                                                    | [07](./07-gouvernance-exploitation-roadmap.md) |
| C8    | Refonte plateforme publique & gratuite | Produit/Tech | 🟢 **MVP live en prod depuis le 2026-06-22** (PR #180) — 100 % gratuit, trilingue, navigable sans login ; L2.A livré, SEO livré et le domaine répond depuis le 2026-07-27. Reste : post-MVP L3 (enseignant), revert de l'override bêta avant tout retour du premium | [08](./08-refonte-plateforme-publique.md)      |
| 90    | Backlog de remédiation         | Mixte        | 🟡 **34 ouverts / 20 soldés** sur 54 émis · **0 P0** · **3 P1** (GAP-003 INPDP, GAP-024 droits des personnes, GAP-040 contenu 13 niveaux) | [90](./90-backlog-remediation.md)              |
| —     | Journal du programme           | —            | 46 événements + 23 mouvements de backlog, append-only                                                               | [journal](./journal.md)                        |
| —     | Actions côté Mohamed           | —            | Ce qui ne peut pas se faire depuis un dépôt (DNS, comptes tiers, démarches)                                         | [91](./91-actions-mohamed.md)                  |

Statuts : 🔴 non démarré · 🟠 kickoff fait · 🟡 en cours · 🟢 terminé · ⚪ supersédé/abandonné

### 3bis. Ce qui bloque encore la Porte 1 (vérifié le 2026-08-02)

Trois choses, et **aucune n'est technique** :

1. **GAP-003 — conformité mineurs / INPDP.** Le signup ne demande ni âge ni consentement
   parental pour un produit qui vise des 11-15 ans. Demande des décisions humaines (statut
   juridique, modèle de consentement) ; **non vérifiable depuis un dépôt**.
2. **GAP-024 — droits des personnes, à moitié fait.** Les **pages légales existent** depuis la
   PR #701 (`confidentialite`, `conditions`). La **suppression de compte et l'export/portabilité
   n'existent pas** — vérifié dans `src/` le 2026-08-02. Une PR qui cite un GAP dans son titre
   ne le clôt pas : c'est le piège que ce chantier vient de retrouver.
3. **Test à blanc de `rollback-prod.yml`** (`freeze-only` puis `unfreeze`). Les secrets
   `VERCEL_*` ont été posés le 2026-07-27 — le kill-switch était inopérant depuis son écriture.
   Tant que le test n'est pas joué, on ne sait pas s'il fonctionne, on l'espère.

Le reste est du **rituel d'exploitation** à démarrer, pas un blocage : triage hebdomadaire de
`content_reports` + `bug_reports` (consoles `/admin/*` + skill `report-triage`, cf.
[91-actions](./91-actions-mohamed.md) E3).

---

## 4. Phasage & dépendances

```
PHASE A — État des lieux & stratégie (chantiers indépendants, parallélisables)
  C1 Audit fonctionnel ──────────┐
  C2 Audit technique ────────────┼──► alimentent ──► 90-Backlog remédiation
  C3 Audit cybersécurité ────────┘                         │
  C5 Marketing ◄──► C6 Modèle économique                   │
       (segments ↔ pricing s'alimentent mutuellement)      │
                                                           ▼
PHASE B — Décisions & remédiation                   Exécution backlog P0/P1
  C4 Architecture prod  (← C2 risques, ← C3 exigences, ← C6 hypothèses de coûts)
  C6 → décision paiement en ligne → item technique majeur du backlog

PHASE C — Pré-lancement
  C7 Gouvernance & roadmap (← synthèse de tous)
  Checklist Go/No-Go (§6) ──► 🚀 Lancement
```

Dépendances clés :
- **C4 attend** les conclusions de C2 (risques techniques) et C3 (exigences sécu/backup), et les hypothèses de volume/coûts de C6.
- **C5 et C6** se nourrissent mutuellement (segments ↔ pricing) — peuvent avancer en alternance.
- **C7 est le chantier de synthèse** : il ferme le programme et porte la checklist Go/No-Go.
- Les **P0 du backlog bloquent le go-live** par définition.

---

## 5. État des lieux initial (2026-06-10)

**Acquis (forces sur lesquelles capitaliser) :**
- Gate qualité solide : lint zéro-warning, tsc strict, couverture ~93 % (seuil 80), husky, CI GitHub Actions, bundle budget.
- E2E Playwright vs projet Supabase TEST dédié (PR #53).
- Sécurité by-design déjà réelle : RLS partout, RPCs privilégiées REVOKE, middleware CSRF, DOMPurify, rate-limit, logger avec redaction.
- Audits techniques du 2026-06-01 (3 rapports : repo + 2 runs wrapper) — **largement obsolètes** : la plupart des actions critiques sont faites depuis (migration features/, couverture 93 % vs objectif 40 %, DOMPurify, e2e). À réconcilier dans C2, pas à refaire de zéro.
- Modèle premium per-parcours + entitlements + pack famille opérationnel en base (migrations 202606xx).
- Contenu riche : 9ème (math, SVT…), 6ème (math 23 ch. + éveil scientifique 9 ch.), culture G ×3 langues, IQ ×3, anglais A1-B1 + donjon.

**Gaps connus avant audits (présomptions à confirmer, déjà seedés dans le backlog 90) :**
- 💳 Pas de paiement en ligne — paywall hors-ligne (téléphone) + provisioning manuel admin. Stripe indisponible en Tunisie → PSP local à choisir (Konnect, Paymee, Flouci, ClicToPay…).
- 🔭 Pas de monitoring/alerting/observabilité prod outillés (au-delà des logs Vercel/Supabase par défaut). Pas d'analytics produit (rétention, funnels).
- 🧒 Utilisateurs mineurs → conformité INPDP (loi 2004-63) + consentement parental à cadrer.
- 💾 Stratégie backup/restore/DR non formalisée ni testée.
- 🧪 Tests de charge jamais réalisés.
- 🌐 Domaine custom, emails transactionnels, branding prod : à vérifier/configurer.
- 🧹 Double config deploy (Vercel actif + Cloudflare vestige) à trancher. ~20 branches `claude/*` + 6 PRs dependabot à trier.

---

## 6. Checklist Go/No-Go (squelette — à affiner par C7)

- [ ] 0 finding sécurité P0 ouvert (C3)
- [ ] Monitoring + alerting actifs et testés (C4)
- [ ] Backup + restore testé en réel (C4)
- [ ] Test de charge passé sur cibles définies (C2)
- ~~Parcours d'achat opérationnel — en ligne OU process manuel assumé et documenté (C6)~~ ⏸️ **gelé** (pivot gratuité 2026-06-21 ; redevient exigible au dégel de l'étude 01)
- [ ] Conformité données mineurs validée (C3)
- [ ] Domaine + SSL + emails transactionnels prod (C4)
- [ ] Process support + incidents actif (C7)
- [ ] Plan de communication J-7 / J0 / J+7 prêt (C5)
- ~~Pricing + offre publiés (C6)~~ ⏸️ **gelé** (pivot gratuité — aucune offre payante en phase actuelle)

> **Volet infra détaillé** (items C4 ci-dessus : monitoring, backup, domaine/SSL/emails) → grille
> binaire complète A/B/C/D/E dans [`checklist-go-no-go.md`](./livrables/04-architecture-prod/checklist-go-no-go.md)
> + procédure de déploiement/rollback dans [`runbook-deploiement.md`](./livrables/04-architecture-prod/runbook-deploiement.md).
> C7 agrège cette grille avec les volets produit/légal/marketing/paiement.

---

## 7. Journal global

> **Sorti d'ici le 2026-08-02** → [`journal.md`](./journal.md) §1. Les 46 événements y sont
> intacts. Ce fichier garde le **tableau de bord** ; le journal garde la **mémoire**.
