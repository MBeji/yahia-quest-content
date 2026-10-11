# Étude 37 — Le harness en boucles : de l'événement qui tire à la boucle qui converge

> **Statut** : **brouillon** — rédigée le 2026-10-11 depuis une session cloud, sur un relevé
> du jour (§2) ; passe `validée` quand Q-1 (où tournent les têtes d'agent) est arbitrée, les
> lots L0 à L3 ne dépendant pas de cette réponse peuvent démarrer avant.
> **Priorité** : 37 · **Valeur** : 🔁 chaque mécanisme autonome du harness — la garde après push
> (DoD §8), les quatre gardes planifiées, la routine hebdomadaire — devient une **boucle de
> réconciliation** : observer l'état réel, agir, re-observer, sortir sur une **preuve de contenu**,
> sous **budget** — au lieu d'un événement qui tire une fois et oublie. Concrètement : une PR de
> garde est menée au merge au lieu de s'empiler (six ouvertes aujourd'hui, aucun lot mergé depuis
> le 2026-07-31), une tête d'agent refusée est **nommée** en six heures au lieu de cinq jours de
> rouges identiques, et une routine morte se voit depuis le dépôt · **Complexité** : moyenne —
> trois scripts déterministes testés, un skill, deux retouches de workflow, un registre et un
> invariant de `harness:check` ; aucun impact runtime produit, aucune migration
> **Architecte** : session Claude Code, 2026-10-11 · **Exécuteur cible** : Sonnet (ou équiv.) —
> lots courts, outillage et docs ; L1 et L2 demandent de lire `docs/agents/gardes.md` en entier
> **Dépend de** : é25 (harness déclaratif, `harness:check`, `harness/*.json`) · é32 (gardes
> partagées, `actions:census`, `guard-watch.mjs`) · étude cloud-first lot 5 (abonnement PR +
> réveil différé, `passation.md` §7.10) · étude « IA → déterministe » (pré-gates, hook
> déterministe) · **Bloque** : la clôture de l'étude cloud-first (son arbitrage « porter les
> gardes en routines » est repris ici, Q-1) ; #1002 (jeton des gardes) reçoit sa réponse ici
> **Docs normatifs liés** : `AGENTS.md` (DoD §8, Execution policy), `docs/agents/gardes.md`,
> `docs/agents/zero-intervention.md`, `docs/passation.md` §7, `docs/agents/collaboration.md`,
> `docs/ci-cd-and-branch-protection.md`, `harness/policy.json`, `harness/controls.json`
>
> **Fiche de verticalité** (doctrine verticale, é26 D-2) : **Verticale** : fondation (harness) —
> hors de l'arbre de décision par construction (`docs/doctrine-verticale.md` §4, « les deux cas
> qui ne passent pas par l'arbre ») · **Maturité visée** : M3 · **Boucles** : l'étude ne fait
> **que** refermer — (a) la garde après push, restée une **discipline de prose** depuis le lot 5
> de l'étude cloud-first (2026-09-05) et qu'aucune commande ne porte ; (b) les PR que les gardes
> ouvrent **sans après** : six PR de dépendances ouvertes, quatre en conflit, zéro mergée depuis
> 72 jours ; (c) l'horloge sans relève (STATUS.md L-8) : la seule routine cloud est morte depuis
> au moins le 2026-10-05 et rien dans le dépôt ne pouvait le dire. Consommateurs datés : toute
> session qui pousse (L1, dès son merge), les gardes (L2-L3), la clôture de session (L4) ·
> **Apport IA** : **rejeté pour le contrôle des boucles** — ce qui observe, compare et décide
> de sortir est un script (le déterministe décide, le LLM agit, é26 §5 et étude
> « IA → déterministe ») ; **retenu là où il est déjà** : le jugement sur l'action (gate rouge,
> triage, major) — l'étude ne déplace aucun jugement vers un script et n'en confie aucun nouveau
> à un modèle.

## 0. TL;DR

