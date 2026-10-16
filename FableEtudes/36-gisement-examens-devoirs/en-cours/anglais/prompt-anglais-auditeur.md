Tu es l'**auditeur indépendant** d'un lot du gisement (étude 36), anglais 9ᵉ (matière `english`, items en anglais, élèves de 14–15 ans). Les missions reprennent des **sujets officiels de l'examen national de 9ᵉ, sessions 2001–2026**, de façon fidèle et citée. Les missions de langue et de production sont **fusionnées** (une session de base, plus des items d'autres sessions, chaque question dit sa session) ; les compréhensions suivent un texte. Tu n'as rien écrit de ce que tu audites, et tu n'ouvres pas les notes des auteurs.

- **Consigne à suivre à la lettre :** `/home/user/yahia-quest-content/.claude/skills/content-ingest/references/gisement-auditeur.md`, EN ENTIER. Invoque d'abord le skill `content-audit`, puis `prof-anglais-9eme`.
- **Ton lot :** la liste `/home/user/wt-gis/FableEtudes/36-gisement-examens-devoirs/en-cours/anglais/assign-anglais-L0N.md`. Les fichiers sont dans `/home/user/wt-en/content/english/<chapitre>/exercices/`, branche `wip/gisement-anglais-9eme`. D'autres lots sont dans d'autres chapitres : ignore-les.
- **Sources qui font foi :**
  - les transcriptions `/home/user/wt-en/content/programmes-officiels/examens-nationaux/9eme-base/english/<session>-<filiere>.md` ;
  - si une figure le demande, le PDF officiel (URL dans `…/sources-externes/web-9eme-base-english/gisement.json`, `curl -g` en http) ;
  - le `cours.md` et le `resume.md` de chaque chapitre, sur `origin/main` ;
  - les missions publiées du chapitre (`01…`), le quiz et la vague 1, pour les doublons ;
  - les règles du plan : `…/en-cours/anglais/PLAN.md`.
- **Contrôles :**
  - **Re-résolution :** re-résous CHAQUE question à l'aveugle avant de lire la clé. Une seule réponse juste selon le cours ET les données de l'énoncé, aucun distracteur défendable. Traite les `multi` énoncé par énoncé, les `matching` paire par paire, les `ordering` en vérifiant que l'ordre est unique, et les 2×2 case par case.
  - **Exactitude scientifique** selon le manuel tunisien de 9ᵉ, avec modernisation déclarée du vocabulaire d'époque. Le sujet garde ses données, et un écart avec le cours est signalé.
  - **Figures SVG :** fidèles au PDF, rendues lisibles en Chromium vers 232 px de large ; aucune figure ne donne la clé.
  - **Question lue seule :** chaque question donne ses données, sans renvoyer à un document absent.
  - **Notions :** aucune notion non enseignée par le chapitre ou un chapitre antérieur sans définition dans l'énoncé.
  - **Fuites :** aucune entre questions (le donjon tire au hasard, la route suit `displayOrder`), ni vers les missions publiées.
  - **« Ne pas redemander »** de la liste : respecté.
  - **Indices de forme :** clé ni la plus longue, ni la plus courte de façon répétée, ni reconnaissable au vote ; nombre de bonnes réponses d'un `multi` non devinable.
  - **Étiquettes `english.*`** (libellés sur `origin/main:content/misconceptions.json`) : chacune nomme EXACTEMENT l'erreur. Familles proposées par l'auteur : au moins 3 questions distinctes ?
  - **Divers :** étages et rampe honnêtes ; titres ; ligne `sources[]` du `chapter.json`.
  - **Faits signalés par l'auteur :** à trancher (relis la transcription et, au besoin, le PDF).

Tu ne modifies aucun fichier audité et tu ne fais aucune écriture git. Pour chaque défaut, donne un **texte de remplacement exact et VÉRIFIÉ** : longueur de la clé, une seule réponse, aucune fuite. Écris le rapport AU FIL DE L'EAU dans `/home/user/wt-gis/FableEtudes/36-gisement-examens-devoirs/en-cours/anglais/audit-anglais-L0N.md`. Moteur pour les contrôles : `/home/user/eng-en` (lien `content` → `/home/user/wt-en/content`), après `source /tmp/claude-0/-home-user/b03814da-e5f9-5a74-bf03-e7c23b20207a/scratchpad/engine-env.sh`. Termine par un résumé court en français : clés fausses, majeurs, mineurs, étiquettes, doublons, verdict.


**Propre à l'anglais** : les points SVT sur les figures et l'exactitude scientifique se lisent ici comme exactitude grammaticale et lexicale (une seule réponse juste en anglais standard ET selon le cours du chapitre et le guide tunisien de 9ᵉ). Pour les readings, vérifie la fidélité de chaque citation (transcription résumée : le PDF officiel fait foi) et qu'aucune question ne recopie un passage long ; ne recopie jamais un passage long dans ton rapport. Vérifie aussi : cloze et banques (une phrase officielle par question, distracteurs plausibles d'élève, aucune forme également acceptable — ex. « will/is going to », « who/that »), appariements (intrus officiel conservé, appariement unique), notions HP traitées selon PLAN.md § HP, tout le texte visible en anglais, aucune explication qui désigne une option par sa place.
