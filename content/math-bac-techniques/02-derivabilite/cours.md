# ⚔️ Dérivabilité — lire la pente en chaque point

> 💡 «Une courbe ne ment jamais sur sa pente : il suffit de savoir la lire, point par point.»

Avec les limites et la continuité, tu sais dire où une fonction va. Ici tu apprends à dire à quelle vitesse elle y va, et dans quel sens : c'est la dérivée, l'outil de presque tous les problèmes du Bac (tangente, variations, extrema, encadrements). Huit notions, dans l'ordre où elles s'appellent les unes les autres.

## 🎯 Nombre dérivé, tangente et approximation affine

Un chariot descend une rampe : après x secondes il a parcouru f(x) = x² mètres. On sait calculer sa vitesse moyenne entre deux instants, mais pas encore sa vitesse à l'instant x = 3.
Entre 3 et 3 + h, la vitesse moyenne vaut ((3 + h)² − 9)/h = 6 + h : plus h est petit, plus elle se rapproche de 6. Comment nommer cette valeur limite et à quoi sert-elle ?

::: definition
Soit f définie sur un intervalle ouvert I et a un réel de I. On dit que **f est dérivable en a** si le **taux d'accroissement** (f(x) − f(a))/(x − a) admet une limite finie quand x tend vers a (ou, en posant x = a + h, si (f(a + h) − f(a))/h admet une limite finie quand h tend vers 0). Cette limite est le **nombre dérivé** de f en a, noté f′(a).
:::

::: figure La corde AB (pente 7) tourne vers la tangente en A quand B glisse vers A : la pente limite 6 est le nombre dérivé f′(3)
<svg viewBox="0 0 340 270">
<title>Parabole y = x² : la corde AB de pente 7 tourne vers la tangente en A, de pente 6</title>
<line x1="34" y1="214" x2="326" y2="214" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="326,214 318,218 318,210" fill="#0f172a"/><line x1="56.9" y1="244" x2="56.9" y2="14" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="56.9,14 60.9,22 52.9,22" fill="#0f172a"/><line x1="114.16" y1="211" x2="114.16" y2="217" stroke="#0f172a" stroke-width="1.2"/><line x1="171.41" y1="211" x2="171.41" y2="217" stroke="#0f172a" stroke-width="1.2"/><line x1="228.67" y1="211" x2="228.67" y2="217" stroke="#0f172a" stroke-width="1.2"/><line x1="285.92" y1="211" x2="285.92" y2="217" stroke="#0f172a" stroke-width="1.2"/><line x1="53.9" y1="164" x2="59.9" y2="164" stroke="#0f172a" stroke-width="1.2"/><line x1="53.9" y1="114" x2="59.9" y2="114" stroke="#0f172a" stroke-width="1.2"/><line x1="53.9" y1="64" x2="59.9" y2="64" stroke="#0f172a" stroke-width="1.2"/><g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="114.16" y="229" text-anchor="middle" fill="#0f172a" font-size="10">1</text><text x="171.41" y="229" text-anchor="middle" fill="#0f172a" font-size="10">2</text><text x="228.67" y="229" text-anchor="middle" fill="#0f172a" font-size="10">3</text><text x="285.92" y="229" text-anchor="middle" fill="#0f172a" font-size="10">4</text><text x="50.9" y="167.5" text-anchor="end" fill="#0f172a" font-size="10">5</text><text x="50.9" y="117.5" text-anchor="end" fill="#0f172a" font-size="10">10</text><text x="50.9" y="67.5" text-anchor="end" fill="#0f172a" font-size="10">15</text><text x="322" y="208" text-anchor="end" fill="#0f172a" font-size="12">x</text><text x="64.9" y="22" text-anchor="start" fill="#0f172a" font-size="12">y</text></g><polyline points="34,212.4 35.72,212.63 37.44,212.84 39.15,213.04 40.87,213.22 42.59,213.38 44.31,213.52 46.02,213.64 47.74,213.74 49.46,213.83 51.18,213.9 52.89,213.95 54.61,213.98 56.33,214 58.05,214 59.76,213.98 61.48,213.94 63.2,213.88 64.92,213.8 66.64,213.71 68.35,213.6 70.07,213.47 71.79,213.32 73.51,213.16 75.22,212.98 76.94,212.78 78.66,212.56 80.38,212.32 82.09,212.06 83.81,211.79 85.53,211.5 87.25,211.19 88.96,210.86 90.68,210.52 92.4,210.16 94.12,209.78 95.84,209.38 97.55,208.96 99.27,208.52 100.99,208.07 102.71,207.6 104.42,207.11 106.14,206.6 107.86,206.08 109.58,205.54 111.29,204.98 113.01,204.4 114.73,203.8 116.45,203.18 118.16,202.55 119.88,201.9 121.6,201.23 123.32,200.54 125.04,199.84 126.75,199.12 128.47,198.38 130.19,197.62 131.91,196.84 133.62,196.04 135.34,195.23 137.06,194.4 138.78,193.55 140.49,192.68 142.21,191.8 143.93,190.9 145.65,189.98 147.36,189.04 149.08,188.08 150.8,187.1 152.52,186.11 154.24,185.1 155.95,184.07 157.67,183.02 159.39,181.96 161.11,180.88 162.82,179.77 164.54,178.66 166.26,177.52 167.98,176.36 169.69,175.19 171.41,174 173.13,172.79 174.85,171.56 176.56,170.32 178.28,169.06 180,167.77 181.72,166.48 183.44,165.16 185.15,163.82 186.87,162.47 188.59,161.1 190.31,159.71 192.02,158.3 193.74,156.88 195.46,155.44 197.18,153.97 198.89,152.5 200.61,151 202.33,149.48 204.05,147.95 205.76,146.4 207.48,144.83 209.2,143.24 210.92,141.64 212.64,140.02 214.35,138.37 216.07,136.72 217.79,135.04 219.51,133.34 221.22,131.63 222.94,129.9 224.66,128.15 226.38,126.38 228.09,124.6 229.81,122.8 231.53,120.97 233.25,119.14 234.96,117.28 236.68,115.4 238.4,113.51 240.12,111.6 241.84,109.67 243.55,107.72 245.27,105.76 246.99,103.78 248.71,101.77 250.42,99.76 252.14,97.72 253.86,95.66 255.58,93.59 257.29,91.5 259.01,89.39 260.73,87.26 262.45,85.12 264.16,82.96 265.88,80.77 267.6,78.58 269.32,76.36 271.04,74.12 272.75,71.87 274.47,69.6 276.19,67.31 277.91,65 279.62,62.68 281.34,60.34 283.06,57.97 284.78,55.6 286.49,53.2 288.21,50.78 289.93,48.35 291.65,45.9 293.36,43.43 295.08,40.94 296.8,38.44 298.52,35.92 300.24,33.38 301.95,30.82 303.67,28.24 305.39,25.64 307.11,23.03 308.82,20.4" fill="none" stroke="#0f6e56" stroke-width="2.8"/><line x1="194.31" y1="166" x2="303.1" y2="33" stroke="#64748b" stroke-width="2" stroke-dasharray="6 4"/><line x1="131.33" y1="226" x2="308.82" y2="40" stroke="#d97706" stroke-width="2.4"/><circle cx="228.67" cy="124" r="4" fill="#0f172a" stroke="#ffffff" stroke-width="1.2"/><circle cx="285.92" cy="54" r="3.5" fill="#64748b" stroke="#ffffff" stroke-width="1.2"/><g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="218.67" y="119" text-anchor="end" fill="#0f172a" font-size="13">A</text><text x="277.92" y="46" text-anchor="end" fill="#64748b" font-size="13">B</text><text x="118.16" y="178" text-anchor="start" fill="#0f6e56" font-size="13">C_f</text><text x="324" y="148" text-anchor="end" fill="#d97706" font-size="11">tangente en A : pente 6</text><text x="324" y="174" text-anchor="end" fill="#64748b" font-size="11">corde AB : pente 7</text></g>
</svg>
:::

Sur la figure, la pente de la corde AB est le taux d'accroissement (16 − 9)/(4 − 3) = 7, soit 6 + h pour h = 1 ; la pente de la tangente est la limite 6 : c'est f′(3).

::: exemple Vitesse du chariot en x = 3

1. Taux d'accroissement de f(x) = x² en 3 : (x² − 9)/(x − 3) — c'est la définition appliquée en a = 3.
2. On factorise x² − 9 = (x − 3)(x + 3) et on simplifie par x − 3, non nul car x ≠ 3 : le taux vaut x + 3.
3. lim x→3 (x + 3) = 6, donc f est dérivable en 3 et f′(3) = 6 : le chariot roule à 6 m/s.
4. Tangente en A(3 ; 9) : y = f′(3)(x − 3) + f(3) = 6(x − 3) + 9 = 6x − 9.
5. Approximation affine : (3,02)² = f(3 + 0,02) ≈ f(3) + 0,02 × f′(3) = 9 + 0,12 = 9,12 (la valeur exacte est 9,1204).

