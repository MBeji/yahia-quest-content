# ⚔️ Les enregistrements — une fiche pour des données de types différents

> 💡 «Un tableau range des choses du même genre ; une fiche range tout ce qu'on sait d'une seule chose.»

Ce chapitre apprend à regrouper des informations de types différents dans une seule variable, puis à en traiter toute une liste. Quatre notions, la dernière en deux temps (traiter un vecteur, puis y chercher), avec un fil rouge : le tournoi d'échecs du lycée, où chaque joueur a sa fiche. On suppose acquis les tableaux, les intervalles et types énumérés, les procédures et fonctions avec leurs paramètres, et les boucles. Le code est donné en algorithmique (notation du programme) puis en Pascal.

## 🗂️ Définir un enregistrement : une fiche, plusieurs types

Le tournoi d'échecs du lycée accueille des joueurs. Pour chacun, le programme garde son nom (une chaîne), son année d'étude de 1 à 4 et ses points (un réel). Un tableau ne convient pas : tous ses éléments ont le même type, alors qu'une fiche de joueur mélange chaîne, entier et réel.
Comment fabriquer un type qui regroupe plusieurs informations de types différents ?

::: definition
Un **enregistrement** (on dit aussi un **article** ; mot réservé `Record` en Pascal) est un type défini par le programmeur. Il regroupe un nombre fini d'éléments appelés **champs**, chacun avec son nom et son type, et ces types peuvent être différents.
Le type d'un champ est prédéfini (Entier, Réel, Chaîne, Booléen, Caractère) ou défini plus haut par le programmeur (intervalle, type énuméré, autre enregistrement).
:::

| Champ  | Type       | Contenu de la fiche de Sana |
| ------ | ---------- | --------------------------- |
| nom    | Chaîne[20] | Sana                        |
| annee  | 1..4       | 3                           |
| points | Réel       | 12,5                        |

Chaque ligne du tableau est un champ : son nom, son type, et la valeur qu'une fiche remplie lui donne. Le type `Joueur` que l'on va déclarer est exactement la liste des deux premières colonnes.

::: exemple Déclarer le type Joueur

