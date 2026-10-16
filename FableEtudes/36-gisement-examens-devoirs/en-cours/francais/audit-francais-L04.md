# Audit indépendant — lot L04, français 9ᵉ (gisement, étude 36)

Auditeur indépendant, 2026-10-16. Branche `wip/gisement-francais-9eme` (arbre `/home/user/wt-fr`).
Consigne suivie : `content-ingest/references/gisement-auditeur.md` (en entier), skills `content-audit` puis
`prof-francais-9eme`. Je n'ai ouvert ni les notes des auteurs ni les sources de devoirs.

Périmètre : 5 missions, 54 questions.

| mission | fichier | q. |
| --- | --- | ---: |
| m018 | `07-lexique-et-figures-de-style/exercices/06-examens-2018-2026-sens-d-un-mot-en-contexte.json` | 12 |
| m019 | `07-lexique-et-figures-de-style/exercices/07-examens-2015-2026-synonyme-en-contexte-et-autre-sens.json` | 10 |
| m020 | `14-homophones-et-adverbes-en-ment/exercices/06-examens-2002-2025-former-l-adverbe-en-ment.json` | 10 |
| m021 | `14-homophones-et-adverbes-en-ment/exercices/07-examens-2007-2026-homophones-en-contexte.json` | 10 |
| m022 | `12-reprises-et-pronoms-complements/exercices/06-examens-2001-2021-le-pronom-qui-remplace-le-groupe.json` | 12 |

Gates (moteur `/home/user/eng-svtses`, lien `content` → `wt-fr/content`) : `content:check` vert ;
`content:qa:strict` : aucune alerte sur les 5 fichiers (la seule erreur du corpus est hors lot :
`french-1ere-sec/06-…/cours`) ; `content:tranche --chapters 07,12,14` : clé strictement la plus longue
0/141, positions 24/26/25/26 %, 0 paire proche. `sources[]` : la ligne R8 est ajoutée aux trois
`chapter.json`. Aucune figure (sans objet). Toutes les données ont été confrontées aux transcriptions.

---

## m018 — `07/06` sens d'un mot en contexte (d2, 12 q.)

| Q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 exploit | réussite | c | OK (réserve) | « échec » et « défaite » sont synonymes entre eux (options officielles) |
| 2 champion | vainqueur | b | OK | |
| 3 diriger | commander | a | OK | bon piège « orienter vers un lieu » (le texte a « se dirigent vers ») |
| 4 franchir | passer | d | OK | « ouvrir » ajouté, faux |
| 5 personnalité | personne connue | a | réserve | fuite vers `09/10` Q3 (voir mineurs) |
| 6 lever | gonfler | b | OK | |
| 7 couronner | conclut | d | **défaut** | l'énoncé ajoute « ou le détruit » : le distracteur officiel « détruit » s'élimine à vue |
| 8 témoigner | montrer | c | OK | |
| 9 louer | valoriser | a | OK | |
| 10 retouche | correction | b | OK | |
| 11 au rabais | à un prix réduit | d | OK | options modernisées, sens conservé |
| 12 tomber fou amoureux | coup de foudre | c | OK | |

Fidélité : toutes les phrases citées sont dans les transcriptions (2026 T, 2025 T, 2024 T, 2023 T,
2021 T, 2020 T, 2019 T). Aucune question de 2018 T (écartée par la consigne) : le titre « 2018–2026 »
est faux. Rien de redemandé (07 quiz, 07/01–05, 09 quiz/missions publiées : aucun de ces mots).

## m019 — `07/07` synonyme en contexte et autre sens (d2, 10 q.)

