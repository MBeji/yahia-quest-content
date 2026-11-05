# ⚔️ Statistiques — deux mesures, une seule droite

> 💡 «Une moyenne résume une série ; une droite tente de relier deux séries. Reste à lui demander de prouver qu'elle le mérite.»

En 1669, Huygens lit les registres de décès de Londres : sur 100 personnes conçues, 64 atteignent 6 ans, 40 atteignent 16 ans, 25 atteignent 26 ans… Il en tire une durée de vie moyenne, puis prévient que ce n'est pas une prédiction pour un enfant donné. Toute la statistique tient dans cette prudence. Ce dernier chapitre du manuel te met deux séries entre les mains. Huit notions : distributions marginales, covariance d'un échantillon simple, covariance d'un échantillon groupé, nuage de points et point moyen, méthode de Mayer, moindres carrés, coefficient de corrélation linéaire et changement de variable. Tu réutilises la moyenne et l'écart-type, la dérivée, la fonction exponentielle, le logarithme népérien et la valeur moyenne d'une fonction.

## 📊 Distributions marginales

Une mairie interroge 25 ménages. Sur chacun, elle relève X, le nombre d'enfants (0, 1 ou 2), et Y, le revenu mensuel en centaines de dinars, rangé par classes [2 ; 4[, [4 ; 6[ et [6 ; 8[.
Chaque ménage fournit un couple, pas un nombre isolé. Comment résumer chaque variable séparément, sans perdre le tableau commun ?

::: definition
Une **série statistique double** (X, Y) associe à chaque individu d'un échantillon de taille n deux valeurs numériques (xᵢ, yᵢ). La **distribution marginale** de X est la distribution des seules valeurs xᵢ ; celle de Y est la distribution des seules valeurs yᵢ.
Pour une variable discrète, x₁, …, x_p sont ses valeurs distinctes ; pour une variable continue, ce sont les centres des classes. nᵢ est l'effectif de xᵢ.
$$ X̄ = (1/n)Σ nᵢxᵢ    V(X) = (1/n)Σ nᵢ(xᵢ − X̄)²    σ_X = √V(X) $$
:::

