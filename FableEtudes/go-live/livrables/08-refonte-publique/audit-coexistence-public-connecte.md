# Audit — Coexistence « monde public anonyme » vs « monde connecté »

> Livrable **post-MVP** du chantier **C8 — Refonte plateforme publique & gratuite** (voir
> [`../../08-refonte-plateforme-publique.md`](../../08-refonte-plateforme-publique.md)).
> Complète l'[`etude-conception-ux.md`](./etude-conception-ux.md) (conception *avant* build) par un
> **audit de code de l'existant** *après* livraison du MVP (L0+L1) en prod. Ancré sur le code réel de
> `yahia-quest-arena/`. Date : **2026-06-23**. Méthode : 5 explorations parallèles (navigation,
> thème, contenu, données, gamification) recoupées.
>
> **Portée** : comparer la coexistence des deux mondes sur 6 axes (thème · parcours utilisateurs ·
> navigation · contenu · code redondant · code commun), trancher la **meilleure option par axe**,
> évaluer l'**UX**, et définir comment **donner de la valeur au mode connecté** (futur premium,
> gratuit pour l'instant). Alimente le lot **L2** et les GAP **036 / 039 / 042 / 043** + **035**.

---

## 0. TL;DR

Le mental model « deux versions parallèles qui dupliquent tout » est **faux** : le MVP C8 a déjà
unifié le contenu. **La coexistence n'est pas un problème de contenu dupliqué — c'est un problème de
*coquille* (shell) dupliquée.** Deux layouts épinglent deux registres visuels opposés
([`_public.tsx`](../../../yahia-quest-arena/src/routes/_public.tsx) sobre/teal ·
[`_authenticated.tsx`](../../../yahia-quest-arena/src/routes/_authenticated.tsx) gamifié/or), et **le
même contenu se rend sous la coquille publique, qu'on soit connecté ou non**. Un enfant connecté qui
lit un cours **perd toute trace visuelle de son compte** (ni XP, ni profil, ni retour) — au pic
d'engagement.

> **Clé de voûte** : le registre est lié à **l'arbre de routes**, pas à **l'état d'authentification**.
> C'est exactement l'inverse du principe directeur de la conception (étude §3.2 — « enrichissement
> progressif : le même écran se densifie quand une session existe ; un seul arbre, pas de fork »). Le
> MVP a livré la moitié **Référence** ; la moitié **enrichissement** (lot **L2**) n'est pas encore
> construite. **Cet audit opérationnalise L2.**

La seule **vraie redondance de code** résiduelle est unique : le rendu d'un QCM
([`practice-exercise.tsx`](../../../yahia-quest-arena/src/features/quest/components/practice-exercise.tsx)
public vs le bloc inline de
[`quest.$exerciseId.tsx`](../../../yahia-quest-arena/src/routes/_authenticated/quest.$exerciseId.tsx)
connecté, ~80 % dupliqué). Le reste des divergences est **intentionnel** (double registre, validé
21/06).

---

## 1. Le constat structurant

**Contenu déjà unifié (acquis C8).** Les anciennes routes connectées
[`_authenticated/subject.$subjectId`](../../../yahia-quest-arena/src/routes/_authenticated/subject.$subjectId.tsx)
et [`_authenticated/lesson.$chapterId`](../../../yahia-quest-arena/src/routes/_authenticated/lesson.$chapterId.tsx)
ne sont plus que des **redirections 301** vers `/matiere` et `/chapitre`. Les composants de contenu
(`SubjectHub`, `LessonReader`, `PracticeExercise`) sont **partagés**, montés sous la coquille
publique. La **lecture des données** est unifiée : un seul middleware `optionalSupabaseAuth` sert les
deux mondes en branchant sur `userId`.

**Ce qui reste « deux mondes »**, ce sont les **coquilles** : le registre visuel et la navigation
changent selon que l'URL est `/matiere|/chapitre` (sobre) ou `/dashboard|/quest` (gamifié) — pas
selon que l'utilisateur est connecté. D'où le **whiplash** : un connecté enchaîne or (dashboard) →
teal (cours/matière) → or (quête) pour le *même* sujet.

