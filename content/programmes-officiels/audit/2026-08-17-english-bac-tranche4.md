# Rapport d'audit — **english-bac**, tranche 4 (chapitres 10 et 11)

> **Généré** : 2026-08-17 · **Empreinte** : `wip/content-english-bac-ch10-12@5741a1ba`.
> **Périmètre audité** : les **trois** chapitres de la tranche — 69 questions. Audit complet.
> **Méthode** : un auditeur par chapitre, contexte vierge, n'ayant écrit aucune ligne de ce qu'il
> relit, avec les onze autres chapitres en croisement. Re-résolution **à l'aveugle** de chaque clé.
> **Lecture seule — aucune correction appliquée.** Ce document est la **worklist**.

## Synthèse

| | ch.10 | ch.11 | ch.12 |
| --- | --- | --- | --- |
| clés re-résolues à l'aveugle | 23 | 23 | 23 |
| **clés fausses** | **0** | **0** | **0** |
| BLOCKER | 0 | 2 | **4** |
| MAJOR | 9 | 6 | **14** |
| items rejouant un exemple du cours (**compte LU**) | **10/23** | — | **16/23** |

## ⚠️ Ce que ces deux audits apprennent sur l'INSTRUMENT

`fragments.py` (fragments communs ≥ 20 caractères entre questions et cours) **sous-détecte le
recyclage de plus de la moitié**. Sur le chapitre 10, l'auditeur a confronté chaque item aux
exemples du cours un par un : **10 items sur 23 rejouent un exemple**, quand le scan n'en voit
que **4**. C'est précisément pourquoi l'auteur a pu croire sa passe finie.

**Conséquence pour les tranches suivantes** : un compte de fragments bas ne vaut pas quitus. Il
attrape la copie littérale, pas la reprise avec un mot changé. Deux signatures lui échappent
entièrement, et ce sont les pires :

1. **la clé ET son distracteur sont les colonnes ✓/✗ d'une même ligne du cours** — l'élève qui a
   relu le mur des pièges reconnaît la paire sans lire la grammaire. Trouvée **3 fois** au ch.10,
   **1 fois** au ch.11 ;
2. **l'item EST l'exemple du cours, avec un détail glissé** (un lieu, une date, un nom changé).
   Trouvée **2 fois** au ch.10, **1 fois** au ch.11 — dont une sur la question-porte d'un chapitre.

Seule une lecture item par item contre le cours les voit. Le scan reste utile comme filet bas,
jamais comme critère.

## Deux chiffres de brief corrigés par les auditeurs

La matière compte **12 `ordering` et 13 `matching`** — mes briefs annonçaient 7 puis 8. Un auteur
à qui l'on dit « sept existent déjà » n'a pas la même prudence que celui à qui l'on dit « douze ».

## Ce qui est acquitté

- **Droits (ch.11, le plus exposé)** : aucune phrase de l'adaptation Lamb nulle part.
- **Piège du guide (`theatre`/`theater`)** : évité au ch.10, la bonne paire est enseignée.
- **Noms propres du récit (ch.11)** : zéro occurrence dans les fichiers de questions.
- **Les quatre retouches de forme de l'orchestrateur** : validées par les deux auditeurs.
- **Aucun point de grammaire inventé** au ch.10, dont la colonne *Functions* est vide au syllabus.

## Le chapitre 12 — la forme la meilleure, le fond le pire

Clés parfaitement réparties (5/5/5/5), 0 % de clé la plus courte, deux `ordering` strictement
forcés, aucun distracteur défendable — et **16 items sur 23 (70 %) rejouent un exemple du cours**.
`01-pratique` est recyclé **6 fois sur 6**. C'est la démonstration la plus nette que les mesures de
forme et la qualité du fond sont deux axes indépendants.

Ses quatre blockers sont tous de la famille « l'item vient du cours » :
les quatre options d'un item sont **les quatre mots d'une seule phrase du cours**, avec son
classement ; une clé est **les deux titres en gras du cours mis bout à bout**, ses distracteurs
étant les non-mots que le cours énumère ; trois options sur quatre d'un autre sont **les trois
phrases d'exemple du cours**, un mot glissé dans chacune.

⚠️ **Le quatrième blocker était le mien.** En ramenant un `multi` de 8 à 6 options pour le schéma,
j'ai laissé **l'explication de la version supprimée** : elle annonçait « Four words… The four
others… Two are adjectives » pour un item devenu 3 clés / 3 distracteurs / 1 adjectif. Seule erreur
de fait délivrée à l'élève de toute la tranche, sur un item noté tout ou rien. **Corrigée le
2026-08-17.** Le fond du correctif, lui, est validé par l'audit : les trois clés sont indiscutables
et les trois distracteurs indiscutablement faux.

**Arbitrages confirmés** : mon jugement sur `attendance` (+1 caractère, faux positif de la mesure
sur une question de formation de mots) est **confirmé** — mais l'item a un autre défaut, il rejoue
le paragraphe du cours, sur la porte du chapitre. Les **deux mains** qui ont écrit ce chapitre sont
cohérentes, et la seconde est nettement la plus propre (3 items recyclés sur 6, contre 13 sur 17).

**Le geste le plus rentable, chiffré par l'auditeur** : onze constats se corrigent **entièrement
côté `cours.md`/`resume.md`**, sans toucher un seul item calibré.

---

# AUDIT — chapitre 10

# AUDIT — `content/english-bac/10-put-a-little-drama-in-your-travel/`

Auditeur : agent indépendant, n'a écrit aucune ligne du chapitre.
Périmètre : 23 questions (quiz 5 · 01-pratique 6 · 02-boss 6 · 03-revision 6).
Branche : `feat/content-english-bac-ch10-12` (worktree `wip/content-english-bac-ch10-12`).
Statut : **TERMINÉ** — 23/23 questions re-résolues à l'aveugle. 0 BLOCKER · 9 MAJOR · 12 MINOR.
Aucun fichier du corpus n'a été modifié : toutes les corrections ci-dessous sont prêtes à coller.

---

## 0. Mesures muettes — RE-MESURÉES par moi, pas reprises de l'en-tête

```
23 questions · 19 mcq + 2 multi + 1 matching + 1 ordering

1a. clé strictement la plus LONGUE : 0/19  (0 %)   — cible 0 %          OK
1b. clé strictement la plus COURTE : 4/19 (21 %)   — cible ≤ 25 %       OK global
    MAIS localement : 02-boss = 3 clés courtes sur 5 mcq (60 %)         -> MINOR-6
2.  distribution des clés : a=4 (21 %) b=5 (26 %) c=6 (32 %) d=4 (21 %)  OK
4.  fragments ≥ 20 car. partagés avec cours.md/resume.md : 23            cible 0 -> MAJOR-1..4
```

Les quatre clés « la plus courte » : `quiz#Q1`, `02-boss#Q3`, `02-boss#Q4`, `02-boss#Q5`.
Les chiffres de l'en-tête pré-existante sont exacts, je les ai recalculés.

**La passe finale annoncée par l'auteur n'a PAS été faite sur le point 6 (recyclage du cours) :
les 23 fragments subsistent, et quatre d'entre eux ne sont pas des définitions partagées mais
des EXEMPLES du cours rejoués tels quels.**

---

## 1. Ce que je retiens en priorité

Aucune clé fausse (19 QCM + 2 multi + 1 matching + 1 ordering re-résolus à l'aveugle).
**Le défaut central n'est pas la justesse : c'est que quatre items ne testent plus une
compétence mais la mémoire d'une lecture** — et deux d'entre eux sont exactement la forme que
la consigne demandait de chercher : la clé ET son distracteur sont les colonnes ✓/✗ d'une même
ligne du cours.

S'y ajoutent une fuite inter-items dans le boss (l'énoncé de Q3 contient la réponse de Q4) et
une clé d'`ordering` qui n'est pas forcée.

---

## 2. Constats

### MAJOR-1 — `03-revision` Q5 : la clé ET son distracteur sont le couple ✓/✗ du cours

**Le pire item du chapitre.** Trois recyclages empilés dans un seul item.

`cours.md`, § « The first line » :

> A biography does not open on a date. Its first line says **who the person was and why a
> stranger should read on**
> ✗ *Habib Ferjani was born in 1931 in a village that had no theatre.*
> ✓ *Habib Ferjani, born in 1931, took Tunisian theatre out of the capital.*

L'item, `content/english-bac/10-put-a-little-drama-in-your-travel/exercices/03-revision.json` Q5 :

- **l'énoncé recopie la règle sur 52 caractères** (« who the person was and why a stranger
  should read on ») — l'élève n'a plus à se souvenir du critère, on le lui donne dans l'énoncé ;
- **le distracteur `a`** = la ligne ✗ du cours, nom propre changé :
  « Leïla Mansour was born in 1928, in a town that had no company at all. »
  (moule : `Nom was born in ANNÉE, in a <lieu> that had no <X>.`)
- **la clé `c`** = la ligne ✓ du cours, nom propre changé :
  « Leïla Mansour, born in 1928, was the first woman to run a national company. »
  (moule : `Nom, born in ANNÉE, <fait notable>.`)

Un élève qui a lu le cours reconnaît les deux moules sans jamais raisonner. Correction :
**réécrire le côté COURS** (règle 6 du brief : un exemple de cours se remplace sans coût, un
item calibré non), et desserrer l'énoncé.

**Correction 1** — `content/english-bac/10-put-a-little-drama-in-your-travel/cours.md`,
§ « The first line », les deux lignes d'exemple :

`ancien texte`
```
> ✗ *Habib Ferjani was born in 1931 in a village that had no theatre.* (an opening date, and no reason to continue)
> ✓ *Habib Ferjani, born in 1931, took Tunisian theatre out of the capital.* (who he was, and why he matters)
```
`nouveau texte`
```
> ✗ *Habib Ferjani started school in Kairouan in 1938.* (an opening date, and no reason to continue)
> ✓ *Habib Ferjani spent forty years teaching a town of farmers to act.* (who he was, and why he matters)
```

**Correction 2** — `.../exercices/03-revision.json` Q5, énoncé :

`ancien texte`
`A biography does not open on its first date: its first line says who the person was and why a stranger should read on. Which of these opening lines does that job?`

`nouveau texte`
`Four pupils have written the first line of the same biography. Only one of them opens it the way a first line should. Which one?`

---

### MAJOR-2 — `quiz` Q4 : l'item EST l'exemple du cours, avec un détail ajouté

`cours.md`, § « Opening a dictionary properly », étape 2 :

> In *The company is staging the play in a shed*, the word is what the company **does**, so
> you read the verb half and ignore the five noun senses printed above it.

`content/english-bac/10-put-a-little-drama-in-your-travel/quiz.json` Q4 :

- énoncé : « The company is staging the play in a disused railway shed. » — la phrase du cours
  **mot pour mot**, avec deux mots glissés devant `shed` (37 car. de recouvrement mesurés) ;
- clé `d` : « the verb part, since staging is what the company does » — la justification du
  cours mot pour mot (21 car. : « is what the company »).

C'est la forme exacte que l'audit du chapitre 11 a trouvée deux fois : *l'item est l'exemple du
cours avec un détail ajouté*. La clé est juste ; l'item ne teste plus le choix de la moitié
d'entrée, il teste si on a lu le paragraphe. **Et c'est un item du QUIZ, donc de la porte du
chapitre (≥ 80 % pour ouvrir) : la porte s'ouvre sur une reconnaissance, pas sur une lecture.**

