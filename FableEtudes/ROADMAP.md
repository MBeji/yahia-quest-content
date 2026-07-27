# ROADMAP — ordre d'exécution du reste-à-faire (études, lots, contenu)

<!-- roadmap-sync: since-pr=641 -->

> **Instantané du 2026-07-27** (créé le 2026-07-20, resynchronisé contre `main` le 2026-07-25
> puis le **2026-07-27**) — déclinaison opérationnelle de l'**étude 26 (doctrine verticale : profondeur
> avant largeur)**. Les Q-1…Q-5 de l'étude 26 ayant été **arbitrées le 2026-07-20**, cet ordre
> n'est plus une recommandation d'architecte : il est **officiel**. La même session a rendu
> **tous les arbitrages en attente** (A1→A5) — plus aucune ligne de ce fichier n'est bloquée par
> une décision humaine. L'état de référence reste [STATUS.md](../STATUS.md) + l'[index des
> études](./README.md).
> **Jalon produit : rentrée scolaire, 1ᵉʳ septembre 2026** (§7).

## 0. Mode d'emploi (comment exécuter cette roadmap)

1. **Une ligne = une session = un lot = une PR** (règles FableEtudes inchangées : cadre fermé,
   DoD intégral, la session suit sa PR jusqu'au merge).
2. **Trois files parallèles** : PRODUIT (§3), FONDATIONS (§4), CONTENU (§5). Elles ne se
   bloquent pas entre elles — une session prend **la première ligne non cochée de sa file**
   dont les dépendances sont satisfaites.
3. **Plus aucun arbitrage humain n'est en attente** (tous rendus le 2026-07-20, §2). Les
   entrées autrefois marquées ⚖️ portent désormais leur décision entre parenthèses.
4. Priorité inter-files en cas de choix : finir l'en-vol (§1) > PRODUIT > FONDATIONS >
   CONTENU nouveau (les corrections qualité contenu passent, elles, avant tout — P-4).

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

## 2. Arbitrages — TOUS RENDUS le 2026-07-20

> Session de décision unique (Mohamed, 2026-07-20), consignée par #537. **Aucun arbitrage n'est
> plus en attente** :
> toute ligne de ce fichier est exécutable dès qu'une session la prend. Le détail de chaque
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

**Ce qui reste à la main de Mohamed** (hors lots, sans blocage de file) : é23 Q-3 (self-désigner
l'app child-directed auprès de Google + paragraphe « vidéos YouTube » de la politique de
confidentialité — la page n'existe pas encore) · é24 Q-4 (démarche OTDAV/INNORPI) · F5 (légal
avant rentrée) · **le signalement `d12f0f96` à passer `dismissed`** dans `/admin/content-reports`
(artefact e2e écrit en prod, cause corrigée par #618 — état **non vérifiable depuis ce dépôt**) ·
le **test à blanc de `rollback-prod.yml`** (`freeze-only` puis `unfreeze`) et les **gabarits
d'e-mail FR** à coller dans Supabase (STATUS §2 du 2026-07-27).
**~~F4~~ en sort** : domaine, monitoring, analytics et sitemap sont **faits, constatés le
2026-07-27** — voir F4 au §4.

## 3. FILE PRODUIT — la verticale V1 « apprendre & maîtriser » (ordre strict)

> Objectif : refermer les trois boucles mortes (SM-2, misconceptions, adaptativité) et porter
> la boucle d'apprentissage à M3 avant la rentrée.
> **État au 2026-07-27 : 11 des 19 lignes livrées** (inchangé depuis le 2026-07-25 — les
> livraisons des 26-27/07 sont toutes des fondations ou du contenu). La prochaine ligne libre
> est la **9** (exécution de la correction riche, dont le contrat est désormais écrit).

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
- [ ] 9. **é04 lot A1.2 — exécution de la correction riche** — **⬅️ PROCHAINE LIGNE PRODUIT**, deux lots cadrés : **A1.2a** (serveur, `get_attempt_review` rend le tag de l'option choisie) puis **A1.2b** (client, bloc de correction riche). ⚠️ Stop-point de sécurité D-A1.2-2 : ne jamais rendre la map `distractor_tags` — l'option correcte étant la seule sans tag, elle désignerait la bonne réponse par élimination

**Étape C — le Rappel cesse de refuser des réponses justes (étude 20, validée)**

- [x] 10. **é20 lot 1 — socle scoring ensembliste** (`accepted_answers` server-only + juge unique `is_accepted_free_answer`) — #583
- [ ] 11. **é20 lot 7 — type natif `short_answer`** (moteur) — **indépendant, exécutable dès maintenant** (l'étape D dont il était parallélisé est finie)

**Étape D — la maîtrise devient visible (étude 07 puis 04-A2)**

- [x] 12. **é07 lot 2 — DB de maîtrise** (`user_competency_mastery` EWMA + oubli, trigger sur télémétrie) — #579
- [x] 13. **é07 lot 4 — panneau compétences** (« ce qui te bloque », RPCs map/blockers) — #588. ⚠️ Livré **avant** le tagging C4 : inerte par construction tant que le corpus n'est pas tagué, jamais faux
- [x] 14. **é07 lot 5 — plan compétence-aware** (`get_daily_plan` priorise par compétence) — #616, correctif de GRANT #617. Même réserve : inerte sans C4
- [ ] 15. **é04 lot A2.1 — « Points faibles »** (misconceptions en langage élève + « S'entraîner »)
- [ ] 16. **é04 lot A2.2 — rapport parent enrichi** (3 points faibles majeurs + tendance)

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
      **Deuxième reliquat, à faire ICI** : porter dans la Content CI privée les **assertions
      pgTAP de contenu** devenues orphelines à la scission (issue publique MBeji/yahia-quest-arena#574).
      Elles ont été retirées du dépôt public parce qu'elles dépendaient de lignes de corpus qui
      n'y sont plus ; tant qu'elles ne sont pas rejouées quelque part, **ce que le contenu
      garantissait en base n'est plus testé nulle part**. Petit lot, mais il ferme un trou de
      couverture ouvert depuis le 2026-07-20.
- [ ] F3. **é09 lots 1-2 — la mesure** (page admin « Économie » + simulateur `economy:check`) — condition du KPI-4 é26 (« excellent » mesurable) ; lot 3 conditionnel ensuite. _Vérifié le 2026-07-25 : aucune route admin « Économie », rien n'est commencé._
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
- [ ] F5. **Légal avant rentrée** : GAP-003 (conformité mineurs INPDP) + GAP-024 (pages légales)
- [ ] F6. **Ops récurrent** : le triage hebdo des signalements. **Le volet technique est fait** —
      le pré-gate déterministe (#611) ne réveille l'agent que sur du nouveau, avec une soupape
      à 14 jours. Reste le **geste opérateur** : appliquer depuis `/admin/content-reports` et
      `/admin/bug-reports` les `dismissed` recommandés, ce qui referme la boucle. **La file a
      fondu** : plus 14 issues de triage ouvertes mais **3** au 2026-07-27 — le pré-gate fait son
      travail, le geste manque toujours. ⚠️ Et ces trois-là (#627, #632, #637) sont **des
      artefacts**, pas des élèves : **arena#638 (ouverte)** montre que
      `e2e/authed/content-report.spec.ts` écrit en prod **chaque nuit vers 04:42 UTC** depuis le
      2026-07-25 — le filet de #618 ne couvre que les hôtes exacts, un **slug de preview** passe
      au travers. Tant qu'il n'est pas corrigé, la file se re-remplit toute seule.
- [ ] F7. **Dépendances majeures — la file est nettoyée, deux majors restent.** Le lot
      patch/minor étant scripté (#613, corrigé par #625 qui lui apprend à lire les lignes `0.x`),
      il ne restait que les majors et leurs issues doublonnées (#233 ≡ #595 · #236 ⊂ #594 ·
      #234 périmé, closes depuis). **Le major Supabase est fait** : `setup-cli` v2 → v3.0.0 +
      CLI 2.108.0 → 2.109.1, livré le 2026-07-25 par **#622** (ferme #594/#236). **Restent deux
      PRs, une par major** : **#595** (`@types/node` v22 → v26, lié Node 22 → 26 LTS) et
      **#593** (`typescript` v7, gate rouge : `typescript-eslint` incompatible — attendre l'amont).
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
- [ ] C3. **é16 vague A — les 4 matières restantes de 1ère secondaire** (base fidèle au programme + overlay `prof-*-lycee` d3/d4 ; une matière = une session ; génération native fr, décision 2026-07-13)
- [ ] C4. **é07 lot 3 — tagging compétences vague 1** (questions math 9ᵉ + 6ᵉ, registre `content/competences/math.json`). **⬅️ PRIORITÉ MONTÉE** : les lots 4 et 13/14 produit sont livrés mais **inertes sans ce tagging** — c'est le seul chantier qui allume la maîtrise, la carte « ce qui te bloque » et la priorisation du plan quotidien.
- [ ] C5. **é20 lots 2 → 4 — réponses acceptées** : Tier A morphologique déterministe (corpus entier) → skill Tier B + pilote petites classes ar → campagne (1 matière/PR, priorité petites classes → concours) ; puis lot 5 (saisie arabe) et lot 8 (pilote `short_answer`)
- [ ] C6. **Illustration — backlog é18 (ordre petites-classes-d'abord)** : 4ᵉ puis 5ᵉ année (toutes matières visuelles) → maths 7ᵉ (5 ch.) → maths 9ᵉ fonctions+stats (2) → iq-training (3) → français (1). **Entamé le 2026-07-26** : 10 figures « objet réel » remplacées par des illustrations libres en `eveil-2eme` (#10) et **23 figures** de la campagne animaux sur 1ᵉʳ → 4ᵉ année (#11), outillées par l'import du moteur (arena#623). Le reste de la liste est inchangé
- [ ] C7. **é19 lot 1 — doctrine + gate figures questions** _(A3 rendu : SVG seul, vérification intégrale, lots ≤ ~40 figures)_, puis campagne questions illustrées (concours d'abord : 6ᵉ/9ᵉ/bac)
- [ ] C8. **é21 lot 1 — doctrine manuels** _(A4 rendu : verbatim court non créatif toléré ; provenance NON affichée à l'élève, lot 3 abandonné)_, puis pilote `math-1ere-sec` (exercices tracés `manuel_ref`, rapport de couverture)
- [ ] C9. **Transcriptions secondaire (fil continu, METHODE-GENERATION-CONTENU)** : finir `math-2eme-sec-sciences` (12/19 ch. transcrits) · `3eme-sec-anglais` (wip) · suite du lycée. **La campagne de GÉNÉRATION lycée massive est débloquée** depuis l'exécution des lots 3b/4 de é24 (#544) — elle n'attendait pas le lot 5.
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

## 6. FILES DIFFÉRÉES (ne rien lancer avant leur porte d'entrée)

| File                                                             | Porte d'entrée                                                      | Contenu                                                                           |
| ---------------------------------------------------------------- | ------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| **V2 — concours**                                                | V1 ≥ M3 (étapes 1-16) **et** annales transcrites (`NN-annales-bac`) | é02 re-scopée (« examen blanc » sans wording premium), percentiles                |
| **V4 — parent**                                                  | é04-A2.2 livré (ligne 16)                                           | é08 re-scopée + digest hebdo IA (é11 lot 6 la sert aussi)                         |
| **Gels — actés (A1-Q3, 2026-07-20)** ; application par é26 lot 2 | Dégel par décision humaine explicite uniquement                     | é06 (PWA offline) · é10 (anti-fraude — se dégèle au volume) · é12 (studio in-app) |
| **Gelée (phase)**                                                | Sortie de la phase gratuite (décision humaine)                      | é01 (paiement en ligne — véhicule de réactivation du premium)                     |

## 7. Vue jalon — ce qui doit être vrai le 1ᵉʳ septembre 2026

| Axe        | Cible rentrée                                                                                                                                                                                                  | État au 2026-07-27                                                                                                                        |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| Produit    | File V1 étapes **1-16** livrées (é22 complet dont bannière rentrée · Révision du jour · correction riche · Rappel tolérant lot 1 · maîtrise visible · points faibles + rapport parent)                         | **11/19 lignes faites** (le « 10/19 » du 2026-07-25 comptait mal), dont toute l'étape A et l'étape D côté moteur. Restent : correction riche (9), `short_answer` (11), A2 (15-16) |
| IA         | A5 **rendu le 2026-07-20** : é11 dégelée (lots 0-2, pilote math 9ᵉ, budget 5 $/j, tuteur « El Ostedh »). Lots 0-1 à la rentrée **seulement si une session les prend hors file V1** — sinon octobre             | non commencé — conforme au plan                                                                                                           |
| Contenu    | Classes existantes à la barre é18 · 1ère sec complète (5 matières) · vidéos 9ᵉ · Tier A `acceptedAnswers` corpus entier · cible arbitrée (A1-Q2) = **statu quo consolidé à la barre é18**, sans classe vitrine | **C4 (tagging compétences) reste le point dur** — trois lots produit livrés en dépendent. Bougé depuis : la campagne petites classes (C10 : `french-4eme`, `french-5eme`, `arabic-6eme` + fiche 6ᵉ base) et l'illustration entamée (C6) ; ni 1ère sec, ni vidéos 9ᵉ, ni Tier A |
| Fondations | Domaine câblé + monitoring + sitemap (F4) · légal F5 · triage ops F6 en route · `main` verte (§1)                                                                                                              | **`main` verte ✅** (nightly + e2e-auth) et **F4 soldée le 2026-07-27** (domaine, monitoring, analytics, SMTP, secrets du kill-switch). Restent **F5** (Mohamed) et le geste opérateur de **F6** — que le bug arena#638 re-remplit chaque nuit |

## 8. Journal de la roadmap

| Date       | Événement                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2026-07-20 | Création (déclinaison de l'étude 26, état consolidé post #525/#526/#527/#529/#531)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 2026-07-20 | **Session d'arbitrages — A1→A5 tous rendus** (Mohamed). é26, é19, é21, é11 → `validée` ; les 4 écarts de é24 tranchés (lot 3b débloqué) ; é23 resynchronisée en `en exécution`. **Corrections d'état** : A6 sans objet (PRs legacy mergées les 12-13/07), `main` — CI requise verte, `Nightly`/`E2E auth` rouges. Le tuteur IA est renommé **« El Ostedh »**. La roadmap devient officielle (A1-Q1).                                                                                                                                                                                                                                                                                                                                                                                                                |
| 2026-07-25 | **Ligne 8 livrée — amendement é04-A1.2 écrit** (`04-moteur-adaptatif/ETUDE.md` §9). Contrat fermé en deux lots (A1.2a serveur / A1.2b client). Il corrige deux suppositions du mandat : l'explication post-erreur n'était **pas** monnayée (c'est l'indice avant réponse qui l'est), et le feedback question-par-question rouvre la couture de soumission atomique — sorti du périmètre, posé en **Q-4**. Le lot sera **inerte tant que le corpus n'est pas tagué** (C4), assumé. La prochaine ligne PRODUIT devient la **9**.                                                                                                                                                                                                                                                                                      |
| 2026-07-25 | **Resynchronisation contre `main` — 24 lots livrés manquaient.** La règle « cocher dans la même PR » était inapplicable depuis la scission (é24) : deux dépôts, aucune PR commune. Elle est remplacée par un invariant vérifié (§0) — chaque ligne cochée cite sa PR, et le gate `check-roadmap-sync.mjs` échoue si un lot livré n'est cité nulle part. **§1 « reverdir `main` » est clos** (nightly vert 5 nuits, e2e-auth vert, #250/#363 closes) et sa mise en garde pgTAP est périmée (#563). **F8 ajoutée** : l'étude « IA vs déterministe », 6 lots, close — elle avait tourné entièrement hors roadmap. **A8** consigné (script maison plutôt que Renovate). **F7 nettoyée** (issues majors doublonnées, #234 périmé). **C4 remontée en priorité** : trois lots produit livrés sont inertes sans le tagging. |
| 2026-07-27 | **Resynchronisation contre `main` (base #536 → #641).** Le gate `check-roadmap-sync.mjs` était **vert** — il ne voit que les sujets de commit en forme « étude/lot », et rien de ce qui a été livré les 26-27/07 n'en portait la forme : la dérive de ces deux jours est un **angle mort assumé** du gate, pas une panne. Corrigé ici à la main. **Fondations** : F4 **cochée** — le go-live infra est soldé, et il l'était en partie **depuis des semaines sans trace dans le repo** (GA4 tournait, le DSN Sentry était posé) ; F7 **nettoyée** (major Supabase livré par arena#622, restent #595 et #593) ; F8 **refermée** par son volet contenu (5 lots `LC0…LC4` le 2026-07-25) ; **F9 ajoutée** pour l'outillage de campagne, livré entièrement hors roadmap. **Contenu** : **C10 ajoutée** — une campagne petites classes (`french-4eme`, `french-5eme`, `arabic-6eme`, fiche 6ᵉ base) tournait depuis le 26/07 **sans aucune ligne ici** ; C6 entamée (33 figures). **F6** : la file de triage est passée de 14 à 3 issues, mais les 3 sont des **artefacts** d'arena#638 (un e2e écrit en prod chaque nuit) — le geste opérateur reste vain tant que le bug vit. **Aucune ligne PRODUIT n'a bougé** : la prochaine reste la **9**. |
