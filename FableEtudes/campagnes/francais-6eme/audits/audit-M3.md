# Audit M3 — missions du gisement, french-6eme `05-sauver-la-nature` (06–10) et `06-etre-en-forme` (06–10)

> Auditeur indépendant (opus), 2026-10-19. Branche `wip/francais-6eme-un-passage`, commit `c106bfb2`.
> Grilles : `prompt-auditeur.md` (avec `content-audit` et la grille du 9ᵉ → `gisement-auditeur.md`). Autorités : la carte `assign-M3.md`, `PLAN-gisement.md` (R1–R10, E1–E8), les transcriptions `examens-nationaux/6eme-base/french/` et les PDF 2023 et 2024 relus en vision (texte intégral des deux lectures).
> Méthode : j'ai re-résolu à l'aveugle les 85 questions, sans les clés, avant de les lire. Je n'ai pas ouvert le rapport de l'auteur. Rien n'est modifié sous `content/`, pas d'écriture git.

## 0. Gates et contrôles

| Contrôle | Résultat |
| --- | --- |
| `content:check` | ✓ french-6eme : 73 exercices, 502 questions |
| `content:qa -- --subject french-6eme` | ✓ |
| `content:tranche --chapters 05…,06… --fresh --strict-longest` | ✓ 0/127 clé strictement la plus longue. ⚠ 39 paires proches (§ 2) et 9 groupes gabarit (§ 5) |
| `content:gisement:controle` (salle blanche) sur `06/10-devoir-corriger-les-erreurs.json` | ✓ 0 plage ≥ 8 mots, 0 donnée commune. Mes textes de remplacement de q4 et q5 repassés au contrôle : 0 aussi |
| Rendu | ✓ aucun `_` ni `*` résiduel. Les `___` sont des blancs voulus, que `RichField` affiche en texte brut. Aucune `short_answer` dans les 10 fichiers : la règle « l'explication ne donne pas la réponse » est sans objet. |
| Ajouts au cours | ✓ La puce « Présent » de *prendre/mettre* (cours 05 l.119 + résumé) et d'*aller/faire* (cours 06 l.120 + résumé) est juste. Elle couvre *met*, *reprend*, *vous mettez*, *nous allons*, et rien n'est plus enseigné sans cours. |

## 1. Re-résolution — clés

**85/85 clés justes.** Je n'ai trouvé qu'une seule double réponse : 06 m021 q8 (critique C-1).
- m015 : a b c (1-1,2-2) (1-1,2-2) d b a
- m016 : a b c d a b c d
- m017 : a b c d a b c d
- m018 : (a,b) a b c d d b a (a,b,c)
- m019 : (a,b,c) c d,a,b,c a d,a,b,c (a,b,c) c b
- m020 : a b c d a b c a b c d
- m021 : a b c d a b c d a
- m022 : a b (a,b) c d a b c d
- m023 : (a,b,c) b d,a,b,c (a,b,c) a b c d,a,b,c
- m024 : a b c b (a,b,c) d a d

**Fidélité** : toutes les phrases officielles sont reprises mot pour mot, et chaque question cite sa session.
- Seule normalisation : le « : » final des consignes devient « . », et « a- quel est » devient « Quel est » (2008). Coquille gommée : « vague . » (2026). Mineur, rien à corriger.
- La « Claudine écrit » du 2023 et les extraits du 2024 sont conformes au PDF, que j'ai relu.

**Conversion des questions ouvertes en fermées** : conforme à R1–R3, avec les écarts traités ci-dessous.

## 2. Les 39 paires proches : fuite ou pas (doute principal)

Ma règle de partage :
- il y a **fuite** quand l'énoncé ou les options d'une question, visibles avant de répondre, montrent la clé de l'autre, ou quand son explication l'énonce mot pour mot ;
- les autres paires sont des questions parallèles voulues sur une même phrase officielle.