:::

::: piege
**Erreur : écrire la tangente y = f′(a)x + f(a)**, ici y = 6x + 9. Elle tente parce que « pente × x + ordonnée » ressemble à y = mx + p. Mais f(a) est l'ordonnée du point A, pas l'ordonnée à l'origine : il faut décaler x de a. Le test le montre : en x = 3, la formule fautive donne 6 × 3 + 9 = 27, et la droite ne passe même pas par A(3 ; 9). La bonne écriture est y = 6(x − 3) + 9 = 6x − 9.
:::

::: propriete
Si f est dérivable en a, sa courbe admet au point A(a ; f(a)) une **tangente** de pente f′(a), dirigée par le vecteur (1 ; f′(a)), d'équation :
$$ y = f′(a)(x − a) + f(a) $$
Pour h voisin de 0, on a l'**approximation affine** f(a + h) ≈ f(a) + h f′(a). Cas particulier : si f′(a) = 0, la tangente est horizontale, d'équation y = f(a).
:::

::: exemple Le même outil, sans situation : √x en 4

1. Taux d'accroissement de g(x) = √x en 4 : (√x − 2)/(x − 4).
2. On écrit x − 4 = (√x − 2)(√x + 2) et on simplifie : le taux vaut 1/(√x + 2).
3. lim x→4 1/(√x + 2) = 1/4, donc g′(4) = 1/4.
4. Tangente : y = (1/4)(x − 4) + 2 = x/4 + 1, et √4,1 ≈ 2 + 0,1 × (1/4) = 2,025 (la valeur exacte est 2,0248…).

:::

::: verifie À toi : le taux d'accroissement de 1/x
Soit p(x) = 1/x. Calcule p′(2) à partir de la définition, puis écris l'équation de la tangente en x = 2.

---

Le taux est (1/x − 1/2)/(x − 2). On réduit au même dénominateur : 1/x − 1/2 = (2 − x)/(2x), puis on simplifie par x − 2 en écrivant 2 − x = −(x − 2) : le taux vaut −1/(2x). Sa limite en 2 est −1/4, donc p′(2) = −1/4. La tangente est y = −(1/4)(x − 2) + 1/2 = −x/4 + 1.
:::

::: retenir
f′(a) = lim x→a (f(x) − f(a))/(x − a) est la pente de la tangente en A(a ; f(a)), d'équation y = f′(a)(x − a) + f(a).
:::

## 🔀 Dérivabilité à gauche et à droite

La courbe de f(x) = |x² − 4| rejoint l'axe des abscisses en x = 2 en formant une pointe. Calculons le taux d'accroissement en 2 de chaque côté :
pour x = 2,1 il vaut 0,41/0,1 = 4,1, et pour x = 1,9 il vaut 0,39/(−0,1) = −3,9. Les deux côtés ne tendent pas vers le même nombre. Existe-t-il alors une tangente en ce point ?

::: definition
Soit f définie sur un intervalle I et a un réel de I. **f est dérivable à droite en a** si (f(x) − f(a))/(x − a) admet une limite finie quand x tend vers a par valeurs supérieures ; cette limite est le **nombre dérivé à droite** f′d(a). **f est dérivable à gauche en a** si cette limite existe quand x tend vers a par valeurs inférieures ; c'est le **nombre dérivé à gauche** f′g(a).
:::

::: figure En A(2 ; 0), la courbe de |x² − 4| a deux demi-tangentes de pentes différentes : f′g(2) = −4 et f′d(2) = 4
<svg viewBox="0 0 340 250">
<title>Courbe de |x² − 4| : en A(2 ; 0), deux demi-tangentes de pentes −4 et 4</title>
<line x1="20" y1="203.51" x2="326" y2="203.51" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="326,203.51 318,207.51 318,199.51" fill="#0f172a"/><line x1="168.63" y1="224" x2="168.63" y2="14" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="168.63,14 172.63,22 164.63,22" fill="#0f172a"/><line x1="37.49" y1="200.51" x2="37.49" y2="206.51" stroke="#0f172a" stroke-width="1.2"/><line x1="81.2" y1="200.51" x2="81.2" y2="206.51" stroke="#0f172a" stroke-width="1.2"/><line x1="124.91" y1="200.51" x2="124.91" y2="206.51" stroke="#0f172a" stroke-width="1.2"/><line x1="212.34" y1="200.51" x2="212.34" y2="206.51" stroke="#0f172a" stroke-width="1.2"/><line x1="256.06" y1="200.51" x2="256.06" y2="206.51" stroke="#0f172a" stroke-width="1.2"/><line x1="299.77" y1="200.51" x2="299.77" y2="206.51" stroke="#0f172a" stroke-width="1.2"/><line x1="165.63" y1="152.29" x2="171.63" y2="152.29" stroke="#0f172a" stroke-width="1.2"/><line x1="165.63" y1="101.07" x2="171.63" y2="101.07" stroke="#0f172a" stroke-width="1.2"/><line x1="165.63" y1="49.85" x2="171.63" y2="49.85" stroke="#0f172a" stroke-width="1.2"/><g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="37.49" y="218.51" text-anchor="middle" fill="#0f172a" font-size="10">−3</text><text x="81.2" y="218.51" text-anchor="middle" fill="#0f172a" font-size="10">−2</text><text x="124.91" y="218.51" text-anchor="middle" fill="#0f172a" font-size="10">−1</text><text x="212.34" y="218.51" text-anchor="middle" fill="#0f172a" font-size="10">1</text><text x="256.06" y="218.51" text-anchor="middle" fill="#0f172a" font-size="10">2</text><text x="299.77" y="218.51" text-anchor="middle" fill="#0f172a" font-size="10">3</text><text x="162.63" y="155.79" text-anchor="end" fill="#0f172a" font-size="10">2</text><text x="162.63" y="104.57" text-anchor="end" fill="#0f172a" font-size="10">4</text><text x="162.63" y="53.35" text-anchor="end" fill="#0f172a" font-size="10">6</text><text x="322" y="197.51" text-anchor="end" fill="#0f172a" font-size="12">x</text><text x="176.63" y="22" text-anchor="start" fill="#0f172a" font-size="12">y</text></g><polyline points="24.37,27.06 26.17,33.99 27.98,40.83 29.78,47.59 31.58,54.25 33.39,60.83 35.19,67.33 36.99,73.73 38.8,80.05 40.6,86.28 42.4,92.43 44.21,98.48 46.01,104.45 47.81,110.34 49.62,116.13 51.42,121.84 53.22,127.46 55.03,133 56.83,138.44 58.63,143.8 60.44,149.08 62.24,154.26 64.04,159.36 65.85,164.37 67.65,169.3 69.45,174.13 71.26,178.88 73.06,183.54 74.86,188.12 76.66,192.61 78.47,197.01 80.27,201.32 82.07,201.47 83.88,197.33 85.68,193.28 87.48,189.32 89.29,185.44 91.09,181.65 92.89,177.94 94.7,174.33 96.5,170.8 98.3,167.35 100.11,164 101.91,160.73 103.71,157.55 105.52,154.45 107.32,151.45 109.12,148.53 110.93,145.7 112.73,142.95 114.53,140.29 116.34,137.72 118.14,135.24 119.94,132.84 121.75,130.53 123.55,128.31 125.35,126.17 127.15,124.13 128.96,122.16 130.76,120.29 132.56,118.5 134.37,116.8 136.17,115.19 137.97,113.67 139.78,112.23 141.58,110.88 143.38,109.61 145.19,108.44 146.99,107.35 148.79,106.35 150.6,105.43 152.4,104.6 154.2,103.86 156.01,103.21 157.81,102.64 159.61,102.16 161.42,101.77 163.22,101.47 165.02,101.25 166.83,101.12 168.63,101.07 170.43,101.12 172.24,101.25 174.04,101.47 175.84,101.77 177.64,102.16 179.45,102.64 181.25,103.21 183.05,103.86 184.86,104.6 186.66,105.43 188.46,106.35 190.27,107.35 192.07,108.44 193.87,109.61 195.68,110.88 197.48,112.23 199.28,113.67 201.09,115.19 202.89,116.8 204.69,118.5 206.5,120.29 208.3,122.16 210.1,124.13 211.91,126.17 213.71,128.31 215.51,130.53 217.32,132.84 219.12,135.24 220.92,137.72 222.72,140.29 224.53,142.95 226.33,145.7 228.13,148.53 229.94,151.45 231.74,154.45 233.54,157.55 235.35,160.73 237.15,164 238.95,167.35 240.76,170.8 242.56,174.33 244.36,177.94 246.17,181.65 247.97,185.44 249.77,189.32 251.58,193.28 253.38,197.33 255.18,201.47 256.99,201.32 258.79,197.01 260.59,192.61 262.4,188.12 264.2,183.54 266,178.88 267.81,174.13 269.61,169.3 271.41,164.37 273.22,159.36 275.02,154.26 276.82,149.08 278.62,143.8 280.43,138.44 282.23,133 284.03,127.46 285.84,121.84 287.64,116.13 289.44,110.34 291.25,104.45 293.05,98.48 294.85,92.43 296.66,86.28 298.46,80.05 300.26,73.73 302.07,67.33 303.87,60.83 305.67,54.25 307.48,47.59 309.28,40.83 311.08,33.99 312.89,27.06" fill="none" stroke="#0f6e56" stroke-width="2.8"/><line x1="227.64" y1="136.93" x2="256.06" y2="203.51" stroke="#2563eb" stroke-width="2.8"/><line x1="256.06" y1="203.51" x2="284.47" y2="136.93" stroke="#d97706" stroke-width="2.8"/><circle cx="256.06" cy="203.51" r="4" fill="#0f172a" stroke="#ffffff" stroke-width="1.2"/><g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="256.06" y="231.51" text-anchor="middle" fill="#0f172a" font-size="11">A(2 ; 0)</text><text x="223.27" y="180.46" text-anchor="end" fill="#2563eb" font-size="11">pente −4</text><text x="290.47" y="134.93" text-anchor="start" fill="#d97706" font-size="11">pente 4</text><text x="41.86" y="121.56" text-anchor="middle" fill="#0f6e56" font-size="13">C_f</text></g>
</svg>
:::

