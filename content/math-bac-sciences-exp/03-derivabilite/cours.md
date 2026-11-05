# ⚔️ Dérivabilité — quand la pente gouverne la courbe

> 💡 «Une courbe se lit comme un paysage : la dérivée dit, en chaque point, si l'on monte, si l'on descend ou si l'on touche un sommet.»

Les limites et la continuité t'ont appris à suivre une fonction ; la dérivée t'apprend à lire sa pente. Huit notions te mènent du nombre dérivé aux points d'inflexion, en passant par les théorèmes de Rolle et des accroissements finis. On suppose acquis ce qui précède dans le tome : limites, continuité, théorème des valeurs intermédiaires, et les dérivées de troisième année (polynômes, quotients).

## 🧭 Nombre dérivé, tangente et approximation affine

Quel est le volume d'un cube d'arête 1,0002 m ? L'arête est presque 1 m, donc le volume est presque 1 m³ ; mais de combien le dépasse-t-il ?
Près d'un point, une courbe se confond avec sa tangente : tout revient à connaître la pente de cette tangente.

::: definition
Soit f définie sur un intervalle ouvert I et a un réel de I. On dit que f est **dérivable en a** s'il existe un réel, noté f′(a), tel que :

$$ lim x→a (f(x) − f(a))/(x − a) = f′(a) $$

Le quotient est le **taux d'accroissement** (la pente de la corde entre les points d'abscisses a et x) ; f′(a) est le **nombre dérivé**. La **tangente** à C_f au point A(a ; f(a)) est la droite de pente f′(a) passant par A :

$$ y = f′(a)(x − a) + f(a) $$
:::

::: figure La tangente en A(1 ; 1) a pour pente 3 : tout près de A, la courbe de x ↦ x³ et la droite se confondent
<svg viewBox="0 0 340 240">
<title>Courbe de x ↦ x³ pour x entre −0,2 et 2, et sa tangente au point A(1 ; 1), droite de pente 3 d'équation y = 3x − 2</title>
<line x1="28" y1="184.3" x2="336" y2="184.3" stroke="#0f172a" stroke-width="1.6"/>
<line x1="60.55" y1="222" x2="60.55" y2="6" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="336,184.3 328,180.3 328,188.3" fill="#0f172a"/>
<polygon points="60.55,6 56.55,14 64.55,14" fill="#0f172a"/>
<polyline points="34.0,184.46 36.43,184.42 38.87,184.38 41.3,184.36 43.73,184.34 46.17,184.32 48.6,184.31 51.03,184.3 53.47,184.3 55.9,184.3 58.33,184.3 60.77,184.3 63.2,184.3 65.63,184.3 68.07,184.29 70.5,184.29 72.93,184.28 75.37,184.27 77.8,184.25 80.23,184.23 82.67,184.21 85.1,184.17 87.53,184.13 89.97,184.08 92.4,184.02 94.83,183.96 97.27,183.88 99.7,183.79 102.13,183.69 104.57,183.57 107.0,183.45 109.43,183.31 111.87,183.15 114.3,182.98 116.73,182.79 119.17,182.59 121.6,182.37 124.03,182.13 126.47,181.87 128.9,181.59 131.33,181.29 133.77,180.97 136.2,180.63 138.63,180.26 141.07,179.88 143.5,179.46 145.93,179.02 148.37,178.56 150.8,178.07 153.23,177.55 155.67,177.01 158.1,176.43 160.53,175.83 162.97,175.2 165.4,174.53 167.83,173.84 170.27,173.11 172.7,172.35 175.13,171.55 177.57,170.73 180.0,169.86 182.43,168.96 184.87,168.02 187.3,167.05 189.73,166.04 192.17,164.99 194.6,163.9 197.03,162.76 199.47,161.59 201.9,160.38 204.33,159.12 206.77,157.82 209.2,156.48 211.63,155.09 214.07,153.65 216.5,152.17 218.93,150.65 221.37,149.07 223.8,147.45 226.23,145.78 228.67,144.05 231.1,142.28 233.53,140.46 235.97,138.58 238.4,136.65 240.83,134.67 243.27,132.63 245.7,130.54 248.13,128.39 250.57,126.19 253.0,123.93 255.43,121.61 257.87,119.23 260.3,116.79 262.73,114.3 265.17,111.74 267.6,109.12 270.03,106.44 272.47,103.69 274.9,100.89 277.33,98.01 279.77,95.07 282.2,92.07 284.63,89.0 287.07,85.86 289.5,82.65 291.93,79.38 294.37,76.03 296.8,72.62 299.23,69.13 301.67,65.57 304.1,61.94 306.53,58.24 308.97,54.46 311.4,50.61 313.83,46.68 316.27,42.68 318.7,38.59 321.13,34.44 323.57,30.2 326.0,25.88" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"/>
<line x1="80.45" y1="214.99" x2="299.45" y2="116.97" stroke="#b45309" stroke-width="2"/>
<line x1="193.27" y1="181.3" x2="193.27" y2="187.3" stroke="#0f172a" stroke-width="1.2"/>
<text x="193.27" y="198.3" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text>
<line x1="326.0" y1="181.3" x2="326.0" y2="187.3" stroke="#0f172a" stroke-width="1.2"/>
<text x="326.0" y="198.3" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text>
<line x1="57.55" y1="164.5" x2="63.55" y2="164.5" stroke="#0f172a" stroke-width="1.2"/>
<text x="54.55" y="168.5" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text>
<line x1="57.55" y1="105.09" x2="63.55" y2="105.09" stroke="#0f172a" stroke-width="1.2"/>
<text x="54.55" y="109.09" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4</text>
<line x1="57.55" y1="25.88" x2="63.55" y2="25.88" stroke="#0f172a" stroke-width="1.2"/>
<text x="54.55" y="29.88" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">8</text>
<line x1="193.27" y1="184.3" x2="193.27" y2="164.5" stroke="#94a3b8" stroke-width="1.1" stroke-dasharray="3 3"/>
<line x1="60.55" y1="164.5" x2="193.27" y2="164.5" stroke="#94a3b8" stroke-width="1.1" stroke-dasharray="3 3"/>
<circle cx="193.27" cy="164.5" r="4" fill="#0f172a"/>
<text x="200.27" y="178.5" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">A</text>
<text x="249.0" y="155.76" text-anchor="start" font-size="12" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">pente f′(1) = 3</text>
<text x="249.56" y="96.11" text-anchor="start" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">C_f</text>
</svg>
:::

La pente de la droite orange est le f′(1) de la formule, et l'abscisse 1 est le a : la droite et la courbe sont indiscernables tout près de A.

::: exemple Le cube d'arête 1,0002 m

1. Soit g(x) = x³, un polynôme : g′(x) = 3x², car on dérive terme à terme.
2. En a = 1 : g(1) = 1 et g′(1) = 3, donc la tangente est y = 3(x − 1) + 1 = 3x − 2.
3. Pour h petit, g(1 + h) ≈ g(1) + g′(1)h : c'est l'**approximation affine**, qui remplace la courbe par sa tangente. Ici h = 0,0002.
4. (1,0002)³ ≈ 1 + 3 × 0,0002 = 1,0006 m³ : le cube dépasse 1 m³ d'environ 0,0006 m³ (la calculatrice donne 1,00060012).

:::

::: exemple Deux tangentes d'une même courbe

1. f(x) = x³ + 3x² + 3x + 1 est un polynôme : f′(x) = 3x² + 6x + 3.
2. En 0 : f(0) = 1 et f′(0) = 3, donc y = 3(x − 0) + 1 = 3x + 1.
3. En 1 : f(1) = 1 + 3 + 3 + 1 = 8 et f′(1) = 3 + 6 + 3 = 12, donc y = 12(x − 1) + 8 = 12x − 4.

