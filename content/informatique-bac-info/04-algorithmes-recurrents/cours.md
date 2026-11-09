# ⚔️ Les algorithmes récurrents — chaque résultat s'appuie sur les précédents

> 💡 «Une suite se construit pas à pas : pour écrire le terme suivant, il suffit de relire ceux qui le précèdent.»

Additionner des cases, bâtir une chaîne, remplir un triangle, calculer les termes d'une suite : tous ces algorithmes avancent en réutilisant ce qu'ils viennent de produire. Ce chapitre apprend à les reconnaître, à les classer par ordre et à les écrire en pseudo-langage et en Pascal. Huit notions : le cumul, Thue-Morse, le triangle de Pascal (itératif puis récursif), Fibonacci, le nombre d'or, les suites convergentes et les débordements de type.

## 🔗 Récurrence, ordre et cumul

Pour additionner les cases d'une matrice, on garde un total et on lui ajoute chaque case : le total d'une étape se déduit du total de l'étape précédente.
Comment classer les calculs dont chaque résultat dépend de résultats déjà obtenus ?

::: definition
Un algorithme ou un traitement est **récurrent** s'il utilise un procédé itératif ou récursif pour engendrer un résultat qui peut dépendre de p résultats précédents : il est alors **récurrent d'ordre p**.
**Ordre 1** : le résultat dépend du résultat précédent. **Ordre 2** : il dépend des deux résultats précédents. **Ordre 3** : des trois résultats précédents.
Un **cumul** range le total courant dans une **variable de cumul**, initialisée avant la boucle.
:::

```
0) Fonction Somme_Mat (M : MAT ; N : Entier non signé) : Entier
1) S ← 0
   Pour ligne de 1 à N Faire
      Pour colonne de 1 à N Faire
         S ← S + M [ligne, colonne]
      Fin Pour
   Fin Pour
2) Somme_Mat ← S
3) Fin Somme_Mat
```

```pascal
Function Somme_Mat (M : Mat; N : Word) : LongInt;
Var S : LongInt; ligne, colonne : Word;
Begin
  S := 0;
  For ligne := 1 To N Do
    For colonne := 1 To N Do S := S + M[ligne, colonne];
  Somme_Mat := S;
End;
```

::: exemple Suivre le cumul sur une matrice 2 × 2
La matrice est M = [[1, 2], [3, 4]].

1. Initialisation : S = 0, avant toute case.
2. Case [1,1] : S = 0 + 1 = 1. Case [1,2] : S = 1 + 2 = 3.
3. Case [2,1] : S = 3 + 3 = 6. Case [2,2] : S = 6 + 4 = 10.
4. À chaque pas, le nouveau S ne dépend que du S précédent (et de la case lue) : le traitement est récurrent d'ordre 1, et la fonction rend 10 ✓.

:::

::: piege
**Erreur : lire l'ordre dans le nombre de boucles.** On voit deux boucles imbriquées dans `Somme_Mat` et l'on écrit « ordre 2 ». L'erreur tente parce que les boucles sont visibles et que le mot « ordre » évoque un nombre. Mais l'ordre compte les résultats précédents dont dépend le nouveau résultat : ici S ne dépend que de l'ancien S, donc l'ordre est 1, quel que soit le nombre de boucles.
:::

::: propriete
L'ordre est le nombre de résultats précédents nécessaires pour calculer le suivant. Une factorielle F ← F × i est d'ordre 1, une suite où chaque terme dépend des deux précédents est d'ordre 2.
Cas limite : une constante ne compte pas dans l'ordre. S ← S + 5 est d'ordre 1, car 5 n'est pas un résultat précédent.
:::

::: verifie À toi : trouver l'ordre
Donner l'ordre de la suite P(n) = P(n−1) × n, puis celui de la suite Q(n) = 3 × Q(n−1) − Q(n−2).

---

P(n) ne dépend que de P(n−1) : ordre 1. Q(n) a besoin de Q(n−1) et de Q(n−2) : ordre 2. Les nombres 3 et n ne sont pas des résultats précédents, ils n'entrent pas dans l'ordre.
:::

