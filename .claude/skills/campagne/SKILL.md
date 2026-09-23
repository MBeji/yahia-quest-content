---
name: campagne
description: >-
  Point d'entrée UNIQUE d'une campagne de contenu : établit l'état des lieux vérifié
  (`programme:etat` — fiche × programme × contenu), DEMANDE à l'humain quel couple
  niveau × matière lancer, puis déroule la chaîne complète de la méthode pour ce
  couple — LOT A (transcription de la source) et/ou LOT B (génération du contenu) —
  en appelant les bons skills (content-ingest, content-ecole-tn, content-cours,
  content-interactif, prof-*), en passant les gates, en tenant le registre et en
  poussant la PR jusqu'à son merge. Use whenever the user says « lance une campagne »,
  « /campagne », « on fait quoi ensuite en contenu ? », « état des lieux et on y va »,
  « continue la campagne », « transcris et génère <niveau> <matière> ». Ne choisit
  JAMAIS le couple à la place de l'humain : il présente les faits, l'humain tranche.
---

# campagne — établir l'état, demander, dérouler

**Rôle.** Une seule entrée pour toute la chaîne contenu. Tu **orchestres** : tu ne réinventes ni la
méthode, ni les règles d'authoring. La référence de processus est
[`FableEtudes/METHODE-GENERATION-CONTENU.md`](../../../FableEtudes/METHODE-GENERATION-CONTENU.md)
(boucle, lots, profils, socle R-1…R-7, charte tokens T-1…T-10) ; la carte des skills d'écriture est
[`content-engine/references/generation-pipeline.md`](../content-engine/references/generation-pipeline.md).
En cas de désaccord : **AGENTS.md du moteur → skills & docs normatifs → la méthode → ce skill**.

**Ce que tu ne fais jamais.** Choisir le couple. L'outillage établit les faits — statut, couverture,
trous, contenu présent ou non, et **l'étape que la méthode prescrit pour ce couple** — mais
« par quoi on commence » est une décision humaine (méthode, Phase 0.4 ; décision du 2026-07-26).
Tu présentes, tu demandes, tu exécutes. Aucun « je recommande », aucun tri par priorité, aucun
« je lance le plus rentable ». Si l'humain ne répond pas, tu ne lances rien.

---

## 0. Préalables (une fois par session)

La campagne a besoin des **deux dépôts** (étude 24) : ce dépôt (le corpus, où tout se commite) et le
moteur public (les commandes). Vérifie, depuis la racine du corpus :

```bash
test -x ../engine/node_modules/.bin/tsc &&
  test -f ../engine/content/misconceptions.json &&
  test -d ../engine/content/programmes-officiels/manifest &&
  echo "moteur + corpus + skills branchés"
```

Ce sont les **deux assertions de la Content CI** (méthode, Phase 0.1) : tester la seule existence de
`engine/content` dirait « prêt » avec le lien des skills manquant, et `programme:etat` échouerait la
commande suivante. Absent ⇒ dérouler **Phase 0.1 de la méthode** (double clone, `npm ci`, les DEUX
lien `engine/content` — un seul depuis l'étude 32, variante jonction sous Windows) et **s'arrêter là
si un lien échoue** : sans corpus branché, toutes les commandes mentent par omission.

⚠️ **Branché ne suffit pas : le moteur doit être à JOUR.** Les gates tournent avec le code du
clone moteur, donc un clone en retard rend un verdict qui n'engage personne — **dans les deux
sens**. Mesure-le, ne le suppose pas :

```bash
git -C ../engine fetch -q origin && git -C ../engine rev-list --count HEAD..origin/main  # doit rendre 0
```

Un **vert** de trop : le clone n'a pas la garde qui aurait crié (constaté avec 167 commits de
retard). Un **rouge** de trop, plus traître parce qu'il ressemble à du travail à faire : le
2026-09-01, `content:figures:check` signalait 32 figures invalides dans trois matières — toutes
déjà réparées en amont (arena #936), sur un clone à 7 commits de retard. Conclure sans avoir
mesuré ce retard, c'est ouvrir un lot pour réparer ce qui l'est déjà.

Un LOT A a un second préalable — **ScribeKit construit** (méthode, Phase 0.2), le déterministe qui se
paie une fois (T-1) :

```bash
test -f ../ScribeKit/dist/bin.js && echo "scribekit prêt"
```

Absent ⇒ clone + `npm install && npm run build` avant d'ouvrir le moindre PDF. Un LOT B seul
(profil sans-source) n'en a pas besoin.

Rappels de posture, valables tout du long :

- **`npm run …` depuis `engine/`**, **`git`/`gh` depuis le corpus**. Le corpus n'a pas de
  `package.json`, pas de husky, pas de Prettier — rien ne s'y formate au commit.
- Une jonction/lien ne se supprime **jamais** par `rm -rf` (ça viderait le corpus).

## 1. Établir l'état des lieux

```bash
cd ../engine && npm run programme:etat -- --json          # tout ; ou --grade <niveau>
```

Tu obtiens, par couple : l'état de la **fiche** (statut, profondeur, couverture calculée, plages non
lues, R-7, génération autorisée), l'état du **contenu** (sujet présent, chapitres couverts/attendus,
incomplets), les **constats**, et **`prochaineEtape`** — `{ lot, etape, action, motif, bloquant }`,
c'est-à-dire ce que la méthode prescrit **si** on choisit ce couple.

