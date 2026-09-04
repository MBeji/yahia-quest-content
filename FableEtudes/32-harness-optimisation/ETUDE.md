# Étude 32 — Harness : optimiser, simplifier, améliorer (les deux dépôts vus comme un seul outillage)

> **Statut** : **livrée** — les cinq lots sont mergés sur les deux dépôts le 2026-09-04 :
> arena#970, #971, #974, #975, #980, #981, #982, #983, #984 et privé#342, #343, #344, #345, #346.
> Q-1 a été **rouverte et retranchée** en cours d'exécution (la voie de repli, sans jeton), Q-5
> est née de la livraison et a été tranchée, et **deux constats neufs** — C-14 et C-15 — sont
> sortis de l'exécution elle-même. Rien n'attend plus le propriétaire
> **Priorité** : 32 · **Valeur** : 🔧 le harness (instructions, politique, hooks, gates, chaîne PR, gardes)
> est **bon** — déterministe, relu, gardé — mais il **crie pour rien** (21 % des runs du privé sont des
> rouges fantômes), **se paie deux fois** (chaque branche neuve du moteur fait tourner ses trois checks
> requis en double), **se répète** (trois workflows en deux versions divergentes, 1 579 lignes), et
> **ne se vérifie qu'à moitié** (le dépôt privé n'a aucun gate harness, et la seule borne du gate qui
> porte sur les skills ne mesure pas ce qu'elle annonce) · **Complexité** : moyenne
> **Architecte** : Fable / audit du 2026-09-03 · **Exécuteur cible** : Sonnet (ou équiv.) — lots courts,
> outillage et workflows, aucun impact runtime produit, aucune migration
> **Dépend de** : é25 (livrée sauf L7), étude « IA → déterministe » (close, moteur + volet contenu),
> arbitrage GitHub Free du 2026-08-24 (on reste en gratuit : rien ici ne le rouvre) · **Bloque** : —
> **Docs normatifs liés** : `AGENTS.md`, `docs/agents/gardes.md`, `docs/agents/zero-intervention.md`,
> `docs/ci-cd-and-branch-protection.md`, `harness/policy.json`, `CLAUDE.md` (privé)

## 0. TL;DR

Ce que l'audit a **mesuré** (pas supposé) le 2026-09-03, sur les 800 derniers runs du privé
(6,0 jours) et les 795 derniers runs du moteur (4,4 jours) :

