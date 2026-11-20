# ⚔️ Géométrie analytique — quand droites et cercles deviennent des équations

> 💡 «Un point, deux nombres ; une droite, une équation ; un cercle, une autre équation : avec un repère, la géométrie se règle par le calcul.»

Descartes (1596-1650) a eu l'idée de donner à chaque point du plan deux coordonnées. Depuis, un alignement, un parallélisme ou une distance se calculent au lieu de se deviner sur un dessin. Huit étapes te mènent du milieu d'un segment jusqu'à l'équation d'un cercle. On suppose acquis les composantes d'un vecteur et le déterminant (chapitre 5), le barycentre (chapitre 6) et les fonctions affines. Le plan est muni d'un repère (O, i⃗, j⃗) ; dès qu'il est question de perpendiculaires, de distances ou de cercles, ce repère est **orthonormé**, et l'énoncé le précise.

## 📍 Milieu et barycentre en coordonnées

Deux amis habitent aux points A(−2 ; 1) et B(6 ; 5) d'un plan de quartier, l'unité étant le kilomètre. Ils se retrouvent d'abord à mi-chemin, puis un autre jour en un point trois fois plus proche de A que de B.
Quelles sont les coordonnées de ces deux points de rendez-vous ?

::: definition
Soit A(xA ; yA) et B(xB ; yB) deux points. Le **milieu** I de [AB] a pour coordonnées ((xA + xB)/2 ; (yA + yB)/2).

Si α + β ≠ 0, le **barycentre** G des points pondérés (A, α) et (B, β) a pour coordonnées ((αxA + βxB)/(α + β) ; (αyA + βyB)/(α + β)).
:::

::: figure Les points A et B, leur milieu I et le barycentre G des points (A, 3) et (B, 1) : I est à égale distance de A et de B, tandis que G, plus près de A, est au quart du trajet
<svg viewBox="0 0 320 236"><path d="M20 216 V20 M48 216 V20 M76 216 V20 M104 216 V20 M132 216 V20 M160 216 V20 M188 216 V20 M216 216 V20 M244 216 V20 M272 216 V20 M300 216 V20 M20 216 H300 M20 188 H300 M20 160 H300 M20 132 H300 M20 104 H300 M20 76 H300 M20 48 H300 M20 20 H300" fill="none" stroke="#94a3b8" stroke-width="0.8" opacity="0.55"/><path d="M20 188 H308 M104 216 V12" fill="none" stroke="#0f172a" stroke-width="1.8"/><path d="M305 184 L313 188 L305 192 Z M100 15 L104 7 L108 15 Z" fill="#0f172a"/><path d="M48 160 L272 48" fill="none" stroke="#0f172a" stroke-width="2.4" stroke-linecap="round"/><circle cx="48" cy="160" r="4.5" fill="#0f172a"/><circle cx="272" cy="48" r="4.5" fill="#0f172a"/><circle cx="160" cy="104" r="4.5" fill="#0f6e56"/><circle cx="104" cy="132" r="4.5" fill="#b45309"/><g font-size="10.5" text-anchor="middle" paint-order="stroke" stroke="#ffffff" stroke-width="3.2" stroke-linejoin="round"><text x="20" y="201" fill="#0f172a">−3</text><text x="48" y="201" fill="#0f172a">−2</text><text x="76" y="201" fill="#0f172a">−1</text><text x="132" y="201" fill="#0f172a">1</text><text x="160" y="201" fill="#0f172a">2</text><text x="188" y="201" fill="#0f172a">3</text><text x="216" y="201" fill="#0f172a">4</text><text x="244" y="201" fill="#0f172a">5</text><text x="272" y="201" fill="#0f172a">6</text><text x="300" y="201" fill="#0f172a">7</text><text x="99" y="220" fill="#0f172a" text-anchor="end">−1</text><text x="99" y="164" fill="#0f172a" text-anchor="end">1</text><text x="99" y="136" fill="#0f172a" text-anchor="end">2</text><text x="99" y="108" fill="#0f172a" text-anchor="end">3</text><text x="99" y="80" fill="#0f172a" text-anchor="end">4</text><text x="99" y="52" fill="#0f172a" text-anchor="end">5</text><text x="99" y="24" fill="#0f172a" text-anchor="end">6</text><text x="99" y="201" fill="#0f172a" text-anchor="end">O</text></g><g paint-order="stroke" stroke="#ffffff" stroke-width="3.6" stroke-linejoin="round"><text x="48" y="176" fill="#0f172a" text-anchor="middle" font-size="12" font-weight="700">A(−2 ; 1)</text><text x="272" y="38" fill="#0f172a" text-anchor="middle" font-size="12" font-weight="700">B(6 ; 5)</text><text x="156" y="93" fill="#0f6e56" text-anchor="middle" font-size="12" font-weight="700">I(2 ; 3)</text><text x="110" y="149" fill="#b45309" text-anchor="middle" font-size="12" font-weight="700">G(0 ; 2)</text></g></svg>
:::

L'abscisse de I est la moyenne des abscisses de A et de B, et de même pour l'ordonnée. Pour G, chaque coordonnée est une moyenne **pondérée** : un coefficient plus grand attire G vers son point.

::: exemple Les deux points de rendez-vous
1. Milieu : xI = (−2 + 6)/2 = 2 et yI = (1 + 5)/2 = 3, donc I(2 ; 3), car chaque coordonnée est la moyenne de celles des extrémités.
2. Barycentre de (A, 3) et (B, 1) : la somme des coefficients vaut 3 + 1 = 4, non nulle, donc G existe ; c'est par elle qu'on divise.
3. xG = (3 × (−2) + 1 × 6)/4 = 0/4 = 0 et yG = (3 × 1 + 1 × 5)/4 = 8/4 = 2, donc G(0 ; 2).
4. Contrôle : AB⃗ a pour composantes (8 ; 4) et AG⃗ a pour composantes (2 ; 1) = (1/4)AB⃗ : G est bien au quart du trajet à partir de A, donc trois fois plus près de A que de B.

Autre exemple, sans contexte : le centre de gravité du triangle A(1 ; 5), B(−2 ; 1), C(7 ; −3) est le barycentre de (A, 1), (B, 1), (C, 1). On obtient xG = (1 − 2 + 7)/3 = 2 et yG = (5 + 1 − 3)/3 = 1, donc G(2 ; 1).

:::

::: piege Diviser par 2 au lieu de la somme des coefficients
Pour le barycentre de (A, 3) et (B, 1), on écrit xG = (3 × (−2) + 1 × 6)/2 = 0 et yG = (3 × 1 + 1 × 5)/2 = 4, donc G(0 ; 4). Cela tente parce qu'il y a deux points, comme pour le milieu. Mais on divise par α + β = 4. Test : avec G(0 ; 4), AG⃗(2 ; 3) n'est pas colinéaire à AB⃗(8 ; 4), car 2 × 4 − 3 × 8 = −16 ≠ 0 : ce point n'est même pas sur la droite (AB).
:::

::: propriete
Si α + β ≠ 0, le barycentre de (A, α) et (B, β) est le point ((αxA + βxB)/(α + β) ; (αyA + βyB)/(α + β)). Si α + β + γ ≠ 0, celui de (A, α), (B, β) et (C, γ) est le point ((αxA + βxB + γxC)/(α + β + γ) ; (αyA + βyB + γyC)/(α + β + γ)).

- Si α = β ≠ 0, on retrouve le milieu ; si α = β = γ ≠ 0, on retrouve le centre de gravité.
- Cas limite : si α + β = 0, il n'y a pas de barycentre, car il faudrait diviser par 0.
:::

::: verifie Un barycentre à compléter
Donner le barycentre G de (A, 2) et (B, 3), avec A(−4 ; 0) et B(1 ; 5).
---
La somme des coefficients vaut 2 + 3 = 5, non nulle : on divise par 5. xG = (2 × (−4) + 3 × 1)/5 = −5/5 = −1 et yG = (2 × 0 + 3 × 5)/5 = 15/5 = 3, donc G(−1 ; 3). Le point est plus près de B, qui porte le plus grand coefficient.
:::

::: retenir
Le milieu a pour coordonnées les moyennes de celles des extrémités ; un barycentre, des moyennes pondérées divisées par la somme des coefficients, qui doit être non nulle.
:::

## ➖ Équation cartésienne d'une droite

Une piste cyclable rectiligne passe par les points A(0 ; 3) et B(4 ; 1) d'un plan, l'unité étant le kilomètre. Le point C(2 ; 2) est-il sur la piste ? Et le point E(6 ; 1) ?
Plutôt que de tracer à chaque fois, on cherche une relation entre x et y que vérifient les points de la piste, et eux seuls.

