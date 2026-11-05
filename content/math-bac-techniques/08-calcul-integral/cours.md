# ⚔️ Calcul intégral — de la primitive à l'aire, au volume et à la moyenne

> 💡 «Une primitive mesure ce qui s'accumule ; l'intégrale lit le total entre deux instants.»

Le chapitre des primitives laissait une question ouverte : que représente la différence F(b) − F(a) ? Ce chapitre lui donne un nom, l'intégrale, et en tire des propriétés de calcul, des aires, des volumes et des moyennes. Huit notions, avec un fil rouge : un réservoir que remplit un robinet au débit q(t) = 2t + 1 (en L/min) à l'instant t (en min).

## 🎯 L'intégrale d'une fonction continue

Le robinet débite q(t) = 2t + 1 litres par minute. Entre t = 1 et t = 3, le débit passe de 3 à 7 L/min : sous la droite de q, on voit un trapèze de hauteurs 3 et 7 et de largeur 2, d'aire (3 + 7)/2 × 2 = 10. D'autre part, la quantité d'eau versée depuis l'ouverture est Q(t) = t² + t, car Q′(t) = 2t + 1 = q(t), et Q(3) − Q(1) = 12 − 2 = 10. Les deux calculs coïncident.
Le nombre F(b) − F(a) mesure-t-il toujours ce qui s'accumule entre a et b, et dépend-il de la primitive choisie ?

::: figure Entre t = 1 et t = 3, la surface sous la droite q(t) = 2t + 1 est un trapèze : son aire, 10, est le volume d'eau (en L) versé
<svg viewBox="0 0 340 250">
<title>Le trapèze sous la droite q(t) = 2t + 1 entre t = 1 et t = 3 : hauteurs 3 et 7, largeur 2</title>
<polygon points="119.83,200.46 119.83,142.19 236.5,64.5 236.5,200.46" fill="#0f6e56" fill-opacity="0.22" stroke="#0f6e56" stroke-width="1.6"/>
<line x1="49.83" y1="200.46" x2="324" y2="200.46" stroke="#0f172a" stroke-width="1.6"/>
<line x1="61.5" y1="208.23" x2="61.5" y2="14" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="324,200.46 316,204.46 316,196.46" fill="#0f172a"/>
<polygon points="61.5,14 65.5,22 57.5,22" fill="#0f172a"/>
<line x1="119.83" y1="197.46" x2="119.83" y2="203.46" stroke="#0f172a" stroke-width="1.2"/>
<line x1="236.5" y1="197.46" x2="236.5" y2="203.46" stroke="#0f172a" stroke-width="1.2"/>
<line x1="58.5" y1="142.19" x2="64.5" y2="142.19" stroke="#0f172a" stroke-width="1.2"/>
<line x1="58.5" y1="64.5" x2="64.5" y2="64.5" stroke="#0f172a" stroke-width="1.2"/>
<line x1="61.5" y1="142.19" x2="119.83" y2="142.19" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="4 3"/>
<line x1="61.5" y1="64.5" x2="236.5" y2="64.5" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="4 3"/>
<polyline points="61.5,181.04 90.67,161.62 119.83,142.19 149,122.77 178.17,103.35 207.33,83.92 236.5,64.5 265.67,45.08 294.83,25.65" fill="none" stroke="#d97706" stroke-width="2.8"/>
<circle cx="119.83" cy="142.19" r="3.8" fill="#0f172a" stroke="#ffffff" stroke-width="1.2"/>
<circle cx="236.5" cy="64.5" r="3.8" fill="#0f172a" stroke="#ffffff" stroke-width="1.2"/>
<g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="320" y="218.46" text-anchor="end" fill="#0f172a" font-size="12">t</text><text x="71.5" y="22" text-anchor="start" fill="#0f172a" font-size="12">q</text><text x="119.83" y="216.46" text-anchor="middle" fill="#0f172a" font-size="11">1</text><text x="236.5" y="216.46" text-anchor="middle" fill="#0f172a" font-size="11">3</text><text x="54.5" y="146.19" text-anchor="end" fill="#0f172a" font-size="11">3</text><text x="54.5" y="68.5" text-anchor="end" fill="#0f172a" font-size="11">7</text><text x="290.83" y="17.65" text-anchor="end" fill="#d97706" font-size="12">q(t) = 2t + 1</text><text x="178.17" y="165.62" text-anchor="middle" fill="#0f6e56" font-size="13">aire = 10</text></g>
</svg>
:::

Les hauteurs du trapèze, 3 à gauche et 7 à droite, sont les valeurs q(1) et q(3) lues sur la droite.

::: definition
Soit f une fonction continue sur un intervalle I, F une primitive de f sur I, a et b deux réels de I. Le nombre F(b) − F(a) ne dépend pas de la primitive choisie : c'est **l'intégrale de a à b de f**, notée ∫ₐᵇ f(x)dx.
∫ₐᵇ f(x)dx = [F(x)]ₐᵇ = F(b) − F(a)
:::

::: exemple Le volume versé par le robinet

1. q(t) = 2t + 1 est continue sur ℝ, donc elle a des primitives ; F(t) = t² + t en est une, car F′(t) = 2t + 1.
2. ∫₁³ (2t + 1)dt = [t² + t]₁³ = F(3) − F(1), par définition.
3. F(3) = 9 + 3 = 12 et F(1) = 1 + 1 = 2, donc l'intégrale vaut 10 : c'est l'aire du trapèze, en litres.
4. Avec une autre primitive, G(t) = t² + t + 5, on trouve G(3) − G(1) = 17 − 7 = 10 : la constante disparaît dans la soustraction.

:::

::: exemple Le même outil, sans situation

1. I = ∫₀¹ (4x³ − e^{−x})dx. La fonction est continue sur ℝ ; une primitive est F(x) = x⁴ + e^{−x}, car (e^{−x})′ = −e^{−x}.
2. I = [x⁴ + e^{−x}]₀¹ = F(1) − F(0).
3. F(1) = 1 + e⁻¹ et F(0) = 0 + 1 = 1, donc I = e⁻¹ ≈ 0,37.

:::

::: piege
**Erreur : ne calculer que F(b).** Pour ∫₁³ (2t + 1)dt, on écrit F(3) = 12 et l'on répond 12. L'erreur tente parce que, lorsque la borne inférieure est 0, F(0) = 0 et l'on n'a en effet besoin que de F(b). Ici F(1) = 2 n'est pas nul : il faut soustraire, 12 − 2 = 10.
:::

::: propriete
Si f est continue sur [a, b], l'intégrale ∫ₐᵇ f(x)dx existe. La lettre x est muette : ∫ₐᵇ f(x)dx = ∫ₐᵇ f(t)dt, et elle disparaît du résultat. Pour une constante k, ∫ₐᵇ k dt = k(b − a).
Cas limite : si a = b, F(a) − F(a) = 0. Et quand la borne supérieure est la variable x, on écrit ∫₀ˣ f(t)dt, jamais ∫₀ˣ f(x)dx.
:::

