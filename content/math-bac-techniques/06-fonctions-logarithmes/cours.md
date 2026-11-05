# ⚔️ Fonctions logarithmes — le produit qui devient somme

> 💡 «Multiplier deux nombres, c'est additionner leurs logarithmes : une fonction née d'une simple dérivée devient le plus lent et le plus fidèle des calculateurs.»

Ce chapitre construit une fonction que ni les polynômes ni les racines ne fournissent : celle dont la dérivée est 1/x. Huit notions, dans l'ordre où elles s'appellent, avec un fil rouge : un mobile se déplace sur une droite graduée ; à l'instant x > 0 (en secondes) sa vitesse est 1/x (en m/s), et à l'instant 1 il passe par l'origine.

## 🧭 La fonction logarithme népérien

Le mobile ralentit sans jamais s'arrêter : sa vitesse 1/x est de plus en plus petite et toujours positive. Sa position P(x) doit donc vérifier P′(x) = 1/x, puisque la vitesse est la dérivée de la position, et P(1) = 0. Aucune puissance ne convient : (xⁿ)′ = n xⁿ⁻¹ ne donne 1/x = x⁻¹ pour aucun entier n, car il faudrait n = 0 et (x⁰)′ = 0.
Existe-t-il une fonction de dérivée 1/x, et comment la nommer ?

::: definition
La fonction x ↦ 1/x est continue sur ]0 ; +∞[ : elle y admet des primitives (chapitre sur les fonctions primitives). La **fonction logarithme népérien**, notée ln, est la primitive de x ↦ 1/x sur ]0 ; +∞[ qui s'annule en 1. Ainsi, pour tout x > 0 :
$$ ln′(x) = 1/x $$
$$ ln 1 = 0 $$
:::

| x (instant en s) | 0,5 | 1 | 2 | 3 | 10 |
| --- | --- | --- | --- | --- | --- |
| ln x (position en m, valeur approchée) | −0,69 | 0 | 0,69 | 1,10 | 2,30 |

La ligne du bas est la position du mobile à l'instant de la ligne du haut : il est à gauche de l'origine avant l'instant 1, à droite après, et il avance de moins en moins vite, comme le dit la vitesse ln′(x) = 1/x.

::: exemple Le mobile

1. La position est la primitive de la vitesse 1/x qui s'annule à l'instant 1 : c'est ln, par définition.
2. À l'instant 2, la vitesse est ln′(2) = 1/2 m/s, car ln′(x) = 1/x.
3. En x = 1, ln′(1) = 1 et ln 1 = 0, donc la tangente est y = 1 × (x − 1) + 0 = x − 1. Près de l'instant 1, la position est donc proche de x − 1 : pour x = 1,1 on obtient 0,1, et la calculatrice donne ln 1,1 ≈ 0,095.

:::

::: piege
**Erreur : appliquer à 1/x la règle « xⁿ a pour primitive xⁿ⁺¹/(n + 1) ».** Pour 1/x = x⁻¹, il faudrait n = −1 et diviser par n + 1 = 0. La règle tente parce qu'elle réussit pour 1/x² = x⁻², de primitive −1/x (car (−1/x)′ = 1/x²). Mais n = −1 est justement le cas qu'elle exclut : la primitive de 1/x n'est pas une puissance, c'est ln x.
:::

::: propriete
Pour tout x > 0, ln′(x) = 1/x. Les primitives de x ↦ 1/x sur ]0 ; +∞[ sont les fonctions x ↦ ln x + k, où k est une constante réelle. La fonction ln est dérivable, donc continue, sur ]0 ; +∞[.
Cas limite : ln n'est définie que pour x > 0 ; ln 0 et ln(−3) n'existent pas.
:::

::: exemple Le même outil, sans situation : une primitive avec condition

1. Soit f(x) = 2x + 3/x sur ]0 ; +∞[. Une primitive de 2x est x², une primitive de 3/x est 3 ln x (car (3 ln x)′ = 3/x) : donc F(x) = x² + 3 ln x + k.
2. On impose F(1) = 2 : F(1) = 1 + 3 ln 1 + k = 1 + k, car ln 1 = 0. Donc 1 + k = 2 et k = 1.
3. La primitive cherchée est F(x) = x² + 3 ln x + 1.

:::

::: verifie À toi : une primitive qui vaut 3 en 1
Soit g(x) = 4x + 5/x sur ]0 ; +∞[. Détermine la primitive G de g telle que G(1) = 3.

---

Une primitive de 4x est 2x² et une primitive de 5/x est 5 ln x, donc G(x) = 2x² + 5 ln x + k. En x = 1, ln 1 = 0 donne G(1) = 2 + k ; la condition G(1) = 3 impose k = 1. Donc G(x) = 2x² + 5 ln x + 1, et on contrôle G′(x) = 4x + 5/x = g(x).
:::

::: retenir
ln est la primitive de x ↦ 1/x sur ]0 ; +∞[ qui s'annule en 1 : ln′(x) = 1/x et ln 1 = 0.
:::

## 🧮 La propriété fondamentale : le produit devient somme

À l'instant 2 le mobile est à ln 2 ≈ 0,69 m ; à l'instant 4, le double, à ln 4 ≈ 1,39 m ; à l'instant 8, à ln 8 ≈ 2,08 m. À chaque doublement du temps, il avance de la même distance, environ 0,69 m.
Pourquoi cette régularité, et que devient ln(ab) quand on connaît ln a et ln b ?

| instant x | 1 | 2 | 4 | 8 | 16 |
| --- | --- | --- | --- | --- | --- |
| ln x (valeur approchée) | 0 | 0,69 | 1,39 | 2,08 | 2,77 |

Chaque colonne ajoute 0,69 à la précédente alors que l'instant est multiplié par 2 : le tableau montre un produit sur la ligne du haut devenu une somme sur la ligne du bas.

::: exemple Pourquoi ln(2x) = ln x + ln 2

1. Pour x > 0, on pose g(x) = ln(2x), composée de u(x) = 2x et de ln. Alors g′(x) = u′(x) × ln′(u(x)) = 2 × 1/(2x) = 1/x.
2. Les fonctions g et ln ont la même dérivée 1/x sur l'intervalle ]0 ; +∞[ : leur différence a une dérivée nulle, donc elle est constante. Ainsi g(x) = ln x + k.
3. En x = 1 : g(1) = ln 2 et ln 1 = 0, donc ln 2 = 0 + k et k = ln 2.
4. Donc ln(2x) = ln x + ln 2. Par exemple ln 4 = ln(2 × 2) = 2 ln 2 ≈ 1,39 et ln 8 = ln(2 × 4) = ln 4 + ln 2 = 3 ln 2 ≈ 2,08, comme dans le tableau.

:::

::: exemple Le même outil, sans situation : tout exprimer avec a = ln 2 et b = ln 3

1. ln 72 = ln(2³ × 3²) = ln(2³) + ln(3²) = 3a + 2b, car le logarithme d'un produit est la somme des logarithmes et ln(xⁿ) = n ln x.
2. ln(1/12) = −ln 12 = −ln(2² × 3) = −(2a + b), car ln(1/x) = −ln x.
3. ln √18 = (1/2) ln 18 = (1/2) ln(2 × 3²) = (1/2)(a + 2b) = a/2 + b, car √x = x^(1/2) et ln(x^r) = r ln x.
4. Avec a ≈ 0,693 et b ≈ 1,099, on obtient ln 72 ≈ 4,277, ln(1/12) ≈ −2,485 et ln √18 ≈ 1,445.

:::

::: piege
**Erreur : écrire ln(a + b) = ln a + ln b.** La règle transforme un produit en somme, pas une somme en somme. Avec a = 2 et b = 3 : ln(2 + 3) = ln 5 ≈ 1,61, alors que ln 2 + ln 3 ≈ 1,79. L'erreur tente parce que le signe + figure des deux côtés de la règle correcte ln(ab) = ln a + ln b. Mais ce qui entre dans le logarithme est le produit ab, jamais la somme a + b.
:::

::: propriete
**Propriété fondamentale.** Pour tous réels a > 0 et b > 0 :
$$ ln(ab) = ln a + ln b $$
Pour x > 0, y > 0, n entier relatif et r rationnel, on en déduit :
$$ ln(1/x) = −ln x $$
$$ ln(x/y) = ln x − ln y $$
$$ ln(xⁿ) = n ln x $$
$$ ln(x^r) = r ln x $$
En particulier ln √x = (1/2) ln x, et ln(a₁ a₂ … aₙ) = ln a₁ + ln a₂ + … + ln aₙ. On les obtient par la propriété fondamentale : ln x + ln(1/x) = ln 1 = 0 donne ln(1/x) = −ln x, puis ln(x/y) = ln x + ln(1/y) ; ln(xⁿ) = n ln x s'obtient par récurrence, puis pour n négatif avec ln(1/x).
Cas limite : la condition de signe est indispensable. Pour a = b = −2, ln(ab) = ln 4 existe, mais ln(−2) n'existe pas : la règle ne dit rien.
:::

::: verifie À toi : deux écritures avec ln 2
Soit a = ln 2. Exprime ln 0,125 et ln ∛4 en fonction de a.

---

On écrit 0,125 = 1/8 = 2⁻³ : ln 0,125 = ln(2⁻³) = −3 ln 2 = −3a ≈ −2,08, car ln(xⁿ) = n ln x avec n = −3. Pour ∛4 = 4^(1/3) = 2^(2/3), on applique ln(x^r) = r ln x avec r = 2/3 : ln ∛4 = (2/3) ln 2 = 2a/3 ≈ 0,46.
:::

::: retenir
ln(ab) = ln a + ln b pour a > 0 et b > 0, d'où ln(1/a) = −ln a, ln(a/b) = ln a − ln b et ln(aʳ) = r ln a.
:::

## 📈 Variations, limites et courbe de ln

Le mobile n'a jamais une vitesse négative : il avance toujours. Avant l'instant 1 il est à gauche de l'origine (−0,69 m à l'instant 0,5). Un jour, malgré sa vitesse qui s'éteint, dépassera-t-il 100 m ? Où était-il en remontant vers l'instant 0 ? Et à quel instant atteint-il 1 m ? Ce nombre sera noté e.

