# 🌀 Le banc d'essai de torsion : vriller une éprouvette pour mesurer ce qu'elle supporte

> 💡 « Un arbre qui transmet un couple ne fait pas que tourner : il se vrille, très peu. Mesurer ce vrillage sur une éprouvette, c'est apprendre à choisir le diamètre d'un arbre qui ne cède pas. »

Ce chapitre ouvre le thème **Comportement des solides déformables**, thème de l'AXE 2 « Analyse structurelle et conception », puis traite la première activité du thème : un **banc d'essai de torsion**. Le support est un banc didactique à deux montants reliés par deux colonnes : une **éprouvette** cylindrique est tenue à une extrémité et vrillée à l'autre par un levier chargé de masses, et un comparateur à cadran lit l'angle de rotation. Les notations de ce chapitre : **Mt** le moment de torsion, **α** l'angle relatif de torsion, **x** la longueur libre de l'éprouvette, **r** la longueur du levier, **F** la charge, **θ** l'angle unitaire de torsion, **G** le module d'élasticité transversale, **I₀** le moment quadratique polaire, **τ** la contrainte tangentielle. La lettre **r**, qui désignait un rapport de transmission aux chapitres précédents, désigne ici le levier ; le texte le rappelle quand il y a un risque de confusion.

> 🗡️ Le manuel ne donne **aucun corrigé** : ses tableaux de mesures sont vides, et la question finale n'a pas de réponse imprimée. Toutes les valeurs numériques de ce cours qui ne sont pas lues dans le manuel sont des **illustrations**, calculées avec la théorie puis arrondies comme une lecture de comparateur ; le texte le dit chaque fois. Les définitions et les formules de la torsion (angle unitaire, contrainte, conditions de résistance et de rigidité) viennent de la **synthèse du thème** (p.250), pas de l'activité elle-même : le texte l'indique. Les expressions de I₀ et de I₀/R pour une section circulaire pleine sont de la résistance des matériaux courante, qui n'est pas imprimée dans les pages de l'activité.

## 🧭 Le thème : quand un solide n'est plus indéformable

Un arbre de transmission reçoit un couple à une extrémité et le rend à l'autre. Dans les chapitres précédents, on le supposait **indéformable** : il tournait, c'est tout. En réalité, il se déforme un peu, et s'il est trop mince ou trop chargé, il finit par céder.

Comment savoir à l'avance si un diamètre suffit, et quelles grandeurs mesurer pour le savoir ?

::: definition Solide déformable et sollicitation
Un **solide déformable** est un solide dont la forme change, même très peu, sous les actions mécaniques qu'il reçoit. La manière dont ces actions le chargent s'appelle la **sollicitation** : torsion, flexion, ou plusieurs ensemble (**sollicitation composée**).
:::

La page d'ouverture du thème (p.216) annonce trois séquences et deux compétences, que la « carte du manuel » relie :

| Séquence | Compétence disciplinaire | Savoirs annoncés |
| --- | --- | --- |
| Torsion simple | CD 1.7 : retrouver les sollicitations que subit un solide | essai, contrainte, condition de résistance, condition de rigidité |
| Flexion plane simple | CD 2.1 : dimensionner un composant et vérifier sa résistance | essai, contraintes, efforts tranchants, moments fléchissants, condition de résistance |
| Sollicitations composées | CD 2.1 | condition de résistance |

Dans la carte, CD 1.7 est rattachée à la torsion et CD 2.1 à la flexion et aux sollicitations composées ; l'activité du banc de torsion, elle, affiche les deux compétences en tête de ses pages de travail. Ce chapitre traite la séquence **torsion simple** ; la flexion et les sollicitations composées sont l'objet des chapitres suivants.

::: exemple Placer une question dans la carte
Question : « Le diamètre de cet arbre, vrillé par un couple, suffit-il pour qu'il résiste ? »

1. **Trouver la compétence.** « Dimensionner » et « vérifier la résistance » sont les verbes de CD 2.1 : c'est un travail de dimensionnement.
2. **Trouver la sollicitation.** L'arbre est vrillé par un couple : c'est de la torsion, donc la séquence « torsion simple ».
3. **Lire le savoir attendu.** La carte annonce pour la torsion l'essai, la contrainte, la condition de résistance et la condition de rigidité : la réponse passera par la **condition de résistance**.

:::

::: piege La sollicitation n'est pas la déformation
On confond souvent la **cause** et l'**effet** : la sollicitation est l'ensemble des actions qui chargent la pièce (ici, un couple), la déformation est ce que la pièce en subit (ici, le vrillage). Dire « la torsion est la rotation de l'éprouvette » mélange les deux. La torsion est la manière dont on la charge ; la rotation de ses sections en est la conséquence, et c'est elle que le banc mesure.
:::

::: verifie
Une pièce est à la fois tirée et fléchie. Quelle séquence du thème la traite, et pourquoi ?
---
La séquence **sollicitations composées** : la pièce subit **plusieurs** sollicitations en même temps (traction et flexion), alors que la torsion simple et la flexion plane simple n'en traitent qu'une seule à la fois.
:::

## 🔩 Le banc : une éprouvette tenue d'un côté, vrillée de l'autre

Le manuel donne au banc trois buts : étudier le comportement d'éprouvettes cylindriques en **torsion pure** à partir de la courbe du moment de torsion en fonction de la rotation ; étudier les **contraintes** qui naissent dans l'éprouvette quand on la charge, et identifier la contrainte tangentielle ; déterminer le **module d'élasticité transversale G** d'un matériau. Il fournit trois éprouvettes de **8 mm** de diamètre et **600 mm** de longueur, en acier, en aluminium et en laiton, un support de charge de **2,5 N**, deux masses de **5 N**, une masse de **10 N**, un comparateur à cadran, un pied à coulisse au 1/50 et un réglet.

