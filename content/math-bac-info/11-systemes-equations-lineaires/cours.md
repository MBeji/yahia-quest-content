# ⚔️ Systèmes d'équations linéaires — le tableau qui résout tout

> 💡 «Un système de trois équations à trois inconnues tient dans un tableau de nombres. Apprends à calculer avec ce tableau, et la solution sort d'un produit, d'un pivot ou d'un quotient de déterminants.»

Bienvenue, héros de la section Sciences de l'informatique. Les ingénieurs de l'ère des ordinateurs ne résolvent pas les systèmes à la main : ils rangent les coefficients dans une matrice et laissent un programme ou un tableur calculer. Huit étapes te mènent de la matrice au système de Cramer : matrices et somme, produit de matrices, déterminant, propriétés du déterminant, matrice inverse, pivot de Gauss, forme matricielle AX = B, formules de Cramer. On suppose acquis le calcul sur les systèmes de deux équations (substitution, élimination).

Dans tout le chapitre, une matrice s'écrit **ligne par ligne**, les lignes étant séparées par « ; » : (1 2 ; 3 4) a pour lignes (1 2) et (3 4). Un vecteur-colonne s'écrit donc (x ; y ; z), et un déterminant |a b ; c d|.

## 🗂️ Matrices : ranger les nombres, les additionner, les agrandir

Une station-service note, pour deux jours, les litres vendus : sans plomb 1200 et 1400, super 900 et 800, gazole 2100 et 1900.
Six nombres, trois carburants, deux jours : comment les ranger dans un seul objet qui garde la trace du carburant et du jour, et comment cumuler deux séries de ventes ?

::: definition
Une **matrice** de dimension n × p est un tableau de nombres réels rangés en **n lignes** et **p colonnes**. On la note M = (aᵢⱼ) : aᵢⱼ est le **coefficient** de la ligne i et de la colonne j, avec 1 ≤ i ≤ n et 1 ≤ j ≤ p.

Une matrice à une seule ligne est un **vecteur-ligne**, à une seule colonne un **vecteur-colonne**. Si n = p, la matrice est **carrée** d'ordre n.
:::

::: exemple Lire et cumuler des ventes
Les ventes de la première série forment M = (1200 1400 ; 900 800 ; 2100 1900) : lignes sans plomb, super, gazole ; colonnes jour 1, jour 2. Une seconde série donne N = (1000 1100 ; 1000 700 ; 1800 2200).

1. M a trois lignes et deux colonnes : sa dimension est 3 × 2. Le coefficient a₃₂ = 1900 est à la ligne 3 (gazole) et à la colonne 2 (jour 2).
2. Pour cumuler les deux séries, on additionne les coefficients de même position, car chaque case désigne le même carburant le même jour : M + N = (2200 2500 ; 1900 1500 ; 3900 4100).
3. Si chaque vente augmente de 10 %, on multiplie chaque coefficient par 1,1 : 1,1 × M = (1320 1540 ; 990 880 ; 2310 2090).

:::

::: piege Lire aᵢⱼ en colonne puis ligne
Pour M, on lit a₂₁ comme « colonne 2, ligne 1 » et l'on trouve 1400. Cela tente parce qu'on lit « 2 puis 1 » comme une abscisse puis une ordonnée. Mais le premier indice est toujours la **ligne** : a₂₁ est à la ligne 2 et à la colonne 1, soit 900 (le super du jour 1).
:::

::: propriete
Pour des matrices A, B, C de même dimension n × p et un réel k :

- A + B est la matrice des sommes de coefficients de même position, kA celle des coefficients multipliés par k ; A − B désigne A + (−1)B ;
- A + B = B + A, (A + B) + C = A + (B + C) et k(A + B) = kA + kB.

La **matrice nulle** θ, dont tous les coefficients sont nuls, vérifie A + θ = A. La **matrice unité** Iₙ est la matrice carrée dont la diagonale est formée de 1 et les autres coefficients de 0 ; une matrice **diagonale** n'a de coefficients non nuls que sur sa diagonale. Deux matrices sont **égales** si elles ont la même dimension et les mêmes coefficients aux mêmes positions.

