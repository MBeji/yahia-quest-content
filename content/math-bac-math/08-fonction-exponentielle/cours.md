# ⚔️ Fonction exponentielle — la courbe qui est sa propre dérivée

> 💡 «Une seule fonction ne change pas quand on la dérive. Celui qui la maîtrise tient la croissance, la décroissance et presque tout le programme d'analyse.»

En 1748, Euler calculait déjà l'accroissement d'une population « d'une trentième chaque année » et les intérêts composés d'une dette de 400 000 florins ; c'est en poussant (1 + 1/N)^N vers l'infini qu'il rencontra le nombre **e**. Toi, tu arrives par l'autre porte : au chapitre précédent tu as construit **ln**, continue et strictement croissante de ℝ*₊ sur ℝ. Le chapitre 4 t'a appris qu'une telle fonction possède une **réciproque**. Cette réciproque a un nom : c'est l'exponentielle. Tout ce qui suit — propriétés, limites, dérivées, primitives — n'est que la relecture de ln dans le miroir Δ : y = x.

## 🏰 exp, la réciproque de ln

Tu sais déjà que ln est continue et **strictement croissante** sur ]0, +∞[, avec lim_{x→0⁺} ln x = −∞ et lim_{x→+∞} ln x = +∞. D'après le chapitre 4, ln réalise donc une **bijection** de ℝ*₊ sur ℝ : tout réel possède un antécédent unique par ln. On peut donc la retourner.

> **Définition — fonction exponentielle** (p.159) — « On appelle fonction exponentielle la fonction réciproque de la fonction logarithme népérien. L'image d'un réel x par la fonction exponentielle est noté [sic] e^x. »

exp est donc définie sur **ℝ** tout entier (le domaine de départ de exp est l'ensemble d'arrivée de ln) et à valeurs dans **ℝ*₊** (l'ensemble de départ de ln). Autrement dit : **e^x existe pour tout x, et e^x est toujours strictement positif.**

> **Conséquences** (p.159) — « • Pour tout réel x et pour tout réel strictement positif y, y = e^x ⟺ x = ln y. • Pour tout réel x, ln(e^x) = x. • Pour tout réel x > 0, e^(ln x) = x. • ln e = 1. »

Ces quatre lignes sont exactement les règles f(x) = y ⟺ f⁻¹(y) = x et f⁻¹∘f = id du chapitre 4, écrites avec ln et exp. Retiens surtout l'**équivalence** : elle transforme toute équation exponentielle en équation logarithmique, et réciproquement.

Comme f et f⁻¹ ont des courbes symétriques par rapport à la première bissectrice, on obtient gratuitement le dessin de exp.

::: figure Les deux courbes se déduisent l'une de l'autre par le pliage le long de Δ : le point (0, 1) de C_exp devient le point (1, 0) de C_ln.
<svg viewBox="0 0 330 320"><path d="M10 200 H320" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M120 310 V15" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M320 200 l-7 -3.5 l0 7 z" fill="#0f172a"/><path d="M120 15 l-3.5 7 l7 0 z" fill="#0f172a"/><path d="M20 300 L310 10" fill="none" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="5 4"/><polyline points="20,196.7 40,194.6 60,191.1 80,185.3 100,175.7 120,160 130,148.6 140,134.1 150,115.3 160,91.3 170,60.4 176,37.8 180,20.7" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/><polyline points="123.3,300 125.4,280 128.9,260 134.7,240 144.3,220 160,200 171.4,190 185.9,180 204.7,170 228.7,160 259.6,150 282.2,144 299.3,140" fill="none" stroke="#b45309" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/><g fill="#0f172a"><circle cx="120" cy="160" r="3.5"/><circle cx="160" cy="200" r="3.5"/></g><g font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="196" y="32" fill="#0f6e56">C_exp</text><text x="292" y="132" text-anchor="middle" fill="#b45309">C_ln</text><text x="252" y="46" text-anchor="middle" fill="#94a3b8">Δ : y = x</text><text x="106" y="156" text-anchor="middle" fill="#0f172a">1</text><text x="163" y="216" text-anchor="middle" fill="#0f172a">1</text></g></svg>
:::

_Exemple détaillé_ — quelques valeurs à connaître par cœur. e^0 = 1 (car ln 1 = 0), e^1 = e ≈ 2,71828 (car ln e = 1), e^2 ≈ 7,389 et e^(−1) = 1/e ≈ 0,368. _Contrôle_ : chaque valeur est strictement positive, et elles croissent avec x ✓.

_Exemple détaillé_ — simplifions e^(−2 ln 3). On écrit e^(−2 ln 3) = e^(ln(3^(−2))) = 3^(−2) = **1/9**, car ln(3^(−2)) = −2 ln 3. _Contrôle numérique_ : −2 ln 3 ≈ −2,197 et e^(−2,197) ≈ 0,111 = 1/9 ✓.

> ⚠️ **e^x n'est jamais nul et jamais négatif.** Dans un produit A(x)·e^(u(x)), le facteur exponentiel ne change donc **jamais** le signe : le signe du produit est celui de A(x). C'est le raccourci le plus rentable du chapitre.

## ⚡ Les règles de calcul de l'exponentielle

Chaque propriété de exp est la traduction d'une propriété de ln. Par exemple, ln(e^a × e^b) = ln(e^a) + ln(e^b) = a + b ; or ln(e^(a+b)) = a + b aussi, et ln est injective : les deux nombres sont égaux.

> **Propriétés** (p.160) — « Soit deux réels a et b. P₁ : e^(a+b) = e^a × e^b, e^(a−b) = e^a/e^b, e^−a = 1/e^a. P₂ : Pour tout entier n, e^(na) = (e^a)^n. P₃ : Pour tout entier naturel q ≥ 2, e^(a/q) = q√(e^a). P₄ : Pour tout entier naturel q ≥ 2 et tout entier p, e^((p/q)a) = q√(e^(pa)). »

Un tableau pour ne plus hésiter — **l'exponentielle transforme les sommes en produits**, exactement à l'envers de ln :

| ln transforme…      | exp transforme…               |
| ------------------- | ----------------------------- |
| ln(ab) = ln a + ln b | e^(a+b) = e^a × e^b           |
| ln(a/b) = ln a − ln b | e^(a−b) = e^a/e^b             |
| ln(aⁿ) = n ln a     | e^(na) = (e^a)^n              |
| ln(q√a) = (1/q)ln a | e^(a/q) = q√(e^a)             |

_Exemple détaillé_ — simplifions (√(e³)/√(e^(−4))) × ⁴√(e²). On ramène tout à une puissance de e :

$$ √(e³) = e^(3/2),  √(e^(−4)) = e^(−2),  ⁴√(e²) = e^(2/4) = e^(1/2) $$

$$ (e^(3/2)/e^(−2)) × e^(1/2) = e^(3/2 + 2 + 1/2) = e^4 $$

_Contrôle_ : 3/2 + 2 + 1/2 = 4 exactement, et e⁴ ≈ 54,6 ; le calcul direct donne (4,4817/0,1353) × 1,6487 ≈ 33,12 × 1,6487 ≈ 54,6 ✓.

_Exemple détaillé (identité à vérifier)_ — montrons que e^(2x) + e^(−2x) + 2 = (e^x + e^(−x))². On développe le carré :

$$ (e^x + e^(−x))² = (e^x)² + 2 e^x e^(−x) + (e^(−x))² = e^(2x) + 2 e^0 + e^(−2x) $$

Comme e^0 = 1, on retrouve bien e^(2x) + e^(−2x) + 2 ✓. _Contrôle numérique en x = 1_ : e² + e^(−2) + 2 = 7,389 + 0,135 + 2 = 9,524, et (e + 1/e)² = (2,71828 + 0,36788)² = 3,08616² = 9,524 ✓.

> 🗡️ **Le réflexe « tout en e^(quelque chose) »** : dès qu'une expression mêle racines, puissances et quotients d'exponentielles, réécris chaque facteur sous la forme e^α et **additionne les exposants**. Aucune erreur possible.

## 🛡️ Équations et inéquations avec exponentielle

exp est une bijection de ℝ sur ℝ*₊, strictement croissante (on le démontre à la section suivante). Deux conséquences opératoires :

$$ e^A = e^B ⟺ A = B  et  e^A ≤ e^B ⟺ A ≤ B $$

Et l'équation e^A = k n'a de solution que si **k > 0** ; dans ce cas A = ln k.

_Exemple détaillé (équation simple)_ — résolvons e^(2x+3) = 4. Comme 4 > 0, l'équation équivaut à 2x + 3 = ln 4, soit x = (ln 4 − 3)/2 ≈ (1,3863 − 3)/2 ≈ **−0,8069**. _Contrôle_ : 2x + 3 ≈ 1,3863 et e^(1,3863) ≈ 4 ✓.

_Exemple détaillé (équation « bicarrée »)_ — résolvons e^(2x) + e^x − 2 = 0. On pose **X = e^x**, avec la contrainte X > 0. Comme e^(2x) = (e^x)² = X², l'équation devient X² + X − 2 = 0, dont le discriminant vaut 1 + 8 = 9 :

$$ X = (−1 + 3)/2 = 1  ou  X = (−1 − 3)/2 = −2 $$

La racine −2 est **rejetée** (X = e^x > 0). Il reste e^x = 1, donc x = ln 1 = **0**. _Contrôle_ : e^0 + e^0 − 2 = 1 + 1 − 2 = 0 ✓. L'ensemble des solutions est S = {0}.

_Exemple détaillé (inéquation)_ — résolvons e^(3x) ≤ 4e^x. On divise par e^x, qui est **strictement positif** (le sens de l'inégalité est conservé) : e^(3x−x) ≤ 4, c'est-à-dire e^(2x) ≤ 4, soit 2x ≤ ln 4, donc x ≤ (ln 4)/2 = **ln 2 ≈ 0,693**. _Contrôle en x = ln 2_ : e^(3 ln 2) = 2³ = 8 et 4e^(ln 2) = 4 × 2 = 8 : égalité à la borne ✓. En x = 1 : e³ ≈ 20,1 > 4e ≈ 10,9, l'inégalité est bien fausse ✓.

_Exemple_ — e^(3x) ≤ e^(x²) ⟺ 3x ≤ x² ⟺ x(x − 3) ≥ 0 ⟺ x ∈ ]−∞, 0] ∪ [3, +∞[. Et e^(x(x−1)) > 1 = e^0 ⟺ x(x − 1) > 0 ⟺ x ∈ ]−∞, 0[ ∪ ]1, +∞[.

> ⚠️ Une inéquation du type e^(x²−1) < 1 se traite en revenant à **l'exposant** : x² − 1 < 0, soit −1 < x < 1. En revanche −2 < e^(x²−1) est vraie pour **tout** x, puisqu'une exponentielle est toujours positive : cette moitié d'encadrement n'apporte aucune contrainte.

## 🔮 Étude de la fonction exponentielle

Toutes les propriétés analytiques de exp se lisent sur ln par la symétrie. La dérivée en particulier : le chapitre 4 donne (f⁻¹)′(y) = 1/f′(f⁻¹(y)). Avec f = ln et f′(t) = 1/t :

$$ exp′(x) = 1/ln′(e^x) = 1/(1/e^x) = e^x $$

C'est la propriété fondatrice : **exp est sa propre dérivée**. Comme e^x > 0, exp est strictement croissante sur ℝ.

> **Théorème** (p.161) — « • lim_{x→−∞} e^x = 0, lim_{x→+∞} e^x = +∞, lim_{x→+∞} e^x/x = +∞, lim_{x→0} (e^x − 1)/x = 1. • La fonction exponentielle est dérivable sur ℝ et sa fonction dérivée est la fonction x ↦ e^x. La fonction exponentielle est strictement croissante sur ℝ. • La fonction exponentielle est bijective de ℝ sur ℝ*₊ et pour tout réel x, e^x > 0. »

| x       | −∞ | → | +∞ |
| ------- | -- | - | -- |
| (e^x)′  |    | + |    |
| e^x     | 0  | ↗ | +∞ |

Deux limites méritent leur démonstration.

- **e^x/x → +∞ en +∞** : on pose X = e^x, donc x = ln X et X → +∞. Alors e^x/x = X/ln X, et comme (ln X)/X → 0, son inverse tend vers +∞ ✓. Graphiquement, C_exp admet une **branche parabolique de direction (Oy)**.
- **(e^x − 1)/x → 1 en 0** : c'est le taux d'accroissement (e^x − e^0)/(x − 0), donc le **nombre dérivé de exp en 0**, qui vaut e^0 = 1 ✓. _Contrôle numérique_ : pour x = 0,01, (e^(0,01) − 1)/0,01 = 0,010050/0,01 = 1,005 ✓.

**La tangente en 0 et la position de la courbe.** La tangente T à C au point d'abscisse 0 a pour équation y = exp′(0)(x − 0) + exp(0), soit **T : y = x + 1**. Posons h(x) = e^x − x − 1 : alors h′(x) = e^x − 1, négative sur ]−∞, 0[ et positive sur ]0, +∞[. La fonction h atteint donc son **minimum** en 0, où h(0) = 1 − 0 − 1 = 0. Conclusion :

$$ pour tout réel x,  e^x ≥ x + 1,  avec égalité si et seulement si x = 0 $$

C est donc **au-dessus** de sa tangente T (la courbe est convexe). _Contrôle_ : en x = 1, e ≈ 2,718 ≥ 2 ✓ ; en x = −1, 0,368 ≥ 0 ✓ ; en x = −3, 0,0498 ≥ −2 ✓.

::: figure La courbe de exp reste au-dessus de la droite y = x + 1 et ne la touche qu'au point A(0, 1) : c'est l'inégalité e^x ≥ x + 1, lue d'un coup d'œil.
<svg viewBox="0 0 330 280"><path d="M15 200 H320" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M150 270 V25" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M320 200 l-7 -3.5 l0 7 z" fill="#0f172a"/><path d="M150 25 l-3.5 7 l7 0 z" fill="#0f172a"/><path d="M49.2 258.8 L206.7 101.3" fill="none" stroke="#b45309" stroke-width="2.2"/><polyline points="24,197.9 45,196.6 66,194.3 87,190.6 108,184.5 129,174.5 150,158 171,130.8 192,85.8 206.7,38" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/><circle cx="150" cy="158" r="4" fill="#0f172a"/><g font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="214" y="40" fill="#0f6e56">C : y = e^x</text><text x="60" y="270" fill="#b45309">T : y = x + 1</text><text x="158" y="150" fill="#0f172a">A(0, 1)</text></g></svg>
:::

**L'équation f′ = f.** Cherchons toutes les fonctions dérivables sur ℝ telles que f′(x) = f(x). Posons h(x) = e^(−x) f(x) : h est dérivable et

$$ h′(x) = −e^(−x) f(x) + e^(−x) f′(x) = e^(−x)(f′(x) − f(x)) = 0 $$

Donc h est **constante**, égale à un réel k, et f(x) = k e^x. Réciproquement, toute fonction x ↦ k e^x vérifie bien f′ = f. **Les solutions de (E) : f′ = f sont exactement les fonctions x ↦ k e^x, k ∈ ℝ.**

> 🗡️ **Les tangentes de C_exp forment un éventail régulier** : la tangente au point d'abscisse a a pour équation y = e^a(x − a) + e^a. En prenant a = n + 1, on obtient en x = n : e^(n+1)(n − n − 1) + e^(n+1) = 0. **La tangente au point d'abscisse n + 1 coupe l'axe des abscisses exactement en (n, 0)** — un point de construction gratuit à chaque tracé.

## 🧪 Limites usuelles et croissances comparées

Face à x² − e^(2x) ou x e^x, on tombe sur des formes indéterminées « ∞ − ∞ » ou « 0 × ∞ ». Le programme fournit l'arbitrage : **l'exponentielle l'emporte toujours sur la puissance.**

> **Théorème** (p.163) — « Soit m et n deux entiers naturels non nuls, lim_{x→+∞} e^(nx)/x^m = +∞, lim_{x→−∞} x^m e^(nx) = 0. »

> **Théorème** (p.170) — « Soit r un rationnel strictement positif. lim_{x→+∞} (ln x)/x^r = 0 ; lim_{x→0⁺} x^r ln x = 0 ; lim_{x→+∞} e^x/x^r = +∞. »

La hiérarchie à mémoriser, du plus lent au plus rapide en +∞ : **ln x ≪ x^r ≪ e^x**.

_Exemple détaillé (forme ∞ − ∞)_ — calculons lim_{x→+∞} (x³ − e^(2x)). On met e^(2x) en facteur :

$$ x³ − e^(2x) = e^(2x)(x³/e^(2x) − 1) $$

Or x³/e^(2x) → 0 (croissances comparées), donc la parenthèse tend vers −1 tandis que e^(2x) → +∞ : la limite est **−∞**. _Contrôle numérique en x = 10_ : 1000 − e^20 ≈ 1000 − 4,85×10⁸, très négatif ✓.

_Exemple détaillé (forme 0 × ∞)_ — calculons lim_{x→−∞} x e^x. On pose t = −x, qui tend vers +∞ :

$$ x e^x = −t e^(−t) = −t/e^t → 0 $$

La limite vaut donc **0**, et plus précisément 0⁻ car x < 0. _Contrôle numérique en x = −10_ : −10 × e^(−10) = −10 × 4,54×10⁻⁵ ≈ −4,5×10⁻⁴ ✓.

_Exemple détaillé (étude complète)_ — étudions f(x) = x e^x sur ℝ.

1. **Limites** : lim_{−∞} f = 0⁻ (ci-dessus) — la droite y = 0 est **asymptote horizontale** en −∞ ; lim_{+∞} f = +∞, et f(x)/x = e^x → +∞ donne une **branche parabolique de direction (Oy)**.
2. **Dérivée** : f′(x) = e^x + x e^x = (1 + x)e^x, du signe de 1 + x. Donc f décroît sur ]−∞, −1] et croît sur [−1, +∞[, avec un minimum f(−1) = −1/e ≈ **−0,368**.
3. **Point d'inflexion** : f″(x) = e^x + (1 + x)e^x = (2 + x)e^x, qui **change de signe** en x = −2. Le point I(−2, −2e^(−2)) ≈ (−2 ; −0,271) est un point d'inflexion, et la tangente en I a pour coefficient directeur f′(−2) = −e^(−2) ≈ −0,135.

_Contrôle_ : f(0) = 0, f(1) = e ≈ 2,718, f(−1) ≈ −0,368 < f(−2) ≈ −0,271 : le minimum est bien en −1, pas en −2 ✓.

> ⚠️ Ne confonds pas **minimum** et **point d'inflexion** : le premier annule f′ (ici en −1), le second fait changer f″ de signe (ici en −2). Les deux abscisses n'ont aucune raison de coïncider.

## 🧮 La fonction x ↦ e^(u(x)) : dériver, primitiver, intégrer

C'est la forme sous laquelle l'exponentielle apparaît dans 90 % des problèmes de bac.

> **Théorème** (p.164) — « Soit u une fonction dérivable sur un intervalle I. La fonction h : x ↦ e^(u(x)) est dérivable sur I et h′(x) = u′(x)e^(u(x)), x ∈ I. »

> **Corollaire** (p.164) — « Soit u une fonction dérivable sur un intervalle I. Les primitives sur I de la fonction x ↦ u′(x)e^(u(x)) sont les fonctions x ↦ e^(u(x)) + k, k ∈ ℝ. »

_Exemple détaillé (dérivée)_ — dérivons f(x) = (2x + 1)e^(−3x). C'est un produit ; avec u(x) = −3x on a u′(x) = −3 :

$$ f′(x) = 2 e^(−3x) + (2x + 1)(−3)e^(−3x) = e^(−3x)(2 − 6x − 3) = −(6x + 1)e^(−3x) $$

_Contrôle en x = 0_ : la formule donne f′(0) = −1 ; le calcul direct du produit en 0 donne 2 × 1 + 1 × (−3) = −1 ✓. Signe : e^(−3x) > 0, donc f′ est du signe de −(6x + 1), positive pour x < −1/6.

_Exemple détaillé (dérivée)_ — pour g(x) = x³e^(3x) : g′(x) = 3x²e^(3x) + 3x³e^(3x) = **3x²(1 + x)e^(3x)**, du signe de 1 + x (car 3x² ≥ 0 et l'exponentielle est positive).

_Exemple détaillé (primitives)_ — cherchons une primitive de f(x) = x e^(x²) sur ℝ. On veut faire apparaître u′e^u avec u(x) = x², donc u′(x) = 2x. Or x e^(x²) = **½** × 2x e^(x²) = ½ u′(x)e^(u(x)). Une primitive est donc F(x) = ½ e^(x²). _Vérification par dérivation_ : F′(x) = ½ × 2x × e^(x²) = x e^(x²) ✓.

Trois autres, à reconnaître d'un coup d'œil :

| f(x)               | u(x)    | primitive F(x)      |
| ------------------ | ------- | ------------------- |
| e^(−3x)            | −3x     | −(1/3)e^(−3x) + k   |
| (2x + 1)e^(x²+x)   | x² + x  | e^(x²+x) + k        |
| sin x · e^(cos x)  | cos x   | −e^(cos x) + k      |

_Contrôle de la dernière_ : (−e^(cos x))′ = −(−sin x)e^(cos x) = sin x · e^(cos x) ✓.

_Exemple détaillé (intégrale par une primitive)_ — calculons ∫₀¹ e^x/(e^x + 1)² dx. Avec u(x) = e^x + 1, on a u′(x) = e^x, donc l'intégrande vaut u′/u², dont une primitive est −1/u :

$$ ∫₀¹ e^x/(e^x + 1)² dx = [−1/(e^x + 1)]₀¹ = −1/(e + 1) + 1/2 ≈ 0,5 − 0,269 = 0,231 $$

_Contrôle_ : l'intégrande vaut 0,25 en x = 0 et 0,197 en x = 1 ; une aire de l'ordre de 0,23 sur une largeur 1 est cohérente ✓.

_Exemple détaillé (intégration par parties)_ — calculons ∫₀¹ x e^x dx. On pose f(t) = t (donc f′ = 1) et g′(t) = e^t (donc g(t) = e^t) ; la formule du chapitre 6 donne :

$$ ∫₀¹ t e^t dt = [t e^t]₀¹ − ∫₀¹ e^t dt = e − [e^t]₀¹ = e − (e − 1) = 1 $$

_Contrôle_ : l'intégrande croît de 0 à e ≈ 2,718 sur [0, 1] ; une valeur de 1 est plausible ✓. Et ∫₀¹ x e^(x²) dx = [½e^(x²)]₀¹ = **(e − 1)/2 ≈ 0,859** — attention, ce n'est **pas** la même intégrale.

> ⚠️ ∫ x e^(x²) dx se règle par **reconnaissance de u′e^u** (aucune IPP), alors que ∫ x e^x dx exige une **intégration par parties**. Confondre les deux est l'erreur n°1 du chapitre : regarde toujours si le facteur devant l'exponentielle est la dérivée de l'exposant.

_Exemple détaillé (suite d'intégrales)_ — posons Iₙ = ∫₀¹ xⁿ e^(−x) dx pour n ≥ 1. Sur [0, 1], on a 0 ≤ e^(−x) ≤ 1, donc 0 ≤ xⁿ e^(−x) ≤ xⁿ ; en intégrant cet encadrement :

$$ 0 ≤ Iₙ ≤ ∫₀¹ xⁿ dx = 1/(n + 1) → 0,  donc Iₙ → 0 $$

Une IPP (f = xⁿ, g′ = e^(−x), g = −e^(−x)) donne la récurrence Iₙ = [−xⁿ e^(−x)]₀¹ + n∫₀¹ x^(n−1) e^(−x) dx = **n Iₙ₋₁ − 1/e**. _Contrôle_ : I₀ = ∫₀¹ e^(−x)dx = 1 − 1/e ≈ 0,632, donc I₁ = 1 × I₀ − 1/e = 1 − 2/e ≈ **0,264**, valeur bien comprise entre 0 et 1/2 ✓.

## 📐 Exponentielle de base a

Comment donner un sens à 2^√3 ou à (3/2)^0,7 ? On part de l'identité aⁿ = e^(n ln a), vraie pour tout entier n et tout a > 0 (car e^(n ln a) = e^(ln(aⁿ)) = aⁿ), et on **l'érige en définition** pour un exposant quelconque.

> **Encadré — puissance à exposant réel** (p.166) — « Soit un réel a > 0. Pour tout réel b, on pose a^b = e^(b ln a). »

> **Définition — exponentielle de base a** (p.166) — « Soit un réel a > 0. On appelle fonction exponentielle de base a la fonction x ↦ a^x. »

> **Propriétés** (p.166) — « Pour tous nombres réels strictement positifs a et b et tous réels c et d, a^(c+d) = a^c × a^d ; (a^c)^d = a^(cd) ; a^(c−d) = a^c/a^d ; a^c × b^c = (ab)^c ; a^c/b^c = (a/b)^c. »

> **Conséquences** (p.166–167) — « Soit un réel a > 0. La fonction x ↦ a^x est dérivable sur ℝ et sa fonction dérivée est la fonction x ↦ (ln a)a^x. La fonction x ↦ a^x est strictement croissante sur ℝ si a > 1. La fonction x ↦ a^x est strictement décroissante sur ℝ si 0 < a < 1. La fonction x ↦ 1^x est une fonction constante. Si a > 1 alors lim_{x→+∞} a^x = +∞ ; lim_{x→−∞} a^x = 0. Si 0 < a < 1 alors lim_{x→+∞} a^x = 0 ; lim_{x→−∞} a^x = +∞. »

La dérivée se retrouve en une ligne : (a^x)′ = (e^(x ln a))′ = (ln a) e^(x ln a) = (ln a) a^x. Le **signe de ln a** décide donc de tout : positif si a > 1, négatif si 0 < a < 1.

::: figure Les trois courbes passent toutes par (0, 1) ; y = 2^x et y = e^x montent (base > 1), y = (1/2)^x descend (base < 1), et les deux courbes de base 2 et 1/2 sont symétriques par rapport à l'axe des ordonnées.
<svg viewBox="0 0 330 250"><path d="M25 200 H315" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M165 215 V15" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M315 200 l-7 -3.5 l0 7 z" fill="#0f172a"/><path d="M165 15 l-3.5 7 l7 0 z" fill="#0f172a"/><polyline points="45,195 85,190 125,180 165,160 205,120 225,86.9 245,40 251,22.4" fill="none" stroke="#0f172a" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/><polyline points="45,198 85,194.6 125,185.3 165,160 185,134.1 205,91.3 221,37.8 225,20.7" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/><polyline points="285,195 245,190 205,180 165,160 125,120 105,86.9 85,40 79,22.4" fill="none" stroke="#b45309" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/><circle cx="165" cy="160" r="4" fill="#0f172a"/><g font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="231" y="26" fill="#0f6e56">y = e^x</text><text x="258" y="58" fill="#0f172a">y = 2^x</text><text x="12" y="30" fill="#b45309">y = (1/2)^x</text><text x="172" y="176" fill="#0f172a">(0, 1)</text></g></svg>
:::

_Exemple détaillé (calculs)_ — e^(3 ln 2) = 2³ = **8** ; e^(4 ln(3/2)) = (3/2)⁴ = 81/16 = **5,0625** ; e^(−2 ln(1/3)) = (1/3)^(−2) = **9** ; e^(−2 ln √2) = (√2)^(−2) = **1/2**. _Contrôle du premier_ : 3 ln 2 ≈ 2,079 et e^(2,079) ≈ 8 ✓.

_Exemple détaillé (équation)_ — résolvons (√2)^x = 2^(−x+1). On ramène **tout à la base 2** : (√2)^x = (2^(1/2))^x = 2^(x/2). L'égalité 2^(x/2) = 2^(−x+1) équivaut, en passant au logarithme (ln 2 ≠ 0), à x/2 = −x + 1, soit (3/2)x = 1 et **x = 2/3**. _Contrôle_ : (√2)^(2/3) = 2^(1/3) ≈ 1,2599 et 2^(−2/3+1) = 2^(1/3) ≈ 1,2599 ✓.

_Exemple détaillé (limite)_ — lim_{x→−∞} (1/2)^(3−2x). Posons X = 3 − 2x : quand x → −∞, X → +∞. Comme 0 < 1/2 < 1, on a (1/2)^X → **0**. _Contrôle en x = −10_ : (1/2)^23 ≈ 1,2×10⁻⁷ ✓.

> ⚠️ **a^x ne se dérive pas comme x^n.** Écrire (2^x)′ = x·2^(x−1) est faux : l'exposant est la **variable**, pas la base. La bonne formule est (2^x)′ = (ln 2)·2^x.

## 👑 Fonctions puissances x ↦ x^r

Même définition, mais cette fois c'est la **base** qui varie. On se place sur ℝ*₊, où ln x existe.

> **Définition — fonction puissance** (p.169) — « Soit r un rationnel. On appelle fonction puissance r la fonction x ↦ e^(r·ln x), x > 0. »

> **Notation** (p.169) — « Pour tout rationnel r et tout x > 0, on note e^(r·ln x) = x^r. »

> **Théorème** (p.169) — « Soit r un rationnel. La fonction x ↦ x^r est dérivable sur ℝ*₊ et sa dérivée est la fonction x ↦ r x^(r−1). »

> **Corollaire** (p.169) — « Soit r un rationnel différent de −1. Les primitives sur ℝ*₊ de la fonction x ↦ x^r sont les fonctions x ↦ (1/(r + 1))x^(r+1) + k, k ∈ ℝ. »

> **Encadré — limites des fonctions puissances** (p.169) — « Si r > 0 alors lim_{x→+∞} x^r = +∞ ; lim_{x→0⁺} x^r = 0. Si r < 0 alors lim_{x→+∞} x^r = 0 ; lim_{x→0⁺} x^r = +∞. »

Les formules connues pour un exposant entier restent donc valables pour un exposant rationnel — et elles englobent les **racines** du chapitre 4 : pour n ≥ 2 et x > 0,

$$ ⁿ√x = x^(1/n)  car e^((1/n)ln x) = e^(ln(ⁿ√x)) = ⁿ√x $$

_Exemple détaillé (étude)_ — soit f(x) = √(x³) sur ℝ*₊. On écrit f(x) = (x³)^(1/2) = x^(3/2) = e^((3/2)ln x). Sa dérivée est f′(x) = (3/2)x^(1/2) = (3/2)√x > 0 : f est **strictement croissante**. Avec lim_{0⁺} f = 0 et lim_{+∞} f = +∞, f réalise une **bijection de ℝ*₊ sur ℝ*₊**. Sa réciproque s'obtient en résolvant y = x^(3/2), soit x = y^(2/3) : f⁻¹(y) = y^(2/3). _Contrôle_ : f(4) = √64 = 8 et f⁻¹(8) = 8^(2/3) = (8^(1/3))² = 2² = 4 ✓ ; et f′(4) = (3/2)×2 = 3.

_Exemple détaillé (intégrale)_ — calculons ∫₁² x^(4/3) dx. Ici r = 4/3, donc r + 1 = 7/3 :

$$ ∫₁² x^(4/3) dx = [(3/7)x^(7/3)]₁² = (3/7)(2^(7/3) − 1) $$

Or 2^(7/3) = 2² × 2^(1/3) ≈ 4 × 1,2599 = 5,0397, d'où le résultat ≈ (3/7) × 4,0397 ≈ **1,731**. _Contrôle_ : l'intégrande passe de 1 à 2^(4/3) ≈ 2,52 sur une largeur 1 ; une aire d'environ 1,73 est cohérente ✓.

_Exemple_ — limites : lim_{x→+∞} x^(2/3) = +∞ et lim_{x→0⁺} x^(2/3) = 0 (car 2/3 > 0) ; lim_{x→+∞} x^(−4/3) = 0 et lim_{x→0⁺} x^(−4/3) = +∞ (car −4/3 < 0).

> 🗡️ **Comparer deux croissances par le quotient.** Pour situer x^(1/3) et x^(2/3) en +∞, forme le quotient x^(1/3)/x^(2/3) = x^(−1/3) → 0 : c'est donc x^(2/3) qui l'emporte. Le même geste, avec ln x/x^r → 0 et e^x/x^r → +∞, règle toutes les indéterminations du chapitre.

> ⚠️ x^r n'est défini que pour **x > 0** dans ce chapitre. Écrire (−8)^(1/3) = −2 sort du cadre : la définition passe par ln x, donc la base doit être strictement positive.

> 🏆 Huitième porte franchie, héros : tu as retourné ln pour en tirer exp, tu sais qu'elle est sa propre dérivée, qu'elle écrase toute puissance en +∞, qu'elle se dérive et se primitive en e^u, et qu'elle donne un sens à a^b comme à x^r. Il te reste une marche : au chapitre suivant, l'équation f′ = f devient y′ = ay + b — et l'exponentielle, cette fois, sera la clé de toutes les équations différentielles.
