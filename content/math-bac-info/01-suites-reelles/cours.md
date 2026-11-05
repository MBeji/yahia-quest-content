# ⚔️ Suites réelles — prévoir où va une boucle

> 💡 «Une boucle de programme fabrique une suite : avant de la lancer, on voudrait savoir où elle va.»

Une suite est une file de nombres u₀, u₁, u₂, … : ce chapitre apprend à dire si elle monte, où elle reste et où elle finit. Huit notions, avec un fil rouge : le temps de réponse d'un serveur, tₙ = 2 + 6/(n + 1) ms après n séries d'optimisations. On suppose acquis le raisonnement par récurrence, les suites arithmétiques et géométriques et les limites de fonctions en +∞ (3ᵉ année). Sauf mention contraire, les suites sont définies sur ℕ.

## 📈 Sens de variation et opérations sur les suites

Un serveur gagne en vitesse après chaque série d'optimisations. Après n séries, son temps de réponse est tₙ = 2 + 6/(n + 1) ms : 8 ; 5 ; 4 ; 3,5 ; 3,2 ; … Les premiers temps baissent, mais rien ne garantit qu'ils baisseront encore à la série 1000.
Comment démontrer un sens de variation pour tous les entiers n, et pas seulement sur les premiers termes ?

::: definition
Soit (uₙ) une suite définie pour tout entier n ≥ n₀.
**Croissante** : uₙ ≤ uₙ₊₁ pour tout n ≥ n₀. **Décroissante** : uₙ ≥ uₙ₊₁ pour tout n ≥ n₀.
**Monotone** : croissante ou décroissante.
Avec des inégalités strictes (uₙ < uₙ₊₁ ou uₙ > uₙ₊₁), on dit **strictement** croissante ou décroissante.
:::

Le temps tₙ est lui-même construit avec des opérations sur les suites, qu'il faut nommer.

::: definition
Soient (u) et (v) deux suites définies pour n ≥ n₀.
**Somme** u + v : suite de terme général uₙ + vₙ. **Produit** u × v : suite de terme général uₙ × vₙ.
**Quotient** u/v, lorsque vₙ ≠ 0 pour tout n ≥ n₀ : suite de terme général uₙ/vₙ.
:::

Ainsi tₙ est la somme de la suite constante 2 et du produit de la constante 6 par la suite de terme général 1/(n + 1).

::: exemple Le temps de réponse baisse

1. tₙ₊₁ − tₙ = 6/(n + 2) − 6/(n + 1). On met au même dénominateur (n + 1)(n + 2) pour comparer.
2. tₙ₊₁ − tₙ = 6[(n + 1) − (n + 2)]/((n + 1)(n + 2)) = −6/((n + 1)(n + 2)).
3. Cette différence est strictement négative pour tout n ∈ ℕ, puisque n + 1 et n + 2 sont positifs.
4. (tₙ) est strictement décroissante : de t₂ = 4 à t₃ = 3,5, la baisse est bien 6/(3 × 4) = 0,5.

:::

::: exemple Comparer le rapport à 1

1. wₙ = (n + 2)/3ⁿ a tous ses termes strictement positifs : on peut comparer wₙ₊₁/wₙ à 1 au lieu d'étudier une différence.
2. wₙ₊₁/wₙ = ((n + 3)/3ⁿ⁺¹) × (3ⁿ/(n + 2)) = (n + 3)/(3(n + 2)), car 3ⁿ⁺¹ = 3 × 3ⁿ.
3. (n + 3)/(3(n + 2)) < 1 ⟺ n + 3 < 3n + 6 ⟺ 0 < 2n + 3, vrai pour tout n ∈ ℕ.
4. Le rapport est inférieur à 1 et les termes sont positifs : (wₙ) est strictement décroissante (2 ; 1 ; 4/9 ; …).

:::

Une suite définie par cas se calcule par une boucle. La suite de Syracuse est définie par u₀ ∈ ℕ*, uₙ₊₁ = uₙ/2 si uₙ est pair et uₙ₊₁ = 3uₙ + 1 si uₙ est impair ; pour u₀ = 6, la boucle est :

```
u ← 6
Tant que u ≠ 1 :
    si u est pair : u ← u / 2
    sinon : u ← 3 × u + 1
    afficher u
```

::: exemple Dérouler la boucle de Syracuse

1. u₀ = 6 est pair, donc u₁ = 6/2 = 3.
2. 3 est impair, donc u₂ = 3 × 3 + 1 = 10, puis u₃ = 5 (10 est pair), u₄ = 16 (5 est impair), u₅ = 8, u₆ = 4, u₇ = 2 et u₈ = 1.
3. La suite descend de 6 à 3, remonte à 10, puis redescend : elle n'est ni croissante ni décroissante.
4. Elle atteint 1 au rang 8, et la boucle s'arrête. On ignore encore si, pour tout départ u₀, elle finit par atteindre 1.

:::

::: piege
**Erreur : conclure sur les premiers termes.** Pour cₙ = 20n/(n² + 9), on calcule c₀ = 0, c₁ = 2, c₂ ≈ 3,08, c₃ ≈ 3,33 et l'on écrit « (cₙ) est croissante ». L'erreur tente parce que quatre termes qui montent ressemblent à une règle. Mais c₄ = 80/25 = 3,2 est inférieur à c₃ : la suite redescend à partir du rang 3, et des termes en nombre fini ne prouvent rien sur tous les n.
:::