1. On choisit le nom du nouveau type, Joueur : on décrit un modèle de fiche, aucune fiche n'existe encore.
2. On liste les champs avec leur type : nom (chaîne d'au plus 20 caractères), annee (un intervalle 1..4, déjà connu) et points (un réel).
3. On ferme la structure : `Fin Joueur` en algorithmique, `End;` en Pascal.
4. On déclare enfin un objet j de type Joueur : c'est lui qui recevra une fiche.

:::

En algorithmique, le type va dans le tableau de déclaration des nouveaux types, l'objet dans le tableau de déclaration des objets :

```
Type
Joueur = Enregistrement
    nom : Chaîne[20]
    annee : 1..4
    points : Réel
Fin Joueur
```

| Objet | Type / Nature | Rôle              |
| ----- | ------------- | ----------------- |
| j     | Joueur        | Fiche d'un joueur |

En Pascal :

```
TYPE
  Joueur = Record
    nom    : String[20];
    annee  : 1..4;
    points : Real;
  End;
VAR
  j : Joueur;
```

Un champ peut lui-même être un enregistrement. Pour l'inscription, on garde la date de naissance : jour, mois, année.

::: exemple Un champ qui est lui-même un enregistrement

1. On décrit d'abord Date : jj de 1 à 31, mm de 1 à 12, aa entier.
2. On déclare ensuite Inscrit, dont le champ naissance est de type Date : le compilateur lit de haut en bas, il doit connaître Date au moment où il rencontre naissance.
3. La variable ins de type Inscrit contient donc un nom et, à l'intérieur, une date complète.

:::

```
TYPE
  Date = Record
    jj : 1..31;
    mm : 1..12;
    aa : Integer;
  End;
  Inscrit = Record
    nom       : String[20];
    naissance : Date;
  End;
VAR
  ins : Inscrit;
```

::: piege
**Erreur : déclarer Inscrit avant Date.** On écrit d'abord la fiche principale, puis ses détails, parce que c'est l'ordre dans lequel on y pense. Mais le champ `naissance : Date` est alors refusé : à cet endroit du texte, Date n'existe pas encore. Il faut écrire Date en premier, puis Inscrit.
:::

::: propriete
Un enregistrement se déclare en deux temps : le **type** (la liste des champs), puis l'**objet** de ce type dans la section des variables. Le type d'un champ est tout type déjà déclaré plus haut, un autre enregistrement compris.
Cas limite : déclarer le type ne crée aucune fiche. Sans la ligne `j : Joueur` dans les variables, il n'y a rien à remplir.
:::

::: verifie À toi : déclarer un type Colis
Écrire en Pascal la déclaration d'un type Colis (numero : entier, poids : réel, fragile : booléen) et d'une variable c de ce type.

---

`TYPE Colis = Record numero : Integer; poids : Real; fragile : Boolean; End;` : un type, donc le mot `Record` et trois champs séparés par des points-virgules, chacun avec son type, la structure fermée par `End;`. Puis `VAR c : Colis;` : c'est la variable c, et non le type, qui recevra un colis.
:::

::: retenir
Un enregistrement regroupe des champs nommés de types différents ; on déclare d'abord le type, puis la variable, et un type utilisé comme champ se déclare avant celui qui le contient.
:::

## 📍 Atteindre un champ : la notation pointée

La variable j est déclarée de type Joueur. Sana est en 3ème année et a 12,5 points : il faut ranger ces valeurs dans la fiche j, puis les relire. Tous les champs sont dans j, chacun avec son propre nom.
Comment désigner le champ points de j, et pas celui d'une autre fiche ?

::: definition
Le champ d'une variable enregistrement se désigne par **variable.champ** : le nom de la variable, un point, le nom du champ. Un tel champ se comporte comme une variable ordinaire du type du champ.
:::

| Opération                 | Algorithmique   | Pascal            |
| ------------------------- | --------------- | ----------------- |
| Affecter un champ         | j.points ← 12.5 | j.points := 12.5; |
| Lire un champ au clavier  | Lire (j.points) | ReadLn(j.points); |
| Écrire un champ à l'écran | Écrire (j.nom)  | Write(j.nom);     |
| Recopier toute la fiche   | k ← j           | k := j;           |

Avant le point se trouve la fiche (j), après le point le champ, avec le nom donné dans la déclaration du type : `j.points` est le champ points de la fiche j.

Voici un programme complet. Il lit une fiche, la recopie dans une seconde variable, puis modifie la copie.

```
PROGRAM Fiche_Joueur;
TYPE
  Joueur = Record
    nom    : String[20];
    annee  : 1..4;
    points : Real;
  End;
VAR
  j, k : Joueur;
BEGIN
  Write('Nom : ');    ReadLn(j.nom);
  Write('Annee : ');  ReadLn(j.annee);
  Write('Points : '); ReadLn(j.points);
  k := j;
  k.points := k.points + 2;
  WriteLn(j.nom, ' : ', j.points:0:1);
  WriteLn(k.nom, ' : ', k.points:0:1);
END.
```

::: exemple Exécuter le programme à la main avec Sana, 3 et 12.5

1. `ReadLn(j.nom)` range Sana dans le champ nom de j ; `ReadLn(j.annee)` range 3 dans annee, et `ReadLn(j.points)` range 12.5 dans points. Chaque lecture ne touche que son champ.
2. `k := j` recopie les trois champs de j dans k, car j et k ont le même type : k contient maintenant Sana, 3 et 12.5.
3. `k.points := k.points + 2` lit le champ points de k (12.5), ajoute 2 et le range dans le même champ : k.points vaut 14.5.
4. Le champ points de j n'a pas été touché : il vaut toujours 12.5.
5. L'écran affiche `Sana : 12.5` puis `Sana : 14.5`.

:::

::: piege
**Erreur : croire que `k := j` relie k et j.** On pense que k devient un autre nom de la fiche j, et que modifier k modifie j. Ce n'est pas le cas : l'affectation recopie les valeurs, et les deux fiches vivent ensuite chacune de leur côté. Ici, `k.points` passe à 14.5 pendant que `j.points` reste à 12.5. Pour changer la fiche j, il faut écrire `j.points := …`.
:::

::: propriete
On écrit toujours le nom de la **variable** devant le point, jamais celui du type : `j.points`, et non `Joueur.points`. Lire et écrire au clavier et à l'écran portent sur un champ à la fois. L'affectation globale `k := j` n'est permise qu'entre deux variables du même type.
Cas limite : si un champ est lui-même un enregistrement, on enchaîne les points. Avec ins de type Inscrit, `ins.naissance.aa := 2008` range 2008 dans le champ aa du champ naissance de ins.
:::

::: verifie À toi : lire un champ imbriqué
Avec ins de type Inscrit (section précédente), écrire l'instruction Pascal qui affiche le mois de naissance de ins.

---

`Write(ins.naissance.mm);` : on part de la variable ins, le point mène au champ naissance qui est une Date, un second point mène au champ mm de cette date, et `Write` affiche ce champ comme n'importe quel entier.
:::

::: retenir
`variable.champ` désigne un champ, qui se traite comme une variable de son type ; `k := j` recopie toute la fiche, sans lier k à j.
:::

## 🎯 Travailler sur une seule fiche : la structure Avec … Faire

Pour remplir la fiche de Sana, on écrit trois lignes, et chacune répète `j.` :

```
j.nom := 'Sana';
j.annee := 3;
j.points := 12.5;
```

Ces lignes travaillent toutes sur la même fiche.
Comment dire une seule fois « dans la fiche j » ?

::: definition
La structure **Avec … Faire** (`With … Do` en Pascal) désigne une variable enregistrement une fois pour toutes : à l'intérieur, les champs de cette variable s'écrivent par leur nom seul. Elle s'emploie avec une affectation, une lecture ou une écriture.
En algorithmique : `Avec variable Faire … Fin Avec`. En Pascal : `With variable Do Begin … End;`.
:::

```
Avec j Faire
    nom ← "Sana"
    annee ← 3
    points ← 12.5
Fin Avec
```

```
With j Do
Begin
  nom := 'Sana';
  annee := 3;
  points := 12.5;
End;
```

Les deux blocs font la même chose que les trois lignes précédentes : `nom` y est le champ nom de j, car la fiche a été désignée par `With j Do`.

::: exemple Réécrire la saisie du programme Fiche_Joueur

1. Les trois lectures travaillent sur j : on écrit `With j Do` une seule fois, devant le bloc.
2. Il y a plusieurs instructions à placer sous le With : on les entoure de `Begin` et `End;`.
3. À l'intérieur, `ReadLn(nom)` lit le champ nom de j, `ReadLn(annee)` le champ annee, `ReadLn(points)` le champ points.

:::

```
With j Do
Begin
  Write('Nom : ');    ReadLn(nom);
  Write('Annee : ');  ReadLn(annee);
  Write('Points : '); ReadLn(points);
End;
```

::: piege
**Erreur : oublier `Begin` et `End;`.** Avec `With j Do ReadLn(nom);` suivi de `ReadLn(annee);`, on croit que les deux lectures sont sous le With. Seule la première l'est : le With ne porte que sur l'instruction qui le suit. La seconde est hors du With, `annee` n'y est plus reconnu comme champ de j (aucune variable de ce nom n'existe), et le compilateur la refuse. Dès qu'il y a deux instructions, on écrit `Begin … End;`.
:::

