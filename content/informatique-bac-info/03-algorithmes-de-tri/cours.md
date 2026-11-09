# ⚔️ Les algorithmes de tri — mettre de l'ordre dans les données

> 💡 «Trier, c'est payer une fois pour que chaque recherche, ensuite, coûte beaucoup moins.»

Un tableau en désordre cache ses plus petites valeurs au hasard des cases ; un tableau trié les livre à la première case. Ce chapitre présente sept notions : ce qu'est un tri, puis les méthodes par sélection, à bulles, par insertion, de Shell et par fusion, et enfin le calcul d'un rang. Toutes les procédures sont en Pascal et trient un tableau en ordre croissant.

## 📊 Trier : un ordre, deux familles

Le classement d'une classe, les contacts d'un téléphone rangés de A à Z, les prix du moins cher au plus cher : à chaque fois, une suite d'éléments est rangée selon un ordre.
Mais un tableau de 40 moyennes en mémoire et un fichier de 10 millions de lignes se trient-ils de la même façon ?

::: definition
**Trier**, c'est ranger une suite d'éléments dans un ordre donné : croissant, décroissant ou alphabétique. C'est possible dès que l'ensemble est muni d'un **ordre total** : deux éléments quelconques sont toujours comparables.
**Tri interne** : méthode pour une masse de données limitée, stockée en mémoire centrale (un tableau).
**Tri externe** : méthode pour de grandes masses de données, stockées dans des fichiers.
:::

| Famille | Où sont les données ? | Structure | Exemple                               |
| ------- | --------------------- | --------- | ------------------------------------- |
| Interne | mémoire centrale      | tableau   | 40 moyennes dans un tableau T         |
| Externe | support de stockage   | fichier   | 10 millions de lignes dans un fichier |

Le tableau trié contient exactement les mêmes valeurs que le tableau de départ, rangées autrement. La famille se lit dans la colonne « Structure ».

::: exemple Classer trois situations

1. Trente prénoms lus dans un tableau sont rangés de A à Z : les données sont en mémoire centrale, dans un tableau, donc **tri interne**, ordre alphabétique.
2. Un fichier de 10 millions d'opérations ne tient pas en mémoire : **tri externe**, que ce chapitre ne traite pas.
3. Pour [12, 7, 9], l'ordre croissant donne [7, 9, 12] et l'ordre décroissant [12, 9, 7] : ce sont les mêmes trois valeurs, donc le tri n'ajoute ni ne retire rien ✓.

:::

::: piege
**Erreur : déclarer « non trié » un tableau décroissant.** On lit [12, 9, 7] et l'on dit « il n'est pas trié, 12 passe avant 9 ». L'erreur tente parce que l'ordre croissant est celui auquel on pense par défaut. Mais « trié » se juge par rapport à l'ordre demandé : [12, 9, 7] est trié décroissant, et c'est le tableau [7, 9, 12] qui serait « à l'envers » pour ce tri.
:::

::: propriete
Un tri conserve les valeurs : le tableau obtenu est le tableau de départ réarrangé. Le sens du tri est fixé par le test de comparaison utilisé.
Cas limite : des valeurs égales ne gênent pas, [3, 5, 5, 8] est trié croissant ; un tableau d'un seul élément est trié d'office.
:::

::: verifie À toi : la famille du tri
Un programme trie les 25 prénoms d'une classe lus dans un tableau, un autre trie les 8 millions d'enregistrements d'un fichier. Quelle famille pour chacun ?

---

Les 25 prénoms sont en mémoire centrale, dans un tableau : tri interne. Les 8 millions d'enregistrements sont une grande masse stockée dans un fichier : tri externe. La structure qui porte les données, tableau ou fichier, décide de la famille.
:::

::: retenir
Trier, c'est ranger les mêmes valeurs dans un ordre donné ; le tri interne travaille sur un tableau en mémoire centrale, le tri externe sur de grands fichiers.
:::

## 🎯 Le tri par sélection

Pour ranger cinq élèves par taille, on cherche le plus petit, on le place en tête, puis on recommence avec ceux qui restent.
Sur un tableau, où l'on ne sait qu'échanger deux cases, comment faire ?

