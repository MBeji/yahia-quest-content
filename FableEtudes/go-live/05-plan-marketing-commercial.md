# Chantier 05 — Plan marketing & commercial

> Pilotage : [00-MASTER-PLAN.md](./00-MASTER-PLAN.md) · Livrables volumineux : `go-live/livrables/05-marketing/`

| | |
|---|---|
| **Statut** | 🟢 Terminé (S1+S2+S3) — livrables complets ; exécution = Mohamed. ⚠️ **Revu 2026-07-11** : volet « bascule payante » gelé (pivot gratuité — C6 supersédé) ; chantier réorienté **SEO/acquisition gratuite** (cf. C8) |
| **Avancement** | 100 % (livrables) |
| **Dépendances** | Aucune ferme (Phase A) — s'alimente mutuellement avec C6 (segments ↔ pricing) et profite de C1 (valeur produit) |
| **Alimente** | C6 (segments, hypothèses d'acquisition) · C7 (KPIs business) · Checklist Go/No-Go (plan de comm) · **C4 (domaine `na9ranal3ab.tn` choisi → checklist domaine/SMTP déroulable dès l'achat)** |
| **Dernière session** | 2026-06-13 (S1 positionnement/GTM + marque **Na9ra Nal3ab** + S2 acquisition + S3 kit commercial/KPIs) |
| **Prochaine action** | **Exécution (Mohamed)** : ① `na9ranal3ab.tn` acheté — **câbler le domaine** (www/apex, cf. 91-actions B1/B4) puis soumettre le sitemap ; ② dérouler le playbook « école pilote » + page Facebook ; ③ brancher PostHog (C4) pour instrumenter l'entonnoir avant la rentrée. ~~prix + PSP = C6~~ (gelé — pivot gratuité) ; conformité mineurs/pages légales = **C3/C7**. |

## Contexte à charger en début de session
- Ce fichier + `00-MASTER-PLAN.md`
- Synthèse C1 (cartographie/valeur produit) si disponible ; sinon `yahia-quest-arena/CLAUDE.md` §"What this is"
- Chantier business : pas de code à charger

## Objectifs (périmètre validé)
- Définir le positionnement du portail et sa proposition de valeur.
- Identifier les segments de clientèle prioritaires.
- Construire la stratégie d'acquisition (SEO, réseaux sociaux, publicité digitale, influenceurs…).
- Définir les partenariats stratégiques.
- Plan de communication avant et après lancement.
- Définir les indicateurs (CAC, conversion, rétention, engagement…).
- Construire le processus commercial et les argumentaires de vente.
- Stratégie de croissance pour maximiser adoption et usage.

## Livrables attendus
- [x] Document de positionnement + proposition de valeur + messaging (FR + AR) — [S1](./livrables/05-marketing/01-positionnement-segments-timing.md)
- [x] Segmentation priorisée (payeur ≠ utilisateur : parents vs élèves) + personas — [S1](./livrables/05-marketing/01-positionnement-segments-timing.md)
- [x] Plan d'acquisition 90 jours (canaux, budget, calendrier) calé sur le calendrier scolaire tunisien — [S2](./livrables/05-marketing/02-plan-acquisition.md)
- [x] Plan de communication pré-lancement (J-30 → J0) et post-lancement — [S2](./livrables/05-marketing/02-plan-acquisition.md) (calendrier 90 j)
- [x] Plan de partenariats (écoles privées, centres de soutien, influenceurs édu…) — [S2](./livrables/05-marketing/02-plan-acquisition.md) (playbook « école pilote »)
- [x] Kit commercial : argumentaire, FAQ, traitement des objections, offre de lancement — [S3](./livrables/05-marketing/03-kit-commercial-kpis.md)
- [x] Tableau de KPIs avec cibles (CAC, activation, conversion preview→premium, rétention D7/D30, engagement) — [S3](./livrables/05-marketing/03-kit-commercial-kpis.md)

## Découpage proposé (à affiner au kickoff)
- [ ] **1. Positionnement** : « académie gamifiée tunisienne » — différenciation vs cours particuliers, centres de soutien, apps génériques ; trilinguisme et concours comme angles
- [ ] **2. Segments & personas** : parents d'élèves de 9ème / de 6ème (payeurs, décideurs), élèves (utilisateurs, prescripteurs), enseignants/écoles (B2B plus tard) — prioriser
- [ ] **3. Timing marché** : calendrier scolaire TN (rentrée sept = fenêtre n°1, jan–mars = pic révisions avant concours de juin) → caler la date de lancement et les vagues
- [ ] **4. Canaux** : Facebook (groupes parents très actifs en TN), Instagram, TikTok, YouTube édu, SEO FR/AR, influenceurs éducation, bouche-à-oreille beta testers → prioriser par CAC estimé
- [ ] **5. Pré-lancement** : landing + liste d'attente, témoignages beta, présence sociale active avant J0
- [ ] **6. Process commercial** : funnel (découverte → essai gratuit → conversion), relances, rôle du paywall téléphonique actuel vs paiement en ligne (selon décision C6)
- [ ] **7. KPIs & outillage de mesure** (lien C4 analytics) + plan de croissance 12 mois

