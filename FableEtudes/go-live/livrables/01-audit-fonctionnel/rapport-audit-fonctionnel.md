# C1 — Rapport d'audit fonctionnel (S3, 2026-06-10)

> Livrable de clôture du chantier [01-audit-fonctionnel](../../01-audit-fonctionnel.md).
> S'appuie sur [`cartographie.md`](./cartographie.md) (S1, analyse statique) et
> [`walkthrough-log.md`](./walkthrough-log.md) (S2, conditions réelles sur projet TEST).
> Tous les constats actionnables sont versés au [backlog 90](../../90-backlog-remediation.md) (GAP-NNN).

---

## 1. Synthèse exécutive

**Le produit est fonctionnellement riche et le cœur de l'expérience est solide.** La boucle de jeu
(quiz gate pédagogique → missions → scoring serveur → XP/coins/badges/streak → SM-2 → donjon →
boutique/consommables) fonctionne de bout en bout, avec une vraie qualité : anti-triche transparent
(temps validé serveur, shuffle des options), contenu trilingue riche (RTL arabe soigné), rendu mobile
correct, gamification cohérente. **Le squelette d'un bon produit est là.**

**Mais le produit n'est pas prêt pour un lancement public en l'état**, pour trois raisons de natures différentes :

1. **Un bug bloquant l'exploitation (P0)** : l'**admin ne peut accéder à aucune de ses 3 consoles**
   (`/admin/*`) à cause d'une collision de cache React Query. Or la console d'entitlements est
   aujourd'hui **le seul moyen de vendre** (activer un parcours premium). En l'état, **personne ne
   peut être passé en premium via l'UI**, ni les demandes beta triées, ni le contenu modéré. → GAP-017.
2. **Une finition produit insuffisante pour inspirer confiance à un parent payeur** : i18n
   incohérente sur **tout** le produit (anglais par défaut, FR+EN mélangés sur le même écran), et
   plusieurs mécaniques annoncées qui ne tiennent pas leur promesse (récompenses d'objectifs jamais
   versées, indice « ×3 » qui n'en donne qu'1, récupération de streak morte). → GAP-010/012/013/014.
3. **Le modèle de vente lui-même est un frein** : paiement uniquement hors-ligne (téléphone +
   activation manuelle admin) — déjà identifié (GAP-001), mais l'audit confirme qu'il est la **seule**
   voie et qu'elle est de surcroît cassée par le P0 ci-dessus.

**Verdict** : l'adéquation vision ↔ implémentation est **bonne sur le fond, fragile sur la finition
et bloquée sur l'exploitation**. Aucun de ces points n'est structurel — ce sont des bugs et des
finitions, pas des impasses d'architecture. Une poignée de corrections P0/P1 ciblées remettrait le
produit en état de lancement.

---

## 2. Matrice fonctionnelle (état × valeur)

Valeur : **V1** cœur de la promesse · **V2** support/engagement · **V3** accessoire.
État : ✅ fonctionne · ⚠️ fonctionne avec réserve · ❌ cassé / bloquant.

| Domaine fonctionnel | Valeur | État | Verdict |
|---|---|---|---|
| Inscription / login / OAuth | V1 | ⚠️ | Marche ; pas de « mot de passe oublié » ni page profil/compte (A-3) ; rôle parent perdu si confirmation email (cartographie E.1) |
| Onboarding (choix parcours) | V1 | ⚠️ | Flux clair et fonctionnel ; **FR-only** dans une UI EN (GAP-010) |
| Quiz gate pédagogique (école) | V1 | ✅ | Exemplaire : verrou → réussite → déblocage, badge, temps serveur |
| Boucle de quête + scoring | V1 | ✅ | Solide : anti-triche, shuffle, récompenses réelles, correction, SM-2 |
| Gate premium (entitlements) | V1 | ✅ | Le gate serveur fonctionne (free verrouillé, premium ouvert, pack famille) |
| **Parcours d'achat / paiement** | **V1** | ❌ | **Hors-ligne uniquement (téléphone) ET la console d'activation admin est cassée** (GAP-001 + GAP-017) |
| **Administration (ventes/beta/modération)** | **V1** | ❌ | **3 consoles inaccessibles** (GAP-017, P0) |
| Donjon (perk premium) | V2 | ⚠️ | Run complet OK ; **mélange les langues** dans un run (GAP-019) |
| Boutique / consommables | V2 | ⚠️ | Achat/équiper/armer OK ; indice « ×3 »→1 (GAP-014) ; 2 skins homonymes |
| Objectifs quotidiens / hebdo | V2 | ⚠️ | Progressent mais **récompenses jamais créditées** (GAP-012) |
| Badges | V2 | ⚠️ | 4/13 attribuables (cartographie B-4) ; le reste est décoratif sans logique |
| Récupération de streak | V3 | ❌ | **Inatteignable** par construction (GAP-013) |
| Rapport parent / pack famille | V1 | ✅ | Rapport clair (argument de vente n°1) ; lien Alliance Code OK |
| Leaderboard | V2 | ⚠️ | Rend ; onglets non scopés + « Mathématiques » en double (GAP-018) |
| Signalement de contenu | V2 | ✅ | Côté élève OK (testé S2) ; triage admin bloqué par GAP-017 |
| Contenu (école 6/9, langues, culture G, IQ) | V1 | ✅ | Riche, trilingue, RTL soigné, stylé RPG, figures SVG |
| i18n (FR/EN/AR + RTL) | V1 | ❌ | RTL technique OK mais **cohérence linguistique cassée partout** (GAP-010) |
| Mobile | V1 | ✅ | Rendu correct (testé landing, leçon RTL) |
| Alliance Code (privacy) | V2 | ⚠️ | = UUID brut de l'élève exposé (GAP-015) |

