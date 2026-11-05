# ⚔️ Équations de droites, de plans et de sphères — mettre l'espace en équations

> 💡 «Une droite, un plan, une sphère : trois objets de l'espace, trois façons d'écrire que des coordonnées leur appartiennent.»

Ce chapitre apprend à décrire par des équations les droites, les plans et les sphères de l'espace, puis à trancher leurs positions par le calcul : parallèles, perpendiculaires, sécants, tangents. Huit notions, de la représentation paramétrique d'une droite jusqu'à l'intersection d'une sphère et d'un plan. L'espace est rapporté à un repère (O, i⃗, j⃗, k⃗), orthonormé direct dès qu'il est question de distance ou de perpendicularité. On suppose connus le produit scalaire u⃗.v⃗ et le produit vectoriel u⃗ ∧ v⃗ du chapitre précédent.

## 🧭 Une droite se décrit avec un paramètre

Un faisceau laser part du point A(1, 0, 2) et passe par B(3, 2, 3).
Si on le prolonge, passe-t-il par C(7, 6, 5) ?
Pour le savoir, il faut décrire par des nombres tous les points de la droite (AB).

::: definition
Soit A un point et u⃗ un vecteur non nul. La droite D passant par A et de **vecteur directeur** u⃗ est l'ensemble des points M tels que AM⃗ = αu⃗, où α est un réel. Si A(x₀, y₀, z₀) et u⃗(a, b, c), M(x, y, z) est sur D si et seulement s'il existe un réel α tel que
$$ x = x₀ + αa ;  y = y₀ + αb ;  z = z₀ + αc $$
Ce système est une **représentation paramétrique** de D. Deux droites sont **parallèles** si leurs vecteurs directeurs sont colinéaires.
:::

::: figure La droite D passe par A avec le vecteur directeur u⃗ : chaque valeur du paramètre α donne un point, α = 0 pour A et α = 1 pour B = A + u⃗
<svg viewBox="0 15 340 95">
<title>Droite de point A et de vecteur directeur u, avec les points obtenus pour α = −1, 0, 1, 3</title>
<path d="M80.6 92.2 L297.2 42.2" fill="none" stroke="#0f172a" stroke-width="2.2" stroke-linecap="round"/>
<path d="M138.1 78.9 L173.5 70.7" fill="none" stroke="#0f6e56" stroke-width="3" stroke-linecap="round"/><path d="M182.3 68.7 L174.4 74.7 L172.6 66.8 Z" fill="#0f6e56"/>
<circle cx="93.9" cy="89.1" r="4.5" fill="#0f172a"/>
<text x="91.9" y="77.1" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">α = −1</text>
<circle cx="138.1" cy="78.9" r="4.5" fill="#0f6e56"/>
<text x="136.1" y="66.9" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">A (α = 0)</text>
<circle cx="182.3" cy="68.7" r="4.5" fill="#0f6e56"/>
<text x="186.3" y="90.7" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">B (α = 1)</text>
<circle cx="270.7" cy="48.3" r="4.5" fill="#0f172a"/>
<text x="270.7" y="36.3" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">C (α = 3)</text>
<text x="186.2" y="57.8" text-anchor="middle" font-size="15" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">u⃗</text>
</svg>
:::

Sur la figure, avancer de α fois le vecteur u⃗ à partir de A donne le point de paramètre α : le point de D est entièrement repéré par le seul nombre α.

::: exemple Le faisceau laser passe-t-il par C ?

1. On calcule le vecteur directeur : AB⃗(3 − 1, 2 − 0, 3 − 2) = (2, 2, 1), car il va de A à B.
2. La droite (AB) passe par A et est dirigée par AB⃗ : x = 1 + 2α ; y = 2α ; z = 2 + α.
3. C(7, 6, 5) est sur (AB) s'il existe **un même α** qui convient aux trois équations : 7 = 1 + 2α donne α = 3, puis 2α = 6 ✓ et 2 + α = 5 ✓.
4. Le même α = 3 convient aux trois coordonnées : C est sur la droite, le faisceau passe par C.

:::

::: exemple Où se coupent deux droites ?
Soit D : x = 1 + 2α ; y = 2α ; z = 2 + α et Δ : x = 3 + β ; y = 6 − β ; z = 2β.

1. Un point commun a un α pour D et un β pour Δ : on prend **deux lettres différentes**, car les deux droites n'avancent pas du même pas.
2. On égale les deux premières coordonnées : 1 + 2α = 3 + β et 2α = 6 − β. En additionnant, 1 + 4α = 9, donc α = 2 et β = 2.
3. On vérifie la troisième : 2 + α = 4 et 2β = 4 ✓.
4. Les droites sont sécantes au point obtenu pour α = 2 : (5, 4, 4).

:::

::: piege
**Erreur : prendre la même lettre pour les deux droites.** L'erreur tente parce qu'on écrit « α » partout. Pour D : x = 1 + 2α ; y = 2α ; z = 2 + α et Δ′ : x = β ; y = 5 − β ; z = β, poser α = β donne 1 + 2α = α, donc α = −1, puis 2α = −2 ≠ 6 : on conclurait à tort « aucun point commun ». Avec deux paramètres, 1 + 2α = β et 2α = 5 − β donnent α = 1, β = 3, et la troisième équation 3 = 3 ✓ : les droites se coupent en (3, 2, 3).
:::

::: propriete
- Un point est sur D si **un seul** réel α convient aux trois équations à la fois.
- Deux droites de vecteurs directeurs colinéaires sont parallèles (confondues si elles ont un point commun) ; sinon, on résout le système avec deux paramètres α et β : une solution donne un point commun, aucune solution signifie qu'elles ne se coupent pas.

Cas limite : si une coordonnée de u⃗ est nulle (b = 0 par exemple), la coordonnée y reste constante sur toute la droite.
:::

