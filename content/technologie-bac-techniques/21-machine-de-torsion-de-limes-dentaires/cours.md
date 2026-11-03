# 🛠️ La machine de torsion de limes dentaires : du couple à la section de l'arbre

> 💡 «Un arbre qui transmet un couple ne casse pas parce qu'il est faible, mais parce qu'on a oublié qu'il est tordu et plié en même temps. Ce chapitre apprend à calculer les deux, puis à choisir son diamètre.»

La **machine de torsion de limes dentaires** tord des tiges d'acier inoxydable pour en faire les limes des dentistes. Un moteur Mt1 fait tourner le mandrin, et un second moteur Mt2 déplace le **traînard** par un système vis-écrou, à travers une **boîte de vitesses**. Le manuel (activité 5 du thème « Comportement des solides déformables ») demande de dimensionner une pièce de cette boîte, le **pignon arbré (39)**, pour qu'il « résiste en toute sécurité ». Le chemin tient en huit notions : puissance et couple, efforts sur la denture, modèle de poutre, torsion, flexion, section dangereuse, moment idéal, diamètre.

> 🗡️ Le manuel ne donne **aucun corrigé**, et son dessin d'ensemble n'est pas reproduit ici. Ce cours n'enseigne donc que des règles standard de génie mécanique, et il dit à chaque fois ce qui vient du manuel (le rendement 0,97, la puissance de 1 000 W, l'angle de 20°, les cotes 40, 50 et 35 mm, l'acier 30CrNiMo16 de Re = 700 MPa, le coefficient s = 2, le rapport D = 3/2 × d) et ce qui est une **valeur d'illustration** choisie pour s'entraîner (la vitesse de l'arbre, le rayon du pignon). Les schémas sont des **schémas de principe**, redessinés pour expliquer.

## ⚙️ Du moteur à l'arbre : puissance transmise et couple

Le moteur de la boîte fournit 1 000 W, mais une boîte de vitesses perd un peu de puissance en frottements. Le manuel donne son rendement : η = 0,97.

Combien de puissance arrive au pignon arbré (39), et quel couple cette puissance fait-elle porter à l'arbre ?

::: definition Puissance transmise et couple
Un mécanisme de **rendement** η transmet à sa sortie la part η de la puissance qu'il reçoit :

$$ P = η × Pm $$

Cette puissance est le produit du **couple** C par la vitesse angulaire ω de l'arbre, d'où :

$$ C = P / ω $$

$$ ω = 2π × N / 60 $$

P est en watts (W), ω en radians par seconde (rad/s), N en tours par minute (tr/min) et C en newtons-mètres (N·m).
:::

::: exemple Du moteur au couple C39 (illustration)
Données du manuel : Pm = 1 000 W et η = 0,97. Valeur d'illustration : l'arbre (39) tourne à N = 70 tr/min (le manuel donne cette vitesse pour la vis mère (36) ; celle de l'arbre (39) dépend de la chaîne de la boîte, que son dessin d'ensemble détaille).
1. **Puissance transmise.** P = 0,97 × 1 000 = **970 W**. Pourquoi : la boîte perd 3 %, il en arrive 97 %.
2. **Vitesse angulaire.** ω = 2π × 70 / 60 ≈ **7,33 rad/s**. Pourquoi : la relation P = C × ω exige des rad/s, pas des tr/min.
3. **Couple.** C39 = 970 / 7,33 ≈ **132,3 N·m**. Pourquoi : on isole C dans P = C × ω.
4. **Contrôle.** C39 × ω = 132,3 × 7,33 ≈ 970 W, la puissance de départ.

:::

