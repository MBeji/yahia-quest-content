# ⚔️ Étude de fonctions — lire la courbe d'un coût, d'un bénéfice, d'un marché

> 💡 «Une étude de fonction transforme une formule en portrait : où la courbe s'envole, où elle se couche contre une droite, où elle culmine.»

Bienvenue, héros de l'Économie et gestion. Un coût moyen qui explose pour une toute petite production, un bénéfice qui culmine puis s'effondre, un marché qui trouve son prix : une courbe bien étudiée répond à ces questions sans tâtonner. Sept étapes te mènent des asymptotes au point d'équilibre : asymptotes, branches paraboliques, symétries, translations et valeur absolue, plan d'étude complet, optimisation d'un coût ou d'un bénéfice, offre et demande. On suppose acquis les limites, la dérivation et le signe de la dérivée (chapitres 1 et 2).

## 🧱 Asymptotes : verticale, horizontale, oblique

Une chocolaterie fabrique x milliers de tablettes ; son coût total est C(x) = 4x² + 80 milliers de dinars, donc son coût moyen par millier est CM(x) = (4x² + 80)/x, pour x > 0.
Que devient CM quand on produit très peu, puis quand on produit énormément ?

::: definition
Soit C la courbe de f dans un repère.

- La droite **x = a** est une **asymptote verticale** si f(x) tend vers +∞ ou −∞ quand x tend vers a (à droite ou à gauche de a).
- La droite **y = b** est une **asymptote horizontale** si f(x) tend vers le réel b quand x tend vers +∞ ou vers −∞.
- La droite **y = ax + b** (a ≠ 0) est une **asymptote oblique** si la différence f(x) − (ax + b) tend vers 0 quand x tend vers +∞ ou vers −∞.
:::

::: figure La courbe du coût moyen se colle à l'axe x = 0 près de l'origine et à la droite y = 4x loin de l'origine
<svg viewBox="0 0 340 250"><title>Courbe du coût moyen CM(x) = 4x + 80/x pour x > 0, avec l'asymptote verticale x = 0 et l'asymptote oblique y = 4x</title><polyline points="88.2,13.6 89.5,23.8 90.7,32.9 91.9,41.1 93.1,48.6 94.3,55.4 95.5,61.6 96.7,67.2 97.9,72.4 99.1,77.2 100.3,81.6 101.6,85.7 102.8,89.5 104.0,93.1 105.2,96.3 106.4,99.4 107.6,102.3 108.8,104.9 110.0,107.5 111.2,109.8 112.5,112.0 113.7,114.1 114.9,116.0 116.1,117.9 117.3,119.6 118.5,121.2 119.7,122.8 120.9,124.2 122.1,125.6 123.4,126.9 124.6,128.1 125.8,129.3 127.0,130.4 128.2,131.4 129.4,132.4 130.6,133.4 131.8,134.3 133.0,135.1 134.3,135.9 135.5,136.7 136.7,137.4 137.9,138.0 139.1,138.7 140.3,139.3 141.5,139.9 142.7,140.4 143.9,140.9 145.2,141.4 146.4,141.9 147.6,142.3 148.8,142.7 150.0,143.1 151.2,143.5 152.4,143.8 153.6,144.2 154.8,144.5 156.1,144.7 157.3,145.0 158.5,145.3 159.7,145.5 160.9,145.7 162.1,145.9 163.3,146.1 164.5,146.3 165.7,146.4 166.9,146.6 168.2,146.7 169.4,146.8 170.6,146.9 171.8,147.0 173.0,147.1 174.2,147.2 175.4,147.3 176.6,147.3 177.8,147.4 179.1,147.4 180.3,147.4 181.5,147.4 182.7,147.4 183.9,147.4 185.1,147.4 186.3,147.4 187.5,147.4 188.7,147.4 190.0,147.3 191.2,147.3 192.4,147.2 193.6,147.2 194.8,147.1 196.0,147.0 197.2,147.0 198.4,146.9 199.6,146.8 200.9,146.7 202.1,146.6 203.3,146.5 204.5,146.4 205.7,146.3 206.9,146.1 208.1,146.0 209.3,145.9 210.5,145.8 211.8,145.6 213.0,145.5 214.2,145.3 215.4,145.2 216.6,145.0 217.8,144.9 219.0,144.7 220.2,144.5 221.4,144.4 222.7,144.2 223.9,144.0 225.1,143.8 226.3,143.7 227.5,143.5 228.7,143.3 229.9,143.1 231.1,142.9 232.3,142.7 233.5,142.5 234.8,142.3 236.0,142.1 237.2,141.9 238.4,141.7 239.6,141.5 240.8,141.2 242.0,141.0 243.2,140.8 244.4,140.6 245.7,140.3 246.9,140.1 248.1,139.9 249.3,139.7 250.5,139.4 251.7,139.2 252.9,138.9 254.1,138.7 255.3,138.5 256.6,138.2 257.8,138.0 259.0,137.7 260.2,137.5 261.4,137.2 262.6,137.0 263.8,136.7 265.0,136.4 266.2,136.2 267.5,135.9 268.7,135.7 269.9,135.4 271.1,135.1 272.3,134.9 273.5,134.6 274.7,134.3 275.9,134.1 277.1,133.8 278.4,133.5 279.6,133.2 280.8,133.0 282.0,132.7 283.2,132.4 284.4,132.1 285.6,131.8 286.8,131.5 288.0,131.3 289.3,131.0 290.5,130.7 291.7,130.4 292.9,130.1 294.1,129.8 295.3,129.5 296.5,129.2 297.7,128.9 298.9,128.6 300.1,128.3 301.4,128.1 302.6,127.8 303.8,127.5 305.0,127.2 306.2,126.9 307.4,126.5 308.6,126.2 309.8,125.9 311.0,125.6 312.3,125.3 313.5,125.0 314.7,124.7 315.9,124.4 317.1,124.1 318.3,123.8 319.5,123.5 320.7,123.2 321.9,122.9 323.2,122.5 324.4,122.2 325.6,121.9 326.8,121.6 328.0,121.3" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><line x1="66.2" y1="224.0" x2="328.0" y2="138.4" stroke="#b45309" stroke-width="2.2"/><line x1="66.2" y1="224.0" x2="66.2" y2="10.0" stroke="#7c3aed" stroke-width="2.4" stroke-dasharray="6 4"/><line x1="34" y1="224.0" x2="336" y2="224.0" stroke="#0f172a" stroke-width="1.6"/><line x1="66.2" y1="230" x2="66.2" y2="6" stroke="#0f172a" stroke-width="1.6"/><polygon points="336,224.0 329,220.5 329,227.5" fill="#0f172a"/><polygon points="66.2,6 62.7,13 69.7,13" fill="#0f172a"/><text x="332.0" y="217.0" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x</text><text x="74.2" y="18.0" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">CM</text><line x1="118.5" y1="221.0" x2="118.5" y2="227.0" stroke="#0f172a" stroke-width="1.3"/><text x="118.5" y="239.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><line x1="170.9" y1="221.0" x2="170.9" y2="227.0" stroke="#0f172a" stroke-width="1.3"/><text x="170.9" y="239.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4</text><line x1="223.3" y1="221.0" x2="223.3" y2="227.0" stroke="#0f172a" stroke-width="1.3"/><text x="223.3" y="239.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">6</text><line x1="275.6" y1="221.0" x2="275.6" y2="227.0" stroke="#0f172a" stroke-width="1.3"/><text x="275.6" y="239.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">8</text><line x1="328.0" y1="221.0" x2="328.0" y2="227.0" stroke="#0f172a" stroke-width="1.3"/><text x="328.0" y="239.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">10</text><line x1="63.2" y1="181.2" x2="69.2" y2="181.2" stroke="#0f172a" stroke-width="1.3"/><text x="59.2" y="185.2" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">20</text><line x1="63.2" y1="138.4" x2="69.2" y2="138.4" stroke="#0f172a" stroke-width="1.3"/><text x="59.2" y="142.4" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">40</text><line x1="63.2" y1="95.6" x2="69.2" y2="95.6" stroke="#0f172a" stroke-width="1.3"/><text x="59.2" y="99.6" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">60</text><line x1="63.2" y1="52.8" x2="69.2" y2="52.8" stroke="#0f172a" stroke-width="1.3"/><text x="59.2" y="56.8" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">80</text><circle cx="170.9" cy="147.0" r="4" fill="#0f172a" stroke="#0f172a" stroke-width="1"/><text x="178.9" y="139.0" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">CM(4) = 36</text><text x="220.7" y="185.5" text-anchor="start" font-size="11" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">y = 4x</text><text x="74.0" y="27.1" text-anchor="start" font-size="11" font-weight="700" fill="#7c3aed" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x = 0</text></svg>
:::

