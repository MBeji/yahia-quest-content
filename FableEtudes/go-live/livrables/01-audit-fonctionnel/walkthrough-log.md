# C1 — Journal de walkthrough (S2, 2026-06-10)

> Observations en conditions réelles sur le projet Supabase **TEST** (`pqegdnwdtbjtplcthxyp`),
> dev server lancé via `scripts/e2e/dev-on-test.mjs` (garde anti-prod). Comptes seedés (rôles +
> entitlements + reset) via les outils `tools/` (le seed officiel du repo est cassé — voir F-201).
> Findings notés `F-2NN`. Les confirmés sont promus en `GAP-NNN` au [backlog 90](../../90-backlog-remediation.md).

## Setup (fait)
- Env TEST vérifié (`e2e:doctor` ✅). DB à jour (`db push` a appliqué 4 migrations anglais en attente).
- Contenu présent : 6 thèmes · 13 grades · 31 sujets · 146 chapitres · 756 exercices · 4430 questions · 7 parcours · 13 shop_items · 13 badges.
- 4 comptes : `student.free`, `student.premium` (2 entitlements concours actifs), `parent`, `admin`.

## Parcours testés

### P2 — Onboarding nouvel élève (free) → ✅ fonctionnel, i18n cassée
- Login → redirection `/onboarding` (profil sans `current_parcours_id`). OK.
- Étape 1 « Que veux-tu faire ? » (concours / explorer) → étape 2 « Quel concours ? » (9ème / 6ème) → dashboard. Flux clair.
- **F-210 (i18n)** : onboarding **entièrement en FR** alors que la langue active est **EN** (shell de nav, toasts en EN). Aucune traduction de l'onboarding. Visuellement incohérent.

### P3 — Paywall premium (free sur mission difficulté 3) → ✅ gate OK, modèle hors-ligne
- Navigation directe `/quest/<boss d3 9ème>` → écran **« 👑 Défi élite verrouillé »**. Le gate serveur `resolve_exercise_access` fonctionne (accès refusé sans entitlement).
- **F-211 (business / GAP-001)** : la seule voie d'achat affichée est **« contacter l'administrateur » + téléphone +216 55 447 504** + bouton beta. Aucun paiement en ligne. Friction majeure pour un lancement grand public.
- **F-210 (i18n, suite)** : même écran mélange titre FR (« Défi élite verrouillé »), corps EN (« Premium access is unlocked per Concours parcours… »), 2 liens retour (un EN « Back to hall », un FR « Retour à la matière »).

### P4/P6 — Boucle de quête (free, thème libre IQ, 6 questions) → ✅ moteur OK
- Moteur de quête rend correctement : numéro de question, label difficulté **« ⭐ ÉCHAUFFEMENT »**, **figures SVG inline** (matrice IQ visuelle + options A-D en SVG), raccourcis clavier 1-4/A-D.
- Soumission → écran de résultat riche : score, **« SERVER-VALIDATED TIME · 88S »** (transparence anti-triche), barème XP/coins/level/streak, badges débloqués, correction.
- Vérif SQL du chemin d'échec (score 33 % < 60 %) : `attempt` enregistré, profil `xp=0 / streak 0→1`, **3 lignes `spaced_repetition_schedule` pending** (rappels J+1/3/7), badge `first_quest` attribué. Boucle correcte de bout en bout.
- **F-212 (design)** : badge **« Première Quête » attribué sur un échec à 33 %** — `first_quest` se déclenche à la 1ʳᵉ tentative quel que soit le score (à confirmer comme intentionnel).
- **F-210 (i18n, suite)** : écran de résultat mélange EN (titre « Nice try, warrior », « correct answers », boutons) et FR (raison no-XP, nom du badge, classe « Candidat Civil »).
- Note méthodo : le 33 % est un artefact d'automatisation (clic radio + Next dans un même eval synchrone ne laisse pas React committer la sélection), **pas** un bug produit. Le chemin « succès ≥ 60 % » reste à filmer en S2-suite.

### Dashboard élève (free) → ✅ rend, 2 incohérences
- **F-213 (privacy / GAP-015)** : le **« Alliance Code » est l'UUID brut de l'élève** affiché en clair (`CD4D-1A35-7019-413B-89C0-8A6F-9189-6846` = son `user_id`) avec invitation à le partager au parent. UUID exposé, non régénérable (confirme B-9). Angle vie privée → recoupe C3.
- **F-214 (cohérence / A-14)** : « TODAY'S GOAL » est une barre **codée en dur à 100 XP** (`dashboard.tsx:445`), distincte de l'objectif quotidien réel « 3 exercices » (SQL). Deux notions d'objectif coexistent.