| Q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 réservée | discrète | b | OK | mais clé livrée par les options de Q10 |
| 2 emploi | usage | a | OK | mais clé livrée par l'explication de Q9 |
| 3 décidé | résolu | c | OK | |
| 4 à l'œuvre | en plein travail | d | OK (mineur) | citation coupée sans « […] » |
| 5 prendre la relève | la remplacer | c | OK (mineur) | étiquette approximative sur « l'aider à se relever » |
| 6 déchirer | rompre | a | OK | |
| 7 donner du mal | m'ont posé des difficultés | b | OK | |
| 8 mettre la main à la pâte | participer soi-même au travail | d | OK (mineur) | sens donné tel quel par le cours (cas-limite § expressions figées) |
| 9 emploi, autre sens | « proposer un emploi » | b | OK (réserve) | explication qui livre Q2 |
| 10 réservé, autre sens | « table réservée » | c | **défaut** | trois options sur quatre paraphrasent « discrète » : clé de Q1 |

Fidélité : phrases conformes (2024 G, 2022 T, 2026 G, 2025 G, 2023 G, 2022 G, 2021 G, 2019 G), sauf
« pièces d'étoffe » (l'imprimé a « étoffes ») et la coupe de 2025 G. Aucune question de 2015 à 2018 :
le titre « 2015–2026 » est faux.

## m020 — `14/06` former l'adverbe en -ment (d2, 10 q.)

| Q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 poli | poliment | b | **défaut** | redemande 14/02 Q3 et 14/04 Q6 (liste « ne pas redemander »), et l'exemple travaillé du cours |
| 2 chaleureux | chaleureusement | d | réserve | clé reconstituable au vote |
| 3 fréquent | fréquemment | c | réserve | vote |
| 4 quotidien | quotidiennement | a | réserve | vote |
| 5 absolu | absolument | d | **défaut** | l'explication nomme « profond » → clé de Q7 |
| 6 constant | constamment | b | réserve | vote |
| 7 profond | profondément | c | OK | |
| 8 net | nettement | a | réserve | vote ; l'explication cite « profondément » (fuite au donjon) |
| 9 gentil | gentiment | d | **défaut** | redemande 14/02 Q3 (gentiment / gentillement) |
| 10 impatient | impatiemment | b | OK | déjà en 2×2 (« impatiament » à deux erreurs, muet) |

Fidélité : phrases conformes (2025 G, 2024 G, 2023 G, 2017 G, 2005, 2002), sauf deux cadres : Q7
« voit sa mère rentrer » (c'est l'élève qui rentre et trouve sa mère) et Q9 « Un élève dit du petit
Chose » (le petit Chose est le surveillant-narrateur).

## m021 — `14/07` homophones en contexte (d2, 10 q.)

| Q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 Quand / Quant | Quand … Quant | c | OK | 2×2 propre |
| 2 n'y | n'y | a | **défaut** | rappel unilatéral qui désigne la clé ; « nie », « nid » de remplissage ; l'explication livre Q7 |
| 3 Quand / qu'en | Quand … qu'en | d | OK (mineur) | 2e blanc = geste de 14/02 Q4 |
| 4 qu'en | qu'en | b | OK | |
| 5 sans s'en | Sans s'en | a | OK (mineur) | proche de 14/04 Q3–Q4 |
| 6 s'en tirer | s'en | c | OK (mineur) | même variante que Q5 ; le « qu'en comptant » de l'énoncé montre la forme de Q3 |
| 7 ni … ni | Ni … ni | b | **défaut** | rappel « ni sert à nier deux éléments, ni l'un ni l'autre » = la clé |
| 8 Quel / qu'elle | Quel … qu'elle | a | **défaut** | « Quel chagrin » est le « quel + nom » à écarter ; « penser … partirait » = 14 quiz Q1 et 14/05 Q6 |
| 9 quelle que | quelle | d | **défaut** | rappel « quels que soient » = forme-clé de Q10 ; citation officielle modifiée |
| 10 quels que | quels | b | **défaut** | rappel « quelle que soit » = forme-clé de Q9 ; Q9 et Q10 font doublon |

## m022 — `12/06` pronom qui remplace le groupe (d2, 12 q.)

