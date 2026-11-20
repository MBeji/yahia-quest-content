# ⚔️ Trigonométrie et mesure de grandeurs — du demi-cercle au triangle quelconque

> 💡 «Un angle et deux longueurs suffisent à décrire tout un triangle : la trigonométrie est l'art de passer des uns aux autres sans jamais déplier le terrain.»

Jusqu'ici, un angle était une ouverture que l'on mesure au rapporteur. Dans ce chapitre il devient un **nombre** que l'on calcule, et ce nombre ouvre deux portes : celle des lignes trigonométriques (cosinus, sinus, tangente, cotangente), puis celle de la mesure d'un triangle quelconque (loi du sinus, aire, théorème d'El-Kashi).
Huit étapes t'y conduisent : cosinus et sinus, valeurs remarquables, tangente et cotangente, relations fondamentales, angles supplémentaires et complémentaires, loi du sinus, aire d'un triangle, théorème d'El-Kashi. Le radian, vu avec les rotations, est supposé connu : π radians valent 180°, et l'on note π/2 l'angle droit.

## 🌓 Cosinus et sinus : lire un angle sur le demi-cercle

Une lampe de bureau pivote autour d'une charnière O. Son bras a pour longueur 1 (c'est l'unité du dessin) et, à partir de la position horizontale, on l'incline d'un angle α compris entre 0 et π, c'est-à-dire entre 0° et 180°.
Pour chaque inclinaison, deux nombres décrivent le bout du bras : de combien il est décalé horizontalement de la charnière, et à quelle hauteur il se trouve. Ces deux nombres ne dépendent que de α : comment les lire sur le dessin, et que valent-ils aux positions extrêmes ?

::: definition
Le plan est muni d'un repère orthonormé (O, i⃗, j⃗), avec OA⃗ = i⃗ et OB⃗ = j⃗. Le **demi-cercle trigonométrique** est le demi-cercle de centre O et de rayon 1, de diamètre [A′A], qui contient B (A′ est le symétrique de A par rapport à O).
À tout réel α de [0 ; π] correspond un seul point M de ce demi-cercle tel que AÔM = α. Le **cosinus** de α, noté cos α, est l'abscisse de M ; le **sinus** de α, noté sin α, est l'ordonnée de M.
:::

::: figure Pour un angle α dessiné ici à titre d'illustration (environ 50°), le point M a pour abscisse la longueur verte, qui est cos α, et pour ordonnée la longueur orange, qui est sin α
<svg viewBox="0 60 340 176"><path d="M60 200 L60 200 L60.4 190.4 L61.7 180.9 L63.7 171.5 L66.6 162.4 L70.3 153.5 L74.7 145 L79.9 136.9 L85.7 129.3 L92.2 122.2 L99.3 115.7 L106.9 109.9 L115 104.7 L123.5 100.3 L132.4 96.6 L141.5 93.7 L150.9 91.7 L160.4 90.4 L170 90 L179.6 90.4 L189.1 91.7 L198.5 93.7 L207.6 96.6 L216.5 100.3 L225 104.7 L233.1 109.9 L240.7 115.7 L247.8 122.2 L254.3 129.3 L260.1 136.9 L265.3 145 L269.7 153.5 L273.4 162.4 L276.3 171.5 L278.3 180.9 L279.6 190.4 L280 200 Z" fill="#0f6e56" opacity="0.07"/><path d="M60 200 A110 110 0 0 1 280 200" fill="none" stroke="#0f172a" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/><path d="M36 200 H304 M170 200 V74" fill="none" stroke="#0f172a" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/><path d="M304 200 L296 204 L296 196 Z" fill="#0f172a"/><path d="M170 74 L174 82 L166 82 Z" fill="#0f172a"/><path d="M170 200 L240.7 115.7" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M240.7 115.7 L240.7 200" fill="none" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="5 4" stroke-linecap="round" stroke-linejoin="round"/><path d="M240.7 115.7 L170 115.7" fill="none" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="5 4" stroke-linecap="round" stroke-linejoin="round"/><path d="M170 200 L240.7 200" fill="none" stroke="#0f6e56" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/><path d="M170 200 L170 115.7" fill="none" stroke="#b45309" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/><path d="M200 200 A30 30 0 0 0 189.3 177" fill="none" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/><circle cx="60" cy="200" r="3.5" fill="#0f172a"/><circle cx="280" cy="200" r="3.5" fill="#0f172a"/><circle cx="170" cy="90" r="3.5" fill="#0f172a"/><circle cx="170" cy="200" r="3.5" fill="#0f172a"/><circle cx="240.7" cy="115.7" r="4.5" fill="#6d28d9"/><g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.6" stroke-linejoin="round"><text x="158" y="217" text-anchor="middle" font-size="14" fill="#0f172a">O</text><text x="280" y="217" text-anchor="middle" font-size="14" fill="#0f172a">A</text><text x="60" y="217" text-anchor="middle" font-size="14" fill="#0f172a">A′</text><text x="184" y="88" text-anchor="middle" font-size="14" fill="#0f172a">B</text><text x="254.7" y="107.7" text-anchor="middle" font-size="14" fill="#6d28d9">M</text><text x="240.7" y="218" text-anchor="middle" font-size="13" fill="#0f6e56">cos α</text><text x="162" y="120.7" text-anchor="end" font-size="13" fill="#b45309">sin α</text><text x="206" y="193" text-anchor="middle" font-size="14" fill="#0f172a">α</text></g></svg>
:::

Sur la figure, la longueur verte, portée par l'axe des abscisses, est l'abscisse de M, donc cos α ; la longueur orange, portée par l'axe des ordonnées, est son ordonnée, donc sin α. Pour la lampe, cos α est le décalage horizontal du bout du bras et sin α sa hauteur.

::: exemple Le bras de la lampe à trois inclinaisons : 0, π/2 et π

1. α = 0 : le bras est couché vers la droite, M = A, de coordonnées (1 ; 0). Donc cos 0 = 1 et sin 0 = 0, car l'abscisse et l'ordonnée de M se lisent directement.
2. α = π/2 : le bras est vertical, M = B, de coordonnées (0 ; 1). Donc cos π/2 = 0 et sin π/2 = 1, car B est sur l'axe des ordonnées, à la hauteur 1.
3. α = π : le bras est couché vers la gauche, M = A′, de coordonnées (−1 ; 0). Donc cos π = −1 et sin π = 0, car A′ est le symétrique de A par rapport à O.
4. Entre π/2 et π, le bout du bras passe à gauche de l'axe des ordonnées : son abscisse est négative, donc cos α < 0, alors que sa hauteur reste positive, donc sin α > 0.

:::

::: piege Prendre le cosinus pour une longueur, donc pour un nombre toujours positif
Sur le dessin d'un angle obtus, un élève voit que M est à 0,3 de l'axe des ordonnées et écrit cos α = 0,3. Cela tente parce que, pour un angle aigu, cos α est bien la longueur OP.
Mais le cosinus est l'abscisse de M, un nombre qui a un signe : M étant à gauche de l'axe des ordonnées, l'abscisse vaut −0,3. La longueur OP vaut 0,3, le cosinus vaut −0,3.
:::

::: propriete

- Pour tout α de [0 ; π] : −1 ≤ cos α ≤ 1 et 0 ≤ sin α ≤ 1, car M est sur le demi-cercle de rayon 1, au-dessus ou sur l'axe des abscisses.
- cos α > 0 pour α dans [0 ; π/2[ et cos α < 0 pour α dans ]π/2 ; π] ; sin α ≥ 0 sur tout [0 ; π].
- Une valeur donnée de [−1 ; 1] est le cosinus d'un seul angle de [0 ; π], car un seul point du demi-cercle a cette abscisse.

Cas limite : cos π/2 = 0 (M est sur l'axe des ordonnées) et sin 0 = sin π = 0 (M est sur l'axe des abscisses).
:::

::: verifie
Pour quel angle α de [0 ; π] a-t-on cos α = −1 ? Pour quels angles a-t-on sin α = 0 ?

---

cos α = −1 signifie que M a pour abscisse −1 : le seul point du demi-cercle dans ce cas est A′, donc α = π. sin α = 0 signifie que M est sur l'axe des abscisses : il y a deux points du demi-cercle dans ce cas, A et A′, donc α = 0 ou α = π.
:::

::: retenir
cos α et sin α sont l'abscisse et l'ordonnée du point M du demi-cercle trigonométrique tel que AÔM = α : cos α est dans [−1 ; 1] et peut être négatif, sin α est dans [0 ; 1] et ne l'est jamais.
:::

## 📐 Valeurs remarquables : trois angles dont on connaît tout

Une échelle de 4 m est appuyée contre un mur et forme avec le sol un angle de 60°, soit π/3. À quelle hauteur touche-t-elle le mur ? Sans calculatrice, tout repose sur le nombre sin(π/3).
D'où viennent des valeurs comme √3/2 ou √2/2, que l'on dit « exactes », et comment les retrouver quand la mémoire flanche ?

::: propriete
Soit un triangle rectangle et α l'un de ses angles aigus. Alors cos α = côté adjacent / hypoténuse et sin α = côté opposé / hypoténuse.
Raison : si M est le point du demi-cercle avec AÔM = α et P son projeté sur (OA), le triangle OPM est rectangle en P avec OM = 1, donc OP/OM = cos α et MP/OM = sin α. Un triangle rectangle de même angle α en est un agrandissement, et les rapports ne changent pas.
:::

::: figure Deux triangles rectangles à connaître : la moitié d'un carré de côté 1, et la moitié d'un triangle équilatéral de côté 2 coupé par une hauteur ; leurs côtés se calculent par le théorème de Pythagore
<svg viewBox="0 58 340 176"><path d="M25 205 L101 205 L25 129 Z" fill="#0f6e56" opacity="0.12"/><path d="M25 205 L101 205 L25 129 Z" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M35 205 L35 195 L25 195" fill="none" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/><path d="M84 188 A24 24 0 0 0 77 205" fill="none" stroke="#b45309" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M185 205 L261 205 L261 73.4 Z" fill="#0f6e56" opacity="0.12"/><path d="M185 205 L261 205 L261 73.4 Z" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M251 205 L251 195 L261 195" fill="none" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/><path d="M211 205 A26 26 0 0 0 198 182.5" fill="none" stroke="#b45309" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M248 95.9 A26 26 0 0 0 261 99.4" fill="none" stroke="#b45309" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.6" stroke-linejoin="round"><text x="63" y="223" text-anchor="middle" font-size="14" fill="#0f172a">1</text><text x="10" y="171" text-anchor="middle" font-size="14" fill="#0f172a">1</text><text x="77" y="156" text-anchor="middle" font-size="14" fill="#0f6e56">√2</text><text x="64" y="191" text-anchor="middle" font-size="12" fill="#b45309">π/4</text><text x="223" y="223" text-anchor="middle" font-size="14" fill="#0f172a">1</text><text x="284" y="141" text-anchor="middle" font-size="14" fill="#0f6e56">√3</text><text x="207" y="131" text-anchor="middle" font-size="14" fill="#0f6e56">2</text><text x="231" y="179" text-anchor="middle" font-size="12" fill="#b45309">π/3</text><text x="246" y="128.4" text-anchor="middle" font-size="12" fill="#b45309">π/6</text></g></svg>
:::

Sur la figure, le triangle de droite a pour hypoténuse 2 ; le côté 1 est adjacent à l'angle π/3 mais opposé à l'angle π/6, et le côté √3 est opposé à π/3 mais adjacent à π/6 (Pythagore : 2² − 1² = 3).

::: exemple L'échelle de 4 m, puis le demi-carré

1. Dans le demi-triangle équilatéral, l'angle π/3 a pour côté adjacent 1 et pour côté opposé √3, l'hypoténuse valant 2. Donc cos π/3 = 1/2 et sin π/3 = √3/2, par les rapports « adjacent » et « opposé » sur l'hypoténuse.
2. La hauteur de l'échelle est le côté opposé à l'angle de 60°, l'échelle étant l'hypoténuse : 4 × sin π/3 = 4 × √3/2 = 2√3, soit environ 3,46 m.
3. Dans le demi-carré, les deux côtés de l'angle droit valent 1 et l'hypoténuse √2 (Pythagore : 1 + 1 = 2). L'angle π/4 a pour côté adjacent 1 : cos π/4 = 1/√2 = √2/2, et de même sin π/4 = √2/2.

:::

::: piege Lire « le grand côté » au lieu de lire le côté opposé à l'angle
Un élève retient que √3/2 « va avec le sinus » et écrit sin π/6 = √3/2. Cela tente parce que, dans la table, le sinus de π/3 vaut bien √3/2.
Mais « adjacent » et « opposé » se lisent depuis l'angle considéré : pour π/6, le côté opposé est 1, donc sin π/6 = 1/2 ; c'est le cosinus de π/6 qui vaut √3/2.
:::

::: propriete

| α (radians) | 0   | π/6  | π/4  | π/3  | π/2 | π    |
| ----------- | --- | ---- | ---- | ---- | --- | ---- |
| α (degrés)  | 0°  | 30°  | 45°  | 60°  | 90° | 180° |
| cos α       | 1   | √3/2 | √2/2 | 1/2  | 0   | −1   |
| sin α       | 0   | 1/2  | √2/2 | √3/2 | 1   | 0    |

Cas limite : les valeurs en 0, π/2 et π viennent du demi-cercle (il n'existe pas de triangle rectangle d'angle 0). Pour passer des degrés aux radians, on multiplie par π/180 : 135° = 135 × π/180 = 3π/4.
:::

::: verifie
Un toboggan de 5 m de long fait un angle de π/6 avec le sol. Quelle est sa hauteur, et quelle distance horizontale couvre-t-il ?

---

Le toboggan est l'hypoténuse. La hauteur est le côté opposé à l'angle π/6 : 5 × sin π/6 = 5 × 1/2 = 2,5 m. La distance horizontale est le côté adjacent : 5 × cos π/6 = 5 × √3/2 = 5√3/2, soit environ 4,33 m.
:::

::: retenir
Dans un triangle rectangle, cos α = adjacent/hypoténuse et sin α = opposé/hypoténuse ; pour π/6, π/4 et π/3, on retrouve cos et sin avec le demi-carré et le demi-triangle équilatéral.
:::

## 📏 Tangente et cotangente : le rapport de la pente

Le soleil est à 30° au-dessus de l'horizon, et un poteau de 3 m projette son ombre sur le sol. Le rapport « hauteur du poteau sur longueur de l'ombre » ne dépend pas du poteau : il ne dépend que de l'angle.
Quel nombre, calculé à partir de α, donne ce rapport ? Et que devient-il quand le soleil est à la verticale ?

::: definition
Pour α dans [0 ; π] avec α ≠ π/2, la **tangente** de α est le réel tan α = sin α / cos α. Pour α dans ]0 ; π[, la **cotangente** de α est le réel cot α = cos α / sin α.
:::

::: figure Pour un angle aigu α (dessiné ici à titre d'illustration, environ 50°), la droite (OM) coupe la tangente au demi-cercle en A au point T : la longueur orange AT est tan α
<svg viewBox="0 52 300 178"><path d="M10 205 A100 100 0 0 1 210 205" fill="none" stroke="#0f172a" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/><path d="M-0 205 H250 M110 205 V95" fill="none" stroke="#0f172a" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/><path d="M250 205 L242 209 L242 201 Z" fill="#0f172a"/><path d="M110 95 L114 103 L106 103 Z" fill="#0f172a"/><path d="M210 205 L210 71.8" fill="none" stroke="#0f172a" stroke-width="1.6" stroke-dasharray="6 4" stroke-linecap="round" stroke-linejoin="round"/><path d="M110 205 L210 85.8" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M210 205 L210 85.8" fill="none" stroke="#b45309" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/><path d="M140 205 A30 30 0 0 0 129.3 182" fill="none" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/><circle cx="110" cy="205" r="3.5" fill="#0f172a"/><circle cx="210" cy="205" r="3.5" fill="#0f172a"/><circle cx="174.3" cy="128.4" r="4.5" fill="#6d28d9"/><circle cx="210" cy="85.8" r="4.5" fill="#b45309"/><g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.6" stroke-linejoin="round"><text x="100" y="222" text-anchor="middle" font-size="14" fill="#0f172a">O</text><text x="212" y="222" text-anchor="middle" font-size="14" fill="#0f172a">A</text><text x="164.3" y="118.4" text-anchor="middle" font-size="14" fill="#6d28d9">M</text><text x="224" y="75.8" text-anchor="middle" font-size="14" fill="#b45309">T</text><text x="232" y="149.4" text-anchor="middle" font-size="13" fill="#b45309">tan α</text><text x="158" y="198" text-anchor="middle" font-size="14" fill="#0f172a">α</text></g></svg>
:::

Sur la figure, A a pour coordonnées (1 ; 0) et OA = 1 ; si P est le projeté de M sur (OA) (non tracé), Thalès dans les triangles OAT et OPM donne AT/OA = MP/OP, donc AT = sin α / cos α : la longueur orange est bien tan α, comme la hauteur d'un poteau est le rapport « opposé sur adjacent ».

::: exemple Le poteau de 3 m sous un soleil à 30°

1. tan π/6 = sin π/6 / cos π/6 = (1/2)/(√3/2) = 1/√3 = √3/3, par la définition de la tangente.
2. Le rapport hauteur / ombre vaut tan π/6, donc l'ombre est égale à la hauteur divisée par la tangente : 3 / (√3/3) = 9/√3 = 3√3.
3. L'ombre mesure 3√3, soit environ 5,2 m. À 45°, tan π/4 = 1 : l'ombre serait égale au poteau, ce qui donne un repère simple pour vérifier.

:::

::: exemple Un angle obtus : cos α = −3/5 et sin α = 4/5

1. tan α = sin α / cos α = (4/5)/(−3/5) = −4/3, car on divise les deux fractions.
2. cot α = cos α / sin α = (−3/5)/(4/5) = −3/4, et l'on retrouve cot α = 1/tan α.
3. Les deux nombres sont négatifs : pour un angle obtus, sin α > 0 et cos α < 0, donc leur quotient est négatif.

:::

::: piege Écrire tan(π/2) = 1/0 = 0, comme si diviser par zéro donnait un résultat
Pour α = π/2, on lit sin π/2 = 1 et cos π/2 = 0, puis l'on écrit tan π/2 = 1/0 = 0, ou bien « ∞ ». Cela tente parce que « quelque chose divisé par 0 » semble forcément valoir quelque chose.
Mais une division par 0 n'existe pas : tan π/2 n'est pas définie, et c'est pour cela que la définition exclut π/2. De même, cot 0 et cot π ne sont pas définies, car sin 0 = sin π = 0.
:::

::: propriete

| α     | 0           | π/6  | π/4 | π/3  | π/2         | π           |
| ----- | ----------- | ---- | --- | ---- | ----------- | ----------- |
| tan α | 0           | √3/3 | 1   | √3   | non définie | 0           |
| cot α | non définie | √3   | 1   | √3/3 | 0           | non définie |

Quand tan α et cot α sont toutes les deux définies, cot α = 1/tan α. Cas limite : tan α > 0 pour α aigu, tan α < 0 pour α obtus, et tan α = 0 en 0 et en π.
:::

::: verifie
Calculer tan π/3 et cot π/3, puis vérifier que leur produit vaut 1.

---

tan π/3 = sin π/3 / cos π/3 = (√3/2)/(1/2) = √3. cot π/3 = cos π/3 / sin π/3 = (1/2)/(√3/2) = 1/√3 = √3/3. Le produit vaut √3 × √3/3 = 3/3 = 1, ce qui confirme cot α = 1/tan α.
:::

::: retenir
tan α = sin α / cos α (α ≠ π/2) et cot α = cos α / sin α (α ≠ 0 et α ≠ π) ; tan π/2 n'existe pas, et pour un angle aigu tan α est la longueur AT sur la tangente au demi-cercle en A.
:::

## ⚖️ Relations fondamentales : un seul nombre suffit

Le point M du demi-cercle a pour ordonnée 0,6. Où se trouve-t-il ? Le dessin en montre deux : l'un à droite de l'axe des ordonnées, l'autre à gauche.
Quelle équation relie l'abscisse et l'ordonnée d'un point du demi-cercle, et qu'en tire-t-on pour les autres lignes trigonométriques ?

::: figure Les deux points du demi-cercle d'ordonnée 0,6 : dans le triangle OPM, rectangle en P, l'hypoténuse OM vaut 1, un côté vaut 0,6 et l'autre côté vaut cos α, qu'il reste à calculer
<svg viewBox="0 60 340 176"><path d="M60 200 A110 110 0 0 1 280 200" fill="none" stroke="#0f172a" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/><path d="M36 200 H304 M170 200 V74" fill="none" stroke="#0f172a" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/><path d="M304 200 L296 204 L296 196 Z" fill="#0f172a"/><path d="M170 74 L174 82 L166 82 Z" fill="#0f172a"/><path d="M170 200 L258 200 L258 134 Z" fill="#0f6e56" opacity="0.14"/><path d="M82 134 L258 134" fill="none" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="5 4" stroke-linecap="round" stroke-linejoin="round"/><path d="M170 200 L258 134" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M258 134 L258 200" fill="none" stroke="#b45309" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/><path d="M170 200 L258 200" fill="none" stroke="#0f6e56" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/><path d="M248 200 L248 190 L258 190" fill="none" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/><circle cx="258" cy="134" r="4.5" fill="#6d28d9"/><circle cx="82" cy="134" r="4.5" fill="#6d28d9"/><circle cx="170" cy="200" r="3.5" fill="#0f172a"/><g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.6" stroke-linejoin="round"><text x="272" y="126" text-anchor="middle" font-size="14" fill="#6d28d9">M</text><text x="66" y="126" text-anchor="middle" font-size="14" fill="#6d28d9">M′</text><text x="158" y="217" text-anchor="middle" font-size="14" fill="#0f172a">O</text><text x="258" y="218" text-anchor="middle" font-size="14" fill="#0f172a">P</text><text x="214" y="158" text-anchor="middle" font-size="14" fill="#0f172a">1</text><text x="241" y="171" text-anchor="middle" font-size="13" fill="#b45309">0,6</text><text x="214" y="217" text-anchor="middle" font-size="13" fill="#0f6e56">cos α</text><text x="122" y="128" text-anchor="middle" font-size="12" fill="#94a3b8">y = 0,6</text></g></svg>
:::

Sur la figure, le triangle OPM est rectangle en P avec OM = 1, donc Pythagore s'écrit (OP)² + (MP)² = 1, c'est-à-dire cos²α + 0,6² = 1 : l'abscisse de M est un cos α encore inconnu, et c'est cette équation qui la donne.

::: exemple Les points d'ordonnée 0,6 : abscisse, tangente

1. cos²α = 1 − 0,6² = 1 − 0,36 = 0,64, car cos²α + sin²α = 1 avec sin α = 0,6 (on note cos²α pour (cos α)²).
2. cos α = 0,8 ou cos α = −0,8, car deux nombres ont pour carré 0,64.
3. Les deux points existent : M(0,8 ; 0,6) à droite, d'angle aigu, et M′(−0,8 ; 0,6) à gauche, d'angle obtus. Pour M, tan α = 0,6/0,8 = 3/4 ; pour M′, tan α = −3/4.

:::

::: exemple Retrouver cos α et sin α à partir de tan α = 2, avec α aigu

1. En divisant cos²α + sin²α = 1 par cos²α (qui n'est pas nul), on obtient 1 + tan²α = 1/cos²α.
2. 1 + 2² = 5 = 1/cos²α, donc cos²α = 1/5.
3. α est aigu, donc cos α > 0 et cos α = 1/√5 = √5/5.
4. sin α = tan α × cos α = 2 × √5/5 = 2√5/5. Contrôle : cos²α + sin²α = 1/5 + 4/5 = 1.

:::

::: piege Choisir la racine positive sans regarder la position de l'angle
Pour sin α = 0,6, un élève écrit cos²α = 0,64 puis cos α = 0,8, en disant « la racine carrée est positive ». Cela tente parce qu'une racine carrée est positive.
Mais cos α est une solution de t² = 0,64, qui en a deux : +0,8 et −0,8. C'est la position de α qui tranche, aigu pour +0,8 et obtus pour −0,8. Pour sin α, au contraire, le signe est connu : sin α ≥ 0 sur [0 ; π].
:::

::: propriete

- Pour tout x de [0 ; π] : cos²x + sin²x = 1.
- Pour tout x de [0 ; π] avec x ≠ π/2 : 1 + tan²x = 1/cos²x.
- Pour tout x de ]0 ; π[ : 1 + cot²x = 1/sin²x.

Cas limite : la deuxième relation exige cos x ≠ 0, donc x ≠ π/2 ; la troisième exige sin x ≠ 0, donc x ≠ 0 et x ≠ π. La troisième se montre comme la deuxième, en divisant par sin²x.
:::

::: verifie
Un angle x de [0 ; π] vérifie cos x = −7/25. Calculer sin x, puis tan x et cot x.

---

sin²x = 1 − cos²x = 1 − 49/625 = 576/625, donc sin x = 24/25, et non −24/25 puisque sin x ≥ 0 sur [0 ; π]. Alors tan x = sin x / cos x = (24/25)/(−7/25) = −24/7 et cot x = 1/tan x = −7/24. Le signe négatif est cohérent avec un angle obtus.
:::

::: retenir
Pour x dans [0 ; π] : cos²x + sin²x = 1 ; 1 + tan²x = 1/cos²x (x ≠ π/2) ; 1 + cot²x = 1/sin²x (x ≠ 0, π) ; le signe de cos x se décide par la position de x, celui de sin x est toujours positif ou nul.
:::

## 🔄 Angles supplémentaires et complémentaires : deux symétries du demi-cercle

Sur la lampe, deux inclinaisons α et π − α, par exemple 30° et 150°, placent le bout du bras à la même hauteur, de part et d'autre de la verticale. Et deux angles dont la somme fait 90°, comme 30° et 60°, semblent échanger leurs rôles.
Si l'on connaît cos et sin de α, que valent ceux de π − α et de π/2 − α ?

::: figure Deux symétries du demi-cercle (angle α dessiné à titre d'illustration, environ 25°) : M′, symétrique de M par rapport à l'axe des ordonnées, correspond à l'angle π − α ; N, symétrique de M par rapport à la droite d'équation y = x, correspond à l'angle π/2 − α
<svg viewBox="0 66 340 170"><path d="M60 205 A110 110 0 0 1 280 205" fill="none" stroke="#0f172a" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/><path d="M44 205 H306 M170 205 V80" fill="none" stroke="#0f172a" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/><path d="M306 205 L298 209 L298 201 Z" fill="#0f172a"/><path d="M170 80 L174 88 L166 88 Z" fill="#0f172a"/><path d="M269.7 158.5 L269.7 205" fill="none" stroke="#94a3b8" stroke-width="1.3" stroke-dasharray="5 4" stroke-linecap="round" stroke-linejoin="round"/><path d="M70.3 158.5 L70.3 205" fill="none" stroke="#94a3b8" stroke-width="1.3" stroke-dasharray="5 4" stroke-linecap="round" stroke-linejoin="round"/><path d="M216.5 105.3 L216.5 205" fill="none" stroke="#94a3b8" stroke-width="1.3" stroke-dasharray="5 4" stroke-linecap="round" stroke-linejoin="round"/><path d="M70.3 158.5 L269.7 158.5" fill="none" stroke="#94a3b8" stroke-width="1.3" stroke-dasharray="5 4" stroke-linecap="round" stroke-linejoin="round"/><path d="M170 105.3 L216.5 105.3" fill="none" stroke="#94a3b8" stroke-width="1.3" stroke-dasharray="5 4" stroke-linecap="round" stroke-linejoin="round"/><path d="M170 205 L260.5 114.5" fill="none" stroke="#b45309" stroke-width="1.6" stroke-dasharray="7 4" stroke-linecap="round" stroke-linejoin="round"/><circle cx="269.7" cy="158.5" r="4.5" fill="#0f6e56"/><circle cx="70.3" cy="158.5" r="4.5" fill="#b45309"/><circle cx="216.5" cy="105.3" r="4.5" fill="#6d28d9"/><circle cx="170" cy="205" r="3.5" fill="#0f172a"/><g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.6" stroke-linejoin="round"><text x="283.7" y="152.5" text-anchor="middle" font-size="14" fill="#0f6e56">M</text><text x="56.3" y="152.5" text-anchor="middle" font-size="14" fill="#b45309">M′</text><text x="220.5" y="93.3" text-anchor="middle" font-size="14" fill="#6d28d9">N</text><text x="158" y="222" text-anchor="middle" font-size="14" fill="#0f172a">O</text><text x="70.3" y="224" text-anchor="middle" font-size="12" fill="#b45309">−cos α</text><text x="216.5" y="224" text-anchor="middle" font-size="12" fill="#6d28d9">sin α</text><text x="269.7" y="224" text-anchor="middle" font-size="12" fill="#0f6e56">cos α</text><text x="164" y="153.5" text-anchor="end" font-size="12" fill="#0f6e56">sin α</text><text x="164" y="109.3" text-anchor="end" font-size="12" fill="#6d28d9">cos α</text><text x="286.5" y="118.5" text-anchor="middle" font-size="12" fill="#b45309">y = x</text></g></svg>
:::

Sur la figure, M′ a la même ordonnée que M et l'abscisse opposée, donc AÔM′ = π − α. N, symétrique de M par rapport à la droite y = x, a pour abscisse l'ordonnée de M et pour ordonnée l'abscisse de M, et AÔN = π/2 − α.

::: exemple De 30° à 150° : lire cos, sin et tan de 5π/6

1. 5π/6 = π − π/6 : l'angle 150° est le supplémentaire de 30°, donc M′ est le symétrique du point M de π/6.
2. cos 5π/6 = −cos π/6 = −√3/2, car la symétrie change le signe de l'abscisse.
3. sin 5π/6 = sin π/6 = 1/2, car la symétrie conserve l'ordonnée.
4. tan 5π/6 = sin / cos = (1/2)/(−√3/2) = −√3/3 = −tan π/6.

:::

::: exemple Résoudre dans [0 ; π] l'équation 2 sin x = √2

1. sin x = √2/2, en divisant par 2.
2. La table donne sin π/4 = √2/2, donc x = π/4 est une solution.
3. L'angle π − π/4 = 3π/4 a le même sinus, car la symétrie conserve l'ordonnée : x = 3π/4 est aussi une solution.
4. Il n'y en a pas d'autre, car un seul point du demi-cercle de chaque côté de l'axe a cette ordonnée : S = {π/4 ; 3π/4}.

:::

::: piege Écrire cos(2π/3) = cos(π/3) comme pour le sinus
Un élève sait que sin(π − x) = sin x et en déduit cos(π − x) = cos x, donc cos 2π/3 = cos π/3 = 1/2. Cela tente parce que, pour le sinus, la valeur ne bouge pas.
Mais la symétrie par rapport à l'axe des ordonnées conserve l'ordonnée et change le signe de l'abscisse : cos(π − x) = −cos x, donc cos 2π/3 = −1/2. Un angle obtus a un cosinus négatif.
:::

::: propriete

- Angles supplémentaires, pour x dans [0 ; π] : cos(π − x) = −cos x et sin(π − x) = sin x ; tan(π − x) = −tan x si x ≠ π/2 ; cot(π − x) = −cot x si x ∈ ]0 ; π[.
- Angles complémentaires, pour x dans [0 ; π/2] : cos(π/2 − x) = sin x et sin(π/2 − x) = cos x ; tan(π/2 − x) = cot x si x ∈ ]0 ; π/2] et cot(π/2 − x) = tan x si x ∈ [0 ; π/2[.

Cas limite : une équation sin x = k, avec 0 < k < 1, a deux solutions dans [0 ; π], x et π − x ; une équation cos x = k, avec −1 ≤ k ≤ 1, n'en a qu'une.
:::

::: verifie
Résoudre dans [0 ; π] l'équation cos x = −√2/2.

---

cos x est négatif, donc x est obtus. L'angle π − x a pour cosinus −cos x = √2/2, et la table donne cos π/4 = √2/2, donc π − x = π/4 et x = 3π/4. Il n'y a qu'une solution, car un seul point du demi-cercle a cette abscisse : S = {3π/4}.
:::

::: retenir
Supplémentaires : cos(π − x) = −cos x et sin(π − x) = sin x. Complémentaires : cos(π/2 − x) = sin x et sin(π/2 − x) = cos x.
:::

## 🔺 La loi du sinus : relier les côtés aux angles opposés

Pour mesurer la largeur d'un lac, on ne peut pas tendre une corde en travers. Sur la rive, on mesure BC = 120 m, et de B puis de C on vise un îlot A : on trouve B̂ = 45° et Ĉ = 75°.
Comment obtenir la distance CA de l'îlot, alors que le triangle ABC n'est pas rectangle ?

::: figure Dans le triangle ABC, la hauteur CH se calcule de deux façons, dans les deux triangles rectangles ACH et BCH : CH = b sin Â et CH = a sin B̂
<svg viewBox="0 36 340 196"><path d="M60 205 L285 205 L150 65 Z" fill="#0f6e56" opacity="0.12"/><path d="M60 205 L285 205 L150 65 Z" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M150 65 L150 205" fill="none" stroke="#b45309" stroke-width="2" stroke-dasharray="6 4" stroke-linecap="round" stroke-linejoin="round"/><path d="M140 205 L140 195 L150 195" fill="none" stroke="#b45309" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/><path d="M88 205 A28 28 0 0 0 75.1 181.4" fill="none" stroke="#0f6e56" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M265.6 184.8 A28 28 0 0 0 257 205" fill="none" stroke="#0f6e56" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><circle cx="60" cy="205" r="4" fill="#0f172a"/><circle cx="285" cy="205" r="4" fill="#0f172a"/><circle cx="150" cy="65" r="4" fill="#0f172a"/><g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.6" stroke-linejoin="round"><text x="46" y="224" text-anchor="middle" font-size="14" fill="#0f172a">A</text><text x="299" y="224" text-anchor="middle" font-size="14" fill="#0f172a">B</text><text x="150" y="54" text-anchor="middle" font-size="14" fill="#0f172a">C</text><text x="152" y="224" text-anchor="middle" font-size="14" fill="#b45309">H</text><text x="108" y="195" text-anchor="middle" font-size="13" fill="#0f6e56">Â</text><text x="239" y="195" text-anchor="middle" font-size="13" fill="#0f6e56">B̂</text><text x="91" y="131" text-anchor="middle" font-size="15" fill="#0f6e56">b</text><text x="231.5" y="131" text-anchor="middle" font-size="15" fill="#0f6e56">a</text><text x="222" y="225" text-anchor="middle" font-size="15" fill="#0f6e56">c</text><text x="158" y="142" text-anchor="start" font-size="13" fill="#b45309">CH</text></g></svg>
:::

Sur la figure, a = BC, b = CA et c = AB sont les côtés opposés aux angles Â, B̂ et Ĉ ; dans le triangle ACH rectangle en H, CH est le côté opposé à Â, d'hypoténuse b ; dans BCH, CH est opposé à B̂, d'hypoténuse a.

::: exemple Le lac : trouver CA avec BC = 120 m, B̂ = 45° et Ĉ = 75°

1. Â = 180° − 45° − 75° = 60°, car la somme des angles d'un triangle vaut π.
2. La hauteur CH vaut b sin Â et aussi a sin B̂, d'après les deux triangles rectangles : b sin Â = a sin B̂.
3. b = a sin B̂ / sin Â = 120 × (√2/2)/(√3/2) = 120√2/√3 = 40√6, en gardant les valeurs exactes de la table.
4. CA = 40√6, soit environ 98,0 m.

:::

::: piege Associer chaque côté à l'angle voisin au lieu de l'angle opposé
Dans le lac, un élève écrit a / sin B̂ = b / sin Â et obtient b = 120 × (√3/2)/(√2/2) = 60√6, soit environ 147 m. Cela tente parce que le côté a = BC touche B, et que l'on associe « BC » au sommet B.
Mais chaque côté se divise par le sinus de l'angle en face de lui : a est en face de Â, b en face de B̂. La bonne écriture est a/sin Â = b/sin B̂, qui donne 40√6, soit environ 98 m.
:::

::: propriete
Dans tout triangle ABC, avec a = BC, b = CA, c = AB, et R le rayon du cercle circonscrit :

$$ a / sin Â = b / sin B̂ = c / sin Ĉ = 2R $$

Raison du dernier égal : si B′ est le point du cercle diamétralement opposé à B, le triangle BCB′ est rectangle en C et BB′ = 2R ; l'angle en B′ est égal à Â ou à π − Â (angles inscrits), donc sin Â = BC/BB′ = a/(2R).
Cas limite : la loi donne sin d'un angle, pas l'angle. Si b = 3, B̂ = π/6 et a = 3√3, alors sin Â = a sin B̂ / b = √3/2, donc Â = π/3 ou Â = 2π/3 ; les deux conviennent, car π/3 + π/6 et 2π/3 + π/6 sont inférieurs à π. Il faut un renseignement de plus pour choisir.
:::

::: verifie
Dans un triangle ABC, c = AB = 6, Ĉ = π/4 et Â = π/6. Calculer a = BC.

---

a est en face de Â et c est en face de Ĉ : a/sin Â = c/sin Ĉ. Donc a = c sin Â / sin Ĉ = 6 × (1/2)/(√2/2) = 6/√2 = 3√2, soit environ 4,24. On a bien mis chaque côté avec le sinus de l'angle opposé.
:::

::: verifie
Un triangle ABC a pour côté BC = 8 et pour angle Â = π/6. Quel est le rayon R de son cercle circonscrit ?

---

a/sin Â = 2R, donc 2R = 8 / sin π/6 = 8 / (1/2) = 16, car sin π/6 = 1/2, et R = 8. On a divisé par le sinus de l'angle opposé au côté BC, puis pris la moitié du diamètre.
:::

::: retenir
Dans tout triangle, a/sin Â = b/sin B̂ = c/sin Ĉ = 2R : chaque côté est divisé par le sinus de l'angle en face de lui, et la loi donne sin d'un angle, pas l'angle.
:::

## 📐 Aire d'un triangle : un angle remplace la hauteur

Un terrain triangulaire a deux côtés de 40 m et 50 m qui forment un angle de 30° ; la hauteur est impossible à mesurer à travers les broussailles. Comment calculer l'aire avec ce que l'on sait mesurer ?
Et si l'angle des deux côtés était obtus, la hauteur tomberait-elle encore dans le triangle ?

::: figure Quand l'angle Â est obtus (dessiné ici à 120°, à titre d'illustration), la hauteur h issue de C tombe hors du triangle, sur le prolongement de [BA] ; l'angle gris est le supplémentaire de Â, et h = b sin(π − Â) = b sin Â
<svg viewBox="0 36 340 204"><path d="M170 190 L40 190 L245 60.1 Z" fill="#0f6e56" opacity="0.12"/><path d="M170 190 L40 190 L245 60.1 Z" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M170 190 L245 190" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-dasharray="6 4" stroke-linecap="round" stroke-linejoin="round"/><path d="M245 60.1 L245 190" fill="none" stroke="#b45309" stroke-width="2.2" stroke-dasharray="6 4" stroke-linecap="round" stroke-linejoin="round"/><path d="M235 190 L235 180 L245 180" fill="none" stroke="#b45309" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/><path d="M183 167.5 A26 26 0 0 0 144 190" fill="none" stroke="#0f6e56" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M208 190 A38 38 0 0 0 189 157.1" fill="none" stroke="#94a3b8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><circle cx="170" cy="190" r="4" fill="#0f172a"/><circle cx="40" cy="190" r="4" fill="#0f172a"/><circle cx="245" cy="60.1" r="4" fill="#0f172a"/><circle cx="245" cy="190" r="3.5" fill="#b45309"/><g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.6" stroke-linejoin="round"><text x="166" y="210" text-anchor="middle" font-size="14" fill="#0f172a">A</text><text x="30" y="208" text-anchor="middle" font-size="14" fill="#0f172a">B</text><text x="247" y="50.1" text-anchor="middle" font-size="14" fill="#0f172a">C</text><text x="253" y="208" text-anchor="middle" font-size="14" fill="#b45309">H</text><text x="162" y="156" text-anchor="middle" font-size="13" fill="#0f6e56">Â</text><text x="105" y="210" text-anchor="middle" font-size="15" fill="#0f6e56">c</text><text x="191.5" y="125" text-anchor="middle" font-size="15" fill="#0f6e56">b</text><text x="261" y="125" text-anchor="middle" font-size="15" fill="#b45309">h</text></g></svg>
:::

Sur la figure, h est le côté opposé à l'angle gris dans le triangle rectangle AHC, d'hypoténuse b, donc h = b sin(π − Â) ; comme sin(π − Â) = sin Â, l'aire ½ × c × h s'écrit ½ c b sin Â.

::: exemple Le terrain : 40 m, 50 m et un angle de 30°

1. Les deux côtés forment l'angle de 30° : l'aire est ½ × 40 × 50 × sin 30°, car l'angle utilisé doit être celui des deux côtés.
2. sin 30° = 1/2, donc S = ½ × 40 × 50 × 1/2 = 500.
3. L'aire du terrain est 500 m².

:::

::: exemple Un angle obtus : deux côtés de 6 et 8 formant 135°

1. S = ½ × 6 × 8 × sin 135°, par la même formule.
2. sin 135° = sin(180° − 135°) = sin 45° = √2/2, car les angles supplémentaires ont le même sinus.
3. S = 24 × √2/2 = 12√2, soit environ 16,97.

:::

::: piege Oublier le ½ et prendre l'aire du parallélogramme
Sur le terrain, un élève écrit S = 40 × 50 × sin 30° = 1000 m². Cela tente parce que « base × hauteur » donne l'aire d'un rectangle, et que 50 sin 30° est bien une hauteur.
Mais 1000 m² est l'aire du parallélogramme construit sur les deux côtés ; le triangle en est la moitié. Il faut le ½ : S = 500 m².
:::

::: propriete
Dans le triangle ABC, avec a = BC, b = CA, c = AB, l'aire S vaut, avec l'angle compris entre les deux côtés utilisés :

$$ S = ½ bc sin Â = ½ ac sin B̂ = ½ ab sin Ĉ $$

En combinant avec la loi du sinus, sin Ĉ = c/(2R), donc S = abc/(4R).
Cas limite : si Â = π/2, sin Â = 1 et l'on retrouve S = ½ bc, la moitié du produit des côtés de l'angle droit.
:::

::: verifie
Un triangle ABC a AB = 7, AC = 8 et Â = π/3. Calculer son aire.

---

L'angle Â est compris entre les côtés AB et AC, donc S = ½ × 7 × 8 × sin π/3. Avec sin π/3 = √3/2, S = 28 × √3/2 = 14√3, soit environ 24,25. Le facteur ½ est bien présent.
:::

::: retenir
S = ½ bc sin Â, avec l'angle compris entre les deux côtés ; cela marche aussi pour un angle obtus, et en combinant avec la loi du sinus S = abc/(4R).
:::

## 🧭 Le théorème d'El-Kashi : Pythagore corrigé par l'angle

Deux sentiers partent du même point A d'une plage : l'un de 60 m, l'autre de 80 m. S'ils forment un angle droit, leurs extrémités sont distantes de 100 m, par Pythagore. Mais s'ils forment un angle de 60° ?
Comment calculer la distance BC entre les extrémités quand l'angle n'est pas droit ?

::: figure Dans le triangle ABC, la hauteur CH partage le côté [AB] : AH = b cos Â, HB = c − b cos Â et CH = b sin Â ; Pythagore dans BCH donnera a² en fonction de b, c et Â
<svg viewBox="0 36 340 228"><path d="M55 205 L285 205 L130 60 Z" fill="#0f6e56" opacity="0.12"/><path d="M55 205 L285 205 L130 60 Z" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M130 60 L130 205" fill="none" stroke="#b45309" stroke-width="2" stroke-dasharray="6 4" stroke-linecap="round" stroke-linejoin="round"/><path d="M120 205 L120 195 L130 195" fill="none" stroke="#b45309" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/><path d="M83 205 A28 28 0 0 0 67.9 180.1" fill="none" stroke="#0f6e56" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><circle cx="55" cy="205" r="4" fill="#0f172a"/><circle cx="285" cy="205" r="4" fill="#0f172a"/><circle cx="130" cy="60" r="4" fill="#0f172a"/><circle cx="130" cy="205" r="3.5" fill="#b45309"/><path d="M57 234 L128 234 M57 229 L57 239 M128 229 L128 239" fill="none" stroke="#0f6e56" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/><path d="M132 234 L283 234 M132 229 L132 239 M283 229 L283 239" fill="none" stroke="#0f6e56" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/><g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.6" stroke-linejoin="round"><text x="42" y="224" text-anchor="middle" font-size="14" fill="#0f172a">A</text><text x="299" y="224" text-anchor="middle" font-size="14" fill="#0f172a">B</text><text x="130" y="50" text-anchor="middle" font-size="14" fill="#0f172a">C</text><text x="130" y="224" text-anchor="middle" font-size="14" fill="#b45309">H</text><text x="107" y="196" text-anchor="middle" font-size="13" fill="#0f6e56">Â</text><text x="78.5" y="130.5" text-anchor="middle" font-size="15" fill="#0f6e56">b</text><text x="221.5" y="128.5" text-anchor="middle" font-size="15" fill="#0f6e56">a</text><text x="140" y="136.5" text-anchor="start" font-size="12" fill="#b45309">b sin Â</text><text x="92.5" y="254" text-anchor="middle" font-size="12" fill="#0f6e56">b cos Â</text><text x="207.5" y="254" text-anchor="middle" font-size="12" fill="#0f6e56">c − b cos Â</text></g></svg>
:::

Sur la figure, a est l'hypoténuse du triangle BCH rectangle en H, donc a² = CH² + HB² ; or CH = b sin Â et HB = c − b cos Â, deux côtés que le triangle ACH, rectangle en H, donne à partir de b et de l'angle Â.

::: exemple Les sentiers de 60 m et 80 m formant 60°

1. a² = 60² + 80² − 2 × 60 × 80 × cos 60°, car l'angle Â des deux sentiers est entre les côtés b et c.
2. cos 60° = 1/2, donc a² = 3600 + 6400 − 9600 × 1/2 = 10 000 − 4800 = 5200.
3. a = √5200 = 20√13, soit environ 72,1 m, nettement moins que les 100 m de l'angle droit, ce qui est cohérent : en refermant l'angle, on rapproche les extrémités.

:::

::: exemple Un angle obtus : b = 3, c = 5 et Â = 2π/3

1. a² = 3² + 5² − 2 × 3 × 5 × cos 2π/3, par le théorème.
2. cos 2π/3 = −cos π/3 = −1/2 (angles supplémentaires), donc a² = 9 + 25 − 30 × (−1/2) = 34 + 15 = 49.
3. a = 7. Le terme −2bc cos Â est ici positif, parce que cos Â est négatif : le côté opposé à un angle obtus dépasse ce que donnerait Pythagore.

:::

::: piege Écrire +2bc cos Â au lieu de −2bc cos Â
Pour les sentiers, un élève écrit a² = 3600 + 6400 + 9600 × 1/2 = 14 800 et trouve a ≈ 121,7 m. Cela tente parce que, dans (b + c)², le double produit s'ajoute.
Mais le signe est un moins : on retrouve ainsi Pythagore à 90° sans changer de forme, et l'on obtient 72,1 m. Un contrôle simple : refermer l'angle de 90° à 60° ne peut pas éloigner les extrémités, alors que 121,7 m dépasse 100 m.
:::

::: propriete
Dans tout triangle ABC, avec a = BC, b = CA, c = AB :

$$ a² = b² + c² − 2bc cos Â $$

On a de même b² = a² + c² − 2ac cos B̂ et c² = a² + b² − 2ab cos Ĉ. Réciproquement, cos Â = (b² + c² − a²)/(2bc), ce qui donne un angle à partir des trois côtés.
Cas limite : si Â = π/2, cos Â = 0 et l'on retrouve a² = b² + c² (Pythagore) ; si Â est obtus, cos Â < 0 et a² > b² + c².
:::

::: verifie
Un triangle ABC a pour côtés AB = 7, AC = 8 et BC = 13. Calculer l'angle Â.

---

Â est l'angle en face du côté BC = 13 : cos Â = (7² + 8² − 13²)/(2 × 7 × 8) = (49 + 64 − 169)/112 = −56/112 = −1/2. Comme cos 2π/3 = −1/2 et qu'un seul angle de [0 ; π] a ce cosinus, Â = 2π/3. Le cosinus négatif annonce bien un angle obtus.
:::

::: retenir
a² = b² + c² − 2bc cos Â, où Â est l'angle compris entre les côtés b et c ; c'est Pythagore quand Â = π/2, et la formule se lit à l'envers pour trouver un angle.
:::

> 🗡️ Culture mathématique : le théorème de cette dernière étape porte le nom d'**Al-Kashi**, astronome et mathématicien mort vers 1430 à Samarcande, directeur de l'observatoire de la ville et auteur de tables astronomiques. Il calcula aussi π avec 16 décimales.

> 🏆 Quête franchie, héros : tu sais lire cosinus et sinus sur le demi-cercle, retrouver les valeurs de π/6, π/4 et π/3, calculer tangente et cotangente, utiliser les relations fondamentales et les angles supplémentaires ou complémentaires, puis mesurer n'importe quel triangle avec la loi du sinus, la formule de l'aire et le théorème d'El-Kashi. Les prochaines portes ouvrent sur la géométrie analytique.
