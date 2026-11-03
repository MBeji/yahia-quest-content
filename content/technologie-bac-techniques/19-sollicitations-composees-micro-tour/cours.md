# 🌀 Le micro-tour : quand la broche plie et se tord à la fois

> 💡 « Un arbre qui transmet la puissance d'une courroie à un outil n'est pas seulement tiré, il est aussi tordu. Pour savoir s'il tient, il faut mettre le pliage et la torsion dans le même calcul, et savoir le faire. »

Ce chapitre étudie la troisième activité du thème **Comportement des solides déformables** : le **micro-tour**, une petite machine-outil dont la **broche** reçoit sa rotation du moteur par un système **poulies-courroie** et la transmet à la pièce. La broche est guidée par deux **roulements à rouleaux coniques** ; à une extrémité, une poulie réceptrice la tire par la courroie, à l'autre, l'outil appuie sur la pièce pendant un **tronçonnage** (la coupe à longueur). Le manuel pose la question de l'activité : comment identifier les sollicitations de la broche, puis vérifier qu'elle résiste ? On y répond en **huit notions** : modéliser la broche en poutre, passer de la puissance du moteur au couple de la broche et à l'effort de l'outil, calculer les actions des appuis, trouver les moments de torsion et de flexion, lire les diagrammes et nommer la sollicitation, composer les deux moments, écrire la condition de résistance, enfin alléger la broche avec une section creuse.

Les notations sont celles du manuel : **Pm** la puissance du moteur, **η** le rendement du système poulies-courroie, **Nm** et **N11** les vitesses du moteur et de la broche en tr/min, **D20** et **D13** les diamètres de la poulie motrice et de la poulie réceptrice, **C11** le couple de la broche (11), **FT** l'effort tangentiel de l'outil sur la pièce, **F19/13** l'action de la courroie (19) sur la poulie réceptrice (13), **RA** et **RB** les actions des deux appuis, **Mt** le moment de torsion, **Mf** le moment fléchissant, **Mfi** le moment idéal de flexion, **Rpg** et **Rpe** les résistances pratiques au glissement et à l'extension, **λ** leur rapport. Les abscisses x sont en millimètres, mesurées depuis O, et les moments se calculent en N·mm avant d'être exprimés en N·m (1 N·m = 1 000 N·mm).

