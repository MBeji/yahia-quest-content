# ⚔️ Matrices et systèmes — ranger les nombres, calculer en tableau, retrouver les inconnues

> 💡 « Un stock, une facture, un budget sont des tableaux de nombres. Apprends à calculer avec le tableau lui-même, et les prix inconnus d'un marché se retrouvent en un seul produit. »

Bienvenue, héros de l'Économie et gestion. Une coopérative suit ses stocks sur plusieurs marchés, un atelier calcule ses commandes de matières, un gérant cherche des prix qu'on ne lui donne pas directement. Huit étapes te mènent du tableau de nombres à la résolution d'un système : matrices, somme et produit par un réel, produit de deux matrices, déterminant, matrice inverse, écriture matricielle d'un système, mise en équation d'un problème économique, et le cas où l'inverse n'existe pas. On suppose acquis les équations du premier degré et la résolution d'un système de deux équations par substitution ou combinaison.

Dans tout le chapitre, une matrice s'écrit **ligne par ligne** : les coefficients d'une ligne sont séparés par une espace, les lignes par « ; ». Ainsi (1 2 ; 3 4) a pour lignes (1 2) et (3 4). Un coefficient négatif colle à son signe : (3 −1) a deux coefficients, alors que 3 − 1 est une soustraction. Dans une matrice, un nombre n'a pas d'espace de milliers : (150 ; 1020). Une colonne s'écrit (x ; y ; z) et un déterminant |a b ; c d|.

## 🗂️ Matrices : ranger les nombres dans un tableau

Une coopérative oléicole suit ses bidons en stock. Le marché de Sfax garde 40 bidons d'huile extra vierge, 18 de vierge et 12 de raffinée ; celui de Sousse en garde 25, 30 et 9.
Six nombres, trois huiles, deux marchés : comment les ranger dans un seul objet qui garde la trace de l'huile et du marché ?

::: definition
Une **matrice** d'ordre n × p est un tableau de nombres réels rangés en **n lignes** et **p colonnes**. On la note M = (aᵢⱼ) : aᵢⱼ est le **coefficient** situé à la ligne i et à la colonne j, avec 1 ≤ i ≤ n et 1 ≤ j ≤ p.

Le premier indice désigne toujours la **ligne**, le second la **colonne**.
:::

| | Sfax | Sousse |
| --- | --- | --- |
| extra vierge | 40 | 25 |
| vierge | 18 | 30 |
| raffinée | 12 | 9 |

Ce tableau s'écrit M = (40 25 ; 18 30 ; 12 9) : chaque ligne de M est une ligne du tableau (une huile), chaque colonne de M une colonne du tableau (un marché).

::: exemple Lire la matrice du stock
1. M a trois lignes et deux colonnes : elle est d'ordre 3 × 2.
2. Le coefficient a₃₁ est à la ligne 3 (raffinée) et à la colonne 1 (Sfax) : a₃₁ = 12.
3. La colonne 2, (25 ; 30 ; 9), donne le stock des trois huiles à Sousse ; la ligne 2, (18 30), donne le stock de l'huile vierge sur les deux marchés.

:::

::: piege Lire aᵢⱼ en colonne puis ligne
Pour M, on lit a₂₁ comme « colonne 2, ligne 1 » et l'on trouve 25. Cela tente parce qu'on lit « 2 puis 1 » comme une abscisse puis une ordonnée. Mais le premier indice est la **ligne** : a₂₁ est à la ligne 2 et à la colonne 1, soit 18 bidons d'huile vierge à Sfax.
:::

::: propriete
- Une matrice à une seule ligne est une **matrice ligne**, à une seule colonne une **matrice colonne** ; si n = p, elle est **carrée** d'ordre n et ses coefficients a₁₁, a₂₂, … forment sa **diagonale**.
- La **matrice unité** Iₙ est la matrice carrée d'ordre n dont la diagonale ne porte que des 1 et dont les autres coefficients sont nuls : I₂ = (1 0 ; 0 1). La **matrice nulle** O a tous ses coefficients nuls.
- Deux matrices sont **égales** si elles ont le même ordre et les mêmes coefficients aux mêmes places.

Cas limite : (1 2) et (1 ; 2) portent les mêmes nombres mais ne sont pas égales, car l'une est d'ordre 1 × 2 et l'autre d'ordre 2 × 1.
:::

