# ⚔️ Graphes — réseaux, chemins, matrices et probabilités : du plan de livraison à l'état d'équilibre

> 💡 « Un graphe garde l'essentiel d'un réseau : qui est relié à qui. Le reste, c'est du calcul. »

Bienvenue, héros de l'Économie et gestion. Un responsable logistique cherche la route la plus courte, un directeur d'opérateur veut savoir où se stabilisera sa clientèle, un organisateur de salon doit loger ses ateliers sans conflit d'horaire : tous dessinent des points reliés par des traits. Huit étapes te mènent du vocabulaire des graphes à leurs matrices et à leurs probabilités : sommets et degrés, chaînes eulériennes, coloration, plus court chemin, graphes orientés et matrice associée, puissances de la matrice, distance et diamètre, graphes probabilistes. On suppose acquis le produit de deux matrices (chapitre « Matrices et systèmes ») et les probabilités conditionnelles. Les calculs se font à la main, la calculatrice servant de contrôle.

## 🕸️ Sommets, arêtes et degrés

Une société installe cinq bornes de recharge A, B, C, D, E, reliées par cinq câbles : AB, AC, BC, CD et DE.
Combien de câbles partent de chaque borne, et que dit le total de ces nombres ?

::: definition
Un **graphe** est un ensemble de **sommets** reliés par des **arêtes**. Son **ordre** est le nombre de sommets. Le **degré** d'un sommet est le nombre d'arêtes qui en partent ; deux sommets reliés par une arête sont **adjacents**.
Une **chaîne** est une suite de sommets où deux sommets consécutifs sont adjacents ; sa **longueur** est le nombre d'arêtes parcourues.
Un graphe est **connexe** si deux sommets quelconques sont reliés par une chaîne, et **complet** si deux sommets distincts quelconques sont adjacents.
:::

::: figure Les cinq bornes : la borne C touche trois câbles, la borne E un seul
<svg viewBox="0 0 340 150"><title>Graphe de cinq bornes A, B, C, D, E reliées par cinq câbles</title><line x1="40" y1="115" x2="90" y2="40" stroke="#0f172a" stroke-width="1.8"/><line x1="40" y1="115" x2="140" y2="115" stroke="#0f172a" stroke-width="1.8"/><line x1="90" y1="40" x2="140" y2="115" stroke="#0f172a" stroke-width="1.8"/><line x1="140" y1="115" x2="220" y2="115" stroke="#0f172a" stroke-width="1.8"/><line x1="220" y1="115" x2="300" y2="115" stroke="#0f172a" stroke-width="1.8"/><circle cx="40" cy="115" r="15" fill="#ecfdf5" stroke="#0f172a" stroke-width="1.5"/><text x="40" y="120" font-size="14" text-anchor="middle" fill="#0f172a" font-weight="bold">A</text><circle cx="90" cy="40" r="15" fill="#ecfdf5" stroke="#0f172a" stroke-width="1.5"/><text x="90" y="45" font-size="14" text-anchor="middle" fill="#0f172a" font-weight="bold">B</text><circle cx="140" cy="115" r="15" fill="#ecfdf5" stroke="#0f172a" stroke-width="1.5"/><text x="140" y="120" font-size="14" text-anchor="middle" fill="#0f172a" font-weight="bold">C</text><circle cx="220" cy="115" r="15" fill="#ecfdf5" stroke="#0f172a" stroke-width="1.5"/><text x="220" y="120" font-size="14" text-anchor="middle" fill="#0f172a" font-weight="bold">D</text><circle cx="300" cy="115" r="15" fill="#ecfdf5" stroke="#0f172a" stroke-width="1.5"/><text x="300" y="120" font-size="14" text-anchor="middle" fill="#0f172a" font-weight="bold">E</text></svg>
:::

::: exemple Les bornes de recharge
1. L'ordre du graphe est 5, car il y a cinq sommets.
2. Les degrés sont A : 2 (AB, AC), B : 2 (AB, BC), C : 3 (AC, BC, CD), D : 2 (CD, DE) et E : 1 (DE).
3. La somme des degrés est 2 + 2 + 3 + 2 + 1 = 10.
4. Il y a 5 arêtes et 10 = 2 × 5 : chaque arête a deux extrémités, donc elle est comptée deux fois, une fois dans chacun de ses sommets.
5. Le graphe est connexe : A-C-D-E relie A à E, et B se joint à A ou C. Il n'est pas complet, car A et D ne sont pas adjacents.

:::

::: piege Prendre la somme des degrés pour le nombre d'arêtes
On trouve 10 câbles, parce que les degrés ont été additionnés et que le résultat est sous les yeux. Mais chaque câble est compté **deux fois** dans cette somme. Le nombre d'arêtes est 10 ÷ 2 = 5, et on peut le vérifier en les recomptant sur la figure.
:::

::: propriete
- La somme des degrés des sommets est égale à **2 × le nombre d'arêtes** : elle est donc toujours paire.
- Il y a donc un nombre **pair** de sommets de degré impair : un graphe n'a jamais un seul sommet de degré impair.
- Dans un graphe complet d'ordre n, chaque sommet a pour degré n − 1, et le nombre d'arêtes est n(n − 1)/2 : un graphe complet d'ordre 4 a 3 × 4/2 = 6 arêtes.

