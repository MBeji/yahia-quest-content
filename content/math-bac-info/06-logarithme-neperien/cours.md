# ⚔️ Logarithme népérien — la fonction qui change les produits en sommes

> 💡 «Multiplier est long, additionner est court : le logarithme transforme l'un en l'autre, et c'est ce qui a fait gagner des années de calcul aux astronomes.»

Bienvenue, héros de la section Sciences de l'informatique. En 1614, John Napier publie des tables qui remplacent chaque multiplication par une addition ; Henry Briggs en tire les logarithmes de base 10, et Jost Bürgi y avait pensé dès 1588. Aujourd'hui, c'est ln que ta calculatrice et tes programmes appellent. Huit étapes te mènent de sa définition à l'étude d'une fonction du bac : définition, produit et somme, courbe et nombre e, équations, encadrement de ln(1 + x), limites, ln(u) et logarithme décimal. On suppose acquis les limites (chapitre 2), la continuité (chapitre 3), les dérivées, les primitives et l'inégalité des accroissements finis (chapitre 4).

## 🏰 Définition : la primitive de 1/x qui s'annule en 1

Au chapitre 4, tu as primitivé xⁿ en xⁿ⁺¹/(n + 1), formule qui échoue pour n = −1 : elle diviserait par 0.
Pourtant x ↦ 1/x est continue et strictement positive sur ]0 ; +∞[ : elle y admet des primitives, qui diffèrent d'une constante, et aucune fonction connue n'en fait partie.
Une seule de ces primitives vaut 0 en x = 1. Que peut-on dire d'une fonction que l'on ne connaît que par sa dérivée ?

::: definition
La **fonction logarithme népérien**, notée **ln** (ou Log), est la primitive de x ↦ 1/x sur ]0 ; +∞[ qui s'annule en 1.

$$ (ln)′(x) = 1/x pour tout x > 0 $$

$$ ln 1 = 0 $$
:::

| Ce que l'on lit | D'où cela vient |
| --- | --- |
| ln est définie sur ]0 ; +∞[, dérivable, donc continue | c'est, par définition, une primitive de x ↦ 1/x sur l'intervalle ]0 ; +∞[ |
| (ln)′(x) = 1/x > 0 | l'inverse d'un nombre strictement positif est strictement positif |
| ln est strictement croissante | une dérivée strictement positive donne une fonction strictement croissante |
| ln x < 0 sur ]0 ; 1[ et ln x > 0 sur ]1 ; +∞[ | ln est croissante et ln 1 = 0 |

La première ligne fixe le domaine : on ne prend jamais le logarithme de 0 ni d'un nombre négatif. La dernière dit que le signe de ln x se lit en comparant x à 1, et non à 0.

::: exemple Lire ln sans calculatrice
1. (ln)′(4) = 1/4 : la dérivée de ln en a vaut 1/a, puisque ln est la primitive de x ↦ 1/x.
2. 0,3 < 1 et ln est strictement croissante : ln 0,3 < ln 1 = 0, donc ln 0,3 est négatif bien que 0,3 soit positif.
3. 5 > 1 donne ln 5 > ln 1 = 0 : on compare toujours à 1.
4. Pour comparer ln(2/3) et ln(3/4), on compare les arguments : 2/3 ≈ 0,667 < 0,75 = 3/4, donc, ln conservant l'ordre, ln(2/3) < ln(3/4).

:::

::: piege Croire qu'un logarithme est positif parce que le nombre l'est
On écrit « 0,3 > 0, donc ln 0,3 > 0 ». Cela tente parce que ln n'existe que pour des nombres strictement positifs. Mais le signe de ln x dépend de la position de x par rapport à 1, pas par rapport à 0 : ln 0,3 < ln 1 = 0 puisque 0,3 < 1. Quant à ln 0 et ln(−2), ils n'existent pas.
:::

::: propriete
Pour tous réels a > 0 et b > 0 :

- ln a = ln b ⟺ a = b ;
- ln a < ln b ⟺ a < b ;
- ln a = 0 ⟺ a = 1 ; ln a > 0 ⟺ a > 1 ; ln a < 0 ⟺ 0 < a < 1.

Ces équivalences viennent de la stricte croissance de ln : deux nombres distincts ont deux logarithmes distincts, rangés dans le même ordre.

Cas limite : tout est soumis à a > 0 et b > 0. Pour a = 0 ou a < 0, ln a n'existe pas et l'on ne conclut rien.
:::

::: verifie
Comparer, sans calculatrice, ln(7/5) et ln(10/7), puis donner le signe de ln 0,98.

---

7/5 = 1,4 et 10/7 ≈ 1,43 : 1,4 < 1,43, donc, ln étant croissante, ln(7/5) < ln(10/7). Puis 0,98 < 1, donc ln 0,98 < ln 1 = 0 : il est négatif. On compare les arguments entre eux, puis chacun à 1.
:::

::: retenir
ln est la primitive de 1/x sur ]0 ; +∞[ qui s'annule en 1 : strictement croissante, négative sur ]0 ; 1[, positive sur ]1 ; +∞[, elle conserve l'ordre.
:::

## 🧮 La propriété fondamentale : le produit devient une somme

Sur une calculatrice, ln 2 ≈ 0,6931 et ln 5 ≈ 1,6094. Leur somme vaut 2,3025, et ln 10 ≈ 2,3026, au dernier chiffre près.
Or 2 × 5 = 10. Est-ce un hasard, ou ln change-t-elle toujours un produit en somme ?

::: exemple Preuve : fixer k, puis comparer deux fonctions
1. Fixons k > 0 et posons f(x) = ln(kx) pour x > 0 : c'est une composée, de x ↦ kx puis de ln.
2. Sa dérivée est f′(x) = k × 1/(kx) = 1/x, c'est la règle de dérivation d'une composée (chapitre 4) : f a la même dérivée que ln.
3. Deux fonctions de même dérivée sur un intervalle diffèrent d'une constante : f(x) = ln x + α pour tout x > 0.
4. En x = 1 : f(1) = ln k et ln 1 = 0, donc α = ln k. Ainsi ln(kx) = ln x + ln k, pour tout k > 0 et tout x > 0.

:::

::: propriete
**Propriété fondamentale.** Pour tous réels x > 0 et y > 0 :

$$ ln(xy) = ln x + ln y $$
:::

Elle entraîne quatre conséquences, que l'on retient comme des règles de calcul :

| Écriture | devient | Pourquoi | Exemple |
| --- | --- | --- | --- |
| ln(1/x) | −ln x | ln x + ln(1/x) = ln 1 = 0 | ln(1/2) = −ln 2 |
| ln(x/y) | ln x − ln y | x/y = x × (1/y) | ln(5/2) = ln 5 − ln 2 |
| ln(xⁿ), n entier relatif | n ln x | produit répété n fois, puis inverse si n < 0 | ln(2⁵) = 5 ln 2 |
| ln √x | ½ ln x | 2 ln √x = ln((√x)²) = ln x | ln √10 = ½ ln 10 |

::: exemple Exprimer avec ln 2, ln 3 et ln 5 (on donne ln 3 ≈ 1,0986)
1. 50 = 2 × 5² : ln 50 = ln 2 + 2 ln 5 ≈ 0,6931 + 3,2189 = 3,9120, car le produit devient une somme et la puissance un facteur.
2. 0,15 = 3/(2² × 5) : ln 0,15 = ln 3 − 2 ln 2 − ln 5 ≈ 1,0986 − 1,3863 − 1,6094 = −1,8971. Contrôle : 0,15 < 1, donc ln 0,15 < 0 ✓.
3. √20 est la racine de 20 = 2² × 5 : ln √20 = ½ ln 20 = ½(2 ln 2 + ln 5) = ln 2 + ½ ln 5 ≈ 1,4979, car la racine donne le facteur ½.
4. Sans calculatrice : ln(√5 + 2) + ln(√5 − 2) = ln((√5 + 2)(√5 − 2)) = ln(5 − 4) = ln 1 = 0, car on regroupe la somme en un produit.

:::

::: piege Croire que ln(a + b) = ln a + ln b
Avec a = 3 et b = 7, on écrit « ln(3 + 7) = ln 3 + ln 7 ». Cela tente parce que le produit devient une somme. Mais ln(3 + 7) = ln 10 ≈ 2,3026, alors que ln 3 + ln 7 = ln 21 ≈ 3,0445. Seul un produit se transforme en somme : une somme dans ln ne se dissocie pas.
:::

::: methode
Pour simplifier ou calculer un logarithme : (1) décomposer l'argument en facteurs, quotients et puissances, comme 50 = 2 × 5² ; (2) appliquer les quatre règles du tableau ; (3) regrouper les termes semblables.

Cas limite : ln(xⁿ) = n ln x suppose x > 0. Pour x < 0 et n pair, xⁿ > 0 existe mais ln x n'existe pas : ln((−3)²) = ln 9 = 2 ln 3, et l'on ne peut pas écrire 2 ln(−3).
:::

::: verifie
Simplifier A = ln 45 − 2 ln 3 + ln 4, puis l'écrire avec ln 2 et ln 5.

---

ln 45 − 2 ln 3 = ln 45 − ln 9 = ln 5, car 2 ln 3 = ln 3² = ln 9 et un quotient devient une différence. Puis ln 5 + ln 4 = ln 20 = 2 ln 2 + ln 5. On a d'abord regroupé tout en un seul logarithme, puis décomposé en facteurs premiers.
:::

::: retenir
ln(xy) = ln x + ln y, ln(1/x) = −ln x, ln(x/y) = ln x − ln y, ln(xⁿ) = n ln x (n entier), ln √x = ½ ln x ; en revanche ln(x + y) ≠ ln x + ln y.
:::

## 📈 Courbe, limites et nombre e

Calculons ln de nombres de plus en plus grands, avec ln(10ⁿ) = n ln 10 ≈ 2,3026 n :

| x | 100 | 10⁴ | 10¹³ | 10⁵⁰ | 10¹⁰⁰ | 10¹⁰⁰⁰ |
| --- | --- | --- | --- | --- | --- | --- |
| ln x | 4,61 | 9,21 | 29,93 | 115,13 | 230,26 | 2 302,59 |

Même pour 10¹⁰⁰⁰, ln reste modeste. Elle monte pourtant toujours : on admet que ln x finit par dépasser tout nombre, c'est-à-dire lim x→+∞ ln x = +∞.
Que fait ln près de 0, à quoi ressemble sa courbe, et que vaut le réel dont le logarithme est 1 ?

::: figure La courbe de ln monte de plus en plus lentement, plonge le long de l'axe des ordonnées près de 0 et passe par (1 ; 0) ; le point d'ordonnée 1 a pour abscisse e ≈ 2,718
<svg viewBox="0 0 340 250"><title>Courbe de ln : elle plonge le long de l'axe des ordonnées, coupe l'axe des abscisses en 1 et passe par le point (e ; 1)</title><line x1="40" y1="110" x2="332.4" y2="110" stroke="#0f172a" stroke-width="1.6"/><line x1="40" y1="225.2" x2="40" y2="12.8" stroke="#0f172a" stroke-width="1.6"/><polygon points="332.4,110 325.4,106.5 325.4,113.5" fill="#0f172a"/><polygon points="40,12.8 36.5,19.8 43.5,19.8" fill="#0f172a"/><text x="328.4" y="103" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x</text><text x="48" y="20.8" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">y</text><line x1="74" y1="107" x2="74" y2="113" stroke="#0f172a" stroke-width="1.3"/><text x="74" y="125" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><line x1="108" y1="107" x2="108" y2="113" stroke="#0f172a" stroke-width="1.3"/><text x="108" y="125" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><line x1="142" y1="107" x2="142" y2="113" stroke="#0f172a" stroke-width="1.3"/><text x="142" y="125" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">3</text><line x1="176" y1="107" x2="176" y2="113" stroke="#0f172a" stroke-width="1.3"/><text x="176" y="125" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4</text><line x1="210" y1="107" x2="210" y2="113" stroke="#0f172a" stroke-width="1.3"/><text x="210" y="125" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">5</text><line x1="244" y1="107" x2="244" y2="113" stroke="#0f172a" stroke-width="1.3"/><text x="244" y="125" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">6</text><line x1="278" y1="107" x2="278" y2="113" stroke="#0f172a" stroke-width="1.3"/><text x="278" y="125" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">7</text><line x1="312" y1="107" x2="312" y2="113" stroke="#0f172a" stroke-width="1.3"/><text x="312" y="125" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">8</text><line x1="37" y1="182" x2="43" y2="182" stroke="#0f172a" stroke-width="1.3"/><text x="34" y="186" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−2</text><line x1="37" y1="146" x2="43" y2="146" stroke="#0f172a" stroke-width="1.3"/><text x="34" y="150" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−1</text><line x1="37" y1="74" x2="43" y2="74" stroke="#0f172a" stroke-width="1.3"/><text x="34" y="78" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><line x1="37" y1="38" x2="43" y2="38" stroke="#0f172a" stroke-width="1.3"/><text x="34" y="42" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><polyline points="42.2,208.4 45.7,174.2 49.2,157 52.7,145.4 56.2,136.7 59.7,129.6 63.2,123.7 66.7,118.7 70.2,114.3 73.7,110.3 77.2,106.8 80.7,103.5 84.2,100.5 87.7,97.8 91.2,95.3 94.7,92.9 98.2,90.6 101.7,88.5 105.2,86.6 108.7,84.7 112.2,82.9 115.7,81.2 119.2,79.6 122.7,78 126.2,76.5 129.7,75.1 133.2,73.7 136.7,72.4 140.2,71.1 143.7,69.9 147.2,68.7 150.7,67.5 154.2,66.4 157.7,65.3 161.2,64.2 164.7,63.2 168.2,62.2 171.7,61.2 175.2,60.3 178.7,59.4 182.2,58.5 185.7,57.6 189.2,56.8 192.7,55.9 196.2,55.1 199.7,54.3 203.2,53.5 206.7,52.8 210.2,52 213.7,51.3 217.2,50.6 220.7,49.9 224.2,49.2 227.7,48.5 231.2,47.8 234.7,47.2 238.2,46.5 241.7,45.9 245.2,45.3 248.7,44.7 252.2,44.1 255.7,43.5 259.2,42.9 262.7,42.3 266.2,41.8 269.7,41.2 273.2,40.7 276.7,40.1 280.2,39.6 283.7,39.1 287.2,38.6 290.7,38.1 294.2,37.6 297.7,37.1 301.2,36.6 304.7,36.1 308.2,35.6 311.7,35.2 315.2,34.7 318.7,34.3 322.2,33.8" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><line x1="132.4" y1="74" x2="132.4" y2="110" stroke="#94a3b8" stroke-width="1.3" stroke-dasharray="5 3"/><line x1="40" y1="74" x2="132.4" y2="74" stroke="#94a3b8" stroke-width="1.3" stroke-dasharray="5 3"/><circle cx="74" cy="110" r="4" fill="#0f6e56" stroke="#0f172a" stroke-width="1"/><circle cx="132.4" cy="74" r="4" fill="#0f6e56" stroke="#0f172a" stroke-width="1"/><text x="126.4" y="66" text-anchor="end" font-size="11" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">(e ; 1)</text><text x="80" y="146" text-anchor="start" font-size="11" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">(1 ; 0)</text><text x="216.8" y="39.6" text-anchor="middle" font-size="13" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">y = ln x</text><text x="48" y="218" text-anchor="start" font-size="11" font-weight="700" fill="#94a3b8" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x = 0</text></svg>
:::

Le point (1 ; 0) du dessin traduit ln 1 = 0 ; la courbe qui s'enfonce vers le bas près de l'axe des ordonnées traduit une limite −∞ en 0, que l'exemple établit ; le point (e ; 1) traduit ln e = 1.

::: exemple Des limites au nombre e
1. Limite en 0⁺ : on pose X = 1/x ; quand x → 0⁺, X → +∞, et ln x = ln(1/X) = −ln X, qui tend vers −∞. L'axe des ordonnées est asymptote verticale.
2. ln est continue et strictement croissante sur ]0 ; +∞[, de limites −∞ et +∞ : elle prend toutes les valeurs de ℝ, une seule fois chacune (chapitre 3). C'est une bijection de ]0 ; +∞[ sur ℝ.
3. Le réel 1 a donc un unique antécédent, que l'on note **e** : ln e = 1, avec e ≈ 2,718281828.
4. Pour n entier relatif, ln(eⁿ) = n ln e = n, donc ln x = n ⟺ x = eⁿ. Par exemple ln x = −2 donne x = e⁻² = 1/e² ≈ 0,135, et ln √e = ½ ln e = ½.

:::

::: piege Croire que ln « monte lentement » donc qu'elle est bornée
Dans le tableau, ln 10¹⁰⁰⁰ ≈ 2 302 seulement, et l'on conclut « ln ne dépassera jamais, disons, 10 000 ». Cela tente parce que les valeurs croissent très peu. Mais lim x→+∞ ln x = +∞ : pour atteindre 100, il suffit de x = e¹⁰⁰ ≈ 2,7 × 10⁴³, un nombre immense mais fini. Croître lentement n'est pas être borné.
:::

::: propriete
- ln est strictement croissante sur ]0 ; +∞[ : de −∞ (limite en 0⁺) à +∞ (limite en +∞), en s'annulant en 1.
- C'est une bijection de ]0 ; +∞[ sur ℝ ; l'équation ln x = 1 a pour unique solution e ≈ 2,718281828.
- Pour tout entier relatif n, ln x = n ⟺ x = eⁿ.

| x | 0 | | 1 | | +∞ |
| --- | --- | --- | --- | --- | --- |
| ln x | −∞ | ↗ | 0 | ↗ | +∞ |

Cas limite : n = 0 donne e⁰ = 1, d'où ln x = 0 ⟺ x = 1. Et eⁿ > 0 pour tout n : ln x = −2 a bien une solution, positive.
:::

::: verifie
Résoudre ln x = −3, puis donner la valeur approchée de la solution au centième.

---

ln est une bijection de ]0 ; +∞[ sur ℝ et −3 est un réel : l'équation a une unique solution, x = e⁻³. Elle est positive, comme il se doit, et e⁻³ ≈ 0,0498, soit 0,05 au centième. Une équation ln x = n se résout toujours par x = eⁿ.
:::

::: retenir
ln croît de −∞ en 0⁺ à +∞ en +∞ ; c'est une bijection de ]0 ; +∞[ sur ℝ, et ln x = n ⟺ x = eⁿ, où e ≈ 2,718281828 est l'unique solution de ln x = 1.
:::

## ⚡ Équations, inéquations et systèmes avec ln

Tu places 1 000 dinars à 3,5 % par an à intérêts composés : le capital après n années est Cₙ = 1 000 × 1,035ⁿ, suite géométrique de raison 1,035 (chapitre 1).
Au bout de combien d'années aura-t-il doublé ? L'inconnue n est en exposant : aucune opération déjà connue ne l'en sort.

::: exemple Doubler un capital : 1 000 × 1,035ⁿ ≥ 2 000
1. On doit avoir 1,035ⁿ ≥ 2 : les deux membres sont strictement positifs.
2. ln est strictement croissante, donc elle conserve le sens : ln(1,035ⁿ) ≥ ln 2.
3. Une puissance entière sort de ln : n ln 1,035 ≥ ln 2.
4. ln 1,035 ≈ 0,0344 est strictement positif, on divise sans changer le sens : n ≥ ln 2/ln 1,035 ≈ 0,6931/0,0344 ≈ 20,15. Le plus petit entier est n = 21. Contrôle : 1,035²⁰ ≈ 1,990 < 2 et 1,035²¹ ≈ 2,059 ≥ 2 ✓.

:::

::: exemple Trois résolutions, chacune avec ses conditions d'existence
1. ln(x + 6) = 2 ln x. Conditions : x + 6 > 0 et x > 0, donc x > 0. Comme 2 ln x = ln x², l'équation devient x + 6 = x², soit (x − 3)(x + 2) = 0. La racine −2 viole x > 0 : **S = {3}**.
2. ln(2x − 1) ≤ ln(x + 3). Conditions : 2x − 1 > 0 et x + 3 > 0, donc x > 1/2. La croissance de ln donne 2x − 1 ≤ x + 3, soit x ≤ 4 : **S = ]1/2 ; 4]**.
3. (ln x)² + ln x − 2 = 0. On pose X = ln x : X² + X − 2 = (X − 1)(X + 2) = 0, donc X = 1 ou X = −2. Comme ln x = n ⟺ x = eⁿ, on obtient **x = e ou x = e⁻²**.

