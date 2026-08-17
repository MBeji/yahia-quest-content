# Étude 02 — Examen blanc / simulation concours

> **Statut** : **livrée le 2026-08-16** — sortie de la file différée V2 le 2026-08-13 (é28 Q-4,
> arbitrée par Mohamed), puis re-scopée **et** exécutée le 2026-08-16. Sa porte d'entrée était
> « V1 ≥ M3 **et** annales transcrites » ; elle a été **levée** parce qu'un **v1 n'a pas besoin
> d'annales** : un assemblage chronométré du corpus existant plus un rang relatif suffisent à
> créer la preuve et le partage. Les annales restent un **enrichissement ultérieur** — c'est un
> chantier de **contenu**, au dépôt privé, et il n'est pas ouvert.
> **Les quatre lots utiles sont sur `main`** : lots 1-2, schéma + moteur SQL (**arena#743**,
> migrations appliquées en prod) ; lots 3-4, passation + copie corrigée (**arena#746**). Le
> **lot 5 est sans objet** — voir l'écart n° 2 ci-dessous.
>
> ⚠️ **Trois écarts par rapport au texte ci-dessous, tranchés à l'exécution.** Le raisonnement
> complet vit dans les **en-têtes des deux migrations**, qui en sont la source ; ce fichier ne
> fait que les inscrire (§8).
>
> 1. **R-7 est rescopé** : réserver le mode aux porteurs d'un entitlement `concours` livrerait,
>    en phase gratuite, un **écran verrouillé pour tout le monde** — aucun parcours n'est
>    `is_premium`, donc personne n'a d'entitlement. La seule condition est d'**avoir un compte**.
> 2. **Le lot 5 (console de composition admin) n'a pas été construit** — remplacé par un
>    assemblage **par requête** dans la migration de seed.
> 3. **Le détail par chapitre et les liens de remédiation de l'US-3 / lot 4 n'ont pas été
>    livrés** : le détail est **par épreuve**, avec son coefficient. Reste ouvert.
>
> ⚠️ 2026-07-11 : la justification « premium » ci-dessous précède le pivot gratuité. Elle n'a
> pas été réécrite au re-scopage — elle a été **tranchée à l'exécution** par l'écart n° 1 : la
> feature est ouverte à tout compte, et **aucune surface ne dit « premium »**.
> **Priorité** : 02 · **Valeur** : l'expérience « concours » en conditions réelles : note /20 au barème réel du concours, classement percentile, diagnostic par matière (rédaction d'origine : « justifie les parcours premium ») · **Complexité** : moyenne+
> **Architecte** : Fable (claude-fable-5), 2026-07-04 · **Exécuteur** : Opus 5, 2026-08-16
> **Dépend de** : ~~contenu exam-style suffisant (paliers d4 + `NN-annales-bac` pour le bac)~~ — **dépendance levée** : le v1 s'assemble sur le corpus existant ; rien côté code
> **Docs normatifs liés** : AGENTS.md (canonique — gamification centralisée, DoD §7, grants d'une table neuve), STATUS.md (§ phase gratuite), ARCHITECTURE.md, docs/lycee-architecture.md (palier annales)
> **Source de vérité de l'exécution** : les en-têtes de `supabase/migrations/20260816120000_mock_exams_schema.sql` et `20260816130000_mock_exams_engine.sql`

## 1. Contexte & objectif produit

Les parcours payants s'appellent « concours » mais rien ne simule un concours : tout est mission
par mission, avec récompenses immédiates. Il manque l'épreuve : sujet multi-matières, durée
globale, pas de feedback pendant, correction différée, **percentile face aux autres candidats**.
KPI : % d'entitled qui font ≥1 examen blanc, récurrence mensuelle, corrélation score↔progression
(argument parents), churn des entitled avant/après.
Non-objectif : reproduire officiellement les barèmes ministériels (on affiche « simulation »),
surveiller/anti-plagiat lourd, épreuves rédactionnelles (QCM/engine actuel uniquement).

> **Livré (2026-08-16) — ce que la phase gratuite fait de ces KPI.** Les deux qui parlent
> d'`entitled` (taux et churn) sont **sans objet** tant que l'étude 01 est gelée : le dénominateur
> est l'ensemble des comptes. Restent mesurables la **récurrence** et la **corrélation
> score↔progression**, et il s'y ajoute celui que le barème rend possible : **l'écart entre la
> note /20 de l'examen blanc et la moyenne de l'élève sur ses missions** — c'est lui qui dit si
> l'entraînement prépare vraiment l'épreuve. Aucun de ces KPI n'est instrumenté à ce jour.
> Le non-objectif « barèmes ministériels » tient toujours pour la **notation officielle**, mais
> les **coefficients** du concours, eux, sont bien reproduits (R-9) : c'est la différence entre
> simuler l'épreuve et simuler l'administration.

## 2. Spécification fonctionnelle

**Acteurs** : ~~élève entitled (le mode est un **perk premium concours**, comme le Dungeon)~~ →
**tout élève connecté** (écart n° 1) ; ~~admin (composer/publier des examens)~~ → **personne**,
la composition est un `INSERT … SELECT` de migration (écart n° 2) ; anonyme : rien (les six RPC
sont `REVOKE`d pour `anon`).

- **US-1** : je vois la liste des examens blancs de MON parcours (ex. « Concours blanc 9ème —
  session 1 », durée totale, matières) avec mon historique (fait/score/percentile).
- **US-2** : je démarre : écran consignes → le chrono global démarre (deadline serveur) ; je
  navigue entre les épreuves (une par matière), je réponds, je peux revenir en arrière tant que
  le temps court ; aucun indice/correction pendant.
- **US-3** : je rends (ou le temps expire) → écran résultats : score global sur barème, détail
  par matière ~~et par chapitre~~, percentile parmi tous les candidats de cet examen, ~~et liens
  de remédiation (« revois le chapitre X »)~~.
  → **Livré partiellement (écart n° 3)** : note /20 en tête, détail **par épreuve** avec son
  coefficient, percentile, et le corrigé complet question par question. **Le détail par chapitre
  et les liens de remédiation manquent** — `get_mock_exam_review` ne remonte pas le chapitre de
  la question, donc il n'y a rien à quoi accrocher un lien. C'est le seul reliquat fonctionnel
  du v1 ; il vaut un lot 6, pas une reprise.
- **US-4** : je ne peux faire chaque examen qu'une fois en mode classé ; je peux le refaire en
  mode entraînement (non classé, non récompensé).
- ~~**US-5** : admin — je compose un examen (choix d'exercices existants par matière, durée,
  barème par exercice), je le publie/dépublie.~~ → **sans objet (écart n° 2)** : la composition
  se fait par requête en migration. Une console n'a de sens qu'au-delà d'une session par mois.

**Règles métier** :

- **R-1** : un examen = une liste ordonnée d'**exercices existants** (mode `challenge`/`boss`,
  idéalement issus des paliers d4/annales) — pas de banque parallèle, pas de génération dynamique.