::: verifie
Soit N = (3 7 1 ; 0 5 2). Donner l'ordre de N et la valeur de n₂₃. L'écriture n₃₂ a-t-elle un sens ?

---

N a deux lignes et trois colonnes : elle est d'ordre 2 × 3. Le coefficient n₂₃ est à la ligne 2 et à la colonne 3 : n₂₃ = 2. Il n'existe pas de ligne 3, donc n₃₂ n'a pas de sens.
:::

::: retenir
Matrice d'ordre n × p : n lignes, p colonnes ; aᵢⱼ est à la ligne i, colonne j (ligne d'abord). Matrices particulières : ligne, colonne, carrée, unité Iₙ, nulle O ; l'égalité exige le même ordre et les mêmes coefficients.
:::

## ➕ Somme, différence et produit par un réel

Un atelier de couture suit le stock de deux modèles (chemises, pantalons) dans deux boutiques. Au début de la semaine : I = (12 5 ; 8 20) ; il entre E = (30 10 ; 15 25) et il sort S = (28 9 ; 20 14), lignes = boutiques, colonnes = modèles.
Comment obtenir d'un seul coup le nouvel état du stock, boutique par boutique, modèle par modèle ?

::: definition
Pour deux matrices A = (aᵢⱼ) et B = (bᵢⱼ) de **même ordre**, la somme A + B est la matrice (aᵢⱼ + bᵢⱼ) et la différence A − B la matrice (aᵢⱼ − bᵢⱼ). Pour un réel k, kA est la matrice (k·aᵢⱼ) : on multiplie **chaque** coefficient par k.
:::

::: exemple Le nouvel état du stock
1. Même ordre 2 × 2 : le calcul est possible. On additionne les coefficients de même place, car chaque case désigne la même boutique et le même modèle : I + E = (42 15 ; 23 45).
2. On retranche les sorties case par case : (I + E) − S = (14 6 ; 3 31).
3. Pour une hausse de 10 % de tous les stocks, on multiplie chaque coefficient par 1,1 : 1,1 × (14 6 ; 3 31) = (15,4 6,6 ; 3,3 34,1).

:::

::: piege Confondre TVA et prix TTC
Avec les prix HT P = (20 35 ; 12 18) et une TVA de 19 %, on écrit 0,19 × P = (3,8 6,65 ; 2,28 3,42) et l'on prend cette matrice pour les prix TTC. Cela tente parce que « 19 % » s'écrit 0,19. Mais 0,19P ne contient que la **TVA** ; le prix TTC est le prix HT plus la TVA, soit 1,19 × P = (23,8 41,65 ; 14,28 21,42).
:::

::: propriete
Pour des matrices A, B, C de même ordre et un réel k :
- A + B = B + A, (A + B) + C = A + (B + C), A + O = A ;
- k(A + B) = kA + kB, et (−1)A = −A est la matrice opposée.

Cas limite : la somme n'existe que pour deux matrices de même ordre, même si elles ont autant de coefficients (une matrice 2 × 3 et une matrice 3 × 2 ne s'additionnent pas).
:::

::: verifie
Soit A = (2 −1 ; 0 3) et B = (1 4 ; −2 5). Calculer 3A − B.

---

On calcule case par case : 3A = (6 −3 ; 0 9), puis on retranche chaque coefficient de B, ce qui donne 3A − B = (5 −7 ; 2 4). Les deux matrices ont le même ordre 2 × 2, donc la différence est définie.
:::

::: retenir
A + B et A − B : même ordre, case par case ; kA : tous les coefficients multipliés par k. Un prix TTC avec une TVA de t % s'obtient par (1 + t/100) × P, jamais par (t/100) × P.
:::

## ✖️ Produit de deux matrices

Un gérant de kiosque note, sur trois jours, les quantités vendues de jus, de sandwichs et de gâteaux : Q = (60 40 25 ; 55 45 30 ; 70 35 20). Les prix unitaires, en dinars, forment la colonne P = (1,5 ; 3,5 ; 2).
Comment obtenir la recette de chaque jour sans recalculer à la main ligne après ligne ?

::: definition
Soit A d'ordre n × p et B d'ordre p × q. Le produit A × B est la matrice d'ordre n × q dont le coefficient de la ligne i et de la colonne j est
**aᵢ₁b₁ⱼ + aᵢ₂b₂ⱼ + … + aᵢₚbₚⱼ** :
on multiplie la **ligne i de A** par la **colonne j de B**, terme à terme, puis on additionne.

