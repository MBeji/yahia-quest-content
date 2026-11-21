# ⚔️ Statistiques — lire les nombres pour comprendre ce qu'ils taisent

> 💡 «Un nombre seul ne dit presque rien : la moyenne cache des écarts, la médiane cache une moitié, un taux cache ses proportions. Apprends à lire ce qu'ils taisent.»

Jusqu'ici, tu as calculé des valeurs exactes. Ici, on part d'une foule de données et l'on cherche des nombres qui la résument : où est le milieu, quelle est la dispersion, comment suivre une évolution, comment ne pas se laisser tromper par une proportion.
Huit étapes t'y conduisent : le vocabulaire, les séries chronologiques, la médiane, les quartiles, les séries regroupées en classes, la moyenne, la variance et l'écart type, l'effet de structure.

## 🧭 Lire une série : population, caractère, effectif et fréquence

La médecine scolaire examine 60 des 400 internes d'un lycée : pour chacun, elle note l'âge, la taille et le groupe sanguin.
Ces 60 fiches sont des données brutes. Comment les résumer, et comment comparer ce lycée à un autre où l'on aurait examiné 90 internes ?

::: definition
La **population** est l'ensemble des individus que l'étude concerne (ici les 400 internes) ; l'**échantillon** est la partie réellement observée (ici 60 internes), et sa **taille** est n = 60. Ce que l'on note sur chaque individu est le **caractère** ; chaque valeur possible du caractère est une **modalité**.
Le caractère est **qualitatif** quand ses modalités sont des mots (le groupe sanguin). Il est **quantitatif** quand ce sont des nombres : **discret** s'il ne prend que des valeurs isolées (l'âge en années), **continu** s'il peut prendre toutes les valeurs d'un intervalle (la taille), que l'on regroupe alors en **classes** [a ; b[.
L'**effectif** nᵢ d'une valeur (ou d'une classe) est le nombre d'individus qui la portent ; sa **fréquence** est fᵢ = nᵢ / n.
:::

::: figure Diagramme en bâtons des âges des 60 internes : la hauteur de chaque bâton est l'effectif de la valeur, 27 pour 17 ans, et les cinq hauteurs totalisent 60
<svg viewBox="0 0 300 200"><title>Diagramme en bâtons des âges des 60 internes</title><path d="M38 168 H284 M38 143 H284 M38 118 H284 M38 93 H284 M38 68 H284 M38 43 H284 M38 18 H284" fill="none" stroke="#94a3b8" stroke-width="0.8" opacity="0.55"/><path d="M38 168 H288 M38 168 V12" fill="none" stroke="#0f172a" stroke-width="1.8"/><path d="M286 164.5 L292 168 L286 171.5 Z M34.5 14 L38 8 L41.5 14 Z" fill="#0f172a"/><text x="32" y="172" font-size="11" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">0</text><text x="32" y="147" font-size="11" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">5</text><text x="32" y="122" font-size="11" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">10</text><text x="32" y="97" font-size="11" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">15</text><text x="32" y="72" font-size="11" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">20</text><text x="32" y="47" font-size="11" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">25</text><text x="32" y="22" font-size="11" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">30</text><path d="M62.6 168 L62.6 93" fill="none" stroke="#0f6e56" stroke-width="6" stroke-linecap="butt"/><text x="62.6" y="88" font-size="11" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">15</text><text x="62.6" y="182" font-size="11" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">16</text><path d="M111.8 168 L111.8 33" fill="none" stroke="#0f6e56" stroke-width="6" stroke-linecap="butt"/><text x="111.8" y="28" font-size="11" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">27</text><text x="111.8" y="182" font-size="11" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">17</text><path d="M161 168 L161 108" fill="none" stroke="#0f6e56" stroke-width="6" stroke-linecap="butt"/><text x="161" y="103" font-size="11" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">12</text><text x="161" y="182" font-size="11" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">18</text><path d="M210.2 168 L210.2 148" fill="none" stroke="#0f6e56" stroke-width="6" stroke-linecap="butt"/><text x="210.2" y="143" font-size="11" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">4</text><text x="210.2" y="182" font-size="11" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">19</text><path d="M259.4 168 L259.4 158" fill="none" stroke="#0f6e56" stroke-width="6" stroke-linecap="butt"/><text x="259.4" y="153" font-size="11" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">2</text><text x="259.4" y="182" font-size="11" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">20</text><text x="161" y="196" font-size="11" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">âge (ans)</text><text x="42" y="10" font-size="11" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">effectif</text></svg>
:::

Sur la figure, un bâton est une valeur du caractère et sa hauteur est l'effectif nᵢ de cette valeur. Pour une taille, caractère continu, on trace un histogramme.

::: figure Histogramme des tailles des 60 internes : chaque rectangle est une classe de 5 cm, et comme toutes les classes ont la même amplitude, la hauteur se lit directement comme l'effectif
<svg viewBox="0 0 320 210"><title>Histogramme des tailles des 60 internes</title><path d="M38 178 H304 M38 151.33 H304 M38 124.67 H304 M38 98 H304 M38 71.33 H304 M38 44.67 H304 M38 18 H304" fill="none" stroke="#94a3b8" stroke-width="0.8" opacity="0.55"/><path d="M38 178 H308 M38 178 V12" fill="none" stroke="#0f172a" stroke-width="1.8"/><path d="M306 174.5 L312 178 L306 181.5 Z M34.5 14 L38 8 L41.5 14 Z" fill="#0f172a"/><text x="32" y="182" font-size="11" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">0</text><text x="32" y="155.33" font-size="11" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">4</text><text x="32" y="128.67" font-size="11" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">8</text><text x="32" y="102" font-size="11" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">12</text><text x="32" y="75.33" font-size="11" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">16</text><text x="32" y="48.67" font-size="11" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">20</text><text x="32" y="22" font-size="11" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">24</text><path d="M38 178 V138 H91.2 V178" fill="#0f6e56" fill-opacity="0.18" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round"/><text x="64.6" y="133" font-size="11" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">6</text><path d="M91.2 178 V78 H144.4 V178" fill="#0f6e56" fill-opacity="0.18" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round"/><text x="117.8" y="73" font-size="11" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">15</text><path d="M144.4 178 V38 H197.6 V178" fill="#0f6e56" fill-opacity="0.18" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round"/><text x="171" y="33" font-size="11" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">21</text><path d="M197.6 178 V98 H250.8 V178" fill="#0f6e56" fill-opacity="0.18" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round"/><text x="224.2" y="93" font-size="11" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">12</text><path d="M250.8 178 V138 H304 V178" fill="#0f6e56" fill-opacity="0.18" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round"/><text x="277.4" y="133" font-size="11" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">6</text><text x="38" y="192" font-size="11" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">150</text><text x="91.2" y="192" font-size="11" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">155</text><text x="144.4" y="192" font-size="11" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">160</text><text x="197.6" y="192" font-size="11" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">165</text><text x="250.8" y="192" font-size="11" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">170</text><text x="304" y="192" font-size="11" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">175</text><text x="171" y="206" font-size="11" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">taille (cm)</text><text x="42" y="10" font-size="11" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">effectif</text></svg>
:::

Sur la figure, la classe [160 ; 165[ contient 21 internes : elle comprend 160 cm mais pas 165 cm, qui appartient à la classe suivante.

::: exemple Les internes, âge par âge

1. Effectif total : 15 + 27 + 12 + 4 + 2 = 60, car on additionne les effectifs de toutes les valeurs.
2. Fréquence des 17 ans : 27 / 60 = 0,45, soit 45 %, car on rapporte l'effectif à la taille de l'échantillon.
3. Part des internes de moins de 18 ans : (15 + 27) / 60 = 42 / 60 = 0,70, soit 70 %, car on regroupe d'abord les âges 16 et 17 ans, puis on divise.
4. Contrôle : les fréquences 25 %, 45 %, 20 %, 6,7 % et 3,3 % totalisent 100 %, comme il se doit.

:::

::: piege Dire que la fréquence des 17 ans est 27
Un élève lit 27 sur le bâton et écrit « la fréquence des 17 ans est 27 ». Cela tente parce que 27 est bien le nombre affiché sur la figure.
Mais 27 est l'effectif. La fréquence compare cet effectif au total : 27 / 60 = 0,45. Une fréquence est un nombre compris entre 0 et 1, et les fréquences d'une série totalisent 1.
:::

::: propriete

- Les effectifs totalisent n, et les fréquences totalisent 1 (ou 100 %).
- Une fréquence est un rapport à la taille de l'échantillon : c'est elle, et non l'effectif, qui permet de comparer deux échantillons de tailles différentes.
- Un caractère qualitatif se représente souvent par un diagramme circulaire (ou à barres) ; un caractère discret par un diagramme en bâtons ; un caractère continu par un histogramme.

Cas limite : une modalité d'effectif nul, comme le groupe AB− absent de l'échantillon, a une fréquence nulle et reste pourtant une modalité possible.
:::

::: verifie
Parmi les 60 internes, 4 ont 19 ans et 2 ont 20 ans. Quelle est la fréquence, en pourcentage, des internes qui ont au moins 19 ans ?

---

Il faut regrouper les deux valeurs concernées : 4 + 2 = 6 internes. On rapporte cet effectif à la taille de l'échantillon : 6 / 60 = 0,10, soit 10 %. On ne divise pas par 400, la population, car les 60 fiches sont les seules données observées.
:::

::: retenir
Une fréquence est un effectif divisé par la taille de l'échantillon ; c'est ce rapport, et non l'effectif brut, qui permet de comparer des échantillons de tailles différentes.
:::

## 📈 Suivre une évolution : coefficient multiplicateur et indice

La récolte de blé dur en Tunisie est de 897 milliers de tonnes en 1990 et de 1 323 en 1992. Un journal titre « la récolte a augmenté de 47 % », un autre « la récolte atteint 147 % de celle de 1990 ».
Disent-ils la même chose ? Et comment suivre une série d'années sans se perdre dans les milliers de tonnes ?

::: definition
Une **série chronologique** donne les valeurs d'une même grandeur relevées à des instants régulièrement espacés. On choisit une année de **base**, de valeur v₀. Pour une année de valeur v, le **coefficient multiplicateur** est c = v / v₀, et l'**indice** (base 100) est 100 × c.
La courbe qui relie les points (année ; indice) est la **courbe d'évolution**.
:::

| Année                                            | 1990 | 1992  | 1994 | 1996  | 1998  | 2000 | 2002 |
| ------------------------------------------------ | ---- | ----- | ---- | ----- | ----- | ---- | ---- |
| Production (milliers de tonnes)                  | 897  | 1 323 | 436  | 1 706 | 1 090 | 706  | 371  |
| Coefficient multiplicateur (arrondi au centième) | 1    | 1,47  | 0,49 | 1,90  | 1,22  | 0,79 | 0,41 |
| Indice                                           | 100  | 147   | 49   | 190   | 122   | 79   | 41   |

::: figure Courbe d'évolution de l'indice du blé dur, base 100 en 1990 : la droite pointillée marque la base, et un point situé au-dessus d'elle correspond à une production supérieure à celle de 1990
<svg viewBox="0 0 340 210"><title>Courbe d'évolution de l'indice de la production de blé dur</title><path d="M40 178 H322 M40 138 H322 M40 98 H322 M40 58 H322 M40 18 H322" fill="none" stroke="#94a3b8" stroke-width="0.8" opacity="0.55"/><path d="M40 178 H326 M40 178 V12" fill="none" stroke="#0f172a" stroke-width="1.8"/><path d="M324 174.5 L330 178 L324 181.5 Z M36.5 14 L40 8 L43.5 14 Z" fill="#0f172a"/><text x="34" y="182" font-size="11" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">0</text><text x="34" y="142" font-size="11" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">50</text><text x="34" y="102" font-size="11" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">100</text><text x="34" y="62" font-size="11" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">150</text><text x="34" y="22" font-size="11" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">200</text><path d="M40 98 L322 98" fill="none" stroke="#b45309" stroke-width="1.4" stroke-linecap="round" stroke-dasharray="5 4"/><path d="M56.59 98 L98.06 60.4 L139.53 138.8 L181 26 L222.47 80.4 L263.94 114.8 L305.41 145.2" fill="none" stroke="#0f6e56" stroke-width="2.4" stroke-linejoin="round" stroke-linecap="round"/><circle cx="56.59" cy="98" r="3.6" fill="#0f6e56"/><circle cx="98.06" cy="60.4" r="3.6" fill="#0f6e56"/><circle cx="139.53" cy="138.8" r="3.6" fill="#0f6e56"/><circle cx="181" cy="26" r="3.6" fill="#0f6e56"/><circle cx="222.47" cy="80.4" r="3.6" fill="#0f6e56"/><circle cx="263.94" cy="114.8" r="3.6" fill="#0f6e56"/><circle cx="305.41" cy="145.2" r="3.6" fill="#0f6e56"/><text x="56.59" y="192" font-size="11" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">1990</text><text x="98.06" y="192" font-size="11" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">1992</text><text x="139.53" y="192" font-size="11" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">1994</text><text x="181" y="192" font-size="11" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">1996</text><text x="222.47" y="192" font-size="11" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">1998</text><text x="263.94" y="192" font-size="11" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">2000</text><text x="305.41" y="192" font-size="11" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">2002</text><text x="56.59" y="91" font-size="10" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">100</text><text x="98.06" y="53.4" font-size="10" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">147</text><text x="149.53" y="154.8" font-size="10" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">49</text><text x="181" y="19" font-size="10" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">190</text><text x="222.47" y="73.4" font-size="10" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">122</text><text x="263.94" y="107.8" font-size="10" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">79</text><text x="305.41" y="138.2" font-size="10" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">41</text><text x="181" y="206" font-size="11" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">année</text><text x="44" y="10" font-size="11" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">indice</text></svg>
:::

Sur la figure, l'ordonnée d'un point est l'indice du tableau : le point de 1992 est à 147, celui de 2002 à 41.

::: exemple Lire le tableau du blé dur

1. Année de base : 1990, donc c = 897 / 897 = 1 et l'indice vaut 100, car la base se compare à elle-même.
2. Année 1992 : c = 1 323 / 897 ≈ 1,47 et l'indice vaut 147, car on divise la valeur de l'année par la valeur de base.
3. Lecture : 147 − 100 = 47, la production de 1992 dépasse celle de 1990 d'environ 47 %. Le premier journal dit donc « +47 % » et le second « 147 % de la base » : les deux disent la même chose.
4. Année 2002 : c = 371 / 897 ≈ 0,41, indice 41, soit 100 − 41 = 59 % de moins qu'en 1990, environ.

:::

::: piege Lire l'indice 147 comme une hausse de 147 %
Un élève voit 147 sur la courbe et écrit « la production a augmenté de 147 % ». Cela tente parce que 147 est un grand nombre, apparemment une forte hausse.
Mais l'indice compare à une base de 100 : 147 signifie « 147 pour 100 de la base », donc 47 de plus. La hausse est de 147 − 100 = 47 %.
:::

::: propriete

- Coefficient multiplicateur : c = v / v₀ (valeur de l'année divisée par valeur de base).
- Indice : 100 × c ; l'année de base a l'indice 100.
- Un indice supérieur à 100 indique une hausse par rapport à la base, un indice inférieur à 100 une baisse : l'écart avec 100 donne le pourcentage de variation.

Cas limite : c'est la valeur de base qui est au dénominateur. En 2002, le quotient inverse 897 / 371 ≈ 2,42 serait un coefficient « à l'envers », qui dirait que la production a plus que doublé alors qu'elle a baissé.
:::

::: verifie
La production d'orge est de 477 milliers de tonnes en 1990 (base) et de 145 en 1994. Calculer le coefficient multiplicateur au centième, l'indice, et la variation par rapport à 1990.

---

On divise la valeur de l'année par la base : c = 145 / 477 ≈ 0,30, donc l'indice vaut 30. Comme 30 est inférieur à 100, c'est une baisse, de 100 − 30 = 70 % par rapport à 1990.
:::

::: retenir
Le coefficient multiplicateur est la valeur de l'année divisée par la valeur de base, et l'indice vaut 100 fois ce coefficient : l'écart entre l'indice et 100 donne le pourcentage de variation depuis la base.
:::

## 🎯 Mode et médiane d'une série discrète

Dans une classe de 21 élèves, le professeur veut annoncer une note « du milieu » : celle qui coupe la classe en deux groupes de même effectif. Ce n'est pas la note la plus fréquente, et pas forcément la moyenne.
Comment la trouver sans recopier les 21 notes dans l'ordre ?

::: definition
Le **mode** est la valeur dont l'effectif est le plus grand. La **médiane** m est la valeur qui partage la série, rangée par ordre croissant, en deux groupes de même effectif.
L'**effectif cumulé croissant** d'une valeur est la somme des effectifs de cette valeur et de toutes les valeurs plus petites.
:::

| Note                      | 8   | 10  | 11  | 12  | 13  | 16  | 18  |
| ------------------------- | --- | --- | --- | --- | --- | --- | --- |
| Effectif                  | 2   | 6   | 3   | 2   | 2   | 4   | 2   |
| Effectif cumulé croissant | 2   | 8   | 11  | 13  | 15  | 19  | 21  |

La dernière ligne se lit ainsi : 11 élèves ont une note inférieure ou égale à 11.

::: exemple La médiane de la classe de 21 élèves

1. L'effectif total est 21, un nombre impair. La médiane est la valeur de rang (21 + 1) / 2 = 11, car il y a alors 10 valeurs avant elle et 10 après.
2. On cherche la première note dont le cumul atteint au moins 11 : la note 10 s'arrête à 8, la note 11 monte à 11. La 11ᵉ valeur est donc 11, car les rangs 9, 10 et 11 sont occupés par la note 11.
3. La médiane est m = 11 : au moins la moitié des élèves a 11 ou moins, et au moins la moitié a 11 ou plus.
4. Le mode est la note d'effectif 6, soit 10. Mode et médiane répondent à deux questions différentes : « laquelle est la plus fréquente ? » et « laquelle coupe la classe en deux ? ».

:::

::: piege Prendre la valeur du milieu du tableau
Un élève compte 7 notes différentes dans le tableau et choisit la quatrième, 12. Cela tente parce qu'elle est au milieu de la ligne des notes.
Mais chaque note compte autant de fois que son effectif : la note 12 n'occupe que les rangs 12 et 13, alors que la médiane est au rang 11. On place la médiane avec les effectifs cumulés, jamais avec le nombre de colonnes du tableau.
:::

::: propriete

- Effectif total n impair : la médiane est la valeur de rang (n + 1) / 2.
- Effectif total n pair : les valeurs de rang n / 2 et n / 2 + 1 encadrent la médiane, qui est leur moyenne.
- Une série peut avoir plusieurs modes, et la médiane d'une série d'effectif pair n'est pas forcément l'une de ses valeurs.

Cas limite : avec 6 notes dont les deux valeurs centrales sont 8 et 13, la médiane est 10,5, un nombre qui n'est la note de personne.
:::

::: verifie
Huit élèves ont obtenu les notes 7, 12, 9, 12, 15, 9, 10 et 16. Quelle est leur médiane ?

---

On range d'abord : 7, 9, 9, 10, 12, 12, 15, 16. L'effectif 8 est pair, donc les rangs 4 et 5 encadrent la médiane : ce sont les notes 10 et 12. La médiane est leur moyenne, (10 + 12) / 2 = 11.
:::

::: retenir
La médiane se lit sur la série rangée, avec les effectifs cumulés : au rang (n + 1) / 2 si n est impair, à la moyenne des rangs n / 2 et n / 2 + 1 si n est pair.
:::

## 📦 Quartiles et diagramme en boîte

Deux groupes A et B de 20 élèves ont la même médiane à un devoir : 10. Pourtant le professeur affirme que A est homogène et que B est étalé.
Quel nombre, autre que la médiane, permet de le prouver ? Et comment le montrer sur un dessin ?

::: definition
Le **premier quartile** Q₁ est la plus petite valeur de la série telle qu'au moins 25 % de l'effectif lui soit inférieur ou égal ; le **troisième quartile** Q₃ est la plus petite valeur telle qu'au moins 75 % de l'effectif lui soit inférieur ou égal. Le deuxième quartile Q₂ est la médiane.
L'**intervalle interquartile** est [Q₁ ; Q₃] et l'**écart interquartile** est Q₃ − Q₁. L'**étendue** est la différence entre la plus grande et la plus petite valeur.
Un **diagramme en boîte** est un rectangle allant de Q₁ à Q₃, coupé d'un trait à la médiane, prolongé par deux segments jusqu'aux valeurs extrêmes.
:::

| Note du groupe B          | 4   | 6   | 8   | 10  | 12  | 14  | 16  | 18  |
| ------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| Effectif                  | 2   | 2   | 2   | 6   | 3   | 2   | 2   | 1   |
| Effectif cumulé croissant | 2   | 4   | 6   | 12  | 15  | 17  | 19  | 20  |

::: exemple Les quartiles du groupe B

1. L'effectif est 20 et 25 % de 20 font 5. Q₁ est la première note dont le cumul atteint au moins 5, car c'est la plus petite valeur qui rassemble au moins un quart de la classe.
2. Le cumul vaut 4 à la note 6, donc pas assez, puis 6 à la note 8 : Q₁ = 8.
3. Pour 75 %, il faut 15 élèves. Le cumul vaut 12 à la note 10, puis 15 à la note 12 : Q₃ = 12.
4. L'écart interquartile est 12 − 8 = 4, et l'étendue est 18 − 4 = 14.

:::

Le groupe A, de notes plus resserrées, a pour valeurs extrêmes 7 et 14, pour quartiles Q₁ = 9 et Q₃ = 11, et pour médiane 10.

::: figure Diagrammes en boîte des groupes A et B, sur la même graduation : les deux traits de médiane sont au même endroit, 10, mais la boîte de B est deux fois plus longue que celle de A
<svg viewBox="0 0 330 160"><title>Diagrammes en boîte des groupes A et B</title><path d="M44 14 V130 M74 14 V130 M104 14 V130 M134 14 V130 M164 14 V130 M194 14 V130 M224 14 V130 M254 14 V130 M284 14 V130 M314 14 V130" fill="none" stroke="#94a3b8" stroke-width="0.8" opacity="0.55"/><path d="M44 130 L318 130" fill="none" stroke="#0f172a" stroke-width="1.8" stroke-linecap="round"/><text x="44" y="144" font-size="11" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">2</text><text x="74" y="144" font-size="11" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">4</text><text x="104" y="144" font-size="11" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">6</text><text x="134" y="144" font-size="11" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">8</text><text x="164" y="144" font-size="11" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">10</text><text x="194" y="144" font-size="11" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">12</text><text x="224" y="144" font-size="11" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">14</text><text x="254" y="144" font-size="11" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">16</text><text x="284" y="144" font-size="11" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">18</text><text x="314" y="144" font-size="11" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">20</text><path d="M119 48 L149 48" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round"/><path d="M179 48 L224 48" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round"/><path d="M119 40 L119 56" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round"/><path d="M224 40 L224 56" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round"/><path d="M149 36 H179 V60 H149 Z" fill="#0f6e56" fill-opacity="0.18" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><path d="M164 36 L164 60" fill="none" stroke="#b45309" stroke-width="3" stroke-linecap="butt"/><text x="36" y="52" font-size="11" text-anchor="end" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">A</text><path d="M74 100 L134 100" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round"/><path d="M194 100 L284 100" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round"/><path d="M74 92 L74 108" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round"/><path d="M284 92 L284 108" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round"/><path d="M134 88 H194 V112 H134 Z" fill="#0f6e56" fill-opacity="0.18" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><path d="M164 88 L164 112" fill="none" stroke="#b45309" stroke-width="3" stroke-linecap="butt"/><text x="36" y="104" font-size="11" text-anchor="end" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">B</text><text x="179" y="157" font-size="11" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">note sur 20</text></svg>
:::

Sur la figure, la longueur de la boîte est l'écart interquartile : 2 pour A, 4 pour B. C'est elle, et non la médiane, qui distingue les deux groupes.

::: piege Écrire Q₁ = 5 parce que 25 % de 20 font 5
Un élève calcule 20 × 0,25 = 5 et annonce « Q₁ = 5 ». Cela tente parce que le calcul est exact et que le nombre 5 sort du bon produit.
Mais 5 est un rang, pas une note : c'est la place de la valeur cherchée dans la série rangée. Le quartile est la note qui occupe ce rang, ici 8 pour le groupe B.
:::

::: propriete

- Au moins 25 % de l'effectif est inférieur ou égal à Q₁, et au moins 75 % est inférieur ou égal à Q₃.
- L'intervalle [Q₁ ; Q₃] contient au moins la moitié des valeurs : c'est la partie centrale de la série.
- L'écart interquartile mesure la dispersion de cette partie centrale, alors que l'étendue dépend des deux valeurs extrêmes seules.

Cas limite : si 25 % de n n'est pas entier, par exemple 2,25 pour n = 9, on prend la première valeur dont le cumul atteint au moins ce nombre, ici la 3ᵉ. Si la plus grande valeur d'une série est remplacée par une valeur encore plus éloignée, l'étendue augmente mais Q₁ et Q₃ ne bougent pas : pour B, Q₁ = 8 et Q₃ = 12 resteraient les mêmes.
:::

::: verifie
Une série de 24 notes a pour effectifs : note 5, effectif 2 ; note 7, 4 ; note 9, 5 ; note 10, 5 ; note 12, 4 ; note 14, 3 ; note 16, 1. Calculer Q₁, Q₃ et l'écart interquartile.

---

Les effectifs cumulés sont 2, 6, 11, 16, 20, 23, 24. Pour Q₁, 25 % de 24 font 6 : le cumul atteint 6 à la note 7, donc Q₁ = 7. Pour Q₃, 75 % de 24 font 18 : le cumul vaut 16 à la note 10, puis 20 à la note 12, donc Q₃ = 12. L'écart interquartile est 12 − 7 = 5.
:::

::: retenir
Q₁ et Q₃ sont les plus petites valeurs dont le cumul atteint 25 % et 75 % de l'effectif ; l'écart interquartile Q₃ − Q₁ mesure la dispersion de la partie centrale, et la boîte le dessine.
:::

## ✂️ Séries regroupées en classes : médiane et quartiles par interpolation

La direction d'une entreprise a relevé le temps de transport quotidien de 200 salariés, regroupé en classes de 20 minutes. Les durées individuelles ne sont plus connues : on sait seulement combien de salariés sont dans chaque classe.
Où se trouve la médiane, alors que l'on ne peut plus ranger les valeurs ?

::: definition
Quand une série est regroupée en classes [a ; b[, on suppose les valeurs **régulièrement réparties** dans chaque classe : c'est l'**interpolation linéaire**. La médiane est alors le nombre m pour lequel l'effectif cumulé atteint N / 2, où N est l'effectif total ; Q₁ et Q₃ correspondent à N / 4 et 3N / 4.
:::

| Temps (min)               | [20 ; 40[ | [40 ; 60[ | [60 ; 80[ | [80 ; 100[ | [100 ; 120[ | [120 ; 140[ |
| ------------------------- | --------- | --------- | --------- | ---------- | ----------- | ----------- |
| Effectif                  | 10        | 25        | 50        | 60         | 50          | 5           |
| Effectif cumulé croissant | 10        | 35        | 85        | 145        | 195         | 200         |

::: figure Polygone des effectifs cumulés croissants : en orange, la droite d'ordonnée 100 coupe la courbe au point d'abscisse m, donc la moitié des 200 salariés a un temps inférieur à m
<svg viewBox="0 0 330 230"><title>Polygone des effectifs cumulés croissants des temps de transport</title><path d="M42 198 H312 M42 153 H312 M42 108 H312 M42 63 H312 M42 18 H312" fill="none" stroke="#94a3b8" stroke-width="0.8" opacity="0.55"/><path d="M42 198 H316 M42 198 V12" fill="none" stroke="#0f172a" stroke-width="1.8"/><path d="M314 194.5 L320 198 L314 201.5 Z M38.5 14 L42 8 L45.5 14 Z" fill="#0f172a"/><text x="36" y="202" font-size="11" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">0</text><text x="36" y="157" font-size="11" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">50</text><text x="36" y="112" font-size="11" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">100</text><text x="36" y="67" font-size="11" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">150</text><text x="36" y="22" font-size="11" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">200</text><path d="M42 198 L87 189 L132 166.5 L177 121.5 L222 67.5 L267 22.5 L312 18" fill="none" stroke="#0f6e56" stroke-width="2.4" stroke-linejoin="round"/><circle cx="42" cy="198" r="3.2" fill="#0f6e56"/><circle cx="87" cy="189" r="3.2" fill="#0f6e56"/><circle cx="132" cy="166.5" r="3.2" fill="#0f6e56"/><circle cx="177" cy="121.5" r="3.2" fill="#0f6e56"/><circle cx="222" cy="67.5" r="3.2" fill="#0f6e56"/><circle cx="267" cy="22.5" r="3.2" fill="#0f6e56"/><circle cx="312" cy="18" r="3.2" fill="#0f6e56"/><text x="42" y="212" font-size="11" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">20</text><text x="87" y="212" font-size="11" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">40</text><text x="132" y="212" font-size="11" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">60</text><text x="177" y="212" font-size="11" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">80</text><text x="222" y="212" font-size="11" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">100</text><text x="267" y="212" font-size="11" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">120</text><text x="312" y="212" font-size="11" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">140</text><path d="M42 108 L188.25 108" fill="none" stroke="#b45309" stroke-width="1.5" stroke-linecap="round" stroke-dasharray="5 4"/><path d="M188.25 108 L188.25 198" fill="none" stroke="#b45309" stroke-width="1.5" stroke-linecap="round" stroke-dasharray="5 4"/><circle cx="188.25" cy="108" r="4" fill="#b45309"/><text x="195.25" y="192" font-size="11" text-anchor="start" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">m = 85</text><text x="46" y="103" font-size="11" text-anchor="start" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">100</text><text x="177" y="226" font-size="11" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">temps de transport (min)</text><text x="46" y="10" font-size="11" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">effectif cumulé</text></svg>
:::

Sur la figure, la partie de la courbe entre les abscisses 80 et 100 est un segment de droite, parce que les valeurs y sont supposées régulièrement réparties : c'est ce segment qui sert à interpoler.

::: exemple La médiane et le premier quartile des temps de transport

1. N / 2 = 100. Les cumuls 85 puis 145 encadrent 100, donc la médiane est dans la classe [80 ; 100[, de borne inférieure 80 et d'amplitude 20.
2. Il manque 100 − 85 = 15 salariés sur les 60 de cette classe, soit un quart : on avance donc d'un quart de l'amplitude, car les valeurs sont réparties régulièrement.
3. m = 80 + (15 / 60) × 20 = 80 + 5 = 85 minutes.
4. Pour Q₁, N / 4 = 50 : les cumuls 35 puis 85 encadrent 50, donc Q₁ est dans [60 ; 80[ et Q₁ = 60 + (50 − 35) / 50 × 20 = 60 + 6 = 66 minutes.

:::

::: piege Donner le centre de la classe médiane
Un élève repère la classe [80 ; 100[ et répond « m = 90 », son centre. Cela tente parce que la classe médiane est bien celle-là.
Mais le centre supposerait que la moitié des 60 salariés de la classe soit en dessous. Il n'en faut que 15 pour atteindre 100 : la médiane est plus basse, à 85.
:::

::: propriete
Si [a ; b[ est la classe où le cumul atteint le rang cherché, c l'effectif cumulé en a et n_c l'effectif de cette classe :

$$ m = a + (N / 2 − c) / n_c × (b − a) $$

Pour Q₁ on remplace N / 2 par N / 4, pour Q₃ par 3N / 4.

Cas limite : si le cumul vaut exactement N / 2 à une borne, la médiane est cette borne, sans interpolation. Pour une série en classes, la **classe modale** est la classe d'effectif maximal, ici [80 ; 100[.
:::

::: verifie
Avec le même tableau, calculer le troisième quartile Q₃.

---

3N / 4 = 150. Les cumuls 145 puis 195 encadrent 150 : Q₃ est dans la classe [100 ; 120[, de borne 100, d'effectif 50 et d'amplitude 20. Il manque 150 − 145 = 5 salariés sur 50, soit un dixième de l'amplitude : Q₃ = 100 + (5 / 50) × 20 = 102 minutes.
:::

::: retenir
Dans une série regroupée en classes, on trouve la classe où le cumul atteint N / 2, N / 4 ou 3N / 4, puis on interpole : borne inférieure plus la fraction d'effectif manquante multipliée par l'amplitude.
:::

## ⚖️ La moyenne et ses propriétés

La direction veut maintenant le temps de transport moyen des mêmes 200 salariés. Mais, dans la première classe, on ignore si les 10 salariés mettent 21 ou 39 minutes.
Quelle valeur attribuer à chaque salarié, et comment pondérer les classes ?

::: definition
La **moyenne** de la série (xᵢ ; nᵢ), d'effectif total n, est :

$$ x̄ = (n₁x₁ + n₂x₂ + … + nₚxₚ) / n $$

Pour une série regroupée en classes, xᵢ est le **centre** de la classe, c'est-à-dire le milieu de ses deux bornes.
:::

| Classe (min) | [20 ; 40[ | [40 ; 60[ | [60 ; 80[ | [80 ; 100[ | [100 ; 120[ | [120 ; 140[ | Total  |
| ------------ | --------- | --------- | --------- | ---------- | ----------- | ----------- | ------ |
| Centre xᵢ    | 30        | 50        | 70        | 90         | 110         | 130         |        |
| Effectif nᵢ  | 10        | 25        | 50        | 60         | 50          | 5           | 200    |
| Produit nᵢxᵢ | 300       | 1 250     | 3 500     | 5 400      | 5 500       | 650         | 16 600 |

::: exemple Le temps moyen de transport

1. On remplace chaque classe par son centre : [20 ; 40[ devient 30, [40 ; 60[ devient 50, et ainsi de suite, car le centre représente au mieux une classe dont on ignore le détail.
2. On pondère par les effectifs : 10 × 30 = 300 pour la première classe, 25 × 50 = 1 250 pour la deuxième, etc., car une classe de 60 salariés pèse plus qu'une classe de 5.
3. La somme des produits est 16 600, et on divise par l'effectif total : 16 600 / 200 = 83 minutes.
4. La moyenne 83 et la médiane 85 sont proches mais différentes : la moyenne tient compte de toutes les valeurs, la médiane partage l'effectif en deux.

:::

::: piege Faire la moyenne des centres sans les effectifs
Un élève additionne les six centres et divise par 6 : (30 + 50 + 70 + 90 + 110 + 130) / 6 = 80. Cela tente parce qu'on obtient un nombre plausible, au milieu des classes.
Mais cette moyenne traite une classe de 5 salariés comme une classe de 60. Chaque centre doit être multiplié par son effectif, puis on divise par 200 : le résultat est 83.
:::

::: propriete

- **Moyennes partielles.** Si une série est coupée en deux séries d'effectifs p et q, de moyennes x̄ et ȳ, la moyenne de l'ensemble est z̄ = (p x̄ + q ȳ) / (p + q).
- **Transformation affine.** Si x̄ est la moyenne de la série (xᵢ ; nᵢ), alors la série (a xᵢ + b ; nᵢ) a pour moyenne a x̄ + b.

Cas limite : la moyenne simple (x̄ + ȳ) / 2 ne donne la moyenne de l'ensemble que si les deux groupes ont le même effectif ou la même moyenne.
:::

::: exemple Filles, garçons, puis changement de barème

1. Une classe de 30 élèves compte 18 filles de moyenne 11,5 et 12 garçons de moyenne 9,5. Pour la classe : z̄ = (18 × 11,5 + 12 × 9,5) / 30 = (207 + 114) / 30 = 10,7, car chaque moyenne est pondérée par l'effectif de son groupe.
2. Le professeur ajoute 1 point à chaque note, puis divise par 2 pour ramener à une note sur 10 : y = 0,5x + 0,5, donc a = 0,5 et b = 0,5.
3. La nouvelle moyenne est 0,5 × 10,7 + 0,5 = 5,85, sans recalculer les 30 notes, parce que la moyenne suit la transformation affine.

:::

> 🗡️ Une valeur isolée tire la moyenne vers elle. Cinq pesées d'un colis donnent 9,8 ; 10,1 ; 10,0 ; 10,2 et 14,9 kg : la moyenne est 11,0 kg. En écartant la plus petite et la plus grande valeur, la **moyenne élaguée** des trois restantes vaut 10,1 kg, bien plus représentative du colis.

::: verifie
Dans un groupe, 25 élèves ont une moyenne de 12 et 15 autres élèves une moyenne de 8. Quelle est la moyenne des 40 élèves ?

---

On pondère chaque moyenne par l'effectif de son groupe : (25 × 12 + 15 × 8) / 40 = (300 + 120) / 40 = 420 / 40 = 10,5. On ne fait pas (12 + 8) / 2 = 10, car le groupe des 25 compte davantage que celui des 15.
:::

::: retenir
La moyenne est la somme des produits effectif × valeur, divisée par l'effectif total, avec les centres pour des classes ; elle se pondère pour des groupes et suit toute transformation affine : a x̄ + b.
:::

## 📏 Variance et écart type : mesurer la dispersion

Deux villes A et B ont relevé la température à midi pendant 10 jours : la moyenne est 12 °C dans les deux. Pourtant A passe de 6 à 15 °C quand B reste voisine de 12 °C.
La moyenne ne voit pas cette différence : quel nombre mesure l'étalement des valeurs autour de la moyenne ?

::: definition
La **variance** d'une série (xᵢ ; nᵢ), de moyenne x̄ et d'effectif total n, est :

$$ V = (n₁x₁² + n₂x₂² + … + nₚxₚ²) / n − x̄² $$

L'**écart type** est σ = √V. Pour une série en classes, xᵢ est le centre de la classe. La variance est la moyenne des carrés des écarts à la moyenne.
:::

::: figure Les températures des deux villes sur la même graduation : même moyenne 12 °C, représentée par le trait pointillé, mais les valeurs de A s'écartent beaucoup plus de ce trait que celles de B
<svg viewBox="0 0 340 204"><title>Températures des villes A et B sur 10 jours</title><path d="M229.33 10 L229.33 162" fill="none" stroke="#b45309" stroke-width="1.6" stroke-linecap="round" stroke-dasharray="5 4"/><path d="M40 84 L328 84" fill="none" stroke="#0f172a" stroke-width="1.8" stroke-linecap="round"/><text x="30" y="62" font-size="11" text-anchor="end" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">A</text><path d="M87.33 84 L87.33 71" fill="none" stroke="#0f6e56" stroke-width="7" stroke-linecap="butt"/><text x="87.33" y="67" font-size="10" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">1</text><path d="M158.33 84 L158.33 58" fill="none" stroke="#0f6e56" stroke-width="7" stroke-linecap="butt"/><text x="158.33" y="54" font-size="10" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">2</text><path d="M229.33 84 L229.33 45" fill="none" stroke="#0f6e56" stroke-width="7" stroke-linecap="butt"/><text x="240.33" y="41" font-size="10" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">3</text><path d="M300.33 84 L300.33 32" fill="none" stroke="#0f6e56" stroke-width="7" stroke-linecap="butt"/><text x="300.33" y="28" font-size="10" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">4</text><path d="M40 162 L328 162" fill="none" stroke="#0f172a" stroke-width="1.8" stroke-linecap="round"/><text x="30" y="140" font-size="11" text-anchor="end" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">B</text><path d="M182 162 L182 149" fill="none" stroke="#0f6e56" stroke-width="7" stroke-linecap="butt"/><text x="182" y="145" font-size="10" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">1</text><path d="M205.67 162 L205.67 136" fill="none" stroke="#0f6e56" stroke-width="7" stroke-linecap="butt"/><text x="205.67" y="132" font-size="10" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">2</text><path d="M229.33 162 L229.33 123" fill="none" stroke="#0f6e56" stroke-width="7" stroke-linecap="butt"/><text x="240.33" y="119" font-size="10" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">3</text><path d="M253 162 L253 110" fill="none" stroke="#0f6e56" stroke-width="7" stroke-linecap="butt"/><text x="253" y="106" font-size="10" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">4</text><text x="40" y="176" font-size="11" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">4</text><text x="87.33" y="176" font-size="11" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">6</text><text x="134.67" y="176" font-size="11" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">8</text><text x="182" y="176" font-size="11" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">10</text><text x="229.33" y="176" font-size="11" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">12</text><text x="276.67" y="176" font-size="11" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">14</text><text x="324" y="176" font-size="11" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">16</text><text x="182" y="201" font-size="11" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">température (°C)</text></svg>
:::

Sur la figure, la hauteur de chaque bâton est le nombre de jours : A a un jour à 6 °C, 2 jours à 9 °C, 3 jours à 12 °C et 4 jours à 15 °C, alors que B a des valeurs de 10 à 13 °C.

::: exemple Comparer A et B

1. Pour A, la somme des nᵢxᵢ² est 1 × 36 + 2 × 81 + 3 × 144 + 4 × 225 = 1 530, car on élève chaque température au carré avant de la pondérer.
2. La moyenne des carrés est 1 530 / 10 = 153, et V = 153 − 12² = 153 − 144 = 9. Donc σ = √9 = 3 °C.
3. Pour B : 1 × 100 + 2 × 121 + 3 × 144 + 4 × 169 = 1 450, donc 1 450 / 10 = 145 et V = 145 − 144 = 1, soit σ = 1 °C.
4. Même moyenne, mais σ = 3 pour A et σ = 1 pour B : A est plus dispersée, ce que la moyenne ne montrait pas.

:::

::: piege Oublier de retrancher le carré de la moyenne
Un élève s'arrête à la moyenne des carrés, 153, et annonce σ = √153 ≈ 12,4 °C. Cela tente parce que le calcul de la somme des carrés est long et paraît être le résultat.
Mais il manque le « − x̄² » de la définition. Un écart type de 12,4 °C est de plus supérieur à l'étendue de la série, 15 − 6 = 9 °C : signe d'une erreur. Avec le carré de la moyenne retranché, V = 9 et σ = 3.
:::

::: propriete
Pour la série (a xᵢ + b ; nᵢ), d'écart type σ et de variance V :

$$ σ' = |a| σ $$

$$ V' = a² V $$

- Ajouter un même nombre b à toutes les valeurs ne change pas l'écart type : la série est seulement décalée.
- Multiplier par a multiplie l'écart type par |a| et la variance par a².
- Lecture de proportions : pour A, l'intervalle [x̄ − σ ; x̄ + σ] = [9 ; 15] contient les relevés de 9, 12 et 15 °C, soit 2 + 3 + 4 = 9 jours sur 10, et [x̄ − 2σ ; x̄ + 2σ] = [6 ; 18] les contient tous.

Cas limite : avec a = −1, les valeurs sont retournées mais l'écart type reste σ, car |−1| = 1.
:::

::: verifie
Les relevés de A sont diminués de 3 °C, puis tous multipliés par 2. Quels sont l'écart type et la variance de la nouvelle série ?

---

Retrancher 3 est une translation : l'écart type reste 3. Multiplier par 2 le multiplie par |2| = 2, donc σ' = 6. La variance est multipliée par 2² = 4 : V' = 4 × 9 = 36, ce qui est bien 6².
:::

::: retenir
La variance est la moyenne des carrés moins le carré de la moyenne, et l'écart type est sa racine ; une translation ne change pas σ, un facteur a le multiplie par |a|.
:::

## 🧩 L'effet de structure : quand un taux global trompe

Un lycée constate que son taux de réussite au baccalauréat est passé de 65 % à 57,5 %. Pourtant, les professeurs affirment que chaque catégorie d'élèves a progressé.
Qui a raison, et comment un taux global peut-il baisser quand tous les taux de détail montent ?

::: definition
Quand une population est formée de sous-groupes, le **taux global** est la proportion calculée sur l'ensemble. On parle d'**effet de structure** lorsque la composition de la population, c'est-à-dire les effectifs des sous-groupes, fait varier le taux global autrement que les taux de chaque sous-groupe.
:::

| Candidats au baccalauréat | Année 1 : présentés | Année 1 : admis | Année 1 : taux | Année 2 : présentés | Année 2 : admis | Année 2 : taux |
| ------------------------- | ------------------- | --------------- | -------------- | ------------------- | --------------- | -------------- |
| Non redoublants           | 200                 | 140             | 70 %           | 100                 | 75              | 75 %           |
| Redoublants               | 40                  | 16              | 40 %           | 140                 | 63              | 45 %           |
| Ensemble                  | 240                 | 156             | 65 %           | 240                 | 138             | 57,5 %         |

::: exemple Qui a raison ?

1. Taux global : 156 / 240 = 0,65 en année 1 et 138 / 240 = 0,575 en année 2. Le taux global a baissé de 7,5 points.
2. Par catégorie : 70 % puis 75 % pour les non redoublants, 40 % puis 45 % pour les redoublants. Chaque taux a monté de 5 points.
3. Explication : les redoublants, qui réussissent moins, passent de 40 sur 240 (environ 17 % des candidats) à 140 sur 240 (environ 58 %). Le groupe le moins performant pèse beaucoup plus.
4. Le taux global est une moyenne pondérée des taux : (200 × 0,70 + 40 × 0,40) / 240 = (140 + 16) / 240 = 0,65. Quand les poids changent, il peut baisser même si chaque taux monte.

:::

::: piege Croire que le taux global suit les taux des catégories
Un élève voit que les deux taux montent et conclut que le taux global monte aussi. Cela tente parce qu'une moyenne de deux nombres qui montent tous les deux semble devoir monter aussi.
Mais le taux global dépend aussi des effectifs de chaque catégorie. Ici le taux global baisse de 65 % à 57,5 %, alors que les deux taux montent : la structure a changé entre les deux années.
:::

::: propriete

- Le taux global est la moyenne pondérée des taux des sous-groupes, les poids étant les effectifs des sous-groupes.
- Comparer deux taux globaux est trompeur quand les structures diffèrent beaucoup : on compare alors d'abord groupe par groupe.
- Le taux global n'est la moyenne simple des taux que si les sous-groupes ont le même effectif (ou le même taux) : ici (70 + 40) / 2 = 55 % ne vaut pas 65 %.

Cas limite : si les effectifs des deux sous-groupes ne changent pas d'une année à l'autre, le taux global monte bien quand les deux taux montent.
:::

::: verifie
Au basket, Sami réussit 9 tirs faciles sur 10 et 20 tirs difficiles sur 40. Lina réussit 32 tirs faciles sur 40 et 4 tirs difficiles sur 10. Qui a le meilleur taux de réussite global, et qui a le meilleur taux dans chaque type de tir ?

---

Sami : (9 + 20) / (10 + 40) = 29 / 50 = 58 %. Lina : (32 + 4) / (40 + 10) = 36 / 50 = 72 %. Lina a donc le meilleur taux global. Mais, tir par tir, Sami est meilleur : 90 % contre 80 % aux tirs faciles, 50 % contre 40 % aux tirs difficiles. Lina a pris surtout des tirs faciles : c'est la structure de ses tirs qui améliore son taux global.
:::

::: retenir
Un taux global est une moyenne pondérée par les effectifs des sous-groupes : il peut baisser alors que chaque taux de détail monte, si la composition de la population change.
:::

> 🏆 Quête franchie, héros : tu sais résumer une série par ses effectifs et ses fréquences, suivre une évolution par un indice, placer la médiane et les quartiles, tracer une boîte, interpoler dans des classes, calculer une moyenne, une variance et un écart type, et démasquer un effet de structure. Tu as maintenant de quoi lire un chiffre avec méfiance, et ce sera utile partout où l'on te présente des données.
