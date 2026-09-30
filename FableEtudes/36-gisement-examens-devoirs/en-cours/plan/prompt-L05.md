Tu es un **auteur** du pipeline « gisement » (étude 36), maths 9ᵉ, chapitre 04 (équations, inéquations, factorisation). Tu transformes des exercices de **sujets officiels de l'examen national de 9ᵉ** en missions du portail. C'est une **reprise fidèle et citée** : ces sujets sont du corpus officiel.

1. **Consigne à suivre à la lettre** : `/home/user/yahia-quest-content/.claude/skills/content-ingest/references/gisement-auteur-examen.md`. Elle te fait charger d'abord `prof-math-9eme`, puis `content-ecole-tn`.
2. **Ta liste** : 6 missions, une par ligne, dans `/tmp/claude-0/-home-user/b03814da-e5f9-5a74-bf03-e7c23b20207a/scratchpad/author/exam/assign-L05.md`.
   - Chaque ligne nomme la transcription officielle de la session (sous `content/programmes-officiels/examens-nationaux/9eme-base/math/`), le numéro de l'exercice, le fichier et son `displayOrder`.
   - Lis **seulement** les exercices qui te sont confiés.
   - L'archétype et le piège viennent du lecteur : ce sont des indications, la transcription fait foi.
   - N'ouvre rien d'autre sous `/tmp/claude-0/`, ni sous `content/programmes-officiels/sources-externes/`.
3. **Fichiers, numéros et `displayOrder`** : ceux de la liste, sans rien renommer d'existant.
   - Lis les missions existantes du chapitre pour la forme et pour **ne pas répéter leurs formulations** ; lis aussi, dans l'arbre de travail, les fichiers `17` à `22` du dossier (missions d'examen d'un lot voisin, en fin d'audit : mêmes chapitres d'annales, gabarits proches à ne pas reproduire : produit nul, développer, factoriser, inéquation sur droite graduée) et NE LES MODIFIE PAS. L'arbre de travail garde parfois des versions périmées de fichiers déjà publiés : lis les publiés sur `main` (`git -C /home/user/yahia-quest-content ls-tree --name-only origin/main content/math/04-equations-inequations/exercices/`, puis `git -C /home/user/yahia-quest-content show origin/main:<chemin>`).
   - Chaque exercice officiel donne sa propre mission, même s'il ressemble à un autre : ce sont des annales. Tes fichiers sont les numéros 23 à 28 : n'écris rien d'autre dans ce dossier.
   - Les énoncés portent les **données de leur session**, pour que le contrôle « paires proches » des gates reste à 0 dans ta tranche.
4. **Titre** : « 🏛️ مناظرة <année> · التمرين <N> » suivi des étoiles et du sujet. Pour la filière technique, écris « 🏛️ مناظرة <année> (تقني) · التمرين <N> ». L'en-tête suit l'étage (d2 practice 75/15 ; d3 boss 120/30 ; d4 challenge 300/60). Un exercice d'examen n'est jamais d1 : une ligne notée d1 devient d2.
5. **Programme en vigueur (R-3)**
   - Ordre du manifeste : 15 → 01 → 19 → 02 → 16 → 17 → 03 → 04 → 07 → 12 → 08 → 09 → 18 → 20. Une question ne s'appuie que sur son chapitre et les précédents.
   - Pas de vecteurs ni de translation en 9ᵉ. Un item d'un ancien programme (vecteur, translation, système…) **ne devient pas une question** : si la suite en dépend, donne son résultat dans l'énoncé (« on admet que… ») et dis-le dans ton rapport.
   - Une technique qu'aucun cours n'enseigne se donne dans l'énoncé.
6. **`chapter.json`** : si la ligne n'y est pas encore, ajoute à `sources[]` exactement : « Sujets officiels de l'examen national de fin d'études de l'enseignement de base (9ᵉ), Ministère de l'Éducation (corpus officiel, reprise citée, étude 36) — transcriptions : programmes-officiels/examens-nationaux/9eme-base/math/ ». Rien d'autre dans ce fichier.
7. **Écris chaque fichier dès qu'il est prêt**, puis passe au suivant.

D'autres auteurs écrivent en même temps dans d'autres chapitres : n'y touche pas. Un rouge des gates qui ne nomme pas tes fichiers n'est pas le tien.

**Validation**
- Double résolution de chaque question contre les données officielles (deux chemins ; un script numérique est bienvenu).
- Chaque distracteur est faux **en valeur** et exécute l'erreur de son étiquette.
- Puis : `source /tmp/claude-0/-home-user/b03814da-e5f9-5a74-bf03-e7c23b20207a/scratchpad/engine-env.sh && cd /home/user/yahia-quest-arena && npm run -s content:gates -- --tranche`.

Rapport final comme la consigne le demande. Pas de commit.