La droite violette en pointillés est l'asymptote verticale x = 0 ; la droite orange y = 4x est l'asymptote oblique : l'écart vertical entre la courbe et la droite, 80/x, devient aussi petit qu'on veut.

::: exemple Le coût moyen de la chocolaterie : CM(x) = (4x² + 80)/x
1. Quand x tend vers 0 par valeurs positives, le numérateur tend vers 80 > 0 et le dénominateur vers 0⁺ : CM(x) tend vers +∞. La droite x = 0 est donc asymptote verticale.
2. On sépare : CM(x) = 4x + 80/x. Alors CM(x) − 4x = 80/x, qui tend vers 0 quand x tend vers +∞ : la droite y = 4x est asymptote oblique.
3. Comme 80/x > 0 pour x > 0, la courbe reste au-dessus de la droite : CM(x) > 4x. Contrôle : CM(4) = 36 > 16.

:::

Pour une asymptote horizontale, la limite en l'infini est un réel. Le rendement d'un apprenti, mesuré en pièces par heure après t semaines, vaut R(t) = (50t + 20)/(t + 4) pour t ≥ 0.

::: exemple Le rendement R(t) = (50t + 20)/(t + 4)
1. On factorise par t en haut et en bas : R(t) = (50 + 20/t)/(1 + 4/t). Quand t tend vers +∞, 20/t et 4/t tendent vers 0, donc R(t) tend vers 50 : la droite y = 50 est asymptote horizontale.
2. Le dénominateur s'annule en t = −4, mais −4 n'appartient pas au domaine [0 ; +∞[ : ce n'est pas une asymptote de cette courbe.
3. 50 − R(t) = 180/(t + 4) > 0 : le rendement reste sous 50 et s'en rapproche.

:::

::: piege Croire que « le dénominateur s'annule » suffit pour une asymptote verticale
Pour f(x) = (x² − 4)/(x − 2), on écrit « le dénominateur s'annule en 2, donc x = 2 est asymptote verticale ». Cela tente parce que, dans CM, c'est ce qui se passe. Mais ici le numérateur s'annule aussi : x² − 4 = (x − 2)(x + 2), donc f(x) = x + 2 pour x ≠ 2 et f(x) tend vers 4, un réel. Test : f(2,001) = 4,001. Il n'y a pas d'asymptote en 2, seulement un trou dans la courbe.
:::

::: propriete
- Pour une asymptote verticale, on étudie f aux valeurs interdites et aux bornes ouvertes du domaine ; si la limite est un réel, il n'y a pas d'asymptote.
- Pour une asymptote horizontale, on calcule la limite en +∞ et en −∞ ; elles peuvent être différentes.
- Pour une asymptote oblique, on écrit f(x) = ax + b + g(x) avec g(x) tendant vers 0 (division euclidienne pour une fraction dont le degré du numérateur dépasse de 1 celui du dénominateur) ; le signe de g(x) donne la **position relative** de la courbe et de la droite.

Cas limite : la courbe peut avoir une asymptote horizontale en +∞ et une autre direction en −∞ ; on traite chaque côté séparément.
:::

::: verifie
Soit g(x) = (2x² − x + 3)/(x − 1) sur ℝ \ {1}. Déterminer les asymptotes de la courbe et sa position par rapport à l'asymptote oblique.

---

En 1, le numérateur vaut 2 − 1 + 3 = 4 ≠ 0 et le dénominateur tend vers 0 : g tend vers +∞ à droite de 1 et vers −∞ à gauche, donc x = 1 est asymptote verticale. Par division, 2x² − x + 3 = (x − 1)(2x + 1) + 4, donc g(x) = 2x + 1 + 4/(x − 1). Comme 4/(x − 1) tend vers 0 en +∞ et en −∞, la droite y = 2x + 1 est asymptote oblique des deux côtés. Le signe de 4/(x − 1) est celui de x − 1 : la courbe est au-dessus de la droite pour x > 1 et en dessous pour x < 1.
:::

::: retenir
Une asymptote est une droite dont la courbe se rapproche indéfiniment : x = a quand f tend vers ±∞ en a, y = b quand f tend vers b en l'infini, y = ax + b quand f(x) − (ax + b) tend vers 0 ; le signe de cet écart donne la position relative.
:::

## 🚀 Branches paraboliques : quand la courbe n'a pas de droite pour guide

Le coût total d'un atelier de menuiserie est C(x) = 0,5x² + 10x milliers de dinars pour x milliers de planches. Le coût moyen C(x)/x = 0,5x + 10 grandit sans limite : la courbe de C s'envole.
Se rapproche-t-elle d'une droite, et vers quelle direction se redresse-t-elle ?

::: definition
Soit f une fonction dont la limite en +∞ est +∞ ou −∞. On étudie le quotient f(x)/x :

- si f(x)/x tend vers 0, la courbe a une **branche parabolique de direction l'axe des abscisses** ;
- si f(x)/x tend vers +∞ ou −∞, la courbe a une **branche parabolique de direction l'axe des ordonnées** ;
- si f(x)/x tend vers un réel a ≠ 0, on calcule f(x) − ax : si cette différence tend vers un réel b, la droite y = ax + b est **asymptote oblique** ; si elle tend vers +∞ ou −∞, la courbe a une **branche parabolique de direction la droite y = ax**.

On raisonne de même en −∞.
:::

::: exemple Trois courbes, trois comportements
1. Menuiserie : C(x) = 0,5x² + 10x. Le quotient C(x)/x = 0,5x + 10 tend vers +∞, donc la courbe a une branche parabolique de direction l'axe des ordonnées : elle devient de plus en plus raide.
2. Recette d'une brasserie : R(x) = 12√x, qui tend vers +∞. Le quotient R(x)/x = 12/√x tend vers 0 : branche parabolique de direction l'axe des abscisses, la courbe s'aplatit sans jamais plafonner.
3. f(x) = 2x + √x. Le quotient f(x)/x = 2 + 1/√x tend vers 2, puis f(x) − 2x = √x tend vers +∞ : branche parabolique de direction la droite y = 2x. Pour comparer, g(x) = 2x + 5 + 1/x a g(x) − 2x = 5 + 1/x qui tend vers 5 : y = 2x + 5 est asymptote oblique de g.

:::

::: piege Conclure à une asymptote parce que f(x)/x a une limite réelle
Pour f(x) = 2x + √x, on écrit « f(x)/x tend vers 2, donc y = 2x est asymptote oblique ». Cela tente parce que 2 est le coefficient dominant. Mais le quotient ne dit que la pente : il faut encore calculer f(x) − 2x. Test : f(100) − 200 = 10, f(10 000) − 20 000 = 100 : l'écart grandit, la courbe s'éloigne de la droite.
:::

::: propriete
- Le quotient f(x)/x donne la **direction** de la courbe à l'infini ; la différence f(x) − ax décide s'il y a une asymptote ou seulement une branche parabolique.
- Un polynôme de degré 2 ou plus a une branche parabolique de direction l'axe des ordonnées.
- Si f(x)/x n'a pas de limite, ces critères ne permettent pas de conclure.

Cas limite : f(x) = √x tend vers +∞ mais f(x)/x = 1/√x tend vers 0 : la courbe monte plus lentement que n'importe quelle droite, sans avoir de limite réelle, donc sans asymptote horizontale.
:::

::: verifie
Étudier la branche infinie de f(x) = x − 4√x en +∞.

---

f(x) tend vers +∞ car x domine √x. Le quotient f(x)/x = 1 − 4/√x tend vers 1 ; puis f(x) − x = −4√x tend vers −∞. La courbe a donc une branche parabolique de direction la droite y = x, sans asymptote : elle passe sous cette droite et s'en éloigne.
:::

::: retenir
Quand f tend vers l'infini, le quotient f(x)/x donne la direction : 0 pour l'axe des abscisses, ±∞ pour l'axe des ordonnées, a ≠ 0 pour la droite y = ax, et f(x) − ax décide entre asymptote oblique et branche parabolique.
:::

## 🪞 Parité, axe et centre de symétrie

Une maroquinerie estime son bénéfice, en centaines de dinars, à B(x) = −x² + 12x − 20 pour x dizaines de sacs, 0 ≤ x ≤ 12. On calcule B(4) = 12 et B(8) = 12 : deux productions, le même bénéfice, et 6 est le milieu de 4 et 8.
Comment prouver que la courbe est symétrique autour de la droite x = 6 pour toutes les valeurs de x ?

::: definition
Soit f définie sur un domaine D.

- f est **paire** si D est symétrique par rapport à 0 et si f(−x) = f(x) pour tout x de D : la courbe est symétrique par rapport à l'axe des ordonnées.
- f est **impaire** si D est symétrique par rapport à 0 et si f(−x) = −f(x) : la courbe est symétrique par rapport à l'origine.
- La droite **x = a** est un **axe de symétrie** si, pour tout x de D, 2a − x appartient à D et f(2a − x) = f(x).
- Le point **I(a ; b)** est un **centre de symétrie** si, pour tout x de D, 2a − x appartient à D et f(2a − x) = 2b − f(x).
- f est **périodique** de période t ≠ 0 si, pour tout x de D, x + t appartient à D et f(x + t) = f(x) : on l'étudie sur un intervalle de longueur t, puis on complète la courbe par des translations de vecteur t i.
:::

::: figure Le point I(3 ; 18) est le milieu de tous les segments qui joignent deux points de la courbe d'abscisses 3 − t et 3 + t, comme [AB]
<svg viewBox="0 0 340 270"><title>Courbe de f : x ↦ x³ − 9x² + 24x, et son centre de symétrie I(3 ; 18), milieu du segment [AB] avec A(2 ; 20) et B(4 ; 16)</title><polyline points="43.8,223.0 45.2,218.4 46.6,213.9 48.0,209.5 49.4,205.2 50.8,201.0 52.2,196.9 53.7,192.8 55.1,188.9 56.5,185.0 57.9,181.2 59.3,177.5 60.7,173.9 62.1,170.4 63.5,166.9 64.9,163.5 66.3,160.2 67.7,157.0 69.1,153.9 70.5,150.8 71.9,147.8 73.3,144.9 74.7,142.1 76.1,139.3 77.5,136.7 78.9,134.0 80.3,131.5 81.7,129.0 83.1,126.6 84.5,124.3 85.9,122.0 87.3,119.8 88.7,117.7 90.1,115.6 91.5,113.6 92.9,111.6 94.3,109.7 95.7,107.9 97.1,106.2 98.5,104.5 99.9,102.8 101.3,101.2 102.7,99.7 104.1,98.2 105.5,96.8 106.9,95.5 108.3,94.2 109.7,92.9 111.1,91.7 112.5,90.5 113.9,89.4 115.3,88.4 116.7,87.4 118.1,86.4 119.5,85.5 120.9,84.7 122.3,83.8 123.7,83.1 125.1,82.3 126.5,81.6 127.9,81.0 129.3,80.4 130.7,79.8 132.1,79.3 133.5,78.8 134.9,78.4 136.3,77.9 137.7,77.6 139.1,77.2 140.6,76.9 142.0,76.6 143.4,76.4 144.8,76.2 146.2,76.0 147.6,75.8 149.0,75.7 150.4,75.6 151.8,75.5 153.2,75.5 154.6,75.4 156.0,75.4 157.4,75.5 158.8,75.5 160.2,75.6 161.6,75.7 163.0,75.8 164.4,75.9 165.8,76.1 167.2,76.2 168.6,76.4 170.0,76.6 171.4,76.8 172.8,77.0 174.2,77.3 175.6,77.5 177.0,77.8 178.4,78.0 179.8,78.3 181.2,78.6 182.6,78.9 184.0,79.2 185.4,79.5 186.8,79.8 188.2,80.1 189.6,80.5 191.0,80.8 192.4,81.1 193.8,81.4 195.2,81.8 196.6,82.1 198.0,82.4 199.4,82.7 200.8,83.0 202.2,83.4 203.6,83.7 205.0,84.0 206.4,84.3 207.8,84.5 209.2,84.8 210.6,85.1 212.0,85.3 213.4,85.6 214.8,85.8 216.2,86.0 217.6,86.2 219.0,86.4 220.4,86.6 221.8,86.8 223.2,86.9 224.6,87.0 226.0,87.1 227.4,87.2 228.9,87.3 230.3,87.3 231.7,87.3 233.1,87.3 234.5,87.3 235.9,87.2 237.3,87.2 238.7,87.0 240.1,86.9 241.5,86.7 242.9,86.6 244.3,86.3 245.7,86.1 247.1,85.8 248.5,85.5 249.9,85.1 251.3,84.7 252.7,84.3 254.1,83.8 255.5,83.3 256.9,82.8 258.3,82.2 259.7,81.6 261.1,80.9 262.5,80.2 263.9,79.5 265.3,78.7 266.7,77.9 268.1,77.0 269.5,76.1 270.9,75.1 272.3,74.1 273.7,73.0 275.1,71.9 276.5,70.7 277.9,69.5 279.3,68.2 280.7,66.9 282.1,65.5 283.5,64.1 284.9,62.6 286.3,61.1 287.7,59.5 289.1,57.8 290.5,56.1 291.9,54.3 293.3,52.5 294.7,50.6 296.1,48.6 297.5,46.6 298.9,44.5 300.3,42.3 301.7,40.1 303.1,37.8 304.5,35.4 305.9,33.0 307.3,30.5 308.7,28.0 310.1,25.3 311.5,22.6 312.9,19.8 314.3,17.0 315.8,14.0 317.2,11.0" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><line x1="155.2" y1="75.4" x2="232.0" y2="87.3" stroke="#b45309" stroke-width="1.8" stroke-dasharray="5 3"/><circle cx="155.2" cy="75.4" r="4" fill="#0f172a" stroke="#0f172a" stroke-width="1"/><text x="147.2" y="67.4" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">A</text><circle cx="232.0" cy="87.3" r="4" fill="#0f172a" stroke="#0f172a" stroke-width="1"/><text x="240.0" y="103.3" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">B</text><circle cx="193.6" cy="81.4" r="4" fill="#b45309" stroke="#b45309" stroke-width="1"/><text x="202.6" y="72.4" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">I(3 ; 18)</text><line x1="34" y1="134.9" x2="336" y2="134.9" stroke="#0f172a" stroke-width="1.6"/><line x1="78.4" y1="248" x2="78.4" y2="6" stroke="#0f172a" stroke-width="1.6"/><polygon points="336,134.9 329,131.4 329,138.4" fill="#0f172a"/><polygon points="78.4,6 74.9,13 81.9,13" fill="#0f172a"/><text x="332.0" y="127.9" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x</text><text x="86.4" y="18.0" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">y</text><line x1="116.8" y1="131.9" x2="116.8" y2="137.9" stroke="#0f172a" stroke-width="1.3"/><text x="116.8" y="149.9" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><line x1="155.2" y1="131.9" x2="155.2" y2="137.9" stroke="#0f172a" stroke-width="1.3"/><text x="155.2" y="149.9" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><line x1="193.6" y1="131.9" x2="193.6" y2="137.9" stroke="#0f172a" stroke-width="1.3"/><text x="193.6" y="149.9" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">3</text><line x1="232.0" y1="131.9" x2="232.0" y2="137.9" stroke="#0f172a" stroke-width="1.3"/><text x="232.0" y="149.9" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4</text><line x1="270.4" y1="131.9" x2="270.4" y2="137.9" stroke="#0f172a" stroke-width="1.3"/><text x="270.4" y="149.9" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">5</text><line x1="308.8" y1="131.9" x2="308.8" y2="137.9" stroke="#0f172a" stroke-width="1.3"/><text x="308.8" y="149.9" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">6</text><line x1="75.4" y1="194.4" x2="81.4" y2="194.4" stroke="#0f172a" stroke-width="1.3"/><text x="71.4" y="198.4" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">-20</text><line x1="75.4" y1="75.4" x2="81.4" y2="75.4" stroke="#0f172a" stroke-width="1.3"/><text x="71.4" y="79.4" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">20</text><line x1="75.4" y1="15.9" x2="81.4" y2="15.9" stroke="#0f172a" stroke-width="1.3"/><text x="71.4" y="19.9" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">40</text></svg>
:::

Sur la figure, A(2 ; 20) et B(4 ; 16) sont symétriques par rapport à I(3 ; 18) : leurs abscisses ont pour moyenne 3 et leurs ordonnées ont pour moyenne 18.

::: exemple L'axe de la maroquinerie : B(x) = −x² + 12x − 20 sur [0 ; 12]
1. Le domaine est symétrique par rapport à 6 : si x est dans [0 ; 12], alors 12 − x l'est aussi.
2. B(12 − x) = −(12 − x)² + 12(12 − x) − 20 = −144 + 24x − x² + 144 − 12x − 20.
3. On simplifie : B(12 − x) = −x² + 12x − 20 = B(x). La droite x = 6 est un axe de symétrie, et B(6) = 16 est le bénéfice maximal.

:::

::: exemple Un centre de symétrie : f(x) = x³ − 9x² + 24x sur ℝ
1. On pose x = 3 + t, pour décrire les deux côtés de 3. Alors f(3 + t) = (3 + t)³ − 9(3 + t)² + 24(3 + t) = t³ − 3t + 18 (les termes en t² s'annulent).
2. Donc f(3 − t) = −t³ + 3t + 18, et f(3 + t) + f(3 − t) = 36 = 2 × 18.
3. Ainsi f(6 − x) = 36 − f(x) : le point I(3 ; 18) est un centre de symétrie. On vérifie sur A et B : 20 + 16 = 36.

:::

::: exemple Une fonction périodique : f(x) = sin(πx) sur ℝ
1. Le domaine ℝ est symétrique par rapport à 0 et sin(−πx) = −sin(πx) : f est impaire, la courbe a pour centre de symétrie O.
2. f(x + 2) = sin(πx + 2π) = sin(πx) = f(x) pour tout x : f est périodique de période 2.
3. On étudie f sur [0 ; 1], l'imparité donne l'intervalle [−1 ; 1] de longueur 2, puis les translations de vecteur 2 i et −2 i, 4 i et −4 i, et ainsi de suite, complètent la courbe. Contrôle : f(0,5) = 1 et f(2,5) = sin(2,5π) = 1.

:::

::: piege Tester la parité sans regarder le domaine
Pour g(x) = x² + 1 définie sur [−2 ; 5], on écrit « g(−x) = x² + 1 = g(x), donc g est paire ». Cela tente parce que le calcul marche. Mais −5 n'est pas dans [−2 ; 5] alors que 5 y est : g(−5) n'existe pas. Le domaine n'est pas symétrique par rapport à 0, donc g n'est ni paire ni impaire : la courbe est un arc de parabole qui s'arrête à gauche à x = −2 et à droite à x = 5.
:::

::: propriete
- La parité permet d'étudier f sur [0 ; +∞[ seulement, puis de compléter la courbe par symétrie.
- Pour montrer un axe ou un centre, on vérifie d'abord que 2a − x reste dans le domaine, puis on compare f(2a − x) à f(x) (axe) ou à 2b − f(x) (centre).
- Pour une fonction polynôme de degré 3, le centre de symétrie est le point d'inflexion de la courbe.

Cas limite : une fonction impaire définie en 0 vérifie f(0) = −f(0), donc f(0) = 0 ; la courbe passe par l'origine.
:::

::: verifie
Montrer que I(2 ; 3) est un centre de symétrie de la courbe de f(x) = (3x − 2)/(x − 2) sur ℝ \ {2}.

---

Le domaine ℝ \ {2} est symétrique par rapport à 2 : 4 − x est différent de 2 exactement quand x l'est. Ensuite f(4 − x) = (3(4 − x) − 2)/((4 − x) − 2) = (10 − 3x)/(2 − x) = (3x − 10)/(x − 2). Par ailleurs 6 − f(x) = (6(x − 2) − (3x − 2))/(x − 2) = (3x − 10)/(x − 2). Les deux expressions sont égales : f(4 − x) = 6 − f(x), donc I(2 ; 3) est un centre de symétrie.
:::

::: retenir
Un axe x = a vérifie f(2a − x) = f(x) et un centre I(a ; b) vérifie f(2a − x) = 2b − f(x), toujours sur un domaine qui contient 2a − x en même temps que x ; la parité est le cas a = 0 (axe) ou I = O (centre) ; une fonction de période t se complète par des translations de vecteur t i.
:::

## 🔁 Translations et courbe de |f|

Le résultat net d'un atelier de tissage, en milliers de dinars, vaut f(x) = x² − 4x pour x milliers de mètres : négatif (une perte) entre 0 et 4, positif ensuite. Le directeur ajoute 3 milliers de dinars de subvention, puis décale sa production de 2 milliers de mètres.
Que deviennent la courbe, son sommet, et que devient-elle si on ne garde que la valeur absolue du résultat ?

::: definition
Dans un repère, la courbe de f étant C :

- la courbe de **x ↦ f(x) + k** est l'image de C par la **translation de vecteur k j** (vers le haut si k > 0) ;
- la courbe de **x ↦ f(x − k)** est l'image de C par la **translation de vecteur k i** (vers la droite si k > 0) ;
- la courbe de **|f|** coïncide avec C là où f(x) ≥ 0, et avec la symétrique de C par rapport à l'axe des abscisses là où f(x) < 0.
:::

::: figure La courbe de |f| (trait plein) replie vers le haut l'arc de la courbe de f (pointillés) qui passe sous l'axe des abscisses
<svg viewBox="0 0 340 250"><title>Courbe de f : x ↦ x² − 4x en pointillés et de |f| en trait plein : la partie sous l'axe des abscisses est repliée, avec un point anguleux en O(0 ; 0) et en A(4 ; 0)</title><polyline points="40.0,10.6 41.8,15.1 43.6,19.6 45.4,24.0 47.2,28.4 49.0,32.7 50.8,37.0 52.6,41.2 54.4,45.4 56.2,49.5 58.0,53.5 59.8,57.5 61.6,61.4 63.4,65.3 65.2,69.1 67.0,72.8 68.8,76.5 70.6,80.1 72.4,83.7 74.2,87.2 76.0,90.7 77.8,94.1 79.6,97.5 81.4,100.7 83.2,104.0 85.0,107.2 86.8,110.3 88.6,113.3 90.4,116.3 92.2,119.3 94.0,122.2 95.8,125.0 97.6,127.8 99.4,130.5 101.2,133.2 103.0,135.8 104.8,138.3 106.6,140.8 108.4,143.2 110.2,145.6 112.0,147.9 113.8,150.2 115.6,152.4 117.4,154.6 119.2,156.6 121.0,158.7 122.8,160.6 124.6,162.6 126.4,164.4 128.2,166.2 130.0,168.0 131.8,169.7 133.6,171.3 135.4,172.9 137.2,174.4 139.0,175.8 140.8,177.2 142.6,178.6 144.4,179.9 146.2,181.1 148.0,182.3 149.8,183.4 151.6,184.5 153.4,185.5 155.2,186.4 157.0,187.3 158.8,188.1 160.6,188.9 162.4,189.6 164.2,190.3 166.0,190.9 167.8,191.4 169.6,191.9 171.4,192.3 173.2,192.7 175.0,193.0 176.8,193.3 178.6,193.5 180.4,193.6 182.2,193.7 184.0,193.7 185.8,193.7 187.6,193.6 189.4,193.5 191.2,193.3 193.0,193.0 194.8,192.7 196.6,192.3 198.4,191.9 200.2,191.4 202.0,190.9 203.8,190.3 205.6,189.6 207.4,188.9 209.2,188.1 211.0,187.3 212.8,186.4 214.6,185.5 216.4,184.5 218.2,183.4 220.0,182.3 221.8,181.1 223.6,179.9 225.4,178.6 227.2,177.2 229.0,175.8 230.8,174.4 232.6,172.9 234.4,171.3 236.2,169.7 238.0,168.0 239.8,166.2 241.6,164.4 243.4,162.6 245.2,160.6 247.0,158.7 248.8,156.6 250.6,154.6 252.4,152.4 254.2,150.2 256.0,147.9 257.8,145.6 259.6,143.2 261.4,140.8 263.2,138.3 265.0,135.8 266.8,133.2 268.6,130.5 270.4,127.8 272.2,125.0 274.0,122.2 275.8,119.3 277.6,116.3 279.4,113.3 281.2,110.3 283.0,107.2 284.8,104.0 286.6,100.7 288.4,97.5 290.2,94.1 292.0,90.7 293.8,87.2 295.6,83.7 297.4,80.1 299.2,76.5 301.0,72.8 302.8,69.1 304.6,65.3 306.4,61.4 308.2,57.5 310.0,53.5 311.8,49.5 313.6,45.4 315.4,41.2 317.2,37.0 319.0,32.7 320.8,28.4 322.6,24.0 324.4,19.6 326.2,15.1 328.0,10.6" fill="none" stroke="#94a3b8" stroke-width="2" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="6 4"/><polyline points="40.0,10.6 41.0,13.0 41.9,15.4 42.9,17.8 43.8,20.2 44.8,22.6 45.8,24.9 46.7,27.3 47.7,29.6 48.6,31.9 49.6,34.2 50.6,36.4 51.5,38.7 52.5,40.9 53.4,43.2 54.4,45.4 55.4,47.6 56.3,49.7 57.3,51.9 58.2,54.0 59.2,56.2 60.2,58.3 61.1,60.4 62.1,62.4 63.0,64.5 64.0,66.5 65.0,68.6 65.9,70.6 66.9,72.6 67.8,74.5 68.8,76.5 69.8,78.5 70.7,80.4 71.7,82.3 72.6,84.2 73.6,86.1 74.6,87.9 75.5,89.8 76.5,91.6 77.4,93.4 78.4,95.2 79.4,97.0 80.3,98.8 81.3,100.5 82.2,102.3 83.2,104.0 84.2,105.7 85.1,107.4 86.1,109.0 87.0,110.7 88.0,112.3 89.0,113.9 89.9,115.5 90.9,117.1 91.8,118.7 92.8,120.3 93.8,121.8 94.7,123.3 95.7,124.8 96.6,126.3 97.6,127.8 98.6,129.3 99.5,130.7 100.5,132.1 101.4,133.5 102.4,134.9 103.4,136.3 104.3,136.7 105.3,135.4 106.2,134.1 107.2,132.8 108.2,131.5 109.1,130.2 110.1,128.9 111.0,127.7 112.0,126.5 113.0,125.2 113.9,124.0 114.9,122.9 115.8,121.7 116.8,120.6 117.8,119.4 118.7,118.3 119.7,117.2 120.6,116.1 121.6,115.1 122.6,114.0 123.5,113.0 124.5,112.0 125.4,111.0 126.4,110.0 127.4,109.0 128.3,108.1 129.3,107.1 130.2,106.2 131.2,105.3 132.2,104.4 133.1,103.5 134.1,102.7 135.0,101.8 136.0,101.0 137.0,100.2 137.9,99.4 138.9,98.6 139.8,97.9 140.8,97.2 141.8,96.4 142.7,95.7 143.7,95.0 144.6,94.4 145.6,93.7 146.6,93.0 147.5,92.4 148.5,91.8 149.4,91.2 150.4,90.6 151.4,90.1 152.3,89.5 153.3,89.0 154.2,88.5 155.2,88.0 156.2,87.5 157.1,87.0 158.1,86.6 159.0,86.2 160.0,85.8 161.0,85.4 161.9,85.0 162.9,84.6 163.8,84.3 164.8,83.9 165.8,83.6 166.7,83.3 167.7,83.0 168.6,82.8 169.6,82.5 170.6,82.3 171.5,82.0 172.5,81.8 173.4,81.7 174.4,81.5 175.4,81.3 176.3,81.2 177.3,81.1 178.2,81.0 179.2,80.9 180.2,80.8 181.1,80.7 182.1,80.7 183.0,80.7 184.0,80.7 185.0,80.7 185.9,80.7 186.9,80.7 187.8,80.8 188.8,80.9 189.8,81.0 190.7,81.1 191.7,81.2 192.6,81.3 193.6,81.5 194.6,81.7 195.5,81.8 196.5,82.0 197.4,82.3 198.4,82.5 199.4,82.8 200.3,83.0 201.3,83.3 202.2,83.6 203.2,83.9 204.2,84.3 205.1,84.6 206.1,85.0 207.0,85.4 208.0,85.8 209.0,86.2 209.9,86.6 210.9,87.0 211.8,87.5 212.8,88.0 213.8,88.5 214.7,89.0 215.7,89.5 216.6,90.1 217.6,90.6 218.6,91.2 219.5,91.8 220.5,92.4 221.4,93.0 222.4,93.7 223.4,94.4 224.3,95.0 225.3,95.7 226.2,96.4 227.2,97.2 228.2,97.9 229.1,98.6 230.1,99.4 231.0,100.2 232.0,101.0 233.0,101.8 233.9,102.7 234.9,103.5 235.8,104.4 236.8,105.3 237.8,106.2 238.7,107.1 239.7,108.1 240.6,109.0 241.6,110.0 242.6,111.0 243.5,112.0 244.5,113.0 245.4,114.0 246.4,115.1 247.4,116.1 248.3,117.2 249.3,118.3 250.2,119.4 251.2,120.6 252.2,121.7 253.1,122.9 254.1,124.0 255.0,125.2 256.0,126.5 257.0,127.7 257.9,128.9 258.9,130.2 259.8,131.5 260.8,132.8 261.8,134.1 262.7,135.4 263.7,136.7 264.6,136.3 265.6,134.9 266.6,133.5 267.5,132.1 268.5,130.7 269.4,129.3 270.4,127.8 271.4,126.3 272.3,124.8 273.3,123.3 274.2,121.8 275.2,120.3 276.2,118.7 277.1,117.1 278.1,115.5 279.0,113.9 280.0,112.3 281.0,110.7 281.9,109.0 282.9,107.4 283.8,105.7 284.8,104.0 285.8,102.3 286.7,100.5 287.7,98.8 288.6,97.0 289.6,95.2 290.6,93.4 291.5,91.6 292.5,89.8 293.4,87.9 294.4,86.1 295.4,84.2 296.3,82.3 297.3,80.4 298.2,78.5 299.2,76.5 300.2,74.5 301.1,72.6 302.1,70.6 303.0,68.6 304.0,66.5 305.0,64.5 305.9,62.4 306.9,60.4 307.8,58.3 308.8,56.2 309.8,54.0 310.7,51.9 311.7,49.7 312.6,47.6 313.6,45.4 314.6,43.2 315.5,40.9 316.5,38.7 317.4,36.4 318.4,34.2 319.4,31.9 320.3,29.6 321.3,27.3 322.2,24.9 323.2,22.6 324.2,20.2 325.1,17.8 326.1,15.4 327.0,13.0 328.0,10.6" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><circle cx="104.0" cy="137.2" r="4" fill="#0f172a" stroke="#0f172a" stroke-width="1"/><text x="96.0" y="153.2" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">O</text><circle cx="264.0" cy="137.2" r="4" fill="#0f172a" stroke="#0f172a" stroke-width="1"/><text x="273.0" y="153.2" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">A</text><text x="132.0" y="60.9" text-anchor="start" font-size="11" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">|f|</text><text x="168.0" y="202.2" text-anchor="start" font-size="11" font-weight="700" fill="#64748b" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">f (pointillés)</text><line x1="34" y1="137.2" x2="336" y2="137.2" stroke="#0f172a" stroke-width="1.6"/><line x1="104.0" y1="228" x2="104.0" y2="6" stroke="#0f172a" stroke-width="1.6"/><polygon points="336,137.2 329,133.7 329,140.7" fill="#0f172a"/><polygon points="104.0,6 100.5,13 107.5,13" fill="#0f172a"/><text x="332.0" y="130.2" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x</text><text x="112.0" y="18.0" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">y</text><line x1="64.0" y1="134.2" x2="64.0" y2="140.2" stroke="#0f172a" stroke-width="1.3"/><text x="64.0" y="152.2" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">-1</text><line x1="144.0" y1="134.2" x2="144.0" y2="140.2" stroke="#0f172a" stroke-width="1.3"/><text x="144.0" y="152.2" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><line x1="184.0" y1="134.2" x2="184.0" y2="140.2" stroke="#0f172a" stroke-width="1.3"/><text x="184.0" y="152.2" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><line x1="224.0" y1="134.2" x2="224.0" y2="140.2" stroke="#0f172a" stroke-width="1.3"/><text x="224.0" y="152.2" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">3</text><line x1="304.0" y1="134.2" x2="304.0" y2="140.2" stroke="#0f172a" stroke-width="1.3"/><text x="304.0" y="152.2" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">5</text><line x1="101.0" y1="193.7" x2="107.0" y2="193.7" stroke="#0f172a" stroke-width="1.3"/><text x="97.0" y="197.7" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">-4</text><line x1="101.0" y1="80.7" x2="107.0" y2="80.7" stroke="#0f172a" stroke-width="1.3"/><text x="97.0" y="84.7" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4</text><line x1="101.0" y1="24.1" x2="107.0" y2="24.1" stroke="#0f172a" stroke-width="1.3"/><text x="97.0" y="28.1" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">8</text></svg>
:::

La figure montre que |f| garde la même courbe hors de ]0 ; 4[ et remplace l'arc sous l'axe par son symétrique, ce qui crée un angle en O et en A.

::: exemple Subvention, décalage et valeur absolue : f(x) = x² − 4x
1. f′(x) = 2x − 4 s'annule en 2 et f(2) = −4 : le sommet de la courbe est S(2 ; −4).
2. g(x) = f(x) + 3 : le sommet devient S(2 ; −1), image de S par la translation de vecteur 3 j.
3. h(x) = f(x − 2) = x² − 8x + 12 : h(4) = −4 = f(2), donc le sommet devient (4 ; −4), image de S par la translation de vecteur 2 i, vers la droite.
4. |f|(x) = f(x) pour x ≤ 0 ou x ≥ 4, et −f(x) pour 0 ≤ x ≤ 4. En 0, le nombre dérivé à gauche est f′(0) = −4 et à droite il vaut −f′(0) = 4 : deux demi-tangentes de pentes différentes, donc |f| n'est pas dérivable en 0 (point anguleux). On le voit de même en 4.

:::

::: piege Déplacer la courbe de f(x − k) vers la gauche
Pour h(x) = f(x − 2), on écrit « le signe moins décale vers la gauche, de vecteur −2 i ». Cela tente parce qu'on soustrait 2 à x. Mais h(x) prend la valeur que f prenait deux unités plus tôt : h(4) = f(2). Le sommet passe de x = 2 à x = 4, vers la droite. Pour savoir où va un point, on cherche quel x donne le même résultat.
:::

::: propriete
- Ajouter k à f(x) déplace la courbe verticalement, remplacer x par x − k la déplace horizontalement ; les deux se composent, g(x) = f(x − k) + m est l'image de C par la translation de vecteur k i + m j.
- Les tangentes, les extremums et les asymptotes se déplacent avec la courbe.
- La courbe de |f| a un point anguleux là où f s'annule avec f′ ≠ 0 : les demi-tangentes ont des pentes opposées.

Cas limite : si f s'annule en x₀ sans changer de signe (f(x) = (x − 1)², f′(1) = 0), alors |f| = f près de x₀ et la courbe n'a pas de point anguleux.
:::

::: verifie
La courbe de f(x) = x² − 2x a pour sommet S(1 ; −1). Quel est le sommet de la courbe de g(x) = f(x − 4) + 3 ?

---

La courbe de g est l'image de celle de f par la translation de vecteur 4 i + 3 j : l'abscisse augmente de 4 (vers la droite) et l'ordonnée de 3. Le sommet est S′(5 ; 2). Contrôle : g(5) = f(1) + 3 = −1 + 3 = 2.
:::

::: retenir
f(x) + k translate la courbe de k j, f(x − k) la translate de k i (vers la droite si k > 0), et |f| replie vers le haut les arcs sous l'axe des abscisses, avec un point anguleux là où f s'annule en traversant l'axe.
:::

## 🗺️ Le plan d'étude d'une fonction : polynôme, rationnelle, racine

Reprenons f(x) = x³ − 9x² + 24x, dont on a montré plus haut le centre de symétrie I(3 ; 18) : on veut savoir où elle croît, où elle décroît, et quelle forme prend sa courbe.
Dans quel ordre mène-t-on une étude pour ne rien oublier ?

::: exemple Un polynôme de degré 3 : f(x) = x³ − 9x² + 24x sur ℝ
1. Domaine ℝ. Pas de parité : f(1) = 16 et f(−1) = −34, qui n'est ni 16 ni −16.
2. Limites : f tend vers +∞ en +∞ et vers −∞ en −∞ (terme dominant x³). Le quotient f(x)/x = x² − 9x + 24 tend vers +∞ : branches paraboliques de direction l'axe des ordonnées.
3. Dérivée : f′(x) = 3x² − 18x + 24 = 3(x − 2)(x − 4), positive hors de [2 ; 4], négative entre 2 et 4. On calcule f(2) = 20 et f(4) = 16.
4. Tableau :

| x | −∞ | | 2 | | 4 | | +∞ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| f′(x) | | + | 0 | − | 0 | + | |
| f(x) | −∞ | ↗ | 20 | ↘ | 16 | ↗ | +∞ |

5. Dérivée seconde : f″(x) = 6x − 18 s'annule en 3 en changeant de signe, et f(3) = 18 : point d'inflexion I(3 ; 18), centre de symétrie comme on l'a montré plus haut.

:::

::: exemple Une fraction rationnelle : f(x) = x²/(x − 2) sur ℝ \ {2}
1. Par division, x² = (x − 2)(x + 2) + 4, donc f(x) = x + 2 + 4/(x − 2). La droite y = x + 2 est asymptote oblique en +∞ et en −∞ ; la courbe est au-dessus pour x > 2 et en dessous pour x < 2.
2. En 2, le numérateur vaut 4 > 0 : f tend vers +∞ à droite et vers −∞ à gauche, donc x = 2 est asymptote verticale.
3. f′(x) = (2x(x − 2) − x²)/(x − 2)² = x(x − 4)/(x − 2)² : positive sur ]−∞ ; 0[ et ]4 ; +∞[, négative sur ]0 ; 2[ et ]2 ; 4[. On calcule f(0) = 0 et f(4) = 8.
4. Tableau : f croît de −∞ à 0 sur ]−∞ ; 0], décroît de 0 à −∞ sur [0 ; 2[, décroît de +∞ à 8 sur ]2 ; 4], croît de 8 à +∞ sur [4 ; +∞[.

:::

::: exemple Une racine carrée : f(x) = √(x² − 4x + 5)
1. x² − 4x + 5 = (x − 2)² + 1 > 0 : le domaine est ℝ. L'expression ne dépend que de (x − 2)², donc la droite x = 2 est un axe de symétrie.
2. f′(x) = (x − 2)/√(x² − 4x + 5) est négative avant 2 et positive après : f a un minimum f(2) = 1.
3. En +∞, f(x) − (x − 2) = ((x² − 4x + 5) − (x − 2)²)/(f(x) + x − 2) = 1/(f(x) + x − 2), qui tend vers 0 : y = x − 2 est asymptote oblique. Par symétrie par rapport à x = 2, la droite y = 2 − x est asymptote en −∞.

:::

::: piege Dire « décroissante » sur un intervalle qui contient la valeur interdite
Pour f(x) = x²/(x − 2), f′ est négative sur ]0 ; 2[ et sur ]2 ; 4[, d'où « f est décroissante sur [0 ; 4] ». Cela tente parce que le signe est le même des deux côtés de 2. Mais 2 n'est pas dans le domaine : f(1) = −1 et f(3) = 9, donc f(1) < f(3). La monotonie se lit sur chaque intervalle de définition, ici ]0 ; 2[ et ]2 ; 4], jamais sur leur réunion.
:::

::: methode Mener l'étude d'une fonction
1. Déterminer le domaine de définition et vérifier la dérivabilité.
2. Chercher parité, périodicité, axe ou centre de symétrie, pour réduire le domaine d'étude.
3. Calculer les limites aux bornes du domaine : asymptotes verticale, horizontale, oblique, branches paraboliques.
4. Calculer f′, la factoriser, étudier son signe sur chaque intervalle.
5. Dresser le tableau de variation avec les limites et les valeurs aux points où f′ s'annule.
6. Tracer la courbe : asymptotes, points particuliers, tangentes horizontales, puis la courbe.
:::

::: verifie
Étudier les variations de h(x) = x³ − 12x sur ℝ et préciser sa symétrie.

---

h est impaire (domaine ℝ et h(−x) = −h(x)) : le centre de symétrie est O. On a h′(x) = 3x² − 12 = 3(x − 2)(x + 2), positive hors de [−2 ; 2], négative entre −2 et 2. Les valeurs sont h(−2) = −8 + 24 = 16 et h(2) = 8 − 24 = −16. Donc h croît de −∞ à 16 sur ]−∞ ; −2], décroît de 16 à −16 sur [−2 ; 2], croît de −16 à +∞ sur [2 ; +∞[. Les valeurs 16 et −16 sont opposées, comme l'impose la symétrie par rapport à O.
:::

::: retenir
Une étude suit un enchaînement fixe : domaine, symétries, limites et asymptotes, dérivée et signe, tableau, tracé ; la monotonie se lit sur chaque intervalle de définition, jamais à cheval sur une valeur interdite.
:::

## 💰 Coût moyen minimal et bénéfice maximal

Une conserverie fabrique x tonnes de sardines (0 ≤ x ≤ 20) pour un coût total C(x) = x³ − 24x² + 200x milliers de dinars, et vend chaque tonne 116 milliers de dinars.
Quelle production donne le bénéfice maximal, et à quel prix minimal peut-elle vendre sans perdre d'argent ?

::: definition
Pour un prix unitaire constant p, la **recette** est R(x) = px et le **bénéfice** est B(x) = R(x) − C(x). Le **coût marginal** est Cm = C′ et le **coût moyen** est CM(x) = C(x)/x pour x > 0. On a donc B′(x) = p − Cm(x).
:::

::: exemple Le bénéfice maximal de la conserverie
1. B(x) = 116x − (x³ − 24x² + 200x) = −x³ + 24x² − 84x. Sa dérivée est B′(x) = −3x² + 48x − 84 = −3(x − 2)(x − 14).
2. B′ est négative sur [0 ; 2], positive sur [2 ; 14], négative sur [14 ; 20]. Valeurs : B(0) = 0, B(2) = −80, B(14) = 784, B(20) = −80.
3. Le maximum est B(14) = 784 : produire 14 tonnes rapporte 784 milliers de dinars, le plus grand bénéfice sur [0 ; 20]. Contrôle : Cm(14) = 588 − 672 + 200 = 116 = p.
4. B(x) = −x(x² − 24x + 84) est positif entre 12 − √60 et 12 + √60, soit environ entre 4,25 et 19,75 tonnes : hors de cet intervalle, l'entreprise perd de l'argent.

:::

::: exemple Le coût moyen minimal : CM(x) = C(x)/x
1. CM(x) = x² − 24x + 200 pour x > 0, donc CM′(x) = 2x − 24, négative avant 12 et positive après.
2. Le minimum est CM(12) = 144 − 288 + 200 = 56 milliers de dinars par tonne.
3. Contrôle : Cm(12) = 432 − 576 + 200 = 56, égal au coût moyen au minimum. À 56 milliers de dinars la tonne, le bénéfice maximal est nul : c'est le prix de vente le plus bas qui évite la perte.

:::

::: piege Annuler C′ pour trouver le bénéfice maximal
On écrit « on cherche un maximum, donc je résous C′(x) = 0 ». Cela tente parce que « dériver et annuler » est le réflexe du chapitre précédent. Mais C est le coût, pas le bénéfice : ici C′(x) = 3x² − 48x + 200 ne s'annule jamais (son discriminant 2 304 − 2 400 est négatif). C'est B′(x) = p − C′(x) qu'il faut annuler, c'est-à-dire résoudre Cm(x) = p.
:::

::: propriete
- Le bénéfice est extremal là où le coût marginal égale le prix, Cm(x) = p, à condition que B′ change de signe ; on compare ensuite aux valeurs en 0 et à l'autre extrémité du domaine.
- Le coût moyen est minimal là où il égale le coût marginal.
- Pour trouver un extremum sur un domaine borné, on compare toujours le candidat aux valeurs aux bornes.

Cas limite : l'équation Cm(x) = p peut avoir deux solutions ; ici x = 2 donne un minimum local du bénéfice (une perte de 80), pas un maximum.
:::

::: verifie
Une verrerie produit x tonnes (0 ≤ x ≤ 8) pour un coût C(x) = x³ − 9x² + 30x milliers de dinars ; la tonne se vend 30 milliers de dinars. Quelle production donne le bénéfice maximal ?

---

B(x) = 30x − C(x) = −x³ + 9x² et B′(x) = −3x² + 18x = −3x(x − 6), positive sur ]0 ; 6[ et négative sur ]6 ; 8]. Le maximum est donc en x = 6 : B(6) = −216 + 324 = 108 milliers de dinars. On compare à la borne : B(8) = −512 + 576 = 64 < 108.
:::