:::

::: exemple Un système : x + y = 20 et ln x + ln y = ln 96
1. Conditions : x > 0 et y > 0.
2. ln x + ln y = ln(xy) = ln 96, donc xy = 96 (ln est injective).
3. x et y ont pour somme 20 et pour produit 96 : ce sont les racines de t² − 20t + 96 = 0, de discriminant 400 − 384 = 16, soit t = (20 ± 4)/2 = 12 ou 8.
4. Les deux sont strictement positifs : **(x ; y) = (8 ; 12) ou (12 ; 8)**.

:::

::: piege Résoudre en « enlevant » ln sans écrire les conditions
Pour ln(x − 5) = ln(3x + 1), on écrit x − 5 = 3x + 1, donc x = −3. Cela tente parce que ln a = ln b équivaut à a = b. Mais en x = −3, x − 5 = −8 < 0 : ln(−8) n'existe pas. Les conditions donnent x > 5 et −3 n'y est pas : **S = ∅**. Une valeur trouvée hors du domaine est une fausse solution.
:::

::: methode
Pour toute équation ou inéquation avec ln :

1. écrire les **conditions d'existence** : chaque expression sous un ln est strictement positive ;
2. ramener à une forme ln A = ln B (ou ln A ≤ ln B), ou poser X = ln x si ln x apparaît seul ;
3. appliquer l'équivalence ou la croissance de ln, puis résoudre ;
4. rejeter toute solution qui viole les conditions.

