# Audit B2 — french-6eme, `03-accepter-les-autres` et `04-sentraider-pour-reussir`

> Auditeur indépendant (opus), 2026-10-19. Branche `wip/francais-6eme-un-passage` (worktree `wt-fr6b`), état des fichiers au 08:49.
> Grilles appliquées : skill `content-audit`, grille français 9ᵉ (`prompt-francais-auditeur.md`), `course-quality.md`.
> Autorité : fiche `programme/6eme-base/francais.md` (§ 2.3, § 2.4, § 2.10), PLAN F1–F7, PDF 121615 (cahier) et 121614 (manuel) relus aux pages reprises.
> Méthode : les 70 questions ont été re-résolues à l'aveugle (quiz + 5 exercices × 2 chapitres) avant toute lecture du rapport et des notes de l'auteur. Rien n'a été modifié dans `content/`, aucune écriture git.

## 0. Gates et rendu

| Contrôle | Résultat |
| --- | --- |
| `content:check` (global, `eng-deliver`) | ✓ `french-6eme: 8 chapters, 40 exercises, 240 questions` ; 121 matières validées |
| `content:qa -- --subject french-6eme` | ✓ aucune clé suspecte, 0 erreur |
| `content:tranche … --chapters 03…,04… --fresh --strict-longest` | ✓ clé strictement la plus longue 0/46 ; positions a 26 % · b 26 % · c 22 % · d 26 % ; paires proches 0 ; gabarits 0 ; patron de notion 0 en recul |
| Rendu `renderLesson` / `renderSummary` (vitest jetable) | ⚠️ **un défaut** : cours 04 l.31 (voir M-6). Le reste est propre : 6 sections par cours, tableaux, blocs `exemple` / `piege` / `verifie`, citations du dialogue |
| Chromium 360 px | pas de débordement de page avec le CSS du moteur (`.lesson-table` est en `display:block; overflow-x:auto`) ; le tableau être/avoir à 5 colonnes (367 px) défile dans son cadre, comme prévu |

Fichiers jetables (test vitest, captures) supprimés du moteur ; les captures restent dans le scratchpad de l'auditeur.

## 1. Re-résolution — synthèse

70 questions re-résolues. Toutes les clés sont justes. Deux questions ont **une deuxième réponse défendable** (C-1, C-2). Les explications nomment la bonne option, sauf deux qui désignent les options par leur rang (M-2, M-9).

| Chapitre | Questions | Critiques | Majeurs | Mineurs |
| --- | --- | --- | --- | --- |
| 03-accepter-les-autres | 35 | 0 | 6 | 9 |
| 04-sentraider-pour-reussir | 35 | 2 | 6 | 8 |

## 2. Critiques (deux réponses défendables)

### C-1 — `04/exercices/03-revision.json` q6 (short_answer)

Le prompt est « Complète la phrase négative avec le mot qui convient : « Hier encore, il courait ; aujourd'hui, il ne court ___. » ». Or **« pas »** donne une phrase juste et sensée (« aujourd'hui, il ne court pas »). Un élève qui tape « pas » est refusé.

Remplacement du `prompt` :

> Complète avec « plus » ou « jamais » : « Hier encore, il courait ; aujourd'hui, il ne court ___. »

Remplacement de l'`explanation` :

> Hier encore, il courait : c'était vrai avant et ça ne l'est plus aujourd'hui. C'est « ne… plus » qui dit ce changement. « Jamais » voudrait dire qu'il n'a couru à aucun moment, ce que « hier encore » contredit.

Clé `plus` inchangée. `jamais` reste unique erreur attendue. Vérifié : une seule réponse.

### C-2 — `04/exercices/04-defi.json` q3

Prompt : « Quelle phrase dit le contraire de « J'ai toujours fini mes devoirs avant le dîner. » ? ». L'option c « Je n'ai pas toujours fini mes devoirs avant le dîner. » **contredit** la phrase : c'est même sa négation logique. Un élève (ou un parent) peut la défendre. L'explanation doit d'ailleurs argumenter contre elle. De plus, *ne… pas toujours* n'est enseigné nulle part.

