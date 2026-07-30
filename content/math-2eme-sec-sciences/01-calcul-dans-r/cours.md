# ⚔️ Calcul dans ℝ — la forge des nombres réels

> 💡 «Avant d'affronter les équations, les polynômes et les fonctions, il faut réapprendre à frapper juste. Ce chapitre est la forge : on y reforge tous les outils de calcul, un par un.»

Bienvenue en 2ème année secondaire, héros. Ce premier chapitre est un **chapitre bilan** : le manuel ne t'y donne presque aucune leçon nouvelle, il t'y propose une longue suite d'**activités**. Tout ce que tu vas lire ici, tu l'as déjà croisé — mais cette fois tu dois le maîtriser au niveau de l'outil : rapide, sûr, réutilisable. Chaque section est une arme que les chapitres suivants (équations, polynômes, arithmétique, fonctions) supposeront déjà affûtée.

## 🔢 Les ensembles de nombres

Cinq ensembles s'emboîtent les uns dans les autres :

| Symbole | Nom               | Exemples             |
| ------- | ----------------- | -------------------- |
| ℕ       | entiers naturels  | 0 ; 1 ; 12 ; √36 = 6 |
| ℤ       | entiers relatifs  | −4 ; −63/7 = −9 ; 12 |
| 𝔻       | décimaux          | 2,5 ; −0,125 ; 12    |
| ℚ       | rationnels        | 5/8 ; −2/3 ; 1,98    |
| ℝ       | réels             | √5 ; π ; √3/7        |

$$ ℕ ⊂ ℤ ⊂ 𝔻 ⊂ ℚ ⊂ ℝ $$

Un **décimal** est un rationnel qui s'écrit a/10ⁿ : sa forme irréductible n'a que des 2 et des 5 au dénominateur. Ainsi 5/8 = 0,625 est décimal, mais **1/3 ne l'est pas** (0,333… ne s'arrête jamais) — il reste rationnel. Et √5, √2, π ne sont même pas rationnels : ce sont des **irrationnels**, ils n'existent que dans ℝ.

::: figure Les cinq ensembles s'emboîtent : tout entier naturel est un entier relatif, tout décimal est un rationnel, et tout rationnel est un réel
<svg viewBox="0 0 340 200">
<rect x="5" y="5" width="330" height="190" rx="8" fill="#eef2ff" stroke="#0f172a" stroke-width="2"/>
<rect x="33" y="25" width="274" height="150" rx="7" fill="#dbeafe" stroke="#0f172a" stroke-width="2"/>
<rect x="61" y="45" width="218" height="110" rx="6" fill="#bbf7d0" stroke="#0f172a" stroke-width="2"/>
<rect x="89" y="65" width="162" height="70" rx="5" fill="#fef08a" stroke="#0f172a" stroke-width="2"/>
<rect x="117" y="82" width="106" height="36" rx="5" fill="#fdba74" stroke="#0f172a" stroke-width="2"/>
<g font-size="15" font-weight="700" fill="#0f172a" text-anchor="middle">
<text x="19" y="110">ℝ</text>
<text x="47" y="110">ℚ</text>
<text x="75" y="110">𝔻</text>
<text x="103" y="110">ℤ</text>
<text x="140" y="105">ℕ</text>
</g>
<g font-size="12" fill="#0f172a" text-anchor="middle">
<text x="200" y="19">π ; √5</text>
<text x="200" y="39">2/3 ; 1/3</text>
<text x="200" y="59">2,5 ; 0,625</text>
<text x="200" y="78">−4 ; −63/7</text>
<text x="185" y="105">0 ; 1 ; 12</text>
</g>
</svg>
:::

> ⚠️ Piège classique : ℚ ⊄ 𝔻. L'inclusion va dans l'autre sens, 𝔻 ⊂ ℚ. Beaucoup d'élèves écrivent « ℚ ⊂ 𝔻 » par symétrie — c'est faux, 1/3 le prouve.

## 📊 Proportionnalité et pourcentages

Deux grandeurs sont **proportionnelles** quand on passe de l'une à l'autre en multipliant toujours par le même nombre (le **coefficient de proportionnalité**). Un ressort qui s'allonge de 9 mm sous 15 g s'allonge de 9/15 = 0,6 mm par gramme : sous 50 g, l'allongement vaut 50 × 0,6 = **30 mm**.

