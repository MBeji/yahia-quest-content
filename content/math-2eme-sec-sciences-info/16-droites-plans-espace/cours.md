# ⚔️ Droites et plans de l'espace — voir et prouver dans les trois dimensions

> 💡 «Sur une feuille, tout est plat. Dans l'espace, deux droites peuvent se frôler sans jamais se toucher : apprendre à le voir, puis à le prouver, c'est gagner une troisième dimension.»

Jusqu'ici, tes figures vivaient dans un plan. Maintenant, le dessin n'est que l'ombre d'un solide : il faut raisonner sur ce que la feuille ne montre pas.
Huit étapes t'y conduisent : les solides usuels, leurs mesures, les axiomes de base, la détermination d'un plan, la coplanarité, la position de deux droites, d'une droite et d'un plan, de deux plans. Sur tous les dessins, les arêtes cachées sont en tirets. Le parallélisme et l'orthogonalité dans l'espace sont l'objet des deux chapitres suivants : ici, on n'en a pas besoin.

## 🧊 Les solides usuels : faces, arêtes, sommets

Une boîte de chocolats a la forme d'un prisme dont la base est un triangle : deux triangles aux extrémités, des rectangles sur les côtés.
Combien a-t-elle de faces, d'arêtes et de sommets, et comment n'en oublier aucun quand certains sont cachés derrière le dessin ?

::: definition
Un solide de l'espace est limité par des **faces**, qui sont des polygones plans. Deux faces voisines se rejoignent suivant une **arête**, qui est un segment, et les extrémités des arêtes sont les **sommets**.
Solides usuels : le **cube** et le **parallélépipède rectangle** (le pavé), à 6 faces rectangulaires ; le **tétraèdre**, à 4 faces triangulaires ; le **prisme droit**, qui a deux bases superposables reliées par des faces rectangulaires ; la **pyramide**, qui a une base et des faces triangulaires réunies en un sommet S.
:::

::: figure Le prisme droit à base triangulaire ABCA′B′C′ : les triangles ABC et A′B′C′ sont ses bases, et les arêtes cachées [CA], [CB] et [CC′] sont en tirets
<svg viewBox="0 20 340 220"><path d="M40 89 L250 89 L182.4 39 Z" fill="#0f6e56" opacity="0.14"/><path d="M40 215 L250 215 L250 89 L40 89 Z" fill="#0f6e56" opacity="0.07"/><path d="M250 215 L182.4 165" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M40 215 L182.4 165" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M182.4 165 L182.4 39" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M40 215 L250 215" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M40 89 L250 89" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M250 89 L182.4 39" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M40 89 L182.4 39" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M250 215 L250 89" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M40 215 L40 89" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><g fill="#0f172a"><circle cx="40" cy="215" r="3.8"/><circle cx="250" cy="215" r="3.8"/><circle cx="182.4" cy="165" r="3.8"/><circle cx="40" cy="89" r="3.8"/><circle cx="250" cy="89" r="3.8"/><circle cx="182.4" cy="39" r="3.8"/></g><g font-size="15" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="29" y="227" text-anchor="middle" fill="#0f172a">A</text><text x="261" y="229" text-anchor="middle" fill="#0f172a">B</text><text x="180.4" y="156" text-anchor="middle" fill="#0f172a">C</text><text x="28" y="86" text-anchor="middle" fill="#0f172a">A′</text><text x="262" y="86" text-anchor="middle" fill="#0f172a">B′</text><text x="184.4" y="29" text-anchor="middle" fill="#0f172a">C′</text></g></svg>
:::

Sur la figure, les bases sont les triangles ABC et A′B′C′, et les faces latérales sont les rectangles ABB′A′, BCC′B′ et CAA′C′ : ce sont les arêtes en tirets qu'on oublie de compter.

::: exemple La boîte de chocolats, comptée pas à pas

1. Faces : 2 triangles pour les bases et 3 rectangles pour les côtés, soit 5 faces, car chaque polygone du dessin est une face, y compris celles que l'on ne voit pas.
2. Sommets : 3 par base et 2 bases, soit 6 sommets, car les sommets sont les coins des deux triangles.
3. Arêtes : 3 par base, soit 6, plus les 3 arêtes latérales [AA′], [BB′] et [CC′] : 9 arêtes, dont 3 cachées en tirets.

:::

::: piege Compter les arêtes face par face
Un élève additionne les côtés de toutes les faces : 2 × 3 + 3 × 4 = 18, et annonce 18 arêtes. Cela tente parce que chaque face a bien ses côtés.
Mais une arête sépare deux faces voisines, donc ce total la compte deux fois. Le nombre d'arêtes est 18 / 2 = 9.
:::

::: propriete

| Solide                           | Faces | Arêtes | Sommets |
| -------------------------------- | ----- | ------ | ------- |
| Cube, parallélépipède rectangle  | 6     | 12     | 8       |
| Tétraèdre                        | 4     | 6      | 4       |
| Prisme droit à base triangulaire | 5     | 9      | 6       |
| Pyramide à base carrée           | 5     | 8      | 5       |

Cas limite : la base de la pyramide a 4 sommets, mais la pyramide en a 5, car le sommet S compte aussi.
:::

::: verifie
Un prisme droit a pour base un quadrilatère ABCD. Combien a-t-il de faces, d'arêtes et de sommets ?

---

Faces : 2 bases et 4 faces latérales, une par côté de la base, soit 6. Sommets : 4 par base, soit 8. Arêtes : 4 par base, soit 8, plus 4 arêtes latérales, soit 12. On retrouve les nombres du pavé, qui est un prisme droit à base rectangulaire.
:::

