# ⚔️ Équations différentielles — quand la dérivée dicte la fonction

> 💡 «Jusqu'ici on te donnait la fonction et tu cherchais sa dérivée. Ici on te donne une relation entre la fonction et sa dérivée, et tu dois retrouver la fonction : c'est ainsi que la science écrit ses lois.»

En 1673, Huygens cherche un pendule dont la période ne dépende plus de l'amplitude. Il trouve une condition d'un genre nouveau : s″ + Ks = 0 — une équation où l'inconnue n'est pas un nombre, mais **une fonction**. Un noyau radioactif qui se désintègre, un corps qui refroidit, un condensateur qui se charge : tous obéissent au même type de relation. Huit notions te mènent de y′ = ay jusqu'à y″ + ω²y = 0. Ce chapitre clôt le tome d'analyse et **réunit tout ce que tu as forgé** : les primitives (chapitre 6), l'intégrale (chapitre 7), le logarithme (chapitre 8) et surtout l'exponentielle (chapitre 9), la seule fonction qui soit, à un facteur près, sa propre dérivée.

## 🏰 L'équation y′ = ay : toute une famille de solutions

Un laboratoire suit une population de bactéries soumise à un antibiotique : N(t) = 9000e^(−0,4t), avec t en heures. Dérivons : N′(t) = 9000 × (−0,4)e^(−0,4t) = −0,4 N(t). La vitesse de disparition est proportionnelle à l'effectif. Avec 3000 bactéries au départ au lieu de 9000, la même relation tient.
Une relation entre une fonction et sa dérivée ne désigne donc pas une fonction, mais plusieurs. Peut-on retrouver toutes les fonctions N qui vérifient N′ = −0,4N ?

::: definition
**Vocabulaire** — « Une équation de la forme y′ = ay, où l'inconnue y est une fonction et a est un réel, est appelée équation différentielle linéaire du premier ordre à coefficient constant. Résoudre dans ℝ une équation de la forme y′ = ay, c'est trouver toutes les fonctions dérivables sur ℝ qui vérifient y′ = ay. Ces fonctions sont appelées solutions sur ℝ de l'équation y′ = ay. »
:::

::: exemple Vérifier qu'une fonction est solution

1. N(t) = 9000e^(−0,4t) : N′(t) = −3600e^(−0,4t) = −0,4 × 9000e^(−0,4t) = −0,4N(t) pour tout t. N est solution de y′ = −0,4y.
2. M(t) = 3000e^(−0,4t) : M′(t) = −1200e^(−0,4t) = −0,4M(t). Même équation, autre solution.
3. f : x ↦ e^(−x), g : x ↦ −2e^(−x) et h : x ↦ 0,5e^(−x) sont solutions de y′ = −y : f′(x) = −e^(−x) = −f(x), g′(x) = 2e^(−x) = −g(x), h′(x) = −0,5e^(−x) = −h(x).
4. Conclusion : une équation différentielle a toute une **famille** de solutions, ce qui la distingue d'une équation numérique. Pour tester une candidate, on la dérive, on remplace dans l'équation et on vérifie l'égalité **pour tout x**.

:::

::: propriete
**Théorème** — « Soit a un réel. L'ensemble des solutions de l'équation différentielle y′ = ay est l'ensemble des fonctions définies sur ℝ par f : x ↦ ke^(ax), où k est un réel quelconque. »
**Démonstration.** Pour tout réel k, f(x) = ke^(ax) est dérivable et f′(x) = kae^(ax) = af(x). Réciproquement, soit g une solution et h(x) = g(x)e^(−ax). Alors h′(x) = g′(x)e^(−ax) − ag(x)e^(−ax) = (g′(x) − ag(x))e^(−ax) = 0, donc h est constante, égale à un réel k, et g(x) = ke^(ax). ∎
:::

Toute la famille se déduit d'une seule courbe : le signe de a décide de la croissance ou de la décroissance de l'exponentielle, le signe de k décide du côté de l'axe.

