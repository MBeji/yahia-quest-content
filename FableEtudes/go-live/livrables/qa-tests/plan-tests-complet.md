# Plan de tests complet — non-régression, E2E, qualité, UX & multi-device

> Plan d'action **à exécuter plus tard** (on n'écrit pas les tests ici). Objectif : couverture
> maximale des parcours utilisateurs, des cas d'usage, de la qualité du portail, de l'UX et de
> l'affichage multi-device (téléphone / tablette / PC), avec mise à jour des non-régressions suite
> aux correctifs déjà livrés. Rattaché au programme go-live ([backlog GAP-025](../../90-backlog-remediation.md)).
> Pilotage : [00-MASTER-PLAN.md](../../00-MASTER-PLAN.md).

> ## ⏸️ STATUT : PLANIFIÉ — à implémenter (tests NON écrits)
> Décision Mohamed (2026-06-10) : **stocker le plan, implémenter plus tard.**
> **Reprise → commencer par le Lot 0** (§10) : **INF-1 réparer le seed e2e (GAP-011)** = prérequis
> bloquant, puis **NR-1** (réconcilier l'existant avec les correctifs GAP-016/017/020).
> Plus fort ROI ensuite : **Lot 2 multi-device** (RWD-1 authed-mobile, RWD-3 balayage 6 viewports,
> RWD-4 RTL×mobile, RWD-5 WebKit). Ne rien implémenter sans relire ce plan + l'état des correctifs
> en cours (certains items attendent un fix : GAP-010/012/013/014/018/021).

---

## 1. État des lieux (2026-06-10)

**Non-régression (Vitest 4 + Testing Library)** — `npm test`
- **~572 tests** (unit + intégration), gate à **80 %** sur toutes les métriques.
- Couverture **scopée au code « owned »** : `src/features/**`, `src/shared/**`, `src/lib/**`, `src/hooks/**`.
- **Exclus de la couverture** (donc territoire e2e/intégration, pas unit) : `src/features/**/components/**`
  (composants React des features), `src/components/ui/**` (shadcn vendored), `src/routes/**` (wrappers),
  barrels `index.ts`, `types.ts` généré.
- Mock Supabase (`mockFrom`/`mockRpc`) — pas de vraie DB.

**E2E (Playwright)** — `npm run test:e2e` (public) / `test:e2e:auth` (authentifié)
- **31 specs** : 7 public (sans backend) + 24 authentifiées (vs projet Supabase **TEST** dédié).
- **Projets** : `public-chromium` (Desktop Chrome), `public-mobile` (**Pixel 7**), `authed-chromium`
  (**Desktop Chrome uniquement**) + `setup` (auth.setup.ts → storage states des 4 rôles).
- **4 rôles seedés** : `free`, `premium`, `parent`, `admin` (`e2e/.auth/*.json`).
- **11 page objects** (`e2e/pages/`), helpers `a11y.ts` (axe-core WCAG2 A/AA), `db.ts` (adminDb
  service-role), `viewports.ts` (6 devices), `users.ts`, `env.ts`.
- **6 device viewports définis** : iPhone SE 375, iPhone 14 Pro Max 430, iPad Mini 768 portrait,
  iPad Pro 1194 paysage, Laptop 1366, Desktop 1920 + `expectNoHorizontalOverflow`.
- Approche graphique retenue : **DOM + a11y, pas de pixel-snapshot** (cf. `e2e/RAPPORT-DE-TEST.md`).

**Trous structurels identifiés**
- **T-1 — Le tier authentifié ne tourne que sur Desktop Chrome** : aucun projet `authed-mobile` ni
  `authed-tablet`. Le responsive des écrans connectés (dashboard, quête, donjon, boutique, rapport
  parent, admin) repose sur un seul `authed/responsive.spec.ts` qui redimensionne à la main.
- **T-2 — Un seul moteur (Chromium)** : pas de WebKit (Safari/iOS) ni Firefox → angle mort réel pour
  les utilisateurs iPhone (Safari) du marché TN.
- **T-3 — Seed e2e cassé (GAP-011)** : `npm run e2e:setup` échoue (provisioning premium) → le tier
  authentifié n'est pas fiable en CI sans contournement.
- **T-4 — RTL/arabe sous-couvert** : `i18n-rtl.spec.ts` existe mais le rendu **AR × mobile/tablette**
  (contenu 6ème éveil scientifique, culture G AR) n'est pas systématiquement vérifié.
- **T-5 — Régressions des correctifs récents non garanties par e2e** : GAP-017 (consoles admin),
  GAP-016 (forge attempts), GAP-020 (banque de réponses) ont des tests unit mais peu/pas de garde
  e2e « bout en bout » côté API/parcours.
- **T-6 — Bugs C1 non corrigés** (GAP-010 i18n, GAP-012 objectifs, GAP-013 streak, GAP-014 indices,
  GAP-018 leaderboard) : à fixer **puis** verrouiller par non-régression.

---

## 2. Objectifs & principes directeurs

1. **Couverture maximale des parcours** : les **8 personas** de l'audit fonctionnel C1 (visiteur,
   nouvel élève, élève freemium, élève premium, élève 6ème AR/RTL, élève exploration, parent, admin).