::: figure La courbe de ln avec ses tangentes en A(1 ; 0), de pente 1, et en B(e ; 1), de pente 1/e
<svg viewBox="0 0 340 262">
<title>Courbe de la fonction ln avec ses tangentes en A(1 ; 0) et B(e ; 1) : la courbe est au-dessous de chacune</title>
<line x1="32" y1="110.28" x2="328" y2="110.28" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="328,110.28 320,114.28 320,106.28" fill="#0f172a"/>
<line x1="32" y1="240" x2="32" y2="12" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="32,12 36,20 28,20" fill="#0f172a"/>
<line x1="70.95" y1="107.28" x2="70.95" y2="113.28" stroke="#0f172a" stroke-width="1.2"/>
<line x1="109.89" y1="107.28" x2="109.89" y2="113.28" stroke="#0f172a" stroke-width="1.2"/>
<line x1="148.84" y1="107.28" x2="148.84" y2="113.28" stroke="#0f172a" stroke-width="1.2"/>
<line x1="187.79" y1="107.28" x2="187.79" y2="113.28" stroke="#0f172a" stroke-width="1.2"/>
<line x1="226.74" y1="107.28" x2="226.74" y2="113.28" stroke="#0f172a" stroke-width="1.2"/>
<line x1="265.68" y1="107.28" x2="265.68" y2="113.28" stroke="#0f172a" stroke-width="1.2"/>
<line x1="304.63" y1="107.28" x2="304.63" y2="113.28" stroke="#0f172a" stroke-width="1.2"/>
<line x1="29" y1="228.21" x2="35" y2="228.21" stroke="#0f172a" stroke-width="1.2"/>
<line x1="29" y1="188.9" x2="35" y2="188.9" stroke="#0f172a" stroke-width="1.2"/>
<line x1="29" y1="149.59" x2="35" y2="149.59" stroke="#0f172a" stroke-width="1.2"/>
<line x1="29" y1="70.97" x2="35" y2="70.97" stroke="#0f172a" stroke-width="1.2"/>
<line x1="29" y1="31.66" x2="35" y2="31.66" stroke="#0f172a" stroke-width="1.2"/>
<line x1="41.74" y1="139.76" x2="164.42" y2="15.93" stroke="#d97706" stroke-width="2.2"/>
<line x1="51.47" y1="103.05" x2="273.47" y2="20.61" stroke="#2563eb" stroke-width="2.2"/>
<polyline points="33.75,232.18 35.09,209.89 36.43,195.75 37.77,185.37 39.1,177.17 40.44,170.39 41.78,164.61 43.12,159.57 44.45,155.1 45.79,151.09 47.13,147.45 48.47,144.12 49.8,141.05 51.14,138.2 52.48,135.55 53.81,133.06 55.15,130.72 56.49,128.51 57.83,126.42 59.16,124.44 60.5,122.55 61.84,120.75 63.18,119.02 64.51,117.37 65.85,115.79 67.19,114.26 68.53,112.8 69.86,111.38 71.2,110.02 72.54,108.7 73.88,107.42 75.21,106.19 76.55,104.99 77.89,103.83 79.23,102.7 80.56,101.6 81.9,100.53 83.24,99.49 84.58,98.48 85.91,97.49 87.25,96.53 88.59,95.59 89.93,94.67 91.26,93.77 92.6,92.9 93.94,92.04 95.28,91.2 96.61,90.38 97.95,89.57 99.29,88.78 100.63,88.01 101.96,87.25 103.3,86.5 104.64,85.77 105.98,85.06 107.31,84.35 108.65,83.66 109.99,82.98 111.33,82.31 112.66,81.65 114,81.01 115.34,80.37 116.68,79.75 118.01,79.13 119.35,78.52 120.69,77.93 122.03,77.34 123.36,76.76 124.7,76.19 126.04,75.62 127.38,75.07 128.71,74.52 130.05,73.98 131.39,73.45 132.73,72.92 134.06,72.4 135.4,71.89 136.74,71.39 138.08,70.89 139.41,70.4 140.75,69.91 142.09,69.43 143.43,68.95 144.76,68.49 146.1,68.02 147.44,67.56 148.78,67.11 150.11,66.66 151.45,66.22 152.79,65.78 154.13,65.35 155.46,64.92 156.8,64.5 158.14,64.08 159.48,63.66 160.81,63.25 162.15,62.85 163.49,62.45 164.83,62.05 166.16,61.65 167.5,61.26 168.84,60.88 170.18,60.5 171.51,60.12 172.85,59.74 174.19,59.37 175.53,59 176.86,58.64 178.2,58.28 179.54,57.92 180.88,57.56 182.21,57.21 183.55,56.86 184.89,56.52 186.23,56.18 187.56,55.84 188.9,55.5 190.24,55.17 191.58,54.84 192.91,54.51 194.25,54.18 195.59,53.86 196.93,53.54 198.26,53.22 199.6,52.91 200.94,52.59 202.28,52.28 203.61,51.98 204.95,51.67 206.29,51.37 207.63,51.07 208.96,50.77 210.3,50.47 211.64,50.18 212.98,49.89 214.31,49.6 215.65,49.31 216.99,49.03 218.33,48.74 219.66,48.46 221,48.18 222.34,47.91 223.68,47.63 225.01,47.36 226.35,47.09 227.69,46.82 229.03,46.55 230.36,46.28 231.7,46.02 233.04,45.76 234.38,45.5 235.71,45.24 237.05,44.98 238.39,44.72 239.73,44.47 241.06,44.22 242.4,43.97 243.74,43.72 245.08,43.47 246.41,43.22 247.75,42.98 249.09,42.74 250.43,42.5 251.76,42.26 253.1,42.02 254.44,41.78 255.78,41.54 257.11,41.31 258.45,41.08 259.79,40.85 261.13,40.62 262.46,40.39 263.8,40.16 265.14,39.93 266.48,39.71 267.81,39.48 269.15,39.26 270.49,39.04 271.83,38.82 273.16,38.6 274.5,38.39 275.84,38.17 277.18,37.95 278.51,37.74 279.85,37.53 281.19,37.32 282.53,37.11 283.86,36.9 285.2,36.69 286.54,36.48 287.88,36.27 289.21,36.07 290.55,35.87 291.89,35.66 293.23,35.46 294.56,35.26 295.9,35.06 297.24,34.86 298.58,34.66 299.91,34.47 301.25,34.27 302.59,34.08 303.93,33.88 305.26,33.69 306.6,33.5 307.94,33.31 309.28,33.12 310.61,32.93 311.95,32.74 313.29,32.55 314.63,32.37 315.96,32.18 317.3,32 318.64,31.81 319.98,31.63 321.31,31.45 322.65,31.27 323.99,31.09 325.33,30.91 326.66,30.73 328,30.55" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round"/>
<line x1="137.87" y1="110.28" x2="137.87" y2="70.97" stroke="#64748b" stroke-width="1.4" stroke-dasharray="5 4"/>
<line x1="32" y1="70.97" x2="137.87" y2="70.97" stroke="#64748b" stroke-width="1.4" stroke-dasharray="5 4"/>
<circle cx="70.95" cy="110.28" r="4" fill="#0f172a" stroke="#ffffff" stroke-width="1.2"/>
<circle cx="137.87" cy="70.97" r="4" fill="#0f172a" stroke="#ffffff" stroke-width="1.2"/>
<g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="70.95" y="125.28" text-anchor="middle" fill="#0f172a" font-size="10">1</text><text x="109.89" y="125.28" text-anchor="middle" fill="#0f172a" font-size="10">2</text><text x="148.84" y="125.28" text-anchor="middle" fill="#0f172a" font-size="10">3</text><text x="187.79" y="125.28" text-anchor="middle" fill="#0f172a" font-size="10">4</text><text x="226.74" y="125.28" text-anchor="middle" fill="#0f172a" font-size="10">5</text><text x="265.68" y="125.28" text-anchor="middle" fill="#0f172a" font-size="10">6</text><text x="304.63" y="125.28" text-anchor="middle" fill="#0f172a" font-size="10">7</text><text x="25" y="231.71" text-anchor="end" fill="#0f172a" font-size="10">−3</text><text x="25" y="192.4" text-anchor="end" fill="#0f172a" font-size="10">−2</text><text x="25" y="153.09" text-anchor="end" fill="#0f172a" font-size="10">−1</text><text x="25" y="74.47" text-anchor="end" fill="#0f172a" font-size="10">1</text><text x="25" y="35.16" text-anchor="end" fill="#0f172a" font-size="10">2</text><text x="326" y="104.28" text-anchor="end" fill="#0f172a" font-size="12">x</text><text x="40" y="22" text-anchor="start" fill="#0f172a" font-size="12">y</text><text x="82" y="126" text-anchor="start" fill="#0f172a" font-size="12">A</text><text x="144.88" y="85.9" text-anchor="start" fill="#0f172a" font-size="12">B</text><text x="137.87" y="127.97" text-anchor="middle" fill="#0f172a" font-size="11">e</text><text x="226.74" y="66.25" text-anchor="start" fill="#0f6e56" font-size="12">y = ln x</text><text x="277.37" y="21.83" text-anchor="start" fill="#2563eb" font-size="12">y = x/e</text><text x="111.84" y="37.55" text-anchor="end" fill="#d97706" font-size="12">y = x − 1</text></g>
</svg>
:::

La pente de chaque tangente est la vitesse du mobile : 1 en A (x = 1) et 1/e ≈ 0,37 en B (x = e), plus petite car la vitesse 1/x diminue. La courbe monte sans jamais redescendre, très abrupte près de l'axe des ordonnées, très lente vers la droite.

::: exemple Le mobile, de l'instant 0 à l'infini

