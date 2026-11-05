# ⚔️ Variables aléatoires réelles — du hasard aux nombres

> 💡 «Un jeu de hasard n'a plus de secret quand on sait en prédire la moyenne et l'écart.»

Ce chapitre transforme les résultats d'une expérience aléatoire en nombres (un gain, un nombre de pièces défectueuses, une durée) pour en calculer la loi, la moyenne et la dispersion. Huit notions : variable aléatoire et loi, fonction de répartition, espérance, variance et écart-type, loi binomiale, variable continue et densité, loi uniforme, loi exponentielle. Tu réutilises les probabilités conditionnelles, l'indépendance et les combinaisons Cₙᵖ du chapitre précédent, puis les intégrales et l'exponentielle pour les lois continues.

## 🎲 Variable aléatoire et loi de probabilité

Un atelier contrôle un lot de 6 pièces dont 2 sont défectueuses. Le contrôleur en prélève 2 au hasard, d'un seul coup.
Ce qui l'intéresse n'est pas le tirage lui-même, mais un nombre : combien de pièces défectueuses a-t-il en main ? Quelles valeurs ce nombre peut-il prendre, et avec quelle probabilité ?

::: definition
Soit Ω l'univers fini d'une expérience aléatoire. Une **variable aléatoire réelle** X est une application X : Ω → ℝ qui associe un nombre à chaque issue. On note X(Ω) l'ensemble de ses valeurs, et (X = x) l'événement formé des issues dont l'image est x.
La **loi de probabilité** de X associe à chaque valeur xᵢ le nombre pᵢ = p(X = xᵢ). Si X(Ω) = {x₁, …, xₙ} est fini, X est dite **discrète**.
:::

| xᵢ | x₁ | x₂ | … | xₙ | Total |
| --- | --- | --- | --- | --- | --- |
| pᵢ = p(X = xᵢ) | p₁ | p₂ | … | pₙ | 1 |

Le tableau range les valeurs et leurs probabilités côte à côte ; la case « Total » rappelle que les événements (X = xᵢ) couvrent tous les résultats sans se recouvrir, donc que p₁ + p₂ + … + pₙ = 1.

::: exemple Le lot de six pièces

1. Le tirage est simultané : card Ω = C₆² = 15 tirages équiprobables, car on choisit une partie de 2 pièces parmi 6.
2. X compte les pièces défectueuses parmi les 2 prélevées, donc X(Ω) = {0 ; 1 ; 2}.
3. (X = 0) : 2 pièces bonnes parmi les 4 bonnes, soit C₄² = 6 tirages, donc p(X = 0) = 6/15.
4. (X = 1) : 1 défectueuse parmi 2 et 1 bonne parmi 4, soit 2 × 4 = 8 tirages, donc p(X = 1) = 8/15.
5. (X = 2) : les 2 défectueuses, soit C₂² = 1 tirage, donc p(X = 2) = 1/15.
6. Contrôle : 6/15 + 8/15 + 1/15 = 15/15 = 1 ✓, la loi est complète.

:::

::: piege
**Erreur : croire que les valeurs de X sont équiprobables.** On voit trois valeurs, 0, 1 et 2, et on écrit 1/3 pour chacune. Mais 6, 8 et 1 tirages mènent à ces valeurs : elles n'ont pas la même chance. Une probabilité se calcule en comptant les issues de l'événement (X = xᵢ), jamais en comptant les valeurs.
:::

::: propriete
Pour une variable discrète X de valeurs x₁, …, xₙ :
- 0 ≤ pᵢ ≤ 1 pour chaque i, et p₁ + p₂ + … + pₙ = 1 ;
- si plusieurs issues ont la même image x, on additionne leurs probabilités pour obtenir p(X = x).

Cas limite : si X ne prend qu'une seule valeur, cette valeur a la probabilité 1.
:::

::: verifie À toi : les ampoules
Une boîte contient 5 ampoules dont 2 sont grillées. On en prélève 2 simultanément ; Y est le nombre d'ampoules grillées obtenues. Donne la loi de Y.

---

Le tirage simultané donne card Ω = C₅² = 10 tirages équiprobables. (Y = 0) : 2 bonnes parmi 3, C₃² = 3 tirages, soit 3/10. (Y = 1) : 2 × 3 = 6 tirages, soit 6/10. (Y = 2) : 1 tirage, soit 1/10. Contrôle : 3/10 + 6/10 + 1/10 = 1 ✓. On compte les tirages de chaque événement, pas les valeurs.
:::

::: retenir
Une variable aléatoire donne un nombre à chaque issue ; sa loi est le tableau des p(X = xᵢ), dont la somme vaut 1.
:::

## 📈 La fonction de répartition

À la kermesse, un sac contient 10 billes : 5 bleues, 3 vertes et 2 rouges. On tire une bille : bleue, on gagne 1 dinar ; verte, on gagne 4 dinars ; rouge, on perd 6 dinars. Soit X le gain algébrique : sa loi est donnée par le tableau suivant.

| xᵢ | −6 | 1 | 4 |
| --- | --- | --- | --- |
| p(X = xᵢ) | 0,2 | 0,5 | 0,3 |