Cas limite : un graphe réduit à un seul sommet, sans arête, est à la fois connexe et complet ; son sommet a pour degré 0.
:::

::: verifie
Un graphe d'ordre 7 a pour degrés 3, 3, 3, 2, 2, 2, 1. Combien a-t-il d'arêtes, et combien de sommets de degré impair ?

---

La somme des degrés est 3 + 3 + 3 + 2 + 2 + 2 + 1 = 16, et chaque arête est comptée deux fois : il y a 16 ÷ 2 = 8 arêtes. Les degrés impairs sont 3, 3, 3 et 1, soit 4 sommets : un nombre pair, comme la propriété l'annonce.
:::

::: retenir
Somme des degrés = 2 × nombre d'arêtes, donc un nombre pair de sommets de degré impair ; un graphe complet d'ordre n compte n(n − 1)/2 arêtes.
:::

## 🚶 Chaînes et cycles eulériens

Un facteur dessert un quartier dont les carrefours sont P, Q, R, S et les rues PQ, QR, RS, SP et PR. Il voudrait emprunter chaque rue exactement une fois.
Est-ce possible, et comment le savoir sans essayer tous les trajets ?

::: definition
Un **cycle** est une chaîne **fermée** (elle revient à son point de départ) dont les arêtes sont toutes distinctes.
Une chaîne est **eulérienne** si elle passe **une fois et une seule** par chaque arête du graphe ; un **cycle eulérien** est une chaîne eulérienne fermée.
:::

::: figure Le carré PQRS avec la diagonale PR : seuls P et R ont un nombre impair de rues
<svg viewBox="0 0 250 160"><title>Carré de quatre carrefours P, Q, R, S avec la diagonale PR</title><line x1="60" y1="30" x2="190" y2="30" stroke="#0f172a" stroke-width="1.8"/><line x1="190" y1="30" x2="190" y2="130" stroke="#0f172a" stroke-width="1.8"/><line x1="190" y1="130" x2="60" y2="130" stroke="#0f172a" stroke-width="1.8"/><line x1="60" y1="130" x2="60" y2="30" stroke="#0f172a" stroke-width="1.8"/><line x1="60" y1="30" x2="190" y2="130" stroke="#0f172a" stroke-width="1.8"/><circle cx="60" cy="30" r="15" fill="#ecfdf5" stroke="#0f172a" stroke-width="1.5"/><text x="60" y="35" font-size="14" text-anchor="middle" fill="#0f172a" font-weight="bold">P</text><circle cx="190" cy="30" r="15" fill="#ecfdf5" stroke="#0f172a" stroke-width="1.5"/><text x="190" y="35" font-size="14" text-anchor="middle" fill="#0f172a" font-weight="bold">Q</text><circle cx="190" cy="130" r="15" fill="#ecfdf5" stroke="#0f172a" stroke-width="1.5"/><text x="190" y="135" font-size="14" text-anchor="middle" fill="#0f172a" font-weight="bold">R</text><circle cx="60" cy="130" r="15" fill="#ecfdf5" stroke="#0f172a" stroke-width="1.5"/><text x="60" y="135" font-size="14" text-anchor="middle" fill="#0f172a" font-weight="bold">S</text></svg>
:::

::: exemple Le quartier du facteur
1. Les degrés sont P : 3 (PQ, SP, PR), Q : 2, R : 3 (QR, RS, PR) et S : 2.
2. Exactement deux sommets, P et R, sont de degré impair : le graphe n'a pas de cycle eulérien, mais il a une chaîne eulérienne dont P et R sont les extrémités.
3. On la trouve : P-Q-R-S-P-R passe par PQ, QR, RS, SP puis PR, soit les 5 rues, chacune une seule fois.
4. Un trajet qui reviendrait à P est donc impossible : le facteur finit forcément en R s'il part de P.

:::

::: piege Oublier de vérifier que le graphe est connexe
Deux triangles ABC et DEF, sans aucune rue entre eux, ont tous leurs sommets de degré 2, donc pair : on conclut à un cycle eulérien. Cela tente parce que le critère des degrés est satisfait. Mais le graphe n'est pas connexe : aucune chaîne ne passe d'un triangle à l'autre, donc aucune ne parcourt toutes les arêtes.
:::

::: propriete
Soit G un graphe **connexe**.
- Si tous les sommets sont de degré pair, G a un cycle eulérien.
- Si exactement deux sommets sont de degré impair, G a une chaîne eulérienne, non fermée, dont ces deux sommets sont les extrémités.
- S'il y a plus de deux sommets de degré impair, G n'a aucune chaîne eulérienne.

Cas limite : le cas d'un seul sommet de degré impair n'existe pas, puisque leur nombre est toujours pair.
:::

::: verifie
Un graphe a pour arêtes MN, NO, OM, OP, PQ et QO. Admet-il un cycle eulérien ? Si oui, en donner un.

---

Le graphe est connexe. Les degrés sont M : 2, N : 2, O : 4 (NO, OM, OP, QO), P : 2 et Q : 2, tous pairs : il y a un cycle eulérien. Par exemple O-M-N-O-P-Q-O utilise OM, MN, NO, OP, PQ, QO, soit les 6 arêtes une seule fois, et revient en O.
:::