::: propriete
Un With porte sur une seule variable enregistrement, et sur une seule instruction, ou sur le bloc `Begin … End;` qui le suit. Pour agir sur une autre variable à l'intérieur, on garde le préfixe de celle-ci : sous `With j Do`, l'instruction `k.points := points * 2` lit le champ points de j et range le résultat dans k.points.
Cas limite : en dehors du bloc, les champs ne sont plus reconnus par leur nom seul.
:::

::: verifie À toi : récrire avec Avec … Faire
Récrire en un seul With les deux instructions `j.annee := 4;` et `j.points := j.points + 1;`.

---

`With j Do Begin annee := 4; points := points + 1; End;` : les deux instructions portent sur j, donc un seul With suffit ; elles sont deux, donc `Begin … End;` est nécessaire ; dans `points := points + 1`, les deux `points` sont le champ points de j.
:::

::: retenir
`With j Do Begin … End;` évite de répéter `j.` : Begin et End dès qu'il y a plusieurs instructions, et le préfixe reste obligatoire pour une autre variable.
:::

## 📋 Traiter tout le tournoi : le vecteur d'enregistrements

Le tournoi compte N joueurs, avec 2 ≤ N ≤ 40. Il faut mémoriser N fiches, puis les parcourir pour compter, chercher, calculer un pourcentage. Un tableau convient dès que tous ses éléments sont du même type : si chaque case reçoit une fiche Joueur, la condition est remplie.
Comment déclarer ce tableau, et comment atteindre un champ de la fiche d'une case ?