| #   | Constat                                                                                                                                                                 | Mesure                                                             | Remède (lot)                                                   |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | -------------------------------------------------------------- |
| C-1 | Au privé, chaque PR ouverte par `auto-pr` laisse **quatre runs `failure` à zéro job** (Content CI, Pin check, Automerge, Roadmap sync) — l'événement `opened` du bot     | **167 fantômes / 800 runs = 21 %** ; a déjà coûté #280, #291, #293 | PAT au privé, ou retirer `opened` des déclencheurs (L1, Q-1)   |
| C-2 | `automerge` privé se réveille **cinq fois par branche** (2 dispatch de réveil + 2-3 `workflow_run` + 1 `pull_request`)                                                  | **288 runs / 6 j**, dont 108 par dispatch de réveil                | un seul chemin de réveil (L1)                                  |
| C-3 | Sur un dépôt **privé**, chaque job est facturé à la minute entamée : la chaîne consomme surtout des jobs de 10 s facturés 1 min                                          | ≈ **3 800 min/mois** estimées, pour 2 000 gratuites               | ✅ L1 livré (privé#344) ; relevé de facturation encore utile, mais **plus bloquant** (Q-2) |
| C-4 | Au moteur, `auto-pr` dispatche **inconditionnellement** CI + CodeQL + Migration gate sur chaque branche neuve, en plus des runs `pull_request` natifs                     | **38 dispatch pour 71 runs natifs** : ~35 % des runs CI en double  | dispatch de secours **après constat d'absence** (L3)           |
| C-5 | `second-opinion.yml` est **dormant** mais checkout le dépôt entier (`fetch-depth: 0`) à chaque push de PR pour conclure qu'il n'est pas armé                             | **71 runs / 4,4 j** pour zéro travail                              | garde-fou **avant** le checkout (L1)                           |
| C-6 | `auto-pr.yml`, `automerge.yml`, `guard-watch.yml` existent **dans les deux dépôts**, sans une ligne commune, et ont divergé **en sens inverse** (C-1/C-4)                | **1 579 lignes** en double ; 490/517/164 lignes différentes         | `guard-watch` réutilisable ; chaîne PR partagée ensuite (L3)   |
| C-7 | `harness:check` borne les descriptions de skills à 1 024 caractères — mais **ne mesure que la première ligne** (le `$` d'une regex en mode multiligne)                    | 2 skills privés hors spec (**1 202** et **1 157**) que rien ne voit | corriger par un vrai parse YAML (L2)                           |
| C-8 | Le dépôt privé (43 skills, 12 workflows, `CLAUDE.md` de 9,2 Ko) **n'a aucun gate harness** — ni budget, ni Unicode, ni spec, ni contrôle des vues ; `--corpus` n'est câblé nulle part | 1 invariant sur 9 (épinglage, ré-écrit en bash)                    | `harness:check --corpus` dans Content CI, `pin-check` supprimé (L2) |
| C-9 | `AGENTS.md` est à **250 / 250 lignes** et **24 184 / 24 576 octets** : la prochaine règle ne peut entrer qu'en en sortant une, et personne ne le sait avant d'échouer     | budget saturé à 100 % / 98 %                                       | ramener à ≤ 200 l. par déplacement, pas par suppression (L4)   |
| C-10 | `policy.json` nomme 27 scripts `npm run` un par un alors que `node scripts/:*` est ouvert en bloc ; et n'ouvre **ni `cat`, ni `grep`, ni `head`, ni `find`** — des lectures qui déclenchent une invite, donc une validation manuelle | 92 règles `allow`, 7,3 Ko de commentaire-journal                   | `npm run:*` + groupe `shell-readonly`, journal déplacé (L4)     |
| C-11 | Les workflows portent **30 % de commentaires** (2 226 lignes), souvent le récit complet d'un incident, parfois raconté trois fois (workflow, `CLAUDE.md`, ROADMAP)         | 7 365 lignes de YAML, 2 226 de prose                               | convention « le pourquoi en 10 lignes, le récit en doc » (Q-3) |
| C-15 | **`npm run typecheck` ne voyait aucun script** : `tsconfig.json` n'incluait que `src/**`. Les 13 fichiers qui portent les gates de contenu n'étaient typés par personne — trouvé par un `ReferenceError` que `tsc` aurait dû attraper | « 44 erreurs » qui n'en étaient **qu'une** : les scripts sont du Node | ✅ **livré (arena#986)** — second programme + invariant de gate |
| C-14 | Une PR doit être **à jour avec `main`** pour merger : chaque PR mergée pendant sa CI la relance **en entier**. Vu sur arena#975, qui n'a pas une ligne de `src/`                                                        | **5 têtes, 5 cycles CI complets** en 41 min, pour 4 PR entrées entre-temps | ✅ tranché (Q-5) : **accepté et mesuré** — arena#982                |
| C-12 | Le privé n'a **pas de `.gitattributes`** : le piège CRLF documenté pour le poste Windows n'est gardé que côté moteur                                                     | 0 règle EOL sur 659 chapitres                                      | copier la règle du moteur (L2)                                 |

Quatre lots, tous « une PR, gate verte, utile seul », sans toucher au produit. Le lot 1 se **remesure**
avec le même relevé que cette étude (§7) : c'est la métrique.

## 1. Contexte & objectif

### 1.1 Ce qu'on appelle « harness » ici

Cinq couches, réparties sur les deux dépôts depuis la scission de l'étude 24 :

| Couche                          | Moteur (public)                                                                                                                                | Privé (corpus)                                                                        |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| **Instructions**                | `AGENTS.md` (250 l.) canonique, `CLAUDE.md` pointeur, `copilot-instructions.md`, `.gemini/settings.json`, 5 skills techniques + miroir `.agents/` | `CLAUDE.md` (116 l., 9,2 Ko) autonome, 43 skills pédagogiques (13 Mo, 187 fichiers), `FableEtudes/` (METHODE 65 Ko, CONTRIBUER, POSTE) |
| **Politique & hooks**           | `harness/policy.json` (92 allow, 8 deny) → `.claude/settings.json` généré ; 3 hooks déterministes ; `models.json` ; `controls.json`            | **rien** — ni settings, ni hooks, ni politique                                        |
| **Gates locaux**                | `verify` (7 étapes, 2 min 50 s mesurées), husky pre-commit/pre-push, `harness:check` (9 invariants), `leak:check`, `db:check-chain`, `eol:check` | aucun (les gates contenu tournent depuis le moteur)                                    |
| **Chaîne PR & gardes CI**       | 25 workflows (4 667 l.), dont 3 gardes agent avec pré-gate, 1 dormant, ruleset avec 4 checks requis                                             | 12 workflows (2 698 l.), dont 1 garde agent avec pré-gate ; **aucun check requis** (Free) |
| **Méthode**                     | `docs/agents/` (9 playbooks, 2 825 l.), `STATUS.md` (225 Ko)                                                                                    | études, ROADMAP, skill `/campagne` (319 l.)                                          |

### 1.2 Ce que l'étude 25 et l'étude « IA → déterministe » ont laissé

Elles ont fait le gros du travail — et cette étude ne rouvre rien de ce qu'elles ont fermé :

- **déterministe d'abord** : plus aucune surface ne dépense un agent sur un chemin nominal ; les cinq
  pré-gates tournent ; le lot patch/minor est un script ; le hook pré-commit est un script (< 1 s) ;
- **déclaratif** : `policy.json` compile `settings.json`, `models.json` est la seule place d'un
  identifiant de modèle, `controls.json` déclare où tourne chaque contrôle orphelin ;
- **gardé** : neuf invariants dans `harness:check`, actions épinglées au SHA, YAML strict, garde des
  gardes dans les deux dépôts, anti-fuite du corpus.

Ce qu'elles n'ont pas regardé, parce que ce n'était pas leur objet : **le volume** (combien de runs
pour une PR), **la symétrie** (le privé a hérité de la structure du moteur, pas de ses gates), et **la
saturation** (AGENTS.md et policy.json ont grossi jusqu'à leur plafond).

### 1.3 Objectif & indicateurs

Objectif : **moins de bruit, moins de double, et des gates qui vérifient ce qu'ils annoncent** — sans
retirer un seul filet.

| KPI                                                     | Aujourd'hui (2026-09-03)                | Cible après L1-L4                          |
| ------------------------------------------------------- | --------------------------------------- | ------------------------------------------ |
| Runs `failure` à zéro job au privé (6 j)                | 167 (21 % des runs)                     | ✅ **0** (livré, privé#344 + arena#980) — **constaté dans les deux sens le jour même** : la PR #343 portait 3 de ces runs sur son SHA, la #344 aucun. Un invariant de `harness:check --corpus` empêche la rechute |
| Runs par branche poussée au privé (moyenne)             | **9,7** (runs hors branche par défaut ÷ 48 branches, définition d'`actions-census`) | ≤ 4 |
| Runs CI+CodeQL+Migration gate par branche neuve, moteur | 6 (3 natifs + 3 dispatchés)             | ✅ **3** (livré, arena#974) — constaté sur la PR qui le livrait : 8 check runs au lieu de 14 |
| Runs de `second-opinion` dormant (4,4 j)                | 71 **runners alloués**                  | ✅ **0 runner** (livré, arena#970) — la LIGNE du run demeure, avec un job `skipped` : la cible d'origine disait « 0 run », elle était fausse |
| Invariants `harness:check` vérifiés sur le privé        | 1 (épinglage, en bash)                  | ✅ **7** (livré, arena#971 + privé#342) — et `pin-check.yml` supprimé |
| Skills hors spec Agent Skills (description > 1 024)     | 2, invisibles                           | ✅ **0**, et gatés (arena#971 + privé#342) |
| Lignes de workflow en double entre dépôts               | 1 579                                   | ⚠️ **partiellement** (L3b, arena#981 + privé#345). `guard-watch` : 378 lignes en deux copies → 314 de YAML dont **74 encore identiques**, plus 173 lignes de script partagé et testé. **Le total brut AUGMENTE** — ce qui disparaît n'est pas du volume mais une seconde copie non testée de la décision. La chaîne PR (`auto-pr`, `automerge`) reste en deux exemplaires |
| Cycles CI par PR au moteur, `main` chargée              | **5** (mesuré sur arena#975, 41 min)    | ✅ **mesuré en continu** (Q-5 tranchée : accepter, mais compter). `actions:census` rend désormais les têtes par branche et nomme la plus relancée |
| Symlinks pour lancer les gates de contenu               | 2                                       | ✅ **1** (lot 5, arena#983/#984 + privé#346) — le registre de 12 Mo a rejoint `content/`. Vérifié : le SQL émis reste **identique octet pour octet**, donc aucune dérive avec la prod |
| Scripts couverts par `typecheck`                        | **0** sur `scripts/**`                  | ✅ **13 sur 13** (livré, arena#986). Les « 44 erreurs » étaient **une seule cause** : 31 disaient `Cannot find name 'process'`, les scripts étant du Node là où `tsconfig.json` ne charge que `vite/client`. Avec `lib: ES2023` + `types: ["node"]`, il en reste **zéro** |
| Marge d'`AGENTS.md`                                     | 0 ligne, 392 octets                     | ✅ **36 lignes** (214/250, livré arena#975), pas les 50 promises : le reste est irréductible sans perte. Un seuil d'alerte à 92 % préviendra avant le prochain plafond |
| Scripts npm nommés à la main dans `policy.json`         | 21                                      | ✅ **0** (livré, arena#975). ⚠️ La cible d'origine — « ≤ 60 règles » — était **fausse** : elle comptait 27 entrées npm là où il y en avait 21, et ne comptait pas les 15 lectures ajoutées. Le compte réel tombe à 88, et le nombre de règles n'était de toute façon pas la bonne mesure |

## 2. État des lieux mesuré (2026-09-03)

### 2.1 Méthode de relevé

- **Runs** : l'API Actions des deux dépôts, 8 pages de 100 runs chacune, dédoublonnées par id,
  agrégées par workflow × conclusion × événement. Fenêtre obtenue : privé 2026-08-28 21:46 →
  2026-09-03 21:12 (6,0 j) ; moteur 2026-08-30 11:32 → 2026-09-03 21:10 (4,4 j). Les durées de job
  viennent de `/runs/{id}/jobs` sur des runs témoins.
- **Gates locaux** : chronométrés dans une session Linux neuve (`npm install` à froid, Node 22 —
  le poste et la CI sont en 24, l'ordre de grandeur est le même).
- **Skills** : frontmatters parsés en **YAML réel** (paquet `yaml` du moteur), puis comparés à ce que
  `checkSkillFrontmatter` de `check.mjs` renvoie sur les mêmes fichiers.
- **Churn** : `git log` sur `origin/main` approfondi (1 026 commits moteur, 1 000 privé), depuis le
  2026-07-19 (début de l'étude 25).

### 2.2 Volumes de la chaîne CI

**Privé — 800 runs en 6,0 jours (134/jour) pour 95 pushes de branche :**

| Workflow                | Runs | /jour | Conclusions                                        | Événements                                           |
| ----------------------- | ---: | ----: | -------------------------------------------------- | ---------------------------------------------------- |
| Automerge (corpus)      |  288 |  48,2 | 199 ok · **51 failure** · 32 skipped · 5 cancelled | 116 `workflow_run` · **108 `workflow_dispatch`** · 62 `pull_request` |
| Content CI              |  149 |  24,9 | 89 ok · **58 failure**                             | 93 `pull_request` · 54 dispatch · 2 push             |
| Pin check               |  147 |  24,6 | 95 ok · **51 failure**                             | 93 `pull_request` · 52 dispatch · 2 push             |
| Auto PR (corpus)        |   95 |  15,9 | 95 ok                                              | 95 push                                              |
| Apply content (PROD)    |   38 |   6,4 | 36 ok · 2 failure                                  | 38 dispatch                                          |
| Contenu non publié      |   32 |   5,4 | 32 ok                                              | 25 dispatch · 6 schedule · 1 push                    |
| Garde des gardes        |   23 |   3,8 | 23 ok                                              | 22 schedule                                          |
| Roadmap sync            |   23 |   3,8 | 10 ok · **13 failure**                             | 13 `pull_request` · 6 schedule · 4 dispatch          |
| Content audit           |    3 |   0,5 | 2 ok · 1 failure                                   | 2 schedule · 1 dispatch                              |
| Video / Manuel health   |    2 |   0,3 | 2 ok                                               | schedule                                             |

Les **167 `failure`** de Content CI / Pin check / Automerge / Roadmap sync sont **toutes** des runs
`pull_request` à **zéro job** (vérifié sur les runs 33806452226 et 33784452835 : `total_count: 0`) —
le run que GitHub enregistre puis refuse quand la PR a été ouverte par le `GITHUB_TOKEN`. Ce sont
exactement les fantômes que `CLAUDE.md` décrit, et qui ont coûté trois incidents. Hors fantômes, la
chaîne est verte : **zéro échec réel** sur Pin check, Automerge et Roadmap sync ; 6 vrais rouges de
Content CI sur 97 runs réels (des PR de contenu en cours de correction).

**Ce que coûte une branche poussée au privé** (relevé sur `claude/avance-prochaines-etapes-02eeta`,
2026-09-03 21:10) : Auto PR (1) → fantômes `pull_request` (4, à 0 job) → Content CI et Pin check
dispatchés (2) → chacun réveille automerge (2) → `workflow_run` de chacun (2) → `pull_request:opened`
d'automerge (1, fantôme). **Douze runs, dont cinq à zéro job et cinq réveils d'automerge, pour deux
gates.**

**Facturation** : sur un dépôt privé, chaque job est facturé à la minute **entamée** (`CLAUDE.md`,
« le plan gratuit n'en donne que 2 000 par mois »). Or les jobs réels sont courts — Pin check **10 s**,
Automerge **9 s**, Content CI **33 s** (npm ci 11 s, cinq gates 8 s) — donc facturés 1 min chacun.
Estimation sur la fenêtre : ≈ 750 min pour 6 jours, soit **≈ 3 800 min/mois**, dont ≈ 1 200 pour
les seuls réveils et sweeps d'automerge. C'est une estimation (les fantômes ne coûtent rien, les
`apply-content` sont comptés à 4 min) ; **le chiffre réel est sur la page de facturation du compte**,
hors dépôt — c'est un mur au sens de `zero-intervention.md`, et c'est la seule ligne de cette étude
qui demande un relevé humain (Q-2).

**Moteur — 795 runs en 4,4 jours (181/jour) pour 72 pushes de branche :**

| Workflow                 | Runs | /jour | Conclusions                        | Événements                                     |
| ------------------------ | ---: | ----: | ---------------------------------- | ---------------------------------------------- |
| CodeQL                   |  145 |  32,9 | 131 ok · 14 cancelled              | 71 `pull_request` · **38 dispatch** · 35 push  |
| CI                       |  144 |  32,7 | 110 ok · 17 failure · 17 cancelled | 71 `pull_request` · **38 dispatch** · 35 push  |
| Migration gate           |  109 |  24,8 | 109 ok                             | 71 `pull_request` · **38 dispatch**            |
| Auto-merge / Auto PR     | 72+72 | 32,8 | ok                                 | push / `pull_request`                          |
| Second opinion (dormant) |   71 |  16,1 | 69 ok · 2 cancelled                | 71 `pull_request`                              |
| Report close             |   35 |   8,0 | 35 skipped                         | `pull_request`                                 |
| db-migrate-prod          |   31 |   7,0 | 31 ok                              | 24 schedule · 7 push                           |
| DB integration tests     |   30 |   6,8 | 20 ok · 6 failure · 4 cancelled    | `pull_request` (chemins filtrés)               |
| Freeze / Garde / Triage  | 21+17+17 |    | ok                                 | schedule                                       |
| Nightly · E2E auth · Upgrade guard · Regression guard | 5+3+5+1 | | 3 nightly rouges (#854) | schedule / dispatch / `workflow_run` |

Les 17 `failure` de CI sont de vrais rouges sur des branches en cours (6 sur une seule) ; les 17
`cancelled` sont la concurrence par ref qui annule un run dépassé. Les **38 dispatch** sont la
dispatch **inconditionnelle** posée le 2026-08-24 dans `auto-pr.yml` après la panne d'événements
`pull_request` du 2026-08-23 : le fichier lui-même écrit « on paie donc deux exécutions complètes
par check requis ». Sur un dépôt public les minutes sont gratuites ; ce qu'on paie est la **file** —
le 2026-08-26, GitHub a cessé d'assigner des runners pendant des heures (STATUS.md), et un dépôt
qui demande six runs là où trois suffisent attend deux fois plus.

### 2.3 Gates locaux et hooks (mesurés)

| Étape de `verify`         | Durée   | Note                                                                      |
| ------------------------- | ------- | ------------------------------------------------------------------------- |
| `eol:check`               | 0,27 s  |                                                                           |
| `leak:check`              | 0,17 s  |                                                                           |
| `db:check-chain`          | 0,23 s  |                                                                           |
| `harness:check`           | 0,28 s  | 9 invariants                                                              |
| `lint`                    | 24 s    | ESLint + 2 scripts maison                                                 |
| `typecheck`               | 26 s    |                                                                           |
| `test`                    | 115 s   | 319 fichiers, 3 922 tests ; `environment 84 s` (jsdom — déjà traité par docblocks `node`) |
| **Total (pre-push)**      | **≈ 2 min 50 s** | ordre « rapide d'abord » respecté ; rien à optimiser ici sans risque |

Les trois hooks Claude (`guard-generated`, `precommit-checks`, `format-changed`) sont déterministes,
fail-open, testés (250 l. de tests pour le pré-commit). Rien à changer — sauf noter qu'ils sont
**Claude-only** (accepté par l'étude 25 : le filet dur reste husky + CI).

### 2.4 Le gate `harness:check`, éprouvé sur le privé

`check.mjs` exporte ses fonctions pures ; on les a appliquées au dépôt privé, que le gate ne voit
jamais :

| Invariant                                  | Résultat sur le privé                                                                                                         |
| ------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------- |
| Budget de taille (`checkAgentsSize`)       | `CLAUDE.md` : 116 l., 9 213 o — dans le budget, mais **personne ne le mesure**                                               |
| Spec skills (`checkSkillFrontmatter`)      | **0 problème** sur 43 — **faux** : parsés en YAML, `content-ingest` = **1 202** et `content-audit` = **1 157** caractères     |
| Unicode invisible (`findInvisibleChars`)   | **38 occurrences** dans 29 fichiers : U+200D dans des séquences emoji (l’emoji « enseignant », deux glyphes joints) de 25 `prof-*`, U+200F (marque RTL) dans les skills arabes, U+200C dans `course-figures.md`, un BOM U+FEFF dans un programme — **tous légitimes**, tous rouges tels quels |
| Identifiants de modèle (`findModelIds`)    | **1 faux positif** : « O2 » (le dioxygène, programme de SVT 1ʳᵉ sec) matche `\bo[0-9]`                                       |
| Épinglage SHA                              | 12/12 épinglés — vérifié par `pin-check.yml`, une ré-écriture bash de `findUnpinnedActions`                                    |
| YAML strict `.github/**`                   | jamais vérifié au privé (l'incident du 2026-08-24 était un doublon de clé dans `auto-pr.yml` — le fichier existe aussi ici)  |
| `controls.json` mode `--corpus`            | « crues sur parole » (le fichier le dit) — alors que Content CI a **déjà** les deux checkouts et le `npm ci` qu'il lui faut  |

Le défaut de C-7 se reproduit en trois lignes (annexe B) : la regex qui extrait la description s'arrête
au premier `$` en mode `m`, donc à la première fin de ligne. Toutes les descriptions du projet sont
des blocs `>-` multilignes : **la borne n'a jamais rien mesuré**, sur aucun des 48 skills.

### 2.5 Duplication et prose

| Fichier             | Moteur | Privé | Lignes différentes | Divergence de fond                                                                     |
| ------------------- | -----: | ----: | -----------------: | -------------------------------------------------------------------------------------- |
| `auto-pr.yml`       |    325 |   289 |                490 | moteur : PAT + auto-merge natif + dispatch **inconditionnelle** ; privé : pas de PAT, dispatch **si aucun run réel** (compte les jobs) |
| `automerge.yml`     |    246 |   341 |                517 | moteur : arme `gh pr merge --auto` (ruleset) ; privé : sweep maison « état, pas événement » |
| `guard-watch.yml`   |    170 |   208 |                164 | même métier, même filtre zéro-job ré-écrit, cadence et libellés différents             |

Trois constats : (1) le privé a la **meilleure** logique de dispatch (il compte les runs réels avant
de dispatcher), le moteur la **meilleure** chaîne de merge (native, opposable) ; (2) chaque correctif
d'un côté doit être re-découvert de l'autre — `guard-watch` en est à sa 3ᵉ ré-écriture du test
« zéro job » ; (3) un workflow public est **appelable** depuis un dépôt privé (`uses:
MBeji/yahia-quest-arena/.github/workflows/x.yml@<sha>`), ce que rien n'exploite.

Prose : 4 667 l. de workflows moteur dont 1 337 de commentaires (28 %) ; 2 698 l. privées dont 889
(32 %). `policy.json` : 7 326 caractères de `$comment` pour 100 règles. `CLAUDE.md` privé : sur 116
lignes, 60 racontent la chaîne de merge (auto-pr, fantômes, automerge, drift) — la même histoire
que l'en-tête de `auto-pr.yml` (45 l.) et que ROADMAP §11. Le savoir est juste et précieux ; c'est
sa **place** qui coûte : trois copies dérivent, et l'une des trois est le fichier que chaque session
lit en premier.

Churn depuis le 2026-07-19 : moteur 41 commits sur `.github/workflows` (10 sur `ci.yml`, 9 sur
`report-triage.yml`, 8 sur `upgrade-guard.yml`), 32 sur `AGENTS.md`, 72 sur `STATUS.md` ; privé 35
sur `.github/workflows` (11 sur `apply-content.yml`), 85 sur `.claude/skills`. Le harness est une
surface **vivante** : un tiers des commits de la période le touchent d'une façon ou d'une autre.

### 2.6 Ce qui est bon et ne bouge pas

- Le contrat des gardes (`gardes.md`), les cinq pré-gates, `models.json`, `check-claude-result.py`.
- Le hook pré-commit déterministe et le trio de hooks.
- Le ruleset du moteur et ses 4 checks requis ; l'anti-fuite ; `db:check-chain` ; le canari npm 10 et
  la garde de diff de dépendance (A17, #958).
- La garde des gardes, `content-drift`, `freeze-watch` : des gardes qui **rendent visible**.
- L'ordre de `verify` (4 gates à 1 s avant lint/typecheck/test).
- L'arbitrage « on reste en GitHub Free » : rien ici ne suppose un ruleset au privé.

## 3. Constats détaillés

### C-1 — Les fantômes : un événement que personne n'a demandé

**Fait.** `auto-pr.yml` (privé) ouvre la PR avec le `GITHUB_TOKEN`. GitHub émet l'événement
`pull_request: opened`, l'enregistre comme run pour chaque workflow qui l'écoute — Content CI, Pin
check, Roadmap sync (via `paths`), Automerge (`types: [opened, …]`) — puis le **refuse** (garde
anti-récursion) : conclusion `failure`, **zéro job**, aucun log. 4 fantômes par PR, 167 sur 6 jours.

**Coût.** Nul en minutes, lourd en lecture : `gh pr checks` les affiche rouges ; `gh run list` les
compte ; trois sessions les ont mal lus (#280 course imaginaire, #291 garde qui a gelé la chaîne un
jour, #293 « 37 gardes en échec »). Le projet a répondu par une **heuristique** partout — le test
`jobs | length == 0` dans `auto-pr.yml`, `guard-watch.yml`, et 20 lignes de `CLAUDE.md` — au lieu de
supprimer la cause.

**Remède.** Deux voies étaient exclusives ; **Q-1 a tranché pour (a) le 2026-09-04**. La voie (b)
est conservée ci-dessous parce qu'elle reste le repli exact si le jeton ne peut pas être créé :

- **(a) Un PAT au privé** (`GH_AUTOMATION_PAT`, fine-grained, `contents:write` + `pull_requests:write`,
  comme au moteur) : la PR est ouverte par une identité de collaborateur → les événements
  `pull_request` sont **réels**, `workflow_run` se déclenche, plus de dispatch, plus de réveils, plus
  de fantômes. C'est ce que fait le moteur depuis le 2026-07-12. Contrepartie : un secret qui expire
  (celui du moteur expire le 2026-10-04 — la rotation est un geste humain annuel, deux dépôts → deux
  secrets, ou un seul PAT à deux dépôts). La logique « dispatch si aucun run réel » du privé **reste**
  en secours, comme le moteur a appris à le faire le 2026-08-23 — mais elle ne sert plus que le jour
  où GitHub perd ses événements.
- **(b) Sans PAT** : retirer `opened` des `types:` de `pull_request` sur les quatre workflows
  (`[synchronize, reopened, ready_for_review]` ; automerge garde `labeled, unlabeled`). L'événement
  `opened` du bot ne produisait **jamais** un run à jobs : le retirer ne retire aucune évaluation —
  `auto-pr` dispatche déjà les gates à la création. Un push suivant (`synchronize`, par un humain ou
  une session) reste un événement réel. Coût zéro, une ligne par workflow ; **mais** la mécanique de
  réveil et de dispatch reste, avec ses cinq runs d'automerge.

Dans les deux cas : **supprimer les heuristiques zéro-job** devenues sans objet (auto-pr, guard-watch)
et réduire le paragraphe de `CLAUDE.md` à deux lignes qui disent ce qui a été fait, pas comment lire
un fantôme.

### C-2 — Cinq réveils d'automerge par branche

**Fait.** Le chemin dispatché ne produit pas de `workflow_run` (même garde anti-récursion), donc
`content-ci.yml` et `pin-check.yml` portent chacun une étape « Réveiller automerge » (`gh workflow run
automerge.yml --ref main`, sous condition `workflow_dispatch`). Deux réveils par branche, plus les
`workflow_run` du chemin natif sur les pushes suivants, plus le `pull_request` d'automerge lui-même.
288 runs en 6 jours pour ≈ 51 PR.

**Remède.** Avec C-1(a) le chemin dispatché devient l'exception : les deux étapes de réveil ne tournent
plus que sur ce chemin (leur condition existe déjà). Avec C-1(b), les réduire à **une** : seul le
dernier gate dispatché réveille — ou, plus simple et sans dépendance d'ordre, `auto-pr` dispatche
**un seul** workflow-parapluie `checks.yml` (`workflow_call` des deux gates) qui réveille automerge
une fois. Cette seconde forme a un autre mérite : un seul run à dispatcher, un seul à compter.

### C-3 — Les minutes du privé

Voir §2.2. Le remède est C-1/C-2 (moitié des runs) et C-8 (un workflow de moins). Le relevé
facturation est Q-2 : si le compte est en dépassement, cette étude monte d'un rang ; s'il est en Pro,
le mur « ruleset sur dépôt privé » de `zero-intervention.md` est levé et l'arbitrage du 2026-08-24
mérite une note — pas une réouverture.

### C-4 — Au moteur, chaque branche neuve paie deux fois

**Fait.** Depuis le 2026-08-24, `auto-pr.yml` dispatche `ci.yml`, `migration-gate.yml` et `codeql.yml`
sur toute branche dont il vient d'ouvrir la PR, **sans regarder** si le run `pull_request` natif
existe — parce qu'au moment où l'étape s'exécute il n'existe pas encore, et que « son absence
définitive ne se distingue pas de son simple retard ». Les groupes de concurrence sont indexés sur
le ref (`refs/pull/N/merge` vs `refs/heads/<branche>`), donc les jumeaux ne s'annulent pas.

**Remède (D-3).** Distinguer l'absence du retard **en attendant** : l'étape dort 90 s, puis demande
à l'API les runs sur le SHA de tête (`gh run list --commit`, exactement le test du privé) et ne
dispatche que les workflows sans run réel. Sur un dépôt public, 90 s d'un job d'une minute ne
coûtent rien ; la panne du 2026-08-23 (aucun run une heure après) est toujours couverte, et le cas
nominal ne tourne plus qu'une fois. La concurrence par branche a été écartée à raison (un `cancelled`
est un rouge pour le ruleset) — on ne la rouvre pas.

### C-5 — Un garde dormant qui checkout tout

**Fait.** `second-opinion.yml` écoute `pull_request` (`opened, synchronize, reopened, labeled`), fait
un `actions/checkout` avec `fetch-depth: 0`, **puis** constate que le secret manque et skippe. 71
runs en 4,4 jours. L'étude « IA → déterministe » L5 a borné l'agent, pas le workflow.

**Remède — ✅ LIVRÉ le 2026-09-04 (arena#970).** Une condition **de job**, avant tout checkout : `if: vars.SECOND_OPINION_ARMED == 'true'
|| github.event.label.name == 'second-avis' || github.event_name == 'workflow_dispatch'`. La variable
de dépôt remplace le test du secret (un `if:` de job ne peut pas lire `secrets`) ; `gh variable set`
est dans `policy.json` (`repo-config`). Le double verrou (secret + `models.json`) reste dans le job.

### C-6 — Trois workflows en deux versions

Voir §2.5. Le remède se fait en deux temps, du plus simple au plus structurant :

1. **`guard-watch`** devient un workflow **réutilisable** du moteur (`on: workflow_call`, entrées :
   fenêtre, cadence, libellé d'issue), appelé au privé par une ligne `uses:` épinglée au SHA. Le
   filtre zéro-job disparaît des deux (C-1). Un seul fichier à corriger la prochaine fois.
2. **La chaîne PR** converge **après** Q-1 : si le privé reçoit un PAT, `auto-pr.yml` des deux dépôts
   ne diffère plus que par l'armement natif (`gh pr merge --auto`, impossible sans ruleset) — une
   entrée `with: native-automerge: false` suffit à un réutilisable. `automerge.yml` reste double par
   nature (natif vs sweep) tant que le privé est en Free ; on ne force pas une abstraction sur deux
   comportements voulus différents.

### C-7 — La borne qui ne mesure que la première ligne

**Fait.** `checkSkillFrontmatter` extrait la description par une regex terminée par `(?=\n[a-zA-Z-]+:|$)`
en mode `m` ; en mode multiligne `$` matche **chaque** fin de ligne, la capture paresseuse s'y arrête,
et une description de 1 400 caractères sur deux lignes rend `[]` (annexe B). Le gate a été livré au
lot 3 de l'étude 25 avec la phrase « dépassements attendus sur content-*/prof-* » — et n'en a jamais
signalé un seul.

**Remède.** Parser le frontmatter avec le paquet `yaml` déjà présent (il sert à l'invariant 8) :
`parse(frontmatter).description`. Trois lignes, un test qui rejoue le cas de l'annexe B, et deux
skills privés à raccourcir (`content-ingest` 1 202 → ≤ 1 024, `content-audit` 1 157 → ≤ 1 024).
Ce n'est pas cosmétique : la description est injectée dans le prompt système de **chaque session**
(la somme au privé est de 34 047 caractères pour 43 skills), et la spec plafonne à 1 024 pour cette
raison.

### C-8 — Le privé n'a pas de gate harness

**Fait.** Le dépôt privé est né « avec la même structure harness » (é25 D-8) — il a les skills et les
workflows, pas les gates. `harness:check` ne connaît que le moteur ; le mode `--corpus` de
`checkControlCoverage` existe et n'est « branché dans aucun workflow » (`controls.json`, qui l'écrit
honnêtement et cite `roadmap-sync.yml` sans `npm ci` comme candidat). Or **`content-ci.yml` a déjà
tout** : les deux checkouts, `npm ci` du moteur, et tourne sur chaque PR.

**Remède (D-5).** Une étape dans `content-ci.yml` :
`node engine/scripts/harness/check.mjs --corpus "$GITHUB_WORKSPACE/corpus"`, après avoir rendu le
mode `--corpus` complet — aujourd'hui il ne vérifie que `controls.json`. Ce qu'il doit couvrir sur le
corpus, et ce que §2.4 impose d'ajuster :

| Invariant                      | Sur le corpus                                                                                                           |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------- |
| Budget                         | `CLAUDE.md` privé ≤ 150 l. / ≤ 12 Kio (aujourd'hui 116 / 9,2)                                                           |
| Spec skills                    | les 43 frontmatters (`name` = dossier, description ≤ 1 024 **en YAML**)                                                  |
| Unicode invisible              | frontmatters + workflows seulement (comme au moteur) ; **tolérer** U+200D entre deux points de code emoji et U+200E/U+200F dans un fichier contenant de l'arabe ; interdire toujours U+202A-E, U+2060-64, U+FEFF, tags |
| Identifiants de modèle         | workflows + frontmatters seulement, jamais `references/` (« O2 »)                                                       |
| Épinglage SHA                  | `findUnpinnedActions` sur `.github/workflows` du corpus → **`pin-check.yml` supprimé** (−1 workflow, −96 runs / 6 j)     |
| YAML strict                    | `.github/**` du corpus                                                                                                   |
| `controls.json`                | mode vérifié (déjà écrit)                                                                                                |

Et `.gitattributes` copié du moteur (C-12), avec `eol:check` pointé sur le corpus si le script accepte
une racine (sinon, `git ls-files --eol` en une ligne).

### C-9 — AGENTS.md est plein

**Fait.** 250 lignes sur 250, 24 184 octets sur 24 576. Le budget de l'étude 25 (D-1b) était une borne
haute pour Codex ; il est devenu un plafond touché. Sections les plus lourdes : « Known gotchas »
42 l., « Content pipeline » 40 l., « Essential commands » 27 l. Deux des pièges de « Known gotchas »
existent déjà en long dans `docs/agents/pieges-du-code.md` (229 l.), et l'histoire de la scission dans
`docs/content-generation-pipeline.md`.

**Remède (D-8).** Déplacer, ne rien supprimer : « Known gotchas » → 8 l. (les trois pièges qui coûtent
le plus + pointeur) ; « Content pipeline » → 15 l. (ce qu'on fait, pas quand on l'a décidé) ;
`harness:check` ajoute un **seuil d'alerte** (≥ 230 l. ou ≥ 22 Kio → `::warning`, pas rouge) pour que
la saturation se voie **avant** d'être bloquante. Cible ≤ 200 l.

### C-10 — La politique nomme trop et couvre trop peu

**Fait.** 92 règles `allow`. 27 sont des `npm run <script>` nominatifs (`gates` + `content-pipeline`)
alors que `repo-scripts` ouvre `node scripts/:*` — c'est-à-dire **tout** ce que ces scripts appellent.
Aucun script npm n'écrit la prod (le seul qui le fait, `push-prod.mjs`, est dénié par nom). À
l'inverse, les lectures ordinaires du shell — `cat`, `head`, `tail`, `grep`, `rg`, `find`, `wc`,
`diff`, `jq`, `sed -n` — ne sont pas listées, donc **invitent**, donc violent la règle « une invite est
une validation manuelle » sur des commandes qui ne changent rien. Manquent aussi `npm run eol:check`,
`harness:sync`, `perf:check`, `programme:*`, `content:emit`, `content:figures:check`, `economy:check`.

**Remède (D-7).** `Bash(npm run:*)` + `Bash(npm test)` remplacent 27 entrées ; un groupe
`shell-readonly` (liste close, sans `sed -i`, sans `xargs`, sans `>`), avec la même règle que
`ops-dispatch` : on ajoute par nom, jamais par joker. Le `$comment` de 7,3 Ko — trois arbitrages datés
— va dans `docs/agents/zero-intervention.md` (qui est déjà le document de ces arbitrages), le fichier
gardant **une ligne de raison par groupe**. `harness:check` vérifie que chaque groupe a sa raison.
Cible : ≤ 60 règles couvrant plus de commandes qu'aujourd'hui. ⚠️ Ceci lève des invites **du dépôt** ;
le classifieur d'auto-mode reste un mur (zero-intervention.md).

### C-11 — La prose des workflows

**Fait.** 2 226 lignes de commentaires dans 37 workflows, dont l'essentiel est le **récit** d'incidents
(dates, numéros de PR, ce qu'on a cru puis compris). Ce récit est la meilleure documentation du projet
— et il est au **mauvais endroit** pour deux raisons : un workflow se lit en diagonale par qui doit le
corriger vite, et le même récit vit déjà ailleurs (ROADMAP §11, STATUS, journal des décisions,
`CLAUDE.md`), donc dérive.

**Remède (Q-3, pas de lot imposé).** Convention pour tout workflow **touché** désormais : l'en-tête dit
**ce que** le fichier fait, **pourquoi** il existe et **ce qu'il ne fait pas**, en ≤ 15 lignes ; chaque
étape non triviale garde ≤ 5 lignes de « pourquoi » ; le récit d'incident va dans
`docs/agents/incidents-ci.md` (nouveau, append-only, une entrée = date, symptôme, cause, correctif,
fichiers) et le workflow le **cite**. Pas de réécriture en masse — ce serait un lot de 2 000 lignes
pour zéro comportement — mais chaque lot de cette étude applique la convention aux fichiers qu'il
touche (auto-pr, automerge, guard-watch, content-ci, second-opinion : 1 546 lignes, ≈ 500 de prose).

### C-12 — Pas de `.gitattributes` au privé

**Fait.** Le moteur impose `* text=auto eol=lf` et garde l'arbre par `eol:check`, parce qu'un CRLF
invisible a cassé `npm test` sur le poste Windows (2026-07-25). Le corpus — 659 chapitres édités
depuis ce même poste — n'a ni l'un ni l'autre. Un `quiz.json` en CRLF passe Zod, passe la QA, et
diffère à l'octet de ce que `content:emit` produira ailleurs.

**Remède.** Dans L2, avec C-8.

### C-13 — Un registre de transcription dans un skill (hors lot, Q-4)

`programmes-officiels/` (12 Mo, 130 fichiers : manifestes, programmes transcrits, `suivi/`) vit sous
`.claude/skills/content-ecole-tn/references/`. C'est un **registre de données** (sortie du LOT A de la
méthode), pas une instruction de skill ; c'est lui qui impose le **second** symlink de la recette
locale et de Content CI, et son chemin est codé dans quatre scripts du moteur (`audit-program.ts`,
`check-manuel-links.ts`, `etat.ts`, `programmes-io.ts`). Le déplacer sous `content/programmes-officiels/`
ramènerait à un symlink et sortirait 12 Mo du prompt-space des skills. C'est un chantier à cheval sur
les deux dépôts, la METHODE et le skill `/campagne` : **hors périmètre** de cette étude, posé en Q-4
pour qu'il soit tranché plutôt qu'oublié.

### C-15 — `typecheck` ne voyait aucun script (né de l'exécution, livré arena#986)

Trouvé de la seule façon honnête : par un bug que cette étude a elle-même introduit. En
centralisant le chemin du registre (lot 5), `join` a manqué à l'import d'`audit-program.ts` ;
`npm run typecheck` est passé **vert**, et c'est `content:audit:strict` qui est mort sur un
`ReferenceError` au premier lancement réel.

La cause : `tsconfig.json` n'inclut que `src/**`, `vite.config.ts` et `eslint.config.js`.
**Aucun des scripts n'est typé** — ni `scripts/content/**`, qui porte les gates de contenu du
corpus, ni `scripts/ci/**`, ni `scripts/harness/**`. Ce sont pourtant des fichiers `.ts` que
Node exécute en `--experimental-strip-types` : le typage y est purement décoratif.

Mesuré en étendant l'inclusion au reste de l'arbre : **44 erreurs de type**, concentrées sur
`suivi.ts` (10), `programmes-io.ts` (10), `etat.ts` (5), `check-manuel-links.ts` (5).

✅ **Livré (arena#986), et le chiffre était trompeur** : ces 44 erreurs n'en étaient **qu'une**.
**31 sur 44** disaient `Cannot find name 'process'` — les scripts sont du **Node**, et
`tsconfig.json` ne charge que `vite/client` et `vitest/globals` ; les 13 autres (paramètres
implicitement `any`) en découlaient, faute d'API Node typées. Avec un second programme
(`tsconfig.scripts.json`, `lib: ES2023`, `types: ["node"]`), il en reste **zéro**, sans une
ligne de code corrigée. D'où deux programmes plutôt qu'un : les fondre obligerait à charger les
types du navigateur dans les scripts et ceux de Node dans l'app.

**Et le filet ne peut plus se vider en silence** — la leçon que cette étude a tirée trois fois.
`harness:check` ferme les deux façons de le perdre : débrancher le second programme de la chaîne
npm, ou rétrécir son `include`. Éprouvé dans les deux sens ; la seconde panne sort 13 constats,
un par fichier redevenu invisible.

⚠️ **Un bug de la livraison, attrapé par son propre test** : la conversion glob → regex faisait
deux `replace` enchaînés, et le second réécrivait le `*` que le premier venait d'insérer dans
`(?:.*/)`. Le motif `scripts/**/*.ts` ne couvrait alors plus un fichier profond — un gate qui
aurait menti dans le sens du silence. C'est la troisième fois de cette étude qu'un test écrit
pour un cas précis attrape le défaut de son propre outil.

⚠️ Ce constat rejoint la ligne directrice de l'étude — *un gate qui ne mesure pas ce qu'il
annonce est pire qu'un gate absent* — et c'est le troisième de la même famille : la borne des
descriptions de skills ne lisait que leur première ligne (C-7), le corpus n'avait aucun gate de
harness (C-8), et `typecheck` ne couvre pas la moitié du code exécuté.

### C-14 — Rester à jour avec `main` relance toute la CI (né de l'exécution, hors lot)

Ce constat ne vient pas de l'audit : il vient de **cette étude en train de se livrer**. Pour merger,
arena#975 devait être à jour avec `main` ; l'auto-merge y a donc fusionné `main` à chaque fois qu'une
autre PR entrait, et chaque fusion a produit une tête neuve, donc **un cycle CI complet de plus**.

| Tête       | Née de                                     | Ce qu'elle a relancé            |
| ---------- | ------------------------------------------ | ------------------------------- |
| `3d7d95d9` | le push de la PR                           | CI + CodeQL + Migration gate    |
| `2b0ee5c0` | `main` ← #976                              | idem                            |
| `82146fb1` | `main` ← #977                              | idem                            |
| `ca26098c` | `main` ← #972                              | idem                            |
| `e4fa88a8` | `main` ← #978                              | idem — celle qui a mergé        |

**Cinq cycles pour une PR de 8 fichiers**, dont aucun ne touche `src/` : ni le build, ni le smoke
navigateur, ni les 3 982 tests ne pouvaient changer d'un cycle à l'autre. Les quatre relances sont
arrivées en **41 minutes**, parce que quatre PR ont mergé dans cette fenêtre.

C'est une **troisième** source de runs par branche, distincte des deux que l'audit avait nommées (les
fantômes de C-1, le double dispatch de C-4) : celle-ci ne vient d'aucun défaut de configuration mais
de la règle « à jour avant de merger », qui est **saine** — c'est elle qui empêche un merge sémantique
cassé. Elle n'apparaissait pas au relevé du 2026-09-03 parce que ce jour-là `main` était calme ; elle
explique une part du **9,7 runs/branche** que le §1.3 attribuait entièrement aux deux autres causes.

Deux voies existent, et **aucune n'est évidente** : une file de merge (GitHub merge queue — à vérifier
sur un compte Free, où les rulesets ne sont déjà pas disponibles au privé), ou une CI en deux étages où
seul l'étage sensible au contenu du diff se rejoue. La seconde touche au gate lui-même, ce que cette
étude s'est interdit ailleurs. D'où **Q-5** plutôt qu'un lot : le constat est mesuré, le remède est un
arbitrage.

## 4. Décisions d'architecture (fermées, sous réserve de Q-1)

| #    | Décision                                                                                                                                                                       | Constat |
| ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------- |
| D-1  | Une PR n'émet jamais un check rouge qu'aucun job n'a évalué : la cause des fantômes est supprimée (PAT **ou** retrait d'`opened`, Q-1), et toute heuristique « zéro job » est retirée avec elle | C-1     |
| D-2  | Un seul chemin de réveil d'`automerge` au privé ; le dispatch de secours ne tourne qu'après constat d'absence de run réel                                                        | C-2     |
| D-3  | Au moteur, la dispatch de secours attend 90 s puis ne dispatche que les checks **sans** run natif sur le SHA — la logique du privé, portée                                     | C-4     |
| D-4  | Un garde dormant coûte zéro run : condition de job avant tout checkout, armée par une variable de dépôt                                                                        | C-5     |
| D-5  | **Un seul `harness:check`** pour les deux dépôts : `--corpus` couvre les invariants de §C-8, tourne dans Content CI, remplace `pin-check.yml` ; la borne des descriptions parse du YAML | C-7, C-8 |
| D-6  | Ce qui est identique de métier est un workflow **réutilisable** du moteur, appelé par SHA depuis le privé — `guard-watch` d'abord, `auto-pr` après Q-1 ; `automerge` reste double tant que le privé est en Free | C-6     |
| D-7  | `policy.json` ouvre par **famille** ce que ses dénis bornent déjà (`npm run:*`), ajoute `shell-readonly` par nom, et garde une raison par groupe — le journal des arbitrages va dans `zero-intervention.md` | C-10    |
| D-8  | `AGENTS.md` retrouve ≥ 50 lignes de marge par déplacement vers les docs qui existent, et `harness:check` avertit à 92 % du budget                                                | C-9     |
| D-9  | Convention de prose des workflows (≤ 15 l. d'en-tête, récit en `docs/agents/incidents-ci.md`), appliquée aux fichiers touchés, jamais en masse                                  | C-11    |
| D-10 | Le privé reçoit `.gitattributes` et un contrôle EOL                                                                                                                             | C-12    |
| D-11 | Le relevé des runs de cette étude devient un script (`scripts/ci/actions-census.mjs`), pour que les KPI se **remesurent** au lieu de se raconter                                | §1.3    |

Ce que l'étude **écarte** : passer le privé en GitHub Pro (arbitré, Q-2 ne le rouvre que si la
facturation le force) ; un `schedule` d'automerge (144 runs/jour à 1 min facturée) ; la concurrence
par branche au moteur (un `cancelled` est un rouge pour le ruleset) ; réécrire la prose des workflows
en masse ; un hook agent quelconque (l'étude « IA → déterministe » a fermé ça) ; toucher à l'ordre ou
au contenu de `verify`.

## 5. Cible

| Surface                                        | Avant                                    | Après                                                            |
| ---------------------------------------------- | ---------------------------------------- | ---------------------------------------------------------------- |
| Runs par branche poussée (privé)               | 12 (5 à zéro job, 5 réveils d'automerge) | 4 (Auto PR, Content CI, Automerge ×2) avec PAT ; 6 sans           |
| Workflows privés                               | 12                                       | 10 (`pin-check` absorbé, `guard-watch` appelé)                   |
| Runs CI/CodeQL/Migration gate par branche neuve (moteur) | 6                              | 3 (+ 3 le jour où GitHub perd ses événements)                     |
| Invariants harness au privé                    | 1 (bash)                                 | 7, par le même script que le moteur, dans la même CI              |
| Lignes de workflow dupliquées                  | 1 579                                    | ≈ 350 (`automerge` seulement)                                    |
| `policy.json`                                  | 92 allow, 7,3 Ko de commentaire          | ≤ 60 allow, une raison par groupe, plus de lectures couvertes     |
| `AGENTS.md`                                    | 250 l. / 24,2 Ko                         | ≤ 200 l., alerte à 230                                            |
| Mesure                                         | à la main, une fois                      | ✅ `actions-census.mjs`, rejouable (livré, arena#970) — `--from` rejoue un dump hors ligne |

Arborescence touchée (aucun fichier produit) :

```
moteur/
  .github/workflows/auto-pr.yml           D-3 (attente + constat), D-9
  .github/workflows/second-opinion.yml    D-4
  .github/workflows/guard-watch.yml       D-6 (workflow_call + entrées)
  scripts/harness/check.mjs               D-5 (YAML, --corpus complet, tolérances Unicode, seuil d'alerte)
  scripts/harness/__tests__/check.test.mjs
  scripts/ci/actions-census.mjs (+ test)  D-11
  harness/policy.json                     D-7
  AGENTS.md, docs/agents/pieges-du-code.md, docs/agents/zero-intervention.md, docs/agents/incidents-ci.md (nouveau)
privé/
  .github/workflows/auto-pr.yml, automerge.yml, content-ci.yml, roadmap-sync.yml   D-1, D-2, D-9
  .github/workflows/pin-check.yml         supprimé (D-5)
  .github/workflows/guard-watch.yml       → appel du réutilisable (D-6)
  .gitattributes (nouveau)                D-10
  .claude/skills/content-ingest/SKILL.md, content-audit/SKILL.md   descriptions ≤ 1 024
  CLAUDE.md                               § chaîne de merge ramené à ce qui reste vrai
```

## 6. Plan d'exécution en lots

Chaque lot = **une PR par dépôt**, gate verte, utile seul. Ordre : L1 → L2 → L3 → L4, puis L5
(optionnel, Q-4). Depuis l'arbitrage du 2026-09-04, **plus aucune décision n'est en attente** : L1
attend seulement la **valeur** du PAT, et sa moitié moteur (D-4, D-11) ne l'attend même pas. Aucun lot ne touche deux dépôts dans une même PR
(invariant du projet) : les lots à deux dépôts se livrent **moteur d'abord** (le privé l'appelle).

| Lot | Contenu                                                                                                                                                                                                                                     | Dépôt(s)            | Tests / preuve exigés                                                                                                                                  | Dépend de |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | --------- |
| L1  | **La chaîne cesse de crier pour rien.** D-1 (voie (a), Q-1), D-2, D-4, D-11 ; retrait des heuristiques zéro-job (auto-pr privé, guard-watch ×2) ; `CLAUDE.md` privé § chaîne de merge ramené à l'état vrai                                       | moteur (D-4, D-11) puis privé | `actions-census.mjs` avant/après sur 3 jours : **0 run à zéro job**, ≤ 4 runs par branche ; une PR de test poussée au privé merge seule ; `second-opinion` : 0 run sur une PR sans label | valeur du PAT (Q-1) |
| L2  | **Un seul `harness:check`.** D-5 (YAML, `--corpus` complet, tolérances Unicode, scope des ids de modèle, seuil d'alerte D-8), D-10 ; Content CI appelle le gate ; `pin-check.yml` supprimé ; 2 descriptions raccourcies                       | moteur puis privé   | Vitest : cas de l'annexe B, ZWJ-emoji toléré / RLO refusé, « O2 » ignoré, `--corpus` sur un faux corpus ; Content CI verte **et** rouge sur une PR témoin qui rallonge une description | —         |
| L3  | **Le moteur ne paie plus deux fois.** D-3 ; D-6 (`guard-watch` réutilisable, appelé du privé) ; D-9 sur les fichiers touchés                                                                                                                | moteur puis privé   | census : 3 runs par branche neuve ; une branche poussée pendant une panne simulée d'événements (dispatch manuel de test) déclenche bien la secours ; `guard-watch` privé ouvre/ferme son issue sur un rouge fabriqué (`workflow_dispatch` d'un workflow en `exit 1`) | L1        |
| L4  | **La politique dit moins et couvre plus.** D-7, D-8 ; `harness:check` vérifie « une raison par groupe » et avertit à 92 %                                                                                                                    | moteur              | `harness:sync` idempotent ; session réelle : `cat`/`grep`/`npm run eol:check` sans invite ; `AGENTS.md` ≤ 200 l. avec table de correspondance dans la PR (rien ne se perd, règle D-1b de l'é25) | —         |

Points durs :

- **L1, la seule décision.** Q-1 change la forme du lot, pas son critère : zéro fantôme, un réveil. Si
  PAT : `gh secret set GH_AUTOMATION_PAT` est dans `policy.json` (`repo-config`), la session le pose
  dès que Mohamed lui donne la valeur — et note la date d'expiration dans `zero-intervention.md`
  (tableau des murs, ligne « secrets hors dépôt »). Sans PAT : quatre lignes `types:` et rien d'autre.
- **L2, le piège des tolérances.** Un ZWJ n'est légitime **qu'entre deux points de code emoji** ; une
  marque RTL n'est légitime **que** dans un fichier qui contient de l'arabe (plage U+0600–U+06FF). Les
  tests doivent rejouer les 38 occurrences réelles de §2.4 **et** un RLO caché dans une description —
  le cas d'attaque que l'invariant existe pour attraper. `pin-check.yml` n'est supprimé qu'**après** que
  Content CI a prouvé le rouge sur une action dé-épinglée dans une PR témoin.
- **L3, l'attente.** 90 s de `sleep` dans un job d'`auto-pr` de 5 min de plafond ; si l'API répond
  une erreur, on **dispatche** (le doute réveille, comme pour les pré-gates). Le réutilisable
  `guard-watch` est appelé par SHA — donc `pin-check`… n'existe plus : c'est `harness:check --corpus`
  (L2) qui exige l'épinglage de la ligne `uses:` du privé, et il tourne avant.
- **L4, rien ne se perd.** Comme au L1 de l'é25 : la PR embarque le tableau section → destination.
  Le `$comment` de `policy.json` ne disparaît pas, il devient trois entrées datées de
  `zero-intervention.md` — qu'il cite déjà.

- [ ] Lot 1 — La chaîne cesse de crier pour rien (D-1, D-2, D-4, D-11)
      - [x] moitié **moteur** — D-4 (garde dormant borné) + D-11 (recensement) — arena#970, 2026-09-04
      - [ ] moitié **privé** — D-1, D-2 : attend la VALEUR du PAT (Q-1)
- [x] Lot 2 — Un seul `harness:check` pour les deux dépôts (D-5, D-8 seuil, D-10) — arena#971,
      arena#974 (correctif du mode corpus), privé#342, 2026-09-04
- [x] Lot 3a — Le filet de dispatch constate avant de doubler (D-3) — arena#974, 2026-09-04
- [ ] Lot 3b — `guard-watch` mutualisé (D-6) : **dépend du lot 1 privé**, et ce n'est pas un
      oubli — la version privée filtre les runs à zéro job, que le lot 1 supprime à la racine
      avec les fantômes. Mutualiser avant graverait un paramètre destiné à mourir
- [x] Lot 4 — La politique dit moins et couvre plus ; `AGENTS.md` respire (D-7, D-8) — arena#975,
      2026-09-04
- [ ] Lot 5 (optionnel, après L2) — `programmes-officiels/` sort du skill et rejoint `content/` (C-13, Q-4)

## 7. Stratégie de test & mesure

- **Unit (Vitest)** : `scripts/harness/__tests__/check.test.mjs` (description YAML, tolérances
  Unicode, scope des ids, seuil d'alerte, `--corpus` sur fixture), `scripts/ci/__tests__/actions-census.test.mjs`
  (agrégation sur un JSON témoin de runs — le même format que l'API).
- **Gate CI** : `harness:check` (moteur) et `harness:check --corpus` (Content CI) sont les juges ; la
  PR témoin « rouge attendu » de L2 est le seul test qui vaille pour un gate (leçon de
  `content:figures:check` : un gate que rien ne fait rougir n'a jamais été vu fonctionner).
- **Mesure** : `node scripts/ci/actions-census.mjs --repo MBeji/yahia-quest-content --pages 8`
  imprime le tableau de §2.2 ; il tourne **avant** et **après** chaque lot, et ses deux sorties vont
  dans le corps de la PR. C'est la métrique de l'étude, et le critère pour passer au lot suivant
  (même règle que l'étude « IA → déterministe » §7).

## 8. Risques & mitigations

| Risque                                                                                                    | Mitigation                                                                                                                            |
| --------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| Le PAT expire et personne ne le voit (RISK-1)                                                             | date d'expiration écrite dans `zero-intervention.md` ; la dispatch de secours du privé **reste** et couvre l'expiration comme une panne d'événements ; `freeze-watch`-like : une garde mensuelle lit `gh api /user` avec le PAT et ouvre une issue 30 j avant |
| Retirer `opened` cache une PR ouverte à la main (RISK-2, voie (b) seulement)                              | `auto-pr` ouvre la PR sur **chaque** push avant qu'un humain le puisse ; le sweep d'automerge sur `push: main` rattrape le reste ; documenté dans l'en-tête |
| L'attente de 90 s au moteur retarde la secours d'une vraie panne (RISK-3)                                 | 90 s contre « une heure sans run » constatée le 2026-08-23 : négligeable ; et le doute dispatche                                       |
| La tolérance Unicode ouvre une porte (RISK-4)                                                             | tolérances **contextuelles** (ZWJ entre emoji, RTL avec arabe), jamais par fichier ni par plage entière ; RLO/LRO/tags restent interdits partout ; test d'attaque dans la suite |
| Supprimer `pin-check.yml` avant que le remplaçant prouve son rouge (RISK-5)                               | ordre imposé dans L2 : PR témoin rouge d'abord, suppression ensuite                                                                   |
| `npm run:*` ouvre un script futur qui écrira la prod (RISK-6)                                             | `node scripts/:*` l'ouvre **déjà** ; le déni par nom (`push-prod.mjs`) reste ; règle écrite : tout script qui écrit la prod se dénie par nom le jour où il naît, comme `push-prod.mjs` |
| `AGENTS.md` perd une règle en déménageant (RISK-7)                                                        | table de correspondance dans la PR + `harness:check` continue de vérifier l'inventaire des features et les pointeurs                    |
| Le réutilisable `guard-watch` casse les deux dépôts d'un coup (RISK-8)                                    | appel **épinglé au SHA** : le privé ne bouge que quand on met sa ligne à jour ; c'est le même contrat que pour toute action tierce     |

## 9. Questions ouvertes — **toutes arbitrées le 2026-09-04**

Les quatre ont été posées une par une à Mohamed, avec leurs contreparties ; **les quatre réponses
suivent la recommandation de l'architecte**. Aucun ADR du §4 n'a eu à être révisé.

| #   | Question                                                                                          | Arbitrage du 2026-09-04                                                                                                                                                                                                                                    |
| --- | -------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Q-1 bis | Le jeton n'est pas venu : attendre, ou basculer sur le repli ?                             | ✅ **le repli, sans jeton** (2026-09-04, seconde passe). La question a été ROUVERTE parce que le contexte avait changé — et parce que la règle « zéro intervention » classe explicitement **supprimer le besoin** au-dessus de **remonter au propriétaire**. Un jeton à créer puis à renouveler dans un an est exactement l'intervention qu'elle cherche à éliminer. Livré en privé#344 + arena#980. Contrepartie assumée : la chaîne du privé reste organisée autrement que celle du moteur, donc une part de C-6 subsiste |
| Q-1 | Un PAT pour le privé, ou le retrait d'`opened` des déclencheurs ?                                 | ✅ **(a) un PAT fine-grained** — les deux dépôts, `contents:write` + `pull_requests:write`, 1 an. La chaîne du privé devient identique à celle du moteur : C-1 et C-2 disparaissent à la racine, et L3 (auto-pr partagé) devient possible. ⚠️ **DÉPASSÉE par Q-1 bis** (ligne suivante) : le jeton n'est jamais venu, et la question a été rouverte le jour même. C'est la voie (b), le repli sans jeton, qui a été livrée — privé#344 + arena#980. Cette ligne est conservée telle quelle : elle date l'arbitrage d'origine, et le récit de son revirement vaut mieux que sa réécriture |
| Q-2 | Relevé de facturation Actions du compte (minutes du mois, plan)                                   | ⏳ **ouverte, mais elle ne bloque plus rien.** Elle servait à décider si L1 passait au rang 0 pour cause de dépassement ; L1 est livré, et les fantômes qu'il supprime étaient la principale source de minutes facturées. Le chiffre reste **utile** pour vérifier après coup ce que le lot a rendu — c'est de la mesure, plus un arbitrage. Le moteur étant public, seules les minutes du dépôt PRIVÉ se paient |
| Q-3 | La prose des workflows : récit déplacé, en-tête ≤ 15 lignes ?                                     | ✅ **oui, sur les fichiers touchés** (D-9). `docs/agents/incidents-ci.md` naît append-only ; les cinq workflows que les lots modifient déjà y portent leur récit et le citent. **Jamais en masse** : rien n'est réécrit pour la seule beauté du geste, et rien n'est supprimé — le récit change de place                                                                    |
| Q-4 | `programmes-officiels/` hors du skill (C-13) : lot dédié, tout de suite, ou jamais ?               | ✅ **lot 5 optionnel, APRÈS le lot 2** — le gate `harness:check --corpus` protège alors le déplacement au lieu de le subir. Ordre non négociable : ce registre est le garde-fou anti-double-transcription, et un faux « rien à faire » y est le pire résultat possible                                                                                        |

| Q-5 | **Cinq cycles CI pour une PR** (C-14) : file de merge, CI en deux étages, ou on l'accepte ?        | ✅ **l'accepter, et le mesurer** (arbitré le 2026-09-04). Livré en arena#982 : `actions:census` rend les têtes par branche et nomme la plus relancée. Le raisonnement retenu  : le moteur est **public**, donc ses minutes sont gratuites — le coût réel est du temps de file, pas de la facture ; et la règle « à jour avant de merger » est saine, c'est elle qui empêche un merge sémantiquement cassé. On rouvrira sur un chiffre. La file de merge est à vérifier sur un compte Free (les rulesets n'y sont déjà pas disponibles au privé), et découper le gate en deux étages toucherait à ce que cette étude s'est interdit de fragiliser. Le coût réel est du **temps de file**, pas de la facture : le moteur est public, donc ses minutes sont gratuites — au privé, le même défaut se paierait |

## 10. Journal d'exécution

- **2026-09-04, seconde moitié — l'étude est livrée en entier.** Neuf PR de plus (arena#980 à
  #984, privé#344 à #346), et trois choses qu'aucune relecture n'aurait données :
  - **La suppression du besoin l'a emporté sur la demande au propriétaire.** Q-1 avait été
    tranchée en faveur du PAT ; le jeton n'est pas venu, et plutôt que d'attendre, la question a
    été **rouverte** avec la doctrine du dépôt comme argument — l'échelle de traitement de
    `zero-intervention.md` place « supprimer le besoin » AU-DESSUS de « remonter ». Le repli
    (retirer `opened` des déclencheurs) supprime les fantômes à la racine sans secret à créer ni
    à renouveler dans un an. **Constaté dans les deux sens en une heure** : la PR #343 portait
    trois runs `pull_request` en `failure` à zéro job, la #344 aucun.
  - **Une correction qui ne tient qu'à la mémoire n'en est pas une.** Sans `types:`, GitHub
    réécoute `opened` par DÉFAUT : l'oubli était le comportement le plus facile. D'où un
    invariant de `harness:check --corpus` qui fait échouer la CI si un workflow du corpus le
    réécoute — éprouvé dans les deux sens contre le vrai corpus, comme le lot 2 l'avait exigé
    avant de supprimer `pin-check`.
  - **Une déviation assumée d'un ADR validé.** D-1 demandait de retirer les heuristiques « zéro
    job » en même temps que leur cause. Elles restent : dans `auto-pr` ce n'est pas une
    heuristique anti-fantôme mais la décision « faut-il dispatcher ? » (sans elle C-4 revient),
    et dans `guard-watch` elle coûte un appel d'API par rouge pour que l'alarme dise vrai si
    quelqu'un remet `opened`. Retirer un filet parce que sa cause est absente est le geste
    exact de #291, qui a gelé la chaîne une journée.

  **Le lot 5 a coûté dix fois ce que l'étude annonçait, et c'est le plus instructif.** C-13
  parlait de « quatre scripts du moteur ». Le relevé réel : **3** copies du chemin dans le
  moteur, **12** skills, **8** études, 2 workflows, le `CLAUDE.md` — et surtout **151 citations
  de provenance dans `content/**/chapter.json`**, invisibles depuis l'audit. Ce qui a rendu le
  lot faisable sans risque tient en une vérification : le SQL émis par `content:emit` avant et
  après le déplacement est **identique octet pour octet** (118 fichiers, même SHA-256). Sans
  elle, ce lot aurait ouvert une issue `content-drift` sur des dizaines de matières et exigé un
  dispatch humain d'`apply-content` — pour rien. Le déplacement s'est fait en **trois temps**
  (résolution additive → déplacement → retrait du chemin de compatibilité), la discipline
  « additif d'abord » de la DoD §7 appliquée à un arbre de fichiers.

  **Ce que la livraison a encore appris sur les gates eux-mêmes** : `typecheck` ne voit aucun
  script (C-15), découvert par un `ReferenceError` que `tsc` aurait dû attraper. Troisième
  membre d'une famille que cette étude n'a cessé de croiser — un gate qui ne mesure pas ce
  qu'il annonce (C-7, C-8, C-15).

  _Deux gestes de session à ne pas reproduire_ : `--force-with-lease` échoue sur une branche
  distante **supprimée** après un squash-merge (il faut une poussée simple, et la référence
  locale périmée fait croire à une divergence qui n'existe pas) ; et deux poussées concurrentes
  se bloquent mutuellement, le hook `pre-push` relançant le gate complet sur le même checkout —
  il a fallu en tuer une paire. C'est la raison d'être de la recommandation « un worktree par
  session parallèle » du `CLAUDE.md` du moteur.


- **2026-09-04 12:06 UTC — Les deux dernières PR sont mergées** (arena#975, privé#342) : tout ce que
  cette étude pouvait livrer sans le PAT est **dans `main` sur les deux dépôts**. Ce que la mise au
  merge a appris, et qui ne se lisait sur aucun diff :
  - **C-14, un troisième gisement de runs**, découvert en regardant une PR de cette étude peiner à
    entrer : rester à jour avec `main` relance la CI en entier, cinq fois ici. L'audit du 2026-09-03
    ne pouvait pas le voir — ce jour-là `main` était calme. Un audit mesure la journée qu'il mesure.
  - **`audit:deps` a rendu un 503 du registre npm**, cinq minutes de tentatives, et a fait échouer
    `verify` sur la tête `82146fb1`. Le dépôt documente ce gate comme non hermétique ; ce qui a
    **tranché** n'est pas cette documentation mais un fait : la CI de `main` butait au même instant
    sur le même appel. Un rouge se dit étranger à une PR quand la **base** le porte aussi, jamais
    parce qu'on connaît le défaut. Le registre est revenu de lui-même à 12:01 ; la relance manuelle
    n'a jamais eu à être dépensée, la re-synchronisation de branche ayant relancé la CI d'elle-même.
  - **La garde `guard-watch` du privé a tenu une issue `garde-rouge` (#338) sur un run à 1 job** —
    un vrai rouge de `roadmap-sync`, sur une branche de cette étude, avant que la roadmap ne connaisse
    les lots livrés. Elle n'a **pas** alarmé sur les fantômes de la même fenêtre. C'est le premier
    déclenchement réel du test « zéro job » depuis qu'il est le critère, et il a trié dans le bon sens.

- **2026-09-04 — Lots 2, 3a et 4 livrés (arena#971, #974, #975, privé#342).** Ce que l'exécution
  a appris, et que l'audit n'avait pas vu :
  - **Les invariants du moteur et ceux du corpus ne peuvent pas cohabiter dans une même
    invocation.** Trouvé par la CI au PREMIER appel réel de `--corpus` : la Content CI privée
    branche les 43 skills du corpus par symlink dans `engine/.claude/skills` — c'est sa raison
    d'être — et dans ce décor l'invariant « chaque vue générée est à jour » a réclamé **225
    fichiers de miroir** qui n'ont aucune raison d'exister. La recette LOCALE tombe dans le même
    trou. Reproduit dans les deux sens : 188 constats avec le corpus branché, zéro après.
  - **Une sonde muette doit valoir « dispatch », pas « c'est bon ».** Le filet de D-3 écrivait
    `|| echo 1` : une API qui ne répond pas faisait compter le run comme réel, donc supprimait le
    filet **précisément le jour où il sert**. Trouvé par un banc d'essai avec un faux `gh`, pas
    par relecture. Même polarité que le corpus, et l'INVERSE de `guard-watch`, où un run de jobs
    inconnus doit rester rouge — la même ligne de shell veut dire deux choses opposées selon ce
    qu'on garde.
  - **L'auto-merge du privé comptait les check runs remplacés par une relance** : une PR passée
    au rouge une seule fois ne pouvait plus jamais merger sur ce commit. Le seul contournement
    aurait été un commit vide, c'est-à-dire le geste que la DoD interdit. Corrigé dans privé#342,
    la PR qu'il bloquait. Le moteur n'a pas ce défaut (auto-merge natif, arbitré par GitHub).
  - **Le premier passage du gate sur le corpus a sorti 3 constats, tous vrais, zéro faux positif**
    sur 38 occurrences d'Unicode invisible : deux descriptions hors spec (1 202 et 1 157) et un
    BOM en tête d'un programme officiel. Les tolérances devaient être **contextuelles** — liant
    d'emoji, marques RTL en texte arabe — jamais par fichier ni par plage.
  - **Deux cibles de plus étaient fausses**, corrigées ci-dessus au §1.3 : « ≤ 60 règles »
    (mauvais compte, et mauvaise mesure) et « ≤ 200 lignes » pour AGENTS.md (214, le reste étant
    irréductible sans perte). Avec les deux du lot 1, **cinq des KPI de cette étude ont été
    rectifiés par les livraisons elles-mêmes**. C'est le fonctionnement voulu : un audit qui
    n'est pas exécuté se croit exact.
  _Geste de session à ne pas reproduire_ : un `--force-with-lease` a écrasé le correctif du mode
  corpus, non mergé, parce que le diff qui devait prouver « déjà mergé » a été lu à l'envers.
  Rétabli par cherry-pick. La leçon est celle du dépôt : **une livraison se constate, elle ne se
  déduit pas d'un diff qu'on interprète**.

- **2026-09-04 — Lot 1, moitié moteur livrée (arena#970).** Les deux décisions qui ne dépendaient
  d'aucun jeton : **D-4**, la condition de job de `second-opinion.yml`, et **D-11**,
  `scripts/ci/actions-census.mjs` (+ 18 tests). Le garde a skippé en zéro seconde dès le premier
  run de la PR elle-même — la preuve est arrivée sur le diff qui la produisait.
  **Deux chiffres de cette étude étaient faux, et la livraison les a corrigés** :
  - la cible « 0 run » pour le garde dormant **n'était pas atteignable** : un `if:` de job supprime
    le runner et le clone, pas la LIGNE du run (job `skipped`). Seul un filtre de déclencheur le
    ferait, et il est écarté depuis le lot L5 de l'étude « IA → déterministe ». Le KPI dit
    désormais ce qui se mesure : **runners alloués** ;
  - « 9,7 runs par branche » remplace le « ≈ 8,4 » du §1.3 : celui-ci divisait 800 runs par
    95 *pushes*, le script divise les runs des branches hors défaut par le nombre de **branches**.
    Deux définitions défendables, une seule doit faire foi — c'est celle du script, puisque c'est
    lui qui rejouera la mesure.
  **Ce que le relevé de la PR a montré en passant** : sur cette PR du moteur, `verify`, `CodeQL` et
  les deux checks de migration ont tourné **en double** — le run natif et celui qu'`auto-pr`
  dispatche sans regarder si le premier existe. C-4 vu en direct, sur le diff d'une étude qui le
  décrit. Le lot 3 le ferme.
  ⚠️ **Ce qui n'est pas prouvé** : le chemin réseau du recensement (`gh api`). `gh` était absent de
  la session ; les 18 tests couvrent les fonctions pures et `--from` a rejoué les dumps réels, à
  l'identique des tableaux du §2.2. Le vérifier est le premier geste de qui l'utilisera.

- **2026-09-04 — Validation.** Les quatre questions ont été posées **une par une** à Mohamed, avec
  leurs contreparties chiffrées ; **les quatre réponses suivent la recommandation** (§9). Statut
  passé à `validée`. Deux d'entre elles appellent une **valeur**, pas une décision, et l'attendre
  n'arrête rien : le PAT de Q-1 (que la session posera elle-même) et les deux nombres de
  facturation de Q-2. Le lot 5 (C-13) entre au plan, explicitement **après** le lot 2. Aucun ADR du
  §4 n'a eu à être révisé — comme pour l'étude 25, les décisions encodaient déjà le chemin retenu.

- **2026-09-03 — Audit et rédaction.** Relevé sur les deux dépôts (800 + 795 runs, 8 pages d'API
  chacun), gates chronométrés, 48 frontmatters parsés en YAML, `check.mjs` rejoué sur le privé, bug
  C-7 reproduit (annexe B), churn sur `origin/main` approfondi. Tout ce qui est écrit « mesuré » l'a
  été dans la session ; deux chiffres sont **estimés** et dits tels : les minutes facturées (§2.2,
  Q-2) et le nombre de PR ouvertes (déduit des `pull_request:opened`). Statut `brouillon` : rien
  n'est exécuté avant Q-1.

---

## Annexe A — Compteurs bruts utiles à la remesure

- Privé, fenêtre 2026-08-28 21:46 → 2026-09-03 21:12 : 800 runs ; `failure` à zéro job : Content CI 52,
  Pin check 51, Automerge 51, Roadmap sync 13 (= 167) ; Content CI `failure` réels : 6 (5 dispatch, 1 push).
- Moteur, fenêtre 2026-08-30 11:32 → 2026-09-03 21:10 : 795 runs ; `workflow_dispatch` d'auto-pr :
  38 par workflow requis ; `second-opinion` : 71.
- Durées témoin (jobs) : Pin check 10 s (run 33806502637), Automerge 9 s (33806678119), Content CI
  33 s (33806625988 : checkouts 4 s, npm ci 11 s, cinq gates 8 s, réveil 2 s).
- Skills : privé 43 (SKILL.md de 50 à 319 l., descriptions 34 047 caractères cumulés, 2 > 1 024) ;
  moteur 5 (3 212 caractères). `content-ecole-tn/references` : 12 Mo / 130 fichiers.
- Instructions : `AGENTS.md` 250 l. / 24 184 o ; `CLAUDE.md` privé 116 l. / 9 213 o ; `STATUS.md`
  514 l. / 225 722 o ; `docs/agents/` 2 825 l.
- Politique : 92 allow (gates 14, content-pipeline 7, tooling 5, db-readonly 3, git-readonly 12,
  git-write 7, gh-write 9, repo-config 4, repo-scripts 2, gh-readonly 9, ops-dispatch 20), 8 deny,
  `$comment` 7 326 caractères.
- Gates locaux (Node 22, Linux) : eol 0,27 s · leak 0,17 s · chain 0,23 s · harness 0,28 s ·
  perf 0,39 s · lint 24 s · typecheck 26 s · test 115 s (319 fichiers, 3 922 tests).

## Annexe B — Reproduction de C-7

```js
import { checkSkillFrontmatter } from "./scripts/harness/check.mjs";
const twoLines = "name: x\ndescription: >-\n  " + "a".repeat(500) + "\n  " + "b".repeat(900);
checkSkillFrontmatter("x", twoLines); // → []  (1 400 caractères, aucune violation)
const oneLine = "name: x\ndescription: >-\n  " + "a".repeat(1100);
checkSkillFrontmatter("x", oneLine); // → ["description is 1100 chars > spec max 1024"]
```

Cause : `/^description:\s*(?:>-|>|\|-|\|)?\s*\n?([\s\S]*?)(?=\n[a-zA-Z-]+:|$)/m` — en mode `m`,
`$` matche chaque fin de ligne ; la capture paresseuse s'arrête à la première. Correctif :
`parse(frontmatter).description` avec le paquet `yaml` déjà importé par l'invariant 8.
