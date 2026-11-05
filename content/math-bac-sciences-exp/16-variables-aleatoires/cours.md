# ⚔️ Variables aléatoires — de l'urne aux lois continues

> 💡 «Le hasard déroute celui qui regarde une issue ; il se laisse lire par celui qui regarde une loi.»

Ce chapitre transforme les résultats d'une expérience aléatoire en nombres (un gain, un nombre de succès, une durée) pour en calculer la loi, la moyenne et la dispersion. Sept notions : variable aléatoire et loi, espérance, variance et écart-type, fonction de répartition, loi binomiale, loi uniforme, loi exponentielle. Tu réutilises les probabilités sur un ensemble fini, l'indépendance et les combinaisons Cₙᵏ du chapitre précédent, puis les intégrales et l'exponentielle pour les deux lois à densité.

## 🎯 Variable aléatoire et loi de probabilité

À la kermesse de l'école, un sac opaque contient 7 boules : 3 boules marquées 2 et 4 boules marquées −1. Un visiteur en tire deux d'un seul coup et retient la somme des deux numéros.
Ce qui compte pour lui n'est pas le tirage, mais ce nombre : quelles valeurs peut-il prendre, et avec quelle probabilité chacune ?

::: definition
Soit (E, 𝒫(E), p) un espace probabilisé fini. Une **variable aléatoire** X est une application X : E → ℝ, qui associe un nombre à chaque issue. On note X(E) l'ensemble des valeurs prises par X, et (X = xᵢ) l'événement {a ∈ E ; X(a) = xᵢ}.
La **loi de probabilité** de X associe à chaque valeur xᵢ de X(E) le nombre pᵢ = p(X = xᵢ).
:::

| xᵢ | x₁ | x₂ | … | xₙ | Total |
| --- | --- | --- | --- | --- | --- |
| pᵢ = p(X = xᵢ) | p₁ | p₂ | … | pₙ | 1 |

Le tableau range les valeurs et leurs probabilités côte à côte ; la case « Total » annonce que les événements (X = xᵢ) couvrent toutes les issues sans se recouvrir.

::: exemple Les boules de la kermesse

1. Le tirage est simultané : card E = C₇² = 21 tirages équiprobables.
2. Deux boules « 2 » donnent la somme 4, une boule de chaque sorte donne 2 + (−1) = 1, deux boules « −1 » donnent −2. Donc X(E) = {−2 ; 1 ; 4}.
3. (X = 4) : 2 boules « 2 » parmi 3, soit C₃² = 3 tirages, donc p(X = 4) = 3/21 = 1/7.
4. (X = 1) : une boule « 2 » et une boule « −1 », soit 3 × 4 = 12 tirages, donc p(X = 1) = 12/21 = 4/7.
5. (X = −2) : 2 boules « −1 » parmi 4, soit C₄² = 6 tirages, donc p(X = −2) = 6/21 = 2/7.
6. Contrôle : 3 + 12 + 6 = 21 tirages, donc 1/7 + 4/7 + 2/7 = 1 ✓.

:::

::: piege
**Erreur : croire que les valeurs de X sont équiprobables.** On voit trois valeurs, −2, 1 et 4, et on écrit 1/3 pour chacune. Mais 6, 12 et 3 tirages mènent à ces valeurs : elles n'ont pas la même chance. Une probabilité se calcule en comptant les issues de l'événement (X = xᵢ), jamais en comptant les valeurs.
:::

::: propriete
Si X(E) = {x₁, …, xₙ}, alors p(X = x₁) + p(X = x₂) + … + p(X = xₙ) = 1.

Preuve : chaque issue a une seule image, donc les événements (X = x₁), …, (X = xₙ) forment une partition de E. La somme de leurs probabilités est p(E) = 1.

Cas limite : si X ne prend qu'une seule valeur, cette valeur a la probabilité 1.
:::

::: verifie À toi : le concours
Trois candidats passent le même test l'un après l'autre. Chacun le réussit avec la probabilité 0,6, indépendamment des autres. Le premier qui réussit est engagé et les suivants ne passent pas. Soit X le rang du candidat engagé, avec X = 4 si personne ne réussit. Donne la loi de X.

---

Pour être engagé au rang j, les j − 1 premiers échouent (probabilité 0,4 chacun) puis le jᵉ réussit : p(X = 1) = 0,6 ; p(X = 2) = 0,4 × 0,6 = 0,24 ; p(X = 3) = 0,4² × 0,6 = 0,096. Personne n'est engagé si les trois échouent : p(X = 4) = 0,4³ = 0,064. Contrôle : 0,6 + 0,24 + 0,096 + 0,064 = 1 ✓.
:::

::: retenir
Une variable aléatoire donne un nombre à chaque issue ; sa loi est le tableau des p(X = xᵢ), dont la somme vaut 1.
:::

## ⚖️ L'espérance

Au stand de tir de la fête foraine, le tireur gagne 7 dinars s'il touche le centre de la cible, 2 dinars s'il touche le bord, et perd 3 dinars (sa mise) s'il rate. Soit X son gain algébrique, de loi :