## Décisions
| Date | Décision | Motif |
|------|----------|-------|
| 2026-06-13 | **Plan kickoff validé** : 3 sessions — S1 positionnement/segments/timing · S2 acquisition + pré-lancement · S3 kit commercial + KPIs | Cadrage chantier |
| 2026-06-13 | **D1 — Fenêtre de lancement : beta été 2026 → public à la rentrée sept 2026 → poussée premium au pic révisions jan-mars 2027** | Aligné calendrier scolaire TN ; construire usage/preuve avant de monétiser |
| 2026-06-13 | **D2 — Premier lancement = beta GRATUITE d'abord**, bascule payante ensuite (séquencée avec C6/PSP) | Réduire la friction, bâtir preuve sociale + liste d'attente, laisser le temps de monter le paiement |
| 2026-06-13 | **D3 — Marque CONFIRMÉE (Mohamed) : « Na9ra Nal3ab » (نقرا نلعب = « j'apprends, je joue »)** — domaine principal **`na9ranal3ab.tn`** (+ `.com` en protection ; les deux libres au sondage DNS). À exécuter en *système* : wordmark Arabizi + script arabe **نقرا نلعب** + signature sérieuse (« programme & concours tunisiens »). Réserver variantes de typo + pseudos sociaux. **Reste opérationnel (non bloquant pour la stratégie) : achat domaine via registrar ATI + check marque INNORPI.** Alternatives explorées et écartées : XP Academy (`.com` pris par tiers, non-ownable), Faris/Najmi (`.tn` seul), Ludisavoir/Na9ra court (ownables mais moins sur-message). | Nom = proposition de valeur en derja, double cible (na9ra=parent / nal3ab=enfant), différenciant, **100 % ownable** (.tn+.com). Remplace le nom de travail « XP Scholars » (anglais, `.com` pris). Vigilances actées : lisibilité Arabizi 9/3, registre très fun → portées par signature + script arabe |
| 2026-07-11 | **D4 — Volet « bascule payante » de D1/D2 GELÉ** (pivot gratuité : C8 2026-06-21 + étude 15 Q-2 2026-07-10 ; C6 supersédé). Le GTM gratuit (école pilote, Facebook, rentrée sept 2026) reste valable tel quel ; le chantier est réorienté SEO/acquisition (cf. C8). | Alignement post-pivot (passe de rationalisation) |

## Journal d'avancement (append-only)
| Date | Fait | Reste / prochaine étape |
|------|------|--------------------------|
| 2026-06-13 | **S3 livrée → C5 terminé (S1+S2+S3).** [Kit commercial & KPIs](./livrables/05-marketing/03-kit-commercial-kpis.md) : argumentaire de vente prêt-à-l'emploi (Problème→Promesse→Preuve→Offre→Action), FAQ parents (12 Q/R), traitement des 7 objections classiques, offre de lancement (beta « Héros Fondateurs » gratuite → premium au pic concours : early-bird + pack famille + satisfait-ou-remboursé + parrainage), tableau KPIs (entonnoir activation, rétention D7/D30, conversion preview→premium 3-7 %, seuils d'alerte), plan de croissance 12 mois (T1 beta/lancement → T2 base/rétention → T3 premium/PSP → T4 scale/preuve). | **Exécution Mohamed** (domaine, école pilote, landing, PostHog). Dépendances : prix/PSP=C6, légal=C3/C7. |
| 2026-06-13 | **Marque tranchée + S2 livrée.** Marque **Na9ra Nal3ab** (نقرا نلعب) confirmée après exploration (XP Academy écarté = non-ownable ; Faris/Najmi/Ludisavoir comparés) — `na9ranal3ab.tn` + `.com` libres. [Plan d'acquisition S2](./livrables/05-marketing/02-plan-acquisition.md) calé sur les inputs réels (budget **1000-2000 TND/an** → organique-first + micro-boosts ; **partenariat école** = canal n°1 avec playbook « école pilote » réplicable ; **Facebook** = moteur parent : page + groupes valeur-d'abord + boosts ciblés ; secondaires TikTok/Insta/WhatsApp/parrainage). Calendrier 90 j (fondations → beta → rentrée). | **S3** (kit commercial + KPIs + croissance 12 mois). Mohamed : réserver domaine/handles + INNORPI ; capacité contenu ; fourchette prix (C6). |
| 2026-06-13 | **Kickoff + S1 livrés.** Plan 3 sessions validé. Ancres D1 (timing beta→rentrée→pic concours) et D2 (beta gratuite d'abord) tranchées par Mohamed. [Livrable S1](./livrables/05-marketing/01-positionnement-segments-timing.md) : positionnement (3 piliers : ancrage TN/concours, l'enfant révise seul avec plaisir, le parent garde la main) + carte concurrentielle + proposition de valeur double (parent payeur / élève prescripteur) + messaging FR/AR + segments priorisés (P1 parent 9ème, P2 parent 6ème, élève prescripteur) + go-to-market 5 phases calé sur l'année scolaire. | **Mohamed : 5 inputs** (marque/domaine, budget, assets/réseau, capacité contenu, fourchette prix — §6 du livrable). Puis **S2** (acquisition 90 j + comm pré-lancement + partenariats). |
