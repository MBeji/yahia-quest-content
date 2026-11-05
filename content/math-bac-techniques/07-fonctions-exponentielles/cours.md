# ⚔️ Fonctions exponentielles — la réciproque de ln qui s'emballe

> 💡 «ln change les produits en sommes ; son inverse change les sommes en produits, et c'est la seule fonction qui se retrouve elle-même quand on la dérive.»

Au chapitre précédent, tu as construit ln, une bijection de ]0 ; +∞[ sur ℝ. Ce chapitre la retourne : on obtient l'exponentielle, et avec elle de quoi résoudre des équations, dériver, calculer des limites et modéliser une croissance. Huit notions, de la définition à l'étude complète d'une fonction.

## 🌱 exp, la réciproque de ln

Le chapitre 6 a montré que ln est une bijection de ]0 ; +∞[ sur ℝ : pour tout réel x, l'équation ln t = x a une seule solution t, et elle est strictement positive. Par exemple, il existe un seul réel t > 0 tel que ln t = 3.
Comment nommer ce réel, et que sait-on de lui quand x varie ?

::: definition
La **fonction exponentielle de base e**, notée **exp**, est la fonction réciproque de ln. Elle est définie sur ℝ, à valeurs dans ]0 ; +∞[, et pour tout réel x et tout réel y > 0 :
exp(x) = y ⇔ x = ln y
:::

| x         | −1   | 0 | 1    | 2    |
| --------- | ---- | - | ---- | ---- |
| exp(x) ≈  | 0,37 | 1 | 2,72 | 7,39 |

Lue de droite à gauche, la table donne ln(0,37) ≈ −1 et ln(7,39) ≈ 2 : exp et ln se défont l'une l'autre. Toute la seconde ligne est strictement positive.

::: exemple La solution de ln t = 3

1. ln est une bijection de ]0 ; +∞[ sur ℝ, donc l'équation ln t = 3 a une seule solution t > 0.
2. Par définition de exp, ln t = 3 ⇔ exp(3) = t : la solution est t = exp(3) ≈ 20,09 à la calculatrice.
3. Contrôle : ln(20,09) ≈ 3 ✓.

:::

::: exemple Le même outil, sans situation

1. exp(ln 5) = 5 : avec x = ln 5 et y = 5, l'égalité x = ln y est vraie, donc exp(x) = y.
2. ln(exp(−2)) = −2 : en posant y = exp(−2), l'équivalence exp(−2) = y ⇔ −2 = ln y donne ln y = −2.
3. exp(0) = 1 car ln 1 = 0, et exp(1) = e car ln e = 1.

:::

::: piege
**Erreur : résoudre exp(x) = −3 en écrivant x = ln(−3).** L'erreur tente parce que l'équivalence « exp(x) = y ⇔ x = ln y » semble s'écrire sans condition. Mais elle suppose y > 0 : ln(−3) n'existe pas, et pour cause, exp ne prend que des valeurs strictement positives. L'équation exp(x) = −3 n'a aucune solution.
:::

::: propriete
Pour tout réel x : exp(x) > 0 et ln(exp(x)) = x. Pour tout réel y > 0 : exp(ln y) = y. De plus exp(0) = 1 et exp(1) = e.
Comme ln est strictement croissante, exp l'est aussi : pour tous réels a et b, exp(a) = exp(b) ⇔ a = b et exp(a) < exp(b) ⇔ a < b. En particulier exp(a) > 1 ⇔ a > 0, et 0 < exp(a) < 1 ⇔ a < 0.
Cas limite : exp(ln y) n'a de sens que pour y > 0. Ainsi exp(ln(−2)) n'existe pas, alors que ln(exp(−2)) = −2 est bien défini.
:::

::: verifie À toi : une solution de signe connu
Résoudre dans ]0 ; +∞[ l'équation ln x = −2. Sans calculatrice, dire si la solution est plus petite ou plus grande que 1.

---

ln x = −2 ⇔ x = exp(−2), par définition de exp. Comme −2 < 0, on a 0 < exp(−2) < 1 : la solution est plus petite que 1. À la calculatrice, exp(−2) ≈ 0,135.
:::

::: retenir
exp est la réciproque de ln : exp(x) = y ⇔ x = ln y pour y > 0 ; elle est strictement positive et strictement croissante, avec exp(0) = 1 et exp(1) = e.
:::

## 🧩 Les règles de calcul et la notation eˣ

ln change un produit en somme : ln 6 = ln 2 + ln 3. Comme exp défait ln, elle doit faire le chemin inverse. Avec a = ln 2 et b = ln 3, on a exp(a) = 2 et exp(b) = 3, et a + b = ln 6, donc exp(a + b) = 6 = 2 × 3 = exp(a) × exp(b).
Cette égalité vaut-elle pour tous les réels a et b, et que deviennent l'opposé et la différence ?

::: exemple Pourquoi exp(a + b) = exp(a) × exp(b)

1. Posons x = exp(a) et y = exp(b) : deux réels strictement positifs, avec a = ln x et b = ln y, par définition de exp.
2. Alors a + b = ln x + ln y = ln(xy), par la propriété fondamentale de ln (x et y sont strictement positifs).
3. Par définition de exp, a + b = ln(xy) signifie exp(a + b) = xy = exp(a) × exp(b). Avec a = ln 2 et b = ln 3, on retrouve exp(ln 6) = 6 = 2 × 3 ✓.

:::

::: exemple L'opposé et la différence

1. exp(a) × exp(−a) = exp(a + (−a)) = exp(0) = 1, donc exp(−a) = 1/exp(a).
2. exp(a − b) = exp(a + (−b)) = exp(a) × exp(−b) = exp(a)/exp(b).
3. Application : exp(ln 12 − ln 3) = exp(ln 12)/exp(ln 3) = 12/3 = 4. Contrôle : ln 12 − ln 3 = ln 4, et exp(ln 4) = 4 ✓.

:::

::: exemple La notation eˣ

1. Pour un rationnel r, ln(eʳ) = r × ln e = r, car ln e = 1.
2. Or ln(exp(r)) = r aussi. Deux réels strictement positifs de même logarithme sont égaux : exp(r) = eʳ.
3. On étend alors cette notation à tout réel x : exp(x) s'écrit eˣ. Les règles précédentes deviennent e^(a + b) = eᵃ × eᵇ, e^(a − b) = eᵃ/eᵇ et e⁻ᵃ = 1/eᵃ.

:::

::: exemple Simplifier avec les règles

1. Soit E(x) = (e^(x + 1))² × e^(−2x)/√e. On a (e^(x + 1))² = e^(2x + 2), car (eᵃ)ʳ = e^(ar) avec r = 2.
2. √e = e^(1/2), car (e^(1/2))² = e¹ = e.
3. E(x) = e^(2x + 2) × e^(−2x)/e^(1/2) = e^(2x + 2 − 2x − 1/2) = e^(3/2). Le résultat ne dépend pas de x. Contrôle en x = 0 : e²/√e ≈ 7,389/1,649 ≈ 4,48 ≈ e^(3/2) ✓.

:::

::: piege
**Erreur : écrire e^(a + b) = eᵃ + eᵇ.** L'erreur tente parce que ln, elle, transforme bien les produits en sommes, et qu'on inverse mal le sens. Pourtant, avec a = b = 0, e⁰ = 1 alors que e⁰ + e⁰ = 2. La règle correcte change la somme des exposants en produit : e^(a + b) = eᵃ × eᵇ.
:::

::: propriete
Pour tous réels a et b et tout rationnel r :

| ln transforme…                  | exp transforme…                       |
| ------------------------------- | ------------------------------------- |
| ln(xy) = ln x + ln y            | e^(a + b) = eᵃ × eᵇ                   |
| ln(x/y) = ln x − ln y           | e^(a − b) = eᵃ/eᵇ                     |
| ln(1/x) = −ln x                 | e⁻ᵃ = 1/eᵃ                            |
| ln(xʳ) = r × ln x               | (eᵃ)ʳ = e^(ar)                        |

Dans les deux colonnes : e⁰ = 1 et e¹ = e.
Cas limite : eᵃ × e⁻ᵃ = e⁰ = 1, et (eᵃ)^(1/2) = e^(a/2) = √(eᵃ).
:::

::: verifie À toi : une expression qui ne dépend pas de x
Simplifier F(x) = (eˣ)³/(e^(x − 1) × e^(2x)).

---

(eˣ)³ = e^(3x) par la règle (eᵃ)ʳ = e^(ar). Au dénominateur, e^(x − 1) × e^(2x) = e^(3x − 1) (on ajoute les exposants). Donc F(x) = e^(3x − (3x − 1)) = e¹ = e : l'expression est constante. Contrôle en x = 0 : 1/e⁻¹ = e ✓.
:::

::: retenir
e^(a + b) = eᵃ × eᵇ, e^(a − b) = eᵃ/eᵇ, e⁻ᵃ = 1/eᵃ et (eᵃ)ʳ = e^(ar) : l'exponentielle change les sommes en produits.
:::

## ⚖️ Équations et inéquations exponentielles

Une culture compte Q(t) = 50 e^(0,2t) bactéries à l'instant t, en heures. Elle atteint 150 individus quand 50 e^(0,2t) = 150, soit e^(0,2t) = 3.
Comment passer de l'exponentielle à l'inconnue, et que devient une inéquation ?

::: exemple Quand la culture atteint-elle 150 individus ?

1. 50 e^(0,2t) = 150 ⇔ e^(0,2t) = 3, en divisant par 50.
2. Comme 3 > 0, e^(0,2t) = 3 ⇔ 0,2t = ln 3, par définition de exp.
3. t = ln 3/0,2 = 5 ln 3 ≈ 5,49 heures. Contrôle : 0,2 × 5,49 ≈ 1,10 ≈ ln 3, donc e^(1,10) ≈ 3 ✓.

:::

::: exemple Un changement d'inconnue

1. Résoudre e^(2x) + eˣ − 6 = 0. Comme e^(2x) = (eˣ)², on pose X = eˣ, avec X > 0.
2. L'équation devient X² + X − 6 = 0, de discriminant 1 + 24 = 25 : X = (−1 + 5)/2 = 2 ou X = (−1 − 5)/2 = −3.
3. Une exponentielle est strictement positive : on rejette X = −3.
4. eˣ = 2 ⇔ x = ln 2 ≈ 0,69. Contrôle : e^(2 ln 2) = 4 et 4 + 2 − 6 = 0 ✓.

:::

::: exemple Une inéquation du second degré en eˣ

1. Résoudre e^(2x) − 7eˣ + 10 ≤ 0. Avec X = eˣ > 0 : X² − 7X + 10 ≤ 0.
2. X² − 7X + 10 = (X − 2)(X − 5) est négatif entre ses racines : 2 ≤ X ≤ 5.
3. ln est strictement croissante, donc elle garde le sens : 2 ≤ eˣ ≤ 5 ⇔ ln 2 ≤ x ≤ ln 5.
4. S = [ln 2 ; ln 5] ≈ [0,69 ; 1,61]. Contrôle en x = 1 : e² − 7e + 10 ≈ 7,39 − 19,03 + 10 = −1,64 ≤ 0 ✓.

:::

::: piege
**Erreur : prendre ln terme à terme dans une somme.** Pour eˣ + 1 = 3, on écrit « x + ln 1 = ln 3 », donc x = ln 3 ≈ 1,10. L'erreur tente parce que ln « traverse » les produits, et l'on croit qu'elle traverse aussi les sommes. Mais ln(a + b) n'est pas ln a + ln b : on isole d'abord l'exponentielle, eˣ = 2, et alors x = ln 2 ≈ 0,69. Contrôle : e^(ln 3) + 1 = 4 ≠ 3.
:::

::: propriete
Pour tous réels u et v, e^u = e^v ⇔ u = v et e^u ≤ e^v ⇔ u ≤ v : exp est strictement croissante, le sens est conservé.
Pour un réel k > 0 : e^u = k ⇔ u = ln k ; e^u < k ⇔ u < ln k ; e^u > k ⇔ u > ln k.
Cas limite : si k ≤ 0, e^u = k et e^u < k n'ont aucune solution, et e^u > k est vraie pour tout u. Si 0 < k < 1, ln k est négatif : eˣ < 1/2 ⇔ x < ln(1/2) = −ln 2.
Application : pour Q(t) = Q₀ e^(kt) avec k > 0, la durée de doublement vérifie e^(kt) = 2, donc t = ln 2/k, quel que soit Q₀.
:::

::: methode Résoudre une équation ou une inéquation exponentielle
1. Isoler l'exponentielle : se ramener à e^u = e^v ou à e^u = k.
2. Si eˣ et e^(2x) apparaissent ensemble, poser X = eˣ, avec X > 0.
3. Résoudre en X, puis rejeter toute valeur X ≤ 0.
4. Revenir à x (par u = v, ou par ln), puis contrôler en remplaçant.

:::

::: verifie À toi : un changement d'inconnue
Résoudre dans ℝ l'équation e^(2x) − 3eˣ − 4 = 0.

---

On pose X = eˣ > 0 : X² − 3X − 4 = 0, soit (X − 4)(X + 1) = 0, donc X = 4 ou X = −1. On rejette X = −1, qui est négatif. Il reste eˣ = 4, donc x = ln 4 = 2 ln 2 ≈ 1,39. Contrôle : e^(2 ln 4) = 16, et 16 − 12 − 4 = 0 ✓.
:::

::: retenir
e^u = e^v ⇔ u = v, e^u = k ⇔ u = ln k pour k > 0, et lorsque eˣ et e^(2x) coexistent on pose X = eˣ avec X > 0.
:::

## 📈 Dérivée, variations et courbe de exp

La courbe de exp est la symétrique de celle de ln par rapport à la droite y = x. Sur la figure, au point A(0 ; 1) de la courbe de exp, la tangente T semble de pente 1, et exp(0) = 1.
Quelle est la dérivée de exp, et que dit-elle des variations et de la courbe ?

::: figure Les courbes de exp et de ln se déduisent l'une de l'autre par la symétrie d'axe y = x ; la tangente T en A(0 ; 1) reste sous la courbe de exp
<svg viewBox="0 0 340 270">
<title>Les courbes de exp et de ln, symétriques par rapport à la droite y = x, et la tangente T à la courbe de exp au point A(0 ; 1)</title>
<line x1="10.2" y1="169" x2="298.2" y2="169" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="298.2,169 290.2,165 290.2,173" fill="#0f172a"/>
<line x1="135" y1="260.2" x2="135" y2="10.6" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="135,10.6 131,18.6 139,18.6" fill="#0f172a"/>
<line x1="39" y1="166" x2="39" y2="172" stroke="#0f172a" stroke-width="1.2"/>
<line x1="87" y1="166" x2="87" y2="172" stroke="#0f172a" stroke-width="1.2"/>
<line x1="183" y1="166" x2="183" y2="172" stroke="#0f172a" stroke-width="1.2"/>
<line x1="231" y1="166" x2="231" y2="172" stroke="#0f172a" stroke-width="1.2"/>
<line x1="279" y1="166" x2="279" y2="172" stroke="#0f172a" stroke-width="1.2"/>
<line x1="132" y1="217" x2="138" y2="217" stroke="#0f172a" stroke-width="1.2"/>
<line x1="132" y1="121" x2="138" y2="121" stroke="#0f172a" stroke-width="1.2"/>
<line x1="132" y1="73" x2="138" y2="73" stroke="#0f172a" stroke-width="1.2"/>
<line x1="132" y1="25" x2="138" y2="25" stroke="#0f172a" stroke-width="1.2"/>
<line x1="43.8" y1="260.2" x2="293.4" y2="10.6" stroke="#64748b" stroke-width="1.6" stroke-dasharray="5 4"/>
<polyline points="10.2,165.43 12.22,165.28 14.25,165.12 16.27,164.95 18.29,164.78 20.32,164.6 22.34,164.41 24.36,164.21 26.39,164 28.41,163.79 30.43,163.57 32.46,163.33 34.48,163.09 36.5,162.83 38.53,162.57 40.55,162.29 42.57,162 44.6,161.7 46.62,161.39 48.65,161.06 50.67,160.72 52.69,160.36 54.72,159.99 56.74,159.6 58.76,159.19 60.79,158.77 62.81,158.33 64.83,157.87 66.86,157.39 68.88,156.89 70.9,156.37 72.93,155.83 74.95,155.26 76.97,154.67 79,154.05 81.02,153.41 83.04,152.74 85.07,152.04 87.09,151.31 89.11,150.55 91.14,149.75 93.16,148.92 95.18,148.06 97.21,147.16 99.23,146.22 101.25,145.24 103.28,144.21 105.3,143.15 107.32,142.03 109.35,140.87 111.37,139.66 113.39,138.4 115.42,137.08 117.44,135.71 119.46,134.27 121.49,132.78 123.51,131.22 125.54,129.59 127.56,127.89 129.58,126.12 131.61,124.28 133.63,122.35 135.65,120.34 137.68,118.25 139.7,116.06 141.72,113.78 143.75,111.41 145.77,108.93 147.79,106.34 149.82,103.64 151.84,100.83 153.86,97.89 155.89,94.83 157.91,91.64 159.93,88.31 161.96,84.83 163.98,81.21 166,77.43 168.03,73.49 170.05,69.37 172.07,65.08 174.1,60.61 176.12,55.94 178.14,51.08 180.17,46 182.19,40.7 184.21,35.18 186.24,29.42 188.26,23.41 190.28,17.14 192.31,10.6" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/>
<polyline points="142.18,260.2 143.48,252.21 144.78,245.36 146.08,239.37 147.38,234.05 148.68,229.25 149.98,224.89 151.28,220.9 152.58,217.21 153.88,213.79 155.18,210.59 156.48,207.59 157.78,204.77 159.08,202.11 160.38,199.58 161.68,197.19 162.98,194.9 164.28,192.72 165.58,190.64 166.88,188.64 168.18,186.72 169.48,184.88 170.78,183.1 172.08,181.39 173.38,179.73 174.68,178.13 175.98,176.59 177.28,175.09 178.58,173.63 179.88,172.22 181.18,170.85 182.48,169.52 183.78,168.22 185.08,166.96 186.39,165.73 187.69,164.53 188.99,163.36 190.29,162.22 191.59,161.1 192.89,160.01 194.19,158.94 195.49,157.9 196.79,156.88 198.09,155.88 199.39,154.9 200.69,153.94 201.99,153 203.29,152.08 204.59,151.17 205.89,150.28 207.19,149.41 208.49,148.56 209.79,147.71 211.09,146.89 212.39,146.07 213.69,145.27 214.99,144.49 216.29,143.71 217.59,142.95 218.89,142.2 220.19,141.46 221.49,140.74 222.79,140.02 224.09,139.31 225.39,138.62 226.69,137.93 227.99,137.26 229.29,136.59 230.59,135.93 231.89,135.29 233.19,134.65 234.49,134.01 235.79,133.39 237.09,132.78 238.39,132.17 239.69,131.57 240.99,130.98 242.29,130.39 243.59,129.81 244.89,129.24 246.19,128.68 247.49,128.12 248.79,127.57 250.09,127.02 251.39,126.48 252.69,125.95 253.99,125.42 255.29,124.9 256.59,124.38 257.89,123.87 259.19,123.37 260.49,122.87 261.8,122.37 263.1,121.88 264.4,121.4 265.7,120.92 267,120.44 268.3,119.97 269.6,119.51 270.9,119.05 272.2,118.59 273.5,118.14 274.8,117.69 276.1,117.24 277.4,116.8 278.7,116.37 280,115.94 281.3,115.51 282.6,115.08 283.9,114.66 285.2,114.24 286.5,113.83 287.8,113.42 289.1,113.01 290.4,112.61 291.7,112.21 293,111.81 294.3,111.42 295.6,111.03 296.9,110.64 298.2,110.26" fill="none" stroke="#d97706" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/>
<line x1="63" y1="193" x2="211.8" y2="44.2" stroke="#0f172a" stroke-width="2.2"/>
<circle cx="135" cy="121" r="3.8" fill="#0f172a" stroke="#ffffff" stroke-width="1.2"/>
<circle cx="183" cy="169" r="3.8" fill="#0f172a" stroke="#ffffff" stroke-width="1.2"/>
<g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="39" y="184" text-anchor="middle" fill="#0f172a" font-size="11">−2</text><text x="87" y="184" text-anchor="middle" fill="#0f172a" font-size="11">−1</text><text x="183" y="184" text-anchor="middle" fill="#0f172a" font-size="11">1</text><text x="231" y="184" text-anchor="middle" fill="#0f172a" font-size="11">2</text><text x="279" y="184" text-anchor="middle" fill="#0f172a" font-size="11">3</text><text x="128" y="221" text-anchor="end" fill="#0f172a" font-size="11">−1</text><text x="128" y="125" text-anchor="end" fill="#0f172a" font-size="11">1</text><text x="128" y="77" text-anchor="end" fill="#0f172a" font-size="11">2</text><text x="128" y="29" text-anchor="end" fill="#0f172a" font-size="11">3</text><text x="294.2" y="161" text-anchor="end" fill="#0f172a" font-size="12" font-style="italic">x</text><text x="143" y="20.6" text-anchor="start" fill="#0f172a" font-size="12" font-style="italic">y</text><text x="148" y="115" text-anchor="start" fill="#0f172a" font-size="13">A</text><text x="190" y="162" text-anchor="start" fill="#0f172a" font-size="13">A′</text><text x="186.36" y="17" text-anchor="start" fill="#0f6e56" font-size="13">exp</text><text x="296.2" y="126.26" text-anchor="end" fill="#d97706" font-size="13">ln</text><text x="240" y="86" text-anchor="start" fill="#64748b" font-size="12">y = x</text><text x="217.8" y="48.2" text-anchor="start" fill="#0f172a" font-size="13">T</text></g>
</svg>
:::

Le point A(0 ; 1) de la courbe de exp a pour symétrique A′(1 ; 0) sur celle de ln, car exp(0) = 1 ⇔ ln 1 = 0. La pente 1 de T est le nombre dérivé de exp en 0 : l'exemple suivant le justifie.

::: exemple Pourquoi exp′ = exp

1. ln est dérivable sur ]0 ; +∞[ et ln′(y) = 1/y ne s'annule jamais : d'après le chapitre 3, sa réciproque exp est dérivable sur ℝ.
2. On dérive l'égalité ln(exp(x)) = x, composée de deux fonctions dérivables : exp′(x)/exp(x) = 1.
3. Donc exp′(x) = exp(x) pour tout réel x. Comme exp(x) > 0, exp′ est strictement positive : exp est strictement croissante.

:::

::: exemple Les tangentes aux points A(0 ; 1) et B(1 ; e)

1. La tangente au point d'abscisse a a pour équation y = exp′(a)(x − a) + exp(a), avec exp′(a) = eᵃ.
2. En a = 0 : y = 1 × (x − 0) + 1, soit y = x + 1. C'est la droite T de la figure.
3. En a = 1 : y = e(x − 1) + e = ex.
4. Près de 0, la courbe colle à T : eˣ ≈ 1 + x, et le taux d'accroissement (eˣ − 1)/x tend vers exp′(0) = 1. Par exemple e^(0,02) ≈ 1,02 (la calculatrice donne 1,0202).

:::

::: exemple La courbe reste au-dessus de la tangente T

1. Posons h(x) = eˣ − x − 1, de dérivée h′(x) = eˣ − 1.
2. h′(x) ≥ 0 ⇔ eˣ ≥ 1 ⇔ x ≥ 0 : h décroît sur ]−∞ ; 0], puis croît sur [0 ; +∞[.
3. Le minimum est h(0) = 1 − 0 − 1 = 0. Donc h(x) ≥ 0 pour tout x, c'est-à-dire eˣ ≥ x + 1, avec égalité seulement en 0.

:::

::: piege
**Erreur : dériver eˣ comme une puissance, (eˣ)′ = x eˣ⁻¹.** L'erreur tente parce que la règle (xⁿ)′ = n xⁿ⁻¹ est celle qu'on a le plus souvent appliquée. Mais ici la variable est dans l'exposant, pas dans la base : (eˣ)′ = eˣ. Contrôle en x = 0 : la formule fausse donne 0, alors que la tangente T a pour pente 1.
:::

::: propriete
exp est dérivable sur ℝ et (eˣ)′ = eˣ ; elle est strictement croissante sur ℝ. Pour tout réel x : eˣ ≥ x + 1. De plus lim x→0 (eˣ − 1)/x = 1, ce qui s'écrit eˣ ≈ 1 + x pour x voisin de 0.
Cas limite : l'approximation ne vaut que près de 0. En x = 1, e ≈ 2,72 alors que 1 + 1 = 2.
:::

::: verifie À toi : une inégalité par les variations
Étudier les variations de g(x) = eˣ − 2x et en déduire que eˣ > 2x pour tout réel x.

---

g′(x) = eˣ − 2, et g′(x) ≥ 0 ⇔ eˣ ≥ 2 ⇔ x ≥ ln 2 : g décroît sur ]−∞ ; ln 2], puis croît. Son minimum est g(ln 2) = 2 − 2 ln 2 = 2(1 − ln 2). Comme 2 < e, on a ln 2 < ln e = 1, donc ce minimum est strictement positif : g(x) > 0, c'est-à-dire eˣ > 2x pour tout réel x.
:::