| xᵢ | −3 | 2 | 7 |
| --- | --- | --- | --- |
| p(X = xᵢ) | 0,2 | 0,5 | 0,3 |

Si le tireur joue un très grand nombre de parties, combien gagne-t-il en moyenne par partie ?

::: definition
Soit X une variable aléatoire telle que X(E) = {x₁, …, xₙ}. L'**espérance mathématique** (ou moyenne) de X est le nombre
$$ E(X) = x₁p₁ + x₂p₂ + … + xₙpₙ $$
Autrement dit, chaque valeur compte avec son poids pᵢ.
:::

**Théorème (admis).** Pour deux variables aléatoires X et Y sur le même espace probabilisé et pour tout réel α : E(αX) = αE(X) et E(X + Y) = E(X) + E(Y).

::: exemple Le gain au stand de tir

1. E(X) = (−3) × 0,2 + 2 × 0,5 + 7 × 0,3 = −0,6 + 1 + 2,1 = 2,5 dinars par partie en moyenne.
2. Si les gains triplent, E(3X) = 3 × E(X) = 7,5. Contrôle par la loi de 3X, qui prend −9, 6 et 21 : −1,8 + 3 + 6,3 = 7,5 ✓.
3. Un bonus Y de 1 dinar est versé seulement quand X = 7 (sinon Y = 0) : E(Y) = 1 × 0,3 = 0,3.
4. Par le théorème, E(X + Y) = 2,5 + 0,3 = 2,8. Contrôle : X + Y prend −3, 2 et 8 avec 0,2 ; 0,5 et 0,3, et −0,6 + 1 + 2,4 = 2,8 ✓.

:::

::: piege
**Erreur : faire la moyenne simple des valeurs.** On calcule (−3 + 2 + 7)/3 = 2 et on annonce 2 dinars par partie. Cette moyenne oublie que le tireur rate deux fois sur dix mais touche le bord une fois sur deux : chaque valeur compte avec son poids, et la bonne moyenne est 2,5.
:::

::: propriete
- E(X) s'exprime dans la même unité que X, et il est compris entre la plus petite et la plus grande valeur de X.
- E(αX) = αE(X) et E(X + Y) = E(X) + E(Y) : l'espérance de la somme est la somme des espérances.

Cas limite : E(X) n'est pas forcément une valeur que X peut prendre. Ici 2,5 n'est pas un gain possible : c'est une moyenne sur un grand nombre de parties.
:::

::: verifie À toi : les huit cartes
On tire une carte au hasard parmi 8 cartes numérotées de 1 à 8. X est le numéro obtenu ; Y vaut 2 si le numéro est un multiple de 4 et 0 sinon. Calcule E(X), E(Y) puis E(X + Y).

---

Les 8 numéros sont équiprobables : E(X) = (1 + 2 + … + 8)/8 = 36/8 = 4,5. Y vaut 2 pour les cartes 4 et 8, soit avec la probabilité 2/8 : E(Y) = 2 × 2/8 = 0,5. Par le théorème, E(X + Y) = 4,5 + 0,5 = 5. Contrôle : les huit valeurs de X + Y ont pour somme 36 + 2 + 2 = 40, et 40/8 = 5 ✓.
:::

::: retenir
E(X) = Σ xᵢpᵢ est la moyenne pondérée par les probabilités ; E(αX) = αE(X) et E(X + Y) = E(X) + E(Y).
:::

## 📏 Variance et écart-type

Un second stand propose un gain Y de 1 dinar ou de 4 dinars, avec la probabilité 0,5 chacun : E(Y) = 0,5 + 2 = 2,5, la même moyenne que le stand de tir précédent. Pourtant le gain du premier stand varie de −3 à 7, celui du second de 1 à 4 seulement. La moyenne ne dit rien de cette différence.
Comment mesurer l'écart typique des valeurs autour de E(X) ?

::: definition
Soit X une variable aléatoire. La **variance** de X est la moyenne des carrés des écarts à l'espérance, et l'**écart-type** en est la racine carrée :
$$ V(X) = E((X − E(X))²) et σ(X) = √V(X) $$
:::

**Propriété (admise).** V(X) = E(X²) − (E(X))², où E(X²) = x₁²p₁ + … + xₙ²pₙ.

::: exemple Deux stands, même moyenne

1. Par la définition, avec E(X) = 2,5 pour le stand de tir : les écarts au carré sont (−3 − 2,5)² = 30,25 ; (2 − 2,5)² = 0,25 et (7 − 2,5)² = 20,25.
2. On pondère : V(X) = 0,2 × 30,25 + 0,5 × 0,25 + 0,3 × 20,25 = 6,05 + 0,125 + 6,075 = 12,25.
3. Par la formule : E(X²) = 0,2 × 9 + 0,5 × 4 + 0,3 × 49 = 1,8 + 2 + 14,7 = 18,5, puis V(X) = 18,5 − 2,5² = 12,25 ✓, le même résultat.
4. L'écart-type vaut σ(X) = √12,25 = 3,5 dinars.
5. Pour le second stand : E(Y²) = 0,5 × 1 + 0,5 × 16 = 8,5, donc V(Y) = 8,5 − 6,25 = 2,25 et σ(Y) = 1,5 dinar. Même moyenne, mais 1,5 contre 3,5 : le second stand est bien moins dispersé.