::: definition
Le **tri par sélection** : à l'étape i, on cherche la position du plus petit élément de T[i..n] et on l'échange avec T[i]. Après n − 1 étapes, le tableau est trié, car le dernier élément est alors forcément le plus grand.
La fonction `Pos_Min (T, p, k)` rend la position du plus petit élément de T[p..k].
:::

```pascal
Type Tab = Array [1..100] Of Integer;

Function Pos_Min (T : Tab; p, k : Integer) : Integer;
Var i, m : Integer;
Begin
  m := p;
  For i := p + 1 To k Do
    If T[i] < T[m] Then m := i;
  Pos_Min := m;
End;

Procedure Tri_Selection (n : Integer; Var T : Tab);
Var i, m, aux : Integer;
Begin
  For i := 1 To n - 1 Do
  Begin
    m := Pos_Min (T, i, n);
    If m <> i Then
    Begin
      aux := T[i]; T[i] := T[m]; T[m] := aux;
    End;
  End;
End;
```

| Étape i | Pos_Min (T, i, 6) | Tableau après l'étape  |
| ------- | ----------------- | ---------------------- |
| départ  |                   | [27, 9, 34, 5, 18, 12] |
| 1       | 4 (valeur 5)      | [5, 9, 34, 27, 18, 12] |
| 2       | 2 (valeur 9)      | [5, 9, 34, 27, 18, 12] |
| 3       | 6 (valeur 12)     | [5, 9, 12, 27, 18, 34] |
| 4       | 5 (valeur 18)     | [5, 9, 12, 18, 27, 34] |
| 5       | 5 (valeur 27)     | [5, 9, 12, 18, 27, 34] |

::: exemple Suivre le tri de [27, 9, 34, 5, 18, 12]

1. Étape 1 : le plus petit de T[1..6] est 5, en case 4 ; on l'échange avec T[1], et 27 part en case 4.
2. Étape 2 : le plus petit de T[2..6] est 9, déjà en case 2 ; `m = i`, aucun échange.
3. Étapes 3 et 4 : 12 (case 6) puis 18 (case 5) viennent prendre les cases 3 et 4.
4. Étape 5 : 27 est déjà en case 5, et 34 reste en case 6 : le tableau est trié après n − 1 = 5 étapes ✓.

:::

::: piege
**Erreur : chercher le minimum dans tout le tableau à chaque étape.** On écrit `m := Pos_Min (T, 1, n)` dans la boucle. L'erreur tente parce que « le plus petit » semble se dire sans borne. Mais les cases 1 à i − 1 contiennent déjà les plus petits : à l'étape 2, `Pos_Min (T, 1, n)` rend 1 (le 5 est le minimum global) et le programme échange T[2] avec T[1] : le 5 quitte sa place. La recherche porte sur T[i..n], jamais plus loin en arrière.
:::

::: propriete
Il y a n − 1 étapes et au plus un échange par étape. Après l'étape i, les i plus petits éléments sont à leur place définitive.
Cas limite : si le minimum est déjà en case i, on n'échange rien (étapes 2 et 5 ci-dessus) ; un tableau déjà trié fait quand même les n − 1 recherches.
:::

::: verifie À toi : deux étapes de sélection
Que contient T = [6, 9, 2, 5, 3] après l'étape 2 du tri par sélection ?

---

Étape 1 : le plus petit de T[1..5] est 2, en case 3 ; on l'échange avec T[1] et T devient [2, 9, 6, 5, 3]. Étape 2 : le plus petit de T[2..5] est 3, en case 5 ; on l'échange avec T[2] et T devient [2, 3, 6, 5, 9]. La recherche de l'étape 2 commence en case 2 et ignore la case 1.
:::

::: retenir
Le tri par sélection place à l'étape i le minimum de T[i..n] en case i par un échange ; il fait n − 1 étapes.
:::

## 🫧 Le tri à bulles

Dans une file d'élèves, deux voisins mal rangés (le plus grand devant le plus petit) échangent leur place.
En parcourant la file plusieurs fois de cette façon, que garantit un parcours, et quand peut-on s'arrêter ?

