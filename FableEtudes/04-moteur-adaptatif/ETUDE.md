# Étude 04 — Moteur adaptatif & diagnostic de misconceptions

> **Statut** : en exécution — phase A0 **livrée** (2026-07-06), **A1.1 livrée** (2026-07-20, #581),
> **A1.2 spécifiée** (§9, 2026-07-25) et exécutable ; A2 derrière le seuil de données de Q-1
> **Priorité** : 04 · **Valeur** : le différenciateur défendable — chaque distracteur du contenu encode déjà une erreur nommée (protocole « erreur exécutée ») ; personne n'exploite ce signal. Diagnostic par élève → révision/remédiation personnalisées → progression mesurable (l'argument de vente parents) · **Complexité** : haute
> **Architecte** : Fable (claude-fable-5), 2026-07-04 · **Exécuteur cible** : Sonnet
> **Dépend de** : volume d'usage (la télémétrie A0 doit tourner quelques semaines avant A2) ; le tagging de contenu (pipeline) monte en charge progressivement
> **Docs normatifs liés** : CLAUDE.md (gamification centralisée, anti-farm, gotcha grants), `content-engine/references/expert-exercises.md` (taxonomies de pièges — la matière première), ARCHITECTURE.md

## 1. Contexte & objectif produit

L'app sait _si_ l'élève a raté, pas _pourquoi_. Or le contenu d3–4 est construit pour que chaque
distracteur soit **l'exécution d'une erreur précise** (les taxonomies des prof-\*) : choisir le
distracteur « 0,45 > 0,5 » diagnostique « compare les décimaux par longueur d'écriture ». La table
`spaced_repetition_schedule` (SM-2) existe mais n'alimente aucune expérience visible (seul le
dashboard l'effleure). Objectif en trois marches : **A0** tracer le choix par question ; **A1**
transformer SM-2 en « Révision du jour » jouable ; **A2** profil de misconceptions + remédiation
recommandée. KPI : complétion de la révision du jour, delta de réussite sur notions remédiées,
rétention hebdo. Non-objectif (v1) : génération dynamique d'exercices (A3, gelé), IA générative,
crédit partiel.

## 2. Spécification fonctionnelle

- **US-1 (A1)** : chaque jour, je vois « Révision du jour » : 1–3 exercices existants recommandés
  (notions dues SM-2 + faiblesses récentes), avec la raison (« Tu n'as pas revu _Fractions_ depuis
  12 jours »). Les récompenses standard s'appliquent (règles anti-farm inchangées).
- **US-2 (A2)** : dans ma progression, un panneau « Tes points faibles » : jusqu'à 5 misconceptions
  actives, en langage élève (« Tu additionnes les dénominateurs »), chacune avec un bouton
  « S'entraîner » → l'exercice de remédiation du chapitre concerné.
- **US-3 (A2)** : le rapport parent inclut les 3 points faibles majeurs + tendance.
- **R-1** : la télémétrie n'enregistre que (question, option choisie, correct, contexte session) —
  jamais la clé ; aucune donnée nouvelle exposée au client hors agrégats de l'élève lui-même.
- **R-2** : une misconception est « active » à partir de **3 occurrences du même tag sur ≥2
  sessions dans les 30 derniers jours** (constantes centralisées, ajustables).
- **R-3** : la recommandation ne propose QUE des exercices accessibles à l'élève (gate premium
  `resolve_exercise_access` respecté ; sinon repli sur un exercice d1–2 du même chapitre).
- **R-4** : « Révision du jour » plafonnée (3 exercices) et sans nouveau type de récompense —
  c'est un _sélecteur_, pas une nouvelle économie.
- **R-5** : tags de misconception **namespacés par matière** (`math.frac.add-denominators`) et
  centralisés dans un registre versionné du pipeline contenu (pas de texte libre).
- **i18n** : libellés élève des tags en FR/EN/AR dans le registre (le tag est un id, jamais affiché).
- **Hors périmètre (v1)** : A3 (assemblage dynamique de missions à partir de questions
  individuelles — étude séparée quand A2 aura des données), notifications push de rappel (le cron
  notifications existant peut s'y brancher plus tard). La **maîtrise par compétence** (profil
  fractions/équations/géométrie, prérequis, BKT-allégé) et les modèles avancés (IRT/ML, gate de
  volume) sont l'**étude 07** — cette étude-ci reste le socle télémétrie + heuristique ; le lot
  A1.1 devient compétence-aware via le lot 5 de l'étude 07.

