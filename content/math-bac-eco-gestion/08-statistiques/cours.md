# ⚔️ Statistiques — du nuage de points à la droite de prévision

> 💡 « Une seule série décrit un phénomène ; deux séries relevées sur les mêmes individus racontent comment les deux grandeurs varient ensemble. »

Bienvenue, héros de l'Économie et gestion. Une boutique se demande combien elle gagne en plus pour chaque dinar de publicité, un marché cherche le prix où l'offre rencontre la demande : dans les deux cas, il faut passer de quelques relevés à une règle qui prévoit. Huit étapes te mènent du nuage de points à cette règle : le point moyen, la covariance, l'effet d'un changement d'unité, les deux droites de régression, le coefficient de corrélation, la droite de Mayer, puis les ajustements qui ne sont pas des droites. On suppose acquis la moyenne et la variance d'une série simple, ainsi que ln et l'exponentielle. À chaque étape, les calculs se font à la main, la calculatrice ou le tableur servant de contrôle.

## 🔵 Nuage de points et point moyen

La boutique Sahar, à Sousse, relève pendant cinq mois ses dépenses de publicité x (en centaines de dinars) et son chiffre d'affaires y (en milliers de dinars).

| Mois | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- |
| Publicité x | 2 | 4 | 5 | 7 | 9 |
| Chiffre d'affaires y | 14 | 18 | 19 | 25 | 29 |

Comment résumer ces cinq mois par un seul point, et le chiffre d'affaires semble-t-il monter avec la publicité ?

::: definition
Une **série statistique double** est une liste de couples (xᵢ ; yᵢ), i = 1, …, n, relevés sur les mêmes individus. Dans un repère orthogonal, les points Mᵢ(xᵢ ; yᵢ) forment le **nuage de points**. Le **point moyen** est G(x̄ ; ȳ), où x̄ = (x₁ + … + xₙ)/n et ȳ = (y₁ + … + yₙ)/n.
:::

::: figure Le nuage des cinq mois (points noirs) : il est allongé et monte de la gauche vers la droite ; la croix ambre marque le point moyen G(5,4 ; 21), qui n'est pas l'un des points relevés
<svg viewBox="0 0 340 250">
<title>Nuage des cinq points (2 ; 14), (4 ; 18), (5 ; 19), (7 ; 25), (9 ; 29) et point moyen G(5,4 ; 21)</title>
<line x1="103.6" y1="208" x2="103.6" y2="22" stroke="#e2e8f0" stroke-width="1"/>
<line x1="157.2" y1="208" x2="157.2" y2="22" stroke="#e2e8f0" stroke-width="1"/>
<line x1="210.8" y1="208" x2="210.8" y2="22" stroke="#e2e8f0" stroke-width="1"/>
<line x1="264.4" y1="208" x2="264.4" y2="22" stroke="#e2e8f0" stroke-width="1"/>
<line x1="318.0" y1="208" x2="318.0" y2="22" stroke="#e2e8f0" stroke-width="1"/>
<line x1="50" y1="154.9" x2="318" y2="154.9" stroke="#e2e8f0" stroke-width="1"/>
<line x1="50" y1="101.7" x2="318" y2="101.7" stroke="#e2e8f0" stroke-width="1"/>
<line x1="50" y1="48.6" x2="318" y2="48.6" stroke="#e2e8f0" stroke-width="1"/>
<path d="M50 22 L50 208 L318 208" fill="none" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/>
<line x1="103.6" y1="208" x2="103.6" y2="212" stroke="#0f172a" stroke-width="1.2"/>
<text x="103.6" y="224" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >2</text>
<line x1="157.2" y1="208" x2="157.2" y2="212" stroke="#0f172a" stroke-width="1.2"/>
<text x="157.2" y="224" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >4</text>
<line x1="210.8" y1="208" x2="210.8" y2="212" stroke="#0f172a" stroke-width="1.2"/>
<text x="210.8" y="224" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >6</text>
<line x1="264.4" y1="208" x2="264.4" y2="212" stroke="#0f172a" stroke-width="1.2"/>
<text x="264.4" y="224" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >8</text>
<line x1="318.0" y1="208" x2="318.0" y2="212" stroke="#0f172a" stroke-width="1.2"/>
<text x="318.0" y="224" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >10</text>
<line x1="46" y1="154.9" x2="50" y2="154.9" stroke="#0f172a" stroke-width="1.2"/>
<text x="43" y="158.9" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >10</text>
<line x1="46" y1="101.7" x2="50" y2="101.7" stroke="#0f172a" stroke-width="1.2"/>
<text x="43" y="105.7" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >20</text>
<line x1="46" y1="48.6" x2="50" y2="48.6" stroke="#0f172a" stroke-width="1.2"/>
<text x="43" y="52.6" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >30</text>
<text x="318" y="237" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >x (centaines de dinars)</text>
<text x="54" y="17" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >y (milliers de dinars)</text>
<circle cx="103.6" cy="133.6" r="4" fill="#0f172a" stroke="#ffffff" stroke-width="1"/>
<circle cx="157.2" cy="112.3" r="4" fill="#0f172a" stroke="#ffffff" stroke-width="1"/>
<circle cx="184.0" cy="107.0" r="4" fill="#0f172a" stroke="#ffffff" stroke-width="1"/>
<circle cx="237.6" cy="75.1" r="4" fill="#0f172a" stroke="#ffffff" stroke-width="1"/>
<circle cx="291.2" cy="53.9" r="4" fill="#0f172a" stroke="#ffffff" stroke-width="1"/>
<line x1="189.7" y1="91.4" x2="199.7" y2="101.4" stroke="#b45309" stroke-width="2.6" stroke-linecap="round"/><line x1="189.7" y1="101.4" x2="199.7" y2="91.4" stroke="#b45309" stroke-width="2.6" stroke-linecap="round"/>
<text x="203.7" y="114.4" text-anchor="start" font-size="13" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >G</text>
</svg>
:::

