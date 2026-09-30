#!/bin/bash
# Prépare la livraison d'un lot d'examens : worktree frais sur origin/main, copie des fichiers, ligne sources[],
# registre du gisement (mergee), contrôle anti-copie (devoirs) et sept étages de gates.
# Usage : deliver-lot.sh <lot> <dossier-chapitre> <NN> [<NN> ...]      (les NN sont les préfixes à deux chiffres)
set -u
LOT=$1; CH=$2; shift 2; NNS="$@"
SP=/tmp/claude-0/-home-user/b03814da-e5f9-5a74-bf03-e7c23b20207a/scratchpad
source $SP/engine-env.sh
cd /home/user/yahia-quest-content && git fetch -q origin main || exit 1
git worktree remove --force $SP/wt-$LOT >/dev/null 2>&1; git branch -D t-$LOT >/dev/null 2>&1
git worktree add -q $SP/wt-$LOT -b t-$LOT origin/main || exit 1
cd $SP/wt-$LOT || exit 1
for n in $NNS; do cp /home/user/yahia-quest-content/content/math/$CH/exercices/$n-examen-*.json content/math/$CH/exercices/ || exit 1; done
python3 $SP/add-source-line.py content/math/$CH/chapter.json
python3 $SP/gen-spec-lot.py $LOT $SP/wt-$LOT > $SP/spec-$LOT-add.json || exit 1
G=content/programmes-officiels/sources-externes/web-9eme-base-math/gisement.json
python3 $SP/registre-add.py $G $SP/spec-$LOT-add.json || exit 1
cd /home/user/eng-gisement || exit 1
F=$(for n in $NNS; do ls $SP/wt-$LOT/content/math/$CH/exercices/$n-examen-*.json; done)
echo "== devoirs (pilot)" > $SP/gates-$LOT.txt
npm run -s content:gisement:controle -- --sources $SP/pilot/snapshots $F 2>&1 | grep -E '✓|✗|texte' | tail -3 >> $SP/gates-$LOT.txt
ln -sfn $SP/wt-$LOT/content content
npm run -s content:gates -- --tranche >> $SP/gates-$LOT.txt 2>&1; echo "EXIT=$?" >> $SP/gates-$LOT.txt
cd /home/user
echo "FINI $LOT"
