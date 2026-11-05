# ⚔️ Suites réelles — lire la destination d'une suite

> 💡 «Une suite est une file de nombres : tout l'art est de deviner où elle va, puis de le prouver.»

Les fonctions te donnaient une valeur pour chaque réel ; une suite en donne une pour chaque entier n : u₀, u₁, u₂, … Huit notions te mènent de la définition d'une limite jusqu'aux suites adjacentes, en passant par les opérations, les gendarmes et le point fixe. On suppose acquis le raisonnement par récurrence, les suites arithmétiques et géométriques (avec la somme 1 + q + … + qⁿ = (1 − qⁿ⁺¹)/(1 − q) pour q ≠ 1), ainsi que les limites de fonctions et la continuité du chapitre précédent, dont la limite usuelle sin x / x → 1 en 0.

## 🧭 Limite d'une suite et sous-suites paire et impaire

Une balance de précision affiche, à la pesée n (n = 1, 2, 3, …), le relevé xₙ = 20 + (−1)ⁿ/n grammes : 19 ; 20,5 ; 19,67 ; 20,25 ; 19,8 ; … Les relevés sautent de part et d'autre de 20 en se resserrant.
Peut-on affirmer que xₙ se stabilise sur 20, alors que le signe change à chaque rang ?

::: figure Les points orange (rangs pairs) sont au-dessus de la droite y = 20, les points verts (rangs impairs) au-dessous : chaque famille se rapproche de 20
<svg viewBox="0 0 340 236">
<title>Les points (n ; xₙ) pour xₙ = 20 + (−1)ⁿ/n et n de 1 à 12 : les rangs pairs sont au-dessus de 20, les rangs impairs au-dessous, tous se resserrent sur 20</title>
<line x1="44" y1="206" x2="326" y2="206" stroke="#0f172a" stroke-width="1.6"/>
<line x1="44" y1="214" x2="44" y2="12" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="326,206 318,202 318,210" fill="#0f172a"/>
<polygon points="44,12 40,20 48,20" fill="#0f172a"/>
<line x1="44" y1="98" x2="316" y2="98" stroke="#0f6e56" stroke-width="1.6" stroke-dasharray="6 3"/>
<line x1="65.59" y1="203" x2="65.59" y2="209" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="65.59" cy="188" r="3.6" fill="#0f6e56" stroke="#0f172a" stroke-width="1.2"/>
<line x1="87.17" y1="203" x2="87.17" y2="209" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="87.17" cy="53" r="3.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<line x1="108.76" y1="203" x2="108.76" y2="209" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="108.76" cy="128" r="3.6" fill="#0f6e56" stroke="#0f172a" stroke-width="1.2"/>
<line x1="130.35" y1="203" x2="130.35" y2="209" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="130.35" cy="75.5" r="3.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<line x1="151.94" y1="203" x2="151.94" y2="209" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="151.94" cy="116" r="3.6" fill="#0f6e56" stroke="#0f172a" stroke-width="1.2"/>
<line x1="173.52" y1="203" x2="173.52" y2="209" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="173.52" cy="83" r="3.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<line x1="195.11" y1="203" x2="195.11" y2="209" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="195.11" cy="110.86" r="3.6" fill="#0f6e56" stroke="#0f172a" stroke-width="1.2"/>
<line x1="216.7" y1="203" x2="216.7" y2="209" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="216.7" cy="86.75" r="3.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<line x1="238.29" y1="203" x2="238.29" y2="209" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="238.29" cy="108" r="3.6" fill="#0f6e56" stroke="#0f172a" stroke-width="1.2"/>
<line x1="259.87" y1="203" x2="259.87" y2="209" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="259.87" cy="89" r="3.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<line x1="281.46" y1="203" x2="281.46" y2="209" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="281.46" cy="106.18" r="3.6" fill="#0f6e56" stroke="#0f172a" stroke-width="1.2"/>
<line x1="303.05" y1="203" x2="303.05" y2="209" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="303.05" cy="90.5" r="3.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<line x1="41" y1="188" x2="47" y2="188" stroke="#0f172a" stroke-width="1.2"/>
<line x1="41" y1="98" x2="47" y2="98" stroke="#0f172a" stroke-width="1.2"/>
<g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="65.59" y="222" text-anchor="middle" fill="#0f172a" font-size="11">1</text><text x="87.17" y="222" text-anchor="middle" fill="#0f172a" font-size="11">2</text><text x="108.76" y="222" text-anchor="middle" fill="#0f172a" font-size="11">3</text><text x="130.35" y="222" text-anchor="middle" fill="#0f172a" font-size="11">4</text><text x="151.94" y="222" text-anchor="middle" fill="#0f172a" font-size="11">5</text><text x="173.52" y="222" text-anchor="middle" fill="#0f172a" font-size="11">6</text><text x="195.11" y="222" text-anchor="middle" fill="#0f172a" font-size="11">7</text><text x="216.7" y="222" text-anchor="middle" fill="#0f172a" font-size="11">8</text><text x="238.29" y="222" text-anchor="middle" fill="#0f172a" font-size="11">9</text><text x="259.87" y="222" text-anchor="middle" fill="#0f172a" font-size="11">10</text><text x="281.46" y="222" text-anchor="middle" fill="#0f172a" font-size="11">11</text><text x="303.05" y="222" text-anchor="middle" fill="#0f172a" font-size="11">12</text><text x="37" y="192" text-anchor="end" fill="#0f172a" font-size="11">19</text><text x="37" y="102" text-anchor="end" fill="#0f172a" font-size="11">20</text><text x="318" y="198" text-anchor="middle" fill="#0f172a" font-size="12">n</text><text x="56" y="14" text-anchor="start" fill="#0f172a" font-size="12">xₙ</text></g>
</svg>
:::

Les points orange sont les termes x₂ₙ et les points verts les termes x₂ₙ₊₁ : c'est cette séparation en deux familles qui permet de conclure.

::: definition
La suite (uₙ) **converge** vers le réel ℓ, ce qu'on note lim n→+∞ uₙ = ℓ, lorsque uₙ est aussi proche qu'on veut de ℓ dès que n est assez grand. Elle **diverge** si elle tend vers +∞, vers −∞, ou si elle n'a pas de limite.
Elle est **bornée** s'il existe deux réels m et M tels que m ≤ uₙ ≤ M pour tout n.
:::

::: exemple La balance se stabilise

1. Pour les rangs pairs, (−1)²ⁿ = 1 : x₂ₙ = 20 + 1/(2n), n ≥ 1.
2. Pour les rangs impairs, (−1)²ⁿ⁺¹ = −1 : x₂ₙ₊₁ = 20 − 1/(2n + 1), n ≥ 0.
3. 1/(2n) → 0 et 1/(2n + 1) → 0 : x₂ₙ → 20 et x₂ₙ₊₁ → 20, deux limites égales.
4. D'après le théorème ci-dessous, lim xₙ = 20 : la balance se stabilise sur 20 grammes.