::: figure Les solutions de y′ = −y forment une famille de courbes emboîtées, chacune repérée par son coefficient k ; deux courbes de la famille ne se coupent jamais.
<svg viewBox="0 0 320 210"><path d="M40 105 H305" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M70 190 V15" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M305 105 l-7 -3.5 l0 7 z" fill="#0f172a"/><path d="M70 15 l-3.5 7 l7 0 z" fill="#0f172a"/><polyline points="60,19.5 65,27.6 70,35 75,41.7 80,47.7 85,53.1 90,58.1 95,62.5 100,66.6 105,70.2 110,73.5 115,76.5 120,79.2 125,81.7 130,83.9 135,85.9 140,87.7 145,89.4 150,90.9 155,92.2 160,93.4 165,94.5 170,95.5 175,96.4 180,97.2 185,98 190,98.6 195,99.3 200,99.8 205,100.3 210,100.7 215,101.1 220,101.5 225,101.8 230,102.1 235,102.4 240,102.7 245,102.9 250,103.1 255,103.3 260,103.4 265,103.6 270,103.7 275,103.8 280,104 285,104.1 290,104.1 295,104.2 300,104.3" fill="none" stroke="#b45309" stroke-width="2.4" stroke-linecap="round"/><polyline points="40,41.2 45,47.3 50,52.8 55,57.8 60,62.3 65,66.3 70,70 75,73.3 80,76.3 85,79.1 90,81.5 95,83.8 100,85.8 105,87.6 110,89.3 115,90.8 120,92.1 125,93.3 130,94.5 135,95.5 140,96.4 145,97.2 150,97.9 155,98.6 160,99.2 165,99.8 170,100.3 175,100.7 180,101.1 185,101.5 190,101.8 195,102.1 200,102.4 205,102.6 210,102.9 215,103.1 220,103.3 225,103.4 230,103.6 235,103.7 240,103.8 245,103.9 250,104 255,104.1 260,104.2 265,104.3 270,104.4 275,104.4 280,104.5 285,104.5 290,104.6 295,104.6 300,104.6" fill="none" stroke="#0f6e56" stroke-width="2.4" stroke-linecap="round"/><polyline points="40,168.8 45,162.7 50,157.2 55,152.2 60,147.7 65,143.7 70,140 75,136.7 80,133.7 85,130.9 90,128.5 95,126.2 100,124.2 105,122.4 110,120.7 115,119.2 120,117.9 125,116.7 130,115.5 135,114.5 140,113.6 145,112.8 150,112.1 155,111.4 160,110.8 165,110.2 170,109.7 175,109.3 180,108.9 185,108.5 190,108.2 195,107.9 200,107.6 205,107.4 210,107.1 215,106.9 220,106.7 225,106.6 230,106.4 235,106.3 240,106.2 245,106.1 250,106 255,105.9 260,105.8 265,105.7 270,105.6 275,105.6 280,105.5 285,105.5 290,105.4 295,105.4 300,105.4" fill="none" stroke="#7c3aed" stroke-width="2.4" stroke-linecap="round"/><text x="105" y="45" font-size="12" font-weight="700" fill="#b45309">k = 2</text><text x="130" y="72" font-size="12" font-weight="700" fill="#0f6e56">k = 1</text><text x="130" y="134" font-size="12" font-weight="700" fill="#7c3aed">k = −1</text><text x="62" y="118" font-size="12" font-weight="700" fill="#0f172a">O</text><text x="285" y="98" font-size="11" fill="#0f172a">x</text></svg>
:::

::: exemple Lire le coefficient a, puis résoudre

1. Résoudre 2y′ + 3y = 0. **Premier geste** : isoler y′ en divisant par le coefficient de y′. On obtient y′ = −(3/2)y, donc a = −3/2 et f(x) = ke^(−3x/2). Contrôle : 2f′(x) + 3f(x) = −3ke^(−3x/2) + 3ke^(−3x/2) = 0 ✓.
2. x ↦ 2e^(2x) a pour dérivée 4e^(2x) = 2 × (2e^(2x)) : c'est une solution de **y′ = 2y**, et non de y′ = 4y.
3. Une autre base : x ↦ 2^x = e^(x ln 2) a pour dérivée (ln 2)e^(x ln 2). C'est une solution de y′ = (ln 2)y, soit y′ − y ln 2 = 0.
4. Pour a = 0, l'équation devient y′ = 0 : ses solutions sont les fonctions constantes ke^0 = k.

:::

::: piege
**Erreur : lire a devant l'exponentielle.** Pour f(x) = −5e^(3x), on est tenté de répondre « y′ = −5y ». Or f′(x) = −15e^(3x) = 3 × (−5e^(3x)) = 3f(x) : le coefficient a est celui qui apparaît **dans l'exposant**, ici 3, tandis que −5 joue le rôle de k. Autre piège voisin : si f(x) = ke^(−2x), alors f′(x) = −2ke^(−2x) est du signe de −k ; avec k < 0, la fonction est **croissante** malgré a < 0.
:::

::: verifie À toi : lire a, puis vérifier
Donner les solutions de 5y′ − 2y = 0, puis dire de quelle équation y′ = ay la fonction x ↦ −3e^(4x) est solution.

---

On isole y′ : 5y′ = 2y donc y′ = (2/5)y, avec a = 2/5 : les solutions sont les x ↦ ke^(2x/5), k ∈ ℝ. Pour x ↦ −3e^(4x), la dérivée est −12e^(4x) = 4 × (−3e^(4x)) : le coefficient dans l'exposant est 4, donc la fonction est solution de y′ = 4y.
:::

::: retenir
Résoudre y′ = ay, c'est écrire la famille x ↦ ke^(ax), k ∈ ℝ, après avoir isolé y′ pour lire a dans l'exposant.
:::

## 🎯 Une condition initiale, une seule solution

Le laboratoire connaît l'effectif de départ : 9000 bactéries. Parmi toutes les courbes de la famille ke^(−0,4t), une seule passe par le point (0 ; 9000).
Et si l'effectif était connu non pas à l'instant 0, mais à un instant x₀ quelconque ? Une seule donnée suffit-elle encore à isoler une solution ?

::: propriete
**Théorème** — « Soit a un réel non nul. Pour tous réels x₀ et y₀, l'équation y′ = ay admet une unique solution qui prend la valeur y₀ en x₀. C'est la fonction définie sur ℝ par f : x ↦ y₀e^(a(x−x₀)). »
**Démonstration.** Toute solution s'écrit f(x) = ke^(ax) et la condition f(x₀) = y₀ s'écrit ke^(ax₀) = y₀, donc k = y₀e^(−ax₀) : le réel k est imposé, et f(x) = y₀e^(−ax₀)e^(ax) = y₀e^(a(x−x₀)). ∎
:::

::: exemple Quatre conditions, quatre solutions