Cas limite : la somme n'existe que pour deux matrices de même dimension, même si elles ont autant de coefficients (une matrice 2 × 3 et une matrice 3 × 2 ne s'additionnent pas).
:::

::: verifie
Soit A = (2 −1 ; 0 3 ; 5 4) et B = (1 0 ; −2 6 ; 3 −4). Calculer 2A − B.

---

On écrit 2A − B = 2A + (−1)B et l'on travaille case par case : 2A = (4 −2 ; 0 6 ; 10 8), puis on retranche chaque coefficient de B, ce qui donne (3 −2 ; 2 0 ; 7 12). Les deux matrices ont la même dimension 3 × 2, donc la différence est définie.
:::

::: retenir
Une matrice n × p range des nombres en n lignes et p colonnes, aᵢⱼ se lit ligne i puis colonne j, et l'on additionne ou multiplie par un réel case par case, à condition d'avoir la même dimension.
:::

## ✖️ Le produit de deux matrices

Une boulangerie fabrique des baguettes et des croissants. Une baguette demande 250 g de farine, 5 g de beurre et 10 g de sucre ; un croissant, 100 g de farine, 60 g de beurre et 30 g de sucre. Lundi, elle sort 40 baguettes et 30 croissants ; mardi, 60 baguettes et 20 croissants.
Comment obtenir d'un seul calcul les besoins en farine, beurre et sucre de chaque jour ?

::: definition
Soit A une matrice n × p et B une matrice p × q : le nombre de colonnes de A est égal au nombre de lignes de B. Le **produit** A × B est la matrice n × q dont le coefficient de la ligne i et de la colonne k est :

cᵢₖ = aᵢ₁b₁ₖ + aᵢ₂b₂ₖ + … + aᵢₚbₚₖ

C'est le produit de la ligne i de A par la colonne k de B. Si le nombre de colonnes de A n'est pas égal au nombre de lignes de B, le produit n'est pas défini.
:::

::: exemple Les besoins de la boulangerie
Les recettes forment R = (250 100 ; 5 60 ; 10 30) : lignes farine, beurre, sucre ; colonnes baguette, croissant. La production forme P = (40 60 ; 30 20) : lignes baguette, croissant ; colonnes lundi, mardi.

1. R est de dimension 3 × 2 et P de dimension 2 × 2 : R a 2 colonnes et P a 2 lignes, donc R × P est défini, de dimension 3 × 2.
2. Farine du lundi : ligne 1 de R par colonne 1 de P, soit 250 × 40 + 100 × 30 = 13000 g. Chaque terme est une quantité par pièce fois le nombre de pièces.
3. De même, farine du mardi 250 × 60 + 100 × 20 = 17000, beurre du lundi 5 × 40 + 60 × 30 = 2000, beurre du mardi 1500, sucre du lundi 1300, sucre du mardi 1200.
4. Donc R × P = (13000 17000 ; 2000 1500 ; 1300 1200). Le produit P × R n'est pas défini : P a 2 colonnes, R a 3 lignes.

:::

::: piege Croire que A × B = B × A
Pour A = (1 1 ; 0 1) et B = (1 0 ; 2 1), on calcule A × B = (3 1 ; 2 1), puis B × A = (1 1 ; 2 3). Ces matrices sont différentes. Cela surprend parce que le produit de deux réels est commutatif, mais ici chaque coefficient mêle une ligne et une colonne, et l'ordre des facteurs décide de ce que l'on mélange. On garde donc l'ordre exact des facteurs.
:::

::: propriete
Pour des matrices dont les produits sont définis :

- A × (B × C) = (A × B) × C, A × (B + C) = A × B + A × C et A × Iₙ = Iₙ × A = A ;
- en général A × B ≠ B × A, et A × B = θ n'entraîne pas A = θ ou B = θ ;
- pour une matrice carrée A, Aⁿ = A × A × … × A (n facteurs) ; pour une matrice diagonale D, Dⁿ s'obtient en élevant chaque coefficient de la diagonale à la puissance n.

Cas limite : (1 −1 ; −1 1) × (1 1 ; 1 1) = θ, alors qu'aucun des deux facteurs n'est nul.
:::