::: verifie À toi : le point appartient-il à la droite ?
La droite Δ passe par A(0, 2, −1) et B(2, 3, 2). Le point E(6, 5, m) est sur Δ : quelle est la valeur de m ?

---

AB⃗(2, 1, 3), donc Δ : x = 2α ; y = 2 + α ; z = −1 + 3α. Pour E, 6 = 2α donne α = 3, et 5 = 2 + α ✓ confirme le même α. Alors m = −1 + 3 × 3 = 8. On a bien utilisé un seul α pour les trois coordonnées.
:::

::: retenir
Une droite est donnée par un point et un vecteur directeur : x = x₀ + αa ; y = y₀ + αb ; z = z₀ + αc, et un point en fait partie si un même α convient aux trois équations.
:::

## 🧱 Un plan : un point et deux directions

Un toit plat repose sur trois poteaux dont les sommets sont A(1, 0, 2), B(2, 1, 0) et C(0, 2, 1).
Quelle équation vérifient les coordonnées de tous les points M de la toiture ?

::: definition
Soit A un point, u⃗(a, b, c) et v⃗(a′, b′, c′) deux vecteurs non colinéaires. Le plan P passant par A et de **vecteurs directeurs** u⃗ et v⃗ est l'ensemble des points M tels que det(AM⃗, u⃗, v⃗) = 0, c'est-à-dire tels que AM⃗, u⃗ et v⃗ sont coplanaires. Pour M(x, y, z), le développement du déterminant donne
$$ (x − x_A)(bc′ − cb′) + (y − y_A)(ca′ − ac′) + (z − z_A)(ab′ − ba′) = 0 $$
Il se réduit à une **équation cartésienne** de la forme ax + by + cz + d = 0 (ces a, b, c sont les trois coefficients calculés, pas les coordonnées de u⃗).
:::

::: figure Le plan (ABC) est engendré depuis A par u⃗ = AB⃗ et v⃗ = AC⃗ ; le point M s'obtient en avançant de 0,45 fois u⃗ puis de 0,4 fois v⃗ (valeurs choisies pour le dessin)
<svg viewBox="0 35 340 145">
<title>Plan (ABC) : le point M est atteint depuis A en avançant de 0,45 fois u puis de 0,4 fois v</title>
<path d="M108.1 63.9 L130.2 143.8 L210.1 165.9 L188 86 Z" fill="#0f6e56" fill-opacity="0.14" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/>
<path d="M108.1 63.9 L127.8 135.1" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linecap="round"/><path d="M130.2 143.8 L123.9 136.2 L131.7 134 Z" fill="#0f6e56"/>
<path d="M108.1 63.9 L179.3 83.6" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linecap="round"/><path d="M188 86 L178.2 87.5 L180.4 79.7 Z" fill="#0f6e56"/>
<path d="M108.1 63.9 L150 108.7" fill="none" stroke="#b45309" stroke-width="2" stroke-linecap="round" stroke-dasharray="5 4"/>
<circle cx="108.1" cy="63.9" r="4" fill="#0f172a"/>
<circle cx="130.2" cy="143.8" r="4" fill="#0f172a"/>
<circle cx="188" cy="86" r="4" fill="#0f172a"/>
<circle cx="150" cy="108.7" r="4.5" fill="#b45309"/>
<text x="96.1" y="57.9" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">A</text>
<text x="132.2" y="163.8" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">B</text>
<text x="202" y="84" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">C</text>
<text x="164" y="112.7" text-anchor="middle" font-size="13" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">M</text>
<text x="99.1" y="109.9" text-anchor="middle" font-size="15" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">u⃗</text>
<text x="150.1" y="65" text-anchor="middle" font-size="15" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">v⃗</text>
</svg>
:::

Sur la figure, M est dans le plan parce que AM⃗ s'écrit à l'aide de u⃗ et de v⃗ : les trois vecteurs AM⃗, u⃗, v⃗ sont coplanaires, ce que traduit le déterminant nul.

::: exemple L'équation du toit, puis d'un plan parallèle

1. On prend A comme origine et deux vecteurs : u⃗ = AB⃗(1, 1, −2) et v⃗ = AC⃗(−1, 2, −1), non colinéaires car aucun n'est multiple de l'autre.
2. On calcule les trois coefficients : bc′ − cb′ = 1×(−1) − (−2)×2 = 3 ; ca′ − ac′ = (−2)×(−1) − 1×(−1) = 3 ; ab′ − ba′ = 1×2 − 1×(−1) = 3.
3. L'équation est 3(x − 1) + 3y + 3(z − 2) = 0, soit x + y + z − 3 = 0. On contrôle avec B : 2 + 1 + 0 − 3 = 0 ✓ et avec C : 0 + 2 + 1 − 3 = 0 ✓.
4. Un plan Q passant par D(2, −1, 4) et dirigé par les **mêmes** u⃗ et v⃗ a les mêmes coefficients : x + y + z + d = 0, avec 2 − 1 + 4 + d = 0, donc d = −5. Q : x + y + z − 5 = 0 est parallèle à P.

:::

::: piege
**Erreur : écrire x, y, z au lieu de x − x_A, y − y_A, z − z_A.** L'erreur tente parce que les coefficients ressemblent à une équation toute faite. Ici, elle donnerait 3x + 3y + 3z = 0, plan qui passe par O. Mais A(1, 0, 2) n'y est pas : 3 + 0 + 6 ≠ 0. Le déterminant se forme avec AM⃗, pas avec OM⃗.
:::

