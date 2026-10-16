# Audit indépendant — gisement français 9ᵉ, lot L02 (m007–m012)

Auditeur : session d'audit du 2026-10-16, branche `wip/gisement-francais-9eme` au commit `fcea5969`
(« L02 écrit »). Valide pour ce commit : ré-auditer si les fichiers ont bougé.
Skills chargés : `content-audit`, `prof-francais-9eme` ; consigne `gisement-auditeur.md` suivie.
Notes d'auteur non ouvertes. Comparaison : transcriptions officielles des sessions citées, `cours.md`
/ `resume.md` / quiz / missions publiées de `origin/main` (`ee891788`), registre `fr.*` de
`origin/main:content/misconceptions.json`, fiche programme `programme/9eme-base/francais.md`.

Gates (moteur `/home/user/eng-svtses`) : `content:check` vert ; `content:qa --strict` : 0 constat
sur `french/` (la seule erreur du dépôt est sur `french-1ere-sec`, sans lien avec ce lot) ;
`content:tranche --chapters 01,02,11` : clé strictement la plus longue 0/140, positions 28/26/25/21 %,
aucune paire proche dans le lot. Le candidat gabarit « examen générale de départ quelle phrase est
juste » (02/07 Q2, Q6, Q7 et 11/06 Q7) ne vient que du chapeau commun : les tâches diffèrent, ce n'est
pas un gabarit.

Périmètre : 6 missions, **53 questions**, toutes re-résolues à l'aveugle (énoncé et options
d'abord, clé ensuite).

## 1. Tableaux de re-résolution

### `02-propositions-subordonnees/exercices/06-examens-2002-2025-cause-but-consequence-intensite.json` (m007, d3 boss 120/30)

| Q | ma réponse | clé | verdict | motif |
|---|---|---|---|---|
| 1 | b | b | OK | 2024 G a, fidèle |
| 2 | a | a | réserve | énoncé paraphrasé au lieu de la phrase officielle (voir D-8) |
| 3 | c | c | OK | 2025 G a, fidèle |
| 4 | d | d | OK | 2025 G b, fidèle |
| 5 | b | b | OK | 2022 G b, fidèle |
| 6 | a | a | OK | 2021 G a ; contrainte « en commençant par la subordonnée » déclarée |
| 7 | c | c | OK | 2021 G b ; même sujet → infinitif dit dans l'explication |
| 8 | d | d | OK | 2017 G (but), fidèle |
| 9 | a | a | OK | 2006 b, fidèle |
| 10 | b | b | réserve | 2002 demandait « la conséquence » seule : précision non déclarée (D-9) |

### `02-propositions-subordonnees/exercices/07-examens-2001-2018-pronom-relatif-selon-la-fonction.json` (m008, d3 boss 120/30)

| Q | ma réponse | clé | verdict | motif |
|---|---|---|---|---|
| 1 | b | b | réserve | « Rappel » du relatif composé dans l'énoncé (cours muet, D-6) |
| 2 | a | a | OK | 2018 G b, fidèle |
| 3 | c | c | réserve | « Rappel » qui donne la soudure de + lequel : application directe (D-6) |
| 4 | d | d | OK | 2008 b, fidèle |
| 5 | a | a | réserve | « Rappel » des formes (D-6) |
| 6 | b | b | OK | 2005 b ; « auquel » absent des options, comme prévu |
| 7 | c | c | OK | 2010 G b |

### `02-propositions-subordonnees/exercices/08-examens-2001-2021-dire-la-cause-autrement.json` (m009, d2 practice 75/15)