::: retenir
Un solide se compte face par face, sommet par sommet et arête par arête, cachées comprises : pavé 6 · 12 · 8, tétraèdre 4 · 6 · 4, prisme droit à base triangulaire 5 · 9 · 6, pyramide à base carrée 5 · 8 · 5.
:::

## 📦 Mesurer un pavé et un cube : diagonales, aire latérale, volume

Une tige de 13 cm doit être rangée dans une boîte de 12 cm de long, 4 cm de large et 3 cm de haut. Posée à plat le long de la boîte, elle ne tient pas, puisque 12 < 13. Peut-elle tenir en biais, d'un coin au coin opposé ?
Pour répondre, il faut mesurer une diagonale du solide, puis, pour la peinture et le remplissage, son aire latérale et son volume.

::: definition
Dans un pavé ABCDA′B′C′D′, de base ABCD et de hauteur AA′, une **petite diagonale** est la diagonale d'une face, par exemple [AC], et une **grande diagonale** joint deux sommets opposés du solide, par exemple [AC′].
L'**aire latérale** est la somme des aires des quatre faces latérales, sans les deux bases ; l'**aire totale** y ajoute les deux bases. Le **volume** mesure la place occupée par le solide.
:::

::: figure La boîte de l'exemple, de 12 cm sur 4 cm sur 3 cm : le triangle ACC′ est rectangle en C, sa base [AC] est une petite diagonale et son hypoténuse [AC′] la grande diagonale
<svg viewBox="0 70 340 160"><path d="M22 190 L276.6 163.4 L276.6 106.4 Z" fill="#b45309" opacity="0.14"/><path d="M276.6 163.4 L48.6 163.4" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M22 190 L48.6 163.4" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M48.6 163.4 L48.6 106.4" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M22 190 L250 190" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M250 190 L276.6 163.4" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M22 133 L250 133" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M250 133 L276.6 106.4" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M276.6 106.4 L48.6 106.4" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M22 133 L48.6 106.4" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M250 190 L250 133" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M22 190 L22 133" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M276.6 163.4 L276.6 106.4" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M22 190 L276.6 163.4" fill="none" stroke="#b45309" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M22 190 L276.6 106.4" fill="none" stroke="#0f6e56" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/><g fill="#0f172a"><circle cx="22" cy="190" r="3.8"/><circle cx="250" cy="190" r="3.8"/><circle cx="276.6" cy="163.4" r="3.8"/><circle cx="48.6" cy="163.4" r="3.8"/><circle cx="22" cy="133" r="3.8"/><circle cx="250" cy="133" r="3.8"/><circle cx="276.6" cy="106.4" r="3.8"/><circle cx="48.6" cy="106.4" r="3.8"/></g><g font-size="15" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="11" y="202" text-anchor="middle" fill="#0f172a">A</text><text x="261" y="204" text-anchor="middle" fill="#0f172a">B</text><text x="289.6" y="167.4" text-anchor="middle" fill="#0f172a">C</text><text x="37.6" y="161.4" text-anchor="middle" fill="#0f172a">D</text><text x="10" y="131" text-anchor="middle" fill="#0f172a">A′</text><text x="242" y="151" text-anchor="middle" fill="#0f172a">B′</text><text x="289.6" y="101.4" text-anchor="middle" fill="#0f172a">C′</text><text x="44.6" y="96.4" text-anchor="middle" fill="#0f172a">D′</text></g><g font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="136" y="207" text-anchor="middle" fill="#0f172a">12</text></g><g font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="276.3" y="188.7" text-anchor="middle" fill="#0f172a">4</text></g><g font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="12" y="165.5" text-anchor="middle" fill="#0f172a">3</text></g></svg>
:::

Sur la figure, [AC] est la diagonale de la base et [CC′] a la longueur de la hauteur, 3 cm ; [AC′] est l'hypoténuse du triangle ACC′, rectangle en C parce que l'arête [CC′] est dressée à angle droit sur la base.

::: exemple La tige de 13 cm dans la boîte de 12 × 4 × 3

1. Dans le rectangle ABCD, AC² = AB² + BC² = 144 + 16 = 160, par le théorème de Pythagore (angle droit en B).
2. Dans le triangle ACC′ rectangle en C, AC′² = AC² + CC′² = 160 + 9 = 169, donc AC′ = 13 cm : la troisième dimension s'ajoute sous la racine.
3. Le plus long segment de la boîte mesure donc 13 cm : la tige tient juste, d'un coin à l'autre.
4. Aire latérale : 2 × (12 + 4) × 3 = 96 cm², car les quatre faces latérales, mises bout à bout, forment un rectangle dont la longueur est le périmètre de la base et la hauteur 3 cm.
5. Volume : 12 × 4 × 3 = 144 cm³, soit l'aire de la base, 48 cm², multipliée par la hauteur. L'aire totale vaut 96 + 2 × 48 = 192 cm².

:::

::: piege Calculer la grande diagonale avec deux dimensions seulement
Un élève écrit AC′ = √(12² + 4²) = √160 ≈ 12,65 et conclut que la tige ne tient pas. Cela tente parce que, dans un rectangle, Pythagore n'utilise que deux côtés.
Mais √160 est la longueur de [AC], la diagonale de la base, et non celle de [AC′]. Il faut une seconde application de Pythagore avec la hauteur : 160 + 9 = 169, donc 13 cm.
:::

::: propriete

- Cube d'arête a : petite diagonale a√2, grande diagonale a√3 (car AC′² = 2a² + a²), aire latérale 4a², volume a³.
- Pavé de dimensions a, b, c (base a sur b, hauteur c) : grande diagonale √(a² + b² + c²), aire latérale 2(a + b)c, volume abc.

Cas limite : le cube est le pavé où a = b = c ; l'aire totale s'obtient en ajoutant les deux bases à l'aire latérale.
:::

