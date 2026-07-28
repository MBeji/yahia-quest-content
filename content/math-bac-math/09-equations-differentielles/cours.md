# ⚔️ Équations différentielles — quand la dérivée dicte la fonction

> 💡 «Jusqu'ici on te donnait la fonction et tu cherchais sa dérivée. Ici on te donne une relation entre la fonction et sa dérivée, et tu dois retrouver la fonction : c'est ainsi que la science écrit ses lois.»

En 1673, Huygens cherche un pendule dont la période ne dépende plus de l'amplitude. Il trouve une condition d'un genre nouveau : s″ + Ks = 0 — une équation où l'inconnue n'est pas un nombre, mais **une fonction**. Un noyau radioactif qui se désintègre, un corps qui refroidit, un condensateur qui se charge, une population qui prolifère : tous obéissent au même type de relation. Ce chapitre clôt le tome d'analyse et **réunit tout ce que tu as forgé** — les primitives (chapitre 5), l'intégrale (chapitre 6), le logarithme (chapitre 7) et surtout l'exponentielle (chapitre 8), qui est ici l'arme absolue : c'est la seule fonction qui soit, à un facteur près, sa propre dérivée.

## 🏰 Une équation dont l'inconnue est une fonction

Résoudre 2x + 5 = 13, c'est chercher un **nombre**. Résoudre y′ = 2y, c'est chercher une **fonction** dérivable dont la dérivée est le double : ici l'inconnue y désigne une fonction, et y′ sa dérivée.

> **Vocabulaire** — « Une équation de la forme y′ = ay, où l'inconnue y est une fonction et a est un réel, est appelée équation différentielle linéaire du premier ordre à coefficient constant. Résoudre dans ℝ une équation de la forme y′ = ay, c'est trouver toutes les fonctions dérivables sur ℝ qui vérifient y′ = ay. Ces fonctions sont appelées solutions sur ℝ de l'équation y′ = ay. »

Le premier geste, avant toute résolution, est donc de savoir **vérifier** qu'une fonction donnée est solution : on la dérive et on réinjecte.

_Exemple détaillé_ — la fonction f : x ↦ e^(−x) est-elle solution de y′ = −y ? On dérive : f′(x) = −e^(−x). On compare à −f(x) = −e^(−x). Les deux expressions coïncident pour tout réel x : **f est solution**. Reprenons avec g : x ↦ −2e^(−x) : g′(x) = 2e^(−x) et −g(x) = 2e^(−x) ✓. Et avec h : x ↦ 0,5e^(−x) : h′(x) = −0,5e^(−x) = −h(x) ✓.

Trois fonctions différentes, une même équation : une équation différentielle n'a donc pas **une** solution mais toute une **famille**. C'est la différence essentielle avec une équation numérique.

> 🗡️ Pour tester une fonction candidate, ne cherche jamais à « résoudre » : dérive-la, remplace dans l'équation, et vérifie que les deux membres sont égaux **pour tout x**. C'est la vérification qui te sauvera au bac quand un énoncé te souffle la réponse.

## 🧮 Le cas le plus simple : y′ = f(x)

Quand le second membre ne dépend que de x, l'équation y′ = f(x) demande exactement ceci : trouver les fonctions dont la dérivée est f. Tu sais déjà le faire — ce sont les **primitives** de f (chapitre 5).

> **Règle** — Si f est continue sur un intervalle I et si F est une primitive de f sur I, les solutions de y′ = f(x) sur I sont les fonctions x ↦ F(x) + c, c ∈ ℝ.

_Exemple détaillé_ — résolvons y′ = 3x² − 2x sur ℝ. Une primitive du second membre est F(x) = x³ − x², donc les solutions sont les fonctions y : x ↦ x³ − x² + c. _Vérification_ : (x³ − x² + c)′ = 3x² − 2x ✓. Si de plus on impose y(1) = 5, alors 1 − 1 + c = 5, donc c = 5 et y(x) = x³ − x² + 5. _Contrôle_ : y(1) = 1 − 1 + 5 = 5 ✓.