Pour les pourcentages, une seule idée : **appliquer t %, c'est multiplier par le coefficient 1 + t/100** (ou 1 − t/100 pour une baisse).

- **Taux de remise** : un article à 32 dinars soldé à 20,400 dinars a baissé de 11,600 dinars, soit 11,600/32 = 0,3625 = **36,25 %**.
- **TVA** : prix TTC = prix HT × (1 + t/100). Avec 58 dinars HT et t = 17 %, on obtient 58 × 1,17 = **67,860 dinars**. Inversement, prix HT = prix TTC / 1,17.
- **Pourcentages successifs** : ils se **multiplient**, ils ne s'additionnent pas. Une hausse de 10 % suivie d'une hausse de 20 % donne 1,10 × 1,20 = 1,32, soit **+32 %** (et non +30 %).

> ⚠️ Le piège n°1 du chapitre : additionner des pourcentages successifs. Une hausse de 10 % puis une baisse de 10 % donne 1,10 × 0,90 = 0,99 : on **perd** 1 %, on ne revient pas au prix de départ.

## 🧮 Identités remarquables, développement et factorisation

Les identités à connaître par cœur, dans les deux sens (à gauche pour **développer**, à droite pour **factoriser**) :

$$ (a + b)² = a² + 2ab + b² ; (a − b)² = a² − 2ab + b² ; (a − b)(a + b) = a² − b² $$

$$ (a + b)³ = a³ + 3a²b + 3ab² + b³ ; (a − b)³ = a³ − 3a²b + 3ab² − b³ $$

$$ a³ − b³ = (a − b)(a² + ab + b²) ; a³ + b³ = (a + b)(a² − ab + b²) $$

_Exemple détaillé_ : (3 − √5)² = 3² − 2 × 3 × √5 + (√5)² = 9 − 6√5 + 5 = **14 − 6√5**. Attention, (√5)² = 5 et non √5.

_Exemple détaillé_ : (2 + a)³ = 2³ + 3 × 2² × a + 3 × 2 × a² + a³ = **8 + 12a + 6a² + a³**.

_Exemple détaillé (factorisation)_ : 25x² − 9 = (5x)² − 3² = **(5x − 3)(5x + 3)** ; et x³ − 64 = x³ − 4³ = **(x − 4)(x² + 4x + 16)**.

Ces identités servent aussi au **calcul mental** : (75895478)² − 75895477 × 75895479 = n² − (n − 1)(n + 1) = n² − (n² − 1) = **1**.

> 🗡️ Réflexe de factorisation : cherche d'abord un **facteur commun**, puis une **identité remarquable**. Dans A = (4x − 1)² − (4x − 1)(3x − 6), le facteur commun (4x − 1) saute aux yeux : A = (4x − 1)(4x − 1 − 3x + 6) = (4x − 1)(x + 5).

## ⚖️ Comparer et encadrer des réels

Pour comparer deux réels, on étudie le **signe de leur différence**. Cela donne trois résultats à retenir.

- Si **0 < a < 1** : a² < a < √a. Si **a > 1** : √a < a < a².
- Si **0 < a < 1** : 1/a > 1 > a. Si **a > 1** : 1/a < 1 < a.

_Exemple_ : a = 0,34 → a² = 0,1156 < a = 0,34 < √a ≈ 0,583, et 1/a ≈ 2,94 > 1. _Exemple_ : a = 4 → √a = 2 < a = 4 < a² = 16, et 1/a = 0,25 < 1.

::: figure Pour 0 < a < 1, le carré de côté a tient dans le rectangle de dimensions 1 et a : son aire a² est donc plus petite que a
<svg viewBox="0 0 340 180">
<rect x="20" y="40" width="150" height="90" fill="#bfdbfe" stroke="#0f172a" stroke-width="2"/>
<rect x="210" y="40" width="90" height="90" fill="#fdba74" stroke="#0f172a" stroke-width="2"/>
<g font-size="13" font-weight="700" fill="#0f172a" text-anchor="middle">
<text x="95" y="150">1</text>
<text x="10" y="90">a</text>
<text x="255" y="150">a</text>
<text x="200" y="90">a</text>
<text x="95" y="25">aire = a</text>
<text x="255" y="25">aire = a²</text>
</g>
</svg>
:::

