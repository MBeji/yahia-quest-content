# Mode gisement — le déroulé de l'orchestrateur (étude 36)

Examens nationaux et devoirs en ligne → exercices, pour UN couple classe × matière. Spécification
et décisions : `FableEtudes/36-gisement-examens-devoirs/ETUDE.md` ; résumé dans la méthode
(§ Le gisement). Ce fichier dit **quoi faire, dans quel ordre, avec quelles commandes**. Les
consignes de rôle sont à côté : `gisement-lecteur.md`, `gisement-auteur-devoir.md`,
`gisement-auteur-examen.md`, `gisement-auditeur.md`.

**Tu orchestres, tu n'écris pas de mission.** Les rôles vont à des sous-agents au contexte frais
(T-4) : le lecteur lit, l'auteur écrit, l'auditeur relit. Toi, tu fixes l'échantillon, tu tiens le
registre, tu fais la carte et le plan, tu contrôles, tu livres, tu publies.

## Variables de session

```bash
SP=<scratchpad de la session>           # hors dépôt : snapshots, rendus, lignes brutes
CORPUS=<clone du dépôt de contenu>      # où l'on commite
ENGINE=<clone du moteur>                # où l'on lance les commandes (content/ y est un lien)
COUPLE=<classe>-<matière>                # ex. 9eme-base-math
REG=$CORPUS/content/programmes-officiels/sources-externes/web-$COUPLE   # le registre du couple
```

En session cloud : Node 24 (`.nvmrc` du moteur) et la chaîne de certificats du moteur
(`scripts/cloud/ca-chain/`) pour les sites à certificat incomplet — jamais `-k` ni
`NODE_TLS_REJECT_UNAUTHORIZED=0`.

## G0 — Qualifier

- **Archive officielle.** Le sujet d'un examen national se lit sur le portail du Ministère (fiche
  `web-echoexam-edunet-tn`, archive des sujets de 9ᵉ par session). Un site qui le ré-héberge ne
  sert que si le portail ne l'a pas, et on n'en prend que le sujet.
- **Sites de devoirs.** Une fiche `web-<site>/fiche.md` par site, en-tête de 8 champs (méthode,
  profil `source-web`) ; les fiches existantes servent d'un couple à l'autre, il suffit de vérifier
  que le site couvre la classe. `robots.txt` et CGU lus (R-13) ; un site qui interdit l'accès
  automatisé se lit à la main ou pas du tout.

## G1 — Fixer l'échantillon, AVANT d'ouvrir un document

Écris la liste dans la fiche du couple (`$REG/fiche.md`, § Échantillon : id, nature, session ou
créneau, page, fichier) et **merge-la** avant toute lecture. Règles (étude 36, D-4) :

- **examens** : toutes les sessions que l'archive publie pour la matière ; le lecteur marquera
  celles d'un programme ancien ;
- **devoirs** : par **vagues de neuf** (un par créneau DC1 … DS3), collège pilote et ordinaire en
  alternance, année scolaire du programme en vigueur, **au plus deux devoirs par auteur** dans
  l'échantillon (sans ce plafond, un seul enseignant remplit tout) ; une vague de plus tant que la
  précédente a apporté ≥ 30 % de signatures neuves, quatre vagues au plus ;
- **séries** : une par chapitre, après les devoirs, seulement si la dernière vague a encore trouvé
  du neuf.

Le contenu d'un document tranche sur son rayon : un devoir classé « collège pilote » dont
l'en-tête dit le contraire se note comme tel.

## G2 — Lire

- Télécharge dans `$SP/snapshots/<site>/` (`curl -g`, les crochets des noms de fichiers
  cassent sinon), calcule le SHA-256, reporte-le au registre.
- Un lecteur (sous-agent, `gisement-lecteur.md`) par lot de **≤ 6 documents**, lots en parallèle.
  Il rend : les lignes (`$SP/lines/<id>.tsv`), une méta par document, le snapshot texte (hors git)
  et, pour un **examen**, sa transcription fidèle au format de la page officielle
  (`$SP/officiel/<session>.md`), que tu recopies sous
  `content/programmes-officiels/examens-nationaux/<classe>/<matière>/<session>.md`.