Que fait-on exactement subir à l'éprouvette, et quelles longueurs et quel angle faut-il relever ?

::: definition La torsion simple
Une poutre est sollicitée en **torsion** lorsque les actions mécaniques sur ses deux extrémités se réduisent à **deux couples égaux et opposés**, dont l'axe est la **ligne moyenne** de la poutre. La ligne moyenne est la ligne qui joint les centres des sections droites ; pour un cylindre, c'est son axe. Sur le banc, la portée fixe retient une extrémité et le levier chargé applique le couple à l'autre.
:::

::: figure Schéma de principe de l'essai. À gauche, vue de côté : l'éprouvette est encastrée dans la portée fixe (hachures) et sa longueur libre est x, jusqu'à la section où le levier est fixé (tirets rouges). À droite, vue du côté libre : le levier de longueur r tourne autour de l'axe de l'éprouvette et supporte la charge F, verticale vers le bas ; l'angle α est la rotation du levier depuis sa position de départ (tirets gris). Il est exagéré sur le dessin : sur le banc il reste petit
<svg viewBox="0 0 360 200"><rect x="12" y="62" width="14" height="76" fill="#e2e8f0" stroke="#0f172a" stroke-width="1.6"/><line x1="12" y1="76" x2="26" y2="68" stroke="#64748b" stroke-width="1.2" stroke-linecap="round"/><line x1="12" y1="87" x2="26" y2="79" stroke="#64748b" stroke-width="1.2" stroke-linecap="round"/><line x1="12" y1="98" x2="26" y2="90" stroke="#64748b" stroke-width="1.2" stroke-linecap="round"/><line x1="12" y1="109" x2="26" y2="101" stroke="#64748b" stroke-width="1.2" stroke-linecap="round"/><line x1="12" y1="120" x2="26" y2="112" stroke="#64748b" stroke-width="1.2" stroke-linecap="round"/><line x1="12" y1="131" x2="26" y2="123" stroke="#64748b" stroke-width="1.2" stroke-linecap="round"/><line x1="12" y1="142" x2="26" y2="134" stroke="#64748b" stroke-width="1.2" stroke-linecap="round"/><rect x="26" y="86" width="164" height="28" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.8"/><line x1="190" y1="72" x2="190" y2="128" stroke="#b91c1c" stroke-width="1.6" stroke-linecap="round" stroke-dasharray="4 3"/><line x1="26" y1="120" x2="26" y2="164" stroke="#64748b" stroke-width="1.1" stroke-linecap="round"/><line x1="190" y1="128" x2="190" y2="164" stroke="#64748b" stroke-width="1.1" stroke-linecap="round"/><line x1="76" y1="158" x2="32" y2="158" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><polygon points="26 158 33 160.8 33 155.2" fill="#0f172a" stroke="#0f172a" stroke-width="1" stroke-linejoin="round"/><line x1="140" y1="158" x2="184" y2="158" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><polygon points="190 158 183 155.2 183 160.8" fill="#0f172a" stroke="#0f172a" stroke-width="1" stroke-linejoin="round"/><line x1="75" y1="158" x2="141" y2="158" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><text x="108" y="152" font-size="13" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x</text><circle cx="262" cy="100" r="14" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.8"/><line x1="262" y1="100" x2="334" y2="100" stroke="#64748b" stroke-width="1.6" stroke-linecap="round" stroke-dasharray="5 4"/><line x1="262" y1="100" x2="330.5" y2="122.2" stroke="#0f6e56" stroke-width="3" stroke-linecap="round"/><circle cx="262" cy="100" r="2.6" fill="#0f172a"/><circle cx="330.5" cy="122.2" r="3.4" fill="#0f6e56" stroke="#0f172a" stroke-width="1"/><line x1="330.5" y1="125.2" x2="330.5" y2="166.2" stroke="#c2410c" stroke-width="2.4" stroke-linecap="round"/><polygon points="330.5 174.2 334.1 165.2 326.9 165.2" fill="#c2410c" stroke="#c2410c" stroke-width="1" stroke-linejoin="round"/><text x="342.5" y="160.2" font-size="13" font-weight="700" text-anchor="start" fill="#c2410c" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">F</text><path d="M312 100 A50 50 0 0 1 309.6 115.5" fill="none" stroke="#7c3aed" stroke-width="2"/><text x="323" y="116" font-size="13" font-weight="700" text-anchor="start" fill="#7c3aed" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">α</text><text x="296" y="128" font-size="13" font-weight="700" text-anchor="middle" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">r</text><text x="104" y="50" font-size="11" font-weight="400" text-anchor="middle" fill="#475569" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">vue de côté</text><text x="262" y="50" font-size="11" font-weight="400" text-anchor="middle" fill="#475569" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">vue du côté libre</text></svg>
:::

Les repères du schéma sont ceux de la suite : **x** pour la longueur tordue, **r** et **F** pour le levier et sa charge, **α** pour l'angle que lit le comparateur.

::: exemple Lire le schéma de principe
On cherche ce que chaque grandeur du schéma représente sur le banc.