::: definition
Une **équation cartésienne** d'une droite D est une équation de la forme ax + by + c = 0, avec (a ; b) ≠ (0 ; 0), que vérifient les coordonnées d'un point M(x ; y) si et seulement si M appartient à D. On écrit D : ax + by + c = 0.
:::

::: figure La piste D passe par A, B et C ; le point E reste à l'écart. Une équation de D doit être vérifiée par les coordonnées de A, de B et de C, mais pas par celles de E
<svg viewBox="0 0 292 180"><path d="M20 160 V20 M48 160 V20 M76 160 V20 M104 160 V20 M132 160 V20 M160 160 V20 M188 160 V20 M216 160 V20 M244 160 V20 M272 160 V20 M20 160 H272 M20 132 H272 M20 104 H272 M20 76 H272 M20 48 H272 M20 20 H272" fill="none" stroke="#94a3b8" stroke-width="0.8" opacity="0.55"/><path d="M20 132 H280 M48 160 V12" fill="none" stroke="#0f172a" stroke-width="1.8"/><path d="M277 128 L285 132 L277 136 Z M44 15 L48 7 L52 15 Z" fill="#0f172a"/><path d="M20 34 L272 160" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linecap="round"/><circle cx="48" cy="48" r="4.5" fill="#0f6e56"/><circle cx="160" cy="104" r="4.5" fill="#0f6e56"/><circle cx="104" cy="76" r="4.5" fill="#0f6e56"/><circle cx="216" cy="104" r="4.5" fill="#b45309"/><g font-size="10.5" text-anchor="middle" paint-order="stroke" stroke="#ffffff" stroke-width="3.2" stroke-linejoin="round"><text x="20" y="145" fill="#0f172a">−1</text><text x="76" y="145" fill="#0f172a">1</text><text x="104" y="145" fill="#0f172a">2</text><text x="132" y="145" fill="#0f172a">3</text><text x="160" y="145" fill="#0f172a">4</text><text x="188" y="145" fill="#0f172a">5</text><text x="216" y="145" fill="#0f172a">6</text><text x="244" y="145" fill="#0f172a">7</text><text x="272" y="145" fill="#0f172a">8</text><text x="43" y="164" fill="#0f172a" text-anchor="end">−1</text><text x="43" y="108" fill="#0f172a" text-anchor="end">1</text><text x="43" y="80" fill="#0f172a" text-anchor="end">2</text><text x="43" y="52" fill="#0f172a" text-anchor="end">3</text><text x="43" y="24" fill="#0f172a" text-anchor="end">4</text><text x="43" y="145" fill="#0f172a" text-anchor="end">O</text></g><g paint-order="stroke" stroke="#ffffff" stroke-width="3.6" stroke-linejoin="round"><text x="60" y="40" fill="#0f6e56" text-anchor="middle" font-size="13" font-weight="700">A</text><text x="170" y="96" fill="#0f6e56" text-anchor="middle" font-size="13" font-weight="700">B</text><text x="114" y="68" fill="#0f6e56" text-anchor="middle" font-size="13" font-weight="700">C</text><text x="226" y="96" fill="#b45309" text-anchor="middle" font-size="13" font-weight="700">E</text><text x="25.6" y="28.8" fill="#0f6e56" text-anchor="middle" font-size="14" font-weight="700">D</text></g></svg>
:::

Le point C est sur la droite, le point E n'y est pas : c'est exactement ce que l'équation va décider, point par point, sans regarder le dessin.

::: exemple Trouver l'équation de la piste
1. M(x ; y) est sur (AB) si et seulement si AM⃗ et AB⃗ sont colinéaires, car A et B sont deux points de la droite. Ici AB⃗(4 ; −2) et AM⃗(x ; y − 3).
2. Deux vecteurs sont colinéaires si et seulement si leur déterminant est nul (chapitre 5) : x × (−2) − 4 × (y − 3) = 0, soit −2x − 4y + 12 = 0.
3. On divise par −2 pour simplifier, ce qui ne change pas la droite : x + 2y − 6 = 0, avec a = 1, b = 2 et c = −6.
4. Contrôle : A donne 0 + 6 − 6 = 0 et B donne 4 + 2 − 6 = 0. Puis C(2 ; 2) donne 2 + 4 − 6 = 0, donc C ∈ D, et E(6 ; 1) donne 6 + 2 − 6 = 2 ≠ 0, donc E ∉ D.

Autre exemple, sans contexte : la droite (RS) avec R(−1 ; 2) et S(3 ; −4). On a RS⃗(4 ; −6) et RM⃗(x + 1 ; y − 2), donc (x + 1) × (−6) − 4 × (y − 2) = −6x − 4y + 2 = 0. En divisant par −2 : 3x + 2y − 1 = 0. Contrôle : R donne −3 + 4 − 1 = 0 et S donne 9 − 8 − 1 = 0.

:::

::: piege Oublier le terme constant en testant un point
Pour savoir si C(2 ; 2) est sur D : x + 2y − 6 = 0, on calcule 2 + 2 × 2 = 6 et on conclut « 6 ≠ 0, donc non ». Cela tente parce qu'on ne regarde que les termes en x et en y. Mais le −6 fait partie de l'équation : 2 + 4 − 6 = 0, donc C est sur D. À l'inverse, le point (2 ; −1) donne 2 − 2 = 0 sans le −6, et on le croirait sur D ; en réalité 2 − 2 − 6 = −6 ≠ 0.
:::

::: propriete
Toute droite admet une équation cartésienne ax + by + c = 0 avec (a ; b) ≠ (0 ; 0). Réciproquement, toute équation de cette forme est celle d'une droite. En multipliant a, b et c par un même réel non nul, on obtient une autre équation de la même droite.

- Pour tracer D, on cherche deux points : x = 0 donne y = −c/b (si b ≠ 0) et y = 0 donne x = −c/a (si a ≠ 0).
- Cas limites : si b = 0, la droite est verticale, d'équation x = −c/a ; si a = 0, elle est horizontale ; si a = b = 0, ce n'est plus une droite.
:::

::: verifie Tracer une droite
Tracer D : 2x − y + 4 = 0 en cherchant deux points, puis dire si F(3 ; 10) est sur D.
---
Pour x = 0, −y + 4 = 0 donne y = 4 : le point (0 ; 4). Pour y = 0, 2x + 4 = 0 donne x = −2 : le point (−2 ; 0). On trace la droite qui passe par ces deux points. Pour F : 2 × 3 − 10 + 4 = 0, donc F ∈ D.
:::

::: retenir
Une droite a pour équation ax + by + c = 0 avec (a ; b) ≠ (0 ; 0) : un point est sur la droite si et seulement si ses coordonnées vérifient l'équation, terme constant compris.
:::

## ↗️ Vecteur directeur et droites parallèles

La piste D est d'équation x + 2y − 6 = 0. Une deuxième piste a pour équation 2x + 4y − 3 = 0, une troisième 2x − y − 2 = 0.
Sans les tracer, lesquelles ne se rencontreront jamais, et en quel point se croisent les autres ?

::: definition
Soit D une droite. Un **vecteur directeur** de D est un vecteur non nul AB⃗, où A et B sont deux points distincts de D. Tout vecteur non nul colinéaire à un vecteur directeur de D en est un aussi.
:::