Le produit n'existe que si le nombre de colonnes de A égale le nombre de lignes de B.
:::

::: exemple Les recettes des trois jours
Q est d'ordre 3 × 3 et P d'ordre 3 × 1 : le produit existe et il est d'ordre 3 × 1.
1. Jour 1 : la ligne (60 40 25) fois la colonne P donne 60 × 1,5 + 40 × 3,5 + 25 × 2 = 90 + 140 + 50 = 280.
2. Jour 2 : 55 × 1,5 + 45 × 3,5 + 30 × 2 = 82,5 + 157,5 + 60 = 300.
3. Jour 3 : 70 × 1,5 + 35 × 3,5 + 20 × 2 = 105 + 122,5 + 40 = 267,5.

Donc Q × P = (280 ; 300 ; 267,5) : chaque coefficient est la recette d'un jour.
:::

::: piege Multiplier case par case
Pour A = (1 2 ; 0 1) et B = (3 0 ; 1 1), on écrit A × B = (1×3 2×0 ; 0×1 1×1) = (3 0 ; 0 1). Cela tente parce que la somme se fait case par case. Mais le produit combine une **ligne** de A avec une **colonne** de B : le coefficient en haut à gauche est 1×3 + 2×1 = 5, et A × B = (5 2 ; 1 1).
:::

::: propriete
- **Pas commutatif** : ici B × A = (3 6 ; 1 3), différent de A × B = (5 2 ; 1 1).
- **Associatif et distributif** : A × (B × C) = (A × B) × C et A × (B + C) = A × B + A × C, quand les produits existent.
- **Neutre** : Iₙ × M = M × Iₙ = M pour toute matrice carrée M d'ordre n. Pour une matrice carrée A, A² = A × A et A³ = A² × A.

Cas limite : A × B peut exister sans que B × A existe : une matrice 2 × 3 par une matrice 3 × 1 se multiplient, mais une matrice 3 × 1 par une matrice 2 × 3 non.
:::

::: verifie
Calculer (2 −1 ; 0 3) × (4 ; 5).

---

La matrice est d'ordre 2 × 2 et la colonne d'ordre 2 × 1 : le produit existe et il est d'ordre 2 × 1. Ligne 1 : 2 × 4 + (−1) × 5 = 3. Ligne 2 : 0 × 4 + 3 × 5 = 15. Le résultat est (3 ; 15).
:::

::: retenir
A × B : ligne de A fois colonne de B, possible si colonnes(A) = lignes(B), d'ordre n × q. Non commutatif, mais associatif, distributif, avec Iₙ pour neutre ; jamais de produit case par case.
:::

## 🔢 Déterminant d'une matrice d'ordre 2 ou 3

Un marchand propose deux paniers : le premier, 2 kg d'oranges et 3 kg de pommes, coûte 11 dinars ; le second, 4 kg d'oranges et 6 kg de pommes, coûte 22 dinars. On voudrait retrouver le prix du kilo de chaque fruit.
Quel nombre, calculé à partir des quatre coefficients (2 3 ; 4 6), dit si les prix sont retrouvables ?

::: definition
Le **déterminant** d'une matrice carrée d'ordre 2, M = (a b ; c d), est le réel **dét(M) = ad − bc**.

Pour une matrice d'ordre 3 de lignes (a₁ a₂ a₃), (b₁ b₂ b₃), (c₁ c₂ c₃), on développe par rapport à la **première colonne** :
dét = a₁ × |b₂ b₃ ; c₂ c₃| − b₁ × |a₂ a₃ ; c₂ c₃| + c₁ × |a₂ a₃ ; b₂ b₃|.
Les signes alternent + − + ; le développement par la première ligne donne le même nombre.
:::

::: exemple Deux déterminants
1. Pour les paniers, dét(2 3 ; 4 6) = 2 × 6 − 3 × 4 = 0.
2. Pour N = (2 1 0 ; 1 3 4 ; 0 2 1), on développe par la première colonne : dét(N) = 2 × |3 4 ; 2 1| − 1 × |1 0 ; 2 1| + 0 × |1 0 ; 3 4|.
3. Chaque déterminant d'ordre 2 se calcule par ad − bc : |3 4 ; 2 1| = 3 − 8 = −5 et |1 0 ; 2 1| = 1 − 0 = 1.
4. Donc dét(N) = 2 × (−5) − 1 × 1 + 0 = −11.