1. Les bactéries : N′ = −0,4N et N(0) = 9000. Ici x₀ = 0 et y₀ = 9000, donc N(t) = 9000e^(−0,4t). Au bout de 10 heures, N(10) = 9000e^(−4) ≈ 165 bactéries.
2. y′ − y/2 = 0 avec y(−1) = e. On écrit y′ = (1/2)y, donc a = 1/2, x₀ = −1, y₀ = e : f(x) = e × e^((x+1)/2) = e^((x+3)/2). Contrôle : f(−1) = e^1 = e ✓ et f′(x) = (1/2)f(x) ✓.
3. −3y′ − y = 0 avec y(ln 8) = 1. On isole : y′ = −(1/3)y, donc f(x) = e^(−(x − ln 8)/3) = e^(−x/3) × e^((ln 8)/3). Comme e^((ln 8)/3) = 8^(1/3) = 2, on obtient f(x) = 2e^(−x/3). Contrôle : f(ln 8) = 2 × 8^(−1/3) = 1 ✓.
4. f est la solution de y′ = 3y telle que f′(1) = 3. L'équation transforme la donnée sur f′ en donnée sur f : f′(1) = 3f(1), donc f(1) = 1 et f(x) = e^(3(x−1)).

:::

::: piege
**Erreur : prendre k = y₀ quand x₀ ≠ 0.** Pour la solution de y′ = 3y telle que f(1) = 2, on écrit « f(x) = 2e^(3x) ». Mais ce f vérifie f(1) = 2e^3 ≠ 2. La valeur donnée est f(x₀) = ke^(ax₀), pas k : on trouve k = 2e^(−3) et f(x) = 2e^(3(x−1)). Le réflexe qui sauve : calculer f(x₀) pour contrôler.
:::

::: verifie À toi : une condition en un point x₀ ≠ 0
Déterminer la solution f de y′ = −2y telle que f(3) = 5.

---

Ici a = −2, x₀ = 3 et y₀ = 5, donc f(x) = 5e^(−2(x−3)). Contrôle : f(3) = 5e^0 = 5 ✓ et f′(x) = −2f(x) ✓.
:::

::: retenir
Pour y′ = ay, une seule condition f(x₀) = y₀ fixe la solution : f(x) = y₀e^(a(x−x₀)), et l'équation relie f′(x₀) à f(x₀).
:::

## 🔮 Le second membre constant : y′ = ay + b

La fonction f : x ↦ e^(−2x) + 3 a pour dérivée −2e^(−2x). Calculons −2f(x) + 6 = −2e^(−2x) − 6 + 6 = −2e^(−2x) : elle est solution de y′ = −2y + 6. La fonction constante 3 l'est aussi, car 0 = −2 × 3 + 6.
Une constante au second membre déplace donc la solution d'équilibre. Où se trouve-t-elle en général, et que devient la famille de solutions ?

Si y est constante égale à c, alors y′ = 0 et l'équation devient 0 = ac + b, soit c = −b/a (possible car a ≠ 0). La fonction constante **−b/a** est toujours solution.

::: propriete
**Théorème** — « Soit a et b deux réels tels que a ≠ 0. L'ensemble des solutions de l'équation différentielle y′ = ay + b est l'ensemble des fonctions f : x ↦ ke^(ax) − b/a, où k est un réel quelconque. De plus pour tous réels x₀, y₀, la fonction f : x ↦ (y₀ + b/a)e^(a(x−x₀)) − b/a est l'unique solution de y′ = ay + b, telle que f(x₀) = y₀. »
**Démonstration.** Posons h = f + b/a. Alors h′ = f′ et : f est solution de y′ = ay + b ⟺ h′ = a(h − b/a) + b = ah. Donc h est solution de y′ = ay, c'est-à-dire h(x) = ke^(ax), et f(x) = ke^(ax) − b/a. Si f(x₀) = y₀, alors ke^(ax₀) = y₀ + b/a, d'où la seconde formule. ∎
:::

::: exemple Du second membre aux solutions

1. y′ = −2y + 6. Ici a = −2 et b = 6, donc −b/a = 3 et les solutions sont x ↦ ke^(−2x) + 3. La fonction e^(−2x) + 3 correspond à k = 1.
2. y′ + 3y + 3/4 = 0 avec y(−1) = 0. On isole : y′ = −3y − 3/4, donc a = −3, b = −3/4 et −b/a = −(−3/4)/(−3) = −1/4. Les solutions sont x ↦ ke^(−3x) − 1/4 ; la condition donne ke^3 − 1/4 = 0, soit k = (1/4)e^(−3), et f(x) = (1/4)e^(−3(x+1)) − 1/4. Contrôle : f′(x) = −(3/4)e^(−3(x+1)) et −3f(x) − 3/4 = −(3/4)e^(−3(x+1)) + 3/4 − 3/4 ✓.
3. √2 y′ − 2y = 1 avec f(0) = −1. On divise par √2 : y′ = √2 y + √2/2, donc a = √2 et −b/a = −(√2/2)/√2 = −1/2. Les solutions sont ke^(√2 x) − 1/2 ; f(0) = k − 1/2 = −1 donne k = −1/2, et f(x) = −(1/2)e^(√2 x) − 1/2.
4. La même équation avec f(0) = −1/2 donne k = 0 : f est la **fonction constante −1/2**. C'est la solution d'équilibre, atteinte quand la condition initiale tombe pile dessus.

:::

