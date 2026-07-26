# Étude — IA → déterministe, volet contenu

> **Statut : ouverte le 2026-07-25, et les 5 lots sont livrés le jour même** — état par lot au
> §6. Pendant privé de `docs/agents/etude-ia-vs-deterministe.md` du moteur public (close le
> 2026-07-25, 6 lots sur 6), dont le §4.6 renvoyait explicitement cet arbitrage ici.
> **Périmètre** : ce dépôt (corpus, skills, workflows) et les checks du moteur que le corpus
> consomme. Le moteur lui-même est traité chez lui.

## 0. TL;DR

Ce dépôt est **déjà très majoritairement déterministe** : cinq workflows sur six sont des
scripts, la Content CI passe quatre gates à chaque PR, et la méthode de campagne a sa propre
charte tokens dont la règle **T-1** dit mot pour mot ce que dit cette étude. **Une seule
surface dépense un agent** : `content-audit.yml`.

L'application de la grille en sort trois constats — et le premier n'est pas une économie de
tokens, c'est un **trou de couverture** :

| #   | Constat                                                                                                                | Nature             | Priorité |
| --- | ---------------------------------------------------------------------------------------------------------------------- | ------------------ | -------- |
| 1   | Deux règles que le skill énonce **en regex** ne sont implémentées nulle part → 7 cours livrés avec du LaTeX brut        | **défaut, pas coût** | **P1**   |
| 2   | Le garde pédagogique est **mort-né** : armé le 20/07, une seule exécution, échouée sur un jeton invalide, jamais vue    | fiabilité          | **P1**   |
| 3   | Son prompt recalcule son propre périmètre, dédoublonne à la main, et **refait des checks que le gate assure déjà**      | coût               | P2       |

Le principe est celui du moteur : **l'IA écrit la règle une fois ; le script l'applique ensuite
gratuitement, instantanément et partout.** Ici « partout » compte autant que « gratuitement » —
voir §4.1.

## 1. Le fait qui cadre tout : le garde pédagogique n'a jamais tourné

`content-audit.yml` n'est **pas** dormant : le secret `CLAUDE_CODE_OAUTH_TOKEN` est configuré
sur ce dépôt depuis le **2026-07-20**. Le garde est donc armé, et son cron (mer. + sam. 22:07
UTC) a déclenché.

Il a produit **une seule exécution** — run `29965432119`, le **2026-07-22 à 23:13 UTC** — qui a
**échoué en 56 secondes** :

```
##[error]Claude result reported subtype success with is_error:true
##[error]API Error: Header 'Authorization' has invalid value
```

Le jeton est invalide. Aucun audit pédagogique n'a donc eu lieu depuis l'armement, et la
prochaine tentative échouera de la même façon. **Personne ne l'a vu** : un cron qui échoue dans
un dépôt privé ne notifie rien, et contrairement à `video-health.yml` — qui ouvre et referme une
issue de suivi — le garde d'audit n'a aucune surface de signalement.

Deux enseignements, qui sont exactement ceux du lot L4 du moteur :

1. **Le chemin nominal ne doit pas dépendre du jeton.** Un gate script tourne sans secret ; un
   garde agent, non. Tout ce qu'on descend du prompt vers un script devient immunisé contre la
   panne ci-dessus.
2. **Le silence d'un garde ressemble à sa réussite.** Le moteur a payé ce défaut deux fois cette
   semaine (le lot patch/minor qui ne voyait pas les lignes 0.x, le `npm outdated` qui ne
   tournait pas). Ici la forme est administrative plutôt que logique, la conséquence est la même.

> **Action hors périmètre de cette étude** : renouveler le secret (`claude setup-token`) relève
> de l'opérateur — aucun agent ne manipule ce jeton. Le lot **LC4** ne le renouvelle pas : il
> rend son absence **bruyante**.

## 2. Inventaire des surfaces (dépôt privé, 2026-07-25)

82 sujets, 3 943 fichiers JSON, 1 138 fichiers Markdown, 41 skills (13 `content-*`, 27 `prof-*`,
`curriculum-architect`), 6 workflows.

| Surface                  | Déclencheur                     | Agent ?                        | Ce qu'elle fait                                        |
| ------------------------ | ------------------------------- | ------------------------------ | ------------------------------------------------------ |
| `content-ci.yml`         | chaque PR + push `main`         | **non**                        | `content:check`, `qa:strict`, `audit:strict`, `programme:check` |
| `apply-content.yml`      | dispatch                        | **non**                        | applique `sql/content/*.sql` en prod, journalise        |
| `apply-content-test.yml` | dispatch                        | **non**                        | idem sur le projet TEST                                 |
| `roadmap-sync.yml`       | PR sur `ROADMAP.md` + cron      | **non**                        | gate de connaissance des lots livrés                    |
| `video-health.yml`       | dim. 06:00 UTC + dispatch       | **non**                        | sonde les vidéos, ouvre/ferme une issue de suivi         |
| `content-audit.yml`      | **mer. + sam. 22:07 UTC** + dispatch | **oui** (Sonnet, ≤ 60 tours) | audit pédagogique du contenu récemment modifié           |
| Campagnes de génération  | session locale, à la demande    | **oui** (le gros du budget)    | écriture des fiches et du contenu (méthode + charte T)   |