::: definition
Le **tri à bulles** (bubble sort) compare les valeurs **adjacentes** T[j] et T[j+1], pour j de 1 à n − 1, et les **permute** si elles ne sont pas dans le bon ordre. Après un passage, la plus grande valeur est en dernière case : le passage suivant porte sur les cases restantes. L'algorithme s'arrête quand un passage ne fait aucune permutation.
Au pire des cas, il faut n passages : n − 1 qui permutent, puis un n-ième passage vide (fin = 1) qui constate qu'il n'y a pas eu de permutation.
:::

```pascal
Procedure Tri_Bulles (n : Integer; Var T : Tab);
Var fin, j, aux : Integer; echange : Boolean;
Begin
  fin := n;
  Repeat
    echange := False;
    For j := 1 To fin - 1 Do
      If T[j] > T[j + 1] Then
      Begin
        aux := T[j]; T[j] := T[j + 1]; T[j + 1] := aux;
        echange := True;
      End;
    fin := fin - 1;
  Until Not echange;
End;
```

::: exemple Suivre le tri de [6, 4, 9, 2, 7]

1. Passage 1 : 6 > 4 permute, 6 < 9 non, 9 > 2 permute, 9 > 7 permute. T = [4, 6, 2, 7, 9] et le 9 est à sa place.
2. Passage 2 (4 cases) : 4 < 6 non, 6 > 2 permute, 6 < 7 non. T = [4, 2, 6, 7, 9].
3. Passage 3 (3 cases) : 4 > 2 permute, 4 < 6 non. T = [2, 4, 6, 7, 9].
4. Passage 4 : aucune permutation, donc `echange` reste faux et la boucle s'arrête : 4 passages ✓.

:::

::: piege
**Erreur : croire que la plus petite valeur remonte aussi vite que la plus grande.** On pense qu'après un passage, la plus petite valeur est en tête. L'erreur tente par symétrie avec la plus grande. Mais les comparaisons ne vont que dans un sens : la plus grande voyage jusqu'au bout en un passage, la plus petite recule d'une seule case par passage. Pour [2, 3, 4, 5, 1], un passage donne [2, 3, 4, 1, 5] : le 1 n'a avancé que d'une case, et il faut 5 passages au total.
:::

::: propriete
L'ordre dépend du test : permuter quand `T[j] > T[j+1]` trie en ordre croissant, permuter quand `T[j] < T[j+1]` trie en ordre décroissant. Après k passages, les k plus grandes valeurs sont en fin de tableau.
Cas limite : avec le test `<`, [3, 8, 5] devient [8, 3, 5] à la première permutation, puis [8, 5, 3] à la fin du passage 1 ; un tableau déjà trié se termine en un seul passage.
:::

::: verifie À toi : compter les passages
Combien de passages (le dernier, sans permutation, compris) le tri à bulles fait-il sur T = [5, 1, 4, 2, 3] ?

---

Passage 1 : T = [1, 4, 2, 3, 5]. Passage 2 : 4 > 2 puis 4 > 3 permutent, T = [1, 2, 3, 4, 5]. Passage 3 : aucune permutation, la boucle s'arrête. Il y a donc 3 passages, dont le dernier ne sert qu'à vérifier.
:::

::: retenir
Le tri à bulles permute les voisins mal rangés ; chaque passage fixe la plus grande valeur restante, et il s'arrête au premier passage sans permutation.
:::

## 🃏 Le tri par insertion

Tu tiens une main de cartes : tu prends la carte suivante et tu la glisses à sa place parmi celles déjà triées, en poussant les plus grandes vers la droite.
Comment faire la même chose dans un tableau ?

::: definition
Le **tri par insertion** insère, à l'itération i (i de 2 à n), l'élément T[i] à sa place dans T[1..i − 1], qui est déjà trié. Le processus d'insertion comprend trois actions : (1) sauvegarder T[i] dans une variable intermédiaire **Tmp** ; (2) **décaler** vers la droite les éléments T[i − 1], T[i − 2], … tant qu'ils sont supérieurs à Tmp ; (3) ranger Tmp dans la case libérée, T[j + 1].
Il y a n − 1 itérations. Le manuel écrit la même idée avec une procédure `Decaler` qui rend dans p l'indice où le décalage s'est arrêté (la case libérée est p + 1), puis `T[p + 1] ← Tmp` : son p est notre j.
:::