| Q | ma réponse | clé | verdict | motif |
|---|---|---|---|---|
| 1 | a | a | réserve | glose « bec-de-lièvre » placée à l'intérieur de la citation (D-12) |
| 2 | b | b | OK | 2012 G, 3ᵉ blanc |
| 3 | a | a | OK | 2009 G b |
| 4 | c | c | MAJEUR | deux distracteurs éliminés à vue (D-7) |
| 5 | d | d | OK | 2003 a |
| 6 | a | a | OK | 2013 G a |
| 7 | b | b | réserve | « Rappel » car/donc (D-6) ; phrase officielle retouchée (D-11) |
| 8 | c | c | OK | 2021 T a |
| 9 | a | a | MAJEUR | trois phrases sur quatre inventées sous l'étiquette « Examen 2010 technique » (D-3) |
| 10 | d | d | OK | 2002, 2ᵉ item |

### `02-propositions-subordonnees/exercices/09-examens-2002-2022-temps-concession-subordonnee-ou-groupe.json` (m010, d3 boss 120/30)

| Q | ma réponse | clé | verdict | motif |
|---|---|---|---|---|
| 1 | a | a | OK | 2022 T a |
| 2 | b | b | mineur | « toute » ajouté dans la seule option a (D-14) |
| 3 | a | a | OK | 2020 G a ; « ne » explétif expliqué |
| 4 | c | c | OK | 2020 G b, QCM conforme à R6 |
| 5 | d | d | OK | 2017 G 2, gérondif |
| 6 | a | a | OK | 2017 G 2, subordonnée |
| 7 | b | b | OK | 2013 G c |
| 8 | c | c | MAJEUR | concession : le cours du 02 la déclare hors programme et « non évaluée » (D-5) |
| 9 | a | a | MAJEUR | idem (D-5) |

### `11-groupe-nominal-et-attribut/exercices/06-examens-2016-2026-enrichir-le-groupe-nominal.json` (m011, d3 boss 120/30)

| Q | ma réponse | clé | verdict | motif |
|---|---|---|---|---|
| 1 | a | a | OK | 2026 G ; étiquette possible sur d (D-15) |
| 2 | c | c | OK | 2026 G |
| 3 | d | d | OK | 2026 G |
| 4 | b | b | mineur | phrase officielle restructurée sans le dire (D-15) |
| 5 | a | a | OK | 2016 G ; étiquette possible sur c (D-15) |
| 6 | c | c | MAJEUR | « Au bout de la même phrase » : renvoie à Q5 (D-4) |
| 7 | a | a | OK | 2016 G |
| 8 | d | d | OK | 2022 T b |

### `01-types-et-formes-de-phrases/exercices/06-examens-2011-2024-forme-negative-qui-garde-le-sens.json` (m012, d2 practice 75/15)

| Q | ma réponse | clé | verdict | motif |
|---|---|---|---|---|
| 1 | a | a | MAJEUR | d est aussi une phrase négative bien construite (D-1) |
| 2 | c | c | OK | 2024 T b |
| 3 | b | b | OK | 2023 T a |
| 4 | a | a | réserve | règle « une → de » donnée dans l'énoncé (D-6) |
| 5 | d | d | MAJEUR | c « n'était jamais fier » est une négation bien construite, l'explication le reconnaît (D-1) |
| 6 | b | b | MAJEUR | d « ne s'est plus occupé » est correct aussi (D-1) |
| 7 | c | c | MAJEUR | explication fausse : « ai » n'est pas un auxiliaire ici (D-2) ; règle dans l'énoncé (D-6) |
| 8 | a | a | OK | 2011 T a |
| 9 | d | d | MAJEUR | c « n'ai plus » est correct aussi (D-1) ; explication fausse (« auxiliaire », D-2) |

**Bilan : 53 questions re-résolues, 0 clé fausse.** Toutes mes réponses à l'aveugle égalent la clé.

## 2. Défauts classés

### Critiques

Aucun : pas de clé fausse, pas d'explication qui contredit la clé.

### Majeurs

**D-1 — m012 Q1, Q5, Q6, Q9 : un distracteur est une négation juste.** Les énoncés demandent « la
forme négative » ou « nier correctement », sans exiger le même sens. Or « n'était jamais fier »,
« ne s'est plus occupé », « n'ai plus confiance » et « ont continué à ne pas partager » sont des
phrases négatives bien construites. Les explications de Q5, Q6 et Q9 le reconnaissent elles-mêmes
(« est bien construit, mais il dit autre chose »). Un élève qui raisonne bien peut les défendre.
Correctif : remplacer le distracteur par une faute de construction. Les longueurs sont vérifiées par
script : la clé n'est jamais strictement la plus longue.

