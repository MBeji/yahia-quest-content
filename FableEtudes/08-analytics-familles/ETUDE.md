# Étude 08 — Analytics parents & enseignants

> **Statut** : brouillon — **RE-SCOPÉE le 2026-08-24 : son volet parent a été livré hors d'elle.**
> Entre le 2026-08-16 et le 2026-08-23, le rapport parental a reçu un socle de mesure du temps,
> un tableau de bord « jour par jour » (arena#751, #752, #753, #754, #759, #762, #763, #764,
> #769) et les points faibles nommés (arena#818, é04 A2.2) — sans passer par cette étude, et
> sous une spec normative qui lui est propre : `docs/suivi-parental-quotidien.md`. **Six des huit
> US de la version du 2026-07-04 sont livrées ou caduques.** Les re-spécifier serait une
> duplication : §0 fait le tri ligne à ligne et nomme le propriétaire de ce qui est parti.
> **Ce que cette étude garde** : le **canal enseignant** (é28 Q-3 — son nouveau cœur, aucune
> étude nouvelle ouverte, le portefeuille reste resserré é26 KPI-3) et **quatre reliquats
> parent** que personne n'a construits — l'examen blanc au rapport, le digest hebdo enrichi, le
> comparatif de parcours seuillé, et les compétences déclarées maîtrisées que é30 lui délègue.
> ⛔ **PRÉCONDITION (é28 D-5)** : aucune démarche vers un **établissement** avant GAP-024 livré
> et GAP-003 tranché. État au 2026-08-24 : **une moitié de GAP-024 est tombée** — `deleteAccount`
> existe (arena#791), **`export_user_data` reste absent de `src/`**, GAP-003 reste non tranché.
> Ce que D-5 bloque exactement — la prospection, ou aussi la construction — est **Q-4**.
> **Priorité** : 08 · **Valeur** : le seul canal d'acquisition à CAC ≈ 0 du budget réel (é28 M-3 :
> un enseignant qui donne un chapitre en devoir apporte 30 élèves **et** 30 parents), plus les
> quatre trous restants du suivi familial · **Complexité** : moyenne
> **Architecte** : Fable (claude-fable-5), 2026-07-04 · **re-scopage** : Opus 5, 2026-08-24 ·
> **Exécuteur cible** : Sonnet (ou équiv.)
> **Dépend de** : **plus rien côté données pour les lots 1 à 6** — é04 est TERMINÉE (2026-08-23),
> é07 et é02 sont **livrées** (les trois sont passées en `EtudeRealisé/`). Seul le lot 7 attend
> é30 (maîtrise déclarée, son lot 2) · **Bloque** : é30 US-7, qui lui délègue explicitement le
> rapport parent (é30 §2.4)
> **Docs normatifs liés** : `AGENTS.md`, `ARCHITECTURE.md`, **`docs/suivi-parental-quotidien.md`
> — spec normative du volet livré, elle prime sur ce document pour tout ce qui est déjà à
> l'écran**, `STATUS.md` §1bis, é28 (Q-3 / D-5), é30 (§2.4)
> ⚠️ Le wording « ceux qui paient / abonnement » de la version du 2026-07-04 est **supprimé** :
> depuis le pivot du 2026-06-21 l'application est 100 % gratuite et le suivi parent est un
> **pilier de l'offre gratuite**, pas une justification d'abonnement.

---

## 0. Ce qui est déjà livré — et que cette étude ne re-spécifie plus

Cette étude a été écrite le 2026-07-04 pour un rapport parent qui était « un instantané 7 jours ».
Il ne l'est plus. Ce qui suit est **observé sur `main` le 2026-08-24**, pas remémoré : chaque
ligne a été relue dans le code ou la migration citée.

### 0.1 Les huit user stories de la version 2026-07-04

| US   | état observé sur `main` le 2026-08-24 | propriétaire désormais |
| ---- | -------------------------------------- | ---------------------- |
| US-1 | **Livrée et dépassée.** `learning_pulses` (20260816180000) mesure le temps **réel** par surface (`lesson`/`exercise`/`quiz`/`recall`/`dungeon`/`duel`/`browse`), écrêté à l'horloge murale — lire un cours laisse enfin une trace. Temps d'application **et** temps d'apprentissage, distincts, jusqu'à 92 jours, avec la période précédente de même longueur | `docs/suivi-parental-quotidien.md` |
| US-2 | **Livrée pour l'essentiel, sous une autre forme.** Niveau, série en cours, meilleure série et dernière activité sont au rapport ; les séries sont **journalières sur une période choisie** (six périodes prédéfinies + une plage libre), pas hebdomadaires sur 8 semaines. **Seul reliquat réel : aucune série d'XP** — retenu comme non-objectif (§2.2) | idem |
| US-3 | **Livrée et dépassée.** Par matière : minutes, cours, exercices, score moyen, écart avec la période précédente, **couverture du programme** (chapitres terminés / publiés) et **niveau scolaire** — sans lui le bilan listait « Mathématiques » quatre fois (constat prod 2026-08-16). Plus l'analyse `analyzeSubjects` : fortes, négligées, à revoir | idem |
| US-4 | **Livrée dans une autre monnaie, et meilleure.** Pas « top 5 compétences 0–100 » mais : chapitres forts / faibles (`chapterInsights`) **et les erreurs NOMMÉES** avec leur tendance (`misconceptionInsights`, é04 A2.2, arena#818, migration 20260823101000). « Fractions : 45 % » dit OÙ ça coince ; « il additionne les dénominateurs » dit QUOI réviser | é04 (close) — consommé par le rapport |
| US-5 | **NON LIVRÉE — reste ici.** é02 est livrée depuis le 2026-08-16 et `get_mock_exam_percentile` existe, mais **rien n'en remonte au rapport parent** | **cette étude, lot 1** |
| US-6 | **Livrée et très dépassée.** `buildAlerts` rend **12 clés** d'alerte (ton, gravité, paramètres, **cible d'action** — le chapitre à ouvrir), plafonnées à 6, avertissements d'abord, aucun texte en dur : le libellé est monté en i18n FR/EN/AR. Là où cette étude prévoyait 3 règles OR | `docs/suivi-parental-quotidien.md` §9 |
| US-7 | **NON LIVRÉE — reste ici.** `dispatchParentDigest` appelle toujours `weeklyParentDigestPayload()` **sans argument** : le push du dimanche reste le générique « ton rapport est prêt » | **cette étude, lot 2** |
| US-8 | **NON LIVRÉE — reste ici.** Aucun `get_parcours_platform_stats`, aucun comparatif de quelque nature que ce soit | **cette étude, lot 3** |

### 0.2 Les règles et les décisions

| item | sort |
| ---- | ---- |
| R-1  | **Périmée.** Le temps ne se déduit plus de la durée d'`exercise_sessions` bornée à 30 min : il est **mesuré** par les pouls, et l'invariant anti-triche est plus fort (`record_learning_pulse` ne crédite jamais plus de secondes qu'il ne s'en est écoulé). Les 30 min existent toujours, mais comme **seuil de nouvelle session**, ce qui n'est pas le même objet |
| R-2  | **Périmée.** Pas de série hebdomadaire lundi–dimanche sur 8 semaines : période choisie (aujourd'hui → 92 jours), découpée en jours, fuseau `Africa/Tunis`, comparée à la période précédente de même longueur |
| R-3  | **Livrée autrement.** Les seuils de non-diagnostic existent — une tendance reste `stable` sous 3 occurrences, un facteur non mesuré est **retiré du calcul** et les poids renormalisés (jamais compté zéro) |
| R-4  | **Périmée.** Remplacée par les 12 alertes de `buildAlerts` (§0.1, US-6) |
| R-5  | **Toujours en vigueur** — « moyenne nationale » reste interdite. Rien ne l'a encore mise à l'épreuve : le comparatif n'existe pas |
| R-6  | **Toujours en vigueur** (seuil N ≥ 30 sur un comparatif plateforme) — s'applique au lot 3 |
| R-7  | **Toujours en vigueur** — s'applique au lot 2 |
| R-8  | **Tenue côté élève non lié** (les RPC vérifient le lien), mais **une décision produit postérieure la nuance** : le 2026-08-16, le tableau de bord entier a été ouvert au **porteur du code alliance** sur `/suivi`, réponses de l'enfant comprises. C'est un accès au porteur **assumé** (122 bits, transmis par l'élève). Cette étude n'y revient pas — elle en **hérite**, comme elle héritait de la Q-2 de é04 |
| D-1  | **Confirmée par la livraison** : tout est allé dans `src/features/parent-report/`, aucune feature `analytics/`. Voir D-10 pour le canal enseignant, qui est un autre guard |
| D-2  | **Confirmée par la livraison** : `get_student_daily_report`, `get_student_attempt_detail` et `student_parcours_progress` sont des RPC SQL `SECURITY DEFINER` qui vérifient le lien en tête. Aucune agrégation TS |
| D-3  | **Toujours ouverte** — le comparatif honnête n'existe pas encore (lot 3) |
| D-4  | **Livrée** : le décrochage est une heuristique lisible, aucun ML, règles pures et testées ligne à ligne |
| D-5  | **Livrée à deux maillons sur trois.** Le repli chapitre existe, l'étage « erreur nommée » existe. Le maillon `competency` (`user_competency_mastery`, migration 20260721100000) **n'est lu par aucune feature** — et il ne le sera pas sous cette forme : é30 remplace le pourcentage moyen par la **maîtrise déclarée avec sa preuve**, et délègue son affichage ici (lot 7) |
| D-6  | **Toujours ouverte** — le digest passe toujours par le canal existant, mais son contenu n'a pas bougé (lot 2) |

### 0.3 Le plan de lots du 2026-07-04

- ~~Lot 1 — RPC agrégats + pgTAP~~ : **livré autrement**. `get_student_daily_report` couvre les
  séries, les matières et le décrochage ; les faiblesses viennent de `get_my_weaknesses` et de
  `_student_report_json`. Restent inconstruits les deux RPC d'examen et de résumé de digest.
- ~~Lot 2 — page rapport enrichie~~ : **livré** (arena#752 → #769), avec deux surfaces au lieu
  d'une (`/parent-report` connecté et `/suivi` par code) et un onglet dédié.
- **Lot 3 — digest hebdo opt-in** : intact, personne n'y a touché → devient le **lot 2** ci-dessous.
- **Lot 4 — comparatifs plateforme** : intact → devient le **lot 3** ci-dessous.

### 0.4 La règle que cette étude s'impose désormais

**Ce document ne décrit plus rien de ce qui est à l'écran.** Pour le tableau de bord parental
livré, la source de vérité est `docs/suivi-parental-quotidien.md` dans le dépôt du moteur ; s'en
écarter ici créerait deux specs pour un seul écran, et la seconde serait fausse la semaine
suivante. Cette étude ne décrit que ce qui **n'existe pas** — et **les numéros ne sont jamais
recyclés** : un `US-n`, un `R-n` ou un `D-n` désigne la même chose dans toutes les versions de ce
fichier, qu'il soit livré, périmé ou à faire.

---

## 1. Contexte & objectif produit

Deux chantiers, un seul document, parce qu'ils partagent la même donnée et la même famille de guards.

**Volet A — le canal enseignant (le cœur).** L'étude 28 a mesuré, le 2026-08-13, qu'il n'existe
**aucun canal d'acquisition actif**, et que celui-ci est le seul dont le coût d'acquisition est
quasi nul au budget réel : un enseignant qui donne un chapitre en devoir amène sa classe entière,
donc autant de familles. Le produit n'a aujourd'hui **rien** pour lui — `profiles.role` vaut
`student`, `parent` ou `admin`, et la seule porte « Je suis enseignant » de la page d'accueil mène
à `/programme`, c'est-à-dire à des cours imprimables. Objectif : classe, code, liste, taux de
réussite par chapitre. Rien de plus (é28 Q-3, mot pour mot).

**Volet B — les quatre trous du suivi familial.** Le rapport parent est riche ; il lui manque
exactement quatre choses, toutes indépendantes et toutes petites : l'examen blanc qu'il ne montre
pas alors qu'il existe, le digest dominical resté générique, le comparatif qui n'a jamais été
construit, et les compétences maîtrisées que é30 lui délègue.

**KPI** — mesurables, et aucun ne parle d'argent (phase gratuite) :

1. **classes actives** et **élèves entrés par un code de classe** — le seul chiffre qui dise si le
   canal M-3 fonctionne ; à comparer aux inscriptions par tout autre chemin.
2. **parents liés dérivés d'une classe** — la conversion réelle du « 30 élèves ⇒ 30 parents ».
3. **% de parents liés ouvrant le rapport ≥ 1×/semaine** — déjà mesurable, jamais publié.
4. **taux d'opt-in au digest enrichi**, et taux de coupure après le premier envoi : un digest
   qu'on coupe est un digest raté.

**Non-objectifs** : prédiction (« score au concours »), prescription pédagogique (é04, puis é30),
export de données pour l'enseignant, vue par élève dans le tableau de classe (§2.5), et toute
re-spécification du tableau de bord livré (§0.4).

## 2. Spécification fonctionnelle

### 2.1 Volet A — le canal enseignant

**Acteurs** : **enseignant** = un compte ordinaire qui possède au moins une classe (D-7) ;
**élève** qui rejoint ; **parent lié**, informé, jamais sollicité. Aucun nouveau rôle.

- **US-9** : enseignant — je crée une **classe** (nom libre, niveau, matière) et j'obtiens un
  **code de classe** court, que j'écris au tableau. Je peux le **régénérer** et **retirer** un
  membre.
- **US-10** : élève — je rejoins une classe avec ce code depuis mon tableau de bord ; l'écran me
  dit **exactement** ce que l'enseignant verra et ce qu'il ne verra pas ; je peux **quitter** en
  un geste, au même endroit.
- **US-11** : enseignant — je vois la **liste** de ma classe : prénom d'affichage, date d'entrée,
  activité récente (actif cette semaine / pas actif). Rien de plus nominatif que ce que le
  classement affiche déjà.
- **US-12** : enseignant — je vois le **taux de réussite par chapitre** du programme de la
  matière, avec l'effectif qui l'a travaillé et la part de la classe qui l'a terminé. C'est le
  livrable : ce qui est compris, ce qui est à reprendre en cours.
- **US-13** : enseignant — je **donne un chapitre en devoir** avec une échéance ; la classe le
  voit sur son tableau de bord ; le mien me dit combien l'ont terminé. _(Q-5 : v1 ou v2.)_
- **US-14** : enseignant — j'obtiens un **message prêt à copier** pour les familles, qui explique
  ce que le parent verra et où trouver le code alliance de son enfant. Le canal parent existe
  déjà : cette US ne fait que l'ouvrir.

### 2.2 Volet B — les quatre reliquats parent

- **US-5** _(inchangée depuis 2026-07-04)_ : parent — si mon enfant a passé des examens blancs,
  je vois score et **percentile** par examen, aux règles d'affichage de é02 (seuil N ≥ 20).
- **US-7** _(inchangée)_ : parent — j'active (opt-in) le **digest hebdo** : le push du dimanche
  contient le résumé chiffré de la semaine (temps, missions, série, 1 point faible) au lieu du
  générique.
- **US-8** _(inchangée)_ : parent — je situe mon enfant par rapport à la **moyenne de la
  plateforme sur ce parcours** (score moyen, temps hebdo) — agrégat anonymisé, masqué sous N < 30.
- **US-15** _(nouvelle, déléguée par é30 §2.4)_ : parent — le rapport nomme les **compétences
  déclarées maîtrisées**, avec leur preuve (« prouvé 4 fois, sous 3 formes »), **jamais** un
  pourcentage moyen. é30 produit la lecture ; cette étude l'affiche.

**Retiré du périmètre, en connaissance de cause** : la série d'XP hebdomadaire sur 8 semaines
(reliquat de US-2). L'écran répond déjà à « est-ce qu'il progresse ? » par l'écart de score avec
la période précédente, qui est la question réelle du parent ; une courbe d'XP mesurerait surtout
la générosité du barème (é09), pas l'enfant.

### 2.3 Règles métier

Les règles **R-5, R-6, R-7 et R-8** de la version 2026-07-04 restent en vigueur telles quelles
(§0.2). S'y ajoutent, pour le canal enseignant :

- **R-9 — un code de classe n'est pas un code alliance.** Il ouvre un **agrégat de classe** et la
  liste de ses membres. Jamais le rapport d'un élève, jamais ses réponses, jamais son temps minute
  par minute, jamais le détail d'une tentative. Rejoindre une classe ne donne aucun droit sur
  l'enfant à qui que ce soit.
- **R-10 — le lien va dans un seul sens : l'élève rejoint.** Un enseignant ne peut pas faire
  entrer un mineur dans son tableau par un geste à lui seul. Corollaire : la mécanique du code
  alliance n'est **pas** réutilisable telle quelle — elle va dans l'autre sens, et demander son
  code à trente élèves donnerait à l'enseignant trente capacités au porteur sur trente enfants.
- **R-11 — seuil d'agrégat de classe : 5.** Un taux par chapitre ne s'affiche qu'à partir de
  **5 élèves** l'ayant travaillé ; en deçà, « pas encore assez d'élèves ». Sous ce seuil, un
  pourcentage désigne un enfant. _(Distinct de R-6, qui vaut pour la plateforme entière.)_
- **R-12 — aucune donnée nouvelle n'est révélée** par l'entrée dans une classe : le nom affiché
  est le prénom d'affichage déjà public au classement.
- **R-13 — sortie en un geste.** L'élève, ou son parent lié, quitte la classe depuis l'écran où il
  l'a rejointe ; ses données sortent des agrégats au calcul suivant. Aucune confirmation par
  l'enseignant.
- **R-14 — le taux de réussite d'un chapitre réutilise la règle qui fait déjà autorité**
  (`student_parcours_progress`, migration 20260816200000 : mission réussie à 60 % en variante
  classique, quiz de compréhension à 80 % en scolaire). **Aucune seconde définition** de
  « chapitre réussi » n'est écrite — c'est exactement la dette que cette migration a soldée.

### 2.4 i18n

Toutes les nouvelles clés en FR/EN/AR ; le tableau de classe est lisible en RTL — un
prénom et un pourcentage dans la même phrase forment **un seul nœud de texte**
(`docs/design-surfaces.md`).

### 2.5 Hors périmètre (v1)

- **La vue par élève dans le tableau de classe.** é28 Q-3 dit « code de classe, liste d'élèves,
  taux de réussite par chapitre » — trois choses. Un enseignant qui veut le détail d'un enfant
  demande à la famille : le canal existe, c'est le code alliance, et il appartient à l'élève.
- Export de données pour l'enseignant (CSV/PDF) ; notation ; messagerie enseignant ↔ élève.
- Toute re-spécification du tableau de bord parental livré (§0.4).
- La **prédiction du score au concours** — v2, toujours gelée, toujours faute de volume.
- Le **démarchage d'établissement** : é28 D-5, précondition dure, indépendante de ce document.

## 3. Architecture technique (décisions fermées)

Les décisions **D-1, D-2, D-3, D-4 et D-6** restent celles du 2026-07-04 (§0.2). S'y ajoutent :

- **D-7 — pas de rôle `teacher`.** La capacité vient de la **propriété d'une classe**
  (`classrooms.owner_user_id`), pas de `profiles.role`. Rejeté : ajouter un rôle — il faudrait
  altérer le CHECK de `20260522153000_family_content_rewards.sql`, re-trancher chaque policy qui
  teste le rôle, et un enseignant est de toute façon souvent **aussi** un parent sur le même
  compte : un rôle unique le forcerait à choisir.
- **D-8 — le code de classe est une clé propre, courte et révocable.** 8 caractères d'un alphabet
  sans ambiguïté (ni `O`/`0`, ni `I`/`1`), tiré aléatoirement, unique, régénérable. Rejeté :
  réutiliser le code alliance (R-10). Un code qui circule ne fait entrer que du bruit dans un
  agrégat — jamais sortir de la donnée — et se répare par régénération + retrait du membre.
- **D-9 — les agrégats de classe sont des RPC `SECURITY DEFINER` qui vérifient la propriété en
  tête**, même patron que les RPC parent (D-2, confirmé par la livraison). Le taux par chapitre
  **appelle `student_parcours_progress`** pour chaque membre et agrège : une seule définition de
  « chapitre réussi » dans tout le produit (R-14).
- **D-10 — le canal enseignant est une feature à part, `src/features/classroom/`.** D-1 rejetait
  une feature `analytics/` parce qu'elle **dupliquait** le guard parent ; ici le guard est
  différent (propriété de classe vs lien famille) et le payload aussi (agrégat vs individuel).
  Les mélanger est précisément RISK-5. `parent-report/` reste au parent.

**Modèle de données** (additif, GRANTs explicites — gotcha `AGENTS.md`) :

```sql
CREATE TABLE public.classrooms (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  owner_user_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
  name          TEXT NOT NULL,
  grade_id      UUID REFERENCES public.grades(id),
  subject_id    TEXT REFERENCES public.subjects(id),
  join_code     TEXT NOT NULL UNIQUE,          -- 8 car., alphabet sans ambiguïté (D-8)
  created_at    TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE public.classroom_members (
  classroom_id UUID NOT NULL REFERENCES public.classrooms(id) ON DELETE CASCADE,
  student_id   UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
  joined_at    TIMESTAMPTZ NOT NULL DEFAULT now(),
  PRIMARY KEY (classroom_id, student_id)
);
-- RLS : l'enseignant lit/écrit SES classes ; l'élève lit/supprime SA ligne (R-13).
-- GRANT SELECT/INSERT/UPDATE/DELETE explicites à `authenticated` — sans quoi la
-- suite pgTAP casse sur une base VIERGE (gotcha AGENTS.md).

CREATE TABLE public.parent_digest_prefs (      -- lot 2, opt-in digest (R-7)
  parent_user_id  UUID PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,
  enriched_digest BOOLEAN NOT NULL DEFAULT false,
  updated_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);
-- RLS owner-only ; lecture par le cron en service-role.
```

**Server** — toutes read-only sauf mention, `SECURITY DEFINER`, `REVOKE anon` :

- `create_classroom` / `regenerate_join_code` / `remove_classroom_member` (écriture, propriétaire).
- `join_classroom(p_code text)` / `leave_classroom(p_classroom uuid)` (écriture, élève — R-10/R-13).
- `get_classroom_roster(p_classroom uuid)` : la liste (US-11, R-12).
- `get_classroom_chapter_stats(p_classroom uuid)` : taux par chapitre, seuillé (US-12, R-11, R-14).
- `get_student_exam_summary(p_student uuid)` : scores + percentiles, réutilise
  `get_mock_exam_percentile` de é02 ; rend vide si l'élève n'a passé aucun examen (lot 1).
- `get_parcours_platform_stats(p_parcours text)` : moyennes anonymes seuillées, `STABLE` (lot 3).
- `get_parent_digest_summary(p_parent uuid)` : résumé compact par élève lié, appelé par le cron
  en service-role (lot 2, D-6 — aucun nouveau cron, même `CRON_SECRET`, même planning).

Server fns zod correspondantes, mêmes patrons `failWithClientError` et schémas `.catch()` que
l'existant ; `setDigestPref` rate-limité comme `setStudentWeeklyGoal`.

**Client** : `src/features/classroom/` (barrel, `classroom.server.ts`, composants, `__tests__/`) et
une route authentifiée dédiée ; côté parent, trois sections ajoutées à `ReportContent` (examens,
comparatif, compétences maîtrisées) et un interrupteur de digest. États vides / erreur **par
section** : une section qui échoue ne casse pas la page — c'est déjà la posture de l'écran.
**Observabilité** : logs structurés par RPC (durée, comparatif masqué/affiché, seuil R-11
déclenché), compteur de digests enrichis envoyés/refusés, compteur d'entrées par code de classe —
KPI-1 et KPI-2 ne se mesurent pas autrement.

## 4. Plan d'exécution en lots

Les lots 1 à 3 sont **indépendants, déjà débloqués et utiles seuls** : ils ferment les trous du
volet parent sans rien attendre. Le volet A commence au lot 4, après Q-4.

| lot | contenu (résumé) | fichiers/objets créés | tests exigés | dépend de |
| --- | ---------------- | --------------------- | ------------ | --------- |
| 1 | Examens blancs au rapport (US-5) | RPC `get_student_exam_summary` + section UI | pgTAP : accès (parent lié / non lié / anon), vide sans examen ; Vitest UI | — (é02 livrée) |
| 2 | Digest hebdo enrichi opt-in (US-7, R-7, D-6) | `parent_digest_prefs`, RPC résumé, cron étendu | Vitest cron : opt-in respecté, payload, repli générique, VAPID absent | — |
| 3 | Comparatif de parcours seuillé (US-8, R-5, R-6, D-3) | RPC `get_parcours_platform_stats` + section UI | pgTAP : seuil 29 vs 30, anonymat ; Vitest : libellé R-5 | — |
| 4 | Classes, code, adhésion, sortie (US-9, US-10, R-9→R-13, D-7, D-8) | 1 migration (2 tables, RLS, grants) + RPC d'écriture | pgTAP : matrice d'accès, sens du lien, sortie, code régénéré | **Q-4 tranchée** |
| 5 | Liste + taux de réussite par chapitre (US-11, US-12, R-11, R-14, D-9, D-10) | feature `classroom/` + 2 RPC + route | pgTAP : seuil R-11, égalité avec `student_parcours_progress` ; Vitest UI, RTL | 4 |
| 6 | Le devoir + l'invitation des familles (US-13, US-14) | table `classroom_assignments` + UI élève/enseignant | pgTAP : échéance, visibilité ; Vitest : compteur de rendus | 5 · **Q-5** |
| 7 | Compétences déclarées maîtrisées au rapport (US-15) | section UI consommant les lectures de é30 | Vitest : preuve affichée, jamais de pourcentage moyen | **é30 lot 2** |

- [ ] Lot 1 — examens blancs au rapport
- [ ] Lot 2 — digest hebdo enrichi opt-in
- [ ] Lot 3 — comparatif de parcours seuillé
- [ ] Lot 4 — classes, code, adhésion
- [ ] Lot 5 — liste + taux par chapitre
- [ ] Lot 6 — devoir + invitation des familles _(sous réserve Q-5)_
- [ ] Lot 7 — compétences déclarées maîtrisées _(après é30 lot 2)_

**Stop-points** — un lot qui les franchit est à refuser en revue : aucun lot ne modifie
`get_student_daily_report`, `get_student_report` ni `student_parcours_progress` (le tableau de
bord livré ne bouge pas) ; aucun payload de classe ne contient un champ par élève autre que les
trois de US-11 (R-9) ; aucun écran n'affiche « moyenne nationale » (R-5) ; aucun lot n'écrit une
seconde définition de « chapitre réussi » (R-14) ; aucun lot n'ouvre de surface publique
d'inscription « enseignant » tant que Q-4 n'est pas tranchée.

## 5. Stratégie de test

**pgTAP porte la sécurité**, comme au volet parent. Matrice d'accès sur chaque RPC de classe :
propriétaire / autre enseignant / élève membre / élève non membre / parent lié / anonyme — et
l'assertion qui compte : **aucun chemin ne rend de donnée individuelle au-delà de US-11** (R-9).
Puis : le sens du lien (R-10 — un `INSERT` d'enseignant dans `classroom_members` échoue), la
sortie (R-13), le code régénéré qui invalide l'ancien, le seuil R-11 à 4 vs 5 élèves, et
l'**égalité stricte** entre le taux de classe et la somme des `student_parcours_progress` de ses
membres (R-14). Côté volet B : seuil R-6 à 29 vs 30, et absence de toute donnée individuelle dans
l'agrégat plateforme.

**Vitest** co-localisés : schémas zod `.catch()`, sections vides / pleines / en erreur isolée,
RTL, cron digest (opt-in, payload, repli générique). **Non-régression** : les suites existantes
`parent-report.test.ts`, `insights.test.ts`, `alerts.test.ts`, `parent-report-daily.test.ts`,
`daily-insights.test.tsx` et `notifications.cron.test.ts` restent vertes **sans modification de
leurs assertions** — si l'une bouge, c'est que le lot a touché le tableau de bord livré, ce
qu'aucun n'a le droit de faire. Pas d'impact `smoke:shell` (routes authentifiées) ; e2e non requis
en v1.

## 6. Risques & mitigations

- **RISK-1** Mésusage du comparatif — pression parentale, lecture « classement » (probable/moyen)
  → R-5/R-6 : libellé honnête, agrégat seuillé, jamais de rang individuel ; encart « chaque élève
  progresse à son rythme ». Le canal enseignant ajoute la même tentation à l'échelle de la classe :
  R-11 y répond.
- **RISK-5** **Le tableau de classe recrée un rapport parent au rabais** (probable / **élevé** —
  c'est le risque principal de cette étude) → R-9 + D-10, et un critère de revue explicite : **tout
  champ par élève dans un payload de classe est un signal d'alarme**, hors les trois de US-11. Un
  enseignant qui voit le détail d'un enfant sans que la famille l'ait voulu est une faute, pas une
  fonctionnalité.
- **RISK-6** Un code de classe qui circule — élève d'un autre établissement qui rejoint
  (possible/faible) → un intrus ne **lit** rien : il ne fait qu'entrer du bruit dans un agrégat.
  Régénération du code, retrait du membre et seuil R-11 suffisent ; pas de validation manuelle, qui
  ferait de l'enseignant un modérateur.
- **RISK-7** **Construire le canal avant le verrou légal** (certain si Q-4 n'est pas tranchée) →
  l'ordre des lots met le volet B d'abord ; le volet A ne démarre pas sans Q-4, et
  `export_user_data` reste absent de `src/` au 2026-08-24.
- **RISK-8** Données creuses au lancement — une classe de 3, un parcours à 12 élèves
  (certain/faible) → R-6 et R-11 : états vides explicites, aucun chiffre sous le seuil. Le tableau
  de classe reste utile avec la seule liste (US-11).
- **RISK-9** **Duplication de spec** — ce document et `docs/suivi-parental-quotidien.md` divergent
  (probable/moyen : **c'est déjà arrivé une fois, et c'est ce que ce re-scopage répare**) → §0.4 :
  ce document ne décrit que l'inexistant ; toute règle sur l'écran livré s'écrit là-bas.

## 7. Questions ouvertes (pour l'humain)

- **Q-1** _(2026-07-04, toujours ouverte)_ : le digest enrichi est-il opt-in désactivé par défaut,
  ou activé pour les parents déjà destinataires du générique ? **Recommandation** : désactivé, et
  proposé en un clic dans le rapport — un push enrichi non demandé est le meilleur moyen de faire
  couper les notifications.
- **Q-2** — ~~rôle enseignant reporté en v2~~ **RÉPONDUE le 2026-08-13 (é28 Q-3)** : le canal
  enseignant revient à cette étude, sans étude nouvelle. Et il n'y a **pas** de rôle à créer (D-7).
- **Q-3** — ~~seuils R-3 / R-4~~ **CADUQUE** : ces seuils vivent désormais dans
  `docs/suivi-parental-quotidien.md` et dans `src/features/parent-report/insights/`.
- **Q-4** _(nouvelle)_ : **é28 D-5 bloque-t-il la construction du canal enseignant, ou seulement la
  prospection d'établissement ?** Le texte dit « aucune **démarche** vers un établissement ».
  **Recommandation** : la précondition porte sur la prospection ; les lots 4-5 peuvent se
  construire, mais **aucune surface publique d'inscription enseignant** ne s'ouvre tant que
  `export_user_data` manque — un enseignant qui fait entrer 30 mineurs alors que le produit ne sait
  pas exporter leurs données, c'est la moitié du verrou légal qui manque au pire moment.
- **Q-5** _(nouvelle)_ : le **devoir** (US-13) est-il dans la v1 ? C'est le geste que é28 M-3 décrit
  comme le déclencheur de l'acquisition — mais c'est aussi le lot le plus lourd.
  **Recommandation** : v1, **après** avoir vu une classe réelle vivre avec les lots 4-5.
- **Q-6** _(nouvelle)_ : le seuil R-11 (5 élèves) est-il le bon ? Une classe tunisienne compte
  25-35 élèves, mais toutes ne rejoindront pas. **Recommandation** : 5, ajustable — constante
  centralisée, comme les seuils du volet parent.

## 8. Journal d'exécution

| date | lot | PR | note |
| ---- | --- | -- | ---- |
| 2026-08-24 | — | — | **Re-scopage, aucun code écrit.** Le volet parent ayant été livré hors de cette étude (arena#751 → #769, puis #818), six des huit US sont livrées ou périmées : §0 fait le tri ligne à ligne et renvoie à `docs/suivi-parental-quotidien.md`, qui devient la spec de l'écran. Le canal enseignant (é28 Q-3) devient le cœur du document ; quatre reliquats parent restent, dont **trois immédiatement exécutables** (é02, é04 et é07 étant toutes livrées). Q-2 et Q-3 sont closes, Q-4 à Q-6 ouvertes. |
