# ⚔️ Géométrie du triangle — bissectrices, Héron, triangles isométriques et semblables, relations métriques

> 💡 «Un triangle se laisse deviner par très peu de choses : l'art est de savoir lesquelles suffisent, et ce qu'elles permettent de calculer ensuite.»

Le chapitre « Trigonométrie et mesure de grandeurs » a donné trois outils pour un triangle quelconque : la loi du sinus, l'aire S = ½ bc sin Â et le théorème d'El-Kashi. Ce chapitre les met au travail sur d'autres questions : comment une bissectrice partage un côté, comment trouver l'aire sans angle ni hauteur, quand deux triangles sont identiques ou de même forme, et ce que cache la hauteur d'un triangle rectangle.
Six étapes t'y conduisent : le théorème des bissectrices, la formule de Héron, les triangles isométriques, les triangles semblables, leurs critères, puis les relations métriques du triangle rectangle. La loi du sinus et les angles supplémentaires (sin(π − x) = sin x) servent dès la première étape.

## 📐 Les bissectrices : où le chemin coupe la clôture

Un terrain triangulaire ABC est clôturé : AB = 40 m, AC = 60 m et BC = 50 m. Depuis le coin A, un chemin rectiligne rejoint la clôture [BC] en un point I, en faisant des angles égaux avec [AB] et avec [AC] : c'est la bissectrice de l'angle Â.
Où tombe I sur [BC] : combien valent IB et IC ?

::: figure Le terrain dessiné à l'échelle : la bissectrice (AI) coupe l'angle Â en deux angles égaux (mêmes arcs), mais le point I n'est pas au milieu de [BC]
<svg viewBox="10 20 249 216"><path d="M58.9 50 L40 200 L229 200 Z" fill="#0f6e56" opacity="0.12"/><path d="M58.9 50 L40 200 L229 200 Z" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M58.9 50 L115.6 200" fill="none" stroke="#0f6e56" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/><path d="M56.1 71.8 A22 22 0 0 0 66.7 70.6" fill="none" stroke="#b45309" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M55.5 76.8 A27 27 0 0 0 68.4 75.3" fill="none" stroke="#b45309" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M66.7 70.6 A22 22 0 0 0 75.4 64.6" fill="none" stroke="#b45309" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M68.4 75.3 A27 27 0 0 0 79.1 67.9" fill="none" stroke="#b45309" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><circle cx="58.9" cy="50" r="4" fill="#0f172a"/><circle cx="40" cy="200" r="4" fill="#0f172a"/><circle cx="229" cy="200" r="4" fill="#0f172a"/><circle cx="115.6" cy="200" r="4.5" fill="#0f6e56"/><g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.6" stroke-linejoin="round"><text x="52.1" y="41.6" text-anchor="middle" font-size="14" fill="#0f172a">A</text><text x="27.8" y="213.8" text-anchor="middle" font-size="14" fill="#0f172a">B</text><text x="242.8" y="210.8" text-anchor="middle" font-size="14" fill="#0f172a">C</text><text x="128.6" y="191" text-anchor="middle" font-size="14" fill="#0f6e56">I</text><text x="36.5" y="124.6" text-anchor="middle" font-size="13" fill="#0f6e56">40</text><text x="155.3" y="121.8" text-anchor="middle" font-size="13" fill="#0f6e56">60</text><text x="134.5" y="222" text-anchor="middle" font-size="13" fill="#0f6e56">50</text></g></svg>
:::

Sur la figure, les angles BÂI et IÂC portent les mêmes arcs : ils sont égaux. Les longueurs 40 et 60 sont celles des côtés AB et AC, et les segments à trouver sont IB et IC.

::: exemple Le chemin du terrain : IB et IC avec AB = 40 m, AC = 60 m et BC = 50 m

1. IB / IC = AB / AC = 40/60 = 2/3, d'après le théorème des bissectrices : chaque segment est comparé au côté qui a la même extrémité que lui (IB avec AB, IC avec AC).
2. On pose IB = 2k et IC = 3k, car le rapport IB / IC vaut 2/3. Comme I est sur [BC], IB + IC = 50, donc 5k = 50 et k = 10.
3. IB = 20 m et IC = 30 m. Contrôle : 20/30 = 2/3 = 40/60, et I est plus près de B, extrémité du plus petit côté AB.

:::

::: piege Prendre le milieu de [BC] parce que la bissectrice « coupe en deux »
Pour le terrain, un élève écrit IB = IC = 25 m. Cela tente parce que le mot bissectrice dit « couper en deux » et que la médiane, elle, coupe bien [BC] en deux.
Mais la bissectrice coupe l'angle Â en deux, pas le côté : IB / IC = AB / AC = 2/3 n'est pas égal à 1, donc I n'est pas le milieu. La bonne réponse est IB = 20 m et IC = 30 m ; le milieu n'apparaît que si AB = AC.
:::

::: propriete
Dans un triangle ABC, la bissectrice intérieure de l'angle Â coupe [BC] en I. Alors :

$$ IB / IC = AB / AC $$