::: piege Les tours par minute ne sont pas des radians par seconde
Diviser P par N directement donne 970 / 70 ≈ 13,9 N·m : plus de neuf fois trop petit, parce que 1 tr/min vaut 2π / 60 ≈ 0,105 rad/s. Autres glissades : partir de Pm au lieu de η × Pm (le couple est alors trop grand de 3 %), ou diviser par η au lieu de multiplier (la sortie dépasserait l'entrée).
:::

::: propriete Le rendement ne fait que retrancher
Comme η est compris entre 0 et 1, la puissance de sortie ne dépasse jamais celle d'entrée :
- η = 0,97 : P = 970 W, soit 30 W perdus en chaleur ;
- η = 1 (mécanisme idéal, sans aucune perte) : P = Pm ;
- un η supérieur à 1 créerait de l'énergie, ce qui n'existe pas.

À vitesse donnée, une puissance plus petite donne un couple plus petit, dans le même rapport.
:::

::: verifie
Un réducteur de rendement 0,85 reçoit 600 W. Son arbre de sortie tourne à 90 tr/min. Quel couple transmet-il ?
---
P = 0,85 × 600 = 510 W ; ω = 2π × 90 / 60 ≈ 9,42 rad/s ; **C = 510 / 9,42 ≈ 54,1 N·m**. On commence par retrancher les pertes (η), puis on passe en rad/s avant de diviser.
:::

## 🦷 La denture pousse l'arbre : efforts tangentiel et radial

Le pignon arbré (39) engrène avec une roue dentée. Au contact, une dent de la roue pousse sur une dent du pignon : c'est un seul effort, mais il n'est pas dirigé le long du cercle.

Quelle partie de cet effort fait tourner l'arbre, et quelle partie ne fait que le presser vers son axe ?

::: definition Effort tangentiel T et effort radial R
L'effort **F** exercé par la dent se décompose en deux efforts perpendiculaires :
- l'effort **tangentiel T**, tangent au cercle primitif du pignon : c'est lui qui fait tourner l'arbre ;
- l'effort **radial R**, dirigé vers l'axe : il presse l'arbre sur ses appuis, sans le faire tourner.

L'angle entre F et T est l'**angle de pression** α ; le manuel le donne : 20°. Avec r le **rayon primitif** du pignon :

$$ C39 = T × r $$

$$ R = T × tan α $$

$$ F = T / cos α $$
:::

::: figure L'effort F de la roue sur la dent du pignon se décompose en T, tangent au cercle, et R, dirigé vers le centre O. L'angle entre F et T vaut 20° et r est le rayon primitif du pignon. Schéma de principe, sans les dents
<svg viewBox="0 0 340 312"><title>Décomposition de l'effort de la dent en effort tangentiel T et effort radial R</title><circle cx="130" cy="195" r="105" fill="#0f6e56" fill-opacity="0.12" stroke="#0f172a" stroke-width="2"/><line x1="130" y1="195" x2="130" y2="137.3" stroke="#94a3b8" stroke-width="1.5" stroke-linecap="round" stroke-dasharray="5 4"/><line x1="260" y1="90" x2="260" y2="137.3" stroke="#94a3b8" stroke-width="1.5" stroke-linecap="round" stroke-dasharray="5 4"/><line x1="130" y1="137.3" x2="260" y2="137.3" stroke="#94a3b8" stroke-width="1.5" stroke-linecap="round" stroke-dasharray="5 4"/><line x1="130" y1="90" x2="250" y2="90" stroke="#0f172a" stroke-width="3" stroke-linecap="round"/><polygon points="260 90 250 94.2 250 85.8" fill="#0f172a"/><line x1="130" y1="90" x2="130" y2="127.3" stroke="#0f6e56" stroke-width="3" stroke-linecap="round"/><polygon points="130 137.3 125.8 127.3 134.2 127.3" fill="#0f6e56"/><line x1="130" y1="90" x2="250.6" y2="133.9" stroke="#b45309" stroke-width="3" stroke-linecap="round"/><polygon points="260 137.3 249.2 137.8 252 129.9" fill="#b45309"/><path d="M185 90 A55 55 0 0 1 181.7 108.8" fill="none" stroke="#0f172a" stroke-width="1.5"/><circle cx="130" cy="195" r="3.5" fill="#0f172a"/><circle cx="130" cy="90" r="4" fill="#0f172a"/><g><text x="200" y="81" font-size="12" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">T</text><text x="119" y="122" font-size="12" font-weight="600" text-anchor="middle" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">R</text><text x="274" y="151.3" font-size="12" font-weight="600" text-anchor="middle" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">F</text><text x="230" y="107" font-size="11" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">20°</text><text x="119" y="175" font-size="12" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">r</text><text x="144" y="211" font-size="11" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">O</text></g></svg>
:::

Sur le dessin, T est le côté horizontal du triangle rectangle, R son côté vertical et F l'hypoténuse : les trois formules viennent directement de ce triangle.

::: exemple Les efforts sur le pignon arbré (illustration)
Suite du calcul précédent : C39 = 132,3 N·m. Valeur d'illustration : le rayon primitif de (39), que le manuel fait relever sur son dessin, est r = 50 mm.
1. **Unités.** r = 50 mm = 0,05 m. Pourquoi : C39 est en N·m, T sortira en N.
2. **Effort tangentiel.** T = 132,3 / 0,05 = **2 646 N**. Pourquoi : C39 = T × r, on isole T.
3. **Effort radial.** R = T × tan 20° ≈ 2 646 × 0,364 ≈ **963 N**. Pourquoi : R est le côté opposé à l'angle et T le côté adjacent, et tan = opposé / adjacent.
4. **Effort total.** F = T / cos 20° ≈ 2 646 / 0,940 ≈ **2 816 N**. Contrôle : l'hypoténuse est la plus grande des trois, et 2 646² + 963² ≈ 2 816².

:::

::: piege R se calcule avec tan, pas avec sin
On écrit parfois R = T × sin 20°, ce qui donne environ 905 N au lieu de 963 N. Le sinus relie R à l'hypoténuse F (R = F × sin 20° ≈ 2 816 × 0,342 ≈ 963 N), pas à T. Autre erreur classique : mettre le **diamètre** primitif à la place du rayon, qui divise T par deux.
:::

::: propriete Pour 20°, R est plus petit que T
Tant que α reste inférieur à 45°, tan α est inférieur à 1 et R est plus petit que T :
- α = 20° : R ≈ 0,364 × T, soit 36 % de T ;
- α = 0° (effort purement tangentiel) : R = 0 ;
- plus α grandit, plus R prend de poids.

Le manuel demande de **négliger R devant T** dans la suite : c'est une **hypothèse de l'énoncé**, qui garde une seule charge dans le modèle de l'arbre. Elle simplifie le calcul, sans que R soit petit en soi.
:::

::: verifie
Un pignon de rayon primitif 30 mm transmet un couple de 45 N·m, avec un angle de pression de 20°. Que valent T et R ?
---
T = C / r = 45 / 0,03 = **1 500 N** (rayon en mètres). R = T × tan 20° ≈ 1 500 × 0,364 ≈ **546 N** : on applique tan à T, le côté adjacent.
:::

## 📐 Du pignon à la poutre : le modèle et les réactions d'appui

Pour savoir comment l'arbre travaille, on remplace sa forme réelle par un trait : une **poutre**. Deux roulements la portent, et l'effort T pousse sur elle en un point.

Quelle force chaque appui exerce-t-il pour tenir la poutre immobile ?

::: definition Le modèle de poutre
Le pignon arbré (39) est assimilé à une **poutre** le long de l'axe x, avec les hypothèses du manuel : section creuse, poids des pièces et frottements négligés. Le manuel cote 4 points :
- **A** (x = 0), **appui articulé** : il retient l'arbre sans le laisser se déplacer, et exerce une réaction verticale **R_A** ;
- **C** (x = 40 mm), **point de réduction** de la denture : l'effort **T** y est ramené sur l'axe ;
- **B** (x = 90 mm), **appui à rouleaux** : il exerce une réaction verticale **R_B** ;
- **D** (x = 125 mm), extrémité de l'arbre.

Comme la poutre est immobile, les forces et leurs moments s'équilibrent :

$$ R_A + R_B = T $$

$$ R_B × AB = T × AC $$
:::

::: figure Le modèle de poutre du pignon arbré, avec les cotes du manuel : appui articulé en A, appui à rouleaux en B, effort T appliqué en C, extrémité D où le couple C39 ressort, repris par le couple résistant, dans ce modèle. R_A et R_B sont les réactions des appuis. Schéma de principe, x se mesure à partir de A
<svg viewBox="0 0 430 225"><title>Modèle de poutre du pignon arbré : appuis A et B, effort T en C, couple en D</title><rect x="37" y="92" width="316" height="8" fill="#cbd5e1" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round"/><polygon points="45 100 31 124 59 124" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round"/><line x1="25" y1="124" x2="65" y2="124" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><polygon points="261 100 247 120 275 120" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round"/><circle cx="254" cy="123.5" r="3.5" fill="#ffffff" stroke="#0f172a" stroke-width="1.4"/><circle cx="268" cy="123.5" r="3.5" fill="#ffffff" stroke="#0f172a" stroke-width="1.4"/><line x1="241" y1="128" x2="281" y2="128" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><line x1="141" y1="28" x2="141" y2="80" stroke="#b45309" stroke-width="3" stroke-linecap="round"/><polygon points="141 90 136.8 80 145.2 80" fill="#b45309"/><text x="151" y="40" font-size="12" font-weight="600" text-anchor="start" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">T</text><line x1="45" y1="176" x2="45" y2="142" stroke="#0f6e56" stroke-width="3" stroke-linecap="round"/><polygon points="45 132 49.2 142 40.8 142" fill="#0f6e56"/><line x1="261" y1="176" x2="261" y2="142" stroke="#0f6e56" stroke-width="3" stroke-linecap="round"/><polygon points="261 132 265.2 142 256.8 142" fill="#0f6e56"/><text x="54" y="166" font-size="12" font-weight="600" text-anchor="start" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">R<tspan font-size="9" dy="3">A</tspan></text><text x="270" y="166" font-size="12" font-weight="600" text-anchor="start" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">R<tspan font-size="9" dy="3">B</tspan></text><path d="M353 66 Q381 96 351 126" fill="none" stroke="#0f172a" stroke-width="2.4" stroke-linecap="round"/><polygon points="349 128 352 116 361 124" fill="#0f172a"/><text x="387" y="98" font-size="12" font-weight="600" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">C39</text><line x1="45" y1="200" x2="345" y2="200" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><line x1="45" y1="195" x2="45" y2="205" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><text x="45" y="221" font-size="13" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">A</text><line x1="141" y1="195" x2="141" y2="205" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><text x="141" y="221" font-size="13" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">C</text><line x1="261" y1="195" x2="261" y2="205" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><text x="261" y="221" font-size="13" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">B</text><line x1="345" y1="195" x2="345" y2="205" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><text x="345" y="221" font-size="13" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">D</text><text x="93" y="194" font-size="11" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">40</text><text x="201" y="194" font-size="11" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">50</text><text x="303" y="194" font-size="11" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">35</text><line x1="141" y1="100" x2="141" y2="194" stroke="#94a3b8" stroke-width="1.2" stroke-linecap="round" stroke-dasharray="4 4"/><line x1="345" y1="100" x2="345" y2="194" stroke="#94a3b8" stroke-width="1.2" stroke-linecap="round" stroke-dasharray="4 4"/></svg>
:::

La seconde équation prend les moments autour de A : AB est la distance entre les appuis, AC la distance de l'effort à A, et R_A n'y figure pas puisque son bras de levier est nul.

::: exemple Les réactions de A et de B (illustration)
Avec T = 2 646 N du calcul précédent et les cotes du manuel : AC = 40 mm, CB = 50 mm, donc AB = 40 + 50 = 90 mm.
1. **Moments autour de A.** R_B × 90 = 2 646 × 40, donc R_B = 105 840 / 90 = **1 176 N**. Pourquoi : on choisit A pour éliminer l'inconnue R_A.
2. **Équilibre des forces.** R_A = T − R_B = 2 646 − 1 176 = **1 470 N**. Pourquoi : la somme des réactions est égale à la charge.
3. **Contrôle autour de B.** R_A × 90 = 132 300 N·mm et T × CB = 2 646 × 50 = 132 300 N·mm : les deux moments s'égalent.

:::

::: piege Le plus proche porte le plus
On partage parfois la charge en deux moitiés égales (1 323 N par appui). C'est juste seulement si l'effort est au milieu de AB. Ici C est plus près de A que de B (40 mm contre 50 mm) : A porte plus, 1 470 N contre 1 176 N. Autre glissade : croiser les distances, c'est-à-dire écrire R_A = T × AC / AB (1 176 N) : la réaction d'un appui est proportionnelle à la distance de **l'autre** appui à la charge.
:::

::: propriete Les réactions suivent la position de la charge
$$ R_A = T × CB / AB $$

$$ R_B = T × AC / AB $$

- charge au milieu (AC = CB) : les deux réactions valent T / 2 ;
- charge au-dessus de A (AC = 0) : R_A = T et R_B = 0, l'appui A porte tout ;
- la somme R_A + R_B reste égale à T, quelle que soit la position de la charge.
:::

::: verifie
Une poutre repose sur deux appuis distants de 90 mm et porte une charge T = 1 800 N à 30 mm de A. Que valent R_A et R_B ?
---
AC = 30 mm et CB = 60 mm. R_B = T × AC / AB = 1 800 × 30 / 90 = **600 N** (moments autour de A), puis R_A = 1 800 − 600 = **1 200 N**. Le plus proche de la charge, A, porte le plus.
:::

## 🌀 Le moment de torsion : où l'arbre est-il tordu ?

Quand on essore un torchon, seule la partie comprise entre les deux mains est tordue : le reste suit sans se vriller. Un arbre se comporte de même.

Sur quelle longueur du pignon arbré (39) le couple passe-t-il, et que vaut-il ?

::: definition Le moment de torsion Mt
Dans une section de l'arbre, le **moment de torsion Mt** est le couple que la partie d'un côté transmet à l'autre autour de l'axe. Pour le trouver, on coupe l'arbre et on regarde **un seul côté**, le plus simple : Mt est la somme des couples qui s'y appliquent.

Dans le modèle de ce cours, le couple C39 entre en C par la denture (l'effort T de la roue 33) et ressort à l'extrémité D, où il est repris par le couple résistant : le couple passe donc de C à D.
:::

::: exemple Mt le long de l'arbre (illustration)
Avec C39 = 132,3 N·m, on teste une coupe dans chaque zone.
1. **Coupe entre C et D** (par exemple x = 100 mm). Le côté droit ne contient que l'extrémité D, où ressort le couple : **Mt = C39 = 132,3 N·m**. Pourquoi : on choisit le côté qui a le moins d'actions.
2. **Coupe entre A et C** (par exemple x = 20 mm). Le côté gauche ne contient que l'appui A, dont la réaction ne tourne pas autour de l'axe : **Mt = 0**. Pourquoi : aucun couple n'y est appliqué.
3. **Contrôle en C.** T × r = 2 646 × 0,05 = 132,3 N·m : la denture apporte exactement le couple qui ressort en D. Le moment de torsion saute de 0 à 132,3 N·m en passant par C.

:::

::: piege Tout l'arbre n'est pas tordu
On peut croire que Mt vaut C39 sur toute la longueur, puisque l'arbre « transmet un couple ». Le couple ne circule qu'entre l'endroit où il entre (la denture, en C) et celui où il ressort (D). Le tronçon AC ne transmet rien : le torchon n'est pas tordu au-delà de la main qui le retient.
:::

::: propriete Mt change seulement là où un couple est appliqué
Entre deux sections sans couple appliqué, Mt est **constant** :
- de D à C : Mt = C39 = 132,3 N·m ;
- de C à A : Mt = 0, après un saut de 132,3 N·m en C ;
- un diagramme de Mt est fait de **paliers** reliés par des sauts aux points où un couple est appliqué, jamais de droites inclinées.

Mt se porte en valeur positive : seule sa grandeur compte pour la résistance.
:::

::: verifie
Même modèle, avec C39 = 60 N·m entrant en C par la denture et ressortant en D. Que valent Mt à x = 20 mm et à x = 100 mm ?
---
À x = 20 mm (entre A et C), le côté gauche ne contient que l'appui A : **Mt = 0**. À x = 100 mm (entre C et D), le côté droit ne contient que le couple de sortie : **Mt = 60 N·m**.
:::

## 📈 Le moment fléchissant : tronçon par tronçon

L'effort T plie l'arbre entre ses appuis, comme une planche qui fléchit sous une charge. Mais elle ne fléchit pas partout autant : près d'un appui elle est peu pliée.

Comment le pliage varie-t-il le long de l'axe, et où est-il le plus grand ?

::: definition Le moment fléchissant Mf(x)
Dans la section d'abscisse x, le **moment fléchissant Mf** est la somme des moments, par rapport à cette section, des forces qui agissent d'**un côté** de la coupe (ici le côté gauche). Une force à la distance d de la coupe y compte pour force × d.

Il change de formule à chaque effort ou appui rencontré : on découpe l'arbre en **tronçons** et on écrit une expression par tronçon.
:::

::: exemple Les trois tronçons du pignon arbré (illustration)
Avec R_A = 1 470 N, T = 2 646 N et les cotes du manuel (A en 0, C en 40, B en 90, D en 125 mm). On regarde le côté gauche.
1. **Tronçon 1, 0 ≤ x ≤ 40 mm.** Seule R_A agit : Mf = R_A × x = 1 470 × x. En A : 0 ; en C : 1 470 × 40 = **58 800 N·mm = 58,8 N·m**.
2. **Tronçon 2, 40 ≤ x ≤ 90 mm.** T s'ajoute, à la distance (x − 40) de la coupe : Mf = R_A × x − T × (x − 40). En C : 58 800 N·mm (même valeur qu'avant : pas de saut) ; en B : 1 470 × 90 − 2 646 × 50 = 132 300 − 132 300 = **0**.
3. **Tronçon 3, 90 ≤ x ≤ 125 mm.** On regarde plutôt le côté droit : il ne contient aucune force (poids négligés) ; le couple C39 qui s'y applique tord l'arbre mais ne le plie pas. Donc **Mf = 0**. En D : 0.
4. **Valeurs aux quatre points.**

| point | A | C | B | D |
| --- | --- | --- | --- | --- |
| x (mm) | 0 | 40 | 90 | 125 |
| Mf (N·m) | 0 | 58,8 | 0 | 0 |

Ces valeurs relient les segments de droite du diagramme : Mf monte de 0 à 58,8 N·m de A à C, puis redescend à 0 en B.

:::

::: piege Oublier T dans le tronçon 2
Si l'on garde Mf = R_A × x au-delà de C, on trouve en B : 1 470 × 90 = 132 300 N·mm, soit 132,3 N·m, alors que le moment fléchissant d'un appui à rouleaux est nul. L'effort T a bien été oublié. Autre erreur : écrire T × x au lieu de T × (x − 40), c'est-à-dire mesurer son bras de levier depuis A et non depuis la coupe.
:::

::: propriete La forme du diagramme de Mf
- entre deux efforts, Mf est une **droite** (expression du premier degré en x) ;
- Mf ne fait pas de saut au passage d'une charge : les deux tronçons donnent la même valeur en C (58,8 N·m dans les deux cas) ;
- il est nul à l'extrémité libre D et au niveau d'un appui à rouleaux ;
- avec une seule charge, il est **maximal sous la charge**, ici en C ;
- sur un tronçon sans charge au-delà du dernier appui (de B à D), il reste nul.
:::

::: verifie
Une poutre repose sur deux appuis distants de 90 mm et porte T = 1 800 N à 30 mm de A (R_A = 1 200 N). Quel est le moment fléchissant en C et en B ?
---
Côté gauche de C : Mf(C) = R_A × 30 = 1 200 × 30 = **36 000 N·mm = 36 N·m**. En B : Mf(B) = 1 200 × 90 − 1 800 × 60 = 108 000 − 108 000 = **0**. Le maximum est sous la charge, et l'appui B ne subit aucun moment.
:::

## 🎯 La section la plus sollicitée : flexion et torsion ensemble

Les deux diagrammes sont tracés. Le premier montre où l'arbre est tordu, le second où il est plié, et ils ne se ressemblent pas.

Quelle section faut-il dimensionner, et à quelle sollicitation est-elle soumise ?

::: definition Section dangereuse et sollicitation composée
La **section la plus sollicitée** (ou section dangereuse) est celle où les moments sont les plus grands : c'est elle que l'on dimensionne, puisque si elle tient, toutes les autres tiennent.

Une section soumise en même temps à plusieurs sollicitations simples subit une **sollicitation composée**. Ici, Mf correspond à de la **flexion** et Mt à de la **torsion** : on parle de **flexion–torsion**.
:::

::: figure Les diagrammes de Mt et de Mf du pignon arbré, en valeur absolue et à la même échelle (C39 = 132,3 N·m, Mf maximal = 58,8 N·m). Mt est un palier de C à D, Mf est une pointe en C, repérée par la verticale verte en pointillés épais
<svg viewBox="0 0 430 330"><title>Diagrammes du moment de torsion et du moment fléchissant du pignon arbré</title><line x1="45" y1="28" x2="45" y2="300" stroke="#94a3b8" stroke-width="1.2" stroke-linecap="round" stroke-dasharray="4 4"/><text x="45" y="20" font-size="13" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">A</text><line x1="141" y1="28" x2="141" y2="300" stroke="#0f6e56" stroke-width="2.2" stroke-linecap="round" stroke-dasharray="4 4"/><text x="141" y="20" font-size="13" font-weight="600" text-anchor="middle" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">C</text><line x1="261" y1="28" x2="261" y2="300" stroke="#94a3b8" stroke-width="1.2" stroke-linecap="round" stroke-dasharray="4 4"/><text x="261" y="20" font-size="13" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">B</text><line x1="345" y1="28" x2="345" y2="300" stroke="#94a3b8" stroke-width="1.2" stroke-linecap="round" stroke-dasharray="4 4"/><text x="345" y="20" font-size="13" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">D</text><line x1="33" y1="134" x2="361" y2="134" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><polygon points="45 134 141 134 141 74.5 345 74.5 345 134" fill="#0f6e56" fill-opacity="0.18" stroke="#0f6e56" stroke-width="2.4" stroke-linejoin="round"/><text x="6" y="46" font-size="12" font-weight="600" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Mt (N·m)</text><text x="243" y="67.5" font-size="12" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">132,3</text><text x="93" y="126" font-size="12" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><text x="369" y="138" font-size="12" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x</text><line x1="33" y1="280" x2="361" y2="280" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><polygon points="45 280 141 253.5 261 280 345 280" fill="#0f6e56" fill-opacity="0.18" stroke="#0f6e56" stroke-width="2.4" stroke-linejoin="round"/><text x="6" y="192" font-size="12" font-weight="600" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Mf (N·m)</text><text x="141" y="246.5" font-size="12" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">58,8</text><text x="369" y="284" font-size="12" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x</text></svg>
:::

On lit sur le dessin que la flexion est maximale en C et que la torsion y est complète (132,3 N·m) : aucune autre section n'a un Mf plus grand, ni un Mt plus grand.

::: exemple Choisir la section et nommer la sollicitation (illustration)
À partir des deux diagrammes de la figure.
1. **Candidates.** Le maximum de Mf est en C (58,8 N·m). Le palier de Mt, lui, s'étend de C à D.
2. **Comparaison.** En B ou en D, Mf vaut 0 : seule la torsion agit. En C, côté D, on a **à la fois** le maximum de Mf et le maximum de Mt : aucune autre section n'est plus chargée en flexion, ni en torsion. La section la plus sollicitée est donc **la section C, du côté de D**.
3. **Sollicitation.** Flexion (Mf = 58,8 N·m) et torsion (Mt = 132,3 N·m) agissent dans la même section : c'est une **flexion–torsion**, une sollicitation composée. Pourquoi : on justifie en citant les deux moments non nuls.

:::

::: piege Un seul diagramme ne suffit pas
Si l'on lit seulement Mf, on trouve C mais on ignore que, juste à gauche de C, la torsion est nulle : cette section n'est pas la plus chargée. Si l'on lit seulement Mt, tout le palier de C à D semble équivalent. C'est la lecture **des deux** qui désigne C, côté D, comme la seule section où les deux moments sont à leur maximum.
:::

::: propriete De la sollicitation simple à la sollicitation composée
Dans une section donnée :
- seul Mf non nul : flexion simple ;
- seul Mt non nul : torsion simple ;
- Mf et Mt non nuls ensemble : flexion–torsion, sollicitation composée.

Sur le même arbre, ces cas se succèdent : en B et en D, la torsion est seule (torsion simple) ; en C, côté D, flexion et torsion s'ajoutent.
:::

::: verifie
Sur ce même arbre, une section entre A et C subit Mf = 30 N·m. Quelle sollicitation y règne, et pourquoi n'est-ce pas la section dangereuse ?
---
Entre A et C, Mt = 0 : seul Mf agit, c'est une **flexion simple**. Mf y reste sous son maximum (58,8 N·m en C) et la torsion y manque : la section C, côté D, la dépasse sur les deux moments.
:::

## 🧮 Le moment idéal de flexion : un seul moment pour deux

On sait calculer un diamètre quand l'arbre est seulement plié. Notre section est pliée et tordue à la fois.

Peut-on remplacer le couple (Mf, Mt) par un seul moment de flexion, qui serait aussi dangereux ?

::: definition Le moment idéal de flexion Mfi
C'est le **moment de flexion équivalent** à la flexion et à la torsion réunies. Le manuel donne la formule :

$$ Mfi = (1 − 1/(2λ)) × Mf + (1/(2λ)) × √(Mf² + Mt²) $$

λ est le rapport entre la résistance pratique au glissement et la résistance pratique à l'extension du matériau : λ = Rpg / Rpe. **Pour l'acier, λ = 0,5** (valeur du manuel). Alors 1 / (2λ) = 1, le premier terme disparaît et il reste :

$$ Mfi = √(Mf² + Mt²) $$
:::

::: exemple Mfi dans la section C (illustration)
Avec Mf = 58,8 N·m et Mt = 132,3 N·m.
1. **Simplifier la formule.** λ = 0,5, donc 1 / (2 × 0,5) = 1 et 1 − 1 = 0 : le terme en Mf seul s'annule. Pourquoi : c'est la seule simplification, la racine reste.
2. **Carrés.** Mf² = 58,8² ≈ 3 457 et Mt² = 132,3² ≈ 17 503.
3. **Racine de la somme.** Mfi = √(3 457 + 17 503) = √20 960 ≈ **144,8 N·m**.
4. **Contrôle.** Mfi est plus grand que chacun des deux moments (58,8 et 132,3) et plus petit que leur somme (191,1) : le résultat est plausible.

:::

::: piege Les moments ne s'additionnent pas
Écrire Mfi = Mf + Mt = 58,8 + 132,3 = 191,1 N·m donne un moment idéal trop grand de 32 %, donc un arbre surdimensionné : la flexion crée des contraintes normales et la torsion des contraintes tangentielles : elles ne s'ajoutent pas comme deux nombres de même nature. Autres glissades : oublier la racine (garder Mf² + Mt² ≈ 20 960, qui n'est plus un moment) ou ne garder que Mt (132,3 N·m), ce qui oublie la flexion.
:::