Remplacement de l'option c (étiquetée) :

```json
{ "id": "c", "text": "J'ai jamais fini mes devoirs avant le dîner.", "misconceptionTag": "fr.phrase.ne-oublie" }
```

Remplacement de l'`explanation` :

> Le contraire de « toujours » est « ne… jamais ». À un temps composé, ne se place avant l'auxiliaire et jamais juste après lui : je n'ai jamais fini. « Ne… plus » est le contraire de « encore », et à l'écrit le ne ne disparaît jamais.

Longueurs : a 45 · b 48 · c 44 · clé d 47. La clé n'est pas la plus longue. Une seule réponse juste.

## 3. Majeurs

### Chapitre 03

**M-1 — `03/cours.md` § « Lire pour comprendre », l.218 et l.233 : le cours commet l'erreur qu'il dénonce.** L'ancrage ne dit nulle part que Hutché « reste à l'écart ». Pourtant la question et la réponse modèle l'affirment (« Hutché reste à l'écart parce qu'il boite »). Le piège de la même section dit pourtant : « Une réponse s'appuie sur une phrase du texte ». La réponse modèle est donc une déduction sans indice (`fr.lecture.deduction-sans-indice`).

- l.218 → `Lis ce début de récit : « _Hutché ne court pas comme les autres enfants de la tribu : il boite. Alors il reste à l'écart de leurs jeux. Un soir, son père lui dit : "Ouvre les yeux, le monde est grand."_ »`
- l.233 → `2. Dans le texte : « _il boite. Alors il reste à l'écart_ » ← le mot _alors_ relie la cause (il boite) à ce qu'elle entraîne (il reste à l'écart).`

**M-2 — `03/exercices/04-defi.json` q1 : l'explication désigne les options par leur rang, et ce rang est faux.** « Dans la première phrase, « calme » suit le verbe d'état « reste » ». Même dans l'ordre d'écriture, la première option est « Un lac calme… », une épithète. De plus, les options a et c sont presque identiques : elles exécutent la même erreur sur la même phrase.