:::

::: piege Oublier le signe moins du deuxième terme
Dans le développement de N, on additionne les trois termes : 2 × (−5) + 1 × 1 + 0 = −9. Cela tente parce que le premier et le dernier terme gardent leur signe. Mais le coefficient du milieu porte un signe **moins** dans le développement : le bon résultat est 2 × (−5) − 1 × 1 = −11.
:::

::: propriete
- dét(I₂) = 1 et dét(I₃) = 1.
- Le déterminant peut être nul sans que la matrice soit la matrice nulle : c'est le cas de (2 3 ; 4 6), dont la seconde ligne vaut deux fois la première.
- Le déterminant d'une matrice d'ordre 3 se calcule en trois déterminants d'ordre 2.

Cas limite : une matrice qui a une ligne de zéros, comme (0 0 ; 3 5), a un déterminant nul : 0 × 5 − 0 × 3 = 0.
:::

::: verifie
Calculer dét(6 −2 ; 4 5).

---

On applique ad − bc avec a = 6, b = −2, c = 4, d = 5 : 6 × 5 − (−2) × 4 = 30 + 8 = 38. Le signe de bc compte : soustraire un produit négatif revient à ajouter.
:::

::: retenir
Ordre 2 : dét(a b ; c d) = ad − bc. Ordre 3 : développement par la première colonne (ou ligne) avec les signes + − +. dét(Iₙ) = 1 ; un déterminant nul n'implique pas une matrice nulle.
:::

## 🔄 Matrice inverse

Un grossiste facture deux clients à partir des quantités (x ; y) de caisses A et B : la facture du premier est 2x + y, celle du second 4x + 3y. Cette règle est le produit de A = (2 1 ; 4 3) par la colonne (x ; y).
Comment, connaissant les deux factures, remonter aux quantités ? Il faut une matrice qui « défait » A.

::: definition
Une matrice carrée M d'ordre n est **inversible** s'il existe une matrice M' d'ordre n telle que **M × M' = M' × M = Iₙ**. M' est alors l'**inverse** de M, notée M⁻¹ ; elle est unique.

**Théorème (admis)** : pour une matrice d'ordre 2 ou 3, M est inversible si et seulement si dét(M) ≠ 0.

**Inverse d'ordre 2** : si dét(M) ≠ 0, alors M⁻¹ = (1/dét(M)) × (d −b ; −c a) pour M = (a b ; c d).
:::

::: exemple L'inverse de A = (2 1 ; 4 3)
1. dét(A) = 2 × 3 − 1 × 4 = 2, différent de 0 : A est inversible.
2. On échange les termes de la diagonale (3 et 2) et l'on change le signe des deux autres (1 devient −1, 4 devient −4) : (3 −1 ; −4 2).
3. On multiplie par 1/dét(A) = 1/2 : A⁻¹ = (3/2 −1/2 ; −2 1).
4. Vérification : la ligne 1 de A fois la colonne 1 de A⁻¹ donne 2 × 3/2 + 1 × (−2) = 1, et ainsi de suite : A × A⁻¹ = I₂.

:::

::: piege Garder les signes de b et c
Pour A, on écrit (3 1 ; 4 2) / 2, en échangeant seulement a et d. Cela tente parce que « échanger » semble suffire. Mais le test échoue : la ligne 1 de A fois la colonne 1 de ce « candidat » donne 2 × 3/2 + 1 × 2 = 5, pas 1. Il faut **changer le signe** de b et de c : l'inverse est (3 −1 ; −4 2) / 2.
:::

::: propriete
- M est inversible si et seulement si dét(M) ≠ 0.
- Il suffit de trouver M' avec M × M' = Iₙ **ou** M' × M = Iₙ pour conclure que M est inversible et que M' = M⁻¹ (admis).
- **Ordre 3**, quatre étapes : calculer dét(M) ; former Δᵢⱼ = (−1)ⁱ⁺ʲ × dét(Mᵢⱼ), appelé **cofacteur**, où Mᵢⱼ est M privée de sa ligne i et de sa colonne j ; échanger lignes et colonnes de la matrice (Δᵢⱼ) ; multiplier par 1/dét(M).
- Si une relation M² − aM + bIₙ = O est connue avec b ≠ 0, alors M × (aIₙ − M) = bIₙ, donc M⁻¹ = (aIₙ − M)/b.

