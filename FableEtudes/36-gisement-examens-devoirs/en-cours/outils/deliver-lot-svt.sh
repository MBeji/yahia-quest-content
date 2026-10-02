#!/bin/bash
# Prépare la livraison d'un lot d'examens de SVT 9ᵉ : worktree frais sur origin/main, copie des fichiers, ligne sources[],
# registre du gisement (mergee) et sept étages de gates. Un lot SVT couvre plusieurs chapitres.
# Usage : deliver-lot-svt.sh <lot> <dossier-chapitre>:<NN>[,<NN>…] [<dossier-chapitre>:<NN>[,<NN>…] …]
#   (les NN sont les préfixes à deux chiffres des fichiers « NN-examen-*.json » de l'arbre partagé)
set -u
LOT=$1; shift; SPECS="$@"
SP=/tmp/claude-0/-home-user/b03814da-e5f9-5a74-bf03-e7c23b20207a/scratchpad
SH=/home/user/yahia-quest-content
source $SP/engine-env.sh
cd $SH && git fetch -q origin main || exit 1
git worktree remove --force $SP/wt-$LOT >/dev/null 2>&1; git branch -D t-$LOT >/dev/null 2>&1
git worktree add -q $SP/wt-$LOT -b t-$LOT origin/main || exit 1
cd $SP/wt-$LOT || exit 1
for spec in $SPECS; do
  CH=${spec%%:*}; NNS=${spec#*:}; NNS=${NNS//,/ }
  for n in $NNS; do cp $SH/content/sciences-vie-terre/$CH/exercices/$n-examen-*.json content/sciences-vie-terre/$CH/exercices/ || exit 1; done
  python3 $SP/add-source-line-svt.py content/sciences-vie-terre/$CH/chapter.json
done
MATIERE=sciences-vie-terre python3 $SP/gen-spec-lot.py $LOT $SP/wt-$LOT > $SP/spec-$LOT-add.json || exit 1
G=content/programmes-officiels/sources-externes/web-9eme-base-sciences-vie-terre/gisement.json
python3 $SP/registre-add.py $G $SP/spec-$LOT-add.json || exit 1
cd /home/user/eng-gisement || exit 1
ln -sfn $SP/wt-$LOT/content content
npm run -s content:gates -- --tranche > $SP/gates-$LOT.txt 2>&1; echo "EXIT=$?" >> $SP/gates-$LOT.txt
cd /home/user
echo "FINI $LOT"