| Q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 l'ont réconforté | b | b | OK | |
| 2 pour le cacher | d | d | mineur | « pour cacher lui » porte deux erreurs mais une étiquette |
| 3 Nous le | c | c | OK | |
| 4 de lui | a | a | mineur | « d'elle » s'élimine par le genre d'André |
| 5 lui a demandé | c | c | OK | |
| 6 y poursuit | b | b | OK | |
| 7 y consacre | y | a | **critique** | « leur » (option d) est défendable |
| 8 en parle | d | d | OK | |
| 9 la laissent faire | b | b | mineur | étiquette sur la mauvaise option |
| 10 il le nourrit | d | d | **défaut** | doublon de Q3 (et de Q1) |
| 11 les réciter | a | a | **défaut** | la clé remplace aussi la 1re phrase, que l'examen garde : pronoms sans antécédent |
| 12 le mettre | c | c | OK | 2×2 propre |

Fidélité : conforme (2006, 2008, 2017 T, 2003, 2011 G, 2011 T, 2015 T, 2021 T, 2016 T), sauf Q11.
Aucune question de 2001 : le titre « 2001–2021 » est faux.

---

## Défauts classés

### Critique (1)

**C1 — m022 Q7 (`12/06`), distracteur défendable.** « Elle leur consacre tout un livre » se dit en
français standard. Avec les choses, on emploie « lui / leur » quand le verbe est « consacrer » (« Ce
projet, je lui consacre mes soirées »). La lecture « leur = les enfants » est encore plus naturelle.
L'explication (« leur ne reprend pas des choses ») va trop loin. NB : contrairement à ce qui est
signalé, « leur » **figure** dans les options (d).
Correctif : option d `leur` → `lui`. Elle est fausse sans appel : singulier, aucun référent singulier
possible. Explication, dernière phrase → « « En » remplace un complément introduit par « de », « les »
un COD, et « lui », singulier, ne peut pas reprendre des témoignages. » Longueurs y 1 · en 2 · les 3 ·
lui 3 : la clé reste la plus courte, comme avant (inhérent à « y »).

### Majeurs (12)

**M1 — m018 Q7, option éliminée par l'énoncé.** L'énoncé cite le texte avec « … ou le détruit », alors
que l'item officiel s'arrête à « couronne le travail ». « détruit » ne peut plus être choisi.
Énoncé → `(Examen 2023 technique) Henri, le boulanger, va enfourner son pain : « Le boulanger accomplissait l'opération la plus délicate qui couronne le travail. » Dans cette phrase, que signifie « couronne » ?`
(phrase officielle de l'item ; les options sont conjuguées, donc on demande « couronne », pas l'infinitif).
Explication →
`« Couronner » vient de « couronne » : on pose la couronne en dernier, au sommet. Au figuré, couronner un travail, c'est le conclure en beauté. Enfourner est la dernière étape du travail du boulanger : elle le conclut. « Commence » dit l'inverse, « détruit » est le contraire d'une réussite, et aucun prix n'est décerné ici.`
Options inchangées : la clé « conclut » (7) n'est pas la plus longue.

