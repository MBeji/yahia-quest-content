"""Écrit le prompt d'auteur d'un lot d'examen SVT 9ᵉ : gen-prompt-svt.py <lot> (plan : gisement/9eme-svt-plan/plan-examens-v1.json)."""
import json, sys
SP = '/tmp/claude-0/-home-user/b03814da-e5f9-5a74-bf03-e7c23b20207a/scratchpad'
lot = sys.argv[1]
plan = json.load(open(f'{SP}/gisement/9eme-svt-plan/plan-examens-v1.json', encoding='utf-8'))
L = next(l for l in plan['lots'] if l['id'] == lot)
M = {m['id']: m for m in plan['missions']}
ms = [M[i] for i in L['missions']]
chs = L['chapters']
rng = L['nnRanges']
low = lot.lower()
listing = '; '.join(f"`{c}` : fichiers {rng[c][0]:02d} à {rng[c][1]:02d}" for c in chs)
lsc = ' ; '.join(f"`git -C /home/user/yahia-quest-content ls-tree --name-only origin/main content/sciences-vie-terre/{c}/exercices/`" for c in chs)
txt = f"""Tu es un **auteur** du pipeline « gisement » (étude 36), **sciences de la vie et de la terre (SVT) 9ᵉ** (matière `sciences-vie-terre`). Tu transformes des exercices de **sujets officiels de l'examen national de 9ᵉ** en missions du portail. C'est une **reprise fidèle et citée** : ces sujets sont du corpus officiel.

1. **Consigne à suivre à la lettre** : `/home/user/yahia-quest-content/.claude/skills/content-ingest/references/gisement-auteur-examen.md`. Elle te fait charger d'abord `prof-svt-9eme`, puis `content-ecole-tn`.
2. **Ta liste** : {len(ms)} missions, une par ligne, dans `{SP}/author/exam/assign-svt-{lot}.md`.
   - Chaque ligne nomme la transcription officielle de la session (sous `content/programmes-officiels/examens-nationaux/9eme-base/sciences-vie-terre/`), le numéro de l'exercice, le chapitre, le fichier et son `displayOrder`.
   - Lis **seulement** les exercices qui te sont confiés.
   - L'archétype et le piège viennent du lecteur : ce sont des indications, la transcription fait foi. Un exercice qui couvre plusieurs notions (un QCM de quatre questions sur quatre leçons, par exemple) est placé dans UN chapitre : la mission reste l'exercice officiel entier ; chaque question s'appuie sur ce qu'enseigne son chapitre ou ceux qui le précèdent (point 5).
   - N'ouvre rien d'autre sous `/tmp/claude-0/`, ni sous `content/programmes-officiels/sources-externes/`.
3. **Fichiers, numéros et `displayOrder`** : ceux de ta liste, sans rien renommer d'existant. Chapitres et plages : {listing}.
   - Lis les missions existantes de ces chapitres pour la forme (matière en arabe, étiquettes, figures) et pour **ne pas répéter leurs formulations**. L'arbre de travail garde parfois des versions périmées de fichiers déjà publiés : lis les publiés sur `main` ({lsc}, puis `git -C /home/user/yahia-quest-content show origin/main:<chemin>`). Lis aussi le `cours.md` et le `resume.md` du chapitre : ils disent le vocabulaire et les faits enseignés (la campagne « 9ᵉ au patron » a refait les cours de SVT : les chapitres `sciences-vie-terre` de l'arbre de travail ont été resynchronisés avec `origin/main` le 2026-10-01 ; en cas de doute, lis sur `origin/main`).
   - Chaque exercice officiel donne sa propre mission, même s'il ressemble à un autre : ce sont des annales. N'écris rien d'autre dans ces dossiers.
   - Les énoncés portent les **données de leur session** (valeurs des tableaux, résultats des expériences), pour que le contrôle « paires proches » des gates reste à 0 dans ta tranche.
4. **Titre** : « 🏛️ مناظرة <année> · التمرين <N> » suivi des étoiles et du sujet (arabe, dans la langue de la matière). L'en-tête suit l'étage (d2 practice 75/15 ; d3 boss 120/30 ; d4 challenge 300/60). Un exercice d'examen n'est jamais d1 : une ligne notée d1 devient d2.
5. **Programme en vigueur (R-3)**
   - Ordre du manifeste (`content/programmes-officiels/manifest/9eme-base.json`, sujet `sciences-vie-terre`) : 01 → 02 → 03 → 04 → 05 → 06 → 07 → 08 → 09 → 10 → 11 → 12 → 13 → 14. Une question ne s'appuie que sur son chapitre et les précédents.
   - Un item marqué `[hors programme en vigueur : …]` dans la transcription **ne devient pas une question** : si la suite en dépend, donne son résultat dans l'énoncé (« on admet que… ») et dis-le dans ton rapport. Un item `[illisible]` ne s'invente pas : saute-le et signale-le.
   - Une notion qu'aucun cours du manifeste n'enseigne se donne dans l'énoncé de CHAQUE question qui l'emploie.
6. **Du sujet imprimé à la question fermée** : les consignes « légender », « compléter », « relier », « justifier », « rédiger » deviennent des questions fermées du portail (QCM, plusieurs réponses, mise en ordre, appariement) dont les options sont des réponses plausibles d'élève ; une sous-question de rédaction se découpe en deux ou trois questions de raisonnement, jamais en une question où la clé est une phrase longue. Chaque question redonne les **données du document** (tableau, résultats, valeurs lues sur la courbe) pour se lire seule.
   - **Documents et schémas** : un schéma ou une courbe se refait en SVG vrai (légendes par lettres ou nombres, arabe seulement dans `<title>`), ou — quand le dessin n'ajoute rien — se remplace par un **tableau de valeurs** ou une description complète dans l'énoncé. Jamais de question qui renvoie à un document absent, jamais de figure qui donne la clé. Les figures sont décrites entre crochets dans la transcription, avec leurs données : tu les reprends fidèlement.
   - **Exactitude scientifique** : chaque fait est celui du manuel tunisien de 9ᵉ (voir `cours.md`). Double résolution : chaque clé est justifiée deux fois (cours, puis document de l'énoncé) ; un fait d'un sujet qui contredit le cours se signale dans le rapport, il ne s'adapte pas en silence.
7. **Étiquettes d'erreur** : le registre `content/misconceptions.json` porte depuis privé#569 une famille SVT `bio.*` (une centaine d'identifiants, par chapitre : `bio.nerv.…`, etc.). Lis les libellés **sur `origin/main`** (`git -C /home/user/yahia-quest-content show origin/main:content/misconceptions.json` — l'arbre de travail est en retard) et pose sur un distracteur de QCM l'étiquette dont le libellé nomme EXACTEMENT l'erreur qu'il exécute ; n'invente aucun identifiant et n'étiquette pas une option de question `multi`, `ordering` ou `matching` (l'étiquette y serait perdue ; la validation la refuse). Un distracteur sans étiquette adéquate reste **muet** : décris dans ton rapport, par question, l'erreur d'élève qu'il exécute (une phrase), pour qu'une étiquette soit créée si la famille revient.
8. **`chapter.json`** : si la ligne n'y est pas encore, ajoute à `sources[]` exactement : « Sujets officiels de l'examen national de fin d'études de l'enseignement de base (9ᵉ), Ministère de l'Éducation (corpus officiel, reprise citée, étude 36) — transcriptions : programmes-officiels/examens-nationaux/9eme-base/sciences-vie-terre/ ». Rien d'autre dans ce fichier.
9. **Écris chaque fichier dès qu'il est prêt**, puis passe au suivant.

D'autres auteurs écrivent en même temps dans d'autres chapitres : n'y touche pas. Un rouge des gates qui ne nomme pas tes fichiers n'est pas le tien.

**Validation**
- Chaque distracteur est faux **en fait** (pas seulement dans la forme) et exécute une erreur plausible ; la clé n'est jamais l'option la plus longue ; aucune option ne devient vraie sous les données de l'énoncé.
- Puis : `source {SP}/engine-env.sh && cd /home/user/yahia-quest-arena && npm run -s content:gates -- --tranche`.

**Ton dossier de travail** : `{SP}/svt-{low}-work/` (crée-le pour tes scripts de génération et de contrôle ; ne touche à aucun autre dossier du scratchpad : d'autres auteurs y écrivent, un fichier partagé a déjà été écrasé). Écris des notes d'avancement dans ce dossier au fil du travail : une limite de session peut te couper à tout moment.

**Rendu arabe (à jour)** : depuis arena#1137 à #1145 le moteur traite seul la ponctuation de bord, les formules ouvertes par un nombre ou un signe collé à une lettre, et « ∠ » : écris les énoncés naturellement. Les symboles chimiques et les formules (CO₂, O₂, g/L) se reconnaissent ; évite une ligne qui ne contient QUE des chiffres séparés par des virgules arabes (« ٣ ، ٥ »).

Rapport final comme la consigne le demande (liste des fichiers, adaptations de forme, items écartés, erreurs de distracteurs par question). Pas de commit.
"""
open(f'{SP}/author/exam/prompt-svt-{lot}.md', 'w', encoding='utf-8').write(txt)
print(f'{SP}/author/exam/prompt-svt-{lot}.md', len(txt))
