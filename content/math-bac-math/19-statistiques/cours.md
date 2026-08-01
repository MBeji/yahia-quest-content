# ⚔️ Statistiques — deux mesures, une seule droite

> 💡 «Mesurer une grandeur, tu sais faire. Ici on en mesure **deux** sur le même individu — et la seule question qui compte devient : est-ce que l'une raconte l'autre ?»

En 1669, Huygens dépouille les relevés de décès de Londres et écrit à son frère : sur 100 personnes, 64 atteignent 6 ans, 40 atteignent 16 ans, 25 atteignent 26 ans… Il en tire une moyenne — l'espérance de vie — et prend soin d'ajouter que ce n'est **pas** une prédiction pour un enfant donné. Toute la statistique tient dans cette prudence. Tu sais déjà résumer **une** série par sa moyenne et son écart-type ; ce dernier chapitre du programme te donne l'outil qui manque pour **deux** séries à la fois : la covariance, la droite d'ajustement et le nombre qui dit si cette droite mérite qu'on lui fasse confiance.

## 🏰 Deux caractères sur le même individu

On interroge 20 logements d'un quartier. Sur **chaque** logement on relève deux nombres : X = le nombre de pièces habitées, Y = le nombre d'enfants. Chaque logement fournit donc un **couple** (xᵢ, yᵢ), pas un nombre isolé.

> **Définitions** — « Soit (X, Y) une série statistique double sur un échantillon de taille n et soit (xᵢ, yᵢ), 1 ≤ i ≤ n, les valeurs numériques prises respectivement par les variables X et Y. La distribution marginale de la variable X est la distribution des valeurs xᵢ, 1 ≤ i ≤ n, prises par la variable X. La distribution marginale de la variable Y est la distribution des valeurs yᵢ, 1 ≤ i ≤ n, prises par la variable Y. »

Les résultats se rangent dans un **tableau à double entrée** : la case (i, j) contient l'effectif nᵢⱼ des individus pour lesquels X vaut xᵢ **et** Y vaut yⱼ.

| Effectifs nᵢⱼ | Y = 0 | Y = 1 | Y = 2 | **Total** |
| ------------- | ----- | ----- | ----- | --------- |
| X = 1         | 5     | 2     | 1     | **8**     |
| X = 2         | 2     | 4     | 2     | **8**     |
| X = 3         | 0     | 1     | 3     | **4**     |
| **Total**     | **7** | **7** | **6** | **20**    |

La colonne des totaux donne la **distribution marginale de X** : la valeur 1 a l'effectif 8, la valeur 2 l'effectif 8, la valeur 3 l'effectif 4. La ligne des totaux donne celle de **Y** : 7, 7 et 6. Les fréquences s'en déduisent en divisant par n = 20 : pour X, 0,40 ; 0,40 ; 0,20 — et **0,40 + 0,40 + 0,20 = 1** ; pour Y, 0,35 ; 0,35 ; 0,30, de somme 1 elle aussi. Une marge dont les fréquences ne somment pas à 1 est une marge fausse : c'est ton premier contrôle, gratuit.

Chaque marge est alors une série simple ordinaire, et les formules du collège s'y appliquent telles quelles.

> **Définition** — « Soit X une série statistique sur un échantillon de taille n. Si X̄, V(X) et σ_X désignent respectivement la moyenne, la variance et l'écart-type de la série, alors X̄ = (1/n)Σ_(i=1)^(p) nᵢxᵢ, V(X) = (1/n)Σ_(i=1)^(p) nᵢ(xᵢ − X̄)², σ_X = √(V(X)), où les valeurs x₁, x₂, …, x_p désignent les valeurs distinctes prises par la variable X si elle est discrète, ou les centres des classes si la variable X est continue. L'entier nᵢ désigne l'effectif de la valeur xᵢ. »

En développant le carré, on obtient la forme la plus commode au calcul, celle que rend une calculatrice :

$$ V(X) = (1/n)Σ nᵢxᵢ² − X̄² $$

_Exemple détaillé_ — sur la marge de X : Σnᵢxᵢ = 8×1 + 8×2 + 4×3 = 8 + 16 + 12 = 36, donc **X̄ = 36/20 = 1,8**. Puis Σnᵢxᵢ² = 8×1 + 8×4 + 4×9 = 8 + 32 + 36 = 76, donc **V(X) = 76/20 − 1,8² = 3,8 − 3,24 = 0,56** et **σ_X = √0,56 ≈ 0,748**.

_Contrôle par l'autre formule_ — par les écarts : 8(1 − 1,8)² + 8(2 − 1,8)² + 4(3 − 1,8)² = 8(0,64) + 8(0,04) + 4(1,44) = 5,12 + 0,32 + 5,76 = 11,2, et 11,2/20 = **0,56** ✓. Les deux chemins donnent le même nombre : la variance est juste.

