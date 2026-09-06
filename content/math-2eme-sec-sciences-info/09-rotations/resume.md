# 📜 Résumé : Rotations

- **Le radian** : sur un cercle de rayon r, un angle au centre intercepte un arc de longueur L, et le rapport **L/r** ne dépend pas du rayon choisi — c'est la **mesure en radians** de cet angle. Repères : l'angle **plat** vaut **π**, l'angle **droit** vaut **π/2**.
- **Conversions** : on multiplie par **π/180** pour aller des degrés aux radians, par **180/π** pour revenir. Exemples : 150° = 5π/6 ; 72° = 2π/5 ; 3π/10 = 54° ; π/8 = 22,5°. Le facteur est **180**, jamais 360.
- **Longueur d'un arc** : **L = r × α**, avec α **en radians**. Exemple : r = 6 cm et α = π/3 donnent L = 2π cm.
- **Définition** : pour O un point et α ∈ **]0 ; π[**, la **rotation directe de centre O et d'angle α** laisse O invariant et associe à tout point M ≠ O le point M′ tel que **OM′ = OM** et **MÔM′ = α**, l'angle étant parcouru dans le **sens direct** (contraire des aiguilles d'une montre). Le sens des aiguilles d'une montre donne la **rotation indirecte**.

::: figure Les trois données d'une rotation se lisent sur cette figure : le centre O, qui ne bouge pas ; l'égalité des distances OM′ = OM ; et l'angle α parcouru dans le sens direct
<svg viewBox="0 0 220 160">
<path d="M95 110 L164.73 103.9 M95 110 L107.16 41.06" fill="none" stroke="#0f172a" stroke-width="2"/>
<path d="M128.87 107.04 A 34 34 0 0 0 100.9 76.52" fill="none" stroke="#0f6e56" stroke-width="2.2"/>
<polygon points="100.9,76.52 108.17,81.36 109.39,74.46" fill="#0f6e56"/>
<g fill="#0f172a"><circle cx="95" cy="110" r="4"/><circle cx="164.73" cy="103.9" r="4"/></g>
<circle cx="107.16" cy="41.06" r="4.5" fill="#0f6e56"/>
<g font-size="14" font-weight="700" text-anchor="middle" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">
<text x="86" y="126" fill="#0f172a">O</text>
<text x="176" y="100" fill="#0f172a">M</text>
<text x="116" y="32" fill="#0f6e56">M′</text>
<text x="113" y="102" fill="#0f6e56">α</text>
</g>
</svg>
:::

- **Vocabulaire** : la rotation d'angle **π/2** est un **quart de tour** ; celle d'angle **π** est un **demi-tour**. L'angle est toujours pris dans ]0 ; π[ et le **sens** est porté par le mot « directe » ou « indirecte », jamais par un signe.
- **Cas limites** : la rotation d'angle **π** est la **symétrie centrale de centre O** (le sens n'y change rien) ; la rotation d'angle **nul** est l'**identité**. Tout point M′ admet un **unique** antécédent.
- **Unicité** : si O, A, B sont distincts avec **OA = OB**, il existe **une seule** rotation de centre O telle que r(A) = B — l'angle géométrique donne la mesure, la position de B impose le sens.
- **Conservations** : une rotation conserve les **distances**, les **angles** (donc l'**orthogonalité**), l'**alignement**, le **milieu**, le **barycentre**, le **parallélisme**, le **contact** et les **aires**. Une figure et son image sont **superposables**. Conséquence utile : l'image du centre de gravité de ABC est le centre de gravité de A′B′C′.
- **Images des figures usuelles** : segment → segment **isométrique** ; droite → droite ; cercle de centre I et de rayon R → cercle de centre r(I) et de **même rayon R** ; triangle → triangle isométrique. Cas à part : par un **quart de tour**, l'image d'une droite lui est **perpendiculaire**.
- **Figures globalement invariantes** : une figure est globalement invariante par une application si son image est **elle-même**. Un **centre de symétrie** est un point I tel que la figure soit invariante par la symétrie centrale de centre I ; un **axe de symétrie** est une droite D telle qu'elle soit invariante par la symétrie axiale d'axe D.
- **Éléments de symétrie usuels** : un **cercle** de centre O a O pour centre de symétrie et **toutes** les droites passant par O pour axes ; un **carré** de centre O a O pour centre et **quatre** axes, et il est invariant par les rotations d'angle **π/2 et π** ; un **triangle équilatéral** a **trois** axes, **aucun** centre, et il est invariant par la rotation d'angle **2π/3**.
- **Enrichissement** : si ABC est équilatéral inscrit dans un cercle Γ et si M appartient à l'arc AB ne contenant pas C, alors **MC = MA + MB** (rotation de centre A et d'angle π/3). Le **point de Toricelli**, qui minimise PA + PB + PC, voit les trois côtés sous l'angle **2π/3**.
