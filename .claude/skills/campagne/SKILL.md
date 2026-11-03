---
name: campagne
description: >-
  LA procédure unique de génération de contenu, du choix du couple à la production :
  état des lieux (`programme:etat`), question à l'humain (il choisit le couple
  niveau × matière), lecture des sources du Drive au moindre coût (texte d'abord,
  vision en dernier), fiche, puis chapitre par chapitre en un seul passage — cours
  au patron, exercices et missions tirées des examens nationaux —, audit, PR,
  publication. Remplace la méthode, le workflow de content-ingest et le mode
  gisement comme déroulé. Use whenever the user says « lance une campagne »,
  « /campagne », « on fait quoi ensuite en contenu ? », « continue », « transcris et
  génère <niveau> <matière> », « exploite les anciens examens ». Ne choisit JAMAIS le
  couple à la place de l'humain : il présente les faits, l'humain tranche.
---

# campagne — la procédure unique de génération de contenu

**Ce fichier est LA procédure** (décision de Mohamed du 2026-11-03 : *une seule procédure, simple,
claire, moins coûteuse*). Du choix du couple à la production, tout se fait ici, dans cet ordre. Les
autres documents ne sont plus des déroulés :

| Document | Ce qu'il reste | Quand le lire |
| --- | --- | --- |
| `content-engine` + ses `references/` | **règles d'écriture** (schéma, barre de qualité, patron de notion, figures, récompenses) | l'auteur et l'auditeur, au moment d'écrire ou de relire |
| `content-ecole-tn`, `prof-<matière>-<cycle>`, `content-cours`, `content-interactif` | règles d'écriture par programme et par matière | l'auteur |
| `content-ingest` | les règles de fidélité R-1…R-7 et les **consignes de rôle** du lecteur, des auteurs de mission et de l'auditeur (`references/gisement-*.md`) | les sous-agents de lecture et de mission |
| `FableEtudes/METHODE-GENERATION-CONTENU.md` | **annexe** : l'historique et le détail des règles citées (R-x, T-x, § B2…) | jamais en entier ; seulement un paragraphe cité |
| `FableEtudes/PILOTAGE.md` | la **priorité** (§ 0) et le **tableau de bord** des couples | au début, et mis à jour dans chaque PR |

En cas de désaccord : **AGENTS.md du moteur → règles d'écriture → ce fichier → l'annexe**.

**Les cinq règles qui ne bougent pas.**

1. **L'humain choisit le couple.** Tu présentes les faits et tu demandes ; jamais « je recommande »,
   jamais de priorité de ton cru (la seule est celle du `PILOTAGE.md` § 0). Pas de réponse ⇒ rien ne
   se lance.
2. **Fidélité.** Rien d'inventé ; le programme officiel gagne ; `[?]` pour l'illisible.
3. **Une étape ne se refait pas.** Une page lue ne se relit pas, un chapitre a un seul auteur à la
   fois, un audit fait se cite.
4. **Aucun SQL, aucune migration, jamais `content:build`** dans le corpus.
5. **Fini = en production**, pas au merge.

---

## Étape 1 — Préparer (une fois par session)

Deux clones côte à côte, le corpus (ici, où l'on commite) et le moteur `../engine` (où l'on lance les
commandes), reliés par un lien :

```bash
test -x ../engine/node_modules/.bin/tsc && test -f ../engine/content/misconceptions.json && echo "branché"
git -C ../engine fetch -q origin && git -C ../engine rev-list --count HEAD..origin/main   # doit rendre 0
```

Absent ⇒ `git clone` des deux dépôts, `npm ci` dans le moteur, `ln -s "$PWD/content" ../engine/content`
(jamais `rm -rf` sur un lien). Un moteur en retard rend des verdicts faux dans les deux sens : le
mettre à jour avant tout gate.