::: definition
Un **vecteur d'enregistrements** est un tableau dont chaque élément est un enregistrement du même type. Si T est un tel vecteur, `T[i]` désigne la fiche de rang i et `T[i].champ` l'un de ses champs.
En algorithmique : `Tab = Tableau de 40 Joueur`. En Pascal : `Tab = Array[1..40] Of Joueur;`.
:::

| i   | T[i].nom | T[i].annee | T[i].points |
| --- | -------- | ---------- | ----------- |
| 1   | Sana     | 3          | 12,5        |
| 2   | Omar     | 2          | 9           |
| 3   | Lina     | 3          | 14          |
| 4   | Yassine  | 4          | 11,5        |

Une ligne est une fiche `T[i]` ; une colonne est un champ. `T[3].points` est la case de la ligne 3 et de la colonne points : 14.

Voici le programme complet. La procédure Saisir remplit les N premières fiches ; la fonction Compter donne le nombre de joueurs d'une année ; le programme principal affiche leur pourcentage.

```
Algorithme Tournoi
Début
    Répéter
        Écrire ("Nombre de joueurs (2 à 40) : ")
        Lire (N)
    Jusqu'à (N ≥ 2) ET (N ≤ 40)
    Saisir (T, N)
    nb ← Compter (T, N, 3)
    p ← nb * 100 / N
    Écrire (nb, " joueur(s) de 3ème année : ", p, " %")
Fin Tournoi
```

```
Procédure Saisir (Var T : Tab ; N : Entier)
Début
    Pour i de 1 à N Faire
        Avec T[i] Faire
            Écrire ("Nom : ") ; Lire (nom)
            Écrire ("Année : ") ; Lire (annee)
            Écrire ("Points : ") ; Lire (points)
        Fin Avec
    Fin Pour
Fin Saisir
```

```
Fonction Compter (T : Tab ; N, a : Entier) : Entier
Début
    nb ← 0
    Pour i de 1 à N Faire
        Si T[i].annee = a Alors
            nb ← nb + 1
        Fin Si
    Fin Pour
    Compter ← nb
Fin Compter
```

