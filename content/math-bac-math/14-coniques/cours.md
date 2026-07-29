# ⚔️ Coniques — trois courbes, une seule loi

> 💡 «Une planète autour du Soleil, un obus qui retombe, le faisceau d'un phare : trois trajectoires qui n'ont l'air de rien avoir en commun. Elles obéissent toutes les trois à la même phrase — un point, une droite, un rapport.»

Tu connais déjà deux de ces courbes sans le savoir : la parabole, c'est la courbe de x ↦ x² ; l'hyperbole, c'est celle de x ↦ 1/x. Ce chapitre révèle **pourquoi** ces deux dessins si différents portent des noms de la même famille, et il en ajoute une troisième, l'ellipse. Al-Tusi écrivait déjà, au XIIIᵉ siècle, l'équation de la parabole et celle de l'hyperbole rapportée à ses asymptotes — les mêmes que tu vas manipuler. Il te faudra le barycentre, les homothéties et les similitudes du chapitre 13 : ils servent à construire les points et à redresser les équations tordues.

## 🏰 Un point, une droite, un rapport

Commence par un cas que tu sais tracer les yeux fermés : la parabole 𝒫 d'équation y = x². Prends le point F(0, 1/4) et la droite D d'équation y = −1/4. Soit M(x, x²) un point de 𝒫 et H son projeté orthogonal sur D.

$$ MF² = x² + (x² − 1/4)² = x² + x⁴ − x²/2 + 1/16 = x⁴ + x²/2 + 1/16 = (x² + 1/4)² $$

Comme x² + 1/4 > 0, on obtient MF = x² + 1/4. Et MH = |x² − (−1/4)| = x² + 1/4. Donc **MF = MH** : tout point de cette parabole est à égale distance de F et de D. Ce n'est pas un hasard de calcul, c'est la définition de la courbe.

> **Définition générale** — « Soit D une droite, F un point n'appartenant pas à D et un réel e > 0. Pour tout point M du plan, on note H son projeté orthogonal sur D. On appelle **conique** 𝒞 d'excentricité e, de foyer F et de directrice D l'ensemble des points M tels que MF = eMH. Si e = 1, 𝒞 est une **parabole** de foyer F et de directrice D. Si e > 1, 𝒞 est une **hyperbole** de foyer F, de directrice D et d'excentricité e. Si e < 1, 𝒞 est une **ellipse** de foyer F, de directrice D et d'excentricité e. »

Un seul nombre, l'**excentricité** e, décide de tout :

| Excentricité  | Genre de la conique | Ce que ça donne                                        |
| ------------- | ------------------- | ------------------------------------------------------ |
| **e = 1**     | **Parabole**        | une seule branche ouverte, pas de centre               |
| **e > 1**     | **Hyperbole**       | deux branches, un centre, deux asymptotes              |
| **0 < e < 1** | **Ellipse**         | une courbe fermée, un centre, bornée                   |

La perpendiculaire à D passant par F s'appelle l'**axe focal** de la conique, dans les trois cas.

::: figure MH se mesure horizontalement jusqu'à la directrice, MF en diagonale jusqu'au foyer : c'est le rapport de ces deux longueurs, et lui seul, qui décide du genre de la courbe.
<svg viewBox="0 0 300 220"><path d="M70 20 V200" fill="none" stroke="#0f172a" stroke-width="2"/><path d="M240 60 H70" fill="none" stroke="#0f6e56" stroke-width="2.6"/><path d="M240 60 L190 140" fill="none" stroke="#b45309" stroke-width="2.6"/><path d="M82 60 L82 72 L70 72" fill="none" stroke="#0f172a" stroke-width="1.6"/><g fill="#0f172a"><circle cx="190" cy="140" r="4.5"/><circle cx="240" cy="60" r="4.5"/><circle cx="70" cy="60" r="4.5"/></g><g font-size="15" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="200" y="158" text-anchor="middle" fill="#0f172a">F</text><text x="252" y="52" text-anchor="middle" fill="#0f172a">M</text><text x="58" y="52" text-anchor="middle" fill="#0f172a">H</text><text x="70" y="214" text-anchor="middle" fill="#0f172a">D</text><text x="152" y="52" text-anchor="middle" fill="#0f6e56">MH</text><text x="228" y="112" text-anchor="middle" fill="#b45309">MF</text></g></svg>
:::

> ⚠️ L'excentricité est un **rapport de deux longueurs** : un nombre strictement positif, sans unité. Et le foyer n'est **jamais** sur la directrice — sans cette hypothèse, l'ensemble MF = eMH dégénère en droites.

