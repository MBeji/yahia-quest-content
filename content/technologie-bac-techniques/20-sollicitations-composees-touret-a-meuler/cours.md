# 🔩 Le touret à meuler : quand l'arbre fléchit et se tord

> 💡 « La meule pousse sur l'arbre, la courroie le tire, le poids l'incline : il ne subit pas une seule épreuve, mais deux à la fois. Pour trouver son diamètre, on ne les additionne pas comme on croit. »

Ce chapitre étudie la quatrième activité du thème **Comportement des solides déformables** : le **touret à meuler**, une machine qui enlève de la matière par **abrasion** (ébavurage, affûtage). Un **arbre**, entraîné en rotation par **poulies-courroie** et guidé par deux **roulements à billes**, porte à une extrémité la **meule**, qui est l'outil, et à l'autre la **poulie**. Le manuel pose la question du chapitre : comment dimensionner et vérifier la résistance d'un composant soumis à une **sollicitation composée** ? Ici, on cherche le **diamètre minimal** de l'arbre plein.

Le chapitre suit la démarche du manuel en sept notions : modéliser l'arbre en poutre, équilibrer la rotation autour de l'axe, calculer les réactions des paliers, trouver le moment fléchissant, lire les diagrammes, composer flexion et torsion, puis écrire la condition de résistance. La synthèse du thème n'est pas ici : elle est portée par le chapitre 22. Les notations sont celles du manuel : **FT** l'effort tangentiel sur la meule, **T** et **t** les brins de la courroie, **P** le poids, **RA** et **RC** les réactions des paliers, **Mt** le moment de torsion, **Mf** le moment fléchissant, **rm** et **rp** les rayons de la meule et de la poulie. Les abscisses x sont en millimètres, et les moments se calculent en N·mm avant d'être convertis en N·m (1 N·m = 1 000 N·mm).

> 🗡️ Les schémas de ce cours sont des **schémas de principe**, redessinés pour expliquer : le dessin d'ensemble du manuel (p.234) n'est pas reproduit, et le manuel ne donne aucun corrigé. Quand une valeur est lue dans le manuel (FT = 110 N, P = 30 N, les cotes, r = 75 mm et 22 mm, T ≈ 4 t, λ = 0,5, S275, s = 2), le texte le dit ; quand elle est choisie pour s'entraîner, il parle de valeur d'**illustration** ; quand un point relève d'un **principe** de mécanique plutôt que du manuel, il le dit aussi. Les résultats sont recalculés ici et refaits dans les exercices.

## 🧩 Du touret à la poutre : points, appuis et actions

La meule ébavure une pièce ; l'arbre qui la porte repose sur deux roulements et il est chargé à ses deux bouts. Avant de calculer quoi que ce soit, il faut remplacer la machine par un modèle assez simple pour qu'on puisse y écrire des équations.

Quelles forces agissent sur l'arbre, et à quels endroits ?

::: definition Le modèle de poutre du touret
On remplace l'ensemble {arbre (1) + poulie (2) + meule (3)} par une **poutre** tracée suivant l'axe x, avec cinq points repérés :

- **O**, le plan de la meule ;
- **A**, le palier de gauche, modélisé par un appui **articulé** ;
- **G**, le point d'application du poids, au **milieu d'OB** ;
- **C**, le palier de droite, modélisé par un appui à **rouleaux** ;
- **B**, le plan de la poulie.

Les liaisons sont supposées **parfaites** (sans frottement). Les cotes du manuel sont OA = 100 mm, AC = 240 mm et AB = 330 mm. Les actions extérieures sont : **FT = 110 N** en O, **P = 30 N** en G, **T + t** en B, et les deux réactions inconnues **RA** et **RC**. Un appui à rouleaux ne retient pas la poutre suivant x : sa réaction est perpendiculaire à l'appui, donc verticale (principe).
:::