```
PROGRAM Tournoi;
TYPE
  Joueur = Record
    nom    : String[20];
    annee  : 1..4;
    points : Real;
  End;
  Tab = Array[1..40] Of Joueur;
VAR
  T : Tab;
  N, nb : Integer;
  p : Real;

PROCEDURE Saisir (Var T : Tab; N : Integer);
VAR i : Integer;
BEGIN
  FOR i := 1 TO N DO
    WITH T[i] DO
    BEGIN
      Write('Nom : ');    ReadLn(nom);
      Write('Annee : ');  ReadLn(annee);
      Write('Points : '); ReadLn(points);
    END;
END;

FUNCTION Compter (T : Tab; N, a : Integer) : Integer;
VAR i, nb : Integer;
BEGIN
  nb := 0;
  FOR i := 1 TO N DO
    IF T[i].annee = a THEN nb := nb + 1;
  Compter := nb;
END;

BEGIN
  REPEAT
    Write('Nombre de joueurs (2 a 40) : ');
    ReadLn(N);
  UNTIL (N >= 2) AND (N <= 40);
  Saisir(T, N);
  nb := Compter(T, N, 3);
  p := nb * 100 / N;
  WriteLn(nb, ' joueur(s) de 3eme annee : ', p:6:2, ' %');
END.
```

::: exemple Exécuter Tournoi avec les quatre joueurs du tableau

1. L'utilisateur tape 1, puis 50, puis 4 : la condition d'arrêt `(N >= 2) AND (N <= 40)` est fausse pour 1 et pour 50, vraie pour 4. N vaut 4.
2. `Saisir(T, 4)` remplit T[1] à T[4] : à chaque tour, `With T[i]` désigne la fiche de rang i, et `nom`, `annee`, `points` sont ses champs. Les cases T[5] à T[40] ne sont pas touchées.
3. `Compter(T, 4, 3)` met nb à 0 puis parcourt les quatre fiches : T[1].annee et T[3].annee valent 3, donc nb passe à 1 puis à 2. La fonction rend 2.
4. `p := nb * 100 / N` donne 2 × 100 / 4 = 50. Avec `p:6:2`, l'écran affiche ` 50.00` précédé d'un espace de cadrage : `2 joueur(s) de 3eme annee :  50.00 %`.

:::

::: piege
**Erreur : écrire `T.points[i]`.** On a l'habitude de tableaux séparés, un pour les noms, un pour les points, et on écrit le champ avant l'indice. Mais T est un tableau de fiches : `T.points` n'existe pas, car les champs sont dans chaque case, pas dans T. La fiche s'obtient d'abord par son rang, puis le champ : `T[i].points`.
:::

::: methode
**Traiter un vecteur d'enregistrements.**

1. Contrôler N à la saisie : on répète la lecture jusqu'à ce que N soit dans l'intervalle voulu, c'est-à-dire `Jusqu'à (N ≥ 2) ET (N ≤ 40)`.
2. Parcourir les N premières cases avec `Pour i de 1 à N`, et désigner un champ par `T[i].champ` (ou par `With T[i]`).
3. Compter : initialiser le compteur à 0, l'augmenter à chaque fiche qui vérifie le critère. Pour un pourcentage, calculer `nb * 100 / N`.
4. Passer le tableau en paramètre avec `Var` quand la procédure doit le modifier, comme Saisir ; sans `Var`, la procédure ou la fonction travaille sur une copie, ce qui suffit pour Compter. Un enregistrement seul se passe de la même façon.

Cas limites : avec `OU` à la place de `ET`, la condition d'arrêt serait vraie pour tout entier et le contrôle ne filtrerait rien ; un comptage peut valoir 0, donc une moyenne divisée par nb exige de tester nb ≠ 0 avant de diviser.
:::

::: verifie À toi : compter selon un autre champ
Dans le programme Tournoi, quelle ligne de Compter faut-il changer pour compter les joueurs dont les points sont au moins 10, et quel nombre obtient-on sur le tableau à quatre joueurs ?

---

On remplace `IF T[i].annee = a THEN` par `IF T[i].points >= 10 THEN` : le critère porte maintenant sur le champ points de la fiche de rang i. Sur le tableau, 12,5 ; 14 et 11,5 sont au moins 10, mais 9 ne l'est pas : la fonction rend 3.
:::

::: retenir
Un vecteur d'enregistrements se parcourt avec `T[i].champ` ; la saisie se fait par une procédure à paramètre `Var`, et un comptage part de 0.
:::

## 🔎 Chercher dans un vecteur : s'arrêter au bon endroit

Le comité veut retrouver la fiche d'Omar parmi les fiches du tableau, sans savoir s'il est inscrit. On parcourt les cases une à une, mais on ne sait pas d'avance où la recherche s'arrête.
Comment s'arrêter sur la bonne case, et comment savoir à la sortie si Omar a été trouvé ?

```
i ← 1
Tant que (i ≤ N) ET (T[i].nom ≠ "Omar") Faire
    i ← i + 1
