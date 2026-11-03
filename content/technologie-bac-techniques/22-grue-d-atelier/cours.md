# 🏗️ La grue d'atelier : une flèche tirée et pliée, puis la synthèse du thème

> 💡 « Une flèche de grue ne casse pas parce qu'on la tire, ni parce qu'on la plie : elle casse parce qu'on fait les deux en même temps. Ce chapitre apprend à les additionner, puis range tout le thème en quelques lignes. »

Ce chapitre clôt le thème **Comportement des solides déformables**, après la torsion, la flexion et la flexion–torsion. Le support est une **grue d'atelier hydraulique** : un **vérin** pousse une **flèche extensible**, qui lève une charge de 250 kg au plus. Le dossier technique donne une flèche extensible à trois longueurs (895 à 1 685 mm) et un vérin double effet de course 495 mm (de 670 à 1 165 mm de longueur, soit 1 165 − 670 = 495). Le manuel étudie la flèche dans la **position la plus haute**, à sa **longueur maximale**, et demande de choisir son tube dans un catalogue.

Le chapitre a deux parties. Les sections 1 à 6 suivent l'activité de la grue : le modèle et les efforts extérieurs, les efforts de cohésion, les diagrammes, le tube carré, la superposition des contraintes, le choix de la section. Les sections 7 et 8 reprennent la **synthèse du thème** : torsion et flexion simples, puis sollicitations composées et choix de la bonne condition. Quelques lettres changent de sens d'un chapitre à l'autre, et le texte dit chaque fois laquelle : **θ** est ici l'**inclinaison de la flèche** (38°), non l'angle unitaire de torsion ; **N** est l'**effort normal** (non une vitesse de rotation) ; **T** seul est l'**épaisseur** du tube, alors que **Ty** est l'effort tranchant ; **B** désigne le **point B** de la flèche et, dans « B × B × T », le **côté extérieur** du tube. **Mfz** est le moment fléchissant Mf des chapitres précédents, noté avec son axe z.

> 🗡️ Le manuel ne donne **aucun corrigé** : toutes ses cases sont vides, et son dessin d'ensemble n'est pas reproduit. Ce cours n'enseigne donc que des règles standard de génie mécanique, et il dit ce qui vient du manuel (β = 51°, θ = 38°, AC = 1 685 mm, AB = 420 mm, P = 2 500 N, Fv = 10 170 N, les trois tubes 70 × 70 × 5, 80 × 80 × 5 et 90 × 90 × 5, l'acier S355, s = 4, l'abscisse x = 200 mm), ce qui est un **principe** (les conventions de signe, Re = 355 MPa pour un S355) et ce qui est une **valeur d'illustration** choisie pour s'entraîner. La façon dont le manuel mesure l'angle de P ne se lit pas sans son dessin : on retient celle qui redonne exactement FV = 10 170 N (section 1). Les schémas sont des **schémas de principe**, redessinés pour expliquer.

## 🧭 La flèche vue comme une poutre : le modèle et les efforts extérieurs

La capacité de la grue est de 250 kg : au bout de la flèche, la charge pèse donc P = 250 × 10 = 2 500 N (avec g = 10 N/kg, comme au chapitre du palan). La flèche est soutenue par le vérin en B et pivote sur le châssis en A. Le pied A exerce une action que personne ne donne.

Comment trouver tous les efforts qui s'exercent sur la flèche, y compris celui du pied ?

::: definition Le modèle de la flèche : une poutre ABC
Le manuel remplace la flèche par une **poutre** A–B–C. **A** est le pied (le pivot), **B** l'attache du vérin et **C** l'extrémité qui porte le crochet. Les longueurs sont a = AB = 420 mm et L = AC = 1 685 mm. Trois forces agissent sur elle :

- **FV**, l'effort du vérin en B, qui fait l'angle β = 51° avec la flèche ;
- **P**, la charge en C, verticale, qui fait l'angle θ = 38° avec la perpendiculaire à la flèche ;
- **FA**, l'action du pied en A, **inconnue** : un pivot peut pousser dans n'importe quelle direction, donc FA a deux composantes.

Deux hypothèses du manuel : on **néglige** le poids des pièces devant les efforts extérieurs, et on suppose **parfaites** toutes les liaisons. Pour calculer, on utilise un repère (A, x, y) **lié à la flèche**, pivoté de θ par rapport à la position réelle : l'axe x suit la flèche, l'axe y lui est perpendiculaire.
:::

::: figure La grue en position haute (schéma de principe). La flèche AC monte de θ = 38° sur l'horizontale, la charge P est verticale en C et le vérin, presque vertical, pousse la flèche en B
<svg viewBox="0 0 340 225"><title>La grue d'atelier en position haute : flèche inclinée de 38°, vérin presque vertical, charge verticale</title><line x1="20" y1="208" x2="330" y2="208" stroke="#0f172a" stroke-width="2.5"/><path d="M24 208 L15 217 M36 208 L27 217 M48 208 L39 217 M60 208 L51 217 M72 208 L63 217 M84 208 L75 217 M96 208 L87 217 M108 208 L99 217 M120 208 L111 217 M132 208 L123 217 M144 208 L135 217 M156 208 L147 217 M168 208 L159 217 M180 208 L171 217 M192 208 L183 217 M204 208 L195 217 M216 208 L207 217 M228 208 L219 217 M240 208 L231 217 M252 208 L243 217 M264 208 L255 217 M276 208 L267 217 M288 208 L279 217 M300 208 L291 217 M312 208 L303 217 M324 208 L315 217" stroke="#64748b" stroke-width="1.5"/><polygon points="36,208 36,187 100,187 100,208" fill="#e2e8f0" stroke="#0f172a" stroke-width="2"/><line x1="70" y1="175" x2="222.7" y2="55.7" stroke="#0f6e56" stroke-width="9"/><line x1="70" y1="175" x2="222.7" y2="55.7" stroke="#bbf7d0" stroke-width="4"/><line x1="107" y1="206" x2="108.06" y2="145.26" stroke="#2563eb" stroke-width="6"/><circle cx="107" cy="206" r="4" fill="#0f172a" stroke="#0f172a" stroke-width="2"/><line x1="222.7" y1="55.7" x2="222.7" y2="113.7" stroke="#ef4444" stroke-width="3"/><polygon points="222.7,113.7 218.2,104.7 227.2,104.7" fill="#ef4444"/><line x1="222.7" y1="55.7" x2="222.7" y2="59.7" stroke="#ef4444" stroke-width="1"/><line x1="70" y1="175" x2="155" y2="175" stroke="#64748b" stroke-width="1.5" stroke-dasharray="5 4"/><path d="M 110.98 142.99 A 52 52 0 0 1 122 175" fill="none" stroke="#0f172a" stroke-width="1.6"/><circle cx="70" cy="175" r="5" fill="#ffffff" stroke="#0f172a" stroke-width="2"/><circle cx="108.06" cy="145.26" r="4" fill="#0f172a" stroke="#0f172a" stroke-width="2"/><circle cx="222.7" cy="55.7" r="4" fill="#0f172a" stroke="#0f172a" stroke-width="2"/><g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="56" y="167" text-anchor="middle" fill="#0f172a" font-size="13">A</text><text x="94.06" y="139.26" text-anchor="middle" fill="#0f172a" font-size="13">B</text><text x="234.7" y="49.7" text-anchor="middle" fill="#0f172a" font-size="13">C</text><text x="152" y="151" text-anchor="middle" fill="#0f172a" font-size="12">θ = 38°</text><text x="240.7" y="95.7" text-anchor="middle" fill="#ef4444" font-size="14">P</text><text x="133" y="198.71" text-anchor="middle" fill="#2563eb" font-size="12">vérin</text><text x="77" y="200" text-anchor="middle" fill="#0f172a" font-size="13"></text></g></svg>
:::