- Q1 d → `Au lycée, Antoine et Charles ne pas ont continué à partager les mêmes activités.` (80 ;
  clé 79). Explication, dernière proposition → « ne pas ont continué » place les deux mots avant
  l'auxiliaire au lieu de l'encadrer.
- Q5 c → `Khalid était pas fier de son jardin.` (36 ; clé 38), `misconceptionTag`
  `fr.phrase.ne-oublie`. Fin d'explication → « « était pas fier » oublie le « ne ». »
- Q6 d → `Khalid se n'est pas occupé de ses plantes.` (42 ; clé 42 ; c 42), muet. Fin d'explication
  → « « se n'est pas » glisse le « ne » entre le pronom et l'auxiliaire : il se place devant le
  pronom. »
- Q9 c → `J'ai pas confiance en toi.` (26 ; clé 29), `fr.phrase.ne-oublie`. Explication complète
  (corrige aussi D-2) : « Le verbe conjugué est « ai » : la négation l'encadre, « n'ai pas ».
  « ne pas ai » place les deux mots avant le verbe au lieu de l'encadrer ; « confiance pas » met
  « pas » après le nom ; « J'ai pas » oublie le « ne ». « confiance » n'a pas d'article : il reste
  tel quel après « pas ». »

**D-2 — m012 Q7 et Q9 : explication fausse.** Dans « J'ai de la chance » et « J'ai confiance en
toi », « ai » est le verbe avoir employé seul, pas un auxiliaire. Q7, début d'explication →
« La négation encadre le verbe conjugué (« n'ai pas ») et l'article partitif « de la » devient
« de » : « pas de chance ». » (la suite est inchangée). Q9 : voir D-1.

**D-3 — m009 Q9 : données inventées sous l'étiquette d'examen.** Seule la phrase a (adaptée) vient de
2010 T. Les phrases b (« Gabriel sourit… »), c (« Le client part sans payer… », qui contredit le
texte) et d sont écrites par l'auteur. Correctif, fidèle à la phrase officielle et en 2×2 (vote
muet : chaque mot occupe deux fois chaque trou) :

- prompt : `(Examen 2010 technique) Phrase : « Le client mange le morceau de pain ___ lui donne Gabriel et le remercie ___ il l'a trouvé très bon. » Quels mots complètent les deux trous, dans l'ordre ?`
- options : a `que, puis parce que` (19, **clé**) · b `parce que, puis que` (19) · c `que, puis que`
  (13) · d `parce que, puis parce que` (25). Distracteurs muets.
- explication : `Dans le premier trou, le mot reprend « le morceau de pain », COD de « donne » (le sujet « Gabriel » est placé après le verbe) : c'est le pronom relatif « que ». Dans le second, « il l'a trouvé très bon » donne la raison du remerciement : il faut la conjonction de cause « parce que ».`

Le sujet inversé justifie le d3.

**D-4 — m011 Q6 : la question ne se lit pas seule.** « Au bout de la même phrase » renvoie à Q5, et
le donjon tire au hasard. Prompt → `(Examen 2016 générale) Dans « Un mur s'était subitement dressé
autour de l'enfant. », on enrichit « l'enfant » par une proposition relative introduite par
« qui ». Quel groupe nominal convient ?` (options inchangées).

**D-5 — m010 Q8, Q9 (et le titre) : la concession.** Le cours du 02 la range dans « 🚀 Pour aller
plus loin (hors programme de 9e) » et dit qu'elle n'est « pas évaluée ». La fiche programme ne nomme,
pour le 02, que le temps, le lieu, la cause, la conséquence et le but. Le 05 (après le 02) enseigne
« bien que » + subjonctif. Or les examens 2003 et 2007 la posent. Deux issues :