::: retenir
(eˣ)′ = eˣ : exp est strictement croissante, la tangente en A(0 ; 1) est y = x + 1, et eˣ ≥ x + 1 pour tout réel x.
:::

## ♾️ Limites et croissances comparées

Voici quelques valeurs de eˣ et de x².

| x    | 1    | 5      | 10         | 20          |
| ---- | ---- | ------ | ---------- | ----------- |
| eˣ   | 2,72 | 148,41 | 22 026,47  | 4,85 × 10⁸  |
| x²   | 1    | 25     | 100        | 400         |

Dès x = 20, eˣ dépasse x² plus d'un million de fois, et l'écart se creuse à chaque ligne : eˣ semble dépasser très vite tout polynôme.
Que valent les limites de eˣ en +∞ et en −∞, et comment lever des formes indéterminées comme x eˣ ou eˣ/x² ?

::: exemple Pourquoi eˣ/x tend vers +∞

1. On pose X = eˣ. Quand x → +∞, X → +∞ (exp strictement croissante, eˣ ≥ x + 1), et x = ln X.
2. eˣ/x = X/ln X = 1/((ln X)/X).
3. Le chapitre 6 donne lim X→+∞ (ln X)/X = 0, par valeurs positives : le quotient 1/((ln X)/X) tend vers +∞ ✓.

