# Audit M2 — missions du gisement, french-6eme chapitres 03 et 04

> Auditeur indépendant (opus), 2026-10-19. Grille : `prompt-auditeur.md`, plus les contrôles du gisement (fidélité, conversion, salle blanche, « ne pas redemander », short_answer, rendu). Autorités : `assign-M2.md`, `PLAN-gisement.md` (R1–R10, E1–E8), transcriptions `examens-nationaux/6eme-base/french/<année>-unique.md`.
> Fichiers audités, 38 questions, toutes re-résolues à l'aveugle avant lecture du rapport de l'auteur :
> `03/exercices/06-exams-2010-2023-epithete-attribut-et-etre` (m009, 5 q), `07-exams-2016-2017-recit-faire-accepter` (m010, 7 q), `08-devoir-lire-ordre-titre-portrait` (m011, 8 q) ; `04/exercices/06-exams-2018-2024-phrase-negative` (m012, 5 q), `07-exams-2020-2025-verbes-comme-finir` (m013, 6 q), `08-exams-2015-2021-recit-entraide` (m014, 7 q).
> Rien n'a été écrit sous `content/`, aucune écriture git.

## 0. Contrôles

| Contrôle | Résultat |
| --- | --- |
| `content:check` (corpus réel) | ✓ `french-6eme` : 8 chapitres, 73 exercices, 504 questions |
| `content:qa -- --subject french-6eme` | ✓ 0 erreur |
| `content:tranche --chapters 03…,04… --fresh --strict-longest` | ✓ clé strictement la plus longue 0/72 ; positions 24/29/22/25 % ; paires proches 0 ; gabarits 0 |
| `content:gisement:controle` sur m011 | ✓ 0 plage ≥ 8 mots, 0 plage ≥ 6 mots, 0 exercice source dont on reprend trois données |
| Rendu | ✓ 0 `_` ni `*` résiduel dans les prompts, options et explications (hors blancs `___`) |
| Short_answer : la réponse est-elle dans l'explication ? | ✓ aucune (m013 q2, q5) |
| Fidélité au texte officiel | ✓ phrases d'examen reprises mot pour mot (coquilles de 2010 gardées) ; situations de 2015, 2016, 2017, 2019 et 2021 fidèles ; sessions citées. Écarts mineurs en § 3 |
| `sources[]` | ✓ ligne des examens dans les deux `chapter.json`, ligne « devoirs publics » au 03 |

## 1. Critiques (deux réponses défendables)

