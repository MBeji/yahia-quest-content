# Audit indépendant — lot L05, anglais 9ᵉ (gisement, étude 36 — devoirs en salle blanche)

Auditeur indépendant, 2026-10-17. Arbre `/home/user/wt-en`, branche `wip/gisement-anglais-9eme`. Les deux fichiers ont été écrits au commit `99bd463b` et n'ont pas changé depuis (vérifié au HEAD `82062c59`) :
- `17-devoir-…` : sha1 `67fd53dc` ;
- `09-devoir-…` : sha1 `7e3c2379`.

Consignes suivies :
- `content-ingest/references/gisement-auditeur.md` ;
- skill `content-audit` ;
- grille `prompt-anglais-auditeur.md` ;
- règles de l'auteur `prompt-anglais-devoirs.md` et `gisement-auteur-devoir.md` ;
- cartes `assign-anglais-devoirs.md`.

Sur demande expresse de l'orchestrateur, j'ai lu les instantanés `/tmp/claude-0/devoirs-snapshots/english/D0*.txt`, pour le contrôle de salle blanche. Je n'ai pas lu les notes de l'auteur. Rien n'a été écrit dans `content/` ni dans git.

Périmètre : 2 missions, 15 questions.

| mission | fichier | étage | q. |
| --- | --- | --- | ---: |
| 09/17 | `09-reading-comprehension-writing/exercices/17-devoir-text-type-and-correcting-false-statements.json` | d2 practice 75/15 | 7 |
| 08/09 | `08-relative-clauses-comparatives/exercices/09-devoir-tense-and-degree-in-one-text.json` | d3 boss 120/30 | 8 |

## Gates (lecture seule, moteur `/home/user/eng-en`, lien `content` → `wt-en/content`)

- `content:check` : vert. 120 matières, 29 874 questions, 1 069 étiquettes.
- `content:qa:strict` : 0 erreur. Aucun avertissement ne touche `english/08` ou `english/09` : les 506 avertissements sont tous hors lot.
- `content:tranche --subject english --chapters 08,09` :
  - clé strictement la plus longue : 12/191, aucune dans le lot ;
  - positions des clés : 22/25/30/24 % ;
  - **22 paires proches, dont 12 entre questions du fichier 17** (Jaccard de 0,72 à 0,94). Je les juge au point 2 ;
  - aucun candidat gabarit dans le lot.
- `content:gisement:controle --sources …/devoirs-snapshots/english <2 fichiers>` : 15 textes contrôlés ; 0 plage de 8 mots ou plus ; 0 plage de 6 mots ou plus ; 0 exercice source dont on reprenne 2 ou 3 données. ✓

## 1. Salle blanche (contrôle manuel sur D01–D06)

J'ai cherché par `grep` les noms, lieux, objets, nombres et adjectifs des deux missions dans les 6 instantanés : seed library, post office, Oued Rmel, les quatre noms, bakery, loaf, crust, oven, tourists, popular, 1962, 2015, 2019…

- **Thèmes.** Aucun thème commun. Les sources parlent d'un pirate de l'air (D04), d'un parc d'attractions (D06), d'une mère seule (D02), de Cape Town (D04 ex. 3), de Spielberg (D05) et d'un argent de poche (D02). Ni bibliothèque de semences ni boulangerie.
- **Structure des questions.** Elle vient des cartes, comme prévu. D04 propose « article / e-mail / speech » et un tableau « Passenger / Destination / Purpose » ; la mission propose « news report / guide / advertisement / letter » et un tableau « Name / Who is this? ». Aucune phrase reprise.
- **Deux rapprochements d'un mot, sous le seuil de l'outil**, tous deux dans l'exercice de la carte D04#4 (« Over the past decade… tourists (fly) » ; « Cape Town is South Africa's (popular) city ») :
  1. 08/09 Q6 : « lately he (sell) bread to many tourists ». Même couple « tourists + present perfect ». La question tombe pour une autre raison (M5).
  2. 08/09 Q7 : « Mr Hamadi's is (popular) ___ of them all ». Même adjectif, au même superlatif, avec le même mécanisme de parenthèses. Mineur, mais correctif simple (m1).