La constante c est le prix de la primitivation : une seule condition supplémentaire suffit à la fixer. Retiens ce schéma, il se répète dans tout le chapitre : **famille de solutions, puis une condition qui en sélectionne une seule.**

## ⚡ L'équation reine : y′ = ay

Passons au cœur du chapitre : le second membre contient maintenant l'inconnue elle-même.

> **Théorème** — « Soit a un réel. L'ensemble des solutions de l'équation différentielle y′ = ay est l'ensemble des fonctions définies sur ℝ par f : x ↦ ke^(ax), où k est un réel quelconque. »

_Démonstration (à connaître)_ — dans un sens : si f(x) = ke^(ax), alors f′(x) = ake^(ax) = af(x) ✓. Dans l'autre : soit f une solution, et posons g(x) = f(x)e^(−ax). Alors g′(x) = f′(x)e^(−ax) − af(x)e^(−ax) = (f′(x) − af(x))e^(−ax) = 0. Donc g est constante, égale à un réel k, et f(x) = ke^(ax). ∎

Toute la famille se déduit donc d'une seule courbe par un facteur k : le signe de a décide de la croissance (a > 0) ou de la décroissance (a < 0) de l'exponentielle, le signe de k décide du côté de l'axe.

::: figure Les solutions de y′ = −y forment une famille de courbes emboîtées, chacune repérée par son coefficient k ; deux courbes de la famille ne se coupent jamais.
<svg viewBox="0 0 320 210"><path d="M40 105 H305" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M70 190 V15" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M305 105 l-7 -3.5 l0 7 z" fill="#0f172a"/><path d="M70 15 l-3.5 7 l7 0 z" fill="#0f172a"/><polyline points="60,19.5 70,35 95,62.5 120,79.2 170,95.5 220,101.5 270,103.7 300,104.3" fill="none" stroke="#b45309" stroke-width="2.4" stroke-linecap="round"/><polyline points="40,41.2 55,57.8 70,70 95,83.8 120,92.1 170,100.3 220,103.3 270,104.4 300,104.6" fill="none" stroke="#0f6e56" stroke-width="2.4" stroke-linecap="round"/><polyline points="40,168.8 55,152.2 70,140 95,126.2 120,117.9 170,109.7 220,106.7 270,105.6 300,105.4" fill="none" stroke="#7c3aed" stroke-width="2.4" stroke-linecap="round"/><text x="105" y="45" font-size="12" font-weight="700" fill="#b45309">k = 2</text><text x="130" y="72" font-size="12" font-weight="700" fill="#0f6e56">k = 1</text><text x="130" y="134" font-size="12" font-weight="700" fill="#7c3aed">k = −1</text><text x="62" y="118" font-size="12" font-weight="700" fill="#0f172a">O</text><text x="285" y="98" font-size="11" fill="#0f172a">x</text></svg>
:::

_Exemple détaillé_ — résolvons (E) : 2y′ + 3y = 0. **Premier geste** : isoler y′ en divisant par le coefficient de y′, ici 2. On obtient y′ = −(3/2)y, donc a = −3/2 :

$$ f(x) = ke^(−3x/2), k ∈ ℝ $$

Cherchons celle qui vérifie f(0) = −3 : f(0) = ke^0 = k, donc k = −3 et f(x) = −3e^(−3x/2). _Vérification complète_ : f′(x) = −3 × (−3/2)e^(−3x/2) = (9/2)e^(−3x/2), donc 2f′(x) + 3f(x) = 9e^(−3x/2) − 9e^(−3x/2) = 0 ✓, et f(0) = −3e^0 = −3 ✓.

_Exemple_ — la fonction x ↦ 2e^(2x) : sa dérivée est 4e^(2x), c'est-à-dire 2 × (2e^(2x)). Elle est donc solution de **y′ = 2y** — et non de y′ = 4y, dont les solutions sont les x ↦ ke^(4x).

> ⚠️ Le coefficient a est celui qui apparaît **dans l'exposant**, pas devant l'exponentielle. Et n'oublie jamais le facteur k : écrire « la solution est e^(ax) » revient à n'en donner qu'une sur une infinité.