Schéma avant/après en [§6](#6-schéma-avantaprès).

---

## 2. Synthèse par axe

| Axe | État actuel | Verdict | Meilleure option |
|-----|-------------|---------|------------------|
| **Contenu** | Unifié : `SubjectHub` / `LessonReader` partagés ; 1 pipeline markdown sanitizé | 🟢 **Excellent** (déjà fait) | Statu quo — continuer le modèle C8. |
| **Code commun (données)** | 1 middleware de lecture (`optionalSupabaseAuth`) branchant sur `userId` ; sécurité propre | 🟢 **Très bon** | Garder ; solder 2 dettes mineures. |
| **Code redondant** | **1 seul foyer** : rendu QCM ~80 % dupliqué (`PracticeExercise` ↔ `quest.$exerciseId`) | 🟡 **À corriger** | Extraire un `<QcmQuestionCard>` partagé. |
| **Thème / double registre** | 3 palettes / 2 axes ; registre **lié au layout**, pas à l'auth | 🟡 **Concept bon, implémentation incohérente** | Garder le double registre, **le piloter par l'auth/type de page**. |
| **Navigation** | 2 shells ; transition anon→inscription **casse le contexte** ; pas de retour connecté→public ; mobile public appauvri | 🔴 **Maillon faible** | `returnTo` + HUD compte persistant + nav mobile publique. |
| **Parcours utilisateur** | Anonyme fluide ; à l'inscription → atterrissage forcé `/dashboard`/`/onboarding`, **perte du chapitre** | 🔴 **Rupture de conversion** | Threader l'URL d'origine ; onboarding non bloquant. |

---

## 3. Détail & meilleure option par axe

### 3.1 Contenu — 🟢 ne rien dédupliquer
Un écran de matière (`SubjectHub`), un lecteur de cours (`LessonReader`), un pipeline markdown
unique sanitizé DOMPurify ([`markdown.ts`](../../../yahia-quest-arena/src/shared/lib/markdown.ts)).
**Meilleure option : statu quo.** Seul reliquat = le QCM (§3.3).

### 3.2 Code commun (données) — 🟢 modèle de référence
`getSubject` / `getChapterLesson` / `getExercise` sont anon-capables et enrichissent derrière
`if (userId)` ([`quest.server.ts`](../../../yahia-quest-arena/src/features/quest/quest.server.ts)).
**Sécurité sans faille identifiée** : `questions.correct_option` / `explanation` sont `REVOKE`d et ne
sortent que par RPC `SECURITY DEFINER` (`check_answers` anonyme stateless, `get_attempt_review`
authentifié) ; l'anon ne voit que `source='admin'`. **Meilleure option : garder.** Deux dettes au
backlog (→ **GAP-042** / transverse SEO S3) :
- Rate-limit anonyme **en mémoire par IP** → non distribué sur Vercel multi-instance.
- **Double résolution** « ce parcours est-il débloqué » entre `getSubject` et `getDashboard`.

### 3.3 Code redondant — 🟡 le seul refactor à fort levier
Le cœur de rendu d'une question (prompt + options A/B/C/D shufflées + états correct/faux +
explication) est réimplémenté **~80 % à l'identique** côté public (`PracticeExercise`, stateless
`check_answers`) et côté connecté (bloc inline de `quest.$exerciseId`, scoré `submit_exercise_attempt`).
Seules les primitives bas-niveau (`OptionContent`, `shuffleOptions`) sont partagées.
**Meilleure option :** extraire un composant **`<QcmQuestionCard>`** (présentation pure, prop
`register` sobre/gamifié) ; les parents gardent leur logique propre (correction one-shot vs session
scorée + chrome). Bénéfice double : déduplication **et** convergence du thème. À cadrer avec **GAP-042**
(sprint qualité) — recoupe la dette « routes monolithiques » (la route quête fait ~770 lignes).