**Encadrer**, c'est propager un encadrement à travers les opérations. On ajoute librement, mais **multiplier par un nombre négatif renverse les inégalités**.

_Exemple détaillé_ : si −2 ≤ a ≤ 3, alors en multipliant par −3 (qui renverse) : −9 ≤ −3a ≤ 6, puis en ajoutant 5 : **−4 ≤ −3a + 5 ≤ 11**.

Trois inégalités classiques, toutes issues de (x − y)² ≥ 0 :

$$ 2xy ≤ x² + y² $$

$$ x + 1/x ≥ 2 ; x/y + y/x ≥ 2 $$

La première est valable pour **tous les réels** x et y, sans condition de signe : elle se réécrit x² − 2xy + y² ≥ 0, c'est-à-dire (x − y)² ≥ 0, ce qui est toujours vrai. Les deux suivantes, elles, exigent des réels **strictement positifs**, car on y divise par x et par y. Le minimum de x + 1/x sur ]0 ; +∞[ vaut donc **2**, atteint pour **x = 1**.

Deux autres inégalités utiles, pour a > 0 et b > 0 : √(a + b) < √a + √b (car (√a + √b)² = a + b + 2√(ab) > a + b) et 1/(a + b) < 1/a + 1/b.

Enfin, l'inégalité entre **moyenne arithmétique** et **moyenne géométrique** (AM-GM), pour a > 0 et b > 0 :

$$ (a + b)/2 ≥ √(ab) $$

::: figure Le demi-cercle de diamètre [AB] : la hauteur CH vaut √(ab) et le rayon OC vaut (a + b)/2 — une hauteur est toujours plus courte que le rayon
<svg viewBox="0 0 340 200">
<path d="M30 160 A 140 140 0 0 1 310 160" fill="#e0f2fe" stroke="#0f172a" stroke-width="2"/>
<path d="M30 160 L310 160" fill="none" stroke="#0f172a" stroke-width="2"/>
<path d="M120 160 L120 29.2" fill="none" stroke="#c2410c" stroke-width="2.5"/>
<path d="M170 160 L120 29.2" fill="none" stroke="#1d4ed8" stroke-width="2.5"/>
<path d="M120 148 L132 148 L132 160" fill="none" stroke="#0f172a" stroke-width="2"/>
<g fill="#0f172a"><circle cx="30" cy="160" r="4"/><circle cx="120" cy="160" r="4"/><circle cx="310" cy="160" r="4"/><circle cx="170" cy="160" r="4"/><circle cx="120" cy="29.2" r="4"/></g>
<g font-size="14" font-weight="700" fill="#0f172a" text-anchor="middle">
<text x="26" y="180">A</text>
<text x="120" y="180">H</text>
<text x="170" y="180">O</text>
<text x="312" y="180">B</text>
<text x="120" y="20">C</text>
</g>
<g font-size="13" font-weight="700" text-anchor="middle">
<text x="75" y="178" fill="#0f172a">a</text>
<text x="215" y="178" fill="#0f172a">b</text>
<text x="94" y="100" fill="#c2410c">√(ab)</text>
<text x="180" y="95" fill="#1d4ed8">(a + b)/2</text>
</g>
</svg>
:::

> 🗡️ Ces inégalités permettent aussi d'encadrer sans calculatrice : √2003 + √2005 < 2√2004, car la moyenne arithmétique de 2003 et 2005 dépasse leur moyenne géométrique.

**L'inégalité triangulaire** — pour tous réels x et y (la valeur absolue |x| est révisée plus bas) :

$$ |x + y| ≤ |x| + |y| $$

Une somme peut se **compenser**, jamais s'amplifier : avec x = 7 et y = −3, |7 + (−3)| = 4 tandis que |7| + |−3| = 10, donc 4 ≤ 10. L'égalité n'a lieu que si x et y sont de **même signe** : |7 + 3| = 10 = |7| + |3|.

Sa lecture géométrique est celle du triangle — **le chemin direct est toujours le plus court**. Pour trois points A, B et C :

$$ AB ≤ AC + CB $$

avec égalité seulement lorsque C appartient au segment [AB]. C'est l'outil qui permet, dans un triangle ABC et pour un point M intérieur, de démontrer MB + MC ≤ AB + AC.