> ⚠️ Une solution de y′ = ay n'est pas croissante parce que a est négatif ou positif : si f(x) = ke^(−2x), alors f′(x) = −2ke^(−2x), du signe de **−k**. Pour k > 0 la fonction décroît, pour k < 0 elle croît, pour k = 0 elle est constante.

## 🎯 Une condition initiale, une seule solution

Une famille de courbes, un point imposé : il n'en reste qu'une. C'est ce qu'on appelle une **condition initiale** (ou problème de Cauchy).

> **Théorème** — « Soit a un réel non nul. Pour tous réels x₀ et y₀, l'équation y′ = ay admet une unique solution qui prend la valeur y₀ en x₀. C'est la fonction définie sur ℝ par f : x ↦ y₀e^(a(x−x₀)). »

_Vérification de la formule_ — f′(x) = ay₀e^(a(x−x₀)) = af(x) ✓, et f(x₀) = y₀e^0 = y₀ ✓. L'unicité vient du théorème précédent : toute solution s'écrit ke^(ax), et la condition ke^(ax₀) = y₀ fixe k = y₀e^(−ax₀) sans ambiguïté.

_Exemple détaillé_ — trouvons la solution de y′ − y/2 = 0 telle que y(−1) = e. On écrit d'abord y′ = (1/2)y, donc a = 1/2, avec x₀ = −1 et y₀ = e :

$$ f(x) = e × e^((1/2)(x + 1)) = e^((x + 3)/2) $$

_Vérification_ : f′(x) = (1/2)e^((x+3)/2) = (1/2)f(x), donc f′ − f/2 = 0 ✓. Et f(−1) = e^(2/2) = e ✓.

_Exemple détaillé_ — solution de −3y′ − y = 0 telle que y(ln 8) = 1. On isole : −3y′ = y, donc y′ = −(1/3)y, a = −1/3. La formule donne f(x) = 1 × e^(−(1/3)(x − ln 8)) = e^(−x/3) × e^((ln 8)/3). Or e^((ln 8)/3) = 8^(1/3) = 2, d'où :

$$ f(x) = 2e^(−x/3) $$

_Vérification_ : f′(x) = −(2/3)e^(−x/3), donc −3f′(x) − f(x) = 2e^(−x/3) − 2e^(−x/3) = 0 ✓. Et f(ln 8) = 2e^(−(ln 8)/3) = 2 × 8^(−1/3) = 2/2 = 1 ✓.

