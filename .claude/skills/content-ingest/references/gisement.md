# Gisement — les règles propres aux examens et aux devoirs (étude 36)

> **Ce fichier n'est plus un déroulé.** Depuis le 2026-11-03, le gisement est fondu dans la procédure
> unique du skill [`campagne`](../../campagne/SKILL.md) : les sujets d'examen national se lisent à
> l'**étape 3** (avec la fiche), leurs missions s'écrivent à l'**étape 4** par l'auteur du chapitre,
> l'audit et la livraison sont ceux des **étapes 5-6**. Les devoirs en ligne ne se traitent **que sur
> demande de l'humain**. Spécification et historique : `FableEtudes/36-gisement-examens-devoirs/ETUDE.md`.
> Ne restent ici que les règles que la procédure applique.

## Deux régimes, jamais mélangés

- **Sujet d'examen national** (concours de 6ᵉ, de 9ᵉ, Bac) : corpus officiel (R-2). Lu sur l'archive
  du Ministère d'abord (fiche `web-echoexam-edunet-tn`), un site qui le ré-héberge seulement à défaut,
  et dans ce cas le sujet seul. Transcription fidèle sous
  `content/programmes-officiels/examens-nationaux/<classe>/<matière>/<session>.md`. **Une mission par
  exercice**, placée au chapitre **le plus avancé** qu'il mobilise (ordre du manifeste), reprise et
  citée. Un exercice entièrement hors programme (`HP:`) n'est pas placé.
- **Devoir ou série d'un site** (sur demande) : source web, tier T2′, **salle blanche**. Le lecteur rend
  une ligne anonyme par exercice ; l'auteur écrit une mission neuve **par signature distincte**
  (chapitre + compétences + archétype) sans voir la source.

## Échantillon des devoirs — fixé et mergé AVANT toute lecture

Vagues de **neuf** devoirs (un par créneau DC1 … DS3), collège pilote et ordinaire en alternance, année
scolaire du programme en vigueur, **au plus deux devoirs par auteur**. Une vague de plus seulement si la
précédente a apporté **≥ 30 % de signatures neuves**, quatre vagues au plus. Séries : une par chapitre,
après les devoirs, seulement si la dernière vague a encore trouvé du neuf. `robots.txt` et CGU lus ; un
site qui interdit l'accès automatisé se lit à la main ou pas du tout.

## Contrôle local (devoirs et séries)

Snapshots hors git (SHA-256 au registre). Sur les fichiers écrits : **zéro plage de ≥ 8 mots** commune
avec une source ; une question qui partage **≥ 3 nombres non triviaux** avec un même exercice source se
réécrit, coïncidence ou non (`content:gisement:controle --sources <snapshots> <fichiers>` quand il
existe, sinon le script de session équivalent). Une ligne de lecteur qui porte un nombre, un contexte ou
une phrase de la source se réécrit avant d'entrer dans git.

## Registre du couple

`content/programmes-officiels/sources-externes/web-<couple>/` : `fiche.md` (échantillon, carte),
`gisement.json` (missions `planifiee` → `mergee` → `publiee`, avec le numéro de PR), `lignes.tsv`
(10 colonnes, aucun nombre de deux chiffres dans l'archétype ou le piège). Les affectations d'auteur
sont anonymes (« devoir A, exercice 3 »), jamais l'identifiant d'un document.