::: figure Les pistes D1 (vert) et D2 (ocre) ont la même direction, la piste D3 (noire) les coupe ; le vecteur violet u, porté par D1 de B(4 ; 1) vers C(2 ; 2), est un vecteur directeur de D1
<svg viewBox="0 0 292 208"><path d="M20 188 V20 M48 188 V20 M76 188 V20 M104 188 V20 M132 188 V20 M160 188 V20 M188 188 V20 M216 188 V20 M244 188 V20 M272 188 V20 M20 188 H272 M20 160 H272 M20 132 H272 M20 104 H272 M20 76 H272 M20 48 H272 M20 20 H272" fill="none" stroke="#94a3b8" stroke-width="0.8" opacity="0.55"/><path d="M20 160 H280 M48 188 V12" fill="none" stroke="#0f172a" stroke-width="1.8"/><path d="M277 156 L285 160 L277 164 Z M44 15 L48 7 L52 15 Z" fill="#0f172a"/><path d="M20 62 L272 188" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linecap="round"/><path d="M20 125 L146 188" fill="none" stroke="#b45309" stroke-width="2.6" stroke-linecap="round"/><path d="M62 188 L146 20" fill="none" stroke="#0f172a" stroke-width="2.6" stroke-linecap="round"/><path d="M160 132 L104 104" fill="none" stroke="#6d28d9" stroke-width="3" stroke-linecap="round"/><polygon points="104,104 113.9,104.4 110.2,111.6" fill="#6d28d9"/><circle cx="104" cy="104" r="4.5" fill="#0f172a"/><circle cx="160" cy="132" r="4.5" fill="#0f172a"/><g font-size="10.5" text-anchor="middle" paint-order="stroke" stroke="#ffffff" stroke-width="3.2" stroke-linejoin="round"><text x="20" y="173" fill="#0f172a">−1</text><text x="76" y="173" fill="#0f172a">1</text><text x="104" y="173" fill="#0f172a">2</text><text x="132" y="173" fill="#0f172a">3</text><text x="160" y="173" fill="#0f172a">4</text><text x="188" y="173" fill="#0f172a">5</text><text x="216" y="173" fill="#0f172a">6</text><text x="244" y="173" fill="#0f172a">7</text><text x="272" y="173" fill="#0f172a">8</text><text x="43" y="192" fill="#0f172a" text-anchor="end">−1</text><text x="43" y="136" fill="#0f172a" text-anchor="end">1</text><text x="43" y="108" fill="#0f172a" text-anchor="end">2</text><text x="43" y="80" fill="#0f172a" text-anchor="end">3</text><text x="43" y="52" fill="#0f172a" text-anchor="end">4</text><text x="43" y="24" fill="#0f172a" text-anchor="end">5</text><text x="43" y="173" fill="#0f172a" text-anchor="end">O</text></g><g paint-order="stroke" stroke="#ffffff" stroke-width="3.6" stroke-linejoin="round"><text x="92" y="96" fill="#0f172a" text-anchor="middle" font-size="13" font-weight="700">C</text><text x="170" y="150" fill="#0f172a" text-anchor="middle" font-size="13" font-weight="700">B</text><text x="142.8" y="132" fill="#6d28d9" text-anchor="middle" font-size="14" font-weight="700">u</text><text x="208" y="143" fill="#0f6e56" text-anchor="middle" font-size="13" font-weight="700">D1</text><text x="36" y="123" fill="#b45309" text-anchor="middle" font-size="13" font-weight="700">D2</text><text x="158" y="18.8" fill="#0f172a" text-anchor="middle" font-size="13" font-weight="700">D3</text></g></svg>
:::

Une droite n'a qu'une direction, mais une infinité de vecteurs directeurs, tous colinéaires entre eux. Deux droites de même direction ont donc des vecteurs directeurs colinéaires : c'est ce qu'on va tester.

::: exemple Parallèles ou sécantes ?
1. D1 : x + 2y − 6 = 0 passe par A(0 ; 3) et B(4 ; 1), donc AB⃗(4 ; −2) la dirige, ainsi que u⃗(−2 ; 1) = −(1/2)AB⃗, qui lui est colinéaire. On remarque que u⃗ est le couple (−b ; a).
2. Pour D2 : 2x + 4y − 3 = 0, le couple (−b ; a) est (−4 ; 2) = 2u⃗ : D2 a la même direction que D1. Le déterminant le confirme : ab′ − a′b = 1 × 4 − 2 × 2 = 0.
3. D1 et D2 sont distinctes, car A(0 ; 3) est sur D1 mais pas sur D2 : 2 × 0 + 4 × 3 − 3 = 9 ≠ 0. Elles sont donc strictement parallèles et n'ont aucun point commun.
4. Pour D3 : 2x − y − 2 = 0, ab′ − a′b = 1 × (−1) − 2 × 2 = −5 ≠ 0 : D1 et D3 sont sécantes. On résout x + 2y = 6 et 2x − y = 2 : la seconde donne y = 2x − 2, donc x + 4x − 4 = 6, soit x = 2 et y = 2. Elles se croisent en C(2 ; 2) : 2 + 4 − 6 = 0 et 4 − 2 − 2 = 0.

Autre exemple, sans contexte : la droite passant par A(2 ; −1) de vecteur directeur u⃗(3 ; 1). Si M(x ; y) est sur cette droite, AM⃗(x − 2 ; y + 1) est colinéaire à u⃗, donc (x − 2) × 1 − 3 × (y + 1) = 0, soit x − 3y − 5 = 0. Contrôle : A donne 2 + 3 − 5 = 0 et A + u⃗ = (5 ; 0) donne 5 − 0 − 5 = 0.

:::

::: piege Prendre (a ; b) pour vecteur directeur
Pour D1 : x + 2y − 6 = 0, on lit le vecteur (1 ; 2) comme vecteur directeur. Cela tente parce que a et b sont écrits en premier. Mais le vecteur directeur est (−b ; a) = (−2 ; 1). Test : AB⃗(4 ; −2) est porté par D1, et son déterminant avec (1 ; 2) vaut 4 × 2 − 1 × (−2) = 10 ≠ 0 : (1 ; 2) n'est pas colinéaire à AB⃗.
:::

::: propriete
Soit D : ax + by + c = 0. Le vecteur u⃗(−b ; a) est un vecteur directeur de D. Soit D′ : a′x + b′y + c′ = 0. Alors D ∥ D′ si et seulement si ab′ − a′b = 0 ; sinon, D et D′ sont sécantes en un seul point, dont on obtient les coordonnées en résolvant le système.

- Pourquoi (−b ; a) : si A(xA ; yA) et M(x ; y) sont sur D, on soustrait axA + byA + c = 0 à ax + by + c = 0 et il reste a(x − xA) + b(y − yA) = 0, c'est-à-dire que AM⃗ et (−b ; a) ont un déterminant nul.
- La parallèle à D passant par A est la droite ax + by + c′ = 0, avec c′ = −(axA + byA). La droite de vecteur directeur (p ; q) passant par A a pour équation q(x − xA) − p(y − yA) = 0.
- Cas limite : si ab′ − a′b = 0, les droites sont parallèles, strictement ou confondues : on teste un point de D dans D′ pour trancher.
:::

::: verifie Condition de parallélisme
Déterminer k pour que D : 4x − 6y + 1 = 0 et D′ : 6x + ky − 2 = 0 soient parallèles.
---
Ici a = 4, b = −6, a′ = 6 et b′ = k. Le parallélisme équivaut à ab′ − a′b = 0, c'est-à-dire 4k − 6 × (−6) = 4k + 36 = 0, donc k = −9. Contrôle : D′ : 6x − 9y − 2 = 0 a pour vecteur directeur (9 ; 6) et D a pour vecteur directeur (6 ; 4), colinéaires puisque 9 × 4 − 6 × 6 = 0.
:::

::: retenir
Un vecteur directeur de ax + by + c = 0 est (−b ; a) ; deux droites sont parallèles si et seulement si ab′ − a′b = 0, et sécantes sinon, en un point donné par un système.
:::

## ⟂ Vecteur normal et droites perpendiculaires

Dans un repère orthonormé (unité : le kilomètre), la piste D : x + 2y − 6 = 0 passe près d'un puits situé en P(1 ; 4). On veut creuser, à partir du puits, un canal rectiligne qui coupe la piste à angle droit.
Quelle est l'équation de ce canal ?

::: definition
Un **vecteur normal** à une droite D est un vecteur non nul orthogonal à un vecteur directeur de D.
:::

