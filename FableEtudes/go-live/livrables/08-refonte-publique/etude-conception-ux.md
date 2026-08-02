# Étude & conception — Refonte « plateforme publique gratuite »

> Livrable du chantier **C8 — Refonte plateforme publique & gratuite** (voir
> [`../../08-refonte-plateforme-publique.md`](../../08-refonte-plateforme-publique.md)).
> Portée demandée par Mohamed : **écrans, design UI, messages**. Statut : **conception validée**
> (raffinements actés le 2026-06-21). Ancré sur le code réel de `yahia-quest-arena/`.

---

## 0. TL;DR

On transforme une **académie de jeu, sur inscription, payante au concours** en une
**plateforme de référence publique et 100 % gratuite pour l'école tunisienne (1ère année → Bac,
13 niveaux)**, où le contenu (cours, résumés, exercices) est **accessible sans authentification**.
Le compte ne sert plus qu'à **jouer, gagner des XP, sauvegarder sa progression et se comparer**.

**La bonne nouvelle technique** : ce n'est pas une reconstruction. Le modèle de données porte déjà
les 13 niveaux ; le verrou d'accès est **unique** ; le premium est **isolé** ; les messages sont
centralisés. Le travail est une **réorganisation d'accès + un repositionnement visuel et éditorial**.

**Principe directeur : l'enrichissement progressif.** Un seul arbre de contenu, public par défaut.
Connecté, le **même** écran gagne sa couche de jeu (XP, progression, étoiles, classement). Pas deux
applications parallèles.

> **Périmètre de CE chantier = les *contenants*** (écrans, navigation, structure des parcours,
> design, messages, ouverture de l'accès). **La *production de contenu*** (cours/exercices des 13
> niveaux) est **gérée hors de ce chantier**, dans des sessions dédiées (skills `content-*`). Ici on
> structure et on affiche, on ne rédige pas le contenu pédagogique.

### 4 décisions de cadrage (actées par Mohamed, 21/06)

| # | Décision | Implication conception |
|---|----------|------------------------|
| 1 | **Pratique interactive libre** | L'anonyme peut *répondre* aux QCM (feedback + explication). Compte = sauvegarde/XP/classement. |
| 2 | **Double registre visuel** | Surfaces contenu/adultes **sobres & crédibles** ; surfaces enfant/jeu gardent le **RPG/manga**. |
| 3 | **Élève joue, adultes libres** | Compte surtout pour l'élève-joueur ; parents/enseignants consultent sans compte. |
| 4 | **Tout gratuit, paywall retiré** | Concours gratuits ; suppression des écrans paywall/verrous. **Aucune monétisation ni page « soutien » en v1.** |

### Raffinements actés (21/06)

- **URLs renommées** (FR, lisibles, SEO) — acté.
- **Donjon** : réservé aux **connectés** (mode jeu, **seuil de niveau**), pas de démo anonyme.
- **Compte parent** (suivi enfant) : **backlog** (non urgent).
- **Soutien / don** : **rien en v1** (ni page, ni mention) — 100 % gratuit, point.
- **Reprise des essais anonymes** (localStorage → compte) : **backlog**.
- **Contenu** : produit **ailleurs**, progressivement — **hors périmètre de ce chantier**.
- **🆕 Structure du programme officiel en 3 parcours-cycles, chacun clôturé par un concours**
  (voir §4.3) + **extras hors-programme optionnels** (langues, culture générale, muscle-cerveau).

**⚠️ Conséquence stratégique hors-UI** : ce pivot **supersède le chantier C6 (modèle économique
payant)** et **réoriente C5 (marketing → SEO)** — voir §11.

---

## 1. Vision & repositionnement

### 1.1 Avant → Après