Quelle est la probabilité de gagner au plus 3 dinars ? Plutôt que de refaire une somme à chaque question, existe-t-il une fonction qui donne d'un coup p(X ≤ x) pour tout réel x ?

::: definition
La **fonction de répartition** de X est la fonction F définie sur ℝ par
$$ F(x) = p(X ≤ x) $$
Elle cumule les probabilités des valeurs inférieures ou égales à x.
:::

::: figure La fonction de répartition du gain est un escalier : elle monte de la probabilité de chaque valeur en passant par cette valeur, et la marche en x = 1 a pour hauteur 0,5
<svg viewBox="0 0 340 250">
<title>Fonction de répartition du gain : marches en −6, 1 et 4, de hauteurs 0,2 ; 0,5 et 0,3</title>
<path d="M20 200 L324 200" fill="none" stroke="#0f172a" stroke-width="1.8" stroke-linecap="round"/>
<path d="M190 206 L190 32" fill="none" stroke="#0f172a" stroke-width="1.8" stroke-linecap="round"/>
<text x="324" y="218" text-anchor="end" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">x</text>
<text x="194" y="28" text-anchor="start" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">F(x)</text>
<path d="M30 200 L70 200" fill="none" stroke="#0f6e56" stroke-width="3" stroke-linecap="round"/>
<path d="M70 170 L210 170" fill="none" stroke="#0f6e56" stroke-width="3" stroke-linecap="round"/>
<path d="M210 95 L270 95" fill="none" stroke="#0f6e56" stroke-width="3" stroke-linecap="round"/>
<path d="M270 50 L310 50" fill="none" stroke="#0f6e56" stroke-width="3" stroke-linecap="round"/>
<circle cx="70" cy="200" r="4" fill="#ffffff" stroke="#0f6e56" stroke-width="2"/>
<circle cx="70" cy="170" r="4" fill="#0f6e56" stroke="#0f172a" stroke-width="1"/>
<circle cx="210" cy="170" r="4" fill="#ffffff" stroke="#0f6e56" stroke-width="2"/>
<circle cx="210" cy="95" r="4" fill="#0f6e56" stroke="#0f172a" stroke-width="1"/>
<circle cx="270" cy="95" r="4" fill="#ffffff" stroke="#0f6e56" stroke-width="2"/>
<circle cx="270" cy="50" r="4" fill="#0f6e56" stroke="#0f172a" stroke-width="1"/>
<path d="M190 170 L186 170" fill="none" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="182" y="166" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0,2</text>
<path d="M190 95 L186 95" fill="none" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="182" y="91" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0,7</text>
<path d="M190 50 L186 50" fill="none" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="182" y="46" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">1</text>
<path d="M70 200 L70 205" fill="none" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<path d="M210 200 L210 205" fill="none" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<path d="M270 200 L270 205" fill="none" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="70" y="220" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">−6</text>
<text x="210" y="220" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">1</text>
<text x="270" y="220" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">4</text>
<path d="M221 170 L221 95" fill="none" stroke="#b45309" stroke-width="2" stroke-linecap="round"/>
<text x="227" y="136.5" text-anchor="start" font-size="13" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0,5</text>
</svg>
:::

Sur la figure, un point plein marque la valeur de F en une marche, un point creux la valeur qui n'est pas atteinte : la marche en x = 1 monte de 0,2 à 0,7, soit 0,5 = p(X = 1).

::: exemple Le gain de la kermesse

1. Pour x < −6, aucune valeur n'est inférieure ou égale à x : F(x) = 0.
2. Pour −6 ≤ x < 1, seule la valeur −6 compte : F(x) = 0,2.
3. Pour 1 ≤ x < 4, les valeurs −6 et 1 comptent : F(x) = 0,2 + 0,5 = 0,7.
4. Pour x ≥ 4, toutes les valeurs comptent : F(x) = 0,2 + 0,5 + 0,3 = 1.
5. Lecture : p(X ≤ 3) = F(3) = 0,7 ; p(X > 1) = 1 − F(1) = 1 − 0,7 = 0,3 ; p(−6 < X ≤ 4) = F(4) − F(−6) = 1 − 0,2 = 0,8.

:::

::: piege
**Erreur : lire F(1) comme p(X = 1).** Comme 1 est une valeur du tableau, on est tenté de lire 0,7 comme la probabilité de gagner exactement 1 dinar. Or F(1) = p(X ≤ 1) = 0,2 + 0,5 : c'est un cumul. La probabilité de la valeur 1 est la hauteur de la marche, F(1) − F(−6) = 0,7 − 0,2 = 0,5.
:::

::: propriete
Pour une variable discrète de valeurs x₁ < x₂ < … < xₙ :
- F est en escalier, croissante, avec 0 ≤ F ≤ 1 ; F(x) = 0 avant x₁ et F(x) = 1 à partir de xₙ ;
- p(X > x) = 1 − F(x) et p(a < X ≤ b) = F(b) − F(a) pour a < b ;
- p₁ = F(x₁) et, pour i ≥ 2, pᵢ = F(xᵢ) − F(xᵢ₋₁) : la probabilité de xᵢ est la hauteur de la marche.

