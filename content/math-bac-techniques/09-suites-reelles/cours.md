# ⚔️ Suites réelles — suivre un nombre qui avance pas à pas

> 💡 «Une suite est une file de nombres : on la comprend en regardant où elle monte, où elle reste et où elle finit.»

Le calcul intégral mesurait des surfaces ; ici, les nombres arrivent un par un : u₀, u₁, u₂, … Huit notions, avec deux fils rouges. Le premier est un atelier dont la cadence monte semaine après semaine, pₙ = 100n/(n + 3) pièces par heure à la semaine n. Le second est un bassin qui reçoit chaque jour 2 m³ d'eau et en perd un cinquième : u₀ = 4 et uₙ₊₁ = (4/5)uₙ + 2, en m³. On suppose acquis le raisonnement par récurrence, les suites arithmétiques et géométriques et les limites de fonctions en +∞.

## 📈 Sens de variation d'une suite

Un atelier monte en cadence. À la semaine n (n = 0, 1, 2, …), il produit pₙ = 100n/(n + 3) pièces par heure : 0 ; 25 ; 40 ; 50 ; puis environ 57,1. Les premières valeurs montent, mais rien ne garantit qu'elles montent encore à la semaine 100.
Comment démontrer un sens de variation pour tous les entiers n, et pas seulement sur les premiers termes ?

::: figure Les points (n ; pₙ) de la production montent d'un rang au suivant : de p₂ = 40 à p₃ = 50, la hausse est de 10
<svg viewBox="0 0 340 236">
<title>Les points (n ; pₙ) de la production pₙ = 100n/(n + 3) pour n de 0 à 8 : ils montent d'un rang au suivant</title>
<line x1="44" y1="206" x2="326" y2="206" stroke="#0f172a" stroke-width="1.6"/>
<line x1="44" y1="214" x2="44" y2="12" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="326,206 318,202 318,210" fill="#0f172a"/>
<polygon points="44,12 40,20 48,20" fill="#0f172a"/>
<line x1="44" y1="203" x2="44" y2="209" stroke="#0f172a" stroke-width="1.2"/>
<line x1="77" y1="203" x2="77" y2="209" stroke="#0f172a" stroke-width="1.2"/>
<line x1="110" y1="203" x2="110" y2="209" stroke="#0f172a" stroke-width="1.2"/>
<line x1="143" y1="203" x2="143" y2="209" stroke="#0f172a" stroke-width="1.2"/>
<line x1="176" y1="203" x2="176" y2="209" stroke="#0f172a" stroke-width="1.2"/>
<line x1="209" y1="203" x2="209" y2="209" stroke="#0f172a" stroke-width="1.2"/>
<line x1="242" y1="203" x2="242" y2="209" stroke="#0f172a" stroke-width="1.2"/>
<line x1="275" y1="203" x2="275" y2="209" stroke="#0f172a" stroke-width="1.2"/>
<line x1="308" y1="203" x2="308" y2="209" stroke="#0f172a" stroke-width="1.2"/>
<line x1="41" y1="156" x2="47" y2="156" stroke="#0f172a" stroke-width="1.2"/>
<line x1="44" y1="156" x2="316" y2="156" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3 4"/>
<line x1="41" y1="106" x2="47" y2="106" stroke="#0f172a" stroke-width="1.2"/>
<line x1="44" y1="106" x2="316" y2="106" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3 4"/>
<line x1="41" y1="56" x2="47" y2="56" stroke="#0f172a" stroke-width="1.2"/>
<line x1="44" y1="56" x2="316" y2="56" stroke="#94a3b8" stroke-width="1" stroke-dasharray="3 4"/>
<circle cx="44" cy="206" r="3.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="77" cy="156" r="3.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="110" cy="126" r="3.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="143" cy="106" r="3.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="176" cy="91.71" r="3.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="209" cy="81" r="3.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="242" cy="72.67" r="3.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="275" cy="66" r="3.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="308" cy="60.55" r="3.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<line x1="110" y1="126" x2="143" y2="126" stroke="#0f6e56" stroke-width="1.6" stroke-dasharray="4 3"/>
<line x1="143" y1="126" x2="143" y2="106" stroke="#0f6e56" stroke-width="1.6" stroke-dasharray="4 3"/>
<g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="318" y="198" text-anchor="middle" fill="#0f172a" font-size="12">n</text><text x="56" y="22" text-anchor="start" fill="#0f172a" font-size="12">pₙ</text><text x="44" y="222" text-anchor="middle" fill="#0f172a" font-size="11">0</text><text x="77" y="222" text-anchor="middle" fill="#0f172a" font-size="11">1</text><text x="110" y="222" text-anchor="middle" fill="#0f172a" font-size="11">2</text><text x="143" y="222" text-anchor="middle" fill="#0f172a" font-size="11">3</text><text x="176" y="222" text-anchor="middle" fill="#0f172a" font-size="11">4</text><text x="209" y="222" text-anchor="middle" fill="#0f172a" font-size="11">5</text><text x="242" y="222" text-anchor="middle" fill="#0f172a" font-size="11">6</text><text x="275" y="222" text-anchor="middle" fill="#0f172a" font-size="11">7</text><text x="308" y="222" text-anchor="middle" fill="#0f172a" font-size="11">8</text><text x="37" y="160" text-anchor="end" fill="#0f172a" font-size="11">25</text><text x="37" y="110" text-anchor="end" fill="#0f172a" font-size="11">50</text><text x="37" y="60" text-anchor="end" fill="#0f172a" font-size="11">75</text><text x="149" y="120" text-anchor="start" fill="#0f6e56" font-size="11">+10</text></g>
</svg>
:::

Un point plus haut que le précédent se lit pₙ₊₁ > pₙ : c'est ce que la définition suivante exige pour tout n.

::: definition
Soit (uₙ) une suite définie pour tout entier n ≥ n₀.
**Croissante** : uₙ₊₁ ≥ uₙ pour tout n ≥ n₀ ; **strictement croissante** si uₙ₊₁ > uₙ.
**Décroissante** : uₙ₊₁ ≤ uₙ pour tout n ≥ n₀ ; **strictement décroissante** si uₙ₊₁ < uₙ.
**Constante** : uₙ₊₁ = uₙ pour tout n ≥ n₀. **Monotone** : croissante ou décroissante.
**Stationnaire** : il existe un entier p ≥ n₀ tel que uₙ₊₁ = uₙ pour tout n ≥ p.
:::

::: exemple La cadence de l'atelier

