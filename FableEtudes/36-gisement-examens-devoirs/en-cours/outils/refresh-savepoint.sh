#!/bin/bash
# Rafraîchit la branche de sauvegarde wip/gisement-9eme-lots-en-ecriture (dépôt privé) avec l'état courant des lots en cours.
set -u
SP=/tmp/claude-0/-home-user/b03814da-e5f9-5a74-bf03-e7c23b20207a/scratchpad
SH=/home/user/yahia-quest-content
cd $SP/wt-sav2 || exit 1
EC=FableEtudes/36-gisement-examens-devoirs/en-cours
mkdir -p $EC/plan $EC/audits $EC/etiquettes $EC/outils
cp $SP/author/exam/assign-L*.md $SP/author/exam/prompt-L*.md $SP/author/exam/prompt-audit-L*.md $SP/author/exam/prompt-audit-SVT-L*.md $SP/author/prompt-G2.md $SP/author/prompt-I.md $EC/plan/ 2>/dev/null
cp $SP/gisement/9eme-math/plan-examens-v6.json $EC/plan/
cp $SP/author/exam/audit-L*.md $SP/author/exam/reverif-L*.md $SP/author/exam/audit-SVT-L*.md $SP/author/exam/reverif-SVT-L*.md $EC/audits/ 2>/dev/null; mkdir -p $EC/plan/auditspec && cp $SP/auditspec/*.json $EC/plan/auditspec/ 2>/dev/null
cp $SP/pending-tags/*.json $EC/etiquettes/
cp $SP/spec-pub-*.json $SP/mk-pending.py $SP/lint/lot-lint.mjs $SP/fix-L08.py $SP/fix-L10.py $EC/outils/ 2>/dev/null
cp $SP/deliver-lot-svt.sh $SP/add-source-line-svt.py $SP/add-source-line.py $SP/apply-tags.py $SP/gen-spec-lot.py $SP/gen-exam-assign.py $SP/registre-add.py $SP/registre-docs.py $SP/registre-set.py $SP/deliver-lot.sh $SP/gates-summary.sh $SP/fixlib17.py $SP/widen-labels.py $SP/tags-pass2.py $SP/fix-L07.py $SP/spec-pub-L03L04.json $SP/pass2-notes.md $SP/refresh-savepoint.sh $EC/outils/ 2>/dev/null
cp $SH/.claude/skills/content-ingest/references/gisement-auteur-examen.md $SH/.claude/skills/content-ingest/references/gisement-auditeur.md .claude/skills/content-ingest/references/
# étage de lecture des autres matières de 9e (textes seuls : ni PDF ni rendus)
G=$SP/gisement
for pair in "9eme-sciences-vie-terre:svt" "9eme-svt:svt-liste" "9eme-arabic:arabe" "9eme-english:anglais" "9eme-french:francais"; do
  src=${pair%%:*}; dst=$EC/lecture-9eme/${pair##*:}
  mkdir -p $dst
  for f in docs.json machine-list.tsv reader-context.md chk.py mksnap.py mktsv.py zoom.py; do [ -f $G/$src/$f ] && cp $G/$src/$f $dst/; done
  for d in officiel lines lots; do [ -d $G/$src/$d ] && mkdir -p $dst/$d && cp $G/$src/$d/* $dst/$d/; done
done
cp $SP/etat-reprise.md $EC/ETAT-REPRISE.md 2>/dev/null
mkdir -p $EC/svt && cp $SP/gen-exam-assign-subj.py $SP/gen-prompt-svt.py $EC/outils/ 2>/dev/null; cp $SP/gisement/9eme-svt-plan/plan-examens-v1.json $SP/gisement/9eme-svt-plan/gisement.json $EC/svt/ 2>/dev/null; cp $SP/author/exam/prompt-svt-L*.md $SP/author/exam/assign-svt-L*.md $EC/plan/ 2>/dev/null
# lots en cours (fichiers d'examen non livrés) : « matière/chapitre NN NN … »
for spec in "math/09-triangle-rectangle-trigo 36 37 38 39 40 41" "math/18-quadrilateres 29 30 31 32 33 34 35" "math/03-calcul-litteral 27 28 29 30 31" "sciences-vie-terre/02-al-af3al-al-in3ikasiya 07 08" "sciences-vie-terre/05-al-hadm 07 08" "sciences-vie-terre/07-ad-dawaran 07 08"; do
  set -- $spec; path=$1; shift
  mkdir -p content/$path/exercices
  for nn in "$@"; do
    for f in $SH/content/$path/exercices/$nn-examen-*.json; do [ -f "$f" ] && cp "$f" content/$path/exercices/; done
  done
done
git add -A
if git diff --cached --quiet; then echo "rien à sauvegarder"; exit 0; fi
git commit -q -m "wip(gisement): rafraîchissement du point de sauvegarde (L08, L10, L13, L15, audits, étiquettes)

Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_0121C1nDUtcSUvXYZ6KNzYNz" && git push -q origin wip/gisement-9eme-lots-en-ecriture 2>&1 | tail -2
git log --oneline -1 | cut -c1-120