Cas limite : si l'inconnue est en exposant, on prend ln des deux membres, puis on divise par ln a en regardant son signe. Pour a < 1, ln a < 0 et l'inégalité change de sens : 0,8ⁿ ≤ 0,1 donne n ln 0,8 ≤ ln 0,1, donc n ≥ ln 0,1/ln 0,8 ≈ 10,3, soit n = 11.
:::

::: verifie
Résoudre ln(2x + 3) = 2 ln x.

---

Conditions : 2x + 3 > 0 et x > 0, donc x > 0. Alors 2 ln x = ln x², et l'équation devient 2x + 3 = x², soit (x − 3)(x + 1) = 0. La racine −1 ne vérifie pas x > 0 : S = {3}. On a écrit les conditions d'abord et rejeté la solution hors domaine.
:::

::: retenir
Conditions d'existence d'abord, puis ln A = ln B ⟹ A = B ou la croissance de ln ; une solution hors des conditions est rejetée, et diviser par un ln négatif renverse l'inégalité.
:::

## 🔬 Encadrer ln(1 + x) par des polynômes

Un programme qui ne sait faire que des additions et des multiplications doit, pour afficher ln 1,1, coincer ln(1 + x) entre des expressions qui n'utilisent que ces deux opérations, des polynômes en x.
Peut-on trouver de tels polynômes, et quelle précision en attendre ?

