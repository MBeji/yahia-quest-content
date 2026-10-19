# Audit M1 — missions du gisement, french-6eme `01` et `02` (8 fichiers, 66 questions)

> Auditeur indépendant (opus), 2026-10-19. Branche `wip/francais-6eme-un-passage` (worktree `wt-fr6b`).
> Grilles : `prompt-auditeur.md`, skill `content-audit`, grille français 9ᵉ. Autorités : `assign-M1.md`, `PLAN-gisement.md` (R1–R10, E1–E8), transcriptions `examens-nationaux/6eme-base/french/` (2009, 2012, 2013, 2015-2017, 2019, 2020, 2022-2026 relues aux items repris), PDF officiel 2026 relu en image (texte de la lecture m006).
> Méthode : les 66 questions ont été re-résolues à l'aveugle (clés masquées) avant de lire les clés et la section « Missions du gisement » du rapport de l'auteur. Rien n'a été modifié sous `content/`, aucune écriture git.

## 0. Gates

| Contrôle | Résultat |
| --- | --- |
| `content:check` | ✓ `french-6eme: 8 chapters, 73 exercises, 502 questions` |
| `content:qa -- --subject french-6eme` | ✓ aucune clé suspecte |
| `content:tranche … 01,02 --fresh --strict-longest` | ✓ clé jamais strictement la plus longue (0/103) ; positions 22/30/22/25 % ; ⚠ 4 paires proches, 3 groupes gabarit (voir § 4) |
| `content:gisement:controle -- --sources …/devoirs-snapshots/french-6eme` sur les 3 devoirs | ✓ 0 plage ≥ 8 mots, 0 plage ≥ 6 mots, 0 exercice dont on reprend 2 ou 3 données (sortie 0) |
| Rendu | 0 `_` ou `*` résiduel dans les 8 fichiers |
| `sources[]` des deux `chapter.json` | ✓ ligne « Sujets officiels du concours… » présente |

## 1. Synthèse

Toutes les clés actuelles sont justes. Mais **deux questions ont une seconde réponse défendable** (C-1, C-2) et **une question est insoluble sans le texte** (C-3). Le défaut le plus répandu est une **fuite entre questions jumelles** (M-2) : la question de la seconde case redonne, déjà remplie, la réponse de la première. Le donjon tirant les questions au hasard, l'une donne la clé de l'autre.

| Mission | Q | Critiques | Majeurs | Mineurs |
| --- | --- | --- | --- | --- |
| m001 `01/06` temps | 8 | 0 | 1 | 1 |
| m002 `01/07` devoir classer | 6 | 0 | 1 | 0 |
| m003 `01/08` devoir métier | 6 | 0 | 0 | 0 |
| m004 `02/06` déterminants | 10 | 1 | 1 | 2 |
| m005 `02/07` impératif | 11 | 0 | 1 | 1 |
| m006 `02/08` lecture 2026 | 10 | 2 | 2 | 1 |
| m007 `02/09` récit écrans | 8 | 0 | 1 | 1 |
| m008 `02/10` devoir relier | 7 | 0 | 1 | 0 |

## 2. Critiques

### C-1 — m004 q3-q4 (2024, « notre aventure à mon père ») — trois possessifs défendables

La réécriture « Quand vous avez raconté … aventure à … parents » admet aussi « notre aventure » (vous avez raconté NOTRE aventure) et surtout « mes parents » ou « nos parents » : le « mon » de départ appartient à « je », que le passage de « nous » à « vous » ne touche pas. Sans corrigé publié, ces lectures sont grammaticales et défendables. Il faut dire à qui appartiennent l'aventure et les parents.

- q3 `prompt` : `(Concours 2024) Consigne : « Réécris cette phrase en faisant les changements nécessaires. » Phrase de départ : « Quand nous avons raconté notre aventure à mon père, il nous a dit que les phoques étaient plus nombreux dans cet archipel. » Début de la réécriture : « Quand vous avez raconté … aventure à … parents, ils vous ont dit que les baleines étaient plus nombreuses dans cette île. » L'aventure et les parents sont maintenant ceux de « vous ». Quel déterminant complète le premier vide ?`
- q4 `prompt` : `(Concours 2024) Même réécriture : « Quand vous avez raconté … aventure à … parents, ils vous ont dit que les baleines étaient plus nombreuses dans cette île. » L'aventure et les parents sont ceux de « vous ». Quel déterminant complète le second vide ?`