> 🗡️ Le manuel ne donne aucun corrigé, et ce chapitre n'enseigne donc que des règles standard de la mécanique. Ce qui est lu dans le manuel est dit comme tel (les données de la page 229 : Pm = 0,55 kW, η = 0,92, Nm = 750 tr/min, diamètres de poulies 24 et 48 mm, pièce de Ø 18 mm, Rpg = 5 daN/mm², F19/13 = 537 N, OA = 40, AB = 80 et BC = 60 mm, λ = 0,5, d/D = 0,8). Ce qui relève d'un **principe** général (P = C × ω, la contrainte de flexion, le moment quadratique d'une section circulaire) est annoncé « principe ». Deux éléments viennent de la **synthèse du thème** (p.251) et sont repris ici parce que la partie B ne se calcule pas sans eux : σmax = Mf / (IGz / v) et la condition σmax ≤ Rpe. Les schémas sont des **schémas de principe** redessinés, et chaque valeur choisie pour s'entraîner est appelée **illustration**. La **rigidité** de la broche (déformation, module E = 200 GPa) est citée par la question du manuel mais aucune question ne la calcule : elle reste hors de ce chapitre.

## 🧩 Du micro-tour à la poutre : points, appuis et actions

Pendant un tronçonnage, la broche tourne dans ses deux roulements, tirée à gauche par la courroie et poussée à droite par l'outil. Avant de calculer quoi que ce soit, on remplace la machine par un modèle assez simple pour qu'on puisse y écrire des équations.

Quelles actions agissent sur la broche, et à quels endroits ?

::: definition Le modèle de poutre de la broche
On remplace la broche (11) par une **poutre** horizontale suivant l'axe x, avec quatre points :

- **O**, où s'applique l'action **F19/13** de la courroie sur la poulie réceptrice, **verticale vers le bas** ;
- **A**, le premier roulement, modélisé par un appui **articulé** ;
- **B**, le second roulement, modélisé par un appui à **rouleaux** ;
- **C**, où s'applique l'effort **FT** de l'outil sur la pièce, **vertical vers le haut**.

Les cotes du manuel sont **OA = 40 mm, AB = 80 mm et BC = 60 mm**. Les hypothèses sont celles du manuel : liaisons parfaites, poids négligeables devant les actions mécaniques, broche assimilée à une poutre sur deux **appuis de niveau**, effort axial de l'outil négligé. Un appui à rouleaux ne retient pas la poutre suivant x : sa réaction est perpendiculaire à l'appui, donc verticale (principe). L'appui articulé pourrait porter aussi une composante suivant x ; elle est nulle ici, puisque aucune action n'est dirigée suivant l'axe.
:::

::: figure Le modèle de poutre de la broche. La flèche rouge est l'action de la courroie en O, la flèche verte l'effort de l'outil en C, les flèches grises les réactions des appuis, dessinées vers le haut par convention. Les cotes du haut sont les distances entre points voisins, les nombres dessous les abscisses depuis O
<svg viewBox="0 0 380 232"><title>Modèle de poutre de la broche : points O, A, B, C, cotes, appuis et actions</title><line x1="40" y1="30" x2="328.0" y2="30" stroke="#64748b" stroke-width="1.2"/><line x1="40" y1="25" x2="40" y2="35" stroke="#64748b" stroke-width="1.2"/><line x1="104.0" y1="25" x2="104.0" y2="35" stroke="#64748b" stroke-width="1.2"/><line x1="232.0" y1="25" x2="232.0" y2="35" stroke="#64748b" stroke-width="1.2"/><line x1="328.0" y1="25" x2="328.0" y2="35" stroke="#64748b" stroke-width="1.2"/><text x="72.0" y="22" font-size="11" font-weight="700" text-anchor="middle" fill="#64748b" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">40</text><text x="168.0" y="22" font-size="11" font-weight="700" text-anchor="middle" fill="#64748b" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">80</text><text x="280.0" y="22" font-size="11" font-weight="700" text-anchor="middle" fill="#64748b" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">60</text><rect x="40" y="96" width="288.0" height="10" fill="#bfdbfe" stroke="#0f172a" stroke-width="2"/><polygon points="104.0,106 92.0,126 116.0,126" fill="#fde68a" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><polygon points="232.0,106 220.0,124 244.0,124" fill="#fde68a" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><circle cx="232.0" cy="129" r="4.5" fill="#fde68a" stroke="#0f172a" stroke-width="1.8"/><line x1="40" y1="52" x2="40.0" y2="85.0" stroke="#dc2626" stroke-width="2.6"/><polygon points="40,94 35.5,85.0 44.5,85.0" fill="#dc2626"/><text x="48" y="60" font-size="12" font-weight="700" text-anchor="start" fill="#dc2626" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">F19/13</text><line x1="104.0" y1="192" x2="104.0" y2="149.0" stroke="#64748b" stroke-width="2.6"/><polygon points="104.0,140 108.5,149.0 99.5,149.0" fill="#64748b"/><text x="104.0" y="208" font-size="12" font-weight="700" text-anchor="middle" fill="#475569" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">RA</text><line x1="232.0" y1="192" x2="232.0" y2="151.0" stroke="#64748b" stroke-width="2.6"/><polygon points="232.0,142 236.5,151.0 227.5,151.0" fill="#64748b"/><text x="232.0" y="208" font-size="12" font-weight="700" text-anchor="middle" fill="#475569" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">RB</text><line x1="328.0" y1="192" x2="328.0" y2="117.0" stroke="#0f6e56" stroke-width="2.6"/><polygon points="328.0,108 332.5,117.0 323.5,117.0" fill="#0f6e56"/><text x="328.0" y="208" font-size="12" font-weight="700" text-anchor="middle" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">FT</text><text x="28" y="94" font-size="13" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">O</text><text x="104.0" y="92" font-size="13" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">A</text><text x="232.0" y="92" font-size="13" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">B</text><text x="328.0" y="92" font-size="13" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">C</text><text x="190" y="226" font-size="11" font-weight="600" text-anchor="middle" fill="#475569" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">RA et RB : sens supposé vers le haut, à vérifier par le calcul</text><text x="40" y="44" font-size="10" font-weight="600" text-anchor="middle" fill="#64748b" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x = 0</text><text x="104.0" y="44" font-size="10" font-weight="600" text-anchor="middle" fill="#64748b" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">40</text><text x="232.0" y="44" font-size="10" font-weight="600" text-anchor="middle" fill="#64748b" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">120</text><text x="328.0" y="44" font-size="10" font-weight="600" text-anchor="middle" fill="#64748b" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">180</text></svg>
:::

Les quatre lettres de la figure sont celles de la définition, et les trois distances 40, 80 et 60 mm s'additionnent en abscisses : x = 0 en O, 40 en A, 120 en B, 180 en C.

::: exemple Placer les points sur l'axe x
1. **Abscisse de A.** OA = 40 mm, donc xA = **40 mm** : on part de O, origine des abscisses.
2. **Abscisse de B.** On ajoute AB à l'abscisse de A : xB = 40 + 80 = **120 mm**, car les cotes se suivent bout à bout.
3. **Abscisse de C.** xC = 120 + 60 = **180 mm**, ce qui est aussi la longueur totale OC de la poutre : x varie de 0 à 180 mm.
4. **Bras de levier depuis A.** F19/13 est à 40 mm à **gauche** de A et FT à 180 − 40 = 140 mm à **droite** : une distance dépend toujours du point dont on part.

:::

::: piege Les cotes ne sont pas des abscisses
Le manuel donne BC = 60 mm, et l'on est tenté d'écrire xC = 60 mm, ou xB = 80 mm parce que AB = 80 mm. Ce sont des distances entre points voisins, non des positions depuis O. Les positions sont obtenues en **additionnant** : xB = 40 + 80 = 120 et xC = 120 + 60 = 180 mm. Une erreur ici fausse tous les bras de levier qui suivent.
:::

::: verifie
Sur une poutre d'illustration, OA = 30 mm, AB = 70 mm et BC = 50 mm. Quelles sont les abscisses de B et de C ?
---
On additionne les cotes depuis O : xB = 30 + 70 = **100 mm** et xC = 100 + 50 = **150 mm**. Les cotes données sont des distances entre points voisins, et non des abscisses.
:::

## ⚙️ De la puissance du moteur à l'effort de l'outil

Le moteur donne 0,55 kW, mais la broche ne reçoit pas tout, et elle ne tourne pas à la même vitesse que lui. Pour savoir ce que la courroie doit transmettre et ce que l'outil subit, il faut suivre la puissance du moteur jusqu'à la pièce.

Quel couple la broche transmet-elle, et quel effort l'outil exerce-t-il sur la pièce ?

::: definition Puissance, vitesse, couple et effort tangentiel
Le **rendement** η d'un système de transmission est le rapport de la puissance reçue à la puissance fournie. Des poulies reliées par une courroie sans glissement tournent à des vitesses **inversement proportionnelles** à leurs diamètres, D20 étant la poulie motrice et D13 la poulie réceptrice :

$$ P11 = η × Pm $$

$$ N11 = Nm × D20 / D13 $$

La puissance d'un arbre qui tourne est le produit du couple par la vitesse angulaire (principe), avec P en W, C en N·m, ω en rad/s et N en tr/min :

$$ P = C × ω, avec ω = 2π × N / 60 $$

L'**effort tangentiel** FT de l'outil sur la pièce a pour bras de levier le **rayon** de la pièce, D / 2 :

$$ C11 = FT × (D / 2) $$

:::

::: figure La chaîne de puissance du micro-tour avec les données de l'énoncé. Les trois inconnues sont celles de la broche : sa puissance, sa vitesse et son couple
<svg viewBox="0 0 400 152"><title>De la puissance du moteur à celle de la broche : trois blocs et leurs données</title><rect x="8" y="34" width="104" height="82" fill="#e2e8f0" stroke="#0f172a" stroke-width="2"/><text x="60" y="24" font-size="12" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Moteur (21)</text><text x="60" y="60" font-size="11" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Pm = 550 W</text><text x="60" y="78" font-size="11" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Nm = 750 tr/min</text><rect x="148" y="34" width="104" height="82" fill="#fde68a" stroke="#0f172a" stroke-width="2"/><text x="200" y="24" font-size="12" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Poulies-courroie</text><text x="200" y="60" font-size="10" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">D20 = 24 mm</text><text x="200" y="78" font-size="11" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">D13 = 48 mm</text><text x="200" y="96" font-size="11" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">η = 0,92</text><rect x="288" y="34" width="104" height="82" fill="#bbf7d0" stroke="#0f172a" stroke-width="2"/><text x="340" y="24" font-size="12" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Broche (11)</text><text x="340" y="60" font-size="11" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">P11 = ?</text><text x="340" y="78" font-size="11" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">N11 = ?</text><text x="340" y="96" font-size="11" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">C11 = ?</text><line x1="112" y1="75" x2="135.0" y2="75.0" stroke="#0f172a" stroke-width="2.6"/><polygon points="144,75 135.0,79.5 135.0,70.5" fill="#0f172a"/><line x1="252" y1="75" x2="275.0" y2="75.0" stroke="#0f172a" stroke-width="2.6"/><polygon points="284,75 275.0,79.5 275.0,70.5" fill="#0f172a"/><text x="200" y="140" font-size="11" font-weight="600" text-anchor="middle" fill="#475569" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">la puissance diminue (rendement), la vitesse diminue (rapport 24/48)</text></svg>
:::

::: figure Vue de face de la pièce pendant le tronçonnage : l'outil appuie en un point du bord, l'effort FT est tangent à la pièce, donc perpendiculaire au rayon D/2, et le couple C11 de la broche l'équilibre
<svg viewBox="0 0 280 190"><title>Tronçonnage : l'effort FT est tangent à la pièce, son bras de levier est le rayon D/2</title><circle cx="100" cy="96" r="62" fill="#e2e8f0" stroke="#0f172a" stroke-width="2"/><circle cx="100" cy="96" r="3" fill="#0f172a"/><line x1="100" y1="96" x2="162" y2="96" stroke="#0f172a" stroke-width="1.6" stroke-dasharray="4 3"/><text x="142" y="88" font-size="12" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">D/2</text><polygon points="162,96 184,87 184,105" fill="#fde68a" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="184" y="87" width="40" height="18" fill="#fde68a" stroke="#0f172a" stroke-width="2"/><text x="206" y="126" font-size="12" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">outil</text><line x1="162" y1="96" x2="162.0" y2="53.0" stroke="#0f6e56" stroke-width="2.6"/><polygon points="162,44 166.5,53.0 157.5,53.0" fill="#0f6e56"/><text x="170" y="52" font-size="13" font-weight="700" text-anchor="start" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">FT</text><path d="M70 96 A30 30 0 1 1 100 126" fill="none" stroke="#2563eb" stroke-width="2.4"/><polygon points="90,126 100,120 100,132" fill="#2563eb"/><text x="70" y="146" font-size="12" font-weight="700" text-anchor="middle" fill="#1d4ed8" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">C11</text><text x="96" y="28" font-size="12" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">pièce</text></svg>
:::

Les trois blocs de la première figure sont ceux de l'énoncé, avec leurs lettres P11, N11, C11, et le rayon pointillé de la seconde est le **D / 2** de la formule : FT est perpendiculaire à ce rayon, donc son bras de levier est le rayon entier.

::: exemple Du moteur à l'outil
1. **Puissance de la broche.** P11 = 0,92 × 550 = **506 W** : on convertit 0,55 kW en 550 W, et le rendement retire la part perdue dans la courroie.
2. **Vitesse de la broche.** N11 = 750 × 24 / 48 = **375 tr/min** : la poulie réceptrice est deux fois plus grande, donc elle tourne deux fois moins vite.
3. **Vitesse angulaire.** ω = 2π × 375 / 60 ≈ **39,27 rad/s** : on passe des tours par minute aux radians par seconde.
4. **Couple.** C11 = P11 / ω = 506 / 39,27 ≈ **12,89 N·m** : le couple est la puissance de la broche divisée par **sa** vitesse.
5. **Effort de l'outil.** La pièce a un diamètre de 18 mm, donc un rayon de 9 mm = 0,009 m. FT = C11 / 0,009 = 12,885 / 0,009 ≈ **1 432 N**.
6. **Contrôle.** C11 / 0,024 m (le rayon de la poulie réceptrice, 48 / 2) vaut 12,885 / 0,024 ≈ 537 N : l'écart avec les 537 N donnés par le manuel pour F19/13 est d'à peine 0,1 N. C'est un constat numérique, qui sert de contrôle pour C11.

:::

::: piege Le moteur n'est pas la broche
On calcule parfois C11 avec la vitesse du moteur : 506 / (2π × 750 / 60) ≈ 6,44 N·m, deux fois trop petit, parce que la broche tourne à 375 tr/min et non à 750. On oublie aussi le rendement : 550 / 39,27 ≈ 14,0 N·m. Une autre erreur est de diviser par le diamètre de la pièce (18 mm) au lieu de son rayon : FT sort à 716 N, deux fois trop petit. Le couple se calcule avec la puissance et la vitesse **du même arbre**, et l'effort avec un **rayon**.
:::

::: verifie
Un moteur de 0,5 kW entraîne par poulies-courroie (η = 0,9) une broche : poulie motrice de 30 mm, poulie réceptrice de 90 mm, moteur à 900 tr/min (valeurs d'illustration). Que valent P11, N11 et C11 ?
---
P11 = 0,9 × 500 = **450 W**. N11 = 900 × 30 / 90 = **300 tr/min**, donc ω = 2π × 300 / 60 ≈ 31,42 rad/s. C11 = 450 / 31,42 ≈ **14,32 N·m** : la puissance et la vitesse sont toutes deux celles de la broche.
:::

::: verifie
Avec C11 = 12 N·m et une pièce de Ø 30 mm (valeurs d'illustration), que vaut FT ?
---
Le rayon est 30 / 2 = 15 mm = 0,015 m, donc FT = 12 / 0,015 = **800 N**. Le bras de levier de FT est le rayon, et non le diamètre.
:::

## ⚖️ Les actions des appuis : une réaction peut être négative

La courroie tire la broche vers le bas en O, l'outil la pousse vers le haut en C, et les deux roulements doivent tenir le tout en place. On connaît deux forces, il en manque deux, RA et RB : il faut donc deux équations.

Comment les écrire pour qu'une seule inconnue reste dans chacune ?

::: methode Écrire l'équilibre de la poutre
La poutre est en équilibre : la **somme des forces** est nulle et la **somme des moments** est nulle. On prend l'axe y vers le haut. Le moment, **par rapport à un point P d'abscisse xP**, d'une force verticale Fy appliquée à l'abscisse xi vaut Fy × (xi − xP), positif dans le sens trigonométrique.

1. Écrire la somme des forces suivant y, égale à zéro.
2. Écrire la somme des moments **en A** : RA a un bras nul, il disparaît et il reste RB seule.
3. En déduire RB, puis RA avec l'équation des forces.
4. Contrôler en écrivant les moments en B.

:::

::: exemple Calculer RA et RB
1. **Forces suivant y**, avec F19/13 = 537 N vers le bas et FT = 1 432 N vers le haut : −537 + RA + RB + 1 432 = 0, donc RA + RB = **−895 N**.
2. **Moments en A**, chaque bras étant mesuré depuis A : (−537) × (0 − 40) + RB × (120 − 40) + 1 432 × (180 − 40) = 0, soit 21 480 + 80 RB + 200 480 = 0.
3. **Résolution.** 80 RB = −221 960, donc **RB = −2 774,5 N**. RA n'apparaît pas : son bras est nul.
4. **Réaction en A.** RA = −895 − (−2 774,5) = **+1 879,5 N**.
5. **Contrôle, moments en B.** (−537) × (0 − 120) + RA × (40 − 120) + 1 432 × (180 − 120) = 64 440 − 150 360 + 85 920 = 0 ✓.

:::

::: propriete Une réaction négative n'est pas une erreur
Le signe de RB indique que le sens supposé (vers le haut) était faux : la réaction en B est dirigée **vers le bas**, avec une intensité de 2 774,5 N. Ici, l'outil pousse l'extrémité C vers le haut au bout d'un bras de 140 mm depuis A, et la courroie tire O vers le bas de l'autre côté de A : les deux font basculer la broche dans le même sens autour de A, et le roulement B la retient en la tirant vers le bas. On ne recommence donc pas le calcul, on **garde le signe** dans la suite et l'on dit le sens dans la phrase de conclusion. Un contrôle est toujours possible : la somme des forces est nulle.
:::

::: piege Rendre positive une réaction négative
Quand RB sort négatif, on croit à une faute de calcul et l'on écrit RB = +2 774,5 N, « par bon sens », en pensant qu'un roulement ne peut que porter. L'équilibre est alors violé : −537 + 1 879,5 + 2 774,5 + 1 432 = 5 549 N, qui n'est pas nul. Le signe est une information : RB est dirigée vers le bas, et la somme des forces redevient nulle avec −2 774,5 N.
:::

::: verifie
Une poutre d'illustration est articulée en A (x = 40 mm) et sur rouleaux en B (x = 140 mm). Une seule charge de 300 N, vers le bas, agit en O (x = 0). Que valent RB et RA ?
---
Les moments en A : (−300) × (0 − 40) + RB × (140 − 40) = 0, soit 12 000 + 100 RB = 0, donc **RB = −120 N** (vers le bas). Les forces : −300 + RA + RB = 0, donc **RA = 300 + 120 = 420 N** (vers le haut). Comme dans le cours, la charge en porte-à-faux fait basculer la poutre autour de A, et B la retient.
:::

## ✂️ Les moments de torsion et de flexion, tronçon par tronçon

Maintenant que toutes les forces sont connues, on cherche ce qui sollicite la broche en chaque section. Deux effets s'y exercent : le couple qui la tord et les forces transversales qui la plient.

Comment varient ces deux moments entre O et C ?

::: definition Moment de torsion Mt et moment fléchissant Mf(x)
Le **moment de torsion** Mt est le couple que l'arbre transmet de la poulie à l'outil : tant qu'aucun couple n'est ajouté ni retiré entre deux sections, il y est le même. Le **moment fléchissant** en une section d'abscisse x est le moment, par rapport à cette section, des forces situées **à gauche** de la coupure :

$$ Mf(x) = Σ Fy × (x − xi) $$

où la somme porte sur les forces d'abscisse xi < x. Elle change de forme à chaque point d'application d'une force : il faut **découper** la poutre en tronçons. Le manuel en imprime trois : **0 ≤ x ≤ 40**, **40 ≤ x ≤ 120** et **120 ≤ x ≤ 180** mm. Seule la **valeur absolue** de Mf sert au dimensionnement ; le signe indique de quel côté la broche se courbe (principe). Ce signe suit la convention des moments internes, opposée à celle des moments de la section précédente : il n'a pas besoin d'être retenu.
:::

::: exemple Mt, puis Mf aux points O, A, B et C
1. **Moment de torsion.** Le couple C11 entre dans la broche par la poulie en O et sort par l'outil en C ; les roulements, supposés parfaits, n'en retirent pas. Donc Mt = C11 = **12,89 N·m** en toute section de O à C, soit 12 885 N·mm.
2. **Tronçon 1 (0 ≤ x ≤ 40).** Seule F19/13 est à gauche : Mf = −537 x. En O : **0**. En A : −537 × 40 = −21 480 N·mm = **−21,48 N·m**.
3. **Tronçon 2 (40 ≤ x ≤ 120).** RA s'ajoute : Mf = −537 x + 1 879,5 (x − 40). En B : −64 440 + 1 879,5 × 80 = −64 440 + 150 360 = 85 920 N·mm = **+85,92 N·m**.
4. **Tronçon 3 (120 ≤ x ≤ 180).** Il est plus court de regarder à **droite**, où seule FT agit : |Mf| = 1 432 × (180 − x). En B : 1 432 × 60 = 85 920 N·mm, ce qui **confirme** l'étape 3. En C : 1 432 × 0 = **0**, comme à toute extrémité libre. Le signe est positif, puisque Mf redescend de +85 920 à 0 sans changer de côté.
5. **Où Mf s'annule-t-il dans le tronçon 2 ?** −537 x + 1 879,5 (x − 40) = 0 donne 1 342,5 x = 75 180, soit x ≈ **56 mm** : Mf change de signe entre A et B.

:::

::: piege Oublier RB en regardant à gauche
Dans le tronçon 3, si l'on garde RA mais qu'on oublie RB, on trouve en C : −537 × 180 + 1 879,5 × 140 = 166 470 N·mm, un moment **non nul** à l'extrémité libre, ce qui est impossible. Avec RB = −2 774,5 N, on ajoute −2 774,5 × 60 = −166 470 et le total est bien **0**. Le moment en C doit s'annuler : c'est le contrôle qui dénonce l'oubli, et regarder à droite, où seule FT agit, l'évite.
:::

::: verifie
Sur la poutre d'illustration de la section précédente (A en x = 40, B en x = 140, charge de 300 N vers le bas en O, RA = 420 N, RB = −120 N), que vaut Mf en A, et que vaut-il en B ?
---
En A : Mf = −300 × 40 = **−12 000 N·mm = −12 N·m** (seule la charge est à gauche). En B : −300 × 140 + 420 × 100 = −42 000 + 42 000 = **0**, car B est ici l'extrémité de la poutre : le contrôle est bon.
:::

## 📈 Les diagrammes et la sollicitation de la broche

Quatre points, quatre valeurs de Mf et une valeur de Mt : pour voir d'un coup d'œil où la broche souffre, on les trace l'un sous l'autre.

Où est la section la plus sollicitée, et à quel type de sollicitation la broche est-elle soumise ?

::: definition Diagramme des moments et sollicitation composée
Un **diagramme** porte l'abscisse x à l'horizontale et le moment à la verticale, les points O, A, B, C étant alignés avec ceux de la poutre. Celui de Mt est un **plateau**, car Mt est constant. Celui de Mf est une **ligne brisée** qui relie les valeurs calculées aux points d'application : dans chaque tronçon, Mf est une fonction affine de x. On le lit en **valeur absolue**.

Une **sollicitation simple** est l'un de ces effets : traction ou compression suivant l'axe, **torsion** autour de l'axe, **flexion** (plier). Une section subit une **sollicitation composée** quand elle en subit **plusieurs à la fois**.
:::

::: figure Les diagrammes de Mt, en haut, et de Mf, en bas, sous les points O, A, B, C de la broche. Le plateau vert est le moment de torsion, constant. La ligne brisée orange passe par −21,48 N·m en A et +85,92 N·m en B, et coupe l'axe près de 56 mm. L'échelle verticale est la même pour les deux diagrammes
<svg viewBox="0 0 380 312"><title>Diagrammes de Mt et de Mf le long de la broche, de O à C</title><line x1="40" y1="22" x2="40" y2="300" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3 4"/><text x="40" y="16" font-size="13" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">O</text><line x1="104.0" y1="22" x2="104.0" y2="300" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3 4"/><text x="104.0" y="16" font-size="13" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">A</text><line x1="232.0" y1="22" x2="232.0" y2="300" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3 4"/><text x="232.0" y="16" font-size="13" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">B</text><line x1="328.0" y1="22" x2="328.0" y2="300" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3 4"/><text x="328.0" y="16" font-size="13" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">C</text><line x1="26" y1="100" x2="342.0" y2="100" stroke="#0f172a" stroke-width="1.2"/><polygon points="40,100 40,84.5 328.0,84.5 328.0,100" fill="#bbf7d0" stroke="#0f6e56" stroke-width="2.2"/><text x="184.0" y="78.538" font-size="11" font-weight="700" text-anchor="middle" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Mt = 12,89 N·m (constant)</text><text x="342.0" y="114" font-size="11" font-weight="600" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x</text><text x="346.0" y="94" font-size="11" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"></text><text x="34" y="38" font-size="12" font-weight="700" text-anchor="end" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Mt</text><line x1="26" y1="240" x2="342.0" y2="240" stroke="#0f172a" stroke-width="1.2"/><polygon points="40.0,240.0 104.0,265.8 232.0,136.9 328.0,240.0" fill="#fed7aa" stroke="#c2410c" stroke-width="2.4" stroke-linejoin="round"/><text x="104.0" y="279.776" font-size="11" font-weight="700" text-anchor="middle" fill="#9a3412" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−21,48</text><text x="232.0" y="130.89600000000002" font-size="11" font-weight="700" text-anchor="middle" fill="#9a3412" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">+85,92</text><text x="34" y="140" font-size="12" font-weight="700" text-anchor="end" fill="#c2410c" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Mf</text><text x="342.0" y="254" font-size="11" font-weight="600" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x</text><text x="190" y="306" font-size="11" font-weight="600" text-anchor="middle" fill="#475569" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Mf en N·m ; mêmes échelles verticales pour Mt et Mf</text></svg>
:::

Les points du diagramme de Mf sont les valeurs de l'exemple précédent, et le plateau est le Mt = 12,89 N·m de l'étape 1.

::: exemple Trouver la section la plus sollicitée et nommer la sollicitation
1. **Torsion.** Mt = 12,89 N·m en toute section : il ne départage pas les sections.
2. **Flexion.** Les valeurs absolues de Mf sont 0, 21,48, 85,92 et 0 N·m : la plus grande est 85,92 N·m, en **B**.
3. **Conclusion pour la section.** La section la plus sollicitée est celle de **B**, là où la flexion est maximale et où la torsion est aussi présente.
4. **Nommer la sollicitation.** En B, Mf ≠ 0 (forces perpendiculaires à l'axe) **et** Mt ≠ 0 (couple transmis), et aucun effort n'est dirigé suivant l'axe (l'effort axial de l'outil est négligé). La broche est soumise à de la **flexion-torsion**, une sollicitation composée.

:::

::: piege Une torsion petite reste une torsion
Mt = 12,89 N·m est près de sept fois plus petit que Mf = 85,92 N·m : on est tenté d'écrire « flexion simple » et d'oublier la torsion. Mais le nom d'une sollicitation dépend de **ce qui est présent**, pas de ce qui domine : la section est pliée et tordue, donc composée. Que l'on puisse ensuite négliger l'un des moments n'est pas une question de nom, c'est un calcul à faire (section suivante).
:::

::: verifie
Dans le tronçon AB d'une poutre d'illustration (80 mm de long), Mf passe de −10 N·m en A à +30 N·m en B. À quelle distance de A s'annule-t-il ?
---
Mf varie de façon **affine** dans le tronçon, donc proportionnellement à la distance. La variation totale est 30 − (−10) = 40 N·m sur 80 mm, soit 0,5 N·m par mm. Pour monter de −10 à 0, il faut 10 / 0,5 = **20 mm** à partir de A.
:::

## 🔀 Le moment idéal de flexion : un seul moment pour deux

En B, la broche est pliée (85,92 N·m) et tordue (12,89 N·m). Pour calculer un diamètre, il faudrait un seul nombre.

Comment réunir ces deux moments pour pouvoir calculer le diamètre ?

::: definition Le moment idéal de flexion Mfi
Le **moment idéal de flexion** Mfi est le moment de flexion qui, seul, produirait la même contrainte maximale que Mf et Mt ensemble (principe). La formule du manuel est :

$$ Mfi = (1 − 1/(2λ)) × Mf + (1/(2λ)) × √(Mf² + Mt²) $$

où λ = Rpg / Rpe est le rapport des résistances pratiques au glissement et à l'extension, qui dépend de la nature du matériau. Pour l'acier de la broche, le manuel donne **λ = 0,5**. Alors 1/(2λ) = 1 et 1 − 1/(2λ) = 0 : le premier terme disparaît et il reste

$$ Mfi = √(Mf² + Mt²) $$
:::

::: exemple Le moment idéal en B
1. **Valeur de λ.** λ = 0,5 donne 1/(2λ) = 1 : on utilise la forme simplifiée, Mfi = √(Mf² + Mt²).
2. **Les carrés**, en B : Mf² = 85,92² ≈ 7 382,2 et Mt² = 12,885² ≈ 166,0, en N²·m².
3. **La racine.** Mfi = √(7 382,2 + 166,0) = √7 548,2 ≈ **86,88 N·m**.
4. **Plausibilité.** Mfi est un peu plus grand que Mf (85,92) et bien plus petit que Mf + Mt (98,8) : 85,92 < 86,88 < 98,8. La torsion ne pèse ici qu'environ 1 % de plus.

:::

::: piege On n'additionne pas Mf et Mt
Pour « cumuler » les deux effets, on écrit Mf + Mt = 85,92 + 12,885 = 98,8 N·m. C'est trop grand de 14 % : les deux moments agissent suivant des directions perpendiculaires, et se composent comme les côtés de l'angle droit d'un triangle rectangle. On prend la racine de la somme des carrés, et Mfi = 86,88 N·m.
:::

::: propriete Deux cas limites de Mfi
Avec λ = 0,5 : si la torsion est nulle (Mt = 0), alors Mfi = √(Mf²) = |Mf| (la flexion simple) ; si la flexion est nulle (Mf = 0), alors Mfi = Mt. Entre les deux, Mfi est toujours supérieur ou égal au plus grand des deux moments. On calcule donc Mfi dans la section où |Mf| est maximal quand Mt est constant : ici B.
:::

::: verifie
En une section, Mf = 24 N·m et Mt = 10 N·m (valeurs d'illustration, λ = 0,5). Que vaut Mfi ?
---
Mfi = √(24² + 10²) = √(576 + 100) = √676 = **26 N·m**. On additionne les carrés, puis on prend la racine : 26 est inférieur à 24 + 10 = 34 et supérieur à chacun des deux moments.
:::

## 📏 La condition de résistance et le diamètre minimal

Tout ce calcul sert une question : quel est le plus petit diamètre pour lequel la broche ne cède pas ?

Comment passer d'un moment en N·m à un diamètre en mm ?

::: definition La condition de résistance
Pour une poutre fléchie, la contrainte normale maximale est donnée par la synthèse du thème (p.251) : σmax = Mf / (IGz / v). Pour l'arbre soumis à la flexion-torsion, on remplace Mf par le moment idéal Mfi. Dans une section circulaire **pleine** de diamètre d, le module IGz / v vaut π × d³ / 32 (principe). La broche résiste en toute sécurité si σ ne dépasse pas la **résistance pratique à l'extension** Rpe :

$$ σ = Mfi / (π × d³ / 32) ≤ Rpe $$

Le manuel donne Rpg = 5 daN/mm² et λ = Rpg / Rpe = 0,5, donc :

$$ Rpe = Rpg / λ = 5 / 0,5 = 10 daN/mm² = 100 N/mm² = 100 MPa $$

car 1 daN = 10 N. En résolvant pour d :

$$ d³ ≥ 32 × Mfi / (π × Rpe) $$

et d est la racine cubique du second membre. Les unités sont cohérentes en **N·mm et N/mm²** : d sort en mm.
:::

::: exemple Le diamètre minimal de la broche
1. **Moment idéal en N·mm.** Mfi = 86,88 N·m = 86 880 N·mm : on convertit avant de calculer, puisque Rpe est en N/mm².
2. **Cube du diamètre.** d³ ≥ 32 × 86 880 / (π × 100) = 2 780 160 / 314,16 ≈ 8 850 mm³.
3. **Racine cubique.** d ≥ 8 850^(1/3) ≈ **20,7 mm**. Le diamètre minimal est d'environ 20,7 mm.
4. **Vérifier un choix.** Avec d = 25 mm (valeur d'illustration), la contrainte réelle est 86 880 / (π × 25³ / 32) = 86 880 / 1 534 ≈ 56,6 N/mm², inférieure à Rpe = 100 N/mm² : 25 ≥ 20,7, la broche résiste.

:::

::: piege Les unités doivent s'accorder
Si l'on garde Rpg en daN/mm² sans convertir, Rpe = 10 « N/mm² » et le diamètre calculé monte à environ 44,6 mm, plus de deux fois trop grand. Si l'on garde Mfi en N·m avec Rpe en N/mm², d sort dix fois trop petit. L'autre erreur classique est de calculer avec Rpg à la place de Rpe : on trouve environ 26,1 mm, un diamètre trop grand et qui n'est pas celui que la condition de résistance donne.
:::

::: propriete d est un minimum
La condition donne un diamètre **minimal** : à d = 20,68 mm, σ égale exactement Rpe, sans marge de plus. Le constructeur choisit plus grand, en général une valeur normalisée au-dessus. Comme d intervient au cube, un petit gain de diamètre apporte une grande marge sur la contrainte. Inversement, d³ est proportionnel à Mfi : si tous les efforts sont multipliés par 1,5, le diamètre minimal n'est multiplié que par 1,5^(1/3) ≈ 1,145.
:::

::: verifie
Avec Mfi = 40 N·m et Rpe = 100 N/mm² (valeurs d'illustration), quel est le diamètre minimal d'une broche pleine ?
---
On convertit : Mfi = 40 000 N·mm. Alors d³ ≥ 32 × 40 000 / (π × 100) = 1 280 000 / 314,16 ≈ 4 074 mm³, donc d ≥ 4 074^(1/3) ≈ **15,97 mm**, soit environ 16 mm. Sans la conversion en N·mm, le résultat serait dix fois trop petit.
:::

## 🪶 La broche creuse : alléger sans perdre en résistance

Pour usiner des pièces longues et alléger la broche, le manuel propose de la percer : une section creuse dont le rapport des diamètres vaut d/D = 0,8.

Quels diamètres extérieur D et intérieur d faut-il alors, et que gagne-t-on ?

::: definition Section creuse et rapport k = d / D
Une section circulaire **creuse** a un diamètre extérieur **D** et un diamètre intérieur **d**, avec k = d / D. Son module de flexion vaut (principe) :

$$ IGz / v = π × D³ × (1 − k⁴) / 32 $$

La condition σ ≤ Rpe donne donc :

$$ D³ ≥ 32 × Mfi / (π × Rpe × (1 − k⁴)) $$

Avec k = 0,8 : k⁴ = 0,4096 et 1 − k⁴ = **0,5904**. Pour k = 0, on retrouve la section pleine.
:::

::: figure Une section pleine de diamètre d, à gauche, et une section creuse de diamètres D et d, à droite, avec d/D = 0,8. La matière de la section creuse est la couronne bleue
<svg viewBox="0 0 360 192"><title>Section circulaire pleine de diamètre d et section creuse de diamètres D et d</title><circle cx="95" cy="90" r="50" fill="#bfdbfe" stroke="#0f172a" stroke-width="2"/><line x1="45" y1="90" x2="145" y2="90" stroke="#0f172a" stroke-width="1.2"/><text x="95" y="84" font-size="13" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">d</text><text x="95" y="160" font-size="12" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">section pleine</text><circle cx="265" cy="90" r="50" fill="#bfdbfe" stroke="#0f172a" stroke-width="2"/><circle cx="265" cy="90" r="40" fill="#ffffff" stroke="#0f172a" stroke-width="2"/><line x1="225" y1="90" x2="305" y2="90" stroke="#0f172a" stroke-width="1.2"/><line x1="215" y1="30" x2="315" y2="30" stroke="#0f172a" stroke-width="1.2"/><line x1="215" y1="25" x2="215" y2="35" stroke="#0f172a" stroke-width="1.2"/><line x1="315" y1="25" x2="315" y2="35" stroke="#0f172a" stroke-width="1.2"/><text x="265" y="86" font-size="13" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">d</text><text x="265" y="24" font-size="13" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">D</text><text x="265" y="160" font-size="12" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">section creuse, d/D = 0,8</text><text x="190" y="184" font-size="10" font-weight="600" text-anchor="middle" fill="#475569" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">schéma de principe, hors échelle</text></svg>
:::

Le D de la formule est le diamètre extérieur de la couronne, et le d de la section creuse son diamètre intérieur : la lettre d désigne ici le **trou**, alors qu'elle désignait le diamètre de la broche pleine plus haut.

::: exemple Les diamètres de la broche creuse
1. **Même moment idéal.** Mfi = 86 880 N·mm et Rpe = 100 N/mm², comme pour la broche pleine.
2. **Cube de D.** D³ ≥ 2 780 160 / (π × 100 × 0,5904) = 8 850 / 0,5904 ≈ 14 990 mm³.
3. **Diamètre extérieur.** D ≥ 14 990^(1/3) ≈ **24,7 mm** : la broche creuse est un peu plus grosse que la pleine (20,7 mm).
4. **Diamètre intérieur.** d = 0,8 × 24,66 ≈ **19,7 mm**, le plus grand trou possible avec ce D.
5. **Gain de matière.** Aire pleine π × 20,68² / 4 ≈ 336 mm² ; aire creuse π × (24,66² − 19,72²) / 4 ≈ 172 mm² : la broche creuse contient environ **51 %** de la matière de la pleine, pour la même résistance.

:::

::: piege Le facteur est 1 − k⁴, pas 1 − k²
Il est tentant d'écrire 1 − k² = 1 − 0,64 = 0,36, parce que l'aire de la couronne contient D² − d². Mais la résistance à la flexion ne dépend pas de l'aire : elle dépend du moment quadratique, qui varie comme la **quatrième puissance** des diamètres. Avec 0,36, on trouve D ≈ 29,1 mm, donc une broche inutilement grosse. Le facteur de la formule est 1 − k⁴ = 0,5904.
:::

::: propriete Pourquoi creuser coûte peu en résistance
La matière près de l'axe travaille peu : la contrainte de flexion est nulle sur l'axe et maximale à la périphérie. Retirer le cœur enlève beaucoup de masse et peu de résistance à la flexion. C'est pourquoi, pour la même résistance, une section creuse de diamètre extérieur un peu plus grand que celui de la section pleine n'utilise qu'environ la moitié de la matière.
:::

::: verifie
Une broche pleine de d = 20 mm convient (valeurs d'illustration). On la remplace par un tube de même résistance avec d/D = 0,5. Que valent D et le diamètre intérieur ?
---
1 − k⁴ = 1 − 0,0625 = 0,9375. À résistance égale, D³ × 0,9375 = 20³ = 8 000, donc D³ ≈ 8 533 mm³ et D ≈ **20,4 mm**. Le diamètre intérieur est 0,5 × 20,4 ≈ **10,2 mm**. Le tube est à peine plus gros que la barre pleine.
:::

## 🧭 La méthode qui reste : sept marches

Devant une broche ou un arbre soumis à la flexion et à la torsion, reprends toujours cet ordre :

1. **Modéliser** : placer les points et les appuis (articulé, à rouleaux) sur l'axe x, avec les abscisses cumulées.
2. **De la puissance à l'effort** : P11 = η × Pm, N11 = Nm × D20 / D13, C11 = P11 / ω, puis FT = C11 / (D / 2).
3. **Trouver les actions des appuis** : forces suivant y, moments en A, contrôle en B ; garder le signe de chaque réaction.
4. **Calculer Mt et Mf** tronçon par tronçon, en regardant du côté qui a le moins de forces ; Mf est nul aux extrémités libres.
5. **Tracer, lire, nommer** : la section la plus sollicitée est celle de |Mf| maximal quand Mt est constant ; Mf ≠ 0 et Mt ≠ 0 donne la flexion-torsion.
6. **Composer** : Mfi = √(Mf² + Mt²) avec λ = 0,5, puis Rpe = Rpg / λ.
7. **Dimensionner** : d³ ≥ 32 × Mfi / (π × Rpe) pour une section pleine, D³ ≥ 32 × Mfi / (π × Rpe × (1 − k⁴)) pour une section creuse, en N·mm et N/mm².

::: retenir
La broche du micro-tour, tirée par la courroie et poussée par l'outil, subit de la **flexion-torsion** : **Mt** = C11 = 12,89 N·m est constant de O à C, **Mf** culmine en **B** (85,92 N·m), le **moment idéal** Mfi = √(Mf² + Mt²) = 86,88 N·m (λ = 0,5) donne le diamètre minimal **d ≈ 20,7 mm** par d³ ≥ 32 × Mfi / (π × Rpe) avec Rpe = Rpg / λ = 100 N/mm², et la section creuse d/D = 0,8 demande D ≈ 24,7 mm et d ≈ 19,7 mm, avec 1 − k⁴ au dénominateur.
:::

> 🏆 De la puissance du moteur au diamètre de la broche, tu as suivi chaque étape. Il ne reste qu'à mettre ces calculs à l'épreuve.
