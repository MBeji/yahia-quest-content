# ⚔️ Rotations — faire tourner le plan autour d'un point

> 💡 «Une rotation ne déforme rien : elle déplace la figure entière sans changer une seule longueur ni un seul angle. Tout l'art consiste à repérer le centre autour duquel tout tourne.»

Tu as appris à faire glisser le plan, puis à l'agrandir. Il reste le troisième geste, celui de la clé dans la serrure et de l'aiguille sur le cadran : **faire tourner**. Une rotation demande trois renseignements, jamais deux — un **centre**, un **angle** et un **sens**. Et parce qu'elle ne change aucune distance, elle transporte les figures telles quelles : c'est l'outil qui démontre en trois lignes des alignements et des égalités de longueurs qu'un calcul direct rendrait pénibles.

Mais avant de faire tourner quoi que ce soit, il faut une unité d'angle taillée pour la mesure : le **radian**.

## 📏 Mesurer un angle autrement : le radian

Trace un cercle de centre O et de rayon r, puis deux demi-droites issues de O. Elles découpent sur le cercle un arc de longueur L. Si tu doubles l'angle, l'arc double : la longueur de l'arc est **proportionnelle** à la mesure de l'angle qui l'intercepte.

L'idée décisive est ailleurs. Recommence sur un cercle plus grand, de rayon r′ : l'arc L′ est plus long, mais le **rapport** L′/r′ est exactement le même que L/r. Ce rapport ne dépend donc plus du cercle choisi : il ne dépend que de l'angle. On tient là une mesure d'angle.

> **Vocabulaire (encadré officiel).** Le rapport **L/r** est une **mesure en radians** de l'angle AÔB.

::: figure Le même angle α intercepte l'arc L sur le cercle de rayon r et l'arc L′ sur le cercle de rayon r′ : les deux rapports L/r et L′/r′ sont égaux, et cette valeur commune est la mesure de α en radians
<svg viewBox="0 0 320 260">
<path d="M60 190 L300 190" fill="none" stroke="#0f172a" stroke-width="2"/>
<path d="M60 190 L243.85 35.73" fill="none" stroke="#0f172a" stroke-width="2"/>
<path d="M150 190 A 90 90 0 0 0 128.94 132.15" fill="none" stroke="#0f6e56" stroke-width="3"/>
<path d="M220 190 A 160 160 0 0 0 182.57 87.15" fill="none" stroke="#0f6e56" stroke-width="3"/>
<g fill="#0f172a"><circle cx="60" cy="190" r="4.5"/></g>
<g fill="none" stroke="#94a3b8" stroke-width="1.4">
<path d="M60 204 L60 212 M150 204 L150 212 M60 208 L150 208"/>
<path d="M60 224 L60 232 M220 224 L220 232 M60 228 L220 228"/>
</g>
<g font-size="15" font-weight="700" text-anchor="middle" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">
<text x="48" y="184" fill="#0f172a">O</text>
<text x="158" y="152" fill="#0f6e56">L</text>
<text x="228" y="128" fill="#0f6e56">L′</text>
<text x="100" y="180" fill="#0f172a">α</text>
<text x="105" y="224" fill="#94a3b8">r</text>
<text x="140" y="246" fill="#94a3b8">r′</text>
</g>
</svg>
:::

Deux mesures se lisent alors immédiatement sur la figure du demi-cercle, et ce sont les deux repères à connaître par cœur.

> **Retenir (les deux angles de référence).** L'angle **plat** a pour mesure **π radians** ; l'angle **droit** a pour mesure **π/2 radians**. On écrit le plus souvent π, π/2, 2π/3 au lieu de π rad, π/2 rad, 2π/3 rad.

De ces deux repères découle toute la conversion : puisque 180° et π radians désignent le même angle plat, on passe d'une unité à l'autre par une simple règle de trois.

| angle en degrés | 180° | 90°  | 60°  | 45°  | 30°  | 150° | 72°   |
| --------------- | ---- | ---- | ---- | ---- | ---- | ---- | ----- |
| angle en radians | π    | π/2  | π/3  | π/4  | π/6  | 5π/6 | 2π/5  |