## ⚡ La parabole : le cas e = 1

> **Définition** — « Soit D une droite et F un point n'appartenant pas à D. Pour tout point M du plan, on note H son projeté orthogonal sur la droite D. On appelle **parabole** de foyer F et de directrice D, l'ensemble des points M tels que MF = MH »

> **Vocabulaire** — « La distance du foyer à la directrice est appelée **paramètre** de la parabole. »

Autrement dit, si K est le projeté orthogonal de F sur D, alors p = FK.

> **Théorème** — « Toute parabole admet comme axe de symétrie son axe focal. Toute parabole rencontre son axe focal en un unique point appelé **sommet** de la parabole. Le sommet d'une parabole de foyer F et de directrice D est le **milieu du segment [FK]** où K est le projeté orthogonal de F sur D. »

Place-toi alors dans le repère orthonormé (S, i⃗, j⃗) où S est le sommet et i⃗ pointe vers le foyer. Le calcul de la définition se simplifie en une seule ligne :

> **Théorème (équation réduite)** — « La parabole 𝒫 a pour équation **y² = 2px**, la directrice D a pour équation x = −p/2 et le foyer F a pour coordonnées (p/2, 0). Réciproquement, l'ensemble des points M(x, y) tels que y² = 2px (p > 0) est la parabole de foyer F(p/2, 0), de directrice la droite d'équation x = −p/2, de paramètre p et de sommet O. »

Les trois autres orientations s'obtiennent par symétrie — c'est le même dessin retourné :

| Équation      | Ouverture       | Foyer      | Directrice |
| ------------- | --------------- | ---------- | ---------- |
| y² = 2px      | vers les x > 0  | (p/2, 0)   | x = −p/2   |
| y² = −2px     | vers les x < 0  | (−p/2, 0)  | x = p/2    |
| x² = 2py      | vers les y > 0  | (0, p/2)   | y = −p/2   |
| x² = −2py     | vers les y < 0  | (0, −p/2)  | y = p/2    |

_Exemple détaillé_ — soit 𝒫 : y² = 8x. On identifie 2p = 8, donc **p = 4** : le sommet est O(0, 0), le foyer F(2, 0) et la directrice a pour équation x = −2.

_Contrôle par la définition_ — pour x = 2, y² = 16 donne le point M(2, 4). Alors MF = √((2 − 2)² + 4²) = 4, et MH = |2 − (−2)| = 4 : MF = MH ✓. Recommence avec x = 1/2 : y² = 4 donne M′(1/2, 2), MF = √((1/2 − 2)² + 2²) = √(2,25 + 4) = √6,25 = 2,5 et MH = 1/2 + 2 = 2,5 ✓. Deux points concordants, l'identification est sûre.

::: figure Sur la parabole y² = 8x, les deux segments issus de M ont exactement la même longueur — 4 unités chacun : MF = MH, la définition lue directement sur le dessin.
<svg viewBox="0 0 300 250"><path d="M55 125 H255" fill="none" stroke="#94a3b8" stroke-width="1.5"/><path d="M71 20 V230" fill="none" stroke="#0f172a" stroke-width="2" stroke-dasharray="7 5"/><path d="M191 29 Q95 77 95 125 Q95 173 191 221" fill="none" stroke="#0f172a" stroke-width="2.4"/><path d="M119 77 L119 125" fill="none" stroke="#0f6e56" stroke-width="3"/><path d="M119 77 L71 77" fill="none" stroke="#b45309" stroke-width="3"/><path d="M113 101 H125" fill="none" stroke="#0f6e56" stroke-width="2"/><path d="M95 71 V83" fill="none" stroke="#b45309" stroke-width="2"/><g fill="#0f172a"><circle cx="95" cy="125" r="4"/><circle cx="119" cy="125" r="4.5"/><circle cx="119" cy="77" r="4.5"/><circle cx="71" cy="77" r="4.5"/></g><g font-size="15" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="88" y="144" text-anchor="middle" fill="#0f172a">S</text><text x="126" y="144" text-anchor="middle" fill="#0f172a">F</text><text x="132" y="70" text-anchor="middle" fill="#0f172a">M</text><text x="60" y="70" text-anchor="middle" fill="#0f172a">H</text><text x="78" y="244" text-anchor="middle" fill="#0f172a">D</text></g></svg>
:::

> ⚠️ Le paramètre p est la distance **foyer–directrice**, pas la distance foyer–sommet (qui vaut p/2). Dans y² = 2px, c'est le coefficient **entier** de x qui vaut 2p : dans y² = 8x, p vaut 4 et non 8.