```pascal
Procedure Tri_Insertion (n : Integer; Var T : Tab);
Var i, j, Tmp : Integer;
Begin
  For i := 2 To n Do
  Begin
    Tmp := T[i];
    j := i - 1;
    While (j >= 1) And (T[j] > Tmp) Do
    Begin
      T[j + 1] := T[j];
      j := j - 1;
    End;
    T[j + 1] := Tmp;
  End;
End;
```

| i      | Tmp | Éléments décalés | Tableau après l'itération |
| ------ | --- | ---------------- | ------------------------- |
| départ |     |                  | [14, 6, 21, 3, 9]         |
| 2      | 6   | 14               | [6, 14, 21, 3, 9]         |
| 3      | 21  | aucun            | [6, 14, 21, 3, 9]         |
| 4      | 3   | 21, 14, 6        | [3, 6, 14, 21, 9]         |
| 5      | 9   | 21, 14           | [3, 6, 9, 14, 21]         |

::: exemple Suivre l'itération i = 4

1. Au début, T[1..3] = [6, 14, 21] est trié. On sauvegarde `Tmp := T[4]`, donc Tmp = 3, car la case 4 va être recouverte.
2. j part de 3 : 21 > 3, on le copie en case 4 ; 14 > 3, on le copie en case 3 ; 6 > 3, on le copie en case 2. Alors j vaut 0 : `j >= 1` est faux et la boucle s'arrête. Turbo Pascal évalue le And de gauche à droite et s'arrête au premier terme faux (réglage par défaut {$B-}) : T[0], qui n'existe pas, n'est donc jamais lu.
3. On range `T[j + 1] := Tmp`, soit T[1] := 3 : T = [3, 6, 14, 21, 9] ✓.

:::

::: piege
**Erreur : décaler sans avoir sauvegardé T[i].** On écrit directement `T[j + 1] := T[j]` pour insérer T[i]. L'erreur tente parce que le décalage semble faire toute la place nécessaire. Mais la première recopie écrase T[i] : pour [14, 6], elle donne [14, 14] et le 6 est perdu, il n'y a plus rien à ranger. Tmp garde la valeur à l'abri jusqu'à l'étape 3.
:::

::: propriete
Si le tableau est presque trié, très peu d'éléments sont décalés et l'insertion est efficace. En moyenne, elle est d'ordre n² (deux boucles imbriquées) : chaque instruction ne déplace une valeur que d'une case. Une variante cherche la place par dichotomie, mais les décalages restent nécessaires.
Cas limite : un tableau déjà trié ne décale rien ; un tableau en ordre décroissant décale i − 1 éléments à l'itération i, le pire des cas.
:::

::: verifie À toi : deux itérations d'insertion
Pour T = [18, 7, 25, 11], que contient T après l'itération i = 3, et combien d'éléments décale l'itération i = 4 ?

---

Itération 2 : Tmp = 7, on décale 18, T = [7, 18, 25, 11]. Itération 3 : Tmp = 25, 18 < 25 donc rien ne bouge, T = [7, 18, 25, 11]. Itération 4 : Tmp = 11, on décale 25 puis 18 (7 < 11 arrête la boucle), soit 2 éléments, et T devient [7, 11, 18, 25].
:::

::: retenir
Le tri par insertion sauvegarde T[i] dans Tmp, décale vers la droite les éléments plus grands, puis range Tmp dans la case libérée.
:::

## 🐚 Le tri Shell

Avec l'insertion, une petite valeur située au bout d'un tableau de 1000 cases avance d'une case à la fois : jusqu'à 999 décalages pour elle seule.
Peut-on la faire sauter plus loin d'un coup ?