- **(recommandée) une ligne de cours au 02.** Dans la boîte 🚀, remplacer la phrase
  `_« **Bien qu'il** **soit** blessé, il continue »_ et _« **Même s'il** pleut, il partira »_ expriment la **concession** : un obstacle qui n'empêche rien.`
  par `_« **Même s'il** pleut, il partira »_ exprime une concession au futur.` Remplacer aussi
  « deux tours » par « des tours ». Puis ajouter, à la fin de la section « 🎯 L'expression du but »,
  après son `::: retenir` :
  `> 💡 **La concession** (examens 2003 et 2007) : un fait qui aurait dû en empêcher un autre ne l'empêche pas. Phrase simple : **malgré** + nom (_« **Malgré** le vent, il sort »_) ; phrase complexe : **bien que** + **subjonctif** (_« **Bien que** le vent **souffle**, il sort »_).`
  `resume.md`, fin de la puce « But » : `Concession : malgré + nom ; bien que + subjonctif.`
- sinon, déplacer Q8–Q9 au 05 ou les retirer, et ôter « et la concession » du titre.

Avec la ligne de cours, un défaut mineur demeure : l'énoncé de Q8 affiche « Bien que le règlement
**soit** sévère », modèle du mode que Q9 demande. On peut le laisser, puisque c'est la donnée
officielle.

**D-6 — Notions données dans l'énoncé parce que le cours ne les enseigne pas** (point signalé par
l'auteur). Le cas est le même partout : la règle est posée puis appliquée aussitôt, donc l'énoncé
désigne la clé, et un rappel de Q4 sert aussi Q7 (et inversement). **Pour les quatre notions, une
ligne de cours vaut mieux qu'un rappel**, et pour les relatifs composés c'est même un manque du
cours : la fiche programme (`programme/9eme-base/francais.md`, l. 86, 258, 302, 421) inscrit
« pronoms relatifs composés » au chapitre 02, que le tableau du cours ignore.

1. **Relatifs composés (m008 Q1, Q3, Q5) → cours.** Dans le tableau de « ⚡ La subordonnée relative »,
   après la ligne « préposition + qui », ajouter :
   `| préposition + **lequel** (_auquel_, _duquel_…) | complément prépositionnel, surtout une chose | La chaise _sur laquelle il s'assoit_. |`
   Après le `::: propriete` existant de la section, ajouter :
   ```
   ::: propriete
   **Lequel** est un pronom relatif **composé** : il suit une préposition et s'accorde avec
   l'antécédent — _lequel, laquelle, lesquels, lesquelles_. Avec **à** et **de**, il se soude :
   _à + lequel_ → **auquel**, _à + lesquels_ → **auxquels**, _à + lesquelles_ → **auxquelles** ;
   _de + lequel_ → **duquel**, _de + lesquels_ → **desquels**, _de + lesquelles_ → **desquelles**
   (mais _à laquelle_, _de laquelle_). Cas-limite : après une locution qui finit par _de_ (_près
   de_, _au milieu de_), on garde la locution — _la maison **près de laquelle** j'habite_ —,
   jamais _dont_.
   :::
   ```
   `resume.md`, puce « Relative », avant le point final : `; **lequel** composé après une préposition, accordé et soudé (auquel, duquel…)`.
   Les exemples évitent les données du lot (spectacle, endroit, peines). Puis on retire les
   rappels :
   - Q1, début du prompt → `(Examen 2018 générale) Phrases de départ : …` (sans la phrase
     « Rappel : … ») ;
   - Q3 → `(Examen 2009 générale) Phrases de départ : …` (sans le rappel) ;
   - Q5 → `(Examen 2008) Phrase de départ : …` (sans le rappel).