_Exemple détaillé (la marge de Y)_ — Σnⱼyⱼ = 7×0 + 7×1 + 6×2 = 19, donc **Ȳ = 19/20 = 0,95**. Σnⱼyⱼ² = 7×0 + 7×1 + 6×4 = 31, donc **V(Y) = 31/20 − 0,95² = 1,55 − 0,9025 = 0,6475** et **σ_Y ≈ 0,805**. _Contrôle_ — 7(0 − 0,95)² + 7(1 − 0,95)² + 6(2 − 0,95)² = 6,3175 + 0,0175 + 6,615 = 12,95, et 12,95/20 = **0,6475** ✓.

> ⚠️ Ne confonds pas l'effectif d'une **case** et celui d'une **marge**. Ici 4 logements ont X = 3 (marge), mais seulement 3 d'entre eux ont aussi Y = 2 (case). Une moyenne calculée sur des cases au lieu des marges est fausse dès la première ligne, et rien ne le signale ensuite.

**Et si la variable est continue ?** La définition l'a dit en une incise, et c'est tout ce qu'il y a à retenir : quand les données arrivent groupées en **classes**, on remplace chaque classe par son **centre** — le centre de la classe [a, b[ vaut (a + b)/2 — puis on applique les mêmes formules, sans rien changer d'autre.

_Exemple détaillé (série groupée en classes)_ — une librairie en ligne relève le montant, en dinars, de 25 commandes.