::: piege
**Erreur : écrire +b/a au lieu de −b/a.** Pour y′ = 3y − 12 on lit b = −12 et l'on propose « ke^(3x) − 4 », avec b/a = −4. Le test qui ne trompe pas : la constante c doit annuler ay + b, et 3 × (−4) − 12 = −24 ≠ 0. La bonne constante est −b/a = 4 : 3 × 4 − 12 = 0 ✓, et les solutions sont ke^(3x) + 4.
:::

::: verifie À toi : le second membre et la condition
Résoudre y′ = −5y + 15 avec f(0) = 2.

---

Ici a = −5 et b = 15, donc −b/a = 3 et f(x) = ke^(−5x) + 3. La condition f(0) = k + 3 = 2 donne k = −1, donc f(x) = 3 − e^(−5x). Contrôle : f′(x) = 5e^(−5x) et −5f(x) + 15 = −15 + 5e^(−5x) + 15 ✓.
:::

::: retenir
Les solutions de y′ = ay + b (a ≠ 0) sont les x ↦ ke^(ax) − b/a : la constante −b/a annule ay + b, et k se fixe par la condition initiale.
:::

## 🧪 Modéliser : circuits électriques et refroidissement

Allume un circuit : le courant ne saute pas à sa valeur finale, il y monte en un court instant. Dans un circuit formé d'un générateur de force électromotrice E, d'une bobine d'inductance L et de résistance r, l'intensité i vérifie L i′ + r i = E. Les mêmes lois, avec d'autres lettres, décrivent un condensateur qui se charge ou un café qui refroidit.
Comment passer d'une loi physique à une fonction, et vers quelle valeur la grandeur se stabilise-t-elle ?

::: methode
**Modèle en trois temps** : (1) traduire l'énoncé en y′ = ay + b, (2) écrire la famille ke^(ax) − b/a, (3) fixer k avec la valeur à l'instant 0. Si a < 0, le terme ke^(ax) s'efface avec le temps et la grandeur tend vers **−b/a**.
:::

::: exemple Trois lois, une même méthode

1. **Bobine** : E = 10 V, r = 100 Ω, L = 0,2 H, intensité nulle à t = 0. L'équation 0,2 i′ + 100 i = 10 devient i′ = −500 i + 50, avec −b/a = 0,1. Donc i(t) = ke^(−500t) + 0,1 et i(0) = 0 donne k = −0,1 : i(t) = 0,1(1 − e^(−500t)). Contrôle : i′(t) = 50e^(−500t) et −500 i(t) + 50 = 50e^(−500t) ✓. Quand t → +∞, i(t) → 0,1 A = E/r.
2. **Condensateur** : R q′ + q/C = U avec q(0) = 0, R = 1000 Ω, C = 2 × 10⁻⁴ F, U = 10 V. On isole q′ = −5q + 0,01, avec −b/a = 0,002. Donc q(t) = 0,002(1 − e^(−5t)) coulomb. L'intensité i = q′ vaut i(t) = 0,01e^(−5t) : i(0) = 10 mA, puis i décroît vers 0 pendant que q tend vers CU = 0,002 C.
3. **Refroidissement de Newton** : un corps à 100 °C dans un air à 25 °C passe à 75 °C en 15 min, avec f′(t) = a(f(t) − 25). Posons g = f − 25 : g′ = ag, donc f(t) = 25 + 75e^(at). La donnée f(15) = 75 impose e^(15a) = 2/3, donc a = (ln(2/3))/15 ≈ −0,0270. Contrôle : f(0) = 100 ✓ et f(15) = 25 + 75 × 2/3 = 75 ✓.
4. Seuil : f(t) < 26 équivaut à 75e^(at) < 1, soit t > (ln 75)/0,0270 ≈ 160 : au bout de 160 minutes environ, la température est à moins de 1 °C de l'air ambiant.

:::

::: figure Le courant part de zéro et monte vers sa valeur limite E/r : le terme en e^(−500t) est le régime transitoire, qui s'efface en quelques millisecondes.
<svg viewBox="0 0 320 200"><path d="M45 160 H305" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M60 175 V25" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M305 160 l-7 -3.5 l0 7 z" fill="#0f172a"/><path d="M60 25 l-3.5 7 l7 0 z" fill="#0f172a"/><line x1="55" y1="60" x2="300" y2="60" stroke="#b45309" stroke-width="1.4" stroke-dasharray="5 3"/><polyline points="60,160 65,149.7 70,140.5 75,132.2 80,124.7 85,118.1 90,112.1 95,106.7 100,101.9 105,97.6 110,93.7 115,90.3 120,87.1 125,84.3 130,81.8 135,79.6 140,77.6 145,75.8 150,74.1 155,72.7 160,71.4 165,70.2 170,69.2 175,68.2 180,67.4 185,66.6 190,65.9 195,65.3 200,64.8 205,64.3 210,63.8 215,63.4 220,63.1 225,62.8 230,62.5 235,62.2 240,62 245,61.8 250,61.6 255,61.4 260,61.3 265,61.2 270,61 275,60.9 280,60.8 285,60.8 290,60.7 295,60.6 300,60.5" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/><text x="230" y="54" font-size="12" font-weight="700" fill="#b45309">E/r = 0,1 A</text><text x="288" y="176" font-size="11" fill="#0f172a">t (s)</text><text x="34" y="36" font-size="11" fill="#0f172a">i (A)</text><text x="52" y="174" font-size="11" fill="#0f172a">0</text></svg>
:::

