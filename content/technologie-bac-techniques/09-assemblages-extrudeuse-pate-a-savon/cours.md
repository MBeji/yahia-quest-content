# 🧼 La boudineuse : un réducteur, des assemblages, un œil de technicien

> 💡 « Une machine tourne parce que ses pièces ont le droit de bouger, et elle tient parce qu'on leur interdit tout le reste. Assembler, c'est décider, pièce par pièce, ce qui est permis et ce qui est interdit. »

Ce chapitre ouvre le thème des assemblages avec une machine de savonnerie : l'**extrudeuse de pâte à savon**, appelée aussi **boudineuse**, qui façonne le savon en barres. Autour de son moteur électrique, on trouve une trémie d'alimentation, un fourreau qui contient la vis d'extrusion, un cône d'extrusion et un nez de sortie (la filière). Un module retient toute notre attention : le **réducteur à roue et vis sans fin**. Son nom dit sa fonction globale : il transmet une rotation en la ralentissant. Son corps est formé de deux **demi-carters**, le carter inférieur (4) et le carter supérieur (8), fixés par des boulons ; à l'intérieur, la **vis sans fin** (1), à 1 filet, engrène avec la **roue creuse** (9), à 40 dents, et les arbres sont guidés par des roulements.

Le chapitre suit les trois activités du manuel : comment tiennent les deux carters ? comment fixer la roue sur son arbre et la régler ? que faire quand les roulements de la vis s'usent ? Il commence par la lecture du plan et finit par le dessin de la solution.

## 🔎 Lire la nomenclature : quantités, pièces achetées, matières

Un technicien reçoit le dessin d'ensemble du réducteur et sa nomenclature de 28 repères. Trois questions pressantes : combien de pièces de chaque sorte, lesquelles s'achètent sur catalogue, en quelle matière est le carter ? 

Les réponses sont dans les colonnes, encore faut-il savoir les lire.

::: definition La nomenclature
Chaque ligne décrit un **repère** du dessin : son numéro (**Rep.**), le nombre d'exemplaires (**Nbr.**), sa **désignation**, sa **matière** et une **observation**. L'observation « **Standard** » signale un **composant normalisé** : on l'achète sur catalogue, on ne le fabrique pas.
:::

| Rep. | Nbr. | Désignation | Matière | Observation |
| --- | --- | --- | --- | --- |
| 4 | 1 | Carter inférieur | EN AB-43 000 | |
| 5 | 2 | Pied de positionnement | S 275 | |
| 9 | 1 | Roue creuse | Cu Sn 12 | Z9 = 40 dents |
| 12 | 2 | Roulement à rouleaux coniques | | Standard |
| 13 | 1 | Couvercle | EN AB-43 000 | |
| 15 | 6 | Écrou | | Standard |
| 18 | 1 | Couvercle | EN AB-43 000 | |
| 23 | 1 | Couvercle | EN AB-43 000 | |

La colonne Nbr. donne la quantité : le repère 5 compte 2 pièces, que le dessin ne montre pas forcément toutes.

::: exemple Trois réponses lues dans la nomenclature
1. **Combien de pieds de positionnement ?** Repère 5, colonne Nbr. : **2**. ← la quantité est écrite, on ne la compte pas sur le dessin.
2. **Peut-on commander le roulement (12) sur catalogue ?** Son observation est « Standard » : **oui**. ← un composant normalisé s'achète.
3. **Combien de couvercles simples ?** Trois lignes portent cette désignation, (13), (18) et (23), à 1 exemplaire chacune : 1 + 1 + 1 = **3**. ← on additionne toutes les lignes de même désignation.

:::

La colonne Matière se déchiffre aussi :

| Désignation | Ce qu'elle dit | Où on la lit |
| --- | --- | --- |
| **EN AB-43 000** | alliage d'**aluminium de fonderie** : la pièce est coulée dans un moule | carters (4) et (8), couvercles (13), (18), (23) |
| **EN AW-2017**, observation « Corroyé » | alliage d'aluminium **corroyé** : travaillé à l'état solide (laminé, forgé, filé), non moulé | couvercle creux (3) |
| **Cu Sn 12** | **bronze** : cuivre allié à environ 12 % d'étain | roue creuse (9) |
| **S 275** | acier non allié d'usage général, 275 MPa de limite d'élasticité minimale | pieds de positionnement (5) |
| **C 45** | acier non allié à 0,45 % de carbone | clavette (7) |
| **42 Cr Mo 4** | acier faiblement allié : 0,42 % de carbone, environ 1 % de chrome, du molybdène | arbre (6) |

::: piege Corroyé n'est pas corrodé
Le mot « corroyé » ressemble à « corrosion », et la situation de départ du manuel parle justement de corrosion. ✗ « Corroyé : la pièce est protégée contre la rouille. » ✓ Corroyé parle de **fabrication**, pas de protection : un métal corroyé a été travaillé à l'état solide, un métal de fonderie a été coulé. La protection contre la corrosion est un autre sujet.
:::

::: verifie
Dans la nomenclature, le repère 15 « Écrou » a pour quantité 6, et le repère 22 « Écrou » pour quantité 1. Combien d'écrous le réducteur compte-t-il au total ?

---

Deux lignes portent la désignation « Écrou » : on additionne leurs quantités, 6 + 1 = **7**. On ne s'arrête pas à la première ligne trouvée.
:::

::: retenir
Nbr. donne la quantité, « Standard » signale une pièce achetée, et une désignation de matière se déchiffre : EN AB = fonderie, EN AW « corroyé » = travaillé par déformation, Cu Sn = bronze.
:::

## 🔩 Interdire des mouvements : liaison complète ou partielle

Soulève le carter supérieur (8) : il s'enlève. Repose-le sans rien visser : il reste assis sur le carter inférieur (4), mais glisse au moindre choc. Visse-le avec ses pieds et ses boulons : plus rien ne bouge. D'une situation à l'autre, la pièce n'a pas changé, c'est ce qu'on lui **interdit** qui a changé.