## 3. La grille, et sa version contenu

Rappel du §3 du moteur : un check **doit** être un script quand sa règle s'exprime en pattern,
AST, diff ou comparaison de nombres ; l'agent reste justifié pour un jugement sémantique, une
entrée non bornée, une production de texte.

Côté contenu, la frontière se lit encore plus simplement : **la règle porte-t-elle sur la forme
du texte, ou faut-il refaire l'exercice pour trancher ?** Et le skill `content-audit` tranche
souvent lui-même — plusieurs de ses items sont **donnés en regex dans le prompt** (`[٠-٩]`,
`\\[a-zA-Z]+`, `\d \d{3}`, `[√∛∜](?:[؀-ۿ]…`). Une règle qu'on sait écrire en regex n'a rien à
faire dans un prompt : elle y coûte des tokens, elle y est appliquée de façon variable, et elle
ne s'applique qu'aux fichiers que l'agent a eu le temps de regarder.

## 4. Analyse surface par surface

### 4.1 Les règles mécaniques que personne n'exécute (P1 — un trou, pas une économie)

Le moteur implémente déjà beaucoup de vérifications déterministes (`scripts/content/qa-checks.ts`,
948 lignes) : bidi fragile, radicande arabe, virgule arabe dans une notation, groupes de chiffres
séparés par une espace sécable, `<svg>` sans `viewBox`, options méta (« aucune de ces réponses »),
options dupliquées, pureté de langue, tags de méprise, références de compétences, registre vidéo.

**Deux règles du skill n'y sont pas** — alors que le skill les classe [MAJOR] et les écrit en
regex :

| Règle du skill                                                       | Dans `content:qa` ? | Réalité du corpus                                   |
| ---------------------------------------------------------------------- | ------------------- | --------------------------------------------------- |
| LaTeX rendu brut (`\command`, `$…$` — l'app n'a pas de moteur de rendu) | ❌ absente          | **7 `cours.md` en infraction** (voir ci-dessous)     |
| Chiffres arabo-indiens `[٠-٩]` (doivent être zéro)                     | ❌ absente (juste normalisés) | respectée de fait — 1 occurrence, dans `content/README.md`, qui documente la règle |

Sonde du 2026-07-25 sur l'intégralité du corpus (3 943 JSON parsés + 1 138 Markdown, blocs de
code et `<svg>` retirés) : **zéro** occurrence dans les questions, et **7 chapitres de
`math-8eme`** dont le cours contient du LaTeX brut — `\dfrac`, `\text`, `\qquad`, `\quad`,
`\parallel`, `\Longrightarrow`. Exemple réel
(`content/math-8eme/12-muthallath-qa2im-wa-da2ira/cours.md`) :

```
$$ R = \dfrac{BC}{2} $$
$$ IA = \dfrac{BC}{2} \quad \Longrightarrow \quad \text{المثلث ABC قائم الزاوية في A} $$
```

L'élève de 8ᵉ voit littéralement `\dfrac{BC}{2}`. Le seul filet prévu pour attraper ça est un
audit hebdomadaire, échantillonné sur les sujets modifiés dans les quatre derniers jours, et
qui — §1 — **n'a jamais tourné**.

Descendre ces deux règles dans le moteur ne fait pas qu'économiser des tokens : **ça change la
couverture**, de « les sujets qu'un agent a eu le temps de relire » à « les 3 943 fichiers, à
chaque PR ». C'est le lot **LC1**, et il a un préalable strict (**LC0**) : le corriger d'abord
au corpus, sinon la Content CI passe au rouge sur les 7 fiches existantes.

### 4.2 `content-audit.yml` — ne réveiller l'agent que sur du nouveau (P1)

Le prompt actuel demande à l'agent, en langage naturel, de **calculer son propre périmètre** :

> list the subjects whose files under `content/**` were modified on `main` in roughly the last 4
> days (`git log --since="4 days ago" --name-only --pretty=format: -- content` …)

