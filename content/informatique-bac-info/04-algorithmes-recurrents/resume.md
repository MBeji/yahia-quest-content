# 📜 Résumé : Les algorithmes récurrents

- **Récurrence et ordre** : un traitement récurrent calcule chaque résultat à partir des p résultats précédents (ordre 1, 2, 3, p) ; le cumul avec une variable de cumul est d'ordre 1, et l'ordre ne se lit ni dans le nombre de boucles ni dans les constantes
- **Thue-Morse** : on remplace chaque `0` par `01` et chaque `1` par `10` (`Insert`, `Length`, pas de 2 pour sauter le caractère inséré) ; récurrence d'ordre 1, longueur 2ⁿ, donc N ≤ 7 dans un `String`
- **Pascal itératif** : bords à 1, `MAT[ligne, colonne] = MAT[ligne-1, colonne] + MAT[ligne-1, colonne-1]` pour les colonnes 2 à ligne − 1 ; récurrence d'ordre 2, la voisine est celle de gauche
- **Pascal récursif** : `Val_Triangle (col, lig)` a deux cas particuliers (`col = 1` et `col = lig`) et un cas général à deux appels sur la ligne du dessus ; hors du triangle, il ne s'arrête pas
- **Fibonacci** : U(n) = U(n−1) + U(n−2), U1 = U2 = 1, ordre 2 ; deux variables, tableau ou récursivité, avec le cas N ≤ 2 rendant 1 ; la boucle de 3 à N fait N − 2 passes
- **Nombre d'or** : Fib(n+1) / Fib(n) tend vers (1 + √5) / 2 ≈ 1,618, solution positive de x² − x − 1 = 0 ; l'inverse tend vers 0,618 ; on s'arrête quand |V(n) − V(n−1)| < e, après avoir calculé V[2]
- **Suites convergentes** : on répète tant que |U(n+1) − U(n)| > e, avec la valeur absolue ; Héron et racine de N donnent (U + N / U) / 2, avec N ≥ 1
- **Débordement** : Byte 0..255, Word 0..65535, Integer −32768..32767, LongInt −2147483648..2147483647 ; un résultat hors intervalle est faux sans alerte, donc on borne le maximum ou on teste `u2 <= Limite - u1` avant d'additionner