::: figure Le modèle de poutre du touret. Les points O, A, G, C, B sont alignés sur l'axe x. La flèche verte est l'effort FT de la pièce, les flèches rouges sont le poids P et les actions T + t de la courroie, les flèches grises sont les réactions inconnues RA et RC, dessinées vers le haut par convention. La valeur T + t = 625 N se calcule à la section suivante
<svg viewBox="0 0 340 190"><title>Modèle de poutre du touret : points O, A, G, C, B, cotes et actions extérieures</title><line x1="20" y1="20" x2="20" y2="110" stroke="#64748b" stroke-width="1" stroke-dasharray="2 3"/><line x1="90" y1="20" x2="90" y2="110" stroke="#64748b" stroke-width="1" stroke-dasharray="2 3"/><line x1="170.5" y1="20" x2="170.5" y2="110" stroke="#64748b" stroke-width="1" stroke-dasharray="2 3"/><line x1="258" y1="20" x2="258" y2="110" stroke="#64748b" stroke-width="1" stroke-dasharray="2 3"/><line x1="321" y1="20" x2="321" y2="110" stroke="#64748b" stroke-width="1" stroke-dasharray="2 3"/><g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="20" y="14" text-anchor="middle" fill="#0f172a" font-size="13">O</text><text x="90" y="14" text-anchor="middle" fill="#0f172a" font-size="13">A</text><text x="170.5" y="14" text-anchor="middle" fill="#0f172a" font-size="13">G</text><text x="258" y="14" text-anchor="middle" fill="#0f172a" font-size="13">C</text><text x="321" y="14" text-anchor="middle" fill="#0f172a" font-size="13">B</text></g><line x1="20" y1="36" x2="90" y2="36" stroke="#0f172a" stroke-width="1.2"/><polygon points="90,36 84,39 84,33" fill="#0f172a"/><line x1="90" y1="36" x2="20" y2="36" stroke="#0f172a" stroke-width="1.2"/><polygon points="20,36 26,33 26,39" fill="#0f172a"/><text x="55" y="31" text-anchor="middle" fill="#0f172a" font-size="10" font-weight="600" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">100</text><line x1="90" y1="36" x2="258" y2="36" stroke="#0f172a" stroke-width="1.2"/><polygon points="258,36 252,39 252,33" fill="#0f172a"/><line x1="258" y1="36" x2="90" y2="36" stroke="#0f172a" stroke-width="1.2"/><polygon points="90,36 96,33 96,39" fill="#0f172a"/><text x="174" y="31" text-anchor="middle" fill="#0f172a" font-size="10" font-weight="600" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">240</text><line x1="258" y1="36" x2="321" y2="36" stroke="#0f172a" stroke-width="1.2"/><polygon points="321,36 315,39 315,33" fill="#0f172a"/><line x1="321" y1="36" x2="258" y2="36" stroke="#0f172a" stroke-width="1.2"/><polygon points="258,36 264,33 264,39" fill="#0f172a"/><text x="289.5" y="31" text-anchor="middle" fill="#0f172a" font-size="10" font-weight="600" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">90</text><rect x="20" y="107" width="301" height="6" fill="#cbd5e1" stroke="#0f172a" stroke-width="1.6"/><polygon points="90,113 81,130 99,130" fill="#fde68a" stroke="#0f172a" stroke-width="1.4"/><line x1="76" y1="130" x2="104" y2="130" stroke="#0f172a" stroke-width="1.4"/><path d="M78 130 L73 135 M84 130 L79 135 M90 130 L85 135 M96 130 L91 135 M102 130 L97 135" stroke="#64748b" stroke-width="1"/><polygon points="258,113 249,127 267,127" fill="#fde68a" stroke="#0f172a" stroke-width="1.4"/><circle cx="253" cy="130" r="3" fill="#ffffff" stroke="#0f172a" stroke-width="1.2"/><circle cx="263" cy="130" r="3" fill="#ffffff" stroke="#0f172a" stroke-width="1.2"/><line x1="244" y1="133" x2="272" y2="133" stroke="#0f172a" stroke-width="1.4"/><path d="M246 133 L241 138 M252 133 L247 138 M258 133 L253 138 M264 133 L259 138 M270 133 L265 138" stroke="#64748b" stroke-width="1"/><line x1="20" y1="107" x2="20" y2="66" stroke="#0f6e56" stroke-width="2.5"/><polygon points="20,66 24.5,75 15.5,75" fill="#0f6e56"/><line x1="90" y1="107" x2="90" y2="70" stroke="#64748b" stroke-width="2.2"/><polygon points="90,70 94.5,79 85.5,79" fill="#64748b"/><line x1="258" y1="107" x2="258" y2="70" stroke="#64748b" stroke-width="2.2"/><polygon points="258,70 262.5,79 253.5,79" fill="#64748b"/><line x1="170.5" y1="113" x2="170.5" y2="150" stroke="#ef4444" stroke-width="2.5"/><polygon points="170.5,150 166,141 175,141" fill="#ef4444"/><line x1="321" y1="113" x2="321" y2="165" stroke="#ef4444" stroke-width="2.5"/><polygon points="321,165 316.5,156 325.5,156" fill="#ef4444"/><g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="6" y="58" text-anchor="start" fill="#0f6e56" font-size="11">FT = 110 N</text><text x="90" y="64" text-anchor="middle" fill="#64748b" font-size="11">RA</text><text x="258" y="64" text-anchor="middle" fill="#64748b" font-size="11">RC</text><text x="170.5" y="163" text-anchor="middle" fill="#ef4444" font-size="11">P = 30 N</text><text x="313" y="178" text-anchor="end" fill="#ef4444" font-size="11">T + t = 625 N</text></g></svg>
:::

Sur la figure, chaque flèche est une action de la liste, et chaque point porte la lettre du manuel : FT est la flèche verte en O, P la flèche rouge en G, T + t la flèche rouge en B. Les nombres 100, 240 et 90 sont les distances entre points voisins.

::: exemple Placer les points et mesurer les distances

1. **Longueur de la poutre.** OB = OA + AC + CB = 100 + 240 + 90 = 430 mm : les trois cotes se suivent bout à bout.
2. **Contrôle avec le manuel.** AB = AC + CB = 240 + 90 = 330 mm, c'est bien la valeur donnée : les cotes sont cohérentes.
3. **Position du poids.** G est au milieu d'OB, donc OG = 430 / 2 = 215 mm, mesurés depuis O.
4. **Bras depuis A.** G est à 215 − 100 = 115 mm à droite de A, et à gauche de C puisque 215 < 340. Une distance dépend toujours du point dont on part.

:::