::: figure La piste D, un vecteur normal n (violet) et la droite D′ qui passe par le puits P et coupe D en H à angle droit : D′ est dirigée par n, c'est ce qui la rend perpendiculaire à D
<svg viewBox="0 0 264 236"><path d="M20 216 V20 M48 216 V20 M76 216 V20 M104 216 V20 M132 216 V20 M160 216 V20 M188 216 V20 M216 216 V20 M244 216 V20 M20 216 H244 M20 188 H244 M20 160 H244 M20 132 H244 M20 104 H244 M20 76 H244 M20 48 H244 M20 20 H244" fill="none" stroke="#94a3b8" stroke-width="0.8" opacity="0.55"/><path d="M20 188 H252 M76 216 V12" fill="none" stroke="#0f172a" stroke-width="1.8"/><path d="M249 184 L257 188 L249 192 Z M72 15 L76 7 L80 15 Z" fill="#0f172a"/><path d="M20 76 L244 188" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linecap="round"/><path d="M34 216 L132 20" fill="none" stroke="#b45309" stroke-width="2.6" stroke-linecap="round"/><path d="M132 132 L160 76" fill="none" stroke="#6d28d9" stroke-width="3" stroke-linecap="round"/><polygon points="160,76 159.6,85.9 152.4,82.2" fill="#6d28d9"/><path d="M97.2 114.6 L102.2 104.6 L92.2 99.6" fill="none" stroke="#0f172a" stroke-width="1.6"/><circle cx="104" cy="76" r="4.5" fill="#b45309"/><circle cx="87.2" cy="109.6" r="4" fill="#0f172a"/><g font-size="10.5" text-anchor="middle" paint-order="stroke" stroke="#ffffff" stroke-width="3.2" stroke-linejoin="round"><text x="20" y="201" fill="#0f172a">−2</text><text x="48" y="201" fill="#0f172a">−1</text><text x="104" y="201" fill="#0f172a">1</text><text x="132" y="201" fill="#0f172a">2</text><text x="160" y="201" fill="#0f172a">3</text><text x="188" y="201" fill="#0f172a">4</text><text x="216" y="201" fill="#0f172a">5</text><text x="244" y="201" fill="#0f172a">6</text><text x="71" y="220" fill="#0f172a" text-anchor="end">−1</text><text x="71" y="164" fill="#0f172a" text-anchor="end">1</text><text x="71" y="136" fill="#0f172a" text-anchor="end">2</text><text x="71" y="108" fill="#0f172a" text-anchor="end">3</text><text x="71" y="80" fill="#0f172a" text-anchor="end">4</text><text x="71" y="52" fill="#0f172a" text-anchor="end">5</text><text x="71" y="24" fill="#0f172a" text-anchor="end">6</text><text x="71" y="201" fill="#0f172a" text-anchor="end">O</text></g><g paint-order="stroke" stroke="#ffffff" stroke-width="3.6" stroke-linejoin="round"><text x="94" y="70" fill="#b45309" text-anchor="middle" font-size="13" font-weight="700">P</text><text x="99.2" y="123.6" fill="#0f172a" text-anchor="middle" font-size="13" font-weight="700">H</text><text x="156" y="110" fill="#6d28d9" text-anchor="middle" font-size="14" font-weight="700">n</text><text x="227.2" y="168.8" fill="#0f6e56" text-anchor="middle" font-size="14" font-weight="700">D</text><text x="97.6" y="211.2" fill="#b45309" text-anchor="middle" font-size="14" font-weight="700">D′</text></g></svg>
:::

Le vecteur n est tracé perpendiculairement à D ; comme D′ est parallèle à n, n est un vecteur directeur de D′.

::: exemple Le canal qui coupe la piste à angle droit
1. Un vecteur directeur de D est u⃗(−2 ; 1). Un vecteur normal est un vecteur non nul orthogonal à u⃗ : n⃗(1 ; 2) convient, car (−2) × 1 + 1 × 2 = 0 (orthogonalité xx′ + yy′ = 0 du chapitre 5, valable en repère orthonormé).
2. Le canal D′ est dirigé par n⃗(1 ; 2), puisqu'il est perpendiculaire à D. Si M(x ; y) est sur D′, PM⃗(x − 1 ; y − 4) est colinéaire à n⃗ : (x − 1) × 2 − 1 × (y − 4) = 0, soit 2x − y + 2 = 0.
3. Contrôle : P donne 2 − 4 + 2 = 0. Et aa′ + bb′ = 1 × 2 + 2 × (−1) = 0 pour D et D′ : les deux droites sont bien perpendiculaires.

Autre exemple, sans contexte : la droite passant par A(3 ; −1) de vecteur normal n⃗(2 ; 1). Si M(x ; y) est sur cette droite, AM⃗(x − 3 ; y + 1) est orthogonal à n⃗, donc 2(x − 3) + 1 × (y + 1) = 0, soit 2x + y − 5 = 0. Contrôle : A donne 6 − 1 − 5 = 0.

:::

::: piege Tester la perpendicularité avec la condition de parallélisme
Pour D : x + 2y − 6 = 0 et D′ : 2x − y + 2 = 0, on calcule ab′ − a′b = 1 × (−1) − 2 × 2 = −5 et on conclut « non nul, donc pas perpendiculaires ». Cela tente parce que c'est la seule condition déjà vue. Mais ab′ − a′b = 0 teste le parallélisme. La perpendicularité se teste par aa′ + bb′ = 1 × 2 + 2 × (−1) = 0, et ici elle est vraie.
:::

::: propriete
Le plan est muni d'un repère orthonormé. Soit D : ax + by + c = 0. Le vecteur n⃗(a ; b) est un vecteur normal à D, car a × (−b) + b × a = 0 avec le vecteur directeur (−b ; a). Soit D′ : a′x + b′y + c′ = 0. Alors D ⊥ D′ si et seulement si aa′ + bb′ = 0.

- La droite passant par A de vecteur normal (p ; q) a pour équation p(x − xA) + q(y − yA) = 0. La perpendiculaire à D passant par A est la droite bx − ay + c′ = 0, avec c′ = −(bxA − ayA).
- Cas limite : les droites x = 3 et y = 5 sont perpendiculaires, et aa′ + bb′ = 1 × 0 + 0 × 1 = 0 le confirme.
:::

::: verifie Droite perpendiculaire
Donner une équation de la perpendiculaire à D : 3x − 2y + 5 = 0 passant par O(0 ; 0).
---
Un vecteur normal à D est (3 ; −2) : la perpendiculaire est dirigée par ce vecteur, donc son vecteur normal est (2 ; 3), orthogonal à (3 ; −2) puisque 3 × 2 + (−2) × 3 = 0. Elle passe par O : 2x + 3y = 0. Contrôle : aa′ + bb′ = 3 × 2 + (−2) × 3 = 0.
:::

::: retenir
En repère orthonormé, (a ; b) est un vecteur normal à ax + by + c = 0, et D ⊥ D′ si et seulement si aa′ + bb′ = 0, à ne pas confondre avec ab′ − a′b = 0, qui teste le parallélisme.
:::

## 📈 Équation réduite et coefficient directeur

Une rampe d'accès est la droite D : 3x + 4y − 12 = 0, dans un repère orthonormé dont l'unité est le mètre. Quand on avance de 1 m vers la droite, de combien la rampe monte-t-elle ou descend-elle ?
Pour répondre, on cherche à écrire y en fonction de x.

::: definition
Si b ≠ 0, l'équation ax + by + c = 0 s'écrit y = mx + p. Cette écriture est l'**équation réduite** de D ; m est son **coefficient directeur** (ou **pente**) et p est son **ordonnée à l'origine**.
:::

::: figure La rampe D coupe l'axe des ordonnées en (0 ; 3) : p = 3. Pour 4 unités vers la droite, elle descend de 3 : m = −3/4. Dans le triangle rectangle de côtés 4 et 3, l'angle α que fait D avec l'axe des abscisses a pour tangente 3/4
<svg viewBox="0 0 278 210"><path d="M20 190 V20 M54 190 V20 M88 190 V20 M122 190 V20 M156 190 V20 M190 190 V20 M224 190 V20 M258 190 V20 M20 190 H258 M20 156 H258 M20 122 H258 M20 88 H258 M20 54 H258 M20 20 H258" fill="none" stroke="#94a3b8" stroke-width="0.8" opacity="0.55"/><path d="M20 156 H266 M54 190 V12" fill="none" stroke="#0f172a" stroke-width="1.8"/><path d="M263 152 L271 156 L263 160 Z M50 15 L54 7 L58 15 Z" fill="#0f172a"/><path d="M20 28.5 L235.3 190" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linecap="round"/><path d="M54 156 L190 156" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-dasharray="5 4"/><path d="M54 156 L54 54" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-dasharray="5 4"/><polyline points="165.5,137.6 164.9,138.4 164.4,139.3 163.9,140.1 163.4,140.9 162.9,141.8 162.5,142.7 162,143.6 161.7,144.5 161.3,145.4 161,146.3 160.7,147.3 160.4,148.2 160.2,149.2 160,150.1 159.8,151.1 159.7,152.1 159.5,153.1 159.5,154 159.4,155 159.4,156" fill="none" stroke="#0f172a" stroke-width="1.6"/><circle cx="54" cy="54" r="4.5" fill="#0f6e56"/><circle cx="190" cy="156" r="4.5" fill="#0f6e56"/><g font-size="10.5" text-anchor="middle" paint-order="stroke" stroke="#ffffff" stroke-width="3.2" stroke-linejoin="round"><text x="20" y="169" fill="#0f172a">−1</text><text x="88" y="169" fill="#0f172a">1</text><text x="122" y="169" fill="#0f172a">2</text><text x="156" y="169" fill="#0f172a">3</text><text x="190" y="169" fill="#0f172a">4</text><text x="224" y="169" fill="#0f172a">5</text><text x="258" y="169" fill="#0f172a">6</text><text x="49" y="194" fill="#0f172a" text-anchor="end">−1</text><text x="49" y="126" fill="#0f172a" text-anchor="end">1</text><text x="49" y="92" fill="#0f172a" text-anchor="end">2</text><text x="49" y="58" fill="#0f172a" text-anchor="end">3</text><text x="49" y="24" fill="#0f172a" text-anchor="end">4</text><text x="49" y="169" fill="#0f172a" text-anchor="end">O</text></g><g paint-order="stroke" stroke="#ffffff" stroke-width="3.6" stroke-linejoin="round"><text x="62" y="48" fill="#0f6e56" text-anchor="start" font-size="12" font-weight="700">(0 ; 3)</text><text x="122" y="149" fill="#0f172a" text-anchor="middle" font-size="12" font-weight="700">4</text><text x="64" y="109" fill="#0f172a" text-anchor="middle" font-size="12" font-weight="700">3</text><text x="156" y="150" fill="#0f172a" text-anchor="middle" font-size="14" font-weight="700">α</text><text x="200" y="147" fill="#0f6e56" text-anchor="middle" font-size="12" font-weight="700">(4 ; 0)</text></g></svg>
:::