::: retenir
Un traitement récurrent d'ordre p calcule chaque résultat à partir des p résultats précédents ; le cumul est d'ordre 1, et l'ordre ne se lit pas dans le nombre de boucles.
:::

## 🔤 La suite de Thue-Morse : récurrence sur les chaînes

On part de la chaîne `0` et, à chaque étape, on remplace chaque `0` par `01` et chaque `1` par `10` : `0`, puis `01`, puis `0110`.
Comment programmer cette substitution sur une chaîne, et quelle taille prend-elle ?

::: definition
La **suite de Thue-Morse** est une suite de chaînes binaires : U0 = A (le caractère `0` ou `1`), puis U(n) s'obtient en remplaçant dans U(n−1) chaque `0` par `01` et chaque `1` par `10`. Chaque terme dépend du seul terme précédent : récurrence d'ordre 1.
`Insert (s, ch, p)` insère la chaîne `s` dans `ch` à la position `p` ; `Length (ch)` donne la longueur.
Termes en partant de `0` : U0 = `0`, U1 = `01`, U2 = `0110`, U3 = `01101001`, U4 = `0110100110010110`.
:::

```pascal
Function Thue_Morse (N : Word; A : Char) : String;
Var Ch : String; i, j, L : Word;
Begin
  Ch := A;
  For i := 1 To N Do
  Begin
    j := 1;
    Repeat
      If Ch[j] = '0' Then Insert ('1', Ch, j + 1)
      Else Insert ('0', Ch, j + 1);
      L := Length (Ch);
      j := j + 2;
    Until j > L;
  End;
  Thue_Morse := Ch;
End;
```

::: exemple Passer de U1 à U2
On part de Ch = `01`.

1. j = 1 : Ch[1] = `0`, donc `Insert ('1', Ch, 2)` donne `011`. La longueur L vaut 3, et j devient 3.
2. j = 3 ≤ 3 : Ch[3] = `1`, donc `Insert ('0', Ch, 4)` donne `0110`. L vaut 4, et j devient 5.
3. j = 5 > 4 : la boucle `Repeat` s'arrête. Le pas de 2 saute le caractère qu'on vient d'insérer.
4. Résultat : `0110`, soit U2 ✓.

:::

::: piege
**Erreur : croire que U(n) a n + 1 caractères.** On écrit « U4 a 5 caractères », comme si l'on ajoutait un caractère par étape. L'erreur tente parce que l'indice augmente de 1 à chaque étape. Mais chaque caractère est remplacé par deux : la longueur double, donc U(n) a 2ⁿ caractères. U4 en a 16, comme `0110100110010110` le montre.
:::

::: propriete
La longueur de U(n) vaut 2ⁿ. Un `String` Pascal contient au plus 255 caractères, donc N ≤ 7 (2⁷ = 128, mais 2⁸ = 256).
Cas limite : pour N = 0, la boucle `For` ne s'exécute pas et la fonction rend A tel quel.
:::

::: verifie À toi : la taille de U5
Combien de caractères a U5 ? Peut-on le ranger dans un `String` ?

---

U5 a 2⁵ = 32 caractères, soit le double des 16 de U4. 32 ≤ 255 : un `String` suffit.
:::

::: retenir
Thue-Morse est une récurrence d'ordre 1 sur les chaînes : chaque caractère donne deux caractères (`Insert`, pas de 2), donc la longueur double à chaque terme.
:::

## 🔺 Le triangle de Pascal : version itérative

`1` / `1 1` / `1 2 1` / `1 3 3 1` : chaque ligne se déduit de la ligne du dessus. On veut afficher les n premières lignes.
Comment remplir un tableau MAT avec ces lignes ?

::: definition
Dans le **triangle de Pascal**, la ligne l contient l éléments. Le premier et le dernier valent 1. Les autres se calculent par `MAT [ligne, colonne] = MAT [ligne-1, colonne] + MAT [ligne-1, colonne-1]`.
Chaque élément dépend de deux résultats de la ligne précédente : récurrence d'ordre 2.
:::

