"""Écrit le prompt d'un auditeur de lot d'examen : gen-prompt-audit.py <spec.json> [sortie.md]
spec = {"lot","subject" (dossier content/), "chapter", "nn":[…], "classe":"9eme-base", "matiere_manifeste":"math|sciences-vie-terre",
        "ordre_manifeste":"…", "blind_extra","fidelity","programme","etiquettes","distracteurs_extra","doublons":"…",
        "intro_matiere":"maths 9ᵉ"}"""
import json, sys, glob, os, re
SP = '/tmp/claude-0/-home-user/b03814da-e5f9-5a74-bf03-e7c23b20207a/scratchpad'
S = json.load(open(sys.argv[1], encoding='utf-8'))
out = sys.argv[2] if len(sys.argv) > 2 else f"{SP}/author/exam/prompt-audit-{S['lot']}.md"
subj, lot = S['subject'], S['lot']
classe = S.get('classe', '9eme-base')
chapters = S.get('chapters') or [{'chapter': S['chapter'], 'nn': S['nn']}]
multi = len(chapters) > 1
files = []
for C in chapters:
    ch = C['chapter']
    for n in C['nn']:
        g = glob.glob(os.environ.get('CORPUS','/home/user/wt-gis')+f'/content/{subj}/{ch}/exercices/{n:02d}-*.json')
        assert len(g) == 1, (ch, n, g)
        d = json.load(open(g[0], encoding='utf-8'))
        qs = d['questions']
        types = {}
        for q in qs: types[q.get('type', 'qcm')] = types.get(q.get('type', 'qcm'), 0) + 1
        ramp = ','.join(str(q.get('difficulty', '?')) for q in qs)
        sess = re.match(r'\d+-examen-([0-9]{4}(?:-[a-z]+)?)-', os.path.basename(g[0])).group(1)
        label = f"{ch[:2]}/{n:02d}" if multi else f"{n}"
        files.append(dict(ch=ch, n=n, label=label, base=os.path.basename(g[0]), nq=len(qs), mode=d.get('mode'), xp=d.get('xpReward'), coins=d.get('rewardCoins'), ramp=ramp, types=types, sess=sess))