::: propriete
- Tout plan a une équation ax + by + cz + d = 0 avec (a, b, c) ≠ (0, 0, 0), et tout ensemble de cette forme est un plan.
- Les plans P(A, u⃗, v⃗) et P(B, u⃗, v⃗) ont mêmes coefficients a, b, c : ils sont parallèles.
- Le plan (O, i⃗, k⃗) a pour équation y = 0 et le plan (A, i⃗, k⃗) a pour équation y = y_A ; de même pour les deux autres plans de base.

Cas limite : si u⃗ et v⃗ sont colinéaires, les trois coefficients sont nuls et l'on n'obtient aucun plan, d'où l'exigence de vecteurs non colinéaires.
:::

::: verifie À toi : un plan par un point et deux vecteurs
Quelle est l'équation du plan passant par A(1, 0, −1) et dirigé par u⃗(2, 1, 0) et v⃗(0, 1, 3) ?

---

bc′ − cb′ = 1×3 − 0×1 = 3 ; ca′ − ac′ = 0×0 − 2×3 = −6 ; ab′ − ba′ = 2×1 − 1×0 = 2. L'équation est 3(x − 1) − 6y + 2(z + 1) = 0, soit 3x − 6y + 2z − 1 = 0. Contrôle : A donne 3 − 0 − 2 − 1 = 0 ✓, et u⃗ : 3×2 − 6×1 + 0 = 0 ✓.
:::

::: retenir
Un plan est donné par un point A et deux vecteurs non colinéaires : det(AM⃗, u⃗, v⃗) = 0 se développe en ax + by + cz + d = 0, et deux plans de mêmes vecteurs directeurs sont parallèles.
:::

## 📐 Le vecteur normal : l'équation du plan se lit

Un mât est planté droit sur un sol plat.
Dans l'équation du toit x + y + z − 3 = 0 du paragraphe précédent, les coefficients valaient 3, 3, 3 avant simplification : comment lire sur l'équation la direction perpendiculaire au plan ?

::: definition
Le repère est orthonormé. Un vecteur non nul n⃗ est **normal** à un plan P s'il est orthogonal à deux vecteurs directeurs de P : n⃗.u⃗ = n⃗.v⃗ = 0. Toute droite dirigée par n⃗ est alors perpendiculaire à P.
:::

::: figure Le vecteur normal n⃗ part de A perpendiculairement au plan P : il est orthogonal à AM⃗ pour tout point M de P
<svg viewBox="0 85 340 180">
<title>Le vecteur normal n part de A perpendiculairement au plan P : il est orthogonal à AM pour tout point M de P</title>
<path d="M60 190 L264 190 L216.4 237.6 L12.4 237.6 Z" fill="#0f6e56" fill-opacity="0.12" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/>
<path d="M121.2 213.8 L121.2 114" fill="none" stroke="#0f6e56" stroke-width="3" stroke-linecap="round"/><path d="M121.2 105 L125.2 114 L117.2 114 Z" fill="#0f6e56"/>
<path d="M121.2 213.8 L176.3 226.1" fill="none" stroke="#0f172a" stroke-width="2.2" stroke-linecap="round"/><path d="M185.1 228.1 L175.5 230.1 L177.2 222.2 Z" fill="#0f172a"/>
<path d="M121.2 213.8 L132.3 216.3 L132.3 201 L121.2 198.5 Z" fill="none" stroke="#b45309" stroke-width="1.6" stroke-linejoin="round"/>
<circle cx="121.2" cy="213.8" r="4" fill="#0f172a"/>
<circle cx="185.1" cy="228.1" r="4" fill="#0f172a"/>
<text x="109.2" y="229.8" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">A</text>
<text x="199.1" y="232.1" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">M</text>
<text x="135.2" y="109" text-anchor="middle" font-size="16" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">n⃗</text>
<text x="34.2" y="254.8" text-anchor="middle" font-size="16" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">P</text>
</svg>
:::

Sur la figure, n⃗ est le vecteur vertical au point A et AM⃗ un vecteur quelconque du plan : leur produit scalaire est nul, quelle que soit la position de M.

Les trois coefficients du développement du déterminant sont les coordonnées de u⃗ ∧ v⃗ = (bc′ − cb′, ca′ − ac′, ab′ − ba′) : ce vecteur est orthogonal à u⃗ et à v⃗, donc normal au plan.

::: exemple Le plan par un point et un vecteur normal, puis par trois points

1. Plan passant par A(1, −2, 0) de vecteur normal n⃗(2, −1, 3) : M est dans le plan si AM⃗.n⃗ = 0, soit 2(x − 1) − (y + 2) + 3z = 0, donc 2x − y + 3z − 4 = 0. Contrôle : A donne 2 + 2 + 0 − 4 = 0 ✓.
2. Plan (ABC) pour A(1, 0, 1), B(2, 2, 0), C(0, 1, 3) : AB⃗(1, 2, −1) et AC⃗(−1, 1, 2), non colinéaires.
3. On prend n⃗ = AB⃗ ∧ AC⃗ = (2×2 − (−1)×1, (−1)×(−1) − 1×2, 1×1 − 2×(−1)) = (5, −1, 3), qui est normal car orthogonal aux deux vecteurs.
4. L'équation est 5(x − 1) − y + 3(z − 1) = 0, soit 5x − y + 3z − 8 = 0. Contrôle : B donne 10 − 2 + 0 − 8 = 0 ✓ et C donne 0 − 1 + 9 − 8 = 0 ✓.
5. La droite passant par O et perpendiculaire à (ABC) est dirigée par n⃗ : x = 5α ; y = −α ; z = 3α.

:::

::: piege
**Erreur : prendre (a, b, c) pour un vecteur du plan.** L'erreur tente parce que ces trois nombres sont lus dans l'équation. Pour 2x − y + 3z − 4 = 0, le vecteur (2, −1, 3) ne vérifie pas 2α − β + 3γ = 0, car 2×2 + (−1)×(−1) + 3×3 = 14 ≠ 0 : il n'est pas dans le plan, il lui est perpendiculaire. Un vecteur du plan vérifie 2α − β + 3γ = 0, comme (1, 2, 0).
:::