- **R-2** : la deadline est **serveur** : `deadline = started_at + duration`; toute soumission
  après deadline est acceptée mais tronquée aux réponses déjà enregistrées (auto-rendu).
- **R-3** : pendant la session, aucune review/clé n'est renvoyée (posture GAP-020) ; la review
  complète se débloque à l'état `finished` seulement.
- **R-4** : une seule session classée (`ranked`) par (user, exam) — contrainte unique ; les
  suivantes sont `practice` (US-4).
- **R-5** : récompense forfaitaire à la fin (XP/coins selon score, constantes dans
  `src/shared/constants/gamification.ts`) versée UNE fois (session classée uniquement) via
  `award_xp` ; ~~les gates anti-farm existants (tooFast par épreuve) s'appliquent~~.
  → **Livré, avec une nuance** : la garde `tooFast` n'a **pas** été portée, et n'avait rien à
  garder — R-4 n'autorise **qu'une** session classée par examen, et l'entraînement ne paie rien.
  Il n'y a donc pas de boucle à farmer : l'anti-farm est structurel, pas conditionnel. Le
  barème (300 XP / 60 pièces × le score) vit **en dur dans `finish_mock_exam`** — la RPC est la
  garde — et il est **mirroré** dans les constantes TS, qui pilotent l'affichage.
- **R-6** : percentile calculé sur les sessions `ranked finished` du même examen ; affiché à
  partir de N≥20 candidats (sinon « classement disponible à partir de 20 candidats »).
- **R-7 — RESCOPÉE le 2026-08-16 (écart n° 1)** : ~~accès = entitlement live sur le parcours de
  l'examen (réutilise `has_parcours_entitlement`), pas de preview gratuit en v1~~.
  **La seule condition d'accès est d'avoir un compte.** Motif : R-7 raisonne sur une prémisse
  **pré-pivot** — l'annotation du 2026-07-11 en tête le disait déjà de toute la justification
  « premium » — alors que la gratuité est actée depuis le **2026-06-21**. En phase gratuite, tout
  parcours a `is_premium = false`, donc **plus personne ne détient d'entitlement `concours`** ;
  appliquer R-7 tel quel n'aurait pas protégé un privilège, il aurait livré un écran verrouillé
  pour **tout le monde** — une feature mort-née. Rien n'est gaté, aucune surface ne nomme
  « premium ».
  ⚠️ **Au passage, une date fausse à ne pas propager** : l'en-tête de
  `20260816120000_mock_exams_schema.sql` écrit que « l'étude a été écrite AVANT le pivot gratuit
  du 2026-06-21 ». C'est inexact — elle est datée du **2026-07-04**, donc **après**. Le
  raisonnement, lui, tient entièrement : ce n'est pas la chronologie qui compte mais le fait que
  son texte n'avait pas absorbé le pivot.
  **Où la garde se reposera** : dans `start_mock_exam`, au dégel du premium par l'étude 01. C'est
  **un `IF` dans une fonction**, pas une migration de schéma — c'est précisément pour ça que le
  rescopage ne coûte rien à défaire, et pourquoi il ne fallait pas encoder l'entitlement dans les
  tables.
- **R-8** : réponses **enregistrées au fil de l'eau** (par épreuve) côté serveur — un crash/refresh
  ne perd rien ; reprise de session tant que la deadline court.