Combien de mouvements une pièce libre peut-elle faire, et lesquels interdit-on ici ?

::: definition Mobilités et liaison
Une pièce libre dans l'espace dispose de **six mobilités** : trois **translations** (Tx, Ty, Tz) et trois **rotations** (Rx, Ry, Rz) autour des axes x, y et z. Un **assemblage** lie des pièces en **supprimant** des mobilités. Si les six sont supprimées (**0 degré de mobilité**), la liaison est **complète** ; s'il en reste au moins une, elle est **partielle** (pivot, glissière, hélicoïdale). Une liaison complète est **démontable** quand on peut la défaire sans détériorer les pièces ni les éléments de liaison.
:::

::: figure Coupe schématique des deux demi-carters (schéma de principe, pas le dessin du manuel). Le trait vert est le plan de joint, où les carters s'appuient l'un sur l'autre ; z en est la normale, x et y sont dans le plan (y entre dans la feuille). Les deux pieds (5) traversent le plan, les boulons (14), (15), (28) pressent les carters
<svg viewBox="0 0 520 280"><rect x="60" y="70" width="340" height="80" fill="#e2e8f0" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="60" y="150" width="340" height="80" fill="#e2e8f0" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><circle cx="230" cy="150" r="34" fill="#ffffff" stroke="#0f172a" stroke-width="2"/><path d="M60 150 L196 150" fill="none" stroke="#0f6e56" stroke-width="4.5"/><path d="M264 150 L400 150" fill="none" stroke="#0f6e56" stroke-width="4.5"/><rect x="112" y="126" width="12" height="48" fill="#334155" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="336" y="126" width="12" height="48" fill="#334155" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="77" y="70" width="10" height="176" fill="#cbd5e1" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round"/><rect x="68" y="54" width="28" height="16" fill="#94a3b8" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="66" y="230" width="32" height="5" fill="#64748b" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round"/><rect x="68" y="235" width="28" height="16" fill="#94a3b8" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="373" y="70" width="10" height="176" fill="#cbd5e1" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round"/><rect x="364" y="54" width="28" height="16" fill="#94a3b8" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="362" y="230" width="32" height="5" fill="#64748b" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round"/><rect x="364" y="235" width="28" height="16" fill="#94a3b8" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><text x="160" y="104" font-size="13" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">(8)</text><text x="160" y="204" font-size="13" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">(4)</text><text x="342" y="118" font-size="12.5" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">(5)</text><text x="40" y="64" font-size="12" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">(14)</text><text x="40" y="246" font-size="12" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">(15)</text><text x="40" y="222" font-size="12" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">(28)</text><path d="M52 60 L68 60" fill="none" stroke="#94a3b8" stroke-width="1"/><path d="M52 243 L68 243" fill="none" stroke="#94a3b8" stroke-width="1"/><path d="M52 219 L66 231" fill="none" stroke="#94a3b8" stroke-width="1"/><text x="300" y="143" font-size="10.5" font-weight="700" text-anchor="middle" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">plan de joint</text><circle cx="452" cy="196" r="7" fill="#ffffff" stroke="#0f172a" stroke-width="2"/><path d="M447.5 191.5 L456.5 200.5" fill="none" stroke="#0f172a" stroke-width="1.8"/><path d="M447.5 200.5 L456.5 191.5" fill="none" stroke="#0f172a" stroke-width="1.8"/><path d="M459 196 L487.0 196.0" fill="none" stroke="#0f172a" stroke-width="2.2"/><polygon points="496.0,196.0 487.0,199.8 487.0,192.2" fill="#0f172a" stroke="#0f172a" stroke-width="0" stroke-linejoin="round"/><path d="M452 189 L452.0 161.0" fill="none" stroke="#0f172a" stroke-width="2.2"/><polygon points="452.0,152.0 455.8,161.0 448.2,161.0" fill="#0f172a" stroke="#0f172a" stroke-width="0" stroke-linejoin="round"/><text x="505" y="200" font-size="13" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x</text><text x="452" y="146" font-size="13" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">z</text><text x="438" y="214" font-size="13" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">y</text></svg>
:::

Sur la figure, l'axe z est perpendiculaire au trait vert du plan de joint ; c'est lui qui sert de repère pour compter.

::: exemple Que supprime l'appui plan entre (4) et (8) ?
1. **Translation selon z** : (8) ne peut pas s'enfoncer dans (4), donc **Tz** est supprimée dans ce sens. ← le plan de joint barre le passage dans la direction de sa normale. Le sens inverse, s'écarter, n'est pas interdit par la forme : ce sont les boulons qui l'interdisent, en pressant (MAP).
2. **Rotations autour de x et de y** : basculer (8) sur un bord ferait entrer l'autre bord dans (4), donc **Rx** et **Ry** sont supprimées. ← un appui plan interdit de se pencher.
3. **Mouvements dans le plan** : (8) peut glisser selon x et selon y et tourner autour de z, comme une assiette sur une nappe : **Tx, Ty, Rz** restent libres. ← glisser sur un plan ne le traverse pas.
4. **Bilan** : 3 supprimées, 3 libres, donc l'appui plan seul ne donne qu'une liaison partielle.

:::

::: piege Démontable ne veut pas dire partielle
« On peut démonter les carters, donc la liaison est partielle » ✗. Les deux mots ne mesurent pas la même chose : **complète** ou **partielle** compte les mobilités qui restent ; **démontable** dit seulement qu'on peut défaire l'assemblage sans rien détériorer. Les carters assemblés n'ont plus aucune mobilité (liaison complète) et se démontent pourtant sans casse.
:::

::: methode Analyser une liaison
1. Nommer la nature des surfaces en contact : plane, cylindrique.
2. Compter les mobilités que ces surfaces suppriment seules, éléments de position retirés.
3. Ajouter celles que suppriment les éléments de position, pieds par exemple.
4. Classer chaque élément en MIP ou en MAP.
:::

::: verifie
Deux plaques sont en appui plan l'une sur l'autre, mais le plan de contact est cette fois perpendiculaire à y. Quelles mobilités cet appui supprime-t-il ?