::: piege G n'est pas le milieu des deux paliers
On est tenté de placer le poids au milieu de AC, soit à 100 + 120 = 220 mm de O, parce que ce sont les paliers qui portent. L'énoncé dit pourtant que P est appliqué au **milieu d'OB**, meule et poulie comprises : 215 mm. L'écart de 5 mm paraît petit, mais il change tous les bras de levier qui suivent. On lit donc d'abord de quel segment G est le milieu.
:::

::: verifie
À quelle distance de C le poids est-il appliqué, et de quel côté de C ?
---

G est à 215 mm de O et C à 340 mm de O : la distance est 340 − 215 = **125 mm**. Comme 215 < 340, G est à **gauche** de C, entre A et C.
:::

## 🌀 La torsion : ce que la courroie reprend à la meule

La pièce à ébavurer freine la meule avec un effort tangentiel FT = 110 N, appliqué en D sur le bord de la meule, à 75 mm de l'axe. Pour que la meule tourne à vitesse constante, la courroie doit exactement compenser ce freinage par l'intermédiaire de la poulie.

Quel couple l'arbre transmet-il, et que valent les deux brins T et t de la courroie ?

::: definition Moment de torsion et équilibre de rotation
Le **moment** d'une force par rapport à l'axe de l'arbre est le produit de la force par son **bras de levier**, la distance entre l'axe et la droite d'action. Pour une force tangente à un cercle, le bras est le rayon. Le **moment de torsion** Mt est le couple que l'arbre transmet de la meule à la poulie :

$$ Mt = FT × rm $$

À vitesse constante, l'ensemble est en **équilibre de rotation** autour de l'axe x : le moment de FT est exactement compensé par celui des brins de la courroie, tangents à la poulie de rayon rp = 22 mm :

$$ FT × rm = (T − t) × rp $$

Le manuel donne rm = OD = 75 mm et la relation T ≈ 4 t.
:::

::: figure Meule et poulie vues de face, l'axe x pointant vers l'observateur. À gauche, FT tire en D sur le cercle de rayon rm. À droite, les brins T et t tirent sur le cercle de rayon rp, T étant le brin le plus tendu, donc le plus long. Les deux flèches de la poulie sont dirigées vers le bas
<svg viewBox="0 0 340 180"><title>Meule et poulie vues de face : l'effort FT sur la meule, les brins T et t sur la poulie</title><circle cx="85" cy="96" r="48" fill="#fde68a" stroke="#0f172a" stroke-width="1.8"/><circle cx="85" cy="96" r="3" fill="#0f172a" stroke="#0f172a" stroke-width="1"/><circle cx="255" cy="96" r="14" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.8"/><circle cx="255" cy="96" r="3" fill="#0f172a" stroke="#0f172a" stroke-width="1"/><line x1="85" y1="96" x2="133" y2="96" stroke="#0f172a" stroke-width="1.2" stroke-dasharray="4 3"/><line x1="255" y1="96" x2="269" y2="96" stroke="#0f172a" stroke-width="1.2" stroke-dasharray="4 3"/><circle cx="133" cy="96" r="3.5" fill="#0f6e56" stroke="#0f6e56" stroke-width="1"/><line x1="133" y1="96" x2="133" y2="40" stroke="#0f6e56" stroke-width="2.6"/><polygon points="133,40 137.5,49 128.5,49" fill="#0f6e56"/><line x1="269" y1="96" x2="269" y2="156" stroke="#ef4444" stroke-width="2.6"/><polygon points="269,156 264.5,147 273.5,147" fill="#ef4444"/><line x1="241" y1="96" x2="241" y2="111" stroke="#ef4444" stroke-width="2.6"/><polygon points="241,111 236.5,102 245.5,102" fill="#ef4444"/><g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="139" y="34" text-anchor="start" fill="#0f6e56" font-size="12">FT</text><text x="109" y="110" text-anchor="middle" fill="#0f172a" font-size="11">rm</text><text x="276" y="138" text-anchor="start" fill="#ef4444" font-size="12">T</text><text x="235" y="126" text-anchor="end" fill="#ef4444" font-size="12">t</text><text x="264" y="91" text-anchor="middle" fill="#0f172a" font-size="10">rp</text><text x="85" y="168" text-anchor="middle" fill="#0f172a" font-size="11">Meule (3)</text><text x="255" y="168" text-anchor="middle" fill="#0f172a" font-size="11">Poulie (2)</text><text x="137" y="90" text-anchor="start" fill="#0f172a" font-size="12">D</text></g></svg>
:::

Le rayon rm de la figure est celui de la formule FT × rm, et le rayon rp celui de (T − t) × rp. Les deux disques sont dessinés à l'échelle l'un de l'autre : 75 mm contre 22 mm.

::: exemple Trouver Mt, T et t

1. **Moment de torsion.** Mt = FT × rm = 110 × 75 = 8 250 N·mm, soit **8,25 N·m** : FT est tangente, son bras est le rayon de la meule.
2. **Équilibre de rotation.** (T − t) × 22 = 8 250, donc T − t = 8 250 / 22 = **375 N** : l'arbre n'accélère pas, les deux moments sont égaux.
3. **Relation du manuel.** T = 4 t donne 4 t − t = 3 t = 375, donc t = **125 N** et T = **500 N**.
4. **Somme verticale.** T + t = 500 + 125 = **625 N** : c'est la force que la courroie appuie sur l'arbre, celle de la section précédente. Contrôle : (500 − 125) × 22 = 8 250 N·mm ✓.