1. **Ce qui est tenu.** L'extrémité de gauche est bloquée dans la portée fixe : sa section ne tourne pas. Sans cela, on ne pourrait pas mesurer une rotation **relative**.
2. **Ce qui est tordu.** Entre la portée fixe et le levier, l'éprouvette a une longueur libre **x**. Le manuel règle x = 600 mm pour sa première série de mesures, puis 500, 400, 300 et 200 mm pour la seconde.
3. **Ce qui tord.** La charge F pend au bout du levier, à la distance **r** de l'axe : une force dont la direction ne passe pas par l'axe fait tourner la pièce autour de lui.
4. **Ce qu'on lit.** L'angle **α** est la rotation de la section du levier par rapport à la section bloquée ; d'où son nom d'**angle relatif de torsion**. Le comparateur le donne : un tour d'aiguille vaut 1°, donc 3,5 tours lus font α = 3,5°.

:::

::: methode La démarche d'une série de mesures
Le manuel impose cet ordre, pour une éprouvette en acier d'abord :

1. **Régler les portées** de fixation à la longueur libre voulue, x = 600 mm au départ : c'est la longueur qui sera tordue.
2. **Placer l'éprouvette** à travers les éléments de fixation et la **bloquer** dans la portée fixe : ce côté ne tournera plus.
3. **Fixer l'autre extrémité** dans la mâchoire porte-éprouvette, qui porte le levier.
4. **Régler le comparateur** pour que sa pointe soit face à l'entaille du levier, puis **mettre l'aiguille à zéro** : le levier est alors en place, et le zéro se fait avant toute charge.
5. **Ajouter les charges** indiquées dans le tableau et **relever α** pour chacune.

Pour la seconde série, on reprend la même démarche avec l'éprouvette en aluminium, chargée une fois pour toutes de 12,5 N : seule la longueur x varie d'une mesure à l'autre.
:::

::: piege Une charge qui pend ne tire pas l'éprouvette
La charge F est un poids qui descend, et l'on est tenté de parler de traction. Or F est perpendiculaire à l'axe et loin de lui : elle **vrille** l'éprouvette sans l'allonger. Une traction serait deux forces alignées sur l'axe ; la torsion est deux couples d'axe confondu avec l'axe.
:::

::: verifie
On règle x = 400 mm au lieu de 600 mm, sans changer F ni le levier. Lesquelles des grandeurs x, r, F, α sont modifiées par le réglage, et lesquelles peuvent encore changer ensuite ?
---
Le réglage ne modifie directement que **x**. Les grandeurs **r** et **F** restent celles qu'on a choisies. L'angle **α** est la grandeur **mesurée** : il peut changer, puisque c'est lui qui répond à la nouvelle longueur libre.
:::

## ⚖️ Le moment de torsion : la charge fois le levier

Le support de charge pèse 2,5 N et les masses 5 N et 10 N. Accrochées au levier, elles tordent l'éprouvette d'autant plus que le levier est long et que la charge est lourde.

Comment résumer la charge et le bras de levier en une seule grandeur, et dans quelle unité ?

::: definition Le moment de torsion Mt
Pour une charge F appliquée à la distance r de l'axe, perpendiculairement à lui :

$$ Mt = F × r $$

F en newtons et r en millimètres donnent Mt en **N·mm**. L'angle α restant petit, le bras de levier reste très voisin de r pendant l'essai.
:::

::: exemple Remplir la première colonne du tableau (valeurs d'illustration)
Le manuel charge l'éprouvette avec F = 2,5 ; 5 ; 7,5 puis 10 N, et laisse le levier r à mesurer sur le banc. On prend ici, **pour s'entraîner**, r = 100 mm.

1. **Première charge.** Mt = 2,5 × 100 = 250 N·mm : la force est en N, la longueur en mm, donc le produit est en N·mm.
2. **Les suivantes.** 5 × 100 = 500 N·mm, 7,5 × 100 = 750 N·mm et 10 × 100 = 1 000 N·mm : r ne change pas, donc Mt est proportionnel à F.
3. **Composer la charge.** F = 12,5 N s'obtient avec le support et la masse de 10 N (2,5 + 10) : le support compte toujours dans la charge, puisqu'il est accroché. Avec le support toujours accroché, les masses listées donnent 2,5 ; 7,5 ; 12,5 ; 17,5 ou 22,5 N : les valeurs 5 N et 10 N du premier tableau du manuel ne s'obtiennent pas ainsi ; le manuel ne le commente pas, et l'on reprend ses valeurs telles quelles.

:::

::: piege Les mm et les m ne se mélangent pas
Avec F = 10 N et r = 100 mm, écrire Mt = 10 × 0,1 = 1 N·m est juste, mais écrire « 1 N·mm » est faux d'un facteur 1 000. On garde **une** unité de longueur dans tout le calcul : ici le millimètre, donc des N·mm, et 1 N·m = 1 000 N·mm.
:::

::: verifie
La charge est F = 12,5 N et le levier mesure r = 80 mm. Que vaut Mt en N·mm, puis en N·m ?
---
Mt = F × r = 12,5 × 80 = **1 000 N·mm**, soit **1 N·m** puisque 1 N·m = 1 000 N·mm. La force est en N et la longueur en mm : le produit sort en N·mm.
:::

## 📈 Mt en fonction de α : une droite

Le manuel demande de relever α pour chaque charge de l'éprouvette en acier, de tracer la courbe Mt = f(α), puis de conclure. On sait que plus Mt augmente, plus l'éprouvette se vrille.

La rotation croît-elle de façon régulière avec le moment, et que dit la forme de la courbe ?

::: exemple Tracer Mt = f(α) pour l'éprouvette en acier (valeurs d'illustration)
Le manuel donne x = 600 mm. Avec r = 100 mm, Mt vaut 250, 500, 750 et 1 000 N·mm. On prend, **pour s'entraîner**, les lectures suivantes (valeurs théoriques arrondies au centième de degré) :