## Bugs de logique métier confirmés (SQL/code, déterministes)
- **F-215 (GAP-012, B-2)** : récompenses d'objectifs/quêtes hebdo **jamais créditées**. `submit_exercise_attempt` ne crédite que `exercises.xp_reward` ; la complétion d'un `daily_objectives`/`weekly_quests` passe en `status='completed'` mais ses `xp_reward`/`coin_reward` ne sont ajoutés nulle part (`20260606130000:485-507`). Récompenses affichées (« +50 XP ») non versées.
- **F-216 (GAP-013, B-3)** : **récupération de streak (15 coins) inatteignable**. `recoverStreak` exige `current_streak=0 & longest_streak>0`, mais `award_xp` ne met jamais le streak à 0 (reset ⇒ 1). Confirmé live : 1ʳᵉ activité a fait passer le streak 0→1. Code mort en pratique.
- **F-217 (GAP-014, B-13)** : **l'indice acheté « ×3 » n'en donne qu'1**. `purchase_shop_item` insère toujours `quantity=1` quel que soit l'`effect_payload` ; `booster_hint` vendu `{"hints":3}` (30 coins) → 1 seule révélation. Le payload n'est jamais lu.

## Tooling / CI
- **F-201 (GAP-011)** : le seed e2e officiel (`npm run e2e:setup` → `seed-test-users.mjs`) **échoue** : `admin_grant_parcours` lève `Unauthorized` avec la clé service. Cause racine confirmée : la RPC appelle `is_admin()` qui teste `auth.uid()` = NULL pour un token service via PostgREST. Le commentaire du script (« service-role key bypasses is_admin() ») est faux. ⇒ impossible de provisionner les entitlements premium pour les e2e authentifiés (`test:e2e:auth`) sans contournement. Recoupe C2 (fiabilité CI/e2e).

---

# S2-suite (2026-06-10) — premium, parent, admin, transverse

> Élève **premium** (entitlements concours actifs) sauf mention. Réponses QCM matchées par
> **texte** (l'UI mélange l'ordre des options — voir F-222).

### P4 — Quiz gate école (happy path) → ✅ parfait
- Sujet **Anglais 9ème**, chapitre « Present Tenses » : bandeau **« Comprehension quiz REQUIRED — Pass the quiz to unlock the exercises »**, 4 missions verrouillées (cadenas). Ce n'est PAS le verrou premium (l'élève a l'entitlement) → c'est bien le gate **pédagogique école**.
- **F-220 (✅)** : quiz réussi 100 % → **« ✅ Bravo ! Tu as compris le cours, les exercices sont débloqués »** ; **+20 XP / +5 coins** (barème quiz) ; badge **« Score Parfait »** (perfect_score) ; temps serveur 155 s. Retour au sujet → **« Comprehension quiz ✓ Passed »** (vert) et 4 missions **déverrouillées**.