## 🔮 L'hyperbole : le cas e > 1

> **Définition** — « Soit D une droite, F un point n'appartenant pas à D et un réel **e > 1**. On appelle **hyperbole** de foyer F, de directrice D et d'excentricité e, l'ensemble des points M tels que MF/MH = e. »

> **Théorème (sommets)** — « • L'axe focal de ℋ est un axe de symétrie pour ℋ. • ℋ rencontre son axe focal en **deux points** appelés sommets de l'hyperbole et ils sont les barycentres respectifs des points (F, 1), (K, −e) et (F, 1), (K, e) où K est le projeté orthogonal de F sur D. »

Le milieu O des deux sommets est le **centre** de l'hyperbole : c'est un centre de symétrie, ce qui garantit l'existence d'un **second foyer** F′ et d'une **seconde directrice** D′, symétriques de F et D. Dans le repère (O, i⃗, j⃗) construit sur l'axe focal, avec S(a, 0) et F(c, 0) :

> **Théorème (équation réduite)** — « L'hyperbole ℋ a pour équation **x²/a² − y²/b² = 1**, avec b² = c² − a². Réciproquement, l'ensemble des points M(x, y) tels que x²/a² − y²/b² = 1 (a > 0, b > 0) est une hyperbole de centre O, de foyer **F(√(a²+b²), 0)**, de directrice d'équation **x = a²/c**, d'excentricité **e = c/a** avec c = √(a²+b²) et de sommets S(a, 0) et S′(−a, 0). […] la courbe ℋ d'équation −x²/a² + y²/b² = 1 est une hyperbole de centre O, de foyer F(0, √(a²+b²)), de directrice la droite d'équation y = b²/c, d'excentricité e = c/b avec c = √(a²+b²) et de sommets S(0, b) et S′(0, −b). »

Reste la signature de l'hyperbole, ses deux droites de fuite :

> **Théorème (asymptotes et tangente)** — « ℋ admet deux asymptotes d'équations **y = (b/a)x** et **y = −(b/a)x**. La tangente à ℋ en un point M₀(x₀, y₀) a pour équation x₀x/a² − y₀y/b² = 1. »

_Exemple détaillé_ — soit ℋ : x²/9 − y²/16 = 1. On lit a² = 9 et b² = 16, donc a = 3 et b = 4, puis **c = √(9 + 16) = 5**. D'où : sommets S(3, 0) et S′(−3, 0), foyers F(5, 0) et F′(−5, 0), directrices x = a²/c = **9/5** et x = −9/5, excentricité **e = c/a = 5/3**, asymptotes y = 4x/3 et y = −4x/3.

_Contrôle par la définition_ — pour x = 5, y² = 16(25/9 − 1) = 256/9 donne M(5, 16/3). Alors MF = 16/3 (les deux points ont la même abscisse) et MH = |5 − 9/5| = 16/5. Le rapport vaut (16/3) ÷ (16/5) = **5/3 = e** ✓. Sur le sommet S(3, 0) : SF = |3 − 5| = 2 et SH = |3 − 9/5| = 6/5, rapport 2 ÷ (6/5) = 10/6 = **5/3** ✓.

::: figure Les deux branches se collent aux droites y = ±4x/3 sans jamais les toucher : ce sont les asymptotes, et elles passent toutes deux par le centre O.
<svg viewBox="0 0 340 250"><path d="M60 125 H290" fill="none" stroke="#94a3b8" stroke-width="1.5"/><path d="M170 12 V240" fill="none" stroke="#94a3b8" stroke-width="1.5"/><path d="M83 9 L257 241" fill="none" stroke="#0f6e56" stroke-width="1.8" stroke-dasharray="7 5"/><path d="M83 241 L257 9" fill="none" stroke="#0f6e56" stroke-width="1.8" stroke-dasharray="7 5"/><path d="M254 28 C218.3 82.9 212 104.7 212 125 C212 145.3 218.3 167.1 254 222" fill="none" stroke="#0f172a" stroke-width="2.4"/><path d="M86 28 C121.7 82.9 128 104.7 128 125 C128 145.3 121.7 167.1 86 222" fill="none" stroke="#0f172a" stroke-width="2.4"/><g fill="#0f172a"><circle cx="170" cy="125" r="4"/><circle cx="212" cy="125" r="4.5"/><circle cx="128" cy="125" r="4.5"/></g><g fill="#b45309"><circle cx="240" cy="125" r="4.5"/><circle cx="100" cy="125" r="4.5"/></g><g font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="162" y="144" text-anchor="middle" fill="#0f172a">O</text><text x="214" y="146" text-anchor="middle" fill="#0f172a">S</text><text x="126" y="146" text-anchor="middle" fill="#0f172a">S′</text><text x="246" y="146" text-anchor="middle" fill="#b45309">F</text><text x="96" y="146" text-anchor="middle" fill="#b45309">F′</text></g></svg>
:::

