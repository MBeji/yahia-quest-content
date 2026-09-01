# Annexe é31 — Bibliothèque des mécanismes d'engagement

> Annexe de [`ETUDE.md`](./ETUDE.md). Elle répond à la commande d'origine — « trouve des
> mécanismes d'attractivité comme utilisés par les réseaux sociaux et les jeux vidéo » — en
> trois temps : les fondations psychologiques (§A), le catalogue des mécaniques avec, pour
> chacune, **l'état réel chez nous** relevé dans le code le 2026-09-01 (§B–§C), et les lignes
> rouges d'un produit destiné à des mineurs (§D). Les verdicts (prendre / différer / refuser)
> sont consolidés au §E ; l'ETUDE.md n'exécute que les « prendre ».

## A. Les fondations psychologiques — le pourquoi avant le quoi

Une mécanique n'est jamais bonne « parce que Duolingo le fait » : elle est bonne parce qu'elle
active un ressort documenté. Les douze ressorts qui portent tout ce qui suit :

1. **Autodétermination (Deci & Ryan)** — la motivation intrinsèque naît de trois besoins :
   **autonomie** (je choisis), **compétence** (je progresse et je le vois), **relation** (je
   compte pour quelqu'un). C'est la boussole : chaque mécanique doit nourrir au moins un des
   trois, sinon elle fabrique de la motivation extrinsèque qui s'effondre quand la récompense
   s'arrête (effet de sur-justification — documenté par les méta-analyses de gamification en
   éducation, qui trouvent un effet positif en moyenne MAIS conditionnel au design).
2. **Flow (Csikszentmihalyi)** — l'engagement maximal vit dans le couloir entre ennui et
   anxiété : difficulté ≈ compétence + ε. Chez nous, c'est le métier du moteur adaptatif
   (é04/é30) — l'algorithme qui maximise l'apprentissage EST notre « algorithme de feed ».
3. **Renforcement à ratio variable (Skinner)** — la récompense imprévisible crée le
   comportement le plus persistant (machines à sous, coffres, pull-to-refresh). Puissant et
   dangereux : jamais sur l'accès au savoir, seulement sur le bonus/cosmétique, avec un socle
   garanti.
4. **Aversion à la perte (Kahneman & Tversky)** — perdre 10 fait plus mal que gagner 10 ne
   fait du bien. C'est le moteur des streaks et des relégations. À manier avec un filet
   (gel, rachat, pardon) : Duolingo a itéré des centaines d'expériences sur le seul streak et
   a convergé vers PLUS de pardon, pas moins — la cruauté fait churner.
5. **Progrès doté (Nunes & Drèze)** — une jauge déjà entamée (2/12) est complétée bien plus
   souvent qu'une jauge vide (0/10). S'applique aux collections, aux barres de chapitre, aux
   paliers de badge.
6. **Effet Zeigarnik** — la tâche inachevée occupe l'esprit. « Il te reste 3 questions dans
   ce chapitre » ramène mieux qu'un « reviens pratiquer » générique. Chez nous,
   `resolveNextAction` est déjà l'incarnation de ce ressort — côté écran ; rien ne le porte
   hors de l'app.
7. **Gradient d'objectif** — on accélère près du but. « Plus que 20 XP avant le niveau 8 »
   déclenche le « allez, une dernière série ».
8. **Preuve sociale (Festinger)** — on se calibre sur les pairs : classements, « ta classe a
   résolu N questions », duels.
9. **Nouveau départ (fresh start effect)** — lundi, rentrée, nouvelle saison : les compteurs
   remis à zéro relancent ceux qui avaient décroché. Un classement cumulatif à vie est
   l'anti-mécanique exacte : il fige la hiérarchie et décourage l'arrivant.
10. **Pic-fin (Kahneman)** — on mémorise le pic émotionnel et la fin. Terminer la session sur
    une célébration (« objectif du jour atteint, à demain ! ») colore le souvenir entier.