### P4 — Boucle de succès premium → ✅ récompense réelle
- **F-221 (✅)** : mission Practice d1 réussie 100 % → **+50 XP / +10 coins réels**, confettis, écran « Victory! », « Quest Review » (correction visible — contrairement au quiz qui la masque). Vérif SQL : profil premium **xp=70 (20+50), coins=15 (5+10), streak=1** — comptabilité exacte.
- **F-222 (méthodo / anti-triche ✅)** : l'UI **mélange l'ordre des options** (ex. Q1 : DB `a,b,c,d` → UI `A,B,D,C`). Bonne pratique anti-triche. **Explique le 33 % de S2** (j'avais cliqué par lettre) : c'était un artefact de shuffle, pas un bug. Le matching par texte donne 100 %.
- **B-2 confirmé en live** : daily objective `3_exercises` à **2/3** après quiz+practice, mais le profil n'a que 70 XP (somme des exercices) — l'objectif ne crédite rien (GAP-012).

### P4 — Donjon (premium) → ✅ complet
- Lobby : élève premium **passe le gate d'entitlement** (pas de paywall), mais **gate de prérequis** affiché clairement : « Matières entamées : 1/2, Chapitres entamés : 1/3 ». (Prérequis débloqués via SQL — 2 attempts maths — pour tester le run ; exploite GAP-016.)
- **F-223 (✅)** : run OK — Floor 1 (Anglais B1) → bonne réponse → **Floor 2** ; mauvaise réponse → **« Dungeon Collapsed · You fell at floor 2 »** avec **question fatale + correction** (YOUR ANSWER B / CORRECT C) et **+15 XP** (15/étage), +0 coins (5/5 étages). Barème conforme.
- **F-224 (finding → GAP-019)** : le donjon **mélange les langues** dans un même run (Floor 1 en anglais, Floor 2 en **arabe** — maths). Un élève francophone peut recevoir des questions dans une langue qu'il ne maîtrise pas. Incohérence UX/équité.

### Boutique (premium, +500 coins via SQL) → ✅ achat/équiper/armer
- **F-225 (✅)** : achat **skin Ninja** (−80 coins) → bouton « Equip » → équipé (`avatar_slug='ninja'`, `is_equipped=true`, coins 500→420). Achat **Potion XP x2** (−50) → « Activer » → armée (`is_active=true`, slot next-quest). Tout vérifié en SQL.
- **F-226 (corrige un candidat)** : la **potion `potion_coins` (Pierre Philosophale, coinMultiplier) EXISTE** au catalogue → **infirme** le candidat B (cartographie : « aucune potion coinMultiplier »). Par contre **2 skins samouraï quasi-homonymes** : `skin_samurai` (Armure Samouraï, 100) et `skin_samourai` (Skin Samourai Neon, 500). Descriptions boutique **en FR en base** (non i18n).

### P7 — Parent → ✅ rapport OK
- **F-227 (✅)** : « Rapport de suivi » (FR) — élève « Free Student » **déjà lié** (le lien survit au reset gameplay), classe, niveau, streak, **verdict d'assiduité « Inactif · 0/100 »** (cohérent, free sans activité). Formulaire de liaison Alliance Code présent et clair. Argument de vente n°1 fonctionnel.

### P8 — Admin → ❌ **BUG MAJEUR : consoles admin inaccessibles**
- **F-228 (BUG → GAP-017, P0/P1)** : connecté **admin** (rôle `admin` confirmé en base + nav admin + badge « 6 » reports rendus), les **3 consoles admin** (`/admin/subscriptions`, `/admin/beta-requests`, `/admin/content-reports`) affichent **« Administrators only. »** — accès refusé. Persiste après full reload ET navigation in-app.
  - **Cause racine (lecture de code + repro)** : **collision de `queryKey` React Query**. `_authenticated.tsx:45` et les 3 routes admin utilisent la **même clé** `["me-role", user?.id]`, mais des `queryFn` de **shapes différentes** : le layout retourne un **objet** `{role, current_parcours_id}` (`return data ?? null`), les routes admin attendent une **string** (`return data?.role ?? null`) et testent `role === "admin"`. Le layout parent monte en premier et peuple le cache avec l'objet → la route admin lit l'objet → `objet === "admin"` est **toujours faux** → refus.
  - Preuve : un `fetch` PostgREST de la requête exacte renvoie `[{role:"admin"}]` (status 200) — données/API correctes, le bug est purement client.
  - **Régression probable** : l'ajout de `current_parcours_id` à la requête `_authenticated` (guard onboarding, modèle parcours ~2026-06-08) a changé la shape string→objet, cassant les routes admin qui partageaient la clé.
  - **Impact go-live MAJEUR** : sans console admin, impossible d'**accorder des entitlements (= vendre)**, de **trier les demandes beta**, ni de **modérer les signalements de contenu**. Bloque toute l'exploitation. **Fix simple** : clés distinctes (ex. `["me-role-admin", uid]`) ou lire `me?.role` au lieu de partager la clé.

### Leaderboard → ✅ rend, 2 findings
- **F-229 (finding → GAP-018)** : « Academy Leaderboard » avec onglet Global + **~30 onglets matière** = TOUTES les matières de l'académie (école 9ème+6ème, langues, culture G ×3 langues, IQ), **non scopés au parcours** de l'élève. Surcharge UX. **« Mathématiques » apparaît en double** (maths 9ème et 6ème ont le même `name_fr`) → onglets indistinguables.

### Transverse — RTL/AR + mobile → ✅ excellent
- **F-230 (✅)** : leçon **arabe** (sujet `arabic`, chapitre الأساليب النحوية) en **mobile 375px** : layout **RTL correct** (alignement droite, nav RTL, index/résumé), cours markdown riche et stylé RPG (« سلاحك في التعبير والإقناع »), gras coloré, citation encadrée. Rendu très soigné. Mineur : le compteur de progression en haut s'affiche **« 11 / 4 »** (inversé par le RTL ; la carte « CH. 4/11 » est correcte).
- **F-231 (i18n, renforce GAP-010)** : mix EN/FR confirmé partout (écrans « Victory! » EN + raisons/badges FR ; boutique « Buy »/« Activer » mélangés ; descriptions boutique FR en base).

## Reste à tester (S2-reliquat, non bloquant pour S3)
- Pack famille (parent avec entitlement → enfant lié débloqué) ; level-up réel (accumulation XP) ; états d'erreur réseau ; flux complet « Signaler une erreur » côté élève.

## Comptes / état TEST en fin de session
- TEST seedé proprement en début de session. `student.premium` a de l'activité (anglais + 2 attempts maths injectés, inventaire ninja+potion, ~85 XP). `student.free` lié au parent. Toute reprise redémarre par `tools/fix-test-seed.py` (reset propre).