### 3.4 Thème / double registre — 🟡 garder le concept, changer le pilotage
Le double registre est **stratégiquement juste** (validé 21/06 : Référence sobre = confiance / SEO /
parents-enseignants ; Jeu = enfants engagés) et la marque l'incarne (« Na9ra » / « Nal3ab »). Trois
défauts de cohérence d'implémentation :
1. **Registre lié au layout** → whiplash or/teal/or, et **valeur du compte invisible** sur le contenu.
2. **Trois vocabulaires « doré »** : teal Référence, tokens `--gold` du registre Jeu, et **ambre
   Tailwind brut** dans le bloc Jeu de la landing
   ([`public-landing.tsx`](../../../yahia-quest-arena/src/components/public/public-landing.tsx)).
3. `theme-color` PWA figé `#0a0a0a` quelle que soit la peau ; couleurs de correctness mélangées
   (`emerald-*` littéral vs token `--success`).

**Meilleure option (clé de voûte) : découpler « registre » de « arbre de routes ».** Le registre doit
être fonction de **(état d'auth, type de page)**, appliqué par une **coquille adaptative** — pas par
`_public` vs `_authenticated`. Sur les routes de contenu partagées : un **anon** voit la chrome
sobre + CTA compte ; un **connecté** voit la même page + **HUD compte persistant** (XP / streak / coins
+ retour dashboard) et l'accent or. Règle d'un coup la cohérence visuelle, la navigation et la
visibilité de la valeur du compte. **C'est la matérialisation de l'étude §3.2 (enrichissement
progressif) et le cœur des GAP-043 + GAP-036.**

### 3.5 Navigation — 🔴 le maillon faible
- **Transition anonyme→inscription cassée** : aucun `returnTo`. Les CTA signup mènent à `/auth` sans
  URL d'origine ; après succès, navigation **en dur vers `/dashboard`**
  ([`auth.tsx`](../../../yahia-quest-arena/src/routes/auth.tsx)) + possible détour `/onboarding`.
  **L'anon qui s'inscrit en plein chapitre perd tout son contexte.**
- **Mobile public appauvri** : Programme, Extras et Connexion sont tous en `sm:` → sur smartphone, la
  nav publique = logo + langue + « Créer mon compte ». Pas de catalogue ni de login mobile, **pas de
  bottom-nav publique** (contrairement au connecté).
- **Retour connecté→public quasi inexistant** ; pas de fil d'Ariane ; `LessonReader` n'a pas de lien
  « retour à la matière ».
- **Vocabulaire divergent** : « Programme / Extras / niveau / matière » (public) vs « Hall des Héros /
  Parcours / Découvrir / Donjon » (connecté) — un même connecté voit les deux.

**Meilleure option :** (1) `returnTo` de bout en bout, (2) HUD compte persistant (cf. 3.4), (3) nav
mobile publique (menu ou bottom-nav + login mobile), (4) breadcrumbs légers + retour matière.

### 3.6 Parcours utilisateur — 🔴 refermer la boucle de conversion
Le parcours anonyme est fluide (accueil → catalogue → matière → cours → entraînement corrigé). La
rupture est **au passage au compte** : atterrissage forcé loin du point d'engagement + onboarding
bloquant ([`_authenticated.tsx`](../../../yahia-quest-arena/src/routes/_authenticated.tsx), garde
`useEffect`). **Meilleure option :** après inscription, **revenir exactement où on était**, avec la
tentative en cours sauvegardée ; rendre l'onboarding **différable**. (Aligne le backlog C8 « reprise
des essais anonymes ».)

---

## 4. Évaluation UX

**Forces**
- Contenu 100 % ouvert sans login → acquisition, SEO, confiance parents/enseignants.
- Sécurité d'accès anonyme propre (clés de réponse jamais exposées).
- Gamification **riche et réellement câblée** (XP, streak, badges, donjon, boutique, classement,
  objectifs, rapports parent).

**Faiblesses**
1. **Whiplash de registre** : le connecté change 3 fois de peau dans un seul parcours.
2. **Conversion qui fuit** : signup sans `returnTo`, perte de contexte, onboarding-péage.
3. **Valeur du compte invisible au bon moment** : en lisant un cours ou en s'entraînant (pic
   d'engagement), rien ne montre ce qu'un compte apporterait.
