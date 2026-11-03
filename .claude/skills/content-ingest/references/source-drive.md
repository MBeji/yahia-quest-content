# Source des manuels et lecture à moindre coût (procédure du 2026-11-03)

> **Ce fichier est LA procédure d'accès aux sources officielles et de leur lecture.** Il remplace,
> pour tout LOT A et tout gisement, la méthode § A2 « Obtenir les sources » et § A3.1-2 (ScribeKit +
> vision), le préalable ScribeKit du skill `campagne` § 0, et la note « TLS en session » du
> `CLAUDE.md`. Décision de Mohamed du 2026-11-03 : *la source, c'est désormais le dossier Drive ;
> l'OCR doit être plus simple et moins coûteuse.*

## 1. La source : le dossier Drive `cnp-officiel`

- **Où :** <https://drive.google.com/drive/folders/1ZUUgEx71bKFsXulk_WL7cSfNxc6U9tmX>, dossier du
  compte Google du projet. Il porte **tout le corpus CNP** (375 PDF : cycle de base 1ʳᵉ–9ᵉ et
  secondaire 1ʳᵉ–Bac, élève et enseignant).
- **Accès :** le connecteur **Google Drive** de la session doit être connecté **au compte
  propriétaire du dossier**. Un autre compte voit « Requested entity was not found » (constaté le
  2026-11-03, résolu en changeant le compte du connecteur).
- **Le site du CNP n'est plus la source.** Depuis une session cloud, son téléchargement échoue
  (`content:manuel:fetch` → `curl 35 : Connection reset by peer`, mesuré le 2026-11-03).
  `content:manuel:fetch` reste utilisable sur un poste local, c'est tout.

Ce que contient la racine :

| Élément | Usage |
| --- | --- |
| `index.csv` | **l'inventaire** : `cycle,classe,type,code,file,bytes,status` (cycle 1 = base, 2 = secondaire ; classe 4 du cycle 2 = **Bac**). Le lire **d'abord** : il dit si un manuel existe sans fouiller les dossiers. Les codes sont ceux de `suivi/corpus-cnp.json`. |
| `manuels/` | les PDF, rangés `asasi/c<classe>/{eleve,enseignant}/` et `secondaire/…`, nommés `<code><tome>.pdf` (ex. `228462P01.pdf`). |
| `_txt/` | **couches texte déjà extraites** (`<code><tome>-<slug>.txt`) : quand le fichier existe, c'est la lecture la moins chère. |
| `_render/`, `_render_lo/` | **pages déjà rendues en PNG** (`<code><tome>-NNN.png`, NNN = page du PDF) : la vision lit ces images, inutile de rendre. |
| `_transcriptions-wip/` | transcriptions brutes en cours, même contrat que `programmes-officiels/_tranches-wip/`. |

Trouver un fichier : `search_files` avec `title = '<code><tome>.pdf'` (ou `title contains
'<code>'`) — jamais une navigation dossier par dossier. Un fichier fraîchement versé peut mettre
quelques minutes à apparaître dans la recherche (constaté le 2026-11-03) : chercher à nouveau avant
de conclure qu'il manque.

## 2. Lire au moindre coût : l'échelle L0 → L3

On prend **le premier barreau qui suffit**, page par page. La vision n'est plus le cas général :
c'est le dernier barreau.

| Barreau | Quand | Comment | Coût |
| --- | --- | --- | --- |
| **L0 — texte déjà extrait** | `_txt/<code><tome>-*.txt` existe | `read_file_content` sur le `.txt` | quasi nul |
| **L1 — couche texte du PDF** | manuel en **français / anglais** (tout le secondaire scientifique, le Bac) | `read_file_content` sur le PDF | faible |
| **L2 — couche texte décodée** | manuel **arabe** à polices propriétaires (texte brouillé `jÉØµdG øe…`) | `read_file_content`, puis la **table glyphe → lettre** de la fiche du couple (recette : `programme/6eme-base/arabe.md` § 7, `programme/1ere-base/arabe.md` § 7-2) | faible |
| **L3 — vision** | ce que L0-L2 ne rendent pas : formules, vecteurs, fractions, tableaux, figures, encadrés à mise en page, pages scannées sans texte ; **et** le sondage de contrôle (§ 3) | `_render/<code><tome>-NNN.png` (lu avec Read) ; à défaut `render.sh` | élevé |

Mesures qui fondent l'échelle (2026-11-03) :

- **L1** sur `222422P00` (maths Bac lettres, 2,5 Mo) : 79 475 caractères pour le manuel entier,
  prose et consignes **propres** ; perdus ou dégradés : formules, vecteurs, fractions, figures,
  quelques signes (`f'(-3)-5` pour `f'(-3)=5`). ⇒ on lit le texte, on ne passe en vision **que** les
  pages de formules et de figures.
- **L2** sur `501603P00` (guide arabe 6ᵉ) : 107 612 caractères de glyphes brouillés, mais la table de
  la fiche 6ᵉ décode 899 pages avec 0 glyphe inconnu (validée sur quatre vérités-terrain le
  2026-09-22). Limite : **les harakat n'y sont pas fiables** — un encadré vocalisé se lit en L3.

Mode d'emploi de `read_file_content` :

- au-delà d'environ 80 000 caractères, le résultat **n'arrive pas dans la conversation** : il est
  écrit dans un fichier local (JSON `{fileContent, title, viewUrl}`) dont le chemin est donné. Le
  traiter avec `python3 -I` ou `jq`, **dans un sous-agent** quand il faut tout lire (le contexte de
  l'orchestrateur ne doit pas l'absorber) ;
- le texte **n'a pas de marqueur de page fiable** (les numéros imprimés y sont noyés) : pour déclarer
  des plages, ancrer chaque passage sur le numéro de page imprimé, et le vérifier sur le PNG de
  `_render/` correspondant ;
- **ne jamais télécharger** un PDF par `download_file_content` : il revient en base64 dans la
  conversation, inexploitable au-delà de quelques centaines de Ko.

ScribeKit devient **facultatif** : il garde son intérêt pour échafauder une fiche neuve
(`scribekit app-cnp`), il n'est plus un préalable à la lecture.

## 3. Ce qui compte comme « lu » au registre

Une page lue par L0, L1 ou L2 **compte comme lue** (`pagesLues` de `suivi/<grade>.json`) dès qu'un
**sondage image** l'a validée :

- **au moins une page sur dix** de la plage, choisies parmi les plus denses (tableaux, encadrés,
  exercices), confrontées au PNG ;
- **0 écart substantiel** (mot ou nombre faux, ligne sautée, ordre inversé). Un écart ⇒ on élargit
  le sondage à toute la section ; trois écarts ⇒ la section passe en L3 ;
- le sondage se note dans la fiche (pages sondées, écarts trouvés), comme un R-7 dirigé.

Ceci **remplace** la règle de prudence du 2026-09-22 (« une couverture atteinte par décodage n'est
pas une lecture »), qui maintenait des fiches à 100 % de couverture en `partielle` (5ᵉ et 6ᵉ arabe).
Une telle fiche passe à `complete` quand le sondage de ses plages décodées est fait et noté.

Ce qui ne change pas : fidélité absolue (rien d'inventé, `[?]` pour l'illisible, `[sic]` pour la
coquille), chiffres 0-9, lecture intégrale (R-6), R-7 avant promotion, et **jamais un PDF ni une
image de page dans git** (les manuels sont l'œuvre du CNP : on cite, on ne copie pas).