_Exemple détaillé_ : convertissons 150° en radians. On multiplie par π/180 :

$$ 150 × π/180 = 150π/180 = 5π/6 $$

_Exemple détaillé (dans l'autre sens)_ : convertissons 3π/10 radians en degrés. On multiplie cette fois par 180/π, et le π disparaît :

$$ (3π/10) × (180/π) = 3 × 18 = 54° $$

> ⚠️ Le facteur de conversion est **180**, pas 360 : c'est l'angle **plat** qui vaut π, pas le tour complet. Convertir π/8 en écrivant 360/8 = 45° est l'erreur la plus fréquente du chapitre ; la bonne réponse est 180/8 = 22,5°.

Enfin, la définition se relit à l'envers et donne la longueur d'un arc sans aucune formule nouvelle.

> **Retenir (longueur d'un arc).** Sur un cercle de rayon r, l'arc intercepté par un angle au centre de mesure α **en radians** a pour longueur **L = r × α**.

_Exemple détaillé_ : sur un cercle de rayon 6 cm, l'angle au centre de mesure π/3 intercepte un arc de longueur 6 × π/3 = 2π cm, soit environ 6,3 cm. Et pour α = π, on retrouve L = 6π cm, la moitié du périmètre : c'est bien un demi-cercle.

## 🌀 La rotation : un centre, un angle, un sens

Décalque un triangle équilatéral ABC de centre O, plante ta pointe de compas en O et fais tourner le calque jusqu'à amener A sur B. Chaque point du calque a bougé, sauf un : le point O. Et aucune longueur n'a changé, puisque le calque est rigide. Voilà toute la rotation.

Reste à préciser dans quel sens on a tourné. Le **sens direct** est le sens **contraire des aiguilles d'une montre** ; le **sens indirect** est celui des aiguilles d'une montre. Cette précision n'est pas un détail : à partir d'un point M donné, il existe **deux** points situés à la même distance de O et faisant l'angle voulu, un de chaque côté.

> **Définition (rotation directe, rotation indirecte).** Soient O un point du plan et α un réel appartenant à **]0 ; π[**. L'application du plan dans le plan qui laisse invariant le point O et qui, à tout point M distinct de O, associe le point M′ tel que
>
> $$ OM′ = OM et MÔM′ = α $$
>
> l'angle étant mesuré dans le **sens direct**, est appelée la **rotation directe de centre O et d'angle α**. En mesurant l'angle dans le **sens indirect**, on définit de même la **rotation indirecte de centre O et d'angle α**.

::: figure Rotation directe de centre O et d'angle α : le point M′ est à la même distance de O que M — les deux traits marquent l'égalité OM′ = OM — et l'angle MÔM′ vaut α, parcouru dans le sens direct, contraire des aiguilles d'une montre
<svg viewBox="0 0 330 230">
<path d="M150 180 L263.25 160.03 M150 180 L179.76 68.92" fill="none" stroke="#0f172a" stroke-width="2"/>
<path d="M204.16 170.45 A 55 55 0 0 0 164.24 126.87" fill="none" stroke="#0f6e56" stroke-width="2.4"/>
<polygon points="164.24,126.87 173.97,125.34 171.9,133.06" fill="#0f6e56"/>
<g fill="none" stroke="#0f172a" stroke-width="2">
<path d="M237.47 159.5 L239.21 169.34"/>
<path d="M168.38 92.06 L178.04 94.64"/>
</g>
<g fill="#0f172a"><circle cx="150" cy="180" r="4.5"/><circle cx="263.25" cy="160.03" r="4.5"/></g>
<circle cx="179.76" cy="68.92" r="5" fill="#0f6e56"/>
<g font-size="15" font-weight="700" text-anchor="middle" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">
<text x="142" y="198" fill="#0f172a">O</text>
<text x="276" y="154" fill="#0f172a">M</text>
<text x="190" y="60" fill="#0f6e56">M′</text>
<text x="185" y="158" fill="#0f6e56">α</text>
</g>
</svg>
:::

Deux rotations reviennent si souvent qu'elles ont reçu un nom propre.

> **Vocabulaire.** La rotation d'angle **π/2** s'appelle un **quart de tour** (direct ou indirect selon le sens) ; la rotation d'angle **π** s'appelle un **demi-tour**.

> ⚠️ Ne confonds pas l'**angle de la rotation** et les **angles de la figure**. L'angle α est la donnée qui décrit le mouvement ; les angles du triangle qu'on fait tourner, eux, ne bougent pas d'un degré. Faire tourner de π/4 un angle de π/3 ne donne pas π/3 + π/4 : cela donne π/3, ailleurs.

> 🗡️ Ici, l'angle d'une rotation est toujours un réel de **]0 ; π[**, et c'est le **mot** « directe » ou « indirecte » qui porte le sens — jamais un signe. Une « rotation d'angle −π/3 » ou « d'angle 4π/3 » n'a pas de sens dans ce chapitre : la première s'écrit « rotation indirecte d'angle π/3 », et la seconde se remplace par la rotation indirecte d'angle 2π/3, qui amène au même endroit.

## 🧭 Cas limites, antécédent et unicité

Aux deux bords de l'intervalle ]0 ; π[, la rotation se confond avec une transformation déjà connue.

> **Remarques (encadré officiel).** La rotation directe ou indirecte de centre O et d'angle **π** est la **symétrie centrale de centre O** — dans ce cas seul, le sens ne change rien. La rotation directe ou indirecte d'angle **nul** est l'**identité** du plan. Enfin, si r est une rotation, tout point M′ possède un **unique** antécédent M tel que r(M) = M′.

_Exemple détaillé_ : le demi-tour de centre O envoie M sur le point M′ tel que OM′ = OM et MÔM′ = π, c'est-à-dire tel que O soit le milieu de [MM′]. C'est mot pour mot la définition du symétrique de M par rapport à O.

L'unicité de l'antécédent a une conséquence pratique : une rotation ne « colle » jamais deux points l'un sur l'autre, et l'on peut toujours remonter d'une figure image à la figure de départ. Elle s'accompagne d'un second résultat d'unicité, plus utile encore, qui sert à **identifier** une rotation à partir d'un seul couple de points.

> **Retenir (existence et unicité).** Étant donné trois points distincts O, A et B tels que **OA = OB**, il existe **une unique** rotation r de centre O telle que **r(A) = B**.

L'égalité OA = OB est indispensable : une rotation conserve les distances au centre, donc si OA ≠ OB, aucune rotation de centre O ne peut envoyer A sur B. Et lorsqu'elle est vérifiée, il n'y a **pas** deux solutions : l'angle géométrique AÔB fixe la mesure, et le sens est imposé par la position de B — l'un des deux sens amène sur B, l'autre non.

_Exemple détaillé_ : A et B sont deux points d'un cercle de centre O tels que l'angle AÔB mesure π/2, et B se trouve à un quart de tour de A dans le sens contraire des aiguilles d'une montre. La rotation cherchée est alors le **quart de tour direct** de centre O — et c'est la seule. Le quart de tour indirect, lui, enverrait A sur le point diamétralement opposé à B.

## 🛡️ Ce qu'une rotation conserve

Une rotation déplace une figure rigide : rien de ce qui se mesure à l'intérieur de la figure ne change. Le tableau ci-dessous récapitule les conservations à connaître ; toutes se démontrent de la même façon, en revenant à l'égalité des distances au centre.

| ce qui est conservé            | conséquence directe                                            |
| ------------------------------ | -------------------------------------------------------------- |
| les **distances**              | A′B′ = AB : la figure image est isométrique                    |
| les **angles**                 | un angle de mesure θ garde la mesure θ                         |
| l'**orthogonalité**            | deux droites perpendiculaires ont des images perpendiculaires  |
| l'**alignement**               | trois points alignés ont des images alignées                   |
| le **milieu**                  | l'image du milieu de [AB] est le milieu de [A′B′]              |
| le **barycentre**              | l'image du barycentre est le barycentre des images, mêmes coefficients |
| le **parallélisme**            | deux droites parallèles ont des images parallèles              |
| le **contact**                 | une tangente à un cercle a pour image une tangente au cercle image |
| les **aires** et les périmètres | la figure et son image sont **superposables**                  |

> 🗡️ La conservation du barycentre est la plus rentable en exercice : elle offre gratuitement l'image du centre de gravité d'un triangle, puisque celui-ci est l'isobarycentre des trois sommets. L'image du centre de gravité de ABC est donc le centre de gravité de A′B′C′.

_Exemple détaillé_ : une rotation transforme le triangle ABC en A′B′C′, avec AB = 7 cm et l'angle BÂC de mesure π/3. Alors A′B′ = 7 cm et l'angle B′Â′C′ mesure encore π/3, **quel que soit** l'angle de la rotation. Si de plus l'aire de ABC vaut 15 cm², celle de A′B′C′ vaut 15 cm².

> ⚠️ Une rotation conserve les distances : c'est ce qui la sépare radicalement d'un agrandissement. Aucun coefficient ne vient multiplier les longueurs, ni leur carré multiplier les aires.

## 📐 Images des figures usuelles

Les conservations précédentes se traduisent en un catalogue d'images, qu'il faut savoir citer sans hésiter.

> **Retenir (encadré officiel).** Par une rotation : l'image d'un **segment** est un segment **isométrique** ; l'image d'une **droite** est une **droite** ; l'image d'un **cercle** de centre I et de rayon R est le cercle de centre r(I) et de **même rayon R** ; l'image d'un **triangle** est un triangle **isométrique**. Une figure et son image sont **superposables** : même périmètre, même aire, angles homologues isométriques.

Un cas mérite d'être isolé, parce qu'il donne un résultat que rien d'autre ne fournit aussi vite.

> **Retenir (le quart de tour).** L'image d'une droite (D) par un **quart de tour** est une droite **perpendiculaire** à (D).

::: figure Image d'une droite par le quart de tour direct de centre O : le point A a pour image A′, à la même distance de O, et la droite image (D′) est perpendiculaire à (D) — l'angle droit est marqué à leur intersection
<svg viewBox="0 0 330 250">
<path d="M40 70 L305 70" fill="none" stroke="#0f172a" stroke-width="2.4"/>
<path d="M80 25 L80 230" fill="none" stroke="#0f6e56" stroke-width="2.4"/>
<path d="M92 70 L92 82 L80 82" fill="none" stroke="#0f172a" stroke-width="2"/>
<path d="M230 70 A 106.3 106.3 0 0 0 80 60" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-dasharray="5 4"/>
<path d="M150 140 L230 70 M150 140 L80 60" fill="none" stroke="#94a3b8" stroke-width="1.4"/>
<g fill="#0f172a"><circle cx="150" cy="140" r="4.5"/><circle cx="230" cy="70" r="4.5"/></g>
<circle cx="80" cy="60" r="5" fill="#0f6e56"/>
<g font-size="15" font-weight="700" text-anchor="middle" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">
<text x="160" y="158" fill="#0f172a">O</text>
<text x="240" y="60" fill="#0f172a">A</text>
<text x="64" y="48" fill="#0f6e56">A′</text>
<text x="288" y="60" fill="#0f172a">(D)</text>
<text x="104" y="224" fill="#0f6e56">(D′)</text>
</g>
</svg>
:::

_Exemple détaillé_ : le cercle de centre I et de rayon 3 cm a pour image, par la rotation directe de centre O et d'angle π/4, le cercle de centre r(I) et de rayon **3 cm**. Le centre se déplace, le rayon ne bouge pas — c'est exactement ce que dit la conservation des distances, appliquée aux distances entre le centre et les points du cercle.

## 🔁 Figures globalement invariantes, centre et axe de symétrie

Jusqu'ici on suivait un point à la trace. Changeons de point de vue et regardons une figure **entière** : il arrive qu'elle retombe sur elle-même, même si chacun de ses points a bougé.

> **Définitions (encadré officiel).** On dit qu'une figure est **globalement invariante** par une application du plan si son image par cette application est **elle-même**. On dit qu'un point I est un **centre de symétrie** d'une figure si cette figure est globalement invariante par la symétrie centrale de centre I. On dit qu'une droite D est un **axe de symétrie** d'une figure si cette figure est globalement invariante par la symétrie axiale d'axe D.

::: figure Le triangle équilatéral ABC de centre O est globalement invariant par la rotation directe d'angle 2π/3 : elle envoie A sur B, B sur C et C sur A, si bien que le triangle tout entier retombe sur lui-même
<svg viewBox="0 0 320 240">
<polygon points="160,40 73.4,190 246.6,190" fill="#0f6e56" opacity="0.10"/>
<polygon points="160,40 73.4,190 246.6,190" fill="none" stroke="#0f172a" stroke-width="2.2"/>
<path d="M160 85 A 55 55 0 0 0 112.37 167.5" fill="none" stroke="#0f6e56" stroke-width="2.4"/>
<polygon points="112.37,167.5 111.33,157.71 104.41,161.71" fill="#0f6e56"/>
<g fill="#0f172a"><circle cx="160" cy="40" r="4.5"/><circle cx="73.4" cy="190" r="4.5"/><circle cx="246.6" cy="190" r="4.5"/><circle cx="160" cy="140" r="4"/></g>
<g font-size="15" font-weight="700" text-anchor="middle" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">
<text x="160" y="30" fill="#0f172a">A</text>
<text x="60" y="206" fill="#0f172a">B</text>
<text x="260" y="206" fill="#0f172a">C</text>
<text x="174" y="146" fill="#0f172a">O</text>
<text x="126" y="116" fill="#0f6e56">2π/3</text>
</g>
</svg>
:::

Un même objet cumule souvent plusieurs éléments de symétrie. Le carré est le cas le plus riche du programme.

::: figure Les éléments de symétrie du carré : son centre O, et ses quatre axes en pointillés — les deux médiatrices des côtés et les deux diagonales. Il est de plus globalement invariant par le quart de tour de centre O
<svg viewBox="0 0 320 240">
<polygon points="85,55 235,55 235,205 85,205" fill="#0f6e56" opacity="0.10"/>
<polygon points="85,55 235,55 235,205 85,205" fill="none" stroke="#0f172a" stroke-width="2.2"/>
<g fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-dasharray="6 4">
<path d="M160 37 L160 223"/>
<path d="M67 130 L253 130"/>
<path d="M72.27 42.27 L247.73 217.73"/>
<path d="M247.73 42.27 L72.27 217.73"/>
</g>
<circle cx="160" cy="130" r="5" fill="#0f6e56"/>
<g font-size="15" font-weight="700" text-anchor="middle" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">
<text x="174" y="126" fill="#0f6e56">O</text>
</g>
</svg>
:::

> **Retenir (les éléments de symétrie usuels).** Une **droite** est son propre axe de symétrie, et **tout** point de cette droite en est un centre de symétrie. Un **cercle** de centre O admet O pour centre de symétrie et **toute** droite passant par O pour axe de symétrie. Un **carré** de centre O admet O pour centre de symétrie et **quatre** axes de symétrie. Un **triangle équilatéral** admet **trois** axes de symétrie mais **aucun** centre de symétrie.

_Exemple détaillé_ : cherchons tous les réels α de ]0 ; π[ tels que le carré de centre O soit globalement invariant par la rotation directe de centre O et d'angle α. Un sommet doit se poser sur un sommet, et les sommets ne sont espacés que de quarts de tour. Le quart de tour direct fait glisser chaque sommet sur le suivant : le carré retombe sur lui-même, donc α = π/2 convient. Aucune autre valeur de l'intervalle ne marche. La seule valeur cherchée est donc **π/2**.

> 🗡️ **Et le demi-tour ?** Il échange bien chaque sommet avec le sommet opposé, donc il laisse lui aussi le carré invariant — mais **π n'appartient pas à ]0 ; π[**, l'intervalle ouvert où ce chapitre définit l'angle d'une rotation. Le demi-tour est le cas de bord : c'est la **symétrie centrale de centre O**, une transformation déjà connue, et c'est exactement ce que veut dire « le carré admet O pour centre de symétrie ». Répondre « π/2 et π » à la question posée, c'est sortir de l'intervalle qu'elle donne.

> ⚠️ Un triangle équilatéral est globalement invariant par la rotation d'angle 2π/3, mais il n'a pas de centre de symétrie : le demi-tour de centre O ne le laisse pas invariant, il le retourne. Avoir un centre de rotation invariant et avoir un centre de symétrie sont deux choses différentes.

## 👑 Aller plus loin : trois configurations qui tombent par rotation

**Un alignement démontré sans calcul.** Lorsqu'une figure contient un triangle équilatéral ou un carré, la rotation qui le laisse globalement invariant transporte d'un coup toute une portion de la figure. Deux longueurs égales apparaissent, deux droites perpendiculaires aussi si l'angle est droit, et l'alignement de trois points se lit comme la somme de deux angles valant π. C'est la méthode que suivent les configurations classiques du chapitre : carrés construits sur les côtés d'un triangle, triangles équilatéraux dressés sur les côtés d'un carré.

**L'égalité MA + MB = MC.** Voici le plus joli résultat que la rotation donne au niveau de ce chapitre.

> **Retenir (enrichissement).** Soit ABC un triangle équilatéral inscrit dans un cercle Γ, et soit M un point de Γ situé sur l'**arc AB ne contenant pas C**. Alors **MC = MA + MB**.

La démonstration tient en trois pas et n'utilise que ce chapitre. Comme M et C sont de part et d'autre de la corde [AB], l'angle AMB vaut π − π/3 = 2π/3. On considère alors la rotation r de centre A et d'angle π/3 qui envoie B sur C, et on pose M′ = r(M). D'une part AM′ = AM et l'angle MAM′ vaut π/3 : le triangle AMM′ est isocèle avec un angle de π/3, donc **équilatéral**, d'où MM′ = MA. D'autre part r envoie le segment [MB] sur [M′C], donc M′C = MB. Enfin les angles se recollent : l'angle AM′C vaut 2π/3 comme son antécédent AMB, et l'angle AM′M vaut π/3, dont la somme fait π — les points M, M′ et C sont **alignés**. On conclut : MC = MM′ + M′C = MA + MB.

**Le point de Toricelli.** Dans un triangle dont les angles sont tous inférieurs à 2π/3, on cherche le point P qui rend la somme PA + PB + PC **minimale**. Une rotation directe d'angle π/3 et de centre B transforme la ligne brisée formée par les trois segments en une ligne brisée de même longueur, joignant deux points fixes : elle est la plus courte lorsqu'elle est **droite**. Le point cherché est donc celui qui voit les trois côtés sous le même angle : APB = APC = BPC = **2π/3**. Ce point porte le nom de **point de Toricelli**.

> 🗡️ Culture mathématique : les **carrés magiques** — ces tableaux 3 × 3 remplis des entiers de 1 à 9 dont chaque ligne, chaque colonne et chaque diagonale totalisent 15 — ont occupé les mathématiciens de la Chine antique à la Renaissance, en passant par Ibn Al Haytham, Abul Wafa Busjani et le mathématicien tunisien **Ibn Al Khatib**. On en connaît huit ; et l'on passe de l'un à l'autre exactement par les applications du plan qui laissent le carré globalement invariant. Quant au nombre central, il est nécessairement 5.

> 🏆 Quête franchie, héros : tu sais convertir un angle en radians, calculer la longueur d'un arc, construire l'image d'un point par une rotation directe ou indirecte, reconnaître le demi-tour et le quart de tour, citer tout ce qu'une rotation conserve, donner l'image d'un segment, d'une droite et d'un cercle, et repérer les éléments de symétrie d'une figure. Le prochain gate quitte la géométrie : on y suivra des nombres qui se succèdent selon une règle, les **suites**.