```pascal
Const Max = 20;
Type Mat = Array [1..Max, 1..Max] Of LongInt;

Procedure Remplir_Mat (N : Word; Var T : Mat);
Var ligne, colonne : Word;
Begin
  T[1, 1] := 1;
  For ligne := 2 To N Do
  Begin
    T[ligne, 1] := 1;
    T[ligne, ligne] := 1;
    For colonne := 2 To ligne - 1 Do
      T[ligne, colonne] := T[ligne - 1, colonne] + T[ligne - 1, colonne - 1];
  End;
End;
```

::: exemple Construire la ligne 5
La ligne 4 contient 1 3 3 1.

1. Les bords valent 1 : MAT[5,1] = 1 et MAT[5,5] = 1.
2. MAT[5,2] = MAT[4,2] + MAT[4,1] = 3 + 1 = 4.
3. MAT[5,3] = MAT[4,3] + MAT[4,2] = 3 + 3 = 6.
4. MAT[5,4] = MAT[4,4] + MAT[4,3] = 1 + 3 = 4.
5. La ligne 5 est 1 4 6 4 1 ✓ : la boucle des colonnes va de 2 à ligne − 1, car les bords sont posés à part.

:::

::: piege
**Erreur : prendre la case du dessus à droite.** On calcule MAT[5,2] avec MAT[4,2] + MAT[4,3], donc 3 + 3 = 6 au lieu de 4. L'erreur tente parce que le triangle est symétrique et que, sur les petites lignes, la case de droite donne le même résultat : pour la ligne 4, MAT[3,2] + MAT[3,3] vaut bien 3. Mais la formule utilise la case du dessus et sa voisine de **gauche**, colonne − 1.
:::

::: propriete
Le remplissage se fait ligne après ligne : une ligne n'est calculée qu'une fois la précédente complète. Les lignes 1 et 2 n'ont pas de case intérieure.
Cas limite : pour ligne = 2, la boucle `For colonne := 2 To 1` est vide, et la ligne vaut simplement 1 1.
:::

::: verifie À toi : la ligne 6
Calculer la ligne 6 à partir de la ligne 5 : 1 4 6 4 1.

---

Les bords valent 1. Les cases intérieures : 4 + 1 = 5, 6 + 4 = 10, 4 + 6 = 10, 1 + 4 = 5. La ligne 6 est donc 1 5 10 10 5 1.
:::

::: retenir
Le triangle de Pascal est une récurrence d'ordre 2 : bords à 1, et chaque case intérieure est la somme de la case au-dessus et de sa voisine de gauche.
:::

## 🪜 Le triangle de Pascal : version récursive

Pour connaître la case de la ligne 5, colonne 3, on peut éviter de remplir tout le tableau : elle est la somme de deux cases de la ligne 4, qui se calculent de la même façon.
Comment écrire une fonction qui rend une case à elle seule ?

::: definition
`Val_Triangle (col, lig)` rend l'élément de la colonne col et de la ligne lig.
**Cas particulier** : `col = 1` ou `col = lig` (un bord) : la valeur est 1.
**Cas général** : `Val_Triangle (col, lig - 1) + Val_Triangle (col - 1, lig - 1)`, deux appels récursifs sur la ligne du dessus.
:::

```pascal
Function Val_Triangle (col, lig : Integer) : Integer;
Begin
  If (col = 1) Or (col = lig) Then Val_Triangle := 1
  Else Val_Triangle := Val_Triangle (col, lig - 1) + Val_Triangle (col - 1, lig - 1);
End;
```

::: exemple Calculer Val_Triangle (3, 5)
Le cas général s'applique, car 3 n'est ni 1 ni 5.