::: verifie À toi : une intégrale trigonométrique
Calculer ∫₀^{π/2} (3 cos x + 2)dx.

---

Une primitive de 3 cos x + 2 est F(x) = 3 sin x + 2x, car (sin x)′ = cos x. Alors F(π/2) = 3 + π et F(0) = 0, donc l'intégrale vaut F(π/2) − F(0) = 3 + π : on évalue aux deux bornes et on soustrait.
:::

::: retenir
L'intégrale de a à b d'une fonction continue f est F(b) − F(a) pour n'importe quelle primitive F de f : on évalue aux deux bornes et on soustrait.
:::

## 🔗 Bornes, relation de Chasles et linéarité

On veut le volume versé entre t = 0 et t = 3 en coupant la durée à t = 1, puis comparer avec le volume « à l'envers », quand on parcourt le temps de 3 vers 1.
Peut-on toujours couper une intégrale, échanger les bornes, séparer une somme ?

::: exemple Couper la durée du robinet

1. Avec F(t) = t² + t : ∫₀³ q = F(3) − F(0) = 12.
2. ∫₀¹ q = F(1) − F(0) = 2 et ∫₁³ q = F(3) − F(1) = 10 : la somme 2 + 10 = 12, car F(1) est ajouté puis retranché.
3. ∫₃¹ q = F(1) − F(3) = −10 : échanger les bornes change le signe.
4. ∫₁³ (2t + 1)dt = 2∫₁³ t dt + ∫₁³ 1 dt = 2 × 4 + 2 = 10, car ∫₁³ t dt = [t²/2]₁³ = 9/2 − 1/2 = 4 et ∫₁³ 1 dt = 3 − 1 = 2.

:::

::: piege
**Erreur : intégrer un produit comme le produit des intégrales.** Pour ∫₀¹ x × x dx, on écrit (∫₀¹ x dx) × (∫₀¹ x dx) = 1/2 × 1/2 = 1/4. L'erreur tente parce que la linéarité traverse les sommes et les constantes. Mais ∫₀¹ x² dx = [x³/3]₀¹ = 1/3 ≠ 1/4 : la linéarité ne concerne pas les produits.
:::

::: propriete
Soit f et g continues sur un intervalle I, a, b, c dans I, k et l réels.
**Bornes** : ∫ₐᵃ f = 0 et ∫_bᵃ f = −∫ₐᵇ f.
**Chasles** : ∫ₐᵇ f = ∫ₐᶜ f + ∫_cᵇ f.
**Linéarité** : ∫ₐᵇ (kf + lg) = k∫ₐᵇ f + l∫ₐᵇ g.
Cas limite : c peut sortir de [a, b]. Avec q(t) = 2t + 1 : ∫₀¹ q = 2, et ∫₀² q + ∫₂¹ q = 6 + (−4) = 2.
:::

::: exemple Une valeur absolue

1. I = ∫₀⁴ |x − 3|dx. On ne sait pas primitiver |x − 3| d'un bloc : |x − 3| = 3 − x pour x ≤ 3 et x − 3 pour x ≥ 3, donc on coupe en 3 (Chasles).
2. ∫₀³ (3 − x)dx = [3x − x²/2]₀³ = 9 − 9/2 = 9/2.
3. ∫₃⁴ (x − 3)dx = [x²/2 − 3x]₃⁴ = (8 − 12) − (9/2 − 9) = 1/2.
4. I = 9/2 + 1/2 = 5.

:::

::: verifie À toi : couper une valeur absolue
Calculer ∫₋₁³ |x − 1|dx.

---

On coupe en 1, où x − 1 change de signe. ∫₋₁¹ (1 − x)dx = [x − x²/2]₋₁¹ = 1/2 − (−3/2) = 2, et ∫₁³ (x − 1)dx = [x²/2 − x]₁³ = 3/2 − (−1/2) = 2. Par Chasles, l'intégrale vaut 2 + 2 = 4.
:::

::: retenir
Une intégrale se coupe (Chasles), change de signe quand on échange les bornes, et se sépare en sommes et en multiples constants, jamais en produits.
:::

## ⚖️ Parité et périodicité

Une arche de pont a pour profil la courbe de g(x) = 4 − x², entre x = −2 et x = 2. Elle est symétrique par rapport à l'axe des ordonnées : la moitié gauche de la surface semble égale à la moitié droite.
Peut-on alors calculer un seul côté et doubler, et que se passe-t-il quand la symétrie est autour de l'origine plutôt que de l'axe ?