4. **Mobile public** sous-équipé.
5. **Valeur dormante non montrée** (cf. §5.B).
6. **Crédibilité AR** : termes non-arabes résiduels dans le rendu des matières (→ **GAP-039**).

---

## 5. Donner de la valeur au mode connecté (et préparer le premium)

**Fait majeur :** aujourd'hui le premium est **gratuit** (override de beta `supabase/test-phase/`,
hors migrations versionnées — l'état réel de prod ne se déduit pas du repo). Donc **le vrai delta
anonyme → compte gratuit n'est PAS le contenu premium** (l'anon voit déjà le catalogue débloqué) —
**c'est toute la gamification**. Problème : cette valeur est **réelle mais invisible** dans le flux
public sobre.

### Échelle de valeur à 3 niveaux (claire & monétisable)

| Niveau | Qui | Ce qu'il a | Rôle | Registre |
|--------|-----|------------|------|----------|
| **0 · Anonyme** | tout visiteur | Lire les cours + s'entraîner avec correction/explications | Acquisition, SEO, confiance | Sobre (Référence) |
| **1 · Compte gratuit** | inscrit | TOUTE la gamification : XP, streak, badges, **sauvegarde & reprise**, classement, objectifs, journey map, **révisions espacées**, rapports parent | Engagement, rétention | Gamifié (HUD persistant) |
| **2 · Premium (futur payant)** | famille concours | Profondeur examen : **concours 9ème/6ème difficulté ≥2**, **donjon**, **family pack**, suivi de maîtrise avancé | Monétisation | Gamifié + |

### Levier A — rendre la valeur du compte VISIBLE dans le flux anonyme (conversion)
- Après une correction d'entraînement anonyme, afficher la **récompense fantôme** : « Avec un compte,
  tu aurais gagné **+X XP**, débloqué le badge *Perfectionniste*, et **sauvegardé** ta progression. »
  (Le CTA existe déjà après correction — il suffit de le charger en valeur concrète.)
- **Teaser** du classement / de la carte d'aventure / du streak en lecture seule pour l'anon.
- Dramatiser la **non-persistance** : « ta progression ne sera pas sauvegardée ».

### Levier B — activer la VALEUR DORMANTE (déjà codée, non montrée) — ROI maximal, faible coût
- 🥇 **Répétition espacée (SM-2)** : le moteur écrit déjà le planning J+1/J+3/J+7, et
  `getSprint2Dashboard` **lit déjà** `pendingSpacedReps`… mais **aucune UI ne l'affiche**. Une vue
  « Tes révisions du jour » est un levier de rétention énorme, quasi gratuit.
- **Narration audio des cours** (`theory_scrolls` existe en base, **0 référence dans `src/`**) :
  différenciateur fort, parké (cf. note mémoire « Réviser le cours » = label mort).
- **Badges** : moteur riche, **seulement 4 règles** câblées → ajouter maîtrise par matière, paliers,
  donjon (recoupe **GAP-037** : échelle 50 niveaux scientifiques).
- **Classement par matière** existe mais peu visible ; objectifs/quêtes figés à 2+2 sans rotation.
- **Social** : groupes / défis (→ **GAP-041**) = valeur d'engagement future du compte.

### Frontière premium recommandée
Garder le **compte gratuit = jeu complet** (crée l'habitude + la base d'utilisateurs) et réserver au
**payant la profondeur examen** : concours difficulté ≥2 + donjon + family pack + (à terme) narration
& maîtrise avancée. Le free preview actuel (quiz de compréhension + difficulté 1) est le bon produit
d'appel — à garder. **⚠️ Go-live blocker connu** : exécuter `close-premium.sql` /
`revoke-all-premium.sql` avant tout lancement payant (déjà tracé C8).

---

## 6. Schéma avant/après

> Rendu interactif produit en session (SVG). Version texte ci-dessous pour archive.