:::

::: exemple Deux limites différentes

1. vₙ = (−1)ⁿ n/(n + 2), n ≥ 1, vaut −1/3 ; 1/2 ; −3/5 ; 2/3 ; … : le signe alterne.
2. v₂ₙ = 2n/(2n + 2) = n/(n + 1) → 1, car on divise par le terme dominant n.
3. v₂ₙ₊₁ = −(2n + 1)/(2n + 3) → −1, pour la même raison.
4. 1 ≠ −1 : (vₙ) n'a pas de limite. Pourtant |vₙ| = n/(n + 2) < 1, donc −1 < vₙ < 1 : (vₙ) est bornée.

:::

::: piege
**Erreur : conclure avec une seule des deux sous-suites.** Pour wₙ = n(1 + (−1)ⁿ)/(n + 1), on calcule w₂ₙ = 4n/(2n + 1) → 2 et l'on écrit lim wₙ = 2. L'erreur tente parce que le rang pair donne une belle limite. Mais w₂ₙ₊₁ = 0 pour tout n, car 1 + (−1)²ⁿ⁺¹ = 0 : les rangs impairs tendent vers 0 ≠ 2, donc (wₙ) n'a pas de limite.
:::

::: propriete
**Rangs pairs et impairs (théorème admis)** : lim uₙ = a, avec a fini ou infini, si et seulement si lim u₂ₙ = a et lim u₂ₙ₊₁ = a.
**Suite convergente (théorème admis)** : toute suite convergente est bornée. Par contraposée, une suite non bornée diverge.
Cas limite : la réciproque est fausse. (vₙ) est bornée et pourtant divergente ; on ne conclut jamais « elle converge » à partir de « elle est bornée ».
:::

::: verifie À toi : séparer pairs et impairs
Déterminer la limite de uₙ = 5 − (−1)ⁿ/(n + 1), n ≥ 0.

---

Pour les rangs pairs, u₂ₙ = 5 − 1/(2n + 1) → 5. Pour les rangs impairs, u₂ₙ₊₁ = 5 + 1/(2n + 2) → 5. Les deux sous-suites ont la même limite 5, donc lim uₙ = 5 d'après le théorème des rangs pairs et impairs.
:::

::: retenir
Une suite tend vers a exactement quand ses rangs pairs et ses rangs impairs tendent tous deux vers a ; une suite convergente est bornée, mais une suite bornée peut diverger.
:::

## 🧮 Opérations sur les limites

Dans un réservoir, la quantité de sel au jour n est mₙ = 3n² + n grammes et le volume d'eau vₙ = n² + 5 litres. La concentration cₙ = mₙ/vₙ vaut environ 2,95 g/L au jour 10, 3,009 au jour 100 et 3,001 au jour 1000.
Les deux termes tendent vers +∞ : que devient le quotient, et comment le démontrer sans calculer des milliers de termes ?

::: exemple La concentration du réservoir

1. mₙ → +∞ et vₙ → +∞ : la forme +∞/+∞ est indéterminée, on ne peut pas conclure directement.
2. On met n² en facteur en haut et en bas : cₙ = n²(3 + 1/n)/(n²(1 + 5/n²)) = (3 + 1/n)/(1 + 5/n²), pour n ≥ 1, car n² est le terme dominant.
3. 1/n → 0 et 5/n² → 0 : le numérateur tend vers 3 et le dénominateur vers 1, qui n'est pas nul.
4. lim cₙ = 3/1 = 3, ce que suggère le tableau de valeurs.

:::

::: exemple Un produit et une différence

1. aₙ = (1/n² − 1/2)(n³ + 3n − 1) : le premier facteur tend vers −1/2 et le second vers +∞, deux formes déterminées. Par la règle des signes, lim aₙ = −∞.
2. bₙ = n³ − 4n² + 2 est de la forme +∞ − ∞ : on ne conclut pas directement. On met n³ en facteur : bₙ = n³(1 − 4/n + 2/n³), car n³ domine.
3. La parenthèse tend vers 1, donc lim bₙ = (+∞) × 1 = +∞.

:::

::: piege
**Erreur : écrire ∞/∞ = 1.** Pour (n² + 1)/(n + 3), on écrit +∞/+∞ = 1. L'erreur tente parce que x/x = 1 pour tout réel x non nul. Mais n/n² → 0, 2n/n → 2 et n²/n → +∞ : trois quotients de la forme ∞/∞ avec trois limites différentes. Ici (n² + 1)/(n + 3) = n(1 + 1/n²)/(1 + 3/n) → +∞.
:::

::: propriete
**Somme** : a + b ; (+∞) + b = +∞ ; (−∞) + b = −∞ ; (+∞) + (+∞) = +∞ ; (−∞) + (−∞) = −∞.
**Produit** : ab ; ∞ × b = ∞ si b ≠ 0 ; ∞ × ∞ = ∞, avec la règle des signes.
**Quotient** : a/b si b ≠ 0 ; ∞/b = ∞ avec la règle des signes ; a/(±∞) = 0 ; a/0 = ∞ si a ≠ 0, avec la règle des signes.
Les formes indéterminées sont (+∞) − (+∞), 0 × ∞, ∞/∞ et 0/0 : on transforme l'expression (terme dominant en facteur) avant de conclure.
Cas limite : « a/0 = ∞ » exige un dénominateur de signe constant. Pour vₙ = (−1)ⁿ/n → 0, le quotient 1/vₙ = (−1)ⁿ n change de signe en grandissant et n'a pas de limite.
:::

::: verifie À toi : le terme dominant
Calculer lim n→+∞ (7n² + 2)/(3n² − n).

---

Le quotient est de la forme ∞/∞. On met n² en facteur : (7 + 2/n²)/(3 − 1/n), pour n ≥ 1. Le numérateur tend vers 7 et le dénominateur vers 3, non nul : la limite vaut 7/3.
:::

::: retenir
Hors formes indéterminées, les limites se combinent comme celles de fonctions ; pour ∞/∞ ou ∞ − ∞, on met le terme dominant en facteur avant de conclure.
:::

## 📐 Suites géométriques : la limite de qⁿ

Une balle lâchée de 2 m rebondit à 80 % de sa hauteur précédente : après n rebonds, elle monte à hₙ = 2 × 0,8ⁿ mètres, soit 2 ; 1,6 ; 1,28 ; 1,024 ; … La hauteur s'écrase vers 0.
Et si le rebond atteignait 120 % de la hauteur précédente, ou si la raison était négative ? Tout dépend de la raison q.

::: exemple Quatre raisons, quatre comportements

1. (1/5)ⁿ : 0 < 1/5 < 1, donc lim (1/5)ⁿ = 0.
2. (−2/√5)ⁿ : |−2/√5| = 2/√5 ≈ 0,894 < 1, donc lim = 0, avec des termes de signes alternés.
3. (√π)ⁿ : √π ≈ 1,77 > 1, donc lim (√π)ⁿ = +∞.
4. (−√3)ⁿ : −√3 < −1, les termes grandissent en valeur absolue en changeant de signe, donc (−√3)ⁿ n'a pas de limite.