::: propriete
Si P a pour équation ax + by + cz + d = 0, alors n⃗(a, b, c) est normal à P. Réciproquement, l'ensemble des points M tels que AM⃗.n⃗ = 0 est le plan passant par A de vecteur normal n⃗. Un vecteur normal n'est défini qu'à un facteur près : (2, −1, 3) et (4, −2, 6) conviennent pour le même plan.

Cas limite : si l'équation ne contient pas z (par exemple x + y − 3 = 0), n⃗(1, 1, 0) est normal : le plan est parallèle à l'axe des cotes.
:::

::: verifie À toi : la perpendiculaire à un plan
Quelle est une représentation paramétrique de la droite passant par M(1, 2, −1) et perpendiculaire au plan 3x − y + 2z + 4 = 0 ?

---

Le vecteur normal n⃗(3, −1, 2) dirige la perpendiculaire, qui passe par M : x = 1 + 3α ; y = 2 − α ; z = −1 + 2α. Elle est dirigée par le vecteur normal car une droite de vecteur directeur n⃗ est perpendiculaire au plan.
:::

::: retenir
Les coefficients (a, b, c) de ax + by + cz + d = 0 forment un vecteur normal au plan ; n⃗ = AB⃗ ∧ AC⃗ est normal à (ABC), et AM⃗.n⃗ = 0 décrit le plan.
:::

## 📏 La distance d'un point à un plan

Un drone en M(3, 0, 3) survole un toit plat d'équation 2x − y + 2z − 3 = 0.
À quelle distance du toit est-il, et au-dessus de quel point du toit ?

::: definition
Le repère est orthonormé. La **distance** du point M(x₀, y₀, z₀) au plan P d'équation ax + by + cz + d = 0 est le réel
$$ d(M, P) = |ax₀ + by₀ + cz₀ + d| / √(a² + b² + c²) $$
Le **projeté orthogonal** H de M sur P est le point de P tel que MH⃗ est normal à P : c'est le point de P le plus proche de M, et d(M, P) = MH.
:::

::: figure Le projeté orthogonal H de M sur P : le segment MH est perpendiculaire à P et il est plus court que MX pour tout autre point X de P
<svg viewBox="0 88 340 185">
<title>Le projeté orthogonal H de M sur P est le point de P le plus proche de M : d = MH est la distance de M au plan</title>
<path d="M60 200 L264 200 L216.4 247.6 L12.4 247.6 Z" fill="#0f6e56" fill-opacity="0.12" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/>
<path d="M140.6 105.8 L180.7 235.7" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-dasharray="5 4"/>
<path d="M140.6 221.4 L180.7 235.7" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-dasharray="5 4"/>
<path d="M140.6 105.8 L140.6 221.4" fill="none" stroke="#b45309" stroke-width="3" stroke-linecap="round"/>
<path d="M140.6 221.4 L155.9 221.4 L155.9 206.1 L140.6 206.1 Z" fill="none" stroke="#b45309" stroke-width="1.6" stroke-linejoin="round"/>
<circle cx="140.6" cy="105.8" r="4.5" fill="#0f172a"/>
<circle cx="140.6" cy="221.4" r="4.5" fill="#b45309"/>
<circle cx="180.7" cy="235.7" r="3.5" fill="#94a3b8"/>
<text x="154.6" y="107.8" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">M</text>
<text x="126.6" y="235.4" text-anchor="middle" font-size="13" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">H</text>
<text x="192.7" y="249.7" text-anchor="middle" font-size="13" font-weight="700" fill="#475569" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">X</text>
<text x="128" y="167.6" text-anchor="middle" font-size="15" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">d</text>
<text x="34.2" y="264.8" text-anchor="middle" font-size="16" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">P</text>
</svg>
:::

Sur la figure, la longueur du segment orange MH est la distance d de la formule ; tout autre point X du plan donne un segment MX plus long.

::: exemple La distance du drone, puis le point survolé

1. On remplace dans le numérateur : 2×3 − 0 + 2×3 − 3 = 9.
2. Le dénominateur est √(2² + (−1)² + 2²) = √9 = 3, donc d(M, P) = 9/3 = 3.
3. Le projeté H est sur la perpendiculaire à P menée par M, dirigée par n⃗(2, −1, 2) : H = (3 + 2k, −k, 3 + 2k) pour un réel k.
4. H est dans P : 2(3 + 2k) + k + 2(3 + 2k) − 3 = 9 + 9k = 0, donc k = −1 et H(1, 1, 1). Contrôle : MH = |k| × |n⃗| = 3 ✓, égal à la distance.

:::

::: piege
**Erreur : oublier de diviser par √(a² + b² + c²).** L'erreur tente parce que le numérateur est déjà un nombre. Ici elle donnerait « 9 » au lieu de 3. Elle ne tient pas : 4x − 2y + 4z − 6 = 0 décrit le même plan que 2x − y + 2z − 3 = 0, mais son numérateur vaudrait 18, alors que la distance du drone ne change pas. Seul le quotient par la norme du vecteur normal donne toujours 3.
:::

::: propriete
- d(M, P) = 0 si et seulement si M est dans P.
- Pour le projeté, on écrit H = M + kn⃗ et on détermine k en reportant les coordonnées de H dans l'équation de P ; on a alors MH = |k| × ‖n⃗‖.

Cas limite : si M est dans P, le numérateur est nul : la distance est 0 et H = M.
:::

::: verifie À toi : une distance
Quelle est la distance du point A(1, −1, 2) au plan 2x + 6y − 3z + 12 = 0 ?

---

