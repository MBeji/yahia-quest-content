# Rapport d'audit — **english-bac**, tranche 4 (chapitres 10 et 11)

> **Généré** : 2026-08-17 · **Empreinte** : `wip/content-english-bac-ch10-12@5741a1ba`.
> **Périmètre audité** : `10-put-a-little-drama-in-your-travel` et `11-the-winters-tale` — 46 questions.
> ⚠️ **`12-school-related-words` N'A PAS D'AUDIT.** Ne pas merger la tranche sans le sien.
> **Méthode** : un auditeur par chapitre, contexte vierge, n'ayant écrit aucune ligne de ce qu'il
> relit, avec les onze autres chapitres en croisement. Re-résolution **à l'aveugle** de chaque clé.
> **Lecture seule — aucune correction appliquée.** Ce document est la **worklist**.

## Synthèse

| | ch.10 | ch.11 |
| --- | --- | --- |
| clés re-résolues à l'aveugle | 23 | 23 |
| **clés fausses** | **0** | **0** |
| BLOCKER | 0 | **2** |
| MAJOR | 9 | 6 |

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