| Mt (N·mm) | 250 | 500 | 750 | 1 000 |
| --- | --- | --- | --- | --- |
| α (°) | 0,27 | 0,53 | 0,80 | 1,07 |

1. **Placer les points.** Mt en ordonnée, α en abscisse, comme le demande le manuel : les quatre points sont presque alignés avec l'origine.
2. **Tester l'alignement.** On calcule le quotient Mt / α pour chaque point : 250 / 0,27 ≈ 926 ; 500 / 0,53 ≈ 943 ; 750 / 0,80 ≈ 938 ; 1 000 / 1,07 ≈ 935 N·mm/°. Les écarts viennent de l'arrondi des lectures.
3. **Conclure.** Le quotient est constant (≈ 935 N·mm/°) : les points sont sur une **droite passant par l'origine**, d'équation Mt = k × α avec k ≈ 935 N·mm/°.

:::

::: propriete Dans le domaine élastique, α est proportionnel à Mt
Tant que l'éprouvette retrouve sa forme quand on la décharge (**domaine élastique**), l'angle α est proportionnel au moment Mt : doubler Mt double α, et Mt = 0 donne α = 0. Le coefficient k dépend de la matière, du diamètre et de la longueur de l'éprouvette. Au-delà de la **limite élastique**, la droite se courbe et l'éprouvette garde une déformation : la proportionnalité ne vaut plus.
:::

::: figure Trois éprouvettes de même diamètre et de même longueur, tracées avec les valeurs théoriques de G du manuel (acier 80 GPa, laiton 37 GPa, aluminium 28 GPa). Pour un même moment Mt, l'acier tourne le moins : c'est la droite la plus raide, donc celle dont le coefficient k est le plus grand
<svg viewBox="0 0 340 230"><line x1="58" y1="190" x2="58" y2="24" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/><text x="58" y="205" font-size="10.5" font-weight="400" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><line x1="133.4" y1="190" x2="133.4" y2="24" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/><text x="133.4" y="205" font-size="10.5" font-weight="400" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><line x1="208.9" y1="190" x2="208.9" y2="24" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/><text x="208.9" y="205" font-size="10.5" font-weight="400" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><line x1="284.3" y1="190" x2="284.3" y2="24" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/><text x="284.3" y="205" font-size="10.5" font-weight="400" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">3</text><line x1="58" y1="190" x2="322" y2="190" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/><text x="52" y="194" font-size="10.5" font-weight="400" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><line x1="58" y1="152.3" x2="322" y2="152.3" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/><text x="52" y="156.3" font-size="10.5" font-weight="400" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">250</text><line x1="58" y1="114.5" x2="322" y2="114.5" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/><text x="52" y="118.5" font-size="10.5" font-weight="400" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">500</text><line x1="58" y1="76.8" x2="322" y2="76.8" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/><text x="52" y="80.8" font-size="10.5" font-weight="400" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">750</text><line x1="58" y1="39.1" x2="322" y2="39.1" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/><text x="52" y="43.1" font-size="10.5" font-weight="400" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1 000</text><line x1="58" y1="190" x2="321" y2="190" stroke="#0f172a" stroke-width="1.8" stroke-linecap="round"/><polygon points="328 190 320 186.8 320 193.2" fill="#0f172a" stroke="#0f172a" stroke-width="1" stroke-linejoin="round"/><line x1="58" y1="190" x2="58" y2="23" stroke="#0f172a" stroke-width="1.8" stroke-linecap="round"/><polygon points="58 16 54.8 24 61.2 24" fill="#0f172a" stroke="#0f172a" stroke-width="1" stroke-linejoin="round"/><line x1="58" y1="190" x2="138.6" y2="39.1" stroke="#0f6e56" stroke-width="2.6" stroke-linecap="round"/><line x1="58" y1="190" x2="232.3" y2="39.1" stroke="#b45309" stroke-width="2.6" stroke-linecap="round"/><line x1="58" y1="190" x2="288.3" y2="39.1" stroke="#1d4ed8" stroke-width="2.6" stroke-linecap="round"/><text x="318" y="184" font-size="12" font-weight="700" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">α (°)</text><text x="66" y="16" font-size="12" font-weight="700" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Mt (N·mm)</text><text x="146.6" y="35.1" font-size="12" font-weight="700" text-anchor="start" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">acier</text><text x="240.3" y="43.1" font-size="12" font-weight="700" text-anchor="start" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">laiton</text><text x="328.3" y="61.1" font-size="12" font-weight="700" text-anchor="end" fill="#1d4ed8" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">aluminium</text></svg>
:::

Le coefficient k est la pente de la droite sur ce graphique : la droite la plus raide est celle de la matière qui se vrille le moins.

::: piege Le zéro du comparateur
Si l'on oublie de remettre l'aiguille à zéro avant de charger, chaque lecture contient le même décalage. Avec un décalage de 0,3°, les lectures de l'exemple deviennent 0,57 ; 0,83 ; 1,10 et 1,37° : les quotients Mt / α valent alors 439, 602, 682 et 730 N·mm/°, qui ne sont plus constants, et la droite ne passe plus par l'origine. C'est pourquoi la démarche du manuel impose de régler le zéro **avant** d'ajouter les masses.
:::

::: verifie
Pour cette éprouvette, k ≈ 935 N·mm/°. Quel angle α produit Mt = 600 N·mm ?
---
Dans le domaine élastique Mt = k × α, donc α = Mt / k = 600 / 935 ≈ **0,64°**. On divise Mt par k parce que Mt = k × α, et le résultat est entre 0,53° (500 N·mm) et 0,80° (750 N·mm), comme il se doit.
:::

## 📏 Mt constant : l'angle dépend de la longueur