Quand les deux asymptotes sont **perpendiculaires**, on dit que l'hyperbole est **équilatère**. Leurs pentes b/a et −b/a vérifient alors (b/a)(−b/a) = −1, c'est-à-dire **a = b** — et l'excentricité vaut e = c/a = √(a² + a²)/a = **√2**, toujours la même. Dans le repère porté par ses asymptotes, une hyperbole prend sa forme la plus courte :

> **Théorème** — « Toute hyperbole rapportée à ses asymptotes a une équation de la forme **XY = k** où k est un réel non nul. »

_Exemple détaillé_ — soit ℋ : x² − y² = 4, donc a = b = 2 : hyperbole équilatère, d'asymptotes y = x et y = −x. Prends les vecteurs unitaires u⃗ = (1/√2)(i⃗ + j⃗) et v⃗ = (1/√2)(i⃗ − j⃗) qui les dirigent ; (O, u⃗, v⃗) est orthonormé. Un point M = Xu⃗ + Yv⃗ a pour coordonnées x = (X + Y)/√2 et y = (X − Y)/√2, d'où :

$$ x² − y² = [(X + Y)² − (X − Y)²]/2 = 4XY/2 = 2XY = 4, soit XY = 2 $$

_Contrôle_ — le sommet S(2, 0) vérifie X + Y = 2√2 et X − Y = 0, donc X = Y = √2 et XY = 2 ✓. La courbe de x ↦ 2/x est donc bien une hyperbole, vue depuis ses asymptotes.

> ⚠️ Pour une hyperbole, **c est le plus grand** : b² = c² − a², donc c² = a² + b². Pour une ellipse ce sera l'inverse. Et rien n'oblige a à dépasser b : dans x²/9 − y²/16 = 1, b = 4 est plus grand que a = 3, et pourtant les foyers sont bien sur (Ox). C'est le **signe +** qui désigne l'axe focal, jamais la taille du dénominateur.

## 💠 L'ellipse : le cas 0 < e < 1

> **Définition** — « Soit D une droite, F un point n'appartenant pas à D et un réel **0 < e < 1**. On appelle **ellipse** de foyer F, de directrice D et d'excentricité e, l'ensemble des points M tels que MF/MH = e. »

Comme pour l'hyperbole, l'axe focal coupe la courbe en deux **sommets principaux** dont le milieu O est centre de symétrie ; il existe donc un second foyer F′ et une seconde directrice D′. La perpendiculaire à l'axe focal en O coupe l'ellipse en deux **sommets secondaires**.

> **Théorème (équation réduite)** — « Si S a pour coordonnées (a, 0) et F a pour coordonnées (c, 0) alors l'ellipse ℰ a pour équation **x²/a² + y²/b² = 1**, avec **b² = a² − c²**. »

> **Théorème (les deux cas)** — « • Soit a > b deux réels strictement positifs. L'ensemble des points M(x, y) tels que x²/a² + y²/b² = 1 est une ellipse de centre O, de foyer **F(√(a²−b²), 0)**, de directrice associée la droite d'équation x = a²/c et d'excentricité **e = c/a**, où a² = c² + b². • Soit a < b […] c'est une ellipse de centre O, de foyer **F(0, √(b²−a²))**, de directrice associée la droite d'équation y = b²/c et d'excentricité **e = c/b**, où b² = a² + c². »

_Exemple détaillé_ — soit ℰ : x²/25 + y²/9 = 1. Ici a = 5 > b = 3, donc **c = √(25 − 9) = 4** : foyers F(4, 0) et F′(−4, 0), sommets principaux (±5, 0), sommets secondaires (0, ±3), directrices x = a²/c = **25/4** et x = −25/4, excentricité **e = 4/5**.

_Contrôle par la définition_ — sur le sommet secondaire B(0, 3) : BF = √(16 + 9) = 5 et BH = |0 − 25/4| = 25/4, rapport 5 ÷ (25/4) = **4/5** ✓. Sur le sommet principal S(5, 0) : SF = 1 et SH = 25/4 − 5 = 5/4, rapport 1 ÷ (5/4) = **4/5** ✓.