::: retenir
Pour un graphe connexe : 0 sommet impair, cycle eulérien ; 2 sommets impairs, chaîne eulérienne entre eux ; plus de 2, aucune.
:::

## 🎨 Colorier un graphe

Cinq ateliers A, B, C, D, E d'un salon professionnel doivent se tenir à des heures différentes quand ils partagent des inscrits : AB, AC, BC, CD et DE sont dans ce cas.
C'est le graphe des cinq bornes de la première section.
Quel est le plus petit nombre de créneaux horaires qui évite tout conflit ?

::: definition
**Colorier** un graphe, c'est donner une couleur à chaque sommet de sorte que deux sommets **adjacents** n'aient jamais la même couleur.
Le **nombre chromatique** de G, noté γ(G), est le plus petit nombre de couleurs avec lequel on peut y parvenir.
Un **sous-graphe** est formé de certains sommets de G et des arêtes de G qui les relient.
:::

::: exemple Les créneaux du salon
1. Les ateliers A, B, C sont deux à deux adjacents : ils exigent trois couleurs différentes, donc γ ≥ 3.
2. On colore A en 1, B en 2, C en 3.
3. D est adjacent à C seulement parmi les sommets déjà colorés : on lui donne la couleur 1. E est adjacent à D : on lui donne la couleur 2.
4. Trois couleurs suffisent et il en faut au moins trois, donc γ = 3 : trois créneaux.

:::

::: piege Prendre le plus grand degré plus un pour le nombre chromatique
Le plus grand degré est 3 (celui de C), et on annonce γ = 3 + 1 = 4. Cela tente parce qu'on pense qu'il faut une couleur de plus que le plus grand nombre de voisins. Mais 4 n'est qu'une **borne supérieure** : le salon se règle en 3 créneaux, et la coloration 1, 2, 3, 1, 2 le prouve.
:::

::: propriete
- γ(G) est supérieur ou égal à l'ordre de tout sous-graphe complet de G : un triangle impose au moins 3 couleurs.
- γ(G) est inférieur ou égal à Δ + 1, où Δ est le plus grand degré des sommets.
- Entre ces deux bornes, c'est une coloration explicite qui tranche : on en exhibe une pour la borne haute, un sous-graphe complet pour la borne basse.

Cas limite : un graphe sans arête se colore avec une seule couleur ; un graphe complet d'ordre n exige n couleurs, car les deux bornes valent alors n.
:::

::: verifie
Quatre salles U, V, W, X forment un cycle : UV, VW, WX et XU sont les couples de salles qui ne peuvent pas être utilisées en même temps. Quel est γ ?

---

Le plus grand sous-graphe complet est une arête (ordre 2) et Δ + 1 = 3, donc 2 ≤ γ ≤ 3. On colore U en 1, V en 2, W en 1, X en 2 : deux sommets adjacents ont toujours des couleurs différentes. Deux couleurs suffisent, donc γ = 2.
:::

::: retenir
γ(G) se trouve entre l'ordre du plus grand sous-graphe complet et Δ + 1 ; on le fixe par une coloration qui atteint la borne basse.
:::

## 🛣️ Le plus court chemin : l'algorithme de Dijkstra

Un livreur part du dépôt S vers le client T. Le réseau routier est un graphe dont chaque arête porte une distance en kilomètres.
La route qui compte le moins d'arêtes est-elle la plus courte en kilomètres ?

::: definition
Un graphe est **pondéré** quand chaque arête porte un nombre, son **poids** (une distance, une durée, un coût). Le **poids d'une chaîne** est la somme des poids de ses arêtes.
Une **plus courte chaîne** entre deux sommets est une chaîne de poids minimal.
:::