```
①  AUJOURD'HUI — MVP L0+L1 (en prod)
                         __root
                ┌──────────┴───────────┐
        _public (sobre/teal)     _authenticated (jeu/or)
                │                        │
        Contenu partagé            Gameplay
        matière·cours·exercice  ◄┈┈ dashboard·quête·donjon
                                  301   (/subject·/lesson)

   Parcours connecté = 3 peaux :  [Dashboard or] → [Cours teal] → [Quête or]
   ⚠ Registre lié à la route → valeur du compte invisible sur le contenu.

②  CIBLE — lot L2 · enrichissement progressif
                         __root
                           │
                  Coquille adaptative          (registre = f(auth, type de page))
                           │
                  1 seul arbre de contenu
                  matière · cours · exercice
                ┌──────────┴───────────┐
        Anonyme (teal)            Connecté (or)
        Référence sobre +         même écran + HUD (XP·streak·retour)
        CTA « créer un compte »   → valeur du compte visible

   Un seul arbre, pas de fork. Le compte enrichit l'écran au lieu de le remplacer.
```

---

## 7. Recommandations priorisées

| # | Action | Axe | Impact | Effort | Rattachement |
|---|--------|-----|--------|--------|--------------|
| **1** | **Coquille adaptative + HUD compte persistant** sur le contenu (découpler registre ↔ route) | Thème + Nav + Valeur | 🔥🔥🔥 | M-L | **L2** · **GAP-043** · **GAP-036** · **GAP-035** |
| **2** | **`returnTo`** au signup/login + reprise du contexte (+ tentative en cours) | Parcours | 🔥🔥🔥 | S-M | backlog C8 « reprise essais anonymes » |
| **3** | **Activer la répétition espacée** (UI « révisions du jour ») | Valeur dormante | 🔥🔥🔥 | S | **L2** |
| **4** | **Récompense fantôme** après entraînement anonyme | Conversion | 🔥🔥 | S | **L2** (AccountInvite) |
| **5** | Extraire **`<QcmQuestionCard>`** partagé | Code redondant | 🔥🔥 | M | **GAP-042** (routes monolithiques) |
| **6** | **Nav mobile publique** (menu/bottom-nav + login mobile) | Nav | 🔥🔥 | S | **GAP-036** |
| **7** | Aligner les **3 vocabulaires dorés** + `theme-color` dynamique + tokens correctness | Thème | 🔥 | S | **GAP-036** |
| **8** | Onboarding **non bloquant** ; breadcrumbs + retour matière | Parcours/Nav | 🔥 | S | **L2** |
| **9** | Dettes données : rate-limit anon distribué ; dédupe résolution parcours | Code commun | 🔥 | S | **GAP-042** · SEO S3 |
| **10** | Badges supplémentaires + rotation objectifs/quêtes ; narration audio ; groupes/défis | Valeur | 🔥 | M | **GAP-037** · **GAP-041** |
| — | Crédibilité AR : purger les termes non-arabes du rendu matière | UX/contenu | 🔥 | S | **GAP-039** |

**La clé de voûte est la reco #1.** Tant que le registre est lié à l'arbre de routes, le connecté
perd son contexte sur le contenu et la valeur du compte reste invisible. La régler débloque
simultanément la cohérence visuelle, la navigation et la perception de valeur — donc la conversion
et, plus tard, le premium. Elle **fusionne et donne un cap** aux GAP-036 (public fade), GAP-043
(refonte connecté + parité) et GAP-035 (gate visuel matière), tous aujourd'hui épars.

---

## 8. Cohérence avec C8 (décisions déjà actées)

- **Double registre** : confirmé pertinent (décision 21/06). Cet audit ne le remet pas en cause — il
  corrige son **pilotage** (auth, pas route).
- **Enrichissement progressif** (étude §3.2) : c'est le principe directeur de la conception ; le MVP
  n'en a livré que la moitié Référence. Reco #1 = l'autre moitié = **L2**.
- **Premium réversible / override beta** : inchangé ; le revert avant launch reste un blocker tracé.
- **Tokens** : Référence teal `#0F6E56` / Jeu doré `#EFA32A` (étude §6.0) — à conserver ; le HUD
  connecté réutilise le registre Jeu existant.
- **Tests** : la reco #1 restaurera les e2e du gate visuel matière (**GAP-035**) et élargit la
  couverture (**GAP-038**).
