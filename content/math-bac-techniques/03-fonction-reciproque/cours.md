# ⚔️ Fonction réciproque — refaire le chemin à l'envers

> 💡 «Une fonction t'emmène de x vers y ; sa réciproque te ramène de y vers x. Reste à savoir quand ce retour est possible, et comment il se comporte.»

Le chapitre précédent mesurait la pente d'une courbe. Celui-ci pose le problème inverse : connaissant la valeur y, retrouver le x qui l'a produite, et dire comment cette fonction « retour » varie, où elle est dérivable et à quoi ressemble sa courbe. Sept notions, dans l'ordre où elles s'appellent, avec un fil rouge : une balle lancée vers le haut, à la hauteur h(t) = −5t² + 20t mètres, t secondes après le lancer.

## 🎯 Restriction d'une fonction

On lit sur la formule h(1) = 15 et h(3) = 15 : la balle passe deux fois à 15 m, à la montée puis à la descente. Pour parler de « la date où la balle atteint 15 m », on voudrait une seule réponse.
Comment ne garder que la montée sans changer la formule ?

::: definition
Soit f définie sur D et I une partie de D. La **restriction de f à I** est la fonction g définie sur I par g(x) = f(x) pour tout x de I. Sa courbe est la partie de la courbe de f formée des points dont l'abscisse est dans I.
:::

::: figure La parabole de h sur ℝ, et en orange l'arc de t = 0 à t = 2 : la courbe de la restriction g de h à [0 ; 2]
<svg viewBox="0 0 340 252">
<title>Parabole de h(t) = −5t² + 20t sur ℝ, avec en orange l'arc t de 0 à 2 : la restriction g</title>
<line x1="40" y1="142.8" x2="331.2" y2="142.8" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="331.2,142.8 323.2,146.8 323.2,138.8" fill="#0f172a"/>
<line x1="73.6" y1="215.6" x2="73.6" y2="18" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="73.6,18 77.6,26 69.6,26" fill="#0f172a"/>
<line x1="129.6" y1="139.8" x2="129.6" y2="145.8" stroke="#0f172a" stroke-width="1.2"/>
<line x1="185.6" y1="139.8" x2="185.6" y2="145.8" stroke="#0f172a" stroke-width="1.2"/>
<line x1="241.6" y1="139.8" x2="241.6" y2="145.8" stroke="#0f172a" stroke-width="1.2"/>
<line x1="297.6" y1="139.8" x2="297.6" y2="145.8" stroke="#0f172a" stroke-width="1.2"/>
<line x1="70.6" y1="194.8" x2="76.6" y2="194.8" stroke="#0f172a" stroke-width="1.2"/>
<line x1="70.6" y1="90.8" x2="76.6" y2="90.8" stroke="#0f172a" stroke-width="1.2"/>
<line x1="70.6" y1="38.8" x2="76.6" y2="38.8" stroke="#0f172a" stroke-width="1.2"/>
<polyline points="40,214.56 41.82,210.19 43.64,205.88 45.46,201.63 47.28,197.42 49.1,193.28 50.92,189.18 52.74,185.15 54.56,181.17 56.38,177.24 58.2,173.37 60.02,169.55 61.84,165.79 63.66,162.08 65.48,158.43 67.3,154.83 69.12,151.29 70.94,147.8 72.76,144.37 74.58,140.99 76.4,137.67 78.22,134.4 80.04,131.18 81.86,128.03 83.68,124.92 85.5,121.87 87.32,118.88 89.14,115.94 90.96,113.06 92.78,110.23 94.6,107.46 96.42,104.74 98.24,102.07 100.06,99.46 101.88,96.91 103.7,94.41 105.52,91.97 107.34,89.58 109.16,87.24 110.98,84.96 112.8,82.74 114.62,80.57 116.44,78.46 118.26,76.4 120.08,74.39 121.9,72.44 123.72,70.55 125.54,68.71 127.36,66.92 129.18,65.19 131,63.52 132.82,61.9 134.64,60.33 136.46,58.82 138.28,57.36 140.1,55.96 141.92,54.62 143.74,53.33 145.56,52.09 147.38,50.91 149.2,49.79 151.02,48.71 152.84,47.7 154.66,46.74 156.48,45.83 158.3,44.98 160.12,44.18 161.94,43.44 163.76,42.75 165.58,42.12 167.4,41.55 169.22,41.02 171.04,40.56 172.86,40.15 174.68,39.79 176.5,39.49 178.32,39.24 180.14,39.05 181.96,38.91 183.78,38.83 185.6,38.8 187.42,38.83 189.24,38.91 191.06,39.05 192.88,39.24 194.7,39.49 196.52,39.79 198.34,40.15 200.16,40.56 201.98,41.02 203.8,41.55 205.62,42.12 207.44,42.75 209.26,43.44 211.08,44.18 212.9,44.98 214.72,45.83 216.54,46.74 218.36,47.7 220.18,48.71 222,49.78 223.82,50.91 225.64,52.09 227.46,53.33 229.28,54.62 231.1,55.96 232.92,57.36 234.74,58.82 236.56,60.33 238.38,61.9 240.2,63.52 242.02,65.19 243.84,66.92 245.66,68.71 247.48,70.55 249.3,72.44 251.12,74.39 252.94,76.4 254.76,78.46 256.58,80.57 258.4,82.74 260.22,84.96 262.04,87.24 263.86,89.58 265.68,91.97 267.5,94.41 269.32,96.91 271.14,99.46 272.96,102.07 274.78,104.74 276.6,107.46 278.42,110.23 280.24,113.06 282.06,115.94 283.88,118.88 285.7,121.87 287.52,124.92 289.34,128.03 291.16,131.18 292.98,134.4 294.8,137.66 296.62,140.99 298.44,144.37 300.26,147.8 302.08,151.29 303.9,154.83 305.72,158.43 307.54,162.08 309.36,165.79 311.18,169.55 313,173.37 314.82,177.24 316.64,181.17 318.46,185.15 320.28,189.18 322.1,193.28 323.92,197.42 325.74,201.63 327.56,205.88 329.38,210.19 331.2,214.56" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round"/>
<polyline points="73.6,142.8 75.47,139.36 77.33,135.98 79.2,132.66 81.07,129.4 82.93,126.19 84.8,123.04 86.67,119.95 88.53,116.92 90.4,113.94 92.27,111.02 94.13,108.16 96,105.36 97.87,102.62 99.73,99.93 101.6,97.3 103.47,94.73 105.33,92.22 107.2,89.76 109.07,87.36 110.93,85.02 112.8,82.74 114.67,80.52 116.53,78.35 118.4,76.24 120.27,74.19 122.13,72.2 124,70.26 125.87,68.38 127.73,66.56 129.6,64.8 131.47,63.1 133.33,61.45 135.2,59.86 137.07,58.33 138.93,56.86 140.8,55.44 142.67,54.08 144.53,52.78 146.4,51.54 148.27,50.36 150.13,49.23 152,48.16 153.87,47.15 155.73,46.2 157.6,45.3 159.47,44.46 161.33,43.68 163.2,42.96 165.07,42.3 166.93,41.69 168.8,41.14 170.67,40.65 172.53,40.22 174.4,39.84 176.27,39.52 178.13,39.26 180,39.06 181.87,38.92 183.73,38.83 185.6,38.8" fill="none" stroke="#d97706" stroke-width="5" stroke-linejoin="round"/>
<line x1="185.6" y1="38.8" x2="185.6" y2="142.8" stroke="#64748b" stroke-width="1.4" stroke-dasharray="5 4"/>
<circle cx="73.6" cy="142.8" r="4" fill="#0f172a" stroke="#ffffff" stroke-width="1.2"/>
<circle cx="185.6" cy="38.8" r="4" fill="#0f172a" stroke="#ffffff" stroke-width="1.2"/>
<g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="129.6" y="157.8" text-anchor="middle" fill="#0f172a" font-size="10">1</text><text x="185.6" y="157.8" text-anchor="middle" fill="#0f172a" font-size="10">2</text><text x="241.6" y="157.8" text-anchor="middle" fill="#0f172a" font-size="10">3</text><text x="297.6" y="157.8" text-anchor="middle" fill="#0f172a" font-size="10">4</text><text x="66.6" y="198.3" text-anchor="end" fill="#0f172a" font-size="10">-10</text><text x="66.6" y="94.3" text-anchor="end" fill="#0f172a" font-size="10">10</text><text x="66.6" y="42.3" text-anchor="end" fill="#0f172a" font-size="10">20</text><text x="329.2" y="158.8" text-anchor="end" fill="#0f172a" font-size="12">t</text><text x="81.6" y="26" text-anchor="start" fill="#0f172a" font-size="12">h</text><text x="192.32" y="29.44" text-anchor="start" fill="#0f172a" font-size="11">(2 ; 20)</text><text x="272.4" y="77.8" text-anchor="start" fill="#0f6e56" font-size="12">C_h sur ℝ</text><text x="118.4" y="119.4" text-anchor="start" fill="#d97706" font-size="12">restriction g</text></g>
</svg>
:::

L'arc orange est formé des points de la parabole d'abscisse t entre 0 et 2 : c'est la montée de la balle, du sol (0 ; 0) au sommet (2 ; 20).

::: exemple La montée de la balle