Vérifié : q3 → votre seul ; q4 → vos seul ; la case remplie de q4 ne livre plus la clé de q3 (voir M-2). Même précaution recommandée en q1-q2 (2025) : ajouter `Les impressions et le journal sont ceux des deux filles.` avant la question (« ses » / « son » se lisent sinon comme les affaires de l'amie).

### C-2 — m006 q10 (justifier « je suis d'accord ») — l'option c répond littéralement à la question

On demande « Quelle justification s'appuie sur le texte ? ». Or c cite le texte (« Mme Guégan a souvent des idées bizarres », phrase du texte) : elle s'appuie bien sur le texte, même si elle ne justifie pas l'ennui.

- `prompt` : remplacer la dernière phrase par `Tu es d'accord avec ces élèves. Quelle phrase justifie ce point de vue en s'appuyant sur le texte ?`
- c → `Je suis d'accord : sans écrans, tout le monde s'ennuie toujours et partout, c'est bien connu de tous.` [`fr.lecture.deduction-sans-indice`] (101 car. ; la clé d en fait 96 : elle n'est pas la plus longue)
- fin de l'`explanation` : `… dire qu'on n'est pas d'accord change de position, et affirmer que tout le monde s'ennuie partout ne s'appuie sur rien du texte.`

Vérifié : d seule.

### C-3 — m006 q1 (personnages qui rejettent l'idée) — insoluble sans le texte, et la question n'est plus celle du sujet (doute 1)

La mission ne fournit pas le texte. q1 ne cite aucune phrase et demande « lequel annonce l'échec » : l'élève doit deviner. En plus, la consigne officielle redonnée (cocher les personnages qui **rejettent** l'idée) ne correspond pas à la question posée, qui ajoute Mme Guégan, hors de la liste officielle. La réponse au sujet officiel est unique et se défend : **Louis et Gordon** (Louis rit et juge « complètement débile » l'idée d'essayer ; Gordon dit qu'on n'aura jamais le temps). Paloma est enthousiaste. Je propose de reprendre le sujet tel quel, en question à choix multiples :

- `type` `multi` ; `prompt` : `(Concours 2026) Texte : Louis raconte une scène de classe où la maîtresse, Mme Guégan, propose dix jours sans écrans. Louis juge « complètement débile » la phrase « Ce serait chouette d'essayer. » Gordon murmure : « On n'aura jamais le temps de donner envie aux autres. » Paloma s'écrie : « Moi, je peux même commencer dès ce soir ! » Consigne : « Coche la bonne réponse. Les personnages qui rejettent l'idée de passer dix jours sans écrans sont : Paloma, Louis, Gordon. » Quels personnages rejettent l'idée ?`
- options a `Paloma` · b `Louis` · c `Gordon` · d `Mme Guégan` (toutes muettes : multi) ; `answerKey` `{"correct": ["b", "c"]}`
- `explanation` : `Louis trouve « débile » l'idée d'essayer et Gordon annonce qu'on n'aura jamais le temps : tous deux rejettent le défi. Paloma veut commencer dès ce soir, et Mme Guégan est celle qui le propose.`

Vérifié sur le PDF : citations mot pour mot. La question ne livre pas la clé de q2 (« on sera morts d'ennui » n'y figure pas) ni celle de q3 (qui a dit « chouette »).

## 3. Majeurs

### M-1 — m001 q1-q2 (2025, « Bientôt ») — la phrase officielle est altérée, et elle contredit la clé

La transcription imprime deux vides : « Bientôt, une voix ........ à hurler... Une tête ........ ». La mission remplit le second vide par « surgit », un **présent**, juste après avoir posé que « bientôt » impose le futur. Remplacer, dans les deux `prompt`, `Une tête surgit.` par `Une tête …` ; en q1, `Quel temps le mot « bientôt » impose-t-il ?` → `Quel temps le mot « bientôt » impose-t-il aux deux verbes ?`. Clés inchangées (futur ; se mettra).

### M-2 — fuites entre questions jumelles (m004, m005)

La seconde question de chaque paire redonne la clé de la première, déjà remplie dans sa phrase : m004 q2 (« leurs »), q4 (« votre » ; corrigé par C-1), q6 (« Cet »), q8 (« Cette nuit-là ») ; m005 q3 affiche « va » (clé de q4), q4 affiche « Prends » (clé de q3) ; m005 q6 donne « Faites », or c'est la clé décisive de q8 (« Regardez – faites » contre « Regardez – faisez »). Remplacements :

- m004 q2 : `(Concours 2025) Même phrase : « Jeanne et son amie couchent … impressions sur … journal de voyage. » Les impressions et le journal sont ceux des deux filles. Quel déterminant complète le second vide ?`
- m004 q6 : `(Concours 2023) Même réécriture : « … ami venait à la maison toutes les matinées pour m'apporter … leçon et … devoir. » Quelles formes complètent les deux derniers vides ?`
- m004 q8 : `(Concours 2022) Même réécriture : « … nuit-là, j'ai demandé à ma mère de me faire sortir de … embarras. » Quel groupe complète le second vide ?`
- m005 q3 : `Début de la réponse : « … la piste tortueuse et va à l'école ! »` → `Début de la réponse : « … la piste tortueuse et … à l'école ! »` et `complète le début ?` → `complète le premier vide ?`
- m005 q4 : `(Concours 2024) Même réponse : « … la piste tortueuse et … à l'école ! » Quelle forme d'« aller » complète le second vide ?`
- m005 q8 : options a `Regarde – faites` [`fr.conj.imperatif-avec-sujet`, qui couvre « à une autre personne »] · b `Regarder – faire` [`fr.conj.conjugue-infinitif-confondus`] · c `Vous regardez – vous faites` [`fr.conj.imperatif-avec-sujet`] · d `Regardez – faites` (clé). `explanation` : `La maîtresse parle à plusieurs élèves : 2e personne du pluriel, sans pronom sujet : regardez, et faites, la forme irrégulière de faire. « Regarde » ne s'adresse qu'à un seul élève, l'infinitif ne donne pas d'ordre et « vous regardez » garde le sujet.` Ainsi q8 ne teste plus « faites », que q6 donne et que `02/02-boss#4` pose déjà. Clé 17 car. ; c en a 27.

### M-3 — m002 (devoir « classer les mots ») — deux questions en donnent deux autres

q1 relie « Sousse » à « nom propre » : c'est la clé de q2. q4 coche « clientes » parmi les noms communs : c'est la clé de q5.

- q1 : l1 `Sousse` → `Samir` (paire l1-r2 inchangée). `explanation` : remplacer `« Sousse » est le nom d'une ville précise, avec une majuscule : un nom propre.` par `« Samir » est le prénom d'une personne précise, avec une majuscule : un nom propre.`
- q5 `prompt` : `Dans la phrase « Roses et tulipes arrivent chaque matin. », dans quelle colonne place-t-on le mot « matin » ?`. Options inchangées (clé a « nom commun », c `nom propre` étiqueté). `explanation` : `« Matin » désigne un moment de la journée en général : il s'écrit sans majuscule et on peut dire « le matin ». C'est un nom commun, ni un nom propre, ni un pronom, ni un déterminant.`

Vérifié : chaque question a sa clé propre ; la clé n'est pas la plus longue.

### M-4 — m006 q4 (multi, caractère commun du narrateur et de Gordon) — trois distracteurs éliminés d'un coup d'œil

c, d et e parlent de Paloma, de la maîtresse et de Pablo ; la question porte sur le narrateur et Gordon. L'explication le dit elle-même. Leurre de la carte : des actions **des deux garçons** sans lien avec le trait.

- c → `Louis ne se retourne même pas quand une élève parle.`
- e → `Gordon murmure qu'on n'aura jamais le temps de donner envie aux autres.`
- `explanation` : `Louis ne peut pas se retenir de rire à une blague, et Gordon l'imite : les deux amis sont rieurs. Ne pas se retourner ou murmurer qu'on n'aura pas le temps ne concerne qu'un des deux garçons, et le vote est une idée de la maîtresse.`

Vérifié sur le PDF (« Je ne me retourne même pas », « On n'aura jamais le temps de donner envie aux autres, murmure Gordon ») ; clé [a, b] inchangée et seule.

### M-5 — m006 q2 — citations recousues, et une explication qui désigne l'option par son rang

b colle deux répliques séparées de la maîtresse ; d colle deux répliques séparées de Paloma. L'explication dit « Seule la dernière phrase » alors que la clé est l'option a, et les options sont mélangées à l'affichage.

- b → `« Je comptais vous proposer une expérience de ce type. »` ; d → `« Moi, je peux même commencer dès ce soir ! »` (mot pour mot d'après le PDF ; clé a, 61 car., n'est pas la plus longue : c en fait 85)
- `explanation` : `Seule la phrase « on sera morts d'ennui » annonce un échec : après deux jours sans écrans, Gordon prévoit que tout le monde s'ennuiera. Les autres sont des paroles de Paloma, enthousiaste, et de la maîtresse, qui propose l'expérience.`
- b, c, d : rendre muets (`fr.lecture.personnage-confondu` ne nomme pas l'erreur, qui est de prendre une proposition pour une prédiction d'échec).

### M-6 — m007 q2 — l'explication désigne les options par leur rang, et le fait faussement

« La première phrase raconte seulement l'arrivée de Paloma, la deuxième sort du sujet, et la troisième décrit Paloma » : ni l'ordre du fichier ni l'ordre affiché ne correspondent. `explanation` : `La réaction de Gordon est ce qu'il fait ou ressent quand Paloma le surprend : il rougit et cache le téléphone. « Le lendemain, Paloma arrive… » ne raconte que son arrivée, le vote de la maîtresse sort du sujet, et « Paloma fronce les sourcils » décrit la réaction de Paloma, pas celle de Gordon.`

### M-7 — m008 q3 — doublon de q1, et texte absent

q3 (« Nour est la grande sœur de Walid ») redonne la paire Nour ↔ grande sœur de q1 ; c'est la paire proche que mesure la tranche (0,46). De plus, q3 renvoie au texte (« D'après le texte… ») sans le citer : lue seule, elle ne se résout pas.

- `prompt` : `Lis : « Chez les Ben Salem, le téléphone sonne souvent. Nour, la grande sœur, envoie un message à sa cousine. Walid, le petit frère, appelle son oncle pour lui dire bonjour. Leur mère écrit un courriel à la maîtresse. » Combien de personnes le texte nomme-t-il par leur prénom ?`
- options a `Une` · b `Deux` (clé) · c `Trois` · d `Quatre`, toutes muettes
- `explanation` : `Seuls Nour et Walid sont nommés par leur prénom. La mère, la cousine, l'oncle et la maîtresse sont désignés par ce qu'ils sont, et « Ben Salem » est le nom de la famille, pas un prénom.`

Vérifié : deux seule.

## 4. Mineurs, paires et gabarits

- **m001 q3** : option d (phrase inchangée) étiquetée `fr.temps.indicateur-de-temps-ignore` ; la phrase n'a aucun indicateur de temps, l'erreur est d'ignorer la consigne. La rendre muette.
- **m004 q9** : « les noms soulignés » sans soulignement visible. Ajouter `(« plante » et « feuillage »)` après `les noms soulignés` dans la consigne citée, entre crochets d'auteur : `… au pluriel. » [Noms soulignés : plante, feuillage.]`
- **m005 q7** : la consigne officielle de 2020 est « Ecris la phrase à l'impératif. » (sans accent, coquille comprise, comme le veut la règle commune). Remplacer `Écris` par `Ecris`.
- **m007 q4** : la consigne de 2020 est tronquée. La citer en entier : `Consigne : « Raconte ce qui s'est passé en huit phrases au moins. Intègre dans ton récit un court dialogue où chacun de vous explique son point de vue et justifie son choix. »`
- **m004, étiquetage (doute 4)** : oui, un id est justifié. L'erreur « garder le possessif de la personne de départ » est portée par au moins trois distracteurs de m004 (q3 a « notre », q4 a « mes », q4 c « nos ») et revient dans d'autres sujets (2023 « ta – ton »). Id proposé : `fr.det.possessif-personne-non-changee`, libellé fr : `Tu gardes le possessif de la personne de départ quand le possesseur change (nous → vous : notre aventure → votre aventure ; je → nous : mes amis → nos amis) : le possessif suit la personne qui possède.` Après C-1, il nomme exactement l'erreur de ces trois options.
- **Paires proches** : m004 q1-q2, q3-q4 et q7-q8 sont les deux vides d'une même phrase officielle, et m008 q1-q3 deux questions sur un même texte. Après M-2, C-1 et M-7, aucune paire ne livre plus la clé de l'autre. La parenté des énoncés est voulue et ne fuit pas.
- **Gabarits « synonyme / contraire »** (m006 q6-q8 avec les chapitres 05, 06, 07, 08) : le cadre est la consigne officielle de chaque session ; les mots et les textes diffèrent, aucune clé ne passe d'une question à l'autre. Pas de fuite.
- **« Ne pas redemander »** : respecté. m005 q3-q4 (prends, va) et m002 q3 (groupe mixte → ils) touchent des gestes du patron, mais sur une phrase officielle ou un texte neuf, comme la carte le prévoit.
- **Conversion** : toutes les questions ouvertes du sujet sont devenues fermées (QCM, multi, ordering, matching) ; aucune `short_answer` dans le lot, donc pas de risque de réponse dans l'explication.

## 5. Fidélité (vérifiée sur les transcriptions et, pour 2026, sur le PDF)

Toutes les phrases officielles sont mot pour mot et chaque question dit sa session, sauf M-1 (case remplie par « surgit »), M-5 (répliques recousues) et les deux coquilles ou troncatures de § 4. Les blancs hors cible (`toutes`, `nombreuses`, `cette`, `Finis`, `Faites`) sont donnés, comme le veut la règle R1. Le paradigme de « être » à l'impératif est donné dans l'énoncé de m005 q10 (doute 3), ce qui est juste puisque le cours du `02` ne l'enseigne pas. « Faites » donné en q6 est sans dommage une fois M-2 appliqué.

## 6. Doutes de l'auteur — tranchés

1. **m006 q1** : « Gordon » est bien la seule réponse à la question posée, mais celle-ci s'écarte du sujet et ne se résout pas sans le texte. Remplacée par la question officielle en choix multiple, clé Louis + Gordon (C-3).
2. **m006 q8-q10** : *désagréable* (q8) et *plaisir* (q9) sont seuls justes parmi leurs options (q9 : *tristesse* n'est pas un contraire, *amusant* et *ennuyeux* ne suivent pas « combles de »). q10 avait deux réponses défendables (C-2) ; corrigée, elle n'en a plus qu'une.
3. **m005** : donner *faites* et le paradigme de *être* est juste. *faites* faisait fuir la clé de q8 : corrigé par M-2.
4. **m004** : oui, un id `fr.det.possessif-personne-non-changee` (§ 4).

## 7. Verdict

**À corriger** : 3 critiques (C-1 à C-3), 7 majeurs (M-1 à M-7), 4 mineurs. Chaque défaut a son texte de remplacement vérifié ci-dessus : une seule réponse, la clé n'est pas la plus longue, aucune fuite. m003 est prêt tel quel. Après correction : relancer `content:check`, `content:qa`, `content:tranche --fresh --strict-longest` et `content:gisement:controle` sur m002 et m008.