**M2 — m019 Q10 → Q1, fuite au donjon.** Les options a, b et d définissent « réservé » (« parle peu »,
« n'aime pas se faire remarquer », « sourit sans rien dire ») et livrent « discrète ».
Options a, b, d →
`Mon cousin est très réservé avec les inconnus.` (46) · `Malgré son succès, ce garçon est resté réservé.` (47) ·
`Ma sœur est d'un naturel plutôt réservé.` (40). La clé c (44) n'est ni la plus longue ni la plus courte.
Explication →
`Dans la phrase officielle, « réservée » parle du caractère d'une personne : c'est le même sens pour le cousin, le garçon et la sœur. Dans « une table réservée pour six personnes », le mot est le participe du verbe « réserver » : la table est retenue à l'avance pour des clients. C'est un autre sens.`

**M3 — m019 Q9 → Q2, fuite au donjon.** L'explication (« la manière dont on utilise les étoffes »)
livre « usage ». Explication →
`Dans « mode d'emploi », dans « l'emploi du pluriel » et dans « faire bon emploi de son argent », le mot a le même sens que dans la phrase officielle. Dans « me proposer un emploi », il désigne un travail rémunéré, un poste : c'est un autre sens du même mot.`
Réponse au point signalé : oui, les questions « autre sens » livraient les synonymes. Q10 le faisait
par ses options, Q9 par son explication. Après M2–M3, elles ne le font plus. L'inverse (Q1 et Q2
avant Q9 et Q10 sur la route) est le schéma voulu de la consigne officielle en deux temps : acceptable.

**M4 — m020 Q1 et Q9, « ne pas redemander » violé.** Q1 (poli → poliment, piège « poliement ») =
14/04 Q6 et 14/02 Q3, plus l'exemple travaillé et le piège du cours. Q9 (gentil → gentiment, piège
« gentillement ») = 14/02 Q3 et le piège du cours. La consigne de tri gardait ces deux adverbes tout en
listant 14/02 Q3 et 14/04 Q6 à ne pas redemander : j'applique la liste. Remplacements tirés des mêmes
sujets, sans « poli » ni « gentil » (vérifiés absents de `content/french/` sur `origin/main`) :
- Q1 → (2024 G, d1)
  `(Examen 2024 générale) Une adolescente raconte : « … et maman s'adonnait (régulier) … à la marche. » Quel adverbe en -ment forme-t-on sur l'adjectif « régulier » ?`
  options `régulierement` · `régulièrement` (clé) · `régulieremment` · `régulièremment`, toutes muettes.
  C'est un plan 2×2 accent × double m. Longueurs 13 / 13 / 14 / 14.
  Explication : `On ajoute -ment au féminin de l'adjectif. Le féminin de régulier est régulière, avec un accent grave : on obtient régulièrement, comme fier donne fièrement. Sans accent, on n'écrit pas le féminin ; et le double m ne concerne que les adjectifs en -ant et en -ent.`
- Q9 → (2005, d1 ; corrigé officiel : « accepter tout adverbe » ; l'énoncé impose l'adjectif)
  `(Examen 2005) Dans un récit d'Alphonse Daudet, on lit : « Le petit Chose nous rejoignit d'un pas rapide. » Quel adverbe en -ment, formé sur l'adjectif « rapide », remplace « d'un pas rapide » ?`
  options `rapidément` · `rapidemment` · `rapidémment` · `rapidement` (clé), toutes muettes, 2×2 é × mm.
  Longueurs 10 / 11 / 11 / 10.
  Explication : `L'adjectif rapide se termine déjà par un e au masculin : son féminin est le même. On ajoute simplement -ment : rapidement. L'accent aigu de -ément n'appartient qu'à quelques adverbes à retenir, et le double m qu'aux adjectifs en -ant et en -ent.`
  Ces deux items sont d1 : les placer dans le bloc d1, en tête.

**M5 — m020 Q5 (et Q8) → Q7, fuite.** L'explication de Q5 (« -ément … (profond, énorme) ») livre la clé
de Q7, qui la suit sur la route. Celle de Q8 (« (profondément) ») la livre au donjon.
Q5, dernière phrase → `La terminaison -ément ne concerne que quelques adverbes à retenir.`
Q8, dernière phrase → `Nettément et nettemment sont inventés : l'accent aigu n'appartient qu'à quelques adverbes en -ément à retenir, et le double m qu'aux adjectifs en -ant ou -ent.`