La seconde série du manuel charge une éprouvette en aluminium d'une charge fixe de 12,5 N et fait varier la longueur libre : 500, 400, 300 puis 200 mm.

Quand on raccourcit l'éprouvette, tourne-t-elle autant ? Et existe-t-il une grandeur qui ne dépend pas de la longueur choisie ?

::: exemple Tracer α = f(x) pour l'aluminium (valeurs d'illustration)
Avec F = 12,5 N et r = 100 mm, Mt = 1 250 N·mm. On prend, **pour s'entraîner**, ces lectures :

| x (mm) | 500 | 400 | 300 | 200 |
| --- | --- | --- | --- | --- |
| α (°) | 3,2 | 2,5 | 1,9 | 1,3 |

1. **Tester la proportionnalité.** On calcule α / x : 3,2 / 500 = 0,0064 ; 2,5 / 400 = 0,00625 ; 1,9 / 300 ≈ 0,00633 ; 1,3 / 200 = 0,0065 °/mm. Le quotient est constant, aux arrondis près.
2. **En déduire la forme.** Les points sont sur une droite passant par l'origine : α est proportionnel à x, à Mt constant.
3. **Donner la valeur commune.** Ce quotient est l'**angle de torsion par millimètre** de l'éprouvette, ≈ 0,0064 °/mm. En radians (× π / 180), il vaut ≈ 1,1 × 10⁻⁴ rad/mm.

:::

::: propriete L'angle unitaire de torsion θ
D'après la synthèse du thème, le quotient de l'angle de torsion par la longueur tordue est l'**angle unitaire de torsion** :

$$ θ = α / L $$

α est l'angle relatif de torsion **en radians**, L la longueur tordue (c'est x sur le banc), et θ s'exprime en **rad/mm**. Sur le banc, α se lit en degrés : le quotient α / x donne alors θ en °/mm, que l'on convertit (× π / 180) en rad/mm avant toute formule où figurent G ou τ. Pour un même Mt et une même éprouvette, θ est constant le long de l'éprouvette.
:::

::: figure Les quatre mesures de l'exemple (cercles) et la droite α = 0,0064 × x, qui passe par l'origine : une longueur double donne un angle double. Sa pente, 0,0064 °/mm, est l'angle unitaire de torsion
<svg viewBox="0 0 340 230"><line x1="58" y1="190" x2="58" y2="24" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/><text x="58" y="205" font-size="10.5" font-weight="400" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><line x1="102" y1="190" x2="102" y2="24" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/><text x="102" y="205" font-size="10.5" font-weight="400" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">100</text><line x1="146" y1="190" x2="146" y2="24" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/><text x="146" y="205" font-size="10.5" font-weight="400" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">200</text><line x1="190" y1="190" x2="190" y2="24" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/><text x="190" y="205" font-size="10.5" font-weight="400" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">300</text><line x1="234" y1="190" x2="234" y2="24" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/><text x="234" y="205" font-size="10.5" font-weight="400" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">400</text><line x1="278" y1="190" x2="278" y2="24" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/><text x="278" y="205" font-size="10.5" font-weight="400" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">500</text><line x1="322" y1="190" x2="322" y2="24" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/><text x="322" y="205" font-size="10.5" font-weight="400" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">600</text><line x1="58" y1="190" x2="322" y2="190" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/><text x="52" y="194" font-size="10.5" font-weight="400" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><line x1="58" y1="152.3" x2="322" y2="152.3" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/><text x="52" y="156.3" font-size="10.5" font-weight="400" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><line x1="58" y1="114.5" x2="322" y2="114.5" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/><text x="52" y="118.5" font-size="10.5" font-weight="400" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><line x1="58" y1="76.8" x2="322" y2="76.8" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/><text x="52" y="80.8" font-size="10.5" font-weight="400" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">3</text><line x1="58" y1="39.1" x2="322" y2="39.1" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/><text x="52" y="43.1" font-size="10.5" font-weight="400" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4</text><line x1="58" y1="190" x2="321" y2="190" stroke="#0f172a" stroke-width="1.8" stroke-linecap="round"/><polygon points="328 190 320 186.8 320 193.2" fill="#0f172a" stroke="#0f172a" stroke-width="1" stroke-linejoin="round"/><line x1="58" y1="190" x2="58" y2="23" stroke="#0f172a" stroke-width="1.8" stroke-linecap="round"/><polygon points="58 16 54.8 24 61.2 24" fill="#0f172a" stroke="#0f172a" stroke-width="1" stroke-linejoin="round"/><line x1="58" y1="190" x2="322" y2="45.1" stroke="#0f6e56" stroke-width="2.6" stroke-linecap="round"/><circle cx="278" cy="69.3" r="3.8" fill="#ffffff" stroke="#0f172a" stroke-width="1.8"/><circle cx="234" cy="95.7" r="3.8" fill="#ffffff" stroke="#0f172a" stroke-width="1.8"/><circle cx="190" cy="118.3" r="3.8" fill="#ffffff" stroke="#0f172a" stroke-width="1.8"/><circle cx="146" cy="141" r="3.8" fill="#ffffff" stroke="#0f172a" stroke-width="1.8"/><text x="318" y="184" font-size="12" font-weight="700" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x (mm)</text><text x="66" y="16" font-size="12" font-weight="700" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">α (°)</text></svg>
:::

Le coefficient directeur de la droite de ce graphique est le θ de la formule : on le lit, au lieu de le calculer point par point.

::: piege α change avec la longueur, θ non
Un élève qui compare l'éprouvette de 500 mm (α = 3,2°) à celle de 200 mm (α = 1,3°) et conclut que « la matière a changé » se trompe : c'est la **même** éprouvette, et θ vaut 0,0064 °/mm dans les deux cas. α est un total qui s'accumule sur la longueur ; θ est la part qui revient à chaque millimètre.
:::