---

La normale au plan est y : l'appui supprime la translation selon cette normale, **Ty**, et les deux rotations autour des axes du plan, x et z, soit **Rx** et **Rz**. Restent libres Tx et Tz (glissement) et Ry (rotation autour de la normale) : 3 supprimées, 3 libres.
:::

::: retenir
Six mobilités possibles ; liaison complète = aucune mobilité restante ; un appui plan en supprime trois : la translation normale et les deux rotations autour d'axes du plan.
:::

## 📌 Mettre en position, maintenir en position : pieds et boulons

Le plan de joint laisse trois mobilités libres (Tx, Ty, Rz). Pourtant, une fois le réducteur monté, rien ne glisse ni ne tourne. Et après chaque démontage, les carters doivent retrouver exactement la même place.

Qui interdit les trois mobilités restantes, et qui garde les carters plaqués l'un contre l'autre ?

::: definition MIP et MAP
La **mise en position (MIP)** place une pièce par rapport à une autre grâce à des surfaces (planes, cylindriques, coniques) ou à des éléments de centrage. Le **maintien en position (MAP)** conserve le contact entre les pièces ainsi positionnées, par un obstacle démontable ou par l'adhérence que crée le serrage.
:::

| Élément | Rôle | Mobilités concernées |
| --- | --- | --- |
| Appui plan des deux carters | MIP | Tz, Rx, Ry |
| Deux pieds de positionnement (5) | MIP | Tx, Ty, Rz |
| Boulons : vis (14) + écrou (15) + rondelle (28), 6 de chaque | MAP | aucune par leur forme : en pressant, ils interdisent au carter de s'écarter |

