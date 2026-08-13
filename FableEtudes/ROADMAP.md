# ROADMAP — ordre d'exécution du reste-à-faire (études, lots, contenu)

<!-- roadmap-sync: since-pr=716 -->

> **Instantané du 2026-08-10** (créé le 2026-07-20, resynchronisé contre `main` les 2026-07-25,
> 2026-07-27, 2026-07-29, 2026-08-01, 2026-08-03 puis le **2026-08-10**) — déclinaison opérationnelle de l'**étude 26 (doctrine verticale : profondeur
> avant largeur)**. Les Q-1…Q-5 de l'étude 26 ayant été **arbitrées le 2026-07-20**, cet ordre
> n'est plus une recommandation d'architecte : il est **officiel**. Les arbitrages **A1→A8**
> (2026-07-20) puis **A9→A14** (2026-08-02) sont rendus : cette seconde session a vidé les
> questions internes des études 04 et 09, et tranché le périmètre du tagging, le lien
> misconception → compétence et le statut du check pgTAP. L'état de référence reste
> [STATUS.md](../STATUS.md) + l'[index des études](./README.md).
> **Jalon produit : rentrée scolaire, 1ᵉʳ septembre 2026** (§7) — **J-22**.
>
> ⚠️ **Ce que la resynchronisation du 2026-08-10 a corrigé — et le fait qui commande la file
> aujourd'hui.** **37 PR livrées n'étaient citées nulle part** : 30 ici (#117 → #148) et 7 au
> moteur (arena#710 → #716). Le gate `roadmap-sync` était **vert** pendant tout ce temps, et il
> avait raison de l'être : il ne lit que les sujets de commit du **moteur** en forme
> « étude/lot » — or ces sept jours se sont joués **au privé**, où il ne regarde pas. Un gate vert
> n'a jamais voulu dire « la roadmap est à jour » ; il veut dire « rien de ce que je sais lire ne
> manque ».
>
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
   ⚠️ **Exception constatée au 2026-08-03, ré-arbitrée le 2026-08-10 — elle prime sur cet
   ordre.** L'ordre à prendre est **C11 → F10 → C4bis**, trois lignes hors file PRODUIT.
   La règle « PRODUIT d'abord » suppose que la file PRODUIT a une ligne prenable — or la 15
   livrerait un écran vide et la 9 est close.
   **C11 d'abord parce que c'est le seul geste qui ne produit rien et livre tout** : 18 sujets
   sont écrits, audités, mergés — et invisibles. À J-22, publier ce qui existe bat écrire ce qui
   n'existe pas, quelle que soit la file. **F10 ensuite** : le garde pédagogique est en panne
   depuis le 2026-07-29, donc tout ce qui s'écrit d'ici là s'écrit sans filet — le réparer avant
   la campagne suivante coûte un jeton, après coûte un audit. **C4bis en troisième**, inchangée
   sur le fond : elle reste la ligne qui **allume quatre lots déjà mergés**.
   L'ordre sert la valeur livrée ; il ne la remplace pas.

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
> **État au 2026-08-10 : 14 des 19 lignes livrées, inchangé depuis le 2026-08-03.** La ligne 9
> est CLOSE (arena#689, #691, #695, **#707**) — son reliquat, le geste « m'entraîner », est livré
> le 2026-08-03 sur l'arbitrage A12. Restent **15, 16** (é04 A2) et **17-19** (é11, hors file
> par A1). **Aucune ligne PRODUIT n'a bougé cette semaine** : les 37 PR de la période sont du
> contenu, de la transcription et des correctifs de moteur.
> ⚠️ **La 15 n'est PAS prenable telle quelle** : **le corpus ne porte toujours aucun tag de
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
- [ ] 15. **é04 lot A2.1 — « Points faibles »** (misconceptions en langage élève + « S'entraîner »).
      ⛔ **NE PAS PRENDRE AVANT C4bis** : `user_misconceptions` est vide en prod depuis l'origine
      (la chaîne est mécanique — voir ligne 9), donc ce lot **livrerait un écran vide**. Ce n'est
      pas une réserve de prudence, c'est arithmétique : l'écran n'a aucune ligne à afficher
- [ ] 16. **é04 lot A2.2 — rapport parent enrichi** (3 points faibles majeurs + tendance).
      Même dépendance de fond à C4bis pour les « points faibles » ; la **tendance**, elle, se
      calcule sur la télémétrie existante

**Étape E — l'étage IA (étude 11) — A5 rendu le 2026-07-20 : exécution dégelée pour les lots 0-2**

> ⚠️ **Tension à arbitrer par le calendrier, pas par une décision** : A5 dégèle é11, mais A1
> lui assigne le **rang 9** du pipeline V1. Les lots 0-1 ne seront donc à la rentrée que si une
> session s'y consacre **hors de la file PRODUIT** ; sinon la cible reste octobre (§7), sans
> impact sur la rentrée.

- [ ] 17. **é11 lot 0 — socle IA** (adaptateur unique, comptabilité `ai_usage_events`, quotas/énergie, kill-switch) — la **porte LLM unique** (é26 D-8)
- [ ] 18. **é11 lot 1 — explication personnalisée post-review** (la brique signature : ancrée sur l'item + distracteur + tag)
- [ ] 19. **é11 lots 2 → 7** dans l'ordre de l'étude (plan du jour · chat cadré · boucle de compréhension · exercices ciblés · bilans hebdo · énergie UI) — une PR par lot, cadence selon usage/coûts observés

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
- [ ] F5. **Légal avant rentrée.** ⚠️ **Cette entrée disait « GAP-024 livré » et « reste, et c'est
      humain » — les deux sont faux, corrigé le 2026-08-10.** **GAP-024 est à MOITIÉ fait**, et
      la moitié qui manque est **du code** : ni suppression de compte ni export/portabilité
      n'existent dans `src/` (`deleteAccount`, `export_user_data` : zéro occurrence, vérifié sur
      `main` au 2026-08-10). C'est **le seul bloqueur légal de la Porte 1 qu'un agent peut
      lever**, et le classer « humain » l'a gelé une semaine (constat déjà porté par STATUS §5 le
      2026-08-03 — cette roadmap ne l'avait pas repris, ce qui est exactement la dérive que le §0
      cherche à empêcher). **Rappel du piège qui a produit l'erreur : une PR qui cite un GAP dans
      son titre ne le clôt pas.**
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
      **Reste côté code, et c'est prenable dès maintenant** : le volet « droits des personnes »
      ci-dessus (suppression de compte + export). Une ligne de session à part entière, pas un
      reliquat.
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
- [ ] F10. **LE GARDE PÉDAGOGIQUE EST EN PANNE DEPUIS LE 2026-07-29 — ligne ouverte le
      2026-08-10, deuxième priorité de toutes files.** L'issue **#81** est ouverte depuis douze
      jours et **quatre runs consécutifs ont échoué** : 07-29, 08-01, **08-05**, **08-08**.
      Cause connue et écrite dans l'issue elle-même : le secret `CLAUDE_CODE_OAUTH_TOKEN` est
      invalide ou expiré (`API Error: Header 'Authorization' has invalid value`) — le geste est
      `claude setup-token` puis remise en secret du dépôt. L'issue se referme seule au premier
      run vert.
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

## 5. FIL CONTENU (parallèle — sessions de campagne dédiées)

> Règle é26 D-6 : la largeur _catalogue_ continue sous sa propre barre de qualité (é18 axe 5,
> gates, audits). **A1-Q2 rendu** : la cible de couverture pour la rentrée est le **statu quo
> consolidé à la barre é18** — aucune nouvelle classe « vitrine » sous cette barre.

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
- [ ] C4bis. **Tagging des MISCONCEPTIONS — pilote `math` 9ᵉ** _(A11 rendu le 2026-08-02)_.
      🟠 **ÉTAPE 0 FAITE le 2026-08-04 (#118), ÉTAPE 1 À PRENDRE** — troisième ligne de la
      roadmap au 2026-08-10 (derrière C11 et F10), et toujours la seule qui **allume du code déjà
      livré**.
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
- [ ] C11. **PUBLIER CE QUI EST DÉJÀ MERGÉ — 18 sujets en retard sur la prod.**
      🔴 **PREMIÈRE LIGNE DE TOUTE LA ROADMAP au 2026-08-10**, toutes files confondues, et la
      seule qui **ne produit rien** : tout est écrit, audité, mergé. Ligne ouverte ce jour ;
      l'écart, lui, est mesuré et **visible depuis le 2026-08-04** — personne ne l'a pris.
      **Le fait** : l'issue **#124** (`content-drift`, ouverte le 2026-08-04, régénérée le
      2026-08-06) liste **18 sujets** dont `main` porte du contenu que la production n'a pas.
      Le détail est plus dur que le nombre — **la campagne lycée anglais/français n'a jamais
      atteint un élève, pas un chapitre** : `english-3eme-sec` ×6 sections, `english-bac` ×6,
      `french-bac` ×5, tous **« jamais publié · tout le sujet »**, plus le correctif
      `education-islamique-5eme` (#123). C'est **C9 en entier** — dix jours d'écriture et cinq
      correctifs d'audit — invisible, **à J-22 de la rentrée**.
      **Le geste, et il tient en une ligne** : Actions → *Apply content (PROD)* → `dry_run: false`,
      **`subjects` laissé vide** (applique tout le corpus : idempotent, journalisé dans
      `content_releases`, et c'est le geste le plus sûr quand plusieurs sujets sont en retard).
      L'issue se referme **d'elle-même** au passage suivant de la garde. C'est un des dispatches
      **explicitement autorisés** à un agent par la politique d'exécution — il ne publie rien de
      neuf, seulement le SQL compilé d'un corpus déjà mergé et validé.
      🚨 **PRÉREQUIS DÉCOUVERT EN ÉCRIVANT CETTE LIGNE — le dispatch était INEXÉCUTABLE.**
      `apply-content.yml` fait `npm ci` sur le moteur, et **ce `npm ci` échouait** :
      `Missing: typescript@5.9.3 from lock file`. Cause : **arena#688 a monté le moteur à Node 24**
      (`.nvmrc` + ses 11 workflows) le 2026-08-03, mais les **six workflows de CE dépôt qui
      checkoutent le moteur** sont restés à **Node 22** — et aucun gate ne traverse les deux
      dépôts pour le voir. Tant que l'écart tenait, npm 10 refusait un lockfile régénéré sous
      npm 11 (arena#716, le bump `undici`, qui a supprimé au passage l'entrée imbriquée
      `vite-tsconfig-paths/node_modules/typescript` dont le peer `tsconfck ^5.0.0` a besoin).
      **Corrigé dans la même PR que cette ligne** : les six workflows passent à Node 24.
      ⚠️ **À retenir, parce que ça se reproduira** : le moteur a bumpé sa version de Node **dans
      son dépôt**, ce qui est correct et complet **de son point de vue** — les workflows d'ici qui
      exécutent ses scripts sont invisibles à sa CI. C'est le **même angle mort** que celui qui
      tenait la roadmap périmée : un gate ne voit qu'un dépôt.
      ⚠️ **Le piège de lecture qui a laissé passer dix jours** : `apply-content.yml` est désarmé
      **volontairement** (é24 lot 3a). Ni la CI verte, ni l'automerge, ni `content_releases` — qui
      ne sait que ce qui a été appliqué, jamais ce qui manque — ne signalent le geste absent. La
      garde #124 est précisément ce qui rend l'écart **visible** ; elle ne le **referme** pas, et
      une issue ouverte qu'on croise sans la prendre coûte autant qu'une garde en panne (**F10**).
      **Ce qui supprimerait le risque à la racine reste le lot 3b d'é24** (répétition sur TEST +
      arbitrage §4.3) — armer le déclencheur. Une garde ne re-designe pas le canal qu'elle
      surveille : entre un merge et le passage suivant, la prod est en retard sans que personne ne
      le sache.

## 6. FILES DIFFÉRÉES (ne rien lancer avant leur porte d'entrée)

| File                                                             | Porte d'entrée                                                      | Contenu                                                                           |
| ---------------------------------------------------------------- | ------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| **V2 — concours**                                                | V1 ≥ M3 (étapes 1-16) **et** annales transcrites (`NN-annales-bac`) | é02 re-scopée (« examen blanc » sans wording premium), percentiles                |
| **V4 — parent**                                                  | é04-A2.2 livré (ligne 16)                                           | é08 re-scopée + digest hebdo IA (é11 lot 6 la sert aussi)                         |
| **Gels — actés (A1-Q3, 2026-07-20)** ; application par é26 lot 2 | Dégel par décision humaine explicite uniquement                     | é06 (PWA offline) · é10 (anti-fraude — se dégèle au volume) · é12 (studio in-app) |
| **Gelée (phase)**                                                | Sortie de la phase gratuite (décision humaine)                      | é01 (paiement en ligne — véhicule de réactivation du premium)                     |

## 7. Vue jalon — ce qui doit être vrai le 1ᵉʳ septembre 2026

| Axe        | Cible rentrée                                                                                                                                                                                                  | État au **2026-08-10 (J-22)**                                                                                                              |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| Produit    | File V1 étapes **1-16** livrées (é22 complet dont bannière rentrée · Révision du jour · correction riche · Rappel tolérant lot 1 · maîtrise visible · points faibles + rapport parent)                         | **14/19 lignes faites — inchangé depuis le 2026-08-03** (11/19 au 2026-07-27). Restent **15-16** (é04 A2) et 17-19 (é11, hors file). ⛔ **La 15 est bloquée par C4bis, pas par du code** : elle livrerait un écran vide. La semaine écoulée a été **entièrement contenu + transcription** — ce n'est pas une dérive, c'est C9 qui a tourné |
| IA         | A5 **rendu le 2026-07-20** : é11 dégelée (lots 0-2, pilote math 9ᵉ, budget 5 $/j, tuteur « El Ostedh »). Lots 0-1 à la rentrée **seulement si une session les prend hors file V1** — sinon octobre             | non commencé — conforme au plan. À J-22, la cible **octobre** est désormais l'hypothèse par défaut, pas le repli                          |
| Contenu    | Classes existantes à la barre é18 · 1ère sec complète (5 matières) · vidéos 9ᵉ · Tier A `acceptedAnswers` corpus entier · cible arbitrée (A1-Q2) = **statu quo consolidé à la barre é18**, sans classe vitrine | 🔴 **Le point dur n'est plus C4bis : c'est la PUBLICATION (C11)** — **18 sujets mergés jamais appliqués**, dont la campagne lycée anglais/français **en entier**. Du travail fini, invisible. **C3 est à 4/5** (reste l'arabe, bloqué par sa transcription) et la 1ère sec compte **6 matières en ligne**. **C9 a beaucoup avancé** (anglais 2ᵉ/3ᵉ/bac, français 2ᵉ/bac, philo bac). **C4bis étape 0 faite** (#118, registre 5 → 56, tous avec `competency`) ; étape 1 à prendre. **Tier A fait** (arena#652). Toujours rien sur : **vidéos 9ᵉ** (C2) |
| Fondations | Domaine câblé + monitoring + sitemap (F4) · légal F5 · triage ops F6 en route · `main` verte (§1)                                                                                                              | **`main` verte ✅** et **F4 soldée**. 🔴 **Nouveau : le garde pédagogique est en panne depuis 12 jours** (F10, #81 — 4 runs échoués) ; toute la campagne C9 a été écrite sans lui. **F6 n'a plus aucun blocage technique** ; reste le seul geste opérateur. **F5 reste le vrai bloqueur de la Porte 1**, et **un volet est du CODE** : GAP-024 « droits des personnes » (suppression de compte + export) n'existe nulle part dans `src/` — re-vérifié le 2026-08-10 |

## 8. Journal de la roadmap

| Date       | Événement                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2026-08-10 | **Resynchronisation contre les DEUX dépôts (#709 → #716 au moteur, #116 → #148 ici) — 37 PR n'étaient citées nulle part, et le gate était vert.** C'est le constat de méthode de la passe : `roadmap-sync` ne lit que les sujets de commit du **moteur** en forme « étude/lot ». Les sept jours écoulés se sont joués **au privé**, sur du contenu et de la transcription — deux catégories qu'il ne regarde pas et qu'il n'a jamais prétendu regarder. **Un gate vert veut dire « rien de ce que je sais lire ne manque », jamais « la roadmap est à jour »** ; l'écrire ici parce qu'une session qui voit le vert conclut l'inverse. **Deux chantiers ouverts n'avaient AUCUNE ligne**, alors que leurs deux issues étaient ouvertes, étiquetées et visibles : **C11** — #124, `content-drift`, **18 sujets mergés jamais publiés**, dont `english-3eme-sec` ×6, `english-bac` ×6 et `french-bac` ×5, soit **la campagne lycée en entier**, à J-22 — et **F10** — #81, le **garde pédagogique en panne depuis le 2026-07-29**, quatre runs échoués (07-29, 08-01, 08-05, 08-08), donc **toute cette campagne écrite sans filet**. Les deux se referment seules une fois le geste fait ; aucune ne s'est refermée, faute de geste. **Quatre lignes décrivaient un état faux** : **C4bis** (son étape 0 est faite — #118, registre de **5 à 56 entrées, toutes avec `competency`** ; une session l'aurait refaite), **C3** (**4 matières sur 5 en prod** au 2026-08-04, seul l'arabe manque et c'est un blocage de **transcription**, pas de génération — arena#714 ; la 1ère sec compte **6 matières en ligne**), **C9** (une campagne lycée entière livrée : #126 → #144, plus les correctifs d'audit #146/#147/#148), **F5** (« reste, et c'est humain » — faux : la suppression de compte et l'export **n'existent pas dans `src/`**, re-vérifié ce jour ; c'est le seul bloqueur légal qu'un agent peut lever, et le classer humain l'a gelé une semaine). **Priorité inter-files ré-arbitrée au §0** : **C11 → F10 → C4bis**. C11 d'abord parce que c'est le seul geste qui **ne produit rien et livre tout**. **Aussi au moteur, non repris ailleurs** : le topo resynchronisé deux fois (arena#710, #714) · l'admin rebondi hors du Hall, chaque « Retour au hall » le ramenant sur Suivi (arena#711) · le tableau de cours qui se coupait en deux et dont les colonnes arabes se lisaient à l'envers (arena#712), puis son en-tête qui n'en était pas un pour un lecteur d'écran (arena#713) · un secret malformé qui annonçait le nom d'une librairie à la place du sien (arena#715) · le bump `undici` (arena#716). **Et ici** : le doublon de gabarit, défaut n°1 de l'écriture parallèle, qui n'était écrit nulle part (#121) · la clôture de session du 2026-08-03 (#122) · la garde `content-drift` consignée là où on la cherchera (#125) — consignée, et pourtant non prise pendant six jours : **documenter une garde ne la fait pas exécuter**. **ENFIN, TROUVÉ EN VÉRIFIANT CETTE PR — la CI de contenu de ce dépôt était MORTE, et le geste de C11 avec elle.** La PR de resynchronisation a fait rougir `content-ci` sur `npm ci`, pas sur son diff : `Missing: typescript@5.9.3 from lock file`. Reproduit en local, bissecté à **arena#716** (bump `undici` par Dependabot, qui a supprimé au passage l'entrée imbriquée `vite-tsconfig-paths/node_modules/typescript` que le peer `tsconfck ^5.0.0` réclame). **Mais #716 était VERTE au moteur** — et c'est là que se trouve la vraie cause : le moteur tourne sur **Node 24 depuis arena#688** (`.nvmrc` + ses 11 workflows), tandis que **les six workflows d'ici qui le checkoutent étaient restés à Node 22**. Même arbre, deux npm majeurs, deux verdicts : npm 11 accepte ce lockfile, npm 10 le refuse. **Portée réelle de la panne** : `content-ci` (toute PR de contenu), `content-audit`, `video-health`, `apply-content-test` et surtout **`apply-content`** — donc **la publication des 18 sujets de C11 était impossible** au moment même où cette PR la déclarait « un dispatch ». Corrigé ici : les six passent à Node 24. **La leçon est la même que celle de toute la passe, sous un troisième costume : un gate ne voit qu'un dépôt.** Le moteur a bumpé Node chez lui, complètement et correctement de son point de vue ; les workflows d'ici, qui exécutent ses scripts, lui sont invisibles. **POST-SCRIPTUM — `main` a avancé pendant la rédaction de cette entrée, ce qui est sa meilleure illustration** : **#145** (`english-bac` ch.04-06, la tranche 2) et **#149** ont mergé pendant la session, portant la base à `77a7736`. Les deux sont inscrites (C9 pour la première, F10 pour la seconde). **#149 mérite mieux qu'une citation** : `video-health.yml` avait été exécuté **trois fois** depuis son portage et avait échoué les trois fois au même endroit — un **troisième** garde qui n'avait jamais rendu de verdict, après les deux pannes du garde pédagogique. Sa sonde marchait ; c'est l'étape `gh` d'après qui tombait, faute de `GH_REPO` dans un workspace dont la racine n'est pas un dépôt git. Et l'étape qui **ouvre** l'issue portait le même défaut sans jamais s'exécuter, gardée par `broken != '0'` : elle aurait cassé le jour du premier vrai incident. F10 cesse donc de décrire un incident et décrit une **série** — trois gardes, trois pannes muettes : ce qui manque n'est jamais la garde, c'est que **sa panne n'atteint personne**. |
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