**La source** (seulement si l'étape choisie lit un document) : le connecteur Google Drive doit voir le
dossier `cnp-officiel` — `search_files` avec `title = 'index.csv'` rend l'inventaire. « Requested
entity was not found » ⇒ le connecteur est sur un autre compte : le dire et s'arrêter.

## Étape 2 — Choisir (l'humain tranche)

```bash
cd ../engine && npm run programme:etat -- --json      # ou --grade <niveau> si l'humain l'a nommé
```

Par couple : fiche (statut, couverture, plages non lues), contenu (chapitres présents/attendus) et
`prochaineEtape` (l'étape à faire **si** on choisit ce couple).

**Qui tient déjà le couple ?** Avant de présenter, depuis le corpus, les trois pattes — chacune voit ce
que les autres ratent :

```bash
git fetch --prune -q origin
git worktree list                                                     # sessions de cette machine
git branch -r --no-merged origin/main | grep -iE "(<matière FR>|<préfixe sujet>)" | grep -i "<niveau>"
gh pr list --state open --limit 50 --json number,title,headRefName,isDraft   # tout lire, ne rien filtrer
```

Le nom de matière change de langue d'une branche à l'autre (`anglais`/`english`) et le préfixe de
branche n'est pas normalisé : greper les deux noms, jamais un préfixe. Un couple trouvé est **TENU** :
il se présente quand même, préfixé `⚠️ TENU par <branche ou #PR>`.

**Présenter** dans l'ordre du `PILOTAGE.md` § 0 (depuis le 2026-11-03 : le Bac d'abord, matières
principales en tête), puis l'ordre du registre. Question par `AskUserQuestion` : une option = un couple
`<niveau> / <matière>`, description = le fait + l'étape (« complète, 13/25 — écrire ch. 14-16 »). Un
couple bloquant se présente préfixé `⛔`, avec ce qui reste faisable (« ⛔ génération interdite —
compléter la fiche »). Plus de 4 couples ⇒ ceux du niveau demandé, « Other » ouvert. Les matières
annexes (musique, dessin, EPS, 3ᵉ langue) se refusent. Un couple imposé directement (« finalise
l'anglais de 2ème ») se scanne **aussi** avant la première ligne de travail.

Choix fait ⇒ **branche fraîche** depuis `origin/main`, poussée tout de suite sur `wip/<couple>` : c'est
la réservation (visible des trois pattes). Le statut `en-cours` du registre ne se pose **que** pour
une fiche qui n'existe pas encore — sur une fiche exploitée, il coupe la génération pour tout le monde.

## Étape 3 — Lire les sources, une seule fois (seulement si la fiche manque ou est partielle)

**Où :** le dossier Drive `cnp-officiel`
(<https://drive.google.com/drive/folders/1ZUUgEx71bKFsXulk_WL7cSfNxc6U9tmX>) : `index.csv` (l'inventaire,
`cycle,classe,type,code,file,bytes,status` ; classe 4 du cycle 2 = Bac), `manuels/` (`<code><tome>.pdf`),
`_txt/` (textes déjà extraits), `_render/` (pages déjà rendues en PNG `<code><tome>-NNN.png`). Trouver
un fichier : `search_files` avec `title = '<code><tome>.pdf'`. Le site du CNP n'est plus la source
(injoignable en cloud). Absent du Drive ⇒ le demander à Mohamed.

**Comment, au moindre coût — chaque page au premier barreau qui suffit :**

| Barreau | Quand | Comment |
| --- | --- | --- |
| L0 | `_txt/<code><tome>-*.txt` existe | `read_file_content` sur le `.txt` |
| L1 | manuel en français ou en anglais (tout le Bac scientifique) | `read_file_content` sur le PDF : prose propre ; formules et figures perdues |
| L2 | manuel arabe à polices propriétaires (sortie brouillée) | `read_file_content` puis la table glyphe → lettre de la fiche (`programme/6eme-base/arabe.md` § 7) |
| L3 | formules, tableaux, figures, encadrés vocalisés, pages sans texte, **et** le sondage | vision sur le PNG de `_render/` |

Au-delà d'environ 80 000 caractères, `read_file_content` écrit son résultat dans un fichier local :
le traiter en sous-agent (`python3 -I`). Jamais `download_file_content` sur un PDF. Le texte n'a pas de
marqueur de page fiable : ancrer chaque passage sur le numéro imprimé.

**Compte comme lu** au registre une page lue en L0-L2 **après un sondage image** : ≥ 1 page sur 10,
parmi les plus denses, confrontée au PNG, 0 écart substantiel (un écart ⇒ sonder la section entière,
trois ⇒ la lire en L3). Le sondage se note dans la fiche. Règle validée par Mohamed le 2026-11-03 ; elle
remplace celle du 2026-09-22 (« une couverture par décodage n'est pas une lecture ») : une fiche à 100 %
restée `partielle` pour ce seul motif (5ᵉ et 6ᵉ arabe) passe à `complete` une fois le sondage fait et noté.

**Ce qu'on écrit :** la fiche `content/programmes-officiels/programme/<niveau>/<matière>.md`, à
**profondeur de génération** — chaque activité décrite (énoncé, données, demande), les encadrés de
règles verbatim, le vocabulaire officiel, les bornes INCLUS/EXCLU, et le chapitrage codifié dans
`manifest/<niveau>.json`. Guide enseignant pour le scope, manuel élève pour le contenu. Puis le
registre `suivi/<niveau>.json` (statut, plages `pagesLues`, sondage) et
`npm run programme:index && npm run programme:check` (0 erreur). Un auditeur opus relit 100 % des
encadrés et du chapitrage et ≥ 15 % des pages contre la source (R-7) avant le passage à `complete`.
Une fiche se livre dans sa propre PR (étape 6), sans rien publier.

Les **sujets des examens nationaux** du couple (concours de 6ᵉ, de 9ᵉ, Bac — corpus officiel, repris et
cités) se lisent **dans la même passe** : transcription fidèle sous
`content/programmes-officiels/examens-nationaux/<classe>/<matière>/<session>.md`, archive du Ministère
d'abord (fiche `web-echoexam-edunet-tn`). Toutes les sessions publiées pour la matière ; le lecteur
marque celles d'un programme ancien.

Une étape `A5.4` (déclarer les `sujets` d'une fiche) se fait sans lecture : éditer le registre avec
des ids du manifeste du niveau, jamais inventés (`[]` + note si aucun).

## Étape 4 — Écrire, chapitre par chapitre, en un seul passage

La **fiche** est la seule source de l'auteur : on ne rouvre pas les PDF. Unité de travail : **le
chapitre**, par **tranches de 3** (jamais plus de 4 non poussés), **un auteur par chapitre** en
parallèle (≤ 4 sous-agents). Chaque auteur produit, pour son chapitre et lui seul :

- `chapter.json`, `cours.md` **au patron de notion** (ancrer → nommer → voir → exemple résolu →
  erreur typique → règle → `::: verifie` ; `content-engine/references/course-explanation.md`),
  `resume.md`, `quiz.json`, les quatre exercices de la ladder (pratique, boss, révision, défi) ;
- **les missions des examens nationaux rattachés à ce chapitre** — une mission par exercice d'examen,
  placée au chapitre le plus avancé qu'il mobilise, reprise fidèlement et citée dans `sources[]`
  (consigne de rôle : `content-ingest/references/gisement-auteur-examen.md`).

Le brief de chaque auteur contient : la section de la fiche de son chapitre, les fichiers exacts qu'il
écrit, le chemin des **chapitres déjà publiés** de la matière (à lire avant d'écrire, pour changer la
**tâche** et pas seulement le décor), les sessions d'examen à reprendre, et la liste des défauts
récurrents ci-dessous. Il valide seul son chapitre (`content:check`, `content:qa:strict`,
`content:figures:check`, `content:tranche -- --changed --fresh --strict-lessons`) avant de rendre.

**Défauts récurrents à éviter dès l'écriture** (mesurés par les audits de 2026) : cours qui se
contredit (tableau, exemple, piège, résumé) ; règle énoncée en absolu ; distracteur absurde, contredit
par l'énoncé ou synonyme d'un autre ; clé la plus longue, la plus courte, ou seule à porter une marque ;
option « consensus » ; explication qui cite une option par son rang ; question qui en révèle une autre
ou qui rejoue le `::: verifie` ; difficulté 3 sur du rappel ; notion testée non enseignée ; plus de 8
notions par chapitre ; légende qui cite un repère absent du dessin ; valeur d'illustration non annoncée
comme telle.

**Devoirs d'établissement en ligne** (sites d'enseignants) : **seulement si l'humain le demande**. Ils
sont une source web — rien n'en est repris : un lecteur rend une ligne anonyme par exercice, un auteur
écrit une mission neuve par archétype sans voir la source, et le contrôle local le prouve (aucune
plage de ≥ 8 mots, pas 3 nombres non triviaux d'un même exercice). Échantillon fixé et mergé **avant**
toute lecture : vagues de neuf devoirs, ≤ 2 par auteur, une vague de plus seulement si la précédente a
apporté ≥ 30 % de signatures neuves. Consignes : `gisement-lecteur.md`, `gisement-auteur-devoir.md`,
registre `sources-externes/web-<couple>/gisement.json`.

## Étape 5 — Vérifier : un audit, une reprise

```bash
cd ../engine && npm run content:gates -- --tranche     # 7 étages + mesures de tranche, 0 erreur
```

`content:catalogue` régénère `content/CATALOGUE.md` : le committer avec la tranche.

Puis **un auditeur opus par chapitre**, en contexte vierge (`content-audit` ; pour les missions,
`gisement-auditeur.md`) : il re-résout chaque question à l'aveugle (calculs refaits), cherche les
indices de forme, les doublons avec les chapitres publiés et frères, les contradictions du cours, la
vérité des figures, la fidélité à la fiche. Il rend BLOCKER / MAJOR / MINOR avec la correction précise.

Les corrections reviennent à **l'auteur du chapitre** (par `SendMessage` : il a gardé son contexte, ça
coûte une fraction d'une réécriture). Puis le **même auditeur** revérifie **seulement les points
corrigés** et les questions réécrites — pas de second audit complet. Une clé fausse ou un BLOCKER
restant ⇒ la tranche ne part pas.

## Étape 6 — Livrer et publier

On ne change **jamais** de branche dans l'arbre où des auteurs écrivent : la livraison se fait depuis
la branche de la session, poussée une fois les gates et l'audit verts.

```bash
git add content/… && git commit -m "feat(<sujet>): ch.NN-MM …"    # fichiers content/ seuls
git push -u origin <branche>           # auto-pr.yml ouvre la PR ; automerge.yml la merge au vert
```

Tu restes de garde jusqu'au merge réel (corriger un rouge, rebaser sur `main` si une PR intermédiaire
a été mergée). **Puis publier** — un merge n'applique rien :

```bash
gh workflow run apply-content.yml -f subjects="<subject-id>" -f dry_run=true     # le plan
gh workflow run apply-content.yml -f subjects="<subject-id>" -f dry_run=false    # l'application
```

`subjects` toujours renseigné (vide = tout le corpus, ~45 min de charge). Vérifier les étapes
« Appliquer », « Vérifier en base », « Journaliser », puis l'issue `content-drift` close. Un lot de
fiche ne publie rien.

Mettre à jour dans la même PR : le registre du couple (missions `publiee`) et la ligne du couple au
`PILOTAGE.md`. **Première tranche d'une classe** ⇒ son parcours reste `coming_soon` tant qu'une
migration `open_<parcours>` n'est pas mergée **au moteur** (PR distincte, avec son pgTAP) : la porter
si l'humain le demande, sinon la signaler nommément comme reste à faire.

## Étape 7 — Boucler

Merge publié ⇒ refaire l'étape 2 et **redemander** (le couple suivant est un choix humain, « on
s'arrête » compris). Fin de budget ⇒ finir le chapitre en cours, pousser sur `wip/`, étiqueter
honnêtement. Rapport : par couple, la PR, ce qui est publié, les restes, ce qui attend l'humain.

## Les modèles : le moins cher qui tient la tâche (décision du 2026-11-03)

Le modèle se passe **explicitement** à chaque sous-agent (`model` de l'outil Agent ou d'un `agent()`
de workflow) ; un sous-agent n'hérite jamais par défaut de l'orchestrateur, dont le modèle est le
choix de l'humain (`/model`). Familles par nom court ; les identifiants exacts ne vivent que dans
`harness/models.json` du moteur.

| Tâche | Famille |
| --- | --- |
| Inventaire, recherche Drive, extraction et décodage de la couche texte, comptages, scan, extraction des constats d'un long rapport | **haiku** |
| Lecture vision (L3), sondage image, lecteur de devoirs ou d'examens (classement en archétypes) | **sonnet** (opus pour l'arabe vocalisé ou le manuscrit) |
| Auteur de chapitre et de missions, correcteur qui applique un audit | **sonnet** |
| Auditeur de tranche, relecture R-7 de fiche, fiche à profondeur de génération | **opus** |
| Gates, git, PR, publication | aucun sous-agent (scripts) |

Escalade d'un cran, jamais d'emblée : un chapitre qui échoue deux fois aux gates ou garde un BLOCKER
passe à un auteur opus ; un texte inexploitable passe au barreau de vision.

## STOP — ne jamais improviser

- l'humain n'a pas tranché ⇒ redemander ;
- l'état des lieux n'a pas pu être établi (moteur non branché, manifeste invalide) ⇒ réparer d'abord ;
- doute sur les droits d'une source hors corpus officiel ⇒ elle sort ;
- source absente du Drive, page illisible, divergence fiche ↔ programme ⇒ le dire, ne pas deviner ;
- génération demandée sur une fiche sous la barre (statut `partielle` sans chapitre générable) ⇒
  compléter la fiche d'abord ;
- clé fausse à l'audit ⇒ la tranche ne part pas ; tranche mergée mais pas publiée ⇒ pas finie.