| Dimension | Avant (POC actuel) | Après (cible) |
|-----------|--------------------|----------------|
| **Promesse** | « Deviens un héros, prépare ton concours » | « La référence gratuite de l'école tunisienne, pour toute la famille » |
| **Périmètre** | Surtout 9ème + concours 6ème | **13 niveaux en 3 parcours** (Primaire→6e · Collège→9e · Lycée→Bac), chacun clôturé par un concours |
| **Hors-programme** | Mélangé au reste | **Extras optionnels** séparés (langues, culture G, muscle-cerveau) |
| **Accès** | Login obligatoire (mur d'entrée) | **Public par défaut**, login optionnel |
| **Modèle** | Freemium, parcours concours payants | **100 % gratuit** (aucune monétisation v1) |
| **Public** | Élève-joueur | Élève · **Parent** · **Enseignant** |
| **Identité** | RPG/manga partout | **Double registre** : référence sobre + jeu RPG |
| **Acquisition** | Pub + école pilote (payant) | **+ SEO massif** (contenu indexable, voir §11) |

### 1.2 La marque face au pivot

La marque **« Na9ra Nal3ab » (نقرا نلعب — apprendre en jouant)** reste pertinente, mais son centre
de gravité se déplace : **« Na9ra » (on apprend/lit) devient la promesse publique** (la référence de
cours), **« Nal3ab » (on joue) devient la couche d'engagement** pour l'enfant connecté. Le double
registre traduit exactement cette dualité — c'est la signature, pas une contradiction.

---

## 2. Personas & jobs-to-be-done

| Persona | Contexte | Job principal | Authentification | Registre dominant |
|---------|----------|---------------|------------------|-------------------|
| **L'enfant-élève** | 6-18 ans, mobile/tablette | Apprendre **en s'amusant**, gagner des XP, progresser | **Compte** (le cœur du jeu) | **Jeu (RPG)** |
| **Le parent** | Suit la scolarité | Consulter cours/résumés, trouver des exercices | **Aucun** requis (compte parent **backlog**) | **Référence** |
| **L'enseignant** | Prépare cours/évaluations | Trouver du contenu conforme au programme, **imprimer/exporter** | **Aucun** requis | **Référence** |
| **L'élève autonome (ado/Bac)** | Révise seul | Réviser efficacement (résumés, exos ciblés) | **Optionnel** | Mixte |

**Principe d'accès** : *la valeur de base (consulter, comprendre, s'entraîner) est offerte
immédiatement à tous, sans friction. Le compte n'est jamais un péage — c'est une montée en
puissance (jeu, mémoire, comparaison).*

---

## 3. Principes de conception (les 6 règles)

1. **Public-first, jamais de mur.** Aucun écran de contenu ne redirige vers le login. L'auth est
   *invitée*, jamais *imposée*.
2. **Enrichissement progressif.** Le même écran se densifie quand une session existe (XP, étoiles,
   reprise, indices). Un seul arbre, pas de fork.
3. **Double registre assumé.** *Référence* (sobre, lisible, crédible, imprimable) pour le contenu et
   les adultes ; *Jeu* (RPG/manga, animé) pour l'enfant connecté.
4. **Gratuité totale et visible.** « 100 % gratuit » est affiché. Zéro vocabulaire de verrou
   (`premium`, `débloquer`, `payant`). **Aucune monétisation en v1.**
5. **Cœur officiel + extras optionnels.** Le **programme scolaire officiel** (3 parcours) est le
   cœur ; les contenus **hors-programme** (langues, culture G, muscle-cerveau) sont des **extras
   clairement séparés et optionnels**. Toute l'échelle 1re→Bac est affichée même incomplète
   (« Bientôt »), jamais le vide.
6. **Trilingue & RTL natifs.** FR/EN/AR avec direction adaptée (propriétés logiques CSS).

---

## 4. Architecture d'information & navigation

### 4.1 Le changement structurel : un seul verrou à déplacer

Aujourd'hui (cf. [`src/routes/_authenticated.tsx`](../../../yahia-quest-arena/src/routes/_authenticated.tsx)) :

```
__root  →  _authenticated (REDIRIGE si non connecté)  →  TOUT (dashboard, contenu, jeu…)
```

Cible — on scinde en **deux coquilles** (URLs renommées en FR, **acté**) :

```
__root
 ├─ (public, sans garde, auth-optionnelle)
 │    /                        Accueil repositionné
 │    /programme               Les 3 parcours officiels (cœur)
 │    /parcours/$cycle         primaire | college | lycee → niveaux + bloc concours
 │    /niveau/$grade           Matières d'un niveau
 │    /matiere/$subjectId      Chapitres d'une matière (ex-/subject/$id)
 │    /chapitre/$chapterId     Cours + résumé (ex-/lesson/$id)
 │    /exercice/$exerciseId    Pratique libre (ex-/quest/$id, sans XP si anon)
 │    /extras                  Hors-programme optionnel (langues, culture G, muscle-cerveau)
 │    /connexion               Login/inscription (ex-/auth)
 │
 └─ _compte (garde maintenue — surfaces strictement liées au compte)
      /tableau-de-bord         Dashboard joueur (XP, objectifs, radar…)
      /classement              Leaderboard
      /donjon                  Donjon — **réservé connectés, seuil de niveau** (entraînement concours)
      /profil                  Profil héros, badges, boutique cosmétique
      /demarrage               Onboarding simplifié (ex-/onboarding)
      /admin/*                 Consoles admin
      (/parent                 Espace parent — **backlog**, non v1)
```