Remarque au passage la valeur BF = 5 = a : elle n'est pas un accident. Le triangle OFB est rectangle en O, de côtés c et b, donc son hypoténuse vaut √(b² + c²) = a. **La relation a² = b² + c² se lit sur la figure.**

::: figure Le triangle OFB est rectangle en O : son hypoténuse FB mesure exactement a — la relation a² = b² + c² dessinée en un seul trait.
<svg viewBox="0 0 340 240"><path d="M25 118 H320" fill="none" stroke="#94a3b8" stroke-width="1.5"/><path d="M170 22 V214" fill="none" stroke="#94a3b8" stroke-width="1.5"/><path d="M300 118 C300 74.9 241.8 40 170 40 C98.2 40 40 74.9 40 118 C40 161.1 98.2 196 170 196 C241.8 196 300 161.1 300 118 Z" fill="#0f6e56" opacity="0.10"/><path d="M300 118 C300 74.9 241.8 40 170 40 C98.2 40 40 74.9 40 118 C40 161.1 98.2 196 170 196 C241.8 196 300 161.1 300 118 Z" fill="none" stroke="#0f172a" stroke-width="2.4"/><path d="M170 118 L274 118" fill="none" stroke="#0f6e56" stroke-width="3"/><path d="M170 118 L170 40" fill="none" stroke="#0f6e56" stroke-width="3"/><path d="M274 118 L170 40" fill="none" stroke="#b45309" stroke-width="2.6"/><path d="M170 106 L182 106 L182 118" fill="none" stroke="#0f172a" stroke-width="1.6"/><g fill="#0f172a"><circle cx="170" cy="118" r="4"/><circle cx="300" cy="118" r="4.5"/><circle cx="40" cy="118" r="4.5"/><circle cx="170" cy="40" r="4.5"/><circle cx="170" cy="196" r="4.5"/></g><g fill="#b45309"><circle cx="274" cy="118" r="4.5"/><circle cx="66" cy="118" r="4.5"/></g><g font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="160" y="136" text-anchor="middle" fill="#0f172a">O</text><text x="308" y="136" text-anchor="middle" fill="#0f172a">S</text><text x="32" y="136" text-anchor="middle" fill="#0f172a">S′</text><text x="170" y="30" text-anchor="middle" fill="#0f172a">B</text><text x="170" y="214" text-anchor="middle" fill="#0f172a">B′</text><text x="278" y="136" text-anchor="middle" fill="#b45309">F</text><text x="60" y="136" text-anchor="middle" fill="#b45309">F′</text><text x="222" y="110" text-anchor="middle" fill="#0f6e56">c</text><text x="158" y="82" text-anchor="middle" fill="#0f6e56">b</text><text x="232" y="72" text-anchor="middle" fill="#b45309">a</text></g></svg>
:::

_Exemple détaillé (le cas a < b)_ — soit ℰ′ : 9x² + 4y² = 36, c'est-à-dire **x²/4 + y²/9 = 1**. Ici a = 2 < b = 3 : le grand axe est **vertical**, donc c = √(9 − 4) = √5, les foyers sont F(0, √5) et F′(0, −√5), les directrices y = b²/c = 9√5/5 et son opposée, et l'excentricité vaut **e = c/b = √5/3**.

_Contrôle_ — sur le sommet principal B(0, 3) : BF = 3 − √5 ≈ 0,7639 et BH = |3 − 9√5/5| ≈ |3 − 4,0249| = 1,0249. Le rapport vaut 0,7639 ÷ 1,0249 ≈ **0,7454**, et √5/3 ≈ 0,7454 ✓.

Enfin, une ellipse se **paramètre** : si P décrit le cercle de rayon a et P′ le cercle de rayon b sur le même rayon [OP), le point M de coordonnées (a cos θ, b sin θ) décrit ℰ. Vérification immédiate : (a cos θ)²/a² + (b sin θ)²/b² = cos²θ + sin²θ = 1 ✓.

> ⚠️ **e = c/a est faux quand a < b.** L'excentricité vaut toujours c divisé par le **demi-grand axe**. Dans x²/4 + y²/9 = 1, écrire e = √5/2 est l'erreur classique : le demi-grand axe est 3, pas 2, donc e = √5/3 — et il faut bien e < 1, ce que √5/2 ≈ 1,118 ne respecte pas.

## 🗡️ Les tangentes : la règle du dédoublement

Les quatre équations de tangentes du chapitre se retiennent d'un seul geste. Dans l'équation de la conique, **dédouble** chaque terme en y glissant les coordonnées de M₀ :