_Exemple (lecture d'une condition sur la dérivée)_ — si f est la solution de y′ = 3y telle que f′(1) = 3, alors, puisque f′(1) = 3f(1), on obtient 3f(1) = 3, donc **f(1) = 1**. L'équation elle-même transforme une donnée sur f′ en une donnée sur f.

> 🗡️ Deux chemins mènent au même résultat : appliquer la formule x ↦ y₀e^(a(x−x₀)), ou partir de f(x) = ke^(ax) et calculer k avec la condition. Le second est plus sûr quand x₀ ≠ 0 et que les exposants s'emmêlent.

## 🔮 Le second membre constant : y′ = ay + b

Une constante s'ajoute au second membre. Une seule idée suffit : **repérer la solution constante** et se ramener au cas précédent.

Si y est la fonction constante égale à c, alors y′ = 0 et l'équation devient 0 = ac + b, soit c = −b/a (possible car a ≠ 0). La fonction constante **−b/a** est donc toujours solution.

> **Théorème** — « Soit a et b deux réels tels que a ≠ 0. L'ensemble des solutions de l'équation différentielle y′ = ay + b est l'ensemble des fonctions f : x ↦ ke^(ax) − b/a, où k est un réel quelconque. De plus pour tous réels x₀, y₀, la fonction f : x ↦ (y₀ + b/a)e^(a(x−x₀)) − b/a est l'unique solution de y′ = ay + b, telle que f(x₀) = y₀. »

_Démonstration (le changement de fonction)_ — posons h(x) = f(x) + b/a. Alors h′ = f′ et : f est solution de y′ = ay + b ⟺ h′ = a(h − b/a) + b = ah. Donc h est solution de y′ = ay, c'est-à-dire h(x) = ke^(ax), et f(x) = ke^(ax) − b/a. ∎

_Exemple détaillé_ — montrons que f : x ↦ e^(−2x) + 3 est solution de (E) : y′ = −2y + 6, puis donnons toutes les solutions. On dérive : f′(x) = −2e^(−2x). On calcule le second membre : −2f(x) + 6 = −2e^(−2x) − 6 + 6 = −2e^(−2x) ✓ : les deux coïncident. Ici a = −2 et b = 6, donc −b/a = −6/(−2) = 3, et les solutions de (E) sont les fonctions x ↦ ke^(−2x) + 3.

_Exemple détaillé (avec condition initiale)_ — résolvons y′ + 3y + 3/4 = 0 avec y(−1) = 0. On isole : y′ = −3y − 3/4, donc a = −3 et b = −3/4, d'où −b/a = −(−3/4)/(−3) = −1/4. Les solutions sont x ↦ ke^(−3x) − 1/4. La condition donne ke^3 − 1/4 = 0, soit k = (1/4)e^(−3), et donc :

$$ f(x) = (1/4)e^(−3(x + 1)) − 1/4 $$

_Vérification complète_ : f′(x) = −(3/4)e^(−3(x+1)) ; et −3f(x) − 3/4 = −(3/4)e^(−3(x+1)) + 3/4 − 3/4 = −(3/4)e^(−3(x+1)) ✓. Condition : f(−1) = (1/4)e^0 − 1/4 = 0 ✓.

_Exemple (quand k vaut 0)_ — soit f la solution de y′ = −y + 1 telle que f(0) = 1. Ici a = −1, b = 1, donc −b/a = 1 et f(x) = ke^(−x) + 1. La condition donne k + 1 = 1, donc k = 0 : **f est la fonction constante égale à 1**, donc strictement positive sur ℝ.

> ⚠️ Le terme constant est **−b/a**, pas +b/a ni b/a. Le réflexe qui ne trompe jamais : vérifie que la constante trouvée annule bien ay + b (ici a × (−b/a) + b = −b + b = 0).

## 🧪 Le régime transitoire : quand la physique parle

Un circuit série formé d'un générateur de force électromotrice E, d'une bobine d'inductance L et de résistance r impose à l'intensité i l'équation Li′ + ri = E. Avec E = 10 V, r = 100 Ω, L = 0,2 H et une intensité nulle à l'instant 0 :

$$ 0,2 i′ + 100 i = 10 ⟺ i′ = −500 i + 50 $$

Ici a = −500 et b = 50, donc −b/a = 0,1. Les solutions sont i(t) = ke^(−500t) + 0,1, et i(0) = 0 donne k = −0,1 :

$$ i(t) = 0,1(1 − e^(−500t)) $$

_Vérification complète_ : i′(t) = 0,1 × 500e^(−500t) = 50e^(−500t), et −500i(t) + 50 = −50 + 50e^(−500t) + 50 = 50e^(−500t) ✓. Condition : i(0) = 0,1(1 − 1) = 0 ✓. Enfin, comme e^(−500t) → 0 quand t → +∞, on a i(t) → 0,1 : l'intensité tend vers **E/r = 10/100 = 0,1 A**, la loi d'Ohm du régime permanent.

::: figure Le courant part de zéro et monte vers sa valeur limite E/r : le terme en e^(−500t) est le régime transitoire, qui s'efface en quelques millisecondes.
<svg viewBox="0 0 320 200"><path d="M45 160 H305" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M60 175 V25" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M305 160 l-7 -3.5 l0 7 z" fill="#0f172a"/><path d="M60 25 l-3.5 7 l7 0 z" fill="#0f172a"/><line x1="55" y1="60" x2="300" y2="60" stroke="#b45309" stroke-width="1.4" stroke-dasharray="5 3"/><polyline points="60,160 83,120.7 106,96.8 129,82.3 152,73.5 175,68.2 198,65 244,61.8 290,60.7" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/><text x="230" y="54" font-size="12" font-weight="700" fill="#b45309">E/r = 0,1 A</text><text x="288" y="176" font-size="11" fill="#0f172a">t (s)</text><text x="34" y="36" font-size="11" fill="#0f172a">i (A)</text><text x="52" y="174" font-size="11" fill="#0f172a">0</text></svg>
:::

> 🗡️ Dans tout problème physique du bac, la démarche est la même en trois temps : traduire l'énoncé en y′ = ay + b, écrire la famille ke^(ax) − b/a, puis fixer k avec la condition à l'instant 0. La limite en +∞ vaut alors **−b/a** dès que a < 0.

## ☢️ Décroissance radioactive et demi-vie

Une substance radioactive perd ses noyaux à une vitesse proportionnelle au nombre de noyaux présents. Si N(t) est ce nombre à l'instant t et λ > 0 la constante radioactive :

$$ N′(t) = −λN(t), N(0) = N₀ ⟹ N(t) = N₀e^(−λt) $$

_Vérification_ : N′(t) = −λN₀e^(−λt) = −λN(t) ✓ et N(0) = N₀ ✓.

**Demi-vie.** On cherche T₀.₅ tel que N(T₀.₅) = N₀/2, c'est-à-dire e^(−λT₀.₅) = 1/2. En composant par ln : −λT₀.₅ = −ln 2, donc :

$$ T₀.₅ = (ln 2)/λ $$

Ce nombre ne dépend **pas** de N₀ : quelle que soit la quantité de départ, il en reste la moitié après la même durée. C'est ce qui rend la datation possible.

::: figure Sur chaque intervalle de durée T, la proportion restante est divisée par 2, quel que soit le point de départ choisi sur la courbe.
<svg viewBox="0 0 320 200"><path d="M45 165 H305" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M60 180 V25" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M305 165 l-7 -3.5 l0 7 z" fill="#0f172a"/><path d="M60 25 l-3.5 7 l7 0 z" fill="#0f172a"/><polyline points="60,55 95,87.2 130,110 165,126.1 200,137.5 235,145.6 270,151.3" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/><line x1="60" y1="110" x2="130" y2="110" stroke="#b45309" stroke-width="1.3" stroke-dasharray="4 3"/><line x1="130" y1="110" x2="130" y2="165" stroke="#b45309" stroke-width="1.3" stroke-dasharray="4 3"/><line x1="60" y1="137.5" x2="200" y2="137.5" stroke="#7c3aed" stroke-width="1.3" stroke-dasharray="4 3"/><line x1="200" y1="137.5" x2="200" y2="165" stroke="#7c3aed" stroke-width="1.3" stroke-dasharray="4 3"/><circle cx="60" cy="55" r="3" fill="#0f172a"/><text x="30" y="59" font-size="11" font-weight="700" fill="#0f172a">N₀</text><text x="24" y="114" font-size="11" font-weight="700" fill="#b45309">N₀/2</text><text x="24" y="141" font-size="11" font-weight="700" fill="#7c3aed">N₀/4</text><text x="130" y="179" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a">T</text><text x="200" y="179" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a">2T</text><text x="286" y="181" font-size="11" fill="#0f172a">t</text></svg>
:::

_Exemple détaillé (carbone 14)_ — sa demi-vie vaut T₀.₅ = 5730 ans. On en déduit λ = (ln 2)/5730 ≈ 0,6931/5730 ≈ 1,21 × 10⁻⁴ (par an). Un fragment d'os contient 60 % de la quantité initiale : on résout e^(−λt) = 0,6, soit −λt = ln 0,6, donc t = −(ln 0,6)/λ. Numériquement :

$$ t = 5730 × (−ln 0,6)/(ln 2) ≈ 5730 × 0,5108/0,6931 ≈ 4223 ans $$

_Contrôle_ — 60 % est un peu plus que la moitié : l'âge trouvé doit être un peu **inférieur** à une demi-vie (5730 ans). C'est bien le cas ✓.

_Exemple détaillé (loi de refroidissement de Newton)_ — un corps perd sa chaleur à une vitesse proportionnelle à l'écart avec l'air ambiant à 25 °C : f′(t) = a(f(t) − 25). Posons g = f − 25 : alors g′ = f′ = ag, donc g(t) = g(0)e^(at) et f(t) = 25 + (f(0) − 25)e^(at). Avec f(0) = 100 : f(t) = 25 + 75e^(at). La donnée f(15) = 75 impose 75e^(15a) = 50, soit e^(15a) = 2/3 et a = (ln(2/3))/15 ≈ −0,0270. _Vérifications_ : f(0) = 25 + 75 = 100 ✓ ; f(15) = 25 + 75 × (2/3) = 75 ✓ ; f′(t) = 75ae^(at) = a(f(t) − 25) ✓.

> ⚠️ « Au bout de combien de temps le corps atteint-il 25 °C ? » — **jamais** exactement : 75e^(at) ne s'annule pas. La température **tend** vers 25 °C. Une telle question ne peut porter que sur un seuil, du type f(t) < 25,1.

## 🌊 Les oscillations : y″ + ω²y = 0

On passe à l'ordre deux. Ici la dérivée seconde est l'opposée de la fonction, à un facteur positif près : au lieu de croître ou décroître, la solution **oscille**.

> **Vocabulaire** — « Une équation de la forme y″ + ω²y = 0, où l'inconnue y est une fonction et ω est un réel, est appelée équation différentielle linéaire du second ordre à coefficients constants. Résoudre une équation de la forme y″ + ω²y = 0, c'est trouver toutes les fonctions deux fois dérivables sur ℝ qui la vérifient. »

> **Théorème** — « Soit ω un réel non nul. L'ensemble des solutions de l'équation différentielle y″ + ω²y = 0 est l'ensemble des fonctions définies sur ℝ par f(x) = A sin(ωx) + B cos(ωx), (A, B) ∈ ℝ². »

_Vérification_ — f′(x) = Aω cos(ωx) − Bω sin(ωx), puis f″(x) = −Aω² sin(ωx) − Bω² cos(ωx) = −ω²f(x). Donc f″ + ω²f = 0 ✓, quels que soient A et B.

> **Théorème (condition initiale)** — « Soit ω un réel non nul et x₀, y₀ deux réels. L'équation y″ + ω²y = 0 admet une unique solution dans ℝ vérifiant f(0) = x₀ et f′(0) = y₀. C'est la fonction définie sur ℝ par f(x) = (y₀/ω) sin(ωx) + x₀ cos(ωx). »

À l'ordre deux il faut donc **deux** conditions (la valeur et la pente en un point), là où l'ordre un n'en demandait qu'une. _Conséquence_ : la fonction nulle est l'unique solution vérifiant y(0) = y′(0) = 0.

_Exemple détaillé_ — résolvons (E) : y″ + 9y = 0 avec f(0) = √3/2 et f′(0) = 3/2. Comme 9 = 3², on a ω = 3 et f(x) = A sin(3x) + B cos(3x). Alors f(0) = B = √3/2. Ensuite f′(x) = 3A cos(3x) − 3B sin(3x), donc f′(0) = 3A = 3/2, soit A = 1/2 :

$$ f(x) = (1/2)sin(3x) + (√3/2)cos(3x) $$

_Vérification complète_ : f″(x) = −(9/2)sin(3x) − (9√3/2)cos(3x) = −9f(x), donc f″ + 9f = 0 ✓ ; f(0) = √3/2 ✓ ; f′(0) = 3 × 1/2 = 3/2 ✓.

_Exemple détaillé_ — solution de y″ + 2y = 0 avec y(0) = 1 et y′(0) = √2. Ici ω² = 2 donc ω = √2, et la formule donne f(x) = (√2/√2)sin(√2 x) + 1 × cos(√2 x) = sin(√2 x) + cos(√2 x). _Vérification_ : f(0) = 0 + 1 = 1 ✓ ; f′(x) = √2 cos(√2 x) − √2 sin(√2 x), donc f′(0) = √2 ✓ ; f″(x) = −2sin(√2 x) − 2cos(√2 x) = −2f(x) ✓.

> ⚠️ Dans y″ + ω²y = 0, **ω est la racine carrée** du coefficient de y : pour y″ + 9y = 0 c'est ω = 3, pas 9. Erreur classique : écrire A sin(9x) + B cos(9x), qui vérifie y″ + 81y = 0.

> ⚠️ Le signe est décisif. Seul le cas y″ + ω²y = 0 (oscillant) est au programme ; l'équation y″ − ω²y = 0 n'a pas les mêmes solutions et n'est pas traitée dans ce chapitre.

## 🎼 Amplitude et phase : la forme r cos(ωx − φ)

Une somme A sin(ωx) + B cos(ωx) se réécrit toujours comme **une seule** sinusoïde. C'est la forme qui donne l'amplitude et permet de résoudre f(x) = m.

En développant r cos(ωx − φ) = r cos φ cos(ωx) + r sin φ sin(ωx), on identifie : **B = r cos φ** et **A = r sin φ**. D'où :

$$ r = √(A² + B²), cos φ = B/r, sin φ = A/r $$

_Exemple détaillé_ — reprenons f(x) = (1/2)sin(3x) + (√3/2)cos(3x). Alors r = √(1/4 + 3/4) = 1, puis cos φ = √3/2 et sin φ = 1/2, donc φ = π/6 (dans ]−π, π]) :