:::

::: exemple Lever une forme +∞ − ∞

1. Soit lim x→+∞ (eˣ − x²). Les deux termes tendent vers +∞ : c'est la forme indéterminée +∞ − ∞.
2. On factorise le terme dominant : eˣ − x² = x²(eˣ/x² − 1).
3. Par croissance comparée, eˣ/x² → +∞, donc eˣ/x² − 1 → +∞, et x² → +∞ : le produit tend vers +∞.

:::

::: exemple Une limite en −∞

1. Soit lim x→−∞ x³eˣ : forme indéterminée (−∞) × 0.
2. On pose X = −x : X → +∞ et x³eˣ = (−X)³ × e^(−X) = −X³/e^X.
3. X³/e^X = 1/(e^X/X³), et e^X/X³ → +∞ : le quotient tend vers 0. Donc lim x→−∞ x³eˣ = 0.

:::

::: piege
**Erreur : conclure que x¹⁰/eˣ tend vers +∞ parce que x¹⁰ est « de degré 10 ».** L'erreur tente parce que, pour de petites valeurs, x¹⁰ est bien plus grand que eˣ : en x = 10, 10¹⁰ = 10 000 000 000 contre e¹⁰ ≈ 22 026. Mais la limite se joue à l'infini, et eˣ/xⁿ → +∞ pour tout entier n : le quotient x¹⁰/eˣ tend vers 0.
:::