2. **Non-régression d'abord** : chaque correctif livré (GAP) et chaque bug à corriger reçoit un test
   qui **échoue avant / passe après** et garde le comportement.
3. **Pyramide de tests** : beaucoup d'unit/intégration (rapides, logique), un socle e2e ciblé sur les
   parcours critiques, une passe a11y et une passe responsive. Pas de sur-investissement e2e sur ce
   qui est déjà couvert en unit.
4. **Qualité = i18n cohérente + états (vide/erreur/chargement) + a11y + responsive sans débordement**.
5. **Déterminisme** : données via `adminDb` (seed/reset), sélecteurs stables (rôle/texte/`data-testid`),
   retries anti-hydratation déjà en place — à généraliser.
6. **Jamais sur la prod** : tout e2e authentifié vise le projet **TEST** (garde anti-prod existante).

---

## 3. Axe 1 — Non-régression (Vitest) : mise à jour & complétude

> But : refléter le code actuel (post-correctifs) et couvrir les règles métier non testées.

| # | Action | Cible | Prio |
|---|--------|-------|------|
| NR-1 | **Réconcilier les tests existants avec les correctifs livrés** : vérifier que `quest`, `auth`, `subscription` reflètent `useMyRole` (GAP-017), le REVOKE écritures (GAP-016), `get_attempt_review` (GAP-020). | `features/{auth,quest}/__tests__` | 🔴 |
| NR-2 | **Tests des règles de gamification chiffrées** non couvertes : courbe XP/niveau, tiers hero-class, anti-farm (tooFast/≥60 %/improved), streak (+ bouclier), SM-2 (J+1/3/7), adaptation difficulté (10/75/40). | `shared/constants` + `quest`/`progression` server fns | 🟠 |
| NR-3 | **Consommables** : potions (×2/×3, slot next-quest exclusif), bouclier retry (suppression pénalité SM-2), bouclier streak (passif), indices (anti-gaspillage). | `shop`, `quest` | 🟠 |
| NR-4 | **Premium gate** : `resolve_exercise_access` (free vs premium vs preview vs coming_soon), pack famille (parent lié), donjon (entitlement concours). | `quest`, `dungeon`, `subscription` | 🔴 |
| NR-5 | **Parcours parent** : lien Alliance Code, rapport (verdict d'assiduité, scoping élève), absence de fuite PII. | `parent-report` | 🟠 |
| NR-6 | **Régressions des bugs C1 (après fix)** : objectifs/hebdo récompensés (GAP-012), récupération streak atteignable (GAP-013), indice ×3 = 3 charges (GAP-014). | server fns + RPC | 🟠 (post-fix) |
| NR-7 | **Couverture des helpers purs** non testés (journey, next-exercise, no-xp-reason, quest-labels, family-link). | `features/*/` helpers | 🟢 |
| NR-8 | **Maintenir le seuil 80 %** : la migration de logique vers SQL (ex. futur `start_exercise_session`, GAP-021) **déplace la couverture** vers les sondes/e2e — documenter et compenser par des tests d'intégration. | `vitest.config.ts` scope | 🔴 |

---

## 4. Axe 2 — E2E : couverture maximale des parcours utilisateurs

> Matrice **persona × parcours critique**. ✅ = spec existante (à auditer/renforcer) · ➕ = à créer.

| Parcours | Persona | Spec actuelle | Action |
|----------|---------|---------------|--------|
| Landing → compréhension valeur → CTA | Visiteur | `public/landing` ✅ | Renforcer (langue par défaut, CTA, liens légaux quand créés) |
| Signup (rôles, confirmation email) + login + logout | Visiteur | `signup`, `auth-flows`, `logout` ✅ | Compléter : mot de passe oublié (quand implémenté), erreurs |
| Onboarding (intention → parcours) → 1ʳᵉ quête | Nouvel élève | `onboarding` ✅ | Renforcer : état vide dashboard, guidage 1ʳᵉ quête |
| Freemium : preview gratuite → **paywall** difficulté ≥ 2 | Élève freemium | `premium-gate`, `free-user` ✅ | Vérifier message paywall + voie d'achat (téléphone) |
| **Quiz gate école** : verrou → réussite → déblocage missions | Élève premium | `quiz-gate`, `quiz-unlock` ✅ | OK — garder ; ajouter cas « rushé ne débloque pas » |
| **Boucle quête** complète (submit, récompenses, correction) | Élève premium | `gameplay-loop` ✅ | Renforcer : écran résultat (XP/coins/badges/level-up), **correction via get_attempt_review** (GAP-020) |
| **Donjon** : run, game-over, récompenses, gates | Élève premium | `dungeon` ✅ | Renforcer : prérequis (2 matières/3 chapitres), multi-langues (GAP-019) |
| **Boutique** : achat → équiper skin → armer potion → effet | Élève premium | `shop` ✅ | Renforcer : effet de la potion sur la quête suivante |
| Progression : objectifs/hebdo, badges, SM-2, leaderboard | Élève premium | `progression-stats`, `leaderboard` ✅ | Compléter : récompenses objectifs (après GAP-012), leaderboard scoping (GAP-018) |
| Exploration : culture G ×3 langues, IQ, langues CECR | Élève exploration | `four-families`, `catalogue` ✅ | Renforcer : quiz non bloquant hors école, gratuité totale |
| **Contenu 6ème AR/RTL** (éveil scientifique) | Élève 6ème | `i18n-rtl` (partiel) ➕ | **Créer** : leçon + quête AR, figures SVG RTL, sur **mobile** |
| Lien famille + rapport + **pack famille** | Parent | `parent-link`, `admin-and-parent` ✅ | Compléter : pack famille e2e (parent entitlement → enfant débloqué) |
| **Consoles admin** (entitlements/ventes, beta, content-reports) | Admin | `admin-and-parent`, `authorization` ✅ | **Renforcer (GAP-017)** : admin atteint les 3 consoles + grant/revoke end-to-end |
| Signalement d'erreur de contenu (flux complet) | Élève + Admin | `content-report` ✅ | OK |
| Autorisations / refus (non-admin sur /admin, IDOR) | Tous | `authorization` ✅ | **Renforcer (sécurité)** : voir Axe 6 |

**Cas d'usage transverses à couvrir** : double soumission, perte réseau pendant une quête, session
expirée, 404 (sujet/exercice inexistant), changement de parcours via l'Explorer, états « pas encore
de contenu ».

---

## 5. Axe 3 — Qualité du portail

| # | Action | Détail |
|---|--------|--------|
| Q-1 | **i18n cohérente (GAP-010)** : vérifier FR/EN/AR sur les écrans clés (landing, onboarding, dashboard, quête, paywall, résultat, boutique, leaderboard, rapport parent) — **aucun fragment codé en dur**, défaut FR. | Spec dédiée `i18n-coverage` balayant les 3 langues × écrans clés ; assert absence de clés non traduites. À renforcer après le fix GAP-010. |
| Q-2 | **États vide / chargement / erreur** : chaque route de lecture a une branche d'erreur (A-5 : `lesson`, `parcours`, `dungeon` n'en ont pas) ; états vides soignés (dashboard neuf, leaderboard vide). | Spec `states` : forcer erreurs réseau (route interception Playwright) et vérifier le rendu dégradé, pas de spinner infini. |
| Q-3 | **Cohérence du catalogue** : leaderboard sans doublon de matière (GAP-018), onglets scopés au parcours. | Après fix GAP-018. |
| Q-4 | **Performance perçue** (lien C2) : budget bundle déjà en CI ; ajouter une passe **Lighthouse/Web Vitals** sur landing + dashboard (LCP/CLS/TBT) comme garde qualité. | Outillage `@playwright/test` + lighthouse-ci (optionnel) ; cibles à définir avec C4. |