:::

::: piege
**Erreur : écrire y = f′(a)x + f(a).** Pour g(x) = x³ en a = 1, on écrit y = 3x + 1. L'erreur tente parce que, dans y = mx + p, le nombre m est la pente et que f(a) ressemble à une ordonnée à l'origine. Mais f(a) est l'ordonnée au point d'abscisse a, pas en 0 : la droite y = 3x + 1 passe par le point (1 ; 4), pas par A(1 ; 1). La bonne formule translate de a : y = 3(x − 1) + 1 = 3x − 2.
:::

::: propriete
Si f est dérivable en a, alors f(a + h) ≈ f(a) + f′(a)h pour h voisin de 0, et la tangente en a a pour équation y = f′(a)(x − a) + f(a).
Cas limite : si f′(a) = 0, la tangente est horizontale, d'équation y = f(a).
:::

::: verifie À toi : la tangente en −1
Soit f(x) = 2x² + x. Donner l'équation de la tangente à C_f au point d'abscisse −1.

---

f(−1) = 2 − 1 = 1 et f′(x) = 4x + 1, donc f′(−1) = −3. La tangente est y = f′(−1)(x + 1) + f(−1) = −3(x + 1) + 1 = −3x − 2. Contrôle : elle passe par (−1 ; 1), puisque −3 × (−1) − 2 = 1.
:::

::: retenir
f′(a) est la limite du taux d'accroissement : c'est la pente de la tangente y = f′(a)(x − a) + f(a), et f(a + h) ≈ f(a) + f′(a)h.
:::

## 🗡️ Dérivabilité à gauche, à droite et sur un intervalle

Le profil d'une rampe de skate est la courbe de f(x) = |x² − 1|. En x = 1, la planche arrive de la gauche et repart vers la droite : la rampe a-t-elle une seule pente en ce point ?

::: figure En A(1 ; 0), la courbe de x ↦ |x² − 1| a deux demi-tangentes de pentes différentes : −2 à gauche, 2 à droite
<svg viewBox="0 0 340 240">
<title>Courbe de x ↦ |x² − 1| et, au point A(1 ; 0), deux demi-tangentes de pentes −2 à gauche et 2 à droite</title>
<line x1="28" y1="184.0" x2="336" y2="184.0" stroke="#0f172a" stroke-width="1.6"/>
<line x1="180.0" y1="222" x2="180.0" y2="6" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="336,184.0 328,180.0 328,188.0" fill="#0f172a"/>
<polygon points="180.0,6 176.0,14 184.0,14" fill="#0f172a"/>
<polyline points="34.0,34.0 35.46,37.98 36.92,41.92 38.38,45.82 39.84,49.68 41.3,53.5 42.76,57.28 44.22,61.02 45.68,64.72 47.14,68.38 48.6,72.0 50.06,75.58 51.52,79.12 52.98,82.62 54.44,86.08 55.9,89.5 57.36,92.88 58.82,96.22 60.28,99.52 61.74,102.78 63.2,106.0 64.66,109.18 66.12,112.32 67.58,115.42 69.04,118.48 70.5,121.5 71.96,124.48 73.42,127.42 74.88,130.32 76.34,133.18 77.8,136.0 79.26,138.78 80.72,141.52 82.18,144.22 83.64,146.88 85.1,149.5 86.56,152.08 88.02,154.62 89.48,157.12 90.94,159.58 92.4,162.0 93.86,164.38 95.32,166.72 96.78,169.02 98.24,171.28 99.7,173.5 101.16,175.68 102.62,177.82 104.08,179.92 105.54,181.98 107.0,184.0 108.46,182.02 109.92,180.08 111.38,178.18 112.84,176.32 114.3,174.5 115.76,172.72 117.22,170.98 118.68,169.28 120.14,167.62 121.6,166.0 123.06,164.42 124.52,162.88 125.98,161.38 127.44,159.92 128.9,158.5 130.36,157.12 131.82,155.78 133.28,154.48 134.74,153.22 136.2,152.0 137.66,150.82 139.12,149.68 140.58,148.58 142.04,147.52 143.5,146.5 144.96,145.52 146.42,144.58 147.88,143.68 149.34,142.82 150.8,142.0 152.26,141.22 153.72,140.48 155.18,139.78 156.64,139.12 158.1,138.5 159.56,137.92 161.02,137.38 162.48,136.88 163.94,136.42 165.4,136.0 166.86,135.62 168.32,135.28 169.78,134.98 171.24,134.72 172.7,134.5 174.16,134.32 175.62,134.18 177.08,134.08 178.54,134.02 180.0,134.0 181.46,134.02 182.92,134.08 184.38,134.18 185.84,134.32 187.3,134.5 188.76,134.72 190.22,134.98 191.68,135.28 193.14,135.62 194.6,136.0 196.06,136.42 197.52,136.88 198.98,137.38 200.44,137.92 201.9,138.5 203.36,139.12 204.82,139.78 206.28,140.48 207.74,141.22 209.2,142.0 210.66,142.82 212.12,143.68 213.58,144.58 215.04,145.52 216.5,146.5 217.96,147.52 219.42,148.58 220.88,149.68 222.34,150.82 223.8,152.0 225.26,153.22 226.72,154.48 228.18,155.78 229.64,157.12 231.1,158.5 232.56,159.92 234.02,161.38 235.48,162.88 236.94,164.42 238.4,166.0 239.86,167.62 241.32,169.28 242.78,170.98 244.24,172.72 245.7,174.5 247.16,176.32 248.62,178.18 250.08,180.08 251.54,182.02 253.0,184.0 254.46,181.98 255.92,179.92 257.38,177.82 258.84,175.68 260.3,173.5 261.76,171.28 263.22,169.02 264.68,166.72 266.14,164.38 267.6,162.0 269.06,159.58 270.52,157.12 271.98,154.62 273.44,152.08 274.9,149.5 276.36,146.88 277.82,144.22 279.28,141.52 280.74,138.78 282.2,136.0 283.66,133.18 285.12,130.32 286.58,127.42 288.04,124.48 289.5,121.5 290.96,118.48 292.42,115.42 293.88,112.32 295.34,109.18 296.8,106.0 298.26,102.78 299.72,99.52 301.18,96.22 302.64,92.88 304.1,89.5 305.56,86.08 307.02,82.62 308.48,79.12 309.94,75.58 311.4,72.0 312.86,68.38 314.32,64.72 315.78,61.02 317.24,57.28 318.7,53.5 320.16,49.68 321.62,45.82 323.08,41.92 324.54,37.98 326.0,34.0" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"/>
<line x1="212.85" y1="129.0" x2="253.0" y2="184.0" stroke="#b45309" stroke-width="2.2"/>
<line x1="253.0" y1="184.0" x2="293.15" y2="129.0" stroke="#7c3aed" stroke-width="2.2"/>
<line x1="107.0" y1="181.0" x2="107.0" y2="187.0" stroke="#0f172a" stroke-width="1.2"/>
<text x="107.0" y="198.0" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−1</text>
<line x1="253.0" y1="181.0" x2="253.0" y2="187.0" stroke="#0f172a" stroke-width="1.2"/>
<text x="253.0" y="198.0" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text>
<circle cx="253.0" cy="184.0" r="4" fill="#0f172a"/>
<text x="259.0" y="176.0" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">A</text>
<text x="187.3" y="103.0" text-anchor="start" font-size="12" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">pente −2</text>
<text x="254.46" y="103.0" text-anchor="start" font-size="12" font-weight="700" fill="#7c3aed" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">pente 2</text>
<text x="58.25" y="46.5" text-anchor="start" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">C_f</text>
</svg>
:::