1. h(t) = −5t² + 20t = −5(t − 2)² + 20, car −5(t² − 4t + 4) + 20 = −5t² + 20t : le sommet de la parabole est (2 ; 20).
2. La dérivée h′(t) = −10t + 20 = 10(2 − t) est positive pour t ≤ 2 et négative pour t ≥ 2 : h monte puis redescend, elle n'est donc pas monotone sur ℝ.
3. On restreint à I = [0 ; 2] : g(t) = −5t² + 20t pour t de [0 ; 2]. Sur ]0 ; 2[, g′(t) = 10(2 − t) > 0, donc g est strictement croissante sur [0 ; 2].
4. g(0) = 0 et g(2) = 20 : sur cet intervalle, la balle monte de 0 m à 20 m.

:::

::: piege
**Erreur : croire qu'une restriction est « la même fonction » parce qu'elle a la même formule.** On a h(1) = h(3) = 15, donc sur ℝ la valeur 15 a deux antécédents. La restriction g, elle, n'est pas définie en 3 : elle ne prend la valeur 15 qu'en t = 1. L'erreur tente parce que la formule ne change pas. Mais le domaine change, et avec lui le sens de variation et le nombre d'antécédents : g et h sont deux fonctions différentes.
:::

::: propriete
Une fonction qui n'est pas monotone sur D l'est souvent sur une restriction bien choisie : on coupe D aux points où le sens de variation change (ici t = 2). On choisit aussi une restriction pour faire disparaître une valeur absolue.
Cas limite : un point où la dérivée s'annule (le sommet t = 2) peut être une borne de l'intervalle sans gêner la stricte monotonie de la restriction.
:::

::: exemple Le même outil, sans situation : une valeur absolue

1. Soit q(x) = |2x − 4| + x. Pour x ≤ 2, 2x − 4 ≤ 0, donc |2x − 4| = −(2x − 4) = 4 − 2x, par définition de la valeur absolue.
2. La restriction de q à ]−∞ ; 2] est donc x ↦ 4 − 2x + x = 4 − x, affine de pente −1 : strictement décroissante.
3. Pour x ≥ 2, |2x − 4| = 2x − 4 et la restriction de q à [2 ; +∞[ est x ↦ 3x − 4, strictement croissante.

:::

::: verifie À toi : la descente de la balle
Quelle restriction de h décrit la descente de la balle, du sommet jusqu'au sol, et entre quelles hauteurs la balle y évolue-t-elle ?

---

La descente est la restriction de h à [2 ; 4]. Sur cet intervalle, h′(t) = 10(2 − t) ≤ 0, avec h′(t) < 0 sur ]2 ; 4[ : h y est strictement décroissante. Elle part de h(2) = 20 et arrive à h(4) = −80 + 80 = 0 : la balle redescend de 20 m à 0 m.
:::

::: retenir
La restriction de f à I garde la formule de f mais sur une partie I du domaine ; on choisit I là où f est strictement monotone.
:::

## 📏 Image d'un intervalle par une fonction continue et strictement monotone

Entre t = 0 et t = 2, la balle passe de 0 m à 20 m. A-t-elle traversé toutes les hauteurs intermédiaires, par exemple 7,3 m, et aucune autre ? Et quelles hauteurs atteint-elle entre t = 0 et t = 1 exclu ?
On cherche l'**image** f(I) = {f(x) ; x ∈ I} de chaque intervalle I.

::: figure La courbe de g sur [0 ; 2] : quand t décrit l'intervalle orange I = [0 ; 2], la hauteur décrit tout l'intervalle bleu g(I) = [0 ; 20]
<svg viewBox="0 0 340 272">
<title>Courbe de g(t) = −5t² + 20t sur [0 ; 2] : l'image de [0 ; 2] est [0 ; 20]</title>
<line x1="26" y1="225.2" x2="334" y2="225.2" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="334,225.2 326,229.2 326,221.2" fill="#0f172a"/>
<line x1="59" y1="251.6" x2="59" y2="14" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="59,14 63,22 55,22" fill="#0f172a"/>
<line x1="169" y1="222.2" x2="169" y2="228.2" stroke="#0f172a" stroke-width="1.2"/>
<line x1="279" y1="222.2" x2="279" y2="228.2" stroke="#0f172a" stroke-width="1.2"/>
<line x1="56" y1="181.2" x2="62" y2="181.2" stroke="#0f172a" stroke-width="1.2"/>
<line x1="56" y1="137.2" x2="62" y2="137.2" stroke="#0f172a" stroke-width="1.2"/>
<line x1="56" y1="93.2" x2="62" y2="93.2" stroke="#0f172a" stroke-width="1.2"/>
<line x1="56" y1="49.2" x2="62" y2="49.2" stroke="#0f172a" stroke-width="1.2"/>
<polyline points="59,225.2 60.38,223.01 61.75,220.83 63.12,218.66 64.5,216.51 65.88,214.37 67.25,212.25 68.62,210.14 70,208.04 71.38,205.96 72.75,203.89 74.12,201.83 75.5,199.79 76.88,197.76 78.25,195.75 79.62,193.75 81,191.76 82.38,189.79 83.75,187.83 85.12,185.88 86.5,183.95 87.88,182.03 89.25,180.13 90.62,178.24 92,176.36 93.38,174.5 94.75,172.65 96.12,170.81 97.5,168.99 98.88,167.18 100.25,165.39 101.62,163.61 103,161.84 104.37,160.09 105.75,158.35 107.12,156.62 108.5,154.91 109.88,153.21 111.25,151.53 112.62,149.86 114,148.2 115.38,146.56 116.75,144.93 118.12,143.31 119.5,141.71 120.88,140.12 122.25,138.55 123.62,136.99 125,135.44 126.38,133.91 127.75,132.39 129.12,130.88 130.5,129.39 131.88,127.91 133.25,126.45 134.62,125 136,123.56 137.38,122.14 138.75,120.73 140.12,119.33 141.5,117.95 142.88,116.58 144.25,115.23 145.62,113.89 147,112.56 148.38,111.25 149.75,109.95 151.12,108.66 152.5,107.39 153.88,106.13 155.25,104.89 156.62,103.66 158,102.44 159.38,101.24 160.75,100.05 162.12,98.87 163.5,97.71 164.88,96.56 166.25,95.43 167.62,94.31 169,93.2 170.38,92.11 171.75,91.03 173.13,89.96 174.5,88.91 175.88,87.87 177.25,86.85 178.62,85.84 180,84.84 181.38,83.86 182.75,82.89 184.12,81.93 185.5,80.99 186.88,80.06 188.25,79.15 189.62,78.25 191,77.36 192.38,76.49 193.75,75.63 195.12,74.78 196.5,73.95 197.88,73.13 199.25,72.33 200.63,71.54 202,70.76 203.38,70 204.75,69.25 206.12,68.51 207.5,67.79 208.88,67.08 210.25,66.39 211.62,65.71 213,65.04 214.38,64.39 215.75,63.75 217.12,63.12 218.5,62.51 219.88,61.91 221.25,61.33 222.62,60.76 224,60.2 225.38,59.66 226.75,59.13 228.13,58.61 229.5,58.11 230.88,57.62 232.25,57.15 233.62,56.69 235,56.24 236.38,55.81 237.75,55.39 239.12,54.98 240.5,54.59 241.88,54.21 243.25,53.85 244.62,53.5 246,53.16 247.37,52.84 248.75,52.53 250.12,52.23 251.5,51.95 252.88,51.68 254.25,51.43 255.62,51.19 257,50.96 258.38,50.75 259.75,50.55 261.12,50.36 262.5,50.19 263.88,50.03 265.25,49.89 266.62,49.76 268,49.64 269.38,49.54 270.75,49.45 272.12,49.37 273.5,49.31 274.88,49.26 276.25,49.23 277.62,49.21 279,49.2" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round"/>
<line x1="279" y1="49.2" x2="279" y2="225.2" stroke="#64748b" stroke-width="1.4" stroke-dasharray="5 4"/>
<line x1="279" y1="49.2" x2="59" y2="49.2" stroke="#64748b" stroke-width="1.4" stroke-dasharray="5 4"/>
<line x1="59" y1="225.2" x2="279" y2="225.2" stroke="#d97706" stroke-width="5"/>
<line x1="59" y1="225.2" x2="59" y2="49.2" stroke="#2563eb" stroke-width="5"/>
<circle cx="59" cy="225.2" r="4.2" fill="#d97706" stroke="#ffffff" stroke-width="1.2"/>
<circle cx="279" cy="225.2" r="4.2" fill="#d97706" stroke="#ffffff" stroke-width="1.2"/>
<circle cx="59" cy="49.2" r="4.2" fill="#2563eb" stroke="#ffffff" stroke-width="1.2"/>
<circle cx="279" cy="49.2" r="3.8" fill="#0f172a" stroke="#ffffff" stroke-width="1.2"/>
<g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="169" y="240.2" text-anchor="middle" fill="#0f172a" font-size="10">1</text><text x="279" y="240.2" text-anchor="middle" fill="#0f172a" font-size="10">2</text><text x="47" y="184.7" text-anchor="end" fill="#0f172a" font-size="10">5</text><text x="47" y="140.7" text-anchor="end" fill="#0f172a" font-size="10">10</text><text x="47" y="96.7" text-anchor="end" fill="#0f172a" font-size="10">15</text><text x="47" y="52.7" text-anchor="end" fill="#0f172a" font-size="10">20</text><text x="332" y="241.2" text-anchor="end" fill="#0f172a" font-size="12">t</text><text x="67" y="22" text-anchor="start" fill="#0f172a" font-size="12">g</text><text x="169" y="202.32" text-anchor="middle" fill="#d97706" font-size="12">I</text><text x="28.2" y="124" text-anchor="start" fill="#2563eb" font-size="12">g(I)</text><text x="290" y="36" text-anchor="start" fill="#0f172a" font-size="11">(2 ; 20)</text></g>
</svg>
:::

Les deux extrémités de I sont des abscisses atteintes (points pleins sur l'axe des t) ; leurs images 0 et 20 sont les extrémités de g(I) sur l'axe des hauteurs. La continuité de g empêche tout saut : aucune hauteur intermédiaire n'est sautée.

::: exemple Les hauteurs atteintes par la balle

1. g est continue (polynôme) et strictement croissante sur [0 ; 2] : le résultat s'applique à tout intervalle contenu dans [0 ; 2].
2. Pour I = [0 ; 2], les deux extrémités sont dans I, donc g(I) = [g(0) ; g(2)] = [0 ; 20], fermé des deux côtés.
3. Pour [0 ; 1[, l'extrémité 1 n'est pas dans l'intervalle, donc g([0 ; 1[) = [g(0) ; g(1)[ = [0 ; 15[, avec g(1) = −5 + 20 = 15 non atteint.
4. L'image de [0 ; 2] est un intervalle : la balle est donc bien passée par 7,3 m, et par toute hauteur de [0 ; 20], sans jamais dépasser 20 m.

:::

::: piege
**Erreur : lire l'image « de borne à borne » sans vérifier la monotonie.** Pour h sur [0 ; 3], h(0) = 0 et h(3) = 15 donneraient « [0 ; 15] ». C'est faux : la balle atteint 20 m en t = 2, qui est dans [0 ; 3], donc h([0 ; 3]) = [0 ; 20]. L'erreur tente parce que, sur [0 ; 2], la lecture borne à borne réussit. Mais h n'est pas monotone sur [0 ; 3] : la règle ne s'applique pas.
:::

::: propriete
Soit f continue et strictement monotone sur un intervalle I d'extrémités a et b. Alors f(I) est un intervalle dont les extrémités sont les valeurs de f, ou ses limites, en a et en b, rangées dans le sens de la monotonie (voir le tableau ci-dessous).
Cas limite : a peut valoir −∞ et b peut valoir +∞ (la « valeur » est alors la limite en l'infini). Un crochet est fermé seulement si l'extrémité appartient à I : une limite n'est jamais atteinte, son crochet reste ouvert.
:::

| I | f strictement croissante | f strictement décroissante |
| --- | --- | --- |
| [a ; b] | [f(a) ; f(b)] | [f(b) ; f(a)] |
| ]a ; b] | ]lim x→a⁺ f(x) ; f(b)] | [f(b) ; lim x→a⁺ f(x)[ |
| [a ; b[ | [f(a) ; lim x→b⁻ f(x)[ | ]lim x→b⁻ f(x) ; f(a)] |
| ]a ; b[ | ]lim x→a⁺ f(x) ; lim x→b⁻ f(x)[ | ]lim x→b⁻ f(x) ; lim x→a⁺ f(x)[ |

Pour une fonction croissante, les extrémités de l'image sont rangées dans le même ordre que celles de I ; pour une fonction décroissante, dans l'ordre inverse, et chaque crochet suit celui de l'extrémité de I dont il provient.

::: figure La courbe de x ↦ 1/(x − 1) : quand x décrit I = ]1 ; 3] (orange), la valeur décroît de +∞ à 1/2 : l'image est [1/2 ; +∞[ (bleu)
<svg viewBox="0 0 340 262">
<title>Courbe de x ↦ 1/(x − 1) : l'image de ]1 ; 3] est [1/2 ; +∞[</title>
<line x1="30" y1="207.6" x2="330" y2="207.6" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="330,207.6 322,211.6 322,203.6" fill="#0f172a"/>
<line x1="60" y1="242.8" x2="60" y2="14" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="60,14 64,22 56,22" fill="#0f172a"/>
<line x1="160" y1="204.6" x2="160" y2="210.6" stroke="#0f172a" stroke-width="1.2"/>
<line x1="260" y1="204.6" x2="260" y2="210.6" stroke="#0f172a" stroke-width="1.2"/>
<line x1="310" y1="204.6" x2="310" y2="210.6" stroke="#0f172a" stroke-width="1.2"/>
<line x1="57" y1="163.6" x2="63" y2="163.6" stroke="#0f172a" stroke-width="1.2"/>
<line x1="57" y1="119.6" x2="63" y2="119.6" stroke="#0f172a" stroke-width="1.2"/>
<line x1="57" y1="75.6" x2="63" y2="75.6" stroke="#0f172a" stroke-width="1.2"/>
<line x1="57" y1="31.6" x2="63" y2="31.6" stroke="#0f172a" stroke-width="1.2"/>
<line x1="110" y1="242.8" x2="110" y2="14" stroke="#64748b" stroke-width="1.4" stroke-dasharray="6 4"/>
<polyline points="121.4,14.62 122.7,34.42 124.01,50.54 125.31,63.91 126.62,75.19 127.92,84.82 129.22,93.15 130.53,100.42 131.83,106.82 133.13,112.5 134.44,117.57 135.74,122.13 137.05,126.25 138.35,130 139.65,133.41 140.96,136.53 142.26,139.4 143.56,142.05 144.87,144.5 146.17,146.78 147.47,148.89 148.78,150.87 150.08,152.71 151.39,154.44 152.69,156.07 153.99,157.59 155.3,159.03 156.6,160.39 157.91,161.68 159.21,162.89 160.51,164.05 161.82,165.14 163.12,166.18 164.42,167.18 165.73,168.12 167.03,169.02 168.34,169.89 169.64,170.71 170.94,171.5 172.25,172.26 173.55,172.98 174.85,173.68 176.16,174.35 177.46,174.99 178.77,175.61 180.07,176.2 181.37,176.78 182.68,177.33 183.98,177.86 185.28,178.38 186.59,178.87 187.89,179.36 189.19,179.82 190.5,180.27 191.8,180.71 193.11,181.13 194.41,181.54 195.71,181.93 197.02,182.32 198.32,182.69 199.63,183.05 200.93,183.41 202.23,183.75 203.54,184.08 204.84,184.4 206.14,184.72 207.45,185.02 208.75,185.32 210.06,185.61 211.36,185.89 212.66,186.17 213.97,186.44 215.27,186.7 216.57,186.96 217.88,187.21 219.18,187.45 220.49,187.69 221.79,187.92 223.09,188.15 224.4,188.37 225.7,188.59 227,188.8 228.31,189 229.61,189.21 230.91,189.41 232.22,189.6 233.52,189.79 234.83,189.98 236.13,190.16 237.43,190.34 238.74,190.51 240.04,190.68 241.34,190.85 242.65,191.01 243.95,191.18 245.26,191.33 246.56,191.49 247.86,191.64 249.17,191.79 250.47,191.94 251.78,192.08 253.08,192.22 254.38,192.36 255.69,192.5 256.99,192.63 258.29,192.76 259.6,192.89 260.9,193.02 262.2,193.15 263.51,193.27 264.81,193.39 266.12,193.51 267.42,193.62 268.72,193.74 270.03,193.85 271.33,193.96 272.63,194.07 273.94,194.18 275.24,194.29 276.55,194.39 277.85,194.49 279.15,194.59 280.46,194.69 281.76,194.79 283.06,194.89 284.37,194.98 285.67,195.08 286.98,195.17 288.28,195.26 289.58,195.35 290.89,195.44 292.19,195.52 293.5,195.61 294.8,195.7 296.1,195.78 297.41,195.86 298.71,195.94 300.01,196.02 301.32,196.1 302.62,196.18 303.92,196.26 305.23,196.33 306.53,196.41 307.84,196.48 309.14,196.55 310.44,196.62 311.75,196.7 313.05,196.77 314.36,196.83 315.66,196.9 316.96,196.97 318.27,197.04 319.57,197.1 320.87,197.17 322.18,197.23 323.48,197.29 324.78,197.36 326.09,197.42 327.39,197.48 328.7,197.54 330,197.6" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round"/>
<line x1="110" y1="207.6" x2="210" y2="207.6" stroke="#d97706" stroke-width="5"/>
<circle cx="110" cy="207.6" r="4.2" fill="#ffffff" stroke="#0f172a" stroke-width="1.8"/>
<circle cx="210" cy="207.6" r="4.2" fill="#d97706" stroke="#ffffff" stroke-width="1.2"/>
<line x1="60" y1="185.6" x2="60" y2="18.4" stroke="#2563eb" stroke-width="5"/>
<polygon points="60,14 64.5,23 55.5,23" fill="#2563eb"/>
<circle cx="60" cy="185.6" r="4.2" fill="#2563eb" stroke="#ffffff" stroke-width="1.2"/>
<line x1="210" y1="207.6" x2="210" y2="185.6" stroke="#64748b" stroke-width="1.4" stroke-dasharray="5 4"/>
<line x1="210" y1="185.6" x2="60" y2="185.6" stroke="#64748b" stroke-width="1.4" stroke-dasharray="5 4"/>
<circle cx="210" cy="185.6" r="3.6" fill="#0f172a" stroke="#ffffff" stroke-width="1.2"/>
<g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="160" y="222.6" text-anchor="middle" fill="#0f172a" font-size="10">2</text><text x="260" y="222.6" text-anchor="middle" fill="#0f172a" font-size="10">4</text><text x="310" y="222.6" text-anchor="middle" fill="#0f172a" font-size="10">5</text><text x="48" y="167.1" text-anchor="end" fill="#0f172a" font-size="10">1</text><text x="48" y="123.1" text-anchor="end" fill="#0f172a" font-size="10">2</text><text x="48" y="79.1" text-anchor="end" fill="#0f172a" font-size="10">3</text><text x="48" y="35.1" text-anchor="end" fill="#0f172a" font-size="10">4</text><text x="328" y="223.6" text-anchor="end" fill="#0f172a" font-size="12">x</text><text x="68" y="22" text-anchor="start" fill="#0f172a" font-size="12">y</text><text x="110" y="231.8" text-anchor="middle" fill="#d97706" font-size="11">1</text><text x="210" y="231.8" text-anchor="middle" fill="#d97706" font-size="11">3</text><text x="54" y="185.6" text-anchor="end" fill="#2563eb" font-size="11">1/2</text><text x="114" y="31.6" text-anchor="start" fill="#64748b" font-size="11">x = 1</text><text x="255" y="139.4" text-anchor="start" fill="#0f6e56" font-size="13">C_φ</text><text x="54" y="31.6" text-anchor="end" fill="#2563eb" font-size="11">image</text></g>
</svg>
:::

Le point creux en 1 (non atteint) correspond à +∞ sur l'axe des y ; le point plein en 3 correspond au point plein 1/2 = φ(3), valeur atteinte.

::: exemple Le même outil, sans situation : une limite infinie

1. Soit φ(x) = 1/(x − 1) sur ]1 ; +∞[. φ est continue (quotient dont le dénominateur ne s'annule pas) et φ′(x) = −1/(x − 1)² < 0 : φ est strictement décroissante.
2. lim x→1⁺ φ(x) = +∞ (dénominateur positif tendant vers 0) et lim x→+∞ φ(x) = 0.
3. Cas ]a ; b[ décroissant : φ(]1 ; +∞[) = ]0 ; +∞[. La valeur 0 est une limite jamais atteinte : crochet ouvert.
4. Pour ]1 ; 3] : φ(]1 ; 3]) = [φ(3) ; lim x→1⁺ φ(x)[ = [1/2 ; +∞[. Le crochet est fermé en 1/2, valeur atteinte en x = 3.

:::

::: verifie À toi : une fonction croissante
Soit ψ(x) = 5 − 4/x sur ]0 ; +∞[. Détermine l'image de [2 ; +∞[ par ψ.

---

ψ′(x) = 4/x² > 0 : ψ est continue et strictement croissante. En 2, la valeur est ψ(2) = 5 − 2 = 3, atteinte car 2 est dans l'intervalle : crochet fermé. En +∞, la limite est 5, jamais atteinte : crochet ouvert. Pour [a ; +∞[ croissant, l'image est [ψ(2) ; lim ψ[ = [3 ; 5[.
:::

::: retenir
Si f est continue et strictement monotone sur I, f(I) est l'intervalle dont les extrémités sont les valeurs ou limites de f aux extrémités de I, rangées dans le sens de la monotonie ; un crochet est fermé seulement si la valeur est atteinte.
:::

## 🔄 Bijection et fonction réciproque

Retour à la balle, mais dans l'autre sens : à quel instant de la montée est-elle à 15 m ? à 20 m ? à 8,75 m ? Pour chaque hauteur y de [0 ; 20], on cherche l'unique date t de [0 ; 2] telle que g(t) = y.
Cette correspondance y ↦ t est-elle une fonction, et laquelle ?

::: definition
Soit f définie sur un intervalle I et J = f(I). f est une **bijection de I sur J** si tout réel y de J a **un seul antécédent** dans I. La fonction qui à y associe cet antécédent est la **fonction réciproque** de f, notée f⁻¹, définie sur J. Pour x dans I et y dans J :
$$ y = f(x) ⟺ x = f⁻¹(y) $$
:::

| t (en s) | 0 | 0,5 | 1 | 1,5 | 2 |
| --- | --- | --- | --- | --- | --- |
| g(t) (en m) | 0 | 8,75 | 15 | 18,75 | 20 |

La ligne du bas donne les hauteurs y, la ligne du haut les dates t : lue de bas en haut, la table est celle de g⁻¹. On lit g⁻¹(15) = 1 et g⁻¹(18,75) = 1,5.

::: exemple Expliciter g⁻¹ pour la balle

1. g est continue et strictement croissante sur [0 ; 2], d'image [0 ; 20] : c'est une bijection de [0 ; 2] sur [0 ; 20], et g⁻¹ est définie sur [0 ; 20].
2. Pour y de [0 ; 20], on résout g(t) = y avec t dans [0 ; 2] : −5(t − 2)² + 20 = y équivaut à (t − 2)² = (20 − y)/5.
3. Comme t ≤ 2, le nombre t − 2 est négatif : t − 2 = −√((20 − y)/5). On garde la seule solution qui est dans l'intervalle de départ.
4. Donc g⁻¹(y) = 2 − √((20 − y)/5). Contrôle : g⁻¹(15) = 2 − √1 = 1, g⁻¹(20) = 2 − 0 = 2 et g⁻¹(0) = 2 − √4 = 0, comme dans la table.

:::

::: piege
**Erreur : confondre f⁻¹ avec 1/f.** Ici g(1) = 15 : l'inverse du nombre 15 est 1/15, alors que g⁻¹(15) = 1. L'erreur tente parce que f⁻¹(x) ressemble à x⁻¹ = 1/x. Mais f⁻¹ défait f en remontant de l'image à l'antécédent : g⁻¹(g(1)) = 1, alors que 1/g(1) = 1/15 ne redonne jamais l'antécédent.
:::

::: figure Les tableaux de variation de f(x) = (2x + 1)/(x − 3) sur ]3 ; +∞[ et de sa réciproque sur ]2 ; +∞[ : deux flèches descendantes
<svg viewBox="0 0 380 250">
<title>Tableaux de variation de f sur ]3 ; +∞[ et de sa réciproque sur ]2 ; +∞[ : deux flèches descendantes</title>
<rect x="8" y="10" width="364" height="104" fill="none" stroke="#0f172a" stroke-width="1.6"/>
<line x1="8" y1="44" x2="372" y2="44" stroke="#0f172a" stroke-width="1.2"/>
<line x1="78" y1="10" x2="78" y2="114" stroke="#0f172a" stroke-width="1.2"/>
<line x1="138" y1="66" x2="312" y2="96" stroke="#d97706" stroke-width="2.4"/>
<polygon points="312,96 302.37,98.91 303.9,90.04" fill="#d97706"/>
<rect x="8" y="136" width="364" height="104" fill="none" stroke="#0f172a" stroke-width="1.6"/>
<line x1="8" y1="170" x2="372" y2="170" stroke="#0f172a" stroke-width="1.2"/>
<line x1="78" y1="136" x2="78" y2="240" stroke="#0f172a" stroke-width="1.2"/>
<line x1="138" y1="192" x2="312" y2="222" stroke="#d97706" stroke-width="2.4"/>
<polygon points="312,222 302.37,224.91 303.9,216.04" fill="#d97706"/>
<g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="43" y="32" text-anchor="middle" fill="#0f172a" font-size="13">x</text><text x="43" y="84" text-anchor="middle" fill="#0f172a" font-size="13">f(x)</text><text x="104" y="32" text-anchor="middle" fill="#0f172a" font-size="13">3</text><text x="346" y="32" text-anchor="middle" fill="#0f172a" font-size="13">+∞</text><text x="104" y="62" text-anchor="middle" fill="#d97706" font-size="13">+∞</text><text x="346" y="106" text-anchor="middle" fill="#d97706" font-size="13">2</text><text x="43" y="158" text-anchor="middle" fill="#0f172a" font-size="13">y</text><text x="43" y="210" text-anchor="middle" fill="#0f172a" font-size="13">f⁻¹(y)</text><text x="104" y="158" text-anchor="middle" fill="#0f172a" font-size="13">2</text><text x="346" y="158" text-anchor="middle" fill="#0f172a" font-size="13">+∞</text><text x="104" y="188" text-anchor="middle" fill="#d97706" font-size="13">+∞</text><text x="346" y="232" text-anchor="middle" fill="#d97706" font-size="13">3</text></g>
</svg>
:::

Les deux flèches descendent : f⁻¹ varie dans le même sens que f. Les valeurs 2 et 3 changent de ligne : 2 est la valeur limite de f en +∞ et devient la borne de J, tandis que 3, borne de I, devient la limite de f⁻¹ en +∞.

::: exemple Le même outil, sans situation : une fonction homographique

1. Soit f(x) = (2x + 1)/(x − 3) sur I = ]3 ; +∞[. Sa dérivée f′(x) = (2(x − 3) − (2x + 1))/(x − 3)² = −7/(x − 3)² est négative : f est continue et strictement décroissante.
2. lim x→3⁺ f(x) = +∞ (numérateur proche de 7, dénominateur positif tendant vers 0) et lim x→+∞ f(x) = 2, donc J = f(I) = ]2 ; +∞[.
3. Pour y > 2, y = (2x + 1)/(x − 3) équivaut à y(x − 3) = 2x + 1, soit x(y − 2) = 3y + 1, soit x = (3y + 1)/(y − 2) : on peut diviser par y − 2, qui est non nul.
4. Donc f⁻¹(y) = (3y + 1)/(y − 2) sur ]2 ; +∞[. Contrôle : f(4) = 9 et f⁻¹(9) = 28/7 = 4.

:::

::: propriete
**Théorème de la bijection.** Si f est strictement monotone sur un intervalle I, alors f est une bijection de I sur f(I), et f⁻¹ est strictement monotone sur f(I), dans le même sens que f. Si de plus f est continue sur I, alors f(I) est un intervalle et f⁻¹ est continue sur f(I).
:::

::: methode Expliciter f⁻¹

1. Vérifier que f est continue et strictement monotone sur I, puis calculer J = f(I) avec les valeurs et les limites aux bornes : J est l'ensemble de définition de f⁻¹.
2. Pour y de J, résoudre l'équation f(x) = y d'inconnue x. Si plusieurs solutions apparaissent, garder celle qui est dans I.
3. Conclure f⁻¹(y) = cette solution, puis contrôler sur une valeur : f⁻¹(f(x₀)) = x₀.

Cas limite : l'ensemble de définition de f⁻¹ est J, et non I ; et la stricte monotonie seule donne la bijection, la continuité sert à garantir que f(I) est un intervalle.
:::

::: verifie À toi : une réciproque avec racine
Soit k(x) = x² + 2x sur [−1 ; +∞[. Montre que k est une bijection de [−1 ; +∞[ sur [−1 ; +∞[ et explicite k⁻¹.

---

k(x) = (x + 1)² − 1 et k′(x) = 2(x + 1) > 0 sur ]−1 ; +∞[ : k est continue et strictement croissante, avec k(−1) = −1 et une limite +∞ en +∞ : c'est une bijection de [−1 ; +∞[ sur [−1 ; +∞[. Pour y ≥ −1, y = (x + 1)² − 1 équivaut à (x + 1)² = y + 1 ; comme x + 1 ≥ 0, x + 1 = √(y + 1). Donc k⁻¹(y) = √(y + 1) − 1. Contrôle : k(2) = 8 et k⁻¹(8) = √9 − 1 = 2.
:::

::: retenir
f strictement monotone sur I ⟹ bijection de I sur f(I) ; y = f(x) ⟺ x = f⁻¹(y) ; f⁻¹ varie dans le même sens que f et est continue si f l'est ; f⁻¹ n'est pas 1/f.
:::

## 🪞 Deux courbes symétriques par rapport à la droite Δ : y = x

Le dernier contrôle donne k(1) = 3, donc k⁻¹(3) = 1. Le point A(1 ; 3) est sur la courbe de k, et le point A′(3 ; 1), qui a les coordonnées échangées, est sur celle de k⁻¹.
Quelle transformation du plan échange l'abscisse et l'ordonnée d'un point ?

::: figure Les courbes de k (vert) et de k⁻¹ (bleu), échangées par la symétrie d'axe Δ : y = x ; le segment AA′ coupe Δ à angle droit en son milieu
<svg viewBox="0 0 340 330">
<title>Courbes de k(x) = x² + 2x sur [−1 ; +∞[ et de sa réciproque, symétriques par rapport à la droite y = x</title>
<line x1="22" y1="239" x2="322" y2="239" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="322,239 314,243 314,235" fill="#0f172a"/>
<line x1="97" y1="314" x2="97" y2="14" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="97,14 101,22 93,22" fill="#0f172a"/>
<line x1="47" y1="236" x2="47" y2="242" stroke="#0f172a" stroke-width="1.2"/>
<line x1="147" y1="236" x2="147" y2="242" stroke="#0f172a" stroke-width="1.2"/>
<line x1="197" y1="236" x2="197" y2="242" stroke="#0f172a" stroke-width="1.2"/>
<line x1="247" y1="236" x2="247" y2="242" stroke="#0f172a" stroke-width="1.2"/>
<line x1="297" y1="236" x2="297" y2="242" stroke="#0f172a" stroke-width="1.2"/>
<line x1="94" y1="289" x2="100" y2="289" stroke="#0f172a" stroke-width="1.2"/>
<line x1="94" y1="189" x2="100" y2="189" stroke="#0f172a" stroke-width="1.2"/>
<line x1="94" y1="139" x2="100" y2="139" stroke="#0f172a" stroke-width="1.2"/>
<line x1="94" y1="89" x2="100" y2="89" stroke="#0f172a" stroke-width="1.2"/>
<line x1="94" y1="39" x2="100" y2="39" stroke="#0f172a" stroke-width="1.2"/>
<line x1="22" y1="314" x2="322" y2="14" stroke="#64748b" stroke-width="1.8" stroke-dasharray="7 4"/>
<polyline points="47,289 47.73,288.99 48.47,288.96 49.2,288.9 49.94,288.83 50.67,288.73 51.41,288.61 52.14,288.47 52.88,288.31 53.61,288.13 54.34,287.92 55.08,287.69 55.81,287.45 56.55,287.18 57.28,286.89 58.02,286.57 58.75,286.24 59.48,285.88 60.22,285.51 60.95,285.11 61.69,284.69 62.42,284.24 63.16,283.78 63.89,283.29 64.62,282.79 65.36,282.26 66.09,281.71 66.83,281.14 67.56,280.54 68.3,279.93 69.03,279.29 69.77,278.63 70.5,277.95 71.23,277.25 71.97,276.53 72.7,275.79 73.44,275.02 74.17,274.23 74.91,273.42 75.64,272.59 76.38,271.74 77.11,270.87 77.84,269.97 78.58,269.06 79.31,268.12 80.05,267.16 80.78,266.18 81.52,265.17 82.25,264.15 82.98,263.1 83.72,262.03 84.45,260.95 85.19,259.83 85.92,258.7 86.66,257.55 87.39,256.37 88.12,255.17 88.86,253.96 89.59,252.72 90.33,251.45 91.06,250.17 91.8,248.86 92.53,247.54 93.27,246.19 94,244.82 94.73,243.43 95.47,242.02 96.2,240.58 96.94,239.12 97.67,237.65 98.41,236.15 99.14,234.63 99.88,233.08 100.61,231.52 101.34,229.94 102.08,228.33 102.81,226.7 103.55,225.05 104.28,223.38 105.02,221.68 105.75,219.97 106.48,218.23 107.22,216.47 107.95,214.69 108.69,212.89 109.42,211.07 110.16,209.23 110.89,207.36 111.62,205.47 112.36,203.56 113.09,201.63 113.83,199.68 114.56,197.71 115.3,195.71 116.03,193.69 116.77,191.66 117.5,189.59 118.23,187.51 118.97,185.41 119.7,183.29 120.44,181.14 121.17,178.97 121.91,176.78 122.64,174.57 123.38,172.34 124.11,170.08 124.84,167.81 125.58,165.51 126.31,163.19 127.05,160.85 127.78,158.49 128.52,156.1 129.25,153.7 129.98,151.27 130.72,148.82 131.45,146.35 132.19,143.86 132.92,141.35 133.66,138.81 134.39,136.26 135.12,133.68 135.86,131.08 136.59,128.46 137.33,125.82 138.06,123.15 138.8,120.47 139.53,117.76 140.27,115.03 141,112.28 141.73,109.51 142.47,106.71 143.2,103.9 143.94,101.06 144.67,98.2 145.41,95.32 146.14,92.42 146.88,89.5 147.61,86.56 148.34,83.59 149.08,80.6 149.81,77.59 150.55,74.56 151.28,71.51 152.02,68.43 152.75,65.34 153.48,62.22 154.22,59.08 154.95,55.92 155.69,52.74 156.42,49.54 157.16,46.31 157.89,43.07 158.62,39.8 159.36,36.51 160.09,33.2 160.83,29.86 161.56,26.51 162.3,23.13 163.03,19.73 163.77,16.32" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round"/>
<polyline points="47,289 48.72,279.73 50.44,275.89 52.16,272.94 53.88,270.46 55.59,268.27 57.31,266.29 59.03,264.47 60.75,262.78 62.47,261.19 64.19,259.68 65.91,258.25 67.62,256.89 69.34,255.58 71.06,254.31 72.78,253.1 74.5,251.92 76.22,250.78 77.94,249.67 79.66,248.59 81.38,247.54 83.09,246.52 84.81,245.52 86.53,244.54 88.25,243.59 89.97,242.65 91.69,241.73 93.41,240.83 95.12,239.95 96.84,239.08 98.56,238.22 100.28,237.39 102,236.56 103.72,235.75 105.44,234.95 107.16,234.16 108.88,233.38 110.59,232.61 112.31,231.85 114.03,231.11 115.75,230.37 117.47,229.64 119.19,228.92 120.91,228.21 122.63,227.51 124.34,226.81 126.06,226.13 127.78,225.45 129.5,224.77 131.22,224.11 132.94,223.45 134.66,222.8 136.38,222.15 138.09,221.51 139.81,220.88 141.53,220.25 143.25,219.63 144.97,219.01 146.69,218.4 148.41,217.79 150.12,217.19 151.84,216.6 153.56,216.01 155.28,215.42 157,214.84 158.72,214.26 160.44,213.69 162.16,213.12 163.88,212.56 165.59,212 167.31,211.44 169.03,210.89 170.75,210.34 172.47,209.79 174.19,209.25 175.91,208.72 177.62,208.18 179.34,207.65 181.06,207.13 182.78,206.6 184.5,206.08 186.22,205.57 187.94,205.05 189.66,204.54 191.38,204.04 193.09,203.53 194.81,203.03 196.53,202.53 198.25,202.04 199.97,201.54 201.69,201.05 203.41,200.57 205.12,200.08 206.84,199.6 208.56,199.12 210.28,198.64 212,198.17 213.72,197.7 215.44,197.23 217.16,196.76 218.88,196.3 220.59,195.84 222.31,195.38 224.03,194.92 225.75,194.46 227.47,194.01 229.19,193.56 230.91,193.11 232.63,192.66 234.34,192.22 236.06,191.77 237.78,191.33 239.5,190.89 241.22,190.46 242.94,190.02 244.66,189.59 246.38,189.16 248.09,188.73 249.81,188.3 251.53,187.87 253.25,187.45 254.97,187.03 256.69,186.61 258.41,186.19 260.12,185.77 261.84,185.36 263.56,184.94 265.28,184.53 267,184.12 268.72,183.71 270.44,183.3 272.16,182.9 273.88,182.49 275.59,182.09 277.31,181.69 279.03,181.29 280.75,180.89 282.47,180.49 284.19,180.1 285.91,179.71 287.62,179.31 289.34,178.92 291.06,178.53 292.78,178.14 294.5,177.76 296.22,177.37 297.94,176.99 299.66,176.6 301.38,176.22 303.09,175.84 304.81,175.46 306.53,175.09 308.25,174.71 309.97,174.33 311.69,173.96 313.41,173.59 315.12,173.21 316.84,172.84 318.56,172.47 320.28,172.11 322,171.74" fill="none" stroke="#2563eb" stroke-width="2.8" stroke-linejoin="round"/>
<line x1="147" y1="89" x2="247" y2="189" stroke="#d97706" stroke-width="1.8" stroke-dasharray="4 3"/>
<circle cx="147" cy="89" r="4" fill="#0f172a" stroke="#ffffff" stroke-width="1.2"/>
<circle cx="247" cy="189" r="4" fill="#0f172a" stroke="#ffffff" stroke-width="1.2"/>
<circle cx="197" cy="139" r="3.2" fill="#d97706" stroke="#ffffff" stroke-width="1.2"/>
<g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="47" y="254" text-anchor="middle" fill="#0f172a" font-size="10">-1</text><text x="147" y="254" text-anchor="middle" fill="#0f172a" font-size="10">1</text><text x="197" y="254" text-anchor="middle" fill="#0f172a" font-size="10">2</text><text x="247" y="254" text-anchor="middle" fill="#0f172a" font-size="10">3</text><text x="297" y="254" text-anchor="middle" fill="#0f172a" font-size="10">4</text><text x="90" y="292.5" text-anchor="end" fill="#0f172a" font-size="10">-1</text><text x="90" y="192.5" text-anchor="end" fill="#0f172a" font-size="10">1</text><text x="90" y="142.5" text-anchor="end" fill="#0f172a" font-size="10">2</text><text x="90" y="92.5" text-anchor="end" fill="#0f172a" font-size="10">3</text><text x="90" y="42.5" text-anchor="end" fill="#0f172a" font-size="10">4</text><text x="320" y="255" text-anchor="end" fill="#0f172a" font-size="12">x</text><text x="105" y="22" text-anchor="start" fill="#0f172a" font-size="12">y</text><text x="139.5" y="76.5" text-anchor="end" fill="#0f172a" font-size="11">A(1 ; 3)</text><text x="252" y="204" text-anchor="start" fill="#0f172a" font-size="11">A′(3 ; 1)</text><text x="157" y="36.5" text-anchor="start" fill="#0f6e56" font-size="13">C_k</text><text x="279.5" y="166.5" text-anchor="start" fill="#2563eb" font-size="13">C_k⁻¹</text><text x="67" y="301.5" text-anchor="start" fill="#64748b" font-size="11">Δ : y = x</text></g>
</svg>
:::

A et A′ sont de part et d'autre de la droite pointillée, à égale distance d'elle : on passe de l'une à l'autre en échangeant les deux coordonnées, et la courbe bleue entière est l'image de la verte.

::: exemple Les points A et A′

1. k(1) = 1 + 2 = 3, donc A(1 ; 3) est sur la courbe de k.
2. y = k(x) équivaut à x = k⁻¹(y) : k⁻¹(3) = 1, donc A′(3 ; 1) est sur la courbe de k⁻¹. On a échangé abscisse et ordonnée.
3. Le milieu de [AA′] est ((1 + 3)/2 ; (3 + 1)/2) = (2 ; 2), qui est sur Δ : ses deux coordonnées sont égales.
4. Le vecteur AA′ a pour coordonnées (2 ; −2) et Δ est dirigée par (1 ; 1) : 2 × 1 + (−2) × 1 = 0, donc AA′ est perpendiculaire à Δ. A′ est le symétrique de A par rapport à Δ.
5. Sans résoudre d'équation : k(2) = 8 donne le point (2 ; 8) de la courbe de k, donc le point (8 ; 2) de celle de k⁻¹, soit k⁻¹(8) = 2.

:::

::: piege
**Erreur : appliquer le miroir dans un repère qui n'est pas orthonormé.** Si l'unité des ordonnées est deux fois plus petite que celle des abscisses (0,5 cm contre 1 cm), A(1 ; 3) est dessiné en (1 cm ; 1,5 cm) et A′(3 ; 1) en (3 cm ; 0,5 cm) : le vecteur dessiné (2 ; −1) n'est pas perpendiculaire à la droite y = x, dessinée dans la direction (1 ; 0,5), car 2 × 1 + (−1) × 0,5 = 1,5 ≠ 0. Plier le papier le long de Δ ne superpose plus les courbes.
:::

::: propriete
Dans un repère **orthonormé**, les courbes de f et de f⁻¹ sont symétriques par rapport à la droite Δ : y = x. Un point M(a ; b) est sur la courbe de f si et seulement si M′(b ; a) est sur la courbe de f⁻¹.
Cas limite : un point de la courbe de f situé sur Δ (f(a) = a) est son propre symétrique : c'est un point commun des deux courbes, comme (0 ; 0) et (−1 ; −1) pour k.
:::

::: exemple Le même outil, sans situation : tracer la courbe de la réciproque

1. Une bijection f croissante passe par (−2 ; −1), (0 ; 1) et (3 ; 6).
2. On échange les coordonnées : (−1 ; −2), (1 ; 0) et (6 ; 3) sont sur la courbe de f⁻¹, symétriques des trois premiers par rapport à Δ.
3. On relie ces points par une courbe croissante, comme f⁻¹ qui varie dans le même sens que f.

:::

::: verifie À toi : trois points de la réciproque
Soit u(x) = x³ + x − 2, strictement croissante sur ℝ. On a u(−1) = −4, u(1) = 0 et u(2) = 8. Donne trois points de la courbe de u⁻¹.

---

Un point (a ; u(a)) de la courbe de u donne le point (u(a) ; a) de la courbe de u⁻¹, par la symétrie d'axe Δ. Donc (−4 ; −1), (0 ; 1) et (8 ; 2) sont sur la courbe de u⁻¹ ; on a donc u⁻¹(0) = 1.
:::

::: retenir
Dans un repère orthonormé, la courbe de f⁻¹ est la symétrique de celle de f par rapport à Δ : y = x ; M(a ; b) sur la courbe de f ⟺ M′(b ; a) sur celle de f⁻¹.
:::

## ⛏️ La racine n-ième : réciproque de x ↦ xⁿ

Un cube a un volume de 64 dm³ : son arête c vérifie c³ = 64, donc c = 4 dm, car 4³ = 64. Et pour un volume de 10 dm³ ? L'arête existe et elle est unique, car c ↦ c³ est strictement croissante, mais aucun nombre simple ne convient.
Comment nommer ce nombre ?

::: definition
Pour tout entier n ≥ 2, la fonction x ↦ xⁿ est continue et strictement croissante sur [0 ; +∞[ : c'est une bijection de [0 ; +∞[ sur [0 ; +∞[. Sa réciproque est la **racine n-ième**, notée x ↦ ⁿ√x ou x^(1/n), définie sur [0 ; +∞[. Pour x ≥ 0 et y ≥ 0 :
$$ y = ⁿ√x ⟺ yⁿ = x $$
Pour n = 2, c'est √x ; pour n = 3, c'est ∛x.
:::

::: figure Les courbes de √x (vert), ∛x (orange) et ⁴√x (bleu) : elles partent de (0 ; 0), passent par (1 ; 1), et se rangent selon n au-delà de x = 1
<svg viewBox="0 0 384 206">
<title>Courbes de √x, ∛x et ⁴√x sur [0 ; 4,5] : elles passent toutes par (0 ; 0) et (1 ; 1)</title>
<line x1="22" y1="165.6" x2="348.4" y2="165.6" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="348.4,165.6 340.4,169.6 340.4,161.6" fill="#0f172a"/>
<line x1="47.6" y1="184.8" x2="47.6" y2="12" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="47.6,12 51.6,20 43.6,20" fill="#0f172a"/>
<line x1="111.6" y1="162.6" x2="111.6" y2="168.6" stroke="#0f172a" stroke-width="1.2"/>
<line x1="175.6" y1="162.6" x2="175.6" y2="168.6" stroke="#0f172a" stroke-width="1.2"/>
<line x1="239.6" y1="162.6" x2="239.6" y2="168.6" stroke="#0f172a" stroke-width="1.2"/>
<line x1="303.6" y1="162.6" x2="303.6" y2="168.6" stroke="#0f172a" stroke-width="1.2"/>
<line x1="44.6" y1="101.6" x2="50.6" y2="101.6" stroke="#0f172a" stroke-width="1.2"/>
<line x1="44.6" y1="37.6" x2="50.6" y2="37.6" stroke="#0f172a" stroke-width="1.2"/>
<polyline points="47.6,165.6 49.4,154.87 51.2,150.42 53,147.01 54.8,144.13 56.6,141.6 58.4,139.31 60.2,137.2 62,135.24 63.8,133.4 65.6,131.66 67.4,130 69.2,128.42 71,126.9 72.8,125.44 74.6,124.03 76.4,122.67 78.2,121.35 80,120.06 81.8,118.82 83.6,117.6 85.4,116.41 87.2,115.26 89,114.13 90.8,113.02 92.6,111.93 94.4,110.87 96.2,109.83 98,108.81 99.8,107.8 101.6,106.81 103.4,105.84 105.2,104.88 107,103.94 108.8,103.02 110.6,102.1 112.4,101.2 114.2,100.31 116,99.44 117.8,98.57 119.6,97.72 121.4,96.87 123.2,96.04 125,95.22 126.8,94.4 128.6,93.6 130.4,92.8 132.2,92.02 134,91.24 135.8,90.47 137.6,89.71 139.4,88.95 141.2,88.2 143,87.46 144.8,86.73 146.6,86 148.4,85.28 150.2,84.57 152,83.86 153.8,83.16 155.6,82.46 157.4,81.77 159.2,81.09 161,80.41 162.8,79.73 164.6,79.07 166.4,78.4 168.2,77.75 170,77.09 171.8,76.44 173.6,75.8 175.4,75.16 177.2,74.53 179,73.9 180.8,73.27 182.6,72.65 184.4,72.03 186.2,71.42 188,70.81 189.8,70.2 191.6,69.6 193.4,69 195.2,68.41 197,67.82 198.8,67.23 200.6,66.65 202.4,66.07 204.2,65.49 206,64.91 207.8,64.34 209.6,63.78 211.4,63.21 213.2,62.65 215,62.09 216.8,61.54 218.6,60.99 220.4,60.44 222.2,59.89 224,59.35 225.8,58.81 227.6,58.27 229.4,57.73 231.2,57.2 233,56.67 234.8,56.14 236.6,55.62 238.4,55.1 240.2,54.58 242,54.06 243.8,53.54 245.6,53.03 247.4,52.52 249.2,52.01 251,51.51 252.8,51 254.6,50.5 256.4,50 258.2,49.5 260,49.01 261.8,48.52 263.6,48.02 265.4,47.54 267.2,47.05 269,46.56 270.8,46.08 272.6,45.6 274.4,45.12 276.2,44.64 278,44.17 279.8,43.7 281.6,43.22 283.4,42.75 285.2,42.29 287,41.82 288.8,41.36 290.6,40.89 292.4,40.43 294.2,39.97 296,39.51 297.8,39.06 299.6,38.6 301.4,38.15 303.2,37.7 305,37.25 306.8,36.8 308.6,36.36 310.4,35.91 312.2,35.47 314,35.03 315.8,34.59 317.6,34.15 319.4,33.71 321.2,33.27 323,32.84 324.8,32.41 326.6,31.97 328.4,31.54 330.2,31.11 332,30.69 333.8,30.26 335.6,29.84" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round"/>
<polyline points="47.6,165.6 49.4,146.14 51.2,141.08 53,137.53 54.8,134.7 56.6,132.32 58.4,130.23 60.2,128.37 62,126.67 63.8,125.12 65.6,123.67 67.4,122.31 69.2,121.04 71,119.84 72.8,118.69 74.6,117.6 76.4,116.56 78.2,115.56 80,114.59 81.8,113.66 83.6,112.77 85.4,111.9 87.2,111.06 89,110.25 90.8,109.46 92.6,108.69 94.4,107.94 96.2,107.21 98,106.5 99.8,105.8 101.6,105.12 103.4,104.46 105.2,103.81 107,103.17 108.8,102.55 110.6,101.94 112.4,101.33 114.2,100.74 116,100.17 117.8,99.6 119.6,99.04 121.4,98.49 123.2,97.95 125,97.41 126.8,96.89 128.6,96.37 130.4,95.86 132.2,95.36 134,94.87 135.8,94.38 137.6,93.9 139.4,93.42 141.2,92.95 143,92.49 144.8,92.03 146.6,91.58 148.4,91.14 150.2,90.7 152,90.26 153.8,89.83 155.6,89.4 157.4,88.98 159.2,88.57 161,88.16 162.8,87.75 164.6,87.34 166.4,86.95 168.2,86.55 170,86.16 171.8,85.77 173.6,85.39 175.4,85.01 177.2,84.63 179,84.26 180.8,83.89 182.6,83.52 184.4,83.16 186.2,82.8 188,82.44 189.8,82.09 191.6,81.74 193.4,81.39 195.2,81.04 197,80.7 198.8,80.36 200.6,80.02 202.4,79.69 204.2,79.36 206,79.03 207.8,78.7 209.6,78.38 211.4,78.06 213.2,77.74 215,77.42 216.8,77.1 218.6,76.79 220.4,76.48 222.2,76.17 224,75.87 225.8,75.56 227.6,75.26 229.4,74.96 231.2,74.66 233,74.37 234.8,74.07 236.6,73.78 238.4,73.49 240.2,73.2 242,72.91 243.8,72.63 245.6,72.34 247.4,72.06 249.2,71.78 251,71.5 252.8,71.23 254.6,70.95 256.4,70.68 258.2,70.41 260,70.14 261.8,69.87 263.6,69.6 265.4,69.33 267.2,69.07 269,68.81 270.8,68.54 272.6,68.28 274.4,68.03 276.2,67.77 278,67.51 279.8,67.26 281.6,67 283.4,66.75 285.2,66.5 287,66.25 288.8,66 290.6,65.76 292.4,65.51 294.2,65.27 296,65.02 297.8,64.78 299.6,64.54 301.4,64.3 303.2,64.06 305,63.82 306.8,63.58 308.6,63.35 310.4,63.11 312.2,62.88 314,62.65 315.8,62.42 317.6,62.19 319.4,61.96 321.2,61.73 323,61.5 324.8,61.28 326.6,61.05 328.4,60.83 330.2,60.6 332,60.38 333.8,60.16 335.6,59.94" fill="none" stroke="#d97706" stroke-width="2.8" stroke-linejoin="round"/>
<polyline points="47.6,165.6 49.4,139.39 51.2,134.43 53,131.11 54.8,128.53 56.6,126.41 58.4,124.58 60.2,122.97 62,121.52 63.8,120.2 65.6,118.99 67.4,117.87 69.2,116.82 71,115.83 72.8,114.9 74.6,114.02 76.4,113.18 78.2,112.38 80,111.62 81.8,110.88 83.6,110.17 85.4,109.49 87.2,108.84 89,108.2 90.8,107.59 92.6,106.99 94.4,106.42 96.2,105.86 98,105.31 99.8,104.78 101.6,104.26 103.4,103.76 105.2,103.26 107,102.78 108.8,102.31 110.6,101.85 112.4,101.4 114.2,100.96 116,100.53 117.8,100.1 119.6,99.69 121.4,99.28 123.2,98.88 125,98.48 126.8,98.1 128.6,97.72 130.4,97.34 132.2,96.98 134,96.61 135.8,96.26 137.6,95.91 139.4,95.56 141.2,95.22 143,94.88 144.8,94.55 146.6,94.23 148.4,93.9 150.2,93.59 152,93.27 153.8,92.96 155.6,92.66 157.4,92.35 159.2,92.06 161,91.76 162.8,91.47 164.6,91.18 166.4,90.9 168.2,90.62 170,90.34 171.8,90.06 173.6,89.79 175.4,89.52 177.2,89.25 179,88.99 180.8,88.73 182.6,88.47 184.4,88.22 186.2,87.96 188,87.71 189.8,87.46 191.6,87.22 193.4,86.97 195.2,86.73 197,86.49 198.8,86.25 200.6,86.02 202.4,85.79 204.2,85.56 206,85.33 207.8,85.1 209.6,84.87 211.4,84.65 213.2,84.43 215,84.21 216.8,83.99 218.6,83.78 220.4,83.56 222.2,83.35 224,83.14 225.8,82.93 227.6,82.72 229.4,82.51 231.2,82.31 233,82.1 234.8,81.9 236.6,81.7 238.4,81.5 240.2,81.31 242,81.11 243.8,80.91 245.6,80.72 247.4,80.53 249.2,80.34 251,80.15 252.8,79.96 254.6,79.77 256.4,79.59 258.2,79.4 260,79.22 261.8,79.04 263.6,78.85 265.4,78.67 267.2,78.5 269,78.32 270.8,78.14 272.6,77.96 274.4,77.79 276.2,77.62 278,77.44 279.8,77.27 281.6,77.1 283.4,76.93 285.2,76.76 287,76.59 288.8,76.43 290.6,76.26 292.4,76.1 294.2,75.93 296,75.77 297.8,75.61 299.6,75.45 301.4,75.29 303.2,75.13 305,74.97 306.8,74.81 308.6,74.65 310.4,74.5 312.2,74.34 314,74.18 315.8,74.03 317.6,73.88 319.4,73.73 321.2,73.57 323,73.42 324.8,73.27 326.6,73.12 328.4,72.97 330.2,72.83 332,72.68 333.8,72.53 335.6,72.39" fill="none" stroke="#2563eb" stroke-width="2.8" stroke-linejoin="round"/>
<circle cx="111.6" cy="101.6" r="4" fill="#0f172a" stroke="#ffffff" stroke-width="1.2"/>
<g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="111.6" y="180.6" text-anchor="middle" fill="#0f172a" font-size="10">1</text><text x="175.6" y="180.6" text-anchor="middle" fill="#0f172a" font-size="10">2</text><text x="239.6" y="180.6" text-anchor="middle" fill="#0f172a" font-size="10">3</text><text x="303.6" y="180.6" text-anchor="middle" fill="#0f172a" font-size="10">4</text><text x="40.6" y="105.1" text-anchor="end" fill="#0f172a" font-size="10">1</text><text x="40.6" y="41.1" text-anchor="end" fill="#0f172a" font-size="10">2</text><text x="346.4" y="181.6" text-anchor="end" fill="#0f172a" font-size="12">x</text><text x="55.6" y="20" text-anchor="start" fill="#0f172a" font-size="12">y</text><text x="118" y="115.68" text-anchor="start" fill="#0f172a" font-size="11">(1 ; 1)</text><text x="338.8" y="24.8" text-anchor="start" fill="#0f6e56" font-size="12">√x</text><text x="338.8" y="55.52" text-anchor="start" fill="#d97706" font-size="12">∛x</text><text x="338.8" y="82.4" text-anchor="start" fill="#2563eb" font-size="12">⁴√x</text></g>
</svg>
:::

Chaque courbe est la symétrique de celle de xⁿ par rapport à Δ. Pour x > 1, plus n est grand, plus la courbe est basse ; pour 0 < x < 1, c'est l'inverse.

::: exemple L'arête d'un cube

1. Volume 64 dm³ : c = ∛64 = 4 dm, car 4³ = 64 (y = ∛x équivaut à y³ = x).
2. Volume 10 dm³ : c = ∛10, valeur exacte de l'arête, et c ≈ 2,15 dm car 2,15³ ≈ 9,94 est proche de 10.
3. Par définition, (∛10)³ = 10 : élever au cube défait la racine cubique.
4. Les puissances rationnelles se lisent par racine puis puissance : 8^(2/3) = (8²)^(1/3) = ∛64 = 4.

:::

::: piege
**Erreur : lire 8^(1/3) comme 8/3.** L'écriture x^(1/n) désigne la racine n-ième, pas une division : 8^(1/3) = ∛8 = 2, alors que 8/3 ≈ 2,67. L'erreur tente parce que l'exposant 1/3 ressemble à une fraction qu'on multiplierait. Le test est de vérifier : 2³ = 8, alors que (8/3)³ = 512/27 ≈ 18,96, loin de 8.
:::

::: propriete
Pour n ≥ 2 : x ↦ ⁿ√x est continue et strictement croissante sur [0 ; +∞[, avec ⁿ√0 = 0 et ⁿ√1 = 1. Pour tout x ≥ 0, (ⁿ√x)ⁿ = x. En +∞ : lim x→+∞ ⁿ√x = +∞ et lim x→+∞ ⁿ√x / x = 0. Pour des entiers p, q ≥ 1 et x ≥ 0 : x^(p/q) = (x^p)^(1/q).
Cas limite : dans ce chapitre, ⁿ√x n'est défini que pour x ≥ 0.
:::

::: exemple Le même outil, sans situation : simplifier et passer à la limite

1. ⁴√81 = 3 car 3⁴ = 81, et ∛(x⁶) = x² pour x ≥ 0 car (x²)³ = x⁶.
2. Pour la limite de ∛x / x en +∞, on pose t = ∛x : alors x = t³ et ∛x / x = t / t³ = 1/t².
3. Quand x tend vers +∞, t = ∛x tend vers +∞, donc 1/t² tend vers 0 : lim x→+∞ ∛x / x = 0. La racine croît moins vite que x.

:::

::: verifie À toi : racine et puissance rationnelle
Calcule ⁵√32 et 16^(3/4).

---

⁵√32 = 2, car 2⁵ = 32 (y = ⁿ√x équivaut à yⁿ = x). Pour 16^(3/4), on applique x^(p/q) = (x^p)^(1/q) : 16^(3/4) = (16³)^(1/4) = ⁴√4096 = 8, car 8⁴ = 4096.
:::

::: retenir
ⁿ√x est la réciproque de xⁿ sur [0 ; +∞[ : y = ⁿ√x ⟺ yⁿ = x ; elle est croissante, ⁿ√x / x tend vers 0 en +∞, et x^(p/q) = (x^p)^(1/q).
:::

## 📐 Dérivée de la réciproque en un point

À t = 1, la balle monte à la vitesse g′(1) = 10 m/s, puisque g′(t) = −10t + 20. Vers 15 m, combien de temps met-elle à gagner un mètre de plus ? À peu près 1/10 de seconde : c'est la pente de g⁻¹ en 15.
Peut-on la calculer à partir de g′, sans expliciter g⁻¹ ?

::: figure Les courbes de u(x) = x³ + x − 2 (vert) et de sa réciproque (bleu) avec leurs tangentes orange en A(1 ; 0) et A′(0 ; 1) : pentes 4 et 1/4
<svg viewBox="0 0 330 326">
<title>Courbes de u(x) = x³ + x − 2 et de sa réciproque avec leurs tangentes en (1 ; 0) et (0 ; 1), de pentes 4 et 1/4</title>
<line x1="14" y1="164.4" x2="314.8" y2="164.4" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="314.8,164.4 306.8,168.4 306.8,160.4" fill="#0f172a"/>
<line x1="164.4" y1="314.8" x2="164.4" y2="14" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="164.4,14 168.4,22 160.4,22" fill="#0f172a"/>
<line x1="23.4" y1="161.4" x2="23.4" y2="167.4" stroke="#0f172a" stroke-width="1.2"/>
<line x1="70.4" y1="161.4" x2="70.4" y2="167.4" stroke="#0f172a" stroke-width="1.2"/>
<line x1="117.4" y1="161.4" x2="117.4" y2="167.4" stroke="#0f172a" stroke-width="1.2"/>
<line x1="211.4" y1="161.4" x2="211.4" y2="167.4" stroke="#0f172a" stroke-width="1.2"/>
<line x1="258.4" y1="161.4" x2="258.4" y2="167.4" stroke="#0f172a" stroke-width="1.2"/>
<line x1="305.4" y1="161.4" x2="305.4" y2="167.4" stroke="#0f172a" stroke-width="1.2"/>
<line x1="161.4" y1="305.4" x2="167.4" y2="305.4" stroke="#0f172a" stroke-width="1.2"/>
<line x1="161.4" y1="258.4" x2="167.4" y2="258.4" stroke="#0f172a" stroke-width="1.2"/>
<line x1="161.4" y1="211.4" x2="167.4" y2="211.4" stroke="#0f172a" stroke-width="1.2"/>
<line x1="161.4" y1="117.4" x2="167.4" y2="117.4" stroke="#0f172a" stroke-width="1.2"/>
<line x1="161.4" y1="70.4" x2="167.4" y2="70.4" stroke="#0f172a" stroke-width="1.2"/>
<line x1="161.4" y1="23.4" x2="167.4" y2="23.4" stroke="#0f172a" stroke-width="1.2"/>
<line x1="14" y1="314.8" x2="314.8" y2="14" stroke="#64748b" stroke-width="1.6" stroke-dasharray="7 4"/>
<polyline points="128.83,314.34 129.43,312.72 130.03,311.14 130.64,309.59 131.24,308.07 131.84,306.59 132.44,305.14 133.04,303.72 133.64,302.33 134.24,300.97 134.85,299.64 135.45,298.34 136.05,297.07 136.65,295.82 137.25,294.6 137.85,293.41 138.46,292.25 139.06,291.11 139.66,290 140.26,288.91 140.86,287.84 141.46,286.8 142.07,285.78 142.67,284.78 143.27,283.8 143.87,282.85 144.47,281.91 145.07,280.99 145.68,280.1 146.28,279.22 146.88,278.36 147.48,277.51 148.08,276.69 148.68,275.87 149.28,275.08 149.89,274.3 150.49,273.53 151.09,272.78 151.69,272.04 152.29,271.31 152.89,270.6 153.5,269.89 154.1,269.2 154.7,268.51 155.3,267.84 155.9,267.18 156.5,266.52 157.11,265.87 157.71,265.23 158.31,264.59 158.91,263.96 159.51,263.34 160.11,262.72 160.72,262.11 161.32,261.5 161.92,260.89 162.52,260.28 163.12,259.68 163.72,259.08 164.32,258.48 164.93,257.87 165.53,257.27 166.13,256.67 166.73,256.06 167.33,255.46 167.93,254.85 168.54,254.23 169.14,253.61 169.74,252.99 170.34,252.36 170.94,251.73 171.54,251.09 172.15,250.44 172.75,249.79 173.35,249.13 173.95,248.46 174.55,247.77 175.15,247.08 175.76,246.38 176.36,245.67 176.96,244.94 177.56,244.21 178.16,243.46 178.76,242.7 179.36,241.92 179.97,241.13 180.57,240.32 181.17,239.5 181.77,238.66 182.37,237.8 182.97,236.92 183.58,236.03 184.18,235.12 184.78,234.19 185.38,233.24 185.98,232.27 186.58,231.27 187.19,230.26 187.79,229.22 188.39,228.16 188.99,227.08 189.59,225.97 190.19,224.84 190.8,223.68 191.4,222.5 192,221.29 192.6,220.05 193.2,218.78 193.8,217.49 194.4,216.17 195.01,214.81 195.61,213.43 196.21,212.02 196.81,210.58 197.41,209.1 198.01,207.59 198.62,206.05 199.22,204.48 199.82,202.87 200.42,201.22 201.02,199.54 201.62,197.83 202.23,196.07 202.83,194.29 203.43,192.46 204.03,190.59 204.63,188.69 205.23,186.74 205.84,184.76 206.44,182.74 207.04,180.67 207.64,178.56 208.24,176.41 208.84,174.22 209.44,171.98 210.05,169.7 210.65,167.37 211.25,165 211.85,162.58 212.45,160.12 213.05,157.61 213.66,155.05 214.26,152.44 214.86,149.78 215.46,147.07 216.06,144.32 216.66,141.51 217.27,138.65 217.87,135.74 218.47,132.78 219.07,129.76 219.67,126.69 220.27,123.56 220.88,120.38 221.48,117.15 222.08,113.86 222.68,110.51 223.28,107.1 223.88,103.64 224.48,100.12 225.09,96.54 225.69,92.9 226.29,89.2 226.89,85.43 227.49,81.61 228.09,77.73 228.7,73.78 229.3,69.77 229.9,65.69 230.5,61.55 231.1,57.35 231.7,53.08 232.31,48.75 232.91,44.34 233.51,39.87 234.11,35.33 234.71,30.73 235.31,26.05 235.92,21.31 236.52,16.49" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round"/>
<polyline points="14.46,199.97 16.08,199.37 17.66,198.77 19.21,198.16 20.73,197.56 22.21,196.96 23.66,196.36 25.08,195.76 26.47,195.16 27.83,194.56 29.16,193.95 30.46,193.35 31.73,192.75 32.98,192.15 34.2,191.55 35.39,190.95 36.55,190.34 37.69,189.74 38.8,189.14 39.89,188.54 40.96,187.94 42,187.34 43.02,186.73 44.02,186.13 45,185.53 45.95,184.93 46.89,184.33 47.81,183.73 48.7,183.12 49.58,182.52 50.44,181.92 51.29,181.32 52.11,180.72 52.93,180.12 53.72,179.52 54.5,178.91 55.27,178.31 56.02,177.71 56.76,177.11 57.49,176.51 58.2,175.91 58.91,175.3 59.6,174.7 60.29,174.1 60.96,173.5 61.62,172.9 62.28,172.3 62.93,171.69 63.57,171.09 64.21,170.49 64.84,169.89 65.46,169.29 66.08,168.69 66.69,168.08 67.3,167.48 67.91,166.88 68.52,166.28 69.12,165.68 69.72,165.08 70.32,164.48 70.93,163.87 71.53,163.27 72.13,162.67 72.74,162.07 73.34,161.47 73.95,160.87 74.57,160.26 75.19,159.66 75.81,159.06 76.44,158.46 77.07,157.86 77.71,157.26 78.36,156.65 79.01,156.05 79.67,155.45 80.34,154.85 81.03,154.25 81.72,153.65 82.42,153.04 83.13,152.44 83.86,151.84 84.59,151.24 85.34,150.64 86.1,150.04 86.88,149.44 87.67,148.83 88.48,148.23 89.3,147.63 90.14,147.03 91,146.43 91.88,145.83 92.77,145.22 93.68,144.62 94.61,144.02 95.56,143.42 96.53,142.82 97.53,142.22 98.54,141.61 99.58,141.01 100.64,140.41 101.72,139.81 102.83,139.21 103.96,138.61 105.12,138 106.3,137.4 107.51,136.8 108.75,136.2 110.02,135.6 111.31,135 112.63,134.4 113.99,133.79 115.37,133.19 116.78,132.59 118.22,131.99 119.7,131.39 121.21,130.79 122.75,130.18 124.32,129.58 125.93,128.98 127.58,128.38 129.26,127.78 130.97,127.18 132.73,126.57 134.51,125.97 136.34,125.37 138.21,124.77 140.11,124.17 142.06,123.57 144.04,122.96 146.06,122.36 148.13,121.76 150.24,121.16 152.39,120.56 154.58,119.96 156.82,119.36 159.1,118.75 161.43,118.15 163.8,117.55 166.22,116.95 168.68,116.35 171.19,115.75 173.75,115.14 176.36,114.54 179.02,113.94 181.73,113.34 184.48,112.74 187.29,112.14 190.15,111.53 193.06,110.93 196.02,110.33 199.04,109.73 202.11,109.13 205.24,108.53 208.42,107.92 211.65,107.32 214.94,106.72 218.29,106.12 221.7,105.52 225.16,104.92 228.68,104.32 232.26,103.71 235.9,103.11 239.6,102.51 243.37,101.91 247.19,101.31 251.07,100.71 255.02,100.1 259.03,99.5 263.11,98.9 267.25,98.3 271.45,97.7 275.72,97.1 280.05,96.49 284.46,95.89 288.93,95.29 293.47,94.69 298.07,94.09 302.75,93.49 307.49,92.88 312.31,92.28" fill="none" stroke="#2563eb" stroke-width="2.8" stroke-linejoin="round"/>
<line x1="185.55" y1="267.8" x2="237.25" y2="61" stroke="#d97706" stroke-width="2.2"/>
<line x1="51.6" y1="145.6" x2="296" y2="84.5" stroke="#d97706" stroke-width="2.2"/>
<circle cx="211.4" cy="164.4" r="4" fill="#0f172a" stroke="#ffffff" stroke-width="1.2"/>
<circle cx="164.4" cy="117.4" r="4" fill="#0f172a" stroke="#ffffff" stroke-width="1.2"/>
<g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="23.4" y="179.4" text-anchor="middle" fill="#0f172a" font-size="10">-3</text><text x="70.4" y="179.4" text-anchor="middle" fill="#0f172a" font-size="10">-2</text><text x="117.4" y="179.4" text-anchor="middle" fill="#0f172a" font-size="10">-1</text><text x="211.4" y="179.4" text-anchor="middle" fill="#0f172a" font-size="10">1</text><text x="258.4" y="179.4" text-anchor="middle" fill="#0f172a" font-size="10">2</text><text x="305.4" y="179.4" text-anchor="middle" fill="#0f172a" font-size="10">3</text><text x="157.4" y="308.9" text-anchor="end" fill="#0f172a" font-size="10">-3</text><text x="157.4" y="261.9" text-anchor="end" fill="#0f172a" font-size="10">-2</text><text x="157.4" y="214.9" text-anchor="end" fill="#0f172a" font-size="10">-1</text><text x="157.4" y="120.9" text-anchor="end" fill="#0f172a" font-size="10">1</text><text x="157.4" y="73.9" text-anchor="end" fill="#0f172a" font-size="10">2</text><text x="157.4" y="26.9" text-anchor="end" fill="#0f172a" font-size="10">3</text><text x="312.8" y="156.4" text-anchor="end" fill="#0f172a" font-size="12">x</text><text x="172.4" y="22" text-anchor="start" fill="#0f172a" font-size="12">y</text><text x="216.1" y="193.54" text-anchor="start" fill="#0f172a" font-size="11">A(1 ; 0)</text><text x="157.35" y="99.54" text-anchor="end" fill="#0f172a" font-size="11">A′(0 ; 1)</text><text x="240.54" y="44.55" text-anchor="start" fill="#0f6e56" font-size="13">C_u</text><text x="263.1" y="77.45" text-anchor="start" fill="#2563eb" font-size="13">C_u⁻¹</text><text x="235.84" y="122.1" text-anchor="start" fill="#d97706" font-size="11">pente 4</text><text x="53.95" y="157.35" text-anchor="start" fill="#d97706" font-size="11">pente 1/4</text></g>
</svg>
:::

La tangente en A a pour pente 4 ; sa symétrique par rapport à Δ est la tangente en A′, de pente 1/4 : échanger x et y échange la « montée » et l'« avancée » du triangle de pente, donc inverse la pente.

::: exemple La vitesse de montée de la balle

1. g′(t) = −10t + 20, donc g′(1) = 10, qui est non nul.
2. g(1) = 15 : on a y₀ = 15 et x₀ = g⁻¹(15) = 1.
3. La tangente de la courbe de g⁻¹ en (15 ; 1) est la symétrique de celle de g en (1 ; 15), de pente 10 : sa pente est 1/10, soit (g⁻¹)′(15) = 1/10.
4. Vérification avec g⁻¹(y) = 2 − √((20 − y)/5) : (g⁻¹)′(y) = 1/(10√((20 − y)/5)), qui vaut 1/10 pour y = 15. À 10 m/s, gagner 1 m prend environ 0,1 s.

:::

::: exemple Le même outil, sans situation : une réciproque non explicite

1. Soit u(x) = x³ + x − 2 sur ℝ. u′(x) = 3x² + 1 > 0 : u est une bijection de ℝ sur ℝ, mais on ne sait pas écrire u⁻¹ simplement.
2. On cherche x₀ tel que u(x₀) = 0 : u(1) = 1 + 1 − 2 = 0, donc u⁻¹(0) = 1.
3. u′(1) = 3 + 1 = 4, non nul : (u⁻¹)′(0) = 1/u′(1) = 1/4.
4. Tangente à la courbe de u⁻¹ en A′(0 ; 1) : y = (1/4)(x − 0) + 1 = x/4 + 1, comme sur la figure.

:::

::: piege
**Erreur : calculer f′ au point y₀ au lieu de x₀.** Pour g, g′(15) = −10 × 15 + 20 = −130, et 1/g′(15) = −1/130 est négatif. C'est impossible : g⁻¹ est croissante, sa dérivée est positive. L'erreur tente parce que la formule porte sur « la dérivée au point 15 ». Mais f′ s'évalue à l'antécédent x₀ = f⁻¹(y₀) = 1, jamais en y₀.
:::

::: propriete
Soit f une bijection d'un intervalle I sur J = f(I), x₀ un réel de I et y₀ = f(x₀). Si f est dérivable en x₀ et f′(x₀) ≠ 0, alors f⁻¹ est dérivable en y₀ et :
$$ (f⁻¹)′(y₀) = 1/f′(x₀) = 1/f′(f⁻¹(y₀)) $$
Cas limite : si f′(x₀) = 0, f⁻¹ n'est pas dérivable en y₀ : sa courbe y a une tangente verticale.
:::

::: verifie À toi : un nombre dérivé de réciproque
Soit v(x) = x⁵ + 2x, bijection de ℝ sur ℝ (v′(x) = 5x⁴ + 2 > 0). Calcule (v⁻¹)′(3).

---

On cherche x₀ = v⁻¹(3), c'est-à-dire x₀ tel que v(x₀) = 3 : v(1) = 1 + 2 = 3, donc x₀ = 1. Puis v′(1) = 5 + 2 = 7, non nul, donc (v⁻¹)′(3) = 1/v′(1) = 1/7. La dérivée s'évalue en x₀ = 1, pas en 3.
:::

::: retenir
(f⁻¹)′(y₀) = 1/f′(f⁻¹(y₀)) quand f′(f⁻¹(y₀)) ≠ 0 ; on calcule f′ à l'antécédent, jamais à y₀.
:::

## 🧭 Dérivée de la réciproque sur un intervalle

On voudrait maintenant toute la fonction (f⁻¹)′ et savoir où elle existe. Prenons f(x) = x³ + 1 sur [0 ; +∞[ : au point (0 ; 1), la courbe de f est horizontale, puisque f′(0) = 0.
Que devient la tangente de f⁻¹ au point symétrique (1 ; 0) ?

::: figure Les courbes de f(x) = x³ + 1 (vert) et de f⁻¹ (bleu) : la tangente horizontale y = 1 en (0 ; 1) a pour symétrique la tangente verticale x = 1 en (1 ; 0)
<svg viewBox="0 0 330 322">
<title>Courbes de x³ + 1 et de ∛(x − 1) : tangente horizontale en (0 ; 1), tangente verticale en (1 ; 0)</title>
<line x1="18" y1="286.8" x2="326" y2="286.8" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="326,286.8 318,290.8 318,282.8" fill="#0f172a"/>
<line x1="53.2" y1="322" x2="53.2" y2="14" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="53.2,14 57.2,22 49.2,22" fill="#0f172a"/>
<line x1="141.2" y1="283.8" x2="141.2" y2="289.8" stroke="#0f172a" stroke-width="1.2"/>
<line x1="229.2" y1="283.8" x2="229.2" y2="289.8" stroke="#0f172a" stroke-width="1.2"/>
<line x1="317.2" y1="283.8" x2="317.2" y2="289.8" stroke="#0f172a" stroke-width="1.2"/>
<line x1="50.2" y1="198.8" x2="56.2" y2="198.8" stroke="#0f172a" stroke-width="1.2"/>
<line x1="50.2" y1="110.8" x2="56.2" y2="110.8" stroke="#0f172a" stroke-width="1.2"/>
<line x1="50.2" y1="22.8" x2="56.2" y2="22.8" stroke="#0f172a" stroke-width="1.2"/>
<line x1="18" y1="322" x2="317.2" y2="22.8" stroke="#64748b" stroke-width="1.6" stroke-dasharray="7 4"/>
<polyline points="53.2,198.8 53.89,198.8 54.59,198.8 55.28,198.8 55.97,198.8 56.66,198.79 57.36,198.79 58.05,198.79 58.74,198.78 59.44,198.77 60.13,198.76 60.82,198.74 61.52,198.73 62.21,198.71 62.9,198.68 63.6,198.65 64.29,198.62 64.98,198.59 65.67,198.55 66.37,198.51 67.06,198.46 67.75,198.4 68.45,198.34 69.14,198.28 69.83,198.21 70.53,198.13 71.22,198.04 71.91,197.95 72.6,197.86 73.3,197.75 73.99,197.64 74.68,197.52 75.38,197.39 76.07,197.26 76.76,197.11 77.46,196.96 78.15,196.79 78.84,196.62 79.53,196.44 80.23,196.25 80.92,196.05 81.61,195.84 82.31,195.62 83,195.38 83.69,195.14 84.39,194.88 85.08,194.62 85.77,194.34 86.46,194.05 87.16,193.74 87.85,193.43 88.54,193.1 89.24,192.76 89.93,192.4 90.62,192.03 91.31,191.65 92.01,191.25 92.7,190.84 93.39,190.41 94.09,189.97 94.78,189.52 95.47,189.05 96.17,188.56 96.86,188.05 97.55,187.53 98.25,187 98.94,186.44 99.63,185.87 100.32,185.29 101.02,184.68 101.71,184.06 102.4,183.42 103.1,182.76 103.79,182.08 104.48,181.38 105.17,180.67 105.87,179.93 106.56,179.18 107.25,178.41 107.95,177.61 108.64,176.8 109.33,175.96 110.03,175.1 110.72,174.23 111.41,173.33 112.1,172.41 112.8,171.46 113.49,170.5 114.18,169.51 114.88,168.5 115.57,167.47 116.26,166.41 116.96,165.33 117.65,164.23 118.34,163.1 119.04,161.95 119.73,160.78 120.42,159.58 121.11,158.35 121.81,157.1 122.5,155.82 123.19,154.52 123.89,153.19 124.58,151.84 125.27,150.46 125.97,149.05 126.66,147.61 127.35,146.15 128.04,144.66 128.74,143.14 129.43,141.6 130.12,140.02 130.82,138.42 131.51,136.79 132.2,135.13 132.9,133.44 133.59,131.72 134.28,129.97 134.97,128.19 135.67,126.38 136.36,124.54 137.05,122.66 137.75,120.76 138.44,118.83 139.13,116.86 139.82,114.86 140.52,112.83 141.21,110.77 141.9,108.67 142.6,106.54 143.29,104.38 143.98,102.18 144.68,99.95 145.37,97.69 146.06,95.39 146.75,93.06 147.45,90.69 148.14,88.29 148.83,85.85 149.53,83.38 150.22,80.87 150.91,78.33 151.61,75.74 152.3,73.13 152.99,70.47 153.69,67.78 154.38,65.05 155.07,62.28 155.76,59.48 156.46,56.63 157.15,53.75 157.84,50.83 158.54,47.87 159.23,44.88 159.92,41.84 160.62,38.76 161.31,35.64 162,32.48 162.69,29.29 163.39,26.05 164.08,22.77" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round"/>
<polyline points="141.2,286.8 141.79,270.24 142.37,265.93 142.96,262.91 143.55,260.51 144.13,258.48 144.72,256.7 145.31,255.12 145.89,253.68 146.48,252.35 147.07,251.12 147.65,249.97 148.24,248.88 148.83,247.86 149.41,246.88 150,245.95 150.59,245.07 151.17,244.21 151.76,243.39 152.35,242.61 152.93,241.84 153.52,241.11 154.11,240.39 154.69,239.7 155.28,239.03 155.87,238.37 156.45,237.73 157.04,237.11 157.63,236.51 158.21,235.92 158.8,235.34 159.39,234.77 159.97,234.22 160.56,233.68 161.15,233.14 161.73,232.62 162.32,232.11 162.91,231.61 163.49,231.12 164.08,230.63 164.67,230.16 165.25,229.69 165.84,229.23 166.43,228.78 167.01,228.33 167.6,227.89 168.19,227.46 168.77,227.03 169.36,226.61 169.95,226.19 170.53,225.78 171.12,225.38 171.71,224.98 172.29,224.59 172.88,224.2 173.47,223.81 174.05,223.44 174.64,223.06 175.23,222.69 175.81,222.32 176.4,221.96 176.99,221.6 177.57,221.25 178.16,220.9 178.75,220.55 179.33,220.21 179.92,219.87 180.51,219.53 181.09,219.2 181.68,218.87 182.27,218.54 182.85,218.22 183.44,217.9 184.03,217.58 184.61,217.27 185.2,216.95 185.79,216.65 186.37,216.34 186.96,216.04 187.55,215.73 188.13,215.44 188.72,215.14 189.31,214.85 189.89,214.55 190.48,214.27 191.07,213.98 191.65,213.69 192.24,213.41 192.83,213.13 193.41,212.85 194,212.58 194.59,212.3 195.17,212.03 195.76,211.76 196.35,211.49 196.93,211.23 197.52,210.96 198.11,210.7 198.69,210.44 199.28,210.18 199.87,209.92 200.45,209.67 201.04,209.42 201.63,209.16 202.21,208.91 202.8,208.66 203.39,208.42 203.97,208.17 204.56,207.93 205.15,207.68 205.73,207.44 206.32,207.2 206.91,206.97 207.49,206.73 208.08,206.49 208.67,206.26 209.25,206.03 209.84,205.79 210.43,205.56 211.01,205.34 211.6,205.11 212.19,204.88 212.77,204.66 213.36,204.43 213.95,204.21 214.53,203.99 215.12,203.77 215.71,203.55 216.29,203.33 216.88,203.11 217.47,202.9 218.05,202.68 218.64,202.47 219.23,202.26 219.81,202.05 220.4,201.84 220.99,201.63 221.57,201.42 222.16,201.21 222.75,201.01 223.33,200.8 223.92,200.6 224.51,200.39 225.09,200.19 225.68,199.99 226.27,199.79 226.85,199.59 227.44,199.39 228.03,199.19 228.61,199 229.2,198.8 229.79,198.6 230.37,198.41 230.96,198.22 231.55,198.02 232.13,197.83 232.72,197.64 233.31,197.45 233.89,197.26 234.48,197.07 235.07,196.89 235.65,196.7 236.24,196.51 236.83,196.33 237.41,196.14 238,195.96 238.59,195.78 239.17,195.59 239.76,195.41 240.35,195.23 240.93,195.05 241.52,194.87 242.11,194.69 242.69,194.51 243.28,194.34 243.87,194.16 244.45,193.98 245.04,193.81 245.63,193.63 246.21,193.46 246.8,193.29 247.39,193.11 247.97,192.94 248.56,192.77 249.15,192.6 249.73,192.43 250.32,192.26 250.91,192.09 251.49,191.92 252.08,191.75 252.67,191.59 253.25,191.42 253.84,191.25 254.43,191.09 255.01,190.92 255.6,190.76 256.19,190.59 256.77,190.43 257.36,190.27 257.95,190.11 258.53,189.94 259.12,189.78 259.71,189.62 260.29,189.46 260.88,189.3 261.47,189.14 262.05,188.98 262.64,188.83 263.23,188.67 263.81,188.51 264.4,188.36 264.99,188.2 265.57,188.04 266.16,187.89 266.75,187.73 267.33,187.58 267.92,187.43 268.51,187.27 269.09,187.12 269.68,186.97 270.27,186.82 270.85,186.67 271.44,186.51 272.03,186.36 272.61,186.21 273.2,186.07 273.79,185.92 274.37,185.77 274.96,185.62 275.55,185.47 276.13,185.32 276.72,185.18 277.31,185.03 277.89,184.89 278.48,184.74 279.07,184.59 279.65,184.45 280.24,184.31 280.83,184.16 281.41,184.02 282,183.87 282.59,183.73 283.17,183.59 283.76,183.45 284.35,183.31 284.93,183.16 285.52,183.02 286.11,182.88 286.69,182.74 287.28,182.6 287.87,182.46 288.45,182.33 289.04,182.19 289.63,182.05 290.21,181.91 290.8,181.77 291.39,181.64 291.97,181.5 292.56,181.36 293.15,181.23 293.73,181.09 294.32,180.96 294.91,180.82 295.49,180.69 296.08,180.55 296.67,180.42 297.25,180.28 297.84,180.15 298.43,180.02 299.01,179.89 299.6,179.75 300.19,179.62 300.77,179.49 301.36,179.36 301.95,179.23 302.53,179.1 303.12,178.97 303.71,178.84 304.29,178.71 304.88,178.58 305.47,178.45 306.05,178.32 306.64,178.19 307.23,178.06 307.81,177.93 308.4,177.81 308.99,177.68 309.57,177.55 310.16,177.43 310.75,177.3 311.33,177.17 311.92,177.05 312.51,176.92 313.09,176.8 313.68,176.67 314.27,176.55 314.85,176.42 315.44,176.3 316.03,176.17 316.61,176.05 317.2,175.93" fill="none" stroke="#2563eb" stroke-width="2.8" stroke-linejoin="round"/>
<line x1="26.8" y1="198.8" x2="141.2" y2="198.8" stroke="#d97706" stroke-width="2.2" stroke-dasharray="7 4"/>
<line x1="141.2" y1="313.2" x2="141.2" y2="198.8" stroke="#d97706" stroke-width="2.2" stroke-dasharray="7 4"/>
<circle cx="53.2" cy="198.8" r="4" fill="#0f172a" stroke="#ffffff" stroke-width="1.2"/>
<circle cx="141.2" cy="286.8" r="4" fill="#0f172a" stroke="#ffffff" stroke-width="1.2"/>
<g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="141.2" y="301.8" text-anchor="middle" fill="#0f172a" font-size="10">1</text><text x="229.2" y="301.8" text-anchor="middle" fill="#0f172a" font-size="10">2</text><text x="317.2" y="301.8" text-anchor="middle" fill="#0f172a" font-size="10">3</text><text x="46.2" y="202.3" text-anchor="end" fill="#0f172a" font-size="10">1</text><text x="46.2" y="114.3" text-anchor="end" fill="#0f172a" font-size="10">2</text><text x="46.2" y="26.3" text-anchor="end" fill="#0f172a" font-size="10">3</text><text x="324" y="278.8" text-anchor="end" fill="#0f172a" font-size="12">x</text><text x="61.2" y="22" text-anchor="start" fill="#0f172a" font-size="12">y</text><text x="62" y="216.4" text-anchor="start" fill="#0f172a" font-size="11">(0 ; 1)</text><text x="150" y="276.24" text-anchor="start" fill="#0f172a" font-size="11">(1 ; 0)</text><text x="97.2" y="71.2" text-anchor="start" fill="#0f6e56" font-size="13">C_f</text><text x="273.2" y="154.8" text-anchor="start" fill="#2563eb" font-size="13">C_f⁻¹</text></g>
</svg>
:::

La droite orange horizontale, tangente en (0 ; 1), devient par symétrie la droite orange verticale en (1 ; 0) : la courbe bleue part à la verticale, donc f⁻¹ n'y a pas de dérivée finie.

::: exemple Dérivée de g⁻¹ sur ]0 ; 20[

1. Sur I = ]0 ; 2[, g′(t) = 10(2 − t) > 0 : g′ ne s'annule pas, et g est une bijection de ]0 ; 2[ sur ]g(0) ; g(2)[ = ]0 ; 20[.
2. On applique (g⁻¹)′(y) = 1/g′(g⁻¹(y)) en tout y de ]0 ; 20[. Comme g⁻¹(y) = 2 − √((20 − y)/5), on a g′(g⁻¹(y)) = 10(2 − g⁻¹(y)) = 10√((20 − y)/5).
3. Donc (g⁻¹)′(y) = 1/(10√((20 − y)/5)) pour y de ]0 ; 20[.
4. Quand y tend vers 20 par la gauche, √((20 − y)/5) tend vers 0 et (g⁻¹)′(y) tend vers +∞ : au sommet de la trajectoire, là où g′(2) = 0, la courbe de g⁻¹ se redresse à la verticale.

:::

::: exemple Le même outil, sans situation : la réciproque de la tangente

1. Soit h(x) = tan x sur ]−π/2 ; π/2[ (une nouvelle fonction h, sans lien avec la hauteur de la balle). h′(x) = 1 + tan²x > 0 et les limites de h en −π/2 et π/2 sont −∞ et +∞ : h est une bijection de ]−π/2 ; π/2[ sur ℝ.
2. h′ ne s'annule pas, donc h⁻¹ est dérivable sur ℝ et (h⁻¹)′(x) = 1/h′(h⁻¹(x)) = 1/(1 + tan²(h⁻¹(x))).
3. Comme tan(h⁻¹(x)) = x (relation h(h⁻¹(x)) = x), on obtient (h⁻¹)′(x) = 1/(1 + x²) pour tout réel x.
4. Application : h⁻¹(1) = π/4 car tan(π/4) = 1, donc (h⁻¹)′(1) = 1/2.

:::

::: piege
**Erreur : croire que f⁻¹ est dérivable partout où f est dérivable et strictement monotone.** f(x) = x³ + 1 sur [0 ; +∞[ est dérivable et strictement croissante, mais f⁻¹(y) = ∛(y − 1) n'est pas dérivable en 1 : le taux (f⁻¹(1 + h) − f⁻¹(1))/h = ∛h / h = 1/∛(h²) tend vers +∞ quand h tend vers 0 par valeurs positives. L'erreur tente parce que f paraît « lisse ». Ce qui compte, c'est que f′(x₀) = f′(0) = 0.
:::

::: propriete
Soit f une bijection de I sur J = f(I). Si f est dérivable sur I et si f′ ne s'annule pas sur I, alors f⁻¹ est dérivable sur J et (f⁻¹)′ = 1/(f′∘f⁻¹).
Cas limite : si f′(x₀) = 0 en un point de I, f⁻¹ n'est pas dérivable en f(x₀). Pour la racine n-ième, f(x) = xⁿ vérifie f′(0) = 0 : x ↦ ⁿ√x est dérivable sur ]0 ; +∞[, pas en 0, et sa dérivée vaut 1/(n(ⁿ√x)ⁿ⁻¹) = ⁿ√x/(n x). Par exemple (∛x)′ en x = 8 vaut ∛8/(3 × 8) = 1/12.
:::

::: verifie À toi : l'expression de (r⁻¹)′
Soit r(x) = x³ + 3x sur ℝ, bijection de ℝ sur ℝ. Exprime (r⁻¹)′(y) à l'aide de r⁻¹(y), puis calcule (r⁻¹)′(4).

---

r′(x) = 3x² + 3 > 0 ne s'annule pas : r⁻¹ est dérivable sur ℝ et (r⁻¹)′(y) = 1/r′(r⁻¹(y)) = 1/(3(r⁻¹(y))² + 3). Pour y = 4 : r(1) = 1 + 3 = 4, donc r⁻¹(4) = 1, puis (r⁻¹)′(4) = 1/(3 × 1² + 3) = 1/6.
:::

::: retenir
Si f′ ne s'annule pas sur I, f⁻¹ est dérivable sur f(I) et (f⁻¹)′ = 1/(f′∘f⁻¹) ; là où f′ s'annule, f⁻¹ a une tangente verticale.
:::

> 🏆 Tu sais maintenant remonter le courant : restreindre pour rendre une fonction bijective, lire l'image d'un intervalle, expliciter la réciproque, la tracer par symétrie, la dériver sans la connaître, et reconnaître où elle se redresse à la verticale.