C'est un `git log`. Exactement le pré-gate du lot L3 du moteur : un script le calcule pour rien,
et quand la liste est vide **l'agent n'est pas réveillé du tout** — au lieu d'être réveillé pour
conclure « rien à auditer ». Le corpus évolue par rafales de campagne (depuis la création du
dépôt : 27 commits dont **5 touchant `content/`**, sur **2 journées distinctes**), donc la
majorité des crons trouveront zéro sujet modifié.

Deuxième point, transposé du lot L2 : la **déduplication des issues** est aujourd'hui à la charge
de l'agent (« list existing open `content-audit` issues and do NOT duplicate one already filed for
the same locator »). Un script sait lister les issues ouvertes `content-audit` et en extraire les
`locator` — à condition qu'ils soient dans un champ structuré du corps, ce que le lot doit
imposer. L'agent reçoit l'ensemble déjà trié ; il ne le reconstitue pas à chaque réveil.

### 4.3 Le prompt refait le travail du gate (P2)

La checklist du skill mêle des items de jugement et des items que `content:qa:strict` **fait déjà
échouer en CI** : notation bidi, radicande arabe, virgule arabe dans une notation, `viewBox`,
options méta, options dupliquées. Les faire re-scanner à l'œil par l'agent, c'est payer deux fois
et introduire une variance sur un verdict déjà tranché ailleurs. Le prompt doit **citer le gate**
(« ces classes sont déjà garanties par `content:qa:strict`, ne les re-vérifie pas ») et réserver
les tours d'agent aux items qui ne s'automatisent pas — §4.6.

### 4.4 Ce que le harness de ce dépôt n'a pas hérité du moteur (P2)

Trois écarts, tous constatés dans `content-audit.yml`, qui expliquent en partie le §1 :

- **Modèle en dur** : `--model claude-sonnet-4-6` dans le workflow. Le moteur l'interdit depuis
  l'étude 25 (les rôles vivent dans `harness/models.json`, et `harness:check` échoue sur un
  identifiant de modèle en dur dans un workflow). Ici, changer de modèle demande d'éditer le YAML,
  et rien ne prévient quand l'identifiant vieillit.
- **Actions non épinglées** : `actions/checkout@v7`, `actions/setup-node@v6`,
  `anthropics/claude-code-action@v1` — le moteur épingle tout par SHA (étude 25 lot 5b). Un dépôt
  qui porte la propriété intellectuelle du corpus mérite au moins la même discipline.
- **Aucune visibilité d'échec** : `video-health.yml` ouvre une issue de suivi quand la sonde
  trouve un problème, et la referme quand tout va bien. Le garde d'audit, lui, meurt en silence
  (§1). Le lot **LC4** lui donne la même mécanique.

Ces trois points ne sont pas « IA vs déterministe » au sens strict, mais ils décident **si** la
part d'IA qu'on garde fonctionne. Un garde qu'on ne sait pas voir tomber n'est pas un garde.

### 4.5 Les campagnes : doctrine déjà écrite, mécanique encore absente

C'est de loin le premier poste de dépense du projet (une session entière par tranche de
chapitres). Et la méthode a **déjà** sa charte tokens `T-1…T-10`, dont la première règle est
littéralement cette étude :

> **T-1 — Le déterministe est gratuit : ne le refais jamais au LLM.**

Il n'y a donc rien à ajouter côté doctrine. Le manque est ailleurs, et c'est la leçon du lot L4
du moteur : **une règle qui ne tient que si l'agent s'en souvient n'est pas un garde-fou.** T-9
(« chaque lot rapporte son coût ») et T-10 (« jamais une longue session sans PR ») sont
mécanisables — un script de fin de tranche qui refuse de clore sans coût déclaré, un rappel de
push adossé au ledger. Ce n'est pas un lot de cette étude : c'est le candidat suivant, à instruire
avec l'étude 12, et il ne doit pas retarder LC0-LC4.

### 4.6 Ce qui doit RESTER de l'IA (et pourquoi)

- **La double résolution à l'aveugle** — refaire l'exercice sans regarder la clé. Aucune règle de
  forme ne remplace ça, et c'est la vérification qui attrape les fautes qui comptent.
- **L'accord explication ↔ clé**, la qualité des distracteurs, la calibration de difficulté.
- **La cohérence linguistique** : le skill le dit lui-même — _« no regex catches this — it is the
  auditor's job »_ (accord grammatical, référents, duel arabe sur trois référents, calques).
- **L'exactitude factuelle et la fidélité au programme CNP**, qui demandent de lire une source.
- **L'écriture** : cours, questions, distracteurs, figures. C'est le métier, pas de l'outillage.

## 5. Ce que ce dépôt fait déjà bien (ne pas y toucher)