Restreins avec `--grade` quand l'humain a déjà nommé un niveau : c'est du budget de contexte gagné
(T-6), pas une présélection.

**Limite assumée du point d'entrée.** L'état des lieux se calcule sur le registre et les manifestes :
il ne voit que les profils `ecole-cnp`, `ecole-secondaire` et `sans-source`. Un **document-libre**
(PDF d'enseignant, polycopié, annales papier) n'a ni ligne de registre ni couple à proposer — il se
traite hors `/campagne`, par la méthode (§ Profils, checklist droits R-2) et `content-ingest`, sur
demande explicite de l'humain. Ne l'invente pas dans la liste des options.

### 1 bis. Qui travaille déjà dessus — à faire AVANT de présenter quoi que ce soit

`programme:etat` lit le registre et les manifestes : il ne voit **que `main`**. Il ne peut pas savoir
qu'une autre session tient déjà un couple. Ce scan-là est le seul qui le sache, et il se lance
**avant** l'étape 2, parce qu'il change ce qu'on a le droit de proposer.

```bash
cd <corpus> && git fetch --prune -q origin
GR=2eme-sec ; MA=anglais ; SU=english        # SU = préfixe des ids de sujet (english/french/math…)

git worktree list                                                    # (1) sessions de CETTE machine
git branch -r --no-merged origin/main | grep -iE "($MA|$SU)" | grep -i "$GR"   # (2) travail poussé
gh pr list --state open --limit 50 --json number,title,headRefName,isDraft     # (3) travail déclaré
```

**Les trois pattes sont nécessaires, et chacune rattrape ce que les autres ratent** — mesuré sur ce
dépôt le 2026-08-31 :

| Patte | Ce qu'elle voit | Ce qu'elle rate |
| --- | --- | --- |
| (1) `git worktree list` | une session de la même machine **avant tout push** — le seul signal précoce | une session sur une autre machine |
| (2) branches non mergées | du travail poussé **sans PR** — `bac × anglais` avait 4 branches vivantes et **zéro PR ouverte** | ce qui n'est pas encore poussé |
| (3) PR ouvertes | le travail déclaré, avec son état draft/wip | ce qui n'a pas encore de PR |

⚠️ **Deux pièges de filtrage, tous deux constatés :**

- **le nom de matière change de langue selon la branche** — `feat/programme-**anglais**-2eme-sec-…`
  et `feat/content-**english**-2eme-sec-…` désignent le même couple. Grepper l'un sans l'autre rate
  la moitié du travail. D'où les deux jetons `$MA|$SU`.
- **le préfixe de branche n'est pas normalisé** : `feat/content-`, `feat/programme-`, `claude/`,
  `wip/` sont tous en usage. Ne filtre **jamais** sur un préfixe.

⚠️ **`--no-merged origin/main` n'est pas cosmétique** : sans lui le scan remonte tout l'historique du
couple et noie le travail vivant sous les branches finies.

⭐ **La patte (3) ne filtre volontairement rien** : elle liste **toutes** les PR ouvertes et c'est toi
qui lis. Le dépôt en compte une poignée, et un filtre `--search` ou `jq` mal quoté rend un tableau
vide — c'est-à-dire le message « personne ne travaille dessus », qui est exactement la panne qu'on
répare ici. Une liste courte à relire vaut mieux qu'un filtre qui peut mentir.

**Ce que tu en fais** : tout couple qui ressort d'une des trois pattes est **TENU**. Il se présente
quand même à l'étape 2 — masquer une option n'est jamais permis — mais préfixé `⚠️ TENU par
<branche ou #PR>`, et l'humain arbitre en connaissance de cause.

## 2. Demander — et seulement demander

Présente l'état **dans l'ordre du registre** (jamais réordonné), puis pose la question avec
`AskUserQuestion`. Règles de la question :

- une option = un couple, libellé `<niveau> / <matière>`, description = **le fait + l'étape**
  (ex. « partielle 48 %, 4 plages non lues — [LOT A A3] compléter la fiche ») ;
- les couples **bloquants** se présentent quand même, préfixés `⛔`, avec leur motif **et l'étape
  prescrite** : `bloquant` veut dire « pas lançable **tel quel** », pas « pas lançable ». Un couple
  `en-cours` est réellement fermé (réservé par une session) ; un couple sous la barre R-5 a la
  **génération** interdite, mais son étape `A3` — compléter la fiche — est parfaitement lançable et
  se libelle « ⛔ génération interdite — [LOT A A3] compléter la fiche (4 plages non lues) » ;
- **jamais** « (recommandé) », jamais un ordre autre que celui du registre, jamais un couple
  masqué parce qu'il te paraît moins utile ;
- au-delà de 4 couples plausibles, propose ceux du niveau demandé et laisse « Other » ouvert plutôt
  que d'en écarter selon ton propre critère ;
- l'humain peut aussi répondre un couple absent de la liste : c'est son droit, tu l'exécutes — à
  une exception, les **matières annexes hors périmètre** (musique, éducation artistique/dessin,
  EPS et la section sport, 3èmes langues : allemand, espagnol, italien). Celles-là ne se proposent
  pas et se **refusent** si elles sont demandées, en rappelant la règle (méthode, Phase 0.4) ; puis
  tu redemandes.

Choix d'un couple `en-cours` ⇒ redis qu'une autre session le tient (R-4), et **redemande**.

⚠️⚠️ **Le scan 1 bis vaut aussi — et surtout — quand le couple ne vient pas de la question.** Le cas
qui a coûté le plus cher n'est pas celui d'un humain qui choisit mal dans une liste : c'est celui
d'une session à qui l'on confie directement un couple (« finalise l'anglais de 2ème année »), qui
saute donc l'étape 2, et avec elle le contrôle qui vit en dessous. **Un couple imposé se scanne
avant la première ligne de travail**, exactement comme un couple choisi ; s'il ressort TENU, tu le
dis et tu attends l'arbitrage plutôt que de démarrer en parallèle.

Coût mesuré du contraire, le 2026-08-31 sur `2eme-sec × anglais` : une fiche LOT A entière écrite
puis jetée, et **85 questions générées deux fois** par deux sessions qui s'ignoraient.

## 3. Dérouler l'étape prescrite

Avant tout : **branche fraîche depuis `origin/main` fetchée**, dans le corpus (A1/B1 de la méthode),
et **rejoue le scan 1 bis** — entre la question et le premier commit, une autre session a pu pousser.

> ⚠️ **Ce paragraphe prescrivait jusqu'au 2026-08-31 un contrôle qui ne marchait pas**, et c'est
> pire qu'aucun contrôle, parce qu'il rend une réponse vide avec assurance. Il demandait
> `gh pr list --search "<niveau> <matière>"` — sur `2eme-sec anglais`, cette requête ne remontait
> **aucune** des PR concurrentes, les titres étant écrits « english-2eme-sec » ou « anglais 2ème
> sec » — et un grep sur `feat/transcription-<niveau>-*`, préfixe qu'**aucune** des huit branches
> réelles du couple ne portait ; sur `2eme-sec` il ne trouvait qu'une branche **de français**.
> La version 1 bis a été construite contre ces branches-là et vérifiée sur trois couples.

| `prochaineEtape.etape` | Ce que tu déroules                                                     | Qui écrit                                                              |
| ---------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `A1`                   | LOT A complet : sources → transcription → profondeur → audits → PR     | `content-ingest`                                                       |
| `A3`                   | LOT A partiel : **uniquement les plages listées**, puis profondeur R-5 | `content-ingest`                                                       |
| `A5.4`                 | déclarer `sujets` (+ statut/couverture) au registre, régénérer la vue  | toi — édition du registre, aucun skill d'écriture                      |
| `B1`                   | LOT B : `subject.json` + **première tranche** de chapitres             | `content-ecole-tn` (carte `generation-pipeline.md`)                    |
| `B2`                   | LOT B : tranches suivantes, chapitres manquants ou incomplets          | idem + `content-cours`, `content-interactif`, `prof-<matière>-<cycle>` |

Points de vigilance, tous hérités de la méthode :

- **LOT A** : fidélité absolue, jamais d'invention ; tranches de 10–20 pages écrites au format final
  (T-2) ; **jamais rouvrir un PDF déjà transcrit** (T-3) ; R-7 par sondage dirigé avant promotion.
- **LOT B** : la **fiche** est la source de scope et de contenu — on ne rouvre pas les PDF ; unité de
  travail = le chapitre, avec le brief matière + LA section de la fiche (T-5) ; tranches de **3
  chapitres complets par défaut, jamais plus de 4 non poussés** (T-10), commit local par chapitre ;
  illustration systématique des notions spatiales.
- **A5.4** : `sujets` doit désigner des ids du manifeste du niveau — `programme:check` refuse le
  reste. Aucun sujet correspondant (matière hors programme codifié) ⇒ laisser `[]` et l'écrire en
  note, jamais inventer un id pour faire disparaître un constat.
- **Sous-agents** : un lot = un contexte frais (T-4). Délègue le lot à un sous-agent quand le harnais
  le permet, et garde le rôle d'orchestrateur mince. Écriture parallèle ⇒ **périmètre nommé** par
  agent **et chemin des chapitres déjà publiés**, sinon le moule d'un item se rejoue d'un chapitre à
  l'autre : c'est le défaut n°1 des tranches livrées (méthode, B2 « le doublon de gabarit »).
  Avant chaque commit : `npm run content:tranche -- --changed` — les trois mesures muettes **et**
  les candidats gabarit, croisés avec les chapitres publiés ; ses groupes vont au mandat de
  l'auditeur.

## 4. Gates, PR, garde jusqu'au merge

Depuis `engine/`, 0 erreur exigé — **`npm run content:gates -- --tranche`** rejoue d'un coup les sept
étages de la Content CI (dont `programme:check` pour un lot de fiche ; `content:check`,
`content:qa:strict`, `content:audit` pour un lot de contenu) et les mesures de tranche, et mesure le
retard du moteur (§ 0) — (+ l'audit pédagogique `content-audit` sur les chapitres de la
tranche — **un auditeur par chapitre, en contexte vierge, qui n'a rien écrit de ce qu'il relit** ;
les quatre points de son mandat sont en B3 de la méthode) pour un lot de contenu. Un gate vert ne
dit rien du fond : sur deux tranches d'anglais 1ère sec, les quatre gates étaient verts, les
138 clés justes, et l'audit a trouvé 5 BLOCKER et 33 MAJOR.

**Aucun SQL, aucune migration** dans un commit de campagne : le
contenu se compile hors des migrations (méthode, B3). ⚠️ Et **jamais `npm run content:build`** :
sans `--sql-dir` il écrit des migrations horodatées dans le dépôt **moteur** — canal mort depuis
l'étude 24, et une fuite de corpus que son gate `leak:check` bloque.

Puis commit, push, `gh pr create --fill`. La chaîne de merge du dépôt merge une PR entièrement
verte ; tu restes **de garde** jusqu'au merge réel (surveiller, corriger les rouges, confirmer).
Sauvegarde d'une session interrompue : branche `wip/…` + PR draft.

**Puis publier — un merge n'applique rien.** Contrairement au canal schéma du moteur,
`apply-content.yml` est en `workflow_dispatch` **seul** (méthode, B3) : une tranche de contenu mergée
reste invisible en prod tant qu'on ne l'a pas dispatchée, depuis le corpus :

```bash
gh workflow run apply-content.yml -f subjects="<subject-id>" -f dry_run=true    # le plan
gh workflow run apply-content.yml -f subjects="<subject-id>" -f dry_run=false   # l'application
```

Vérifier le run vert **et** la ligne journalisée dans `content_releases` (l'application est
idempotente : un run rouge ou coupé se redispatche, jamais de rattrapage à la main). Sans droit de
dispatch : s'arrêter au merge et le dire. Un lot de **fiche** (LOT A) ne publie rien.

**Première tranche complète d'une classe ⇒ ouvrir la classe en production** (R-8, règle d'ouverture
du 2026-07-19) : on n'attend pas la matière complète — bascule `coming_soon → available`, les
chapitres suivants, d3/d4 et annales s'ajoutent en continu sans bloquer.

⚠️ **Mais l'ouverture n'est pas un geste de campagne.** La bascule est une **migration `open_*` du
dépôt moteur** — une par section (R-8) —, donc une **PR distincte, sur l'autre dépôt**, avec son
test pgTAP et le gate `verify` :

```
supabase/migrations/<horodatage>_open_<parcours>_parcours.sql   # UPDATE parcours … available
supabase/tests/NN_open_<parcours>_parcours.test.sql             # le pgTAP qui l'atteste
```

Elle ne va **jamais** dans la PR de campagne (§ B3 : aucun SQL, aucune migration dans le corpus) et
ne se déclenche qu'après le merge **et** l'application vérifiée de la tranche. Tu la portes en PR
moteur si l'humain te le demande ; sinon tu la **rapportes comme reste à faire** (§ 5), nommément —
une classe dont le contenu est en base mais le parcours resté `coming_soon` est invisible pour les
élèves, et rien dans les gates ne le signale.

## 4 bis. Poser — et ne pas poser — la réservation `en-cours`

Le registre porte un statut de réservation, `en-cours` (« réservé par une session »). L'étape 2 sait
**le lire** ; encore faut-il que quelqu'un l'**écrive**. Personne ne le faisait : au 2026-08-31,
**zéro fiche** du dépôt était marquée `en-cours`.

**Quand l'écrire** : à l'ouverture d'un **LOT A sur une fiche qui n'existe pas encore**, ou dont
rien n'est encore générable. Tu écris `"statut": "en-cours"`, tu commites, **tu pousses tout de
suite** — une réservation qui dort sur une branche locale ne réserve rien — et tu la remplaces par
le vrai statut en fin de lot.

⚠️⚠️ **Quand ne PAS l'écrire, et c'est impératif.** `en-cours` n'est pas un drapeau « je travaille
ici » : il **coupe la génération pour tout le monde**. Le moteur est explicite —

```ts
export function chapitresGenerables(entry: FicheEntry): string[] {
  if (generationAutorisee(entry)) return [];
  if (entry.statut === "en-cours") return [];   // ← la levée R-5 disparaît
  return entry.chapitresGeneration;
}
```

Posé sur une fiche `partielle` dont `chapitresGeneration` est peuplé, il **rend non générables des
chapitres qui l'étaient**, y compris pour la session qui les génère légitimement. Donc : `en-cours`
**ne réserve jamais un LOT B**, et ne se pose jamais sur une fiche déjà exploitée.

**Pour un LOT B, la réservation est le scan 1 bis**, pas un statut : une branche poussée tôt (même
vide) est visible par les trois pattes, ne casse rien, et n'a pas besoin d'être relâchée.
⚠️ Et **`_tranches-wip/` n'est pas un verrou** : c'est un sas de sauvegarde de transcriptions brutes,
avec son propre contrat (voir son README). Ne l'utilise pas pour signaler du travail en cours.

## 5. Boucler, ou s'arrêter proprement

Merge confirmé ⇒ **re-établis l'état des lieux** (il a changé) et **redemande** — le couple suivant
est de nouveau un choix humain, y compris « on s'arrête ». À l'approche du budget ou de la fenêtre
de contexte : finir le palier poussable en cours, étiqueter honnêtement la profondeur atteinte,
pousser, rapporter le coût (T-9/T-10). Jamais de travail non poussé en fin de session.

Rapport de fin : par couple traité, la PR, la profondeur atteinte, le verdict R-7, le coût, l'état
de la **publication** (dispatch appliqué, ligne `content_releases`) et celui de l'**ouverture**
(migration `open_*` portée, ou à faire — dis-le nommément, personne d'autre ne le verra) ; les
couples écartés et pourquoi ; ce qui reste. Le coût par chapitre publié est le KPI de l'étude 12.

## STOP — ne jamais improviser

Les conditions d'arrêt sont celles de la méthode (§ STOP) et s'appliquent telles quelles : doute sur
les **droits** d'une source hors corpus officiel, source introuvable, scan illisible, divergence
fiche ↔ programme officiel, LOT B sur une fiche restée sous la barre R-5, format de contenu
inexistant dans le moteur, budget insuffisant. Deux de plus, propres à ce point d'entrée :

- **l'humain n'a pas tranché** ⇒ on ne lance rien, on redemande ;
- **l'état des lieux n'a pas pu être établi** (corpus non branché, manifeste invalide) ⇒ on répare le
  préalable, on ne devine pas l'état.
