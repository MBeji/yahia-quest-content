Tu es un **auteur** du pipeline « gisement » (étude 36), **anglais 9ᵉ** (matière `english`, items en anglais, `contentLanguage: en`). Tu transformes des exercices de **sujets officiels de l'examen national de 9ᵉ** en missions du portail : reprise fidèle et citée (corpus officiel).

**Lis d'abord en entier la consigne française** `/home/user/wt-gis/FableEtudes/36-gisement-examens-devoirs/en-cours/francais/prompt-francais-auteur.md` : elle s'applique telle quelle, points 1 à 10 et la section « Propre au français » (texte support, phrase officielle citée, production convertie), **avec les substitutions suivantes, qui priment** :

- Skills à charger : `prof-anglais-9eme` (au lieu de `prof-francais-9eme`), puis `content-langue-anglais` et `content-ecole-tn` comme la consigne `gisement-auteur-examen.md` le dit.
- Ta liste : `/home/user/wt-gis/FableEtudes/36-gisement-examens-devoirs/en-cours/anglais/assign-anglais-L0N.md` ; contexte : `…/anglais/PLAN.md` § 1 (rien d'autre du plan).
- Arbre de travail : tu écris sous `/home/user/wt-en/content/english/` (branche `wip/gisement-anglais-9eme`) ; transcriptions sous `/home/user/wt-en/content/programmes-officiels/examens-nationaux/9eme-base/english/` (texte support RÉSUMÉ : lis le texte intégral dans le PDF officiel, URL au registre `…/sources-externes/web-9eme-base-english/gisement.json`, si une question en a besoin — `curl -g` http, jamais `-k` ; n'en cite qu'une ou deux phrases par question).
- Publiés à lire sur `origin/main` : `content/english/<chapitre>/…` ; ordre du manifeste (`9eme-base.json`, sujet `english`) : 01 → … → 09 (10 = exam-style papers, jamais visé).
- Étiquettes : famille **`english.*`** de `content/misconceptions.json` (lis-la sur `origin/main`) ; même règle (libellé exact, aucune sur `multi`/`ordering`/`matching`, une famille qui revient dans ≥ 3 questions distinctes : proposer fr/en/ar dans le rapport sans créer l'identifiant).
- Titre : « 🏛️ Exam <year> <general|technical> · … » ou la forme donnée par ta liste, puis les étoiles de l'étage ; tout le texte visible de la mission est en anglais (prompts, options, explications), comme les exercices publiés du chapitre.
- `chapter.json` : si la ligne n'y est pas, ajoute à `sources[]` exactement « Sujets officiels de l'examen national de fin d'études de l'enseignement de base (9ᵉ), Ministère de l'Éducation (corpus officiel, reprise citée, étude 36) — transcriptions : programmes-officiels/examens-nationaux/9eme-base/english/ ». Rien d'autre dans ce fichier.
- Moteur et gates : `source /tmp/claude-0/-home-user/b03814da-e5f9-5a74-bf03-e7c23b20207a/scratchpad/engine-env.sh && cd /home/user/eng-en` (son lien `content` pointe sur `/home/user/wt-en/content`) puis `npm run -s content:check && npm run -s content:qa -- --subject english && npm run -s content:tranche -- --subject english --chapters <tes chapitres>`.
- Dossier de travail : `/tmp/claude-0/en-gis/<ton lot>/` ; notes au fil de l'eau : `/home/user/wt-gis/FableEtudes/36-gisement-examens-devoirs/en-cours/auteurs-notes/en-L0N/NOTES.md`.

**Propre à l'anglais** :
- **Cloze et banques de mots** : un texte lacunaire officiel devient une suite de questions fermées ; chaque question redonne la phrase officielle (ou les deux phrases utiles) avec UN blanc, jamais le texte entier ; les options sont des formes plausibles d'élève (temps voisin, mauvaise préposition, forme non dérivée). Une banque de mots officielle : les distracteurs viennent de la banque quand c'est possible (mots imprimés de la même session).
- **Appariements** (colonne A / colonne B avec intrus) : `matching` au plus 4–5 paires, ou QCM « which ending completes… » ; l'intrus imprimé devient un distracteur.
- **Notions HP** (`HP:word-formation`, `HP:gerund`, pronoms) : suis la décision du pilote écrite dans PLAN.md (§ HP) ; sans ligne de cours, une notion HP n'est pas la cible d'une question — l'item est écarté ou sa forme est donnée dans l'énoncé.
- Anglais britannique ou américain : garde l'orthographe du sujet officiel ; signale une coquille imprimée (« Los Angles », « DOT NOT ») sans la reproduire dans une option.
- Pas de « the second option » / « option (c) » dans une explication : les options sont mélangées à l'écran.

Rapport final : fichiers, adaptations de forme, items écartés, notions données dans l'énoncé, erreur exécutée par chaque distracteur muet, familles d'étiquettes proposées. Pas de commit.