**M6 — m020, clé reconstituable au vote (Q2, Q3, Q4, Q6, Q8).** Chaque distracteur ne change qu'un
trait de la clé, si bien que le vote trait par trait donne la clé. Remplacer un distracteur par une
forme à deux erreurs, muette (vote recalculé : il ne donne plus la clé ; aucune clé n'est strictement
la plus longue) :
- Q2 : a `chaleureusemment` → `chaleureuxemment` (longueurs 16 / 14 / 15 / clé 15) ;
- Q3 : d `fréquement` → `fréquament`, étiquette retirée (13 / 11 / clé 11 / 10) ;
- Q4 : d `quotidiennemment` → `quotidienemment` (clé 15 / 14 / 13 / 15) ;
- Q6 : c `constemment` → `constement`, étiquette retirée (13 / clé 11 / 10 / 10) ;
- Q8 : c `nettément` → `netément` (clé 9 / 8 / 8 / 10).
Ajuster les explications en conséquence : nommer l'erreur de chaque forme, sans lettre.
Q5, Q7 et Q10 sont déjà sans reconstruction.

**M7 — m021 Q2 et Q7 (n'y / ni), rappels qui désignent la clé et fuite croisée.** Q2 rappelle seulement
« n'y » (clé de Q2) ; Q7 rappelle seulement « ni … ni, ni l'un ni l'autre » (clé de Q7).
L'explication de Q2 (« ni aurait besoin d'un second élément nié ») résout Q7, qui la suit.
« nie » et « nid » sont du remplissage. Correctif : **fusionner Q2 et Q7** en une question (d2), sur les
trois premiers blancs du paragraphe officiel de 2021 G, avec un rappel symétrique :
`(Examen 2021 générale) On rappelle que « ni » relie deux éléments niés ensemble (ni l'un ni l'autre) et que « n'y » est formé de « ne » et du pronom « y ». Quels mots complètent, dans l'ordre : « Aman est devenu ingénieur. Personne … croyait. … Dan, … les autres élèves n'imaginaient qu'il réussirait un jour à terminer brillamment ses études. » ?`
options `n'y / Ni / ni` (clé, 13) · `ni / Ni / ni` (12) · `n'y / N'y / n'y` (15) · `ni / N'y / n'y` (14), muettes.
Le vote est nul à chaque position.
Explication : `Premier blanc : « croyait » demande la négation « ne » et un complément « à cela », repris par le pronom « y » : Personne n'y croyait. Deuxième et troisième blancs : « Dan » et « les autres élèves » sont niés ensemble : Ni Dan, ni les autres élèves. « N'y » ne se met pas devant un nom : le pronom « y » se place devant un verbe.`