::: figure Le réseau du livreur : les poids sont en kilomètres, et l'arête B-D de 11 km est une fausse bonne idée
<svg viewBox="0 0 330 180"><title>Graphe pondéré de six points S, A, B, C, D, T</title><line x1="30" y1="95" x2="95" y2="35" stroke="#0f172a" stroke-width="1.8"/><line x1="30" y1="95" x2="95" y2="150" stroke="#0f172a" stroke-width="1.8"/><line x1="95" y1="35" x2="95" y2="150" stroke="#0f172a" stroke-width="1.8"/><line x1="95" y1="35" x2="195" y2="60" stroke="#0f172a" stroke-width="1.8"/><line x1="95" y1="150" x2="195" y2="60" stroke="#0f172a" stroke-width="1.8"/><line x1="95" y1="150" x2="195" y2="145" stroke="#0f172a" stroke-width="1.8"/><line x1="195" y1="60" x2="195" y2="145" stroke="#0f172a" stroke-width="1.8"/><line x1="195" y1="60" x2="300" y2="100" stroke="#0f172a" stroke-width="1.8"/><line x1="195" y1="145" x2="300" y2="100" stroke="#0f172a" stroke-width="1.8"/><text x="50.5" y="59.0" font-size="13" text-anchor="middle" fill="#0f6e56" font-weight="bold" stroke="#fff" stroke-width="3" paint-order="stroke">5</text><text x="50.5" y="136.5" font-size="13" text-anchor="middle" fill="#0f6e56" font-weight="bold" stroke="#fff" stroke-width="3" paint-order="stroke">9</text><text x="82.0" y="96.5" font-size="13" text-anchor="middle" fill="#0f6e56" font-weight="bold" stroke="#fff" stroke-width="3" paint-order="stroke">3</text><text x="145.0" y="39.5" font-size="13" text-anchor="middle" fill="#0f6e56" font-weight="bold" stroke="#fff" stroke-width="3" paint-order="stroke">8</text><text x="143.0" y="95.0" font-size="13" text-anchor="middle" fill="#0f6e56" font-weight="bold" stroke="#fff" stroke-width="3" paint-order="stroke">4</text><text x="145.0" y="141.5" font-size="13" text-anchor="middle" fill="#0f6e56" font-weight="bold" stroke="#fff" stroke-width="3" paint-order="stroke">11</text><text x="209.0" y="106.5" font-size="13" text-anchor="middle" fill="#0f6e56" font-weight="bold" stroke="#fff" stroke-width="3" paint-order="stroke">2</text><text x="253.5" y="70.0" font-size="13" text-anchor="middle" fill="#0f6e56" font-weight="bold" stroke="#fff" stroke-width="3" paint-order="stroke">10</text><text x="255.5" y="138.5" font-size="13" text-anchor="middle" fill="#0f6e56" font-weight="bold" stroke="#fff" stroke-width="3" paint-order="stroke">5</text><circle cx="30" cy="95" r="15" fill="#ecfdf5" stroke="#0f172a" stroke-width="1.5"/><text x="30" y="100" font-size="14" text-anchor="middle" fill="#0f172a" font-weight="bold">S</text><circle cx="95" cy="35" r="15" fill="#ecfdf5" stroke="#0f172a" stroke-width="1.5"/><text x="95" y="40" font-size="14" text-anchor="middle" fill="#0f172a" font-weight="bold">A</text><circle cx="95" cy="150" r="15" fill="#ecfdf5" stroke="#0f172a" stroke-width="1.5"/><text x="95" y="155" font-size="14" text-anchor="middle" fill="#0f172a" font-weight="bold">B</text><circle cx="195" cy="60" r="15" fill="#ecfdf5" stroke="#0f172a" stroke-width="1.5"/><text x="195" y="65" font-size="14" text-anchor="middle" fill="#0f172a" font-weight="bold">C</text><circle cx="195" cy="145" r="15" fill="#ecfdf5" stroke="#0f172a" stroke-width="1.5"/><text x="195" y="150" font-size="14" text-anchor="middle" fill="#0f172a" font-weight="bold">D</text><circle cx="300" cy="100" r="15" fill="#ecfdf5" stroke="#0f172a" stroke-width="1.5"/><text x="300" y="105" font-size="14" text-anchor="middle" fill="#0f172a" font-weight="bold">T</text></svg>
:::

::: exemple De S à tous les points, par Dijkstra
1. On retient S avec la distance 0 et on inscrit ∞ pour les autres points.
2. On retient le point de plus petite distance provisoire : S. Ses voisins prennent A : 5 et B : 9.
3. On retient A (5) : B devient 5 + 3 = 8, car 8 < 9, et C reçoit 5 + 8 = 13.
4. On retient B (8) : C devient 8 + 4 = 12, car 12 < 13, et D reçoit 8 + 11 = 19.
5. On retient C (12) : D devient 12 + 2 = 14, car 14 < 19, et T reçoit 12 + 10 = 22.
6. On retient D (14) : T devient 14 + 5 = 19, car 19 < 22. On retient T (19).

| Étape | Point retenu | A | B | C | D | T |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | S (0) | 5 | 9 | ∞ | ∞ | ∞ |
| 2 | A (5) | 5 | 8 | 13 | ∞ | ∞ |
| 3 | B (8) | 5 | 8 | 12 | 19 | ∞ |
| 4 | C (12) | 5 | 8 | 12 | 14 | 22 |
| 5 | D (14) | 5 | 8 | 12 | 14 | 19 |

On remonte les prédécesseurs depuis T : T ← D ← C ← B ← A ← S. La plus courte chaîne est S-A-B-C-D-T, de poids 5 + 3 + 4 + 2 + 5 = 19 km.

:::

::: piege Choisir la chaîne qui compte le moins d'arêtes
La chaîne S-B-D-T n'a que 3 arêtes et paraît directe, mais elle pèse 9 + 11 + 5 = 25 km. La chaîne S-A-B-C-D-T a 5 arêtes et pèse 19 km. Le nombre d'arêtes mesure une **longueur** de chaîne ; la plus courte **en poids** se cherche avec Dijkstra, jamais en comptant les arêtes.
:::

::: methode Dijkstra, pas à pas
1. Donner la distance 0 au sommet de départ et ∞ aux autres.
2. Retenir le sommet non retenu dont la distance provisoire est la plus petite.
3. Mettre à jour ses voisins non retenus : on garde la plus petite entre l'ancienne distance et distance retenue + poids de l'arête.
4. Recommencer jusqu'à retenir tous les sommets, ou l'arrivée.
5. Remonter les prédécesseurs depuis l'arrivée pour lire la chaîne.

Cas limite : si deux chaînes ont le même poids minimal, les deux sont des plus courtes ; si un sommet reste à ∞, il n'est relié à aucune chaîne depuis le départ.
:::