Les deux segments tracés en A sont les deux limites de la corde, l'une venue de la gauche (pente −2) et l'autre de la droite (pente 2) : la courbe n'a pas une tangente mais deux demi-tangentes.

::: definition
Le **nombre dérivé à gauche** et le **nombre dérivé à droite** de f en a sont :

$$ f′_g(a) = lim x→a⁻ (f(x) − f(a))/(x − a) $$

$$ f′_d(a) = lim x→a⁺ (f(x) − f(a))/(x − a) $$

f est dérivable en a si et seulement si elle est dérivable à gauche et à droite en a avec f′_g(a) = f′_d(a).
f est **dérivable sur [a ; b]** si elle est dérivable sur ]a ; b[, à droite en a et à gauche en b ; on définit de même la dérivabilité sur [a ; b[, ]a ; b] ou sur un intervalle infini.
:::

::: exemple La rampe en x = 1

1. f(1) = 0. Pour x > 1, x² − 1 > 0 : le taux est (x² − 1)/(x − 1) = x + 1, qui tend vers 2. Donc f′_d(1) = 2.
2. Pour −1 < x < 1, x² − 1 < 0 donc f(x) = 1 − x² : le taux est (1 − x²)/(x − 1) = −(x + 1), qui tend vers −2. Donc f′_g(1) = −2.
3. −2 ≠ 2 : f n'est pas dérivable en 1. La courbe y a un **point anguleux**, bien qu'elle y soit continue.

:::

::: exemple Un paramètre qui recolle deux branches

1. f(x) = x² + x + c si x < 0 et f(x) = 2√(x + 1) si x ≥ 0. On a f(0) = 2, et le recollement exige lim x→0⁻ f(x) = c = 2.
2. À gauche, le taux (x² + x)/x = x + 1 tend vers 1 : f′_g(0) = 1.
3. À droite, on multiplie par le conjugué, car (√(x + 1) − 1)(√(x + 1) + 1) = x : le taux 2(√(x + 1) − 1)/x = 2/(√(x + 1) + 1) tend vers 1 : f′_d(0) = 1.
4. f′_g(0) = f′_d(0) = 1 : f est dérivable en 0 et f′(0) = 1.

:::

::: piege
**Erreur : fixer c par la continuité et conclure que f est dérivable.** Pour g(x) = x² + c si x < 0 et g(x) = 2√(x + 1) si x ≥ 0, la continuité donne bien c = 2 et l'on écrit « donc g est dérivable en 0 ». L'erreur tente parce que le recollement fait disparaître le saut de la courbe. Mais la continuité ne dit rien des pentes : g′_g(0) = lim x²/x = 0 alors que g′_d(0) = 1, donc g n'est pas dérivable en 0.
:::

::: propriete
Pour étudier une fonction définie par morceaux en a, on calcule séparément f′_g(a) et f′_d(a) à partir des taux d'accroissement, puis on les compare.
Cas limite : si le taux tend vers +∞ ou −∞, f n'est pas dérivable en a et la courbe a une **demi-tangente verticale**. Ainsi x ↦ √x n'est pas dérivable à droite en 0, car (√x − 0)/x = 1/√x tend vers +∞.
:::

::: verifie À toi : un point anguleux
Étudier la dérivabilité en 3 de h(x) = |x² − 9|.

---

h(3) = 0. Pour x > 3, x² − 9 > 0 : le taux est (x² − 9)/(x − 3) = x + 3 → 6, donc h′_d(3) = 6. Pour x < 3 proche de 3, x² − 9 < 0 donc h(x) = 9 − x² : le taux est −(x + 3) → −6, donc h′_g(3) = −6. Comme −6 ≠ 6, h n'est pas dérivable en 3 : point anguleux, demi-tangentes de pentes −6 et 6.
:::

::: retenir
f est dérivable en a exactement quand f′_g(a) = f′_d(a) ; la continuité ne suffit pas, et un taux qui tend vers ±∞ donne une demi-tangente verticale.
:::

## 🔮 Dérivées usuelles, opérations et composée

La courbe de f(x) = sin(x²) a, en x = 1, une pente que l'on peut estimer par le taux entre 1 et 1,001 : environ 1,08. Ni cos 1 ≈ 0,54 (la dérivée « brute » du sinus) ni 2 (celle de x²) ne conviennent. Quelle règle fabrique 1,08 pour une fonction emboîtée dans une autre ?

::: exemple Le sinus de x²

1. On pose u(x) = x², donc u′(x) = 2x, et f = sin∘u : on dérive de l'extérieur vers l'intérieur.
2. La dérivée de sin évaluée en u(x) est cos(x²), à multiplier par la dérivée de l'intérieur : f′(x) = 2x × cos(x²).
3. En x = 1 : f′(1) = 2 cos 1 ≈ 1,08, ce que suggérait le calcul numérique.

:::

::: exemple Un quotient avec ses ensembles de définition

1. f(x) = (3x + 1)/(x² − 4) est définie sur ℝ \ {−2 ; 2}, et f′ aussi : on dérive là où le dénominateur ne s'annule pas.
2. Avec u = 3x + 1, u′ = 3, v = x² − 4 et v′ = 2x : f′(x) = (u′v − v′u)/v² = (3(x² − 4) − 2x(3x + 1))/(x² − 4)².
3. On développe le numérateur : 3x² − 12 − 6x² − 2x = −3x² − 2x − 12, donc f′(x) = (−3x² − 2x − 12)/(x² − 4)².

:::

::: exemple Une racine

1. Pour a > 0, (√x − √a)/(x − a) = 1/(√x + √a) : on multiplie par le conjugué, car (√x − √a)(√x + √a) = x − a.
2. Ce taux tend vers 1/(2√a) : x ↦ √x est dérivable sur ]0 ; +∞[ et (√x)′ = 1/(2√x).
3. Soit h(x) = √(2x − 1) sur ]1/2 ; +∞[. Avec u(x) = 2x − 1 > 0 et u′(x) = 2, h′(x) = u′/(2√u) = 2/(2√(2x − 1)) = 1/√(2x − 1).

:::

::: piege
**Erreur : oublier la dérivée de l'intérieur.** Pour f(x) = sin(x²), on écrit f′(x) = cos(x²). L'erreur tente parce que la table donne (sin)′ = cos et que l'on s'arrête à la première règle connue. Mais f′(1) vaudrait alors cos 1 ≈ 0,54, loin des 1,08 mesurés : il manque le facteur u′(x) = 2x de la fonction intérieure, d'où f′(x) = 2x cos(x²).
:::

::: propriete
**Dérivées usuelles** : (xⁿ)′ = nxⁿ⁻¹ sur ℝ ; (1/xⁿ)′ = −n/xⁿ⁺¹ sur tout intervalle de ℝ* ; (sin(ax + b))′ = a cos(ax + b) ; (cos(ax + b))′ = −a sin(ax + b) ; (tan(ax + b))′ = a(1 + tan²(ax + b)) là où tan est définie.
**Opérations** (f et g dérivables) : (f + g)′ = f′ + g′ ; (af)′ = af′ ; (fg)′ = f′g + g′f ; (1/f)′ = −f′/f² ; (f/g)′ = (f′g − g′f)/g² ; (fⁿ)′ = nf′fⁿ⁻¹ ; (1/fⁿ)′ = −nf′/fⁿ⁺¹, là où f (ou g, pour un quotient) ne s'annule pas.
**Composée (théorème admis)** : si f est dérivable en a et g dérivable en f(a), alors g∘f est dérivable en a et (g∘f)′(a) = f′(a) × g′(f(a)). Sur un intervalle : si f est dérivable sur I et g sur un intervalle J contenant f(I), (g∘f)′(x) = f′(x) × g′(f(x)) pour tout x de I.
Cas limite : x ↦ √x est continue en 0 mais non dérivable en 0, donc √u n'est dérivable que là où u > 0, et (√u)′ = u′/(2√u).
:::

::: verifie À toi : produit et composée
Dériver k(x) = x² cos(2x) sur ℝ.

---

On applique (uv)′ = u′v + v′u avec u = x² (u′ = 2x) et v = cos(2x), où v′ = −2 sin(2x) d'après la composée (l'intérieur 2x a pour dérivée 2). Donc k′(x) = 2x cos(2x) + x² × (−2 sin(2x)) = 2x cos(2x) − 2x² sin(2x).
:::