::: propriete
lim x→+∞ eˣ = +∞ et lim x→−∞ eˣ = 0, par valeurs positives. Pour tout entier n ≥ 1 : lim x→+∞ eˣ/xⁿ = +∞ et lim x→−∞ xⁿeˣ = 0.

| x                  | −∞ |   | +∞ |
| ------------------ | -- | - | -- |
| signe de (eˣ)′     |    | + |    |
| variation de eˣ    | 0  | ↗ | +∞ |

Conséquences : l'axe des abscisses est asymptote à la courbe de exp en −∞ ; en +∞, la courbe a une branche parabolique de direction (Oy), puisque eˣ/x → +∞.
Cas limite : x eˣ en +∞ n'est pas indéterminé, c'est +∞ × +∞ = +∞.
:::

::: verifie À toi : une puissance contre l'exponentielle
Calculer lim x→+∞ x³e⁻ˣ.

---

x³e⁻ˣ = x³/eˣ = 1/(eˣ/x³). Par croissance comparée, eˣ/x³ → +∞, donc le quotient 1/(eˣ/x³) tend vers 0. Le résultat vaut 0 : l'exponentielle l'emporte sur la puissance.
:::

::: retenir
eˣ → +∞ en +∞ et eˣ → 0 en −∞ ; l'exponentielle l'emporte sur toute puissance : eˣ/xⁿ → +∞ en +∞ et xⁿeˣ → 0 en −∞.
:::