::: exemple Les puissances d'une matrice
Avec A = (1 1 ; 0 1) : A² = A × A = (1 2 ; 0 1), puis A³ = A² × A = (1 3 ; 0 1). On conjecture Aⁿ = (1 n ; 0 1). Le passage de n à n + 1 le confirme : Aⁿ⁺¹ = Aⁿ × A = (1 n ; 0 1) × (1 1 ; 0 1) = (1 n+1 ; 0 1).

:::

::: verifie
Soit C = (1 2 0 ; 3 −1 4) et D = (2 1 ; 0 5 ; −1 3). Le produit C × D est-il défini, et que vaut-il ?

---

C est de dimension 2 × 3 et D de dimension 3 × 2 : le nombre de colonnes de C est égal au nombre de lignes de D, donc C × D est défini, de dimension 2 × 2. La ligne 1 de C par la colonne 1 de D donne 2, par la colonne 2 donne 11 ; la ligne 2 donne 2 et 10. Donc C × D = (2 11 ; 2 10).
:::

::: retenir
Le produit A × B existe quand le nombre de colonnes de A égale le nombre de lignes de B, chaque coefficient est un produit ligne par colonne, et A × B ≠ B × A en général.
:::

## 🔢 Le déterminant d'ordre 2 et 3

Les systèmes {2x + 3y = 5 ; 4x + 6y = 7} et {2x + 3y = 5 ; 4x + 5y = 7} se ressemblent. Le premier n'a aucune solution, car la seconde équation a ses coefficients doubles de la première mais pas son second membre ; le second en a une.
Existe-t-il un nombre, calculé avec les seuls coefficients, qui dise si un système de deux équations a une solution unique ?

::: definition
Le **déterminant** de la matrice carrée M = (a b ; c d) est le réel :

det(M) = |a b ; c d| = ad − bc
:::

::: exemple Les deux systèmes de départ

1. Pour le premier système, la matrice des coefficients est (2 3 ; 4 6) : det = 2 × 6 − 3 × 4 = 0. Les deux lignes sont proportionnelles.
2. Pour le second, (2 3 ; 4 5) : det = 2 × 5 − 3 × 4 = −2, non nul. Les lignes ne sont pas proportionnelles et le système a une solution unique.

:::

::: propriete
Pour une matrice carrée M = (aᵢⱼ) d'ordre 3, on développe suivant la première ligne, avec une alternance de signes + − + :

det(M) = a₁₁ × |a₂₂ a₂₃ ; a₃₂ a₃₃| − a₁₂ × |a₂₁ a₂₃ ; a₃₁ a₃₃| + a₁₃ × |a₂₁ a₂₂ ; a₃₁ a₃₂|

Chaque déterminant 2 × 2 est obtenu en supprimant la ligne et la colonne du coefficient devant lequel il se trouve. On peut développer suivant n'importe quelle ligne ou colonne, en donnant au coefficient aᵢⱼ le signe (−1)ⁱ⁺ʲ, c'est-à-dire la grille + − + ; − + − ; + − +.

Cas limite : une ligne ou une colonne de zéros donne un déterminant nul, et développer suivant une ligne riche en zéros abrège le calcul.
:::

::: exemple Développer deux fois le même déterminant
Soit M = (2 0 1 ; 3 1 −2 ; 1 4 0).

1. Suivant la ligne 1, avec les signes + − + : det = 2 × |1 −2 ; 4 0| − 0 × |3 −2 ; 1 0| + 1 × |3 1 ; 1 4| = 2 × 8 + 0 + 11 = 27.
2. Suivant la colonne 2, qui contient un zéro, avec les signes − + − : det = −0 × |3 −2 ; 1 0| + 1 × |2 1 ; 1 0| − 4 × |2 1 ; 3 −2| = 0 + (−1) − 4 × (−7) = 27.
3. Les deux développements donnent 27, ce qui vaut contrôle.

:::

::: piege Garder les signes de la première ligne partout
Développons M suivant la ligne 2 avec les signes + − + de la ligne 1 : 3 × (−4) − 1 × (−1) + (−2) × 8 = −27. Cela tente parce qu'on réutilise la grille déjà apprise. Mais les signes de la ligne 2 sont − + − : −3 × (−4) + 1 × (−1) − (−2) × 8 = 12 − 1 + 16 = 27. Le résultat avait changé de signe.
:::