:::

::: piege
**Erreur : oublier le carré sur l'espérance.** Avec E(X²) = 18,5 et E(X) = 2,5, on écrit V(X) = 18,5 − 2,5 = 16, d'où σ = 4. Le terme à retrancher est (E(X))² = 6,25, ce qui donne 12,25. Un contrôle : une variance n'est jamais négative, et σ(X) doit rester de l'ordre de l'écart entre les valeurs.
:::

::: propriete
- V(X) ≥ 0, et σ(X) s'exprime dans la même unité que X ;
- plus σ(X) est grand, plus les valeurs de X s'écartent de E(X) ;
- V(X) = E(X²) − (E(X))².

Cas limite : si X ne prend qu'une seule valeur, alors V(X) = 0, car cette valeur est égale à son espérance.
:::

::: verifie À toi : variance d'une loi
X prend les valeurs 0, 2 et 6 avec les probabilités 0,5 ; 0,4 et 0,1. Calcule E(X), V(X) et σ(X).

---

E(X) = 0 × 0,5 + 2 × 0,4 + 6 × 0,1 = 0,8 + 0,6 = 1,4. Ensuite E(X²) = 0 × 0,5 + 4 × 0,4 + 36 × 0,1 = 1,6 + 3,6 = 5,2. La formule retranche le carré de l'espérance : V(X) = 5,2 − 1,4² = 5,2 − 1,96 = 3,24, donc σ(X) = √3,24 = 1,8.
:::

::: retenir
V(X) = E(X²) − (E(X))² et σ(X) = √V(X) : plus σ est grand, plus les valeurs s'éloignent de l'espérance.
:::

## 📈 La fonction de répartition

Après une panne, un atelier note la durée X, en jours, d'immobilisation d'une machine. Cette durée vaut 1, 2, 3 ou 5 jours, avec la loi suivante.

| xᵢ | 1 | 2 | 3 | 5 |
| --- | --- | --- | --- | --- |
| p(X = xᵢ) | 0,1 | 0,3 | 0,4 | 0,2 |

Quelle est la probabilité que l'arrêt dure au plus 3 jours ? Plutôt que de refaire une somme à chaque question, existe-t-il une fonction qui donne d'un coup p(X ≤ x) pour tout réel x ?

::: definition
Soit X une variable aléatoire. La **fonction de répartition** de X est l'application F de ℝ dans [0 ; 1] définie par
$$ F(x) = p(X ≤ x) $$
où (X ≤ x) désigne l'événement {a ∈ E ; X(a) ≤ x}. Elle cumule les probabilités des valeurs inférieures ou égales à x.
:::

::: figure La fonction de répartition de la durée d'immobilisation monte par sauts, un saut à chaque valeur possible ; celui en x = 2 a pour hauteur 0,3
<svg viewBox="0 0 340 250">
<title>Fonction de répartition de la durée d'immobilisation : sauts en 1, 2, 3 et 5 jours, de hauteurs 0,1 ; 0,3 ; 0,4 et 0,2</title>
<path d="M40 190 L334.4 190" fill="none" stroke="#0f172a" stroke-width="1.8" stroke-linecap="round"/>
<path d="M50 196 L50 32" fill="none" stroke="#0f172a" stroke-width="1.8" stroke-linecap="round"/>
<text x="334.4" y="208" text-anchor="end" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">x</text>
<text x="54" y="28" text-anchor="start" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">F(x)</text>
<path d="M50 190 L93.5 190" fill="none" stroke="#0f6e56" stroke-width="3" stroke-linecap="round"/>
<path d="M93.5 176 L137.1 176" fill="none" stroke="#0f6e56" stroke-width="3" stroke-linecap="round"/>
<path d="M137.1 134 L180.6 134" fill="none" stroke="#0f6e56" stroke-width="3" stroke-linecap="round"/>
<path d="M180.6 78 L267.7 78" fill="none" stroke="#0f6e56" stroke-width="3" stroke-linecap="round"/>
<path d="M267.7 50 L328 50" fill="none" stroke="#0f6e56" stroke-width="3" stroke-linecap="round"/>
<circle cx="93.5" cy="190" r="4" fill="#ffffff" stroke="#0f6e56" stroke-width="2"/>
<circle cx="93.5" cy="176" r="4" fill="#0f6e56" stroke="#0f172a" stroke-width="1"/>
<circle cx="137.1" cy="176" r="4" fill="#ffffff" stroke="#0f6e56" stroke-width="2"/>
<circle cx="137.1" cy="134" r="4" fill="#0f6e56" stroke="#0f172a" stroke-width="1"/>
<circle cx="180.6" cy="134" r="4" fill="#ffffff" stroke="#0f6e56" stroke-width="2"/>
<circle cx="180.6" cy="78" r="4" fill="#0f6e56" stroke="#0f172a" stroke-width="1"/>
<circle cx="267.7" cy="78" r="4" fill="#ffffff" stroke="#0f6e56" stroke-width="2"/>
<circle cx="267.7" cy="50" r="4" fill="#0f6e56" stroke="#0f172a" stroke-width="1"/>
<path d="M50 176 L46 176" fill="none" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="42" y="180" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0,1</text>
<path d="M50 134 L46 134" fill="none" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="42" y="138" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0,4</text>
<path d="M50 78 L46 78" fill="none" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="42" y="82" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0,8</text>
<path d="M50 50 L46 50" fill="none" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="42" y="54" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">1</text>
<path d="M93.5 190 L93.5 195" fill="none" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="93.5" y="210" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">1</text>
<path d="M137.1 190 L137.1 195" fill="none" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="137.1" y="210" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">2</text>
<path d="M180.6 190 L180.6 195" fill="none" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="180.6" y="210" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">3</text>
<path d="M267.7 190 L267.7 195" fill="none" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="267.7" y="210" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">5</text>
<path d="M148.1 176 L148.1 134" fill="none" stroke="#b45309" stroke-width="2" stroke-linecap="round"/>
<text x="154.1" y="159" text-anchor="start" font-size="13" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0,3</text>
</svg>
:::

