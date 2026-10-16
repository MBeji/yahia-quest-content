Tu es le **PLANIFICATEUR** du gisement (étude 36) pour le couple 9ᵉ × anglais (matière `english`), étapes G3–G4 : carte et écart, puis plan des missions d'examen et du lot de devoirs. Tu n'écris AUCUN exercice.

**Entrées**
- Consignes : `/home/user/yahia-quest-content/.claude/skills/content-ingest/references/gisement.md` (sections G3, G4, missions fusionnées, « ne pas redemander », plafond par mission) et `references/gisement-lecteur.md`.
- Les 41 sujets lus (C01–C42 sans C39, 2004 introuvable ; 2014 absente de l'archive) : transcriptions `/home/user/wt-en/content/programmes-officiels/examens-nationaux/9eme-base/english/*.md` (texte support RÉSUMÉ : le texte intégral est dans le PDF officiel, URL et sha256 au registre).
- Les lignes et journaux : `/home/user/wt-gis/FableEtudes/36-gisement-examens-devoirs/en-cours/lecture-9eme/anglais/` (`lines/C*.tsv`, `lines/D*.tsv`, `JOURNAL-lecture-*.md` — lis leurs § 0, § 4, § 5 : doutes de classement).
- Le contenu publié `/home/user/wt-en/content/english/` (10 chapitres au patron : `cours.md`, `quiz.json`, `exercices/*.json`) et le manifeste du niveau.
- Registre : `/home/user/wt-en/content/programmes-officiels/sources-externes/web-9eme-base-english/gisement.json` ; fiche `…/fiche.md`.
- **Modèle à suivre** : le plan français `/home/user/wt-gis/FableEtudes/36-gisement-examens-devoirs/en-cours/francais/PLAN.md`, `plan-examens-v1.json`, `assign-francais-L01.md` et `assign-francais-devoirs.md` (même forme de sorties, mêmes règles R1–R6 transposées).

**Règles à transposer** (PLAN français § 1) :
- R1 langue : une mission par famille et par chapitre, sessions fusionnées, chaque question dit sa session et redonne la phrase officielle ; placement au chapitre le plus avancé de la ligne, exceptions déclarées. Titre « 🏛️ Exams <années> · <subject> » + étoiles de l'étage (l'interface de la matière est en anglais : regarde comment les titres des exercices existants sont écrits et suis-les).
- R2 reading : une mission par texte, **au plus cinq textes** récents et représentatifs (générale et technique) ; la mission cite une à deux phrases par question prises dans le PDF officiel, jamais le texte entier ; questions ouvertes converties en fermées.
- R3 writing : converti en préparation fermée (tâche exacte, idées pertinentes `multi`, plan `ordering`, modal ou temps attendu, formule d'une lettre…), regroupé par archétypes (conseil/règles avec modaux ; récit au passé ; description/avis ; lettre/courriel) — une mission par archétype.
- R4 : rien de ce que le patron, les quiz ou une autre mission posent déjà ; croisement question par question ; la note de chaque mission liste « ne pas redemander ».
- R5 placement des writings convertis : au chapitre de l'opération préparée (04 pour conseiller, 02 pour le récit au passé, 09 sinon), déclaré.
- R6 consignes ambiguës : reformulées pour une seule réponse et déclarées, ou écartées.
- Plafond : 12 questions par mission au plus ; étages d1–d3 (`difficulty` ≤ 3).

**Décisions du pilote déjà prises** :
- Barèmes en demi-points gardés (2.5).
- Pronoms objets et réfléchis : jetons `HP:object-pronoun` / `HP:reflexive-pronoun` (le lot C07–C18 les a rangés en 09 seul : harmonise dans ton analyse, sans réécrire les lignes).
- `HP:gerund` couvre aussi l'infinitif ou le participe exigé après un verbe/une préposition (verb patterns).
- Les cadres « If I were… » d'un reading ne comptent pas comme conditionnel ; le 2ᵉ conditionnel n'est pas au programme.
- Les blocs d'écoute des contrôles (D01, D03, D05) ne donnent rien (pas d'audio dans l'application, pas d'écoute à l'examen).
- Notions HP récurrentes (`word-formation`, `gerund`, pronoms) : **ne pas créer de mission HP**. Si une famille HP revient dans au moins 6 sessions, propose au pilote (§ dédié du PLAN) soit une ligne de cours au chapitre le plus proche (texte exact, avec la page du guide/manuel CNP si tu la trouves dans `content/programmes-officiels/` ou les cours), soit l'écart. Le pilote tranche avant l'écriture.

**Lot devoirs** (salle blanche, cartes seulement, plafond de deux devoirs par auteur déjà vérifié : Fraoua D04+D05) : cartes D0x#n à partir des lignes `D*.tsv` (jamais leur texte), fusionnées en missions de devoirs `NN-devoir-<slug>.json`, chacune avec sa liste « ne pas redemander » (patron + missions d'examen planifiées). Règle des 30 % de signatures neuves à mesurer pour décider d'une vague 2 (l'énoncer, le pilote décide).

**Sorties** (comme le français) :
- `…/web-9eme-base-english/fiche.md` § 3 « Carte et écart » (sujets officiels seulement) ;
- `/home/user/wt-gis/FableEtudes/36-gisement-examens-devoirs/en-cours/anglais/PLAN.md` et `plan-examens-v1.json` ;
- registre `gisement.json` : missions `planifiee` (id = source de base, `sources` = toutes les sources fusionnées, `chapitre`, `fichier` proposé, `etage`, `etapes`, `lot`, `nn`, `note`) ; tu ne touches pas à la section `documents` ;
- affectations `assign-anglais-L01.md` … `assign-anglais-LNN.md` (lots de 4 à 6 missions, une mission = un fichier, carte complète : sources, phrases officielles à reprendre, piège, « ne pas redemander », étage, nombre de questions) et `assign-anglais-devoirs.md`.

**Contrôle** : `content:gisement:controle` depuis `/home/user/eng-svtses` (après `source /tmp/claude-0/-home-user/b03814da-e5f9-5a74-bf03-e7c23b20207a/scratchpad/engine-env.sh`, avec `--content /home/user/wt-en/content` si la commande l'accepte) contre les transcriptions et les snapshots de devoirs `/tmp/claude-0/devoirs-snapshots/english/` : 0 plage de 8 mots contre les devoirs dans tes sorties. `content:check` doit rester vert (le registre est lu par les gates).

Écris au fil de l'eau. Aucune écriture git, rien sous `content/english/`. Rapport final court en français : nombre de missions par lot et par chapitre, textes de reading retenus, archétypes de writing, ce qui est écarté et pourquoi, propositions HP soumises au pilote, mesure des signatures neuves des devoirs.