Un **boulon** est une vis et son écrou (ici avec une rondelle sous l'écrou) : la vis traverse les deux carters, l'écrou la serre de l'autre côté. Le tableau relie chaque élément de la figure précédente à son rôle.

::: figure Une note du dessin d'ensemble dit que le pied (5) est « ramené dans le plan de coupe ». Le plan de coupe B-B ne passe pas par lui ; pour qu'il soit visible sur la coupe, on le représente comme s'il avait tourné autour du centre de la vue jusqu'à tomber dans ce plan. Sa distance au centre ne change pas, et sur la machine il reste à sa place
<svg viewBox="0 0 540 250"><circle cx="140" cy="125" r="92" fill="#e2e8f0" stroke="#0f172a" stroke-width="2"/><circle cx="140" cy="125" r="22" fill="#ffffff" stroke="#0f172a" stroke-width="2"/><path d="M22 125 L258 125" fill="none" stroke="#0f172a" stroke-width="2.2" stroke-dasharray="14 4 3 4"/><path d="M34 125 L34.0 104.0" fill="none" stroke="#0f172a" stroke-width="2.4"/><polygon points="34.0,95.0 37.8,104.0 30.2,104.0" fill="#0f172a" stroke="#0f172a" stroke-width="0" stroke-linejoin="round"/><path d="M246 125 L246.0 104.0" fill="none" stroke="#0f172a" stroke-width="2.4"/><polygon points="246.0,95.0 249.8,104.0 242.2,104.0" fill="#0f172a" stroke="#0f172a" stroke-width="0" stroke-linejoin="round"/><text x="34" y="87" font-size="14" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">B</text><text x="246" y="87" font-size="14" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">B</text><circle cx="179.9" cy="77.5" r="9" fill="#334155" stroke="#0f172a" stroke-width="2"/><text x="179.9" y="61.5" font-size="12.5" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">(5)</text><path d="M187.5 85.1 A62 62 0 0 1 201.4 116.4" fill="none" stroke="#0f6e56" stroke-width="2.4" stroke-dasharray="6 4"/><circle cx="202" cy="125" r="9" fill="#ffffff" stroke="#0f6e56" stroke-width="2"/><text x="140" y="226" font-size="11.5" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">vue de dessus</text><path d="M272 125 L317.0 125.0" fill="none" stroke="#0f6e56" stroke-width="2.4"/><polygon points="326.0,125.0 317.0,128.8 317.0,121.2" fill="#0f6e56" stroke="#0f172a" stroke-width="0" stroke-linejoin="round"/><text x="299" y="115" font-size="11" font-weight="700" text-anchor="middle" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">ramené</text><rect x="340" y="70" width="170" height="110" fill="#e2e8f0" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="398" y="70" width="54" height="110" fill="#ffffff" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="480" y="92" width="14" height="70" fill="#334155" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><text x="487" y="84" font-size="12.5" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">(5)</text><text x="425" y="204" font-size="11.5" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">coupe B-B</text></svg>
:::


Le pied est donc dessiné là où le plan de coupe le rend lisible, pas forcément là où il se trouve sur la machine : il n'a pas bougé.
La mention « ramené dans le plan de coupe » prévient le lecteur de cette convention.

::: verifie
Le pied (5) apparaît sur la coupe B-B alors que le plan de coupe ne passe pas par lui. Se trouve-t-il ailleurs sur la machine que sur la vue de dessus ?

---

Non : la mention « ramené dans le plan de coupe » indique une convention de dessin. Le pied est représenté comme s'il avait tourné jusqu'à tomber dans le plan, mais sur la machine il reste à sa place, celle qu'on lit sur la vue de dessus.
:::

::: exemple Pourquoi deux pieds et pas un ?
1. **Un seul pied** : un cylindre ajusté dans un trou de chaque carter interdit tout glissement dans le plan, donc **Tx** et **Ty** sont supprimées. ← il ne peut plus aller ni à droite ni en avant.
2. **Reste Rz** : le carter supérieur peut encore pivoter autour de ce pied, comme une porte autour de son axe. ← le pied est lui-même l'axe de cette rotation.
3. **Second pied, écarté du premier** : pour pivoter autour du premier, le second devrait décrire un arc, mais il est lui aussi ajusté dans son trou, donc **Rz** est supprimée. ← deux appuis écartés bloquent la rotation qu'un seul laisse libre.
4. **Bilan** : 3 (plan) + 2 + 1 = 6 mobilités supprimées : liaison complète.

:::

::: piege Les boulons ne positionnent pas
« Les boulons sont serrés, ils interdisent donc aussi le glissement : les pieds sont inutiles » ✗. Une vis traverse un trou plus large qu'elle, sinon on ne pourrait pas la monter : elle n'impose aucune position. Les boulons **pressent** les carters l'un contre l'autre (MAP) ; ce sont les pieds qui imposent la position (MIP) et la font retrouver à chaque remontage.
:::

::: verifie
Classe chacun de ces éléments en MIP ou en MAP : l'écrou (15), l'un des deux pieds (5), la rondelle (28).

---

Le pied (5) est un cylindre ajusté dans son trou : il impose la position, c'est de la **MIP**. L'écrou (15) et la rondelle (28) font partie du boulon, qui presse les carters l'un contre l'autre : c'est du **MAP**.
:::

::: retenir
MIP = imposer la position (appui plan, pieds ajustés) ; MAP = garder le contact (boulons, par serrage). Un boulon = une vis + son écrou.
:::

## 🛞 La roue creuse sur son arbre : lier, bloquer, régler

Sur l'arbre (6), la roue creuse (9) doit tourner avec lui sans glisser le long de lui. Cela ne suffit pas : pour que ses dents portent correctement sur le filet de la vis sans fin (1), on doit aussi pouvoir **régler** sa position le long de l'arbre.

Comment écrit-on ce cahier des charges, et quelles pièces le réalisent ?

::: definition Le F.A.S.T. partiel d'un assemblage
Pour la liaison encastrement de la roue creuse (9) sur l'arbre (6), le **F.A.S.T. partiel** place sous la fonction « assemblage roue creuse / arbre » deux **fonctions techniques** : **lier en rotation** et **lier en translation**. En face de chacune, il écrit la **solution constructive** qui la réalise.
:::

| Fonction technique | Solution constructive |
| --- | --- |
| Lier en rotation | clavette parallèle (7) + rainures (dans l'arbre et dans la roue) |
| Lier en translation | à choisir : bloquer la roue et permettre de régler sa position |

La colonne de gauche dit ce qu'il faut faire ; celle de droite dit avec quelle pièce ou quelle forme.

Le réglage met en jeu des **cales** : de minces plaques d'épaisseur calibrée, que l'on ajoute ou que l'on retire. Les roulements à rouleaux coniques (12) et (12') ont un **jeu interne**, petit déplacement relatif de leurs bagues, qui se règle aussi par l'épaisseur des cales.

::: figure Disposition de principe supposée : les cales (27) et (27') sont placées de part et d'autre, entre les couvercles et les roulements (12) et (12'). Déplacer de l'épaisseur d'un côté à l'autre décale l'arbre (6) et la roue (9) sans changer l'épaisseur totale ; la clavette (7) lie la roue à l'arbre en rotation. Schéma de principe
<svg viewBox="0 0 540 240"><rect x="60" y="56" width="34" height="44" fill="#e2e8f0" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="60" y="124" width="34" height="56" fill="#e2e8f0" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="446" y="56" width="34" height="44" fill="#e2e8f0" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="446" y="124" width="34" height="56" fill="#e2e8f0" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="98" y="70" width="4" height="30" fill="#0f6e56" stroke="#0f172a" stroke-width="0.8" stroke-linejoin="round"/><rect x="98" y="124" width="4" height="30" fill="#0f6e56" stroke="#0f172a" stroke-width="0.8" stroke-linejoin="round"/><rect x="420" y="70" width="4" height="30" fill="#0f6e56" stroke="#0f172a" stroke-width="0.8" stroke-linejoin="round"/><rect x="420" y="124" width="4" height="30" fill="#0f6e56" stroke="#0f172a" stroke-width="0.8" stroke-linejoin="round"/><rect x="105" y="70" width="4" height="30" fill="#0f6e56" stroke="#0f172a" stroke-width="0.8" stroke-linejoin="round"/><rect x="105" y="124" width="4" height="30" fill="#0f6e56" stroke="#0f172a" stroke-width="0.8" stroke-linejoin="round"/><rect x="413" y="70" width="4" height="30" fill="#0f6e56" stroke="#0f172a" stroke-width="0.8" stroke-linejoin="round"/><rect x="413" y="124" width="4" height="30" fill="#0f6e56" stroke="#0f172a" stroke-width="0.8" stroke-linejoin="round"/><rect x="112" y="70" width="4" height="30" fill="#0f6e56" stroke="#0f172a" stroke-width="0.8" stroke-linejoin="round"/><rect x="112" y="124" width="4" height="30" fill="#0f6e56" stroke="#0f172a" stroke-width="0.8" stroke-linejoin="round"/><rect x="406" y="70" width="4" height="30" fill="#0f6e56" stroke="#0f172a" stroke-width="0.8" stroke-linejoin="round"/><rect x="406" y="124" width="4" height="30" fill="#0f6e56" stroke="#0f172a" stroke-width="0.8" stroke-linejoin="round"/><rect x="130" y="76" width="38" height="24" fill="#dbeafe" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="130" y="124" width="38" height="24" fill="#dbeafe" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="372" y="76" width="38" height="24" fill="#dbeafe" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="372" y="124" width="38" height="24" fill="#dbeafe" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="240" y="58" width="60" height="42" fill="#d1e7df" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="240" y="124" width="60" height="42" fill="#d1e7df" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><path d="M244 50 L244 58" fill="none" stroke="#0f172a" stroke-width="2"/><path d="M244 166 L244 174" fill="none" stroke="#0f172a" stroke-width="2"/><path d="M254 50 L254 58" fill="none" stroke="#0f172a" stroke-width="2"/><path d="M254 166 L254 174" fill="none" stroke="#0f172a" stroke-width="2"/><path d="M264 50 L264 58" fill="none" stroke="#0f172a" stroke-width="2"/><path d="M264 166 L264 174" fill="none" stroke="#0f172a" stroke-width="2"/><path d="M274 50 L274 58" fill="none" stroke="#0f172a" stroke-width="2"/><path d="M274 166 L274 174" fill="none" stroke="#0f172a" stroke-width="2"/><path d="M284 50 L284 58" fill="none" stroke="#0f172a" stroke-width="2"/><path d="M284 166 L284 174" fill="none" stroke="#0f172a" stroke-width="2"/><path d="M294 50 L294 58" fill="none" stroke="#0f172a" stroke-width="2"/><path d="M294 166 L294 174" fill="none" stroke="#0f172a" stroke-width="2"/><rect x="70" y="100" width="400" height="24" fill="#cbd5e1" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="253" y="95" width="34" height="9" fill="#334155" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round"/><text x="111" y="52" font-size="12.5" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">(27)</text><text x="409" y="52" font-size="12.5" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">(27')</text><text x="149" y="64" font-size="12.5" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">(12)</text><text x="391" y="64" font-size="12.5" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">(12')</text><text x="270" y="40" font-size="12.5" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">(9)</text><text x="270" y="88" font-size="12" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">(7)</text><text x="190" y="116" font-size="12.5" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">(6)</text><path d="M118 198 L389.0 198.0" fill="none" stroke="#0f6e56" stroke-width="2"/><polygon points="398.0,198.0 389.0,201.8 389.0,194.2" fill="#0f6e56" stroke="#0f172a" stroke-width="0" stroke-linejoin="round"/><path d="M402 198 L131.0 198.0" fill="none" stroke="#0f6e56" stroke-width="2"/><polygon points="122.0,198.0 131.0,194.2 131.0,201.8" fill="#0f6e56" stroke="#0f172a" stroke-width="0" stroke-linejoin="round"/><text x="260" y="222" font-size="11.5" font-weight="700" text-anchor="middle" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">on déplace de l'épaisseur d'un côté à l'autre</text></svg>
:::


::: exemple Recentrer la roue sans toucher aux roulements
Le contrôle montre que les dents de la roue (9) portent trop d'un côté du filet de la vis.
1. **Cause** : la roue est décalée le long de l'arbre. ← la portée des dents dépend de la position axiale.
2. **Réglage** : on retire une épaisseur de cales du côté (27) et on la remet du côté (27'). ← l'arbre se décale et entraîne la roue qu'il porte.
3. **Contrôle du jeu** : l'épaisseur totale n'a pas changé, donc le jeu interne des roulements non plus. ← c'est l'épaisseur totale, non sa répartition, qui fixe ce jeu.
4. **Résultat** : la position est corrigée, le jeu est intact. Cela demande pourtant de manipuler les deux piles de cales ensemble, et de démonter à chaque essai.

:::

::: piege Régler l'un, c'est dérégler l'autre
« Pour décaler la roue, j'ajoute des cales d'un seul côté » ✗. Les mêmes cales règlent la position de la roue **et** le jeu des roulements : on ne peut pas régler l'un sans agir sur l'autre, et en ajouter d'un seul côté change l'épaisseur totale, donc le jeu. Le manuel parle de « **réglage simultané** » et propose une solution qui sépare les deux réglages.
:::

::: verifie
Pourquoi la clavette (7) ne suffit-elle pas à bloquer la roue (9) le long de l'arbre ?

---

La clavette est logée dans une rainure parallèle à l'axe : elle empêche la roue de tourner par rapport à l'arbre (« lier en rotation »), mais ne s'oppose pas à un glissement le long de l'arbre. Il faut une autre solution constructive pour « lier en translation ».
:::

::: retenir
Une fonction technique se réalise par une solution constructive ; la clavette lie en rotation seulement ; les cales règlent la position axiale et le jeu des roulements : déplacer l'épaisseur d'un côté à l'autre garde le jeu, en ajouter d'un seul côté le change (réglage simultané).
:::

## 🔧 Guider la vis sans fin : choisir le type de roulement

Une inspection par ultrasons repère, sur les roulements (19) qui guident la vis sans fin, une usure du chemin sur lequel roulent les billes. Rien n'est encore cassé : c'est une **défaillance précoce**.

Pourquoi ces roulements s'usent-ils, et par quoi les remplacer ?

::: definition Le guidage en rotation par roulements
Un **guidage en rotation** réalise concrètement une liaison **pivot** : l'arbre ne garde que sa rotation. On le fait avec des **roulements**, généralement montés **par paire**, choisis selon deux critères : les **charges** à supporter et leurs **directions** (radiale, perpendiculaire à l'axe ; axiale, le long de l'axe), et la **vitesse**.
:::

| Type de roulement | Charges supportées | Vitesse |
| --- | --- | --- |
| Billes à contact radial | surtout radiales | — |
| Billes à contact oblique | radiales et axiales importantes | importante |
| Rouleaux coniques | radiales et axiales importantes | moyenne |

::: figure La vis sans fin (1) est guidée par deux roulements (19). L'engrènement avec la roue creuse (9) la charge perpendiculairement à son axe (charge radiale) et la pousse le long de son axe (charge axiale)
<svg viewBox="0 0 520 240"><rect x="60" y="100" width="400" height="24" fill="#cbd5e1" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><polygon points="190.0,100.0 202.0,86.0 214.0,100.0" fill="#d1e7df" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><polygon points="190.0,124.0 202.0,138.0 214.0,124.0" fill="#d1e7df" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><polygon points="214.0,100.0 226.0,86.0 238.0,100.0" fill="#d1e7df" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><polygon points="214.0,124.0 226.0,138.0 238.0,124.0" fill="#d1e7df" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><polygon points="238.0,100.0 250.0,86.0 262.0,100.0" fill="#d1e7df" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><polygon points="238.0,124.0 250.0,138.0 262.0,124.0" fill="#d1e7df" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><polygon points="262.0,100.0 274.0,86.0 286.0,100.0" fill="#d1e7df" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><polygon points="262.0,124.0 274.0,138.0 286.0,124.0" fill="#d1e7df" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><polygon points="286.0,100.0 298.0,86.0 310.0,100.0" fill="#d1e7df" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><polygon points="286.0,124.0 298.0,138.0 310.0,124.0" fill="#d1e7df" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><polygon points="310.0,100.0 322.0,86.0 334.0,100.0" fill="#d1e7df" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><polygon points="310.0,124.0 322.0,138.0 334.0,124.0" fill="#d1e7df" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><rect x="190" y="142" width="144" height="52" fill="#d1e7df" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="96" y="82" width="28" height="60" fill="#dbeafe" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="396" y="82" width="28" height="60" fill="#dbeafe" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><text x="110" y="74" font-size="12.5" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">(19)</text><text x="410" y="74" font-size="12.5" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">(19)</text><text x="262" y="188" font-size="12" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">roue creuse (9)</text><path d="M190 48 L325.0 48.0" fill="none" stroke="#0f6e56" stroke-width="2.6"/><polygon points="334.0,48.0 325.0,51.8 325.0,44.2" fill="#0f6e56" stroke="#0f172a" stroke-width="0" stroke-linejoin="round"/><text x="262" y="38" font-size="12" font-weight="700" text-anchor="middle" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">charge axiale</text><path d="M262 168 L262.0 149.0" fill="none" stroke="#0f6e56" stroke-width="2.6"/><polygon points="262.0,140.0 265.8,149.0 258.2,149.0" fill="#0f6e56" stroke="#0f172a" stroke-width="0" stroke-linejoin="round"/><text x="396" y="172" font-size="12" font-weight="700" text-anchor="middle" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">charge radiale</text></svg>
:::

La nomenclature désigne les roulements (19) comme des roulements à une rangée de billes à contact radial.

::: exemple Critiquer le choix des roulements (19)
1. **Relever le type** : billes à contact radial. ← c'est la désignation de la nomenclature.
2. **Relever les charges** : la roue creuse charge la vis en travers de son axe, mais aussi le long de son axe, et cette charge axiale est importante. ← un engrenage à vis sans fin pousse la vis dans le sens de son axe.
3. **Comparer** : un contact radial convient aux charges radiales ; il supporte mal une forte charge axiale. ← la charge arrive sur le chemin de roulement dans une direction pour laquelle il n'est pas fait.
4. **Conclure** : le choix est mauvais, ce qui explique l'usure du chemin. La vis tournant vite, on remplace par une paire de roulements à billes à contact oblique.

:::

::: piege Remplacer à l'identique ne guérit rien
« Les roulements sont usés : j'en remets deux neufs, du même modèle » ✗. L'usure du chemin est le symptôme d'un type mal adapté à la charge axiale, pas d'un exemplaire défectueux : les neufs s'useront de la même façon. On corrige la cause, c'est-à-dire le type.
:::

::: verifie
Un arbre porte des charges radiales et axiales importantes et tourne à vitesse moyenne. Quel type de roulements retenir ?

---

Charges radiales et axiales importantes : il faut un contact oblique ou des rouleaux coniques. À vitesse moyenne, ce sont les **rouleaux coniques** ; les billes à contact oblique se choisissent pour une vitesse importante.
:::

::: retenir
Contact radial : charges surtout radiales. Charges radiales et axiales importantes : billes à contact oblique (vitesse importante) ou rouleaux coniques (vitesse moyenne). Remplacer à l'identique ne corrige pas un mauvais choix.
:::

## ✖️ Monter la paire : en X ou en O

Un roulement à billes à contact oblique ne reprend l'effort axial que dans un sens : seul, il laisserait l'arbre partir dans l'autre. On les monte donc **par paire**, retournés l'un par rapport à l'autre. 

Il y a deux façons de les retourner, et la bonne dépend de ce qui tourne : laquelle choisir ?

::: definition Montage en X et montage en O
Chaque roulement transmet son effort le long d'une **ligne d'action**, droite oblique qui passe par ses points de contact. Dans un montage **en X**, les deux lignes se rapprochent en allant vers l'axe de l'arbre ; dans un montage **en O**, elles s'écartent en allant vers l'axe. Règle d'usage : **arbre tournant, montage en X** ; **moyeu (alésage) tournant, montage en O**.
:::

::: figure Demi-coupe d'un arbre dans son logement. Les traits verts épais sont les lignes d'action ; en pointillé, leur prolongement. En X (à gauche), elles se rejoignent près de l'axe de l'arbre ; en O (à droite), elles se rejoignent de l'autre côté, vers le logement
<svg viewBox="0 0 520 250"><rect x="20" y="60" width="180" height="32" fill="#cbd5e1" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="20" y="140" width="180" height="50" fill="#e2e8f0" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><path d="M14 190 L206 190" fill="none" stroke="#0f172a" stroke-width="1.6" stroke-dasharray="14 4 3 4"/><rect x="53" y="92" width="34" height="16" fill="#dbeafe" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="53" y="124" width="34" height="16" fill="#dbeafe" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><circle cx="70" cy="116" r="7" fill="#ffffff" stroke="#0f172a" stroke-width="2"/><rect x="133" y="92" width="34" height="16" fill="#dbeafe" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="133" y="124" width="34" height="16" fill="#dbeafe" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><circle cx="150" cy="116" r="7" fill="#ffffff" stroke="#0f172a" stroke-width="2"/><path d="M56 92 L84 140" fill="none" stroke="#0f6e56" stroke-width="3"/><path d="M164 92 L136 140" fill="none" stroke="#0f6e56" stroke-width="3"/><path d="M84 140 L110 184.6" fill="none" stroke="#0f6e56" stroke-width="1.8" stroke-dasharray="5 4"/><path d="M136 140 L110 184.6" fill="none" stroke="#0f6e56" stroke-width="1.8" stroke-dasharray="5 4"/><circle cx="110" cy="184.6" r="3.6" fill="#0f6e56" stroke="#0f6e56" stroke-width="1"/><text x="110" y="26" font-size="14" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">montage en X</text><rect x="280" y="60" width="180" height="32" fill="#cbd5e1" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="280" y="140" width="180" height="50" fill="#e2e8f0" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><path d="M274 190 L466 190" fill="none" stroke="#0f172a" stroke-width="1.6" stroke-dasharray="14 4 3 4"/><rect x="313" y="92" width="34" height="16" fill="#dbeafe" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="313" y="124" width="34" height="16" fill="#dbeafe" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><circle cx="330" cy="116" r="7" fill="#ffffff" stroke="#0f172a" stroke-width="2"/><rect x="393" y="92" width="34" height="16" fill="#dbeafe" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="393" y="124" width="34" height="16" fill="#dbeafe" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><circle cx="410" cy="116" r="7" fill="#ffffff" stroke="#0f172a" stroke-width="2"/><path d="M344 92 L316 140" fill="none" stroke="#0f6e56" stroke-width="3"/><path d="M396 92 L424 140" fill="none" stroke="#0f6e56" stroke-width="3"/><path d="M344 92 L370 47.4" fill="none" stroke="#0f6e56" stroke-width="1.8" stroke-dasharray="5 4"/><path d="M396 92 L370 47.4" fill="none" stroke="#0f6e56" stroke-width="1.8" stroke-dasharray="5 4"/><circle cx="370" cy="47.4" r="3.6" fill="#0f6e56" stroke="#0f6e56" stroke-width="1"/><text x="370" y="26" font-size="14" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">montage en O</text></svg>
:::

Les deux montages utilisent les mêmes roulements : seule leur orientation change.

::: exemple Choisir le montage d'une vis, puis d'une poulie
1. **Vis sans fin** : c'est l'arbre qui tourne dans un carter fixe, donc **montage en X**. ← règle : arbre tournant, X.
2. **Poulie** qui tourne autour d'un axe fixe : c'est le moyeu, donc l'alésage, qui tourne, donc **montage en O**. ← règle : moyeu tournant, O.
3. **Dans les deux cas** la question utile est « qu'est-ce qui tourne ? », pas « quel type de roulement ? ». ← le type est déjà choisi : contact oblique.

:::

::: verifie
Un arbre tournant dans un carter fixe est guidé par une paire de roulements à billes à contact oblique. Quel montage adopter ?

---

L'arbre tourne : montage **en X**. La règle ne regarde que la pièce qui tourne, pas le type de roulement.
:::

::: retenir
Arbre tournant : X ; moyeu tournant : O. En X les lignes d'action se rapprochent vers l'axe, en O elles s'écartent.
:::

## 🧱 Arrêter les bagues, ajuster les portées

Une paire de roulements est montée sur la vis sans fin. Si rien ne bloque leurs bagues le long de l'axe, la paire glisse dès qu'une charge axiale arrive.

Que faut-il arrêter, et comment dire qu'une bague est montée serrée ou avec jeu ?

::: definition Arrêts axiaux et portées
Chaque **bague** d'un roulement, intérieure comme extérieure, est arrêtée en translation par une **butée** : épaulement, couvercle, anneau. Une **portée** est la surface de l'arbre ou du logement qui reçoit une bague ; sa **tolérance** dit comment la bague s'y monte. La casse de la lettre dit la pièce : **minuscule** pour l'arbre (m6), **majuscule** pour l'alésage du logement (H7).
:::

::: figure Les quatre bagues de la paire montée en X, chacune appuyée sur sa butée noire : la bague extérieure de gauche et celle de droite côté logement, les deux bagues intérieures côté arbre. Quatre bagues, quatre arrêts
<svg viewBox="0 0 260 230"><rect x="20" y="60" width="180" height="32" fill="#cbd5e1" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="20" y="140" width="180" height="50" fill="#e2e8f0" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><path d="M14 190 L206 190" fill="none" stroke="#0f172a" stroke-width="1.6" stroke-dasharray="14 4 3 4"/><rect x="53" y="92" width="34" height="16" fill="#dbeafe" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="53" y="124" width="34" height="16" fill="#dbeafe" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><circle cx="70" cy="116" r="7" fill="#ffffff" stroke="#0f172a" stroke-width="2"/><rect x="133" y="92" width="34" height="16" fill="#dbeafe" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="133" y="124" width="34" height="16" fill="#dbeafe" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><circle cx="150" cy="116" r="7" fill="#ffffff" stroke="#0f172a" stroke-width="2"/><path d="M56 92 L84 140" fill="none" stroke="#0f6e56" stroke-width="3"/><path d="M164 92 L136 140" fill="none" stroke="#0f6e56" stroke-width="3"/><rect x="45" y="92" width="8" height="16" fill="#0f172a" stroke="#0f172a" stroke-width="1.5" stroke-linejoin="round"/><rect x="87" y="124" width="8" height="16" fill="#0f172a" stroke="#0f172a" stroke-width="1.5" stroke-linejoin="round"/><rect x="125" y="124" width="8" height="16" fill="#0f172a" stroke="#0f172a" stroke-width="1.5" stroke-linejoin="round"/><rect x="167" y="92" width="8" height="16" fill="#0f172a" stroke="#0f172a" stroke-width="1.5" stroke-linejoin="round"/></svg>
:::

Chaque butée noire de la figure correspond à un arrêt : on en compte autant que de bagues.

::: exemple Arrêter et ajuster la paire de la vis sans fin
1. **Compter les bagues** : 2 roulements × 2 bagues = 4. ← un arrêt par bague.
2. **Choisir l'arrêt de réglage** : un seul des quatre est réglable, par des cales, pour fixer le jeu. ← les trois autres sont fixes.
3. **Portée de l'arbre** : la bague intérieure tourne avec l'arbre et s'y monte serrée, on écrit **m6** (minuscule). ← la lettre minuscule désigne l'arbre.
4. **Alésage du logement** : le logement est fixe et reçoit la bague extérieure, on écrit **H7** (majuscule). ← la lettre majuscule désigne l'alésage.

:::

::: piege Un roulement n'est pas un arrêt
« Deux roulements, donc deux arrêts » ✗. On compte par **bague** : chaque roulement a une bague intérieure et une bague extérieure, et chacune doit être arrêtée. Deux roulements, quatre arrêts.
:::

::: verifie
Un dessin porte « H7 » sur une portée de roulement. S'agit-il d'un arbre ou d'un alésage ? Combien d'arrêts pour une paire, dont combien de réglage ?

---

La lettre est majuscule : c'est un **alésage**, celui du logement. Une paire compte 2 × 2 = **4 arrêts**, dont **un seul** de réglage.
:::

::: retenir
Une paire de roulements : quatre arrêts, dont un de réglage. Portées : m6 (minuscule) pour l'arbre, H7 (majuscule) pour l'alésage.
:::

## 🛢️ Lubrifier et étancher

Le réducteur doit résister à la corrosion, à la poussière et à un fonctionnement permanent. Des surfaces qui frottent sans huile s'usent vite ; une huile qui fuit s'épuise ; une poussière qui entre abîme les roulements.

Quelles pièces de la nomenclature s'en occupent ?

::: definition Lubrification et étanchéité
**Lubrifier**, c'est interposer un lubrifiant (huile ou graisse) entre des surfaces qui frottent, pour limiter frottement et usure. **Étancher**, c'est empêcher le lubrifiant de sortir et les poussières d'entrer.
:::

| Pièce | Rep. | Rôle |
| --- | --- | --- |
| Voyant niveau d'huile | 17 | contrôler le niveau d'huile sans ouvrir le carter |
| Bouchon de vidange | 20 | évacuer l'huile usagée |
| Joint feutre | 24 | étanchéité : retient l'huile, arrête les poussières |
| Joint | 2 | étanchéité (composant standard) |

::: exemple Un changement d'huile en trois gestes
1. **Vider** : on dévisse le bouchon de vidange (20) et l'huile usagée s'écoule. ← c'est la pièce prévue pour vider le carter.
2. **Refermer** le bouchon (20), puis remplir. ← une vidange mal refermée fuirait.
3. **Contrôler** le niveau au voyant (17), sans rien ouvrir. ← le voyant montre le niveau de l'extérieur.

:::

::: piege Contrôler le niveau n'étanche pas
« Le voyant (17) empêche l'huile de fuir » ✗. Le voyant fait partie de la lubrification : il **contrôle** le niveau. L'étanchéité est le métier des joints, comme le joint feutre (24).
:::

::: verifie
Un opérateur veut vérifier le niveau d'huile sans ouvrir le carter, puis changer l'huile. Quelles pièces utilise-t-il, dans quel ordre ?

---

Il lit d'abord le voyant (17), qui indique le niveau sans rien ouvrir ; il ouvre ensuite le bouchon de vidange (20) pour évacuer l'huile.
:::

::: retenir
Lubrifier = limiter le frottement (huile, voyant, vidange) ; étancher = garder l'huile et chasser la poussière (joints).
:::

## 📐 Dessiner la nouvelle solution à l'échelle

Une fois la nouvelle solution choisie, il faut la dessiner. Le manuel demande de compléter le dessin de la nouvelle solution « à l'échelle du dessin », avec des composants normalisés. Chaque feuille a son échelle, et se tromper de sens dans le rapport fausse tout le tracé. Les dessins du chapitre n'ont pas tous la même échelle : 2:5 pour l'ensemble du réducteur, 1:1 pour la roue creuse, 3:4 pour la vis sans fin.

Que veulent dire ces nombres, et comment passer du réel au dessin ?

::: definition L'échelle
L'**échelle** a:b compare une longueur mesurée **sur le dessin** à la longueur **réelle** : dessin : réel. 1:1, c'est la grandeur nature ; 2:5 et 3:4 sont des **réductions** : le dessin est plus petit que la pièce.
:::

| Échelle | On multiplie la longueur réelle par | Réel 100 mm donne, sur le dessin |
| --- | --- | --- |
| 1:1 | 1 | 100 mm |
| 3:4 | 3/4 | 75 mm |
| 2:5 | 2/5 | 40 mm |

::: exemple Du réel au dessin, et retour
Une cote réelle de 80 mm, sur un dessin à l'échelle 2:5.
1. **Du réel au dessin** : 80 × 2/5 = **32 mm**. ← on multiplie par le rapport dessin : réel.
2. **Du dessin au réel** : 32 × 5/2 = **80 mm**. ← on multiplie par l'inverse.
3. **Contrôle** : une réduction donne un dessin plus petit que la pièce, 32 < 80. ✓

:::

::: piege Le rapport à l'envers
« Échelle 2:5, cote réelle 80 mm : 80 × 5/2 = 200 mm sur le dessin » ✗. Un dessin à l'échelle 2:5 est une réduction, il ne peut pas dépasser la pièce. Test de bon sens avant de conclure : réduction, donc dessin plus petit.
:::

::: methode Dessiner un composant normalisé
1. Prendre ses dimensions dans la norme ou le catalogue : roulement, joint, anneau élastique, vis.
2. Les ramener à l'échelle du dessin.
3. Tracer, puis refaire le même tracé avec un logiciel de dessin 2D.

Un composant normalisé ne s'invente pas : ses dimensions sont fixées par sa norme.
:::

::: verifie
Une cote réelle de 48 mm est dessinée à l'échelle 3:4. Combien mesure-t-elle sur le dessin ?

---

Réduction : on multiplie par 3/4, 48 × 3/4 = **36 mm**. Contrôle : 36 < 48, le dessin est plus petit que la pièce.
:::

::: retenir
Échelle = dessin : réel. Réel vers dessin : multiplier par le rapport ; dessin vers réel : par son inverse. Une réduction donne toujours un dessin plus petit.
:::

> 🏆 Le réducteur n'a plus de secret, héros : tu sais ce qui tient ses carters, ce qui règle sa roue et ce qui guide sa vis. Le prochain support te fera voir les mêmes assemblages sous d'autres formes.
