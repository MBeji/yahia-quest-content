# S1 — Modèle de revenus, prix & structure d'offre — Na9ra Nal3ab

> ⚠️ **SUPERSÉDÉ (pivot gratuit du 2026-06-21 + gratuité de phase 2026-07-10/11)** — aucune
> monétisation en phase actuelle ; document conservé comme matière première pour l'étude 01
> (paiement en ligne, gelée). Voir la bannière du chantier [06](../../06-modele-economique-monetisation.md).

> Livrable S1 du chantier [06](../../06-modele-economique-monetisation.md). Date : 2026-06-13.
> Ancres validées (kickoff) : **pack one-shot « année scolaire »** (pas d'abonnement) · **paiement
> manuel d'abord** (D17/virement + activation admin, déjà câblé) · **statut légal à cadrer**
> (prérequis du lancement payant, pas de la beta gratuite). Modèle existant : freemium par parcours
> (preview gratuite = quiz + difficulté 1 ; parcours concours 9ème/6ème payants ; pack famille ;
> entitlements `purchase/beta/gift/family`). Prix = **hypothèses à tester en beta**, pas gravés.

---

## 1. Modèle de revenus : confirmer le **freemium par parcours**

L'app a déjà le bon modèle, **déjà câblé** : accès gratuit à la preview (quiz de compréhension +
difficulté 1) + **parcours concours payants**. On le **confirme** et on le précise (offre §3).