::: exemple Un pavé dont on ne connaît pas les dimensions
Un pavé a une aire totale de 76 cm² et la somme de ses 12 arêtes vaut 44 cm. Quelle est la longueur de sa grande diagonale ?

1. Les 12 arêtes se groupent par quatre selon la dimension : 4(a + b + c) = 44, donc a + b + c = 11.
2. L'aire totale vaut 2(ab + bc + ca) = 76, donc ab + bc + ca = 38.
3. On développe (a + b + c)² = a² + b² + c² + 2(ab + bc + ca) : 121 = a² + b² + c² + 76, donc a² + b² + c² = 45.
4. La grande diagonale vaut √(a² + b² + c²) = √45 = 3√5, soit environ 6,71 cm, sans avoir calculé a, b ni c.

:::

> 🗡️ Pour compter dans un cube découpé, pense volume : un cube de 5 cm d'arête, peint sur ses six faces, est scié en 125 petits cubes de 1 cm. Ceux qui n'ont aucune face peinte forment un cube intérieur de côté 3, soit 27 cubes : 125 − 27 = 98 petits cubes ont au moins une face peinte.

::: verifie
Un cube a pour arête 4 cm. Calculer sa grande diagonale et son aire latérale.

---

Grande diagonale : 4√3 cm, soit environ 6,93 cm, car 16 + 16 + 16 = 48 = 16 × 3 : les trois dimensions s'ajoutent sous la racine. Aire latérale : 4 × 4² = 64 cm², les quatre faces carrées ayant 16 cm² chacune.
:::

::: retenir
La grande diagonale d'un pavé vaut √(a² + b² + c²), avec les trois dimensions ; l'aire latérale vaut 2(a + b)c et le volume abc ; pour un cube d'arête a : a√2, a√3, 4a² et a³.
:::

## 📜 Les axiomes de base : ce qu'on admet pour raisonner dans l'espace

Un appareil photo posé sur un trépied ne bouge jamais, même sur un sol irrégulier, alors qu'une table à quatre pieds peut être bancale. Pourquoi trois points d'appui suffisent-ils à fixer un plan ?
Et si une règle touche une table en deux points, où se trouve le reste de la règle ? Ces questions se règlent par quelques vérités que l'on admet : les axiomes.

::: propriete Les quatre axiomes

- **Axiome 1** : par trois points non alignés passe un plan et un seul.
- **Axiome 2** : si un plan contient deux points distincts A et B, il contient toute la droite (AB).
- **Axiome 3** : si deux plans distincts ont un point commun, ils se coupent suivant une droite qui passe par ce point.
- **Axiome 4** : tout ce que l'on sait de la géométrie plane (Thalès, Pythagore, propriétés des triangles) s'applique à l'intérieur de chaque plan de l'espace.

Notations : un point **appartient** (∈) à une droite ou à un plan ; une droite est **contenue** (⊂) dans un plan.
:::

::: figure Le plan P est fixé par les points non alignés A, B et C ; la droite (AB), en vert, est tout entière dans P parce que A et B y sont
<svg viewBox="0 40 340 190"><path d="M40 210 L280 210 L336 154 L96 154 Z" fill="#0f6e56" opacity="0.1"/><path d="M40 210 L280 210 L336 154 L96 154 Z" fill="none" stroke="#0f172a" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/><path d="M45.8 204.2 L319.9 170.1" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/><path d="M100.6 197.4 L178 168 L246.8 179.2" fill="none" stroke="#94a3b8" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><g fill="#0f172a"><circle cx="100.6" cy="197.4" r="4.2"/><circle cx="246.8" cy="179.2" r="4.2"/><circle cx="178" cy="168" r="4.2"/></g><g font-size="15" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="96.6" y="214.4" text-anchor="middle" fill="#0f172a">A</text><text x="256.8" y="194.2" text-anchor="middle" fill="#0f172a">B</text><text x="176" y="158" text-anchor="middle" fill="#0f172a">C</text></g><g font-size="16" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="294" y="202" text-anchor="middle" fill="#0f6e56">P</text></g></svg>
:::

Sur la figure, A, B et C fixent le plan P (axiome 1), et la droite (AB) y reste tout entière (axiome 2) : la règle posée sur la table en deux points est entièrement sur la table.

::: exemple Une droite dans le plan d'une face
Dans un tétraèdre ABCD, I est le milieu de [AB] et J celui de [AC]. Montrons que la droite (IJ) est contenue dans le plan (ABC).

1. A, B et C ne sont pas alignés, car ce sont les sommets d'une face triangulaire : ils déterminent un seul plan (ABC), par l'axiome 1.
2. A et B sont dans (ABC), donc (AB) ⊂ (ABC) par l'axiome 2, et I ∈ (AB) donne I ∈ (ABC). De même J ∈ (AC) ⊂ (ABC).
3. I et J sont deux points distincts de (ABC), donc (IJ) ⊂ (ABC), encore par l'axiome 2.

:::

::: piege Écrire (IJ) ∈ (ABC)
Un élève conclut « (IJ) ∈ (ABC) », ou « I ⊂ (ABC) ». Cela tente parce que les deux symboles se lisent « est dans ».
Mais ∈ relie un point à une droite ou à un plan, et ⊂ relie une droite à un plan : on écrit I ∈ (ABC) et (IJ) ⊂ (ABC).
:::

::: methode Montrer qu'une droite est contenue dans un plan

1. Nommer le plan par trois de ses points non alignés (axiome 1).
2. Montrer que deux points distincts de la droite appartiennent à ce plan.
3. Conclure par l'axiome 2.

Cas limite : avec trois points alignés A, B, C, il n'y a pas un plan mais une infinité, tous contenant la droite (AB), comme les pages d'un livre ouvert autour de son dos.
:::