11. **Investissement (modèle Hook, Nir Eyal)** — déclencheur → action → récompense variable →
    **investissement** : chaque session doit augmenter la valeur du compte (série, collection,
    avatar, profil), donc le coût subjectif d'arrêter. Le modèle décrit aussi notre trou
    actuel : nous avons l'action et la récompense, presque pas de déclencheur externe et un
    investissement pauvre (6 emojis, 4 badges atteignables).
12. **Identité** — le niveau ultime : « je suis quelqu'un qui pratique tous les jours ».
    Duolingo vend une identité, pas des leçons. Titres, classes de héros, avatars, rituels.

## B. Catalogue jeux vidéo — mécanique par mécanique, avec l'état réel chez nous

Légende « état » : ✅ existe et vit · 🟡 existe mais éteint/invisible/incomplet · ⬜ n'existe
pas. Relevé du 2026-09-01 (source : code + migrations, inventaire complet en tête d'ETUDE.md).

### B1. Boucle de base & « juice »

| Mécanique                                                                 | Référence              | État chez nous                                                     |
| ------------------------------------------------------------------------- | ---------------------- | ------------------------------------------------------------------ |
| Feedback immédiat par réponse (son, verdict)                              | tout jeu d'arcade      | ✅ `use-instant-feedback` + 17 sons procéduraux + haptique         |
| Combo de bonnes réponses qui escalade                                     | Tetris, OSU            | ✅ x3→x10 (« Combo/En feu/Imparable/Légendaire ») + échelle sonore |
| Célébration de fin proportionnelle                                        | tout RPG               | ✅ confettis, grille de gains, rang boss                           |
| Level-up plein écran                                                      | tout RPG               | ✅ couronne + 60 particules + son dédié                            |
| Barre d'XP qui se remplit, pièces qui s'incrémentent, « +50 XP » flottant | Duolingo, Clash Royale | ⬜ les nombres changent sans animation de comptage                 |
| Célébration hors quête (fin de donjon, victoire de duel, gain de ligue)   | —                      | ⬜ le donjon et la ligue finissent sans fête                       |

**Verdict** : le juice de la boucle est notre point fort — le compléter (compteurs animés,
célébrations donjon/duel/ligue) est un polissage à faible risque, pas un chantier.

### B2. Progression & déblocage

| Mécanique                                                 | Référence             | État chez nous                                                                                          |
| --------------------------------------------------------- | --------------------- | ------------------------------------------------------------------------------------------------------- |
| XP / niveaux                                              | universel             | ✅ mais courbe **linéaire infinie** (200 XP/niveau, du 1 au 50)                                         |
| Classe/titre qui évolue                                   | RPG                   | 🟡 `hero_class` automatique, 6 paliers, non choisi, stocké en FR non accentué affiché tel quel en AR/EN |
| Évolution visuelle du personnage                          | Pokémon               | 🟡 `avatar_tier` (6 paliers) **calculé, transporté au client, jamais rendu**                            |
| Étoiles/couronnes de maîtrise par chapitre (rejouabilité) | Candy Crush, Duolingo | 🟡 le rappel actif (é17) est notre « couronne » — mais aucune vue collection                            |
| Carte de monde qui s'éclaire                              | tout jeu d'aventure   | ✅ `/parcours` journey map à nœuds, sans faux verrou (é22 R-11)                                         |
| Arbre de compétences visible                              | RPG                   | 🟡 la carte à 4 états é30 existe (math 9ᵉ seulement, par construction)                                  |

**Verdict** : rendre visible ce qui est déjà calculé (`avatar_tier`) est gratuit ; la courbe de
niveaux est un sujet é09 (économie), pas é31.

### B3. Rituels quotidiens — le cœur du retour volontaire

| Mécanique                                               | Référence                   | État chez nous                                                                                                                                                                                                                                        |
| ------------------------------------------------------- | --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Streak quotidien visible partout                        | Duolingo, Snapchat          | ✅ flamme sur dashboard/classement/résultat                                                                                                                                                                                                           |
| Gel de série (freeze)                                   | Duolingo                    | ✅ `bouclier_flamme` 250 pièces, 1 jour manqué exactement                                                                                                                                                                                             |
| Rachat de série                                         | Duolingo (repair)           | 🟡 `recoverStreak` 15 pièces existe **mais la bannière qui y mène est quasi inatteignable** (elle teste `current_streak === 0`, valeur jamais persistée) — et é09 A16 constate l'inverse : à 15 pièces « la série s'achète » (38 % des jours manqués) |
| Objectif du jour choisi par l'élève                     | Duolingo (daily goal)       | ⬜ l'anneau du jour est fixe (100 XP) et **affiche un chiffre faux** (0 % ou 50 %, jamais l'XP réelle)                                                                                                                                                |
| Missions quotidiennes rotatives                         | WoW, Fortnite, Clash Royale | 🟡 tables et triggers en place, mais **une seule mission, identique depuis le premier jour** (`3_exercises`) ; les types `10_min`, `complete_chapter`, `maintain_streak_5` sont documentés dans le schéma et jamais instanciés                        |
| Première victoire du jour (bonus)                       | League of Legends           | ⬜                                                                                                                                                                                                                                                    |
| Coffre quotidien lié à la pratique                      | Clash Royale                | ⬜                                                                                                                                                                                                                                                    |
| Rendez-vous pédagogique (« tes révisions t'attendent ») | Anki, Duolingo              | ✅ « Révision du jour » ≤ 3 items, pondérée misconceptions — notre meilleur rendez-vous, purement in-app                                                                                                                                              |

**Verdict** : c'est ici que le ratio effort/effet est le meilleur. La rotation des missions et
un anneau honnête réutilisent des tables existantes ; le rachat de série est un fix d'une
condition ; le bonus « première victoire du jour » et le coffre passent par é09 (valeurs).

### B4. Récompense variable (dosée)

| Mécanique                                              | Référence             | État chez nous                               |
| ------------------------------------------------------ | --------------------- | -------------------------------------------- |
| Coffre semi-aléatoire (socle garanti + bonus surprise) | Clash Royale          | ⬜ toutes les récompenses sont déterministes |
| Événement surprise (question dorée, double XP)         | Candy Crush, Fortnite | ⬜                                           |
| Gacha / loot boxes payantes                            | mobile F2P            | ⬜ et **refusé** (§D)                        |

**Verdict** : un unique point de variabilité (coffre de fin d'objectif du jour, cosmétique ou
pièces bonus, probabilités affichées) suffit à créer le frisson sans le casino. Valeurs → é09.

### B5. Social & compétition

| Mécanique                                            | Référence                 | État chez nous                                                                                                                                                                                        |
| ---------------------------------------------------- | ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Ligue hebdomadaire par cohorte, reset chaque semaine | Duolingo (cohortes de 30) | 🟡 existe (é05) mais **par centile global**, sans promotion/relégation persistante, **sans notification ni écran de résultat** — le gain tombe lundi 02:30 et l'élève ne le découvre que s'il revient |
| Classement à fenêtre courte (« cette semaine »)      | tous les jeux mobiles     | ⬜ le classement XP est **cumulatif à vie, sans reset** : un compte de septembre ne rattrapera jamais un compte de juin                                                                               |
| Duel + revanche                                      | Clash Royale              | 🟡 duels livrés (é05), **aucune revanche, aucune invitation, aucun ami** — matchmaking anonyme seulement                                                                                              |
| Streak de duo (série partagée à deux)                | Snapchat                  | ⬜ (exige un graphe d'amis — différé)                                                                                                                                                                 |
| Défi coopératif de classe                            | Kahoot                    | 🟡 le seul levier relationnel est l'objectif famille (`FamilyGoalCard`)                                                                                                                               |
| Présence (« N élèves s'entraînent »)                 | tout MMO                  | ⬜                                                                                                                                                                                                    |
| Kudos/réactions sur les exploits                     | réseaux sociaux           | ⬜                                                                                                                                                                                                    |

**Verdict** : fermer la boucle de la ligue (résultat célébré + notifié — la dette US-7 de é05)
et offrir une fenêtre courte de classement sont les deux gestes à fort effet. Tout ce qui
exige un graphe social (amis, duo-streak, kudos) est différé : produit à zéro canal
d'acquisition, cohortes vides (§D et RISK).

### B6. Collection & complétion

| Mécanique                                                                         | Référence          | État chez nous                                                                                                                                                                                                                                                                                                                                                                      |
| --------------------------------------------------------------------------------- | ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Badges avec familles et séries (3/5 possédés)                                     | Xbox/PSN, Duolingo | 🟡 13 badges seedés, **4 seulement décernables** (`first_quest`, `perfect_score`, `speed_demon`, `streak_7`), tous obtenus la première semaine ; **9 morts** (`streak_30`, `boss_slayer`, `level_10`, `math_master`, `polyglot`, `collector`, `rich_kid`, `night_owl`, `math_blitz`) ; `rule_key` jamais lu ; **aucune vitrine des badges verrouillés, aucune progression visible** |
| Vitrine / profil qui expose les trophées                                          | tout jeu           | ⬜ seuls les badges obtenus s'affichent, dans la boutique                                                                                                                                                                                                                                                                                                                           |
| Badge saisonnier exclusif (rareté honnête : accessible à tous pendant la fenêtre) | Fortnite           | ⬜                                                                                                                                                                                                                                                                                                                                                                                  |
| Cosmétique riche (cadres, titres, thèmes, bordures)                               | tout F2P           | 🟡 6 skins-emoji, catalogue **jamais retouché depuis le 2026-05-22** ; les pièces n'ont que 2 puits                                                                                                                                                                                                                                                                                 |

**Verdict** : les badges sont le progrès doté (§A5) le moins cher du produit : tout rallumer,
montrer le verrouillé avec sa condition (cohérent avec é22 R-30 : « tout verrou énonce sa
condition »), donner une vitrine. Les nouveaux cosmétiques sont le puits de pièces que é09
cherche (`sink_ratio`).

### B7. Saisons & événements

| Mécanique                                                            | Référence               | État chez nous                                                                                                                                                                                                                   |
| -------------------------------------------------------------------- | ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Saison courte à reset (fresh start industrialisé)                    | ligues Duolingo         | 🟡 la semaine ISO de la ligue de duels — seul cycle du produit                                                                                                                                                                   |
| Passe de saison (piste de paliers, gratuite)                         | Fortnite battle pass    | ⬜ (différé : lourd, P-7)                                                                                                                                                                                                        |
| Événements calendaires courts (révisions d'examen, rentrée, Ramadan) | tous les live games     | ⬜ **rien** — la seule chose datée est la bannière de rentrée (suggestion de classe, pas un événement) ; le calendrier scolaire tunisien (devoirs de synthèse, concours, Ramadan) est pourtant une machine à événements naturels |
| Défi de la semaine qui expire dimanche (FOMO doux)                   | stories, défis Fortnite | 🟡 `beat_2_bosses` existe mais unique et invariable                                                                                                                                                                              |
| Double XP week-end                                                   | tous les live games     | ⬜ (multiplicateurs = économie → é09)                                                                                                                                                                                            |

**Verdict** : commencer par un « événement » minimal piloté par une table (fenêtre + défi
spécial + badge saisonnier), calé sur le calendrier scolaire réel. Le passe de saison attend
des utilisateurs et des mesures.

### B8. Rendez-vous & retours (hors app)

| Mécanique                                                           | Référence               | État chez nous                                                                                                                                                                 |
| ------------------------------------------------------------------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Notification « ta série est en danger » le soir                     | Duolingo                | ✅ 1 cron/jour 18:00 UTC — mais **en français pour tous** (locale non stockée serveur)                                                                                         |
| Rappel du plan de révision                                          | Anki                    | ✅ `tutor-daily-plan`, exclusion croisée ≤ 1 push/jour — bonne règle, à garder                                                                                                 |
| Relance de l'élève qui a PERDU sa série                             | Duolingo (win-back)     | ⬜ **le trou le plus grave** : le rappel ne vise que `current_streak > 0` — celui qui a cassé sa série n'est **plus jamais recontacté**                                        |
| Notification d'événement social (duel reçu/fini, résultat de ligue) | tous                    | ⬜ (dette é05 US-7 assumée)                                                                                                                                                    |
| Récap hebdo type « ta semaine »                                     | Spotify Wrapped, Strava | 🟡 le bilan El Ostedh (é11 lot 6) existe **mais dépend d'une clé IA jamais branchée → jamais produit en prod** ; aucune version déterministe/visuelle ; l'élève ne reçoit rien |
| Email de ré-engagement                                              | tous les SaaS           | ⬜ aucun email produit (auth Supabase seulement) — assumé, le push est le canal                                                                                                |
| Énergie qui se régénère (appointment forcé)                         | Candy Crush             | ⬜ et **refusé** sur l'accès au savoir (§D) ; l'énergie du tuteur IA (D-14 é11) reste une mécanique de jeu, pas un levier de retour                                            |

**Verdict** : le canal existe (infra push + cron + audiences) ; il est simplement pauvre
(3 payloads), monolingue et aveugle aux moments qui comptent. L'enrichir est du travail
d'audience SQL, pas d'infrastructure.

### B9. Narration & personnage

| Mécanique                                                       | Référence      | État chez nous                                                                                                                                                                 |
| --------------------------------------------------------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Mascotte à personnalité qui porte notifications et célébrations | Duo (Duolingo) | 🟡 **El Ostedh existe et parle bien** (voix déterministe, 2×4 moments, jamais culpabilisant, signé « الأستاذ ») mais **n'a aucun visage** — icône générique, zéro illustration |
| Rival récurrent                                                 | Pokémon        | ⬜                                                                                                                                                                             |
| Arcs d'histoire, cinématiques                                   | RPG            | ⬜ univers shonen posé (vocabulaire, Hall des Héros, citations d'auteurs fictifs) sans aucune histoire                                                                         |

**Verdict** : donner un visage à El Ostedh est le chantier « identité » au meilleur ratio
(un personnage > un thème). Dépend d'assets illustrés → porte humaine (direction artistique),
à séquencer avec é19 (illustrations). Rival et narration : différés.

### B10. Accueil (D0) — la première session décide de la deuxième

| Mécanique                                                | Référence                            | État chez nous                                                                                                     |
| -------------------------------------------------------- | ------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| Victoire garantie dans les 3 premières minutes           | Duolingo (leçon 1 avant inscription) | ⬜ onboarding = 3 écrans de **choix**, aucune question jouée, aucune réussite                                      |
| Récompense de bienvenue (pièces de départ, objet offert) | tous les F2P                         | ⬜ compte neuf : 0 XP, 0 pièce, aucun choix d'avatar                                                               |
| Choix d'avatar/pseudo à l'entrée (identité immédiate)    | tous                                 | ⬜ pseudo dérivé de l'email, avatar par défaut                                                                     |
| Conversion du joueur anonyme (« garde tes XP »)          | jeux web                             | ⬜ la pratique sans compte existe (très bien) mais **aucun appel à créer un compte pour conserver la progression** |

**Verdict** : chantier entier, à petit coût. La première session doit finir sur : une réussite
jouée, une récompense reçue, une identité choisie, et une raison datée de revenir demain.

## C. Mécaniques des réseaux sociaux — ce qu'on transpose, ce qu'on refuse

| Mécanique                    | Ce que fait le réseau                          | Transposition chez nous                                                                                           | Verdict          |
| ---------------------------- | ---------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ---------------- |
| Streak (Snapchat)            | série d'échanges à deux, coût social de casser | streak personnel ✅ déjà là ; duo-streak différé (exige des amis)                                                 | ✅ / différé     |
| Feed infini, pull-to-refresh | récompense variable **sans fin de session**    | — aucune surface sans fin ; la session a un objectif et une fin célébrée                                          | ❌ refusé        |
| Notifications de rafale      | « X a posté », volume illimité                 | ≤ 1 push/jour/élève (règle déjà en place, à généraliser), fenêtre du soir, opt-out à un geste                     | ⚠️ version douce |
| Validation sociale (likes)   | dopamine sur la personne                       | kudos sur les **exploits** (réussites, séries), jamais sur la personne — différé avec le social                   | différé          |
| Stories éphémères            | FOMO quotidien                                 | défi de la semaine qui expire dimanche ; **jamais** de contenu pédagogique qui expire                             | ⚠️ doux          |
| Récap partageable (Wrapped)  | fierté + viralité                              | « Ta semaine » : carte visuelle in-app, partage **vers le parent** (lien alliance existant), pas de réseau public | ✅ adapté        |
| Présence (« en ligne »)      | pression sociale permanente                    | compteur anonyme agrégé éventuel — différé                                                                        | différé          |
| Algorithme d'engagement      | maximise le temps passé                        | le moteur adaptatif maximise **l'apprentissage** (flow §A2) — c'est déjà notre ADN                                | ✅ acquis        |

## D. Lignes rouges — produit pour mineurs (6–18 ans)

Cadre de référence : l'esprit de l'« age appropriate design » (protection des mineurs contre
les dark patterns) + la doctrine maison (é26 P-7, é22 §2.6, D-14, digests R-11). Ces règles
sont reprises comme `R-*` normatives dans ETUDE.md :

1. **La métrique de garde est l'apprentissage.** Un mécanisme qui augmente les minutes sans
   augmenter la précision/progression est un échec, même s'il « marche ». Toute mesure
   d'engagement se publie à côté d'une mesure d'apprentissage.
2. **Jamais de limitation d'accès au savoir** : pas d'énergie sur la pratique, pas de vies,
   pas de contenu pédagogique qui expire, pas de faux verrou (é22 R-11 déjà actée).
3. **Pas d'argent réel dans la boucle** (phase gratuite actée 2026-06-21) ; le hasard (coffre)
   ne porte que du cosmétique/bonus gagné en jouant, avec un socle garanti et des probabilités
   affichées. Aucune esthétique de casino (pas de roue, pas de machine à sous).
4. **Notifications frugales** : ≤ 1 push/jour/élève (l'exclusion croisée existante devient la
   règle générale), fenêtre du soir uniquement, jamais la nuit, opt-out en un geste,
   localisées dans la langue de l'élève. Le ton est celui d'El Ostedh : jamais culpabilisant
   (règle déjà écrite dans `coaching.ts` — elle s'étend au push).
5. **Compétition sans humiliation** : cohortes comparables (« Ma classe » d'abord), pas
   d'exposition publique de l'échec, le bas de ligue n'est jamais nommé « relégué » devant
   les autres. L'exclusion des tricheurs reste silencieuse (é10/é22 R-26).
6. **Fin de session propre** : l'objectif du jour atteint se célèbre comme une **fin**
   (« à demain ! »), on n'enchaîne pas automatiquement sur « encore un » (pic-fin §A10,
   et c'est ce qu'un parent doit pouvoir constater).
7. **Transparence parents** : le suivi parental voit la même vérité (temps réel mesuré par
   `learning_pulses`, série, progrès). L'engagement se construit à ciel ouvert — c'est un
   avantage concurrentiel, pas une contrainte.
8. **Vocabulaire** : l'objectif interne est « l'envie de revenir » (rétention volontaire).
   Le mot « addiction » est la métaphore de départ, pas le cahier des charges — et aucun
   mécanisme retenu ici ne survivrait à un test « est-ce encore défendable si un parent nous
   regarde le construire ? ».

## E. Synthèse des verdicts

**Prendre en v1 (l'ETUDE.md les contractualise)** — rallumer et compléter l'existant :

1. Mesurer la rétention et instrumenter les moments clés (rien de tout le reste n'est
   pilotable sans ça — é26 KPI-4, STATUS KPI-2 🔴).
2. Missions quotidiennes **rotatives** + anneau du jour honnête + objectif choisi.
3. Badges tous décernables + collection visible avec conditions + familles.
4. Rachat de série atteignable + relance de l'élève qui a perdu sa série.
5. Push localisés + les 3 déclencheurs manquants à plus forte valeur (résultat de ligue,
   série perdue, jalon de série).
6. La ligue **fermée en beauté** : écran de résultat/podium + classement « cette semaine ».
7. Accueil D0 : victoire jouée + bienvenue + identité + conversion anonyme→compte.
8. Récap « Ta semaine » déterministe (les chiffres existent — `get_tutor_digest_inputs`),
   partage parent.
9. Un premier événement calendaire piloté par table (rentrée / semaine de révisions).
10. `avatar_tier` rendu + 2-3 puits cosmétiques (cadres/titres) — valeurs via é09.

**Différer (v2, gated sur les mesures du lot 1 et l'arrivée d'utilisateurs réels)** :
passe de saison, coffres à récompense variable, graphe d'amis + duo-streak + kudos +
présence, revanche/invitations de duel, visage illustré d'El Ostedh (porte artistique, à
articuler avec é19), rival narratif, double XP (économie), bonus première victoire du jour.

**Refuser (définitif, §D)** : feed infini, énergie sur la pratique, contenu pédagogique
expirant, loot payant / esthétique de casino, notifications en rafale ou nocturnes,
classement humiliant, temps d'écran comme objectif.

## F. Sources — faits vérifiés (recherche du 2026-09-01)

Chaque fait a été lu dans sa source primaire (pas de chiffre de blog marketing de seconde
main). Précaution générale : les chiffres Duolingo sont des mesures **internes racontées par
l'entreprise ou ses ex-dirigeants**, jamais auditées — citer « selon Duolingo ».

1. **Ligues Duolingo** : +17 % de temps d'apprentissage global et ×3 sur les apprenants très
   engagés (≥ 1 h/jour, 5 j/sem.) au lancement des leaderboards hebdomadaires ; refonte
   « rétention d'abord » : CURR +21 %, DAU ×4,5 en ~4 ans — Jorge Mazal (ex-CPO),
   lennysnewsletter.com/p/how-duolingo-reignited-user-growth (2023). Mazal reconnaît
   lui-même un **biais de sélection** derrière « streak long → abandon quasi nul ».
2. **Pardon de streak mesuré** : le « Streak Wager » (miser des gems sur 7 jours tenus) a
   amélioré la rétention J7 de **+14 %** ; l'amulette de week-end : +4 % de retour, −5 % de
   pertes de série. Et : les utilisateurs qui « bingent » churnent plus que ceux qui étalent
   — blog.duolingo.com/how-streaks-keep-duolingo-learners-committed… (10 mai 2017).
3. **Notifications optimisées** (bandit multi-bras sur le texte des rappels, production) :
   **+0,5 % de DAU total, +2 % de rétention des nouveaux** — Yancey & Settles, KDD 2020,
   research.duolingo.com/papers/yancey.kdd20.pdf. La source la plus rigoureuse du dossier.
4. **Mascotte** : la moitié des porteurs du widget Duo ont un streak ≥ 6 mois, rétention
   meilleure « même en contrôlant » l'auto-sélection — blog.duolingo.com/widget-feature/
   (29 août 2023). ⚠️ Le « +60 % grâce au widget » qui circule est invérifiable, ne pas citer.
5. **Échelle atteinte** : 40,5 M DAU (+51 % YoY) fin 2024 (earnings T4 2024) ; ~50 M DAU et
   **> 10 M d'utilisateurs à streak ≥ 365 jours** début 2026 (PG Connects, janv. 2026,
   pocketgamer.biz du 16 févr. 2026).
6. **Streaks Snapchat (12-15 ans, N = 2 483, Flandre)** : 83,3 % des filles et 66,9 % des
   garçons présents sur Snapchat entretiennent un streak (plus longs : 223 j filles /
   179 j garçons) ; associations avec l'usage problématique **réelles mais faibles**
   (r ≈ 0,1-0,18) ; stress documenté à la **perte** — van Essen & Van Ouytsel, Telematics
   and Informatics Reports 11 (2023) 100087.
7. **Battle pass** : ~30-60 % du revenu des shooters F2P (estimation d'expert, non auditée
   — GameMakers, 4 mars 2025) ; le moteur d'habitude est la mission quotidienne calibrée
   « ≥ 1 palier de passe par jour » (Game Developer, 18 mars 2022, qualitatif).
8. **Loot boxes et mineurs** : chez les 16-18 ans, les joueurs en situation de jeu
   problématique dépensent **> 5×** plus en loot boxes ; le lien est plus de deux fois plus
   fort que chez les adultes ; c'est le **hasard payé** + la rareté temporelle qui sont
   pointés — Zendle, Meyer & Over, Royal Society Open Science 6(6):190049 (2019). Fonde
   notre refus §D3 (jamais d'argent réel sur du hasard ; coffre = socle garanti, cosmétique).
9. **Méta-analyse gamification & apprentissage** : g = 0,49 (cognitif), 0,36 (motivation),
   0,25 (comportement) sur 40 expériences — mais **seuls les effets cognitifs survivent**
   aux sous-analyses de qualité — Sailer & Homner, Educational Psychology Review 32 (2020).
10. **Le contre-exemple** : badges + leaderboard sur 16 semaines → motivation intrinsèque en
    baisse et notes finales plus basses (médiation par la motivation) — Hanus & Fox,
    Computers & Education 80 (2015). ⚠️ N = 80, non randomisé — c'est un avertissement
    (comparaison sociale « qui ne désigne qu'un gagnant »), pas une loi.
11. **SDT** : les récompenses vécues comme contrôlantes minent l'autonomie, « surtout pour
    les non-gagnants » ; la voie saine est la motivation extrinsèque **internalisée** — XP et
    badges au service du sentiment de compétence, pas du contrôle — Ryan & Deci,
    Contemporary Educational Psychology 61:101860 (2020).
12. **Cadre mineurs (UE)** : les lignes directrices DSA de la Commission européenne
    (14 juillet 2025) recommandent de **désactiver par défaut pour les mineurs** streaks de
    communication, autoplay, notifications push et « design persuasif visant principalement
    l'engagement » — digital-strategy.ec.europa.eu/en/library/commission-publishes-guidelines-protection-minors.
    Notre lecture (reprise en R dans l'étude) : push **opt-in** (c'est déjà le cas), streak
    **pardonnable** et jamais culpabilisant, aucun autoplay. Le UK Age Appropriate Design
    Code (ICO) serait le second pilier — inaccessible à la vérification ce jour (403), ne
    pas le citer précisément sans lecture.
13. **Cas d'école ed-tech (échec éthique)** : Prodigy Math, plainte de 22 associations à la
    FTC (19 févr. 2021, Fairplay) — récompenses virtuelles « teasées » pour vendre un
    abonnement aux familles, inégalité visible en classe. C'est une plainte, pas un
    jugement ; elle fonde notre règle « aucune pression commerciale dans la boucle »
    (cohérente avec la gratuité de phase et l'interdit « premium » existant).