::: figure La courbe de g est symétrique par rapport à (Oy) : les zones A₁ et A₂ sont l'image l'une de l'autre, donc égales
<svg viewBox="0 0 340 230">
<title>La courbe de g(x) = 4 − x² entre −2 et 2, symétrique par rapport à l'axe des ordonnées : les deux zones colorées A₁ et A₂ sont égales</title>
<polygon points="70,155.72 71.67,151.9 73.33,148.14 75,144.44 76.67,140.81 78.33,137.24 80,133.74 81.67,130.3 83.33,126.93 85,123.62 86.67,120.37 88.33,117.19 90,114.07 91.67,111.02 93.33,108.03 95,105.11 96.67,102.25 98.33,99.45 100,96.72 101.67,94.05 103.33,91.45 105,88.91 106.67,86.44 108.33,84.03 110,81.68 111.67,79.4 113.33,77.18 115,75.03 116.67,72.94 118.33,70.91 120,68.95 121.67,67.06 123.33,65.23 125,63.46 126.67,61.76 128.33,60.12 130,58.54 131.67,57.03 133.33,55.58 135,54.2 136.67,52.89 138.33,51.63 140,50.44 141.67,49.32 143.33,48.26 145,47.26 146.67,46.33 148.33,45.46 150,44.66 151.67,43.92 153.33,43.24 155,42.63 156.67,42.09 158.33,41.61 160,41.19 161.67,40.83 163.33,40.54 165,40.32 166.67,40.16 168.33,40.06 170,40.03 170,155.72 168.33,155.72 166.67,155.72 165,155.72 163.33,155.72 161.67,155.72 160,155.72 158.33,155.72 156.67,155.72 155,155.72 153.33,155.72 151.67,155.72 150,155.72 148.33,155.72 146.67,155.72 145,155.72 143.33,155.72 141.67,155.72 140,155.72 138.33,155.72 136.67,155.72 135,155.72 133.33,155.72 131.67,155.72 130,155.72 128.33,155.72 126.67,155.72 125,155.72 123.33,155.72 121.67,155.72 120,155.72 118.33,155.72 116.67,155.72 115,155.72 113.33,155.72 111.67,155.72 110,155.72 108.33,155.72 106.67,155.72 105,155.72 103.33,155.72 101.67,155.72 100,155.72 98.33,155.72 96.67,155.72 95,155.72 93.33,155.72 91.67,155.72 90,155.72 88.33,155.72 86.67,155.72 85,155.72 83.33,155.72 81.67,155.72 80,155.72 78.33,155.72 76.67,155.72 75,155.72 73.33,155.72 71.67,155.72 70,155.72" fill="#0f6e56" fill-opacity="0.22" stroke="none" stroke-width="0"/>
<polygon points="170,40.03 171.67,40.06 173.33,40.16 175,40.32 176.67,40.54 178.33,40.83 180,41.19 181.67,41.61 183.33,42.09 185,42.63 186.67,43.24 188.33,43.92 190,44.66 191.67,45.46 193.33,46.33 195,47.26 196.67,48.26 198.33,49.32 200,50.44 201.67,51.63 203.33,52.89 205,54.2 206.67,55.58 208.33,57.03 210,58.54 211.67,60.12 213.33,61.76 215,63.46 216.67,65.23 218.33,67.06 220,68.95 221.67,70.91 223.33,72.94 225,75.03 226.67,77.18 228.33,79.4 230,81.68 231.67,84.03 233.33,86.44 235,88.91 236.67,91.45 238.33,94.05 240,96.72 241.67,99.45 243.33,102.25 245,105.11 246.67,108.03 248.33,111.02 250,114.07 251.67,117.19 253.33,120.37 255,123.62 256.67,126.93 258.33,130.3 260,133.74 261.67,137.24 263.33,140.81 265,144.44 266.67,148.14 268.33,151.9 270,155.72 270,155.72 268.33,155.72 266.67,155.72 265,155.72 263.33,155.72 261.67,155.72 260,155.72 258.33,155.72 256.67,155.72 255,155.72 253.33,155.72 251.67,155.72 250,155.72 248.33,155.72 246.67,155.72 245,155.72 243.33,155.72 241.67,155.72 240,155.72 238.33,155.72 236.67,155.72 235,155.72 233.33,155.72 231.67,155.72 230,155.72 228.33,155.72 226.67,155.72 225,155.72 223.33,155.72 221.67,155.72 220,155.72 218.33,155.72 216.67,155.72 215,155.72 213.33,155.72 211.67,155.72 210,155.72 208.33,155.72 206.67,155.72 205,155.72 203.33,155.72 201.67,155.72 200,155.72 198.33,155.72 196.67,155.72 195,155.72 193.33,155.72 191.67,155.72 190,155.72 188.33,155.72 186.67,155.72 185,155.72 183.33,155.72 181.67,155.72 180,155.72 178.33,155.72 176.67,155.72 175,155.72 173.33,155.72 171.67,155.72 170,155.72" fill="#d97706" fill-opacity="0.22" stroke="none" stroke-width="0"/>
<line x1="25" y1="155.72" x2="315" y2="155.72" stroke="#0f172a" stroke-width="1.6"/>
<line x1="170" y1="196.22" x2="170" y2="14" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="315,155.72 307,159.72 307,151.72" fill="#0f172a"/>
<polygon points="170,14 174,22 166,22" fill="#0f172a"/>
<line x1="70" y1="152.72" x2="70" y2="158.72" stroke="#0f172a" stroke-width="1.2"/>
<line x1="270" y1="152.72" x2="270" y2="158.72" stroke="#0f172a" stroke-width="1.2"/>
<line x1="167" y1="40.03" x2="173" y2="40.03" stroke="#0f172a" stroke-width="1.2"/>
<polyline points="55,193.03 58.83,183 62.67,173.31 66.5,163.96 70.33,154.95 74.17,146.28 78,137.95 81.83,129.96 85.67,122.31 89.5,115 93.33,108.03 97.17,101.4 101,95.11 104.83,89.16 108.67,83.55 112.5,78.28 116.33,73.35 120.17,68.76 124,64.51 127.83,60.6 131.67,57.03 135.5,53.8 139.33,50.91 143.17,48.36 147,46.15 150.83,44.28 154.67,42.75 158.5,41.56 162.33,40.71 166.17,40.2 170,40.03 173.83,40.2 177.67,40.71 181.5,41.56 185.33,42.75 189.17,44.28 193,46.15 196.83,48.36 200.67,50.91 204.5,53.8 208.33,57.03 212.17,60.6 216,64.51 219.83,68.76 223.67,73.35 227.5,78.28 231.33,83.55 235.17,89.16 239,95.11 242.83,101.4 246.67,108.03 250.5,115 254.33,122.31 258.17,129.96 262,137.95 265.83,146.28 269.67,154.95 273.5,163.96 277.33,173.31 281.17,183 285,193.03" fill="none" stroke="#0f172a" stroke-width="2.8"/>
<g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="311" y="173.72" text-anchor="end" fill="#0f172a" font-size="12">x</text><text x="180" y="22" text-anchor="start" fill="#0f172a" font-size="12">y</text><text x="70" y="171.72" text-anchor="middle" fill="#0f172a" font-size="11">−2</text><text x="270" y="171.72" text-anchor="middle" fill="#0f172a" font-size="11">2</text><text x="163" y="44.03" text-anchor="end" fill="#0f172a" font-size="11">4</text><text x="120" y="118.12" text-anchor="middle" fill="#0f6e56" font-size="14">A₁</text><text x="220" y="118.12" text-anchor="middle" fill="#d97706" font-size="14">A₂</text><text x="232.5" y="51.6" text-anchor="start" fill="#0f172a" font-size="12">y = 4 − x²</text></g>
</svg>
:::

L'égalité des deux zones de la figure s'écrit ∫₋₂⁰ g = ∫₀² g.

::: exemple L'arche, côté par côté

1. g(−x) = 4 − (−x)² = g(x) : g est paire.
2. ∫₀² (4 − x²)dx = [4x − x³/3]₀² = 8 − 8/3 = 16/3.
3. ∫₋₂⁰ (4 − x²)dx = [4x − x³/3]₋₂⁰ = 0 − (−8 + 8/3) = 16/3 : même valeur que la moitié droite.
4. ∫₋₂² g = 16/3 + 16/3 = 32/3 (Chasles).

:::

::: exemple Une fonction impaire plus une constante

1. I = ∫₋₂² (x³ − 5x + 3)dx = ∫₋₂² (x³ − 5x)dx + ∫₋₂² 3 dx (linéarité).
2. h(x) = x³ − 5x vérifie h(−x) = −h(x) : elle est impaire. Sur [−2 ; 2], ∫ h = [x⁴/4 − 5x²/2]₋₂² = (4 − 10) − (4 − 10) = 0.
3. ∫₋₂² 3 dx = 3 × (2 − (−2)) = 12.
4. I = 0 + 12 = 12.

:::

::: exemple Un tour complet