1. ln′(x) = 1/x > 0 sur ]0 ; +∞[ : ln est strictement croissante. Comme ln 1 = 0, ln x < 0 pour 0 < x < 1 et ln x > 0 pour x > 1.
2. En +∞ : ln 2 ≈ 0,69 > 0 et ln(2ⁿ) = n ln 2, donc ln(2¹⁴⁵) ≈ 145 × 0,693 ≈ 100,5 > 100. Comme ln est croissante, ln x > 100 pour tout x ≥ 2¹⁴⁵. Le même raisonnement vaut pour toute hauteur : lim x→+∞ ln x = +∞.
3. En 0⁺ : ln x = −ln(1/x), car ln(1/x) = −ln x. Quand x tend vers 0⁺, t = 1/x tend vers +∞, donc ln t tend vers +∞ et ln x = −ln t tend vers −∞ : lim x→0⁺ ln x = −∞.
4. ln est continue, strictement croissante, de limites −∞ et +∞ : par le théorème de la bijection, c'est une bijection de ]0 ; +∞[ sur ℝ. Le réel 1 a donc un unique antécédent, noté e : ln e = 1.
5. ln 2 ≈ 0,69 < 1 < 1,10 ≈ ln 3 et ln est croissante, donc 2 < e < 3 (e ≈ 2,718).

:::

::: exemple Le même outil, sans situation : la courbe est sous sa tangente en A

1. Soit g(x) = x − 1 − ln x sur ]0 ; +∞[. Alors g′(x) = 1 − 1/x = (x − 1)/x, qui a le signe de x − 1 puisque x > 0.
2. g décroît sur ]0 ; 1] et croît sur [1 ; +∞[ : son minimum est g(1) = 1 − 1 − ln 1 = 0.
3. Donc g(x) ≥ 0, c'est-à-dire ln x ≤ x − 1 pour tout x > 0, avec égalité seulement en x = 1 : la courbe de ln est au-dessous de sa tangente en A, qui est la droite y = x − 1.

:::

::: piege
**Erreur : croire que ln est bornée parce que sa vitesse 1/x tend vers 0.** Une dérivée qui tend vers 0 ne force pas la fonction à s'arrêter : ln(2ⁿ) = n ln 2 grandit de 0,69 m à chaque doublement du temps, sans limite. L'erreur tente parce qu'un mobile de plus en plus lent semble finir par se fixer. Mais il garde une vitesse positive : il ralentit sans jamais s'arrêter, et passera toute position.
:::

::: figure Le tableau de variation de ln : une flèche montante de −∞ à +∞, qui passe par 0 en x = 1 et par 1 en x = e
<svg viewBox="0 0 380 130">
<title>Tableau de variation de ln sur ]0 ; +∞[ : une flèche montante de −∞ à +∞, qui passe par 0 en x = 1 et par 1 en x = e</title>
<rect x="8" y="8" width="364" height="110" fill="none" stroke="#0f172a" stroke-width="1.6"/>
<line x1="8" y1="42" x2="372" y2="42" stroke="#0f172a" stroke-width="1.2"/>
<line x1="78" y1="8" x2="78" y2="118" stroke="#0f172a" stroke-width="1.2"/>
<line x1="125.61" y1="104.73" x2="182.39" y2="91.11" stroke="#d97706" stroke-width="2.4"/>
<polygon points="182.39,91.11 175.14,96.45 173.51,89.63" fill="#d97706"/>
<line x1="209.67" y1="84.82" x2="248.33" y2="76.3" stroke="#d97706" stroke-width="2.4"/>
<polygon points="248.33,76.3 240.99,81.5 239.48,74.66" fill="#d97706"/>
<line x1="275.48" y1="69.51" x2="324.52" y2="55.77" stroke="#d97706" stroke-width="2.4"/>
<polygon points="324.52,55.77 317.48,61.38 315.59,54.63" fill="#d97706"/>
<g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="43" y="30" text-anchor="middle" fill="#0f172a" font-size="13">x</text><text x="112" y="30" text-anchor="middle" fill="#0f172a" font-size="13">0</text><text x="196" y="30" text-anchor="middle" fill="#0f172a" font-size="13">1</text><text x="262" y="30" text-anchor="middle" fill="#0f172a" font-size="13">e</text><text x="338" y="30" text-anchor="middle" fill="#0f172a" font-size="13">+∞</text><text x="43" y="84" text-anchor="middle" fill="#0f172a" font-size="13">ln x</text><text x="112" y="112" text-anchor="middle" fill="#d97706" font-size="13">−∞</text><text x="196" y="91.84" text-anchor="middle" fill="#d97706" font-size="13">0</text><text x="262" y="77.28" text-anchor="middle" fill="#d97706" font-size="13">1</text><text x="338" y="56" text-anchor="middle" fill="#d97706" font-size="13">+∞</text></g>
</svg>
:::

La flèche monte entre chaque paire de valeurs : ln est croissante, et les deux valeurs de la colonne x = 1 et x = e sont celles de la courbe.

::: propriete
La fonction ln est strictement croissante sur ]0 ; +∞[, de limite −∞ en 0⁺ et +∞ en +∞ ; c'est une bijection de ]0 ; +∞[ sur ℝ. On a ln 1 = 0 et ln e = 1, avec 2 < e < 3. Pour tout x > 0 :
$$ ln x < 0 ⟺ 0 < x < 1 $$
$$ ln x > 0 ⟺ x > 1 $$
L'axe des ordonnées est asymptote verticale à la courbe, qui est au-dessous de sa tangente y = x − 1 en A.
Cas limite : ln est strictement croissante sans être majorée ; sa limite en +∞ est infinie, même si elle croît très lentement.
:::

::: verifie À toi : une équation ln x = 2
On donne ln 7 ≈ 1,95 et ln 8 ≈ 2,08. Montre que l'équation ln x = 2 a une seule solution et qu'elle est dans ]7 ; 8[.

---

ln est une bijection de ]0 ; +∞[ sur ℝ et 2 est un réel : l'équation a donc une seule solution, car chaque réel a un unique antécédent. Comme ln 7 ≈ 1,95 < 2 < 2,08 ≈ ln 8 et que ln est strictement croissante, la solution x vérifie 7 < x < 8 (on a en fait x = e² ≈ 7,39).
:::

::: retenir
ln est une bijection strictement croissante de ]0 ; +∞[ sur ℝ, avec ln 1 = 0, ln e = 1, une limite −∞ en 0⁺ et +∞ en +∞.
:::

## ⚖️ Équations et inéquations

À quel instant le mobile est-il à 3 m ? À partir de quand a-t-il dépassé 5 m ? On cherche x tel que ln x = 3, puis tel que ln x > 5.
Comment défaire un logarithme ?

::: exemple Les instants du mobile

1. ln(e³) = 3 ln e = 3 × 1 = 3, car ln(x^r) = r ln x et ln e = 1.
2. ln est strictement croissante, donc injective : ln x = 3 = ln(e³) donne x = e³ ≈ 20,1. Le mobile est à 3 m à l'instant e³ ≈ 20,1 s.
3. ln x > 5 = ln(e⁵) équivaut à x > e⁵, car ln est croissante : elle conserve le sens de l'inégalité. Le mobile dépasse 5 m après l'instant e⁵ ≈ 148,4 s.

:::

::: exemple Le même outil, sans situation : une équation avec deux logarithmes
Résoudre dans ℝ : ln(x + 2) + ln x = ln 3.

1. Les deux logarithmes existent si x + 2 > 0 et x > 0, donc pour x > 0.
2. Sur ]0 ; +∞[ : ln(x + 2) + ln x = ln(x(x + 2)), car la somme de logarithmes est le logarithme du produit.
3. L'équation devient ln(x² + 2x) = ln 3, soit x² + 2x = 3, car ln est injective. Alors x² + 2x − 3 = (x − 1)(x + 3) = 0, donc x = 1 ou x = −3.
4. Seule x = 1 vérifie la condition x > 0. Contrôle : ln 3 + ln 1 = ln 3. L'ensemble des solutions est S = {1}.

:::

::: exemple Le même outil, sur une suite géométrique
Un capital placé à 3 % par an est multiplié par 1,03 chaque année : après n années il vaut C × 1,03ⁿ. Au bout de combien d'années a-t-il doublé ?

1. On cherche le plus petit entier n tel que 1,03ⁿ ≥ 2.
2. ln est croissante : 1,03ⁿ ≥ 2 équivaut à ln(1,03ⁿ) ≥ ln 2, soit n ln 1,03 ≥ ln 2.
3. Comme 1,03 > 1, on a ln 1,03 > 0 (≈ 0,0296) : on divise sans changer le sens. Donc n ≥ ln 2 / ln 1,03 ≈ 23,45.
4. n est entier : n = 24. Contrôle : 1,03²³ ≈ 1,974 < 2 et 1,03²⁴ ≈ 2,033 ≥ 2.

:::

::: piege
**Erreur : oublier le domaine et garder toutes les racines.** Pour ln(x + 2) + ln x = ln 3, le calcul x² + 2x − 3 = 0 donne deux racines, 1 et −3, et on écrit S = {−3 ; 1}. L'erreur tente parce que l'équation du second degré se résout sans condition. Mais pour x = −3, ln x = ln(−3) n'existe pas : on ne garde que les racines qui respectent les conditions de départ, ici S = {1}.
:::

::: methode Résoudre une équation ou une inéquation avec ln

1. Écrire le domaine : chaque expression placée sous un ln doit être strictement positive.
2. Regrouper : ln a + ln b = ln(ab) et ln a − ln b = ln(a/b), pour avoir un seul ln de chaque côté, ou isoler ln x.
3. Passer aux arguments : ln u = ln v ⟺ u = v ; ln u ≤ ln v ⟺ u ≤ v (ln est croissante, le sens est conservé) ; ln x = r ⟺ x = eʳ pour r rationnel.
4. Résoudre, puis ne garder que ce qui respecte le domaine du 1.

Cas limite : diviser par ln q change le sens de l'inégalité si 0 < q < 1, car ln q < 0. Ainsi 0,9ⁿ ≤ 0,5 ⟺ n ln 0,9 ≤ ln 0,5 ⟺ n ≥ ln 0,5 / ln 0,9 ≈ 6,6, donc le plus petit entier est n = 7.
:::

::: verifie À toi : une équation à deux logarithmes
Résoudre dans ℝ : ln x + ln(x − 2) = ln 8.

---

Domaine : x > 0 et x − 2 > 0, donc x > 2. Alors ln x + ln(x − 2) = ln(x(x − 2)), et l'équation devient x(x − 2) = 8, soit x² − 2x − 8 = (x − 4)(x + 2) = 0 : x = 4 ou x = −2. Seule x = 4 vérifie x > 2, donc S = {4}. Contrôle : ln 4 + ln 2 = ln 8.
:::

::: retenir
Pour a > 0 et b > 0 : ln a = ln b ⟺ a = b et ln a < ln b ⟺ a < b ; on résout en écrivant le domaine d'abord et en gardant les solutions qui le respectent.
:::

## ⚡ Limites usuelles et croissances comparées

Après x secondes, le mobile est à ln x mètres : le rapport ln x / x compare sa position à la durée écoulée.

| x | 10 | 100 | 1 000 | 1 000 000 |
| --- | --- | --- | --- | --- |
| ln x / x (valeur approchée) | 0,23 | 0,046 | 0,0069 | 0,000014 |

Le quotient semble tendre vers 0 : la position grandit bien moins vite que le temps. Peut-on le démontrer ? Et que deviennent x ln x quand x tend vers 0⁺ et ln(1 + x)/x quand x tend vers 0 ?

::: figure La courbe de x ↦ ln(1 + x) et sa tangente y = x à l'origine : la courbe colle à la droite près de 0 et reste au-dessous de part et d'autre
<svg viewBox="0 0 340 262">
<title>Courbe de x ↦ ln(1 + x) et sa tangente y = x en l'origine : les deux se confondent près de 0 et la courbe reste au-dessous de part et d'autre</title>
<line x1="34" y1="111.13" x2="328" y2="111.13" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="328,111.13 320,115.13 320,107.13" fill="#0f172a"/>
<line x1="124.16" y1="240" x2="124.16" y2="12" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="124.16,12 128.16,20 120.16,20" fill="#0f172a"/>
<line x1="45.76" y1="108.13" x2="45.76" y2="114.13" stroke="#0f172a" stroke-width="1.2"/>
<line x1="202.56" y1="108.13" x2="202.56" y2="114.13" stroke="#0f172a" stroke-width="1.2"/>
<line x1="280.96" y1="108.13" x2="280.96" y2="114.13" stroke="#0f172a" stroke-width="1.2"/>
<line x1="121.16" y1="210.26" x2="127.16" y2="210.26" stroke="#0f172a" stroke-width="1.2"/>
<line x1="121.16" y1="160.7" x2="127.16" y2="160.7" stroke="#0f172a" stroke-width="1.2"/>
<line x1="121.16" y1="61.57" x2="127.16" y2="61.57" stroke="#0f172a" stroke-width="1.2"/>
<line x1="121.16" y1="12" x2="127.16" y2="12" stroke="#0f172a" stroke-width="1.2"/>
<line x1="45.76" y1="240" x2="45.76" y2="12" stroke="#64748b" stroke-width="1.4" stroke-dasharray="6 4"/>
<line x1="49.68" y1="158.22" x2="280.96" y2="12" stroke="#d97706" stroke-width="2.2"/>
<polyline points="52.4,233.48 53.55,225.55 54.71,218.71 55.86,212.7 57.01,207.34 58.17,202.51 59.32,198.1 60.47,194.06 61.63,190.32 62.78,186.84 63.93,183.59 65.09,180.54 66.24,177.67 67.39,174.95 68.54,172.38 69.7,169.93 70.85,167.6 72,165.37 73.16,163.24 74.31,161.2 75.46,159.24 76.62,157.35 77.77,155.53 78.92,153.78 80.08,152.08 81.23,150.44 82.38,148.86 83.54,147.32 84.69,145.83 85.84,144.38 87,142.98 88.15,141.61 89.3,140.28 90.45,138.98 91.61,137.72 92.76,136.49 93.91,135.29 95.07,134.12 96.22,132.97 97.37,131.85 98.53,130.76 99.68,129.68 100.83,128.64 101.99,127.61 103.14,126.6 104.29,125.62 105.45,124.65 106.6,123.7 107.75,122.77 108.9,121.86 110.06,120.96 111.21,120.08 112.36,119.21 113.52,118.36 114.67,117.53 115.82,116.7 116.98,115.89 118.13,115.1 119.28,114.31 120.44,113.54 121.59,112.78 122.74,112.03 123.9,111.3 125.05,110.57 126.2,109.86 127.35,109.15 128.51,108.46 129.66,107.77 130.81,107.09 131.97,106.43 133.12,105.77 134.27,105.12 135.43,104.48 136.58,103.84 137.73,103.22 138.89,102.6 140.04,101.99 141.19,101.39 142.35,100.79 143.5,100.2 144.65,99.62 145.8,99.05 146.96,98.48 148.11,97.92 149.26,97.36 150.42,96.81 151.57,96.27 152.72,95.73 153.88,95.2 155.03,94.67 156.18,94.15 157.34,93.64 158.49,93.13 159.64,92.63 160.8,92.13 161.95,91.63 163.1,91.14 164.26,90.66 165.41,90.18 166.56,89.7 167.71,89.23 168.87,88.76 170.02,88.3 171.17,87.84 172.33,87.39 173.48,86.94 174.63,86.5 175.79,86.05 176.94,85.62 178.09,85.18 179.25,84.75 180.4,84.33 181.55,83.9 182.71,83.49 183.86,83.07 185.01,82.66 186.16,82.25 187.32,81.84 188.47,81.44 189.62,81.04 190.78,80.65 191.93,80.25 193.08,79.86 194.24,79.48 195.39,79.09 196.54,78.71 197.7,78.34 198.85,77.96 200,77.59 201.16,77.22 202.31,76.85 203.46,76.49 204.61,76.13 205.77,75.77 206.92,75.41 208.07,75.06 209.23,74.71 210.38,74.36 211.53,74.02 212.69,73.67 213.84,73.33 214.99,72.99 216.15,72.66 217.3,72.32 218.45,71.99 219.61,71.66 220.76,71.33 221.91,71.01 223.06,70.68 224.22,70.36 225.37,70.04 226.52,69.73 227.68,69.41 228.83,69.1 229.98,68.79 231.14,68.48 232.29,68.17 233.44,67.86 234.6,67.56 235.75,67.26 236.9,66.96 238.06,66.66 239.21,66.36 240.36,66.07 241.51,65.78 242.67,65.49 243.82,65.2 244.97,64.91 246.13,64.62 247.28,64.34 248.43,64.05 249.59,63.77 250.74,63.49 251.89,63.22 253.05,62.94 254.2,62.66 255.35,62.39 256.51,62.12 257.66,61.85 258.81,61.58 259.97,61.31 261.12,61.05 262.27,60.78 263.42,60.52 264.58,60.26 265.73,60 266.88,59.74 268.04,59.48 269.19,59.22 270.34,58.97 271.5,58.71 272.65,58.46 273.8,58.21 274.96,57.96 276.11,57.71 277.26,57.46 278.42,57.22 279.57,56.97 280.72,56.73 281.87,56.49 283.03,56.24 284.18,56 285.33,55.76 286.49,55.53 287.64,55.29 288.79,55.05 289.95,54.82 291.1,54.59 292.25,54.35 293.41,54.12 294.56,53.89 295.71,53.66 296.87,53.43 298.02,53.21 299.17,52.98 300.32,52.76 301.48,52.53 302.63,52.31 303.78,52.09 304.94,51.87 306.09,51.65 307.24,51.43 308.4,51.21 309.55,50.99 310.7,50.78 311.86,50.56 313.01,50.35 314.16,50.13 315.32,49.92 316.47,49.71 317.62,49.5 318.77,49.29 319.93,49.08 321.08,48.87 322.23,48.66 323.39,48.46 324.54,48.25 325.69,48.05 326.85,47.84 328,47.64" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round"/>
<circle cx="124.16" cy="111.13" r="4" fill="#0f172a" stroke="#ffffff" stroke-width="1.2"/>
<g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="45.76" y="126.13" text-anchor="middle" fill="#0f172a" font-size="10">−1</text><text x="202.56" y="126.13" text-anchor="middle" fill="#0f172a" font-size="10">1</text><text x="280.96" y="126.13" text-anchor="middle" fill="#0f172a" font-size="10">2</text><text x="117.16" y="213.76" text-anchor="end" fill="#0f172a" font-size="10">−2</text><text x="117.16" y="164.2" text-anchor="end" fill="#0f172a" font-size="10">−1</text><text x="117.16" y="65.07" text-anchor="end" fill="#0f172a" font-size="10">1</text><text x="117.16" y="15.5" text-anchor="end" fill="#0f172a" font-size="10">2</text><text x="326" y="105.13" text-anchor="end" fill="#0f172a" font-size="12">x</text><text x="132.16" y="22" text-anchor="start" fill="#0f172a" font-size="12">y</text><text x="324.08" y="91.3" text-anchor="end" fill="#0f6e56" font-size="12">y = ln(1 + x)</text><text x="245.68" y="14.48" text-anchor="end" fill="#d97706" font-size="12">y = x</text><text x="52.03" y="30" text-anchor="start" fill="#64748b" font-size="11">x = −1</text></g>
</svg>
:::

Le quotient ln(1 + x)/x est la pente de la droite qui joint l'origine au point de la courbe d'abscisse x ; la tangente y = x a pour pente 1, ce qui annonce une limite égale à 1.

::: exemple Pourquoi ln x / x tend vers 0

1. Pour tout t > 0, ln t ≤ t − 1 (courbe sous sa tangente). Avec t = √x, où x > 1 : ln √x ≤ √x − 1 < √x.
2. Comme ln x = 2 ln √x, on obtient 0 < ln x < 2√x (ln x > 0 car x > 1).
3. On divise par x > 0 : 0 < ln x / x < 2/√x. Pour x = 1 000 000, 2/√x = 0,002 et ln x / x ≈ 0,000014, ce qui est cohérent.
4. 2/√x tend vers 0 en +∞, donc par encadrement ln x / x tend vers 0.

:::

::: exemple Le passage de +∞ à 0⁺

1. Pour x > 0, on pose t = 1/x. Quand x tend vers 0⁺, t tend vers +∞.
2. x ln x = (1/t) ln(1/t) = −ln t / t, car ln(1/t) = −ln t.
3. Or ln t / t tend vers 0 en +∞, donc lim x→0⁺ x ln x = 0. Contrôle : pour x = 0,001, x ln x ≈ −0,0069, cohérent avec le tableau.

:::

::: exemple Le même outil, sans situation : quatre limites

1. lim x→+∞ (5 ln x − 2√x) : on écrit 5 ln x − 2√x = √x (5 ln x/√x − 2). Comme ln x/√x tend vers 0, la parenthèse tend vers −2 et √x vers +∞ : la limite est −∞.
2. lim x→0⁺ x² ln x : on écrit x² ln x = x × (x ln x), produit de deux facteurs de limite 0 : la limite est 0.
3. lim x→1 ln x/(x² − 1) : on écrit ln x/(x² − 1) = (ln x/(x − 1)) × 1/(x + 1). Comme ln x/(x − 1) tend vers 1, la limite est 1 × 1/2 = 1/2.
4. lim x→0 ln(1 + 3x)/x : on écrit ln(1 + 3x)/x = 3 × ln(1 + 3x)/(3x). Comme 3x tend vers 0, ln(1 + 3x)/(3x) tend vers 1 : la limite est 3.

:::

::: piege
**Erreur : conclure que x ln x tend vers −∞ parce que ln x tend vers −∞.** En 0⁺, x tend vers 0 et ln x vers −∞ : c'est une forme 0 × ∞, qui ne se lit pas à l'œil. Pour x = 0,001, x ln x ≈ −0,0069 : le facteur x qui s'écrase vers 0 l'emporte sur le logarithme. L'erreur tente parce que le logarithme explose visiblement ; mais avec t = 1/x, x ln x = −ln t / t, et ln t est négligeable devant t en +∞ : c'est la croissance comparée qui tranche.
:::

::: propriete
Limites usuelles :
$$ lim x→+∞ ln x / x = 0 $$
$$ lim x→0⁺ x ln x = 0 $$
$$ lim x→1 ln x/(x − 1) = 1 $$
$$ lim x→0 ln(1 + x)/x = 1 $$
Pour tout rationnel r > 0 : lim x→+∞ ln x / xʳ = 0 et lim x→0⁺ xʳ ln x = 0. Pour x proche de 0, x est une approximation affine de ln(1 + x). En +∞, ln x/x tend vers 0 : la courbe de ln a une branche parabolique de direction l'axe des abscisses.
Cas limite : ln x / x ne tend vers 0 qu'en +∞ ; en 0⁺, ln x tend vers −∞ et 1/x vers +∞, donc lim x→0⁺ ln x / x = −∞.
:::

::: verifie À toi : une limite de la forme ∞ − ∞
Calcule lim x→+∞ (x² − 5 ln x).

---

On met x² en facteur : x² − 5 ln x = x² (1 − 5 ln x / x²). Comme ln x / x² = (ln x / x) × (1/x) tend vers 0 × 0 = 0, la parenthèse tend vers 1 et x² vers +∞. La limite est +∞ : en +∞, x² l'emporte sur le logarithme.
:::

::: retenir
ln x / x tend vers 0 en +∞ et x ln x tend vers 0 en 0⁺ (et, pour r > 0, ln x / xʳ et xʳ ln x aussi) ; ln x/(x − 1) et ln(1 + x)/x tendent vers 1.
:::

## 🔗 Dérivée de ln(u) et primitives

On retarde le mobile d'une seconde : il démarre à l'instant 1 et sa position à l'instant x > 1 est Q(x) = ln(x − 1), le même mouvement décalé. Sa vitesse doit être celle de l'ancien mobile une seconde plus tôt.
Comment dériver ln(u(x)) pour une fonction u quelconque, et comment retrouver des primitives ?

::: exemple Le mobile retardé

1. Pour x > 1, x − 1 > 0 : Q = ln∘u est définie avec u(x) = x − 1, dérivable, u′(x) = 1.
2. Par dérivée d'une composée, Q′(x) = u′(x) × ln′(u(x)) = 1 × 1/(x − 1) = 1/(x − 1).
3. À l'instant 3, Q′(3) = 1/2 m/s, la vitesse de l'ancien mobile à l'instant 2 : le décalage d'une seconde est bien retrouvé.

:::

::: exemple Le même outil, sans situation : deux dérivées
Calculer la dérivée de f(x) = ln(x² + 4x + 7) et celle de g(x) = ln|x² − 9|.

1. Pour f : x² + 4x + 7 = (x + 2)² + 3 > 0, donc f est définie et dérivable sur ℝ, et f′(x) = u′(x)/u(x) = (2x + 4)/(x² + 4x + 7).
2. Pour g : x² − 9 = 0 si x = 3 ou x = −3, donc g est définie sur ℝ privé de {−3 ; 3}. Sur cet ensemble, u(x) = x² − 9 ≠ 0.
3. Avec la valeur absolue, g′(x) = u′(x)/u(x) = 2x/(x² − 9) : là où u(x) < 0, |u(x)| = −u(x) et la dérivée de ln(−u) est (−u′)/(−u) = u′/u, la même.

:::

::: figure La courbe de ln|x| avec ses tangentes en x = 2 (pente 1/2) et en x = −2 (pente −1/2) : deux branches symétriques
<svg viewBox="0 0 340 250">
<title>Courbe de x ↦ ln|x| : deux branches symétriques, avec les tangentes en x = 2 (pente 1/2) et en x = −2 (pente −1/2)</title>
<line x1="12" y1="104.57" x2="328" y2="104.57" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="328,104.57 320,108.57 320,100.57" fill="#0f172a"/>
<line x1="170" y1="228" x2="170" y2="12" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="170,12 174,20 166,20" fill="#0f172a"/>
<line x1="26.36" y1="101.57" x2="26.36" y2="107.57" stroke="#0f172a" stroke-width="1.2"/>
<line x1="74.24" y1="101.57" x2="74.24" y2="107.57" stroke="#0f172a" stroke-width="1.2"/>
<line x1="122.12" y1="101.57" x2="122.12" y2="107.57" stroke="#0f172a" stroke-width="1.2"/>
<line x1="217.88" y1="101.57" x2="217.88" y2="107.57" stroke="#0f172a" stroke-width="1.2"/>
<line x1="265.76" y1="101.57" x2="265.76" y2="107.57" stroke="#0f172a" stroke-width="1.2"/>
<line x1="313.64" y1="101.57" x2="313.64" y2="107.57" stroke="#0f172a" stroke-width="1.2"/>
<line x1="167" y1="220.29" x2="173" y2="220.29" stroke="#0f172a" stroke-width="1.2"/>
<line x1="167" y1="181.71" x2="173" y2="181.71" stroke="#0f172a" stroke-width="1.2"/>
<line x1="167" y1="143.14" x2="173" y2="143.14" stroke="#0f172a" stroke-width="1.2"/>
<line x1="167" y1="66" x2="173" y2="66" stroke="#0f172a" stroke-width="1.2"/>
<line x1="167" y1="27.43" x2="173" y2="27.43" stroke="#0f172a" stroke-width="1.2"/>
<line x1="184.36" y1="104.84" x2="294.48" y2="16.12" stroke="#d97706" stroke-width="2.2"/>
<line x1="155.64" y1="104.84" x2="45.52" y2="16.12" stroke="#2563eb" stroke-width="2.2"/>
<polyline points="171.08,224.19 171.86,203.08 172.65,189.52 173.43,179.5 174.22,171.56 175,164.98 175.78,159.35 176.57,154.45 177.35,150.1 178.14,146.19 178.92,142.64 179.71,139.38 180.49,136.39 181.28,133.61 182.06,131.01 182.85,128.58 183.63,126.29 184.42,124.14 185.2,122.09 185.98,120.15 186.77,118.3 187.55,116.54 188.34,114.85 189.12,113.24 189.91,111.68 190.69,110.19 191.48,108.76 192.26,107.37 193.05,106.04 193.83,104.75 194.62,103.5 195.4,102.29 196.18,101.11 196.97,99.97 197.75,98.87 198.54,97.79 199.32,96.75 200.11,95.73 200.89,94.74 201.68,93.77 202.46,92.82 203.25,91.9 204.03,91 204.82,90.12 205.6,89.27 206.38,88.42 207.17,87.6 207.95,86.8 208.74,86.01 209.52,85.23 210.31,84.47 211.09,83.73 211.88,83 212.66,82.29 213.45,81.58 214.23,80.89 215.02,80.21 215.8,79.55 216.58,78.89 217.37,78.25 218.15,77.61 218.94,76.99 219.72,76.38 220.51,75.77 221.29,75.18 222.08,74.59 222.86,74.02 223.65,73.45 224.43,72.89 225.22,72.34 226,71.79 226.78,71.26 227.57,70.73 228.35,70.2 229.14,69.69 229.92,69.18 230.71,68.68 231.49,68.18 232.28,67.69 233.06,67.21 233.85,66.73 234.63,66.26 235.42,65.8 236.2,65.34 236.98,64.88 237.77,64.43 238.55,63.99 239.34,63.55 240.12,63.12 240.91,62.69 241.69,62.26 242.48,61.84 243.26,61.43 244.05,61.02 244.83,60.61 245.62,60.21 246.4,59.81 247.18,59.42 247.97,59.03 248.75,58.64 249.54,58.26 250.32,57.88 251.11,57.5 251.89,57.13 252.68,56.77 253.46,56.4 254.25,56.04 255.03,55.68 255.82,55.33 256.6,54.98 257.38,54.63 258.17,54.28 258.95,53.94 259.74,53.6 260.52,53.27 261.31,52.94 262.09,52.61 262.88,52.28 263.66,51.95 264.45,51.63 265.23,51.31 266.02,51 266.8,50.68 267.58,50.37 268.37,50.06 269.15,49.76 269.94,49.45 270.72,49.15 271.51,48.85 272.29,48.55 273.08,48.26 273.86,47.97 274.65,47.68 275.43,47.39 276.22,47.1 277,46.82 277.78,46.54 278.57,46.26 279.35,45.98 280.14,45.7 280.92,45.43 281.71,45.16 282.49,44.89 283.28,44.62 284.06,44.35 284.85,44.09 285.63,43.83 286.42,43.57 287.2,43.31 287.98,43.05 288.77,42.79 289.55,42.54 290.34,42.29 291.12,42.04 291.91,41.79 292.69,41.54 293.48,41.29 294.26,41.05 295.05,40.81 295.83,40.57 296.62,40.33 297.4,40.09 298.18,39.85 298.97,39.62 299.75,39.38 300.54,39.15 301.32,38.92 302.11,38.69 302.89,38.46 303.68,38.23 304.46,38.01 305.25,37.78 306.03,37.56 306.82,37.34 307.6,37.12 308.38,36.9 309.17,36.68 309.95,36.46 310.74,36.25 311.52,36.03 312.31,35.82 313.09,35.61 313.88,35.4 314.66,35.19 315.45,34.98 316.23,34.77 317.02,34.56 317.8,34.36 318.58,34.15 319.37,33.95 320.15,33.75 320.94,33.55 321.72,33.35 322.51,33.15 323.29,32.95 324.08,32.75 324.86,32.56 325.65,32.36 326.43,32.17 327.22,31.98 328,31.78" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round"/>
<polyline points="12,31.78 12.78,31.98 13.57,32.17 14.35,32.36 15.14,32.56 15.92,32.75 16.71,32.95 17.49,33.15 18.28,33.35 19.06,33.55 19.85,33.75 20.63,33.95 21.42,34.15 22.2,34.36 22.98,34.56 23.77,34.77 24.55,34.98 25.34,35.19 26.12,35.4 26.91,35.61 27.69,35.82 28.48,36.03 29.26,36.25 30.05,36.46 30.83,36.68 31.62,36.9 32.4,37.12 33.18,37.34 33.97,37.56 34.75,37.78 35.54,38.01 36.32,38.23 37.11,38.46 37.89,38.69 38.68,38.92 39.46,39.15 40.25,39.38 41.03,39.62 41.82,39.85 42.6,40.09 43.38,40.33 44.17,40.57 44.95,40.81 45.74,41.05 46.52,41.29 47.31,41.54 48.09,41.79 48.88,42.04 49.66,42.29 50.45,42.54 51.23,42.79 52.02,43.05 52.8,43.31 53.58,43.57 54.37,43.83 55.15,44.09 55.94,44.35 56.72,44.62 57.51,44.89 58.29,45.16 59.08,45.43 59.86,45.7 60.65,45.98 61.43,46.26 62.22,46.54 63,46.82 63.78,47.1 64.57,47.39 65.35,47.68 66.14,47.97 66.92,48.26 67.71,48.55 68.49,48.85 69.28,49.15 70.06,49.45 70.85,49.76 71.63,50.06 72.42,50.37 73.2,50.68 73.98,51 74.77,51.31 75.55,51.63 76.34,51.95 77.12,52.28 77.91,52.61 78.69,52.94 79.48,53.27 80.26,53.6 81.05,53.94 81.83,54.28 82.62,54.63 83.4,54.98 84.18,55.33 84.97,55.68 85.75,56.04 86.54,56.4 87.32,56.77 88.11,57.13 88.89,57.5 89.68,57.88 90.46,58.26 91.25,58.64 92.03,59.03 92.82,59.42 93.6,59.81 94.38,60.21 95.17,60.61 95.95,61.02 96.74,61.43 97.52,61.84 98.31,62.26 99.09,62.69 99.88,63.12 100.66,63.55 101.45,63.99 102.23,64.43 103.02,64.88 103.8,65.34 104.58,65.8 105.37,66.26 106.15,66.73 106.94,67.21 107.72,67.69 108.51,68.18 109.29,68.68 110.08,69.18 110.86,69.69 111.65,70.2 112.43,70.73 113.22,71.26 114,71.79 114.78,72.34 115.57,72.89 116.35,73.45 117.14,74.02 117.92,74.59 118.71,75.18 119.49,75.77 120.28,76.38 121.06,76.99 121.85,77.61 122.63,78.25 123.42,78.89 124.2,79.55 124.98,80.21 125.77,80.89 126.55,81.58 127.34,82.29 128.12,83 128.91,83.73 129.69,84.47 130.48,85.23 131.26,86.01 132.05,86.8 132.83,87.6 133.62,88.42 134.4,89.27 135.18,90.12 135.97,91 136.75,91.9 137.54,92.82 138.32,93.77 139.11,94.74 139.89,95.73 140.68,96.75 141.46,97.79 142.25,98.87 143.03,99.97 143.82,101.11 144.6,102.29 145.38,103.5 146.17,104.75 146.95,106.04 147.74,107.37 148.52,108.76 149.31,110.19 150.09,111.68 150.88,113.24 151.66,114.85 152.45,116.54 153.23,118.3 154.02,120.15 154.8,122.09 155.58,124.14 156.37,126.29 157.15,128.58 157.94,131.01 158.72,133.61 159.51,136.39 160.29,139.38 161.08,142.64 161.86,146.19 162.65,150.1 163.43,154.45 164.22,159.35 165,164.98 165.78,171.56 166.57,179.5 167.35,189.52 168.14,203.08 168.92,224.19" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round"/>
<circle cx="217.88" cy="77.84" r="4" fill="#0f172a" stroke="#ffffff" stroke-width="1.2"/>
<circle cx="122.12" cy="77.84" r="4" fill="#0f172a" stroke="#ffffff" stroke-width="1.2"/>
<g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="26.36" y="119.57" text-anchor="middle" fill="#0f172a" font-size="10">−6</text><text x="74.24" y="119.57" text-anchor="middle" fill="#0f172a" font-size="10">−4</text><text x="122.12" y="119.57" text-anchor="middle" fill="#0f172a" font-size="10">−2</text><text x="217.88" y="119.57" text-anchor="middle" fill="#0f172a" font-size="10">2</text><text x="265.76" y="119.57" text-anchor="middle" fill="#0f172a" font-size="10">4</text><text x="313.64" y="119.57" text-anchor="middle" fill="#0f172a" font-size="10">6</text><text x="163" y="223.79" text-anchor="end" fill="#0f172a" font-size="10">−3</text><text x="163" y="185.21" text-anchor="end" fill="#0f172a" font-size="10">−2</text><text x="152" y="146.64" text-anchor="end" fill="#0f172a" font-size="10">−1</text><text x="163" y="69.5" text-anchor="end" fill="#0f172a" font-size="10">1</text><text x="163" y="30.93" text-anchor="end" fill="#0f172a" font-size="10">2</text><text x="326" y="98.57" text-anchor="end" fill="#0f172a" font-size="12">x</text><text x="178" y="22" text-anchor="start" fill="#0f172a" font-size="12">y</text><text x="241.82" y="96.86" text-anchor="start" fill="#d97706" font-size="11">pente 1/2</text><text x="98.18" y="96.86" text-anchor="end" fill="#2563eb" font-size="11">pente −1/2</text><text x="323.21" y="62.14" text-anchor="end" fill="#0f6e56" font-size="12">y = ln|x|</text></g>
</svg>
:::

Pour u(x) = x, la formule donne (ln|x|)′ = 1/x sur ℝ privé de 0 : positive à droite, où la courbe monte (pente 1/2 en x = 2), négative à gauche, où elle descend (pente −1/2 en x = −2).

::: exemple Le même outil, dans l'autre sens : trois primitives

1. f(x) = 3x²/(x³ + 1) sur ]−1 ; +∞[ : avec u(x) = x³ + 1 > 0 et u′(x) = 3x², f = u′/u et F(x) = ln(x³ + 1) + k. Pour F(0) = 2 : ln 1 + k = 2, donc F(x) = ln(x³ + 1) + 2.
2. f(x) = x/(x² + 1) = (1/2) × 2x/(x² + 1) sur ℝ, avec u(x) = x² + 1 > 0 : F(x) = (1/2) ln(x² + 1) + k.
3. F(x) = x ln x − x est une primitive de ln sur ]0 ; +∞[ : F′(x) = ln x + x × (1/x) − 1 = ln x, par la dérivée d'un produit.

:::

::: piege
**Erreur : écrire (ln u)′ = 1/u en oubliant u′.** Pour u(x) = 2x + 1, on écrirait (ln(2x + 1))′ = 1/(2x + 1). L'erreur tente parce que (ln x)′ = 1/x. Mais près de 0, ln(1 + t) ≈ t avec t = 2x : ln(2x + 1) ≈ 2x, la pente en x = 0 est 2, alors que 1/(2x + 1) vaut 1. La bonne formule est u′/u = 2/(2x + 1), qui vaut bien 2 en x = 0.
:::

::: propriete
**Théorème.** Si u est dérivable sur D et u(x) > 0 sur D, alors ln∘u est dérivable sur D et :
$$ (ln u)′ = u′/u $$
Si u est dérivable sur D et u(x) ≠ 0 sur D, alors x ↦ ln|u(x)| est dérivable sur D, avec la même dérivée u′/u.
Primitives : si u est dérivable et ne s'annule pas sur un intervalle I, les primitives de u′/u sur I sont les fonctions x ↦ ln|u(x)| + k. Une primitive de ln sur ]0 ; +∞[ est x ↦ x ln x − x.
Cas limite : une primitive se prend sur un intervalle. Sur ]−∞ ; 0[ et sur ]0 ; +∞[, les primitives de 1/x sont ln|x| + k₁ et ln|x| + k₂, avec des constantes k₁ et k₂ qui peuvent différer.
:::

::: verifie À toi : une dérivée de ln(u) avec u′ négative
Soit g(x) = ln(3 − 2x) sur ]−∞ ; 3/2[. Calcule g′(x).

---

On pose u(x) = 3 − 2x, strictement positive sur ]−∞ ; 3/2[, avec u′(x) = −2. Donc g′(x) = u′(x)/u(x) = −2/(3 − 2x). Elle est négative : g est décroissante, ce qui est logique car 3 − 2x décroît et ln est croissante.
:::

::: retenir
(ln u)′ = u′/u, et (ln|u|)′ = u′/u quand u ne s'annule pas ; les primitives de u′/u sont ln|u| + k ; ln a pour primitive x ln x − x.
:::

## 🧩 Étudier une fonction contenant un logarithme

Un atelier fabrique x centaines de pièces (x > 0). Son coût moyen par pièce, en dinars, est f(x) = x − 2 ln x : pour une toute petite série, les frais fixes pèsent lourd ; pour une grande, la fabrication coûte de plus en plus.
À quelle production le coût moyen est-il le plus bas, et quelle est l'allure de la courbe ?

::: figure La courbe C de f(x) = x − 2 ln x : minimum en M(2 ; 2 − 2 ln 2), passage par A(1 ; 1) sur la droite Δ : y = x, courbe au-dessous de Δ pour x > 1
<svg viewBox="0 0 340 262">
<title>Courbe C de f(x) = x − 2 ln x : minimum en M(2 ; 2 − 2 ln 2), passage par A(1 ; 1) sur la droite Δ : y = x, au-dessous de Δ pour x > 1</title>
<line x1="30" y1="240" x2="328" y2="240" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="328,240 320,244 320,236" fill="#0f172a"/>
<line x1="30" y1="240" x2="30" y2="12" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="30,12 34,20 26,20" fill="#0f172a"/>
<line x1="69.21" y1="237" x2="69.21" y2="243" stroke="#0f172a" stroke-width="1.2"/>
<line x1="108.42" y1="237" x2="108.42" y2="243" stroke="#0f172a" stroke-width="1.2"/>
<line x1="147.63" y1="237" x2="147.63" y2="243" stroke="#0f172a" stroke-width="1.2"/>
<line x1="186.84" y1="237" x2="186.84" y2="243" stroke="#0f172a" stroke-width="1.2"/>
<line x1="226.05" y1="237" x2="226.05" y2="243" stroke="#0f172a" stroke-width="1.2"/>
<line x1="265.26" y1="237" x2="265.26" y2="243" stroke="#0f172a" stroke-width="1.2"/>
<line x1="304.47" y1="237" x2="304.47" y2="243" stroke="#0f172a" stroke-width="1.2"/>
<line x1="27" y1="197.78" x2="33" y2="197.78" stroke="#0f172a" stroke-width="1.2"/>
<line x1="27" y1="155.56" x2="33" y2="155.56" stroke="#0f172a" stroke-width="1.2"/>
<line x1="27" y1="113.33" x2="33" y2="113.33" stroke="#0f172a" stroke-width="1.2"/>
<line x1="27" y1="71.11" x2="33" y2="71.11" stroke="#0f172a" stroke-width="1.2"/>
<line x1="27" y1="28.89" x2="33" y2="28.89" stroke="#0f172a" stroke-width="1.2"/>
<line x1="30" y1="240" x2="237.82" y2="16.22" stroke="#64748b" stroke-width="1.8" stroke-dasharray="6 4"/>
<polyline points="32.92,17.56 34.06,44.05 35.19,63.66 36.33,79.14 37.46,91.85 38.6,102.58 39.73,111.84 40.87,119.93 42,127.1 43.14,133.5 44.27,139.28 45.41,144.52 46.54,149.3 47.68,153.68 48.81,157.72 49.94,161.44 51.08,164.89 52.21,168.1 53.35,171.08 54.48,173.87 55.62,176.47 56.75,178.91 57.89,181.2 59.02,183.34 60.16,185.36 61.29,187.26 62.43,189.04 63.56,190.73 64.7,192.31 65.83,193.81 66.97,195.22 68.1,196.55 69.24,197.81 70.37,198.99 71.51,200.11 72.64,201.17 73.78,202.16 74.91,203.1 76.05,203.99 77.18,204.82 78.32,205.61 79.45,206.35 80.59,207.04 81.72,207.69 82.86,208.3 83.99,208.87 85.13,209.41 86.26,209.91 87.4,210.37 88.53,210.8 89.67,211.2 90.8,211.57 91.94,211.91 93.07,212.22 94.21,212.51 95.34,212.76 96.48,213 97.61,213.2 98.75,213.39 99.88,213.55 101.02,213.69 102.15,213.8 103.29,213.9 104.42,213.97 105.56,214.03 106.69,214.07 107.83,214.09 108.96,214.09 110.1,214.07 111.23,214.04 112.37,213.98 113.5,213.92 114.64,213.84 115.77,213.74 116.91,213.63 118.04,213.5 119.17,213.36 120.31,213.21 121.44,213.04 122.58,212.86 123.71,212.66 124.85,212.46 125.98,212.24 127.12,212.01 128.25,211.77 129.39,211.52 130.52,211.26 131.66,210.98 132.79,210.7 133.93,210.4 135.06,210.1 136.2,209.78 137.33,209.46 138.47,209.12 139.6,208.78 140.74,208.43 141.87,208.07 143.01,207.7 144.14,207.32 145.28,206.93 146.41,206.54 147.55,206.14 148.68,205.72 149.82,205.31 150.95,204.88 152.09,204.45 153.22,204.01 154.36,203.56 155.49,203.1 156.63,202.64 157.76,202.17 158.9,201.7 160.03,201.22 161.17,200.73 162.3,200.23 163.44,199.73 164.57,199.22 165.71,198.71 166.84,198.19 167.98,197.67 169.11,197.14 170.25,196.6 171.38,196.06 172.52,195.51 173.65,194.96 174.79,194.4 175.92,193.84 177.06,193.27 178.19,192.7 179.33,192.12 180.46,191.54 181.6,190.95 182.73,190.36 183.87,189.76 185,189.16 186.14,188.56 187.27,187.95 188.41,187.33 189.54,186.71 190.67,186.09 191.81,185.46 192.94,184.83 194.08,184.19 195.21,183.55 196.35,182.91 197.48,182.26 198.62,181.61 199.75,180.95 200.89,180.29 202.02,179.63 203.16,178.96 204.29,178.29 205.43,177.62 206.56,176.94 207.7,176.26 208.83,175.58 209.97,174.89 211.1,174.2 212.24,173.5 213.37,172.8 214.51,172.1 215.64,171.4 216.78,170.69 217.91,169.98 219.05,169.27 220.18,168.55 221.32,167.83 222.45,167.11 223.59,166.38 224.72,165.65 225.86,164.92 226.99,164.19 228.13,163.45 229.26,162.71 230.4,161.97 231.53,161.22 232.67,160.48 233.8,159.73 234.94,158.97 236.07,158.22 237.21,157.46 238.34,156.7 239.48,155.93 240.61,155.17 241.75,154.4 242.88,153.63 244.02,152.86 245.15,152.08 246.29,151.3 247.42,150.52 248.56,149.74 249.69,148.96 250.83,148.17 251.96,147.38 253.1,146.59 254.23,145.8 255.37,145 256.5,144.2 257.64,143.4 258.77,142.6 259.9,141.8 261.04,140.99 262.17,140.18 263.31,139.37 264.44,138.56 265.58,137.74 266.71,136.93 267.85,136.11 268.98,135.29 270.12,134.47 271.25,133.64 272.39,132.82 273.52,131.99 274.66,131.16 275.79,130.33 276.93,129.5 278.06,128.66 279.2,127.82 280.33,126.99 281.47,126.15 282.6,125.3 283.74,124.46 284.87,123.62 286.01,122.77 287.14,121.92 288.28,121.07 289.41,120.22 290.55,119.36 291.68,118.51 292.82,117.65 293.95,116.79 295.09,115.93 296.22,115.07 297.36,114.21 298.49,113.35 299.63,112.48 300.76,111.61 301.9,110.74 303.03,109.87 304.17,109 305.3,108.13 306.44,107.25 307.57,106.38 308.71,105.5 309.84,104.62 310.98,103.74 312.11,102.86 313.25,101.98 314.38,101.09 315.52,100.21 316.65,99.32 317.79,98.43 318.92,97.54 320.06,96.65 321.19,95.76 322.33,94.86 323.46,93.97 324.6,93.07 325.73,92.18 326.87,91.28 328,90.38" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round"/>
<circle cx="69.21" cy="197.78" r="4" fill="#0f172a" stroke="#ffffff" stroke-width="1.2"/>
<circle cx="108.42" cy="214.09" r="4.4" fill="#d97706" stroke="#ffffff" stroke-width="1.2"/>
<line x1="108.42" y1="240" x2="108.42" y2="214.09" stroke="#64748b" stroke-width="1.4" stroke-dasharray="5 4"/>
<g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="69.21" y="255" text-anchor="middle" fill="#0f172a" font-size="10">1</text><text x="108.42" y="255" text-anchor="middle" fill="#0f172a" font-size="10">2</text><text x="147.63" y="255" text-anchor="middle" fill="#0f172a" font-size="10">3</text><text x="186.84" y="255" text-anchor="middle" fill="#0f172a" font-size="10">4</text><text x="226.05" y="255" text-anchor="middle" fill="#0f172a" font-size="10">5</text><text x="265.26" y="255" text-anchor="middle" fill="#0f172a" font-size="10">6</text><text x="304.47" y="255" text-anchor="middle" fill="#0f172a" font-size="10">7</text><text x="23" y="201.28" text-anchor="end" fill="#0f172a" font-size="10">1</text><text x="23" y="159.06" text-anchor="end" fill="#0f172a" font-size="10">2</text><text x="23" y="116.83" text-anchor="end" fill="#0f172a" font-size="10">3</text><text x="23" y="74.61" text-anchor="end" fill="#0f172a" font-size="10">4</text><text x="23" y="32.39" text-anchor="end" fill="#0f172a" font-size="10">5</text><text x="326" y="234" text-anchor="end" fill="#0f172a" font-size="12">x</text><text x="38" y="22" text-anchor="start" fill="#0f172a" font-size="12">y</text><text x="65.29" y="174.56" text-anchor="end" fill="#0f172a" font-size="12">A</text><text x="108.42" y="231.82" text-anchor="start" fill="#d97706" font-size="12">M</text><text x="244" y="28" text-anchor="start" fill="#64748b" font-size="12">Δ : y = x</text><text x="241.74" y="140.78" text-anchor="start" fill="#0f6e56" font-size="13">C</text></g>
</svg>
:::

La courbe plonge le long de l'axe des ordonnées, atteint son plus bas niveau en M, puis remonte en s'écartant de plus en plus de la droite pointillée : c'est ce que l'étude va établir.

::: exemple Le coût moyen d'une série

1. Domaine : ln x exige x > 0, donc D = ]0 ; +∞[. Limite en 0⁺ : x tend vers 0 et −2 ln x vers +∞, donc f(x) tend vers +∞ et l'axe des ordonnées est asymptote verticale. Limite en +∞ : f(x) = x (1 − 2 ln x / x) avec ln x / x → 0, donc f(x) tend vers +∞.
2. Dérivée : f′(x) = 1 − 2/x = (x − 2)/x, du signe de x − 2 car x > 0. Donc f décroît sur ]0 ; 2] et croît sur [2 ; +∞[, avec un minimum f(2) = 2 − 2 ln 2 ≈ 0,61 : la production la moins chère est de 200 pièces, à 0,61 dinar la pièce.
3. Branche infinie en +∞ : f(x)/x = 1 − 2 ln x / x tend vers 1, mais f(x) − x = −2 ln x tend vers −∞. Il n'y a donc pas d'asymptote : la courbe a une branche parabolique de direction la droite Δ : y = x.
4. Position par rapport à Δ : f(x) − x = −2 ln x est positif si x < 1 et négatif si x > 1. La courbe est au-dessus de Δ avant l'abscisse 1, passe par A(1 ; 1), et reste au-dessous ensuite.

:::

::: figure Le tableau de variation de f : décroissante de +∞ à 2 − 2 ln 2 sur ]0 ; 2], puis croissante de 2 − 2 ln 2 à +∞
<svg viewBox="0 0 380 170">
<title>Tableau de variation de f(x) = x − 2 ln x : décroissante de +∞ à 2 − 2 ln 2 sur ]0 ; 2], puis croissante de 2 − 2 ln 2 à +∞</title>
<rect x="8" y="8" width="364" height="150" fill="none" stroke="#0f172a" stroke-width="1.6"/>
<line x1="8" y1="42" x2="372" y2="42" stroke="#0f172a" stroke-width="1.2"/>
<line x1="78" y1="8" x2="78" y2="158" stroke="#0f172a" stroke-width="1.2"/>
<line x1="8" y1="76" x2="372" y2="76" stroke="#0f172a" stroke-width="1.2"/>
<line x1="214" y1="42" x2="214" y2="76" stroke="#0f172a" stroke-width="1.0" stroke-dasharray="3 3"/>
<line x1="128.06" y1="91.88" x2="190.16" y2="132.43" stroke="#d97706" stroke-width="2.4"/>
<polygon points="190.16,132.43 181.31,130.84 185.14,124.97" fill="#d97706"/>
<line x1="239.29" y1="134.05" x2="317.59" y2="90.84" stroke="#d97706" stroke-width="2.4"/>
<polygon points="317.59,90.84 312.03,97.92 308.64,91.78" fill="#d97706"/>
<g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="43" y="30" text-anchor="middle" fill="#0f172a" font-size="13">x</text><text x="116" y="30" text-anchor="middle" fill="#0f172a" font-size="13">0</text><text x="214" y="30" text-anchor="middle" fill="#0f172a" font-size="13">2</text><text x="330" y="30" text-anchor="middle" fill="#0f172a" font-size="13">+∞</text><text x="43" y="64" text-anchor="middle" fill="#0f172a" font-size="12">f′(x)</text><text x="166" y="64" text-anchor="middle" fill="#0f172a" font-size="14">−</text><text x="214" y="64" text-anchor="middle" fill="#0f172a" font-size="14">0</text><text x="272" y="64" text-anchor="middle" fill="#0f172a" font-size="14">+</text><text x="43" y="120" text-anchor="middle" fill="#0f172a" font-size="13">f(x)</text><text x="116" y="88" text-anchor="middle" fill="#d97706" font-size="13">+∞</text><text x="214" y="152" text-anchor="middle" fill="#d97706" font-size="13">2 − 2 ln 2</text><text x="330" y="88" text-anchor="middle" fill="#d97706" font-size="13">+∞</text></g>
</svg>
:::