**M8 — m021 Q9 et Q10 (« quel que »), doublon et fuite croisée.** Réponse au point signalé : oui,
c'est un doublon de fait. La règle est la même (accord avec le sujet de « soit ») ; seuls le genre et
le nombre changent. En plus, l'exemple du rappel de chacune est la forme-clé de l'autre : « quels que
soient » pour Q10, « quelle que soit » pour Q9. Q9 modifie aussi la citation officielle (« devra
assumer » au lieu de « sera amenée à assumer »). Correctif :
- Q9 devient le choix homophone sur la phrase officielle 2009 G (c'est la consigne d'origine :
  qu'elle / quel / quelle) :
  `(Examen 2009 générale) On rappelle que, dans « quel que soit … », « quel » s'accorde avec le sujet de « soit », placé après lui. Quels mots complètent, dans l'ordre : « Sa sœur, quant à elle, sait déjà … réussira … que soit la responsabilité […]. » ?`
  options `qu'elle … quelle` (clé, 16) · `quelle … qu'elle` (16, muette) ·
  `qu'elle … qu'elle` (17, `fr.homophone.quel-qu-elle`) · `quelle … quelle` (15, `fr.homophone.quel-qu-elle`).
  Explication : `Premier blanc : « elle » est le sujet du verbe « réussira » ; on peut dire « qu'il réussira » : que + elle, qu'elle. Second blanc : « soit » a pour sujet « la responsabilité », nom féminin singulier : quelle que soit. « Qu'elle que soit » n'a pas de sens : aucun sujet « elle » n'y précède un verbe.`
- Q10 : même rappel, sans exemple de forme :
  `On rappelle que, dans « quel que soit … », « quel » s'accorde avec le sujet de « soit », placé après lui.`
  (le reste est inchangé).

**M9 — m021 Q8, matière déjà posée.** « Quel chagrin ! » est le « quel » exclamatif devant un nom, que
la consigne de tri demandait d'écarter (14/01 Q1). « J'étais triste de penser … partirait » est le
geste de 14 quiz Q1 (« Je crois … viendra ») et de 14/05 Q6 (« dit … ira »), tous deux sur la liste.
Les autres blancs de 2019 G (« … émotion ! », « … autres expériences ») sont aussi déjà posés (13 quiz
Q5, 14/04 Q1). Correctif : **supprimer Q8**.

**M10 — m022 Q10, doublon de Q3.** Même fait : un COD de personne remplacé par « le », placé devant un
verbe au présent, avec sujet pronominal. Mêmes pièges : « lui », pronom après le verbe. Le plan
disait « 2015 T : un item au plus, s'il apporte du neuf ». Les autres items de 2001, 2008, 2010 T et
2012 T sont aussi déjà posés (Q2, Q4, Q5, 12/04 Q5). Correctif : **supprimer Q10**.

**M11 — m022 Q11, consigne officielle altérée, pronoms sans antécédent.** L'examen souligne seulement
« Ma mère » et « mes poèmes » de la **seconde** phrase. La clé « Elle les aime. Elle m'encourage à les
réciter… » remplace aussi la première : dans un chapitre de **reprises**, « Elle » et « les » n'ont plus
d'antécédent. Correctif :
`(Examen 2021 technique) Mary raconte : « Ma mère aime mes poèmes. Ma mère m'encourage à réciter mes poèmes devant nos proches. » Dans la seconde phrase, on remplace « Ma mère » et « mes poèmes » par des pronoms. Quelle seconde phrase est correcte ?`
options `Elle m'encourage à les réciter devant nos proches.` (clé, 50) ·
`Elle m'encourage à réciter les devant nos proches.` (50, `fr.pronom.place-apres-verbe`) ·
`Elle m'encourage à leur réciter devant nos proches.` (51, `fr.pronom.cod-coi-confondus`) ·
`Elle m'encourage à réciter leur devant nos proches.` (51, muette), en plan 2×2.
Explication : `« Elle » reprend « Ma mère », nommée dans la première phrase. « Mes poèmes » est le COD de l'infinitif « réciter » (réciter quelque chose) : on le remplace par « les », placé devant cet infinitif, « à les réciter ». « Leur » remplace un complément introduit par « à » qui désigne des personnes.`

**M12 — m021 et m022 : effectifs après correctifs.** m021 passe de 10 à 8 questions (Q2+Q7 fusionnées,
Q8 supprimée), m022 de 12 à 11. Les deux restent dans la fourchette R7 (6–12).

### Mineurs (12)

- **m1 — Titres faux** sur la borne basse : m018 « 2018–2026 » → **2019–2026** (2018 T écarté) ; m019
  « 2015–2026 » → **2019–2026** ; m022 « 2001–2021 » → **2003–2021**. Les noms de fichier portent les
  mêmes années : ils peuvent être renommés tant que rien n'est publié. m020 (2002–2025) et m021
  (2007–2026) sont justes.
- **m2 — m018 Q5, fuite vers `09/10` Q3** (lot L01, même texte 2024 T) : « alors que leurs familles ne
  se fréquentaient pas » est la clé de `09/10` Q3 et Q4. Énoncé →
  `(Examen 2024 technique) Antoine se demande pourquoi Charles s'est rapproché de lui au collège : « Son père était une personnalité de la ville. » Dans cette phrase, que signifie le mot « personnalité » ?`
  Explication, phrase « Une personne ordinaire… » → `Dans le texte, ce père est opposé au père d'Antoine, un modeste cordonnier : il est connu et respecté. Rien ne parle d'un étranger.`
- **m3 — m018 Q1** : « un échec » et « une défaite » sont synonymes entre eux (options officielles).
  Ils s'éliminent ensemble ; c'est toléré pour une reprise fidèle.
- **m4 — m019 Q4** : coupe de la phrase officielle sans marque → `« Rarement […] avait-il été donné d'admirer une serveuse si vive à l'œuvre. »`.
- **m5 — m019 Q2 et Q9** : « pièces d'étoffe » → `pièces d'étoffes` (texte imprimé) dans la citation.
- **m6 — m019 Q5** : `fr.lexique.sens-figure-lu-au-propre` sur « l'aider à se relever ». C'est une
  confusion de famille (relève / se relever), pas une expression figurée lue au propre. Option à
  laisser muette.
- **m7 — m019 Q8** : le sens de « mettre la main à la pâte » est donné tel quel par le cours (§
  expressions figées, cas-limite). La question est un rappel direct : à garder, mais elle ne vaut pas
  le d2.
- **m8 — m020 Q7** : cadre inexact → `(Examen 2023 générale) Après l'incendie d'une remise, un élève raconte : « En rentrant à la maison, j'ai trouvé ma mère (profond) … inquiète. »` (phrase de l'item).
- **m9 — m021 Q3, Q5, Q6** : Q3 (2e blanc) reprend le geste « qu'en + gérondif » de 14/02 Q4 ; Q5
  recoupe 14/04 Q3–Q4 (sans / s'en, s'en devant un infinitif pronominal). Q6 répète la variante de
  Q5, et son énoncé officiel (« qu'en comptant ») montre la forme du 2e blanc de Q3 au donjon. Le
  planificateur les a gardés à dessein : à garder, mais si un item doit encore tomber, c'est Q6.
- **m10 — m022 Q2 c et Q9 c** : « pour cacher lui » et « laissent faire elle » ont deux erreurs (pronom
  tonique ET place) mais portent `place-apres-verbe`. Q2 c → `… pour cacher le.` (17 ; étiquette gardée).
  Q9 c → étiquette retirée ; Q9 d « ils laissent la faire », qui est l'erreur de place seule → étiquette
  `fr.pronom.place-apres-verbe`.
- **m11 — m022, distracteurs éliminés par une prémisse** : Q4 d « d'elle » (André est un garçon), Q1 d
  « les ont », Q3 d « Nous les » (antécédent singulier). Ils restent dans des items à quatre options où
  le reste discrimine : à garder, mais faibles. Q4 d → `Elle s'est approchée de le.` (forme atone après
  préposition, muette) ; la clé (28) devient alors la plus longue d'un caractère, sur ce seul item.
- **m12 — m022 Q6 et Q7** : deux « y » de suite (lieu, puis à + chose). L'explication de Q6 (« une chose
  introduite par à → y ») résout Q7 par la règle. C'est de la pratique d'une règle du cours : toléré.

