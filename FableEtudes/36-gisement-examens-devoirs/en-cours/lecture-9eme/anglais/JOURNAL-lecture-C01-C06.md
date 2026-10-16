# Journal du lecteur — anglais 9ᵉ, lot pilote C01 à C06 (sessions 2026, 2025, 2024 ; générale et technique)

Étape G2. Lot pilote : les conventions du § 0 valent pour les autres lots anglais (C07 et suivants).
Lecture du 2026-10-16. Les six PDF sont des scans sans couche texte (`pdftotext` rend 4 octets) : lecture en
vision, 150 DPI, une fois par page (un détail relu à 220 DPI : « Los Angles », C06). Les six sha256 téléchargés
(`curl -g`, http, sans `-k`) égalent ceux de `docs.json`. Aucune écriture git, rien sous `content/english/`.

## 0. CONVENTIONS FIXÉES (à reprendre par les autres lots)

**Grain des lignes** (une ligne = un exercice numéroté imprimé ou une partie notée) :
- **Reading comprehension** : UNE ligne pour toute la partie (texte + questions), n°exo `1`, barème = total
  de la partie (6 en générale, 8 en technique), étapes = nombre de questions numérotées (5 sur les six sessions). Chapitre : `09-reading-comprehension-writing` **seul**, même si une question embarque une notion
  (C02 q3 « could » = possibilité ; C06 q4 « used to » = habitude passée : notées ici, pas ajoutées à la ligne).
- **Language** : UNE ligne par exercice numéroté imprimé (1, 2, 3), n°exo = rang d'ordre dans l'épreuve, donc
  **n° imprimé + 1** (2, 3, 4). Barème = points imprimés de l'exercice. Sous-items (0.5 chacun) sans suffixe.
- **Writing** : UNE ligne, dernière du document (n°exo `5`).
- n°exo = rang d'ordre `\d+[a-z]?` : toujours 1 (reading), 2-4 (langue), 5 (writing). Toutes les épreuves
  d'anglais ont exactement 3 exercices de langue.
- **Barème** : entier quand il l'est ; **un barème imprimé 2.5 est gardé tel quel** (« 2.5 marks » ne se ramène
  pas à un entier ; le validateur accepte le point décimal : 6 lignes décimales sur les 30). La transcription garde
  les 0.5/0.5 imprimés. À signaler au pilote si `lignes.tsv` exige l'entier.
- **Étage** : reading générale `d2` (question de justification personnelle), reading technique `d1` si guidée
  sans production (C02, C04), `d2` si table de dates ou valeur grammaticale (C06) ; cloze à banque guidée
  `d1` (C04 ex. 2 seulement, mots de vocabulaire uniquement), cloze/choix/appariement `d2`, mise en forme d'un mot
  entre parenthèses à plusieurs notions `d3` (C03 ex. 4) ; writing générale (10 à 12 lignes, 3 arguments) `d3`,
  technique (8 lignes) `d2`. Aucun `d4` en anglais.

**Chapitres** (jamais `10-exam-style-papers` ; compétences toujours `-`) :
- *Texte lacunaire à banque / à choix / mots à mettre en forme* : on cumule, dans l'ordre du manifeste, les
  chapitres de **notion de langue effectivement testée par au moins un item** — temps (01/02/03 selon le temps),
  modaux 04, conditionnel 05, passif 06, discours rapporté 07, relatives et comparatifs/superlatifs 08 (« who »,
  « which », « most », « wisest », « less ») — puis on ajoute `09-reading-comprehension-writing` quand **au moins
  la moitié des items** est lexicale (vocabulaire en contexte, collocations, prépositions, connecteurs
  « however/when »). Un exercice 100 % lexical = `09` seul (C04 ex. 2).