::: verifie
Calculer le déterminant de A = (1 2 0 ; 0 3 −1 ; 4 0 2) en développant suivant la ligne 1.

---

On a det(A) = 1 × |3 −1 ; 0 2| − 2 × |0 −1 ; 4 2| + 0 × |0 3 ; 4 0|. Le premier déterminant vaut 3 × 2 − (−1) × 0 = 6, le deuxième 0 × 2 − (−1) × 4 = 4, et le troisième terme disparaît à cause du facteur 0. Donc det(A) = 6 − 2 × 4 = −2.
:::

::: retenir
Le déterminant d'ordre 2 vaut ad − bc ; celui d'ordre 3 se développe suivant une ligne ou une colonne avec les signes (−1)ⁱ⁺ʲ ; un déterminant nul signale des lignes dépendantes.
:::

## 🔧 Propriétés du déterminant

Un déterminant 3 × 3 demande une dizaine de produits, et une erreur de signe est vite arrivée. Avec des zéros, le calcul serait court.
Peut-on fabriquer des zéros sans changer la valeur du déterminant ?

::: propriete
Pour une matrice carrée M, les mêmes règles valent pour les lignes et pour les colonnes :

- permuter deux lignes change le signe du déterminant ;
- deux lignes identiques ou proportionnelles donnent un déterminant nul ;
- on peut mettre en facteur un réel commun à tous les coefficients d'une ligne ;
- remplacer une ligne par elle-même plus une combinaison des autres lignes, par exemple L₂ ← L₂ − 2L₁, ne change pas le déterminant.

:::

::: exemple Fabriquer des zéros
Soit M = (1 2 3 ; 2 5 4 ; 3 7 8).

1. On annule les coefficients sous le 1 de la première colonne avec L₂ ← L₂ − 2L₁ et L₃ ← L₃ − 3L₁. Ces opérations ne changent pas le déterminant.
2. On obtient (1 2 3 ; 0 1 −2 ; 0 1 −1). En développant suivant la colonne 1, qui n'a plus qu'un coefficient non nul, det(M) = 1 × |1 −2 ; 1 −1| = −1 + 2 = 1.
3. Contrôle par le développement suivant la ligne 1 de M : 1 × 12 − 2 × 4 + 3 × (−1) = 1 ✓.

:::

::: piege Penser que det(kM) = k × det(M)
Soit M une matrice 3 × 3 de déterminant 5. On écrit det(3M) = 3 × 5 = 15. Cela tente parce qu'on pense à « multiplier par 3 ». Mais 3M a **chaque** ligne multipliée par 3 : on met en facteur 3 trois fois, une par ligne, donc det(3M) = 3³ × 5 = 135.
:::

::: propriete
Pour des matrices carrées M et N de même ordre n et un réel k :

- det(kM) = kⁿ × det(M) et det(Mᵗ) = det(M) ;
- det(M × N) = det(M) × det(N), propriété admise ;
- un déterminant dont tous les coefficients sous la diagonale (ou tous ceux au-dessus) sont nuls vaut le produit des coefficients de la diagonale.

Cas limite : en général det(M + N) ≠ det(M) + det(N), et la propriété du produit ne s'étend pas à la somme.
:::

::: exemple Un triangle de zéros
Pour T = (2 5 −1 ; 0 3 4 ; 0 0 −2), det(T) = 2 × 3 × (−2) = −12 : en développant suivant la colonne 1, on retrouve 2 × |3 4 ; 0 −2| = 2 × (−6), et ce déterminant se développe de même.

:::

::: verifie
Calculer |1 1 2 ; 1 3 5 ; 2 2 7| à l'aide de L₂ ← L₂ − L₁ et L₃ ← L₃ − 2L₁.

---

Ces deux opérations ne changent pas la valeur du déterminant et donnent (1 1 2 ; 0 2 3 ; 0 0 3). Cette matrice est triangulaire : le déterminant vaut le produit des coefficients de la diagonale, 1 × 2 × 3 = 6.
:::

::: retenir
Permuter deux lignes change le signe, une combinaison avec les autres lignes ne change rien, un facteur commun sort, det(kM) = kⁿ det(M) et det(M × N) = det(M) × det(N).
:::