Sur la figure, un point plein marque la valeur de F à l'endroit d'un saut, un point creux la valeur qui n'est pas atteinte : le saut en x = 2 monte de 0,1 à 0,4, soit 0,3 = p(X = 2).

::: exemple La durée d'immobilisation

1. Pour x < 1, aucune valeur n'est inférieure ou égale à x : F(x) = 0.
2. Pour 1 ≤ x < 2, seule la valeur 1 compte : F(x) = 0,1. Pour 2 ≤ x < 3, les valeurs 1 et 2 comptent : F(x) = 0,1 + 0,3 = 0,4.
3. Pour 3 ≤ x < 5, F(x) = 0,4 + 0,4 = 0,8. Pour x ≥ 5, toutes les valeurs comptent : F(x) = 1.
4. Lecture : p(X ≤ 3) = F(3) = 0,8 et F(2,5) = 0,4.
5. Inégalité stricte : p(X < 3) ne compte pas la valeur 3, donc p(X < 3) = F(2) = 0,4, et non F(3).
6. Valeur isolée et intervalle : p(X = 3) = F(3) − F(2) = 0,8 − 0,4 = 0,4 ; p(2 ≤ X ≤ 5) = 1 − F(1) = 0,9 ; p(X > 2) = 1 − F(2) = 0,6.

:::

::: piege
**Erreur : lire F(3) comme p(X = 3).** Comme 3 est une valeur du tableau, on lit 0,8 comme la probabilité d'un arrêt de 3 jours exactement. Or F(3) = p(X ≤ 3) = 0,1 + 0,3 + 0,4 : c'est un cumul. La probabilité de la valeur 3 est la hauteur du saut, F(3) − F(2) = 0,4.
:::

::: propriete
Pour des valeurs x₁ < x₂ < … < xₙ :
- F(x) = 0 à gauche de x₁ et F(x) = 1 à partir de xₙ ;
- en chaque valeur xᵢ, F fait un saut de hauteur p(X = xᵢ) ;
- p(X > x) = 1 − F(x) et p(a < X ≤ b) = F(b) − F(a) pour a < b ;
- p(X < a) additionne les probabilités des valeurs strictement inférieures à a.

Cas limite : si a est une valeur de X, p(X < a) est différent de F(a), car F(a) compte aussi la valeur a.
:::

::: verifie À toi : lire F sur une autre loi
X prend les valeurs 1, 3 et 4 avec les probabilités 0,2 ; 0,5 et 0,3. Calcule F(3,5), p(X < 3) et p(X ≥ 3).

---

Les valeurs inférieures ou égales à 3,5 sont 1 et 3 : F(3,5) = 0,2 + 0,5 = 0,7. L'inégalité est stricte : p(X < 3) ne compte que la valeur 1, soit 0,2. Enfin p(X ≥ 3) est la probabilité contraire de p(X < 3) : 1 − 0,2 = 0,8, qui est bien 0,5 + 0,3.
:::

::: retenir
F(x) = p(X ≤ x) cumule les probabilités ; la probabilité d'une valeur est la hauteur du saut de F, et p(X > x) = 1 − F(x).
:::

## 🔁 La loi binomiale

Une jardinière sème 4 graines. Chacune germe avec la probabilité 0,8, indépendamment des autres. Soit X le nombre de graines qui germent.
Quelle est la loi de X, et combien de graines germent-elles en moyenne ?

