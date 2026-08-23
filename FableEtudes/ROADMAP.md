# ROADMAP — ordre d'exécution du reste-à-faire (études, lots, contenu)

<!-- roadmap-sync: since-pr=818 -->

> **Instantané du 2026-08-22** (créé le 2026-07-20, resynchronisé contre `main` les 2026-07-25,
> 2026-07-27, 2026-07-29, 2026-08-01, 2026-08-03, 2026-08-10, 2026-08-16/17 puis le
> **2026-08-22**) — déclinaison opérationnelle de l'**étude 26 (doctrine verticale : profondeur
> avant largeur)**. Les Q-1…Q-5 de l'étude 26 ayant été **arbitrées le 2026-07-20**, cet ordre
> n'est plus une recommandation d'architecte : il est **officiel**. Les arbitrages **A1→A8**
> (2026-07-20) puis **A9→A14** (2026-08-02) sont rendus : cette seconde session a vidé les
> questions internes des études 04 et 09, et tranché le périmètre du tagging, le lien
> misconception → compétence et le statut du check pgTAP. L'état de référence reste
> [STATUS.md](../STATUS.md) + l'[index des études](./README.md).
> **Jalon produit : rentrée scolaire, 1ᵉʳ septembre 2026** (§7) — **J-10**.
>
> ⚠️⚠️⚠️ **CE QUE LA PASSE DU 2026-08-22 A TROUVÉ — et les deux premières lignes de la roadmap
> sont tombées sans qu'aucune session ne les prenne.** La citation de é29 au §0bis a déplacé la
> base de **#746 à #807** : elle a donc déclaré « connues » les **60 PR moteur livrées entre les
> deux** (#747 → #810) sans en citer une seule, et le gate est resté vert — aucune ne porte la
> forme « étude/lot » qu'il sait lire. C'est le **même angle mort** que le 2026-08-10, dans
> l'autre sens : là c'était le privé qu'il ne regarde pas, ici c'est le pointeur qui a sauté.
>
> **Trois lignes décrivaient un état factuellement faux — corrigées ici.** **C11**, désignée
> « PREMIÈRE LIGNE DE TOUTE LA ROADMAP », est **faite** : son issue #124 est close depuis le
> **2026-08-10 à 17 h 46**, c'est-à-dire *le jour même où la ligne a été écrite* et **six jours
> avant qu'elle n'atteigne `main`** (#152/#184, mergées le 2026-08-16). **F10**, deuxième
> priorité, est **faite** aussi : #81 close le 2026-08-14, `content-audit.yml` vert depuis.
> **F5** enfin : la suppression de compte **existe** (arena#791) — la moitié « code » de GAP-024
> que cette roadmap donnait pour inexistante. Vérifié le 2026-08-22, pas déduit.
>
> **Et quatre chantiers entiers n'avaient aucune ligne** : le **suivi parental quotidien**
> (15 PR — **F11**), le **programme officiel devenu structure du produit** (**F12**), les
> **manuels officiels déclarés et liés** (**F13**), et la campagne **فقه** côté corpus
> (37 chapitres, rubrique ouverte aux élèves — **C12**).
>
> ✅ **Le point dur de ce paragraphe est TOMBÉ le 2026-08-23 — 24 h après avoir été écrit.**
> Il disait : « c'est C4bis, et il commande désormais aussi l'IA · le corpus ne porte toujours
> **aucun** tag de misconception (0 occurrence, re-mesuré le 2026-08-22 sur 719 chapitres) ».
> C4bis a été livré le soir même (#219, **1 049 tags**) puis **appliqué en prod** le lendemain
> (`apply-content.yml`, run 32629700267). Les quatre lots é04/é07 et l'ancrage du tuteur
> (arena#816) sont donc alimentés. **Ce qui reste du point dur** : le tagging couvre **64 %**
> des questions de `math` 9ᵉ et **s'arrête à cette matière** ; et `user_misconceptions` est
> encore vide — elle ne se remplira qu'avec des élèves. **Armé n'est pas prouvé.**
>
> ⚠️ **La leçon de méthode, et elle est nouvelle.** Le 2026-08-10 disait « un gate vert ne veut
> pas dire à jour ». Le 2026-08-22 ajoute : **une priorité écrite le jour J et mergée à J+6 n'est
> pas une priorité, c'est un instantané périmé.** Les deux premières lignes de cette roadmap ont
> été refermées par d'autres pendant que le fichier les proclamait urgentes. **Relire l'issue
> avant de prendre la ligne** — c'est trente secondes, et ça vient d'en coûter deux.
>
> ⚠️ **[HISTORIQUE — passe du 2026-08-10] Ce qu'elle avait corrigé, et ce qu'elle croyait
> commander.** **37 PR livrées n'étaient citées nulle part** : 30 ici (#117 → #148) et 7 au
> moteur (arena#710 → #716). Le gate `roadmap-sync` était **vert** pendant tout ce temps, et il
> avait raison de l'être : il ne lit que les sujets de commit du **moteur** en forme
> « étude/lot » — or ces sept jours se sont joués **au privé**, où il ne regarde pas. Un gate vert
> n'a jamais voulu dire « la roadmap est à jour » ; il veut dire « rien de ce que je sais lire ne
> manque ».
>
> **[Verdict du 2026-08-10, PÉRIMÉ le 2026-08-22 — les deux lignes qu'il a créées sont faites.]**
> **Le point dur a changé de nature.** Ce n'est plus C4bis : c'est que **du contenu mergé,
> audité et validé n'atteint aucun élève**. La garde `content-drift` tient l'issue **#124**
> ouverte depuis le 2026-08-04 sur **18 sujets** — dont la campagne lycée anglais/français
> **en entier**, jamais publiée. Et elle a été écrite pendant que le **garde pédagogique était en
> panne** (#81, quatre runs échoués : 07-29, 08-01, 08-05, 08-08). Les deux nouvelles lignes sont
> **C11** (§5) et **F10** (§4) — aucun des deux chantiers n'avait de ligne, alors que les deux
> issues étaient ouvertes et visibles.
>
> ⚠️ Quatre lignes décrivaient un état **factuellement faux** — corrigées ici : **C4bis** (son
> étape 0 est faite, #118), **C3** (4 matières sur 5 en prod), **C9** (une campagne lycée entière
> livrée), **F5** (son reliquat n'est pas que humain : il est **du code**).
>
> ⚠️⚠️ **Et une cinquième était fausse dans la correction elle-même.** La PR #150 attribuait la
> panne `npm ci` à l'écart de Node entre les deux dépôts et présentait son alignement comme le
> correctif. La cause était un **lockfile défectueux** (arena#716 : une majeure + une alpha
> entrées sous un titre de « bump indirect »), le correctif est le **revert** arena#718, et
> l'écart de Node expliquait **l'inverse d'une cause** — npm 10 refusait ce lockfile là où
> npm 11 l'acceptait, ce qui faisait de la Content CI d'ici le **seul détecteur** du système.
> Détail en **C11**, arbitrage ouvert en **A17**. Une roadmap qui corrige les autres se corrige
> aussi.

## 0bis. Livré au moteur depuis le #716 (citation exigée par `check-roadmap-sync`)

Le gate a un avis sur la **connaissance**, jamais sur le statut : citer suffit, coché, reporté ou
sans objet. Ces trois-là ne créent aucune ligne de roadmap — ils sont **hors file**, ce qui est
précisément pourquoi ils n'y figuraient pas.

- **arena#718** — revert du bump « undici » qui embarquait `miniflare 5-alpha` et deux majeures :
  `npm ci` était cassé sur npm 10 depuis le 2026-08-09, donc **la Content CI d'ici est restée
  rouge 33 h**, `main` comprise. Hors file (incident de dépendance).
- **arena#720** — « corriger chaque question à l'instant où elle est validée ». Hors file au sens
  strict : la file PRODUIT V1 ne portait pas cette ligne.
- **arena#722** — la **garde anti-verbatim** entre dans `content:qa` (**étude 27 lot 2**). Elle
  appartient à la file de l'étude 27, pas à celle-ci : citée ici au titre de la connaissance,
  **sans objet** pour les trois files de cette roadmap.
- **arena#723 · arena#724** — deux lots UI (silhouettes de chargement, surfaces du lecteur de
  quête). Hors file également : la file PRODUIT V1 ne les portait pas.
- **arena#721** — trois faits canoniques re-mesurés : registre des misconceptions à **56 entrées
  toutes pourvues de leur `competency`** (l'étape 0 de C4bis est donc **faite**), corpus à
  659 chapitres / 22 146 questions, et « Node 22 » corrigé en 24 dans AGENTS.md. Hors file
  (resynchronisation documentaire) — mais **C4bis §5 en dépend** : ce qui reste est le seul
  tagging des distracteurs.

**Ajout du 2026-08-16** — trois lots de plus, que le gate réclamait depuis trois nuits (il
échouait sur `main` les 08-14, 08-15 et 08-16 ; personne ne lit un cron rouge) :

- **arena#726** — étude 28 lot 3 : la position et sa scorecard. Hors file (documentaire).
- **arena#743 · arena#746** — ⚠️ **l'étude 02 est LIVRÉE** : le schéma et le
  moteur SQL de l'examen blanc (lots 1-2), puis l'écran passer / rendre / se corriger
  (lots 3-4), livrés tous les deux le **2026-08-16**. **Ce n'est pas hors file** : le §6 disait
  encore « **é02 se re-scope maintenant** » (sortie du différé le 2026-08-13, é28 Q-4) —
  quatre lots plus tard, cette phrase décrivait un état révolu ; **corrigé le 2026-08-17**, en
  même temps que la clôture de l'étude, qui passe dans `EtudeRealisé/`. Ce qui restait à écrire
  — **où s'arrête son v1** — l'est désormais dans son §8 : trois écarts assumés (R-7 rescopé pour
  la phase gratuite, lot 5 remplacé par un seed **par requête**, US-3 partielle) et cinq questions
  dont **Q-2, la cadence éditoriale, qui est la mitigation de RISK-1**, et **Q-5, à vérifier en
  base avant tout le reste : la session 1 est-elle réellement `published` ?**

**Ajout du 2026-08-22** — une PR, cinq lots, et une ligne de file qui change de propriétaire :

- **arena#807** — ⚠️ **l'étude 29 est LIVRÉE** (mode IA « à la clé de la famille », 5 lots).
  **Ce n'est pas hors file** : elle **remplace la ligne 17** (é11 lot 0), que Q-1 a rayée au
  profit d'un socle unique. §3 étape E réécrite en conséquence, et la ligne 18 (é11 lot 1)
  devient prenable — c'est le KPI que é29 se donne à elle-même. Reste entier : le **pilote de
  mesure de deux semaines**, et le fait qu'**aucune clé réelle n'a encore été branchée**.

**Ajout du 2026-08-22, seconde passe — 60 PR moteur d'un coup, et quatre chantiers sans ligne.**
La citation de é29 ci-dessus a porté la base de **#746 à #807**, déclarant « connues » les 60 PR
livrées entre les deux sans en citer une. Les voici, groupées. La plupart sont **hors file** ;
quatre groupes ne le sont pas.

- ⚠️ **Suivi parental quotidien — un axe produit entier, aucune ligne** : arena#744 · #748 ·
  #750 → #754 · #759 · #762 → #764 · #769 · #777 · #779 · #782. Nouvelle ligne **F11** (§4).
- ⚠️ **Le programme officiel devient une structure du produit** : arena#749 · #766 · #767 ·
  #770 (et au corpus #197 → #202). Nouvelle ligne **F12** (§4).
- ⚠️ **Manuels officiels déclarés et liés, plus hébergés** : arena#778 · #785 · #808 · #810
  (et au corpus #205 → #212). Nouvelle ligne **F13** (§4) — elle **ne clôt pas C8**.
- ⚠️ **arena#791 — la suppression de compte est livrée.** Elle ferme la moitié « code » de
  **GAP-024** que **F5** donnait pour inexistante. L'export/portabilité, lui, reste à **zéro
  occurrence** dans `src/` (re-vérifié le 2026-08-22). **F5 corrigée.**
- **arena#760** — les **4 sections bac** dont le contenu était prêt sont **ouvertes aux élèves**
  (R-8) ; avec **arena#741** (rubrique « Éducation islamique », migrations `20260814120000` /
  `20260815120000`), c'est le geste « ouvrir » que **C10** distingue de « générer ». Cités en
  **C11** et **C12**.
- **Hors file** — auth et robustesse (#747, #772, #773, #775, #776) · e2e (#755, #796, #797,
  #801, #802) · perf et mesure (#780) · domaine et CSP (#783, #784 — l'issue **arena#804**,
  ouverte le 2026-08-22, reste sans ligne et n'en demande pas) · a11y et bidi (#765, #786) ·
  navigation et réglages (#787, #790, #798) · CI (#792) · doc d'agents et de passation (#756,
  #757, #758, #761, #768, #774, #781, #794, #806).

⚠️ **Une précision qui vaut pour é29** : `/parametrage` est créée par **arena#787** ;
**arena#798** ne fait qu'y déplacer le Code Alliance. Le §8 de l'étude 29 attribue la page à
#798 — sans conséquence sur sa décision (D-16 est bien caduque sur son constat), mais à ne pas
recopier.

**Ajout du 2026-08-22, troisième passe — les deux premières lignes de l'ordre sont livrées.**

- **arena#816 — é11 LOT 1 EST LIVRÉ** : « Demander au Prof », la première brique
  PÉDAGOGIQUE de l'étage IA. **Ce n'est pas hors file** : c'est la **ligne 18**,
  et elle se coche. Le lot ne recrée aucun objet de é29 (Q-1, socle unique) et
  livre la pièce que é29 lot 5 lui avait laissée en toutes lettres — le **cache
  mutualisé d'explications** (R-15.2), dont `AI_CURATED_MODELS` était la
  condition d'entrée et n'était jusque-là référencé nulle part.
- **arena#799 · arena#812 · arena#815** — e2e, correctif de console IA, doc
  d'agents. Hors file.
- **arena#811 · arena#813** — ⚠️ **manquaient à cette liste**, et #811 n'est pas
  un correctif d'écran : elle porte une **décision produit**. Les plafonds de
  consommation de é29 (argent **et** énergie) **ne coupent plus par défaut** ;
  ils mesurent et alertent, et le porteur les réarme d'un interrupteur
  (`limits_enforced`). RISK-2 n'est donc plus arrêté par la machine — seule
  l'alerte d'anomalie à 3× la médiane subsiste comme signal automatique. Le
  reste des deux PR est de la même classe : l'écran n'annonçait que deux
  fournisseurs quand le moteur en accepte n'importe lequel (DeepSeek, Kimi, GLM
  nommés ; grille de prix élargie, sans quoi une famille DeepSeek était coupée à
  ~4 % de sa dépense), et le panneau d'activation proposait huit surfaces pour
  un seul écran livré. Détail au §8 de l'étude 29. **Sans objet pour les trois
  files**, mais à connaître avant toute reprise de l'étage IA.
- Côté corpus : **#219 — C4bis ÉTAPE 1 EST LIVRÉE** (1 049 distracteurs tagués,
  registre 56 → 154). Elle se coche au §5.

⚠️ **Et le fait qui relie les deux, à ne pas perdre** : le tagging est **mergé**
mais **pas appliqué en production**. Tant qu'`apply-content.yml` n'a pas tourné,
`get_tutor_question_context` rend `misconception = NULL` et l'explication du
tuteur se tait sur l'erreur nommée. Les deux lots sont bons ; c'est le geste
d'application qui les relie, et il tient en un dispatch (voir **C11**).

## 0. Mode d'emploi (comment exécuter cette roadmap)

1. **Une ligne = une session = un lot = une PR** (règles FableEtudes inchangées : cadre fermé,
   DoD intégral, la session suit sa PR jusqu'au merge).
2. **Trois files parallèles** : PRODUIT (§3), FONDATIONS (§4), CONTENU (§5). Elles ne se
   bloquent pas entre elles — une session prend **la première ligne non cochée de sa file**
   dont les dépendances sont satisfaites.
3. **Les arbitrages A1→A14 sont rendus** (§2). ⚠️ Mais « arbitrage rendu » ≠ « ligne
   exécutable » : vérifier aussi le **statut de l'étude** (`brouillon` / `validée` / `en
   exécution`) et ses questions internes. C'est le piège dans lequel ce fichier est tombé
   jusqu'au 2026-08-01 — voir l'encart du §2.
4. Priorité inter-files en cas de choix : finir l'en-vol (§1) > PRODUIT > FONDATIONS >
   CONTENU nouveau (les corrections qualité contenu passent, elles, avant tout — P-4).
   ⚠️ **Exception ré-arbitrée le 2026-08-22 — elle prime sur cet ordre.** L'ordre du
   2026-08-10 était **C11 → F10 → C4bis** ; **C11 et F10 sont faites** (vérifiées, §5 et §4), et
   C4bis n'a pas bougé. L'ordre à prendre est donc :

   ~~1. **C4bis étape 1**~~ · ~~2. **Ligne 18**~~ — **LES DEUX SONT LIVRÉES le 2026-08-22**
   (#219 et arena#816). L'ordre à prendre devient :

   ~~1. **APPLIQUER LE CORPUS EN PRODUCTION**~~ — **FAIT le 2026-08-23**, et c'est la ligne la
   plus vite refermée de cette roadmap : `apply-content.yml` dispatché sur `math`
   (run 32629700267, `pg_dump` préalable, journalisé dans `content_releases`). Vérifié **hors
   du workflow**, en anon : 20 chapitres et **818 questions** `math` en base, à l'identique du
   corpus. Les 1 049 tags sont donc atteignables par un élève, et s'allument d'un coup les
   quatre lots é04/é07 restés inertes depuis l'origine **plus** l'ancrage de l'explication du
   tuteur (arena#816, livrée la veille sans avoir jamais eu un tag à citer).
   ⚠️ **La leçon vaut d'être notée, parce qu'elle ne s'attrapait pas au vert** : l'étape de
   contrôle du workflow compte les **chapitres et les questions**, jamais les colonnes
   **serveur-seul** — `distractor_tags` en fait partie. Un run vert n'aurait donc pas prouvé
   que les tags étaient arrivés ; c'est le décompte externe qui le prouve. Écrit dans le
   moteur : `docs/agents/campagnes-contenu.md`.

   L'ordre à prendre devient :

   1. **C4ter** (§5) — `french-6eme`, la complétude de la classe de concours (é28 D-4).
   2. ~~**Ligne 15** (§3) — é04 A2.1 « Points faibles »~~ — **LIVRÉE le 2026-08-23**
      (arena#818), avec la **16** : l'étude 04 est finie. Prise le lendemain de l'application,
      exactement comme cette ligne l'annonçait.
   3. **Trancher les 36 % non tagués** — le tagging couvre **521 des 818 questions** de `math`
      9ᵉ. Les 297 restantes sont soit légitimes (tout distracteur n'encode pas une erreur
      nommable — le champ est optionnel par conception), soit un reliquat de C4bis. Personne
      n'a regardé. Une vingtaine de distracteurs suffisent à trancher, et le KPI-1 de é30 en
      dépend.

   La règle « PRODUIT d'abord » suppose que la file PRODUIT a une ligne prenable : depuis
   l'application, **la 15 en est une** — elle ne livrerait plus un écran vide. L'ordre sert la
   valeur livrée ; il ne la remplace pas.

   ⚠️ **Ordre du 2026-08-23, en fin de journée — le rang 2 ci-dessus est tombé le jour même.**
   La ligne 15 est livrée (arena#818), et la **16** avec elle. Il reste donc **C4ter** et
   **les 36 % non tagués**, auxquels s'ajoute la seule ligne PRODUIT encore ouverte :

   1. **C4ter** (§5) — `french-6eme`, la complétude de la classe de concours (é28 D-4).
   2. **Trancher les 36 % non tagués** (rang 3 ci-dessus, inchangé) — et il vient de gagner un
      second commanditaire : ce n'est plus seulement le KPI-1 de é30, c'est **ce que l'élève
      voit**. Les surfaces de A2 n'affichent que des erreurs **nommées** ; chaque distracteur
      laissé sans tag est un échec qui ne remontera jamais dans « Tes points faibles ». Une
      vingtaine de distracteurs suffisent toujours à trancher.
   3. **Ligne 19** (§3) — é11 lots 2 → 7, **la dernière ligne non cochée de toute la file
      PRODUIT**. Elle n'a plus aucune dépendance : le socle é29 est en prod, le lot 1 aussi, et
      `math` 9ᵉ est tagué **et appliqué**. Sa cadence se règle sur les coûts observés — c'est
      un choix de rythme, plus un blocage.

   Au-delà, **C4bis étape 2** (étendre le tagging aux autres matières) : `math` 9ᵉ démontre
   maintenant la chaîne complète, du distracteur tagué jusqu'à l'écran de l'élève ; les autres
   matières n'en ont encore rien.

### Comment cet ordre reste vrai (règle amendée le 2026-07-25)

La règle d'origine — « cocher la case dans la même PR que le lot » — est **inapplicable depuis
la scission de l'étude 24** : cette roadmap vit dans le dépôt privé, la quasi-totalité des lots
se livre dans le dépôt public, et aucune PR ne touche les deux. Elle a dérivé exactement comme
on pouvait le prévoir : **24 lots livrés entre le 2026-07-20 et le 2026-07-25 n'y figuraient
nulle part**, dont toute la fin de l'étude 22, é04-A1.1, é20 lot 1, é07 lots 2/4/5 et une étude
harness entière. Une session prenant « la première ligne non cochée » aurait refait du travail
déjà sur `main`.

La règle est donc remplacée par un **invariant vérifié** :

- chaque ligne cochée **cite la ou les PR** qui l'ont livrée — le fichier porte sa propre preuve ;
- le gate [`check-roadmap-sync.mjs`](https://github.com/MBeji/yahia-quest-arena/blob/main/scripts/ci/check-roadmap-sync.mjs)
  (dans le moteur public, appelé par la Content CI d'ici) **échoue** si un lot livré sur `main`
  après la PR de référence déclarée en tête de ce fichier n'y est cité nulle part. Citer suffit :
  coché, reporté ou sans objet — le gate a un avis sur la **connaissance**, jamais sur le statut.
- une session qui livre un lot au public **ouvre une PR d'une ligne ici** pour cocher. C'est le
  seul geste cross-repo, et le gate le rend non-oubliable au lieu de compter sur la discipline.

## 1. En vol aujourd'hui (à finir avant d'ouvrir autre chose)

- [x] **Étude 25 lot 2** (gate `harness:check` + rôles de modèles) : **mergé le 2026-07-20**
      (#530, porté par sa session d'origine ; les doublons de sauvetage #523/#529/#534 sont
      fermés).
- [x] **Session « resynchroniser l'index »** : é15/é17 passées `livrée` le 2026-07-20 (#536) ;
      l'**étude 23** — en-tête « brouillon » alors que ses lots 1-4 étaient mergés — est
      resynchronisée par la session d'arbitrages du 2026-07-20 (`en exécution`, lots 1-4 cochés,
      PRs #524/#527 inscrites au journal).
- [x] **Reverdir `main`** — **fait, vérifié le 2026-07-25**. Les deux volets rouges sont clos : - **Nightly (#250)** : réparé par #570 (quatre causes indépendantes accumulées), les suites
      pgTAP orphelines séparées du corpus (#574/#575) et les collisions de préfixe nées des
      merges parallèles renumérotées (#584/#587/#599 → rangs 35-39). **Vert 5 nuits d'affilée**
      (du 2026-07-21 au 2026-07-25). Issue close. - **E2E authentifié (#363)** : les 12 échecs préexistants traités par vagues (#576/#577,
      #580, #586/#589) puis **un run entièrement vert sur `main`** le 2026-07-21 — le premier
      depuis l'ouverture de l'issue. Close. - Le diagnostic « 7 tests d'entitlements premium devenus faux par le pivot gratuit » a bien
      été traité par re-scoping des fixtures, pas par une correction de code. - ⚠️ **La mise en garde « `db-tests.yml` ne tourne pas sur les PR » est PÉRIMÉE** : depuis
      #563 (2026-07-21), la suite pgTAP tourne sur **toute PR** touchant
      `supabase/migrations/**` ou `supabase/tests/**`. Elle reste hors des checks _requis_ :
      un rouge n'empêche pas l'auto-merge, il faut le lire.
- [x] ~~**Trancher les PRs legacy**~~ — **sans objet** : vérifié le 2026-07-20, #374 (français
      3ᵉ), #376 (transcription 2ᵉ sec) et #348 (transcriptions ScribeKit) sont **toutes les
      trois mergées** les 12-13/07. Le contenu « coffre-fort » qu'elles ont sauvé est sur `main` ;
      son exploitation relève du fil contenu (§5), pas d'un arbitrage.

## 2. Arbitrages — A1→A8 le 2026-07-20, A9→A14 le 2026-08-02

> Deux sessions de décision : **A1→A8** le 2026-07-20 (consignée par #537), puis **A9→A14** le
> 2026-08-02 — celle-ci vide les questions internes des études 04 et 09 et tranche le périmètre
> du tagging, le lien misconception → compétence et le statut du check pgTAP.
> ⚠️ **Ne pas lire « aucun arbitrage en attente » comme « toute ligne est exécutable ».** C'est
> l'erreur qu'a faite ce fichier jusqu'au 2026-08-01 : les arbitrages A* étaient rendus, mais les
> **questions internes des études restées en `brouillon`** ne l'étaient pas — é09 en portait trois,
> dont une bloquait un lot entier. Avant de prendre une ligne, **lire le statut de son étude**. Le détail de chaque
> décision, avec sa conséquence sur les lots, vit dans le §7 (ou §8) de l'étude concernée —
> ce tableau n'en est que le sommaire.

| #   | Arbitrage                                                                                                                                | Décision rendue                                                                                                                                                                                                                                                                        |
| --- | ---------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| A1  | **é26 Q-1…Q-5** (verticales & pipeline V1 · cible catalogue rentrée · gels 06/10/12 · propriétaire « correction riche » · signatures M4) | ✅ Pipeline V1 adopté **tel quel** · cible rentrée = **statu quo consolidé à la barre é18** (aucune classe vitrine), V1 prioritaire et contenu en parallèle · **gel des trois** (é06/é10/é12) · correction riche → **é04 phase A1.2** · M4 fermé à 3 capacités. é26 → `validée`        |
| A2  | **é24 — les 4 écarts du lot 3b** (volumétrie, critère d'inventaire, garde orpheline, ordre repair-revert)                                | ✅ Critère de **provenance** ratifié · les **17 migrations manuelles restent au public** (KPI + gate anti-fuite amendés pour les exclure nommément) · contrainte **reposée en migration de schéma publique** · **ordre inversé** + dégraissage remonté dans le lot 3b. **3b débloqué** |
| A3  | **é19 Q-1…Q-4**                                                                                                                          | ✅ SVG inline seul + une PR par lot · concours → matières spatiales → **STOP** sur le non spatial · **vérification intégrale**, un lot > ~40 figures est scindé, jamais échantillonné. é19 → `validée`, lot 1 exécutable                                                               |
| A4  | **é21 Q-1…Q-4** (verbatim/droits des manuels)                                                                                            | ✅ Verbatim toléré pour les **énoncés techniques courts non créatifs**, adaptation ailleurs (posture de risque, **pas un avis juridique**) · **provenance NON affichée à l'élève → lot 3 abandonné** · pilote `math-1ere-sec` · manipulations hors périmètre v1. é21 → `validée`       |
| A5  | **é11 Q-1…Q-9** (tuteur IA)                                                                                                              | ✅ Exécution **dégelée pour les lots 0-2**, pilote **math 9ᵉ** · énergie 10/j (plafond dur 30) · budget **5 $/j** (≤ 150 $/mois) · **le tuteur s'appelle « El Ostedh » (الأستاذ)**, sans mascotte · pas de verbatim parent · champ libre dès le collège · GO coordonné avec é04-A1.1   |
| A6  | ~~PRs legacy #374 / #376 / #348~~                                                                                                        | **Sans objet** — les trois sont mergées depuis les 12-13/07 (voir §1)                                                                                                                                                                                                                  |
| A7  | _(rendus antérieurement, pour mémoire)_ é23 Q-1/Q-2/Q-5 le 2026-07-19 (#531) ; é22 Q-1…Q-5 le 2026-07-18 ; é20 Q-1…Q-5 le 2026-07-16     | é23 lot 5, é22 lots 1-6, é20 lots 1-8 : **exécutables**                                                                                                                                                                                                                                |
| A8  | **Renovate ou script maison** pour le lot patch/minor (rendu le 2026-07-25)                                                              | ✅ **Script maison** — pas de tiers dans la chaîne, même régime que les autres gardes du harness. Appliqué par le lot L4 de l'étude « IA vs déterministe » (#613)                                                                                                                      |
| A9  | **é09 Q-1…Q-3** (garde-fous chiffrés · cadence de revue · déclencheur du lot 3) — rendu le 2026-08-02                                    | ✅ **G-1…G-4 ratifiés tels quels**, comme **hypothèses de départ** à corriger après la première lecture de la page Économie · revue **mensuelle** (hebdo inviterait au réglage réactif, RISK-2) · lot 3 déclenché par la **latence** (> 2 s, déjà journalisée), pas par la volumétrie. **é09 lot 2 débloqué** — ⚠️ **et son premier run en dément deux** (arena#708) : niveau 5 au jour 6 pour l'assidu et au jour 31 pour le moyen contre une fenêtre 7-14 j (G-1), shields à ~38 % contre 20 % (G-4). L'hypothèse a joué son rôle exactement comme prévu ; les seuils sont **à re-trancher — voir A15/A16** ci-dessous. Lire cette ligne sans son démenti, c'est lire une décision périmée |
| A10 | **é04 Q-4 / Q-5** (feedback par question · ancres de cours) — rendu le 2026-08-02                                                        | ✅ Feedback question-par-question : **non pour la rentrée** (rouvrirait la soumission atomique), à reconsidérer après mesure du clic A1.2b · `courseAnchor` : **v1 sans ancres**, on ancrera sur les tags que la télémétrie montrera fréquents                                          |
| A11 | **Tagging des misconceptions — périmètre** (rendu le 2026-08-02)                                                                        | ✅ **Pilote sur `math` 9ᵉ** (557 questions), pas la vague large : il donne un coût réel par question avant d'engager `math-6eme`, et allume l'écran sur la matière de concours. C'est le déblocage de TOUT l'axe adaptatif                                                              |
| A12 | **Lien misconception → compétence** (rendu le 2026-08-02)                                                                               | ✅ **Un champ `competency` dans le registre des misconceptions** — chaque erreur déclare la compétence qu'elle met en défaut. Réutilise le chemin d'é07 lot 4 sans en créer un second (R-A1.2-6). **Débloque « m'entraîner », donc la ligne 9**                                        |
| A13 | **`pgTAP suite` requis sur les PR de migration** (rendu le 2026-08-02)                                                                   | ✅ **Requis.** #689 a mergé ROUGE trois minutes après son ouverture : le check tournait, il était rouge, la fenêtre de lecture était plus courte que le temps de lire. ~2 min par PR de schéma contre une classe entière de pannes de base                                              |
| A14 | **Garde-fou de volumétrie des registres** (rendu le 2026-08-02)                                                                          | ✅ **Non** — la purge est déjà gardée là où le dégât se produit (arena#702, fail-closed à l'application). Un seuil « ne pas descendre sous N » serait un doublon plus faible, et en pgTAP donc après coup                                                                              |

**Ce qui reste à la main de Mohamed** (hors lots, sans blocage de file) : é23 Q-3 (self-désigner
l'app child-directed auprès de Google — le paragraphe « vidéos YouTube » a désormais une page où
vivre, arena#701) · é24 Q-4 (démarche OTDAV/INNORPI) · F5 (légal avant rentrée) ·
**le signalement `d12f0f96` à passer `dismissed`** dans `/admin/content-reports`
(artefact e2e, cause corrigée par #618 — état **non vérifiable depuis ce dépôt**) ·
le **test à blanc de `rollback-prod.yml`** (`freeze-only` puis `unfreeze`) et les **gabarits
d'e-mail FR** à coller dans Supabase (STATUS §2 du 2026-07-27).
**Ajouté le 2026-08-10** : le **renouvellement du secret `CLAUDE_CODE_OAUTH_TOKEN`** de ce dépôt
(`claude setup-token`) — c'est le geste humain que F10 attend, et le seul qui remette le garde
pédagogique en marche. ⚠️ Celui-ci n'est **pas** « sans blocage de file » : il conditionne la
qualité de tout ce qui s'écrira ensuite.

**A15/A16 — deux arbitrages NEUFS, produits par l'exécution du 2026-08-03** (arena#708, é09
lot 2). Ils ne sont pas des questions d'étude restées ouvertes : le simulateur les a **fabriqués
en tournant**, ce qui est exactement son métier. Les deux portent sur des garde-fous que A9 avait
ratifiés **comme hypothèses de départ** — les corriger maintenant est le protocole prévu, pas un
revirement.

| #   | Constat mesuré                                                                                                                                                                                        | Ce qui est à trancher                                                                                                                                                        |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| A15 | **G-1 (niveau 5 en 7-14 j) échoue des DEUX côtés** : l'assidu l'atteint au jour 6, le moyen au jour 31. À 3 j/semaine × 2 exercices, 800 XP demandent ~5 semaines — le seuil est arithmétiquement hors d'atteinte | **Recaler G-1** (une fenêtre par persona, ou une cible qui décrive le moyen). ⚠️ Ne PAS retoucher `gamification.ts` pour faire passer le test : ce serait régler l'outil        |
| A16 | **G-4 (shields ≤ 20 % des jours manqués) échoue à 38 %** — celui-là est un **signal d'économie**, pas un seuil trop serré : à 15 coins, le rachat de série est bon marché face au revenu                 | Desserrer le seuil **ou** renchérir le shield. C'est le premier réglage d'équilibrage que la mesure rend possible — la revue est **mensuelle** (A9), rien n'oblige à trancher ce jour |

**A17 — un arbitrage NEUF, produit par une erreur de session** (2026-08-10). En réparant la
Content CI, la PR #150 a aligné les six workflows d'ici sur **Node 24** (celui du moteur) en
présentant l'écart de Node comme la **cause** de la panne. C'était faux : la cause était un
lockfile défectueux (arena#716), réparé par un **revert** (arena#718). Et l'écart de Node
expliquait l'inverse d'une cause — npm 10 (Node 22) **refusait** ce lockfile là où npm 11
l'acceptait, ce qui faisait de la Content CI d'ici **le seul détecteur du système**.

| #   | Constat                                                                                                                                                                                                                                                                          | Ce qui est à trancher                                                                                                                                                                                                                                                                                                                                                       |
| --- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| A17 | **L'alignement sur Node 24 a supprimé le seul détecteur** qui ait attrapé une majeure + une alpha entrées sous un titre de « bump indirect ». La propriété perdue était **accidentelle** (la sévérité de npm 10), donc fragile — mais elle a fonctionné là où tout le reste était vert | **Revenir à Node 22** (garder le canari, au prix de faire tourner les scripts du moteur sur un Node qu'il n'utilise pas) **ou tenir Node 24** et poser la vraie garde : refuser une PR de dépendance dont le **diff dépasse ce que son titre annonce**. ⚠️ Ne pas trancher par confort : le statu quo (24) est l'option qui a déjà coûté quelque chose |

⏳ **Toujours en attente au 2026-08-10** — une semaine après leur production. Rien ne les
relance et rien ne les bloque : la revue d'économie est **mensuelle** (A9), donc A16 peut
légitimement attendre. **A15 est différent** : tant que G-1 reste au tableau, `economy:check`
échoue **par construction**, et un garde-fou qui échoue toujours cesse d'être lu — c'est le
mécanisme exact par lequel le garde pédagogique (#81) est resté en panne douze jours.

Écart d'énoncé relevé au passage, sans arbitrage : l'étude é09 écrit « niveau 5 (1 000 XP) » ;
avec `XP_PER_LEVEL = 200` le niveau 5 est à **800 XP** — le simulateur suit le niveau.
**~~F4~~ en sort** : domaine, monitoring, analytics et sitemap sont **faits, constatés le
2026-07-27** — voir F4 au §4.

## 3. FILE PRODUIT — la verticale V1 « apprendre & maîtriser » (ordre strict)

> Objectif : refermer les trois boucles mortes (SM-2, misconceptions, adaptativité) et porter
> la boucle d'apprentissage à M3 avant la rentrée.
> **État au 2026-08-23 : 19 des 20 lignes livrées.** La ligne 9 est CLOSE (arena#689, #691,
> #695, **#707**). La **17 est close par substitution** — é29 lot 1 remplace é11 lot 0 — la
> **19bis** est livrée, la **18** l'est depuis le 2026-08-22 (arena#816) et les **15 et 16**
> depuis le 2026-08-23 (arena#818). **Il ne reste que la 19** — é11 lots 2 → 7.
> ⭐ **Et avec les 15 et 16, l'ÉTUDE 04 EST FINIE** : les quatre phases sont closes (A0, A1.1,
> A1.2, A2), l'étude est passée en `EtudeRealisé/`. La verticale « apprendre & maîtriser » n'a
> donc plus de dette adaptative — ce qui reste dans cette file est **entièrement** de l'IA.
> ⚠️ **Ce que les douze jours du 2026-08-03 au 2026-08-21 ont produit hors de cette file** : é02
> close (arena#743, #746), tout le **suivi parental quotidien** (**F11**), le **programme
> officiel** comme structure (**F12**), les **manuels** (**F13**) et é29 (19bis). Ce n'était pas
> une dérive : aucune ligne d'ici ne pouvait bouger tant que le corpus n'était pas tagué.
> ✅ **Le gel a cessé le 2026-08-22** — trois lignes (18, 15, 16) en deux jours, dès que C4bis
> étape 1 a levé le blocage. **Dix-huit jours d'immobilité de la file PRODUIT tenaient à un
> travail de CONTENU**, et c'est la leçon à ne pas perdre au moment de trancher une priorité.
> ✅ **LEVÉ le 2026-08-22 — le paragraphe qui suit est conservé pour son histoire, pas pour son
> verdict.** `math` 9ᵉ porte **1 049 tags** (#219), appliqués en prod le 2026-08-23, et la 15 a
> été prise le lendemain. La leçon reste : ce blocage a tenu **dix-huit jours** une ligne PRODUIT
> que rien n'empêchait techniquement d'écrire, et il n'était levable que par du **contenu**.
> ⚠️ ~~**La 15 n'est PAS prenable telle quelle**~~ : **le corpus ne porte toujours aucun tag de
> misconception** — 0 occurrence sur ~18 700 questions, re-mesuré **inchangé le 2026-08-10**.
> Tout l'étage « erreur nommée / points faibles » est alimenté par du vide, y compris le geste
> que #707 a livré. Le déblocage est **C4bis** (§5), un travail de contenu, pas de code.
> ✅ **Mais son étape 0 est faite** (#118, 2026-08-04) : le registre
> `content/misconceptions.json` est passé de **5 à 56 entrées**, et **les 56 déclarent leur
> `competency`** — les 51 neuves couvrent les 13 chapitres de `math` 9ᵉ, les 5 anciennes ont
> gagné le champ qui leur manquait. Ce n'est **pas** un détail de comptage : la moitié du travail
> que la ligne 15 attend existe désormais, et une session qui lit « 5 entrées, aucun
> `competency` » la referait.

**Étape A — réparer le parcours (étude 22, validée — 6 lots) — ✅ ÉTUDE CLOSE le 2026-07-21**

- [x] 1. **é22 lot 1 — la carte honnête** (`/parcours` : plus de faux verrou séquentiel, états `next`/`done`) — #538
- [x] 2. **é22 lot 2 — la boucle SM-2 refermée** (`submit_exercise_attempt` passe les révisions à `completed`) — #540
- [x] 3. **é22 lot 5 — le donjon scopé** au parcours (fallback cycle → catalogue, `pool_scope`) — #547
- [x] 4. **é22 lot 4 — cohorte « Ma classe »** (`get_grade_leaderboard` + onglet par défaut dès ≥ 10 classés) — #565
- [x] 5. **é22 lot 6 — « prochaine action » unifiée** (`resolveNextAction`) + purge des objectifs fantômes — #567
- [x] 6. **é22 lot 3 — la rentrée** (bannière 1ᵉʳ sept → 31 oct, `current_parcours_set_at`, bloc « Réviser ») — #573, livré **en avance** (échéance mi-août)

**Étape B — la révision devient un produit (étude 04)**

- [x] 7. **é04 lot A1.1 — « Révision du jour »** (RPC `get_daily_plan` + panneau dashboard, consomme SM-2 refermée en 2) — #581 (pgTAP renuméroté #584)
- [x] 8. **amendement é04-A1.2 « correction riche à l'échec »** _(A1 rendu : rattachée à l'étude 04)_ — **rédigé le 2026-07-25**, contrat fermé en `04-moteur-adaptatif/ETUDE.md` §9. Il **corrige deux suppositions du mandat** : l'explication post-erreur n'a jamais été monnayée (c'est l'indice _avant_ réponse qui l'est), et un feedback question-par-question rouvrirait la couture de soumission atomique — sorti du périmètre, posé en Q-4. Reste donc à livrer : l'erreur nommée + le lien « revoir le cours »
- [x] 9. **é04 lot A1.2 — correction riche — LIGNE CLOSE le 2026-08-03** (arena#689, #691, #695, **#707**).
      **A1.2a (serveur)** — arena#689, correctif de test arena#691. `get_attempt_review` rend
      `misconception_tag` (le tag de l'option **choisie**, et seulement sur une réponse fausse) +
      `chapter_id`, sans qu'une porte bouge. L'appariement réutilise `resolve_misconception_tag`
      (é20 lot 7) au lieu d'être réécrit. Stop-point **D-A1.2-2 tenu** : la map `distractor_tags`
      n'est jamais rendue — l'option correcte étant la seule sans tag, elle désignerait la bonne
      réponse par élimination. Trois assertions pgTAP jouent cette attaque, pas le cas nominal.
      **A1.2b (client)** — arena#695. Le bloc riche sur une question ratée : erreur nommée, lien
      « revoir le cours », i18n FR/EN/AR + RTL, dégradation totale et silencieuse (R-A1.2-3).
      Il a fallu **corriger D-A1.2-3** : elle fondait les libellés sur un registre « déjà compilé
      côté client pour d'autres surfaces » — cette surface n'existe pas, et depuis la scission
      `content/` n'est pas dans le dépôt public au build. Les libellés passent donc par la base,
      **par le canal des compétences** (é07), qui répondait déjà au même besoin. L'intention est
      préservée : la fonction SQL rend un ID, le registre reste source unique, une reformulation
      reste une correction de registre sans migration.
      **Reliquat — LIVRÉ le 2026-08-03** (arena#707), sur l'arbitrage A12 : le geste
      **« m'entraîner »**. R-A1.2-6 imposait de réutiliser celui d'é07 lot 4, qui résout une
      COMPÉTENCE en exercices — or une misconception n'en est pas une. A12 a posé la traduction
      **dans le registre**, déclarée par l'auteur qui écrit l'erreur, plutôt que devinée par du
      code à partir des compétences de la question. Livré : champ **optionnel** `competency` au
      schéma (`misconception_competency`, migration `20260802120000`), résolution via l'unique
      `get_exercises_for_competency`, bouton sur le bloc de correction.
      **Trois partis pris à connaître avant d'y toucher** : le champ est optionnel **par
      conception** — une confusion de vocabulaire n'a pas de compétence propre, et proposer un
      exercice au hasard serait pire que ne rien proposer ; **pas de FK** vers `competencies`,
      les deux registres passant par le même canal dans un ordre que rien ne garantit (l'intégrité
      est vérifiée à la source par `content:qa`, sur les deux à la fois) ; la server fn vit dans
      `quest.training.ts` et non `quest.server`, sinon l'écran tirait tout le serveur dans le
      chunk client.
      ⚠️ **Livré ne veut pas dire allumé** — et la raison a changé le 2026-08-04. Le registre
      déclare désormais **56 `competency` sur 56 entrées** (#118), donc ce n'est plus lui qui
      manque : le bouton ne s'affiche chez aucun élève parce qu'**aucune question ne pointe vers
      une de ces 56 entrées**. C'est l'étape 1 de **C4bis**.
      ⚠️⚠️ **LE FAIT QUI COMMANDE TOUT L'AXE, mesuré le 2026-07-31 et RE-MESURÉ INCHANGÉ les
      2026-08-03 et 2026-08-10 : le corpus ne contient AUCUN
      tag de misconception.** Zéro occurrence de `misconceptionTag` sur 566 chapitres et
      ~18 700 questions ; zéro `distractor_tags` non vide dans les 17 migrations manuelles ; les
      56 entrées du registre ne sont référencées nulle part. La chaîne est mécanique : pas de tag authoré
      → `distractor_tags` vide → `resolve_misconception_tag` rend NULL → le trigger
      `trg_question_attempts_misconception` (qui ne se déclenche que sur un tag non nul) ne s'est
      **jamais** déclenché → **`user_misconceptions` est vide en prod**. Le récit de l'étude 26
      (« signal collecté depuis le 2026-07-06, jamais surfacé ») est donc faux dans sa prémisse :
      la boucle n'était pas *collectée-jamais-surfacée*, elle n'était **jamais alimentée**.
      Conséquences à ne pas redécouvrir : A1.2 ne nommera **aucune** erreur tant que rien n'est
      tagué (le lien « revoir le cours », lui, fonctionne) · le terme « misconceptions » de
      `get_daily_plan` (A1.1, #581, D-3) vaut zéro depuis le premier jour · **la ligne 15 (A2.1
      « Points faibles ») livrerait un écran vide** — à lire avant de la prendre.
      **Le blocage de tout l'axe est donc du CONTENU, pas du code** : taguer les distracteurs,
      comme C4 l'a fait pour les compétences. ⚠️ Ne pas confondre : **C4 a tagué les COMPÉTENCES**
      (`math`, `math-6eme`), pas les misconceptions — ce sont deux registres distincts, et le
      second est vide d'usage.
      ~~**Q-5 reste à trancher par Mohamed**~~ — **tranchée le 2026-08-02 par A10** : `courseAnchor`
      en **v1 sans ancres**, tous les liens pointent le haut du cours ; on ancrera plus tard sur les
      tags que la télémétrie montrera fréquents (donc après C4bis, comme le reste de l'axe).

**Étape C — le Rappel cesse de refuser des réponses justes (étude 20, validée)**

- [x] 10. **é20 lot 1 — socle scoring ensembliste** (`accepted_answers` server-only + juge unique `is_accepted_free_answer`) — #583
- [x] 11. **é20 lot 7 — type natif `short_answer`** (moteur) — **livré le 2026-07-27** (arena#654).
      Sixième type natif, dans le cadre fermé de l'étude 03 **sans rien élargir** : aucune colonne
      (clé `{text, mistakes?}` dans `answer_key`), aucun écran (le champ du Rappel devient
      `FreeTextInput`, partagé), aucun grant. Son verdict réutilise le juge du lot 1 — donc une
      question libre accepte les paraphrases **dès sa naissance**. L'appariement des erreurs, qui
      était dupliqué entre les deux RPCs de soumission, devient `resolve_misconception_tag`
      (3 variantes, 1 fonction). Garde d'autorat R-12 bloquante dans `content:qa`.
      ⚠️ **Aucun contenu n'est authoré** : le type existe, il n'est joué nulle part tant que le
      lot 8 n'a pas écrit ses chapitres témoins (et ce lot demande une décision de doctrine).

**Étape D — la maîtrise devient visible (étude 07 puis 04-A2)**

- [x] 12. **é07 lot 2 — DB de maîtrise** (`user_competency_mastery` EWMA + oubli, trigger sur télémétrie) — #579
- [x] 13. **é07 lot 4 — panneau compétences** (« ce qui te bloque », RPCs map/blockers) — #588. ⚠️ Livré **avant** le tagging C4 : inerte par construction tant que le corpus n'est pas tagué, jamais faux
- [x] 14. **é07 lot 5 — plan compétence-aware** (`get_daily_plan` priorise par compétence) — #616, correctif de GRANT #617. Même réserve : inerte sans C4
- [x] 15. **é04 lot A2.1 — « Points faibles » — LIVRÉE le 2026-08-23** (arena#818).
      `get_my_weaknesses` rend les erreurs actives en langage élève, dans les trois langues, avec
      la compétence qui arme « S'entraîner » (le **même** `get_exercises_for_competency` que la
      correction riche : un seul chemin de remédiation), le chapitre où l'erreur se commet le plus,
      et une **tendance mesurée** sur deux fenêtres de 7 jours de `question_attempts` —
      `user_misconceptions` étant un agrégat sans histoire. Sous trois occurrences : `stable`, et
      un tiret à l'écran, parce qu'une flèche sur deux points ment.
      ⛔ Le blocage C4bis **est levé** : les 1 049 tags sont appliqués en prod depuis le 2026-08-22
      (`apply-content`, run 32629700267, vérifié en anon hors du workflow). L'écran a des lignes à afficher — mais
      seulement pour qui a répondu : une erreur exige **3 occurrences sur 2 séances**, donc les deux
      surfaces de A2 restent vides chez presque tous les comptes, et **c'est correct**. Elles ne
      rendent alors **rien** — pas d'encadré « aucune erreur détectée », qui se lirait comme un
      satisfecit sur un compte neuf alors qu'il ne dit que « on n'a pas encore assez joué »
- [x] 16. **é04 lot A2.2 — rapport parent enrichi — LIVRÉE le 2026-08-23** (arena#818).
      ⚠️ **L'avertissement de cette ligne a servi, et il avait à moitié raison.** Mesuré avant
      d'écrire : le rapport portait **déjà** `chapterInsights.weaknesses` — mais **par CHAPITRE**.
      Ce n'est pas le même axe, et les deux cohabitent : « **Fractions : 45 %** » dit _où_ ça
      coince, « **il additionne les dénominateurs** » dit _quoi_ réviser, et seul le second se
      traite le soir même. `misconceptionInsights` s'ajoute donc sous l'autre, dans le même
      encadré, sans le remplacer.
      `_student_weakness_insights` lit les erreurs d'un **autre** utilisateur : SECURITY DEFINER,
      **REVOKE de `authenticated`**, appelée seulement par `_student_report_json` une fois le
      lien parent-élève vérifié — une assertion pgTAP tient cette frontière

> ⭐ **Ce que le lot a fait EN PLUS des deux lignes, et qu'aucune des deux ne demandait — R-2
> cesse d'être recopié.** L'étude 04 promet en R-2 des « constantes **centralisées**, ajustables » ;
> elles ne l'avaient jamais été. Le triplet (3 occurrences, 2 séances, 30 jours) était écrit à la
> main dans `get_daily_plan` **et** dans `get_tutor_learner_context` (ligne 18). La 15 en aurait
> fait une troisième copie, la 16 une quatrième — un seuil pédagogique dupliqué quatre fois n'est
> plus ajustable, il est juste faux à trois endroits le jour où on y touche.
> `misconception_active_thresholds()` porte les trois nombres, `active_misconceptions()` la
> définition, et **les deux appelants vivants sont rebranchés dans la même migration**.
> ⚠️ **Et la réécriture de `get_daily_plan` a failli coûter la bande focus du tableau de bord** :
> retapée à la main, elle sortait un algorithme **entièrement réinventé** — score normalisé perdu,
> `DISTINCT ON` anti-doublon perdu, exclusion des quiz du repli perdue. C'est le `diff` contre sa
> révision vivante qui l'a montré, pas un test. La version livrée est une **substitution par
> script** sur le texte extrait, et `35_daily_plan.test.sql` — **inchangée, restée verte** — en est
> la preuve. **Une fonction SQL vivante se substitue, elle ne se retape pas.**

**Étape E — l'étage IA — ⚠️ RÉÉCRITE le 2026-08-22 : la porte est livrée, par é29**

> ⚠️ **Ce que la ligne 17 disait n'existe plus.** L'étude 29 (validée le 2026-08-20, Q-1) **raye
> le lot 0 de é11** : il n'y a qu'un socle, et c'est le lot 1 de é29 — le même adaptateur, la même
> comptabilité, les mêmes kill-switches, **plus le payeur**. Laisser la ligne 17 ouverte
> conduirait une session à écrire un SECOND socle, ce que RISK-9 nomme précisément.
>
> ⚠️ **Et la tension de calendrier a changé de nature.** A5 dégelait é11 mais A1 lui donnait le
> rang 9, et ce qui la tenait là n'était ni la conception ni la faisabilité : **une dépense
> récurrente à engager par une plateforme sans revenu**. é29 retire cet obstacle — la famille qui
> veut l'IA branche sa propre clé. La cible d'octobre n'est plus commandée par la trésorerie ;
> elle l'est par l'ingénierie, et par un pilote de mesure qui n'a pas encore eu lieu.
>
> ⚠️ **Ce que é29 n'a PAS livré, et qu'aucune ligne ne doit laisser croire acquis** : aucune clé
> réelle n'a été branchée. Le seul appel réel du système est la vérification d'une clé à sa
> saisie, déclenchée par un humain — tout le reste est testé contre un fournisseur factice, ce
> qui est la règle du §5 de l'étude et aussi sa limite. **Le pilote de deux semaines de Q-9
> précède toute activation d'une famille.**

- [x] 17. ~~é11 lot 0 — socle IA~~ → **REMPLACÉ par é29 lot 1** (Q-1 : socle unique). **Livré le
      2026-08-22**, arena#807 : adaptateur multi-fournisseur, `ai_usage_events` **avec `payer`**,
      kill-switches, et les **sept conditions de sortie** de R-6 que l'adresse libre de Q-4 exige
- [x] 18. **é11 lot 1 — explication personnalisée post-review — LIVRÉE le 2026-08-22**
      (arena#816). « Demander au Prof » sous une question ratée : quatre tables, neuf RPC, trois
      prompts système écrits **nativement** FR/EN/AR, le validateur de sortie du §3.4, et le
      **cache mutualisé** que é29 lot 5 lui avait laissé (R-15.2 — une explication d'un modèle
      curé est resservie gratuitement à tout élève ; un modèle hors liste reste privé à son
      payeur). L'écran occupe l'emplacement que é04 A1.2b avait posé (D-A1.2-5) : le lot
      **remplace un contenu**, il n'a pas refondu un écran.
      **Ce qui n'y est pas** : le mini-check (US-4) et l'escalade R-8 sont au lot 4, le chat à
      champ libre au lot 3 — la hiérarchie de confiance R-5 est déjà écrite dans les prompts,
      pour qu'elle y soit **avant** le premier texte libre.
      ⚠️ **Deux réserves à ne pas perdre.** (1) **Aucune clé de fournisseur n'a été branchée** :
      le lot est testé contre un transport mocké, comme é29 avant lui ; le **pilote Q-9** reste
      entier. (2) La **personnalisation attend l'application du corpus** — les tags de C4bis sont
      mergés, pas en prod ; d'ici là le tuteur explique sans nommer l'erreur, ce qui est une
      dégradation prévue et pas une panne.
      ⚠️⚠️ **La PR a mergé avec `pgTAP suite` ROUGE** : ses 18 assertions avortaient sur une
      fixture (`source = 'authored'`, refusé par le CHECK). Ce n'est pas un check requis — les
      quatre requis étaient verts, l'automerge a fait son travail. Correctif : arena#817, poussé
      sur une branche `wip/` **à dessein**, hors automerge, jusqu'à ce que la suite soit
      vraiment verte. ~~**Prenable maintenant**~~ : la porte existe, les deux payeurs sont
      câblés, `callAi()` attend son premier appelant pédagogique. C'est **le KPI honnête de é29**
      (§1.4) — elle réussit si é11 démarre, pas si des clés sont saisies.
      🔴 **Mais sa personnalisation dépend de C4bis, et personne ne l'a écrit jusqu'ici.** Le lot
      promet une explication « ancrée sur l'item + **distracteur** + **tag** ». Le tag n'existe
      **nulle part** dans le corpus — 0 occurrence de `misconceptionTag`, re-mesuré le
      2026-08-22. Prise telle quelle, la ligne livrera une explication contextualisée par l'item
      et l'option choisie, et **rien de ce que le mot « personnalisée » promet en plus**. Deux
      voies, à trancher par qui la prend : livrer d'abord **C4bis étape 1** (recommandé — c'est
      le rang 1 du §0), ou livrer le lot en **nommant l'écart** dans son étude plutôt qu'en
      laissant croire le contraire.
      ✅ **Prérequis d'exploitation levé le 2026-08-22** : `AI_KEY_ENC_KEY` **est posée** dans
      l'environnement de production (Mohamed). Le chemin famille n'est donc plus éteint par
      défaut. ⚠️ Une variable Vercel ne prend effet qu'au **déploiement suivant** sa pose
      (`docs/environment-variables.md`, § rotation de la KEK) : avant de conclure « le mode est
      allumé », vérifier que le déploiement courant lui est postérieur — c'est le seul point que
      cette roadmap ne peut pas mesurer d'elle-même
- [ ] 19. **é11 lots 2 → 7** dans l'ordre de l'étude (plan du jour · chat cadré · boucle de compréhension · exercices ciblés · bilans hebdo · énergie UI) — une PR par lot, cadence selon usage/coûts observés
- [x] 19bis. **é29 — mode IA « à la clé de la famille », 5 lots** — **livrée le 2026-08-22**
      (arena#807). Porte · coffre chiffré · activation par élève · coupure atomique · **la Forge**
      · consoles de dépense et d'admin. R-1 la voulait **éteinte tant qu'`AI_KEY_ENC_KEY` n'est
      pas posée** — ✅ **elle l'est depuis le 2026-08-22** (Mohamed, posée dans l'environnement de
      production ; effet au déploiement suivant sa pose). Le §8 de l'étude dit encore
      « `AI_KEY_ENC_KEY` n'est posée nulle part » : c'était vrai à sa rédaction, plus depuis.
      **Ce qui reste vrai, et c'est ce qui compte** : aucune clé de fournisseur n'a été branchée,
      et **le pilote de mesure de deux semaines (Q-9) n'a pas eu lieu**. Écarts et reste-à-faire au §8 de
      [son étude](./29-mode-ia-cle-utilisateur/ETUDE.md) — dont l'**ordre de Q-9 non suivi**
      (é11 lot 1 devait s'intercaler entre les lots 1 et 2 de é29)

## 4. FILE FONDATIONS (parallèle — ne bloque pas la file produit)

- [x] F1. **é25 — lots livrés** : 1-2 (#519/#530), 4 et 6 (#541/#543 — politique déclarative
      `harness/policy.json`, hook externalisé, invariant anti-dérive des vues générées,
      `docs/agents/`), **5a/5b/5c** (#545/#550/#560 — gardes CI portables, épinglage SHA,
      CODEOWNERS, garde « second avis » dormante) et **3** (#558 — miroir `.agents/skills/`,
      squashé sous un titre qui ne le nomme pas). **Reste le seul L7** : drill de portabilité,
      **à faire avec Mohamed** (session hors file).
- [ ] F2. **é24 — reste le lot 5** _(A2 rendu)_ : lots 3b et 4 exécutés le 2026-07-20 (#544 — le
      corpus, l'usine et `FableEtudes/` partis au privé, gate anti-fuite posé), lot 6
      resynchronisation de l'index fait ici. **Lot 5 = purge de l'historique git public**,
      volontairement **reporté à une fenêtre calme constatée** (STATUS §2) — l'historique public
      reste lisible pour mai→juillet 2026. Ce n'était PAS un prérequis de la campagne lycée : la
      scission qui l'était (3b/4) est faite, **§5-C9 est débloqué**.
      **Deuxième reliquat — RÉGLÉ le 2026-08-01, autrement que demandé** (arena#574 close,
      arena#702). Ce que cette entrée disait — « ce que le contenu garantissait en base n'est plus
      testé nulle part » — était **faux depuis le 2026-07-25** : l'analyse portée sur l'issue
      montrait que **cinq des six assertions orphelines sont couvertes à la source, et mieux**
      (Zod interdit un label vide ; l'assertion pgTAP était un faux vert — `count(*) WHERE
      label = ''` sur table vide vaut 0). Ne restaient que deux garde-fous de volumétrie.
      En cherchant ce qu'ils protégeaient, le vrai risque s'est révélé **plus grave et ailleurs** :
      le SQL d'un registre converge la base vers le fichier, donc il **purge ce qui n'y est plus** —
      et `question_competencies` part en CASCADE. Mesuré sur un Postgres réel depuis l'état
      d'après C4, un registre tronqué à 3 compétences donnait `competencies=3 mappings=0` :
      **les 1 362 mappings de C4 effacés** par un `apply-content.yml` de routine, idempotent et
      journalisé. arena#702 pose une garde **fail-closed dans le SQL émis** (compter les condamnés
      avant d'effacer, refuser au-delà d'un tiers, nommer les deux nombres et la casse
      collatérale) — sur les deux registres, compétences et misconceptions.
      **Ce qui reste, sans urgence** : un garde-fou de **volumétrie** côté corpus (« ce registre ne
      devrait pas descendre sous N ») — décision data-dépendante, donc ici, et désormais un confort
      plutôt qu'un filet, la propriété étant garantie à l'application.
      ⚠️ Leçon de méthode : le seuil pgTAP visait le bon danger **de loin**. Il ne l'attrape
      qu'après coup et seulement si quelqu'un lit — or `pgTAP suite` n'est pas un check requis
      (#689 a mergé rouge trois minutes après son ouverture le 2026-07-31). Une garde à
      l'application bat une assertion sur un check non opposable.
- [ ] F3. **é09 — la mesure. LOTS 1 ET 2 LIVRÉS** (arena#703 le 2026-08-01, **arena#708 le
      2026-08-03**) ; reste le **lot 3, conditionnel**. Condition du KPI-4 é26 (« excellent » mesurable).
      **Lot 1** : cinq vues `econ_*` derrière UNE porte admin (`admin_economy_overview`, SECURITY
      DEFINER, `is_admin()`), route `/admin/economie` en lecture seule, US-1…US-4. Deux partis pris
      qui sont le vrai contenu du lot : **jamais une moyenne seule** (p50/p90/max — une moyenne
      d'XP noie l'élève qui décroche, or c'est lui qu'on cherche) et **une estimation qui se dit
      telle** (les coins gagnés ne sont pas persistés par tentative, D-5 : les sources sont
      reconstruites, le mot « estimé » est à l'écran, et là où il n'y a pas de donnée la page rend
      un tiret — jamais « 0 % d'inflation » sur une économie à l'arrêt).
      **Lot 2 (simulateur) — LIVRÉ le 2026-08-03** (arena#708), débloqué la veille par A9.
      `npm run economy:check` rejoue 8 semaines de trois personas sur les constantes réelles, en
      **déterministe** (PRNG à graine fixe : un garde-fou qui passerait un jour et casserait le
      lendemain ne prouverait rien). Hors `verify`/`ci:verify` (D-4).
      **DEUX GARDE-FOUS CASSENT DÈS LE PREMIER RUN — et c'est le livrable, pas un incident.**
      G-1 et G-4 échouent ; ni `gamification.ts` ni les seuils n'ont été touchés. Les deux
      décisions qui en découlent sont posées en **A15/A16** au §2. C'était le protocole prévu :
      A9 avait ratifié G-1…G-4 comme **hypothèses de départ**, à corriger à la première mesure.
      **Trois corrections de fond, remontées par la confrontation à `submit_exercise_attempt`** —
      elles valent plus que le simulateur lui-même : (1) **le lot 1 encodait une règle
      inexistante**, la branche « 40-59 % → xp/10 » — le moteur n'a **aucune** règle de demi-coins,
      l'éligibilité est binaire et décide de l'XP et des coins ensemble ; (2) **les coins ne
      dérivent pas de l'XP**, c'est le forfait `exercises.reward_coins` ; (3) donc **la prémisse de
      D-5 tombe** — « les coins ne sont pas persistés, donc on estime » est vrai de la colonne et
      faux de l'information : `attempts.xp_earned > 0` signe l'éligibilité, `reward_coins` donne le
      montant, le flux se **calcule**. `sources_estimated` devient `sources_earned`, et la seule
      inconnue restante est nommée (un multiplicateur de potion n'est stocké nulle part).
      ✅ **Les trois questions d'é09 sont tranchées** (A9, 2026-08-02) : seuils ratifiés,
      revue **mensuelle** (hebdo inviterait au réglage réactif, RISK-2), lot 3 déclenché par la
      **latence** déjà journalisée et non par la volumétrie. L'étude est passée `en exécution`.
      Le piège de lecture qu'elle a révélé reste consigné au §2 : « arbitrage rendu » n'a jamais
      voulu dire « ligne exécutable ».
      **Lot 3** : conditionnel, ne se lance que sur constat mesuré (RPC > 2 s, ou écart coins jugé
      gênant) — le seuil est journalisé par la server fn, donc observé et non deviné.
- [x] F4. **C4 côté Mohamed — FAIT, constaté le 2026-07-27.** Le récapitulatif a été rendu en
      **sondant l'état réel** plutôt qu'en lisant la doc : `www.na9ranal3ab.tn` répond 200
      (l'apex redirige en 308), propriété **Search Console vérifiée** (TXT sur l'apex),
      `sitemap.xml` joignable, **DSN Sentry** posé (constaté dans le bundle prod), **GA4** déjà
      actif sans figurer nulle part, **UptimeRobot** actif, ruleset `main` en place. Livrés dans
      la foulée : **PostHog** en second puits (projet EU, sans SDK, sans PII) — arena#639 —,
      l'**auth hardening** Supabase (qui a révélé `mailer_autoconfirm=true` : aucune adresse
      n'était prouvée), le **SMTP Resend** sur `send.na9ranal3ab.tn`, et les secrets `VERCEL_*`
      sans lesquels `rollback-prod.yml` était **inopérant depuis son écriture**.
      **Règle qui en sort** : une action faite hors du repo n'y laisse aucune trace — « pas écrit
      fait » ≠ « pas fait ».
- [ ] F5. **Légal avant rentrée — GAP-024 est passé d'une moitié à trois quarts.**
      ✅ **Corrigé le 2026-08-22 : la suppression de compte EXISTE** (arena#791, le 2026-08-19 —
      migration `20260819170000_account_deletion_fk.sql`, `src/features/auth/auth.server.ts`,
      le geste dans `/parametrage`, ses tests). Cette entrée affirmait le 2026-08-10 qu'aucun des
      deux volets n'existait dans `src/` : c'était vrai ce jour-là, faux depuis neuf jours.
      🔜 **Ce qui manque vraiment, et c'est tout ce qui manque côté code** : l'**export /
      portabilité** — `export_user_data`, `exportUserData`, « portabilité » : **zéro occurrence**
      dans `src/` et `supabase/migrations/`, re-vérifié sur `main` le 2026-08-22. C'est **le
      seul bloqueur légal de la Porte 1 qu'un agent peut lever**.
      ⚠️ **Le piège d'origine reste le bon** : une PR qui cite un GAP dans son titre ne le clôt
      pas — et son symétrique vient de coûter douze jours dans l'autre sens : **un GAP qu'aucune
      PR ne cite peut avoir été livré quand même.** arena#791 s'intitule « un compte peut enfin
      être supprimé », sans un mot de GAP-024.
      ⚠️ **é29 ajoute une pièce à ce dossier** : son §3.8 demande un **registre de traitement
      INPDP** pour le mode IA. Il rejoint la démarche INPDP ci-dessous plutôt que d'en ouvrir une.
      **Ce qui EST livré le 2026-07-31** (arena#701) : `/confidentialite`
      et `/conditions`, deux **URL stables** — c'est le point : la déclaration « child-directed »
      auprès de Google (é23 Q-3) comme la conformité mineurs exigent une politique **atteignable**,
      là où une modale n'aurait pas suffi. La politique n'affirme QUE ce que le code prouve
      (inventaire préalable : PostHog UE sans profil individuel, Sentry en Allemagne, YouTube en
      `youtube-nocookie` chargé après un clic délibéré) ; elle ne nomme aucune région non vérifiée
      et ne prétend pas qu'une déclaration INPDP a été faite.
      **Reste côté humain** : la démarche **INPDP** (GAP-003), l'identité d'éditeur pour des
      mentions légales complètes, et la décision « français seul ou trilingue » — traduire un
      engagement juridique sans relecture ferait dire autre chose à une version.
      **Reste côté code, et c'est prenable dès maintenant** : **l'export / portabilité seul**
      (la suppression est livrée). Une ligne de session à part entière, pas un reliquat.
- [ ] F6. **Ops récurrent** : le triage hebdo des signalements. **Le volet technique est fait** —
      le pré-gate déterministe (#611) ne réveille l'agent que sur du nouveau, avec une soupape
      à 14 jours. Reste le **geste opérateur** : appliquer depuis `/admin/content-reports` et
      `/admin/bug-reports` les `dismissed` recommandés, ce qui referme la boucle. **La file a
      fondu** : plus 14 issues de triage ouvertes mais **1** au 2026-08-03 (arena#673) — le
      pré-gate fait son travail, le geste manque toujours.
      ⚠️⚠️ **LE MOTIF QUI TENAIT CE CHANTIER FERMÉ EST FAUX — corrigé le 2026-08-03.** Cette
      entrée disait « les trois signalements sont des artefacts, arena#638 (ouverte) montre que
      l'e2e écrit en prod chaque nuit, le geste est vain tant que le bug vit ». **arena#638 est
      close depuis le 2026-07-27, sa prémisse réfutée** : l'e2e n'a **jamais** écrit en
      production — la ligne était la seule de `content_reports` du projet **TEST**, recréée puis
      effacée chaque nuit. L'« id neuf chaque matin en prod » était un artefact de lecture.
      **La vraie panne était l'inverse, et plus grave** : le secret `PROD_SUPABASE_URL` pointait
      sur TEST depuis le 2026-07-17, donc **la boucle de triage était aveugle à la production
      pendant dix jours** — le signalement d'un vrai élève ne serait remonté nulle part. Corrigé
      par `assertProdReportSource` (arena#643) + secrets repointés le 2026-07-27.
      **Conséquence pour cette file** : il n'y a plus aucun blocage technique, plus aucune raison
      d'attendre. Le geste opérateur est le seul reste — et il porte désormais sur de **vrais**
      signalements. ⚠️ Leçon de méthode, la même que F4 dans l'autre sens : **un motif de report
      se re-vérifie avant d'être invoqué**. Celui-ci a gardé un chantier fermé une semaine de plus
      que le fait qui le justifiait.
- [ ] F7. **Dépendances majeures — la file est nettoyée, deux majors restent.** Le lot
      patch/minor étant scripté (#613, corrigé par #625 qui lui apprend à lire les lignes `0.x`),
      il ne restait que les majors et leurs issues doublonnées (#233 ≡ #595 · #236 ⊂ #594 ·
      #234 périmé, closes depuis). **Le major Supabase est fait** : `setup-cli` v2 → v3.0.0 +
      CLI 2.108.0 → 2.109.1, livré le 2026-07-25 par **#622** (ferme #594/#236). **Restent deux
      issues, une par major** (références corrigées le 2026-08-03) : **arena#595** — aligner
      `@types/node` (v26) sur le runtime CI, **passé à Node 24 depuis** (arena#688), pas 26 — et
      **arena#660** (`typescript` v7.0.2, gate rouge : `typescript-eslint` incompatible, attendre
      l'amont). ⚠️ **#660 remplace #593**, que cette entrée citait encore ; #593 est close.
- [x] F8. **Étude « IA vs déterministe » — CLOSE le 2026-07-25, 6 lots.** Ouverte le 2026-07-21
      hors roadmap (#598), elle a remplacé par des scripts les 5 surfaces de garde qui
      dépensaient des tokens sur un chemin mécanique : hook pré-commit (#608) et invariant
      d'auth des server fns passé en règle ESLint (#600), `regression-guard` pré-gaté (#604),
      garde « second avis » bornée (#606), `report-triage` pré-gaté (#611), lot patch/minor
      d'`upgrade-guard` scripté (#613, arbitrage A8). L'étude vit **au public**
      (`docs/agents/etude-ia-vs-deterministe.md`) : c'est de l'outillage, pas du contenu.
- [x] F8 bis. **Volet contenu de la même étude — arbitrage rendu ET exécuté le 2026-07-25**
      (l'entrée F8 le posait comme « arbitrage à rendre ici »). L'étude vit ici
      ([`EtudeRealisé/ETUDE-IA-VS-DETERMINISTE-CONTENU.md`](./EtudeRealisé/ETUDE-IA-VS-DETERMINISTE-CONTENU.md)),
      **5 lots livrés le jour même** : **LC0** les 7 `cours.md` de `math-8eme` dé-LaTeXés (#13) ·
      **LC1** `content:qa` attrape enfin le LaTeX et les chiffres arabo-indiens (arena#628) —
      deux règles que le skill énonçait **en regex** et que personne n'exécutait · **LC2**
      pré-gate déterministe du garde pédagogique (arena#629 + #16) · **LC3** prompt allégé de
      tout ce que le gate garantit, contrat `Locator:` obligatoire (#16) · **LC4** modèle par
      `harness/models.json`, Actions épinglées au SHA (#14), issue de suivi sur garde en panne
      (#16). Le fait qui cadrait l'étude : **le garde pédagogique n'avait jamais tourné** (token
      OAuth invalide). Leçon consignée (arena#631/#635) : **une sonde de calibration ne vaut que
      si elle exécute le même regex que le gate**.
- [x] F9. **Outillage de campagne — livré les 25-27/07, hors roadmap** (consigné ici pour que la
      file le sache, pas pour rouvrir un chantier). Côté **moteur** : `programme:etat`, l'état
      des lieux d'une campagne — registre de transcription × conformité au programme × **ouverture
      réelle aux élèves rejouée depuis les migrations** (#633/#634/#636), qui **ne classe ni ne
      recommande jamais** (décision du 2026-07-26 : l'outil donne les faits, la priorité reste
      humaine) · import outillé des illustrations libres (#623, correctif de namespace SVG #626) ·
      gate **CRLF** `eol:check`/`eol:fix` dans `verify` (#619) · gate **roadmap-sync** (#620) ·
      politique d'exécution élargie à trois dispatches d'exploitation nommés un par un, trois
      autres refusés avec motif (#640). Côté **privé** : chaîne de merge du corpus
      (#17/#26 — son bloc `permissions:` **remplace** le défaut du dépôt, il ne s'y ajoute pas,
      #27) · skill **`/campagne`** en entrée unique (#19/#21/#36) et la règle **« ouvrir une
      classe aux élèves est une PR moteur, pas un geste de campagne »** (#44) · registre rattaché
      aux sujets du programme (#23) · méthode à jour de la scission (#18) · études livrées
      regroupées dans `EtudeRealisé/` (#20/#22) · workflow `roadmap-sync.yml`.
- [x] F10. **LE GARDE PÉDAGOGIQUE — RÉPARÉ le 2026-08-14, quatre jours après l'ouverture de la
      ligne, et par personne qui l'ait prise.** L'issue **#81** est **close depuis le 2026-08-14
      à 16 h 32** et `content-audit.yml` est **vert depuis** : 08-14, 08-15, 08-19 (un dernier
      échec le 08-12, avant le correctif). Le geste était bien celui que l'issue décrivait —
      `CLAUDE_CODE_OAUTH_TOKEN` renouvelé puis remis en secret du dépôt. **Vérifié le
      2026-08-22**, pas déduit.
      ⚠️ Cette ligne a été écrite le 2026-08-10 comme **deuxième priorité de toutes files** et
      elle est arrivée sur `main` le 2026-08-16 — deux jours **après** sa propre résolution.
      Même défaut que C11, même remède : **relire l'issue avant de prendre la ligne**.
      **Ce qui suit reste vrai et vaut d'être gardé** : la leçon, pas l'état.
      **Pourquoi ça mérite une ligne et pas une note de bas de page** : `content-audit.yml` est
      la **seule** garde pédagogique de la chaîne — les gates déterministes (`content:check`,
      `content:qa:strict`, `content:audit:strict`) valident le schéma, la notation, les doublons,
      jamais la **justesse d'une clé de réponse**. Pendant ces douze jours **la plus grosse
      campagne de contenu du projet a été écrite** : `english-3eme-sec`, `english-bac`,
      `french-bac`, soit 17 sujets compilés (#136 → #148). Elle l'a été **sans filet
      pédagogique**, et ce n'est pas théorique : les correctifs #138, #140, #146, #147 et #148
      montrent que les erreurs de fond ont bien été trouvées — mais par des **audits en session,
      à la main**, chacun décidé par son auteur. Ce qu'aucune session n'a décidé de relire n'a
      été relu par personne.
      ⚠️⚠️ **CE N'EST PAS UN INCIDENT, C'EST UNE SÉRIE — trois gardes, trois pannes muettes.**
      (1) **Le garde pédagogique n'avait jamais tourné** — F8 bis, 2026-07-25, token OAuth
      invalide. (2) **Il est de nouveau en panne** depuis le 2026-07-29 — même cause, #81, la
      présente ligne. (3) **Le garde vidéo n'avait jamais tourné non plus** — #149, corrigé le
      2026-08-10 : `video-health.yml` a été exécuté **trois fois** depuis son portage (26/07,
      02/08, 09/08) et a échoué les trois fois **au même endroit, avec les mêmes 357 lignes de
      log**. Sa sonde marchait pourtant (« 0 vidéo cassée » à chaque passage) ; c'est l'étape
      d'après qui tombait — `gh` sans `GH_REPO`, dans un workspace dont la racine n'est pas un
      dépôt git parce que les deux checkouts vont en sous-dossiers. **Et le pire y est dit** :
      l'étape qui **ouvre** l'issue quand une vidéo meurt portait le même défaut et n'avait
      jamais tourné, étant gardée par `broken != '0'` — elle aurait échoué **le jour même où ce
      garde sert à quelque chose**.
      **Ce que la série apprend, et qui dépasse chaque cas** : une garde qui échoue en silence est
      **indistinguable d'une garde qui passe**, et une issue qui se re-commente toute seule cesse
      d'être lue au troisième commentaire. La question à porter à l'étude « IA vs déterministe » :
      ce qui manque n'est jamais la garde — c'est que **sa panne n'atteint personne**. Trois
      gardes sur trois l'ont montré ; il faut cesser de traiter chacune comme une surprise.
      **Le geste est humain** (renouveler le jeton, §2) ; le suivi est ici.
      ⚠️⚠️ **ET IL Y A UN QUATRIÈME CAS, trouvé depuis — la série ne s'arrête pas à trois.**
      (4) **La sonde des manuels ne tournait pas du tout sous Windows, et taisait ses pannes**
      (arena#785, 2026-08-19) ; pire, **un passage aveugle REFERMAIT l'issue en affirmant que
      tout allait bien** (#211), avant que le vrai motif ne soit trouvé — le CNP n'envoie pas son
      certificat intermédiaire (#212). Une garde qui se tait est indistinguable d'une garde qui
      passe ; une garde qui **certifie faussement** est pire que pas de garde du tout. Quatre
      gardes sur quatre ont fait l'une ou l'autre. La question à porter à l'étude « IA vs
      déterministe » ne change pas — elle s'aggrave.
- [x] F11. **Suivi parental quotidien — livré du 2026-08-16 au 2026-08-19, hors roadmap.**
      Consigné ici pour que la file le sache, pas pour rouvrir un chantier (motif F9). **Quinze
      PR** : socle de mesure du temps (arena#751 — table `learning_pulses`, pouls d'activité
      écrêté à l'horloge murale ; **avant lui, lire un cours ne laissait aucune trace**) ·
      tableau de bord jour par jour, temps / engagement / efficacité / alertes (#752) ·
      couverture du programme par matière et matières désambiguïsées (#753, #754) · filtres et
      sélecteurs de classe (#759, #762, #763, #764) · la session enfin rattachée à la tentative
      (#748, #750) · le code d'alliance retenu sur l'appareil du parent (#744) · quatre lots de
      perf et de vérité mesurée (#769, #777, #779, #782).
      Spec : `docs/suivi-parental-quotidien.md` (moteur).
      ⚠️ **Ce que ça change pour deux lignes d'ici — c'est la raison d'être de l'entrée** :
      (1) la **ligne 16** (é04 A2.2, « rapport parent enrichi ») a été écrite contre un rapport
      parent qui n'a plus la même surface — **la relire et mesurer avant de l'écrire** ; (2) le
      **volet parent de é08** (§6) ne part plus de zéro.
- [x] F12. **Le programme officiel devient une structure du produit — livré les 2026-08-16/18,
      hors roadmap.** Le menu d'un niveau liste **tout** le programme, matières à venir comprises
      (arena#749) · les chapitres se rangent sous les **sections** de leur programme (#766) · le
      fil du cours nomme la section où l'on se trouve (#767) · et `content:qa` **vérifie** qu'une
      section déclarée est bien une notion du programme (#770). Côté corpus : les 5 sections du
      programme de maths 9ᵉ (#197) et le rattachement de **446 chapitres** à leur domaine
      (#198 : 231 en maths et arabe · #199 : 178 en sciences et éducation islamique · #201 : 37
      en fiqh), la règle « les sections ne valent que pour le programme scolaire » (#202).
      ⚠️ **Ce que ça change** : la couverture d'une matière se lit désormais **contre les sections
      du programme**, plus contre un décompte de chapitres. À savoir avant de prendre **C3**,
      **C4ter** ou **C9** — et `programme:etat` n'est plus la seule lecture possible.
- [x] F13. **Manuels officiels : déclarés, liés, plus hébergés — livré les 2026-08-19/22, hors
      roadmap.** Le manuel remonte **au niveau matière** et n'est plus stocké chez nous : un lien
      vers le document là où il est déjà publié, l'adresse rebâtie **par gabarit** depuis le
      `code` que le contenu déclare — aucune URL libre ne traverse le pipeline (arena#778,
      doctrine é23 D-10 appliquée telle quelle). Côté corpus, **60 volumes déclarés** en trois
      lots (#208 primaire : 13 matières / 24 volumes · #209 collège : 15 / 30 · #210 lycée :
      3 / 6), après les 8 matières dont le code était déjà là (#206), plus une sonde hebdomadaire
      des liens (#205, #211, #212 — voir **F10**). Le bucket `manuel-eleve` est démonté
      (arena#808, débloqué par #810).
      ⚠️ **Ceci ne clôt PAS C8.** é21 lot 1 vise la **doctrine** et le pilote `manuel_ref` —
      des **exercices tracés au manuel** et un rapport de couverture. Ce qui est livré est la
      **déclaration** et la **surface de lien**. Le point de départ de C8 a changé ; sa ligne non.

## 5. FIL CONTENU (parallèle — sessions de campagne dédiées)

> Règle é26 D-6 : la largeur _catalogue_ continue sous sa propre barre de qualité (é18 axe 5,
> gates, audits). ~~**A1-Q2 rendu** : la cible de couverture pour la rentrée est le **statu quo
> consolidé à la barre é18**~~ — **AMENDÉ le 2026-08-13 par é28 Q-2** (arbitrage Mohamed).
>
> 🔴 **Le critère de priorité de cette file n'est plus « consolider l'existant » mais
> « CLASSE DE CONCOURS ENTIÈRE D'ABORD »** (é28 D-3/D-4). Ce qui **ne change pas** : la barre
> é18 reste non négociable, et **aucune classe « vitrine »** n'est ouverte sous cette barre —
> l'amendement porte sur la **priorité**, jamais sur la qualité. On n'ouvre pas plus vite en
> ouvrant moins bien (é28 RISK-4).
>
> **Pourquoi** : un élève de 6ᵉ qui ne trouve pas le français ne conclut pas « le français
> arrive », il conclut « ce site ne couvre pas mon concours » et ne revient pas (é28 D-4). La
> complétude d'une classe de concours prime donc sur l'ouverture d'une classe nouvelle.
>
> **Conséquence immédiate, et c'est la seule ligne que cet amendement crée** : **C4ter
> (`french-6eme`) passe devant toute autre ligne de cette file après C4bis.**

- [x] C1. **Corrections qualité — FAIT le 2026-07-25.** Les 9 issues sont closes : `french-8eme` 2 BLOCKER (#336/#337) + 6 MAJOR (#338/#339/#340/#341/#342/#343) · `math-bac-math` (#344), corrigées ici par la PR #6. ⚠️ **Leçon de la scission** : une PR de correction avait été ouverte dans le dépôt **public**
      (#610) — elle a dû être **fermée sans merge**, le gate anti-fuite refusant du corpus
      là-bas. Une correction de contenu se fait ici, jamais dans le moteur.
      **Deux corrections ont suivi** : `math-8eme` — plus une seule commande LaTeX dans les cours
      (#13, lot LC0 de F8 bis : 7 chapitres livraient du `\dfrac` que l'élève lisait tel quel,
      l'app n'ayant aucun moteur de rendu) — et la double option méta du défi élite `french-8eme`
      (#15).
- [ ] C2. **é23 lot 5 — campagne vidéos maths 9ᵉ** (débloquée : Q-1 arbitrée, skill `content-videos` + health-check livrés #527/#531) — puis extension aux autres matières concours au fil de l'eau
- [ ] C3. **é16 vague A — 1ère secondaire : 4 matières sur 5 EN PRODUCTION, reste l'arabe**
      _(état corrigé le 2026-08-10 — cette ligne se lisait « les 4 matières restantes », non
      entamée, alors que la vague était presque finie)_. En prod au **2026-08-04** : math,
      physique, SVT et **français** (#119, 7 modules, 203 questions, 7 défauts de fond levés par
      l'audit). **Reste la seule matière `arabe`**, et elle est **bloquée à la source** : sa fiche
      de programme est `partielle`/`first-pass`, donc génération interdite tant que le **محور 3**
      n'est pas transcrit — c'est une tâche de **transcription** (C9), pas de génération.
      ⚠️ **Ne pas lire « 1ère sec = 4/5 » comme « la classe est à moitié vide »** : elle compte
      **6 matières en ligne**, `chimie-1ere-sec` (#114) et `english-1ere-sec` (#117, #120)
      s'étant ajoutés **hors vague A**. Les chiffres à jour, relus sur `origin/main` et non
      recopiés du tableau de suivi : chimie **2 chapitres codifiés sur 11**, anglais **6 sur 35**,
      français **7 sur 7** (arena#714). ⚠️ Le tableau de suivi annonçait « 35/35 » et
      « 11 chapitres » : une session qui lit « LIVRÉ » saute la matière, et **38 chapitres
      seraient partis en silence**.
      Cadre inchangé : base fidèle au programme + overlay `prof-*-lycee` d3/d4 ; une matière =
      une session ; génération native fr (décision 2026-07-13)
- [x] C4. **é07 lot 3 — tagging compétences vague 1 — FAIT le 2026-07-27.** `math` (9ᵉ) **557/557**
      et `math-6eme` **805/805**, soit **1 362 questions** en 10 PRs (#51, #53, #54, #55 pour la 9ᵉ ;
      #56 → #61 pour la 6ᵉ), 1 à 3 compétences par question, la première étant la principale.
      Les trois lots produit livrés mais inertes (maîtrise EWMA é07 lot 2, carte « ce qui te
      bloque » lot 4, plan quotidien compétence-aware lot 5) **s'allument sur ces deux sujets**
      dès que le contenu atteint la prod.
      **Pour le stop-point Q-1** (validation humaine de l'échantillon, jamais rendue) : les
      **57 compétences du registre sont toutes mobilisées, aucune n'est morte** — le calibrage
      « granularité medium ~55-70 » est désormais vérifié par l'usage et non seulement par
      construction. Les deux manques ressortis en creux — **`math.num.valeur-absolue`** et
      **`math.stat.mode`** — ont été **tranchés par Mohamed le 2026-07-31 et livrés** (#90) :
      registre à **59 compétences**, **16 questions re-taguées** (et non 18 comme annoncé d'abord —
      le recensement à la main confondait les tableaux Markdown de statistiques avec des valeurs
      absolues, refait sur un discriminant vérifié). Une question garde son tag voisin :
      `07/04-defi#1` porte déjà 3 compétences et le plafond est de 3 — choix assumé.
      **Appliqué en prod le 2026-08-01**, registre compris.
      **Vagues suivantes** (hors périmètre de ce lot) : les autres matières et les autres niveaux
      restent non tagués — la famille `math` couvre `math*`, une famille `physique`/`svt` reste à
      écrire par l'architecte avant tout tagging scientifique.
- [x] C4bis. **Tagging des MISCONCEPTIONS — LIVRÉ le 2026-08-22** (#219) _(A11 rendu le
      2026-08-02)_.
      **1 049 distracteurs tagués sur 2 454 (43 %), sur les VINGT chapitres** — et le périmètre
      n'était plus celui qu'A11 décrivait : le corpus comptait 818 questions sur 20 chapitres,
      pas 557 sur 13. Sept chapitres sont arrivés depuis l'étape 0 ; s'arrêter à 13 aurait laissé
      un tiers de la matière muette.
      **Registre 56 → 154 entrées**, 149 mobilisées, **154/154 déclarant leur `competency`**.
      Trois domaines entiers n'avaient **aucun mot** — probabilités, puissances, quadrilatères —
      et un quatrième n'en avait qu'un (orthogonalité dans l'espace) : ils sont arrivés APRÈS
      l'étape 0, qui avait couvert les 13 chapitres d'alors.
      **43 % n'est pas un travail à moitié fait** : c'est la part des distracteurs qui portent une
      erreur NOMMABLE. Les systèmes plafonnent à 10 % (leurs mauvaises réponses sont des couples
      numériques faux), la valeur absolue atteint 75 % (presque chaque option fausse y est une
      règle mal appliquée). Un distracteur sans erreur nommable **reste sans tag** — le champ est
      optionnel par conception, et nommer une erreur au hasard afficherait un diagnostic faux à
      un enfant de 9ᵉ.
      🔜 **Ce qui reste, et c'est un geste, pas un chantier** : **appliquer le corpus en prod**.
      Les tags sont sur `main` et n'atteignent aucun élève ; les quatre lots qu'ils allument
      restent inertes tant que `apply-content.yml` n'a pas tourné.
      **Vague suivante** : `math-6eme` (805 questions déjà taguées en compétences par C4) — les
      5 entrées non mobilisées du registre décrivent précisément ce bout-là de la famille.
      ⚠️ Un défaut de contenu croisé en chemin, non corrigé : `08-thales/quiz` Q1, l'option `d`
      est mathématiquement ÉQUIVALENTE à la bonne réponse. À traiter par `content-audit`.

<details><summary>L'état d'avant le 2026-08-22 (conservé : il porte l'arbitrage A11 et l'étape 0)</summary>
      🔴 **ÉTAPE 0 FAITE le 2026-08-04 (#118), ÉTAPE 1 À PRENDRE — PREMIÈRE LIGNE DE TOUTE LA
      ROADMAP au 2026-08-22**, toutes files confondues. Elle était **troisième** au 2026-08-10,
      derrière C11 et F10 : **les deux sont tombées** (et aucune n'a été prise — voir leur ligne),
      celle-ci n'a pas bougé d'un tag en douze jours.
      🆕 **Ce qui est neuf, et qui la fait changer de catégorie** : depuis é29, elle ne commande
      plus seulement l'axe adaptatif — elle commande aussi **l'étage IA**. La **ligne 18** (é11
      lot 1) promet une explication « ancrée sur l'item + distracteur + **tag** ». Le tag n'existe
      nulle part : **0 occurrence de `misconceptionTag`**, re-mesuré le **2026-08-22** sur les
      **719 chapitres** du corpus. Un seul travail de contenu débloque désormais **quatre lots
      é04/é07 déjà mergés, les lignes 15 et 16, et la première brique pédagogique de l'IA**.
      ✅ **Ce qui est fait — une étape 0 que l'arbitrage ne prévoyait pas, et elle avait raison
      d'exister.** A11 décrivait C4bis comme « deux gestes par question ratée : le tag sur le
      distracteur et l'entrée correspondante au registre ». Vérifié avant de commencer, l'énoncé
      sous-estimait le point de départ : les 5 entrées existantes décrivaient des erreurs de
      fractions, de décimaux et de pourcentages — le bout **6ème** de la famille. Sur les
      **31 compétences des domaines de 9ème** (alg, fn, vec, geo, stat, esp), **pas une** n'avait
      de misconception en face : il n'y avait rien contre quoi taguer. Taguer et écrire le
      vocabulaire dans le même geste aurait produit un registre **au fil de l'eau**, avec les
      doublons et les formulations divergentes que produit toujours un vocabulaire écrit en marge.
      Le registre est donc passé de **5 à 56 entrées**, les 51 neuves couvrant les 13 chapitres de
      `math` 9ᵉ, et **les 5 anciennes ont gagné le `competency`** qu'elles n'avaient pas —
      **56/56 le déclarent** aujourd'hui.
      🔜 **Ce qui reste — l'étape 1, le tagging lui-même** : poser `misconceptionTag` sur les
      distracteurs des **557 questions** de `math` 9ᵉ, contre le vocabulaire désormais fixé.
      ⚠️ **Ne pas confondre avec C4**, qui a tagué les **compétences** : ce sont deux registres
      distincts, et celui des misconceptions reste **vide d'usage côté corpus** — 0 occurrence de
      `misconceptionTag` sur ~18 700 questions, mesuré le 2026-07-31, **re-mesuré inchangé les
      2026-08-03 et 2026-08-10**. C'est le corpus qui manque, plus le registre.
      **C'est le déblocage de TOUT l'axe adaptatif** : sans lui, `user_misconceptions` reste vide
      en prod, la correction riche (ligne 9) ne nomme aucune erreur, le geste « m'entraîner »
      livré le 2026-08-03 ne s'affiche chez personne, le terme « misconceptions » de
      `get_daily_plan` vaut zéro, et la ligne 15 livrerait un écran vide.
      **Le compte des lots que ce seul travail de contenu allume : quatre** — é04 A1.2a, A1.2b,
      le geste « m'entraîner », et le terme misconception d'A1.1. Tous sur `main`, tous inertes.
      **Périmètre arbitré : `math` 9ᵉ seulement** (557 questions, déjà tagué en compétences par
      C4). Le pilote donne un **coût réel par question** avant d'engager `math-6eme`, et allume
      l'écran sur la matière de concours. **Il ne reste qu'un geste par question ratée** depuis
      l'étape 0 : `misconceptionTag` sur les distracteurs, pointant une des **56 entrées** de
      `content/misconceptions.json`. Le second geste — écrire l'entrée **avec son `competency`**
      (A12), sans quoi « m'entraîner » reste mort — est **déjà fait** (#118) ; il ne se rouvre que
      si un distracteur ne trouve aucune entrée qui le décrive.
      ⚠️ Le champ est **optionnel par conception** (arena#707) : une confusion de vocabulaire ou
      une erreur de lecture d'énoncé n'a pas de compétence propre, et il vaut mieux ne rien
      proposer qu'un exercice au hasard. Ne pas en inventer une pour remplir la colonne.
</details>

- [ ] C4ter. **`french-6eme` — compléter la 6ᵉ, classe de CONCOURS** _(é28 Q-2/D-4, arbitré le
      2026-08-13)_.
      🔴 **DEUXIÈME LIGNE DE CETTE FILE, juste après C4bis** — l'amendement de é28 Q-2 la place
      devant tout le reste du fil contenu.
      **Le fait** : la 6ᵉ a **3 matières avec du contenu** (math, arabe, éveil) pour **6 fiches
      de programme transcrites**. Le **français a sa fiche et zéro contenu** — sur une classe de
      **concours**, dont le français est une épreuve.
      **Ce n'est pas un blocage de source.** La fiche est `partielle`, et depuis l'amendement
      **R-5 du 2026-07-29** une fiche partielle ne bloque plus la matière : on génère
      **chapitre par chapitre**, sur les seules sections transcrites à profondeur de génération.
      Le seul motif du retard est qu'aucune session ne l'a prise.
      **Barre inchangée** : é18 axes 1-5, gates contenu, audit — la priorité change, pas la
      qualité (é28 RISK-4). Une matière se livre **entière ou par tranches ≤ 4 chapitres**,
      jamais en échantillon vitrine.
      **Ensuite, dans le même esprit** : les deux autres matières de 6ᵉ sans contenu (anglais,
      islamique) puis la vérification que la 9ᵉ tient bien la barre é18 sur ses 6 matières. Le
      **Bac n'entre pas ici** — cinq de ses six sections n'ont aucune fiche transcrite, c'est un
      LOT A de transcription et un chantier **septembre→janvier** (é28 D-6).
- [ ] C5. **é20 lots 2 → 4 — réponses acceptées.** **Lot 2 (Tier A) livré le 2026-07-27**
      (arena#652) : l'expansion morphologique — article arabe plié dans les deux sens, articles
      fr/en, contractions — est une **fonction pure appliquée au build**, pas des variantes
      écrites dans le corpus (une dérivée de la clé n'est pas une décision d'auteur). Mesure sur
      le corpus réel : **13 017 des 13 049 questions éligibles** au Rappel gagnent au moins une
      forme acceptée, 24 932 variantes, 42 refusées par R-4 ; le gisement « article » arabe
      (1 851 clés) est couvert à **1 849**. Écart assumé : la langue est prise du
      `contentLanguage` déclaré au lieu d'être déduite — appliquer les trois langues produisait
      « an Afrique ».
      **Lot 5 livré le 2026-07-27** (arena#655) — et son constat corrige l'énoncé du lot : la
      barre de caractères n'offrait que 8 formes rares, **toutes repliées par la normalisation**,
      donc les taper ne changeait même pas le verdict. Le vrai manque était **l'alphabet**, pour
      l'enfant sans clavier arabe. ⚠️ Les **translittérations** du lot 5 ne sont pas livrées :
      elles relèvent des Tiers A/B.
      **Lot 3 livré le 2026-08-01** (#96), après levée de la mise en attente du 2026-07-27 : le
      skill `content-accepted-answers` et son pilote sur `math-1ere/07-reperage-espace`, la
      mission même où le défaut avait été constaté. 25 des 30 questions couvertes ;
      « فوق الشجرة » est enfin acceptée là où « فوقها » était attendue, distracteurs toujours
      refusés. **Dette remontée** : Tier A produit « الفوقها » en préfixant « ال » sans condition
      — inoffensif au scoring, mais consomme la borne des 24. Candidat à un lot moteur.
      **Reste** : **lot 4** (campagne Tier B, 1 matière par PR) — à décider sur la base du pilote,
      c'est ce que l'arbitrage prévoyait ; lot 6 (refus contesté, optionnel) ; lot 8 (pilote
      `short_answer`, qui attend en plus la doctrine R-14).
- [ ] C6. **Illustration — backlog é18 (ordre petites-classes-d'abord)** : 4ᵉ puis 5ᵉ année (toutes matières visuelles) → maths 7ᵉ (5 ch.) → maths 9ᵉ fonctions+stats (2) → iq-training (3) → français (1). **Entamé le 2026-07-26** : 10 figures « objet réel » remplacées par des illustrations libres en `eveil-2eme` (#10) et **23 figures** de la campagne animaux sur 1ᵉʳ → 4ᵉ année (#11), outillées par l'import du moteur (arena#623). Le reste de la liste est inchangé
- [ ] C7. **é19 lot 1 — doctrine + gate figures questions** _(A3 rendu : SVG seul, vérification intégrale, lots ≤ ~40 figures)_, puis campagne questions illustrées (concours d'abord : 6ᵉ/9ᵉ/bac)
- [ ] C8. **é21 lot 1 — doctrine manuels** _(A4 rendu : verbatim court non créatif toléré ; provenance NON affichée à l'élève, lot 3 abandonné)_, puis pilote `math-1ere-sec` (exercices tracés `manuel_ref`, rapport de couverture)
- [ ] C9. **Transcriptions secondaire (fil continu, METHODE-GENERATION-CONTENU).**
      ⚠️ **Cette ligne décrivait l'état du 2026-07-20 — une campagne lycée entière s'est jouée
      depuis, sans jamais repasser ici. Rattrapée le 2026-08-10.**
      **Transcrit du 2026-08-04 au 2026-08-06** : `anglais 2ème sec` tranche 1, et le montage
      ⚭×4 sous un nœud legacy (#126) · `français 2ème sec`, chapitrage des 18 séquences, palier
      partiel honnête (#128) · **`anglais 3ème sec`** — la seule matière du lycée qui sert
      **six classes d'un coup** (#129, #131), R-7 rendue et ses trois écarts (#133) ·
      **`anglais bac`** — un manuel, six terminales (#130), second palier **84 % → 92 %** (#134),
      le WORD LIST qui ne s'extrait pas mais se lit (#135), R-7 rendue et ses **huit** écarts
      (#142) · **`français bac`** (#132), avec l'éco-gestion tranchée par constat ·
      **`philosophie bac`** — ossature + chapitrage mutualisé ×5 (#127), puis le **مبحث 2**
      transcrit en entier, premier chapitre générable (#143).
      **Généré dans la foulée** (même fenêtre, matières ci-dessus) : `english-3eme-sec` ch.01-06
      (#136, #139, #144) et `english-bac` ch.01-06 — ch.01-03 (#137) puis la **tranche 2**
      ch.04-06 le 2026-08-10 (**#145**, « la fuite que je ne mesurais que d'un côté ») — **un
      dossier authored une fois, six terminales servies** — puis `french-bac` ch.01-03 (#141).
      Les correctifs d'audit qui ont suivi comptent autant que les tranches : #138, #140, #146,
      #147, #148 — **le manuel officiel s'est contredit plusieurs fois**, et c'est un audit en
      session qui l'a vu, pas un gate (voir **F10**).
      **Reste** : `math-2eme-sec-sciences` (12/19 ch.) · le **محور 3 d'arabe 1ère sec**, seul
      verrou de C3 · la suite du lycée. **La campagne de GÉNÉRATION lycée massive est débloquée**
      depuis l'exécution des lots 3b/4 de é24 (#544) — elle n'attendait pas le lot 5.
- [ ] C10. **Campagne petites classes — EN COURS depuis le 2026-07-26, hors roadmap.** Elle
      tournait sans ligne ici ; la voici, avec son état constaté au 2026-07-27 :
      **`french-4eme`** chapitres 00→05, en deux tranches (#24, #28 qui ajoute le chapitrage au
      manifeste) · **`french-5eme`** modules 1→8, en deux tranches (#29, #30) ·
      **`arabic-6eme`** : les 7 chapitres de l'unité 1 (#39, #41, #43, #46), puis un **audit
      indépendant** — 252 clés re-résolues, **7 bloquants dont une règle d'orthographe fausse**
      (#47) — et sa correction intégrale (#49). **Leçon à ne pas reperdre** : ces 7 chapitres ont
      été publiés **avant** l'audit ; lancer `content-audit` avant d'ajouter des chapitres, pas
      après. En parallèle, la **fiche 6ᵉ base** avance : `eveil` transcrit p.20→70 (#31→#34, #37,
      #38, #40, #42, #45, #48) et `arabe` passée à la barre R-5 (#35).
      ⚠️ **Générer n'est pas ouvrir** : aucune de ces classes n'est visible des élèves tant
      qu'une **PR moteur** ne l'ouvre (#44) — l'état des lieux le rapporte depuis arena#636.
      À confronter à **A1-Q2** (statu quo consolidé à la barre é18, aucune classe vitrine) au
      prochain point : la roadmap constate, elle ne tranche pas à la place de Mohamed.
      **Suite constatée le 2026-08-03** : la campagne a continué sans repasser ici —
      **`education-islamique-5eme`** est un **sujet neuf**, ses 10 chapitres livrés en 4 tranches
      (#105 → #109) · **`math-bac-math`** ch.16-19, le manuel couvert en entier (#100), puis la
      correction de 4 épisodes qui clonaient l'annale (#104) · `arabic-2eme-sec-lettres` ·
      `arabic-6eme` (suite).
      **Suite constatée le 2026-08-10** : `education-islamique-5eme` a reçu les **huit retouches
      d'un audit indépendant** — et le blocker que cet audit avait **inventé** (#123, à lire :
      un audit peut se tromper dans les deux sens).
      ⚠️⚠️ **ET GÉNÉRER N'EST PAS APPLIQUER.** Ce paragraphe listait à la main ce qui avait été
      produit depuis la dernière application, en prévenant que « rien ici ne peut vérifier l'état
      réel de la prod ». **Ce n'est plus vrai** : la garde `content-drift` le mesure depuis le
      2026-08-04, et l'écart a désormais **sa propre ligne, C11**, avec un chiffre au lieu d'une
      liste. Nuance conservée, à ne pas confondre avec le « générer n'est pas ouvrir » ci-dessus :
      le parcours **5ᵉ base est ouvert depuis le 2026-06-20**
      (`20260620140000_open_5eme_base_parcours.sql`), donc l'islamique 5ᵉ ne demande **aucune PR
      moteur** — seulement un run `apply-content.yml`. **Du contenu généré et jamais appliqué est
      du travail invisible pour l'élève.**
- [x] C11. **PUBLIER CE QUI EST DÉJÀ MERGÉ — FAIT, et la ligne était déjà fausse en arrivant.**
      🟢 **L'écart est refermé, vérifié le 2026-08-22.** L'issue **#124** est **close depuis le
      2026-08-10 à 17 h 46** — soit *le jour même où cette ligne a été écrite*, et **six jours
      avant qu'elle n'atteigne `main`** (#152/#184, mergées le 2026-08-16). Depuis :
      `content-drift` **vert tous les jours** (dernier passage le 2026-08-22), **aucune issue
      ouverte dans ce dépôt**, et `apply-content.yml` a tourné avec succès le 2026-08-20 et
      **cinq fois le 2026-08-22**. Les 18 sujets sont en production.
      ⚠️ **La leçon n'est pas « la ligne était inutile ».** L'écart de 18 sujets était réel, et la
      garde l'a rendu visible — c'est exactement ce pour quoi elle existe. La leçon est que cette
      roadmap a désigné comme **PREMIÈRE LIGNE DE TOUTE LA FILE un chantier déjà refermé**, parce
      que la PR qui la portait est restée **six jours en draft** (§8, 2026-08-16). Une priorité
      écrite le jour J et mergée à J+6 n'est pas une priorité : c'est un instantané périmé.
      **Relire l'issue avant de prendre la ligne.**
      **Ouvrir n'est pas publier — et les deux ont eu lieu** : arena#741 ouvre la rubrique
      « Éducation islamique » (migrations `20260814120000` / `20260815120000`) et **arena#760**
      les **4 sections bac** dont le contenu était prêt (R-8). C'est le geste **moteur** que
      **C10** distingue de la génération, et il a été fait sans qu'aucune ligne ne le demande.
      **Le geste, s'il faut le refaire un jour, tient en une ligne** : Actions → *Apply content
      (PROD)* → `dry_run: false`,
      **`subjects` laissé vide** (applique tout le corpus : idempotent, journalisé dans
      `content_releases`, et c'est le geste le plus sûr quand plusieurs sujets sont en retard).
      L'issue se referme **d'elle-même** au passage suivant de la garde. C'est un des dispatches
      **explicitement autorisés** à un agent par la politique d'exécution — il ne publie rien de
      neuf, seulement le SQL compilé d'un corpus déjà mergé et validé.
      **Ce qui suit est l'historique du prérequis, gardé parce qu'il porte A17, toujours ouvert.**
      🚨 **PRÉREQUIS RENCONTRÉ EN ÉCRIVANT CETTE LIGNE — le dispatch a été inexécutable
      quelques heures.** `apply-content.yml` fait `npm ci` sur le moteur, et ce `npm ci`
      échouait : `Missing: typescript@5.9.3 from lock file`.
      ⚠️⚠️ **CORRECTION DU 2026-08-10, ET ELLE PORTE SUR CE QUE CETTE LIGNE AFFIRMAIT
      ELLE-MÊME.** La version précédente désignait comme **cause** l'écart de Node entre les deux
      dépôts (le moteur à 24 depuis arena#688, les six workflows d'ici restés à 22) et présentait
      leur alignement comme **le correctif**. **C'est faux, et l'inversion est instructive.**
      **La cause est un lockfile défectueux**, livré par **arena#716** : une PR intitulée « bump
      undici · dependency-type: indirect » qui modifiait en réalité `package.json` et faisait
      passer `@cloudflare/vite-plugin` de `^1.40.2` à `^1.51.1`, entraînant en cascade
      **miniflare 4 → 5 alpha**, workerd et wrangler — un saut de **majeure** et une **alpha**
      dans la chaîne de build, sous un intitulé de bump indirect. **Le correctif est
      arena#718**, qui **revert** #716 : une simple resynchronisation du lockfile
      (`npm install --package-lock-only`) suffisait à reverdir `npm ci` — elle a été essayée et
      elle marche — mais elle aurait **gardé l'alpha et la majeure que personne n'a arbitrées**.
      ⚠️ **Ce que l'écart de Node explique vraiment — et c'est l'inverse d'une cause.** npm 11
      (Node 24) **acceptait** ce lockfile ; npm 10 (Node 22) le **refusait**. Donc la CI du
      moteur était verte sur #716, et **la Content CI d'ici a été le SEUL détecteur de tout le
      système**. Elle n'a pas échoué parce qu'elle était mal configurée : elle a échoué parce
      qu'elle avait raison.
      ⚠️⚠️ **Conséquence à assumer, pas à enterrer** : en alignant les six workflows sur Node 24,
      la PR #150 a **supprimé ce détecteur**. L'alignement reste défendable pour lui-même — faire
      tourner les scripts du moteur sur un Node que le moteur n'utilise pas est un risque en soi,
      et le `.nvmrc` du moteur dit 24 — mais il a été **vendu comme un correctif qu'il n'était
      pas**, et il a un **coût qui n'était écrit nulle part**. ⚠️ La propriété perdue était de
      toute façon **accidentelle** : elle venait de la sévérité de npm 10, pas d'une intention.
      S'y fier était fragile. **À arbitrer (voir A17, §2)** : revenir à Node 22 pour garder le
      canari, ou tenir Node 24 et poser un vrai gate — celui qui manque vraiment n'est pas une
      version de Node, c'est **une garde qui refuse une PR de dépendance dont le diff dépasse ce
      que son titre annonce**.
      ⚠️ **Le piège de lecture qui a laissé passer dix jours** : `apply-content.yml` est désarmé
      **volontairement** (é24 lot 3a). Ni la CI verte, ni l'automerge, ni `content_releases` — qui
      ne sait que ce qui a été appliqué, jamais ce qui manque — ne signalent le geste absent. La
      garde #124 est précisément ce qui rend l'écart **visible** ; elle ne le **referme** pas, et
      une issue ouverte qu'on croise sans la prendre coûte autant qu'une garde en panne (**F10**).
      **Ce qui supprimerait le risque à la racine reste le lot 3b d'é24** (répétition sur TEST +
      arbitrage §4.3) — armer le déclencheur. Une garde ne re-designe pas le canal qu'elle
      surveille : entre un merge et le passage suivant, la prod est en retard sans que personne ne
      le sache.
- [ ] C12. **Sous-rubrique فقه — « الرسالة » d'Ibn Abî Zayd. EN COURS depuis le 2026-08-13,
      hors roadmap.** Elle tournait sans ligne ici ; la voici, état constaté au **2026-08-22** :
      **37 chapitres sur `main`** en neuf tranches (#172 → #181), rattachés à leur livre (#201),
      et **la rubrique est ouverte aux élèves** — arena#738 (thème) puis **arena#741** (parcours
      `education-islamique` passé `coming_soon` → `available`).
      **Ce que la campagne a produit au-delà des chapitres, et qui vaut la ligne** : un contrôle
      de fidélité au texte source (#174) · une tranche **arrêtée au contrôle, corrigée, puis
      livrée** (#175) · et des audits qui ont **corrigé trois faussetés déjà en production**
      (#178) avant de ramener trois chapitres à zéro écart (#179). C'est précisément la boucle
      que la panne de **F10** rendait impossible ailleurs pendant la même période.
      **Reste — huit أبواب sur 45.** Les 37 chapitres couvrent les أبواب **01 → 32, 34, 36, 38,
      41 et 42** ; manquent les **33, 35, 37, 39, 40, 43, 44, 45** (relevé sur les préfixes de
      `content/fiqh/` au 2026-08-22, un dossier par باب).
      ⚠️ **À ne pas relire comme C10** : ce n'est pas une classe de l'école, c'est une rubrique
      **Extras**. Elle ne concourt donc ni à la barre é18 par classe, ni à la priorité « classe de
      concours entière d'abord » (é28 D-4) — elle ne passe **pas** devant **C4bis** ni **C4ter**.

## 6. FILES DIFFÉRÉES (ne rien lancer avant leur porte d'entrée)

| File                                                             | Porte d'entrée                                                      | Contenu                                                                           |
| ---------------------------------------------------------------- | ------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| ~~**V2 — concours**~~ **SORTIE DU DIFFÉRÉ le 2026-08-13** (é28 Q-4), **puis LIVRÉE le 2026-08-16** | ~~V1 ≥ M3 **et** annales transcrites~~ — **porte levée** | ~~**é02 se re-scope maintenant**~~ → **é02 est re-scopée, exécutée et close** (arena#743 lots 1-2, arena#746 lots 3-4 ; [étude](./EtudeRealisé/02-examen-blanc/ETUDE.md)). Le v1 est bien **borné SANS annales** : assemblage chronométré du corpus existant + rang relatif, et le barème porte les **coefficients réels du concours** (maths 4, arabe 2+2, français 3, sciences 3, anglais 1) dont la note /20 dérive. Les annales restent un **enrichissement** — chantier de **contenu**, **non ouvert** : si quelqu'un le lance, il entre en file CONTENU (§5), pas ici. Motif (é28 M-2) : un parent tunisien juge sur « est-ce que ça prépare au concours », et c'est le plus gros écart produit face au marché. Wording premium toujours proscrit (phase gratuite) — R-7 a d'ailleurs été **rescopé** pour cette raison : le mode est ouvert à tout compte. ⚠️ **Reliquat à porter par qui reprend** : Q-2 (cadence éditoriale = mitigation de RISK-1), Q-4 (lot 6 optionnel : détail par chapitre + remédiation) et **Q-5 (vérifier en base que la session 1 est `published`)** |
| ~~**V4 — parent**~~ **SORTIE DU DIFFÉRÉ le 2026-08-13** (é28 Q-3) | ~~é04-A2.2 livré (ligne 16)~~ — **porte levée** | **é08 se re-scope maintenant** sur son **volet enseignant** : code de classe, liste d'élèves, taux de réussite par chapitre — la mécanique existe déjà (le rapport parent par code alliance est le même objet). Motif (é28 M-3) : c'est le seul canal à **CAC ≈ 0** au budget réel (1 000-2 000 TND/an). ⚠️⚠️ **MAIS LE VOLET PARENT NE PART PLUS DE ZÉRO — ajouté le 2026-08-22.** Quinze PR ont livré le **suivi parental quotidien** hors file entre les 2026-08-16 et 08-19 (**F11**, §4) : socle de temps mesuré (`learning_pulses`), tableau de bord jour par jour, couverture du programme par matière, niveau scolaire affiché, et le tableau de bord **ouvert au rapport public par code**. é08 doit se re-scoper contre **ce** point de départ, pas contre celui de sa rédaction — sous peine de spécifier des écrans qui existent. Le digest hebdo IA reste, lui, derrière é04-A2.2 (ligne 16) — elle-même à relire pour la même raison. ⛔ **Précondition dure é28 D-5, et elle bouge à moitié** : **GAP-024 est aux trois quarts** — la suppression de compte est livrée (arena#791), **l'export/portabilité non** (**F5**) ; **GAP-003** reste à trancher. Aucune démarche vers un établissement avant les deux |
| **Gels — actés (A1-Q3, 2026-07-20)** ; application par é26 lot 2 | Dégel par décision humaine explicite uniquement                     | é06 (PWA offline) · é10 (anti-fraude — se dégèle au volume) · é12 (studio in-app) |
| **Gelée (phase)**                                                | Sortie de la phase gratuite (décision humaine)                      | é01 (paiement en ligne — véhicule de réactivation du premium)                     |

## 7. Vue jalon — ce qui doit être vrai le 1ᵉʳ septembre 2026

| Axe        | Cible rentrée                                                                                                                                                                                                  | État au **2026-08-22 (J-10)**                                                                                                              |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| Produit    | File V1 étapes **1-16** livrées (é22 complet dont bannière rentrée · Révision du jour · correction riche · Rappel tolérant lot 1 · maîtrise visible · points faibles + rapport parent)                         | **19/20 lignes faites.** Les **15 et 16 sont livrées le 2026-08-23** (arena#818) — é04 A2, et avec elles **l'étude 04 est finie**. La **18** l'est depuis le 2026-08-22 (arena#816). Ne reste que la **19** (é11 lots 2-7). La cible « points faibles + rapport parent » est donc **atteinte**. 🟢 **La 15 est DÉBLOQUÉE** : C4bis a livré 1 049 tags le même jour, l'écran a enfin des lignes à afficher. ⚠️ **Après l'application du corpus en prod, pas avant** — les tags sont mergés, pas appliqués |
| IA         | A5 **rendu le 2026-07-20** : é11 dégelée (lots 0-2, pilote math 9ᵉ, budget 5 $/j, tuteur « El Ostedh »). ⚠️ **Le socle n'attend plus** : é29 l'a livré le 2026-08-22 (arena#807), avec un second payeur — la famille | 🟢 **LA PORTE EST ALLUMÉE, ET L'ÉTAGE PÉDAGOGIQUE A COMMENCÉ.** é29 déployée (`/api/health` → `548a429`), `AI_KEY_ENC_KEY` posée (Mohamed, 2026-08-22), et **é11 lot 1 livré le même jour** (arena#816) : explication personnalisée, escalier de reformulation, cache mutualisé, retour 👍/👎. Le KPI que é29 se donnait — « elle réussit si é11 démarre » — est atteint. **Restent** : le **pilote Q-9** (aucune clé de fournisseur n'a jamais été branchée) et **é11 lots 2-7** |
| Contenu    | Classes existantes à la barre é18 · 1ère sec complète (5 matières) · vidéos 9ᵉ · Tier A `acceptedAnswers` corpus entier · cible arbitrée (A1-Q2) = **statu quo consolidé à la barre é18**, sans classe vitrine | 🟢 **C4bis EST LIVRÉE** (#219, 2026-08-22) : 1 049 distracteurs tagués sur 2 454, registre 56 → 154 entrées toutes pourvues de leur `competency`, sur les vingt chapitres de `math` 9ᵉ. C11 et F10 restent faites. 🔜 **Le point dur redevient l'APPLICATION** : les tags sont sur `main` et n'atteignent aucun élève — un dispatch les allume. **C3 toujours à 4/5**. Toujours rien sur : **vidéos 9ᵉ** (C2). **Prochaine ligne : C4ter** (`french-6eme`, classe de concours) |
| Fondations | Domaine câblé + monitoring + sitemap (F4) · légal F5 · triage ops F6 en route · `main` verte (§1)                                                                                                              | **`main` verte ✅**, **F4 soldée**, et **F10 réparée** le 2026-08-14 — la panne de douze jours est close. **F5 bouge à moitié** : la **suppression de compte est livrée** (arena#791), **l'export/portabilité reste à zéro occurrence** — c'est désormais le seul volet code de GAP-024, et il tient encore la Porte 1 avec l'INPDP (côté humain ; é29 §3.8 y ajoute son registre de traitement). **F6** : plus aucun blocage technique, une seule issue de triage ouverte (arena#673) — le geste opérateur manque toujours. **F7** : deux majeures (arena#660 TypeScript v7 gate rouge, arena#595 `@types/node`). **Trois lignes neuves** : F11, F12, F13 — livrées, consignées, pas rouvertes |

## 8. Journal de la roadmap

| Date       | Événement                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2026-08-23 | **L'ÉTUDE 04 EST FINIE — et le lot qui la ferme a passé la moitié de son temps sur une promesse que l'étude avait faite trois fois sans jamais la tenir.** Les lignes **15** et **16** livrées ensemble (arena#818), phase A2 close, étude passée en `EtudeRealisé/`. **Ce que les deux lignes demandaient** : l'élève voit ses erreurs nommées, en langage d'élève, avec un geste (« S'entraîner », via le **même** `get_exercises_for_competency` que la correction riche — un seul chemin de remédiation) ; le parent les voit aussi, **sans doublonner** `chapterInsights.weaknesses` qui existait déjà — l'un dit « Fractions : 45 % », _où_ ça coince, l'autre « il additionne les dénominateurs », _quoi_ réviser, et seul le second se traite le soir même. La mise en garde de la ligne 16 (« mesurer avant d'écrire, sinon on livre deux fois le même écran ») a donc **servi** : elle avait raison de faire mesurer, et tort de supposer un doublon. **⭐ Ce qu'aucune des deux ne demandait, et qui était le vrai travail : R-2 cesse d'être recopié.** L'étude 04 promet en R-2 des « constantes **centralisées**, ajustables ». Elles ne l'ont jamais été : le triplet (3 occurrences, 2 séances, 30 jours) était écrit **à la main** dans `get_daily_plan` et dans `get_tutor_learner_context` (livré la veille par la ligne 18). La 15 en aurait fait une **troisième** copie, la 16 une **quatrième**. Un seuil pédagogique dupliqué quatre fois n'est pas « ajustable » : il est faux à trois endroits le jour où on l'ajuste. `misconception_active_thresholds()` et `active_misconceptions()` portent désormais la définition, les deux appelants vivants sont rebranchés **dans la même migration**, et le triplet n'existe plus qu'à un seul endroit. **La leçon de méthode, elle, n'est pas sur R-2** : une exigence peut être écrite, relue, citée dans quatre lots et **jamais vérifiée**, parce que rien ne la teste — les surfaces marchaient toutes. Ce qui l'a révélée n'est pas un gate, c'est d'avoir voulu en écrire la quatrième copie. **⚠️⚠️ ET LE PLUS COÛTEUX A FAILLI PASSER : `get_daily_plan` retapée sortait un algorithme ENTIÈREMENT RÉINVENTÉ.** Il fallait y insérer un CTE ; je l'ai d'abord **retapée**. Le `diff` contre sa révision vivante a montré : score normalisé perdu, `DISTINCT ON` anti-doublon perdu, exclusion des quiz du repli perdue — la bande focus du tableau de bord serait devenue une autre fonctionnalité, sans un seul test rouge. **Ce n'est pas un gate qui l'a attrapé, c'est le `diff`** ; la version livrée est une **substitution par script** sur le texte extrait, et `35_daily_plan.test.sql` — **inchangée, restée verte** — est la preuve de non-régression. La règle à retenir vaut au-delà de ce lot : **une fonction SQL vivante se substitue, elle ne se retape pas** — et sa dernière révision n'est pas dans la migration qui l'a créée, mais dans le dernier `CREATE OR REPLACE` de `main`, souvent sous un nom sans rapport. **Ce qui s'affiche aujourd'hui : rien, chez presque tout le monde — et c'est correct.** Une erreur n'est active qu'après 3 occurrences sur 2 séances, et seul `math` 9ᵉ est tagué — appliqué en prod **le matin même** par #222, qui a refermé le rang 1 de l'ordre pendant que ce lot s'écrivait, et dont la vérification mérite d'être relue ici : l'étape de contrôle d'`apply-content` compte les chapitres et les questions, **jamais les colonnes serveur-seul** — `distractor_tags` en fait partie, donc son vert n'aurait pas prouvé que les tags étaient arrivés. Les deux surfaces rendent alors **rien du tout** — délibérément pas d'encadré « aucune erreur détectée », qui se lirait comme un satisfecit sur un compte neuf alors qu'il ne dit que « on n'a pas encore assez joué ». Le « GO humain » que le plan de lots attendait (« ≥ 4 semaines de télémétrie ») portait sur les **données**, jamais sur le code : les écrans se remplissent seuls. **État de la file PRODUIT : 19 lignes sur 20.** Ne reste que la **19** (é11 lots 2 → 7) — plus aucune dépendance, seulement une cadence à régler sur les coûts observés. **La verticale « apprendre & maîtriser » n'a plus de dette adaptative : tout ce qui reste dans cette file est de l'IA.** Aussi au moteur, hors file : **arena#817** — les 18 assertions pgTAP du tuteur ne s'exécutaient **pas** (un `source` inventé faisait avorter le fichier avant sa première assertion, et le `throws_ok` à 4 arguments comparait le message au SQLSTATE) ; **arena#805**, troisième instance du sélecteur e2e de #733. ⚠️ **#817 mérite d'être lue avec #816** : la PR du lot 1 a mergé **par-dessus un pgTAP rouge**, parce que `pgTAP suite` **n'est pas un check requis** — les quatre requis étaient verts et l'auto-merge a tiré. Le lot d'aujourd'hui est donc parti en `wip/`, promu seulement une fois la suite vraiment verte (`Files=69, Tests=886`, +14 = les siennes). **Un gate non requis ne garde rien ; il informe qui va le lire.** |
| 2026-08-22 | **Les deux premières lignes de l'ordre sont livrées le même jour — et le lien entre elles n'est pas encore fait.** **C4bis étape 1** (#219) : 1 049 distracteurs tagués sur 2 454 (43 %), registre 56 → 154 entrées, sur les VINGT chapitres — le périmètre d'A11 (« 557 questions, 13 chapitres ») décrivait un corpus qui a grandi de sept chapitres depuis l'étape 0. Trois domaines entiers n'avaient AUCUN mot (probabilités, puissances, quadrilatères) et un quatrième un seul : ils sont arrivés après. **43 % est la part des distracteurs NOMMABLES**, pas un travail à moitié fait — 10 % sur les systèmes (des couples numériques faux), 75 % sur la valeur absolue (des règles mal appliquées). **é11 lot 1** (arena#816) le même jour : « Demander au Prof », avec le cache mutualisé que é29 lot 5 lui avait laissé — `AI_CURATED_MODELS` n'était référencé nulle part avant. ⚠️ **Ce qui manque est un GESTE, pas un chantier** : les tags sont mergés et pas appliqués, donc le tuteur explique sans nommer l'erreur, et les quatre lots é04/é07 restent inertes. C11 avait appris exactement ça il y a douze jours. ⚠️⚠️ **Et arena#816 a mergé avec `pgTAP suite` ROUGE** : ses 18 assertions avortaient sur une fixture (`source = 'authored'`, refusé par un CHECK), donc 0 test exécuté sur 18 planifiés. Les quatre checks REQUIS étaient verts, l'automerge a fait son travail — c'est le piège de 2026-07-31 (#689), à l'identique. `db:check-chain` était vert lui aussi, et il avait raison : il rejoue la CHAÎNE, il n'exécute pas les contraintes d'un INSERT. Correctif arena#817, poussé sur une branche `wip/` À DESSEIN pour qu'il ne merge pas avant que la suite soit vraiment verte. |
| 2026-08-22 | **Les DEUX premières lignes de cette roadmap étaient déjà faites quand elles y sont arrivées — et 60 PR moteur sont entrées « connues » sans être citées.** Resynchronisation contre les deux dépôts, base #746 → #807. **(1) La base a sauté de 61 PR d'un coup** : la citation de é29 (#216) a porté le pointeur à #807, déclarant connues les 60 PR intermédiaires (#747 → #810) sans en citer une. Le gate est resté vert — aucune ne porte la forme « étude/lot ». Même angle mort que le 2026-08-10, dans l'autre sens : là c'était le dépôt privé qu'il ne regarde pas, ici c'est le pointeur qui a sauté par-dessus. **(2) C11 et F10, les deux priorités proclamées, sont tombées sans qu'aucune session ne les prenne.** #124 close le **2026-08-10 à 17 h 46** — le jour même de la rédaction de C11, **six jours avant** que la ligne n'atteigne `main` (#152/#184, restées en draft). #81 close le **2026-08-14**, deux jours avant l'arrivée de F10. **La leçon est neuve et elle est simple : une priorité écrite le jour J et mergée à J+6 n'est pas une priorité, c'est un instantané périmé. Relire l'issue avant de prendre la ligne.** **(3) F5 était fausse à moitié** : arena#791 a livré la suppression de compte le 2026-08-19, sous un titre qui ne cite pas GAP-024 — le symétrique du piège que cette même ligne documentait (« une PR qui cite un GAP ne le clôt pas » ⟶ « un GAP qu'aucune PR ne cite peut être livré »). **(4) Quatre chantiers entiers n'avaient aucune ligne** : suivi parental quotidien (**F11**, 15 PR), programme officiel devenu structure du produit (**F12**), manuels déclarés et liés (**F13**), campagne فقه (**C12**, 37 أبواب sur 45, rubrique ouverte). **(5) Le point dur change encore, et il change de nature** : c'est **C4bis**, qui ne commande plus seulement l'axe adaptatif mais aussi **l'étage IA** — la ligne 18 promet une explication ancrée sur un tag qui n'existe nulle part (0 occurrence sur 719 chapitres). **(6) Côté IA, le prérequis d'exploitation est levé** : `AI_KEY_ENC_KEY` est posée en production (Mohamed, 2026-08-22) ; é29 est déployée (`/api/health` → `548a429`). Restent le pilote Q-9 — **aucune clé de fournisseur n'a jamais été branchée** — et é11 lots 1-7. **(7) Une garde de plus dans la série des muettes** : la sonde des manuels ne tournait pas sous Windows et **refermait son issue en affirmant que tout allait bien** (arena#785, #211/#212) — quatrième cas, consigné en **F10**. |
| 2026-08-16 | **Cette correction est restée SIX JOURS en draft, verte, à un rebase du merge — et le gate `roadmap-sync` rougissait sur `main` depuis trois nuits sans que personne ne le voie.** La PR #152 (rédigée le 08-10) portait A17 et la réécriture de C11 ; elle a été ouverte **en draft**, jamais promue, puis `main` a avancé de 31 commits et elle est passée en conflit. Deux gardes distinctes ont donc échoué au même endroit — **la sortie**. (1) **La chaîne d'automerge d'ici était événementielle** : elle n'évaluait une PR qu'à l'instant où un workflow de PR finissait, une fois, sans reprise — donc une PR promue après ce coup d'œil, ou un merge perdant une course, n'était **plus jamais relu**. Deux PR vertes en sont restées ouvertes deux jours (#167, #162) ; corrigé par **#182**, qui rebalaye l'état complet à chaque déclenchement (**l'événement dit quand regarder, jamais quoi**). (2) **`roadmap-sync` échouait sur `main`** les 08-14, 08-15 et 08-16 : trois lots moteur n'étaient cités nulle part — **arena#726** (é28 lot 3) et surtout **arena#743 · arena#746**, qui font passer **l'étude 02 en exécution** (schéma + moteur SQL, puis l'écran de l'examen blanc). Le §6 dit toujours « é02 se re-scope maintenant » : quatre lots plus tard, c'est faux. Cités au **§0bis**, base portée à **#746**. **La leçon commune aux deux** : un cron qui rougit n'atteint personne, exactement comme les trois gardes muettes du 2026-08-10 ci-dessous. Ce qui manque n'est toujours pas la garde — c'est que **sa panne arrive à quelqu'un**. |
| 2026-08-10 | **Correction — la cause n'était pas l'écart de Node, et le correctif n'était pas le mien.** L'entrée suivante (même jour) affirme que la panne `npm ci` venait de ce que les six workflows d'ici étaient restés à Node 22 pendant que le moteur passait à 24, et que leur alignement l'a réparée. **Les deux sont faux.** La cause est **arena#716** : une PR intitulée « bump undici · dependency-type: **indirect** » qui modifiait en réalité `package.json` et faisait passer `@cloudflare/vite-plugin` de `^1.40.2` à `^1.51.1`, entraînant **miniflare 4 → 5 alpha**, workerd et wrangler — un saut de **majeure** et une **alpha** dans la chaîne de build, sous un intitulé de bump indirect, soit exactement ce que la politique de montée de version refuse. Le correctif est **arena#718**, qui la **revert** : resynchroniser le lockfile (`npm install --package-lock-only`) suffisait à reverdir `npm ci` — essayé, ça marche — mais gardait l'alpha et la majeure que personne n'avait arbitrées. **Ce que l'écart de Node explique vraiment est l'INVERSE d'une cause** : npm 11 (Node 24) acceptait ce lockfile, npm 10 (Node 22) le refusait — donc la CI du moteur était **verte** sur #716 et **la Content CI d'ici a été le seul détecteur du système**. Elle n'a pas échoué par mauvaise configuration : elle a échoué **parce qu'elle avait raison**. **Conséquence assumée, et c'est le vrai enseignement** : en alignant les six workflows sur Node 24, la PR #150 **a supprimé ce détecteur**. L'alignement se défend pour lui-même — le `.nvmrc` du moteur dit 24, et exécuter ses scripts sur un Node qu'il n'utilise pas est un risque — mais il a été **présenté comme un correctif qu'il n'était pas**, et son coût n'était écrit nulle part. La propriété perdue était de toute façon **accidentelle** (la sévérité de npm 10, pas une intention) : s'y fier était fragile, et c'est pourquoi la question posée en **A17** n'est pas seulement « 22 ou 24 » mais **quelle garde refuse une PR de dépendance dont le diff dépasse ce que son titre annonce**. **Méthode, pour la prochaine fois** : le premier diagnostic tenait parce qu'il expliquait le symptôme observé (deux CI, deux verdicts) — il n'a pas été confronté à la question « et si l'autre côté avait simplement tort ? ». Un écart entre deux environnements désigne rarement le plus strict comme fautif. |
| 2026-08-10 | **Resynchronisation contre les DEUX dépôts (#709 → #716 au moteur, #116 → #148 ici) — 37 PR n'étaient citées nulle part, et le gate était vert.** C'est le constat de méthode de la passe : `roadmap-sync` ne lit que les sujets de commit du **moteur** en forme « étude/lot ». Les sept jours écoulés se sont joués **au privé**, sur du contenu et de la transcription — deux catégories qu'il ne regarde pas et qu'il n'a jamais prétendu regarder. **Un gate vert veut dire « rien de ce que je sais lire ne manque », jamais « la roadmap est à jour »** ; l'écrire ici parce qu'une session qui voit le vert conclut l'inverse. **Deux chantiers ouverts n'avaient AUCUNE ligne**, alors que leurs deux issues étaient ouvertes, étiquetées et visibles : **C11** — #124, `content-drift`, **18 sujets mergés jamais publiés**, dont `english-3eme-sec` ×6, `english-bac` ×6 et `french-bac` ×5, soit **la campagne lycée en entier**, à J-22 — et **F10** — #81, le **garde pédagogique en panne depuis le 2026-07-29**, quatre runs échoués (07-29, 08-01, 08-05, 08-08), donc **toute cette campagne écrite sans filet**. Les deux se referment seules une fois le geste fait ; aucune ne s'est refermée, faute de geste. **Quatre lignes décrivaient un état faux** : **C4bis** (son étape 0 est faite — #118, registre de **5 à 56 entrées, toutes avec `competency`** ; une session l'aurait refaite), **C3** (**4 matières sur 5 en prod** au 2026-08-04, seul l'arabe manque et c'est un blocage de **transcription**, pas de génération — arena#714 ; la 1ère sec compte **6 matières en ligne**), **C9** (une campagne lycée entière livrée : #126 → #144, plus les correctifs d'audit #146/#147/#148), **F5** (« reste, et c'est humain » — faux : la suppression de compte et l'export **n'existent pas dans `src/`**, re-vérifié ce jour ; c'est le seul bloqueur légal qu'un agent peut lever, et le classer humain l'a gelé une semaine). **Priorité inter-files ré-arbitrée au §0** : **C11 → F10 → C4bis**. C11 d'abord parce que c'est le seul geste qui **ne produit rien et livre tout**. **Aussi au moteur, non repris ailleurs** : le topo resynchronisé deux fois (arena#710, #714) · l'admin rebondi hors du Hall, chaque « Retour au hall » le ramenant sur Suivi (arena#711) · le tableau de cours qui se coupait en deux et dont les colonnes arabes se lisaient à l'envers (arena#712), puis son en-tête qui n'en était pas un pour un lecteur d'écran (arena#713) · un secret malformé qui annonçait le nom d'une librairie à la place du sien (arena#715) · le bump `undici` (arena#716). **Et ici** : le doublon de gabarit, défaut n°1 de l'écriture parallèle, qui n'était écrit nulle part (#121) · la clôture de session du 2026-08-03 (#122) · la garde `content-drift` consignée là où on la cherchera (#125) — consignée, et pourtant non prise pendant six jours : **documenter une garde ne la fait pas exécuter**. **ENFIN, TROUVÉ EN VÉRIFIANT CETTE PR — la CI de contenu de ce dépôt était MORTE, et le geste de C11 avec elle.** La PR de resynchronisation a fait rougir `content-ci` sur `npm ci`, pas sur son diff : `Missing: typescript@5.9.3 from lock file`. Reproduit en local, bissecté à **arena#716** (bump `undici` par Dependabot, qui a supprimé au passage l'entrée imbriquée `vite-tsconfig-paths/node_modules/typescript` que le peer `tsconfck ^5.0.0` réclame). **Mais #716 était VERTE au moteur** — et c'est là que se trouve la vraie cause : le moteur tourne sur **Node 24 depuis arena#688** (`.nvmrc` + ses 11 workflows), tandis que **les six workflows d'ici qui le checkoutent étaient restés à Node 22**. Même arbre, deux npm majeurs, deux verdicts : npm 11 accepte ce lockfile, npm 10 le refuse. **Portée réelle de la panne** : `content-ci` (toute PR de contenu), `content-audit`, `video-health`, `apply-content-test` et surtout **`apply-content`** — donc **la publication des 18 sujets de C11 était impossible** au moment même où cette PR la déclarait « un dispatch ». Corrigé ici : les six passent à Node 24. **La leçon est la même que celle de toute la passe, sous un troisième costume : un gate ne voit qu'un dépôt.** Le moteur a bumpé Node chez lui, complètement et correctement de son point de vue ; les workflows d'ici, qui exécutent ses scripts, lui sont invisibles. **POST-SCRIPTUM — `main` a avancé pendant la rédaction de cette entrée, ce qui est sa meilleure illustration** : **#145** (`english-bac` ch.04-06, la tranche 2) et **#149** ont mergé pendant la session, portant la base à `77a7736`. Les deux sont inscrites (C9 pour la première, F10 pour la seconde). **#149 mérite mieux qu'une citation** : `video-health.yml` avait été exécuté **trois fois** depuis son portage et avait échoué les trois fois au même endroit — un **troisième** garde qui n'avait jamais rendu de verdict, après les deux pannes du garde pédagogique. Sa sonde marchait ; c'est l'étape `gh` d'après qui tombait, faute de `GH_REPO` dans un workspace dont la racine n'est pas un dépôt git. Et l'étape qui **ouvre** l'issue portait le même défaut sans jamais s'exécuter, gardée par `broken != '0'` : elle aurait cassé le jour du premier vrai incident. F10 cesse donc de décrire un incident et décrit une **série** — trois gardes, trois pannes muettes : ce qui manque n'est jamais la garde, c'est que **sa panne n'atteint personne**. ⚠️⚠️ **DEUX AFFIRMATIONS DE CETTE ENTRÉE SONT FAUSSES** — la cause de la panne `npm ci` et l'identité de son correctif. Elles ne sont pas réécrites ici (ce journal ne se réécrit pas) : la correction est l'entrée **« Correction — la cause n'était pas l'écart de Node »** du 2026-08-10, ci-dessus. |
| 2026-08-03 | **Le désarmement du canal de contenu avait un angle mort : rien ne disait qu'un merge n'était pas publié — et 23 sujets l'étaient depuis des jours.** Point de départ : un audit du ch.19 de `math-bac-math` relevait quatre paires de questions clonées entre `06-histoire-statistiques` et `07-annales-bac` (mêmes gabarits, mêmes triplets de distracteurs) — réécrites sur place, sans réordonner ni changer une lettre de clé (#104). **Mais la PR a révélé pire que son objet** : appliquée à 19:11 le 2026-08-01 depuis `891c864`, elle a été mergée à 19:27 en `67e3dd7` — **seize minutes**, deux jours de contenu périmé servi en prod, et rien pour le dire. `apply-content.yml` est désarmé (lot 3a) : aucun merge ne publie, et ni la CI verte, ni l'automerge, ni `content_releases` — qui ne sait que ce qui a été appliqué, jamais ce qui manque — ne signalent le geste absent. **Livré : `content-drift.yml`** (#112, corrigée par #116), garde en **lecture seule** qui compare `content_releases` à `main` et tient **une** issue `content-drift` ouverte tant qu'un sujet est en retard, refermée d'elle-même — mécanique de `video-health.yml`. Pas de run rouge : une issue ouverte survit à l'onglet Actions. **Son premier passage a trouvé 23 sujets**, dont `0e17aab` (« les explications citent la valeur de l'option, pas sa lettre »), correctif transverse mergé le 29 juillet, jamais publié sur une dizaine de matières — le stock que la ligne précédente signalait est donc **soldé** : corpus complet appliqué (run 30819985947, 49 min, backup + vérification en base verts), puis `chimie-1ere-sec`, mergé *pendant* cette application, soit exactement la course d'origine. Cycle complet exercé en prod : ouverture (23) → mises à jour (23 → 2 → 1) → **clôture automatique** (0). **Le piège pour la suite** : le nom du dossier de `content/` n'est pas l'identifiant en base — `compileTo` fait compiler un dossier vers plusieurs sujets, et la v1 de la garde criait « jamais publié » sur un dossier fraîchement appliqué, faux positif **éternel** qui l'aurait fait ignorer en quelques semaines (#116). **Ce qui n'est PAS fait, délibérément** : armer le déclencheur automatique. Ça reste le **lot 3b** d'é24 (répétition sur TEST + arbitrage §4.3) — une garde ne re-designe pas le canal qu'elle surveille. Le risque résiduel est donc entier : entre un merge et le passage suivant de la garde, la prod est en retard sans que personne ne le sache. C'est ce risque-là, pas la visibilité, que 3b supprimerait. |
| 2026-08-03 | **Resynchronisation contre `main` (base #702 → #709) — et deux motifs périmés retirés.** Trois lots livrés les 2026-08-02/03 manquaient : **arena#707** (le geste « m'entraîner », qui **ferme la ligne 9** — ce fichier la donnait encore ouverte, donc une session « première ligne non cochée » aurait réimplémenté du code déjà sur `main`), **arena#708** (é09 lot 2, le simulateur) et **arena#706** (le canonique SEO tranché : `SITE_URL` passe à `www`, balise `rel=canonical` posée sur toute la coquille publique — les 1 541 URL du sitemap pointaient vers une redirection). **Deux arbitrages NEUFS, A15/A16 au §2** : le simulateur casse G-1 et G-4 dès son premier run, ce qui est son métier — A9 les avait ratifiés comme hypothèses de départ, les corriger est le protocole, pas un revirement. Le lot rend aussi trois corrections de fond, dont **le lot 1 encodait une règle de demi-coins qui n'existe pas dans le moteur** — donc la prémisse de D-5 tombe et le flux de coins se **calcule** au lieu d'être estimé. **Deux motifs de report réfutés** : F6 justifiait l'inaction du triage par arena#638, **close depuis le 2026-07-27** (l'e2e n'a jamais écrit en prod ; la vraie panne était l'inverse — la boucle de triage était aveugle à la prod pendant dix jours) ; F7 citait encore #593, remplacée par #660, et « Node 26 » là où la CI est à **Node 24**. **Q-5 d'é04** était donnée « à trancher » alors qu'A10 l'a tranchée. **Constat contenu ajouté à C10** : un stock généré depuis le 2026-07-29 (`education-islamique-5eme`, `math-bac-math`, `arabic-6eme`, `arabic-2eme-sec-lettres`) attend son application — et le parcours 5ᵉ étant ouvert depuis juin, l'islamique ne demande aucune PR moteur. **Rien n'a bougé sur la file PRODUIT au-delà de la 9** : la prochaine ligne prenable reste **C4bis**, pas la 15. |
| 2026-07-20 | Création (déclinaison de l'étude 26, état consolidé post #525/#526/#527/#529/#531)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 2026-07-20 | **Session d'arbitrages — A1→A5 tous rendus** (Mohamed). é26, é19, é21, é11 → `validée` ; les 4 écarts de é24 tranchés (lot 3b débloqué) ; é23 resynchronisée en `en exécution`. **Corrections d'état** : A6 sans objet (PRs legacy mergées les 12-13/07), `main` — CI requise verte, `Nightly`/`E2E auth` rouges. Le tuteur IA est renommé **« El Ostedh »**. La roadmap devient officielle (A1-Q1).                                                                                                                                                                                                                                                                                                                                                                                                                |
| 2026-07-25 | **Ligne 8 livrée — amendement é04-A1.2 écrit** (`04-moteur-adaptatif/ETUDE.md` §9). Contrat fermé en deux lots (A1.2a serveur / A1.2b client). Il corrige deux suppositions du mandat : l'explication post-erreur n'était **pas** monnayée (c'est l'indice avant réponse qui l'est), et le feedback question-par-question rouvre la couture de soumission atomique — sorti du périmètre, posé en **Q-4**. Le lot sera **inerte tant que le corpus n'est pas tagué** (C4), assumé. La prochaine ligne PRODUIT devient la **9**.                                                                                                                                                                                                                                                                                      |
| 2026-07-25 | **Resynchronisation contre `main` — 24 lots livrés manquaient.** La règle « cocher dans la même PR » était inapplicable depuis la scission (é24) : deux dépôts, aucune PR commune. Elle est remplacée par un invariant vérifié (§0) — chaque ligne cochée cite sa PR, et le gate `check-roadmap-sync.mjs` échoue si un lot livré n'est cité nulle part. **§1 « reverdir `main` » est clos** (nightly vert 5 nuits, e2e-auth vert, #250/#363 closes) et sa mise en garde pgTAP est périmée (#563). **F8 ajoutée** : l'étude « IA vs déterministe », 6 lots, close — elle avait tourné entièrement hors roadmap. **A8** consigné (script maison plutôt que Renovate). **F7 nettoyée** (issues majors doublonnées, #234 périmé). **C4 remontée en priorité** : trois lots produit livrés sont inertes sans le tagging. |
| 2026-07-27 | **Resynchronisation contre `main` (base #536 → #641).** Le gate `check-roadmap-sync.mjs` était **vert** — il ne voit que les sujets de commit en forme « étude/lot », et rien de ce qui a été livré les 26-27/07 n'en portait la forme : la dérive de ces deux jours est un **angle mort assumé** du gate, pas une panne. Corrigé ici à la main. **Fondations** : F4 **cochée** — le go-live infra est soldé, et il l'était en partie **depuis des semaines sans trace dans le repo** (GA4 tournait, le DSN Sentry était posé) ; F7 **nettoyée** (major Supabase livré par arena#622, restent #595 et #593) ; F8 **refermée** par son volet contenu (5 lots `LC0…LC4` le 2026-07-25) ; **F9 ajoutée** pour l'outillage de campagne, livré entièrement hors roadmap. **Contenu** : **C10 ajoutée** — une campagne petites classes (`french-4eme`, `french-5eme`, `arabic-6eme`, fiche 6ᵉ base) tournait depuis le 26/07 **sans aucune ligne ici** ; C6 entamée (33 figures). **F6** : la file de triage est passée de 14 à 3 issues, mais les 3 sont des **artefacts** d'arena#638 (un e2e écrit en prod chaque nuit) — le geste opérateur reste vain tant que le bug vit. **Aucune ligne PRODUIT n'a bougé** : la prochaine reste la **9**. |
| 2026-07-27 | **Étude 20 — deux lots livrés (2 et 7), et la file C5 s'arrête là où l'IA commence.** **Lot 2** (Tier A, arena#652) : l'expansion morphologique est une fonction PURE appliquée au build, pas des variantes gravées dans le corpus — 13 017 des 13 049 questions éligibles au Rappel gagnent une forme acceptée, 42 refusées par R-4, gisement « article » arabe couvert à 1 849/1 851. **Lot 7** (type natif `short_answer`, arena#654, = ligne PRODUIT 11) : sixième type dans le cadre fermé de l'étude 03, sans colonne ni écran ni grant nouveau ; l'appariement des erreurs, dupliqué entre les deux RPCs de soumission, devient une fonction unique. **Les lots 3 et 4 (Tier B) sont mis en attente par Mohamed** : ils reposent sur de la génération IA — hors ligne et relue, jamais au runtime (R-7), mais génération quand même. Restent donc exécutables sans IA : lot 5 (saisie arabe) et lot 6 (refus contesté). Le lot 8 attend en plus une décision de doctrine (R-14). |
| 2026-07-29 | **Le canal de contenu a tourné pour de vrai — pour la première fois depuis la scission.** Le secret `PROD_SUPABASE_DB_URL` du privé repointé sur le pooler (Mohamed), deux applications passées et **vérifiées en base** : `french-4eme`/`french-5eme`/`arabic-6eme`, puis `math`/`math-6eme` — donc les **1 362 questions taggées** sont en prod, et les trois lots é07 livrés le 20/07 reçoivent enfin des données. Backup `pg_dump` avant chaque écriture, releases journalisées. **Ce qui a rendu la panne trouvable la prochaine fois** (#71/#72/#73) : l'URL IPv6 est refusée d'emblée en nommant la cause, le mauvais port et le tenant manquant sont attrapés, et une étape « vérifier que le contenu est bien en base » **échoue si un sujet revient vide** — elle transforme « le SQL est passé » en « le contenu est là », la distinction exacte qui manquait. Audit préalable au risque de prune : prod avait déjà été convergée vers les mêmes UUIDv5 le 2026-06-02 par les 231 migrations générées d'avant la scission, donc appliquer `math` était une convergence ordinaire, pas une purge. |
| 2026-08-01 | **Session de clôture — les quatre arbitrages du 2026-07-31 sont livrés, et deux canaux ont été réparés en s'en servant.** Livré : les deux compétences manquantes du registre (#90, 16 questions re-taguées, **appliquées en prod** avec le registre à 59) · l'alarme de gel `freeze-watch` (arena#696) — le gel reste DISCIPLINAIRE et non opposable, parce que la panne réelle a été un gel **invisible**, pas un gel contourné · les pages légales (arena#701, GAP-024) · le **lot 3 de l'étude 20** (#96, skill Tier B + pilote sur la mission constatée). **Deux réparations de canal, trouvées en l'utilisant** : `apply-content.yml` n'émettait **jamais** le registre de compétences (#92 — `--competences` est un mode « registre seul », l'appel se faisait sans lui), puis la vérification post-application comptait ce registre **comme un sujet** et le déclarait « appliqué sans effet » (#98, régression de #92 : le contenu était bien en base, mais la release n'était pas journalisée). Même famille que les précédentes : un canal écrit, jamais exercé, qui échoue sans bruit. **Dette remontée par le pilote** : Tier A préfixe « ال » sans condition et produit « الفوقها » — inoffensif au scoring, candidat à un lot moteur. |
| 2026-07-27 | **C4 cochée — le tagging de compétences vague 1 est fait** (1 362 questions : `math` 557/557, `math-6eme` 805/805, 10 PRs #51→#61). Les trois lots produit livrés depuis le 2026-07-20 mais **inertes faute de corpus tagué** ne le sont plus. Le lot rend deux constats à l'humain : les **57 compétences du registre sont toutes mobilisées** (le calibrage Q-1 est vérifié par l'usage, pas seulement par construction — c'est ce qui manquait à la validation de l'échantillon), et **deux compétences manquent** au registre (`num.valeur-absolue`, `stat.mode` — 18 questions rabattues sur une compétence voisine). **Découverte du même jour, et c'est le nouveau point dur** : `apply-content.yml` **n'a jamais appliqué de contenu en prod** — son unique run réel a échoué au backup, l'URL du secret `PROD_SUPABASE_DB_URL` d'ici étant la connexion directe Supabase, IPv6-only, injoignable depuis les runners GitHub (#52). Rien de ce qui a été produit depuis la scission n'est donc en prod. La prod est intacte : le fail-closed a joué avant toute écriture. |
| 2026-07-31 | **Ligne 9 à moitié livrée — é04 lot A1.2a (serveur) est sur `main`** (arena#689, correctif de test arena#691). `get_attempt_review` rend `misconception_tag` + `chapter_id` : la troisième boucle « collectée-jamais-surfacée » de l'étude 26 se referme côté serveur, le signal capté depuis la phase A0 cesse de n'alimenter que la télémétrie. Le stop-point D-A1.2-2 est tenu et **encodé en attaque** — trois assertions rejouent l'élimination par la map plutôt que le cas nominal. La ligne reste décochée : **A1.2b** (client) n'est pas fait. **Deux enseignements de process, qui valent au-delà de ce lot.** (1) `pgTAP suite` tourne sur les PR de migration mais **n'est pas requise** : #689 a mergé 3 minutes après son ouverture, sur les checks requis verts, avec un fichier de test rouge — la fenêtre de lecture d'un check non requis est plus courte que le temps de le lire. Sur une PR de migration, soit on rend le check requis, soit on ouvre en `wip/`. (2) La vérification locale du lot avait tourné sur des **shims pgTAP écrits pour l'occasion**, dont l'un implémentait `unlike()` — une fonction que pgTAP n'a jamais eue. Un harnais qui définit la fonction qu'il est censé valider ne valide rien : c'est la leçon d'arena#631/#635 (« une sonde ne vaut que si elle exécute le même code que le gate ») rejouée sous une autre forme. |
| 2026-07-31 | **Ligne 9 — les deux lots livrés (A1.2a arena#689/#691, A1.2b arena#695), et un constat qui vaut plus que le lot.** A1.2b a dû **corriger D-A1.2-3**, fondée sur une surface de compilation client qui n'existe pas : les libellés passent désormais par la base, par le canal des compétences (é07), sans rien perdre de l'intention (la fonction rend un ID, le registre reste source unique, une reformulation reste une correction de registre). **Le fait majeur** : mesuré ce jour, le corpus ne contient **aucun** tag de misconception — 0 occurrence sur ~18 700 questions, 0 `distractor_tags` non vide dans les migrations manuelles, les 5 tags du registre inutilisés. Donc `user_misconceptions` est **vide en prod** depuis l'origine, le terme « misconceptions » de `get_daily_plan` vaut zéro depuis #581, et **la ligne 15 (A2.1) livrerait un écran vide**. L'étude 26 décrivait une boucle « collectée-jamais-surfacée » : elle n'était **jamais alimentée**. Le blocage de tout l'axe est du **contenu** — taguer les distracteurs, comme C4 l'a fait pour les compétences (deux registres distincts : C4 n'a PAS tagué les misconceptions). **Reliquat de la ligne 9** : le geste « m'entraîner », suspendu à la décision « quel lien misconception → compétence ». |
| 2026-08-01 | **F3 — é09 lot 1 livré** (arena#703) : la console « Économie » mesure enfin ce que la courbe XP/coins produit en vrai. Vérifié en exécution réelle sur PostgreSQL 16, sur des scores choisis pour être contrôlables de tête (100 XP à 80 % → 20 coins, à 45 % → 10, à 30 % → 0 : le RPC rend 30.00). **Le lot 2 est bloqué par Q-1** — les garde-fous G-1…G-4 n'ont jamais été arbitrés, et les choisir en exécutant serait décider de l'équilibrage sous couvert d'outillage. **Constat de méthode qui dépasse é09** : le §2 affirme « plus aucun arbitrage humain n'est en attente ». C'est vrai des arbitrages A1→A8 ; ce n'est PAS vrai des questions internes des études restées en `brouillon`. Une session qui lit le §2 littéralement croit toute ligne exécutable de bout en bout — é09 montre que non. À vérifier étude par étude avant de prendre une ligne. |
| 2026-08-02 | **Session d'arbitrages — A9→A14 rendus** (Mohamed). Les questions internes des études 04 et 09 sont vidées, et trois décisions de fond tranchées. **Ce qui se débloque** : é09 lot 2 (le simulateur a enfin des seuils opposables, ratifiés comme **hypothèses de départ** — un seuil que le simulateur fait sauter au premier run a probablement tort lui-même, on ne retouche pas `gamification.ts` pour faire passer un test) · le geste « m'entraîner » de la ligne 9 (**un champ `competency` dans le registre des misconceptions**, qui réutilise le chemin d'é07 lot 4 au lieu d'en créer un second) · **C4bis**, le pilote de tagging des misconceptions sur `math` 9ᵉ — le déblocage de tout l'axe adaptatif, volontairement limité à une matière pour obtenir un coût réel par question avant d'engager une vague. **Deux décisions de posture** : `pgTAP suite` devient **requis** sur les PR de migration (#689 a mergé rouge en trois minutes : la fenêtre de lecture était plus courte que le temps de lire) · **pas** de garde-fou de volumétrie des registres, la purge étant déjà gardée là où le dégât se produit (arena#702). **Correction de lecture consignée au §2** : « arbitrage rendu » n'a jamais voulu dire « ligne exécutable » — il faut aussi lire le statut de l'étude. |