**C-1 — m012 q1 (2024, « La peur nous broie toujours les entrailles »).** Sans contexte, *toujours* peut vouloir dire « encore ». L'option c « ne nous broie **plus** » se défend donc. L'option d « ne nous broie **jamais plus** » est même du français correct (« plus jamais »).
- c → `{ "id": "c", "text": "La peur ne nous broie toujours les entrailles.", "misconceptionTag": "fr.phrase.negation-sens-inexact" }` (elle garde l'adverbe d'origine, c'est le piège de la ligne C03#7)
- d → `{ "id": "d", "text": "La peur ne jamais nous broie les entrailles.", "misconceptionTag": "fr.phrase.negation-mal-placee" }`
- `explanation` → `« Toujours » devient « ne… jamais » : ne se place devant le verbe (avant « nous »), jamais juste après le verbe. Sans ne, la négation écrite est incomplète ; garder « toujours » ne nie pas le sens ; jamais ne passe pas devant le verbe.`
- Longueurs : 41 · clé 44 · 46 · 44. Une seule réponse juste.

**C-2 — m012 q5 (2019, « Veux-tu du pain ? »).** « Non, je ne veux **plus** de pain. » est une réponse négative juste. Elle est même naturelle si l'on vient d'en prendre. L'étiquette `negation-sens-inexact` ne décrit pas ce cas : rien ne demande ici de nier *encore* ou *toujours*.
- c → `{ "id": "c", "text": "Non, je ne pas veux de pain.", "misconceptionTag": "fr.phrase.negation-mal-placee" }`
- d → `{ "id": "d", "text": "Non, je ne veux de pain." }` (« pas » oublié ; aucun libellé exact, muette)
- `explanation` → `Pour répondre non, on emploie « ne… pas » autour du verbe : ne devant veux, pas juste après. Sans ne ou sans pas, la négation écrite est incomplète, et pas ne passe jamais devant le verbe.`
- Longueurs : 25 · clé 28 · 28 · 24. Il y a égalité, la clé n'est donc pas strictement la plus longue. Une seule réponse juste. La précision « l'article est « de » » reste vraie pour les quatre options.

## 2. Majeurs

**M-1 — Explications qui désignent les options par leur rang, alors qu'elles sont mélangées.**
- m011 q7 : le rang cité est **faux**. La « première phrase » désignée n'est pas la clé, qui est en c. `explanation` → `Dans « Elle lui a prêté son ballon rouge », « rouge » est collé au nom « ballon » et dit comment il est : c'est un adjectif. Dans « Le rouge est sa couleur préférée » et « Un peu de rouge monte à ses joues », « rouge » est un nom, précédé d'un déterminant. Dans « Nour a rougi de plaisir », « rougi » est une forme du verbe rougir.`
- m010 q7 : `La phrase de fin dit comment la situation a changé à la suite de la démarche : l'enfant joue avec le groupe et est devenu un ami. « Il vit seul dans l'immeuble… » décrit la situation de départ ; le jeu de cartes rangé et le livreur ne parlent pas de l'intégration.`
- m014 q2 : `La complication est l'événement qui change tout : la visite du propriétaire. « Claire s'habitue au chat… » décrit le calme du début, l'explication de Claire est la suite des événements, et le départ du propriétaire avec le chat serait une fin.`
- m014 q5 (multi) : `Trois répliques donnent des raisons d'aider : le devoir d'entraide (« il faut le faire »), la réciprocité (« nous aurons besoin d'aide ») et le bien fait au vieux monsieur. « Il ne faut pas parler aux inconnus » et « Un goûter, ça se mange tout seul » soutiennent le point de vue de la mère.`
- m014 q7 : `La phrase de fin dit ce que la famille fait pour l'enfant après sa décision : elle lui apporte des provisions chaque semaine. « Le petit aveugle vit seul… » décrit la situation de départ ; le départ de François pour l'école et la soirée devant la télévision ne parlent pas de l'aide.`

**M-2 — m011 q2, q3, q4 : il faut lire le texte pour répondre, mais il n'est que dans q1.** Le donjon tire les questions au hasard : sans q1, l'élève n'a pas le texte. Ajouter en tête des trois prompts le texte de q1, tel quel :
`Lis le texte : « Aujourd'hui, Karim rit et joue avec toute sa classe. Il y a une semaine pourtant, il est arrivé seul dans la cour. Karim est un petit garçon timide, avec des lunettes rondes. Personne ne lui a parlé pendant la récréation. Alors Nour, une fille curieuse et joyeuse, s'est assise près de lui. Elle lui a prêté son ballon rouge. Depuis ce jour, Karim n'est plus seul. » ` puis le prompt actuel. Les clés ne changent pas. Les questions q5 à q8 citent leur phrase : elles se lisent seules.

**M-3 — m013 : deux short_answer dont la réponse est affichée dans une question voisine.** q1 affiche « a saisi », réponse de q2. q4 affiche « grandira », réponse de q5. La route suit `displayOrder` et le donjon tire au hasard : dans les deux cas, la réponse peut avoir été vue. Toutes les formes du 2ᵉ groupe de ces phrases officielles sont déjà dans les options des QCM : une short_answer ne peut rien y ajouter. **Supprimer q2 et q5.** La mission garde alors 4 questions (2025, 2021, 2020, 2022), une par session. Le fichier n'est pas publié, on peut donc retirer ces questions.

**M-4 — m014 q3 répète en fait `03/02-boss` q2.** Même tâche, mêmes quatre options (répond, affirme, ajoute, demande), même clé *demande*. Remplacement :
- prompt → `(Concours 2021) Dans le dialogue entre Claire et le propriétaire, le propriétaire retrouve son chat : « Mon chat ! Te voilà enfin ! ___ le propriétaire. » Quel verbe introducteur convient ?`
- options → a `demande` (`fr.dialogue.verbe-introducteur-inadapte`), b `répond` (idem), c `interroge` (idem), d `s'écrie` (clé, `correctOption: "d"`)
- `explanation` → `La réplique est une exclamation de joie : le verbe introducteur qui lui convient est « s'écrie ». « Demande » et « interroge » annoncent une question, et « répond » suit une question qu'on vient de poser.`
- Longueurs : 7 · 6 · 9 · clé 7. Le verbe est enseigné au cours 03 (« crier ou s'écrier pour un appel », l.200). Une seule réponse juste.

**M-5 — m010 q1 : les distracteurs s'éliminent d'un coup d'œil (doute 3).** Le match à la télévision, la cantine et le tableau n'ont aucun rapport avec la situation. Il faut des répliques plausibles qui ne mènent pas à l'acceptation, ce qui est le piège de la ligne C10#9 :
- a → `{ "id": "a", "text": "« Tu as raison, elle est bizarre : on ne va pas jouer avec elle. »" }`
- b → `{ "id": "b", "text": "« Caroline, viens vite avec nous : on le laisse tout seul dans son coin. »" }`
- d → `{ "id": "d", "text": "« Toi, avec ta bouche rouge, tu n'as rien à dire ! »" }`
- Les trois sont muettes : `fr.production.hors-sujet` ne les décrit plus, et aucun libellé ne dit « ne mène pas à l'acceptation ».
- `explanation` → `La consigne demande d'amener l'élève à accepter et à respecter Caroline : la réplique doit parler d'elle et de son droit d'être respectée. Lui donner raison, l'éviter ou se moquer de lui à son tour ne l'amène pas à accepter sa nouvelle camarade.`
- Longueurs : 66 · 74 · clé 70 · 52. Une seule réponse juste.

**M-6 — m009 q2 : l'explication ne dit pas clairement le temps.** Elle affirme que « le temps de l'auxiliaire sert à nommer », ce qui pousse vers « présent », puis elle se contredit. C'est en outre une question de l'auteur : son étiquette de session doit le dire (§ 3).
- `explanation` → `« J'ai été » est formé de l'auxiliaire avoir au présent (ai) et du participe passé de être (été) : auxiliaire au présent + participe passé, c'est le passé composé. Le présent de être serait « je suis ».`

## 3. Mineurs

1. **m009 q2 et m012 q3 sont des variantes de l'auteur, pas des items officiels (doute 1).** Elles sont acceptables, à condition de le signaler. Remplacer « (Concours 2023) » par `(D'après le concours 2023)`, et « (Concours 2021, avec « encore ») » par `(D'après le concours 2021, avec « encore »)`.
2. **m009 q3 : la consigne n'est pas reprise mot pour mot.** Remplacer « Consigne : remplir le tableau. » par `Consigne : « Lis la phrase et remplis le tableau suivant. »`.
3. **Consignes officielles de rédaction absentes (R3).** Ajouter la consigne une fois par session, à la fin de la situation :
   - m014 q1 : `Consigne : « Ecris un récit de huit phrases au moins pour raconter ce que fait Claire pour le chat et imagine le dialogue entre la fillette et le propriétaire. »`
   - m014 q4 : `Consigne : « Rédige un récit de huit phrases au moins pour raconter ce qui s'est passé en intégrant un dialogue. »`
   - m014 q6 : `Consigne : « Rédige un récit de huit phrases au moins pour raconter ce qui s'est passé. (Ton récit doit intégrer un court dialogue.) »`
   - m010 q5 : `Consigne : « Raconte, en huit phrases au moins, ce qui s'est passé en intégrant un dialogue dans ton récit. »`
4. **m013 q6, option d « Une grande joie m'a envahi » : elle touche l'accord avec un COD placé avant (F5),** car avec « je » au féminin il faudrait « envahie ». → `{ "id": "d", "text": "Demain, je serai sur scène. Une grande joie m'envahit.", "misconceptionTag": "fr.temps.indicateur-de-temps-ignore" }`. Longueurs 53 · clé 55 · 58 · 54.
5. **m011 q8 : l'explication déforme le texte (« de grandes lunettes »).** → `La phrase de portrait dit comment est Karim : petit, timide, avec des lunettes rondes. Les autres phrases racontent des actions : personne ne lui parle, on lui prête un ballon, il arrive dans la cour.`
6. **m009 compte 5 questions au lieu des 8 de la carte,** car C11#8 est écarté (E7). Le choix est justifié et déclaré, sans constat.

## 4. Réponses aux doutes de l'auteur

1. **Variantes « d'après » (m009 q2, m012 q3) : acceptables.** Chacune a une seule réponse juste, et m012 q3 est prévue par la carte (2 q pour 2021). Mais l'énoncé doit les dire « D'après le concours … » (mineur 1) et l'explication de m009 q2 doit être réécrite (M-6).
2. **« plus » comme distracteur en m012 q2 (2021) : acceptable.** La précision « Ici, « toujours » veut dire « à chaque fois » » lève l'ambiguïté, et le texte officiel la confirme : le chat est sur son banc chaque jour. En revanche, le même problème existait **sans** précision en q1 (2024) et en q5 (2019) : ce sont C-1 et C-2.
3. **Répliques hors sujet de m010 : oui, elles s'éliminent trop vite.** Remplacées en M-5. m010 q7 et m014 q7 gardent des phrases de fin hors sujet, mais leur distracteur principal (la situation de départ) est réel : on peut les tolérer.
4. **Distracteurs muets du devoir : justes.** Aucun libellé `fr.*` ne nomme la confusion de nature (nom, verbe ou nom propre à la place d'un adjectif), et la règle veut une étiquette exacte ou aucune. q3 porte `detail-pour-idee-principale` et q8 `description-narration-confondues`, à bon droit.

## 5. Ce qui a été vérifié en plus

- **Conversion des questions ouvertes en questions fermées :** conforme à R1, R3 et R6. Les réécritures sont devenues des QCM de formes, le tableau de 2020 un matching, les rédactions des préparations fermées (ordering des cinq temps, multi des éléments exigés, première réplique, phrase de fin). Aucune rédaction n'est demandée.
- **« Ne pas redemander » :** les listes de la carte sont respectées, sauf M-4 (doublon hors liste).
- **Sujets sensibles (E8) :** handicap, mutisme, pauvreté. Le ton reste sobre et rien n'est ajouté.
- **Placements :** conformes à F4 et R5.

## 6. Verdict

**À corriger** : 2 critiques et 6 majeurs, chacun avec son texte de remplacement vérifié (une seule réponse, la clé jamais strictement la plus longue), plus 6 mineurs. Les gates sont verts, le contrôle de salle blanche est à 0 et la fidélité aux transcriptions est bonne. Après correction, relancer `content:check`, `content:qa` et `content:tranche --fresh --strict-longest`.