::: verifie
Dans le même tétraèdre, K est le milieu de [BC]. La droite (IK) est-elle contenue dans le plan (ABC) ?

---

Oui. Le plan (ABC) est déterminé par A, B, C. Le point I est sur (AB) et K sur (BC), deux droites contenues dans (ABC) puisque deux de leurs points y sont : I et K sont donc dans (ABC). Ils sont distincts, donc (IK) ⊂ (ABC) par l'axiome 2.
:::

::: retenir
Trois points non alignés fixent un plan ; deux points d'un plan entraînent toute leur droite ; deux plans distincts qui se rencontrent partagent une droite ; la géométrie plane vaut dans chaque plan. On écrit ∈ pour un point, ⊂ pour une droite.
:::

## 🚪 Déterminer un plan : trois façons de le désigner

Une porte tient sur ses charnières, qui forment une droite. Tant que l'on ne tient que cette droite, la porte peut pivoter, et chaque ouverture donne un plan différent. Que faut-il ajouter pour qu'un seul plan reste possible ? La poignée suffit : un point hors de la droite.
Quels ingrédients fixent un plan, et lesquels ne suffisent pas ?

::: propriete
Un plan est **déterminé**, c'est-à-dire qu'il existe et qu'il est unique, par l'une de ces trois données :

- trois points non alignés ;
- une droite et un point n'appartenant pas à cette droite ;
- deux droites sécantes.
:::

::: figure Les trois façons de fixer un plan : trois points non alignés, une droite Δ et un point A hors d'elle, deux droites D et D′ qui se coupent en O
<svg viewBox="0 80 340 85"><path d="M10 150 L93.2 150 L113.4 129.8 L30.2 129.8 Z" fill="#0f6e56" opacity="0.1"/><path d="M10 150 L93.2 150 L113.4 129.8 L30.2 129.8 Z" fill="none" stroke="#0f172a" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/><g fill="#0f172a"><circle cx="32.1" cy="145.5" r="3.6"/><circle cx="80.2" cy="143.8" r="3.6"/><circle cx="65.1" cy="134.9" r="3.6"/></g><g font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="30.1" y="160.5" text-anchor="middle" fill="#0f172a">A</text><text x="89.2" y="157.8" text-anchor="middle" fill="#0f172a">B</text><text x="64.1" y="126.9" text-anchor="middle" fill="#0f172a">C</text></g><path d="M112.4 150 L195.6 150 L215.8 129.8 L132.6 129.8 Z" fill="#0f6e56" opacity="0.1"/><path d="M112.4 150 L195.6 150 L215.8 129.8 L132.6 129.8 Z" fill="none" stroke="#0f172a" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/><path d="M118.5 143.9 L208 137.6" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/><g fill="#0f172a"><circle cx="176.1" cy="134.3" r="3.6"/></g><g font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="175.1" y="126.3" text-anchor="middle" fill="#0f172a">A</text></g><g font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="193.3" y="153.5" text-anchor="middle" fill="#0f6e56">Δ</text></g><path d="M214.8 150 L298 150 L318.2 129.8 L235 129.8 Z" fill="#0f6e56" opacity="0.1"/><path d="M214.8 150 L298 150 L318.2 129.8 L235 129.8 Z" fill="none" stroke="#0f172a" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/><path d="M215.9 148.9 L317.1 130.9" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/><path d="M241.6 129.8 L291.4 150" fill="none" stroke="#b45309" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/><g fill="#0f172a"><circle cx="266.5" cy="139.9" r="3.6"/></g><g font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="269.5" y="154.9" text-anchor="middle" fill="#0f172a">O</text></g><g font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="217.9" y="163.9" text-anchor="middle" fill="#0f6e56">D</text></g><g font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="239.6" y="122.8" text-anchor="middle" fill="#b45309">D′</text></g></svg>
:::

Sur la figure, les deux derniers cas se ramènent au premier : sur Δ, on prend deux points qui, avec A, sont non alignés ; pour D et D′, on prend O et un autre point sur chaque droite.

::: figure La face SAD de la pyramide SABCD, en teinte : son plan se désigne par S, A, D, par (AD) et S, ou par (SA) et (SD)
<svg viewBox="0 20 340 230"><path d="M168.9 38.9 L40 225 L242.4 225 Z" fill="#0f6e56" opacity="0.12"/><path d="M297.8 169.6 L95.4 169.6" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M40 225 L95.4 169.6" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M95.4 169.6 L168.9 38.9" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M40 225 L242.4 225" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M242.4 225 L297.8 169.6" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M40 225 L168.9 38.9" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M242.4 225 L168.9 38.9" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M297.8 169.6 L168.9 38.9" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><g fill="#0f172a"><circle cx="40" cy="225" r="3.8"/><circle cx="242.4" cy="225" r="3.8"/><circle cx="297.8" cy="169.6" r="3.8"/><circle cx="95.4" cy="169.6" r="3.8"/><circle cx="168.9" cy="38.9" r="3.8"/></g><g font-size="15" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="29" y="238" text-anchor="middle" fill="#0f172a">A</text><text x="253.4" y="239" text-anchor="middle" fill="#0f172a">B</text><text x="310.8" y="173.6" text-anchor="middle" fill="#0f172a">C</text><text x="84.4" y="167.6" text-anchor="middle" fill="#0f172a">D</text><text x="168.9" y="28.9" text-anchor="middle" fill="#0f172a">S</text></g></svg>
:::

::: exemple Les trois façons pour la face SAD
La pyramide SABCD a pour base le carré ABCD. Désignons le plan de sa face SAD de trois façons.

1. Par trois points non alignés : S, A et D, car S n'est pas sur la droite (AD).
2. Par une droite et un point : (AD) et S, car S n'appartient pas à (AD) ; deux points de (AD) avec S redonnent les trois points de la façon précédente.
3. Par deux droites sécantes : (SA) et (SD), qui se coupent en S ; leurs points S, A et D sont encore les mêmes trois points.