Fin Tant que
Si i ≤ N Alors
    Écrire ("Trouvé au rang ", i)
Sinon
    Écrire ("Absent")
Fin Si
```

```
i := 1;
WHILE (i <= N) AND (T[i].nom <> 'Omar') DO
  i := i + 1;
IF i <= N THEN WriteLn('Trouve au rang ', i)
ELSE WriteLn('Absent');
```

::: exemple Chercher Omar, puis Hedi, dans le tableau à quatre joueurs

1. Pour Omar : T[1].nom est Sana, différent d'Omar, donc i passe à 2. T[2].nom est Omar : la condition `T[i].nom <> 'Omar'` devient fausse, la boucle s'arrête avec i = 2.
2. Comme 2 ≤ N, on affiche `Trouve au rang 2`.
3. Pour Hedi : aucun des quatre noms ne convient, i monte jusqu'à 5. Alors `i <= N` est faux et la boucle s'arrête, sans fiche trouvée.
4. Comme 5 > N, on affiche `Absent` : en sortie de boucle, i vaut N + 1 quand le nom n'est pas dans le tableau.

:::

::: piege
**Erreur : lire T[i] à la sortie sans tester i.** La boucle est finie, on croit que i désigne forcément la fiche cherchée et on écrit `WriteLn(T[i].nom)`. Mais la boucle s'arrête pour deux raisons : le nom est trouvé, ou le tableau est épuisé. Dans le second cas i vaut N + 1, une case jamais remplie, et on afficherait n'importe quoi. Il faut d'abord tester `i <= N`.
:::

::: methode
**Recherche séquentielle d'une fiche.**

1. Partir de `i ← 1`.
2. Avancer avec `Tant que (i ≤ N) ET (T[i].champ ≠ valeur cherchée)` : la borne `i ≤ N` s'écrit en premier, pour ne pas dépasser les N fiches. Pascal évalue le ET de gauche à droite et s'arrête dès que la première condition est fausse : quand i dépasse N, T[i] n'est jamais lu.
3. À la sortie, tester `i ≤ N` : vrai, la fiche cherchée est T[i] ; faux, elle est absente.

Cas limite : si la valeur apparaît dans plusieurs fiches, la boucle s'arrête sur la première rencontrée.
:::

::: verifie À toi : chercher un autre joueur
Dans le tableau à quatre joueurs (Sana, Omar, Lina, Yassine), que vaut i à la sortie de la boucle et qu'affiche-t-on pour la valeur cherchée Lina ?

---

T[1].nom (Sana) et T[2].nom (Omar) sont différents de Lina : i passe à 2 puis à 3. T[3].nom est Lina, la condition devient fausse et la boucle s'arrête avec i = 3. Comme 3 ≤ N, on affiche `Trouve au rang 3`.
:::

::: retenir
Une recherche séquentielle s'arrête sur la première fiche trouvée ou à i = N + 1 ; on teste donc i ≤ N avant de lire T[i].
:::

> 🏆 Les fiches n'ont plus de secret : tu sais les déclarer, les remplir et en traiter toute une liste. Au prochain défi, une fiche mal copiée ou un `Begin` oublié ne passera plus.