::: definition
Le **tri Shell** (Donald Shell, 1959) est une variante du tri par insertion : on trie séparément, par insertion, les **sous-vecteurs** formés des éléments distants de p cases, où p est le **pas**, puis on diminue p jusqu'à 1. Le dernier passage (p = 1) est l'insertion simple, sur un tableau déjà dégrossi.
**Suite des pas** : p ← 3p + 1 donne 1, 4, 13, 40, 121, … On monte tant que p < n, puis on redescend par p ← p Div 3.
:::

```pascal
Procedure Tri_Shell (n : Integer; Var T : Tab);
Var p, i, j, valeur : Integer;
Begin
  p := 0;
  While p < n Do p := 3 * p + 1;
  While p > 1 Do
  Begin
    p := p Div 3;
    For i := p + 1 To n Do
    Begin
      valeur := T[i];
      j := i;
      While (j > p) And (T[j - p] > valeur) Do
      Begin
        T[j] := T[j - p];
        j := j - p;
      End;
      T[j] := valeur;
    End;
  End;
End;
```

::: exemple Un passage de pas 4 sur 10 éléments

1. Les pas : p vaut 0, 1, 4, 13 ; 13 n'est pas inférieur à n = 10, la montée s'arrête. La descente donne 13 Div 3 = 4, puis 4 Div 3 = 1 : on utilise les pas 4 puis 1.
2. T = [23, 8, 41, 15, 4, 30, 12, 27, 6, 19]. Pas 4, sous-vecteurs : cases {1, 5, 9} = (23, 4, 6), {2, 6, 10} = (8, 30, 19), {3, 7} = (41, 12), {4, 8} = (15, 27).
3. Chacun est trié par insertion : (4, 6, 23), (8, 19, 30), (12, 41), et (15, 27) ne change pas. T = [4, 8, 12, 15, 6, 19, 41, 27, 23, 30].
4. Pas 1 : insertion simple, 7 décalages seulement ; T = [4, 6, 8, 12, 15, 19, 23, 27, 30, 41] ✓. Avec 4 décalages au pas 4, le total est 11, contre 25 pour l'insertion seule.

:::

::: piege
**Erreur : s'arrêter après le pas 4.** On voit que les plus grandes valeurs sont allées vers la fin et l'on juge le tableau trié. L'erreur tente parce que le désordre a beaucoup diminué. Mais le pas 4 ne compare que des cases distantes de 4 : dans [4, 8, 12, 15, 6, 19, …], le 6 est derrière 15, 12 et 8 sans jamais avoir été comparé à eux. Seul le pas 1, qui compare les voisins, garantit un tableau trié.
:::

::: propriete
Le premier pas utilisé est le plus grand terme de la suite strictement inférieur à n : 13 pour n = 14 ou 15 ; pour n = 13, c'est 4, car 13 n'est pas inférieur à 13. Le manuel écrit `Tant que p ≠ 0` : il fait en plus un passage avec p = 0, sans effet ; s'arrêter à `p > 1` donne les mêmes pas.
Cas limite : pour 2 ≤ n ≤ 4, le premier pas est déjà 1 et le tri Shell est l'insertion simple.
:::

::: verifie À toi : la suite des pas
Quels pas le tri Shell utilise-t-il, dans l'ordre, pour n = 45 ?

---

La montée donne p = 0, 1, 4, 13, 40 (40 < 45), puis 121 : on s'arrête sur 121, qui n'est pas inférieur à 45. La descente donne 121 Div 3 = 40, 40 Div 3 = 13, 13 Div 3 = 4, 4 Div 3 = 1. Les pas sont donc 40, 13, 4, 1.
:::

::: retenir
Le tri Shell applique l'insertion à des sous-vecteurs de pas p décroissant (3p + 1 vers le haut, Div 3 vers le bas) et finit toujours par le pas 1.
:::

## 🔀 La fusion de deux tableaux triés

Deux listes d'élèves, une par classe, sont déjà triées par moyenne. Pour obtenir la liste de l'année, inutile de tout retrier : on compare les deux premiers de chaque liste, le meilleur passe en tête, et l'on continue.
Comment automatiser ce geste ?