---

## Points signalés par l'auteur — tranchés

1. **Notions données dans l'énoncé.**
   - « ni … ni » n'est enseigné nulle part (01 à 14) : la définition dans l'énoncé est nécessaire.
   - « n'y » se déduit du cours : le pronom « y » est au chapitre 12, la négation au 01.
   - L'accord de « quel » avec le sujet de « être » est au 13 (« Quels sont tes projets »). La locution
     « quel que soit » n'est pas enseignée : le rappel est légitime.
   - Mais un rappel ne doit ni nommer la seule clé (Q2, Q7), ni montrer la forme-clé d'une autre
     question (Q9 ↔ Q10). Correctifs M7–M8.
   - Les deux « quel que » sont un doublon (M8).
2. **Réponses que l'énoncé officiel laisse passer.**
   - 2005 « avec gentillesse » : l'énoncé impose « formé sur gentil » et aucune option n'est un autre
     adverbe juste, donc la réponse est unique. Mais l'item redemande 14/02 Q3 : il est remplacé (M4).
   - 2011 G « consacre » : « leur » n'a **pas** été écarté. Il est l'option d, et il est défendable
     (C1) : le remplacer par « lui ».
3. **m021 à 10 au lieu de 12, écartés vérifiés.** « Ce n'est … interrogeant » (2011 G) = qu'en +
   gérondif, déjà en Q3 et en 14/02 Q4. « il … félicite » (2022 G) = s'en devant un verbe conjugué,
   comme 14/02 Q2. « il … pensait plus » (2021 G) = même geste que « Personne n'y croyait ». Les trois
   écarts sont justes. Après correctifs, la mission tombe à 8 (M7–M9).