::: propriete Mfi encadre les deux moments
Avec λ = 0,5 :
- Mfi est plus grand que Mf et plus grand que Mt, sans dépasser leur somme ;
- si Mt = 0 (flexion simple), Mfi = Mf ;
- si Mf = 0 (torsion simple), Mfi = Mt.

La formule retrouve ainsi les deux sollicitations simples comme cas particuliers.
:::

::: verifie
Dans une section, Mf = 20 N·m et Mt = 21 N·m, avec λ = 0,5. Que vaut Mfi ?
---
λ = 0,5 : Mfi = √(Mf² + Mt²) = √(400 + 441) = √841 = **29 N·m**. Les carrés s'additionnent avant la racine : 20 + 21 = 41 serait faux.
:::

## 🔧 Dimensionner la section creuse : de Mfi à D et à d

Le moment idéal est connu : 144,8 N·m. Reste à choisir le diamètre d'un arbre creux en acier 30CrNiMo16, de limite élastique Re = 700 MPa, avec un coefficient de sécurité s = 2 et un rapport D = 3/2 × d.

Quel diamètre extérieur D minimal garantit que l'arbre tienne en toute sécurité ?

::: definition Condition de résistance à la flexion
Le matériau supporte sans danger une contrainte **Rpe = Re / s**, la résistance pratique à l'extension (Re est la limite élastique, s le coefficient de sécurité). La contrainte maximale dans la section vaut Mfi / (I/v), où I/v est le **module de flexion** de la section. La condition de résistance s'écrit :