::: definition
La **fusion** (ou **interclassement**) construit, à partir de deux tableaux triés T1 (n1 éléments) et T2 (n2 éléments), un tableau trié T de n1 + n2 éléments. Deux positions c1 et c2 parcourent T1 et T2 : on compare T1[c1] et T2[c2], on recopie le plus petit dans T et on avance dans son tableau. Quand un tableau est épuisé, on recopie le **reste** de l'autre.
:::

```pascal
Procedure Fusionner (T1 : Tab; n1 : Integer; T2 : Tab; n2 : Integer; Var T : Tab);
Var c, c1, c2 : Integer;
Begin
  c := 0; c1 := 1; c2 := 1;
  While (c1 <= n1) And (c2 <= n2) Do
  Begin
    c := c + 1;
    If T1[c1] < T2[c2] Then
    Begin T[c] := T1[c1]; c1 := c1 + 1; End
    Else
    Begin T[c] := T2[c2]; c2 := c2 + 1; End;
  End;
  While c1 <= n1 Do
  Begin c := c + 1; T[c] := T1[c1]; c1 := c1 + 1; End;
  While c2 <= n2 Do
  Begin c := c + 1; T[c] := T2[c2]; c2 := c2 + 1; End;
End;
```

::: exemple Fusionner [4, 9, 15, 22] et [6, 7, 18]

1. T aura n1 + n2 = 4 + 3 = 7 cases. On compare 4 et 6 : 4 est recopié ; puis 9 et 6 : 6 ; puis 9 et 7 : 7 ; puis 9 et 18 : 9 ; puis 15 et 18 : 15.
2. On compare 22 et 18 : 18 est recopié, et T2 est épuisé. La boucle principale s'arrête après 6 comparaisons.
3. Il reste 22 dans T1, déjà trié et plus grand que tout ce qui est recopié : on le recopie sans comparaison.
4. T = [4, 6, 7, 9, 15, 18, 22] ✓.

:::

::: piege
**Erreur : s'arrêter dès qu'un tableau est épuisé.** On pense que la fusion est finie quand T2 est vide. L'erreur tente parce que la boucle de comparaison s'arrête à ce moment-là. Mais T1 contient encore 22 : sans la recopie du reste, la case 7 de T n'est jamais remplie et la valeur 22 est perdue. Les deux boucles de recopie finales sont indispensables.
:::

::: propriete
La fusion suppose deux tableaux déjà triés. Le **tri par fusion** s'en sert selon le principe « diviser pour régner » : couper le tableau en deux, trier chaque moitié (par la même méthode, de façon récursive), puis fusionner. Pour [8, 3, 6, 1] : [8, 3] devient [3, 8], [6, 1] devient [1, 6], et la fusion donne [1, 3, 6, 8]. Son inconvénient est le tableau intermédiaire, aussi grand que le tableau à trier.
Cas limite : pour [1, 2, 3] et [7, 8], on fait 3 comparaisons, puis 7 et 8 sont recopiés sans comparaison.
:::

::: verifie À toi : une fusion
On fusionne T1 = [2, 10, 11] et T2 = [3, 5, 12, 14]. Quelle est la taille de T, combien de comparaisons sont faites, et quelles valeurs sont recopiées sans comparaison ?

---

T a 3 + 4 = 7 cases. On compare 2 et 3 (2), 10 et 3 (3), 10 et 5 (5), 10 et 12 (10), 11 et 12 (11) : T1 est épuisé après 5 comparaisons. Il reste 12 et 14 dans T2, recopiés sans comparaison : T = [2, 3, 5, 10, 11, 12, 14].
:::

::: retenir
La fusion de deux tableaux triés compare leurs têtes, recopie la plus petite, puis recopie le reste de l'autre ; le tri par fusion coupe, trie les moitiés, puis fusionne.
:::

## 🏅 Rang et comptage

Un professeur veut afficher le rang de chacun de ses 30 élèves selon la moyenne, sans trier le tableau ni déplacer personne.
Comment calculer le rang d'un élève, et peut-on en tirer un tri ?

