Tu es un **auteur** du pipeline « gisement » (étude 36), **arabe 9ᵉ** (matière `arabic`, items en arabe). Tu écris une mission **neuve** à partir de **cartes** tirées de devoirs en ligne, en salle blanche (tier T2′) : tu n'as jamais vu ces devoirs et tu ne dois pas les voir.

Lis d'abord en entier `/home/user/wt-gis/FableEtudes/36-gisement-examens-devoirs/en-cours/francais/prompt-francais-devoirs.md` : il s'applique tel quel, avec ces substitutions qui priment :
- skill `prof-arabe-9eme` (puis `content-ecole-tn`) ; liste `/home/user/wt-gis/FableEtudes/36-gisement-examens-devoirs/en-cours/arabe/assign-arabe-devoirs.md` ;
- arbre de travail `/home/user/wt-ar2/content/arabic/` (branche `wip/gisement-arabe-9eme-anciennes`) ; publiés sur `origin/main` du dépôt `/home/user/yahia-quest-content` ;
- étiquettes : famille `arabe.*` de `content/misconceptions.json` (sur `origin/main`) ;
- ne lis rien sous `…/lecture-9eme/`, `/tmp/claude-0/devoirs-snapshots/`, ni `content/programmes-officiels/sources-externes/` ;
- gates : `source /tmp/claude-0/-home-user/b03814da-e5f9-5a74-bf03-e7c23b20207a/scratchpad/engine-env.sh && cd /home/user/eng-ar` (lien `content` → `/home/user/wt-ar2/content`) puis `npm run -s content:check && npm run -s content:qa -- --subject arabic && npm run -s content:tranche -- --subject arabic --chapters <ton chapitre>` et `npm run -s content:gisement:controle -- --sources /tmp/claude-0/devoirs-snapshots/arabic <ton fichier>` (l'outil seul lit les snapshots) ;
- notes `…/en-cours/auteurs-notes/ar-devoirs-v2/NOTES.md` ; dossier de travail `/tmp/claude-0/ar-gis/devoirs-v2/`.

**N'écris AUCUN `chapter.json`** (le pilote ajoute la ligne `sources[]` à la livraison). N'écris que ton fichier `NN-devoir-*.json`. Rendu arabe : écris naturellement, le moteur gère la ponctuation de bord.