:::

::: exemple Une somme géométrique

1. Sₙ = 1 + 5/3 + (5/3)² + … + (5/3)ⁿ est la somme de n + 1 termes d'une suite géométrique de raison q = 5/3 ≠ 1.
2. Sₙ = (1 − (5/3)ⁿ⁺¹)/(1 − 5/3) = (3/2)((5/3)ⁿ⁺¹ − 1), car 1 − 5/3 = −2/3.
3. 5/3 > 1 donc (5/3)ⁿ⁺¹ → +∞ et lim Sₙ = +∞.

:::

::: exemple Une suite qui se ramène à une géométrique

1. u₀ = 1 et uₙ₊₁ = 3uₙ − 4. On cherche α tel que α = 3α − 4, soit α = 2 : c'est le réel qui ne bouge pas.
2. On pose vₙ = uₙ − 2. Alors vₙ₊₁ = 3uₙ − 4 − 2 = 3(uₙ − 2) = 3vₙ, car −6 = 3 × (−2).
3. (vₙ) est géométrique de raison 3 et de premier terme v₀ = 1 − 2 = −1, donc vₙ = −3ⁿ.
4. uₙ = 2 − 3ⁿ. Contrôle : u₁ = 2 − 3 = −1 et 3 × 1 − 4 = −1 ✓. Comme 3ⁿ → +∞, lim uₙ = −∞.

:::

::: piege
**Erreur : traiter q = −1 comme une raison de module inférieur à 1.** Pour (−1)ⁿ, on écrit |q| = 1 ≤ 1, donc la limite est 0. L'erreur tente parce que la frontière |q| = 1 ressemble au cas |q| < 1 et paraît sans danger. Mais (−1)ⁿ vaut 1, −1, 1, −1, … : ces termes restent à distance 1 de 0, et la suite n'a pas de limite. Pour q = 1, la suite est constante égale à 1.
:::

::: propriete
**Théorème (rappel)** : pour q réel non nul, q > 1 donne lim qⁿ = +∞ ; |q| < 1 donne lim qⁿ = 0 ; q ≤ −1 donne une suite sans limite ; q = 1 donne la suite constante 1.
**Somme** : pour |q| < 1, 1 + q + … + qⁿ = (1 − qⁿ⁺¹)/(1 − q) → 1/(1 − q).
**Suite auxiliaire** : pour uₙ₊₁ = a uₙ + b avec a ≠ 1, on pose vₙ = uₙ − α où α = aα + b ; alors (vₙ) est géométrique de raison a.
Cas limite : pour a = 1, uₙ₊₁ = uₙ + b est déjà arithmétique de raison b.
:::

::: verifie À toi : une somme qui converge
Calculer lim n→+∞ (1 + 3/4 + (3/4)² + … + (3/4)ⁿ).

---

C'est la somme d'une suite géométrique de raison q = 3/4 ≠ 1 : elle vaut (1 − (3/4)ⁿ⁺¹)/(1 − 3/4). Comme |3/4| < 1, (3/4)ⁿ⁺¹ → 0, et la limite est 1/(1 − 3/4) = 4.
:::

::: retenir
qⁿ tend vers +∞ si q > 1, vers 0 si |q| < 1, et n'a pas de limite si q ≤ −1 ; pour uₙ₊₁ = a uₙ + b, la suite uₙ − α est géométrique de raison a.
:::

## 🔄 Composer une suite avec une fonction

On tourne un cadran d'un angle de 1/n radian à l'étape n et l'on lit la projection cos(1/n) : environ 0,54 ; 0,88 ; 0,98 ; 0,995 pour n = 1 ; 2 ; 5 ; 10. La lecture semble se rapprocher de 1 = cos 0.
Peut-on toujours calculer la limite d'une suite f(uₙ) en « appliquant f » à la limite de uₙ ?

::: exemple Le cadran

1. uₙ = 1/n tend vers 0, et uₙ est un élément de l'intervalle ouvert I = ℝ.
2. f(x) = cos x est continue en 0, donc lim x→0 cos x = cos 0 = 1.
3. Par le théorème ci-dessous, lim cos(1/n) = 1, ce que suggèrent les valeurs lues.

:::

::: exemple Un produit avec un sinus