$$ f(x) = cos(3x − π/6) $$

_Vérification_ : cos(3x − π/6) = cos(3x)cos(π/6) + sin(3x)sin(π/6) = (√3/2)cos(3x) + (1/2)sin(3x) ✓ — c'est bien la même fonction. On lit alors directement : amplitude 1, période 2π/3, et f(x) = 1 exactement quand 3x − π/6 = 2kπ, soit x = π/18 + 2kπ/3.

_Exemple détaillé (mobile oscillant)_ — un mobile a une accélération proportionnelle à sa position, de coefficient −π²/4 : x″(t) + (π²/4)x(t) = 0, donc ω = π/2 et x(t) = A sin(πt/2) + B cos(πt/2). Les données x(1) = 2 et x(2) = 0 donnent : x(1) = A × 1 + B × 0 = A = 2, et x(2) = A × 0 + B × (−1) = −B = 0, donc B = 0 :

$$ x(t) = 2 sin(πt/2) $$

_Vérifications_ : x(1) = 2 sin(π/2) = 2 ✓ ; x(2) = 2 sin(π) = 0 ✓ ; x″(t) = −2(π²/4)sin(πt/2) = −(π²/4)x(t) ✓. À l'instant 0, le mobile est à l'origine (x(0) = 0) et sa vitesse vaut x′(0) = 2 × (π/2)cos 0 = **π m/s**. La période vaut 2π/ω = 2π/(π/2) = **4 s**.