Numérateur : 2×1 + 6×(−1) − 3×2 + 12 = 2. Dénominateur : √(4 + 36 + 9) = √49 = 7. La distance est 2/7. Le numérateur n'est pas la distance : on divise par la norme 7 du vecteur normal.
:::

::: retenir
d(M, P) = |ax₀ + by₀ + cz₀ + d| / √(a² + b² + c²), et le projeté orthogonal s'obtient avec H = M + kn⃗.
:::

## 🪟 Positions relatives de deux plans, d'une droite et d'un plan

Dans une salle, le plancher et un mur se rencontrent suivant une arête, deux murs en vis-à-vis ne se rencontrent jamais.
Comment le décider à partir des équations, et trouver l'arête ?

::: definition
Le repère est orthonormé. Deux plans sont **parallèles** si et seulement si leurs vecteurs normaux sont colinéaires. Deux plans sont **perpendiculaires** si et seulement si leurs vecteurs normaux sont orthogonaux. Deux plans non parallèles sont **sécants** suivant une droite.
:::

::: figure Deux plans perpendiculaires P et Q se coupent suivant la droite Δ ; leurs vecteurs normaux n⃗ et n⃗′ sont orthogonaux
<svg viewBox="0 0 340 250">
<title>Deux plans perpendiculaires P et Q se coupent suivant la droite Δ ; leurs vecteurs normaux n et n′ sont orthogonaux</title>
<path d="M75 175 L255 175 L213 217 L33 217 Z" fill="#0f6e56" fill-opacity="0.12" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/>
<path d="M165 175 L165 67 L123 109 L123 217 Z" fill="#b45309" fill-opacity="0.14" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/>
<path d="M168.2 171.8 L118.8 221.2" fill="none" stroke="#0f172a" stroke-width="3.2" stroke-linecap="round"/>
<path d="M144 196 L144 127" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linecap="round"/><path d="M144 118 L148.1 127 L139.9 127 Z" fill="#0f6e56"/>
<path d="M144 196 L198 196" fill="none" stroke="#b45309" stroke-width="2.8" stroke-linecap="round"/><path d="M207 196 L198 200.1 L198 191.9 Z" fill="#b45309"/>
<circle cx="144" cy="196" r="4" fill="#0f172a"/>
<text x="158" y="120" text-anchor="middle" font-size="16" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">n⃗</text>
<text x="223" y="200" text-anchor="middle" font-size="16" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">n⃗′</text>
<text x="114.7" y="241.3" text-anchor="middle" font-size="16" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">Δ</text>
<text x="96.7" y="185.3" text-anchor="middle" font-size="16" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">P</text>
<text x="156.6" y="90.4" text-anchor="middle" font-size="16" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">Q</text>
</svg>
:::

Sur la figure, n⃗ et n⃗′ forment un angle droit exactement quand les plans sont perpendiculaires, et la droite Δ est commune aux deux plans.

::: exemple Deux plans perpendiculaires, puis une droite et un plan

1. P : 2x − y + z − 4 = 0 et Q : x + 3y + z − 1 = 0 ont pour vecteurs normaux (2, −1, 1) et (1, 3, 1) : non colinéaires, donc sécants ; leur produit scalaire vaut 2 − 3 + 1 = 0 : ils sont perpendiculaires.
2. On cherche leur droite commune : l'équation de P donne z = 4 − 2x + y ; on reporte dans Q : x + 3y + 4 − 2x + y − 1 = 0, soit x = 4y + 3.
3. En posant y = α, on trouve x = 3 + 4α et z = 4 − 2(3 + 4α) + α = −2 − 7α : Δ : x = 3 + 4α ; y = α ; z = −2 − 7α. Contrôle : le vecteur (4, 1, −7) est orthogonal aux deux vecteurs normaux : 8 − 1 − 7 = 0 ✓ et 4 + 3 − 7 = 0 ✓.
4. Pour la droite D : x = 2 + α ; y = 1 − α ; z = 3 + 2α et le plan R : 2x + y − z − 1 = 0, on reporte : 2(2 + α) + (1 − α) − (3 + 2α) − 1 = 1 − α. Cette expression est nulle pour α = 1 : D coupe R au point (3, 0, 5).

:::

::: piege
**Erreur : conclure que deux plans sécants ont un seul point commun.** L'erreur tente parce qu'on résout un système et qu'on s'arrête dès qu'on a trouvé une solution. Pour P et Q ci-dessus, le point (3, 0, −2) est commun, mais ce n'est qu'un point de Δ : pour α = 1, Δ donne (7, 1, −9), qui est aussi commun. L'intersection est la droite entière.
:::

::: propriete
Pour une droite D et un plan P, on reporte la représentation paramétrique de D dans l'équation de P, ce qui donne kα + h = 0.
- Si k ≠ 0, il y a un seul point commun (D et P sont sécants).
- Si k = 0 et h ≠ 0, il n'y en a aucun : D est strictement parallèle à P.
- Si k = 0 et h = 0, tous les points de D sont dans P : D est contenue dans P.

Cas limite : k = 0 signifie que le vecteur directeur de D est orthogonal au vecteur normal de P.
:::

::: verifie À toi : l'intersection de deux plans
Déterminer l'intersection des plans P : x + y − 2z + 1 = 0 et Q : 2x − y + z − 4 = 0.

---

Les vecteurs normaux (1, 1, −2) et (2, −1, 1) ne sont pas colinéaires : les plans sont sécants. En additionnant, 3x − z − 3 = 0, donc z = 3x − 3. Alors y = 2z − 1 − x = 5x − 7. Avec x = α : x = α ; y = −7 + 5α ; z = −3 + 3α. Contrôle avec P : α − 7 + 5α − 2(−3 + 3α) + 1 = 0 ✓. L'intersection est une droite, pas un point.
:::