| Classe [a, b[ | [10, 20[ | [20, 30[ | [30, 40[ | [40, 50[ | **Total** |
| ------------- | -------- | -------- | -------- | -------- | --------- |
| Centre cᵢ     | 15       | 25       | 35       | 45       | —         |
| Effectif nᵢ   | 4        | 9        | 8        | 4        | **25**    |

Contrôle des fréquences d'abord : 0,16 + 0,36 + 0,32 + 0,16 = 1 ✓. Puis Σnᵢcᵢ = 4×15 + 9×25 + 8×35 + 4×45 = 60 + 225 + 280 + 180 = 745, donc **X̄ = 745/25 = 29,8 dinars**. Ensuite Σnᵢcᵢ² = 4×225 + 9×625 + 8×1225 + 4×2025 = 900 + 5625 + 9800 + 8100 = 24 425, donc **V(X) = 24 425/25 − 29,8² = 977 − 888,04 = 88,96** et **σ_X = √88,96 ≈ 9,43 dinars**.

_Contrôle par l'autre formule_ — par les écarts au carré : 4(15 − 29,8)² + 9(25 − 29,8)² + 8(35 − 29,8)² + 4(45 − 29,8)² = 4(219,04) + 9(23,04) + 8(27,04) + 4(231,04) = 876,16 + 207,36 + 216,32 + 924,16 = 2 224, et 2 224/25 = **88,96** ✓.

> ⚠️ Le centre d'une classe n'est **pas** une de ses bornes. Avec les bornes inférieures on trouverait (4×10 + 9×20 + 8×30 + 4×40)/25 = 620/25 = 24,8, avec les bornes supérieures 870/25 = 34,8 : deux moyennes fausses, l'une systématiquement trop basse, l'autre trop haute. Le centre est la seule valeur qui encadre honnêtement la classe — et la vraie moyenne, 29,8, tombe bien entre les deux.

## ⚡ La covariance : mesurer si les deux varient ensemble

X̄ et Ȳ résument chaque variable **séparément** ; elles ne disent rien du lien entre les deux. L'idée est simple : quand X est au-dessus de sa moyenne, Y l'est-il aussi ? Le produit des deux écarts (xᵢ − X̄)(yᵢ − Ȳ) est positif quand ils vont dans le même sens, négatif sinon. La covariance en fait la moyenne.

> **Définition (échantillon simple)** — « Soit (X, Y) une série statistique double sur un échantillon de taille n. On appelle covariance de (X, Y) le réel, noté cov(X, Y) défini par cov(X, Y) = (1/n)Σ_(i=1)^(n) xᵢyᵢ − X̄·Ȳ, où (xᵢ, yᵢ) est la valeur observée pour l'individu i si X et Y sont discrètes, ou le centre de la classe si l'une des variables est continue. »

Comme pour la variance, cette écriture est la forme développée de la moyenne des produits d'écarts — et l'échange des rôles de X et de Y n'y change rien : **cov(X, Y) = cov(Y, X)**.

> **Interprétation** — « La covariance mesure la tendance qu'ont les variables X et Y à varier ensemble. La covariance est **positive** si X et Y ont tendance à varier dans le **même sens**. La covariance est **négative** si X et Y ont tendance à varier en **sens contraire**. »

_Exemple détaillé_ — une bibliothèque numérique compte ses abonnés (en milliers) de 2019 à 2023. On note X le rang de l'année.

| Année                 | 2019 | 2020 | 2021 | 2022 | 2023 |
| --------------------- | ---- | ---- | ---- | ---- | ---- |
| Rang xᵢ               | 1    | 2    | 3    | 4    | 5    |
| Abonnés yᵢ (milliers) | 4    | 8    | 7    | 12   | 15   |

Ici n = 5. Σxᵢ = 15 donc **X̄ = 3** ; Σyᵢ = 4 + 8 + 7 + 12 + 15 = 46 donc **Ȳ = 46/5 = 9,2**. Σxᵢ² = 1 + 4 + 9 + 16 + 25 = 55 donc **V(X) = 55/5 − 3² = 11 − 9 = 2** et σ_X = √2 ≈ 1,414. Σyᵢ² = 16 + 64 + 49 + 144 + 225 = 498 donc **V(Y) = 498/5 − 9,2² = 99,6 − 84,64 = 14,96** et σ_Y ≈ 3,868. Enfin Σxᵢyᵢ = 4 + 16 + 21 + 48 + 75 = 164, d'où :

$$ cov(X, Y) = 164/5 − 3 × 9,2 = 32,8 − 27,6 = 5,2 $$

_Contrôle par les écarts_ — les écarts de Y à Ȳ valent −5,2 ; −1,2 ; −2,2 ; 2,8 ; 5,8, et ceux de X valent −2 ; −1 ; 0 ; 1 ; 2. La somme des produits fait (−2)(−5,2) + (−1)(−1,2) + 0 + (1)(2,8) + (2)(5,8) = 10,4 + 1,2 + 2,8 + 11,6 = 26, et 26/5 = **5,2** ✓. Covariance positive : les deux séries montent ensemble, ce que le tableau laissait deviner.

Quand les données arrivent déjà groupées dans un tableau à double entrée, chaque produit xᵢyⱼ compte autant de fois que son effectif.

> **Définition (échantillon groupé)** — « Soit (X, Y) une série statistique double de taille n. Soit nᵢⱼ le nombre de fois qu'apparaît le couple (xᵢ, yⱼ). Alors cov(X, Y) = (1/n)Σ_(j=1)^(q)Σ_(i=1)^(p) nᵢⱼxᵢyⱼ − X̄·Ȳ. »

_Exemple détaillé_ — reprenons les 20 logements. On balaie le tableau case par case, en ignorant celles où un facteur est nul : ligne X = 1 : 2×(1×1) + 1×(1×2) = 2 + 2 = 4 ; ligne X = 2 : 4×(2×1) + 2×(2×2) = 8 + 8 = 16 ; ligne X = 3 : 1×(3×1) + 3×(3×2) = 3 + 18 = 21. Total ΣΣnᵢⱼxᵢyⱼ = 4 + 16 + 21 = **41**. Avec X̄ = 1,8 et Ȳ = 0,95 :

$$ cov(X, Y) = 41/20 − 1,8 × 0,95 = 2,05 − 1,71 = 0,34 $$

Positive : les logements les plus grands abritent plutôt les familles les plus nombreuses.

> ⚠️ La covariance **dépend des unités**. Passe les abonnés des milliers aux unités et cov(X, Y) est multipliée par 1000 — alors que le lien entre les deux séries, lui, n'a pas bougé d'un cheveu. Une covariance «grande» ou «petite» ne veut donc rien dire toute seule : c'est le coefficient de corrélation, plus loin, qui donnera une échelle absolue.

## 🔮 Le nuage de points et son point moyen

Une série double se voit. On place chaque individu à la position de son couple, et le dessin dit en une seconde ce qu'un tableau cache.

> **Définition** — « Soit (X, Y) une série statistique double de valeurs (xᵢ, yᵢ), 1 ≤ i ≤ n. L'ensemble des points Mᵢ de coordonnées (xᵢ, yᵢ) dans un repère orthogonal est appelé **nuage de points** représentant la série statistique. Le **point moyen** du nuage est le point dont les coordonnées sont les moyennes X̄ et Ȳ. »

::: figure Les cinq abonnements forment une bande qui monte ; le point moyen G(3 ; 9,2) n'est **aucun** des cinq points observés — c'est leur centre d'équilibre.
<svg viewBox="0 0 340 250"><g stroke="#94a3b8" stroke-width="1" fill="none"><path d="M50 160 H310 M50 105 H310 M50 50 H310"/></g><path d="M50 215 H322" fill="none" stroke="#0f172a" stroke-width="1.8"/><path d="M50 215 V32" fill="none" stroke="#0f172a" stroke-width="1.8"/><g stroke="#0f172a" stroke-width="1.4" fill="none"><path d="M90 215 V220 M130 215 V220 M170 215 V220 M210 215 V220 M250 215 V220"/></g><path d="M50 113.8 H170 M170 113.8 V215" fill="none" stroke="#0f6e56" stroke-width="1.6" stroke-dasharray="6 4"/><g fill="#0f172a"><circle cx="90" cy="171" r="4.5"/><circle cx="130" cy="127" r="4.5"/><circle cx="170" cy="138" r="4.5"/><circle cx="210" cy="83" r="4.5"/><circle cx="250" cy="50" r="4.5"/></g><circle cx="170" cy="113.8" r="5.5" fill="#0f6e56"/><g font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="90" y="233" text-anchor="middle" fill="#0f172a">1</text><text x="130" y="233" text-anchor="middle" fill="#0f172a">2</text><text x="170" y="233" text-anchor="middle" fill="#0f172a">3</text><text x="210" y="233" text-anchor="middle" fill="#0f172a">4</text><text x="250" y="233" text-anchor="middle" fill="#0f172a">5</text><text x="38" y="165" text-anchor="middle" fill="#0f172a">5</text><text x="34" y="110" text-anchor="middle" fill="#0f172a">10</text><text x="34" y="55" text-anchor="middle" fill="#0f172a">15</text><text x="186" y="110" text-anchor="middle" fill="#0f6e56">G</text><text x="328" y="233" text-anchor="middle" fill="#0f172a">x</text><text x="42" y="28" text-anchor="middle" fill="#0f172a">y</text></g></svg>
:::

Le nuage sert d'abord à **décider** : si les points s'alignent grossièrement, chercher une droite a un sens ; s'ils dessinent un V, une courbe qui s'infléchit ou un brouillard sans forme, aucune droite ne les résumera. Ce coup d'œil précède tout calcul.

Le texte du manuel pose la question à laquelle tout le reste du chapitre répond : « peut-on prévoir la valeur de Y lorsqu'on connaît la variable X ? […] faire un ajustement affine consiste à déterminer deux réels a et b tels que Y = aX + b soit un modèle acceptable du phénomène étudié. » On dit alors que X est la variable **explicative** et Y la variable **expliquée**, et la droite d'équation y = ax + b est la **droite d'ajustement affine de Y en X**.

## 🗡️ La méthode de Mayer : deux points moyens suffisent

La première méthode ne demande aucune formule savante : on coupe le nuage en deux, on prend le centre de chaque moitié, et on trace la droite qui les joint.

> **Principe de la méthode de Mayer** — « Soit un nuage de points représentant une série statistique double (X, Y) et G son point moyen. On scinde le nuage de points de (X, Y) en deux parties contenant à peu près le même nombre de points. On considère alors les points moyens G₁ et G₂ des deux nuages obtenus. La droite (G₁G₂) définit un ajustement affine du nuage de points représentant la série statistique double (X, Y). La droite (G₁G₂) est appelée **droite de Mayer** et passe par le point moyen G du nuage global. »

_Exemple détaillé_ — sur les abonnés, on sépare les trois premières années des deux dernières. G₁ a pour abscisse (1 + 2 + 3)/3 = 2 et pour ordonnée (4 + 8 + 7)/3 = 19/3 ≈ 6,333, donc **G₁(2 ; 19/3)**. G₂ a pour abscisse (4 + 5)/2 = 4,5 et pour ordonnée (12 + 15)/2 = 13,5, donc **G₂(4,5 ; 13,5)**. La pente vaut :

$$ a = (13,5 − 19/3) / (4,5 − 2) = (43/6) / (5/2) = 43/15 ≈ 2,867 $$

puis b = 19/3 − (43/15)×2 = 19/3 − 86/15 = 95/15 − 86/15 = 9/15 = **0,6**. La droite de Mayer est donc **y = (43/15)x + 0,6**.

_Contrôle obligatoire_ — elle doit passer par G(3 ; 9,2) : (43/15)×3 + 0,6 = 43/5 + 0,6 = 8,6 + 0,6 = **9,2** ✓. Si ce contrôle échoue, une des deux moyennes partielles est fausse — c'est presque toujours là que l'erreur se cache.

::: figure La droite (G₁G₂) traverse le point moyen G sans qu'on l'y ait forcée : c'est la propriété qui sert de vérification à toute la méthode de Mayer.
<svg viewBox="0 0 340 250"><g stroke="#94a3b8" stroke-width="1" fill="none"><path d="M50 160 H310 M50 105 H310 M50 50 H310"/></g><path d="M50 215 H322" fill="none" stroke="#0f172a" stroke-width="1.8"/><path d="M50 215 V32" fill="none" stroke="#0f172a" stroke-width="1.8"/><g stroke="#0f172a" stroke-width="1.4" fill="none"><path d="M90 215 V220 M130 215 V220 M170 215 V220 M210 215 V220 M250 215 V220"/></g><path d="M70 192.63 L262 41.27" fill="none" stroke="#0f6e56" stroke-width="2.4"/><g fill="#0f172a"><circle cx="90" cy="171" r="4.5"/><circle cx="130" cy="127" r="4.5"/><circle cx="170" cy="138" r="4.5"/><circle cx="210" cy="83" r="4.5"/><circle cx="250" cy="50" r="4.5"/></g><g fill="#0f6e56"><circle cx="130" cy="145.33" r="5"/><circle cx="230" cy="66.5" r="5"/></g><circle cx="170" cy="113.8" r="5.5" fill="#b45309"/><g font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="90" y="233" text-anchor="middle" fill="#0f172a">1</text><text x="130" y="233" text-anchor="middle" fill="#0f172a">2</text><text x="170" y="233" text-anchor="middle" fill="#0f172a">3</text><text x="210" y="233" text-anchor="middle" fill="#0f172a">4</text><text x="250" y="233" text-anchor="middle" fill="#0f172a">5</text><text x="38" y="165" text-anchor="middle" fill="#0f172a">5</text><text x="34" y="110" text-anchor="middle" fill="#0f172a">10</text><text x="34" y="55" text-anchor="middle" fill="#0f172a">15</text><text x="114" y="160" text-anchor="middle" fill="#0f6e56">G₁</text><text x="244" y="62" text-anchor="middle" fill="#0f6e56">G₂</text><text x="182" y="126" text-anchor="middle" fill="#b45309">G</text></g></svg>
:::

> ⚠️ Mayer donne **une** droite, pas **la** meilleure. Change le découpage — 2 points d'un côté et 3 de l'autre au lieu de 3 et 2 — et tu obtiens une autre droite, tout aussi légitime. Elle passera encore par G, mais sa pente aura changé. C'est le prix de la simplicité, et c'est ce qui motive la méthode suivante.

## 🧮 Les moindres carrés : la droite qui minimise l'erreur

Pour classer les droites, il faut d'abord mesurer ce qu'elles coûtent. Pour une droite D d'équation y = ax + b, on note Hᵢ(xᵢ, zᵢ) le point de D qui a la **même abscisse** que le point observé Mᵢ. L'écart MᵢHᵢ = |yᵢ − (axᵢ + b)| est ce que la droite se trompe sur l'individu i. Le manuel énonce alors : « Le principe de la méthode d'ajustement par la méthode des moindres carrés consiste à déterminer les réels a et b tels que la somme Σ_(i=1)^(n) MᵢHᵢ² soit **minimale**. Dans ce cas, le statisticien pourra faire des prévisions en remplaçant la valeur observée yᵢ par la valeur théorique zᵢ = axᵢ + b. »

On élève au carré pour deux raisons : les écarts positifs et négatifs ne doivent pas se compenser, et les gros écarts doivent peser plus lourd que les petits.

> **Théorème (admis)** — « Soit (X, Y) une série statistique double sur un échantillon de taille n et telle que σ_X ≠ 0. Soit (xᵢ, yᵢ), 1 ≤ i ≤ n, les valeurs observées de la série. Alors la somme Σ_(i=1)^(n) (axᵢ + b − yᵢ)² est minimale pour le couple (a₀, b₀) tel que **a₀ = cov(X, Y)/σ_X²** et **b₀ = Ȳ − (cov(X, Y)/σ_X²)·X̄**. »

> **Définition** — « La droite d'équation **y = (cov(X, Y)/σ_X²)(x − X̄) + Ȳ** est appelée droite des moindres carrés de Y en X, ou **droite de régression de Y en X**. La droite d'équation **x = (cov(X, Y)/σ_Y²)(y − Ȳ) + X̄** est appelée droite des moindres carrés de X en Y, ou droite de régression de X en Y. »

> **Conséquence** — « Les droites des moindres carrés de Y en X et de X en Y passent par le point moyen G du nuage associé à la série (X, Y). »

_Exemple détaillé_ — sur les abonnés, cov(X, Y) = 5,2 et σ_X² = V(X) = 2, donc a₀ = 5,2/2 = **2,6**, puis b₀ = 9,2 − 2,6×3 = 9,2 − 7,8 = **1,4** :

$$ D : y = 2,6x + 1,4 $$

_Contrôle n° 1 (le point moyen)_ — 2,6×3 + 1,4 = 7,8 + 1,4 = 9,2 = Ȳ ✓. _Contrôle n° 2 (les résidus se compensent)_ — les valeurs théoriques sont 4,0 ; 6,6 ; 9,2 ; 11,8 ; 14,4 et les écarts observés−théoriques valent 0 ; 1,4 ; −2,2 ; 0,2 ; 0,6, de somme **0** ✓. Cette somme nulle est automatique dès que la droite passe par G : c'est un contrôle qui ne coûte rien.

_La comparaison qui justifie le nom_ — pour cette droite, S_D = 0² + 1,4² + (−2,2)² + 0,2² + 0,6² = 0 + 1,96 + 4,84 + 0,04 + 0,36 = **7,20**. Pour la droite de Mayer y = (43/15)x + 0,6, les valeurs théoriques sont 52/15 ; 95/15 ; 138/15 ; 181/15 ; 224/15, les écarts valent 8/15 ; 25/15 ; −33/15 ; −1/15 ; 1/15, et S_Δ = (64 + 625 + 1089 + 1 + 1)/225 = 1780/225 ≈ **7,911**. On a bien **7,20 < 7,911** : aucune droite ne fait mieux que celle des moindres carrés, et Mayer paie sa simplicité.

::: figure Les segments verticaux sont les MᵢHᵢ : la droite des moindres carrés est celle, parmi toutes les droites du plan, qui rend la somme de leurs **carrés** la plus petite. Le point de 2019 tombe exactement dessus, son écart est nul.
<svg viewBox="0 0 340 250"><g stroke="#94a3b8" stroke-width="1" fill="none"><path d="M50 160 H310 M50 105 H310 M50 50 H310"/></g><path d="M50 215 H322" fill="none" stroke="#0f172a" stroke-width="1.8"/><path d="M50 215 V32" fill="none" stroke="#0f172a" stroke-width="1.8"/><g stroke="#0f172a" stroke-width="1.4" fill="none"><path d="M90 215 V220 M130 215 V220 M170 215 V220 M210 215 V220 M250 215 V220"/></g><path d="M70 185.3 L262 48.02" fill="none" stroke="#0f6e56" stroke-width="2.4"/><g stroke="#b45309" stroke-width="3" fill="none"><path d="M130 127 V142.4"/><path d="M170 138 V113.8"/><path d="M210 83 V85.2"/><path d="M250 50 V56.6"/></g><g fill="#0f172a"><circle cx="90" cy="171" r="4.5"/><circle cx="130" cy="127" r="4.5"/><circle cx="170" cy="138" r="4.5"/><circle cx="210" cy="83" r="4.5"/><circle cx="250" cy="50" r="4.5"/></g><circle cx="170" cy="113.8" r="5.5" fill="#0f6e56"/><g font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="90" y="233" text-anchor="middle" fill="#0f172a">1</text><text x="130" y="233" text-anchor="middle" fill="#0f172a">2</text><text x="170" y="233" text-anchor="middle" fill="#0f172a">3</text><text x="210" y="233" text-anchor="middle" fill="#0f172a">4</text><text x="250" y="233" text-anchor="middle" fill="#0f172a">5</text><text x="38" y="165" text-anchor="middle" fill="#0f172a">5</text><text x="34" y="110" text-anchor="middle" fill="#0f172a">10</text><text x="34" y="55" text-anchor="middle" fill="#0f172a">15</text><text x="186" y="110" text-anchor="middle" fill="#0f6e56">G</text><text x="146" y="140" text-anchor="middle" fill="#b45309">H₂</text></g></svg>
:::

_Prévision_ — l'année 2026 a pour rang 8 : y = 2,6×8 + 1,4 = 20,8 + 1,4 = **22,2 milliers d'abonnés**, soit environ 22 200.

_Exemple détaillé (l'autre droite)_ — la droite de régression de X en Y s'obtient en divisant par σ_Y² au lieu de σ_X² : x = (5,2/14,96)(y − 9,2) + 3 ≈ **0,348(y − 9,2) + 3**. Elle passe par G elle aussi (y = 9,2 donne x = 3 ✓), mais ce **n'est pas** la première droite retournée : résoudre y = 2,6x + 1,4 en x donnerait x ≈ 0,385y − 0,538, de pente 0,385 et non 0,348. Deux droites distinctes, qui se croisent en G.

> 🗡️ En mode statistique à deux variables, la calculatrice fournit directement n, Σx, Σx², Σxy, X̄, σ_X, le coefficient r et les coefficients a et b de la droite de régression de Y en X. Sur un tableau groupé, on saisit chaque couple avec son effectif (par exemple `2 STO 1 STO 4 M+` pour la case (X = 2, Y = 1) d'effectif 4). Utilise-la pour **vérifier**, jamais pour remplacer la ligne de calcul que le correcteur attend.

> ⚠️ **Prévoir loin, c'est inventer.** La droite a été ajustée sur les rangs 1 à 5 ; l'utiliser au rang 8 est déjà une extrapolation, et rien ne garantit que la bibliothèque continuera de croître au même rythme. Un ajustement décrit les données observées — il ne promet rien au-delà.

## 📐 Le coefficient de corrélation : la droite est-elle légitime ?

Les formules précédentes produisent une droite **quelles que soient** les données, même sur un nuage informe. Le manuel prévient : « parfois cette dernière n'est d'aucune efficacité, dans la mesure où les prédictions que l'on fait à partir de cette droite ne sont pas raisonnables. » Il faut donc un juge, et ce juge est un nombre sans unité.

> **Définition** — « Soit (X, Y) une série statistique double. On appelle **coefficient de corrélation linéaire** le réel noté ρ_XY défini par **ρ_XY = cov(X, Y)/(σ_X σ_Y)**. »

> **Propriétés** — « Soit (X, Y) une série statistique double. Alors **−1 ≤ ρ_XY ≤ 1**. Le coefficient de corrélation linéaire est **invariant par changement d'unité ou d'origine**. »

Diviser par les deux écarts-types efface précisément ce qui gênait dans la covariance : compter les abonnés en unités plutôt qu'en milliers multiplie cov et σ_Y par 1000 chacun, et laisse ρ inchangé. Reste le signe, qui est celui de la covariance, et la valeur absolue, qui mesure l'alignement.

> **Seuil d'acceptation** — « Les statisticiens conviennent que lorsque **|ρ_XY| > √3/2**, l'ajustement affine est justifié et les prédictions faites au moyen de cet ajustement sont raisonnables. »

Retiens la valeur numérique du seuil : √3/2 ≈ **0,866**.

::: figure Trois nuages, trois verdicts : à gauche les points s'alignent en montant, au centre ils ne racontent rien, à droite ils s'alignent en descendant. Seuls le premier et le troisième dépassent le seuil de 0,866 en valeur absolue.
<svg viewBox="0 0 380 165"><g stroke="#0f172a" stroke-width="1.6" fill="none"><path d="M15 130 H105 M15 130 V40"/><path d="M145 130 H235 M145 130 V40"/><path d="M275 130 H365 M275 130 V40"/></g><g fill="#0f6e56"><circle cx="27" cy="109" r="4"/><circle cx="39" cy="102" r="4"/><circle cx="51" cy="81" r="4"/><circle cx="63" cy="74" r="4"/><circle cx="75" cy="60" r="4"/><circle cx="87" cy="53" r="4"/></g><g fill="#94a3b8"><circle cx="157" cy="74" r="4"/><circle cx="169" cy="109" r="4"/><circle cx="181" cy="60" r="4"/><circle cx="193" cy="102" r="4"/><circle cx="205" cy="67" r="4"/><circle cx="217" cy="95" r="4"/></g><g fill="#b45309"><circle cx="287" cy="53" r="4"/><circle cx="299" cy="60" r="4"/><circle cx="311" cy="74" r="4"/><circle cx="323" cy="81" r="4"/><circle cx="335" cy="102" r="4"/><circle cx="347" cy="109" r="4"/></g><g font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="60" y="152" text-anchor="middle" fill="#0f6e56">ρ ≈ 0,99</text><text x="190" y="152" text-anchor="middle" fill="#94a3b8">ρ ≈ −0,06</text><text x="320" y="152" text-anchor="middle" fill="#b45309">ρ ≈ −0,99</text></g></svg>
:::

_Exemple détaillé (le cas favorable)_ — sur les abonnés : cov = 5,2, σ_X ≈ 1,414 et σ_Y ≈ 3,868, donc ρ_XY = 5,2/(1,414 × 3,868) = 5,2/5,470 ≈ **0,951**. Comme 0,951 > 0,866, l'ajustement affine est justifié — la prévision de 22,2 milliers a un sens.

_Contrôle_ — on peut éviter les racines carrées en passant par le carré : ρ² = cov²/(V(X)·V(Y)) = 5,2²/(2 × 14,96) = 27,04/29,92 ≈ 0,9037, et √0,9037 ≈ **0,951** ✓. Au passage, ρ² est aussi le produit des pentes des deux droites de régression : 2,6 × (5,2/14,96) = 13,52/14,96 ≈ 0,9037 ✓.

_Exemple détaillé (le cas défavorable)_ — sur les 20 logements : cov = 0,34, σ_X ≈ 0,748 et σ_Y ≈ 0,805, donc ρ_XY = 0,34/(0,748 × 0,805) = 0,34/0,602 ≈ **0,565**. Le lien existe (ρ > 0), mais 0,565 < 0,866 : **un ajustement affine n'est pas justifié**. On peut calculer la droite de régression — rien ne l'interdit — mais s'en servir pour prédire le nombre d'enfants d'un logement de 4 pièces serait abusif.

> ⚠️ Corrélation n'est pas causalité, et ρ ne mesure **que** l'alignement. Un nuage parfaitement posé sur une parabole peut avoir un ρ proche de 0 alors que le lien entre X et Y est total. Le nombre ne remplace pas le regard sur le nuage : il le confirme.

## 🧪 Quand le nuage n'est pas droit : changer de variable

Un nuage nettement incurvé n'appelle pas de droite — mais il en cache souvent une. Si Y semble croître de façon **exponentielle**, on pose Z = ln Y : la relation Y = k·e^(ax) devient ln Y = ax + ln k, c'est-à-dire **Z = ax + b**, qui est affine. On ajuste alors (X, Z) par les moindres carrés, puis on revient à Y par la fonction exponentielle.

_Exemple détaillé_ — on compte une culture de bactéries (en milliers) heure par heure.

| Rang xᵢ (heures)        | 0     | 1     | 2     | 3     | 4     |
| ----------------------- | ----- | ----- | ----- | ----- | ----- |
| Bactéries yᵢ (milliers) | 5     | 8     | 13    | 20    | 33    |
| zᵢ = ln yᵢ (à 10⁻³)     | 1,609 | 2,079 | 2,565 | 2,996 | 3,497 |

Sur X : X̄ = 10/5 = **2**, Σxᵢ² = 0 + 1 + 4 + 9 + 16 = 30, V(X) = 30/5 − 4 = **2**, σ_X ≈ 1,414. Sur Z : Σzᵢ = 12,746 donc **Z̄ = 2,5492** ; Σzᵢ² ≈ 34,695 donc V(Z) ≈ 34,695/5 − 2,5492² ≈ 6,939 − 6,498 = **0,4407** et σ_Z ≈ 0,664. Enfin Σxᵢzᵢ = 0 + 2,079 + 2×2,565 + 3×2,996 + 4×3,497 = 2,079 + 5,130 + 8,988 + 13,988 = 30,185, d'où :

$$ cov(X, Z) = 30,185/5 − 2 × 2,5492 = 6,037 − 5,0984 ≈ 0,9386 $$

_Contrôle par les écarts_ — les écarts de Z à Z̄ valent −0,940 ; −0,470 ; 0,016 ; 0,447 ; 0,948, et ceux de X valent −2 ; −1 ; 0 ; 1 ; 2 : la somme des produits fait 1,880 + 0,470 + 0 + 0,447 + 1,896 = 4,693, et 4,693/5 ≈ **0,9386** ✓.

Le coefficient de corrélation de la série (X, Z) vaut ρ_XZ = 0,9386/(1,414 × 0,664) ≈ 0,9386/0,939 ≈ **0,9998**, très supérieur au seuil 0,866 : l'ajustement affine de Z en X est pleinement justifié. Sa droite a pour pente a = 0,9386/2 = 0,4693 et pour ordonnée à l'origine b = 2,5492 − 0,4693×2 = 1,6106, soit, à 10⁻³ près :

$$ z = 0,469x + 1,611 $$

_Contrôle_ — au point moyen : 0,469×2 + 1,611 = 0,938 + 1,611 = 2,549 = Z̄ ✓.

On revient enfin à Y en composant par l'exponentielle : y = e^z = e^(0,469x + 1,611) = e^(1,611)·e^(0,469x), soit **y ≈ 5,01·e^(0,469x)**. Le facteur e^(0,469) ≈ 1,60 se lit comme une croissance d'environ 60 % par heure.

_Contrôle sur les données_ — au rang 4 : 5,01 × e^(1,876) ≈ 5,01 × 6,527 ≈ **32,7**, contre 33 observés ✓ ; au rang 2 : 5,01 × e^(0,938) ≈ 5,01 × 2,555 ≈ **12,8**, contre 13 observés ✓. Le modèle colle.

_Prévision_ — à la 6ᵉ heure : y ≈ 5,01 × e^(0,469×6) = 5,01 × e^(2,814) ≈ 5,01 × 16,68 ≈ **83,5 milliers**, soit près de 84 000 bactéries.

> 🗡️ Le changement de variable se choisit sur l'**allure** du nuage, et l'énoncé le souffle presque toujours : Z = ln Y pour une croissance exponentielle, Z = √Y quand Y semble proportionnel au carré de X, X = V² et Y = R/V pour une résistance qui grimpe en puissance de la vitesse. Une fois posé, tout le chapitre s'applique à la **nouvelle** série — puis on remonte à la variable de départ.

> ⚠️ Ne calcule jamais ρ sur (X, Y) pour valider un ajustement fait sur (X, Z). Le coefficient qui justifie la droite est **celui de la série ajustée**, ρ_XZ. Et l'ordre des opérations ne s'inverse pas : la moyenne des ln n'est pas le ln de la moyenne.

## 👑 Méthode : traiter une série double de bout en bout

| Étape | Question                       | Outil                                                                         |
| ----- | ------------------------------ | ----------------------------------------------------------------------------- |
| 1     | Quelles sont les deux séries ? | marges du tableau ; contrôler que les fréquences somment à 1                  |
| 2     | Comment les résumer ?          | X̄, V(X) = (1/n)Σnᵢxᵢ² − X̄², σ_X — idem pour Y                                 |
| 3     | Varient-elles ensemble ?       | cov(X, Y) = (1/n)Σxᵢyᵢ − X̄Ȳ (ou ΣΣnᵢⱼxᵢyⱼ si groupé) ; lire le **signe**      |
| 4     | Une droite est-elle légitime ? | allure du nuage, puis ρ_XY = cov/(σ_X σ_Y) comparé à √3/2 ≈ 0,866             |
| 5     | Quelle droite ?                | moindres carrés a₀ = cov/σ_X², b₀ = Ȳ − a₀X̄ (ou Mayer si l'énoncé l'impose)   |
| 6     | Vérification                   | la droite passe par G(X̄, Ȳ) et la somme des écarts observés−théoriques vaut 0 |
| 7     | Le nuage est courbe ?          | changement de variable (Z = ln Y, Z = √Y…), ajuster (X, Z), puis revenir à Y  |

> 🏆 Dix-neuvième et dernière porte, héros. Tu sais lire un tableau à double entrée, en extraire deux séries et leurs paramètres, mesurer leur lien par la covariance puis par la corrélation, tracer la droite qui minimise vraiment l'erreur, la contrôler en la faisant passer par le point moyen, et redresser un nuage courbe par un changement de variable. Le manuel s'arrête ici : de la continuité du chapitre 1 jusqu'à ce nuage de points, tu tiens désormais le programme entier. Il ne reste qu'à t'en servir.