| Dans l'équation | Remplace par     |
| --------------- | ---------------- |
| x²              | x₀x              |
| y²              | y₀y              |
| 2x              | x + x₀           |
| 2y              | y + y₀           |

| Conique                | Équation           | Tangente en M₀(x₀, y₀)     |
| ---------------------- | ------------------ | -------------------------- |
| Ellipse                | x²/a² + y²/b² = 1  | x₀x/a² + y₀y/b² = 1        |
| Hyperbole              | x²/a² − y²/b² = 1  | x₀x/a² − y₀y/b² = 1        |
| Parabole (axe (Ox))    | y² = 2px           | y₀y = p(x + x₀)            |
| Parabole (axe (Oy))    | x² = 2py           | x₀x = p(y + y₀)            |

Conséquences immédiates : la tangente à une parabole **en son sommet** a pour équation x = 0 ; la tangente à une ellipse ou à une hyperbole au sommet S(a, 0) a pour équation **x = a** ; celle à une ellipse au sommet L(0, b) a pour équation **y = b**.

_Exemple détaillé_ — reprends ℰ : x²/25 + y²/9 = 1 et le point M₀(3, 12/5). D'abord, **est-il sur l'ellipse ?** 9/25 + (144/25)/9 = 9/25 + 16/25 = 1 ✓. La tangente est donc 3x/25 + (12/5)y/9 = 1, soit 3x/25 + 4y/15 = 1 ; en multipliant par 75 :

$$ T : 9x + 20y = 75 $$

_Contrôle n° 1 (le point)_ — 9(3) + 20(12/5) = 27 + 48 = 75 ✓. _Contrôle n° 2 (la tangence)_ — remplace y = (75 − 9x)/20 dans l'équation de ℰ : x²/25 + (75 − 9x)²/3600 = 1, soit 144x² + (75 − 9x)² = 3600, soit 225x² − 1350x + 2025 = 0, soit **(x − 3)² = 0**. Racine double en x = 3 : la droite touche ℰ en M₀ et **nulle part ailleurs** ✓.

_Exemple détaillé (la propriété reine de la parabole)_ — sur 𝒫 : y² = 8x (p = 4, F(2, 0), D : x = −2), prends M₀(2, 4). La tangente vaut 4y = 4(x + 2), soit **y = x + 2**. Soit H₀(−2, 4) le projeté de M₀ sur D. Le milieu de [FH₀] est ((2 − 2)/2, (0 + 4)/2) = (0, 2), qui vérifie 2 = 0 + 2 : **il est sur T** ✓. Et FH₀⃗ = (−4, 4) est orthogonal au vecteur directeur (1, 1) de T, car (−4)(1) + (4)(1) = 0 ✓. La tangente est donc la **médiatrice de [FH₀]** — ce qui redit MF = MH₀, la définition même.

::: figure La tangente en M₀ coupe [FH₀] en son milieu et à angle droit : c'est la médiatrice de [FH₀], autrement dit la définition MF = MH relue comme une propriété de tangence.
<svg viewBox="0 0 300 250"><path d="M55 125 H255" fill="none" stroke="#94a3b8" stroke-width="1.5"/><path d="M71 20 V230" fill="none" stroke="#0f172a" stroke-width="2" stroke-dasharray="7 5"/><path d="M191 29 Q95 77 95 125 Q95 173 191 221" fill="none" stroke="#0f172a" stroke-width="2.4"/><path d="M59 137 L179 17" fill="none" stroke="#0f6e56" stroke-width="2.6"/><path d="M119 125 L71 77" fill="none" stroke="#b45309" stroke-width="2.2"/><path d="M101 119 L113 107" fill="none" stroke="#b45309" stroke-width="2"/><path d="M77 95 L89 83" fill="none" stroke="#b45309" stroke-width="2"/><path d="M102.1 93.9 L95 86.9 L87.9 93.9" fill="none" stroke="#0f172a" stroke-width="1.6"/><g fill="#0f172a"><circle cx="119" cy="125" r="4.5"/><circle cx="119" cy="77" r="5"/><circle cx="71" cy="77" r="4.5"/><circle cx="71" cy="125" r="4"/></g><g font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="128" y="143" text-anchor="middle" fill="#0f172a">F</text><text x="134" y="70" text-anchor="middle" fill="#0f172a">M₀</text><text x="58" y="70" text-anchor="middle" fill="#0f172a">H₀</text><text x="58" y="143" text-anchor="middle" fill="#0f172a">T₀</text><text x="78" y="244" text-anchor="middle" fill="#0f172a">D</text><text x="180" y="34" text-anchor="middle" fill="#0f6e56">T</text></g></svg>
:::