::: definition
Soit une expérience formée de n épreuves identiques et indépendantes, chacune n'ayant que deux issues : succès (de probabilité p) ou échec (de probabilité 1 − p). Le nombre X de succès suit la **loi binomiale** de paramètre (n ; p), notée ℬ(n ; p) :
$$ p(X = k) = Cₙᵏ pᵏ (1 − p)ⁿ⁻ᵏ pour k ∈ {0 ; 1 ; … ; n} $$
Pour n = 1, on dit que X suit une loi de Bernoulli.
:::

::: figure La loi binomiale ℬ(4 ; 0,8) en bâtons : la hauteur de chaque bâton est p(X = k), et les cinq hauteurs ont pour somme 1
<svg viewBox="0 0 400 250">
<title>Loi binomiale B(4 ; 0,8) : bâtons de hauteurs 0,0016 ; 0,0256 ; 0,1536 ; 0,4096 et 0,4096</title>
<path d="M40 200 L385 200" fill="none" stroke="#0f172a" stroke-width="1.8" stroke-linecap="round"/>
<rect x="48" y="199.4" width="44" height="0.6" fill="#0f6e56" fill-opacity="0.28" stroke="#0f6e56" stroke-width="2.2"/>
<text x="70" y="192.4" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0,0016</text>
<text x="70" y="220" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0</text>
<rect x="118" y="190.6" width="44" height="9.4" fill="#0f6e56" fill-opacity="0.28" stroke="#0f6e56" stroke-width="2.2"/>
<text x="140" y="183.6" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0,0256</text>
<text x="140" y="220" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">1</text>
<rect x="188" y="143.8" width="44" height="56.2" fill="#0f6e56" fill-opacity="0.28" stroke="#0f6e56" stroke-width="2.2"/>
<text x="210" y="136.8" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0,1536</text>
<text x="210" y="220" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">2</text>
<rect x="258" y="50" width="44" height="150" fill="#0f6e56" fill-opacity="0.28" stroke="#0f6e56" stroke-width="2.2"/>
<text x="280" y="43" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0,4096</text>
<text x="280" y="220" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">3</text>
<rect x="328" y="50" width="44" height="150" fill="#0f6e56" fill-opacity="0.28" stroke="#0f6e56" stroke-width="2.2"/>
<text x="350" y="43" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0,4096</text>
<text x="350" y="220" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">4</text>
<text x="396" y="220" text-anchor="end" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">k</text>
</svg>
:::

Chaque bâton représente une valeur k de X et sa hauteur est p(X = k) ; les deux plus hauts sont en k = 3 et en k = 4, à égalité : 3 ou 4 graines germent le plus souvent.

::: exemple Les quatre graines

1. Semer une graine est une épreuve à deux issues (succès = elle germe, p = 0,8), répétée 4 fois de façon indépendante : X suit ℬ(4 ; 0,8), et X(E) = {0 ; 1 ; 2 ; 3 ; 4}.
2. p(X = 0) = 0,2⁴ = 0,0016 ; p(X = 1) = 4 × 0,8 × 0,2³ = 0,0256 ; p(X = 2) = 6 × 0,8² × 0,2² = 0,1536.
3. p(X = 3) = 4 × 0,8³ × 0,2 = 0,4096 ; p(X = 4) = 0,8⁴ = 0,4096.
4. Contrôle : 0,0016 + 0,0256 + 0,1536 + 0,4096 + 0,4096 = 1 ✓.
5. E(X) = 4 × 0,8 = 3,2 graines ; V(X) = 4 × 0,8 × 0,2 = 0,64 et σ(X) = 0,8.
6. Au moins une graine germe : p(X ≥ 1) = 1 − p(X = 0) = 1 − 0,0016 = 0,9984.
7. Combien de graines faut-il semer pour que p(X ≥ 1) soit au moins 0,999 ? On veut 1 − 0,2ⁿ ≥ 0,999, soit 0,2ⁿ ≤ 0,001, soit n ln 0,2 ≤ ln 0,001. Comme ln 0,2 < 0, le sens s'inverse : n ≥ ln 0,001/ln 0,2 ≈ 4,29. Donc n = 5 (contrôle : 0,2⁵ = 0,00032 ≤ 0,001, alors que 0,2⁴ = 0,0016 > 0,001).

:::

::: piege
**Erreur : appliquer ℬ(n ; p) à des tirages sans remise.** Dans une urne de 3 boules rouges et 7 noires, on tire 3 boules l'une après l'autre sans les remettre. La probabilité d'une rouge est 3/10 au premier tirage, mais 2/9 au deuxième si la première était rouge : les épreuves ne sont ni identiques ni indépendantes, et le nombre de rouges ne suit pas une loi binomiale. Avec remise, p reste égal à 3/10 à chaque tirage et la loi binomiale s'applique.
:::

