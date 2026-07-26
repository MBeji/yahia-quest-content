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
test -x ../engine/node_modules/.bin/tsc && test -e ../engine/content && echo "moteur prêt"
```

Absent ⇒ dérouler **Phase 0.1 de la méthode** (double clone, `npm ci`, les DEUX liens
`engine/content` et `engine/.claude/skills`, variante jonctions sous Windows) et **s'arrêter là si
un lien échoue** : sans corpus branché, toutes les commandes mentent par omission.

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

## 2. Demander — et seulement demander

Présente l'état **dans l'ordre du registre** (jamais réordonné), puis pose la question avec
`AskUserQuestion`. Règles de la question :

- une option = un couple, libellé `<niveau> / <matière>`, description = **le fait + l'étape**
  (ex. « partielle 48 %, 4 plages non lues — [LOT A A3] compléter la fiche ») ;
- les couples **bloquants** se présentent quand même, préfixés `⛔`, avec leur motif — l'humain doit
  voir pourquoi il ne peut pas les lancer tels quels ;
- **jamais** « (recommandé) », jamais un ordre autre que celui du registre, jamais un couple
  masqué parce qu'il te paraît moins utile ;
- au-delà de 4 couples plausibles, propose ceux du niveau demandé et laisse « Other » ouvert plutôt
  que d'en écarter selon ton propre critère ;
- l'humain peut aussi répondre un couple absent de la liste : c'est son droit, tu l'exécutes.

Choix d'un couple `en-cours` ⇒ redis qu'une autre session le tient (R-4), et **redemande**.

## 3. Dérouler l'étape prescrite

Avant tout : **branche fraîche depuis `origin/main` fetchée**, dans le corpus (A1/B1 de la méthode),
et re-vérifie la contention — `gh pr list --search "<niveau> <matière>"` + branches
`feat/transcription-<niveau>-*` — que `programme:etat` ne peut pas connaître.

| `prochaineEtape.etape` | Ce que tu déroules                                                        | Qui écrit                                                               |
| ---------------------- | ------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `A1`                   | LOT A complet : sources → transcription → profondeur → audits → PR        | `content-ingest`                                                        |
| `A3`                   | LOT A partiel : **uniquement les plages listées**, puis profondeur R-5    | `content-ingest`                                                        |
| `A5.4`                 | déclarer `sujets` (+ statut/couverture) au registre, régénérer la vue     | toi — édition du registre, aucun skill d'écriture                       |
| `B1`                   | LOT B : `subject.json` + **première tranche** de chapitres                | `content-ecole-tn` (carte `generation-pipeline.md`)                     |
| `B2`                   | LOT B : tranches suivantes, chapitres manquants ou incomplets             | idem + `content-cours`, `content-interactif`, `prof-<matière>-<cycle>`  |

Points de vigilance, tous hérités de la méthode :

- **LOT A** : fidélité absolue, jamais d'invention ; tranches de 10–20 pages écrites au format final
  (T-2) ; **jamais rouvrir un PDF déjà transcrit** (T-3) ; R-7 par sondage dirigé avant promotion.
- **LOT B** : la **fiche** est la source de scope et de contenu — on ne rouvre pas les PDF ; unité de
  travail = le chapitre, avec le brief matière + LA section de la fiche (T-5) ; tranches de ≤ 4
  chapitres complets, commit local par chapitre ; illustration systématique des notions spatiales.
- **A5.4** : `sujets` doit désigner des ids du manifeste du niveau — `programme:check` refuse le
  reste. Aucun sujet correspondant (matière hors programme codifié) ⇒ laisser `[]` et l'écrire en
  note, jamais inventer un id pour faire disparaître un constat.
- **Sous-agents** : un lot = un contexte frais (T-4). Délègue le lot à un sous-agent quand le harnais
  le permet, et garde le rôle d'orchestrateur mince.

## 4. Gates, PR, garde jusqu'au merge

Depuis `engine/`, 0 erreur exigé — `programme:check` pour un lot de fiche ; `content:check`,
`content:qa:strict`, `content:audit` (+ l'audit pédagogique `content-audit` sur les chapitres de la
tranche) pour un lot de contenu. **Aucun SQL, aucune migration** dans un commit de campagne : le
contenu se compile hors des migrations (méthode, B3).

Puis commit, push, `gh pr create --fill`. La chaîne de merge du dépôt merge une PR entièrement
verte ; tu restes **de garde** jusqu'au merge réel (surveiller, corriger les rouges, confirmer).
Sauvegarde d'une session interrompue : branche `wip/…` + PR draft.

## 5. Boucler, ou s'arrêter proprement

Merge confirmé ⇒ **re-établis l'état des lieux** (il a changé) et **redemande** — le couple suivant
est de nouveau un choix humain, y compris « on s'arrête ». À l'approche du budget ou de la fenêtre
de contexte : finir le palier poussable en cours, étiqueter honnêtement la profondeur atteinte,
pousser, rapporter le coût (T-9/T-10). Jamais de travail non poussé en fin de session.

Rapport de fin : par couple traité, la PR, la profondeur atteinte, le verdict R-7, le coût ; les
couples écartés et pourquoi ; ce qui reste. Le coût par chapitre publié est le KPI de l'étude 12.

## STOP — ne jamais improviser

Les conditions d'arrêt sont celles de la méthode (§ STOP) et s'appliquent telles quelles : doute sur
les **droits** d'une source hors corpus officiel, source introuvable, scan illisible, divergence
fiche ↔ programme officiel, LOT B sur une fiche restée sous la barre R-5, format de contenu
inexistant dans le moteur, budget insuffisant. Deux de plus, propres à ce point d'entrée :

- **l'humain n'a pas tranché** ⇒ on ne lance rien, on redemande ;
- **l'état des lieux n'a pas pu être établi** (corpus non branché, manifeste invalide) ⇒ on répare le
  préalable, on ne devine pas l'état.