> ⚠️ Le dédoublement ne vaut que si **M₀ appartient à la conique**. Pour chercher les tangentes issues d'un point **extérieur**, on ne dédouble pas : on écrit la droite y = m(x − x_I) + y_I, on la substitue dans l'équation et on impose au trinôme obtenu un **discriminant nul**.

## 🧮 Quand l'équation n'est pas réduite

Une conique dont le centre (ou le sommet) n'est pas en O a une équation encombrée de termes en x et en y. La méthode est toujours la même : **compléter les carrés**, puis translater l'origine.

_Exemple détaillé (parabole)_ — soit 𝒫 : y² + 2y − 4x + 4 = 0. On complète : y² + 2y = (y + 1)² − 1, donc (y + 1)² − 1 − 4x + 4 = 0, c'est-à-dire :

$$ (y + 1)² = 4(x − 3/4) $$

Pose X = x − 3/4 et Y = y + 1, soit une nouvelle origine O′(3/4, −1). Dans (O′, i⃗, j⃗) l'équation devient Y² = 4X : parabole de paramètre **p = 2**, de sommet O′, de foyer d'abscisse X = p/2 = 1 et de directrice X = −p/2 = −1. On revient au repère de départ : **F(7/4, −1)** et **D : x = −1/4**.

_Contrôle_ — le point X = 1, Y = 2 (car Y² = 4) correspond à M(7/4, 1). Vérifie dans l'équation de départ : 1 + 2 − 7 + 4 = 0 ✓. Et MF = |1 − (−1)| = 2 tandis que MH = |7/4 − (−1/4)| = 2 : MF = MH ✓.

_Exemple détaillé (ellipse)_ — soit ℰ : x² + 9y² + 4x − 18y − 23 = 0. On complète les deux carrés : x² + 4x = (x + 2)² − 4 et 9y² − 18y = 9(y − 1)² − 9. D'où (x + 2)² + 9(y − 1)² − 4 − 9 − 23 = 0, soit (x + 2)² + 9(y − 1)² = 36 :

$$ (x + 2)²/36 + (y − 1)²/4 = 1 $$

Centre O′(−2, 1), a = 6, b = 2, c = √(36 − 4) = 4√2, **e = 4√2/6 = 2√2/3 ≈ 0,943 < 1** ✓. Sommets principaux (4, 1) et (−8, 1), sommets secondaires (−2, 3) et (−2, −1), foyers (−2 ± 4√2, 1).

_Contrôle_ — le sommet (4, 1) dans l'équation de départ : 16 + 9 + 16 − 18 − 23 = 0 ✓. Le sommet (−8, 1) : 64 + 9 − 32 − 18 − 23 = 0 ✓. Le sommet secondaire (−2, 3) : 4 + 81 − 8 − 54 − 23 = 0 ✓.

::: figure Les mêmes axes, simplement replantés en O′(−2, 1) : dans le repère (O′, i⃗, j⃗) l'ellipse retrouve son équation réduite X²/36 + Y²/4 = 1.
<svg viewBox="0 0 340 220"><path d="M80 110 H336" fill="none" stroke="#0f172a" stroke-width="1.8"/><path d="M250 25 V148" fill="none" stroke="#0f172a" stroke-width="1.8"/><path d="M85 90 H336" fill="none" stroke="#0f6e56" stroke-width="1.8" stroke-dasharray="7 5"/><path d="M210 45 V140" fill="none" stroke="#0f6e56" stroke-width="1.8" stroke-dasharray="7 5"/><path d="M330 90 C330 67.9 276.3 50 210 50 C143.7 50 90 67.9 90 90 C90 112.1 143.7 130 210 130 C276.3 130 330 112.1 330 90 Z" fill="#0f6e56" opacity="0.10"/><path d="M330 90 C330 67.9 276.3 50 210 50 C143.7 50 90 67.9 90 90 C90 112.1 143.7 130 210 130 C276.3 130 330 112.1 330 90 Z" fill="none" stroke="#0f172a" stroke-width="2.4"/><g fill="#0f172a"><circle cx="250" cy="110" r="4"/></g><g fill="#0f6e56"><circle cx="210" cy="90" r="5"/></g><g font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="258" y="126" text-anchor="middle" fill="#0f172a">O</text><text x="200" y="106" text-anchor="middle" fill="#0f6e56">O′</text><text x="140" y="82" text-anchor="middle" fill="#0f6e56">X</text><text x="222" y="60" text-anchor="middle" fill="#0f6e56">Y</text></g></svg>
:::