::: piege
**Erreur : demander quand le corps « atteint » 25 °C.** Comme 75e^(at) ne s'annule jamais, f(t) reste strictement supérieure à 25 : la température **tend** vers 25 sans l'atteindre. Seule une question de seuil (moins de 1 °C d'écart) a une réponse. De même pour le condensateur : q tend vers CU, mais l'intensité i = q′ tend vers **0**, pas vers CU/R.
:::

::: verifie À toi : un régime transitoire
Dans un circuit où L i′ + r i = E, on donne E = 6 V, r = 30 Ω, L = 0,3 H et i(0) = 0. Déterminer i(t) et sa limite en +∞.

---

On divise par L : i′ = −100 i + 20, avec −b/a = 0,2. Donc i(t) = ke^(−100t) + 0,2 et i(0) = 0 donne k = −0,2 : i(t) = 0,2(1 − e^(−100t)). Quand t → +∞, e^(−100t) → 0 et i(t) → 0,2 A = E/r = 6/30 ✓.
:::

::: retenir
Traduire en y′ = ay + b, écrire ke^(ax) − b/a, fixer k à l'instant 0 : pour a < 0, la grandeur tend vers −b/a sans jamais l'atteindre.
:::

## ☢️ Décroissance radioactive et demi-vie

Pour dater un os, les archéologues mesurent la part de carbone 14 qui reste. Une substance radioactive perd ses noyaux à une vitesse proportionnelle au nombre de noyaux présents : si N(t) est ce nombre à l'instant t et λ > 0 la constante radioactive, alors N′(t) = −λN(t).
Au bout de quelle durée la substance a-t-elle perdu la moitié de ses noyaux, et cette durée dépend-elle de la quantité de départ ?

::: propriete
**Désintégration** — La solution de N′ = −λN telle que N(0) = N₀ est N(t) = N₀e^(−λt). La **demi-vie** T₀.₅ est la durée qui vérifie N(T₀.₅) = N₀/2, soit e^(−λT₀.₅) = 1/2, donc −λT₀.₅ = −ln 2 :
$$ T₀.₅ = (ln 2)/λ $$
Elle ne dépend **pas** de N₀ : après chaque durée T₀.₅, il reste la moitié de ce qu'il y avait au début de l'intervalle.
:::

::: figure Sur chaque intervalle de durée T, la proportion restante est divisée par 2, quel que soit le point de départ choisi sur la courbe.
<svg viewBox="0 0 320 200"><path d="M45 165 H305" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M60 180 V25" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M305 165 l-7 -3.5 l0 7 z" fill="#0f172a"/><path d="M60 25 l-3.5 7 l7 0 z" fill="#0f172a"/><polyline points="60,55 95,87.2 130,110 165,126.1 200,137.5 235,145.6 270,151.3" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/><line x1="60" y1="110" x2="130" y2="110" stroke="#b45309" stroke-width="1.3" stroke-dasharray="4 3"/><line x1="130" y1="110" x2="130" y2="165" stroke="#b45309" stroke-width="1.3" stroke-dasharray="4 3"/><line x1="60" y1="137.5" x2="200" y2="137.5" stroke="#7c3aed" stroke-width="1.3" stroke-dasharray="4 3"/><line x1="200" y1="137.5" x2="200" y2="165" stroke="#7c3aed" stroke-width="1.3" stroke-dasharray="4 3"/><circle cx="60" cy="55" r="3" fill="#0f172a"/><text x="30" y="59" font-size="11" font-weight="700" fill="#0f172a">N₀</text><text x="24" y="114" font-size="11" font-weight="700" fill="#b45309">N₀/2</text><text x="24" y="141" font-size="11" font-weight="700" fill="#7c3aed">N₀/4</text><text x="130" y="179" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a">T</text><text x="200" y="179" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a">2T</text><text x="286" y="181" font-size="11" fill="#0f172a">t</text></svg>
:::

::: exemple Le carbone 14

1. La demi-vie vaut T₀.₅ = 5730 ans, donc λ = (ln 2)/5730 ≈ 0,6931/5730 ≈ 1,21 × 10⁻⁴ par an.
2. Un fragment d'os contient 60 % de la quantité initiale : on résout e^(−λt) = 0,6, soit −λt = ln 0,6, donc t = −(ln 0,6)/λ = 5730 × (−ln 0,6)/(ln 2) ≈ 5730 × 0,5108/0,6931 ≈ 4223 ans.
3. Contrôle : 60 % est un peu plus que la moitié, donc l'âge doit être un peu **inférieur** à une demi-vie (5730 ans) ✓.

:::

::: piege
**Erreur : croire qu'après deux demi-vies tout a disparu.** Après T₀.₅ il reste la moitié, après 2T₀.₅ il reste la moitié de la moitié, soit **le quart** : N(2T₀.₅) = N₀e^(−2 ln 2) = N₀/4. La décroissance ne s'arrête jamais : N(t) > 0 pour tout t.
:::

::: verifie À toi : un quart de la quantité
Le radium 226 a une demi-vie de 1600 ans. Au bout de combien d'années ne reste-t-il que 25 % d'un échantillon ?

---

On résout e^(−λt) = 1/4 = (1/2)², soit −λt = −2 ln 2 et t = 2(ln 2)/λ = 2T₀.₅ = 3200 ans. Contrôle : deux demi-vies donnent bien (1/2)² = 1/4 ✓.
:::

::: retenir
Si N′ = −λN, alors N(t) = N₀e^(−λt) et la demi-vie vaut (ln 2)/λ, indépendante de N₀ : après n demi-vies, il reste N₀/2ⁿ.
:::

## 🌊 Les oscillations : y″ + ω²y = 0

Dérivons deux fois f(x) = sin x + cos x : f′(x) = cos x − sin x, puis f″(x) = −sin x − cos x = −f(x). Même chose pour g(x) = sin 3x : g′(x) = 3cos 3x, puis g″(x) = −9 sin 3x = −9g(x).
Ici la dérivée seconde est un multiple négatif de la fonction : au lieu de croître ou de décroître, la fonction **oscille**. Quelles sont toutes les fonctions qui vérifient f″ = −ω²f ?

::: definition
**Vocabulaire** — « Une équation de la forme y″ + ω²y = 0, où l'inconnue y est une fonction et ω est un réel, est appelée équation différentielle linéaire du second ordre à coefficients constants. Résoudre une équation de la forme y″ + ω²y = 0, c'est trouver toutes les fonctions deux fois dérivables sur ℝ qui la vérifient. »
:::

::: exemple Du problème de Cauchy aux formules

1. y″ + 9y = 0 avec f(0) = √3/2 et f′(0) = 3/2. Comme 9 = 3², ω = 3 et f(x) = A sin(3x) + B cos(3x). Alors f(0) = B = √3/2. Ensuite f′(x) = 3A cos(3x) − 3B sin(3x), donc f′(0) = 3A = 3/2 et A = 1/2 : f(x) = (1/2)sin(3x) + (√3/2)cos(3x). Contrôle : f″ = −9f ✓.
2. y″ + 2y = 0 avec y(0) = 1 et y′(0) = √2. Ici ω = √2 et f(x) = (√2/√2)sin(√2 x) + 1 × cos(√2 x) = sin(√2 x) + cos(√2 x). Contrôle : f′(0) = √2 cos 0 − √2 sin 0 = √2 ✓.
3. Conditions en un autre point : y″ + 4y = 0 avec f(π/2) = −1 et f′(π/2) = 2. Alors f(x) = A sin(2x) + B cos(2x) ; f(π/2) = A sin π + B cos π = −B = −1, donc B = 1. Puis f′(x) = 2A cos(2x) − 2B sin(2x) donne f′(π/2) = −2A = 2, donc A = −1 : f(x) = −sin(2x) + cos(2x). Contrôle : f′(x) = −2cos(2x) − 2 sin(2x) et f′(π/2) = 2 ✓.

:::

::: propriete
**Théorème** — « Soit ω un réel non nul. L'ensemble des solutions de l'équation différentielle y″ + ω²y = 0 est l'ensemble des fonctions définies sur ℝ par f(x) = A sin(ωx) + B cos(ωx), (A, B) ∈ ℝ². »
**Théorème** (conditions en 0) — « Soit ω un réel non nul et x₀, y₀ deux réels. L'équation y″ + ω²y = 0 admet une unique solution dans ℝ vérifiant f(0) = x₀ et f′(0) = y₀. C'est la fonction définie sur ℝ par f(x) = (y₀/ω) sin(ωx) + x₀ cos(ωx). » **Conséquence** : la fonction nulle est l'unique solution qui vérifie y(0) = y′(0) = 0.
**Idée de la preuve.** Si f est solution, posons g(x) = f(x) − (f′(0)/ω) sin(ωx) − f(0) cos(ωx) : g est solution avec g(0) = g′(0) = 0. La fonction h = ω²g² + g′² a pour dérivée h′ = 2g′(ω²g + g″) = 0, donc h est constante égale à h(0) = 0, ce qui impose g = 0 et donne la forme annoncée.
:::

::: piege
**Erreur : prendre ω égal au coefficient de y.** Pour y″ + 9y = 0, on écrit « A sin(9x) + B cos(9x) ». Or ω² = 9 donc ω = 3, et A sin(9x) + B cos(9x) vérifie y″ + 81y = 0. De plus, **deux** conditions sont nécessaires à l'ordre deux (la valeur et la pente), là où l'ordre un n'en demandait qu'une. Deux valeurs de f en deux points (sans f′) peuvent donner une, aucune ou une infinité de solutions : on écrit le système en A et B et on le discute.
:::

::: verifie À toi : l'ordre deux
Déterminer la solution de y″ + 16y = 0 telle que f(0) = 2 et f′(0) = −8.

---

Ici ω = 4 (car 16 = 4²), donc f(x) = A sin(4x) + B cos(4x). f(0) = B = 2 ; f′(0) = 4A = −8 donne A = −2. Ainsi f(x) = −2 sin(4x) + 2cos(4x). Contrôle : f″ = −16f ✓.
:::

::: retenir
Les solutions de y″ + ω²y = 0 sont les x ↦ A sin(ωx) + B cos(ωx), avec ω = √(coefficient de y) ; deux conditions (f(0), f′(0)) fixent A et B.
:::

## 🎼 Amplitude et phase : la forme r cos(ωx − φ)

La fonction f(x) = sin x + cos x ressemble à une cosinusoïde décalée. Peut-on l'écrire avec un seul cosinus, pour lire directement son amplitude et résoudre f(x) = m ?

En développant r cos(ωx − φ) = r cos φ cos(ωx) + r sin φ sin(ωx), on identifie **B = r cos φ** et **A = r sin φ**.

::: propriete
**Forme amplitude-phase** — Pour A sin(ωx) + B cos(ωx) non nul, on a A sin(ωx) + B cos(ωx) = r cos(ωx − φ), avec
$$ r = √(A² + B²), cos φ = B/r, sin φ = A/r, φ ∈ ]−π, π] $$
La période vaut 2π/ω ; l'amplitude r dépend des conditions initiales.
:::