::: figure Le modèle de la flèche, redessiné dans le repère pivoté : la flèche est horizontale, FV fait l'angle β avec elle, et P fait l'angle θ avec la perpendiculaire à la flèche. FA, calculée plus bas, descend vers la gauche
<svg viewBox="0 0 360 252"><title>Modèle de la flèche : poutre horizontale ABC, avec l'effort du vérin en B, la charge en C et l'action du pied en A</title><line x1="78" y1="118" x2="330.75" y2="118" stroke="#0f6e56" stroke-width="8"/><line x1="78" y1="118" x2="330.75" y2="118" stroke="#bbf7d0" stroke-width="3.5"/><line x1="141" y1="118" x2="198.9" y2="46.5" stroke="#2563eb" stroke-width="3"/><polygon points="198.9,46.5 196.73,56.33 189.74,50.66" fill="#2563eb"/><path d="M 164.91 88.47 A 38 38 0 0 1 179 118" fill="none" stroke="#0f172a" stroke-width="1.6"/><line x1="330.75" y1="118" x2="330.75" y2="178" stroke="#64748b" stroke-width="1.5" stroke-dasharray="5 4"/><line x1="330.75" y1="118" x2="285.19" y2="176.31" stroke="#ef4444" stroke-width="3"/><polygon points="285.19,176.31 287.19,166.45 294.28,171.99" fill="#ef4444"/><path d="M 330.75 158 A 40 40 0 0 1 306.12 149.52" fill="none" stroke="#0f172a" stroke-width="1.6"/><line x1="78" y1="118" x2="28.57" y2="178.34" stroke="#0f6e56" stroke-width="3"/><polygon points="28.57,178.34 30.79,168.53 37.76,174.23" fill="#0f6e56"/><line x1="78" y1="168" x2="141" y2="168" stroke="#0f172a" stroke-width="1.4"/><line x1="78" y1="164" x2="78" y2="172" stroke="#0f172a" stroke-width="1.4"/><line x1="141" y1="164" x2="141" y2="172" stroke="#0f172a" stroke-width="1.4"/><line x1="78" y1="190" x2="330.75" y2="190" stroke="#0f172a" stroke-width="1.4"/><line x1="78" y1="186" x2="78" y2="194" stroke="#0f172a" stroke-width="1.4"/><line x1="330.75" y1="186" x2="330.75" y2="194" stroke="#0f172a" stroke-width="1.4"/><line x1="30" y1="236" x2="80" y2="236" stroke="#0f172a" stroke-width="2"/><polygon points="80,236 72,240 72,232" fill="#0f172a"/><line x1="30" y1="236" x2="30" y2="210" stroke="#0f172a" stroke-width="2"/><polygon points="30,210 34,218 26,218" fill="#0f172a"/><circle cx="78" cy="118" r="5" fill="#ffffff" stroke="#0f172a" stroke-width="2"/><circle cx="141" cy="118" r="4" fill="#0f172a" stroke="#0f172a" stroke-width="2"/><circle cx="330.75" cy="118" r="4" fill="#0f172a" stroke="#0f172a" stroke-width="2"/><g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="74" y="106" text-anchor="middle" fill="#0f172a" font-size="13">A</text><text x="153" y="134" text-anchor="middle" fill="#0f172a" font-size="13">B</text><text x="334.75" y="106" text-anchor="middle" fill="#0f172a" font-size="13">C</text><text x="219" y="54" text-anchor="middle" fill="#2563eb" font-size="14">FV</text><text x="195" y="104" text-anchor="middle" fill="#0f172a" font-size="12">β</text><text x="268.75" y="184" text-anchor="middle" fill="#ef4444" font-size="14">P</text><text x="322.75" y="162" text-anchor="middle" fill="#0f172a" font-size="12">θ</text><text x="42" y="184" text-anchor="middle" fill="#0f6e56" font-size="14">FA</text><text x="109.5" y="162" text-anchor="middle" fill="#0f172a" font-size="11">a = 420</text><text x="204.38" y="204" text-anchor="middle" fill="#0f172a" font-size="11">L = 1685</text><text x="88" y="240" text-anchor="middle" fill="#0f172a" font-size="12">x</text><text x="22" y="210" text-anchor="middle" fill="#0f172a" font-size="12">y</text></g></svg>
:::

Sur le premier dessin, l'inclinaison de la flèche vaut θ = 38° et le vérin est presque vertical (β + θ = 89° : un peu moins de 90°, car le vérin n'est pas exactement vertical). Sur le second, on a tourné la feuille de 38° pour que la flèche soit horizontale : la charge, restée verticale, fait alors θ avec l'axe y, et le **cosinus** de θ donne sa part perpendiculaire à la flèche.

::: exemple Projeter P et FV, puis trouver FA (valeurs du manuel)
1. **Projeter P.** P fait l'angle θ avec l'axe y : Px = −P × sin θ = −2 500 × 0,616 ≈ **−1 539 N** (vers A) et Py = −P × cos θ = −2 500 × 0,788 ≈ **−1 970 N** (vers le bas). Pourquoi : l'angle est mesuré avec y, donc le cosinus donne la part sur y et le sinus la part sur x.
2. **Projeter FV.** L'angle β est mesuré avec la flèche (axe x) : FVx = FV × cos β = 10 170 × 0,629 ≈ **6 400 N** et FVy = FV × sin β = 10 170 × 0,777 ≈ **7 904 N**. Pourquoi : cette fois l'angle est avec x, donc le cosinus va sur x.
3. **Écrire l'équilibre des forces.** Sur x : FAx + 6 400 − 1 539 = 0, d'où FAx ≈ **−4 861 N**. Sur y : FAy + 7 904 − 1 970 = 0, d'où FAy ≈ **−5 934 N**. Pourquoi : la flèche ne bouge pas, donc la somme des composantes est nulle sur chaque axe. Les deux signes sont négatifs : FA est dirigée vers le bas et vers la gauche.
4. **Contrôler par les moments en A.** FVy × a = 7 904 × 420 ≈ 3 319 700 N·mm et Py × L = 1 970 × 1 685 ≈ 3 319 450 N·mm : les deux sont égaux, aux arrondis près. Pourquoi : FA passe par A et n'a pas de moment en A ; les composantes sur x passent par l'axe de la flèche et n'en ont pas non plus. C'est ce contrôle qui explique FV = P × cos θ × L / (sin β × a) ≈ 10 170 N.

| Force | Point d'application | Projection sur Ax | Projection sur Ay |
| --- | --- | --- | --- |
| FA | A | −4 861 N | −5 934 N |
| FV | B | +6 400 N | +7 904 N |
| P | C | −1 539 N | −1 970 N |

:::

::: piege Le sinus et le cosinus de P échangés
Par habitude, on écrit Py = −P × sin θ = −1 539 N, parce qu'un angle « de la figure » appelle le sinus. Mais ici θ est mesuré avec l'axe y : la bonne part sur y est P × cos θ. L'erreur se voit au contrôle : le moment de P en A vaudrait 1 539 × 1 685 ≈ 2 593 000 N·mm, et il ne serait plus égal à celui de FV (3 319 700 N·mm). Quand on projette, on regarde toujours **avec quel axe** l'angle est mesuré.
:::

::: methode Projeter, puis équilibrer
1. Repérer pour chaque force l'axe avec lequel son angle est mesuré : cosinus sur cet axe, sinus sur l'autre.
2. Écrire la somme des composantes sur x, puis sur y : elle donne les deux composantes inconnues du pivot.
3. Contrôler par les moments autour du pivot.