- **Fichier 17.** Rien de commun avec D02, D04 ou D06 hors archétype.

---

## 09/17 — text type and correcting false statements (d2, 7 q.)

| Q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 horaires | nine to noon, except on Fridays | c | **défaut** | grille 2×2 propre, mais même donnée (horaires et jour de fermeture) que 09 quiz Q2, sur la liste (M6) |
| 2 familles | thirty, first week | b | OK (réserve) | 2×2 propre ; d « ninety » bien étiqueté (premier nombre de la phrase) ; a « first month » n'est pas faux au sens strict (m4) |
| 3 ouverture | last Tuesday, old post office | d | OK | 2×2 propre (jour × lieu) |
| 4 matching | Hana → reporter ; Chaabane → librarian ; Dhouib → retired farmer ; Salim → neighbour | idem | OK (mineur) | appariement unique ; facile pour d2, chaque nom porte son étiquette (m5) |
| 5 emprunteurs | new seeds in autumn | a | OK (voir M7) | 2×2 propre ; c'est la seule question qui peut porter le piège de la carte, absent du lot |
| 6 type | news report | c | OK | forme (titre, signature, faits récents, citations) contre thème ; le guide exécute le piège « juger sur le thème » |
| 7 cause | seeds twice as expensive | b | OK (mineur) | paraphrase juste de « had doubled » ; c et d bien étiquetés ; a contient « free », absent du texte (m6) |

Grilles 2×2 (Q1, Q2, Q3, Q5) : chaque valeur apparaît exactement deux fois, et l'option à deux erreurs est muette. Aucun vote ne reconstruit la clé. ✓

## 08/09 — tenses and degrees in one text (d3 boss, 8 q.)

| Q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 Every morning … (open) | opens | c | **défaut** | doublon de 01 quiz Q1 (« My father buys the newspaper every morning ») : même repère, même grille -s / continu / base (M1) |
| 2 (thin) ___ the crust | thinner than | a | **défaut** | vote : chaque distracteur ne change qu'un trait, donc « thinner » + « than » reconstruit la clé (M2) ; consonne doublée = gabarit de m015 Q1–Q2 |
| 3 in 1962 (build) | built | d | OK | builded / has built / builds bien étiquetés |
| 4 Recently … (hire) | **has hired OU hired** | b | **CRITIQUE** | « Recently, Mr Hamadi hired two young bakers. » est juste en anglais standard ; vote : has + hired → b (C1) |
| 5 Of all the ovens … (old) | the oldest | c | **défaut** | doublon de 08/05 Q5 publié (« Of all the days of the week, Monday is ___ (hard) » : the harder / the hardest / hardest / the most hard) ; vote : the + -est → c (M4) |
| 6 in 2015 / lately | opened / has sold | a | **défaut** | 2×2 propre, mais doublon de 02/04 Q4, sur la liste (« I first ___ snails in 2019, and I ___ them a lot lately ») ; aussi 02/02 Q6 et 02/05 Q6 (M5) |
| 7 Before 2015 / (popular) | had / the most popular | d | OK (mineur) | 2×2 propre ; a, à une seule erreur, est muet alors que l'étiquette existe ; « popular » = D04#4 (m1) |
| 8 multi | a, c, f | a, c, f | OK (mineur) | 3 justes sur 6, nombre non devinable ; l'énoncé garde « Complete the sentence. » alors qu'il n'y a rien à compléter (m2) |