:::

::: piege Fixer un plan avec une droite et l'un de ses points
Un élève écrit « le plan défini par la droite (AD) et le point A ». Cela tente parce qu'il y a bien une droite et un point.
Mais A est sur (AD) : rien n'a été ajouté, et une infinité de plans contiennent (AD), comme la porte qui pivote. Le point doit être hors de la droite.
:::

::: methode Désigner le plan d'une face

1. Repérer trois points non alignés de la face, par exemple ses sommets.
2. Si l'on préfère, remplacer deux de ces points par la droite qu'ils déterminent, ou prendre deux droites sécantes passant par eux.
3. Vérifier la condition de la façon choisie : points non alignés, point hors de la droite, droites sécantes.

Cas limite : deux droites quelconques ne suffisent pas, il faut qu'elles soient sécantes.
:::

::: verifie
Dans la même pyramide, désigner le plan de la face SBC de deux façons différentes de « trois sommets ».

---

Par une droite et un point : (BC) et S, puisque S n'est pas sur (BC). Par deux droites sécantes : (SB) et (SC), qui se coupent en S. Dans les deux cas on retrouve les trois points non alignés S, B et C, donc le plan (SBC).
:::

::: retenir
Trois points non alignés, une droite et un point hors d'elle, ou deux droites sécantes déterminent un plan et un seul ; un point de la droite, ou deux droites quelconques, ne suffisent pas.
:::

## 🔭 Points coplanaires, droites coplanaires

Une table est stable lorsque les extrémités de ses quatre pieds sont dans un même plan, celui du sol ; sinon elle est bancale. Quatre points de l'espace sont-ils toujours dans un même plan ?
Et comment le savoir, sans les voir posés à plat ?

::: definition
Des points sont **coplanaires** lorsqu'un même plan les contient tous ; des droites sont **coplanaires** lorsqu'un même plan les contient toutes.
Dans un tétraèdre ABCD, les quatre sommets ne sont pas coplanaires : D n'est pas dans le plan (ABC).
:::

::: figure Dans le tétraèdre ABCD, I est sur [AB] et J sur [CD] : le plan teinté (ABJ) contient A, B et J, et aussi I puisque I est sur la droite (AB)
<svg viewBox="0 10 340 235"><path d="M44 222 L272 222 L212 99.1 Z" fill="#0f6e56" opacity="0.16"/><path d="M272 222 L201.7 155.5" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M44 222 L201.7 155.5" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M201.7 155.5 L224.5 30.1" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M44 222 L272 222" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M272 222 L224.5 30.1" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M44 222 L224.5 30.1" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M135.2 222 L212 99.1" fill="none" stroke="#0f6e56" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M44 222 L212 99.1" fill="none" stroke="#0f6e56" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M272 222 L212 99.1" fill="none" stroke="#0f6e56" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/><g fill="#0f172a"><circle cx="44" cy="222" r="3.8"/><circle cx="272" cy="222" r="3.8"/><circle cx="201.7" cy="155.5" r="3.8"/><circle cx="224.5" cy="30.1" r="3.8"/></g><g fill="#0f6e56"><circle cx="135.2" cy="222" r="4.2"/><circle cx="212" cy="99.1" r="4.2"/></g><g font-size="15" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="33" y="234" text-anchor="middle" fill="#0f172a">A</text><text x="283" y="236" text-anchor="middle" fill="#0f172a">B</text><text x="189.7" y="151.5" text-anchor="middle" fill="#0f172a">C</text><text x="224.5" y="20.1" text-anchor="middle" fill="#0f172a">D</text><text x="135.2" y="239" text-anchor="middle" fill="#0f6e56">I</text><text x="224" y="103.1" text-anchor="middle" fill="#0f6e56">J</text></g></svg>
:::

Sur la figure, A, B et J déterminent le plan teinté ; comme I est sur (AB), il appartient à ce plan.

::: exemple Quatre points du tétraèdre, avec I sur [AB] et J sur [CD]
Les points I et J sont distincts des extrémités de leurs arêtes.

1. Pour I, A, B, J : les droites (AB) et (CD) n'ont aucun point commun, sinon A, B, C, D seraient coplanaires ; donc J n'est pas sur (AB), et A, B, J déterminent le plan (ABJ).
2. I est sur (AB), contenue dans (ABJ) par l'axiome 2, donc I ∈ (ABJ) : les points I, A, B, J sont coplanaires.
3. Pour I, J, A, C, supposons un plan qui les contient. Il contient A et I, donc toute la droite (AI) = (AB), donc B ; il contient C et J, donc (CJ) = (CD), donc D. Les quatre sommets seraient coplanaires, ce qui est faux : I, J, A, C ne sont pas coplanaires.

:::

::: piege Croire coplanaires des points parce qu'ils sont dessinés sur la même feuille
Un élève regarde le dessin et affirme que I, J, A, C sont coplanaires, car ils sont tous sur la page. Cela tente parce que le dessin range les quatre points dans un même plan, celui de la feuille.
Mais la feuille est plane, pas l'espace : le dessin aplatit la profondeur, et seule une preuve décide.
:::

::: methode Décider si quatre points sont coplanaires

1. Chercher trois points alignés parmi les quatre : s'il y en a, les quatre points sont coplanaires.
2. Sinon, prendre trois points non alignés, qui déterminent un plan (axiome 1).
3. Regarder si le quatrième point est dans ce plan ; sinon, supposer qu'ils sont coplanaires et chercher une absurdité, comme pour I, J, A, C.

Cas limite : les quatre sommets d'un tétraèdre ne sont jamais coplanaires.
:::