::: retenir
Plans parallèles : normaux colinéaires ; plans perpendiculaires : normaux orthogonaux ; sinon une droite commune ; pour une droite et un plan, on reporte dans l'équation et l'on discute kα + h = 0.
:::

## 🔵 La sphère : une équation, un centre, un rayon

Un radar placé en I(3, −1, 2) repère exactement à 3 km les balises d'une flotte.
Quels sont les points M de l'espace à 3 km de I ?
Et la balise A(5, 0, 4) est-elle l'une d'elles ?

::: definition
Soit I un point et R un réel strictement positif. La **sphère** de centre I et de rayon R est l'ensemble des points M tels que IM = R. Dans un repère orthonormé, si I(x₀, y₀, z₀), c'est l'ensemble des points M(x, y, z) tels que
$$ (x − x₀)² + (y − y₀)² + (z − z₀)² = R² $$
:::

::: figure La sphère de centre I et de rayon R : tout point M de la sphère est à la distance R de I (dessin sans échelle)
<svg viewBox="0 0 340 240">
<title>Sphère de centre I et de rayon R : tout point M de la sphère vérifie IM = R</title>
<circle cx="170" cy="125" r="90" fill="#0f6e56" fill-opacity="0.12" stroke="#0f172a" stroke-width="2"/>
<path d="M80 125 A90 30 0 0 0 260 125" fill="none" stroke="#0f172a" stroke-width="1.6"/>
<path d="M80 125 A90 30 0 0 1 260 125" fill="none" stroke="#0f172a" stroke-width="1.6" stroke-dasharray="5 4"/>
<path d="M170 125 L243.7 73.4" fill="none" stroke="#b45309" stroke-width="2.6" stroke-linecap="round"/>
<circle cx="170" cy="125" r="4.5" fill="#0f172a"/>
<circle cx="243.7" cy="73.4" r="4.5" fill="#b45309"/>
<text x="158" y="143" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">I</text>
<text x="257.7" y="67.4" text-anchor="middle" font-size="13" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">M</text>
<text x="208.9" y="117.2" text-anchor="middle" font-size="15" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">R</text>
</svg>
:::

Sur la figure, le segment orange IM est de longueur R, et tous les points de la sphère se répartissent à cette même distance autour du centre I.

::: exemple Lire l'équation d'une sphère, et en construire une

1. Pour le radar, S : (x − 3)² + (y + 1)² + (z − 2)² = 9, soit x² + y² + z² − 6x + 2y − 4z + 5 = 0. La balise A(5, 0, 4) en fait partie : (5 − 3)² + (0 + 1)² + (4 − 2)² = 4 + 1 + 4 = 9 ✓.
2. Pour x² + y² + z² − 4x + 6y − 2z + d = 0, on complète les carrés : (x − 2)² + (y + 3)² + (z − 1)² = 14 − d. Le centre est I(2, −3, 1), quelle que soit la valeur de d.
3. Pour d = −2 : le second membre vaut 16, on a une sphère de rayon 4. Pour d = 14 : il vaut 0, l'ensemble est le point I. Pour d = 20 : il vaut −6, l'ensemble est vide, car une somme de carrés n'est jamais négative.
4. La sphère passant par O, A(2, 2, 0), B(2, 0, 2) et C(0, 2, 2) a une équation x² + y² + z² + ax + by + cz + d = 0. O donne d = 0 ; A donne 8 + 2a + 2b = 0, B donne 8 + 2a + 2c = 0 et C donne 8 + 2b + 2c = 0, d'où a = b = c = −2. Le centre est (1, 1, 1) et le rayon vaut √(1 + 1 + 1 − 0) = √3.

:::

::: piege
**Erreur : lire le centre et le rayon sans passer par la forme canonique.** L'erreur tente parce que (x − 1)² + (y + 3)² + (z − 2)² = 16 se lit presque à l'œil. On prend alors le centre (1, 3, 2), en oubliant que (y + 3)² signifie y − (−3), et le rayon 16 au lieu de 4. Le centre est (1, −3, 2), car on change le signe de chaque nombre, et le rayon est √16 = 4, car le second membre est R².
:::

::: propriete
L'ensemble des points M(x, y, z) tels que x² + y² + z² + ax + by + cz + d = 0 est une sphère, un point ou l'ensemble vide. Son centre est I(−a/2, −b/2, −c/2) et on pose K = a²/4 + b²/4 + c²/4 − d.
- Si K > 0, c'est la sphère de centre I et de rayon √K.
- Si K = 0, c'est le point I.
- Si K < 0, c'est l'ensemble vide.

Cas limite : une sphère passant par quatre points non coplanaires est unique, d'où les quatre équations à quatre inconnues a, b, c, d.
:::

::: verifie À toi : de quel ensemble s'agit-il ?
Quel est l'ensemble des points M(x, y, z) tels que x² + y² + z² + 2x − 4y + 6z + 14 = 0 ?

---

On complète les carrés : (x + 1)² + (y − 2)² + (z + 3)² = 1 + 4 + 9 − 14 = 0. Une somme de carrés nulle impose x = −1, y = 2, z = −3 : l'ensemble est réduit au point (−1, 2, −3), ce n'est pas une sphère.
:::

::: retenir
(x − x₀)² + (y − y₀)² + (z − z₀)² = R² est la sphère de centre I(x₀, y₀, z₀) et de rayon R ; x² + y² + z² + ax + by + cz + d = 0 est une sphère, un point ou le vide selon le signe de a²/4 + b²/4 + c²/4 − d.
:::

## 🔆 La sphère de diamètre [AB] et le plan médiateur

Un ballon sphérique est tendu entre deux piquets A et B placés aux extrémités d'un de ses diamètres.
Quels sont les points M du ballon, et que vaut l'angle AMB ?