::: retenir
On dérive de l'extérieur vers l'intérieur : (g∘f)′ = f′ × g′∘f, d'où (uⁿ)′ = nu′uⁿ⁻¹ et (√u)′ = u′/(2√u) là où u > 0.
:::

## 🛡️ Théorème de Rolle

Un ballon est lancé vers le haut ; sa hauteur est h(t) = 20t − 5t² mètres à l'instant t secondes. Il retombe à son point de départ à t = 4. À un instant entre le lancement et le retour, la montée s'arrête et la descente commence : peut-on affirmer, sans calcul, qu'il y a un instant où la pente de la courbe est nulle ?

::: figure Comme h(0) = h(4), la courbe monte puis redescend : en c, sa tangente est horizontale
<svg viewBox="0 0 340 240">
<title>Courbe de h(t) = 20t − 5t² pour t entre 0 et 4 : elle part de 0, atteint 20 à t = 2 où la tangente est horizontale, et revient à 0 à t = 4</title>
<line x1="28" y1="192.57" x2="336" y2="192.57" stroke="#0f172a" stroke-width="1.6"/>
<line x1="61.55" y1="222" x2="61.55" y2="6" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="336,192.57 328,188.57 328,196.57" fill="#0f172a"/>
<polygon points="61.55,6 57.55,14 65.55,14" fill="#0f172a"/>
<polyline points="61.55,192.57 63.38,187.85 65.22,183.21 67.06,178.64 68.89,174.16 70.73,169.75 72.57,165.43 74.4,161.18 76.24,157.02 78.08,152.93 79.91,148.92 81.75,144.99 83.58,141.14 85.42,137.37 87.26,133.68 89.09,130.07 90.93,126.54 92.77,123.09 94.6,119.71 96.44,116.42 98.28,113.21 100.11,110.07 101.95,107.02 103.79,104.04 105.62,101.14 107.46,98.33 109.3,95.59 111.13,92.93 112.97,90.35 114.81,87.85 116.64,85.43 118.48,83.09 120.31,80.83 122.15,78.64 123.99,76.54 125.82,74.52 127.66,72.57 129.5,70.71 131.33,68.92 133.17,67.21 135.01,65.59 136.84,64.04 138.68,62.57 140.52,61.18 142.35,59.87 144.19,58.64 146.03,57.49 147.86,56.42 149.7,55.43 151.53,54.52 153.37,53.68 155.21,52.93 157.04,52.25 158.88,51.66 160.72,51.14 162.55,50.71 164.39,50.35 166.23,50.07 168.06,49.87 169.9,49.75 171.74,49.71 173.57,49.75 175.41,49.87 177.25,50.07 179.08,50.35 180.92,50.71 182.75,51.14 184.59,51.66 186.43,52.25 188.26,52.93 190.1,53.68 191.94,54.52 193.77,55.43 195.61,56.42 197.45,57.49 199.28,58.64 201.12,59.87 202.96,61.18 204.79,62.57 206.63,64.04 208.47,65.59 210.3,67.21 212.14,68.92 213.97,70.71 215.81,72.57 217.65,74.52 219.48,76.54 221.32,78.64 223.16,80.83 224.99,83.09 226.83,85.43 228.67,87.85 230.5,90.35 232.34,92.93 234.18,95.59 236.01,98.33 237.85,101.14 239.69,104.04 241.52,107.02 243.36,110.07 245.19,113.21 247.03,116.42 248.87,119.71 250.7,123.09 252.54,126.54 254.38,130.07 256.21,133.68 258.05,137.37 259.89,141.14 261.72,144.99 263.56,148.92 265.4,152.93 267.23,157.02 269.07,161.18 270.91,165.43 272.74,169.75 274.58,174.16 276.42,178.64 278.25,183.21 280.09,187.85 281.92,192.57" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"/>
<line x1="111.13" y1="49.71" x2="232.34" y2="49.71" stroke="#b45309" stroke-width="2" stroke-dasharray="6 4"/>
<line x1="171.74" y1="192.57" x2="171.74" y2="49.71" stroke="#94a3b8" stroke-width="1.1" stroke-dasharray="3 3"/>
<line x1="171.74" y1="189.57" x2="171.74" y2="195.57" stroke="#0f172a" stroke-width="1.2"/>
<text x="171.74" y="206.57" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text>
<line x1="281.92" y1="189.57" x2="281.92" y2="195.57" stroke="#0f172a" stroke-width="1.2"/>
<text x="281.92" y="206.57" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4</text>
<line x1="58.55" y1="49.71" x2="64.55" y2="49.71" stroke="#0f172a" stroke-width="1.2"/>
<text x="55.55" y="53.71" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">20</text>
<circle cx="61.55" cy="192.57" r="3.5" fill="#0f172a"/>
<circle cx="281.92" cy="192.57" r="3.5" fill="#0f172a"/>
<circle cx="171.74" cy="49.71" r="4" fill="#0f172a"/>
<text x="183.74" y="41.71" text-anchor="start" font-size="11" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">tangente horizontale</text>
<text x="171.74" y="186.57" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">c</text>
</svg>
:::

L'instant c de la figure est celui où la courbe a une tangente horizontale : c'est là que la pente h′(c) s'annule.

::: exemple Le sommet du lancer