---

## 6. Axe 4 — UX & accessibilité

| # | Action | Détail |
|---|--------|--------|
| UX-1 | **a11y systématique (axe-core)** : étendre la passe WCAG2 A/AA (déjà sur landing/login/signup/dashboard/leaderboard/subject) à **quête, donjon, boutique, onboarding, rapport parent, consoles admin**. | `helpers/a11y.ts` existant ; fail sur serious/critical. |
| UX-2 | **Corriger + verrouiller le finding contraste** : `--muted-foreground` #4f5460 sur fond sombre = 2.61:1 (< 4.5:1) sur la page sujet (déjà désactivé ponctuellement). | Réactiver la règle color-contrast après correction du token. |
| UX-3 | **Navigation au clavier** : raccourcis quête (1-4/A-D), focus visible, ordre de tabulation, fermeture des modales (paywall). | Specs ciblées clavier. |
| UX-4 | **Parcours fluides** : nombre de clics jusqu'à la 1ʳᵉ quête, réversibilité du changement de parcours, retour cohérent (les « back » FR/EN mélangés → après GAP-010). | Assertions de navigation. |
| UX-5 | **Lecteur d'écran (smoke)** : noms accessibles des contrôles clés (boutons d'action, options de quête, switchers langue/thème). | Via le snapshot d'accessibilité. |