Cas limite : si dét(M) = 0, aucune matrice ne convient, car la division par dét(M) est impossible.
:::

::: exemple L'inverse d'ordre 3 de B = (1 2 0 ; 0 1 3 ; 2 0 1)
1. dét(B) = 1 × |1 3 ; 0 1| − 0 + 2 × |2 0 ; 1 3| = 1 + 12 = 13, non nul : B est inversible.
2. Les neuf Δᵢⱼ forment la matrice (1 6 −2 ; −2 1 4 ; 6 −3 1) ; par exemple Δ₁₂ = −|0 3 ; 2 1| = −(0 − 6) = 6.
3. On échange lignes et colonnes : (1 −2 6 ; 6 1 −3 ; −2 4 1).
4. On multiplie par 1/13 : B⁻¹ = (1/13) × (1 −2 6 ; 6 1 −3 ; −2 4 1).

:::

::: exemple Déduire l'inverse d'une relation
Soit C = (1 2 ; 0 3). Un calcul donne C² = (1 8 ; 0 9), donc C² − 4C + 3I₂ = (1−4+3 8−8 ; 0 9−12+3) = O.
1. On isole : C² − 4C = −3I₂, soit C × (4I₂ − C) = 3I₂ en changeant les signes.
2. On divise par 3 : C × ((4I₂ − C)/3) = I₂. Comme M × M' = Iₙ suffit, C est inversible et C⁻¹ = (4I₂ − C)/3.
3. Or 4I₂ − C = (3 −2 ; 0 1), donc C⁻¹ = (1 −2/3 ; 0 1/3).
4. Contrôle : la ligne 1 de C fois la colonne 2 de C⁻¹ donne 1 × (−2/3) + 2 × 1/3 = 0, et la ligne 1 fois la colonne 1 donne 1.

:::

::: verifie
Donner l'inverse de M = (5 2 ; 7 3).

---

dét(M) = 5 × 3 − 2 × 7 = 1, non nul. On échange 5 et 3, on change le signe de 2 et de 7 : M⁻¹ = (3 −2 ; −7 5), car la division par dét(M) = 1 ne change rien. On vérifie : 5 × 3 + 2 × (−7) = 1.

Ordre 3 : calculer Δ₃₁ pour B = (1 2 0 ; 0 1 3 ; 2 0 1).

---

Δ₃₁ = (−1)⁴ × |2 0 ; 1 3| = 6 − 0 = 6, conforme à la matrice des Δᵢⱼ de l'exemple.
:::

::: retenir
Inversible ⟺ dét ≠ 0. Ordre 2 : M⁻¹ = (1/dét) × (d −b ; −c a). Ordre 3 : dét, matrice des Δᵢⱼ, échange lignes/colonnes, puis 1/dét. M × M' = Iₙ suffit pour affirmer M' = M⁻¹.
:::

## 📐 Écriture matricielle d'un système et résolution

Une maroquinerie fabrique des sacs (x) et des ceintures (y). Un sac demande 3 h de couture et 2 m de cuir ; une ceinture, 1 h de couture et 1 m de cuir. L'atelier dispose de 70 h et de 50 m.
Comment écrire ces deux contraintes d'un seul trait, et en tirer x et y par un calcul sur matrices ?

::: definition
Un système de n équations à n inconnues s'écrit **A × X = B**, où A est la matrice des coefficients (**matrice du système**), X la colonne des inconnues et B la colonne des constantes. Quand A est carrée, le système est dit **carré**. Par exemple, 3x + y = 70 ; 2x + y = 50 s'écrit A × X = B avec A = (3 1 ; 2 1), X = (x ; y) et B = (70 ; 50).

**Théorème** : si dét(A) ≠ 0, le système A × X = B a **une solution et une seule**, X = A⁻¹ × B.
:::

::: exemple Les quantités de la maroquinerie
1. dét(A) = 3 × 1 − 1 × 2 = 1, non nul : le système a une solution unique.
2. A⁻¹ = (1/1) × (1 −1 ; −2 3) = (1 −1 ; −2 3).
3. X = A⁻¹ × B : ligne 1 : 1 × 70 + (−1) × 50 = 20 ; ligne 2 : (−2) × 70 + 3 × 50 = 10. Donc X = (20 ; 10).
4. Contrôle dans l'énoncé : 3 × 20 + 10 = 70 h et 2 × 20 + 10 = 50 m. Ce sont 20 sacs et 10 ceintures.