La demi-tangente bleue, à gauche de A, a pour pente f′g(2) ; l'orange, à droite, a pour pente f′d(2) : leur différence est ce qui fait la pointe.

::: exemple Le toit |x² − 4| en x = 2

1. Pour x > 2 proche de 2, x² − 4 > 0 : f(x) = x² − 4 et le taux est (x² − 4)/(x − 2) = x + 2, après factorisation par (x − 2).
2. lim x→2⁺ (x + 2) = 4, donc f′d(2) = 4.
3. Pour x < 2 proche de 2, x² − 4 < 0 : la valeur absolue change le signe, f(x) = 4 − x² et le taux est (4 − x²)/(x − 2) = −(x + 2).
4. lim x→2⁻ −(x + 2) = −4, donc f′g(2) = −4.
5. Comme −4 ≠ 4, f n'est pas dérivable en 2. La courbe a deux demi-tangentes en A(2 ; 0) : y = −4(x − 2) pour x ≤ 2 et y = 4(x − 2) pour x ≥ 2.

:::

::: piege
**Erreur : croire qu'une fonction continue en a est dérivable en a.** f(x) = |x² − 4| est continue en 2 (f(2) = 0 est bien la limite de f(x)) et pourtant non dérivable. L'erreur tente parce qu'une courbe sans saut paraît « lisse ». Mais la continuité interdit les sauts, pas les pointes. Ce qui est vrai : dérivable en a ⟹ continue en a, jamais la réciproque.
:::