**Point clé** : les écrans de **contenu** (`/matiere`, `/chapitre`, `/exercice`) **sortent** de la
coquille gardée et passent en **auth-optionnelle**. Connecté, ils affichent la couche jeu ; anonyme,
le contenu + des invitations douces. Seules les surfaces **intrinsèquement liées au compte** restent
derrière la garde.

> **Migration d'URLs** : avant lancement public, on renomme (les URLs deviennent un actif SEO).
> Prévoir des redirections 301 des anciens chemins (`/subject`, `/lesson`, `/quest`, `/themes`) vers
> les nouveaux si des liens existent déjà.

### 4.2 Navigation selon l'état

| Élément de nav | Anonyme | Connecté (élève) |
|----------------|---------|------------------|
| Accueil / Programme / Extras | ✅ | ✅ |
| Recherche contenu | ✅ | ✅ |
| Cours / Résumés / Exos | ✅ (pratique libre) | ✅ (+ XP, étoiles, reprise) |
| **CTA principal** | **« Créer mon compte gratuit »** | Avatar + XP/niveau |
| Tableau de bord / Classement / Donjon | masqués (« Connecte-toi pour jouer ») | ✅ |
| Sélecteurs langue/thème | ✅ | ✅ |

- **Coquille publique** = en-tête léger (logo, Programme + Extras + recherche, sélecteurs, **1 CTA
  compte**) + **pied de page riche** (sitemap des 3 parcours × niveaux pour le SEO, « 100 % gratuit »,
  mentions légales, contact). **Pas de lien soutien/don.**
- **Coquille compte** = on conserve le **chrome de jeu actuel** ([`_authenticated.tsx`](../../../yahia-quest-arena/src/routes/_authenticated.tsx)), enrichi des chips héros.
- La **bottom-nav mobile** existe déjà → version publique (Programme, Recherche, Mon compte) pour
  l'anonyme, version jeu pour le connecté.

### 4.3 🆕 Hiérarchie du catalogue — 3 parcours officiels + extras

**Le cœur = le programme scolaire officiel tunisien, structuré en 3 parcours-cycles**, chacun
**clôturé par son concours national**. Les 13 niveaux s'y répartissent exactement (6 + 3 + 4) :

| Parcours (cycle) | Niveaux | Aboutit à |
|------------------|---------|-----------|
| **Primaire** | 1re, 2e, 3e, 4e, 5e, **6e** année de base (6) | 🏁 **Concours 6e** (collèges pilotes) |
| **Collège** | 7e, 8e, **9e** année de base (3) | 🏁 **Concours 9e** (lycées pilotes) |
| **Lycée** | 1re, 2e, 3e, **4e** secondaire (4) | 🏁 **Baccalauréat** |

```
/programme  (cœur — école tunisienne officielle)
 ├─ Parcours PRIMAIRE  (1re → 6e) ─────────→ 🏁 Concours 6e
 ├─ Parcours COLLÈGE   (7e → 9e) ──────────→ 🏁 Concours 9e
 └─ Parcours LYCÉE     (1re sec → Bac) ────→ 🏁 Baccalauréat
        └─ /parcours/$cycle → /niveau/$grade → /matiere/$id → /chapitre → cours/résumé/exos

/extras  (optionnel — « pour aller plus loin », hors programme officiel)
 └─ Culture générale · Muscle ton cerveau · Anglais · Français · Arabe
```

- **Le « parcours » reprend son vrai sens** : un **cycle** menant à un **concours** (≠ l'ancien sens
  « parcours premium concours-9eme/6eme »). Resignification importante — impact data model en §10.
- **Le concours = jalon final visible** de chaque parcours (badge « Examen national », bloc dédié en
  fin de cycle), comme **repère pédagogique**, plus comme produit payant.
- **Proposition (à valider) — le concours comme « boss de fin de parcours »** : l'épreuve type
  concours peut être gamifiée via le **Donjon** (déjà réservé aux connectés, à seuil de niveau) =
  l'entraînement-examen chronométré qui couronne le cycle. Cela relie naturellement *donjon
  connectés* ↔ *concours fin de cycle*.
- **Extras** : visuellement et structurellement à part (section « Et aussi / Pour aller plus loin »),
  jamais mélangés au cursus officiel ; 100 % optionnels.
- **Niveaux/matières non encore produits** : carte « Bientôt » (ambition + collecte de demande),
  jamais le vide. (La production est gérée hors de ce chantier.)

---

## 5. Conception écran par écran

Légende : **Aujourd'hui** → **Cible** · *Registre*.

### 5.1 Accueil `/` — *Référence*
- **Aujourd'hui** : landing marketing RPG (héros 3D, « forge ton héros »). Promesse = jeu/concours.
  Fichiers : [`src/routes/index.tsx`](../../../yahia-quest-arena/src/routes/index.tsx), [`src/components/landing/`](../../../yahia-quest-arena/src/components/landing/).