2. **« car » et « donc » (m009 Q7) → cours.** Ils sont enseignés au 08, qui vient après. Une ligne au
   02 suffit, car ce sont les équivalents des subordonnants que le 02 enseigne. Après le
   `::: propriete` de « 🔥 L'expression de la cause » :
   `> 💡 _Car_ et _donc_ ne sont pas des subordonnants : ces **mots de liaison** (chapitre 8) relient deux propositions. _Car_ annonce la **cause** de ce qui précède (_« Il resta, **car** il pleuvait »_) ; _donc_ en annonce la **conséquence** (_« Il pleuvait, **donc** il resta »_).`
   `resume.md`, puce « Cause », en fin : `; car (cause) et donc (conséquence) sont des mots de liaison, pas des subordonnants.`
   Q7, prompt → `(Examen 2013 technique) Phrases : « Au Guatemala, beaucoup de familles vivent dans la pauvreté, ___ leurs enfants sont souvent obligés de travailler. » et « Juan a pu apprendre à lire ___ il est courageux. » Quels mots complètent les deux trous, dans l'ordre ?`
   Ce prompt rétablit aussi la phrase officielle (D-11).
3. **Article → « de » après la négation (m012 Q4, Q7) → cours.** Au 01, section « ✋ Forme affirmative
   et forme négative », après le `::: propriete` existant, ajouter :
   ```
   ::: propriete
   Après la négation, l'article **un, une, des** ou **du, de la, de l'** devant le COD devient
   **de** (_d'_ devant une voyelle) : _« Il a **une** voiture »_ → _« Il n'a **pas de**
   voiture »_ ; _« Il boit **du** lait »_ → _« Il ne boit **pas de** lait »_. Cas-limite : après
   _être_, l'article reste (_« Ce n'est **pas une** voiture »_) ; un adverbe de quantité garde son
   _de_ (_« pas **beaucoup de** temps »_) ; un nom sans article reste sans article (_« Il n'a
   **pas** faim »_).
   :::
   ```
   Puis :
   - Q4, prompt → `(Examen 2017 technique) Phrase négative : « Moi, je n'ai pas de famille. » Quelle est la phrase affirmative correspondante ?` ;
   - Q7, prompt → `(Examen 2012 technique) Quelle est la forme négative de « J'ai de la chance. » ?`
4. **Place de la négation au passé composé pronominal (m012 Q6) → cours.** Même `propriete`
   existante du 01 : après `_« La porte **n'a pas** été fermée. »_`, insérer
   `Un pronom placé devant le verbe reste **à l'intérieur** de la négation : _« Il **ne** s'est **pas** levé »_, _« Il **ne** me parle **pas** »_.`
   L'énoncé de Q6 ne contient aucune règle : rien à retirer. Ce point sert aussi Q8 (« ne me donnes
   pas »).

`resume.md` du 01, puce « Forme négative », en fin : `; un pronom devant le verbe reste dans la
négation (il ne s'est pas levé) ; devant le COD, un, une, des, du, de la → de (il n'a pas de
voiture).` Ces lignes de cours entrent dans la PR du lot (sections touchées à ré-auditer, très
courtes).

**D-7 — m009 Q4 : distracteurs éliminés à vue.** « grâce à gentil » et « grâce à il est gentil » ne
sont pas des phrases. Remplacements (longueurs : clé 54, a 57) :

- b → `Mondo est devenu l'ami de tous grâce à être gentil.` (51) ;
- d → `Mondo est devenu l'ami de tous faute de sa gentillesse.` (55).

Explication, dernière phrase → `« à cause de » jugerait cet effet négatif ; « faute de » dirait que
la gentillesse manque ; et « grâce à » se construit avec un nom, jamais avec un infinitif comme
« être gentil ».`

### Mineurs