::: propriete
Pour étudier le sens de variation de (uₙ), on dispose de quatre techniques.
**Différence** : on étudie le signe de uₙ₊₁ − uₙ.
**Rapport** : si tous les termes sont strictement positifs, uₙ₊₁/uₙ ≥ 1 donne une suite croissante et uₙ₊₁/uₙ ≤ 1 une suite décroissante.
**Fonction** : si uₙ = f(n) et si f est monotone sur [n₀ ; +∞[, alors (uₙ) a le même sens de variation à partir du rang n₀.
**Récurrence** : on démontre par récurrence que uₙ ≤ uₙ₊₁ pour tout n (ou uₙ ≥ uₙ₊₁).
Cas limite : un rapport inférieur à 1 ne donne une suite décroissante que si les termes sont positifs. Pour vₙ = −10 × (4/5)ⁿ, vₙ₊₁/vₙ = 4/5 < 1, et pourtant (vₙ) est croissante : −10 ; −8 ; −6,4 ; …
:::

::: verifie À toi : un sens de variation à partir d'un rang
Étudier le sens de variation de uₙ = n² − 6n sur ℕ.

---

uₙ₊₁ − uₙ = (n + 1)² − 6(n + 1) − n² + 6n = 2n − 5. Cette différence est négative pour n ≤ 2 et positive pour n ≥ 3 : u₀ ≥ u₁ ≥ u₂ ≥ u₃ (0 ; −5 ; −8 ; −9), puis (uₙ) est strictement croissante à partir de n = 3 (−9 ; −8 ; −5 ; …). Elle n'est pas monotone sur ℕ. On retrouve le rang 3 avec la technique « fonction » : f(x) = x² − 6x a son minimum en x = 3.
:::

::: retenir
Un sens de variation se prouve pour tous les n, par le signe de uₙ₊₁ − uₙ ou par le rapport à 1 pour des termes strictement positifs, et non sur les premiers termes seulement.
:::

## 🔒 Suite majorée, minorée, bornée

Le serveur ne peut pas être plus lent qu'au départ ni plus rapide qu'un matériel parfait. On voudrait prouver que, pour tout n, le temps tₙ ne dépasse jamais 8 ms et ne descend jamais sous 2 ms.
Comment montrer qu'un seuil n'est franchi par aucun terme d'une suite ?

::: definition
Soit (uₙ) une suite définie pour tout entier n ≥ n₀.
**Majorée** : il existe un réel M tel que uₙ ≤ M pour tout n ≥ n₀ ; M est un majorant.
**Minorée** : il existe un réel m tel que uₙ ≥ m pour tout n ≥ n₀ ; m est un minorant.
**Bornée** : à la fois majorée et minorée, soit m ≤ uₙ ≤ M pour tout n ≥ n₀.
Un majorant n'est pas unique : tout réel supérieur à M est encore un majorant.
:::

::: exemple Le temps de réponse est borné

1. Pour tout n ∈ ℕ, 6/(n + 1) > 0, donc tₙ = 2 + 6/(n + 1) > 2 : la suite est minorée par 2.
2. Comme n + 1 ≥ 1, on a 6/(n + 1) ≤ 6, donc tₙ ≤ 8 : la suite est majorée par 8.
3. Ainsi 2 < tₙ ≤ 8 pour tout n : (tₙ) est bornée. Le majorant 8 est atteint (t₀ = 8), le minorant 2 ne l'est jamais.

:::

::: exemple Une suite qui alterne

1. vₙ = (−1)ⁿ(2n + 1)/(n + 2) vaut 1/2 ; −1 ; 5/4 ; −7/5 ; … Le signe alterne, donc (vₙ) n'est pas monotone.
2. |vₙ| = (2n + 1)/(n + 2) = 2 − 3/(n + 2) < 2, car 3/(n + 2) > 0.
3. Donc −2 < vₙ < 2 pour tout n : (vₙ) est bornée, bien que non monotone.

:::

::: piege
**Erreur : croire qu'une suite décroissante est bornée.** (tₙ) est décroissante et bornée, et l'on en conclut que toute suite décroissante l'est. L'erreur tente parce qu'une suite qui descend est bloquée en haut par son premier terme. Mais uₙ = −n est décroissante, majorée par u₀ = 0, et n'est pas minorée : pour tout réel m, −n < m dès que l'entier n dépasse −m.
:::

::: propriete
**Premier terme** : une suite croissante est minorée par son premier terme ; une suite décroissante est majorée par son premier terme.
**Valeur absolue** : (uₙ) est bornée si et seulement s'il existe un réel M tel que |uₙ| ≤ M pour tout n.
Cas limite : un nombre voisin de la limite n'est pas un majorant. Pour aₙ = 2 − 5/(n + 1) (n ≥ 1), le réel 1,99 est dépassé dès que 5/(n + 1) < 0,01, soit n ≥ 500 : 1,99 n'est pas un majorant, alors que 2 en est un.
:::

::: verifie À toi : borner une fraction
Montrer que uₙ = (6n + 1)/(2n + 3) est bornée sur ℕ.

---

On écrit 3 − uₙ = (6n + 9 − 6n − 1)/(2n + 3) = 8/(2n + 3) > 0, donc uₙ < 3. Pour n ∈ ℕ, 6n + 1 > 0 et 2n + 3 > 0, donc uₙ > 0. Ainsi 0 < uₙ < 3 pour tout n : (uₙ) est bornée.
:::

::: retenir
Une suite est majorée, minorée ou bornée lorsqu'un réel fixe limite tous ses termes ; on le prouve par une inégalité vraie pour tout n.
:::

## 🧭 Limite d'une suite : la définition par ε

Les valeurs de tₙ semblent se rapprocher de 2 ms sans jamais l'atteindre. « Se rapprocher » reste vague : à partir de quel rang le temps est-il à moins de 1 ms de 2 ? à moins de 0,1 ms ?
Comment dire précisément qu'une suite tend vers un réel, ou vers l'infini ?

::: figure À partir du rang 6, tous les points (n ; tₙ) restent dans la bande centrée en ℓ = 2 et de demi-largeur ε = 1 ; le point n = 5 est sur le bord, donc il n'y est pas (l'axe horizontal est tracé à la hauteur 0,5)
<svg viewBox="0 0 340 236">
<title>Les points (n ; tₙ) pour n de 0 à 10 : à partir de n = 6, ils restent dans la bande ]1 ; 3[ centrée en 2</title>
<rect x="50" y="151.0" width="275.6" height="44.0" fill="#0f6e56" opacity="0.12"/>
<line x1="50" y1="173.0" x2="325.59999999999997" y2="173.0" stroke="#0f6e56" stroke-width="1.4" stroke-dasharray="5 3"/>
<line x1="50" y1="151.0" x2="325.59999999999997" y2="151.0" stroke="#0f6e56" stroke-width="1" stroke-dasharray="2 3"/>
<line x1="50" y1="195.0" x2="325.59999999999997" y2="195.0" stroke="#0f6e56" stroke-width="1" stroke-dasharray="2 3"/>
<line x1="50" y1="206" x2="336" y2="206" stroke="#0f172a" stroke-width="1.6"/>
<line x1="50" y1="214" x2="50" y2="12" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="336,206 328,202 328,210" fill="#0f172a"/>
<polygon points="50,12 46,20 54,20" fill="#0f172a"/>
<circle cx="50" cy="41.0" r="4.2" fill="#ffffff" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="76" cy="107.0" r="4.2" fill="#ffffff" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="102" cy="129.0" r="4.2" fill="#ffffff" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="128" cy="140.0" r="4.2" fill="#ffffff" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="154" cy="146.6" r="4.2" fill="#ffffff" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="180" cy="151.0" r="4.2" fill="#ffffff" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="206" cy="154.1" r="4.2" fill="#0f6e56" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="232" cy="156.5" r="4.2" fill="#0f6e56" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="258" cy="158.3" r="4.2" fill="#0f6e56" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="284" cy="159.8" r="4.2" fill="#0f6e56" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="310" cy="161.0" r="4.2" fill="#0f6e56" stroke="#0f172a" stroke-width="1.2"/>
<line x1="50" y1="203" x2="50" y2="209" stroke="#0f172a" stroke-width="1.2"/>
<text x="50" y="224" text-anchor="middle" fill="#0f172a" font-size="12" font-weight="700">0</text>
<line x1="180" y1="203" x2="180" y2="209" stroke="#0f172a" stroke-width="1.2"/>
<text x="180" y="224" text-anchor="middle" fill="#0f172a" font-size="12" font-weight="700">5</text>
<line x1="310" y1="203" x2="310" y2="209" stroke="#0f172a" stroke-width="1.2"/>
<text x="310" y="224" text-anchor="middle" fill="#0f172a" font-size="12" font-weight="700">10</text>
<text x="42" y="199.0" text-anchor="end" fill="#0f172a" font-size="12" font-weight="700">1</text>
<text x="42" y="177.0" text-anchor="end" fill="#0f172a" font-size="12" font-weight="700">2</text>
<text x="42" y="155.0" text-anchor="end" fill="#0f172a" font-size="12" font-weight="700">3</text>
<text x="323.59999999999997" y="168.0" text-anchor="end" fill="#0f6e56" font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">ℓ = 2</text>
<text x="323.59999999999997" y="146.0" text-anchor="end" fill="#0f6e56" font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">ℓ + ε</text>
<text x="323.59999999999997" y="190.0" text-anchor="end" fill="#0f6e56" font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">ℓ − ε</text>
<text x="62" y="22" text-anchor="start" fill="#0f172a" font-size="12" font-weight="700">tₙ</text>
<text x="330" y="198" text-anchor="middle" fill="#0f172a" font-size="12" font-weight="700">n</text>
</svg>
:::

La bande de la figure est l'intervalle ]ℓ − ε ; ℓ + ε[ : dire que les termes y restent à partir d'un rang p, c'est dire que |tₙ − ℓ| < ε pour n ≥ p.

::: definition
**Limite finie** : (uₙ) tend vers le réel ℓ quand n tend vers +∞ si, pour tout réel ε > 0, il existe p ∈ ℕ tel que : n ≥ p ⟹ |uₙ − ℓ| < ε. On écrit lim uₙ = ℓ.
**Limite infinie** : (uₙ) tend vers +∞ (respectivement −∞) si, pour tout réel A > 0, il existe p ∈ ℕ tel que : n ≥ p ⟹ uₙ > A (respectivement uₙ < −A). On écrit lim uₙ = +∞ (respectivement −∞).
**Convergente** : qui admet une limite réelle. **Divergente** : non convergente (limite infinie, ou pas de limite).
:::

::: exemple Le temps de réponse tend vers 2

1. |tₙ − 2| = 6/(n + 1), positif. Donner ε = 1 revient à chercher n tel que 6/(n + 1) < 1.
2. 6/(n + 1) < 1 ⟺ n + 1 > 6 ⟺ n > 5 : le rang p = 6 convient, comme sur la figure.
3. Pour un ε > 0 quelconque, 6/(n + 1) < ε ⟺ n > 6/ε − 1 : on prend pour p un entier supérieur à 6/ε.
4. Donc lim tₙ = 2. Pourtant tₙ = 2 est impossible, puisque 6/(n + 1) ≠ 0 : la suite n'atteint jamais sa limite.

:::

::: exemple Une limite infinie

1. uₙ = n² et un réel A > 0 : on cherche n tel que n² > A.
2. Si n > √A, alors n² > A. On prend pour p un entier supérieur à √A.
3. Pour tout n ≥ p, uₙ > A : lim n² = +∞.

:::

Pour trouver ce rang sans résoudre l'inégalité, un algorithme teste les entiers un par un. Pour ε = 0,1, il cherche le plus petit n tel que 6/(n + 1) < 0,1 :

```
n ← 0
Tant que 6 / (n + 1) ≥ 0,1 :
    n ← n + 1
afficher n
```

::: exemple Lire le résultat de l'algorithme

1. La boucle continue tant que 6/(n + 1) ≥ 0,1, et s'arrête dès que 6/(n + 1) < 0,1.
2. 6/(n + 1) < 0,1 ⟺ n + 1 > 60 ⟺ n ≥ 60.
3. Contrôle : pour n = 59, 6/60 = 0,1 n'est pas strictement inférieur à 0,1, la boucle continue ; pour n = 60, 6/61 ≈ 0,098 l'est.
4. L'algorithme affiche 60 : à partir du rang 60, tₙ est à moins de 0,1 ms de 2.

:::

::: piege
**Erreur : croire qu'une suite convergente atteint sa limite.** Pour tₙ, on cherche n avec tₙ = 2 et l'on déclare que la limite n'existe pas faute d'en trouver. L'erreur tente parce que « tendre vers 2 » ressemble à « devenir égal à 2 ». Mais la définition ne demande que |tₙ − 2| < ε, aussi petit que soit ε : la suite peut s'approcher sans jamais toucher.
:::

::: propriete
**Unicité** : si une suite est convergente, sa limite est unique.
**Limites usuelles** : si p est un entier strictement positif, lim 1/nᵖ = 0 et lim nᵖ = +∞.
**Suites géométriques** : lim qⁿ = +∞ si q > 1 ; lim qⁿ = 0 si −1 < q < 1 ; (qⁿ) n'a pas de limite si q < −1.
Cas limite : pour q = 1, qⁿ vaut toujours 1 et converge vers 1. Pour q = −1, les termes alternent entre 1 et −1 : pas de limite. Pour q = −3/2, les termes grandissent en changeant de signe : pas de limite non plus.
:::

::: verifie À toi : trois limites
Donner la limite de (1/2)ⁿ, de (5/4)ⁿ et de (−5/4)ⁿ.

---

−1 < 1/2 < 1, donc (1/2)ⁿ tend vers 0. Comme 5/4 > 1, (5/4)ⁿ tend vers +∞. Comme −5/4 < −1, (−5/4)ⁿ vaut 1 ; −1,25 ; 1,5625 ; −1,953125 ; … : les termes grandissent en changeant de signe, et la suite n'a pas de limite.
:::

::: retenir
lim uₙ = ℓ signifie que |uₙ − ℓ| devient plus petit que tout ε > 0 à partir d'un rang ; la limite est unique, et qⁿ tend vers 0 lorsque −1 < q < 1.
:::

## 🧮 Opérations sur les limites

Le fournisseur facture le serveur : le coût du jour n est cₙ = (3n² + 5n)/(n² + 1) dinars. Le numérateur et le dénominateur tendent tous deux vers +∞ : le quotient est de la forme « infini sur infini », et le calcul direct ne dit pas ce qu'il devient.
Comment obtenir la limite d'une somme, d'un produit ou d'un quotient, et que faire quand le tableau ne conclut pas ?

Les tableaux ci-dessous donnent la limite de uₙ + vₙ, de uₙ × vₙ et de uₙ/vₙ lorsque lim uₙ = a et lim vₙ = b, avec a et b réels, +∞ ou −∞. Le signe « ? » marque une case où l'on ne peut pas conclure.

| a \ b | b réel | +∞ | −∞ |
| --- | --- | --- | --- |
| a réel : limite de la somme | a + b | +∞ | −∞ |
| a = +∞ : limite de la somme | +∞ | +∞ | ? |
| a = −∞ : limite de la somme | −∞ | ? | −∞ |

| a \ b | b réel | +∞ | −∞ |
| --- | --- | --- | --- |
| a réel : limite du produit | ab | ±∞ si a ≠ 0 ; ? si a = 0 | ±∞ si a ≠ 0 ; ? si a = 0 |
| a = +∞ : limite du produit | ±∞ si b ≠ 0 ; ? si b = 0 | +∞ | −∞ |
| a = −∞ : limite du produit | ±∞ si b ≠ 0 ; ? si b = 0 | −∞ | +∞ |

| a \ b | b réel, b ≠ 0 | +∞ ou −∞ |
| --- | --- | --- |
| a réel : limite du quotient | a/b | 0 |
| a = +∞ ou −∞ : limite du quotient | ±∞ | ? |

Le signe ±∞ se détermine par la règle des signes. Les cas « ? » sont +∞ − ∞, 0 × ∞ et ∞/∞ ; le quotient 0/0 (b = 0, hors tableau) ne permet pas non plus de conclure.

::: exemple La limite du coût

1. cₙ = (3n² + 5n)/(n² + 1) est de la forme ∞/∞ : le tableau ne conclut pas.
2. On met n² en facteur au numérateur et au dénominateur : cₙ = n²(3 + 5/n)/(n²(1 + 1/n²)) = (3 + 5/n)/(1 + 1/n²), pour n ≥ 1.
3. Quand n → +∞, 5/n → 0 et 1/n² → 0 : le numérateur tend vers 3 et le dénominateur vers 1, un réel non nul.
4. lim cₙ = 3/1 = 3 dinars.

:::

::: exemple Une différence qui tend vers +∞

1. aₙ = 3n² − 5n + 2 est de la forme +∞ − ∞ : le tableau ne conclut pas.
2. On met n² en facteur : aₙ = n²(3 − 5/n + 2/n²), pour n ≥ 1.
3. La parenthèse tend vers 3 et n² vers +∞ : le produit de +∞ par un réel strictement positif vaut +∞.
4. lim aₙ = +∞.

:::

::: exemple Une différence de racines

1. bₙ = √(n² + 8n) − n est de la forme +∞ − ∞.
2. On multiplie et on divise par la quantité conjuguée √(n² + 8n) + n : bₙ = ((n² + 8n) − n²)/(√(n² + 8n) + n) = 8n/(√(n² + 8n) + n), car (A − B)(A + B) = A² − B².
3. Pour n ≥ 1, √(n² + 8n) = n√(1 + 8/n) : on divise numérateur et dénominateur par n, ce qui donne bₙ = 8/(√(1 + 8/n) + 1).
4. 8/n → 0, donc √(1 + 8/n) → 1 et lim bₙ = 8/(1 + 1) = 4.

:::

::: piege
**Erreur : écrire +∞ − ∞ = 0.** Pour (n² + n) − n², on écrit « +∞ − ∞ = 0 ». L'erreur tente parce que x − x = 0 pour tout réel x. Mais (n² + n) − n² = n tend vers +∞, et (n + 3) − n = 3 tend vers 3 : deux différences de la même forme, deux limites différentes. Une case « ? » du tableau n'a pas de valeur générale.
:::

::: propriete
Quand le tableau ne conclut pas, on transforme l'écriture de uₙ avant de passer à la limite.
**Fraction de polynômes** : on met en facteur la plus grande puissance de n au numérateur et au dénominateur, puis on simplifie.
**Différence de racines** : on multiplie et on divise par la quantité conjuguée.
**Suite géométrique dominante** : on met en facteur le plus grand qⁿ, par exemple (3ⁿ + 2ⁿ)/3ⁿ = 1 + (2/3)ⁿ.
Cas limite : l'écriture transformée n'est valable que pour n assez grand (n ≥ 1 ici) ; on le précise, car la limite ne dépend pas des premiers termes.
:::

::: verifie À toi : la quantité conjuguée
Calculer lim (√(n² + 3) − n).

---

C'est la forme +∞ − ∞. On multiplie par la quantité conjuguée √(n² + 3) + n : √(n² + 3) − n = ((n² + 3) − n²)/(√(n² + 3) + n) = 3/(√(n² + 3) + n). Le dénominateur tend vers +∞, donc le quotient d'un réel par une quantité qui tend vers +∞ tend vers 0 : la limite est 0.
:::

::: retenir
Une somme, un produit ou un quotient se traite avec les tableaux ; dans un cas « ? » (+∞ − ∞, 0 × ∞, ∞/∞, 0/0), on transforme l'expression par factorisation ou quantité conjuguée.
:::

## 🛡️ Comparaison et encadrement

La suite xₙ = (n + cos n)/(n + 1) mêle un terme qui grandit, n, et un terme qui oscille, cos n : on ne sait pas la calculer terme à terme. En revanche, on sait que cos n reste entre −1 et 1.
Peut-on conclure sur la limite de xₙ à partir d'une inégalité, sans connaître xₙ exactement ?

::: propriete
**Théorèmes de comparaison** (admis). Les inégalités sont vraies à partir d'un certain rang.
**Minoration** : si uₙ ≤ xₙ et lim uₙ = +∞, alors lim xₙ = +∞.
**Majoration** : si xₙ ≤ uₙ et lim uₙ = −∞, alors lim xₙ = −∞.
**Encadrement (gendarmes)** : si uₙ ≤ xₙ ≤ vₙ et si (uₙ) et (vₙ) convergent vers la même limite ℓ, alors (xₙ) converge vers ℓ.
**Distance** : si |xₙ − ℓ| ≤ uₙ et lim uₙ = 0, alors (xₙ) converge vers ℓ.
**Passage à la limite** : si xₙ ≤ yₙ, si lim xₙ = ℓ et lim yₙ = ℓ′, alors ℓ ≤ ℓ′.
:::

::: exemple Un encadrement

1. Pour tout n, −1 ≤ cos n ≤ 1, donc (n − 1)/(n + 1) ≤ xₙ ≤ (n + 1)/(n + 1) = 1, car n + 1 > 0.
2. (n − 1)/(n + 1) = 1 − 2/(n + 1) tend vers 1, et la suite constante 1 tend vers 1.
3. Les deux suites qui encadrent xₙ ont la même limite 1 : lim xₙ = 1.

:::

::: exemple Une minoration et une distance

1. Pour yₙ = n + 4 sin n : sin n ≥ −1, donc yₙ ≥ n − 4. Comme lim (n − 4) = +∞, lim yₙ = +∞.
2. Pour zₙ = 3 + (−1)ⁿ/(n + 1) : |zₙ − 3| = 1/(n + 1), qui tend vers 0. Donc lim zₙ = 3.

:::

::: piege
**Erreur : garder l'inégalité stricte à la limite.** Pour 0 < 1/n, on écrit « donc 0 < lim 1/n ». L'erreur tente parce que l'inégalité est vraie pour chaque n. Mais lim 1/n = 0, et 0 < 0 est faux : à la limite, une inégalité stricte devient large. On peut seulement écrire 0 ≤ lim 1/n.
:::

::: verifie À toi : un gendarme
Déterminer lim (2n + (−1)ⁿ)/n pour n ≥ 1.

---

Pour n ≥ 1, (2n − 1)/n ≤ (2n + (−1)ⁿ)/n ≤ (2n + 1)/n, soit 2 − 1/n ≤ (2n + (−1)ⁿ)/n ≤ 2 + 1/n. Les deux bornes tendent vers 2, donc la suite tend vers 2.
:::

::: retenir
Une inégalité permet de conclure sans calculer : minorer par une suite qui tend vers +∞, encadrer entre deux suites de même limite, ou majorer |xₙ − ℓ| par une suite qui tend vers 0 ; à la limite, une inégalité stricte devient large.
:::

## 🧱 Suites monotones bornées

Le temps tₙ décroît et reste au-dessus de 2 : il semble ne pouvoir que se stabiliser. Dans un autre test, un débit ne cesse de croître sans jamais dépasser la capacité du réseau. Peut-on affirmer que ce débit se stabilise, sans connaître sa formule ?
Que garantit un sens de variation joint à une borne ?

::: propriete
**Théorème (admis)** : toute suite croissante et majorée est convergente ; toute suite décroissante et minorée est convergente.
**Complément** : une suite croissante et non majorée tend vers +∞ ; une suite décroissante et non minorée tend vers −∞.
Cas limite : le théorème donne l'existence de la limite, pas sa valeur. uₙ = 4 − 1/(n + 1) est croissante, majorée par 5, et sa limite est 4, pas 5.
:::

::: exemple Une somme majorée

1. sₙ = 1 + 1/2² + 1/3² + … + 1/n² (n ≥ 1). Elle est croissante : sₙ₊₁ − sₙ = 1/(n + 1)² > 0.
2. Pour k ≥ 2, 1/k² ≤ 1/(k(k − 1)) = 1/(k − 1) − 1/k, car k² ≥ k(k − 1).
3. En sommant de k = 2 à n, les termes se simplifient deux à deux : 1/(1) − 1/n. Donc sₙ ≤ 1 + (1 − 1/n) = 2 − 1/n ≤ 2.
4. (sₙ) est croissante et majorée par 2 : elle converge, vers un réel inférieur ou égal à 2.

:::

::: exemple Une suite récurrente croissante et majorée

1. u₀ = 1 et uₙ₊₁ = √(4uₙ + 5). On montre d'abord par récurrence que 1 ≤ uₙ ≤ 5.
2. Initialisation : u₀ = 1 convient. Hérédité : si 1 ≤ uₙ ≤ 5, alors 9 ≤ 4uₙ + 5 ≤ 25, donc 3 ≤ uₙ₊₁ ≤ 5, et 3 ≥ 1.
3. uₙ₊₁² − uₙ² = 4uₙ + 5 − uₙ² = (5 − uₙ)(uₙ + 1) ≥ 0, donc uₙ₊₁ ≥ uₙ puisque les termes sont positifs.
4. (uₙ) est croissante et majorée par 5 : elle converge vers un réel ℓ. Sa valeur se calcule à la notion suivante.

:::

::: piege
**Erreur : croire que « le terme général tend vers 0 » suffit pour qu'une somme converge.** Pour Sₙ = 1 + 1/2 + 1/3 + … + 1/n, on remarque que 1/n → 0 et l'on en conclut que (Sₙ) converge. Mais S₂ₙ − Sₙ = 1/(n + 1) + … + 1/(2n) contient n termes qui valent chacun au moins 1/(2n), donc S₂ₙ − Sₙ ≥ 1/2. Si (Sₙ) convergeait, cette différence tendrait vers 0 : c'est impossible. (Sₙ), croissante, n'est donc pas majorée, et elle tend vers +∞.
:::

::: verifie À toi : croissante, non majorée
(uₙ) est croissante et n'est pas majorée. Que peut-on dire de sa limite ? Et si (vₙ) est seulement non majorée ?

---

Une suite croissante et non majorée tend vers +∞. Mais une suite non majorée n'a pas forcément pour limite +∞ : vₙ = (1 + (−1)ⁿ)n vaut 0 pour n impair et 2n pour n pair. Elle est non majorée (v₂ₖ = 4k), mais elle revient à 0 : elle ne tend pas vers +∞.
:::

::: retenir
Croissante et majorée, ou décroissante et minorée : la suite converge, vers une limite que le théorème ne donne pas ; croissante et non majorée : elle tend vers +∞.
:::

## 🔁 Suites et fonctions : f(n), f(uₙ) et point fixe

La limite de (uₙ) définie par u₀ = 1 et uₙ₊₁ = √(4uₙ + 5) existe, nous venons de le prouver. Mais quelle est-elle ? Un graphique aide à la lire : on place la courbe de f(x) = √(4x + 5) et la droite y = x.
Comment relier une suite à une fonction pour calculer une limite ?

::: figure L'escalier de la suite : de u₀ = 1, les termes montent vers l'abscisse 5 du point d'intersection de la courbe y = f(x) et de la droite y = x
<svg viewBox="0 0 340 260">
<title>Escalier de la suite uₙ₊₁ = √(4uₙ + 5) avec u₀ = 1 : les marches montent vers l'abscisse 5 du point d'intersection de la courbe et de la droite y = x</title>
<line x1="40" y1="220" x2="264.0" y2="220" stroke="#0f172a" stroke-width="1.6"/>
<line x1="40" y1="228" x2="40" y2="12" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="264.0,220 256.0,216 256.0,224" fill="#0f172a"/>
<polygon points="40,12 36,20 44,20" fill="#0f172a"/>
<line x1="40" y1="220" x2="248.0" y2="12.0" stroke="#94a3b8" stroke-width="1.8"/>
<polyline points="40.0,130.6 42.0,128.8 44.0,127.0 46.0,125.3 48.0,123.7 50.0,122.0 52.0,120.4 54.0,118.8 56.0,117.2 58.0,115.7 60.0,114.2 62.0,112.7 64.0,111.2 66.0,109.7 68.0,108.3 70.0,106.9 72.0,105.5 74.0,104.1 76.0,102.7 78.0,101.3 80.0,100.0 82.0,98.7 84.0,97.4 86.0,96.1 88.0,94.8 90.0,93.5 92.0,92.3 94.0,91.0 96.0,89.8 98.0,88.5 100.0,87.3 102.0,86.1 104.0,84.9 106.0,83.8 108.0,82.6 110.0,81.4 112.0,80.3 114.0,79.1 116.0,78.0 118.0,76.9 120.0,75.8 122.0,74.7 124.0,73.6 126.0,72.5 128.0,71.4 130.0,70.3 132.0,69.3 134.0,68.2 136.0,67.2 138.0,66.1 140.0,65.1 142.0,64.1 144.0,63.0 146.0,62.0 148.0,61.0 150.0,60.0 152.0,59.0 154.0,58.0 156.0,57.0 158.0,56.0 160.0,55.1 162.0,54.1 164.0,53.1 166.0,52.2 168.0,51.2 170.0,50.3 172.0,49.4 174.0,48.4 176.0,47.5 178.0,46.6 180.0,45.6 182.0,44.7 184.0,43.8 186.0,42.9 188.0,42.0 190.0,41.1 192.0,40.2 194.0,39.3 196.0,38.5 198.0,37.6 200.0,36.7 202.0,35.8 204.0,35.0 206.0,34.1 208.0,33.2 210.0,32.4 212.0,31.5 214.0,30.7 216.0,29.8 218.0,29.0 220.0,28.2 222.0,27.3 224.0,26.5 226.0,25.7 228.0,24.9 230.0,24.0 232.0,23.2 234.0,22.4 236.0,21.6 238.0,20.8 240.0,20.0 242.0,19.2 244.0,18.4 246.0,17.6 248.0,16.8" fill="none" stroke="#d97706" stroke-width="2.4"/>
<line x1="240" y1="20" x2="240" y2="220" stroke="#0f6e56" stroke-width="1.2" stroke-dasharray="4 3"/>
<line x1="240" y1="20" x2="40" y2="20" stroke="#0f6e56" stroke-width="1.2" stroke-dasharray="4 3"/>
<line x1="80.0" y1="220.0" x2="80.0" y2="100.0" stroke="#0f6e56" stroke-width="1.6"/>
<line x1="80.0" y1="100.0" x2="160.0" y2="100.0" stroke="#0f6e56" stroke-width="1.6"/>
<line x1="160.0" y1="100.0" x2="160.0" y2="55.1" stroke="#0f6e56" stroke-width="1.6"/>
<line x1="160.0" y1="55.1" x2="204.9" y2="55.1" stroke="#0f6e56" stroke-width="1.6"/>
<line x1="204.9" y1="55.1" x2="204.9" y2="34.6" stroke="#0f6e56" stroke-width="1.6"/>
<line x1="204.9" y1="34.6" x2="225.4" y2="34.6" stroke="#0f6e56" stroke-width="1.6"/>
<line x1="225.4" y1="34.6" x2="225.4" y2="25.9" stroke="#0f6e56" stroke-width="1.6"/>
<line x1="225.4" y1="25.9" x2="234.1" y2="25.9" stroke="#0f6e56" stroke-width="1.6"/>
<line x1="80.0" y1="217" x2="80.0" y2="223" stroke="#0f172a" stroke-width="1.2"/>
<line x1="160.0" y1="217" x2="160.0" y2="223" stroke="#0f172a" stroke-width="1.2"/>
<line x1="204.9" y1="217" x2="204.9" y2="223" stroke="#0f172a" stroke-width="1.2"/>
<line x1="225.4" y1="217" x2="225.4" y2="223" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="240" cy="20" r="4.2" fill="#0f6e56" stroke="#0f172a" stroke-width="1.2"/>
<text x="80.0" y="238" text-anchor="middle" fill="#0f172a" font-size="12" font-weight="700">u₀</text>
<text x="160.0" y="252" text-anchor="middle" fill="#0f172a" font-size="12" font-weight="700">u₁</text>
<text x="204.9" y="238" text-anchor="middle" fill="#0f172a" font-size="12" font-weight="700">u₂</text>
<text x="225.4" y="252" text-anchor="middle" fill="#0f172a" font-size="12" font-weight="700">u₃</text>
<text x="240" y="238" text-anchor="middle" fill="#0f6e56" font-size="12" font-weight="700">5</text>
<text x="32" y="24" text-anchor="end" fill="#0f6e56" font-size="12" font-weight="700">5</text>
<text x="260.0" y="212" text-anchor="middle" fill="#0f172a" font-size="12" font-weight="700">x</text>
<text x="50" y="20" text-anchor="start" fill="#0f172a" font-size="12" font-weight="700">y</text>
<text x="244.0" y="6.0" text-anchor="end" fill="#475569" font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">y = x</text>
<text x="160.0" y="45.1" text-anchor="middle" fill="#b45309" font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">y = f(x)</text>
</svg>
:::

Pour lire u₁ = f(u₀), on monte de u₀ jusqu'à la courbe ; on rabat cette hauteur sur l'axe par la droite y = x, ce qui place u₁ ; on recommence. Les marches se resserrent vers le point d'intersection des deux courbes.

::: propriete
**Suite du type uₙ = f(n)** : si lim f(x) = ℓ quand x → +∞ (ℓ fini ou infini), alors lim uₙ = ℓ.
**Image d'une suite** : si lim uₙ = a et lim f(x) = L quand x → a (a, L finis ou infinis), alors lim f(uₙ) = L.
**Continuité** : si lim uₙ = ℓ avec ℓ ∈ I et si f est continue en ℓ, alors (f(uₙ)) converge vers f(ℓ).
**Point fixe** : si uₙ₊₁ = f(uₙ) avec f(I) ⊂ I, si (uₙ) converge vers ℓ et si f est continue en ℓ, alors f(ℓ) = ℓ.
Cas limite : l'équation f(x) = x peut avoir plusieurs solutions. C'est l'encadrement de la suite qui désigne la bonne, et la convergence se démontre avant de résoudre l'équation.
:::

::: exemple Un point fixe

1. On a prouvé que (uₙ) converge vers un réel ℓ avec 1 ≤ uₙ ≤ 5 pour tout n, donc 1 ≤ ℓ ≤ 5.
2. uₙ₊₁ tend aussi vers ℓ, et f(x) = √(4x + 5) est continue sur [1 ; 5] : f(uₙ) tend vers f(ℓ). Donc ℓ = √(4ℓ + 5).
3. En élevant au carré, ℓ² − 4ℓ − 5 = 0, soit (ℓ − 5)(ℓ + 1) = 0 : ℓ = 5 ou ℓ = −1.
4. Comme ℓ ≥ 1, seule ℓ = 5 convient : l'abscisse du point d'intersection de la figure.

:::

::: exemple Les deux premiers théorèmes

1. Pour eₙ = (2n² − 1)/(n² + 3), on pose f(x) = (2x² − 1)/(x² + 3) : lim f(x) = 2 quand x → +∞, donc lim eₙ = 2.
2. Pour wₙ = cos(πn/(3n + 3)), on a uₙ = πn/(3n + 3) → π/3, et cos est continue en π/3 : lim wₙ = cos(π/3) = 1/2.

:::

::: piege
**Erreur : résoudre f(ℓ) = ℓ sans savoir que la suite converge.** Pour u₀ = 1 et uₙ₊₁ = 2uₙ, on écrit ℓ = 2ℓ, donc ℓ = 0, et l'on annonce lim uₙ = 0. L'erreur tente parce que l'équation a une solution. Mais uₙ = 2ⁿ tend vers +∞ : la suite ne converge pas, et l'équation ne dit rien.
:::

::: verifie À toi : un point fixe
(uₙ) est définie par u₀ = 1 et uₙ₊₁ = √(6uₙ + 16). On admet qu'elle est croissante et majorée par 8. Déterminer sa limite.

---

La suite converge vers un réel ℓ avec 1 ≤ ℓ ≤ 8. La fonction f(x) = √(6x + 16) est continue, donc ℓ = √(6ℓ + 16), d'où ℓ² − 6ℓ − 16 = 0, soit (ℓ − 8)(ℓ + 2) = 0. Comme ℓ ≥ 1, ℓ = 8.
:::

::: retenir
Si (uₙ) converge et si f est continue en sa limite, alors ℓ vérifie f(ℓ) = ℓ : on résout cette équation, puis on garde la solution compatible avec l'encadrement de la suite.
:::

## 🧩 Suite auxiliaire : se ramener à une suite connue

Une suite comme u₀ = 9, uₙ₊₁ = −uₙ/2 + 3 ne se calcule que terme après terme. On voudrait une formule pour u₁₀₀ sans faire cent étapes. L'idée : fabriquer à partir de (uₙ) une suite auxiliaire qui, elle, est arithmétique ou géométrique.
Comment trouver la bonne suite auxiliaire, et que faire d'une récurrence à deux pas ?

::: exemple Récurrence affine : une suite géométrique

1. u₀ = 9 et uₙ₊₁ = −uₙ/2 + 3. Le point fixe de x ↦ −x/2 + 3 est ℓ = 2, solution de ℓ = −ℓ/2 + 3.
2. On pose vₙ = uₙ − 2. Alors vₙ₊₁ = uₙ₊₁ − 2 = −uₙ/2 + 1 = −(uₙ − 2)/2 = −vₙ/2.
3. (vₙ) est géométrique de raison −1/2 et de premier terme v₀ = 7 : vₙ = 7(−1/2)ⁿ, donc uₙ = 2 + 7(−1/2)ⁿ.
4. Comme −1 < −1/2 < 1, lim vₙ = 0 et lim uₙ = 2. La suite oscille autour de 2 : 9 ; −1,5 ; 3,75 ; 1,125 ; … (elle n'est pas monotone). Sur le graphique de x ↦ −x/2 + 3, les marches s'enroulent autour du point d'intersection avec y = x (représentation en « escargot »), parce que la pente −1/2 est négative.

:::

::: exemple Récurrence homographique : une suite arithmétique

1. u₀ = 1 et uₙ₊₁ = 2uₙ/(uₙ + 2). Par récurrence, uₙ > 0 pour tout n : si uₙ > 0, alors 2uₙ > 0 et uₙ + 2 > 0.
2. On pose vₙ = 1/uₙ, bien défini. vₙ₊₁ = (uₙ + 2)/(2uₙ) = 1/2 + 1/uₙ = vₙ + 1/2.
3. (vₙ) est arithmétique de raison 1/2 et de premier terme v₀ = 1 : vₙ = 1 + n/2 = (n + 2)/2, donc uₙ = 2/(n + 2).
4. Ainsi lim uₙ = 0, et (uₙ) est décroissante (u₁ = 2/3, u₂ = 1/2, …).

:::

::: exemple Récurrence à deux pas

1. u₀ = 0, u₁ = 5 et uₙ₊₂ = 7uₙ₊₁ − 6uₙ. On résout x² = 7x − 6, soit (x − 1)(x − 6) = 0 : les racines sont 1 et 6.
2. Les racines 1 et 6 donnent les suites 1ⁿ = 1 et 6ⁿ, qui vérifient la relation ; on les combine en cherchant uₙ = α × 6ⁿ + β. Avec u₀ = 0 : α + β = 0. Avec u₁ = 5 : 6α + β = 5. Donc 5α = 5, α = 1 et β = −1.
3. La suite wₙ = 6ⁿ − 1 vérifie w₀ = 0, w₁ = 5 et la même relation, car 7(6ⁿ⁺¹ − 1) − 6(6ⁿ − 1) = 6ⁿ⁺¹(7 − 1) − 1 = 6ⁿ⁺² − 1. Une suite est déterminée par ses deux premiers termes et sa relation : uₙ = 6ⁿ − 1.
4. Contrôle : u₂ = 7 × 5 − 0 = 35 = 6² − 1.

:::

::: piege
**Erreur : prendre la limite de la suite auxiliaire pour celle de la suite de départ.** Avec vₙ = uₙ − 2, on trouve lim vₙ = 0 et l'on écrit lim uₙ = 0. L'erreur tente parce que la suite auxiliaire est celle que l'on sait étudier. Mais uₙ = vₙ + 2 : la limite de uₙ est 0 + 2 = 2.
:::

::: propriete
**Récurrence affine uₙ₊₁ = a uₙ + b** (a ≠ 1) : avec ℓ = b/(1 − a), la suite vₙ = uₙ − ℓ est géométrique de raison a, donc uₙ = ℓ + (u₀ − ℓ)aⁿ.
**Récurrence homographique** : si uₙ ≠ 0 pour tout n et que 1/uₙ₊₁ s'écrit en fonction de 1/uₙ, on pose vₙ = 1/uₙ.
**Somme géométrique** : pour q ≠ 1, v₀ + v₁ + … + vₙ = v₀(1 − qⁿ⁺¹)/(1 − q), qui compte n + 1 termes. Pour une suite arithmétique, la somme de n + 1 termes vaut (n + 1)(v₀ + vₙ)/2.
Cas limite : pour a = 1, uₙ₊₁ = uₙ + b est déjà arithmétique de raison b, et ℓ = b/(1 − a) n'existe pas.
:::

::: verifie À toi : le bon changement de suite
(uₙ) est définie par u₀ = 5 et uₙ₊₁ = (2/3)uₙ + 2. Exprimer uₙ en fonction de n et donner sa limite.

---

Le point fixe est ℓ = 2/(1 − 2/3) = 6. La suite vₙ = uₙ − 6 vérifie vₙ₊₁ = (2/3)uₙ + 2 − 6 = (2/3)(uₙ − 6) = (2/3)vₙ : elle est géométrique de raison 2/3, avec v₀ = −1. Donc uₙ = 6 − (2/3)ⁿ, et comme (2/3)ⁿ → 0, lim uₙ = 6.
:::

::: retenir
On ramène une récurrence à une suite connue : vₙ = uₙ − ℓ pour uₙ₊₁ = a uₙ + b, vₙ = 1/uₙ pour une récurrence homographique ; la limite de uₙ se déduit de celle de vₙ, elle ne lui est pas égale.
:::