Raison : dans les triangles AIB et AIC, la loi du sinus donne IB / sin(Â/2) = AB / sin AÎB et IC / sin(Â/2) = AC / sin AÎC. Les angles AÎB et AÎC sont supplémentaires, donc de même sinus ; en divisant, IB / IC = AB / AC.
Bissectrice extérieure : si AB ≠ AC, la bissectrice de l'angle extérieur en A coupe la droite (BC) en un point J extérieur à [BC], au-delà de B si AB < AC, et JB / JC = AB / AC. Raison analogue : les angles en J sont les mêmes, et les angles en A, (π − Â)/2 et (π + Â)/2, sont supplémentaires. Pour le terrain : JB / JC = 2/3 avec JC = JB + 50, donc 3 JB = 2 (JB + 50), JB = 100 m et JC = 150 m.
Cas limite : si AB = AC, I est le milieu de [BC] et la bissectrice extérieure est parallèle à (BC) : elle ne coupe pas cette droite.
:::

::: figure La bissectrice extérieure (AJ) du même terrain (les segments sont dessinés à l'échelle) : elle coupe l'angle extérieur en A en deux angles égaux (mêmes arcs) et rencontre la droite (BC) en J, au-delà de B ; le trait pointillé prolonge [CA] au-delà de A
<svg viewBox="10 66 330 170"><path d="M229 128.6 L220 200 L310 200 Z" fill="#0f6e56" opacity="0.12"/><path d="M229 128.6 L220 200 L310 200 Z" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M40 200 L229 128.6" fill="none" stroke="#0f6e56" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/><path d="M40 200 L220 200" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M229 128.6 L192.6 96.4" fill="none" stroke="#94a3b8" stroke-width="1.8" stroke-dasharray="5 4" stroke-linecap="round" stroke-linejoin="round"/><path d="M211 112.7 A24 24 0 0 0 206.6 137" fill="none" stroke="#b45309" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M207.2 109.4 A29 29 0 0 0 201.9 138.8" fill="none" stroke="#b45309" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M206.6 137 A24 24 0 0 0 226 152.4" fill="none" stroke="#b45309" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M201.9 138.8 A29 29 0 0 0 225.4 157.3" fill="none" stroke="#b45309" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><circle cx="229" cy="128.6" r="4" fill="#0f172a"/><circle cx="220" cy="200" r="4" fill="#0f172a"/><circle cx="310" cy="200" r="4" fill="#0f172a"/><circle cx="40" cy="200" r="4.5" fill="#0f6e56"/><g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.6" stroke-linejoin="round"><text x="244" y="122.6" text-anchor="middle" font-size="14" fill="#0f172a">A</text><text x="222" y="222" text-anchor="middle" font-size="14" fill="#0f172a">B</text><text x="323.8" y="210.8" text-anchor="middle" font-size="14" fill="#0f172a">C</text><text x="40" y="222" text-anchor="middle" font-size="14" fill="#0f6e56">J</text></g></svg>
:::

Sur la figure, J est du côté de B, extrémité du plus petit côté AB : JB = 100 m est plus petit que JC = 150 m, et JC − JB = BC = 50 m.

::: verifie
Dans un triangle ABC, AB = 9, AC = 12 et BC = 14. La bissectrice de l'angle Â coupe [BC] en I. Calculer IB.

---

IB / IC = AB / AC = 9/12 = 3/4. On pose IB = 3k et IC = 4k, avec IB + IC = BC = 14, donc 7k = 14 et k = 2 : IB = 6 (et IC = 8). On a comparé chaque segment au côté qui a la même extrémité : IB avec AB.
:::

::: retenir
La bissectrice intérieure de Â coupe [BC] en I avec IB / IC = AB / AC : I n'est le milieu que si AB = AC, et la bissectrice extérieure suit la même proportion à l'extérieur de [BC].
:::

## 🌿 La formule de Héron : l'aire avec les trois côtés seulement

Un jardin triangulaire a des côtés de 20 m, 13 m et 11 m. Personne n'a mesuré une hauteur ni un angle. Avec les outils précédents, il faudrait calculer un angle par El-Kashi, puis son sinus, puis l'aire ½ bc sin Â.
Existe-t-il un chemin direct, qui ne demande que les trois côtés ?

::: definition
Pour un triangle de côtés a = BC, b = CA et c = AB, on appelle **demi-périmètre** le nombre p = (a + b + c) / 2. La **formule de Héron** donne l'aire S du triangle :

$$ S = √(p (p − a)(p − b)(p − c)) $$
:::

::: figure Le jardin : trois côtés a = 20, b = 13 et c = 11 (en mètres), et aucune hauteur ni aucun angle
<svg viewBox="5 113 330 147"><path d="M155.6 140.8 L50 220 L290 220 Z" fill="#0f6e56" opacity="0.12"/><path d="M155.6 140.8 L50 220 L290 220 Z" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><circle cx="155.6" cy="140.8" r="4" fill="#0f172a"/><circle cx="50" cy="220" r="4" fill="#0f172a"/><circle cx="290" cy="220" r="4" fill="#0f172a"/><g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.6" stroke-linejoin="round"><text x="152.9" y="131" text-anchor="middle" font-size="14" fill="#0f172a">A</text><text x="35.4" y="228.4" text-anchor="middle" font-size="14" fill="#0f172a">B</text><text x="304.7" y="228.1" text-anchor="middle" font-size="14" fill="#0f172a">C</text><text x="77.4" y="180" text-anchor="middle" font-size="13" fill="#0f6e56">c = 11</text><text x="248.1" y="179.6" text-anchor="middle" font-size="13" fill="#0f6e56">b = 13</text><text x="170" y="246" text-anchor="middle" font-size="13" fill="#0f6e56">a = 20</text></g></svg>
:::

Sur la figure, a, b et c sont les trois côtés du triangle ; ce sont les seuls nombres qui entrent dans p, p − a, p − b et p − c.

::: exemple Le jardin de 20 m, 13 m et 11 m

1. p = (20 + 13 + 11) / 2 = 22, car p est la moitié du périmètre.
2. p − a = 22 − 20 = 2, p − b = 22 − 13 = 9 et p − c = 22 − 11 = 11, car on retire chaque côté à p.
3. S = √(22 × 2 × 9 × 11) = √4356 = 66, car 66² = 4356.
4. L'aire du jardin est 66 m².

:::

::: exemple Les côtés 7, 8 et 9, sans contexte

1. p = (7 + 8 + 9) / 2 = 12, puis p − 7 = 5, p − 8 = 4 et p − 9 = 3.
2. S = √(12 × 5 × 4 × 3) = √720 = √(144 × 5) = 12√5, en extrayant le carré parfait 144.
3. S = 12√5, soit environ 26,83.

:::

::: piege Prendre le périmètre entier pour p
Pour le jardin, un élève écrit p = 20 + 13 + 11 = 44 et S = √(44 × 24 × 31 × 33), soit environ 1039,4 m². Cela tente parce que la lettre p fait penser à « périmètre ».
Mais p est le demi-périmètre : p = 22 et S = 66 m². Un contrôle l'aurait signalé : comme S = ½ ab sin Ĉ avec sin Ĉ ≤ 1, l'aire ne dépasse pas ½ × 20 × 13 = 130, et 1039,4 est impossible.
:::

::: propriete
La formule de Héron est une conséquence d'El-Kashi et de S = ½ ab sin Ĉ.
Raison : 2ab cos Ĉ = a² + b² − c², donc 4a²b² sin²Ĉ = 4a²b² − (a² + b² − c²)² = (c² − (a − b)²)((a + b)² − c²) = (a + b + c)(a + b − c)(b + c − a)(c + a − b). Ces quatre facteurs valent 2p, 2(p − c), 2(p − a) et 2(p − b), et 4a²b² sin²Ĉ = 16 S² : on obtient S² = p (p − a)(p − b)(p − c).
Cas limite : si c = a + b, alors p − c = 0 et S = 0 : le triangle est aplati. Si c > a + b, p − c est négatif et la racine n'existe pas : aucun triangle n'a ces côtés.
:::

::: verifie
Calculer l'aire d'un triangle de côtés 4, 13 et 15.

---

p = (4 + 13 + 15) / 2 = 16, puis p − 4 = 12, p − 13 = 3 et p − 15 = 1. Donc S = √(16 × 12 × 3 × 1) = √576 = 24. On a pris p = 16, le demi-périmètre, et non le périmètre 32.
:::

::: retenir
S = √(p (p − a)(p − b)(p − c)) avec p = (a + b + c) / 2 : les trois côtés suffisent, et p − c = 0 signale un triangle aplati.
:::

## 🔁 Triangles isométriques : combien de mesures pour être sûr ?

Dans un atelier, on découpe deux pièces triangulaires de charpente, ABC et A′B′C′, d'après le même plan. Le contrôleur n'a pas le temps de mesurer les trois côtés de chaque pièce : il mesure quelques longueurs et quelques angles.
Lesquelles lui suffisent pour affirmer que les côtés de l'une sont égaux à ceux de l'autre ?

::: definition
Deux triangles ABC et A′B′C′ sont **isométriques** si leurs côtés sont deux à deux égaux : AB = A′B′, AC = A′C′ et BC = B′C′.
:::

::: figure Deux triangles isométriques (valeurs d'illustration : AB = A′B′ = 5, AC = A′C′ = 6, Â = Â′ = 60°) : les traits identiques marquent les côtés égaux, et l'arc marque l'angle égal compris entre les côtés à un et à deux traits
<svg viewBox="0 55 361 211"><path d="M30 230 L140 230 L96 115.7 Z" fill="#0f6e56" opacity="0.12"/><path d="M30 230 L140 230 L96 115.7 Z" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M85 234 L85 226" fill="none" stroke="#0f6e56" stroke-width="2" stroke-linecap="round"/><path d="M65.2 177 L58.3 173" fill="none" stroke="#0f6e56" stroke-width="2" stroke-linecap="round"/><path d="M67.7 172.7 L60.8 168.7" fill="none" stroke="#0f6e56" stroke-width="2" stroke-linecap="round"/><path d="M123.5 176.1 L116.1 178.9" fill="none" stroke="#0f6e56" stroke-width="2" stroke-linecap="round"/><path d="M121.7 171.4 L114.3 174.3" fill="none" stroke="#0f6e56" stroke-width="2" stroke-linecap="round"/><path d="M119.9 166.7 L112.5 169.6" fill="none" stroke="#0f6e56" stroke-width="2" stroke-linecap="round"/><path d="M52 230 A22 22 0 0 0 41 210.9" fill="none" stroke="#b45309" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><circle cx="30" cy="230" r="4" fill="#0f172a"/><circle cx="140" cy="230" r="4" fill="#0f172a"/><circle cx="96" cy="115.7" r="4" fill="#0f172a"/><path d="M219.2 216.8 L325.5 188.3 L253.4 89.3 Z" fill="#0f6e56" opacity="0.12"/><path d="M219.2 216.8 L325.5 188.3 L253.4 89.3 Z" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M273.4 206.4 L271.3 198.7" fill="none" stroke="#0f6e56" stroke-width="2" stroke-linecap="round"/><path d="M239.5 156.5 L231.8 154.4" fill="none" stroke="#0f6e56" stroke-width="2" stroke-linecap="round"/><path d="M240.8 151.7 L233.1 149.6" fill="none" stroke="#0f6e56" stroke-width="2" stroke-linecap="round"/><path d="M295.6 140.5 L289.1 145.2" fill="none" stroke="#0f6e56" stroke-width="2" stroke-linecap="round"/><path d="M292.6 136.5 L286.2 141.2" fill="none" stroke="#0f6e56" stroke-width="2" stroke-linecap="round"/><path d="M289.7 132.4 L283.2 137.1" fill="none" stroke="#0f6e56" stroke-width="2" stroke-linecap="round"/><path d="M240.5 211.1 A22 22 0 0 0 224.9 195.5" fill="none" stroke="#b45309" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><circle cx="219.2" cy="216.8" r="4" fill="#0f172a"/><circle cx="325.5" cy="188.3" r="4" fill="#0f172a"/><circle cx="253.4" cy="89.3" r="4" fill="#0f172a"/><g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.6" stroke-linejoin="round"><text x="17.4" y="243.2" text-anchor="middle" font-size="14" fill="#0f172a">A</text><text x="152" y="243.9" text-anchor="middle" font-size="14" fill="#0f172a">B</text><text x="97.4" y="105.8" text-anchor="middle" font-size="14" fill="#0f172a">C</text><text x="209.2" y="232.9" text-anchor="middle" font-size="14" fill="#0f172a">A′</text><text x="339.4" y="198.8" text-anchor="middle" font-size="14" fill="#0f172a">B′</text><text x="250.9" y="79.5" text-anchor="middle" font-size="14" fill="#0f172a">C′</text></g></svg>
:::

Sur la figure, un trait marque AB et A′B′, deux traits marquent AC et A′C′, trois traits marquent BC et B′C′ : ce sont les trois paires de côtés égaux de la définition. L'arc en A et en A′ marque l'angle compris entre les côtés d'un et de deux traits.

::: exemple Les deux pièces : AB = A′B′ = 5, AC = A′C′ = 6 et Â = Â′ = 60°

1. Dans ABC, l'angle Â est compris entre AB et AC, donc El-Kashi donne BC² = 5² + 6² − 2 × 5 × 6 × cos 60°.
2. cos 60° = 1/2, donc BC² = 25 + 36 − 30 = 31 et BC = √31.
3. Dans A′B′C′, les mêmes données donnent B′C′² = 31, donc B′C′ = √31 = BC.
4. Les trois côtés sont deux à deux égaux : par définition, les triangles sont isométriques. Deux côtés et l'angle compris ont suffi.

:::

::: exemple Un côté et ses deux angles voisins : BC = B′C′ = 12, B̂ = B̂′ = 30° et Ĉ = Ĉ′ = 60°

1. Â = 180° − 30° − 60° = 90° et Â′ = 90°, car la somme des angles d'un triangle vaut 180°.
2. Loi du sinus dans ABC : AB = BC sin Ĉ / sin Â = 12 × (√3/2) / 1 = 6√3 et AC = BC sin B̂ / sin Â = 12 × (1/2) / 1 = 6.
3. Les mêmes calculs dans A′B′C′ donnent A′B′ = 6√3 et A′C′ = 6 : les trois paires de côtés sont égales.

:::

::: piege Choisir un angle qui n'est pas compris entre les deux côtés égaux
Le chapitre de trigonométrie a montré que BC = 3√3, CA = 3 et B̂ = 30° donnent deux triangles : l'un avec Â = 60° et AB = 6, l'autre avec Â = 120° et AB = 3. Un élève conclut pourtant « deux côtés et un angle égaux, donc isométriques ». Cela tente parce qu'un cas d'isométrie parle de deux côtés et d'un angle.
Mais B̂ n'est pas l'angle compris entre BC et CA (c'est Ĉ) : ces deux triangles ont les trois égalités sans être isométriques, puisque AB vaut 6 dans l'un et 3 dans l'autre. L'angle doit être compris entre les deux côtés.
:::

::: propriete
Deux triangles ABC et A′B′C′ sont isométriques dans chacun de ces trois cas :

- 1ᵉʳ cas : un côté égal compris entre deux angles respectivement égaux (BC = B′C′, B̂ = B̂′ et Ĉ = Ĉ′) ;
- 2ᵉ cas : un angle égal compris entre deux côtés respectivement égaux (AB = A′B′, AC = A′C′ et Â = Â′) ;
- 3ᵉ cas : trois côtés respectivement égaux (c'est la définition).

Raison du 1ᵉʳ cas : Â = Â′ par la somme des angles, et la loi du sinus donne AB = BC sin Ĉ / sin Â = B′C′ sin Ĉ′ / sin Â′ = A′B′, et de même AC = A′C′. Raison du 2ᵉ cas : El-Kashi donne BC² = AB² + AC² − 2 AB × AC cos Â = B′C′², donc BC = B′C′.
Cas limite : trois angles égaux ne suffisent pas. Un triangle de côtés 3, 4, 5 et un triangle de côtés 6, 8, 10 ont les mêmes angles sans être isométriques : ils sont semblables, notion de l'étape suivante.

:::

::: verifie
Les triangles ABC et A′B′C′ vérifient AB = A′B′ = 8, BC = B′C′ = 5 et B̂ = B̂′ = 60°. Sont-ils isométriques ? Si oui, que vaut AC ?

---

L'angle B̂ est compris entre les côtés BA et BC, qui sont les deux côtés égaux : c'est le 2ᵉ cas, donc les triangles sont isométriques. El-Kashi donne AC² = 8² + 5² − 2 × 8 × 5 × cos 60° = 64 + 25 − 40 = 49, donc AC = A′C′ = 7.
:::

::: retenir
Deux triangles sont isométriques si leurs côtés sont deux à deux égaux : un côté et les deux angles voisins, ou deux côtés et l'angle compris, ou trois côtés suffisent ; un angle qui n'est pas compris ne suffit pas.
:::

## 🔍 Triangles semblables : même forme, autre taille

Un fanion triangulaire ABC mesure AB = 30 cm, AC = 40 cm et BC = 50 cm. Son modèle réduit A′B′C′ a exactement les mêmes angles, mais son côté [A′B′] ne mesure que 12 cm.
Que valent A′C′ et B′C′ : les côtés sont-ils réduits de la même façon ?

::: definition
Deux triangles ABC et A′B′C′ sont **semblables** si leurs angles sont deux à deux égaux : Â = Â′, B̂ = B̂′ et Ĉ = Ĉ′. Les côtés opposés à des angles égaux, comme BC et B′C′, sont dits **homologues**.
:::

::: figure Le fanion ABC et son modèle réduit A′B′C′, dessinés à l'échelle : un arc en B et en B′, deux arcs en C et en C′ et un angle droit en A et en A′ marquent les angles égaux, mais les côtés n'ont pas les mêmes longueurs
<svg viewBox="0 62 366 194"><path d="M30 220 L30 94 L198 220 Z" fill="#0f6e56" opacity="0.12"/><path d="M30 220 L30 94 L198 220 Z" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M30 209 L41 209 L41 220" fill="none" stroke="#0f172a" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/><path d="M30 118 A24 24 0 0 0 49.2 108.4" fill="none" stroke="#b45309" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M170 220 A28 28 0 0 1 175.6 203.2" fill="none" stroke="#6d28d9" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M165 220 A33 33 0 0 1 171.6 200.2" fill="none" stroke="#6d28d9" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><circle cx="30" cy="220" r="4" fill="#0f172a"/><circle cx="30" cy="94" r="4" fill="#0f172a"/><circle cx="198" cy="220" r="4" fill="#0f172a"/><path d="M265.2 220 L265.2 169.6 L332.4 220 Z" fill="#0f6e56" opacity="0.12"/><path d="M265.2 220 L265.2 169.6 L332.4 220 Z" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M265.2 211 L274.2 211 L274.2 220" fill="none" stroke="#0f172a" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/><path d="M265.2 182.6 A13 13 0 0 0 275.6 177.4" fill="none" stroke="#b45309" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M317.4 220 A15 15 0 0 1 320.4 211" fill="none" stroke="#6d28d9" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M313.4 220 A19 19 0 0 1 317.2 208.6" fill="none" stroke="#6d28d9" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><circle cx="265.2" cy="220" r="4" fill="#0f172a"/><circle cx="265.2" cy="169.6" r="4" fill="#0f172a"/><circle cx="332.4" cy="220" r="4" fill="#0f172a"/><g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.6" stroke-linejoin="round"><text x="21.7" y="237.5" text-anchor="middle" font-size="14" fill="#0f172a">A</text><text x="21.8" y="86.4" text-anchor="middle" font-size="14" fill="#0f172a">B</text><text x="212.1" y="230.2" text-anchor="middle" font-size="14" fill="#0f172a">C</text><text x="255.8" y="236.7" text-anchor="middle" font-size="14" fill="#0f172a">A′</text><text x="257.3" y="161.9" text-anchor="middle" font-size="14" fill="#0f172a">B′</text><text x="346.5" y="230.1" text-anchor="middle" font-size="14" fill="#0f172a">C′</text><text x="17" y="162" text-anchor="middle" font-size="13" fill="#0f6e56">30</text><text x="114" y="238" text-anchor="middle" font-size="13" fill="#0f6e56">40</text><text x="124.4" y="154.2" text-anchor="middle" font-size="13" fill="#0f6e56">50</text><text x="252.2" y="199.8" text-anchor="middle" font-size="13" fill="#0f6e56">12</text></g></svg>
:::

Sur la figure, les arcs identiques marquent les angles égaux. [AB] et [A′B′] sont opposés à Ĉ et Ĉ′ : ils sont homologues, comme [AC] et [A′C′] (opposés à B̂ et B̂′) et comme [BC] et [B′C′] (opposés à Â et Â′).

::: exemple Le fanion : A′C′ et B′C′ avec A′B′ = 12 cm

1. AB et A′B′ sont homologues, et AB / A′B′ = 30/12 = 5/2 : c'est le rapport de similitude k, car les angles sont égaux.
2. AC / A′C′ = 5/2, donc A′C′ = 40 × 2/5 = 16 cm, car chaque paire de côtés homologues a le même rapport.
3. BC / B′C′ = 5/2, donc B′C′ = 50 × 2/5 = 20 cm.
4. Contrôle : 12² + 16² = 144 + 256 = 400 = 20², le petit fanion est donc rectangle en A′ comme le grand (30² + 40² = 50²).

:::

::: exemple Deux triangles semblables : BC = 9, B′C′ = 6 et AB = 12

1. BC et B′C′ sont homologues, donc k = BC / B′C′ = 9/6 = 3/2.
2. AB / A′B′ = 3/2, donc A′B′ = 12 × 2/3 = 8.
3. Du petit au grand triangle, le rapport est l'inverse : 2/3, et 8 × 3/2 = 12 retrouve AB.

:::

::: piege Retirer la même longueur au lieu d'appliquer le même rapport
Pour le fanion, un élève remarque que 30 devient 12, soit 18 cm de moins, et retire 18 cm aux autres côtés : A′C′ = 22 cm et B′C′ = 32 cm. Cela tente parce que « réduire » ressemble à « retrancher la même chose partout ».
Mais des angles égaux imposent le même rapport, pas le même écart : avec 12, 22 et 32 on aurait 12² + 22² = 628 différent de 32² = 1024, un triangle qui n'est même plus rectangle. La bonne réponse est 16 cm et 20 cm.
:::

::: propriete
Si ABC et A′B′C′ sont semblables, avec a = BC, b = CA, c = AB, a′ = B′C′, b′ = C′A′ et c′ = A′B′, leurs côtés homologues sont proportionnels :

$$ a / a′ = b / b′ = c / c′ $$

Ce quotient commun est le rapport de similitude k de ABC à A′B′C′ ; celui de A′B′C′ à ABC est 1/k.
Raison : la loi du sinus donne a = 2R sin Â et a′ = 2R′ sin Â′, avec le même sinus puisque Â = Â′ ; donc a / a′ = R / R′. Le raisonnement est le même pour b et c : les trois quotients valent R / R′.
Cas limite : si k = 1, les côtés homologues sont égaux et les triangles sont isométriques ; réciproquement, deux triangles isométriques ont les mêmes angles (le cosinus cos Â = (b² + c² − a²) / (2bc) est le même), donc sont semblables de rapport 1. Deux angles égaux suffisent : le troisième s'en déduit par la somme des angles.
:::

::: verifie
Les triangles ABC et A′B′C′ vérifient Â = Â′ = 50° et B̂ = B̂′ = 70°. On donne AB = 10, A′B′ = 4 et BC = 15. Calculer B′C′.

---

Le troisième angle est aussi égal : Ĉ = Ĉ′ = 180° − 50° − 70° = 60°. Les triangles sont donc semblables, et AB, A′B′ (opposés à Ĉ et Ĉ′) sont homologues : k = 10/4 = 5/2. Alors BC / B′C′ = 5/2, donc B′C′ = 15 × 2/5 = 6.
:::

::: retenir
Deux triangles semblables ont les mêmes angles et leurs côtés homologues sont proportionnels, dans le même rapport de similitude k ; k = 1 redonne l'isométrie.
:::

## 🧮 Les critères de similitude : reconnaître des triangles semblables sans mesurer d'angle

Sur un plan, on ne lit que des longueurs : un triangle de côtés 4, 6 et 8 cm, et un second de côtés 6, 9 et 12 cm. Aucun angle n'est marqué.
Peut-on affirmer que ces triangles sont semblables, donc qu'ils ont les mêmes angles, sans jamais mesurer un angle ?

::: figure Deux triangles dessinés à l'échelle : 4, 6, 8 d'un côté et 6, 9, 12 de l'autre ; en rangeant les côtés de chaque triangle du plus petit au plus grand, les trois quotients valent 2/3
<svg viewBox="-4 50 345 120"><path d="M60.2 98 L30 130 L118 130 Z" fill="#0f6e56" opacity="0.12"/><path d="M60.2 98 L30 130 L118 130 Z" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><circle cx="60.2" cy="98" r="4" fill="#0f172a"/><circle cx="30" cy="130" r="4" fill="#0f172a"/><circle cx="118" cy="130" r="4" fill="#0f172a"/><path d="M218.4 82.1 L173 130 L305 130 Z" fill="#0f6e56" opacity="0.12"/><path d="M218.4 82.1 L173 130 L305 130 Z" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><circle cx="218.4" cy="82.1" r="4" fill="#0f172a"/><circle cx="173" cy="130" r="4" fill="#0f172a"/><circle cx="305" cy="130" r="4" fill="#0f172a"/><g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.6" stroke-linejoin="round"><text x="54.3" y="89.3" text-anchor="middle" font-size="14" fill="#0f172a">A</text><text x="15.5" y="138.9" text-anchor="middle" font-size="14" fill="#0f172a">B</text><text x="132.7" y="138.2" text-anchor="middle" font-size="14" fill="#0f172a">C</text><text x="212.4" y="73.3" text-anchor="middle" font-size="14" fill="#0f172a">A′</text><text x="158.5" y="138.9" text-anchor="middle" font-size="14" fill="#0f172a">B′</text><text x="319.7" y="138.2" text-anchor="middle" font-size="14" fill="#0f172a">C′</text><text x="32.4" y="116.2" text-anchor="middle" font-size="13" fill="#0f6e56">4</text><text x="101.7" y="115.6" text-anchor="middle" font-size="13" fill="#0f6e56">6</text><text x="74" y="152" text-anchor="middle" font-size="13" fill="#0f6e56">8</text><text x="183" y="108.3" text-anchor="middle" font-size="13" fill="#0f6e56">6</text><text x="274.2" y="107.6" text-anchor="middle" font-size="13" fill="#0f6e56">9</text><text x="239" y="152" text-anchor="middle" font-size="13" fill="#0f6e56">12</text></g></svg>
:::

Sur la figure, on apparie les côtés dans l'ordre de leurs longueurs : AB avec A′B′, AC avec A′C′, BC avec B′C′. Les trois quotients AB / A′B′, AC / A′C′ et BC / B′C′ sont les nombres à comparer.

::: exemple Les côtés 4, 6, 8 et 6, 9, 12

1. On range les côtés dans le même ordre : 4 avec 6, 6 avec 9 et 8 avec 12, car des triangles semblables gardent l'ordre de leurs côtés.
2. Les trois quotients sont 4/6 = 2/3, 6/9 = 2/3 et 8/12 = 2/3, tous égaux.
3. Les triangles sont donc semblables, de rapport 2/3 de ABC à A′B′C′, et ils ont les mêmes angles.

:::

::: exemple Un angle égal et deux côtés proportionnels : Â = Â′ = 50°, AB = 3, AC = 5, A′B′ = 4,5 et A′C′ = 7,5

1. Â est compris entre AB et AC, et entre A′B′ et A′C′ : l'angle égal est bien entre les côtés comparés.
2. AB / A′B′ = 3/4,5 = 2/3 et AC / A′C′ = 5/7,5 = 2/3 : les deux côtés qui comprennent l'angle sont proportionnels.
3. Les triangles sont donc semblables, de rapport 2/3, sans avoir mesuré les angles B̂ et Ĉ.

:::

::: piege Ne vérifier que deux rapports sur trois
Pour les côtés 4, 6, 8 et 6, 9, 13, un élève calcule 4/6 = 2/3 et 6/9 = 2/3, puis conclut « semblables ». Cela tente parce que deux égalités sur trois ressemblent à un motif.
Mais le troisième quotient 8/13 n'est pas égal à 2/3 (8/12 l'aurait été) : les triangles ne sont pas semblables. Les trois quotients doivent être égaux.
:::

::: propriete
Deux triangles ABC et A′B′C′ sont semblables dans chacun de ces deux cas :

- les trois côtés sont proportionnels : a / a′ = b / b′ = c / c′ ;
- un angle est égal et les deux côtés qui le comprennent sont proportionnels : Â = Â′ et c / c′ = b / b′.

Raison du second cas : si b = k b′ et c = k c′, El-Kashi donne a² = k² (b′² + c′² − 2b′c′ cos Â′) = k² a′², donc a = k a′ : on retombe sur trois côtés proportionnels. Raison du premier cas : cos B̂ = (a² + c² − b²) / (2ac) = (k²a′² + k²c′² − k²b′²) / (2k²a′c′) = cos B̂′, donc B̂ = B̂′ (un seul angle de [0 ; π] a ce cosinus), de même Â = Â′ et Ĉ = Ĉ′.
Cas limite : comme pour l'isométrie, deux côtés proportionnels et un angle qui n'est pas compris entre eux ne garantissent rien.
:::

::: verifie
Un triangle ABC a pour côtés 9, 12 et 6 (écrits dans le désordre) et un triangle A′B′C′ a pour côtés 4, 6 et 8. Sont-ils semblables ? Si oui, quel est le rapport de similitude de ABC à A′B′C′ ?

---

On range les côtés : 6, 9, 12 et 4, 6, 8. Les quotients 6/4, 9/6 et 12/8 valent tous 3/2 : les triangles sont semblables, de rapport 3/2. Apparier dans l'ordre d'écriture (9/4, 12/6, 6/8) donnerait des quotients différents : il faut apparier du plus petit au plus grand.
:::

::: retenir
Trois côtés proportionnels, ou un angle égal compris entre deux côtés proportionnels, suffisent pour des triangles semblables ; on compare les trois quotients, côtés rangés dans le même ordre.
:::

## 🔱 Relations métriques : le triangle rectangle et sa hauteur

Une pièce d'équerre a un angle droit en A, avec AB = 6 cm et AC = 8 cm. On veut percer un trou au pied H de la hauteur issue de A sur l'hypoténuse [BC] : il faut connaître AH, mais aussi BH et CH, qui placent H.
Comment les obtenir avec AB et AC seulement ?

::: figure Le triangle rectangle de l'équerre (dessiné à l'échelle) et sa hauteur [AH] : B̂ et HÂC portent un arc orange, Ĉ et BÂH deux arcs violets, car chacun complète l'angle voisin à un angle droit ; ABC, HBA et HAC sont donc trois triangles semblables
<svg viewBox="10 40 330 196"><path d="M137.2 70.4 L40 200 L310 200 Z" fill="#0f6e56" opacity="0.12"/><path d="M137.2 70.4 L40 200 L310 200 Z" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M137.2 70.4 L137.2 200" fill="none" stroke="#b45309" stroke-width="2" stroke-dasharray="6 4" stroke-linecap="round" stroke-linejoin="round"/><path d="M131.2 78.4 L139.2 84.4 L145.2 76.4" fill="none" stroke="#0f172a" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/><path d="M137.2 189 L126.2 189 L126.2 200" fill="none" stroke="#0f172a" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/><path d="M56.8 177.6 A28 28 0 0 1 68 200" fill="none" stroke="#b45309" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M137.2 94.4 A24 24 0 0 0 156.4 84.8" fill="none" stroke="#b45309" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M287.6 183.2 A28 28 0 0 0 282 200" fill="none" stroke="#6d28d9" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M283.6 180.2 A33 33 0 0 0 277 200" fill="none" stroke="#6d28d9" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M122.8 89.6 A24 24 0 0 0 137.2 94.4" fill="none" stroke="#6d28d9" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M119.8 93.6 A29 29 0 0 0 137.2 99.4" fill="none" stroke="#6d28d9" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><circle cx="137.2" cy="70.4" r="4" fill="#0f172a"/><circle cx="40" cy="200" r="4" fill="#0f172a"/><circle cx="310" cy="200" r="4" fill="#0f172a"/><circle cx="137.2" cy="200" r="3.5" fill="#b45309"/><g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.6" stroke-linejoin="round"><text x="131.2" y="61.7" text-anchor="middle" font-size="14" fill="#0f172a">A</text><text x="25.7" y="209.6" text-anchor="middle" font-size="14" fill="#0f172a">B</text><text x="324.3" y="209.6" text-anchor="middle" font-size="14" fill="#0f172a">C</text><text x="137.2" y="220" text-anchor="middle" font-size="14" fill="#b45309">H</text><text x="74.8" y="137.6" text-anchor="middle" font-size="13" fill="#0f6e56">6</text><text x="237.1" y="136.4" text-anchor="middle" font-size="13" fill="#0f6e56">8</text></g></svg>
:::

Sur la figure, B̂ + Ĉ = 90° dans ABC, et HÂC + Ĉ = 90° dans AHC : HÂC et B̂ sont égaux, d'où l'arc orange. De même BÂH et Ĉ sont égaux, d'où les deux arcs violets.

::: exemple L'équerre : AB = 6 cm et AC = 8 cm

1. BC² = AB² + AC² = 36 + 64 = 100, donc BC = 10 : c'est Pythagore dans le triangle rectangle ABC.
2. L'aire de ABC s'écrit ½ AB × AC et aussi ½ AH × BC, donc AH = AB × AC / BC = 48/10 = 4,8, car c'est la même aire calculée avec la hauteur [AH] sur la base [BC].
3. ABH et ABC sont semblables (angle droit et angle B̂ communs) : AB / BC = BH / AB, donc BH = AB² / BC = 36/10 = 3,6.
4. De même CH = AC² / BC = 64/10 = 6,4. Contrôle : BH + CH = 3,6 + 6,4 = 10 = BC, et AH² = 23,04 = 3,6 × 6,4.

:::

::: exemple Sans contexte : BH = 2 et CH = 8

1. ABH et CAH sont semblables : BH / AH = AH / CH, donc AH² = BH × CH = 16 et AH = 4.
2. BC = BH + CH = 10, donc AB² = BH × BC = 20 et AC² = CH × CB = 80 ; AB = 2√5 et AC = 4√5.
3. Contrôle de Pythagore : AB² + AC² = 20 + 80 = 100 = BC².

:::

::: piege Additionner BH et CH au lieu de les multiplier
Pour BH = 2 et CH = 8, un élève écrit AH² = BH + CH = 10 et AH = √10. Cela tente parce que l'on sait déjà que BH + CH = BC, et que la somme est le premier geste.
Mais la relation est un produit : AH² = BH × CH = 16 et AH = 4. Le contrôle le confirme : dans ABH rectangle en H, AB² = AH² + BH² = 16 + 4 = 20 = BH × BC, alors que AH = √10 donnerait AB² = 14, qui est différent de 20.
:::

::: propriete
Soit ABC un triangle rectangle en A et H le pied de la hauteur issue de A. Alors :

- BC² = AB² + AC² ;
- AH × BC = AB × AC ;
- AH² = BH × CH ;
- AB² = BH × BC et AC² = CH × CB.

Raison : AH × BC = AB × AC écrit l'aire de deux façons. ABH et CBA ont un angle droit et l'angle B̂ en commun, donc AB / CB = BH / BA ; de même AC / BC = CH / CA avec ACH et BCA. ABH et CAH sont semblables (BÂH = Ĉ et ABĤ = CÂH), donc BH / AH = AH / CH. Enfin AB² + AC² = (BH + CH) × BC = BC² retrouve Pythagore.
Cas limite : si AB = AC, H est le milieu de [BC] : BH = CH = BC/2 et AH = BC/2.
:::

::: verifie
Dans un triangle ABC rectangle en A, on a AB = 4 et BC = 8. H est le pied de la hauteur issue de A. Calculer BH, puis AC.

---

AB² = BH × BC donne 16 = 8 × BH, donc BH = 2. Puis CH = BC − BH = 6 et AC² = CH × CB = 6 × 8 = 48, donc AC = 4√3, soit environ 6,93. Contrôle de Pythagore : 16 + 48 = 64 = 8².
:::

::: retenir
Dans le triangle ABC rectangle en A, de hauteur [AH] : AB² = BH × BC, AC² = CH × CB, AH² = BH × CH et AH × BC = AB × AC ; tout vient de triangles semblables et d'une aire écrite de deux façons.
:::

> 🗡️ Culture mathématique : la formule de la deuxième étape porte le nom de **Héron d'Alexandrie**, mathématicien de l'Antiquité.

> 🏆 Quête franchie, héros : tu sais partager un côté avec une bissectrice, calculer une aire à partir des trois côtés, reconnaître des triangles isométriques ou semblables avec peu de mesures, et exploiter la hauteur d'un triangle rectangle. Ces six outils complètent ceux du chapitre de trigonométrie.
