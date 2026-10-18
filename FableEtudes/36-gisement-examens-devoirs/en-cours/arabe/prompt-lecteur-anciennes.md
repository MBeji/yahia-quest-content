Tu es un **LECTEUR** du gisement (étude 36) pour le couple 9ᵉ × arabe (matière `arabic`), étape G2 « Lire », **sessions anciennes** (2001–2019) — ta liste est donnée à la fin. Les sessions 2020–2026 (C01–C12) sont déjà lues et publiées.

- **Consignes à suivre à la lettre** : `/home/user/yahia-quest-content/.claude/skills/content-ingest/references/gisement-lecteur.md` (EN ENTIER) et la section G2 de `…/references/gisement.md`.
- **Contexte du couple** : `/home/user/wt-gis/FableEtudes/36-gisement-examens-devoirs/en-cours/lecture-9eme/arabe/reader-context.md` (17 chapitres du manifeste + 2 dossiers hors manifeste `01-i3rab-wal-bina` et `06-al-mushtaqqat` ; `HP:<mot-clé>` pour une notion hors liste ; jamais `11-annales-subur` ; compétences toujours `-`).
- **Méta** : `…/lecture-9eme/arabe/docs.json` (URL `fichier`, sha256, pages) ; registre `/home/user/wt-ar2/content/programmes-officiels/sources-externes/web-9eme-base-arabic/gisement.json`.
- **Modèles** : journal `…/lecture-9eme/arabe/JOURNAL-lecture.md` (lots C01–C12 : formats, rattachements, HP), transcriptions `/home/user/wt-ar2/content/programmes-officiels/examens-nationaux/9eme-base/arabic/2023-generale.md` et `2020-generale.md`.

**Conventions FIXÉES (elles priment sur le journal C01–C12, dont le n°exo `partie.question` est refusé par le validateur)** :
- **n°exo = rang d'ordre dans l'épreuve** (`\d+`, sans point ni suffixe de sous-question) : 1, 2, 3… dans l'ordre imprimé, compréhension puis langue puis production.
- **Grain** : une ligne par question notée (comme C01–C12) ; production écrite = UNE ligne, la dernière ; une épreuve « الإنشاء العربي » sans compréhension ni langue = une seule ligne (n°exo 1, chapitre `09-al-intaj-al-kitabi`).
- **Barème** : points imprimés de la question ; quand seul le total d'un bloc est imprimé, `-` sur les questions du bloc.
- Rattachements : comme C01–C12 (les acquis de 7ᵉ-8ᵉ — مفعول مطلق/لأجله، الجمع، الإسناد، البناء للمجهول، حروف الجرّ… — en `HP:<mot-clé>` ; المشتقّات → `06-al-mushtaqqat`, المثنّى/الإعراب → `01-i3rab-wal-bina`) ; une notion d'un ANCIEN programme absente du manuel révisé : `HP:` et noter au journal « programme ancien ».
- Étage : compréhension et langue d'application `d1` ; transformation ou deux notions `d2`/`d3` ; production `d3`.

**Texte support (filtre de contenu, règle du 2026-10-16)** : le texte support **ne se transcrit pas en entier** — référence (auteur, œuvre, année si imprimés), nombre de lignes, résumé neutre de 3 à 5 phrases écrit par toi, au plus deux citations courtes (une phrase) utiles à une question, mention « النصّ كاملاً : الوثيقة الرسمية، sha256 في السجلّ ». Consignes, questions, items et barèmes restent mot pour mot, vocalisation telle qu'imprimée, soulignés `<u>…</u>`.

Pour chaque document : téléchargement (`curl -g`, http ; si https, `CURL_CA_BUNDLE=/root/.cache/yqa-ca/ca-bundle.pem` ; jamais `-k`) dans `/tmp/claude-0/arlec2/src/`, sha256 comparé à `docs.json` ; lecture en vision (150 DPI, 220 pour les textes vocalisés) ; transcription FIDÈLE `/home/user/wt-ar2/content/programmes-officiels/examens-nationaux/9eme-base/arabic/<session>-<filiere>.md` ; lignes `…/lecture-9eme/arabe/lines/<id>.tsv` + `.meta` ; snapshot `/tmp/claude-0/arlec2/snapshots/<id>.txt` ; journal AU FIL DE L'EAU `…/lecture-9eme/arabe/JOURNAL-lecture-<ton lot>.md`. Un document introuvable (404) ou illisible ne s'invente pas : cherche-le sur la page du portail (`page`), puis propose le statut.

Validation : depuis `/home/user/eng-svtses` (après `source /tmp/claude-0/-home-user/b03814da-e5f9-5a74-bf03-e7c23b20207a/scratchpad/engine-env.sh`) `npm run -s content:gisement:lignes -- --subject arabic --grade 9eme-base --content /home/user/wt-ar2/content <tes .tsv>` : 0 fautive.

D'autres lecteurs lisent d'autres sessions en même temps : n'écris que tes fichiers. Tu ne modifies NI `gisement.json` NI `lignes.tsv`, ni rien sous `content/arabic/`. Aucune écriture git. Rapport final court en français : documents lus et sha (= registre ?), transcriptions, nombre de lignes, format de chaque épreuve (général / technique / unique ; « الإنشاء العربي » seul ?), notions par chapitre, part HP et « programme ancien », difficultés.