::: propriete
Si X suit ℬ(n ; p), avec q = 1 − p :
- p(X = 0) = qⁿ et p(X = n) = pⁿ ;
- E(X) = np, V(X) = npq et σ(X) = √(npq) (résultats admis) ;
- p(X ≥ 1) = 1 − qⁿ : « au moins un succès » se calcule par l'événement contraire.

Cas limite : pour trouver le plus petit n tel que 1 − qⁿ dépasse un seuil, on passe au logarithme et on inverse l'inégalité, puisque ln q < 0.
:::

::: verifie À toi : tirages avec remise
Une urne contient 2 boules rouges et 3 boules vertes. On tire une boule, on note sa couleur et on la remet, et on recommence : 3 tirages en tout. Soit X le nombre de boules rouges obtenues. Donne la loi de X, calcule p(X = 2) puis E(X).

---

Chaque tirage est une épreuve à deux issues (succès = rouge, p = 2/5 = 0,4), répétée 3 fois avec remise, donc de façon indépendante : X suit ℬ(3 ; 0,4). Alors p(X = 2) = C₃² × 0,4² × 0,6 = 3 × 0,16 × 0,6 = 0,288, et E(X) = 3 × 0,4 = 1,2 boule rouge en moyenne.
:::

::: retenir
Le nombre de succès de n épreuves identiques et indépendantes suit ℬ(n ; p) : p(X = k) = Cₙᵏ pᵏ (1 − p)ⁿ⁻ᵏ, E(X) = np et V(X) = np(1 − p).
:::

## 🎯 La loi uniforme

Une baguette de bois de 50 cm est cassée en un point choisi au hasard : tous les points se valent. Soit X la distance, en cm, entre l'extrémité gauche et le point de cassure, donc une valeur quelconque de l'intervalle [0 ; 50].
Quelle est la probabilité que la baguette casse entre 10 cm et 25 cm ? Et exactement à 20 cm ?

::: definition
Soit [a ; b] un intervalle (a < b). La fonction f définie sur [a ; b] par
$$ f(x) = 1/(b − a) $$
est la **densité** de la loi uniforme sur [a ; b]. La **probabilité uniforme** associe à tout intervalle [c ; d] inclus dans [a ; b] le nombre p([c ; d]) = ∫ de f entre c et d = (d − c)/(b − a).
On dit que X suit la **loi uniforme** sur [a ; b] si p(c ≤ X ≤ d) = (d − c)/(b − a).
:::

::: figure La densité de la loi uniforme sur [0 ; 50] est un rectangle de hauteur 1/50 : la partie de 10 à 25 a pour aire 15 × 1/50 = 0,3
<svg viewBox="0 0 340 250">
<title>Densité de la loi uniforme sur [0 ; 50] : un rectangle de hauteur 1/50 ; la partie de 10 à 25 a pour aire 0,3</title>
<path d="M30 200 L332 200" fill="none" stroke="#0f172a" stroke-width="1.8" stroke-linecap="round"/>
<path d="M40 206 L40 70" fill="none" stroke="#0f172a" stroke-width="1.8" stroke-linecap="round"/>
<text x="332" y="218" text-anchor="end" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">x</text>
<rect x="40" y="110" width="252" height="90" fill="#0f6e56" fill-opacity="0.10" stroke="none"/>
<rect x="90.4" y="110" width="75.6" height="90" fill="#b45309" fill-opacity="0.28" stroke="none"/>
<path d="M40 110 L292 110 L292 200" fill="none" stroke="#0f6e56" stroke-width="3" stroke-linejoin="round"/>
<path d="M90.4 200 L90.4 110" fill="none" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round" stroke-dasharray="4 3"/>
<path d="M166 200 L166 110" fill="none" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round" stroke-dasharray="4 3"/>
<path d="M40 200 L40 205" fill="none" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="40" y="220" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0</text>
<path d="M90.4 200 L90.4 205" fill="none" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="90.4" y="220" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">10</text>
<path d="M166 200 L166 205" fill="none" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="166" y="220" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">25</text>
<path d="M292 200 L292 205" fill="none" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="292" y="220" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">50</text>
<path d="M40 110 L36 110" fill="none" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="32" y="114" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">1/50</text>
<text x="128.2" y="160" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0,3</text>
<text x="226" y="102" text-anchor="middle" font-size="15" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">f</text>
</svg>
:::

La hauteur 1/50 est choisie pour que l'aire totale du rectangle, 50 × 1/50, vaille 1 ; la partie colorée, de largeur 15, a pour aire 15 × 1/50 = 0,3.

::: exemple La baguette

1. Sur [0 ; 50], la densité vaut f(x) = 1/50, car l'aire du rectangle doit valoir 1.
2. p(10 ≤ X ≤ 25) = ∫₁₀²⁵ (1/50) dx = (25 − 10)/50 = 0,3.
3. Pour un point isolé, p(X = 20) = ∫₂₀²⁰ f(x) dx = 0 : une valeur isolée n'a aucune probabilité.
4. Pour le complémentaire de [10 ; 25] dans [0 ; 50], p = 1 − 0,3 = 0,7.
5. Fonction de répartition : F(x) = 0 pour x < 0, F(x) = x/50 pour 0 ≤ x ≤ 50 et F(x) = 1 pour x > 50. Par exemple F(30) = 0,6 = p(X ≤ 30).