## ↩️ La matrice inverse

Un message (x ; y) est codé en (2x + y ; 5x + 3y), c'est-à-dire multiplié par A = (2 1 ; 5 3). Pour le décoder, il faut une matrice qui défait A, comme multiplier par 1/5 défait « × 5 ».
Une telle matrice existe-t-elle, et comment la calculer ?

::: definition
Une matrice carrée M d'ordre n est **inversible** s'il existe une matrice carrée, notée M⁻¹, telle que M × M⁻¹ = M⁻¹ × M = Iₙ. Cette matrice **inverse** est alors unique. Si elle n'existe pas, M n'est pas inversible.
:::

::: propriete
Une matrice carrée d'ordre 2, M = (a b ; c d), est inversible si et seulement si det(M) ≠ 0, et alors :

M⁻¹ = (1/det(M)) × (d −b ; −c a)

On échange a et d, on change le signe de b et de c, puis on divise par le déterminant.
:::

::: exemple Décoder le message

1. Pour A = (2 1 ; 5 3), det(A) = 2 × 3 − 1 × 5 = 1, non nul : A est inversible.
2. On échange 2 et 3, on change le signe de 1 et de 5 : A⁻¹ = (3 −1 ; −5 2), et le facteur 1/1 ne change rien.
3. Contrôle : A × A⁻¹ = (2 × 3 + 1 × (−5), 2 × (−1) + 1 × 2 ; 5 × 3 + 3 × (−5), 5 × (−1) + 3 × 2) = (1 0 ; 0 1) ✓.

:::

::: piege Changer le signe de a et de d
Pour M = (3 1 ; 4 2), on écrit M⁻¹ = (1/2) × (3 −1 ; −4 2), en changeant le signe de b et de c sans échanger a et d. Cela tente parce que « les signes changent ». Mais M × (3 −1 ; −4 2) a pour première ligne (3 × 3 + 1 × (−4), …) = (5 …), qui n'est pas celle de 2I₂. La bonne matrice est (1/2) × (2 −1 ; −4 3).
:::

::: propriete
Une matrice carrée d'ordre 3 est inversible si et seulement si son déterminant est non nul, et alors det(M⁻¹) = 1/det(M), car det(M) × det(M⁻¹) = det(I₃) = 1.

Pour la calculer, on utilise trois notions. La **transposée** Mᵗ s'obtient en échangeant lignes et colonnes. Le **mineur** de aᵢⱼ est le déterminant 2 × 2 obtenu en supprimant la ligne i et la colonne j ; le **cofacteur** est αᵢⱼ = (−1)ⁱ⁺ʲ fois ce mineur. La **comatrice** Com M est la matrice des cofacteurs, et :

M⁻¹ = (1/det(M)) × (Com M)ᵗ
:::

::: exemple Inverser une matrice d'ordre 3
Soit A = (1 1 0 ; 0 1 1 ; 1 0 1).

1. det(A) = 1 × |1 1 ; 0 1| − 1 × |0 1 ; 1 1| + 0 = 1 + 1 = 2, non nul : A est inversible.
2. α₁₁ = +|1 1 ; 0 1| = 1, α₁₂ = −|0 1 ; 1 1| = 1, α₁₃ = +|0 1 ; 1 0| = −1, et de même pour les six autres cofacteurs : Com A = (1 1 −1 ; −1 1 1 ; 1 −1 1).
3. On transpose, puis on divise par 2 : A⁻¹ = (1/2) × (1 −1 1 ; 1 1 −1 ; −1 1 1).
4. Contrôle sur la première ligne de A × A⁻¹ : (1 + 1 + 0, −1 + 1 + 0, 1 − 1 + 0)/2 = (2, 0, 0)/2 = (1 0 0) ✓.

:::

::: verifie
Calculer l'inverse de M = (3 −1 ; 2 2).

---

det(M) = 3 × 2 − (−1) × 2 = 8, non nul. On échange 3 et 2, on change le signe de −1 et de 2 : M⁻¹ = (1/8) × (2 1 ; −2 3).
:::