::: verifie
Dans le même tétraèdre, K est sur [AC] et L sur [BC], distincts des extrémités. Les points A, B, K, L sont-ils coplanaires ?

---

Oui. A, B et C déterminent le plan (ABC). K est sur (AC) et L sur (BC), deux droites contenues dans (ABC) par l'axiome 2 : K et L sont dans (ABC), avec A et B. Les quatre points sont donc dans un même plan.
:::

::: retenir
Des points sont coplanaires quand un plan les contient tous ; trois points alignés et un quatrième sont toujours coplanaires, et l'on prouve qu'ils ne le sont pas par l'absurde.
:::

## 🛤️ Deux droites : sécantes, parallèles ou non coplanaires

Sur un cube de verre, une fourmi suit l'arête [AB] et une autre l'arête verticale [CC′]. Leurs chemins ne se croisent jamais ; et pourtant, à la différence de deux traits sur une feuille, ces droites ne sont pas parallèles.
Combien de positions deux droites de l'espace peuvent-elles avoir, et comment les reconnaître ?

::: definition
Deux droites **coplanaires** sont **sécantes** si elles ont un seul point commun. Dans un même plan, deux droites distinctes sans point commun sont **parallèles**, comme en géométrie plane.
Deux droites sont **non coplanaires** si aucun plan ne les contient toutes les deux : elles n'ont alors aucun point commun.
:::

::: figure (AB) en vert et (CC′) en orange : elles n'ont aucun point commun, et aucun plan ne les contient toutes les deux
<svg viewBox="0 5 300 240"><path d="M223.6 177.4 L87.6 177.4" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M40 225 L87.6 177.4" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M87.6 177.4 L87.6 41.4" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M40 225 L176 225" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M176 225 L223.6 177.4" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M40 89 L176 89" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M176 89 L223.6 41.4" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M223.6 41.4 L87.6 41.4" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M40 89 L87.6 41.4" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M176 225 L176 89" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M40 225 L40 89" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M223.6 177.4 L223.6 41.4" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M40 225 L176 225" fill="none" stroke="#0f6e56" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"/><path d="M223.6 177.4 L223.6 41.4" fill="none" stroke="#b45309" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"/><g fill="#0f172a"><circle cx="40" cy="225" r="3.8"/><circle cx="176" cy="225" r="3.8"/><circle cx="223.6" cy="177.4" r="3.8"/><circle cx="87.6" cy="177.4" r="3.8"/><circle cx="40" cy="89" r="3.8"/><circle cx="176" cy="89" r="3.8"/><circle cx="223.6" cy="41.4" r="3.8"/><circle cx="87.6" cy="41.4" r="3.8"/></g><g font-size="15" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="29" y="237" text-anchor="middle" fill="#0f172a">A</text><text x="187" y="239" text-anchor="middle" fill="#0f172a">B</text><text x="236.6" y="181.4" text-anchor="middle" fill="#0f172a">C</text><text x="76.6" y="175.4" text-anchor="middle" fill="#0f172a">D</text><text x="28" y="87" text-anchor="middle" fill="#0f172a">A′</text><text x="180" y="80" text-anchor="middle" fill="#0f172a">B′</text><text x="236.6" y="36.4" text-anchor="middle" fill="#0f172a">C′</text><text x="83.6" y="31.4" text-anchor="middle" fill="#0f172a">D′</text></g></svg>
:::

Sur la figure, le seul plan qui contient (AB) et le point C est celui de la base ; il ne contient pas C′, donc il ne contient pas (CC′).

::: exemple Trois paires de droites du cube ABCDA′B′C′D′

1. (AB) et (A′B′) : toutes deux dans la face ABB′A′, qui est un carré, et sans point commun : elles sont parallèles, comme deux côtés opposés d'un carré.
2. (CD) et (CD′) : toutes deux dans la face CDD′C′, avec le point C en commun : elles sont sécantes en C.
3. (AB) et (CC′) : sans point commun, car (CC′) ne rencontre le plan de la base qu'en C et C n'est pas sur (AB). Le seul plan contenant (AB) et C est celui de la base, qui ne contient pas C′ : elles sont non coplanaires.

:::

::: piege Dire que deux droites sans point commun sont parallèles
Un élève voit que (AB) et (CC′) ne se coupent pas et écrit « elles sont parallèles ». Cela tente parce que, dans un plan, ne pas se couper veut dire être parallèles.
Mais dans l'espace il existe une troisième possibilité : les droites non coplanaires. Deux droites sont parallèles si elles sont dans un même plan et sans point commun.
:::

::: propriete

| Position            | Dans un même plan ? | Points communs  |
| ------------------- | ------------------- | --------------- |
| Sécantes            | oui                 | un seul         |
| Parallèles distinctes | oui               | aucun           |
| Confondues          | oui                 | toute la droite |
| Non coplanaires     | non                 | aucun           |

Cas limite : deux droites confondues sont coplanaires, et leur intersection est toute la droite.
:::

::: methode Décider de la position de deux droites

1. Chercher un point commun : un seul, les droites sont sécantes ; plusieurs, elles sont confondues.
2. Sinon, chercher un plan qui les contient toutes les deux, comme une face ou le plan défini par l'une et un point de l'autre : s'il existe, elles sont parallèles.
3. Si aucun plan ne convient, elles sont non coplanaires.
:::

::: verifie
Dans le même cube, quelle est la position de (BC) et de (AA′) ?

---

Elles n'ont aucun point commun : (AA′) ne rencontre le plan de la base qu'en A, et A n'est pas sur (BC). Le seul plan contenant (BC) et A est la base, qui ne contient pas A′ : les droites sont non coplanaires.
:::

::: retenir
Deux droites de l'espace sont sécantes, parallèles, confondues ou non coplanaires ; sans point commun ne veut pas dire parallèles.
:::