1. pₙ₊₁ − pₙ = 100(n + 1)/(n + 4) − 100n/(n + 3). On met au même dénominateur (n + 3)(n + 4) pour comparer.
2. Le numérateur est 100[(n + 1)(n + 3) − n(n + 4)] = 100[(n² + 4n + 3) − (n² + 4n)] = 300, car les termes en n² et en n se détruisent.
3. Donc pₙ₊₁ − pₙ = 300/((n + 3)(n + 4)), strictement positif pour tout n ∈ ℕ puisque n + 3 et n + 4 sont positifs.
4. (pₙ) est strictement croissante sur ℕ. La hausse de p₂ à p₃ vaut 300/(5 × 6) = 10, comme sur la figure.

:::

::: exemple Comparer le rapport à 1

1. tₙ = n/2ⁿ pour n ≥ 1 a des termes strictement positifs : on peut comparer tₙ₊₁/tₙ à 1 au lieu d'étudier une différence.
2. tₙ₊₁/tₙ = ((n + 1)/2^{n+1}) × (2ⁿ/n) = (n + 1)/(2n), car 2^{n+1} = 2 × 2ⁿ.
3. (n + 1)/(2n) ≤ 1 ⟺ n + 1 ≤ 2n ⟺ n ≥ 1 : le rapport est inférieur ou égal à 1 pour tout n ≥ 1.
4. (tₙ) est décroissante sur {n ≥ 1}, sans être strictement décroissante : le rapport vaut 1 pour n = 1, et t₁ = t₂ = 1/2.

:::

::: piege
**Erreur : conclure sur les premiers termes.** Pour aₙ = n²/2ⁿ, on calcule a₀ = 0, a₁ = 1/2, a₂ = 1, a₃ = 9/8 et l'on écrit « (aₙ) est croissante ». L'erreur tente parce que quatre termes qui montent ressemblent à une règle. Mais a₄ = 16/16 = 1 < a₃ : la différence aₙ₊₁ − aₙ = (−n² + 2n + 1)/2^{n+1} change de signe, et la suite descend à partir de n = 3.
:::