Un outil du chapitre 4 : si f est continue sur [0 ; x], dérivable sur ]0 ; x[ et si m ≤ f′ ≤ M, alors m·x ≤ f(x) − f(0) ≤ M·x (inégalité des accroissements finis).

::: exemple Coincer ln(1 + x) pour x > 0
1. On pose f(t) = ln(1 + t) − (t − t²/2) sur [0 ; x] : f(0) = 0, et il suffit d'encadrer f(x) = f(x) − f(0).
2. f′(t) = 1/(1 + t) − 1 + t = (1 − (1 + t) + t(1 + t))/(1 + t) = t²/(1 + t), en mettant au même dénominateur.
3. Pour t dans [0 ; x], 1 + t ≥ 1, donc 0 ≤ f′(t) ≤ t² ≤ x² : on prend m = 0 et M = x².
4. L'inégalité des accroissements finis donne 0 ≤ f(x) ≤ x² × x = x³, c'est-à-dire x − x²/2 ≤ ln(1 + x) ≤ x − x²/2 + x³.

:::

::: figure Pour x positif, la courbe de ln(1 + x) est coincée entre la parabole x − x²/2 en dessous et la courbe x − x²/2 + x³ au-dessus ; les trois se confondent près de 0
<svg viewBox="0 -22 340 272"><title>Pour x positif, la courbe de ln(1 + x) reste entre la parabole x − x²/2 en dessous et la courbe x − x²/2 + x³ au-dessus</title><line x1="50" y1="215" x2="335" y2="215" stroke="#0f172a" stroke-width="1.6"/><line x1="50" y1="224.5" x2="50" y2="-13" stroke="#0f172a" stroke-width="1.6"/><polygon points="335,215 328,211.5 328,218.5" fill="#0f172a"/><polygon points="50,-13 46.5,-6 53.5,-6" fill="#0f172a"/><text x="331" y="208" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x</text><text x="58" y="-5" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">y</text><line x1="110" y1="212" x2="110" y2="218" stroke="#0f172a" stroke-width="1.3"/><text x="110" y="230" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0,2</text><line x1="170" y1="212" x2="170" y2="218" stroke="#0f172a" stroke-width="1.3"/><text x="170" y="230" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0,4</text><line x1="230" y1="212" x2="230" y2="218" stroke="#0f172a" stroke-width="1.3"/><text x="230" y="230" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0,6</text><line x1="290" y1="212" x2="290" y2="218" stroke="#0f172a" stroke-width="1.3"/><text x="290" y="230" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0,8</text><line x1="47" y1="120" x2="53" y2="120" stroke="#0f172a" stroke-width="1.3"/><text x="44" y="124" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0,5</text><line x1="47" y1="25" x2="53" y2="25" stroke="#0f172a" stroke-width="1.3"/><text x="44" y="29" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><polyline points="50,215 54.1,212.4 58.2,209.9 62.3,207.4 66.4,204.9 70.5,202.4 74.6,200 78.7,197.5 82.8,195.1 86.9,192.7 91,190.3 95.1,187.9 99.2,185.6 103.3,183.2 107.4,180.8 111.5,178.4 115.6,176 119.7,173.6 123.8,171.2 127.9,168.7 132,166.3 136.1,163.8 140.2,161.3 144.3,158.8 148.4,156.2 152.5,153.6 156.6,151 160.7,148.3 164.8,145.6 168.9,142.8 173,140 177.1,137.1 181.2,134.2 185.3,131.2 189.4,128.2 193.5,125.1 197.6,121.9 201.7,118.6 205.8,115.3 209.9,111.9 214,108.5 218.1,104.9 222.2,101.3 226.3,97.6 230.4,93.8 234.5,89.9 238.6,85.9 242.7,81.8 246.8,77.6 250.9,73.3 255,68.9 259.1,64.4 263.2,59.8 267.3,55 271.4,50.2 275.5,45.2 279.6,40.1 283.7,34.8 287.8,29.5 291.9,24 296,18.3" fill="none" stroke="#b45309" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><polyline points="50,215 54.5,212.2 59,209.4 63.5,206.6 68,203.9 72.5,201.3 77,198.6 81.5,196 86,193.5 90.5,190.9 95,188.4 99.5,186 104,183.6 108.5,181.2 113,178.8 117.5,176.4 122,174.1 126.5,171.8 131,169.6 135.5,167.4 140,165.2 144.5,163 149,160.8 153.5,158.7 158,156.6 162.5,154.5 167,152.4 171.5,150.4 176,148.4 180.5,146.4 185,144.4 189.5,142.4 194,140.5 198.5,138.6 203,136.7 207.5,134.8 212,133 216.5,131.1 221,129.3 225.5,127.5 230,125.7 234.5,123.9 239,122.2 243.5,120.4 248,118.7 252.5,117 257,115.3 261.5,113.6 266,112 270.5,110.3 275,108.7 279.5,107.1 284,105.4 288.5,103.8 293,102.3 297.5,100.7 302,99.1 306.5,97.6 311,96.1 315.5,94.6 320,93" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><polyline points="50,215 54.5,212.2 59,209.4 63.5,206.6 68,203.9 72.5,201.3 77,198.7 81.5,196.1 86,193.6 90.5,191.1 95,188.6 99.5,186.2 104,183.9 108.5,181.6 113,179.3 117.5,177.1 122,174.9 126.5,172.7 131,170.6 135.5,168.6 140,166.6 144.5,164.6 149,162.6 153.5,160.8 158,158.9 162.5,157.1 167,155.3 171.5,153.6 176,152 180.5,150.3 185,148.7 189.5,147.2 194,145.7 198.5,144.2 203,142.8 207.5,141.4 212,140.1 216.5,138.8 221,137.6 225.5,136.4 230,135.2 234.5,134.1 239,133 243.5,132 248,131 252.5,130 257,129.1 261.5,128.3 266,127.4 270.5,126.7 275,125.9 279.5,125.2 284,124.6 288.5,124 293,123.4 297.5,122.9 302,122.4 306.5,122 311,121.6 315.5,121.3 320,121" fill="none" stroke="#1d4ed8" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><line x1="70" y1="22" x2="92" y2="22" stroke="#b45309" stroke-width="2.8"/><text x="98" y="26" text-anchor="start" font-size="11" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x − x²/2 + x³</text><line x1="70" y1="39" x2="92" y2="39" stroke="#0f6e56" stroke-width="2.8"/><text x="98" y="43" text-anchor="start" font-size="11" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">ln(1 + x)</text><line x1="70" y1="56" x2="92" y2="56" stroke="#1d4ed8" stroke-width="2.8"/><text x="98" y="60" text-anchor="start" font-size="11" font-weight="700" fill="#1d4ed8" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x − x²/2</text></svg>
:::

Les trois courbes partent du même point (0 ; 0) et se séparent peu à peu : plus x est petit, plus l'encadrement est fin, car l'écart maximal est x³.

::: exemple Valeurs approchées de ln 1,1 et de ln 1,2
1. Pour ln 1,1, x = 0,1 : x − x²/2 = 0,1 − 0,005 = 0,095 et x³ = 0,001, donc 0,095 ≤ ln 1,1 ≤ 0,096.
2. L'amplitude de l'encadrement est 0,001 : chaque borne est à moins de 10⁻³ de ln 1,1. Donc ln 1,1 ≈ 0,095 à 10⁻³ près (la calculatrice donne 0,0953 ✓).
3. Pour ln 1,2, x = 0,2 : x − x²/2 = 0,18 et x³ = 0,008, donc 0,18 ≤ ln 1,2 ≤ 0,188.
4. L'amplitude est 0,008 ≤ 10⁻² : ln 1,2 ≈ 0,18 à 10⁻² près.

:::

::: piege Garantir une précision que l'amplitude ne donne pas
Pour ln 1,3, x = 0,3 : 0,255 ≤ ln 1,3 ≤ 0,282, et l'on écrit « ln 1,3 ≈ 0,26 à 10⁻² près ». Cela tente parce que 0,26 est bien dans l'encadrement. Mais l'amplitude est 0,027 > 10⁻² : ln 1,3 pourrait être n'importe où entre 0,255 et 0,282, et rien ne garantit l'écart. Une précision de 10⁻² exige une amplitude d'au plus 10⁻², donc un x assez petit, puisque l'écart croît comme x³.
:::

::: propriete
Pour tout réel x > 0 :

- x − x²/2 ≤ ln(1 + x) ≤ x − x²/2 + x³ ;
- x/(1 + x) ≤ ln(1 + x) ≤ x, par la même méthode avec f(t) = ln(1 + t), dont la dérivée 1/(1 + t) reste entre m = 1/(1 + x) et M = 1 sur [0 ; x].

Conséquence : 0 ≤ (ln(1 + x) − x + x²/2)/x² ≤ x, donc ce quotient tend vers 0 quand x → 0⁺ (théorème des gendarmes).

Cas limite : ces inégalités sont établies pour x > 0, en x = 0 elles sont des égalités. Et avec X = 1 + x, la seconde s'écrit 1 − 1/X ≤ ln X ≤ X − 1 pour X > 1.
:::

::: verifie
Encadrer ln 1,05 avec x − x²/2 ≤ ln(1 + x) ≤ x − x²/2 + x³, puis donner une valeur approchée à 10⁻³ près.

---

Ici x = 0,05 : x − x²/2 = 0,05 − 0,00125 = 0,04875 et x³ = 0,000125, donc 0,04875 ≤ ln 1,05 ≤ 0,048875. L'amplitude est 0,000125 ≤ 10⁻³ : ln 1,05 ≈ 0,049 à 10⁻³ près. On a vérifié l'amplitude avant de conclure sur la précision.
:::

::: retenir
Pour x > 0, x − x²/2 ≤ ln(1 + x) ≤ x − x²/2 + x³ et x/(1 + x) ≤ ln(1 + x) ≤ x ; la précision d'une valeur approchée est donnée par l'amplitude de l'encadrement.
:::

## 🔮 Limites de référence et changements de variable

Calculons deux rapports avec ln, de plus en plus près de 1 d'un côté, de plus en plus loin de l'autre :

| h | 0,1 | 0,01 | 0,001 |
| --- | --- | --- | --- |
| ln(1 + h)/h | 0,9531 | 0,9950 | 0,9995 |

| x | 10 | 1 000 | 1 000 000 |
| --- | --- | --- | --- |
| (ln x)/x | 0,2303 | 0,0069 | 0,0000138 |

Le premier rapport semble tendre vers 1, le second vers 0.
Peut-on le démontrer, et comment s'en servir pour lever les formes indéterminées ?

::: exemple Pourquoi ces limites, et comment en obtenir d'autres
1. Le nombre dérivé : ln 1 = 0 et (ln)′(1) = 1, donc lim h→0 ln(1 + h)/h = lim h→0 (ln(1 + h) − ln 1)/h = 1.
2. Pour (ln x)/x, posons f(x) = ln x − √x : f′(x) = 1/x − 1/(2√x) = (2 − √x)/(2x) ≤ 0 pour x ≥ 4, donc f décroît sur [4 ; +∞[ et f(x) ≤ f(4) = ln 4 − 2 ≈ −0,61 < 0 : ln x < √x.
3. Ainsi 0 < (ln x)/x < √x/x = 1/√x pour x ≥ 4, et 1/√x → 0 : par encadrement, lim x→+∞ (ln x)/x = 0.
4. En 0⁺, on pose X = 1/x : x ln x = (1/X) ln(1/X) = −(ln X)/X, qui tend vers 0 quand X → +∞. On a lim x→0⁺ x ln x = 0.

:::

::: exemple Calculer des limites par changement de variable ou factorisation
1. lim x→+∞ ln(x + 3)/(3x − 2) : on écrit ln(x + 3)/(x + 3) × (x + 3)/(3x − 2). Avec X = x + 3 → +∞, le premier facteur tend vers 0 ; le second tend vers 1/3. La limite est 0.
2. lim x→+∞ (ln x)²/x : on pose x = X², soit ln x = 2 ln X, donc (ln x)²/x = 4 (ln X)²/X² = 4((ln X)/X)², qui tend vers 0.
3. lim x→+∞ (x − ln x) : forme +∞ − ∞, on factorise x(1 − (ln x)/x), et (ln x)/x → 0 donne +∞.
4. lim x→+∞ (ln(2x + 1) − ln x) = lim ln((2x + 1)/x) = lim ln(2 + 1/x) = ln 2, car ln est continue en 2.
5. lim x→0 ln(1 + 3x)/x : on écrit 3 × ln(1 + 3x)/(3x), et h = 3x → 0 donne 3 × 1 = 3.

:::

::: piege Appliquer (ln x)/x → 0 en 0⁺
En 0⁺, on écrit « (ln x)/x → 0 comme en +∞ ». Cela tente parce que la même expression est dans le tableau. Mais en 0⁺, ln x → −∞ et 1/x → +∞ : le produit (ln x) × (1/x) tend vers −∞. La limite 0 n'est vraie qu'en +∞ : avant d'appliquer un résultat, on vérifie vers où va x.
:::

::: propriete
- lim x→1 (ln x)/(x − 1) = 1 et lim h→0 ln(1 + h)/h = 1 ;
- lim x→+∞ (ln x)/x = 0 et, pour n entier, n ≥ 1 : lim x→+∞ (ln x)/xⁿ = 0 ;
- lim x→0⁺ x ln x = 0 et, pour n ≥ 2 : lim x→0⁺ xⁿ ln x = 0 ;
- lim x→+∞ (ln x)/√x = 0 et lim x→0⁺ √x ln x = 0.

Conséquence graphique : (ln x)/x → 0 signifie que la courbe de ln a, en +∞, une branche parabolique de direction l'axe des abscisses.

Cas limite : tous ces résultats portent sur un seul sens à la fois (+∞ ou 0⁺). En 0⁺, (ln x)/x → −∞.
:::

::: verifie
Calculer lim x→+∞ (x² − 3 ln x).

---

C'est une forme +∞ − ∞ : on factorise le terme dominant, x² − 3 ln x = x²(1 − 3 (ln x)/x²). Comme (ln x)/x² → 0, la parenthèse tend vers 1 et la limite est +∞. On a ramené ln à un rapport de référence.
:::

::: retenir
ln est négligeable devant toute puissance de x : (ln x)/xⁿ → 0 en +∞ et xⁿ ln x → 0 en 0⁺ ; et ln(1 + h)/h → 1 en 0. On vérifie toujours le sens de la limite.
:::

## 🛡️ ln(u) : dériver, primitiver, étudier

Un programme de tracé évalue f(x) = ln(2x − 3). Pour quels x l'expression existe-t-elle ?
Quelle est sa dérivée ? Et si l'on ne te donne que la dérivée 2/(2x − 3), comment remonter à la fonction ?

::: exemple Dériver ln(2x − 3), puis ln|2x − 3|
1. f(x) = ln(2x − 3) existe pour 2x − 3 > 0, c'est-à-dire x > 3/2.
2. f est la composée de u(x) = 2x − 3 puis de ln : f′(x) = u′(x) × (ln)′(u(x)) = 2 × 1/(2x − 3) = 2/(2x − 3).
3. g(x) = ln|2x − 3| existe pour tout x ≠ 3/2. Sur ]3/2 ; +∞[, |2x − 3| = 2x − 3 et g′(x) = 2/(2x − 3).
4. Sur ]−∞ ; 3/2[, |2x − 3| = 3 − 2x : g′(x) = −2 × 1/(3 − 2x) = 2/(2x − 3). On trouve la même formule des deux côtés : ln|2x − 3| est donc une primitive de 2/(2x − 3) sur chacun des deux intervalles, ce qui répond à la question de départ.

:::

::: piege Oublier le facteur u′
Pour f(x) = ln(3x + 5), on écrit « f′(x) = 1/(3x + 5) ». Cela tente parce que (ln)′(x) = 1/x : il suffirait de remplacer x par 3x + 5. Mais on dérive une composée : f′(x) = 3 × 1/(3x + 5) = 3/(3x + 5). Contrôle : entre x = 0 et x = 0,1, f varie de ln 5 à ln 5,3, soit (ln 5,3 − ln 5)/0,1 ≈ 0,58, proche de 3/5 = 0,6 et loin de 1/5 = 0,2.
:::

::: propriete
- **Dérivée.** Si u est dérivable et strictement positive sur un intervalle I, alors ln∘u est dérivable sur I et (ln u)′ = u′/u.
- **Primitive.** Si u est dérivable sur I et ne s'annule pas sur I, les primitives de u′/u sur I sont x ↦ ln|u(x)| + k, avec k constante réelle.

Cas limite : u ne doit pas s'annuler sur I. Pour x ↦ 1/x, la primitive est ln x sur ]0 ; +∞[ et ln|x| = ln(−x) sur ]−∞ ; 0[ : deux intervalles, deux formules.
:::

::: exemple Reconnaître u′/u pour primitiver
1. x ↦ 3x²/(x³ + 1) sur ]−1 ; +∞[ : u = x³ + 1 a pour dérivée u′ = 3x², donc une primitive est ln(x³ + 1).
2. x ↦ x/(1 + x²) : avec u = 1 + x², u′ = 2x, on écrit x/(1 + x²) = ½ × 2x/(1 + x²), d'où la primitive ½ ln(1 + x²).
3. x ↦ 1/(x ln x) sur ]1 ; +∞[ : avec u = ln x, u′ = 1/x et u′/u = 1/(x ln x), d'où la primitive ln(ln x), puisque ln x > 0 sur cet intervalle.

:::

::: exemple Étudier f(x) = ln((x − 1)/(x + 2))
1. Ensemble de définition : (x − 1)/(x + 2) > 0 ; le tableau de signes donne x < −2 ou x > 1, donc D = ]−∞ ; −2[ ∪ ]1 ; +∞[.
2. En 1⁺, (x − 1)/(x + 2) → 0⁺, donc f → −∞. En −2⁻, x − 1 → −3 et x + 2 → 0⁻, le quotient tend vers +∞, donc f → +∞. En ±∞, (x − 1)/(x + 2) = (1 − 1/x)/(1 + 2/x) → 1 et ln est continue en 1 : f → ln 1 = 0.
3. Asymptotes verticales x = −2 et x = 1, asymptote horizontale y = 0 en ±∞.
4. Avec u = (x − 1)/(x + 2), u′ = 3/(x + 2)² : f′ = u′/u = 3/(x + 2)² × (x + 2)/(x − 1) = 3/((x + 2)(x − 1)). Sur D, (x + 2)(x − 1) > 0, donc f′ > 0.
5. f croît de 0 à +∞ sur ]−∞ ; −2[ et de −∞ à 0 sur ]1 ; +∞[.

:::

::: figure Deux branches : à gauche f monte de 0 vers +∞ le long de x = −2 ; à droite f monte de −∞ le long de x = 1 vers l'asymptote y = 0
<svg viewBox="0 0 340 230"><title>Courbe de f(x) = ln((x − 1)/(x + 2)) : deux branches, asymptotes verticales x = −2 et x = 1, asymptote horizontale y = 0</title><line x1="6.6" y1="115" x2="333.4" y2="115" stroke="#0f172a" stroke-width="1.6"/><line x1="170" y1="217" x2="170" y2="13" stroke="#0f172a" stroke-width="1.6"/><polygon points="333.4,115 326.4,111.5 326.4,118.5" fill="#0f172a"/><polygon points="170,13 166.5,20 173.5,20" fill="#0f172a"/><text x="329.4" y="108" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x</text><text x="178" y="21" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">y</text><line x1="56" y1="112" x2="56" y2="118" stroke="#0f172a" stroke-width="1.3"/><text x="56" y="130" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−6</text><line x1="94" y1="112" x2="94" y2="118" stroke="#0f172a" stroke-width="1.3"/><text x="94" y="130" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−4</text><line x1="208" y1="112" x2="208" y2="118" stroke="#0f172a" stroke-width="1.3"/><text x="208" y="130" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><line x1="246" y1="112" x2="246" y2="118" stroke="#0f172a" stroke-width="1.3"/><text x="246" y="130" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4</text><line x1="167" y1="175" x2="173" y2="175" stroke="#0f172a" stroke-width="1.3"/><text x="164" y="179" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−2</text><line x1="167" y1="145" x2="173" y2="145" stroke="#0f172a" stroke-width="1.3"/><text x="164" y="149" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−1</text><line x1="167" y1="85" x2="173" y2="85" stroke="#0f172a" stroke-width="1.3"/><text x="164" y="89" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><line x1="167" y1="55" x2="173" y2="55" stroke="#0f172a" stroke-width="1.3"/><text x="164" y="59" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><line x1="132" y1="217" x2="132" y2="13" stroke="#94a3b8" stroke-width="1.3" stroke-dasharray="5 3"/><line x1="189" y1="217" x2="189" y2="13" stroke="#94a3b8" stroke-width="1.3" stroke-dasharray="5 3"/><polyline points="18,102.8 19.9,102.7 21.7,102.5 23.6,102.3 25.4,102.1 27.3,102 29.1,101.8 31,101.6 32.8,101.4 34.7,101.2 36.5,101 38.4,100.7 40.2,100.5 42.1,100.3 43.9,100 45.8,99.8 47.6,99.5 49.5,99.2 51.3,99 53.2,98.7 55,98.4 56.9,98.1 58.7,97.7 60.6,97.4 62.4,97.1 64.3,96.7 66.1,96.3 68,95.9 69.8,95.5 71.7,95 73.5,94.6 75.4,94.1 77.2,93.6 79.1,93.1 80.9,92.5 82.8,91.9 84.6,91.3 86.5,90.6 88.3,90 90.2,89.2 92,88.4 93.9,87.6 95.7,86.7 97.6,85.7 99.4,84.7 101.3,83.5 103.1,82.3 105,81 106.8,79.5 108.7,77.9 110.5,76.1 112.4,74.1 114.2,71.9 116.1,69.4 117.9,66.4 119.8,63 121.6,58.9 123.5,53.8 125.3,47.4 127.2,38.5 129,25" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><polyline points="192,205 194.1,189.7 196.3,180.2 198.5,173.4 200.7,168.2 202.8,164 205,160.6 207.2,157.6 209.3,155.1 211.5,152.9 213.7,150.9 215.8,149.2 218,147.6 220.2,146.2 222.3,144.9 224.5,143.7 226.7,142.7 228.8,141.7 231,140.7 233.2,139.9 235.3,139.1 237.5,138.3 239.7,137.6 241.8,137 244,136.3 246.2,135.8 248.3,135.2 250.5,134.7 252.7,134.2 254.8,133.7 257,133.3 259.2,132.8 261.3,132.4 263.5,132 265.7,131.7 267.8,131.3 270,131 272.2,130.7 274.3,130.3 276.5,130.1 278.7,129.8 280.8,129.5 283,129.2 285.2,129 287.3,128.7 289.5,128.5 291.7,128.2 293.8,128 296,127.8 298.2,127.6 300.3,127.4 302.5,127.2 304.7,127 306.8,126.8 309,126.7 311.2,126.5 313.3,126.3 315.5,126.2 317.7,126 319.8,125.8 322,125.7" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><text x="128" y="19" text-anchor="end" font-size="11" font-weight="700" fill="#94a3b8" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x = −2</text><text x="193" y="19" text-anchor="start" font-size="11" font-weight="700" fill="#94a3b8" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x = 1</text><text x="65.5" y="85.4" text-anchor="middle" font-size="12" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">y = f(x)</text></svg>
:::

La courbe ne coupe jamais l'axe des abscisses : f(x) = 0 exigerait (x − 1)/(x + 2) = 1, soit −1 = 2, impossible. Les deux droites en pointillés et l'axe des abscisses sont les asymptotes trouvées aux étapes 2 et 3.

::: exemple Quand le signe de f′ ne se voit pas : f(x) = x ln x − x²/2 sur ]0 ; +∞[
1. f′(x) = ln x + 1 − x : la dérivée de x ln x est ln x + x × 1/x = ln x + 1.
2. Son signe n'est pas lisible : on étudie la fonction auxiliaire g(x) = ln x + 1 − x. Alors g′(x) = 1/x − 1 = (1 − x)/x, positive sur ]0 ; 1[ et négative sur ]1 ; +∞[.
3. g croît puis décroît : son maximum est g(1) = 0 + 1 − 1 = 0. Donc g(x) ≤ 0 pour tout x > 0, avec égalité seulement en 1.
4. Ainsi f′ ≤ 0, nulle en un seul point : f est strictement décroissante sur ]0 ; +∞[.
5. Au passage, g ≤ 0 s'écrit ln x ≤ x − 1 pour tout x > 0. Avec 1/x à la place de x, on obtient 1 − 1/x ≤ ln x.

:::

::: verifie
Donner l'ensemble de définition de h(x) = ln(x² + x − 6) et calculer h′(x).

---

Il faut x² + x − 6 = (x + 3)(x − 2) > 0, soit x < −3 ou x > 2 : D = ]−∞ ; −3[ ∪ ]2 ; +∞[. Avec u = x² + x − 6 et u′ = 2x + 1, h′(x) = (2x + 1)/(x² + x − 6) : on a dérivé u, puis divisé par u.
:::

::: retenir
(ln u)′ = u′/u là où u > 0 ; les primitives de u′/u sont ln|u| + k ; pour étudier une fonction à logarithme : domaine, limites, dérivée u′/u, et une fonction auxiliaire quand le signe de f′ ne se lit pas.
:::

## 🔟 Logarithme décimal : compter les puissances de 10

Le pH d'une solution, le niveau sonore d'un concert, la taille d'un nombre en chiffres : toutes ces échelles comptent des puissances de 10.
Peut-on construire à partir de ln une fonction qui vaut exactement p en 10ᵖ ?

::: definition
Le **logarithme décimal**, noté **log**, est la fonction définie sur ]0 ; +∞[ par :

$$ log x = ln x / ln 10 $$

On a ln 10 ≈ 2,302585, donc 1/ln 10 ≈ 0,434294 et log x ≈ 0,4343 ln x. La fonction log vérifie les mêmes propriétés que ln (produit en somme, quotient en différence, puissance en facteur), puisqu'on divise ln par une constante, et log 10 = 1.
:::

| x | 0,001 | 0,1 | 1 | 10 | 1 000 |
| --- | --- | --- | --- | --- | --- |
| log x | −3 | −1 | 0 | 1 | 3 |

Pour une puissance de 10, log x est l'exposant : log(10ᵖ) = p ln 10/ln 10 = p. Le logarithme décimal « compte les zéros ».

::: exemple Partie entière de log x par l'écriture scientifique
1. Tout x > 0 s'écrit x = a × 10ᵖ avec 1 ≤ a < 10 et p entier, donc log x = log a + p, avec 0 ≤ log a < 1 puisque log 1 = 0 et log 10 = 1. L'entier p est la partie entière de log x.
2. 42 500 = 4,25 × 10⁴ : log 42 500 = log 4,25 + 4 ≈ 0,628 + 4, de partie entière 4.
3. 0,0073 = 7,3 × 10⁻³ : log 0,0073 = log 7,3 − 3 ≈ 0,863 − 3 = −2,137, de partie entière −3, le plus grand entier inférieur ou égal à −2,137.
4. 1/8 = 0,125 = 1,25 × 10⁻¹ : log(1/8) = log 1,25 − 1 ≈ 0,097 − 1 = −0,903, de partie entière −1.

:::

::: exemple Nombre de chiffres de 2⁶⁴ et niveau sonore
1. Un entier N = a × 10ᵖ (1 ≤ a < 10) s'écrit avec p + 1 chiffres : il a donc autant de chiffres que (partie entière de log N) + 1.
2. log 2⁶⁴ = 64 log 2 ≈ 64 × 0,30103 = 19,266 : la partie entière est 19, donc 2⁶⁴ a 20 chiffres.
3. Le niveau sonore, en décibels, est d(I) = 10 log(I/I₀). Pour I = 10⁶ I₀ (voix humaine), d = 10 × 6 = 60 dB.
4. Si l'intensité est multipliée par 2, d(2I) − d(I) = 10 log(2I/I₀) − 10 log(I/I₀) = 10 log 2 ≈ 3,0 dB : le quotient devient une différence.

:::

Le manuel donne deux programmes Pascal. Le premier calcule simplement y := ln(x)/ln(10). Le second compte les puissances de 10 de x, sans appeler log ; en pseudo-code :

```
si x < 1 : x ← 1/x ; afficher « − »
n ← 0
tant que x ≥ 10 : x ← x/10 ; n ← n + 1
afficher n, « , »
```

::: exemple Suivre l'algorithme pas à pas
1. Pour x = 4 250 (x ≥ 1) : x vaut 4 250, 425, 42,5 puis 4,25, avec n = 0, 1, 2 puis 3. On affiche « 3, » : c'est la partie entière de log 4 250 ≈ 3,628.
2. Pour x = 0,0073 (x < 1) : on affiche « − » et x devient 1/0,0073 ≈ 137, puis deux divisions par 10 donnent n = 2. On affiche « −2, » et les décimales qui suivent donnent −2,13…
3. Pour les décimales, la boucle a ramené x dans [1 ; 10[, où 0 ≤ log x < 1 ; comme log(x¹⁰) = 10 log x décale la virgule d'un rang, le premier chiffre après la virgule de log x est la partie entière de log(x¹⁰), comptée par la même boucle. Pour x = 2, 2¹⁰ = 1 024 demande trois divisions par 10 pour passer sous 10 : log 2 = 0,3…

:::

::: piege Lire la partie entière d'un logarithme négatif sur son écriture décimale
Pour log 0,0073 ≈ −2,137, on écrit « la partie entière est −2 ». Cela tente parce que l'on garde les chiffres avant la virgule. Mais la partie entière est le plus grand entier inférieur ou égal au nombre : −3 ≤ −2,137 < −2. On le retrouve par l'écriture scientifique : 0,0073 = 7,3 × 10⁻³, donc p = −3. L'algorithme, lui, affiche « −2, » parce qu'il travaille sur 1/x.
:::

::: propriete
- log x = ln x/ln 10 ; log(10ᵖ) = p pour tout entier p ; log est strictement croissante.
- Si x = a × 10ᵖ avec 1 ≤ a < 10 et p entier, alors log x = log a + p : p est la partie entière de log x.
- Un entier N ≥ 1 a (partie entière de log N) + 1 chiffres.
- Niveau sonore : d(I) = 10 log(I/I₀) décibels ; multiplier l'intensité par 2 ajoute environ 3 dB.

Cas limite : si x = 10ᵖ exactement, a = 1 et log x = p entier ; 1 000 = 10³ a bien 4 chiffres, soit 3 + 1.
:::

::: verifie
Combien de chiffres a 5³⁰ ? On donne log 5 ≈ 0,69897.

---

log 5³⁰ = 30 log 5 ≈ 30 × 0,69897 = 20,969. La partie entière est 20, donc 5³⁰ s'écrit avec 20 + 1 = 21 chiffres. On a pris la partie entière avant d'ajouter 1.
:::

::: retenir
log x = ln x/ln 10 vaut p en 10ᵖ ; la partie entière de log x est l'exposant p de l'écriture scientifique, un entier N a (partie entière de log N) + 1 chiffres, et d = 10 log(I/I₀) mesure le niveau sonore.
:::

> 🏆 Sixième porte franchie, héros. Tu sais transformer un produit en somme, résoudre avec ln, encadrer ses valeurs, lever ses formes indéterminées et étudier une fonction à logarithme jusqu'à son tableau. Au chapitre 7, les fonctions exponentielles font le chemin inverse : elles changent les sommes en produits.