Le nombre p est l'ordonnée du point où D coupe (Oy), et m mesure la variation de y quand x augmente de 1 : la pente se lit dans le triangle de la figure.

::: exemple De 3x + 4y − 12 = 0 à y = mx + p
1. On isole y : 4y = −3x + 12, car on change le signe d'un terme qui passe de l'autre côté. Puis on divise par 4 : y = −(3/4)x + 3.
2. Donc m = −3/4 et p = 3 : D coupe (Oy) en (0 ; 3). En avançant de 4, y varie de m × 4 = −3, ce qui donne le point (4 ; 0) de la figure.
3. Le vecteur u⃗(1 ; m) = (1 ; −3/4) dirige D : il joint les points (0 ; p) et (1 ; m + p). En général, si A et B sont sur D avec xA ≠ xB, alors m = (yB − yA)/(xB − xA) ; ici (0 − 3)/(4 − 0) = −3/4.
4. Dans le triangle rectangle de côtés 4 et 3, tan α = côté opposé / côté adjacent = 3/4 = |m|.

Autre exemple, sans contexte : la parallèle à D passant par A(3 ; 1) a la même pente −3/4 : y = −(3/4)x + p avec 1 = −9/4 + p, donc p = 13/4. La perpendiculaire a une pente m′ telle que mm′ = −1, soit m′ = 4/3 : y = (4/3)x + p′ avec 1 = 4 + p′, donc p′ = −3. Contrôle : (4/3) × 3 − 3 = 1.

:::

::: piege Lire m et p directement dans ax + by + c = 0
Dans 3x + 4y − 12 = 0, on lit « m = 3/4 et p = −12/4 = −3 », comme si l'équation était déjà résolue en y. Cela tente parce que les nombres sont sous les yeux. Mais il faut isoler y, ce qui change les signes : m = −3/4 et p = 3. Test : le point A(0 ; 3) est sur D, car 0 + 12 − 12 = 0, alors que y = (3/4)x − 3 donne −3 en x = 0.
:::

::: propriete
Le plan est muni d'un repère orthonormé. Toute droite D non parallèle à l'axe (Oy) a une équation réduite y = mx + p, avec m = −a/b et p = −c/b si D : ax + by + c = 0. Le vecteur u⃗(1 ; m) dirige D, le vecteur n⃗(m ; −1) lui est normal, et l'angle aigu α entre D et l'axe des abscisses vérifie tan α = |m|. Pour D′ : y = m′x + p′ : D ∥ D′ si et seulement si m = m′, et D ⊥ D′ si et seulement si mm′ = −1.

- Si A et B sont deux points de D d'abscisses différentes, m = (yB − yA)/(xB − xA).
- Cas limites : une droite parallèle à (Oy) a pour équation x = k et n'a ni pente ni équation réduite ; une droite horizontale y = p a pour pente 0 ; les droites y = p et x = k sont perpendiculaires bien que la seconde n'ait pas de pente.
:::

::: verifie Équation réduite et perpendiculaire
Donner l'équation réduite de D : 2x − 5y + 10 = 0, puis la pente d'une perpendiculaire à D.
---
On isole y : −5y = −2x − 10, donc y = (2/5)x + 2 : m = 2/5 et p = 2. Une perpendiculaire a pour pente m′ avec mm′ = −1, soit m′ = −5/2. Contrôle : (2/5) × (−5/2) = −1.
:::

::: retenir
Si b ≠ 0, ax + by + c = 0 s'écrit y = mx + p avec m = −a/b et p = −c/b ; deux droites sont parallèles si m = m′, perpendiculaires (repère orthonormé) si mm′ = −1, et une droite x = k n'a pas de pente.
:::

## ∨ La fonction x ↦ |ax + b|

On compare le nombre 2x au nombre 3 : l'écart entre les deux vaut |2x − 3|. Pour x = 0, l'écart est 3 ; pour x = 1, il est 1 ; pour x = 3/2, il est nul ; pour x = 3, il est de nouveau 3.
Quelle courbe dessinent ces écarts quand x varie ?

::: definition
Soit a ≠ 0 et b deux réels. La fonction f : x ↦ |ax + b| est définie sur ℝ par f(x) = ax + b si ax + b ≥ 0, et par f(x) = −(ax + b) si ax + b < 0.
:::

::: figure La courbe de x ↦ |2x − 3| (en vert) est formée de deux demi-droites qui se rejoignent au point (3/2 ; 0) de l'axe des abscisses ; en tirets gris, les droites y = 2x − 3 et y = −2x + 3 dont elles sont des morceaux
<svg viewBox="0 0 200 232"><path d="M20 212 V20 M52 212 V20 M84 212 V20 M116 212 V20 M148 212 V20 M180 212 V20 M20 212 H180 M20 180 H180 M20 148 H180 M20 116 H180 M20 84 H180 M20 52 H180 M20 20 H180" fill="none" stroke="#94a3b8" stroke-width="0.8" opacity="0.55"/><path d="M20 180 H188 M52 212 V12" fill="none" stroke="#0f172a" stroke-width="1.8"/><path d="M185 176 L193 180 L185 184 Z M48 15 L52 7 L56 15 Z" fill="#0f172a"/><path d="M84 212 L180 20" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-dasharray="6 4"/><path d="M20 20 L116 212" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-dasharray="6 4"/><polyline points="20,20 21.6,23.2 23.2,26.4 24.8,29.6 26.4,32.8 28,36 29.6,39.2 31.2,42.4 32.8,45.6 34.4,48.8 36,52 37.6,55.2 39.2,58.4 40.8,61.6 42.4,64.8 44,68 45.6,71.2 47.2,74.4 48.8,77.6 50.4,80.8 52,84 53.6,87.2 55.2,90.4 56.8,93.6 58.4,96.8 60,100 61.6,103.2 63.2,106.4 64.8,109.6 66.4,112.8 68,116 69.6,119.2 71.2,122.4 72.8,125.6 74.4,128.8 76,132 77.6,135.2 79.2,138.4 80.8,141.6 82.4,144.8 84,148 85.6,151.2 87.2,154.4 88.8,157.6 90.4,160.8 92,164 93.6,167.2 95.2,170.4 96.8,173.6 98.4,176.8 100,180 101.6,176.8 103.2,173.6 104.8,170.4 106.4,167.2 108,164 109.6,160.8 111.2,157.6 112.8,154.4 114.4,151.2 116,148 117.6,144.8 119.2,141.6 120.8,138.4 122.4,135.2 124,132 125.6,128.8 127.2,125.6 128.8,122.4 130.4,119.2 132,116 133.6,112.8 135.2,109.6 136.8,106.4 138.4,103.2 140,100 141.6,96.8 143.2,93.6 144.8,90.4 146.4,87.2 148,84 149.6,80.8 151.2,77.6 152.8,74.4 154.4,71.2 156,68 157.6,64.8 159.2,61.6 160.8,58.4 162.4,55.2 164,52 165.6,48.8 167.2,45.6 168.8,42.4 170.4,39.2 172,36 173.6,32.8 175.2,29.6 176.8,26.4 178.4,23.2 180,20" fill="none" stroke="#0f6e56" stroke-width="3.2" stroke-linejoin="round" stroke-linecap="round"/><circle cx="52" cy="84" r="4" fill="#0f6e56"/><circle cx="148" cy="84" r="4" fill="#0f6e56"/><circle cx="100" cy="180" r="5" fill="#b45309"/><g font-size="10.5" text-anchor="middle" paint-order="stroke" stroke="#ffffff" stroke-width="3.2" stroke-linejoin="round"><text x="20" y="193" fill="#0f172a">−1</text><text x="84" y="193" fill="#0f172a">1</text><text x="116" y="193" fill="#0f172a">2</text><text x="148" y="193" fill="#0f172a">3</text><text x="180" y="193" fill="#0f172a">4</text><text x="47" y="216" fill="#0f172a" text-anchor="end">−1</text><text x="47" y="152" fill="#0f172a" text-anchor="end">1</text><text x="47" y="120" fill="#0f172a" text-anchor="end">2</text><text x="47" y="88" fill="#0f172a" text-anchor="end">3</text><text x="47" y="56" fill="#0f172a" text-anchor="end">4</text><text x="47" y="24" fill="#0f172a" text-anchor="end">5</text><text x="47" y="193" fill="#0f172a" text-anchor="end">O</text></g><g paint-order="stroke" stroke="#ffffff" stroke-width="3.6" stroke-linejoin="round"><text x="60" y="78" fill="#0f6e56" text-anchor="start" font-size="12" font-weight="700">(0 ; 3)</text><text x="140" y="78" fill="#0f6e56" text-anchor="end" font-size="12" font-weight="700">(3 ; 3)</text><text x="100" y="214" fill="#b45309" text-anchor="middle" font-size="12" font-weight="700">(3/2 ; 0)</text></g></svg>
:::