:::

::: piege
**Erreur : lire f(20) = 1/50 comme p(X = 20).** La valeur de la densité en un point est une hauteur de rectangle, pas une probabilité : p(X = 20) = 0. Seule une aire, donc un intervalle de largeur non nulle, donne une probabilité.
:::

::: propriete
Si X suit la loi uniforme sur [a ; b] :
- p(c ≤ X ≤ d) = (d − c)/(b − a) : la probabilité d'un sous-intervalle ne dépend que de sa longueur ;
- p({c}) = 0, donc inégalités strictes ou larges donnent la même probabilité ;
- pour deux intervalles sans point commun, on additionne leurs probabilités ;
- F(x) = 0 pour x < a, F(x) = (x − a)/(b − a) pour a ≤ x ≤ b et F(x) = 1 pour x > b.

Cas limite : le dénominateur est b − a, la longueur de l'intervalle total, et non b.
:::

::: verifie À toi : le facteur
Le facteur arrive à un instant X, en heures, de loi uniforme sur [9 ; 11]. Calcule p(9,5 ≤ X ≤ 10), puis p(X ≥ 10,4).

---

La densité vaut 1/(11 − 9) = 1/2. Donc p(9,5 ≤ X ≤ 10) = (10 − 9,5)/2 = 0,25. Pour p(X ≥ 10,4), l'intervalle utile est [10,4 ; 11] : p = (11 − 10,4)/2 = 0,3.
:::

::: retenir
Loi uniforme sur [a ; b] : densité 1/(b − a), p(c ≤ X ≤ d) = (d − c)/(b − a), p({c}) = 0.
:::

## ⏳ La loi exponentielle

La durée de vie X, en années, d'une batterie de drone est un nombre positif sans borne supérieure : elle peut dépasser 5 ou 10 ans, avec une probabilité de plus en plus faible.
Comment attribuer une probabilité à un intervalle de durées, par exemple entre 1 et 3 ans ?

