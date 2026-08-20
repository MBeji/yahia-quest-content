# Étude 29 — Mode IA « à la clé de la famille » (BYOK) : la porte, le coffre et la Forge

> **Statut** : brouillon — Q-1…Q-9 à arbitrer (§7)
> **Priorité** : 29 · **Valeur** : l'étage IA du produit s'allume **sans budget plateforme et
> sans sortir de la phase gratuite** — la famille qui veut l'IA branche sa propre clé et paie
> son propre modèle ; le produit reste entier, à l'identique, pour celles qui n'en branchent
> pas · **Complexité** : haute (secret d'un tiers stocké et exécuté pour le compte d'un mineur,
> multi-fournisseur, première dépense d'argent réel déclenchée depuis l'app)
> **Architecte** : Opus 5, 2026-08-16 · **Exécuteur cible** : Sonnet (ou équiv.)
> **Dépend de** : **étude 11 (validée, A5 du 2026-07-20)** — cette étude en est la **porte
> d'accès alternative**, pas une variante : elle **reprend et remplace son lot 0** (D-1, Q-1) et
> laisse ses lots 1-7 intacts · étude 04 lot A0 ✅ · étude 07 lot 1 ✅ · `parent_student_links`
> + `is_parent_of_student` (en prod depuis `20260522153000`)
> **Bloque** : rien. **Débloque** : l'exécution de é11 sans la décision de budget qui la tient
> à octobre (ROADMAP §3 étape E, lignes 17-19)
> **Docs normatifs liés** : AGENTS.md · ARCHITECTURE.md · `docs/environment-variables.md` ·
> `docs/logging-standard.md` · `docs/xss-rendering-policy.md` ·
> `docs/content-voice-and-composition.md` (registres) · `content-engine/references/math-and-notation.md` ·
> skill `claude-api` (ids de modèles et prix courants **au moment de l'implémentation**)

---

## 1. Contexte & objectif produit

### 1.1 Le problème : l'étage IA est écrit, validé, dégelé — et éteint

L'étude 11 est **validée depuis le 2026-07-20** (arbitrage A5), son exécution est **dégelée pour
les lots 0-2**, son architecture est fermée jusqu'aux gabarits de prompts. Elle n'a produit
**aucune ligne de code**. Vérifié dans le moteur le **2026-08-16**, sur `main` :

| Vérification                                  | Constat                                                              |
| --------------------------------------------- | -------------------------------------------------------------------- |
| Dépendance LLM dans `package.json`            | **aucune** (`anthropic`, `openai`, `ai-sdk`, `langchain` : 0 occurrence) |
| `src/features/tutor/`                         | **inexistant**                                                        |
| Migration portant `tutor_*` ou `ai_usage_events` | **aucune**                                                         |
| Appel réseau vers un fournisseur de modèles   | **aucun**                                                             |

La ROADMAP l'écrit sans détour : « **IA — non commencé, conforme au plan. À J-22, la cible
octobre est désormais l'hypothèse par défaut, pas le repli.** » Ce qui la tient là n'est ni la
conception (fermée), ni la faisabilité (é11 §3 est exécutable tel quel), ni un gel (A5 l'a levé) :
c'est **une dépense récurrente à engager par une plateforme sans revenu**, en pleine phase
gratuite. A5 a chiffré le plafond — 5 $/jour, ≤ 150 $/mois — et ce plafond est raisonnable ; il
n'en reste pas moins une décision d'argent que rien n'oblige à prendre maintenant, et une
décision non prise se traduit par un rang 9 dans une file qui en compte plus.

### 1.2 Le retournement : la famille qui veut l'IA la paie

Le mode IA n'a pas besoin d'être financé par la plateforme pour exister. Il a besoin d'**une
clé d'API valide**. Cette étude ouvre la voie où **c'est la famille qui la fournit** :

- le parent colle sa clé (Anthropic, OpenAI, ou tout fournisseur compatible de la liste blanche)
  dans une console dédiée, choisit son modèle, pose un plafond mensuel ;
- il **active** le mode pour tel ou tel de ses enfants liés ;
- côté élève, le mode IA s'allume : explications personnalisées, chat cadré, plan commenté,
  bilans — et la **Forge**, le générateur de quiz personnalisés que cette étude livre (§2.3) ;
- côté plateforme, le coût marginal est **nul**, et le budget de A5 reste disponible pour ce
  qu'il finance déjà (le chemin plateforme, §1.3).

Les conséquences dépassent le financement, et l'une d'elles est un piège :

1. **Le calendrier se libère.** L'étage IA cesse d'être une décision de trésorerie ; il redevient
   une décision d'ingénierie. Les lots 0-2 de é11 deviennent prenables dès que la porte existe.
2. **Le wording reste propre.** Rien n'est vendu, rien n'est monnayé : aucune surface ne dit
   « premium », « abonnement » ni « payant » (é15 D-3 intact). La famille ne paie pas *l'app*,
   elle paie *son fournisseur*, directement, hors de l'app. Nous ne touchons pas un centime — et
   c'est une propriété à défendre, pas un manque à gagner (D-12).
3. **Le garde-fou du coût disparaît, et c'est le piège.** Dans é11, le budget plateforme est un
   frein structurel : à 5 $/jour, l'abus s'arrête tout seul. En BYOK, **le frein est la carte
   bancaire d'un parent** — donc il n'y en a plus côté produit. Tous les plafonds que é11 tenait
   « aussi » pour des raisons de coût (énergie, plafond dur, bornes de tokens) doivent être
   **re-fondés sur la pédagogie et la protection de la famille**, et complétés par des plafonds
   monétaires explicites (R-9 à R-12). Une étude BYOK qui se contente de retirer le budget
   livre une facture surprise à une famille tunisienne. Celle-ci ne le fait pas.
4. **Le mode devient inégalitaire.** Une clé d'API suppose un compte fournisseur et une carte
   internationale — en Tunisie, ce n'est pas la norme. Le BYOK n'est donc **pas** la voie d'accès
   du grand nombre : c'est une voie *supplémentaire* pour les familles qui le peuvent
   (RISK-3, et Q-5 en tire la conséquence : le chemin plateforme n'est pas supprimé).

### 1.3 Une seule porte, deux payeurs

L'invariant de é26 D-8 — **une seule porte LLM runtime** — n'est pas assoupli : il est *rempli*.
Cette étude ne crée pas un second moteur IA à côté de celui de é11 ; elle livre **le** socle, en
lui ajoutant la seule chose que é11 n'avait pas prévue : *de qui vient la clé*.

```
                    ┌──────────────────────────────────────────┐
   une seule porte  │  résolution de crédential (§3.4)          │
                    │  1. clé de la famille  → payeur = family  │  ← é29
                    │  2. clé plateforme     → payeur = platform│  ← é11 (budget A5)
                    │  3. aucune             → mode IA éteint   │
                    └──────────────────────────────────────────┘
```

La chaîne est ordonnée, testée, et **le mode « éteint » est un état de première classe** : c'est
l'état par défaut de tout le monde, et le produit y est complet (R-1).

### 1.4 Indicateurs de succès (KPI)

Tous calculables depuis les tables de cette étude — aucun tracker tiers.

- **Ouverture de l'étage IA** : nombre de lots é11 exécutés dans les 60 jours suivant le lot 3
  de é29 (le KPI honnête de cette étude : elle réussit si é11 démarre, pas si des clés sont
  saisies).
- **Adoption** : nombre de familles avec une clé `active` ; % d'élèves liés dont le mode est
  activé ; médiane des interactions IA/semaine par élève activé.
- **Tenue de la facture** : dépense mensuelle médiane par famille (**cible : ≤ 3 $**) ; % de
  familles ayant atteint leur plafond (cible < 10 % — au-delà, le plafond par défaut est mal
  calibré, pas la famille) ; nombre de dépassements **non** stoppés par le produit : **cible 0,
  strictement** (un seul est un incident, RISK-2).
- **Qualité sous modèle libre** : taux de rebut de la Forge (cible < 20 % ; > 50 % sur une
  famille ⇒ conseil de modèle, R-19) ; ratio 👍/👎 par modèle (le tableau qui dira si un modèle
  bon marché tient la barre — donnée que personne n'a aujourd'hui).
- **Sécurité** : 0 fuite de clé (mesuré, pas espéré : test pgTAP d'absence de privilège §5, garde
  de log, revue de bundle) ; 0 appel émis avec la clé d'une famille pour un travail qui ne sert
  pas ses propres élèves (R-13, journalisé).
- **Dégradation** : % de sessions IA retombées en déterministe (panne fournisseur, clé invalide,
  plafond atteint) **sans erreur visible pour l'élève** (cible : 100 % des dégradations sont
  silencieuses côté élève et explicites côté parent).

### 1.5 Ce que l'epic ne cherche PAS à faire

- **Pas un second moteur IA.** é26 D-8 : la porte est unique. Cette étude *est* le socle ; é11
  garde ses lots 1-7 sans y toucher (annexe B).
- **Pas de revente, pas de marge, pas de proxy commercial.** Nous n'intermédions pas une
  facturation : la clé du parent appelle son fournisseur, la relation commerciale reste entre
  eux (D-12). Aucun compteur de l'app ne fait foi devant une facture.
- **Pas de clé côté client, jamais.** Ni en base locale, ni en cookie, ni en mémoire du
  navigateur, ni dans une réponse d'API (D-3, D-4, RISK-1).
- **Pas de contenu généré au catalogue.** La ligne rouge de é12 et le D-10 de é11 tiennent :
  éphémère, non noté, jamais promu, jamais partagé hors de la famille (R-16, R-17).
- **Pas d'IA obligatoire.** Aucune fonctionnalité existante ne devient dépendante d'une clé.
  L'app sans clé est exactement l'app d'aujourd'hui (R-1) — invariant vérifié par les tests.
- **Pas de prix affiché à l'élève.** Un enfant ne voit jamais ni dollar, ni token, ni
  « il te reste 0,42 $ » : il voit l'énergie de é11, une mécanique de jeu (R-14).
- **Pas de service après-vente du fournisseur.** L'app diagnostique et nomme l'erreur
  (annexe C) ; elle n'explique pas comment recharger un compte OpenAI.
- **Pas de clé partagée entre familles**, pas de « clé de la classe », pas de clé d'enseignant
  en v1 (hors périmètre §2.6 ; le canal enseignant est é08).

---

## 2. Spécification fonctionnelle

### 2.1 Acteurs & surfaces

| Acteur                  | Ce qu'il peut faire                                                                                                                                                     |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Parent** (`role='parent'`) | Attacher / vérifier / remplacer / révoquer **une** clé ; choisir fournisseur + modèles ; poser les plafonds ; activer le mode par enfant lié ; lire la dépense et la qualité ; couper. **Seul acteur autorisé à saisir une clé en v1** (R-2, Q-2). |
| **Élève** (`role='student'`) | Utiliser les surfaces IA **si** un parent lié les a activées pour lui ; voir son énergie ; ne voit **jamais** ni clé, ni fournisseur en clair, ni montant (R-14).      |
| **Admin**               | Couper globalement ou par famille ; lire l'agrégat (jamais un transcript, jamais une clé) ; voir les taux de rebut et de 👎 par modèle.                                    |
| **Anonyme**             | Rien. Aucune surface IA hors `_authenticated`.                                                                                                                             |

Surfaces nouvelles : **la rubrique « Réglages » (`/settings`)**, dont le **Mode IA** est une
section — c'est là, et nulle part ailleurs, que la clé se saisit (D-16) — et **la Forge** (§2.3),
atteignable depuis le hub d'un chapitre et depuis le dashboard élève. Les surfaces IA de é11
(panneau de review, chat, plan, bilans) restent chez é11 et n'apparaissent pas ici.

⚠️ **La rubrique Réglages n'existe pas encore** — constaté dans le moteur le 2026-08-17 : aucune
route `settings`/`réglages`/`profil` sous `_authenticated`, et les préférences d'aujourd'hui sont
éparpillées hors de toute page (sélecteur de langue et de thème dans l'en-tête, carte d'opt-in
push dans la feature `notifications`). Le lot 2 la **crée**, avec le Mode IA pour première
section. Deux conséquences fermes :

1. **Le lot 2 crée la page, pas le déménagement.** Langue, thème, notifications et compte ont
   vocation à y venir — ils **n'y viennent pas dans ce lot** (ce serait une refonte UX déguisée,
   territoire é14/é15). Ils sont nommés ici pour que personne ne construise une seconde page de
   réglages six semaines plus tard.
2. **`/settings` doit être atteignable dans le shell parent.** Vérifié dans
   `src/routes/_authenticated.tsx` : le parent a un shell **Suivi-only** (pas de nav de jeu, un
   seul lien vers `/parent-report`). Si l'entrée Réglages n'est ajoutée qu'à la nav élève, le
   propriétaire de la clé ne peut littéralement pas atteindre l'écran où il la saisit. C'est un
   critère d'acceptation du lot 2, pas un détail d'intégration.

### 2.2 Parcours (user stories)

- **US-1 — Attacher une clé.** Réglages → section « Mode IA » → « Activer le mode IA » → écran de consentement (§3.8,
  texte versionné) → choix du fournisseur → collage de la clé → choix des modèles (liste curée +
  saisie libre d'un id) → plafonds (défauts proposés) → « Vérifier et enregistrer ».
- **US-2 — Vérification.** À l'enregistrement, l'app émet **un** appel minimal (≤ 16 tokens de
  sortie, prompt fixe) vers le fournisseur pour prouver que la clé et le modèle répondent. Succès
  ⇒ `status='active'`, `verified_at` posé. Échec ⇒ **la clé n'est pas enregistrée** et l'erreur
  est nommée en clair (annexe C : clé invalide / modèle inconnu / crédit épuisé / réseau).
- **US-3 — Activer par enfant.** La console liste les enfants liés (`parent_student_links`) ;
  pour chacun : interrupteur, sélection des surfaces autorisées (explication, chat, Forge,
  bilans), plafond d'énergie quotidien. Défaut à la création : **tout éteint** (R-3).
- **US-4 — Poser les plafonds.** Plafond **mensuel** famille et plafond **journalier** famille,
  en dollars, avec les défauts de Q-6. Alertes à 50 % / 80 % / 100 % (e-mail parent + bandeau
  console). À 100 % : coupure, mode dégradé, aucune erreur visible pour l'élève (R-11).
- **US-5 — L'élève voit que le mode est allumé.** Un état, pas une publicité : le panneau de
  révision propose « Demander au Prof », la Forge apparaît dans le hub du chapitre, l'énergie
  s'affiche. Aucune mention de clé, de fournisseur, de coût. Si le mode est éteint, **rien ne
  s'affiche du tout** — pas de bouton grisé, pas de teasing (R-1, R-14).
- **US-6 — Forger un quiz** (§2.3).
- **US-7 — Suivre la dépense.** Réglages › Mode IA : dépense estimée du jour / du mois, par enfant et par
  surface, nombre d'appels, tokens, taux de rebut de la Forge, ratio 👍/👎, et l'avertissement
  permanent : **« estimation — la facture qui fait foi est celle de votre fournisseur »** (R-12).
- **US-8 — Révoquer.** Un bouton, un effet immédiat : la ligne chiffrée est **supprimée**
  (pas marquée), toutes les activations enfants tombent, la dépense historique reste (agrégats
  sans secret). L'écran rappelle le geste qui compte vraiment : **révoquer la clé chez le
  fournisseur** (nous ne pouvons pas le faire à sa place).
- **US-9 — La panne.** Fournisseur en erreur, clé devenue invalide, crédit épuisé, plafond
  atteint : côté élève, la surface IA **disparaît** et le produit déterministe reprend la main
  sans message d'erreur ; côté parent, la console affiche l'état, le code et la date (annexe C),
  et un e-mail part **une fois** par transition d'état (pas à chaque appel).

### 2.3 La Forge — le générateur de quiz personnalisé (livrable signature de cette étude)

C'est la surface que é11 n'a pas : son lot 5 génère des exercices *que le tuteur choisit* pour
combler une lacune détectée. La Forge est l'inverse — **l'élève demande**, sur un périmètre qu'il
choisit, et obtient un quiz jouable immédiatement.

**Ce que l'élève choisit** (tout est déterministe, aucun de ces champs n'est décidé par le modèle) :

| Champ      | Valeurs                                                                                        |
| ---------- | ------------------------------------------------------------------------------------------------ |
| Périmètre  | un **chapitre** de son parcours · une **compétence** (é07) · **« mes erreurs »** (tags actifs é04) |
| Volume     | 5 · 8 · 10 questions (jamais plus — R-18)                                                        |
| Difficulté | ⭐ à ⭐⭐⭐⭐, défaut = celle que `difficulty_adaptation` lui donnerait                            |
| Format     | QCM 4 options (v1). Les types natifs (`numeric`, `multi`, `ordering`, `matching`) sont **hors v1** |
| Langue     | imposée : `subjects.content_language` de la matière (R-3 de é11) — pas un choix                  |

**Ce que la chaîne fait ensuite** (§3.6 pour le détail technique) : contexte fermé (cours du
chapitre + 3 questions du catalogue **comme référence de style, jamais à recopier**) → génération
de N+2 candidats en sortie structurée → filtres déterministes (schéma zod miroir du pipeline
contenu, notation, doublon catalogue, vocabulaire d'âge) → **double résolution indépendante**
(un second appel résout sans voir la clé déclarée ; désaccord ⇒ rebut) → au moins N validés, ou
échec honnête (« la Forge n'a pas réussi à écrire un quiz correct — réessaie ou change de
périmètre »).

**Ce que le quiz forgé est, et n'est pas** :

| Il est                                                       | Il n'est pas                                                                    |
| ------------------------------------------------------------ | --------------------------------------------------------------------------------- |
| Jouable dans le lecteur de quête existant                    | Noté : **aucun XP, aucune pièce, aucun badge, aucune série** (R-16, é11 R-11)   |
| Éphémère : `expires_at` à 30 jours, rejouable jusque-là     | Écrit dans `question_attempts` (é11 D-10 — la télémétrie de é04 reste pure)     |
| Étiqueté « écrit par l'IA de ta famille — signale une erreur » | Promu au catalogue, proposé à une autre famille, ni indexé (R-17)               |
| Compté dans la dépense de la famille, avant génération       | Gratuit : c'est **l'action la plus chère du produit** (annexe A) — énergie 3     |

**Estimation avant dépense** : l'écran de la Forge affiche, *avant* de lancer, le coût estimé
(« ≈ 0,20 $ ») sur le modèle configuré. Pour l'élève : rien, jamais (R-14) — l'estimation est
côté parent, et l'élève ne voit que le coût en énergie.

### 2.4 Règles métier

L'exécuteur référence ces numéros dans ses tests. Les règles de é11 (R-1…R-18) restent en
vigueur telles quelles pour ses propres surfaces ; celles-ci s'y ajoutent et ne les contredisent
jamais.

- **R-1 — Le produit sans clé est le produit d'aujourd'hui.** Aucune fonctionnalité existante ne
  devient conditionnée par une clé. Aucune surface IA n'est visible sans mode actif : pas de
  bouton grisé, pas d'appel à l'action, pas de « bientôt ». Testé : le rendu de chaque écran
  touché est identique, à l'octet de DOM près sur les zones concernées, mode éteint.
- **R-2 — Seul un adulte lié attache une clé.** `role IN ('parent','admin')`, vérifié **en SQL**
  dans la RPC d'écriture, jamais seulement dans l'UI. Un compte `student` ne peut pas en attacher
  une, même en appelant la RPC directement (pgTAP obligatoire).
- **R-3 — L'activation est explicite, par enfant, par surface.** Une clé enregistrée n'allume
  rien. Le défaut de toute activation est **éteint**. Un enfant délié (`parent_student_links`
  supprimé) perd l'accès **immédiatement** (résolu à chaque appel, jamais mis en cache côté client).
- **R-4 — La clé n'est jamais lisible.** Aucune API, aucune RPC, aucun log, aucune réponse
  d'erreur, aucun export ne rend la clé, en clair ou chiffrée. La console affiche `sk-…4f2a`
  (4 derniers caractères) et rien d'autre. Une clé enregistrée ne peut être que **remplacée**.
- **R-5 — La clé ne sort pas du serveur.** Elle est déchiffrée en mémoire dans du code
  `.server.ts`, utilisée pour un appel, et jamais écrite ailleurs — ni fichier, ni cache, ni
  variable de module, ni trace d'erreur. Toute exception remontant d'un appel fournisseur est
  **re-typée** avant de sortir (annexe C) : le corps d'erreur brut du fournisseur n'est jamais
  propagé (certains y répètent un fragment de clé).
- **R-6 — Le fournisseur est dans la liste blanche.** Fournisseur ∈ liste fermée ; `base_url`
  d'un fournisseur compatible ∈ `AI_ALLOWED_HOSTS` (constante serveur), **https** obligatoire,
  pas de littéral IP, pas de plage privée, aucune redirection suivie. Un hôte hors liste est
  refusé à l'enregistrement **et** re-vérifié à chaque appel (RISK-7).
- **R-7 — Un appel IA porte toujours un payeur.** `payer ∈ ('family','platform')` est résolu
  server-side avant l'appel et écrit dans `ai_usage_events`. Aucun appel n'est émis sans payeur
  identifié — c'est la condition pour qu'aucune dépense ne soit orpheline.
- **R-8 — La clé d'une famille ne sert que ses élèves.** Jamais un travail de plateforme (batch
  nocturne, pré-génération, audit, test, évaluation de modèle, tâche d'administration), jamais un
  élève non lié. Vérifié à la résolution ; toute violation est un incident de sécurité.
- **R-9 — L'énergie de é11 reste, et son plafond devient un réglage parental.**
  `TUTOR_DAILY_ENERGY` reste le défaut ; le parent peut le baisser, et le monter **jusqu'à**
  `TUTOR_HARD_DAILY_CAP` — jamais au-delà. Le plafond dur ne se règle pas : ce n'est pas un
  garde-fou de coût, c'est un garde-fou pédagogique (é09 : anti-farm, é11 R-12).
- **R-10 — Bornes de tokens non négociables.** `maxTokens` par surface est une constante serveur
  (é11 §3.11) ; ni le parent, ni l'élève, ni le modèle configuré ne les modifient. Un contexte
  qui dépasse est tronqué par la règle de découpage, jamais élargi.
- **R-11 — Double plafond monétaire, coupure atomique.** Avant **chaque** appel, la dépense
  estimée du jour et du mois pour cette famille est comparée à ses plafonds, dans la même
  transaction que la réservation d'énergie. Dépassement ⇒ appel non émis, dégradé é11 R-15,
  parent notifié une fois. Le plafond mensuel par défaut n'est pas nul (Q-6).
- **R-12 — Le montant affiché est une estimation, et le dit.** Calculé depuis les tokens
  rapportés par le fournisseur × une table de prix **datée** en code. Aucune surface ne le
  présente comme une facture ; la mention de renvoi au fournisseur est permanente, pas une
  note de bas de page.
- **R-13 — Traçabilité du payeur dans la qualité.** `ai_usage_events` porte le `provider` et le
  `model` réels de chaque appel. Un 👎 ou un rebut est imputable au modèle qui l'a produit — sinon
  la console qualité mélange les fournisseurs et ne veut plus rien dire.
- **R-14 — L'élève ne voit jamais d'argent.** Ni montant, ni token, ni nom de fournisseur, ni
  « il te reste X appels ». Il voit l'énergie (mécanique de jeu, é11 R-12) et le contenu. Cette
  règle est absolue, y compris dans les états d'erreur et les e-mails.
- **R-15 — Le cache d'explications est privé à la famille** (D-9, Q-3). Une réponse produite par
  la clé d'une famille n'est jamais servie à une autre. Le cache partagé de é11 (D-6) reste
  valable pour le **payeur plateforme** uniquement ; les deux espaces sont disjoints, séparés par
  une colonne, pas par une convention.
- **R-16 — Le contenu forgé ne rapporte rien.** Aucun XP, pièce, badge, série, classement,
  progression de chapitre, ni écriture dans `question_attempts` / `attempts` / `spaced_repetition_schedule`.
- **R-17 — Le contenu forgé ne quitte pas la famille.** Non promu, non partagé, non indexé, absent
  du sitemap, absent des surfaces publiques, purgé à 30 jours. Le signalement d'une erreur sur un
  item forgé va au canal IA (§3.9), **jamais** dans la file `content_reports` du catalogue.
- **R-18 — La Forge est bornée.** ≤ 10 questions par quiz, ≤ N+2 candidats générés, ≤ 3 quiz
  forgés par élève et par jour (constante), 1 génération concurrente par élève (verrou), énergie 3.
- **R-19 — Un modèle qui ne tient pas la barre est nommé.** Taux de rebut > 50 % sur 7 jours pour
  une famille ⇒ bandeau dans la console parent : ce modèle échoue trop souvent, voici ceux qui
  passent. Jamais de bascule automatique vers un autre modèle : c'est la clé du parent, donc son
  choix (D-11).
- **R-20 — Consentement versionné, préalable, révocable.** Aucune donnée d'élève n'est transmise
  à un fournisseur avant que le parent ait accepté un texte **versionné** listant ce qui part et
  ce qui ne part pas (§3.8). Un changement de fournisseur ou de version du texte redemande le
  consentement. La révocation coupe tout, immédiatement.

### 2.5 i18n & RTL

- **Réglages › Mode IA et Forge** : microcopy FR/EN/AR livrée **dans la même PR** que le code
  (é11 R-18), namespace `ai.*` (plus `settings.*` pour la coquille de la rubrique), registre
  parent pour les Réglages (vouvoiement, é15) et registre élève pour la Forge (tutoiement).
  Fichiers : `src/lib/i18n/{fr,en,ar}.ts`.
- **RTL** : la console est un formulaire dense (clé, plafonds, tableaux de dépense) — captures FR
  **et** AR exigées à la revue (é15 R-5). La clé masquée `sk-…4f2a` est du contenu **LTR** dans un
  contexte RTL : `dir="ltr"` explicite sur ces champs, sinon le masque se lit à l'envers (piège
  déjà payé sur les tableaux de cours, arena#712).
- **Contenu forgé** : dans la langue d'enseignement de la matière, jamais celle de l'interface
  (é11 R-3) ; notation `math-and-notation.md`, chiffres 0-9 y compris en arabe.

### 2.6 Hors périmètre (v1)

- Clé attachée par un **élève majeur** (Q-2) · clé de **session** non persistée (D-4 alt.) ·
  clé d'**enseignant** ou de classe (c'est é08) · **plusieurs clés** par famille ou par matière.
- **Fournisseurs locaux** (Ollama, LM Studio) : un `base_url` privé est structurellement
  incompatible avec R-6 et avec un serveur hébergé (RISK-7).
- **Multimodal** (photo d'énoncé, voix), **types natifs** dans la Forge, **promotion** d'un item
  forgé au catalogue, **correction par LLM d'une réponse libre** (é20 tranche déterministe —
  laisser un modèle noter serait la seule surface où l'IA déciderait, ce que D-3 de é11 interdit).
- **Facturation, reventes, crédits, parrainage** : rien de commercial, dans aucun sens.

---

## 3. Architecture technique (décisions fermées)

### 3.1 Vue d'ensemble

```
Parent ── /settings › Mode IA                   Élève ── surfaces IA (é11) + Forge (é29)
   │  server fns : createServerFn                  │  server fns / SSE (é11 lot 3)
   │  + requireSupabaseAuth + zod                  │
   ▼                                               ▼
set_ai_credential / revoke / set_access      orchestrateur (src/features/ai/*.server.ts)
   │                                               1. resolve_ai_access(student, feature)  ← SQL : R-1/R-2/R-3/R-9
   │  chiffre en Node (AES-256-GCM)                2. reserve_ai_spend(family, estimate)   ← SQL : R-11 (atomique)
   ▼                                               3. charge le secret (service_role)      ← R-5, mémoire seule
public.ai_credentials  ── AUCUN grant client ──┤   4. déchiffre + AiProvider.{generate,stream}
   (ciphertext seul ; la clé de chiffrement       5. valide la sortie (é11 §3.4)
    vit dans l'env Vercel, jamais en base)        6. log_ai_usage(payer, provider, model, tokens, cost)
                                                  7. libère / ajuste la réservation
```

Trois séparations portent toute la sécurité de l'étude, et aucune n'est une convention :

1. **Le SQL décide, Node déchiffre.** Aucune fonction SQL ne voit jamais la clé en clair ; aucun
   code Node ne décide seul du droit d'appeler. Les deux moitiés doivent tomber d'accord.
2. **La table du secret n'a aucun chemin client.** `REVOKE ALL … FROM anon, authenticated` :
   PostgREST ne peut pas l'atteindre, quelle que soit la policy. Une erreur de RLS ne suffit donc
   pas à produire une fuite — il faudrait aussi une erreur de grant *et* la clé de chiffrement.
3. **Le secret et sa clé ne vivent pas au même endroit.** Chiffrement enveloppe : le coffre est en
   base, la clé du coffre est dans l'environnement Vercel. Un dump de base volé (y compris une
   sauvegarde de `db-backup.yml`) ne rend rien d'exploitable.

### 3.2 Le coffre — chiffrement enveloppe (spécification exacte)

Primitive : **AES-256-GCM** via `node:crypto` (aucune dépendance nouvelle ; ni `pgcrypto`, ni
`pgsodium`, ni Vault — D-5).

| Élément            | Valeur                                                                                                     |
| ------------------ | ------------------------------------------------------------------------------------------------------------ |
| Clé maîtresse (KEK) | `AI_KEY_ENC_KEY` — 32 octets, base64, **jamais** préfixée `VITE_`. Absente ⇒ le coffre refuse d'écrire et de lire, et le mode IA famille est éteint (le mode plateforme, lui, continue) |
| Dérivation          | `HKDF-SHA256(KEK, salt = 'ai-cred-v1', info = 'enc')` pour le chiffrement · `info = 'fp'` pour l'empreinte — une seule variable d'env pour deux usages, jamais la même valeur des deux côtés |
| IV                  | 12 octets, **aléatoire par écriture** (`randomBytes`) — jamais réutilisé, jamais dérivé du `user_id`      |
| AAD                 | `"${owner_user_id}:${enc_version}:${provider}"` — lie le chiffré à sa ligne : déplacer un chiffré vers une autre ligne le rend indéchiffrable (défense contre une écriture SQL malveillante) |
| Stockage            | `secret_enc bytea` = `iv (12) ‖ tag (16) ‖ ciphertext` — un seul champ, pas trois : impossible d'en désynchroniser un |
| Empreinte           | `key_fingerprint text` = `HMAC-SHA256(HKDF(…,'fp'), clé brute)` tronqué à 32 hex — permet de détecter une clé déjà connue (même clé recollée, clé partagée entre deux comptes) **sans** pouvoir remonter à la clé |
| Affichage           | `last4 text` (4 derniers caractères) — le seul fragment qui existe en clair                               |
| Rotation            | `enc_version smallint` + `AI_KEY_ENC_KEY_PREVIOUS` (optionnelle) : la lecture essaie la version courante puis la précédente, et **ré-écrit** en version courante au passage (rotation paresseuse, sans migration de données ni fenêtre de panne) |

**Ce que le coffre ne fait pas** : il ne déchiffre jamais pour afficher, jamais pour exporter,
jamais pour un support. Il n'existe **aucun chemin de code** dont la sortie contient le clair —
la fonction de lecture retourne un objet opaque consommé uniquement par l'adaptateur, dans le même
appel (D-3). Un test le vérifie par lecture du module, pas par confiance.

### 3.3 Modèle de données (migrations additives, grants explicites — DoD §7)

```sql
-- 1) LE COFFRE — une clé par adulte. Aucun rôle client n'a le moindre droit ici.
CREATE TABLE public.ai_credentials (
  owner_user_id   uuid PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,
  provider        text NOT NULL CHECK (provider IN ('anthropic','openai_compatible')),
  base_url        text,                                   -- NULL sauf openai_compatible ; validé R-6
  model_fast      text NOT NULL,
  model_rich      text NOT NULL,
  secret_enc      bytea NOT NULL,                         -- iv ‖ tag ‖ ciphertext (§3.2)
  enc_version     smallint NOT NULL DEFAULT 1,
  key_fingerprint text NOT NULL,
  last4           text NOT NULL CHECK (char_length(last4) = 4),
  status          text NOT NULL DEFAULT 'unverified'
                    CHECK (status IN ('unverified','active','invalid','revoked')),
  last_error_code text,                                   -- code stable, annexe C — jamais le corps fournisseur
  verified_at     timestamptz,
  last_used_at    timestamptz,
  daily_budget_usd   numeric(6,2) NOT NULL CHECK (daily_budget_usd   > 0 AND daily_budget_usd   <= 50),
  monthly_budget_usd numeric(7,2) NOT NULL CHECK (monthly_budget_usd > 0 AND monthly_budget_usd <= 500),
  consent_version text NOT NULL,
  consent_at      timestamptz NOT NULL,
  created_at      timestamptz NOT NULL DEFAULT now(),
  updated_at      timestamptz NOT NULL DEFAULT now(),
  CHECK ((provider = 'openai_compatible') OR base_url IS NULL)
);
ALTER TABLE public.ai_credentials ENABLE ROW LEVEL SECURITY;
REVOKE ALL ON public.ai_credentials FROM anon, authenticated;   -- ← l'invariant central
GRANT ALL ON public.ai_credentials TO service_role;
-- Aucune policy pour anon/authenticated : il n'y a rien à autoriser, le grant est retiré.
CREATE INDEX idx_ai_credentials_fingerprint ON public.ai_credentials (key_fingerprint);

-- 2) ACTIVATION PAR ÉLÈVE — c'est ici que le mode s'allume, pas dans le coffre.
CREATE TABLE public.ai_student_access (
  student_user_id uuid PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,
  owner_user_id   uuid NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
  enabled         boolean NOT NULL DEFAULT false,          -- R-3 : défaut éteint
  features        text[]  NOT NULL DEFAULT '{}',           -- sous-ensemble de AI_FEATURES (constante)
  daily_energy_max int    NOT NULL DEFAULT 10 CHECK (daily_energy_max BETWEEN 0 AND 30),  -- R-9
  updated_at      timestamptz NOT NULL DEFAULT now(),
  CHECK (owner_user_id <> student_user_id)
);
ALTER TABLE public.ai_student_access ENABLE ROW LEVEL SECURITY;
-- SELECT : l'élève lit SA ligne ; le parent lit celles de ses enfants liés ; admin tout.
CREATE POLICY ai_access_select_self ON public.ai_student_access FOR SELECT TO authenticated
  USING (student_user_id = (SELECT auth.uid())
      OR (owner_user_id  = (SELECT auth.uid()) AND public.is_parent_of_student((SELECT auth.uid()), student_user_id))
      OR public.is_admin());
-- Aucune policy d'écriture : tout passe par set_ai_student_access (SECURITY DEFINER, R-2/R-3).
GRANT SELECT ON public.ai_student_access TO authenticated;
GRANT ALL    ON public.ai_student_access TO service_role;

-- 3) COMPTABILITÉ — extension de ai_usage_events de é11 lot 0, repris ici (D-1).
CREATE TABLE public.ai_usage_events (
  id               bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  user_id          uuid REFERENCES auth.users(id) ON DELETE SET NULL,   -- l'élève servi
  payer            text NOT NULL CHECK (payer IN ('family','platform')), -- ← é29, R-7
  credential_owner uuid REFERENCES auth.users(id) ON DELETE SET NULL,    -- ← é29 (NULL si platform)
  provider         text NOT NULL,                                        -- ← é29, R-13
  feature          text NOT NULL CHECK (feature IN
    ('verify','explain','reformulate','chat','check','forge','forge_solve',
     'exercise_gen','digest_student','digest_parent')),
  model            text NOT NULL,
  input_tokens     int  NOT NULL DEFAULT 0,
  output_tokens    int  NOT NULL DEFAULT 0,
  cached_tokens    int  NOT NULL DEFAULT 0,
  cost_usd_micros  bigint NOT NULL DEFAULT 0,      -- estimation R-12, en micro-dollars (entier)
  status           text NOT NULL CHECK (status IN ('ok','rejected','error','degraded','discarded')),
  error_code       text,                            -- annexe C
  latency_ms       int,
  created_at       timestamptz NOT NULL DEFAULT now()
);
ALTER TABLE public.ai_usage_events ENABLE ROW LEVEL SECURITY;
-- L'ÉLÈVE N'A AUCUN ACCÈS ICI : la table porte des montants, et R-14 est absolue — un enfant
-- ne voit pas d'argent, y compris par PostgREST. Il lit son énergie dans les tables de é11.
CREATE POLICY ai_usage_select ON public.ai_usage_events FOR SELECT TO authenticated
  USING (public.is_admin() OR credential_owner = (SELECT auth.uid()));   -- le parent voit SA dépense
GRANT SELECT ON public.ai_usage_events TO authenticated;
GRANT ALL    ON public.ai_usage_events TO service_role;
CREATE INDEX idx_ai_usage_owner_day ON public.ai_usage_events (credential_owner, created_at DESC);
CREATE INDEX idx_ai_usage_user_day  ON public.ai_usage_events (user_id, created_at DESC);

-- 4) RÉSERVATION DE DÉPENSE — le compteur qui coupe AVANT l'appel (R-11).
CREATE TABLE public.ai_spend_ledger (
  owner_user_id uuid NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
  day           date NOT NULL,
  reserved_micros bigint NOT NULL DEFAULT 0 CHECK (reserved_micros >= 0),
  spent_micros    bigint NOT NULL DEFAULT 0 CHECK (spent_micros    >= 0),
  PRIMARY KEY (owner_user_id, day)
);
ALTER TABLE public.ai_spend_ledger ENABLE ROW LEVEL SECURITY;
CREATE POLICY ai_ledger_select ON public.ai_spend_ledger FOR SELECT TO authenticated
  USING (owner_user_id = (SELECT auth.uid()) OR public.is_admin());
GRANT SELECT ON public.ai_spend_ledger TO authenticated;
GRANT ALL    ON public.ai_spend_ledger TO service_role;

-- 5) LA FORGE — quiz éphémères, jamais au catalogue (R-16, R-17).
CREATE TABLE public.ai_forged_quizzes (
  id             uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  student_user_id uuid NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
  owner_user_id  uuid NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
  scope          text NOT NULL CHECK (scope IN ('chapter','competency','mistakes')),
  chapter_id     uuid REFERENCES public.chapters(id) ON DELETE CASCADE,
  competency_id  uuid,
  lang           text NOT NULL CHECK (lang IN ('fr','en','ar')),
  difficulty     int  NOT NULL CHECK (difficulty BETWEEN 1 AND 4),
  requested      int  NOT NULL CHECK (requested BETWEEN 5 AND 10),
  payload        jsonb NOT NULL,      -- items VALIDÉS, clés comprises — REVOKE total (voir plus bas)
  model          text NOT NULL,
  discarded      int  NOT NULL DEFAULT 0,
  expires_at     timestamptz NOT NULL DEFAULT (now() + interval '30 days'),
  created_at     timestamptz NOT NULL DEFAULT now(),
  CHECK ((scope = 'chapter') = (chapter_id IS NOT NULL))
);
ALTER TABLE public.ai_forged_quizzes ENABLE ROW LEVEL SECURITY;
REVOKE ALL ON public.ai_forged_quizzes FROM anon, authenticated;  -- payload = clés de réponse
GRANT ALL  ON public.ai_forged_quizzes TO service_role;
-- Lecture élève : UNIQUEMENT via serve_forged_quiz (SECURITY DEFINER) qui retire les clés,
-- exactement comme resolve_exercise_access le fait pour le catalogue (AGENTS.md § Data model).
CREATE INDEX idx_forged_student ON public.ai_forged_quizzes (student_user_id, created_at DESC);

-- 6) RETOUR QUALITÉ (👍/👎 et signalements sur du contenu IA — canal SÉPARÉ du catalogue, R-17)
CREATE TABLE public.ai_feedback (
  id          bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  user_id     uuid NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
  usage_id    bigint REFERENCES public.ai_usage_events(id) ON DELETE SET NULL,
  quiz_id     uuid   REFERENCES public.ai_forged_quizzes(id) ON DELETE CASCADE,
  verdict     text NOT NULL CHECK (verdict IN ('up','down')),
  reason      text CHECK (char_length(reason) <= 300),
  model       text NOT NULL,
  created_at  timestamptz NOT NULL DEFAULT now()
);
ALTER TABLE public.ai_feedback ENABLE ROW LEVEL SECURITY;
CREATE POLICY ai_feedback_select ON public.ai_feedback FOR SELECT TO authenticated
  USING (user_id = (SELECT auth.uid()) OR public.is_admin());
GRANT SELECT ON public.ai_feedback TO authenticated;
GRANT ALL    ON public.ai_feedback TO service_role;
```

**Purges** (cron existant) : `ai_forged_quizzes` à `expires_at` · `ai_usage_events` à 12 mois ·
`ai_spend_ledger` à 13 mois · `ai_feedback` à 12 mois. `ai_credentials` n'a **pas** de purge : une
clé disparaît quand son propriétaire la révoque ou quand son compte est supprimé (cascade).

**Attention DoD §7 & `db:check-chain`** : ces six tables sont nouvelles, donc **grants explicites**
obligatoires (piège documenté d'AGENTS.md : `CREATE TABLE` sans `GRANT` passe en cloud et casse la
suite pgTAP sur base vierge). Aucune n'a de FK vers du contenu absent du dépôt public :
`chapters(id)` existe dans les migrations publiques, `competency_id` n'est volontairement **pas**
une FK (é07 lot 1 est livré, mais le lien reste souple pour ne pas dépendre d'un référentiel dont
les lignes viennent du corpus privé).

### 3.4 Résolution d'accès (le point où tout se décide)

Une seule fonction SQL, appelée avant **chaque** appel IA, quel que soit le payeur :

```sql
CREATE OR REPLACE FUNCTION public.resolve_ai_access(p_student uuid, p_feature text)
RETURNS TABLE (allowed boolean, payer text, owner_user_id uuid, provider text,
               base_url text, model_fast text, model_rich text,
               energy_left int, reason text)
LANGUAGE plpgsql SECURITY DEFINER SET search_path = public AS $$
-- 1. le mode global est-il allumé (kill-switch data-driven + env côté Node) ?
-- 2. l'élève a-t-il une ligne ai_student_access enabled avec p_feature ∈ features ?
-- 3. le lien parent_student_links existe-t-il TOUJOURS (R-3) ?
-- 4. le crédential du parent est-il status='active' (R-2, R-6 re-vérifié) ?
-- 5. reste-t-il de l'énergie (é11 R-12, plafond ai_student_access.daily_energy_max) ?
-- 6. sinon : chemin plateforme si ANTHROPIC_API_KEY + budget A5 disponibles ;
-- 7. sinon : allowed = false, reason = code stable → l'UI dégrade en silence (é11 R-15).
$$;
```

Elle **ne rend jamais le secret** — seulement l'identité du coffre à ouvrir. Le chargement du
chiffré se fait ensuite en Node, avec le client `service_role`
(`src/shared/integrations/supabase/client.server.ts`, déjà en place), puis le déchiffrement en
mémoire. C'est la couture qui garantit qu'un bug d'un seul côté ne suffit pas.

Autres contrats (tous `SECURITY DEFINER`, tous appelés depuis des server fns validées zod) :

| RPC                                                     | Rôle                                                                                      |
| ------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `set_ai_credential_meta(provider, base_url, models, budgets, consent_version, last4, fingerprint, enc_version)` | Écrit **tout sauf le secret** ; le `bytea` chiffré est posé par le même appel Node en `service_role`. Vérifie R-2 (rôle) et R-6 (hôte) |
| `revoke_ai_credential()`                                | Supprime la ligne, éteint toutes les activations liées, garde l'historique agrégé (US-8)  |
| `set_ai_student_access(student, enabled, features, energy_max)` | R-2 + `is_parent_of_student` ; refuse `energy_max > TUTOR_HARD_DAILY_CAP` (R-9)   |
| `reserve_ai_spend(owner, micros)` / `settle_ai_spend(owner, reserved, actual)` | Réservation atomique puis solde réel (R-11) — même motif que l'énergie de é11 |
| `log_ai_usage(...)`                                     | Écrit `ai_usage_events` (R-7, R-13)                                                       |
| `get_ai_console(owner)`                                 | Ce que la console parent affiche : statut, `last4`, modèles, dépense jour/mois, par enfant et par surface, taux de rebut, ratio 👍/👎 — **jamais** le secret |
| `serve_forged_quiz(quiz_id)`                            | Rend les items **sans clé de réponse** (motif `resolve_exercise_access`)                  |
| `grade_forged_quiz(quiz_id, answers)`                   | Corrige côté serveur, ne verse **aucune** récompense (R-16)                               |

### 3.5 L'adaptateur multi-fournisseur — `src/shared/integrations/ai/`

Le contrat de é11 §3.5 (`TutorLLM`) est **généralisé et renommé** `AiProvider` — même intention
(le nom d'un fournisseur n'apparaît jamais dans le code de feature), périmètre élargi :

```ts
type AiRequest = {
  tier: "fast" | "rich";
  system: string;
  blocks: AiBlock[];          // ordre stable → volatile (prompt caching, é11 §3.4)
  maxTokens: number;          // constante serveur, R-10
  feature: AiFeature;
  responseSchema?: ZodType;   // sortie structurée (Forge, §3.6)
};
type AiCredential = { provider: AiProviderId; baseUrl?: string; secret: Opaque<string>; models: { fast: string; rich: string } };
interface AiProvider {
  generate(req: AiRequest, cred: AiCredential): Promise<AiResult>;
  stream(req: AiRequest, cred: AiCredential): AsyncIterable<AiChunk>;
  readonly capabilities: { streaming: boolean; structuredOutput: boolean; promptCache: boolean };
}
```

Implémentations v1 — **deux**, pas cinq (D-6) :

| Id                  | Transport                                                  | Couvre                                                                                     |
| ------------------- | ---------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `anthropic`         | SDK `@anthropic-ai/sdk` (server-only), API Messages         | Anthropic. Seul chemin qui exploite le prompt caching et les paliers de é11                 |
| `openai_compatible` | `fetch` sur `POST {base_url}/chat/completions`              | OpenAI, OpenRouter, Groq, DeepSeek, Mistral, et l'endpoint compatible de Google — **si et seulement si** l'hôte est dans `AI_ALLOWED_HOSTS` (R-6) |
| `fake`              | déterministe, par feature                                   | CI, e2e, dev sans clé (`AI_FAKE_PROVIDER=1`) — coût zéro, sortie stable                     |

`capabilities` n'est pas décoratif : un fournisseur sans `structuredOutput` fait tourner la Forge
en mode « JSON demandé dans le prompt + parsing strict », avec un taux de rebut supérieur — c'est
un fait à afficher (R-19), pas à masquer. Un fournisseur sans `streaming` fait retomber le chat de
é11 en réponse non streamée (dégradation prévue, pas panne).

**Ce que l'adaptateur garantit, quel que soit le fournisseur** : timeout 30 s ; 2 retries sur
429/5xx uniquement ; **aucun retry** sur 401/403 (une clé invalide le reste — sinon on brûle le
quota du parent) ; erreurs re-typées (R-5, annexe C) ; usage rapporté (tokens in/out/cache) ;
absence du bundle client prouvée par `build:check`.

### 3.6 La Forge — chaîne de validation (là où la qualité se gagne)

```
scope (déterministe)                        ← SQL : chapitre / compétence / tags actifs é04
   ▼
contexte fermé   cours du chapitre (≤ 1 500 tk) + 3 questions du catalogue en RÉFÉRENCE DE STYLE
   ▼             + bande d'âge + langue de la matière + difficulté cible
génération       1 appel `rich`, sortie structurée, N+2 candidats
   ▼
filtres déterministes (0 token, aucune indulgence) :
   • schéma zod miroir du pipeline contenu (4 options, clé unique, longueurs, difficulté)
   • notation : chiffres 0-9, pas de LaTeX, équations LTR, unités SI
   • pas de doublon : hash normalisé de l'énoncé ≠ catalogue du chapitre ET ≠ les autres candidats
   • vocabulaire de la bande d'âge (liste d'interdits) · zéro URL · zéro « aucune des réponses »
   ▼
double résolution  1 appel `rich` par candidat survivant : « résous », SANS voir la clé déclarée
   ▼               désaccord ⇒ rebut (compté, affiché) · item numérique ré-exécutable ⇒ vérif
   ▼               arithmétique côté serveur, préférée à l'appel (moins cher, plus sûr)
≥ N validés ? ── oui ─► ai_forged_quizzes (payload avec clés, REVOKE total) ─► jouable
              └─ non ─► échec honnête, énergie remboursée, dépense réelle malgré tout journalisée
```

Le double-solve **double le coût** de la Forge, et c'est assumé : sans lui, un modèle bon marché
livre des quiz dont la clé est fausse une fois sur dix, à un enfant qui n'a aucun moyen de le
savoir. C'est le seul endroit de l'étude où l'on dépense davantage pour protéger la pédagogie —
et c'est le prix d'entrée du BYOK (Q-7 propose de le rendre non désactivable ; la recommandation
est **oui, jamais désactivable**).

### 3.7 Comptabilité, budgets & coupure

- **Estimation avant appel** : `tokens_in_estimés × prix_in + maxTokens × prix_out`, avec
  `AI_MODEL_PRICES` — table **datée** en constante serveur (`src/shared/constants/ai.ts`),
  identique dans son esprit à `MODEL_PRICES` de é11. Un modèle absent de la table est facturé à
  l'estimation **la plus haute** de son fournisseur (jamais 0 : un prix inconnu ne doit pas ouvrir
  une vanne).