::: retenir
Le bénéfice B = px − C est maximal là où le coût marginal égale le prix, le coût moyen est minimal là où il égale le coût marginal, et un extremum sur un domaine borné se confirme en comparant aux bornes.
:::

## ⚖️ Offre, demande, prix d'équilibre, satisfaction et envie

Sur un marché d'olives, x désigne le prix du kilo en dinars. Les producteurs offrent O(x) = 2x milliers de kilos et les consommateurs demandent D(x) = 120/(x + 4) milliers de kilos : plus le prix monte, plus on offre et moins on demande.
À quel prix les deux quantités sont-elles égales ?

::: definition
La **fonction d'offre** O donne la quantité que les producteurs proposent à un prix x, et la **fonction de demande** D la quantité que les consommateurs veulent à ce prix. Le **prix d'équilibre** x₀ est le prix où O(x₀) = D(x₀), et la **quantité d'équilibre** est la valeur commune de O(x₀) et D(x₀).
:::

::: figure Les courbes d'offre (croissante) et de demande (décroissante) se coupent au point d'équilibre E(6 ; 12)
<svg viewBox="0 0 340 250"><title>Courbes de l'offre O(x) = 2x et de la demande D(x) = 120/(x + 4) en fonction du prix x en dinars, quantités en milliers : elles se coupent au point d'équilibre E(6 ; 12)</title><polyline points="44.0,222.0 48.7,218.8 53.5,215.6 58.2,212.4 62.9,209.2 67.7,205.9 72.4,202.7 77.1,199.5 81.9,196.3 86.6,193.1 91.3,189.9 96.1,186.7 100.8,183.5 105.5,180.2 110.3,177.0 115.0,173.8 119.7,170.6 124.5,167.4 129.2,164.2 133.9,161.0 138.7,157.8 143.4,154.5 148.1,151.3 152.9,148.1 157.6,144.9 162.3,141.7 167.1,138.5 171.8,135.3 176.5,132.1 181.3,128.8 186.0,125.6 190.7,122.4 195.5,119.2 200.2,116.0 204.9,112.8 209.7,109.6 214.4,106.4 219.1,103.2 223.9,99.9 228.6,96.7 233.3,93.5 238.1,90.3 242.8,87.1 247.5,83.9 252.3,80.7 257.0,77.5 261.7,74.2 266.5,71.0 271.2,67.8 275.9,64.6 280.7,61.4 285.4,58.2 290.1,55.0 294.9,51.8 299.6,48.5 304.3,45.3 309.1,42.1 313.8,38.9 318.5,35.7 323.3,32.5 328.0,29.3" fill="none" stroke="#b45309" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><polyline points="86.6,11.8 89.0,14.9 91.3,17.9 93.7,20.9 96.1,23.8 98.4,26.6 100.8,29.3 103.2,31.9 105.5,34.5 107.9,37.0 110.3,39.4 112.6,41.8 115.0,44.1 117.4,46.3 119.7,48.5 122.1,50.7 124.5,52.8 126.8,54.8 129.2,56.8 131.6,58.7 133.9,60.6 136.3,62.5 138.7,64.3 141.0,66.1 143.4,67.8 145.8,69.5 148.1,71.2 150.5,72.8 152.9,74.4 155.2,75.9 157.6,77.5 160.0,78.9 162.3,80.4 164.7,81.8 167.1,83.2 169.4,84.6 171.8,86.0 174.2,87.3 176.5,88.6 178.9,89.8 181.3,91.1 183.6,92.3 186.0,93.5 188.4,94.7 190.7,95.9 193.1,97.0 195.5,98.1 197.8,99.2 200.2,100.3 202.6,101.3 204.9,102.4 207.3,103.4 209.7,104.4 212.0,105.4 214.4,106.4 216.8,107.3 219.1,108.3 221.5,109.2 223.9,110.1 226.2,111.0 228.6,111.9 231.0,112.7 233.3,113.6 235.7,114.4 238.1,115.3 240.4,116.1 242.8,116.9 245.2,117.7 247.5,118.4 249.9,119.2 252.3,120.0 254.6,120.7 257.0,121.4 259.4,122.2 261.7,122.9 264.1,123.6 266.5,124.3 268.8,125.0 271.2,125.6 273.6,126.3 275.9,127.0 278.3,127.6 280.7,128.2 283.0,128.9 285.4,129.5 287.8,130.1 290.1,130.7 292.5,131.3 294.9,131.9 297.2,132.5 299.6,133.0 302.0,133.6 304.3,134.2 306.7,134.7 309.1,135.3 311.4,135.8 313.8,136.3 316.2,136.9 318.5,137.4 320.9,137.9 323.3,138.4 325.6,138.9 328.0,139.4" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><line x1="214.4" y1="222.0" x2="214.4" y2="106.4" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="4 3"/><line x1="44.0" y1="106.4" x2="214.4" y2="106.4" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="4 3"/><circle cx="214.4" cy="106.4" r="4" fill="#0f172a" stroke="#0f172a" stroke-width="1"/><text x="223.4" y="97.4" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">E(6 ; 12)</text><line x1="38" y1="222.0" x2="336" y2="222.0" stroke="#0f172a" stroke-width="1.6"/><line x1="44.0" y1="228" x2="44.0" y2="6" stroke="#0f172a" stroke-width="1.6"/><polygon points="336,222.0 329,218.5 329,225.5" fill="#0f172a"/><polygon points="44.0,6 40.5,13 47.5,13" fill="#0f172a"/><text x="332.0" y="215.0" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">prix</text><text x="52.0" y="18.0" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">quantité</text><line x1="100.8" y1="219.0" x2="100.8" y2="225.0" stroke="#0f172a" stroke-width="1.3"/><text x="100.8" y="237.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><line x1="157.6" y1="219.0" x2="157.6" y2="225.0" stroke="#0f172a" stroke-width="1.3"/><text x="157.6" y="237.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4</text><line x1="214.4" y1="219.0" x2="214.4" y2="225.0" stroke="#0f172a" stroke-width="1.3"/><text x="214.4" y="237.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">6</text><line x1="271.2" y1="219.0" x2="271.2" y2="225.0" stroke="#0f172a" stroke-width="1.3"/><text x="271.2" y="237.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">8</text><line x1="328.0" y1="219.0" x2="328.0" y2="225.0" stroke="#0f172a" stroke-width="1.3"/><text x="328.0" y="237.0" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">10</text><line x1="41.0" y1="173.8" x2="47.0" y2="173.8" stroke="#0f172a" stroke-width="1.3"/><text x="37.0" y="177.8" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">5</text><line x1="41.0" y1="125.6" x2="47.0" y2="125.6" stroke="#0f172a" stroke-width="1.3"/><text x="37.0" y="129.6" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">10</text><line x1="41.0" y1="106.4" x2="47.0" y2="106.4" stroke="#0f172a" stroke-width="1.3"/><text x="37.0" y="110.4" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">12</text><line x1="41.0" y1="77.5" x2="47.0" y2="77.5" stroke="#0f172a" stroke-width="1.3"/><text x="37.0" y="81.5" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">15</text><line x1="41.0" y1="29.3" x2="47.0" y2="29.3" stroke="#0f172a" stroke-width="1.3"/><text x="37.0" y="33.3" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">20</text><text x="276.9" y="58.2" text-anchor="start" font-size="11" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">offre</text><text x="254.2" y="171.9" text-anchor="start" font-size="11" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">demande</text></svg>
:::