1. `Val_Triangle (3, 5)` = `Val_Triangle (3, 4)` + `Val_Triangle (2, 4)`.
2. `Val_Triangle (3, 4)` = `Val_Triangle (3, 3)` + `Val_Triangle (2, 3)` = 1 + 2 = 3, car (3,3) est un bord et (2,3) = (2,2) + (1,2) = 1 + 1.
3. `Val_Triangle (2, 4)` = `Val_Triangle (2, 3)` + `Val_Triangle (1, 3)` = 2 + 1 = 3.
4. Donc `Val_Triangle (3, 5)` = 3 + 3 = 6 ✓, la valeur de MAT[5,3] de la version itérative.

:::

::: piege
**Erreur : n'écrire qu'un seul cas d'arrêt.** On pose `Si col = 1 Alors 1` et l'on oublie la diagonale. L'erreur tente parce que le bord gauche est le plus facile à voir. Mais `Val_Triangle (2, 2)` appelle alors (2, 1) puis (2, 0), (2, −1), … : lig décroît sans jamais atteindre `col = 1`, donc l'appel ne s'arrête pas. Les deux bords sont deux cas particuliers.
:::

::: propriete
La fonction ne s'arrête que pour 1 ≤ col ≤ lig, les cases réelles du triangle. À chaque appel, lig diminue de 1 : on se rapproche d'un bord.
Cas limite : pour une case hors du triangle comme (3, 2), col dépasse lig, aucun bord n'est atteint et l'appel ne s'arrête pas.
:::

::: verifie À toi : une case récursive
Que rend `Val_Triangle (2, 4)` ? Quels appels lance-t-il en tout ?

---

`Val_Triangle (2, 4)` = (2, 3) + (1, 3). Le terme (1, 3) est un bord et vaut 1. Le terme (2, 3) = (2, 2) + (1, 2) = 1 + 1 = 2. Le résultat est 2 + 1 = 3. Les appels sont (2,4), (2,3), (1,3), (2,2) et (1,2), soit 5 appels.
:::

::: retenir
Val_Triangle a deux cas particuliers (col = 1 et col = lig) et un cas général à deux appels sur la ligne du dessus ; hors du triangle, il ne s'arrête pas.
:::

## 🐇 La suite de Fibonacci en trois versions

Un couple de lapins donne un nouveau couple chaque saison dès qu'il est adulte. Le nombre de couples est 1, 1, 2, 3, 5, 8, 13, … : chaque nombre est la somme des deux précédents.
Comment calculer le N-ième terme ?

::: definition
La **suite de Fibonacci** vérifie U(n) = U(n−1) + U(n−2) avec U1 = 1 et U2 = 1 : c'est une récurrence d'ordre 2.
Trois solutions : **sans tableau** (deux variables u1 et u2 qui gardent les deux derniers termes), **avec tableau** T (tous les termes sont rangés), **récursive** (deux appels).
:::

```pascal
Function Fibo_It1 (N : Word) : LongInt;
Var u1, u2, F : LongInt; i : Word;
Begin
  u1 := 1; u2 := 1; F := 1;
  If N > 2 Then
    For i := 3 To N Do
    Begin
      F := u1 + u2;
      u1 := u2;
      u2 := F;
    End;
  Fibo_It1 := F;
End;
```

```pascal
Function Fibo_It2 (N : Word) : LongInt;
Var T : Array [1..40] Of LongInt; i : Word;
Begin
  T[1] := 1; T[2] := 1;
  For i := 3 To N Do T[i] := T[i - 1] + T[i - 2];
  Fibo_It2 := T[N];
End;

Function Fibo_Rec (N : Word) : LongInt;
Begin
  If N <= 2 Then Fibo_Rec := 1
  Else Fibo_Rec := Fibo_Rec (N - 1) + Fibo_Rec (N - 2);
End;
```

::: exemple Suivre Fibo_It1 (6)
Au départ, u1 = 1 et u2 = 1.

1. i = 3 : F = 1 + 1 = 2, puis u1 = 1 et u2 = 2.
2. i = 4 : F = 1 + 2 = 3, puis u1 = 2 et u2 = 3.
3. i = 5 : F = 2 + 3 = 5, puis u1 = 3 et u2 = 5.
4. i = 6 : F = 3 + 5 = 8, puis u1 = 5 et u2 = 8. La fonction rend 8 ✓.

:::

