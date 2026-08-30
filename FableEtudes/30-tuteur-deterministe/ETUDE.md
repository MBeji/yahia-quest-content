# Étude 30 — Le tuteur déterministe : porter le moteur adaptatif au rang des références (ALEKS · Squirrel AI · CENTURY)

> **Statut** : **validée** — Q-1…Q-7 arbitrées le 2026-08-23 par Mohamed (§7 ; **deux contre la
> recommandation** : Q-5 et Q-6, l'étude est réécrite en conséquence). **Lot 0 LIVRÉ** (C4bis,
> privé #219, appliqué en prod le 2026-08-23). **Révisée le 2026-08-25** sur mandat de Mohamed
> (« améliorer et optimiser », é04 **et é11 livrées**) : l'articulation é11 passe du futur au
> **mesuré** (§1.2bis, §3.13), l'amendement D devient un lot exécutable (**3bis** — le pack du
> tuteur apprend la maîtrise), le poids du mini-check est re-spécifié sur la couture **réelle**
> (§3.2), et le sélecteur vise la ZPD calculée (§3.4). **Aucun arbitrage n'est rouvert.**
> **PÉRIMÈTRE RETENU LIVRÉ EN ENTIER le 2026-08-25** (0bis · 1 · 2 · 3 · 3bis · 4 — arena#856,
> #857, #858, #859, #860 ; contenu privé #241). Journal, écarts et dettes au **§8**, qui fait foi
> sur ce qui a été mesuré. Les lots 5 à 9 restent **différés**, pas
> gelés (Q-7). Prête à exécuter, lot 0bis en premier.
> **Priorité** : 30 · **Valeur** : le produit sait déjà _si_ l'élève a raté et _à quel point_ une
> compétence est faible ; il ne sait pas **ce qu'il croit**, **ce qu'il peut en déduire**, ni **quoi
> servir ensuite**. Cette étude ferme les quatre organes manquants d'un système tutoriel
> intelligent — croyance calibrée, inférence dans le graphe, diagnostic d'entrée, prochaine
> meilleure action — et les rend **tous déterministes**, donc vivants sans clé d'IA ·
> **Complexité** : très haute (transverse DB + moteur + corpus)
> **Architecte** : Opus 5 (claude-opus-5), 2026-08-22 · **Révision** : session Claude du
> 2026-08-25 (mêmes six mécanismes, état re-mesuré) · **Exécuteur cible** : Sonnet (ou équiv.)
> **Dépend de** : **é04 — TERMINÉE le 2026-08-23** (les quatre phases A0/A1.1/A1.2/A2 closes,
> arena#818 ayant livré « Tes points faibles » élève + parent ; l'étude est passée en
> `EtudeRealisé/`, privé #223). É30 ne prolonge donc pas une étude en cours : elle **reprend là
> où é04 s'arrête** — é04 modélise _quelle erreur tu fais_, é30 modélise _ce que tu maîtrises et
> ce que tu es prêt à apprendre_. · é07 lots 1/2/4/5 ✅ (graphe, maîtrise
> EWMA, RPCs de lecture, plan compétence-aware) · é22 ✅ (parcours, `resolveNextAction`) ·
> **et d'un chantier de contenu hors de ce périmètre** : C4bis (tagging des distracteurs) et
> l'extension du registre de compétences hors `math` — §6 RISK-1
> **Bloque** : rien de démarré ; **fournit** à é11 (tuteur IA — **LIVRÉE, 8 lots, 2026-08-24**,
> constaté sur `main` : `20260824120000_tutor_digests` + `20260824130000_tutor_energy_console`,
> branche `claude/etude-11-lots-6-7`, #844) la ligne de maîtrise que son pack **n'a toujours
> pas** — `get_tutor_learner_context` re-mesuré le 2026-08-25 : classe, âge, objectif, série,
> misconceptions actives, intérêts, verbosité, **zéro maîtrise** ; c'est le lot **3bis** —, à
> é08 (rapport parent/enseignant) la maîtrise déclarable, à é02 (examen blanc) le percentile
> par compétence
> **Docs normatifs liés** : AGENTS.md · ARCHITECTURE.md · STATUS.md §1bis (scorecard é28) ·
> é26 (doctrine verticale — **P-5a gouverne cette étude**) · é04 §9 (correction riche, décisions
> fermées) · é07 (R-1…R-6, non rouvertes) · é22 (« carte honnête, pas de faux verrou ») ·
> é29 (la porte IA — **livrée**, dossier en `EtudeRealisé/`) · `docs/content-generation-pipeline.md`

---

## 1. Contexte & objectif produit

### 1.1 La commande humaine (mandat du 2026-08-22)

Mohamed demande que la plateforme atteigne le niveau méthodologique des trois références
citées — **Squirrel AI** (Chine), **ALEKS** (McGraw-Hill, États-Unis), **CENTURY Tech**
(Royaume-Uni) — sur six mécanismes, repris ici comme cahier des charges :

1. **cartographie atomique du savoir** — micro-compétences, dépendances strictes, niveaux
   d'objectifs, batterie d'activités graduées ;
2. **diagnostic initial adaptatif** — situer sans faire passer tout le programme : déduire les
   prérequis d'une réussite complexe, isoler immédiatement la lacune d'un échec de base ;
3. **suivi dynamique de la maîtrise** — recalculer après chaque réponse, en tenant compte de
   **la faute d'inattention** et de **la bonne réponse due au hasard** ; ne déclarer « maîtrisé »
   qu'après validation **répétée et variée** ;
4. **moteur de décision (ZPD)** — la prochaine meilleure action : monter, varier le format, ou
   déclencher une **boucle de remédiation qui remonte la chaîne des prérequis** ;
5. **guidage socratique & échafaudage** — jamais la solution brute ; trois paliers (question
   réflexive → règle/analogie → décomposition) ; ton adapté ;
6. **gestion du rythme et de la charge cognitive** — détecter surcharge et fatigue (latence
   anormale, hésitations, série d'erreurs inhabituelle) et réagir.

Cadre théorique posé par le mandat : Bloom (mastery learning), Vygotsky (ZPD), Bruner
(échafaudage), Sweller (charge cognitive).

**Ce que cette étude fait de ce mandat.** Elle le prend en entier, et elle en **traduit** cinq
points sur six en mécanique déterministe spécifiée ici. Le sixième — le **ton** et la
**formulation** du guidage socratique (point 5, second alinéa) — n'est pas de son ressort : il
appartient à l'étude 11, derrière la porte de l'étude 29. Cette étude lui livre l'échafaudage
**écrit**, qui fonctionne sans clé ; é11 — **livrée depuis le 2026-08-24** — lui ajoute la voix.
C'est la doctrine é26 P-5b, pas un renoncement : **le déterministe décide, le LLM parle.**

**Le mandat a été réitéré le 2026-08-25** (« améliorer et optimiser l'étude 30, sachant é04 et
é11 implémentées, pour que la plateforme atteigne le niveau des trois références ») — mêmes six
mécanismes, même cadre théorique. La présente révision n'y répond pas en ajoutant des organes :
elle **re-mesure** l'état (§1.2bis), branche le tuteur livré sur la charpente (lot 3bis) et
resserre deux coutures que la livraison de é11 a déplacées. Un fait mesuré cadre tout le reste :
**aucune clé de fournisseur n'a jamais été branchée** (STATUS, 2026-08-24 — le pilote Q-9 de é29
n'a pas commencé). Autrement dit, l'intelligence que reçoivent **100 % des élèves aujourd'hui**
est la déterministe — celle qui fait la réputation des trois références, et celle de cette
étude. É11 n'y change rien tant qu'une famille n'apporte pas sa clé : la charpente é30 n'est pas
un complément du tuteur, elle est **le produit**.

### 1.2 L'état réel, mesuré dans le code et le corpus le 2026-08-22

Rien de ce qui suit n'est de mémoire. Chaque ligne a été relue dans `main` (moteur) et sur
`origin/main` (corpus) le jour de la rédaction.

**Ce qui existe déjà, et qui est en avance sur sa réputation :**

| Organe                     | Où                                                                                 | État vérifié                                                                                                                                                                                                                 |
| -------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Télémétrie par question    | `question_attempts` (é04 A0.1)                                                     | ✅ (élève, question, chapitre, **session**, choix, correct, tag résolu à l'insert, source) — append-only, écriture RPC seule                                                                                                 |
| Erreur nommée par option   | `questions.distractor_tags` JSONB **serveur seul**                                 | ✅ colonne + `REVOKE SELECT` ; **0 valeur dans le corpus**                                                                                                                                                                   |
| Registre des erreurs       | `content/misconceptions.json`                                                      | ✅ **56 entrées, 56 pourvues de `competency`** (mesuré)                                                                                                                                                                      |
| Graphe de compétences      | `competencies` / `competency_prereqs` / `question_competencies`                    | ✅ **62 compétences, 80 arêtes, 11 domaines, profondeur 6, 5 racines, 1,29 prérequis en moyenne, max 3 directs, fan-out max 7** (mesuré sur `content/competences/math.json` ; STATUS.md dit encore 59 — écart signalé au §8) |
| Maîtrise par compétence    | `user_competency_mastery` (é07 lot 2)                                              | ✅ EWMA `m ← m + α(r − m)`, α = .15/.20/.25/.30 selon le palier de difficulté, init 50, **oubli à la lecture** (−1 pt/semaine, plancher 30)                                                                                  |
| Lectures du graphe         | `get_my_competency_map`, `get_competency_blockers`, `get_exercises_for_competency` | ✅ (é07 lot 4)                                                                                                                                                                                                               |
| Ordonnanceur quotidien     | `get_daily_plan`                                                                   | ✅ score = retard SM-2 (0→1) + 0,5 × poids misconceptions + 0,5 × faiblesse de compétence, **plafond 3**                                                                                                                     |
| Répétition espacée         | `spaced_repetition_schedule`                                                       | ✅ paliers 1/3/7 j, boucle refermée à la réussite (é22 lot 2)                                                                                                                                                                |
| Correction riche à l'échec | `get_attempt_review` (é04 A1.2)                                                    | ✅ erreur nommée + « revoir le cours » + « m'entraîner »                                                                                                                                                                     |
| Types d'items              | `questions.question_type`                                                          | ✅ **6 natifs** : `mcq`, `numeric`, `ordering`, `matching`, `multi`, `short_answer` + la **variante rappel** (é17, saisie libre)                                                                                             |
| Porte d'accès              | `resolve_exercise_access`                                                          | ✅ arbitre unique, jamais contourné                                                                                                                                                                                          |

**Ce qui manque, et qui est exactement le mandat** — ⚠️ **la première ligne de ce tableau n'est
plus vraie depuis le 2026-08-23** : C4bis a été livré le soir de la rédaction puis appliqué en
prod. Le reste du tableau tient. Le §8 dit ce qui a changé, et ce que ça n'a **pas** réglé :

| Manque (mesuré)                                                                                                                                                                                  | Conséquence                                                                                           | Point du mandat |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------- | --------------- |
| **0 occurrence de `misconceptionTag` sur 22 146 questions** (re-mesuré ici sur tout `content/`)                                                                                                  | tout l'étage « erreur nommée » est alimenté par du vide                                               | 2, 4            |
| Compétences taggées sur **`math` (9ᵉ) et `math-6eme` seulement** — 234 fichiers, ~2 matières sur 90                                                                                              | le graphe n'éclaire que deux matières                                                                 | 1               |
| **Aucun modèle de croyance** : l'EWMA traite toute erreur comme une preuve pleine                                                                                                                | ni inattention, ni hasard ; un QCM à 4 options réussi au hasard pèse autant qu'une saisie libre juste | **3**           |
| **Aucune inférence dans le graphe** : réussir une compétence avancée n'apprend rien sur ses prérequis                                                                                            | il faut tout jouer pour tout savoir                                                                   | **2**           |
| **Aucun diagnostic d'entrée** : tout élève démarre à 50 partout                                                                                                                                  | la première semaine est aveugle                                                                       | **2**           |
| **Aucune autorité de séquencement à l'item** : `computeNextExerciseId` trie par `display_order` ; un exercice est servi et soumis **en bloc**                                                    | pas de « prochaine meilleure action »                                                                 | **4**           |
| **Aucun échafaudage** : le seul secours est `consume_hint`, qui révèle **l'explication entière** contre un consommable                                                                           | tout ou rien, et payant                                                                               | **5**           |
| **Aucune latence par item** : `question_attempts` n'a que `created_at` ; le temps n'existe qu'au niveau de l'exercice (`attempts.duration_seconds`, `exercise_sessions.started_at/completed_at`) | la surcharge est indétectable                                                                         | **6**           |
| `difficulty_adaptation` **écrite par les RPC de soumission, lue par aucun sélecteur**                                                                                                            | une boucle morte de plus                                                                              | 4               |

> **Le diagnostic tient en une phrase.** Le moteur n'est pas en retard sur l'intelligence — il
> est en retard sur **la preuve** (le corpus ne dit pas ce que chaque erreur signifie) et sur
> **la décision** (personne ne choisit l'item suivant). Il manque **six organes**, numérotés ici et repris tels
> quels au §3 : une **croyance calibrée** ❶ · une **inférence** ❷ · un **diagnostic d'entrée** ❸ ·
> une **frontière « prêt à apprendre »** ❹, d'où se déduit la prochaine action · un
> **échafaudage** ❺ · une **gestion de la charge** ❻. Les organes ❶ ❷ ❹ sont la charpente — ce
> sont eux, avec le tagging du corpus, que livre le sous-ensemble minimal du §4.1.

### 1.2bis Re-mesure du 2026-08-25 (révision)

Même règle qu'au §1.2 : rien de mémoire. Chaque ligne relue le jour de la révision sur `main`
du moteur (#852) et `origin/main` du corpus (#237).

| Fait mesuré                                                                                                                                                                                                                                                                                    | Conséquence pour l'étude                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| **é11 est LIVRÉE — 8 lots sur 8** : lot 6 `20260824120000_tutor_digests.sql`, lot 7 `20260824130000_tutor_energy_console.sql`, branche `claude/etude-11-lots-6-7` (#844). ⚠️ Son ETUDE.md dit encore « 6 sur 8 » et son dossier n'est pas dans `EtudeRealisé/` — dérive signalée au §8         | §3.13 est réécrit au **présent mesuré** ; l'amendement D n'a plus de porteur → **lot 3bis** (§3.13d)                              |
| **é29 est LIVRÉE — 5 lots** (2026-08-22), dossier **déjà** dans `EtudeRealisé/` (déplacé le 2026-08-24) : six migrations `20260822170000…220000_ai_*.sql` sur `main` ; la Forge vérifiée telle que §3.13c la cite (`scope IN ('chapter','competency','mistakes')`, `competency_id TEXT` sans FK) ; la chaîne P4 vérifiée (`get_targeted_exercises` + `tutor_practice_needs_generation`, porte Q-8 « ≥ 3 questions fraîches » en SQL) | l'étude citait déjà é29 au présent — rien à corriger ; mais le **branchement « cause racine »** (P4) était orphelin comme l'amendement D : il reçoit son porteur, le **lot 4** (§3.13c) |
| **Le pack tuteur n'a aucune ligne de maîtrise** : `get_tutor_learner_context` (dernière version, `20260823100000`) rend classe, bande d'âge, objectif, bandes niveau/série, misconceptions actives (tag + libellés ×3), intérêts, verbosité — rien sur ce que l'élève maîtrise ni sur sa suite | le trou que comble le lot 3bis est **mesuré au jour de la révision**, pas déduit d'une version passée                             |
| **Le mini-check écrit `source = 'exercise'`, pas `'tutor'`** : `submit_tutor_mini_check` (é11 lot 4, `20260823140000`) insère dans `question_attempts` avec `session_id =` le fil `tutor_threads` actif, et seulement pour une question du catalogue (`exercise_source = 'admin'`)             | l'hypothèse « é11 lot 4 ajoutera la source `'tutor'` » est **falsifiée** ; le poids `w = 0,5` se détecte **par le fil** (§3.2)    |
| La contrainte `source` vaut aujourd'hui `('exercise','quiz','dungeon','exam')` (CHECK en ligne, nom auto `question_attempts_source_check`)                                                                                                                                                      | la migration du lot 7 (ajout `'placement'`, §3.8b) reste valable telle quelle                                                     |
| **Zéro artefact é30 dans le moteur** : `p_known`, `belief_*`, `placement_sessions`, `scaffold_reveals` — 0 occurrence dans `supabase/migrations/` et `src/`                                                                                                                                    | les lots 1-4 partent de zéro, comme spécifié ; rien à réconcilier                                                                 |
| ~~**Lot 0bis non démarré**~~ — **LIVRÉ le 2026-08-25** (§8) : les 297 questions muettes ont été lues une à une ; couverture **521 → 662/818 (64 % → 81 %)**, 156 muettes **statuées**                                                                                                       | KPI-1 est **tranché**, pas atteint à 100 % : la file démarre au lot 1                                                             |
| **Registre `math` : 62 entrées, 0 `scaffold`, 0 `pInit`/`pTransit`** (compté ce jour)                                                                                                                                                                                                          | conforme au plan ; STATUS §1bis porte désormais **62** — le signalement du §8 (2026-08-22) a été traité                           |
| **Aucune clé IA jamais branchée** (STATUS 2026-08-24) : é29 + é11 sont testées contre un transport factice ; le seul appel réel du système est la vérification d'une clé à sa saisie                                                                                                           | la voie déterministe est **100 % de l'intelligence servie** — c'est l'argument d'exécution de cette étude, écrit au §1.1 et §3.13c |

### 1.3 Le référentiel : ce que font les trois systèmes cités

Détail sourcé en **annexe B**. Le condensé qui commande l'architecture :

| Référence       | Le mécanisme qui fait sa réputation                                                                                                                                                                                                                                                                 | Ce qu'on en retient ici                                                                                                                             |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| **ALEKS**       | _Knowledge Space Theory_ : l'état de connaissance est un **ensemble** dans la structure ordonnée du domaine ; le diagnostic situe l'élève sur 200–300 items en **~25–30 questions**, chacune choisie d'après la précédente ; la « frange extérieure » nomme ce que l'élève est **prêt à apprendre** | **la frontière** (§3.4) et **l'inférence** (§3.3) — l'organe le plus rentable et le plus absent                                                     |
| **Squirrel AI** | découpage **nano** (jusqu'à ~10 000 points pour les maths collège, contre 2 000–3 000 dans un manuel) + moteur à trois étages (carte de l'élève / gestion d'objectifs / recommandation)                                                                                                             | **la granularité est un choix de corpus, pas de code** — 62 compétences par matière-année est la maille retenue (Q-2) ; on ne copie **pas** le nano |
| **CENTURY**     | micro-apprentissage explicitement conçu pour **ne pas surcharger** ; entrelacement, récupération fréquente, intervalles espacés                                                                                                                                                                     | valide l'existant (SM-2, rappel actif) et donne sa raison d'être au **lot 6** (charge cognitive, différé)                                                    |

Les trois partagent la même colonne vertébrale — un **modèle du domaine** (graphe), un **modèle
de l'apprenant** (croyance), un **modèle pédagogique** (décision) : la définition canonique d'un
ITS. L'arena possède le premier, une ébauche du deuxième, et rien du troisième.

### 1.4 Objectif & indicateurs de succès

**Objectif** : qu'à tout instant, pour un élève et une matière taggée, le système sache dire —
et prouver — **trois phrases** :

> « Voilà ce que tu maîtrises, et pourquoi j'en suis sûr. Voilà ce que tu es prêt à apprendre
> maintenant. Voilà ce qui te bloque, et par où on reprend. »

**KPI** (mesurés sur la matière pilote `math` 9ᵉ) :

- **KPI-1 — couverture de preuve** : % d'items servis dont la compétence **et** les distracteurs
  sont **statués** — taggés, ou déclarés légitimement muets par la règle du lot 0bis. Cible
  relue : **« 0 distracteur non statué » sur `math` 9ᵉ** — **ATTEINTE le 2026-08-25** (§8) :
  818/818 questions statuées, **662 taguées (81 %)**, 156 muettes **par décision**, pas par
  oubli. _(La cible d'origine « 100 % taggés » est abandonnée sur la mesure du lot 0bis : la
  règle « taggé ssi reconstructible » plafonne à 81 %, et au-delà le chiffre compterait des
  tags posés au jugé — or un mauvais tag enseigne une fausse erreur, il coûte plus cher que
  pas de tag.)_ Il commande tous les autres.
- **KPI-2 — économie du diagnostic** : nombre médian d'items pour déclarer une première
  compétence maîtrisée. Référence ALEKS : ~30 questions pour situer 200–300 items. Cible ici :
  **≤ 6 items par compétence déclarée**, inférence comprise.
- **KPI-3 — calibration** : parmi les items où le modèle annonçait `p_known ∈ [0,7 ; 0,8]`, le
  taux de réussite observé doit tomber dans **[0,65 ; 0,85]**. Un modèle non calibré est un
  modèle qui ment poliment : c'est le seul KPI qui peut **invalider** l'étude — et depuis
  l'arbitrage **Q-6**, c'est aussi lui qui, seul, ouvre la porte IRT/Elo.
  ⚠️ **Une bande n'a le droit d'être déclarée mauvaise qu'à partir de `n ≥ 100` observations.**
  En dessous, elle est **« non concluante »**, jamais « mauvaise » — sans ce garde-fou la règle
  de Q-6 se déclencherait sur du bruit (avec 40 élèves actifs, une bande contient une douzaine
  de réponses et rougit par hasard). Le seuil n'est pas arbitraire : à `n = 100` et `p ≈ 0,75`,
  l'erreur-type vaut ≈ 0,043, donc l'intervalle à 95 % est ≈ **[0,665 ; 0,835]** — il tient
  **juste** dans la tolérance [0,65 ; 0,85]. La console du lot 8 affiche donc **le `n` de chaque
  bande à côté de son taux** : une courbe de calibration sans effectifs est un piège à décisions.
- **KPI-4 — piétinement** (_wheel-spinning_) : part des élèves accumulant ≥ 10 tentatives sur une
  compétence sans jamais la maîtriser. Mesure de départ établie au lot 6 ; cible : **en baisse**
  après le lot 4 (la remédiation attaque la cause, pas le symptôme).
- **KPI-5 — la frontière est jouée** : % des exercices lancés qui appartiennent à la frontière
  « prêt à apprendre ». Sans cible chiffrée en v1 : on veut la **tendance**, pas un quota.

### 1.5 Ce que cette étude ne cherche PAS à faire

- **Aucun LLM dans le chemin de décision** (é26 P-5a). Tout ce qui est spécifié ici tourne avec
  `AI_KEY_ENC_KEY` absente — c'est-à-dire **dans le produit d'aujourd'hui**.
- **Aucun apprentissage automatique de paramètres.** Les paramètres du modèle de croyance sont
  **écrits dans le registre** et versionnés, pas ajustés par descente de gradient (D-2 — le
  problème d'identifiabilité de BKT, annexe B.4, explique pourquoi).
- **Aucun verrou de progression.** L'étude 22 a retiré les faux verrous séquentiels ; on ne les
  remet pas. La maîtrise **conseille**, elle n'interdit pas (D-3, arbitrage Q-1).
- **Aucune génération d'exercices à la volée** (é04 A3, gelée ; é29 la Forge couvre le besoin
  ponctuel, hors récompense).
- **Aucune refonte de é04 / é07 / é22.** Leurs décisions sont fermées et tenues. Cette étude
  **ajoute des organes** ; les deux seuls amendements nécessaires sont nommés au §3.9 et passent
  par leur étude propriétaire.
- **Pas de nano-découpage à la Squirrel AI.** Multiplier la maille par 100 multiplierait la dette
  de tagging par 100 pour un gain non démontré.
- **Pas de tableau de bord enseignant** (é08, propriétaire du canal enseignant depuis é28 Q-3).

---

## 2. Spécification fonctionnelle

### 2.1 Acteurs & user stories

- **US-1 (élève, diagnostic)** — à mon entrée dans une matière taggée, on me propose « **On te
  situe en 5 minutes** » : 12 à 20 questions, une à la fois, choisies d'après mes réponses. À la
  fin je vois une carte : ce que je maîtrise déjà, ce que je peux attaquer, ce qui manque en
  amont. Je peux **refuser** ou **arrêter** à tout moment, sans perdre ce qui a été mesuré.
- **US-2 (élève, croyance)** — sur ma carte de compétences, chaque compétence porte un état
  lisible — **maîtrisée · en cours · fragile · lacune** — et non un pourcentage nu. Une
  compétence n'est **maîtrisée** que si je l'ai prouvée **plusieurs fois et sous plusieurs
  formes**.
- **US-3 (élève, inférence)** — quand je réussis une compétence avancée, le système **ne me
  refait pas passer** ses prérequis : il me le dit (« _tu as réussi Thalès : je considère la
  proportionnalité acquise, dis-moi si je me trompe_ ») et je peux **contester en un geste**.
- **US-4 (élève, prochaine action)** — après chaque exercice, une seule proposition, motivée :
  monter d'un cran, refaire **la même compétence sous une autre forme**, ou **redescendre au
  prérequis** qui bloque. Jamais une liste : **une** action, avec sa raison en une phrase.
- **US-5 (élève, échafaudage)** — quand je bute, je peux demander de l'aide **par paliers** :
  d'abord une question qui oriente mon attention, puis la règle ou une analogie, puis la
  décomposition en une sous-étape. **Jamais la réponse.** Gratuit, et ça ne consomme aucun objet.
- **US-6 (élève, rythme)** — quand j'enchaîne les erreurs ou que je traîne anormalement, le
  système **baisse d'un cran**, change de format ou me propose une pause — sans jamais me
  bloquer ni me sanctionner.
- **US-7 (parent)** — le rapport nomme les compétences **déclarées maîtrisées** (avec « prouvé
  N fois, sous M formes »), et non un pourcentage moyen. _(Livré par é08, qui consomme les
  lectures de cette étude ; hors périmètre ici.)_
- **US-8 (admin)** — une console de **calibration** : distribution de `p_known`, courbe de
  calibration (KPI-3), liste des compétences dont les paramètres semblent faux. Sans elle, le
  modèle est invérifiable.

### 2.2 Règles métier

**Croyance et preuve**

- **R-1** — la croyance `p_known ∈ [0,01 ; 0,99]` est la **variable de décision** ; la maîtrise
  EWMA `mastery ∈ [0,100]` de é07 reste la **variable d'affichage** et n'est pas modifiée. Les
  deux sont entretenues par le même trigger, sur le même événement, dans la même transaction.
- **R-2** — la probabilité de **hasard** `p(G)` n'est pas une constante d'auteur : c'est la
  **géométrie de l'item** (§3.2). Un `mcq` à 4 options a un plancher de hasard de 0,25 ; une
  saisie libre (`short_answer`, variante **rappel**) tombe à 0,02. **Conséquence produite, pas
  décrétée : une réponse juste en saisie libre vaut plusieurs QCM justes.**
- **R-3** — la probabilité d'**inattention** `p(S)` est plafonnée à **0,10** et ne peut être
  relevée que par un **signal de charge** (lot 6), jamais par l'élève, jamais au-delà de 0,20.
- **R-4** — une compétence est **déclarée maîtrisée** si et seulement si les cinq conditions
  tiennent ensemble : `p_known ≥ 0,95` · `evidence_count ≥ 4` · `distinct_sessions ≥ 2` ·
  `distinct_forms ≥ 2` (deux types d'items distincts, la variante rappel comptant pour un type)
  · dernière preuve **datant de moins de 30 jours**. Le mandat dit « répétée et variée » : ce
  sont ces cinq conditions.
- **R-5** — une **lacune est confirmée** si `p_known ≤ 0,25` avec `evidence_count ≥ 3`. En deçà
  de 3 preuves, on dit « fragile », jamais « lacune » : accuser sur deux items est une erreur de
  mesure, pas un diagnostic.
- **R-6** — **neutralité du non-taggé**, non négociable (é07 R-2 étendu) : un item sans
  compétence ne crée ni ne modifie aucune croyance ; une compétence sans preuve n'a aucune ligne.
  Sur les ~88 matières non taggées, **tout ce que spécifie cette étude est silencieux et le
  produit rend exactement ce qu'il rend aujourd'hui**.

**Inférence dans le graphe**

- **R-7** — l'inférence **monte** : établir `p_known(C) ≥ 0,85` **relève** la croyance de chaque
  prérequis `P` à `max(p_known(P), γ^d · p_known(C))`, `γ = 0,7`, profondeur `d ≤ 2`.
- **R-8** — l'inférence **ne descend jamais une croyance**. Une lacune confirmée sur `C` ne baisse
  pas ses prérequis : elle les marque `suspect`, ce qui les **fait sonder en priorité** (lot 3,
  lot 7). Motif : relever par déduction est charitable et fait gagner du temps ; abaisser par
  déduction fabrique des lacunes que l'élève n'a jamais commises.
- **R-9** — **l'inférence ne déclare jamais la maîtrise** : elle plafonne à `p_known = 0,90`,
  sous le seuil de 0,95 de R-4, et n'incrémente **ni** `evidence_count` **ni** `distinct_forms`.
  On ne peut être déclaré maître que de ce qu'on a fait soi-même.
- **R-10** — toute croyance issue d'une inférence est **traçable et contestable** : elle porte sa
  source (`inferred_from`) et l'élève peut la refuser en un geste (US-3), ce qui la ramène à sa
  valeur d'avant inférence et pose `suspect = true`.

**Diagnostic d'entrée**

- **R-11** — le bilan d'entrée est **facultatif, interruptible, rejouable** (une fois par matière
  et par 60 jours) et **borné à 20 items**. Il s'arrête plus tôt dès que la frontière est
  stabilisée (§3.5).
- **R-12** — il **ne donne aucune note** et ne se compare à personne : sa sortie est une carte,
  pas un score. Il rapporte l'XP d'une session normale, jamais davantage — ce n'est pas une
  nouvelle économie (é04 R-4 étendu).
- **R-13** — les croyances écrites par le bilan portent `source = 'placement'` et un
  `evidence_count` qui **ne compte que pour 1** quel que soit le nombre d'items : un mauvais jour
  ne doit pas marquer un élève. Elles sont écrasables par la première preuve de jeu réel.

**Décision & remédiation**

- **R-14** — la **prochaine meilleure action** est calculée serveur, rendue **une** à la fois, et
  toujours accompagnée de **sa raison** en langage élève. Trois branches, dans cet ordre de
  priorité : `remédiation` (une lacune confirmée existe en amont) → `consolidation` (compétence
  en cours) → `progression` (frontière).
- **R-15** — la **boucle de remédiation** remonte la chaîne des prérequis **jusqu'à la première
  compétence non maîtrisée en partant du bas** (la cause racine, pas le symptôme), en réutilisant
  `get_competency_blockers` (é07 lot 4), borné à **profondeur 3** et à **une seule** remontée par
  session.
- **R-16** — la décision ne propose **que** des exercices que `resolve_exercise_access` autorise
  (é04 R-3 tenu, repli d1–2 du même chapitre inchangé).
- **R-17** — la maîtrise **ne verrouille rien**. Une compétence non maîtrisée en amont produit un
  **avertissement motivé** et une action de remédiation proposée ; l'élève reste libre de jouer
  ce qu'il veut (é22). _Arbitrage Q-1._

**Échafaudage**

- **R-18** — l'échafaudage est **du contenu écrit**, versionné et validé par les gates, jamais
  généré à la volée (é26 P-5c). Trois paliers, dans l'ordre : `orient` (question réflexive) →
  `rule` (règle ou analogie) → `decompose` (sous-étape).
- **R-19** — un palier ne se révèle **qu'un à la fois**, dans l'ordre, et **jamais le palier
  suivant sans que le précédent ait été lu**. Aucun palier ne contient la réponse : le gate
  contenu le vérifie (§5).
- **R-20** — l'échafaudage est **gratuit** et **ne consomme aucun consommable**. Il vit dans le
  **chemin de correction et de reprise**, pas dans la première tentative : la couture de
  soumission atomique n'est pas rouverte (é04 §9 Q-4, décision tenue).
- **R-21** — l'échafaudage **n'affecte pas la croyance de l'item en cours** ; il déclasse en
  revanche la preuve de la **reprise** : une réussite après palier 3 compte comme une preuve à
  poids réduit (§3.2), jamais comme une preuve pleine.

**Charge cognitive**

- **R-22** — la latence par item (`elapsed_ms`) est **rapportée par le client**, bornée
  serveur à `[0 ; 300 000]` ms, et **n'entre dans aucun calcul de récompense** — jamais. C'est un
  signal de charge, pas une mesure de performance (le chrono récompensé du boss reste serveur et
  n'est pas touché).
- **R-23** — trois signaux, tous relatifs **à l'élève lui-même**, jamais à une moyenne de
  cohorte : latence > 3 × sa médiane personnelle sur la compétence · ≥ 3 erreurs consécutives
  dans la session · **piétinement** (≥ 10 tentatives sur une compétence sans 3 réussites
  consécutives — seuil repris de la littérature, annexe B.3).
- **R-24** — la réaction est **graduée et jamais bloquante** : baisser d'un palier de difficulté,
  changer de type d'item, proposer une pause. Le message est une **proposition**, refusable, et
  n'apparaît **pas plus d'une fois par session**.
- **R-25** — un signal de charge actif **relève `p(S)`** vers son plafond de 0,20 (R-3) : le
  système devient **plus indulgent quand il détecte la fatigue**. C'est l'unique couplage entre
  les points 3 et 6 du mandat, et il va dans le seul sens acceptable — jamais l'inverse.

### 2.3 i18n & RTL

Toutes les nouvelles surfaces sont trilingues **FR/EN/AR** avec RTL, comme le reste. Trois
familles de libellés :

- **états de maîtrise** (4 valeurs) et **raisons de décision** (≈ 8 valeurs) : le serveur rend un
  **identifiant**, le client le met en langue — même posture que é04 A1.2b (« la fonction SQL rend
  un ID, le registre reste source unique »). Aucune phrase française en base.
- **paliers d'échafaudage** : ils viennent du **corpus**, donc trilingues à l'authoring, validés
  par le gate contenu au même titre que `explanation`.
- **libellés de compétences** : déjà trilingues dans `competencies` (é07 lot 1) — rien à faire.

⚠️ Deux pièges connus, à rappeler à l'exécuteur : une phrase arabe mêlant texte, chiffres et
unités est **un seul nœud de texte** (sinon elle s'inverse), et un pourcentage suivi d'un signe
se compose avec les marques bidi explicites. Voir `docs/design-surfaces.md`.

### 2.4 Hors périmètre (v1)

- La **voix** du tuteur (reformulation, dialogue socratique génératif) → é11, **livrée** —
  éteinte sans clé (é29 R-1) ; elle attend la **substance** des lots 5·9 pour reformuler
  l'échafaudage au lieu de l'inventer.
- Le **rapport parent** consommant la maîtrise déclarée → é08.
- Le **percentile par compétence** dans l'examen blanc → é02.
- Le **tagging** lui-même (C4bis et l'extension hors math) → fil contenu, dépôt privé.
- L'**IRT / Elo** et tout modèle à difficulté latente estimée : `p(G)` par géométrie d'item est
  la version pauvre et honnête qu'on peut tenir sans données. Porte de réouverture en Q-6.

---

## 3. Architecture technique (décisions fermées)

### 3.1 Vue d'ensemble — où s'insèrent les six organes

```
                 ┌───────────────────────────────────────────────┐
   une réponse   │  submit_exercise_attempt / submit_placement…  │  (RPC SECURITY DEFINER
                 │                          ▲ ❸ le bilan d'entrée │   existantes, inchangées
   ───────────▶  │      ↓ INSERT question_attempts (+elapsed_ms) │   sauf la colonne ajoutée)
                 └───────────────────────────────────────────────┘
                                    │ AFTER INSERT (triggers, même transaction)
             ┌──────────────────────┼──────────────────────┬────────────────────────┐
             ▼                      ▼                      ▼                        ▼
   record_user_misconception  record_competency_    ❶ record_competency_    ❷ propagate_competency_
        (é04, inchangé)         mastery (é07 EWMA,     belief  (BKT)            belief  (graphe, ≤2)
                                   inchangé)          ─ NOUVEAU ─               ─ NOUVEAU ─
                                                            │                        │
                                                            └────────┬───────────────┘
                                                                     ▼
                                              user_competency_mastery  — une ligne par (élève, compétence)
                                              mastery 0-100  ← AFFICHAGE (é07, intouché)
                                              p_known 0-1    ← DÉCISION  (nouveau)
                                                                     │
                    ┌────────────────────────────────────────────────┼────────────────────┐
                    ▼                             ▼                  ▼                    ▼
          get_learning_state()       ❹ get_learning_frontier()   get_daily_plan()   get_competency_
           (carte + états)              (« prêt à apprendre »)     (é04, inchangé)    blockers (é07)
                    └──────────────┬──────────────┘                                        │
                                   ▼                                                       │
                        resolveNextAction()  ◀───────────────────────────────────────────┘
                        (é22 D-8 : TS partagé, PAS une RPC — deux priorités ajoutées)
```

Quatre principes de greffe, qui expliquent chaque choix ci-dessous :

1. **On n'ajoute pas de second écrivain.** Les croyances vivent dans la table qui porte déjà la
   maîtrise, écrites par un trigger de plus sur le même événement, dans la même transaction. Deux
   tables entretenues par deux triggers sur le même fait, c'est une divergence programmée.
2. **On n'ajoute pas de second décideur.** `resolveNextAction` reste **le** moteur de décision
   (é22 D-8) ; le serveur lui livre des **faits** de plus, pas un verdict concurrent.
3. **On ne change aucune signature existante.** Toute lecture nouvelle est une **nouvelle**
   fonction ; aucune `DROP FUNCTION` sur une RPC que le client appelle (DoD §7).
4. **Tout dégrade au silence.** Sans tag, sans preuve, sans clé : le produit rend exactement ce
   qu'il rend aujourd'hui (R-6).

### 3.2 Le modèle de croyance (organe ❶)

**Le modèle.** Bayesian Knowledge Tracing (Corbett & Anderson, 1994), quatre paramètres :
`p(L₀)` initial, `p(T)` apprentissage, `p(G)` hasard, `p(S)` inattention. Après une observation :

```
correct :  p⁺ = p(1−S) / [ p(1−S) + (1−p)G ]
faux    :  p⁺ = p·S    / [ p·S    + (1−p)(1−G) ]
puis      p' = p⁺ + (1−p⁺)·T                       (l'élève peut avoir appris en répondant)
```

**D-1 — deux nombres, une seule vérité.** `p_known` (0–1) devient la variable de **décision** ;
`mastery` (0–100, EWMA de é07) reste la variable d'**affichage** et n'est pas touchée.
_Alternatives rejetées_ : (a) remplacer l'EWMA — casse la carte é07 lot 4, le terme « faiblesse
de compétence » de `get_daily_plan`, le rapport parent et 40+ assertions pgTAP, pour un gain nul
côté écran (un élève ne lit pas une probabilité) ; (b) une table de croyance séparée — deux
écrivains sur le même fait. La règle de coexistence est simple et testable : **l'EWMA se montre,
la croyance décide** ; aucune surface n'affiche `p_known` en clair sauf la console d'admin.

**D-2 — deux paramètres dérivés, deux paramètres écrits : BKT sans ajustement.** C'est la
décision qui rend ce modèle tenable ici.

- `p(G)` **n'est pas un paramètre libre : c'est la géométrie de l'item.** Un QCM à 4 options a un
  plancher de hasard de 1/4. Une saisie libre n'en a pas.
- `p(S)` **n'est pas un paramètre libre non plus** : il dépend du palier de difficulté (une erreur
  sur un item facile est plus probablement une étourderie) et du **signal de charge** (R-25).
- `p(L₀)` et `p(T)` sont **écrits dans le registre de compétences**, versionnés, avec des défauts
  de famille — jamais estimés.

_Pourquoi c'est décisif_ : le reproche classique fait à BKT est l'**identifiabilité** (Beck) —
plusieurs jeux de paramètres expliquent également bien les mêmes données, et l'ajustement dérive
vers des valeurs dégénérées (annexe B.4). Ici **rien n'est ajusté** : deux paramètres sont
déduits de la forme de l'item, deux sont déclarés par un auteur. Le problème d'identifiabilité
ne se pose pas, parce qu'il n'y a pas d'estimation. Les bornes de la littérature —
`p(G) ≤ 0,30`, `p(S) ≤ 0,10` hors charge — sont conservées **comme garde-fous d'écriture**, pas
comme contraintes d'optimisation.

Les deux fonctions de constantes, sur le modèle de `competency_mastery_alpha` (é07 R-4 :
« constantes centralisées, jamais en ligne à l'appel ») :

```sql
-- Le hasard est la géométrie de l'item (D-2). mcq : 1/k, borné [0,15 ; 0,30] — la borne haute
-- est celle de la littérature (anti-dégénérescence), la borne basse dit qu'un QCM reste un QCM.
CREATE OR REPLACE FUNCTION public.belief_guess(
  p_question_type TEXT, p_option_count INT, p_variant TEXT
) RETURNS NUMERIC LANGUAGE sql IMMUTABLE AS $$
  SELECT (CASE
    WHEN p_variant = 'recall'          THEN 0.02   -- é17 : saisie libre de mémoire
    WHEN p_question_type = 'short_answer' THEN 0.02
    WHEN p_question_type = 'numeric'   THEN 0.05
    WHEN p_question_type IN ('ordering','matching') THEN 0.05
    WHEN p_question_type = 'multi'     THEN 0.08
    WHEN p_question_type = 'mcq'       THEN
      LEAST(0.30, GREATEST(0.15, 1.0 / GREATEST(COALESCE(p_option_count, 4), 2)))
    ELSE 0.25
  END)::NUMERIC;
$$;

-- L'inattention décroît avec la difficulté : rater un item facile ressemble à une étourderie,
-- rater un item dur ressemble à une lacune. Le palier de charge (lot 6) la pousse au plafond.
CREATE OR REPLACE FUNCTION public.belief_slip(p_difficulty INT, p_under_load BOOLEAN)
RETURNS NUMERIC LANGUAGE sql IMMUTABLE AS $$
  SELECT (CASE WHEN p_under_load THEN 0.20 ELSE
    CASE COALESCE(p_difficulty, 2)
      WHEN 1 THEN 0.10 WHEN 2 THEN 0.08 WHEN 3 THEN 0.06 WHEN 4 THEN 0.05 ELSE 0.08 END
  END)::NUMERIC;
$$;
```

> **Le corollaire produit, qui n'a pas été décrété mais calculé** (table complète en annexe A.1).
> Une réponse juste en **rappel actif** (é17) fait passer une croyance de 0,20 à **0,932** en un
> item ; il faut **trois** QCM à 4 options justes pour atteindre le même niveau (0,961). Le
> mandat demande une validation « répétée
> **et variée** » : la variété n'est pas un ornement, c'est **la quantité d'information**. C'est
> aussi la justification quantitative des 6 types natifs (é03) et du rappel actif (é17) — deux
> études qui deviennent rétroactivement des investissements dans le diagnostic.

**Le poids de la preuve.** Un item résolu **après échafaudage** n'est pas la même preuve qu'un
item résolu seul (R-21). La mise à jour est mélangée :
`p_final = p_avant + w · (p_après − p_avant)`, avec `w = 1,0` sans aide, `0,5` après les paliers
1–2, `0,25` après le palier 3. C'est l'échafaudage de Bruner rendu mesurable : **l'aide se retire
à mesure que l'autonomie se prouve**, et le système sait de quelle autonomie il parle.

**Le mini-check du tuteur est le premier cas réel de ce poids — et il se détecte par le fil, pas
par la source** _(re-spécifié le 2026-08-25 sur la couture livrée)_. É11 lot 4 n'a **pas** créé
de source `'tutor'` : `submit_tutor_mini_check` écrit `source = 'exercise'` avec `session_id =`
le fil `tutor_threads` actif (mesuré, `20260823140000`). Le trigger du lot 1 applique donc
`w = 0,5` quand `NEW.session_id` est l'id d'un fil de tuteur — un `EXISTS` sur la clé primaire
de `tutor_threads`, le coût d'un lookup indexé, nul pour les soumissions dont le `session_id`
est un exercice ou un donjon. La raison du poids est inchangée : une question posée **juste
après une explication** est structurellement une reprise après aide (é11 US-4), pas une preuve
d'autonomie. L'autre moitié du contrat de §3.13 est **déjà tenue par é11 telle que livrée** :
seule une vraie question du catalogue entre dans `question_attempts` (`exercise_source = 'admin'`
vérifié dans la RPC) — rien de ce que le tuteur ou la Forge produit ne peut fabriquer une
croyance.

**Constantes centralisées** — un seul fichier TS isomorphe `src/shared/constants/adaptive.ts`
(les seuils lus côté client pour l'affichage) et les fonctions SQL ci-dessus (les seuils lus côté
décision). Aucune valeur en ligne à un site d'appel :

| constante                                     | valeur          | d'où elle vient                                    |
| --------------------------------------------- | --------------- | -------------------------------------------------- |
| `MASTERY_THRESHOLD`                           | `0,95`          | seuil canonique de Corbett & Anderson (annexe B.4) |
| `GAP_THRESHOLD`                               | `0,25`          | symétrique bas ; en deçà, on parle de lacune       |
| `FRAGILE_THRESHOLD`                           | `0,60`          | borne basse de la ZPD affichée                     |
| `MIN_EVIDENCE` / `MIN_SESSIONS` / `MIN_FORMS` | `4` / `2` / `2` | « répétée et variée » (R-4)                        |
| `EVIDENCE_STALE_DAYS`                         | `30`            | aligné sur la fenêtre des misconceptions (é04 R-2) |
| `INFERENCE_DAMPING` γ                         | `0,70`          | R-7                                                |
| `INFERENCE_MAX_DEPTH`                         | `2`             | R-7 · perf (§3.8)                                  |
| `INFERENCE_CEILING`                           | `0,90`          | R-9 — sous le seuil de maîtrise, par construction  |
| `PLACEMENT_MAX_ITEMS`                         | `20`            | R-11                                               |
| `LOAD_LATENCY_FACTOR`                         | `3,0`           | R-23 (× la médiane personnelle)                    |
| `LOAD_ERROR_STREAK`                           | `3`             | R-23                                               |
| `WHEEL_SPIN_ATTEMPTS`                         | `10`            | seuil de la littérature (annexe B.3)               |
| `EVIDENCE_WEIGHTS` (sans aide · pal. 1–2 · pal. 3) | `1,0 / 0,5 / 0,25` | R-21 · annexe A.3                             |
| `TUTOR_CHECK_WEIGHT`                          | `0,5`           | §3.2 — mini-check é11 = reprise après aide, détecté par le fil |
| `ZPD_TARGET`                                  | `[0,55 ; 0,80]` | P(réussite) visée par le sélecteur (§3.4 · annexe A.5) |

### 3.3 L'inférence dans le graphe (organe ❷)

Le mandat, point 2 : « _si l'élève valide une notion complexe, le système en déduit la maîtrise
probable des prérequis sous-jacents_ ». C'est le cœur de l'économie d'ALEKS — et c'est
exactement ce que le graphe de é07 permet **sans rien ajouter au corpus**.

**D-3 — l'inférence monte, elle ne descend jamais.** Une croyance haute sur `C` **relève** ses
prérequis (R-7). Une lacune confirmée sur `C` **ne baisse pas** ses prérequis : elle les marque
`suspect`, ce qui les fait **sonder en priorité** (R-8). _Motif_ : relever par déduction est
charitable — au pire on fait sauter des exercices redondants, et la première preuve contraire
corrige. Abaisser par déduction est accusatoire — on fabrique dans le dossier de l'élève des
lacunes qu'il n'a jamais commises, et le rapport parent les affichera. L'asymétrie n'est pas une
timidité : c'est la seule qui reste vraie quand on se trompe.

**D-4 — l'inférence ne déclare jamais la maîtrise** (R-9) : plafond `0,90 < 0,95`, et
`evidence_count` / `distinct_forms` restent inchangés. On peut être **dispensé** d'un prérequis ;
on n'est **déclaré maître** que de ce qu'on a fait.

**D-5 — l'inférence est traçable et contestable** (R-10) : la ligne porte `belief_source`
(`'evidence' | 'inference' | 'placement'`) et `inferred_from` (la compétence qui a déduit). Un
geste « je ne suis pas d'accord » ramène la croyance à sa valeur d'avant inférence et pose
`suspect = true`. Le mandat parle de tuteur autonome, pas d'un tuteur qui a toujours raison.

**Déclenchement et coût.** La propagation ne tourne **pas à chaque réponse** : elle tourne à la
**traversée de bande**, quand `p_known` franchit `0,85` vers le haut (et, pour le marquage
`suspect`, `0,25` vers le bas). Sur le graphe mesuré — 62 compétences, 80 arêtes, **1,29 prérequis
en moyenne, 3 au maximum en direct** — une propagation de profondeur 2 touche **≈ 3 lignes en
régime courant, 12 dans le pire cas théorique**. C'est un ordre de grandeur, pas une promesse :
le lot 2 doit **mesurer** le coût réel du trigger avant/après sur la RPC de soumission (§4,
critère d'acceptation), parce que dans ce dépôt une réécriture SQL a déjà guéri un appelant et
empoisonné l'autre.

### 3.4 La frontière « prêt à apprendre » (organe ❹)

C'est la lecture la plus rentable de toute l'étude, et elle ne coûte qu'une requête.

```
intérieur    : state(C) = 'maitrisee'
frontière    : state(C) ≠ 'maitrisee'  ET  tous les prérequis directs de C sont 'maitrisee'
hors-portée  : state(C) ≠ 'maitrisee'  ET  au moins un prérequis direct ne l'est pas
```

La **frontière** est ce que l'élève peut attaquer maintenant : c'est la ZPD de Vygotsky, rendue
calculable par le graphe. Le **hors-portée** n'est pas une zone interdite (R-17) : c'est la zone
où toute proposition du système commence par une **remontée**. Et une compétence hors-portée sur
laquelle l'élève insiste malgré l'avertissement reste jouable — c'est son droit, et c'est parfois
lui qui a raison.

`get_learning_frontier(p_family TEXT DEFAULT NULL, p_limit INT DEFAULT 5)` rend, par ordre de
valeur décroissante : la compétence, son état, son `p_known`, le nombre de compétences qu'elle
**débloque** (fan-out — mesuré jusqu'à **7** sur le graphe math), et un exercice d'entrée résolu
par `get_exercises_for_competency` (é07 lot 4, réutilisée, jamais réécrite).

> Le tri par fan-out est le seul endroit où cette étude fait un pari pédagogique explicite :
> **à croyance égale, on propose d'abord ce qui ouvre le plus de portes**. C'est ce qui distingue
> un plan d'un tirage, et c'est vérifiable — KPI-5.

**Et le sélecteur vise la ZPD, en nombres** _(ajout de la révision du 2026-08-25 — il ne crée
aucun objet : il choisit mieux parmi les candidats déjà rendus)_. Parmi les exercices que
`get_exercises_for_competency` rend pour la compétence retenue, l'exercice d'entrée est celui
dont le couple (type d'item, palier de difficulté) donne la `P(réussite)` prédite — annexe A.5 :
`p·(1−S) + (1−p)·G` — **dans l'intervalle `ZPD_TARGET = [0,55 ; 0,80]`**, à défaut le plus
proche du bord. Même règle au lot 4 pour `strengthen` (à types distincts égaux) et au lot 7
pour le bilan (qui disait « difficulté 2 de préférence » — la formule remplace la préférence).
C'est le mandat point 4 rendu arithmétique — « réussite facile → défi supérieur, difficulté
légère → autre format » — et c'est exactement ce que é11 US-13 appelait « probabilité de
réussite estimée 60-80 % » : elle cesse d'être estimée.

### 3.5 Le bilan d'entrée (organe ❸)

**Le principe ALEKS, transposé** : ne pas balayer le programme, mais **choisir chaque question
pour ce qu'elle apprend au système**. À chaque étape, l'item retenu est celui dont on ignore le
plus le résultat — la compétence dont `p_known` est **la plus proche de 0,5**, prise dans la
**frontière** courante, en préférant les fort-fan-out et les `suspect`.

```
répéter jusqu'à (items ≥ 20)  ou  (aucune compétence avec 0,25 < p_known < 0,80)  ou  abandon :
    C  ← argmax sur la frontière ∪ suspects  de   info(C) = 1 − |p_known(C) − 0,5| × 2
                                                  départage : fan-out ↓, puis aléatoire stable
    q  ← un item de C non encore servi, accessible (resolve_exercise_access), P(réussite) dans ZPD_TARGET (§3.4)
    servir q, lire la réponse, mettre à jour la croyance (BKT normal, w = 1,0)
    propager (§3.3) — c'est CE pas qui rend le bilan court
```

La condition d'arrêt « plus aucune compétence dans l'intervalle d'incertitude » est ce qui permet
de finir en **8 items** sur un élève net, et de ne jamais dépasser 20 sur un élève difficile à
situer. Référence : ALEKS situe 200–300 items en ~25–30 questions ; ici, 62 compétences en **≤ 20**
(KPI-2). La borne dure de 20 est un choix de produit, pas une limite d'algorithme : au-delà,
l'abandon coûte plus cher que l'imprécision (RISK-3).

**Anti-abus & vie privée.** `submit_placement_answer` est `SECURITY DEFINER` et corrige côté
serveur (la clé ne sort jamais, ici comme partout) ; le bilan n'accepte qu'**une** session
`running` par (élève, matière) ; les items servis sont écrits dans `question_attempts` avec
`source = 'placement'` — donc soumis à la même purge à 12 mois, à la même RLS, aux mêmes
agrégats. Aucune nouvelle surface de données personnelles.

### 3.6 L'échafaudage (organe ❺, mandat point 5)

**D-6 — l'échafaudage est du contenu écrit, servi palier par palier, gratuit, hors de la
première tentative.** Trois décisions en une, chacune contrainte par une décision antérieure :

- **écrit, pas généré** : é26 P-5c (la génération runtime non vérifiée en maths est
  l'anti-pattern documenté). Il vit dans le corpus, passe les gates, se relit.
- **hors de la première tentative** : é04 §9 Q-4 a explicitement refusé un retour
  question-par-question qui rouvrirait la couture de soumission atomique. **Cette décision est
  tenue.** L'échafaudage apparaît dans le **bloc de correction** (é04 A1.2b, déjà là) et dans la
  **reprise** — c'est-à-dire exactement au moment où le mandat le demande (« en cas de blocage »).
- **gratuit** : `consume_hint` (révélation payante de l'explication **avant** réponse) n'est pas
  touché — c'est une autre mécanique, dans un autre moment, avec une autre économie. Deux aides
  qui ne se rencontrent jamais : é04 R-4 (« pas de nouvelle économie ») reste vrai.

**D-6bis — deux paliers appartiennent à la COMPÉTENCE, un seul à la question.** C'est la
décision qui rend l'échafaudage réalisable, et elle vient d'un calcul, pas d'un goût : écrire
trois paliers pour **22 146 questions** représente ~66 000 textes à rédiger, relire et traduire.
C'est hors d'atteinte, et ce serait du gaspillage — parce que **les deux premiers paliers ne
dépendent pas de l'item**.

- Palier 1 `orient` (« où regarder ») et palier 2 `rule` (la règle, l'analogie) décrivent la
  **compétence**. « Regarde les dénominateurs : sont-ils les mêmes ? » est vrai de toutes les
  additions de fractions. → **62 × 2 = 124 textes pour toute la matière `math`**, et ils
  couvrent alors **chaque question taggée**, gratuitement.
- Palier 3 `decompose` (« fais seulement la première étape ») est le seul qui parle de **cet
  item-là**. → optionnel, par question, réservé aux d3–d4 où il change quelque chose.

_Alternative rejetée_ : tout au niveau de la question — pédagogiquement à peine meilleur,
économiquement impossible, et il aurait produit ce que produisent toujours les champs
obligatoires trop chers : des remplissages génériques copiés d'une question à l'autre.

**Authoring**, dans la langue de la matière (comme `explanation` — les matières sont monolingues
par construction, `subjects.content_language`) :

```jsonc
// content/competences/math.json — le registre, deux textes par compétence
{ "id": "math.frac.add-sous",
  "labels": { "fr": "…", "en": "…", "ar": "…" },
  "prereqs": ["math.frac.equivalentes"],
  "scaffold": {
    "orient": "Regarde les dénominateurs : sont-ils les mêmes ?",                 // palier 1
    "rule":   "On n'additionne des fractions que sur un dénominateur commun."     // palier 2
  }
}

// content/math/11-addition-soustraction-fractions/exercices/04-defi.json — le palier 3, optionnel
{ "prompt": "…", "explanation": "…",
  "competencies": ["math.frac.add-sous"],
  "scaffoldDecompose": "Ne fais que l'étape 1 : réduis 1/3 et 1/4 au même dénominateur." }
```

**Gate contenu (nouveau, `content:qa`)** — trois contrôles, tous mécaniques :

1. **appariement** : `scaffoldDecompose` sur une question **sans** `competencies` est une erreur —
   le palier 3 sans les paliers 1–2 est un escalier qui commence à la dernière marche.
2. **complétude du registre** : `orient` et `rule` vont ensemble (l'un sans l'autre est refusé) ;
   une compétence sans `scaffold` est **légale** et simplement muette (R-6).
3. **anti-solution** : la chaîne normalisée de la bonne option (et, pour les types numériques, sa
   valeur) ne doit apparaître dans aucun palier. Le contrôle ne mord en pratique que sur le
   palier 3 — les deux premiers, étant génériques, ne peuvent structurellement pas contenir la
   réponse d'un item particulier. **Niveau à calibrer sur le corpus commité avant de choisir
   `error` ou `warn`** (patron du gate « options citées par lettre », arena #680).

**Service.** `reveal_scaffold_tier(p_question UUID)` (`SECURITY DEFINER`) rend **le palier
suivant seulement**, écrit `scaffold_reveals`, et refuse de sauter un palier (R-19). Il compose
les paliers 1–2 depuis la compétence **principale** de la question (`question_competencies.
is_primary`, é07 R-2) et le palier 3 depuis la question. Une question non taggée n'a aucun
palier : l'escalier est simplement absent, sans message d'erreur (R-6). Aucun coût, aucun
consommable, aucun effet sur la croyance de l'item courant — seulement sur le poids de la preuve
de la **reprise** (R-21).

**Ce que é11 en fera, et ce qu'elle n'en fera pas.** Ces paliers sont **la substance** ; l'étude
11 apporte **la voix**. Son « escalier de registres » (é11 US-3 : concret/analogie → visuel-verbal
→ formel) ne remplace pas cet escalier-ci, il le **reformule** : le LLM reçoit le palier à
délivrer et le dit autrement, dans la bande d'âge et la langue de l'élève. Il ne choisit ni quel
palier servir, ni ce qu'il contient. Sans clé, l'élève lit le texte écrit ; avec clé, il lit le
même contenu dans ses mots à lui. C'est é26 P-5b appliqué à la lettre, et c'est ce qui garantit
que **l'échafaudage existe dans le produit d'aujourd'hui** (§3.13).

### 3.7 La charge cognitive (organe ❻, mandat point 6)

**Le constat qui commande le lot** : il n'existe **aucune latence par item** dans ce dépôt. Le
temps est mesuré à l'exercice (`attempts.duration_seconds`, `exercise_sessions`), et le chrono
récompensé du boss est serveur. Le mandat demande de détecter « un temps de réponse anormalement
long » : cela suppose une donnée qui n'est pas collectée.

**D-7 — `elapsed_ms` est rapporté par le client, borné serveur, et interdit de récompense.**
Le client mesure le temps passé sur chaque item et le joint à la soumission ; le serveur le borne
à `[0 ; 300 000]` ms et le range dans `question_attempts.elapsed_ms`. _Alternative rejetée_ : une
horloge serveur par item — elle exigerait un aller-retour **par question**, donc précisément la
couture que é04 Q-4 a refusé de rouvrir. Le prix de ce choix est qu'un client hostile peut mentir
sur son temps ; c'est acceptable **parce que ce champ n'entre dans aucun barème, aucun XP, aucun
classement, aucun anti-farm** — un mensonge n'achète rien. Il ne sert qu'à rendre le système
**plus indulgent** (R-25), et l'indulgence est bornée par le plafond `p(S) = 0,20`.

**Les trois signaux** (R-23), tous relatifs à l'élève lui-même — jamais à une moyenne de cohorte,
qui punirait les lents :

| signal              | détection                                                                             | réaction (R-24)                                                                  |
| ------------------- | ------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| **lenteur**         | `elapsed_ms > 3 ×` médiane personnelle sur la compétence (≥ 5 mesures, sinon inactif) | `p(S)` au plafond ; proposition de changer de format                             |
| **série d'erreurs** | ≥ 3 erreurs consécutives dans la session                                              | `p(S)` au plafond ; baisse d'un palier de difficulté sur la proposition suivante |
| **piétinement**     | ≥ 10 tentatives sur une compétence sans 3 réussites consécutives                      | remédiation forcée en tête de `resolveNextAction` + proposition de pause         |

Le **piétinement** est le seul des trois qui décrive un échec **du système**, pas de l'élève :
dix tentatives sans maîtrise veulent dire que ce qu'on lui sert ne marche pas. C'est aussi le
seul qui soit un KPI (KPI-4). Sa définition est reprise de la littérature (annexe B.3), et **sa
valeur de départ doit être mesurée avant d'être ciblée** : on ne pose pas d'objectif sur une
grandeur qu'on n'a jamais observée.

**Une proposition, une fois.** Le message de charge est une proposition refusable, plafonnée à
**une par session** (R-24). Un système qui dit trois fois « tu sembles fatigué » devient
l'agression qu'il prétendait éviter.

### 3.8 Modèle de données (migrations, toutes additives)

**(a) `user_competency_mastery` — la croyance rejoint la maîtrise** _(amendement é07, §3.9)_

```sql
ALTER TABLE public.user_competency_mastery
  ADD COLUMN IF NOT EXISTS p_known          NUMERIC NOT NULL DEFAULT 0.20
      CHECK (p_known BETWEEN 0.01 AND 0.99),
  ADD COLUMN IF NOT EXISTS evidence_count   INT     NOT NULL DEFAULT 0,
  ADD COLUMN IF NOT EXISTS sessions_seen    INT     NOT NULL DEFAULT 0,
  ADD COLUMN IF NOT EXISTS forms_seen       TEXT[]  NOT NULL DEFAULT '{}',
  ADD COLUMN IF NOT EXISTS last_evidence_at TIMESTAMPTZ,
  ADD COLUMN IF NOT EXISTS belief_source    TEXT    NOT NULL DEFAULT 'evidence'
      CHECK (belief_source IN ('evidence','inference','placement')),
  ADD COLUMN IF NOT EXISTS inferred_from    UUID REFERENCES public.competencies(id) ON DELETE SET NULL,
  ADD COLUMN IF NOT EXISTS suspect          BOOLEAN NOT NULL DEFAULT false,
  ADD COLUMN IF NOT EXISTS disputed_at      TIMESTAMPTZ;

-- « les compétences dont je suis le moins sûr » (bilan d'entrée, §3.5) : l'incertitude est une
-- distance à 0,5, donc un index sur l'expression, pas sur la colonne.
CREATE INDEX IF NOT EXISTS idx_ucm_user_uncertainty
  ON public.user_competency_mastery (user_id, (abs(p_known - 0.5)));
```

⚠️ **Deux pièges tenus.** (1) Une ligne créée **par inférence** ne touche pas `mastery` : elle
reste à son 50 neutre avec `attempts = 0`, parce que é07 RISK-2 interdit de traiter ce 50 comme
un diagnostic — c'est `belief_source` qui dit à l'écran de rendre « déduit » et non une barre.
(2) `forms_seen` est un tableau et non un compteur : « varié » se vérifie sur des **types
distincts**, et un compteur ne saurait pas si les 4 preuves sont 4 fois le même QCM.

**(b) `question_attempts` — la latence et la source `placement`** _(amendement é04, §3.9)_

```sql
ALTER TABLE public.question_attempts
  ADD COLUMN IF NOT EXISTS elapsed_ms INT CHECK (elapsed_ms BETWEEN 0 AND 300000);

ALTER TABLE public.question_attempts DROP CONSTRAINT IF EXISTS question_attempts_source_check;
ALTER TABLE public.question_attempts
  ADD CONSTRAINT question_attempts_source_check
  CHECK (source IN ('exercise','quiz','dungeon','exam','placement'));
```

Aucun `GRANT` ne bouge : la table est déjà `SELECT`-seule pour `authenticated`, écriture par les
RPC `SECURITY DEFINER` uniquement.

**(c) `competencies` — les deux paramètres écrits** _(amendement é07)_

```sql
ALTER TABLE public.competencies
  ADD COLUMN IF NOT EXISTS p_init    NUMERIC NOT NULL DEFAULT 0.20 CHECK (p_init    BETWEEN 0.02 AND 0.60),
  ADD COLUMN IF NOT EXISTS p_transit NUMERIC NOT NULL DEFAULT 0.15 CHECK (p_transit BETWEEN 0.02 AND 0.40);
```

Compilés depuis `content/competences/<famille>.json` (champs optionnels `pInit` / `pTransit`,
défauts de famille) par `sql-builder` — **jamais écrits à la main en base**.

**(d) `placement_sessions` — le bilan d'entrée** _(nouvelle table)_

```sql
CREATE TABLE IF NOT EXISTS public.placement_sessions (
  id           UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id      UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
  subject_id   TEXT NOT NULL REFERENCES public.subjects(id) ON DELETE CASCADE,
  family       TEXT NOT NULL,
  status       TEXT NOT NULL DEFAULT 'running'
               CHECK (status IN ('running','completed','abandoned','expired')),
  items_served INT  NOT NULL DEFAULT 0,
  started_at   TIMESTAMPTZ NOT NULL DEFAULT now(),
  ended_at     TIMESTAMPTZ
);

-- Une seule session vivante par (élève, matière) — l'unicité partielle est le garde-fou, pas
-- une vérification applicative qui perd la course.
CREATE UNIQUE INDEX IF NOT EXISTS uq_placement_running
  ON public.placement_sessions (user_id, subject_id) WHERE status = 'running';
CREATE INDEX IF NOT EXISTS idx_placement_user_recent
  ON public.placement_sessions (user_id, started_at DESC);

ALTER TABLE public.placement_sessions ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Users read own placement sessions" ON public.placement_sessions
  FOR SELECT USING (user_id = (SELECT auth.uid()) OR public.is_admin());
-- Aucune policy d'écriture : les seuls écrivains sont les RPC SECURITY DEFINER (gotcha grants).
REVOKE ALL ON public.placement_sessions FROM anon, authenticated;
GRANT SELECT ON public.placement_sessions TO authenticated;
GRANT ALL    ON public.placement_sessions TO service_role;
```

Les items servis ne créent **pas** de table : ils vont dans `question_attempts`
(`source = 'placement'`, `session_id = placement_sessions.id`), exactement comme le donjon y va
avec `dungeon_runs.id` — le `session_id` est polymorphe par conception (é04 A0.1).

**(e) `scaffold_reveals` — l'échafaudage consommé** _(nouvelle table)_

```sql
CREATE TABLE IF NOT EXISTS public.scaffold_reveals (
  user_id     UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
  question_id UUID NOT NULL REFERENCES public.questions(id) ON DELETE CASCADE,
  max_tier    INT  NOT NULL DEFAULT 0 CHECK (max_tier BETWEEN 0 AND 3),
  first_at    TIMESTAMPTZ NOT NULL DEFAULT now(),
  last_at     TIMESTAMPTZ NOT NULL DEFAULT now(),
  PRIMARY KEY (user_id, question_id)
);
ALTER TABLE public.scaffold_reveals ENABLE ROW LEVEL SECURITY;
CREATE POLICY "Users read own scaffold reveals" ON public.scaffold_reveals
  FOR SELECT USING (user_id = (SELECT auth.uid()) OR public.is_admin());
REVOKE ALL ON public.scaffold_reveals FROM anon, authenticated;
GRANT SELECT ON public.scaffold_reveals TO authenticated;
GRANT ALL    ON public.scaffold_reveals TO service_role;
```

**(f) Les paliers d'échafaudage — deux colonnes au registre, une à la question** _(D-6bis)_

```sql
ALTER TABLE public.competencies
  ADD COLUMN IF NOT EXISTS scaffold_orient TEXT,
  ADD COLUMN IF NOT EXISTS scaffold_rule   TEXT;

ALTER TABLE public.questions
  ADD COLUMN IF NOT EXISTS scaffold_decompose TEXT;
REVOKE SELECT (scaffold_decompose) ON public.questions FROM anon, authenticated;
```

⚠️ **L'asymétrie de grant est voulue et il faut la comprendre avant d'y toucher.** Les deux
paliers du registre sont **génériques** : les rendre lisibles ne révèle la réponse d'aucun item,
exactement comme les libellés de compétences (é07 lot 1, client-readable). Le palier 3 est
**spécifique à l'item** : il décrit sa première étape, donc il entre dans la même whitelist
d'exclusion que `correct_option` et `distractor_tags` (`20260610170000_hide_answer_key`). Il ne
sort **que** par `reveal_scaffold_tier`, un palier à la fois. Livrer les trois d'un coup au
client, c'est livrer la décomposition complète — donc, sur beaucoup d'items, la réponse.

### 3.9 Les trois amendements (et rien d'autre)

Cette étude ne rouvre aucune décision. Elle amende trois objets, chacun par une modification
**additive** dont le comportement par défaut est **identique à aujourd'hui** :

| #     | Étude propriétaire | Amendement                                                                                                                                                     | Comportement sans tag / sans donnée                             |
| ----- | ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| **A** | **é07**            | `user_competency_mastery` et `competencies` gagnent des colonnes ; `competency_mastery_alpha` / `_with_decay` / la carte / `get_daily_plan` sont **intouchés** | identique                                                       |
| **B** | **é04**            | `question_attempts` gagne `elapsed_ms` et la source `placement`                                                                                                | identique                                                       |
| **C** | **é22**            | `resolveNextAction` gagne deux priorités : `remediate` (rang 2) et `strengthen` (rang 4)                                                                       | identique — les deux ne peuvent pas se déclencher sans croyance |

L'amendement **C** est le seul qui touche une règle de produit (R-31 de é22). Sa justification :
l'ordre actuel place `retry` au rang 2 parce que « reprendre un échec récent vaut mieux
qu'avancer sur du neuf » — c'était **le meilleur proxy disponible d'une cause quand aucune cause
n'était connue**. `remediate` est la même intention avec la cause à la place du symptôme, et
rejouer l'exercice raté sans traiter le prérequis manquant est la définition même du
piétinement. Le nouvel ordre :

```
1. review       (SM-2 dû — la mémoire prime, inchangé)
2. remediate    ← NOUVEAU : une lacune confirmée bloque la frontière ; on remonte à la cause
3. retry        (le dernier exercice raté, inchangé)
4. strengthen   ← NOUVEAU : une compétence « en cours », servie sous une AUTRE forme
5. continue     (la mission suivante du chemin, inchangé)
6. discover     (une matière jamais ouverte, inchangé)
```

Les rangs 2 et 4 rendent `null` dès que la matière n'est pas taggée ; le test de non-régression
exigé est littéral : **sur des données non taggées, `resolveNextAction` rend exactement ce
qu'elle rendait** (§5).

### 3.10 Contrats des lectures (nouvelles RPC, aucune signature existante modifiée)

| RPC                                                                                         | sécurité                                          | rend                                                                                                                                                                                                                                       |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `get_learning_state(p_family TEXT DEFAULT NULL)`                                            | **DEFINER** (appelle les helpers non exécutables) | par compétence : `slug`, libellés, `state` (`maitrisee`/`en-cours`/`fragile`/`lacune`/`inconnue`), `p_known`, `evidence_count`, `sessions_seen`, `forms_count`, `belief_source`, `suspect`, `zone` (`interieur`/`frontiere`/`hors-portee`) |
| `get_learning_frontier(p_family TEXT DEFAULT NULL, p_limit INT DEFAULT 5)`                  | **DEFINER**                                       | la frontière triée : compétence, `p_known`, `unlocks` (fan-out), `entry_exercise_id` (via `get_exercises_for_competency`)                                                                                                                  |
| `get_remediation_path(p_competency TEXT)`                                                   | **DEFINER**                                       | la chaîne de remontée jusqu'à la première compétence non maîtrisée en partant du bas (profondeur ≤ 3), en réutilisant `get_competency_blockers`                                                                                            |
| `start_placement(p_subject TEXT)`                                                           | **DEFINER**                                       | la session (ou l'existante `running`)                                                                                                                                                                                                      |
| `next_placement_item(p_session UUID)`                                                       | **DEFINER**                                       | **un** item : `question_id`, `prompt`, `options` (jamais la clé), `ordinal`, `total_max`                                                                                                                                                   |
| `submit_placement_answer(p_session UUID, p_question UUID, p_choice TEXT, p_elapsed_ms INT)` | **DEFINER**                                       | `{ is_correct, done }` — corrige, écrit la télémétrie, met à jour la croyance, propage                                                                                                                                                     |
| `finish_placement(p_session UUID)`                                                          | **DEFINER**                                       | le résumé : maîtrisées / frontière / lacunes                                                                                                                                                                                               |
| `reveal_scaffold_tier(p_question UUID)`                                                     | **DEFINER**                                       | `{ tier, text }` — le palier **suivant** uniquement                                                                                                                                                                                        |
| `get_calibration_report(p_days INT DEFAULT 30)`                                             | **DEFINER + `is_admin()`**                        | KPI-3 : histogramme (bande de `p_known` prédite × taux de réussite observé)                                                                                                                                                                |

**Invariants de sécurité, sans exception** : aucune de ces fonctions ne prend d'identifiant
d'élève en paramètre — le périmètre est `(SELECT auth.uid())` **en dur**, dans chaque requête
(é07 R-6) ; sans session, `auth.uid()` est `NULL`, le filtre ne rend rien et la fonction renvoie
vide au lieu de lever. La clé de correction ne sort d'aucune : `next_placement_item` sélectionne
`prompt` et `options`, deux colonnes de la whitelist de `20260610170000_hide_answer_key`. La map
`distractor_tags` n'est jamais rendue (é04 D-A1.2-2 : l'option correcte étant la seule sans tag,
la rendre désignerait la bonne réponse par élimination). Et `scaffold` suit la même règle.

### 3.11 Client

```
src/shared/constants/adaptive.ts        ← seuils isomorphes (§3.2), zéro secret, zéro import .server
src/shared/lib/next-action.ts           ← +2 priorités (amendement C), toujours une fonction pure
src/features/progression/
  progression.server.ts                 ← +getLearningState, +getLearningFrontier, +disputeInference
  components/learning-state-map.tsx     ← la carte à 4 états (remplace l'affichage % de é07 lot 4)
  components/frontier-card.tsx          ← « prêt à apprendre » (≤ 3 cartes, jamais une liste)
src/features/tutor/
  tutor.server.ts                       ← lot 3bis : toLearnerContext + le gabarit rendent le bloc mastery
src/features/quest/
  quest.scaffold.ts                     ← revealScaffoldTier (fichier séparé : é04 A1.2 a montré
                                          qu'importer quest.server tire tout le serveur dans le chunk)
  components/scaffold-ladder.tsx        ← les 3 paliers, dans le bloc de correction existant
  components/load-nudge.tsx             ← la proposition de charge, une fois par session
src/features/placement/                 ← NOUVELLE feature (le « 13 → 14 » d'origine est caduc : é11 a créé `tutor`)
  index.ts · placement.server.ts · components/{placement-runner,placement-summary}.tsx
src/routes/_authenticated/bilan.$subjectId.tsx      ← le bilan d'entrée
src/routes/_authenticated/admin.calibration.tsx     ← la console KPI-3
```

⚠️ **Frontière de feature tenue** : `placement` ne peut pas importer `quest` (AGENTS.md — les
features ne s'importent pas). Ce qu'elles partagent — le rendu d'un item et la saisie d'une
réponse — descend dans `@/components/ui` ou `@/shared/lib` **au moment où le lot 3 en a besoin**,
pas avant. Si ce partage s'avère coûteux, le repli est de **ne pas partager** : le bilan sert des
items d'un seul type (`mcq` + `numeric`), la surface est petite.

États TanStack Query : `['learning-state', family]` et `['frontier', family]` invalidés par la
soumission d'un exercice ; le bilan n'utilise **pas** de cache (chaque item est un aller-retour
qui écrit — c'est le seul endroit de l'app où c'est justifié).

### 3.12 Observabilité

Événements structurés via `@/shared/lib/logger` (jamais `console`) :
`belief.updated` (compétence, avant, après, `w`, type d'item) · `belief.inferred` (source, cible,
profondeur) · `belief.disputed` · `placement.started|item|finished|abandoned` (durée, items) ·
`scaffold.revealed` (palier) · `load.detected` (signal, réaction) · `nextaction.resolved` (rang
retenu). Aucun contenu d'item, aucun libellé, **jamais le nom de l'élève** (é26 P-5e).

Deux tableaux d'admin : **calibration** (KPI-3, la courbe qui peut invalider le modèle) et
**piétinement** (KPI-4, la liste des couples (élève, compétence) au-delà du seuil — c'est là que
se lisent les trous du corpus, pas ceux de l'élève).

### 3.13 Articulation avec l'étude 11 (le tuteur) et l'étude 29 (la porte)

Cette section n'est pas un rappel de courtoisie : c'est le contrat qui empêche d'écrire deux fois
la même ligne, et il prolonge la règle de tranchage que é29 a posée en annexe B.

> **É29 dit** : « si la brique parle de pédagogie, elle est à é11 ; si elle parle de qui paie, de
> quel modèle répond, ou de ce que l'élève demande lui-même, elle est à é29. »
>
> **É30 la complète d'un cran** : **ce qui DÉCIDE est ici (é30) · ce qui PARLE est à é11 · ce qui
> PAIE est à é29.** Une brique qui choisit un item, un chemin, un palier ou un moment appartient
> à cette étude, avec ou sans IA. Une brique qui met une décision en mots appartient à é11. Une
> brique qui ouvre un coffre, compte des jetons ou coupe une dépense appartient à é29.

#### (a) Ce que é30 **prend** de l'existant (et ne réécrit pas)

| Brique réutilisée telle quelle                                             | Origine              | Ce que é30 en fait                                            |
| -------------------------------------------------------------------------- | -------------------- | ------------------------------------------------------------- |
| `question_attempts` (+ trigger misconceptions)                             | é04 A0               | y branche un **troisième** trigger, sur le même événement     |
| `user_competency_mastery`, EWMA, oubli à la lecture                        | é07 lot 2            | y ajoute des colonnes ; **n'en modifie aucune formule**       |
| `get_competency_blockers`, `get_exercises_for_competency`                  | é07 lot 4            | les **appelle** pour la remédiation et la frontière           |
| `get_daily_plan` (score à 3 termes, plafond 3)                             | é04 A1.1 + é07 lot 5 | **intouchée** — la révision reste le rang 1                   |
| `get_attempt_review` (erreur nommée, « revoir le cours », « m'entraîner ») | é04 A1.2             | y **accroche** l'escalier d'échafaudage                       |
| `resolve_exercise_access`                                                  | —                    | reste l'arbitre unique (R-16)                                 |
| `normalize_recall_text`, variante rappel                                   | é17 / é20            | fournissent les items **à faible hasard** du §3.2             |
| `resolveNextAction`                                                        | é22                  | **amendée** (+2 priorités), jamais dupliquée en RPC (é22 D-8) |

#### (b) Ce que é30 **donne** à l'étude 11 — re-mesuré sur l'étude **livrée** (2026-08-25)

É11 est **livrée — 8 lots** (2026-08-23/24, dernière branche `claude/etude-11-lots-6-7`, #844).
Ce tableau disait au futur ce que chaque surface gagnerait ; chaque ligne est désormais
**constatée sur `main`** — et le gain reste entier : é11 a livré ses surfaces **sans** les
organes de cette étude, qui les nourriront par le contrat ci-dessous.

| Surface é11 (**livrée**)                                                                                       | Ce qu'elle fait aujourd'hui, mesuré                                                                                                                                              | Ce que é30 lui branche                                                                                                                                                                                |
| -------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Learner Context Pack** — `get_tutor_learner_context` (lot 1 #816, re-défini par `20260823100000`)            | classe, bande d'âge, objectif, bandes niveau/série, **misconceptions actives** (é04, tag + libellés ×3), intérêts, verbosité — **aucune ligne de maîtrise, ni faible/forte, ni proxy** | **lot 3bis** : le bloc `mastery` (états + frontière + prérequis bloquant, jamais `p_known` brut) — la seule information qu'un tuteur humain demanderait en premier : _où l'élève en est, où il est prêt à aller_ |
| **P5 — difficulté & rythme** (US-13)                                                                            | l'intention « probabilité de réussite estimée 60-80 % » est écrite ; `difficulty_adaptation` dort toujours (Q-4) — é11 a livré **sans** la brancher                                | `P(réussite) = p·(1−S) + (1−p)·G` par item (annexe A.5) : l'inégalité devient calculable, et le sélecteur la vise (§3.4, `ZPD_TARGET`)                                                                |
| **P4 — exercices ciblés** (lot 5 : `20260823150000_tutor_targeted_practice` + fallback Q-8, seuil en SQL)       | cible la compétence **où l'erreur s'est vue** (misconception → compétence, é04 A12)                                                                                               | `get_remediation_path` (lot 4) : la **cause racine** — le prérequis manquant, pas le symptôme                                                                                                          |
| **P1 — explications** (`/api/tutor/stream`, cache d'explications, escalade en 5 marches)                        | reformule l'explication canonique et le cours, dans le registre de l'élève                                                                                                        | l'escalier de **substance** (orient → rule → decompose, lots 5·9 différés) : le LLM reformulera un palier qu'on lui donne au lieu d'inventer son contenu                                               |
| **P2 — plan du jour commenté** (lot 2, bibliothèque de coaching **zéro token**)                                 | raisons issues des misconceptions + du plan é04/é07                                                                                                                               | l'état et la cible (« _tu es prêt pour Thalès : il ne te manque que la proportionnalité_ ») via `get_learning_state`                                                                                   |
| **P6 — bilans hebdo** (lot 6 : `tutor_digests`, batch sur le chemin plateforme)                                 | agrégats d'activité et de faiblesses                                                                                                                                              | des compétences **déclarées maîtrisées avec leur preuve** (« prouvé 4 fois, sous 3 formes ») — ce qu'un parent peut lire sans y croire sur parole                                                       |

**Les deux règles que é30 avait posées « pour que é11 n'ait pas à les re-décider » — bilan
après livraison** :

- **la vérification du tuteur est une preuve à poids réduit** : la règle **survit, sa détection
  change**. É11 lot 4 n'a pas créé de source `'tutor'` — le mini-check écrit
  `source = 'exercise'` avec `session_id =` le fil. Le poids `w = 0,5` se reconnaît donc **au
  fil**, pas à la source (§3.2, contrat du lot 1). Rien à changer côté é11 : sa couture livrée
  suffit.
- **rien de ce que le tuteur écrit n'entre dans une croyance** : **tenu par construction, et
  vérifié dans la RPC livrée** — elle n'insère dans `question_attempts` que pour une question du
  catalogue (`exercise_source = 'admin'`), et un item de la Forge n'y a pas de FK (§3.13c). Une
  explication, un encouragement, un quiz forgé : zéro preuve.

**Et le froid du démarrage, nommé pour la réévaluation Q-7** : pour un élève neuf, le pack livré
est presque vide — aucune misconception, aucune maîtrise, des bandes par défaut. Le tuteur parle
alors **sans rien savoir de l'élève**, exactement comme la carte. L'organe qui remplit ce vide en
cinq minutes est le **bilan d'entrée (lot 7, différé)**. Ce n'est pas un argument pour le
dé-différer aujourd'hui : c'est la pièce à verser au dossier quand la charpente aura rencontré
son public.

#### (c) Ce que é30 **doit** à l'étude 29 — et l'invariant qu'elle tient

**D-8 — é30 n'ouvre aucune surface IA, et ne peut pas en ouvrir par accident.** Aucun des dix
lots n'ajoute de valeur à `AI_FEATURES` (`src/shared/constants/ai.ts`), n'appelle
`resolve_ai_access`, ne touche `ai_usage_events`, ni ne consomme d'énergie. La vérification est
mécanique et gratuite : le CHECK de `ai_usage_events.feature` **refuse** en base toute surface
non déclarée par une migration (é29 §3.3) — une dérive n'échouerait pas en revue, elle
échouerait à l'écriture.

**Conséquence produite, et c'est la raison d'être de cette étude** : les six mécanismes du mandat
fonctionnent **avec `AI_KEY_ENC_KEY` absente**, c'est-à-dire dans le produit qui tourne
aujourd'hui en production. Une famille qui branche sa clé n'obtient pas un autre produit : elle
obtient **le même, mis en mots**. C'est é29 R-1 (« le produit sans clé est le produit
d'aujourd'hui ») appliqué à l'adaptatif.

**Le seul point de contact, et il va dans le bon sens : la Forge.** `ai_forged_quizzes` accepte
déjà `scope = 'competency'` avec un `competency_id TEXT` **volontairement sans clé étrangère**
(é29 §3.3). É30 lui donne **laquelle** : la compétence de la frontière, ou celle du prérequis
bloquant. Aucune ligne de é29 ne change ; c'est un paramètre mieux choisi, rien de plus.

**Et ce paramètre a maintenant un chemin livré, donc il lui faut un porteur** _(précisé le
2026-08-25 — é29 et é11 sont closes toutes les deux)_. La chaîne P4 existe sur `main` :
`get_targeted_exercises` sélectionne par erreur nommée (é11 lot 5, `20260823150000`) et
`tutor_practice_needs_generation` tient la porte Q-8 vers la Forge (seuil « ≥ 3 questions
fraîches », en SQL et nulle part ailleurs — elle **appelle** sa voisine, jamais ne la recopie).
Aujourd'hui cette chaîne vise la compétence **où l'erreur s'est vue**. Le branchement « cause
racine » promis par le tableau (b) — viser le prérequis manquant quand une remontée existe —
est du même genre que l'amendement D : une couture sur une surface dont l'étude propriétaire
est close. Il appartient donc au **lot 4**, qui livre `get_remediation_path` et rebranche sa
première consommatrice dans la même PR : `get_targeted_exercises` sert la cause racine quand
une lacune confirmée existe en amont du tag visé, et la Forge — quand Q-8 l'ouvre — reçoit ce
`competency_id`-là. Sans croyance, sans graphe, sans remontée : sélection **identique à
aujourd'hui** (R-6, assertion littérale au lot 4).

⚠️ **Et une conséquence contre-intuitive qu'il faut assumer** : un quiz de la Forge **ne fait
bouger aucune croyance**. Ce n'est pas un oubli, c'est structurel — `question_attempts.question_id`
porte une clé étrangère vers `public.questions`, et un item forgé n'y existe pas ; é29 l'écrit
d'ailleurs en toutes lettres (« aucune écriture dans `question_attempts`, `attempts` ni
`spaced_repetition_schedule` »). Un élève peut donc enchaîner vingt questions forgées sans voir
sa carte bouger. **L'UI doit le dire** — « _cet entraînement ne compte pas dans ta progression_ »
— sinon c'est vécu comme un bug. C'est le prix, accepté, d'un contenu que personne n'a relu.

**Mesure du 2026-08-25 qui cadre l'articulation entière** : `AI_KEY_ENC_KEY` n'est posée nulle
part et **aucune clé de famille n'a jamais été branchée** (STATUS 2026-08-24 — le pilote Q-9 de
deux semaines n'a pas commencé). É11 est donc livrée **et muette pour 100 % des élèves**. Ce
n'est pas un échec de é11, c'est sa conception (é29 R-1) — mais il faut le lire dans le bon
sens : la seule voie qui élève **aujourd'hui** le produit vers les trois références est la voie
déterministe de cette étude. Le tuteur la racontera à ceux qui brancheront une clé ; la
charpente, elle, sert tout le monde.

#### (d) L'amendement D devient le lot 3bis — le pack du tuteur apprend la maîtrise

_(Réécrit le 2026-08-25. L'historique tient en trois états : à la **rédaction**, é11 n'avait
aucune ligne de code et l'amendement était documentaire ; à l'**arbitrage**, une session
exécutait é11 lots 2 → 7 et la règle était « le lot 3 n'édite aucun fichier de é11 —
l'amendement se porte par la session propriétaire » ; depuis le **2026-08-24**, é11 est
**livrée et close** — la session propriétaire n'existe plus, et un amendement sans porteur est
un amendement qui ne se fera pas. É30 en hérite donc, en lot propre.)_

| #     | Étude           | Amendement                                                                                                                        | Porteur                                                                                                                            |
| ----- | --------------- | ---------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| **D** | **é11** (close) | `get_tutor_learner_context` gagne un bloc `mastery` ; US-13 cite `P(réussite)` calculée (§3.4) au lieu de `difficulty_adaptation` | **é30 lot 3bis** — é11 n'ayant plus de session, le protocole du dépôt (un lot, une PR, un jeu de fichiers) désigne l'étude vivante |

**Le contrat du lot 3bis, et les décisions de é11 qu'il tient** :

- **il n'ajoute au pack que le bloc `mastery`**, composé des mêmes helpers que
  `get_learning_state` (lot 3) : jusqu'à **3** compétences `maitrisee` (les plus récentes),
  jusqu'à **3** de la **frontière**, jusqu'à **2** prérequis **bloquants** — slug + libellé dans
  la langue de la matière + état. **Jamais `p_known` brut** : le pack part vers un modèle qui
  peut le répéter à l'élève, et D-1 dit que la probabilité ne s'affiche que dans la console
  d'admin.
- **le budget du pack est une décision de é11, et elle est tenue** : ~1 000-1 200 tokens
  (é11 §2.2). Le bloc est borné par ses plafonds (3+3+2, de l'ordre de 150 tokens sur fixture)
  et **la mesure avant/après fait partie de l'acceptation**. Rien n'est retiré du pack existant
  pour le faire entrer.
- **R-6 s'applique au pack comme aux écrans** : matière non taggée ou aucune croyance → la clé
  `mastery` est **absente**, et le prompt de é11 rend exactement ce qu'il rend aujourd'hui. Le
  pgTAP l'affirme littéralement (§5).
- **le périmètre de fichiers est celui de la couture, pas de l'étude** : la migration
  `CREATE OR REPLACE` de `get_tutor_learner_context` (troisième redéfinition — é11 lot 1 puis
  `20260823100000` l'ont déjà fait, le patron existe), le consommateur TS (`toLearnerContext`,
  `tutor.server.ts`) et le gabarit de prompt qui rend le bloc. **Rien d'autre de é11 n'est
  touché** — ni le chat, ni le mini-check, ni les digests, ni l'énergie.

---

## 4. Plan d'exécution en lots

Chaque lot est **une PR mergeable, gate verte, utile seule**. Trois lots sont du **contenu** et se
livrent dans le dépôt **privé** (0 · 0bis · 9) ; les neuf autres sont du **moteur** et se livrent
dans l'arena.

| lot                      | contenu (résumé)                                                                                                                                 | objets créés                                             | tests exigés                                                 | dépend de               |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------- | ------------------------------------------------------------ | ----------------------- |
| ~~**0**~~ _(contenu, privé)_ | ✅ **LIVRÉ le 2026-08-22** (#219) — **1 049 tags** sur les **20** chapitres de `math` 9ᵉ (l'étude en annonçait 13), registre 56 → **154 entrées**, **appliqué en prod** le 2026-08-23 | `content/math/**`                                        | verts                                                        | —                       |
| ~~**0bis**~~ _(contenu, privé)_ | ✅ **LIVRÉ le 2026-08-25** — **Trancher les 297 questions non taguées** (Q-5) : lire une vingtaine de distracteurs et statuer — erreur nommable manquante au registre, ou distracteur qui n'en encode simplement aucune. Tagger ce qui doit l'être, **documenter la règle** pour les campagnes suivantes | `content/math/**`, `content/misconceptions.json`, la règle dans la méthode | `content:qa:strict` ; **mesure de couverture avant/après** | 0 |
| **1** _(moteur)_         | **Le socle de croyance** : colonnes, `belief_guess`/`belief_slip`, trigger `record_competency_belief`, script de calibration                     | migration + 3 fonctions SQL + `adaptive.ts`              | pgTAP (≥ 14 assertions), Vitest constantes                   | —                       |
| **2** _(moteur)_         | **L'inférence** : `propagate_competency_belief`, `belief_source`/`inferred_from`/`suspect`, **mesure de perf avant/après**                       | 1 fonction + 1 trigger                                   | pgTAP (≥ 10), **relevé de perf**                             | 1                       |
| **3** _(moteur)_         | **Les lectures & la carte** : `get_learning_state`, `get_learning_frontier`, la carte à 4 états, « prêt à apprendre »                            | 2 RPC + 2 composants + i18n ×3                           | pgTAP (≥ 8), Vitest composants, `build:check`                | 2                       |
| **3bis** _(moteur)_      | **Le pack du tuteur apprend la maîtrise** (amendement D, §3.13d) : bloc `mastery` de `get_tutor_learner_context`, consommateur TS, gabarit de prompt | 1 migration (`CREATE OR REPLACE`) + TS | pgTAP (≥ 6, dont « pack inchangé sans tag »), Vitest pack, **mesure tokens avant/après** | 3 |
| **4** _(moteur)_         | **La décision** : amendement C (`resolveNextAction` +2 priorités), `get_remediation_path`, rebranchement **cause racine** de `get_targeted_exercises` (§3.13c)                                                        | 1 RPC + `next-action.ts` + 1 `CREATE OR REPLACE`         | Vitest **non-régression littérale**, pgTAP (≥ 8)             | 3                       |
| **5** _(moteur)_         | **L'échafaudage** : schéma contenu, gate anti-solution, colonnes, `reveal_scaffold_tier`, l'escalier dans le bloc de correction, poids de preuve | migration + RPC + `quest.scaffold.ts` + composant + gate | pgTAP (≥ 8), Vitest gate + composant, e2e                    | 1 (poids) · 4 (reprise) |
| **6** _(moteur)_         | **La charge cognitive** : `elapsed_ms`, les 3 signaux, la réaction graduée, `p(S)` sous charge, **mesure de départ de KPI-4**                    | migration + détecteur + composant                        | pgTAP (≥ 6), Vitest détecteur                                | 1                       |
| **7** _(moteur)_         | **Le bilan d'entrée** : `placement_sessions`, les 4 RPC, la feature `placement`, la route                                                        | migration + 4 RPC + feature + route                      | pgTAP (≥ 12), Vitest, **e2e Playwright**                     | 3                       |
| **8** _(moteur)_         | **Les consoles** : calibration (KPI-3) et piétinement (KPI-4)                                                                                    | 1 RPC + 1 route admin                                    | pgTAP (≥ 4), Vitest                                          | 1 · 6                   |
| **9** _(contenu, privé)_ | **L'échafaudage écrit** : `orient` + `rule` sur les 62 compétences `math` ; palier 3 sur les d3–d4                                               | `content/competences/math.json`, `content/math/**`       | gates contenu (dont le nouveau)                              | 5                       |

- [x] Lot 0 — tagger les distracteurs de `math` 9ᵉ _(contenu, dépôt privé)_ — **livré #219, appliqué en prod**
- [x] Lot 0bis — trancher les 297 questions non taguées _(contenu, dépôt privé)_ — **livré**, couverture 64 % → **81 %**, règle de décision écrite
- [x] Lot 1 — le socle de croyance — **livré arena#856**
- [x] Lot 2 — l'inférence dans le graphe — **livré arena#857**, relevé de perf au §8
- [x] Lot 3 — les lectures & la carte à 4 états — **livré arena#858**
- [x] Lot 3bis — le pack du tuteur apprend la maîtrise _(amendement D)_ — **livré arena#859**
- [x] Lot 4 — la décision (amendement é22) — **livré arena#860**
- [ ] Lot 5 — l'échafaudage
- [ ] Lot 6 — la charge cognitive
- [ ] Lot 7 — le bilan d'entrée
- [ ] Lot 8 — les consoles de calibration et de piétinement
- [ ] Lot 9 — l'échafaudage écrit _(contenu, dépôt privé)_

### 4.1 Le périmètre retenu (arbitrage Q-7 du 2026-08-23)

Ce n'est plus un repli si la file se resserre : c'est **le périmètre décidé**.
**Lots 0bis · 1 · 2 · 3 · 3bis · 4** — la preuve, puis la charpente : croyance ❶, inférence ❷,
frontière ❹, le **branchement du tuteur livré** (3bis — seul ajout de la révision du
2026-08-25 : l'amendement D a perdu son porteur quand é11 a fermé, §3.13d ; il se détache
proprement si l'arbitrage le veut) et la décision que la frontière rend possible. Ils tiennent
la promesse principale
(« ce que tu maîtrises · ce que tu es prêt à apprendre · ce qui te bloque ») et rallument le
différenciateur de la scorecard é28 (sa **ligne 3**, STATUS §1bis — à ne pas confondre avec le
KPI-3 de calibration du §1.4).

**Les lots 5 à 9 sont différés, pas gelés** : chacun reste autonome et reprenable tel quel. La
réévaluation se fait quand la charpente aura **rencontré un public** — le motif de Q-7 étant que
la scorecard place le goulot sur l'acquisition, et qu'une charpente démontrable **sert**
l'acquisition au lieu de lui faire concurrence.

~~⚠️ **Le lot 0bis passe avant tout code.**~~ **Fait le 2026-08-25** — et l'estimation était
fausse : l'étude annonçait « une vingtaine de distracteurs à lire », il y en avait **890** sur
297 questions. Ce qu'il rend à la file n'est pas un chiffre mais une **règle** : le champ vide
est désormais une décision documentée (§8), donc les lots 1 à 4 mesurent sur un corpus dont on
sait ce que son incomplétude veut dire. **La file démarre au lot 1.**

### 4.2 Détail, critères d'acceptation et stop-points

**Lot 0 — tagger les distracteurs (`math` 9ᵉ)** · _dépôt privé_
Périmètre : les 13 chapitres de `content/math/**`, chaque distracteur de QCM recevant son
`misconceptionTag` parmi les 56 entrées existantes (le registre est **déjà** complet et pourvu de
ses `competency` — ne pas le refaire).
Acceptation : `content:qa:strict` vert · **0 distracteur non taggé** sur les d3–d4 · l'option
correcte n'en porte jamais (le schéma le refuse déjà).
Stop-point : ne pas étendre à d'autres matières dans cette PR ; ne pas toucher au registre.

**Lot 1 — le socle de croyance**
Acceptation : sur un corpus taggé, une réponse juste en `short_answer` fait passer une croyance
de 0,20 à ≥ 0,90 en **un** item ; il faut **≥ 3** QCM à 4 options pour le même résultat · sur un
corpus **non taggé**, `user_competency_mastery` est strictement inchangée (aucune ligne créée) ·
`get_daily_plan` rend le **même** plan qu'avant le lot (assertion littérale) · le script
`scripts/adaptive/calibration.mjs` produit le tableau de KPI-3 en lecture seule · une ligne
`question_attempts` dont `session_id` est un fil `tutor_threads` pèse `w = 0,5` (§3.2 —
assertion pgTAP sur une fixture de fil).
Stop-point : **ne pas** écrire l'inférence, **ne pas** afficher `p_known` dans une surface élève.

**Lot 2 — l'inférence**
Acceptation : établir `p_known ≥ 0,85` sur une compétence de profondeur 3 relève ses prérequis de
profondeur 1 et 2, **jamais** au-delà de 0,90, **sans** toucher `evidence_count` ni `forms_seen` ·
une lacune confirmée ne baisse **aucune** croyance et pose `suspect` · **relevé de performance
obligatoire** : temps de `submit_exercise_attempt` avant/après le lot, sur un jeu d'au moins 20
questions, mesuré **sur les deux appelants** (soumission d'exercice **et** donjon).
Stop-point : profondeur 2, pas 3 ; pas de recalcul par lot nocturne.

**Lot 3 — les lectures & la carte**
Acceptation : la carte affiche 4 états et **jamais** un pourcentage de croyance · une compétence
`belief_source = 'inference'` est rendue « déduit » avec le geste « je ne suis pas d'accord »
(US-3/R-10) · sur une matière non taggée, l'écran est **identique** à celui d'aujourd'hui · FR/EN/AR

- RTL vérifiés au pixel sur une phrase mixte texte/chiffres.
  Stop-point : **ne pas** modifier `get_my_competency_map` (é07 lot 4 reste servie ; sa retraite est
  une décision de é07, pas d'ici).

**Lot 3bis — le pack du tuteur apprend la maîtrise** _(amendement D, §3.13d — ajouté le 2026-08-25)_
Acceptation : sur une fixture taggée avec croyances, le pack porte `mastery` (≤ 3 maîtrisées ·
≤ 3 frontière · ≤ 2 bloquants — états et libellés, **jamais** `p_known` : recherche de motif
dans le JSON rendu, pas seulement clé absente) · sur une matière non taggée ou sans croyance,
le pack est **octet pour octet** celui d'aujourd'hui · la taille du pack est mesurée avant/après
sur la même fixture et reste sous le budget é11 (~1 200 tokens) · le gabarit de prompt rend le
bloc en langage élève.
Stop-point : ne toucher **aucune** autre surface de é11 (chat, mini-check, digests, énergie) ;
ne pas réordonner le pack existant ; pas de percentile, pas de comparaison de cohorte.

**Lot 4 — la décision**
Acceptation : le test de non-régression est **littéral** — sur les fixtures existantes de
`next-action.test.ts`, `resolveNextAction` rend **exactement** ce qu'elle rendait · `remediate`
ne se déclenche qu'avec une lacune confirmée en amont d'une compétence de la frontière ·
`strengthen` propose un item d'un **type différent** de celui déjà réussi (à types distincts
égaux, celui dont `P(réussite)` prédite tombe dans `ZPD_TARGET`, §3.4) · les deux rendent
`null` sans croyance · `get_targeted_exercises` sert la **cause racine** quand une lacune
confirmée existe en amont du tag visé, et sa sélection est **identique à aujourd'hui** sans
croyance (assertion littérale, R-6) — la porte Q-8 (`tutor_practice_needs_generation`) n'est
pas touchée : elle hérite du rebranchement en appelant sa voisine.
Stop-point : pas de nouvelle RPC de décision (é22 D-8) ; le moteur reste la fonction TS
partagée ; côté é11/é29, ne toucher que `get_targeted_exercises` (un `CREATE OR REPLACE`) —
ni la porte Q-8, ni la Forge, ni ses budgets.

**Lot 5 — l'échafaudage**
Acceptation : les paliers se révèlent dans l'ordre et un seul à la fois · le palier 3 ne quitte
jamais le serveur autrement que par la RPC · **le gate anti-solution est calibré sur le corpus
commité avant de choisir son niveau** · une réussite après palier 3 pèse `w = 0,25` (vérifié en
pgTAP sur la croyance résultante) · aucun consommable n'est débité (assertion explicite).
Stop-point : ne rien écrire dans le corpus (c'est le lot 9) ; ne pas toucher `consume_hint`.

**Lot 6 — la charge cognitive**
Acceptation : `elapsed_ms` hors bornes est **clampé**, jamais rejeté (une soumission ne doit
jamais échouer pour un chrono) · aucune valeur de `elapsed_ms` n'atteint un calcul d'XP, de
classement ou d'anti-farm (assertion par recherche dans le code, pas seulement par test) · le
message de charge n'apparaît **pas deux fois** dans une session · KPI-4 a une valeur de départ
mesurée et écrite au §8.
Stop-point : ne pas toucher le chrono serveur du boss (é09) ; pas de détection d'émotion, pas de
webcam, pas de signal comportemental hors des trois listés.

**Lot 7 — le bilan d'entrée**
Acceptation : ≤ 20 items, arrêt anticipé effectif (médiane mesurée et écrite au §8) · abandon à
l'item _n_ conserve les _n_ croyances déjà écrites · aucune note, aucun classement, XP d'une
session normale · une seule session `running` par (élève, matière), garantie par l'index unique
partiel · e2e Playwright : démarrer, répondre 5 items, quitter, revenir, terminer.
Stop-point : une seule matière à la fois ; pas de bilan multi-matières ; pas de re-passage avant
60 jours.

**Lot 8 — les consoles**
Acceptation : la courbe de calibration est lisible et la bande `[0,7 ; 0,8]` affiche son taux
observé (KPI-3) · le tableau de piétinement trie par (compétence, nombre d'élèves) — **c'est un
outil de diagnostic du corpus, et l'écran doit le dire.**
Stop-point : réservé à `is_admin()` ; aucune donnée nominative.

**Lot 9 — l'échafaudage écrit** · _dépôt privé_
Acceptation : 62 `orient` + 62 `rule` · palier 3 sur **au moins** les d4 · gate vert · relecture
indépendante (l'auto-relecture de l'auteur ne compte pas).
Stop-point : ne pas écrire de paliers pour une matière non taggée en compétences.

---

## 5. Stratégie de test

**pgTAP (le gros du poids — toute la logique est en SQL).** Suite dédiée
`supabase/tests/adaptive_belief_test.sql` et suivantes. Les assertions qui comptent :

1. **La table de vérité BKT** — pour chaque type d'item, la croyance après une réponse juste et
   après une réponse fausse, comparée à la valeur calculée à la main dans le commentaire du test.
   C'est le seul endroit du dépôt où un nombre magique est légitime : il est **dérivé et montré**.
2. **La borne d'inférence** — aucune séquence d'inférences, si longue soit-elle, ne porte une
   croyance au-dessus de `0,90` ni ne crée une compétence `maitrisee`. Test par **attaque** :
   on cherche à faire déclarer une maîtrise sans preuve, on vérifie que c'est impossible.
3. **L'asymétrie** — une lacune confirmée ne baisse aucune croyance de prérequis (D-3).
4. **La neutralité du non-taggé** (R-6) — le test central de non-régression : sur un jeu de
   fixtures **sans** compétence et **sans** tag, `get_daily_plan`, `get_my_competency_map` et le
   contenu de `user_competency_mastery` sont **identiques** avant et après toute la série de lots.
5. **La clé ne sort pas** — `next_placement_item` et `reveal_scaffold_tier` jouées en attaque :
   ni `correct_option`, ni `distractor_tags`, ni `scaffold_decompose` d'un autre palier. Trois
   assertions d'attaque, pas le cas nominal (patron é04 A1.2a).
6. **RLS** — aucune fonction ne rend la ligne d'un autre élève, y compris avec un identifiant
   forgé en paramètre (elles n'en prennent pas : le test le prouve par la signature).
7. **Grants** — chaque table nouvelle a ses `GRANT` explicites (le piège documenté d'AGENTS.md :
   un `CREATE TABLE` sans grant passe en cloud et casse la suite sur une base fraîche).
8. **Le poids du fil** (lot 1) — une soumission dont `session_id` est un fil `tutor_threads`
   pèse `w = 0,5` ; la même soumission avec un `session_id` d'exercice pèse plein. Deux
   assertions jumelles, mêmes fixtures, seul le fil change (§3.2).
9. **Le pack** (lot 3bis) — sans tag : identique octet pour octet ; avec croyances : le bloc
   `mastery` présent et **aucun** `p_known` dans le JSON rendu (recherche de motif).

**Vitest (co-localisé).** `next-action.test.ts` étendu — dont **la non-régression littérale** sur
les fixtures existantes ; les constantes de `adaptive.ts` ; le détecteur de charge (fonction
pure) ; le gate anti-solution ; les composants de carte et d'escalier (Testing Library, dont RTL).

**Playwright (e2e, projet TEST dédié).** Un seul parcours, mais complet : lancer un bilan
d'entrée, répondre, quitter en cours, revenir, terminer, voir la carte. C'est le seul flux de
l'étude qui traverse tout, et le seul qu'un test unitaire ne peut pas prouver.
⚠️ Rappel opératoire : `verify` ne voit **aucun** fichier de `e2e/` — un libellé renommé casse
Playwright et fusionne vert. Le lot 7 doit donc **lire le décompte** du run e2e, pas sa conclusion.

**`db:check-chain`.** Chaque migration de cette étude doit rejouer sur une base **vierge** : les
`ALTER TABLE` de `competencies` et `user_competency_mastery` arrivent après les migrations é07
qui les créent, et aucun INSERT ne dépend de lignes absentes du dépôt public.

**Ce qui prouve la non-régression de l'existant**, en une phrase : **les trois quarts des
assertions de cette étude portent sur ce qui ne doit PAS changer.** C'est voulu. Une étude qui
greffe quatre organes sur un moteur en production se juge d'abord à ce qu'elle n'a pas cassé.

---

## 6. Risques & mitigations

- **RISK-1 — le moteur est en avance sur son corpus, et cette étude aggrave l'écart.**
  _Probabilité : certaine. Impact : elle est inerte._ Sans le lot 0, huit lots de code tournent
  sur du vide — c'est exactement l'histoire de é04 A1.2, livrée complète et éteinte depuis trois
  semaines, et de é07 lot 5, correcte et sans effet. **Mitigation** : le lot 0 est le premier, il
  est **non négociable** (§4.1), et chaque lot moteur porte un critère d'acceptation mesuré **sur
  la matière taggée**. Un lot dont l'effet n'est pas observable sur `math` 9ᵉ n'est pas livré.
- **RISK-2 — le modèle est mal calibré et ment poliment.** _Probabilité : moyenne. Impact :
  grave — un diagnostic faux est pire que pas de diagnostic._ **Mitigation** : KPI-3 est un
  **critère d'invalidation**, pas un indicateur de confort ; le script de calibration est livré
  **au lot 1**, avant toute surface élève ; et parce que rien n'est ajusté (D-2), une dérive se
  corrige en changeant une constante montrée, pas en ré-entraînant une boîte noire.
- **RISK-2bis — KPI-3 rougit sur du bruit et ouvre la porte IRT pour rien.** _Né de l'arbitrage
  **Q-6**, qui retire la condition des 12 mois : la mesure décide seule, donc la mesure doit
  être fiable seule._ _Probabilité : **élevée** sans garde-fou — le produit a peu d'usage, c'est
  la ligne 1 de la scorecard._ **Mitigation décidée** : `n ≥ 100` par bande, en dessous la bande
  est « non concluante » (§1.4) ; le `n` est affiché partout où le taux l'est ; et la décision
  d'ouvrir la porte se prend sur **deux relevés successifs** concluants, jamais sur un seul.
  Sans ces trois-là, Q-6 remplacerait une constante explicable par une estimation plus fragile
  qu'elle — l'inverse exact de l'intention.
- **RISK-3 — le bilan d'entrée décourage.** _Probabilité : haute (c'est le reproche classique
  fait à ALEKS). Impact : abandon à l'entrée._ **Mitigation** : facultatif, interruptible,
  ≤ 20 items, **aucune note**, arrêt anticipé, XP normal, et une sortie qui montre ce qu'on
  **sait déjà** avant ce qui manque. Si la médiane d'abandon dépasse 30 % au lot 7, le bilan
  passe à ≤ 12 items — décision prise d'avance, pas à étudier.
- **RISK-4 — « maîtrise » sans verrou déçoit l'attente du mandat.** _Probabilité : moyenne._
  Bloom demande de ne pas avancer avant 80–90 % ; é22 a retiré les faux verrous. **Mitigation** :
  D-3 (avertissement motivé + remédiation proposée, jamais un blocage), et **Q-1** porte
  l'arbitrage à l'humain plutôt que de le trancher dans le dos de é22.
- **RISK-5 — le trigger d'inférence coûte cher sur le chemin chaud.** _Probabilité : moyenne._
  La soumission d'exercice est déjà le chemin le plus sollicité. **Mitigation** : propagation à
  la **traversée de bande** seulement, profondeur 2, index dédié, et une **mesure obligatoire sur
  les deux appelants** au lot 2 — parce que dans ce dépôt une réécriture SQL a déjà guéri un
  appelant en empoisonnant l'autre.
- **RISK-6 — l'inférence se trompe sur un élève qui a bien deviné.** _Probabilité : faible mais
  certaine à l'échelle._ **Mitigation** : plafond 0,90, jamais de maîtrise déclarée (D-4),
  contestation en un geste (D-5), et la première preuve contraire écrase l'inférence.
- **RISK-7 — `elapsed_ms` est falsifiable.** _Probabilité : haute. Impact : nul par
  construction._ Le champ n'ouvre sur aucune récompense (D-7) et son seul effet est de rendre le
  système **plus indulgent**, dans une borne. **Mitigation** : l'assertion « aucun chemin de
  `elapsed_ms` vers un barème » est un test, pas une intention.
- **RISK-8 — la dette d'échafaudage devient infinie.** _Probabilité : elle l'était._ 22 146
  questions × 3 paliers = ~66 000 textes. **Mitigation** : D-6bis ramène la dette à **124 textes
  pour toute la matière** + un palier 3 optionnel sur les seuls d3–d4.
- **RISK-9 — quatre organes de plus, quatre boucles mortes de plus.** _Probabilité : réelle —
  c'est le diagnostic de é26 sur ce dépôt._ **Mitigation** : chaque lot livre **sa surface
  visible dans la même PR** (la doctrine é26 P-1), et les deux consoles du lot 8 existent pour
  qu'un organe éteint se voie.
- **RISK-10 — l'étude est écrite pendant que le vrai goulot est ailleurs.** _Probabilité :
  certaine._ La scorecard é28 dit que le point dur du projet est **zéro canal d'acquisition**,
  pas la finesse du moteur. **Mitigation** : c'est dit ici, en toutes lettres (§7 Q-7), et le
  lot 0 est précisément la ligne M-1 de é28 — le seul point où cette étude et la scorecard se
  rejoignent.

---

## 7. Questions — **TOUTES ARBITRÉES le 2026-08-23 par Mohamed**

> **Cinq sur les recommandations, deux contre** (Q-5 et Q-6). L'étude est réécrite en
> conséquence — mitigations comprises — et non simplement annotée : c'est la règle de ce dossier.
> Les deux arbitrages contraires sont les plus intéressants, et ils vont dans des directions
> opposées : Q-5 **ralentit** (finir avant d'élargir), Q-6 **accélère** (ouvrir la porte IRT sans
> attendre). Aucun des deux ne change une décision d'architecture ; les deux changent la file.

- **Q-1 — la maîtrise verrouille-t-elle ? → NON. Conseiller, jamais bloquer.** _(sur la
  recommandation)_ Le système avertit et propose la remédiation ; l'exercice reste jouable.
  **Conséquence** : **D-3 et R-17 sont confirmés tels quels**, é22 n'est pas rouverte, et le lot 4
  ne livre aucun verrou. Le garde-fou contre l'entêtement n'est pas une porte, c'est le
  **piétinement** (lot 6, R-23) : dix tentatives sans maîtrise décrivent un échec du système, et
  c'est lui qui déclenche la remontée.
- **Q-2 — la maille des compétences ? → RESTER à ~62 par matière-année.** _(sur la
  recommandation)_ **Conséquence** : le registre `math` ne bouge pas, le tagging de C4bis est
  capitalisé, aucune dette créée. La porte se rouvre **par la mesure et seulement par elle** : si
  KPI-3 montre que 62 compétences sont trop grossières pour prédire, on éclatera les plus
  chargées — pas avant, et pas par conviction.
- **Q-3 — à qui proposer le bilan d'entrée ? → À TOUS, une fois par matière.** _(sur la
  recommandation)_ Refusable, interruptible, rejouable après 60 j, **entrée discrète** pour les
  élèves déjà actifs — leur croyance est déjà nourrie par le jeu, le bilan ne comble que les
  compétences jamais touchées. **Conséquence** : R-11 est confirmé, et le lot 7 livre **deux**
  points d'entrée (bannière à l'ouverture d'une matière taggée · ligne discrète pour les actifs),
  pas un seul.
- **Q-4 — que devient `difficulty_adaptation` ? → LA LAISSER VIVRE, trancher après le lot 4.**
  _(sur la recommandation)_ **Conséquence** : aucun lot de cette étude ne la touche, ni en
  lecture ni en écriture. Son sort se décide sur un **fait** — « quelqu'un la lit-il encore ? » —
  une fois la décision par compétence livrée. Une suppression serait une migration destructive,
  en merge séparé, après le code (DoD §7).
  ✅ **RÉ-OUVERTE ET TRANCHÉE le 2026-08-30 par Mohamed, sur la recommandation : elle tombe.**
  Le fait attendu est tombé du bon côté — sur les **218 fonctions SQL vivantes**, **une seule**
  la touchait (`submit_exercise_attempt`, qui l'écrivait à chaque soumission depuis le sprint 2)
  et **aucune** ne la lisait ; zéro occurrence dans `src/` hors le fichier de types généré.
  é11 US-13, livrée entre-temps, ne l'a pas branchée non plus. Exécutée exactement comme la
  décision l'annonçait, en deux merges : arena#910 retire l'écrivain, arena#911 fait tomber la
  table. Détail et preuves au §8.
- **Q-5 — quelle matière après `math` 9ᵉ ? → NI `math-6eme`, NI `french-6eme` : FINIR `math` 9ᵉ.**
  ⚠️ **CONTRE la recommandation** (qui disait `math-6eme`, le moins cher). L'arbitrage retient
  l'option que l'étude avait elle-même signalée comme la plus honnête : le tagging couvre
  **521 / 818 questions (64 %)**, et **personne n'a lu** les 297 restantes pour savoir si elles
  sont légitimes (tout distracteur n'encode pas une erreur nommable — le champ est optionnel
  **par conception**) ou un reliquat de campagne. **Conséquence : un lot 0bis apparaît** (§4), et
  il précède tout élargissement. Le motif de l'arbitrage, qui vaut d'être écrit : _élargir sur
  une matière à 64 % revient à dupliquer une incomplétude qu'on n'a pas comprise._ Il rejoint
  KPI-1, qui n'est pas atteint.
- **Q-6 — quand rouvrir la porte IRT/Elo ? → DÈS QUE KPI-3 EST MAUVAIS, sans attendre 12 mois.**
  ⚠️ **CONTRE la recommandation** (qui exigeait ≥ 12 mois de télémétrie **et** un KPI-3 mauvais).
  La mesure décide seule. **Conséquence, et c'est la mitigation qui rend la règle opérable** : il
  faut alors définir **à partir de quand une bande de calibration a le droit d'être déclarée
  mauvaise**, sinon la règle se déclenche sur du bruit — avec 40 élèves actifs une bande contient
  une douzaine de réponses et rougit par hasard. Seuil retenu, et il n'est pas arbitraire :
  **n ≥ 100 observations dans la bande**. À n = 100 et p ≈ 0,75, l'erreur-type vaut ≈ 0,043, donc
  l'intervalle à 95 % est ≈ [0,665 ; 0,835] — il tient **juste** dans la tolérance [0,65 ; 0,85]
  de KPI-3. En dessous de 100, la bande est déclarée **« non concluante »**, jamais « mauvaise ».
  KPI-3 (§1.4) et RISK-2 (§6) sont amendés en ce sens, et la console du lot 8 doit afficher le
  **n** de chaque bande à côté de son taux — une courbe de calibration sans effectifs est un
  piège à décisions.
- **Q-7 — cette étude passe-t-elle avant l'acquisition ? → LES LOTS 1·2·3·4, puis réévaluer.**
  _(sur la recommandation)_ La charpente — croyance, inférence, carte à 4 états, décision —
  parce qu'elle rend la promesse **démontrable**, donc montrable à un enseignant ou à un parent :
  elle sert l'acquisition au lieu de lui faire concurrence. **Conséquence** : §4.1 est confirmé et
  précisé (le sous-ensemble est **0bis · 1 · 2 · 3 · 4**), et les lots **5 à 9 sont différés** —
  non gelés, différés : chacun reste autonome et reprenable, et la réévaluation se fait quand la
  charpente aura rencontré un public.

### 7bis. Ce qui reste ouvert après ces arbitrages

Aucune question ne bloque le lot 0bis ni le lot 1. Trois points attendent **une mesure**, pas une
décision — et c'est volontaire :

1. **KPI-3 doit exister avant de pouvoir trancher quoi que ce soit** (Q-2 et Q-6 en dépendent
   toutes les deux). Le script de calibration est livré au lot 1, la console au lot 8.
2. **`user_misconceptions` est encore vide** : l'étage é04 est armé depuis le 2026-08-23, pas
   prouvé. Il ne se remplira qu'avec des élèves.
3. ~~**Le sort de `difficulty_adaptation`** (Q-4)~~ — **CLOS le 2026-08-30** : rouverte après
   le lot 4 comme prévu, tranchée par Mohamed sur la recommandation, exécutée en deux merges
   (arena#910 puis #911). C'était le seul des trois points qui attendait une **décision** ; les
   deux autres attendent des **élèves**.
4. **La réévaluation des lots 5 à 9** (Q-7) reste déclenchée par la rencontre d'un public, pas
   par une date. Le mandat réitéré du 2026-08-25 ne la rouvre pas ; il verse deux pièces datées
   au dossier : la **voix existe** (é11 livrée) et attend la substance de l'échafaudage
   (lots 5·9), et le **démarrage à froid** du tuteur attend le bilan d'entrée (lot 7) — §3.13b.

---

## 8. Journal d'exécution

_(rempli au fil des lots par l'exécuteur : date, lot, PR, écarts acceptés, dettes notées)_

| date       | lot   | PR                                | écarts / dettes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ---------- | ----- | --------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2026-08-22 | —     | —                                 | Étude rédigée. **Trois mesures à reporter dans STATUS.md** : le registre de compétences `math` compte **62** entrées (STATUS annonce encore 59) ; le corpus porte **0** `misconceptionTag` (re-mesuré, inchangé depuis le 2026-07-31) ; le tagging de compétences couvre **`math` + `math-6eme`**, 234 fichiers.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| 2026-08-23 | **0** | privé #219 · dispatch 32629700267 | ⚠️ **La deuxième mesure ci-dessus était périmée trois heures après avoir été écrite, et c'est une bonne nouvelle : le lot 0 est LIVRÉ.** #219 a posé **1 049 tags** sur les **20 chapitres** de `math` 9ᵉ (l'étude en annonçait 13 — elle sous-estimait le périmètre), registre des misconceptions **56 → 154 entrées**, puis le corpus a été **appliqué en prod** (`apply-content.yml` ciblé `math`, `pg_dump` préalable, journalisé). Vérifié hors du workflow : 20 chapitres et **818 questions** `math` en base = le corpus. **Le sous-ensemble minimal du §4.1 démarre donc au lot 1.** — **Écart à connaître : KPI-1 n'est PAS atteint.** La couverture est de **521 / 818 questions, soit 64 %**, pas 100 %. Les 297 restantes sont soit légitimes (`misconceptionTag` est optionnel par conception — tout distracteur n'encode pas une erreur nommable), soit un reliquat ; **personne n'a tranché**, et le lot 4 en dépend. Concentration des non-tagués : `05-systemes` (33), `08-thales` (27), `15-numeration-et-calcul` (24). — **Et un fait qui renforce l'amendement D** : é11 lot 1 a été livré le 2026-08-22 (arena#816) et son `get_tutor_learner_context()` ne porte **aucune** ligne de maîtrise — ni compétences faibles, ni proxy. Le trou que comble le lot 3 est donc réel et mesuré, pas théorique. |
| 2026-08-23 | — | — | **Q-1…Q-7 arbitrées** (§7) : cinq sur les recommandations, **deux contre** — Q-5 (finir `math` 9ᵉ avant d élargir → **lot 0bis** créé) et Q-6 (porte IRT ouverte par KPI-3 seul, sans les 12 mois → **RISK-2bis** et le garde-fou `n ≥ 100` par bande). Statut **brouillon → validée** ; périmètre retenu **0bis · 1 · 2 · 3 · 4**, lots 5 à 9 **différés, pas gelés**. — ⚠️ **Deux faits mesurés le jour même changent le contexte de l étude** : **é04 est TERMINÉE** (arena#818 a livré A2.1 + A2.2 ; les quatre phases sont closes, privé #223) — é30 ne prolonge donc pas une étude en cours, elle reprend là où é04 s arrête ; et **une session exécute é11 lots 2 → 7**, ce qui fait de l amendement D un point de **collision** et non une note : le lot 3 n édite aucun fichier de é11 (§3.13). |
| 2026-08-25 | — | privé #239 | **Révision sur mandat de Mohamed** (« améliorer et optimiser é30, sachant é04 et é11 implémentées, cap sur ALEKS · Squirrel AI · CENTURY »). **Mesuré** sur `main` moteur (#852) et corpus (#237) : **é11 LIVRÉE 8/8** — lot 6 `20260824120000_tutor_digests`, lot 7 `20260824130000_tutor_energy_console`, branche `claude/etude-11-lots-6-7` (#844) · `get_tutor_learner_context` (version `20260823100000`) **sans aucune ligne de maîtrise** · le mini-check écrit `source='exercise'` + `session_id=` fil `tutor_threads`, questions du catalogue seules — l'hypothèse « source `'tutor'` » du §3.13b d'origine est **falsifiée** · **zéro artefact é30** dans le moteur (`p_known`/`belief_*`/`placement_sessions`/`scaffold_reveals` : 0 occurrence) · lot 0bis **non démarré** (couverture toujours 521/818) · registre : 62 entrées, 0 `scaffold`, 0 `pInit`/`pTransit` · **aucune clé IA jamais branchée** (pilote Q-9 pas commencé). **Ce qui change** : lot **3bis** (le pack apprend la maîtrise — l'amendement D a perdu son porteur à la clôture de é11, §3.13d) · poids `w = 0,5` du mini-check re-spécifié **par le fil** (§3.2) · sélecteur ZPD en nombres (§3.4, `ZPD_TARGET`) · §3.13 réécrit au présent mesuré · §1.2bis ajouté · 3 constantes de plus au registre §3.2 · 5 renvois d'une numérotation antérieure corrigés (lot 8→6, lot 5→4/7). **Ce qui ne change pas** : Q-1…Q-7 tenues, lots 5-9 différés, aucune décision d'architecture rouverte. **Trois dérives signalées, à corriger par leurs propriétaires** : l'ETUDE.md de é11 dit encore « 6 lots sur 8 » et son dossier n'est pas dans `EtudeRealisé/` ; le bloc ⭐ du §4 de STATUS.md dit « é11 à 6/8 » quand sa ligne §3 dit 8/8 ; la ligne « é11 lots 6-7 (en vol) » de la ROADMAP est périmée. |
| 2026-08-25 | — | (cette PR, 2ᵉ) | **Précision du mandat : « étude 29 aussi implémentée. »** Mesuré : é29 **livrée en 5 lots le 2026-08-22**, dossier **déjà** dans `EtudeRealisé/` (déplacé le 2026-08-24) — l'étude la citait au présent, aucune dérive côté é29 · la Forge vérifiée (`scope` `'competency'`, `competency_id TEXT` sans FK, `20260822200000`) · la chaîne P4 vérifiée (`get_targeted_exercises` + `tutor_practice_needs_generation`, porte Q-8 en SQL, `20260823150000`). **Ce qui change** : le branchement « cause racine » (P4), orphelin au même titre que l'amendement D depuis la clôture de é11 et é29, reçoit son porteur — le **lot 4** rebranche `get_targeted_exercises` dans la même PR que `get_remediation_path` (§3.13c, §4.2) ; pgTAP du lot 4 : ≥ 6 → ≥ 8. La révision de la veille est mergée : privé #239 (automerge, une minute après l'ouverture). |
| 2026-08-25 | **0bis** | (cette PR) | **Les 297 questions muettes sont tranchées — KPI-1 n'est plus une inconnue, il est une décision.** Les **297** questions et leurs **891** distracteurs ont été lus un à un (l'étude en annonçait « une vingtaine » — elle sous-estimait le périmètre d'un facteur 45, comme le lot 0 l'avait fait sur les chapitres). **Mesure avant/après**, sur les 20 chapitres de `math` 9ᵉ : questions taguées **521 → 662 / 818**, soit **64 % → 81 %** ; distracteurs taggés **1 049 → 1 244 / 2 454**, soit **43 % → 51 %**. **195** tags posés sur **141** questions, mobilisant **52** tags distincts. — **Le reste n'est pas un impayé : 156 questions restent muettes, et c'est la réponse.** La règle de décision, écrite pour les campagnes suivantes dans `.claude/skills/content-engine/references/content-schema.md` (§ `misconceptionTag`) et pointée depuis `METHODE-GENERATION-CONTENU.md` § B2 : un distracteur est taggé **si et seulement s'il est reconstructible** — R1 l'`explanation` nomme déjà l'erreur et l'option qu'elle produit · R2 tout le jeu de distracteurs est bâti sur une seule erreur · R3 une seule opération inversée ou omise, sans autre lecture. Muet sinon, dans trois cas nommés : **nombre de remplissage**, **ambiguïté** (deux erreurs mènent à la même option — un mauvais tag enseigne une fausse erreur, il coûte plus cher que pas de tag), **erreur réelle hors registre et vue < 3 fois**. ⚠️ **Conséquence à porter au lot 4 et à KPI-1 : 100 % n'est pas la cible.** La règle appliquée intégralement plafonne à 81 % ; au-delà, le chiffre mesurerait des tags posés au jugé, pas un corpus mieux tenu. KPI-1 doit être relu comme « 0 distracteur **non statué** », pas « 0 distracteur non taggé ». — **Registre : 154 → 160 entrées** (seuil d'extension respecté : ≥ 3 questions distinctes). La plus lourde est aussi la plus instructive : `math.alg.reponse-a-l-autre-inconnue` (« tu donnes une autre grandeur que celle demandée — l'autre inconnue, ou un résultat intermédiaire ») sert **54 fois à elle seule**, soit 28 % des tags de ce lot. C'est une erreur de **lecture d'énoncé**, pas de compétence : elle est déclarée **sans `competency`** — le champ est optionnel exactement pour ce cas (`schema.ts`, commentaire de `misconceptionEntrySchema`), et le bloc de correction é04 nommera l'erreur sans proposer d'exercice. Les cinq autres : `math.num.diviseurs-un-et-lui-meme-oublies` (5), `math.mes.rayon-non-eleve-au-carre` (4, πrh au lieu de πr²h), `math.alg.difference-carres-somme-au-lieu-de-difference` (4), `math.num.critere-somme-applique-au-chiffre` (3), `math.alg.difference-carres-second-terme-non-eleve-au-carre` (3). **Gates** : `content:check` (160 tags, 22 733 questions), `content:qa:strict` **0 erreur**, `content:audit:strict`, `programme:check` — tous verts. **Stop-points tenus** : aucune autre matière touchée, aucune entrée existante du registre réécrite. ⚠️ **Dette laissée, à connaître** : le corpus **n'est pas en prod** tant qu'`apply-content.yml` n'a pas été dispatché sur `math` (CLAUDE.md — merger ne publie pas) ; `content-drift` ouvrira l'écart s'il n'est pas comblé. |

| 2026-08-25 | **1** | arena#856 | **Le socle de croyance est livré et appliqué en prod.** Colonnes de croyance sur `user_competency_mastery`, `p_init`/`p_transit` au registre, `belief_guess`/`belief_slip`/`belief_update`/`belief_evidence_weight` (toutes hors de portée de tout rôle client), trigger `record_competency_belief`, `adaptive.ts`, et `scripts/adaptive/` (KPI-3 en lecture seule, par **rejeu déterministe** de l'historique — `question_attempts` n'enregistre pas la croyance qui avait cours, et rejouer n'est possible que parce que le modèle est déterministe). **27 assertions pgTAP** pour ≥ 14 exigées. — ⚠️ **ÉCART AVEC L'ANNEXE A, tranché en faveur du modèle, à corriger dans l'étude.** Huit des neuf lignes de A.1/A.2 se rejouent **exactement** avec les formules du §3.2. Une seule ne s'y rejoue pas : **A.1 n° 2** (`numeric` juste depuis 0,200) y est annoncée à **0,861** alors que les formules donnent **0,8482** — il faudrait `p(G) = 0,045` et non 0,05. Le §3.2 donne les formules ET les constantes ; la table en dérive. Là où elle contredit le modèle dont elle dérive, le modèle fait foi. Le désaccord est écrit dans les deux suites (SQL et JS) avec sa dérivation, plutôt que subi. Même remarque, hors périmètre : A.5 annonce 0,880 pour `short_answer` à p = 0,95, la formule donne 0,875. — ⚠️ **DÉCOUVERTE À PORTER AU §3.8c : `p_transit` écrit haut ÉTEINT la détection de lacune.** Le plancher de la croyance n'est pas 0,01 : p(T) impose un point fixe à ≈ 1,12 × p(T), parce que BKT suppose qu'on peut apprendre EN répondant. Au défaut de famille (0,15) il vaut ≈ **0,168**, sous le seuil de lacune de R-5 (0,25). Mais le CHECK du registre autorise `p_transit` jusqu'à **0,40** : au-delà de ≈ **0,22**, le plancher passe au-dessus du seuil et **une lacune devient indétectable**, quel que soit le nombre d'erreurs. §3.8c donne le CHECK, §3.2 le seuil, et rien ne dit qu'ils se contraignent l'un l'autre. Le CHECK est implémenté tel que spécifié ; l'interaction est épinglée par un test. — **Écart de périmètre assumé** : l'amendement B (`elapsed_ms`, source `placement`) n'est PAS livré. Ses deux lecteurs sont différés (lots 6 et 7), et un élargissement de CHECK sans consommateur n'a pas à voyager — il partira avec le lot qui le lit. |
| 2026-08-25 | **2** | arena#857 | **L'inférence dans le graphe**, avec le relevé de perf exigé. `propagate_competency_belief` + trigger à la **traversée de bande** ; garde de récursion **sémantique** (une ligne écrite par inférence ne propage pas) plutôt que `pg_trigger_depth()`, ce qui tient le stop-point « profondeur 2, pas 3 » **en disant pourquoi**. **20 assertions** pour ≥ 10, dont trois **attaques** contre D-4 (cent propagations d'affilée depuis 0,99 : ni preuve, ni forme, ni session, ni l'EWMA de é07 ne bougent). — **RELEVÉ DE PERF, sur les DEUX vraies RPC** (pas un `INSERT` nu), même base, mêmes fixtures, triggers basculés par `DISABLE`/`ENABLE`, deux passes reproductibles à ±0,4 ms — harnais versionné : `scripts/adaptive/bench-belief.sql`. Par soumission de 20 réponses : `submit_exercise_attempt` **4,5 → 11,1 → 14,4 ms**, `submit_dungeon_answer` ×20 **12,9 → 19,4 → 22,6 ms**. **+9,9 et +9,7 ms au total, soit ~0,5 ms par réponse — et SYMÉTRIQUE** : la dissymétrie que redoutait le §3.3 (« une réécriture a déjà guéri un appelant et empoisonné l'autre ») ne s'est pas produite. Une propagation touche **4 lignes en moyenne, 4 au pire**, conforme au « ≈ 3 en régime courant » annoncé. — ⚠️ **CE QUE LA MESURE A TROUVÉ ET QUE PERSONNE NE CHERCHAIT** : le coût dominant venait du **lot 1**, à +12,7 ms, parce que `belief_update` contenait une **CTE** — et une fonction SQL contenant une CTE **n'est pas inlinable**, donc appelée par le gestionnaire de fonctions une fois par ligne ET par compétence. Réécrite en une seule expression (identité `p⁺ + (1−p⁺)·T ≡ T + (1−T)·p⁺`) : **−6,7 ms** sur l'exercice, **−7,6 ms** sur le donjon, zéro changement de comportement (la table de vérité inchangée en est la preuve exécutable). C'est l'argument à ressortir la prochaine fois qu'un critère de perf paraîtra cérémoniel. — **Mesuré, non appliqué** : l'index d'incertitude `idx_ucm_user_uncertainty` (§3.8a) coûte **0,8 ms** par soumission et ne sert que le lot 7, différé. Conservé (il est spécifié ; le retirer serait re-décider à la place de l'étude), mais le chiffre est posé pour que le lot 7 hérite d'une décision documentée. — ⚠️ **Note de passage assumée** : une ligne créée par inférence garde `mastery = 50` (§3.8a piège 1), donc `get_my_competency_map` de é07 l'affiche en barre à 50 % jusqu'au lot 3. Fenêtre d'une PR. |
| 2026-08-25 | **3** | arena#858 | **Les lectures & la carte à 4 états.** `get_learning_state`, `get_learning_frontier` (tri par fan-out + sélecteur **ZPD**, §3.4), `competency_state` (les cinq conditions de R-4 **en un seul endroit** — c'est la règle la plus recopiable de l'étude), `belief_success_odds`, `dispute_inference`, la carte et la frontière trilingues. **21 assertions pgTAP** pour ≥ 8, + trois suites Vitest. `get_my_competency_map` **non touchée** (stop-point) : elle alimente le repli. — **D-1 est vérifié par le RÉSULTAT, pas par l'implémentation** : les tests des deux composants **balaient le DOM rendu** et échouent sur toute valeur ressemblant à une croyance (brute, décimale française, pourcentage), plus un `not.toMatch(/\d+\s*%/)` général — une régression future qui rebrancherait la valeur ferait rougir le test. Idem R-17 : `querySelectorAll("button:disabled")` doit être vide sur une compétence hors-portée. Idem le piège RTL : la phrase mixte texte/chiffres est asserted comme **un seul nœud de texte**. — ⚠️ **UNE COLONNE QUE LE §3.8 N'AVAIT PAS PRÉVUE, à ajouter à §3.8a : `p_known_before`.** R-10 dit que contester « ramène la croyance à **sa valeur d'avant inférence** » ; aucune des neuf colonnes ne gardait cet avant. Sans elle, la contestation ne peut que **deviner** — retomber sur `p_init`, exact pour une ligne *créée* par déduction, faux pour une ligne *relevée* au-dessus d'une croyance déjà gagnée. Huit octets rendent la phrase vraie plutôt qu'approximativement vraie. La propagation la renseigne avec un `COALESCE` : si la ligne est déjà déduite, son « avant » reste celui de la **première** déduction. — **Le budget de bundle a tranché une question de design** : trois `lazy()` et deux `useQuery` dans la route poussaient le chunk du tableau de bord à **32,13 kB** (budget 32,00). Plutôt que relever le budget pour 130 octets, les panneaux et leur repli sont regroupés dans un composant de la feature — où le choix de quelle carte montrer appartenait de toute façon. Chunk : **31,41 kB**. |
| 2026-08-25 | **3bis** | arena#859 | **Le pack du tuteur apprend la maîtrise** (amendement D). Bloc `mastery` : ≤ 3 maîtrisées les plus récentes · ≤ 3 de la frontière · ≤ 2 prérequis à reprendre — états et libellés, **jamais `p_known`**. **9 assertions** pour ≥ 6. **Budget mesuré : ~85 tokens** ajoutés au prompt à plafonds pleins, très en deçà des ~1 200 de é11, et la mesure est un **test**, pas une note de PR. L'état n'accompagne que les listes où il **varie** (`acquis` vaut toujours `maitrisee`). **Rien d'autre de é11 n'est touché** — le chat compose son propre bloc profil et reste inchangé ; les suites 70 · 71 · 73 · 74 passent sans retouche. — ⚠️ **CE QUE LE pgTAP A TROUVÉ, ET QUI NE VA PAS DE SOI : trois listes vides ne suffisaient PAS à obtenir l'absence.** La frontière d'un élève **neuf** n'est pas vide — toute compétence sans prérequis est « prête à apprendre » **par définition**, même jamais rencontrée. Le pack d'un élève qui n'a rien joué se serait rempli d'un inventaire de compétences `inconnue` : ni « exactement ce que le produit rend aujourd'hui », ni gratuit pour le budget. **La porte R-6 se pose donc sur la PREUVE (aucune ligne de croyance ⇒ aucun bloc), pas sur le résultat.** À reporter au §3.13d, qui écrit « matière non taggée ou aucune croyance » sans dire que la seconde condition doit être testée explicitement. — **Extraction précipitée par le plafond de lignes** de `tutor.server.ts` (750) : la validation du pack et le choix de langue partent dans `learner-context.ts`. C'était dû de toute façon — deux gestes **purs**, et les seuls de ce chemin qu'on peut tester sans monter un serveur. |
| 2026-08-25 | **4** | arena#860 | **La décision — le périmètre retenu est complet.** Amendement C (`remediate` rang 2, `strengthen` rang 4), `get_remediation_path` (cause racine = la plus **profonde** des non maîtrisées, profondeur ≤ 3) et le **rebranchement** de `get_targeted_exercises` (§3.13c) — un seul `CREATE OR REPLACE`, la porte Q-8 héritant en appelant sa voisine. **16 assertions pgTAP** pour ≥ 8. — **La non-régression est littérale ET par balayage** : les **32 combinaisons** d'entrées que les fixtures d'avant permettent, comparées à un **oracle qui réimplémente l'ordre d'origine dans le fichier de test** — le comparer au module aurait comparé le code à lui-même. Côté SQL, sélection identique **ligne à ligne** (`EXCEPT ALL` dans les deux sens) sur un résultat non vide. — ⚠️ **UN DÉFAUT DU LOT 3 TROUVÉ ET CORRIGÉ ICI : `get_learning_frontier` LEVAIT `Unauthorized` sans session** au lieu de rendre vide (elle appelle la porte d'accès, qui lève), contre l'invariant du §3.10 qui ne souffre pas d'exception. Portée réelle étroite — la server fn est derrière `requireSupabaseAuth` — mais c'est le genre de défaut qui **attend un nouvel appelant pour se voir**. Corrigé avec la garde **structurelle** de é11 lot 5 (`CROSS JOIN` sur une relation vide, jamais un prédicat que le planificateur peut évaluer trop tard), dans cette PR parce que le lot 4 introduisait le **jumeau** du bug. — ⚠️ **Et un piège de FIXTURE qui vaut pour toute la campagne** : taguer les cinq questions de la fixture rendait les assertions du rebranchement vertes **avant qu'il existe** — tout entrait par la voie TAG, celle que le lot ne touche pas. Une seule question taguée, et la voie compétence devient le seul chemin qui reste. Un test vert pour la mauvaise raison est pire qu'un test absent. — **Livré dormant, et dit comme tel** : les deux nouveaux rangs rendent `null` tant qu'aucun appelant ne leur fournit d'entrée — le §3.11 ne prévoit pour ce lot ni server fn ni composant, et où ces entrées seront produites est une question de **surface** non tranchée. Même posture que le `p_under_load` du lot 1, que l'étude assume : « une porte, pas une branche morte ». Le **rebranchement**, lui, est vivant dès le merge : c'est par lui que la cause racine atteint l'élève. — ⚠️ **Dette héritée du lot 0bis, à combler avant toute mesure de KPI-1** : le corpus `math` est **mergé mais pas publié** — `apply-content.yml` n'a pas été dispatché. KPI-1 se mesure sur le corpus **en prod**, pas sur `main`. |
| 2026-08-25 | **publication** | privé #243 · runs 32884292829 · 32888918603 | **Le corpus `math` est en prod, et KPI-1 est mesurable pour la première fois.** La dette laissée par le lot 0bis (« mergé mais pas publié ») est levée : `apply-content.yml` dispatché sur `math`, `pg_dump` préalable, application en une transaction, release journalisée. **Mesuré en base** : 20 chapitres, 139 exercices (dont 20 quiz), **818 questions**, dont **662 taguées — 81 %** et **818 rattachées à une compétence — 100 %** ; registre à **62 compétences / 80 arêtes**, exactement les chiffres du §3.3. ⚠️ **Note de lecture qui a failli coûter une fausse alerte** : la ligne de résumé de l'émetteur annonce `math: 20 chapters, 119 exercises, 715 questions` — elle ne compte QUE `exercices/`, pas les quiz. 818 = 715 + 103. Le SQL émis, lui, porte bien 818 insertions de questions et son prune conserve 139 ids. Vérifié en rejouant les fichiers sur une base vierge, pas déduit du log. — ⚠️ **ET LA PUBLICATION A TROUVÉ UN SECOND DÉFAUT, corrigé le jour même (privé #243).** `apply-content.yml` émettait et appliquait `_competences_registry.sql` mais **jamais** `_misconceptions_registry.sql`, et **aucune migration ne sème `misconceptions`** (la table est vide sur une base reconstruite à neuf) : son seul canal historique était une migration **générée**, sortie du dépôt public par l'étude 24 et interdite d'y revenir par le gate anti-fuite. Les **6 entrées** ajoutées par le lot 0bis (154 → 160) n'avaient donc **aucun chemin vers la prod** — alors qu'elles portaient **73 des 1 244 placements de tags** de `math`, dont **54** pour la seule `math.alg.reponse-a-l-autre-inconnue`. Les distracteurs étaient tagués, mais `get_attempt_review` ne trouvait aucune ligne pour **nommer** l'erreur : le bloc de correction s'affichait sans elle. **37 % du travail de lecture du lot 0bis n'atteignait pas l'élève.** C'est le **jumeau exact** du bug corrigé pour les compétences le 2026-07-31, et les deux ont duré pour la même raison : un registre manquant produit un run **VERT** — le SQL passe, le sujet se vérifie, seuls les libellés manquent. Le correctif ajoute l'étape d'émission, met les DEUX registres avant les sujets dans le plan, et — point qui n'est pas cosmétique — donne au nouveau registre **son propre critère de vérification** : sans lui il serait compté comme un SUJET (zéro chapitre, zéro question, « appliqué sans effet »), ce qui rejouerait le bug du 2026-08-01. Rejeu du plan corrigé sur base vierge : `misconceptions` 0 → **160**, placements orphelins **73 → 0**, idempotent au second passage. |
| 2026-08-30 | **Q-4** | arena#910 · arena#911 | **`difficulty_adaptation` est morte, et le fait a décidé — pas l'intention.** Q-4 laissait son sort ouvert « à trancher après le lot 4, sur un fait : quelqu'un la lit-il encore ? ». Mesuré sur `main` avant d'écrire une ligne : **218 fonctions SQL vivantes, UNE SEULE la touchait** — `submit_exercise_attempt`, qui l'écrivait à chaque soumission depuis le sprint 2 (`20260526220000`) — et **aucune ne la lisait** ; zéro occurrence dans `src/` hors le fichier de types généré ; 1 policy, 2 index, **0 FK entrante, 0 trigger, 0 vue dépendante**. Les deux branches de l'attente étaient retombées : é11 US-13 (« viser la ZPD ») a été **livrée sans la brancher**, et é30 lots 3/4 livrent ce qu'elle approximait — `P(réussite)` dans `ZPD_TARGET`, **par compétence** au lieu d'un palier 1-4 par matière entière. — **Deux merges, dans l'ordre qu'impose la DoD §7** : **arena#910** retire le bloc d'adaptation de la RPC (diff de **deux hunks** : le bloc et les quatre variables qui ne servaient qu'à lui ; scoring, clamp anti-triche, XP, SM-2, objectifs du jour et la télémétrie qui nourrit les triggers de croyance é30 **inchangés ligne pour ligne** — la soumission perd au passage un SELECT et un UPDATE) ; **arena#911** fait tomber la table, **sans CASCADE** délibérément (une dépendance apparue entre-temps doit faire échouer bruyamment, pas emporter un objet que personne n'a examiné), et **sans table de sauvegarde** — `db-migrate-prod.yml` prend un `pg_dump` avant d'appliquer, et la donnée est dérivée d'`attempts` qui est conservée ; un `_backup_difficulty_adaptation_*` aurait copié le motif de 2026-06-09, dont le résidu oblige encore chaque régénération de types à le recréer à la main. Suivent la table : sa ligne de la liste de reset E2E et sa mention à l'inventaire INPDP. — **Types RÉGÉNÉRÉS, jamais édités** (`postgres-meta` contre une base montée selon `docs/agents/pgtap-en-local.md`), avec le contrôle fait **dans l'autre sens d'abord** : régénérer AVANT le DROP donne **0 différence de contenu**, ce qui prouve la chaîne de génération ; le diff final est de **56 suppressions** (le bloc de la table) **+ 2 lignes de reflow**. — **Preuves** : chaîne complète rejouée sur base **VIERGE** aux deux temps (0 échec), suite pgTAP **84 fichiers / 1 187 assertions** vertes, `npm run verify` vert (3 539 tests). ⚠️ **Et un fait de méthode qui vaut d'être noté** : ce runbook local (`pgtap-en-local.md`, écrit par la session du lot 2) a permis de **prouver** les deux migrations en secondes — la chaîne de ~193 migrations rejouée trois fois — au lieu de trois dispatches CI de 5-8 min. C'est la deuxième fois qu'il paie. |
---

## Annexe A — Le modèle de croyance en nombres (la table de vérité du pgTAP)

> ⚠️ **Deux valeurs corrigées le 2026-08-30** (privé#247, item 1) : la ligne n° 2 de A.1
> annonçait 0,861 et la case `short_answer` à 0,95 de A.5 annonçait 0,880 — deux erreurs
> d'arithmétique de rédaction. Les formules et les constantes du §3.2 donnent **0,8482** et
> **0,875** ; toutes les autres lignes des deux tables se rejouent exactement. **Là où une table
> contredit le modèle dont elle dérive, le modèle fait foi** : le lot 1 avait déjà tranché ainsi
> et épinglé 0,8482 dans les deux suites (`supabase/tests/75_adaptive_belief.test.sql` et
> `scripts/adaptive/__tests__/belief-model.test.mjs`) — le corps de l'étude les rejoint.

Paramètres : `p(L₀) = 0,20`, `p(T) = 0,15` (défauts de famille, §3.8c) · `p(S) = 0,08`
(difficulté 2, hors charge) · `p(G)` selon le type (§3.2). Valeurs arrondies à 3 décimales ;
ce sont **exactement** les assertions attendues au lot 1.

**A.1 — La même bonne réponse ne vaut pas la même chose selon la forme de l'item**

| n°  | type d'item                | `p(G)` | croyance avant | après     | commentaire                                   |
| --- | -------------------------- | ------ | -------------- | --------- | --------------------------------------------- |
| 1   | `short_answer` / rappel    | 0,02   | 0,200          | **0,932** | une seule réponse juste, et on y est presque  |
| 2   | `numeric`                  | 0,05   | 0,200          | **0,8482** |                                              |
| 3   | `mcq` 4 options            | 0,25   | 0,200          | 0,557     |                                               |
| 4   | `mcq` 4 options (2ᵉ juste) | 0,25   | 0,557          | 0,849     |                                               |
| 5   | `mcq` 4 options (3ᵉ juste) | 0,25   | 0,849          | **0,961** | il en a fallu **trois** pour dépasser le n° 1 |
| 6   | `mcq` 4 options (4ᵉ juste) | 0,25   | 0,961          | 0,991     |                                               |

> **Et pourtant, au n° 6, la compétence n'est PAS déclarée maîtrisée.** `p_known = 0,991` passe le
> seuil, `evidence_count = 4` passe, mais `distinct_forms = 1` : quatre fois le même QCM.
> R-4 refuse. C'est le mandat — « validation répétée **et variée** » — rendu opposable par une
> condition, pas par une bonne intention.

**A.2 — L'erreur, et le pardon**

| n°  | situation                          | `p(S)` | avant | après     | lecture                                                                                                                                                     |
| --- | ---------------------------------- | ------ | ----- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 7   | débutant, `mcq` faux               | 0,08   | 0,200 | 0,172     | l'erreur d'un débutant n'apprend presque rien : on le savait déjà                                                                                           |
| 8   | **quasi-maître, `mcq` faux**       | 0,08   | 0,960 | **0,761** | une seule erreur fait sortir de la maîtrise — et c'est correct : la maîtrise se re-prouve                                                                   |
| 9   | **le même, sous signal de charge** | 0,20   | 0,960 | **0,885** | R-25 : le système **pardonne** parce qu'il a détecté la fatigue. L'écart entre 8 et 9 est toute la différence entre « tu ne sais pas » et « tu es fatigué » |

**A.3 — Le poids de la preuve après échafaudage** (R-21) — `p_final = p_avant + w·(p_après − p_avant)`

| aide reçue                       | `w`  | exemple : `mcq` juste depuis 0,200 | croyance finale |
| -------------------------------- | ---- | ---------------------------------- | --------------- |
| aucune                           | 1,00 | 0,200 → 0,557                      | **0,557**       |
| paliers 1–2 (orienter, la règle) | 0,50 |                                    | 0,379           |
| mini-check du tuteur (é11 US-4, détecté par le fil — §3.2) | 0,50 |                        | 0,379           |
| palier 3 (décomposer)            | 0,25 |                                    | 0,289           |

C'est Bruner rendu arithmétique : **l'aide se retire à mesure que l'autonomie se prouve**, et le
système sait toujours de quelle autonomie il parle.

**A.4 — L'inférence** (§3.3) — un élève établit `p_known = 0,88` sur `math.geo.thales-direct`

| compétence                            | profondeur | croyance avant | après inférence                                               | plafond |
| ------------------------------------- | ---------- | -------------- | ------------------------------------------------------------- | ------- |
| `math.prop.quatrieme-proportionnelle` | 1          | 0,300          | **0,616** (= 0,7 × 0,88)                                      | ≤ 0,90  |
| `math.num.operations-entiers`         | 2          | 0,500          | **0,500** (0,49 × 0,88 = 0,431 < 0,500 : on ne baisse jamais) | ≤ 0,90  |

Deux propriétés à retenir de ce tableau : l'inférence **prend le maximum**, donc elle ne peut
jamais dégrader une croyance existante (D-3) ; et elle ne touche ni `evidence_count` ni
`forms_seen`, donc aucune des deux lignes ne peut devenir `maitrisee` (D-4).

**A.5 — Ce que le système annonce avant de servir un item** (é11 US-13 devient calculable)

`P(réussite) = p·(1−S) + (1−p)·G`

| croyance | `mcq` 4 options | `short_answer` | zone                   |
| -------- | --------------- | -------------- | ---------------------- |
| 0,20     | 0,384           | 0,200          | trop dur — frustration |
| 0,50     | 0,585           | 0,470          | **ZPD**                |
| 0,70     | 0,719           | 0,650          | **ZPD**                |
| 0,95     | 0,886           | 0,875          | trop facile — ennui    |

La ZPD de Vygotsky n'est plus une métaphore : c'est l'intervalle `P(réussite) ∈ [0,55 ; 0,80]`,
et le sélecteur peut la viser. On y lit aussi, en creux, pourquoi un QCM ennuie plus tard qu'une
saisie libre : à croyance égale, il est toujours plus facile — de `p(G)` exactement.

---

## Annexe B — Les trois références, sourcées (recherche du 2026-08-22)

Convention de l'annexe B de é26, reprise ici : **⚠ signale un fait de source secondaire ou
promotionnelle**, à manier avec précaution ; les faits sans marque sont académiques ou recoupés.
Cette étude n'appuie **aucune décision** sur un fait marqué ⚠.

### B.1 ALEKS (McGraw Hill, États-Unis) — la théorie des espaces de connaissances

| Fait                                                                                                                                                                                              | Source                                                                                                                                                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ALEKS repose sur la **Knowledge Space Theory** : l'état de connaissance d'un élève est un **ensemble** dans une structure **partiellement ordonnée** — maîtriser un concept suppose ses prérequis | [aleks.com — Research behind ALEKS](https://www.aleks.com/about_aleks/knowledge_space_theory) (éditeur) ; [Matayoshi & al., _A practical perspective on knowledge space theory_, J. Math. Psych. 2021](https://jmatayoshi.github.io/publications/JMP2021_KST_ALEKS_preprint.pdf) (académique) |
| Le diagnostic d'entrée situe l'élève sur un domaine de **200 à 300 items** en **~25–30 questions**, chacune choisie d'après la précédente                                                         | mêmes sources, recoupées                                                                                                                                                                                                                                                                      |
| Le placement lui-même a fait l'objet d'une évaluation publiée à EDM                                                                                                                               | [EDM 2024, industry track](https://educationaldatamining.org/edm2024/proceedings/2024.EDM-industry.61/)                                                                                                                                                                                       |
| La **frange extérieure** de l'état de connaissance nomme ce que l'élève est « prêt à apprendre »                                                                                                  | littérature KST                                                                                                                                                                                                                                                                               |

**Ce qu'on en prend** : l'inférence dans l'ordre partiel (§3.3) et la frontière (§3.4) — les deux
organes qui font l'économie du diagnostic. **Ce qu'on n'en prend pas** : la combinatoire complète
des espaces de connaissances, hors de proportion pour 62 compétences ; et le ton du produit, dont
le caractère décourageant est le reproche le plus constant qui lui soit fait (RISK-3).

### B.2 Squirrel AI (Yixue, Chine) — le nano-découpage

| Fait                                                                                                                                                                                                                                                | Source                                                                                                                                                                                                                                                                                                                                                                     |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Découpage **nano** : les maths collège découpées en **plus de 10 000 points de connaissance**, contre 2 000–3 000 dans un manuel ⚠                                                                                                                  | communications de l'entreprise ([PR Newswire](https://www.prnewswire.com/news-releases/squirrel-ai-learning-by-yixue-group-attends-the-hottest-technology-event-of-north-america-collision-tech-conference-300884608.html), [Forbes 02/2025](https://www.forbes.com/sites/forbeschina/2025/02/18/derek-li-and-squirrel-ai-aim-to-lead-the-future-of-ai-driven-education/)) |
| Moteur à **trois étages** : carte de l'apprenant + carte des contenus · gestion d'objectifs, état de l'utilisateur, moteur de recommandation · stratégies différenciées ⚠                                                                           | mêmes communications                                                                                                                                                                                                                                                                                                                                                       |
| Système **MCM** (_thinking, capacity, method_) : à performance d'examen égale, distinguer capacités et rythmes ⚠                                                                                                                                    | mêmes communications                                                                                                                                                                                                                                                                                                                                                       |
| **Essai randomisé** : des élèves chinois de 8ᵉ année, deux provinces, tirés au sort vers Squirrel AI, progressent davantage en mathématiques que ceux affectés à un cours en classe entière ou en petit groupe **mené par des enseignants experts** | Cui, Tong, Yarnall, Shear, Feng — _Interactive Learning Environments_ 31(2), 793-803, en ligne le 31/08/2020 ([éditeur](https://www.tandfonline.com/doi/abs/10.1080/10494820.2020.1808794)) ⚠ **co-signé par l'entreprise**, mais avec des chercheurs de SRI International — indépendance partielle                                                                        |

**Ce qu'on en prend** : la démonstration qu'un moteur adaptatif discipliné peut battre
l'enseignement collectif — et la **structure** à trois étages, qu'on retrouve trait pour trait
dans le §3.1. **Ce qu'on n'en prend pas** : le nano (Q-2). Il déplace tout le coût sur le
tagging, et rien dans les sources disponibles ne permet d'attribuer le résultat de l'essai à la
granularité plutôt qu'à la boucle.

### B.3 CENTURY Tech (Royaume-Uni) — la charge cognitive comme contrainte de design

| Fait                                                                                                                         | Source                                                                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Plateforme combinant IA, **neurosciences cognitives** et données massives pour un parcours personnalisé ⚠                    | [BESA](https://www.besa.org.uk/news/artificially-intelligent-platform-learns-every-brain-learn/), [HundrED](https://hundred.org/en/innovations/century-tech) — profils éditeur/écosystème |
| **Micro-apprentissage** explicitement destiné à limiter la surcharge cognitive : modules courts, construction incrémentale ⚠ | revues et pages produit secondaires                                                                                                                                                       |
| Techniques revendiquées : **entrelacement**, récupération fréquente, retour adaptatif, **répétition espacée** ⚠              | mêmes sources                                                                                                                                                                             |

⚠⚠ **C'est la référence la plus faiblement sourcée des trois** : aucune évaluation indépendante
n'a été trouvée dans cette passe. Elle est retenue pour ce qu'elle **nomme** — la charge cognitive
comme contrainte de conception, et non comme une intention — pas pour ce qu'elle prouve. Le lot 6
s'appuie sur Sweller et sur la littérature du piétinement (B.4), pas sur CENTURY.

### B.4 Le socle académique du modèle (ce sur quoi les décisions s'appuient réellement)

| Fait                                                                                                                                                                                                            | Source                                                                                                                                          |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| **BKT** (Corbett & Anderson, 1994) : quatre paramètres — `p(L₀)`, `p(T)`, `p(G)`, `p(S)` — estiment la probabilité de maîtrise d'une compétence latente ; seuil canonique de maîtrise **0,95**                  | littérature ITS ; [synthèse](https://www.emergentmind.com/topics/bayesian-knowledge-tracing-bkt)                                                |
| **Bornes anti-dégénérescence** : la littérature propose `p(G) + p(S) ≤ 1`, `p(G)` et `p(S) ≤ 0,50`, ou encore `p(S) = 0,10` / `p(G) = 0,30`                                                                     | [Baker, Corbett & Aleven — _Contextual estimation of slip and guess_, ITS 2008](https://link.springer.com/chapter/10.1007/978-3-540-69132-7_44) |
| **Problème d'identifiabilité** (Beck) : les mêmes données s'ajustent également bien avec des paramètres différents ; les correctifs par a priori de Dirichlet exposent à la **dégénérescence**                  | [Baker & al., _Degree of error in BKT estimates_](https://learninganalytics.upenn.edu/ryanbaker/behaviormetrika_vfinal.pdf)                     |
| **Piétinement** (_wheel-spinning_, Beck & Gong) : élève qui pratique une même compétence **plus de 10 fois** sans parvenir à **trois réponses justes consécutives** ; détectable dès les premières opportunités | [Beck & Gong, AIED 2013](https://link.springer.com/chapter/10.1007/978-3-642-39112-5_44)                                                        |
| Le **retour élaboré** (qui explique) écrase le simple juste/faux — `d ≈ 0,99` sur 435 études                                                                                                                    | Wisniewski, Zierer & Hattie 2020 — **déjà retenu par é26 annexe B.2**, non re-sourcé ici                                                        |
| Le déterministe décide, le LLM parle : les modèles classiques de _knowledge tracing_ battent les LLM en prédiction de maîtrise, pour un coût par décision sans commune mesure                                   | é26 annexe B.2 (EDM 2024) — **c'est P-5a**, et c'est pourquoi cette étude n'a pas de LLM                                                        |

**Ce que B.4 change pour D-2** : le reproche récurrent fait à BKT porte sur **l'estimation** des
paramètres, jamais sur la mise à jour bayésienne elle-même. En dérivant `p(G)` de la géométrie de
l'item et `p(S)` du palier de difficulté, et en **écrivant** `p(L₀)`/`p(T)` dans un registre
versionné, cette étude ne fait aucune estimation — et le problème ne se pose pas. Ce n'est pas
une version affaiblie de BKT : c'est BKT **privé de sa seule partie contestée**.

---

## Annexe C — Le mandat, ligne à ligne : ce qui existe déjà, ce que ce document ajoute

Lecture directe du cahier des charges du §1.1. **« Déjà »** signifie : vérifié dans `main` le
2026-08-22 ; la ligne « adapter le ton » a été re-vérifiée le 2026-08-25 (é11 livrée).

| #        | Ce que demande le mandat                                | Déjà en place                                                                                            | Ce que cette étude ajoute                                                               | Lot     |
| -------- | ------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------- |
| **1**    | micro-compétences atomiques                             | ✅ `competencies` — **62**, 11 domaines (é07 lot 1)                                                      | rien : la maille est bonne (Q-2)                                                        | —       |
| **1**    | dépendances strictes                                    | ✅ `competency_prereqs` — 80 arêtes, profondeur 6, acyclicité vérifiée au pipeline                       | rien                                                                                    | —       |
| **1**    | niveaux d'objectifs (comprendre / appliquer / analyser) | 🟠 approximé par la difficulté d1–d4 et les 6 modes d'exercice                                           | rien en v1 — la difficulté joue déjà ce rôle et un troisième axe alourdirait le tagging | —       |
| **1**    | batterie d'activités graduées                           | ✅ 6 modes (pratique, boss, révision, défi, entraînement, défi-concours) + 6 types natifs + rappel actif | rien                                                                                    | —       |
| **2**    | ne pas faire passer tout le programme                   | ❌                                                                                                       | **bilan adaptatif ≤ 20 items**, arrêt anticipé sur incertitude résiduelle               | 7       |
| **2**    | déduire les prérequis d'une réussite complexe           | ❌                                                                                                       | **inférence montante** dans le DAG, γ = 0,7, profondeur 2, plafond 0,90                 | 2       |
| **2**    | isoler la lacune d'un échec de base                     | 🟠 `get_competency_blockers` sait remonter, mais **rien ne l'appelle**                                   | **`get_remediation_path`** + la priorité `remediate` en tête de la décision             | 2 · 4   |
| **3**    | recalculer après chaque réponse                         | ✅ EWMA au trigger (é07 lot 2)                                                                           | la **croyance** BKT, entretenue par le même événement                                   | 1       |
| **3**    | **probabilité d'inattention**                           | ❌                                                                                                       | `p(S)` par difficulté, plafonnée 0,10 — **relevée à 0,20 sous charge**                  | 1 · 6   |
| **3**    | **probabilité de hasard**                               | ❌                                                                                                       | `p(G)` **par géométrie de l'item** : 0,25 pour un QCM à 4 options, 0,02 en saisie libre | 1       |
| **3**    | maîtrise « répétée et variée »                          | ❌ (l'EWMA est une moyenne mobile : rien n'y est « déclaré »)                                            | **R-4** : 5 conditions conjointes, dont `distinct_forms ≥ 2` et `distinct_sessions ≥ 2` | 1 · 3   |
| **4**    | réussite facile → monter                                | 🟠 `difficulty_adaptation` calcule, **personne ne lit**                                                  | la **frontière** triée par fan-out, et `P(réussite)` pour viser la ZPD                  | 3 · 4   |
| **4**    | difficulté légère → même notion, autre format           | ❌                                                                                                       | priorité **`strengthen`** : même compétence, **type d'item différent**                  | 4       |
| **4**    | échec répété → remonter la chaîne des prérequis         | ❌                                                                                                       | priorité **`remediate`**, cause racine, profondeur ≤ 3, une remontée par session        | 4       |
| **5**    | jamais la solution brute                                | ✅ la clé ne quitte jamais le serveur                                                                    | le gate **anti-solution** sur les paliers                                               | 5       |
| **5**    | palier 1 — question réflexive                           | ❌ (seul `consume_hint` existe : tout ou rien, et payant)                                                | `scaffold.orient`, **au niveau de la compétence**                                       | 5 · 9   |
| **5**    | palier 2 — règle ou analogie                            | ❌                                                                                                       | `scaffold.rule`, au niveau de la compétence                                             | 5 · 9   |
| **5**    | palier 3 — décomposition                                | ❌                                                                                                       | `scaffoldDecompose`, au niveau de la question, serveur seul                             | 5 · 9   |
| **5**    | adapter le ton et le vocabulaire                        | ✅ **é11 livrée** (2026-08-24) — la voix existe, **éteinte sans clé** (é29 R-1)                          | la substance que cette voix reformulera : lots 5·9 (différés)                           | é11     |
| **6**    | détecter la latence anormale                            | ❌ **la donnée n'existe pas**                                                                            | `question_attempts.elapsed_ms`, comparé à la **médiane personnelle**                    | 6       |
| **6**    | détecter l'enchaînement d'erreurs                       | ❌                                                                                                       | série de 3 dans la session                                                              | 6       |
| **6**    | détecter le blocage durable                             | ❌                                                                                                       | **piétinement** : ≥ 10 tentatives sans 3 réussites consécutives (KPI-4)                 | 6       |
| **6**    | baisser la difficulté, varier, proposer une pause       | ❌                                                                                                       | réaction graduée, **jamais bloquante, une fois par session**                            | 6       |
| **P2·1** | Bloom — ne pas progresser avant 80–90 %                 | 🟠 le seuil existe (0,95), **le verrou n'existe pas et é22 l'a retiré**                                  | avertissement motivé + remédiation ; **Q-1** porte l'arbitrage                          | 4 · Q-1 |
| **P2·2** | Vygotsky — la ZPD                                       | ❌                                                                                                       | `P(réussite) ∈ [0,55 ; 0,80]`, calculée (annexe A.5)                                    | 3 · 4   |
| **P2·3** | Bruner — l'échafaudage se retire                        | ❌                                                                                                       | le **poids de la preuve** décroît avec l'aide reçue (`w` = 1 / 0,5 / 0,25)              | 5       |
| **P2·4** | Sweller — la charge cognitive                           | 🟠 le découpage en missions courtes y concourt déjà                                                      | les 3 signaux + `p(S)` indulgente sous charge                                           | 6       |

**Le tableau se lit dans les deux sens.** Sur 27 lignes, **9 sont déjà tenues** et 4 le sont à
moitié : le mandat n'est pas un chantier à ouvrir, c'est un chantier **aux deux tiers construit
dont personne n'a posé la charpente**. Les organes ❶ croyance, ❷ inférence et ❹ frontière sont
cette charpente ; l'arbitrage Q-7 les retient, avec la preuve qui les alimente, en cinq lots :
**0bis · 1 · 2 · 3 · 4** — auxquels la révision du 2026-08-25 ajoute le **3bis**, le branchement
du tuteur livré. Le ❸ bilan d'entrée, le ❺ échafaudage et la ❻ gestion de charge sont
**différés** — chacun autonome, chacun reprenable, aucun gelé.
