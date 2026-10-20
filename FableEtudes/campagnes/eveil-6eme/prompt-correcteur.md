Tu es le **CORRECTEUR** d'un lot du passage **éveil scientifique 6ᵉ** (`eveil-scientifique-6eme`, `ar`, élèves de 11–12 ans). Un auditeur indépendant (opus) a audité le lot ; tu appliques **tous** ses défauts (critiques, majeurs, mineurs) dans les chapitres du lot, sous `/home/user/wt-ev6/content/eveil-scientifique-6eme/`.

**Charge d'abord les skills** `content-ecole-tn`, `content-engine` (références `course-quality.md`, `course-explanation.md`, `style-guide.md`, `course-figures.md`, partie schéma), `content-cours`, `content-interactif`, `prof-eveil-primaire`.

**Lis** le rapport d'audit `/home/user/wt-ev6/FableEtudes/campagnes/eveil-6eme/audits/audit-<lot>.md` EN ENTIER, la consigne d'auteur `prompt-auteur-chapitre.md` (exigences, contrôles) et les arbitrages de `PLAN.md` § 3 (V1–V5, E-7a, E-7b).

**Règles** :
1. Applique le texte de remplacement de l'auditeur quand il en donne un ; sinon écris le tien en respectant les exigences. Avant d'écrire, **re-vérifie** chaque remplacement : une seule réponse défendable, clé juste, science juste, la clé n'est pas strictement la plus longue, pas de paire proche, aucune désignation d'option par sa place, l'explication d'une `short_answer` ne contient pas la réponse, aucune question qui redonne un exemple / `verifie` / ancrage du cours (vérifie-le en relisant le cours après tes changements).
2. Étiquettes : seulement des ids qui existent dans `content/misconceptions.json` ; une option sans id exact reste muette et l'id est **proposé** dans ton rapport (ne touche pas au registre).
3. Ne change ni slug, ni `displayOrder`, ni id/nom de fichier d'exercice ; un exercice ≤ 12 questions.
4. Si un défaut te paraît faux après vérification (PDF à l'image : `/tmp/claude-0/ev6/src/103604P00.pdf`, `503604P00.pdf`, offset 0, `pdftoppm -r 150`), ne l'applique pas et explique pourquoi dans ton rapport.
5. Une décision de programme renvoyée « à l'humain » par l'auditeur n'est pas à appliquer : liste-la.

**Contrôles** (depuis `/home/user/eng-deliver` après `source /tmp/claude-0/-home-user/b03814da-e5f9-5a74-bf03-e7c23b20207a/scratchpad/engine-env.sh` ; lien `content` → `/home/user/wt-ev6/content`, ne le change pas) : `content:check`, `content:qa -- --subject eveil-scientifique-6eme`, `content:figures:check`, `content:tranche -- --subject eveil-scientifique-6eme --chapters <slugs du lot> --fresh --strict-longest --strict-lessons`, `npx prettier --write` puis `--check` sur tes fichiers via `/home/user/eng-deliver/content/…`. D'autres correcteurs travaillent en parallèle : ne touche qu'aux chapitres de ton lot. Scratchpad : un sous-dossier `corr-<lot>` à toi.

Rapport `/home/user/wt-ev6/FableEtudes/campagnes/eveil-6eme/rapports/correction-<lot>.md` : défaut par défaut (appliqué / adapté / refusé et pourquoi), ids proposés, état des gates. Réponse courte. Pas de git.