::: piege
**Erreur : croire que la boucle fait N passes.** On suit `Fibo_It1 (6)` en comptant 6 itérations. L'erreur tente parce que le paramètre vaut 6. Mais les deux premiers termes sont déjà posés : la boucle va de 3 à N, soit N − 2 passes (4 pour N = 6). Chaque passe produit un nouveau terme, du rang 3 au rang N.
:::

::: propriete
Les trois versions rendent la même valeur pour 1 ≤ N ≤ 40. Elles diffèrent par la mémoire : deux variables, N cases, ou la pile des appels.
Cas limite : pour N ≤ 2, la boucle de 3 à N est vide et le résultat est 1. Si une source commence la suite à 0 (0, 1, 1, 2, …), tous les rangs sont décalés d'un cran.
:::

::: verifie À toi : un terme de Fibonacci
Que rend `Fibo_Rec (7)` ? Combien de termes ont été ajoutés pour l'obtenir avec `Fibo_It1` ?

---

La suite est 1, 1, 2, 3, 5, 8, 13 : `Fibo_Rec (7)` rend 13. Avec `Fibo_It1 (7)`, la boucle va de 3 à 7 : 5 passes, donc 5 additions.
:::

::: retenir
Fibonacci est d'ordre 2 : U(n) = U(n−1) + U(n−2), avec U1 = U2 = 1 ; deux variables, un tableau ou la récursivité donnent le même terme.
:::

## 🌟 Le nombre d'or

Dans la suite 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, on divise chaque terme par le précédent, ou le suivant par le terme courant : les quotients semblent se rapprocher d'un même nombre.
Quel est ce nombre, et comment un programme s'arrête-t-il quand il l'a atteint ?

::: definition
La suite V(n) = Fib(n+1) / Fib(n) converge vers le **nombre d'or** λ = (1 + √5) / 2 ≈ 1,618, solution positive de l'équation x² − x − 1 = 0.
Un programme s'arrête avec une **précision e** dès que |V(n) − V(n−1)| < e.
:::

| n   | Fib(n+1) / Fib(n) | valeur approchée |
| --- | ----------------- | ---------------- |
| 3   | 3 / 2             | 1,5000           |
| 4   | 5 / 3             | 1,6667           |
| 5   | 8 / 5             | 1,6000           |
| 6   | 13 / 8            | 1,6250           |
| 7   | 21 / 13           | 1,6154           |
| 8   | 34 / 21           | 1,6190           |
| 9   | 55 / 34           | 1,6176           |

Le Bac pratique 2004 pose U1 = 1, U2 = 2, U(i) = U(i−1) + U(i−2), et V(i) = U(i) / U(i−1) pour i ≥ 2.

```pascal
Var U : Array [1..100] Of LongInt;
    V : Array [1..100] Of Real;
    i : Integer;
BEGIN
  U[1] := 1; U[2] := 2;
  V[2] := U[2] / U[1];
  i := 2;
  Repeat
    i := i + 1;
    U[i] := U[i - 1] + U[i - 2];
    V[i] := U[i] / U[i - 1];
  Until Abs (V[i] - V[i - 1]) < 0.0001;
  WriteLn ('Nombre d''or : ', V[i]:0:5, ' au rang ', i);
END.
```

::: exemple Vérifier λ et trouver le rang

1. λ² = (1 + √5)² / 4 = (6 + 2√5) / 4 = (3 + √5) / 2, et λ + 1 = (3 + √5) / 2 : λ² = λ + 1, donc λ² − λ − 1 = 0 ✓.
2. Avec U = 1, 2, 3, 5, 8, …, le quotient V(i) vaut Fib(i+1) / Fib(i) : V(10) = 89 / 55 ≈ 1,618182 et V(11) = 144 / 89 ≈ 1,617978.
3. L'écart |V(11) − V(10)| vaut 0,000204, supérieur à 0,0001 : la boucle continue.
4. V(12) = 233 / 144 ≈ 1,618056, et l'écart |V(12) − V(11)| vaut 0,000078 < 0,0001 : arrêt au rang 12, avec 1,61806.