## 3. Architecture technique (décisions fermées)

- **D-1 — Les tags vivent côté serveur uniquement.** Si on taggait `options` JSONB (envoyé au
  client), l'option correcte serait la seule sans tag → **fuite de la clé**. Donc : nouvelle
  colonne `questions.distractor_tags JSONB` (`{"b":"math.frac.add-denominators", …}`), posture
  `correct_option` : jamais sélectionnée par une requête client. Rejeté : tagger dans `options`.
- **D-2 — Télémétrie append-only alimentée par le RPC existant.** `submit_exercise_attempt`
  (et `submit_dungeon_answer`) insèrent dans `question_attempts` dans la même transaction —
  extension additive du RPC, pas de nouveau round-trip client. Rejeté : événement côté client
  (falsifiable, incomplet).
- **D-3 — Recommandation = sélection d'exercices existants** (comme D-1 de l'étude 02) : aucun
  nouveau mode de session. L'algorithme est une fonction SQL lisible, pas du ML : score de
  priorité = retard SM-2 normalisé + poids misconceptions actives du chapitre + malus « déjà
  recommandé hier ». Rejeté v1 : bandit/ML (pas de données), génération dynamique (A3).
- **D-4 — Le tagging du contenu est progressif et outillé** : champ optionnel `misconceptionTag`
  par option dans les fichiers `content/` (schema zod additif) ; `sql-builder` route les tags vers
  `distractor_tags` (et les **retire** de `options`) ; registre `content/misconceptions.json`
  (id → libellés FR/EN/AR + matière) validé par `content:qa` (tag inconnu = erreur). Les skills
  prof-\* taguent naturellement (leurs tableaux de pièges = le registre) ; le stock existant est
  taggé par vagues via `content-audit`.

**Modèle de données** (migrations additives + GRANTs — gotcha CLAUDE.md) :

```sql
ALTER TABLE public.questions ADD COLUMN IF NOT EXISTS distractor_tags JSONB; -- server-only (R-1/D-1)
CREATE TABLE public.question_attempts (
  id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  user_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
  question_id UUID NOT NULL REFERENCES public.questions(id) ON DELETE CASCADE,
  chapter_id UUID NOT NULL,                -- dénormalisé pour l'agrégation
  choice TEXT NOT NULL, is_correct BOOLEAN NOT NULL,
  misconception_tag TEXT,                  -- résolu à l'insert depuis distractor_tags[choice]
  source TEXT NOT NULL CHECK (source IN ('exercise','quiz','dungeon','exam')),
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
-- RLS: owner SELECT (agrégats via RPC), admin ALL; INSERT uniquement via les RPCs SECURITY DEFINER.
-- Index: (user_id, created_at DESC), (user_id, misconception_tag) WHERE misconception_tag IS NOT NULL.
-- Rétention: purge >12 mois par le cron (job dédié) — la matière première reste les agrégats.
CREATE TABLE public.user_misconceptions ( -- agrégat entretenu à l'insert (trigger léger) — évite le scan
  user_id UUID NOT NULL, tag TEXT NOT NULL, occurrences INT NOT NULL DEFAULT 0,
  last_seen_at TIMESTAMPTZ NOT NULL, sessions_seen INT NOT NULL DEFAULT 0,
  PRIMARY KEY (user_id, tag)
);
```

**Server** : RPC `get_daily_plan()` (D-3 : retourne ≤3 exercice_ids + raisons, R-3/R-4) ;
RPC `get_my_weaknesses()` (tags actifs R-2 + libellés côté fn via le registre embarqué au build) ;
extension de `submit_exercise_attempt`/`submit_dungeon_answer` (D-2 — migration qui remplace les
fonctions, pgTAP de régression sur les récompenses) ; server fns zod dans
`src/features/progression/` (feature existante — la révision/faiblesses sont de la progression ;
pas de nouvelle feature). Rapport parent : extension de `parent-report` (US-3) via `shared/`.

