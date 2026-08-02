# Chantier 06 — Modèle économique & plan de monétisation

> ## ⚠️ SUPERSÉDÉ (2026-06-21) — conservé comme archive de travail
>
> Le **pivot stratégique du 2026-06-21** (chantier [C8](./08-refonte-plateforme-publique.md),
> décision « Tout gratuit, paywall retiré, AUCUNE monétisation v1 — supersède C6 ») puis
> l'arbitrage **« gratuité de phase »** (étude 15 Q-2, 2026-07-10 ; migration `20260711100000`
> du 2026-07-11 : `is_premium = false` sur tous les parcours) rendent **caducs** le pricing,
> la grille tarifaire, le plan PSP et le business plan ci-dessous. **Aucune action de ce
> chantier n'est à exécuter.** Si la monétisation revient un jour, le véhicule est l'étude
> [`FableEtudes/01-paiement-en-ligne`](../yahia-quest-arena/FableEtudes/01-paiement-en-ligne/ETUDE.md)
> (**gelée**) — ce dossier servira alors de matière première (TAM, comparatif PSP, grille).
> État global : `yahia-quest-arena/STATUS.md`.

> Pilotage : [00-MASTER-PLAN.md](./00-MASTER-PLAN.md) · Livrables volumineux : `go-live/livrables/06-business-model/`