- **Réservation** : `reserve_ai_spend` incrémente `reserved_micros` **avant** l'appel ; le solde
  réel remplace la réservation après (`settle_ai_spend`). Un appel qui meurt en vol libère sa
  réservation (timeout de nettoyage 5 min).
- **Coupure** : `reserved + spent + estimate > plafond` ⇒ appel non émis. Le plafond **journalier**
  protège de l'emballement, le **mensuel** protège la facture. Les deux sont vérifiés.
- **Alertes** : 50 % / 80 % / 100 % du plafond mensuel, une notification par seuil et par mois
  (pas par appel), sur le canal notifications existant + e-mail parent.
- **Ce que la plateforme ne fait pas** : ni provisionnement, ni crédit, ni avance, ni facturation.
  L'app n'a **aucune** vue sur le solde réel du compte fournisseur (aucun fournisseur ne l'expose
  de façon fiable via l'API) — donc « crédit épuisé » est un état constaté *a posteriori*, sur une
  erreur (annexe C), jamais anticipé. Le dire dans la console évite la question de support n° 1.

### 3.8 Sécurité, vie privée & minorité

| Invariant                                            | Mécanisme                                                                                              |
| ---------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| La clé ne fuit pas par la base                       | `REVOKE ALL … FROM anon, authenticated` + chiffrement enveloppe (KEK hors base) + AAD lié à la ligne     |
| La clé ne fuit pas par le code                       | Aucun chemin retournant le clair (D-3) ; `logger` redacteur ; erreurs fournisseur re-typées (R-5)        |
| La clé ne fuit pas par le bundle                     | Adaptateur et coffre en `.server.ts` ; `build:check` prouve l'absence du SDK côté client                 |
| La clé ne sert pas à autre chose                     | R-8 vérifié à la résolution ; `payer`/`credential_owner` sur chaque événement                            |
| Aucune clé de réponse côté client                    | `ai_forged_quizzes` REVOKE total ; `serve_forged_quiz` retire les clés (motif `resolve_exercise_access`)  |
| Pas de PII vers le fournisseur                       | Pack élève pseudonymisé (é11 R-14) : bande d'âge, classe, maîtrise, tags — **jamais** nom, e-mail, id     |
| Le parent sait ce qui part                           | Consentement versionné (R-20), texte listant explicitement l'envoyé et le non-envoyé                      |
| Le fournisseur est un sous-traitant **choisi par le parent** | Le texte le dit : la politique de rétention et d'entraînement du fournisseur **échappe à la plateforme**, et certains paliers gratuits entraînent sur les données envoyées — recommandation explicite d'un palier payant |
| Minorité                                             | La clé appartient à un adulte (R-2) ; l'usage est supervisé ; aucune surface IA n'existe hors activation parentale |
| Injection de prompt                                  | é11 R-5 (entrée élève = donnée, bornée, jamais concaténée aux instructions) + rendu sanitizé (`markdown.ts`, `docs/xss-rendering-policy.md`) |
| SSRF                                                 | R-6 : liste blanche d'hôtes, https, pas d'IP, pas de redirection                                          |
| Conservation                                         | Quiz forgés 30 j · comptabilité 12 mois · retours 12 mois · clé : jusqu'à révocation                      |

**À faire dans le lot 2, pas « plus tard »** : la page `/confidentialite` (route publique
existante) gagne une section « Mode IA » ; le registre de traitement est mis à jour (le même
chantier INPDP que é11 mentionne) ; et la page dit ce que l'app **ne peut pas** garantir — ce que
le fournisseur fait des données après réception.

### 3.9 Observabilité & console

- **Logs structurés** (`@/shared/lib/logger`, jamais `console`) : `ai.request` `{feature, payer,
  provider, model, tier, latencyMs, tokensIn, tokensOut, costUsdMicros, status}` ·
  `ai.credential` `{action: 'set'|'verify'|'revoke'|'rotate', result, errorCode}` ·
  `ai.budget` `{owner, threshold, action:'warn'|'cut'}` · `ai.forge` `{requested, kept, discarded}`.
  **Jamais** : la clé, un fragment de clé au-delà de `last4`, le texte de l'élève, la sortie du
  modèle (`docs/logging-standard.md`).
- **Réglages › Mode IA (parent)** : statut de la clé, dépense, activations, qualité par modèle, journal
  des 20 derniers appels (surface, date, statut, coût estimé — jamais le contenu).
- **Console admin** (motif existant `_authenticated` + `useMyRole` + `is_admin()`) : agrégats
  plateforme, répartition des fournisseurs et modèles, taux de rebut et de 👎 **par modèle**
  (la donnée qui dira si un modèle bon marché est acceptable), état des kill-switches, familles
  en coupure. Aucun transcript, aucune clé, aucun montant nominatif au-delà de l'agrégat.

### 3.10 Intégrations & environnement (MAJ `docs/environment-variables.md` au lot 1)

| Variable                    | Portée                | Rôle                                                                                       |
| --------------------------- | --------------------- | -------------------------------------------------------------------------------------------- |
| `AI_KEY_ENC_KEY`            | serveur uniquement    | **secret** — KEK 32 octets base64 du coffre. Absente ⇒ mode famille éteint (mode plateforme intact) |
| `AI_KEY_ENC_KEY_PREVIOUS`   | serveur uniquement    | **secret** — KEK précédente pendant une rotation (optionnelle, retirée après)                |
| `AI_MODE_ENABLED`           | serveur               | Kill-switch global de la porte IA (défaut `true`)                                            |
| `AI_BYOK_ENABLED`           | serveur               | Kill-switch du seul chemin famille (défaut `true` si `AI_KEY_ENC_KEY` est là)                |
| `AI_FAKE_PROVIDER`          | serveur               | `1` ⇒ fournisseur factice (CI, e2e, dev)                                                     |
| `ANTHROPIC_API_KEY`         | serveur uniquement    | **secret** — clé **plateforme** (chemin é11, budget A5). Absente ⇒ seul le BYOK fonctionne  |
| `AI_PLATFORM_DAILY_BUDGET_USD` | serveur            | Plafond plateforme/jour (5 — A5). Ne s'applique **jamais** au payeur `family`                |

Tout le reste est constante de code (`src/shared/constants/ai.ts`) : `AI_ALLOWED_HOSTS`,
`AI_FEATURES`, `AI_MODEL_PRICES` (datée), `AI_CURATED_MODELS` (liste proposée par fournisseur),
`AI_MAX_TOKENS` par surface, `AI_FORGE_LIMITS`, `AI_DEFAULT_BUDGETS`, `AI_CONSENT_VERSION`.
Aucun id de modèle en dur ailleurs (é11 D-2 étendu).

### 3.11 Décisions d'architecture (ADR)

- **D-1 — Cette étude livre le socle ; le lot 0 de é11 est rayé.** Une seule porte (é26 D-8) : le
  lot 1 ci-dessous *est* le lot 0 de é11, plus le payeur. Rejeté : livrer é11 lot 0 puis le
  refactorer pour le BYOK (deux migrations sur `ai_usage_events`, deux revues, un adaptateur à
  réécrire — pour un socle qui n'existe pas encore). **Arbitrage humain : Q-1.**
- **D-2 — Le BYOK n'est pas exclusif.** Les deux payeurs coexistent derrière la même porte. Rejeté :
  BYOK seul (réserverait l'IA aux familles bancarisées à l'international — RISK-3) ; plateforme
  seule (c'est le statu quo, et il attend octobre).
- **D-3 — Le secret n'a aucun chemin de sortie.** Pas d'endpoint « afficher », pas d'export, pas de
  déchiffrement pour le support. Rejeté : un déchiffrement admin « pour dépanner » — c'est la
  porte par laquelle les fuites arrivent, et le dépannage se fait avec `last4` + code d'erreur.
- **D-4 — La clé est stockée, chiffrée, côté serveur.** Rejetés : **(a) clé dans le navigateur,
  appels directs navigateur → fournisseur** — impossible ici, car le contexte pédagogique contient
  la clé de réponse et l'explication canonique, qui **ne descendent jamais au client** (invariant
  AGENTS.md) ; s'y ajoutent le CORS des fournisseurs (Anthropic exige un en-tête explicite
  d'autorisation navigateur), l'exposition à toute XSS, et l'impossibilité de compter ou de
  plafonner quoi que ce soit. **(b) clé de session non persistée** — élégante côté risque, mais
  elle exige que le parent soit présent à chaque session de l'enfant : le mode ne s'allumerait
  jamais quand il sert. Reportée en v2 pour l'apprenant adulte (§2.6, Q-8).
- **D-5 — Chiffrement en Node, pas en base.** `node:crypto` + KEK dans l'environnement. Rejetés :
  `pgcrypto` (la clé de chiffrement finirait dans une fonction SQL, donc dans le dump) ;
  `pgsodium`/Vault Supabase (surface d'exploitation supplémentaire, et une dépendance de plus à
  une capacité gérée) ; un KMS tiers (aucun précédent dans le projet, coût et latence).
- **D-6 — Deux implémentations, pas cinq.** `anthropic` + `openai_compatible` couvrent l'essentiel
  du marché avec un seul protocole à maintenir en plus. Rejetés : une passerelle multi-fournisseur
  tierce (un intermédiaire de plus qui verrait les clés) ; un SDK par fournisseur (autant de
  chemins de mise à jour, pour un gain marginal).
- **D-7 — Le payeur est une colonne, pas un mode de déploiement.** Toutes les surfaces, tous les
  quotas, toute la comptabilité sont écrits une fois et lisent `payer`. Rejeté : deux chemins de
  code parallèles (la divergence serait garantie au troisième lot).
- **D-8 — La coupure est dans le chemin de requête.** Comme é11 R-13 : pas de job d'alerte séparé,
  la vérification est atomique avec la réservation. Rejeté : un cron de surveillance (il découvre
  le dépassement une fois qu'il est payé).
- **D-9 — Le cache d'explications est cloisonné par payeur.** Le cache partagé de é11 (D-6) reste
  la règle pour le payeur plateforme ; le payeur famille a son propre espace, privé. Motifs : la
  qualité (un modèle libre ne doit pas alimenter les autres enfants), l'équité (une famille ne
  finance pas la plateforme sans le savoir), la vie privée. Conséquence assumée : **le taux de
  réutilisation d'une famille est faible, donc son coût unitaire est plus élevé que celui de é11**
  (annexe A). Alternative offerte en Q-3 : un don explicite, opt-in, jamais par défaut.
- **D-10 — Un seul crédential par adulte en v1.** Rejeté : une clé par matière ou par enfant
  (complexité de résolution sans besoin démontré ; le multi-clé viendra si le besoin apparaît).
- **D-11 — Le choix du modèle appartient au parent, la mesure appartient à l'app.** L'app conseille
  (R-19), n'impose ni ne bascule. Rejeté : forcer un modèle minimal (c'est sa clé, son argent) ;
  taire la mesure (ce serait laisser un enfant réviser sur des quiz faux).
- **D-12 — Aucun flux financier ne passe par la plateforme.** Rejeté : revendre des crédits ou
  proposer un « pack tokens » — cela ferait de nous un intermédiaire de paiement, ouvrirait la
  question fiscale, et contredirait la phase gratuite. La clé du parent, chez son fournisseur.
- **D-13 — La Forge n'écrit jamais dans la télémétrie d'apprentissage.** Reprise de é11 D-10,
  élargie à `attempts` et `spaced_repetition_schedule`. Rejeté : compter les quiz forgés dans la
  progression (du contenu non revu piloterait l'adaptativité et le SM-2).
- **D-14 — Pas de framework de feature flags** (é11 D-15) : kill-switch par env + données.
- **D-16 — La clé se saisit dans les Réglages, pas sur une page à elle.** Une clé d'API est un
  réglage de compte, au même titre que la langue, le thème ou les notifications : elle appartient
  à la rubrique où l'on va quand on cherche « où est-ce que je change ça ? ». Une route dédiée
  `/ia` la rendrait introuvable pour qui ne sait pas déjà qu'elle existe, et créerait une
  quatrième adresse de préférences dans une app qui en a déjà trois éparpillées (en-tête,
  en-tête, feature notifications). Conséquence : le lot 2 **crée la rubrique** — elle n'existe
  pas — et le Mode IA en est la première section, pas l'unique raison d'être. Rejetés : une page
  `/ia` autonome (invisible, et une adresse de plus) ; un onglet du rapport parent (le rapport
  est une lecture de l'activité de l'enfant, pas un lieu de configuration, et l'admin en serait
  exclu) ; une modale depuis l'en-tête (un formulaire à consentement, plafonds et tableau de
  dépense ne tient pas dans une pop-over, et rien ne s'y partage par lien).
- **D-15 — Le mode éteint est l'état par défaut et un état testé.** Rejeté : un « mode découverte »
  offrant quelques appels sur la clé plateforme à qui n'en a pas — c'est une promotion déguisée,
  un coût non borné, et une déception programmée à la fin de l'essai.

---

## 4. Plan d'exécution en lots

Chaque lot = **une PR mergeable, gate verte, utile seul** (`FableEtudes/29-…#lot-N`).
Recommandation : livrer 1 → 2 → 3 (à ce stade le mode existe et é11 peut démarrer), **mesurer
2 semaines sur une famille pilote** (celle de l'humain — la seule dont la clé est disponible),
puis 4 → 5.

| lot | contenu (résumé)                                                                       | fichiers/objets créés (principaux)                                                                                                                                                                                                                                                                | tests exigés                                                                                                                                                                    | dépend de                    |
| --- | -------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- |
| 1   | **La porte IA** : adaptateur multi-fournisseur, comptabilité, kill-switches (remplace é11 lot 0) | dép. `@anthropic-ai/sdk` ; `src/shared/integrations/ai/{index,anthropic.server,openai-compatible.server,fake.server}.ts` ; `src/shared/constants/ai.ts` ; migration `ai_usage_events` + `log_ai_usage` + purge ; MAJ `docs/environment-variables.md`                                            | unit adaptateur (Fake + `fetch` mocké : usage→coût, retries 429/5xx, **pas de retry sur 401**, timeout, re-typage d'erreur) ; unit liste blanche R-6 ; pgTAP grants/RLS ; `build:check` (SDK hors bundle client) | —                            |
| 2   | **Le coffre & la console** : chiffrement, saisie, vérification, révocation, consentement | `src/features/ai/` (barrel, `ai-credentials.server.ts`, `crypto.server.ts`) ; migration `ai_credentials` + RPCs meta/revoke ; **route `/settings` (la rubrique Réglages, créée ici) + sa section « Mode IA »** + son entrée de nav dans les DEUX shells (élève et parent) ; i18n `ai.*` + `settings.*` FR/EN/AR ; section « Mode IA » de `/confidentialite`                                                                                       | unit crypto (round-trip, AAD refusé si déplacé, rotation KEK, IV unique) ; **pgTAP : `has_table_privilege('authenticated','ai_credentials','SELECT') = false`** ; unit R-2 (un `student` est refusé côté RPC) ; captures FR + AR | 1                            |
| 3   | **Activation, énergie & budgets** : le mode s'allume, et il ne peut pas déraper          | migration `ai_student_access` + `ai_spend_ledger` + `resolve_ai_access` + `reserve/settle_ai_spend` + `set_ai_student_access` ; UI activation par enfant ; alertes 50/80/100 % ; badge « mode IA » élève                                                                                          | **pgTAP : matrice de `resolve_ai_access`** (lien rompu, clé révoquée, feature non activée, énergie épuisée, plafond atteint, chemin plateforme) ; pgTAP réservation atomique (double dépense concurrente) ; unit dégradé silencieux | 2                            |
| 4   | **La Forge** : le générateur de quiz personnalisé                                       | migration `ai_forged_quizzes` + `serve_forged_quiz` + `grade_forged_quiz` ; chaîne §3.6 (schéma zod, filtres, double-solve) ; écran Forge + lecture dans le lecteur existant ; étiquetage + 👍/👎                                                                                                | unit chaîne complète avec Fake (candidat invalide rejeté, doublon rejeté, désaccord de double-solve ⇒ rebut) ; **pgTAP : `serve_forged_quiz` ne rend jamais la clé** ; pgTAP zéro récompense (R-16) ; e2e forge→jouer avec `AI_FAKE_PROVIDER=1` | 3                            |
| 5   | **Qualité & pilotage** : console de dépense et de qualité, conseil de modèle, admin      | `get_ai_console` ; tableaux dépense/qualité par enfant, surface et modèle ; bandeau R-19 ; `/admin/ai` (agrégats, kill-switches, familles en coupure) ; purges cron ; `ai_feedback`                                                                                                              | unit agrégats (par surface/modèle) ; pgTAP RLS `ai_feedback` + purges ; unit R-19 (seuil de rebut) ; captures FR + AR                                                              | 4 (utile dès 3, complet à 4) |

- [ ] Lot 1 — la porte IA (adaptateur multi-fournisseur, comptabilité, kill-switches)
- [ ] Lot 2 — le coffre & la console parent (chiffrement, vérification, consentement, révocation)
- [ ] Lot 3 — activation par élève, énergie et budgets famille (coupure atomique)
- [ ] Lot 4 — la Forge (générateur de quiz personnalisé, double-solve, éphémère)
- [ ] Lot 5 — console de dépense et de qualité, conseil de modèle, admin, purges

**Stop-points (non négociables pour l'exécuteur)** :

- **R-1, R-4, R-5, R-8, R-14, R-16, R-17 ne s'assouplissent dans aucun lot.** Un doute sur l'un
  d'eux ⇒ STOP + escalade, jamais un contournement local.
- **Aucun endpoint, aucune RPC, aucune réponse ne rend la clé** — même en admin, même en debug,
  même derrière un flag. Si un besoin de support semble l'exiger, c'est le besoin qu'il faut
  redéfinir (D-3).
- **Le lot 4 ne démarre pas avant que le lot 3 coupe réellement** : une Forge branchée sur un
  budget non appliqué est le scénario de facture surprise (RISK-2).
- **Le double-solve n'est pas « optimisable »** en un seul appel qui s'auto-vérifie : c'est le
  même modèle qui se relit, la garantie tombe (Q-7).
- **Aucun id de modèle ni prix hors `src/shared/constants/ai.ts`** ; la table de prix porte sa date.
- **Aucune écriture** dans `question_attempts`, `attempts`, `spaced_repetition_schedule`, ni
  aucune récompense, depuis un chemin IA (R-16, D-13).
- **Si é11 lot 0 est livré entre-temps** (Q-1 arbitrée dans l'autre sens), le lot 1 d'ici est
  remplacé par un lot d'**extension** de l'existant (colonnes `payer`/`provider`/`credential_owner`
  + généralisation de l'adaptateur) — jamais par un second socle.

## 5. Stratégie de test

- **Vitest (co-localisés `src/features/ai/__tests__/`, `src/shared/integrations/ai/__tests__/`)** :
  chiffrement (round-trip, AAD, rotation, IV distinct à chaque écriture) ; adaptateur par
  fournisseur avec `fetch` mocké (usage→coût, codes d'erreur, absence de retry sur 401/403,
  timeout) ; liste blanche R-6 (hôte hors liste, http, IP littérale, plage privée, redirection) ;
  chaîne de la Forge avec `FakeAiProvider` (candidat hors schéma, doublon, désaccord de
  double-solve) ; dégradation (aucune surface IA rendue mode éteint — R-1).
- **pgTAP (obligatoire, toute logique SQL — DoD)** : **absence de privilège client sur
  `ai_credentials` et `ai_forged_quizzes`** (le test qui garde l'invariant central) ; matrice
  `resolve_ai_access` ; `set_ai_credential_meta` refusée à un `student` (R-2) ; réservation
  concurrente (pas de double dépense) ; `serve_forged_quiz` sans clé de réponse ;
  `grade_forged_quiz` sans récompense ; RLS de chaque table ; purges.
- **Playwright (projet TEST dédié, `AI_FAKE_PROVIDER=1`)** : parcours parent complet (attacher →
  vérifier → activer → révoquer) ; parcours élève (Forge → jouer → 👎) ; **parcours mode éteint**
  (aucune surface IA visible, et la section « Mode IA » des Réglages absente) ; **accès à
  `/settings` depuis le shell PARENT** (le shell Suivi-only : c'est le test qui garde le point 2
  du §2.1) ; RTL sur `/settings`.
- **`smoke:shell`** : la coquille publique reste crash-free (le bundle prod ne doit rien importer
  de la chaîne IA).
- **Non-régression de l'existant** — c'est le test qui compte le plus : la suite complète tourne
  **sans aucune variable IA définie**, et tout écran touché rend exactement ce qu'il rendait
  avant. Une régression visible sans clé serait la preuve que R-1 a été violée.
- **Ce qu'on ne teste pas en CI** : aucun appel réel vers un fournisseur, jamais, sous aucun
  prétexte (ni clé de test en secret CI, ni « un petit appel de fumée »). Le seul appel réel du
  système est celui de la vérification (US-2), déclenché par un humain avec sa propre clé.

## 6. Risques & mitigations

| #       | Risque                                                                                                      | P × I         | Mitigation **décidée**                                                                                                                                                                          |
| ------- | ----------------------------------------------------------------------------------------------------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| RISK-1  | **Fuite d'une clé** (dump de base, log, réponse d'API, bundle)                                              | faible × **critique** | Chiffrement enveloppe, KEK hors base (§3.2) · `REVOKE ALL` · aucun chemin de sortie (D-3) · logger redacteur · erreurs re-typées · pgTAP de privilège · revue de bundle. Procédure d'incident : révocation côté fournisseur par le parent (nous ne pouvons pas la faire), purge de la ligne, rotation de la KEK |
| RISK-2  | **Facture surprise** pour une famille                                                                       | moyenne × **élevé** | Double plafond vérifié **avant** chaque appel, atomiquement (R-11) · alertes 50/80/100 % · estimation affichée avant la Forge · défauts prudents (Q-6) · KPI « dépassements non stoppés : 0 »   |
| RISK-3  | **Le mode reste une porte pour privilégiés** — une clé suppose un compte fournisseur et une carte internationale, rare en Tunisie | **élevée** × moyen | Assumé et nommé : le BYOK est une voie *supplémentaire*, jamais l'unique (D-2, Q-5). Le chemin plateforme reste, avec le budget A5. Aucune fonctionnalité pédagogique du produit ne migre derrière la porte IA (R-1) |
| RISK-4  | **Un modèle faible dégrade la pédagogie** (quiz faux, explication erronée)                                  | moyenne × élevé | Filtres déterministes + double-solve (§3.6) · cache cloisonné (D-9 : le voisin n'hérite pas) · mesure du rebut et du 👎 **par modèle** · conseil explicite (R-19) · étiquetage systématique du contenu IA |
| RISK-5  | **CGU des fournisseurs / usage par un mineur**                                                              | moyenne × moyen | La clé appartient à un adulte (R-2), l'usage est activé et supervisé par lui (R-3), le consentement le dit (R-20). Aucune surface ne s'adresse à un mineur sans ce chemin                        |
| RISK-6  | **Injection de prompt** via le champ libre ou via du contenu forgé rendu                                    | moyenne × moyen | é11 R-5 (entrée = donnée bornée, hiérarchie système) · validateur de sortie · sanitizer de rendu (`markdown.ts`) · zéro URL sortante dans une sortie de modèle                                   |
| RISK-7  | **SSRF via `base_url`**                                                                                     | faible × élevé | Liste blanche fermée en constante serveur, https, pas d'IP littérale, pas de plage privée, pas de redirection suivie (R-6), re-vérifiée à chaque appel et pas seulement à la saisie              |
| RISK-8  | **Support** : « ma clé ne marche pas »                                                                       | **élevée** × faible | Vérification à l'enregistrement (US-2) · codes d'erreur stables et traduits (annexe C) · console qui affiche le dernier état et sa date · périmètre annoncé : nous ne dépannons pas le compte fournisseur |
| RISK-9  | **Deux socles IA finissent par exister** (é11 lot 0 livré ailleurs, é29 lot 1 ici)                          | moyenne × élevé | D-1 + Q-1 arbitrée **avant** le premier lot · stop-point explicite si l'ordre s'inverse · la ROADMAP ligne 17 pointe cette étude une fois Q-1 rendue                                             |
| RISK-10 | **Perte de la KEK** (variable d'environnement effacée ou remplacée sans rotation)                            | faible × moyen | Aucune donnée d'apprentissage n'est perdue : seules les clés deviennent illisibles ⇒ statut `invalid`, invitation à re-saisir. `AI_KEY_ENC_KEY_PREVIOUS` couvre la rotation. Documenté dans le runbook de sauvegarde |

## 7. Questions ouvertes (pour l'humain)

Une étude passe `validée` quand cette section est arbitrée. Chaque question porte une
**recommandation** — l'exécuteur ne tranche aucune d'entre elles.

| #   | Question                                                                                                                              | Recommandation                                                                                                                                                       |
| --- | --------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Q-1 | **Le lot 1 de é29 remplace-t-il le lot 0 de é11 ?** (D-1)                                                                              | **Oui.** Le socle n'existe pas encore ; le livrer deux fois, ou le livrer puis le refactorer, coûte plus que de l'écrire une fois avec le payeur dedans                    |
| Q-2 | **Qui peut attacher une clé ?** Parent/admin seuls, ou aussi un élève majeur (bac, parcours libre, adulte de `muscle-cerveau`) ?      | **Parent/admin en v1.** L'élève majeur est réel mais minoritaire, et sa prise en charge demande une déclaration d'âge fiable que le produit n'a pas. À rouvrir en v2 (Q-8) |
| Q-3 | **Le cache d'explications d'une famille reste-t-il privé ?** (D-9)                                                                     | **Privé par défaut.** Un don explicite et opt-in (« partager mes explications avec les autres élèves ») est acceptable en lot 5, jamais activé par défaut, jamais rétroactif |
| Q-4 | **Quels fournisseurs en v1 ?**                                                                                                        | **Anthropic + compatibles OpenAI par liste blanche** (D-6). La liste blanche exacte est un réglage de constante, pas une décision d'architecture — mais son contenu initial est une décision produit |
| Q-5 | **Le chemin plateforme reste-t-il allumé en parallèle ?** (budget 5 $/j de A5)                                                        | **Oui.** Le couper ferait du BYOK l'unique accès à l'IA, donc un produit à deux vitesses (RISK-3). Le garder coûte au plus ce que A5 a déjà arbitré                       |
| Q-6 | **Plafonds famille par défaut ?**                                                                                                     | **0,50 $/jour et 5 $/mois** (annexe A : couvre un usage régulier avec marge, et reste sous le rechargement minimal habituel d'un compte fournisseur). Réglables par le parent, dans les bornes du schéma |
| Q-7 | **Le double-solve de la Forge est-il désactivable** (moitié moins cher) ?                                                             | **Non, jamais.** C'est la seule barrière entre un modèle bon marché et un enfant qui révise sur une clé de réponse fausse. Le coût est le prix d'entrée du BYOK              |
| Q-8 | **Mode « clé de session » non persistée** pour l'apprenant adulte — v2 ?                                                              | **v2**, en même temps que Q-2. Le spécifier maintenant ajouterait un second chemin de crédential pour un public que la v1 n'ouvre pas                                       |
| Q-9 | **Ordre d'exécution** : é29 lots 1-3 **avant** é11 lots 1-2, ou en parallèle ?                                                        | **Avant, strictement.** é11 lot 1 sans la porte n'a pas de clé à utiliser ; la porte sans é11 a déjà la Forge comme surface utile. Conséquence roadmap : la ligne 17 change de contenu, pas de rang |

## 8. Journal d'exécution

| date | lot | PR | écarts acceptés / dettes notées |
| ---- | --- | -- | ------------------------------- |
| —    | —   | —  | _(à remplir par l'exécuteur, à chaque lot)_ |

---

## Annexe A — Ce que ça coûte **à la famille** (et pourquoi ce n'est pas le chiffrage de é11)

Les coûts unitaires sont ceux de **é11 annexe A** (prix constatés au 2026-07-17, **à re-vérifier
via le skill `claude-api` à l'implémentation** — la table `AI_MODEL_PRICES` porte sa date). Ce qui
change ici n'est pas le prix : c'est **le dénominateur**.

**Deux effets, en sens contraires** :

1. **Le cache privé renchérit** (D-9). é11 compte sur un taux de réutilisation de 60 % obtenu en
   mutualisant les explications entre tous les élèves. Une famille seule ne réutilise que ses
   propres répétitions : **10 à 20 %**. Le poste « explications » d'une famille coûte donc environ
   **le double** de la ligne équivalente de é11.
2. **La Forge est le poste dominant**, et il n'existe pas chez é11. Un quiz de 8 questions =
   1 appel de génération groupée + 8 à 10 double-solves.

| Action                                    | Modèle « capable » (ordre Sonnet 5) | Modèle « économique » (ordre Haiku 4.5) |
| ----------------------------------------- | ----------------------------------- | --------------------------------------- |
| Explication fraîche                       | ≈ 0,014 $                           | ≈ 0,004 $                               |
| Message de chat (préfixe caché)           | ≈ 0,005 $                           | ≈ 0,002 $                               |
| **Quiz forgé de 8 questions (double-solve compris)** | **≈ 0,10 – 0,20 $**        | **≈ 0,03 – 0,06 $**                     |
| Vérification de clé (US-2)                | < 0,001 $                           | < 0,001 $                               |

| Profil d'élève (1 enfant activé)                               | Coût ≈ / mois, modèle capable | Coût ≈ / mois, modèle économique |
| -------------------------------------------------------------- | ----------------------------- | -------------------------------- |
| **Léger** — 2 explications + 5 messages / semaine, 1 quiz/mois  | **0,3 – 0,5 $**               | 0,1 – 0,2 $                      |
| **Régulier** — 3 j/sem, 2 explications + 5 messages, 1 quiz/sem | **1,0 – 1,5 $**               | 0,3 – 0,5 $                      |
| **Intensif** — énergie pleine 6 j/sem, 3 quiz/sem              | **3,5 – 4,5 $**               | 1,0 – 1,5 $                      |
| **Borne dure** — plafond d'énergie 30/j, tout en `rich`        | ≈ 16 $/mois **— jamais atteinte** : le plafond monétaire coupe avant (R-11) | ≈ 5 $/mois |

**Ce que ces chiffres décident** :

- Les **plafonds par défaut de Q-6** (0,50 $/jour, 5 $/mois) laissent passer le profil intensif
  sur un modèle capable, tout en rendant le scénario de facture surprise **arithmétiquement
  impossible**.
- Le **rechargement minimal** d'un compte fournisseur (de l'ordre de 5 $ chez la plupart — à
  vérifier à l'implémentation) couvre **1 à 12 mois** d'usage selon le profil et le modèle. C'est
  l'argument à écrire dans la console, et il vaut mieux que n'importe quelle promesse : la famille
  voit ce qu'elle dépense.
- Le **choix du modèle change la facture d'un facteur 3 à 4** — d'où R-19 et D-11 : conseiller,
  mesurer, ne jamais décider à la place du parent.

## Annexe B — Qui livre quoi (é29 / é11), pour qu'aucune ligne ne soit écrite deux fois

| Brique                                                    | Étude & lot                        |
| --------------------------------------------------------- | ---------------------------------- |
| Adaptateur, comptabilité, kill-switches (**la porte**)    | **é29 lot 1** (remplace é11 lot 0 — Q-1) |
| Coffre de clés, console parent, consentement              | **é29 lot 2**                      |
| Activation par élève, budgets, coupure                    | **é29 lot 3**                      |
| **Forge** — quiz personnalisé à la demande de l'élève     | **é29 lot 4**                      |
| Console de dépense et de qualité, conseil de modèle       | **é29 lot 5**                      |
| Profil d'apprentissage (« learner pack »)                 | é11 §2.2 (lot 1)                   |
| Explication personnalisée post-review, reformulations     | é11 lot 1                          |
| Plan du jour commenté                                     | é11 lot 2                          |
| **Chat IA cadré** (SSE, champ libre, historique)          | é11 lot 3                          |
| Boucle de compréhension, escalades, compteur parent       | é11 lot 4                          |
| Exercices ciblés choisis **par le tuteur**                | é11 lot 5 (à ne pas confondre avec la Forge, choisie par l'élève) |
| Bilans hebdomadaires                                      | é11 lot 6                          |
| Énergie (mécanique de jeu, UI)                            | é11 R-12 et lot 7 — é29 n'en change que le **plafond réglable** (R-9) |
| Gabarits de prompts, validateur de sortie                 | é11 annexe B et §3.4 — **normatifs pour é29 aussi**, y compris la Forge |

Règle de tranchage en cas de doute : **si la brique parle de pédagogie, elle est à é11 ; si elle
parle de qui paie, de quel modèle répond, ou de ce que l'élève demande lui-même, elle est ici.**

## Annexe C — Codes d'erreur stables (fournisseur → produit)

Le corps d'erreur brut d'un fournisseur n'est **jamais** propagé (R-5). Il est traduit en un code
stable, stocké dans `ai_credentials.last_error_code` / `ai_usage_events.error_code`, traduit
FR/EN/AR côté client (motif des codes stables de `parent-code-errors.ts`).

| Code                  | Origine typique                     | Ce que la console parent dit          | Effet produit                                        |
| --------------------- | ----------------------------------- | ------------------------------------- | ---------------------------------------------------- |
| `AI_KEY_INVALID`      | 401 / 403                           | La clé est refusée par le fournisseur | `status='invalid'`, mode éteint, e-mail parent (une fois) |
| `AI_MODEL_UNKNOWN`    | 404 / 400 sur l'id de modèle        | Ce modèle n'existe pas chez ce fournisseur | Enregistrement refusé (US-2) ou mode éteint      |
| `AI_CREDIT_EXHAUSTED` | 402 / 429 « insufficient quota »    | Le compte fournisseur n'a plus de crédit | Mode éteint, e-mail parent (une fois)             |
| `AI_RATE_LIMITED`     | 429 (débit)                         | Trop d'appels d'un coup               | 2 retries, puis dégradé silencieux côté élève        |
| `AI_PROVIDER_DOWN`    | 5xx, timeout                        | Le fournisseur ne répond pas          | Dégradé silencieux (é11 R-15), énergie remboursée    |
| `AI_HOST_NOT_ALLOWED` | `base_url` hors liste blanche       | Cette adresse n'est pas autorisée     | Enregistrement refusé (R-6)                          |
| `AI_BUDGET_REACHED`   | interne (R-11)                      | Plafond atteint, date et montant      | Appel non émis, dégradé, alerte 100 %                |
| `AI_OUTPUT_REJECTED`  | validateur de sortie (é11 §3.4)     | Compté dans le taux de rebut          | 1 retry, puis dégradé                                |
| `AI_FORGE_NO_QUORUM`  | < N items validés (§3.6)            | Compté dans le taux de rebut          | Échec honnête, énergie remboursée                    |