::: verifie
Pour cette même éprouvette, θ = 1,1 × 10⁻⁴ rad/mm. Quel angle α, en degrés, obtient-on sur une longueur de 350 mm ?
---
α = θ × L = 1,1 × 10⁻⁴ × 350 = 0,0385 rad, soit 0,0385 × 180 / π ≈ **2,2°**. On multiplie par la longueur parce que θ est l'angle **par millimètre**, et on convertit les radians en degrés à la fin. Le résultat est entre 1,9° (300 mm) et 2,5° (400 mm).
:::

## 🔧 Le module G et le moment quadratique polaire

Dernière étape de l'activité : déterminer le module d'élasticité transversale G de l'éprouvette. Le manuel fixe X = 500 mm et charge l'éprouvette avec F = 7,5 ; 12,5 ; 17,5 puis 22,5 N, mesure r et d, calcule I₀, puis G pour chaque charge et la moyenne de ces G.

Que mesure G, et comment l'obtenir à partir de α, de Mt et de l'éprouvette ?

::: definition Le module G et le moment I₀
Le **module d'élasticité transversale G** (ou module de Coulomb) mesure la raideur d'une matière en torsion : plus G est grand, moins la matière se vrille. Il s'exprime en N/mm² (= MPa) ; les valeurs théoriques du manuel sont **acier 80 GPa, laiton 37 GPa, aluminium 28 GPa**, avec 1 GPa = 1 000 N/mm².

Le **moment quadratique polaire I₀** de la section décrit comment la matière est répartie autour de son centre. Pour une section circulaire pleine de diamètre d :

$$ I₀ = π × d⁴ / 32 $$

Il s'exprime en mm⁴. La synthèse du thème relie les trois grandeurs par θ = Mt / (G × I₀), ce qui donne, avec θ = α / L :

$$ G = Mt × L / (α × I₀) $$
:::

