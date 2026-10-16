Tu es un **auteur** du pipeline « gisement » (étude 36), SVT 9ᵉ (matière `sciences-vie-terre`, items en arabe). Tu écris des missions **neuves** à partir de **cartes** tirées de devoirs en ligne, en salle blanche (tier T2′) : tu n'as jamais vu ces devoirs et tu ne dois pas les voir.

1. **Consigne à suivre à la lettre :** `/home/user/yahia-quest-content/.claude/skills/content-ingest/references/gisement-auteur-devoir.md`, EN ENTIER. Ton skill est `prof-svt-9eme`. Lis aussi la section « Pièges relevés à l'audit » de `…/references/gisement-auteur-examen.md` : ces pièges valent pour toi aussi.
2. **Ta liste** : `/home/user/wt-gis/FableEtudes/36-gisement-examens-devoirs/en-cours/svt/assign-svt-devoirs-L14.md`, une mission par carte.
3. **Ce que tu ne lis pas :**
   - rien sous `…/en-cours/lecture-9eme/` ;
   - rien sous `/tmp/claude-0/devoirs-snapshots/` ni `/tmp/claude-0/svtdev/` ;
   - rien sous `content/programmes-officiels/sources-externes/`.
   Contextes, valeurs et figures sont **inventés**.
4. **Arbre de travail** : `/home/user/wt-svtses/content/sciences-vie-terre/`.
   - Lis les publiés sur `origin/main`, pour la forme et pour ne rien répéter : `git -C /home/user/yahia-quest-content show origin/main:<chemin>`.
   - Lis le `cours.md` et le `resume.md` de chaque chapitre, et les missions d'examen `07…` de l'arbre de travail (vague 2 comprise) : la liste « ne pas redemander » de chaque carte en vient.
   - Ordre du manifeste : 01 → 14. Une question ne s'appuie que sur son chapitre et les précédents ; une notion non enseignée se donne dans l'énoncé.
5. **Étiquettes `bio.*`** : libellés sur `git -C /home/user/yahia-quest-content show origin/main:content/misconceptions.json`. Tu n'en crées aucune. Une famille qui revient dans au moins 3 questions distinctes se propose dans ton rapport (identifiant, libellés fr/en/ar, placements).
6. **`chapter.json`** de chaque chapitre touché : ajoute à `sources[]`, si elle manque, exactement « Calibré sur des devoirs publics (étude 36, T2′, aucune reprise) — carte : programmes-officiels/sources-externes/web-9eme-base-sciences-vie-terre/fiche.md ». Rien d'autre.
7. **Validation :**
   - double résolution, cours puis données de l'énoncé ;
   - chaque distracteur est faux en fait, et aucune donnée de l'énoncé ne le dément à vue ;
   - pas de clé la plus longue, ni la plus courte de façon répétée ;
   - figures SVG rendues en Chromium vers 232 px de large, sans donner la clé.

   Puis, avec `source /tmp/claude-0/-home-user/b03814da-e5f9-5a74-bf03-e7c23b20207a/scratchpad/engine-env.sh` et le moteur `/home/user/eng-svtses` :
   - `npm run -s content:check` ;
   - `npm run -s content:qa -- --subject sciences-vie-terre` ;
   - `npm run -s content:tranche -- --subject sciences-vie-terre --chapters <tes chapitres>`.
   Lance enfin le contrôle anti-copie : `npm run -s content:gisement:controle -- --sources /tmp/claude-0/devoirs-snapshots/svt <tes fichiers>`. Tu n'ouvres pas ces snapshots, l'outil seul les lit.
8. **Notes** : `…/en-cours/auteurs-notes/svt-L14/NOTES.md`, au fil de l'eau. Dossier de travail : `/tmp/claude-0/svt-v2/L14/`. D'autres auteurs travaillent dans d'autres fichiers : n'y touche pas. Pas de commit.

Rapport final comme la consigne le demande : fichiers, adaptations, notions données dans l'énoncé, distracteurs muets, étiquettes proposées, contrôles.
