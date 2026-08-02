# C1 — Plan de tests fonctionnels (kickoff 2026-06-10)

> Artefact opérationnel du chantier [01-audit-fonctionnel](../../01-audit-fonctionnel.md).
> Les observations se logguent dans `walkthrough-log.md` (créé en S2) ; la synthèse dans
> `rapport-audit-fonctionnel.md` (S3).

## 0. Référentiel vision produit (draft — à corriger par Mohamed à la validation)

> Na9ra Nal3ab est une **académie d'apprentissage gamifiée multi-thèmes** pour le marché tunisien.
> Le cœur payant : la **préparation aux concours nationaux (6ème et 9ème)**, fidèle au programme
> officiel, vendue **par parcours** (+ pack famille), avec preview gratuite. Autour : des thèmes
> d'**exploration gratuits** (culture générale, entraînement cérébral, langues) qui créent l'usage,
> l'engagement quotidien et le bouche-à-oreille. Expérience : RPG/shonen (XP, badges, boutique,
> donjon), boucles d'engagement quotidiennes/hebdomadaires, trilingue FR/EN/AR avec RTL.
> **Payeur = parent ; utilisateur = élève.**

C'est l'étalon contre lequel on jugera « adéquation besoins ↔ vision ↔ implémentation ».

## 1. Environnement d'audit

- **Tout parcours muté se fait sur le projet Supabase TEST** (`pqegdnwdtbjtplcthxyp`) — jamais la
  prod (`fasrenmmrkqjoobrztbp`). La prod ne sert qu'à une vérification **visuelle, anonyme, sans
  mutation** (landing) en fin d'audit.
- ⚠️ Le `.env` local pointe vers la **prod**. Ne pas le modifier : lancer le dev server avec les
  variables TEST injectées par le shell (elles priment sur `.env`, même mécanisme que Playwright) :

```powershell
cd D:\11-coding\YahiaAcademy\yahia-quest-arena
npm run e2e:doctor   # vérifie .env.test complet (secrets masqués)
npm run e2e:setup    # db:push (schéma + contenu) + seed des comptes + reset gameplay
# Puis dev server ciblant TEST (valeurs lues depuis .env.test, ne pas écrire dans .env) :
$env:SUPABASE_URL="<TEST>"; $env:VITE_SUPABASE_URL="<TEST>";
$env:SUPABASE_PUBLISHABLE_KEY="<TEST>"; $env:VITE_SUPABASE_PUBLISHABLE_KEY="<TEST>";
npm run dev
```

- Comptes seedés disponibles (mot de passe : voir `.env.test`, jamais en clair ici) :

| Persona | Compte | Rôle | Premium |
|---|---|---|---|
| Élève freemium | `student.free@e2e.na9ranal3ab.test` | student | non |
| Élève premium | `student.premium@e2e.na9ranal3ab.test` | student | oui (concours) |
| Parent | `parent@e2e.na9ranal3ab.test` | parent | non |
| Admin | `admin@e2e.na9ranal3ab.test` | admin | — |