:::

::: piege Les brins s'additionnent en force, se retranchent en rotation
Les deux brins tirent vers le bas : leurs effets sur la **position** de l'arbre s'ajoutent, d'où T + t = 625 N qui le plie. Mais ils tirent sur la poulie en sens contraires de part et d'autre de l'axe : leurs effets de **rotation** se retranchent, d'où T − t = 375 N qui le tord. Écrire (T + t) × rp = 625 × 22 = 13 750 N·mm donnerait un couple bien supérieur aux 8 250 N·mm de la meule.
:::

::: propriete Le moment de torsion est constant de O à B
Le couple entre dans l'arbre en O (la meule) et en sort en B (la poulie). Entre les deux, rien ne l'ajoute ni ne le retire : les paliers sont parfaits, donc ils n'exercent aucun couple autour de l'axe. Mt vaut donc **8,25 N·m en toute section** de O à B, y compris sous les paliers A et C. Seule l'unité demande de l'attention : 8 250 N·mm et 8,25 N·m désignent le même moment.
:::

::: verifie
Avec FT = 100 N, rm = 75 mm et rp = 25 mm (valeurs d'illustration), toujours avec T = 4 t, que valent Mt, t et T ?
---

Mt = 100 × 75 = 7 500 N·mm = **7,5 N·m**. L'équilibre donne (T − t) × 25 = 7 500, donc T − t = 300 N. Avec T = 4 t, 3 t = 300, d'où **t = 100 N** et **T = 400 N**.
:::

## ⚖️ Les réactions des paliers

L'arbre repose sur deux paliers, en A et en C. Ils le poussent pour l'empêcher de tomber ou de basculer. Deux inconnues, RA et RC, donc il faut deux équations.

Comment les écrire pour qu'une seule inconnue reste dans chacune ?

::: methode Écrire l'équilibre de la poutre
La poutre est en équilibre : la **somme des forces** est nulle et la **somme des moments** est nulle. On prend l'axe y vers le haut. Le moment d'une force verticale Fy appliquée à l'abscisse xi, calculé **au point A**, vaut Fy × (xi − xA), positif dans le sens trigonométrique.

1. Écrire la somme des forces suivant y, égale à zéro.
2. Écrire la somme des moments **en A** : RA a un bras nul, il disparaît et il reste RC seule.
3. En déduire RC, puis RA avec l'équation des forces.
4. Contrôler en écrivant les moments en C.

:::

Le tableau des actions suit celui du manuel, avec les abscisses ajoutées :

| Force | Point | x (mm) | Projection sur Ox | Projection sur Oy (N) |
| ----- | ----- | ------ | ----------------- | --------------------- |
| FT    | O     | 0      | 0                 | +110                  |
| RA    | A     | 100    | 0                 | inconnue              |
| P     | G     | 215    | 0                 | −30                   |
| RC    | C     | 340    | 0                 | inconnue              |
| T + t | B     | 430    | 0                 | −625                  |

Le tableau du manuel porte 30 N dans la colonne Oy du poids. Un poids est dirigé vers le bas : dans le repère où FT, vers le haut, vaut +110 N, il s'écrit −30 N (principe). Les projections sur Ox sont nulles, car aucune action n'est dirigée suivant l'axe de l'arbre.

::: exemple Calculer RA et RC

1. **Forces suivant y.** 110 + RA + RC − 30 − 625 = 0, donc RA + RC = **545 N**. C'est la somme à retrouver à la fin.
2. **Moments en A**, chaque bras étant mesuré depuis A : 110 × (0 − 100) + RC × (340 − 100) − 30 × (215 − 100) − 625 × (430 − 100) = 0, soit −11 000 + 240 RC − 3 450 − 206 250 = 0.
3. **Résolution.** 240 RC = 220 700, donc **RC ≈ 919,6 N**. RA n'apparaît pas : son bras est nul.
4. **Réaction en A.** RA = 545 − 919,6 ≈ **−374,6 N**. Le signe est négatif : le sens supposé (vers le haut) était faux, la réaction est dirigée **vers le bas**.
5. **Contrôle, moments en C.** −37 400 − 240 RA + 3 750 − 56 250 = 0, donc RA = −89 900 / 240 ≈ −374,6 N ✓.

:::

::: piege Les bras se mesurent depuis le point où l'on écrit les moments
Un élève dit « moments en A », mais garde les abscisses prises depuis O (215 pour P, 340 pour RC, 430 pour T + t) : il écrit 340 RC − 30 × 215 − 625 × 430 = 0 et trouve RC ≈ 809 N, au lieu de 919,6 N. Les distances et le point choisi doivent aller ensemble : en A, le bras de RC est 240, celui de P est 115.
:::

::: verifie
Une poutre est articulée en A (x = 0) et sur rouleaux en C (x = 200 mm). Une seule charge de 400 N, vers le bas, agit à x = 50 mm (valeurs d'illustration). Que valent RA et RC ?
---

Les moments en A, avec RA de bras nul, donnent 200 RC − 400 × 50 = 0, donc **RC = 100 N**. Les forces donnent RA + RC = 400, donc **RA = 300 N**. Les deux réactions sont vers le haut, et la plus grande est celle du palier le plus proche de la charge.
:::

## ✂️ Le moment fléchissant, tronçon par tronçon

On coupe l'arbre par la pensée à l'abscisse x. La partie de gauche tend à tourner autour de la coupure sous l'effet des forces qu'elle porte : c'est ce qui plie l'arbre à cet endroit.

Où cet effet est-il le plus grand, et comment le calculer en tout point ?

::: definition Moment fléchissant Mf(x)
Le **moment fléchissant** en une section d'abscisse x est le moment, par rapport à cette section, de toutes les forces situées **à gauche** de la coupure :

$$ Mf(x) = Σ Fy × (x − xi) $$

où la somme porte sur les forces d'abscisse xi < x. La somme change de forme à chaque point d'application d'une force : il faut donc **découper** l'arbre en tronçons. Ici le manuel en imprime quatre : 0 à 100 mm, 100 à 215 mm, 215 à 340 mm et 340 à 430 mm. Le signe dépend de la convention choisie ; seule la **valeur absolue** sert au dimensionnement (principe).
:::

::: figure Les quatre tronçons de l'arbre, de O à B, avec leurs abscisses en millimètres. La coupure rouge est dans le tronçon 2 : à sa gauche, seules FT et RA agissent. Chaque tronçon s'arrête à un point où une force s'applique
<svg viewBox="0 0 340 130"><title>Découpage de l'arbre en quatre tronçons et coupure à l'abscisse x</title><rect x="20" y="52" width="70" height="20" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.6"/><text x="55" y="67" text-anchor="middle" fill="#0f172a" font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><rect x="90" y="52" width="80.5" height="20" fill="#bbf7d0" stroke="#0f172a" stroke-width="1.6"/><text x="130.25" y="67" text-anchor="middle" fill="#0f172a" font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><rect x="170.5" y="52" width="87.5" height="20" fill="#fde68a" stroke="#0f172a" stroke-width="1.6"/><text x="214.25" y="67" text-anchor="middle" fill="#0f172a" font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">3</text><rect x="258" y="52" width="63" height="20" fill="#fecaca" stroke="#0f172a" stroke-width="1.6"/><text x="289.5" y="67" text-anchor="middle" fill="#0f172a" font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4</text><g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="20" y="40" text-anchor="middle" fill="#0f172a" font-size="13">O</text><text x="90" y="40" text-anchor="middle" fill="#0f172a" font-size="13">A</text><text x="170.5" y="40" text-anchor="middle" fill="#0f172a" font-size="13">G</text><text x="258" y="40" text-anchor="middle" fill="#0f172a" font-size="13">C</text><text x="321" y="40" text-anchor="middle" fill="#0f172a" font-size="13">B</text></g><g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="20" y="98" text-anchor="middle" fill="#0f172a" font-size="11">0</text><text x="90" y="98" text-anchor="middle" fill="#0f172a" font-size="11">100</text><text x="170.5" y="98" text-anchor="middle" fill="#0f172a" font-size="11">215</text><text x="258" y="98" text-anchor="middle" fill="#0f172a" font-size="11">340</text><text x="321" y="98" text-anchor="middle" fill="#0f172a" font-size="11">430</text></g><text x="18" y="118" text-anchor="start" fill="#0f172a" font-size="10" font-weight="500" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x en mm</text><line x1="125" y1="30" x2="125" y2="82" stroke="#ef4444" stroke-width="1.8" stroke-dasharray="4 3"/><text x="125" y="24" text-anchor="middle" fill="#ef4444" font-size="10" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">coupure à x</text><line x1="123" y1="12" x2="22" y2="12" stroke="#0f6e56" stroke-width="1.4"/><polygon points="22,12 28,9 28,15" fill="#0f6e56"/><text x="72.5" y="9" text-anchor="middle" fill="#0f6e56" font-size="10" font-weight="600" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">forces à gauche</text></svg>
:::

Les numéros de la figure sont ceux de la liste du manuel ; les abscisses 0, 100, 215, 340 et 430 sont celles de la colonne x du tableau des actions.

::: exemple Les expressions de Mf et leurs valeurs

1. **Tronçon 1** (0 ≤ x ≤ 100) : seule FT est à gauche, donc Mf = 110 x. En O : **0** ; en A : 11 000 N·mm = **11 N·m**.
2. **Tronçon 2** (100 ≤ x ≤ 215) : RA s'ajoute, donc Mf = 110 x − 374,6 (x − 100). En G : 23 650 − 43 077 ≈ −19 427 N·mm ≈ **−19,4 N·m**.
3. **Tronçon 3** (215 ≤ x ≤ 340) : P s'ajoute, donc Mf = 110 x − 374,6 (x − 100) − 30 (x − 215). En C : 37 400 − 89 900 − 3 750 = −56 250 N·mm = **−56,25 N·m**.
4. **Tronçon 4** (340 ≤ x ≤ 430) : il est plus court de regarder à droite, où seule T + t agit. La valeur absolue est |Mf| = 625 × (430 − x). En C : 625 × 90 = 56 250 N·mm, ce qui **confirme** l'étape 3. En B : 625 × 0 = **0**.

:::

| Point    | O   | A   | G     | C      | B   |
| -------- | --- | --- | ----- | ------ | --- |
| Mf (N·m) | 0   | +11 | −19,4 | −56,25 | 0   |

::: piege La plus grande force n'est pas le plus grand moment
T + t = 625 N est de loin la plus grande force du problème : on en déduit que l'arbre fléchit le plus en B. Mais en B le bras de levier est nul, donc Mf(B) = 0. C'est en C, à 90 mm de cette force, que le moment atteint 625 × 90 = 56 250 N·mm. Un moment est le produit d'une force **et** d'une distance.
:::

::: propriete Mf est une droite dans chaque tronçon
Dans un tronçon, les forces sont constantes, donc Mf(x) est une fonction affine de x : deux valeurs, aux deux extrémités, suffisent pour la tracer. La pente change quand on franchit un point d'application d'une force. Aux deux extrémités libres de l'arbre, O et B, il n'y a plus de force au-delà : Mf y vaut zéro.
:::

::: verifie
Que vaut Mf à l'abscisse x = 60 mm, et dans quel tronçon est-on ?
---

60 mm est dans le **tronçon 1** (0 ≤ x ≤ 100), où seule FT est à gauche de la coupure : Mf = 110 × 60 = 6 600 N·mm = **6,6 N·m**. RA n'intervient pas, car A est à droite de la coupure.
:::

## 📈 Les diagrammes et la section la plus sollicitée

Cinq points, cinq valeurs de Mf et une valeur de Mt : pour voir d'un coup d'œil où l'arbre souffre, on les trace.

Où se trouve la section la plus sollicitée ?

::: definition Diagramme des moments
Un **diagramme** porte l'abscisse x à l'horizontale et le moment à la verticale, les points O, A, G, C, B étant alignés sur ceux de l'arbre. Le diagramme de Mt est un **plateau**, car Mt est constant. Celui de Mf est une **ligne brisée** qui relie les valeurs calculées aux points d'application. On le lit en **valeur absolue** : c'est la grandeur du moment qui sollicite l'arbre, non son signe.
:::

::: figure Les diagrammes de Mt, en haut, et de Mf, en bas, sous les points O, A, G, C, B de l'arbre. Le plateau vert est le moment de torsion, constant de O à B. La ligne brisée orange passe par les valeurs du tableau : +11, −19,4 et −56,3 N·m. Les échelles des deux diagrammes sont différentes
<svg viewBox="0 0 340 244"><title>Diagrammes des moments de torsion Mt et de flexion Mf le long de l'arbre, de O à B</title><line x1="45" y1="22" x2="45" y2="232" stroke="#64748b" stroke-width="1" stroke-dasharray="2 3"/><line x1="107" y1="22" x2="107" y2="232" stroke="#64748b" stroke-width="1" stroke-dasharray="2 3"/><line x1="178.3" y1="22" x2="178.3" y2="232" stroke="#64748b" stroke-width="1" stroke-dasharray="2 3"/><line x1="255.8" y1="22" x2="255.8" y2="232" stroke="#64748b" stroke-width="1" stroke-dasharray="2 3"/><line x1="311.6" y1="22" x2="311.6" y2="232" stroke="#64748b" stroke-width="1" stroke-dasharray="2 3"/><g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="45" y="14" text-anchor="middle" fill="#0f172a" font-size="13">O</text><text x="107" y="14" text-anchor="middle" fill="#0f172a" font-size="13">A</text><text x="178.3" y="14" text-anchor="middle" fill="#0f172a" font-size="13">G</text><text x="255.8" y="14" text-anchor="middle" fill="#0f172a" font-size="13">C</text><text x="311.6" y="14" text-anchor="middle" fill="#0f172a" font-size="13">B</text></g><line x1="35" y1="70" x2="323.6" y2="70" stroke="#0f172a" stroke-width="1.4"/><polygon points="45,70 45,37 311.6,37 311.6,70" fill="#bbf7d0" stroke="#0f6e56" stroke-width="2"/><g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="178.3" y="32" text-anchor="middle" fill="#0f6e56" font-size="11">Mt = 8,25 N·m</text><text x="12" y="40" text-anchor="start" fill="#0f172a" font-size="11">Mt</text><text x="323.6" y="83" text-anchor="end" fill="#0f172a" font-size="10">x</text></g><line x1="35" y1="165" x2="323.6" y2="165" stroke="#0f172a" stroke-width="1.4"/><polygon points="45,165 107,152.9 178.3,186.37 255.8,226.87 311.6,165" fill="#fde68a" stroke="#d97706" stroke-width="2"/><circle cx="107" cy="152.9" r="2.8" fill="#0f172a" stroke="#0f172a" stroke-width="1"/><circle cx="178.3" cy="186.37" r="2.8" fill="#0f172a" stroke="#0f172a" stroke-width="1"/><circle cx="255.8" cy="226.87" r="2.8" fill="#0f172a" stroke="#0f172a" stroke-width="1"/><g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="109" y="146.9" text-anchor="start" fill="#0f172a" font-size="11">+11</text><text x="174.3" y="200.37" text-anchor="end" fill="#0f172a" font-size="11">−19,4</text><text x="249.8" y="232.87" text-anchor="end" fill="#d97706" font-size="11">−56,3</text><text x="12" y="128" text-anchor="start" fill="#0f172a" font-size="11">Mf</text><text x="323.6" y="178" text-anchor="end" fill="#0f172a" font-size="10">x</text></g></svg>
:::

Les cinq points de chaque diagramme sont ceux du tableau de la section précédente, et le plateau du haut est le Mt = 8,25 N·m de la section sur la torsion.

::: exemple Trouver la section la plus sollicitée

1. **Torsion.** Mt = 8,25 N·m est le même en toute section : il ne départage pas les sections.
2. **Flexion.** Les valeurs absolues de Mf sont 0, 11, 19,4, 56,25 et 0 N·m : la plus grande est 56,25 N·m, en C.
3. **Conclusion.** La section la plus sollicitée est celle de **C**, où la flexion est maximale et où la torsion est aussi présente. Comme Mt est le même partout, il suffit de chercher le maximum de |Mf|.

:::

::: piege Le signe n'est pas la gravité
Sur le diagramme, +11 est « plus grand » que −56,25, et un élève retient A pour cette raison. Il compare des nombres signés. Le signe ne donne que le côté où l'arbre se courbe ; ce qui compte pour la résistance est la valeur absolue : |−56,25| = 56,25 > 11. La section la plus sollicitée est donc C.
:::

::: verifie
Les trois sections d'un arbre ont Mf = +30, −45 et +20 N·m, avec un Mt constant. Laquelle est la plus sollicitée ?
---

Il faut comparer les valeurs absolues : 30, 45 et 20. La plus grande est 45, donc c'est la **deuxième** section (Mf = −45 N·m). Le signe négatif indique le sens de courbure, pas un effet plus faible. Comme Mt est constant, il ne change pas le classement.
:::

## 🔀 Flexion et torsion ensemble : le moment idéal

En C, l'arbre est plié (Mf = 56,25 N·m) et tordu (Mt = 8,25 N·m) en même temps. Ce sont deux sollicitations différentes, qui agissent sur la même section.

De quelle sollicitation s'agit-il, et comment les réunir en un seul nombre pour calculer le diamètre ?

::: definition Sollicitation composée
Une **sollicitation simple** est l'un de ces effets : **traction** ou **compression** (étirer ou écraser suivant l'axe), **torsion** (tordre autour de l'axe), **flexion** (plier). Une section subit une **sollicitation composée** quand elle en subit **plusieurs à la fois**.

Pour l'arbre du touret, les forces perpendiculaires à l'axe (FT, P, T + t, RA, RC) créent la **flexion** (Mf ≠ 0), et le couple FT × rm crée la **torsion** (Mt ≠ 0). Aucune action n'est dirigée suivant l'axe x : ni traction, ni compression. L'arbre porte-meule est soumis à de la **flexion-torsion**.
:::

::: definition Le moment idéal de flexion
Le chapitre 19 (micro-tour) a introduit ce moment ; on le réutilise ici. Pour calculer le diamètre, on remplace Mf et Mt par un seul moment de flexion, le **moment idéal** Mfi, qui produit la même contrainte maximale que les deux ensemble (principe). La formule du manuel est :

$$ Mfi = (1 − 1/(2λ)) × Mf + (1/(2λ)) × √(Mf² + Mt²) $$

où λ est le rapport des résistances pratiques au glissement et à l'extension, λ = Rpg / Rpe. Pour l'acier de l'arbre, le manuel donne λ = 0,5. Alors 1/(2λ) = 1 et 1 − 1/(2λ) = 0 : le premier terme disparaît et il reste

$$ Mfi = √(Mf² + Mt²) $$
:::

::: exemple Le moment idéal en C

1. **Valeur de λ.** λ = 0,5 donne 1/(2λ) = 1 : on utilise la forme simplifiée, Mfi = √(Mf² + Mt²).
2. **Les carrés.** Mf² = 56,25² ≈ 3 164,1 et Mt² = 8,25² ≈ 68,1, en N²·m².
3. **La racine.** Mfi = √(3 164,1 + 68,1) = √3 232,1 ≈ **56,85 N·m**.
4. **Plausibilité.** Mfi est un peu plus grand que Mf (56,25) et bien plus petit que Mf + Mt (64,5) : 56,25 < 56,85 < 64,5.

:::

::: piege Mfi se calcule dans la bonne section
On calcule Mfi dans une section prise au hasard, par exemple en G : √(19,4² + 8,25²) ≈ 21,1 N·m. Ce moment ne dimensionne rien, car la section G n'est pas la plus sollicitée. Mfi se calcule dans la section où |Mf| est maximal (ici C, 56,85 N·m), puisque Mt est le même partout.
:::

::: propriete Deux cas limites de Mfi
Avec λ = 0,5, si la torsion est nulle (Mt = 0), alors Mfi = √(Mf²) = Mf : on retrouve la flexion simple. Si la flexion est nulle (Mf = 0), alors Mfi = Mt. Entre les deux, Mfi est toujours au moins égal au plus grand des deux moments. Quand Mt varie le long de l'arbre, on calcule Mfi dans chaque section candidate ; ici Mt est constant, donc la section de Mf maximal reste la plus sollicitée.
:::

::: verifie
En une section, Mf = 6 N·m et Mt = 8 N·m (valeurs d'illustration, λ = 0,5). Que vaut Mfi ?
---

Mfi = √(6² + 8²) = √(36 + 64) = √100 = **10 N·m**. On additionne les carrés, puis on prend la racine : le résultat est inférieur à 6 + 8 = 14, et supérieur à chacun des deux moments.
:::

## 📏 La condition de résistance et le diamètre minimal

Tout le calcul précédent sert une question : quel est le plus petit diamètre pour lequel l'arbre ne cède pas, et le choix du constructeur est-il bon ?

Comment passer d'un moment en N·m à un diamètre en mm ?

::: definition La condition de résistance à la flexion
Dans une section circulaire pleine de diamètre d, la contrainte normale maximale due au moment idéal est (principe) :

$$ σ = Mfi / (π × d³ / 32) $$

La condition de résistance exige que σ ne dépasse pas la **résistance pratique à l'extension** Rpe, égale à la limite d'élasticité Re divisée par le **coefficient de sécurité** s :

$$ σ ≤ Rpe, avec Rpe = Re / s $$

Le manuel donne un acier **S275** et s = 2. La désignation S275 indique une limite d'élasticité Re = 275 MPa (principe), donc Rpe = 275 / 2 = **137,5 MPa**. En résolvant pour d :

$$ d³ ≥ 32 × Mfi / (π × Rpe) $$

et d est la racine cubique du second membre. Les unités sont cohérentes en **N·mm et MPa** (1 MPa = 1 N/mm²) : d sort en mm.
:::

::: exemple Le diamètre minimal de l'arbre

1. **Moment idéal en N·mm.** Mfi = 56,85 N·m = 56 852 N·mm : on convertit avant de calculer, puisque Rpe est en N/mm².
2. **Cube du diamètre.** d³ ≥ 32 × 56 852 / (π × 137,5) = 1 819 264 / 431,97 ≈ 4 211 mm³.
3. **Racine cubique.** d ≥ 4 211^(1/3) ≈ **16,15 mm**. Le diamètre minimal est d'environ 16,2 mm.
4. **Vérifier le choix du constructeur.** On relève le diamètre sur le dessin d'ensemble (non reproduit ici) et on le compare : il doit être **supérieur ou égal** à 16,2 mm. Avec 20 mm (valeur d'illustration), 20 ≥ 16,2 est vrai, et la contrainte réelle est 1 819 264 / (π × 20³) ≈ 72 MPa, inférieure à 137,5 MPa.

:::

::: piege Les unités doivent s'accorder
Si l'on garde Mfi = 56,85 en N·m avec Rpe = 137,5 MPa, on trouve d³ = 32 × 56,85 / (π × 137,5) ≈ 4,21 et d ≈ 1,6 mm : dix fois trop petit, puisque 1 N·m = 1 000 N·mm et que le diamètre est la racine cubique de ce facteur 1 000. L'autre erreur classique est de prendre Re = 275 MPa à la place de Rpe : le coefficient de sécurité est alors oublié, et le diamètre calculé tombe à environ 12,8 mm, ce qui est insuffisant.
:::

::: propriete d est un minimum, et la contrainte varie en 1/d³
La condition donne un diamètre **minimal** : le constructeur peut choisir plus grand, jamais plus petit, en général une valeur normalisée au-dessus. Comme d intervient au cube, doubler le diamètre divise la contrainte par 2³ = 8, alors qu'il ne multiplie la masse de l'arbre que par 4 (la section varie avec d²). C'est pourquoi un petit gain de diamètre apporte une grande marge.
:::

::: verifie
Avec Mfi = 10 N·m et Rpe = 100 MPa (valeurs d'illustration), quel est le diamètre minimal ?
---

On convertit : Mfi = 10 000 N·mm. Alors d³ ≥ 32 × 10 000 / (π × 100) = 320 000 / 314,16 ≈ 1 018,6 mm³, donc d ≥ 1 018,6^(1/3) ≈ **10,06 mm**, soit environ 10,1 mm. Sans la conversion en N·mm, le résultat serait dix fois trop petit.
:::

## 🧭 La méthode qui reste : sept marches

Devant un arbre soumis à de la flexion et de la torsion, reprends toujours cet ordre :

1. **Modéliser** : placer les points, les appuis (articulé, à rouleaux) et les actions, avec leurs abscisses.
2. **Équilibrer la rotation** : Mt = FT × rm, T − t = Mt / rp, puis T et t ; Mt est constant de la meule à la poulie.
3. **Trouver les réactions** : forces suivant y, moments en A, puis contrôle en C.
4. **Calculer Mf** tronçon par tronçon, en regardant du côté qui a le moins de forces.
5. **Tracer et lire** : la section la plus sollicitée est celle où |Mf| est maximal quand Mt est constant.
6. **Composer** : Mfi = √(Mf² + Mt²) avec λ = 0,5.
7. **Dimensionner** : d³ ≥ 32 × Mfi / (π × Rpe), avec Rpe = Re / s, puis comparer avec le dessin.

::: retenir
Un arbre chargé de **forces transversales** et d'un **couple** subit de la **flexion-torsion** : **Mt** vaut FT × rm et reste constant de O à B ; **Mf** se calcule par tronçons et culmine en **C** ; le **moment idéal** Mfi = √(Mf² + Mt²) (λ = 0,5) donne le diamètre par **d³ ≥ 32 × Mfi / (π × Rpe)**, avec Rpe = Re / s, et le diamètre choisi doit être **au moins égal** au minimum.
:::

> 🏆 De la meule à la poulie, tu as suivi chaque force jusqu'au diamètre de l'arbre. Il ne reste qu'à mettre ces calculs à l'épreuve.