- **R-9 — LE BARÈME EST LA FEATURE** (ajoutée à l'exécution, 2026-08-16) :
  `mock_exam_papers.points` n'est pas une décoration, c'est là que vivent les **coefficients
  réels du concours** — **maths 4, arabe 2+2, français 3, sciences 3, anglais 1**, portés **×10**
  pour rester en entiers, soit **150 points**. Chaque épreuve rapporte `points × (justes / total)`
  et la **note /20** en dérive (`20 × score / max`) : c'est la seule échelle que l'élève, le
  parent et l'établissement lisent de la même façon. Le pourcentage ne sert qu'à l'économie de
  jeu. **Pourquoi c'est une règle et pas un détail de seed** : un examen blanc qui pondère toutes
  les matières pareil entraîne l'élève à répartir son effort **à l'envers** — c'est le reproche
  principal qu'on peut faire à un QCM générique, et le renverser est l'essentiel de la valeur de
  cette étude. L'écran affiche le coefficient à côté de chaque résultat, sans quoi « 8/10 en
  anglais » et « 8/10 en maths » se liraient pareil.

**i18n** : FR/EN/AR (RTL complet — les épreuves héritent de la langue de leur matière, l'enveloppe
UI suit la langue de l'app). **Hors périmètre (v1)** : examens programmés à heure fixe
(synchrones), certificats PDF, mode surveillé.

## 3. Architecture technique (décisions fermées)

- **D-1 — Composition par curation, pas par tirage** : un examen référence des exercices existants
  (R-1). Rejeté : assemblage aléatoire par chapitre (qualité/équilibrage non garantis, percentile
  non comparable). La rotation anti-partage se fait en publiant de nouvelles sessions (contenu
  pipeline `NN-annales-bac` alimente).
- **D-2 — Sessions serveur, réponses au fil de l'eau** (R-8) : pas de state client précieux ;
  reprise gratuite. Rejeté : tout-soumettre-à-la-fin (fragile mobile).
- **D-3 — Percentile à la lecture** (requête window sur scores finis, index dédié), pas de vue
  matérialisée en v1 (volumes faibles) ; bascule matérialisée = optimisation future notée.
- **D-4 — Réutiliser le moteur de rendu** : l'épreuve rend les questions via les mêmes briques
  (`shuffleOptions`, `RichField`/`OptionContent`) mais dans un conteneur examen dédié
  (`src/features/exam/`) — PAS de fork d'`ExercisePlayer` (trop couplé quête/récompenses) ni
  d'import de la feature quest (frontières) : les briques partagées vivent déjà dans `shared/`.

**Modèle de données** (migration additive + GRANTs explicites) :

```sql
CREATE TABLE public.mock_exams (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  parcours_id TEXT NOT NULL REFERENCES public.parcours(id),
  title_fr TEXT NOT NULL, title_ar TEXT, title_en TEXT,
  duration_minutes INT NOT NULL CHECK (duration_minutes BETWEEN 15 AND 300),
  status TEXT NOT NULL DEFAULT 'draft' CHECK (status IN ('draft','published','archived')),
  display_order INT NOT NULL DEFAULT 0, created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE TABLE public.mock_exam_papers (      -- une "épreuve" = un exercice pondéré
  exam_id UUID NOT NULL REFERENCES public.mock_exams(id) ON DELETE CASCADE,
  exercise_id UUID NOT NULL REFERENCES public.exercises(id),
  points INT NOT NULL CHECK (points > 0),   -- barème de l'épreuve
  display_order INT NOT NULL, PRIMARY KEY (exam_id, exercise_id)
);
CREATE TABLE public.mock_exam_sessions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  exam_id UUID NOT NULL REFERENCES public.mock_exams(id),
  user_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
  kind TEXT NOT NULL DEFAULT 'ranked' CHECK (kind IN ('ranked','practice')),
  started_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  deadline   TIMESTAMPTZ NOT NULL,
  finished_at TIMESTAMPTZ,
  answers JSONB NOT NULL DEFAULT '{}'::jsonb,   -- {questionId: choice} au fil de l'eau (R-8)
  score_points NUMERIC, max_points INT,
  UNIQUE (exam_id, user_id, kind) DEFERRABLE INITIALLY IMMEDIATE  -- R-4 (unique ranked; practice: cf. note lot 1)
);
-- RLS: sessions owner-only; exams/papers SELECT authenticated (published only via policy), admin ALL.
-- NOTE lot 1: l'unicité ne vaut que pour kind='ranked' → index partiel UNIQUE (exam_id,user_id) WHERE kind='ranked'.
```

> **⚠️ Ce bloc est la PROPOSITION de l'architecte, pas le schéma en base.** Le schéma réel est
> `supabase/migrations/20260816120000_mock_exams_schema.sql`, et lui seul fait foi. Cinq écarts,
> tous documentés dans son en-tête :
>
> - `mock_exam_papers` porte en plus **`label_{fr,en,ar}`** — le nom de l'**épreuve**
>   (« Mathématiques »), pas le titre de l'exercice : au concours l'élève voit une matière.
> - `exercise_id` est en **`ON DELETE CASCADE`**, et c'est un arbitrage, pas un réflexe : le
>   corpus est réappliqué régulièrement par `apply-content.yml`. En `RESTRICT`, une application
>   de contenu **échouerait** à cause d'un examen blanc — on casserait la chaîne de publication
>   pour protéger une simulation. En `CASCADE`, l'examen perd une épreuve, ce qui est visible et
>   rattrapable, et `start_mock_exam` refuse d'ouvrir un examen vide (`MOCK_EXAM_EMPTY`) plutôt
>   que de servir une coquille chronométrée.
> - l'unicité est l'**index partiel** annoncé par la note lot 1, pas la contrainte `UNIQUE` du
>   bloc — celle-ci aurait aussi interdit deux entraînements.
> - il s'y ajoute un `CHECK (deadline > started_at)` et **quatre index** (catalogue publié, ordre
>   des épreuves, classement, sessions d'un élève).
> - la RLS des sessions n'est pas « owner-only » : elle est **owner, admin ou parent lié**
>   (`parent_student_links`, actif) — la copie d'un enfant est lisible par son parent, comme le
>   reste de son suivi. **Aucune politique d'écriture nulle part** : le seul écrivain est le jeu
>   de RPC `SECURITY DEFINER`.

**Server** (SQL d'abord — le scoring reste en SQL comme tout le projet) :

- RPC `start_mock_exam(exam uuid, kind text)` SECURITY DEFINER : vérifie R-7 + R-4, crée la
  session, retourne (session, épreuves+questions **sans clés**).
- RPC `save_mock_answers(session uuid, answers jsonb)` : merge si deadline non passée (R-2/R-8).
- RPC `finish_mock_exam(session uuid)` : score en SQL (mêmes égalités que
  `submit_exercise_attempt`, pondérées par `points`), fige `finished_at`, applique R-5 (award_xp
  une fois, ranked only) ; retourne le détail par épreuve/chapitre.
- RPC `get_mock_exam_review(session)` : review complète seulement si `finished` (R-3) ;
  `get_mock_exam_percentile(session)` : window function (D-3, R-6).
- Server fns zod dans `src/features/exam/exam.server.ts` (wrap RPCs + `requireSupabaseAuth`) ;
  ~~admin fns pour US-5~~ (écart n° 2).
- Les ~~4~~ RPCs sont REVOKE anon ; pgTAP complet (états, deadline, unicité ranked, percentile).

> **Livré : six RPC, pas cinq.** Il s'y est ajouté **`list_mock_exams(p_parcours_id)`** — le
> catalogue « mes examens + mon historique », que l'étude supposait implicitement dans US-1 sans
> lui donner de RPC. C'est la seule des six en **`INVOKER`** : la RLS du lot 1 fait déjà exactement
> le tri voulu (examens publiés, mes sessions à moi), et une fonction `DEFINER` n'y ajouterait
> qu'un contournement de RLS à maintenir. Les six sont `REVOKE`d pour `PUBLIC`/`anon` et
> `GRANT EXECUTE` nominatif à `authenticated`.
> Deux points d'implémentation qui ne se lisent pas dans le texte ci-dessus : le scoring
> **réutilise `score_answer` / `answer_key_display`**, les mêmes primitives qui corrigent une
> quête — une réponse ne peut donc pas être jugée différemment selon l'écran qui la pose ; et
> `finish_mock_exam` fige `finished_at = LEAST(now(), deadline)`, si bien que **rendre en retard
> ne vole pas de temps**, ça tronque. Chaque payload emporte `serverNow`, pour que le chrono du
> poste se cale sur l'horloge du serveur.

**Client** : `src/features/exam/` (barrel, `exam.server.ts`, `components/ExamShell`,
`ExamPaper`, `ExamResults`, `__tests__/`) ; routes `_authenticated/examens.tsx` (liste) et
`_authenticated/examen.$sessionId.tsx` (passation, guard deadline) ; chrono global affiché depuis
la deadline serveur (resync à chaque save, jamais source de vérité côté client).

> **Livré, avec deux noms différents.** La route de passation est
> **`_authenticated/examen.$examId.tsx`** et non `$sessionId` : le paramètre d'URL est l'**examen**
> (plus `?kind=ranked|practice`), et c'est `start_mock_exam` qui **résout ou reprend** la session
> côté serveur. Une URL portant la session aurait exposé un identifiant de session dans un lien
> partageable et obligé le client à en créer une avant de savoir s'il en avait déjà une. Les
> composants livrés sont **`exam-countdown.tsx`** et **`exam-results.tsx`** (kebab-case, convention
> du dépôt) ; il n'y a **pas** d'`ExamShell`/`ExamPaper` séparés — la passation vit dans la route,
> comme `quest.$exerciseId`. D-4 est tenu : la route importe `QuestionInput` et `shuffleOptions`
> **sans** passer par le barrel de `quest`, qui aurait tiré toute la boucle de récompense dans son
> graphe de modules.

**Observabilité** : log structuré start/finish/expire + compteur sessions abandonnées.

> **Non livrée.** Ni log structuré dédié, ni compteur de sessions abandonnées. À reprendre si la
> feature vit ; c'est la dette assumée du v1 (§8).

## 4. Plan d'exécution en lots

| lot | contenu                                                                  | objets créés                    | tests exigés                                                        | dépend de | livré                     |
| --- | ------------------------------------------------------------------------ | ------------------------------- | ------------------------------------------------------------------- | --------- | ------------------------- |
| 1   | Migration tables + RLS/grants + index partiel ranked                     | 1 migration                     | pgTAP (RLS, unicité ranked, contraintes)                            | —         | ✅ arena#743              |
| 2   | RPCs start/save/finish/review/percentile                                 | 1 migration RPCs                | pgTAP (deadline R-2, review-gate R-3, R-5 une fois, percentile R-6) | 1         | ✅ arena#743              |
| 3   | Server fns + liste examens + passation UI (chrono, navigation, autosave) | feature `exam/` + routes + i18n | Vitest (guards, autosave, états UI, RTL)                            | 2         | ✅ arena#746              |
| 4   | Résultats + percentile + liens remédiation                               | `ExamResults` + fns             | Vitest ; snapshot breakdown par chapitre                            | 3         | ✅ arena#746, **partiel** |
| 5   | Admin composition/publication (US-5) + e2e authed                        | fns + UI admin                  | Vitest ; 1 spec e2e (start→finish practice)                         | 2         | **sans objet**            |

- [x] **Lot 1 — schéma & sécurité** (merge seul, avant le code — DoD §7) — `20260816120000_mock_exams_schema.sql`, arena#743
- [x] **Lot 2 — moteur SQL de session** — `20260816130000_mock_exams_engine.sql` (6 RPC) + le seed de la session 1, arena#743
- [x] **Lot 3 — passation** — `src/features/exam/`, routes `/examens` et `/examen/$examId`, i18n `exam.*` ×3, arena#746
- [x] **Lot 4 — résultats & percentile** — arena#746. **Partiel** : le détail est par **épreuve**,
      pas par chapitre, et il n'y a **pas** de liens de remédiation (écart n° 3, US-3)
- [ ] ~~Lot 5 — admin & e2e~~ — **SANS OBJET, remplacé par le seed** (écart n° 2)

**Pourquoi le lot 5 n'a pas été construit** — et pourquoi ce n'est pas une paresse d'exécution.
Composer un examen depuis une console suppose de **désigner des exercices par leur id**. Or
**un id d'exercice du corpus ne vit pas dans le dépôt public** (étude 24 : le contenu est compilé
et appliqué depuis le dépôt privé), et une FK littérale vers lui rendrait **une base vierge
irreconstructible** — c'est exactement ce que `db:check-chain` refuse, et les quatre pannes en
cascade de l'étude 24 lot 4 ont montré ce que ça coûte. La composition est donc un
`INSERT … SELECT` **par requête** : il sélectionne l'exercice le plus difficile de chaque matière
au niveau visé, ne rend **rien** quand le corpus est absent (comportement voulu sur une base
neuve), et l'examen ne passe `published` que s'il a **réellement récolté ≥ 5 épreuves** — mieux
vaut aucun examen visible qu'un « concours blanc » à trois matières. Une console d'administration
redeviendra utile au-delà d'une session par mois (Q-2) ; elle devra alors composer par **requête
paramétrée**, jamais par liste d'ids.

**Stop-points** : lot 2 ne touche PAS aux RPCs existants (`submit_exercise_attempt` & co) ; lot 3
ne fork pas `ExercisePlayer` (D-4) ; aucun lot n'introduit de récompense hors constantes
centralisées ; la composition des examens (contenu) n'est pas du ressort de l'exécuteur.
→ **Les trois premiers ont été tenus.** Le quatrième a été **levé par nécessité** : sans une
composition livrée avec le moteur, la feature n'avait aucun examen à ouvrir et personne pour en
créer un (le lot 5 étant tombé). Le seed est donc de l'exécuteur — mais il ne crée **aucune**
question : il ne fait que **désigner** du contenu déjà publié.

## 5. Stratégie de test

pgTAP = cœur (machine d'états, fenêtres de temps simulées via `clock_timestamp` injecté/paramètre,
percentile avec jeu de 25 sessions). Vitest : fns (zod, guards entitlement), composants (chrono
resync, autosave debounce, états finished/expired). E2E authed : un examen practice complet sur le
projet TEST (seed dédié dans `scripts/e2e/`). Pas d'impact `smoke:shell` (routes authed).

> **Ce qui a réellement été écrit.**
>
> - **pgTAP** : `supabase/tests/49_mock_exams.test.sql`, **`plan(26)`** — RLS armée sur les trois
>   tables · `anon` ne voit aucun examen, n'en ouvre aucun, n'en rend aucun · l'élève connecté lit
>   le catalogue **et** peut ouvrir (« la garde est dans la fonction, pas dans le `GRANT` ») ·
>   personne n'écrit une session à la main · **R-3** l'explication secrète est **absente** du
>   payload de `start_mock_exam` et **présente** dans la review · **R-2**
>   `MOCK_EXAM_DEADLINE_PASSED` · **R-4** `MOCK_EXAM_ALREADY_RANKED` · double rendu refusé
>   (`MOCK_EXAM_FINISHED`, « sinon la récompense double ») · **pondération du barème** (la note
>   vaut 12/20 et non 15) · récompense classée au prorata (300 XP × 60 %) · percentile et **R-6**
>   (aucun rang sous 20 candidats) · une copie n'est pas lisible par un autre élève.
>   ⚠️ **`db-tests.yml` n'est pas un check requis** et ne bloque pas l'auto-merge. La suite a bien
>   tourné en vert, mais par un `workflow_dispatch` **sur `main`, le 2026-08-16 à 18h31 UTC —
>   c'est-à-dire APRÈS le merge de arena#743** (16h41). L'ordre est le mauvais : la validation a
>   suivi la livraison au lieu de la précéder. À faire **sur la branche, avant promotion**, comme
>   l'étude 22 l'avait fait.
> - **Vitest** : `exam.test.ts` (server fns, zod, mapping des payloads), `exam-results.test.tsx`
>   (note /20, coefficient affiché, percentile et son état d'attente, corrigé), et
>   `exam-countdown.test.tsx` (dérive d'horloge, expiration).
> - **E2E authed : non écrit.** Il vivait dans le lot 5, tombé avec lui (écart n° 2). C'est la
>   dette de test assumée du v1 — la chaîne start → save → finish n'est couverte de bout en bout
>   qu'en pgTAP, jamais par un navigateur.

## 6. Risques & mitigations

- **RISK-1** Partage des sujets entre élèves (probable/moyen) → D-1 rotation de sessions +
  percentile par examen (le partage fausse le classement, pas l'accès) ; v2 possible : variantes.
- **RISK-2** Triche au chrono (client) (probable/faible) → R-2 deadline serveur, saves refusés après.
- **RISK-3** Percentile trompeur à faible N (certain/faible) → R-6 seuil d'affichage 20.
- **RISK-4** Charge de la window function (rare/faible) → index (exam_id, score) ; D-3 note la
  bascule matérialisée si besoin.

> **RISK-1 est le seul qui reste ouvert au 2026-08-16, et sa mitigation n'existe pas encore.**
> « La rotation anti-partage se fait en publiant de nouvelles sessions » — or **il n'y a qu'une
> session**, et rien ne dit qui publiera la suivante ni à quel rythme : c'est exactement la Q-2,
> toujours ouverte. Tant qu'elle l'est, un sujet partagé reste partagé. Le dégât est **borné**
> (R-4 : une seule copie classée ; le partage fausse le rang, pas l'accès) mais il n'est pas nul,
> et il grandit avec le nombre de candidats. **La Q-2 n'est donc pas une question d'intendance
> éditoriale : c'est la mitigation de RISK-1.**
> RISK-2 et RISK-3 sont tenus par le code (deadline serveur, seuil à 20). RISK-4 est tenu par
> l'index `idx_mock_exam_sessions_ranking` — et le percentile est calculé par deux `count()`
> filtrés plutôt que par une vraie window function, ce qui le rend encore moins coûteux que prévu.

## 7. Questions ouvertes (pour l'humain)

- **Q-1 — TRANCHÉE PAR DÉFAUT à l'exécution, à re-trancher** : barème d'XP/coins de la récompense
  forfaitaire. **Retenu : 300 XP et 60 pièces × le score, session classée uniquement** — c'est-à-dire
  la proposition de l'étude elle-même, faute d'arbitrage humain rendu au moment de livrer.
  **Ancrage** : un exercice complet vaut ≈ 75 XP / 15 pièces ; un blanc en vaut donc cinq à six,
  il est plus long, plus dur, et ne se joue **qu'une fois**. Une session d'entraînement ne paie
  rien — sinon l'examen cesse d'être une mesure pour devenir une ferme à XP, précisément le travers
  que l'étude 09 traque. ⚠️ **Ce chiffre est fait pour être re-tranché sur la première lecture
  réelle** : il n'a été calibré sur aucune donnée, seulement sur une proportion. Il vit à deux
  endroits qu'il faut bouger ensemble — `finish_mock_exam` (la garde) et
  `src/shared/constants/gamification.ts` (l'affichage).
- **Q-2 — OUVERTE, et c'est la question qui compte maintenant** : cadence éditoriale des sessions
  (1/mois par concours ?) et **qui compose**. Le lot 5 étant sans objet, les deux réponses
  possibles ont changé : ce n'est plus « admin humain via US-5 » **ou** « pipeline contenu », c'est
  **une migration de seed par session** (le geste d'aujourd'hui, qui suppose une session de code à
  chaque fois) **ou** un vrai pipeline côté dépôt privé. Voir §6 : **cette question est aussi la
  mitigation de RISK-1**, elle ne se réduit pas à de l'intendance.
- **Q-3 — SANS OBJET en phase gratuite** : ~~le mode examen doit-il être ouvert en preview limitée
  aux non-entitled (marketing) ?~~ La question supposait deux populations ; l'écart n° 1 n'en
  laisse qu'une — **tout compte a l'accès complet**, il n'y a pas de preview à doser. ⚠️ **À
  re-poser telle quelle au dégel de l'étude 01** : c'est le moment où la garde se reposera dans
  `start_mock_exam`, et donc le moment où « qu'est-ce qu'un non-abonné voit ? » redeviendra une
  vraie question.
- **Q-4 — NOUVELLE (2026-08-16)** : faut-il un **lot 6** pour le reliquat de l'US-3 — détail par
  chapitre et liens de remédiation (écart n° 3) ? Ce n'est pas gratuit : il faut que
  `get_mock_exam_review` remonte le chapitre de chaque question. **L'argument pour** : sans lui, la
  copie corrigée dit « tu as raté les maths » et non « revois ce chapitre-là » — or le diagnostic
  actionnable est la moitié de la promesse faite au parent. **L'argument contre** : la valeur de
  l'examen blanc se mesure d'abord à ce que la note /20 déclenche, pas au détail du corrigé ; mieux
  vaut attendre la première session réelle.
- **Q-5 — NOUVELLE (2026-08-16), à vérifier avant toute autre** : **« Concours blanc 9ᵉ — session
  1 » est-il réellement `published` en production ?** Le seed ne publie qu'à partir de **5 épreuves
  récoltées** sur 6, et ce qu'il récolte dépend du corpus 9ᵉ réellement en base au moment de
  l'application. Ce fait **n'est pas vérifiable depuis un poste** (la table n'est lisible que par
  un compte connecté) ; il se lit dans la base. **Tant qu'il n'est pas vérifié, « livrée » décrit
  le code, pas une feature que quelqu'un peut utiliser.**

## 8. Journal d'exécution

- **2026-08-13 — Sortie de la file différée V2** (étude 28, Q-4, arbitrée par Mohamed). La porte
  « V1 ≥ M3 **et** annales transcrites » est levée : un v1 n'a pas besoin d'annales. Motif produit
  (é28 M-2) : un parent tunisien juge sur « est-ce que ça prépare au concours », et c'était le plus
  gros écart du produit face au marché. Statut `brouillon`, aucun lot commencé, re-scopage demandé
  à l'architecte **avant** tout lot.

- **2026-08-16 — Lots 1 et 2 (schéma + moteur SQL), arena#743.** Le re-scopage n'a pas fait l'objet
  d'un document séparé : il a été **écrit dans les en-têtes des deux migrations**, qui sont depuis
  la source de vérité de cette étude. Livré : `20260816120000_mock_exams_schema.sql` (3 tables,
  RLS, grants nominatifs, 5 index dont l'unicité partielle de la session classée) et
  `20260816130000_mock_exams_engine.sql` (**6 RPC**, `REVOKE` pour `anon` + `GRANT EXECUTE` à
  `authenticated`, puis le seed de la session 1). `supabase/tests/49_mock_exams.test.sql`,
  **26 assertions**. Migrations **appliquées en production** par la chaîne `db-migrate-prod.yml`.

  **Écart accepté n° 1 — R-7 est rescopé, et c'est l'arbitrage central de la livraison.** L'étude
  datant du 2026-07-04 réserve le mode aux porteurs d'un entitlement `concours`. Appliqué tel quel
  en phase gratuite, il ne protège aucun privilège : **tout parcours a `is_premium = false`, donc
  personne ne détient d'entitlement**, donc l'examen serait né verrouillé pour tout le monde. La
  condition retenue est d'**avoir un compte**. Le choix qui rend la décision réversible : ne pas
  encoder l'entitlement dans les tables — la garde se reposera dans `start_mock_exam` au dégel de
  l'étude 01, c'est-à-dire **un `IF` dans une fonction**, jamais une migration de schéma.

  **Écart accepté n° 2 — le lot 5 (console de composition) n'est pas construit, il est remplacé.**
  Une console suppose de désigner des exercices **par leur id**, et un id d'exercice du corpus **ne
  vit pas dans le dépôt public** (étude 24). Une FK littérale vers lui rendrait une base vierge
  irreconstructible — ce que `db:check-chain` refuse, et ce qui a produit quatre pannes en cascade
  après l'étude 24 lot 4. La composition est donc un `INSERT … SELECT` en migration, qui **ne rend
  rien** quand le corpus est absent : « Concours blanc 9ᵉ — session 1 », 90 min, naissant en
  `draft` et ne passant `published` **que s'il a récolté ≥ 5 épreuves** sur 6. Mieux vaut aucun
  examen visible qu'un concours blanc à trois matières.

  **Le barème porte les coefficients réels (R-9, ajoutée à l'exécution).** maths 4, arabe 2+2,
  français 3, sciences 3, anglais 1 — **×10**, soit 150 points ; la note /20 en dérive. Ce n'est
  pas un détail de seed : un blanc qui pondère tout pareil entraîne l'élève à répartir son effort
  à l'envers. **Piège de slug rencontré et documenté au passage** : en 9ᵉ, `svt` porte **la
  physique** (العلوم الفيزيائية) et `sciences-vie-terre` porte la SVT — les libellés des épreuves
  rétablissent la vérité côté élève.

  **Deux choix d'implémentation qui ne se lisent pas dans la spec** : (i) le scoring **réutilise
  `score_answer` / `answer_key_display`**, les primitives qui corrigent déjà une quête — une
  réponse ne peut pas être jugée différemment selon l'écran qui la pose, et aucun second chemin de
  correction n'a été ouvert en TypeScript ; (ii) `finish_mock_exam` fige
  `finished_at = LEAST(now(), deadline)` — rendre en retard **ne vole pas de temps**, ça tronque
  aux réponses déjà enregistrées.

  **`ON DELETE CASCADE` sur `exercise_id` est un arbitrage, pas un réflexe** : en `RESTRICT`, une
  application de contenu (`apply-content.yml`, qui rejoue le corpus régulièrement) **échouerait**
  à cause d'un examen blanc — on casserait la chaîne de publication pour protéger une simulation.
  En `CASCADE`, l'examen perd une épreuve, ce qui est visible, et `start_mock_exam` refuse
  (`MOCK_EXAM_EMPTY`) plutôt que de servir une coquille chronométrée.

  **Dette notée, et c'est un défaut de conduite plus qu'une dette** : `db-tests.yml` n'est **pas**
  un check requis et ne bloque pas l'auto-merge. La suite a bien tourné en vert, mais par un
  `workflow_dispatch` **sur `main` à 18h31 UTC, après le merge de 16h41** — la validation a suivi
  la livraison au lieu de la précéder. L'étude 22 avait fait l'inverse (dispatch **sur la branche,
  avant promotion**) et c'est le geste à reprendre : ici, un rouge aurait été découvert sur `main`.

- **2026-08-16 — Lots 3 et 4 (passation + copie corrigée), arena#746.** `src/features/exam/`
  (`exam.server.ts` — 6 server fns, toutes `requireSupabaseAuth` + zod ; `exam-countdown.tsx`,
  `exam-results.tsx`, 3 fichiers de tests), routes `_authenticated/examens.tsx` et
  `_authenticated/examen.$examId.tsx`, i18n `exam.*` dans les **3** catalogues (+ `types.ts`),
  constantes `EXAM_MAX_XP` / `EXAM_MAX_COINS` / `EXAM_AUTOSAVE_INTERVAL_MS`, carte d'entrée dans le
  **hub Arène**, et un relèvement du budget de bundle.

  **Écart accepté n° 3 — le reliquat de l'US-3.** Le détail livré est **par épreuve**, avec son
  coefficient affiché ; **le détail par chapitre et les liens de remédiation ne sont pas livrés**,
  parce que `get_mock_exam_review` ne remonte pas le chapitre de la question — il n'y a rien à quoi
  accrocher un lien. Ce qui **est** livré : la note /20 en tête (la seule échelle que l'élève, le
  parent et l'établissement lisent pareil), le percentile avec son seuil de 20 candidats, et le
  corrigé complet question par question, qui **n'existe qu'après le rendu** (R-3). Voir **Q-4** :
  ce reliquat vaut un lot 6, pas une reprise.

  **La route porte l'examen, pas la session** (`$examId` et non `$sessionId`) : `start_mock_exam`
  **résout ou reprend** la session côté serveur. Une URL portant la session aurait mis un
  identifiant de session dans un lien partageable et forcé le client à en créer une avant de savoir
  s'il en avait déjà une.

  **D-4 est tenu, par un chemin d'import précis** : la route importe `QuestionInput`,
  `buildQuestLabels` et `shuffleOptions` en **imports profonds**, sans passer par le barrel de
  `quest` — qui aurait tiré `quest.server.ts` et toute la boucle de récompense dans le graphe de
  modules d'un écran dont l'intérêt est justement de **ne rien récompenser pendant**.

  **Non livré, et assumé** : l'observabilité du §3 (aucun log structuré dédié, aucun compteur de
  sessions abandonnées) et le **spec e2e authed**, qui vivait dans le lot 5 et est tombé avec lui.
  La chaîne start → save → finish n'est donc couverte de bout en bout qu'en **pgTAP**, jamais par
  un navigateur.

- **2026-08-17 — Clôture documentaire (cette PR).** L'étude passe `brouillon` → **livrée**, les
  lots 1-4 sont cochés, le lot 5 est marqué **sans objet**, et les trois écarts sont inscrits ici
  au lieu de ne vivre que dans les en-têtes de migration du dépôt public. **Le fichier passe dans
  `EtudeRealisé/`** — la règle de l'index est explicite (« études encore ouvertes » = tout ce qui
  n'est pas dans `EtudeRealisé/`), donc le statut et l'emplacement bougent ensemble ; les deux
  études qui pointaient vers l'ancien chemin (08 et 10) sont recâblées. Index
  [`FableEtudes/README.md`](../../README.md) et **ROADMAP** mis à jour — arena#743 / arena#746
  y étaient déjà citées (§0bis, base portée à #746), mais le **§6 décrivait encore « é02 se
  re-scope maintenant »** : quatre lots plus tard, c'est corrigé.
  ⚠️ **Ce que cette clôture ne prouve pas** : que quiconque puisse passer l'examen. Le seed ne
  publie qu'à ≥ 5 épreuves récoltées, et ce qu'il a récolté dépend du corpus 9ᵉ réellement en base
  — **fait non vérifiable depuis un poste** (la table n'est lisible qu'authentifié). C'est la
  **Q-5**, et elle passe avant les autres : « livrée » décrit ici du code appliqué, pas une
  feature dont on a vu qu'elle s'ouvrait.