::: exemple Trois mises sous forme r cos(ωx − φ)

1. f(x) = sin x + cos x : A = B = 1, r = √2, cos φ = sin φ = √2/2, donc φ = π/4 et f(x) = √2 cos(x − π/4). Contrôle : √2 × [cos x × √2/2 + sin x × √2/2] = cos x + sin x ✓.
2. f(x) = (1/2)sin(3x) + (√3/2)cos(3x) : r = √(1/4 + 3/4) = 1, cos φ = √3/2, sin φ = 1/2, donc φ = π/6 et f(x) = cos(3x − π/6). On lit amplitude 1, période 2π/3, et f(x) = 1 exactement quand 3x − π/6 = 2kπ, soit x = π/18 + 2kπ/3.
3. g(x) = √3 sin(2x) − cos(2x) : A = √3 et B = −1, donc r = 2, cos φ = −1/2 et sin φ = √3/2. Le cosinus seul donnerait ±2π/3 ; le sinus positif tranche : φ = 2π/3, et g(x) = 2cos(2x − 2π/3). Contrôle : 2[cos 2x × (−1/2) + sin 2x × (√3/2)] = −cos 2x + √3 sin 2x ✓.

:::

::: exemple Deux mouvements oscillants

1. **Mobile** : l'accélération est proportionnelle à la position, de coefficient −π²/4. Donc x″(t) + (π²/4)x(t) = 0, ω = π/2 et x(t) = A sin(πt/2) + B cos(πt/2). Les données x(1) = 2 et x(2) = 0 donnent x(1) = A = 2, puis x(2) = −B = 0 : x(t) = 2 sin(πt/2). La période est 2π/(π/2) = 4 s ; à l'instant 0, x(0) = 0 et x′(0) = 2 × (π/2)cos 0 = π m/s.
2. **Circuit L-C** : la charge vérifie q″ + q/(LC) = 0. Avec L = 0,5 × 10⁻² H et C = 1,25 × 10⁻³ F, on a LC = 6,25 × 10⁻⁶ et 1/(LC) = 160 000 = 400², donc ω = 400. Avec q(0) = 6 × 10⁻³ C et q′(0) = 0 : q(t) = 6 × 10⁻³ cos(400t). L'intensité i = −q′ vaut i(t) = 2,4 sin(400t) : elle oscille entre −2,4 A et 2,4 A.