---

## 7. Axe 5 — Affichage multi-device (téléphone / tablette / PC)

> **Priorité forte** (demande explicite). Combler T-1 (authed Desktop-only) et T-2 (Chromium-only).

| # | Action | Détail |
|---|--------|--------|
| RWD-1 | **Ajouter un projet `authed-mobile`** (Pixel 7) à `playwright.config.ts` ciblant un sous-ensemble de parcours critiques connectés (dashboard, quête, donjon, boutique, rapport parent, admin). | Nouveau projet + `testMatch` d'un set « smoke mobile authed ». |
| RWD-2 | **Ajouter une couverture tablette** : projet `authed-tablet` (iPad Mini 768 / iPad Pro 1194) OU balayage viewport tablette dans `authed/responsive.spec.ts`. | Cibler le breakpoint `md=768` (bascule de nav). |
| RWD-3 | **Balayage systématique des 6 `DEVICE_VIEWPORTS`** sur les écrans clés (public **et** authed) avec `expectNoHorizontalOverflow` + visibilité des éléments d'action. | Étendre `public/responsive` + `authed/responsive` aux 6 tailles. |
| RWD-4 | **RTL × mobile/tablette** : contenu **arabe** (leçon, quête, figures SVG) sur téléphone et tablette — layout RTL correct, pas de débordement, compteurs non inversés (constat C1 : « 11/4 »). | Combine Axe 2 (6ème AR) + viewports. |
| RWD-5 | **Cross-moteur** : ajouter **WebKit** (Safari/iOS) au minimum sur le tier public + un smoke authed ; Firefox optionnel. | Projets `public-webkit` / `authed-webkit-smoke`. |
| RWD-6 | **Orientations** : portrait/paysage sur tablette (iPad Mini portrait vs iPad Pro paysage déjà dans la liste) pour les écrans denses (donjon, quête, radar dashboard). | Inclus via les viewports. |
| RWD-7 | **Zones sûres mobiles** : `env(safe-area-inset-*)` (header/footer) sur encoches — vérifier le rendu sur iPhone 14 Pro Max. | Assertions de padding. |

---

## 8. Axe 6 — Régression sécurité (verrouiller les correctifs)

> Transforme les **sondes d'exploit C3** (`go-live/livrables/03-cybersecurite/tools/probe*.py`) en
> gardes automatisées, et garde les correctifs livrés.

| # | Action | Réf |
|---|--------|-----|
| SEC-1 | **Forge `attempts` bloquée** : un user authentifié ne peut PAS `POST /rest/v1/attempts` (403). | GAP-016 |
| SEC-2 | **Banque de réponses masquée** : `GET /questions?select=correct_option` → 403 ; `get_attempt_review` ne rend la correction qu'au propriétaire d'une session complétée. | GAP-020 |
| SEC-3 | **Consoles admin accessibles à l'admin / refusées au non-admin** (e2e + intégration). | GAP-017 |
| SEC-4 | **Pas d'élévation / auto-octroi / IDOR** : rôle admin, entitlement premium, lien parent, lecture d'autrui — tous bloqués (reprendre les 10 sondes `probe.py`). | C3 S1 |
| SEC-5 | **Intégration des sondes en CI** : un job (hors `verify`) rejoue `probe*.py` vs TEST (ou réécrits en Playwright API-request) comme garde de non-régression sécurité. | Infra |

---

## 9. Axe 7 — Infrastructure de test & CI