**Modèles écartés / différés** (et pourquoi) :
| Modèle | Décision | Raison |
|---|---|---|
| **Publicité** | ❌ écarté | Public **mineurs** (INPDP/conformité), nuit à la confiance parent et à la marque |
| **Abonnement mensuel** | ❌ écarté au lancement | Décision kickoff : friction du récurrent en TN + PSP locaux gèrent mal le récurrent. *(Réexaminable plus tard pour l'académie large hors-concours.)* |
| **B2B écoles/centres (revente)** | ⏳ différé année 2 | Après preuve B2C. Le partenariat école sert d'abord de **canal marketing** (C5), pas de revenu |
| **Marketplace de contenu parent** | ⏳ différé | Le schéma supporte du contenu parent, mais monétiser ça vient bien plus tard |
| **Freemium par parcours (one-shot)** | ✅ **retenu** | Déjà construit, aligné concours + habitudes de paiement TN |

---

## 2. Étude de prix — marché tunisien (l'ancre de disposition à payer)

**Le concours, c'est un marché énorme et cher.** Le marché tunisien des cours particuliers pèse
**~1,5 à 3 milliards de dinars/an** (sources ci-dessous). Repères de prix :

| Alternative | Prix observé | Coût annuel implicite (concours) |
|---|---|---|
| **Cours particulier 9ème (tarif officiel établissement)** | **~35 DT/séance** (30-40 DT, ~7 élèves/séance) | ~4-8 séances/mois × ~8 mois = **centaines de DT / matière** |
| **Cours particulier privé (secondaire)** | **80-150 DT/séance** (moy. ~80) | **1000-3000+ DT/an** en multi-matières |
| **Bac (prépa cours particuliers)** | jusqu'à **~2000 DT/an** | — |
| **Takiacademy** (réf. edtech TN, vidéo) | abonnement **annuel** (−25 % vs mensuel), remises fratrie **−30 % 2ᵉ / −50 % 3ᵉ** | modèle abonnement, contenu vidéo passif |
| **Plateformes gratuites** (nouvelles, 2026) | **0 DT** | menace : différenciation = **engagement/gamification**, pas le contenu seul |

**Lecture stratégique** :
- L'ancre est **écrasante** : une année de prépa concours en cours particuliers = **des milliers de
  DT**. Notre pack one-shot à quelques dizaines de DT est un **no-brainer** (« le prix de 1-2
  séances pour toute l'année »).
- **Takiacademy** valide qu'un parent tunisien **paie déjà en ligne** pour de l'edtech, et la
  **structure remises fratrie** est une norme acceptée → on s'y aligne (pack famille).
- Des **plateformes gratuites** existent → on **ne vend pas du contenu** (il se commoditise), on
  vend **l'engagement** (l'enfant révise *vraiment*, seul, avec plaisir) + le suivi parent.

---

## 3. Structure d'offre (pack one-shot « année scolaire »)

- **Unité de vente = le parcours concours** (9ème ou 6ème), accès **jusqu'à la fin de l'année
  scolaire / le concours** (entitlement à **expiration annuelle**, renouvelable l'année suivante).
- **Preview gratuite** conservée (quiz + difficulté 1) = l'essai sans risque qui nourrit la
  conversion.
- **Pack famille** : remise multi-enfants (norme TN via Takiacademy) — un parent équipe 2-3 enfants
  (via `parent_student_links` + entitlements `family`, déjà câblés).
- **Offre de lancement « Héros Fondateurs »** : remise early-bird limitée dans le temps (urgence
  « J-90 concours »).
- **Satisfait ou remboursé** (X jours) : annule le risque du 1er achat (cohérent paiement manuel).
- **Continuité fondateurs** : les beta-fondateurs gardent un avantage de fidélité.

> Politique année scolaire : l'entitlement **expire** en fin d'année → revenu **re-récurrent par
> cohortes** (chaque rentrée, nouvelle 9ème/6ème) sans la friction d'un abonnement mensuel.

---

## 4. Grille tarifaire recommandée (en DT — **à valider en beta**)

> Principe : **assez bas pour être un achat d'impulsion approuvé sans délibération**, assez haut
> pour signaler de la valeur. On **testera 2-3 points de prix** sur de vraies familles en beta.

| Offre | Prix catalogue | Prix lancement (« Fondateurs ») |
|---|---|---|
| **Pack Concours** (1 parcours, année scolaire) | **~69-79 DT** | **~39-49 DT** (−40 %) |
| **2ᵉ enfant** (pack famille) | −30 % | cumulable |
| **3ᵉ enfant et +** | −50 % | cumulable |

**Justification du niveau** : ~70 DT pour **toute l'année** de prépa concours = **le prix de ~2
séances** de cours particulier (et ~95 % moins cher qu'une année multi-matières). Le parent compare
à 1000-3000 DT → décision facile. Le pack famille protège le revenu sur les fratries (fréquentes).

*(Alternative « volume » à tester : un point de prix plus bas ~39-49 DT catalogue pour maximiser la
conversion et le bouche-à-oreille, si la beta montre une forte sensibilité au prix.)*

---

## 5. Prérequis légal/fiscal pour **encaisser** (statut « à cadrer »)

**C'est le prérequis dur du lancement *payant*** (pas de la beta gratuite). Pour facturer/encaisser
légalement en Tunisie :

| Option | Pour qui | Notes |
|---|---|---|
| **Auto-entrepreneur** | **Recommandé pour démarrer** | Statut allégé (régime simplifié), permet de facturer ; le plus rapide/léger pour valider le marché |
| **Société (SUARL/SARL)** | Si visée échelle / B2B / TVA | Plus lourd (compta, capital) ; pertinent une fois la traction prouvée et le PSP/partenariats nécessaires |

**Recommandation** : ouvrir le statut **auto-entrepreneur** avant la bascule premium (jan 2027) —
suffisant pour le paiement manuel (facture + D17/virement) et l'onboarding d'un PSP plus tard. À
porter avec **C7 (gouvernance)** et la **checklist Go/No-Go (lancement payant)**. La beta gratuite
de l'été/rentrée **ne le nécessite pas** → on a le temps de le mettre en place.

---

## 6. Reste pour S2

- **Panorama PSP tunisiens** (Konnect/Paymee/Flouci/ClicToPay : frais, délais, intégration,
  confiance parents) + **critère de bascule** manuel → en ligne (ex. seuil de volume/charge de
  gestion manuelle) + lot technique au backlog si intégration.
- **Business plan 3 ans** : TAM (cohortes 6ème/9ème en Tunisie — à sourcer) × hypothèses
  conversion/rétention (C5 : preview→premium 3-7 %) × coûts (C4 : paliers ~0-120 $/mois) →
  scénarios bas/moyen/haut (xlsx).
- **KPIs financiers** (MRR/ARR — ici plutôt **revenu par cohorte annuelle**, CAC, LTV, marge) +
  **seuils de passage à l'échelle** (financement, recrutement, infra).

---

## Sources (prix marché)
- [Jeune Afrique — le business des cours particuliers en Tunisie](https://www.jeuneafrique.com/mag/519365/societe/tunisie-le-fructueux-business-des-cours-particuliers/)
- [La Presse — jusqu'à 2000 DT pour réussir le bac (cours particuliers)](https://lapresse.tn/2025/05/10/jusqua-2-000-dinars-pour-reussir-le-bac-les-cours-particuliers-hors-de-controle-en-tunisie/)
- [Tunisie Numérique — fixation du prix des séances de cours particuliers](https://www.tunisienumerique.com/tunisie-education-fixation-du-prix-des-seances-de-cours-particuliers/)
- [Tunisie Numérique — le coût annuel des cours particuliers (~1,5 Md DT)](https://www.tunisienumerique.com/cours-particuliers-une-annee-scolaire-et-universitaire-coute-aux-tunisiens-pres-de-15-milliard-de-dinars/)
- [Takiacademy — page Offres](https://www.takiacademy.com/offers)
- [Tekiano — plateforme gratuite de soutien scolaire en ligne (2026)](https://www.tekiano.com/2026/03/25/tunisie-une-plateforme-gratuite-de-soutien-scolaire-en-ligne-accessible-a-tous/)