::: figure L'élongation oscille entre −2 et 2 et se répète toutes les 4 secondes : l'amplitude dépend des conditions initiales, la période seulement de ω.
<svg viewBox="0 0 340 190"><path d="M40 95 H325" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M55 175 V20" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M325 95 l-7 -3.5 l0 7 z" fill="#0f172a"/><path d="M55 20 l-3.5 7 l7 0 z" fill="#0f172a"/><line x1="50" y1="40" x2="315" y2="40" stroke="#b45309" stroke-width="1.2" stroke-dasharray="5 3"/><line x1="50" y1="150" x2="315" y2="150" stroke="#b45309" stroke-width="1.2" stroke-dasharray="5 3"/><polyline points="55,95 62.8,74 70.6,56.1 78.4,44.2 86.3,40 94.1,44.2 101.9,56.1 109.7,74 117.5,95 125.3,116 133.1,133.9 140.9,145.8 148.8,150 156.6,145.8 164.4,133.9 172.2,116 180,95 187.8,74 195.6,56.1 203.4,44.2 211.3,40 219.1,44.2 226.9,56.1 234.7,74 242.5,95 250.3,116 258.1,133.9 265.9,145.8 273.8,150 281.6,145.8 289.4,133.9 297.2,116 305,95" fill="none" stroke="#0f6e56" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/><line x1="55" y1="170" x2="180" y2="170" stroke="#7c3aed" stroke-width="1.4"/><line x1="55" y1="166" x2="55" y2="174" stroke="#7c3aed" stroke-width="1.4"/><line x1="180" y1="166" x2="180" y2="174" stroke="#7c3aed" stroke-width="1.4"/><text x="117" y="166" text-anchor="middle" font-size="11" font-weight="700" fill="#7c3aed">T = 4 s</text><text x="40" y="44" font-size="11" font-weight="700" fill="#b45309">2</text><text x="36" y="154" font-size="11" font-weight="700" fill="#b45309">−2</text><text x="306" y="112" font-size="11" fill="#0f172a">t (s)</text><text x="26" y="30" font-size="11" fill="#0f172a">x (m)</text></svg>
:::

