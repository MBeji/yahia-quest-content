# ⚔️ Produit scalaire, produit vectoriel et produit mixte dans l'espace — trois produits pour mesurer l'espace

> 💡 «Dans l'espace, on ne mesure pas avec une règle : on calcule un produit, et le produit donne l'angle, l'aire ou le volume.»

Ce chapitre arme l'espace de trois outils de calcul. Le produit scalaire détecte l'orthogonalité et mesure les distances, le produit vectoriel fabrique une normale et une aire, le produit mixte dit si quatre points sont coplanaires et mesure un volume. Huit notions, du produit scalaire aux sphères. Sauf mention contraire, l'espace est rapporté à un repère orthonormé direct (O, i⃗, j⃗, k⃗), et l'on sait déjà donner une représentation paramétrique d'une droite (chapitre précédent).

## 🎯 Le produit scalaire dans l'espace

Dans un cube ABCDEFGH d'arête 2, la diagonale [AG] traverse le solide et la diagonale [BD] de la face du dessous est posée sur le sol. Ces deux droites ne se coupent pas : on ne peut ni mesurer leur angle à la règle, ni le lire sur un dessin.
Comment savoir si (AG) et (BD) sont orthogonales, et comment calculer un produit comme AB⃗ . AG⃗ ?

::: definition
Soient A, B, C trois points, avec u⃗ = AB⃗ et v⃗ = AC⃗. Le **produit scalaire** de u⃗ et v⃗ est le réel noté **u⃗ . v⃗**. Il vaut 0 si l'un des deux vecteurs est nul, et sinon :
$$ u⃗ . v⃗ = AB × AC × cos(AB⃗, AC⃗) $$
Trois points sont toujours dans un même plan : le cosinus est celui de l'angle géométrique BAC, calculé dans le plan (ABC), comme en géométrie plane.
:::

::: figure Le cube ABCDEFGH d'arête 2 : la diagonale AG (en vert) et la diagonale BD de la face ABCD (en orange). D est caché derrière le solide, donc ses trois arêtes sont en pointillés.
<svg viewBox="0 0 250 232">
<title>Cube ABCDEFGH d'arête 2 : la diagonale AG en vert et la diagonale BD de la face ABCD en orange</title>
<polygon points="36.00,200.00 140.00,200.00 140.00,96.00 36.00,96.00" fill="#0f6e56" opacity="0.07"/><line x1="81.03" y1="174" x2="36" y2="200" stroke="#94a3b8" stroke-width="1.6" stroke-dasharray="5 4"/><line x1="81.03" y1="174" x2="185.03" y2="174" stroke="#94a3b8" stroke-width="1.6" stroke-dasharray="5 4"/><line x1="81.03" y1="174" x2="81.03" y2="70" stroke="#94a3b8" stroke-width="1.6" stroke-dasharray="5 4"/><line x1="36" y1="200" x2="140" y2="200" stroke="#0f172a" stroke-width="2"/><line x1="140" y1="200" x2="185.03" y2="174" stroke="#0f172a" stroke-width="2"/><line x1="36" y1="200" x2="36" y2="96" stroke="#0f172a" stroke-width="2"/><line x1="140" y1="200" x2="140" y2="96" stroke="#0f172a" stroke-width="2"/><line x1="185.03" y1="174" x2="185.03" y2="70" stroke="#0f172a" stroke-width="2"/><line x1="36" y1="96" x2="140" y2="96" stroke="#0f172a" stroke-width="2"/><line x1="140" y1="96" x2="185.03" y2="70" stroke="#0f172a" stroke-width="2"/><line x1="185.03" y1="70" x2="81.03" y2="70" stroke="#0f172a" stroke-width="2"/><line x1="81.03" y1="70" x2="36" y2="96" stroke="#0f172a" stroke-width="2"/><line x1="36" y1="200" x2="185.03" y2="70" stroke="#0f6e56" stroke-width="2.6"/>
<polygon points="185.03,70 180.78,80.34 174.21,72.81" fill="#0f6e56"/><line x1="140" y1="200" x2="81.03" y2="174" stroke="#b45309" stroke-width="2.6"/>
<polygon points="81.03,174 92.2,173.46 88.17,182.61" fill="#b45309"/><circle cx="36" cy="200" r="3.5" fill="#0f172a"/><circle cx="140" cy="200" r="3.5" fill="#0f172a"/><circle cx="185.03" cy="174" r="3.5" fill="#0f172a"/><circle cx="81.03" cy="174" r="3.5" fill="#94a3b8"/><circle cx="36" cy="96" r="3.5" fill="#0f172a"/><circle cx="140" cy="96" r="3.5" fill="#0f172a"/><circle cx="185.03" cy="70" r="3.5" fill="#0f172a"/><circle cx="81.03" cy="70" r="3.5" fill="#0f172a"/><text x="24" y="216" text-anchor="middle" fill="#0f172a" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">A</text><text x="150" y="218" text-anchor="middle" fill="#0f172a" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">B</text><text x="199.03" y="179" text-anchor="middle" fill="#0f172a" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">C</text><text x="69.03" y="168" text-anchor="middle" fill="#94a3b8" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">D</text><text x="24" y="94" text-anchor="middle" fill="#0f172a" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">E</text><text x="128" y="88" text-anchor="middle" fill="#0f172a" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">F</text><text x="199.03" y="64" text-anchor="middle" fill="#0f172a" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">G</text><text x="77.03" y="60" text-anchor="middle" fill="#0f172a" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">H</text><text x="84.52" y="131" text-anchor="middle" fill="#0f6e56" font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">AG⃗</text><text x="114.52" y="207" text-anchor="middle" fill="#b45309" font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">BD⃗</text>
</svg>
:::

Les deux vecteurs de la question sont tracés sur la figure : AG⃗ en vert, BD⃗ en orange. Le triangle ABG, rectangle en B, donne l'angle de AB⃗ et AG⃗.

::: exemple Calculer AB⃗ . AG⃗ dans le cube d'arête 2