Sur la figure, les points se rangent le long d'une bande ascendante : quand x augmente, y augmente aussi. Le point G se situe au centre de cette bande.

::: exemple Le point moyen de la boutique Sahar
1. Moyenne des abscisses : x̄ = (2 + 4 + 5 + 7 + 9)/5 = 27/5 = 5,4 centaines de dinars.
2. Moyenne des ordonnées : ȳ = (14 + 18 + 19 + 25 + 29)/5 = 105/5 = 21 milliers de dinars.
3. Donc G(5,4 ; 21). Aucun mois n'a ces coordonnées exactes : le point moyen résume le nuage sans en faire partie.

:::

::: piege Prendre la ligne du milieu pour le point moyen
On lit la ligne du mois 3, (5 ; 19), parce qu'elle est au centre du tableau. Cela tente car cinq lignes ont une ligne centrale. Mais le point moyen se calcule avec **toutes** les valeurs : ici ȳ = 21, pas 19. Prendre la valeur du milieu donnerait la médiane, une autre notion.
:::

::: propriete
- Le point moyen s'obtient avec une moyenne sur chaque variable, séparément.
- Si une variable est donnée par classes, on remplace chaque classe par son centre : [20 ; 30[ devient 25.

Cas limite : le point moyen n'est pas forcément un point du nuage, comme le montre G(5,4 ; 21) ci-dessus.
:::

::: verifie
Les durées de 10 livraisons sont réparties ainsi : 4 livraisons dans [20 ; 30[ et 6 dans [30 ; 50[. Quelle est la durée moyenne approchée ?

---

Les centres des classes sont 25 et 40. La moyenne approchée vaut (4 × 25 + 6 × 40)/10 = (100 + 240)/10 = 34 minutes.
:::

::: retenir
Un nuage de points représente les couples (xᵢ ; yᵢ) ; son point moyen G(x̄ ; ȳ) se calcule avec toutes les valeurs, classes remplacées par leurs centres.
:::

## 🤝 La covariance : varier ensemble

Sur le nuage de la boutique Sahar, la publicité et le chiffre d'affaires montent ensemble. La variance mesure la dispersion d'une seule variable autour de sa moyenne.
Existe-t-il un nombre qui mesure comment deux variables s'écartent **ensemble** de leurs moyennes ?

::: definition
La **covariance** de x et y est le nombre
$$ cov(x ; y) = (1/n) × Σ (xᵢ − x̄)(yᵢ − ȳ) $$
Elle se calcule plus facilement par
$$ cov(x ; y) = (1/n) × Σ xᵢyᵢ − x̄ × ȳ $$
c'est-à-dire la moyenne des produits moins le produit des moyennes. On a cov(x ; y) = cov(y ; x) et cov(x ; x) = V(x).
:::

::: exemple La covariance de la boutique Sahar
1. Les produits xᵢyᵢ valent 2 × 14 = 28, 4 × 18 = 72, 5 × 19 = 95, 7 × 25 = 175 et 9 × 29 = 261, de somme 631.
2. La moyenne des produits est 631/5 = 126,2, et x̄ × ȳ = 5,4 × 21 = 113,4.
3. Donc cov(x ; y) = 126,2 − 113,4 = 12,8.
4. Contrôle par la définition : les écarts à la moyenne sont −3,4 ; −1,4 ; −0,4 ; 1,6 ; 3,6 pour x et −7 ; −3 ; −2 ; 4 ; 8 pour y. Leurs produits valent 23,8 ; 4,2 ; 0,8 ; 6,4 ; 28,8, de somme 64, et 64/5 = 12,8 ✓.

:::

::: piege Oublier de retrancher le produit des moyennes
On s'arrête à la moyenne des produits et on annonce cov(x ; y) = 126,2. Cela tente parce que le calcul de 631/5 est long et ressemble à un résultat final. Mais c'est la moitié de la formule : il faut encore retrancher x̄ × ȳ = 113,4, ce qui donne 12,8.
:::

::: propriete
- cov(x ; y) > 0 : les deux variables ont tendance à varier dans le même sens ; cov(x ; y) < 0 : en sens contraire.
- cov(x ; x) = V(x) ≥ 0 : la variance est la covariance d'une variable avec elle-même.

Cas limite : une covariance nulle n'exclut pas toute dépendance ; un nuage en parabole peut avoir une covariance nulle alors que y dépend de x.
:::

::: verifie
Un papetier relève le prix x (en dinars) d'un article : 1 ; 2 ; 3 ; 6, et les ventes y (en dizaines) : 9 ; 7 ; 5 ; 3. Calculer cov(x ; y).

---

x̄ = 12/4 = 3 et ȳ = 24/4 = 6. Les produits valent 9 + 14 + 15 + 18 = 56, donc la moyenne des produits est 14. Alors cov(x ; y) = 14 − 3 × 6 = −4. Le signe négatif traduit que les ventes baissent quand le prix monte.
:::

::: retenir
cov(x ; y) = moyenne des produits xᵢyᵢ moins x̄ × ȳ ; son signe donne le sens commun de variation, et cov(x ; x) = V(x).
:::

## 🔧 Changer d'origine ou d'unité

Le comptable de la boutique Sahar trouve les chiffres encombrants : il remplace les dépenses de publicité x par x′ = x − 5 (écart à 5 centaines) et exprime le chiffre d'affaires en dizaines de milliers, y′ = y/10.
Que devient la covariance, sans tout recalculer ?

::: definition
Pour tous réels α, β (propriétés admises) :
$$ cov(x + α ; y + β) = cov(x ; y) $$
$$ cov(αx ; βy) = αβ × cov(x ; y) $$
Ensemble, pour x′ = αx + γ et y′ = βy + δ : cov(x′ ; y′) = αβ × cov(x ; y).
:::

::: exemple Les nouvelles unités de la boutique
1. x′ = x − 5 est un décalage (α = 1, γ = −5) : il ne change aucun écart à la moyenne, donc pas la covariance.
2. y′ = y/10 multiplie tous les écarts par β = 0,1.
3. Donc cov(x′ ; y′) = 1 × 0,1 × 12,8 = 1,28.
4. Contrôle : les nouvelles valeurs x′ valent −3 ; −1 ; 0 ; 2 ; 4 et y′ valent 1,4 ; 1,8 ; 1,9 ; 2,5 ; 2,9. La moyenne des produits est (−4,2 − 1,8 + 0 + 5 + 11,6)/5 = 2,12, et 0,4 × 2,1 = 0,84 ; on retrouve 2,12 − 0,84 = 1,28 ✓.

:::

::: piege Ajouter la constante à la covariance
On écrit cov(x′ ; y) = 12,8 − 5 = 7,8 pour x′ = x − 5. Cela tente parce que la moyenne, elle, bouge de −5. Mais la covariance mesure des écarts **à la moyenne** : un décalage translate la moyenne avec les valeurs et ne change aucun écart. La covariance reste 12,8.
:::

::: propriete
- Un décalage (+ α, + β) ne change pas la covariance ; un changement d'échelle (× α, × β) la multiplie par αβ.
- La covariance dépend donc des unités choisies ; cette gêne conduira au coefficient de corrélation, plus bas.

Cas limite : si αβ < 0, la covariance change de signe ; par exemple cov(−x ; y) = −cov(x ; y).
:::

::: verifie
On sait que cov(x ; y) = −4 (le papetier). Il exprime maintenant les prix en millimes, x′ = 1000x, et retranche 2 aux ventes, y′ = y − 2. Que vaut cov(x′ ; y′) ?

---

Le décalage −2 n'agit pas ; seul le facteur 1000 compte : cov(x′ ; y′) = 1000 × 1 × (−4) = −4000.
:::

::: retenir
Un décalage laisse la covariance intacte, un changement d'échelle la multiplie par le produit des facteurs : cov(αx + γ ; βy + δ) = αβ × cov(x ; y).
:::

## 📈 La droite de régression de y en x

La boutique Sahar prépare une campagne à 12 centaines de dinars. Pour prévoir le chiffre d'affaires, on cherche la droite qui passe « au plus près » des cinq points.
Comment choisir cette droite, et pas une autre ?

::: definition
Pour une droite D d'équation y = ax + b et un point Mᵢ(xᵢ ; yᵢ), le **résidu** est l'écart vertical yᵢ − (axᵢ + b). La **méthode des moindres carrés** retient la droite qui rend minimale la **somme des carrés des résidus** S = Σ (yᵢ − axᵢ − b)². C'est la **droite de régression de y en x** ; elle existe et est unique (admis, V(x) ≠ 0) : elle passe par G(x̄ ; ȳ) et son coefficient directeur est
$$ a = cov(x ; y) / V(x) $$
Son équation réduite est y = a(x − x̄) + ȳ.
:::

::: figure La droite de régression de y en x (trait vert) traverse le nuage et passe par le point moyen G (croix ambre) : c'est la droite qui rend minimale la somme des carrés des écarts verticaux entre les points et la droite
<svg viewBox="0 0 340 250">
<title>Nuage des cinq points, point moyen G(5,4 ; 21) et droite de régression de y en x : y = 2,19x + 9,16</title>
<line x1="103.6" y1="208" x2="103.6" y2="22" stroke="#e2e8f0" stroke-width="1"/>
<line x1="157.2" y1="208" x2="157.2" y2="22" stroke="#e2e8f0" stroke-width="1"/>
<line x1="210.8" y1="208" x2="210.8" y2="22" stroke="#e2e8f0" stroke-width="1"/>
<line x1="264.4" y1="208" x2="264.4" y2="22" stroke="#e2e8f0" stroke-width="1"/>
<line x1="318.0" y1="208" x2="318.0" y2="22" stroke="#e2e8f0" stroke-width="1"/>
<line x1="50" y1="154.9" x2="318" y2="154.9" stroke="#e2e8f0" stroke-width="1"/>
<line x1="50" y1="101.7" x2="318" y2="101.7" stroke="#e2e8f0" stroke-width="1"/>
<line x1="50" y1="48.6" x2="318" y2="48.6" stroke="#e2e8f0" stroke-width="1"/>
<path d="M50 22 L50 208 L318 208" fill="none" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/>
<line x1="103.6" y1="208" x2="103.6" y2="212" stroke="#0f172a" stroke-width="1.2"/>
<text x="103.6" y="224" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >2</text>
<line x1="157.2" y1="208" x2="157.2" y2="212" stroke="#0f172a" stroke-width="1.2"/>
<text x="157.2" y="224" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >4</text>
<line x1="210.8" y1="208" x2="210.8" y2="212" stroke="#0f172a" stroke-width="1.2"/>
<text x="210.8" y="224" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >6</text>
<line x1="264.4" y1="208" x2="264.4" y2="212" stroke="#0f172a" stroke-width="1.2"/>
<text x="264.4" y="224" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >8</text>
<line x1="318.0" y1="208" x2="318.0" y2="212" stroke="#0f172a" stroke-width="1.2"/>
<text x="318.0" y="224" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >10</text>
<line x1="46" y1="154.9" x2="50" y2="154.9" stroke="#0f172a" stroke-width="1.2"/>
<text x="43" y="158.9" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >10</text>
<line x1="46" y1="101.7" x2="50" y2="101.7" stroke="#0f172a" stroke-width="1.2"/>
<text x="43" y="105.7" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >20</text>
<line x1="46" y1="48.6" x2="50" y2="48.6" stroke="#0f172a" stroke-width="1.2"/>
<text x="43" y="52.6" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >30</text>
<text x="318" y="237" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >x (centaines de dinars)</text>
<text x="54" y="17" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >y (milliers de dinars)</text>
<line x1="50.0" y1="159.3" x2="318.0" y2="42.8" stroke="#0f6e56" stroke-width="2.4" stroke-linecap="round"/>
<circle cx="103.6" cy="133.6" r="4" fill="#0f172a" stroke="#ffffff" stroke-width="1"/>
<circle cx="157.2" cy="112.3" r="4" fill="#0f172a" stroke="#ffffff" stroke-width="1"/>
<circle cx="184.0" cy="107.0" r="4" fill="#0f172a" stroke="#ffffff" stroke-width="1"/>
<circle cx="237.6" cy="75.1" r="4" fill="#0f172a" stroke="#ffffff" stroke-width="1"/>
<circle cx="291.2" cy="53.9" r="4" fill="#0f172a" stroke="#ffffff" stroke-width="1"/>
<line x1="189.7" y1="91.4" x2="199.7" y2="101.4" stroke="#b45309" stroke-width="2.6" stroke-linecap="round"/><line x1="189.7" y1="101.4" x2="199.7" y2="91.4" stroke="#b45309" stroke-width="2.6" stroke-linecap="round"/>
<text x="203.7" y="114.4" text-anchor="start" font-size="13" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >G</text>
</svg>
:::

La droite monte comme le nuage et traverse G : elle sert à lire une prévision en y pour un x donné.

::: exemple La droite de la boutique Sahar
1. La moyenne des carrés des x vaut (4 + 16 + 25 + 49 + 81)/5 = 35, donc V(x) = 35 − 5,4² = 35 − 29,16 = 5,84.
2. Le coefficient directeur est a = 12,8/5,84 ≈ 2,19 : chaque centaine de dinars de publicité va avec environ 2,19 milliers de dinars de chiffre d'affaires en plus.
3. La droite passe par G(5,4 ; 21) : y = 2,19(x − 5,4) + 21, soit y ≈ 2,19x + 9,16.
4. Pour x = 6 (entre 2 et 9, valeurs observées) : y ≈ 2,19 × 6 + 9,16 ≈ 22,3 milliers de dinars. Pour la campagne x = 12, hors de l'intervalle observé : y ≈ 2,19 × 12 + 9,16 ≈ 35,4, une extrapolation moins sûre.

:::

::: piege Diviser par la variance de y
On calcule a = 12,8/28,4 ≈ 0,45 « parce que y est la variable qu'on veut prévoir ». Cela tente car on parle de prévoir y. Mais le coefficient d'une droite y = ax + b se divise par la variance de la variable **placée en abscisse**, x : a = cov(x ; y)/V(x) = 12,8/5,84. Le nombre 0,45 est la pente d'une autre droite, vue à l'étape suivante.
:::

::: propriete
- a a le signe de cov(x ; y), puisque V(x) > 0 : la droite monte si les variables varient dans le même sens.
- Une prévision dans l'intervalle des x observés s'appelle une interpolation, en dehors une extrapolation, d'autant moins fiable qu'on s'éloigne des données.

Cas limite : si tous les xᵢ sont égaux, V(x) = 0 et la division est impossible : les points sont sur une verticale, il n'y a pas de droite de régression de y en x.
:::

::: verifie
Une série a pour point moyen G(4 ; 30), cov(x ; y) = 18 et V(x) = 9. Donner l'équation réduite de la droite de régression de y en x.

---

a = 18/9 = 2. La droite passe par G : y = 2(x − 4) + 30 = 2x − 8 + 30, soit y = 2x + 22. Contrôle : pour x = 4, on retrouve 2 × 4 + 22 = 30 ✓.
:::

::: retenir
Droite de régression de y en x : elle passe par G, de coefficient a = cov(x ; y)/V(x), soit y = a(x − x̄) + ȳ ; elle minimise la somme des carrés des résidus.
:::

## 🔄 La droite de régression de x en y

Le gérant de la boutique Sahar inverse la question : il vise 40 milliers de dinars de chiffre d'affaires et veut savoir quelle publicité prévoir. La variable qu'on cherche est maintenant x.
Suffit-il de retourner l'équation de y en x ?

::: definition
La **droite de régression de x en y** est la droite des moindres carrés où les rôles sont échangés : on mesure les écarts horizontaux. Elle passe par G(x̄ ; ȳ), et son équation est
$$ x − x̄ = a′ × (y − ȳ) avec a′ = cov(x ; y) / V(y) $$
:::

::: exemple Quelle publicité pour 40 milliers de dinars ?
1. V(y) = (196 + 324 + 361 + 625 + 841)/5 − 21² = 469,4 − 441 = 28,4, donc a′ = 12,8/28,4 ≈ 0,451.
2. La droite est x − 5,4 = 0,451(y − 21).
3. Pour y = 40 : x ≈ 5,4 + 0,451 × 19 ≈ 13,96 centaines de dinars, soit environ 1 400 dinars de publicité.
4. En retournant la droite de y en x, on aurait x = (40 − 9,16)/2,19 ≈ 14,07 : un résultat voisin, mais différent.

:::

::: piege Retourner l'équation de y en x
On résout y = 2,19x + 9,16 pour x et on obtient 14,07. Cela tente parce qu'une droite se retourne toujours algébriquement. Mais la droite de y en x minimise les écarts verticaux, pas les écarts horizontaux : pour estimer x à partir de y, on emploie la droite de x en y, dont le résultat est 13,96. Les deux ne coïncident que si les points sont alignés.
:::

::: propriete
- Les deux droites de régression passent par G ; elles se coupent donc en G.
- Leurs coefficients cov(x ; y)/V(x) et cov(x ; y)/V(y) ont le même signe que cov(x ; y).

Cas limite : si les points sont exactement alignés, les deux droites sont confondues ; sinon elles sont distinctes, et d'autant plus proches que le nuage est étroit.
:::

::: verifie
Reprenons la série de l'exercice précédent (G(4 ; 30), cov(x ; y) = 18, V(x) = 9), on donne aussi V(y) = 40. Quelle valeur de x prévoit-on pour y = 50 ?

---

a′ = 18/40 = 0,45. La droite de x en y est x − 4 = 0,45(y − 30). Pour y = 50 : x = 4 + 0,45 × 20 = 13.
:::

::: retenir
Pour estimer x à partir de y, on emploie la droite de x en y : x − x̄ = a′(y − ȳ) avec a′ = cov(x ; y)/V(y) ; elle ne s'obtient pas en retournant celle de y en x.
:::

## 🎚️ Le coefficient de corrélation linéaire

La droite de la boutique Sahar prévoit bien si les points sont presque alignés, mal s'ils sont dispersés. Regarder le nuage à l'œil nu ne suffit pas pour décider.
Quel nombre mesure à quel point les points sont alignés, sans dépendre des unités ?

::: definition
Le **coefficient de corrélation linéaire** de x et y est
$$ r = cov(x ; y) / (σx × σy) $$
où σx = √V(x) et σy = √V(y) sont les écarts types. On admet que −1 ≤ r ≤ 1, et que |r| = 1 si et seulement si les points sont alignés (le manuel dit alors qu'il y a **dépendance totale** entre x et y : l'une est fonction affine de l'autre). Pour un ajustement affine :
- |r| ≤ 0,70 : corrélation **faible** ;
- 0,70 < |r| ≤ 0,95 : corrélation **forte** ;
- 0,95 < |r| ≤ 1 : corrélation **très forte**.
:::

::: exemple Corrélation de la boutique Sahar
1. σx = √5,84 ≈ 2,417 et σy = √28,4 ≈ 5,329.
2. r = 12,8/(2,417 × 5,329) ≈ 12,8/12,88 ≈ 0,994.
3. 0,994 > 0,95 : corrélation très forte, l'ajustement affine est justifié.
4. Pour le papetier du calcul de covariance, cov = −4, V(x) = 3,5 et V(y) = 5 : r = −4/√17,5 ≈ −0,956. Le signe négatif dit que les ventes baissent quand le prix monte ; la valeur absolue 0,956 > 0,95 donne aussi une corrélation très forte.

:::

::: piege Conclure à une cause
Un gérant trouve r = 0,96 entre les ventes mensuelles de climatiseurs et le nombre de baignades, et en déduit que les climatiseurs poussent à se baigner. Cela tente parce qu'un r proche de 1 paraît établir un lien solide. Mais r mesure seulement l'alignement des deux séries : ici, la chaleur fait monter les deux. Une forte corrélation n'établit jamais que x cause y ; l'interprétation relève du spécialiste du domaine.
:::

::: propriete
- r a le signe de cov(x ; y) et ne dépend pas des unités choisies.
- Le produit des deux coefficients directeurs vaut a × a′ = cov²/(V(x)V(y)) = r² : plus |r| est proche de 1, plus les deux droites se rapprochent.

Cas limite : r = 0 ne signifie pas « aucun lien », seulement « aucun lien affine » ; un nuage en parabole peut donner r proche de 0.
:::

::: verifie
Pour une série, cov(x ; y) = −30, σx = 5 et σy = 8. Calculer r et qualifier la corrélation.

---

r = −30/(5 × 8) = −0,75. Comme 0,70 < 0,75 ≤ 0,95, la corrélation est forte ; elle est négative, car r a le signe de la covariance.
:::

::: retenir
r = cov(x ; y)/(σx σy) ∈ [−1 ; 1] ; |r| ≤ 0,70 faible, de 0,70 à 0,95 forte, au-delà de 0,95 très forte ; une corrélation n'est jamais une preuve de causalité.
:::

## ✂️ La droite de Mayer

Pour la boutique Sahar, on voudrait une droite rapide, sans variance ni covariance : un nuage allongé se résume par deux « centres de gravité », un pour les petites valeurs de x, un pour les grandes.
Comment tracer la droite qui relie ces deux centres ?

::: definition
**Méthode de Mayer** : on range les points par abscisses croissantes et on les partage en deux groupes dont les effectifs diffèrent d'au plus un (le premier groupe prend le point supplémentaire si n est impair). On note G₁ et G₂ les points moyens des deux groupes. La droite (G₁G₂) est la **droite de Mayer**.
:::

::: exemple La droite de Mayer de la boutique Sahar
1. Les cinq points sont déjà rangés par abscisses croissantes : on forme un groupe de 3 points (x = 2, 4, 5) et un groupe de 2 points (x = 7, 9).
2. G₁ a pour coordonnées ((2 + 4 + 5)/3 ; (14 + 18 + 19)/3) = (11/3 ; 17), et G₂ = ((7 + 9)/2 ; (25 + 29)/2) = (8 ; 27).
3. Le coefficient directeur est (27 − 17)/(8 − 11/3) = 10/(13/3) = 30/13 ≈ 2,31.
4. La droite passe par G₂ : y = 27 + (30/13)(x − 8), soit y ≈ 2,31x + 8,54. Contrôle : elle passe par G(5,4 ; 21), car 2,3077 × 5,4 + 8,538 ≈ 21 ✓.

:::

::: piege Partager sans ranger
Un tableau donne les mois dans l'ordre du calendrier, avec des dépenses x de 7, 2, 9, 4, 5. On prend les trois premières lignes comme premier groupe. Cela tente parce que le tableau est déjà en colonnes. Mais les groupes doivent séparer les petites valeurs de x des grandes : il faut d'abord ranger par x croissants (2, 4, 5, 7, 9), sinon G₁(6 ; 22,7) se retrouve à droite de G₂(4,5 ; 18,5) : les groupes ne séparent plus les petites valeurs de x des grandes, et la droite obtenue (pente ≈ 2,78 au lieu de 2,31) n'a plus de justification.
:::

::: propriete
- Le point moyen G de toute la série appartient toujours à la droite de Mayer : c'est le point moyen de G₁ et G₂ pondérés par les effectifs des deux groupes.
- La droite de Mayer n'est en général pas la droite de régression ; sa somme de carrés des résidus est supérieure ou égale à celle de la droite de régression.

Cas limite : si n est pair, les deux groupes ont le même effectif, n/2 points chacun.
:::

::: verifie
Quatre points : (1 ; 3), (2 ; 6), (5 ; 11), (6 ; 14). Donner l'équation de la droite de Mayer.

---

Deux groupes de 2 points : G₁(1,5 ; 4,5) et G₂(5,5 ; 12,5). Le coefficient directeur vaut (12,5 − 4,5)/(5,5 − 1,5) = 2. La droite est y − 4,5 = 2(x − 1,5), soit y = 2x + 1,5.
:::

::: retenir
Droite de Mayer : points rangés par x croissants, deux groupes d'effectifs presque égaux, droite (G₁G₂) ; elle passe par G.
:::

## 🧬 Quand le nuage n'est pas une droite : changer de variable

Sur un marché, la quantité demandée d'un produit baisse quand le prix monte, mais en s'aplatissant : le nuage est courbé, et une droite s'en écarterait. Voici le prix x (en dinars le kilo) et la demande y (en milliers de kilos).

| Prix x | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- |
| Demande y | 7 | 5 | 3,5 | 2,5 | 1,7 |

Comment ajuster une courbe avec les outils de la droite, et où l'offre rencontre-t-elle cette demande ?

::: definition
Un **ajustement non affine** se ramène à un ajustement affine par un **changement de variable** :
- **exponentiel** : on pose Y = ln y, on ajuste la droite de Y en x, Y = ax + b, puis y = e^(ax + b) ;
- **logarithmique** : on pose X = ln x, on ajuste la droite de y en X, y = aX + b, puis y = a ln x + b ;
- d'autres changements (√y, 1/y, x²) suivent le même principe ;
- **courbe imposée** : on choisit la forme (parabole y = ax² + bx + c, fonction homographique…) et on fixe ses coefficients en la faisant passer par des points choisis du nuage.

Le **prix d'équilibre** est le prix où l'offre égale la demande.
:::

::: exemple La demande, puis l'équilibre
1. On pose z = ln y : les valeurs sont 1,95 ; 1,61 ; 1,25 ; 0,92 ; 0,53 (arrondies au centième). Le nuage (x ; z) est quasi aligné : r ≈ −0,9997.
2. La droite des moindres carrés de z en x est z ≈ −0,35x + 2,31, d'où la demande f(x) = e^(2,31 − 0,35x) ≈ 10,07 × e^(−0,35x).
3. L'offre, ajustée par une droite, est g(x) = 0,5x + 1,5 (valeurs choisies pour l'exemple). On cherche f(x) = g(x).
4. Posons h = f − g : f décroît et g croît, donc h décroît strictement, et h(x) = 0 a au plus une solution. Or h(3) ≈ 3,53 − 3 > 0 et h(3,5) ≈ 2,96 − 3,25 < 0 : la solution est entre 3 et 3,5. De plus h(3,3) ≈ 0,02 > 0 et h(3,4) ≈ −0,14 < 0, donc le prix d'équilibre vaut environ 3,3 dinars le kilo, pour une quantité d'environ 3,2 milliers de kilos.

:::

::: exemple Une parabole imposée par trois points
1. On choisit la forme y = ax² + bx + c et trois points du nuage : (1 ; 3), (2 ; 4) et (3 ; 7).
2. On écrit a + b + c = 3, 4a + 2b + c = 4 et 9a + 3b + c = 7.
3. En retranchant la première équation à la deuxième, puis la deuxième à la troisième : 3a + b = 1 et 5a + b = 3, donc a = 1, b = −2 et c = 4 (système 3 × 3 du chapitre 07).
4. La parabole est y = x² − 2x + 4. Contrôle : en x = 2, 4 − 4 + 4 = 4 ✓.

:::

::: piege Lire la droite comme si elle donnait y
Pour un prix x = 4, on calcule z = −0,35 × 4 + 2,31 = 0,91 et on annonce une demande de 0,91 millier de kilos. Cela tente parce que 0,91 sort directement de la droite. Mais la droite donne z = ln y, pas y : il faut revenir par l'exponentielle, y = e^(0,91) ≈ 2,48 milliers de kilos.
:::

::: propriete
- On choisit le changement de variable d'après la forme du nuage ; on contrôle ensuite par le coefficient de corrélation de la série transformée.
- Le retour à la variable d'origine est indispensable avant toute prévision ; ln n'existe que pour des valeurs strictement positives.

Cas limite : un seul ajustement ne vaut que sur l'intervalle étudié ; hors de lui, une courbe exponentielle ou logarithmique peut donner des valeurs absurdes.
:::

::: verifie
Un ajustement exponentiel a donné ln y = −0,2x + 3. Quelle est la valeur de y prévue pour x = 5 (valeur choisie pour l'exercice) ?

---

On calcule d'abord ln y = −0,2 × 5 + 3 = 2, puis on revient à y : y = e² ≈ 7,39.
:::

::: retenir
Un nuage courbé se redresse par changement de variable (Y = ln y, X = ln x, …) ; on ajuste la droite, puis on revient à y avant de prévoir, et le prix d'équilibre résout offre = demande.
:::