::: figure Le trajet direct de A à B est plus court que le détour par C : AB ≤ AC + CB
<svg viewBox="0 0 340 200">
<path d="M40 165 L150 40 L290 165 Z" fill="#eef2ff" stroke="#0f172a" stroke-width="1.5"/>
<path d="M40 165 L290 165" fill="none" stroke="#1d4ed8" stroke-width="4"/>
<path d="M40 165 L150 40" fill="none" stroke="#c2410c" stroke-width="3"/>
<path d="M150 40 L290 165" fill="none" stroke="#c2410c" stroke-width="3"/>
<g fill="#0f172a"><circle cx="40" cy="165" r="4.5"/><circle cx="290" cy="165" r="4.5"/><circle cx="150" cy="40" r="4.5"/></g>
<g font-size="14" font-weight="700" fill="#0f172a" text-anchor="middle">
<text x="32" y="185">A</text>
<text x="298" y="185">B</text>
<text x="150" y="30">C</text>
</g>
<g font-size="13" font-weight="700" text-anchor="middle">
<text x="165" y="188" fill="#1d4ed8">AB</text>
<text x="80" y="100" fill="#c2410c">AC</text>
<text x="235" y="100" fill="#c2410c">CB</text>
</g>
</svg>
:::

## 🌱 Les radicaux

Trois techniques à maîtriser.

**1. Rationaliser un dénominateur** — on multiplie haut et bas par la **quantité conjuguée**, pour faire apparaître une différence de carrés.

_Exemple détaillé_ : 1/(3 + √2) = (3 − √2)/((3 + √2)(3 − √2)) = (3 − √2)/(9 − 2) = **(3 − √2)/7**.

**2. Simplifier un radical double √(m ± n√p)** — on reconnaît le carré caché sous la racine.

_Exemple détaillé_ : 14 − 6√5 = 9 − 6√5 + 5 = (3 − √5)², donc √(14 − 6√5) = |3 − √5| = **3 − √5** (car 3 > √5 ≈ 2,24).

**3. La somme télescopique** — en rationalisant, 1/(√k + √(k+1)) = √(k+1) − √k. On en tire que la somme
1/(1 + √2) + 1/(√2 + √3) + … + 1/(√99 + √100) se réduit en cascade à √100 − √1 = **9**.

> ⚠️ √(x²) = |x|, **pas** x. C'est le lien direct avec la section suivante : si le contenu du carré peut être négatif, la valeur absolue est obligatoire.

**Formule de Héron** — l'aire d'un triangle de côtés a, b, c, de demi-périmètre p = (a + b + c)/2, vaut :

$$ A = √(p(p − a)(p − b)(p − c)) $$

_Exemple détaillé_ : pour un triangle de côtés 18, 24 et 30 cm, p = 36 et A = √(36 × 18 × 12 × 6) = √46656 = **216 cm²**.

> 🗡️ Ce triangle-là est **rectangle** : 18² + 24² = 324 + 576 = 900 = 30². Le raccourci « produit des deux côtés de l'angle droit divisé par 2 » donne donc 18 × 24/2 = 216 cm² et **confirme** Héron. Retiens bien la condition : ce raccourci n'est valable que si les deux côtés choisis forment un angle droit — sinon, seule la formule de Héron répond.

## 📏 La valeur absolue

Par définition, |x| = x si x ≥ 0 et |x| = −x si x < 0. **Écrire un nombre sans valeur absolue, c'est d'abord déterminer le signe de ce qui est entre les barres.**

_Exemple détaillé_ : √3 ≈ 1,73 < 2, donc √3 − 2 est négatif et |√3 − 2| = **2 − √3**.

**Équations** : |A| = |B| équivaut à A = B **ou** A = −B (deux cas, donc en général deux solutions). Ainsi |2x + 1| = |3 − x| donne 2x + 1 = 3 − x (soit x = 2/3) ou 2x + 1 = x − 3 (soit x = −4) : S = {−4 ; 2/3}.

**Inéquations** : |x − a| < r équivaut à a − r < x < a + r ; |x − a| > r équivaut à x < a − r ou x > a + r. Une équation |A| = k n'a **aucune solution** si k < 0.

**Distance** : sur une droite graduée, si A a pour abscisse x_A et B pour abscisse x_B, alors AB = |x_B − x_A|.