1. Dans le plan (ACG), le triangle ACG est rectangle en C (l'arête [CG] est perpendiculaire à la face ABCD), avec AC = 2√2 (diagonale d'un carré de côté 2) et CG = 2. Donc AG² = 8 + 4 = 12 et AG = 2√3.
2. Le triangle ABG est rectangle en B (l'arête [AB] est perpendiculaire à la face BCGF), donc cos(AB⃗, AG⃗) = AB/AG = 2/(2√3) = 1/√3.
3. On applique la définition : AB⃗ . AG⃗ = 2 × 2√3 × 1/√3 = 4. Contrôle avec une autre diagonale : AB⃗ . AC⃗ = 2 × 2√2 × cos 45° = 4√2 × √2/2 = 4 ✓.

:::

::: exemple Le même calcul en coordonnées, et la réponse à la question

On choisit le repère (A ; i⃗, j⃗, k⃗) avec i⃗ = AB⃗/2, j⃗ = AD⃗/2, k⃗ = AE⃗/2 : il est orthonormé. Alors B(2 ; 0 ; 0), D(0 ; 2 ; 0), G(2 ; 2 ; 2).

1. On a AB⃗ = 2i⃗ et AG⃗ = 2i⃗ + 2j⃗ + 2k⃗. En développant, AB⃗ . AG⃗ = 4 i⃗.i⃗ + 4 i⃗.j⃗ + 4 i⃗.k⃗ ; comme i⃗.i⃗ = 1 (norme 1) et i⃗.j⃗ = i⃗.k⃗ = 0 (orthogonaux), il reste 4 : on retrouve le résultat précédent ✓.
2. Pour les diagonales, BD⃗ = D − B a pour coordonnées (−2 ; 2 ; 0) et AG⃗ (2 ; 2 ; 2). Le même développement donne BD⃗ . AG⃗ = −4 + 4 + 0 = 0.
3. Un produit scalaire nul signifie que les vecteurs sont orthogonaux : les droites (AG) et (BD) sont orthogonales, bien qu'elles ne se coupent pas.

:::

::: piege
**Erreur : conclure de u⃗ . v⃗ = 0 que l'un des deux vecteurs est nul.** L'erreur tente parce qu'un produit de nombres ne s'annule que si un facteur s'annule. Ici AB⃗ . AD⃗ = 2 × 2 × cos 90° = 0, alors que AB⃗ et AD⃗ sont non nuls : un produit scalaire nul dit « orthogonaux », pas « nul ».
:::

::: propriete
Pour tous vecteurs u⃗, v⃗, w⃗ et tout réel α : u⃗ . v⃗ = v⃗ . u⃗ ; (αu⃗) . v⃗ = α(u⃗ . v⃗) ; u⃗ . (v⃗ + w⃗) = u⃗ . v⃗ + u⃗ . w⃗.
Dans une base orthonormée (i⃗, j⃗, k⃗), si u⃗(x ; y ; z) et v⃗(x′ ; y′ ; z′) :
$$ u⃗ . v⃗ = xx′ + yy′ + zz′ $$
$$ ‖u⃗‖ = √(x² + y² + z²) $$
Deux vecteurs u⃗ et v⃗ sont **orthogonaux** si et seulement si u⃗ . v⃗ = 0. Cas limite : le vecteur nul est orthogonal à tout vecteur, et u⃗ . u⃗ = ‖u⃗‖².
:::

::: verifie À toi : l'angle FAH
Dans le même cube d'arête 2, calculer AF⃗ . AH⃗ en coordonnées, puis le cosinus de l'angle FAH. Que peut-on dire du triangle AFH ?

---

On a F(2 ; 0 ; 2) et H(0 ; 2 ; 2), donc AF⃗ . AH⃗ = 0 + 0 + 4 = 4. Les normes valent ‖AF⃗‖ = ‖AH⃗‖ = √8 = 2√2, et la définition donne cos(FAH) = 4/(2√2 × 2√2) = 4/8 = 1/2, soit un angle de 60°. Comme FH = ‖(−2 ; 2 ; 0)‖ = 2√2 vaut aussi AF et AH, le triangle AFH est équilatéral.
:::

::: retenir
Le produit scalaire est un réel : en base orthonormée, u⃗ . v⃗ = xx′ + yy′ + zz′, ‖u⃗‖ = √(x² + y² + z²), et u⃗ . v⃗ = 0 si et seulement si u⃗ et v⃗ sont orthogonaux.
:::

## 🧭 Plans : vecteur normal et équation cartésienne

Une plaque de verre plane doit être fixée au point A(2 ; −1 ; 1), perpendiculairement à un tube de direction N⃗(1 ; 2 ; −2). Un point M(x ; y ; z) de l'espace est-il sur la plaque ?
Comment traduire « la plaque est perpendiculaire au tube » en une condition sur les coordonnées de M ?

::: definition
Un vecteur N⃗ non nul est **normal** à un plan P lorsqu'il est orthogonal à toutes les directions de P. Le plan passant par A et de vecteur normal N⃗ est l'ensemble des points M tels que :
$$ AM⃗ . N⃗ = 0 $$
:::

::: figure Le plan P passant par A, un vecteur normal N⃗ (en orange) et un point M de P : AM⃗ (en vert) reste orthogonal à N⃗, ce que marque le petit carré en A.
<svg viewBox="0 0 285 232">
<title>Le plan P passant par A, son vecteur normal N perpendiculaire à P, et un point M de P : AM est orthogonal à N</title>
<polygon points="15.67,207.50 205.67,207.50 266.29,172.50 76.29,172.50" fill="#0f6e56" opacity="0.14"/><polygon points="15.67,207.5 205.67,207.5 266.29,172.5 76.29,172.5" fill="none" stroke="#0f172a" stroke-width="1.6"/><line x1="105.16" y1="196.25" x2="105.16" y2="101.25" stroke="#b45309" stroke-width="2.6"/>
<polygon points="105.16,101.25 110.16,111.25 100.16,111.25" fill="#b45309"/><line x1="105.16" y1="196.25" x2="216.14" y2="181.25" stroke="#0f6e56" stroke-width="2.6"/>
<polygon points="216.14,181.25 206.9,187.54 205.56,177.63" fill="#0f6e56"/><polyline points="118.0,194.5 118.0,182.5 105.2,184.3" fill="none" stroke="#0f172a" stroke-width="1.4"/><circle cx="105.16" cy="196.25" r="3.5" fill="#0f172a"/><circle cx="216.14" cy="181.25" r="3.5" fill="#0f172a"/><text x="93.16" y="212.25" text-anchor="middle" fill="#0f172a" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">A</text><text x="228.14" y="185.25" text-anchor="middle" fill="#0f6e56" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">M</text><text x="121.16" y="105.25" text-anchor="middle" fill="#b45309" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">N⃗</text><text x="258.29" y="164.5" text-anchor="middle" fill="#0f172a" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">P</text><text x="156.65" y="208.75" text-anchor="middle" fill="#0f6e56" font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">AM⃗</text>
</svg>
:::

Sur la figure, tous les vecteurs AM⃗ tracés dans le plan sont orthogonaux au même vecteur N⃗ : c'est cette condition qui définit le plan.

::: exemple Équation du plan passant par A(2 ; −1 ; 1) de vecteur normal N⃗(1 ; 2 ; −2)

1. Un point M(x ; y ; z) est dans le plan si et seulement si AM⃗ . N⃗ = 0, par définition.
2. Les coordonnées de AM⃗ sont celles de M moins celles de A : (x − 2 ; y + 1 ; z − 1).
3. Le repère est orthonormé, donc le produit scalaire se calcule composante par composante : (x − 2) + 2(y + 1) − 2(z − 1) = 0.
4. On développe : x + 2y − 2z + 2 = 0. Contrôle : A donne 2 − 2 − 2 + 2 = 0 ✓, et B(0 ; −1 ; 0) donne 0 − 2 − 0 + 2 = 0 avec AB⃗(−2 ; 0 ; −1) orthogonal à N⃗ : −2 + 0 + 2 = 0 ✓.

:::

::: exemple Le plan médiateur de [CD]

Soit C(1 ; −1 ; 2) et D(3 ; 1 ; −2). Le plan médiateur de [CD] est l'ensemble des points équidistants de C et D : c'est le plan qui passe par le milieu I de [CD] et qui est normal à CD⃗.

1. Le milieu est I(2 ; 0 ; 0), et CD⃗ a pour coordonnées (2 ; 2 ; −4).
2. Tout multiple non nul d'un vecteur normal est encore normal : on prend N⃗(1 ; 1 ; −2), plus simple.
3. La condition IM⃗ . N⃗ = 0 donne (x − 2) + y − 2z = 0, soit x + y − 2z − 2 = 0. Contrôle : le point M(0 ; 0 ; −1) vérifie 0 + 0 + 2 − 2 = 0 et MC² = 1 + 1 + 9 = 11 = MD² = 9 + 1 + 1 ✓.

:::

::: piege
**Erreur : prendre (a ; b ; c) pour un vecteur contenu dans le plan ax + by + cz + d = 0.** L'erreur tente parce que ces trois nombres se lisent dans l'équation. Mais (a ; b ; c) est un vecteur normal, perpendiculaire au plan. Dans x + y + z − 3 = 0, les points A(1 ; 1 ; 1) et B(3 ; 0 ; 0) sont dans le plan, et AB⃗(2 ; −1 ; −1) est orthogonal à (1 ; 1 ; 1) : 2 − 1 − 1 = 0.
:::

::: propriete
Le plan P d'équation ax + by + cz + d = 0, avec (a ; b ; c) ≠ (0 ; 0 ; 0), admet N⃗(a ; b ; c) pour vecteur normal. Réciproquement, le plan passant par A(xA ; yA ; zA) de vecteur normal N⃗(a ; b ; c) a pour équation a(x − xA) + b(y − yA) + c(z − zA) = 0.
Positions relatives, avec des vecteurs normaux N⃗ et N′⃗ de plans P et P′, et des vecteurs directeurs u⃗ et v⃗ de droites D et D′ :
P ∥ P′ si et seulement si N⃗ et N′⃗ sont colinéaires ; P ⊥ P′ si et seulement si N⃗ . N′⃗ = 0 ;
D ∥ P si et seulement si u⃗ . N⃗ = 0 ; D ⊥ P si et seulement si u⃗ et N⃗ sont colinéaires ;
D ⊥ D′ si et seulement si u⃗ . v⃗ = 0 ; D ∥ D′ si et seulement si u⃗ et v⃗ sont colinéaires.
Cas limite : « parallèle » est pris au sens large — deux plans parallèles peuvent être confondus, et une droite parallèle à un plan peut être contenue dans ce plan.
:::

::: exemple Lire des positions relatives

Soit P : 2x − y + 3z − 1 = 0, P′ : −4x + 2y − 6z + 5 = 0, R : x − y + z + 1 = 0 et R′ : 2x + y − z − 3 = 0.

1. Pour P et P′, N⃗(2 ; −1 ; 3) et N′⃗(−4 ; 2 ; −6) = −2N⃗ sont colinéaires : les plans sont parallèles. Le point (0 ; −1 ; 0) est dans P (1 − 1 = 0) mais pas dans P′ (−2 + 5 = 3), donc ils sont strictement parallèles.
2. Pour R et R′, N⃗ . N′⃗ = 2 − 1 − 1 = 0 : les plans sont perpendiculaires.
3. La droite D passant par A(1 ; 1 ; 0) de vecteur directeur u⃗(1 ; 2 ; 1) vérifie u⃗ . N⃗ = 1 − 2 + 1 = 0 avec N⃗(1 ; −1 ; 1) normal à R : D est parallèle à R. Comme A donne 1 − 1 + 0 + 1 = 1 ≠ 0, elle n'est pas contenue dans R.

:::

::: verifie À toi : le plan perpendiculaire à une droite
Écrire une équation du plan passant par B(2 ; 0 ; 1) et perpendiculaire à la droite de vecteur directeur v⃗(1 ; −2 ; 1).

---

La droite est perpendiculaire au plan si et seulement si v⃗ est colinéaire à un vecteur normal : on prend N⃗ = v⃗(1 ; −2 ; 1). Le plan a donc une équation x − 2y + z + d = 0, et B donne 2 − 0 + 1 + d = 0, soit d = −3 : x − 2y + z − 3 = 0.
:::

::: retenir
Un plan d'équation ax + by + cz + d = 0 a pour vecteur normal (a ; b ; c) : le parallélisme se lit sur des vecteurs normaux colinéaires, la perpendicularité sur un produit scalaire nul.
:::

## 📏 Distance d'un point à un plan et à une droite

Un drone est immobile au point A(1 ; −2 ; 4) au-dessus d'une plaque plane P : 2x + 2y − z + 3 = 0 (unité : le mètre). Quelle est la plus courte distance entre le drone et la plaque, et quel est le point de la plaque le plus proche ?
Faut-il tester tous les points de la plaque, ou une seule direction suffit-elle ?

::: definition
Le **projeté orthogonal** de A sur un plan P est le point H de P tel que AH⃗ soit normal à P. Sur une droite D de vecteur directeur u⃗, c'est le point H de D tel que AH⃗ . u⃗ = 0. La **distance** de A au plan (ou à la droite) est la longueur AH, notée d(A, P) (ou d(A, D)).
:::

::: figure Le point A et son projeté orthogonal H sur le plan P : AH (en orange) est perpendiculaire à P. Pour un autre point M de P, le triangle AHM est rectangle en H, donc AM est plus long que AH.
<svg viewBox="0 0 295 244">
<title>Le point A, son projeté orthogonal H sur le plan P, et un autre point M de P : AH est plus court que AM</title>
<polygon points="15.67,217.50 215.67,217.50 280.62,180.00 80.62,180.00" fill="#0f6e56" opacity="0.14"/><polygon points="15.67,217.5 215.67,217.5 280.62,180 80.62,180" fill="none" stroke="#0f172a" stroke-width="1.6"/><line x1="131.65" y1="82.5" x2="231.14" y2="191.25" stroke="#94a3b8" stroke-width="1.6" stroke-dasharray="5 4"/><line x1="131.65" y1="202.5" x2="231.14" y2="191.25" stroke="#94a3b8" stroke-width="1.6" stroke-dasharray="5 4"/><line x1="131.65" y1="82.5" x2="131.65" y2="202.5" stroke="#b45309" stroke-width="3"/><polyline points="131.7,190.5 144.7,189.0 144.7,201.0" fill="none" stroke="#0f172a" stroke-width="1.4"/><circle cx="131.65" cy="82.5" r="3.5" fill="#0f172a"/><circle cx="131.65" cy="202.5" r="3.5" fill="#b45309"/><circle cx="231.14" cy="191.25" r="3.5" fill="#94a3b8"/><text x="119.65" y="86.5" text-anchor="middle" fill="#0f172a" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">A</text><text x="115.65" y="208.5" text-anchor="middle" fill="#b45309" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">H</text><text x="243.14" y="196.25" text-anchor="middle" fill="#94a3b8" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">M</text><text x="149.65" y="142.5" text-anchor="start" fill="#b45309" font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">AH</text><text x="272.62" y="172" text-anchor="middle" fill="#0f172a" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">P</text>
</svg>
:::

Sur la figure, AM est l'hypoténuse du triangle AHM rectangle en H : AM > AH pour tout point M ≠ H de P, donc AH est bien la plus courte des distances.

::: exemple Le projeté du drone sur la plaque

Pour P : 2x + 2y − z + 3 = 0 et A(1 ; −2 ; 4).

1. Le vecteur N⃗(2 ; 2 ; −1) est normal à P et AH⃗ lui est colinéaire : H a pour coordonnées (1 + 2α ; −2 + 2α ; 4 − α), avec α réel.
2. H est dans P : 2(1 + 2α) + 2(−2 + 2α) − (4 − α) + 3 = 0, soit 9α − 3 = 0 et α = 1/3.
3. Alors H(5/3 ; −4/3 ; 11/3) et AH⃗ = (1/3)N⃗, donc AH = (1/3) × ‖N⃗‖ = (1/3) × 3 = 1. Contrôle : 10/3 − 8/3 − 11/3 + 3 = 0, donc H est bien dans P ✓. Le drone est à 1 m de la plaque.

:::

::: piege
**Erreur : prendre pour distance la longueur AM d'un point M « commode » du plan.** L'erreur tente parce que M(0 ; 0 ; 3), où P rencontre l'axe des cotes, se trouve sans calcul. Mais AM = ‖(−1 ; 2 ; −1)‖ = √6 ≈ 2,45, plus long que AH = 1 : seule la perpendiculaire à P donne la plus courte distance.
:::

::: propriete
L'espace est rapporté à un repère orthonormé, P est le plan d'équation ax + by + cz + d = 0 et A(xA ; yA ; zA) est un point. Alors :
$$ d(A, P) = |a xA + b yA + c zA + d| / √(a² + b² + c²) $$
Cas limite : d(A, P) = 0 si et seulement si A appartient à P. Le numérateur porte une valeur absolue : sans elle, le quotient serait négatif pour les points situés de l'autre côté du plan.
:::

::: exemple La formule appliquée

Distance de A(1 ; 2 ; −1) au plan P′ : x − 2y + 2z − 6 = 0.

1. Le numérateur vaut |1 − 4 − 2 − 6| = |−11| = 11.
2. Le dénominateur vaut √(1 + 4 + 4) = 3.
3. Donc d(A, P′) = 11/3. Contrôle : le signe négatif de −11 dit seulement de quel côté de P′ se trouve A, la distance reste positive.

:::

::: exemple Distance d'un point à une droite par le projeté

Soit D la droite passant par B(1 ; −1 ; 0) de vecteur directeur u⃗(1 ; 2 ; 2) et M(4 ; −1 ; 3).

1. Un point de D s'écrit H(1 + α ; −1 + 2α ; 2α), avec α réel.
2. H est le projeté de M sur D si et seulement si MH⃗ . u⃗ = 0. Or MH⃗(α − 3 ; 2α ; 2α − 3), d'où (α − 3) + 4α + 2(2α − 3) = 9α − 9 = 0 et α = 1.
3. Alors H(2 ; 1 ; 2) et MH⃗(−2 ; 2 ; −1), donc d(M, D) = √(4 + 4 + 1) = 3. Contrôle : MH⃗ . u⃗ = −2 + 4 − 2 = 0 ✓.

:::

::: verifie À toi : une distance à un plan
Calculer la distance du point A(3 ; 3 ; 0) au plan 2x + 3y + 6z − 1 = 0.

---

Le numérateur vaut |2 × 3 + 3 × 3 + 6 × 0 − 1| = |14| = 14 et le dénominateur √(4 + 9 + 36) = √49 = 7. Donc d(A, P) = 14/7 = 2.
:::

::: retenir
d(A, P) = |a xA + b yA + c zA + d| / √(a² + b² + c²) ; pour une droite, on cherche le point H de D tel que AH⃗ . u⃗ = 0 et l'on mesure AH.
:::

## ✖️ Le produit vectoriel

Un toit plat est porté par deux poutres de directions u⃗(1 ; 2 ; 0) et v⃗(0 ; 1 ; 3), et une cheminée doit s'élever perpendiculairement à la toiture. Un vecteur n⃗(x ; y ; z) orthogonal aux deux poutres vérifie x + 2y = 0 et y + 3z = 0, donc n⃗ = z(6 ; −3 ; 1) : il y en a une infinité, tous colinéaires.
Comment choisir l'un d'eux, avec sa direction, son sens et sa longueur imposés, sans résoudre un système à chaque fois ?

::: definition
Soient u⃗ = AB⃗ et v⃗ = AC⃗, dans l'espace orienté. Le **produit vectoriel** de u⃗ et v⃗ est le vecteur noté **u⃗ ∧ v⃗**. Si u⃗ et v⃗ sont colinéaires, il vaut 0⃗. Sinon c'est l'unique vecteur w⃗ tel que :

1. w⃗ est normal au plan (ABC) ;
2. (u⃗, v⃗, w⃗) est une base directe (règle de la main droite : u⃗ le pouce, v⃗ l'index, w⃗ le majeur) ;
3. ‖w⃗‖ = ‖u⃗‖ × ‖v⃗‖ × |sin(AB⃗, AC⃗)|.

:::

::: figure Le vecteur u⃗ ∧ v⃗ (en orange) se dresse perpendiculairement au plan de u⃗ et v⃗, ce que marquent les deux petits carrés en O ; le trièdre (u⃗, v⃗, u⃗ ∧ v⃗) est direct.
<svg viewBox="0 0 250 240">
<title>Les vecteurs u et v engendrent un parallélogramme ; leur produit vectoriel se dresse perpendiculairement à ce parallélogramme</title>
<polygon points="50.00,215.00 142.00,215.00 199.48,197.75 107.48,197.75" fill="#0f6e56" opacity="0.16"/><polygon points="50,215 142,215 199.48,197.75 107.48,197.75" fill="none" stroke="#0f172a" stroke-width="1.3"/><line x1="50" y1="215" x2="50" y2="77" stroke="#b45309" stroke-width="2.6"/>
<polygon points="50,77 55,87 45,87" fill="#b45309"/><line x1="50" y1="215" x2="142" y2="215" stroke="#0f172a" stroke-width="2.6"/>
<polygon points="142,215 132,220 132,210" fill="#0f172a"/><line x1="50" y1="215" x2="107.48" y2="197.75" stroke="#0f172a" stroke-width="2.6"/>
<polygon points="107.48,197.75 99.34,205.41 96.46,195.84" fill="#0f172a"/><polyline points="61.5,215.0 61.5,203.5 50.0,203.5" fill="none" stroke="#0f172a" stroke-width="1.4"/><polyline points="58.9,212.3 58.9,200.8 50.0,203.5" fill="none" stroke="#0f172a" stroke-width="1.4"/><circle cx="50" cy="215" r="3.5" fill="#0f172a"/><text x="38" y="231" text-anchor="middle" fill="#0f172a" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">O</text><text x="146" y="233" text-anchor="middle" fill="#0f172a" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">u⃗</text><text x="97.48" y="191.75" text-anchor="middle" fill="#0f172a" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">v⃗</text><text x="56" y="69" text-anchor="start" fill="#b45309" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">u⃗∧v⃗</text>
</svg>
:::

Sur la figure, la direction de u⃗ ∧ v⃗ est celle de la cheminée de l'énoncé : normale au plan des deux poutres.

::: exemple Le produit vectoriel de u⃗(1 ; 2 ; 0) et v⃗(0 ; 1 ; 3)

1. u⃗ et v⃗ ne sont pas colinéaires : aucune valeur de α ne donne (1 ; 2 ; 0) = α(0 ; 1 ; 3), car la première coordonnée de v⃗ est nulle et pas celle de u⃗. Le produit n'est donc pas nul.
2. En base orthonormée directe, avec u⃗(x ; y ; z) = (1 ; 2 ; 0) et v⃗(x′ ; y′ ; z′) = (0 ; 1 ; 3), les coordonnées de u⃗ ∧ v⃗ sont (yz′ − zy′ ; zx′ − xz′ ; xy′ − yx′).
3. Première coordonnée : yz′ − zy′ = 2 × 3 − 0 × 1 = 6. Deuxième : zx′ − xz′ = 0 × 0 − 1 × 3 = −3. Troisième : xy′ − yx′ = 1 × 1 − 2 × 0 = 1.
4. Donc u⃗ ∧ v⃗ = (6 ; −3 ; 1), le vecteur de l'énoncé pour z = 1. Contrôle : (6 ; −3 ; 1) . u⃗ = 6 − 6 + 0 = 0 ✓ et (6 ; −3 ; 1) . v⃗ = 0 − 3 + 3 = 0 ✓.

:::

::: exemple Simplifier un produit vectoriel

Simplifier (u⃗ + 2v⃗) ∧ (3u⃗ − v⃗), pour deux vecteurs u⃗ et v⃗ non colinéaires.

1. On développe comme un produit ordinaire, car le produit vectoriel se distribue sur la somme : 3 u⃗∧u⃗ − u⃗∧v⃗ + 6 v⃗∧u⃗ − 2 v⃗∧v⃗.
2. Un vecteur est colinéaire à lui-même, donc u⃗∧u⃗ = 0⃗ et v⃗∧v⃗ = 0⃗.
3. Échanger les facteurs change le signe : v⃗∧u⃗ = −u⃗∧v⃗. Il reste −u⃗∧v⃗ − 6 u⃗∧v⃗ = −7 u⃗∧v⃗. Contrôle avec u⃗(1 ; 2 ; 0) et v⃗(0 ; 1 ; 3) : (1 ; 4 ; 6) ∧ (3 ; 5 ; −3) = (−42 ; 21 ; −7) = −7 × (6 ; −3 ; 1) ✓.

:::

::: piege
**Erreur : écrire v⃗ ∧ u⃗ = u⃗ ∧ v⃗, comme pour le produit scalaire.** L'erreur tente parce que le produit de deux nombres et le produit scalaire sont commutatifs. Mais échanger u⃗ et v⃗ renverse le sens de la base : avec u⃗(1 ; 2 ; 0) et v⃗(0 ; 1 ; 3), on trouve v⃗ ∧ u⃗ = (−6 ; 3 ; −1), l'opposé de u⃗ ∧ v⃗.
:::

::: propriete
Pour tous vecteurs u⃗, v⃗, w⃗ et tout réel α :
u⃗ ∧ v⃗ = −(v⃗ ∧ u⃗) ; (αu⃗) ∧ v⃗ = u⃗ ∧ (αv⃗) = α(u⃗ ∧ v⃗) ; (u⃗ + v⃗) ∧ w⃗ = u⃗ ∧ w⃗ + v⃗ ∧ w⃗ ;
u⃗ ∧ v⃗ = 0⃗ si et seulement si u⃗ et v⃗ sont colinéaires.
Dans une base orthonormée directe, si u⃗(x ; y ; z) et v⃗(x′ ; y′ ; z′) :
$$ u⃗ ∧ v⃗ = (yz′ − zy′ ; zx′ − xz′ ; xy′ − yx′) $$
Cas limite : u⃗ ∧ u⃗ = 0⃗. Le résultat est un vecteur, alors que u⃗ . v⃗ est un réel : « u⃗ ∧ v⃗ = 0⃗ » s'écrit avec la flèche, « u⃗ . v⃗ = 0 » sans.
:::

::: verifie À toi : un produit vectoriel en coordonnées
Calculer u⃗ ∧ v⃗ pour u⃗(2 ; −1 ; 1) et v⃗(1 ; 3 ; −1), puis contrôler le résultat.

---

Avec (yz′ − zy′ ; zx′ − xz′ ; xy′ − yx′) : première coordonnée (−1)(−1) − 1 × 3 = −2, deuxième 1 × 1 − 2 × (−1) = 3, troisième 2 × 3 − (−1) × 1 = 7, d'où (−2 ; 3 ; 7). Contrôle : (−2 ; 3 ; 7) . u⃗ = −4 − 3 + 7 = 0 et (−2 ; 3 ; 7) . v⃗ = −2 + 9 − 7 = 0 ✓.
:::

::: retenir
u⃗ ∧ v⃗ est un vecteur normal au plan de u⃗ et v⃗, nul si et seulement si u⃗ et v⃗ sont colinéaires, qui change de signe quand on échange les facteurs ; en base orthonormée directe, u⃗ ∧ v⃗ = (yz′ − zy′ ; zx′ − xz′ ; xy′ − yx′).
:::

## 📐 Le produit vectoriel au travail : plan, aire, angle, distance

Un panneau triangulaire a pour sommets A(2 ; 1 ; 0), B(3 ; 3 ; 1) et C(0 ; 2 ; 3). Pour le fixer et le peindre, il faut l'équation du plan qui le porte et son aire.
Un seul produit vectoriel peut-il fournir les deux ?

::: figure Le parallélogramme ABDC a pour base AB et pour hauteur h = CH ; sa diagonale BC le partage en deux triangles égaux, dont le triangle ABC (en orange).
<svg viewBox="0 0 290 205">
<title>Le parallélogramme ABDC, de base AB et de hauteur h = CH, est partagé par la diagonale BC en deux triangles égaux, dont ABC</title>
<polygon points="40.00,175.00 190.00,175.00 255.00,70.00 105.00,70.00" fill="#0f6e56" opacity="0.12"/><polygon points="40.00,175.00 190.00,175.00 105.00,70.00" fill="#b45309" opacity="0.2"/><polygon points="40,175 190,175 255,70 105,70" fill="none" stroke="#0f172a" stroke-width="1.8"/><line x1="190" y1="175" x2="105" y2="70" stroke="#0f172a" stroke-width="1.8"/><line x1="105" y1="70" x2="105" y2="175" stroke="#b45309" stroke-width="2.6" stroke-dasharray="5 4"/><polyline points="105,163 117,163 117,175" fill="none" stroke="#0f172a" stroke-width="1.3"/><circle cx="40" cy="175" r="3.5" fill="#0f172a"/><circle cx="190" cy="175" r="3.5" fill="#0f172a"/><circle cx="105" cy="70" r="3.5" fill="#0f172a"/><circle cx="255" cy="70" r="3.5" fill="#0f172a"/><circle cx="105" cy="175" r="3.5" fill="#b45309"/><text x="30" y="193" text-anchor="middle" fill="#0f172a" font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">A</text><text x="198" y="193" text-anchor="middle" fill="#0f172a" font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">B</text><text x="101" y="60" text-anchor="middle" fill="#0f172a" font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">C</text><text x="263" y="62" text-anchor="middle" fill="#0f172a" font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">D</text><text x="109" y="193" text-anchor="middle" fill="#b45309" font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">H</text><text x="123" y="128" text-anchor="middle" fill="#b45309" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">h</text>
</svg>
:::

Sur la figure, le parallélogramme ABDC est construit sur AB⃗ et AC⃗ : son aire est base × hauteur = AB × h. Comme h = AC × sin(BAC), cette aire vaut AB × AC × sin(BAC), c'est-à-dire ‖AB⃗ ∧ AC⃗‖ d'après la définition.

::: exemple Plan, aire et angle du panneau ABC

1. AB⃗ a pour coordonnées (1 ; 2 ; 1) et AC⃗ (−2 ; 1 ; 3). Alors AB⃗ ∧ AC⃗ = (2 × 3 − 1 × 1 ; 1 × (−2) − 1 × 3 ; 1 × 1 − 2 × (−2)) = (5 ; −5 ; 5). Ce vecteur est non nul : A, B, C ne sont pas alignés.
2. Il est normal au plan (ABC) par définition ; (1 ; −1 ; 1) l'est aussi, et le plan a une équation x − y + z + d = 0. Comme A donne 2 − 1 + 0 + d = 0, on a d = −1 : x − y + z − 1 = 0. Contrôle : B donne 3 − 3 + 1 − 1 = 0 et C donne 0 − 2 + 3 − 1 = 0 ✓.
3. Le parallélogramme ABDC a pour aire ‖AB⃗ ∧ AC⃗‖ = √(25 + 25 + 25) = 5√3. Le triangle ABC en est la moitié : 5√3/2 ≈ 4,33.
4. Pour l'angle A, ‖AB⃗‖ = √6 et ‖AC⃗‖ = √14. On a cos A = AB⃗ . AC⃗/(‖AB⃗‖ × ‖AC⃗‖) = 3/√84 et |sin A| = 5√3/√84. Contrôle : cos² + sin² = 9/84 + 75/84 = 1 ✓.

:::

::: piege
**Erreur : donner ‖AB⃗ ∧ AC⃗‖ comme aire du triangle ABC.** L'erreur tente parce que la norme du produit vectoriel est la quantité qu'on vient de calculer. Mais elle mesure le parallélogramme ABDC : le triangle ABC n'en est que la moitié, soit 5√3/2 et non 5√3.
:::

::: propriete
Soient u⃗ et v⃗ deux vecteurs non nuls et θ une mesure de l'angle orienté (u⃗, v⃗). Alors :
|sin θ| = ‖u⃗ ∧ v⃗‖/(‖u⃗‖ × ‖v⃗‖) et cos θ = u⃗ . v⃗/(‖u⃗‖ × ‖v⃗‖).
Si u⃗ et v⃗ dirigent un plan P sans être colinéaires, alors u⃗ ∧ v⃗ est un vecteur normal à P.
Trois points A, B, C sont alignés si et seulement si AB⃗ ∧ AC⃗ = 0⃗ ; sinon, l'aire du triangle ABC vaut (1/2)‖AB⃗ ∧ AC⃗‖.
La distance d'un point A à la droite Δ passant par B de vecteur directeur u⃗ vaut ‖AB⃗ ∧ u⃗‖/‖u⃗‖.
Cas limite : si AB⃗ ∧ u⃗ = 0⃗, la distance est nulle et A appartient à Δ.
:::

::: exemple La distance à une droite par le produit vectoriel

On reprend D passant par B(1 ; −1 ; 0) de vecteur directeur u⃗(1 ; 2 ; 2) et le point M(4 ; −1 ; 3).

1. BM⃗ a pour coordonnées (3 ; 0 ; 3), et BM⃗ ∧ u⃗ = (0 × 2 − 3 × 2 ; 3 × 1 − 3 × 2 ; 3 × 2 − 0 × 1) = (−6 ; −3 ; 6).
2. Sa norme vaut √(36 + 9 + 36) = 9, et ‖u⃗‖ = 3.
3. Donc d(M, D) = 9/3 = 3. Contrôle : c'est la valeur trouvée avec le projeté H(2 ; 1 ; 2) ✓.

:::

::: verifie À toi : l'aire d'un triangle
Calculer l'aire du triangle ABC pour A(1 ; 0 ; 0), B(0 ; 2 ; 0) et C(0 ; 0 ; 3).

---

AB⃗(−1 ; 2 ; 0) et AC⃗(−1 ; 0 ; 3) donnent AB⃗ ∧ AC⃗ = (2 × 3 − 0 × 0 ; 0 × (−1) − (−1) × 3 ; (−1) × 0 − 2 × (−1)) = (6 ; 3 ; 2), de norme √(36 + 9 + 4) = 7. Cette norme est l'aire du parallélogramme construit sur AB⃗ et AC⃗ : le triangle en vaut la moitié, soit 7/2.
:::

::: retenir
AB⃗ ∧ AC⃗ donne à la fois la normale du plan (ABC), l'aire du triangle (la moitié de sa norme) et, divisé par ‖u⃗‖, la distance d'un point à une droite.
:::

## 📦 Le produit mixte : coplanarité, volumes, distance de deux droites

Le tétraèdre ABCD a pour sommets A(3 ; 0 ; 2), B(1 ; 1 ; 0), C(2 ; 3 ; 1) et D(0 ; 2 ; 2). Ses quatre sommets sont-ils bien hors d'un même plan, et quel est son volume ?
Peut-on répondre aux deux questions avec un seul nombre ?

::: definition
Le **produit mixte** de trois vecteurs u⃗, v⃗, w⃗ est le réel noté **(u⃗, v⃗, w⃗)** et défini par :
$$ (u⃗, v⃗, w⃗) = (u⃗ ∧ v⃗) . w⃗ $$
:::

::: figure Le parallélépipède construit sur AB⃗, AD⃗ et AE⃗ : la base ABCD est coloriée, et la hauteur h (en orange) descend de E perpendiculairement à la base.
<svg viewBox="0 0 300 244">
<title>Le parallélépipède construit sur AB, AD et AE : la base ABCD est coloriée et la hauteur h descend de E perpendiculairement à la base</title>
<polygon points="40.00,215.00 150.40,215.00 225.66,195.45 115.26,195.45" fill="#0f6e56" opacity="0.18"/><line x1="115.26" y1="195.45" x2="40" y2="215" stroke="#94a3b8" stroke-width="1.6" stroke-dasharray="5 4"/><line x1="115.26" y1="195.45" x2="225.66" y2="195.45" stroke="#94a3b8" stroke-width="1.6" stroke-dasharray="5 4"/><line x1="115.26" y1="195.45" x2="144.24" y2="100" stroke="#94a3b8" stroke-width="1.6" stroke-dasharray="5 4"/><line x1="40" y1="215" x2="150.4" y2="215" stroke="#0f172a" stroke-width="2"/><line x1="150.4" y1="215" x2="225.66" y2="195.45" stroke="#0f172a" stroke-width="2"/><line x1="40" y1="215" x2="68.98" y2="119.55" stroke="#0f172a" stroke-width="2"/><line x1="150.4" y1="215" x2="179.38" y2="119.55" stroke="#0f172a" stroke-width="2"/><line x1="225.66" y1="195.45" x2="254.64" y2="100" stroke="#0f172a" stroke-width="2"/><line x1="68.98" y1="119.55" x2="179.38" y2="119.55" stroke="#0f172a" stroke-width="2"/><line x1="179.38" y1="119.55" x2="254.64" y2="100" stroke="#0f172a" stroke-width="2"/><line x1="254.64" y1="100" x2="144.24" y2="100" stroke="#0f172a" stroke-width="2"/><line x1="144.24" y1="100" x2="68.98" y2="119.55" stroke="#0f172a" stroke-width="2"/><line x1="68.98" y1="119.55" x2="68.98" y2="211.55" stroke="#b45309" stroke-width="2.4" stroke-dasharray="5 4"/><polyline points="69.0,201.4 79.1,201.4 79.1,211.6" fill="none" stroke="#0f172a" stroke-width="1.4"/><circle cx="40" cy="215" r="3.5" fill="#0f172a"/><circle cx="150.4" cy="215" r="3.5" fill="#0f172a"/><circle cx="115.26" cy="195.45" r="3.5" fill="#94a3b8"/><circle cx="225.66" cy="195.45" r="3.5" fill="#0f172a"/><circle cx="68.98" cy="119.55" r="3.5" fill="#0f172a"/><circle cx="179.38" cy="119.55" r="3.5" fill="#0f172a"/><circle cx="144.24" cy="100" r="3.5" fill="#0f172a"/><circle cx="254.64" cy="100" r="3.5" fill="#0f172a"/><circle cx="68.98" cy="211.55" r="3.5" fill="#b45309"/><text x="28" y="231" text-anchor="middle" fill="#0f172a" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">A</text><text x="160.4" y="233" text-anchor="middle" fill="#0f172a" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">B</text><text x="103.26" y="189.45" text-anchor="middle" fill="#94a3b8" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">D</text><text x="239.66" y="201.45" text-anchor="middle" fill="#0f172a" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">C</text><text x="56.98" y="117.55" text-anchor="middle" fill="#0f172a" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">E</text><text x="191.38" y="113.55" text-anchor="middle" fill="#0f172a" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">F</text><text x="140.24" y="90" text-anchor="middle" fill="#0f172a" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">H</text><text x="268.64" y="94" text-anchor="middle" fill="#0f172a" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">G</text><text x="82.98" y="165.55" text-anchor="start" fill="#b45309" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">h</text>
</svg>
:::

Sur la figure, le produit vectoriel AB⃗ ∧ AD⃗ a pour norme l'aire de la base ABCD, et le produit scalaire avec AE⃗ en multiplie la valeur absolue par la hauteur h : |(AB⃗, AD⃗, AE⃗)| = aire de la base × h, le volume du parallélépipède.

::: exemple Volume et hauteur du tétraèdre ABCD

1. AB⃗(−2 ; 1 ; −2), AC⃗(−1 ; 3 ; −1) et AD⃗(−3 ; 2 ; 0).
2. AB⃗ ∧ AC⃗ = (1 × (−1) − (−2) × 3 ; (−2) × (−1) − (−2) × (−1) ; (−2) × 3 − 1 × (−1)) = (5 ; 0 ; −5).
3. (AB⃗, AC⃗, AD⃗) = 5 × (−3) + 0 × 2 + (−5) × 0 = −15. Ce nombre est non nul : A, B, C, D ne sont pas coplanaires, le tétraèdre existe.
4. Le volume est (1/6) × |−15| = 5/2, avec une valeur absolue parce que le produit mixte est signé.
5. Pour la hauteur issue de A, BC⃗(1 ; 2 ; 1), BD⃗(−1 ; 1 ; 2) et BA⃗(2 ; −1 ; 2) donnent BC⃗ ∧ BD⃗ = (3 ; −3 ; 3), de norme 3√3, et (BC⃗, BD⃗, BA⃗) = 6 + 3 + 6 = 15. Donc h = 15/(3√3) = 5√3/3. Contrôle : (1/3) × aire(BCD) × h = (1/3) × (3√3/2) × (5/√3) = 5/2 ✓.

:::

::: piege
**Erreur : garder le signe du produit mixte et annoncer un volume de −5/2.** L'erreur tente parce que le calcul vient de donner −15. Mais un volume est positif : le signe ne dépend que de l'ordre des vecteurs, puisque (AB⃗, AD⃗, AC⃗) = 15 pour ce même tétraèdre. On met toujours le produit mixte en valeur absolue.
:::

::: propriete
Trois vecteurs u⃗, v⃗, w⃗ sont coplanaires si et seulement si (u⃗, v⃗, w⃗) = 0.
Si u⃗ et v⃗ ne sont pas colinéaires, l'ensemble des points M tels que (u⃗, v⃗, AM⃗) = 0 est le plan passant par A de vecteurs directeurs u⃗ et v⃗.
Une base orthonormée (e₁⃗, e₂⃗, e₃⃗) est directe si et seulement si (e₁⃗, e₂⃗, e₃⃗) = 1.
Le volume du parallélépipède ABCDEFGH est |(AB⃗, AD⃗, AE⃗)|. Le volume du tétraèdre ABCD est (1/6)|(AB⃗, AC⃗, AD⃗)|, et sa hauteur issue de A est |(BC⃗, BD⃗, BA⃗)|/‖BC⃗ ∧ BD⃗‖.
Cas limite : un produit mixte nul signifie que le « solide » est aplati dans un plan, donc de volume nul.
:::

Une base orthonormée peut être indirecte : u⃗(1 ; 0 ; 0), v⃗(0 ; 0 ; 1), w⃗(0 ; 1 ; 0) est orthonormée, mais u⃗ ∧ v⃗ = (0 ; −1 ; 0), donc le produit mixte vaut −1 et la base est indirecte.

::: exemple Quatre points coplanaires

Les points E(0 ; 1 ; 2), F(1 ; 3 ; 3), G(2 ; 0 ; 4) et H(3 ; 2 ; 5) sont-ils dans un même plan ?

1. EF⃗(1 ; 2 ; 1), EG⃗(2 ; −1 ; 2) et EH⃗(3 ; 1 ; 3).
2. EF⃗ ∧ EG⃗ = (2 × 2 − 1 × (−1) ; 1 × 2 − 1 × 2 ; 1 × (−1) − 2 × 2) = (5 ; 0 ; −5).
3. (EF⃗, EG⃗, EH⃗) = 5 × 3 + 0 × 1 + (−5) × 3 = 0 : les quatre points sont coplanaires. Contrôle : EH⃗ = EF⃗ + EG⃗, car (1 + 2 ; 2 − 1 ; 1 + 2) = (3 ; 1 ; 3) ✓.

:::

::: propriete
Soient D(A, u⃗) et D′(A′, u′⃗) deux droites non coplanaires, et H, H′ les points où D et D′ coupent leur perpendiculaire commune. La distance des deux droites est :
$$ HH′ = |(u⃗, u′⃗, AA′⃗)| / ‖u⃗ ∧ u′⃗‖ $$
Cas limite : deux droites sont coplanaires si et seulement si (u⃗, u′⃗, AA′⃗) = 0, et la formule ne s'applique alors pas.
:::

::: exemple La distance de deux câbles non coplanaires

D passe par A(1 ; 0 ; 0) avec u⃗(1 ; 1 ; 0) et D′ passe par A′(0 ; 1 ; 3) avec u′⃗(0 ; 1 ; 1).

1. u⃗ ∧ u′⃗ = (1 × 1 − 0 × 1 ; 0 × 0 − 1 × 1 ; 1 × 1 − 1 × 0) = (1 ; −1 ; 1), de norme √3 : les deux directions ne sont pas colinéaires.
2. AA′⃗(−1 ; 1 ; 3) donne (u⃗, u′⃗, AA′⃗) = −1 − 1 + 3 = 1. Ce produit mixte est non nul : D et D′ ne sont pas coplanaires.
3. La distance est HH′ = 1/√3 = √3/3. Contrôle : H(−1/3 ; −4/3 ; 0) est sur D et H′(0 ; −5/3 ; 1/3) sur D′, avec HH′⃗ = (1/3 ; −1/3 ; 1/3) orthogonal à u⃗ et à u′⃗ (1/3 − 1/3 = 0 et −1/3 + 1/3 = 0), de norme √3/3 ✓.

:::

::: verifie À toi : le volume d'un parallélépipède
Calculer le volume du parallélépipède ABCDEFGH tel que AB⃗(1 ; 0 ; 2), AD⃗(0 ; 3 ; 1) et AE⃗(1 ; 1 ; 1).

---

AB⃗ ∧ AD⃗ = (0 × 1 − 2 × 3 ; 2 × 0 − 1 × 1 ; 1 × 3 − 0 × 0) = (−6 ; −1 ; 3). Alors (AB⃗, AD⃗, AE⃗) = −6 − 1 + 3 = −4, et le volume est la valeur absolue : 4.
:::

::: retenir
(u⃗, v⃗, w⃗) = (u⃗ ∧ v⃗) . w⃗ est nul si et seulement si les trois vecteurs sont coplanaires ; sa valeur absolue est le volume du parallélépipède, son sixième celui du tétraèdre, et |(u⃗, u′⃗, AA′⃗)|/‖u⃗ ∧ u′⃗‖ la distance de deux droites non coplanaires.
:::

## 🔮 La sphère : définition et équation

Un ballon de rayon 3 est centré au point I(2 ; −1 ; 3). Un point M(x ; y ; z) est sur sa surface lorsque IM = 3.
Comment traduire cette égalité de longueurs en une équation en x, y, z, et comment reconnaître un ballon dans une équation désordonnée ?

::: definition
Soient I un point et R un réel positif. La **sphère** de centre I et de rayon R est l'ensemble des points M de l'espace tels que IM = R. On la note S(I, R).
:::

::: figure La sphère de centre I et de rayon R, vue en perspective avec son équateur : tous les points M de la surface vérifient IM = R.
<svg viewBox="0 0 260 210">
<title>La sphère de centre I et de rayon R : tous les points M tels que IM = R, vus en perspective avec l'équateur</title>
<circle cx="130" cy="105" r="80" fill="#0f6e56" opacity="0.10"/><circle cx="130" cy="105" r="80" fill="none" stroke="#0f172a" stroke-width="2"/><path d="M50 105 A 80 25.6 0 0 0 210 105" fill="none" stroke="#0f172a" stroke-width="1.5"/><path d="M50 105 A 80 25.6 0 0 1 210 105" fill="none" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="5 4"/><line x1="130" y1="105" x2="198.2" y2="63.19" stroke="#b45309" stroke-width="2.6"/><circle cx="130" cy="105" r="3.5" fill="#0f172a"/><circle cx="198.2" cy="63.19" r="3.5" fill="#b45309"/><text x="118" y="123" text-anchor="middle" fill="#0f172a" font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">I</text><text x="212.2" y="59.19" text-anchor="middle" fill="#b45309" font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">M</text><text x="158.1" y="102.09" text-anchor="middle" fill="#b45309" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">R</text>
</svg>
:::

Sur la figure, le segment [IM] est un rayon : M est sur la sphère exactement lorsque sa longueur est R.

::: exemple Équation du ballon centré en I(2 ; −1 ; 3), de rayon 3

1. M est sur la sphère si et seulement si IM = 3, donc IM² = 9 (deux nombres positifs sont égaux exactement quand leurs carrés le sont).
2. Le repère est orthonormé, donc IM² = (x − 2)² + (y + 1)² + (z − 3)².
3. L'équation est (x − 2)² + (y + 1)² + (z − 3)² = 9. En développant : x² + y² + z² − 4x + 2y − 6z + 5 = 0. Contrôle : le point (2 ; −1 ; 6), situé à 3 au-dessus du centre, donne 0 + 0 + 9 = 9 ✓.

:::

::: exemple Reconnaître une sphère dans une équation développée

Soit x² + y² + z² − 6x + 2y − 4z + 10 = 0.

1. On complète chaque carré : x² − 6x = (x − 3)² − 9, y² + 2y = (y + 1)² − 1 et z² − 4z = (z − 2)² − 4.
2. L'équation devient (x − 3)² + (y + 1)² + (z − 2)² − 14 + 10 = 0, soit (x − 3)² + (y + 1)² + (z − 2)² = 4.
3. C'est la sphère de centre I(3 ; −1 ; 2) et de rayon R = 2, car le second membre vaut R². Contrôle : le point (3 ; −1 ; 4) donne 9 + 1 + 16 − 18 − 2 − 16 + 10 = 0 ✓.

:::

::: piege
**Erreur : lire le centre I(3 ; 1 ; 2) et le rayon R = 4 sur (x − 3)² + (y + 1)² + (z − 2)² = 4.** L'erreur tente parce qu'on recopie les nombres tels qu'ils s'affichent. Mais (y + 1) = (y − (−1)) donne la coordonnée −1, et le second membre est R², donc R = 2 : le centre est I(3 ; −1 ; 2).
:::

::: propriete
L'espace est rapporté à un repère orthonormé. La sphère de centre I(a ; b ; c) et de rayon R a pour équation :
$$ (x − a)² + (y − b)² + (z − c)² = R² $$
Réciproquement, l'équation x² + y² + z² − 2ax − 2by − 2cz + d = 0 s'écrit (x − a)² + (y − b)² + (z − c)² = h avec h = a² + b² + c² − d : si h > 0, c'est la sphère de centre I(a ; b ; c) et de rayon √h ; si h = 0, le seul point I ; si h < 0, l'ensemble vide.
La sphère de diamètre [AB] est l'ensemble des points M tels que MA⃗ . MB⃗ = 0 ; son centre est le milieu de [AB] et son rayon AB/2.
:::

::: exemple La sphère de diamètre [AB]

Soit A(1 ; 0 ; −1) et B(3 ; 2 ; 3).

1. Le centre est le milieu I(2 ; 1 ; 1) et AB⃗(2 ; 2 ; 4) donne AB = √24 = 2√6, donc R = √6.
2. L'équation est (x − 2)² + (y − 1)² + (z − 1)² = 6, soit x² + y² + z² − 4x − 2y − 2z = 0.
3. Contrôle par l'autre caractérisation : MA⃗ . MB⃗ = (1 − x)(3 − x) + (−y)(2 − y) + (−1 − z)(3 − z) = x² − 4x + 3 + y² − 2y + z² − 2z − 3, soit la même équation ✓.

:::

::: verifie À toi : une équation développée
Déterminer l'ensemble des points M(x ; y ; z) tels que x² + y² + z² + 4x − 2y + 6z + 5 = 0.

---

On complète les carrés : (x + 2)² − 4 + (y − 1)² − 1 + (z + 3)² − 9 + 5 = 0, soit (x + 2)² + (y − 1)² + (z + 3)² = 9. L'ensemble est la sphère de centre I(−2 ; 1 ; −3) et de rayon 3, car le second membre vaut R² = 9.
:::

::: retenir
La sphère de centre I(a ; b ; c) et de rayon R a pour équation (x − a)² + (y − b)² + (z − c)² = R² : on lit le centre avec le signe opposé aux nombres affichés, et le rayon sous une racine carrée.
:::

## ✂️ La sphère et le plan : section et tangence

On coupe une orange, sphère de centre I(1 ; −2 ; 1) et de rayon 5, par un plan. Selon la position du plan, on obtient une tranche circulaire, un simple point de contact, ou rien.
Un seul nombre, la distance du centre au plan, permet-il de décider lequel de ces trois cas se présente ?

::: definition
Un plan P est **tangent** à une sphère S en un point H lorsque P ∩ S = {H}. Dans ce cas, H est le projeté orthogonal du centre de S sur P.
:::

::: figure Coupe de la sphère par le plan P (vue de profil, pas en perspective) : dans le triangle IHM rectangle en H, R est l'hypoténuse, d = IH et r = HM. Ici R = 5, d = 3 et r = 4 à titre d'illustration.
<svg viewBox="0 0 240 204">
<title>Coupe de la sphère par un plan P : dans le triangle IHM rectangle en H, R est l'hypoténuse, d et r les côtés de l'angle droit</title>
<circle cx="120" cy="100" r="100" fill="#0f6e56" opacity="0.10"/><circle cx="120" cy="100" r="100" fill="none" stroke="#0f172a" stroke-width="2"/><line x1="14" y1="40" x2="226" y2="40" stroke="#0f172a" stroke-width="1.8"/><line x1="40" y1="40" x2="200" y2="40" stroke="#0f6e56" stroke-width="4"/><line x1="120" y1="100" x2="120" y2="40" stroke="#b45309" stroke-width="2.4"/><line x1="120" y1="100" x2="200" y2="40" stroke="#0f172a" stroke-width="2"/><polyline points="120,51 131,51 131,40" fill="none" stroke="#0f172a" stroke-width="1.3"/><circle cx="120" cy="100" r="3.5" fill="#0f172a"/><circle cx="120" cy="40" r="3.5" fill="#b45309"/><circle cx="200" cy="40" r="3.5" fill="#0f172a"/><text x="108" y="116" text-anchor="middle" fill="#0f172a" font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">I</text><text x="108" y="34" text-anchor="middle" fill="#b45309" font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">H</text><text x="204" y="28" text-anchor="middle" fill="#0f172a" font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">M</text><text x="110" y="75" text-anchor="middle" fill="#b45309" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">d</text><text x="166" y="64" text-anchor="middle" fill="#0f172a" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">R</text><text x="156" y="32" text-anchor="middle" fill="#0f6e56" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">r</text><text x="26" y="32" text-anchor="middle" fill="#0f172a" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">P</text>
</svg>
:::

Sur la figure, M est un point commun à la sphère et au plan : IM = R, IH = d et HM = r. Le théorème de Pythagore relie ces trois longueurs.

::: exemple Un plan qui coupe la sphère

Soit S : x² + y² + z² − 2x + 4y − 2z − 19 = 0 et P : 2x − y + 2z + 3 = 0.

1. On complète les carrés : (x − 1)² + (y + 2)² + (z − 1)² = 25. La sphère a pour centre I(1 ; −2 ; 1) et pour rayon R = 5.
2. La distance du centre au plan est d(I, P) = |2 + 2 + 2 + 3|/√(4 + 1 + 4) = 9/3 = 3, inférieure à 5 : le plan coupe la sphère suivant un cercle.
3. Le centre du cercle est le projeté H de I sur P : H(1 + 2α ; −2 − α ; 1 + 2α), et 2(1 + 2α) − (−2 − α) + 2(1 + 2α) + 3 = 9α + 9 = 0 donne α = −1, soit H(−1 ; −1 ; −1).
4. Le rayon est r = √(R² − d²) = √(25 − 9) = 4. Contrôle : H vérifie −2 + 1 − 2 + 3 = 0, IH = ‖(−2 ; 1 ; −2)‖ = 3 = d, et pour un point M du cercle, IM² = IH² + HM² = 9 + 16 = 25 = R² ✓.

:::

::: piege
**Erreur : prendre r = R − d pour le rayon du cercle.** L'erreur tente parce que le cercle semble « rétrécir » quand le plan s'éloigne du centre. Mais le triangle IHM est rectangle en H, donc r² + d² = R² : avec R = 5 et d = 3, on a r = 4 et non 5 − 3 = 2.
:::

::: propriete
Soient S une sphère de centre I et de rayon R, P un plan, H le projeté orthogonal de I sur P et d = IH = d(I, P). Alors :
Si d > R, P ∩ S = ∅ : le plan et la sphère sont disjoints.
Si d = R, P ∩ S = {H} : le plan est tangent à la sphère en H.
Si d < R, P ∩ S est le cercle du plan P de centre H et de rayon r = √(R² − d²).
Le plan tangent à S en un point A de S est le plan passant par A et de vecteur normal IA⃗.
Cas limite : si d = 0, le plan passe par le centre et r = R.
:::

::: exemple Tangence, vide et plan tangent en un point

On garde S de centre I(1 ; −2 ; 1) et de rayon 5.

1. Pour Q : 2x − y + 2z + 9 = 0, d(I, Q) = |2 + 2 + 2 + 9|/3 = 15/3 = 5 = R : Q est tangent à S. Le point de contact est le projeté H(1 + 2α ; −2 − α ; 1 + 2α), avec 9α + 15 = 0, soit α = −5/3 et H(−7/3 ; −1/3 ; −7/3).
2. Pour Q′ : 2x − y + 2z + 12 = 0, d(I, Q′) = 18/3 = 6 > 5 : Q′ ne rencontre pas S.
3. Le point A(4 ; −6 ; 1) est sur S, car (4 − 1)² + (−6 + 2)² + (1 − 1)² = 9 + 16 = 25. Le plan tangent en A a pour vecteur normal IA⃗(3 ; −4 ; 0) : 3(x − 4) − 4(y + 6) = 0, soit 3x − 4y − 36 = 0. Contrôle : d(I, plan) = |3 + 8 − 36|/5 = 5 = R ✓.

:::

::: verifie À toi : une section plane
La sphère S a pour équation (x − 2)² + (y + 1)² + (z − 3)² = 25 et le plan P pour équation x + 2y + 2z + 6 = 0. Quelle est leur intersection ?

---

Le centre est I(2 ; −1 ; 3) et R = 5. La distance du centre au plan est d = |2 − 2 + 6 + 6|/√(1 + 4 + 4) = 12/3 = 4, inférieure à R : l'intersection est un cercle, de rayon r = √(25 − 16) = 3, dont le centre est le projeté de I sur P.
:::

::: retenir
On compare d(I, P) à R : d > R donne le vide, d = R la tangence en H, d < R le cercle de centre H et de rayon √(R² − d²).
:::

> 🏆 Les huit portes sont franchies : tu calcules un produit scalaire pour détecter une orthogonalité, tu écris l'équation d'un plan et mesures une distance, tu dresses une normale avec le produit vectoriel, tu transformes un produit mixte en volume ou en test de coplanarité, et tu fais parler une sphère coupée par un plan. Prochaine étape : les probabilités sur un ensemble fini.