$$ Mfi / (I/v) ≤ Re / s $$

Pour une section creuse de diamètre extérieur D et de diamètre intérieur d :

$$ I/v = π × (D⁴ − d⁴) / (32 × D) $$

Avec D = 3/2 × d, on a d = D / 1,5 et d⁴ = D⁴ / 5,06, donc I/v ≈ 0,0788 × D³. Les unités : Mfi en N·mm, I/v en mm³, Re / s en MPa (N/mm²).
:::

::: exemple D_min et d pour le pignon arbré (illustration)
Avec Mfi = 144,8 N·m = 144 800 N·mm, Re = 700 MPa, s = 2 et D = 3/2 × d (données du manuel).
1. **Résistance pratique.** Rpe = Re / s = 700 / 2 = **350 MPa**. Pourquoi : on garde une marge de sécurité de 2 par rapport à la limite élastique.
2. **Condition.** 144 800 / (0,0788 × D³) ≤ 350, donc D³ ≥ 144 800 / (0,0788 × 350) ≈ **5 250 mm³**. Pourquoi : on isole D³ en passant le module de flexion de l'autre côté.
3. **Diamètre extérieur minimal.** D_min = ∛5 250 ≈ **17,4 mm**. Pourquoi : D est élevé au cube dans I/v.
4. **Diamètre intérieur.** d = D / 1,5 = 17,4 / 1,5 ≈ **11,6 mm**. Pour D = D_min, c'est le **plus grand** trou permis : un trou plus large baisserait I/v sous la valeur nécessaire.
5. **Contrôle.** I/v = 0,0788 × 17,4³ ≈ 415 mm³ et 144 800 / 415 ≈ 349 MPa, soit moins que 350 MPa : l'arbre tient.