::: definition
Soit λ un réel strictement positif. La fonction f définie sur [0 ; +∞[ par
$$ f(t) = λ e^(−λt) $$
est la **densité** de la loi exponentielle. On dit que X suit la **loi exponentielle de paramètre λ** si, pour 0 ≤ c ≤ d,
$$ p(c ≤ X ≤ d) = e^(−λc) − e^(−λd) et p(X ≥ c) = e^(−λc) $$
:::

::: figure La densité exponentielle de paramètre 0,3 décroît à partir de 0,3 ; l'aire colorée entre t = 1 et t = 3 est la probabilité p(1 ≤ X ≤ 3)
<svg viewBox="0 0 340 250">
<title>Densité exponentielle f(t) = 0,3 e^(−0,3t) ; l'aire entre t = 1 et t = 3 vaut environ 0,33</title>
<path d="M35 200 L332 200" fill="none" stroke="#0f172a" stroke-width="1.8" stroke-linecap="round"/>
<path d="M45 206 L45 36" fill="none" stroke="#0f172a" stroke-width="1.8" stroke-linecap="round"/>
<text x="332" y="218" text-anchor="end" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">t</text>
<polygon points="71.4,200 71.4,88.9 72.7,90.5 74,92.2 75.4,93.8 76.7,95.3 78,96.9 79.3,98.4 80.6,100 82,101.4 83.3,102.9 84.6,104.4 85.9,105.8 87.2,107.2 88.6,108.6 89.9,109.9 91.2,111.3 92.5,112.6 93.8,113.9 95.2,115.2 96.5,116.4 97.8,117.7 99.1,118.9 100.4,120.1 101.8,121.3 103.1,122.5 104.4,123.6 105.7,124.8 107,125.9 108.4,127 109.7,128.1 111,129.1 112.3,130.2 113.6,131.2 115,132.3 116.3,133.3 117.6,134.3 118.9,135.2 120.2,136.2 121.6,137.2 122.9,138.1 124.2,139 124.2,200" fill="#0f6e56" fill-opacity="0.22" stroke="none"/>
<path d="M45 50 L56 67.6 L67 83.2 L78 96.9 L89 109 L100 119.7 L111 129.1 L122 137.5 L133 144.8 L144 151.3 L155 157 L166 162.1 L177 166.5 L188 170.5 L199 173.9 L210 177 L221 179.7 L232 182.1 L243 184.2 L254 186 L265 187.7 L276 189.1 L287 190.4 L298 191.5 L309 192.5" fill="none" stroke="#0f6e56" stroke-width="3" stroke-linejoin="round"/>
<path d="M71.4 200 L71.4 88.9" fill="none" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round" stroke-dasharray="4 3"/>
<path d="M124.2 200 L124.2 139" fill="none" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round" stroke-dasharray="4 3"/>
<path d="M45 200 L45 205" fill="none" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="45" y="220" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0</text>
<path d="M71.4 200 L71.4 205" fill="none" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="71.4" y="220" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">1</text>
<path d="M124.2 200 L124.2 205" fill="none" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="124.2" y="220" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">3</text>
<path d="M177 200 L177 205" fill="none" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="177" y="220" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">5</text>
<path d="M309 200 L309 205" fill="none" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="309" y="220" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">10</text>
<path d="M45 50 L41 50" fill="none" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="37" y="54" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0,3</text>
<text x="97.8" y="186" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0,33</text>
<text x="190.2" y="159.2" text-anchor="middle" font-size="15" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">f</text>
<circle cx="45" cy="50" r="4" fill="#0f6e56" stroke="#0f172a" stroke-width="1"/>
</svg>
:::

La courbe est la densité f(t) = 0,3 e^(−0,3t) : elle part de λ = 0,3 en t = 0 et décroît ; l'aire colorée entre t = 1 et t = 3 est la probabilité p(1 ≤ X ≤ 3), environ 0,33.

::: exemple La batterie

1. Pour un intervalle, l'intégrale de λe^(−λx) entre c et d vaut [−e^(−λx)] pris entre c et d = e^(−λc) − e^(−λd). De plus l'intégrale de f entre 0 et x vaut 1 − e^(−λx), qui tend vers 1 quand x tend vers +∞ : l'aire totale vaut bien 1.
2. Avec λ = 0,3 : p(X ≥ 2) = e^(−0,6) ≈ 0,549.
3. p(1 ≤ X ≤ 3) = e^(−0,3) − e^(−0,9) ≈ 0,7408 − 0,4066 = 0,3342.
4. p(X = 2) = 0 ; p(X ≤ 2) = 1 − p(X ≥ 2) = 1 − e^(−0,6) ≈ 0,451.
5. Fonction de répartition : F(x) = 0 pour x < 0 et F(x) = 1 − e^(−0,3x) pour x ≥ 0.
6. Retrouver λ : pour une batterie d'un autre modèle, la courbe de F passe par le point (2 ; 0,5). Alors 1 − e^(−2λ) = 0,5, soit e^(−2λ) = 0,5, soit −2λ = ln 0,5 = −ln 2, donc λ = ln 2/2 ≈ 0,35.

:::

::: piege
**Erreur : écrire p(X ≥ c) = 1 − e^(−λc).** On confond « au moins c » et « au plus c ». Un contrôle de bon sens : plus c est grand, moins il est probable de dépasser c, donc p(X ≥ c) doit diminuer ; e^(−λc) décroît bien, alors que 1 − e^(−λc) croît. Ici p(X ≥ 2) = e^(−0,6) ≈ 0,549 et p(X ≤ 2) = 1 − e^(−0,6) ≈ 0,451.
:::

::: propriete
Si X suit la loi exponentielle de paramètre λ, pour 0 ≤ c ≤ d :
- p(X ≥ c) = e^(−λc) et p(X ≤ c) = 1 − e^(−λc) ;
- p(c ≤ X ≤ d) = e^(−λc) − e^(−λd), et p(X = c) = 0 ;
- F(x) = 0 pour x < 0 et F(x) = 1 − e^(−λx) pour x ≥ 0, avec F(x) qui tend vers 1 quand x tend vers +∞ ;
- si p(X ≥ t₀) = q, alors λ = −ln q/t₀ ; si la courbe de F passe par (x₀ ; y₀), alors λ = −ln(1 − y₀)/x₀.

Cas limite : p(X < 0) = 0, donc F(x) = 0 pour x < 0 : la durée est toujours positive. Une densité n'est pas une probabilité : f(0) = λ peut dépasser 1 (pour λ = 2, f(0) = 2), seule l'aire totale doit valoir 1.
:::

::: verifie À toi : retrouver le paramètre
X suit la loi exponentielle de paramètre λ et p(X ≥ 3) = 1/8. Détermine λ, puis calcule p(X ≥ 1).

---

On écrit e^(−3λ) = 1/8, donc −3λ = ln(1/8) = −3 ln 2, d'où λ = ln 2. Alors p(X ≥ 1) = e^(−ln 2) = 1/2. Contrôle : e^(−3λ) = (e^(−λ))³ = (1/2)³ = 1/8 = p(X ≥ 3) ✓.
:::

::: retenir
Loi exponentielle de paramètre λ : p(X ≥ c) = e^(−λc), p(c ≤ X ≤ d) = e^(−λc) − e^(−λd), F(x) = 1 − e^(−λx) pour x ≥ 0.
:::

> 🏆 Porte franchie, héros : tu transformes un hasard en nombres, tu en lis la loi, la moyenne et l'écart, et tu passes des valeurs isolées (loi binomiale) aux durées continues (uniforme, exponentielle). Au prochain chapitre, les statistiques décrivent des données réelles avec les mêmes outils de moyenne et de dispersion.
