# Étude 31 — L'envie de revenir : engagement & rétention à hauteur de jeu vidéo

> **Statut** : **LIVRÉE EN PRODUCTION le 2026-09-03** — les 8 lots, arena#949, squashée sur
> `main` en `7bdbccd` ; journal §8. Q-1…Q-4 arbitrées le 2026-09-01 (§7)
> **Priorité** : 31 · **Valeur** : 🔁 le retour de l'élève cesse de reposer sur sa seule
> volonté — mesuré, rappelé, célébré, rythmé ; l'élève ouvre l'app parce qu'il en a envie,
> pas parce qu'on l'y force · **Complexité** : moyenne+
> **Architecte** : Fable 5 / 2026-09-01 · **Exécuteur cible** : Sonnet (ou équiv.)
> **Dépend de** : é22 (livrée — possède la boucle quotidienne/hebdo), é05 (livrée — possède
> duels & ligues), é09 (en exécution — possède **toute** valeur d'économie, é22 R-28),
> é26 (validée — KPI-4 rétention, P-7 feature fatigue) · **Bloque** : rien
> **Docs normatifs liés** : AGENTS.md, ARCHITECTURE.md, `docs/design-surfaces.md`,
> `docs/suivi-parental-quotidien.md`, [`ANNEXE-MECANISMES.md`](./ANNEXE-MECANISMES.md)

## 1. Contexte & objectif produit

### 1.1 La commande, et sa traduction honnête

La commande d'origine : « rendre la plateforme addictive comme les jeux vidéo — qu'un élève
veuille vraiment ouvrir et pratiquer, pas qu'on le force ». La seconde moitié corrige la
première : l'objectif n'est pas l'addiction (temps d'écran maximisé), c'est **le retour
volontaire** — un élève qui revient chaque jour parce que la session est agréable, courte,
gagnante, et qu'une raison précise de revenir demain lui a été donnée. La différence est
opérationnalisée au §1.4 (métrique de garde) et dans les lignes rouges (R-1…R-8) : tout
mécanisme qui ferait monter les minutes sans faire monter l'apprentissage est un échec.

### 1.2 L'état réel — un jeu déjà construit, à moitié éteint

Inventaire du code au 2026-09-01 (`main` arena, détail mécanique par mécanique dans
[`ANNEXE-MECANISMES.md`](./ANNEXE-MECANISMES.md) §B). Ce qui **vit** : la boucle de jeu est
excellente — feedback immédiat, 17 sons procéduraux, combos escaladants, confettis, level-up,
donjon, duels temps réel, ligue hebdomadaire par centile, « Révision du jour » pondérée par
les misconceptions, reprise unifiée (`resolveNextAction`), voix d'El Ostedh jamais
culpabilisante. C'est le point fort : **l'action et sa récompense immédiate**.

Ce qui est **éteint, invisible ou figé** — dix constats, chacun vérifié dans le code :

1. **Rien n'est mesuré.** Aucune vue, RPC ou écran de rétention ; PostHog est anonymisé au
   point de ne pas pouvoir la calculer (`$process_person_profile: false`) et ne reçoit que
   3 événements (`$pageview`, `video_open`, `dungeon_pool_scope`). STATUS KPI-2 : « rétention
   **jamais publiée** » — c'est é26 KPI-4, définie le 2026-07-19, restée lettre morte.
2. **Personne ne relance celui qui a décroché.** Le push « série en danger » ne vise que
   `current_streak > 0` : l'élève qui a perdu sa série n'est **plus jamais recontacté**. Il
   n'existe ni relance J+3/J+7, ni notification de résultat de ligue (dette assumée é05
   US-7), ni push de duel. 3 payloads au total, **en français pour tous** (la locale n'est
   pas stockée serveur).
3. **Les missions sont figées depuis le premier jour** : une quotidienne (`3_exercises`) et
   une hebdo (`beat_2_bosses`), identiques pour tous, pour toujours. Les types `10_min`,
   `complete_chapter`, `maintain_streak_5` sont documentés dans le schéma et jamais
   instanciés (constat déjà fait par é22 R-29). L'anneau du jour affiche un chiffre faux
   (0 % ou 50 %, jamais l'XP réelle).
4. **9 badges sur 13 sont morts** : seuls `first_quest`, `perfect_score`, `speed_demon`,
   `streak_7` sont décernables — tous obtenus la première semaine. `streak_30`,
   `boss_slayer`, `level_10`, `collector`, `rich_kid`, `math_master`, `polyglot`,
   `math_blitz`, `night_owl` ne tombent nulle part ; aucune collection visible, aucun badge
   verrouillé affiché, `rule_key` jamais lu.
5. **Le classement ne repart jamais.** XP cumulé à vie, sans reset ni saison : un compte de
   septembre ne rattrapera jamais un compte de juin — l'anti-« fresh start » exact (annexe
   §A9).
6. **La ligue se termine dans le silence** : le gain tombe lundi 02:30 par cron, aucun écran
   de podium, aucune notification ; l'élève ne le découvre que s'il revient tout seul.
7. **Le rachat de série est invisible** : la bannière teste `current_streak === 0`, valeur
   que `award_xp` ne persiste jamais — bouton quasi inatteignable. Pendant ce temps é09 A16
   constate l'inverse : à 15 pièces, la série **s'achète trop facilement** (38 % des jours
   manqués rachetés).
8. **Le compte naît à zéro** : onboarding = 3 écrans de choix, aucune question jouée, aucune
   récompense de bienvenue, pas de choix d'avatar ; le joueur anonyme n'est jamais invité à
   créer un compte pour garder sa progression.
9. **Aucun événement, aucune saison** hors la semaine ISO de la ligue : rien ne rythme
   l'année scolaire (rentrée, devoirs de synthèse, Ramadan, révisions) — la seule chose
   datée est une suggestion de changement de classe.
10. **L'investissement identitaire est pauvre** : 6 skins-emoji jamais renouvelés,
    `avatar_tier` calculé et jamais rendu, `hero_class` en français non accentué dans les
    3 langues, pas de titres, pas de cadres, pièces sans puits (é09 mesure le `sink_ratio`).

Diagnostic en une phrase, dans les termes du modèle Hook (annexe §A11) : **l'action et la
récompense sont livrées ; le déclencheur externe et l'investissement sont vides.** é22 §2.6
l'avait déjà écrit : « aujourd'hui le retour n'est motivé que par le streak — fragile ».