:::

::: piege
**Erreur : inverser le rapport.** On calcule Fib(n) / Fib(n+1), soit 8 / 13 ≈ 0,615, et l'on croit approcher λ. L'erreur tente parce que les deux quotients portent les mêmes nombres. Mais l'inverse tend vers 1 / λ ≈ 0,618, pas vers 1,618. Le rapport du terme suivant au terme courant tend vers λ.
:::

::: propriete
La condition |V(i) − V(i−1)| < e mesure l'écart entre deux quotients consécutifs, pas l'écart à λ : c'est un critère d'arrêt pratique.
Cas limite : V[2] doit être calculé avant la boucle. Sans cela, le premier test, au rang 3, compare V[3] à une case jamais affectée.
:::

::: verifie À toi : un quotient
Calculer V(13) = Fib(14) / Fib(13) arrondi à 10⁻⁴.

---

Fib(13) = 233 et Fib(14) = 377. Le quotient 377 / 233 = 1,618025… arrondi à 10⁻⁴ donne 1,6180.
:::

::: retenir
Fib(n+1) / Fib(n) tend vers λ = (1 + √5) / 2 ≈ 1,618, racine positive de x² − x − 1 = 0 ; on s'arrête quand deux quotients consécutifs diffèrent de moins de e.
:::

## 🎯 Suites convergentes et condition d'arrêt

Pour calculer √N sans fonction toute faite, on part de U0 = N / 2 et l'on répète U(n+1) = (U(n) + N / U(n)) / 2. Les termes se rapprochent de √N, mais ne l'atteignent pas forcément.
Quand s'arrêter de calculer ?

::: definition
Une suite récurrente **converge** quand ses termes se rapprochent d'une limite. En programme, on ne peut pas calculer indéfiniment : on répète **tant que** l'écart entre deux termes consécutifs reste supérieur à la précision e, soit `Tant que |U(n+1) − U(n)| > e`.
La suite de Héron a la même formule : U(n)/2 + x/(2U(n)) = (U(n) + x/U(n)) / 2.
:::

```pascal
Function Racine (N : Word) : Real;
Var U, V : Real;
Begin
  U := N / 2;
  V := (U + N / U) / 2;
  While Abs (V - U) > 0.000001 Do
  Begin
    U := V;
    V := (U + N / U) / 2;
  End;
  Racine := V;
End;
```

::: exemple Racine de 2 à 10⁻⁶ près

1. U0 = 1, puis U1 = (1 + 2/1) / 2 = 1,5.
2. U2 = (1,5 + 2/1,5) / 2 ≈ 1,416667 et U3 ≈ 1,414216 : les écarts 0,083 et 0,00245 sont supérieurs à 10⁻⁶.
3. U4 ≈ 1,414214 : l'écart |U4 − U3| vaut environ 2,1 × 10⁻⁶, encore supérieur à 10⁻⁶ ; on calcule U5.
4. L'écart |U5 − U4| est inférieur à 10⁻⁶ : la boucle s'arrête, et `Racine (2)` rend 1,4142136 ✓.

:::

::: piege
**Erreur : oublier la valeur absolue.** On écrit `While V - U > 0.000001`. L'erreur tente parce qu'un écart se pense positif. Mais la suite décroît dès U1 : après une première passe (U1 − U0 = 0,5), V − U = U2 − U1 ≈ −0,083 est négatif, donc plus petit que 10⁻⁶, et la boucle s'arrête au deuxième test. Pour N = 2, on obtient V = 1,4166667 au lieu de 1,4142136.
:::

::: propriete
La précision e se règle sur le besoin : plus e est petit, plus on calcule de termes. La suite logistique du manuel, x(n+1) = 4 × x(n) × (1 − x(n)), se calcule de même terme à terme (x0 = 0,2 : x1 = 0,64, puis x2 = 0,9216), mais elle ne converge pas en général : on y calcule un nombre n de termes donné, sans test de précision.
Cas limite : pour N = 0, U0 vaut 0 et `N / U` divise par zéro : `Racine` suppose N ≥ 1.
:::