:::

::: piege Le trou, l'unité et la sécurité
Traiter l'arbre comme plein (I/v = π × D³ / 32 ≈ 0,0982 × D³) donne D ≈ 16,2 mm : environ 7 % trop petit, parce que le trou affaiblit l'arbre. Garder Mfi en N·m avec des MPa donne un diamètre dix fois trop petit. Comparer à Re au lieu de Re / s oublie la marge de sécurité et laisse un arbre trop fin (environ 13,8 mm).
:::

::: propriete Un diamètre qui varie comme une racine cubique
D³ est proportionnel à Mfi / Rpe, donc D_min = ∛(Mfi / (0,0788 × Rpe)) :
- Mfi doublé : D_min est multiplié par ∛2 ≈ 1,26, non par 2 ;
- s passe de 2 à 3 : Rpe baisse d'un tiers et D_min augmente d'environ 14 % (∛1,5 ≈ 1,145) ;
- plus Re est grand, plus D_min est petit : un acier plus résistant permet un arbre plus fin.
:::

::: verifie
Mfi = 100 N·m, Rpe = 200 MPa et D = 3/2 × d. Que valent D_min et d ?
---
D³ ≥ 100 000 / (0,0788 × 200) ≈ 6 345, donc **D_min ≈ 18,5 mm** (racine cubique). Puis d = 18,5 / 1,5 ≈ **12,3 mm**.
:::