- Comptes supplémentaires créés à la volée sur TEST si besoin (nouvel élève pour l'onboarding).

## 2. Surface applicative (inventaire routes — base de la cartographie S1)

**Public** : `/` (landing) · `/login` · `/signup` · `/auth` (callback)
**Élève** : `/onboarding` · `/dashboard` · `/themes` (explorer) · `/parcours` + `/parcours/$subjectId`
(carte d'aventure) · `/subject/$subjectId` · `/lesson/$chapterId` · `/quest/$exerciseId` ·
`/dungeon` · `/leaderboard`
**Parent** : `/parent-report`
**Admin** : `/admin/subscriptions` · `/admin/beta-requests` · `/admin/content-reports`

## 3. Grille d'évaluation

Chaque scénario est noté sur 4 dimensions :

| Dim. | Question | Échelle |
|---|---|---|
| **État** | Ça marche ? | ✅ OK · ⚠️ dégradé/incohérent · ❌ cassé |
| **UX** | Fluide, clair, motivant pour un élève de 11-15 ans ? | note libre + sévérité |
| **Valeur** | Contribution à la promesse produit | V1 cœur · V2 support · V3 accessoire |
| **Métier** | La règle de gamification/monétisation est-elle saine ? | note libre |

Constats : `F-NNN` dans le log → consolidés en S3 → les actionnables deviennent des `GAP-NNN`
dans [90-backlog-remediation.md](../../90-backlog-remediation.md).

## 4. Scénarios par persona

### P1 — Visiteur anonyme (public)
- [ ] Landing : proposition de valeur compréhensible en <10 s ? CTA clair ? FR par défaut ?
- [ ] Signup : validations, messages d'erreur, confirmation email (flow réel sur TEST)
- [ ] Login + logout + session expirée ; mot de passe oublié (existe ?)
- [ ] Demande d'accès beta (`beta_access_requests`) : où, comment, qu'est-ce que l'utilisateur comprend ?
- [ ] Accès direct URL protégée sans session → redirection propre

### P2 — Nouvel élève (activation)
- [ ] Onboarding : choix thème/grade → `set_current_parcours` ; clarté des choix (école vs exploration)
- [ ] Dashboard à l'état vide : que voit un compte neuf ? (états vides soignés ou écran mort ?)
- [ ] Chemin vers la première quête : combien de clics ? guidage ?
- [ ] Changement de parcours via `/themes` (explorer) : compréhensible ? réversible ?

### P3 — Élève concours SANS entitlement (funnel freemium → premium)
- [ ] Preview gratuite : quiz de compréhension accessible + missions difficulté 1 ouvertes
- [ ] Mission difficulté ≥ 2 → paywall : message, clarté de l'offre, action proposée (téléphone — réaliste ?)
- [ ] Donjon → gate premium : message cohérent
- [ ] Le funnel donne-t-il envie ? friction au bon endroit ? (jugement marché TN)

### P4 — Élève concours AVEC entitlement (cœur gameplay 9ème)
- [ ] Boucle quête complète : subject → chapter → quiz gate (seuil ≥ `QUIZ_PASS_THRESHOLD_PCT`) → exercices → submit → récompenses (XP, coins, streak, level, hero class)
- [ ] Anti-farm : réponse trop rapide (`tooFast`), score < 60 %, refaire sans améliorer → pas de récompense + message compréhensible par l'élève
- [ ] Consommables (achat boutique → armement → effet → consommation) :
  - [ ] Potion XP / potion coins (multiplicateur appliqué une fois, slot « next-quest » exclusif)
  - [ ] Bouclier retry (échec < 60 % → pénalité SM-2 supprimée, consommé)
  - [ ] Bouclier de streak (passif — test par manipulation de dates en SQL sur TEST, sinon revue de code)
  - [ ] Indices (bouton, décrément ; question sans explication → non consommé)
- [ ] Donjon : run chronométré complet, étages, échec/réussite, récompenses
- [ ] Progression : daily objectives (génération + complétion), weekly quests, badges, SM-2 (révisions planifiées visibles ?)
- [ ] Boutique : achat, équipement skin, inventaire ; solde coins cohérent
- [ ] Leaderboard : scope (par parcours ?), rang, motivation vs découragement
- [ ] Signaler une erreur de contenu : flow complet élève → table `content_reports`

### P5 — Élève 6ème (contenu récent, AR/RTL)
- [ ] Parcours math-6ème + éveil scientifique : rendu AR + RTL, figures SVG lisibles (thèmes sombre/clair)
- [ ] Niveau de langue/difficulté adapté à un élève de 11 ans (jugement)

### P6 — Élève exploration (thèmes gratuits)
- [ ] Culture G (FR/EN/AR = 3 sujets sœurs) : navigation entre langues compréhensible ?
- [ ] IQ-training : figures SVG, résolubilité par déduction
- [ ] Anglais A1→B1 + donjon langue : progression CECR lisible
- [ ] Quiz **non bloquant** hors école (théorie optionnelle) — vérifié
- [ ] Tout est-il vraiment gratuit (pas de gate résiduel) ?

### P7 — Parent
- [ ] Création compte parent + **lien parent-élève** : le process est-il faisable par un parent réel ?
- [ ] Rapport parent : lisible, utile, donne confiance (argument de vente n°1 vers le payeur)
- [ ] Pack famille : entitlement parent → enfants effectif

### P8 — Admin (exploitabilité au lancement)
- [ ] `/admin/subscriptions` : grant/revoke parcours, recherche d'un user, liste des entitlements
- [ ] `/admin/beta-requests` : flow complet demande → approbation → accès effectif
- [ ] `/admin/content-reports` : triage d'un signalement de bout en bout
- [ ] Un non-admin qui force l'URL admin → refus propre (recoupement C3)

### Transverse
- [ ] i18n : bascule FR/EN/AR sur 5 écrans clés (dashboard, quête, leçon, boutique, landing) ; RTL sans casse
- [ ] Mobile (viewport ~390 px) : landing, dashboard, quête, carte parcours, donjon
- [ ] États d'erreur : 404 exercice/sujet inexistant, double soumission, perte réseau pendant une quête
- [ ] Performance perçue : chargements, transitions (subjectif, recoupé par C2)

## 5. Limites assumées
- Les mécaniques multi-jours (streak, SM-2 long terme) : testées par manipulation de dates en SQL
  sur TEST quand c'est raisonnable, sinon par lecture de code — noté comme tel dans le log.
- Le jugement « fun pour un enfant » reste un proxy d'adulte : recommandation prévue de faire
  tester les parcours clés par de vrais élèves (beta testers) — sera formalisée dans le rapport.

## 6. Déroulé en sessions
- **S1** : cartographie statique (code → carte fonctionnelle) + setup env TEST + smoke test P1-P2 → `cartographie.md`
- **S2** : walkthrough élève complet (P3 → P6 + transverse gameplay) → `walkthrough-log.md`
- **S3** : P7-P8 + i18n/mobile/erreurs + matrice valeur + rapport final + versement des GAP au backlog → `rapport-audit-fonctionnel.md`