## 🎯 Droite et plan : quand une droite perce un plan

Une aiguille traverse un morceau de tissu : un point commun, un seul. Dans un tétraèdre, la droite (IG) semble flotter à côté de la face (BCD) sans la toucher.
Perce-t-elle quand même le plan (BCD), et où ? Un plan est illimité : il continue bien au-delà du triangle dessiné.

::: definition
Une droite et un plan sont **sécants** lorsqu'ils ont un seul point commun : on dit que la droite **perce** le plan en ce point, ou que le plan **coupe** la droite.
Les deux autres positions sont : la droite est contenue dans le plan (toute la droite est commune), ou la droite et le plan n'ont aucun point commun.
:::

::: figure Le tétraèdre ABCD, avec I milieu de [AB], J milieu de [CD] et G centre de gravité de ACD : la droite (IG) coupe (BJ) en E, hors du triangle BCD mais dans son plan
<svg viewBox="62 -29 244 270"><path d="M280 215 L220.8 159 L240 53.4 Z" fill="#0f6e56" opacity="0.1"/><path d="M280 215 L220.8 159" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M88 215 L220.8 159" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M220.8 159 L240 53.4" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M88 215 L280 215" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M280 215 L240 53.4" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M88 215 L240 53.4" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M280 215 L217.2 77.2" fill="none" stroke="#0f6e56" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M217.2 77.2 L180.8 -2.6" fill="none" stroke="#0f6e56" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/><path d="M184 215 L182.5 114.4" fill="none" stroke="#b45309" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M182.5 114.4 L180.8 -2.6" fill="none" stroke="#b45309" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/><path d="M88 215 L230.4 106.2" fill="none" stroke="#94a3b8" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><g fill="#0f172a"><circle cx="88" cy="215" r="3.8"/><circle cx="280" cy="215" r="3.8"/><circle cx="220.8" cy="159" r="3.8"/><circle cx="240" cy="53.4" r="3.8"/><circle cx="184" cy="215" r="3.8"/><circle cx="230.4" cy="106.2" r="3.8"/><circle cx="182.9" cy="142.5" r="3.8"/></g><g fill="#b45309"><circle cx="180.8" cy="-2.6" r="4.6"/></g><g font-size="15" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="77" y="227" text-anchor="middle" fill="#0f172a">A</text><text x="291" y="229" text-anchor="middle" fill="#0f172a">B</text><text x="208.8" y="155" text-anchor="middle" fill="#0f172a">C</text><text x="240" y="43.4" text-anchor="middle" fill="#0f172a">D</text><text x="182" y="232" text-anchor="middle" fill="#0f172a">I</text><text x="242.4" y="109.2" text-anchor="middle" fill="#0f6e56">J</text><text x="171.9" y="138.5" text-anchor="middle" fill="#b45309">G</text><text x="179.8" y="-13.6" text-anchor="middle" fill="#b45309">E</text></g></svg>
:::

Sur la figure, la droite (BJ) est dans le plan (BCD), et E est le point où (IG) la coupe : c'est là que (IG) perce le plan (BCD), même si E est loin du triangle dessiné.

::: exemple Où la droite (IG) perce-t-elle le plan (BCD) ?

1. G est sur la médiane [AJ] du triangle ACD. Le plan (ABJ) contient I, car I est sur (AB), et G, car G est sur (AJ) (axiome 2) : les droites (IG) et (BJ) sont dans un même plan.
2. Dans le triangle ABJ, I est le milieu de [AB] et G est aux deux tiers de [AJ] : AI/AB = 1/2 et AG/AJ = 2/3 sont différents, donc (IG) n'est pas parallèle à (BJ), d'après Thalès (axiome 4). Elles se coupent en un point E.
3. E est sur (BJ), et (BJ) ⊂ (BCD) car B et J sont dans (BCD), J étant sur (CD). Donc E ∈ (BCD).
4. (IG) n'est pas contenue dans (BCD) : I, sur (AB) et distinct de B, n'y est pas, sinon A y serait aussi. Le point commun est unique : (IG) perce (BCD) en E.

:::

::: piege Chercher le point d'intersection dans la face dessinée
Un élève constate que (IG) ne traverse pas le triangle BCD du dessin et conclut qu'elle ne perce pas le plan. Cela tente parce qu'on prend « le plan » pour la face dessinée.
Mais le plan (BCD) est illimité : E est en dehors du triangle, sur le prolongement de [BJ] au-delà de J, et il est bien dans le plan.
:::

::: methode Trouver le point où une droite D perce un plan P

1. Choisir dans P une droite Δ qui est dans un même plan que D : un plan auxiliaire, souvent défini par D et un point de Δ.
2. Dans ce plan auxiliaire, chercher le point E où D et Δ se coupent.
3. Conclure : E est sur D et sur Δ ⊂ P, donc c'est un point commun ; D perce P en E si D n'est pas contenue dans P.

Cas limite : si D est contenue dans P, toute la droite est commune et il n'y a pas de point unique à chercher.
:::

::: verifie
Dans un tétraèdre ABCD, I est sur (AB) et J sur (AC), distincts de A, B et C, et (IJ) coupe (BC) en L. En quel point (IJ) perce-t-elle le plan (BCD) ?

---

En L. Ce point est sur (IJ) et sur (BC), qui est contenue dans (BCD) : c'est un point commun. De plus (IJ) n'est pas contenue dans (BCD), car I, sur (AB) et distinct de B, n'est pas dans (BCD). Le point commun est donc unique : (IJ) perce (BCD) en L.
:::

::: retenir
Une droite et un plan sont sécants, ou la droite est contenue dans le plan, ou ils n'ont aucun point commun ; pour trouver le point de percée, on coupe la droite avec une droite du plan située dans un même plan qu'elle.
:::