- **D-8 — m007 Q1/Q2 (point signalé).** Garder les deux : 2024 G pose bien la même phrase avec deux
  consignes (a cause, b conséquence d'intensité), et les deux gestes sont distincts. Les questions
  ne fuient pas l'une vers l'autre : l'explication de Q2 suppose seulement la relation de cause, que
  Q1 (d2) fait trouver sans difficulté. En revanche, l'énoncé reformulé de Q2 ne redonne pas la
  phrase officielle (R1). Il ajoute « tant elle est impatiente », un marqueur d'intensité qui oriente
  vers la clé, et change « pas trop » en « à peine ». Prompt →
  `(Examen 2024 générale) Phrase de départ : « Je n'écoute pas trop son explication, pressée de tenir le violon et l'archet. » On la transforme en une phrase complexe qui exprime la conséquence liée à un degré d'intensité. Laquelle est juste et fidèle au sens ?`
  Si `content:tranche` signale alors la paire Q1/Q2, la justifier au rapport comme exercice parallèle
  voulu (même phrase officielle, consignes a et b).
- **D-9 — m007 Q10.** 2002 demandait « (CONSÉQUENCE) » sans préciser. La mission exige l'intensité,
  ce qui rend fausse « si bien que », une réponse officielle valable. Il faut déclarer la
  précision. Prompt →
  `(Examen 2002, consigne précisée) Phrases de départ : « Le garçon est impatient de parler à sa mère. » / « Il l'attend dans la rue. » L'examen demandait la conséquence ; on la veut ici liée à un degré d'intensité. Quelle phrase complexe convient ?`
- **D-10 — m007, gabarit d'intensité ×4 (Q2, Q5, Q9, Q10).** Les options ont le même plan :
  intensité juste / « si bien que » / « parce que » renversé / une quatrième erreur. Le vote trait par
  trait (présence de « tellement/si », mode indicatif) reconstruit la clé en Q2 et Q9. Ce n'est pas
  bloquant, car chaque session est citée. Piste : en Q10, remplacer a par le piège annoncé dans
  l'affectation (« si » loin de l'adjectif) :
  `Le garçon est impatient de parler si vite à sa mère qu'il l'attend dans la rue.` (79 ; clé 74).
  Fin d'explication → `« si » doit porter sur l'adjectif qui a le degré, « impatient », et non sur
  un autre mot.` (étiquette `fr.circ.consequence-intensite` à retirer de a).
- **D-11 — m009 Q7.** La phrase officielle est « Au Guatemala beaucoup de familles… », réécrite en
  « familles guatémaltèques » sans déclaration. Correction incluse dans D-6.2.
- **D-12 — m009 Q1, « bec-de-lièvre » (point signalé).** Garder le mot : c'est la donnée officielle,
  et la glose est utile, le terme étant aujourd'hui jugé blessant. Mais la glose est placée entre
  les guillemets, donc dans la citation. La sortir :
  `(Examen 2012 générale) Début d'un paragraphe : « Jeff est malheureux ___ son bec-de-lièvre. Mais, heureusement, ___ ses parents, il peut, parfois, oublier sa malformation. » (« bec-de-lièvre » : ancien nom, aujourd'hui évité, de la fente labiale.) Quelles expressions de cause complètent les deux trous, dans l'ordre ?`
- **D-13 — Titres.** m009 nomme « comme », qui n'est la clé d'aucune de ses questions →
  `🏛️ Examens 2001–2021 · dire la cause autrement : grâce à, à cause de, faute de, car, donc ⭐⭐`.
  m008 énumère des clés (« auquel, duquel, dont, à qui »). Elles sont tolérables parce que chaque
  question en offre plusieurs ; sinon `🏛️ Examens 2001–2018 · le pronom relatif selon sa fonction : simple ou composé ⭐⭐⭐`.
- **D-14 — m010 Q2 a.** « toute la marchandise » est la seule option avec « toute ». →
  `Avant de ranger la marchandise, les ouvrières vont déjeuner.` (60 ; clé 62).
- **D-15 — m011.** Q4 : la phrase officielle (« …le premier couplet qui m'a permis de devenir une
  chanteuse ») est restructurée. Écrire « Même récit (phrase simplifiée) : ». Étiquettes : Q1 d et
  Q5 c (adjectif entre virgules) exécutent exactement `fr.gn.appose-non-reconnu`, enseigné au 11 →
  les étiqueter.