| Paire | Verdict | Correctif |
| --- | --- | --- |
| 05 m016 q1↔q2 (2023, *met / reprend*) | **fuite** : l'option-clé de q1 contient « reprend », la clé de q2 | M-1 |
| 05 m016 q3↔q4 (2021) | **fuite croisée par les énoncés** : q3 affiche « j'aborderai », q4 affiche « je prendrai » | M-1 |
| 05 m017 q3↔q4, q5↔q6, q7↔q8 | **fuite croisée par les énoncés** (« nous jetons », « nous nous approchons », etc.) | M-1 |
| 06 m020 q4↔q5, q9↔q10, q7↔q11 | **fuite par les énoncés** : q4 affiche « iront », q5 « apporteront », q10 « Nous allons », q11 « a préparé » | M-1 |
| 06 m021 q1↔q2 | **fuite** : q1 affiche « longue », et q2 donne elle-même la règle (« long devient longue ») | M-2 |
| 05 m018 q2↔q3, q4↔q5 | **fuite** : q3 et q5 annoncent le sentiment (« Le premier sentiment … est la peur », « … la fascination ») | M-3 |
| 06 m023 q6↔q7↔q8 | **fuite** : la situation officielle contient « ordonne » et « supplient », et les répliques de q8 portent ces verbes | M-5 |
| 06 m024 q2↔q5 | **fuite et doublon** : mêmes phrases fautives (« Ma sœur est content », « son frère sont grand ») | M-6 |
| 06 m022 q1↔q2 | **fuite partielle** : les distracteurs de q1 (« rester immobile… », « réapprendre à marcher ») sont la clé de q2 | M-7 |
| 05 m015 q5↔q6 (2010) | **fuite par la correction** : chaque explication énonce la clé de l'autre, sur le même item officiel | M-8 |
| 05 m015 q7↔q8 (2008, a/b officiels) | **fuite par la correction** : l'explication de q7 dit « A la récréation est un complément non essentiel » | M-8 |
| 05 m016 q5↔q6, q7↔q8 · m017 q1↔q2 · m018 q6↔q7↔q8 · m019 q1↔q2↔q3, q4↔q5↔q6, q7↔q8 · m020 q6↔q8 · m021 q3…q9 · m022 q5↔q6, q7↔q8 · m023 q1↔q2↔q3↔q4 · m024 q3↔q8, q1↔q7 | **sans fuite** : même consigne ou même texte, autre mot, autre verbe ou autre geste | — |

## 3. Critique

### C-1 — 06 m021 q8 (2013, « Chers parents, vous nous manquez »)
L'option c, « Chère maman, vous nous manquez beaucoup. », est juste : c'est le vouvoiement. Il y a donc deux réponses défendables.
- Remplacer c par `Chère maman, vous nous manques beaucoup.` (`fr.accord.verbe-non-accorde-au-sujet`). Longueurs 38/40/40/38.
- Explication, sans renvoi par le rang : `On écrit à une seule personne, une maman : l'adjectif est au féminin singulier, chère, et le sujet « vous » devient « tu », avec le verbe au présent : tu manques. « Tu nous manquez » et « vous nous manques » mélangent deux personnes, et « Chers maman » garde le pluriel de « parents ».`

## 4. Majeurs

### M-1 — fuites par l'énoncé dans les réécritures découpées (m016, m017, m020)
Correctif uniforme : dans l'énoncé de chaque question, la forme qui est la clé de la question jumelle est remplacée par « … ».