La demi-droite de droite est portée par y = 2x − 3 et celle de gauche par y = −2x + 3 : le signe de 2x − 3 décide de la branche.

::: exemple La courbe de f(x) = |2x − 3|
1. On cherche où 2x − 3 change de signe : 2x − 3 ≥ 0 si et seulement si x ≥ 3/2. Le raccord est donc au point (3/2 ; 0), puisque f(3/2) = |0| = 0.
2. Pour x ≥ 3/2, f(x) = 2x − 3 : demi-droite de pente 2, qui passe par (3/2 ; 0) et par (3 ; 3).
3. Pour x < 3/2, 2x − 3 est négatif, donc f(x) = −(2x − 3) = −2x + 3 : tous les termes changent de signe, et l'on obtient la symétrique de la droite précédente par rapport à l'axe des abscisses. Cette demi-droite passe par (0 ; 3) et par (1 ; 1).
4. Contrôle : f(0) = |−3| = 3 et f(3) = |3| = 3 ; ces points sont symétriques par rapport à la droite x = 3/2.
5. Résoudre |2x − 3| = x : sur [3/2 ; +∞[, 2x − 3 = x donne x = 3, valeur acceptée car 3 ≥ 3/2 ; sur ]−∞ ; 3/2[, −2x + 3 = x donne x = 1, acceptée car 1 < 3/2. Les solutions sont 1 et 3.

Autre exemple, sans contexte (cas a < 0) : g(x) = |−2x + 6|. On a −2x + 6 ≥ 0 si et seulement si x ≤ 3, donc g(x) = −2x + 6 pour x ≤ 3 et g(x) = 2x − 6 pour x > 3. Le raccord est (3 ; 0), et g(4) = |−2| = 2 = 2 × 4 − 6.

:::

::: piege Changer seulement le signe du terme constant
Pour x < 3/2, on écrit |2x − 3| = 2x + 3. Cela tente parce que « la valeur absolue enlève le signe moins » du 3. Mais l'opposé de 2x − 3 est −2x + 3 : tous les termes changent de signe. Test : x = 1 donne |2 − 3| = 1, alors que 2 × 1 + 3 = 5.
:::

::: propriete
La courbe de f : x ↦ |ax + b| est formée de deux demi-droites, portées par y = ax + b et par y = −ax − b, qui se rejoignent au point (−b/a ; 0). On a f(x) ≥ 0 pour tout x, f(−b/a) = 0 est le minimum, et la courbe est symétrique par rapport à la droite x = −b/a.

- Cas limite : si a > 0, la branche y = ax + b est à droite du raccord ; si a < 0, elle est à gauche, comme pour g(x) = |−2x + 6|.
:::

::: verifie Écrire sans valeur absolue
Écrire h(x) = |4x + 2| sans valeur absolue, puis donner le point de raccord de sa courbe.
---
On a 4x + 2 ≥ 0 si et seulement si x ≥ −1/2 : pour x ≥ −1/2, h(x) = 4x + 2 ; pour x < −1/2, h(x) = −(4x + 2) = −4x − 2. Le raccord est (−1/2 ; 0), car h(−1/2) = |−2 + 2| = 0.
:::

::: retenir
La courbe de |ax + b| garde la droite y = ax + b là où ax + b ≥ 0 et prend son symétrique par rapport à l'axe des abscisses ailleurs : un V dont la pointe (−b/a ; 0) est sur l'axe des abscisses.
:::

## 📏 Distance d'un point à une droite

Dans un repère orthonormé (unité : le kilomètre), une ferme est au point P(1 ; 4) et la piste est la droite D : x + 2y − 6 = 0. Le plus court chemin de la ferme à la piste rejoint la piste en un point H.
Où est H, et quelle est la longueur du chemin ?

::: definition
Soit D une droite et A un point. Le **projeté orthogonal** de A sur D est le point H de D tel que (AH) soit perpendiculaire à D. La **distance** de A à D, notée d(A ; D), est la distance AH.
:::

::: figure La distance de P à la piste D est la longueur PH, où H est le pied de la perpendiculaire à D passant par P ; tout autre point de D, comme C, est plus loin de P, car PC est l'hypoténuse du triangle rectangle PHC
<svg viewBox="0 0 250 250"><path d="M20 230 V20 M50 230 V20 M80 230 V20 M110 230 V20 M140 230 V20 M170 230 V20 M200 230 V20 M230 230 V20 M20 230 H230 M20 200 H230 M20 170 H230 M20 140 H230 M20 110 H230 M20 80 H230 M20 50 H230 M20 20 H230" fill="none" stroke="#94a3b8" stroke-width="0.8" opacity="0.55"/><path d="M20 200 H238 M80 230 V12" fill="none" stroke="#0f172a" stroke-width="1.8"/><path d="M235 196 L243 200 L235 204 Z M76 15 L80 7 L84 15 Z" fill="#0f172a"/><path d="M20 80 L230 185" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linecap="round"/><path d="M110 80 L140 140" fill="none" stroke="#94a3b8" stroke-width="1.8" stroke-linecap="round" stroke-dasharray="6 4"/><path d="M110 80 L92 116" fill="none" stroke="#b45309" stroke-width="3.4" stroke-linecap="round"/><path d="M101.4 120.7 L106.1 111.3 L96.7 106.6" fill="none" stroke="#0f172a" stroke-width="1.6"/><circle cx="110" cy="80" r="4.5" fill="#b45309"/><circle cx="92" cy="116" r="4.5" fill="#0f172a"/><circle cx="140" cy="140" r="4.5" fill="#0f172a"/><g font-size="10.5" text-anchor="middle" paint-order="stroke" stroke="#ffffff" stroke-width="3.2" stroke-linejoin="round"><text x="20" y="213" fill="#0f172a">−2</text><text x="50" y="213" fill="#0f172a">−1</text><text x="110" y="213" fill="#0f172a">1</text><text x="140" y="213" fill="#0f172a">2</text><text x="170" y="213" fill="#0f172a">3</text><text x="200" y="213" fill="#0f172a">4</text><text x="230" y="213" fill="#0f172a">5</text><text x="75" y="234" fill="#0f172a" text-anchor="end">−1</text><text x="75" y="174" fill="#0f172a" text-anchor="end">1</text><text x="75" y="144" fill="#0f172a" text-anchor="end">2</text><text x="75" y="114" fill="#0f172a" text-anchor="end">3</text><text x="75" y="84" fill="#0f172a" text-anchor="end">4</text><text x="75" y="54" fill="#0f172a" text-anchor="end">5</text><text x="75" y="24" fill="#0f172a" text-anchor="end">6</text><text x="75" y="213" fill="#0f172a" text-anchor="end">O</text></g><g paint-order="stroke" stroke="#ffffff" stroke-width="3.6" stroke-linejoin="round"><text x="99" y="76" fill="#b45309" text-anchor="middle" font-size="13" font-weight="700">P</text><text x="105" y="130" fill="#0f172a" text-anchor="middle" font-size="13" font-weight="700">H</text><text x="151" y="133" fill="#0f172a" text-anchor="middle" font-size="13" font-weight="700">C</text><text x="206" y="174" fill="#0f6e56" text-anchor="middle" font-size="14" font-weight="700">D</text></g></svg>
:::

PH est le plus court des segments qui joignent P à un point de D, puisque dans le triangle rectangle PHC l'hypoténuse PC dépasse PH.

::: exemple La distance de la ferme à la piste
1. L'équation de D donne a = 1, b = 2, c = −6. On remplace x et y par les coordonnées de P(1 ; 4) : 1 × 1 + 2 × 4 − 6 = 3. On garde la valeur absolue, |3| = 3, car une distance n'est jamais négative.
2. Le dénominateur est √(a² + b²) = √(1 + 4) = √5, la norme du vecteur normal (a ; b).
3. Donc d(P ; D) = 3/√5 = 3√5/5 ≈ 1,34 km.
4. Contrôle par H : la perpendiculaire à D passant par P est 2x − y + 2 = 0 (le canal du paragraphe précédent), qui coupe D en H(2/5 ; 14/5). Alors PH² = (3/5)² + (6/5)² = 9/25 + 36/25 = 9/5, donc PH = 3/√5.

Autre exemple, sans contexte : la distance du point A(2 ; −1) à la droite D : 3x − 4y + 7 = 0. Le numérateur vaut |3 × 2 − 4 × (−1) + 7| = |6 + 4 + 7| = 17 et le dénominateur √(9 + 16) = 5, donc d(A ; D) = 17/5 = 3,4.

:::

::: piege Oublier la racine
Pour D : 3x + 4y − 12 = 0 et le point O(0 ; 0), on calcule |−12|/(3² + 4²) = 12/25. Cela tente parce que a² + b² = 25 est déjà sous les yeux. Mais il manque la racine : d = 12/√25 = 12/5 = 2,4. Test : D coupe les axes en (4 ; 0) et (0 ; 3), et le triangle de côtés 3, 4 et 5 a pour aire (3 × 4)/2 = 6 = (5 × d)/2, donc d = 12/5.
:::

::: propriete
Le plan est muni d'un repère orthonormé. Si D : ax + by + c = 0 et A(xA ; yA), alors d(A ; D) = |axA + byA + c| / √(a² + b²).

- Pourquoi : AH⃗ est colinéaire au vecteur normal (a ; b), donc AH⃗ = k(a ; b) et AH = |k|√(a² + b²) ; le calcul des coordonnées de H donne |k|(a² + b²) = |axA + byA + c|.
- Cas limite : d(A ; D) = 0 si et seulement si A est sur D, car le numérateur est alors nul.
:::

::: verifie Une distance à calculer
Calculer la distance du point B(2 ; 1) à la droite D : 6x + 8y − 5 = 0.
---
Le numérateur vaut |6 × 2 + 8 × 1 − 5| = |12 + 8 − 5| = 15 et le dénominateur √(36 + 64) = 10, donc d(B ; D) = 15/10 = 1,5.
:::

::: retenir
En repère orthonormé, d(A ; D) = |axA + byA + c| / √(a² + b²) : le numérateur est en valeur absolue et le dénominateur porte la racine.
:::

## ⭕ Équation d'un cercle

Dans un repère orthonormé (unité : le kilomètre), un émetteur placé au point I(3 ; 1) couvre exactement les points situés à 5 km de lui ou moins. Le village A(6 ; 5), le hameau C(1 ; 2) et la ferme E(8 ; 3) sont-ils couverts ?
Pour répondre, il faut traduire « à la distance 5 de I » en une équation.

::: definition
Soit I(a ; b) un point et R un réel strictement positif. Le **cercle** de centre I et de rayon R est l'ensemble des points M(x ; y) tels que IM = R. Il a pour **équation cartésienne** (x − a)² + (y − b)² = R².
:::

::: figure Le cercle de centre I(3 ; 1) et de rayon 5 : A est sur le cercle, C à l'intérieur, E à l'extérieur
<svg viewBox="0 0 326 326"><path d="M20 306 V20 M42 306 V20 M64 306 V20 M86 306 V20 M108 306 V20 M130 306 V20 M152 306 V20 M174 306 V20 M196 306 V20 M218 306 V20 M240 306 V20 M262 306 V20 M284 306 V20 M306 306 V20 M20 306 H306 M20 284 H306 M20 262 H306 M20 240 H306 M20 218 H306 M20 196 H306 M20 174 H306 M20 152 H306 M20 130 H306 M20 108 H306 M20 86 H306 M20 64 H306 M20 42 H306 M20 20 H306" fill="none" stroke="#94a3b8" stroke-width="0.8" opacity="0.55"/><path d="M20 196 H314 M108 306 V12" fill="none" stroke="#0f172a" stroke-width="1.8"/><path d="M311 192 L319 196 L311 200 Z M104 15 L108 7 L112 15 Z" fill="#0f172a"/><circle cx="174" cy="174" r="110" fill="#0f6e56" opacity="0.08"/><circle cx="174" cy="174" r="110" fill="none" stroke="#0f6e56" stroke-width="2.8"/><path d="M174 174 L240 86" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-dasharray="5 4"/><circle cx="174" cy="174" r="4.5" fill="#0f172a"/><circle cx="240" cy="86" r="4.5" fill="#0f6e56"/><circle cx="130" cy="152" r="4.5" fill="#b45309"/><circle cx="284" cy="130" r="4.5" fill="#6d28d9"/><g font-size="10.5" text-anchor="middle" paint-order="stroke" stroke="#ffffff" stroke-width="3.2" stroke-linejoin="round"><text x="20" y="209" fill="#0f172a">−4</text><text x="42" y="209" fill="#0f172a">−3</text><text x="64" y="209" fill="#0f172a">−2</text><text x="86" y="209" fill="#0f172a">−1</text><text x="130" y="209" fill="#0f172a">1</text><text x="152" y="209" fill="#0f172a">2</text><text x="174" y="209" fill="#0f172a">3</text><text x="196" y="209" fill="#0f172a">4</text><text x="218" y="209" fill="#0f172a">5</text><text x="240" y="209" fill="#0f172a">6</text><text x="262" y="209" fill="#0f172a">7</text><text x="284" y="209" fill="#0f172a">8</text><text x="306" y="209" fill="#0f172a">9</text><text x="103" y="310" fill="#0f172a" text-anchor="end">−5</text><text x="103" y="288" fill="#0f172a" text-anchor="end">−4</text><text x="103" y="266" fill="#0f172a" text-anchor="end">−3</text><text x="103" y="244" fill="#0f172a" text-anchor="end">−2</text><text x="103" y="222" fill="#0f172a" text-anchor="end">−1</text><text x="103" y="178" fill="#0f172a" text-anchor="end">1</text><text x="103" y="156" fill="#0f172a" text-anchor="end">2</text><text x="103" y="134" fill="#0f172a" text-anchor="end">3</text><text x="103" y="112" fill="#0f172a" text-anchor="end">4</text><text x="103" y="90" fill="#0f172a" text-anchor="end">5</text><text x="103" y="68" fill="#0f172a" text-anchor="end">6</text><text x="103" y="46" fill="#0f172a" text-anchor="end">7</text><text x="103" y="24" fill="#0f172a" text-anchor="end">8</text><text x="103" y="209" fill="#0f172a" text-anchor="end">O</text></g><g paint-order="stroke" stroke="#ffffff" stroke-width="3.6" stroke-linejoin="round"><text x="163" y="186" fill="#0f172a" text-anchor="middle" font-size="13" font-weight="700">I</text><text x="251" y="80" fill="#0f6e56" text-anchor="middle" font-size="13" font-weight="700">A</text><text x="125" y="143" fill="#b45309" text-anchor="middle" font-size="13" font-weight="700">C</text><text x="295" y="124" fill="#6d28d9" text-anchor="middle" font-size="13" font-weight="700">E</text><text x="198" y="128" fill="#0f172a" text-anchor="middle" font-size="12" font-weight="700">5</text></g></svg>
:::

Le centre se lit dans les parenthèses, a avec x − a et b avec y − b, et le second membre est R², le carré du rayon IA = 5.

::: exemple L'émetteur et ses trois points
1. En repère orthonormé, IM² = (x − 3)² + (y − 1)², et IM = 5 équivaut à IM² = 25 puisque IM ≥ 0. L'équation est (x − 3)² + (y − 1)² = 25.
2. A(6 ; 5) : (6 − 3)² + (5 − 1)² = 9 + 16 = 25, donc A est sur le cercle.
3. C(1 ; 2) : (1 − 3)² + (2 − 1)² = 4 + 1 = 5 < 25, donc C est à l'intérieur : IC < 5.
4. E(8 ; 3) : (8 − 3)² + (3 − 1)² = 25 + 4 = 29 > 25, donc E est à l'extérieur : IE > 5. Seuls A et C sont couverts.

Autre exemple, sans contexte : x² + y² − 4x + 6y − 12 = 0. On complète les carrés : x² − 4x = (x − 2)² − 4 et y² + 6y = (y + 3)² − 9, donc (x − 2)² + (y + 3)² − 4 − 9 − 12 = 0, soit (x − 2)² + (y + 3)² = 25. C'est le cercle de centre (2 ; −3) et de rayon 5.

:::

::: piege Lire le centre avec le signe de la parenthèse
Dans (x − 3)² + (y + 1)² = 16, on lit le centre (−3 ; 1). Cela tente parce qu'on recopie les nombres avec les signes écrits. Mais (x − 3)² s'annule pour x = 3 et (y + 1)² pour y = −1 : le centre est (3 ; −1). Test : les points (7 ; −1) et (−1 ; −1) sont sur ce cercle (4² + 0² = 16 et (−4)² + 0² = 16) et leur milieu est (3 ; −1).
:::

::: propriete
Le plan est muni d'un repère orthonormé. Soit C le cercle d'équation (x − a)² + (y − b)² = R² et M(x ; y) un point. M est sur C si (x − a)² + (y − b)² = R², à l'intérieur de C si (x − a)² + (y − b)² < R², à l'extérieur si (x − a)² + (y − b)² > R².

- Une équation x² + y² + px + qy + r = 0 s'écrit (x + p/2)² + (y + q/2)² = K avec K = p²/4 + q²/4 − r. Si K > 0, c'est le cercle de centre (−p/2 ; −q/2) et de rayon √K ; si K = 0, le seul point (−p/2 ; −q/2) ; si K < 0, aucun point.
- Des points sont dits **cocycliques** lorsqu'ils sont sur un même cercle. La question n'a d'intérêt qu'à partir de quatre points, car trois points non alignés sont toujours sur un même cercle. Par exemple, A(6 ; 5), F(−2 ; 1), G(8 ; 1) et H(3 ; 6) vérifient tous les quatre (x − 3)² + (y − 1)² = 25 : 9 + 16 = 25, 25 + 0 = 25, 25 + 0 = 25 et 0 + 25 = 25. Ils sont donc cocycliques.
:::

Une route D passe près de l'émetteur. Le cercle de centre I et de rayon 5 la rencontre-t-il ? Tout dépend de la distance d(I ; D) comparée au rayon.

::: figure La droite D touche le cercle en un seul point T : elle est tangente en T, et IT est perpendiculaire à D, donc la distance d(I ; D) est égale au rayon
<svg viewBox="0 0 326 326"><path d="M20 306 V20 M42 306 V20 M64 306 V20 M86 306 V20 M108 306 V20 M130 306 V20 M152 306 V20 M174 306 V20 M196 306 V20 M218 306 V20 M240 306 V20 M262 306 V20 M284 306 V20 M306 306 V20 M20 306 H306 M20 284 H306 M20 262 H306 M20 240 H306 M20 218 H306 M20 196 H306 M20 174 H306 M20 152 H306 M20 130 H306 M20 108 H306 M20 86 H306 M20 64 H306 M20 42 H306 M20 20 H306" fill="none" stroke="#94a3b8" stroke-width="0.8" opacity="0.55"/><path d="M20 196 H314 M108 306 V12" fill="none" stroke="#0f172a" stroke-width="1.8"/><path d="M311 192 L319 196 L311 200 Z M104 15 L108 7 L112 15 Z" fill="#0f172a"/><circle cx="174" cy="174" r="110" fill="#0f6e56" opacity="0.08"/><circle cx="174" cy="174" r="110" fill="none" stroke="#0f6e56" stroke-width="2.8"/><path d="M20 196 L152 20" fill="none" stroke="#b45309" stroke-width="2.6" stroke-linecap="round"/><path d="M174 174 L86 108" fill="none" stroke="#94a3b8" stroke-width="1.8" stroke-linecap="round" stroke-dasharray="5 4"/><path d="M94.8 114.6 L101.4 105.8 L92.6 99.2" fill="none" stroke="#0f172a" stroke-width="1.6"/><circle cx="174" cy="174" r="4.5" fill="#0f172a"/><circle cx="86" cy="108" r="4.5" fill="#b45309"/><g font-size="10.5" text-anchor="middle" paint-order="stroke" stroke="#ffffff" stroke-width="3.2" stroke-linejoin="round"><text x="20" y="209" fill="#0f172a">−4</text><text x="42" y="209" fill="#0f172a">−3</text><text x="64" y="209" fill="#0f172a">−2</text><text x="86" y="209" fill="#0f172a">−1</text><text x="130" y="209" fill="#0f172a">1</text><text x="152" y="209" fill="#0f172a">2</text><text x="174" y="209" fill="#0f172a">3</text><text x="196" y="209" fill="#0f172a">4</text><text x="218" y="209" fill="#0f172a">5</text><text x="240" y="209" fill="#0f172a">6</text><text x="262" y="209" fill="#0f172a">7</text><text x="284" y="209" fill="#0f172a">8</text><text x="306" y="209" fill="#0f172a">9</text><text x="103" y="310" fill="#0f172a" text-anchor="end">−5</text><text x="103" y="288" fill="#0f172a" text-anchor="end">−4</text><text x="103" y="266" fill="#0f172a" text-anchor="end">−3</text><text x="103" y="244" fill="#0f172a" text-anchor="end">−2</text><text x="103" y="222" fill="#0f172a" text-anchor="end">−1</text><text x="103" y="178" fill="#0f172a" text-anchor="end">1</text><text x="103" y="156" fill="#0f172a" text-anchor="end">2</text><text x="103" y="134" fill="#0f172a" text-anchor="end">3</text><text x="103" y="112" fill="#0f172a" text-anchor="end">4</text><text x="103" y="90" fill="#0f172a" text-anchor="end">5</text><text x="103" y="68" fill="#0f172a" text-anchor="end">6</text><text x="103" y="46" fill="#0f172a" text-anchor="end">7</text><text x="103" y="24" fill="#0f172a" text-anchor="end">8</text><text x="103" y="209" fill="#0f172a" text-anchor="end">O</text></g><g paint-order="stroke" stroke="#ffffff" stroke-width="3.6" stroke-linejoin="round"><text x="185" y="186" fill="#0f172a" text-anchor="middle" font-size="13" font-weight="700">I</text><text x="75" y="104" fill="#b45309" text-anchor="middle" font-size="13" font-weight="700">T</text><text x="82.8" y="53" fill="#b45309" text-anchor="middle" font-size="14" font-weight="700">D</text></g></svg>
:::

::: exemple Trois routes et le cercle de centre I(3 ; 1) et de rayon R = 5
1. D1 : 4x − 3y + 16 = 0 : d(I ; D1) = |12 − 3 + 16|/5 = 25/5 = 5 = R. D1 est tangente au cercle, au point T(−1 ; 4), pied de la perpendiculaire menée de I.
2. D2 : 3x + 4y − 4 = 0 : d(I ; D2) = |9 + 4 − 4|/5 = 9/5 = 1,8 < R. D2 coupe le cercle en deux points.
3. D3 : 4x − 3y − 40 = 0 : d(I ; D3) = |12 − 3 − 40|/5 = 31/5 = 6,2 > R. D3 ne rencontre pas le cercle.

:::

::: methode Position d'une droite et d'un cercle
Pour une droite D et le cercle de centre I et de rayon R, on calcule d = d(I ; D), puis on compare d et R : si d < R, D coupe le cercle en deux points ; si d = R, D est tangente, avec un seul point commun ; si d > R, D ne rencontre pas le cercle.

Cas limite : si d = R, le point de contact T est le pied de la perpendiculaire à D menée de I, et IT⃗ est un vecteur normal à D.
:::

::: verifie Centre et rayon
Donner le centre et le rayon du cercle d'équation x² + y² − 6x + 2y + 6 = 0.
---
On complète les carrés : x² − 6x = (x − 3)² − 9 et y² + 2y = (y + 1)² − 1, donc (x − 3)² + (y + 1)² − 9 − 1 + 6 = 0, soit (x − 3)² + (y + 1)² = 4. Le centre est (3 ; −1) et le rayon est 2, car 4 = 2².
:::

::: retenir
Le cercle de centre I(a ; b) et de rayon R a pour équation (x − a)² + (y − b)² = R² ; on le compare à une droite par d(I ; D) et R, et à un point en comparant (x − a)² + (y − b)² à R².
:::

> 🏆 Quête franchie, héros : tu sais calculer un milieu et un barycentre en coordonnées, écrire l'équation d'une droite, lire un vecteur directeur et un vecteur normal, décider d'un parallélisme ou d'une perpendicularité, passer à l'équation réduite, tracer la courbe de |ax + b|, calculer une distance à une droite et manier l'équation d'un cercle. Ces outils transformeront désormais toute figure en calcul : le prochain gate quitte le plan pour la **géométrie de l'espace**.