::: definition
Soit A et B deux points distincts. L'ensemble des points M tels que MA⃗.MB⃗ = 0 est la **sphère de diamètre [AB]**, de centre le milieu I de [AB] et de rayon AB/2. Son équation est
$$ (x − x_A)(x − x_B) + (y − y_A)(y − y_B) + (z − z_A)(z − z_B) = 0 $$
L'ensemble des points M tels que MA = MB est le **plan médiateur** de [AB] : le plan passant par I de vecteur normal AB⃗.
:::

::: figure Dans un plan qui contient A, B et M, le point M de la sphère de diamètre [AB] voit [AB] sous un angle droit : MA⃗.MB⃗ = 0
<svg viewBox="0 0 340 240">
<title>Section de la sphère de diamètre [AB] par un plan qui contient A, B et M : l'angle en M est droit, donc MA.MB = 0</title>
<circle cx="170" cy="120" r="100" fill="#0f6e56" fill-opacity="0.12" stroke="#0f172a" stroke-width="2"/>
<path d="M70 120 L270 120" fill="none" stroke="#0f172a" stroke-width="2.2" stroke-linecap="round"/>
<path d="M216.9 31.7 L70 120" fill="none" stroke="#b45309" stroke-width="2.4" stroke-linecap="round"/>
<path d="M216.9 31.7 L270 120" fill="none" stroke="#b45309" stroke-width="2.4" stroke-linecap="round"/>
<path d="M216.9 31.7 L204.9 38.9 L212.2 50.9 L224.2 43.7 Z" fill="none" stroke="#b45309" stroke-width="1.6" stroke-linejoin="round"/>
<circle cx="70" cy="120" r="4" fill="#0f172a"/>
<circle cx="270" cy="120" r="4" fill="#0f172a"/>
<circle cx="170" cy="120" r="4" fill="#0f6e56"/>
<circle cx="216.9" cy="31.7" r="4.5" fill="#b45309"/>
<text x="58" y="126" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">A</text>
<text x="284" y="126" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">B</text>
<text x="170" y="140" text-anchor="middle" font-size="13" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">I</text>
<text x="228.9" y="23.7" text-anchor="middle" font-size="13" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">M</text>
</svg>
:::

Sur la figure, le carré en M marque l'angle droit AMB, et le centre I est au milieu du diamètre [AB].

::: exemple La sphère de diamètre [AB] et le plan médiateur

1. Pour A(1, −2, 3) et B(5, 2, −1), l'équation est (x − 1)(x − 5) + (y + 2)(y − 2) + (z − 3)(z + 1) = 0, soit x² + y² + z² − 6x − 2z − 2 = 0.
2. Le centre est le milieu I(3, 0, 1), et le rayon vérifie R² = 9 + 0 + 1 + 2 = 12. Contrôle : AB⃗(4, 4, −4), donc AB = 4√3 et AB/2 = 2√3 = √12 ✓.
3. Le plan médiateur passe par I et a pour vecteur normal AB⃗, ou (1, 1, −1) : (x − 3) + y − (z − 1) = 0, soit x + y − z − 2 = 0. Contrôle : le point (2, 0, 0) y est, et MA² = 1 + 4 + 9 = 14 = MB² = 9 + 4 + 1 ✓.

:::

::: piege
**Erreur : confondre MA⃗.MB⃗ = 0 avec MA = MB.** L'erreur tente parce que les deux conditions parlent de A et de B. Le centre I(3, 0, 1) vérifie IA = IB, il est donc sur le plan médiateur, mais IA⃗(−2, −2, 2) et IB⃗(2, 2, −2) donnent IA⃗.IB⃗ = −12 ≠ 0 : I n'est pas sur la sphère de diamètre [AB]. La première condition donne une sphère, la seconde un plan.
:::

::: propriete
- M est sur la sphère de diamètre [AB] si et seulement si MA⃗.MB⃗ = 0 ; on l'écrit en coordonnées sans calculer ni le centre ni le rayon.
- Le plan médiateur de [AB] est l'ensemble des M tels que MA = MB ; il est perpendiculaire à (AB) en son milieu.

Cas limite : M = A et M = B vérifient MA⃗.MB⃗ = 0, car l'un des deux vecteurs est nul : A et B sont bien sur la sphère.
:::

::: verifie À toi : la sphère de diamètre [AB]
Donner l'équation de la sphère de diamètre [AB] pour A(0, 1, −2) et B(2, −1, 0), puis son rayon.

---

L'équation est x(x − 2) + (y − 1)(y + 1) + (z + 2)z = 0, soit x² + y² + z² − 2x + 2z − 1 = 0. Le centre est (1, 0, −1) et R² = 1 + 0 + 1 + 1 = 3, donc R = √3. Contrôle : AB⃗(2, −2, 2) et AB/2 = √12/2 = √3 ✓.
:::

::: retenir
La sphère de diamètre [AB] est l'ensemble des M tels que MA⃗.MB⃗ = 0, le plan médiateur de [AB] celui des M tels que MA = MB.
:::

## 🍊 Une sphère coupée par un plan : cercle, point ou vide

On coupe une orange avec un couteau droit : la coupe est un disque, plus petit quand on s'éloigne du centre, et réduit à un point quand le couteau effleure l'orange.
Comment le prévoir avec des équations ?

::: definition
Soit S une sphère de centre I et de rayon R, P un plan, h la distance de I à P et H le projeté orthogonal de I sur P. L'intersection de S et de P est :
- vide si h > R ;
- réduite au point H si h = R : le plan est alors **tangent** à S en H ;
- le cercle de centre H et de rayon r = √(R² − h²) si h < R.
:::