::: figure Sur une droite graduée, la distance AB est la valeur absolue de la différence des abscisses
<svg viewBox="0 0 340 90">
<path d="M10 55 L330 55" fill="none" stroke="#0f172a" stroke-width="2"/>
<g stroke="#0f172a" stroke-width="1.5">
<path d="M20 51 L20 59"/><path d="M45 51 L45 59"/><path d="M70 51 L70 59"/><path d="M95 51 L95 59"/><path d="M120 51 L120 59"/><path d="M145 51 L145 59"/><path d="M170 51 L170 59"/><path d="M195 51 L195 59"/><path d="M220 51 L220 59"/><path d="M245 51 L245 59"/><path d="M270 51 L270 59"/><path d="M295 51 L295 59"/>
</g>
<g fill="#0f172a"><circle cx="120" cy="55" r="4"/><circle cx="145" cy="55" r="4"/></g>
<g fill="#c2410c"><circle cx="95" cy="55" r="4.5"/><circle cx="195" cy="55" r="4.5"/></g>
<path d="M95 30 L195 30" fill="none" stroke="#c2410c" stroke-width="2"/>
<path d="M95 30 L103 26 M95 30 L103 34 M195 30 L187 26 M195 30 L187 34" fill="none" stroke="#c2410c" stroke-width="2"/>
<g font-size="12" font-weight="700" fill="#0f172a" text-anchor="middle">
<text x="120" y="75">0</text>
<text x="145" y="75">1</text>
<text x="95" y="75">−1</text>
<text x="195" y="75">3</text>
<text x="120" y="45">O</text>
<text x="145" y="45">I</text>
</g>
<g font-size="12" font-weight="700" fill="#c2410c" text-anchor="middle">
<text x="95" y="45">B</text>
<text x="195" y="45">A</text>
<text x="145" y="22">AB = |−1 − 3| = 4</text>
</g>
</svg>
:::

## 🔬 Valeurs approchées, écriture scientifique et ordre de grandeur

**Définition (manuel, p.15)** : soit n un entier. Le décimal a est une **valeur approchée à 10ⁿ près** du réel b lorsque |b − a| ≤ 10ⁿ. Si a < b, l'approximation est **par défaut** ; si a > b, elle est **par excès**.

L'**arrondi** est celle des deux valeurs approchées qui est la plus proche de b.

_Exemple détaillé_ : 75/17 = 4,411764705… Sa valeur approchée à 10⁻² près **par défaut** est 4,41, **par excès** 4,42, et son **arrondi** à 10⁻² est 4,41 (car 4,4117… est plus proche de 4,41 que de 4,42). À 10⁻³ près : 4,411 par défaut, 4,412 par excès, arrondi 4,412.

L'**écriture scientifique** d'un nombre non nul est a × 10ⁿ avec **1 ≤ |a| < 10** et n entier. Ainsi 35 215 000 = **3,5215 × 10⁷** (et non 35,215 × 10⁶ ni 0,35215 × 10⁸ : ces écritures sont justes en valeur, mais leur facteur a n'est pas dans [1 ; 10[).

> 🗡️ Avant de multiplier des grandeurs, pense aux **conversions** : 1 km = 10³ m, donc 1 km² = 10⁶ m² (et non 10³ m²). Une erreur de conversion décale l'ordre de grandeur de plusieurs puissances de 10.

**Remarque (manuel, p.16)** : si a × 10ⁿ est l'écriture scientifique d'un nombre, son **ordre de grandeur** est b × 10ⁿ, où b est l'arrondi de a à l'unité. L'ordre de grandeur de 35 215 000 est donc 4 × 10⁷.

_Exemple détaillé_ : la Terre mesure environ 5,10 × 10⁸ km² et la Tunisie environ 1,62 × 10⁵ km². Il faudrait 5,10 × 10⁸ / (1,62 × 10⁵) ≈ 3148 « Tunisie » pour couvrir la Terre, soit un ordre de grandeur de **3 × 10³**.

> 🏆 La forge est éteinte, héros : ensembles, pourcentages, identités, encadrements, radicaux, valeur absolue et ordres de grandeur sont réaffûtés. Le chapitre 2 t'attend avec les problèmes du premier et du second degré — et il supposera que chacun de ces outils te vient sans réfléchir.