1. h(0) = 0 et h(4) = 80 − 80 = 0 : les deux extrémités ont la même ordonnée.
2. h est un polynôme, donc continue sur [0 ; 4] et dérivable sur ]0 ; 4[.
3. Le théorème ci-dessous garantit un instant c de ]0 ; 4[ avec h′(c) = 0. Ici h′(t) = 20 − 10t s'annule en t = 2, hauteur maximale h(2) = 20 m.

:::

::: exemple Zéros de la dérivée sans la calculer

1. g(x) = (x + 1)(x − 1)(x − 4) = x³ − 4x² − x + 4 s'annule en −1, 1 et 4.
2. Sur [−1 ; 1] puis sur [1 ; 4], g est continue, dérivable, avec la même valeur 0 aux extrémités : g′ s'annule dans ]−1 ; 1[ et dans ]1 ; 4[.
3. Ces deux zéros sont distincts, car les intervalles ouverts sont disjoints. Comme g′ est de degré 2, elle n'a pas d'autre zéro : exactement deux tangentes horizontales.

:::

::: piege
**Erreur : appliquer Rolle sans vérifier la dérivabilité.** Pour f(x) = |x| sur [−1 ; 1], on remarque f(−1) = f(1) = 1 et l'on conclut « donc f′ s'annule ». L'erreur tente parce que l'égalité des valeurs est la seule hypothèse qui se voit. Mais f′ vaut −1 pour x < 0 et 1 pour x > 0 : elle ne s'annule jamais, car f n'est pas dérivable en 0, et c'est précisément là que la courbe change de sens.
:::

::: propriete
**Théorème de Rolle** : soit a < b. Si f est continue sur [a ; b], dérivable sur ]a ; b[ et si f(a) = f(b), alors il existe un réel c de ]a ; b[ tel que f′(c) = 0. Graphiquement, C_f admet au moins une tangente parallèle à l'axe des abscisses.
La preuve : f continue sur [a ; b] atteint son maximum et son minimum ; si f n'est pas constante, l'un des deux est atteint à l'intérieur, en un point où f′ s'annule (voir la section sur les extrema).
Cas limite : le théorème donne l'existence de c, pas sa valeur ni son unicité ; pour f(x) = x³ − x sur [−1 ; 1], il y a deux valeurs possibles, c = ±1/√3.
:::

::: verifie À toi : un lancer symétrique
Soit f(x) = x³ − 9x sur [−3 ; 3]. Montrer qu'il existe c de ]−3 ; 3[ tel que f′(c) = 0, puis trouver tous les c.

---

f est un polynôme, f(−3) = −27 + 27 = 0 et f(3) = 27 − 27 = 0 : les hypothèses de Rolle sont réunies, donc un tel c existe. Ici f′(x) = 3x² − 9 s'annule pour x² = 3, c'est-à-dire c = −√3 ou c = √3, deux valeurs de ]−3 ; 3[.
:::

::: retenir
Si f est continue sur [a ; b], dérivable sur ]a ; b[ et f(a) = f(b), alors f′ s'annule quelque part dans ]a ; b[ ; sans la dérivabilité, c'est faux (|x|).
:::

## 📐 Théorème des accroissements finis et son inégalité

Un train parcourt d(t) = 40t² kilomètres en t heures, pour 0 ≤ t ≤ 3 : 360 km en 3 h, soit une vitesse moyenne de 120 km/h. À un instant précis, le compteur affiche-t-il exactement 120 km/h ?

::: figure La tangente au point d'abscisse c est parallèle à la corde AB : sa pente est la vitesse moyenne 120 km/h
<svg viewBox="0 0 340 240">
<title>Courbe de d(t) = 40t² entre A(0 ; 0) et B(3 ; 360), la corde [AB] de pente 120 et, au point d'abscisse 1,5, la tangente parallèle à cette corde</title>
<line x1="34" y1="196.61" x2="336" y2="196.61" stroke="#0f172a" stroke-width="1.6"/>
<line x1="67.9" y1="222" x2="67.9" y2="6" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="336,196.61 328,192.61 328,200.61" fill="#0f172a"/>
<polygon points="67.9,6 63.900000000000006,14 71.9,14" fill="#0f172a"/>
<polyline points="67.9,196.61 69.76,196.6 71.62,196.56 73.48,196.5 75.34,196.41 77.2,196.3 79.06,196.16 80.92,196.0 82.78,195.82 84.64,195.61 86.5,195.37 88.36,195.11 90.22,194.83 92.08,194.52 93.94,194.18 95.8,193.83 97.67,193.44 99.53,193.03 101.39,192.6 103.25,192.14 105.11,191.66 106.97,191.15 108.83,190.62 110.69,190.07 112.55,189.49 114.41,188.88 116.27,188.25 118.13,187.59 119.99,186.91 121.85,186.21 123.71,185.48 125.57,184.72 127.43,183.94 129.29,183.14 131.15,182.31 133.01,181.46 134.87,180.58 136.73,179.68 138.59,178.75 140.45,177.8 142.31,176.82 144.17,175.82 146.03,174.79 147.89,173.74 149.75,172.67 151.61,171.57 153.47,170.44 155.33,169.29 157.19,168.11 159.05,166.92 160.91,165.69 162.77,164.44 164.63,163.17 166.49,161.87 168.35,160.55 170.21,159.2 172.07,157.83 173.93,156.43 175.79,155.01 177.65,153.56 179.51,152.09 181.37,150.59 183.23,149.07 185.09,147.52 186.95,145.95 188.81,144.36 190.67,142.74 192.53,141.09 194.39,139.42 196.25,137.73 198.11,136.01 199.97,134.27 201.83,132.5 203.69,130.7 205.55,128.89 207.41,127.04 209.27,125.18 211.13,123.28 213.0,121.37 214.86,119.43 216.72,117.46 218.58,115.47 220.44,113.45 222.3,111.41 224.16,109.35 226.02,107.26 227.88,105.14 229.74,103.0 231.6,100.84 233.46,98.65 235.32,96.43 237.18,94.2 239.04,91.93 240.9,89.65 242.76,87.33 244.62,85.0 246.48,82.63 248.34,80.25 250.2,77.83 252.06,75.4 253.92,72.94 255.78,70.45 257.64,67.94 259.5,65.41 261.36,62.85 263.22,60.26 265.08,57.65 266.94,55.02 268.8,52.36 270.66,49.67 272.52,46.97 274.38,44.23 276.24,41.48 278.1,38.69 279.96,35.89 281.82,33.05 283.68,30.2 285.54,27.31 287.4,24.41 289.26,21.48 291.12,18.52" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"/>
<line x1="67.9" y1="196.61" x2="277.17" y2="40.09" stroke="#94a3b8" stroke-width="1.8"/>
<line x1="130.68" y1="188.78" x2="214.39" y2="126.17" stroke="#b45309" stroke-width="2.2"/>
<line x1="172.54" y1="196.61" x2="172.54" y2="157.48" stroke="#94a3b8" stroke-width="1.1" stroke-dasharray="3 3"/>
<line x1="172.54" y1="193.61" x2="172.54" y2="199.61" stroke="#0f172a" stroke-width="1.2"/>
<text x="172.54" y="210.61" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1,5</text>
<line x1="277.17" y1="193.61" x2="277.17" y2="199.61" stroke="#0f172a" stroke-width="1.2"/>
<text x="277.17" y="210.61" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">3</text>
<line x1="64.9" y1="40.09" x2="70.9" y2="40.09" stroke="#0f172a" stroke-width="1.2"/>
<text x="61.900000000000006" y="44.09" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">360</text>
<circle cx="67.9" cy="196.61" r="3.5" fill="#0f172a"/>
<circle cx="277.17" cy="40.09" r="3.5" fill="#0f172a"/>
<circle cx="172.54" cy="157.48" r="4" fill="#0f172a"/>
<text x="53.900000000000006" y="190.61" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">A</text>
<text x="273.17" y="32.09" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">B</text>
<text x="172.54" y="190.61" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">c</text>
<text x="222.39" y="138.17000000000002" text-anchor="start" font-size="11" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">tangente</text>
</svg>
:::

La corde AB a pour pente 120 km/h, la vitesse moyenne ; la tangente orange est parallèle à cette corde, donc sa pente d′(c) est la vitesse indiquée par le compteur à l'instant c.

::: exemple Le compteur du train

1. d(3) − d(0) = 360 − 0 = 360, sur un intervalle de longueur 3 : la pente de la corde est 360/3 = 120.
2. d est un polynôme, donc continue sur [0 ; 3] et dérivable sur ]0 ; 3[ : on cherche c avec d′(c) = 120.
3. d′(t) = 80t, donc 80c = 120 et c = 1,5 h, bien dans ]0 ; 3[ : à 1 h 30 le compteur affiche 120 km/h.

:::

::: exemple Un accroissement de x³

1. Soit g(x) = x³ sur [1 ; 4] : g(4) − g(1) = 64 − 1 = 63.
2. Le théorème s'écrit 63 = g′(c)(4 − 1) = 3c² × 3, donc c² = 7.
3. c = √7 ≈ 2,65 convient, car 1 < √7 < 4 ; −√7 est rejeté, car il n'est pas dans ]1 ; 4[.

:::

::: exemple Encadrer une racine

1. Soit f(x) = √(1 + x) sur [0 ; 1/2] : f′(x) = 1/(2√(1 + x)). Comme 1 ≤ 1 + x ≤ 3/2, on a 1 ≤ √(1 + x) ≤ √(3/2), d'où 1/(2√(3/2)) ≤ f′(x) ≤ 1/2, soit 1/√6 ≤ f′(x) ≤ 1/2.
2. On applique l'inégalité ci-dessous sur [0 ; t], avec t ∈ ]0 ; 1/2], et l'on utilise f(0) = 1 : t/√6 ≤ √(1 + t) − 1 ≤ t/2.
3. Pour t = 0,02 : 1 + 0,02/√6 ≤ √1,02 ≤ 1 + 0,01, c'est-à-dire 1,0081 ≤ √1,02 ≤ 1,01 (la calculatrice donne 1,00995).

:::

::: piege
**Erreur : oublier le facteur b − a.** Sachant 1 ≤ f′(x) ≤ 4 sur ]0 ; 3[, on écrit 1 ≤ f(3) − f(0) ≤ 4. L'erreur tente parce que l'on recopie l'encadrement de f′ comme s'il bornait l'accroissement. Mais f(x) = 3x vérifie les hypothèses et donne f(3) − f(0) = 9, hors de [1 ; 4]. Le bon encadrement multiplie par b − a = 3 : 3 ≤ f(3) − f(0) ≤ 12.
:::

::: propriete
**Théorème des accroissements finis** : soit a < b. Si f est continue sur [a ; b] et dérivable sur ]a ; b[, il existe c de ]a ; b[ tel que f(b) − f(a) = f′(c)(b − a). Graphiquement, une tangente est parallèle à la corde AB. Rolle en est le cas f(a) = f(b) ; la preuve applique Rolle à g(x) = f(x) − ((f(b) − f(a))/(b − a))(x − a).
**Inégalité des accroissements finis** : si f est continue sur [a ; b], dérivable sur ]a ; b[ et si m ≤ f′(x) ≤ M sur ]a ; b[, alors m(b − a) ≤ f(b) − f(a) ≤ M(b − a). En particulier, si |f′(x)| ≤ M sur un intervalle I, alors |f(b) − f(a)| ≤ M|b − a| pour tous a et b de I.
Cas limite : c existe mais n'est pas forcément unique ni calculable ; l'inégalité sert précisément quand on ne le calcule pas.
:::

::: verifie À toi : un c de parabole
Soit f(x) = x² + x sur [1 ; 5]. Trouver le réel c du théorème des accroissements finis.

---

f(5) − f(1) = 30 − 2 = 28, sur une longueur 5 − 1 = 4 : la pente de la corde est 7. On résout f′(c) = 2c + 1 = 7, d'où c = 3, bien dans ]1 ; 5[ (c'est le milieu de l'intervalle, comme toujours pour une parabole).
:::

::: retenir
Entre a et b, une tangente est parallèle à la corde : f(b) − f(a) = f′(c)(b − a) ; borner f′ entre m et M borne f(b) − f(a) entre m(b − a) et M(b − a).
:::

## 🧗 Signe de f′ et sens de variation

Sur la courbe de f(x) = x³ − 6x² + 9x, on lit f(0) = 0, f(1) = 4, f(2) = 2, f(3) = 0 puis f(4) = 4 : la fonction monte, descend, remonte. Comment obtenir ce schéma sans tracer la courbe, et en être sûr entre les valeurs calculées ?

::: exemple Le tableau de f(x) = x³ − 6x² + 9x

1. f est un polynôme : f′(x) = 3x² − 12x + 9 = 3(x − 1)(x − 3).
2. 3(x − 1)(x − 3) est positif en dehors des racines 1 et 3, négatif entre elles.
3. Le signe de f′ donne les variations :

| x              | ]−∞ ; 1[   | ]1 ; 3[      | ]3 ; +∞[   |
| -------------- | ---------- | ------------ | ---------- |
| signe de f′    | +          | −            | +          |
| variation de f | croissante | décroissante | croissante |

4. Aux bornes 1 et 3 la fonction est continue : elle est croissante sur ]−∞ ; 1], décroissante sur [1 ; 3], croissante sur [3 ; +∞[, avec f(1) = 4 et f(3) = 0.

:::

::: exemple Quand f n'est pas dérivable à la borne

1. Soit f(x) = √(4 − x²) sur [0 ; 2]. Sur ]0 ; 2[, avec u = 4 − x² et u′ = −2x, f′(x) = u′/(2√u) = −x/√(4 − x²) < 0.
2. f est donc strictement décroissante sur ]0 ; 2[. Mais f n'est pas dérivable en 2 (son taux tend vers −∞) : on ne peut pas utiliser f′ en 2.
3. f est continue sur [0 ; 2] : elle est strictement décroissante sur [0 ; 2] tout entier, de f(0) = 2 à f(2) = 0, et prend toutes les valeurs de [0 ; 2].

:::

::: exemple Une dérivée qui s'annule en des points isolés

1. f(x) = x − sin x a pour dérivée f′(x) = 1 − cos x ≥ 0.
2. f′(x) = 0 seulement quand cos x = 1, c'est-à-dire en x = 2kπ : des points isolés, jamais sur un intervalle ouvert.
3. f est donc strictement croissante sur ℝ, bien que sa tangente soit horizontale en 0, 2π, 4π…

:::

::: piege
**Erreur : croire que f′ ≥ 0 suffit pour la stricte croissance.** Soit g(x) = 0 si x ≤ 1 et g(x) = (x − 1)² si x > 1 : g est dérivable avec g′ ≥ 0 sur ℝ, et l'on écrit « donc g est strictement croissante ». L'erreur tente parce que f′ > 0 donne la stricte croissance et que l'on relâche l'inégalité sans regarder où f′ s'annule. Mais g′ = 0 sur tout l'intervalle ]−∞ ; 1[ : g y est constante, donc seulement croissante.
:::

::: propriete
Soit f dérivable sur un intervalle I.
**Signe strict** : f′ > 0 sur I donne f strictement croissante ; f′ < 0 sur I donne f strictement décroissante.
**Signe large** : si f′ ≥ 0 (resp. ≤ 0) et ne s'annule sur aucun intervalle ouvert contenu dans I, alors f est strictement croissante (resp. décroissante).
**Prolongement aux bornes** : si f est continue sur [a ; b], dérivable sur ]a ; b[ et (strictement) croissante ou décroissante sur ]a ; b[, elle l'est sur [a ; b].
Cas limite : f′ ≥ 0 avec f′ = 0 sur tout un intervalle donne seulement f croissante, non strictement.
:::

::: verifie À toi : un tableau complet
Dresser le tableau de variation de h(x) = 2x³ + 3x² − 12x sur ℝ.

---

h′(x) = 6x² + 6x − 12 = 6(x + 2)(x − 1), positive pour x < −2, négative entre −2 et 1, positive pour x > 1. Donc h est croissante sur ]−∞ ; −2], décroissante sur [−2 ; 1] puis croissante sur [1 ; +∞[, avec h(−2) = −16 + 12 + 24 = 20 et h(1) = 2 + 3 − 12 = −7.
:::

::: retenir
f′ > 0 donne f croissante, f′ < 0 donne f décroissante ; une dérivée qui s'annule en des points isolés suffit encore pour la stricte monotonie.
:::

## 🎯 Extrema locaux

Sur la courbe de la section précédente, f(x) = x³ − 6x² + 9x, on repère un sommet en x = 1 et un creux en x = 3. Peut-on les trouver sans tracer, et sont-ils les points les plus haut et les plus bas de toute la courbe ?

::: figure Au sommet (1 ; 4) et au creux (3 ; 0), la tangente est horizontale
<svg viewBox="0 0 340 240">
<title>Courbe de x ↦ x³ − 6x² + 9x : un sommet au point (1 ; 4) et un creux au point (3 ; 0), tous deux à tangente horizontale</title>
<line x1="28" y1="149.48" x2="336" y2="149.48" stroke="#0f172a" stroke-width="1.6"/>
<line x1="67.69" y1="222" x2="67.69" y2="6" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="336,149.48 328,145.48 328,153.48" fill="#0f172a"/>
<polygon points="67.69,6 63.69,14 71.69,14" fill="#0f172a"/>
<polyline points="48.6,210.66 51.03,201.49 53.47,192.73 55.9,184.38 58.33,176.44 60.77,168.89 63.2,161.72 65.63,154.94 68.07,148.52 70.5,142.47 72.93,136.77 75.37,131.41 77.8,126.4 80.23,121.71 82.67,117.35 85.1,113.3 87.53,109.56 89.97,106.12 92.4,102.97 94.83,100.11 97.27,97.52 99.7,95.2 102.13,93.13 104.57,91.32 107.0,89.76 109.43,88.43 111.87,87.33 114.3,86.45 116.73,85.78 119.17,85.31 121.6,85.05 124.03,84.97 126.47,85.07 128.9,85.35 131.33,85.79 133.77,86.39 136.2,87.14 138.63,88.03 141.07,89.05 143.5,90.2 145.93,91.47 148.37,92.85 150.8,94.33 153.23,95.91 155.67,97.57 158.1,99.31 160.53,101.12 162.97,103.0 165.4,104.93 167.83,106.91 170.27,108.92 172.7,110.97 175.13,113.04 177.57,115.13 180.0,117.23 182.43,119.32 184.87,121.41 187.3,123.48 189.73,125.53 192.17,127.55 194.6,129.52 197.03,131.45 199.47,133.33 201.9,135.14 204.33,136.88 206.77,138.54 209.2,140.12 211.63,141.6 214.07,142.98 216.5,144.25 218.93,145.4 221.37,146.42 223.8,147.31 226.23,148.06 228.67,148.66 231.1,149.1 233.53,149.38 235.97,149.48 238.4,149.41 240.83,149.14 243.27,148.67 245.7,148.01 248.13,147.13 250.57,146.02 253.0,144.69 255.43,143.13 257.87,141.32 260.3,139.25 262.73,136.93 265.17,134.34 267.6,131.48 270.03,128.33 272.47,124.89 274.9,121.15 277.33,117.1 279.77,112.74 282.2,108.06 284.63,103.04 287.07,97.69 289.5,91.99 291.93,85.93 294.37,79.51 296.8,72.73 299.23,65.56 301.67,58.01 304.1,50.07 306.53,41.72 308.97,32.96 311.4,23.79 313.83,14.19" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"/>
<line x1="90.15" y1="84.97" x2="163.15" y2="84.97" stroke="#b45309" stroke-width="2" stroke-dasharray="6 4"/>
<line x1="202.46" y1="149.48" x2="275.46" y2="149.48" stroke="#b45309" stroke-width="2" stroke-dasharray="6 4"/>
<line x1="123.85" y1="149.48" x2="123.85" y2="84.97" stroke="#94a3b8" stroke-width="1.1" stroke-dasharray="3 3"/>
<line x1="123.85" y1="146.48" x2="123.85" y2="152.48" stroke="#0f172a" stroke-width="1.2"/>
<text x="123.85" y="163.48" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text>
<line x1="236.15" y1="146.48" x2="236.15" y2="152.48" stroke="#0f172a" stroke-width="1.2"/>
<text x="236.15" y="143.48" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">3</text>
<line x1="64.69" y1="84.97" x2="70.69" y2="84.97" stroke="#0f172a" stroke-width="1.2"/>
<text x="61.69" y="88.97" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4</text>
<circle cx="123.85" cy="84.97" r="4" fill="#0f172a"/>
<circle cx="236.15" cy="149.48" r="4" fill="#0f172a"/>
<text x="131.85" y="76.97" text-anchor="start" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">sommet (1 ; 4)</text>
<text x="228.15" y="171.48" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">creux (3 ; 0)</text>
<text x="269.12" y="79.47" text-anchor="start" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">C_f</text>
</svg>
:::

Au sommet comme au creux, la tangente est horizontale : c'est ce que dit f′ = 0 dans la formule ci-dessous.

::: definition
Soit f définie sur un intervalle I et a un réel de I. f admet un **maximum local** en a s'il existe un intervalle ouvert J contenant a, inclus dans I, tel que f(x) ≤ f(a) pour tout x de J. Elle admet un **minimum local** en a si f(x) ≥ f(a) pour tout x de J. Dans les deux cas, on parle d'**extremum local**.
:::

::: exemple Sommet et creux

1. f′(x) = 3(x − 1)(x − 3) s'annule en 1 et en 3.
2. En 1, f′ passe du positif au négatif : f monte puis descend, maximum local f(1) = 4.
3. En 3, f′ passe du négatif au positif : f descend puis monte, minimum local f(3) = 0.
4. Ils sont seulement locaux : f(5) = 20 > 4 et f(−1) = −16 < 0.

:::

::: piege
**Erreur : conclure à un extremum dès que f′(a) = 0.** Pour g(x) = x³, g′(x) = 3x² s'annule en 0 et l'on écrit « donc g admet un extremum en 0 ». L'erreur tente parce que le sommet et le creux de l'exemple avaient eux aussi une tangente horizontale. Mais g′ = 3x² reste positive de part et d'autre de 0 : g est strictement croissante, sans extremum. Il faut un changement de signe de g′.
:::

::: propriete
Soit f dérivable sur un intervalle ouvert I et a un réel de I.
Si f admet un extremum local en a, alors f′(a) = 0 (condition nécessaire).
Si f′ s'annule en a en changeant de signe, alors f admet un extremum local en a (condition suffisante).
Cas limite : l'hypothèse « f dérivable en a » compte. f(x) = |x| admet un minimum en 0, où f′ n'existe pas : on ne peut pas y appliquer f′(a) = 0.
:::

::: verifie À toi : sommet et creux
Déterminer les extrema locaux de g(x) = x³ − 3x² − 9x.

---

g′(x) = 3x² − 6x − 9 = 3(x − 3)(x + 1), positive pour x < −1, négative entre −1 et 3, positive pour x > 3. En −1, g′ passe du positif au négatif : maximum local g(−1) = −1 − 3 + 9 = 5. En 3, g′ passe du négatif au positif : minimum local g(3) = 27 − 27 − 27 = −27.
:::

::: retenir
Un extremum local d'une fonction dérivable annule f′, mais f′(a) = 0 n'en donne un que si f′ change de signe en a.
:::

## 🔭 Dérivées successives et point d'inflexion

Un mobile se déplace sur un axe selon x(t) = t³ − 6t² + 9t mètres, à l'instant t ≥ 0 en secondes : c'est encore la courbe précédente. Sa vitesse est x′(t).
À quel instant cette vitesse cesse-t-elle de décroître pour se mettre à croître, et que devient la courbe à cet instant ?

::: definition
Soit f dérivable sur I. Sa dérivée f′ est la **dérivée première**. Si f′ est dérivable, sa dérivée est la **dérivée seconde**, notée f″ ou f⁽²⁾. Par itération, si f⁽ⁿ⁻¹⁾ (n ≥ 2) est dérivable, sa dérivée est la **dérivée nᵉ** ou dérivée d'ordre n, notée f⁽ⁿ⁾.
:::

::: figure En I(2 ; 2), la courbe passe de l'autre côté de sa tangente : c'est un point d'inflexion
<svg viewBox="0 0 340 240">
<title>Courbe de x ↦ x³ − 6x² + 9x et sa tangente y = −3x + 8 au point I(2 ; 2) : la courbe passe de l'autre côté de sa tangente en I</title>
<line x1="28" y1="149.48" x2="336" y2="149.48" stroke="#0f172a" stroke-width="1.6"/>
<line x1="67.69" y1="222" x2="67.69" y2="6" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="336,149.48 328,145.48 328,153.48" fill="#0f172a"/>
<polygon points="67.69,6 63.69,14 71.69,14" fill="#0f172a"/>
<polyline points="48.6,210.66 51.03,201.49 53.47,192.73 55.9,184.38 58.33,176.44 60.77,168.89 63.2,161.72 65.63,154.94 68.07,148.52 70.5,142.47 72.93,136.77 75.37,131.41 77.8,126.4 80.23,121.71 82.67,117.35 85.1,113.3 87.53,109.56 89.97,106.12 92.4,102.97 94.83,100.11 97.27,97.52 99.7,95.2 102.13,93.13 104.57,91.32 107.0,89.76 109.43,88.43 111.87,87.33 114.3,86.45 116.73,85.78 119.17,85.31 121.6,85.05 124.03,84.97 126.47,85.07 128.9,85.35 131.33,85.79 133.77,86.39 136.2,87.14 138.63,88.03 141.07,89.05 143.5,90.2 145.93,91.47 148.37,92.85 150.8,94.33 153.23,95.91 155.67,97.57 158.1,99.31 160.53,101.12 162.97,103.0 165.4,104.93 167.83,106.91 170.27,108.92 172.7,110.97 175.13,113.04 177.57,115.13 180.0,117.23 182.43,119.32 184.87,121.41 187.3,123.48 189.73,125.53 192.17,127.55 194.6,129.52 197.03,131.45 199.47,133.33 201.9,135.14 204.33,136.88 206.77,138.54 209.2,140.12 211.63,141.6 214.07,142.98 216.5,144.25 218.93,145.4 221.37,146.42 223.8,147.31 226.23,148.06 228.67,148.66 231.1,149.1 233.53,149.38 235.97,149.48 238.4,149.41 240.83,149.14 243.27,148.67 245.7,148.01 248.13,147.13 250.57,146.02 253.0,144.69 255.43,143.13 257.87,141.32 260.3,139.25 262.73,136.93 265.17,134.34 267.6,131.48 270.03,128.33 272.47,124.89 274.9,121.15 277.33,117.1 279.77,112.74 282.2,108.06 284.63,103.04 287.07,97.69 289.5,91.99 291.93,85.93 294.37,79.51 296.8,72.73 299.23,65.56 301.67,58.01 304.1,50.07 306.53,41.72 308.97,32.96 311.4,23.79 313.83,14.19" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"/>
<line x1="112.62" y1="59.16" x2="258.62" y2="184.97" stroke="#b45309" stroke-width="2.2"/>
<line x1="180.0" y1="146.48" x2="180.0" y2="152.48" stroke="#0f172a" stroke-width="1.2"/>
<text x="180.0" y="163.48" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text>
<line x1="64.69" y1="117.23" x2="70.69" y2="117.23" stroke="#0f172a" stroke-width="1.2"/>
<text x="61.69" y="121.23" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text>
<circle cx="180.0" cy="117.23" r="4" fill="#0f172a"/>
<text x="188.0" y="109.23" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">I</text>
<text x="230.54" y="201.1" text-anchor="start" font-size="11" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">tangente en I</text>
<text x="269.12" y="79.47" text-anchor="start" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">C_f</text>
</svg>
:::

En I, la tangente orange (y = −3x + 8) passe d'un côté de la courbe à l'autre : la formule de f″ ci-dessous va nous dire où.

::: exemple De la vitesse à l'inflexion

1. f(x) = x³ − 6x² + 9x : f′(x) = 3x² − 12x + 9, f″(x) = 6x − 12, f⁽³⁾(x) = 6 et f⁽⁴⁾(x) = 0.
2. f″(x) = 6(x − 2) s'annule en 2 en passant du négatif au positif : f′ décroît jusqu'en 2 puis croît, ce qui répond à la question de la vitesse.
3. En x = 2 : f(2) = 8 − 24 + 18 = 2 et f′(2) = 12 − 24 + 9 = −3, donc la tangente est y = −3(x − 2) + 2 = −3x + 8.
4. f(x) − (−3x + 8) = x³ − 6x² + 12x − 8 = (x − 2)³ est négatif avant 2 et positif après : la courbe traverse sa tangente en I(2 ; 2).

:::

::: piege
**Erreur : conclure à une inflexion dès que f″(a) = 0.** Pour h(x) = x⁴, h″(x) = 12x² s'annule en 0 et l'on écrit « donc l'origine est un point d'inflexion ». L'erreur tente parce que f″ s'annulait aussi en 2 dans l'exemple. Mais 12x² reste positive de part et d'autre de 0 : la courbe de x⁴ reste au-dessus de sa tangente y = 0, elle ne la traverse pas. Il faut un changement de signe de f″.
:::

::: propriete
**Définition** : si f est dérivable en a, le point A(a ; f(a)) est un **point d'inflexion** de C_f lorsque C_f traverse sa tangente en A.
**Théorème (admis)** : si f est deux fois dérivable sur ]a − h ; a + h[ (h > 0) et si f″ s'annule en a en changeant de signe, alors le point (a ; f(a)) est un point d'inflexion de C_f.
Cas limite : la tangente d'inflexion peut être horizontale, comme celle de x ↦ x³ en 0, sans qu'il y ait d'extremum.
:::

::: verifie À toi : une inflexion avec sa tangente
Montrer que la courbe de g(x) = x³ + 3x² − 2 admet un point d'inflexion et donner sa tangente.

---

g′(x) = 3x² + 6x et g″(x) = 6x + 6 = 6(x + 1), qui s'annule en −1 en changeant de signe : point d'inflexion d'abscisse −1. On a g(−1) = −1 + 3 − 2 = 0 et g′(−1) = 3 − 6 = −3, donc la tangente est y = −3(x + 1) = −3x − 3. Contrôle : g(x) + 3x + 3 = x³ + 3x² + 3x + 1 = (x + 1)³ change de signe en −1, donc la courbe traverse la tangente.
:::

::: retenir
Si f″ s'annule en a en changeant de signe, la courbe traverse sa tangente en A(a ; f(a)) : c'est un point d'inflexion ; f″(a) = 0 seul ne suffit pas (x⁴).
:::

> 🏆 Troisième porte franchie, héros : tu lis la pente d'une courbe, tu garantis une tangente horizontale par Rolle, tu encadres un accroissement avec le théorème des accroissements finis, et tu dresses variations, extrema et inflexions à partir de f′ et de f″. Ces armes ouvrent les fonctions réciproques et l'étude complète des fonctions.