## ⛓️ Dériver eᵘ et primitiver u′eᵘ

Un plat sort du four. Sa température, en °C, est T(t) = 20 + 60 e^(−0,1t) à l'instant t, en minutes. Pour savoir à quelle vitesse il refroidit, il faut dériver T, mais l'exponentielle porte sur −0,1t et non sur t seul.
Comment dériver e^(u(x)) quand u n'est pas x, et comment remonter à une primitive ?

::: exemple La vitesse de refroidissement

1. T(t) = 20 + 60 e^(u(t)) avec u(t) = −0,1t, dérivable sur ℝ, de dérivée u′(t) = −0,1.
2. (e^u)′ = u′ e^u : c'est la dérivée d'une composée, on multiplie la dérivée de exp par celle de u.
3. T′(t) = 60 × (−0,1) e^(−0,1t) = −6 e^(−0,1t).
4. e^(−0,1t) > 0, donc T′(t) < 0 : le plat refroidit sans cesse. À t = 0, T′(0) = −6 °C par minute ; à t = 10, T′(10) = −6e⁻¹ ≈ −2,21 °C par minute.

:::

::: exemple Le même outil, sans situation

1. f(x) = e^(x² − 3x) sur ℝ : u(x) = x² − 3x, u′(x) = 2x − 3, donc f′(x) = (2x − 3) e^(x² − 3x).
2. g(x) = e^(1/x) sur ℝ* : u(x) = 1/x, u′(x) = −1/x², donc g′(x) = −e^(1/x)/x².

:::

::: exemple Remonter vers une primitive

1. Soit f(x) = x e^(x²) sur ℝ. Avec u(x) = x², u′(x) = 2x, donc f = (1/2) × 2x e^(x²) = (1/2) u′ e^u.
2. Une primitive de u′e^u est e^u : F(x) = (1/2) e^(x²).
3. Contrôle : F′(x) = (1/2) × 2x e^(x²) = f(x) ✓.
4. De même, e⁻ˣ = −u′e^u avec u = −x, donc une primitive de e⁻ˣ est −e⁻ˣ.

:::

::: piege
**Erreur : oublier le facteur u′, en dérivant comme en primitivant.** On écrit (e^(3x))′ = e^(3x), ou « une primitive de e^(2x) est e^(2x) ». L'erreur tente parce que exp est sa propre dérivée. Mais la variable intérieure compte : (e^(3x))′ = 3e^(3x), et une primitive de e^(2x) est (1/2) e^(2x). Contrôle : près de 0, e^(3x) ≈ 1 + 3x a pour pente 3, pas 1.
:::

::: propriete
Si u est dérivable sur D, alors e^u est dérivable sur D et (e^u)′ = u′ e^u.
Si u est dérivable sur un intervalle I, les primitives sur I de u′ e^u sont les fonctions e^u + k, k réel. En particulier, pour a ≠ 0, une primitive de x ↦ e^(ax + b) est (1/a) e^(ax + b).
Cas limite : il faut u′ à un facteur constant près. e^(x²) seule n'a pas cette forme : il manque le facteur 2x, et x n'est pas une constante qu'on peut compenser.
:::

::: verifie À toi : une primitive imposée
Déterminer la primitive F de f(x) = x² e^(x³) sur ℝ qui s'annule en 0.

---

Avec u(x) = x³, u′(x) = 3x², donc f = (1/3) u′ e^u et F(x) = (1/3) e^(x³) + k. La condition F(0) = 0 donne 1/3 + k = 0, soit k = −1/3. Donc F(x) = (e^(x³) − 1)/3. Contrôle : F′(x) = (1/3) × 3x² e^(x³) = f(x) ✓.
:::

::: retenir
(e^u)′ = u′ e^u, et les primitives de u′ e^u sont e^u + k : on compense toujours la constante manquante devant u′.
:::

## 🔢 Les fonctions aˣ et xʳ

Un capital double chaque année : après n années il vaut C₀ × 2ⁿ. Pour n entier, 2ⁿ est un produit répété. Mais que signifie 2^(√2), et comment trouver la durée pour laquelle le capital est multiplié par 100 ?
Le chapitre 6 donne ln(aʳ) = r ln a, donc aʳ = e^(r ln a) pour a > 0 et r rationnel. Cette écriture garde un sens pour tout réel : elle sert de définition.