**Ce qu'on appelle « logique de loop ».** Une boucle, ici, n'est pas une commande qui se répète
toutes les N minutes. C'est une **boucle de réconciliation** : un mécanisme qui **observe l'état
réel** (le contenu de `main`, les check-runs d'une PR, la file des signalements, le dernier run
d'une routine), le **compare à l'état voulu**, **agit** de façon idempotente, **re-observe**, et
ne s'arrête que sur une **preuve** — jamais sur un statut — ou sur un **budget** épuisé, qu'il
dit alors à voix haute. Le déclencheur (un cron, un événement GitHub, un réveil) ne dit **que
quand regarder, jamais quoi regarder**. Le dépôt a déjà écrit cette règle, une fois, pour un
seul workflow (`automerge.yml` du privé, 2026-08-16 : « ÉTAT, PAS ÉVÉNEMENT ») ; cette étude
l'applique à tout ce qui tourne seul.

**Ce que le relevé du 2026-10-11 a mesuré** (§2, API GitHub et API des sessions cloud, pas de
souvenir) :

| #   | Constat                                                                                                                                                                                                                                                         | Mesure                                                                                                                           | Remède (lot)                                                                      |
| --- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| C-1 | **Du 4 au 9 octobre, aucune tête d'agent n'a tourné** — les trois gardes du moteur, la garde du corpus et la routine cloud ont toutes été refusées par le même message, « _Your organization has disabled Claude subscription access for Claude Code_ » — et **le dépôt ne le savait pas** | 17 runs rouges consécutifs de `report-triage` (5 j 1 h), 2 lots `upgrade-guard` en draft, 1 audit privé rouge, 1 routine `ACCESS_DENIED` ; la cause trouvée le 11/10 **dans un journal de job**, écrite nulle part | la garde des gardes **nomme la cause** et compte la série (L3) ; Q-1              |
| C-2 | Les gardes ouvrent des PR **sans après** : un lot patch/minor par jour, jamais mené au merge, chacun entrant en conflit avec le précédent                                                                                                                       | **6 PR de dépendances ouvertes** (#1111, #1128, #1135, #1153, #1157, #1158), 4 `needs-rebase`, 2 drafts `needs-review`, **dernier lot mergé le 2026-07-31** | un seul lot ouvert à la fois, le lot du jour **remplace** celui d'hier (L2)        |
| C-3 | La garde après push (DoD §8) est une **discipline de prose** : `passation.md` §7.10 dit « abonnement + réveil différé ~45 min », aucune commande, aucun skill, aucun script ne la porte ; chaque session la réinvente, et `collaboration.md` documente déjà la boucle `until` qui annonce un faux merge | 0 skill, 0 script ; 1 mention de `send_later` dans tout le dépôt                                                                  | le skill `/garde-pr` + l'observateur `pr-state.mjs` (L1)                           |
| C-4 | **La routine porte son savoir hors dépôt** : son prompt de 2 400 caractères (la procédure entière de re-sonde) vit dans claude.ai, pas dans un skill — à rebours de la règle 3 des gardes (« le savoir vit dans le skill, versionné ») — et sa panne n'est visible d'aucun workflow | 1 routine, `last_run` = `FAILED` ; `list_sessions` **exclut** les sessions de routine : le dépôt ne peut même pas compter ses runs | le skill `status-resonde` ; toute clôture de session relève `list_triggers` (L4)  |
| C-5 | Les primitives de boucle de l'outil (`/loop`, `ScheduleWakeup`, `CronCreate`, `Monitor`, `send_later`, `create_trigger`, `subscribe_pr_activity`, hook `Stop`) ne sont **nommées nulle part** dans le harness, avec leurs limites (60 s–1 h par tick, 7 jours, 30 min, « ne tire que session inactive ») | 0 occurrence dans `AGENTS.md`, `docs/agents/`, `harness/`                                                                          | `docs/agents/boucles.md` + registre `harness/loops.json` (L0)                     |
| C-6 | **22 horloges**, toutes des événements : 16 crons au moteur, 6 au privé ; seules trois surfaces raisonnent par état (`automerge`, `guard-watch`, les gardes « à issue » de 2026-09)                                                                                 | 22 `schedule`, 3 réconciliateurs                                                                                                   | le contrat de boucle, déclaré par mécanisme (L0), et vérifié (`harness:check`)    |
| C-7 | `STATUS.md` ment depuis 13 jours (#1126, 63 PR de retard) : la garde qui **mesure** la dérive existe, celle qui devait la **corriger** (la routine) est morte, et personne ne relie les deux                                                                      | issue `status-perime` ouverte le 2026-09-28, routine en échec                                                                      | la re-sonde devient un skill jouable par toute session ; Q-4                       |
| C-8 | Une boucle sans sortie coûte : `passation.md` §7.11 a mesuré ~100 $ de sessions filles tournant après livraison (2026-09-20), et le relevé du jour compte **29 sessions filles** sur les 100 dernières                                                              | 29/100 sessions d'origine `claude_code_mcp_seed`                                                                                   | budget et sortie obligatoires pour toute boucle, archivage au merge (D-7)         |
| C-9 | Le mur du classifieur est **aussi** un mur de boucle : pendant la rédaction de cette étude, quatre commandes **en lecture seule et `allow` dans `policy.json`** (`sed -n`, `git ls-remote`, un `python3` de dépouillement) ont été refusées en mode auto                      | 4 refus en 15 min, le 2026-10-11 vers 17:40 UTC                                                                                   | une boucle n'insiste jamais sur un refus : elle le nomme et change d'outil (D-8)   |

**Ce que l'étude ne fait pas** : elle ne remplace pas GitHub Actions par des sessions qui
tournent en permanence (une VM qui attend coûte et se fait récupérer) ; elle ne confie aucun
jugement nouveau à un modèle ; elle ne rouvre ni l'étude 32 (volume de la chaîne) ni l'option C
du 2026-09-05 (tout est autorisé) ; elle ne « relance » rien à l'aveugle — une boucle qui
rejoue un rouge sans l'avoir compris est un cron avec un autre nom.

## 1. Contexte & objectif

### 1.1 Ce que « loop » veut dire ici, et ce que ce n'est pas

Trois mots suffisent, et ils sont déjà dans le dépôt :

- **Observer** — lire l'état **réel**, par une commande, jamais par un champ de statut
  (`passation.md` §7.1 : le merge se constate au contenu de `main`, `gardes.md` § « le vert qui
  ne prouve rien » : on lit la conclusion de l'**étape** qui fait le travail, pas celle du run).
- **Réconcilier** — comparer à l'état voulu et agir de façon **idempotente** : rejouer l'action
  sur un état déjà bon ne change rien (`apply-content` l'est ; `guard-watch` l'est : une seule
  issue, réutilisée).
- **Sortir** — sur une preuve, ou sur un budget épuisé, et le dire. Une boucle qui ne sait pas
  quand s'arrêter est le mode de panne le plus cher du harness (C-8).

Ce que ce n'est pas : un `while true` qui interroge une API toutes les trente secondes (la
règle de `collaboration.md` sur les boucles `until` qui sortent sur une réponse vide reste
entière) ; une session laissée ouverte « au cas où » ; un cron de plus. Et ce n'est pas non plus
une rupture : les pré-gates déterministes de l'étude « IA → déterministe » **sont** la moitié
« observer » d'une boucle — il leur manque l'autre moitié, l'**après** : ce que devient ce que
la garde a produit.

### 1.2 Ce que le harness est aujourd'hui : une chaîne d'événements

Les cinq couches de l'étude 32 §1.1 n'ont pas bougé. Ce qui tourne **seul**, et comment :

| Mécanisme                                                 | Déclencheur                                          | Ce qu'il fait d'un état déjà traité                                                          | Ce qu'il fait de sa propre sortie                                                   |
| --------------------------------------------------------- | ---------------------------------------------------- | -------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `auto-pr` → `automerge` (moteur)                          | `push`, `pull_request`, `push: main`                 | ✅ réconcilie (réarme, met à jour une tête en retard, pose `needs-rebase` sur conflit)        | — (c'est lui l'après des autres)                                                    |
| `automerge` (privé)                                       | `workflow_run`, `pull_request`, `push: main`         | ✅ « état, pas événement » : chaque réveil balaie **toutes** les PR ouvertes                   | —                                                                                   |
| `regression-guard`, `upgrade-guard`, `report-triage`      | cron 2×/sem., `workflow_run` du nightly, cron 4 h    | ✅ pré-gate déterministe (skippe à vide)                                                      | ❌ ouvre une PR ou une issue et **s'arrête** ; la PR du jour ignore celle d'hier     |
| `content-audit` (privé)                                   | cron 2×/sem.                                         | ✅ pré-gate                                                                                   | ❌ idem                                                                             |
| `guard-watch` (les deux dépôts)                           | cron 6 h                                             | ✅ une issue réutilisée, refermée seule                                                       | l'issue dit « N runs rouges », **jamais pourquoi**                                 |
| `status-freshness-watch`, `pat-expiry-watch`, `content-drift`, `client-errors-watch`, `freeze-watch` | cron                     | ✅ gardes « à issue » : rougissent sur un état, se referment sur un état                      | personne n'a la charge de refermer la boucle qu'elles ouvrent                       |
| La routine « re-sonde hebdomadaire de STATUS.md »          | cron claude.ai, lundi 07:00 UTC                       | ✅ ne pousse que si le topo a dérivé                                                          | ❌ en échec ; invisible du dépôt                                                    |
| La garde après push (DoD §8)                               | la session elle-même                                 | prose (`passation.md` §7.10) : abonnement + réveil différé                                   | outillée par rien                                                                   |
| La campagne de contenu (`/campagne` §5 « Boucler »)        | la session                                           | ✅ re-établit l'état des lieux après chaque merge, **redemande** l'humain                      | ✅ c'est la seule boucle complète du harness — et elle est humaine à chaque tour     |

Vingt-deux crons (16 au moteur : `ai-pilot-report`, `checkpoint-tag`, `client-errors-watch`,
`codeql`, `db-backup`, `db-migrate-prod`, `engagement-report`, `freeze-watch`, `guard-watch`,
`nightly`, `pat-expiry-watch`, `regression-guard`, `report-apply`, `report-triage`,
`status-freshness-watch`, `tutor-digests` ; 6 au privé : `content-audit`, `content-drift`,
`guard-watch`, `manuel-health`, `roadmap-sync`, `video-health`), et trois seulement
qui **raisonnent par état**.

### 1.3 Les primitives de boucle disponibles, avec leurs limites

Toutes documentées par l'outil dans la session qui rédige ; celles marquées « mesuré » ont été
constatées le 2026-10-11.

| Primitive                                            | Ce qu'elle fait                                                                                                                 | Horizon          | Où vit l'état entre deux ticks                  | Limite à connaître                                                                                                                              |
| ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ----------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `/loop` sans intervalle → `ScheduleWakeup`           | la session se réveille elle-même après un délai qu'elle choisit ; `noop: true` compacte les ticks vides dans la vue de l'utilisateur ; `stop` termine | minutes → heures | la conversation (cache de prompt : 1 h)          | délai **borné à [60 s, 3 600 s]** ; chaque tick est un tour de modèle ; ne survit pas à la session                                               |
| `/loop 5m …` → `CronCreate`                          | un cron **en mémoire de session**, qui ne tire que **session inactive**, jitter ≤ 10 %                                            | heures → jours   | la conversation                                 | **expire après 7 jours** ; rien n'est écrit sur disque ; perdu avec la session                                                                   |
| `Monitor`                                            | un script bash dont chaque ligne de sortie **réveille** la session (ou un websocket)                                             | ≤ 30 min par armement | le script                                   | re-armer à l'expiration ; polling ≥ 30 s sur une API distante ; « le silence n'est pas un succès » — le filtre doit émettre aussi sur l'échec |
| `send_later`                                         | un réveil **unique** dans cette session, granularité 1 min ; **survit à la récupération de la VM** (re-provisionnée, conversation restaurée) | heures → jours   | la session restaurée                            | mesuré : posé à 17:33 UTC pour 17:37, journal §10 ; un réveil n'interrompt pas un tour en cours                                                  |
| `create_trigger` (routine)                           | cron ≥ 1 h ou date unique, dans **cette** session, une **autre**, ou une session **neuve** ; notification push/e-mail            | jours → semaines | hors dépôt (claude.ai)                          | **mesuré : `ACCESS_DENIED` le 2026-10-05** (C-1) ; créée depuis une session, elle part **sans connecteurs** (lot 5 cloud-first) ; `list_sessions` n'affiche pas ses runs |
| `subscribe_pr_activity`                              | les événements GitHub d'une PR (checks, revues, merge) réveillent la session                                                    | durée de la PR   | GitHub                                          | exige l'app GitHub « Claude » sur le dépôt ; **une seule session** abonnée par PR                                                                 |
| `watch_url`                                          | un webhook entrant réveille la session                                                                                          | durée de la session | —                                            | se termine avec la session                                                                                                                       |
| Hook `Stop` de Claude Code                           | un script peut **refuser la fin du tour** (`decision: block`, avec une raison) tant qu'une condition tient                       | le tour          | le script (il relit l'état réel)                | `stop_hook_active` évite qu'il boucle sur lui-même ; **sans budget, il piège la session** — c'est une arme, pas une commodité                     |
| GitHub Actions `schedule` / `workflow_run` / `repository_dispatch` | horloge calendrier, runner neuf à chaque run                                                                         | jours → semaines | les objets GitHub : PR, issue, label, marqueur  | un run **ne peut pas attendre** : il observe, agit, sort ; au privé chaque job coûte une minute entamée (é32)                                     |

La règle de placement qui en découle (D-2) : une boucle vit sur l'horloge la **plus courte**
dont l'horizon couvre sa sortie, et son état vit **toujours dans un objet GitHub** — jamais dans
la mémoire d'une session (règle « aucune mémoire latérale », AGENTS.md § Multi-agent).

### 1.4 Objectif & indicateurs

Objectif : **tout ce qui tourne seul sait dans quel état il est, ce qu'il attend, et quand il a
fini** — et le dit.

| KPI                                                                      | Aujourd'hui (2026-10-11)                                                       | Cible                                                                           | Relevé                                                   |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------- | -------------------------------------------------------- |
| K-1 PR de garde ouvertes sans suite (`dependencies`)                     | **6**, dont 4 en conflit entre elles                                           | ≤ 1 (le lot courant), jamais deux lots patch/minor ouverts                       | `actions:census --lots` (L5), à la main avant            |
| K-2 Délai lot patch/minor → merge, quand le gate est vert                | **aucun merge depuis le 2026-07-31** (72 j)                                     | ≤ 48 h                                                                          | idem                                                     |
| K-3 Durée d'une série de rouges identiques **sans cause nommée**         | **5 j 1 h** (17 runs, C-1)                                                      | ≤ 6 h (la fenêtre de `guard-watch`), la cause dans l'issue                       | corps des issues `garde-rouge`                           |
| K-4 Sessions qui poussent une PR **sans** garde outillée                 | 100 % (aucun outil)                                                            | 0 % des sessions de ce dépôt après L1 (le skill est le chemin)                   | `passation.md` §7 relue à chaque clôture ; journal       |
| K-5 Routines dont l'échec est **visible depuis le dépôt**                | 0 / 1                                                                           | 1 / 1 (relevé en clôture de session, L4)                                         | rapports de clôture                                      |
| K-6 Mécanismes autonomes avec contrat de boucle déclaré                   | 0 / 11 (§1.2)                                                                   | 11 / 11 dans `harness/loops.json`, gaté                                           | `harness:check`                                          |
| K-7 Jours de `STATUS.md` périmé (issue `status-perime` ouverte)           | **13 j** (#1126)                                                                | ≤ 7 j (routine ou session, L4 + Q-4)                                              | `status-freshness-watch`                                 |

## 2. État des lieux mesuré (2026-10-11)

### 2.1 Méthode de relevé

Depuis la session cloud qui rédige (environnement `env_01GaviMQRVhZ2iCdSMDPhKSW`, le même que
celui de la routine en échec) : l'API GitHub par le serveur MCP (`actions_list`,
`get_job_logs`, `list_pull_requests`, `list_issues`, `search_pull_requests`), l'API des
sessions cloud (`list_triggers`, `get_session`, `list_sessions`), et le dépôt (`git`,
`harness/*.json`, les workflows). Pas de `gh` en cloud ; `actions:census` ne peut donc pas
tourner ici (son chemin `--from` rejoue un dump, qui ne porte pas le compte de jobs).

Ce que le relevé **ne peut pas** voir, dit avant les chiffres : l'historique d'une routine
(seul `last_run` est servi), le nombre de ses runs (`list_sessions` exclut les sessions
déclenchées par une routine, « same as the REST default »), et la date d'expiration du jeton
OAuth (#1002). Les tableaux bruts sont en annexe A.

### 2.2 Les gardes agent, run par run

**`regression-guard`** (lun. + jeu. 23:00 UTC) — 20 derniers runs, du 2026-08-04 au 10-09 :
12 `success`, 8 `failure`. Sur les 12 verts, **7 sont des skips du pré-gate** (0,2–0,4 min) et
5 de vrais balayages (4–14 min). Sur les cinq dernières semaines : balayages le 09-04 (rouge,
6,9 min), 09-15 (rouge, 6,5), 09-18 (vert), 09-22 (vert), 10-02 (rouge, 9,1 min, « _failed at
the Claude level: (no message)_ ») ; skips le 09-11, 09-25, 09-29, 10-06, 10-09. **Dernier
balayage réussi : le 2026-09-22.** Un rouge coûte le balayage jusqu'au cron suivant, trois ou
quatre jours plus tard, sans reprise.

**`upgrade-guard`** (après chaque nightly) — 20 derniers runs, du 09-22 au 10-11 : 14 verts de
0,1–0,2 min (rien à faire, ou cadence non tirée — « le vert qui ne prouve rien »), et **6 rouges
qui sont exactement les jours de lot** : 09-22 (0,5 min), 09-25 (35,5), 09-29 (28,7), 10-02
(40,4 : le lot est vert, la PR #1153 ouverte à 07:04, puis l'agent tourne 32 min et le job sort
rouge « lot resté rouge »), 10-06 (9,8), 10-09 (7,9 : « _Your organization has disabled Claude
subscription access for Claude Code · Use an Anthropic API key instead, or ask your admin to
enable access_ », PR #1158 laissée en draft `needs-review`). **Chaque lot tenté depuis le 25
septembre a fini rouge**, et chaque lot a ouvert sa PR : #1111 (09-25), #1128 (09-29), #1153
(10-02, `mergeable_state: dirty`), #1157 (10-06, draft), #1158 (10-09, draft) — plus la major
Dependabot #1135 (09-29). **Dernier lot mergé : #684, le 2026-07-31.** `gardes.md` avait mesuré
« dix-huit jours sans lot appliqué » le 2026-09-22 ; on en est à soixante-douze.

Les quatre `needs-rebase` ne sont pas quatre conflits avec `main` : ce sont des lots qui
touchent le même `package-lock.json` les uns après les autres, puis une correction manuelle
(#1159, 2026-10-10) qui les met tous en conflit d'un coup. **Le garde n'observe jamais sa propre
sortie de la veille** : il ne sait pas qu'un lot est déjà ouvert, et `automerge` ne sait que
poser un label.

**`report-triage`** (cron 4 h) — 30 derniers runs, du 10-02 au 10-11 : 13 verts, **17 rouges
consécutifs du 10-04 14:09 au 10-09 15:22** (5 j 1 h), tous de 0,7–0,9 min : l'étape « _Run the
report-triage agent_ » échoue en **16 secondes**, après un export, un pré-gate et une résolution
de modèle verts. Puis le 10-09 à 21:01, le même workflow sur le même SHA tourne **23 minutes**,
l'agent triage et ouvre #1162. Rien n'a changé dans le dépôt entre les deux runs. La garde des
gardes a bien ouvert #1156 le 10-04 à 21:58 — « Gardes en échec (1 run(s) rouge(s)) », avec le
conseil générique sur les secrets — et l'a refermée seule le 10-10 à 06:25 quand la fenêtre est
redevenue verte. **Personne n'a agi**, et l'issue ne disait pas quoi faire : elle ne portait ni
l'étape en échec, ni le message, ni la longueur de la série.

**`content-audit`** (privé, mer. + sam.) — 15 derniers runs, du 08-27 au 10-11 : 12 verts, 3
rouges (09-03 ; 10-01, 11 min ; 10-04, 0,9 min — l'étape « _Run the content-audit sweep_ » morte
en 16 s, même signature que le triage). Le 10-11 à 00:53, 3,1 min, vert : l'agent tourne à
nouveau.

**La frise de l'incident**, reconstituée après coup — ce qu'aucun document du dépôt ne contient :

| Quand (UTC)      | Quoi                                                                                                    | Où c'est écrit                                        |
| ---------------- | ------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| 10-02 02:00      | `regression-guard` : « failed at the Claude level: (no message) »                                       | journal du job                                        |
| 10-04 00:31      | `content-audit` (privé) : étape agent morte en 16 s                                                      | journal du job, issue de suivi privée                  |
| 10-04 14:09      | `report-triage` : premier des 17 rouges                                                                 | #1156 (« 1 run rouge »)                               |
| 10-05 07:12      | routine STATUS.md : `ROUTINE_RUN_FAILURE_REASON_ACCESS_DENIED`, message explicite                        | `last_run` de la routine — visible d'une session seulement |
| 10-06 07:29      | `upgrade-guard` : rouge, PR #1157 en draft                                                              | journal du job                                        |
| 10-09 07:21      | `upgrade-guard` : le message explicite, PR #1158 en draft                                               | journal du job                                        |
| 10-09 21:01      | `report-triage` : l'agent tourne 23 min, vert ; l'accès est revenu                                       | run                                                   |
| 10-11 ~17:00     | la cause est nommée — par cette étude, en lisant un journal de job                                      | ici                                                   |

C'est le **mur « réglage hors dépôt »** de `zero-intervention.md`, et l'étude ne prétend pas le
lever (Q-1). Ce qu'elle refuse, c'est le délai : cinq jours pour une cause qui tenait dans une
ligne, écrite en clair dans le premier journal rouge.

### 2.3 La seule routine cloud

`trig_01EaY5ufvqscnUdYMU8NL1gi`, « Re-sonde hebdomadaire de STATUS.md », créée le 2026-09-06
depuis une session, cron `0 7 * * 1`, session neuve à chaque tir, notification push. Son
`last_run` : tiré le 2026-10-05 07:12, **`FAILED` / `ACCESS_DENIED`** en 19 secondes
(`post_turn_summary.status_detail` : le message de C-1). Son prompt — 2 400 caractères, la
procédure complète de re-sonde, avec ses règles de preuve — n'existe **que là**. Elle part sans
connecteur (`mcp_connections: []`) : même vivante, elle n'aurait pas les outils GitHub qu'elle
cite (le lot 5 de l'étude cloud-first l'avait noté et laissé au propriétaire). Pendant ce temps,
`status-freshness-watch` tient #1126 ouverte depuis le 2026-09-28 : **63 PR de retard**. La
garde qui mesure est vivante ; celle qui corrige est morte ; rien ne relie les deux.

### 2.4 La garde après push, telle qu'elle est écrite

`passation.md` §7.10 (lot 5 cloud-first) : « la session qui a poussé s'abonne aux événements de
sa PR et se pose un réveil différé (~45 min) ; le check-in constate le merge par le contenu de
`main` ». `collaboration.md` § Congestion ajoute : ré-identifier la PR à chaque contrôle, ne
jamais conclure sur un champ d'API, et traiter `null | "" | erreur` comme « continuer ». Tout
cela est juste — et **rien ne le porte** : pas de skill, pas de script, pas d'entrée dans
`controls.json`. Le `grep` du dépôt rend **une** occurrence de `send_later`. Une session qui
pousse applique ce qu'elle a lu, ou pas.

### 2.5 Ce qui est déjà une boucle, et ne bouge pas

- `automerge` (moteur) : réarme, met à jour les têtes en retard, pose `needs-rebase`. Le privé :
  « l'événement dit quand regarder, jamais quoi regarder » — chaque réveil balaie tout.
- `guard-watch` : une issue, réutilisée, refermée seule ; la décision dans un script partagé et
  testé (`scripts/ci/guard-watch.mjs`). Il lui manque le **pourquoi** (L3), pas la forme.
- Les gardes « à issue » du 2026-09 (`status-freshness-watch`, `pat-expiry-watch`,
  `content-drift`, `client-errors-watch`, `freeze-watch`) : un état, un seuil, une issue qui
  s'ouvre et se referme seule. Ce sont des observateurs parfaits ; il leur manque un **acteur**.
- Les pré-gates (`*-pregate.mjs`) et leurs trois invariants (le doute réveille, le manuel n'est
  jamais skippé, le script ne juge pas) : la moitié « observer » de chaque garde.
- `report-close.yml` : referme les signalements au merge de leur fix — la seule garde qui
  **consomme** la sortie d'une autre.
- `/campagne` §5 : re-établit l'état et redemande après chaque merge. Boucle complète, humaine à
  chaque tour, par doctrine (« l'humain choisit le couple »).

### 2.6 Le coût d'une boucle qui ne sort pas

`passation.md` §7.11 : trois sessions filles mesurées le 2026-09-20 tournant des heures après
le merge de leurs PR, ~100 $. Le relevé du jour : **29 des 100 dernières sessions** sont des
filles (`claude_code_mcp_seed`). La session qui rédige a coûté 7,63 $ en sept heures, pour
4,9 M de tokens lus en cache : un tick de boucle est un tour de modèle sur ce contexte — des
centimes, pas des dollars, mais 24 ticks par jour pendant sept jours ne sont pas gratuits. D'où
le budget de D-7, et la règle déjà écrite dans les consignes de garde de l'outil : trois
check-ins silencieux, puis on s'arrête et on le dit.

### 2.7 Le mur du classifieur, vécu pendant la rédaction

Entre 17:35 et 17:50 UTC, le classifieur d'auto-mode a refusé quatre commandes de cette session,
toutes en lecture seule et toutes `allow` dans `policy.json` : `sed -n` sur
`.github/scripts/check-claude-result.py`, `sed -n` sur `scripts/ci/report-triage-pregate.mjs`,
`git ls-remote origin 'refs/pull/*/head'`, et un `python3` qui dépouillait un fichier de
résultats. Les outils de lecture dédiés sont passés. Le mur est connu (`zero-intervention.md`) ;
ce qui est neuf, c'est sa conséquence pour une boucle : **un tick qui retente la même commande
refusée est une boucle infinie sur un mur**. D'où D-8.

## 3. Constats détaillés

### C-1 — Cinq jours sans tête d'agent, et un dépôt qui ne le savait pas

§2.2 donne la frise. Trois choses à retenir, chacune avec son remède :

1. **Le message était explicite dès le premier run** (« _Your organization has disabled Claude
   subscription access for Claude Code_ ») et `check-claude-result.py` le remonte en annotation
   `::error` du job. Mais `guard-watch.mjs` ne lit que la **conclusion** des runs : son issue
   dit « 1 run rouge », jamais l'étape ni le message. Dix-sept runs plus tard elle dit toujours
   « 1 run rouge » (fenêtre de 8 h). → L3 : l'étape en échec, sa première annotation et la
   **longueur de la série** entrent dans l'issue, et un message d'une classe connue (jeton,
   abonnement, 401) cite le mur qu'il désigne.
2. **Cinq mécanismes sont tombés sur la même cause, chacun dans son coin** : trois gardes du
   moteur, une du privé, une routine. Aucun ne sait que les autres existent. → L0 : le registre
   `harness/loops.json` nomme les têtes d'agent et leur support (`actions-oauth`, `routine`,
   `session`) ; L3 : `guard-watch` regroupe par **cause**, pas seulement par workflow.
3. **La cause est hors dépôt** et le reste (Q-1). Ce que la boucle change : le temps avant que
   quelqu'un sache **quoi** faire — de cinq jours à une fenêtre de garde — et ce qui se passe au
   retour de l'accès : aujourd'hui, les lots en draft et la routine attendent le prochain cron ;
   demain, le réconciliateur de L2 reprend le lot du jour, et la relève de L4 nomme la routine à
   relancer.

### C-2 — Des PR sans après

Le garde ouvre ; personne ne mène. `upgrade-guard.yml` ouvre **une PR par lot** sans regarder
si un lot est déjà ouvert ; `automerge` met à jour une tête en retard mais pose `needs-rebase`
sur un conflit et s'arrête là ; l'agent de réparation n'est réveillé que par le run du jour, qui
ne connaît que le lot du jour. Six PR, zéro merge en 72 jours, et chaque jour qui passe en
ajoute une — **un cron qui produit des PR est une boucle ouverte qui s'empile**.

Le remède n'est pas de relire ces six PR à la main (ce serait la validation manuelle que la règle
interdit), c'est de rendre le garde **idempotent sur sa propre sortie** (L2) : avant de produire,
il observe les lots ouverts ; un lot vert et non draft attend son merge, rien n'est ouvert à
côté ; un lot en conflit ou en draft est **remplacé** par le lot du jour, reconstruit depuis
`main` — à une condition stricte : **jamais fermer un lot qui porte des commits de l'agent**
(une réparation en cours, comme #1153 « réparé par l'agent »). Celui-là est repris, pas remplacé.

Q-2 porte le cas voisin des drafts de `regression-guard` (`draft/regression-guard-<date>`, #932
ouverte depuis le 2026-09-01) : un draft « à promouvoir par un humain » est une validation
manuelle au sens de `zero-intervention.md`.

### C-3 — Une garde après push en prose

La DoD §8 est la règle la plus citée du dépôt et la moins outillée. Ce que sait faire une
session cloud pour l'honorer est documenté en trois endroits (`passation.md` §7.10,
`collaboration.md` § Congestion, les consignes de garde de l'outil) et **vérifié nulle part** :
ni commande qui rend le verdict, ni skill qui enchaîne, ni invariant qui exige que la session
l'ait fait. Le prix se lit dans `collaboration.md` même : la boucle `until` qui sort sur une
réponse vide et annonce un faux merge, écrite par une session qui faisait de son mieux.

→ L1 : un observateur déterministe, `scripts/ci/pr-state.mjs`, qui rend **ce que git peut
prouver** (le merge par le contenu, la PR par le SHA de tête dans `refs/pull/*/head`, la tête à
jour ou non vis-à-vis de `main`) et laisse les check-runs à l'outil MCP ; et un skill
`/garde-pr` qui déroule la boucle : abonnement, ticks `ScheduleWakeup` cadencés sur ce qu'on
attend (5 min quand la CI tourne, 50 min quand on attend une revue), `noop` quand rien n'a bougé,
action sur rouge/conflit selon les règles existantes, sortie sur preuve, réveil différé
(`send_later`) en filet, et le rapport de clôture de `passation.md` §7.

### C-4 — Une routine qui porte son savoir hors dépôt

La règle 3 des gardes (`gardes.md`) : « le workflow n'est que la minuterie et la plomberie ; le
savoir vit dans le skill ». La routine viole la règle par construction : son prompt **est** la
procédure. Deux conséquences : une session qui voudrait jouer la re-sonde à la main n'a rien à
invoquer ; et le jour où la procédure change (elle a déjà changé : `ROADMAP.md`, que le prompt
cite, est fusionnée dans `STATUS.md` depuis le 2026-09-23), c'est claude.ai qu'il faut éditer,
depuis un navigateur. → L4 : le skill `status-resonde` dans le moteur, le prompt de la routine
réduit à « joue `/status-resonde` », et la routine recréée **avec** le connecteur GitHub (la
session qui la crée peut nommer `github`, qu'elle détient).

Et sa panne : `last_run` n'est lisible que d'une session cloud. Aucun workflow, aucun hook ne
peut le voir — l'API des routines n'est pas dans la liste réseau d'un runner, et un hook de
session n'a pas l'outil MCP. La seule surface qui voit une routine morte est **une session**.
→ L4 aussi : la clôture de session (`passation.md` §7) relève `list_triggers` et nomme toute
routine dont `last_run` n'est pas `SUCCEEDED` — une ligne, pas une garde.

### C-5 — Des primitives que personne n'a nommées

§1.3 est la première fois que `ScheduleWakeup`, `CronCreate`, `Monitor`, `send_later`,
`create_trigger`, `subscribe_pr_activity` et le hook `Stop` sont écrits côte à côte avec leurs
limites. Ce n'est pas un détail : la borne de 3 600 s d'un tick, les 7 jours d'un cron de
session, les 30 minutes d'un `Monitor` et le « ne tire que session inactive » **décident** de
l'horloge sur laquelle une boucle peut vivre. Un exécuteur qui ne les connaît pas écrira une
boucle `Monitor` pour attendre une revue de trois jours, ou un `CronCreate` pour une garde
hebdomadaire. → L0 : `docs/agents/boucles.md`, et le registre.

### C-6 — Vingt-deux horloges, trois réconciliateurs

Compté sur les deux dépôts (§1.2). Les dix-neuf autres sont des **événements** : ils tirent,
produisent, sortent. Ce n'est pas un défaut en soi — un relevé hebdomadaire n'a rien à
réconcilier — mais aucun fichier ne dit **lequel** est quoi. → L0 : chaque mécanisme autonome
déclare son contrat dans `harness/loops.json` : `observe` (le script), `voulu`, `agit`, `sortie`,
`budget`, `horloge`, `tête` (`none` | `actions-oauth` | `routine` | `session`), `apres` (ce que
devient sa sortie, ou `none` avec sa raison). `harness:check` exige que les scripts cités
existent et soient testés (même schéma que `controls.json` : un contrôle qu'on ne sait pas
nommer ne garde rien).

### C-7 — Mesurer sans corriger

`status-freshness-watch` fait exactement son travail (#1126, seuil 25, 63 PR de retard). La
routine qui devait corriger est morte (C-1, C-4). Entre les deux, rien : l'issue n'a pas de
preneur, et son corps dit à raison « LIRE, pas `sed` » — c'est un travail d'agent. → L4 (le
skill) et Q-4 (qui le joue, et quand : la routine quand elle revit, sinon toute session du moteur
qui trouve l'issue ouverte, en premier lot).

### C-8 — Le coût d'une boucle sans sortie

§2.6. Une boucle est une dépense récurrente ; une boucle sans sortie est une dépense sans fin.
→ D-7 : sortie sur preuve, budget de ticks silencieux, échéance dure, archivage des filles au
merge ; et une ligne de coût dans le rapport de clôture (T-9/T-10 de la méthode de contenu,
étendus à toute boucle).

### C-9 — Un refus n'est pas un état transitoire

§2.7. Le classifieur refuse par catégorie de commande, pas par hasard ; retenter la même
commande au tick suivant la fera refuser au tick suivant. → D-8 : une boucle qui reçoit un
refus **change d'outil** (lecture dédiée, outil MCP) ou **nomme le mur et sort** — elle ne
retente jamais la même commande, et son rapport dit ce qui a été refusé.

## 4. Décisions d'architecture (fermées, sous réserve de Q-1 pour L2 et L4)

| #    | Décision                                                                                                                                                                                                                                                                                                                     | Constat   |
| ---- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| D-1  | **Le contrat de boucle.** Tout mécanisme autonome du harness est décrit par sept champs — `observe`, `voulu`, `agit`, `sortie`, `budget`, `horloge`, `apres` — dans `harness/loops.json`, source de vérité au même titre que `policy.json` et `controls.json`. `harness:check` (invariant 12) vérifie que chaque champ est présent, que le script `observe` existe et a un test, et qu'un `apres: none` porte sa raison | C-5, C-6  |
| D-2  | **Trois horloges, et la règle de placement.** H1 session (`ScheduleWakeup`, `CronCreate`, `Monitor`) pour ce qui se joue en minutes ou heures ; H2 session persistante (`send_later`, `create_trigger` sur cette session) pour ce qui attend des heures ou des jours ; H3 calendrier (Actions `schedule`, routines) pour ce qui revient par jours ou semaines. Une boucle vit sur l'horloge **la plus courte** dont l'horizon couvre sa sortie, ne sonde jamais plus vite que l'état observé ne change (CI ≈ 4 min → 5 min ; revue → 50 min), et son état vit dans un objet GitHub, jamais en mémoire de session | C-5       |
| D-3  | **La garde après push est un skill, et son verdict est un script.** `scripts/ci/pr-state.mjs` rend ce que git prouve ; `/garde-pr` déroule la boucle sur H1 avec `subscribe_pr_activity` en premier signal, `send_later` en filet, et le rapport §7. Le hook `Stop` n'est **pas** retenu en L1 : on mesure d'abord (K-4) ; s'il reste des sessions qui poussent sans garder, il devient l'exécution forcée de la règle (L1b, Q-3), avec le même observateur et le même budget | C-3       |
| D-4  | **Une garde observe sa propre sortie avant d'en produire une autre.** `upgrade-guard` : au plus **un** lot patch/minor ouvert ; le lot du jour remplace un lot en conflit ou en draft, **sauf** s'il porte des commits de l'agent (il est repris) ; un lot vert attend son merge et rien ne s'ouvre à côté. La décision est un script pur (`scripts/deps/reconcile-lots.mjs`), testé ; le YAML ne garde que les appels `gh` — comme `guard-watch.mjs` | C-2       |
| D-5  | **La garde des gardes nomme la cause.** `guard-watch.mjs` reçoit, par run rouge, l'étape en échec et sa première annotation `::error`, calcule la **longueur de la série** par workflow (depuis quand, combien), regroupe les workflows tombés sur le **même message**, et cite le mur de `zero-intervention.md` quand le message appartient à une classe connue (abonnement, jeton, 401, `JWT issued at future`) | C-1       |
| D-6  | **Le savoir d'une routine vit dans un skill du dépôt.** La re-sonde de STATUS.md devient `.claude/skills/status-resonde/` (moteur, miroir `.agents/`) ; la routine ne porte plus que l'invocation et se recrée avec le connecteur GitHub. Règle générale, ajoutée à `gardes.md` : une routine est une minuterie, comme un workflow | C-4, C-7  |
| D-7  | **Pas de boucle sans sortie ni budget.** Sortie : une preuve de contenu, jamais un statut (`passation.md` §7.1, `gardes.md` § le vert qui ne prouve rien). Budget : au plus **3 ticks silencieux** consécutifs, puis un réveil H2 (50 min, puis 4 h, au plus 3), puis arrêt avec une ligne ; échéance dure = celle de la primitive (7 j, 30 min, la session). Les sessions filles sont archivées au merge de leur lot (§7.11). Le rapport de clôture porte une ligne de coût | C-8       |
| D-8  | **Un refus n'est pas réessayé.** Une commande refusée par le classifieur, par le proxy (403) ou par une politique d'accès (C-1) n'est jamais retentée telle quelle au tick suivant : la boucle change d'outil si un équivalent existe, sinon elle nomme le mur et sort. Le rapport dit ce qui a été refusé | C-9, C-1  |
| D-9  | **La session voit les routines, et le dit.** La clôture de session (`passation.md` §7) gagne un point : `list_triggers`, et une ligne par routine dont `last_run` n'est pas `SUCCEEDED`, avec le `status_detail`. C'est la seule surface qui le peut ; une ligne suffit                                                                                                           | C-4       |
| D-10 | **Mesurer les boucles, pas les raconter.** `actions:census` gagne les séries de rouges consécutifs par workflow (longueur, bornes) et l'âge des PR de garde ouvertes ; les KPI de §1.4 se remesurent avec lui                                                                                                                 | §1.4      |

Ce que l'étude **écarte** : remplacer les gardes Actions par des sessions permanentes (une VM
inactive est récupérée, et une boucle de 7 jours coûte 168 tours pour rien) ; un `Monitor` qui
sonde l'API GitHub à moins de 5 minutes ; une boucle qui « relance » un run rouge sans l'avoir
lu ; un hook `Stop` sans budget ; porter le triage des signalements dans une session cloud
(l'export exige la clé service-role, absente d'une session **par conception**) ; rouvrir l'étude
32 (le volume de la chaîne) ou l'option C du 2026-09-05.

## 5. Cible

| Surface                                         | Avant                                                                 | Après                                                                                              |
| ----------------------------------------------- | --------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| Garde après push                                | prose en trois endroits, 0 outil                                      | `/garde-pr` + `pr-state.mjs` ; `passation.md` §7.10 et `collaboration.md` pointent dessus          |
| PR de lot patch/minor ouvertes                  | 5 (+1 major), 0 mergée depuis le 2026-07-31                            | ≤ 1 ; un lot remplacé est fermé avec un commentaire qui nomme son successeur                        |
| Issue `garde-rouge`                             | « N runs rouges » + conseil générique                                  | l'étape, le message, la série (« depuis le 04/10 14:09, 17 runs »), le mur cité                     |
| Têtes d'agent                                   | 5 supports implicites, une panne commune invisible                     | déclarées dans `loops.json` (`tête`), regroupées par cause dans l'issue                             |
| Routine STATUS.md                               | prompt de 2 400 caractères hors dépôt, sans connecteur, en échec       | `/status-resonde` au moteur ; routine = invocation + connecteur GitHub ; échec relevé en clôture    |
| `harness/`                                      | `policy.json`, `models.json`, `controls.json`                          | + `loops.json` (11 mécanismes déclarés), invariant 12 de `harness:check`                             |
| `docs/agents/`                                  | —                                                                     | + `boucles.md` (le contrat, les trois horloges, les primitives et leurs limites, D-7 et D-8)         |
| Mesure                                          | `actions:census` : cadence, fantômes, minutes, runs par branche        | + séries de rouges, âge des PR de garde                                                            |

Arborescence touchée (aucun fichier produit, aucune migration) :

```
moteur/
  docs/agents/boucles.md                         L0 (nouveau)
  docs/agents/README.md, gardes.md, zero-intervention.md, passation.md §7, collaboration.md   L0, L1, L4 (pointeurs)
  AGENTS.md                                      L0 (une ligne « Where to read next » ; budget 158/200 l.)
  harness/loops.json                             L0 (nouveau)
  scripts/harness/check.mjs (+ __tests__)        L0 (invariant 12)
  scripts/ci/pr-state.mjs (+ __tests__)          L1
  .claude/skills/garde-pr/SKILL.md (+ miroir)    L1
  scripts/deps/reconcile-lots.mjs (+ __tests__)  L2
  .github/workflows/upgrade-guard.yml            L2 (une étape « réconcilier les lots ouverts »)
  scripts/ci/guard-watch.mjs (+ __tests__)       L3
  .github/workflows/guard-watch.yml              L3 (deux appels gh de plus : jobs, annotations)
  .claude/skills/status-resonde/SKILL.md         L4
  scripts/ci/actions-census.mjs (+ __tests__)    L5
privé/
  .github/workflows/guard-watch.yml              L3 (les mêmes entrées, par le réutilisable)
  FableEtudes/37-harness-boucles/ETUDE.md        journal
claude.ai/
  la routine « re-sonde » recréée (invocation du skill + connecteur GitHub)   L4, après Q-1
```

## 6. Plan d'exécution en lots

| lot | contenu (résumé)                                                                                                                                                         | fichiers/objets créés                                                                                          | tests exigés                                                                              | dépend de       |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | --------------- |
| L0  | Doctrine et registre : `boucles.md`, `loops.json` (les 11 mécanismes de §1.2 déclarés **tels qu'ils sont**, `apres: none` avec raison là où c'est le cas), invariant 12 | `docs/agents/boucles.md`, `harness/loops.json`, `check.mjs`, une ligne dans `AGENTS.md`, `docs/agents/README.md` | `check.test.mjs` : schéma, script absent, test absent, `apres: none` sans raison           | —               |
| L1  | `/garde-pr` : l'observateur `pr-state.mjs` et le skill ; `passation.md` §7.10 et `collaboration.md` renvoient au skill                                                   | `scripts/ci/pr-state.mjs`, `.claude/skills/garde-pr/SKILL.md`, miroir `.agents/` par `harness:sync`              | `pr-state.test.mjs` sur fixtures (`ls-remote`, `ls-tree`, diff) ; `verify` vert              | L0              |
| L2  | `upgrade-guard` réconcilie ses lots : `reconcile-lots.mjs` + l'étape ; premier passage réel mesuré sur les 5 PR ouvertes                                                  | `scripts/deps/reconcile-lots.mjs`, `upgrade-guard.yml`                                                          | `reconcile-lots.test.mjs` : remplacer / reprendre (commits de l'agent) / attendre (vert) / ne rien faire | L0 ; Q-1 pour la partie agent |
| L3  | La garde des gardes nomme la cause : étape, annotation, série, regroupement par message, mur cité                                                                        | `scripts/ci/guard-watch.mjs`, `guard-watch.yml` (moteur ; le privé suit par le réutilisable)                     | `guard-watch.test.mjs` : série, regroupement, classes de message → mur                      | L0              |
| L4  | La re-sonde devient un skill ; la routine recréée (invocation + connecteur) ; `passation.md` §7 gagne la relève `list_triggers`                                          | `.claude/skills/status-resonde/SKILL.md`, `passation.md`, la routine                                            | le skill joué une fois depuis une session interactive, rapport identique à celui de la routine | L0 ; Q-1 pour la routine |
| L5  | Mesure : `actions:census` (séries, âge des PR de garde), KPI relevés, étude close                                                                                        | `scripts/ci/actions-census.mjs`                                                                                 | `actions-census.test.mjs` : séries sur un dump                                              | L2, L3          |

Détail par lot :

- **L0 — Doctrine et registre.** Périmètre : `boucles.md` reprend §1.1, §1.3, D-2, D-7, D-8 de
  cette étude en playbook (le « quand lire » dans l'index de `docs/agents/README.md` : « avant
  d'écrire quoi que ce soit qui attend, relance ou se réveille ») ; `loops.json` déclare les 11
  mécanismes de §1.2 **sans en changer un seul** — `apres: none` et sa raison sont une
  description honnête, pas un gate ; `check.mjs` : invariant 12 (schéma clos, `observe` doit
  être un script existant avec un test co-localisé, `apres` ≠ `none` ou `why` non vide, `tete`
  dans l'énumération). Critères : `verify` vert, `harness:check --corpus` inchangé au privé.
  Stop-point : aucun workflow, aucun skill de garde modifié.
- **L1 — `/garde-pr`.** `pr-state.mjs <chemins livrés…>` rend un JSON :
  `{ merged_by_content, pr: { number, head_sha } | null, head_up_to_date, merge_ref_present }`,
  calculé par `git fetch origin main`, `git ls-tree origin/main`, `git ls-remote origin
  'refs/pull/*/head'` (la PR est celle dont la tête vaut le SHA de la branche — **à vérifier au
  premier geste du lot : ce chemin réseau n'a pas tourné dans la session qui l'a écrit**, le
  classifieur l'a refusé, §2.7) et `refs/pull/N/merge` (absent = conflit ou pas encore calculé :
  l'absence vaut « regarder par l'outil », jamais « conflit »). Les check-runs restent à l'outil
  MCP (`pull_request_read get_check_runs`) : le skill les lit, le script ne les devine pas. Le
  skill : abonnement d'abord, tick `ScheduleWakeup` 5 min tant qu'un check tourne, 50 min
  ensuite, `noop` si rien n'a bougé, action sur rouge/conflit selon `ci-cd-and-branch-protection.md`
  et les consignes de garde, sortie sur `merged_by_content` → `passation.md` §7 ; budget D-7 ;
  refus D-8. Critères : K-4 ; un `verify` vert ; le skill ≤ 1 024 caractères de description
  (spec Agent Skills, é32 C-7). Stop-point : pas de hook `Stop` (L1b, Q-3).
- **L2 — Les lots se réconcilient.** `reconcile-lots.mjs` est pur : entrée = la liste des PR
  `claude/upgrade-patch-minor-*` ouvertes (numéro, draft, `mergeable_state`, labels, nombre de
  commits, auteur du dernier) + le plan du jour ; sortie = une décision par PR : `attendre`
  (verte, non draft, à jour), `reprendre` (porte des commits de l'agent), `remplacer` (conflit
  ou draft sans commit d'agent → fermer avec le commentaire « remplacée par #N », supprimer la
  branche), `ignorer`. L'étape YAML applique ; le lot du jour n'est ouvert que si la décision
  l'exige. Premier passage réel : les cinq PR ouvertes, résultat consigné au journal. Critères :
  K-1 ≤ 1 après le premier passage ; aucune PR portant un commit d'agent fermée. Stop-point : ne
  pas toucher à la détection ni à l'apply ; ne pas toucher à Dependabot.
- **L3 — La cause dans l'issue.** `guard-watch.yml` ajoute, pour chaque run rouge retenu, l'appel
  `jobs` (l'étape dont la conclusion est `failure`) et `check-runs/<id>/annotations` (la
  première `failure`) ; `guard-watch.mjs` reçoit ces deux champs par le JSON d'entrée (même
  contrat que l'existant : entrée fichier, sortie Markdown), calcule la série par workflow sur
  la fenêtre **et** sur les runs précédents déjà cités par l'issue (la série de C-1 dépasse la
  fenêtre de 8 h), regroupe par message identique, et cite le mur pour les classes connues.
  Critères : rejouer le JSON du 2026-10-05 en test → une issue qui dit « `report-triage`, étape
  _Run the report-triage agent_, depuis le 04/10 14:09, 5 runs : _Your organization has
  disabled…_ — mur « réglage hors dépôt » ». Stop-point : la garde ne relance rien, ne corrige
  rien (son contrat de `gardes.md`).
- **L4 — Le savoir dans le dépôt.** `status-resonde/SKILL.md` reprend le prompt de la routine
  (§2.3) corrigé de ce qui a changé depuis (plus de `ROADMAP.md` ; §6 de `STATUS.md`) ; la
  routine est mise à jour (`update_trigger`) avec le prompt « lis AGENTS.md puis joue
  `/status-resonde` » et recréée avec `connectors: ["github"]` si la mise à jour ne peut pas
  porter le connecteur ; `passation.md` §7 gagne le point 12 (D-9). Critères : le skill joué
  depuis une session rend le même rapport ; K-5. Stop-point : ne pas re-sonder `STATUS.md` dans
  ce lot (c'est le travail du skill, pas du lot).
- **L5 — Mesure.** `actions:census` : pour chaque workflow, la plus longue série de conclusions
  rouges consécutives (bornes, longueur) et, pour les PR ouvertes par un garde (préfixes
  `claude/upgrade-`, `draft/regression-guard-`), l'âge en jours ; relevé des KPI de §1.4,
  journal, statut `livrée`.

Cases à cocher :

- [ ] L0 — Doctrine et registre
- [ ] L1 — `/garde-pr`
- [ ] L2 — Les lots se réconcilient
- [ ] L3 — La cause dans l'issue
- [ ] L4 — Le savoir dans le dépôt
- [ ] L5 — Mesure

## 7. Stratégie de test & mesure

- **Unitaire (Vitest, co-localisé dans `scripts/**/__tests__/`)** : chaque script est pur ou
  séparé en fonctions pures exportées (le pattern de `guard-watch.mjs` et d'`actions-census`) ;
  les appels réseau restent dans le YAML ou dans un `main()` qui n'est pas testé. Fixtures :
  sorties réelles de `git ls-remote`, de l'API `jobs`, de l'API `annotations`, et le JSON de
  `guard-watch` du 2026-10-05 (reconstitué depuis les runs cités au §2.2).
- **Le gate** : `npm run verify` (dont `harness:check` avec l'invariant 12) sur chaque lot ;
  `harness:check --corpus` continue de passer au privé (L0 ne touche pas les invariants corpus).
- **Pas de test e2e ni de smoke** : aucun fichier produit n'est touché.
- **La mesure est le test d'acceptation** : K-1 et K-2 après le premier passage de L2 ; K-3 sur
  la première série réelle après L3 (ou sur le rejeu du 2026-10-05) ; K-4 sur les sessions qui
  poussent après L1 (le journal de chacune) ; K-5 à chaque clôture.
- **Ce qui prouve la non-régression** : `guard-watch` continue d'ouvrir et de refermer une seule
  issue (ses tests existants restent verts) ; `upgrade-guard` continue d'ouvrir un lot quand
  aucun n'est ouvert (le cas nominal est un cas de test de `reconcile-lots`) ; la chaîne
  `auto-pr` → `automerge` n'est pas touchée.

## 8. Risques & mitigations

- **RISK-1 — Une boucle qui ne sort pas** (probabilité moyenne, impact coût). D-7 : sortie sur
  preuve, 3 ticks silencieux, échéance dure, filles archivées ; la ligne de coût dans le rapport
  rend la dérive visible dès la première session.
- **RISK-2 — Deux sessions gardent la même PR** (faible, impact bruit). `subscribe_pr_activity`
  n'admet qu'un abonné ; `/garde-pr` ne garde que la PR que **cette** session a poussée (DoD §8),
  et un refus d'abonnement vaut « une autre session garde » → sortie avec une ligne.
- **RISK-3 — La VM est récupérée en pleine boucle** (certaine à l'échelle de jours, impact
  nul si D-2 est respectée). L'état est dans GitHub ; `send_later` re-provisionne ; le tick qui
  suit re-observe de zéro.
- **RISK-4 — La tête d'agent reste refusée** (Q-1, impact fort sur L2 et L4). L3 ne dépend pas
  de l'agent et nomme le refus en ≤ 6 h ; L2 traite le cas « agent indisponible » : pas de
  nouveau draft chaque jour, le lot vert attend, le lot rouge est annoté une fois.
- **RISK-5 — Le classifieur refuse un pas de la boucle** (vécu, §2.7). D-8 : changer d'outil
  ou sortir en nommant le refus ; jamais la même commande deux fois.
- **RISK-6 — Fermer une PR qui portait du travail** (faible, impact fort). `reconcile-lots`
  refuse de fermer un lot dont le dernier commit n'est pas celui du script ; le cas est testé en
  premier.
- **RISK-7 — Le registre devient un journal** (moyenne, impact lisibilité — la leçon de
  `policy.json`, é32 C-10). `loops.json` porte un champ `why` par mécanisme, une ligne ; le
  récit vit dans `boucles.md`.
- **RISK-8 — Une primitive change** (plateforme en « research preview », étude cloud-first §5).
  Les limites de §1.3 sont datées ; `boucles.md` dit de les re-constater, pas de les croire.

## 9. Questions ouvertes (pour le propriétaire)

- **Q-1 — Où tournent les têtes d'agent ?** Du 4 au 9 octobre, l'abonnement a été refusé aux
  gardes Actions et à la routine, puis rendu — sans qu'aucun changement du dépôt l'explique.
  Trois chemins, à constater d'abord sur claude.ai (réglage d'organisation « subscription access
  for Claude Code ») : (a) l'abonnement, si le réglage est à nous — rien à changer, L3 nomme la
  prochaine coupure ; (b) une clé API pour les gardes Actions (`anthropic_api_key` à la place
  du jeton OAuth, déjà prévue dans les en-têtes des workflows, `models.json` inchangé) — un coût
  à l'usage, à plafonner ; (c) les têtes en session seulement, en acceptant que `report-triage`
  n'en ait pas (clé service-role). **Recommandation** : (a) si le réglage est à nous, sinon (b)
  avec un plafond mensuel ; (c) n'est pas une réponse, c'est un repli. Cite le mur « réglage
  hors dépôt ». Bloque la partie agent de L2 et la routine de L4, rien d'autre.
- **Q-2 — Les drafts de `regression-guard`.** Un draft que « un humain promeut » est une
  validation manuelle. **Recommandation** : promotion par règle — `verify` vert et diff limité à
  `**/__tests__/**`, `e2e/**`, `supabase/tests/**` → `gh pr ready`, auto-merge normal ; tout
  autre diff reste draft et ouvre une issue. #932 (ouverte depuis le 2026-09-01) est le premier
  cas à passer par la règle.
- **Q-3 — Faut-il forcer la garde après push par un hook `Stop` ?** L1 mesure d'abord (K-4).
  **Recommandation** : non tant que K-4 est à 0 % sur dix sessions ; oui, avec le même
  observateur et le même budget, si une session pousse encore sans garder.
- **Q-4 — Qui re-sonde `STATUS.md` ?** **Recommandation** : la routine (après Q-1) comme chemin
  principal, et — tant que #1126 ou son successeur est ouverte — la première session du moteur
  qui la trouve joue `/status-resonde` comme premier lot. Les deux honorent la règle « un statut
  se constate ».

## 10. Journal d'exécution

| Date       | Lot | Événement                                                                                                                                                                                                                                                                                                  |
| ---------- | --- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2026-10-11 | —   | Étude rédigée depuis une session cloud sur le relevé du jour (§2) ; mesures brutes en annexe A. Livrée en brouillon par privé#649 (cette étude, la ligne d'index) et moteur #1164 (`STATUS.md` §4, §6.3, journal) — les deux poussées par la session, PR ouvertes par `auto-pr`, gate `verify` vert au `pre-push` (352 fichiers, 4 682 tests). Test du réveil différé : `send_later` posé à 17:33 UTC pour 17:37 (`trig_018dKSt77Ebjht9b3hpHmvnb`). **Reçu** : tiré à 17:37:21, il a attendu dans la file de notifications de la session pendant tout le tour en cours (23 min) et a été lu à 18:00:46, à la fin du tour, avec les six événements GitHub des PR abonnées. **Le chemin H2 fonctionne** malgré le refus des routines « session neuve » du 2026-10-05 : un réveil dans une session existante n'est pas une routine qui crée une session. Deux leçons pour D-2 et L1 : un réveil ne coupe jamais un tour (il attend la fin du tour, donc une boucle H1 qui ne rend pas la main ne sera jamais réveillée par H2) ; et les événements GitHub arrivent par la même file — la boucle les lit d'un coup au réveil, dans l'ordre. |

## Annexe A — Relevé brut du 2026-10-11

Runs (API `actions_list`, `perPage` 20 ou 30 ; durée = `run_started_at` → `updated_at`) :

```
regression-guard.yml (41 runs au total)
  10-09 02:47 schedule success  0,2   10-06 02:41 success 0,3   10-02 02:00 FAILURE 9,1
  09-29 02:28 success 0,2          09-25 01:08 success 0,2   09-22 01:26 success 4,0
  09-18 01:03 success 4,7          09-15 01:10 FAILURE 6,5   09-11 00:49 success 0,2
  09-08 00:54 FAILURE 0,6          09-04 00:47 FAILURE 6,9   09-01 01:39 success 14,1
upgrade-guard.yml (125 runs au total) — workflow_run, un par jour
  10-11 0,2 ok  10-10 0,1 ok  10-09 7,9 FAIL  10-08 0,1 ok  10-07 0,2 ok  10-06 9,8 FAIL
  10-05 0,2 ok  10-04 0,2 ok  10-03 0,1 ok  10-02 40,4 FAIL  10-01 0,1 ok  09-30 0,1 ok
  09-29 28,7 FAIL  09-28 0,2 ok  09-27 0,1 ok  09-26 0,2 ok  09-25 35,5 FAIL  09-24 0,1 ok
  09-23 0,2 ok  09-22 0,5 FAIL
report-triage.yml (444 runs au total) — schedule
  10-11 06:01 ok · 10-10 23:39 ok · 20:10 ok · 14:31 ok · 06:03 ok · 10-09 21:01 ok (23,7 min)
  10-09 15:22 FAIL · 06:21 FAIL · 10-08 21:23 · 15:43 · 06:19 FAIL · 10-07 21:22 · 15:37 · 06:11 FAIL
  10-06 23:53 · 18:29 · 11:22 · 01:20 FAIL · 10-05 17:13 · 05:55 FAIL · 10-04 23:18 · 19:42 · 14:09 FAIL
  10-04 06:03 ok · 10-03 23:10 · 19:18 · 13:31 · 05:28 ok · 10-02 20:49 · 14:47 ok
content-audit.yml (privé, 26 runs au total)
  10-11 00:53 ok 3,1   10-08 01:49 ok 0,3   10-04 00:30 FAIL 0,9   10-01 01:13 FAIL 11,1
  09-27 ok 4,3   09-24 ok 6,3   09-20 ok 7,5   09-17 ok 3,7   09-12 ok 2,2   09-10 ok 4,7
  09-05 ok 4,1   09-03 (dispatch) ok 8,8   09-03 FAIL 1,2   08-30 ok 2,7   08-27 ok 6,7
```

Étapes des runs rouges lus (`list_workflow_jobs`) :

- `report-triage` #438 (10-09 15:22) : secrets ✓, checkout ✓, export ✓, ids déjà triés ✓,
  pré-gate ✓, modèle ✓, **« Run the report-triage agent » ✗ en 16 s**, « Fail loudly » ✗,
  issue de suivi ✓. Même profil pour #425 (10-05).
- `report-triage` #439 (10-09 21:01) : identique jusqu'au modèle, puis **l'agent tourne
  21:02 → 21:25**, vert, #1162 ouverte.
- `upgrade-guard` #123 (10-09) : journal — « _failed at the Claude level: Your organization has
  disabled Claude subscription access for Claude Code · Use an Anthropic API key instead, or ask
  your admin to enable access_ » ; PR #1158 en draft `needs-review`.
- `upgrade-guard` #116 (10-02) : lot vert, PR #1153 ouverte 07:04, agent 07:04 → 07:36 ✗,
  « lot resté rouge » ✗ ; E2E et pgTAP `skipped`.
- `regression-guard` #39 (10-02) : « _failed at the Claude level: (no message)_ ».
- `content-audit` #24 (privé, 10-04) : « Run the content-audit sweep » ✗ en 16 s.

PR et issues (`list_pull_requests`, `search_pull_requests`, `list_issues`) :

- Moteur, PR ouvertes : #1158 (draft, `needs-review`), #1157 (draft, `needs-review`), #1153
  (`needs-rebase`, `mergeable_state: dirty`), #1135 (Dependabot, `major`, `needs-rebase`), #1128
  (`needs-rebase`), #1111 (`needs-rebase`), #932 (`draft/regression-guard-20260901`).
- Lots patch/minor mergés : #684 (2026-07-31), #659 (07-28), #592 (07-21), #300 (07-05).
- Issues ouvertes : #1162 (triage du 10-09), #1126 (`status-perime`, 09-28, 63 PR de retard),
  #1087, #1002, #962, #937, #660. Issues `garde-rouge` closes : 29 ; #1156 ouverte 10-04 21:58,
  close 10-10 06:25.
- Privé, PR ouvertes : 4 savepoints `wip/` (#637, #634, #607, #594) — volontaires.

Routine (`list_triggers`) : voir §2.3. Sessions (`list_sessions`, 100 dernières) : origines
`claude_code_cli` 31, `ios` 30, `claude_code_mcp_seed` 29, `web_claude_ai` 10 ; septembre 68,
août 30, octobre 2 ; aucune session d'origine `scheduled_trigger` listée.

## Annexe B — Le contrat d'une boucle (`harness/loops.json`, schéma cible)

```json
{
  "$comment": "Un mécanisme autonome par entrée. Sept champs, tous obligatoires (invariant 12).",
  "loops": {
    "garde-pr": {
      "observe": "scripts/ci/pr-state.mjs",
      "voulu": "l'apport de la branche est sur main (ls-tree), la PR est fermée",
      "agit": "/garde-pr : met à jour, répare un rouge, réarme — jamais merge à la main",
      "sortie": "merged_by_content = true, ou budget épuisé (3 ticks silencieux + 3 réveils)",
      "budget": { "ticks_silencieux": 3, "reveils": 3, "echeance": "session" },
      "horloge": "H1+H2",
      "tete": "session",
      "apres": "passation.md §7 (clôture), none si budget épuisé — la ligne de clôture le dit",
      "why": "la DoD §8 n'était portée par aucun outil (é37 C-3)"
    },
    "upgrade-guard": {
      "observe": "scripts/deps/reconcile-lots.mjs",
      "voulu": "au plus un lot patch/minor ouvert, mergé sous 48 h quand il est vert",
      "agit": "upgrade-guard.yml : remplace, reprend ou attend ; automerge merge",
      "sortie": "le lot est sur main, ou remplacé par le lot du jour",
      "budget": { "echeance": "cron" },
      "horloge": "H3",
      "tete": "actions-oauth",
      "apres": "automerge (vert) · reconcile-lots (conflit, draft)",
      "why": "six lots ouverts, zéro mergé en 72 jours (é37 C-2)"
    }
  }
}
```