::: retenir
M est inversible si et seulement si det(M) ≠ 0 ; en ordre 2, M⁻¹ = (1/det) × (d −b ; −c a) ; en ordre 3, M⁻¹ = (1/det) × (Com M)ᵗ, avec la transposée.
:::

## 🎯 Le pivot de Gauss et l'inversion par les lignes

Un snack propose trois articles dont on ignore les prix en dinars : x pour un sandwich, y pour un jus, z pour un gâteau. Trois commandes sont payées : 1 sandwich, 1 jus et 1 gâteau coûtent 9 ; 2 sandwichs, 1 jus et 2 gâteaux coûtent 16 ; 1 sandwich, 3 jus et 2 gâteaux coûtent 16.
Comment retrouver les prix sans calculer neuf cofacteurs ?

::: propriete
On range les coefficients et les seconds membres dans la **matrice augmentée** du système. Trois **opérations élémentaires** sur les lignes donnent un système équivalent, qui a les mêmes solutions : échanger deux lignes (Lᵢ ↔ Lⱼ), multiplier une ligne par un réel non nul (Lᵢ ← kLᵢ), ajouter à une ligne un multiple d'une autre (Lᵢ ← Lᵢ + kLⱼ).

Le **pivot de Gauss** consiste à les enchaîner pour annuler les coefficients sous chaque pivot, puis à remonter de la dernière équation à la première.
:::

::: exemple Les prix du snack
Le système est x + y + z = 9, 2x + y + 2z = 16, x + 3y + 2z = 16. Sa matrice augmentée est (1 1 1 | 9 ; 2 1 2 | 16 ; 1 3 2 | 16).

1. Avec L₂ ← L₂ − 2L₁ et L₃ ← L₃ − L₁, on supprime x des lignes 2 et 3 : (1 1 1 | 9 ; 0 −1 0 | −2 ; 0 2 1 | 7). Chaque opération touche aussi le second membre.
2. Avec L₃ ← L₃ + 2L₂, on supprime y de la ligne 3 : (1 1 1 | 9 ; 0 −1 0 | −2 ; 0 0 1 | 3).
3. On remonte : z = 3, puis −y = −2 donne y = 2, puis x = 9 − 2 − 3 = 4. Un sandwich coûte 4 dinars, un jus 2 et un gâteau 3.
4. Contrôle sur la deuxième commande : 2 × 4 + 2 + 2 × 3 = 16 ✓.

:::

::: piege Oublier le second membre
Pour supprimer x de la ligne 2, on écrit L₂ ← L₂ − 2L₁ sur les seuls coefficients et l'on garde 16 : (0 −1 0 | 16). Cela tente parce que le second membre semble « à part ». Mais une ligne est une équation entière : on aurait −y = 16, un prix négatif. La bonne ligne est (0 −1 0 | 16 − 2 × 9) = (0 −1 0 | −2).
:::

::: methode
Pour inverser une matrice carrée A par les lignes : (1) écrire (A | Iₙ) ; (2) enchaîner les opérations élémentaires, toujours sur la ligne entière, jusqu'à obtenir Iₙ à gauche ; (3) lire A⁻¹ à droite, car les mêmes opérations transforment Iₙ en A⁻¹.

Cas limite : si un pivot est nul, on échange deux lignes. Si on ne peut plus en trouver un non nul dans la colonne, A n'est pas inversible. Une ligne (0 0 0 | c) avec c ≠ 0 rend le système impossible ; avec c = 0, elle ne dit plus rien et il reste une infinité de solutions.
:::

::: exemple Inverser la matrice du snack
Soit S = (1 1 1 ; 2 1 2 ; 1 3 2) et (S | I₃).

1. L₂ ← L₂ − 2L₁ et L₃ ← L₃ − L₁ donnent (1 1 1 | 1 0 0 ; 0 −1 0 | −2 1 0 ; 0 2 1 | −1 0 1).
2. L₃ ← L₃ + 2L₂ donne la ligne (0 0 1 | −5 2 1), puis L₂ ← −L₂ donne (0 1 0 | 2 −1 0).
3. L₁ ← L₁ − L₂ − L₃ donne (1 0 0 | 4 −1 −1) : à gauche on lit I₃, et à droite S⁻¹ = (4 −1 −1 ; 2 −1 0 ; −5 2 1).
4. Contrôle sur la première ligne de S × S⁻¹ : (4 + 2 − 5, −1 − 1 + 2, −1 + 0 + 1) = (1 0 0) ✓.