**Client** : panneau « Révision du jour » sur le dashboard (composant dans `progression/`,
consommé par la route dashboard — via barrel public), panneau « Points faibles » dans la page
progression, extension du rapport parent. États vides soignés (« Rien à réviser, continue ! »).

**Observabilité** : logs agrégés d'insertion refusée / tag inconnu ; compteur plan-servi/plan-joué.

## 4. Plan d'exécution en lots

| lot   | contenu                                                                                               | tests exigés                                     | dépend de            |
| ----- | ----------------------------------------------------------------------------------------------------- | ------------------------------------------------ | -------------------- |
| A0.1  | Migration : `distractor_tags`, `question_attempts`, `user_misconceptions` (+RLS/grants/index/trigger) | pgTAP (RLS, trigger d'agrégat, R-1)              | —                    |
| A0.2  | Extension des 2 RPCs de soumission (D-2) + purge cron                                                 | pgTAP régression récompenses + insert télémétrie | A0.1                 |
| A0.3  | Pipeline : `misconceptionTag` (zod) + registre + routage sql-builder (D-4) + lint QA                  | Vitest schema/sql-builder ; content:check/qa     | A0.1                 |
| A1.1  | RPC `get_daily_plan` + fn + panneau « Révision du jour » (US-1, R-3/R-4)                              | pgTAP (sélection, gate premium) ; Vitest UI      | A0.2                 |
| A1.2a | Serveur : `get_attempt_review` rend l'erreur nommée + le chapitre (§9, D-A1.2-2)                      | pgTAP (non-fuite de la clé, dégradation à vide)  | A0.3                 |
| A1.2b | Client : bloc de correction riche dans la revue de fin de quête (§9, US-4)                            | Vitest UI + i18n FR/EN/AR ; e2e authed           | A1.2a                |
| A2.1  | RPC `get_my_weaknesses` (R-2) + panneau « Points faibles » (US-2)                                     | pgTAP (seuils R-2) ; Vitest UI + i18n libellés   | A0.2, A0.3 + données |
| A2.2  | Rapport parent enrichi (US-3)                                                                         | Vitest                                           | A2.1                 |

- [x] A0.1 — schéma télémétrie (merge seul — DoD §7)
- [x] A0.2 — capture (RPCs) + purge
- [x] A0.3 — pipeline tags + registre
- [x] A1.1 — révision du jour (PR #581 ; rendue compétence-aware par é07 lot 5, PR #616/#617)
- [ ] A1.2a — serveur : l'erreur nommée dans la correction (§9)
- [ ] A1.2b — client : le bloc de correction riche (§9)
- [ ] A2.1 — points faibles (GO humain : ≥4 semaines de télémétrie ou seuil de volume)
- [ ] A2.2 — rapport parent

**Stop-points** : A0.2 ne change AUCUN barème/gate de récompense (pgTAP de régression obligatoire
avant merge) ; les tags ne transitent jamais dans `options` (D-1) ; **A1.2a ne rend jamais que le
tag de l'option CHOISIE** (§9, RISK-A1.2-A) ; A2.1 attend le GO humain ; le tagging de masse du
stock existant est un chantier CONTENU (content-audit), pas un lot code.

## 5. Stratégie de test

pgTAP porte le risque : régression complète de `submit_exercise_attempt` (barèmes, anti-farm,
potions/shields — la matrice existante doit rester verte), trigger d'agrégat, seuils R-2, gate
R-3. Vitest : fns zod, panneaux (états vides/pleins, RTL). E2E authed : un cycle
« rater 3× le même tag → le point faible apparaît → l'exercice recommandé se lance » sur TEST.

## 6. Risques & mitigations

- **RISK-1** Régression du RPC de soumission (rare/critique) → lots A0.2 minuscule + pgTAP de
  régression exhaustif + `content-audit`/nightly en filet.
- **RISK-2** Fuite de clé via les tags (rare/critique) → D-1 (colonne server-only) + test pgTAP
  « distractor_tags jamais lisible par authenticated via les vues/requêtes client ».
- **RISK-3** Tags de mauvaise qualité → registre fermé (R-5) + lint + montée progressive (D-4) ;
  une misconception mal libellée se corrige dans le registre sans toucher aux données.
- **RISK-4** Reco perçue comme punitive (possible/moyen) → ton RPG des libellés, plafond R-4,
  états vides positifs ; mesurer plan-servi/plan-joué.
- **RISK-5** Volume `question_attempts` (long terme/faible) → append-only + index partiels +
  purge 12 mois + agrégat `user_misconceptions`.

## 7. Questions ouvertes (pour l'humain)

- **Q-1** : GO A2 — seuil de données jugé suffisant (proposition : 4 semaines OU 50k lignes).
- **Q-2** : les faiblesses sont-elles visibles par le parent par défaut (US-3) ou opt-in élève ?
- **Q-3** : politique de rétention télémétrie (proposition 12 mois) — conformité vie privée mineurs.

## 8. Journal d'exécution

- **2026-07-06 — A0.1 livré** (migration `20260706120000_adaptive_telemetry_a0_schema.sql` +
  pgTAP `19_adaptive_telemetry_a0.test.sql`, 20 assertions — suite 210/210 sur base vierge).
  `questions.distractor_tags` (server-only, posture whitelist de colonnes intacte, R-1 testé),
  `question_attempts` (append-only, RLS owner-SELECT + `is_admin()`, zéro grant d'écriture
  client), `user_misconceptions` + trigger d'agrégat.
  **Écart accepté n°1** : ajout de `session_id UUID NOT NULL` à `question_attempts` — le bloc SQL
  de l'étude l'omet, mais R-1 impose le « contexte session » et R-2/`sessions_seen` exigent de
  distinguer les sessions (id polymorphe : `exercise_sessions.id` ou `dungeon_runs.id` selon
  `source`, sans FK). L'index partiel de l'étude est étendu à
  `(user_id, misconception_tag, session_id)` pour servir la recherche du trigger.
  **Écart accepté n°2** : le trigger compare `qa.id < NEW.id` (et non `<>`) — un trigger AFTER
  ROW sur un INSERT multi-lignes voit toutes les lignes du statement ; avec `<>`, deux
  occurrences du même tag dans le même batch s'annuleraient (bug détecté par le pgTAP,
  `sessions_seen` aurait sous-compté). Capture RPC : lot A0.2.
- **2026-07-06 — A0.2 livré** (migration `20260706130000_adaptive_telemetry_a0_capture.sql` +
  pgTAP `20_adaptive_telemetry_a0_capture.test.sql`, 15 assertions — suite 225/225, matrice de
  régression récompenses (tests 04/07) inchangée et verte contre les nouvelles définitions).
  `submit_exercise_attempt` et `submit_dungeon_answer` re-créés **verbatim** avec le seul ajout
  de l'INSERT télémétrie dans la même transaction (D-2) : tag résolu server-side depuis
  `distractor_tags->>choice` (R-1), source `exercise`/`quiz` selon le mode, `dungeon` pour le
  donjon (session = run id). `purge_question_attempts()` (rétention 12 mois — Q-3, les agrégats
  survivent) planifiée quotidiennement via pg_cron (wrapper défensif du repo).
  **Écart accepté n°3** : les questions non répondues ne produisent PAS de ligne de télémétrie
  (aucune option choisie à diagnostiquer — le scoring, lui, continue de les compter fausses,
  inchangé). La source `exam` du CHECK reste réservée à l'étude 02.
- **2026-07-06 — A0.3 livré** (pipeline contenu, pas de migration — la colonne `distractor_tags`
  a atterri en A0.1). Champ optionnel `misconceptionTag` par option (zod, mcq uniquement — voir
  écart n°4) ; `sql-builder` route les tags vers `distractor_tags` (keyé par id d'option) et les
  **retire** de `options` (R-1 — prouvé bout-en-bout : la colonne `options` en base ne contient
  que `{id,text}`, `distractor_tags` porte la map) ; registre versionné `content/misconceptions.json`
  (id namespacé par matière → libellés FR/EN/AR + matière), validé structurellement par
  `content:check` (loader) et croisé par `content:qa` (tag utilisé mais non déclaré = erreur).
  Invariant D-1 durci au schéma : une option **correcte** ne peut pas porter de tag. Tests :
  `content-pipeline-a0.test.ts` (schéma + registre + routage/strip sql-builder + loader) et
  ajouts à `qa-checks.test.ts` (`auditMisconceptionTags`). Gate verte (1062 tests),
  `content:check` (73 sujets) + `content:qa:strict` (0 erreur) verts.
  **Écart accepté n°4** : `misconceptionTag` est autorisé **uniquement sur les options mcq** (le
  seul type où le `choice` de fil = l'id d'option, donc où `distractor_tags->>choice` résout la
  télémétrie — cf. exemple D-1). Les distracteurs multi/ordering/matching ne sont pas tagables
  (leur `choice` est un CSV, la résolution par id ne s'applique pas) — conforme au périmètre QCM
  du protocole « erreur exécutée ». Registre seedé avec 5 misconceptions math canoniques ; le
  tagging de masse du stock reste un chantier CONTENU (`content-audit`), pas un lot code.

## 9. Amendement A1.2 — « la correction riche à l'échec » (architecte, 2026-07-25)

> **Origine** : arbitrage A1-Q4 de l'étude 26 (2026-07-20) — la « correction riche à l'échec »
> est **rattachée à cette étude** en nouvelle phase A1.2, entre A1.1 (livrée) et A2.
> **Mandat reçu** (ROADMAP §3 ligne 8) : feedback in-session · lien « revoir le cours » par
> erreur · misconception affichée · explication post-erreur **non monnayée**.
> **Statut** : contrat fermé, exécutable. Deux lots (A1.2a serveur, A1.2b client).

### 9.1 L'état réel, vérifié dans le code (pas ce que le mandat suppose)

Le mandat est écrit comme s'il fallait tout construire. Vérification faite le 2026-07-25, deux
de ses quatre points **sont déjà vrais**, et le dire évite de re-livrer de l'existant :

| Point du mandat                      | État réel                                                                                                                                                                                                                                                                                                          |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Explication post-erreur non monnayée | **Déjà vrai.** La correction de fin de quête vient de `get_attempt_review` (SECURITY DEFINER, owner-only, session complétée), qui rend `explanation` **sans aucune contrepartie**. Ce qui est monnayé, c'est l'indice **avant** de répondre (`consume_hint`, consommable) — un objet différent, qui reste tel quel |
| Misconception affichée               | **Absente.** `get_attempt_review` rend `(question_id, prompt, correct_option, explanation, is_correct)` — pas le tag. Le signal que toute la phase A0 collecte depuis le 2026-07-06 n'est affiché **nulle part** dans la correction                                                                                |
| Lien « revoir le cours » par erreur  | **Absent.** `quest-review-list` n'a aucun lien vers le cours du chapitre                                                                                                                                                                                                                                           |
| Feedback in-session                  | **Impossible sans casser une couture critique** — voir D-A1.2-1 et Q-4                                                                                                                                                                                                                                             |

**Conséquence de cadrage** : A1.2 n'invente pas une économie ni un écran. Il **branche le
diagnostic déjà capté** sur la surface de correction qui existe déjà. C'est la troisième des
« boucles collectées-jamais-surfacées » de l'étude 26 qui se referme.

### 9.2 Spécification fonctionnelle

- **US-4** : quand je me trompe, la correction de fin de quête ne me dit plus seulement « la bonne
  réponse était B ». Pour **chaque erreur**, elle nomme ce que j'ai fait (« Tu as additionné les
  dénominateurs »), me donne l'explication, et m'offre deux gestes : **revoir le cours** à
  l'endroit concerné, **m'entraîner** sur ce point.
- **R-A1.2-1** : le libellé de l'erreur vient du registre `content/misconceptions.json`, dans la
  langue de l'interface (FR/EN/AR). Le **tag n'est jamais affiché** — c'est un id.
- **R-A1.2-2** : le bloc riche n'apparaît que sur les réponses **fausses**. Une bonne réponse
  garde la correction sobre d'aujourd'hui : ne pas transformer une réussite en leçon.
- **R-A1.2-3** : **dégradation silencieuse et totale.** Question non taguée (l'immense majorité
  du corpus tant que le lot é07-3 / C4 n'a pas tourné), tag absent du registre, chapitre sans
  cours : le bloc se réduit à ce qu'il sait dire, sans trou visuel ni message d'erreur. Le
  comportement d'aujourd'hui est le **plancher** — jamais une régression.
- **R-A1.2-4** : aucune récompense, aucun compteur, aucun anti-farm touché. A1.2 est un
  **affichage**, comme A1.1 était un sélecteur.
- **R-A1.2-5** : les **quiz de compréhension gardent zéro correction** (garde anti-mémorisation
  de `get_attempt_review`, inchangée). L'enrichissement ne s'applique qu'aux modes
  pratique/boss/rappel.
- **R-A1.2-6** : le geste « m'entraîner » **réutilise** l'action livrée par é07 lot 4 (#588) — on
  ne crée pas un second chemin de remédiation.

### 9.3 Décisions d'architecture (fermées)

- **D-A1.2-1 — La correction reste POST-SOUMISSION, pas par question.** `submitAttempt` reçoit
  **toutes** les réponses en un appel et le RPC atomique calcule score, récompenses, anti-farm,
  SM-2 et télémétrie **dans une seule transaction**. Un feedback par question exigerait de
  scinder cette couture — c'est-à-dire de rouvrir la surface anti-triche et le barème, le
  contraire d'un lot d'affichage. « In-session » est donc rendu comme **« immédiatement à la fin
  de la session, sur l'item raté »**, ce qui préserve l'intention pédagogique (l'élève voit son
  erreur nommée pendant qu'il l'a encore en tête) pour une fraction du risque. Un vrai mode
  question-par-question est une **décision produit distincte** → Q-4. _Rejeté_ : soumettre chaque
  question au fil de l'eau (multiplie les round-trips, ouvre le rejeu, et rend l'anti-farm
  attaquable réponse par réponse).
- **D-A1.2-2 — Le serveur ne rend que le tag de l'option CHOISIE.** `get_attempt_review` gagne
  `misconception_tag TEXT` (et `chapter_id UUID`), résolus server-side par
  `distractor_tags ->> <choix de l'élève>`. Rendre la **map** `distractor_tags` serait une
  **fuite de la clé** : l'option correcte est la seule sans tag (D-1), donc la map désigne la
  bonne réponse par élimination. Le pgTAP doit encoder cette attaque, pas seulement le cas
  nominal. _Rejeté_ : exposer `distractor_tags` au client et résoudre côté UI.
- **D-A1.2-3 — Les libellés sont embarqués au build, pas lus en base.** Le registre est un
  fichier du dépôt de contenu, déjà compilé côté client pour d'autres surfaces ; la fonction SQL
  rend l'**id**, l'UI rend le **libellé**. Une misconception mal formulée se corrige alors dans
  le registre sans migration ni retouche de données (RISK-3, inchangé).
- **D-A1.2-4 — « Revoir le cours » vise le chapitre, l'ancre est optionnelle.** Le lien pointe la
  route de cours du `chapter_id` rendu par le RPC. Le registre peut porter un champ **optionnel**
  `courseAnchor` par misconception ; présent, il précise l'ancre ; absent, on ouvre le cours en
  haut. L'affinage est ainsi un **travail de contenu additif**, pas une dépendance de code — et
  le lot ne se bloque pas sur l'ancrage de 566 chapitres. → Q-5.
- **D-A1.2-5 — Déterministe, et c'est le socle sur lequel é11 se branchera.** Aucun LLM en A1.2 :
  le registre écrit la phrase. C'est l'application directe de « le déterministe décide, le LLM
  rédige » (é26 D-8). Le lot 1 de l'**étude 11** (« explication personnalisée post-review »)
  viendra **remplir le même emplacement** avec un texte ancré sur l'item + le distracteur + le
  tag : A1.2 définit donc l'emplacement, ses données et son état vide. Si A1.2 est bien fait,
  é11 lot 1 est un remplacement de contenu, pas une refonte d'écran.
- **D-A1.2-6 — La signature du RPC change par DROP + CREATE, dans la même transaction.** Ajouter
  des colonnes à un `RETURNS TABLE` impose de recréer la fonction, et un paramètre défaillé
  créerait une surcharge ambiguë pour PostgREST — c'est exactement ce qu'a fait
  `20260705150000_get_attempt_review_scored.sql`, dont on reprend la forme. **Fenêtre de
  déploiement** : la migration part **avant** le client qui lit les nouvelles colonnes (DoD §7,
  additif d'abord).

### 9.4 Lots, tests exigés et stop-points

| lot       | périmètre                                                                                                                                                           | tests exigés                                                                                                                                                                                                                                                                                                 |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **A1.2a** | Migration : `get_attempt_review` rend `misconception_tag` + `chapter_id` (D-A1.2-2/D-A1.2-6). Aucun changement de gate (owner-only, session complétée, jamais quiz) | **pgTAP** : (1) le tag rendu est bien celui de l'option choisie ; (2) une bonne réponse ne rend **aucun** tag ; (3) la map `distractor_tags` reste **illisible** par `authenticated` ; (4) question non taguée → NULL, la ligne reste rendue ; (5) quiz → toujours zéro ligne ; (6) non-propriétaire → refus |
| **A1.2b** | UI : bloc riche dans `quest-review-list` (erreur nommée + explication + « revoir le cours » + « m'entraîner »), i18n FR/EN/AR + RTL                                 | **Vitest** : rendu complet, rendu dégradé (tag absent / registre muet / pas de cours), bonne réponse = bloc absent, RTL. **e2e authed** : rater une question taguée → l'erreur est nommée, le lien ouvre le cours                                                                                            |

**Stop-points** — l'exécuteur s'arrête et remonte si :

1. il doit exposer `distractor_tags` au client pour faire marcher l'UI (⇒ il a raté D-A1.2-2) ;
2. il doit modifier `submit_exercise_attempt` (⇒ il a glissé vers Q-4, hors périmètre) ;
3. il doit toucher un barème, un compteur ou `consume_hint` (⇒ R-A1.2-4 / §9.1) ;
4. le corpus tagué est trop maigre pour juger du rendu : **ce n'est pas un blocage** — R-A1.2-3
   impose que le lot soit correct à vide, et le lot é07-3 / C4 l'allumera plus tard.

### 9.5 Risques

- **RISK-A1.2-A — Fuite de la clé par le tag** (rare / **critique**) → D-A1.2-2 + le pgTAP qui
  joue l'attaque par élimination, pas seulement le cas nominal. C'est le seul risque de cette
  phase qui justifie un refus de merge.
- **RISK-A1.2-B — Un lot livré inerte** (certain / faible) → assumé et **voulu** : comme é07 lots
  4 et 5, A1.2 s'allume avec le tagging du corpus. Inerte ≠ faux. À écrire dans le journal pour
  que personne ne le lise comme un bug.
- **RISK-A1.2-C — Correction perçue comme punitive** (possible / moyen) → R-A1.2-2 (rien sur les
  bonnes réponses), ton RPG des libellés du registre, et le geste « m'entraîner » qui transforme
  le constat en action. Mesure : taux de clic « revoir le cours » / « m'entraîner ».
- **RISK-A1.2-D — Divergence avec é11** (possible / moyen) → D-A1.2-5 : l'emplacement, ses
  données et son état vide sont spécifiés maintenant, pour que é11 lot 1 remplisse au lieu de
  refondre.

### 9.6 Questions — TRANCHÉES le 2026-08-02 (Mohamed)

- **Q-4 — feedback question par question : ✅ NON POUR LA RENTRÉE.** Décision conforme à la
  proposition de l'architecte. Ce n'est pas un raffinement d'affichage : cela rouvrirait la
  couture de soumission atomique (score, anti-farm, SM-2, télémétrie calculés en UNE
  transaction). À reconsidérer **après mesure du taux de clic de A1.2b** — donc après que le
  corpus soit tagué, sans quoi il n'y a rien à cliquer.
- **Q-5 — `courseAnchor` : ✅ V1 SANS ANCRES.** Tous les liens « revoir le cours » ouvrent le
  chapitre en haut. Le code ne s'y bloque pas (D-A1.2-4 : l'ancre est un champ **optionnel** du
  registre). On ancrera plus tard, **sur les tags que la télémétrie aura montrés fréquents** —
  ancrer 566 chapitres à l'aveugle serait du travail perdu à 95 %.

### Phase A0 (socle télémétrie) — LIVRÉE

Les trois lots A0.1 (schéma) · A0.2 (capture RPC + purge) · A0.3 (pipeline tags + registre) sont
mergés (PR #308, #309, +A0.3). Le signal « choix par question + misconception » est désormais
capté server-side à chaque soumission.

> ⚠️ **Ce paragraphe disait jusqu'au 2026-07-25 que A1.1 attendait le GO humain de Q-1.**
> C'est faux depuis le 2026-07-20 : le GO a été donné par l'arbitrage A1 de l'étude 26 (pipeline
> V1 mandaté), **A1.1 est livrée** (#581) puis rendue compétence-aware par é07 lot 5 (#616/#617).
> Seule **A2.1** reste derrière le seuil de données de Q-1.

### Phase A1 (la révision devient un produit) — EN COURS

- **2026-07-31 — A1.2a livrée** (arena#689, correctif de test arena#691) : `get_attempt_review`
  rend `misconception_tag` (le tag de l'option **choisie**, et seulement sur une réponse fausse)
  + `chapter_id`, sans qu'une porte bouge. Stop-point **D-A1.2-2 tenu**, et **encodé en attaque** :
  trois assertions pgTAP rejouent l'élimination par la map plutôt que le cas nominal.
- **2026-07-31 — A1.2b livrée** (arena#695). Elle a dû **corriger D-A1.2-3**, fondée sur une
  surface de compilation client qui **n'existe pas** : le registre n'est lu que par `build.ts` et
  `qa.ts`, et depuis la scission `content/` n'est pas dans le dépôt public au build. Les libellés
  passent donc **par la base**, par le canal des compétences (é07). L'intention est préservée : la
  fonction SQL rend un ID, le registre reste source unique, une reformulation reste une correction
  de registre sans migration.
- **2026-08-03 — le geste « m'entraîner » livré** (arena#707, arbitrage **A12**) : un champ
  `competency` dans le registre traduit l'erreur en compétence, et le bouton réutilise
  `get_exercises_for_competency` — R-A1.2-6 tenu, aucun second chemin de remédiation.
- ⚠️ **La phase A1.2 est complète en CODE et muette en PROD** : le corpus ne porte **aucun** tag
  de misconception (0 occurrence sur ~18 700 questions, mesuré le 2026-07-31). Rien ne s'allumera
  avant **C4bis**, le pilote de tagging `math` 9ᵉ (arbitrage A11).

- **2026-07-20 — A1.1 livrée** (#581) : RPC `get_daily_plan` (migration
  `20260721120000_daily_plan_rpc.sql`) + panneau `DailyReviewPanel` sur le dashboard, ≤ 3 items
  triés par retard SM-2 et priorité misconceptions. Première sortie visible du moteur adaptatif :
  deux des trois « boucles collectées-jamais-surfacées » de l'étude 26 (SM-2, `user_misconceptions`)
  cessent d'être mortes. C'est un **sélecteur** d'exercices existants — récompenses et anti-farm
  inchangés (R-4 tenu).
- **2026-07-25 — A1.1 devient compétence-aware** par le **lot 5 de l'étude 07** (#616, correctif
  de GRANT #617) : `get_daily_plan` lit aussi `user_competency_mastery` (troisième terme du score,
  maillon faible décayé). Non-régression par construction — sans ligne de maîtrise, le terme vaut
  zéro et le plan est identique. Le cadrage prévu par R-1 (« le lot A1.1 devient compétence-aware
  via le lot 5 de l'étude 07 ») s'est donc réalisé tel quel.
- **2026-07-25 — amendement A1.2 rédigé** (§9, architecte) : la « correction riche à l'échec »
  rattachée ici par l'arbitrage A1-Q4 de l'étude 26. Le contrat est fermé, en deux lots
  (A1.2a serveur / A1.2b client), et il **corrige deux suppositions du mandat** : l'explication
  post-erreur n'a jamais été monnayée (c'est l'indice _avant_ réponse qui l'est), et un feedback
  question-par-question rouvrirait la couture de soumission atomique — écarté du périmètre et
  posé en Q-4. Le lot allumera peu tant que le corpus n'est pas tagué (é07 lot 3) : **inerte par
  construction, jamais faux**, comme é07 lots 4 et 5.