::: verifie
Un graphe pondéré a pour arêtes P-Q : 4, P-R : 7, Q-R : 2, Q-T : 9 et R-T : 3. Quelle est la plus courte chaîne de P à T, et son poids ?

---

On retient P (0) : Q reçoit 4 et R reçoit 7. On retient Q (4) : R devient 4 + 2 = 6, car 6 < 7, et T reçoit 4 + 9 = 13. On retient R (6) : T devient 6 + 3 = 9, car 9 < 13. La plus courte chaîne est P-Q-R-T, de poids 4 + 2 + 3 = 9.
:::

::: retenir
Le plus court chemin pondéré se calcule par Dijkstra : on retient à chaque tour la plus petite distance provisoire, puis on met à jour ses voisins.
:::

## ➡️ Graphe orienté et matrice associée

Dans un quartier à sens uniques, les carrefours X, Y, Z, W sont reliés par les rues X vers Y, Y vers Z, Z vers X, Z vers W et W vers Y.
Comment résumer ces sens dans un tableau de nombres sur lequel on peut calculer ?

::: definition
Dans un **graphe orienté**, chaque arête est un **arc** : il va d'un sommet **origine** à un sommet **extrémité** et ne se parcourt que dans ce sens. Un arc dont l'origine et l'extrémité sont le même sommet est une **boucle**. Un **chemin**, ou **chaîne orientée**, est une suite d'arcs où l'extrémité de chacun est l'origine du suivant ; un **cycle orienté** est un chemin fermé dont les arcs sont tous distincts.
On note d⁺(S) le nombre d'arcs **sortant** de S et d⁻(S) le nombre d'arcs **entrant** en S.
La **matrice associée** à un graphe de sommets S₁, S₂, …, Sₙ est la matrice carrée A d'ordre n dont le coefficient aᵢⱼ est le nombre d'arcs d'origine Sᵢ et d'extrémité Sⱼ.
Pour un graphe **non orienté**, chaque arête entre Sᵢ et Sⱼ compte dans les deux sens : aᵢⱼ = aⱼᵢ est le nombre d'arêtes qui relient Sᵢ et Sⱼ. Ainsi la matrice des cinq bornes porte un 1 en (A, B) et en (B, A).
:::

::: figure Les cinq sens uniques du quartier : deux rues sortent de Z, et deux rues arrivent en Y
<svg viewBox="0 0 320 170"><title>Graphe orienté de quatre carrefours X, Y, Z, W</title><line x1="55.0" y1="70.0" x2="145.0" y2="70.0" stroke="#0f172a" stroke-width="1.8"/><polygon points="145.0,70.0 136.7,73.5 136.7,66.5" fill="#0f172a"/><line x1="175.0" y1="70.0" x2="265.0" y2="70.0" stroke="#0f172a" stroke-width="1.8"/><polygon points="265.0,70.0 256.7,73.5 256.7,66.5" fill="#0f172a"/><line x1="267.3" y1="77.9" x2="172.7" y2="137.1" stroke="#0f172a" stroke-width="1.8"/><polygon points="172.7,137.1 177.9,129.7 181.6,135.6" fill="#0f172a"/><line x1="160.0" y1="130.0" x2="160.0" y2="85.0" stroke="#0f172a" stroke-width="1.8"/><polygon points="160.0,85.0 163.5,93.3 156.5,93.3" fill="#0f172a"/><path d="M 272 58 Q 160 -10 50 58" fill="none" stroke="#0f172a" stroke-width="1.8"/><polygon points="50.0,58.0 55.9,49.9 59.9,56.6" fill="#0f172a"/><circle cx="40" cy="70" r="15" fill="#ecfdf5" stroke="#0f172a" stroke-width="1.5"/><text x="40" y="75" font-size="14" text-anchor="middle" fill="#0f172a" font-weight="bold">X</text><circle cx="160" cy="70" r="15" fill="#ecfdf5" stroke="#0f172a" stroke-width="1.5"/><text x="160" y="75" font-size="14" text-anchor="middle" fill="#0f172a" font-weight="bold">Y</text><circle cx="280" cy="70" r="15" fill="#ecfdf5" stroke="#0f172a" stroke-width="1.5"/><text x="280" y="75" font-size="14" text-anchor="middle" fill="#0f172a" font-weight="bold">Z</text><circle cx="160" cy="145" r="15" fill="#ecfdf5" stroke="#0f172a" stroke-width="1.5"/><text x="160" y="150" font-size="14" text-anchor="middle" fill="#0f172a" font-weight="bold">W</text></svg>
:::

::: exemple Le quartier à sens uniques
1. On range les sommets dans l'ordre X, Y, Z, W : la ligne d'un sommet dit où il envoie, la colonne dit d'où il reçoit.
2. La ligne X contient un 1 en colonne Y, la ligne Y un 1 en colonne Z, la ligne Z un 1 en colonne X et un 1 en colonne W, la ligne W un 1 en colonne Y.
3. La matrice est A = (0 1 0 0 ; 0 0 1 0 ; 1 0 0 1 ; 0 1 0 0), où les lignes sont séparées par des points-virgules.
4. Les sommes des lignes donnent d⁺ : 1, 1, 2, 1. Les sommes des colonnes donnent d⁻ : 1, 2, 1, 1.
5. Seuls Z et Y sont déséquilibrés : d⁺(Z) = d⁻(Z) + 1 et d⁻(Y) = d⁺(Y) + 1. Il existe donc une chaîne orientée eulérienne de Z à Y : Z-X-Y-Z-W-Y parcourt les 5 arcs une seule fois.