::: exemple Calculer G et sa moyenne (valeurs d'illustration)
Aluminium, d = 8 mm, X = 500 mm, r = 100 mm. On prend, **pour s'entraîner**, ces lectures de α :

1. **Calculer I₀.** I₀ = π × 8⁴ / 32 = π × 4 096 / 32 ≈ 402,1 mm⁴, une seule fois pour tout le tableau.
2. **Calculer Mt et convertir α.** Pour F = 7,5 N : Mt = 7,5 × 100 = 750 N·mm ; α = 1,9° = 1,9 × π / 180 ≈ 0,0332 rad, car la formule veut des radians.
3. **Appliquer la formule.** G = 750 × 500 / (0,0332 × 402,1) = 375 000 / 13,35 ≈ 28 100 N/mm² (28 122 sans arrondir α).
4. **Répéter et moyenner.** Les autres lignes donnent :

| F (N) | Mt (N·mm) | α (°) | G (N/mm²) |
| --- | --- | --- | --- |
| 7,5 | 750 | 1,9 | 28 122 |
| 12,5 | 1 250 | 3,2 | 27 829 |
| 17,5 | 1 750 | 4,5 | 27 705 |
| 22,5 | 2 250 | 5,7 | 28 122 |

5. **Comparer à la théorie.** G moyen = (28 122 + 27 829 + 27 705 + 28 122) / 4 ≈ 27 944 N/mm², soit 27,9 GPa. La valeur théorique de l'aluminium est 28 GPa : l'écart est d'environ 0,2 %, donc l'essai est cohérent.

:::

::: piege Les degrés ne vont pas dans la formule
Avec α = 1,9 **sans** convertir en radians, on obtient G = 375 000 / (1,9 × 402,1) ≈ 491 N/mm², soit 57 fois trop petit : c'est le facteur 180 / π ≈ 57,3 entre le degré et le radian. Un module de 0,5 GPa pour un métal doit alerter : on convertit α **avant** de calculer.
:::

::: verifie
Éprouvette en acier (G = 80 GPa), d = 8 mm, X = 500 mm, Mt = 1 000 N·mm. Quel angle α, en degrés, attend-on ?
---
G = 80 000 N/mm² et I₀ ≈ 402,1 mm⁴. On isole α dans G = Mt × L / (α × I₀) : α = Mt × L / (G × I₀) = 1 000 × 500 / (80 000 × 402,1) ≈ 0,01554 rad, soit 0,01554 × 180 / π ≈ **0,89°**. Le résultat est en radians tant qu'on n'a pas converti.
:::

## 🎯 La contrainte tangentielle : nulle au centre, maximale au bord

Le deuxième but du banc est d'identifier la **contrainte** qui naît dans l'éprouvette. Une éprouvette qui se vrille n'est pas sollicitée de la même façon partout : en son centre, la matière tourne à peine sur place, à la surface elle glisse davantage.

Où la matière est-elle le plus sollicitée, et comment le calculer ?

::: definition La contrainte tangentielle τ
En un point M de la section situé à la distance **ρ** du centre G, la **contrainte tangentielle** est, d'après la synthèse du thème :

$$ τ = (Mt / I₀) × ρ $$

Elle s'exprime en N/mm² (MPa). Elle est proportionnelle à ρ : nulle au centre, maximale au bord, là où ρ = R :

$$ τmax = Mt / (I₀ / R) $$

Pour une section circulaire pleine de diamètre d, I₀ / R = π × d³ / 16. La relation τ = G × θ × ρ en est une autre écriture, puisque θ = Mt / (G × I₀).
:::

::: figure Section circulaire vue de face. La flèche rouge est la contrainte tangentielle, perpendiculaire au rayon : elle vaut τmax au bord (ρ = R), la moitié à mi-rayon (point M) et zéro au centre G. La droite verte en tirets est la répartition linéaire de τ le long d'un diamètre
<svg viewBox="0 0 340 230"><circle cx="170" cy="112" r="72" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.8"/><line x1="170" y1="30" x2="170" y2="194" stroke="#64748b" stroke-width="1.4" stroke-linecap="round" stroke-dasharray="5 4"/><line x1="227.6" y1="40" x2="112.4" y2="184" stroke="#0f6e56" stroke-width="2" stroke-linecap="round" stroke-dasharray="4 3"/><line x1="170" y1="40" x2="220.6" y2="40" stroke="#c2410c" stroke-width="2.4" stroke-linecap="round"/><polygon points="227.6 40 219.6 36.8 219.6 43.2" fill="#c2410c" stroke="#c2410c" stroke-width="1" stroke-linejoin="round"/><line x1="170" y1="184" x2="119.4" y2="184" stroke="#c2410c" stroke-width="2.4" stroke-linecap="round"/><polygon points="112.4 184 120.4 187.2 120.4 180.8" fill="#c2410c" stroke="#c2410c" stroke-width="1" stroke-linejoin="round"/><line x1="170" y1="76" x2="191.8" y2="76" stroke="#c2410c" stroke-width="2.4" stroke-linecap="round"/><polygon points="198.8 76 190.8 72.8 190.8 79.2" fill="#c2410c" stroke="#c2410c" stroke-width="1" stroke-linejoin="round"/><line x1="170" y1="148" x2="148.2" y2="148" stroke="#c2410c" stroke-width="2.4" stroke-linecap="round"/><polygon points="141.2 148 149.2 151.2 149.2 144.8" fill="#c2410c" stroke="#c2410c" stroke-width="1" stroke-linejoin="round"/><circle cx="170" cy="112" r="3" fill="#0f172a"/><circle cx="170" cy="76.0" r="3.6" fill="#ffffff" stroke="#0f172a" stroke-width="1.6"/><text x="182" y="128" font-size="12" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">G</text><text x="159" y="70" font-size="12" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">M</text><text x="233.6" y="44" font-size="12" font-weight="700" text-anchor="start" fill="#c2410c" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">τmax</text><text x="204.8" y="80" font-size="12" font-weight="700" text-anchor="start" fill="#c2410c" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">τ</text><text x="106.4" y="188" font-size="12" font-weight="700" text-anchor="end" fill="#c2410c" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">τmax</text><line x1="170" y1="112" x2="236" y2="112" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><polygon points="242 112 235 109.2 235 114.8" fill="#0f172a" stroke="#0f172a" stroke-width="1" stroke-linejoin="round"/><text x="206" y="105" font-size="12" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">R</text><line x1="144" y1="76" x2="144" y2="112" stroke="#0f6e56" stroke-width="2.4" stroke-linecap="round"/><line x1="139" y1="76" x2="149" y2="76" stroke="#0f6e56" stroke-width="1.6" stroke-linecap="round"/><line x1="139" y1="112" x2="149" y2="112" stroke="#0f6e56" stroke-width="1.6" stroke-linecap="round"/><text x="134" y="98" font-size="12" font-weight="700" text-anchor="end" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">ρ</text><text x="170" y="222" font-size="11" font-weight="400" text-anchor="middle" fill="#475569" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">section droite vue de face</text></svg>
:::

Le segment ρ du dessin est la distance du point M au centre ; la longueur de chaque flèche est proportionnelle à ρ.

::: exemple Calculer τmax sur l'éprouvette d'aluminium (valeurs d'illustration)
d = 8 mm, F = 17,5 N, r = 100 mm.

1. **Moment.** Mt = 17,5 × 100 = 1 750 N·mm.
2. **Section.** R = d / 2 = 4 mm ; I₀ = π × 8⁴ / 32 ≈ 402,1 mm⁴ ; I₀ / R ≈ 100,5 mm³, qui est bien π × 8³ / 16.
3. **Contrainte maximale.** τmax = Mt / (I₀ / R) = 1 750 / 100,5 ≈ 17,4 N/mm², atteinte au bord.
4. **Contrainte à mi-rayon.** Pour ρ = 2 mm : τ = Mt × ρ / I₀ = 1 750 × 2 / 402,1 ≈ 8,7 N/mm², la moitié de τmax, puisque τ est proportionnelle à ρ.

:::

::: piege Le rayon, pas le diamètre
Pour calculer τmax, ρ prend sa valeur maximale **R = d / 2**, pas d. Avec ρ = 8 mm au lieu de 4 mm dans l'exemple, on obtiendrait 1 750 × 8 / 402,1 ≈ 34,8 N/mm², le double de la vraie valeur : un point à 8 mm du centre n'existe pas dans une éprouvette de 8 mm de diamètre.
:::

::: verifie
Même éprouvette (d = 8 mm), avec Mt = 1 000 N·mm. Que vaut τmax ?
---
τmax = Mt / (I₀ / R) = 1 000 / 100,5 ≈ **9,95 N/mm²**. On divise par I₀ / R, soit 100,5 mm³ pour d = 8 mm, parce que τ est maximale au rayon R = 4 mm et non au diamètre. Le résultat est inférieur à celui de l'exemple (17,4), car Mt est plus petit.
:::

## 🛡️ Résister et ne pas trop se vriller : dimensionner un arbre

La dernière question de l'activité demande le diamètre d'une poutre en aluminium qui résiste en toute sécurité, avec Mt = 1 608 N·mm, une limite élastique au cisaillement Reg = 48 N/mm² et un coefficient de sécurité s = 3. Le manuel n'imprime pas la réponse : tu la trouveras en exercice.

Comment passer de la contrainte maximale à un diamètre, et que veut dire « en toute sécurité » ?

::: definition Les deux conditions
La **condition de résistance** compare la contrainte maximale à une limite **réduite** par le coefficient de sécurité s :

$$ τmax ≤ Rpg avec Rpg = Reg / s $$

Reg est la limite élastique au cisaillement de la matière et Rpg la **résistance pratique au glissement**. Pour une section circulaire pleine, τmax = 16 × Mt / (π × d³), et elle donne un diamètre minimal :

$$ d³ ≥ 16 × Mt / (π × Rpg) $$

La **condition de rigidité** limite la torsion, et non plus la contrainte : θ ≤ θlimite, où θlimite est fixé par l'expérience. Avec θ = Mt / (G × I₀), elle donne :

$$ d⁴ ≥ 32 × Mt / (π × G × θlimite) $$
:::

::: exemple Dimensionner un arbre en aluminium (valeurs d'illustration)
Mt = 5 000 N·mm, Reg = 60 N/mm², s = 3, G = 28 000 N/mm² et θlimite = 1,0 × 10⁻⁴ rad/mm. Ces valeurs sont choisies **pour s'entraîner**, pour ne pas donner la réponse du manuel.

1. **Rpg.** Rpg = Reg / s = 60 / 3 = 20 N/mm² : on garde de la marge par rapport à la limite d'élasticité.
2. **Diamètre de résistance.** d³ ≥ 16 × 5 000 / (π × 20) ≈ 1 273 mm³, d'où d ≥ 10,84 mm. On arrondit **par excès**, à 11 mm : un diamètre plus petit ferait dépasser Rpg.
3. **Vérifier la rigidité avec d = 11 mm.** I₀ = π × 11⁴ / 32 ≈ 1 437 mm⁴ et θ = 5 000 / (28 000 × 1 437) ≈ 1,24 × 10⁻⁴ rad/mm, supérieur à θlimite : 11 mm ne suffit pas.
4. **Diamètre de rigidité.** d⁴ ≥ 32 × 5 000 / (π × 28 000 × 1,0 × 10⁻⁴) ≈ 18 190 mm⁴, d'où d ≥ 11,6 mm : on prend **12 mm**.
5. **Contrôler le choix.** Pour d = 12 mm, τmax = 16 × 5 000 / (π × 12³) ≈ 14,7 N/mm² ≤ 20 et θ ≈ 8,8 × 10⁻⁵ rad/mm ≤ 1,0 × 10⁻⁴ : les deux conditions sont tenues.

:::

::: piege Reg n'est pas Rpg
Comparer τmax à Reg au lieu de Rpg oublie le coefficient de sécurité. Dans l'exemple, un diamètre de 8 mm donne τmax = 16 × 5 000 / (π × 8³) ≈ 49,7 N/mm² : c'est moins que Reg = 60, et l'on croirait qu'il convient, alors qu'il dépasse de loin Rpg = 20. La condition porte sur Rpg, toujours.
:::

::: verifie
Mt = 2 000 N·mm, Reg = 36 N/mm² et s = 2. Quel est le plus petit diamètre entier, en mm, qui vérifie la condition de résistance ?
---
Rpg = 36 / 2 = 18 N/mm² ; d³ ≥ 16 × 2 000 / (π × 18) ≈ 566 mm³, donc d ≥ 8,27 mm : on arrondit par excès à **9 mm**. Pour d = 8, τmax = 32 000 / (π × 512) ≈ 19,9 N/mm² dépasserait 18, alors que pour d = 9, τmax ≈ 14,0 N/mm² reste sous 18.
:::

## 🧭 La méthode qui reste : six marches

Devant un essai ou un arbre à dimensionner en torsion, tu reprends toujours cet ordre :

1. **Charger** : calculer Mt = F × r avec une seule unité de longueur ; F peut venir du support et des masses.
2. **Décrire la section** : d, R = d / 2, I₀ = π × d⁴ / 32 et I₀ / R = π × d³ / 16.
3. **Mesurer** : régler le zéro, relever α pour chaque x, vérifier que Mt / α et α / x restent constants, puis θ = α / L en radians.
4. **Identifier la matière** : G = Mt × L / (α × I₀) avec α en radians, puis comparer à la valeur théorique du manuel.
5. **Calculer la contrainte** : τ = Mt × ρ / I₀, maximale au bord, τmax = Mt / (I₀ / R).
6. **Conclure** : Rpg = Reg / s et τmax ≤ Rpg pour résister ; θ ≤ θlimite pour ne pas trop se vriller ; le diamètre retenu, arrondi par excès, vérifie les deux.

::: retenir
La **torsion simple** est due à deux couples égaux et opposés d'axe confondu avec la ligne moyenne ; sur le banc, **Mt = F × r** et, dans le domaine élastique, **α est proportionnel à Mt et à la longueur**, ce qui donne l'**angle unitaire θ = α / L** et le module **G = Mt × L / (α × I₀)** avec α en radians ; la contrainte **τ = Mt × ρ / I₀** est **nulle au centre et maximale au bord**, et l'arbre est bien dimensionné si **τmax ≤ Rpg = Reg / s** et **θ ≤ θlimite**.
:::

> 🏆 Le banc de torsion n'a plus de secret : tu sais charger une éprouvette, lire sa rotation, en tirer G, calculer la contrainte et choisir un diamètre qui résiste. La flexion plane simple t'attend au chapitre suivant.