- **D-16 — Étages.** m012 Q9 (même gabarit que Q5, une fois D-1 appliqué) est un d2, pas un d3. m009
  Q9 actuel est un d2 ; il redevient d3 avec D-3 (sujet inversé). m012 Q5 et Q9 restent deux items
  de même gabarit (construction de « ne… pas » autour d'un verbe simple), un par session. C'est
  tolérable, mais à éviter si une session doit tomber.

## 3. Étiquettes

Libellés relus sur `origin/main`. Chaque étiquette posée nomme exactement l'erreur exécutée :
`rapport-logique-confondu`, `consequence-intensite`, `but-meme-sujet`, `subjonctif-oublie`,
`pronom-selon-construction`, `qui-que-confondus`, `pp-avoir-avec-sujet` (02/07 Q2 c : accord avec
« direction », sujet), `rapport-temporel-confondu`, `groupe-sans-verbe-conjugue`,
`complement-nom-ou-verbe`, `ne-oublie`, `negation-sens-inexact`. Ajouts proposés : D-1 (Q5 c, Q9 c
→ `fr.phrase.ne-oublie`) et D-15 (`fr.gn.appose-non-reconnu`).

**Famille proposée « article gardé ou supprimé après la négation » (m012 Q4, Q7, Q8) : refusée en
l'état.** Seules Q4 b (« j'ai de famille ») et Q7 a/d (« pas de la chance », « pas chance »)
exécutent cette erreur. Q8 c (« beaucoup des ») est une autre erreur : « de » changé en « des »
après un adverbe de quantité, pas un article gardé après la négation. Cela fait 2 questions
distinctes, sous le seuil de 3. Garder les distracteurs muets. La famille deviendrait légitime si
une 3ᵉ question l'exécutait vraiment, une fois la ligne de cours D-6.3 posée.

## 4. Doublons, « ne pas redemander », fuites

- **« Ne pas redemander »** : respecté pour les six missions. 02/02 Q1 donne le mode pour faire
  choisir « pour que » ; m007 Q8 fait l'inverse (le subordonnant est donné, il faut choisir le mode).
  m012 Q5/Q9 appliquent la construction de la négation sans redemander la règle du quiz Q4.
  m011 Q8 reprend le geste de 11/01 Q5 (relative → adjectif), comme l'affectation le prévoit, avec
  en plus le piège de l'accord.