:::

::: piege Lire la matrice à l'envers
L'arc Z vers W est noté en ligne W et colonne Z, soit a₄₃ = 1. Cela tente parce qu'on lit souvent un tableau « colonne puis ligne » ou parce qu'on pense à « arriver en W ». Mais l'**origine** désigne la ligne et l'**extrémité** la colonne : le 1 est en ligne Z (3ᵉ) et colonne W (4ᵉ), soit a₃₄ = 1. Lire à l'envers donne la matrice transposée, qui décrit le graphe aux sens inversés.
:::

::: propriete
- d⁺(Sᵢ) est la somme de la ligne i ; d⁻(Sᵢ) est la somme de la colonne i.
- La matrice d'un graphe **non orienté** est symétrique par rapport à sa diagonale, conséquence de aᵢⱼ = aⱼᵢ, et la somme de tous ses coefficients est la somme des degrés ; celle d'un graphe orienté ne l'est pas en général.
- Un graphe orienté connexe a un cycle orienté eulérien si d⁺(S) = d⁻(S) pour tout sommet S ; il a une chaîne orientée eulérienne, non fermée, si c'est vrai partout sauf en deux sommets A et B où d⁺(A) = d⁻(A) + 1 et d⁻(B) = d⁺(B) + 1, la chaîne allant de A à B.

Cas limite : une boucle sur Sᵢ place un 1 sur la diagonale, en ligne i et colonne i ; elle compte une fois dans d⁺ et une fois dans d⁻.
:::

::: verifie
Un graphe orienté de sommets 1, 2, 3 a les arcs 1 vers 2, 1 vers 3, 2 vers 3 et une boucle en 3. Donner sa matrice associée et les d⁺.

---

Chaque ligne indique l'origine et chaque colonne l'extrémité : la matrice est A = (0 1 1 ; 0 0 1 ; 0 0 1), la boucle donnant le 1 de la diagonale en ligne 3, colonne 3. Les sommes des lignes sont d⁺(1) = 2, d⁺(2) = 1 et d⁺(3) = 1, qui retrouvent le nombre d'arcs partant de chaque sommet.
:::

::: retenir
Ligne = origine, colonne = extrémité : la somme d'une ligne donne d⁺, celle d'une colonne donne d⁻ ; l'égalité d⁺ = d⁻ partout caractérise le cycle orienté eulérien.
:::

## 🔢 Compter les chaînes avec les puissances de la matrice

Le livreur à vélo du quartier précédent part du carrefour Z et veut revenir en Z en exactement trois rues.
Combien de parcours de trois rues existent, sans les chercher un par un ?