4. **Étiquette proposée « -ment ajouté au masculin »**, aucune équivalente sur `origin/main`.
   - Q8 « netement » n'en relève pas : c'est un féminin mal écrit (nete au lieu de nette), pas le
     masculin + -ment.
   - En revanche, Q9 b « gentilment » en relève. La famille compte donc 3 questions distinctes avec
     cette seule erreur : Q2 b, Q4 c et Q9 b.
   - « fréquentement », « constantement » et « impatientement » sont le féminin + -ment : leur
     étiquette `ant-ent-mal-forme` est juste.
   - Si Q9 est remplacée (M4), la famille retombe à 2 : options muettes, pas de nouvelle étiquette.
   - Si l'étiquette est créée, libellé proposé :
     `Tu ajoutes -ment au masculin de l'adjectif : la règle part du féminin (chaleureuse → chaleureusement, quotidienne → quotidiennement) ; seuls les adjectifs en -ai, -é, -i, -u gardent le masculin.`
5. **m019 : les « autre sens » livraient-ils les synonymes ?** Oui : Q10 par ses options, Q9 par son
   explication (M2, M3).
6. **Rampe d1 → d2.** Les étages sont honnêtes, et le tri stable ne change pas l'ordre du fichier. Une
   fuite en avant vient du bloc d1 : m021 Q2 → Q7 (M7). Une autre est interne au d2 : m020 Q5 → Q7 (M5).
   Les autres explications d1 énoncent une règle du cours, non une clé : rien à signaler.

## Résumé

- **Questions auditées :** 54, toutes re-résolues à l'aveugle.
- **Clés fausses :** 0.
- **Critique :** 1 (m022 Q7, « leur » défendable).
- **Majeurs :** 12, à reprendre : m018 Q7 ; m019 Q9–Q10 ; m020 Q1, Q5, Q8, Q9 et le vote sur Q2–Q4,
  Q6 ; m021 Q2/Q7 à fusionner, Q8 à supprimer, Q9–Q10 ; m022 Q10 à supprimer, Q11.
- **Mineurs :** 12 (trois titres, fidélité de citations, étiquettes, distracteurs faibles).
- **Étiquettes :** les `fr.*` employées existent et nomment l'erreur, sauf trois options :
  - m019 Q5 a : à laisser muette ;
  - m022 Q2 c et Q9 c : deux erreurs chacune, à laisser muettes ;
  - famille « masculin + -ment » : 3 questions avec Q9, 2 sans.
- **Doublons :**
  - m020 Q1 et Q9 avec 14/02 Q3 et 14/04 Q6 ;
  - m021 Q8 avec 14 quiz Q1 et 14/05 Q6 ;
  - m021 Q9 et Q10 entre elles ;
  - m022 Q10 et Q3 entre elles.
- **Verdict : à corriger avant fusion** (fix-first). Les correctifs ci-dessus sont vérifiés : longueur de
  la clé, unicité, vote, fuites.