:::

::: figure L'élongation oscille entre −2 et 2 et se répète toutes les 4 secondes : l'amplitude dépend des conditions initiales, la période seulement de ω.
<svg viewBox="0 0 340 190"><path d="M40 95 H325" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M55 175 V20" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M325 95 l-7 -3.5 l0 7 z" fill="#0f172a"/><path d="M55 20 l-3.5 7 l7 0 z" fill="#0f172a"/><line x1="50" y1="40" x2="315" y2="40" stroke="#b45309" stroke-width="1.2" stroke-dasharray="5 3"/><line x1="50" y1="150" x2="315" y2="150" stroke="#b45309" stroke-width="1.2" stroke-dasharray="5 3"/><polyline points="55,95 62.8,74 70.6,56.1 78.4,44.2 86.3,40 94.1,44.2 101.9,56.1 109.7,74 117.5,95 125.3,116 133.1,133.9 140.9,145.8 148.8,150 156.6,145.8 164.4,133.9 172.2,116 180,95 187.8,74 195.6,56.1 203.4,44.2 211.3,40 219.1,44.2 226.9,56.1 234.7,74 242.5,95 250.3,116 258.1,133.9 265.9,145.8 273.8,150 281.6,145.8 289.4,133.9 297.2,116 305,95" fill="none" stroke="#0f6e56" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/><line x1="55" y1="170" x2="180" y2="170" stroke="#7c3aed" stroke-width="1.4"/><line x1="55" y1="166" x2="55" y2="174" stroke="#7c3aed" stroke-width="1.4"/><line x1="180" y1="166" x2="180" y2="174" stroke="#7c3aed" stroke-width="1.4"/><text x="117" y="166" text-anchor="middle" font-size="11" font-weight="700" fill="#7c3aed">T = 4 s</text><text x="40" y="44" font-size="11" font-weight="700" fill="#b45309">2</text><text x="36" y="154" font-size="11" font-weight="700" fill="#b45309">−2</text><text x="306" y="112" font-size="11" fill="#0f172a">t (s)</text><text x="26" y="30" font-size="11" fill="#0f172a">x (m)</text></svg>
:::

::: piege
**Erreur : décider φ par le seul cosinus.** Dans l'exemple 3, cos φ = −1/2 est vrai pour φ = 2π/3 **et** pour φ = −2π/3, deux angles de ]−π, π]. Un seul des deux a un sinus positif. On vérifie toujours le couple (cos φ, sin φ), jamais l'un des deux seuls. Et la période 2π/ω vient de l'**équation**, l'amplitude r des **conditions initiales**.
:::

::: verifie À toi : amplitude et phase
Écrire f(x) = sin x − cos x sous la forme r cos(x − φ), avec r > 0 et φ ∈ ]−π, π].