## ✂️ Deux plans : sécants suivant une droite

Un livre ouvert pose deux pages dans deux plans qui se rejoignent au dos ; deux murs d'une pièce se rejoignent le long d'une arête verticale. Deux plans qui se rencontrent partagent donc toute une droite.
Comment tracer cette droite dans un tétraèdre, où on ne la voit pas ?

::: definition
Deux plans sont **sécants** lorsque leur intersection est une droite. Les autres positions sont : les plans **confondus**, qui ont tous leurs points en commun, et les plans sans aucun point commun.
D'après l'axiome 3, deux plans distincts qui ont un point commun sont sécants.
:::

::: figure Dans le tétraèdre ABCD, les plans (AID) en vert et (ABJ) en orange ont en commun le point A et le point M, où (BJ) coupe (DI) : leur intersection est la droite (AM)
<svg viewBox="0 10 340 235"><path d="M44 222 L236.8 188.8 L224.5 30.1 Z" fill="#0f6e56" opacity="0.1"/><path d="M44 222 L272 222 L213.1 92.8 Z" fill="#b45309" opacity="0.1"/><path d="M272 222 L201.7 155.5" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M44 222 L201.7 155.5" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M201.7 155.5 L224.5 30.1" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M44 222 L272 222" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M272 222 L224.5 30.1" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M44 222 L224.5 30.1" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M272 222 L213.1 92.8" fill="none" stroke="#b45309" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M224.5 30.1 L236.8 188.8" fill="none" stroke="#0f6e56" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M44 222 L232.7 135.9" fill="none" stroke="#0f172a" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><g fill="#0f172a"><circle cx="44" cy="222" r="3.8"/><circle cx="272" cy="222" r="3.8"/><circle cx="201.7" cy="155.5" r="3.8"/><circle cx="224.5" cy="30.1" r="3.8"/><circle cx="236.8" cy="188.8" r="3.8"/><circle cx="213.1" cy="92.8" r="3.8"/></g><g fill="#0f172a"><circle cx="232.7" cy="135.9" r="4.6"/></g><g font-size="15" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="33" y="234" text-anchor="middle" fill="#0f172a">A</text><text x="283" y="236" text-anchor="middle" fill="#0f172a">B</text><text x="189.7" y="151.5" text-anchor="middle" fill="#0f172a">C</text><text x="224.5" y="20.1" text-anchor="middle" fill="#0f172a">D</text><text x="248.8" y="194.8" text-anchor="middle" fill="#0f172a">I</text><text x="226.1" y="90.8" text-anchor="middle" fill="#0f172a">J</text><text x="226.7" y="153.9" text-anchor="middle" fill="#0f172a">M</text></g></svg>
:::

Sur la figure, (DI) est dans le plan vert (AID) et (BJ) dans le plan orange (ABJ) ; leur point commun M est donc dans les deux plans.

::: exemple L'intersection des plans (AID) et (ABJ)
Dans le tétraèdre ABCD, I est un point de [BC] et J un point de [CD], distincts des sommets, et M est le point d'intersection de (BJ) et (DI) dans le plan (BCD).

1. A appartient aux deux plans, puisque c'est un point de (AID) et de (ABJ).
2. M est sur (BJ), contenue dans (ABJ), et sur (DI), contenue dans (AID) (axiome 2) : M est dans les deux plans.
3. A et M sont distincts, car M est dans (BCD) et pas A. Les deux plans sont distincts : B est dans (ABJ) mais pas dans (AID), sinon ce plan contiendrait D, B et I, donc (BI) = (BC) et C, et les quatre sommets seraient coplanaires. Ils contiennent tous deux la droite (AM) par l'axiome 2 : leur intersection est exactement (AM).

:::

::: piege Tracer l'intersection avec un seul point commun
Un élève trouve le point commun A et trace « l'intersection » dans une direction quelconque. Cela tente parce que l'axiome 3 dit que l'intersection passe par ce point.
Mais passer par un point ne fixe pas une droite : il en faut deux, A et M, pour la tracer.
:::

::: methode Trouver l'intersection de deux plans

1. Trouver un premier point commun, souvent un sommet que les deux plans contiennent.
2. Trouver un second point commun, distinct du premier : le point où une droite de l'un coupe une droite de l'autre, quand elles sont dans un même plan.
3. Tracer la droite qui passe par ces deux points : c'est l'intersection.
:::

::: propriete
Des points communs à deux plans distincts sont alignés, puisqu'ils sont tous sur la droite d'intersection.
Cas limite : si deux plans ont trois points communs non alignés, ils sont confondus, d'après l'axiome 1.
:::

::: verifie
Dans un tétraèdre ABCD, I est sur [BC] et J sur [AC], distincts des extrémités. Quelle est l'intersection des plans (ACI) et (BDJ) ?

---

Le plan (ACI) est le plan (ABC) : il contient C et I, donc la droite (CI) = (BC), donc B. Les points B et J sont communs aux deux plans : B est dans (ABC) et dans (BDJ), et J, sur (AC), est dans (ABC) et dans (BDJ). Les deux plans sont distincts, donc leur intersection est la droite (BJ).
:::

::: retenir
Deux plans sont sécants suivant une droite, confondus ou sans point commun ; pour tracer leur intersection il faut deux points communs, et des points communs à deux plans sont alignés.
:::

> 🏆 Quête franchie, héros : tu sais compter les faces, arêtes et sommets d'un solide, mesurer un pavé et un cube, appliquer les axiomes, désigner un plan de trois façons, décider si des points sont coplanaires, et trouver la position de deux droites, d'une droite et d'un plan, de deux plans. Les chapitres suivants ouvrent sur le parallélisme dans l'espace.