| Question | Nouveau fragment cité (le reste de l'énoncé est inchangé) |
| --- | --- |
| 05 m016 q1 | `Quelle forme complète « Claudine ___ du temps pour se rétablir … » ?`. Options : a `met` (clé) · b `mets` (`fr.accord.verbe-non-accorde-au-sujet`) · c `a mis` · d `mettre` (longueurs 3/4/5/6). Explication : `Au présent, avec « Claudine » (elle), « mettre » donne met, sans s : comme il met. « Mets » est la forme de je et tu, « a mis » garde le passé composé de la phrase de départ et « mettre » est l'infinitif.` |
| 05 m016 q3 | `Quelle forme complète « Demain matin, je ___ mon courage à deux mains … » ?` |
| 05 m016 q4 | `On la commence par « Demain matin, … mon courage à deux mains et ___ le chat. » Quelle forme de « aborder » faut-il ?`. Options : a `j'ai abordé` · b `j'aborde` · c `j'aborderais` · d `j'aborderai` (clé), étiquettes inchangées (11/8/12/11). |
| 05 m017 q3 / q4 | `« Nous ___ et nous … un coup d'œil par la fenêtre. »` / `« Nous … et nous ___ un coup d'œil par la fenêtre. »` |
| 05 m017 q5 / q6 | `« Quand nous ___ de l'école, nous … de faire nos devoirs. »` / `« Quand nous … de l'école, nous nous ___ de faire nos devoirs. »` |
| 05 m017 q7 / q8 | `« Vous ___ vos amis d'un œil sévère et vous … à leur parler. »` / `« Vous … vos amis d'un œil sévère et vous vous ___ à leur parler. »` |
| 06 m020 q4 / q5 | `« Les enfants ___ des cadeaux et … chez le petit aveugle. »` / `« Les enfants … des cadeaux et ___ chez le petit aveugle. »` |
| 06 m020 q10 | `Avec « nous » : « Nous … très bien. Nous ___ une surprise. »` |
| 06 m020 q11 | `Avec « Hier soir » : « Hier soir, Sylvie … un rapide souper. Ensuite, elle ___ rejoindre François devant le petit écran. »` |

Les explications de ces questions ne citent que leur propre forme : c'est vérifié, sauf pour m016 q1, qui est réécrite ci-dessus.

### M-2 — 06 m021 q2 (*longue*) : règle donnée, puis application directe
L'énoncé donne « long devient longue ». Sans ce rappel, la règle du cours (+e) mène au distracteur « longe ». En plus, q1 affiche « longue ».
- Dans q1, remplacer « une longue attente » par `une … attente`.
- Réécrire q2 :
  - prompt : `(Concours 2025) Grammaire 2. Phrase officielle : « Après un long moment, une tête à la chevelure hérissée apparait. » Dans la réécriture, « un long moment » devient « une longue attente ». Pourquoi l'adjectif « long » change-t-il ?`
  - options : a `parce que le nom « attente » est féminin` (clé) · b `parce que le nom « attente » est au pluriel` · c `parce que l'adjectif est placé avant le nom` · d `parce que le verbe « apparait » a changé`. Longueurs 40/43/43/40.
  - explication : `L'adjectif prend le genre et le nombre du nom qu'il accompagne : « moment » est masculin, « attente » est féminin singulier, donc « long » passe au féminin. « Attente » n'est pas au pluriel, la place de l'adjectif ne change rien à l'accord, et le verbe n'accorde pas l'adjectif.`

### M-3 — 05 m018 (lecture 2024) : sentiments sans données, fuites, deuxième différence défendable
- **q1** : l'extrait ne montre que la richesse des pères, alors que l'option « leur religion » est une clé. De plus, l'option e « le temps depuis lequel Virginia vit sur l'île » se défend : il est né sur l'île, elle est venue s'y installer.
  - Extrait : `Le narrateur écrit : « Son père possédait le plus grand bateau de pêche de la région. Le mien n'était qu'un simple pêcheur. Elle était chrétienne. Moi, j'étais musulman. »` (verbatim PDF).
  - Option e : `l'école où ils vont`.
- **q2 à q5** : q2 et q4 n'ont aucune donnée du texte, et q3 et q5 annoncent le sentiment. On fusionne chaque sentiment et son indice en un QCM 2×2, sur le modèle de R2 « justifie ». Ordre final : q1, puis s1, s2, *strident*, *effrayer*, *tortueuse*, *grimpe*, causes, soit 8 questions.
  - **s1 (ancienne q2)** :
    - prompt : `(Concours 2024) Lecture : « Une fin tragique ». Compréhension 2. Consigne officielle : « Quels sentiments éprouvent les deux enfants lors de la rencontre avec le phoque ? Justifie à chaque fois ta réponse par un indice du texte. » Extrait : « Un jour, alors que nous nous baignions, nous avons vu une masse noire nager tout près de nous. Le cri strident que nous avons poussé a dû l'effrayer. » Quel est le premier sentiment des enfants, et quel indice le prouve ?`
    - options : a `la peur — « Le cri strident que nous avons poussé »` (clé) · b `la joie — « Le cri strident que nous avons poussé »` · c `la peur — « alors que nous nous baignions »` (`fr.lecture.deduction-sans-indice`) · d `la joie — « alors que nous nous baignions »` (muette). Longueurs 51/51/43/43.
    - explication : `Pousser un cri strident devant une masse noire inconnue, c'est avoir peur : le cri est l'indice. Se baigner ne dit rien de ce que ressentent les enfants, et rien dans l'extrait ne montre de la joie.`
  - **s2 (ancienne q4)** :
    - prompt : `(Concours 2024) Lecture : « Une fin tragique ». Compréhension 2. Extrait : « La bête avait de longues moustaches […] mais nous étions tellement fascinés par cette présence insolite que nous ne songions plus à nous enfuir. » Quel est le second sentiment des enfants, et quel indice le prouve ?`
    - options : a `la fascination — « nous étions tellement fascinés »` (clé) · b `l'envie de fuir — « nous étions tellement fascinés »` (`fr.lecture.contraire-du-texte`) · c `la fascination — « La bête avait de longues moustaches »` (`fr.lecture.deduction-sans-indice`) · d `l'envie de fuir — « La bête avait de longues moustaches »` (muette). Longueurs 51/52/56/57.
    - explication : `Les enfants sont « tellement fascinés » qu'ils ne pensent plus à s'enfuir : c'est la fascination, et ces mots la prouvent. Les moustaches décrivent l'animal, pas ce que ressentent les enfants, et le texte dit le contraire d'une envie de fuir.`
    - La coupure « […] » retire « La peur nous broyait… », qui aurait livré s1.
  - **Supprimer les anciennes q3 et q5.**
  - **Ajouter *effrayer*** (le quatrième mot de 3 a) :
    - prompt : `(Concours 2024) Lecture : « Une fin tragique ». Compréhension 3 a. Consigne officielle : « Remplace chaque mot souligné par un mot ou une expression de même sens. » Phrase : « Le cri strident que nous avons poussé a dû effrayer le phoque. » Quel mot a le même sens que « effrayer » ?`
    - options : a `terrifier` (clé) · b `rassurer` (`fr.lexique.contraire-pour-synonyme`) · c `effrayant` · d `attirer`. Longueurs 9/8/9/7.
    - explication : `Effrayer, c'est faire très peur : « terrifier » a le même sens. « Rassurer » dit le contraire, « effrayant » est un adjectif et non un verbe, et « attirer » n'a pas ce sens.`
- **q8 (*grimpe*)** : la clé est le seul mot simple, et l'explication cite « marche » et « roule », qui ne sont pas des options.
  - Options : a `descend` (clé) · b `monte` (`fr.lexique.contraire-pour-synonyme`) · c `s'avance` · d `tourne`. Longueurs 7/5/8/6.
  - Explication : `« Grimper » veut dire monter : son contraire est « descendre ». « Monte » est un synonyme ; « s'avance » et « tourne » disent une autre façon de bouger, pas le sens opposé.`
- **q4**, si on la garde telle quelle : l'explication parle de « jalousie, honte » au lieu des options. La fusion ci-dessus la remplace.

### M-4 — 05 m015 q2 (« Pablo nous rejoint là-bas ») : F1 (doute n° 2)
**Ce n'est pas acceptable comme support** : la question porte précisément sur *nous*. Les distracteurs a et d se distinguent de la clé seulement parce qu'ils suppriment le pronom complément. C'est cibler le pronom complément, ce que F1 et R10 interdisent. **Supprimer q2.** La première partie de la même consigne de 2026 reste couverte par q1.

### M-5 — 06 m023 q6/q7/q8 (verbes introducteurs livrés par la situation)
- q6, option d `remercie` → `supplie` (`fr.dialogue.verbe-introducteur-inadapte`). Ainsi, les deux verbes de la situation sont présents dans les options de q6 comme de q7, et recopier le mot de la situation ne suffit plus. Explication : `La réplique est un ordre : le verbe « ordonne » dit comment le gardien parle. « Demande » annonce une question, « murmure » une parole à voix basse, et « supplie » convient aux enfants qui demandent une faveur, pas au gardien furieux.`
- q8, deux répliques changent : d `« Que faites-vous ici ? Partez immédiatement ! » crie le gardien.` · a `« Nous voudrions seulement passer la nuit ici », répondent les enfants.` Explication : `Le gardien parle d'abord et demande aux enfants ce qu'ils font là. Les enfants lui répondent qu'ils voudraient rester. Le gardien refuse en donnant sa raison, puis Xavier conclut en acceptant de partir. Chaque réplique répond à la précédente.`

### M-6 — 06 m024 (devoir) : doublons et « ne pas redemander »
- **q5** reprend les phrases de q2.
  - Prompt : `Un élève a écrit ces phrases. Quels mots sont fautifs ? Phrase 1 : « Le chat et noir. » Phrase 2 : « Les fleurs est belles. » Phrase 3 : « La route est longue. » Phrase 4 : « Ta tante est fatigué. »`
  - Options : a `« et » dans la phrase 1` · b `« est » dans la phrase 2` · c `« longue » dans la phrase 3` · d `« fatigué » dans la phrase 4` · e `« belles » dans la phrase 2`. Clé a, b, d.
  - Explication : `Phrase 1 : on peut dire « le chat sera noir », c'est le verbe être : « est ». Phrase 2 : « les fleurs » est au pluriel, le verbe être devient « sont ». Phrase 4 : « ta tante » est féminin, l'adjectif prend un e : « fatiguée ». « Longue » est juste avec « la route », et « belles » est juste avec « les fleurs ».`
  - Contrôle salle blanche : 0.
- **q4** (« Les élèves ___ en classe et ___ maître… ») redemande 03/01-pratique#5, qui figure sur la liste « ne pas redemander » (« Les élèves ___ en classe et Cédric met ___ cartable »). Elle double aussi q3, avec la même clé « sont – son ». Je la remplace par le geste de la carte, la correction :
  - prompt : `Un élève a écrit : « Les joueurs son prêts et Karim attache sont soulier. » Quelle correction est juste ?`
  - options : a `Les joueurs sont prêts et Karim attache son soulier.` (clé) · b `Les joueurs son prêts et Karim attache son soulier.` (`fr.homophone.son-sont-confondus`) · c `Les joueurs sont prêts et Karim attache sont soulier.` (`fr.homophone.son-sont-confondus`) · d `Les joueurs son prêts et Karim attache sont soulier.` (muette). Longueurs 52/51/53/52. Contrôle salle blanche : 0.
  - explication : `« Les joueurs » est le sujet du verbe être : on peut dire « étaient prêts », donc « sont ». Devant le nom « soulier », on peut dire « mon soulier » : c'est le déterminant « son ».`

### M-7 — 06 m022 q1 : les distracteurs livrent la clé de q2
- c → `les moqueries de son amie Danielle` (`fr.lecture.contraire-du-texte`)
- d → `l'opération, qui dura plusieurs heures`
- Longueurs 34/21/34/38.
- Explication : `Avant l'opération, ce que Claudine trouvait le plus difficile n'était pas son handicap : c'était la réaction des gens. Le texte écarte justement le handicap lui-même ; son amie Danielle l'aide au lieu de se moquer, et l'opération n'est pas ce qu'elle décrit comme difficile.`

### M-8 — 05 m015 q3, q6, q7 (2024, 2010, 2008)
- **q3** : l'énoncé nomme le groupe à supprimer, et la clé est la seule option sans « Sans prévenir ». Elle s'élimine à vue.
  - Prompt : `(Concours 2024) Grammaire 1. Consigne officielle : « Réécris cette phrase en supprimant les compléments non essentiels. » Phrase : « Sans prévenir, le phoque a plongé dans l'eau sombre des profondeurs. » Quel groupe de cette phrase est un complément non essentiel ?`
  - Options : a `Sans prévenir` (clé) · b `le phoque` · c `a plongé` · d `le phoque a plongé`. Longueurs 13/9/8/18.
  - Explication : `« Sans prévenir » peut être supprimé ou déplacé (le phoque a plongé, sans prévenir, …) : la phrase garde son sens, c'est un complément non essentiel. « Le phoque » est le sujet, « a plongé » le verbe : sans eux, il n'y a plus de phrase.`
  - « dans l'eau… » est écarté, comme le demande la carte.
- **q6** répète q5 sur la même phrase (ajout de l'auteur ; l'item officiel de 2010 ne demande que « relève »). **Supprimer q6.**
- **q7**, explication : retirer la phrase `« A la récréation » est un complément non essentiel, il n'entre pas dans le groupe verbal.`, qui livre la clé de q8.
- Avec M-4, la mission passe de 8 à 6 questions : q1, q3, q4, q5, q7, q8.

### M-9 — explications qui désignent les options par leur rang, ou citent des options absentes
- **05 m019 q8** : `La bonne réplique donne une raison (un oiseau est fait pour voler) et s'écrit avec deux-points et guillemets. La réplique sans aucun signe oublie la ponctuation du dialogue ; celle qui parle du dîner sort du sujet, et celle qui demande la cage ne pousse pas Amine à libérer l'oiseau.`
- **06 m020 q3** : remplacer la dernière phrase par `« Fairera » traite « faire » comme un verbe régulier, « envahissera » part du radical du présent (envahiss-) et reste au singulier, et la phrase « a fait … ont envahi » garde le passé composé.`
- **06 m020 q9** (l'explication cite « vont », qui n'est pas une option) : `Avec « nous », « aller » prend la forme allons. « Vais » garde la forme de je, « allez » est celle de vous et « allerons » est un futur mal formé.`
- **06 m020 q11** (l'explication cite « va », qui n'est pas une option, et omet « est allées ») : `« Hier soir » demande le passé composé de « aller », avec l'auxiliaire « être » : est. Le participe s'accorde avec le sujet « elle », féminin singulier : allée. « Est allé » oublie l'accord, « est allées » ajoute un s alors que le sujet est au singulier, et « a allé » emploie « avoir ».`
- **06 m022 q6** (l'explication cite des options absentes) : `« Confinée » veut dire enfermée, retenue dans un lieu : Claudine reste dans son lit. « Délivrée » dit le contraire, « tourmentée » dit une souffrance et « abandonnée » n'a pas ce sens.`
- **06 m022 q9** : `La bonne réponse se place dans la situation de Claudine et réagit positivement, avec calme et fierté. « Il faut toujours être gentil… » reste général, ne plus parler à personne est une fuite, et crier sur les gens est une réaction de colère, qui n'est pas positive.`
- **06 m023 q2** : `Pour écrire une parole, on ouvre avec deux-points et guillemets, puis la réplique commence par une majuscule et garde sa ponctuation avant le guillemet fermant. Les trois autres versions oublient les guillemets, les deux-points ou la majuscule de « Claudine ».`
- **06 m023 q5** : `Une bonne description montre l'aspect (grand et sec), un geste (froncer les sourcils) et la voix (rauque). Une liste de parties du corps ne fait pas le portrait de quelqu'un, et les phrases sur l'ordre du gardien et la prière des enfants racontent ce que font les personnages.`

### M-10 — multi « que doit contenir ton récit » : des distracteurs qui s'éliminent à vue
- **05 m019 q6** : remplacer d, e, f (« liste de courses », « poème en vers », « lettre ») par d `un titre souligné` · e `exactement huit phrases, pas une de plus` · f `le portrait d'un arbre`. Clé a, b, c. Explication : `La consigne demande un récit d'au moins huit phrases, avec un dialogue et une description. « Au moins huit » permet d'en écrire davantage : « exactement huit » ne respecte pas la consigne, et ni un titre ni le portrait d'un arbre ne sont demandés.`
- **06 m023 q4** : e `un poème sur la guérison` → `exactement huit phrases, pas une de plus`. Explication : `La consigne demande au moins huit phrases, la réaction des camarades et un court dialogue. « Exactement huit » ne respecte pas « au moins huit », et décrire le médecin n'est pas demandé.`

## 5. Mineurs

- m-1 — Gabarit « a pris » répété : 05 m016 q5, q6 et q7 ont les mêmes distracteurs (« prit », « prendu »), et q7 reprend presque mot pour mot les options de 05/01-pratique#2, qui figure sur la liste « ne pas redemander ». Les phrases officielles sont différentes, donc j'accepte. Pour varier, on peut remplacer en q7 `ont prendu` par `sont pris` (`fr.conj.auxiliaire-mal-choisi`).
- m-2 — 06 m020 : « iront » est clé trois fois (q5, q6, q8), comme le demande la carte. J'accepte.
- m-3 — 06 m024 q3 : l'énoncé dit « Quelle correction est juste ? » pour un texte à trous. Remplacer par `Quelle réponse complète les deux blancs ?`.
- m-4 — 06 m022 q8 : l'étiquette `contraire-pour-synonyme` sur « souffrir » est approximative, puisque ce n'est pas un synonyme de « maltraiter ». Elle peut être rendue muette.
- m-5 — Fidélité : le « : » final des consignes officielles est remplacé par « . », et la coquille « vague . » (2026) est gommée. Sans incidence.
- m-6 — 05 m019 q5 (« Le sable est couvert de sacs, de bouteilles et de boîtes ») est très proche de l'exemple du cours 05. On peut écrire `L'eau est grise et des sacs flottent près des rochers.`

**Gabarits inter-chapitres** (tranche) : « même sens que », « quelle phrase du texte le prouve » et « que doit contenir ton récit » sont des cadres parallèles sur d'autres textes ; j'accepte. Le groupe « le prouve » disparaît avec M-3.

**Doute n° 2 (F1)** : voir M-4. Ce n'est pas acceptable, puisque l'item cible le pronom complément. Les autres pronoms (« l'installe », « Libère-le », « lui ») ne sont que du support : j'accepte.

## 6. Verdict

**À corriger.** Aucune clé fausse. Restent :
- 1 critique : C-1, une double réponse (vouvoiement) ;
- 10 majeurs. Les principaux : les fuites entre questions jumelles (M-1 à M-3, M-5 à M-8), l'item F1 (M-4), le doublon du devoir (M-6) et les explications qui désignent les options par leur rang (M-9) ;
- 6 mineurs.

Tous les correctifs sont des réécritures locales. Les missions changent de taille : m015 passe de 8 à 6 questions et m018 de 9 à 8, soit 82 questions au lieu de 85. Une re-vérification ciblée suffira.