:::

::: piege Multiplier du mauvais côté
On écrit X = B × A⁻¹, en posant la colonne B avant la matrice. Cela tente parce que, pour des nombres, a × b = b × a. Mais le produit n'est pas commutatif : B est d'ordre 2 × 1 et A⁻¹ d'ordre 2 × 2, donc B × A⁻¹ **n'existe même pas**. Partant de A × X = B, on multiplie à **gauche** par A⁻¹ : X = A⁻¹ × B.
:::

::: propriete
- Les étapes : écrire A × X = B, vérifier dét(A) ≠ 0, calculer A⁻¹, puis X = A⁻¹ × B.
- La même matrice A donne la solution pour **tous** les seconds membres : seul B change.

Cas limite : si dét(A) = 0, le théorème ne s'applique pas (dernière section).
:::

::: verifie
Résoudre 2x + 5y = 16 ; x + 3y = 9 avec une matrice inverse.

---

A = (2 5 ; 1 3), dét(A) = 6 − 5 = 1, donc A⁻¹ = (3 −5 ; −1 2). Alors X = A⁻¹ × (16 ; 9) : ligne 1 : 3 × 16 − 5 × 9 = 3 ; ligne 2 : −16 + 2 × 9 = 2. La solution est (x ; y) = (3 ; 2), et 2 × 3 + 5 × 2 = 16, 3 + 2 × 3 = 9.
:::

::: retenir
Système carré : A × X = B ; si dét(A) ≠ 0, solution unique X = A⁻¹ × B (A⁻¹ à gauche de B). Vérifier la solution dans les équations de départ.
:::

## 🏭 Mettre un problème économique en système

Une pâtisserie fabrique chaque jour trois gâteaux G₁, G₂, G₃ en quantités x, y, z. Un G₁ demande 2 kg de farine, 1 kg de sucre et 1 kg de beurre ; un G₂, 1 kg de farine, 2 kg de sucre et 1 kg de beurre ; un G₃, 1 kg de farine, pas de sucre et 2 kg de beurre. Hier, elle a consommé 33 kg de farine, 26 kg de sucre et 28 kg de beurre.
Comment retrouver la production d'hier à partir des consommations ?

::: methode Passer de l'énoncé à la solution
1. **Nommer les inconnues** avec leur unité (x, y, z : nombres de gâteaux).
2. **Écrire une équation par ressource** : total consommé = somme, sur les produits, de (consommation unitaire × quantité fabriquée).
3. **Écrire A × X = B** avec la matrice des coefficients et la colonne des totaux.
4. **Vérifier dét(A) ≠ 0**, puis calculer X = A⁻¹ × B.
5. **Contrôler le sens** : quantités positives, entières si ce sont des objets.
:::

::: exemple La production de la pâtisserie
1. Farine : 2x + y + z = 33. Sucre : x + 2y = 26. Beurre : x + y + 2z = 28.
2. Donc A = (2 1 1 ; 1 2 0 ; 1 1 2), B = (33 ; 26 ; 28) et X = (x ; y ; z).
3. dét(A) = 2 × |2 0 ; 1 2| − 1 × |1 1 ; 1 2| + 1 × |1 1 ; 2 0| = 2 × 4 − 1 − 2 = 5, non nul.
4. Les neuf Δᵢⱼ donnent A⁻¹ = (1/5) × (4 −1 −2 ; −2 3 1 ; −1 −1 3), puis X = A⁻¹ × B = (10 ; 8 ; 5).
5. Contrôle : 2 × 10 + 8 + 5 = 33, 10 + 2 × 8 = 26 et 10 + 8 + 2 × 5 = 28. Hier : 10, 8 et 5 gâteaux, des entiers positifs.

:::

::: piege Écrire les coefficients dans le désordre
On range les équations en prenant, pour le sucre, les coefficients dans l'ordre (2 1 0) au lieu de (1 2 0). Cela tente parce que l'énoncé donne d'abord le chiffre « 2 » à propos de la farine. Mais chaque ligne de A doit suivre l'ordre des **inconnues** x, y, z, et non l'ordre des phrases : la ligne du sucre est (1 2 0), car G₁ consomme 1 kg, G₂ 2 kg et G₃ aucun.
:::