:::

::: verifie
Inverser A = (1 4 ; 2 9) avec les lignes de (A | I₂).

---

L₂ ← L₂ − 2L₁ donne (1 4 | 1 0 ; 0 1 | −2 1). Il reste à annuler le 4 : L₁ ← L₁ − 4L₂ donne (1 0 | 9 −4 ; 0 1 | −2 1). La partie gauche est I₂, donc A⁻¹ = (9 −4 ; −2 1).
:::

::: retenir
Les opérations élémentaires sur les lignes, appliquées à la ligne entière, conservent les solutions ; le pivot de Gauss triangularise puis remonte, et (A | Iₙ) devient (Iₙ | A⁻¹).
:::

## 🧮 Écrire un système sous la forme AX = B

Chaque semaine, le snack reçoit de nouvelles commandes avec les mêmes quantités d'articles mais d'autres sommes à payer. Le pivot de Gauss oblige à tout refaire à chaque fois.
Peut-on résoudre une fois pour toutes, puis réutiliser le travail pour toute nouvelle colonne de seconds membres ?

::: definition
Un système de n équations à n inconnues s'écrit **sous forme matricielle** A × X = B : A est la matrice des coefficients, X le vecteur-colonne des inconnues et B celui des seconds membres. On passe d'un côté à l'autre en développant le produit ligne par colonne.
:::

::: propriete
Si A est inversible, c'est-à-dire si det(A) ≠ 0, le système A × X = B a une solution et une seule, X = A⁻¹ × B. Si le système n'a aucune solution ou en a une infinité, A n'est pas inversible.

Dans un tableur, PRODUITMAT(A ; B) calcule A × B et INVERSEMAT(A) calcule A⁻¹, en validant la formule sur toute la plage avec Ctrl Maj Entrée.
:::

::: exemple De nouvelles commandes
Avec S = (1 1 1 ; 2 1 2 ; 1 3 2) et S⁻¹ = (4 −1 −1 ; 2 −1 0 ; −5 2 1), une nouvelle série de commandes coûte B = (6 ; 10 ; 13).

1. Le système s'écrit S × X = B, avec X = (x ; y ; z) : la première ligne du produit est x + y + z, la deuxième 2x + y + 2z, la troisième x + 3y + 2z.
2. Comme det(S) = −1 est non nul, on multiplie à gauche par S⁻¹ : S⁻¹ × (S × X) = X, donc X = S⁻¹ × B.
3. X = (4 × 6 − 10 − 13 ; 2 × 6 − 10 ; −5 × 6 + 2 × 10 + 13) = (1 ; 2 ; 3). Contrôle : 1 + 2 + 3 = 6 ✓.

:::

::: piege Écrire X = B × A⁻¹
Pour résoudre A × X = B, on écrit X = B × A⁻¹. Cela tente parce qu'on « divise par A » comme on divise dans ℝ. Mais le produit de matrices n'est pas commutatif : ici B est 3 × 1 et A⁻¹ est 3 × 3, et le produit n'est même pas défini. On multiplie à gauche des deux membres : A⁻¹ × (A × X) = A⁻¹ × B.
:::

::: exemple Un polynôme annulateur
Soit C = (2 1 1 ; 1 2 1 ; 1 1 2).

1. On calcule C² = (6 5 5 ; 5 6 5 ; 5 5 6), donc C² − 5C = −4I₃.
2. On met C en facteur : C × (C − 5I₃) = −4I₃, donc C × ((5I₃ − C)/4) = I₃. La matrice C est inversible et C⁻¹ = (5I₃ − C)/4 = (1/4) × (3 −1 −1 ; −1 3 −1 ; −1 −1 3).
3. Pour C × X = (3 ; 4 ; 1), X = C⁻¹ × (3 ; 4 ; 1) = (1/4) × (9 − 4 − 1 ; −3 + 12 − 1 ; −3 − 4 + 3) = (1 ; 2 ; −1).

:::