Le point E est le seul où les deux courbes se rencontrent : à gauche, la demande dépasse l'offre ; à droite, c'est l'inverse.

::: exemple Le marché d'olives : O(x) = 2x et D(x) = 120/(x + 4)
1. On pose p(x) = O(x) − D(x) = 2x − 120/(x + 4). Sa dérivée p′(x) = 2 + 120/(x + 4)² est strictement positive : p est strictement croissante sur [0 ; +∞[.
2. p(0) = −30 < 0 et p(10) = 20 − 120/14 > 0 : p est continue, croissante, et change de signe, donc p s'annule exactement une fois.
3. On résout 2x(x + 4) = 120, soit x² + 4x − 60 = 0, donc (x − 6)(x + 10) = 0 et x₀ = 6 (x + 10 = 0 donnerait −10, hors du domaine).
4. Quantité d'équilibre : O(6) = 12 et D(6) = 120/10 = 12, soit 12 000 kilos à 6 dinars le kilo.

:::

En économie, on appelle aussi **fonction de satisfaction** une fonction S à valeurs entre 0 et 100, et **fonction envie** sa dérivée E = S′ : il y a **envie** quand E > 0 et **rejet** quand E < 0.

::: exemple La satisfaction d'un salarié : E(x) = 60/(x + 2)² et S(0) = 0
1. x est le salaire annuel en milliers de dinars (x ≥ 0). On cherche S telle que S′(x) = 60/(x + 2)² : les primitives de E sont S(x) = −60/(x + 2) + k ; S(0) = 0 donne −30 + k = 0, soit k = 30 : S(x) = 30 − 60/(x + 2).
2. Contrôle : S′(x) = 60/(x + 2)² = E(x) et S(0) = 30 − 30 = 0.
3. La satisfaction vaut au moins 24 quand 60/(x + 2) ≤ 6, c'est-à-dire x + 2 ≥ 10 : à partir de x = 8, soit 8 000 dinars par an. Elle reste inférieure à 30.

:::

::: piege Confondre la satisfaction et l'envie
On écrit « E(x) = 60/(x + 2)² diminue quand x augmente, donc la satisfaction diminue ». Cela tente parce que la formule de E s'effondre. Mais E décrit la vitesse de variation de S, pas S elle-même : E reste positive, donc S croît toujours, de plus en plus lentement. Test : S(0) = 0, S(8) = 24, S(48) = 30 − 1,2 = 28,8.
:::

::: propriete
- Si p = O − D est continue et strictement monotone sur un intervalle, et change de signe, l'équation p(x) = 0 a exactement une solution : c'est le prix d'équilibre.
- Si E > 0 sur un intervalle, S y est croissante (envie) ; si E < 0, S y est décroissante (rejet) ; la satisfaction est maximale là où E s'annule en passant du positif au négatif.
- Si la demande augmente à chaque prix, la courbe de demande se déplace vers le haut ; le prix et la quantité d'équilibre augmentent.

Cas limite : quand p change de signe sans être monotone, l'équilibre peut ne pas être unique ; on le vérifie, on ne le suppose pas.
:::

::: verifie
Une coopérative a pour offre O(x) = 3x et pour demande D(x) = 36/(x + 1), en milliers de pièces, avec x le prix en dinars. Trouver le prix et la quantité d'équilibre.

---

O(x) = D(x) donne 3x(x + 1) = 36, soit x² + x − 12 = 0, donc (x − 3)(x + 4) = 0 et x₀ = 3 (−4 est négatif). La quantité d'équilibre est O(3) = 9, et D(3) = 36/4 = 9 : 9 000 pièces à 3 dinars. L'unicité vient de p = O − D de dérivée 3 + 36/(x + 1)² > 0.
:::

::: retenir
Le prix d'équilibre est l'unique solution de O(x) = D(x), prouvée par la croissance stricte de O − D ; l'envie est la dérivée de la satisfaction, positive quand S croît, négative quand elle décroît.
:::

> 🏆 Tu sais maintenant lire une courbe de bout en bout : asymptotes, directions, symétries, translations, tableau de variation, optimum et équilibre. Prochaine étape : le logarithme népérien et les exponentielles, de nouvelles fonctions à étudier avec les mêmes outils.