**Correction** (côté cours — l'item est bon, on ne le touche pas) — `cours.md` :

`ancien texte`
`In *The company is staging the play in a shed*, the word is what the company **does**, so you read the verb half and ignore the five noun senses printed above it.`

`nouveau texte`
`In *The festival stages nine plays a summer*, the word is what the festival **carries out**, so you read the verb half and ignore the five noun senses printed above it.`

*(Le tableau « The trap wall » porte déjà la même règle sous une autre forme — « Reading sense 1
of the noun for a verb » — la leçon ne perd rien.)*

---

### MAJOR-3 — `03-revision` Q3 : la phrase fautive du cours, un nom changé — et le même véhicule deux fois dans le chapitre

`cours.md`, § « What else an entry gives you » :

> When an entry prints **head for / towards sth**, it is telling you that this verb cannot
> touch its destination directly. ✗ *They were heading the station.* → ✓ *They were heading
> **for** the station.*

…et le même couple une seconde fois dans « The trap wall ».

`.../exercices/03-revision.json` Q3 reprend :

- l'entrée de dictionnaire **verbatim** : `"head for / towards sth — to move in the direction
  of"` (28 car. partagés) ;
- la phrase fautive du cours avec `station` → `ruins` : « The crowd was heading the ruins. »

L'élève qui a lu le cours a la réponse écrite en gras devant lui (`for`).

**Aggravant :** `01-pratique` Q3 utilise « the audience was heading for the ruins » — même
verbe, même nom `ruins`, même entrée de dictionnaire. **Deux des 23 items tournent autour de
`head for` + `ruins`**, tous deux tirés du même paragraphe du cours.

**Correction A** — désolidariser les deux items : `.../exercices/01-pratique.json` Q3, énoncé :

`ancien texte`
`Reading the programme you meet this line: "By eight o'clock the audience was heading for the ruins." You do not know the expression "heading for". Which word do you go looking for in your dictionary?`

`nouveau texte`
`Reading the programme you meet this line: "The two troupes rehearsed in the same hall for a fortnight." You do not know the verb "rehearsed". Which word do you go looking for in your dictionary?`

et les options (la clé reste `c`) :

`ancien texte` `a: "heading"` · `b: "was heading"` · `c: "head"` · `d: "for"`
`nouveau texte` `a: "rehearsed"` · `b: "rehearsed in"` · `c: "rehearse"` · `d: "in"`

*(L'explication demande alors deux substitutions : `head` → `rehearse`, et la dernière phrase
« qui vous dira la direction en général » → « qui vous dira le lieu en général ».)*

**Correction B** — `cours.md`, changer la phrase fautive :

`ancien texte`
`✗ *They were heading the station.* → ✓ *They were heading **for** the station.*`

`nouveau texte`
`✗ *The buses head the festival gate.* → ✓ *The buses head **for** the festival gate.*`

…et la ligne homologue du tableau « The trap wall » :

`ancien texte`
`| "They were heading the station." | *They were heading **for** the station.* | The entry's little example carries the preposition |`

`nouveau texte`
`| "The buses head the festival gate." | *The buses head **for** the festival gate.* | The entry's little example carries the preposition |`

---

### MAJOR-4 — `03-revision` Q2 : clé et distracteur `b` = les deux colonnes d'une même ligne du « trap wall »

Dernière ligne du tableau « The trap wall » de `cours.md` :

| Wrong | Right |
| --- | --- |
| "…, **but** two winters later she reopened it." | *…, **and** two winters later she reopened it.* |

`.../exercices/03-revision.json` Q2 :

- distracteur `b` : « In 1958 he took over the family printing shop, **but** three years later
  he wrote his first play. »
- clé `c` : « In 1958 he took over the family printing shop, **and** three years later he wrote
  his first play. »

Le moule est identique au caractère près — `X, but/and <N unités de temps> later <sujet> <verbe>` —
seuls le fait et l'unité de temps changent. **Deuxième occurrence dans le chapitre du motif
« clé + distracteur = les deux colonnes d'une même ligne du cours ».** Le scan lexical ne le voit
pas (aucun fragment de 20 caractères), c'est le gabarit qui fuit.

**Correction** — `cours.md`, dernière ligne du « trap wall » :

`ancien texte`
`| "…, **but** two winters later she reopened it." | *…, **and** two winters later she reopened it.* | **but** promises a contradiction that has to be really there |`

`nouveau texte`
`| "He learned the trade from his father, **but** he set up on his own." | *He learned the trade from his father, **and** he set up on his own.* | **but** promises a contradiction that has to be really there |`

…et la puce jumelle du § 4 :

`ancien texte`
`- **but** where nothing is contradicted: *She bought the old cinema, **but** two winters later she reopened it* — nothing suggests that a buyer is not expected to reopen the place.`

`nouveau texte`
`- **but** where nothing is contradicted: *He learned the trade from his father, **but** he set up on his own* — nothing suggests that a son taught by his father is not expected to open his own workshop.`

⚠️ Ne pas toucher au tableau des linkers du § 4, qui utilise « She bought the old cinema, **and**
two winters later she reopened it. » comme exemple **positif isolé** de `and` : une fois la ligne
✗ supprimée, il ne fait plus paire avec rien.

---

### MAJOR-5 — `02-boss` Q3 et Q4 : l'énoncé de Q3 contient la réponse de Q4

Les deux items consécutifs du boss travaillent sur **les mêmes données inventées** (Sundial
Players · *A Winter Night* · the old fort · Kef · 2 to 16 August · 8 dinars), et l'un donne la
réponse de l'autre.

`02-boss.json` **Q3**, énoncé :

> A festival page prints one line for each show: **"KEF — the Sundial Players in A Winter Night,
> directed by Nadia Ferchichi — the old fort — 2 to 16 August — tickets 8 dinars"**

`02-boss.json` **Q4**, question : *« Which of these lines has been lifted from the programme
itself? »* — clé `c` : **« A Winter Night — the old fort, Kef — 2 to 16 August — 8 dinars »**

Q3 a déjà **affirmé** que la ligne à tirets est ce qu'« une page de festival imprime pour chaque
spectacle ». Q4 ne demande donc plus de reconnaître un enregistrement contre de la prose : il
demande de retrouver la ligne qu'on vient de lire, avec les mêmes quatre données. Le boss compte
6 items ; il en mesure 5.

Aggravant : la clé `c` est aussi **la plus courte des quatre options** (62 car. contre 71/66/63),
et la seule sans majuscule initiale de phrase — deux indices de forme qui pointent dans le même
sens.

**Correction** — `.../exercices/02-boss.json` Q4 : changer entièrement les données, et allonger
la clé pour la sortir de la position « la plus courte ».

`ancien texte` (option `c`)
`A Winter Night — the old fort, Kef — 2 to 16 August — 8 dinars`

`nouveau texte` (option `c`)
`Ashes of a Crown — the Roman cisterns, Le Kram — 9 to 24 May — 12 dinars, students 6`

et, pour rester cohérent, les trois autres options :

`ancien texte`
`a: The play will be given at the old fort every night from 2 to 16 August.`
`b: The Sundial Players open their season at the old fort on 2 August.`
`d: Tickets for the performances at the old fort cost eight dinars.`

`nouveau texte`
`a: The play will be given in the Roman cisterns every night from 9 to 24 May.`
`b: The Rope Dancers open their season in the Roman cisterns on 9 May.`
`d: A student pays six dinars for any of the performances at the cisterns.`

*(L'explication ne cite aucune donnée nommément : elle reste valable telle quelle.)*

---

### MAJOR-6 — `03-revision` Q1 (`ordering`) : la clé n'est pas forcée

Clé : `b` (né) → `e` (apprend à dessiner de son père) → `d` (peintre de décors dans un atelier)
→ `a` (quitte l'atelier pour enseigner à l'académie) → `c` (écrit le manuel que l'académie
utilise encore).

Trois des quatre contraintes sont réellement forcées par le sens : la naissance ouvre ; on
apprend de son père avant d'être payé ; on ne quitte pas un atelier qu'on n'a pas rejoint.
**La quatrième ne l'est pas.**

`c` = « wrote the handbook **the academy still uses** ». La relative décrit un **état présent**
(« l'académie s'en sert encore »), pas le moment de l'écriture. Rien n'interdit qu'il ait écrit
le manuel du temps de l'atelier et que l'académie l'ait adopté — voire qu'elle l'ait recruté pour
cela. L'ordre `b · e · d · c · a` est donc défendable, et l'explication de l'item le concède
elle-même (« The last one is the subtlest »).

Un `ordering` est noté **tout ou rien** : une contrainte molle sur cinq éléments suffit à
sanctionner un raisonnement juste.

**Correction** — `.../exercices/03-revision.json` Q1, option `c`, ancrer explicitement la
dépendance :

`ancien texte`
`wrote the handbook the academy still uses`

`nouveau texte`
`wrote the handbook for the students of his own class`

*(La dépendance devient stricte : on n'a pas d'élèves avant d'enseigner. L'explication doit alors
lire : « The last one is the subtlest: the handbook was written for his own students, so it
belongs to the years after he began to teach, not before. »)*

---

### MAJOR-7 — `quiz` Q3 : le distracteur `a` porte un « but » concessif défendable

Question : *« In which of these pairs of notes does [but] really have that work to do? »*
Clé `b` : « trained for four years as a lawyer · never argued a single case » — contradiction
franche, la clé est juste.

Mais `a` : « left school at fifteen · found work in a printing shop the same year ».
L'anglais écrit **couramment** cette concession : *He left school at fifteen, **but** found work
in a printing shop the same year* — quitter l'école à quinze ans fait attendre des difficultés,
en trouver du travail la même année les dément. Un élève qui raisonne ainsi raisonne **juste** et
perd le point. L'explication de l'item l'écarte d'autorité (« Leaving school and finding work
belong together »), ce qui n'est pas évident.

Ce n'est pas un BLOCKER — `b` reste nettement la plus forte — mais l'item demande « really »,
donc il exige que les trois autres n'aient **aucune** lecture concessive.

**Correction** — `.../quiz.json` Q3, option `a` :

`ancien texte`
`left school at fifteen · found work in a printing shop the same year`

`nouveau texte`
`toured with the company for ten years · played in every town of the south`

*(Pure addition, aucune attente à démentir. Longueur 72 car. contre 68 : la clé `b` (63) reste
non-extrême. L'explication doit lire : « Touring for ten years and playing everywhere in the
south say the same thing twice over, as do being born in a town and growing up there, and both
call for a simple addition. »)*

---

### MAJOR-8 — `02-boss` Q6 (`multi`) : le distracteur `a` ajoute un lieu que les notes ne donnent pas

Notes : « **1946 born in Sousse** · **1964 left for Tunis to study law** · 1967 … »
Clé : cocher `b`, `c`, `e` — juste sur les trois.

Mais l'option `a` — *« In 1964 he **left Sousse** for Tunis, where he began to study law. »* — 
affirme qu'il **était à Sousse en 1964**. Les notes disent seulement qu'il y est né dix-huit ans
plus tôt et qu'il est parti pour Tunis. C'est une hypothèse de continuité, pas un fait noté, et
la règle 3 du cours (« add nothing the notes do not carry ») a été enseignée avec des exemples de
pure **arithmétique**, jamais de continuité géographique. Un élève rigoureux coche `a` — et,
dans un `multi` noté tout ou rien, perd l'item entier pour avoir appliqué la règle plus
strictement que l'auteur.

**Correction** — `.../exercices/02-boss.json` Q6, option `a` :

`ancien texte`
`In 1964 he left Sousse for Tunis, where he began to study law.`

`nouveau texte`
`In 1964 he left for Tunis, where he began to study law.`

**Durcissement recommandé dans le même item** — l'option `d` (*« after nearly thirty years at
the head of his own company »*) infère une **continuité de direction** entre 1970 et 1998 que les
notes ne portent pas davantage (fonder ≠ diriger jusqu'au bout). L'explication la défend comme
« du calcul » ; ce n'en est qu'à moitié. La rendre purement arithmétique lève le doute :

`ancien texte`
`He retired in 1998, after nearly thirty years at the head of his own company.`

`nouveau texte`
`He retired in 1998, twenty-eight years after he had founded the company.`

---

### MAJOR-9 — le chiffre réel du recyclage : **10 items sur 23**, et le boss est le plus atteint

Le scan lexical trouve 23 fragments, mais la plupart sont des **définitions** (légitimes : ce
chapitre travaille le dictionnaire). Le vrai défaut est **au gabarit**, invisible au scan.
J'ai confronté chaque item aux exemples de `cours.md` un par un. Inventaire complet :

| Item | Exemple du cours rejoué | Ce qui change | Vu par le scan ? |
| --- | --- | --- | --- |
| `quiz` Q4 | l.62 « The company is staging the play in **a shed** » | +« disused railway » | oui (37 c.) — **MAJOR-2** |
| `01-pratique` Q2 | l.158 trap wall « The troupe was restored last winter » → venue | prédicat | non |
| `01-pratique` Q3 | l.71 « head **for** » + l.161 « heading the station » | station → ruins | non |
| `01-pratique` Q4 | l.94+164 « Occupations: schoolmaster; printer; dyer » → « He worked as a X, a Y and a Z » | les 3 métiers | non |
| `02-boss` Q3 | l.25 + l.157 trap wall « Venue: *Mahdia* » → « the vaulted cellar, Mahdia » | Mahdia → Kef, cellier → vieux fort | non |
| `02-boss` Q4 | l.49 le contraste article / entrée : « The Rope Dancers · vaulted cellar, Mahdia · 4-19 June · 6 D. » | mêmes 4 champs, même ordre, données changées | non |
| `02-boss` Q5 | l.47 « *By Roger Petterson*, *Associated Press*, *Oct. 11, 2006* » | **seul le nom change** : agence et date sont verbatim | oui (34 c. sur l'explication) |
| `02-boss` Q6 | l.110-112, les **trois** lignes du tableau ✓/✗ | voir ci-dessous | non |
| `03-revision` Q2 | l.169 trap wall, ligne `but`/`and` | véhicule | non — **MAJOR-4** |
| `03-revision` Q3 | l.71 + l.161, la phrase fautive | station → ruins | oui (28 c.) — **MAJOR-3** |
| `03-revision` Q5 | l.140-141, le couple ✗/✓ du § « The first line » | nom propre | oui (52 c.) — **MAJOR-1** |

**11 lignes, 10 items distincts** (`01-pratique` Q3 et `03-revision` Q3 partagent le même
exemple). Soit **43 % du chapitre**, dans la bande des tranches précédentes (11, 12, 7 et 7
items sur 23). **Le scan de 20 caractères n'en voit que 4 sur 10** : c'est pourquoi l'auteur a
pu croire sa passe finie.

**Le boss ⭐⭐⭐ est l'exercice le plus atteint : 4 items sur 6** (Q3, Q4, Q5, Q6) rejouent un
exemple du cours. Seuls Q1 (prose → notes, direction inverse de celle du cours : bon item, tâche
neuve) et Q2 (idiome *set the stage for*, absent du cours : bon item, la compétence est testée sur
un matériau neuf) sont propres. **C'est l'exercice le plus dur qui note le plus la mémoire d'une
lecture.**

#### Le cas `02-boss` Q6 — le tableau ✓/✗ du cours restitué en entier

`cours.md` l.110-112, tableau « The notes say / You write / Verdict » :

| Le cours | L'item, option par option |
| --- | --- |
| ✓ *« He handed it on in 1981, **after thirty-two years** behind the desk. »* | `d` *« He retired in 1998, **after nearly thirty years** at the head of his own company. »* |
| ✗ *« He opened the lending library **because** the town had none. »* | `b` *« He gave up law in 1967 **because** his family had lost its money. »* |
| ✗ *« He opened the **finest** lending library on the coast. »* | `c` *« … the Carthage Players, the **finest** troupe in the country. »* |

Les trois lignes du cours, dans l'ordre, avec le même adjectif `finest` recopié. C'est la
troisième occurrence du motif « clé et distracteurs = les colonnes d'un tableau du cours », et
elle porte sur l'item le plus lourd du chapitre (`multi`, boss ⭐⭐⭐).

**Correction** — côté cours, changer les trois lignes du tableau de la règle 3 (`cours.md`) :

`ancien texte`
```
| *1949 opened the lending library · 1981 handed it on* | *He handed it on in 1981, after thirty-two years behind the desk.* | ✓ worked out — the two years say so |
| *1949 opened the lending library* | *He opened the lending library because the town had none.* | ✗ invented — no note gives a reason |
| *1949 opened the lending library* | *He opened the finest lending library on the coast.* | ✗ invented — a judgement is a fact too |
```
`nouveau texte`
```
| *1949 opened the lending library · 1981 handed it on* | *He kept the library for thirty-two years.* | ✓ worked out — the two years say so |
| *1949 opened the lending library* | *He opened the lending library to please his mother.* | ✗ invented — no note gives a purpose |
| *1949 opened the lending library* | *He opened a library the whole coast came to envy.* | ✗ invented — a judgement is a fact too |
```

*(`finest` disparaît, la structure `after N years <gérondif>` disparaît, et `because` cesse d'être
le mot-signal partagé avec l'item.)*

**Corrections des trois autres items du boss** — même principe, côté cours cette fois pour Q3/Q4/Q5,
puisque ce sont les items qui sont calibrés :

`cours.md` l.25 :
`ancien texte` `*Mahdia* is where the bus takes you; *the vaulted cellar under the fish market* is the venue.`
`nouveau texte` `*Tozeur* is where the bus takes you; *the courtyard of the old caravanserai* is the venue.`

`cours.md` l.49 :
`ancien texte` `*The Rope Dancers · vaulted cellar, Mahdia · 4-19 June · 6 D.*`
`nouveau texte` `*The Rope Dancers · caravanserai, Tozeur · 4-19 June · 6 D.*`

`cours.md` l.47 : remplacer l'agence et la date, qui sont les deux champs que `02-boss` Q5 garde
verbatim :
`ancien texte` `where it came from (**the agency**, *Associated Press*), and when it was written (**the date**, *Oct. 11, 2006*)`
`nouveau texte` `where it came from (**the agency**, *Reuters*), and when it was written (**the date**, *March 3, 2011*)`

`cours.md` l.157-158 et l.164 (tableau « The trap wall »), aligner sur les mêmes substitutions et
changer le véhicule de la ligne « troupe » :
`ancien texte` `| "The troupe was restored last winter." | *The **venue** was restored last winter.* |`
`nouveau texte` `| "The troupe seats nine hundred people." | *The **venue** seats nine hundred people.* |`

⚠️ Cette dernière substitution **entre en collision** avec `01-pratique` Q2 clé `a` (« The troupe
was built in 1927 and **holds nine hundred** »). Prendre plutôt :
`nouveau texte` `| "The troupe has stood there since 1890." | *The **venue** has stood there since 1890.* |`

---

## 3. Constats MINOR

**MINOR-1 — `venue` est enseigné trois fois dans le corpus, et déjà testé au chapitre 07.**
`05-art-shows/cours.md` l.34 (« **venue** — the place where an event is held »),
`07-walking-tour/cours.md` l.64 (« **venue** | a place where a show, a match or a concert is
held ») **et** `07-walking-tour/exercices/01-pratique.json` Q3 option `b` (« The old harbour is a
busy venue: three concerts are held there each week », avec l'explication « A venue is a place
where shows are held »). Le chapitre 10 le redéfinit une troisième fois et **cinq de ses 23 items
tournent autour de ce mot** (`quiz` Q1, `01-pratique` Q1 l2, `01-pratique` Q2, `02-boss` Q3,
`03-revision` Q4). Le mot est au programme de la leçon 8, donc il a sa place ; mais cinq items sur
un mot déjà acquis deux chapitres plus tôt, c'est du poids perdu. Suggestion : ramener à trois
items (supprimer la redite entre `quiz` Q1 et `03-revision` Q4, qui posent la même question —
« que nomme la colonne / le crédit *venue* ? » — sous deux habillages).

**MINOR-2 — `cours.md` refait le travail du chapitre 02 sur GB/US, sur le couple exact que le
02 utilise comme item.** `cours.md` § « What else an entry gives you » : « British **theatre**,
American **theater** ». Or `02-first-impressions/cours.md` l.133 donne déjà la règle `-re → -er`
avec **theatre/theater** en tête d'exemple, l.237 la reprend, et
`02-first-impressions/exercices/01-pratique.json` en fait un item complet (« Our neighbour walked
to the theatre. » → « Our neighbor walked to the theater. »). Suggestion : garder l'information
(elle est requise par l'activité 6 de la leçon) mais la rattacher explicitement, p. ex.
`ancien texte` `- **The other spelling.** A dictionary flags the form used on the far side of the Atlantic: British **theatre**, American **theater**.`
`nouveau texte` `- **The other spelling.** A dictionary flags the form used on the far side of the Atlantic — the same **-re → -er** switch you met in *First Impressions*, here met inside an entry rather than in a list: British **centre**, American **center**.`

✅ **Le piège de la source est évité.** Le guide écrit « theatre (US spelling of GB theatre » — 
graphie identique des deux côtés, parenthèse non fermée. `cours.md` et `resume.md` donnent tous
deux la bonne paire (*theatre* GB / *theater* US), **aucune clé du chapitre ne recopie l'erreur**,
et `chapter.json` la documente explicitement dans `sources[]`. Vérifié sur les 23 items.

**MINOR-3 — `03-revision` Q1 teste une compétence que le cours n'enseigne pas.** L'item demande
de reconstruire une chronologie **sans aucune date**, par dépendance logique. Le cours ne parle
d'ordre que sous la règle 2 (« the years stay in line ») et suppose partout que les notes portent
des années (« Notes normally arrive in the right sequence »). La méthode sans dates n'apparaît que
dans **l'explication de l'item** (« when they are not, you rebuild it before you write a word ») —
c'est-à-dire après coup, pour celui qui a déjà répondu. Suggestion : ajouter deux phrases à la
règle 2 de `cours.md` :
`ancien texte` `**Rule 2 — the years stay in line.** Notes normally arrive in the right sequence and your paragraph has to keep it.`
`nouveau texte` `**Rule 2 — the years stay in line.** Notes normally arrive in the right sequence and your paragraph has to keep it. When they carry no years at all, the notes still tell you their own order: a birth opens, what is learned comes before what is paid for, and a man cannot leave a place he has not yet joined. Read them for those locks before you write a word.`

**MINOR-4 — l'étape 3 du dictionnaire n'est testée par aucun item.** Le cours donne quatre
étapes ; les items testent l'étape 1 (`01-pratique` Q3, forme de base), l'étape 2 (`quiz` Q4,
moitié nom / moitié verbe) et l'étape 4 (`02-boss` Q2, idiomes classés en fin d'entrée).
**L'étape 3 — « read down the numbered senses inside your half » — n'est jamais mise à
l'épreuve**, alors que c'est celle que l'activité 7 du manuel demande littéralement (trouver
*quel sens* est employé au paragraphe 3). C'est le trou de couverture le plus net du chapitre.

**MINOR-5 — les deux `multi` du chapitre ont le même gabarit exact.** `01-pratique` Q6 et
`02-boss` Q6 : cinq options, trois clés, « Tick EVERY… », toutes deux sur des notes de biographie.
Le brief demande de varier le **type de tâche**, pas seulement le décor. Ici, ni le type ni le
décor ne varient : seul le critère de tri change (« est-ce encore une note ? » / « est-ce
inventé ? »).

**MINOR-6 — dans le boss, la clé est la plus courte 3 fois sur 5 QCM (60 %).** `02-boss` Q3
(51 c. contre 54/56/55), Q4 (62 contre 71/66/63), Q5 (51 contre 55/57/56). Le chapitre est bon
globalement (21 %, cible ≤ 25 %) mais la stratégie « prendre la plus courte » gagne dans
l'exercice noté le plus cher. Les corrections proposées en MAJOR-5 (allongement de Q4 `c`) en
règlent un tiers ; allonger de quelques mots les clés de Q3 et Q5 suffirait pour le reste.

**MINOR-7 — le correctif humain sur `02-boss` Q2 tient, mais laisse un écho.** Vérifié :
`a` (« at the side of the **wooden** stage ») reste **plausible** (un acteur attend bien au bord
du plateau) et **faux** (aucun idiome, c'est le sens 1 du nom) ✅. Il devient même l'option la
plus longue (76 c.), ce qui écarte la clé `d` (70 c.) de toute position extrême ✅. Deux réserves
sans gravité : (i) `a` et `b` portent désormais **tous deux** « wooden stage » et testent
**tous deux** le sens 1 du nom — un des trois distracteurs est redondant ; (ii) l'adjectif
« wooden » est immotivé dans `a`, il se lit comme une rustine. Alternative qui allonge sans
répéter : `nouveau texte` `The actors were already waiting in the dark at the side of the crowded stage.`

**MINOR-8 — `quiz` Q1, distracteur `d` mort.** L'énoncé **énumère** les quatre colonnes (Play ·
Troupe · Venue · Dates) ; `d` (« For which age group is the play intended? ») ne correspond à
aucune d'elles et s'élimine sans rien savoir de la leçon. Suggestion :
`ancien texte` `For which age group is the play intended?`
`nouveau texte` `Which company's name is printed on the poster?`
*(faux — c'est la colonne Troupe — mais il faut avoir compris que « venue » ne nomme pas des gens.
L'explication doit alors renoncer à sa dernière phrase sur l'âge.)*

**MINOR-9 — `01-pratique` Q4, deux distracteurs sur trois éliminables sur la forme seule.**
L'énoncé demande « **a single sentence** » : `c` en compte quatre, `a` garde les deux-points du
fichier. Restent `b` (invention) et `d` (clé). L'item se joue à deux options.

**MINOR-10 — `03-revision` Q6, deux distracteurs faibles.** `c` (« journeys through the countries
that **ban** the internet ») et `d` (« journeys described in printed newspapers **and nowhere
else** ») sont absurdes plutôt qu'erronés : personne n'a jamais lu *cyber-* ainsi. Seul `a`
(« staff of the big computer firms ») est une vraie erreur d'élève.

**MINOR-11 — gabarit `ordering` très proche de celui du chapitre 09.**
`09-at-the-travel-agency/exercices/03-revision.json` Q1 : cinq phrases sur une même personne, à
remettre dans l'ordre des événements. `10/03-revision` Q1 : cinq notes sur une même personne, à
remettre dans l'ordre des événements. **Même position dans le fichier (Q1 du même exercice), même
longueur (5), même consigne.** Le différenciateur est réel — le 09 donne des repères temporels
explicites (« in the spring », « thirty days before departure »), le 10 les supprime — mais il est
mince pour deux chapitres consécutifs. Le corpus compte **12 `ordering` et 13 `matching`**
(recompté : le chiffre de 8 `matching` annoncé dans la consigne est sous-estimé de 5).
Le `matching` du 10, lui, est le seul du corpus à **classer un fragment dans un champ de tableau**
plutôt qu'à apparier deux listes de sens : il est bien différencié ✅.

**MINOR-12 — `03-revision` Q2 porte `difficulty: 3` dans un exercice `difficulty: 2`.** Autorisé
par le moteur, mais c'est aussi l'item le plus recyclé de l'exercice (MAJOR-4) : difficulté
annoncée haute, exigence réelle basse.

---

## 4. Points explicitement demandés — réponses

- **« La passe finale de l'auteur »** — **non faite.** Mesuré, pas supposé : les 23 fragments
  annoncés sont toujours là, et surtout **10 items sur 23 rejouent un exemple du cours**
  (MAJOR-9), dont 6 que le scan de 20 caractères ne voit pas.
- **Les trois pires fragments du scan** — tranchés un par un :
  `03-revision` Q5 (52 c.) : **coupable, le pire item du chapitre** — ce n'est pas une définition,
  c'est la règle du cours recopiée dans l'énoncé, doublée du couple ✓/✗ en clé et distracteur
  (MAJOR-1).
  `03-revision` Q4 (42 c.) : **acquitté** — « the art of inventing the steps of a dance » est la
  glose de `choreography`, dans l'**explication**, et ce chapitre travaille précisément la lecture
  d'entrées de dictionnaire. Une définition partagée est ici la matière de la leçon.
  `quiz` Q1 (39 c.) : **acquitté** — même raison (« the place where a public event is held », glose
  de `venue`, dans l'explication).
- **Le type de défaut prioritaire (clé + distracteur = colonnes ✓/✗ d'une ligne du cours)** —
  **trouvé trois fois** : `03-revision` Q5 (MAJOR-1), `03-revision` Q2 (MAJOR-4), `02-boss` Q6
  (MAJOR-9). Et **l'item qui EST l'exemple du cours avec un détail ajouté** — trouvé deux fois :
  `quiz` Q4 (MAJOR-2) et `03-revision` Q3 (MAJOR-3).
- **Le correctif humain sur `02-boss` Q2** — **il tient** : `a` reste plausible et faux, et la clé
  sort de la position « la plus longue ». Deux réserves cosmétiques en MINOR-7.
- **Point de grammaire inventé** — **aucun.** La colonne *Functions* est bien vide au UNIT OUTLINE
  p.36 (vérifié dans la fiche de programme). Le cours n'introduit aucune règle : le passé est de la
  révision consolidée, les huit linkers sont imprimés par le manuel p.76, et le schéma
  `head for sth` est présenté comme une **information d'entrée de dictionnaire** — c'est-à-dire la
  compétence même de la leçon — et non comme une règle nouvelle. ✅
- **Refait-il le travail du 09 (lettre en quatre mouvements) ?** — **non.** Aucune lettre, aucun
  mouvement épistolaire. Le seul chevauchement est le gabarit `ordering` (MINOR-11), pas le
  contenu.
- **Refait-il le travail du 02 (GB/US) ?** — **oui, dans le cours** (MINOR-2), sur le couple
  *theatre/theater* que le 02 emploie déjà comme item complet. **Non dans les questions** : aucun
  item du 10 ne teste l'orthographe américaine. Le choix de ne pas la tester est le bon ; c'est le
  paragraphe du cours qui devrait renvoyer au 02 au lieu de rejouer son exemple.
- **`ordering` / `matching`** — recensés : **12 `ordering` et 13 `matching`** dans la matière. Voir
  MINOR-11.

---

## 5. Compte final

- **Clés re-résolues à l'aveugle : 23 / 23** (19 `mcq` + 2 `multi` + 1 `matching` + 1 `ordering`).
- **Clés divergentes : 0.** Aucune clé fausse.
- **Clés fragiles : 2** — `03-revision` Q1 (`ordering` dont une contrainte sur quatre n'est pas
  forcée, MAJOR-6) et `02-boss` Q6 (`multi` dont un distracteur est défendable, MAJOR-8).
- **BLOCKER : 0** · **MAJOR : 9** · **MINOR : 12**.

Ordre de traitement conseillé : **MAJOR-9 d'abord** (il porte les corrections côté `cours.md` qui
règlent en une passe MAJOR-1, -2, -3, -4 et la moitié des items du boss), puis MAJOR-5 (fuite
inter-items), puis MAJOR-6, -7, -8 (les trois retouches d'options).

---

# AUDIT — chapitre 11

# AUDIT — `content/english-bac/11-the-winters-tale/` (23 questions)

Auditeur indépendant. **Aucun fichier du corpus modifié.** Rapport écrit au fil de l'eau.

Périmètre : `quiz.json` (5) · `exercices/01-pratique.json` (6) · `exercices/02-boss.json` (6) ·
`exercices/03-revision.json` (6) = **23 questions**.

Racine : `D:\11-coding\YahiaAcademy\campagnes-tronc-commun\wt\anglais-bac\corpus`

---

## 0. Mesures mécaniques (faites avant toute lecture de jugement)

| Mesure | Valeur | Verdict |
| --- | --- | --- |
| Items MCQ | 21 (+1 `matching`, +1 `multi`) | — |
| Clé la plus longue | 2/21 = **10 %** (dont 1 ex æquo) — **4/21 = 19 % avant les retouches du parent** | ✅ sous la barre |
| Clé la plus courte | 2/21 = **10 %** (dont 2 ex æquo) | ✅ sous la barre |
| Répartition des clés | a=4 · b=7 · c=5 · d=5 | ✅ |
| Fragments ≥ 20 car. partagés avec `cours.md`/`resume.md` | **27** | ❌ le plus haut de la tranche |
| `ordering` dans ce chapitre | **aucun** | ✅ (piste tranchée, voir §5) |
| Difficulté des questions | 1–3 partout | ✅ |
| Nombre de fichiers/récompenses conformes au brief | oui | ✅ |

La forme est saine. **Tout le problème est ailleurs** : dans le recyclage du cours et dans la
monotonie de la tâche.

### Les 27 fragments, triés

Le chiffre brut est trompeur : **27 fragments ne signifient pas 27 items défectueux**. Ils se
concentrent, et huit d'entre eux sont du bruit inévitable.

| Groupe | # | Où | Verdict |
| --- | --- | --- | --- |
| **`01-pratique` Q2 à lui seul** | **6** (47, 35, 31, 25, 20, 20) | énoncé + les 4 options + explication | 🟥 **BLOCKER-1** — l'item entier vient d'une ligne du mur des pièges |
| Glose du **climax** recopiée | 2 (43, 24) | `01-pratique` Q4 expl · `03-revision` Q6 expl | 🟨 MINOR-1 |
| Glose de **shamefully** | 2 (49, 20) | `quiz` Q5 expl + énoncé | 🟧 MAJOR-5(a) |
| Glose d'**unfaithfulness** | 1 (46) | `03-revision` Q5 expl | 🟧 MAJOR-6 |
| Glose de **beg** | 1 (29) | `01-pratique` Q5 expl | 🟧 MAJOR-5(b) |
| Tableau des **types de récits** réutilisé comme libellés d'options | 4 (40, 35, 35, 24) | `quiz` Q1, options `b`/`c`/`d` + expl | 🟨 acceptable mais réductible — voir ci-dessous |
| Reprises courtes d'un critère enseigné | 5 (29, 27, 27, 27, 22) | `quiz` Q2/Q4, `01-pratique` Q3, `02-boss` Q5, `03-revision` Q1 | 🟨 tolérable (règle 6 : « formules enseignées explicitement comme telles ») |
| **Bruit** (termes techniques, noms de tâche, tournures banales) | 8 | « historical narratives », « between two clauses », « a five-line summary », « and the ties between them », « with a connector of », « only one of them is th »… | ✅ rien à faire |

**Quatre corrections côté cours (B-1, m-1, M-5a, M-5b) font tomber 11 des 27 fragments d'un coup**,
et ce sont les quatre plus lourds. Le reste est du bruit ou de la répétition tolérée.

**Sur le groupe `quiz` Q1** : les quatre libellés d'options sont les gloses du tableau § 3 du cours,
reprises telles quelles. Ce n'est **pas** une fuite vers la clé — l'option `c` (la clé) est justement
la moins verbatim des quatre (« animals who behave like people » ≠ « animals who talk »), donc rien
ne la désigne. Mais l'item devient une lecture de tableau. Réduction possible sans rien casser :
raccourcir les trois distracteurs au nom du genre + un indice neuf.
```
b  a slice of life: one ordinary moment of ordinary living
d  a historical narrative: real people and real events of the past
```
→
```
b  a slice of life: an hour of an ordinary week, and nothing more
d  a historical narrative: named people who really lived, in a real past
```

---

## Constats

Ordre : BLOCKER, puis MAJOR, puis MINOR. Chaque constat porte un chemin, un numéro de question, et
une correction prête à coller.

---

### 🟥 BLOCKER-1 — `01-pratique` Q2 : la clé ET son distracteur sont les deux colonnes d'une ligne du mur des pièges

`content/english-bac/11-the-winters-tale/exercices/01-pratique.json` — **Q2**

`cours.md`, section « ⚠️ The trap wall », ligne 2 :

| Wrong | Right | Why |
| --- | --- | --- |
| "The fog was such thick that the ferry stayed in." | _The fog was **so** thick that the ferry stayed in._ | `such` cannot stand in front of a bare adjective |

L'item :

- option `c` (distracteur) = « The fog was such thick that the ferry stayed in **port**. » → colonne **Wrong**, mot pour mot + « port »
- option `d` (**clé**) = « The fog was so thick that the ferry stayed in **port**. » → colonne **Right**, mot pour mot + « port »
- l'explication : « such **refuses to stand in front of a bare adjective** » → colonne **Why**, quasi mot pour mot

C'est le pire cas décrit par le brief (§6) : **la clé elle-même est imprimée dans le cours**, et le
distracteur qu'il faut écarter aussi, dans la même ligne de tableau. Un élève qui a relu le mur des
pièges reconnaît la paire sans lire la grammaire. L'item ne note plus qu'une mémoire de lecture.
Mesure : 47 car. sur l'option `c`, 31 sur l'option `d`, 25 sur l'énoncé, 20 sur `a` et `b`, 35 sur
l'explication — **six fragments sur un seul item**, le record du chapitre.

**Correction — côté COURS** (l'item est bon, c'est le cours qu'on réécrit ; règle 6) :

`cours.md`, ligne du mur des pièges :

```
| "The fog was such thick that the ferry stayed in." | _The fog was **so** thick that the ferry stayed in._ | `such` cannot stand in front of a bare adjective |
```
→
```
| "The soup was such salty that nobody finished it." | _The soup was **so** salty that nobody finished it._ | `such` cannot stand in front of a bare adjective |
```

Et, dans la même passe, `cours.md` § 7 ③ conserve « The lamp was so weak… » : rien à changer là.

⚠️ Après ce remplacement, l'énoncé de l'item (« There was so a thick fog that the ferry stayed in
port. ») et ses quatre options ne partagent plus rien avec le cours.

**Verdict sur la piste « such thick » du brief** : *distracteur volontaire, pas une faute recopiée.*
`such` + adjectif nu est agrammatical en anglais (`such` veut un groupe nominal : *such thick fog*),
c'est une erreur d'apprenant extrêmement fréquente chez un francophone/arabophone, et le cours la
range explicitement en colonne **Wrong** avec sa raison. L'option `c` est donc légitime et
inéquivoquement fausse. **Ce n'est pas le distracteur qui est en cause, c'est le fait que le cours
imprime la paire complète.**

---

### 🟥 BLOCKER-2 — `03-revision` Q2 : l'item **est** l'exemple du cours, avec un nom de ville ajouté

`content/english-bac/11-the-winters-tale/exercices/03-revision.json` — **Q2**

`cours.md` § 3 :

> A writer who tells her grandmother's true journey but invents the conversations, because nobody
> wrote them down, has produced a mixture, and that is not a fault.

`resume.md` :

> (a true journey with invented conversations is a mixture, and that is no fault)

L'énoncé de Q2 :

> A writer sets down her grandmother's real journey from Gafsa to Tunis in 1956. Every date and
> every place in it is true, but she supplies the talk herself, since nobody wrote any of it down.

Même autrice, même grand-mère, même voyage, même conversations inventées, même « personne ne l'a
écrit ». Le seul ajout est *Gafsa → Tunis, 1956*. L'explication reprend jusqu'à la formule de
clôture (« and it is no fault » ← « and that is not a fault »).

Le scan à ≥ 20 caractères **ne l'attrape pas** (les mots sont réagencés) : c'est exactement le
doublon invisible à la mesure lexicale que le brief demande de chercher. Un élève qui a lu le § 3 du
cours répond sans réfléchir.

**Correction — côté COURS** (l'item est correct et bien calibré) :

`cours.md` § 3, phrase 2 :

```
A writer who tells her grandmother's true journey but invents the conversations, because nobody wrote them down, has produced a mixture, and that is not a fault.
```
→
```
A ship's log gives the dates, the ports and the weather, and never a word of what was said on deck; the novelist who builds a story on such a log has to invent the talk, and what she produces is a mixture — which is no fault at all.
```

`resume.md`, puce « Kinds of narrative » :

```
**imaginary**, **factual**, or a **mixture of the two** (a true journey with invented conversations is a mixture, and that is no fault).
```
→
```
**imaginary**, **factual**, or a **mixture of the two** (a novel built on a real ship's log, with the talk on deck supplied by the writer, is a mixture — no fault at all).
```

---

### 🟧 MAJOR-1 — `02-boss` Q2 : la question ⭐⭐⭐ rejoue le moule du cours en changeant deux noms

`content/english-bac/11-the-winters-tale/exercices/02-boss.json` — **Q2**

`cours.md` § 7 ② :

> _The old man felt great shame._ + _He did not come out of his house for a week._
> ✗ "He had so shame that he did not come out of his house for a week."
> ✓ _He was **so** ashamed **that** he did not come out of his house for a week._
>
> Keep a short list ready for the examination: _fear → frightened_, _shame → ashamed_, …

L'item :

> « The lorry driver felt great **fear**. » + « He did not leave his **cab** for a whole **hour**. »
> option `a` = « The driver **had so fear** that he did not leave his cab for a whole hour. » ← la ligne ✗
> option `c` (**clé**) = « The driver **was so frightened that** he did not leave his cab for an hour. » ← la ligne ✓

C'est le moule intégral : *felt great <nom d'émotion>* + *did not <verbe> for a <durée>*, le mauvais
essai en `had so <nom>`, la bonne réponse en `was so <adjectif> that`. Et l'adjectif attendu,
*frightened*, est **la première entrée de la liste de conversion imprimée dans le cours**. La
question ne teste plus la conversion : elle teste la mémoire d'une ligne de tableau. Le brief
appelle cela « le défaut n°1 de l'écriture parallèle » (règle 5), et il s'agit ici du **boss ⭐⭐⭐**,
c'est-à-dire de l'item qui devrait être le plus exigeant du chapitre.

**Correction — côté ITEM** (contrairement aux deux BLOCKER : ici c'est la *forme de la tâche* qui est
copiée, pas un fragment ; réécrire le cours ne changerait rien). Changer l'émotion **et** le moule
de la seconde proposition, en gardant la difficulté :

`prompt` :
```
Join these two ideas in one sentence with the pattern of this lesson: \"The lorry driver felt great fear.\" + \"He did not leave his cab for a whole hour.\" Which line is right?
```
→
```
Join these two ideas in one sentence with the pattern of this lesson: \"There was a great deal of noise in the hall.\" + \"The interpreter had to shout into the microphone.\" Which line is right?
```

options :
```
a  The driver had so fear that he did not leave his cab for a whole hour.
b  The driver felt so a great fear that he did not leave his cab for an hour.
c  The driver was so frightened that he did not leave his cab for an hour.      (clé)
d  The driver was so frightened, so he did not leave his cab for an hour.
```
→
```
a  The hall had so noise that the interpreter had to shout into the microphone.
b  The hall was so noisy, so the interpreter had to shout into the microphone.
c  The hall was so noisy that the interpreter had to shout into the microphone.   (clé, inchangée en position)
d  The hall was so noising that the interpreter had to shout into the microphone.
```

`explanation` : remplacer « felt fear becomes was frightened » par « a great deal of noise becomes
was noisy », et le reste tient tel quel — sauf la phrase sur « its article dragged along behind so »,
qui disparaît avec l'option `b` (voir MINOR-4, distracteur mort).

⚠️ *noise → noisy* n'est **pas** dans la liste imprimée du cours (fear/shame/anger/joy/sorrow/
surprise/tiredness) : la conversion doit donc être faite, pas récitée. C'est précisément ce qu'on
veut d'un boss.

---

### 🟧 MAJOR-2 — `quiz` Q4 : la clé se repère à un indice imprimé dans le cours, sans comprendre

`content/english-bac/11-the-winters-tale/quiz.json` — **Q4**

`cours.md` § 4, encadré ⚠️ :

> The problem happens **once**, and the text usually marks it: _one autumn_, _one night_, _that Tuesday_.

L'énoncé de Q4 : le récit est bâti sur le même patron que le récit d'exemple du § 4 du cours
(*deux familles d'un village, une ressource partagée, une habitude « every morning / for years », une
rupture datée, une querelle, une résolution faite « together »*) — et **la seule option datée est la
clé** : « the **July night** on which the old well gave out ». L'explication l'admet en toutes
lettres : « the text marks it with a date: one July night ».

Un élève qui a mémorisé la liste *one autumn / one night / that Tuesday* coche l'option contenant
« one … night » sans lire le reste. La question note la reconnaissance d'un signal, pas la notion.

**Preuve interne que le chapitre sait faire autrement** : `02-boss` Q4 pose la même notion et y
place, lui, **un événement daté qui n'est pas le problème** (« Last month the co-operative gave him
a certificate »). L'élève y est obligé de raisonner. Le quiz, non.

**Correction — côté ITEM** : dater plusieurs événements, pour que la date cesse d'être le
discriminant.

`prompt` :
```
Here is a whole story in four sentences. \"Every morning the women of the village filled their jars at the old well. One July night the well ran dry. For a week the families argued about whose new orchard had drunk the water. In the end they dug a second well together and shared it.\" Which moment is the problem — the one event without which there would be no story at all?
```
→
```
Here is a whole story in four sentences. \"Every morning for sixty years the women of the village filled their jars at the old well. One July night the well ran dry. On the Friday after that the families began to argue about whose new orchard had drunk the water. In September they dug a second well together and shared it.\" Which moment is the problem — the one event without which there would be no story at all?
```

options :
```
a  the women filling their jars there each morning
b  the families arguing for a week over the orchard
c  the digging of a second well by the two sides
d  the July night on which the old well gave out      (clé)
```
→
```
a  the sixty years in which the women filled their jars
b  the Friday on which the families began to argue
c  the September digging of a second well by both sides
d  the July night on which the old well gave out       (clé, inchangée)
```

`explanation`, phrase 1 :
```
The problem is the single occasion that breaks a state of affairs which had been holding until then, and the text marks it with a date: one July night.
```
→
```
The problem is the single occasion that breaks a state of affairs which had been holding until then. Three of the four moments here carry a date, so a date settles nothing: what settles it is that only one of them turns a calm into a trouble.
```

(Longueurs après réécriture : a=51, b=48, c=54, d=45 — la clé reste la plus courte de 3 caractères,
ce qui est acceptable ; à 10 % de « plus courte » sur le chapitre, la marge existe. Si l'on veut la
supprimer : `d` → « the July night on which the old well finally gave out » = 53.)

---

### 🟧 MAJOR-3 — `02-boss` Q1 : l'explication n'explique pas le piège sur lequel l'item est bâti

`content/english-bac/11-the-winters-tale/exercices/02-boss.json` — **Q1** (`multi`)

Option `e` : « The wind on the terrace was so cold **that** evening! »

C'est le piège le mieux construit du chapitre : la chaîne « so cold that » y figure, mais *that* est
un **déterminant** du groupe temporel *that evening*, pas la conjonction du patron. La clé
(`a` + `c`) est juste, l'option `e` est inéquivoquement fausse — **il n'y a pas de seconde bonne
réponse**, j'ai vérifié : après ce *that* il n'y a ni sujet ni verbe, seulement un nom.

Mais l'explication écrit :

> it is an exclamation, and that is why it needs **no that**.

Or l'élève a le mot *that* sous les yeux, dans la phrase. On lui répond que la phrase « n'a besoin
d'aucun *that* » alors qu'elle en contient un. **L'explication ne nomme jamais le piège**, donc
l'élève qui s'est trompé ne comprend pas pourquoi. Une explication qui laisse intacte l'erreur
qu'elle est censée corriger est un défaut, pas une coquille.

**Correction — `explanation`, dernière phrase :**

```
And the terrace sentence does measure a degree, but it stops there and never says what the cold brought about — it is an exclamation, and that is why it needs no that.
```
→
```
And the terrace sentence does measure a degree, but it stops there and never says what the cold brought about: it is an exclamation. The word that does appear in it, and that is the trap — it belongs to the time expression that evening, in the sense of on that evening. A real that of this lesson is followed by a clause with its own subject and its own verb, and evening is only a noun.
```

---

### 🟧 MAJOR-4 — cinq items de vocabulaire sur un seul moule (doublon de GABARIT, interne au chapitre)

Fichiers : `quiz.json` Q2, Q5 · `exercices/01-pratique.json` Q5, Q6 · `exercices/03-revision.json` Q4

Les six mots de l'encadré **MY NEW WORDS** sont balayés un par un, et **cinq** le sont avec la
tâche strictement identique : *une mini-situation contenant le mot* + *« What does that tell you ? »
/ « Which reading is right ? »* + *quatre gloses dont une est celle du cours.*

| Item | Mot | Tâche |
| --- | --- | --- |
| `quiz` Q2 | send for | mini-situation → quelle glose |
| `quiz` Q5 | shamefully | mini-situation → quelle glose |
| `01-pratique` Q5 | beg | mini-situation → quelle glose |
| `01-pratique` Q6 | rule | mini-situation → quelle glose |
| `03-revision` Q4 | evil | mini-situation → quelle glose |
| `03-revision` Q5 | unfaithfulness | *(variante : dans quelle phrase le mot est-il bien employé)* |

C'est le décor qui change, pas la tâche (brief, règle 5). Cinq items sur vingt-trois — **22 % du
chapitre** — ne demandent qu'une seule opération mentale. Aucune mesure lexicale ne le voit : les
six mots sont différents, les six situations aussi.

**Correction — convertir deux des cinq en une tâche différente.** Deux directions non encore
utilisées dans le chapitre, et qui n'existent pas non plus dans le manuel (l'activité 3 p.80 est déjà
un appariement mot↔définition : ne pas la rejouer) :

**(a) sens inverse — la production.** `01-pratique` Q6 (`rule`) :

```
prompt : A history of a small island prints this line: \"That family ruled the island for three generations.\" What does the sentence tell you the family did?
```
→
```
prompt : A history of a small island needs one verb: the family it describes governed the island and made its laws for three generations. Which word does the historian write in the blank? \"That family ___ the island for three generations.\"
```
options :
```
a  owned      →  a  owned the island and everything grown on it
b  governed the island and made the laws it lived by  (clé)  →  b  ruled
c  defended   →  c  guarded
d  measured   →  d  surveyed
```
(Options réécrites à longueur comparable ; la clé `b` = « ruled » reste en `b`.)

**(b) chasse à l'erreur.** `03-revision` Q4 (`evil`) — la tâche devient *repérer le mot mal employé*
au lieu de *choisir la bonne glose*, et l'item couvre alors quatre mots au lieu d'un :

```
prompt : A tale calls one of the king's counsellors an evil man. Which reading of the word is the right one?
```
→
```
prompt : Four sentences taken from pupils' summaries. In one of them a word of this lesson has been given a job it cannot do. Which sentence has to be sent back?
```
options :
```
a  The prisoner begged the guard for a blanket, and asked again at every hour.
b  The queen ruled the kingdom herself while her husband was away at the war.
c  The counsellor sent for the physician as soon as the fever rose in the night.
d  The little prince was so evil after his mother was taken that he would not eat.   ← clé
```
`explanation` : *evil* ne dit pas la détresse mais la méchanceté voulue ; l'élève cherchait un mot
comme *miserable* ou *sorrowful*. Les trois autres emplois sont exacts.

⚠️ Deux contrôles à refaire par l'auteur avant de coller : **(i)** rééquilibrer les longueurs (dans
la rédaction ci-dessus la clé `d` est la plus longue de 2 caractères) ; **(ii)** vérifier que
`d` ne dérive pas vers le corrigé du guide — c'est pourquoi la fin est « would not eat » et non
« stopped eating », qui reprendrait 21 caractères de la clé p.23 (« The little prince was so sad
that he **stopped eating**. »). Vérifié : « stopped eating » n'apparaît nulle part dans le chapitre
aujourd'hui.

**Bénéfice secondaire** : `d` réemploie `so … that`, donc l'item continue de faire travailler le
point de langue officiel tout en changeant de tâche.

---

### 🟧 MAJOR-5 — `quiz` Q5 et `01-pratique` Q5 : la clé est la glose du cours, mot pour mot

Deux items où le fragment ≥ 20 car. **atteint l'option correcte**, pas seulement l'explication.
C'est la limite de la tolérance du brief (« hors formules enseignées explicitement comme telles ») :
une définition répétée dans une *explication* passe encore, la même définition **dans la clé** ne
passe pas, parce qu'elle rend la clé reconnaissable sans la notion.

**(a) `quiz.json` Q5** — 49 caractères, le plus long fragment du chapitre.

`resume.md` : « **shamefully** (in a way that brings disgrace on the one who acts) »
`cours.md` : « in a way that brings disgrace on the person who acts »
option `b` (**clé**) : « that the treasurer **acted in a way that brought him disgrace** »
`explanation` : « to act shamefully is **to act in a way that brings disgrace on the one who acts** »

Correction — **côté cours et résumé** (l'item est bon) :

`cours.md`, tableau « My new words », ligne *shamefully* :
```
| **shamefully** | in a way that brings disgrace on the person who acts | _The steward behaved shamefully in front of the guests._ |
```
→
```
| **shamefully** | so badly that the people who saw it were ashamed for him | _The steward behaved shamefully in front of the guests._ |
```
`resume.md`, puce « My new words » :
```
**shamefully** (in a way that brings disgrace on the one who acts)
```
→
```
**shamefully** (so badly that those who saw it were ashamed for him)
```

**(b) `01-pratique.json` Q5** — 29 caractères sur l'explication, et une reprise sémantique dans la clé.

`cours.md` : « **to beg** is stronger than _to ask_ — **it is the word for someone** with **nothing left to bargain with** »
option `c` (**clé**) : « he asked over and over, in real need, **with nothing to offer** »
`explanation` : « **it is the word for someone** who has run out of everything else »

Correction — **côté cours** :
```
And note that **to beg** is stronger than _to ask_ — it is the word for someone with nothing left to bargain with.
```
→
```
And note that **to beg** is stronger than _to ask_: it belongs to a person whose only argument is his need.
```

---

### 🟧 MAJOR-6 — `03-revision` Q5 : la clé se reconnaît à son sujet, pas à son vocabulaire

`content/english-bac/11-the-winters-tale/exercices/03-revision.json` — **Q5**

```
a  The unfaithfulness of the old clock made the whole household late.
b  The porter's unfaithfulness kept him in the same house for forty years.
c  The unfaithfulness of that summer's weather ruined the year's harvest.
d  The king had his queen shut away for unfaithfulness, and heard no one.   ← clé
```

Trois options parlent d'une horloge, d'un portier et de la météo. **La quatrième est le seul énoncé
qui parle du conte que l'élève vient de lire** — et c'est la clé. Un élève qui ne connaît pas le mot
la choisit à coup sûr : c'est la seule qui « ressemble à la leçon ». La clé se repère à son thème,
ce qui est la règle 1 du brief déclinée au contenu et non plus à la longueur.

S'y ajoute que les trois distracteurs sont invraisemblables au même degré (aucun locuteur n'écrit
« the unfaithfulness of the old clock »), ce qui rend l'item très facile pour un item de révision ⭐⭐.

**Correction — remplacer un distracteur pour qu'il partage le registre humain de la clé, et sortir
la clé du conte :**

```
b  The porter's unfaithfulness kept him in the same house for forty years.
d  The king had his queen shut away for unfaithfulness, and heard no one.
```
→
```
b  The clerk's unfaithfulness to the ledger cost the firm four thousand dinars.
d  She forgave his unfaithfulness, and the two of them stayed married thirty years.
```
(`d` reste la clé. Longueurs : a=66, b=77, c=70, d=79 — remonter `a` à ~74 :
« The unfaithfulness of the old kitchen clock made the whole household late. » = 74.)

**Correction du fragment de 46 car. (3ᵉ pire du chapitre)** — celui-ci est dans l'`explanation`,
donc c'est l'explication qu'on réécrit, pas le cours : la glose est bonne et vaut d'être apprise
telle quelle.

```
In the vocabulary of this lesson the word names one thing only: being untrue to the person you are married to.
```
→
```
In the vocabulary of this lesson the word names one thing only, and it is a thing that happens inside a marriage: a husband or a wife who breaks the promise they made.
```

---

### 🟨 MINOR-1 — définition du climax recopiée à l'identique dans deux explications

`01-pratique` Q4 (43 car.) et `03-revision` Q6 (24 car.) reprennent la glose du § 4 du cours :
« the highest point of the tension, where **matters must now turn one way or the other** ».

Une réécriture **côté cours** règle les deux d'un coup :

`cours.md` § 4, tableau, ligne *climax* :
```
| **climax** (or **crisis**) | the highest point of the tension, where matters must now turn one way or the other |
```
→
```
| **climax** (or **crisis**) | the peak of the tension: after it the story can go one way or the other, but it cannot stay where it is |
```

---

### 🟨 MINOR-2 — `02-boss` Q3 : l'option `c` invente des détails que le récit ne contient pas (défaut préexistant, aggravé d'un cran par la retouche)

`content/english-bac/11-the-winters-tale/exercices/02-boss.json` — **Q3**, option `c`

**La retouche du parent atteint son but** : avant, la clé `b` (189 car.) était la plus longue
(a=178, c=180, d=166) ; après l'ajout de « , each one dated in pencil », `c` monte à 206 et la fuite
de forme disparaît. `c` reste faux, la clé reste unique. ✅

Mais le défaut de fond **préexistait à la retouche** et n'a pas été vu :

1. le récit source ne dit **nulle part** que les montres en or étaient rares dans cette ville, ni que
   des fiches de réparation étaient pliées dans les vitrines — il dit qu'**une** fiche était pliée
   dans **la montre**. Ces deux inventions étaient déjà dans la version d'avant
   (`git show HEAD~1` : « Gold watches were rare there, and repair slips were folded into the
   cases. ») ; la retouche en a ajouté une troisième (« each one dated in pencil ») ;
2. l'`explanation` est donc inexacte sur l'option qu'elle décrit : elle affirme que `c`
   « keeps the small pleasures **of the text** », alors que `c` invente ;
3. et `c` empiète sur le défaut que `d` est là pour illustrer (ajouter ce que le texte n'a pas dit),
   ce qui brouille la leçon des deux distracteurs.

Ce n'est pas bloquant (pas de seconde clé), mais l'item perd la netteté de ses trois erreurs.

**Correction — allonger `c` avec un détail qui EST dans le texte :**
```
A watchmaker worked eleven years in a shop no wider than a door, in a town with a museum and glass cases. Gold watches were rare there, and repair slips were folded into the cases, each one dated in pencil.
```
→
```
A watchmaker worked eleven years in a shop no wider than a door, in a town that had a museum with glass cases in it. The watch he kept was gold, and the repair slip that went with it was still folded up inside the case.
```
(206 → 216 car. ; la clé `b` reste à 189, donc pas la plus longue. « Gold watches were rare there »,
également absent du récit, disparaît au passage.)

---

### 🟨 MINOR-3 — `02-boss` Q6 : la retouche du parent est valide, mais paie en vocabulaire hors leçon

`content/english-bac/11-the-winters-tale/exercices/02-boss.json` — **Q6**, option `a`

« before dawn » → « **before first light** ». Vérifié : l'option reste **vraie** (le passage dit
« refused to cross before dawn », et *first light* ≈ *dawn*), donc toujours **pas** la réponse
attendue, et elle reste plausible. La clé `c` (55) n'est plus la plus longue (a=60). **La retouche
tient.**

Réserve : *first light* n'appartient ni au lexique de la leçon ni au GRAMMAR REFERENCE, et l'item
teste la **prise de notes**, pas le vocabulaire. On ajoute une charge lexicale étrangère à la
compétence mesurée, sur l'exercice le plus dur du chapitre. Substitut de même longueur qui ne coûte
rien :
```
a  the ferryman — refused to cross the water before first light
```
→
```
a  the ferryman — would not take the boat across before dawn
```
(59 car. ; la clé `c` reste à 55, donc toujours pas la plus longue.)

---

### 🟨 MINOR-4 — `02-boss` Q2 : un distracteur mort

Option `b` : « The driver felt **so a great fear** that… ». Aucun apprenant ne produit *so a great* :
la faute réelle est *such a great fear* (qui, elle, serait **correcte** en anglais — donc à ne
surtout pas mettre) ou *so great a fear* (correcte aussi, littéraire). L'option s'élimine sans rien
savoir de la leçon, et l'explication la commente comme « its article dragged along behind so »,
description d'une erreur qui n'existe pas.

Traité par la réécriture proposée en **MAJOR-1** (nouvelle option `d` : *so noising*, confusion
`-ed`/`-ing`, qui est, elle, une erreur d'apprenant documentée). Si l'on ne retient pas MAJOR-1,
remplacer seulement `b` :
```
b  The driver felt so a great fear that he did not leave his cab for an hour.
```
→
```
b  The driver was so frightening that he did not leave his cab for a whole hour.
```

---

### 🟨 MINOR-5 — `03-revision` Q4 : la clé teste un trait que le cours n'enseigne pas

`cours.md`, tableau « My new words » : « **evil** | deeply and deliberately cruel; doing harm on
purpose ». **Aucune mention du remords.**

Option `a` (**clé**) : « he does harm on purpose, **and is not sorry for it afterwards** »
`explanation` : « two things make it strong: the harm is deliberate, **and there is no regret behind
it** ».

Le second critère de la clé n'est enseigné nulle part — ni dans `cours.md`, ni dans `resume.md`
(brief : « Le cours enseigne tout ce que le quiz et les exercices testent — sans exception »). La
clé reste la seule réponse possible (les trois autres sont clairement fausses), donc ce n'est pas
bloquant, mais l'item s'appuie sur un critère non transmis.

**Correction — côté cours** (formulée pour ne pas créer un nouveau fragment ≥ 20 car. avec la clé) :
```
| **evil** | deeply and deliberately cruel; doing harm on purpose | _An evil counsellor whispered against the queen._ |
```
→
```
| **evil** | deeply and deliberately cruel: the harm is meant, and no remorse follows it | _An evil counsellor whispered against the queen._ |
```
Idem `resume.md` : « **evil** (deeply and deliberately cruel) » → « **evil** (deliberately cruel, and
without remorse afterwards) ».

---

### 🟨 MINOR-6 — `quiz` Q5 : le chapitre corrige silencieusement la clé du guide

Le guide (p.23, activité 3 p.80) glose **shamefully** par « **in an embarrassing way** ». Le
chapitre enseigne « in a way that brings disgrace on the one who acts » et, dans `quiz` Q5,
**élimine explicitement** la lecture « embarras / timidité » (option `a` : « far too shy to say a
word »).

La correction du chapitre est la bonne (*shamefully* = de façon déshonorante, pas « embarrassante »),
et le brief prévoit ce cas (« la KEY du guide comporte des corrigés faux ou décalés »). Mais un élève
qui a le corrigé du manuel sous les yeux tiendra la clé du quiz pour fausse. Un mot dans le cours
suffit à désamorcer :

`cours.md`, sous le tableau « My new words », après la note sur *send for* :
```
> 💡 **send for** is one of those verbs whose meaning is not the sum of its words: …
```
→ ajouter une phrase :
```
And take care with **shamefully**: it does not mean "in an embarrassing way". Embarrassment is a small discomfort; this word passes a judgement on what somebody did.
```

---

### 🟨 MINOR-7 — `quiz` Q5 et `quiz` Q2 : un distracteur mort chacun

- `quiz` Q5 option `d` : « that the treasurer behaved **better than anyone had hoped** » — pure
  inversion, aucun élève ne lit *shamefully* ainsi. Remplacer par une erreur réelle (confusion
  *shamefully* / *shamelessly*) :
  ```
  d  that the treasurer behaved as if he had nothing to be ashamed of
  ```
  (⚠️ à trancher par l'auteur : *shamelessly* est proche au point d'être défendable pour certains
  correcteurs. Variante plus sûre, sur la confusion adverbe/adjectif :
  `d  that the treasurer felt shame at the way the banquet had been served`.)
- `quiz` Q2 option `c` : « in the palace kitchen, where he has been **living all week** » — un médecin
  qui vit dans les cuisines du palais depuis une semaine s'écarte sans connaître l'expression.
  Remplacer par l'autre lecture fautive de *send for* (« envoyer quelque chose à ») :
  ```
  c  in the palace kitchen, where the queen's cook has just fed him
  ```

---

### 🟨 MINOR-8 — `01-pratique` Q3 : un distracteur contient un vrai verbe d'action

Option `c` : « the ship was forty years old **and had been sold twice already** ». Le critère
enseigné est « hunt the main verbs / a line earns its place only if it records something somebody
**did** ». *Had been sold twice* enregistre bien un acte (quelqu'un l'a vendue), même s'il est
antérieur au récit et sans agent. Un élève qui applique le critère mécaniquement peut le cocher.
L'option reste fausse (c'est de l'arrière-plan, pas un acte qui pousse le récit), mais le
distracteur affaiblit le critère au lieu de l'éprouver.

```
c  the ship was forty years old and had been sold twice already
```
→
```
c  the ship was forty years old and her paint was grey with salt
```
(61 car., contre 60 avant ; la clé `b` reste à 53 et n'est ni la plus longue ni la plus courte —
elle est à égalité avec `a` et `d`, ce qui était déjà le cas.)

---

### 🟨 MINOR-9 — doublon de gabarit avec le reste de la matière (deux formats non-QCM)

- `01-pratique` Q1 (`matching`, 4 citations ↔ 4 étiquettes analytiques) reprend la forme de
  `09-at-the-travel-agency/exercices/01-pratique.json` Q3 (« Match each of her sentences with the
  move it makes in her complaint »). Même travail : *rattacher un énoncé de locuteur à la catégorie
  qu'il illustre*. Le contenu diffère assez pour que ce ne soit pas bloquant, mais c'est le 13ᵉ
  `matching` de la matière et le 2ᵉ de cette forme précise.
- `02-boss` Q1 (`multi`, « Tick EVERY sentence that does that job ») est le **7ᵉ** « Tick EVERY
  sentence… » de la matière (ch. 01, 03, 04, 06, 09, 10 en ont un). C'est devenu le gabarit unique du
  format `multi` dans `english-bac`. Aucune correction proposée à l'échelle de ce chapitre — c'est
  une remarque de matière, à porter à l'arbitrage global.

---

## 1. Droits (R-2) — verdict

**Aucune phrase du texte de Lamb n'est reproduite**, nulle part : ni dans `cours.md`, ni dans
`resume.md`, ni dans un énoncé, une option ou une explication. Vérifié à la main **et**
mécaniquement contre la section de programme (encadrés verbatim, textes d'activités, clés du guide).

Points vérifiés un par un :

| Élément sous droits ou imprimé | Reproduit ? | Où en est le chapitre |
| --- | --- | --- |
| La phrase citée par le guide comme réponse attendue (act. 2 p.80, « My poor little prisoner… ») | **non** | absente du chapitre. C'était la **seule** citation tolérée : elle n'est pas utilisée. |
| Le chapeau imprimé p.78 (Charles et Mary Lamb, « tried to keep very close to the original words… ») | **non** | `cours.md` § 5 le **paraphrase** intégralement (« They stayed as close to his words as they could », « two aims at once: pleasure… moral lesson »). Reformulé, pas recopié. |
| Le récit lui-même (≈ 700 mots, p.79-80) | **non** | `cours.md` § 5 et `resume.md` en donnent un **résumé en prose neuve**. C'est ce que le brief autorise. |
| Encadré officiel « Narrative Texts » (p.77) | **non**, mais serré | `cours.md` § 1 suit l'encadré **phrase par phrase, dans le même ordre**, en reformulant chaque proposition (« organised round a plot » ← « organised around a plot » ; « a chain of episodes, arranged by the author » ← « a series of episodes … written by the author »). Aucun fragment de 20 caractères, mais la **structure** est celle de l'encadré. Encadré de manuel scolaire, pas œuvre tierce : hors R-2. Signalé pour information. |
| Liste des types de récits (act. 3 p.77) | **oui — 144 caractères verbatim** | ⚠️ voir MINOR-10 ci-dessous. |
| Phrase du GRAMMAR FOCUS p.81 (« He was so happy that he had nothing left to wish for. ») | **non** | absente. |
| Phrase de l'encadré MY GRAMMAR (« Mamillius was so unhappy that he lost his desire to eat or sleep ») | **non** | absente ; aucun item ne l'utilise. |
| Les **trois phrases combinées** du corrigé p.23 (act. 12 a/b/c) | **non, aucune n'est devenue un item** | vérifié : `a)` la reine/les recommandations → absente ; `b)` le roi jaloux/la prison → **paraphrasée dans le cours** (§ 7 ① : « The king was so jealous that he **shut his own wife away** », au lieu de « put his wife in prison » — 33 caractères communs mesurés), jamais dans un item ; `c)` le petit prince/il cesse de manger → absente. **Piste du brief tranchée : les trois corrigés ne sont pas devenus des items.** |
| Les gloses de l'appariement act. 3 p.80 (a…g) | **une sur six, verbatim** | ⚠️ voir MINOR-11 ci-dessous. Les cinq autres sont réécrites (« in an embarrassing way » ≠ « in a way that brings disgrace… » ; « having a relation with a person who is not your spouse » ≠ « being untrue to the person you are married to » ; etc.). |
| Encadré « Narrative Texts », ouverture | 30 car. | « to entertain, to tell a story » se retrouve tel quel dans `cours.md`, `resume.md` **et** `chapter.json`. Trois mots de fonction sur une définition officielle : négligeable. |
| Cinq étapes du plot (act. 2 p.77) | 50 car. dans `chapter.json` | « introduction, problem, climax or crisis, resolution » : liste de termes techniques dans l'ordre du manuel. Non protégeable, et il est normal que la description du chapitre nomme le programme. |

**Réserve non bloquante** : `cours.md` § 7 ① donne à l'élève, sous forme d'exemple, la réponse de
l'activité 12 b) du manuel. Ce n'est pas un problème de droits (phrase reformulée) et pas un problème
de règle 6 (elle n'est dans aucun item), mais cela déflore une activité que le professeur fera
peut-être en classe. À signaler à l'auteur, pas à corriger.

---

### 🟨 MINOR-10 — 144 caractères du manuel reproduits verbatim (le plus long fragment du chapitre)

`cours.md` § 3 et `resume.md`, puce « Kinds of narrative », reprennent la liste de l'activité 3 p.77
**intégralement et dans le même ordre** :

> fairy stories, mysteries, science fiction, romances, horror stories, adventure stories, fables,
> myths and legends, historical narratives, ballads, slice(s) of life, personal experience

144 caractères dans `cours.md`, 143 dans `resume.md` — **plus long que n'importe quel fragment
partagé avec le cours mesuré à l'intérieur du chapitre**. Ce n'est pas une atteinte à R-2 (le texte
en cause est une liste de noms de genres dans un manuel scolaire, pas une œuvre tierce, et le brief
autorise à enseigner « le vocabulaire… que la leçon en tire »). Mais copier **la sélection et
l'ordre** d'une liste de douze items est le geste qui se voit, et il ne coûte rien de le défaire.

**Correction** — réordonner et regrouper, ce qui améliore au passage la lisibilité :

`cours.md` § 3 :
```
The family is large: fairy stories, mysteries, science fiction, romances, horror stories, adventure stories, fables, myths and legends, historical narratives, ballads, slices of life, personal experience.
```
→
```
The family is large. Some kinds live on the marvellous — myths and legends, fairy stories, science fiction, horror; some on the ordinary — slices of life, personal experience, romances; some on a puzzle or a chase — mysteries, adventure stories; and some carry a lesson or a record — fables, ballads, historical narratives.
```
(et la même refonte, en plus court, dans `resume.md`).

---

### 🟨 MINOR-11 — une glose du corrigé du guide reproduite mot pour mot dans le cours

Corrigé du guide, act. 3 p.80, gloses : « b) **ask someone to come to you** » (→ *send for someone*).

`cours.md`, tableau « My new words » : « **to send for someone** | to **ask someone to come to you** »
`resume.md` : « **to send for someone** (**ask someone to come to you** — nothing is sent but the
message) »

28 caractères verbatim, dans les deux fichiers. Contrairement aux cinq autres gloses de la même
activité, celle-ci n'a pas été réécrite. Aucun item ne la reprend (la clé de `quiz` Q2 est « on his
way to the palace, because he has been called there »), donc la règle 6 n'est pas atteinte — mais un
élève qui a le corrigé du manuel lit la même phrase dans les deux documents.

**Correction** — `cours.md` :
```
| **to send for someone** | to ask someone to come to you | _When the fever rose, they sent for the doctor._ |
```
→
```
| **to send for someone** | to call somebody to where you are, and expect them to come | _When the fever rose, they sent for the doctor._ |
```
`resume.md` :
```
**to send for someone** (ask someone to come to you — nothing is sent but the message)
```
→
```
**to send for someone** (call somebody to where you are — nothing is sent but the message)
```

---

## 2. Piège de la source — noms propres

Le manuel hésite entre `Pauline` et `Paulina` et imprime `Proxilenes` pour *Polixenes*.

**Vérifié : aucun item du chapitre ne repose sur un nom propre du récit.** Recherche exhaustive dans
les 4 fichiers de questions :

- `Leontes`, `Hermione`, `Mamillius`, `Polixenes`/`Proxilenes`, `Camillo`, `Paulina`/`Pauline`,
  `Emilia`, `Perdita`, `Antigonus`, `Cleomenes`, `Dion`, `Sicily`, `Bohemia`, `Delphi` :
  **zéro occurrence** dans `quiz.json`, `01-pratique.json`, `02-boss.json`, `03-revision.json`.
- Les items qui touchent au conte le désignent par périphrase (`03-revision` Q5 : « The king had his
  queen shut away… ») — ce qui est exactement le bon geste.
- `cours.md` § 5 et `resume.md` nomment les personnages (Leontes, Hermione, Mamillius) mais rien
  n'est testé dessus ; les orthographes retenues sont les correctes (`Polixenes` n'apparaît pas du
  tout, le cours dit « the king of Bohemia » ; `Paulina` non plus).

✅ **Piste tranchée : rien à corriger.** Le chapitre a évité le piège, y compris dans le cours qui
contourne `Polixenes` et `Paulina` en les désignant par leur fonction.

---

## 3. `ordering` — piste tranchée

**Ce chapitre n'a pas d'`ordering`.** Ses deux formats non-QCM sont un `matching`
(`01-pratique` Q1) et un `multi` (`02-boss` Q1). La tentation évidente — remettre en ordre les cinq
étapes d'un plot, ou les épisodes du conte — **n'a pas été suivie**, et c'était la bonne décision.

⚠️ **Le chiffre du brief est périmé** : la matière ne compte pas sept `ordering` mais **douze**
(recomptés : `mcq` 236, `matching` 13, `ordering` 12, `multi` 15). Les douze sont dans les
chapitres 01, 03, 04, 05, 06 (×2), 07, 08, 09, 10, 12 (×2). Et parmi eux, **quatre** demandent déjà
de remettre des événements ou des étapes dans l'ordre où ils se sont produits :

- `01-…/02-boss` Q1 — les six étapes du processus d'écriture ;
- `08-…/03-revision` Q1 — les cinq phrases d'un e-mail dans l'ordre où elles ont été envoyées ;
- `09-…/03-revision` Q1 — les cinq phrases d'un dossier « in the order in which the events happened » ;
- `10-…/03-revision` Q1 — des notes non datées « in the order in which they must have happened ».

Un cinquième, sur les cinq étapes d'un plot, n'aurait rien ajouté au travail demandé à l'élève.

✅ Rien à corriger. À porter au crédit du chapitre — c'est le seul point de la tranche où la
tentation du gabarit a été explicitement refusée.

---

## 4. Le cours enseigne-t-il tout ce qui est testé, et l'inverse ?

**Sens 1 — testé mais pas enseigné.** Un seul écart : `03-revision` Q4, le critère « no regret »
(→ **MINOR-5**). Tout le reste est couvert : les quatre fenêtres (§ 2), les cinq étapes (§ 4), les
types de récits (§ 3), les six mots (§ 9), `so … that` sous ses quatre emplois (§ 7), la prise de
notes (§ 6), les règles du résumé et les connecteurs (§ 8, avec l'encadré ⚠️ sur *meanwhile* que
`03-revision` Q3 teste directement).

**Sens 2 — enseigné mais jamais testé.** Trois notions du cours n'apparaissent dans aucun des
23 items :

| Notion enseignée | Où | Testée ? |
| --- | --- | --- |
| « ne jamais supprimer le `that` à l'écrit » | § 7, fin + mur des pièges | ❌ jamais posée frontalement (elle n'est qu'un distracteur de `01-pratique` Q2) |
| Garder **un seul temps** dans le résumé | § 8, règle 2 | ❌ aucun item |
| Les six mots du tableau *jealousy / suspicion / oracle / heir / grief / sorrow* (§ 5) | § 5, tableau | ❌ **cinq sur six jamais testés** — vérifié par grep sur les 4 fichiers de questions : seul *suspicion* apparaît, et encore, à l'intérieur de la clé de `02-boss` Q5 (« a suspicion acted on destroys the trust… ») où il n'est pas ce qui est évalué. *heir* et *oracle*, les deux plus utiles pour lire la partie 2 du conte, sont absents des items. Seuls les six mots de **MY NEW WORDS** sont testés. |

Ce n'est pas un défaut au sens du brief (le cours a le droit d'enseigner plus qu'il ne teste), mais
c'est le meilleur gisement pour **MAJOR-4** : convertir un des cinq items de glose en un item sur
*heir* ou *oracle* réduirait la monotonie **et** comblerait le trou.

---

## 5. Bilan des clés re-résolues

| | |
| --- | --- |
| Questions dans le périmètre | **23** |
| Clés re-résolues à l'aveugle | **23 / 23** |
| Clés **divergentes** (réponse de l'auditeur ≠ `correctOption`) | **0** |
| Secondes bonnes réponses défendables trouvées | **0** |
| Distracteurs morts | **3** (`quiz` Q2 `c`, `quiz` Q5 `d`, `02-boss` Q2 `b`) |
| Distracteurs limites mais défendables | **1** (`01-pratique` Q3 `c`) |

**Aucune clé fausse.** Le contrôle particulier demandé sur `02-boss` Q1 (`multi`) confirme que
`answerKey.correct = ["a","c"]` est exact et que l'option `e` (« so cold **that** evening! ») ne peut
pas être une troisième bonne réponse : le `that` y est un déterminant, et rien ne suit qui soit une
proposition.

**Ce qui va mal dans ce chapitre n'est donc pas la justesse — c'est l'origine des items.** Deux
d'entre eux (`01-pratique` Q2, `03-revision` Q2) sont des morceaux du cours réimprimés, deux autres
(`02-boss` Q2, `quiz` Q4) en sont le moule rempli d'autres noms, et cinq exercent la même unique
opération mentale. Les 27 fragments mesurés ne sont pas un bruit de rédaction : ils sont le symptôme
de questions écrites **à partir du cours ouvert** plutôt qu'à partir de la notion.

---

## 6. Récapitulatif

| Sévérité | # | Constats |
| --- | --- | --- |
| **BLOCKER** | 2 | B-1 `01-pratique` Q2 (clé **et** distracteur imprimés dans le mur des pièges) · B-2 `03-revision` Q2 (l'item **est** l'exemple du § 3 du cours) |
| **MAJOR** | 6 | M-1 `02-boss` Q2 (moule du cours, boss ⭐⭐⭐) · M-2 `quiz` Q4 (clé repérable à un indice imprimé) · M-3 `02-boss` Q1 (l'explication n'explique pas le piège) · M-4 gabarit vocabulaire ×5 · M-5 `quiz` Q5 + `01-pratique` Q5 (la glose du cours **dans la clé**) · M-6 `03-revision` Q5 (clé repérable à son sujet) |
| **MINOR** | 11 | m-1 climax ×2 · m-2 `02-boss` Q3 · m-3 `02-boss` Q6 · m-4 `02-boss` Q2 `b` mort · m-5 `03-revision` Q4 non enseigné · m-6 `quiz` Q5 vs guide · m-7 2 distracteurs morts · m-8 `01-pratique` Q3 `c` · m-9 gabarit matière · **m-10 144 car. verbatim du manuel** · **m-11 glose du guide recopiée** |

**Les trois retouches du parent — vérifiées, aucune à annuler.** Toutes trois visaient une clé « la
plus longue » et l'ont bien supprimée (chapitre passé de 19 % à 10 %) :

| Retouche | Avant → après | Clé toujours juste ? | Distracteur toujours faux et plausible ? | Verdict |
| --- | --- | --- | --- | --- |
| `02-boss` Q3 `c` (+ « , each one dated in pencil ») | clé `b` 189 était la plus longue (c=180) → c=206 | ✅ | faux ✅, plausible ✅ | ⚠️ valide, mais approfondit une invention préexistante — **m-2** |
| `02-boss` Q6 `a` (« before dawn » → « before first light ») | clé `c` 55 était la plus longue (a=53) → a=60 | ✅ | l'option reste **vraie** (donc reste un bon leurre) ✅ | ⚠️ valide, mais ajoute du lexique hors leçon — **m-3** |
| `quiz` Q2 `b` (« has just arrived » → « has only just arrived ») | clé `a` 58 était la plus longue (b=56) → b=61 | ✅ | faux ✅, plausible ✅ | ✅ valide sans réserve |

---

# AUDIT — chapitre 12

# AUDIT — `content/english-bac/12-school-related-words/` (23 questions)

Auditeur indépendant, contexte vierge, n'a écrit aucune ligne de ce chapitre.
**Aucun fichier du corpus modifié.** Toutes les corrections ci-dessous sont prêtes à coller.

Périmètre : `quiz.json` (5) · `exercices/01-pratique.json` (6) · `exercices/02-boss.json` (6) ·
`exercices/03-revision.json` (6) = **23 questions**.
Racine : `D:\11-coding\YahiaAcademy\campagnes-tronc-commun\wt\anglais-bac\corpus` ·
branche `wip/content-english-bac-ch10-12`.

Statut : **TERMINÉ** — 23/23 clés re-résolues à l'aveugle.
**4 BLOCKER · 14 MAJOR · 14 MINOR · 0 clé fausse.**

---

## En une phrase

**La forme est la meilleure de la tranche ; le fond est le pire.** Clés parfaitement réparties
(a=5 b=5 c=5 d=5), zéro clé la plus courte, une seule clé la plus longue — et **16 items sur 23
rejouent un exemple du cours**, contre 10/23 au chapitre 10. Deux exercices sur trois se laissent
résoudre en ayant relu `cours.md` sans jamais raisonner. Un item du boss délivre en plus une
**explication factuellement fausse** depuis la correction de schéma.

---

## 0. Mesures mécaniques — recalculées par moi, pas reprises de l'en-tête

```
23 questions · 20 mcq + 2 ordering + 1 multi

1a. clé strictement la plus LONGUE : 1/20 ( 5 %)  — cible 0 %     OK (le cas est discuté §4)
1b. clé strictement la plus COURTE : 0/20 ( 0 %)  — cible ≤ 25 %  OK — le meilleur de la matière
2.  répartition des clés : a=5 · b=5 · c=5 · d=5  (25 % chacune)  PARFAIT
3.  difficulté des questions : 1–3 partout                        OK
4.  fragments ≥ 20 car. partagés avec cours.md / resume.md : 40   cible 0 -> le plus haut
                                                                  de la matière (ch.10 : 23, ch.11 : 27)
5.  formats : 2 ordering, 0 matching, 1 multi                     -> MAJOR-14
6.  fichiers, titres, xpReward/rewardCoins/displayOrder            conformes au brief
```

Les cinq plus gros fragments :

| # car. | Où | Verdict |
| --- | --- | --- |
| 54 | `02-boss` Q1, **énoncé** | 🟥 **BLOCKER-3** — signalé par l'orchestrateur, confirmé |
| 39 | `01-pratique` Q2, explication | 🟧 **MAJOR-6** — signalé, confirmé |
| 38 | `02-boss` Q1, **énoncé** | 🟥 même item (deuxième fragment) |
| 36 | `quiz` Q3, explication | 🟨 minor-12 — reprise de la règle enseignée, tolérée |
| 35 | `quiz` Q5, **énoncé** | 🟧 **MAJOR-8** |

⚠️ Le scan flague **16 items**. Ma lecture item par item en trouve **16 aussi — mais pas les
mêmes**. 13 seulement sont communs : le scan **rate** `02-boss` Q2, `03-revision` Q1 et
`03-revision` Q4, et **lève** `quiz` Q1/Q2/Q3 que j'acquitte (gloses d'une règle enseignée, dans
l'explication). Confirmation de l'avertissement de la tranche : **un compte de fragments ne dit
jamais quels items sont malades.**

---

## 1. Journal de re-résolution à l'aveugle — 23/23

| Item | Ma réponse | Clé | Accord | Recycle le cours ? |
| --- | --- | --- | --- | --- |
| `quiz` Q1 | c | c | ✅ | non (définition appliquée à un cas neuf) |
| `quiz` Q2 | a | a | ✅ | non |
| `quiz` Q3 | d | d | ✅ | non (l'explication seule) |
| `quiz` Q4 | b | b | ✅ | **oui** — MAJOR-7 |
| `quiz` Q5 | c | c | ✅ | **oui** — MAJOR-8 |
| `01-pratique` Q1 | c·e·a·d·b | idem | ✅ | **oui** — MAJOR-5 |
| `01-pratique` Q2 | d | d | ✅ | **oui** — MAJOR-6 |
| `01-pratique` Q3 | a | a | ✅ | **oui** — MAJOR-4 |
| `01-pratique` Q4 | b | b | ✅ | **oui** — MAJOR-3 |
| `01-pratique` Q5 | c | c | ✅ | **oui** — BLOCKER-2 |
| `01-pratique` Q6 | a | a | ✅ | **oui** — MAJOR-2 |
| `02-boss` Q1 | b | b | ✅ | **oui** — BLOCKER-3 |
| `02-boss` Q2 | a·c·d | a·c·d | ✅ | **oui** — BLOCKER-1 / MAJOR-10 |
| `02-boss` Q3 | d | d | ✅ | non |
| `02-boss` Q4 | c | c | ✅ | **oui** — MAJOR-9 |
| `02-boss` Q5 | a | a | ✅ | **oui** — BLOCKER-4 |
| `02-boss` Q6 | d | d | ✅ | **oui** (léger) — minor-4 |
| `03-revision` Q1 | d | d | ✅ | **oui** — MAJOR-11 |
| `03-revision` Q2 | b | b | ✅ | non |
| `03-revision` Q3 | b·a·d·c | idem | ✅ | **oui** (explication) — minor |
| `03-revision` Q4 | a | a | ✅ | **oui** — MAJOR-12 |
| `03-revision` Q5 | c | c | ✅ | non |
| `03-revision` Q6 | b | b | ✅ | non |

**Clés divergentes : 0.** **Clés fragiles : 0** — les deux `ordering` sont strictement forcés
(vérifié contrainte par contrainte, §3), et le `multi` n'a aucun distracteur défendable.
**Items rejouant un exemple du cours : 16 / 23 (70 %).**

---

## 2. BLOCKER

### 🟥 BLOCKER-1 — `02-boss` Q2 : l'explication décrit l'item **supprimé**, pas l'item servi

C'est le seul constat du chapitre qui soit une **erreur de fait délivrée à l'élève**, et il est né
de la correction de schéma 8 options → 6.

`content/english-bac/12-school-related-words/exercices/02-boss.json` — Q2.
L'item sert **6 options** et **3 clés** (`provision`, `denial`, `reduction`), un seul adjectif
(`expectant`). L'explication, restée celle de la version à 8 options, dit :

> **Four** words here are the noun of a verb the lesson uses […] The **four others** all belong to
> the same lesson […] **Two are adjectives** — one of them sits on the adjective branch […]

Trois affirmations fausses sur l'item réel : *four* clés (il y en a 3), *four* distracteurs (3), et
*two* adjectifs (1). Un élève qui coche correctement les trois clés lit ensuite qu'il en fallait
quatre : il croit avoir raté un item qu'il a réussi. Sur un `multi` noté tout ou rien, dans le boss,
c'est le pire endroit possible pour un mensonge de correction.

**Correction 1 — l'explication** (`.../exercices/02-boss.json` Q2) :

`ancien texte`
`Four words here are the noun of a verb the lesson uses, and each wears a different tail, which is exactly the point of the diagram: the family is learnt one member at a time. The four others all belong to the same lesson, and none of them belongs on that diagram. Two are adjectives — one of them sits on the adjective branch of the very same family and describes somebody who is waiting for something. One is a verb in its bare form, and the last is that same kind of verb wearing a past ending, which is still a verb.`

`nouveau texte`
`Three words here are the noun of a verb the lesson uses, and each wears a different tail, which is exactly the point of the diagram: the family is learnt one member at a time. The three others all belong to the same lesson, and none of them belongs on that diagram. One is an adjective, and it sits on the adjective branch of a family whose noun branch you could have filled instead: it describes somebody who is waiting for something. One is a verb in its bare form. And the last is that same kind of verb wearing a past ending, which leaves it a verb still.`

**Sur la question posée par l'orchestrateur — les trois clés et les trois distracteurs :**

- `provision` (← *provide*), `denial` (← *deny*), `reduction` (← *reduce*) : **indiscutables**.
  Les trois verbes sont bien de la leçon (*provide* et *deny* sont dans MY NEW WORDS ; *reduce* est
  l'amorce imprimée du spidergramme **Verb** du manuel et le cours l.136/163 l'enseigne).
- `expectant` : adjectif, jamais nom → **indiscutablement faux** ✅
- `reduce` : verbe nu → **indiscutablement faux** ✅
- `provided` : participe passé — et aussi conjonction (*provided that*). **Ni l'un ni l'autre n'est
  un nom** → **indiscutablement faux** ✅

Le correctif de schéma **tient sur le fond**. Il n'a laissé qu'une chose derrière lui :
l'explication. (Voir aussi MAJOR-10 : Q1 donne deux des trois clés de Q2.)

---

### 🟥 BLOCKER-2 — `01-pratique` Q5 : les **quatre** options sont les quatre mots d'**une seule phrase** du cours, avec son classement

`cours.md` l.227, § « An acrostic about school » :

> On an O line waiting for a verb, *often* (an adverb), *ordinary* (an adjective) and *opinion*
> (a noun) all fail, however well they begin. Only *offer*, *organise*, *open* and their kind may
> stand there.

`.../exercices/01-pratique.json` Q5, les quatre options : `Often` · `Ordinary` · `Offer` (clé) ·
`Opinion`. **Mot pour mot, dans le même rôle.** Le cours nomme les trois ✗ et le ✓.

C'est la signature n°1 poussée à son maximum : au chapitre 11 le motif portait sur **deux**
colonnes d'une ligne ; ici il porte sur **les quatre options**. L'élève qui a lu la dernière
section du cours ne classe rien — il se souvient d'une liste. Quatre fragments du scan tombent
d'ailleurs sur ce seul item (33, 24, 22, 20 car.).

Le résumé rejoue la même liste (l.15) : « *offer* and *organise* qualify, *often*, *ordinary* and
*opinion* do not ».

**Correction — côté COURS** (l'item est excellent : contrainte double, distracteurs de trois
classes grammaticales différentes ; règle 6 du brief, on réécrit le cours) :

`cours.md`, l.227 — `ancien texte`
`The constraint is double, and that is what makes the exercise worth doing: the word must **start with the right letter** *and* **belong to the right class**. On an O line waiting for a verb, *often* (an adverb), *ordinary* (an adjective) and *opinion* (a noun) all fail, however well they begin. Only *offer*, *organise*, *open* and their kind may stand there.`

`nouveau texte`
`The constraint is double, and that is what makes the exercise worth doing: the word must **start with the right letter** *and* **belong to the right class**. Test the second constraint the quick way: drop the word into the frame *a school will …* . *A school will help*, *a school will teach*, *a school will feed* — those go in, and they are verbs. A word that refuses the frame has no business at the head of the line, however well it begins.`

`resume.md`, l.15 — `ancien texte`
`- **An acrostic** spells a word downwards, one letter per line — and if the model asks for verbs, the letter alone is not enough: on an O line, *offer* and *organise* qualify, *often*, *ordinary* and *opinion* do not.`

`nouveau texte`
`- **An acrostic** spells a word downwards, one letter per line — and if the model asks for verbs, the letter alone is not enough: test each candidate in the frame *a school will …* , and keep only what fits.`

---

### 🟥 BLOCKER-3 — `02-boss` Q1 : 54 caractères d'énoncé, la clé imprimée **en gras majuscules** dans le cours, et les trois distracteurs nommés par le cours

Le défaut signalé par l'orchestrateur. **Confirmé, et il est plus large que les 54 caractères.**

`cours.md` l.146 :

> **Why nouns matter: the headline.** A newspaper has one line and no room for verbs, so it turns
> them into nouns and stacks them up. *The government has provided free meals* becomes
> **FREE MEALS PROVISION**; *children are denied a place* becomes **THE DENIAL OF SCHOOL PLACES**.

`cours.md` l.142 :

> English says *provision*, never "providation" and never "providment"; it says *denial*, never
> "deniation" and never "denyal".

L'item `.../exercices/02-boss.json` Q1 :

- **énoncé** : « A newspaper has one line and no room for verbs, so it… » (**54 car. verbatim**)
  + « The government has provided free meals » (**38 car. verbatim**) ;
- **clé `b`** : `FREE MEALS PROVISION ENDS THE DENIAL OF SCHOOL PLACES` = les **deux titres en gras
  du cours mis bout à bout** ;
- **les trois distracteurs** : `PROVIDMENT`, `PROVIDATION`, `DENIATION`, `DENYAL` — **les quatre
  non-mots que le cours énumère**, dans le même paragraphe, et repris une seconde fois par
  `resume.md` l.11 et une troisième par le mur des pièges l.236 (« the providation of meals »).

Le grillage de l'item est pourtant excellent (une erreur dans `a` et `d`, deux dans `c`, zéro dans
`b`). **C'est le cours qui l'a désarmé** : il n'y a rien à décider, tout est imprimé. Et c'est la
**Q1 du boss ⭐⭐⭐**, difficulté 3.

**Correction — côté COURS**, trois endroits :

`cours.md` l.142 — `ancien texte`
`> ⚠️ **You cannot pick the ending by rule — each word keeps the one it has always had.** English says *provision*, never "providation" and never "providment"; it says *denial*, never "deniation" and never "denyal". The learner who invents an ending is not being creative, only wrong: a word either exists or it does not, and the only witness is the dictionary. Learn the family, not the recipe.`

`nouveau texte`
`> ⚠️ **You cannot pick the ending by rule — each word keeps the one it has always had.** *Reduce* takes **-tion** and *attend* takes **-ance**, and neither will accept the other's tail: "reducance" and "attendation" are not English words, however reasonable they look. The learner who invents an ending is not being creative, only wrong: a word either exists or it does not, and the only witness is the dictionary. Learn the family, not the recipe.`

`cours.md` l.146 — `ancien texte`
`*The government has provided free meals* becomes **FREE MEALS PROVISION**; *children are denied a place* becomes **THE DENIAL OF SCHOOL PLACES**.`

`nouveau texte`
`*The council has reduced the fees* becomes **FEE REDUCTION**; *parents expect more of the school* becomes **RISING PARENTAL EXPECTATIONS**.`

`cours.md` l.236 (mur des pièges) — `ancien texte`
`| "the providation of meals"                   | _the **provision** of meals_              | each word keeps its own ending; none of them can be invented     |`

`nouveau texte`
`| "the attendation figures"                    | _the **attendance** figures_              | each word keeps its own ending; none of them can be invented     |`

`resume.md` l.11 — `ancien texte`
`⚠️ **The ending cannot be guessed** — "providation", "providment", "deniation", "denyal" do not exist. And **attendance** (being there) ≠ **attention** (listening). Headlines run on these nouns: _the government provided meals_ → **MEALS PROVISION**.`

`nouveau texte`
`⚠️ **The ending cannot be guessed** — a tail cannot be borrowed from a neighbour ("reducance", "attendation" do not exist). And **attendance** (being there) ≠ **attention** (listening). Headlines run on these nouns: _the council reduced the fees_ → **FEE REDUCTION**.`

⚠️ **Le tableau des familles (l.132-138) reste intact** — il doit enseigner *provision* et *denial*.
Ce qui disparaît, c'est le **titre tout fait** et la **liste des non-mots**, c'est-à-dire les quatre
options de l'item.

---

### 🟥 BLOCKER-4 — `02-boss` Q5 : trois options sur quatre sont les trois phrases d'exemple du cours, un mot glissé dedans

`cours.md` l.119-126, règles 1 et 2 du jeu des contraires :

> - _The last question was **hard**._ → its opposite is **easy** (difficulty).
> - _The bench in the corridor is **hard**._ → its opposite is **soft** (what it is made of).
> …
> **Rule 2** — In _She works hard_, the word is no longer an adjective […] it is an adverb…

`.../exercices/02-boss.json` Q5 :

| Option | Phrase du cours rejouée | Ce qui change |
| --- | --- | --- |
| **`a` (clé)** | « The bench in the corridor is hard. » | + *wooden*, + *very* (26 car. verbatim au scan) |
| `b` | « The last question was hard. » | + *on the paper* |
| `c` | « She works hard » | + *on the days she has no lessons* |
| `d` | — | seule option neuve |

Et l'explication reprend 32 car. du mur des pièges (« an opposite answers a meaning, n… ») et 20 de
la règle 2 (« how she works, and »).

C'est **exactement** la signature n°2 (« l'item EST l'exemple du cours, avec un détail glissé »),
appliquée trois fois dans un même item, sur le **boss ⭐⭐⭐ difficulté 3**. L'élève qui a relu la
section reconnaît le banc et la dernière question sans jamais se demander de quelle *acception* il
s'agit — ce qui est pourtant toute la compétence visée.

**Correction — côté COURS** (l'item est bien construit : il oppose l'acception matérielle, deux
acceptions figurées et un adverbe ; on ne le touche pas).

`cours.md` l.120-121 — `ancien texte`
```
- _The last question was **hard**._ → its opposite is **easy** (difficulty).
- _The bench in the corridor is **hard**._ → its opposite is **soft** (what it is made of).
```
`nouveau texte`
```
- _The examiner set a **hard** paper this year._ → its opposite is **easy** (difficulty).
- _The playground is **hard** after a month without rain._ → its opposite is **soft** (what it is made of).
```

`cours.md` l.126 — `ancien texte`
`**Rule 2 — check what part of speech you are looking at.** In _She works hard_, the word is no longer an adjective describing a thing; it is an adverb saying how she works, and neither *soft* nor *easy* can be pushed into its place.`

`nouveau texte`
`**Rule 2 — check what part of speech you are looking at.** In _He tried hard all term_, the word is no longer an adjective describing a thing; it is an adverb saying in what manner he tried, and neither *soft* nor *easy* can be pushed into its place.`

`cours.md` l.237 (mur des pièges) — `ancien texte`
`| "the bench is hard, so its opposite is easy" | _the bench is hard → **soft**_            | an opposite answers a meaning, not a word on a list              |`

`nouveau texte`
`| "the ground is hard, so its opposite is easy" | _the ground is hard → **soft**_           | an opposite answers a meaning, not a word on a list              |`

`resume.md` l.10 — `ancien texte`
`**1)** an opposite answers a **meaning**, not a word: _a hard question_ → **easy**, but _a hard bench_ → **soft**. **2)** watch the **part of speech**: in _she works hard_, *hard* is an adverb and neither opposite fits.`

`nouveau texte`
`**1)** an opposite answers a **meaning**, not a word: _a hard paper_ → **easy**, but _hard ground_ → **soft**. **2)** watch the **part of speech**: in _he tried hard_, *hard* is an adverb and neither opposite fits.`

---

## 3. MAJOR

### 🟧 MAJOR-1 — `01-pratique` Q6 : l'explication cite une option **par son rang**

Défaut signalé par l'orchestrateur. **Confirmé** — règle 4 du brief (les options sont mélangées à
l'affichage, on cite la **valeur**, jamais la position).

`.../exercices/01-pratique.json` Q6, dernière phrase de l'explication :

`ancien texte`
`And the fourth answer promotes him: the person who presents the lesson is the one giving it.`

`nouveau texte`
`And promoting him to the one who presents the lesson would make him the person giving it, not the person sitting through it.`

*(Les « The first / The second » de la même explication sont acceptables : ils numérotent les
**deux pièges** annoncés par la phrase précédente, pas les options.)*

---

### 🟧 MAJOR-2 — `01-pratique` Q6 : l'énoncé est la ligne ✗ du cours, la clé sa ligne ✓

Même item. `cours.md` l.29 :

> ~~_Yesterday I **assisted at** the biology lesson._~~ ✗ — this comes straight from a French verb
> that looks the same. In English, **to assist somebody is to help them**. If you were merely
> sitting there with your class, you **attended** the lesson.

L'énoncé : « Yesterday I assisted at the **science** lesson. » — **28 car. verbatim**, un seul mot
changé. La clé `a` : « Yesterday I attended the science lesson. » = la sortie prescrite par le
cours. Le mur des pièges l.235 réimprime la paire (« I assisted at the lesson » / *I **attended**
the lesson*), et `resume.md` l.3 imprime le distracteur `c` (« "attend at the lesson" ✗ »).

Signature n°1 **et** n°2 sur le même item : les quatre options sortent toutes du même paragraphe.

**Correction — côté COURS** (l'item est bon : quatre erreurs réelles de francophone) :

`cours.md` l.29 — `ancien texte`
`- ~~_Yesterday I **assisted at** the biology lesson._~~ ✗ — this comes straight from a French verb that looks the same. In English, **to assist somebody is to help them**. If you were merely sitting there with your class, you **attended** the lesson.`

`nouveau texte`
`- ~~_Two hundred parents **assisted at** the prize-giving._~~ ✗ — this comes straight from a French verb that looks the same. In English, **to assist somebody is to help them**. Parents who only sat and watched **attended** the ceremony; the two who carried the chairs assisted the caretaker.`

`cours.md` l.235 — `ancien texte`
`| "I assisted at the lesson"                   | _I **attended** the lesson_               | to assist is to help; and *attend* takes no preposition          |`

`nouveau texte`
`| "the parents assisted at the ceremony"       | _the parents **attended** the ceremony_   | to assist is to help; and *attend* takes no preposition          |`

`resume.md` l.3 — `ancien texte`
`(**no preposition**: _attend the lesson_ ✓, "attend at the lesson" ✗ — and *to assist* means *to help*, never *to be present*)`

`nouveau texte`
`(**no preposition**: _attend a ceremony_ ✓, "attend at a ceremony" ✗ — and *to assist* means *to help*, never *to be present*)`

---

### 🟧 MAJOR-3 — `01-pratique` Q4 : l'item est l'exemple du cours, et ses deux distracteurs sont les deux exclusions que le cours énonce

`cours.md` l.209 :

> - _The shelf is too high **for the little ones** to reach._ → **the little ones** are the ones who
>   cannot reach. **Not the shelf, and not you.**

L'item : « These books are too high up **for the youngest readers** to reach on their own. »
— même hauteur, même verbe *reach*, même structure. Et :

- distracteur `a` « the librarian cannot reach the books » = « **not you** » ;
- distracteur `d` « the books cannot reach the youngest readers » = « **not the shelf** ».

Le cours a écrit les deux mauvaises réponses avant que l'élève ne les lise. L'explication reprend en
outre 24 car. de la règle (« hands the second verb… »).

**Correction — côté COURS** (l'item est bon ; c'est le seul du chapitre qui teste le rôle du *for*) :

`cours.md` l.209 — `ancien texte`
`- _The shelf is too high **for the little ones** to reach._ → **the little ones** are the ones who cannot reach. Not the shelf, and not you.`

`nouveau texte`
`- _The corridor is too narrow **for two classes** to pass at once._ → **the two classes** are the ones that cannot pass. Not the corridor, and not the caretaker who built it.`

`resume.md` l.14 — `ancien texte`
`**3)** with **for + somebody**, that person is the one who acts: _too high for the little ones to reach_ = **the little ones** cannot reach.`

`nouveau texte`
`**3)** with **for + somebody**, that person is the one who acts: _too narrow for two classes to pass_ = **the two classes** cannot pass.`

---

### 🟧 MAJOR-4 — `01-pratique` Q3 : l'exemple travaillé du cours, avec les nombres changés

`cours.md` l.68 :

> 🗡️ Listen for the order, not only for the verbs. *Take three from twelve, then share the rest
> between three* asks you to **subtract** and then to **divide** — in that order. Reverse the two
> and you get a different number, and a wrong answer to a question you understood perfectly.

L'item : « Take **four** away from **twenty**, then share what is left equally among the **four**
pupils in the front row. » → **subtract puis divide**, et l'explication rejoue le raisonnement du
cours (« reverse and you get a different number ») en le chiffrant.

Même couple d'opérations, même ordre, même mise en garde. Seuls les nombres bougent.
*(L'arithmétique de l'explication est juste : (20−4)/4 = 4, et 20/4−4 = 1. ✅)*

**Correction — côté COURS** (l'item est bon et le seul à tester les périphrases orales) :

`cours.md` l.68 — `ancien texte`
`> 🗡️ Listen for the order, not only for the verbs. *Take three from twelve, then share the rest between three* asks you to **subtract** and then to **divide** — in that order. Reverse the two and you get a different number, and a wrong answer to a question you understood perfectly.`

`nouveau texte`
`> 🗡️ Listen for the order, not only for the verbs. *Three lots of eight, and then put six more on top* asks you to **multiply** and then to **add** — in that order. Reverse the two and you get thirty in one direction and forty-two in the other, and a wrong answer to a question you understood perfectly.`

*(Vérifié : 3×8 = 24, +6 = 30 ; et 8+6 = 14, ×3 = 42. Le couple soustraction/division est ainsi
libéré pour l'item, et le cours illustre les deux autres signes, qui n'apparaissaient jusque-là que
dans le tableau.)*

---

### 🟧 MAJOR-5 — `01-pratique` Q1 (`ordering`) : **l'ordre lui-même est imprimé**, dans le cours ET dans le résumé

C'est le cas que le brief nomme « le pire cas rencontré ».

`cours.md` l.72-80 : un tableau dont les cinq lignes sont, dans l'ordre, `a book` · `a chapter` ·
`a paragraph` · `a sentence` · `a full stop`. Précédé de la phrase l.72 : « A written text is a set
of boxes inside boxes, **from the widest down to the smallest mark**. »
`resume.md` l.7 : « **On the page**, from the widest to the smallest: **a book** → **a chapter** →
**a paragraph** → **a sentence** → **a full stop**. »

L'item demande : « Put these five back in order, from the one that holds all the others **down to
the smallest mark** printed on the page. » (**26 car. verbatim de l.72**), clé
`c·e·a·d·b` = l'ordre du tableau, = l'ordre de la flèche du résumé.

Un `ordering` est noté tout ou rien : ici il note une ligne du résumé. La clé est **strictement
forcée** par l'emboîtement (vérifié) — le problème n'est pas la justesse, c'est qu'il n'y a rien à
faire.

**Correction — côté ITEM.** Ici le brief ne s'applique pas à la lettre (« réécris le côté COURS si
la question est bonne ») : la question **n'est pas bonne**, et la hiérarchie livre→chapitre→
paragraphe→phrase→point est un fait que le cours *doit* imprimer et le résumé *doit* rappeler la
veille du bac. C'est l'item qu'il faut changer.

**Et le meilleur remplacement règle trois constats d'un coup** (MAJOR-5, MAJOR-13, MAJOR-14) :
remplacer cet `ordering` par le **`matching` que le chapitre n'a pas** et qui couvre le jeu des
contraires — l'activité 2 du manuel, aujourd'hui testée par un seul item.

`.../exercices/01-pratique.json` Q1 — remplacer intégralement la question par :

```json
{
  "prompt": "Your partner throws you a word from the school field and waits for the word that answers it. Match each one with its opposite.",
  "type": "matching",
  "options": [
    { "id": "l1", "text": "to teach" },
    { "id": "l2", "text": "a candidate" },
    { "id": "l3", "text": "to attend a school" },
    { "id": "l4", "text": "the working weeks" },
    { "id": "r1", "text": "an examiner" },
    { "id": "r2", "text": "the holidays" },
    { "id": "r3", "text": "to learn" },
    { "id": "r4", "text": "to leave it" }
  ],
  "answerKey": { "pairs": [["l1", "r3"], ["l2", "r1"], ["l3", "r4"], ["l4", "r2"]] },
  "explanation": "Four pairs, and each one turns on a different kind of contrast. Two of them are the two ends of the same act seen from the two sides of the desk: one person passes the knowledge on, the other takes it in; one person sits the paper, the other sets it and marks it. The third is a matter of staying or going: you are on the register for years, and then one day you are not. And the fourth divides the calendar in two, since every week of a school year is either one or the other. Notice that none of the eight can be paired by its shape — only by what it means.",
  "difficulty": 1
}
```

*(Schéma vérifié sur `11-the-winters-tale/exercices/01-pratique.json` : `options` avec ids `l1…`/
`r1…` et `answerKey.pairs`. Les paires sont volontairement décroisées — `l1→r3`, `l3→r4` — pour que
l'appariement par rang d'identifiant ne donne rien. Les quatre couples sont ceux du guide
enseignant, p.24.)*

Si l'on tient à garder l'`ordering`, la correction de repli est de **désordonner le tableau du
cours** (le présenter du plus petit au plus grand, ou par ordre alphabétique) et de **remplacer la
chaîne fléchée du résumé** par les deux discriminations utiles (« un chapitre découpe un livre,
jamais une dissertation ; un point clôt une phrase, jamais une idée »). C'est un moindre mal :
l'item reste de la récitation.

---

### 🟧 MAJOR-6 — `01-pratique` Q2 : 39 caractères, et l'item **est** le tableau du cours, ses deux colonnes

Défaut signalé par l'orchestrateur. **Confirmé, et plus large que le fragment.**

`cours.md` l.36-43 : un tableau à deux lignes — « **three** → a **term** → Tunisia, Britain… » /
« **two** → a **semester** → the United States… » — suivi de « it is divided, and **the number of
pieces decides the word** » et de « a report card that reaches your **family three times** a year
closes three terms ».

L'item : l'énoncé **donne les deux nombres et les deux pays** (« Tunisian and British schools
usually cut the year into three; American schools usually cut it into two ») ; l'explication reprend
39 car. (« the number of pieces decides the word. ») et 20 de plus (« family three times »).

L'énoncé fournit donc le **discriminant** que le tableau utilise ; il ne reste qu'à lire la colonne
d'à côté. La bonne addition de l'item (*semicircle*, *semifinal*) est dans l'explication, après coup.

**Correction — côté ITEM** (faire compter l'élève au lieu de lui donner le nombre) et **côté COURS**
(retirer le carnet de notes, qui est le véhicule partagé) :

`.../exercices/01-pratique.json` Q2, énoncé — `ancien texte`
`Tunisian and British schools usually cut the year into three; American schools usually cut it into two. What is one of those pieces called in each system?`

`nouveau texte`
`Sami takes a report home in December, in March and in June, and that is his whole year in Sfax. His cousin in Boston takes one home in January and one in May, and that is her whole year. What is one of those pieces of the year called in each of the two systems?`

*(Les options et la clé `d` sont inchangées. L'explication doit alors renoncer à sa première phrase
« The number of pieces decides the word » au profit de : « Count the reports and you have counted
the pieces: three of them in Sfax, two in Boston. »)*

`cours.md` l.43 — `ancien texte`
`So a report card that reaches your family three times a year closes three **terms**; a report card that comes twice closes two **semesters**. Notice how honest the second word is: *semester* holds *semi*, and half of a year is what it names.`

`nouveau texte`
`So a British pupil sits down to three sets of end-of-**term** examinations, and an American student to two sets of end-of-**semester** ones. Notice how honest the second word is: *semester* holds *semi*, and half of a year is what it names.`

---

### 🟧 MAJOR-7 — `quiz` Q4 : la porte du chapitre s'ouvre sur un paragraphe relu

`cours.md` l.144 :

> **Attendance** is the fact of being there — **the office counts it every morning**. **Attention**
> is what you give the lesson once you are in your seat.

`quiz.json` Q4 : « **Every morning the school office** notes which pupils are present and which are
missing […] What is the office keeping a record of? » — clé `attendance`, distracteur `attention`.

Même acteur (*the office*), même fréquence (*every morning*), et **le distracteur est le terme de
contraste du cours**. L'explication reprend « the fact of being there » (24 car.). Signature n°1 +
n°2 — et c'est un item du **quiz, la porte du chapitre (≥ 80 % pour ouvrir)**, exactement le grief
MAJOR-2 de l'audit du chapitre 10.

**Correction — côté COURS** (l'item est bon : quatre formes d'une même famille, trois classes
grammaticales) :

`cours.md` l.144 — `ancien texte`
`Beware, too, of two branches of the same tree that do not mean the same thing. **Attendance** is the fact of being there — the office counts it every morning. **Attention** is what you give the lesson once you are in your seat. A register of attendance says nothing about whether anybody was listening.`

`nouveau texte`
`Beware, too, of two branches of the same tree that do not mean the same thing. **Attendance** is the fact of being there — a figure that climbs when a new bus route reaches the outlying villages. **Attention** is what you give the lesson once you are in your seat. The first can be counted, the second never has been, and no register has ever pretended otherwise.`

---

### 🟧 MAJOR-8 — `quiz` Q5 : l'item est le paragraphe du cours, sa photo comprise

`cours.md` l.177 et l.179 :

> A page headed *The real wealth of a country is …* above **a photograph of children eating** tells
> you […]
> A web address ending in **.org** belongs to an **organisation**, not to a shop; an e-mail
> **address beginning with fundraising** belongs to somebody whose work is to collect gifts.
> **Two lines nobody looks at** have just told you who is speaking and what they want from you.

`quiz.json` Q5 : « A full page in a magazine shows **a photograph of children eating** at school
[…] a web address of the form www.…org, and an e-mail **address beginning with fundraising@**. »
(deux fragments de 33 et 35 car. **dans l'énoncé**) — clé `c` : « the page was placed by an
**organisation** that is asking for **gifts** » = la conclusion du cours ; explication : « the two
lines that almost no reader looks at » = l.179.

Le cours a résolu l'item avant qu'il soit posé. Deuxième item de la **porte** dans ce cas.

**Correction — côté COURS.** L'information est exigée par le programme (activité 3a du manuel :
« Focus on the website and e-mail address to find out ») : elle **doit** rester enseignée. Ce qui
doit partir, c'est la **conclusion toute faite** et la photo partagée. Enseigner la méthode, pas la
réponse :

`cours.md` l.177 — `ancien texte`
`**Read the paratext first.** From a headline, a subtitle and a photograph you can already predict what the body will say — that is a skill, not a guess. A page headed *The real wealth of a country is …* above a photograph of children eating tells you, before a single line of the body, that its ending will not be *its oil*: an appeal built on children ends its headline on **its children**.`

`nouveau texte`
`**Read the paratext first.** From a headline, a subtitle and a photograph you can already predict what the body will say — that is a skill, not a guess. A page headed *What a village loses when the well runs dry* above a picture of an empty classroom has already told you, before a single line of the body, that the two are about to be tied together — and which of them the page will ask you to pay for.`

`cours.md` l.179 — `ancien texte`
`**And read the last lines, because they name the sender.** A web address ending in **.org** belongs to an **organisation**, not to a shop; an e-mail address whose first word is **fundraising** belongs to somebody whose work is to collect gifts. Two lines nobody looks at have just told you who is speaking and what they want from you.`

`nouveau texte`
`**And read the last lines, because they name the sender.** Nobody looks at the small print at the foot of a page, and it is the one part of an advertisement that cannot lie about who is speaking: the tail of a web address says what kind of body owns it, and the first word of an e-mail address names the desk you would be writing to. Ask those two questions of any page that is asking you for something, and you will know who wants what from you before you have read a line of the body.`

`resume.md` l.13 — `ancien texte`
`The last lines name the sender: **.org** = an organisation, and an address beginning with **fundraising** = somebody collecting gifts.`

`nouveau texte`
`The last lines name the sender: read the **tail** of the web address (what kind of body owns it) and the **first word** of the e-mail address (which desk you would be writing to).`

---

### 🟧 MAJOR-9 — `02-boss` Q4 : la chaîne du cours, y compris le sens interdit

`cours.md` l.183 :

> 🗡️ **The chain of consequences.** A good appeal never asks you to believe a miracle; it shows you
> a chain, link by link. **A plate of food at midday brings a child through the gate**; a child who
> is in the classroom hears the lesson; and a child who hears the lessons all year comes out of the
> year knowing more. […] check that it is **not running backwards**.

`.../exercices/02-boss.json` Q4 : énoncé « how **a plate of food at midday** can change a child's
marks » (27 car.) ; clé `c` = la chaîne du cours en deux maillons ; distracteur `a` = **la chaîne à
l'envers**, c'est-à-dire précisément le piège que le cours annonce ; explication « never asks its
reader to believe a miracle » (21 car.).

Boss ⭐⭐⭐ difficulté 3. L'élève qui a lu l'encadré n'a rien à reconstruire.

**Correction — côté COURS** (l'item est bon, et la chaîne repas → présence → résultats est le
diagramme de l'activité 6 du manuel : elle doit rester la chose *testée*, donc il faut qu'elle cesse
d'être la chose *montrée*) :

`cours.md` l.183 — `ancien texte`
`A plate of food at midday brings a child through the gate; a child who is in the classroom hears the lesson; and a child who hears the lessons all year comes out of the year knowing more. Feeding, attendance, results: three links, each one holding the next.`

`nouveau texte`
`A well sunk in a village gives a girl back the four hours she spent fetching water; a girl who has her mornings free can be put on the register; and a girl on the register sits the same papers as her brothers. Water, time, schooling: three links, each one holding the next.`

*(Le distracteur `d` de l'item — « the meal makes the lessons shorter » — reste faible, voir
minor-2.)*

---

### 🟧 MAJOR-10 — `02-boss` : **Q1 donne deux des trois clés de Q2**

Fuite inter-items, du même type que MAJOR-5 du chapitre 10.

- Q1, clé `b` : « FREE MEALS **PROVISION** ENDS THE **DENIAL** OF SCHOOL PLACES » — l'item établit
  que *provision* et *denial* sont les noms qui existent.
- Q2, immédiatement après : « Tick EVERY word that belongs on [the Noun spidergram] » — clés
  `provision`, `denial`, `reduction`.

Deux des trois clés de Q2 viennent d'être imprimées comme la bonne réponse de Q1 — et le distracteur
`d` de Q1 (`DENYAL`) confirme même l'orthographe attendue. Le boss compte six items ; il en mesure
cinq et demi.

**Correction** — changer le matériel de Q2 pour les **autres** familles du tableau du cours (les
trois types de distracteur voulus par l'orchestrateur sont conservés : adjectif, verbe nu, participe) :

`.../exercices/02-boss.json` Q2, options — `ancien texte`
`a: provision` · `b: expectant` · `c: denial` · `d: reduction` · `e: reduce` · `f: provided`

`nouveau texte`
`a: attendance` · `b: expectant` · `c: expectation` · `d: reduction` · `e: attend` · `f: provided`

`answerKey.correct` — `ancien texte` `["a","c","d"]` · `nouveau texte` `["a","c","d"]` *(inchangé :
`attendance`, `expectation`, `reduction`)*

*(Les trois distracteurs gardent leurs rôles : `expectant` adjectif, `attend` verbe nu, `provided`
participe. `expectant` et `expectation` se retrouvent dans le même item, ce qui rend à nouveau vraie
la phrase de l'explication sur « the adjective branch of the very same family » — voir la réécriture
en BLOCKER-1. ⚠️ Écho résiduel à surveiller : `attendance` est déjà la clé de `quiz` Q4 et le mot
travaillé de `03-revision` Q5.)*

---

### 🟧 MAJOR-11 — `03-revision` Q1 : le cours nomme lui-même la mauvaise réponse

`cours.md` l.51-55 :

> - **the sciences** — the heading over **physics**, **chemistry** and **biology** […]
> - **languages** — the heading over **English**, **French**, **German**, **Spanish** […]
> ⚠️ Answering **"chemistry"** when you are asked what physics, chemistry and biology are
> **together** does not answer the question…

L'item : les deux listes de matières du cours (une matière retirée, l'ordre inversé), et le
distracteur `a` = « Spanish, and then **chemistry** » — le mot que le cours écrit entre guillemets
comme *la* mauvaise réponse. Clé `d` = les deux intitulés en gras du cours.

L'explication se termine en outre sur « geometry is a branch of maths, and art belongs to no heading
at all » — vrai, enseigné, mais **aucune option ne mentionne ni geometry ni art** : c'est du cours
collé dans une explication (voir minor-6).

**Correction — côté COURS** (l'item est bon : il oppose l'intitulé, la matière isolée, l'inversion
et le singulier) :

`cours.md` l.55 — `ancien texte`
`> ⚠️ *Sciences* and *languages* are **collective names**: each one covers several subjects at once. Answering "chemistry" when you are asked what physics, chemistry and biology are **together** does not answer the question — you were asked for the heading, not for one line under it.`

`nouveau texte`
`> ⚠️ *Sciences* and *languages* are **collective names**: each one covers several subjects at once. A heading is never one of the things it stands over. Asked what several subjects are called **together**, you owe the name of the group; naming any single one of them, however correctly spelt, answers a much smaller question than the one you were put.`

---

### 🟧 MAJOR-12 — `03-revision` Q4 : la clé est l'exemple de vocabulaire du cours

`cours.md` l.154, tableau des cinq mots :

> | **nutritious** | nourishing — food that feeds the body properly | _**Bread and lentils** are
> cheap and nutritious._ |

L'item : « Which of these four changes earns her that word? » — clé `a` : « **lentils, brown bread**
and an orange replace a plate of chips ». Le scan ne l'attrape pas (ordre des mots changé) ; c'est
exactement le doublon invisible à la mesure lexicale.

Les trois distracteurs sont excellents et distincts (quantité / goût / prix), et le résumé l.12 les
annonce d'ailleurs (« **not** *tasty*, **not** *plentiful* »). L'item survivrait à la correction ;
c'est la clé qu'il faut sortir du cours.

**Correction — côté COURS** :

`cours.md` l.154 — `ancien texte`
`| **nutritious** | nourishing — food that feeds the body properly        | _Bread and lentils are cheap and nutritious._            |`

`nouveau texte`
`| **nutritious** | nourishing — food that feeds the body properly        | _A boiled egg is a more nutritious break than a biscuit._ |`

---

### 🟧 MAJOR-13 — couverture : le JEU DES CONTRAIRES, activité 2 du manuel, est testé par **un** item — et pas sur les paires

La leçon a **deux** compétences nommées au UNIT OUTLINE : *Reading — Exploiting an ad* et
***Speaking — Expanding vocabulary***. La seconde, côté manuel, c'est l'activité 2 (THE OPPOSITES
GAME) et sa boîte de 24 mots, plus les 15 bulles-questions de l'activité 1.

Le cours enseigne les **12 paires** (l.108-115) et le résumé les réimprime (l.9). Or :

- **un seul item** (`02-boss` Q5) travaille le jeu des contraires — et il porte sur l'**exception**
  (la polysémie de *hard*), pas sur les paires ;
- **huit paires sur douze ne paraissent nulle part** dans les 23 items : *teach/learn*,
  *clever/stupid*, *good/bad*, *pass/fail*, *worse/better*, *last/first*, *work/holiday*,
  *candidate/examiner* ;
- *candidate* et *examiner* sont enseignés sur une section entière (l.88-102) et testés **zéro
  fois** ;
- même remarque, plus légère, pour **timetable** (bulle « Where can you find the days of the
  week? ») qui n'apparaît qu'en distracteur de `01-pratique` Q2, et pour **multiply** / **add** qui
  n'apparaissent qu'en distracteurs de `01-pratique` Q3.

À l'inverse, tout ce qui est testé est bien enseigné : **23/23 items ont leur notion dans
`cours.md`** (vérifié un par un). Le déséquilibre est donc unilatéral — pas d'item orphelin, mais un
gros pan de la leçon non mis à l'épreuve.

**Correction** : le `matching` proposé en MAJOR-5 couvre quatre de ces huit paires en un item et
libère le seul format qui convient à un chapitre lexical.

---

### 🟧 MAJOR-14 — format : **2 `ordering`, 0 `matching`** — dans le seul chapitre où l'appariement s'imposait

Recomptage sur toute la matière (chiffre du brief confirmé) : **12 `ordering` · 13 `matching` ·
15 `multi`**. Le chapitre 12 apporte **2 des 12 `ordering` et 0 des 13 `matching`**.

C'est le **deuxième chapitre du corpus** à porter deux `ordering` (avec `06-exploring-a-song`), et
le seul chapitre purement **lexical** de la matière — celui où « mot ↔ définition », « mot ↔
contraire », « verbe ↔ nom » sont l'instrument naturel, comme le dit le brief. Les deux `ordering`
retenus sont par ailleurs les deux items les plus proches d'une récitation : l'un remet en ordre un
tableau imprimé (MAJOR-5), l'autre — bon item, lui — classe un budget.

**Correction** : voir MAJOR-5 (conversion de `01-pratique` Q1 en `matching`). Elle ramène le
chapitre à 1 `ordering` + 1 `matching`, et la matière à 11/14.

---

## 4. MINOR

**minor-1 — `02-boss` Q3 : deux distracteurs encodent la même erreur.** `a` (« so careful that she
never finishes her work on time ») et `c` (« she spends so long checking her work that it always
arrives late ») sont la même lecture fautive — *too* entendu comme un reproche — écrite deux fois.
L'item se joue à trois options. Suggestion pour `c` :
`ancien texte` `she spends so long checking her work that it always arrives late`
`nouveau texte` `she has been asked twice to check her work before handing it in`
*(erreur différente : la phrase lue comme une consigne reçue et non comme une garantie donnée.)*

**minor-2 — distracteurs quasi morts.** `01-pratique` Q2 `a` (« a chapter » comme fraction de
l'année) et `c` (« a timetable ») s'éliminent sans la leçon ; `02-boss` Q4 `d` (« the meal makes the
lessons shorter ») n'est l'erreur de personne ; `03-revision` Q2 `a` **se contredit lui-même**
(« the O is short for **Outstanding** and beats an **ordinary** pass » — il concède ce qu'il nie).
Trois items se jouent en pratique à trois options.

**minor-3 — `02-boss` Q6 : l'énoncé est le jumeau de l'exemple du cours.** `cours.md` l.153 :
« _No one here is denied a library card._ » → item : « No child in this town is denied a place at
our school. » Même négation, même passif, même verbe, nom changé. L'item reste bon (il exige de
trancher entre les deux sens de *deny* **et** de lire le passif, ce que la phrase du cours ne
demande pas). Correction bon marché, `cours.md` l.153 :
`ancien texte` `_No one here is denied a library card._`
`nouveau texte` `_The office denied her the certificate until the fee was paid._`

**minor-4 — `03-revision` Q5 : « rose from 58 to 91 » sans unité.** Élèves ou pourcentage ? Le
chiffre du manuel est un taux de fréquentation. Suggestion :
`ancien texte` `the pupils in class every day rose from 58 to 91`
`nouveau texte` `the pupils in class every day rose from 58 % to 91 %`

**minor-5 — `03-revision` Q5 : les quatre options font exactement 54 caractères.** Aucune n'est
maladroite, l'anglais tient (vérifié) — mais c'est l'empreinte d'un calibrage à la longueur, et le
chapitre en porte d'autres traces (`03-revision` Q1 : 26/27/32/32 ; `quiz` Q1 : 38/38/41/41). Rien à
corriger, à savoir.

**minor-6 — `03-revision` Q1 : l'explication finit sur du hors-sujet.** « geometry is a branch of
maths, and art belongs to no heading at all » — ni *geometry* ni *art* n'apparaissent dans les
options. C'est `cours.md` l.53 collé là. Supprimer la dernière phrase.

**minor-7 — trois items `too … to` sur le même moule.** `quiz` Q3, `01-pratique` Q4 et `02-boss` Q3
sont trois QCM « voici une phrase, que dit-elle ? ». Les trois angles diffèrent réellement (le
blocage, le rôle du *for*, l'éloge), mais la **tâche** ne varie pas — règle 5 du brief. Une
transformation (« joins these two sentences with *too … to* ») aurait couvert l'exercice du manuel
(GRAMMAR FOCUS activité 1, qui est un exercice de **production**) et diversifié le lot. Aucun item
du chapitre ne demande de **produire** une structure.

**minor-8 — la même règle enseignée deux fois dans deux explications.** `quiz` Q2 (« chapters cut up
a book, never a three-page essay ») et `01-pratique` Q1 (« a book is never cut into paragraphs and
[…] an essay is never cut into chapters »).

**minor-9 — `chapter.json` : description de 2306 caractères**, la plus longue de la matière de 28 %
(la suivante, `07-walking-tour`, fait 1801 ; la médiane est à ~1200). Elle est exacte et sans faute,
mais c'est une phrase unique de plus de deux mille signes.

**minor-10 — `03-revision` Q3 porte `difficulty: 3` dans un exercice `difficulty: 2`.** Autorisé par
le moteur, cohérent ici (c'est bien l'item le plus dur du fichier), signalé pour l'homogénéité avec
le constat MINOR-12 de l'audit du chapitre 10. Idem `03-revision` Q6.

**minor-11 — `quiz` Q3 : 36 caractères de la règle recopiés dans l'explication** (« quality has
passed the point where »). Acquitté au titre de la réserve de la règle 6 (« formules enseignées
explicitement comme telles »), mais c'est le plus gros fragment de cette classe.

**minor-12 — `03-revision` Q1 option `c` : la justification du cours est un peu raide.** Le cours
(l.240) écarte « science » au motif que « the heading is a collective name, **and it is plural** ».
En anglais scolaire britannique réel, *Science* au singulier **est** un intitulé d'emploi du temps
courant. L'option `c` reste fausse par son autre moitié (« **Language** » au singulier), donc l'item
tient — mais la raison affichée est plus absolue que l'usage. Le manuel imprime *sciences* /
*languages* : s'y tenir, sans en faire une loi de l'anglais. Suggestion, `cours.md` l.240 :
`ancien texte` `| "physics, chemistry and biology are science" | _they are **the sciences**_               | the heading is a collective name, and it is plural               |`
`nouveau texte` `| "physics, chemistry and biology are science" | _they are **the sciences**_               | your book's heading is the plural one, and it names a group      |`

**minor-13 — `resume.md` l.12 pré-annonce les distracteurs de `03-revision` Q4** (« **not** *tasty*,
**not** *plentiful* » — soit exactement les options `c` et `b`). C'est le travail légitime d'un
résumé ; noté pour mémoire.

**minor-14 — écho `attendance`.** Le mot est la clé de `quiz` Q4, le mot travaillé de
`03-revision` Q5, et le deviendrait dans `02-boss` Q2 après la correction MAJOR-10. Trois items sur
un même mot : si l'on applique MAJOR-10, préférer `provision` à `attendance` dans la nouvelle liste
de Q2 — mais cela réactive alors la fuite depuis Q1. Le mieux est d'accepter l'écho, `attendance`
étant travaillé sous trois angles différents (forme du nom / famille du verbe / direction du
mouvement).

---

## 5. Ce qui est acquitté — vérifié, pas supposé

- **Aucune clé fausse : 0 / 23.** 20 QCM, 2 `ordering`, 1 `multi` re-résolus à l'aveugle.
- **Les deux `ordering` sont strictement forcés.** `01-pratique` Q1 : l'emboîtement livre ⊃ chapitre
  ⊃ paragraphe ⊃ phrase ⊃ point ne laisse aucune permutation. `03-revision` Q3 : *priority* place le
  bus en tête (le cours définit le mot comme « ce qui vient **d'abord** »), une phrase place les
  bancs avant le toit, une condition (« only if there is anything left in June ») envoie la peinture
  en dernier — les quatre positions sont contraintes, aucun ordre alternatif n'est défendable. C'est
  le meilleur item du chapitre.
- **Le `multi` n'a aucun distracteur défendable** (voir BLOCKER-1 pour le détail des six options).
- **Forme : la meilleure de la tranche.** a=5 b=5 c=5 d=5 exactement ; 0 % de clé la plus courte ;
  5 % de clé la plus longue.
- **Droits (R-2) : rien à signaler.** Aucune ligne de l'annonce du WFP n'est reproduite. Le titre
  imprimé du manuel n'apparaît nulle part dans les questions ; `cours.md` l.177 en cite une variante
  altérée (*a country* pour *a nation*) et la correction MAJOR-8 la fait disparaître de toute façon.
  Les deux items sur l'annonce (`quiz` Q5, `03-revision` Q6) sont écrits sur des pages inventées.
- **Aucun point de grammaire inventé.** La colonne *Functions and linguistic exponents* du UNIT
  OUTLINE p.87 donne « Persuasion ; Word building » : le cours enseigne exactement le spidergramme
  (word building), la mécanique de la persuasion, et `too + adjective + to`, qui est l'encadré
  MY GRAMMAR p.92 mot pour mot. Rien au-delà. Les mentions de *so … that* et *not … enough*
  (l.219) sont présentées comme des voisins, pas enseignées — et ne sont testées par aucun item ✅.
- **Le piège du guide enseignant est évité.** La KEY p.24 donne onze paires de contraires et
  **omet silencieusement *written / oral***, pourtant imprimée dans la boîte de l'élève. Le
  chapitre **enseigne la paire** (`cours.md` l.99, `resume.md` l.8-9), la **teste** (`quiz` Q1) et
  **documente la divergence dans `chapter.json` `sources[]`** ✅. Même traitement pour les trois
  spidergrammes, que le guide laisse sans corrigé : les familles ont été reconstruites sur les
  amorces imprimées (*denial, provision, attend, reduce, expectant*) et le fichier le dit ✅.
- **Aucun doublon avec le chapitre 02.** Le 02 possède le **métalangage** (qu'est-ce qu'un synonyme,
  un antonyme, quel dictionnaire les donne) ; le 12 ne le renomme jamais et l'**emploie** sur le
  champ scolaire. Le cours pose lui-même la frontière (l.9 : « Here you do not name the tool: you
  **use** it »). Aucun item du 12 ne demande la définition d'un antonyme, aucun item du 02 ne porte
  sur le lexique scolaire. **Vérifié sur les 23 items du 12 et sur le cours + les quatre fichiers du
  02.** ✅ Et la **règle 1 du jeu des contraires** (un contraire répond à une acception) est une
  vraie nouveauté : le 02 n'a rien d'équivalent.
- **`quiz` Q4 (`attendance` / `attention` / `attending` / `attendant`) : l'arbitrage de
  l'orchestrateur est CONFIRMÉ.** La clé est la plus longue d'un caractère (10 contre 9/9/9) parce
  que l'anglais écrit *attendance* ainsi. Quatre mots isolés de neuf à dix lettres ne présentent
  aucun indice de longueur perceptible : la mesure « clé strictement la plus longue » vise le cas où
  la clé est une proposition et les distracteurs des syntagmes courts. **Faux positif — laisser en
  l'état.** (L'item a un tout autre défaut, réel : MAJOR-7.)
- **Le chapitre a bien été écrit en deux mains, et les deux moitiés sont cohérentes.**
  `03-revision.json` (second agent) comble exactement ce que la consigne annonçait, et tout y est
  enseigné par le cours : l'échelle scolaire (Q2 ↔ `cours.md` §« The ladder »), les intitulés
  collectifs (Q1 ↔ §« What the timetable prints »), et les trois MY NEW WORDS jamais testés ailleurs
  — *priority* (Q3), *nutritious* (Q4), *boost* (Q5, avec son contraire *reduce*). **Aucune
  contradiction de fond, aucune divergence de registre**, et pas de doublon de notion entre les deux
  moitiés (l'annonce est vue par la porte sous l'angle des coordonnées et par la révision sous
  l'angle de l'appel : deux parties différentes de la même page). Les **trois meilleurs items du
  chapitre — `03-revision` Q2, Q3 et Q6 — sont de la seconde main**, et ce sont aussi trois des
  sept items qui ne recyclent rien. Le second agent a mieux résisté au cours que le premier.

---

## 6. Réponses aux pistes explicitement demandées

| Piste | Verdict |
| --- | --- |
| Cohérence des **deux mains** | ✅ cohérentes sur le fond, le registre et la couverture — **sauf** que la seconde moitié est la plus propre : **3 items recyclés sur 6 (50 %)** contre **13 sur 17 (76 %)** dans la première |
| Le `multi` ramené de 8 à 6 options : **3 clés indiscutables ?** | ✅ oui — *provision*, *denial*, *reduction* sont les noms attestés de trois verbes de la leçon |
| … **3 distracteurs indiscutablement faux ?** | ✅ oui — *expectant* (adjectif), *reduce* (verbe nu), *provided* (participe / conjonction) ne sont des noms dans aucun emploi |
| … **mais** | 🟥 **BLOCKER-1** : l'explication n'a pas suivi et décrit toujours 4 clés, 4 distracteurs et 2 adjectifs. Et 🟧 **MAJOR-10** : Q1 imprime deux des trois clés de Q2 |
| `02-boss` Q1 — **54 car. du cours** | 🟥 confirmé, **BLOCKER-3** — et le défaut dépasse le fragment : la clé et les quatre non-mots des distracteurs sont tous imprimés dans `cours.md` |
| `01-pratique` Q2 — **39 car.** | 🟧 confirmé, **MAJOR-6** — l'énoncé donne en outre le discriminant du tableau |
| `01-pratique` Q6 — **« the fourth answer »** | 🟧 confirmé, **MAJOR-1**, correction fournie |
| `quiz` Q4 — clé la plus longue d'un caractère | ✅ **faux positif confirmé**, laisser en l'état (mais MAJOR-7 sur le même item) |
| Comblements du second agent (échelle, intitulés collectifs, *priority* / *nutritious* / *boost*) | ✅ **justes et tous enseignés par `cours.md`** — vérifié un par un |
| Le chapitre **02** refait-il ce travail ? | ❌ non — frontière métalangage / emploi tenue des deux côtés |
| `ordering` / `matching` dans la matière | ✅ recomptés : **12 `ordering`, 13 `matching`** (+ 15 `multi`). Le ch.12 apporte **2 ordering, 0 matching** → MAJOR-14 |
| Le cours enseigne-t-il tout ce qui est testé ? | ✅ **23/23** |
| … et l'inverse ? | ❌ non — le **jeu des contraires** (8 paires sur 12), *candidate*/*examiner*, *timetable*, *multiply* ne sont jamais testés → MAJOR-13 |

---

## 7. L'inventaire du recyclage — le compte lu, pas le compte du script

| Item | Ce qui est rejoué (`cours.md` / `resume.md`) | Ce qui change | Vu par le scan ? |
| --- | --- | --- | --- |
| `quiz` Q4 | l.144 « the office counts it every morning » + le contraste *attention* | rien (mise en scène) | partiellement (24 c., explication) |
| `quiz` Q5 | l.177 la photo d'enfants qui mangent + l.179 `.org` / `fundraising` + la conclusion | rien | **oui** (35 et 33 c., **énoncé**) |
| `01-pratique` Q1 | l.72-80 le tableau **dans l'ordre** + `resume.md` l.7 la chaîne fléchée | rien | partiellement (26 c.) |
| `01-pratique` Q2 | l.36-43 le tableau, **ses deux colonnes** + le carnet de notes | rien | **oui** (39 + 20 c.) |
| `01-pratique` Q3 | l.68 l'exemple travaillé *soustraire puis diviser* | les nombres | non |
| `01-pratique` Q4 | l.209 « too high for the little ones to reach » + ses deux exclusions | l'objet | partiellement (24 c.) |
| `01-pratique` Q5 | l.227 : **les quatre options sont les quatre mots d'une phrase** | rien | **oui** (4 fragments) |
| `01-pratique` Q6 | l.29 la ligne ✗ + la ligne ✓ + l.235 le mur des pièges + `resume.md` l.3 | *biology* → *science* | **oui** (28 c.) |
| `02-boss` Q1 | l.146 le paragraphe et les deux titres en gras + l.142 les quatre non-mots | rien | **oui** (54 + 38 + 29 c.) |
| `02-boss` Q2 | l.132-138 le tableau des familles, lu ligne à ligne | rien | **non** |
| `02-boss` Q4 | l.183 la chaîne, y compris le sens interdit devenu distracteur | rien | **oui** (27 + 21 c.) |
| `02-boss` Q5 | l.120, l.121 et l.126 : **trois phrases d'exemple sur quatre options** | un mot par phrase | partiellement (26 c.) |
| `02-boss` Q6 | l.153 « No one here is denied a library card » | le nom | non |
| `03-revision` Q1 | l.51-52 les deux listes + l.55 **la mauvaise réponse nommée** | une matière retirée | **non** |
| `03-revision` Q3 | l.161 « not a polite way of saying important » (explication) | — | **oui** (25 c.) |
| `03-revision` Q4 | l.154 « Bread and lentils are cheap and nutritious » = **la clé** | + une orange | **non** |

**16 items sur 23 — 70 % du chapitre.** Les tranches précédentes : 11, 12, 7, 7 puis 10 sur 23.
**C'est le chapitre le plus recyclé de la matière.**

Le scan de 20 caractères en désigne 16 lui aussi, mais **seulement 13 sont les bons** : il rate
`02-boss` Q2, `03-revision` Q1 et `03-revision` Q4 (mots réagencés), et il lève `quiz` Q1, `quiz` Q2
et `quiz` Q3, où la reprise est une glose de règle dans l'explication — légitime.

**Les sept items propres** : `quiz` Q1, `quiz` Q2, `quiz` Q3, `02-boss` Q3, `03-revision` Q2,
`03-revision` Q5, `03-revision` Q6. Trois sont dans la porte, **trois sur six** dans `03-revision`
— l'exercice de la seconde main. Réparti par moitié : **13 items recyclés sur les 17 de la première
main (76 %)** contre **3 sur les 6 de la seconde (50 %)**. Et **`01-pratique` est recyclé
intégralement : 6 items sur 6.**

---

## 8. Ordre de traitement conseillé

1. **BLOCKER-1** (`02-boss` Q2, explication fausse) — c'est le seul constat qui trompe activement un
   élève, et la correction tient en un paragraphe.
2. **MAJOR-10** dans la foulée (mêmes deux items du boss).
3. **BLOCKER-3, BLOCKER-4, BLOCKER-2** puis **MAJOR-2/-3/-4/-7/-8/-9/-11/-12** : **onze constats,
   toutes les corrections du côté `cours.md`/`resume.md`, aucun item calibré touché.** Une seule
   passe sur le cours les règle tous — c'est le geste le plus rentable du chapitre.
4. **MAJOR-5** (conversion de `01-pratique` Q1 en `matching`) — règle du même coup MAJOR-13 et
   MAJOR-14.
5. **MAJOR-1** (« the fourth answer ») et **MAJOR-6** (l'énoncé de `01-pratique` Q2) : deux retouches
   d'item, indépendantes.
6. Les MINOR, en dernier.

⚠️ **Après la passe sur le cours, relancer le scan de fragments** : les corrections ci-dessus
suppriment 15 des 40 fragments, dont les cinq plus longs. Un compte résiduel autour de 20 est
attendu et normal (gloses de règles dans les explications) — **il ne vaut toujours pas quitus**, et
la seule vérification qui compte reste la confrontation item par item.