::: verifie
Soit A⁻¹ = (3 −1 ; −5 2) et B = (4 ; 7). Quelle est la solution de A × X = B ?

---

A est inversible, donc X = A⁻¹ × B, avec A⁻¹ à gauche. X = (3 × 4 − 1 × 7 ; −5 × 4 + 2 × 7) = (5 ; −6).
:::

::: retenir
Un système carré s'écrit A × X = B ; si det(A) ≠ 0, il a une solution unique X = A⁻¹ × B, avec A⁻¹ multiplié à gauche.
:::

## ✂️ Les formules de Cramer et le paramètre

Le système {2x + y − z = 11 ; x + 3y = 10 ; −y − z = −1} se résout par pivot de Gauss.
Peut-on obtenir x seul, sans toucher aux autres inconnues, par le quotient de deux nombres ?

::: definition
Un **système de Cramer** est un système M × X = K de n équations à n inconnues (n = 2 ou 3) dont la matrice M vérifie det(M) ≠ 0.
:::

::: propriete
Un système de Cramer d'ordre 3 a une solution unique, donnée par xᵢ = det(Mᵢ) / det(M), où Mᵢ est la matrice M dont la i-ème colonne est remplacée par la colonne K des seconds membres. La règle est la même pour n = 2.

Cas limite : si det(M) = 0, les formules n'ont pas de sens ; on étudie alors le système par élimination, et il est impossible ou a une infinité de solutions.
:::

::: exemple Résoudre par Cramer
Pour le système de départ, M = (2 1 −1 ; 1 3 0 ; 0 −1 −1) et K = (11 ; 10 ; −1).

1. En développant suivant la ligne 1, det(M) = 2 × (−3) − 1 × (−1) + (−1) × (−1) = −6 + 1 + 1 = −4, non nul : le système est de Cramer.
2. Pour x, on remplace la colonne 1 par K : det(M₁) = |11 1 −1 ; 10 3 0 ; −1 −1 −1| = −16, donc x = −16/−4 = 4.
3. De même det(M₂) = −8 et det(M₃) = 4, donc y = 2 et z = −1.
4. Contrôle sur la deuxième équation : 4 + 3 × 2 = 10 ✓.

:::

::: piege Remplacer la mauvaise colonne
Pour trouver x, on remplace la colonne 2 par K et l'on obtient −8/−4 = 2. Cela tente parce que K est « le bon vecteur » et que l'on oublie quelle colonne appartient à quelle inconnue. Mais la colonne i correspond à l'inconnue xᵢ : la colonne 2 donne y, pas x. Pour x, on remplace la colonne 1.
:::

::: exemple Un système avec paramètre
Soit m un réel et (S) : m x + y = 2, x + m y = 2.

1. La matrice (m 1 ; 1 m) a pour déterminant m² − 1, nul si m = 1 ou m = −1.
2. Si m ≠ ±1, le système est de Cramer : x = (2m − 2)/(m² − 1) = 2/(m + 1), et y = 2/(m + 1) de même.
3. Si m = 1, les deux équations deviennent x + y = 2 : une infinité de solutions. Si m = −1, elles deviennent −x + y = 2 et x − y = 2, qui s'ajoutent en 0 = 4 : aucune solution.

:::

::: verifie
Le système {x + 2y = 7 ; 3x − y = 7} est-il de Cramer ? Que vaut x ?

---

det = 1 × (−1) − 2 × 3 = −7, non nul : le système est de Cramer. Pour x, on remplace la colonne 1 par (7 ; 7) : det(M₁) = 7 × (−1) − 2 × 7 = −21, donc x = −21/−7 = 3.
:::

::: retenir
Si det(M) ≠ 0, chaque inconnue est un quotient det(Mᵢ)/det(M) en remplaçant la colonne i par les seconds membres ; si det(M) = 0, il faut étudier le système, qui est impossible ou à solutions infinies.
:::

> 🏆 Onzième porte franchie, héros. Tu ranges un système dans une matrice, tu multiplies, tu calcules un déterminant, tu inverses par comatrice ou par les lignes, et tu résous par pivot, par X = A⁻¹B ou par Cramer. Au chapitre suivant, la statistique et les probabilités t'attendent.
