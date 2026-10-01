#!/bin/bash
# Rafraîchit la branche de sauvegarde wip/gisement-9eme-lots-en-ecriture (dépôt privé) avec l'état courant des lots en cours.
set -u
SP=/tmp/claude-0/-home-user/b03814da-e5f9-5a74-bf03-e7c23b20207a/scratchpad
SH=/home/user/yahia-quest-content
cd $SP/wt-sav2 || exit 1
EC=FableEtudes/36-gisement-examens-devoirs/en-cours
mkdir -p $EC/plan $EC/audits $EC/etiquettes $EC/outils
cp $SP/author/exam/assign-L*.md $SP/author/exam/prompt-L*.md $SP/author/exam/prompt-audit-L*.md $SP/author/prompt-G2.md $SP/author/prompt-I.md $EC/plan/ 2>/dev/null
cp $SP/gisement/9eme-math/plan-examens-v6.json $EC/plan/
cp $SP/author/exam/audit-L*.md $SP/author/exam/reverif-L*.md $EC/audits/ 2>/dev/null
cp $SP/pending-tags/*.json $EC/etiquettes/
cp $SP/spec-pub-*.json $SP/mk-pending.py $SP/lint/lot-lint.mjs $SP/fix-L08.py $SP/fix-L10.py $EC/outils/ 2>/dev/null
cp $SP/add-source-line.py $SP/apply-tags.py $SP/gen-spec-lot.py $SP/gen-exam-assign.py $SP/registre-add.py $SP/registre-docs.py $SP/registre-set.py $SP/deliver-lot.sh $SP/gates-summary.sh $SP/fixlib17.py $SP/widen-labels.py $SP/tags-pass2.py $SP/fix-L07.py $SP/spec-pub-L03L04.json $SP/pass2-notes.md $SP/refresh-savepoint.sh $EC/outils/ 2>/dev/null
cp $SH/.claude/skills/content-ingest/references/gisement-auteur-examen.md $SH/.claude/skills/content-ingest/references/gisement-auditeur.md .claude/skills/content-ingest/references/
# étage de lecture des autres matières de 9e (textes seuls : ni PDF ni rendus)
G=$SP/gisement
for pair in "9eme-sciences-vie-terre:svt" "9eme-svt:svt-liste" "9eme-arabic:arabe" "9eme-english:anglais" "9eme-french:francais"; do
  src=${pair%%:*}; dst=$EC/lecture-9eme/${pair##*:}
  mkdir -p $dst
  for f in docs.json machine-list.tsv reader-context.md chk.py mksnap.py mktsv.py zoom.py; do [ -f $G/$src/$f ] && cp $G/$src/$f $dst/; done
  for d in officiel lines lots; do [ -d $G/$src/$d ] && mkdir -p $dst/$d && cp $G/$src/$d/* $dst/$d/; done
done
# lots en cours (fichiers d'examen non livrés)
for spec in "08-thales 13 14 15 16 17 18 19 20" "09-triangle-rectangle-trigo 30 31 32 33 34 35 36 37 38 39 40 41" "12-repere-plan 16 17 18 19 20 21" "18-quadrilateres 22 23 24 25 26 27 28" "20-orthogonalite-espace 22 23 24 25 26 27"; do
  set -- $spec; ch=$1; shift
  for nn in "$@"; do
    for f in $SH/content/math/$ch/exercices/$nn-examen-*.json; do [ -f "$f" ] && cp "$f" content/math/$ch/exercices/; done
  done
done
git add -A
if git diff --cached --quiet; then echo "rien à sauvegarder"; exit 0; fi
git commit -q -m "wip(gisement): rafraîchissement du point de sauvegarde (L08, L10, L13, L15, audits, étiquettes)

Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_0121C1nDUtcSUvXYZ6KNzYNz" && git push -q origin wip/gisement-9eme-lots-en-ecriture 2>&1 | tail -2
git log --oneline -1 | cut -c1-120
