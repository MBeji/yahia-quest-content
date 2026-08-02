# S2 — Paiement, business plan 3 ans & KPIs financiers — Na9ra Nal3ab

> ⚠️ **SUPERSÉDÉ (pivot gratuit du 2026-06-21 + gratuité de phase 2026-07-10/11)** — aucune
> monétisation en phase actuelle ; document conservé comme matière première pour l'étude 01
> (paiement en ligne, gelée). Voir la bannière du chantier [06](../../06-modele-economique-monetisation.md).

> Livrable S2 (clôture) du chantier [06](../../06-modele-economique-monetisation.md). Date :
> 2026-06-13. Ancres : pack one-shot année · **paiement manuel d'abord** · auto-entrepreneur à
> ouvrir. Prix net moyen retenu pour la modélisation : **~50 DT/pack** (mix catalogue ~69-79 DT /
> lancement ~39-49 DT / remises famille). **Projections = scénarios illustratifs**, pas des
> promesses ; à recaler sur les vraies données beta (PostHog, C4).

---

## 1. Panorama des moyens de paiement en Tunisie

Contexte : **Stripe indisponible** en Tunisie. Deux familles de solutions.

### a) Phase « manuel d'abord » (au lancement premium — déjà câblée)
- **D17 / e-Dinar (La Poste)** : paiement mobile **très répandu** (y compris non-bancarisés) →
  reach maximal côté parents. Le parent paie, tu **actives l'entitlement** (provisioning admin).
- **Virement bancaire** : pour ceux qui préfèrent.
- **Avantage** : zéro lot technique, démarrage immédiat, **valide la disposition à payer réelle**.
- **Limite** : pas de self-service, gestion manuelle (chaque activation à la main).

### b) PSP en ligne (quand le volume le justifie)
| PSP | Frais (local) | Setup | Notes |
|---|---|---|---|
| **Konnect** | **1,6 %** + 2 DT/payout | **0** (pas d'abonnement ni frais d'inscription) | Pricing transparent, API dev-friendly → **recommandé pour l'intégration** |
| **Flouci** | bas coût (~1,x %) | léger | Populaire PME/freelances, UX moderne, confiance |
| **Paymee** | ~modeste | léger | Établi depuis 2017, intégration simplifiée |
| **ClicToPay (SMT/monétique)** | frais bancaires | lourd | Passerelle carte bancaire « classique », plus bureaucratique |
| *(repère général)* | ~1,3-1,6 % cartes locales / e-Dinar ; ~2,9 % international | | |

**Recommandation paiement** :
1. **Lancement** : **manuel** (D17 + virement + activation admin). Zéro friction technique.
2. **Bascule vers Konnect/Flouci** quand **un seuil de volume** rend le manuel pénible — critère
   proposé : **> ~15-20 activations/semaine** OU friction manuelle qui coûte visiblement des
   conversions. Lot technique alors versé au [backlog 90](../../90-backlog-remediation.md).
3. Les frais PSP (~1,6 %) sont **négligeables** dans le modèle (marge ~90 %).

---

## 2. Marché adressable (TAM) — sourcé

| Segment | Volume annuel (2025) | Tension (places) |
|---|---|---|
| **9ème — cohorte générale** | **~169 000 inscrits** | — (parcours = tout le programme 9ème) |
| **9ème — candidats concours** | **~33 000** (segment le plus motivé/payeur) | **3 750 places** lycées pilotes |
| **6ème — candidats concours** | **~64 000** | **3 850 places** collèges pilotes |
| **Cœur de cible concours (6ème+9ème)** | **~97 000 candidats/an** | rareté extrême → forte disposition à payer |

> La **rareté des places** (3 750 / 33 000 en 9ème ; 3 850 / 64 000 en 6ème) est le moteur
> émotionnel : chaque parent veut maximiser les chances de son enfant. Et au-delà du concours, la
> cohorte **générale** (~169 000 en 9ème) est adressable pour la révision du programme.

---

## 3. Business plan 3 ans (scénarios)

**Hypothèses** : prix net moyen **~50 DT/pack** · acquisition **organique + partenariats +
parrainage** (CAC ~quasi nul) · marge brute **~90 %** (logiciel ; coût marginal = fraction infra +
PSP 1,6 %) · saison de vente = **pic révisions jan-mars** (entitlement année scolaire).

**Clients payants/an** (pénétration du cœur de cible ~97 000) :

| Année (saison) | Bas | Moyen | Haut | Pénétration (Haut) |
|---|---|---|---|---|
| **An 1** (2026-27) | 100 | **300** | 600 | ~0,6 % |
| **An 2** (2027-28) | 400 | **1 200** | 3 000 | ~3 % |
| **An 3** (2028-29) | 900 | **3 500** | 8 000 | ~8 % |

**Revenu brut (× ~50 DT)** :

| Année | Bas | **Moyen** | Haut |
|---|---|---|---|
| An 1 | 5 000 DT | **15 000 DT** | 30 000 DT |
| An 2 | 20 000 DT | **60 000 DT** | 150 000 DT |
| An 3 | 45 000 DT | **175 000 DT** | 400 000 DT |

**Coûts annuels indicatifs** (infra C4 + marketing + PSP + admin) :