Cas limite : une force **dirigée selon la flèche** (comme Px ou FVx) n'a aucun moment en A : elle tire ou comprime la flèche, elle ne la plie pas.
:::

::: verifie
Même grue, mais la flèche est inclinée de θ = 25° et la charge reste P = 2 500 N. Que valent les composantes de P dans le repère lié à la flèche ?
---
θ est mesuré avec l'axe y : Px = −P × sin θ = −2 500 × 0,423 ≈ **−1 057 N** et Py = −P × cos θ = −2 500 × 0,906 ≈ **−2 266 N**. Plus la flèche est basse, plus la part perpendiculaire (celle qui plie) est grande et plus la part selon la flèche est petite.
:::

## ✂️ Couper la poutre : N, Ty et Mfz tronçon par tronçon

Toutes les forces sont connues : FA, FV et P. Mais une poutre ne casse pas à l'endroit où l'on pousse dessus de l'extérieur : elle casse là où sa matière est trop sollicitée à l'intérieur, dans une **section**.

Que subit chaque section de la flèche, et comment le calculer ?

::: definition Les efforts de cohésion N, Ty et Mfz
On **coupe** la poutre par une section d'abscisse x. Le morceau de droite agit sur celui de gauche par trois grandeurs, les **efforts de cohésion** :

- l'**effort normal N**, dirigé selon la flèche : positif si la section est tirée (traction), négatif si elle est comprimée ;
- l'**effort tranchant Ty**, perpendiculaire à la flèche : il cisaille la section ;
- le **moment fléchissant Mfz**, moment autour de l'axe z : il plie la flèche.

Le morceau de gauche est en équilibre : N = −(somme des composantes sur x des forces à gauche), Ty = −(somme des composantes sur y des forces à gauche), et Mfz équilibre le moment de ces forces par rapport à la section. Le manuel n'imprime pas ses conventions de signe : on choisit ici Mfz **positif quand la flèche s'incurve de façon à étirer les fibres du haut** (y > 0), ce qui s'accorde avec σ = (Mfz / IGz) × y de la synthèse. La condition de résistance ne dépend que des valeurs absolues.
:::

::: figure Le morceau de gauche, coupé à l'abscisse x. À gauche, l'action FA du pied ; à la coupure, l'action du morceau de droite : N selon la flèche, Ty perpendiculaire, et le moment Mfz qui s'oppose à celui de FA
<svg viewBox="0 0 340 175"><title>Coupe de la poutre à l'abscisse x : le morceau de droite agit sur le morceau de gauche par N, Ty et Mfz</title><line x1="60" y1="100" x2="250" y2="100" stroke="#0f6e56" stroke-width="8"/><line x1="60" y1="100" x2="250" y2="100" stroke="#bbf7d0" stroke-width="3.5"/><line x1="250" y1="50" x2="250" y2="150" stroke="#64748b" stroke-width="1.6" stroke-dasharray="5 4"/><line x1="60" y1="100" x2="21.98" y2="146.41" stroke="#0f6e56" stroke-width="3"/><polygon points="21.98,146.41 24.2,136.6 31.16,142.3" fill="#0f6e56"/><line x1="250" y1="100" x2="312" y2="100" stroke="#ef4444" stroke-width="3"/><polygon points="312,100 303,104.5 303,95.5" fill="#ef4444"/><line x1="250" y1="100" x2="250" y2="48" stroke="#2563eb" stroke-width="3"/><polygon points="250,48 254.5,57 245.5,57" fill="#2563eb"/><path d="M 221.81 89.74 A 30 30 0 0 1 275.98 85" fill="none" stroke="#d97706" stroke-width="2.5"/><polygon points="275.98,85 267.58,79.46 275.38,74.96" fill="#d97706"/><line x1="60" y1="140" x2="250" y2="140" stroke="#0f172a" stroke-width="1.4"/><line x1="60" y1="136" x2="60" y2="144" stroke="#0f172a" stroke-width="1.4"/><line x1="250" y1="136" x2="250" y2="144" stroke="#0f172a" stroke-width="1.4"/><circle cx="60" cy="100" r="5" fill="#ffffff" stroke="#0f172a" stroke-width="2"/><circle cx="250" cy="100" r="4" fill="#0f172a" stroke="#0f172a" stroke-width="2"/><g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="56" y="86" text-anchor="middle" fill="#0f172a" font-size="13">A</text><text x="236" y="122" text-anchor="middle" fill="#0f172a" font-size="13">G</text><text x="24" y="156" text-anchor="middle" fill="#0f6e56" font-size="14">FA</text><text x="328" y="105" text-anchor="middle" fill="#ef4444" font-size="14">N</text><text x="260" y="40" text-anchor="middle" fill="#2563eb" font-size="14">Ty</text><text x="206" y="70" text-anchor="middle" fill="#d97706" font-size="13">Mfz</text><text x="155" y="158" text-anchor="middle" fill="#0f172a" font-size="12">x</text><text x="150" y="28" text-anchor="middle" fill="#64748b" font-size="12">morceau de gauche</text></g></svg>
:::

Sur la figure, les trois grandeurs de la coupure sont celles qu'il faut ajouter à FA pour que le morceau de gauche reste en équilibre : N équilibre la composante de FA sur x, Ty celle sur y, et Mfz le moment de FA.

::: exemple N, Ty et Mfz dans les deux tronçons (valeurs du manuel)
1. **Découper.** Les forces changent en B, donc la poutre se découpe en deux tronçons : la **section 1** (0 ≤ x ≤ 420 mm) et la **section 2** (420 ≤ x ≤ 1 685 mm). Pourquoi : dans chacun, les mêmes forces sont à gauche de la coupure.
2. **Section 1, morceau de gauche : seule FA y est.** N = −FAx = **+4 861 N** (traction), Ty = −FAy = **+5 934 N**, et le moment de FA par rapport à la coupure a pour bras x : Mfz = **5 934 × x** (en N·mm). Pourquoi : à gauche, il n'y a que FA.
3. **Section 2, morceau de droite : seule P y est.** N = Px = **−1 539 N** (compression), Ty = Py = **−1 970 N**, et Mfz = **1 970 × (1 685 − x)**, puisque P est à la distance 1 685 − x de la coupure et qu'elle étire les fibres du haut. Pourquoi : la flèche entière est en équilibre, donc les forces de droite valent l'opposé de celles de gauche : on peut compter à droite, avec le signe contraire, ce qui évite de garder FA et FV.
4. **Contrôler en B.** Mfz(420) = 5 934 × 420 ≈ 2 492 280 N·mm par la section 1 et 1 970 × 1 265 ≈ 2 492 050 N·mm par la section 2 : égaux aux arrondis près. Pourquoi : le moment ne fait pas de saut en B, alors que N et Ty en font un (de 6 400 N pour N, de 7 904 N pour Ty, soit FVx et FVy).

:::

::: piege Oublier FV dans la section 2
Garder l'expression 5 934 × x au-delà de B revient à ignorer FV. À l'extrémité C, x = 1 685 mm, elle donnerait Mfz ≈ 10 000 000 N·mm, alors que l'extrémité libre C ne porte aucun moment : Mfz(C) = 0. Ce contrôle, **le moment est nul à une extrémité libre**, démasque aussitôt l'oubli.
:::

::: propriete Ce qui change à un point d'application
Entre deux points d'application, les expressions de N, Ty et Mfz ne changent pas. Au passage d'une force, **N saute d'une valeur égale à la composante de la force sur x**, **Ty d'une valeur égale à sa composante sur y**, et Mfz, continu, **change de pente**. Dans la convention choisie, Ty est la pente de Mfz : 2 492 280 / 420 ≈ 5 934 en section 1, et −2 492 050 / 1 265 ≈ −1 970 en section 2.
:::