- option c → `{ "id": "c", "text": "Le pêcheur regarde le lac calme.", "misconceptionTag": "fr.gn.attribut-epithete-confondus" }` (épithète placée après un verbe d'action : c'est l'erreur « après un verbe donc attribut »)
- `explanation` → `Dans « Le lac reste calme », l'adjectif suit le verbe d'état « reste » : il est attribut du sujet. Dans « Un lac calme brille au soleil » et « Le pêcheur regarde le lac calme », il est collé au nom « lac » : il est épithète, même après un verbe d'action. Dans « Le calme du lac rassure les pêcheurs », « calme » est un nom.`
- Longueurs : a 30 · clé b 19 · c 32 · d 37. Une seule réponse juste (seul « reste » est un verbe d'état).

**M-3 — `03/exercices/04-defi.json` q5 (proverbe « Le soleil luit pour tout le monde ») : la notion est testée sans être enseignée, et un distracteur s'élimine d'un coup d'œil.** Le cours 03 ne parle jamais de proverbe ni de sens figuré d'un proverbe (règle d'or). L'option b « les gens riches reçoivent plus de soleil » contredit « pour tout le monde » : on l'écarte sans rien savoir.

- `03/cours.md`, `::: propriete` de la section « Les mots de la paix », ajouter une puce après la l.290 : `- Un **proverbe** se comprend aussi au sens figuré : _Bien faire et laisser dire_ veut dire qu'il faut faire son devoir sans se soucier des critiques.`
- option b → `{ "id": "b", "text": "il faut bien faire son travail sans écouter les critiques" }` (sens d'un autre proverbe de la même page du manuel, p.54 ; muette)
- Longueurs : a 47 · b 57 · clé c 39 · d 36. Une seule réponse juste : b ne parle ni du soleil ni du partage.

**M-4 — `03/exercices/05-entrainement.json` q1 : l'explication enseigne un accord faux.** « le clown et son partenaire est sur la scène » : avec deux sujets, le verbe se met au pluriel (notion du M5). Le test doit retirer un des deux sujets.

- `explanation` → `Le test avec « est » marche pour les blancs 1, 2, 4 et 6 (où est l'ami, il n'est pas arrivé, le clown est sur la scène, il est allé) : sont. Le test avec « mon » marche pour les blancs 3 et 5 (mon partenaire, mon fils) : son.`

**M-5 — `03/quiz.json` q5 : la forme désigne la clé.** Les trois distracteurs contiennent « en criant », la clé non : c'est l'option qui se distingue. On ne peut pas simplement ajouter « en criant » à la clé, car elle deviendrait la plus longue. On retire donc « en criant » partout :

- a → `{ "id": "a", "text": "Rania répond tiens bon je viens t'aider", "misconceptionTag": "fr.dialogue.ponctuation-oubliee" }`
- c → `{ "id": "c", "text": "Rania répond : tiens bon, je viens t'aider !", "misconceptionTag": "fr.dialogue.ponctuation-oubliee" }`
- d → `{ "id": "d", "text": "Rania répond : « tiens bon, je viens t'aider ! »" }` (seule erreur : la majuscule de la réplique ; muette)
- clé b inchangée. Longueurs : 39 · **48** · 44 · 48 : il y a égalité, la clé n'est donc pas *strictement* la plus longue. Une seule réponse juste. L'explanation actuelle (« la réplique commence par une majuscule ») couvre déjà d.

**M-6 — `03/exercices/02-boss.json` q5 : un distracteur s'élimine d'un coup d'œil.** « se ressembler comme deux gouttes d'eau » ne contient pas *paix* et parle de ressemblance : la question porte sur des expressions qui contiennent *paix*.

- option d → `{ "id": "d", "text": "vivre en paix avec tout le monde", "misconceptionTag": "fr.lexique.mot-voisin-du-meme-champ" }`
- `explanation` → `Faire la paix, c'est se réconcilier après une dispute. Avoir la paix chez soi et lire en paix parlent du calme ; vivre en paix avec tout le monde, c'est ne pas se disputer : le mot « paix » n'a pas le même sens dans ces expressions.`
- Longueurs : 22 · 12 · clé 13 · 32. Le cours enseigne explicitement la distinction « vivre en paix ≠ se réconcilier » (l.296–301). Une seule réponse juste.

### Chapitre 04

**M-7 — `04/cours.md` l.31 : rendu cassé.** `_Je \**n'\**ai **plus** …_` s'affiche « Je \*n'… » : un astérisque littéral reste dans le texte et une italique s'imbrique dans l'autre (sortie `renderLesson` vérifiée).

- l.31 → `3. **J'écris** : _Je **n'**ai **plus** téléphoné à mon frère._ (_ne_ devient _n'_ devant une voyelle, parce que _ai_ commence par _a_.)` (rendu vérifié : `<em>Je <strong>n'</strong>ai <strong>plus</strong> …</em>`)

**M-8 — `04/cours.md` § « Lire pour s'informer » : l'exemple et la vérification portent sur un texte que le cours ne montre pas.** « Je relis cette rubrique ← chaque enfant doit apprendre à lire… » et « Dans quelle rubrique cherches-tu… » : l'élève de l'app n'a pas le manuel sous les yeux. Il faut insérer, après le bloc `::: definition` (l.287), un court documentaire réécrit (R-2) avec sa phrase de liaison :

```markdown
> **L'école pour tous les enfants du monde**
> Apprendre est un droit pour chaque enfant. Pourtant, tous les enfants du monde n'ont pas les mêmes chances. Chaque enfant doit pouvoir apprendre à lire, à écrire et à compter.
>
> **Des objectifs pour demain**
> Les pays du monde ont choisi des buts : apprendre à lire à presque tous les enfants et aider les adultes qui ne savent pas lire.

Chaque intertitre en gras annonce ce que dit sa rubrique : on le lit avant de lire la rubrique.
```

Vérifié : la vérification « mêmes chances » ne trouve sa réponse que dans la 1ʳᵉ rubrique, et l'exemple (« lire, écrire, compter ») aussi. Le texte n'emploie ni *ni… ni* ni subjonctif.

**M-9 — `04/cours.md` : deux pièges que rien n'évalue (doute 1 de l'auteur).** Proverbe lu au sens propre (l.256) et documentaire pris pour un récit (l.298). Voir § 5, réponse 1 : on ajoute les deux distracteurs, et on déclare les deux tags dans `coursePitfalls`.

**M-10 — `04/exercices/04-defi.json` q1 (multi) : l'explication désigne les options par leur rang** (« La deuxième phrase oublie ne ; la quatrième place plus avant le verbe »), alors que les options sont mélangées.

- `explanation` → `Il faut toujours deux mots : ne avant le verbe conjugué, plus ou jamais juste après ; à un temps composé, ils encadrent l'auxiliaire. « Elle oublie jamais ses clés » oublie ne, et « Ils ne plus jouent ensemble » place plus avant le verbe.`

**M-11 — `04/exercices/04-defi.json` q4 : la phrase interrogée n'est pas dans le récit donné.** Le récit saute de « il glisse » à « Le maître nageur soigne », puis la question demande la place d'une phrase absente. L'élève doit d'abord l'insérer lui-même : charge inutile, lecture double.

- `prompt` → `Karim joue au football sur la plage avec ses amis. Soudain, il glisse et se tord la cheville. Ses amis l'aident à s'asseoir et appellent le maître nageur. Le maître nageur soigne la cheville. Le lendemain, Karim remercie ses amis. Dans ce récit, que représente la phrase « Ses amis l'aident à s'asseoir et appellent le maître nageur » ?`
- Clé c inchangée. Options inchangées : « la complication du récit » sert de rembourrage, sinon la clé serait strictement la plus longue (21 · 15 · 23 · 11) ; on le garde. Une seule réponse : la solution est le soin, pas l'appel.

**M-12 — `04/exercices/05-entrainement.json` q5 : étiquettes inexactes et notion non enseignée (doute 3).** « amicalement » est un adverbe en *-ment* : c'est le tableau C (enrichissement non arbitré), absent du cours. « amical » exécute une erreur de nature (adjectif à la place d'un nom), que `mot-voisin-du-meme-champ` ne décrit pas.

- a → `{ "id": "a", "text": "amical" }` (muette)
- b inchangé (`ami` + `fr.lexique.mot-voisin-du-meme-champ` : une personne du thème, pas le sentiment demandé)
- c → `{ "id": "c", "text": "entraide", "misconceptionTag": "fr.lexique.mot-voisin-du-meme-champ" }` (mot du thème qui nomme une action, pas un sentiment qu'on ressent ; commence par une voyelle, donc compatible avec « d' »)
- `explanation` → `Après « beaucoup d' », il faut un nom de sentiment : amitié. Amical est un adjectif, ami désigne une personne et l'entraide est une action, pas un sentiment qu'on ressent.`
- Longueurs : 6 · 3 · 8 · clé 6. Une seule réponse : « affection », seul autre nom de sentiment possible, n'est pas proposé.

## 4. Mineurs

### Chapitre 03

1. `03/exercices/03-revision.json` q1, option d (`son – sont – sont – son`) : une seule erreur son/sont, mais l'option n'est pas étiquetée. Ajouter `"misconceptionTag": "fr.homophone.son-sont-confondus"`.
2. `03/exercices/03-revision.json` q2 (reprise cahier p.34 ex.3) : le PDF imprime « le petit lapin **blanc** » et finit par « …un sommeil plus calme, car ses frères ne le taquineront plus. ». Une reprise garde les données → prompt : `Complète le texte : « Hier soir, le petit lapin blanc ___ de la peine. Il ___ un peu maltraité par ses frères qui l'ont griffé et mordu. Dorénavant, il ne ___ plus embêté par eux. Il ___ un sommeil plus calme, car ses frères ne le taquineront plus. »` (clé et options inchangées).
3. `03/cours.md` l.67 : « Au passé composé, le verbe se forme avec l'auxiliaire avoir » généralise trop (*aller* prend *être*, M6) → `Au **passé composé**, _avoir_ et _être_ se forment avec **l'auxiliaire avoir au présent + le participe passé**.`
4. `03/cours.md` l.42 : *épithète* est un nom féminin (« l'épithète… on peut **le** supprimer ») → `- L'adjectif épithète fait partie du groupe du nom : on peut le supprimer, la phrase reste complète (_Le lapin se sauve._).`
5. `03/cours.md` § dialogue : boss q2 demande de choisir le verbe introducteur selon la réplique (`demande` pour une question), mais le cours se contente de lister ces verbes. Ajouter au `::: propriete` (après la l.199) : `- Il va avec la réplique : _demander_ pour une question, _répondre_ après une question, _crier_ ou _s'écrier_ pour un appel.`
6. `03/exercices/04-defi.json` q6 : l'explanation dit « Les autres versions oublient un de ces signes ». Or l'option a ne les oublie pas, elle **déplace** le guillemet fermant → `… puis un tiret pour la parole de Rania, qui est un autre personnage. Les autres versions oublient ou déplacent un de ces signes.`
7. `03/exercices/05-entrainement.json` q6 (« Les frères du lapin deviennent gentils ») répète presque la vérification du cours (l.49 « Ses grands frères deviennent gentils ») → prompt `Dans « Les frères du lapin paraissent honteux. », quel mot est attribut du sujet ?`, clé `honteux`, sans `acceptedAnswers` (invariable), explanation : remplacer « deviennent » par « paraissent » (« restent calmes » et « devient triste » sont déjà pris par 01-pratique q2).
8. `03/quiz.json` q1 : « sujet du verbe » et « complément du verbe » ne tentent pas un élève qui a lu la section. Toléré en d1.
9. `vocab-french-6eme.json` / `map-vocab.md` : `fr.lexique.sens-figure-lu-au-propre` (03 défi q5, et 04 défi q2 après C/M) n'est mappé qu'aux modules 01, 05, 06. Ajouter 03 et 04.

### Chapitre 04

1. `04/cours.md` l.52 (vérification) reprend mot pour mot l'item de `03-revision` q2 (« Les enfants sortent toujours le soir », cahier p.45 ex.3) : l'élève a vu la réponse. Remplacer dans la vérification → `Mets à la forme négative : « _Mon frère range toujours sa chambre le samedi._ »` et la réponse → `_Toujours_ se transforme en _ne… jamais_ ; le verbe conjugué est _range_, donc _ne_ le précède et _jamais_ le suit : **Mon frère ne range jamais sa chambre le samedi.**`
2. `04/cours.md` l.216 : « Laurent crie : « Au secours ! » ». Dans le texte (cahier p.50 ex.4), c'est **la mère** qui crie → `(La mère crie : « Au secours ! » ; « Je n'ai fait que mon devoir », répond l'apprenti)`.
3. `04/quiz.json` q4, option d `remplissez` (présent malgré « demain », une seule erreur) : ajouter `fr.temps.indicateur-de-temps-ignore`. Même chose pour `04/exercices/01-pratique.json` q4 d `choisissent`.
4. `04/exercices/02-boss.json` q4, option b (la suite des événements prise pour la complication) : ajouter `fr.recit.partie-du-recit-confondue`.
5. `04/exercices/05-entrainement.json` q1 (doute 2) : l'ordre est unique en pratique. Pour le rendre strict → option a `Au carrefour, un lourd tonneau tombe d'un camion et roule à grand fracas.` (voir § 5, réponse 2).
6. `04/quiz.json` q4 et `03-revision` q5 : il y a un double espace avant la parenthèse du verbe (« tableau.  (verbe remplir) ») → un seul espace.
7. `04/cours.md` l.108 : le cas-limite « réunir garde ses deux voyelles » n'apprend rien. → `- Cas-limite : le participe ne prend jamais de _t_ ni de _s_, même avec _ils_ : _ils ont rempli_, _elles ont choisi_.`
8. Reprises `04/03-revision` q3 et q4 (cahier p.51 ex.1 et ex.3) : données raccourcies (phrases de Virginie omises, texte au futur de départ retiré). Les blancs et les réponses sont fidèles au PDF : acceptable, signalé pour la traçabilité.

### Reprises confrontées au PDF (cahier 121615, manuel 121614)

| Item | Page PDF | Verdict |
| --- | --- | --- |
| 03 rev q1 | 121615 p.41 ex.2 | ✓ mêmes phrases, 4 choix |
| 03 rev q2 | 121615 p.34 ex.3 | ⚠️ « blanc » et fin de phrase omis (mineur 03-2) ; réponses a eu / a été / sera / aura ✓ |
| 03 entr q1 | 121615 p.41 ex.1 | ✓ 6 blancs (la fiche dit « 7 », le PDF en a 6) |
| 03 entr q2 | 121615 p.32 ex.1a, phrase 2 | ✓ |
| 04 rev q1, q2 | 121615 p.45 ex.2 ph.2, ex.3 ph.3 | ✓ |
| 04 rev q3, q4 | 121615 p.51 ex.1, ex.3 | ✓ blancs fidèles, contexte raccourci (mineur 04-8) |
| 04 rev q5 | 121615 p.47 ex.4a | ✓ a aidé / ont rempli / ont nourri / ont blanchi |
| 04 entr q2 | 121615 p.49 ex.1d, étiquettes 1 | ✓ « je n'ai jamais eu d'aventure pareille » |
| 04 entr q4 | 121615 p.50 ex.4 | ✓ 5 des 6 phrases, mot pour mot |
| 04 boss q5 | 121614 p.69 jeu 4 | ✓ (explication B paraphrasée : « Le bonheur succède souvent au malheur ») |
| 04 entr q1 (variante, sans champ `manuel`) | 121615 p.46 ex.3 | ✓ variante correctement non tracée |

### Cours — les cinq axes

| Axe | 03 | 04 |
| --- | --- | --- |
| Clarté | bonne ; 6 sections, une notion chacune, tableaux pour les conjugaisons | bonne |
| Compréhension (sept temps) | ancrage → question → définition → tableau + liaison → exemple justifié → piège → propriété + cas-limite → vérifie → retenir, dans toutes les sections. Tous les exemples, pièges et vérifications ont été re-résolus et sont justes, **sauf** l'ancrage de lecture (M-1) | même patron, re-résolu, juste ; rendu l.31 (M-7) ; section documentaire sans texte (M-8) |
| Exhaustivité | notions du module couvertes (épithète/attribut et 5 verbes d'état, être/avoir PC + futur, son/sont, dialogue, vocabulaire p.53–54) ; il manquait le proverbe (M-3) et le choix du verbe introducteur (mineur 03-5) | notions du module couvertes (ne… plus / ne… jamais, PC compris ; type finir PC + futur ; et/est ; schéma à 5 temps du cahier p.50 ; boîte à mots p.68–69 ; documentaire p.67) |
| Expérience | épigraphe, emojis, clôture 🏆 ; résumé = 6 cartes, une par section, autonome | idem |
| Illustration | sans objet (pas de famille spatiale) | sans objet |
| Scope (F1, F5, § 2.10) | rien d'interdit n'est ciblé ; l'imparfait n'apparaît qu'en support | idem ; « amicalement » (adverbe en -ment, tableau C) sort avec M-12 |

## 5. Réponses aux doutes de l'auteur

1. **Pièges du cours 04 sans distracteur : il faut ajouter des distracteurs, pas retirer les pièges.** Les deux notions sont au programme (boîte à mots p.69 jeu 4 ; lecture documentaire p.67) et ont un tag exact.
   - Proverbe — remplacer `04/exercices/04-defi.json` q2 (« Elle n'a plus pleuré depuis hier », qui fait doublon avec q1 et avec 03-revision q1) par :
     ```json
     { "prompt": "Que veut dire le proverbe « L'union fait la force » ?", "difficulty": 3, "correctOption": "b",
       "options": [
         { "id": "a", "text": "Quand on s'unit, chacun devient plus musclé.", "misconceptionTag": "fr.lexique.sens-figure-lu-au-propre" },
         { "id": "b", "text": "Ensemble, on réussit mieux que seul." },
         { "id": "c", "text": "Le plus difficile, c'est de commencer." },
         { "id": "d", "text": "Il vaut mieux travailler seul pour aller vite." } ],
       "explanation": "Un proverbe se lit au sens figuré : la force, ici, c'est le pouvoir de réussir. Quand on s'unit, on réussit mieux ensemble. Lu au sens propre, il parlerait de muscles, ce qui n'a pas de sens ici." }
     ```
     Longueurs : 44 · clé 36 · 38 · 46. Une seule réponse. La rampe reste croissante (q1 d2, q2 d3, q3 d3). Le proverbe n'apparaît pas dans la matching du boss : pas de doublon.
   - Documentaire — `04/exercices/04-defi.json` q5, option d → `{ "id": "d", "text": "Ce texte raconte l'histoire d'un enfant qui ne va jamais à l'école.", "misconceptionTag": "fr.texte.informatif-pris-pour-narratif" }`. Longueurs : 32 · clé 42 · 50 · 67. L'option est fausse « d'après ce texte » : il informe, il ne raconte pas.
   - `04/chapter.json` `coursePitfalls` : ajouter `"fr.lexique.sens-figure-lu-au-propre"` et `"fr.texte.informatif-pris-pour-narratif"` (8 ids, tous montrés en `::: piege` et portés par un distracteur).
2. **Variante de p.46 ex.3 : l'ordre est unique en pratique** (b-d-a-c). La sortie ouvre forcément le récit, et le sauvetage suit forcément la chute du tonneau. Seule la place de « rue animée / carrefour » pourrait en théorie suivre le sauvetage. Pour le rendre strict : option a → `Au carrefour, un lourd tonneau tombe d'un camion et roule à grand fracas.` (mineur 04-5). La décision de ne pas reprendre l'original est juste : avec « tournent à gauche », l'ordre n'est qu'une déduction du lecteur, et le cahier n'imprime aucun corrigé.
3. **`fr.lexique.mot-voisin-du-meme-champ`** :
   - 03 boss q5 (« avoir la paix chez soi », « lire en paix » pour « se réconcilier ») : **juste**. Ce sont des expressions du bon thème qui ne nomment pas ce qui est demandé. Le même tag va à la nouvelle option d (M-6).
   - 04 entraînement q5 : **juste pour « ami »** (une personne du thème, pas le sentiment). **Faux pour « amical »** : c'est une erreur de nature, adjectif pour nom, qu'aucun libellé ne décrit, donc l'option reste muette. **Faux pour « amicalement »**, qui est à remplacer (M-12).
4. **Imparfait dans les supports (« se moquait », « courait », « oubliait », « copiait »)** : un élève de 6ᵉ **peut** répondre. Aucune question ne demande d'identifier, de nommer ou de former l'imparfait. Le repère temporel est toujours porté par un mot qu'il connaît (« autrefois », « hier encore », « au début de l'année »). Le manuel lui-même raconte à l'imparfait et au passé simple. C'est conforme au § 2.10 D (« support seulement ») : on garde. Seul C-1 était à reprendre, pour une autre raison (« pas »).

## 6. Verdict

**À corriger** : 2 critiques et 12 majeurs (6 + 6), avec un texte de remplacement vérifié pour chacun. Aucune clé fausse. Les gates sont verts. Les reprises sont fidèles au PDF, à un raccourci près. Le scope F1/F5 est respecté. Après correction, relancer `content:check`, `content:qa -- --subject french-6eme` et `content:tranche … --strict-longest`. Le M-5 crée une égalité de longueur 48/48 : elle doit rester une égalité.

## 7. Re-vérification (après « Corrections après audit » de `rapport-B2.md`)

Contrôlé sur le corpus réel : les huit chapitres sont écrits et le lien `eng-deliver/content` pointe vers `wt-fr6b/content`. Toutes les questions modifiées ont été re-résolues à l'aveugle, soit 25 questions.

**Gates**
- `content:check` : ✓ (121 matières, 1066 chapitres ; `french-6eme` : 8 chapitres, 240 questions).
- `content:qa -- --subject french-6eme` : ✓ aucune clé suspecte.
- `content:tranche --chapters 03…,04… --fresh --strict-longest` : clé strictement la plus longue 0/46 ; positions a 24 % · b 28 % · c 22 % · d 26 % ; paires proches 0 ; gabarits 0 ; patron de notion 0 en recul.

**Rendu** (vitest jetable, supprimé ensuite) : aucun `*`, `:::` ou `_` résiduel dans les deux cours ni dans les deux résumés. À 360 px dans Chromium, la page mesure 360 px de large : aucun débordement.

**M-7 (écart signalé par l'auteur)** : la ligne est devenue `_Je n'ai plus téléphoné à mon frère._`. Elle rend `<em>Je n'ai plus téléphoné à mon frère.</em>`, sans astérisque. Le gras interne disparaît, mais les étapes 1 et 2 de l'exemple disent déjà où se placent *ne* et *plus*. **Corrigé**, l'écart est accepté.

| Défaut | État | Re-résolution |
| --- | --- | --- |
| C-1 04 rev q6 | corrigé | « plus » seul juste ; « jamais » contredit « hier encore » |
| C-2 04 défi q3 | corrigé | clé d seule juste ; a, b, c portent chacune une erreur étiquetée ; longueurs 45/48/44/47 |
| M-1 03 cours, lecture | corrigé | l'ancrage contient l'indice « Alors il reste à l'écart » |
| M-2 03 défi q1 | corrigé | b seule juste ; l'explication ne désigne plus les options par leur rang |
| M-3 03 défi q5 + cours | corrigé | puce « proverbe » au cours (l.292) ; c seule juste |
| M-4 03 entr q1 | corrigé | explication juste (« le clown est ») |
| M-5 03 quiz q5 | corrigé | b seule juste ; égalité 48/48 avec d, la clé n'est pas strictement la plus longue |
| M-6 03 boss q5 | corrigé | c seule juste |
| M-7 04 cours l.31 | corrigé (voir ci-dessus) | — |
| M-8 04 cours, documentaire | corrigé | texte affiché en citations, intertitres en gras ; l'exemple et la vérification se résolvent sur ce texte |
| M-9 04 pièges | corrigé | défi q2 « L'union fait la force » : b seule juste ; défi q5 d étiquetée `informatif-pris-pour-narratif` ; `coursePitfalls` à 8 ids |
| M-10 04 défi q1 | corrigé | a, c, e |
| M-11 04 défi q4 | corrigé | c seule juste, la phrase est dans le récit |
| M-12 04 entr q5 | corrigé | d seule juste ; « amical » muet ; « entraide » étiqueté |
| Mineurs 03-1 à 03-7, 04-1 à 04-7 | corrigés | 03 entr q6 « honteux » seul juste ; 04 entr q1 : l'ordre b-d-a-c est désormais strict (« Au carrefour, ») |
| 03-8, 04-8 | tolérés (inchangés) | — |
| 03-9 | fait par le pilote (hors lot) | — |

**Reste un seul mineur, non bloquant.** `04/exercices/04-defi.json` q5 : l'explication ne mentionne pas la nouvelle option d (texte pris pour un récit). Texte proposé pour `explanation` :

> Le texte dit qu'un enfant sur trois ne va jamais à l'école : certains enfants n'y vont jamais. Dire que tous y vont est le contraire du texte, rien n'y dit que les garçons perdent ce droit, et ce texte informe : il ne raconte pas l'histoire d'un enfant.

**Verdict final : prêt à armer.** Aucun critique ni majeur ne reste. Le mineur ci-dessus peut être corrigé lors de l'armement, sans nouvel audit.