::: definition
Soit a > 0. La fonction x ↦ aˣ est définie sur ℝ par aˣ = e^(x ln a).
Soit r un rationnel. La fonction x ↦ xʳ est définie sur ]0 ; +∞[ par xʳ = e^(r ln x).
:::

::: figure Les courbes de 2ˣ et de (1/2)ˣ passent toutes deux par (0 ; 1) et se déduisent l'une de l'autre par la symétrie d'axe (Oy)
<svg viewBox="0 0 340 215">
<title>Les courbes de x ↦ 2ˣ et de x ↦ (1/2)ˣ, qui passent toutes deux par le point (0 ; 1) et sont symétriques par rapport à l'axe des ordonnées</title>
<line x1="20.4" y1="192" x2="319.6" y2="192" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="319.6,192 311.6,188 311.6,196" fill="#0f172a"/>
<line x1="170" y1="192" x2="170" y2="7.1" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="170,7.1 166,15.1 174,15.1" fill="#0f172a"/>
<line x1="38" y1="189" x2="38" y2="195" stroke="#0f172a" stroke-width="1.2"/>
<line x1="82" y1="189" x2="82" y2="195" stroke="#0f172a" stroke-width="1.2"/>
<line x1="126" y1="189" x2="126" y2="195" stroke="#0f172a" stroke-width="1.2"/>
<line x1="214" y1="189" x2="214" y2="195" stroke="#0f172a" stroke-width="1.2"/>
<line x1="258" y1="189" x2="258" y2="195" stroke="#0f172a" stroke-width="1.2"/>
<line x1="302" y1="189" x2="302" y2="195" stroke="#0f172a" stroke-width="1.2"/>
<line x1="167" y1="170.5" x2="173" y2="170.5" stroke="#0f172a" stroke-width="1.2"/>
<line x1="167" y1="149" x2="173" y2="149" stroke="#0f172a" stroke-width="1.2"/>
<line x1="167" y1="106" x2="173" y2="106" stroke="#0f172a" stroke-width="1.2"/>
<line x1="167" y1="20" x2="173" y2="20" stroke="#0f172a" stroke-width="1.2"/>
<polyline points="20.4,189.96 23.24,189.87 26.08,189.77 28.91,189.67 31.75,189.56 34.59,189.45 37.43,189.34 40.27,189.21 43.1,189.09 45.94,188.95 48.78,188.82 51.62,188.67 54.46,188.52 57.29,188.36 60.13,188.19 62.97,188.02 65.81,187.84 68.65,187.64 71.48,187.45 74.32,187.24 77.16,187.02 80,186.79 82.84,186.55 85.67,186.3 88.51,186.04 91.35,185.77 94.19,185.49 97.03,185.19 99.86,184.88 102.7,184.55 105.54,184.21 108.38,183.86 111.22,183.48 114.05,183.09 116.89,182.69 119.73,182.26 122.57,181.82 125.41,181.35 128.24,180.86 131.08,180.35 133.92,179.82 136.76,179.26 139.6,178.68 142.43,178.07 145.27,177.44 148.11,176.77 150.95,176.07 153.79,175.35 156.62,174.58 159.46,173.79 162.3,172.96 165.14,172.09 167.98,171.17 170.81,170.22 173.65,169.23 176.49,168.19 179.33,167.1 182.17,165.96 185,164.77 187.84,163.52 190.68,162.22 193.52,160.86 196.36,159.43 199.19,157.95 202.03,156.39 204.87,154.76 207.71,153.06 210.55,151.28 213.38,149.42 216.22,147.47 219.06,145.43 221.9,143.3 224.74,141.08 227.57,138.75 230.41,136.31 233.25,133.77 236.09,131.1 238.93,128.32 241.76,125.41 244.6,122.36 247.44,119.18 250.28,115.85 253.12,112.37 255.95,108.73 258.79,104.92 261.63,100.94 264.47,96.78 267.31,92.42 270.14,87.87 272.98,83.11 275.82,78.13 278.66,72.92 281.5,67.48 284.33,61.78 287.17,55.83 290.01,49.6 292.85,43.09 295.69,36.28 298.52,29.17 301.36,21.72 304.2,13.93" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/>
<polyline points="35.8,13.93 38.64,21.72 41.48,29.17 44.31,36.28 47.15,43.09 49.99,49.6 52.83,55.83 55.67,61.78 58.5,67.48 61.34,72.92 64.18,78.13 67.02,83.11 69.86,87.87 72.69,92.42 75.53,96.78 78.37,100.94 81.21,104.92 84.05,108.73 86.88,112.37 89.72,115.85 92.56,119.18 95.4,122.36 98.24,125.41 101.07,128.32 103.91,131.1 106.75,133.77 109.59,136.31 112.43,138.75 115.26,141.08 118.1,143.3 120.94,145.43 123.78,147.47 126.62,149.42 129.45,151.28 132.29,153.06 135.13,154.76 137.97,156.39 140.81,157.95 143.64,159.43 146.48,160.86 149.32,162.22 152.16,163.52 155,164.77 157.83,165.96 160.67,167.1 163.51,168.19 166.35,169.23 169.19,170.22 172.02,171.17 174.86,172.09 177.7,172.96 180.54,173.79 183.38,174.58 186.21,175.35 189.05,176.07 191.89,176.77 194.73,177.44 197.57,178.07 200.4,178.68 203.24,179.26 206.08,179.82 208.92,180.35 211.76,180.86 214.59,181.35 217.43,181.82 220.27,182.26 223.11,182.69 225.95,183.09 228.78,183.48 231.62,183.86 234.46,184.21 237.3,184.55 240.14,184.88 242.97,185.19 245.81,185.49 248.65,185.77 251.49,186.04 254.33,186.3 257.16,186.55 260,186.79 262.84,187.02 265.68,187.24 268.52,187.45 271.35,187.64 274.19,187.84 277.03,188.02 279.87,188.19 282.71,188.36 285.54,188.52 288.38,188.67 291.22,188.82 294.06,188.95 296.9,189.09 299.73,189.21 302.57,189.34 305.41,189.45 308.25,189.56 311.09,189.67 313.92,189.77 316.76,189.87 319.6,189.96" fill="none" stroke="#2563eb" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/>
<circle cx="170" cy="170.5" r="3.8" fill="#0f172a" stroke="#ffffff" stroke-width="1.2"/>
<circle cx="214" cy="149" r="3.8" fill="#0f6e56" stroke="#ffffff" stroke-width="1.2"/>
<circle cx="126" cy="149" r="3.8" fill="#2563eb" stroke="#ffffff" stroke-width="1.2"/>
<g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="38" y="207" text-anchor="middle" fill="#0f172a" font-size="11">−3</text><text x="82" y="207" text-anchor="middle" fill="#0f172a" font-size="11">−2</text><text x="126" y="207" text-anchor="middle" fill="#0f172a" font-size="11">−1</text><text x="214" y="207" text-anchor="middle" fill="#0f172a" font-size="11">1</text><text x="258" y="207" text-anchor="middle" fill="#0f172a" font-size="11">2</text><text x="302" y="207" text-anchor="middle" fill="#0f172a" font-size="11">3</text><text x="159" y="174.5" text-anchor="end" fill="#0f172a" font-size="11">1</text><text x="163" y="153" text-anchor="end" fill="#0f172a" font-size="11">2</text><text x="163" y="110" text-anchor="end" fill="#0f172a" font-size="11">4</text><text x="163" y="24" text-anchor="end" fill="#0f172a" font-size="11">8</text><text x="315.6" y="184" text-anchor="end" fill="#0f172a" font-size="12" font-style="italic">x</text><text x="178" y="17.1" text-anchor="start" fill="#0f172a" font-size="12" font-style="italic">y</text><text x="288.8" y="19.7" text-anchor="end" fill="#0f6e56" font-size="12">a = 2</text><text x="51.2" y="19.7" text-anchor="start" fill="#2563eb" font-size="12">a = 1/2</text></g>
</svg>
:::

Les deux courbes passent par (0 ; 1), car a⁰ = e⁰ = 1. Elles sont symétriques par rapport à (Oy), car (1/2)ˣ = e^(−x ln 2) = 2⁻ˣ : pour a > 1 la courbe monte, pour a < 1 elle descend.

::: exemple Quand le capital est-il multiplié par 100 ?

1. C₀ × 2ˣ = 100 C₀ ⇔ 2ˣ = 100.
2. 2ˣ = e^(x ln 2), donc l'équation s'écrit e^(x ln 2) = 100 ⇔ x ln 2 = ln 100, puisque 100 > 0.
3. x = ln 100/ln 2 ≈ 4,605/0,693 ≈ 6,64 ans. Contrôle : 6,64 × ln 2 ≈ 4,60 ≈ ln 100 ✓.

:::

::: exemple Dériver aˣ et xʳ

1. aˣ = e^u avec u(x) = x ln a, et u′(x) = ln a (a est fixé, ln a est une constante). Donc (aˣ)′ = ln a × aˣ.
2. aˣ > 0 : le signe de la dérivée est celui de ln a. Pour a = 2, ln 2 > 0 : croissante. Pour a = 1/2, ln(1/2) = −ln 2 < 0 : décroissante. Pour a = 1, ln 1 = 0 et 1ˣ = 1 : constante.
3. (xʳ)′ = (e^(r ln x))′ = (r/x) e^(r ln x) = r xʳ⁻¹. Pour r = 3/2 en x = 4 : 4^(3/2) = 8 et (3/2) × 4^(1/2) = 3.

:::

::: exemple Une inéquation avec une base inférieure à 1

1. Résoudre (1/3)ˣ > 9. On écrit (1/3)ˣ = e^(x ln(1/3)) et 9 = e^(ln 9), avec ln 9 = 2 ln 3.
2. L'inéquation équivaut à x ln(1/3) > 2 ln 3, puisque exp est strictement croissante.
3. ln(1/3) = −ln 3 < 0 : en divisant par un nombre négatif, le sens s'inverse. x < 2 ln 3/(−ln 3) = −2.
4. S = ]−∞ ; −2[. Contrôle : en x = −3, (1/3)⁻³ = 27 > 9 ✓ ; en x = −1, (1/3)⁻¹ = 3 < 9 donc −1 n'est pas solution ✓.

:::

::: piege
**Erreur : lire 3ˣ = 7 avec ln(3ˣ) = ln 3 + ln x.** Cela donnerait ln x = ln 7 − ln 3 et x = 7/3. L'erreur tente parce que ln change les produits en sommes, et que 3ˣ « ressemble » à un produit 3 × x. Mais ln(3ˣ) = x ln 3, donc x = ln 7/ln 3 ≈ 1,77. Contrôle : 3^(7/3) ≈ 12,98 ≠ 7.
:::

::: propriete
Pour a > 0, x et y réels et r rationnel : a^(x + y) = aˣ × aʸ, a⁻ˣ = 1/aˣ, a^(x − y) = aˣ/aʸ et (aˣ)ʳ = a^(rx).
x ↦ aˣ est dérivable sur ℝ, de dérivée ln a × aˣ : strictement croissante si a > 1, strictement décroissante si 0 < a < 1, constante égale à 1 si a = 1. Pour a ≠ 1 et b > 0 : aˣ = b ⇔ x = ln b/ln a.
Cas limite : si 0 < a < 1, ln a < 0 et les inéquations en aˣ changent de sens.
:::

::: verifie À toi : une base inférieure à 1
Résoudre dans ℝ l'inéquation (1/2)ˣ < 1/16, puis vérifier avec x = 5 et x = 3.

---

(1/2)ˣ = e^(x ln(1/2)) et 1/16 = e^(−4 ln 2) avec ln(1/2) = −ln 2. L'inéquation devient −x ln 2 < −4 ln 2, et en divisant par −ln 2 < 0 le sens s'inverse : x > 4. En x = 5, (1/2)⁵ = 1/32 < 1/16 ✓ ; en x = 3, (1/2)³ = 1/8 > 1/16 : x = 3 n'est pas solution ✓.
:::

::: retenir
aˣ = e^(x ln a) et xʳ = e^(r ln x) : (aˣ)′ = ln a × aˣ ; aˣ croît si a > 1, décroît si 0 < a < 1, et x ln a se divise par ln a en renversant le sens quand a < 1.
:::

## 🎨 Étudier une fonction e^(u(x))

Un signal augmente puis retombe selon f(x) = e^(2x − x²). On veut savoir où il est maximal, ce qu'il devient aux extrémités et à quoi sa courbe ressemble.
Comment mener l'étude complète d'une fonction du type e^(u(x)) ?

::: figure Un sommet en (1 ; e), deux points (0 ; 1) et (2 ; 1) à la même hauteur, et l'axe des abscisses frôlé aux deux bouts
<svg viewBox="0 0 340 244">
<title>La courbe de f(x) = e^(2x − x²) : un sommet au point (1 ; e), symétrique par rapport à la droite x = 1 et collée à l'axe des abscisses aux deux extrémités</title>
<line x1="20" y1="222" x2="314" y2="222" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="314,222 306,218 306,226" fill="#0f172a"/>
<line x1="104" y1="222" x2="104" y2="-2" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="104,-2 100,6 108,6" fill="#0f172a"/>
<line x1="44" y1="219" x2="44" y2="225" stroke="#0f172a" stroke-width="1.2"/>
<line x1="164" y1="219" x2="164" y2="225" stroke="#0f172a" stroke-width="1.2"/>
<line x1="224" y1="219" x2="224" y2="225" stroke="#0f172a" stroke-width="1.2"/>
<line x1="284" y1="219" x2="284" y2="225" stroke="#0f172a" stroke-width="1.2"/>
<line x1="101" y1="152" x2="107" y2="152" stroke="#0f172a" stroke-width="1.2"/>
<line x1="101" y1="82" x2="107" y2="82" stroke="#0f172a" stroke-width="1.2"/>
<line x1="164" y1="222" x2="164" y2="15.5" stroke="#64748b" stroke-width="1.4" stroke-dasharray="5 4"/>
<line x1="104" y1="152" x2="224" y2="152" stroke="#64748b" stroke-width="1.2" stroke-dasharray="3 3"/>
<polyline points="20,221.4 22.06,221.29 24.11,221.17 26.17,221.03 28.23,220.86 30.29,220.67 32.34,220.46 34.4,220.21 36.46,219.93 38.51,219.6 40.57,219.24 42.63,218.82 44.69,218.35 46.74,217.82 48.8,217.23 50.86,216.57 52.91,215.82 54.97,215 57.03,214.08 59.09,213.06 61.14,211.93 63.2,210.69 65.26,209.32 67.31,207.82 69.37,206.18 71.43,204.4 73.49,202.46 75.54,200.35 77.6,198.08 79.66,195.62 81.71,192.99 83.77,190.17 85.83,187.15 87.89,183.94 89.94,180.53 92,176.92 94.06,173.11 96.11,169.1 98.17,164.9 100.23,160.51 102.29,155.94 104.34,151.2 106.4,146.29 108.46,141.23 110.51,136.04 112.57,130.73 114.63,125.32 116.69,119.83 118.74,114.28 120.8,108.69 122.86,103.1 124.91,97.52 126.97,91.99 129.03,86.53 131.09,81.17 133.14,75.94 135.2,70.88 137.26,66 139.31,61.35 141.37,56.95 143.43,52.82 145.49,49 147.54,45.51 149.6,42.37 151.66,39.6 153.71,37.23 155.77,35.27 157.83,33.72 159.89,32.61 161.94,31.94 164,31.72 166.06,31.94 168.11,32.61 170.17,33.72 172.23,35.27 174.29,37.23 176.34,39.6 178.4,42.37 180.46,45.51 182.51,49 184.57,52.82 186.63,56.95 188.69,61.35 190.74,66 192.8,70.88 194.86,75.94 196.91,81.17 198.97,86.53 201.03,91.99 203.09,97.52 205.14,103.1 207.2,108.69 209.26,114.28 211.31,119.83 213.37,125.32 215.43,130.73 217.49,136.04 219.54,141.23 221.6,146.29 223.66,151.2 225.71,155.94 227.77,160.51 229.83,164.9 231.89,169.1 233.94,173.11 236,176.92 238.06,180.53 240.11,183.94 242.17,187.15 244.23,190.17 246.29,192.99 248.34,195.62 250.4,198.08 252.46,200.35 254.51,202.46 256.57,204.4 258.63,206.18 260.69,207.82 262.74,209.32 264.8,210.69 266.86,211.93 268.91,213.06 270.97,214.08 273.03,215 275.09,215.82 277.14,216.57 279.2,217.23 281.26,217.82 283.31,218.35 285.37,218.82 287.43,219.24 289.49,219.6 291.54,219.93 293.6,220.21 295.66,220.46 297.71,220.67 299.77,220.86 301.83,221.03 303.89,221.17 305.94,221.29 308,221.4" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/>
<circle cx="164" cy="31.72" r="3.8" fill="#0f6e56" stroke="#ffffff" stroke-width="1.2"/>
<circle cx="104" cy="152" r="3.8" fill="#0f172a" stroke="#ffffff" stroke-width="1.2"/>
<circle cx="224" cy="152" r="3.8" fill="#0f172a" stroke="#ffffff" stroke-width="1.2"/>
<g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="44" y="237" text-anchor="middle" fill="#0f172a" font-size="11">−1</text><text x="164" y="237" text-anchor="middle" fill="#0f172a" font-size="11">1</text><text x="224" y="237" text-anchor="middle" fill="#0f172a" font-size="11">2</text><text x="284" y="237" text-anchor="middle" fill="#0f172a" font-size="11">3</text><text x="97" y="156" text-anchor="end" fill="#0f172a" font-size="11">1</text><text x="97" y="86" text-anchor="end" fill="#0f172a" font-size="11">2</text><text x="310" y="214" text-anchor="end" fill="#0f172a" font-size="12" font-style="italic">x</text><text x="112" y="8" text-anchor="start" fill="#0f172a" font-size="12" font-style="italic">y</text><text x="172" y="24.72" text-anchor="start" fill="#0f6e56" font-size="12">(1 ; e)</text><text x="169" y="213.6" text-anchor="start" fill="#64748b" font-size="11">x = 1</text></g>
</svg>
:::

La courbe monte, atteint un sommet, redescend : on lit un sommet en (1 ; e), des points (0 ; 1) et (2 ; 1) à la même hauteur et l'axe (Ox) frôlé de chaque côté. L'étude suivante justifie chaque lecture.

::: exemple Étude de f(x) = e^(2x − x²)

1. Domaine et symétrie : u(x) = 2x − x² est définie sur ℝ, donc D = ℝ. De plus u(2 − x) = (2 − x) x = u(x), donc f(2 − x) = f(x) : la courbe est symétrique par rapport à la droite x = 1.
2. Limites : u(x) → −∞ quand x → ±∞, car −x² l'emporte. Donc f(x) = e^(u(x)) → 0 : l'axe des abscisses est asymptote en −∞ et en +∞.
3. Dérivée : f′(x) = u′(x) e^(u(x)) = (2 − 2x) e^(2x − x²). Comme e^u > 0, f′ a le signe de u′(x) = 2 − 2x.
4. Tableau de variation :

| x                | −∞ |   | 1 |   | +∞ |
| ---------------- | -- | - | - | - | -- |
| signe de f′(x)   |    | + | 0 | − |    |
| variation de f   | 0  | ↗ | e | ↘ | 0  |

5. Valeurs : f(1) = e^(2 − 1) = e ≈ 2,72 et f(0) = f(2) = e⁰ = 1, ce que la figure montre.

:::

::: exemple Prolonger par continuité : g(x) = e^(−1/x) pour x > 0

1. En 0 par valeurs positives, u(x) = −1/x → −∞, donc g(x) → 0. La limite est un réel : on prolonge g par continuité en posant g(0) = 0.
2. Dérivabilité à droite en 0 : (g(x) − g(0))/x = e^(−1/x)/x. Avec X = 1/x → +∞, cette quantité vaut X e^(−X) = X/e^X, qui tend vers 0 : la demi-tangente en 0 est horizontale.
3. En +∞, u(x) → 0, donc g(x) → e⁰ = 1 : la droite y = 1 est asymptote.
4. g′(x) = (1/x²) e^(−1/x) > 0 : g est strictement croissante, de 0 à 1.

:::

::: piege
**Erreur : conclure que f′ est positive parce que e^u > 0.** On lit f′(x) = (2 − 2x) e^(2x − x²) et l'on dit « une exponentielle est positive, donc f croît ». L'erreur tente parce que ce facteur est toujours positif, et l'on oublie l'autre. Seul e^u est positif : f′ a le signe de u′. Contrôle : f′(2) = −2 e⁰ = −2 < 0, la courbe descend en x = 2.
:::

::: methode Étudier f = e^u
1. Domaine de u, parité ou symétrie de f.
2. Limites de u aux bornes, puis de f : u → −∞ donne f → 0, u → +∞ donne f → +∞, et u → ℓ donne f → e^ℓ.
3. f′ = u′ e^u a le signe de u′ : f a les mêmes variations que u, puisque exp est croissante.
4. Tableau de variation, extremum, asymptotes (y = 0, ou y = e^ℓ), prolongement par continuité éventuel.
5. Quelques points, puis la courbe.

:::

::: verifie À toi : un minimum
Étudier g(x) = e^(x² − 4x) : domaine, limites, variations et extremum.

---

u(x) = x² − 4x est définie sur ℝ, donc D = ℝ. Comme u(x) → +∞ quand x → ±∞, g(x) → +∞ aux deux bouts. g′(x) = (2x − 4) e^(x² − 4x) a le signe de 2x − 4 : g décroît sur ]−∞ ; 2], puis croît sur [2 ; +∞[. Son minimum est g(2) = e^(4 − 8) = e⁻⁴ ≈ 0,018.
:::

::: retenir
Pour e^u, f′ = u′ e^u a le signe de u′ : f varie comme u, f → 0 quand u → −∞, et le facteur e^u ne change jamais le signe.
:::

> 🏆 Les huit portes sont franchies : tu sais définir exp, la manier, résoudre avec elle, la dériver, comparer sa croissance, dériver et primitiver eᵘ, définir aˣ et xʳ, et mener l'étude d'une fonction e^(u(x)). Prochaine étape : le calcul intégral, qui mesure ce que ces fonctions dessinent.