::: propriete
Pour étudier le sens de variation de (uₙ), on dispose de quatre techniques.
**Différence** : on étudie le signe de uₙ₊₁ − uₙ.
**Rapport** : si tous les termes sont strictement positifs, uₙ₊₁/uₙ ≥ 1 donne une suite croissante et uₙ₊₁/uₙ ≤ 1 une suite décroissante.
**Récurrence** : on démontre par récurrence uₙ ≤ uₙ₊₁ pour tout n (ou uₙ ≥ uₙ₊₁) ; pour uₙ₊₁ = f(uₙ) avec f croissante, l'hérédité vient de ce que uₙ ≤ uₙ₊₁ entraîne f(uₙ) ≤ f(uₙ₊₁).
**Fonction** : si uₙ = f(n) et si f est monotone sur [n₀ ; +∞[, alors (uₙ) a le même sens de variation sur {n ≥ n₀}.
Cas limite : la réciproque de la technique « fonction » est fausse. La suite uₙ = n est croissante, alors que f(x) = x + sin(2πx), qui vaut n en x = n, n'est pas croissante : f′(1/2) = 1 − 2π < 0.
:::

::: verifie À toi : un sens de variation à partir d'un rang
Étudier le sens de variation de uₙ = n² − 4n sur ℕ.

---

uₙ₊₁ − uₙ = (n + 1)² − 4(n + 1) − n² + 4n = 2n − 3. Cette différence est négative pour n ≤ 1 et positive pour n ≥ 2 : u₀ ≥ u₁ ≥ u₂ (0, −3, −4), puis (uₙ) est strictement croissante à partir de n = 2 (−4, −3, 0). Elle n'est pas monotone sur ℕ. On retrouve le rang 2 avec la technique « fonction » : f(x) = x² − 4x a son minimum en x = 2.
:::

::: retenir
Un sens de variation se prouve pour tous les n, par le signe de uₙ₊₁ − uₙ ou par le rapport à 1 pour des termes strictement positifs, et non sur les premiers termes seulement.
:::

## 🔒 Suite majorée, minorée, bornée

La machine de l'atelier ne peut pas dépasser 100 pièces par heure. On voudrait prouver que, pour tous les n, la cadence pₙ ne franchit jamais ce plafond, et qu'elle ne passe pas sous 0.
Comment montrer qu'un seuil n'est dépassé par aucun terme d'une suite ?

::: figure Tous les points (n ; pₙ) restent dans la bande 0 ≤ y ≤ 100 : la suite est minorée par m = 0 et majorée par M = 100
<svg viewBox="0 0 340 236">
<title>Les points (n ; pₙ) restent dans la bande 0 ≤ y ≤ 100 : la suite est minorée par m = 0 et majorée par M = 100</title>
<rect x="44" y="26" width="291.6" height="180" fill="#0f6e56" fill-opacity="0.10"/>
<line x1="44" y1="206" x2="326" y2="206" stroke="#0f172a" stroke-width="1.6"/>
<line x1="44" y1="214" x2="44" y2="12" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="326,206 318,202 318,210" fill="#0f172a"/>
<polygon points="44,12 40,20 48,20" fill="#0f172a"/>
<line x1="44" y1="26" x2="335.6" y2="26" stroke="#0f6e56" stroke-width="1.6" stroke-dasharray="6 3"/>
<line x1="44" y1="203" x2="44" y2="209" stroke="#0f172a" stroke-width="1.2"/>
<line x1="71" y1="203" x2="71" y2="209" stroke="#0f172a" stroke-width="1.2"/>
<line x1="98" y1="203" x2="98" y2="209" stroke="#0f172a" stroke-width="1.2"/>
<line x1="125" y1="203" x2="125" y2="209" stroke="#0f172a" stroke-width="1.2"/>
<line x1="152" y1="203" x2="152" y2="209" stroke="#0f172a" stroke-width="1.2"/>
<line x1="179" y1="203" x2="179" y2="209" stroke="#0f172a" stroke-width="1.2"/>
<line x1="206" y1="203" x2="206" y2="209" stroke="#0f172a" stroke-width="1.2"/>
<line x1="233" y1="203" x2="233" y2="209" stroke="#0f172a" stroke-width="1.2"/>
<line x1="260" y1="203" x2="260" y2="209" stroke="#0f172a" stroke-width="1.2"/>
<line x1="287" y1="203" x2="287" y2="209" stroke="#0f172a" stroke-width="1.2"/>
<line x1="314" y1="203" x2="314" y2="209" stroke="#0f172a" stroke-width="1.2"/>
<line x1="41" y1="116" x2="47" y2="116" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="44" cy="206" r="3.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="71" cy="161" r="3.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="98" cy="134" r="3.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="125" cy="116" r="3.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="152" cy="103.14" r="3.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="179" cy="93.5" r="3.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="206" cy="86" r="3.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="233" cy="80" r="3.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="260" cy="75.09" r="3.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="287" cy="71" r="3.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="314" cy="67.54" r="3.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="318" y="198" text-anchor="middle" fill="#0f172a" font-size="12">n</text><text x="56" y="22" text-anchor="start" fill="#0f172a" font-size="12">pₙ</text><text x="331.6" y="20" text-anchor="end" fill="#0f6e56" font-size="12">M = 100</text><text x="260" y="198" text-anchor="middle" fill="#0f6e56" font-size="12">m = 0</text><text x="44" y="222" text-anchor="middle" fill="#0f172a" font-size="11">0</text><text x="71" y="222" text-anchor="middle" fill="#0f172a" font-size="11">1</text><text x="98" y="222" text-anchor="middle" fill="#0f172a" font-size="11">2</text><text x="125" y="222" text-anchor="middle" fill="#0f172a" font-size="11">3</text><text x="152" y="222" text-anchor="middle" fill="#0f172a" font-size="11">4</text><text x="179" y="222" text-anchor="middle" fill="#0f172a" font-size="11">5</text><text x="206" y="222" text-anchor="middle" fill="#0f172a" font-size="11">6</text><text x="233" y="222" text-anchor="middle" fill="#0f172a" font-size="11">7</text><text x="260" y="222" text-anchor="middle" fill="#0f172a" font-size="11">8</text><text x="287" y="222" text-anchor="middle" fill="#0f172a" font-size="11">9</text><text x="314" y="222" text-anchor="middle" fill="#0f172a" font-size="11">10</text><text x="37" y="120" text-anchor="end" fill="#0f172a" font-size="11">50</text></g>
</svg>
:::

Les droites y = 0 et y = 100 de la figure sont le m et le M de la définition : aucun point ne passe au-dessus de la seconde ni sous la première.

::: definition
Soit (uₙ) une suite définie pour tout entier n ≥ n₀.
**Majorée** : il existe un réel M tel que uₙ ≤ M pour tout n ≥ n₀ ; M est un majorant.
**Minorée** : il existe un réel m tel que uₙ ≥ m pour tout n ≥ n₀ ; m est un minorant.
**Bornée** : à la fois majorée et minorée, soit m ≤ uₙ ≤ M pour tout n ≥ n₀.
Un majorant n'est pas unique : tout réel supérieur à M est encore un majorant.
:::

::: exemple La production est bornée

1. pₙ = 100n/(n + 3) = 100 − 300/(n + 3), car 100(n + 3) − 300 = 100n.
2. Pour tout n ∈ ℕ, 300/(n + 3) > 0, donc pₙ < 100 : (pₙ) est majorée par 100.
3. Pour n ≥ 0, 100n ≥ 0 et n + 3 > 0, donc pₙ ≥ 0 : (pₙ) est minorée par 0.
4. Ainsi 0 ≤ pₙ ≤ 100 pour tout n : (pₙ) est bornée, comme le montre la bande de la figure.

:::

::: exemple Une suite qui alterne

1. vₙ = (−1)ⁿ × 2n/(n + 1) vaut 0 ; −1 ; 4/3 ; −3/2 ; … : le signe alterne, donc (vₙ) n'est pas monotone.
2. |vₙ| = 2n/(n + 1) < 2, car 2n < 2n + 2.
3. Donc −2 < vₙ < 2 pour tout n : (vₙ) est bornée, bien que non monotone.

:::

::: piege
**Erreur : croire qu'une suite croissante est bornée.** (pₙ) est croissante et bornée, et l'on en conclut que toute suite croissante l'est. L'erreur tente parce que la production monte sans dépasser 100. Mais uₙ = n² est croissante et minorée par 0 sans être majorée : pour tout réel M, n² ≥ n > M dès que l'entier n dépasse M et 1.
:::

::: propriete
**Premier terme** : une suite croissante est minorée par son premier terme, une suite décroissante est majorée par son premier terme.
**Valeur absolue** (théorème admis) : (uₙ) est bornée si et seulement s'il existe un réel M tel que |uₙ| ≤ M pour tout n.
Cas limite : être majorée par M ne veut pas dire atteindre M. (pₙ) est majorée par 100 sans jamais valoir 100, puisque pₙ < 100 pour tout n.
:::

::: verifie À toi : borner une fraction
Montrer que uₙ = (6n + 1)/(2n + 3) est bornée sur ℕ.

---

On écrit 3 − uₙ = (6n + 9 − 6n − 1)/(2n + 3) = 8/(2n + 3) > 0, donc uₙ < 3. Pour n ∈ ℕ, 6n + 1 > 0 et 2n + 3 > 0, donc uₙ > 0. Ainsi 0 < uₙ < 3 pour tout n : (uₙ) est bornée.
:::

::: retenir
Une suite est majorée, minorée ou bornée lorsqu'un réel fixe limite tous ses termes ; on le prouve par une inégalité vraie pour tout n.
:::

## 🧭 Limite d'une suite

À la semaine 1000, la cadence est p₁₀₀₀ = 100 000/1003 ≈ 99,70 pièces par heure. La production semble se rapprocher de 100 sans jamais l'atteindre.
Comment dire précisément vers quoi va une suite, et comment calculer cette limite sans calculer des milliers de termes ?

| n | 10 | 100 | 1000 | 10000 |
| --- | --- | --- | --- | --- |
| pₙ | 76,92 | 97,09 | 99,70 | 99,97 |

La ligne pₙ du tableau s'approche de 100 quand n grandit : c'est ce que note lim n→+∞ pₙ = 100.

::: definition
Une suite est une fonction de l'entier n : on regarde ses termes quand n devient très grand, comme une fonction en +∞. Dire que lim n→+∞ uₙ = ℓ, c'est dire que uₙ est aussi proche qu'on veut de ℓ dès que n est assez grand.
**Convergente** : il existe un réel ℓ tel que lim n→+∞ uₙ = ℓ ; on dit que (uₙ) converge vers ℓ.
**Divergente** : lim uₙ = +∞, ou lim uₙ = −∞, ou (uₙ) n'a pas de limite.
:::

::: exemple La limite de la cadence

1. pₙ = f(n) avec f(x) = 100x/(x + 3), définie sur [0 ; +∞[.
2. En +∞, 100x/(x + 3) a la même limite que 100x/x = 100, quotient des termes de plus haut degré : lim x→+∞ f(x) = 100.
3. Donc lim n→+∞ pₙ = 100 : la production converge vers 100 pièces par heure, comme dans le tableau.
4. Elle n'atteint jamais 100 : 100 − pₙ = 300/(n + 3) > 0.

:::

::: exemple Quatre suites géométriques

1. (4/5)ⁿ vaut 1 ; 0,8 ; 0,64 ; 0,512 ; … Comme −1 < 4/5 < 1, lim (4/5)ⁿ = 0.
2. (6/5)ⁿ : 6/5 > 1, donc lim (6/5)ⁿ = +∞.
3. (−1/2)ⁿ : −1 < −1/2 < 1, donc lim (−1/2)ⁿ = 0, avec des termes de signes alternés.
4. (−6/5)ⁿ vaut 1 ; −1,2 ; 1,44 ; −1,728 ; … : −6/5 < −1, les termes grandissent en changeant de signe et la suite n'a pas de limite.

:::

::: piege
**Erreur : croire qu'une suite bornée converge.** (−1)ⁿ vaut 1, −1, 1, −1, … : elle est bornée par 1, et l'on écrit qu'elle converge. L'erreur tente parce que toute suite convergente est bornée. La réciproque est fausse : si (−1)ⁿ tendait vers ℓ, comme uₙ₊₁ = −uₙ a la même limite que uₙ, on aurait ℓ = −ℓ, donc ℓ = 0 ; or tous les termes sont à distance 1 de 0, ce qui est impossible.
:::

::: propriete
**Fonction** : soit f définie sur [a ; +∞[ et uₙ = f(n). Si lim x→+∞ f(x) vaut ℓ, +∞ ou −∞, alors lim n→+∞ uₙ a la même valeur.
**Limites de référence** : lim n² = +∞, lim √n = +∞, lim 1/n = 0, lim 1/n² = 0, lim (ln n)/n = 0, lim eⁿ/n = +∞.
**Suites géométriques qⁿ** : q > 1 donne +∞ ; −1 < q < 1 donne 0 ; q = 1 donne la suite constante 1 ; q ≤ −1 donne une suite sans limite. Pour u₀qⁿ avec q > 1, la limite est +∞ si u₀ > 0 et −∞ si u₀ < 0.
**Propriétés** : si (uₙ) converge, sa limite est unique, lim uₙ₊₁ = lim uₙ, et (uₙ) est bornée.
Cas limite : pour q = −1, les termes alternent entre 1 et −1 sans limite, alors que −1 < q < 1 donne 0.
:::

::: verifie À toi : deux limites
Déterminer lim n→+∞ (5n − 2)/(2n + 1), puis lim n→+∞ (−3/4)ⁿ.

---

uₙ = f(n) avec f(x) = (5x − 2)/(2x + 1), dont la limite en +∞ est celle de 5x/(2x) = 5/2 : la première limite vaut 5/2. Pour la seconde, −1 < −3/4 < 1, donc (−3/4)ⁿ tend vers 0.
:::

::: retenir
Une suite converge vers ℓ si ses termes s'approchent de ℓ quand n grandit ; on la calcule comme une limite de fonction en +∞, et qⁿ tend vers 0 lorsque −1 < q < 1.
:::

## 🧮 Opérations sur les limites et formes indéterminées

À la semaine n, l'atelier encaisse une recette Rₙ = 6n² + 5n et supporte des frais Cₙ = 2n² + 7. Le rapport mₙ = Rₙ/Cₙ mesure la marge. Les deux termes tendent vers +∞ : le quotient est de la forme +∞/+∞, et le calcul direct ne dit pas ce qu'il devient.
Que fait mₙ quand n grandit, et comment lever une telle indétermination ?

| n | 10 | 100 | 1000 |
| --- | --- | --- | --- |
| mₙ | 3,140 | 3,024 | 3,002 |

Le tableau suggère mₙ → 3 ; il reste à le démontrer.

::: exemple La marge de l'atelier

1. Rₙ → +∞ et Cₙ → +∞ : la forme +∞/+∞ ne permet pas de conclure directement.
2. On met n² en facteur au numérateur et au dénominateur : mₙ = n²(6 + 5/n)/(n²(2 + 7/n²)) = (6 + 5/n)/(2 + 7/n²), pour n ≥ 1.
3. Quand n → +∞, 5/n → 0 et 7/n² → 0 : le numérateur tend vers 6 et le dénominateur vers 2, deux réels avec un dénominateur non nul.
4. lim mₙ = 6/2 = 3, comme le suggère le tableau.

:::

::: exemple Une différence de racines

1. aₙ = √(n² + 4) − n : √(n² + 4) → +∞ et n → +∞, c'est la forme +∞ − ∞.
2. On multiplie et on divise par la quantité conjuguée √(n² + 4) + n : aₙ = ((n² + 4) − n²)/(√(n² + 4) + n) = 4/(√(n² + 4) + n), car (A − B)(A + B) = A² − B².
3. Le dénominateur tend vers +∞, donc aₙ → 0.

:::

::: exemple Un produit n × (quantité qui tend vers 0)

1. bₙ = n sin(2/n) est de la forme +∞ × 0. On pose Xₙ = 2/n : Xₙ → 0 et n = 2/Xₙ, donc bₙ = 2 sin(Xₙ)/Xₙ.
2. La fonction X ↦ sin X/X se prolonge en 0 par la valeur 1 (chapitre 1) : le prolongement est continu en 0, donc sin(Xₙ)/Xₙ → 1.
3. lim bₙ = 2 × 1 = 2.

:::

::: piege
**Erreur : écrire +∞ − ∞ = 0.** Pour (n² + n) − n², on écrit +∞ − ∞ = 0. L'erreur tente parce que x − x = 0 pour tout réel x. Mais (n² + n) − n² = n tend vers +∞, et (n + 3) − n = 3 tend vers 3 : deux différences de même forme, deux limites différentes, donc la forme n'a pas de valeur propre.
:::

::: propriete
**Opérations** : si uₙ → a et vₙ → b, réels, alors uₙ + vₙ → a + b, uₙvₙ → ab, et uₙ/vₙ → a/b si b ≠ 0. Avec ±∞, les règles sont celles des limites de fonctions : (+∞) + a = +∞, (+∞) × (+∞) = +∞, a/(±∞) = 0.
**Formes indéterminées** : +∞ − ∞, 0 × ∞, ∞/∞ et 0/0 n'ont pas de valeur générale.
**Composition** : si uₙ → ℓ et f est continue en ℓ, alors f(uₙ) → f(ℓ) ; si uₙ → +∞ et f(x) → L quand x → +∞, alors f(uₙ) → L.
Cas limite : un quotient 1/vₙ avec vₙ → 0 exige le signe de vₙ : il tend vers +∞ si vₙ → 0⁺ et vers −∞ si vₙ → 0⁻.
:::

::: methode Lever une forme indéterminée

1. Fraction de polynômes ou de racines : on met en facteur le terme dominant au numérateur et au dénominateur, puis on simplifie.
2. Différence de racines : on multiplie par la quantité conjuguée.
3. Produit n × (petite quantité) : on pose X égal à la petite quantité et l'on utilise les limites usuelles en 0, comme lim sin(aX)/X = a et lim (1 − cos X)/X² = 1/2.

:::

::: verifie À toi : la quantité conjuguée
Calculer lim n→+∞ (√(n + 5) − √n).

---

C'est la forme +∞ − ∞ : on multiplie par la quantité conjuguée √(n + 5) + √n. Alors √(n + 5) − √n = ((n + 5) − n)/(√(n + 5) + √n) = 5/(√(n + 5) + √n), dont le dénominateur tend vers +∞ : la limite est 0.
:::

::: retenir
Une forme indéterminée se lève en transformant l'expression : terme dominant, quantité conjuguée ou changement de variable ; +∞ − ∞ n'est pas égal à 0 d'office.
:::

## 🧱 Suites monotones bornées : la convergence garantie

Un bassin contient 4 m³ d'eau au jour 0. Chaque jour, un cinquième du volume s'écoule et l'on verse 2 m³ : uₙ₊₁ = (4/5)uₙ + 2. Il n'y a pas de formule pour uₙ, seulement un moyen de passer d'un jour au suivant.
Le volume va-t-il se stabiliser ou grimper sans fin, et peut-on le savoir sans calculer tous les termes ?

| n | 0 | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- | --- |
| uₙ | 4 | 5,2 | 6,16 | 6,928 | 7,5424 |

Les termes du tableau montent et semblent rester sous un plafond : « monotone » et « borné » sont les deux propriétés à démontrer pour tout n.

::: exemple Le bassin ne dépasse pas 10 m³

1. On montre par récurrence P(n) : 4 ≤ uₙ ≤ 10. Initialisation : u₀ = 4 vérifie 4 ≤ 4 ≤ 10.
2. Hérédité : on suppose 4 ≤ uₙ ≤ 10. On multiplie par 4/5 > 0 puis on ajoute 2 : 4 × 4/5 + 2 ≤ uₙ₊₁ ≤ 10 × 4/5 + 2, soit 5,2 ≤ uₙ₊₁ ≤ 10. Donc P(n + 1) est vraie.
3. Conclusion : 4 ≤ uₙ ≤ 10 pour tout n, donc (uₙ) est majorée par 10.
4. Sens de variation : uₙ₊₁ − uₙ = 2 − (1/5)uₙ = (1/5)(10 − uₙ) ≥ 0, puisque uₙ ≤ 10. La suite (uₙ) est croissante.
5. Croissante et majorée par 10, elle converge d'après le théorème ci-dessous : le volume se stabilise.

:::

::: piege
**Erreur : prendre le majorant pour la limite.** (uₙ) est majorée par 10, et l'on écrit lim uₙ = 10 parce que 10 est le plafond. Mais (uₙ) est aussi majorée par 12 et par 100 : le théorème garantit seulement que la limite existe, et non qu'elle égale un majorant. Sa valeur se calcule à la notion suivante.
:::

::: propriete
**Théorème (admis)** : toute suite croissante et majorée converge ; toute suite décroissante et minorée converge.
Cas limite : chaque hypothèse compte. uₙ = n est croissante sans converger, car elle n'est pas majorée ; (−1)ⁿ est bornée sans converger, car elle n'est pas monotone.
:::

::: methode Prouver la convergence d'une suite récurrente

1. Calculer les premiers termes pour conjecturer un sens de variation et une borne.
2. Démontrer l'encadrement par récurrence : initialisation, puis hérédité en appliquant à l'hypothèse les opérations qui transforment uₙ en uₙ₊₁.
3. Étudier le signe de uₙ₊₁ − uₙ en s'appuyant sur cet encadrement.
4. Conclure avec le théorème.

:::

::: verifie À toi : le cas décroissant
(uₙ) est définie par u₀ = 9 et uₙ₊₁ = (uₙ + 6)/2. Montrer qu'elle est minorée par 6, décroissante, puis qu'elle converge.

---

Récurrence sur P(n) : uₙ ≥ 6. Initialisation : u₀ = 9 ≥ 6. Hérédité : si uₙ ≥ 6, alors (uₙ + 6)/2 ≥ (6 + 6)/2 = 6. Ensuite uₙ₊₁ − uₙ = (6 − uₙ)/2 ≤ 0 puisque uₙ ≥ 6 : (uₙ) est décroissante. Décroissante et minorée par 6, elle converge d'après le théorème.
:::

::: retenir
Une suite croissante et majorée, ou décroissante et minorée, converge ; le théorème donne l'existence de la limite, pas sa valeur.
:::

## 🎯 Limite d'une suite récurrente : le point fixe

Le bassin converge vers un volume ℓ. Lequel ? Sur un graphique, on lit uₙ₊₁ = f(uₙ) avec deux droites : y = f(x) et y = x. On part de u₀ sur l'axe, on monte jusqu'à la droite y = f(x) pour lire u₁ = f(u₀), puis on rabat cette hauteur sur l'axe grâce à la droite y = x, et l'on recommence.
Où cet escalier s'arrête-t-il ?

::: figure L'escalier du bassin : de u₀ = 4, les marches montent vers le point où la droite y = f(x) coupe la droite y = x, d'abscisse 10
<svg viewBox="0 0 290 264">
<title>Escalier de la suite uₙ₊₁ = f(uₙ) avec f(x) = (4/5)x + 2 et u₀ = 4 : les termes montent vers l'abscisse 10 du point d'intersection des deux droites</title>
<line x1="34" y1="226" x2="280" y2="226" stroke="#0f172a" stroke-width="1.6"/>
<line x1="34" y1="232" x2="34" y2="8" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="280,226 272,222 272,230" fill="#0f172a"/>
<polygon points="34,8 30,16 38,16" fill="#0f172a"/>
<line x1="34" y1="226" x2="243" y2="17" stroke="#94a3b8" stroke-width="1.8"/>
<line x1="34" y1="188" x2="243" y2="20.8" stroke="#d97706" stroke-width="2.6"/>
<line x1="224" y1="36" x2="224" y2="226" stroke="#0f6e56" stroke-width="1.2" stroke-dasharray="4 3"/>
<line x1="224" y1="36" x2="34" y2="36" stroke="#0f6e56" stroke-width="1.2" stroke-dasharray="4 3"/>
<line x1="110" y1="226" x2="110" y2="127.2" stroke="#0f6e56" stroke-width="1.6"/>
<line x1="110" y1="127.2" x2="132.8" y2="127.2" stroke="#0f6e56" stroke-width="1.6"/>
<line x1="132.8" y1="127.2" x2="132.8" y2="108.96" stroke="#0f6e56" stroke-width="1.6"/>
<line x1="132.8" y1="108.96" x2="151.04" y2="108.96" stroke="#0f6e56" stroke-width="1.6"/>
<line x1="151.04" y1="108.96" x2="151.04" y2="94.37" stroke="#0f6e56" stroke-width="1.6"/>
<line x1="151.04" y1="94.37" x2="165.63" y2="94.37" stroke="#0f6e56" stroke-width="1.6"/>
<line x1="165.63" y1="94.37" x2="165.63" y2="82.69" stroke="#0f6e56" stroke-width="1.6"/>
<line x1="165.63" y1="82.69" x2="177.31" y2="82.69" stroke="#0f6e56" stroke-width="1.6"/>
<line x1="110" y1="223" x2="110" y2="229" stroke="#0f172a" stroke-width="1.2"/>
<line x1="132.8" y1="223" x2="132.8" y2="229" stroke="#0f172a" stroke-width="1.2"/>
<line x1="151.04" y1="223" x2="151.04" y2="229" stroke="#0f172a" stroke-width="1.2"/>
<line x1="165.63" y1="223" x2="165.63" y2="229" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="224" cy="36" r="4.2" fill="#0f6e56" stroke="#0f172a" stroke-width="1.2"/>
<g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="272" y="218" text-anchor="middle" fill="#0f172a" font-size="12">x</text><text x="44" y="18" text-anchor="start" fill="#0f172a" font-size="12">y</text><text x="224" y="242" text-anchor="middle" fill="#0f172a" font-size="11">10</text><text x="28" y="40" text-anchor="end" fill="#0f172a" font-size="11">10</text><text x="233" y="56" text-anchor="start" fill="#0f6e56" font-size="13">ℓ</text><text x="192" y="96" text-anchor="start" fill="#0f172a" font-size="12">y = x</text><text x="44" y="156" text-anchor="start" fill="#d97706" font-size="12">y = f(x)</text><text x="110" y="242" text-anchor="middle" fill="#0f172a" font-size="11">u₀</text><text x="132.8" y="255" text-anchor="middle" fill="#0f172a" font-size="11">u₁</text><text x="151.04" y="242" text-anchor="middle" fill="#0f172a" font-size="11">u₂</text><text x="165.63" y="255" text-anchor="middle" fill="#0f172a" font-size="11">u₃</text></g>
</svg>
:::

Les abscisses u₀, u₁, u₂, u₃ de la figure sont les volumes 4 ; 5,2 ; 6,16 ; 6,928, et l'abscisse du point d'intersection est la limite ℓ.

::: exemple Le volume limite du bassin

1. uₙ₊₁ = f(uₙ) avec f(x) = (4/5)x + 2, continue sur ℝ, et (uₙ) converge vers un réel ℓ (notion précédente).
2. Alors uₙ₊₁ tend aussi vers ℓ, et f(uₙ) tend vers f(ℓ) par continuité : on obtient ℓ = f(ℓ).
3. ℓ = (4/5)ℓ + 2 ⟺ (1/5)ℓ = 2 ⟺ ℓ = 10.
4. Le bassin tend vers 10 m³, abscisse du point d'intersection sur la figure.

:::

::: exemple Deux solutions possibles

1. u₀ = 1 et uₙ₊₁ = √(2uₙ + 3). Par récurrence, 1 ≤ uₙ ≤ 3 : si 1 ≤ uₙ ≤ 3, alors 5 ≤ 2uₙ + 3 ≤ 9, donc √5 ≤ uₙ₊₁ ≤ 3, et √5 > 1.
2. uₙ₊₁² − uₙ² = 2uₙ + 3 − uₙ² = (3 − uₙ)(1 + uₙ) ≥ 0, donc uₙ₊₁ ≥ uₙ puisque les termes sont positifs : (uₙ) est croissante et majorée, donc convergente vers un réel ℓ.
3. f(x) = √(2x + 3) est continue, donc ℓ = √(2ℓ + 3). En élevant au carré, ℓ² − 2ℓ − 3 = 0, soit (ℓ − 3)(ℓ + 1) = 0 : ℓ = 3 ou ℓ = −1.
4. Comme 1 ≤ uₙ ≤ 3 pour tout n, la limite vérifie 1 ≤ ℓ ≤ 3 : seule la solution ℓ = 3 convient.

:::

::: piege
**Erreur : résoudre f(ℓ) = ℓ sans savoir que la suite converge.** Pour u₀ = 1 et uₙ₊₁ = 2uₙ, on écrit ℓ = 2ℓ, donc ℓ = 0, et l'on annonce lim uₙ = 0. L'erreur tente parce que l'équation a bien une solution. Mais uₙ = 2ⁿ tend vers +∞ : sans convergence démontrée, l'équation ne dit rien.
:::

::: propriete
**Théorème (admis)** : si uₙ₊₁ = f(uₙ), si (uₙ) converge vers ℓ et si f est continue en ℓ, alors f(ℓ) = ℓ.
**Localisation** : si m ≤ uₙ ≤ M pour tout n et si (uₙ) converge vers ℓ, alors m ≤ ℓ ≤ M : une inégalité large reste large à la limite.
Cas limite : f(x) = x peut avoir plusieurs solutions (3 et −1 ci-dessus). C'est l'encadrement de la suite qui désigne la bonne, et la convergence se démontre avant de résoudre l'équation.
:::

::: verifie À toi : un point fixe
(uₙ) est définie par u₀ = 0 et uₙ₊₁ = √(uₙ + 12). On admet qu'elle est croissante et majorée par 4. Déterminer sa limite.

---

La suite converge vers un réel ℓ avec 0 ≤ ℓ ≤ 4. La fonction f(x) = √(x + 12) est continue, donc ℓ = √(ℓ + 12), d'où ℓ² − ℓ − 12 = 0, soit (ℓ − 4)(ℓ + 3) = 0. Comme ℓ ≥ 0, ℓ = 4.
:::

::: retenir
Si (uₙ) converge et si f est continue en sa limite, alors ℓ vérifie f(ℓ) = ℓ : on résout cette équation, puis on garde la solution compatible avec l'encadrement de la suite.
:::

## 🧩 Suite auxiliaire : se ramener à une suite géométrique ou arithmétique

On connaît la limite du bassin, 10 m³, mais pas son volume exact au jour n. L'écart au plafond, vₙ = uₙ − 10, vaut −6 ; −4,8 ; −3,84 aux jours 0, 1, 2 : chaque écart vaut les 4/5 du précédent.
Un écart multiplié par le même nombre chaque jour est une suite géométrique : peut-on s'en servir pour obtenir une formule pour uₙ ?

::: definition
**Suite arithmétique de raison r** : uₙ₊₁ = uₙ + r, donc uₙ = u₀ + nr.
**Suite géométrique de raison q** : uₙ₊₁ = q uₙ, donc uₙ = u₀qⁿ.
**Sommes** : Σ (k = 0 → n) vₖ = v₀ + v₁ + … + vₙ compte n + 1 termes. Arithmétique : (n + 1)(v₀ + vₙ)/2. Géométrique de raison q ≠ 1 : v₀(1 − q^{n+1})/(1 − q).
**Limites** : u₀qⁿ comme à la notion « limite d'une suite » ; u₀ + nr tend vers +∞ si r > 0, vers −∞ si r < 0 et reste égale à u₀ si r = 0.
:::

::: exemple Le volume exact du bassin

1. On pose vₙ = uₙ − 10. Alors vₙ₊₁ = (4/5)uₙ + 2 − 10 = (4/5)uₙ − 8 = (4/5)(uₙ − 10) = (4/5)vₙ.
2. (vₙ) est géométrique de raison 4/5 et de premier terme v₀ = 4 − 10 = −6, donc vₙ = −6(4/5)ⁿ.
3. uₙ = vₙ + 10 = 10 − 6(4/5)ⁿ. Contrôle : u₁ = 10 − 6 × 4/5 = 5,2 ✓.
4. Comme −1 < 4/5 < 1, (4/5)ⁿ → 0, donc lim uₙ = 10 : on retrouve la limite de la notion précédente.
5. La somme des écarts Sₙ = v₀ + … + vₙ = −6(1 − (4/5)^{n+1})/(1 − 4/5) = −30(1 − (4/5)^{n+1}) tend vers −30.

:::

::: exemple Une suite arithmétique cachée

1. u₀ = 1 et uₙ₊₁ = uₙ/(1 + 2uₙ). Les termes sont strictement positifs (un quotient de deux positifs est positif, par récurrence) : on peut poser wₙ = 1/uₙ.
2. wₙ₊₁ = (1 + 2uₙ)/uₙ = 1/uₙ + 2 = wₙ + 2 : (wₙ) est arithmétique de raison 2, avec w₀ = 1.
3. wₙ = 1 + 2n, donc uₙ = 1/(2n + 1). Contrôle : u₁ = 1/(1 + 2) = 1/3 ✓.
4. wₙ → +∞ car r = 2 > 0, donc uₙ = 1/wₙ → 0.

:::

::: piege
**Erreur : donner pour limite de uₙ celle de la suite auxiliaire.** Comme vₙ = −6(4/5)ⁿ tend vers 0, on écrit lim uₙ = 0. L'erreur tente parce que la limite de vₙ est le dernier résultat obtenu. Mais uₙ = vₙ + 10 : la limite de uₙ est 0 + 10 = 10, et 0 est impossible puisque uₙ ≥ 4.
:::

::: methode Se ramener à une suite géométrique

1. Pour uₙ₊₁ = a uₙ + b avec a ≠ 1, on cherche ℓ tel que ℓ = aℓ + b, soit ℓ = b/(1 − a).
2. On pose vₙ = uₙ − ℓ : alors vₙ₊₁ = a vₙ, suite géométrique de raison a.
3. On écrit vₙ = v₀aⁿ, puis uₙ = ℓ + v₀aⁿ ; si −1 < a < 1, lim uₙ = ℓ.
4. Si l'énoncé impose un vₙ (une fraction de uₙ, un inverse), on calcule vₙ₊₁ en fonction de uₙ et on le met sous la forme q vₙ ou vₙ + r.
Cas limite : pour a = 1, uₙ₊₁ = uₙ + b est déjà arithmétique de raison b.

:::

::: verifie À toi : poser la suite auxiliaire
u₀ = 0 et uₙ₊₁ = (1/3)uₙ + 4. On pose vₙ = uₙ − 6. Donner vₙ, uₙ et lim uₙ.

---

vₙ₊₁ = (1/3)uₙ + 4 − 6 = (1/3)uₙ − 2 = (1/3)(uₙ − 6) = (1/3)vₙ : (vₙ) est géométrique de raison 1/3, avec v₀ = −6. Donc vₙ = −6(1/3)ⁿ et uₙ = 6 − 6(1/3)ⁿ. Comme −1 < 1/3 < 1, lim uₙ = 6.
:::

::: retenir
Pour uₙ₊₁ = a uₙ + b, la suite vₙ = uₙ − ℓ est géométrique de raison a ; on revient ensuite à uₙ = vₙ + ℓ avant de prendre la limite.
:::

## 🛡️ Comparaison et gendarmes

Un capteur de pression envoie à la n-ième mesure xₙ = 5 + (sin n)/n. Le terme sin n varie de façon désordonnée et n'a pas de limite : la règle d'addition ne s'applique pas. Pourtant (sin n)/n est petit dès que n est grand, puisque |sin n| ≤ 1.
Peut-on conclure à la limite de xₙ sans connaître celle de sin n ?

::: figure Les points (n ; xₙ) restent entre les courbes 5 − 1/n et 5 + 1/n, qui se resserrent autour de 5
<svg viewBox="0 0 340 236">
<title>Les points (n ; xₙ) avec xₙ = 5 + (sin n)/n restent entre les courbes 5 − 1/n et 5 + 1/n, qui se resserrent autour de 5</title>
<line x1="40" y1="214" x2="326" y2="214" stroke="#0f172a" stroke-width="1.6"/>
<line x1="40" y1="222" x2="40" y2="12" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="326,214 318,210 318,218" fill="#0f172a"/>
<polygon points="40,12 36,20 44,20" fill="#0f172a"/>
<line x1="40" y1="124.4" x2="320.8" y2="124.4" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="4 3"/>
<polyline points="59.5,60.4 64.38,73.2 69.25,81.73 74.12,87.83 79,92.4 83.88,95.96 88.75,98.8 93.62,101.13 98.5,103.07 103.38,104.71 108.25,106.11 113.12,107.33 118,108.4 122.88,109.34 127.75,110.18 132.62,110.93 137.5,111.6 142.38,112.21 147.25,112.76 152.12,113.27 157,113.73 161.88,114.16 166.75,114.55 171.62,114.92 176.5,115.26 181.38,115.57 186.25,115.87 191.12,116.14 196,116.4 200.88,116.64 205.75,116.87 210.62,117.09 215.5,117.29 220.38,117.48 225.25,117.66 230.12,117.84 235,118 239.88,118.16 244.75,118.3 249.62,118.45 254.5,118.58 259.38,118.71 264.25,118.83 269.12,118.95 274,119.07 278.88,119.18 283.75,119.28 288.62,119.38 293.5,119.48 298.38,119.57 303.25,119.66 308.12,119.75 313,119.83 317.88,119.91" fill="none" stroke="#0f6e56" stroke-width="2.2"/>
<polyline points="59.5,188.4 64.38,175.6 69.25,167.07 74.12,160.97 79,156.4 83.88,152.84 88.75,150 93.62,147.67 98.5,145.73 103.38,144.09 108.25,142.69 113.12,141.47 118,140.4 122.88,139.46 127.75,138.62 132.62,137.87 137.5,137.2 142.38,136.59 147.25,136.04 152.12,135.53 157,135.07 161.88,134.64 166.75,134.25 171.62,133.88 176.5,133.54 181.38,133.23 186.25,132.93 191.12,132.66 196,132.4 200.88,132.16 205.75,131.93 210.62,131.71 215.5,131.51 220.38,131.32 225.25,131.14 230.12,130.96 235,130.8 239.88,130.64 244.75,130.5 249.62,130.35 254.5,130.22 259.38,130.09 264.25,129.97 269.12,129.85 274,129.73 278.88,129.62 283.75,129.52 288.62,129.42 293.5,129.32 298.38,129.23 303.25,129.14 308.12,129.05 313,128.97 317.88,128.89" fill="none" stroke="#0f6e56" stroke-width="2.2"/>
<line x1="59.5" y1="211" x2="59.5" y2="217" stroke="#0f172a" stroke-width="1.2"/>
<line x1="137.5" y1="211" x2="137.5" y2="217" stroke="#0f172a" stroke-width="1.2"/>
<line x1="235" y1="211" x2="235" y2="217" stroke="#0f172a" stroke-width="1.2"/>
<line x1="313" y1="211" x2="313" y2="217" stroke="#0f172a" stroke-width="1.2"/>
<line x1="37" y1="188.4" x2="43" y2="188.4" stroke="#0f172a" stroke-width="1.2"/>
<line x1="37" y1="124.4" x2="43" y2="124.4" stroke="#0f172a" stroke-width="1.2"/>
<line x1="37" y1="60.4" x2="43" y2="60.4" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="59.5" cy="70.55" r="3.4" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="79" cy="95.3" r="3.4" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="98.5" cy="121.39" r="3.4" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="118" cy="136.51" r="3.4" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="137.5" cy="136.67" r="3.4" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="157" cy="127.38" r="3.4" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="176.5" cy="118.39" r="3.4" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="196" cy="116.49" r="3.4" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="215.5" cy="121.47" r="3.4" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="235" cy="127.88" r="3.4" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="254.5" cy="130.22" r="3.4" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="274" cy="127.26" r="3.4" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="293.5" cy="122.33" r="3.4" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="313" cy="119.87" r="3.4" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="318" y="206" text-anchor="middle" fill="#0f172a" font-size="12">n</text><text x="50" y="22" text-anchor="start" fill="#0f172a" font-size="12">y</text><text x="59.5" y="230" text-anchor="middle" fill="#0f172a" font-size="11">1</text><text x="137.5" y="230" text-anchor="middle" fill="#0f172a" font-size="11">5</text><text x="235" y="230" text-anchor="middle" fill="#0f172a" font-size="11">10</text><text x="313" y="230" text-anchor="middle" fill="#0f172a" font-size="11">14</text><text x="33" y="192.4" text-anchor="end" fill="#0f172a" font-size="11">4</text><text x="33" y="128.4" text-anchor="end" fill="#0f172a" font-size="11">5</text><text x="33" y="64.4" text-anchor="end" fill="#0f172a" font-size="11">6</text><text x="320.8" y="111.96" text-anchor="end" fill="#0f6e56" font-size="12">5 + 1/n</text><text x="320.8" y="144.84" text-anchor="end" fill="#0f6e56" font-size="12">5 − 1/n</text></g>
</svg>
:::

Les deux courbes de la figure sont les suites 5 − 1/n et 5 + 1/n des gendarmes : le point de rang n est toujours entre elles.

::: exemple Le capteur

1. Pour tout n ≥ 1, −1 ≤ sin n ≤ 1, donc −1/n ≤ (sin n)/n ≤ 1/n en divisant par n > 0.
2. En ajoutant 5 : 5 − 1/n ≤ xₙ ≤ 5 + 1/n.
3. 5 − 1/n → 5 et 5 + 1/n → 5 : les deux bornes ont la même limite.
4. Par le théorème des gendarmes, lim xₙ = 5.

:::

::: exemple Vers l'infini

1. uₙ = n² − 3 cos n. Comme cos n ≤ 1, on a −3 cos n ≥ −3, donc uₙ ≥ n² − 3.
2. lim (n² − 3) = +∞.
3. Par comparaison, lim uₙ = +∞ : la minorante pousse uₙ vers +∞.

:::

::: exemple Une suite d'intégrales

1. Iₙ = ∫₀¹ xⁿ√(1 + x)dx. Sur [0 ; 1], 1 ≤ √(1 + x) ≤ √2 et xⁿ ≥ 0, donc xⁿ ≤ xⁿ√(1 + x) ≤ √2 xⁿ.
2. On intègre sur [0 ; 1], l'intégrale conservant l'ordre : ∫₀¹ xⁿ dx ≤ Iₙ ≤ √2 ∫₀¹ xⁿ dx, avec ∫₀¹ xⁿ dx = [x^{n+1}/(n + 1)]₀¹ = 1/(n + 1).
3. Donc 1/(n + 1) ≤ Iₙ ≤ √2/(n + 1). Les deux bornes tendent vers 0 : lim Iₙ = 0.

:::

::: piege
**Erreur : appliquer les gendarmes avec deux bornes de limites différentes.** −1 ≤ (−1)ⁿ ≤ 1 est un encadrement par deux suites constantes, et l'on écrit que (−1)ⁿ converge. L'erreur tente parce que les deux bornes convergent. Mais leurs limites sont −1 et 1 : le théorème exige la même limite ℓ des deux côtés, et (−1)ⁿ n'a pas de limite.
:::

::: propriete
Soit (uₙ), (vₙ) et (wₙ) trois suites et p un entier.
**Comparaison** : si uₙ ≤ vₙ pour tout n ≥ p et lim uₙ = +∞, alors lim vₙ = +∞ ; si uₙ ≤ vₙ pour tout n ≥ p et lim vₙ = −∞, alors lim uₙ = −∞.
**Gendarmes** : si vₙ ≤ uₙ ≤ wₙ pour tout n ≥ p et si (vₙ) et (wₙ) convergent vers le même réel ℓ, alors lim uₙ = ℓ. En particulier, si |uₙ| ≤ vₙ et lim vₙ = 0, alors lim uₙ = 0.
Cas limite : l'inégalité n'est exigée qu'à partir d'un rang p, car la limite ne dépend pas des premiers termes.
:::

::: verifie À toi : un terme oscillant
Déterminer lim n→+∞ (−1)ⁿ/(n + 2).

---

|(−1)ⁿ/(n + 2)| = 1/(n + 2) pour tout n, et 1/(n + 2) → 0. Par le cas particulier des gendarmes, lim (−1)ⁿ/(n + 2) = 0, alors que (−1)ⁿ seul n'a pas de limite.
:::

::: retenir
Quand un terme oscillant résiste aux opérations, on l'encadre : deux bornes de même limite ℓ imposent la limite ℓ, et une minoration qui tend vers +∞ impose +∞.
:::

> 🏆 Les huit notions sont franchies : tu sais lire le sens de variation et les bornes d'une suite, calculer une limite, lever une forme indéterminée, garantir une convergence, trouver une limite par le point fixe, ramener une suite à une géométrique et encadrer une limite rebelle. Prochaine étape : les nombres complexes.