- **Cible** : **page de référence familiale**. Au-dessus de la ligne de flottaison : promesse claire
  (« Tous les cours de l'école tunisienne, gratuitement — de la 1re année au Bac »), **barre de
  recherche/entrée catalogue**, **3 portes persona** (« élève » / « parent » / « enseignant »), et
  un aperçu des **3 parcours**. En dessous : preuve de gratuité, extras, et **une** section « Et pour
  les enfants : apprends en jouant » (seul endroit où le registre RPG apparaît, comme promesse
  secondaire). Le héros 3D et les animations sont **déplacés** dans cette section jeu.

### 5.2 Catalogue `/programme` + `/parcours/$cycle` — *Référence*
- **Aujourd'hui** : `/themes` = hub circulaire de 5 programmes, sert surtout à **changer de
  parcours** (action liée au compte). Fichier : [`src/features/dashboard/components/program-hub.tsx`](../../../yahia-quest-arena/src/features/dashboard/components/program-hub.tsx).
- **Cible** : **explorateur public** structuré en **3 parcours** (Primaire / Collège / Lycée). La
  page parcours montre ses niveaux **dans l'ordre**, se terminant par un **bloc concours** mis en
  avant. Clair, scannable, imprimable, **sans compte ni « parcours actif »**. Les niveaux non
  produits : « Bientôt » + « Préviens-moi ». **Les extras vivent sur `/extras`**, pas ici.
- **Account-bound retiré** : la notion de « parcours actif » disparaît de la navigation publique ;
  elle ne sert plus qu'au connecté pour personnaliser son dashboard.

### 5.3 Matière / Chapitres `/matiere/$subjectId` — *Référence (+ jeu si connecté)*
- **Aujourd'hui** : [`subject.$subjectId.tsx`](../../../yahia-quest-arena/src/routes/_authenticated/subject.$subjectId.tsx) — chapitres, **quiz-gate**, missions, étoiles, **cadenas premium**.
- **Cible** : chapitres avec, pour chacun : **Cours · Résumé · Exercices**.
  - **Anonyme** : tout visible/cliquable ; pas d'étoiles ni de cadenas ; le quiz-gate devient une
    **recommandation non bloquante** (« Commence par le quiz de compréhension »).
  - **Connecté** : réapparaissent étoiles, progression, reprise, quiz-gate **actif**.
  - **Retirer** : tout cadenas/badge `premium` (cf. [`journey-map.tsx`](../../../yahia-quest-arena/src/features/parcours/components/journey-map.tsx), [`subject-path-card.tsx`](../../../yahia-quest-arena/src/features/dashboard/components/subject-path-card.tsx)).

### 5.4 Lecture Cours + Résumé `/chapitre/$chapterId` — *Référence (100 % public)*
- **Aujourd'hui** : [`lesson.$chapterId.tsx`](../../../yahia-quest-arena/src/routes/_authenticated/lesson.$chapterId.tsx) — markdown (cours `lesson_content` + résumé `summary`), TOC,
  figures SVG. **Aucune logique de compte** : déjà 100 % contenu pur. Servi par `getChapterLesson`
  (à passer en auth-optionnelle).
- **Cible** : **l'écran vitrine de la « plateforme de référence »**. Registre Référence :
  typographie de lecture (manuel scolaire moderne), **mode clair par défaut**, largeur confortable,
  **bouton Imprimer/PDF** (clé enseignant), bascule Cours/Résumé nette, partage. Invitation douce en
  bas (anonyme) : « Entraîne-toi sur les exercices — crée un compte pour gagner des XP ».

### 5.5 Exercice / Pratique `/exercice/$exerciseId` — *Mixte*
- **Aujourd'hui** : [`quest.$exerciseId.tsx`](../../../yahia-quest-arena/src/routes/_authenticated/quest.$exerciseId.tsx) — flux QCM **fortement lié au compte** : session anti-triche
  (`start_exercise_session`), `submitAttempt` (XP/coins/badges/spaced-rep), indices = consommables,
  **paywall premium** si difficulté ≥ 2.
- **Cible (décision 1 — pratique libre)** : deux modes sur le **même** écran.
  - **Anonyme — « mode entraînement »** : répond, **correction immédiate + explication**, score
    final. **Aucun** XP/coins/badge/sauvegarde, pas de session anti-triche, indices = révélation
    gratuite. → **RPC de notation sans état** appelable par `anon` (§10) qui **ne dévoile jamais la
    clé** (préserve GAP-020).
  - **Connecté — « mode jeu »** : flux actuel inchangé (récompenses, consommables, spaced-rep).
  - **Retirer** l'écran paywall ([`subscription-paywall.tsx`](../../../yahia-quest-arena/src/features/subscription/components/subscription-paywall.tsx)) du flux.
  - **Écran de fin (anonyme) = moment d'or** : « 8/10 ! 🎉 Crée ton compte gratuit pour transformer
    ça en **+50 XP**, garder ta progression et entrer au classement. » (non bloquant, « Plus tard »).

### 5.6 Dashboard `/tableau-de-bord` — *Jeu (compte)*
- **Aujourd'hui** : [`dashboard.tsx`](../../../yahia-quest-arena/src/routes/_authenticated/dashboard.tsx) — entièrement lié au compte. **Reste gardé** (cœur du mode jeu).
- **Cible** : inchangé sur le fond ; **retirer les cadenas premium** des cartes matières ; le bandeau
  flagship concours passe de « produit » à « repère de fin de parcours ».

### 5.7 Onboarding `/demarrage` — *Jeu (compte)*
- **Aujourd'hui** : [`onboarding.tsx`](../../../yahia-quest-arena/src/routes/_authenticated/onboarding.tsx) — étape **« Concours vs Explorer »** puis parcours (badges Premium).
- **Cible** : **simplifié**, déclenché **après** création de compte (l'anonyme n'a pas d'onboarding,
  il explore directement). Plus de dichotomie payante. Flux : **« Choisis ton parcours »** (Primaire
  / Collège / Lycée) → **« ta classe »** (niveau) → c'est tout. Le reste du catalogue + les extras
  restent explorables librement. **Retirer** tous les badges premium/intention.

### 5.8 Espace parent `/parent` — *Référence (backlog)*
- L'essentiel (consultation cours/résumés/exos) est déjà offert **sans compte**. Le **compte parent**
  (suivi d'un enfant lié — infra `parent_student_links` déjà là) est reporté en **backlog** (non v1).

### 5.9 Affordances enseignant (transverses) — *Référence*
- Pas d'espace dédié en v1. Affordances réutilisables sur les écrans contenu : **Imprimer / Exporter
  PDF** (cours, résumé, fiche d'exercices **avec corrigé**), marqueur **« conforme au programme
  officiel »**, partage. (Espace classe/assignations = backlog.)

> *(L'ancienne section « /soutien » est supprimée : aucune monétisation ni page soutien en v1.)*

---

## 6. Design UI — le système à double registre

### 6.0 Direction visuelle validée (21/06 — sur maquettes)

Validée sur **5 maquettes haute-fidélité** (accueil, catalogue 3 parcours, lecteur de cours, fin
d'exercice anonyme, dashboard jeu). Tokens d'accent retenus :

| Registre | Fond | Accent principal | Surfaces |
|----------|------|------------------|----------|
| **Référence** | Clair (mode clair par défaut) | **Teal `#0F6E56`** (fills `#E1F5EE`) | Accueil, programme/parcours, extras, cours/résumé, exercice anonyme, adultes |
| **Jeu** | Sombre `#15120d` | **Doré `#EFA32A`** (`#FAC775`) | Dashboard, quête jouée, donjon, classement, profil |
| **Sémantique** | — | succès / erreur (vars CSS) | correction d'exercice (vert/rouge), états |

Principes confirmés sur maquettes : **sentence case** partout, **concours = jalon doré** (trophée)
en fin de parcours, **invitation compte = gain (XP), jamais blocage** (bouton « Plus tard »
toujours présent), **zéro lexique premium**, **URLs FR** visibles, état **« Bientôt »** assumé.
RTL/AR + dark mode adaptatifs. Les 5 maquettes font foi comme **référence d'implémentation** : le
registre Jeu = le thème sombre doré **actuel conservé** ; le registre Référence = nouvelle base
claire teal.

### 6.1 Définition des deux registres

| | **Registre RÉFÉRENCE** | **Registre JEU** |
|---|------------------------|-------------------|
| **Où** | Accueil, programme/parcours, extras, cours/résumé, exos (anon), enseignant | Dashboard, quête jouée, donjon, classement, profil/badges/boutique |
| **Public** | Parent, enseignant, élève qui lit | Enfant/élève connecté |
| **Mood** | Clair, crédible, « manuel scolaire moderne » | RPG/manga, héroïque, animé |
| **Couleur** | Mode **clair par défaut**, neutres + 1 accent sobre | Sombre, gold-sheen, glows |
| **Typo** | Lisibilité (corps généreux), Noto Kufi pour AR | Titres display, effets |
| **Motion** | Discret, fonctionnel (`prefers-reduced-motion`) | Confettis, level-up, canvases 3D |
| **Densité** | Aérée, scannable, imprimable | Dense, riche en feedback |

### 6.2 Un seul design system, deux peaux

- **Tokens communs** : couleurs (variables CSS `--subject-*`, `--gold`…), espacement, primitives
  shadcn/Radix, i18n + RTL, accessibilité (ARIA déjà là).
- **Bascule par la coquille** (`data-register="reference"` vs `"play"`), pas par conditions
  éparpillées. Le thème clair actuel sert de base au registre Référence.
- **Garde-fou bundle** : chrome de jeu lourd (canvases 3D, confettis) **lazy** et **exclusif à la
  coquille compte** → coquille publique légère, **rapide en SSR** (atout SEO + 3G tunisienne).
  Surveiller via `npm run build:check`.

### 6.3 Composants nouveaux / retouchés

| Composant | Action | Registre |
|-----------|--------|----------|
| `PublicHeader` / `PublicFooter` | **Nouveau** : en-tête léger + pied SEO (sitemap 3 parcours × niveaux) | Référence |
| `PersonaDoors` | **Nouveau** : 3 portes élève/parent/enseignant (accueil) | Référence |
| `CycleCatalog` / `ParcoursOverview` | **Nouveau** : 3 parcours, niveaux ordonnés, bloc concours, états « Bientôt » | Référence |
| `ExtrasSection` | **Nouveau** : extras optionnels séparés du cœur | Référence |
| `LessonReader` | **Retouche** : typographie lecture, imprimer/PDF, partage | Référence |
| `PracticeRunner` | **Retouche** de `quest` : mode entraînement anon (sans récompense) | Mixte |
| `AccountInvite` | **Nouveau** : invitation compte non bloquante (réutilisable) | Pont |
| `subscription-paywall` | **Supprimer** du flux (aucune page soutien en v1) | — |
| Badges `premium`/cadenas | **Supprimer** (journey-map, subject cards, dungeon) | — |

---

## 7. Messages & copywriting

### 7.1 Stratégie éditoriale

- **Ton par registre** : Référence = clair, respectueux ; **« vous »** parent, **« tu »** élève. Jeu
  = ludique, héroïque.
- **Bannir** le lexique de péage (`premium`, `débloquer`, `verrouillé`, `concours payant`,
  `abonnement`). **Affirmer** la gratuité totale.
- **L'invitation au compte est récurrente mais douce** : toujours un **gain** (« gagne des XP »,
  « garde ta progression »), jamais une condition d'accès, toujours une sortie (« Plus tard »).

### 7.2 Nouveaux moments de message (exemples)

| Moment | Message (exemple FR) | Où |
|--------|----------------------|----|
| **Promesse d'accueil** | « Tous les cours de l'école tunisienne. De la 1re année au Bac. **Gratuit, pour toute la famille.** » | `/` |
| **Preuve gratuité** | « 100 % gratuit, sans abonnement. » | `/`, footer |
| **Parcours** | « Primaire · Collège · Lycée — chaque parcours te mène jusqu'à ton concours. » | `/programme` |
| **Invitation post-cours** | « Tu as lu le cours ? Entraîne-toi maintenant 💪 » | `/chapitre` |
| **Invitation post-exo (anon)** | « 8/10 ! Crée ton compte **gratuit** pour gagner +50 XP et garder ta progression. » | fin `/exercice` |
| **Valeur du compte** | « Avec un compte : XP, badges, classement, reprise là où tu t'es arrêté. » | `AccountInvite` |
| **Niveau à venir** | « La 3e année arrive bientôt — **préviens-moi**. » | `/parcours/$cycle` |
| **Extras** | « Pour aller plus loin : langues, culture générale, logique. » | `/extras` |
| **Concours** | « Prêt pour le Concours 9e ? Entraîne-toi en conditions d'examen. » | fin parcours / donjon |

### 7.3 Plan i18n (fichiers [`src/lib/i18n`](../../../yahia-quest-arena/src/lib/i18n))

Travail systématique sur `fr.ts` / `en.ts` / `ar.ts` (typés contre `types.ts`). Effort **modéré** :

| Namespace | Action |
|-----------|--------|
| **`subscription`** | **Supprimer/retirer** de l'UX (paywall/grant/premium). Pas de namespace « soutien » (rien en v1). |
| **`onboarding`** | **Simplifier** : retirer `intent*`/`concours*`/`explore*` → « choisis ton parcours / ta classe ». |
| **`parcours`, `explorer`** | **Retirer** `premium`, `premiumHint`, `locked`, `lockedHint`. Réutiliser `parcours` pour les **3 cycles**. |
| **`auth`** | **Recadrer** : « Forge ton héros » → « Crée ton compte gratuit » (ton héros conservé côté *jeu*). |
| **`landing`** | **Réécrire** : promesse référence + gratuité + 3 parcours + 3 personas. |
| **`layout`** | Libellés nav (Programme, Extras, Recherche, Mon compte). |
| **`account` / `invite`** | **Nouveau** : invitations douces (§7.2). |
| **`cycles` / `catalog`** | **Étendre** : 3 parcours, libellés concours, états « Bientôt », « conforme au programme ». |
| **`print` / `share`** | **Nouveau** : imprimer/exporter/partager (enseignant). |

> Rappel piège (mémoire projet) : en **arabe**, garder les **chiffres occidentaux** et se méfier de
> l'aplatissement U+00A0 (`reference_ar_content_nbsp`) — côté contenu, pas i18n d'interface.

---

## 8. Le moment d'authentification (« soft auth »)

- **Jamais de redirection** vers le login depuis un écran de contenu (suppression de l'`useEffect`
  global de [`_authenticated.tsx`](../../../yahia-quest-arena/src/routes/_authenticated.tsx) pour les routes déplacées).
- **L'auth est contextuelle, motivée par un gain** atteint *là, maintenant* :
  - Fin d'un exercice réussi → « transforme ce score en XP ».
  - Clic sur Classement/Donjon → « rejoins le classement / entraîne-toi pour le concours » (seuls
    cas où l'action *exige* le compte, présentés comme invitation).
- **Reprise des essais anonymes** (localStorage → compte) : **backlog** (gain de conversion futur).
- **Bénéfice conformité** : moins de collecte par défaut → **allège** le sujet mineurs/INPDP
  (GAP-003/024) sur la navigation publique.

---

## 9. Parcours utilisateurs cibles

1. **Parent pressé (sans compte)** : Google « cours 9ème maths inéquations » → `/chapitre/...` (SEO)
   → lit, imprime le résumé → explore d'autres chapitres. **0 friction, 0 compte.**
2. **Enfant curieux → joueur** : accueil → « élève » → parcours Collège → 9e → une matière → exo en
   mode entraînement → 9/10 → invitation → **crée son compte** → onboarding « parcours + classe » →
   bascule mode jeu (XP, héros). **Conversion par la valeur.**
3. **Enseignant** : `/programme` → Lycée → matière → imprime la fiche d'exercices **avec corrigé**.

---

## 10. Impacts techniques (cadrage — pas l'implémentation)

1. **Middleware auth-optionnelle.** Créer `optionalSupabaseAuth` à côté de
   [`requireSupabaseAuth`](../../../yahia-quest-arena/src/shared/integrations/supabase/auth-middleware.ts) : JWT présent → client authentifié ; sinon → **client `anon`**. Les server
   fns de **contenu** basculent dessus et adaptent leur retour selon `userId`.
2. **RLS — rouvrir le contenu à `anon`.** La migration `20260522153000` a restreint `exercises` et
   `questions` à `authenticated`. Ajouter des policies **`anon` SELECT** limitées à `source='admin'`
   (et **jamais** `questions.correct_option` côté client — préserver GAP-020). Migration additive.
3. **RPC de notation publique sans état** `check_answers(exercise_id, answers)` callable par `anon` :
   renvoie correct/incorrect + explications **sans** session/attempt, **sans** XP, **sans** exposer
   la clé. **Rate-limit** anti-abus.
4. **Restructuration des routes** + **renommage** (redirections 301 des anciens chemins). Contenu
   hors `_authenticated` ; garde réduite au sous-arbre compte.
5. **Débranchement premium.** `resolve_exercise_access` → toujours « autorisé » ; supprimer paywall
   et cadenas (§6.3) ; **donjon : seuil de niveau** au lieu du gate entitlement. Tables
   `parcours_entitlements` laissées dormantes. **Aucune brique de paiement/soutien.**
6. **🆕 Resignification du concept `parcours`.** Aujourd'hui `parcours` = un `(theme, grade)` (avec
   `concours-9eme`/`concours-6eme` premium). Cible : **3 parcours-cycles** couvrant **N niveaux**
   chacun et culminant sur un concours. → revoir la granularité (`profiles.current_parcours_id`, la
   résolution `(theme,grade)`, l'onboarding « parcours puis classe »). À cadrer en implémentation,
   **sans toucher au contenu**.
7. **SEO** (transverse, voir §11) : SSR propre des pages contenu, métadonnées/OpenGraph par page,
   sitemap des 3 parcours × niveaux, URLs lisibles.
8. **Definition of Done** (CLAUDE.md) préservée : tests qui voyagent, gate vert, migrations
   coordonnées. Chaque lot = PR conventionnelle.

---

## 11. Conséquences stratégiques (hors UI — à reprendre ailleurs)

- **C6 « Modèle économique » est superseded.** Plus de business plan payant (pack année, TAM
  concours). **Aucune monétisation en v1** (décision Mohamed). Pérennité = **coûts d'infra à
  l'échelle gratuite** (déjà cadrés par paliers en C4) — pas de don/soutien pour l'instant.
- **C5 « Marketing » réorienté — et renforcé : le SEO devient LE canal.** Chaque cours/résumé/exo
  est une page indexable (« cours 9ème maths Tunisie »…). → exige SSR propre, metas/OG par page,
  sitemap, URLs lisibles (§10.7). **Reco** : axe SEO explicite.
- **Go/No-Go allégé** : l'item « parcours d'achat opérationnel » **disparaît** ; le volet
  mineurs/INPDP **s'allège** (moins de collecte par défaut) sans disparaître (comptes élèves).

---

## 12. Découpage en lots (roadmap)

| Lot | Contenu | Dépend de | Effort |
|-----|---------|-----------|--------|
| **L0 — Ouverture de l'accès** | `optionalSupabaseAuth` · RLS anon (exos/questions) · RPC `check_answers` · restructuration + **renommage** routes (301) · débranchement premium · **donjon → seuil niveau** | — | M |
| **L1 — Écrans contenu (Référence)** | Accueil repositionné · **catalogue 3 parcours + bloc concours** · extras séparés · matière/chapitre · lecteur cours/résumé (+ imprimer) · exo mode entraînement · i18n/messages | L0 | L |
| **L2 — Couche jeu (enhancement)** | XP/étoiles/reprise sur écrans connectés · `AccountInvite` · **onboarding « parcours + classe »** · resignification `parcours`/cycles | L0, L1 | M |
| **L3 — Personas adultes** | Affordances enseignant (imprimer/exporter/partager) | L1 | S |
| **Transverse** | SEO (SSR/metas/sitemap 3 parcours) · rate-limit RPC publique · perf coquille publique · analytics funnel | — | M |
| **Backlog** | Compte parent · reprise essais anonymes · espace classe enseignant | — | — |
| **Hors périmètre** | **Production du contenu des 13 niveaux** (sessions dédiées, skills `content-*`) | — | — (ailleurs) |

**MVP du pivot = L0 + L1** : l'accès public + les écrans de référence + la structure 3 parcours.

---

## 13. Risques & points d'attention

| Risque | Impact | Mitigation |
|--------|--------|------------|
| **Contenu incomplet sur 13 niveaux** | Promesse « toute l'école » creuse | États « Bientôt » + collecte de demande ; **production pilotée hors de ce chantier** ; communiquer « gratuit, en construction » |
| **Exposition de la banque de réponses** (anon) | Triche / fuite clés | RPC `check_answers` serveur-autoritaire, clé jamais côté client (GAP-020) ; rate-limit |
| **Abus de la RPC publique** | Charge / scraping | Rate-limit + cache ; contenu public de toute façon |
| **Resignification `parcours`** (data model) | Régression onboarding/dashboard | Cadrer en L2, migration prudente, tests pgTAP ; ne pas toucher au contenu |
| **Divergence des 2 registres** | Dette UI | Un seul design system + bascule par coquille |
| **Régression sécurité (RLS ouvertes)** | Fuite données joueur | N'ouvrir que `source='admin'` en SELECT ; ne jamais toucher `profiles`/`attempts` ; pgTAP |
| **Pérennité sans revenus** | Coûts | Infra cadrée par paliers (C4) ; gratuité assumée v1 |

---

## 14. Décisions actées (21/06) — synthèse

| Sujet | Décision |
|-------|----------|
| Renommage des URLs | ✅ **Oui** (FR, SEO) + redirections 301 |
| Donjon sans premium | ✅ **Réservé connectés**, seuil de niveau (entraînement concours) |
| Compte parent | ⏳ **Backlog** (non v1) |
| Soutien / don | ❌ **Rien en v1** — 100 % gratuit |
| Reprise des essais anonymes | ⏳ **Backlog** |
| Production de contenu | ↗️ **Hors de ce chantier** (sessions dédiées) |
| Structure du programme | ✅ **3 parcours** (Primaire→6e · Collège→9e · Lycée→Bac), chacun → concours |
| Hors-programme | ✅ **Extras optionnels séparés** (langues, culture G, muscle-cerveau) |

---

*Fin de l'étude. Prochaine étape : soit **maquettes des écrans clés** (accueil + catalogue 3 parcours
+ lecteur de cours) pour valider la direction visuelle, soit **plan d'exécution L0 + L1** (PRs +
Definition of Done).*