Cinq workflows sur six sans agent ; la Content CI qui passe les quatre gates sur chaque PR ; le
gate de roadmap qui vérifie une connaissance au lieu de la promettre ; `video-health` entièrement
scripté, issue de suivi comprise ; l'application du contenu par SQL compilé et journalisé plutôt
que par un agent ; et la charte tokens de la méthode de génération. La grille ne crée pas un
principe ici — elle finit de l'appliquer, comme dans le moteur.

## 6. Plan par lots

| Lot     | Dépôt  | Contenu                                                                                                       | État                                                                                                            |
| ------- | ------ | ------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| **LC0** | privé  | Corriger les 7 `cours.md` de `math-8eme` : LaTeX → Unicode brut (`R = BC/2`, `⟹`, prose arabe hors `\text{}`) | ✅ livré 2026-07-25 (#13) — 43 lignes, conventions de la maison respectées                                          |
| **LC1** | moteur | `qa-checks.ts` : flag LaTeX (`\command`, `$…$`) + chiffres arabo-indiens, avec tests                           | ✅ livré 2026-07-25 (arena#628) — `auditMathNotation`, +10 tests ; validé en 2 passes sur le corpus réel (voir §7) |
| **LC2** | privé  | Pré-gate déterministe de `content-audit` : sujets modifiés + locators déjà signalés → agent skippé si vide     | ✅ livré 2026-07-25 (arena#629 pour le script + #16 pour le câblage) — 11 tests                                    |
| **LC3** | privé  | Alléger le prompt de tout ce que `content:qa:strict` garantit ; l'audit ne garde que le jugement (§4.6)        | ✅ livré 2026-07-25 (#16) — en échange, le contrat `Locator:` devient obligatoire                                  |
| **LC4** | privé  | Harness : modèle via `harness/models.json`, actions épinglées par SHA, **issue de suivi sur échec du garde**   | ✅ livré 2026-07-25 — SHA par #14 (session sœur), modèle + label `garde-en-panne` par #16                          |
| _(LC5)_ | privé  | _Candidat, pas un lot_ : mécaniser T-9/T-10 de la charte tokens (coût déclaré, push par tranche)               | ⏸️ non instruit — à traiter avec l'étude 12                                                                        |

**Ordre imposé.** `LC0` avant `LC1` (sinon la Content CI passe au rouge sur les fiches
existantes ; aucune PR ne touche les deux dépôts, donc les deux merges sont séquentiels et
assumés). `LC4` avant d'espérer quoi que ce soit d'un run réussi. `LC2`/`LC3` sont indépendants.

**Mesure de clôture** (le critère, comme dans le moteur) : plus une seule surface ne dépense un
agent sur un chemin nominal mécanique, **et** aucune règle énoncée en regex dans un skill ne reste
sans implémentation dans le gate.

## 7. Risques et garde-fous

- **« Le regex voit moins que l'auditeur. »** Vrai, et hors sujet : on ne retire rien à l'auditeur,
  on lui enlève des tâches qu'il fait moins bien qu'un script (et, §4.1, qu'il ne fait pas du tout).
- **Un gate trop strict bloque la campagne.** `LC1` ne part qu'après `LC0`, et son flag doit viser
  la faute réelle (une commande LaTeX, `$…$` en ligne) sans casser les `$$ … $$` en Unicode pur,
  que la doctrine autorise.
- **La dédup par locator suppose un format.** `LC2` doit imposer un champ structuré dans le corps
  de l'issue ; sinon le script dédoublonne sur du texte libre et se trompe. Fail-safe dans le sens
  « réveiller l'agent », jamais « skipper en silence » — comme les pré-gates du moteur.
- **Ne pas généraliser au corpus la doctrine du code.** Le contenu n'a pas de « faux positif
  gratuit » : une règle mécanique mal calibrée fait échouer une campagne entière. Chaque lot
  s'accompagne d'une sonde sur le corpus **avant** d'armer le gate, comme celle du §4.1.

  **Ce garde-fou a servi au premier lot, et il a fallu le renforcer.** La première version du
  flag `$…$` de LC1 utilisait `\S` pour exiger du non-espace contre les délimiteurs — or `\S`
  matche aussi `$` : le regex avalait le premier dollar d'une fermeture `$$` et flaguait une
  quarantaine de cours de primaire parfaitement corrects (`$$24 + 13 = 37$$`). La sonde de
  calibration, elle, avait annoncé « 0 inline » — parce qu'elle retirait les blocs `$$` avant de
  chercher, ce que le gate ne faisait pas. D'où la règle, désormais explicite : **une sonde ne
  vaut que si elle exécute le MÊME regex que le gate**, et un lot de gate se passe sur le corpus
  entier, en deux temps — sur l'état fautif (le détecteur trouve-t-il ce qu'il doit ?) puis sur
  l'état corrigé (ne trouve-t-il rien d'autre ?). Les deux passes sont dans arena#628.