---

## 3. Findings consolidés (du walkthrough → backlog)

**Bloquant lancement (P0)**
- **GAP-017** — Consoles admin inaccessibles (collision queryKey `["me-role"]`). *Bloque la vente, le triage beta et la modération.* Cause racine et fix identifiés.

**Requis avant ouverture grand public (P1)**
- **GAP-001** — Pas de paiement en ligne (PSP tunisien à décider — porté par C6).
- **GAP-010** — i18n incohérente sur tout le produit (défaut EN, mélange FR/EN).
- **GAP-016** — INSERT direct `attempts` non révoqué (intégrité ; à confirmer sévérité en C3, candidat P0).

**Important (P2)**
- **GAP-012** — Récompenses d'objectifs/hebdo jamais créditées.
- **GAP-014** — Indice « ×3 » n'en donne qu'1 (article payé sous-livré).
- **GAP-015** — Alliance Code = UUID brut exposé (privacy → C3).
- **GAP-011** — Seed e2e cassé (tooling/CI → C2).

**Confort / cohérence (P3)**
- **GAP-013** — Récupération de streak morte. **GAP-018** — Leaderboard (doublon + scope). **GAP-019** — Donjon multi-langues.

**Long tail** (dette de code, RPCs orphelins, tables sans UI, nommage `subscription` hérité, badges
non câblés, code mort) : 31 candidats A-*/B-* détaillés dans [`cartographie.md`](./cartographie.md),
**laissés au tri de C2 (audit technique)** — hors périmètre du lancement fonctionnel.

*Un candidat infirmé en S2 : la potion `coinMultiplier` (« Pierre Philosophale ») existe bien au
catalogue, contrairement à ce que suggérait la cartographie (B section consommables).*

---

## 4. Adéquation besoins ↔ vision ↔ implémentation

> Référentiel vision (validé en kickoff, §0 du [plan de tests](./plan-de-tests.md)) : académie
> gamifiée multi-thèmes, cœur payant = concours 6/9, exploration gratuite autour, payeur = parent.

- **Vision ↔ implémentation : alignée sur le fond.** Le modèle (thèmes → grades → parcours →
  entitlements per-parcours + pack famille + preview gratuite) est bien implémenté et cohérent avec
  la stratégie premium. Le catalogue large (école 6/9 + langues + culture G + IQ) matérialise bien
  l'« académie », pas un cours unique.
- **Besoins du payeur (parent) : partiellement servis.** Le rapport parent — l'argument de vente n°1
  — existe et est convaincant. **Mais** le parcours qui transforme l'intérêt en achat est cassé :
  paiement hors-ligne (friction) **et** activation admin inopérante (GAP-017). Le tunnel de
  conversion est donc, à ce jour, **non fonctionnel de bout en bout**.
- **Besoins de l'élève (utilisateur) : bien servis sur le cœur, friction sur la finition.** La boucle
  d'apprentissage gamifiée est engageante et fonctionne. Les promesses non tenues (objectifs,
  indices, streak) et le mélange linguistique entament la confiance et la perception de qualité.
- **Écart marketing/produit** : la landing et les titres figent le produit sur « 6th & 9th grade
  exams » alors que le catalogue est plus large (A-15) — à arbitrer avec C5 (positionnement).

---

## 5. Recommandations

**Avant tout lancement (à verser en priorité backlog)**
1. **Corriger GAP-017** (clés de cache distinctes) — débloque l'exploitation. Effort faible, impact maximal. *À traiter en premier, indépendamment du reste.*
2. **Trancher le paiement** (GAP-001, via C6) — au minimum documenter et fiabiliser le process manuel (qui dépend de GAP-017).
3. **Passer une vraie revue i18n** (GAP-010) : défaut FR, supprimer les chaînes codées en dur, traduire onboarding/leaderboard/lesson.
4. **Tenir les promesses de gamification** (GAP-012/014) ou les retirer de l'UI — ne pas afficher des récompenses non versées ni des articles sous-livrés.

**Qualité de lancement (souhaitable)**
5. Page profil/compte + « mot de passe oublié » (A-3). 6. États d'erreur sur les routes de lecture sans branche erreur (A-5). 7. Régénérer/masquer l'Alliance Code (GAP-015). 8. Leaderboard scopé au parcours + désambiguïser les matières homonymes (GAP-018).

**Méthode** — un point fort à conserver : la testabilité. L'environnement TEST + les outils d'audit
(`tools/`) permettent un walkthrough reproductible. **Recommandation** : faire valider les parcours
clés par de vrais élèves/parents beta avant J0 (le jugement « fun/clair pour un enfant » reste un
proxy d'adulte).

**Reliquat S2** (non bloquant, à compléter si besoin) : pack famille end-to-end, level-up réel,
états d'erreur réseau, flux complet « Signaler une erreur ».

---

## 6. Conclusion

C1 est **terminé** sur l'essentiel : cartographie complète, walkthrough réel multi-persona, findings
priorisés et versés au backlog. Le message à retenir pour le go-live : **le produit est bon mais pas
vendable en l'état** — un P0 bloque la vente, et la finition (i18n, promesses de jeu) doit être reprise
pour convaincre un parent payeur. Aucun de ces points n'est structurel ; ils sont corrigeables avant
lancement. Le bug admin (GAP-017) devrait être corrigé **immédiatement**, indépendamment du reste du
programme, tant son rapport impact/effort est élevé.