---

A = 1 et B = −1, donc r = √2, cos φ = −√2/2 et sin φ = √2/2 : c'est φ = 3π/4. Ainsi f(x) = √2 cos(x − 3π/4). Contrôle : √2 × [cos x × (−√2/2) + sin x × (√2/2)] = −cos x + sin x ✓.
:::

::: retenir
A sin(ωx) + B cos(ωx) = r cos(ωx − φ) avec r = √(A² + B²), cos φ = B/r, sin φ = A/r : la période 2π/ω vient de l'équation, l'amplitude r des conditions.
:::

## 🗝️ Se ramener à un cas connu : solution particulière et z = y′

Certains énoncés de bac posent une équation qui ne ressemble à aucune des précédentes : un second membre en x² ou en cos x, ou une dérivée seconde sans y.
Le réflexe est de se ramener à un cas déjà résolu. Comment ramener chacune à y′ = ay + b ou y′ = ay ?

::: methode
**Deux gestes.** (a) Second membre non nul : l'énoncé fournit la forme d'une solution particulière g ; on la détermine par identification, et f est solution de (E) ⟺ f − g est solution de l'équation sans second membre (E₀). (b) Dérivée seconde sans y : on pose z = y′, on résout l'équation d'ordre un en z, puis on **primitive** pour revenir à y. Même geste à l'ordre trois : pour y‴ + y″ = 0, z = y″ vérifie z′ = −z, puis on primitive deux fois. (c) Changement de fonction imposé par l'énoncé (g = 1/f, f = e^(ax)g, …) : on calcule g′, on reconnaît y′ = ay + b, puis on revient à f.
:::

::: exemple Cinq équations ramenées à un cas connu

1. (E) : y′ + 2y = x². Les solutions de (E₀) : y′ + 2y = 0 sont les ke^(−2x). Cherchons g(x) = αx² + βx + γ : g′ + 2g = 2αx² + (2α + 2β)x + (β + 2γ). On identifie avec x² : 2α = 1, 2α + 2β = 0 et β + 2γ = 0, soit α = 1/2, β = −1/2, γ = 1/4. Comme (f − g)′ + 2(f − g) = x² − x² = 0, les solutions de (E) sont f(x) = ke^(−2x) + x²/2 − x/2 + 1/4.
2. (E) : y′ − y = 4cos x avec g(x) = a cos x + b sin x. On a g′ − g = (b − a)cos x − (a + b)sin x. L'identification avec 4cos x donne b − a = 4 et a + b = 0, soit a = −2 et b = 2. Les solutions de (E) sont f(x) = ke^x − 2cos x + 2 sin x.
3. (E) : y″ = −3y′ + 1, avec f(0) = 0 et f′(0) = 0. Posons z = y′ : z′ = −3z + 1, donc z(x) = ke^(−3x) + 1/3. La condition z(0) = f′(0) = 0 donne k = −1/3, donc f′(x) = (1 − e^(−3x))/3. On primitive : f(x) = x/3 + e^(−3x)/9 + c et f(0) = 1/9 + c = 0 donne c = −1/9. Ainsi f(x) = x/3 + e^(−3x)/9 − 1/9. Contrôle : f″(x) = e^(−3x) et −3f′(x) + 1 = −(1 − e^(−3x)) + 1 = e^(−3x) ✓.
4. y′ + 2y = y², f ne s'annulant pas : g = 1/f donne g′ = −f′/f² = 2g − 1, donc g = ke^(2x) + 1/2. g ne s'annule pas sur ℝ ⟺ k ≥ 0, d'où f(x) = 2/(1 + 2ke^(2x)), k ≥ 0 (k = 0 redonne u = 2).
5. f(x) = ∫₀ˣ f(t)dt + x ⟹ f′ = f + 1 et f(0) = 0, donc f(x) = e^x − 1 (contrôle : ∫₀ˣ(e^t − 1)dt + x = e^x − 1 ✓).

:::

::: piege
**Erreur : appliquer la condition initiale à ke^(ax) seul.** Pour (E) : y′ + 2y = x² avec f(0) = 1, on écrit « k = f(0) = 1 ». Or f(0) = k + g(0) = k + 1/4, donc k = 3/4. La condition porte sur la fonction **entière** f = ke^(−2x) + g, pas sur sa partie homogène.
:::

::: verifie À toi : une solution particulière affine
Résoudre y′ + y = 2x, en cherchant une solution particulière g(x) = ax + b.

---

g′ + g = a + ax + b = 2x donne a = 2 et a + b = 0, soit b = −2 : g(x) = 2x − 2. Les solutions de y′ + y = 0 sont ke^(−x), donc les solutions de (E) sont f(x) = ke^(−x) + 2x − 2. Contrôle : f′ + f = −ke^(−x) + 2 + ke^(−x) + 2x − 2 = 2x ✓.
:::

::: retenir
Pour un second membre non nul : f solution ⟺ f − g solution de l'équation sans second membre ; pour une équation d'ordre deux sans y : poser z = y′, résoudre, puis primitiver.
:::

> 🏆 Dixième porte franchie, héros : tu clos le tome d'analyse. Tu sais lire une loi physique comme une équation, en sortir une famille de fonctions, la resserrer par une condition initiale, et vérifier ton résultat en le réinjectant, le seul contrôle qui ne ment jamais. Le tome 2 t'attend, et il commence par un nombre dont le carré vaut −1.