1. wₙ = n sin(π/(3n)), n ≥ 1. On pose Xₙ = π/(3n) : Xₙ → 0 et Xₙ appartient à I = ]0 ; +∞[, intervalle ouvert.
2. n = π/(3Xₙ), donc wₙ = (π/3) × sin(Xₙ)/Xₙ.
3. lim x→0 sin x/x = 1 (limite usuelle) : par le théorème, sin(Xₙ)/Xₙ → 1.
4. lim wₙ = (π/3) × 1 = π/3.

:::

::: piege
**Erreur : écrire lim f(uₙ) = f(lim uₙ) sans regarder f.** Pour f(x) = x/|x| sur ]−1 ; 0[ ∪ ]0 ; 1[ et uₙ = (−1)ⁿ/n → 0, on écrit f(uₙ) → f(0). L'erreur tente parce que, pour une fonction continue, la formule marche toujours. Mais f(0) n'existe pas, et f n'a pas de limite en 0 : −1 à gauche, +1 à droite. Ici f(uₙ) = (−1)ⁿ, qui n'a pas de limite.
:::

::: propriete
**Théorème (admis)** : soit f définie sur un intervalle ouvert I et (uₙ) une suite d'éléments de I. Si lim uₙ = ℓ (fini ou infini) et si lim x→ℓ f(x) = L (fini ou infini), alors lim f(uₙ) = L.
Cas limite : ℓ peut être +∞. Pour uₙ = n² → +∞ et f(x) = 1/x, qui tend vers 0 en +∞, on obtient lim 1/n² = 0.
:::

::: verifie À toi : composer avec un cosinus
Calculer lim n→+∞ cos(πn/(3n + 2)).

---

Le quotient πn/(3n + 2) tend vers π/3, car on divise par le terme dominant n. La fonction cosinus est continue en π/3, donc lim cos(πn/(3n + 2)) = cos(π/3) = 1/2.
:::

::: retenir
Si uₙ → ℓ et si f a une limite L en ℓ, alors f(uₙ) → L ; il faut toujours vérifier que f a bien une limite en ℓ.
:::

## 🛡️ Comparer pour conclure : encadrement et gendarmes

On veut la limite de tₙ = (5n + 2 cos n)/(n + 4). Le cosinus de n ne se calcule pas simplement, mais il reste entre −1 et 1. Les valeurs sont environ 3,45 pour n = 10, 4,82 pour n = 100 et 4,98 pour n = 1000.
Comment prouver que tₙ tend vers 5 sans jamais calculer cos n ?

::: figure Les points (n ; tₙ) sont pris en étau entre deux courbes qui se resserrent sur la droite y = 5 : ils ne peuvent aller que vers 5
<svg viewBox="0 0 340 236">
<title>Les points (n ; tₙ) pour tₙ = (5n + 2 cos n)/(n + 4) restent entre les deux courbes guides (5n − 2)/(n + 4) et (5n + 2)/(n + 4), qui se resserrent sur la droite y = 5</title>
<line x1="44" y1="206" x2="326" y2="206" stroke="#0f172a" stroke-width="1.6"/>
<line x1="44" y1="214" x2="44" y2="12" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="326,206 318,202 318,210" fill="#0f172a"/>
<polygon points="44,12 40,20 48,20" fill="#0f172a"/>
<line x1="44" y1="56" x2="316" y2="56" stroke="#0f6e56" stroke-width="1.6" stroke-dasharray="6 3"/>
<polyline points="50.67,188 57.33,166 64,150.29 70.67,138.5 77.33,129.33 84,122 90.67,116 97.33,111 104,106.77 110.67,103.14 117.33,100 124,97.25 130.67,94.82 137.33,92.67 144,90.74 150.67,89 157.33,87.43 164,86 170.67,84.7 177.33,83.5 184,82.4 190.67,81.38 197.33,80.44 204,79.57 210.67,78.76 217.33,78 224,77.29 230.67,76.62 237.33,76 244,75.41 250.67,74.86 257.33,74.33 264,73.84 270.67,73.37 277.33,72.92 284,72.5 290.67,72.1 297.33,71.71 304,71.35 310.67,71" fill="none" stroke="#94a3b8" stroke-width="1.6"/>
<polyline points="50.67,164 57.33,146 64,133.14 70.67,123.5 77.33,116 84,110 90.67,105.09 97.33,101 104,97.54 110.67,94.57 117.33,92 124,89.75 130.67,87.76 137.33,86 144,84.42 150.67,83 157.33,81.71 164,80.55 170.67,79.48 177.33,78.5 184,77.6 190.67,76.77 197.33,76 204,75.29 210.67,74.62 217.33,74 224,73.42 230.67,72.88 237.33,72.36 244,71.88 250.67,71.43 257.33,71 264,70.59 270.67,70.21 277.33,69.85 284,69.5 290.67,69.17 297.33,68.86 304,68.56 310.67,68.27" fill="none" stroke="#94a3b8" stroke-width="1.6"/>
<circle cx="50.67" cy="169.52" r="2.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="57.33" cy="160.16" r="2.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="64" cy="150.2" r="2.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="70.67" cy="135.9" r="2.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="77.33" cy="120.78" r="2.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="84" cy="110.24" r="2.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="90.67" cy="106.43" r="2.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="97.33" cy="106.73" r="2.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="104" cy="106.36" r="2.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="110.67" cy="102.45" r="2.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="117.33" cy="95.98" r="2.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="124" cy="90.34" r="2.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="130.67" cy="88.09" r="2.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="137.33" cy="88.88" r="2.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="144" cy="89.98" r="2.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="150.67" cy="88.87" r="2.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="157.33" cy="85.36" r="2.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="164" cy="81.47" r="2.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="170.67" cy="79.51" r="2.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="177.33" cy="79.98" r="2.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="184" cy="81.31" r="2.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="190.67" cy="81.38" r="2.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="197.33" cy="79.41" r="2.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="204" cy="76.52" r="2.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="210.67" cy="74.64" r="2.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="217.33" cy="74.71" r="2.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="224" cy="75.92" r="2.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="230.67" cy="76.55" r="2.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="237.33" cy="75.54" r="2.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="244" cy="73.37" r="2.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="250.67" cy="71.57" r="2.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="257.33" cy="71.28" r="2.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="264" cy="72.24" r="2.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="270.67" cy="73.13" r="2.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="277.33" cy="72.77" r="2.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="284" cy="71.19" r="2.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="290.67" cy="69.51" r="2.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="297.33" cy="68.92" r="2.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="304" cy="69.58" r="2.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="310.67" cy="70.55" r="2.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<line x1="50.67" y1="203" x2="50.67" y2="209" stroke="#0f172a" stroke-width="1.2"/>
<line x1="110.67" y1="203" x2="110.67" y2="209" stroke="#0f172a" stroke-width="1.2"/>
<line x1="177.33" y1="203" x2="177.33" y2="209" stroke="#0f172a" stroke-width="1.2"/>
<line x1="244" y1="203" x2="244" y2="209" stroke="#0f172a" stroke-width="1.2"/>
<line x1="310.67" y1="203" x2="310.67" y2="209" stroke="#0f172a" stroke-width="1.2"/>
<line x1="41" y1="206" x2="47" y2="206" stroke="#0f172a" stroke-width="1.2"/>
<line x1="41" y1="56" x2="47" y2="56" stroke="#0f172a" stroke-width="1.2"/>
<g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="50.67" y="222" text-anchor="middle" fill="#0f172a" font-size="11">1</text><text x="110.67" y="222" text-anchor="middle" fill="#0f172a" font-size="11">10</text><text x="177.33" y="222" text-anchor="middle" fill="#0f172a" font-size="11">20</text><text x="244" y="222" text-anchor="middle" fill="#0f172a" font-size="11">30</text><text x="310.67" y="222" text-anchor="middle" fill="#0f172a" font-size="11">40</text><text x="37" y="210" text-anchor="end" fill="#0f172a" font-size="11">0</text><text x="37" y="60" text-anchor="end" fill="#0f172a" font-size="11">5</text><text x="318" y="198" text-anchor="middle" fill="#0f172a" font-size="12">n</text><text x="56" y="14" text-anchor="start" fill="#0f172a" font-size="12">tₙ</text><text x="312" y="50" text-anchor="end" fill="#0f6e56" font-size="12">5</text><text x="137.33" y="74" text-anchor="middle" fill="#475569" font-size="11">borne haute</text><text x="204" y="99" text-anchor="middle" fill="#475569" font-size="11">borne basse</text></g>
</svg>
:::

Les courbes grises sont les suites (5n − 2)/(n + 4) et (5n + 2)/(n + 4) de l'exemple : elles prennent tₙ en étau.

::: exemple Les gendarmes

1. Pour tout n, −1 ≤ cos n ≤ 1, donc −2 ≤ 2 cos n ≤ 2.
2. On ajoute 5n puis on divise par n + 4 > 0 : (5n − 2)/(n + 4) ≤ tₙ ≤ (5n + 2)/(n + 4).
3. Les deux bornes tendent vers 5, rapport des coefficients dominants 5n/n.
4. D'après le théorème des gendarmes, lim tₙ = 5.

:::

::: exemple Une minoration qui pousse vers +∞

1. bₙ = n + 3 sin n. Comme sin n ≥ −1, bₙ ≥ n − 3 pour tout n.
2. n − 3 → +∞.
3. Une suite supérieure à une suite qui tend vers +∞ tend vers +∞ : lim bₙ = +∞, sans calculer sin n.

:::

::: exemple Une factorielle

1. aₙ = 6ⁿ/n!, n ≥ 1. aₙ₊₁/aₙ = 6/(n + 1) car (n + 1)! = (n + 1) n!.
2. Pour n ≥ 11, 6/(n + 1) ≤ 6/12 = 1/2, donc aₙ₊₁ ≤ aₙ/2.
3. Par récurrence, 0 < aₙ ≤ (1/2)ⁿ⁻¹¹ a₁₁ pour n ≥ 11, et (1/2)ⁿ⁻¹¹ → 0.
4. Par encadrement, lim 6ⁿ/n! = 0 : la factorielle l'emporte sur l'exponentielle.

:::

::: piege
**Erreur : garder l'inégalité stricte à la limite.** On a 1/(2n) < 1/n pour tout n ≥ 1, et l'on conclut que lim 1/(2n) < lim 1/n. L'erreur tente parce que chaque terme est strictement plus petit que l'autre. Mais les deux limites valent 0 : une inégalité large uₙ ≤ vₙ donne a ≤ b, et même une inégalité stricte uₙ < vₙ ne donne que a ≤ b.
:::

::: propriete
**Résultats de comparaison (admis)**, pour n ≥ N₀ :
**Ordre** : si uₙ ≤ vₙ, lim uₙ = a et lim vₙ = b, alors a ≤ b.
**Gendarmes** : si vₙ ≤ uₙ ≤ wₙ et lim vₙ = lim wₙ = a, alors lim uₙ = a.
**Valeur absolue** : si 0 ≤ |uₙ| ≤ vₙ et lim vₙ = 0, alors lim uₙ = 0.
**Vers l'infini** : si uₙ ≤ vₙ et lim uₙ = +∞, alors lim vₙ = +∞ ; si uₙ ≤ vₙ et lim vₙ = −∞, alors lim uₙ = −∞.
Cas limite : les deux bornes doivent avoir la même limite. L'encadrement −1 ≤ (−1)ⁿ ≤ 1 ne dit rien de la limite de (−1)ⁿ, puisque −1 ≠ 1.
:::

::: verifie À toi : la valeur absolue
Calculer lim n→+∞ cos(n²)/(3n + 1).

---

Pour tout n, |cos(n²)| ≤ 1, donc 0 ≤ |uₙ| ≤ 1/(3n + 1). La borne 1/(3n + 1) tend vers 0, donc, d'après le résultat sur la valeur absolue, lim uₙ = 0.
:::

::: retenir
Une suite coincée entre deux suites de même limite a cette limite ; une minoration par une suite qui tend vers +∞ suffit à tendre vers +∞ ; les inégalités strictes deviennent larges.
:::

## 🧱 Suites monotones et sommes Σ

On colle côte à côte des bandes de papier sur une table de 2 m. La k-ième bande a pour largeur 1/k² mètre : 1 ; 0,25 ; 0,11 ; 0,06 ; … La largeur totale Sₙ = 1 + 1/4 + 1/9 + … + 1/n² vaut 1 ; 1,25 ; 1,36 ; 1,42 ; 1,46 pour n = 1 à 5.
Les bandes dépasseront-elles la table, ou la largeur totale se stabilise-t-elle ?

::: figure Les points (n ; Sₙ) montent d'un rang à l'autre mais restent sous la droite y = 2 : la largeur totale ne sort pas de la table
<svg viewBox="0 0 340 236">
<title>Les points (n ; Sₙ) pour Sₙ = 1 + 1/4 + … + 1/n² : ils montent d'un rang au suivant sans jamais atteindre la droite y = 2</title>
<line x1="44" y1="206" x2="326" y2="206" stroke="#0f172a" stroke-width="1.6"/>
<line x1="44" y1="214" x2="44" y2="12" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="326,206 318,202 318,210" fill="#0f172a"/>
<polygon points="44,12 40,20 48,20" fill="#0f172a"/>
<line x1="44" y1="42.36" x2="316" y2="42.36" stroke="#0f6e56" stroke-width="1.6" stroke-dasharray="6 3"/>
<line x1="69.66" y1="203" x2="69.66" y2="209" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="69.66" cy="124.18" r="3.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<line x1="95.32" y1="203" x2="95.32" y2="209" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="95.32" cy="103.73" r="3.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<line x1="120.98" y1="203" x2="120.98" y2="209" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="120.98" cy="94.64" r="3.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<line x1="146.64" y1="203" x2="146.64" y2="209" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="146.64" cy="89.52" r="3.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<line x1="172.3" y1="203" x2="172.3" y2="209" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="172.3" cy="86.25" r="3.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<line x1="197.96" y1="203" x2="197.96" y2="209" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="197.96" cy="83.98" r="3.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<line x1="223.62" y1="203" x2="223.62" y2="209" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="223.62" cy="82.31" r="3.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<line x1="249.28" y1="203" x2="249.28" y2="209" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="249.28" cy="81.03" r="3.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<line x1="274.94" y1="203" x2="274.94" y2="209" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="274.94" cy="80.02" r="3.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<line x1="300.6" y1="203" x2="300.6" y2="209" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="300.6" cy="79.2" r="3.6" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<line x1="41" y1="206" x2="47" y2="206" stroke="#0f172a" stroke-width="1.2"/>
<line x1="41" y1="124.18" x2="47" y2="124.18" stroke="#0f172a" stroke-width="1.2"/>
<line x1="41" y1="42.36" x2="47" y2="42.36" stroke="#0f172a" stroke-width="1.2"/>
<g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="69.66" y="222" text-anchor="middle" fill="#0f172a" font-size="11">1</text><text x="95.32" y="222" text-anchor="middle" fill="#0f172a" font-size="11">2</text><text x="120.98" y="222" text-anchor="middle" fill="#0f172a" font-size="11">3</text><text x="146.64" y="222" text-anchor="middle" fill="#0f172a" font-size="11">4</text><text x="172.3" y="222" text-anchor="middle" fill="#0f172a" font-size="11">5</text><text x="197.96" y="222" text-anchor="middle" fill="#0f172a" font-size="11">6</text><text x="223.62" y="222" text-anchor="middle" fill="#0f172a" font-size="11">7</text><text x="249.28" y="222" text-anchor="middle" fill="#0f172a" font-size="11">8</text><text x="274.94" y="222" text-anchor="middle" fill="#0f172a" font-size="11">9</text><text x="300.6" y="222" text-anchor="middle" fill="#0f172a" font-size="11">10</text><text x="37" y="210" text-anchor="end" fill="#0f172a" font-size="11">0</text><text x="37" y="128.18" text-anchor="end" fill="#0f172a" font-size="11">1</text><text x="37" y="46.36" text-anchor="end" fill="#0f172a" font-size="11">2</text><text x="318" y="198" text-anchor="middle" fill="#0f172a" font-size="12">n</text><text x="56" y="14" text-anchor="start" fill="#0f172a" font-size="12">Sₙ</text><text x="312" y="36.36" text-anchor="end" fill="#0f6e56" font-size="12">2</text></g>
</svg>
:::

La droite y = 2 de la figure est le majorant que l'on cherche à prouver pour tous les n, et pas seulement sur les dix premiers points.

::: definition
Pour des réels a₁, a₂, …, aₙ, on note Σ k=1→n aₖ = a₁ + a₂ + … + aₙ, que l'on lit « somme des aₖ pour k variant de 1 à n ».
:::

::: exemple La largeur totale reste sous 2

1. Sₙ₊₁ − Sₙ = 1/(n + 1)² > 0 : (Sₙ) est croissante.
2. Pour k ≥ 2, 1/(k − 1) − 1/k = 1/(k(k − 1)) ≥ 1/k², donc 1/k² ≤ 1/(k − 1) − 1/k.
3. On somme de k = 2 à n : les termes intermédiaires s'annulent deux à deux (on dit que la somme se télescope), d'où Σ k=2→n 1/k² ≤ 1 − 1/n.
4. Sₙ ≤ 1 + 1 − 1/n = 2 − 1/n < 2 : (Sₙ) est majorée par 2.
5. Croissante et majorée, (Sₙ) converge vers un réel ℓ. Comme (Sₙ) est croissante, ℓ ≥ S₃ = 49/36 ; comme Sₙ ≤ 2, ℓ ≤ 2 par comparaison avec la suite constante 2.

:::

::: exemple Une somme qui se télescope exactement

1. 1/(k(k + 1)) = 1/k − 1/(k + 1), car 1/k − 1/(k + 1) = ((k + 1) − k)/(k(k + 1)).
2. Σ k=1→n 1/(k(k + 1)) = (1 − 1/2) + (1/2 − 1/3) + … + (1/n − 1/(n + 1)) = 1 − 1/(n + 1).
3. 1/(n + 1) → 0, donc la somme tend vers 1.

:::

::: exemple Une suite croissante non majorée

1. Tₙ = Σ k=1→n 1/√k est croissante : on ajoute 1/√(n + 1) > 0.
2. Chacun des n termes vaut au moins 1/√n, car k ≤ n donne √k ≤ √n. Donc Tₙ ≥ n × 1/√n = √n.
3. √n → +∞ : par comparaison, Tₙ → +∞. Une suite croissante qui n'est pas majorée tend vers +∞.

:::

::: piege
**Erreur : prendre le majorant pour la limite.** On a montré Sₙ ≤ 2 et l'on écrit lim Sₙ = 2. L'erreur tente parce que 2 est le plafond que l'on vient d'atteindre dans la preuve. Mais Sₙ est aussi majorée par 3 et par 100 : le théorème garantit seulement l'existence d'une limite ℓ, et ici 49/36 ≤ ℓ ≤ 2. La figure le montre : au rang 10, Sₙ vaut environ 1,55, loin de 2.
:::

::: propriete
**Théorème (admis)** : si (uₙ) est croissante et majorée, elle converge vers un réel a et uₙ ≤ a pour tout n ; si elle est croissante et non majorée, elle tend vers +∞.
Si (uₙ) est décroissante et minorée, elle converge vers un réel b et uₙ ≥ b pour tout n ; si elle est décroissante et non minorée, elle tend vers −∞.
Cas limite : chaque hypothèse compte. uₙ = n est croissante sans converger, car non majorée ; (−1)ⁿ est bornée sans converger, car non monotone.
:::

::: verifie À toi : majorer par télescopage
Montrer que Tₙ = Σ k=1→n 1/(k + 1)² converge, sachant que 1/(k + 1)² ≤ 1/k − 1/(k + 1) pour k ≥ 1.

---

Tₙ₊₁ − Tₙ = 1/(n + 2)² > 0 : (Tₙ) est croissante. En sommant l'inégalité donnée de k = 1 à n, les termes se télescopent : Tₙ ≤ 1 − 1/(n + 1) < 1. Croissante et majorée par 1, (Tₙ) converge, d'après le théorème de convergence monotone.
:::

::: retenir
Une suite croissante et majorée, ou décroissante et minorée, converge ; le théorème donne l'existence de la limite, pas sa valeur.
:::

## 🎯 Suites récurrentes et point fixe

Un tableur calcule les termes de uₙ₊₁ = uₙ(uₙ − 1) à partir de u₁. Selon le départ, la suite finit ailleurs : u₁ = 0 reste en 0 ; u₁ = 2 reste en 2 ; u₁ = 1 donne u₂ = 0 ; u₁ = −1 donne u₂ = 2 ; u₁ = 0,5 donne 0,5 ; −0,25 ; 0,31 ; −0,21 ; … qui se resserre sur 0 ; u₁ = 4 donne 4 ; 12 ; 132 ; … qui monte sans fin.
Les valeurs 0 et 2 reviennent sans cesse : d'où viennent-elles, et quand la suite y arrive-t-elle vraiment ?

::: figure L'escalier de u₀ = 2 et uₙ₊₁ = √(3uₙ + 4) : les marches montent vers l'abscisse ℓ = 4 du point où la courbe et la droite y = x se coupent
<svg viewBox="0 0 340 236">
<title>Escalier de la suite u₀ = 2, uₙ₊₁ = √(3uₙ + 4) entre la courbe y = f(x) et la droite y = x : les marches montent vers le point d'abscisse ℓ = 4</title>
<line x1="44" y1="206" x2="326" y2="206" stroke="#0f172a" stroke-width="1.6"/>
<line x1="44" y1="214" x2="44" y2="12" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="326,206 318,202 318,210" fill="#0f172a"/>
<polygon points="44,12 40,20 48,20" fill="#0f172a"/>
<line x1="44" y1="206" x2="316" y2="26" stroke="#94a3b8" stroke-width="1.6" stroke-dasharray="6 4"/>
<polyline points="44,127.74 46.96,126.29 49.91,124.86 52.87,123.45 55.83,122.07 58.78,120.72 61.74,119.38 64.7,118.07 67.65,116.77 70.61,115.49 73.57,114.23 76.52,112.99 79.48,111.76 82.43,110.55 85.39,109.35 88.35,108.17 91.3,107.01 94.26,105.85 97.22,104.71 100.17,103.59 103.13,102.47 106.09,101.37 109.04,100.28 112,99.19 114.96,98.12 117.91,97.07 120.87,96.02 123.83,94.98 126.78,93.95 129.74,92.93 132.7,91.92 135.65,90.91 138.61,89.92 141.57,88.94 144.52,87.96 147.48,86.99 150.43,86.03 153.39,85.07 156.35,84.13 159.3,83.19 162.26,82.26 165.22,81.33 168.17,80.42 171.13,79.51 174.09,78.6 177.04,77.7 180,76.81 182.96,75.92 185.91,75.04 188.87,74.17 191.83,73.3 194.78,72.44 197.74,71.58 200.7,70.73 203.65,69.88 206.61,69.04 209.57,68.21 212.52,67.38 215.48,66.55 218.43,65.73 221.39,64.91 224.35,64.1 227.3,63.29 230.26,62.49 233.22,61.69 236.17,60.9 239.13,60.11 242.09,59.33 245.04,58.55 248,57.77 250.96,57 253.91,56.23 256.87,55.46 259.83,54.7 262.78,53.94 265.74,53.19 268.7,52.44 271.65,51.7 274.61,50.95 277.57,50.21 280.52,49.48 283.48,48.75 286.43,48.02 289.39,47.29 292.35,46.57 295.3,45.85 298.26,45.14 301.22,44.42 304.17,43.71 307.13,43.01 310.09,42.31 313.04,41.61 316,40.91" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linecap="round"/>
<polyline points="162.26,206 162.26,82.26 230.99,82.26 230.99,62.3 261.15,62.3 261.15,54.36 273.14,54.36" fill="none" stroke="#b45309" stroke-width="2" stroke-linejoin="round"/>
<circle cx="280.52" cy="49.48" r="4" fill="#0f172a" stroke="#0f172a" stroke-width="1.2"/>
<line x1="280.52" y1="49.48" x2="280.52" y2="206" stroke="#94a3b8" stroke-width="1.1" stroke-dasharray="3 3"/>
<line x1="162.26" y1="203" x2="162.26" y2="209" stroke="#0f172a" stroke-width="1.2"/>
<line x1="230.99" y1="203" x2="230.99" y2="209" stroke="#0f172a" stroke-width="1.2"/>
<line x1="261.15" y1="203" x2="261.15" y2="209" stroke="#0f172a" stroke-width="1.2"/>
<g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="162.26" y="222" text-anchor="middle" fill="#b45309" font-size="11">u₀</text><text x="230.99" y="222" text-anchor="middle" fill="#b45309" font-size="11">u₁</text><text x="261.15" y="222" text-anchor="middle" fill="#b45309" font-size="11">u₂</text><text x="284.52" y="222" text-anchor="middle" fill="#0f172a" font-size="12">ℓ</text><text x="97.22" y="92.71" text-anchor="middle" fill="#0f6e56" font-size="12">y = f(x)</text><text x="221.39" y="110.61" text-anchor="middle" fill="#475569" font-size="12">y = x</text><text x="318" y="198" text-anchor="middle" fill="#0f172a" font-size="12">x</text><text x="56" y="14" text-anchor="start" fill="#0f172a" font-size="12">y</text></g>
</svg>
:::

Les abscisses u₀, u₁, u₂ de l'escalier sont les valeurs 2 ; 3,16 ; 3,67 de la suite uₙ₊₁ = √(3uₙ + 4) (exemple ci-dessous), et l'abscisse ℓ de l'intersection est le seul candidat pour la limite.

::: exemple La limite de l'escalier

1. Par récurrence, 2 ≤ uₙ ≤ 4. Initialisation : u₀ = 2. Hérédité : de 2 ≤ uₙ ≤ 4 on tire 10 ≤ 3uₙ + 4 ≤ 16, donc √10 ≤ uₙ₊₁ ≤ 4, et √10 > 2.
2. uₙ₊₁² − uₙ² = 3uₙ + 4 − uₙ² = (4 − uₙ)(uₙ + 1) ≥ 0 car uₙ ≤ 4. Les termes sont positifs, donc uₙ₊₁ ≥ uₙ : (uₙ) est croissante.
3. Croissante et majorée par 4, (uₙ) converge vers un réel ℓ.
4. f(x) = √(3x + 4) est continue, donc ℓ = √(3ℓ + 4), soit ℓ² − 3ℓ − 4 = (ℓ − 4)(ℓ + 1) = 0 : ℓ = 4 ou ℓ = −1.
5. uₙ ≥ 2 pour tout n donne ℓ ≥ 2 par comparaison avec la suite constante 2 : on écarte −1, et ℓ = 4.

:::

::: exemple Une suite homographique

1. u₀ = 1 et uₙ₊₁ = (3uₙ + 4)/(uₙ + 3). Les points fixes vérifient x² + 3x = 3x + 4, soit x² = 4 : x = 2 ou x = −2.
2. Tous les termes sont positifs (par récurrence, f(x) = (3x + 4)/(x + 3) > 0 pour x ≥ 0). On pose vₙ = (uₙ − 2)/(uₙ + 2).
3. uₙ₊₁ − 2 = (uₙ − 2)/(uₙ + 3) et uₙ₊₁ + 2 = 5(uₙ + 2)/(uₙ + 3), donc vₙ₊₁ = vₙ/5 : suite géométrique de raison 1/5, avec v₀ = −1/3.
4. vₙ = −(1/3)(1/5)ⁿ → 0. En résolvant vₙ = (uₙ − 2)/(uₙ + 2), on obtient uₙ = 2(1 + vₙ)/(1 − vₙ).
5. lim uₙ = 2(1 + 0)/(1 − 0) = 2. Contrôle : v₁ = −1/15 donne u₁ = 2(14/15)/(16/15) = 7/4 ✓.

:::

::: piege
**Erreur : conclure à partir du seul point fixe.** Pour uₙ₊₁ = uₙ(uₙ − 1), l'équation x(x − 1) = x donne x = 0 ou x = 2, et l'on écrit que la suite de premier terme u₁ = 4 tend vers 0 ou 2. L'erreur tente parce que ces deux valeurs sont les seules possibles si la suite converge. Mais 4 ; 12 ; 132 ; … tend vers +∞ : sans convergence démontrée, l'équation ne dit rien.
:::

::: propriete
**Théorème** : soit (uₙ) vérifiant uₙ₊₁ = f(uₙ) pour n ≥ 0. Si (uₙ) converge vers un réel a et si f est continue en a, alors a = f(a).
Preuve : (uₙ₊₁) converge aussi vers a ; f est continue en a, donc (f(uₙ)) converge vers f(a) ; comme uₙ₊₁ = f(uₙ), l'unicité de la limite donne a = f(a).
Cas limite : l'équation f(x) = x peut avoir plusieurs solutions, comme 0 et 2 ci-dessus ou 4 et −1 dans l'escalier. C'est la suite elle-même, par son encadrement, qui désigne la bonne ; la convergence se démontre d'abord.
:::

::: verifie À toi : une limite par point fixe
u₀ = 1 et uₙ₊₁ = √(5uₙ + 6). On admet que (uₙ) est croissante et majorée par 6. Déterminer sa limite.

---

Croissante et majorée, (uₙ) converge vers un réel ℓ. La fonction f(x) = √(5x + 6) est continue, donc ℓ = √(5ℓ + 6), d'où ℓ² − 5ℓ − 6 = (ℓ − 6)(ℓ + 1) = 0. Comme uₙ ≥ u₀ = 1 pour tout n, ℓ ≥ 1 et ℓ = 6.
:::

::: retenir
Pour uₙ₊₁ = f(uₙ), on prouve d'abord que (uₙ) converge, puis on résout f(ℓ) = ℓ et l'on garde la solution compatible avec l'encadrement de la suite.
:::

## 🤝 Suites adjacentes

Un randonneur avance de 1 km, recule de 1/√2 km, avance de 1/√3 km, recule de 1/√4 km, et ainsi de suite, avec des pas qui rétrécissent. Sa position après n pas est uₙ = 1 − 1/√2 + 1/√3 − … + (−1)ⁿ⁺¹/√n : environ 1 ; 0,29 ; 0,87 ; 0,37 ; 0,82 ; 0,41 pour n = 1 à 6.
Les positions après un nombre pair de pas montent, celles après un nombre impair de pas descendent : le randonneur est-il enfermé quelque part ?

::: figure Les rangs pairs (orange) avancent par la gauche, les rangs impairs (vert) reculent par la droite : tous enferment le même réel α
<svg viewBox="0 0 350 136">
<title>Sur la droite graduée, les rangs pairs u₂, u₄, u₆ montent par la gauche et les rangs impairs u₁, u₃, u₅, u₇ descendent par la droite : tous enferment le même réel α</title>
<line x1="22" y1="86" x2="344" y2="86" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="344,86 336,82 336,90" fill="#0f172a"/>
<line x1="211.47" y1="62" x2="211.47" y2="86" stroke="#0f172a" stroke-width="1.6"/>
<circle cx="330" cy="86" r="3.8" fill="#0f6e56" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="117.87" cy="86" r="3.8" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="291.07" cy="86" r="3.8" fill="#0f6e56" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="141.07" cy="86" r="3.8" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="275.24" cy="86" r="3.8" fill="#0f6e56" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="152.76" cy="86" r="3.8" fill="#d97706" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="266.15" cy="86" r="3.8" fill="#0f6e56" stroke="#0f172a" stroke-width="1.2"/>
<g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="211.47" y="54" text-anchor="middle" fill="#0f172a" font-size="13">α</text><text x="330" y="72" text-anchor="middle" fill="#0f6e56" font-size="11">u₁</text><text x="117.87" y="106" text-anchor="middle" fill="#d97706" font-size="11">u₂</text><text x="291.07" y="72" text-anchor="middle" fill="#0f6e56" font-size="11">u₃</text><text x="141.07" y="106" text-anchor="middle" fill="#d97706" font-size="11">u₄</text><text x="275.24" y="72" text-anchor="middle" fill="#0f6e56" font-size="11">u₅</text></g>
</svg>
:::

Le réel α de la figure est la position que le randonneur approche sans l'atteindre ; il est toujours entre un rang pair et le rang impair suivant.

::: exemple La position du randonneur

1. Entre deux rangs pairs, on ajoute 1/√(2n + 1) − 1/√(2n + 2) > 0 : u₂ₙ₊₂ > u₂ₙ, donc (u₂ₙ) est croissante.
2. Entre deux rangs impairs, on ajoute −1/√(2n + 2) + 1/√(2n + 3) < 0 : u₂ₙ₊₃ < u₂ₙ₊₁, donc (u₂ₙ₊₁) est décroissante.
3. u₂ₙ₊₁ − u₂ₙ = 1/√(2n + 1) > 0, donc u₂ₙ ≤ u₂ₙ₊₁, et cette différence tend vers 0.
4. Les suites (u₂ₙ) et (u₂ₙ₊₁) sont adjacentes : elles convergent vers une même limite α. Les rangs pairs et impairs ayant la même limite, lim uₙ = α.
5. u₂ₙ ≤ α ≤ u₂ₙ₊₁ pour tout n. Pour n = 2, u₄ ≈ 0,370 ≤ α ≤ u₅ ≈ 0,817.

:::

::: exemple Deux suites explicites

1. aₙ = 5 − 3/n et bₙ = 5 + 2/n², n ≥ 1. Pour tout n, aₙ ≤ 5 ≤ bₙ, donc aₙ ≤ bₙ.
2. (aₙ) est croissante, car −3/n augmente avec n ; (bₙ) est décroissante, car 2/n² diminue.
3. bₙ − aₙ = 3/n + 2/n² → 0.
4. Les trois conditions sont réunies : (aₙ) et (bₙ) sont adjacentes et convergent vers la même limite 5.

:::

::: piege
**Erreur : croire que deux suites de même limite sont adjacentes.** Pour uₙ = 1/n et vₙ = 2/n, on a lim uₙ = lim vₙ = 0, donc « elles sont adjacentes ». L'erreur tente parce que les adjacentes ont bien une limite commune. Mais (uₙ) est décroissante, et non croissante : deux suites qui se rapprochent par le haut ne se « pincent » pas, et la définition n'est pas satisfaite.
:::

::: propriete
**Définition et théorème** : (uₙ) et (vₙ) sont adjacentes lorsque uₙ ≤ vₙ pour tout n, que (uₙ) est croissante, que (vₙ) est décroissante et que (vₙ − uₙ) converge vers 0. Alors elles convergent vers la même limite.
Preuve : (vₙ) est décroissante, donc uₙ ≤ vₙ ≤ v₀ : (uₙ) est croissante et majorée, donc converge vers a. De même (vₙ) est minorée par u₀ et converge vers b. Enfin vₙ = (vₙ − uₙ) + uₙ donne b = 0 + a.
Cas limite : si vₙ − uₙ ne tend pas vers 0, les deux suites peuvent converger vers des limites différentes, comme uₙ = 1 − 1/n et vₙ = 2 + 1/n.
:::

::: verifie À toi : vérifier trois conditions
Montrer que uₙ = 7 − 4/n et vₙ = 7 + 3/(n + 1), n ≥ 1, sont adjacentes.

---

uₙ ≤ 7 ≤ vₙ, donc uₙ ≤ vₙ. (uₙ) est croissante car −4/n augmente ; (vₙ) est décroissante car 3/(n + 1) diminue. Enfin vₙ − uₙ = 4/n + 3/(n + 1) → 0. Les trois conditions sont réunies : les suites sont adjacentes, de limite commune 7.
:::

::: retenir
Deux suites sont adjacentes quand l'une croît, l'autre décroît, la première reste sous la seconde et leur écart tend vers 0 ; elles ont alors la même limite, qui se trouve entre uₙ et vₙ.
:::

> 🏆 Tu sais maintenant lire la destination d'une suite : l'encadrer, la comparer, prouver qu'elle converge par la monotonie, puis capturer sa limite par le point fixe ou l'adjacence. Ces armes serviront dans tout le reste de l'Analyse.