### 1.3 Objectif produit

Fermer la boucle de l'envie de revenir, en quatre verbes, sans ouvrir de nouvelle surface de
navigation (é26 P-7 — **rallumer avant d'ajouter**) :

- **Mesurer** — publier enfin la rétention (é26 KPI-4) et instrumenter les moments qui
  comptent : rien d'autre n'est pilotable sans ça.
- **Rappeler** — un canal de retour digne de ce nom : push localisés, ≤ 1/jour, qui couvrent
  les vrais moments (série perdue, résultat de ligue, jalon) et relancent une fois, jamais
  en rafale.
- **Célébrer** — chaque cycle a une fin fêtée : le jour (missions variées, anneau honnête),
  la semaine (podium de ligue, classement qui repart, récap « Ta semaine »), le parcours
  (badges tous vivants, collection visible).
- **Rythmer** — l'année scolaire tunisienne devient un calendrier d'événements courts, et la
  première session devient une victoire.

### 1.4 KPI mesurables

⚠️ **Assumé d'entrée** : au 2026-09-01 le produit n'a **aucun utilisateur retenu à mesurer**
(canal d'acquisition : « zéro depuis le 2026-06-13 », STATUS KPI-1 ; les 20-30 beta-testeurs
de l'action D3 ne sont pas recrutés). Les cibles ci-dessous sont donc **importées du
benchmark go-live** (`go-live/livrables/05-marketing/03-kit-commercial-kpis.md`), pas
calibrées sur une mesure — le lot 1 existe précisément pour remplacer l'opinion par la
mesure.

| KPI   | Définition                                                                                                      | Cible (benchmark)                                                                                 |
| ----- | --------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| KPI-A | **CURR maison publiée** (é26 KPI-4) : part des élèves actifs en semaine N revenus en semaine N+1                | publiée = calculable en un clic sur `/admin/engagement` + reportée dans la scorecard STATUS §1bis |
| KPI-B | Rétention D7 / D30 par cohorte d'inscription                                                                    | D7 ≥ 25-30 %, D30 ≥ 15 % ; alerte si D7 < 15 %                                                    |
| KPI-C | Part des actifs hebdo avec série ≥ 7 j                                                                          | à établir au lot 1 (référence interne)                                                            |
| KPI-D | Taux d'opt-in push et taux d'opt-out post-push                                                                  | opt-out mensuel < 5 % des opt-in (garde-fou R-4)                                                  |
| KPI-E | **Métrique de garde** : précision moyenne et progression (chapitres complétés/actif) publiées à côté de KPI-A/B | ne régresse pas quand l'engagement monte                                                          |

### 1.5 Ce que l'epic ne cherche PAS à faire

- **Pas d'acquisition** : le goulot du projet (KPI-1, « zéro canal ») est un problème de
  distribution, pas de produit — hors périmètre, cette étude prépare la rétention de ceux
  que l'acquisition amènera.
- **Pas de nouvelle économie** : aucune valeur XP/pièces/prix n'est inventée ici ; tout
  passe par é09 (é22 R-28), cf. §3.9.
- **Pas de refonte de la boucle de jeu** (é22 la possède) ni du gameplay duels/ligues (é05).
- **Pas d'IA** : tout é31 est déterministe et fonctionne sans clé (leçon STATUS : « un étage
  livré et jamais éprouvé est une hypothèse » — les bilans IA é11 ne tournent pas en prod).
- **Pas de graphe social** (amis, duo-streak, kudos, présence), **pas de passe de saison**,
  **pas de coffres aléatoires**, **pas de mascotte illustrée** en v1 — différés, gated sur
  les mesures du lot 1 (annexe §E « Différer »).
- **Pas de dark patterns** — la liste des refus définitifs est en annexe §E, normée ici en
  R-1…R-8.

## 2. Spécification fonctionnelle

### 2.1 Acteurs & user stories

**Élève** (acteur principal), **parent** (lecteur du même réel), **admin** (pilotage),
**visiteur anonyme** (conversion).

- **US-1** (élève) — Chaque jour, je découvre **3 missions du jour** variées et réellement
  faisables pour moi, dont je vois la progression ; les finir toutes se célèbre comme une
  fin de session (« objectif atteint, à demain ! »).
- **US-2** (élève) — Mon **anneau du jour** montre mon XP réel du jour sur un objectif que
  **je** choisis (50/100/200 XP) ; l'atteindre se célèbre.
- **US-3** (élève) — Je vois **toute la collection de badges** — obtenus et verrouillés avec
  leur condition (é22 R-30) — groupée en familles, avec la progression (« 3/5 ») ; chaque
  badge de la liste peut réellement tomber.
- **US-4** (élève) — Si je perds ma série, la bannière de **réparation** m'est réellement
  proposée (aujourd'hui inatteignable), et je reçois **une** notification de réparation le
  lendemain — jamais de harcèlement ensuite.
- **US-5** (élève) — Je reçois mes notifications **dans ma langue**, au plus **une par
  jour**, uniquement le soir, et je peux les couper en un geste. Les moments couverts :
  série en danger (existant), plan de révision (existant), **série perdue** (nouveau),
  **résultat de ligue** (nouveau, dette é05 US-7), **jalon de série 7/30/100** (nouveau),
  **retour au calme J+7** (nouveau, une seule fois par période d'absence).
- **US-6** (élève) — Le lundi, la ligue de la semaine passée m'accueille avec un **podium
  célébré** (rang, gains, son, confetti) au lieu d'un virement silencieux ; un badge de
  ligue existe pour les podiums.
- **US-7** (élève) — Le classement s'ouvre sur **« Cette semaine »** (XP de la semaine ISO,
  remis à zéro lundi) : un nouvel inscrit peut y exister dès sa première semaine ; le
  cumulatif à vie reste accessible en second onglet.
- **US-8** (élève) — Le lundi, ma carte **« Ta semaine »** me montre en une image : XP,
  missions, précision, série, badges et rang de ligue de la semaine — comparés à la semaine
  d'avant. Déterministe (aucune clé IA), et mon parent voit le même réel sur son suivi.
- **US-9** (élève, nouveau compte) — Ma première session se termine sur une **victoire
  jouée** (ma première quête est à un tap de l'onboarding), une **récompense de bienvenue**
  (pièces + choix du pseudo), et une raison datée de revenir demain (mes missions du jour).
- **US-10** (anonyme) — Quand je pratique sans compte, l'écran de résultat me dit ce que je
  **perds** (XP, série, badges non conservés) et m'invite à créer un compte — sans bloquer
  la pratique (acquis é22/é24 : le contenu reste jouable sans compte).
- **US-11** (élève) — Mon héros **évolue visiblement** : le palier d'avatar (déjà calculé)
  se voit, ma classe de héros est dans ma langue, et la boutique propose des cadres/titres
  qui me distinguent (puits de pièces é09).
- **US-12** (élève) — Pendant un **événement du calendrier scolaire** (rentrée, semaine de
  révisions…), un défi spécial borné dans le temps apparaît, avec un badge saisonnier que
  tout le monde peut obtenir pendant la fenêtre — et le contenu pédagogique, lui, n'expire
  jamais.
- **US-13** (admin) — Sur `/admin/engagement`, je lis : CURR hebdo (KPI-A), D1/D7/D30 par
  cohorte, DAU/WAU, distribution des séries, opt-in/opt-out push — calculés depuis Postgres,
  sans PII, read-only.
- **US-14** (parent) — Rien de nouveau à apprendre : le suivi existant reflète les mêmes
  faits (missions, série, temps réel `learning_pulses`) ; la carte « Ta semaine » de mon
  enfant est cohérente avec mon rapport hebdo.

### 2.2 Règles métier

**Lignes rouges (issues de l'annexe §D — non négociables, testées) :**

- **R-1** — La métrique de garde est l'apprentissage : toute surface qui publie un chiffre
  d'engagement (admin) publie à côté précision et progression (KPI-E). Aucun objectif de
  « temps passé » n'existe nulle part.
- **R-2** — Aucune limitation d'accès au savoir : pas d'énergie sur la pratique, pas de
  contenu pédagogique expirant, pas de faux verrou (é22 R-11). Seuls les **défis/badges**
  d'événement sont bornés dans le temps.
- **R-3** — Aucun hasard rémunéré, aucune esthétique de casino, aucun argent réel (phase
  gratuite actée 2026-06-21). Les récompenses é31 sont déterministes.
- **R-4** — Push : **≤ 1 par élève et par jour** (l'exclusion croisée existante devient un
  pipeline de priorité unique), fenêtre du soir (~19:00 Tunis, cron existant), jamais la
  nuit, opt-in explicite (conforme à l'esprit des lignes directrices mineurs DSA — annexe
  §F.12), opt-out en un geste, ton El Ostedh (« jamais culpabilisant » — la règle de
  `coaching.ts` s'étend aux push). La relance d'absent est **unique** par période d'absence
  (J+7), jamais répétée. Le guide parent documente l'opt-in (Q-1, arbitrée).
- **R-5** — Compétition sans humiliation : cohortes comparables d'abord (« Ma classe »,
  ligue par centile), aucun affichage public d'échec, pas de vocabulaire de relégation.
  L'exclusion anti-triche reste silencieuse (é22 R-26).
- **R-6** — Fin de session propre : objectif du jour atteint = célébration de **fin**
  (« à demain ! ») ; jamais d'enchaînement automatique vers « encore un » depuis cette
  célébration.
- **R-7** — Transparence parents : tout ce que l'élève voit de son engagement (série,
  missions, temps) est lisible côté parent via les surfaces existantes ; aucun mécanisme
  n'est conçu pour échapper au regard parental.
- **R-8** — Vocabulaire : aucune surface ne dit « premium/abonnement/payant » (phase
  gratuite) ni ne culpabilise (« tu as échoué », « tu as abandonné » interdits ; on dit
  « ta série t'attend », « reprends où tu en étais »).

**Règles de fonctionnement :**

- **R-9** — Missions du jour : 3 par jour, tirées d'un pool typé, **déterministes par
  (élève, date)** — pas de hasard serveur, testable et stable au re-chargement. Le pool est
  **filtré par éligibilité réelle** (pas de mission donjon sous niveau 1 ou sans accès, pas
  de mission duel sans parcours actif, pas de mission « révision » sans révision due) ; la
  première mission est toujours du type socle `3_exercises`-like, faisable par tous.
- **R-10** — Types de missions v1 (8) : `exercises_n` (socle), `review_due` (finir la
  Révision du jour), `subject_focus` (2 exercices dans une matière du parcours),
  `score_90` (un exercice ≥ 90 %), `recall_one` (un rappel actif — si éligible),
  `dungeon_floors` (5 étages — si accès), `duel_play` (jouer un duel — si disponible),
  `chapter_step` (avancer le chapitre en cours — se nourrit de `resolveNextAction`).
- **R-11** — Enveloppe de récompense du jour **constante** : la somme distribuable par les
  missions quotidiennes reste celle d'aujourd'hui (50 XP / 10 pièces) répartie sur les
  3 missions (15/3 chacune) + bonus de complétion (5/1). Toute autre valeur = §3.9 (é09).
- **R-12** — Anneau du jour : progression = **XP réellement gagné aujourd'hui** (UTC métier
  identique à `award_xp`) sur `daily_xp_goal` choisi ∈ {50, 100, 200} (défaut 100 — la
  valeur é22 R-28). Le choix vit dans `/parametrage`, modifiable 1 fois/jour.
- **R-13** — Badges : **tout badge présent en base est décernable** ; tout badge non
  décernable est retiré de la base (v1 : `night_owl` — récompenser la pratique nocturne
  d'un mineur contredit R-4/annexe §D, et aucune ligne `student_badges` ne le référence).
  Chaque badge affiche sa condition en clair dans la collection (é22 R-30). Les familles
  v1 : `debut`, `serie`, `maitrise`, `arene`, `saison`.
- **R-14** — Le badge de ligue (`league_podium`, famille `saison`) est décerné par la
  clôture hebdo existante (`award_duel_league_week`) aux paliers or/platine/diamant —
  jamais retiré, jamais dégradé.
- **R-15** — Classement « Cette semaine » : XP de la semaine ISO en cours (fuseau Tunis,
  même horloge que la ligue — `app_current_week_start()`), mêmes cohortes que l'existant
  (global / Ma classe / matière), même anti-fuite (aucun `user_id` tiers). Le cumulatif
  reste. L'onglet par défaut : « Cette semaine » (Q-3, arbitrée le 2026-09-01).
- **R-16** — Notifications nouvelles, audiences exactes :
  `streak-lost` — série ≥ 3 perdue avant-hier (fenêtre de rachat encore ouverte), une fois ;
  `league-result` — lundi, tout participant de la semaine close (payload : palier + gain) ;
  `streak-milestone` — le soir où `current_streak` atteint 7, 30 ou 100 ;
  `comeback` — J+7 exact d'inactivité, une seule fois par période d'absence.
  Priorité du pipeline (1 seul push/jour) : `league-result` > `streak-lost` >
  `streak-at-risk` > `streak-milestone` > `tutor-daily-plan` > `comeback`.
- **R-17** — Toute notification est émise dans la **langue du profil** (`profiles.locale`,
  nouvelle colonne backfillée `fr`, écrite à chaque changement de langue in-app) ; les
  3 payloads existants sont migrés ; RTL respecté dans les textes AR.
- **R-18** — « Ta semaine » : carte déterministe calculée depuis les faits existants
  (`get_tutor_digest_inputs` fournit déjà semaine vs semaine-1), affichée lundi (et
  consultable toute la semaine), **aucune récompense attachée** (cohérent é11 R-11 : un
  bilan ne promet ni XP ni pièces).
- **R-19** — Accueil : la récompense de bienvenue est créditée **à la fin de l'onboarding**
  (une seule fois, idempotente) ; le CTA final mène à la première quête recommandée du
  parcours choisi (une seule action, pas un menu). Valeur des pièces : **30**
  (Q-4, arbitrée — un `booster_hint` exactement : la boutique s'apprend par l'usage).
- **R-20** — Conversion anonyme : bandeau sur l'écran de résultat anonyme uniquement
  (jamais bloquant, jamais de compte à rebours), formulé en gain futur (« crée ton compte
  pour garder tes prochains XP ») — la progression anonyme antérieure n'est pas migrée
  (hors périmètre v1).
- **R-21** — Événements : pilotés par table (`app_events`), fenêtres calendaires courtes
  (7-15 jours), au plus **un actif à la fois** ; un événement = un défi mesurable sur la
  fenêtre + un badge saisonnier famille `saison`, décerné à la complétion pendant la
  fenêtre, **jamais après, jamais retiré**. Le calendrier 2026-2027 (Q-2, arbitrée) :
  Rentrée (sept.) · Devoirs de synthèse (fin nov.) · Révisions de mai · Défi Ramadan
  (objectif réduit, ton calme).
- **R-22** — i18n : toute nouvelle chaîne naît FR/EN/AR (clés, pas de texte en dur — la
  leçon des push actuels), RTL vérifié sur les nouvelles surfaces ; `hero_class` cesse
  d'être du français stocké : la base garde un **code** (`s_rank`…), l'affichage passe par
  i18n (migration §3.1).

### 2.3 Hors périmètre v1 (tue le scope creep)

Différés (annexe §E, gated sur lot 1 + utilisateurs réels) : passe de saison, coffres
variables, graphe d'amis / duo-streak / kudos / présence, revanche & invitations de duel,
visage illustré d'El Ostedh (porte artistique, à articuler avec é19), rival narratif,
double-XP (économie é09), bonus « première victoire du jour », emails, A/B testing (é09 s'en
interdit aussi), migration de progression anonyme, admin UI des événements (v1 : seed par
migration).

## 3. Architecture technique (décisions fermées)

### 3.1 Modèle de données (migrations additives, ordre DoD §7)

```sql
-- 1) locale de notification (backfill fr, jamais NULL ensuite)
ALTER TABLE public.profiles
  ADD COLUMN locale text NOT NULL DEFAULT 'fr'
  CHECK (locale IN ('fr','en','ar'));

-- 2) objectif du jour choisi (R-12)
ALTER TABLE public.profiles
  ADD COLUMN daily_xp_goal integer NOT NULL DEFAULT 100
  CHECK (daily_xp_goal IN (50,100,200));

-- 3) familles de badges (R-13) + retrait du badge indécernable
ALTER TABLE public.badges ADD COLUMN family text;            -- backfill par UPDATE seed
DELETE FROM public.badges b WHERE b.code = 'night_owl'
  AND NOT EXISTS (SELECT 1 FROM public.student_badges sb WHERE sb.badge_id = b.id);

-- 4) événements calendaires (R-21) — lus par tous, écrits par migration seulement
CREATE TABLE public.app_events (
  id uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  code text UNIQUE NOT NULL,
  starts_at timestamptz NOT NULL,
  ends_at timestamptz NOT NULL CHECK (ends_at > starts_at),
  goal_type text NOT NULL CHECK (goal_type IN ('exercises_n','score_90_n')),
  goal_target integer NOT NULL CHECK (goal_target BETWEEN 1 AND 100),
  badge_code text REFERENCES public.badges(code),
  name jsonb NOT NULL, description jsonb NOT NULL          -- {fr,en,ar}
);
GRANT SELECT ON public.app_events TO anon, authenticated;   -- grants EXPLICITES (piège connu)
```

Pas de table de progression d'événement : la progression se calcule à la volée sur
`attempts` dans la fenêtre (volumes faibles, index existant par user) — **D-3**. Pas de
nouvelle table pour les missions : `daily_objectives` existe, la rotation est du code.

### 3.2 Server — RPC & fns

- `admin_engagement_overview()` — SQL `SECURITY DEFINER`, gardée `is_admin()`, `REVOKE`
  anon/authenticated, pattern exact de `admin_economy_overview` (é09 lot 1). Retourne un
  JSON : CURR par semaine (8 sem.), cohortes d'inscription hebdo × {D1,D7,D30}, DAU/WAU,
  distribution des séries (0 / 1-6 / 7-29 / 30+), opt-in push, **et KPI-E** (précision
  moyenne, chapitres complétés/actif). Actif = ≥ 1 ligne `attempts` **ou** `learning_pulses`
  sur la période, semaines ISO fuseau Tunis (même horloge que la ligue).
- `ensure_daily_weekly_goals` — étendue : génère les 3 missions du jour (R-9/R-10),
  sélection déterministe = hash md5(user_id ‖ date) modulo le pool éligible, socle en tête.
  L'incrément des nouveaux types se fait là où l'événement se produit déjà
  (`submit_exercise_attempt`, `finalize_dungeon_run`, `finalize_duel`) — le trigger de
  récompense existant (`credit_goal_reward`) ne change pas.
- `award_duel_league_week` — étendue : décerne `league_podium` (R-14) via
  `award_badge_if_new` ; la notification `league-result` lit `duel_league_awards` (aucune
  nouvelle table).
- `get_weekly_leaderboard(scope)` — calcul direct sur `attempts` de la semaine ISO
  (somme `xp_earned`), mêmes garde-fous anti-fuite que `get_grade_leaderboard`.
- `get_weekly_recap()` — server fn (`createServerFn` + `requireSupabaseAuth` + zod) qui
  agrège `get_tutor_digest_inputs` (existant) + badges/ligue de la semaine. Aucune écriture.
- `claim_welcome_pack()` — RPC idempotente (une ligne de garde par user), créditée via
  `award_coins` existant (R-19).
- Rallumage des badges (R-13) — chaque condition vit dans le finalizer qui possède déjà le
  fait : `streak_30`/`level_10`/`math_master`/`polyglot`/`math_blitz` dans
  `submit_exercise_attempt` (révision vivante — **se substitue par script**, jamais retapée),
  `boss_slayer` dans `finalize_dungeon_run`, `collector`/`rich_kid` dans
  `purchase_shop_item`. Conditions exactes par badge : tableau au lot 3.

### 3.3 Client

Aucune nouvelle route élève. Surfaces modifiées : `dashboard-goals` (3 missions),
`DashboardFocus`/`DailyRing` (anneau honnête + choix), `daily-review-panel` (inchangé),
`leaderboard.tsx` (onglet « Cette semaine »), `duel-league.tsx` (podium modal),
`dashboard-badges-shop` → collection complète (verrouillés + conditions + familles),
`quest-result-screen` (bandeau anonyme US-10), `onboarding` étape 2 (bienvenue),
`/parametrage` (objectif du jour), `/admin/engagement` (nouvelle route admin, pattern
`/admin/economie`). Feature owners : `dashboard`, `progression`, `duel`, `shop`, `auth`
(onboarding), pas de nouvelle feature — les frontières existantes suffisent.

### 3.4 Push (feature `notifications`)

`push-audience.ts` : passe de 3 audiences à 7, **pipeline de priorité unique** (R-16) qui
garantit ≤ 1 push/jour/élève by construction (l'exclusion croisée actuelle généralisée).
Payloads : dictionnaire i18n serveur indexé par `profiles.locale` (R-17) — plus aucun texte
en dur. Cadence : le cron quotidien 18:00 UTC existant sert tout, y compris `league-result`
le lundi (pas de second cron, pas de temps réel — assumé, D-2).

### 3.5 Sécurité & anti-triche

Rien ne change au contrat : clé de réponse jamais côté client, RPC privilégiées `REVOKE`d,
RLS sur toute nouvelle table (`app_events` : lecture seule publique, écriture par migration),
`admin_engagement_overview` inaccessible aux non-admins (test pgTAP), aucun `user_id` tiers
dans les nouveaux classements, rate-limit existant inchangé. Les missions étant
déterministes par (user, date), rejouer le tirage est impossible.

### 3.6 Intégrations & env

Aucune nouvelle variable d'env, aucun service nouveau. PostHog : la liste fermée
d'événements produit passe de 3 à ~12 (`signup`, `onboarding_completed`, `quest_completed`,
`level_up`, `badge_earned`, `daily_missions_completed`, `duel_finished`, `league_awarded`,
`shop_purchase`, `streak_recovered`, `push_optin`, `push_optout`) — **toujours zéro PII,
profils désactivés** : PostHog reste l'outil de **funnel**, la rétention par personne vient
de Postgres (D-1). `docs/environment-variables.md` : inchangé.

### 3.7 Observabilité

Logger structuré : le dispatcher push logge par tag (candidats, envoyés, échecs) ; le lot 1
ajoute un compteur d'événements produit par jour dans `/admin/engagement` (méta-mesure :
l'instrumentation elle-même est visible).

### 3.8 Décisions d'architecture

- **D-1 — La rétention se calcule dans Postgres, pas dans PostHog.** Alternative rejetée :
  activer les profils PostHog — refusé, la désactivation est une décision de protection des
  mineurs (pas de PII, pas de session replay) qu'on ne rouvre pas pour du confort d'outil.
- **D-2 — Un seul cron push par jour** (18:00 UTC existant), y compris pour le résultat de
  ligue (reçu le lundi soir). Alternative rejetée : push temps réel des duels/ligues —
  infra nouvelle, valeur marginale, risque de rafale (R-4).
- **D-3 — Pas de table `event_progress`** : calcul à la volée sur `attempts` dans la
  fenêtre. Alternative rejetée : matérialiser — volumes minuscules, une table de plus à
  sécuriser.
- **D-4 — Le tirage des missions est déterministe** (hash user‖date). Alternative rejetée :
  aléatoire serveur — non testable, non stable au rechargement, et le « hasard » n'apporte
  rien qu'une rotation quotidienne n'apporte déjà.
- **D-5 — `night_owl` est supprimé, pas réaffecté** (R-13). Alternative rejetée : le
  transformer en badge « lève-tôt » — c'est le même signal inversé ; aucun badge ne doit
  juger l'heure de pratique d'un enfant.
- **D-6 — Le classement hebdo est un onglet du leaderboard existant**, pas une page.
  Alternative rejetée : nouvelle route « Ligue XP » — P-7, zéro nouvelle surface.
- **D-7 — La carte « Ta semaine » est déterministe et sans récompense** (R-18). Alternative
  rejetée : la brancher sur les digests IA é11 — dépendance à une clé jamais branchée ;
  quand le pilote é29 Q-9 aura tourné, la prose d'El Ostedh pourra **enrichir** la carte,
  jamais la conditionner.

### 3.9 Registre économie (é22 R-28 → é09)

Toute valeur touchée par é31, pour arbitrage é09 (la console `/admin/economie` mesure
avant/après) : répartition 15/3 ×3 + 5/1 (R-11, enveloppe constante) · pièces de bienvenue : 30
(Q-4, arbitrée) · prix des cadres/titres (lot 7, grille à proposer par l'exécuteur dans la
fourchette des skins existants 80-500) · aucun multiplicateur, aucun coffre. Le coût du
rachat de série (15) et du gel (250) ne bougent pas ici — c'est l'arbitrage A16 de é09.

## 4. Plan d'exécution en lots

Chaque lot = une PR mergeable, gate verte, utile seul. L'ordre est l'ordre de valeur ; seuls
liens durs : lot 2 avant 4 et 5 (familles de badges), lot 3 avant 6 (les missions sont la
« raison de revenir demain » de l'accueil).

| lot | contenu (résumé)                                                                                                        | fichiers/objets créés                                                                                            | tests exigés                                                                                            | dépend de         |
| --- | ----------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ----------------- |
| 1   | Mesurer : `admin_engagement_overview` + `/admin/engagement` + 12 événements produit + CURR dans la scorecard            | migration RPC, `admin.engagement.tsx`, `engagement.server.ts`, `product-analytics.ts` étendu                     | pgTAP (cohortes synthétiques → CURR/D7 exacts, accès refusé non-admin), Vitest (mapping events)         | —                 |
| 2   | Badges vivants : 8 rallumés, `night_owl` retiré, familles, collection visible avec conditions, célébrations hors quête  | migrations (badges.family, seeds, finalizers), `badge-collection.tsx`                                            | pgTAP (chaque condition décerne, idempotence), Vitest (collection verrouillé/déverrouillé)              | —                 |
| 3   | Le jour : 3 missions rotatives filtrées, anneau honnête + objectif choisi, fin de session célébrée, fix bannière rachat | migration `ensure_daily_weekly_goals` + `daily_xp_goal`, `dashboard-goals`, `DailyRing`, `/parametrage`          | Vitest (tirage déterministe, filtres d'éligibilité, anneau = XP réel), pgTAP (enveloppe R-11 constante) | —                 |
| 4   | Le canal : `profiles.locale`, payloads i18n, 4 audiences nouvelles, pipeline de priorité ≤ 1/jour                       | migration locale, `push-audience.ts`, `notifications.cron.server.ts`                                             | Vitest (priorité, unicité/jour, i18n complet 3 langues, audiences SQL simulées), pgTAP (audiences)      | 2 (jalon = badge) |
| 5   | La semaine : podium de ligue célébré + badge `league_podium`, onglet « Cette semaine », carte « Ta semaine »            | migration `get_weekly_leaderboard` + award étendu, `duel-league.tsx`, `leaderboard.tsx`, `weekly-recap-card.tsx` | pgTAP (classement hebdo exact, badge podium), Vitest (recap = faits), e2e existant non cassé            | 2                 |
| 6   | L'accueil : bienvenue idempotente + première quête à un tap + bandeau anonyme                                           | migration `claim_welcome_pack`, `onboarding` étape 2, `quest-result-screen`                                      | pgTAP (idempotence du pack), Vitest (CTA unique, bandeau anonyme seulement)                             | 3                 |
| 7   | L'identité : `avatar_tier` rendu, `hero_class` en code + i18n, cadres/titres en boutique                                | migration hero_class code + items, `hero-avatar.tsx`, boutique                                                   | Vitest (mapping tier/rendu, i18n 3 langues), pgTAP (migration hero_class sans perte)                    | —                 |
| 8   | Le calendrier : table `app_events` + bannière + défi + badge saisonnier + événement pilote                              | migrations (table + seed pilote), `event-banner.tsx`                                                             | pgTAP (fenêtres, badge dans la fenêtre seulement), Vitest (bannière : un actif max)                     | 2                 |

Détail par lot — périmètre exact, critères d'acceptation (US/R mappées), et stop-points :

- [ ] **Lot 1 — Mesurer d'abord.** US-13, R-1, KPI-A/B/E. Publier la CURR dans la scorecard
      STATUS §1bis fait partie du lot (le chiffre, même s'il est « n=0 », avec sa date).
      **Stop-point** : aucun événement PostHog au-delà de la liste fermée §3.6 ; ne pas
      toucher à la config PostHog (profils restent désactivés, D-1).
- [ ] **Lot 2 — Badges vivants.** US-3, R-13. Tableau des conditions exactes à écrire en
      tête de PR (proposition : `streak_30` série ≥ 30 · `level_10` niveau ≥ 10 ·
      `boss_slayer` 10 étages cumulés · `math_master` 10 exercices maths ≥ 80 % ·
      `polyglot` 3 matières de langues pratiquées · `math_blitz` rang boss `critical` en
      maths · `collector` 5 objets possédés · `rich_kid` 500 pièces atteintes).
      **Stop-point** : aucun NOUVEAU badge hors `league_podium` (lot 5) et badges
      d'événement (lot 8) ; ne pas toucher aux XP/pièces.
- [ ] **Lot 3 — Le jour.** US-1/2/4(bannière), R-9…R-12, R-6. **Stop-point** : ne pas
      modifier `credit_goal_reward` ni les valeurs hebdo ; la sémantique exacte de la
      fenêtre de rachat (`recoverStreak` à J+2) se **vérifie dans le code avant** de
      corriger la bannière — si elle diverge de l'attendu, STOP et remonter (contrat
      exécuteur).
- [ ] **Lot 4 — Le canal.** US-5, R-4, R-16, R-17. **Stop-point** : pas de second cron, pas
      de push marketing/génériques ; si l'audience `comeback` ne peut pas garantir « une
      seule fois par absence » avec les colonnes existantes, proposer la colonne d'état en
      PR (additive) plutôt que d'élargir la fenêtre.
- [ ] **Lot 5 — La semaine.** US-6/7/8, R-14, R-15, R-18 — Q-3 arbitrée : hebdo par défaut. **Stop-point** :
      ne pas modifier le barème de pièces de la ligue (é09) ; la carte « Ta semaine » ne
      promet aucune récompense (R-18).
- [ ] **Lot 6 — L'accueil.** US-9/10, R-19, R-20 — Q-4 arbitrée : 30 pièces. **Stop-point** : pas
      de diagnostic d'entrée (le bilan adaptatif est é30 lots 5-9, différé) ; pas de
      migration de progression anonyme.
- [ ] **Lot 7 — L'identité.** US-11, R-22. **Stop-point** : prix des nouveaux items
      proposés en PR et enregistrés au §3.9, pas de refonte de la boutique.
- [ ] **Lot 8 — Le calendrier.** US-12, R-21 — Q-2 arbitrée : 4 événements. **Stop-point** : pas
      d'admin UI d'événements ; un seul événement seedé (le pilote) ; aucun contenu
      pédagogique conditionné à la fenêtre (R-2).

## 5. Stratégie de test

- **Vitest co-localisés** (feature `__tests__/`) : tirage déterministe des missions
  (mêmes (user, date) ⇒ mêmes missions ; pools filtrés par éligibilité), pipeline de
  priorité push (jamais 2 tags/jour ; chaque audience dans les 3 langues — un test qui
  échoue si une clé i18n manque, sur le modèle de `auth-refusals.test.ts`), anneau = XP du
  jour, recap = faits d'entrée, bandeau anonyme jamais rendu connecté.
- **pgTAP** (toute logique SQL — c'est le gros de l'étude) : `admin_engagement_overview`
  sur cohortes synthétiques (valeurs CURR/D1/D7/D30 attendues exactes, refus non-admin),
  conditions de chaque badge + idempotence `award_badge_if_new`, enveloppe R-11 constante
  (la somme des récompenses des 3 missions + bonus = 50/10), `get_weekly_leaderboard`
  borné à la semaine ISO Tunis, `claim_welcome_pack` idempotente, fenêtres `app_events`
  (badge hors fenêtre refusé), grants explicites de toute nouvelle table (piège connu :
  pgTAP sur base vierge).
- **Non-régression** : `db:check-chain` (chaîne rejouable sur base vierge), suite existante
  intacte, `smoke:shell` sur les lots UI ; e2e Playwright existants non modifiés (E2E ≠
  gate, jamais vers la prod).
- **Données de test** : cohortes synthétiques en fixtures pgTAP datées relatives à
  `now()` (jamais de date en dur — leçon #934).

## 6. Risques & mitigations

- **RISK-1 — Concevoir de l'engagement pour zéro utilisateur** (probabilité certaine,
  impact fort). C'est le risque assumé au §1.4 : l'acquisition (KPI-1) est le goulot et
  n'est pas ici. Mitigation décidée : lot 1 en tête (la mesure préexiste aux mécaniques) ;
  lots 2-5 = dettes objectives du code (badges morts, missions figées, ligue muette), pas
  des paris sur un comportement ; lots 6-8 revalidés à la lumière des premières mesures
  (beta D3). L'étude ne s'exécute pas avant sa validation humaine et n'aggrave pas le WIP
  (é26 KPI-3 : ≤ 3 études en exécution).
- **RISK-2 — Sur-notification → opt-out massif** (moyenne, fort). Mitigation : R-4 (≤ 1/jour
  by construction, relance unique), KPI-D surveillé au lot 1, opt-out en un geste, textes
  El Ostedh jamais culpabilisants.
- **RISK-3 — Inflation économique** (moyenne, moyen). Mitigation : R-11 (enveloppe
  constante), §3.9 (registre é09), aucune nouvelle source hors registre ; A15/A16 restent
  la propriété de é09.
- **RISK-4 — La comparaison sociale démotive les plus faibles** (moyenne, fort — c'est le
  résultat Hanus & Fox, annexe §F.10). Mitigation : R-5, classement hebdo qui repart
  (chacun peut exister chaque semaine), cohorte « Ma classe » par défaut quand elle est
  peuplée, badges = compétence (annexe §F.11), jamais d'affichage d'échec.
- **RISK-5 — Feature fatigue** (faible, moyen — é26 P-7). Mitigation : zéro nouvelle route
  élève (D-6), tout s'insère dans les surfaces existantes, la liste « différé » est
  explicite (§2.3).
- **RISK-6 — Missions impossibles proposées** (faible, moyen). Mitigation : R-9 (filtrage
  serveur par éligibilité réelle), socle toujours faisable, tests dédiés.
- **RISK-7 — Non-conformité mineurs** (faible, fort). Mitigation : R-2/R-3/R-4 alignées sur
  les lignes directrices DSA (annexe §F.12) — push opt-in (déjà le cas), streak pardonnable
  sans culpabilisation, zéro autoplay, zéro hasard payé ; la revue de chaque lot vérifie
  ces règles comme des critères d'acceptation.

## 7. Questions ouvertes (pour l'humain)

Section **arbitrée le 2026-09-01** par Mohamed — c'est l'acte de validation de l'étude.
Les décisions, consignées ici et répercutées dans les règles :

- **Q-1 — Push et petites classes : opt-in pour tous.** L'activation explicite reste le
  seul filtre, quel que soit l'âge ; le guide parent le documente (R-4 amendée).
- **Q-2 — Calendrier 2026-2027 : les quatre événements.** Rentrée (sept.) · Devoirs de
  synthèse (fin nov.) · Révisions de mai · **Défi Ramadan** (objectif réduit, ton calme).
  Un seul actif à la fois (R-21) ; le pilote du lot 8 est l'événement le plus proche à la
  date d'exécution.
- **Q-3 — Classement par défaut : « Cette semaine ».** L'onglet hebdo devient le défaut,
  le cumulatif reste en second onglet (R-15 amendée).
- **Q-4 — Pièces de bienvenue : 30.** Un `booster_hint` exactement ; inscrite au registre
  économie §3.9 — é09 la mesure comme le reste.

## 8. Journal d'exécution

### 2026-09-03 — les huit lots, MERGÉS EN PRODUCTION (arena#949, `main` en `7bdbccd`)

Chaque lot = un commit, sa migration, ses assertions pgTAP et ses tests co-localisés.
`npm run verify` (3 854 tests), `build:check` et `smoke:shell` verts ; la suite pgTAP
complète — **96 fichiers, 1 363 assertions** — rejouée en local sur la chaîne entière
(`docs/agents/pgtap-en-local.md`, sans Docker).

| lot | livré                                                                                                                                     | pgTAP |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------- | ----- |
| 1   | `admin_engagement_overview` (CURR, cohortes D1/D7/D30, DAU/WAU, séries **effectives**, KPI-D, KPI-E) · `/admin/engagement` · 12 événements produit en liste fermée typée | 29    |
| 2   | 8 badges rallumés dans le finalizer qui possède le fait · `night_owl` retiré · familles NOT NULL · collection avec verrouillés et conditions | 20    |
| 3   | 3 missions/jour tirées d'un pool de 8 filtré par éligibilité · tirage déterministe · anneau sur l'XP réel · objectif choisi · fin de session  | 20    |
| 4   | `profiles.locale` · 6 audiences · pipeline de priorité (≤ 1/jour par structure) · textes FR/EN/AR · badge `league_podium`                    | 16    |
| 5   | classement « Cette semaine » par défaut · podium de ligue célébré · carte « Ta semaine »                                                     | 12    |
| 6   | `claim_welcome_pack` idempotente (30 pièces) · première quête à un tap · bandeau anonyme qui NOMME la perte                                  | 9     |
| 7   | `hero_class` en codes + i18n · `avatar_tier` rendu · cadres et titres (puits de pièces)                                                      | 13    |
| 8   | `app_events` · un seul actif par contrainte · badge saisonnier dans la fenêtre · bannière                                                    | 12    |

### Ce que l'exécution a appris — et qui ne se déduisait pas de l'étude

**1. Deux défauts que seul le harnais pgTAP LOCAL a vus, avant la CI.**

- Le corps d'`award_coins` a été substitué depuis sa révision vivante — en emportant un
  `GRANT … TO authenticated` que 20260606150000 avait **révoqué** : la faille S1, où un
  élève connecté pouvait s'auto-créditer des pièces. `CREATE OR REPLACE` ne touche pas aux
  privilèges, mais recopier le GRANT du fichier source la rouvrait en silence.
  `01_economy_grants` l'a montré. **Règle** : substituer un corps, c'est hériter de son
  fichier — pas de son ÉTAT de privilèges, qui a pu changer trois migrations plus loin.
- `award_duel_rewards` est un **second écrivain de `hero_class`** : il recopie la courbe de
  niveau d'`award_xp` (duplication antérieure à cette étude) et écrivait donc lui aussi du
  français. La contrainte du lot 7 faisait échouer **chaque récompense de duel**.
  `25_duel_forfeit` l'a montré en trois assertions rouges. Une assertion structurelle
  interdit désormais qu'un troisième écrivain réapparaisse.

**2. Trois écarts assumés au contrat**, chacun parce que la lettre de l'étude rendait la
règle inatteignable :

- **`push_consent_events`** (lot 1, hors §3.1) : US-13 demande « opt-in **et** opt-out ». Le
  second n'était comptable par AUCUNE colonne — `delete_push_subscription` supprime la ligne,
  donc « jamais abonné » et « parti » se ressemblaient. KPI-D, le garde-fou de R-4 contre
  RISK-2, était non mesurable par construction.
- **`daily_xp_day` / `daily_xp_base`** (lot 3, hors §3.1), tenues dans `award_xp` : R-12 exige
  l'XP RÉEL du jour, et aucune source ne le donne — `attempts` ignore l'XP du donjon, des
  duels et des objectifs, tous crédités par `award_xp` sans ligne de tentative. Reconstituer
  la somme ailleurs, c'était recopier quatre barèmes et s'engager à les faire diverger.
- **`get_weekly_recap` self-scopée** (lot 5) plutôt qu'un appel à `get_tutor_digest_inputs`
  (§3.2) : cette fonction-là est `service_role` et volontairement dépersonnalisée — son JSON
  part chez un fournisseur de modèle. L'appeler depuis une surface élève supposerait le client
  admin sur un écran de jeu.

**3. Le stop-point du lot 3, remonté plutôt que contourné.** La fenêtre de rachat de série
DIVERGE de ce que R-16 suppose (« série perdue avant-hier, fenêtre encore ouverte ») :
`streakRecoveryBlock` n'impose aucune borne haute, un élève parti depuis dix jours peut encore
racheter. Rien n'a été changé — le coût et la fenêtre du rachat sont l'arbitrage **A16 de
é09**. La bannière, elle, n'avait plus besoin de ce lot : arena#947 l'a rendue atteignable le
2026-09-02, la veille.

**4. Ce que la garantie « une seule fois par période d'absence » (R-16) n'a pas coûté.** Le
stop-point du lot 4 prévoyait une colonne d'état si la garantie n'était pas atteignable avec
l'existant. Elle l'est : **ancrer chaque audience sur un jour EXACT** (`last_active_date =
jour - 7`) la rend vraie un seul soir par absence. Une colonne de moins est une divergence de
moins.

**5. Deux budgets de bundle rouges, traités dans l'ordre que le dépôt prescrit.** Les libellés
de la collection de badges (13 × nom + condition × 3 langues) ne servent qu'à `/boutique`, une
route paresseuse : ils sont partis dans leur propre chunk (`i18n-badges`, 4,5 KB), sur le
mécanisme de `parent/`. Les deux cartes du tableau de bord sont passées en `lazy()`. Les
relèvements restants (i18n 184→188, dashboard 32→36) sont documentés à leur ligne, comme le
fichier de budgets l'exige.

**6. Un dernier défaut, trouvé par CodeQL sur la PR — et il était dans un test.** La regex
qui cherchait les appels `trackProductEvent(…)` pour vérifier qu'aucun ne joint de PII
(`/trackProductEvent\((?:[^()]|\{[^{}]*\})*\)/g`) a été signalée `js/redos` en HIGH : ses
quantificateurs imbriqués rétrogradent exponentiellement. Remplacée par un balayage qui compte
les parenthèses — linéaire, et **plus juste** : la version régulière ne savait pas lire un appel
dont un argument contient lui-même une parenthèse, donc elle en tronquait le texte et pouvait
manquer une propriété interdite. Le test exige désormais d'avoir trouvé au moins autant d'appels
que d'événements câblés : un balayage qui ne trouve rien ne peut plus passer à vide.

### Ce qui reste, et qui n'est pas du code

- **Relever la CURR en prod.** La scorecard STATUS §1bis attend un CHIFFRE DATÉ, pas un
  instrument. Il sortira `n = 0` tant que la ligne 1 (« zéro canal d'acquisition ») tient —
  c'est une lecture, pas un échec, et c'était le risque RISK-1 assumé dès le §1.4.
- **Déplacer ce dossier en `EtudeRealisé/`** — la PR est mergée, le geste reste à faire.
- **Les quatre écrans qui restent différés** (§2.3) le restent : passe de saison, coffres,
  graphe d'amis, A/B testing — gated sur les mesures du lot 1 et sur de vrais utilisateurs.