- **Doublons avec le publié** : 11/01 Q1–Q2 (épithète, complément du nom parmi d'autres expansions)
  ont le même cadre que m011 Q1–Q3, Q5, Q7. C'est le geste officiel de 2016 G et 2026 G, accepté.
  Aucun autre recouvrement.
- **Fuites** : aucune donnée d'une question n'apparaît dans une autre. Restent les règles posées
  dans les énoncés (D-6) et le modèle « bien que… soit » de m010 Q8 (D-5). Les explications ne
  citent que des règles du cours (faute de = manque, même sujet → infinitif), sans clé chiffrée ni
  phrase d'une autre question.

## 5. Items écartés : rien de neuf perdu ?

Le reste de chaque partie langue citée a été relu dans les transcriptions.

- **m007** : 2022 G a (but, même sujet), 2017 G (cause), 2002 (cause) et 2006 a (« parce que »)
  répètent Q1, Q3, Q6 et Q7. 2019 G c (but à compléter) n'a pas de mission, alors que l'affectation
  le gardait. C'est le geste « pour que + subjonctif » de Q4/Q8 et de 02/02 Q1 : perte nulle.
- **m008** (7 questions sur 10 prévues) : 2005 a et 2001 b répètent Q4 et Q1, et 2008 a, 2010 G a
  et 2012 G b ne demandent que des relatifs simples. **Une perte réelle : 2009 G b**, « dont »
  complément d'un nom COD (« les plaquettes de frein de la grosse Ford »). 02/04 Q2 n'en fait
  qu'analyser la fonction, et aucune question ne le fait produire. À ajouter (d3, en fin de fichier) :
  - prompt : `(Examen 2009 générale) Phrases de départ : « Une jeune dame roule à vive allure au volant de la grosse Ford. » / « J'ai changé les plaquettes de frein de la grosse Ford. » On relie les phrases par un pronom relatif, dans le même ordre. Quelle phrase est juste ?`
  - options (préfixe commun `Une jeune dame roule à vive allure au volant de la grosse Ford `) :
    a `dont j'ai changé les plaquettes de frein.` (104, **clé**) · b `que j'ai changé les plaquettes de frein.` (103, `fr.relative.pronom-selon-construction`) · c `dont j'ai changé ses plaquettes de frein.` (104, muet) · d `qui j'ai changé les plaquettes de frein.` (103, `fr.relative.qui-que-confondus`)
  - explication : `« la grosse Ford » complète ici le nom « plaquettes » : les plaquettes de la Ford. Ce complément en « de » se reprend par « dont », qui complète alors un nom et non le verbe. « que » ferait de la Ford le COD de « ai changé », qui en a déjà un ; « qui » serait sujet, alors que le sujet est « j' » ; et « ses » répète le possesseur que « dont » reprend déjà.`
  2012 G a (« dans laquelle / où ») est une perte faible : « où » est déjà posé (02/05 Q5, 11/02
  Q2), et le relatif composé l'est par Q3 et Q5.
- **m009** : 2001 b, 2009 G a et le blanc « comme » de 2012 G répètent Q4, Q3 et m007 Q6.
  2021 T b et 2019 T (« par conséquent ») recouvrent 08 quiz Q4 et 08/01 Q3, donc l'écart est
  justifié. 2009 T (que / parce que) est absorbé par Q9.
- **m010** : 2019 T c (« quand ») répète Q1 ; 2003 b (« jusqu'à l'arrivée du train ») a le même
  geste que Q7 ; 2002 (complément de temps libre) n'a pas de clé unique. 2013 G b
  (« au point qu'elle… » → « au point de se sentir… ») est le miroir de m007 Q9 : perte faible,
  aucun ajout requis.
- **m011** : seul 2022 T a est écarté, conformément au plan (R6).
- **m012** : 2017 T b (« ne poursuit pas » → affirmative) est plus simple que Q4 et fait le même
  geste ; 2023 T b et 2012 T b sont écartés conformément au plan.

**Conclusion : une seule perte à réparer, 2009 G b dans m008.**

## 6. Divers

Rampes croissantes (d2 puis d3) dans les six fichiers. En-têtes conformes à l'affectation (m009 et
m012 en d2 75/15, les autres en d3 120/30). Titres suivis des étoiles de l'étage. La ligne
`sources[]` d'examen est ajoutée, mot pour mot comme dans le plan (R8), aux `chapter.json` 01, 02 et
11. Aucune figure. Notation et langue propres, aucune faute dans les énoncés. Aucune citation longue.

## 7. Résumé

- **Clés fausses : 0 / 53.**
- **Majeurs : 7 défauts** touchant 15 questions :
  - D-1, quatre distracteurs défendables en m012 ;
  - D-2, explications « auxiliaire » fausses en m012 Q7 et Q9 ;
  - D-3, phrases inventées en m009 Q9 ;
  - D-4, m011 Q6 dépend de Q5 ;
  - D-5, concession hors programme selon le cours du 02, en m010 Q8 et Q9 ;
  - D-6, quatre notions données dans l'énoncé faute de cours, une ligne de cours pour chacune
    (texte fourni) ;
  - D-7, distracteurs absurdes en m009 Q4.
- **Mineurs : 9** (D-8 à D-16).
- **Étiquettes** : toutes exactes ; trois ajouts proposés. Famille « article après la négation »
  refusée (2 questions sur 3 requises).
- **Doublons** : aucun bloquant ; un gabarit d'intensité ×4 dans m007.
- **Perte** : 2009 G b à ajouter à m008, question fournie.
- **Verdict : à corriger avant merge.** Correctifs ciblés, aucune réécriture de mission. Les lignes
  de cours du 01 et du 02 sont à ré-auditer après pose.