> 🗡️ La période 2π/ω et l'amplitude r racontent deux histoires distinctes : la période est imposée par l'**équation**, l'amplitude par les **conditions initiales**. C'est exactement l'isochronisme cherché par Huygens.

## 🗝️ Deux techniques que le bac réclame

**a) Second membre non nul : une solution particulière + l'équation homogène.** Quand l'équation s'écrit y′ + αy = φ(x) avec φ non constante, l'énoncé te fait toujours deviner une solution particulière g d'une forme imposée, puis conclure.

_Exemple détaillé_ — (E) : y′ + 2y = x². L'équation homogène (E₀) : y′ + 2y = 0 a pour solutions x ↦ ke^(−2x). Cherchons un trinôme g(x) = αx² + βx + γ solution de (E) :

$$ g′ + 2g = 2αx + β + 2αx² + 2βx + 2γ = 2αx² + (2α + 2β)x + (β + 2γ) $$

L'identification avec x² donne 2α = 1, 2α + 2β = 0 et β + 2γ = 0, soit α = 1/2, β = −1/2, γ = 1/4. _Vérification_ : g(x) = x²/2 − x/2 + 1/4, g′(x) = x − 1/2, donc g′ + 2g = x − 1/2 + x² − x + 1/2 = x² ✓.

Enfin, f est solution de (E) ⟺ (f − g)′ + 2(f − g) = (f′ + 2f) − (g′ + 2g) = x² − x² = 0, c'est-à-dire ⟺ f − g est solution de (E₀). Les solutions de (E) sont donc :