- Concatène les lignes validées dans `$REG/lignes.tsv` (commande moteur
  `content:gisement:lignes` quand le lot 2 de l'étude 36 est mergé ; d'ici là, contrôle à la main :
  10 colonnes, aucun nombre de deux chiffres dans l'archétype ou le piège).

## G3 — Carte et écart

Par chapitre : fréquence en devoir et en examen, créneaux, archétypes, étages, combinaisons de
chapitres, vocabulaire des consignes. Croise avec les questions existantes (par compétence si la
famille a un registre, par archétype sinon). Écris la carte et l'écart dans la fiche du couple, puis
passe le contrôle local sur la fiche : aucune phrase d'une source n'entre dans git par elle.

## G4 — Planifier

`content:gisement:plan` (lot 2), ou à la main selon les mêmes règles :

- placement au chapitre **le plus avancé** de l'exercice, dans l'ordre du manifeste de la classe
  (`programmes-officiels/manifest/<classe>.json`) ; un exercice tout `HP:` n'est pas placé ;
- **devoirs** : une mission par signature distincte (chapitre + compétences + archétype) ;
  **examens** : une mission par exercice ;
- lots d'auteur de **5 à 8 missions**, par chapitre ; **un chapitre = un auteur à la fois** ;
  chaque lot reçoit sa plage de numéros de fichiers, à la suite de l'existant ;
- écris le plan dans `$REG/gisement.json` (missions à l'état `planifiee`) et, pour chaque lot, un
  fichier d'affectation dans `$SP/author/` : une ligne par mission, **anonyme** (« devoir A
  (devoir de contrôle 1, collège pilote), exercice 3 »), jamais l'identifiant d'un document.

## G5 — Écrire

Un sous-agent par lot, en parallèle sur des chapitres disjoints, avec la consigne qui correspond :

- devoir ou série → `gisement-auteur-devoir.md` (salle blanche) + son affectation ;
- examen → `gisement-auteur-examen.md` (reprise citée) + son affectation + la transcription de la
  session (le fichier versionné).

Donne à chaque auteur : le skill `prof-<matière>-<classe>` à charger, ses chapitres, sa plage de
numéros, les étiquettes d'erreur utiles déjà au registre, et la liste des chapitres où d'autres
écrivent (qu'il ne touche pas).

## G6 — Prouver

1. `npm run -s content:gates -- --tranche` depuis `$ENGINE` : vert pour les fichiers de la
   tranche (un rouge qui nomme un autre chapitre en écriture n'est pas le tien).
2. **Contrôle local** (devoirs et séries ; examens mesurés à titre indicatif) :
   `content:gisement:controle --sources $SP/snapshots <fichiers>` (lot 2), ou le script de session
   équivalent. Zéro plage ≥ 8 mots ; une question qui partage ≥ 3 nombres non triviaux avec un
   même exercice source se réécrit, même si c'est une coïncidence (la règle est mécanique).
3. **Audit à l'aveugle** de la tranche (sous-agent, `gisement-auditeur.md`) : chaque clé
   re-résolue avant d'être lue. Les défauts reviennent à l'auteur du lot (SendMessage), puis
   l'auditeur re-vérifie les correctifs.

## G7 — Livrer et publier (une tranche = ≤ 4 chapitres d'une matière)

```bash
cd $CORPUS && git fetch origin main
git worktree add $SP/wt -B <branche de la session> origin/main
# copier depuis l'arbre de travail les fichiers de la tranche, et eux seuls
cd $SP/wt && ln -sfn $PWD/content $ENGINE/content     # le moteur voit la tranche seule
(cd $ENGINE && npm run -s content:gates -- --tranche) # vert sur la tranche isolée
# CATALOGUE.md régénéré par les gates : le committer
git add … && git commit …                              # un commit par chapitre
git push -u origin <branche>                           # la PR s'ouvre, l'automerge la merge au vert
ln -sfn $CORPUS/content $ENGINE/content                # rebrancher l'arbre de travail
```

- On ne change **jamais** de branche dans l'arbre où des auteurs écrivent.
- Après le merge réel : `apply-content.yml` en `workflow_dispatch`, `subjects` = la matière,
  `dry_run` = `false` ; vérifier « Appliquer », « Vérifier en base », « Journaliser » ; puis
  l'issue `content-drift` close (relancer `content-drift.yml` si elle est encore ouverte).
- Registre : les missions de la tranche passent à `publiee`, avec le numéro de la PR.

## G8 — Mesurer et tenir

Par lot : jetons, outils, durée (lecteurs, auteurs, audit). Dans la fiche du couple (§ Mesures) :
documents lus, exercices, signatures, missions écrites et publiées, coût par mission publiée,
taux de reprise à l'audit, contrôle local. Une ligne au journal de l'étude 36 par couple terminé.

## STOP

- un document dont les droits sont douteux ⇒ il sort de l'échantillon ;
- une ligne de lecteur qui porte un nombre, un contexte ou une phrase de la source ⇒ elle se
  réécrit avant d'entrer dans git ;
- une clé fausse à l'audit ⇒ la tranche ne part pas ;
- une tranche mergée mais pas publiée ⇒ elle n'est pas finie.