| Poste | An 1 | An 2 | An 3 |
|---|---|---|---|
| Infra (C4 paliers) | ~0-500 DT (Free/early) | ~1 000-3 000 DT (Supabase Pro) | ~3 000-8 000 DT (scale) |
| Marketing | 1 000-2 000 DT | ~2 000-4 000 DT | ~4 000-8 000 DT |
| PSP (~1,6 %) | ~négl. (manuel) | ~1 000 DT | ~3 000 DT |
| **Total approx.** | **~2-3 000 DT** | **~5-8 000 DT** | **~12-18 000 DT** |

**Résultat net (scénario moyen, ordre de grandeur)** : An 1 ≈ **+10-12 k DT** · An 2 ≈ **+52-55 k
DT** · An 3 ≈ **+160 k DT**. → **Modèle bootstrappable, haute marge**, même à pénétration modeste
d'un marché énorme, sur un budget marketing minime.

> ⚠️ Ces chiffres sont des **ordres de grandeur** pour cadrer la trajectoire — la variable n°1 est
> le **taux de conversion preview→premium** (hypothèse C5 : 3-7 %), à **mesurer en beta** avant de
> s'y fier. Un classeur **xlsx** interactif (hypothèses éditables + formules) peut être généré sur
> demande à partir de ce modèle.

---

## 4. KPIs financiers & unit economics

| KPI | Définition / cible |
|---|---|
| **Prix net moyen** | ~50 DT/pack (à optimiser par tests de prix beta) |
| **CAC** | **~quasi nul** (organique/partenariats/parrainage) ; quelques DT/client avec micro-boosts |
| **Marge brute** | **~90 %+** (coût marginal ≈ infra/user + PSP 1,6 %) |
| **Revenu par cohorte annuelle** | remplace le MRR (modèle one-shot) : chaque rentrée = nouvelle cohorte 6ème/9ème |
| **LTV par famille** | > 1 pack : **pack famille** (fratries) + **6ème→9ème** (même famille à 3 ans d'écart) + **cross-sell académie** (langues/culture G hors-saison) |
| **Conversion preview→premium** | **3-7 %** (hypothèse C5) — **le levier n°1**, à mesurer |
| **Taux de renouvellement cohorte** | nouveau chaque année (le marché se renouvelle tout seul) |

**Levier de LTV** : le concours est **one-shot par enfant**, donc la croissance de la LTV passe par
(a) le **pack famille**, (b) l'**élargissement produit** vers l'académie large (rétention
hors-saison concours), (c) la **réputation** (témoignages de réussite → cohorte suivante).

---

## 5. Passage à l'échelle — seuils de déclenchement

| Levier | Seuil de déclenchement |
|---|---|
| **PSP en ligne** (Konnect/Flouci) | > ~15-20 activations manuelles/semaine, ou friction qui coûte des conversions |
| **Infra** (Supabase Pro, etc.) | paliers C4 : Pro dès les 1ers payants/données clients ; compute add-on à ~1 000+ actifs |
| **1er recrutement** (contenu + support) | quand la charge contenu (nouvelles matières/niveaux) + support dépasse le solo (≈ An 2-3) ; l'**authoring IA** (skills déjà industrialisés) repousse ce seuil |
| **Financement externe** | **optionnel** — modèle bootstrappable (haute marge, CAC bas). À considérer seulement pour **accélérer** (acquisition payante, équipe contenu, force B2B). Piste : **label Startup Act tunisien** (avantages fiscaux/sociaux) |
| **B2B écoles/centres** | après preuve B2C (An 2+) — revenu de revente/licence, force de vente dédiée |

---

## 6. Reste hors-périmètre C6 (dépendances)

- **Statut auto-entrepreneur** : à ouvrir avant la bascule premium (jan 2027) → **C7** + Go/No-Go payant.
- **Conformité mineurs / CGU / politique de confidentialité / mentions de prix** : **C3/légal + C7**.
- **Lot technique PSP** : au backlog 90 **si/quand** bascule en ligne décidée.
- **Instrumentation** : brancher PostHog (C4) pour mesurer le **vrai** taux de conversion → recaler le business plan.

---

## Sources
- [Tekiano — Concours 9ème 2025 : 33 000 candidats / 3 750 places](https://www.tekiano.com/2025/06/19/concours-9eme-2025-plus-de-33-000-candidats-pour-3750-places-dans-les-lycees-pilotes-de-tunisie/)
- [WMC — Concours 9ème : 169 308 inscrits, 33 180 candidats](https://www.webmanagercenter.com/2025/05/30/546963/tunisie-concours-neuvieme-plus-de-33-000-eleves-passeront-lexamen-en-juin-2025/)
- [La Presse — Concours 6ème 2025 : 64 065 candidats / 3 850 places](https://lapresse.tn/2025/05/30/examens-sixieme-64-065-eleves-candidats-au-concours-dacces-aux-colleges-pilotes/)
- [Konnect — tarifs (1,6 % local, sans frais de setup)](https://konnect.network/pricing/)
- [Smartegy — moyens de paiement e-commerce en Tunisie 2025](https://smartegy.tn/les-moyens-de-paiement-e-commerce-en-tunisie-ou-en-est-on-en-2025/)
- [Flouci — accepter les paiements en Tunisie](https://fr.flouci.com/enterprise)