Le signe de f′ commande les flèches : négatif à gauche de 2 (flèche descendante), positif à droite (flèche montante) ; la colonne x = 2 porte le minimum, point M de la courbe.

::: exemple Le même outil, sans situation : une fonction ln(u)
Étudier g(x) = ln(4 − x²).

1. Domaine : 4 − x² > 0 ⟺ −2 < x < 2, donc D = ]−2 ; 2[. De plus g(−x) = g(x), donc g est paire : on étudie sur [0 ; 2[ et on complète par symétrie.
2. Limite en 2⁻ : 4 − x² tend vers 0⁺, donc g(x) tend vers −∞ ; par parité, il en est de même en −2⁺ : les droites x = 2 et x = −2 sont asymptotes verticales.
3. Dérivée : g′(x) = u′(x)/u(x) = −2x/(4 − x²), du signe de −x car 4 − x² > 0 sur D. Donc g croît sur ]−2 ; 0] et décroît sur [0 ; 2[ : son maximum est g(0) = ln 4 ≈ 1,39.
4. Points sur l'axe des abscisses : g(x) = 0 ⟺ 4 − x² = 1 ⟺ x² = 3, donc x = −√3 ou x = √3 (≈ ±1,73).

:::

::: exemple Le même outil, pour la réciproque de f
Soit f(x) = x − 2 ln x, restreinte à [2 ; +∞[.

1. f est continue et strictement croissante sur [2 ; +∞[ (f′ > 0 sur ]2 ; +∞[) : c'est une bijection de [2 ; +∞[ sur [f(2) ; +∞[ = [2 − 2 ln 2 ; +∞[.
2. Le réel e est dans [2 ; +∞[ et f(e) = e − 2 × 1 = e − 2, donc f⁻¹(e − 2) = e.
3. f′(e) = 1 − 2/e = (e − 2)/e ≠ 0, donc (f⁻¹)′(e − 2) = 1/f′(e) = e/(e − 2) ≈ 3,78.

:::

::: piege
**Erreur : conclure que Δ : y = x est asymptote parce que f(x)/x tend vers 1.** Ici f(x)/x tend bien vers 1, mais f(x) − x = −2 ln x tend vers −∞ : l'écart ne se resserre pas, il grandit, de 9,2 pour x = 100 à 27,6 pour x = 1 000 000. L'erreur tente parce que le quotient tend vers 1 et que les deux courbes paraissent parallèles de loin. Mais une asymptote exige f(x) − x → 0 ; ici c'est une branche parabolique de direction Δ.
:::

::: methode Étudier une fonction contenant ln

1. Domaine : chaque expression sous un ln est strictement positive ; ajouter les autres conditions (dénominateur, racine).
2. Limites aux bornes du domaine, en levant les formes indéterminées par les croissances comparées ; une limite infinie en une borne finie donne une asymptote verticale.
3. Dérivée (avec (ln u)′ = u′/u), signe, puis tableau de variation avec les valeurs extrêmes.
4. Branches infinies : f(x)/x et f(x) − ax en ±∞ ; position par rapport à une droite par le signe d'une différence.
5. Si f est continue et strictement monotone sur un intervalle I : bijection de I sur f(I), calculée avec les valeurs et les limites aux bornes ; (f⁻¹)′(y₀) = 1/f′(x₀) avec x₀ = f⁻¹(y₀) et f′(x₀) ≠ 0.

Cas limite : f′ peut s'annuler en un point sans changer de signe ; il n'y a alors pas d'extremum. Si f′(x₀) = 0, f⁻¹ n'est pas dérivable en f(x₀).
:::

::: verifie À toi : le coût minimal d'une autre série
Étudie les variations de h(x) = 2x − ln x sur ]0 ; +∞[ et donne son minimum.

---

Domaine ]0 ; +∞[. h′(x) = 2 − 1/x = (2x − 1)/x, du signe de 2x − 1 : h décroît sur ]0 ; 1/2] et croît sur [1/2 ; +∞[. Le minimum est h(1/2) = 1 − ln(1/2) = 1 + ln 2 ≈ 1,69, car ln(1/2) = −ln 2.
:::

::: retenir
On étudie f avec ln dans l'ordre domaine, limites, dérivée (u′/u), tableau, branches infinies ; en +∞, f(x)/x → 1 ne suffit pas pour une asymptote : il faut f(x) − x → 0.
:::

## 🧪 Le logarithme décimal

Les chimistes comparent des concentrations qui s'étalent sur des puissances de 10 : 10⁻³ mol/L pour un jus acide, 10⁻⁷ pour l'eau pure. Pour les lire d'un coup d'œil, ils retiennent l'exposant : le pH d'une solution de concentration c en ions H₃O⁺ vaut pH = −log c.
Quelle fonction « lit » l'exposant d'une puissance de 10 ?

::: definition
La **fonction logarithme décimal**, notée log, est définie sur ]0 ; +∞[ par :
$$ log x = ln x / ln 10 $$
:::

::: figure Une échelle logarithmique de 1 à 1000 : chaque fois que x est multiplié par 10, log x augmente de 1 ; les repères 2 et 5 de chaque décade sont à 30 % et 70 % de sa longueur
<svg viewBox="0 0 340 120">
<title>Échelle logarithmique de 1 à 1000 : chaque multiplication par 10 avance de la même longueur, et 2 et 5 sont placés à 30 et 70 pour cent de la longueur d'une décade</title>
<line x1="40" y1="62" x2="322" y2="62" stroke="#0f172a" stroke-width="2"/>
<line x1="40" y1="53" x2="40" y2="71" stroke="#0f172a" stroke-width="1.6"/>
<line x1="68.3" y1="56" x2="68.3" y2="68" stroke="#0f172a" stroke-width="1.1"/>
<line x1="84.85" y1="56" x2="84.85" y2="68" stroke="#0f172a" stroke-width="1.1"/>
<line x1="96.59" y1="58.5" x2="96.59" y2="65.5" stroke="#0f172a" stroke-width="1.1"/>
<line x1="105.7" y1="56" x2="105.7" y2="68" stroke="#0f172a" stroke-width="1.1"/>
<line x1="113.15" y1="58.5" x2="113.15" y2="65.5" stroke="#0f172a" stroke-width="1.1"/>
<line x1="119.44" y1="58.5" x2="119.44" y2="65.5" stroke="#0f172a" stroke-width="1.1"/>
<line x1="124.89" y1="58.5" x2="124.89" y2="65.5" stroke="#0f172a" stroke-width="1.1"/>
<line x1="129.7" y1="58.5" x2="129.7" y2="65.5" stroke="#0f172a" stroke-width="1.1"/>
<line x1="134" y1="53" x2="134" y2="71" stroke="#0f172a" stroke-width="1.6"/>
<line x1="162.3" y1="56" x2="162.3" y2="68" stroke="#0f172a" stroke-width="1.1"/>
<line x1="178.85" y1="56" x2="178.85" y2="68" stroke="#0f172a" stroke-width="1.1"/>
<line x1="190.59" y1="58.5" x2="190.59" y2="65.5" stroke="#0f172a" stroke-width="1.1"/>
<line x1="199.7" y1="56" x2="199.7" y2="68" stroke="#0f172a" stroke-width="1.1"/>
<line x1="207.15" y1="58.5" x2="207.15" y2="65.5" stroke="#0f172a" stroke-width="1.1"/>
<line x1="213.44" y1="58.5" x2="213.44" y2="65.5" stroke="#0f172a" stroke-width="1.1"/>
<line x1="218.89" y1="58.5" x2="218.89" y2="65.5" stroke="#0f172a" stroke-width="1.1"/>
<line x1="223.7" y1="58.5" x2="223.7" y2="65.5" stroke="#0f172a" stroke-width="1.1"/>
<line x1="228" y1="53" x2="228" y2="71" stroke="#0f172a" stroke-width="1.6"/>
<line x1="256.3" y1="56" x2="256.3" y2="68" stroke="#0f172a" stroke-width="1.1"/>
<line x1="272.85" y1="56" x2="272.85" y2="68" stroke="#0f172a" stroke-width="1.1"/>
<line x1="284.59" y1="58.5" x2="284.59" y2="65.5" stroke="#0f172a" stroke-width="1.1"/>
<line x1="293.7" y1="56" x2="293.7" y2="68" stroke="#0f172a" stroke-width="1.1"/>
<line x1="301.15" y1="58.5" x2="301.15" y2="65.5" stroke="#0f172a" stroke-width="1.1"/>
<line x1="307.44" y1="58.5" x2="307.44" y2="65.5" stroke="#0f172a" stroke-width="1.1"/>
<line x1="312.89" y1="58.5" x2="312.89" y2="65.5" stroke="#0f172a" stroke-width="1.1"/>
<line x1="317.7" y1="58.5" x2="317.7" y2="65.5" stroke="#0f172a" stroke-width="1.1"/>
<line x1="322" y1="53" x2="322" y2="71" stroke="#0f172a" stroke-width="1.6"/>
<g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="68.3" y="86" text-anchor="middle" fill="#64748b" font-size="10">2</text><text x="105.7" y="86" text-anchor="middle" fill="#64748b" font-size="10">5</text><text x="162.3" y="86" text-anchor="middle" fill="#64748b" font-size="10">20</text><text x="199.7" y="86" text-anchor="middle" fill="#64748b" font-size="10">50</text><text x="256.3" y="86" text-anchor="middle" fill="#64748b" font-size="10">200</text><text x="293.7" y="86" text-anchor="middle" fill="#64748b" font-size="10">500</text><text x="40" y="44" text-anchor="middle" fill="#0f172a" font-size="12">1</text><text x="40" y="108" text-anchor="middle" fill="#0f6e56" font-size="12">0</text><text x="134" y="44" text-anchor="middle" fill="#0f172a" font-size="12">10</text><text x="134" y="108" text-anchor="middle" fill="#0f6e56" font-size="12">1</text><text x="228" y="44" text-anchor="middle" fill="#0f172a" font-size="12">100</text><text x="228" y="108" text-anchor="middle" fill="#0f6e56" font-size="12">2</text><text x="322" y="44" text-anchor="middle" fill="#0f172a" font-size="12">1000</text><text x="322" y="108" text-anchor="middle" fill="#0f6e56" font-size="12">3</text><text x="26" y="108" text-anchor="end" fill="#0f6e56" font-size="11">log x</text><text x="26" y="44" text-anchor="end" fill="#0f172a" font-size="11">x</text></g></svg>
:::

Les graduations 1, 10, 100, 1000 sont équidistantes : leur écart est log 10 = 1, et la ligne du bas donne les valeurs de log x qui leur correspondent, soit 0, 1, 2 et 3.

::: exemple Le pH d'un jus de citron
Le jus de citron a une concentration [H₃O⁺] = 6,3 × 10⁻³ mol/L.

1. pH = −log(6,3 × 10⁻³). Comme log est un multiple de ln, elle a les mêmes règles de calcul : log(ab) = log a + log b.
2. log(6,3 × 10⁻³) = log 6,3 + log 10⁻³ ≈ 0,80 − 3 = −2,20, car log 10ʳ = r (ici r = −3) et la calculatrice donne log 6,3 ≈ 0,80.
3. Donc pH ≈ 2,20.
4. Si le pH baisse de 1, la concentration est multipliée par 10 : pH′ = pH − 1 donne log c′ = log c + 1 = log(10c), donc c′ = 10c, car log est strictement croissante donc injective.

:::

::: exemple Le même outil, sans situation : deux calculs
1. log 5000 = log(5 × 10³) = log 5 + 3 ≈ 0,70 + 3 = 3,70. Avec la définition : ln 5000 / ln 10 ≈ 8,517 / 2,303 ≈ 3,70, même résultat.
2. Plus petit entier n tel que 3ⁿ ≥ 10⁹ : log est croissante, donc n log 3 ≥ log 10⁹ = 9. Comme log 3 ≈ 0,477, n ≥ 9/0,477 ≈ 18,9 ; donc n = 19. Contrôle : 3¹⁸ = 387 420 489 < 10⁹ et 3¹⁹ = 1 162 261 467 ≥ 10⁹.

:::

::: piege
**Erreur : confondre log et ln.** On écrit log 1000 = ln 1000 ≈ 6,91. L'erreur tente parce que les deux fonctions sont croissantes et valent 0 en 1. Mais log 1000 = log 10³ = 3, car log 10 = 1, alors que ln 1000 = 3 ln 10 ≈ 6,91 : les deux logarithmes diffèrent d'un facteur ln 10 ≈ 2,303.
:::

::: propriete
Pour x > 0 : log x = ln x / ln 10 ≈ 0,43 ln x, avec 1/ln 10 ≈ 0,43. On a log 1 = 0, log 10 = 1 et, pour tout rationnel r :
$$ log(10ʳ) = r $$
La fonction log a les mêmes règles de calcul que ln (log(ab) = log a + log b, log(a/b) = log a − log b, log(aʳ) = r log a), elle est strictement croissante et c'est une bijection de ]0 ; +∞[ sur ℝ : log x = r ⟺ x = 10ʳ.
Cas limite : log et ln ne coïncident qu'en x = 1, où elles valent toutes deux 0.
:::

::: verifie À toi : de la concentration au pH, et inversement
Une solution a un pH de 6,6. Donne sa concentration en ions H₃O⁺, d'abord sous la forme 10ʳ, puis en valeur approchée.

---

pH = −log c = 6,6 donne log c = −6,6 = log(10^(−6,6)), et log est injective : c = 10^(−6,6) = 10^(−33/5) mol/L. À la calculatrice, 10^(−6,6) ≈ 2,5 × 10⁻⁷ mol/L : un pH plus grand que 6 correspond à une concentration plus petite que 10⁻⁶.
:::

::: retenir
log x = ln x / ln 10 ≈ 0,43 ln x ; log 1 = 0, log 10 = 1, log(10ʳ) = r ; multiplier x par 10 ajoute 1 à log x.
:::

> 🏆 Tu sais maintenant transformer un produit en somme, résoudre une équation en défaisant son logarithme, lever les formes indéterminées par les croissances comparées, dériver et primitiver avec u′/u, mener l'étude complète d'une fonction à logarithme et lire une échelle de puissances de 10 avec log.