::: figure Coupe de la sphère par un plan P à la distance h du centre I (ici R = 3 et h = 2) : le triangle IHM est rectangle en H, donc R² = h² + r²
<svg viewBox="0 0 340 250">
<title>Coupe de la sphère par un plan P à la distance h du centre : le cercle d'intersection a pour centre H et pour rayon r, avec R² = h² + r²</title>
<circle cx="170" cy="118" r="102" fill="#0f6e56" fill-opacity="0.12" stroke="#0f172a" stroke-width="2"/>
<path d="M48 186 L292 186" fill="none" stroke="#0f172a" stroke-width="2.2" stroke-linecap="round"/>
<path d="M94 186 L246 186" fill="none" stroke="#b45309" stroke-width="4" stroke-linecap="round"/>
<path d="M170 118 L170 186" fill="none" stroke="#94a3b8" stroke-width="2" stroke-linecap="round" stroke-dasharray="5 4"/>
<path d="M170 118 L246 186" fill="none" stroke="#b45309" stroke-width="2.2" stroke-linecap="round"/>
<path d="M170 186 L246 186" fill="none" stroke="#b45309" stroke-width="2.2" stroke-linecap="round"/>
<path d="M170 186 L182 186 L182 174 L170 174 Z" fill="none" stroke="#0f172a" stroke-width="1.4" stroke-linejoin="round"/>
<circle cx="170" cy="118" r="4.5" fill="#0f172a"/>
<circle cx="170" cy="186" r="4.5" fill="#b45309"/>
<circle cx="246" cy="186" r="4.5" fill="#b45309"/>
<circle cx="94" cy="186" r="4.5" fill="#b45309"/>
<text x="158" y="112" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">I</text>
<text x="158" y="204" text-anchor="middle" font-size="13" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">H</text>
<text x="260" y="180" text-anchor="middle" font-size="13" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">M</text>
<text x="158" y="156" text-anchor="middle" font-size="15" font-weight="700" fill="#475569" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">h</text>
<text x="208" y="206" text-anchor="middle" font-size="15" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">r</text>
<text x="214" y="146" text-anchor="middle" font-size="15" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">R</text>
<text x="288" y="178" text-anchor="middle" font-size="16" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">P</text>
</svg>
:::

Sur la figure, le segment IH de longueur h est perpendiculaire à P, et le théorème de Pythagore dans le triangle IHM donne r² = R² − h².

::: exemple Trois positions, un cercle, un plan tangent
Soit S : x² + y² + z² − 6x + 2y − 4z + 5 = 0, de centre I(3, −1, 2) et de rayon 3.

1. Pour P_d : 2x − 2y + z + d = 0, le numérateur en I vaut 6 + 2 + 2 + d = 10 + d, et ‖n⃗‖ = 3. Pour d = 2, h = 12/3 = 4 > 3 : l'intersection est vide. Pour d = −1, h = 9/3 = 3 = R : le plan est tangent. Pour d = −4, h = 6/3 = 2 < 3 : c'est un cercle de rayon √(9 − 4) = √5.
2. Pour le plan Q : x + y + z − 1 = 0, le numérateur en I vaut 3 − 1 + 2 − 1 = 3 et ‖n⃗‖ = √3, donc h = √3 < 3. Le centre du cercle est H = I + kn⃗ avec n⃗(1, 1, 1) : H(3 + k, −1 + k, 2 + k), et k = −1 donne H(2, −2, 1) ; on contrôle H ∈ Q : 2 − 2 + 1 − 1 = 0 ✓. Le rayon est r = √(9 − 3) = √6.
3. Le plan tangent à S en A(5, 0, 4) passe par A et a pour vecteur normal IA⃗(2, 1, 2) : 2(x − 5) + y + 2(z − 4) = 0, soit 2x + y + 2z − 18 = 0. Contrôle : sa distance à I vaut |6 − 1 + 4 − 18|/3 = 3 = R ✓.

:::

::: piege
**Erreur : croire que le cercle a pour centre I et pour rayon R.** L'erreur tente parce que le cercle « appartient » à la sphère. Pour P_{−4}, I n'est même pas dans le plan, puisque son numérateur vaut 6 ≠ 0 : le centre du cercle est le projeté H. Et son rayon est √5 ≈ 2,2, plus petit que R = 3, car le plan ne passe pas par le centre.
:::

::: propriete
- On compare h et R : c'est la distance du centre au plan qui décide.
- Le centre du cercle est H = I + kn⃗, où k est tel que H est dans P ; son rayon est r = √(R² − h²).
- Le plan tangent à S en A est le plan passant par A de vecteur normal IA⃗ ; il est à la distance R de I.

Cas limite : si le plan passe par le centre (h = 0), le cercle est de rayon R, c'est un grand cercle.
:::

::: verifie À toi : un plan et une sphère
La sphère S′ a pour centre O et pour rayon 4, et le plan P′ a pour équation 2x + 2y − z − 9 = 0. Quelle est leur intersection ?

---

La distance de O à P′ est |−9|/√(4 + 4 + 1) = 9/3 = 3, inférieure à 4 : l'intersection est un cercle de rayon √(16 − 9) = √7. Son centre est le projeté de O : H = k(2, 2, −1), et 9k − 9 = 0 donne k = 1, soit H(2, 2, −1) ; contrôle 4 + 4 + 1 − 9 = 0 ✓.
:::

::: retenir
Une sphère de rayon R et un plan à la distance h de son centre se coupent suivant le vide (h > R), un point (h = R, plan tangent) ou le cercle de centre H et de rayon √(R² − h²) (h < R).
:::

> 🏆 Les huit notions sont acquises : tu décris une droite par un paramètre, un plan par une équation et un vecteur normal, tu mesures les distances, tu tranches les positions relatives de plans et de droites, et tu domptes la sphère et ses coupes. Prochaine étape : les probabilités sur un ensemble fini.