Cas limite : en une valeur xᵢ, F est continue à droite, c'est-à-dire que F(xᵢ) est le haut de la marche, pas le bas.
:::

::: verifie À toi : lire F sur les ampoules
Y a pour valeurs 0, 1 et 2 avec les probabilités 0,3 ; 0,6 et 0,1. Calcule F(1,5) et p(Y > 0).

---

Le réel 1,5 est dans [1 ; 2[ : seules les valeurs 0 et 1 sont inférieures ou égales à 1,5, donc F(1,5) = 0,3 + 0,6 = 0,9. Pour p(Y > 0), on passe au contraire : p(Y > 0) = 1 − F(0) = 1 − 0,3 = 0,7, ce qui est bien 0,6 + 0,1.
:::

::: retenir
F(x) = p(X ≤ x) cumule les probabilités ; p(X > x) = 1 − F(x) et p(a < X ≤ b) = F(b) − F(a).
:::

## 💰 L'espérance mathématique

Reprenons le jeu de la kermesse. Si 1 000 joueurs tentaient leur chance, on s'attendrait à peu près à 500 billes bleues (+1), 300 vertes (+4) et 200 rouges (−6). Ces effectifs sont une estimation, pas un résultat certain : ils donnent un gain total d'environ 500 × 1 + 300 × 4 + 200 × (−6) = 500 dinars, soit 0,5 dinar par partie.
Ce gain moyen se lit-il directement sur la loi ?

::: definition
L'**espérance mathématique** de X, notée E(X), est la moyenne des valeurs de X pondérées par leurs probabilités :
$$ E(X) = p₁x₁ + p₂x₂ + … + pₙxₙ = Σ pᵢxᵢ $$
:::

::: exemple Le jeu de la kermesse, puis un jeu équilibré

1. Chaque valeur est pondérée par sa probabilité : E(X) = (−6) × 0,2 + 1 × 0,5 + 4 × 0,3.
2. On calcule : E(X) = −1,2 + 0,5 + 1,2 = 0,5, soit +0,5 dinar par partie en moyenne.
3. E(X) > 0 : le jeu est favorable au joueur.
4. Autre loi : Z vaut −2, 0 et 3 avec les probabilités 0,3 ; 0,5 et 0,2. Alors E(Z) = −0,6 + 0 + 0,6 = 0 : en moyenne, ni gain ni perte.

:::

::: piege
**Erreur : faire la moyenne simple des valeurs.** On calcule (−6 + 1 + 4)/3 = −1/3 et on conclut que le jeu est perdant. Cette moyenne ignore que la bille bleue sort cinq fois sur dix et la rouge deux fois sur dix. Chaque valeur compte avec son poids, et ici le signe de la réponse est même inversé : +0,5 contre −1/3.
:::

::: propriete
Si X est le gain algébrique d'un jeu (gain moins mise éventuelle) :
- le jeu est **favorable** si E(X) > 0, **défavorable** si E(X) < 0 et **équitable** si E(X) = 0 ;
- E(X) s'exprime dans la même unité que X.

Cas limite : E(X) n'est pas forcément une valeur que X peut prendre. Ici 0,5 n'est pas un gain possible : c'est une moyenne sur un grand nombre de parties.
:::

::: verifie À toi : la loterie à 2 dinars
Pour jouer, on paie 2 dinars. On tire une carte : avec la probabilité 0,7 elle ne rapporte rien, avec la probabilité 0,2 elle rapporte 5 dinars et avec la probabilité 0,1 elle rapporte 10 dinars. Soit X le gain net (gain moins mise). Donne la loi de X, calcule E(X) et conclus.

---

Le gain net est le gain moins la mise : X vaut −2, 3 ou 8 avec les probabilités 0,7 ; 0,2 et 0,1 (somme 1 ✓). Alors E(X) = (−2) × 0,7 + 3 × 0,2 + 8 × 0,1 = −1,4 + 0,6 + 0,8 = 0. Le jeu est équitable : la mise est déjà soustraite de chaque valeur, et chaque valeur est pondérée par sa probabilité.
:::

::: retenir
E(X) = Σ pᵢxᵢ est la moyenne pondérée par les probabilités : jeu favorable si E(X) > 0, équitable si E(X) = 0, défavorable si E(X) < 0.
:::

## 📏 Variance et écart-type

Deux jeux ont la même espérance, 0,5 dinar. Le jeu de la kermesse donne −6, 1 ou 4. Un jeu B donne −1 ou 2 dinars avec la probabilité 0,5 chacun (E = −0,5 + 1 = 0,5). Le premier fait osciller le gain bien plus que le second, et la moyenne n'en dit rien.
Comment mesurer l'écart typique des valeurs autour de E(X) ?

::: definition
La **variance** de X est la moyenne des carrés des écarts à l'espérance, et l'**écart-type** en est la racine carrée :
$$ V(X) = Σ pᵢ (xᵢ − E(X))² et σ(X) = √V(X) $$
Une formule pratique donne le même résultat :
$$ V(X) = E(X²) − (E(X))² avec E(X²) = Σ pᵢxᵢ² $$
:::

::: exemple Les deux jeux, même moyenne

1. Par la définition, avec E(X) = 0,5 : les écarts au carré sont (−6 − 0,5)² = 42,25 ; (1 − 0,5)² = 0,25 ; (4 − 0,5)² = 12,25.
2. On pondère : V(X) = 0,2 × 42,25 + 0,5 × 0,25 + 0,3 × 12,25 = 8,45 + 0,125 + 3,675 = 12,25.
3. Par la formule pratique : E(X²) = 0,2 × 36 + 0,5 × 1 + 0,3 × 16 = 7,2 + 0,5 + 4,8 = 12,5, puis V(X) = 12,5 − 0,5² = 12,25 ✓, le même résultat.
4. L'écart-type vaut σ(X) = √12,25 = 3,5 dinars.
5. Pour le jeu B : E(B²) = 0,5 × 1 + 0,5 × 4 = 2,5, donc V = 2,5 − 0,25 = 2,25 et σ = 1,5 dinar. Même moyenne, mais un écart-type de 1,5 contre 3,5 : le jeu B est bien moins risqué.

:::

::: piege
**Erreur : oublier de mettre l'espérance au carré.** Avec E(X²) = 12,5 et E(X) = 0,5, on écrit V(X) = 12,5 − 0,5 = 12, ou même on garde 12,5. Le bon terme à retrancher est (E(X))² = 0,25, ce qui donne 12,25. Un contrôle : une variance n'est jamais négative.
:::

::: propriete
- V(X) ≥ 0 et σ(X) = √V(X) s'exprime dans la même unité que X ;
- plus σ(X) est grand, plus les valeurs de X s'écartent de l'espérance ;
- V(X) = E(X²) − (E(X))².

Cas limite : si X ne prend qu'une seule valeur, V(X) = 0, car cette valeur est égale à son espérance.
:::

::: verifie À toi : variance d'un petit jeu
X prend les valeurs 1, 2 et 3 avec les probabilités 0,2 ; 0,5 et 0,3. Calcule E(X), V(X) et σ(X).

---

E(X) = 1 × 0,2 + 2 × 0,5 + 3 × 0,3 = 0,2 + 1 + 0,9 = 2,1. Ensuite E(X²) = 1 × 0,2 + 4 × 0,5 + 9 × 0,3 = 0,2 + 2 + 2,7 = 4,9. La formule pratique retranche le carré de l'espérance : V(X) = 4,9 − 2,1² = 4,9 − 4,41 = 0,49, donc σ(X) = √0,49 = 0,7.
:::

::: retenir
V(X) = E(X²) − (E(X))² et σ(X) = √V(X) : plus σ est grand, plus les valeurs s'éloignent de l'espérance.
:::

## 🔁 La loi binomiale

Au basket, une joueuse réussit chaque lancer franc avec la probabilité 0,7, et ses lancers sont indépendants les uns des autres. Elle en tente 3. Soit X le nombre de lancers réussis.
Quelle est la loi de X, et combien de lancers réussit-elle en moyenne ?

::: definition
Une **épreuve de Bernoulli** a deux issues : le **succès**, de probabilité p, et l'**échec**, de probabilité 1 − p. Un **schéma de Bernoulli** répète n fois (n > 1) la même épreuve, les épreuves étant deux à deux indépendantes.
Le nombre X de succès suit la **loi binomiale** de paramètres n et p, notée ℬ(n ; p) : pour k ∈ {0 ; 1 ; … ; n},
$$ p(X = k) = Cₙᵏ × pᵏ × (1 − p)ⁿ⁻ᵏ $$
:::

::: figure La loi binomiale ℬ(3 ; 0,7) en bâtons : la hauteur de chaque bâton est p(X = k), et les quatre hauteurs ont pour somme 1
<svg viewBox="0 0 340 250">
<title>Loi binomiale B(3 ; 0,7) : bâtons de hauteurs 0,027 ; 0,189 ; 0,441 et 0,343</title>
<path d="M40 200 L320 200" fill="none" stroke="#0f172a" stroke-width="1.8" stroke-linecap="round"/>
<rect x="48" y="191.4" width="44" height="8.6" fill="#0f6e56" fill-opacity="0.28" stroke="#0f6e56" stroke-width="2.2"/>
<text x="70" y="184.4" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0,027</text>
<text x="70" y="220" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0</text>
<rect x="118" y="139.5" width="44" height="60.5" fill="#0f6e56" fill-opacity="0.28" stroke="#0f6e56" stroke-width="2.2"/>
<text x="140" y="132.5" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0,189</text>
<text x="140" y="220" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">1</text>
<rect x="188" y="58.9" width="44" height="141.1" fill="#0f6e56" fill-opacity="0.28" stroke="#0f6e56" stroke-width="2.2"/>
<text x="210" y="51.9" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0,441</text>
<text x="210" y="220" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">2</text>
<rect x="258" y="90.2" width="44" height="109.8" fill="#0f6e56" fill-opacity="0.28" stroke="#0f6e56" stroke-width="2.2"/>
<text x="280" y="83.2" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0,343</text>
<text x="280" y="220" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">3</text>
<text x="325" y="220" text-anchor="end" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">k</text>
</svg>
:::

Chaque bâton représente une valeur k de X et sa hauteur est p(X = k) ; le plus haut est en k = 2, c'est-à-dire que réussir 2 lancers sur 3 est le cas le plus probable.

::: exemple Les trois lancers francs

1. Un lancer est une épreuve de Bernoulli (succès = réussi, p = 0,7) répétée 3 fois de façon indépendante : X suit ℬ(3 ; 0,7), et X(Ω) = {0 ; 1 ; 2 ; 3}.
2. Une suite de lancers avec k succès a la probabilité 0,7ᵏ × 0,3³⁻ᵏ, et il y en a C₃ᵏ (on choisit les positions des succès).
3. p(X = 0) = 0,3³ = 0,027 ; p(X = 1) = 3 × 0,7 × 0,3² = 0,189 ; p(X = 2) = 3 × 0,7² × 0,3 = 0,441 ; p(X = 3) = 0,7³ = 0,343.
4. Contrôle : 0,027 + 0,189 + 0,441 + 0,343 = 1 ✓.
5. E(X) = 3 × 0,7 = 2,1 et V(X) = 3 × 0,7 × 0,3 = 0,63. Vérification de E avec la loi : 0 + 0,189 + 2 × 0,441 + 3 × 0,343 = 0,189 + 0,882 + 1,029 = 2,1 ✓.

:::

::: piege
**Erreur : appliquer ℬ(n ; p) à des tirages sans remise.** Dans une urne de 3 boules rouges et 7 noires, on tire 3 boules l'une après l'autre sans les remettre. La probabilité d'une rouge est 3/10 au premier tirage, mais 2/9 au deuxième si la première était rouge : les épreuves ne sont ni identiques ni indépendantes, et le nombre de rouges ne suit pas une loi binomiale. Avec remise, p reste égal à 3/10 à chaque tirage et la loi binomiale s'applique.
:::

::: propriete
Si X suit ℬ(n ; p), avec q = 1 − p :
- p(X = k) = Cₙᵏ pᵏ qⁿ⁻ᵏ pour k de 0 à n, avec p(X = 0) = qⁿ et p(X = n) = pⁿ ;
- E(X) = np, V(X) = npq et σ(X) = √(npq).

Cas limite : « au moins un succès » se calcule par le contraire, p(X ≥ 1) = 1 − p(X = 0) = 1 − qⁿ. Ici 1 − 0,3³ = 0,973.
:::

::: verifie À toi : le contrôle de production
Une machine produit des pièces dont 10 % sont défectueuses, de façon indépendante. On prélève 4 pièces. Quelle est la probabilité d'obtenir exactement une pièce défectueuse, et combien en obtient-on en moyenne ?

---

Prélever une pièce est une épreuve de Bernoulli (succès = pièce défectueuse, p = 0,1), répétée 4 fois de façon indépendante : X suit ℬ(4 ; 0,1). Alors p(X = 1) = C₄¹ × 0,1 × 0,9³ = 4 × 0,1 × 0,729 = 0,2916, et E(X) = np = 4 × 0,1 = 0,4 pièce défectueuse en moyenne.
:::

::: retenir
Le nombre de succès de n épreuves de Bernoulli indépendantes suit ℬ(n ; p) : p(X = k) = Cₙᵏ pᵏ (1 − p)ⁿ⁻ᵏ, E(X) = np et V(X) = np(1 − p).
:::

## 🌊 Variable continue, fonction de répartition et densité

Un service d'urgence mesure la durée X d'un appel, en minutes. Elle est comprise entre 0 et 2 et peut prendre n'importe quelle valeur de l'intervalle [0 ; 2] : 1,2 minute, 1,2037 minute… On sait que p(X ≤ x) = x²/4 pour x entre 0 et 2.
Quelle est la probabilité qu'un appel dure exactement 1 minute ? Et qu'il dure entre 0,5 et 1,5 minute ?

::: definition
Une variable aléatoire est **continue** lorsque X(Ω) est un intervalle I non réduit à un point. Alors p(X = a) = 0 pour tout réel a, et on la décrit par sa fonction de répartition F(x) = p(X ≤ x), qui est croissante et continue, avec F = 0 à gauche de I et F = 1 à droite.
La dérivée f = F′ est la **densité de probabilité** de X.
:::

::: figure La densité f(x) = x/2 sur [0 ; 2] : la probabilité de l'intervalle [0,5 ; 1,5] est l'aire colorée sous la courbe, ici 0,5
<svg viewBox="0 0 340 250">
<title>Densité f(x) = x/2 sur [0 ; 2] ; l'aire sous la courbe entre 0,5 et 1,5 vaut 0,5</title>
<path d="M40 200 L330 200" fill="none" stroke="#0f172a" stroke-width="1.8" stroke-linecap="round"/>
<path d="M50 206 L50 36" fill="none" stroke="#0f172a" stroke-width="1.8" stroke-linecap="round"/>
<text x="330" y="218" text-anchor="end" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">x</text>
<polygon points="105,200 105,162.5 215,87.5 215,200" fill="#0f6e56" fill-opacity="0.22" stroke="none"/>
<path d="M50 200 L270 50 L270 200" fill="none" stroke="#0f6e56" stroke-width="3" stroke-linejoin="round"/>
<path d="M105 200 L105 162.5" fill="none" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round" stroke-dasharray="4 3"/>
<path d="M215 200 L215 87.5" fill="none" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round" stroke-dasharray="4 3"/>
<path d="M105 200 L105 205" fill="none" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="105" y="220" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0,5</text>
<path d="M160 200 L160 205" fill="none" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="160" y="220" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">1</text>
<path d="M215 200 L215 205" fill="none" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="215" y="220" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">1,5</text>
<path d="M270 200 L270 205" fill="none" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="270" y="220" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">2</text>
<path d="M50 125 L46 125" fill="none" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="42" y="129" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0,5</text>
<path d="M50 50 L46 50" fill="none" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="42" y="54" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">1</text>
<text x="160" y="178" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">aire 0,5</text>
<text x="245.8" y="60.5" text-anchor="end" font-size="15" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">f</text>
<circle cx="270" cy="50" r="4" fill="#0f6e56" stroke="#0f172a" stroke-width="1"/>
</svg>
:::

La probabilité d'un intervalle est une aire : l'aire colorée sous la courbe de f entre 0,5 et 1,5 est la probabilité p(0,5 ≤ X ≤ 1,5).

::: exemple La durée d'un appel

1. X est continue sur [0 ; 2], donc p(X = 1) = 0 : une valeur isolée n'a aucune probabilité.
2. Pour un intervalle, on utilise F : p(0,5 ≤ X ≤ 1,5) = F(1,5) − F(0,5) = 2,25/4 − 0,25/4 = 2/4 = 0,5.
3. La densité est la dérivée de F : f(x) = F′(x) = x/2 sur [0 ; 2], et f(x) = 0 ailleurs.
4. Par l'intégrale de la densité entre 0,5 et 1,5 : [x²/4] pris entre 0,5 et 1,5 vaut 0,5625 − 0,0625 = 0,5 ✓, et sur tout l'intervalle ∫₀² (x/2) dx = [x²/4]₀² = 1 ✓.

:::

::: piege
**Erreur : lire f(1) = 0,5 comme p(X = 1).** La valeur de la densité en 1 est une hauteur de la courbe, pas une probabilité : p(X = 1) = 0. Seule l'aire sous la courbe, donc une intégrale sur un intervalle, donne une probabilité. Une densité peut même dépasser 1 (par exemple 2 sur un intervalle de longueur 0,5) sans aucune contradiction.
:::

::: propriete
Soit X continue, de fonction de répartition F et de densité f :
- f(x) ≥ 0 pour tout x, et p(s ≤ X ≤ t) = ∫ₛᵗ f(x) dx = F(t) − F(s) ;
- si X(Ω) = [a ; b], alors ∫ₐᵇ f(x) dx = 1 ;
- p(X < a) = p(X ≤ a) et p(X > a) = 1 − F(a) : inégalités strictes ou larges, c'est pareil.

Cas limite : p(X = a) = 0 ne rend pas l'événement impossible, l'appel dure bien une durée précise.
:::

::: verifie À toi : une autre durée
X est continue sur [0 ; 3], avec F(x) = x²/9 sur cet intervalle. Calcule p(1 ≤ X ≤ 2), puis donne la densité de X.

---

Pour un intervalle, p(1 ≤ X ≤ 2) = F(2) − F(1) = 4/9 − 1/9 = 3/9 = 1/3. La densité est la dérivée de F : f(x) = 2x/9 sur [0 ; 3]. Contrôle : ∫₀³ (2x/9) dx = [x²/9]₀³ = 1 ✓.
:::

::: retenir
Pour une variable continue, p(X = a) = 0 et p(s ≤ X ≤ t) = F(t) − F(s) = ∫ₛᵗ f(x) dx, avec f = F′.
:::

## 🕒 La loi uniforme

Un tramway passe toutes les 12 minutes. Un voyageur arrive à la station à un instant quelconque, sans connaître l'horaire : tous les instants du cycle de 12 minutes se valent. Soit X son temps d'attente, en minutes.
Quelle est la probabilité d'attendre moins de 3 minutes, et combien attend-il en moyenne ?

::: definition
X suit la **loi uniforme** sur [a ; b] (a < b) si sa densité est constante sur [a ; b] et nulle ailleurs :
$$ f(x) = 1/(b − a) pour a ≤ x ≤ b $$
Alors E(X) = (a + b)/2 et V(X) = (b − a)²/12, et p(s ≤ X ≤ t) = (t − s)/(b − a) pour a ≤ s ≤ t ≤ b.
:::

::: figure La densité de la loi uniforme sur [0 ; 12] est un rectangle de hauteur 1/12 : la partie de 0 à 3 a pour aire 3 × 1/12 = 0,25
<svg viewBox="0 0 340 250">
<title>Densité de la loi uniforme sur [0 ; 12] : un rectangle de hauteur 1/12 ; la partie de 0 à 3 a pour aire 0,25</title>
<path d="M30 200 L332 200" fill="none" stroke="#0f172a" stroke-width="1.8" stroke-linecap="round"/>
<path d="M40 206 L40 70" fill="none" stroke="#0f172a" stroke-width="1.8" stroke-linecap="round"/>
<text x="332" y="218" text-anchor="end" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">x</text>
<rect x="40" y="110" width="252" height="90" fill="#0f6e56" fill-opacity="0.10" stroke="none"/>
<rect x="40" y="110" width="63" height="90" fill="#b45309" fill-opacity="0.28" stroke="none"/>
<path d="M40 110 L292 110 L292 200" fill="none" stroke="#0f6e56" stroke-width="3" stroke-linejoin="round"/>
<path d="M103 200 L103 110" fill="none" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round" stroke-dasharray="4 3"/>
<path d="M40 200 L40 205" fill="none" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="40" y="220" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0</text>
<path d="M103 200 L103 205" fill="none" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="103" y="220" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">3</text>
<path d="M166 200 L166 205" fill="none" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="166" y="220" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">6</text>
<path d="M229 200 L229 205" fill="none" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="229" y="220" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">9</text>
<path d="M292 200 L292 205" fill="none" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="292" y="220" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">12</text>
<path d="M40 110 L36 110" fill="none" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="32" y="114" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">1/12</text>
<text x="71.5" y="162" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0,25</text>
<text x="208" y="102" text-anchor="middle" font-size="15" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">f</text>
</svg>
:::

La hauteur 1/12 est choisie pour que l'aire totale du rectangle, 12 × 1/12, vaille 1 ; la partie colorée, de largeur 3, a pour aire 0,25.

::: exemple Le tramway, puis un intervalle quelconque

1. Sur [0 ; 12], la densité vaut f(x) = 1/12, car l'aire du rectangle doit valoir 1.
2. p(X ≤ 3) = (3 − 0)/12 = 0,25, c'est l'aire du rectangle de largeur 3 et de hauteur 1/12.
3. E(X) = (0 + 12)/2 = 6 minutes, V(X) = 12²/12 = 12 et σ(X) = √12 ≈ 3,46 minutes.
4. Sur [2 ; 8], la densité vaut 1/6 : p(3 ≤ X ≤ 4,5) = (4,5 − 3)/6 = 0,25, E(X) = (2 + 8)/2 = 5 et V(X) = 6²/12 = 3.

:::

::: piege
**Erreur : confondre le milieu et la demi-largeur.** On écrit E(X) = (b − a)/2, ce qui donne 3 sur [2 ; 8] au lieu de 5. L'erreur tente parce que sur [0 ; 12] les deux formules donnent 6. L'espérance est le milieu de l'intervalle, (a + b)/2 ; de même V(X) = (b − a)²/12, pas (b − a)/12.
:::

::: propriete
Si X suit la loi uniforme sur [a ; b] :
- la probabilité d'un sous-intervalle ne dépend que de sa longueur : (longueur)/(b − a) ;
- la fonction de répartition vaut F(x) = 0 pour x < a, F(x) = (x − a)/(b − a) pour a ≤ x ≤ b, et F(x) = 1 pour x > b ;
- E(X) = (a + b)/2 et V(X) = (b − a)²/12.

Cas limite : un sous-intervalle réduit à un point a pour probabilité 0, comme pour toute loi continue.
:::

::: verifie À toi : le délai de livraison
Le délai X d'une livraison, en minutes, suit la loi uniforme sur [20 ; 30]. Calcule p(X > 27) et E(X).

---

La densité vaut 1/(30 − 20) = 1/10. Donc p(X > 27) = p(27 ≤ X ≤ 30) = (30 − 27)/10 = 0,3. L'espérance est le milieu de l'intervalle : E(X) = (20 + 30)/2 = 25 minutes.
:::

::: retenir
Loi uniforme sur [a ; b] : densité 1/(b − a), p(s ≤ X ≤ t) = (t − s)/(b − a), E(X) = (a + b)/2 et V(X) = (b − a)²/12.
:::

## ⏳ La loi exponentielle

Un capteur de station météo a une durée de vie moyenne de 4 ans. Contrairement au tramway, rien ne borne cette durée : elle peut dépasser 10 ou 20 ans, avec une probabilité de plus en plus faible. Soit X cette durée, en années.
Quelle est la probabilité que le capteur dépasse 2 ans ? Et s'il a déjà fonctionné 4 ans, a-t-il moins de chances de durer encore 2 ans ?

::: definition
X suit la **loi exponentielle** de paramètre λ > 0 si sa densité est
$$ f(t) = λ e^(−λt) pour t ≥ 0, et f(t) = 0 pour t < 0 $$
Alors F(x) = 1 − e^(−λx) pour x ≥ 0, E(X) = 1/λ et V(X) = 1/λ².
:::

::: figure La densité exponentielle de paramètre 0,25 décroît à partir de 0,25 ; l'aire colorée entre t = 2 et t = 6 est la probabilité p(2 ≤ X ≤ 6), environ 0,38
<svg viewBox="0 0 340 250">
<title>Densité exponentielle f(t) = 0,25 e^(−0,25t) ; l'aire entre t = 2 et t = 6 vaut environ 0,38</title>
<path d="M35 200 L332 200" fill="none" stroke="#0f172a" stroke-width="1.8" stroke-linecap="round"/>
<path d="M45 206 L45 36" fill="none" stroke="#0f172a" stroke-width="1.8" stroke-linecap="round"/>
<text x="332" y="218" text-anchor="end" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">t</text>
<polygon points="89,200 89,109 94.5,114.5 100,119.7 105.5,124.6 111,129.1 116.5,133.4 122,137.5 127.5,141.3 133,144.8 138.5,148.2 144,151.3 149.5,154.3 155,157 160.5,159.6 166,162.1 171.5,164.4 177,166.5 177,200" fill="#0f6e56" fill-opacity="0.22" stroke="none"/>
<path d="M45 50 L56 67.6 L67 83.2 L78 96.9 L89 109 L100 119.7 L111 129.1 L122 137.5 L133 144.8 L144 151.3 L155 157 L166 162.1 L177 166.5 L188 170.5 L199 173.9 L210 177 L221 179.7 L232 182.1 L243 184.2 L254 186 L265 187.7 L276 189.1 L287 190.4 L298 191.5 L309 192.5" fill="none" stroke="#0f6e56" stroke-width="3" stroke-linejoin="round"/>
<path d="M89 200 L89 109" fill="none" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round" stroke-dasharray="4 3"/>
<path d="M177 200 L177 166.5" fill="none" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round" stroke-dasharray="4 3"/>
<path d="M45 200 L45 205" fill="none" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="45" y="220" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0</text>
<path d="M89 200 L89 205" fill="none" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="89" y="220" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">2</text>
<path d="M133 200 L133 205" fill="none" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="133" y="220" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">4</text>
<path d="M177 200 L177 205" fill="none" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="177" y="220" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">6</text>
<path d="M221 200 L221 205" fill="none" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="221" y="220" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">8</text>
<path d="M265 200 L265 205" fill="none" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="265" y="220" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">10</text>
<path d="M309 200 L309 205" fill="none" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="309" y="220" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">12</text>
<path d="M45 50 L41 50" fill="none" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="37" y="54" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0,25</text>
<text x="133" y="186" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0,38</text>
<text x="234.2" y="172.5" text-anchor="middle" font-size="15" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">f</text>
<circle cx="45" cy="50" r="4" fill="#0f6e56" stroke="#0f172a" stroke-width="1"/>
</svg>
:::

La courbe est la densité f(t) = 0,25 e^(−0,25t) : elle part de λ = 0,25 en t = 0 et décroît, donc les durées courtes sont plus probables que les longues.

::: exemple Le capteur

1. E(X) = 4 = 1/λ, donc λ = 1/4 = 0,25 et f(t) = 0,25 e^(−0,25t).
2. p(X > 2) = 1 − F(2) = e^(−0,25 × 2) = e^(−0,5) ≈ 0,607.
3. p(2 ≤ X ≤ 6) = F(6) − F(2) = e^(−0,5) − e^(−1,5) ≈ 0,6065 − 0,2231 = 0,3834, soit environ 0,38.
4. Sachant que le capteur a déjà fonctionné 4 ans : p(X > 6 sachant X > 4) = p(X > 6)/p(X > 4) = e^(−1,5)/e^(−1) = e^(−0,5) ≈ 0,607, la même probabilité que pour un capteur neuf. Cette propriété s'appelle l'absence de mémoire.

:::

::: piege
**Erreur : prendre la moyenne pour le paramètre.** La moyenne est 4 ans, on écrit λ = 4 et on trouve p(X > 2) = e^(−8) ≈ 0,0003, ce qui est absurde pour un capteur qui dure 4 ans en moyenne. Le paramètre est l'inverse de la moyenne : λ = 1/E(X) = 0,25.
:::

::: propriete
Si X suit la loi exponentielle de paramètre λ, pour 0 ≤ a ≤ b et t ≥ 0 :
- p(X > t) = e^(−λt) et p(X ≤ t) = 1 − e^(−λt) ;
- p(a ≤ X ≤ b) = e^(−λa) − e^(−λb) ;
- absence de mémoire : p(X > s + t sachant X > s) = p(X > t) = e^(−λt) pour s ≥ 0.

Cas limite : p(X < 0) = 0, donc F(x) = 0 pour x < 0 et la durée est toujours positive.
:::

::: verifie À toi : l'attente au guichet
Le temps d'attente X d'un client à un guichet, en minutes, suit la loi exponentielle de paramètre 0,2. Calcule p(X > 5) et E(X).

---

Pour une loi exponentielle, p(X > t) = e^(−λt), donc p(X > 5) = e^(−0,2 × 5) = e^(−1) ≈ 0,368. L'espérance est l'inverse du paramètre : E(X) = 1/0,2 = 5 minutes.
:::

::: retenir
Loi exponentielle de paramètre λ : densité λe^(−λt), p(X > t) = e^(−λt), E(X) = 1/λ, V(X) = 1/λ², et absence de mémoire.
:::

> 🏆 Porte franchie, héros : tu transformes un hasard en nombres, tu en lis la loi, la moyenne et l'écart, et tu passes des valeurs isolées (loi binomiale) aux durées continues (uniforme, exponentielle). Au prochain chapitre, les statistiques décrivent des données réelles avec les mêmes outils de moyenne et de dispersion.