::: definition
Le **rang** d'un élève vaut 1 plus le nombre d'élèves dont la moyenne est **strictement supérieure** à la sienne. Deux moyennes égales donnent le même rang (ex æquo). Un **tableau d'enregistrements** (Nom, Moy, Rang) garde liés les champs d'un élève ; avec trois tableaux parallèles, chaque échange devrait être refait sur les trois.
Le **tri par comptage** range chaque élément en case 1 + (nombre d'éléments strictement inférieurs) d'un tableau résultat R, si les valeurs sont distinctes.
:::

```pascal
Type Eleve = Record Nom : String; Moy : Real; Rang : Integer; End;
     Tab_El = Array [1..30] Of Eleve;

Procedure Rechercher_Rang (n : Integer; Var E : Tab_El);
Var i, j : Integer;
Begin
  For i := 1 To n Do
  Begin
    E[i].Rang := 1;
    For j := 1 To n Do
      If E[j].Moy > E[i].Moy Then E[i].Rang := E[i].Rang + 1;
  End;
End;
```

::: exemple Calculer des rangs, puis un tri par comptage

1. Moyennes : Amel 14,5 ; Bilel 12 ; Chaima 16 ; Dali 14,5 ; Emna 9,75. Chaima n'a personne au-dessus : rang 1 ; Amel et Dali n'ont que Chaima au-dessus : rang 2 chacune (ex æquo).
2. Bilel a trois élèves au-dessus (Chaima, Amel, Dali) : rang 4. Il n'y a pas de rang 3, et Emna, avec quatre élèves au-dessus, a le rang 5.
3. Comptage de T = [17, 4, 12, 9, 25, 1] : 17 a 4 valeurs inférieures, donc il va en case 5 de R ; 4 en case 2 ; 12 en case 4 ; 9 en case 3 ; 25 en case 6 ; 1 en case 1.
4. R = [1, 4, 9, 12, 17, 25] ✓ : on n'a jamais déplacé T, on a seulement compté.

:::

::: piege
**Erreur : compter avec `>=` au lieu de `>`.** On écrit `If E[j].Moy >= E[i].Moy`. L'erreur tente parce que « au moins aussi bon » semble équitable. Mais j = i est toujours vrai : l'élève se compte lui-même, et Chaima obtient 2 au lieu de 1. De plus Amel et Dali se comptent mutuellement et reçoivent le rang 4 au lieu de 2. Le rang compte seulement ceux qui sont strictement meilleurs.
:::

::: propriete
Le calcul des rangs ne change pas l'ordre du tableau : il fait n × n comparaisons avec deux boucles. Le tri par création (ou par rangement) procède autrement : on cherche le minimum de la partie qui reste, on le range dans un vecteur résultat, puis on recommence.
Cas limite : le comptage exige des valeurs distinctes ; pour [5, 5, 2], les deux 5 ont une seule valeur inférieure et visent la même case 2, la case 3 de R n'est jamais remplie.
:::

::: verifie À toi : un rang
Cinq élèves ont pour moyennes 11, 15, 15, 9 et 12. Quels rangs reçoivent les moyennes 12 et 9 ?

---

Pour 12, deux moyennes lui sont strictement supérieures (15 et 15) : rang 1 + 2 = 3. Pour 9, quatre moyennes sont strictement supérieures (11, 15, 15, 12) : rang 1 + 4 = 5. Les deux 15 sont ex æquo au rang 1, donc il n'y a pas de rang 2.
:::

::: retenir
Le rang vaut 1 plus le nombre de valeurs strictement supérieures ; le comptage utilise 1 plus le nombre de valeurs strictement inférieures pour trouver la case d'un élément.
:::

> 🗡️ Pour reconnaître un tri sur une trace, regarde l'état intermédiaire : minimum placé en tête (sélection), plus grande valeur en fin (bulles), début trié mais incomplet (insertion), éléments éloignés comparés (Shell), deux tableaux triés recopiés (fusion).

> 🏆 Porte franchie ! Tu sais ranger un tableau de cinq façons et calculer des rangs sans rien déplacer. Prochaine arène : les algorithmes récurrents.