tot = sum(f['nq'] for f in files)
modes = {'practice': 'd2', 'boss': 'd3', 'challenge': 'd4'}
flist = '\n'.join(f"- `{f['ch']}/exercices/{f['base']}` ({f['nq']} questions{', ' + ', '.join(f'{v} {k}' for k, v in f['types'].items() if k != 'qcm') if any(k != 'qcm' for k in f['types']) else ''}, {modes.get(f['mode'], f['mode'])} {f['mode']} {f['xp']}/{f['coins']})" for f in files)
rampl = ' ; '.join(f"{f['label']} : {f['ramp']}" for f in files)
etages = ' ; '.join(f"{f['label']} en {modes.get(f['mode'], f['mode'])} ({f['mode']} {f['xp']}/{f['coins']})" for f in files)
trans = ', '.join(sorted({f"`{f['sess']}.md`" for f in files}))
nn = (f"{files[0]['n']} à {files[-1]['n']}" if not multi else ', '.join(f"{f['label']}" for f in files))
txt = f"""Tu es l'auditeur indépendant d'une tranche du gisement : {S['intro_matiere']}, missions tirées des **sujets officiels de l'examen national** (reprise fidèle et citée, corpus officiel).

- **Consigne à suivre à la lettre** : `/home/user/yahia-quest-content/.claude/skills/content-ingest/references/gisement-auditeur.md` (lis-la EN ENTIER : elle porte les « pièges relevés » sur les tranches précédentes, à chercher en priorité). Invoque d'abord le skill `content-audit`.
- Tu n'as rien écrit de ce que tu audites. N'ouvre rien sous `/tmp/claude-0/` (le SEUL chemin que tu y touches : écrire ton rapport dans `{SP}/author/exam/audit-{lot}.md`, à créer{S.get('tmp_exception','')}), ni sous `content/programmes-officiels/sources-externes/`.

**Périmètre exact** : dépôt `{os.environ.get('CORPUS','/home/user/wt-gis')}`, arbre de travail tel quel (d'autres fichiers y sont en cours d'écriture ou de correction : ignore-les). {('Chapitres ' + ', '.join('`content/%s/%s/`' % (subj, C['chapter']) for C in chapters)) if multi else ('Chapitre `content/%s/%s/`' % (subj, chapters[0]['chapter']))}, dossier `exercices/` ({len(files)} fichiers, {tot} questions) :
{flist}

Ce sont les seuls fichiers de l'auteur (les numéros inférieurs sont publiés). `chapter.json` n'est pas modifié par l'auteur (la ligne `sources[]` des sujets officiels est ajoutée à la livraison ; ne la juge pas). Chaque mission reprend un exercice dont la **transcription officielle** est sous `content/programmes-officiels/examens-nationaux/{classe}/{S['matiere_manifeste']}/` : {trans}.{S.get('extra_sources','')}

**Lire les missions déjà publiées** (pour comparer les gabarits et chercher les doublons) : `git -C /home/user/yahia-quest-content fetch -q origin main`, `git ls-tree -r --name-only origin/main content/{subj}/` puis `git show origin/main:<chemin>`. Le registre des étiquettes d'erreur et des compétences se lit de même (`git show origin/main:content/misconceptions.json`, `…/competences/<famille>.json` — l'arbre de travail est EN RETARD sur `origin/main`, lis les libellés sur `origin/main`). Les cours du chapitre et ceux des chapitres du manifeste disent ce qui est enseigné.

**Points d'attention propres à cette tranche**, en plus de la consigne :
- **Blind** : chaque clé est re-résolue **avant** de lire celle du fichier, à partir de l'énoncé, de la figure et de la transcription. Toute divergence est critique. {S['blind_extra']} Les FIGURES comptent : vérifie leur vérité (alignements, angles, proportions, étiquettes ; rends-les en Chromium si tu le peux) ; aucune figure ne donne la clé.
- **Fidélité au sujet** : chaque donnée est celle de la transcription. {S['fidelity']}
- **Étage** : {etages}. Donne ton avis argumenté sur l'étage de chaque mission et sur la difficulté de chaque question ; la rampe interne doit être non décroissante en ordre de fichier ({rampl}). Un en-tête d3/boss dont les questions seraient toutes d1–d2 est malhonnête : dis-le.
- **Programme (R-3) et ordre d'enseignement** : manifeste `content/programmes-officiels/manifest/{classe}.json`, sujet `{S['matiere_manifeste']}`, soit {S['ordre_manifeste']}. {S['programme']}
- **Étiquettes** : {S['etiquettes']}
- **Distracteurs** : chacun est **faux** (en valeur ou en fait) et exécute l'erreur que nomme son étiquette quand il en a une. Aucune valeur ne trahit la clé par sa fréquence dans les options ; la clé n'est jamais l'option la plus longue ; cherche : option somme ou différence de deux autres, vote majoritaire qui reconstruit une clé à plusieurs composantes, option qui nie une prémisse, énoncé qui annonce le résultat, donnée retirée ou ajoutée qui rend un distracteur vrai, rappel ou règle dans l'énoncé qui désigne la clé. {S.get('distracteurs_extra', '')}
- **Titres et en-têtes** : « 🏛️ مناظرة <année> [(تقني)] · التمرين <N> ⭐…: sujet » ; le sujet nomme les notions, jamais un résultat. Vérifie le titre exact, l'étage et `displayOrder` {nn}.
- **Doublons** : {S['doublons']} Des annales voisines qui recyclent des données ne sont un défaut que si la question est quasi identique (mêmes options, mêmes pièges, mêmes explications).
- **Fuites** : aucune explication ni aucun énoncé ne donne la clé d'une autre question ; chaque énoncé se lit seul (le donjon tire les questions AU HASARD parmi toutes les missions du palier, seule la route quête suit `displayOrder`) ; les résultats d'une étape précédente sont redonnés comme données dans l'étape suivante : dis si l'un livre la clé d'une AUTRE question ; pas de décimale de vérification qui livre un verdict ; la coche ✓ ne suit jamais un nombre qui est un distracteur.
- **Rendu arabe** : depuis arena#1137 à #1145 (mergées), la ponctuation et les parenthèses de prose qui bordent une formule restent dans la prose, les formules ouvertes par un nombre ou un signe collé à une lettre et « ∠ » sont isolés, une parenthèse que le texte arabe ferme ou ouvre reste hors de l'isolat. Passe les chaînes suspectes dans `isolateLtrRuns` / `splitMathRuns` (`src/shared/lib/bidi.ts` du moteur, `/home/user/yahia-quest-arena`, branche `origin/main`) ET rends-les dans Chromium `dir=rtl` : signale toute chaîne dont l'ordre affiché diffère du texte source. Une LIGNE de formule seule (sans mot arabe) que `isDisplayEquation` refuse — produit implicite « AM = 2/3 AB », barres « |x| », chaîne chiffres-lettres, terme seul à exposant « (3/21)³ » — s'affiche brouillée : signale-la avec le texte de remplacement. Une paire d'options écrite avec la virgule arabe (« −2 ، 3 ») se lit à l'envers : exige les valeurs étiquetées ou la forme (x ; y).
- **Piège de passe** : la regex de référence à une figure prend « على الشكل التالي » (« sous la forme suivante ») pour un renvoi à une figure sans SVG : signale les occurrences qui resteraient.
- **Figures** : vraies, aucune ne donne la clé, arabe seulement dans `<title>`, aucun élément ni attribut interdit, rien qui déborde du `viewBox` ; une figure dessinée à l'échelle de la solution permet de lire la clé : signale-le.
- **Ton propre correctif** : chaque fois que tu proposes un texte de remplacement (option, énoncé, explication, figure), vérifie contre l'énoncé, la figure et les questions voisines qu'il ne nie aucune prémisse, n'est pas VRAI sous les données, ne contredit aucun nombre donné, ne rend pas la clé devinable ; cinq lots de suite, un texte fourni par l'audit a lui-même été retrouvé défectueux à la re-vérification.

**Rapport** tel que la consigne le demande : un tableau par fichier (question, ta réponse, clé, verdict), les défauts classés (critique, majeur, mineur) avec le correctif **exact** proposé (texte de remplacement), puis le chiffre final. Tu ne modifies aucun fichier du dépôt. Écris ton verdict partiel dans le fichier de rapport dès que tu as fini un fichier, au cas où une limite te recoupe.
"""
open(out, 'w', encoding='utf-8').write(txt)
print(out, len(txt), tot, 'questions')