::: propriete
f est dérivable en a (a intérieur à l'ensemble de définition) **si et seulement si** f est dérivable à gauche et à droite en a et f′g(a) = f′d(a). Quand f′g(a) ≠ f′d(a), la courbe a deux demi-tangentes de directions différentes : A est un **point anguleux**.
Cas limite : si le taux d'accroissement tend vers +∞ ou −∞ d'un côté, f n'est pas dérivable en a et la courbe a une **demi-tangente verticale** en A.
:::

Exemple du cas limite : g(x) = √(x − 1) en a = 1. Le taux (√(x − 1) − 0)/(x − 1) = 1/√(x − 1) tend vers +∞ quand x tend vers 1 par valeurs supérieures.

::: figure La courbe de √(x − 1) part verticalement du point (1 ; 0) : demi-tangente verticale, donc pas de dérivabilité à droite en 1
<svg viewBox="0 0 320 220">
<title>Courbe de √(x − 1) : demi-tangente verticale au point (1 ; 0)</title>
<line x1="30" y1="159.16" x2="306" y2="159.16" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="306,159.16 298,163.16 298,155.16" fill="#0f172a"/><line x1="53.39" y1="194" x2="53.39" y2="14" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="53.39,14 57.39,22 49.39,22" fill="#0f172a"/><line x1="100.17" y1="156.16" x2="100.17" y2="162.16" stroke="#0f172a" stroke-width="1.2"/><line x1="146.95" y1="156.16" x2="146.95" y2="162.16" stroke="#0f172a" stroke-width="1.2"/><line x1="193.73" y1="156.16" x2="193.73" y2="162.16" stroke="#0f172a" stroke-width="1.2"/><line x1="240.51" y1="156.16" x2="240.51" y2="162.16" stroke="#0f172a" stroke-width="1.2"/><line x1="287.29" y1="156.16" x2="287.29" y2="162.16" stroke="#0f172a" stroke-width="1.2"/><line x1="50.39" y1="101.1" x2="56.39" y2="101.1" stroke="#0f172a" stroke-width="1.2"/><line x1="50.39" y1="43.03" x2="56.39" y2="43.03" stroke="#0f172a" stroke-width="1.2"/><g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="100.17" y="174.16" text-anchor="middle" fill="#0f172a" font-size="10">1</text><text x="146.95" y="174.16" text-anchor="middle" fill="#0f172a" font-size="10">2</text><text x="193.73" y="174.16" text-anchor="middle" fill="#0f172a" font-size="10">3</text><text x="240.51" y="174.16" text-anchor="middle" fill="#0f172a" font-size="10">4</text><text x="287.29" y="174.16" text-anchor="middle" fill="#0f172a" font-size="10">5</text><text x="47.39" y="104.6" text-anchor="end" fill="#0f172a" font-size="10">1</text><text x="47.39" y="46.53" text-anchor="end" fill="#0f172a" font-size="10">2</text><text x="302" y="153.16" text-anchor="end" fill="#0f172a" font-size="12">x</text><text x="61.39" y="22" text-anchor="start" fill="#0f172a" font-size="12">y</text></g><polyline points="100.17,159.16 101.4,149.75 102.63,145.86 103.85,142.87 105.08,140.35 106.31,138.13 107.54,136.12 108.77,134.27 109.99,132.55 111.22,130.94 112.45,129.41 113.68,127.96 114.91,126.57 116.13,125.24 117.36,123.96 118.59,122.73 119.82,121.53 121.04,120.37 122.27,119.25 123.5,118.15 124.73,117.09 125.96,116.05 127.18,115.04 128.41,114.04 129.64,113.07 130.87,112.12 132.1,111.19 133.32,110.28 134.55,109.38 135.78,108.5 137.01,107.63 138.24,106.78 139.46,105.94 140.69,105.12 141.92,104.31 143.15,103.51 144.38,102.72 145.6,101.94 146.83,101.17 148.06,100.41 149.29,99.66 150.52,98.92 151.74,98.19 152.97,97.47 154.2,96.76 155.43,96.05 156.66,95.36 157.88,94.67 159.11,93.98 160.34,93.31 161.57,92.64 162.8,91.98 164.02,91.32 165.25,90.67 166.48,90.03 167.71,89.39 168.94,88.76 170.16,88.14 171.39,87.52 172.62,86.9 173.85,86.29 175.08,85.69 176.3,85.09 177.53,84.49 178.76,83.9 179.99,83.32 181.22,82.73 182.44,82.16 183.67,81.58 184.9,81.02 186.13,80.45 187.36,79.89 188.58,79.34 189.81,78.78 191.04,78.23 192.27,77.69 193.49,77.15 194.72,76.61 195.95,76.08 197.18,75.55 198.41,75.02 199.63,74.49 200.86,73.97 202.09,73.45 203.32,72.94 204.55,72.43 205.77,71.92 207,71.41 208.23,70.91 209.46,70.41 210.69,69.91 211.91,69.42 213.14,68.93 214.37,68.44 215.6,67.95 216.83,67.47 218.05,66.99 219.28,66.51 220.51,66.03 221.74,65.56 222.97,65.09 224.19,64.62 225.42,64.15 226.65,63.69 227.88,63.22 229.11,62.76 230.33,62.3 231.56,61.85 232.79,61.4 234.02,60.94 235.25,60.49 236.47,60.05 237.7,59.6 238.93,59.16 240.16,58.72 241.39,58.28 242.61,57.84 243.84,57.4 245.07,56.97 246.3,56.54 247.53,56.11 248.75,55.68 249.98,55.25 251.21,54.83 252.44,54.4 253.67,53.98 254.89,53.56 256.12,53.14 257.35,52.73 258.58,52.31 259.81,51.9 261.03,51.49 262.26,51.08 263.49,50.67 264.72,50.26 265.94,49.86 267.17,49.45 268.4,49.05 269.63,48.65 270.86,48.25 272.08,47.85 273.31,47.45 274.54,47.06 275.77,46.66 277,46.27 278.22,45.88 279.45,45.49 280.68,45.1 281.91,44.71 283.14,44.33 284.36,43.94 285.59,43.56 286.82,43.18 288.05,42.8 289.28,42.42 290.5,42.04 291.73,41.66 292.96,41.29 294.19,40.91 295.42,40.54 296.64,40.16" fill="none" stroke="#0f6e56" stroke-width="2.8"/><line x1="100.17" y1="159.16" x2="100.17" y2="31.42" stroke="#d97706" stroke-width="2.6" stroke-dasharray="7 4"/><circle cx="100.17" cy="159.16" r="4" fill="#0f172a" stroke="#ffffff" stroke-width="1.2"/><g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="108.17" y="37.23" text-anchor="start" fill="#d97706" font-size="11">demi-tangente verticale</text><text x="268.58" y="64.06" text-anchor="middle" fill="#0f6e56" font-size="13">C_f</text><text x="94.17" y="175.16" text-anchor="end" fill="#0f172a" font-size="11">(1 ; 0)</text></g>
</svg>
:::

::: verifie À toi : x|x − 1| en 1
Soit f(x) = x|x − 1|. Étudie la dérivabilité de f en 1 et donne les demi-tangentes éventuelles.

---

Pour x > 1, f(x) = x(x − 1) et le taux (f(x) − f(1))/(x − 1) = x tend vers 1 : f′d(1) = 1. Pour x < 1, |x − 1| = 1 − x donc f(x) = x(1 − x) et le taux vaut −x, qui tend vers −1 : f′g(1) = −1. Comme 1 ≠ −1, f n'est pas dérivable en 1 : point anguleux, avec les demi-tangentes y = x − 1 (à droite) et y = −(x − 1) (à gauche), puisque f(1) = 0.
:::

::: retenir
Dérivable en a ⟺ f′g(a) et f′d(a) existent et sont égaux ; dérivable en a ⟹ continue en a, mais continue ⇏ dérivable (point anguleux, demi-tangente verticale).
:::

## 🧮 Fonction dérivée : dérivées usuelles et opérations

Pour f(x) = x², le calcul fait en 3 se refait au même prix en n'importe quel réel a : (x² − a²)/(x − a) = x + a, de limite 2a. Inutile de repartir de la limite à chaque point.
Peut-on obtenir d'un coup le nombre dérivé en tout point, c'est-à-dire une nouvelle fonction ?

::: definition
f est **dérivable sur un intervalle ouvert I** si elle est dérivable en tout réel de I ; la fonction x ↦ f′(x) est alors la **fonction dérivée** de f. Sur [a ; +∞[, f est dérivable si elle l'est sur ]a ; +∞[ et à droite en a ; de même sur ]−∞ ; a] avec la gauche en a ; sur [a ; b], f est dérivable si elle l'est sur ]a ; b[, à droite en a et à gauche en b.
:::

| a | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- |
| f′(a) pour f(x) = x² | 2 | 4 | 6 | 8 |

La ligne du bas vaut toujours 2a : c'est la valeur en a de la fonction dérivée x ↦ 2x. On retrouve f′(3) = 6, le résultat du chariot.

::: exemple Trois dérivées, trois outils

1. f(x) = x² : la règle (xⁿ)′ = nxⁿ⁻¹ avec n = 2 donne f′(x) = 2x, et f′(3) = 6 — la vitesse du chariot en x = 3.
2. Produit : g(x) = (x² − 1)(3x + 2) est un polynôme, dérivable sur ℝ. Avec u = x² − 1 et v = 3x + 2, (uv)′ = u′v + v′u = 2x(3x + 2) + 3(x² − 1) = 9x² + 4x − 3.
3. Quotient : k(x) = (2x + 1)/(x − 3) est définie et dérivable sur ℝ privé de 3. La formule (ax + b)/(cx + d) donne ad − cb = 2 × (−3) − 1 × 1 = −7, donc k′(x) = −7/(x − 3)².

:::

::: piege
**Erreur : dériver un produit facteur par facteur, (fg)′ = f′g′.** Avec f(x) = x² et g(x) = x³, le produit est x⁵, de dérivée 5x⁴. La formule fautive donne 2x × 3x² = 6x³ : fausse, et on la voit en comparant avec le calcul direct. L'erreur tente par analogie avec (f + g)′ = f′ + g′. La bonne règle est (fg)′ = f′g + g′f : ici 2x · x³ + 3x² · x² = 5x⁴.
:::

::: propriete
Les dérivées usuelles du premier tableau sont valables sur l'ensemble indiqué (k, a, b, c, d réels ; n entier). Les opérations du second tableau s'appliquent à des fonctions dérivables sur un même intervalle I ; pour 1/f et f/g, le dénominateur ne doit pas s'annuler sur I.
:::

| f(x) | f′(x) | f est dérivable sur |
| --- | --- | --- |
| k (constante) | 0 | ℝ |
| ax + b | a | ℝ |
| xⁿ (n ≥ 2) | nxⁿ⁻¹ | ℝ |
| 1/x | −1/x² | ℝ* |
| 1/xⁿ (n ≥ 2) | −n/xⁿ⁺¹ | ℝ* |
| √x | 1/(2√x) | ]0 ; +∞[ |
| √(ax + b) | a/(2√(ax + b)) | l'ensemble où ax + b > 0 |
| (ax + b)/(cx + d) | (ad − cb)/(cx + d)² | ℝ privé de −d/c |
| sin(ax + b) | a cos(ax + b) | ℝ |
| cos(ax + b) | −a sin(ax + b) | ℝ |
| tan x | 1 + tan²x = 1/cos²x | ℝ privé des π/2 + kπ |
| cotan x | −(1 + cotan²x) = −1/sin²x | ℝ privé des kπ |

Opérations (f et g dérivables sur I) :

| Fonction | Dérivée |
| --- | --- |
| f + g | f′ + g′ |
| af (a constante) | af′ |
| f × g | f′g + g′f |
| fⁿ (n ≥ 2) | nf′fⁿ⁻¹ |
| 1/f (f ne s'annulant pas) | −f′/f² |
| f/g (g ne s'annulant pas) | (f′g − g′f)/g² |

La ligne √x est le cas limite de la notion précédente : le taux 1/√x tend vers +∞ en 0, donc √x n'est dérivable que sur ]0 ; +∞[ et sa courbe a une demi-tangente verticale en 0.

::: verifie À toi : un quotient de polynômes
Détermine l'ensemble de dérivabilité de m(x) = (x + 1)/(x² + 1) et calcule m′(x).

---

Le dénominateur x² + 1 ne s'annule jamais : m est dérivable sur ℝ, comme quotient de polynômes. Avec u = x + 1 et v = x² + 1, (u′v − v′u)/v² = (1 × (x² + 1) − 2x(x + 1))/(x² + 1)² = (x² + 1 − 2x² − 2x)/(x² + 1)² = (−x² − 2x + 1)/(x² + 1)².
:::

::: retenir
Une fonction dérivable sur I a une fonction dérivée f′ ; on la calcule par les dérivées usuelles et les opérations, en vérifiant où chaque formule est valable (√ en 0, dénominateur nul).
:::

## 🧩 Dérivée d'une fonction composée

On sait dériver x ↦ 2x − 1 et x ↦ x³. Mais que vaut la dérivée de x ↦ (2x − 1)³, qui emboîte l'une dans l'autre ? Pour ce cas on peut développer ; pour √(x² − 4x + 5) on ne le peut pas. Quelle règle générale donne la dérivée d'une composée ?

::: exemple Développer pour voir la règle

1. Posons f(x) = 2x − 1 et g(x) = x³, donc (g∘f)(x) = (2x − 1)³ = 8x³ − 12x² + 6x − 1.
2. On dérive terme à terme : (g∘f)′(x) = 24x² − 24x + 6 = 6(4x² − 4x + 1) = 6(2x − 1)².
3. On compare avec les deux dérivées : g′(f(x)) = 3(2x − 1)² et f′(x) = 2, et leur produit est 6(2x − 1)² — le même résultat.

:::

Vérifions numériquement que les deux écritures donnent la même dérivée :

| x | −1 | 0 | 1 | 2 |
| --- | --- | --- | --- | --- |
| (g∘f)′(x) = 24x² − 24x + 6 | 54 | 6 | 6 | 54 |
| g′(f(x)) × f′(x) = 3(2x − 1)² × 2 | 54 | 6 | 6 | 54 |

::: definition
La composée g∘f est la fonction x ↦ g(f(x)) : f est la fonction intérieure, g la fonction extérieure.
:::

::: piege
**Erreur : oublier la dérivée de la fonction intérieure**, écrire ((2x − 1)³)′ = 3(2x − 1)². Elle tente parce qu'on applique la règle de xⁿ en traitant 2x − 1 comme une simple variable. Test en x = 1 : la dérivée vraie vaut 6, la fautive 3. La bonne écriture multiplie par la dérivée de l'intérieur : 3(2x − 1)² × 2 = 6(2x − 1)².
:::

::: propriete
Si f est dérivable sur un intervalle I et g dérivable sur f(I), alors g∘f est dérivable sur I et :
$$ (g∘f)′ = (g′∘f) × f′ $$
Cas fréquents : (fⁿ)′ = nf′fⁿ⁻¹ ; et, si f(x) > 0 sur I, (√f)′ = f′/(2√f). Cas limite : là où f s'annule, √f n'est pas dérivable par ce résultat.
:::

::: exemple Racine d'un trinôme, puis cube d'un quotient

1. h(x) = √(x² − 4x + 5) : le discriminant de u(x) = x² − 4x + 5 vaut 16 − 20 = −4 < 0, donc u > 0 sur ℝ et h est dérivable sur ℝ.
2. Avec u′(x) = 2x − 4, h′(x) = u′/(2√u) = (2x − 4)/(2√(x² − 4x + 5)) = (x − 2)/√(x² − 4x + 5).
3. k(x) = ((x + 1)/(x − 2))³ est dérivable sur ℝ privé de 2. Avec u = (x + 1)/(x − 2), u′ = −3/(x − 2)² (formule du quotient, ad − cb = −2 − 1 = −3).
4. k′ = 3u′u² = 3 × (−3/(x − 2)²) × (x + 1)²/(x − 2)² = −9(x + 1)²/(x − 2)⁴.

:::

::: verifie À toi : une racine qui peut s'annuler
Sur quel ensemble q(x) = √(1 − x²) est-elle dérivable ? Calcule q′(x).

---

La racine n'est dérivable que là où 1 − x² > 0, c'est-à-dire sur ]−1 ; 1[ : en −1 et en 1 la quantité sous la racine s'annule. Avec u(x) = 1 − x² et u′(x) = −2x, q′(x) = u′/(2√u) = −2x/(2√(1 − x²)) = −x/√(1 − x²).
:::

::: retenir
(g∘f)′ = (g′∘f) × f′ : on dérive l'extérieur au point intérieur, puis on multiplie par la dérivée de l'intérieur ; (√f)′ = f′/(2√f) là où f > 0.
:::

## 🔁 Dérivée seconde et point d'inflexion

Sur une montagne russe de profil y = x³ − 6x² + 9x, la tangente en un point est tantôt sous la courbe, tantôt au-dessus. Au point où elle passe de l'un à l'autre, la courbe traverse sa tangente.
Où se trouve ce point, et peut-on le trouver par le calcul ?

::: definition
Si f′ est dérivable sur I, f est **deux fois dérivable** et la dérivée de f′, notée f″, est la **dérivée seconde** de f. Le point M₀(x₀ ; f(x₀)) est un **point d'inflexion** de la courbe si la courbe traverse sa tangente en M₀.
:::

::: figure En I(2 ; 2) la courbe passe de sous la tangente T à au-dessus d'elle : elle la traverse
<svg viewBox="0 0 340 270">
<title>Courbe de x³ − 6x² + 9x : au point I(2 ; 2) elle traverse sa tangente T</title>
<line x1="30" y1="164.69" x2="326" y2="164.69" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="326,164.69 318,168.69 318,160.69" fill="#0f172a"/><line x1="64.15" y1="244" x2="64.15" y2="14" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="64.15,14 68.15,22 60.15,22" fill="#0f172a"/><line x1="121.08" y1="161.69" x2="121.08" y2="167.69" stroke="#0f172a" stroke-width="1.2"/><line x1="178" y1="161.69" x2="178" y2="167.69" stroke="#0f172a" stroke-width="1.2"/><line x1="234.92" y1="161.69" x2="234.92" y2="167.69" stroke="#0f172a" stroke-width="1.2"/><line x1="291.85" y1="161.69" x2="291.85" y2="167.69" stroke="#0f172a" stroke-width="1.2"/><line x1="61.15" y1="132.97" x2="67.15" y2="132.97" stroke="#0f172a" stroke-width="1.2"/><line x1="61.15" y1="101.24" x2="67.15" y2="101.24" stroke="#0f172a" stroke-width="1.2"/><line x1="61.15" y1="69.52" x2="67.15" y2="69.52" stroke="#0f172a" stroke-width="1.2"/><line x1="61.15" y1="37.79" x2="67.15" y2="37.79" stroke="#0f172a" stroke-width="1.2"/><g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="121.08" y="179.69" text-anchor="middle" fill="#0f172a" font-size="10">1</text><text x="178" y="179.69" text-anchor="middle" fill="#0f172a" font-size="10">2</text><text x="240" y="179.69" text-anchor="start" fill="#0f172a" font-size="10">3</text><text x="291.85" y="179.69" text-anchor="middle" fill="#0f172a" font-size="10">4</text><text x="58.15" y="136.47" text-anchor="end" fill="#0f172a" font-size="10">2</text><text x="58.15" y="104.74" text-anchor="end" fill="#0f172a" font-size="10">4</text><text x="58.15" y="73.02" text-anchor="end" fill="#0f172a" font-size="10">6</text><text x="58.15" y="41.29" text-anchor="end" fill="#0f172a" font-size="10">8</text><text x="322" y="158.69" text-anchor="end" fill="#0f172a" font-size="12">x</text><text x="72.15" y="22" text-anchor="start" fill="#0f172a" font-size="12">y</text></g><polyline points="41.38,238.04 43.09,231.34 44.8,224.85 46.51,218.56 48.22,212.47 49.92,206.58 51.63,200.87 53.34,195.36 55.05,190.03 56.75,184.89 58.46,179.93 60.17,175.15 61.88,170.55 63.58,166.13 65.29,161.87 67,157.79 68.71,153.87 70.42,150.12 72.12,146.53 73.83,143.09 75.54,139.82 77.25,136.7 78.95,133.73 80.66,130.91 82.37,128.23 84.08,125.7 85.78,123.31 87.49,121.06 89.2,118.95 90.91,116.97 92.62,115.12 94.32,113.4 96.03,111.81 97.74,110.33 99.45,108.98 101.15,107.75 102.86,106.63 104.57,105.63 106.28,104.74 107.98,103.95 109.69,103.27 111.4,102.69 113.11,102.22 114.82,101.84 116.52,101.55 118.23,101.36 119.94,101.26 121.65,101.25 123.35,101.32 125.06,101.47 126.77,101.7 128.48,102.01 130.18,102.39 131.89,102.85 133.6,103.38 135.31,103.97 137.02,104.62 138.72,105.34 140.43,106.12 142.14,106.95 143.85,107.84 145.55,108.78 147.26,109.77 148.97,110.8 150.68,111.88 152.38,113 154.09,114.15 155.8,115.35 157.51,116.57 159.22,117.83 160.92,119.12 162.63,120.43 164.34,121.76 166.05,123.12 167.75,124.49 169.46,125.88 171.17,127.28 172.88,128.69 174.58,130.11 176.29,131.54 178,132.97 179.71,134.39 181.42,135.82 183.12,137.24 184.83,138.65 186.54,140.05 188.25,141.44 189.95,142.81 191.66,144.17 193.37,145.5 195.08,146.81 196.78,148.1 198.49,149.36 200.2,150.58 201.91,151.78 203.62,152.93 205.32,154.05 207.03,155.13 208.74,156.16 210.45,157.15 212.15,158.09 213.86,158.98 215.57,159.81 217.28,160.59 218.98,161.31 220.69,161.96 222.4,162.56 224.11,163.08 225.82,163.54 227.52,163.92 229.23,164.23 230.94,164.46 232.65,164.61 234.35,164.68 236.06,164.67 237.77,164.57 239.48,164.38 241.18,164.09 242.89,163.71 244.6,163.24 246.31,162.66 248.02,161.98 249.72,161.19 251.43,160.3 253.14,159.3 254.85,158.18 256.55,156.95 258.26,155.6 259.97,154.13 261.68,152.53 263.38,150.81 265.09,148.96 266.8,146.98 268.51,144.87 270.22,142.62 271.92,140.23 273.63,137.7 275.34,135.02 277.05,132.2 278.75,129.23 280.46,126.11 282.17,122.84 283.88,119.41 285.58,115.81 287.29,112.06 289,108.14 290.71,104.06 292.42,99.8 294.12,95.38 295.83,90.78 297.54,86 299.25,81.04 300.95,75.9 302.66,70.57 304.37,65.06 306.08,59.36 307.78,53.46 309.49,47.37 311.2,41.08 312.91,34.59 314.62,27.9" fill="none" stroke="#0f6e56" stroke-width="2.8"/><line x1="81.23" y1="52.07" x2="274.77" y2="213.86" stroke="#d97706" stroke-width="2.4"/><circle cx="178" cy="132.97" r="4" fill="#0f172a" stroke="#ffffff" stroke-width="1.2"/><g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="188" y="124.97" text-anchor="start" fill="#0f172a" font-size="12">I(2 ; 2)</text><text x="87.23" y="48.07" text-anchor="start" fill="#d97706" font-size="11">tangente T</text><text x="291.85" y="50.48" text-anchor="end" fill="#0f6e56" font-size="13">C_f</text></g>
</svg>
:::

Sur la figure, à gauche de I la courbe est sous la tangente T, à droite elle est au-dessus : elle change de côté en I, et c'est cela qu'on veut détecter par le calcul.

::: exemple Le point d'inflexion de x³ − 6x² + 9x

1. f′(x) = 3x² − 12x + 9, puis f″(x) = 6x − 12.
2. f″(x) = 0 ⟺ x = 2, et f″ est négative avant 2 et positive après : f″ s'annule en changeant de signe, car c'est une fonction affine de pente 6 > 0.
3. Le point d'inflexion est I(2 ; f(2)) = (2 ; 2), car f(2) = 8 − 24 + 18 = 2.
4. Tangente en I : f′(2) = 12 − 24 + 9 = −3, donc y = −3(x − 2) + 2 = −3x + 8.
5. Contrôle : f(x) − (−3x + 8) = x³ − 6x² + 12x − 8 = (x − 2)³, négatif avant 2 et positif après : la courbe est sous T puis au-dessus de T, elle la traverse bien.

:::

::: piege
**Erreur : croire que f″(a) = 0 suffit pour un point d'inflexion.** Pour f(x) = x⁴, f″(x) = 12x² s'annule en 0, mais reste positive de part et d'autre. La tangente en 0 est y = 0 et f(x) − 0 = x⁴ ≥ 0 : la courbe reste au-dessus de sa tangente, il n'y a pas d'inflexion (c'est un minimum). L'erreur tente parce que « f″ nulle » ressemble à « la courbure change ». Ce qui compte, c'est le **changement de signe** de f″.
:::

::: propriete
Soit f deux fois dérivable sur un intervalle ouvert I contenant x₀. Deux critères suffisent pour que M₀(x₀ ; f(x₀)) soit un point d'inflexion :
- f″ s'annule et change de signe en x₀ ;
- f′ s'annule en x₀ sans changer de signe (la tangente en M₀ est alors horizontale).

:::

::: exemple Le second critère : f′ qui s'annule sans changer de signe

1. g(x) = x³ − 3x² + 3x donne g′(x) = 3x² − 6x + 3 = 3(x − 1)², positive de part et d'autre de 1 et nulle en 1.
2. g′ s'annule en 1 sans changer de signe : le point I(1 ; g(1)) = (1 ; 1) est un point d'inflexion, de tangente horizontale y = 1.
3. Contrôle : g(x) − 1 = x³ − 3x² + 3x − 1 = (x − 1)³ change de signe en 1 : la courbe traverse sa tangente.

:::

::: verifie À toi : un point d'inflexion et sa tangente
Soit h(x) = x³ − 3x² − 9x + 1. Trouve son point d'inflexion et la tangente en ce point.

---

h′(x) = 3x² − 6x − 9 et h″(x) = 6x − 6, qui s'annule en 1 en changeant de signe : le point d'inflexion a pour abscisse 1. h(1) = 1 − 3 − 9 + 1 = −10, donc I(1 ; −10). Comme h′(1) = 3 − 6 − 9 = −12, la tangente est y = −12(x − 1) − 10 = −12x + 2.
:::

::: retenir
Point d'inflexion = la courbe traverse sa tangente : on le repère où f″ s'annule en changeant de signe (ou où f′ s'annule sans changer de signe) ; f″(a) = 0 seul ne suffit pas.
:::

## 📈 Dérivée et sens de variation

Sur la courbe de f(x) = 2x³ − 9x² + 12x − 4, on voit qu'elle monte, redescend, puis remonte. Là où elle monte, ses tangentes montent : leur pente f′ est positive ; là où elle descend, f′ est négative. Peut-on lire le sens de variation d'une fonction uniquement dans le signe de sa dérivée ?

::: exemple Étudier les variations de f(x) = 2x³ − 9x² + 12x − 4

1. f est un polynôme, dérivable sur ℝ, et f′(x) = 6x² − 18x + 12 = 6(x² − 3x + 2) = 6(x − 1)(x − 2).
2. Le signe d'un trinôme est celui de son coefficient dominant (6 > 0) à l'extérieur des racines 1 et 2, et l'opposé entre elles : f′ > 0 sur ]−∞ ; 1[, f′ < 0 sur ]1 ; 2[, f′ > 0 sur ]2 ; +∞[.
3. Donc f est croissante sur ]−∞ ; 1], décroissante sur [1 ; 2], croissante sur [2 ; +∞[.
4. Valeurs aux changements de sens : f(1) = 2 − 9 + 12 − 4 = 1 et f(2) = 16 − 36 + 24 − 4 = 0.
5. Limites : f est un polynôme de degré 3 de coefficient dominant positif, donc lim −∞ f = −∞ et lim +∞ f = +∞.

:::

::: figure Le tableau de variation de f : le signe de f′ sur la ligne du milieu commande la flèche de la ligne du bas
<svg viewBox="0 0 380 196">
<title>Tableau de variation de f : croissante, décroissante, croissante, avec f(1) = 1 et f(2) = 0</title>
<rect x="8" y="8" width="364" height="180" fill="none" stroke="#0f172a" stroke-width="1.6"/><line x1="8" y1="50" x2="372" y2="50" stroke="#0f172a" stroke-width="1.2"/><line x1="8" y1="98" x2="372" y2="98" stroke="#0f172a" stroke-width="1.2"/><line x1="86" y1="8" x2="86" y2="188" stroke="#0f172a" stroke-width="1.2"/><g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="47" y="34" text-anchor="middle" fill="#0f172a" font-size="14">x</text><text x="47" y="78" text-anchor="middle" fill="#0f172a" font-size="14">f′(x)</text><text x="47" y="150" text-anchor="middle" fill="#0f172a" font-size="14">f</text><text x="128" y="34" text-anchor="middle" fill="#0f172a" font-size="13">−∞</text><text x="206" y="34" text-anchor="middle" fill="#0f172a" font-size="13">1</text><text x="284" y="34" text-anchor="middle" fill="#0f172a" font-size="13">2</text><text x="346" y="34" text-anchor="middle" fill="#0f172a" font-size="13">+∞</text><text x="206" y="78" text-anchor="middle" fill="#0f172a" font-size="13">0</text><text x="284" y="78" text-anchor="middle" fill="#0f172a" font-size="13">0</text><text x="167" y="78" text-anchor="middle" fill="#0f172a" font-size="16">+</text><text x="245" y="78" text-anchor="middle" fill="#0f172a" font-size="16">−</text><text x="315" y="78" text-anchor="middle" fill="#0f172a" font-size="16">+</text><text x="128" y="178" text-anchor="middle" fill="#0f172a" font-size="13">−∞</text><text x="206" y="120" text-anchor="middle" fill="#0f172a" font-size="13">1</text><text x="284" y="174" text-anchor="middle" fill="#0f172a" font-size="13">0</text><text x="346" y="120" text-anchor="middle" fill="#0f172a" font-size="13">+∞</text></g><line x1="206" y1="50" x2="206" y2="98" stroke="#cbd5e1" stroke-width="1"/><line x1="284" y1="50" x2="284" y2="98" stroke="#cbd5e1" stroke-width="1"/><line x1="142" y1="168" x2="192" y2="130" stroke="#2563eb" stroke-width="2.2"/>
<polygon points="192,130 188.05,138.03 183.21,131.66" fill="#2563eb"/><line x1="220" y1="130" x2="270" y2="164" stroke="#d97706" stroke-width="2.2"/>
<polygon points="270,164 261.14,162.81 265.63,156.19" fill="#d97706"/><line x1="298" y1="164" x2="330" y2="130" stroke="#2563eb" stroke-width="2.2"/>
<polygon points="330,130 327.43,138.57 321.6,133.08" fill="#2563eb"/>
</svg>
:::

Dans le tableau, chaque « + » de la ligne f′(x) est une flèche montante sous lui, et chaque « − » une flèche descendante ; les valeurs 1 et 0 sont celles de l'étape 4.

::: piege
**Erreur : lire le signe de f au lieu de celui de f′.** On se dit « f(1,5) = 0,5 est positif, donc f monte en 1,5 ». Or f′(1,5) = 6 × 0,5 × (−0,5) = −1,5 < 0 : f décroît en 1,5, tout en étant positive. L'erreur tente parce que « positif » et « croissant » semblent liés. Ce qui commande la variation, c'est le signe de la **dérivée** ; le signe de f dit seulement si la courbe est au-dessus ou au-dessous de l'axe.
:::

::: propriete
Soit f dérivable sur un intervalle I. f est croissante sur I si et seulement si f′(x) ≥ 0 pour tout x de I ; décroissante sur I si et seulement si f′(x) ≤ 0 pour tout x de I ; constante sur I si et seulement si f′(x) = 0 pour tout x de I.
Cas limite : f′ peut s'annuler en un point isolé sans que le sens de variation change, comme en 0 pour x ↦ x³ (f′(x) = 3x²).
:::

::: verifie À toi : un tableau de variation
Dresse le tableau de variation de g(x) = x³ − 12x + 5 sur ℝ (valeurs aux points où le sens change).

---

g′(x) = 3x² − 12 = 3(x − 2)(x + 2), positive à l'extérieur des racines −2 et 2 (coefficient 3 > 0), négative entre elles. Donc g croît sur ]−∞ ; −2], décroît sur [−2 ; 2], croît sur [2 ; +∞[. Valeurs : g(−2) = −8 + 24 + 5 = 21 et g(2) = 8 − 24 + 5 = −11.
:::

::: retenir
Le signe de f′ sur un intervalle donne le sens de variation de f : f′ ≥ 0 ⟺ croissante, f′ ≤ 0 ⟺ décroissante ; on le résume dans un tableau de variation.
:::

## 🏔️ Extrema et problèmes d'optimisation

Pour fabriquer une boîte sans couvercle, on découpe un carré de côté x cm à chaque coin d'une plaque carrée de 30 cm de côté, puis on replie les bords. Quelle valeur de x donne la boîte de plus grand volume ?

::: figure Plaque de 30 cm dont on retire quatre coins de côté x (dessinés ici avec x = 4 cm pour la lisibilité : x est variable) ; la base de la boîte est le carré de côté 30 − 2x
<svg viewBox="0 0 300 246">
<title>Plaque carrée de 30 cm de côté, quatre coins de côté x découpés ; la base de la boîte est un carré de côté 30 − 2x</title>
<rect x="50" y="24" width="180" height="180" fill="#ecfdf5" stroke="#0f172a" stroke-width="2"/><rect x="50" y="24" width="24" height="24" fill="#fde68a" stroke="#0f172a" stroke-width="1.6"/><rect x="206" y="24" width="24" height="24" fill="#fde68a" stroke="#0f172a" stroke-width="1.6"/><rect x="50" y="180" width="24" height="24" fill="#fde68a" stroke="#0f172a" stroke-width="1.6"/><rect x="206" y="180" width="24" height="24" fill="#fde68a" stroke="#0f172a" stroke-width="1.6"/><polygon points="74,48 206,48 206,180 74,180" fill="none" stroke-dasharray="6 4" stroke="#0f6e56" stroke-width="2"/><g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="62" y="41" text-anchor="middle" fill="#0f172a" font-size="13">x</text><text x="140" y="119" text-anchor="middle" fill="#0f6e56" font-size="13">30 − 2x</text><text x="140" y="16" text-anchor="middle" fill="#0f172a" font-size="13">30</text><text x="42" y="119" text-anchor="end" fill="#0f172a" font-size="13">30</text></g><line x1="50" y1="19" x2="230" y2="19" stroke="#64748b" stroke-width="1"/>
</svg>
:::

::: definition
Soit f définie sur D. S'il existe x₀ de D tel que f(x) ≥ f(x₀) pour tout x de D, f admet un **minimum** en x₀, égal à f(x₀) ; avec f(x) ≤ f(x₀), c'est un **maximum**. Un minimum ou un maximum est un **extremum**. Si l'inégalité est vraie au moins pour les x d'un intervalle ouvert J contenant x₀ et inclus dans D, l'extremum est **local** ; si elle est vraie sur tout D, il est **global**.
:::

::: exemple Le volume maximal de la boîte

1. La base est un carré de côté 30 − 2x (on retire x à chaque bout) et la hauteur vaut x : V(x) = x(30 − 2x)², pour 0 < x < 15.
2. V(x) = 900x − 120x² + 4x³, donc V′(x) = 900 − 240x + 12x² = 12(x − 5)(x − 15) = 12(5 − x)(15 − x).
3. Sur ]0 ; 15[, le facteur 15 − x est positif : V′ a le signe de 5 − x, soit + sur ]0 ; 5[ et − sur ]5 ; 15[.
4. V′ s'annule en 5 en passant de + à − : V est croissante puis décroissante, le maximum est atteint en x = 5, et V(5) = 5 × 20² = 2000.
5. Réponse : x = 5 cm, pour un volume maximal de 2000 cm³ (base 20 cm × 20 cm, hauteur 5 cm).

:::

::: piege
**Erreur : croire que f′(a) = 0 suffit pour un extremum en a.** Pour f(x) = x³, f′(0) = 3 × 0² = 0, mais f est croissante de part et d'autre de 0 : il n'y a ni maximum ni minimum. L'erreur tente parce que tous les extrema ont une tangente horizontale. Mais la réciproque est fausse : f′(a) = 0 est nécessaire, pas suffisant. Il faut en plus que f′ **change de signe** en a.
:::

::: propriete
Soit f dérivable sur un intervalle ouvert I et x₀ un réel de I.
- Si f admet un extremum local en x₀, alors f′(x₀) = 0.
- Si f′ s'annule et change de signe en x₀, alors f admet un extremum local en x₀ : un maximum si le signe passe de + à −, un minimum de − à +.

Cas limite : un extremum local n'est pas forcément global. Pour f(x) = 2x³ − 9x² + 12x − 4 de la notion précédente, le maximum local f(1) = 1 n'est pas global, car f(3) = 5.
:::

::: exemple Un minimum global : x + 4/x sur ]0 ; +∞[

1. f(x) = x + 4/x est dérivable sur ]0 ; +∞[ et f′(x) = 1 − 4/x² = (x² − 4)/x².
2. Sur ]0 ; +∞[, x² > 0 : f′ a le signe de x² − 4 = (x − 2)(x + 2), donc − sur ]0 ; 2[ et + sur ]2 ; +∞[.
3. f décroît puis croît, avec un changement de signe de − à + en 2 : minimum en x = 2, et f(2) = 2 + 2 = 4.
4. Comme f est décroissante avant 2 et croissante après, ce minimum est global : f(x) ≥ 4 pour tout x > 0.

:::

::: verifie À toi : un enclos de surface maximale
On dispose de 40 m de grillage pour clôturer un enclos rectangulaire adossé à un mur (trois côtés à grillager). Si x est la largeur, l'aire est A(x) = x(40 − 2x), avec 0 < x < 20. Trouve x qui rend l'aire maximale, et cette aire.

---

A(x) = 40x − 2x², donc A′(x) = 40 − 4x = 4(10 − x), positif sur ]0 ; 10[ et négatif sur ]10 ; 20[. A′ s'annule en 10 en passant de + à − : maximum en x = 10, et A(10) = 10 × 20 = 200. L'enclos a une largeur de 10 m, une longueur de 20 m et une aire de 200 m².
:::

::: retenir
Un extremum local de f dérivable se cherche là où f′ s'annule en changeant de signe : de + à − un maximum, de − à + un minimum ; f′(a) = 0 seul ne suffit pas.
:::

## 📐 Théorème et inégalités des accroissements finis

Un radar de tronçon constate qu'une voiture a parcouru 180 km en 2 heures : sa vitesse moyenne est de 90 km/h. Le compteur a-t-il indiqué exactement 90 km/h à un instant donné ? Sans calculer la position à chaque instant, on peut l'affirmer : c'est ce que dit le théorème des accroissements finis.

::: figure La corde (AB) de pente 3 et la tangente T en C, parallèles : le rapport (f(b) − f(a))/(b − a) est une pente de tangente
<svg viewBox="0 0 340 270">
<title>Courbe de x³ sur [−1 ; 2] : la tangente T en C est parallèle à la corde (AB)</title>
<line x1="30" y1="188.24" x2="326" y2="188.24" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="326,188.24 318,192.24 318,184.24" fill="#0f172a"/><line x1="142.76" y1="244" x2="142.76" y2="14" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="142.76,14 146.76,22 138.76,22" fill="#0f172a"/><line x1="72.29" y1="185.24" x2="72.29" y2="191.24" stroke="#0f172a" stroke-width="1.2"/><line x1="213.24" y1="185.24" x2="213.24" y2="191.24" stroke="#0f172a" stroke-width="1.2"/><line x1="283.71" y1="185.24" x2="283.71" y2="191.24" stroke="#0f172a" stroke-width="1.2"/><line x1="139.76" y1="153.39" x2="145.76" y2="153.39" stroke="#0f172a" stroke-width="1.2"/><line x1="139.76" y1="118.55" x2="145.76" y2="118.55" stroke="#0f172a" stroke-width="1.2"/><line x1="139.76" y1="83.7" x2="145.76" y2="83.7" stroke="#0f172a" stroke-width="1.2"/><line x1="139.76" y1="48.85" x2="145.76" y2="48.85" stroke="#0f172a" stroke-width="1.2"/><g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="72.29" y="181.24" text-anchor="middle" fill="#0f172a" font-size="10">−1</text><text x="213.24" y="203.24" text-anchor="middle" fill="#0f172a" font-size="10">1</text><text x="283.71" y="203.24" text-anchor="middle" fill="#0f172a" font-size="10">2</text><text x="136.76" y="156.89" text-anchor="end" fill="#0f172a" font-size="10">2</text><text x="136.76" y="122.05" text-anchor="end" fill="#0f172a" font-size="10">4</text><text x="136.76" y="87.2" text-anchor="end" fill="#0f172a" font-size="10">6</text><text x="136.76" y="52.35" text-anchor="end" fill="#0f172a" font-size="10">8</text><text x="322" y="182.24" text-anchor="end" fill="#0f172a" font-size="12">x</text><text x="150.76" y="22" text-anchor="start" fill="#0f172a" font-size="12">y</text></g><polyline points="40.26,241.84 41.87,239.36 43.48,236.96 45.09,234.63 46.69,232.38 48.3,230.2 49.91,228.09 51.52,226.06 53.13,224.09 54.73,222.2 56.34,220.37 57.95,218.61 59.56,216.92 61.16,215.29 62.77,213.72 64.38,212.21 65.99,210.77 67.59,209.38 69.2,208.06 70.81,206.78 72.42,205.57 74.03,204.41 75.63,203.3 77.24,202.24 78.85,201.24 80.46,200.28 82.06,199.37 83.67,198.51 85.28,197.7 86.89,196.93 88.5,196.2 90.1,195.51 91.71,194.87 93.32,194.26 94.93,193.69 96.53,193.16 98.14,192.66 99.75,192.2 101.36,191.78 102.96,191.38 104.57,191.01 106.18,190.68 107.79,190.37 109.4,190.09 111,189.84 112.61,189.61 114.22,189.4 115.83,189.22 117.43,189.05 119.04,188.91 120.65,188.78 122.26,188.67 123.87,188.58 125.47,188.5 127.08,188.43 128.69,188.38 130.3,188.34 131.9,188.31 133.51,188.28 135.12,188.26 136.73,188.25 138.34,188.25 139.94,188.24 141.55,188.24 143.16,188.24 144.77,188.24 146.37,188.24 147.98,188.24 149.59,188.23 151.2,188.21 152.8,188.19 154.41,188.16 156.02,188.13 157.63,188.08 159.24,188.02 160.84,187.95 162.45,187.86 164.06,187.76 165.67,187.64 167.27,187.51 168.88,187.36 170.49,187.18 172.1,186.99 173.71,186.77 175.31,186.53 176.92,186.26 178.53,185.96 180.14,185.64 181.74,185.29 183.35,184.91 184.96,184.5 186.57,184.06 188.17,183.58 189.78,183.07 191.39,182.52 193,181.93 194.61,181.31 196.21,180.64 197.82,179.93 199.43,179.18 201.04,178.39 202.64,177.55 204.25,176.67 205.86,175.74 207.47,174.76 209.08,173.73 210.68,172.65 212.29,171.51 213.9,170.32 215.51,169.08 217.11,167.78 218.72,166.43 220.33,165.01 221.94,163.54 223.55,162 225.15,160.4 226.76,158.74 228.37,157.01 229.98,155.22 231.58,153.36 233.19,151.43 234.8,149.43 236.41,147.36 238.01,145.22 239.62,143.01 241.23,140.72 242.84,138.35 244.45,135.91 246.05,133.39 247.66,130.79 249.27,128.1 250.88,125.34 252.48,122.49 254.09,119.56 255.7,116.54 257.31,113.43 258.92,110.24 260.52,106.95 262.13,103.58 263.74,100.11 265.35,96.55 266.95,92.89 268.56,89.14 270.17,85.3 271.78,81.35 273.39,77.3 274.99,73.16 276.6,68.91 278.21,64.55 279.82,60.1 281.42,55.53 283.03,50.86 284.64,46.09 286.25,41.2 287.85,36.2 289.46,31.09 291.07,25.87 292.68,20.53 294.29,15.07" fill="none" stroke="#0f6e56" stroke-width="2.8"/><line x1="44.1" y1="226.58" x2="304.86" y2="33.17" stroke="#64748b" stroke-width="2" stroke-dasharray="6 4"/><line x1="149.81" y1="217.86" x2="290.76" y2="113.32" stroke="#d97706" stroke-width="2.4"/><circle cx="72.29" cy="205.67" r="4" fill="#0f172a" stroke="#ffffff" stroke-width="1.2"/><circle cx="283.71" cy="48.85" r="4" fill="#0f172a" stroke="#ffffff" stroke-width="1.2"/><circle cx="213.24" cy="170.82" r="4" fill="#0f172a" stroke="#ffffff" stroke-width="1.2"/><g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="82.29" y="219.67" text-anchor="start" fill="#0f172a" font-size="13">A</text><text x="275.71" y="64.85" text-anchor="end" fill="#0f172a" font-size="13">B</text><text x="223.24" y="184.82" text-anchor="start" fill="#d97706" font-size="13">C</text><text x="212.29" y="87.89" text-anchor="end" fill="#64748b" font-size="11">(AB)</text><text x="296.76" y="117.32" text-anchor="start" fill="#d97706" font-size="12">T</text><text x="241.43" y="120.29" text-anchor="end" fill="#0f6e56" font-size="13">C_f</text></g>
</svg>
:::

::: exemple La corde et la tangente de x³ sur [−1 ; 2]

1. f(x) = x³ est continue sur [−1 ; 2] et dérivable sur ]−1 ; 2[ : les hypothèses sont vérifiées avant toute chose.
2. Pente de la corde AB, avec A(−1 ; −1) et B(2 ; 8) : (f(2) − f(−1))/(2 − (−1)) = 9/3 = 3.
3. On cherche c tel que f′(c) = 3c² = 3, soit c² = 1 : c = 1 ou c = −1. Seul c = 1 est dans ]−1 ; 2[, car −1 est une borne.
4. La tangente en C(1 ; 1) est y = 3(x − 1) + 1 = 3x − 2 ; la droite (AB) est y = 3x + 2 : mêmes pentes, elles sont parallèles.

:::

::: piege
**Erreur : appliquer le théorème sans vérifier ses hypothèses.** Pour f(x) = |x| sur [−1 ; 2], la pente de la corde est (2 − 1)/(2 − (−1)) = 1/3. Or f′(x) vaut −1 sur ]−1 ; 0[ et 1 sur ]0 ; 2[ : jamais 1/3. Le théorème ne s'applique pas, car f n'est pas dérivable en 0, point de ]−1 ; 2[. L'erreur tente parce que la conclusion semble « évidente » pour toute courbe. Elle ne l'est que si f est continue sur [a ; b] et dérivable sur ]a ; b[.
:::

::: propriete
**Théorème des accroissements finis** (admis) : si f est continue sur [a ; b] et dérivable sur ]a ; b[, il existe au moins un réel c de ]a ; b[ tel que f′(c) = (f(b) − f(a))/(b − a) : la tangente en c est parallèle à la corde (AB).
**Inégalités des accroissements finis** (admises) : si f est dérivable sur un intervalle I et si m ≤ f′(x) ≤ M pour tout x de I, alors pour tous a < b de I, m(b − a) ≤ f(b) − f(a) ≤ M(b − a). Corollaire : si |f′(x)| ≤ k sur I, alors |f(b) − f(a)| ≤ k|b − a| pour tous a et b de I.
:::

::: exemple Encadrer √101, puis majorer un écart

1. f(x) = √x est dérivable sur [100 ; 101] et f′(x) = 1/(2√x) y est décroissante, donc f′(x) ≤ 1/20 (valeur en 100) et f′(x) ≥ 1/(2√101).
2. Comme 101 < 121, √101 < 11, donc 1/(2√101) > 1/22 : on a 1/22 ≤ f′(x) ≤ 1/20 sur [100 ; 101].
3. Avec a = 100 et b = 101 : (1/22)(1) ≤ √101 − 10 ≤ (1/20)(1), soit 10,0454 ≤ √101 ≤ 10,05.
4. Corollaire : g(x) = 1/x sur [1 ; +∞[ vérifie |g′(x)| = 1/x² ≤ 1, donc |1/b − 1/a| ≤ |b − a| pour tous a et b de [1 ; +∞[.

:::

::: verifie À toi : encadrer √26
Avec f(x) = √x sur [25 ; 26], encadre √26 par l'inégalité des accroissements finis. On rappelle que √26 < 6.

---

f est dérivable sur [25 ; 26] et f′(x) = 1/(2√x) y est décroissante : f′(x) ≤ 1/(2√25) = 1/10 et f′(x) ≥ 1/(2√26) > 1/12 puisque √26 < 6. Avec b − a = 1 : 1/12 ≤ √26 − 5 ≤ 1/10, soit 5,0833 ≤ √26 ≤ 5,1.
:::

::: retenir
TAF : f continue sur [a ; b] et dérivable sur ]a ; b[ ⟹ il existe c avec f′(c) = (f(b) − f(a))/(b − a). Si m ≤ f′ ≤ M : m(b − a) ≤ f(b) − f(a) ≤ M(b − a).
:::

> 🏆 Tu sais maintenant lire une courbe point par point : tangente, pointe, inflexion, montée, sommet, et même encadrer ce qu'un calculateur n'a pas encore calculé.