::: verifie À toi : un terme de Héron
Pour N = 9, calculer U0 et U1. Vers quelle valeur la suite converge-t-elle ?

---

U0 = 9 / 2 = 4,5 et U1 = (4,5 + 9 / 4,5) / 2 = (4,5 + 2) / 2 = 3,25. La suite converge vers √9 = 3.
:::

::: retenir
Une suite convergente se calcule jusqu'à ce que deux termes consécutifs diffèrent de moins de e, avec une valeur absolue dans le test.
:::

## 💥 Débordement des types entiers

Les termes de Fibonacci grandissent vite : le terme 24 vaut 46368. Un type entier ne peut pourtant pas ranger n'importe quelle valeur.
Jusqu'à quel rang peut-on calculer sans erreur ?

::: definition
Chaque type entier couvre un intervalle : `Byte` de 0 à 255, `Word` de 0 à 65535, `Integer` de −32768 à 32767 (16 bits), `LongInt` de −2147483648 à 2147483647 (32 bits).
Un **débordement** a lieu quand un résultat sort de l'intervalle : il est faux, sans message d'erreur avec les réglages par défaut du compilateur (sans vérification d'intervalle). Pour savoir si u1 + u2 tient dans une limite, on teste `u2 <= Limite - u1` **avant** d'additionner.
:::

```pascal
Const Limite = 32767;
Var u1, u2, u3 : LongInt; rang : Word;
BEGIN
  u1 := 1; u2 := 1; rang := 2;
  While u2 <= Limite - u1 Do
  Begin
    u3 := u1 + u2; u1 := u2; u2 := u3;
    rang := rang + 1;
  End;
  WriteLn ('Rang ', rang, ' : ', u2);
END.
```

::: exemple Le dernier terme sous 32767

1. Les termes sont rangés dans des `LongInt`, qui ne débordent pas ici ; la limite 32767 est celle de `Integer`.
2. Quand u1 = 17711 (rang 22) et u2 = 28657 (rang 23), le test compare 28657 à 32767 − 17711 = 15056.
3. 28657 > 15056 : la boucle s'arrête, car le terme suivant, 17711 + 28657 = 46368, dépasserait 32767.
4. Le programme affiche le rang 23 et le terme 28657 : c'est le dernier terme qui tient dans un `Integer` ✓.

:::

::: piege
**Erreur : tester la somme après l'avoir rangée.** On calcule `u3 := u1 + u2` dans un `Integer`, puis on teste `u3 <= Limite`. L'erreur tente parce que le test paraît naturel. Mais la somme a déjà débordé : 46368 devient −19168 dans un `Integer`, négatif donc inférieur à la limite, et la boucle continue avec des valeurs fausses.
:::

::: propriete
Pour choisir un type, on borne la plus grande valeur possible du résultat. Une somme de 400 entiers entre 0 et 1000 atteint 400000, au-delà de 32767 : il faut un `LongInt`.
Cas limite : avec `Integer`, le type du manuel, le triangle de Pascal du début déborde aux lignes 19 et 20, dont les éléments centraux valent 48620 et 92378.
:::

::: verifie À toi : choisir le type
Les termes d'une suite sont sommés pour 100 entiers compris entre 0 et 500. Quel type faut-il : `Integer` ou `LongInt` ?

---

La somme maximale est 100 × 500 = 50000, supérieure à 32767 : un `Integer` déborderait. Il faut un `LongInt`, qui atteint 2147483647.
:::

::: retenir
Un type entier a un intervalle fixe ; un résultat qui en sort est faux sans alerte, donc on borne la valeur maximale avant de choisir le type ou on teste avant d'additionner.
:::

> 🗡️ Devant une suite, pose toujours trois questions : de quels résultats précédents dépend-elle, comment démarre-t-elle, et quand s'arrête-t-on ?

> 🏆 Porte franchie ! Tu sais lire, écrire et arrêter un algorithme récurrent. Prochaine arène : les algorithmes d'arithmétique.