| # | Action | Détail |
|---|--------|--------|
| INF-1 | **Réparer le seed e2e (GAP-011)** — **bloquant** pour le tier authentifié fiable. `admin_grant_parcours` échoue avec la clé service. Fix : escape-hatch `service_role` dans la RPC OU seed entitlements en SQL direct (les outils d'audit `tools/fix-test-seed.py` le font déjà). | 🔴 prérequis |
| INF-2 | **Brancher le tier authentifié en CI** : secrets `TEST_SUPABASE_*` + `e2e-auth.yml` ; provisionner la DB TEST (db push + seed) ; gérer la concurrence (free-tier → workers cappés). | CI |
| INF-3 | **Données de test déterministes** : étendre `helpers/db.ts` (reset gameplay, états « élève avec progression », « parent lié », « beta pending ») ; documenter dans `e2e/README.md`. | Fixtures |
| INF-4 | **Stabilité anti-hydratation** : généraliser le pattern `toPass`-retry (déjà sur nav/logout) ; pacing anti-rush (≥4 s/q) pour les soumissions notées. | Page objects |
| INF-5 | **Rapport & artefacts** : maintenir `e2e/RAPPORT-DE-TEST.md` (scénario/étapes/résultat) + HTML report en artefact CI ; traces on-first-retry. | Reporting |
| INF-6 | **Cadence** : `verify` (unit) sur chaque push ; e2e public sur PR ; e2e authentifié + sécurité + responsive multi-device en **nightly** (coût/temps). | CI |

---

## 10. Plan d'exécution phasé (à dérouler plus tard)

> Dépendance forte : plusieurs items attendent des **correctifs** (GAP-010/012/013/014/018/021) ou
> l'**infra** (INF-1 seed). Ordonné par valeur/déblocage.

**Lot 0 — Débloquer (prérequis)**
- INF-1 (réparer le seed) → sans ça, le tier authentifié n'est pas fiable. NR-1 (réconcilier l'existant avec les correctifs livrés).

**Lot 1 — Non-régression sécurité & correctifs livrés**
- SEC-1/2/3 + SEC-5 (sondes en CI). NR-4 (premium gate). Verrouille GAP-016/017/020.

**Lot 2 — Multi-device & responsive (demande forte)**
- RWD-1 (authed-mobile), RWD-3 (balayage 6 viewports), RWD-4 (RTL×mobile), RWD-5 (WebKit), RWD-2 (tablette).

**Lot 3 — Parcours e2e complets**
- Compléter la matrice §4 (6ème AR ➕, pack famille, donjon prérequis, boutique effet potion, états transverses). UX-1 (a11y étendue).

**Lot 4 — Qualité & régressions post-fix**
- Q-1 (i18n après GAP-010), Q-2 (états/erreurs), NR-2/NR-3/NR-5/NR-6, Q-3 (leaderboard après GAP-018), UX-2/3/4.

**Lot 5 — Performance & cross-browser élargi**
- Q-4 (Lighthouse/Web Vitals), Firefox, orientations tablette, safe-areas.

---

## 11. Definition of Done (par lot)

- `npm run verify` **vert** (lint 0-warning + tsc strict + unit), couverture **≥ 80 %** non régressée.
- E2E ciblés **verts** sur les projets concernés (public + authed + mobile/tablette/webkit selon le lot),
  **jamais sur la prod**.
- Chaque correctif a un test qui **échouait avant / passe après**.
- a11y : 0 violation serious/critical sur les écrans du lot.
- Responsive : `expectNoHorizontalOverflow` sur tous les viewports du lot, éléments d'action visibles.
- `e2e/RAPPORT-DE-TEST.md` mis à jour (scénarios + résultats + éventuels findings → backlog).

---

## 12. Récapitulatif des livrables attendus (quand on exécutera)

- `playwright.config.ts` : projets `authed-mobile`, `authed-tablet` (ou viewport sweep), `*-webkit`.
- Nouvelles specs : `i18n-coverage`, `states`, `6eme-ar-rtl`, `security-regression` (ou sondes en CI),
  + renforcements des specs existantes (§4).
- Nouveaux tests unit/intégration (§3).
- Helpers étendus (`db.ts` fixtures, `a11y.ts` écrans, `viewports.ts` déjà prêt).
- `e2e/README.md` + `RAPPORT-DE-TEST.md` à jour ; job CI nightly responsive/sécurité.
- Findings éventuels → [backlog 90](../../90-backlog-remediation.md).