::: propriete
Soit A la matrice associée à un graphe. Le coefficient de la ligne i et de la colonne j de la matrice Aⁿ est le **nombre de chaînes de longueur n** qui vont du sommet i au sommet j. La **longueur** d'une chaîne est le nombre d'arêtes (ou d'arcs) parcourus.
:::

::: exemple Les parcours du quartier
Avec A = (0 1 0 0 ; 0 0 1 0 ; 1 0 0 1 ; 0 1 0 0) pour les sommets X, Y, Z, W :
1. A² = A × A = (0 0 1 0 ; 1 0 0 1 ; 0 2 0 0 ; 0 0 1 0). Le coefficient de la ligne Z et de la colonne Y vaut (1 0 0 1) fois la colonne (1 0 0 1), soit 1 × 1 + 0 + 0 + 1 × 1 = 2 : il y a 2 chaînes de longueur 2 de Z à Y, à savoir Z-X-Y et Z-W-Y.
2. A³ = A² × A = (1 0 0 1 ; 0 2 0 0 ; 0 0 2 0 ; 1 0 0 1). Le coefficient en ligne Z et colonne Z vaut 2.
3. Il y a donc 2 parcours de trois rues de Z à Z : Z-X-Y-Z et Z-W-Y-Z.

:::

::: piege Confondre la longueur et le nombre de sommets
La chaîne Z-X-Y-Z passe par quatre sommets, et on cherche donc le coefficient de A⁴. Cela tente parce qu'on compte les points sur le dessin. Mais la longueur est le nombre d'**arcs** : Z-X, X-Y, Y-Z font trois arcs, et c'est bien A³ qu'il faut lire.
:::

::: methode Dénombrer les chaînes de longueur n
1. Écrire la matrice associée A : ligne = origine, colonne = extrémité.
2. Calculer Aⁿ par des produits successifs : A², puis A³ = A² × A, et ainsi de suite.
3. Lire le coefficient de la ligne de départ et de la colonne d'arrivée : c'est le nombre de chaînes de longueur n.

Cas limite : A⁰ est la matrice identité, car la seule chaîne de longueur 0 est celle qui reste sur place.
:::

::: verifie
Un graphe orienté a pour arcs 1 vers 2, 1 vers 3, 2 vers 1 et 3 vers 2. Combien de chemins de longueur 2 partent de 1 en tout ?

---

La matrice est A = (0 1 1 ; 1 0 0 ; 0 1 0). On calcule A² : sa première ligne est la ligne 1 de A fois A, soit la ligne 2 plus la ligne 3 de A, c'est-à-dire (1 0 0) + (0 1 0) = (1 1 0). Il y a donc 1 chemin de 1 à 1 (1-2-1) et 1 chemin de 1 à 2 (1-3-2), soit 1 + 1 + 0 = 2 chemins de longueur 2 partant de 1.
:::

::: retenir
Le coefficient (i, j) de Aⁿ est le nombre de chaînes de longueur n de i à j, la longueur étant un nombre d'arcs et non de sommets.
:::

## 📏 Distance et diamètre

Pour la société des cinq bornes, un technicien veut savoir en combien de câbles au minimum il peut aller de la borne A à la borne E.
Comment lire ce nombre minimal, et le plus grand de ces minimums sur tout le réseau, sans tracer le graphe ?

::: definition
La **distance** de deux sommets distincts est la longueur de la plus courte chaîne qui les relie ; elle est infinie si aucune chaîne ne les relie. La distance d'un sommet à lui-même est 0.
Le **diamètre** du graphe est la plus grande de ces distances.
:::

::: exemple Les bornes de recharge
Le graphe est celui de la première section (AB, AC, BC, CD, DE), de matrice A = (0 1 1 0 0 ; 1 0 1 0 0 ; 1 1 0 1 0 ; 0 0 1 0 1 ; 0 0 0 1 0).
1. Le coefficient (A, E) vaut 0 dans A et dans A² : aucune chaîne de longueur 1 ni 2 ne relie A à E.
2. Il vaut 1 dans A³, par la chaîne A-C-D-E : la distance de A à E est 3.
3. Aucune distance ne dépasse 3 : les couples les plus éloignés sont (A, E) et (B, E), donc le diamètre est 3.
4. Avec (A + I)ⁿ, où I est la matrice identité : (A + I)² a encore des zéros, en (A, E), (B, E) et leurs symétriques, mais tous les coefficients de (A + I)³ sont strictement positifs, ce qui redonne un diamètre de 3.

:::

::: piege Lire le coefficient comme la distance
Le coefficient (A, E) de A³ vaut 1, et on annonce une distance de 1. Cela tente parce que c'est le nombre inscrit dans la case. Mais ce nombre compte les **chaînes** de longueur 3, pas leur longueur : c'est l'**exposant** n du premier Aⁿ qui devient non nul qui donne la distance, soit 3.
:::

::: propriete
- La distance de deux sommets distincts i et j est le plus petit entier n ≥ 1 tel que le coefficient (i, j) de Aⁿ soit non nul.
- Le diamètre est le plus petit entier n tel que tous les coefficients de (A + I)ⁿ soient strictement positifs.

Cas limite : si le graphe n'est pas connexe, deux sommets de composantes différentes sont à distance infinie, et aucune puissance de A + I ne devient strictement positive.
:::

::: verifie
Quatre villes 1, 2, 3, 4 sont reliées en carré : 1-2, 2-3, 3-4 et 4-1. Quel est le diamètre ?

---

Deux villes voisines sont à distance 1. Les villes opposées, 1 et 3 d'une part, 2 et 4 d'autre part, ne sont pas adjacentes mais sont reliées par une chaîne de longueur 2, par exemple 1-2-3 : leur distance est 2. La plus grande distance est 2, donc le diamètre est 2.
:::

::: retenir
La distance est le premier exposant n pour lequel le coefficient (i, j) de Aⁿ n'est pas nul ; le diamètre est la plus grande distance du graphe.
:::

## 🎲 Graphes probabilistes et état stable

Un opérateur de téléphonie suit ses abonnés d'un mois à l'autre. Un abonné de l'offre A y reste avec la probabilité 0,8 et passe à l'offre B avec la probabilité 0,2 ; un abonné de l'offre B passe à A avec la probabilité 0,3 et reste en B avec 0,7.
Quelle répartition obtient-on au bout de quelques mois, et se stabilise-t-elle ?

::: definition
Un **graphe probabiliste** est un graphe orienté pondéré dont les sommets sont des **états** et où, pour chaque sommet, la somme des poids des arcs qui en sortent vaut 1. Le poids de l'arc de i vers j est la probabilité de passer de l'état i à l'état j.
Sa **matrice de transition** M est la matrice carrée dont le coefficient de la ligne i et de la colonne j est ce poids, 0 s'il n'y a pas d'arc. La **somme de chaque ligne** de M vaut 1.
L'**état probabiliste** à l'étape n est la matrice ligne pₙ = (aₙ bₙ) qui donne les probabilités d'être dans chaque état.
:::

Les poids qui sortent de A, 0,8 et 0,2, font 1 : c'est la première ligne de M.

::: figure Le graphe de l'opérateur : une boucle par offre pour « rester », un arc pour « changer »
<svg viewBox="0 0 320 150"><title>Graphe probabiliste des offres A et B</title><path d="M 83 72 C 66 14 122 14 105 72" fill="none" stroke="#0f172a" stroke-width="1.8"/><polygon points="105.0,72.0 99.6,64.5 108.4,62.0" fill="#0f172a"/><text x="94" y="22" font-size="13" text-anchor="middle" fill="#0f172a">0,8</text><path d="M 215 72 C 198 14 254 14 237 72" fill="none" stroke="#0f172a" stroke-width="1.8"/><polygon points="237.0,72.0 231.6,64.5 240.4,62.0" fill="#0f172a"/><text x="226" y="22" font-size="13" text-anchor="middle" fill="#0f172a">0,7</text><line x1="119" y1="85" x2="201" y2="85" stroke="#0f172a" stroke-width="1.8"/><polygon points="201.0,85.0 192.7,88.5 192.7,81.5" fill="#0f172a"/><text x="160" y="78" font-size="13" text-anchor="middle" fill="#0f172a">0,2</text><line x1="201" y1="105" x2="119" y2="105" stroke="#0f172a" stroke-width="1.8"/><polygon points="119.0,105.0 127.3,101.5 127.3,108.5" fill="#0f172a"/><text x="160" y="122" font-size="13" text-anchor="middle" fill="#0f172a">0,3</text><circle cx="94" cy="95" r="26" fill="#ecfdf5" stroke="#0f172a" stroke-width="1.5"/><text x="94" y="101" font-size="16" text-anchor="middle" fill="#0f172a" font-weight="bold">A</text><circle cx="226" cy="95" r="26" fill="#ecfdf5" stroke="#0f172a" stroke-width="1.5"/><text x="226" y="101" font-size="16" text-anchor="middle" fill="#0f172a" font-weight="bold">B</text></svg>
:::

::: exemple L'opérateur et ses deux offres
On a M = (0,8 0,2 ; 0,3 0,7) et, au départ, p₀ = (0,4 0,6) : 40 % des abonnés sont en A.
1. La règle est p₁ = p₀ × M, car on multiplie la **ligne** d'état à **gauche** de M.
2. Première composante : 0,4 × 0,8 + 0,6 × 0,3 = 0,32 + 0,18 = 0,5 ; seconde : 0,4 × 0,2 + 0,6 × 0,7 = 0,08 + 0,42 = 0,5. D'où p₁ = (0,5 0,5).
3. De même pour p₂ = p₁ × M : première composante 0,5 × 0,8 + 0,5 × 0,3 = 0,55, seconde 0,5 × 0,2 + 0,5 × 0,7 = 0,45, d'où p₂ = (0,55 0,45).
4. En général pₙ = p₀ × Mⁿ, et la somme des deux composantes reste 1 à chaque étape, ce qui sert de contrôle.

:::

::: piege Multiplier l'état à droite de la matrice
On calcule M × p₀ en traitant p₀ comme une colonne (0,4 ; 0,6) et on obtient (0,8 × 0,4 + 0,2 × 0,6 ; 0,3 × 0,4 + 0,7 × 0,6) = (0,44 ; 0,54). Cela tente parce qu'on écrit souvent « la matrice agit sur le vecteur ». Mais la somme 0,44 + 0,54 = 0,98 n'est pas 1 : le résultat n'est pas un état probabiliste. Pour une matrice de transition, la ligne d'état se met à **gauche** : pₙ₊₁ = pₙ × M.
:::

::: propriete
- Si le graphe est d'ordre 2 et que M ne contient aucun 0, pₙ converge vers un **état stable** p, qui ne dépend pas de p₀.
- p est l'unique solution de p × M = p avec x + y = 1, où p = (x y).
- Pour l'opérateur : x = 0,8x + 0,3y donne 0,2x = 0,3y ; avec y = 1 − x, on a 0,2x = 0,3 − 0,3x, donc x = 0,6 et p = (0,6 0,4). Contrôle : 0,2 × 0,6 + 0,7 × 0,4 = 0,4 ✓.

Cas limite : avec M = (0 1 ; 1 0), qui contient des zéros, l'état (1 0) devient (0 1) puis revient à (1 0) : il oscille et ne converge pas, d'où l'hypothèse « aucun 0 ».
:::

::: verifie
On a M = (0,9 0,1 ; 0,3 0,7) et p₀ = (0,2 0,8). Calculer p₁, puis l'état stable.

---

La ligne d'état se met à gauche : première composante 0,2 × 0,9 + 0,8 × 0,3 = 0,18 + 0,24 = 0,42, seconde 0,2 × 0,1 + 0,8 × 0,7 = 0,02 + 0,56 = 0,58, d'où p₁ = (0,42 0,58), de somme 1 ✓. L'état stable (x y) vérifie x = 0,9x + 0,3y, d'où 0,1x = 0,3y, soit x = 3y ; avec x + y = 1, on obtient y = 0,25 et x = 0,75. L'état stable est (0,75 0,25).
:::

::: retenir
Une matrice de transition a des lignes de somme 1 ; pₙ₊₁ = pₙ × M, donc pₙ = p₀ × Mⁿ ; si M n'a aucun zéro (ordre 2), l'état stable est l'unique solution de p × M = p de somme 1.
:::

> 🏆 Tu sais lire un réseau, trancher l'existence d'un parcours eulérien, colorer sans conflit, trouver la route la plus courte, manier la matrice d'un graphe orienté, compter les chaînes par les puissances et prévoir l'équilibre d'une évolution probabiliste. Il ne reste plus qu'à t'entraîner.