| Effectifs nᵢⱼ | Y ∈ [2 ; 4[ | Y ∈ [4 ; 6[ | Y ∈ [6 ; 8[ | **Total** |
| ------------- | ----------- | ----------- | ----------- | --------- |
| X = 0         | 4           | 3           | 1           | **8**     |
| X = 1         | 1           | 5           | 3           | **9**     |
| X = 2         | 0           | 2           | 6           | **8**     |
| **Total**     | **5**       | **10**      | **10**      | **25**    |

La colonne des totaux est la marge de X : les effectifs 8, 9 et 8. La ligne des totaux est la marge de Y : 5, 10 et 10. Leurs fréquences, obtenues en divisant par 25, valent 0,32 ; 0,36 ; 0,32 pour X et 0,2 ; 0,4 ; 0,4 pour Y, et chaque marge a une somme de fréquences égale à 1.

::: exemple Les 25 ménages

1. Pour X : Σnᵢxᵢ = 8 × 0 + 9 × 1 + 8 × 2 = 25, donc X̄ = 25/25 = 1 enfant, car chaque effectif pèse autant de fois que sa valeur.
2. Par les écarts : 8 × (0 − 1)² + 9 × 0² + 8 × 1² = 16, donc V(X) = 16/25 = 0,64 et σ_X = 0,8.
3. Pour Y, on remplace chaque classe par son centre, 3, 5 et 7 : Σnⱼcⱼ = 5 × 3 + 10 × 5 + 10 × 7 = 135, donc Ȳ = 135/25 = 5,4 centaines de dinars, soit 540 DT.
4. Forme développée, équivalente et plus rapide : Σnⱼcⱼ² = 5 × 9 + 10 × 25 + 10 × 49 = 785, donc V(Y) = 785/25 − 5,4² = 31,4 − 29,16 = 2,24 et σ_Y ≈ 1,497.
5. Contrôle par les écarts : 5 × (3 − 5,4)² + 10 × (5 − 5,4)² + 10 × (7 − 5,4)² = 28,8 + 1,6 + 25,6 = 56, et 56/25 = 2,24 ✓.

:::

::: piege
**Erreur : prendre une borne de classe à la place du centre.** Avec les bornes inférieures 2, 4 et 6, on trouve (5 × 2 + 10 × 4 + 10 × 6)/25 = 110/25 = 4,4 ; avec les bornes supérieures 4, 6 et 8, on trouve 160/25 = 6,4. Les deux moyennes sont décalées d'une unité de part et d'autre de la vraie valeur 5,4. Le centre (a + b)/2 est la seule valeur qui représente la classe.
:::

::: propriete

- Les effectifs d'une marge somment à n et ses fréquences à 1 : c'est le premier contrôle, gratuit.
- Pour V(X), la forme centrée (1/n)Σnᵢ(xᵢ − X̄)² et la forme développée (1/n)Σnᵢxᵢ² − X̄² donnent le même nombre ; la seconde est celle des solutions du manuel et de la calculatrice, admise sans démonstration.

Cas limite : si X ne prend qu'une valeur, tous les écarts sont nuls et V(X) = 0.
:::

::: verifie À toi : les durées d'attente
Vingt clients d'un guichet attendent : 6 pendant une durée de la classe [0 ; 4[ minutes, 10 pendant [4 ; 8[ et 4 pendant [8 ; 12[. Calcule la moyenne et l'écart-type de la durée d'attente.

---

Les centres des classes sont 2, 6 et 10. Σnᵢcᵢ = 12 + 60 + 40 = 112, donc X̄ = 112/20 = 5,6 minutes. Puis Σnᵢcᵢ² = 6 × 4 + 10 × 36 + 4 × 100 = 784, donc V = 784/20 − 5,6² = 39,2 − 31,36 = 7,84 et σ = √7,84 = 2,8 minutes. On a utilisé les centres, pas les bornes, puis la forme développée de la variance.
:::

::: retenir
Les marges d'un tableau double sont deux séries simples ; une classe est représentée par son centre, et V(X) = (1/n)Σnᵢxᵢ² − X̄².
:::

## ⚡ Covariance d'un échantillon simple

Pour tester un mur, on pose une couche de polystyrène d'épaisseur X (en cm) et on mesure la résistance thermique Y (en m²·°C/W). Cinq essais :

| Épaisseur xᵢ (cm) | 2   | 4   | 6   | 8   | 10  |
| ----------------- | --- | --- | --- | --- | --- |
| Résistance yᵢ     | 0,9 | 1,3 | 1,7 | 2,4 | 2,7 |

Les moyennes ne parlent pas du lien entre les deux colonnes. Quand l'épaisseur monte, la résistance monte-t-elle aussi, et comment le résumer en un nombre ?

::: definition
La **covariance** de la série double (X, Y), pour un échantillon de taille n, est
$$ cov(X, Y) = (1/n)Σ xᵢyᵢ − X̄·Ȳ $$
où (xᵢ, yᵢ) est la valeur observée pour l'individu i, ou le centre de la classe si une variable est continue. On a cov(X, Y) = cov(Y, X).
:::

::: exemple Le mur et son isolant

1. Moyennes : Σxᵢ = 30, donc X̄ = 6 ; Σyᵢ = 9, donc Ȳ = 1,8.
2. Produits : Σxᵢyᵢ = 1,8 + 5,2 + 10,2 + 19,2 + 27 = 63,4, donc la moyenne des produits vaut 63,4/5 = 12,68.
3. cov(X, Y) = 12,68 − 6 × 1,8 = 12,68 − 10,8 = 1,88.
4. Contrôle par les écarts : ceux de X valent −4 ; −2 ; 0 ; 2 ; 4 et ceux de Y valent −0,9 ; −0,5 ; −0,1 ; 0,6 ; 0,9. Les produits sont 3,6 ; 1 ; 0 ; 1,2 ; 3,6, de somme 9,4, et 9,4/5 = 1,88 ✓.
5. Pour la suite, on retient V(X) = 220/5 − 36 = 8, donc σ_X ≈ 2,828, et V(Y) = 18,44/5 − 1,8² = 0,448, donc σ_Y ≈ 0,669.

:::

::: piege
**Erreur : juger la force du lien sur la valeur de cov(X, Y).** Exprime l'épaisseur en millimètres au lieu de centimètres : X̄ passe à 60, et la covariance à 18,8, soit dix fois plus grande, alors que le lien entre le mur et sa résistance n'a pas changé d'un cheveu. La covariance dépend des unités ; seul son signe se lit directement.
:::

::: propriete

- cov(X, Y) mesure la tendance qu'ont X et Y à varier ensemble.
- Une covariance positive indique que X et Y varient dans le même sens ; une covariance négative, qu'ils varient en sens contraire.

Cas limite : si Y garde la même valeur pour tous les individus, alors Σxᵢyᵢ = Ȳ·Σxᵢ et cov(X, Y) = 0 : rien ne varie.
:::

::: verifie À toi : le sens de la variation
Quatre couples : (1 ; 8), (3 ; 5), (5 ; 4) et (7 ; 1). Calcule cov(X, Y) et interprète son signe.

---

X̄ = 16/4 = 4 et Ȳ = 18/4 = 4,5. Σxᵢyᵢ = 8 + 15 + 20 + 7 = 50, donc cov(X, Y) = 50/4 − 4 × 4,5 = 12,5 − 18 = −5,5. Elle est négative : quand X augmente, Y a tendance à diminuer, les deux variables varient en sens contraire.
:::

::: retenir
cov(X, Y) = (1/n)Σxᵢyᵢ − X̄Ȳ ; son signe dit si X et Y varient dans le même sens ou en sens contraire.
:::

## 🧮 Covariance d'un échantillon groupé

Retour aux 25 ménages : le nombre d'enfants et le revenu varient-ils ensemble ?
Ici les données ne sont plus 25 couples écrits un à un, mais des cases d'effectifs nᵢⱼ, avec les revenus rangés par classes. Chaque produit xᵢyⱼ doit compter autant de fois que son effectif.

::: definition
Soit nᵢⱼ le nombre de fois qu'apparaît le couple (xᵢ, yⱼ). La covariance d'un échantillon groupé de taille n est
$$ cov(X, Y) = (1/n)ΣΣ nᵢⱼxᵢyⱼ − X̄·Ȳ $$
Avec une variable continue, xᵢ ou yⱼ est le centre de la classe.
:::

::: exemple Enfants et revenu

1. On balaie le tableau en ignorant les cases où un facteur est nul. La ligne X = 0 ne contribue pas, car x = 0.
2. Ligne X = 1 : 1 × (1 × 3) + 5 × (1 × 5) + 3 × (1 × 7) = 3 + 25 + 21 = 49, chaque case étant son effectif fois xᵢyⱼ.
3. Ligne X = 2 : 2 × (2 × 5) + 6 × (2 × 7) = 20 + 84 = 104 ; la case d'effectif 0 ne compte pas.
4. Le total est ΣΣ nᵢⱼxᵢyⱼ = 49 + 104 = 153 ; avec X̄ = 1 et Ȳ = 5,4, cov(X, Y) = 153/25 − 1 × 5,4 = 6,12 − 5,4 = 0,72.
5. Elle est positive : les ménages qui ont le plus d'enfants ont plutôt les plus hauts revenus.

:::

::: piege
**Erreur : multiplier par l'effectif d'une marge au lieu de celui de la case.** Pour X = 2 et Y = 7, on écrit 8 × (2 × 7) en prenant le total de la ligne, alors que 6 ménages seulement sont dans cette case. La covariance sort fausse, sans qu'aucun contrôle ne le signale ensuite : l'effectif d'une case est toujours celui du tableau intérieur.
:::

::: propriete

- Chaque case contribue pour nᵢⱼ × xᵢ × yⱼ ; les cases d'effectif nul, ou de valeur x ou y nulle, ne contribuent pas.
- Pour un échantillon simple, tous les nᵢⱼ valent 0 ou 1 et on retrouve la formule précédente.

Cas limite : si le tableau n'a qu'une ligne ou qu'une colonne, X ou Y est constante et la covariance est nulle.
:::

::: verifie À toi : un petit tableau
Dix paniers sont classés selon X (1 ou 2 kg de fruits) et Y (10 ou 20 DT). Effectifs : (1 ; 10) → 3, (1 ; 20) → 1, (2 ; 10) → 2, (2 ; 20) → 4. Calcule cov(X, Y).

---

Les marges de X sont 4 et 6, donc X̄ = (4 + 12)/10 = 1,6 ; celles de Y sont 5 et 5, donc Ȳ = (50 + 100)/10 = 15. Les cases donnent 3 × 10 + 1 × 20 + 2 × 20 + 4 × 40 = 30 + 20 + 40 + 160 = 250, chaque case valant nᵢⱼxᵢyⱼ. Donc cov(X, Y) = 250/10 − 1,6 × 15 = 25 − 24 = 1.
:::

::: retenir
Pour un tableau double, cov(X, Y) = (1/n)ΣΣ nᵢⱼxᵢyⱼ − X̄Ȳ, avec l'effectif de la case et jamais celui d'une marge.
:::

## 🔮 Nuage de points et point moyen

Reprenons le mur. Un tableau de nombres cache la forme du lien.
Où se placent les cinq essais, où est leur « centre », et peut-on prévoir la résistance pour 12 cm d'isolant ?

::: definition
Dans un repère orthogonal, l'ensemble des points Mᵢ(xᵢ ; yᵢ) est le **nuage de points** de la série double. Son **point moyen** G a pour coordonnées les moyennes (X̄ ; Ȳ).
Prévoir Y à partir de X par Y = aX + b est un **ajustement affine** : X est la variable **explicative**, Y la variable **expliquée**, et y = ax + b est la droite d'ajustement affine de Y en X.
:::

::: figure Les cinq essais montent en bande ; le point moyen G(6 ; 1,8) n'est aucun des cinq points observés, c'est leur centre d'équilibre.
<svg viewBox="0 0 340 250"><g stroke="#94a3b8" stroke-width="1" fill="none"><path d="M50 160 H310 M50 105 H310 M50 50 H310"/></g><path d="M50 215 H322" fill="none" stroke="#0f172a" stroke-width="1.8"/><path d="M50 215 V32" fill="none" stroke="#0f172a" stroke-width="1.8"/><g stroke="#0f172a" stroke-width="1.4" fill="none"><path d="M94 215 V220 M138 215 V220 M182 215 V220 M226 215 V220 M270 215 V220"/></g><path d="M182 116 L182 215" fill="none" stroke="#0f6e56" stroke-width="1.6" stroke-dasharray="6 4"/><path d="M50 116 L182 116" fill="none" stroke="#0f6e56" stroke-width="1.6" stroke-dasharray="6 4"/><g fill="#0f172a"><circle cx="94" cy="165.5" r="4.5"/><circle cx="138" cy="143.5" r="4.5"/><circle cx="182" cy="121.5" r="4.5"/><circle cx="226" cy="83" r="4.5"/><circle cx="270" cy="66.5" r="4.5"/></g><circle cx="182" cy="116" r="5.5" fill="#0f6e56"/><g font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="94" y="233" text-anchor="middle" fill="#0f172a">2</text><text x="138" y="233" text-anchor="middle" fill="#0f172a">4</text><text x="182" y="233" text-anchor="middle" fill="#0f172a">6</text><text x="226" y="233" text-anchor="middle" fill="#0f172a">8</text><text x="270" y="233" text-anchor="middle" fill="#0f172a">10</text><text x="38" y="165" text-anchor="middle" fill="#0f172a">1</text><text x="38" y="110" text-anchor="middle" fill="#0f172a">2</text><text x="38" y="55" text-anchor="middle" fill="#0f172a">3</text><text x="328" y="233" text-anchor="middle" fill="#0f172a">x</text><text x="42" y="28" text-anchor="middle" fill="#0f172a">y</text><text x="196" y="108" text-anchor="middle" fill="#0f6e56">G</text></g></svg>
:::

Sur la figure, l'abscisse de G est X̄ = 6 et son ordonnée Ȳ = 1,8, les deux pointillés. Les points à gauche de G sont sous lui, ceux à droite au-dessus, ce qui annonce une droite montante.

::: exemple Le point moyen du mur

1. D'après le calcul de la covariance, X̄ = 6 et Ȳ = 1,8 : G(6 ; 1,8).
2. Aucun essai n'a pour couple (6 ; 1,8) : à l'épaisseur 6, la résistance observée est 1,7. G est donc un point du plan, pas un point du nuage.
3. Les essais s'alignent grossièrement : une droite a un sens. Reste à choisir laquelle, avec Mayer puis les moindres carrés.

:::

::: piege
**Erreur : croire que le point moyen est un des points du nuage.** On cherche G dans le tableau des mesures, et on ne le trouve pas, par exemple ici où l'on lit 1,7 à l'épaisseur 6. G se calcule, il ne se lit pas : ses coordonnées sont des moyennes, qui peuvent n'appartenir à aucun individu.
:::

::: propriete

- Le point moyen G(X̄ ; Ȳ) est calculé à partir des deux marges ; il est le centre du nuage.
- La droite de Mayer et les droites des moindres carrés passent exactement par G.

Cas limite : si tous les points sont alignés sur une droite, G est sur cette droite.
:::

::: verifie À toi : le centre du nuage
Quatre points : (1 ; 7), (2 ; 9), (5 ; 12) et (8 ; 12). Donne le point moyen G et dis s'il appartient au nuage.

---

X̄ = (1 + 2 + 5 + 8)/4 = 4 et Ȳ = (7 + 9 + 12 + 12)/4 = 10, donc G(4 ; 10). Aucun des quatre points n'a l'abscisse 4, donc G n'appartient pas au nuage : c'est un point calculé.
:::

::: retenir
Le nuage place chaque couple ; son point moyen G(X̄ ; Ȳ) en est le centre, et y = ax + b désigne la droite d'ajustement de Y (expliquée) en X (explicative).
:::

## 🗡️ La méthode de Mayer

On connaît un point de la droite cherchée, le point moyen G.
Pour la tracer à la main, il en manque un second. Comment l'obtenir sans formule compliquée ?

::: definition
**Méthode de Mayer.** On scinde le nuage en deux parties contenant à peu près le même nombre de points, de points moyens G₁ et G₂. La droite (G₁G₂), dite **droite de Mayer**, est un ajustement affine du nuage ; elle passe par le point moyen G du nuage entier.
:::

::: figure La droite (G₁G₂) traverse G sans qu'on l'y ait forcée : c'est le contrôle de toute la méthode.
<svg viewBox="0 0 340 250"><g stroke="#94a3b8" stroke-width="1" fill="none"><path d="M50 160 H310 M50 105 H310 M50 50 H310"/></g><path d="M50 215 H322" fill="none" stroke="#0f172a" stroke-width="1.8"/><path d="M50 215 V32" fill="none" stroke="#0f172a" stroke-width="1.8"/><g stroke="#0f172a" stroke-width="1.4" fill="none"><path d="M94 215 V220 M138 215 V220 M182 215 V220 M226 215 V220 M270 215 V220"/></g><path d="M72 184.75 L303 40.38" fill="none" stroke="#0f6e56" stroke-width="2.4"/><g fill="#0f172a"><circle cx="94" cy="165.5" r="4.5"/><circle cx="138" cy="143.5" r="4.5"/><circle cx="182" cy="121.5" r="4.5"/><circle cx="226" cy="83" r="4.5"/><circle cx="270" cy="66.5" r="4.5"/></g><circle cx="138" cy="143.5" r="5" fill="#0f6e56"/><circle cx="248" cy="74.75" r="5" fill="#0f6e56"/><circle cx="182" cy="116" r="5.5" fill="#b45309"/><g font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="94" y="233" text-anchor="middle" fill="#0f172a">2</text><text x="138" y="233" text-anchor="middle" fill="#0f172a">4</text><text x="182" y="233" text-anchor="middle" fill="#0f172a">6</text><text x="226" y="233" text-anchor="middle" fill="#0f172a">8</text><text x="270" y="233" text-anchor="middle" fill="#0f172a">10</text><text x="38" y="165" text-anchor="middle" fill="#0f172a">1</text><text x="38" y="110" text-anchor="middle" fill="#0f172a">2</text><text x="38" y="55" text-anchor="middle" fill="#0f172a">3</text><text x="328" y="233" text-anchor="middle" fill="#0f172a">x</text><text x="42" y="28" text-anchor="middle" fill="#0f172a">y</text><text x="124" y="133.5" text-anchor="middle" fill="#0f6e56">G₁</text><text x="262" y="88.75" text-anchor="middle" fill="#0f6e56">G₂</text><text x="196" y="108" text-anchor="middle" fill="#b45309">G</text></g></svg>
:::

Les deux points verts sont G₁ et G₂, le point orange est G. La pente de la droite est l'accroissement de y sur celui de x entre G₁ et G₂.

::: exemple Mayer sur le mur

1. On sépare les trois premiers essais des deux derniers. G₁ a pour abscisse (2 + 4 + 6)/3 = 4 et pour ordonnée (0,9 + 1,3 + 1,7)/3 = 1,3 : G₁(4 ; 1,3).
2. G₂ a pour abscisse (8 + 10)/2 = 9 et pour ordonnée (2,4 + 2,7)/2 = 2,55 : G₂(9 ; 2,55).
3. Pente : a = (2,55 − 1,3)/(9 − 4) = 1,25/5 = 0,25, puis b = 1,3 − 0,25 × 4 = 0,3. La droite est y = 0,25x + 0,3.
4. Contrôle : elle passe par G, car 0,25 × 6 + 0,3 = 1,8 ✓. Si ce contrôle échoue, une des deux moyennes partielles est fausse.
5. Prévision à 12 cm : 0,25 × 12 + 0,3 = 3,3 m²·°C/W.

:::

::: piege
**Erreur : croire que la droite de Mayer est unique.** Scinde autrement, deux essais puis trois : G₁(3 ; 1,1) et G₂(8 ; 2,2667) donnent une pente de 0,2333 et la droite y ≈ 0,233x + 0,4. Elle passe encore par G (0,2333 × 6 + 0,4 = 1,8), mais ce n'est plus la même droite. Mayer fournit une droite acceptable, pas la meilleure : c'est ce qui motive la méthode suivante.
:::

::: propriete

- Mayer se fait en quatre gestes : scinder, calculer G₁ et G₂, calculer la pente puis l'ordonnée à l'origine, vérifier le passage par G.
- La droite obtenue dépend du découpage choisi.

Cas limite : si le nombre de points est impair, les deux parties diffèrent d'un point, comme ici avec 3 et 2.
:::

::: verifie À toi : une droite de Mayer
Les points moyens des deux parties sont G₁(3 ; 2,5) et G₂(9 ; 5,5). Donne l'équation de la droite de Mayer.

---

La pente est a = (5,5 − 2,5)/(9 − 3) = 3/6 = 0,5. L'ordonnée à l'origine vient de G₁ : b = 2,5 − 0,5 × 3 = 1, donc y = 0,5x + 1. Contrôle sur G₂ : 0,5 × 9 + 1 = 5,5 ✓.
:::

::: retenir
La droite de Mayer est la droite (G₁G₂) des points moyens des deux moitiés du nuage ; elle passe par G, mais dépend du découpage.
:::

## 🎯 Les moindres carrés

Mayer donne une droite, pas la meilleure.
Pour classer des droites, il faut mesurer ce qu'elles coûtent. Quelle droite se trompe le moins sur l'ensemble des points ?

::: definition
Pour une droite D d'équation y = ax + b, Hᵢ(xᵢ ; zᵢ) est le point de D de même abscisse que le point observé Mᵢ(xᵢ ; yᵢ). La méthode des moindres carrés cherche a et b tels que ΣMᵢHᵢ², la somme des carrés des écarts verticaux, soit **minimale**. La prévision remplace alors la valeur observée yᵢ par la valeur théorique zᵢ = axᵢ + b.
**Théorème (admis).** Si σ_X ≠ 0, la somme Σ(axᵢ + b − yᵢ)² est minimale pour
$$ a₀ = cov(X, Y)/σ_X²    b₀ = Ȳ − a₀·X̄ $$
:::

::: figure Les segments orange MᵢHᵢ ne mesurent que de quelques centièmes à un dixième : la droite des moindres carrés est celle qui rend la somme de leurs carrés minimale.
<svg viewBox="0 0 340 250"><g stroke="#94a3b8" stroke-width="1" fill="none"><path d="M50 160 H310 M50 105 H310 M50 50 H310"/></g><path d="M50 215 H322" fill="none" stroke="#0f172a" stroke-width="1.8"/><path d="M50 215 V32" fill="none" stroke="#0f172a" stroke-width="1.8"/><g stroke="#0f172a" stroke-width="1.4" fill="none"><path d="M94 215 V220 M138 215 V220 M182 215 V220 M226 215 V220 M270 215 V220"/></g><path d="M72 180.62 L303 44.91" fill="none" stroke="#0f6e56" stroke-width="2.4"/><g fill="#0f172a"><circle cx="94" cy="165.5" r="2.5"/><circle cx="138" cy="143.5" r="2.5"/><circle cx="182" cy="121.5" r="2.5"/><circle cx="226" cy="83" r="2.5"/><circle cx="270" cy="66.5" r="2.5"/></g><circle cx="182" cy="116" r="3.5" fill="#0f6e56"/><path d="M94 165.5 L94 167.7" fill="none" stroke="#b45309" stroke-width="3"/><path d="M138 143.5 L138 141.85" fill="none" stroke="#b45309" stroke-width="3"/><path d="M182 121.5 L182 116" fill="none" stroke="#b45309" stroke-width="3"/><path d="M226 83 L226 90.15" fill="none" stroke="#b45309" stroke-width="3"/><path d="M270 66.5 L270 64.3" fill="none" stroke="#b45309" stroke-width="3"/><g font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="94" y="233" text-anchor="middle" fill="#0f172a">2</text><text x="138" y="233" text-anchor="middle" fill="#0f172a">4</text><text x="182" y="233" text-anchor="middle" fill="#0f172a">6</text><text x="226" y="233" text-anchor="middle" fill="#0f172a">8</text><text x="270" y="233" text-anchor="middle" fill="#0f172a">10</text><text x="38" y="165" text-anchor="middle" fill="#0f172a">1</text><text x="38" y="110" text-anchor="middle" fill="#0f172a">2</text><text x="38" y="55" text-anchor="middle" fill="#0f172a">3</text><text x="328" y="233" text-anchor="middle" fill="#0f172a">x</text><text x="42" y="28" text-anchor="middle" fill="#0f172a">y</text><text x="196" y="106" text-anchor="middle" fill="#0f6e56">G</text><text x="176" y="141.5" text-anchor="middle" fill="#0f172a">M₃</text></g></svg>
:::

Sur la figure, les segments orange relient chaque point observé Mᵢ au point Hᵢ de la droite ; au rang 3 (abscisse 6), Hᵢ est G lui-même.

::: exemple Les moindres carrés sur le mur

1. Avec cov(X, Y) = 1,88 et σ_X² = V(X) = 8 : a₀ = 1,88/8 = 0,235.
2. b₀ = Ȳ − a₀X̄ = 1,8 − 0,235 × 6 = 1,8 − 1,41 = 0,39, donc D : y = 0,235x + 0,39.
3. Contrôle n° 1 : D passe par G, car 0,235 × 6 + 0,39 = 1,8 ✓.
4. Valeurs théoriques : 0,86 ; 1,33 ; 1,8 ; 2,27 ; 2,74, d'où les écarts yᵢ − zᵢ : 0,04 ; −0,03 ; −0,1 ; 0,13 ; −0,04. Contrôle n° 2 : leur somme vaut 0 ✓, ce qui est automatique quand la droite passe par G.
5. Somme des carrés : S_D = 0,0016 + 0,0009 + 0,01 + 0,0169 + 0,0016 = 0,031. Pour la droite de Mayer, les écarts valent 0,1 ; 0 ; −0,1 ; 0,1 ; −0,1 et S_Δ = 0,04. On a bien 0,031 < 0,04.
6. Prévision à 12 cm : 0,235 × 12 + 0,39 = 3,21 m²·°C/W, contre 3,3 par Mayer.

:::

::: piege
**Erreur : diviser la covariance par σ_X au lieu de σ_X².** On écrit a = 1,88/2,828 ≈ 0,665 et b = 1,8 − 0,665 × 6 ≈ −2,19, donc une résistance de 5,8 à 12 cm, quand les mesures plafonnent à 2,7 à 10 cm. Le dénominateur est une variance, pas un écart-type : un contrôle de vraisemblance sur la pente aurait suffi.
:::

::: propriete

- La droite d'équation y = (cov(X, Y)/σ_X²)(x − X̄) + Ȳ est la **droite de régression de Y en X**.
- La droite d'équation x = (cov(X, Y)/σ_Y²)(y − Ȳ) + X̄ est la **droite de régression de X en Y**, définie de la même façon, en échangeant les rôles.
- Les deux droites de régression passent par le point moyen G du nuage.

Cas limite : si σ_X = 0, tous les points ont la même abscisse et le théorème ne s'applique pas.
:::

::: verifie À toi : une droite de régression
X̄ = 5, Ȳ = 12, σ_X² = 4 et cov(X, Y) = 6. Donne la droite de régression de Y en X, puis la valeur prévue pour x = 8.

---

La pente est a₀ = cov(X, Y)/σ_X² = 6/4 = 1,5, puis b₀ = Ȳ − a₀X̄ = 12 − 1,5 × 5 = 4,5, donc y = 1,5x + 4,5. Contrôle : en x = 5, 7,5 + 4,5 = 12 = Ȳ ✓. Pour x = 8 : y = 12 + 4,5 = 16,5. La prévision est une valeur théorique, pas une certitude.
:::

::: retenir
La droite des moindres carrés de Y en X est y = (cov/σ_X²)(x − X̄) + Ȳ : elle passe par G et rend ΣMᵢHᵢ² minimale.
:::

> 🗡️ En mode statistique à deux variables, la calculatrice fournit n, Σx, Σx², Σxy, X̄, σ_X, le coefficient r, et les coefficients a et b de la droite de régression de Y en X. Les touches changent d'un modèle à l'autre. Utilise-la pour vérifier, jamais pour remplacer la ligne de calcul que le correcteur attend.

## 📐 Le coefficient de corrélation linéaire

Une droite de régression existe toujours, même sur un nuage sans forme.
La prévision par le mur donne 3,21 pour 12 cm ; la prévoir pour le revenu des ménages donnerait quelque chose d'aussi précis, mais d'aussi sûr ? Il faut un juge : un nombre sans unité.

::: definition
Le **coefficient de corrélation linéaire** de (X, Y) est
$$ ρ_XY = cov(X, Y)/(σ_X σ_Y) $$
On a −1 ≤ ρ_XY ≤ 1, et ρ_XY est invariant par changement d'unité ou d'origine. Par convention, quand |ρ_XY| > √3/2 ≈ 0,866, l'ajustement affine est **justifié** et ses prévisions sont raisonnables.
:::

::: figure Trois nuages, trois verdicts : à gauche les points s'alignent en montant, au centre ils ne dessinent rien, à droite ils s'alignent en descendant ; seuls le premier et le dernier dépassent 0,866 en valeur absolue.
<svg viewBox="0 0 380 165"><g stroke="#0f172a" stroke-width="1.6" fill="none"><path d="M15 130 H105 M15 130 V40"/><path d="M145 130 H235 M145 130 V40"/><path d="M275 130 H365 M275 130 V40"/></g><g fill="#0f6e56"><circle cx="27" cy="113.2" r="4"/><circle cx="39" cy="103.4" r="4"/><circle cx="51" cy="82.4" r="4"/><circle cx="63" cy="76.8" r="4"/><circle cx="75" cy="55.8" r="4"/><circle cx="87" cy="50.2" r="4"/></g><g fill="#64748b"><circle cx="157" cy="83.8" r="4"/><circle cx="169" cy="110.4" r="4"/><circle cx="181" cy="65.6" r="4"/><circle cx="193" cy="100.6" r="4"/><circle cx="205" cy="68.4" r="4"/><circle cx="217" cy="89.4" r="4"/></g><g fill="#b45309"><circle cx="287" cy="53" r="4"/><circle cx="299" cy="71.2" r="4"/><circle cx="311" cy="75.4" r="4"/><circle cx="323" cy="96.4" r="4"/><circle cx="335" cy="99.2" r="4"/><circle cx="347" cy="117.4" r="4"/></g><g font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="60" y="152" text-anchor="middle" fill="#0f6e56">ρ ≈ 0,99</text><text x="190" y="152" text-anchor="middle" fill="#475569">ρ ≈ 0,19</text><text x="320" y="152" text-anchor="middle" fill="#b45309">ρ ≈ −0,98</text></g></svg>
:::

Le nombre sous chaque nuage est son ρ ; le signe suit la covariance, et la valeur absolue mesure l'alignement.

::: exemple Le mur et les ménages

1. Pour le mur : ρ_XY = 1,88/(2,828 × 0,669) = 1,88/1,893 ≈ 0,993. Comme 0,993 > 0,866, l'ajustement affine est justifié, et la prévision de 3,21 pour 12 cm est raisonnable.
2. Contrôle sans racines : ρ² = cov²/(V(X)V(Y)) = 1,88²/(8 × 0,448) = 3,5344/3,584 ≈ 0,986, et √0,986 ≈ 0,993 ✓.
3. Pour les ménages : cov = 0,72, σ_X = 0,8 et σ_Y ≈ 1,497, donc ρ_XY = 0,72/(0,8 × 1,497) = 0,72/1,198 ≈ 0,601.
4. Comme 0,601 < 0,866, l'ajustement affine n'est pas justifié : on peut calculer la droite, mais s'en servir pour prévoir un revenu serait abusif.

:::

::: piege
**Erreur : rejeter un ajustement parce que ρ est négatif.** On trouve ρ = −0,95 et on conclut « pas de lien ». C'est la valeur absolue qui se compare au seuil : |−0,95| = 0,95 > 0,866, l'ajustement est justifié, et le signe dit seulement que la droite descend.
:::

::: propriete

- −1 ≤ ρ_XY ≤ 1 : un résultat hors de cet intervalle trahit une erreur de calcul.
- ρ_XY ne change pas quand on change d'unité ou d'origine. Si l'on multiplie toutes les valeurs de Y par 1 000 (changement d'unité), cov et σ_Y sont multipliés par 1 000 chacun et ρ reste 0,993.

Cas limite : si σ_X ou σ_Y est nul, ρ n'existe pas, car on diviserait par zéro.
:::

::: verifie À toi : le juge
cov(X, Y) = −7,2, σ_X = 3 et σ_Y = 2,5. Calcule ρ_XY et dis si l'ajustement affine est justifié.

---

ρ_XY = −7,2/(3 × 2,5) = −7,2/7,5 = −0,96. La valeur absolue 0,96 dépasse √3/2 ≈ 0,866 : l'ajustement affine est justifié, avec une droite décroissante (ρ est négatif).
:::

::: retenir
ρ_XY = cov/(σ_Xσ_Y) est compris entre −1 et 1 ; l'ajustement affine est justifié si |ρ_XY| > √3/2 ≈ 0,866.
:::

## 🧪 Changer de variable pour redresser un nuage

Une application suit ses utilisateurs actifs, en milliers, trimestre après trimestre : 6, 10, 15, 26 et 40 aux rangs X = 0, 1, 2, 3 et 4. Le nuage s'incurve vers le haut ; une droite ne le suit pas. Comment réutiliser tout ce chapitre sur une courbe ?

::: figure À gauche, la série (X, Y) s'incurve ; à droite, la série (X, Z) avec Z = ln Y s'aligne, et sa droite des moindres carrés la suit de près.
<svg viewBox="0 0 380 175"><g stroke="#0f172a" stroke-width="1.6" fill="none"><path d="M30 130 H150 M30 130 V25"/><path d="M215 130 H335 M215 130 V25"/></g><g fill="#0f172a"><circle cx="30" cy="115" r="4.5"/><circle cx="57" cy="105" r="4.5"/><circle cx="84" cy="92.5" r="4.5"/><circle cx="111" cy="65" r="4.5"/><circle cx="138" cy="30" r="4.5"/></g><path d="M215 118 L323 42" fill="none" stroke="#0f6e56" stroke-width="2.4"/><g fill="#0f172a"><circle cx="215" cy="118.32" r="4.5"/><circle cx="242" cy="97.88" r="4.5"/><circle cx="269" cy="81.68" r="4.5"/><circle cx="296" cy="59.68" r="4.5"/><circle cx="323" cy="42.44" r="4.5"/></g><g font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="90" y="155" text-anchor="middle" fill="#b45309">(X, Y) incurvé</text><text x="275" y="155" text-anchor="middle" fill="#0f6e56">(X, Z) aligné</text><text x="42" y="20" text-anchor="middle" fill="#0f172a">y</text><text x="227" y="20" text-anchor="middle" fill="#0f172a">z</text></g></svg>
:::

À gauche le nuage (X, Y), à droite le même nuage une fois Y remplacé par Z = ln Y : l'axe vertical change, pas l'abscisse X.

::: exemple Les utilisateurs de l'application

1. On pose Z = ln Y, car Y est multiplié par un facteur voisin de 1,6 à chaque trimestre : les zᵢ valent 1,792 ; 2,303 ; 2,708 ; 3,258 et 3,689 (à 10⁻³ près).
2. Pour X : X̄ = 2 et V(X) = 2. Pour Z : Σzᵢ = 13,75, donc Z̄ = 2,75 ; Σzᵢ² ≈ 40,072, donc V(Z) ≈ 8,014 − 7,5625 ≈ 0,452 et σ_Z ≈ 0,672.
3. Σxᵢzᵢ = 2,303 + 5,416 + 9,774 + 14,756 = 32,249, donc cov(X, Z) = 32,249/5 − 2 × 2,75 = 6,45 − 5,5 ≈ 0,95.
4. ρ_XZ = 0,95/(1,414 × 0,672) ≈ 0,999 > 0,866 : l'ajustement affine de Z en X est justifié.
5. a = 0,95/2 ≈ 0,475 et b = 2,75 − 0,475 × 2 = 1,8, donc z = 0,475x + 1,8. Contrôle : en x = 2, 0,95 + 1,8 = 2,75 = Z̄ ✓.
6. On revient à Y : y = e^(0,475x + 1,8) = e^1,8 × e^(0,475x) ≈ 6,05 × e^(0,475x). Contrôle sur les données : à x = 4, 6,05 × e^1,9 ≈ 40,4, contre 40 observés ✓.
7. Prévision au rang 5 : y ≈ 6,05 × e^2,375 ≈ 65 milliers d'utilisateurs.
8. Lecture en pourcentage : y ≈ 6,05 × (e^0,475)^x ≈ 6,05 × 1,61^x ; à chaque trimestre Y est multiplié par e^a ≈ 1,61, soit une hausse d'environ 61 %.

:::

::: piege
**Erreur : lire la prévision sur Z au lieu de Y.** Pour x = 5, la droite donne z = 0,475 × 5 + 1,8 = 4,175, et l'on annonce « 4,2 milliers d'utilisateurs ». Mais z est un logarithme : un nombre d'utilisateurs s'obtient par y = e^z = e^4,175 ≈ 65. Le résultat de la droite n'est jamais la réponse, c'est l'exposant de la réponse.
:::

::: methode Ajuster un nuage incurvé

1. Choisir la nouvelle variable d'après l'allure du nuage : Z = ln Y pour une croissance exponentielle.
2. Calculer les valeurs zᵢ et ρ_XZ ; l'ajustement de Z en X est justifié si |ρ_XZ| > √3/2.
3. Ajuster (X, Z) par les moindres carrés : z = ax + b.
4. Revenir à Y par l'exponentielle : y = e^z = e^b × e^(ax).

Le manuel emploie aussi Z = √Y quand Y croît comme le carré de X, X = V² et Y = R/V pour une résistance qui dépend de la vitesse, et U = ln(8/D − 1) pour une croissance qui plafonne à 8. Pour revenir à D, on inverse en entier : 8/D − 1 = e^u, donc D = 8/(1 + e^u) (avec un plafond k, D = k/(1 + e^u)). Dans tous les cas, on juge avec le ρ de la série ajustée, puis on inverse la transformation.

Cas limite : seules des valeurs yᵢ strictement positives ont un logarithme.
:::

::: verifie À toi : redresser trois points
Les points (0 ; 3), (1 ; 6) et (2 ; 12) donnent Z = ln Y de valeurs 1,099 ; 1,792 et 2,485. Ils sont alignés pour (X, Z) : donne leur droite et la prévision de Y pour x = 4.

---

La pente entre deux points consécutifs de (X, Z) est 1,792 − 1,099 = 0,693 (soit ln 2), et l'ordonnée à l'origine est 1,099, donc z = 0,693x + 1,099. Pour x = 4, z = 2,772 + 1,099 = 3,871, puis y = e^3,871 ≈ 48 : on revient à Y par l'exponentielle. On retrouve y = 3 × 2^x, ce qui confirme la prévision 3 × 16 = 48.
:::

::: retenir
Pour un nuage incurvé, on pose Z = ln Y (ou √Y…), on ajuste (X, Z), on juge avec ρ_XZ, puis on revient à Y par l'exponentielle.
:::

## 👑 Méthode : traiter une série double de bout en bout

| Étape | Question                       | Outil                                                                        |
| ----- | ------------------------------ | ---------------------------------------------------------------------------- |
| 1     | Quelles sont les deux séries ? | marges du tableau ; contrôler que les fréquences somment à 1                 |
| 2     | Comment les résumer ?          | X̄, V(X) = (1/n)Σnᵢxᵢ² − X̄², σ_X, et de même pour Y                           |
| 3     | Varient-elles ensemble ?       | cov(X, Y) = (1/n)Σxᵢyᵢ − X̄Ȳ (ou ΣΣnᵢⱼxᵢyⱼ si groupé) ; lire le **signe**     |
| 4     | Une droite est-elle légitime ? | allure du nuage, puis ρ_XY = cov/(σ_X σ_Y) comparé à √3/2 ≈ 0,866            |
| 5     | Quelle droite ?                | moindres carrés a₀ = cov/σ_X², b₀ = Ȳ − a₀X̄ (ou Mayer si l'énoncé l'impose)  |
| 6     | Vérification                   | la droite passe par G(X̄ ; Ȳ), la somme des écarts yᵢ − zᵢ vaut 0             |
| 7     | Le nuage est courbe ?          | changement de variable (Z = ln Y, Z = √Y…), ajuster (X, Z), puis revenir à Y |

> 🏆 Dix-septième et dernière porte, héros. Tu sais tirer deux séries d'un tableau double, mesurer leur lien par la covariance puis par la corrélation, tracer la droite qui minimise vraiment l'erreur et la contrôler en la faisant passer par G, puis redresser un nuage courbe par un changement de variable. Le manuel s'arrête ici : de la continuité du premier chapitre jusqu'à ce nuage de points, tu tiens le programme entier. Il ne reste qu'à t'en servir.