| | |
|---|---|
| **Statut** | ⚪ **Supersédé par C8** (pivot gratuit 2026-06-21) — était : 🟢 Terminé (S1+S2) |
| **Avancement** | 100 % (livrables, valeur d'archive) |
| **Dépendances** | Aucune ferme (Phase A) — s'alimentait mutuellement avec C5 (segments ↔ pricing) |
| **Alimente** | (historique) C4 (hypothèses volume → coûts) · C5 (offre) · future étude 01 si dégel |
| **Dernière session** | 2026-06-13 (S1 modèle/prix/offre + S2 PSP/business plan 3 ans/KPIs) · clôturé le 2026-07-11 |
| **Prochaine action** | **Aucune** (chantier supersédé — ex-actions ①②③ transférées à l'étude 01, gelée) |

## Contexte à charger en début de session
- Ce fichier + `00-MASTER-PLAN.md`
- Modèle premium existant : `yahia-quest-arena/CLAUDE.md` §"Premium gate" (parcours, entitlements, pack famille, preview gratuite)
- Synthèse C5 (segments) si disponible

## Objectifs (périmètre validé)
- Définir les sources de revenus possibles.
- Évaluer les modèles : Freemium, abonnement, commission, publicité, marketplace, B2B.
- Déterminer la stratégie tarifaire optimale.
- Établir les hypothèses de croissance et de rentabilité.
- Construire un business plan 3 à 5 ans.
- Identifier les KPIs financiers (MRR, ARR, marge, CAC, LTV…).
- Définir la trajectoire de passage à l'échelle.
- Évaluer les besoins futurs (financement, recrutement, infrastructure).

## Livrables attendus
- [x] Comparatif des modèles de revenus avec recommandation (freemium par parcours **confirmé** ; pub/abonnement/B2B/marketplace écartés ou différés) — [S1](./livrables/06-business-model/01-modele-revenus-prix.md)
- [x] Grille tarifaire + structure d'offre (parcours concours, pack famille, offre de lancement) en DT — [S1](./livrables/06-business-model/01-modele-revenus-prix.md) (~69-79 DT cat. / ~39-49 DT lancement, à tester)
- [x] **Décision paiement** : **manuel d'abord** (D17/virement + activation admin) → bascule Konnect/Flouci au seuil de volume ; lot technique au backlog si intégration — [S2](./livrables/06-business-model/02-paiement-businessplan-kpis.md)
- [x] Business plan 3 ans (scénarios bas/moyen/haut) — [S2](./livrables/06-business-model/02-paiement-businessplan-kpis.md) (TAM sourcé ~97k candidats concours ; **xlsx générable sur demande**)
- [x] KPIs financiers + tableau de bord (revenu/cohorte, CAC ~nul, LTV/famille, marge ~90 %) — [S2](./livrables/06-business-model/02-paiement-businessplan-kpis.md)
- [x] Note « passage à l'échelle » : seuils (PSP, infra, 1er recrutement, financement optionnel/Startup Act, B2B) — [S2](./livrables/06-business-model/02-paiement-businessplan-kpis.md)

## Découpage proposé (à affiner au kickoff)
- [ ] **1. État des lieux monétisation** : ce qui est déjà câblé (2 parcours premium, entitlements purchase/beta/gift/family, preview gratuite, provisioning admin manuel, paywall téléphone)
- [ ] **2. Étude de prix marché TN** : cours particuliers, centres de soutien, apps concurrentes — repères de disposition à payer des parents
- [ ] **3. Structure d'offre** : achat one-shot « pack concours année scolaire » vs abonnement mensuel vs hybride ; pack famille ; remises de lancement ; politique année scolaire (expiration des entitlements)
- [ ] **4. Paiement en Tunisie** : panorama PSP (frais, délais, intégration, confiance parents), Stripe indisponible → recommandation ; option assumée « manuel d'abord » (virement/D17 + activation admin) avec critère de bascule
- [ ] **5. Modèles écartés ou différés** : publicité (non — mineurs), marketplace, B2B écoles (piste année 2) — documenter le pourquoi
- [ ] **6. Business plan 3 ans** : TAM (cohortes 6ème/9ème en Tunisie — à sourcer), hypothèses conversion/rétention (avec C5), coûts (avec C4) → scénarios
- [ ] **7. KPIs & seuils de scaling**

## Décisions
| Date | Décision | Motif |
|------|----------|-------|
| 2026-06-13 | **Plan kickoff validé** : 2 sessions — S1 modèle/prix/offre · S2 PSP + business plan + KPIs | Cadrage chantier |
| 2026-06-13 | **D1 — Facturation : pack one-shot « année scolaire »** (par parcours, entitlement à expiration annuelle), **pas d'abonnement mensuel** | Aligné objectif concours + habitudes de paiement TN (paiement unique préféré) ; revenu re-récurrent par cohortes sans friction du récurrent |
| 2026-06-13 | **D2 — Paiement au lancement = manuel d'abord** (D17/virement + activation admin, déjà câblé) ; PSP en ligne intégré une fois le volume prouvé | Valider la disposition à payer avant le lot technique + frais ; le code support déjà le provisioning manuel |
| 2026-06-13 | **D3 — Statut légal « à cadrer » → recommandation auto-entrepreneur** avant bascule premium (jan 2027) | Prérequis dur pour encaisser légalement ; la beta gratuite ne le nécessite pas → temps disponible. Porté avec C7 + Go/No-Go payant |

## Journal d'avancement (append-only)
| Date | Fait | Reste / prochaine étape |
|------|------|--------------------------|
| 2026-06-13 | **S2 livrée → C6 terminé (S1+S2).** [Paiement/business plan/KPIs](./livrables/06-business-model/02-paiement-businessplan-kpis.md) : panorama PSP TN (Konnect 1,6 % sans setup = reco intégration ; Flouci/Paymee ; D17 pour le manuel) + **critère de bascule** manuel→en ligne (>~15-20 activ./sem) ; **TAM sourcé** (169k inscrits 9ème / 33k candidats concours / 64k candidats 6ème — ~97k cœur de cible, 3 750+3 850 places = rareté = disposition à payer) ; **business plan 3 ans** scénarios bas/moyen/haut (moyen : An1 ~15k / An2 ~60k / An3 ~175k DT, marge ~90 %, bootstrappable) ; KPIs (revenu/cohorte, CAC ~nul, LTV/famille via fratrie+élargissement) ; seuils de scaling (PSP, infra C4, 1er recrutement, financement optionnel/Startup Act, B2B An2+). | **Exécution Mohamed** (auto-entrepreneur, tests prix beta, PSP au seuil). xlsx générable sur demande. Légal = C3/C7. |
| 2026-06-13 | **Kickoff + S1 livrés.** Plan 2 sessions validé. Ancres D1 (one-shot année), D2 (manuel d'abord), D3 (auto-entrepreneur à ouvrir) tranchées. [Livrable S1](./livrables/06-business-model/01-modele-revenus-prix.md) : modèle freemium par parcours **confirmé** (alternatives pub/abonnement/B2B/marketplace écartées ou différées avec motifs) ; **étude prix marché TN** sourcée (cours particuliers 35-150 DT/séance, marché ~1,5-3 Md DT/an ; Takiacademy = réf. abonnement + remises fratrie ; plateformes gratuites = menace → différenciation engagement) ; structure d'offre (pack concours année + pack famille + offre Fondateurs + satisfait-ou-remboursé) ; **grille tarifaire recommandée ~69-79 DT catalogue / ~39-49 DT lancement** (à tester en beta) ; prérequis légal documenté. | **S2** (PSP + business plan 3 ans + KPIs financiers + scaling). Mohamed : ouvrir auto-entrepreneur ; tester 2-3 prix en beta. |