Attention : la même manipulation peut ne rien laisser du tout. Avec **+14** au lieu de −23, on obtient (x + 2)² + 9(y − 1)² = −1 : **l'ensemble vide**. Avec **+13**, on obtient (x + 2)² + 9(y − 1)² = 0 : le **point unique** (−2, 1). Une somme de carrés ne pardonne pas.

> **Équation générale du second degré** — « L'ensemble des points M(x, y) tels que **Ax² + By² + Cx + Dy + E = 0** est une courbe dont la nature est donnée par le tableau suivant : AB = 0 ⇒ parabole ou deux droites parallèles ou une droite ou le vide ; AB < 0 ⇒ hyperbole ou deux droites sécantes ; AB > 0 ⇒ ellipse ou cercle ou un point ou le vide. »

> 🗡️ Le signe de **AB** te donne le genre en trois secondes, avant tout calcul : produit nul ⇒ parabole, produit négatif ⇒ hyperbole, produit positif ⇒ ellipse (ou cercle si A = B). Les cas dégénérés ne se décident, eux, qu'après la réduction.

## 👑 Méthode : reconnaître une conique à coup sûr

| Étape | Question                          | Outil                                                            |
| ----- | --------------------------------- | ---------------------------------------------------------------- |
| 1     | Quel genre ?                      | signe de AB · ou valeur de e (1, > 1, < 1)                       |
| 2     | Y a-t-il un terme croisé xy ?     | oui ⇒ passer par la similitude donnée · non ⇒ compléter les carrés |
| 3     | Où est le centre (ou le sommet) ? | complétion des carrés ⇒ nouvelle origine O′                      |
| 4     | Quels éléments ?                  | a, b, puis c par b² = a² − c² (ellipse) ou b² = c² − a² (hyperbole) |
| 5     | Vérification                      | réinjecter un sommet dans l'équation **de départ**, et contrôler MF/MH = e |

_Exemple détaillé (synthèse)_ — soit 𝒞 : x² − 9y² − 8x + 36y − 56 = 0.

**Étape 1** — A = 1 et B = −9, donc AB = −9 < 0 : c'est une **hyperbole** (ou deux droites sécantes). **Étape 3** — x² − 8x = (x − 4)² − 16 et −9y² + 36y = −9(y − 2)² + 36, d'où (x − 4)² − 9(y − 2)² − 16 + 36 − 56 = 0, soit (x − 4)² − 9(y − 2)² = 36 :

$$ (x − 4)²/36 − (y − 2)²/4 = 1 $$

**Étape 4** — centre O′(4, 2), a = 6, b = 2, c = √(36 + 4) = 2√10, **e = c/a = √10/3 ≈ 1,054 > 1** ✓. Sommets (10, 2) et (−2, 2) ; foyers (4 ± 2√10, 2) ; asymptotes y − 2 = ±(x − 4)/3.

**Étape 5** — le sommet (10, 2) dans l'équation de départ : 100 − 36 − 80 + 72 − 56 = 0 ✓ ; le sommet (−2, 2) : 4 − 36 + 16 + 72 − 56 = 0 ✓. Un point hors de l'axe, (4 + 6√2, 4) : 155,88 − 144 − 99,88 + 144 − 56 = 0 ✓. Et la directrice associée est X = a²/c = 36/(2√10) = 9√10/5 ≈ 5,692, donc x ≈ 9,692 : pour le sommet (10, 2), SF = |10 − 10,3246| = 0,3246 et SH = |10 − 9,692| = 0,3079, de rapport **1,054 = e** ✓. Identification confirmée.

> 🗡️ Quand l'énoncé fournit une **similitude** (comme dans les problèmes du manuel), ne cherche pas à casser le terme en xy à la main : applique la transformation, réduis la courbe image — bien plus simple —, puis reviens en arrière. Les distances sont multipliées par le rapport de la similitude, les orthogonalités sont conservées, donc **le genre et l'excentricité ne changent pas**.

> 🏆 Quatorzième porte franchie, héros : d'un point, d'une droite et d'un nombre, tu sais désormais faire jaillir trois courbes, lire leurs éléments dans une équation réduite, dédoubler pour obtenir une tangente et redresser n'importe quelle équation du second degré. Au chapitre suivant, on quitte la feuille : le plan devient l'**espace**, et le produit scalaire y prend une troisième dimension.
