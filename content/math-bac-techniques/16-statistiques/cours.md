# ⚔️ Statistiques — du nuage de points à la droite de prévision

> 💡 «Deux mesures sur les mêmes individus en disent plus qu'une seule : il suffit de savoir lire ce qui les relie.»

Ce chapitre apprend à étudier deux caractères quantitatifs X et Y observés sur une même population : les ranger dans un tableau, les représenter par un nuage de points, juger s'ils varient ensemble, puis en tirer une droite pour prévoir. Sept notions : le tableau à double entrée et ses distributions marginales, le nuage de points et le point moyen, la méthode de Mayer, la covariance, le coefficient de corrélation linéaire, les droites de régression et les ajustements non affines. Tu réutilises la moyenne, la variance et l'écart-type d'une série, les fonctions affines, ln et exp ; chaque calcul se fait à la main sur des nombres choisis, puis la calculatrice en mode statistique à deux variables n'est plus qu'un contrôle.

## 📊 Tableau à double entrée et distributions marginales

Un atelier contrôle 40 pièces métalliques. Pour chacune, il mesure la longueur X (en mm) et la masse Y (en g), puis regroupe les mesures en classes ; le tableau donne le nombre de pièces pour chaque couple de classes.
Comment retrouver, à partir de ce seul tableau, la longueur moyenne des pièces et la dispersion de leurs longueurs, sans repasser par les 40 mesures ?

::: definition
Une **série statistique double** (X, Y) associe à chaque individu d'une population d'effectif total N deux caractères quantitatifs. On note xᵢ les valeurs de X et yⱼ celles de Y (ou les centres des classes), et nᵢⱼ l'effectif des individus pour lesquels X = xᵢ et Y = yⱼ. Les totaux nᵢ. = nᵢ₁ + … + nᵢq (par ligne) et n.ⱼ = n₁ⱼ + … + nₚⱼ (par colonne) sont les **effectifs marginaux** ; ils forment les **distributions marginales** de X et de Y, et leur somme vaut N.
:::