- *Appariement de débuts et de fins de phrases* (matching) : `09` seul (cohérence de sens et de construction).
- *Production écrite* : `09` seul pour un message argumenté ou persuasif (décrire, persuader, expliquer
  l'importance) ; `+04-modals` quand la consigne demande de **conseiller, avertir, proposer des moyens d'agir ou
  dire ce qu'on peut faire** (advise, warn, suggest ways, what you can do) ; `+02` pour un récit au passé, `+03`
  pour un projet futur (non rencontrés ici) ; jamais `05` ou `06` imposés par une consigne de writing.
- **HP : un jeton `HP:<mot-clé>` s'ajoute aux chapitres d'une ligne** quand un item teste une notion de langue
  absente des dix chapitres (la ligne reste placée au chapitre le plus avancé des autres jetons). Mots-clés
  fixés : `HP:word-formation` (dérivation : même mot à classe changée, entertain → entertainment, significant →
  significantly, employ- → employment ; le guide 9ᵉ n'enseigne que les noms/adjectifs composés et gérondif+nom) ;
  `HP:gerund` (forme en -ing exigée après préposition ou verbe, « without having », « begun offering », « no point
  in removing » ; le guide cite un « gérondif » mais aucun chapitre ne le porte). Un cas nouveau : le noter ici,
  au plus proche de ces deux mots-clés.
- *Hors HP, rangés en `09`* : prépositions et collocations (take part in, care for, effects on, drop out),
  connecteurs (however, when, while), vocabulaire, déterminants (these/those), choix de verbe lexical.

**Barème total des épreuves** : générale 6 + 8 + 6, technique 8 + 7 + 5 (= 20), durée imprimée 1 h, coefficient 1.
**Texte support** : jamais transcrit en entier. La transcription donne : référence imprimée, paragraphes, nombre de
mots approximatif (compté sur le snapshot), résumé neutre de 3 à 5 phrases, une citation courte au plus, et
« texte intégral : PDF officiel, sha256 au registre ». Le **texte lacunaire** d'un exercice de langue (cloze,
choix, mots à mettre en forme ; 80 à 120 mots) est lui un item : il est transcrit mot pour mot, lacunes en
`........`, options en gras entre parenthèses, banque de mots en tête. Aucun dialogue ni lettre-modèle de plus de
8 lignes n'apparaît dans la partie langue de ces six épreuves.
**Cases à cocher** : `[case]` après chaque proposition ; tableau vrai/faux en tableau Markdown avec `[case] | [case]` ;
mot souligné imprimé : `__mot__` ou rappel en italique sous la question. Pointillés de réponse `........`.
**En-tête de transcription** : même YAML que le français (`source: officiel`, `examen` sous son intitulé imprimé,
`matiere: Anglais`, `session`, `filiere`, `page`, `fichier`, `consulte_le: 2026-10-16`, `sha256`, `lecture: vision`).
**Coquilles imprimées** : conservées telles quelles et signalées entre crochets (§ 3). Aucun corrigé n'est publié
avec ces sujets : les transcriptions ne donnent aucune réponse.

## 1. Documents lus

| id | session | filière | sha256 (= registre ?) | pages | lecture | lignes | transcription |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C01 | 2026 | générale | 310a6cb2ad9f24a9be121118e60380975ef6ffb4ed07a244affc6d52d53bd804 (oui) | 4 | vision | 5 | `english/2026-generale.md` |
| C02 | 2026 | technique | 962f9aaefc24252d7e559f109dd35250d8a0f11b3f26c7fc9764bd4407a2b272 (oui) | 4 | vision | 5 | `english/2026-technique.md` |
| C03 | 2025 | générale | 340a7d17ab5a6c2a1edb28725939de2b81d33d2f262ce804972990e85c1d216c (oui) | 4 | vision | 5 | `english/2025-generale.md` |
| C04 | 2025 | technique | eb335ea548ff996859ea252723e33c237ed14846835736f26ff4f37791b5aacc (oui) | 4 | vision | 5 | `english/2025-technique.md` |
| C05 | 2024 | générale | 2bb302d60d11c488d8054629e4ed94c4131130d25622b22e785b803c75d80a69 (oui) | 4 | vision | 5 | `english/2024-generale.md` |
| C06 | 2024 | technique | 6c04bddfeabf582b77892e8243a734fbcb39d6fe98df5d07f8f6c80d5a37a51c (oui) | 4 | vision | 5 | `english/2024-technique.md` |

Transcriptions sous `/home/user/wt-en/content/programmes-officiels/examens-nationaux/9eme-base/english/`.
Snapshots locaux (hors dépôt, textes complets) : `/tmp/claude-0/enlec/snapshots/C0{1..6}.txt`. Lignes :
`lines/C0{1..6}.tsv` + `.meta` sous `…/lecture-9eme/anglais/lines/` (30 lignes ;
`content:gisement:lignes --subject english --grade 9eme-base … --content /home/user/wt-en/content` : 30 valides,
0 fautive, manifeste de 10 chapitres ; le lien `content` de `eng-svtses` pointe vers `wt-fr`, d'où le `--content`).

## 2. Format de l'épreuve (identique sur les trois sessions)

- Page 1 : un texte support informatif de 165 à 230 mots, trois paragraphes numérotés, source imprimée
  (presse en ligne ou site d'ONG, « Adapted from … ») ; pages 2 à 4 : questions.
- **Générale** (1 h, coeff. 1) : Reading 6 + Language 8 + Writing 6 = 20.
- **Technique** (1 h, coeff. 1) : Reading 8 + Language 7 + Writing 5 = 20. Thème des textes tourné vers les
  métiers (mécanique, jardinage, formation professionnelle) ; compréhension plus longue.
- Reading : 5 questions, toujours la même séquence : idée générale en QCM à trois options, vrai/faux sur deux
  énoncés avec renvoi de paragraphe, synonyme ou sens d'une phrase, référent d'un mot souligné, puis (générale)
  réponse personnelle justifiée à trous ou (technique) réponse courte / tableau / second référent.
- Language : toujours 3 exercices ; au moins un texte lacunaire de 80 à 120 mots avec banque ou choix
  d'options ; l'appariement de parties de phrases (2 points, 4 items + 1 intrus) est présent dans 5 sessions sur 6 ;
  C03 le remplace par des mots à mettre au temps/à la forme.
- Writing : article, message ou post de 8 à 12 lignes, « au moins trois arguments » (générale) ou 8 lignes
  (technique), consigne d'anonymat (« do not write your name »).

| session / filière | texte (nature) | reading | langue (par exercice) | writing |
| --- | --- | --- | --- | --- |
| 2026 G | père et argent de poche (presse) | 5 q., 6 pts | lacunes à banque 3 ; choix de formes 3 ; appariement 2 | article pour mettre en garde contre un danger (6) |
| 2026 T | cours de jardinage (presse) | 5 q., 8 pts | lacunes à banque 2.5 ; choix 2.5 ; appariement 2 | article de conseils sur un outil d'étude (5) |
| 2025 G | vélo-bus scolaire (presse) | 5 q., 6 pts | lacunes à banque 3 ; choix 2.5 ; mise en forme de mots 2.5 | post persuasif pour une destination (6) |
| 2025 T | centre de seconde chance (ONG) | 5 q., 8 pts | lacunes à banque 3 ; choix 2 ; appariement 2 | article sur la sécurité au travail (5) |
| 2024 G | jeune pianiste non voyant (fondation) | 5 q., 6 pts | lacunes à banque 3 ; choix 3 ; appariement 2 | post de moyens de réduire la pollution (6) |
| 2024 T | mécanicienne (presse) | 5 q., 8 pts | lacunes à banque 2.5 ; choix 2.5 ; appariement 2 | paragraphe d'aide à des camarades (5) |

## 3. Notions par chapitre (lot C01-C06, 30 lignes)

| chapitre | lignes où il apparaît |
| --- | --- |
| 01 present tenses | jamais testé comme tel |
| 02 past tenses (+ present perfect) | C01#3 (grew), C02#2 (has been), C03#4 (spent), C05#2 (was destroying), C05#3 (has done), C06#2 (built), C06#3 (began) |
| 03 future | jamais |
| 04 modals | C05#2 (would) ; production : C01, C02, C05, C06 (conseiller, avertir, proposer) ; question de reading C02 q3 (could), non comptée |
| 05 conditionals | jamais testé en langue ; voir § 4 (cadre « If I were… » du reading) |
| 06 passive voice | C03#2 (can be found) |
| 07 reported speech | jamais |
| 08 relatives & comparatives | C01#2 (who, wisest), C03#3 (less), C03#4 (more fashionable), C04#3 (who), C05#3 (which), C06#3 (most) |
| 09 reading & writing | six readings, six writings, tous les appariements, les lexicaux |
| 10 exam-style | non employé |

**Part HP** : aucune ligne entièrement HP ; **7 lignes sur 30** portent un jeton HP en complément d'un vrai
chapitre : `HP:word-formation` (6 lignes : C01#3, C02#3, C03#3, C03#4, C04#3, C06#3) et `HP:gerund` (3 lignes :
C03#4, C04#3, C06#2). Le programme en vigueur (guide 9ᵉ) enseigne les relatifs, comparatifs/superlatifs,
modaux, passé simple/present perfect/past progressive et le premier conditionnel ; l'examen sollicite en plus la
dérivation de mots et le gérondif, absents des dix chapitres.

Chapitres jamais testés : 01, 03, 05, 07 (et 10 par définition). Le passif n'apparaît qu'une fois (C03#2) ; le
discours rapporté, le futur et le conditionnel jamais en langue sur 2024-2026.

Coquilles imprimées conservées dans les transcriptions : « DOT NOT WRITE YOUR NAME » (C01, C02) ; « 2,5 marks » avec
virgule (C03 ex. 3) ; « 2marks » sans espace (C04 reading q5) ; « Los Angles Technical College » (C06 ex. 2) ;
« chapman » sans majuscule (C05, texte) ; « meet-up » avec trait d'union pour le verbe (C03 ex. 3, dans le texte
lacunaire) ; coquilles de pagination (« Page 1 sur 4 » en 2025, « 1/4 » en 2024 et 2026). Aucune consigne n'a
vieilli : les trois grammaires testées (passé, comparatifs, relatifs) sont au programme.

## 4. Doutes de classement (à trancher par le pilote)

- **Cadre « If I were… I ______ approve »** (C01 q5, C03 q5) : la réponse personnelle impose une phrase au
  conditionnel irréel (2ᵉ conditionnel), absent du programme (seul le premier conditionnel est enseigné) ; classé
  `09` seul comme tout le reading. Si le pilote veut compter ce signal, il faudrait un jeton `HP:conditional-2`
  sur ces deux lignes de reading : non fait pour respecter « 09 seul ».
- **Embarqué dans le reading** : C02 q3 (« could » = possibilité) et C06 q4 (« used to » = habitude passée) testent
  une valeur grammaticale ; `04` et `02` écartés par la règle « 09 seul ».
- **`HP:word-formation`** : le guide 9ᵉ mentionne « noun formation » (gérondif + nom, noms composés) mais pas la
  dérivation par suffixe ; classé HP faute de chapitre. Si l'on juge la dérivation enseignée au collège (7ᵉ-8ᵉ),
  la notion resterait quand même hors de la liste des dix chapitres de la 9ᵉ.
- **C04 ex. 3** (« gets educated », forme passive-participiale ; « none who is jobless », relatif) : classé `08`
  + deux HP ; `06` écarté (participe adjectival, pas un passif à produire).
- **C03 ex. 2** (« can be found ») : `06` retenu pour un seul item sur six ; la moitié des autres items est lexicale
  d'où `+09`.
- **C05 ex. 1** : `04` retenu pour « so that he would be away » ; « was destroying » rangé en `02` (past progressive,
  enseigné en M6).
- **Production persuasive** (C03) : classée `09` seul (pas de conseil à donner) ; `08` n'est pas ajouté bien que
  « the best destination » appelle un superlatif.
- **Barème décimal** : 2.5 conservé (voir § 0).

## 5. Difficultés

Aucune de lecture : six scans nets, aucune zone illisible, aucun item `[illisible]` ; aucune marque
`[hors programme en vigueur]` posée, la 9ᵉ de 2024-2026 restant dans le champ du guide (réserve : le cadre
« If I were » ci-dessus). Un transparent de la page imprimée au verso se lit en fantôme sur les scans (texte
d'une page voisine), sans effet sur la transcription. Téléchargement HTTP direct sans proxy particulier ; sha
identiques au registre. Les banques de mots sont reproduites dans l'ordre imprimé ; l'association lacune/mot n'est pas transcrite (aucun corrigé publié).