::: verifie
Dans la section 1, quels sont N, Ty et Mfz à l'abscisse x = 300 mm ?
---
Section 1, morceau de gauche : seule FA y est. N = 4 861 N ; Ty = 5 934 N ; Mfz = 5 934 × 300 = 1 780 200 N·mm ≈ **1 780 N·m**. N et Ty sont constants dans le tronçon, seul Mfz dépend de x.
:::

## 📈 Les diagrammes et la section la plus sollicitée

Les expressions de la section 2 sont difficiles à comparer d'un coup d'œil. Un bureau d'études ne cherche pas la valeur en x = 300 : il cherche **où** la flèche souffre le plus, et **de quelle façon**.

Comment lire cela d'un seul regard ?

::: definition Diagramme et sollicitation d'une section
Un **diagramme** porte l'abscisse x à l'horizontale et la grandeur (N, Ty ou Mfz) à la verticale : on lit ainsi toute la poutre d'un coup. La **sollicitation** d'une section se déduit de ce qui n'y est pas nul :

- N seul : traction ou compression simple ; Mfz (avec Ty) seul : flexion ;
- **N et Mfz ensemble** : sollicitation **composée**, de **flexion–traction** si N est positif, de **flexion–compression** s'il est négatif.
:::

::: figure Les diagrammes de la flèche. N et Ty sont des paliers (la valeur ne change qu'en B), Mfz est une ligne brisée qui monte de A à B puis redescend jusqu'à C
<svg viewBox="0 0 360 322"><title>Diagrammes de l'effort normal N, de l'effort tranchant Ty et du moment fléchissant Mfz le long de la flèche</title><line x1="70" y1="18" x2="70" y2="318" stroke="#64748b" stroke-width="1.2" stroke-dasharray="4 4"/><line x1="132.31" y1="18" x2="132.31" y2="318" stroke="#64748b" stroke-width="1.2" stroke-dasharray="4 4"/><line x1="320" y1="18" x2="320" y2="318" stroke="#64748b" stroke-width="1.2" stroke-dasharray="4 4"/><line x1="62" y1="62" x2="330" y2="62" stroke="#0f172a" stroke-width="1.6"/><polygon points="70,62 70,26 132.31,26 132.31,62" fill="#bfdbfe" stroke="#2563eb" stroke-width="2"/><polygon points="132.31,62 132.31,73.4 320,73.4 320,62" fill="#fecaca" stroke="#ef4444" stroke-width="2"/><g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="101.16" y="21" text-anchor="middle" fill="#0f172a" font-size="11">+4861</text><text x="226.16" y="87.4" text-anchor="middle" fill="#0f172a" font-size="11">−1539</text></g><g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="8" y="22" text-anchor="start" fill="#0f172a" font-size="11">N (N)</text></g><line x1="62" y1="160" x2="330" y2="160" stroke="#0f172a" stroke-width="1.6"/><polygon points="70,160 70,124 132.31,124 132.31,160" fill="#bfdbfe" stroke="#2563eb" stroke-width="2"/><polygon points="132.31,160 132.31,171.95 320,171.95 320,160" fill="#fecaca" stroke="#ef4444" stroke-width="2"/><g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="101.16" y="119" text-anchor="middle" fill="#0f172a" font-size="11">+5934</text><text x="226.16" y="185.95" text-anchor="middle" fill="#0f172a" font-size="11">−1970</text></g><g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="8" y="120" text-anchor="start" fill="#0f172a" font-size="11">Ty (N)</text></g><line x1="62" y1="262" x2="330" y2="262" stroke="#0f172a" stroke-width="1.6"/><polygon points="70,262 132.31,226 320,262" fill="#fde68a" stroke="#d97706" stroke-width="2"/><g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="138.31" y="220" text-anchor="start" fill="#0f172a" font-size="11">2492</text></g><g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="8" y="222" text-anchor="start" fill="#0f172a" font-size="11">Mfz (N·m)</text></g><g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="70" y="12" text-anchor="middle" fill="#0f172a" font-size="13">A</text><text x="132.31" y="12" text-anchor="middle" fill="#0f172a" font-size="13">B</text><text x="320" y="12" text-anchor="middle" fill="#0f172a" font-size="13">C</text></g></svg>
:::

Sur le diagramme de N, le palier positif de A à B est la traction, le palier négatif de B à C la compression ; sur celui de Ty, le saut en B vaut 5 934 + 1 970 = 7 904 N, c'est FVy ; Mfz est nul en A et en C et maximal en B.

::: exemple Lire les diagrammes de la flèche
1. **Sollicitations.** Section 1 : N > 0 et Mfz ≠ 0, donc **flexion–traction**. Section 2 : N < 0 et Mfz ≠ 0, donc **flexion–compression**. Pourquoi : le signe de N change en B.
2. **Moment maximal.** Mfz est une droite de chaque côté de B et il vaut 0 en A comme en C : son maximum est en B, soit **Mfzmax ≈ 2 492 N·m**. Pourquoi : un moment linéaire par tronçon atteint son extrême à un point d'application.
3. **Effort normal associé.** Juste à gauche de B, N = **+4 861 N** (traction) ; juste à droite, N = −1 539 N. La section la plus sollicitée est **B, côté A** : elle cumule le moment maximal et la plus forte traction.
4. **Conclure.** Valeurs maximales : Mfz = 2 492 N·m et N = 4 861 N. Pourquoi : ce sont celles qui entrent dans la condition de résistance.

:::

::: piege L'effort tranchant maximal n'est pas la section la plus sollicitée
Ty vaut 5 934 N dès le pied A, et on pourrait y voir la section dangereuse. Mais en A, Mfz = 0 : le pivot ne plie rien. La flexion dimensionne la poutre, et elle est maximale là où Mfz est maximal, c'est-à-dire en B, **là où Ty change de signe**.
:::

::: propriete Où chercher le maximum de Mfz
Entre deux forces, Mfz est une droite ; il est nul aux extrémités libres ou sur un pivot sans couple ; son maximum se trouve donc à un point d'application, et en général là où Ty change de signe (la pente de Mfz change de signe). Ici Ty passe de +5 934 N à −1 970 N en B : Mfz monte, puis redescend.
:::

::: verifie
Quelle sollicitation subit la section 2, et pourquoi ?
---
La section 2 est en **flexion–compression** : Mfz y est non nul (il décroît de 2 492 à 0 N·m) et N = −1 539 N est négatif, donc la section est comprimée en même temps que pliée. Si N avait été positif, ce serait de la flexion–traction.
:::

## 🔲 Le tube carré creux : S et IGz/v

La flèche est faite d'un tube carré. Le magasin en propose trois : 70 × 70 × 5, 80 × 80 × 5 et 90 × 90 × 5 (en mm). Pour les comparer, il faut deux grandeurs géométriques : l'**aire S**, qui dit comment la traction se répartit, et le **module de flexion IGz/v**, qui dit comment la flexion se répartit.

Comment les calculer pour un tube creux ?

::: definition Les caractéristiques d'un tube carré B × B × T
Le tube a un **côté extérieur B** et une **épaisseur T** (en mm) : son vide est un carré de côté B − 2T. Pour une section creuse, on retranche le vide du plein :

$$ S = B² − (B − 2T)² $$

$$ IGz = (B⁴ − (B − 2T)⁴) / 12 $$

IGz est le moment quadratique autour de l'axe neutre Gz (le b × h³ / 12 du carré plein, appliqué au carré extérieur puis au vide). La fibre la plus éloignée est à v = B / 2 du centre G, et **IGz / v** s'exprime en mm³.
:::

::: figure Section d'un tube carré creux. Le côté extérieur est B, l'épaisseur T, et la fibre la plus éloignée de G est à la distance v = B / 2 sur l'axe y
<svg viewBox="0 0 300 255"><title>Section d'un tube carré creux : côté extérieur B, épaisseur T, centre de gravité G, axes y et z, distance v de G à la fibre extérieure</title><rect x="75" y="45" width="150" height="150" fill="#cbd5e1" stroke="#0f172a" stroke-width="2.5"/><rect x="89" y="59" width="122" height="122" fill="#ffffff" stroke="#0f172a" stroke-width="2"/><line x1="150" y1="120" x2="150" y2="23" stroke="#0f172a" stroke-width="2"/><polygon points="150,23 154,31 146,31" fill="#0f172a"/><line x1="150" y1="120" x2="247" y2="120" stroke="#0f172a" stroke-width="2"/><polygon points="247,120 239,124 239,116" fill="#0f172a"/><circle cx="150" cy="120" r="3.5" fill="#0f172a" stroke="#0f172a" stroke-width="2"/><line x1="75" y1="215" x2="225" y2="215" stroke="#0f172a" stroke-width="1.4"/><line x1="75" y1="210" x2="75" y2="220" stroke="#0f172a" stroke-width="1.4"/><line x1="225" y1="210" x2="225" y2="220" stroke="#0f172a" stroke-width="1.4"/><line x1="53" y1="120" x2="53" y2="45" stroke="#0f172a" stroke-width="1.4"/><line x1="48" y1="120" x2="58" y2="120" stroke="#0f172a" stroke-width="1.4"/><line x1="48" y1="45" x2="58" y2="45" stroke="#0f172a" stroke-width="1.4"/><line x1="211" y1="150" x2="225" y2="150" stroke="#ef4444" stroke-width="2.5"/><g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="150" y="231" text-anchor="middle" fill="#0f172a" font-size="12">B (côté extérieur)</text><text x="45" y="82.5" text-anchor="end" fill="#0f172a" font-size="13">v</text><text x="162" y="136" text-anchor="start" fill="#0f172a" font-size="13">G</text><text x="158" y="19" text-anchor="start" fill="#0f172a" font-size="13">y</text><text x="253" y="124" text-anchor="start" fill="#0f172a" font-size="13">z</text><text x="233" y="156" text-anchor="start" fill="#ef4444" font-size="13">T</text></g></svg>
:::

Sur la figure, B et T sont les deux nombres de la désignation B × B × T, et v est la moitié de B parce que G est au centre du carré.

::: exemple Les caractéristiques du tube 70 × 70 × 5, puis des trois tubes (valeurs du manuel)
1. **Le vide.** B − 2T = 70 − 10 = 60 mm. Pourquoi : la paroi retire 5 mm de chaque côté.
2. **L'aire.** S = 70² − 60² = 4 900 − 3 600 = **1 300 mm²**. Pourquoi : on retranche le carré creux du carré plein.
3. **Le moment quadratique.** IGz = (70⁴ − 60⁴) / 12 = (24 010 000 − 12 960 000) / 12 ≈ **920 833 mm⁴**. Pourquoi : même soustraction, avec la puissance quatrième.
4. **Le module de flexion.** v = 35 mm, donc IGz / v ≈ 920 833 / 35 ≈ **26 310 mm³**.
5. **Les trois tubes.** On refait le calcul pour chacun :

| Section B × B × T | S (mm² × 10²) | IGz / v (mm³ × 10³) |
| --- | --- | --- |
| 70 × 70 × 5 | 13 | 26,3 |
| 80 × 80 × 5 | 15 | 35,3 |
| 90 × 90 × 5 | 17 | 45,6 |

:::

::: piege Le tube n'est pas un carré plein, et v n'est pas B
Calculer IGz / v avec le carré plein, 70⁴ / 12 / 35 ≈ 57 167 mm³, donne plus du double de la valeur du tube (26 310 mm³) : on surestime la rigidité et on choisit un tube trop faible. L'autre glissade est de prendre v = B = 70 mm au lieu de B / 2 = 35 mm : on trouve 13 155 mm³, la moitié de la bonne valeur. Le vide se retranche, et v est une **demi-hauteur**.
:::

::: propriete Le module de flexion croît plus vite que l'aire
De 70 × 70 × 5 à 90 × 90 × 5, l'aire passe de 1 300 à 1 700 mm² (environ 31 % de plus) alors que IGz / v passe de 26 310 à 45 648 mm³ (environ 73 % de plus). Pour la flexion, agrandir le **côté** rapporte plus que d'ajouter de la matière : la matière est utile loin du centre.
:::

::: verifie
Que valent S et IGz / v pour un tube 60 × 60 × 4 ?
---
Le vide a pour côté 60 − 8 = 52 mm. S = 60² − 52² = 3 600 − 2 704 = **896 mm²**. IGz = (60⁴ − 52⁴) / 12 = (12 960 000 − 7 311 616) / 12 ≈ 470 699 mm⁴, et v = 30 mm, donc IGz / v ≈ **15 690 mm³**.
:::

## ➕ Traction et flexion ensemble : deux contraintes qui s'additionnent

Dans la section 1, le tube est **tiré** par N = 4 861 N et **plié** par un moment qui va jusqu'à 2 492 N·m. Chacune de ces sollicitations crée sa propre contrainte normale, c'est-à-dire un effort par mm² perpendiculaire à la section.

Que subit réellement une fibre du tube, quand les deux agissent ensemble ?

::: definition La superposition des contraintes normales
- La traction crée une contrainte **uniforme** : **σN = N / S**.
- La flexion crée une contrainte **linéaire** : **σf = (Mfz / IGz) × y**, nulle sur l'axe neutre et maximale en y = ±v : **σf max = Mfz / (IGz / v)**.
- Les deux sont des contraintes **normales**, de même direction : dans une fibre, elles **s'additionnent** : σ = σN + σf.

La contrainte uniforme décale tout le diagramme : la ligne où σ = 0, le **nouveau plan neutre**, quitte le centre G. Une contrainte en MPa est un effort en N par mm².
:::

::: figure Superposition à l'abscisse x = 200 mm, tube 80 × 80 × 5. À gauche la traction (uniforme), au milieu la flexion (linéaire), à droite leur somme : la zone tendue s'agrandit et la ligne où σ = 0 descend sous G. Les contraintes sont en MPa
<svg viewBox="0 0 440 222"><title>Répartition de la contrainte normale dans une section du tube 80×80×5 à x = 200 mm : traction uniforme plus flexion linéaire</title><line x1="70" y1="42" x2="70" y2="178" stroke="#0f172a" stroke-width="1.6"/><polygon points="70,50 74.34,50 74.34,170 70,170" fill="#bfdbfe" stroke="#2563eb" stroke-width="2"/><line x1="18" y1="50" x2="122" y2="50" stroke="#64748b" stroke-width="1" stroke-dasharray="3 3"/><line x1="18" y1="170" x2="122" y2="170" stroke="#64748b" stroke-width="1" stroke-dasharray="3 3"/><line x1="195" y1="42" x2="195" y2="178" stroke="#0f172a" stroke-width="1.6"/><polygon points="195,50 240,50 150,170 195,170" fill="#fde68a" stroke="#d97706" stroke-width="2"/><line x1="143" y1="50" x2="247" y2="50" stroke="#64748b" stroke-width="1" stroke-dasharray="3 3"/><line x1="143" y1="170" x2="247" y2="170" stroke="#64748b" stroke-width="1" stroke-dasharray="3 3"/><line x1="330" y1="42" x2="330" y2="178" stroke="#0f172a" stroke-width="1.6"/><polygon points="330,50 379.34,50 289.34,170 330,170" fill="#bbf7d0" stroke="#0f6e56" stroke-width="2"/><line x1="278" y1="50" x2="382" y2="50" stroke="#64748b" stroke-width="1" stroke-dasharray="3 3"/><line x1="278" y1="170" x2="382" y2="170" stroke="#64748b" stroke-width="1" stroke-dasharray="3 3"/><line x1="278" y1="115.78" x2="382" y2="115.78" stroke="#ef4444" stroke-width="1.8" stroke-dasharray="6 3"/><line x1="278" y1="110" x2="382" y2="110" stroke="#64748b" stroke-width="1.2" stroke-dasharray="2 3"/><g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="75" y="24" text-anchor="middle" fill="#0f172a" font-size="13">σN</text><text x="195" y="24" text-anchor="middle" fill="#0f172a" font-size="13">σf</text><text x="330" y="24" text-anchor="middle" fill="#0f172a" font-size="13">σN + σf</text><text x="132" y="115" text-anchor="middle" fill="#0f172a" font-size="22">+</text><text x="262" y="115" text-anchor="middle" fill="#0f172a" font-size="22">=</text><text x="80.34" y="110" text-anchor="start" fill="#0f172a" font-size="11">3,24</text><text x="245" y="47" text-anchor="start" fill="#0f172a" font-size="11">+33,61</text><text x="145" y="182" text-anchor="end" fill="#0f172a" font-size="11">−33,61</text><text x="384.34" y="47" text-anchor="start" fill="#0f172a" font-size="11">+36,85</text><text x="285.34" y="182" text-anchor="end" fill="#0f172a" font-size="11">−30,37</text><text x="386" y="119.78" text-anchor="start" fill="#ef4444" font-size="11">σ = 0</text><text x="10" y="54" text-anchor="start" fill="#64748b" font-size="10">haut</text><text x="10" y="174" text-anchor="start" fill="#64748b" font-size="10">bas</text><text x="330" y="206" text-anchor="middle" fill="#ef4444" font-size="11">ligne neutre décalée sous G</text></g></svg>
:::

Sur la figure, le rectangle bleu est σN (le même partout), le triangle jaune est σf (de −33,61 à +33,61), et leur somme en vert est le trapèze de droite.

::: exemple La superposition en x = 200 mm, pour le tube 80 × 80 × 5 (valeurs du manuel)
1. **Les efforts.** x = 200 mm est dans la section 1 : N = 4 861 N et Mfz = 5 934 × 200 = 1 186 800 N·mm. Pourquoi : on reprend les expressions du tronçon.
2. **La traction.** σN = N / S = 4 861 / 1 500 ≈ **3,24 MPa**. Pourquoi : S = 1 500 mm² pour ce tube.
3. **La flexion maximale.** σf max = Mfz / (IGz / v) = 1 186 800 / 35 312,5 ≈ **33,61 MPa**.
4. **Les deux fibres extrêmes.** En haut (y = +v), σN et σf sont tous deux positifs : 3,24 + 33,61 = **+36,85 MPa** (traction). En bas (y = −v), σf est négatif : 3,24 − 33,61 = **−30,37 MPa** (compression). Pourquoi : la flexion étire le haut et comprime le bas.
5. **La ligne neutre.** σ = 0 pour y = −v × σN / σf max = −40 × 3,24 / 33,61 ≈ **−3,9 mm** : la ligne neutre passe 3,9 mm sous G.
6. **Conclure.** La traction agrandit la zone tendue et décale la ligne neutre vers la fibre comprimée ; la contrainte maximale est en haut.

:::

::: piege Additionner les efforts, ou oublier le signe de la fibre basse
Écrire 4 861 + 1 186 800 n'a aucun sens : N est en newtons et Mfz en newtons-millimètres. On additionne des **contraintes** (3,24 et 33,61 MPa), jamais des efforts. Autre glissade : dans la fibre basse, additionner 3,24 + 33,61 = 36,85 MPa fait croire que le haut et le bas sont tendus de la même façon, alors que le bas est **comprimé** : σf y est négatif, et c'est 3,24 − 33,61 = −30,37 MPa.
:::

::: propriete La condition de résistance en flexion–traction
En flexion–traction, la plus forte contrainte normale est celle de la fibre la plus tendue. On la compare à la **résistance pratique à l'extension Rpe = Re / s** :

$$ ‖N‖ / S + ‖Mfz max‖ / (IGz / v) ≤ Rpe $$

Cas limites : si N = 0, on retrouve la condition de la flexion simple, σmax = Mfz / (IGz / v) ≤ Rpe ; si Mfz = 0, il reste N / S ≤ Rpe, la traction simple. Avec N < 0 (flexion–compression), la fibre la plus comprimée porte la même somme en valeur absolue, et la condition s'écrit pareil. Le flambage (risque de la flèche comprimée) n'est pas traité par le manuel.
:::

::: verifie
Une section de S = 1 000 mm² et IGz / v = 20 000 mm³ porte N = 5 000 N et Mfz = 400 000 N·mm. Que valent les contraintes de ses deux fibres extrêmes ?
---
σN = 5 000 / 1 000 = 5 MPa et σf max = 400 000 / 20 000 = 20 MPa. La fibre tendue porte 5 + 20 = **+25 MPa** et la fibre opposée 5 − 20 = **−15 MPa**. On additionne des contraintes, avec le signe de chaque fibre.
:::

## ✅ Choisir la section dans le catalogue

Il reste à trancher : lequel des trois tubes convient pour la grue ? Le constructeur a choisi l'acier S355 avec un coefficient de sécurité s = 4, et un tube trop faible casserait alors qu'un tube trop gros alourdirait la grue.

Comment décider, calcul à l'appui ?

::: definition Rpe et la contrainte équivalente σéq
La désignation **S355** indique une limite élastique Re = 355 MPa (principe). La **résistance pratique** est donc Rpe = Re / s = 355 / 4 = **88,75 MPa**.

La colonne σéq du manuel est la plus grande contrainte normale en valeur absolue : **σéq = ‖N‖ / S + ‖Mfz‖ / (IGz / v)**, portée par la fibre la plus tendue en flexion–traction et par la fibre la plus comprimée en flexion–compression. Elle doit rester inférieure ou égale à Rpe. Le tube retenu est le **plus petit** (donc le plus léger) qui vérifie la condition.
:::

::: exemple Les trois tubes, dans la section la plus sollicitée (valeurs du manuel)
Avec N = 4 861 N et Mfzmax = 2 492 N·m = 2 492 000 N·mm (section B, côté A) :

1. **Rpe.** 355 / 4 = **88,75 MPa**.
2. **Le tube 70 × 70 × 5.** σN = 4 861 / 1 300 ≈ 3,74 MPa, σf = 2 492 000 / 26 310 ≈ 94,72 MPa, donc σéq ≈ **98,46 MPa**, supérieur à 88,75 : **refusé**.
3. **Le tube 80 × 80 × 5.** σN = 4 861 / 1 500 ≈ 3,24 MPa, σf = 2 492 000 / 35 312,5 ≈ 70,57 MPa, donc σéq ≈ **73,81 MPa**, inférieur à 88,75 : **accepté**.
4. **Le tube 90 × 90 × 5.** σN ≈ 2,86 MPa, σf ≈ 54,59 MPa, donc σéq ≈ **57,45 MPa** : accepté aussi.
5. **Choisir.** Les deux derniers conviennent ; on garde le plus petit, le **80 × 80 × 5**. Pourquoi : le 90 × 90 × 5 coûte environ 13 % d'aire (1 700 contre 1 500 mm²) pour une marge dont la grue n'a pas besoin.

| Section | σf (MPa) | σN (MPa) | σéq (MPa) | σéq ≤ 88,75 ? |
| --- | --- | --- | --- | --- |
| 70 × 70 × 5 | 94,72 | 3,74 | 98,46 | non |
| 80 × 80 × 5 | 70,57 | 3,24 | 73,81 | oui |
| 90 × 90 × 5 | 54,59 | 2,86 | 57,45 | oui |

:::

::: piege Comparer à Re au lieu de Rpe
Les trois valeurs de σéq sont inférieures à Re = 355 MPa : on croirait que le tube 70 × 70 × 5 convient, alors qu'il dépasse la résistance pratique de 88,75 MPa. Comparer à Re oublie le coefficient de sécurité s = 4, c'est-à-dire la marge. Autre glissade : ne garder que σf et oublier σN, qui sous-estime la contrainte (ici de 3 à 4 MPa, ce qui peut suffire à faire changer le verdict d'un tube limite).
:::

::: propriete Le coefficient de sécurité réel
Une fois la section choisie, le coefficient réel est **Re / σéq** : 355 / 73,81 ≈ 4,81 pour le tube 80 × 80 × 5, supérieur à s = 4 ; pour le 70 × 70 × 5, 355 / 98,46 ≈ 3,61, inférieur à 4. La condition σéq ≤ Rpe équivaut à Re / σéq ≥ s ; une égalité est acceptée.
:::

::: verifie
Le tube 60 × 60 × 4 (S = 896 mm², IGz / v = 15 690 mm³) convient-il pour la même charge, avec Rpe = 88,75 MPa ?
---
σN = 4 861 / 896 ≈ 5,43 MPa et σf = 2 492 000 / 15 690 ≈ 158,82 MPa, donc σéq ≈ **164 MPa**. C'est presque le double de 88,75 MPa : le tube est **refusé**, même sans compter σN.
:::

## 🌀 Synthèse : torsion simple et flexion plane simple

Les activités du thème ont construit deux outils qui se ressemblent : un pour l'arbre qui se tord, un pour la poutre qui plie. La synthèse du manuel les range côte à côte.

Qu'ont-ils en commun, et où se distinguent-ils ?

::: definition Les deux sollicitations simples du thème
- **Torsion simple** : une poutre est en torsion simple quand ses deux extrémités reçoivent deux couples égaux et opposés, d'axe confondu avec la ligne moyenne. Elle se déforme d'un **angle unitaire θ = α / L** (α : angle relatif en rad ; L : longueur), et la **contrainte tangentielle** vaut **τ = (Mt / I0) × ρ**, où ρ est la distance au centre.
- **Flexion plane simple** : la **contrainte normale** vaut **σ = (Mfz / IGz) × y**, où y est l'ordonnée du point à partir de l'axe neutre.

Dans les deux cas, la contrainte est **proportionnelle à la distance** (ρ ou y) : nulle au centre ou sur l'axe neutre, maximale au bord.

| | Torsion simple | Flexion plane simple |
| --- | --- | --- |
| Moment | Mt | Mfz |
| Contrainte | tangentielle τ | normale σ |
| Maximum | τmax = Mt / (I0 / R), en ρ = R | σmax = Mfz / (IGz / v), en y = v |
| Condition de résistance | τmax ≤ Rpg, avec Rpg = Reg / s | σmax ≤ Rpe, avec Rpe = Re / s |
| Condition de rigidité | θ = Mt / (G × I0) ≤ θlimite (fixé par l'expérience) | la déformée (flèche f de la poutre) n'est pas formalisée dans la synthèse |
:::

::: figure Les deux répartitions de contrainte. En torsion (section ronde) comme en flexion, la contrainte est une droite qui passe par zéro au centre et vaut ±max au bord
<svg viewBox="0 0 420 196"><title>Répartition de la contrainte tangentielle en torsion et de la contrainte normale en flexion : linéaires, nulles au centre, maximales au bord</title><circle cx="100" cy="100" r="55" fill="#e2e8f0" stroke="#0f172a" stroke-width="2"/><line x1="100" y1="39" x2="100" y2="161" stroke="#0f172a" stroke-width="1.2"/><polygon points="100,45 140,45 60,155 100,155" fill="#fecaca" stroke="#ef4444" stroke-width="2"/><circle cx="100" cy="100" r="3" fill="#0f172a" stroke="#0f172a" stroke-width="2"/><rect x="262" y="45" width="76" height="110" fill="#e2e8f0" stroke="#0f172a" stroke-width="2"/><line x1="300" y1="39" x2="300" y2="161" stroke="#0f172a" stroke-width="1.2"/><polygon points="300,45 378,45 222,155 300,155" fill="#fde68a" stroke="#d97706" stroke-width="2"/><circle cx="300" cy="100" r="3" fill="#0f172a" stroke="#0f172a" stroke-width="2"/><g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="100" y="22" text-anchor="middle" fill="#0f172a" font-size="13">Torsion : τ</text><text x="300" y="22" text-anchor="middle" fill="#0f172a" font-size="13">Flexion : σ</text><text x="144" y="41" text-anchor="start" fill="#0f172a" font-size="11">τmax</text><text x="56" y="169" text-anchor="end" fill="#0f172a" font-size="11">−τmax</text><text x="382" y="41" text-anchor="start" fill="#0f172a" font-size="11">σmax</text><text x="218" y="169" text-anchor="end" fill="#0f172a" font-size="11">−σmax</text><text x="110" y="104" text-anchor="start" fill="#0f172a" font-size="11">G</text><text x="310" y="104" text-anchor="start" fill="#0f172a" font-size="11">G</text><text x="100" y="184" text-anchor="middle" fill="#64748b" font-size="11">nulle au centre G</text><text x="300" y="184" text-anchor="middle" fill="#64748b" font-size="11">nulle sur l'axe neutre</text></g></svg>
:::

Sur la figure, le triangle rouge est τ le long d'un diamètre, et le triangle jaune est σ sur la hauteur de la section : même forme, parce que la contrainte est proportionnelle à la distance au centre.

::: exemple Le même arbre en torsion, puis en flexion (illustration)
Un arbre plein de diamètre d = 20 mm, en acier de Re = 320 MPa et Reg = 160 MPa, avec s = 2. Ces valeurs sont choisies pour s'entraîner.

1. **Les résistances pratiques.** Rpg = 160 / 2 = **80 MPa** et Rpe = 320 / 2 = **160 MPa**.
2. **Torsion, Mt = 40 N·m.** I0 / R = π × d³ / 16 = π × 8 000 / 16 ≈ 1 571 mm³, donc τmax = 40 000 / 1 571 ≈ **25,5 MPa**, inférieur à 80 : l'arbre résiste.
3. **Flexion, Mfz = 60 N·m.** IGz / v = π × d³ / 32 = π × 8 000 / 32 ≈ 785 mm³, donc σmax = 60 000 / 785 ≈ **76,4 MPa**, inférieur à 160 : l'arbre résiste. Pourquoi : le module de flexion d'un cercle vaut la moitié de son module de torsion.
4. **Rigidité en torsion.** I0 = π × d⁴ / 32 ≈ 15 708 mm⁴ et G = 80 000 MPa pour l'acier : θ = 40 000 / (80 000 × 15 708) ≈ 3,18 × 10⁻⁵ rad/mm. Avec θlimite = 1,0 × 10⁻⁴ rad/mm (valeur d'illustration, le manuel n'en donne aucune), l'arbre est assez rigide.

:::

::: piege Le module de torsion et le module de flexion
Pour un cercle, I0 / R = π × d³ / 16 est le **double** de IGz / v = π × d³ / 32. Utiliser I0 / R pour la flexion donne σmax = 60 000 / 1 571 ≈ 38,2 MPa, **la moitié** de la vraie valeur : on croit l'arbre deux fois moins chargé qu'il ne l'est, ce qui est l'erreur dangereuse. Chaque sollicitation a son module : I0 / R pour la torsion, IGz / v pour la flexion.
:::

::: propriete Même squelette, deux modules
Dans les deux cas : un moment, une contrainte linéaire, un maximum au bord, une comparaison avec une résistance pratique (Rpg = Reg / s en cisaillement, Rpe = Re / s en traction). Le coefficient de sécurité est le même s, mais la limite élastique change : **Reg** au glissement, **Re** à la traction. Cas particulier : sur l'axe de l'arbre, τ = 0, comme σ = 0 sur l'axe neutre.
:::

::: verifie
Le même arbre Ø 20 mm porte Mt = 100 N·m (Rpg = 80 MPa). Résiste-t-il en torsion ?
---
τmax = Mt / (I0 / R) = 100 000 / 1 571 ≈ **63,7 MPa**, inférieur à Rpg = 80 MPa : l'arbre résiste. On a utilisé I0 / R, le module de **torsion**, et non IGz / v.
:::

## 🧩 Synthèse : les sollicitations composées, et quelle condition choisir

Le touret avait un arbre plié et tordu, la machine de torsion un pignon arbré plié et tordu, la grue une flèche tirée et pliée. Aucune de ces pièces n'était en sollicitation simple.

Comment savoir, devant une pièce, quelle condition de résistance écrire ?

::: definition Les deux sollicitations composées du thème
- **Flexion–traction** (ou flexion–compression) : N et Mfz agissent ensemble. Les deux contraintes sont **normales** : elles s'additionnent, et la condition est **‖N‖ / S + ‖Mfz max‖ / (IGz / v) ≤ Rpe**. La traction décale la ligne neutre.
- **Flexion–torsion** : un arbre est en flexion–torsion quand son moment résultant en G contient un moment de torsion Mt (autour de l'axe de l'arbre) et un moment de flexion Mf (autour de z). Le dimensionnement se fait avec le **moment idéal de flexion** :

$$ Mfi = (1 − 1/(2λ)) × Mf + (1/(2λ)) × √(Mf² + Mt²) $$

où λ = Rpg / Rpe dépend du matériau (λ = 0,5 pour l'acier, donc Mfi = √(Mf² + Mt²)) ; la condition est alors Mfi / (IGz / v) ≤ Rpe.

**Pour choisir : regarder ce qui n'est pas nul dans la section la plus sollicitée.**

| Efforts non nuls | Sollicitation | Condition |
| --- | --- | --- |
| Mt seul | torsion simple | τmax ≤ Rpg |
| Mfz seul | flexion simple | σmax ≤ Rpe |
| N et Mfz | flexion–traction ou –compression | ‖N‖ / S + ‖Mfz max‖ / (IGz / v) ≤ Rpe |
| Mt et Mf | flexion–torsion | Mfi / (IGz / v) ≤ Rpe |
:::

::: exemple Quelle condition pour quelle section ? (illustration)
1. **Section où Mfz = 300 N·m et rien d'autre.** Seul Mfz est non nul : flexion simple, σmax = Mfz / (IGz / v) ≤ Rpe. Pourquoi : un seul moment, une seule contrainte.
2. **Section d'un tube de S = 800 mm² et IGz / v = 20 000 mm³ où N = 8 000 N et Mfz = 300 N·m.** N et Mfz sont tous deux non nuls : flexion–traction. σ = 8 000 / 800 + 300 000 / 20 000 = 10 + 15 = **25 MPa**. Pourquoi : les deux contraintes sont normales, on les additionne.
3. **Section d'un arbre en acier où Mf = 36 N·m et Mt = 48 N·m.** Flexion et torsion : flexion–torsion. Mfi = √(36² + 48²) = √(1 296 + 2 304) = √3 600 = **60 N·m**. Pourquoi : λ = 0,5 pour l'acier, la formule se réduit à la racine.

:::

::: piege Traiter la flexion–torsion comme la flexion–traction
Dans la flexion–traction, σN et σf sont toutes deux **normales**, donc 10 + 15 = 25 MPa. Dans la flexion–torsion, la flexion donne une contrainte normale σ et la torsion une contrainte **tangentielle** τ : elles n'ont pas la même direction et ne s'additionnent pas. On additionne encore moins Mf et Mt : 36 + 48 = 84 N·m, alors que Mfi = 60 N·m. Le moment idéal est là pour ramener les deux à une seule flexion équivalente.
:::

::: propriete Les cas simples sont des cas particuliers
Si N = 0, la flexion–traction redevient la flexion simple ; si Mt = 0, Mfi = Mf (flexion simple) ; si Mf = 0, Mfi = Mt pour l'acier (torsion comptée comme une flexion équivalente). Une condition composée ne contredit jamais une condition simple : elle la contient.
:::

::: verifie
Un tirant tendu porte N = 10 000 N et un moment Mfz = 20 000 N·mm ; sa section a S = 500 mm² et IGz / v = 5 000 mm³. Quelle condition faut-il écrire, et que vaut la contrainte maximale ?
---
N et Mfz sont non nuls : **flexion–traction**, et les deux contraintes sont normales. σ = N / S + Mfz / (IGz / v) = 10 000 / 500 + 20 000 / 5 000 = 20 + 4 = **24 MPa**, à comparer à Rpe.
:::

## 🧭 La méthode qui reste : huit marches

Devant une pièce sollicitée, tu reprends toujours cet ordre :

1. **Modèle** : une poutre, ses points, ses forces, ses hypothèses (poids négligés, liaisons parfaites), un repère lié à la poutre.
2. **Projeter** chaque force : cosinus sur l'axe avec lequel l'angle est mesuré, sinus sur l'autre.
3. **Équilibrer** : somme nulle sur x et sur y, puis contrôle par les moments au pivot ; on en tire l'action inconnue.
4. **Couper** : un tronçon par intervalle ; N, Ty et Mfz du morceau d'un seul côté ; Mfz nul à une extrémité libre.
5. **Diagrammes** : sollicitation de chaque tronçon (N et Mfz : flexion–traction ou –compression) et section la plus sollicitée (Mfz maximal).
6. **Géométrie** : S = B² − (B − 2T)² et IGz / v = (B⁴ − (B − 2T)⁴) / (6 × B) pour un tube carré.
7. **Contraintes** : σN = N / S, σf = Mfz / (IGz / v), σéq = σN + σf ≤ Rpe = Re / s.
8. **Choisir** le plus petit tube qui convient ; pour toute autre pièce, choisir la condition d'après les efforts non nuls (Mt, Mfz, N, Mt et Mf).

::: retenir
Une flèche est **tirée et pliée** : N et Mfz s'additionnent en contraintes normales, **σéq = N / S + Mfz / (IGz / v) ≤ Re / s**, et le tube retenu est le plus petit qui vérifie la condition ; pour toute pièce, on choisit la condition d'après les efforts non nuls de la section la plus sollicitée : **Mt** (τmax ≤ Rpg), **Mfz** (σmax ≤ Rpe), **N et Mfz** (somme des contraintes), **Mt et Mf** (moment idéal Mfi).
:::

> 🏆 Le thème « Comportement des solides déformables » est bouclé : tu sais tordre, plier, tirer et superposer, puis dire de quoi une pièce a besoin pour résister. La suite du programme t'attend avec l'axe « Réalisation et production », et son thème « Obtention des pièces ».