| Longueur X ↓ Masse Y → | [5 ; 15[ | [15 ; 25[ | [25 ; 35[ | Total |
| ---------------------- | -------- | --------- | --------- | ----- |
| [20 ; 30[              | 6        | 2         | 0         | 8     |
| [30 ; 40[              | 4        | 10        | 2         | 16    |
| [40 ; 50[              | 0        | 6         | 10        | 16    |
| Total                  | 10       | 18        | 12        | 40    |

Sur le tableau, la dernière colonne est la distribution marginale de X : ses totaux 8, 16 et 16 comptent les pièces de chaque classe de longueur, quelle que soit la masse. La dernière ligne est celle de Y : 10, 18 et 12.

::: exemple La longueur moyenne et son écart-type

1. Une classe est remplacée par son milieu, son centre : les classes de longueur ont pour centres 25, 35 et 45, avec les effectifs marginaux 8, 16 et 16 (somme 40 = N).
2. X̄ = (8 × 25 + 16 × 35 + 16 × 45) / 40 = (200 + 560 + 720) / 40 = 1480 / 40 = 37 mm, car chaque centre pèse autant que son effectif.
3. La moyenne des carrés vaut (8 × 625 + 16 × 1225 + 16 × 2025) / 40 = (5000 + 19600 + 32400) / 40 = 57000 / 40 = 1425.
4. V(X) = 1425 − 37² = 1425 − 1369 = 56, puis σ(X) = √56 ≈ 7,48 mm : on retranche le carré de la moyenne pour ne garder que la dispersion.
5. Contrôle : un écart-type d'environ 7,5 mm est cohérent avec des classes de 10 mm de large autour de 37 mm ✓.

:::

::: exemple La masse moyenne

1. Les centres des classes de masse sont 10, 20 et 30, avec les effectifs marginaux 10, 18 et 12.
2. Ȳ = (10 × 10 + 18 × 20 + 12 × 30) / 40 = (100 + 360 + 360) / 40 = 820 / 40 = 20,5 g, par la même formule appliquée à la dernière ligne du tableau.

:::

::: piege
**Erreur : oublier de retrancher (X̄)² dans la variance.** L'erreur tente parce que « la moyenne des carrés » ressemble déjà à une variance. Ici elle donne V(X) = 1425 et σ(X) = √1425 ≈ 37,7 mm, un écart-type aussi grand que la moyenne, alors que toutes les longueurs restent entre 20 et 50 mm. La bonne valeur est V(X) = 1425 − 37² = 56.
:::

::: propriete
Pour une série double d'effectif total N, avec les effectifs marginaux nᵢ. de X :
$$ X̄ = (1/N) Σ nᵢ. xᵢ $$
$$ V(X) = (1/N) Σ nᵢ. xᵢ² − (X̄)² $$
$$ σ(X) = √V(X) $$
et de même pour Y avec les effectifs n.ⱼ.
Cas limite : si X prend des valeurs isolées, xᵢ est la valeur elle-même ; seule une série en classes demande les centres, et les résultats sont alors des valeurs approchées.
:::

::: verifie À toi : la dispersion des masses
Avec le même tableau, calcule la variance V(Y) et l'écart-type σ(Y) des masses (on a Ȳ = 20,5 g).

---

La moyenne des carrés vaut (10 × 100 + 18 × 400 + 12 × 900) / 40 = (1000 + 7200 + 10800) / 40 = 19000 / 40 = 475. Donc V(Y) = 475 − 20,5² = 475 − 420,25 = 54,75 et σ(Y) = √54,75 ≈ 7,40 g : on retranche le carré de la moyenne, exactement comme pour X.
:::

::: retenir
Les effectifs marginaux sont les totaux du tableau, et X̄ = (1/N) Σ nᵢ. xᵢ, V(X) = (1/N) Σ nᵢ. xᵢ² − (X̄)² : on pondère par l'effectif et on retranche le carré de la moyenne.
:::

## 🔵 Nuage de points et point moyen

Un magasin d'outillage fait varier le prix X (en dinars) d'une perceuse et relève les ventes Y (en dizaines de perceuses) du mois : (20 ; 46), (30 ; 40), (40 ; 35), (50 ; 27) et (60 ; 22).
Comment voir d'un coup d'œil si les ventes baissent quand le prix monte, et quel point résume l'ensemble des cinq mesures ?

::: definition
Le plan est muni d'un repère orthogonal. Le **nuage de points** d'une série double est l'ensemble des points Mᵢⱼ(xᵢ ; yⱼ), chacun affecté de l'effectif nᵢⱼ correspondant. Le **point moyen** du nuage est le point G(X̄ ; Ȳ), dont les coordonnées sont les moyennes de X et de Y.
:::

::: figure Le nuage descend de gauche à droite : les ventes baissent quand le prix monte ; le point moyen G, cerclé, a pour coordonnées les deux moyennes
<svg viewBox="0 0 340 250">
<title>Nuage de cinq points (prix, ventes) et son point moyen G(40 ; 34), obtenu avec les moyennes 40 et 34</title>
<line x1="94.7" y1="208" x2="94.7" y2="22" stroke="#e2e8f0" stroke-width="1"/>
<line x1="139.3" y1="208" x2="139.3" y2="22" stroke="#e2e8f0" stroke-width="1"/>
<line x1="184" y1="208" x2="184" y2="22" stroke="#e2e8f0" stroke-width="1"/>
<line x1="228.7" y1="208" x2="228.7" y2="22" stroke="#e2e8f0" stroke-width="1"/>
<line x1="273.3" y1="208" x2="273.3" y2="22" stroke="#e2e8f0" stroke-width="1"/>
<line x1="50" y1="181.4" x2="318" y2="181.4" stroke="#e2e8f0" stroke-width="1"/>
<line x1="50" y1="128.3" x2="318" y2="128.3" stroke="#e2e8f0" stroke-width="1"/>
<line x1="50" y1="75.1" x2="318" y2="75.1" stroke="#e2e8f0" stroke-width="1"/>
<line x1="50" y1="22" x2="318" y2="22" stroke="#e2e8f0" stroke-width="1"/>
<path d="M50 22 L50 208 L318 208" fill="none" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/>
<line x1="94.7" y1="208" x2="94.7" y2="212" stroke="#0f172a" stroke-width="1.2"/>
<text x="94.7" y="224" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >20</text>
<line x1="139.3" y1="208" x2="139.3" y2="212" stroke="#0f172a" stroke-width="1.2"/>
<text x="139.3" y="224" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >30</text>
<line x1="184" y1="208" x2="184" y2="212" stroke="#0f172a" stroke-width="1.2"/>
<text x="184" y="224" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >40</text>
<line x1="228.7" y1="208" x2="228.7" y2="212" stroke="#0f172a" stroke-width="1.2"/>
<text x="228.7" y="224" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >50</text>
<line x1="273.3" y1="208" x2="273.3" y2="212" stroke="#0f172a" stroke-width="1.2"/>
<text x="273.3" y="224" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >60</text>
<line x1="46" y1="181.4" x2="50" y2="181.4" stroke="#0f172a" stroke-width="1.2"/>
<text x="43" y="185.4" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >20</text>
<line x1="46" y1="128.3" x2="50" y2="128.3" stroke="#0f172a" stroke-width="1.2"/>
<text x="43" y="132.3" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >30</text>
<line x1="46" y1="75.1" x2="50" y2="75.1" stroke="#0f172a" stroke-width="1.2"/>
<text x="43" y="79.1" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >40</text>
<line x1="46" y1="22" x2="50" y2="22" stroke="#0f172a" stroke-width="1.2"/>
<text x="43" y="26" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >50</text>
<text x="318" y="237" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >X (prix, en dinars)</text>
<text x="54" y="17" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >Y (ventes, en dizaines)</text>
<line x1="184" y1="208" x2="184" y2="107" stroke="#b45309" stroke-width="1.5" stroke-linecap="round" stroke-dasharray="5 4"/>
<line x1="50" y1="107" x2="184" y2="107" stroke="#b45309" stroke-width="1.5" stroke-linecap="round" stroke-dasharray="5 4"/>
<circle cx="94.7" cy="43.3" r="4" fill="#0f172a" stroke="#ffffff" stroke-width="1"/>
<circle cx="139.3" cy="75.1" r="4" fill="#0f172a" stroke="#ffffff" stroke-width="1"/>
<circle cx="184" cy="101.7" r="4" fill="#0f172a" stroke="#ffffff" stroke-width="1"/>
<circle cx="228.7" cy="144.2" r="4" fill="#0f172a" stroke="#ffffff" stroke-width="1"/>
<circle cx="273.3" cy="170.8" r="4" fill="#0f172a" stroke="#ffffff" stroke-width="1"/>
<circle cx="184" cy="107" r="8" fill="none" stroke="#b45309" stroke-width="2.4"/>
<text x="224" y="95" text-anchor="middle" font-size="13" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >G(40 ; 34)</text>
</svg>
:::

Sur la figure, les pointillés montrent que l'abscisse de G est la moyenne X̄ des prix et son ordonnée la moyenne Ȳ des ventes ; chaque point est affecté de l'effectif 1.

::: exemple Le point moyen des perceuses

1. X̄ = (20 + 30 + 40 + 50 + 60) / 5 = 200 / 5 = 40 : l'abscisse de G est la moyenne des prix.
2. Ȳ = (46 + 40 + 35 + 27 + 22) / 5 = 170 / 5 = 34 : l'ordonnée de G est la moyenne des ventes.
3. G(40 ; 34). Le nuage a une forme allongée qui descend, donc les ventes diminuent quand le prix augmente.
4. Contrôle : le point du nuage d'abscisse 40 est (40 ; 35), distinct de G(40 ; 34) ✓ : G n'est pas un point du nuage.

:::

::: piege
**Erreur : prendre pour G le point du nuage situé « au milieu ».** L'erreur tente parce que l'abscisse centrale 40 est bien la moyenne des prix. Elle donne (40 ; 35) au lieu de (40 ; 34) : l'ordonnée de G est la moyenne 170 / 5 = 34 des cinq ventes, pas la vente du mois central. G se calcule, il ne se choisit pas parmi les points.
:::

::: propriete
Pour une série double, X̄ et Ȳ se calculent sur les distributions marginales, et G(X̄ ; Ȳ) est le point moyen du nuage.
Cas limite : G n'est pas forcément un point du nuage, comme dans l'exemple ; et si l'on a un tableau d'effectifs nᵢⱼ, chaque point Mᵢⱼ compte autant de fois que son effectif.
:::

::: verifie À toi : quatre points
Quel est le point moyen du nuage formé des quatre points (2 ; 9), (4 ; 7), (6 ; 4) et (8 ; 4) ?

---

X̄ = (2 + 4 + 6 + 8) / 4 = 5 et Ȳ = (9 + 7 + 4 + 4) / 4 = 24 / 4 = 6, donc G(5 ; 6). Chaque coordonnée est la moyenne des coordonnées correspondantes ; G n'est pas un des quatre points.
:::

::: retenir
Le nuage est l'ensemble des points (xᵢ ; yⱼ) avec leurs effectifs, et son point moyen est G(X̄ ; Ȳ) : on le calcule avec les moyennes, il n'est pas forcément un point du nuage.
:::

## 📏 La méthode de Mayer : deux points moyens suffisent

Une usine suit sa production Y (en centaines de pièces) pendant huit années, X étant le rang de l'année : (1 ; 12), (2 ; 14), (3 ; 17), (4 ; 21), (5 ; 23), (6 ; 27), (7 ; 29) et (8 ; 33).
Le nuage est allongé : peut-on le résumer par une droite pour prévoir la production de l'année de rang 10, sans calcul lourd ?

::: definition
Quand le nuage a une forme allongée, on approche la relation entre X et Y par une relation affine Y = aX + b (ou X = a'Y + b') : c'est un **ajustement affine**. La **méthode de Mayer** partage le nuage en deux parties P₁ et P₂ de part et d'autre d'une parallèle à l'axe des ordonnées, calcule leurs points moyens G₁ et G₂, et retient la droite (G₁G₂), appelée **droite de Mayer**.
:::

::: figure Les huit points sont partagés en deux moitiés de part et d'autre de la parallèle pointillée à l'axe des ordonnées ; la droite (G₁G₂) passe près de tous les points et par le point moyen G
<svg viewBox="0 0 340 262">
<title>Huit points séparés en deux moitiés P1 et P2 par la droite x = 4,5, leurs points moyens G1(2,5 ; 16) et G2(6,5 ; 28), et la droite de Mayer y = 3x + 8,5 qui passe par G(4,5 ; 22)</title>
<line x1="76.4" y1="220" x2="76.4" y2="22" stroke="#e2e8f0" stroke-width="1"/>
<line x1="106.9" y1="220" x2="106.9" y2="22" stroke="#e2e8f0" stroke-width="1"/>
<line x1="137.3" y1="220" x2="137.3" y2="22" stroke="#e2e8f0" stroke-width="1"/>
<line x1="167.8" y1="220" x2="167.8" y2="22" stroke="#e2e8f0" stroke-width="1"/>
<line x1="198.2" y1="220" x2="198.2" y2="22" stroke="#e2e8f0" stroke-width="1"/>
<line x1="228.7" y1="220" x2="228.7" y2="22" stroke="#e2e8f0" stroke-width="1"/>
<line x1="259.1" y1="220" x2="259.1" y2="22" stroke="#e2e8f0" stroke-width="1"/>
<line x1="289.6" y1="220" x2="289.6" y2="22" stroke="#e2e8f0" stroke-width="1"/>
<line x1="46" y1="170.5" x2="320" y2="170.5" stroke="#e2e8f0" stroke-width="1"/>
<line x1="46" y1="121" x2="320" y2="121" stroke="#e2e8f0" stroke-width="1"/>
<line x1="46" y1="71.5" x2="320" y2="71.5" stroke="#e2e8f0" stroke-width="1"/>
<line x1="46" y1="22" x2="320" y2="22" stroke="#e2e8f0" stroke-width="1"/>
<path d="M46 22 L46 220 L320 220" fill="none" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/>
<line x1="76.4" y1="220" x2="76.4" y2="224" stroke="#0f172a" stroke-width="1.2"/>
<text x="76.4" y="236" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >1</text>
<line x1="106.9" y1="220" x2="106.9" y2="224" stroke="#0f172a" stroke-width="1.2"/>
<text x="106.9" y="236" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >2</text>
<line x1="137.3" y1="220" x2="137.3" y2="224" stroke="#0f172a" stroke-width="1.2"/>
<text x="137.3" y="236" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >3</text>
<line x1="167.8" y1="220" x2="167.8" y2="224" stroke="#0f172a" stroke-width="1.2"/>
<text x="167.8" y="236" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >4</text>
<line x1="198.2" y1="220" x2="198.2" y2="224" stroke="#0f172a" stroke-width="1.2"/>
<text x="198.2" y="236" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >5</text>
<line x1="228.7" y1="220" x2="228.7" y2="224" stroke="#0f172a" stroke-width="1.2"/>
<text x="228.7" y="236" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >6</text>
<line x1="259.1" y1="220" x2="259.1" y2="224" stroke="#0f172a" stroke-width="1.2"/>
<text x="259.1" y="236" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >7</text>
<line x1="289.6" y1="220" x2="289.6" y2="224" stroke="#0f172a" stroke-width="1.2"/>
<text x="289.6" y="236" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >8</text>
<line x1="42" y1="170.5" x2="46" y2="170.5" stroke="#0f172a" stroke-width="1.2"/>
<text x="39" y="174.5" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >10</text>
<line x1="42" y1="121" x2="46" y2="121" stroke="#0f172a" stroke-width="1.2"/>
<text x="39" y="125" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >20</text>
<line x1="42" y1="71.5" x2="46" y2="71.5" stroke="#0f172a" stroke-width="1.2"/>
<text x="39" y="75.5" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >30</text>
<line x1="42" y1="22" x2="46" y2="22" stroke="#0f172a" stroke-width="1.2"/>
<text x="39" y="26" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >40</text>
<text x="320" y="249" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >X (rang de l'année)</text>
<text x="50" y="17" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >Y (centaines de pièces)</text>
<line x1="183" y1="220" x2="183" y2="22" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-dasharray="6 4"/>
<line x1="61.2" y1="170.5" x2="310.9" y2="48.7" stroke="#0f6e56" stroke-width="2.4" stroke-linecap="round"/>
<circle cx="76.4" cy="160.6" r="4" fill="#0f6e56" stroke="#ffffff" stroke-width="1"/>
<circle cx="106.9" cy="150.7" r="4" fill="#0f6e56" stroke="#ffffff" stroke-width="1"/>
<circle cx="137.3" cy="135.9" r="4" fill="#0f6e56" stroke="#ffffff" stroke-width="1"/>
<circle cx="167.8" cy="116" r="4" fill="#0f6e56" stroke="#ffffff" stroke-width="1"/>
<circle cx="198.2" cy="106.2" r="4" fill="#b45309" stroke="#ffffff" stroke-width="1"/>
<circle cx="228.7" cy="86.3" r="4" fill="#b45309" stroke="#ffffff" stroke-width="1"/>
<circle cx="259.1" cy="76.5" r="4" fill="#b45309" stroke="#ffffff" stroke-width="1"/>
<circle cx="289.6" cy="56.7" r="4" fill="#b45309" stroke="#ffffff" stroke-width="1"/>
<rect x="116.6" y="135.3" width="11.0" height="11.0" fill="#0f6e56" stroke="#ffffff" stroke-width="1"/>
<rect x="238.4" y="75.9" width="11.0" height="11.0" fill="#b45309" stroke="#ffffff" stroke-width="1"/>
<circle cx="183" cy="111.1" r="5.5" fill="#0f172a" stroke="#ffffff" stroke-width="1"/>
<text x="105.1" y="132.8" text-anchor="middle" font-size="14" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >G₁</text>
<text x="260.9" y="97.4" text-anchor="middle" font-size="14" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >G₂</text>
<text x="201" y="128.1" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >G</text>
<text x="82.5" y="39.3" text-anchor="middle" font-size="13" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >P₁</text>
<text x="298.7" y="31.9" text-anchor="middle" font-size="13" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >P₂</text>
</svg>
:::

Sur la figure, G₁ est le point moyen des quatre points verts et G₂ celui des quatre points orange ; le point noir G est le point moyen des huit points.

::: exemple La production de l'année 10

1. Les abscisses sont déjà rangées par ordre croissant : P₁ contient les rangs 1 à 4 et P₂ les rangs 5 à 8, soit quatre points chacune, séparées par la droite x = 4,5.
2. G₁ : (1 + 2 + 3 + 4) / 4 = 2,5 et (12 + 14 + 17 + 21) / 4 = 64 / 4 = 16, donc G₁(2,5 ; 16).
3. G₂ : (5 + 6 + 7 + 8) / 4 = 6,5 et (23 + 27 + 29 + 33) / 4 = 112 / 4 = 28, donc G₂(6,5 ; 28).
4. La pente de (G₁G₂) est (28 − 16) / (6,5 − 2,5) = 12 / 4 = 3 ; la droite passe par G₁, donc y − 16 = 3(x − 2,5), soit y = 3x + 8,5.
5. Contrôle : G(4,5 ; 22), avec 176 / 8 = 22 pour la moyenne des productions, et 3 × 4,5 + 8,5 = 22 ✓ : la droite de Mayer passe par G.
6. Prévision : pour le rang 10, y = 3 × 10 + 8,5 = 38,5, soit 38,5 centaines de pièces.

:::

::: piege
**Erreur : couper la liste dans l'ordre où elle est écrite, sans la trier par abscisses.** L'erreur tente parce que les points arrivent « dans l'ordre des essais ». Avec (6 ; 21), (2 ; 10), (8 ; 30) et (4 ; 17), couper en deux dans cet ordre donne {(6 ; 21) ; (2 ; 10)} et {(8 ; 30) ; (4 ; 17)}, puis G₁(4 ; 15,5), G₂(6 ; 23,5) et la droite y = 4x − 0,5. Trier d'abord par abscisses croissantes donne P₁ = {(2 ; 10) ; (4 ; 17)} et P₂ = {(6 ; 21) ; (8 ; 30)}, d'où G₁(3 ; 13,5), G₂(7 ; 25,5) et la vraie droite de Mayer y = 3x + 4,5 ; pour x = 10 on prévoit 34,5 et non 39,5.
:::

::: methode
Pour ajuster un nuage par la méthode de Mayer :

1. ranger les points par abscisses croissantes et les partager en deux parties P₁ et P₂, de part et d'autre d'une parallèle à l'axe des ordonnées, de même effectif ;
2. calculer les points moyens G₁ de P₁ et G₂ de P₂ ;
3. écrire l'équation de la droite (G₁G₂) : c'est la droite de Mayer, et elle passe par le point moyen G du nuage.

Cas limite : avec un nombre impair de points, une partie en compte un de plus que l'autre ; l'un ou l'autre partage convient.

:::

::: verifie À toi : six trimestres
Un nuage a pour points (1 ; 5), (2 ; 8), (3 ; 11), (4 ; 12), (5 ; 14) et (6 ; 16). Donne l'équation de sa droite de Mayer, en séparant les trois premiers points des trois derniers, puis la prévision pour x = 9.

---

P₁ = {1 ; 2 ; 3} donne G₁(2 ; 24 / 3) = (2 ; 8) et P₂ = {4 ; 5 ; 6} donne G₂(5 ; 42 / 3) = (5 ; 14). La pente est (14 − 8) / (5 − 2) = 2, donc y − 8 = 2(x − 2), soit y = 2x + 4. Contrôle : G(3,5 ; 11) vérifie 2 × 3,5 + 4 = 11. Pour x = 9, y = 2 × 9 + 4 = 22.
:::

::: retenir
La droite de Mayer est la droite (G₁G₂) des points moyens des deux moitiés du nuage, rangé par abscisses croissantes ; elle passe par le point moyen G.
:::

## 🤝 La covariance : varier ensemble

Un lycée technique relève, pour cinq élèves, le nombre X d'heures d'atelier par semaine et la note Y de TP sur 10 : (2 ; 2), (4 ; 4), (6 ; 5), (8 ; 7) et (10 ; 7).
Les élèves qui font plus d'heures ont de meilleures notes. Comment résumer par un seul nombre le fait que X et Y varient ensemble ?

::: definition
Pour une série double de n couples (xᵢ ; yᵢ), la **covariance** de X et de Y est le réel
$$ Cov(X, Y) = (1/n) Σ xᵢyᵢ − X̄ × Ȳ $$
c'est la moyenne des produits xᵢyᵢ, moins le produit des moyennes.

Pour un tableau à double entrée d'effectif total N : Cov(X, Y) = (1/N) Σᵢ Σⱼ nᵢⱼ xᵢ yⱼ − X̄ × Ȳ, chaque produit xᵢyⱼ étant compté nᵢⱼ fois (centres des classes pour une série en classes). Pour les 40 pièces : (6 × 25 × 10 + 2 × 25 × 20 + 4 × 35 × 10 + 10 × 35 × 20 + 2 × 35 × 30 + 6 × 45 × 20 + 10 × 45 × 30) / 40 = 31900 / 40 = 797,5, d'où Cov = 797,5 − 37 × 20,5 = 39.
:::

::: exemple La covariance des heures d'atelier et des notes

1. X̄ = 30 / 5 = 6 et Ȳ = 25 / 5 = 5 : les moyennes servent à centrer les valeurs.
2. Les produits xᵢyᵢ valent 4, 16, 30, 56 et 70, de somme 176, donc leur moyenne est 176 / 5 = 35,2.
3. Cov(X, Y) = 35,2 − 6 × 5 = 5,2 : le signe est positif, les notes montent avec les heures.
4. Pour comparer, V(X) = (4 + 16 + 36 + 64 + 100) / 5 − 36 = 8 et V(Y) = (4 + 16 + 25 + 49 + 49) / 5 − 25 = 3,6.
5. Alors Cov² = 5,2² = 27,04 et V(X) × V(Y) = 8 × 3,6 = 28,8 : les deux nombres sont voisins, ce qui indique une relation à peu près affine entre X et Y.

:::

::: piege
**Erreur : prendre le produit des moyennes pour la covariance.** L'erreur tente parce que X̄ × Ȳ = 6 × 5 = 30 est le deuxième terme de la formule. Mais la covariance est un écart : 35,2 − 30 = 5,2. Confondre « moyenne des produits » (35,2) et « produit des moyennes » (30) donne 35,2 ou 30 au lieu de 5,2.
:::

::: propriete

- Cov(X, Y) = (moyenne des xᵢyᵢ) − X̄ × Ȳ.
- Si Cov²(X, Y) est assez voisin de V(X) × V(Y), la relation entre X et Y est approximativement affine : on peut trouver a et b tels que Y est proche de aX + b.
- Le signe de Cov(X, Y) donne le sens de la liaison : positif si Y croît avec X, négatif si Y décroît.

Cas limite : si les points sont alignés, Cov² = V(X) × V(Y). Pour (1 ; 2), (2 ; 4) et (3 ; 6) : Cov = 28/3 − 2 × 4 = 4/3, V(X) = 2/3, V(Y) = 8/3, et (4/3)² = 16/9 = (2/3) × (8/3).
:::

::: verifie À toi : une liaison décroissante
Calcule Cov(X, Y) pour (1 ; 8), (2 ; 6), (3 ; 5) et (4 ; 1), et dis dans quel sens varient X et Y.

---

X̄ = 2,5 et Ȳ = 20 / 4 = 5. Les produits xᵢyᵢ valent 8, 12, 15 et 4, de somme 39, donc leur moyenne est 9,75. Cov(X, Y) = 9,75 − 2,5 × 5 = 9,75 − 12,5 = −2,75 : le signe est négatif, donc Y diminue quand X augmente.
:::

::: retenir
Cov(X, Y) = (moyenne des produits xᵢyᵢ) − X̄ × Ȳ : son signe donne le sens de la liaison, et Cov² voisin de V(X) × V(Y) annonce une relation à peu près affine.
:::

## 🎚️ Le coefficient de corrélation linéaire

Dans l'atelier, Cov² vaut 27,04 et V(X) × V(Y) vaut 28,8. Ces deux nombres sont-ils « assez voisins » ? Et pour une autre série, où fixer la limite ?
Il faut un nombre sans unité, indépendant de l'échelle des mesures, qu'on puisse comparer à un seuil.

::: definition
Pour une série double où X et Y ne sont pas constants, le **coefficient de corrélation linéaire** est le réel
$$ r = Cov(X, Y) / (σ(X) × σ(Y)) $$
Lorsque 0,75 ≤ |r| ≤ 1, le nuage a une forme allongée : on dit que la corrélation linéaire est forte et qu'un ajustement affine est justifié.
:::

::: figure Trois nuages et leur coefficient r : plus les points s'alignent, plus |r| s'approche de 1, et le signe de r est celui du sens de variation
<svg viewBox="0 0 340 170">
<title>Trois nuages : r ≈ 0,97 (points presque alignés, croissant), r ≈ −0,10 (points dispersés), r ≈ −0,96 (points presque alignés, décroissant)</title>
<path d="M12 24 L12 136 L108 136" fill="none" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/>
<circle cx="29.5" cy="111.1" r="4" fill="#0f6e56" stroke="#ffffff" stroke-width="1"/>
<circle cx="46.9" cy="86.2" r="4" fill="#0f6e56" stroke="#ffffff" stroke-width="1"/>
<circle cx="64.4" cy="73.8" r="4" fill="#0f6e56" stroke="#ffffff" stroke-width="1"/>
<circle cx="81.8" cy="48.9" r="4" fill="#0f6e56" stroke="#ffffff" stroke-width="1"/>
<circle cx="99.3" cy="48.9" r="4" fill="#0f6e56" stroke="#ffffff" stroke-width="1"/>
<text x="60" y="162" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >r ≈ 0,97</text>
<path d="M124 24 L124 136 L220 136" fill="none" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/>
<circle cx="140" cy="61.3" r="4" fill="#b45309" stroke="#ffffff" stroke-width="1"/>
<circle cx="156" cy="117.3" r="4" fill="#b45309" stroke="#ffffff" stroke-width="1"/>
<circle cx="172" cy="42.7" r="4" fill="#b45309" stroke="#ffffff" stroke-width="1"/>
<circle cx="188" cy="98.7" r="4" fill="#b45309" stroke="#ffffff" stroke-width="1"/>
<circle cx="204" cy="80" r="4" fill="#b45309" stroke="#ffffff" stroke-width="1"/>
<text x="172" y="162" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >r ≈ −0,10</text>
<path d="M236 24 L236 136 L332 136" fill="none" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/>
<circle cx="255.2" cy="46.4" r="4" fill="#0f6e56" stroke="#ffffff" stroke-width="1"/>
<circle cx="274.4" cy="68.8" r="4" fill="#0f6e56" stroke="#ffffff" stroke-width="1"/>
<circle cx="293.6" cy="80" r="4" fill="#0f6e56" stroke="#ffffff" stroke-width="1"/>
<circle cx="312.8" cy="124.8" r="4" fill="#0f6e56" stroke="#ffffff" stroke-width="1"/>
<text x="284" y="162" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >r ≈ −0,96</text>
</svg>
:::

Sur la figure, le nuage de gauche est celui de l'atelier ; le signe de r dit si les points montent ou descendent, et sa valeur absolue dit à quel point ils sont alignés.

::: exemple Les heures d'atelier et les notes

1. On reprend Cov(X, Y) = 5,2, V(X) = 8 et V(Y) = 3,6, donc σ(X) × σ(Y) = √(8 × 3,6) = √28,8 ≈ 5,37.
2. r = 5,2 / 5,37 ≈ 0,969, car r est la covariance ramenée à l'échelle des deux écarts-types.
3. 0,969 ≥ 0,75 : la corrélation linéaire est forte, donc un ajustement affine est justifié.
4. Contrôle : r² = 27,04 / 28,8 ≈ 0,939, le rapport de Cov² à V(X) × V(Y) ✓ : « Cov² voisin de V(X) × V(Y) » veut dire « r² voisin de 1 ».

:::

::: exemple Un nuage sans forme

1. Soit (1 ; 4), (2 ; 1), (3 ; 5), (4 ; 2) et (5 ; 3) : X̄ = Ȳ = 3 et V(X) = V(Y) = 55/5 − 9 = 2.
2. La moyenne des produits vaut (4 + 2 + 15 + 8 + 15) / 5 = 8,8, donc Cov(X, Y) = 8,8 − 9 = −0,2.
3. r = −0,2 / (√2 × √2) = −0,2 / 2 = −0,1 : |r| est très inférieur à 0,75, le nuage n'est pas allongé et un ajustement affine n'est pas justifié.

:::

::: piege
**Erreur : croire que r = 0 signifie qu'il n'y a aucune liaison entre X et Y.** L'erreur tente parce qu'un r nul « ne trouve rien ». Prenons Y = X² avec X = −2, −1, 0, 1, 2 et Y = 4, 1, 0, 1, 4 : la moyenne des produits xᵢyᵢ vaut (−8 − 1 + 0 + 1 + 8) / 5 = 0 et X̄ = 0, donc Cov = 0 et r = 0, alors que Y est exactement X². Le coefficient r mesure seulement la liaison affine.
:::

::: propriete

- r est un nombre de [−1 ; 1] (propriété admise) et n'a pas d'unité ;
- r a le signe de Cov(X, Y) : positif si Y croît avec X, négatif sinon ;
- 0,75 ≤ |r| ≤ 1 : corrélation forte, ajustement affine justifié ; |r| plus petit : l'ajustement affine n'est pas justifié.

Cas limite : si les points sont alignés sur une droite non parallèle aux axes, |r| = 1. Pour (1 ; 2), (2 ; 4) et (3 ; 6) : r = (4/3) / (√(2/3) × √(8/3)) = (4/3) / (4/3) = 1.
:::

::: verifie À toi : la valeur limite
Une série vérifie Cov(X, Y) = −9, V(X) = 9 et V(Y) = 16. Calcule r et conclus.

---

σ(X) = √9 = 3 et σ(Y) = √16 = 4, donc r = −9 / (3 × 4) = −9 / 12 = −0,75. Alors |r| = 0,75, qui atteint le seuil : la corrélation est forte et un ajustement affine est justifié ; le signe négatif dit que Y décroît quand X croît.
:::

::: retenir
r = Cov(X, Y) / (σ(X) × σ(Y)) est un nombre sans unité de [−1 ; 1] : 0,75 ≤ |r| justifie un ajustement affine, et r = 0 n'exclut pas une liaison non affine.
:::

## 📈 Droites de régression et prévision

Un technicien suspend cinq masses X (en kg) à un ressort et mesure l'allongement Y (en mm) : (1 ; 4), (2 ; 7), (3 ; 7), (4 ; 11) et (5 ; 11). Le nuage est allongé et r ≈ 0,95.
Quelle droite utiliser pour prévoir l'allongement d'une masse de 7 kg ? Et pour trouver la masse qui donne 15 mm ?

::: definition
Quand 0,75 ≤ |r| ≤ 1, la liaison entre X et Y s'approche par deux droites passant par le point moyen G(X̄ ; Ȳ) :

- la **droite de régression de Y en X**, D₁ : y = ax + b avec a = Cov(X, Y) / V(X) et b = Ȳ − aX̄ ;
- la **droite de régression de X en Y**, D₂ : x = a'y + b' avec a' = Cov(X, Y) / V(Y) et b' = X̄ − a'Ȳ.

Ces deux droites sont celles de la **méthode des moindres carrés** ; leurs formules sont admises.

:::

::: figure Les deux droites de régression se coupent au point moyen G : D₁ (trait plein) sert à prévoir Y à partir de X, D₂ (pointillés) à prévoir X à partir de Y
<svg viewBox="0 0 340 262">
<title>Cinq points (masse, allongement), le point moyen G(3 ; 8) et les deux droites de régression D1 : y = 1,8x + 2,6 et D2 : y = 2x + 2, qui se coupent en G</title>
<line x1="86.2" y1="220" x2="86.2" y2="22" stroke="#e2e8f0" stroke-width="1"/>
<line x1="128.3" y1="220" x2="128.3" y2="22" stroke="#e2e8f0" stroke-width="1"/>
<line x1="170.5" y1="220" x2="170.5" y2="22" stroke="#e2e8f0" stroke-width="1"/>
<line x1="212.6" y1="220" x2="212.6" y2="22" stroke="#e2e8f0" stroke-width="1"/>
<line x1="254.8" y1="220" x2="254.8" y2="22" stroke="#e2e8f0" stroke-width="1"/>
<line x1="296.9" y1="220" x2="296.9" y2="22" stroke="#e2e8f0" stroke-width="1"/>
<line x1="44" y1="180.4" x2="318" y2="180.4" stroke="#e2e8f0" stroke-width="1"/>
<line x1="44" y1="140.8" x2="318" y2="140.8" stroke="#e2e8f0" stroke-width="1"/>
<line x1="44" y1="101.2" x2="318" y2="101.2" stroke="#e2e8f0" stroke-width="1"/>
<line x1="44" y1="61.6" x2="318" y2="61.6" stroke="#e2e8f0" stroke-width="1"/>
<line x1="44" y1="22" x2="318" y2="22" stroke="#e2e8f0" stroke-width="1"/>
<path d="M44 22 L44 220 L318 220" fill="none" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/>
<line x1="86.2" y1="220" x2="86.2" y2="224" stroke="#0f172a" stroke-width="1.2"/>
<text x="86.2" y="236" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >1</text>
<line x1="128.3" y1="220" x2="128.3" y2="224" stroke="#0f172a" stroke-width="1.2"/>
<text x="128.3" y="236" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >2</text>
<line x1="170.5" y1="220" x2="170.5" y2="224" stroke="#0f172a" stroke-width="1.2"/>
<text x="170.5" y="236" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >3</text>
<line x1="212.6" y1="220" x2="212.6" y2="224" stroke="#0f172a" stroke-width="1.2"/>
<text x="212.6" y="236" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >4</text>
<line x1="254.8" y1="220" x2="254.8" y2="224" stroke="#0f172a" stroke-width="1.2"/>
<text x="254.8" y="236" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >5</text>
<line x1="296.9" y1="220" x2="296.9" y2="224" stroke="#0f172a" stroke-width="1.2"/>
<text x="296.9" y="236" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >6</text>
<line x1="40" y1="180.4" x2="44" y2="180.4" stroke="#0f172a" stroke-width="1.2"/>
<text x="37" y="184.4" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >3</text>
<line x1="40" y1="140.8" x2="44" y2="140.8" stroke="#0f172a" stroke-width="1.2"/>
<text x="37" y="144.8" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >6</text>
<line x1="40" y1="101.2" x2="44" y2="101.2" stroke="#0f172a" stroke-width="1.2"/>
<text x="37" y="105.2" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >9</text>
<line x1="40" y1="61.6" x2="44" y2="61.6" stroke="#0f172a" stroke-width="1.2"/>
<text x="37" y="65.6" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >12</text>
<line x1="40" y1="22" x2="44" y2="22" stroke="#0f172a" stroke-width="1.2"/>
<text x="37" y="26" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >15</text>
<text x="318" y="249" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >X (masse, en kg)</text>
<text x="48" y="17" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >Y (allongement, en mm)</text>
<line x1="56.6" y1="178.6" x2="305.4" y2="38.4" stroke="#0f6e56" stroke-width="2.4" stroke-linecap="round"/>
<line x1="56.6" y1="185.7" x2="305.4" y2="29.9" stroke="#b45309" stroke-width="2.4" stroke-linecap="round" stroke-dasharray="8 5"/>
<circle cx="86.2" cy="167.2" r="4" fill="#0f172a" stroke="#ffffff" stroke-width="1"/>
<circle cx="128.3" cy="127.6" r="4" fill="#0f172a" stroke="#ffffff" stroke-width="1"/>
<circle cx="170.5" cy="127.6" r="4" fill="#0f172a" stroke="#ffffff" stroke-width="1"/>
<circle cx="212.6" cy="74.8" r="4" fill="#0f172a" stroke="#ffffff" stroke-width="1"/>
<circle cx="254.8" cy="74.8" r="4" fill="#0f172a" stroke="#ffffff" stroke-width="1"/>
<rect x="165" y="108.9" width="11.0" height="11.0" fill="#0f172a" stroke="#ffffff" stroke-width="1"/>
<text x="140.5" y="100.4" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >G(3 ; 8)</text>
<text x="299.4" y="55.4" text-anchor="middle" font-size="14" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >D₁</text>
<text x="255.5" y="46.4" text-anchor="middle" font-size="14" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >D₂</text>
</svg>
:::

Sur la figure, D₁ et D₂ sont presque confondues parce que r est proche de 1, mais ce sont deux droites distinctes qui se coupent en G(3 ; 8).

::: exemple Les masses et les allongements

1. X̄ = 15 / 5 = 3 et Ȳ = 40 / 5 = 8 ; V(X) = 55 / 5 − 9 = 2 et V(Y) = 356 / 5 − 64 = 7,2 ; la moyenne des produits vaut 138 / 5 = 27,6, donc Cov = 27,6 − 24 = 3,6.
2. r = 3,6 / √(2 × 7,2) = 3,6 / √14,4 ≈ 0,949 ≥ 0,75 : les droites de régression sont licites.
3. D₁ : a = 3,6 / 2 = 1,8 et b = 8 − 1,8 × 3 = 2,6, donc y = 1,8x + 2,6 ; pour 7 kg, y = 1,8 × 7 + 2,6 = 15,2 mm, car D₁ donne Y à partir de X.
4. D₂ : a' = 3,6 / 7,2 = 0,5 et b' = 3 − 0,5 × 8 = −1, donc x = 0,5y − 1 ; pour 15 mm, x = 0,5 × 15 − 1 = 6,5 kg, car D₂ donne X à partir de Y.
5. Contrôle : G(3 ; 8) est sur D₁ (1,8 × 3 + 2,6 = 8) et sur D₂ (0,5 × 8 − 1 = 3) ✓.

:::

::: piege
**Erreur : retourner D₁ pour trouver X à partir de Y.** L'erreur tente parce que y = 1,8x + 2,6 « se résout en x ». Avec 15 = 1,8x + 2,6 on obtient x ≈ 6,89 kg, et non les 6,5 kg de D₂. Les deux droites ne se déduisent pas l'une de l'autre : on choisit D₁ pour prévoir Y, D₂ pour prévoir X.
:::

::: propriete

- D₁ : y = ax + b avec a = Cov(X, Y) / V(X) et b = Ȳ − aX̄ ; D₂ : x = a'y + b' avec a' = Cov(X, Y) / V(Y) et b' = X̄ − a'Ȳ ;
- D₁ et D₂ passent toutes deux par G, et a × a' = Cov² / (V(X) × V(Y)) = r² ;
- on prévoit Y à partir de X par D₁, et X à partir de Y par D₂.

Cas limite : si les points sont exactement alignés, |r| = 1 et D₁ et D₂ sont confondues ; si Cov = 0, D₁ est la droite horizontale y = Ȳ et D₂ la droite verticale x = X̄. Dans l'exemple, a × a' = 1,8 × 0,5 = 0,9 = r² ✓.
:::

::: verifie À toi : une prévision
Une série vérifie X̄ = 4, Ȳ = 20, V(X) = 2, V(Y) = 12,5 et Cov(X, Y) = 4,5. La corrélation est-elle forte ? Donne la droite de régression de Y en X, puis la valeur prévue de Y pour x = 6.

---

r = 4,5 / √(2 × 12,5) = 4,5 / 5 = 0,9 ≥ 0,75, donc l'ajustement est justifié. a = 4,5 / 2 = 2,25 et b = 20 − 2,25 × 4 = 11, d'où y = 2,25x + 11. Pour x = 6, y = 2,25 × 6 + 11 = 24,5 : on utilise D₁ parce qu'on prévoit Y à partir de X.
:::

::: retenir
D₁ : y = ax + b avec a = Cov / V(X) et b = Ȳ − aX̄ prévoit Y ; D₂ : x = a'y + b' avec a' = Cov / V(Y) prévoit X ; toutes deux passent par G, et l'on ne retourne pas l'une pour obtenir l'autre.
:::

## 🔄 Quand le nuage n'est pas droit : changer de variable

Une plateforme de recharge de véhicules électriques compte ses abonnés Y (en centaines) à la fin de chacun des cinq premiers mois, de rang X : 5, 10, 18, 33 et 60.
Le nuage monte de plus en plus vite, une droite ne lui convient pas. Peut-on se ramener à une droite pour prévoir le mois suivant ?

::: definition
Un **ajustement non affine ramené à un ajustement affine** consiste à poser une nouvelle variable, par exemple Z = ln Y, Z = √Y ou x = 1/n, de sorte que le nuage (X ; Z) soit allongé : on ajuste alors (X ; Z) par une droite, puis on revient à Y par la fonction réciproque. L'énoncé indique le changement de variable à faire.
:::

::: figure À gauche, le nuage (X ; Y) est une courbe qui s'accélère ; à droite, après le changement Z = ln Y, les points sont presque alignés sur la droite z = 0,616x + 1,030
<svg viewBox="0 0 340 212">
<title>À gauche le nuage (X, Y) qui monte de plus en plus vite ; à droite le nuage (X, Z) avec Z = ln Y, presque aligné sur la droite z = 0,616x + 1,030</title>
<line x1="55.3" y1="168" x2="55.3" y2="42" stroke="#e2e8f0" stroke-width="1"/>
<line x1="76.7" y1="168" x2="76.7" y2="42" stroke="#e2e8f0" stroke-width="1"/>
<line x1="98" y1="168" x2="98" y2="42" stroke="#e2e8f0" stroke-width="1"/>
<line x1="119.3" y1="168" x2="119.3" y2="42" stroke="#e2e8f0" stroke-width="1"/>
<line x1="140.7" y1="168" x2="140.7" y2="42" stroke="#e2e8f0" stroke-width="1"/>
<line x1="34" y1="132" x2="162" y2="132" stroke="#e2e8f0" stroke-width="1"/>
<line x1="34" y1="96" x2="162" y2="96" stroke="#e2e8f0" stroke-width="1"/>
<line x1="34" y1="60" x2="162" y2="60" stroke="#e2e8f0" stroke-width="1"/>
<path d="M34 42 L34 168 L162 168" fill="none" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/>
<line x1="55.3" y1="168" x2="55.3" y2="172" stroke="#0f172a" stroke-width="1.2"/>
<text x="55.3" y="183" text-anchor="middle" font-size="10" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >1</text>
<line x1="76.7" y1="168" x2="76.7" y2="172" stroke="#0f172a" stroke-width="1.2"/>
<text x="76.7" y="183" text-anchor="middle" font-size="10" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >2</text>
<line x1="98" y1="168" x2="98" y2="172" stroke="#0f172a" stroke-width="1.2"/>
<text x="98" y="183" text-anchor="middle" font-size="10" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >3</text>
<line x1="119.3" y1="168" x2="119.3" y2="172" stroke="#0f172a" stroke-width="1.2"/>
<text x="119.3" y="183" text-anchor="middle" font-size="10" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >4</text>
<line x1="140.7" y1="168" x2="140.7" y2="172" stroke="#0f172a" stroke-width="1.2"/>
<text x="140.7" y="183" text-anchor="middle" font-size="10" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >5</text>
<line x1="30" y1="132" x2="34" y2="132" stroke="#0f172a" stroke-width="1.2"/>
<text x="27" y="136" text-anchor="end" font-size="10" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >20</text>
<line x1="30" y1="96" x2="34" y2="96" stroke="#0f172a" stroke-width="1.2"/>
<text x="27" y="100" text-anchor="end" font-size="10" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >40</text>
<line x1="30" y1="60" x2="34" y2="60" stroke="#0f172a" stroke-width="1.2"/>
<text x="27" y="64" text-anchor="end" font-size="10" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >60</text>
<text x="162" y="196" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >X</text>
<text x="38" y="37" text-anchor="start" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >Y</text>
<circle cx="55.3" cy="159" r="4" fill="#0f172a" stroke="#ffffff" stroke-width="1"/>
<circle cx="76.7" cy="150" r="4" fill="#0f172a" stroke="#ffffff" stroke-width="1"/>
<circle cx="98" cy="135.6" r="4" fill="#0f172a" stroke="#ffffff" stroke-width="1"/>
<circle cx="119.3" cy="108.6" r="4" fill="#0f172a" stroke="#ffffff" stroke-width="1"/>
<circle cx="140.7" cy="60" r="4" fill="#0f172a" stroke="#ffffff" stroke-width="1"/>
<text x="98" y="14" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >nuage (X, Y) : courbe</text>
<line x1="209.3" y1="168" x2="209.3" y2="42" stroke="#e2e8f0" stroke-width="1"/>
<line x1="230.7" y1="168" x2="230.7" y2="42" stroke="#e2e8f0" stroke-width="1"/>
<line x1="252" y1="168" x2="252" y2="42" stroke="#e2e8f0" stroke-width="1"/>
<line x1="273.3" y1="168" x2="273.3" y2="42" stroke="#e2e8f0" stroke-width="1"/>
<line x1="294.7" y1="168" x2="294.7" y2="42" stroke="#e2e8f0" stroke-width="1"/>
<line x1="188" y1="142.8" x2="316" y2="142.8" stroke="#e2e8f0" stroke-width="1"/>
<line x1="188" y1="117.6" x2="316" y2="117.6" stroke="#e2e8f0" stroke-width="1"/>
<line x1="188" y1="92.4" x2="316" y2="92.4" stroke="#e2e8f0" stroke-width="1"/>
<line x1="188" y1="67.2" x2="316" y2="67.2" stroke="#e2e8f0" stroke-width="1"/>
<path d="M188 42 L188 168 L316 168" fill="none" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/>
<line x1="209.3" y1="168" x2="209.3" y2="172" stroke="#0f172a" stroke-width="1.2"/>
<text x="209.3" y="183" text-anchor="middle" font-size="10" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >1</text>
<line x1="230.7" y1="168" x2="230.7" y2="172" stroke="#0f172a" stroke-width="1.2"/>
<text x="230.7" y="183" text-anchor="middle" font-size="10" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >2</text>
<line x1="252" y1="168" x2="252" y2="172" stroke="#0f172a" stroke-width="1.2"/>
<text x="252" y="183" text-anchor="middle" font-size="10" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >3</text>
<line x1="273.3" y1="168" x2="273.3" y2="172" stroke="#0f172a" stroke-width="1.2"/>
<text x="273.3" y="183" text-anchor="middle" font-size="10" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >4</text>
<line x1="294.7" y1="168" x2="294.7" y2="172" stroke="#0f172a" stroke-width="1.2"/>
<text x="294.7" y="183" text-anchor="middle" font-size="10" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >5</text>
<line x1="184" y1="142.8" x2="188" y2="142.8" stroke="#0f172a" stroke-width="1.2"/>
<text x="181" y="146.8" text-anchor="end" font-size="10" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >1</text>
<line x1="184" y1="117.6" x2="188" y2="117.6" stroke="#0f172a" stroke-width="1.2"/>
<text x="181" y="121.6" text-anchor="end" font-size="10" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >2</text>
<line x1="184" y1="92.4" x2="188" y2="92.4" stroke="#0f172a" stroke-width="1.2"/>
<text x="181" y="96.4" text-anchor="end" font-size="10" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >3</text>
<line x1="184" y1="67.2" x2="188" y2="67.2" stroke="#0f172a" stroke-width="1.2"/>
<text x="181" y="71.2" text-anchor="end" font-size="10" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >4</text>
<text x="316" y="196" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >X</text>
<text x="192" y="37" text-anchor="start" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >Z</text>
<line x1="196.5" y1="135.8" x2="307.5" y2="55.1" stroke="#0f6e56" stroke-width="2.4" stroke-linecap="round"/>
<circle cx="209.3" cy="127.4" r="4" fill="#0f172a" stroke="#ffffff" stroke-width="1"/>
<circle cx="230.7" cy="110" r="4" fill="#0f172a" stroke="#ffffff" stroke-width="1"/>
<circle cx="252" cy="95.2" r="4" fill="#0f172a" stroke="#ffffff" stroke-width="1"/>
<circle cx="273.3" cy="79.9" r="4" fill="#0f172a" stroke="#ffffff" stroke-width="1"/>
<circle cx="294.7" cy="64.8" r="4" fill="#0f172a" stroke="#ffffff" stroke-width="1"/>
<text x="252" y="14" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >nuage (X, Z) : droite</text>
</svg>
:::

Sur la figure, la variable X est la même des deux côtés ; seule l'ordonnée change, de Y à Z = ln Y, et c'est ce changement qui redresse le nuage.

::: exemple Les abonnés de la plateforme

1. On pose Z = ln Y : Z ≈ 1,609 ; 2,303 ; 2,890 ; 3,497 et 4,094, d'où Z̄ ≈ 2,879.
2. Pour (X ; Z), V(X) = 2, Cov(X, Z) ≈ 1,233 et r ≈ 0,9996 : le nuage (X ; Z) est presque aligné, donc l'ajustement affine est justifié.
3. a = 1,233 / 2 ≈ 0,616 et b = Z̄ − aX̄ ≈ 2,8786 − 0,6164 × 3 ≈ 1,030, donc z = 0,616x + 1,030, car la droite passe par G(3 ; 2,879).
4. On revient à Y : Y = e^z = e^(0,616x + 1,030) = e^(1,030) × e^(0,616x) ≈ 2,80 × e^(0,616x), puisque e^(u + v) = e^u × e^v.
5. Prévision pour x = 6 : z = 0,616 × 6 + 1,030 = 4,726, donc Y = e^(4,726) ≈ 113 centaines d'abonnés.

:::

::: exemple Le coût unitaire et l'inverse de la taille du lot

1. Le coût unitaire y d'une pièce dépend de la taille n du lot : n = 1, 2, 4, 5, 10 donne y = 46, 26, 16, 14, 10 en dinars. Le nuage (n ; y) est courbe.
2. On pose x = 1/n : les couples (x ; y) sont (1 ; 46), (0,5 ; 26), (0,25 ; 16), (0,2 ; 14) et (0,1 ; 10).
3. La droite passant par (1 ; 46) et (0,5 ; 26) a pour pente (46 − 26) / (1 − 0,5) = 40, donc y = 40x + 6 ; les trois autres points la vérifient (40 × 0,25 + 6 = 16 ; 40 × 0,2 + 6 = 14 ; 40 × 0,1 + 6 = 10) ✓.
4. Retour à n : y = 40/n + 6, donc pour n = 20, y = 40/20 + 6 = 8 dinars.

:::

::: piege
**Erreur : lire la prévision de Z comme celle de Y.** L'erreur tente parce que la droite z = 0,616x + 1,030 donne un nombre « prêt à l'emploi ». Pour x = 6 elle donne z = 4,726, que l'on prendrait pour 4,726 centaines d'abonnés, alors que le dernier relevé en compte déjà 60. Il faut revenir à Y : Y = e^(4,726) ≈ 113.
:::

::: methode
Pour traiter un nuage courbe :

1. tracer le nuage (X ; Y) et constater qu'il n'est pas allongé en ligne droite ;
2. poser la nouvelle variable indiquée (Z = ln Y, Z = √Y, x = 1/n) et calculer r pour (X ; Z) : il doit vérifier 0,75 ≤ |r| ;
3. ajuster (X ; Z) par la droite de régression z = ax + b ;
4. revenir à Y par la fonction réciproque (exp pour ln, le carré pour la racine, l'inverse pour 1/n) avant toute prévision.

Cas limite : ln n'existe que pour Y > 0 ; une valeur de Y nulle ou négative interdit le changement Z = ln Y.

:::

::: verifie À toi : une racine carrée
On pose Z = √Y et l'ajustement de (X ; Z) donne z = 0,5x + 1 avec r ≈ 0,99. Quelle valeur de Y prévoit-on pour x = 6 ?

---

Pour x = 6, z = 0,5 × 6 + 1 = 4. Mais z = √Y, donc on revient à Y en élevant au carré : Y = 4² = 16. Lire directement 4 serait la même erreur que de prendre z pour y.
:::

::: retenir
Un nuage courbe se redresse par un changement de variable (ln Y, √Y, 1/n) : on vérifie r sur (X ; Z), on ajuste z = ax + b, puis on revient à Y par la fonction réciproque.
:::

> 🏆 Les sept notions sont acquises : tu lis un tableau à double entrée, tu places le nuage et son point moyen, tu traces la droite de Mayer, tu mesures la liaison par la covariance et par r, tu prévois par les droites de régression et tu redresses un nuage courbe par un changement de variable. Tu as fini le manuel : tu peux affronter le quiz, puis les missions.