## 🧭 La méthode qui reste : huit marches

Devant un arbre qui transmet un couple par une denture, tu reprends toujours cet ordre :

1. **Couple** : P = η × Pm, ω = 2π × N / 60, C = P / ω.
2. **Efforts** : T = C / r (en mètres), R = T × tan α, F = T / cos α.
3. **Modèle** : poutre sur deux appuis, T en C ; R_A = T × CB / AB, R_B = T × AC / AB.
4. **Torsion** : Mt = C39 entre la denture et la sortie du couple, 0 ailleurs.
5. **Flexion** : un tronçon par intervalle ; Mf nul à l'extrémité libre et sous l'appui à rouleaux, maximal sous la charge.
6. **Section dangereuse** : celle où Mf et Mt sont tous deux à leur maximum ; flexion–torsion.
7. **Moment idéal** : λ = 0,5, donc Mfi = √(Mf² + Mt²).
8. **Diamètre** : Mfi / (I/v) ≤ Re / s ; avec D = 1,5 × d, D_min = ∛(Mfi / (0,0788 × Rpe)) et d = D / 1,5.

::: retenir
Un arbre porteur d'une denture est **tordu** entre la denture et la sortie du couple, et **plié** par T entre ses appuis ; la section où les deux moments sont maximaux se dimensionne avec **Mfi = √(Mf² + Mt²)** (acier, λ = 0,5) et la condition **Mfi / (I/v) ≤ Re / s**.
:::

> 🏆 Du moteur au diamètre de l'arbre, la chaîne est bouclée : tu sais maintenant dire de quoi une pièce a besoin pour résister. La suite du thème rassemble ces outils en une vue d'ensemble.