1. I = ∫_{π/3}^{7π/3} (2 + cos t)dt. La fonction est 2π-périodique, et 7π/3 − π/3 = 2π : on intègre sur une période entière.
2. I = ∫₀^{2π} (2 + cos t)dt = [2t + sin t]₀^{2π} = 4π.

:::

::: piege
**Erreur : croire qu'une fonction paire a une intégrale nulle.** Pour ∫₋₂² x² dx, on écrit « x² est symétrique, donc ça s'annule » et l'on répond 0. L'erreur tente parce que l'annulation vient bien d'une symétrie, mais de celle par rapport à l'origine (fonction impaire). Pour x², les deux moitiés s'ajoutent : 2∫₀² x² dx = 2 × 8/3 = 16/3.
:::

::: propriete
**Parité** : f continue sur [−a ; a]. Si f est paire, ∫₋ₐᵃ f = 2∫₀ᵃ f ; si f est impaire, ∫₋ₐᵃ f = 0.
**Périodicité** : f continue sur ℝ et de période T : pour tout réel a, ∫ₐ^{a+T} f = ∫₀ᵀ f.
Cas limite : l'intervalle doit être symétrique. Pour x³, impaire, ∫₋₁² x³ dx = [x⁴/4]₋₁² = 4 − 1/4 = 15/4, et non 0.
:::

::: verifie À toi : parité et linéarité
Calculer ∫₋₁¹ (x⁴ + 3x³ − 2)dx.

---

Sur [−1 ; 1], x⁴ − 2 est paire et 3x³ est impaire. La partie impaire donne 0, la partie paire donne 2∫₀¹ (x⁴ − 2)dx = 2[x⁵/5 − 2x]₀¹ = 2 × (−9/5) = −18/5.
:::

::: retenir
Sur [−a ; a], paire donne 2∫₀ᵃ et impaire donne 0 ; sur une période entière, l'intégrale ne dépend pas du point de départ.
:::

## 📏 Intégrale, ordre et valeur moyenne

Entre t = 1 et t = 3, le débit q(t) = 2t + 1 passe de 3 à 7 L/min. Sans aucune intégrale, on sait déjà que le volume versé dépasse celui d'un débit constant de 3 L/min pendant 2 min, soit 6 L, et reste sous 7 × 2 = 14 L ; les 10 L calculés plus haut sont dans cet encadrement.
Comment justifier un tel encadrement, et quel débit constant verserait exactement 10 L ?

::: figure Sur [1 ; 3], le rectangle de hauteur m = 3 est sous la courbe, celui de hauteur M = 7 la dépasse, et la hauteur moyenne μ = 5 est atteinte en c = 2
<svg viewBox="0 0 340 250">
<title>Le débit q(t) = 2t + 1 sur [1 ; 3] : le rectangle de hauteur m = 3 est sous la courbe, celui de hauteur M = 7 la dépasse, et la hauteur μ = 5 est atteinte en c = 2</title>
<polygon points="119.83,200.46 119.83,142.19 236.5,142.19 236.5,200.46" fill="#0f6e56" fill-opacity="0.22" stroke="#0f6e56" stroke-width="1.4"/>
<line x1="119.83" y1="103.35" x2="236.5" y2="103.35" stroke="#d97706" stroke-width="2.4" stroke-dasharray="6 4"/>
<line x1="119.83" y1="64.5" x2="236.5" y2="64.5" stroke="#2563eb" stroke-width="2" stroke-dasharray="6 4"/>
<line x1="119.83" y1="142.19" x2="119.83" y2="64.5" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="3 3"/>
<line x1="236.5" y1="142.19" x2="236.5" y2="64.5" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="3 3"/>
<line x1="49.83" y1="200.46" x2="324" y2="200.46" stroke="#0f172a" stroke-width="1.6"/>
<line x1="61.5" y1="208.23" x2="61.5" y2="14" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="324,200.46 316,204.46 316,196.46" fill="#0f172a"/>
<polygon points="61.5,14 65.5,22 57.5,22" fill="#0f172a"/>
<line x1="119.83" y1="197.46" x2="119.83" y2="203.46" stroke="#0f172a" stroke-width="1.2"/>
<line x1="178.17" y1="197.46" x2="178.17" y2="203.46" stroke="#0f172a" stroke-width="1.2"/>
<line x1="236.5" y1="197.46" x2="236.5" y2="203.46" stroke="#0f172a" stroke-width="1.2"/>
<line x1="58.5" y1="142.19" x2="64.5" y2="142.19" stroke="#0f172a" stroke-width="1.2"/>
<line x1="58.5" y1="103.35" x2="64.5" y2="103.35" stroke="#0f172a" stroke-width="1.2"/>
<line x1="58.5" y1="64.5" x2="64.5" y2="64.5" stroke="#0f172a" stroke-width="1.2"/>
<polyline points="96.5,157.73 116.92,144.13 137.33,130.54 157.75,116.94 178.17,103.35 198.58,89.75 219,76.15 239.42,62.56 259.83,48.96" fill="none" stroke="#0f172a" stroke-width="2.8"/>
<circle cx="178.17" cy="103.35" r="4.4" fill="#d97706" stroke="#ffffff" stroke-width="1.2"/>
<g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="320" y="218.46" text-anchor="end" fill="#0f172a" font-size="12">t</text><text x="71.5" y="22" text-anchor="start" fill="#0f172a" font-size="12">q</text><text x="119.83" y="216.46" text-anchor="middle" fill="#0f172a" font-size="11">1</text><text x="178.17" y="216.46" text-anchor="middle" fill="#0f172a" font-size="11">2</text><text x="236.5" y="216.46" text-anchor="middle" fill="#0f172a" font-size="11">3</text><text x="54.5" y="146.19" text-anchor="end" fill="#0f172a" font-size="11">3</text><text x="54.5" y="107.35" text-anchor="end" fill="#0f172a" font-size="11">5</text><text x="54.5" y="68.5" text-anchor="end" fill="#0f172a" font-size="11">7</text><text x="246.33" y="146.19" text-anchor="start" fill="#0f6e56" font-size="12">m = 3</text><text x="246.33" y="107.35" text-anchor="start" fill="#d97706" font-size="12">μ = 5</text><text x="178.17" y="56.5" text-anchor="middle" fill="#2563eb" font-size="12">M = 7</text><text x="178.17" y="230.46" text-anchor="middle" fill="#d97706" font-size="11">c = 2</text></g>
</svg>
:::

Les hauteurs m, μ et M de la figure sont les nombres 3, 5 et 7 qui encadrent les valeurs de q.

::: exemple Encadrer puis moyenner le débit

1. Sur [1 ; 3], q est croissante, donc 3 ≤ q(t) ≤ 7 : m = 3 et M = 7.
2. En intégrant ces inégalités sur [1 ; 3], de longueur 2 : 3 × 2 ≤ ∫₁³ q ≤ 7 × 2, soit 6 ≤ 10 ≤ 14.
3. Le débit constant qui verse autant est μ = (1/2) × ∫₁³ q = 10/2 = 5 L/min.
4. Ce débit est atteint par q : q(c) = 5 s'écrit 2c + 1 = 5, donc c = 2, qui est bien dans [1 ; 3].