$$ f(x) = ke^(−2x) + x²/2 − x/2 + 1/4, k ∈ ℝ $$

**b) Réduction d'ordre : poser z = y′.** Quand l'équation du second ordre ne contient pas y lui-même, l'inconnue auxiliaire z = y′ ramène au premier ordre.

_Exemple détaillé_ — (E) : y″ = 2y′. Posons z = y′ : l'équation devient z′ = 2z, donc z(x) = ke^(2x). Il reste à primitiver : y′(x) = ke^(2x) donne y(x) = (k/2)e^(2x) + c. Cherchons la solution vérifiant f′(0) = 1 et f(0) = 2. De f′(x) = ke^(2x) on tire f′(0) = k = 1, donc f′(x) = e^(2x) et f(x) = e^(2x)/2 + c ; puis f(0) = 1/2 + c = 2 donne c = 3/2 :

$$ f(x) = e^(2x)/2 + 3/2 $$

_Vérification complète_ : f′(x) = e^(2x), f″(x) = 2e^(2x) = 2f′(x) ✓ ; f(0) = 1/2 + 3/2 = 2 ✓ ; f′(0) = 1 ✓.

> 🗡️ Reconnais le type avant de calculer : y′ = f(x) → primitive ; y′ = ay → ke^(ax) ; y′ = ay + b → ke^(ax) − b/a ; y″ + ω²y = 0 → A sin(ωx) + B cos(ωx) ; y″ = ay′ + b → poser z = y′. Quatre lignes de mémoire, et presque tout le chapitre est couvert.

> 🏆 Neuvième porte franchie, héros : tu clos le tome d'analyse. Tu sais lire une loi physique comme une équation, en sortir une famille de fonctions, la resserrer par une condition initiale, et vérifier ton résultat en le réinjectant — le seul contrôle qui ne ment jamais. Ce que la dérivée avait dispersé, l'exponentielle et les fonctions trigonométriques l'ont rassemblé. Le tome 2 t'attend, et il commence par un nombre dont le carré vaut −1.