Grilles 2×2 et vote :
- Q6 et Q7 : propres (chaque valeur deux fois, l'option à deux erreurs muette).
- **Q2, Q4 et Q5 : le vote reconstruit la clé.** Chaque distracteur n'y modifie qu'un trait de la clé.
- Q8 : les trois justes couvrent les trois temps visés plus un comparatif ; les trois fausses couvrent present perfect + temps fini (×2) et un superlatif manqué. Le `multi` de synthèse est cohérent avec les questions simples.

---

## Défauts classés

### Critique (1)

**C1 — 08/09 Q4, deux réponses justes.** « Recently, Mr Hamadi hired two young bakers. » est correct en anglais standard, britannique comme américain : *recently* accepte le prétérit pour un événement achevé (Swan, *Practical English Usage*, § recently). Le cours 02 associe *recently* au present perfect, mais il ne le place qu'« after have/has, or at the end », jamais en tête de phrase. L'élève qui choisit « hired » n'a pas tort. En plus, le vote (has + hired) désigne la clé.

Remplacement, vérifié. *Lately*, placé en fin de phrase comme le cours l'enseigne, exige le present perfect. Le verbe est irrégulier et figure au cours 02 (take → took → taken). Pas de doublon : m007 Q10 travaille « has written », 02/04 Q3 « lately » seul.
- `prompt` : `A school magazine describes Mr Hamadi's bakery. Complete the sentence.\n\n"The local newspaper (take) ___ many photos of the bakery lately."`
- options :
  - a `have taken` — `english.verb.auxiliaire-mal-accorde`
  - b `has taken` — **clé**
  - c `took` — `english.tense.preterit-au-lieu-du-present-perfect`
  - d `have took` — muette (deux erreurs)
- `explanation` : `"Lately" links the action to today and gives no finished time, so the verb is in the present perfect: have or has, then the past participle. The newspaper is one thing (it), so the auxiliary is "has". Take is irregular: its past participle is "taken", while "took" is its simple past.`
- Vérifications :
  - longueurs 10 / **9** / 4 / 9 : la clé n'est ni la plus longue ni la plus courte ;
  - vote : have ×2, has ×1, sans auxiliaire ×1 ; taken ×2, took ×2. Le vote ne désigne pas b ;
  - une seule réponse juste ;
  - aucune fuite vers les autres questions.

### Majeurs (7)

**M1 — 08/09 Q1, doublon du quiz 01 publié (Q1).** Même repère (*every morning*), même grille : verbe en -s / continu / base / forme fausse. C'est aussi le patron des 12 items de m006, sur la liste.

Remplacement (d1). La question au présent simple est enseignée au cours 01 (« Does he live in Sfax? ») et n'apparaît dans aucune mission d'examen.
- `prompt` : `In the school magazine, a pupil interviews Mr Hamadi, the baker. Complete the pupil's question.\n\n"What time (you / open) ___ your bakery every morning?"`
- options :
  - a `do you open` — **clé**
  - b `are you opening` — `english.tense.continu-pour-habitude`
  - c `you open` — `english.question.auxiliaire-ou-ordre-oublie`
  - d `does you open` — `english.verb.auxiliaire-mal-accorde`
- `explanation` : `"Every morning" shows a habit, so the question is in the present simple. A question in the present simple needs the auxiliary before the subject: "do" with you, "does" only with he, she or it, and the verb then stays in its base form. The continuous is for an action happening now, not for a habit.`
- Vérifications :
  - longueurs 11 / 15 / 8 / 13 ;
  - pas de vote possible : chaque auxiliaire n'apparaît qu'une fois ;
  - 01/04 Q3 (« What does your sister do ») porte sur *do* verbe principal : ce n'est pas le même savoir.

**M2 — 08/09 Q2, le vote reconstruit la clé.** « thinner » est dans a et d, « than » dans a, b et c. La consonne doublée reprend par ailleurs m015 Q1–Q2 (biger / bigest), sur la liste. Le piège de la carte (« comparatif sans than ») mérite une grille 2×2 propre.

Remplacement. *soft* ne figure ni dans m014, ni dans m015, ni dans les publiés du 08, ni dans les instantanés.
- `prompt` : `A school magazine describes Mr Hamadi's bakery. Complete the sentence.\n\n"The crust of the new loaf is (soft) ___ the crust of the old one."`
- options :
  - a `softer than` — **clé**
  - b `more soft than` — `english.comp.forme-selon-longueur`
  - c `softer` — muette (le piège de la carte, sans étiquette au registre)
  - d `more soft` — muette (deux erreurs)
- `explanation` : `Soft is a short adjective, so the comparison takes -er: "softer", not "more soft". Two crusts are compared, so "than" must come before the second one; without it, nothing links the new crust to the old one.`
- Vérifications :
  - longueurs 11 / 14 / 6 / 9 ;
  - softer ×2, more soft ×2 ; than ×2, sans ×2 ;
  - une seule réponse juste.

**M3 — 08/09 Q4** : c'est C1, un seul correctif.

**M4 — 08/09 Q5, doublon de 08/05 Q5 publié, et vote.** Même ouverture (« Of all the… »), même grille the -er / the -est / -est / the most. Le vote (the + -est) désigne c. La même règle revient en Q7 (moitié degré) et en Q8 d : trois fois « of all → superlatif » dans une mission de 8 questions.

Remplacement (d3) par une grille temps × degré, l'archétype propre à la carte. *small* n'est pas employé dans m014 ou m015 ; « smaller » n'y figure que comme indice de m015 Q10.
- `prompt` : `A school magazine describes Mr Hamadi's bakery. Complete the sentence.\n\n"Mr Hamadi usually (bake) ___ (small) ___ loaves for the school canteen than for his shop." Choose the correct pair.`
- options :
  - a `bake / smaller` — `english.verb.s-oublie-3e-personne`
  - b `bakes / more small` — `english.comp.forme-selon-longueur`
  - c `bakes / smaller` — **clé**
  - d `bake / more small` — muette (deux erreurs)
- `explanation` : `"Usually" shows a habit, so the verb is in the present simple, and Mr Hamadi is one person (he): "bakes", with its -s. Small is a short adjective: its comparative is "smaller", and "than" introduces the second thing compared. "More" goes only before a long adjective.`
- Vérifications :
  - longueurs 14 / 18 / **15** / 17 ;
  - bake ×2, bakes ×2 ; smaller ×2, more small ×2 ;
  - une seule réponse juste : « usually » exclut le continu et le passé n'est pas proposé.

**M5 — 08/09 Q6, doublon de 02/04 Q4, sur la liste.** Même grille « année finie / lately » : prétérit / present perfect × 2. Le même patron se retrouve en 02/02 Q6 et 02/05 Q6 (publiés). S'y ajoute l'écho « tourists + present perfect » de D04#4.

Correctif : **supprimer Q6**. Le piège « present perfect avec un repère fini » reste travaillé en Q3 b, Q7 a et Q8 b/e. La suppression règle aussi une incohérence du récit : Q3 dit que le grand-père a bâti le four de la boulangerie en 1962, Q6 que Mr Hamadi a ouvert « sa boulangerie » en 2015.

**M6 — 09/17 Q1, doublon de donnée du quiz 09 publié (Q2), sur la liste.** Le quiz 09 Q2 travaille déjà les jours et horaires de la cantine. Q1 est de plus la quatrième question de la même micro-tâche (correction 2×2 de deux détails, avec Q2, Q3 et Q5) ; ce sont les paires à 0,89–0,94 de l'outil.

Correctifs :
- **supprimer Q1** ;
- retirer du texte sa dernière phrase, qui ne sert plus à aucune question : `The library is open from nine to noon, except on Fridays.` Elle est à retirer dans les 6 énoncés restants, ce qui ramène le texte de 146 à 134 mots.

Après suppression :
- 6 questions, rampe 1-2-2-2-2-3 ;
- les explications de Q3 et Q5 (« The first sentence », « The second sentence ») restent exactes.

**M7 — 09/17, piège de la carte non exécuté.** La carte nomme trois pièges :
1. « corriger en niant la phrase sans le détail juste » ;
2. « juger le type de texte sur le thème » ;
3. « prendre un détail pour la cause ».

Le 2 est en Q6 a, le 3 en Q7 a. **Aucune option n'exécute le 1.** Le cours 09 (§ Scanning) enseigne la correction « avec les mots du texte », ce qui rend le piège enseignable.

Remplacement des options de Q5. L'énoncé ne change pas.
- options :
  - a `They bring back new seeds in autumn.` — **clé**
  - b `They do not bring back ripe tomatoes in the spring.` — muette (piège de la carte, sans étiquette au registre)
  - c `They bring back new seeds in spring.` — muette
  - d `They bring back ripe tomatoes in autumn.` — muette
- `explanation` : `The second sentence of the text says what a borrower does: grow the plants and bring back new seeds in autumn. The borrower returns seeds, not vegetables, and the season is autumn; a correction must give both details. Saying only that the statement is not true corrects nothing: the reader still does not know what the text says.`
- Vérifications :
  - longueurs **36** / 51 / 36 / 40 : la clé est à égalité avec c, jamais seule la plus courte ;
  - seeds ×2, tomatoes ×2 ; autumn ×2, spring ×2. Le vote ne désigne rien ;
  - b est vraie mais ne corrige pas, et l'énoncé demande une correction « with the details of the text » : une seule réponse.

### Mineurs (8)

- **m1 — 08/09 Q7.**
  - « popular » est l'item de D04#4 : changer l'adjectif. *traditional* ne figure dans aucun instantané ni aucun item de 01, 02 ou 08, et il est logique pour une boulangerie familiale de 1962.
  - L'option a (une seule erreur, temps fini + present perfect) est muette alors que l'étiquette existe.
  - Options :
    - a `has had / the most traditional` — `english.tense.present-perfect-avec-temps-fini`
    - b `had / most traditional` — `english.comp.superlatif-sans-the`
    - c `has had / most traditional` — muette
    - d `had / the most traditional` — **clé**
  - Dans l'énoncé, `(popular)` devient `(traditional)`. Dans l'explication, `Popular is a long adjective` devient `Traditional is a long adjective`.
  - Vérifications : longueurs 30 / 22 / 26 / **26** ; chaque valeur deux fois.
- **m2 — 08/09 Q8.** L'énoncé dit « Complete the sentence. Which sentences are correct? ». `prompt` : `A school magazine describes Mr Hamadi's bakery. Which sentences are correct?`
- **m3 — 08/09, rampe après correctifs.** Q1 d1, Q2 d2, Q3 d2, Q4 d2, nouvelle Q5 **d3**, Q7 → 6ᵉ d3, Q8 → 7ᵉ d3. 7 questions, rampe non décroissante, étage boss honnête.
- **m4 — 09/17 Q2.** « Thirty families joined in the first month » n'est pas faux au sens strict : si trente familles se sont inscrites la première semaine, elles se sont inscrites le premier mois. Le distracteur est rattrapé par l'exigence « with the details of the text », mais une option tirée de la même phrase est meilleure :
  - a `Thirty families joined on the first morning.`
  - c `Ninety families joined on the first morning.`
  - b et d inchangées.
  - Explication : `The text gives the number of families and the period together: thirty families, in the first week. Ninety and "the first morning" belong to the packets on the shelves, not to the families. A correction must give both details of the text: the right number and the right period.`
  - Vérifications : longueurs 44 / **41** / 44 / 41 ; 2×2 propre.
- **m5 — 09/17 Q4 (matching).** Facile pour d2 : chaque nom est collé à son étiquette dans le texte. Acceptable comme transfert d'information (archétype de la carte). Sans intrus, la dernière paire est forcée.
- **m6 — 09/17 Q7 a.** « free lessons » : « free » n'est pas dans le texte, et l'option doit rester un vrai détail pris pour la cause. Option : `The village wanted a place for lessons on planting.` (51 ; clé 46, c 37, d 50).
- **m7 — 09/17 Q5.** Correction de saison : c'est le `::: verifie` du cours 09 transposé (« clean the beach in summer » → spring). Acceptable : le savoir-faire est le même, les données sont autres.
- **m8 — 09/17, thème voisin de m004.** Le cours de jardinage de m004 (2026 T) a lieu « every Saturday » ; ici, Mrs Dhouib enseigne la plantation le samedi. Aucune donnée ni aucune clé commune : simple voisinage.

---

## 2. Fichier 17 — le texte repris en entier dans les 7 énoncés

- **Longueur d'écran.** 146 mots, soit 707 à 833 caractères par énoncé. Sur un téléphone, à peu près un écran de texte, puis la question et 4 options d'une ligne. Le chapitre fait autrement : les missions d'examen m001–m005 citent une phrase (145 à 340 caractères), et les publiés 09/01 et 09/03 donnent 1 à 3 phrases par question.
- **Jugement : je garde le texte entier**, pour trois raisons :
  1. Q4 (quatre personnes réparties dans tout le texte), Q6 (le type se lit sur la forme : titre, signature, citations) et Q7 (la cause, contre les fausses pistes) ont besoin du texte complet ;
  2. dans les corrections, les leurres sont dispersés dans le texte : « Saturday » pour le jour, « ninety » pour les familles, « tomatoes » pour les emprunteurs. Couper l'énoncé à une ou deux phrases rendrait la correction triviale, puisque la phrase citée contiendrait la réponse sans aucun leurre ;
  3. 146 mots restent courts pour une compréhension de 9ᵉ.
- **Ce qui ne se justifie pas**, c'est la même micro-tâche répétée quatre fois (Q1, Q2, Q3, Q5). Les correctifs M6 et M7 la ramènent à trois occurrences, dont une qui porte le piège de la négation, et retirent une phrase du texte (134 mots).
- **Paires proches restantes.** Q2, Q3 et Q5 sont lues contre Q4, Q6 et Q7 : la ressemblance vient du texte partagé. C'est un exercice parallèle voulu (même texte, tâches distinctes), à justifier au rapport de livraison.

## 3. « Ne pas redemander », doublons et fuites

- **Liste du fichier 17** :
  - m001–m005 : pas de vrai/faux justifié, pas de tableau de dates ✓ ;
  - 09/01 Q2 (club) : pas de reprise ✓ ;
  - 09 quiz Q2 : **violé par Q1** (M6) ;
  - 09 quiz Q8 : ✓ ;
  - 10 quiz Q2 : la cause y est la raison d'une adhésion, ici celle de l'ouverture d'un lieu, et sur un autre format ✓ ;
  - aucun thème de devoir repris ✓.
- **Liste du fichier 08/09** :
  - m006 et 01 quiz Q1 → **M1** ;
  - m015 Q1–Q2 → **M2** (consonne doublée) ;
  - 02/04 Q4 → **M5** ;
  - m007 et m008 : Q3 (four de 1962) n'est le clone d'aucun item ✓ ;
  - m014 : ✓ ;
  - 01/04 Q2–Q6 : ✓ ;
  - 08/04 Q3 : ✓.
  - Doublon hors liste trouvé à la main, publié : **08/05 Q5** (M4).
  - Dérivation et gérondif : absents ✓.
- **Fuites dans les deux sens** :
  - entre les deux fichiers : aucune (savoirs disjoints) ;
  - entre ces fichiers et m001–m024 : aucune clé donnée ni reçue. J'ai relu chaque explication en me demandant quelle question elle résout ailleurs. Celles du 08/09 répètent des règles générales du cours (habitude → présent simple ; repère fini → prétérit), ce qu'il n'y a pas lieu de corriger. Aucune ne livre la clé exacte d'une autre question ;
  - à l'intérieur du 08/09, avant correctif : Q5, Q7 et Q8 d posaient trois fois la même règle « of all → the + superlatif ». C'est réglé par M4.
  - Les correctifs proposés ne créent aucune fuite :
    - la nouvelle Q1 (question) n'a pas d'équivalent dans le fichier ;
    - la nouvelle Q4 (take) non plus ;
    - la nouvelle Q5 croise « usually » et un comparatif court, ce qu'aucune autre question ne fait ;
    - Q8 a (« every Saturday ») reste une phrase différente.

## 4. Re-résolution

Les 15 questions ont été re-résolues à l'aveugle avant lecture de la clé : 14 accords, 1 clé non unique (C1). Le `matching` a été vérifié paire par paire, le `multi` énoncé par énoncé ; les 2×2 l'ont été case par case et au vote (voir les tableaux). Les textes de remplacement ont été vérifiés par script : longueurs, occurrences de chaque valeur, vote.

## 5. Étiquettes

Toutes existent dans `content/misconceptions.json` de l'arbre de travail, et toutes nomment exactement l'erreur exécutée :
- `s-oublie-3e-personne` ;
- `continu-pour-habitude` ;
- `forme-selon-longueur` (more thin, the most old) ;
- `suffixe-sans-regle-orthographique` (thiner) ;
- `ed-sur-verbe-irregulier` (builded) ;
- `present-perfect-avec-temps-fini` ;
- `present-avec-marqueur-passe` (builds + in 1962) ;
- `have-sans-participe` (has hire) ;
- `preterit-au-lieu-du-present-perfect` (lately) ;
- `auxiliaire-mal-accorde` ;
- `superlatif-sans-the` ;
- `comparatif-et-superlatif-confondus` (the older) ;
- `read.premier-mot-cle-sans-lire-la-phrase` (ninety, premier nombre de la phrase : c'est l'erreur commune du cours 09) ;
- `read.reponse-sans-appui-dans-le-texte` (bureau de poste, demande des voisins).

Réserve : le libellé de `preterit-au-lieu-du-present-perfect` cite « since, lately or ever », pas *recently* ; le correctif C1 passe à *lately* et s'aligne ainsi.

Distracteurs muets :
- à deux erreurs, normalement muets : 08/09 Q6 d, Q7 c ; 17 Q2 c ;
- sans étiquette au registre : 08/09 Q1 d « opened », Q2 d « thinner » (comparatif sans than) ; 17 Q1 a/b/d, Q3 a/b/c, Q5 b/c/d, Q6 a/b/d, Q7 a ;
- **taggable et laissé muet : 08/09 Q7 a** (m1).

**Famille proposée au pilote, si souhaitée.** La « correction incomplète » revient dans 17 Q2 a, Q3 a et c, Q5 c et d, et dans le nouveau Q5 b : au moins 3 questions distinctes.
- `english.read.correction-incomplete`
- fr : « Tu corriges une affirmation fausse à moitié : un détail faux reste, ou tu te contentes de la nier, au lieu de la réécrire avec les détails du texte. »
- en : « You correct a false statement only halfway: one wrong detail stays, or you only deny it, instead of rewriting it with the details of the text. »
- ar : « تصحّح الجملة الخاطئة نصف تصحيح: يبقى فيها تفصيل خاطئ، أو تكتفي بنفيها، بدل إعادة كتابتها بتفاصيل النصّ. »

Si elle est créée, elle se place sur les options à une seule erreur et sur la négation, jamais sur les options à deux erreurs.

## 6. Divers

- **Titres.** « Practice: reading one text closely » et « ⚔️ Boss: tenses and degrees in one story » suivent le patron des publiés du chapitre ✓.
- **En-têtes.** d2 75/15 et d3 120/30 ✓.
- **Langue.** Tout le texte visible est en anglais ✓. Aucune explication ne désigne une option par sa place ✓.
- **Notions.** Rien de hors programme : 08/09 n'emploie que les chapitres 01, 02 et 08 ; 17 n'emploie que le 09 ✓.
- **`chapter.json`.** La ligne T2′ manque dans `sources[]` du 08 et du 09, ce qui est attendu : le pilote l'ajoute à la livraison.

---

## Résumé

- **Questions auditées** : 15 (7 + 8).
- **Clés fausses** : 0. **Critique** : 1, 08/09 Q4 (« Recently … hired » juste en anglais standard ; vote).
- **Majeurs** : 7.
  - 08/09 : Q1 doublon de 01 quiz Q1 ; Q2 vote ; Q5 doublon de 08/05 Q5 + vote ; Q6 doublon de 02/04 Q4, sur la liste.
  - 17 : Q1 doublon de donnée de 09 quiz Q2 et 4ᵉ micro-tâche identique ; piège « nier sans le détail » non exécuté.
  - M3 se confond avec C1.
- **Mineurs** : 8, dont « popular » (rapprochement D04#4) et une option taggable laissée muette.
- **Étiquettes** : toutes exactes ; une famille optionnelle proposée.
- **Salle blanche** : 0 plage à l'outil, aucun thème commun ; deux échos d'un mot avec D04#4, soldés par M5 et m1.
- **Fichier 17** : le texte entier se justifie (leurres dispersés, tâches globales) ; la répétition de la micro-tâche ne se justifie pas (M6, M7).

**Verdict : à corriger avant livraison.**
- 08/09 : remplacer Q1, Q2, Q4 et Q5, supprimer Q6, retoucher Q7 et Q8. Résultat : 7 questions.
- 17 : supprimer Q1 et la phrase des horaires, remplacer les options de Q5, retoucher Q7 a et, si le pilote le veut, Q2. Résultat : 6 questions.

Tous les textes de remplacement sont donnés ci-dessus et vérifiés. Il faut ensuite une re-vérification courte : gates, puis `content:tranche` (les paires proches restantes se justifient par le texte partagé).