:::

::: piege
**Erreur : prendre pour valeur moyenne la moyenne des valeurs aux bornes.** Pour q, (3 + 7)/2 = 5 donne bien μ. On en conclut que μ = (f(a) + f(b))/2 pour toute fonction. L'erreur tente parce que ce résultat est exact pour une fonction affine. Mais pour f(x) = x² sur [0 ; 3], (0 + 9)/2 = 9/2 alors que μ = (1/3)∫₀³ x² dx = (1/3) × 9 = 3.
:::

::: propriete
Soit f et g continues sur [a ; b], avec a ≤ b (a < b pour l'encadrement).
**Ordre** : si f ≥ 0 sur [a ; b], alors ∫ₐᵇ f ≥ 0 ; si f ≤ g sur [a ; b], alors ∫ₐᵇ f ≤ ∫ₐᵇ g ; et |∫ₐᵇ f| ≤ ∫ₐᵇ |f|.
**Encadrement** : si m ≤ f ≤ M sur [a ; b], alors m(b − a) ≤ ∫ₐᵇ f ≤ M(b − a).
Cas limite : il faut a ≤ b. Pour q ≥ 0, ∫₃¹ q = −10 est négative. L'inégalité de la valeur absolue peut être stricte : ∫₀⁴ (x − 3)dx = −4 et ∫₀⁴ |x − 3|dx = 5, avec 4 < 5.
:::

::: propriete
**Théorème de la moyenne** : si f est continue sur [a ; b], avec a < b, il existe au moins un c de [a ; b] tel que f(c) = (1/(b − a))∫ₐᵇ f(x)dx. Ce nombre est la **valeur moyenne** de f sur [a ; b].
:::

::: exemple Une valeur moyenne qui n'est pas une moyenne de bornes

1. f(x) = x² sur [0 ; 3] : ∫₀³ x² dx = [x³/3]₀³ = 9.
2. μ = (1/3) × 9 = 3.
3. f(c) = 3 s'écrit c² = 3, donc c = √3 ou c = −√3 ; seul √3 ≈ 1,73 appartient à [0 ; 3].

:::

::: verifie À toi : valeur moyenne de 1/x
Déterminer la valeur moyenne de f(x) = 1/x sur [1 ; 3], puis le réel c du théorème.

---

∫₁³ (1/x)dx = [ln x]₁³ = ln 3, donc μ = (ln 3)/2 ≈ 0,55. Le réel c vérifie 1/c = (ln 3)/2, donc c = 2/(ln 3) ≈ 1,82, qui appartient bien à [1 ; 3].
:::

::: retenir
L'intégrale respecte l'ordre quand a < b, ce qui donne m(b − a) ≤ ∫ₐᵇ f ≤ M(b − a) ; la valeur moyenne est (1/(b − a))∫ₐᵇ f, atteinte au moins une fois.
:::

## 🧩 Intégration par parties

On veut I = ∫₀¹ x e^{2x}dx. Le produit x e^{2x} n'est ni de la forme u′uⁿ, ni dans le tableau des primitives. Mais la dérivée d'un produit contient des produits : (uv)′ = u′v + uv′. En intégrant de a à b, [uv]ₐᵇ = ∫ₐᵇ u′v + ∫ₐᵇ uv′.
Si l'une des deux intégrales est difficile, peut-on la remplacer par l'autre, plus simple ?

::: exemple Le produit x e^{2x}

1. On pose v(x) = x, qui se simplifie en dérivant (v′ = 1), et u′(x) = e^{2x}, de primitive u(x) = e^{2x}/2.
2. ∫₀¹ x e^{2x}dx = [x e^{2x}/2]₀¹ − ∫₀¹ (e^{2x}/2) × 1 dx, d'après la relation du début.
3. Le crochet vaut e²/2 − 0 = e²/2, et ∫₀¹ (e^{2x}/2)dx = [e^{2x}/4]₀¹ = (e² − 1)/4.
4. I = e²/2 − (e² − 1)/4 = (e² + 1)/4 ≈ 2,10.

:::

::: exemple Avec un logarithme

1. J = ∫₁ᵉ x³ ln x dx. On ne connaît pas de primitive de ln x dans le tableau, mais ln x se dérive en 1/x : v(x) = ln x et u′(x) = x³, de primitive u(x) = x⁴/4.
2. J = [x⁴ ln x/4]₁ᵉ − ∫₁ᵉ (x⁴/4)(1/x)dx = [x⁴ ln x/4]₁ᵉ − ∫₁ᵉ (x³/4)dx.
3. Le crochet vaut e⁴/4 − 0, car ln 1 = 0 ; et ∫₁ᵉ (x³/4)dx = [x⁴/16]₁ᵉ = (e⁴ − 1)/16.
4. J = e⁴/4 − (e⁴ − 1)/16 = (3e⁴ + 1)/16 ≈ 10,30.

:::

::: piege
**Erreur : écrire + au lieu de − devant la seconde intégrale.** Pour I, on écrit [x e^{2x}/2]₀¹ + ∫₀¹ (e^{2x}/2)dx = (3e² − 1)/4 ≈ 5,29. L'erreur tente parce que (uv)′ = u′v + uv′ contient un plus. Mais on a isolé l'intégrale cherchée : ∫ u′v = [uv] − ∫ uv′. Contrôle : x e^{2x} ≤ e^{2x} sur [0 ; 1], donc I ≤ (e² − 1)/2 ≈ 3,19, et 5,29 est impossible.
:::

::: propriete
Soit u et v dérivables sur un intervalle I, de dérivées u′ et v′ continues, a et b dans I :
∫ₐᵇ u′(x)v(x)dx = [u(x)v(x)]ₐᵇ − ∫ₐᵇ u(x)v′(x)dx
:::

::: methode Choisir u′ et v

1. v est le facteur qui se simplifie en dérivant (x, x², ln x) ; u′ est celui dont on connaît une primitive (e^{ax}, sin, cos, xⁿ).
2. Si un facteur xⁿ subsiste après une première fois, on recommence : ∫₀^{π/2} x² cos x dx = [x² sin x]₀^{π/2} − 2∫₀^{π/2} x sin x dx = π²/4 − 2 × 1 = π²/4 − 2.
3. Pour un ln x seul, on prend u′ = 1 et v = ln x : ∫₁ᵉ ln x dx = [x ln x]₁ᵉ − ∫₁ᵉ 1 dx = e − (e − 1) = 1.

:::

::: verifie À toi : le choix de v
Calculer ∫₀¹ (2x + 1)eˣ dx.

---

On pose v(x) = 2x + 1, qui se simplifie (v′ = 2), et u′(x) = eˣ, de primitive u(x) = eˣ. Alors l'intégrale vaut [(2x + 1)eˣ]₀¹ − ∫₀¹ 2eˣ dx = (3e − 1) − 2(e − 1) = e + 1.
:::

::: retenir
∫ₐᵇ u′v = [uv]ₐᵇ − ∫ₐᵇ uv′ : on dérive le facteur qui se simplifie, on primitive l'autre.
:::

## 📈 Une fonction définie par une intégrale

À partir de t = 1, on note V(x) le volume versé entre 1 et x : V(x) = ∫₁ˣ (2t + 1)dt. Le débit est la vitesse à laquelle le volume augmente.
Cette fonction V a-t-elle pour dérivée le débit, et est-ce vrai même quand on ne sait pas calculer l'intégrale ?

::: exemple Le volume depuis t = 1

1. Une primitive de 2t + 1 est F(t) = t² + t, donc V(x) = F(x) − F(1) = x² + x − 2.
2. V′(x) = 2x + 1 = q(x) : la constante F(1) = 2 disparaît en dérivant.
3. V(1) = 1 + 1 − 2 = 0 : V s'annule à la borne inférieure, puisque rien n'a été versé entre 1 et 1.

:::

::: piege
**Erreur : dériver ∫ₐˣ f(t)dt en f(x) − f(a).** Comme V(x) = F(x) − F(1), on écrit V′(x) = q(x) − q(1) = 2x + 1 − 3 = 2x − 2. L'erreur tente parce que la soustraction semble se reporter sur f. Mais F(1) est une constante, de dérivée 0 : V′(x) = F′(x) = q(x) = 2x + 1.
:::

::: propriete
Soit f continue sur un intervalle I et a dans I. La fonction F : x ↦ ∫ₐˣ f(t)dt est dérivable sur I et F′ = f : c'est la primitive de f sur I qui s'annule en a.
Cas limite : x et a doivent rester dans l'intervalle où f est continue. Pour f(t) = 1/t, ∫₁ˣ dt/t n'a de sens que pour x > 0.
:::

::: exemple Étudier une fonction sans la calculer

1. G(x) = ∫₀ˣ e^{−t²}dt. On ne sait pas primitiver e^{−t²}, mais t ↦ e^{−t²} est continue sur ℝ : G est la primitive qui s'annule en 0.
2. G′(x) = e^{−x²} > 0 pour tout réel x, donc G est strictement croissante sur ℝ.
3. G(0) = 0 : par croissance stricte, G(x) < 0 pour x < 0 et G(x) > 0 pour x > 0.

:::

::: verifie À toi : variations d'une fonction intégrale
Étudier le sens de variation et le signe de K(x) = ∫₁ˣ ((t² + 1)/t)dt sur ]0 ; +∞[.

---

La fonction t ↦ (t² + 1)/t est continue sur l'intervalle ]0 ; +∞[, donc K′(x) = (x² + 1)/x > 0 : K est strictement croissante. Comme K(1) = 0, K(x) < 0 sur ]0 ; 1[ et K(x) > 0 sur ]1 ; +∞[.
:::

::: retenir
x ↦ ∫ₐˣ f(t)dt est la primitive de f qui s'annule en a : sa dérivée est f(x).
:::

## 🗺️ Aire d'une partie du plan

Une parcelle est limitée par la courbe de f(x) = x³ − x, l'axe des abscisses et les droites x = −1 et x = 1, dans un repère orthogonal. La fonction f est impaire, donc ∫₋₁¹ f = 0. Une aire nulle ? La parcelle existe clairement.
Que mesure l'intégrale quand f change de signe, et comment calculer l'aire ?

::: figure La courbe de f entre −1 et 1 : la zone A₁ est au-dessus de l'axe des abscisses, la zone A₂ en dessous
<svg viewBox="0 0 340 230">
<title>La courbe de f(x) = x³ − x entre −1 et 1 : la zone A₁ est au-dessus de l'axe des abscisses, la zone A₂ en dessous</title>
<polygon points="76.25,111 77.81,106.8 79.38,102.8 80.94,99.02 82.5,95.44 84.06,92.06 85.62,88.88 87.19,85.9 88.75,83.1 90.31,80.49 91.88,78.07 93.44,75.82 95,73.75 96.56,71.85 98.12,70.13 99.69,68.56 101.25,67.16 102.81,65.92 104.38,64.83 105.94,63.89 107.5,63.1 109.06,62.45 110.63,61.94 112.19,61.57 113.75,61.34 115.31,61.23 116.88,61.24 118.44,61.38 120,61.64 121.56,62.02 123.12,62.5 124.69,63.09 126.25,63.79 127.81,64.59 129.38,65.48 130.94,66.47 132.5,67.54 134.06,68.71 135.62,69.95 137.19,71.28 138.75,72.68 140.31,74.15 141.88,75.69 143.44,77.3 145,78.96 146.56,80.69 148.12,82.47 149.69,84.29 151.25,86.17 152.81,88.09 154.38,90.04 155.94,92.04 157.5,94.06 159.06,96.12 160.62,98.2 162.19,100.3 163.75,102.42 165.31,104.55 166.88,106.69 168.44,108.85 170,111 170,111 168.44,111 166.88,111 165.31,111 163.75,111 162.19,111 160.62,111 159.06,111 157.5,111 155.94,111 154.38,111 152.81,111 151.25,111 149.69,111 148.12,111 146.56,111 145,111 143.44,111 141.88,111 140.31,111 138.75,111 137.19,111 135.62,111 134.06,111 132.5,111 130.94,111 129.38,111 127.81,111 126.25,111 124.69,111 123.12,111 121.56,111 120,111 118.44,111 116.88,111 115.31,111 113.75,111 112.19,111 110.63,111 109.06,111 107.5,111 105.94,111 104.38,111 102.81,111 101.25,111 99.69,111 98.12,111 96.56,111 95,111 93.44,111 91.88,111 90.31,111 88.75,111 87.19,111 85.62,111 84.06,111 82.5,111 80.94,111 79.38,111 77.81,111 76.25,111" fill="#0f6e56" fill-opacity="0.25" stroke="none" stroke-width="0"/>
<polygon points="170,111 171.56,111 173.13,111 174.69,111 176.25,111 177.81,111 179.38,111 180.94,111 182.5,111 184.06,111 185.62,111 187.19,111 188.75,111 190.31,111 191.88,111 193.44,111 195,111 196.56,111 198.12,111 199.69,111 201.25,111 202.81,111 204.38,111 205.94,111 207.5,111 209.06,111 210.62,111 212.19,111 213.75,111 215.31,111 216.88,111 218.44,111 220,111 221.56,111 223.12,111 224.69,111 226.25,111 227.81,111 229.38,111 230.94,111 232.5,111 234.06,111 235.62,111 237.19,111 238.75,111 240.31,111 241.87,111 243.44,111 245,111 246.56,111 248.13,111 249.69,111 251.25,111 252.81,111 254.38,111 255.94,111 257.5,111 259.06,111 260.62,111 262.19,111 263.75,111 263.75,111 262.19,115.2 260.62,119.2 259.06,122.98 257.5,126.56 255.94,129.94 254.38,133.12 252.81,136.1 251.25,138.9 249.69,141.51 248.13,143.93 246.56,146.18 245,148.25 243.44,150.15 241.87,151.87 240.31,153.44 238.75,154.84 237.19,156.08 235.62,157.17 234.06,158.11 232.5,158.9 230.94,159.55 229.38,160.06 227.81,160.43 226.25,160.66 224.69,160.77 223.12,160.76 221.56,160.62 220,160.36 218.44,159.98 216.88,159.5 215.31,158.91 213.75,158.21 212.19,157.41 210.62,156.52 209.06,155.53 207.5,154.46 205.94,153.29 204.38,152.05 202.81,150.72 201.25,149.32 199.69,147.85 198.12,146.31 196.56,144.7 195,143.04 193.44,141.31 191.88,139.53 190.31,137.71 188.75,135.83 187.19,133.91 185.62,131.96 184.06,129.96 182.5,127.94 180.94,125.88 179.38,123.8 177.81,121.7 176.25,119.58 174.69,117.45 173.13,115.31 171.56,113.15 170,111" fill="#d97706" fill-opacity="0.25" stroke="none" stroke-width="0"/>
<line x1="29.38" y1="111" x2="310.62" y2="111" stroke="#0f172a" stroke-width="1.6"/>
<line x1="170" y1="191.19" x2="170" y2="25.64" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="310.62,111 302.62,115 302.62,107" fill="#0f172a"/>
<polygon points="170,25.64 174,33.64 166,33.64" fill="#0f172a"/>
<line x1="76.25" y1="108" x2="76.25" y2="114" stroke="#0f172a" stroke-width="1.2"/>
<line x1="263.75" y1="108" x2="263.75" y2="114" stroke="#0f172a" stroke-width="1.2"/>
<polyline points="52.81,201.94 55.74,187.5 58.67,173.99 61.6,161.38 64.53,149.65 67.46,138.77 70.39,128.71 73.32,119.47 76.25,111 79.18,103.29 82.11,96.32 85.04,90.05 87.97,84.48 90.9,79.56 93.83,75.29 96.76,71.63 99.69,68.56 102.62,66.06 105.55,64.11 108.48,62.68 111.41,61.74 114.34,61.28 117.27,61.27 120.2,61.68 123.12,62.5 126.05,63.7 128.98,65.25 131.91,67.13 134.84,69.32 137.77,71.8 140.7,74.53 143.63,77.5 146.56,80.69 149.49,84.06 152.42,87.6 155.35,91.29 158.28,95.09 161.21,98.98 164.14,102.95 167.07,106.96 170,111 172.93,115.04 175.86,119.05 178.79,123.02 181.72,126.91 184.65,130.71 187.58,134.4 190.51,137.94 193.44,141.31 196.37,144.5 199.3,147.47 202.23,150.2 205.16,152.68 208.09,154.87 211.02,156.75 213.95,158.3 216.88,159.5 219.8,160.32 222.73,160.73 225.66,160.72 228.59,160.26 231.52,159.32 234.45,157.89 237.38,155.94 240.31,153.44 243.24,150.37 246.17,146.71 249.1,142.44 252.03,137.52 254.96,131.95 257.89,125.68 260.82,118.71 263.75,111 266.68,102.53 269.61,93.29 272.54,83.23 275.47,72.35 278.4,60.62 281.33,48.01 284.26,34.5 287.19,20.06" fill="none" stroke="#0f172a" stroke-width="2.8"/>
<g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="306.62" y="129" text-anchor="end" fill="#0f172a" font-size="12">x</text><text x="180" y="33.64" text-anchor="start" fill="#0f172a" font-size="12">y</text><text x="62.25" y="103" text-anchor="middle" fill="#0f172a" font-size="11">−1</text><text x="277.75" y="127" text-anchor="middle" fill="#0f172a" font-size="11">1</text><text x="115.62" y="95.48" text-anchor="middle" fill="#0f6e56" font-size="14">A₁</text><text x="224.38" y="130.52" text-anchor="middle" fill="#d97706" font-size="14">A₂</text><text x="217.19" y="14.06" text-anchor="start" fill="#0f172a" font-size="12">y = x³ − x</text></g>
</svg>
:::

Les zones A₁ et A₂ sont les deux morceaux de la parcelle, de part et d'autre de x = 0.

::: exemple L'aire de la parcelle

1. f(x) = x(x − 1)(x + 1) : f(−0,5) = 0,375 > 0 et f(0,5) = −0,375 < 0, donc f ≥ 0 sur [−1 ; 0] et f ≤ 0 sur [0 ; 1].
2. L'aire de A₁ est ∫₋₁⁰ f = [x⁴/4 − x²/2]₋₁⁰ = 0 − (1/4 − 1/2) = 1/4.
3. L'aire de A₂ est −∫₀¹ f, car f ≤ 0 : −[x⁴/4 − x²/2]₀¹ = −(1/4 − 1/2) = 1/4.
4. L'aire totale est 1/4 + 1/4 = 1/2 u.a, alors que ∫₋₁¹ f = 1/4 − 1/4 = 0.

:::

::: piege
**Erreur : répondre ∫₋₁¹ f = 0 pour l'aire.** On a retenu qu'une intégrale est une aire, et l'on conclut que l'aire de la parcelle est nulle. L'erreur tente parce que cela est vrai quand f ≥ 0. Mais l'intégrale compte A₂ négativement : 1/4 − 1/4 = 0. L'aire, elle, compte les deux morceaux positivement.
:::

::: propriete
Le repère est orthogonal (O, i⃗, j⃗) ; l'**unité d'aire** (u.a) est l'aire du rectangle de côtés ‖i⃗‖ et ‖j⃗‖. Soit f et g continues sur [a ; b], avec a < b.
L'aire de la partie limitée par C_f, l'axe des abscisses et les droites x = a et x = b est ∫ₐᵇ |f(x)|dx u.a : on coupe aux changements de signe, avec ∫ f là où f ≥ 0 et −∫ f là où f ≤ 0.
L'aire de la partie limitée par C_f, C_g et ces droites est ∫ₐᵇ |f(x) − g(x)|dx u.a ; si f ≤ g sur [a ; b], c'est ∫ₐᵇ (g − f).
Cas limite : avec ‖i⃗‖ = 2 cm et ‖j⃗‖ = 3 cm, 1 u.a = 6 cm².
:::

::: exemple Entre deux courbes

1. f(x) = eˣ et g(x) = x + 1 sur [−1 ; 1]. Soit h(x) = eˣ − x − 1 : h′(x) = eˣ − 1 s'annule en 0 et h(0) = 0 est le minimum, donc h ≥ 0 : C_f est au-dessus de C_g.
2. L'aire est ∫₋₁¹ (eˣ − x − 1)dx = [eˣ − x²/2 − x]₋₁¹.
3. En 1 : e − 1/2 − 1 = e − 3/2. En −1 : e⁻¹ − 1/2 + 1 = e⁻¹ + 1/2. La différence est e − e⁻¹ − 2 ≈ 0,35 u.a.
4. Avec ‖i⃗‖ = 2 cm et ‖j⃗‖ = 3 cm, 1 u.a = 6 cm² : l'aire vaut environ 2,1 cm².

:::

::: verifie À toi : une aire avec changement de signe
Calculer l'aire de la partie limitée par la courbe de f(x) = x² − 1, l'axe des abscisses et les droites x = 0 et x = 2.

---

f change de signe en 1 : f ≤ 0 sur [0 ; 1] et f ≥ 0 sur [1 ; 2]. L'aire est −∫₀¹ (x² − 1)dx + ∫₁² (x² − 1)dx = −(1/3 − 1) + (8/3 − 2 − (1/3 − 1)) = 2/3 + 4/3 = 2 u.a.
:::

::: retenir
L'aire se calcule avec |f| (ou |f − g|) : on étudie le signe, on coupe aux changements de signe, et chaque morceau compte positivement.
:::

## 🌀 Volume d'un solide de révolution

On fait tourner autour de l'axe (Ox) le segment d'équation y = x/3 pour 0 ≤ x ≤ 6. Il engendre un cône de hauteur 6 et de rayon de base f(6) = 2, de volume (1/3)π × 2² × 6 = 8π.
Peut-on retrouver ce nombre par une intégrale, pour mesurer aussi des solides dont le profil n'est pas une droite ?

::: figure Le segment y = x/3 tourne autour de (Ox) et engendre un cône ; la coupe d'abscisse x est un disque de rayon f(x)
<svg viewBox="0 0 340 230">
<title>Le segment y = x/3, de x = 0 à x = 6, tourne autour de l'axe des abscisses : il engendre un cône ; la coupe en x est un disque de rayon f(x)</title>
<polygon points="43.25,115 275.75,41.43 275.75,188.57" fill="#0f6e56" fill-opacity="0.14" stroke="none" stroke-width="0"/>
<polyline points="43.25,115 275.75,41.43" fill="none" stroke="#0f6e56" stroke-width="2.6"/>
<polyline points="43.25,115 275.75,188.57" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-dasharray="6 4"/>
<ellipse cx="275.75" cy="115" rx="11" ry="73.57" fill="#0f6e56" fill-opacity="0.1" stroke="#0f172a" stroke-width="2"/>
<ellipse cx="159.5" cy="115" rx="8" ry="36.79" fill="#d97706" fill-opacity="0.35" stroke="#d97706" stroke-width="2"/>
<line x1="27.75" y1="115" x2="322.25" y2="115" stroke="#0f172a" stroke-width="1.6"/>
<line x1="43.25" y1="210.64" x2="43.25" y2="19.36" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="322.25,115 314.25,119 314.25,111" fill="#0f172a"/>
<polygon points="43.25,19.36 47.25,27.36 39.25,27.36" fill="#0f172a"/>
<line x1="159.5" y1="112" x2="159.5" y2="118" stroke="#0f172a" stroke-width="1.2"/>
<line x1="275.75" y1="112" x2="275.75" y2="118" stroke="#0f172a" stroke-width="1.2"/>
<line x1="159.5" y1="115" x2="159.5" y2="78.21" stroke="#d97706" stroke-width="1.6"/>
<g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="318.25" y="133" text-anchor="end" fill="#0f172a" font-size="12">x</text><text x="53.25" y="27.36" text-anchor="start" fill="#0f172a" font-size="12">y</text><text x="159.5" y="133" text-anchor="middle" fill="#0f172a" font-size="11">x</text><text x="275.75" y="133" text-anchor="middle" fill="#0f172a" font-size="11">6</text><text x="155.5" y="66.21" text-anchor="end" fill="#d97706" font-size="12">f(x)</text><text x="97.25" y="75.41" text-anchor="end" fill="#0f6e56" font-size="12">y = x/3</text></g>
</svg>
:::

La coupe orange est le disque de rayon f(x) = x/3 : son aire π(f(x))² est l'intégrande de la formule qui suit.

::: exemple Retrouver le cône

1. La coupe par un plan perpendiculaire à (Ox) au point d'abscisse x est un disque de rayon x/3, d'aire π(x/3)² = πx²/9.
2. Le volume est la somme de ces disques de 0 à 6 : V = π∫₀⁶ (x/3)² dx = π∫₀⁶ (x²/9)dx.
3. V = π[x³/27]₀⁶ = π × 216/27 = 8π : on retrouve la formule du cône.

:::

::: exemple Un solide sans formule de géométrie

1. On fait tourner l'arc de la courbe y = eˣ pour 0 ≤ x ≤ 1. On a (f(x))² = e^{2x}.
2. V = π∫₀¹ e^{2x}dx = π[e^{2x}/2]₀¹, car (e^{2x}/2)′ = e^{2x}.
3. V = π(e² − 1)/2 ≈ 10,04 u.v.

:::

::: piege
**Erreur : élever l'intégrale au carré au lieu d'intégrer le carré.** Pour le cône, on écrit π(∫₀⁶ (x/3)dx)² = π × 6² = 36π. L'erreur tente parce que la formule contient un carré et un symbole d'intégrale, et que l'on place le carré à l'extérieur. Le carré porte sur f(x) avant d'intégrer : on obtient 8π, la valeur du cône.
:::

::: propriete
**Théorème admis.** Soit f continue sur [a ; b], avec a < b, dans un repère orthonormé. Le volume du solide engendré par la rotation autour de (Ox) de la partie limitée par C_f, (Ox) et les droites x = a et x = b est V = π∫ₐᵇ (f(x))²dx, en unités de volume (u.v).
Cas limite : si f est négative, (f(x))² reste positif et la formule ne change pas : l'arc y = −x/3 engendre le même cône.
:::

::: verifie À toi : le carré de x²
Calculer le volume engendré par la rotation autour de (Ox) de l'arc de la courbe y = x² pour 0 ≤ x ≤ 1.

---

Le carré de f(x) = x² est x⁴. V = π∫₀¹ x⁴ dx = π[x⁵/5]₀¹ = π/5 u.v.
:::

::: retenir
V = π∫ₐᵇ (f(x))²dx : on additionne les aires π(f(x))² des disques, le carré est sous l'intégrale.
:::

> 🏆 Les huit portes sont franchies : tu sais définir et calculer une intégrale, la couper, exploiter les symétries, l'encadrer et la moyenner, intégrer par parties, dériver une fonction intégrale, mesurer des aires et des volumes. Prochaine étape : les suites réelles.