::: propriete
- Un problème de **ressources** donne A × X = B ; un problème de **prix** (quantités connues, prix inconnus) a la même forme, avec la colonne des prix pour X.
- Autant d'équations que d'inconnues, et dét(A) ≠ 0, garantissent une solution unique.
- Un modèle à paramètres se traite de la même façon : pour un coût C(q) = aq² + bq + c, chaque valeur relevée, comme C(1) = 15, donne une équation en a, b, c.

Cas limite : une solution mathématique doit rester **admissible** : si l'on trouve −3 gâteaux ou 2,5 voitures, la mise en équation est à revoir.
:::

::: verifie
Un traiteur vend des plateaux à x dinars l'unité en petite taille et y en grande taille. Une commande de 3 petits et 2 grands coûte 47 dinars ; une commande de 1 petit et 4 grands coûte 49 dinars. Écrire A × X = B.

---

Les inconnues sont x et y, les coefficients suivent l'ordre (petit, grand) : 3x + 2y = 47 et x + 4y = 49. Donc A = (3 2 ; 1 4), X = (x ; y) et B = (47 ; 49), avec dét(A) = 12 − 2 = 10, non nul : les prix sont retrouvables.
:::

::: retenir
Mettre en système : nommer les inconnues, une équation par contrainte (coefficients dans l'ordre des inconnues), A × X = B, dét(A) ≠ 0, X = A⁻¹ × B, contrôle de la solution dans l'énoncé.
:::

## ⚠️ Quand la matrice n'est pas inversible

Revenons aux paniers du marchand : 2x + 3y = 11 pour le premier, 4x + 6y = 22 pour le second, avec dét(2 3 ; 4 6) = 0. Si le second panier coûtait 25 dinars au lieu de 22, les deux contraintes se contrediraient.
Que peut-on dire des prix quand dét(A) = 0 : aucune solution, une seule, ou davantage ?

::: propriete
On admet que si dét(A) = 0, la matrice A n'a pas d'inverse et le système A × X = B n'a **soit aucune solution, soit une infinité**, jamais une seule. On le décide par **élimination** : on retranche à une équation un multiple de l'autre pour faire disparaître une inconnue.
:::

::: exemple Les deux paniers
1. Premier cas : 2x + 3y = 11 et 4x + 6y = 22. On calcule L₂ − 2L₁ : 4x + 6y − (4x + 6y) = 22 − 22, soit 0 = 0. La seconde équation n'apporte rien : toutes les solutions de 2x + 3y = 11 conviennent, par exemple (4 ; 1) et (1 ; 3). Il y a une infinité de solutions.
2. Second cas : 2x + 3y = 11 et 4x + 6y = 25. Le même calcul L₂ − 2L₁ donne 0 = 25 − 22, soit 0 = 3, ce qui est impossible. Il n'y a aucune solution.

:::

::: piege Conclure « aucune solution » dès que dét(A) = 0
Pour 2x + 3y = 11 ; 4x + 6y = 22, on lit dét(A) = 0 et l'on répond « pas de solution ». Cela tente parce qu'on ne peut pas calculer A⁻¹. Mais un déterminant nul laisse **deux** possibilités : ici L₂ − 2L₁ donne 0 = 0, donc une infinité de solutions. Seule l'élimination, comparée aux seconds membres, tranche.
:::

::: propriete
- dét(A) = 0 : ni A⁻¹ ni la formule X = A⁻¹ × B.
- Pour deux équations dont les premiers membres sont proportionnels, les seconds membres dans la même proportion donnent une infinité de solutions ; dans une autre proportion, aucune solution.

Cas limite : une matrice non inversible peut avoir une infinité de solutions pour un second membre B et aucune pour un autre : le déterminant ne dépend que de A, pas de B.
:::

::: verifie
Combien de solutions pour 3x − 6y = 9 ; x − 2y = 4 ?

---

dét(3 −6 ; 1 −2) = 3 × (−2) − (−6) × 1 = −6 + 6 = 0 : pas de solution unique. On calcule L₁ − 3L₂ : 3x − 6y − 3x + 6y = 9 − 12, soit 0 = −3, impossible. Le système n'a aucune solution.
:::

::: retenir
dét(A) = 0 : jamais une solution unique. On élimine : 0 = 0 donne une infinité de solutions, 0 = k avec k ≠ 0 aucune.
:::
