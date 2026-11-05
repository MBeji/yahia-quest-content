# ⚔️ Fonctions réciproques — remonter le courant de la fonction

> 💡 «Une fonction t'emmène de x vers y ; sa réciproque est le chemin du retour. Sache quand ce chemin existe, et tu sauras résoudre toute équation f(x) = y.»

Jusqu'ici tu partais de x pour obtenir y. Retourne la question : connaissant y, peux-tu retrouver x, et un seul ? Huit notions te mènent de la bijection à la dérivée des racines nᵉˢ, en passant par la fonction réciproque, son graphique en miroir et sa dérivée. On suppose acquis la continuité et les limites (chapitre 1), la dérivation (chapitre 3) et les équations du second degré.

## 🏰 Bijection : une équation, une seule solution

Soit g(x) = x² + 3. Pour trouver les antécédents de 7, on résout x² + 3 = 7, donc x = 2 ou x = −2 : sur ℝ, il y a deux solutions. Mais si l'on se limite à l'intervalle [0, +∞[, il ne reste que x = 2.
Sur quels intervalles l'équation g(x) = y a-t-elle toujours exactement une solution ?

::: figure La droite y = 7 coupe la parabole en deux points, d'abscisses −2 et 2 ; sur la seule branche verte (x ≥ 0), elle n'en coupe qu'un
<svg viewBox="0 0 340 236">
<title>Parabole y = x² + 3 et droite y = 7 : deux points d'intersection, d'abscisses −2 et 2</title>
<line x1="26" y1="206" x2="314" y2="206" stroke="#0f172a" stroke-width="1.6"/>
<line x1="170" y1="213.5" x2="170" y2="11" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="314,206 306,202 306,210" fill="#0f172a"/>
<polygon points="170,11 166,19 174,19" fill="#0f172a"/>
<polyline points="50,26 52,30.5 54,34.8 56,39.2 58,43.4 60,47.6 62,51.6 64,55.7 66,59.6 68,63.5 70,67.2 72,71 74,74.6 76,78.2 78,81.7 80,85.1 82,88.4 84,91.7 86,94.8 88,98 90,101 92,104 94,106.9 96,109.7 98,112.4 100,115.1 102,117.7 104,120.2 106,122.6 108,125 110,127.2 112,129.5 114,131.6 116,133.7 118,135.6 120,137.6 122,139.4 124,141.2 126,142.8 128,144.5 130,146 132,147.5 134,148.8 136,150.2 138,151.4 140,152.6 142,153.7 144,154.7 146,155.6 148,156.5 150,157.2 152,158 154,158.6 156,159.2 158,159.7 160,160.1 162,160.4 164,160.7 166,160.8 168,161 170,161" fill="none" stroke="#94a3b8" stroke-width="2.2" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="6 3"/>
<polyline points="170,161 172,161 174,160.8 176,160.7 178,160.4 180,160.1 182,159.7 184,159.2 186,158.6 188,158 190,157.2 192,156.5 194,155.6 196,154.7 198,153.7 200,152.6 202,151.4 204,150.2 206,148.8 208,147.5 210,146 212,144.5 214,142.8 216,141.2 218,139.4 220,137.6 222,135.6 224,133.7 226,131.6 228,129.5 230,127.2 232,125 234,122.6 236,120.2 238,117.7 240,115.1 242,112.4 244,109.7 246,106.9 248,104 250,101 252,98 254,94.8 256,91.7 258,88.4 260,85.1 262,81.7 264,78.2 266,74.6 268,71 270,67.2 272,63.5 274,59.6 276,55.7 278,51.6 280,47.6 282,43.4 284,39.2 286,34.8 288,30.5 290,26" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/>
<line x1="34" y1="101" x2="306" y2="101" stroke="#b45309" stroke-width="1.6" stroke-dasharray="6 3"/>
<line x1="90" y1="101" x2="90" y2="206" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="3 3"/>
<line x1="250" y1="101" x2="250" y2="206" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="3 3"/>
<circle cx="90" cy="101" r="4" fill="#0f172a"/>
<circle cx="250" cy="101" r="4" fill="#0f172a"/>
<line x1="90" y1="203" x2="90" y2="209" stroke="#0f172a" stroke-width="1.2"/>
<line x1="250" y1="203" x2="250" y2="209" stroke="#0f172a" stroke-width="1.2"/>
<line x1="167" y1="161" x2="173" y2="161" stroke="#0f172a" stroke-width="1.2"/>
<line x1="167" y1="101" x2="173" y2="101" stroke="#0f172a" stroke-width="1.2"/>
<g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="90" y="220" text-anchor="middle" fill="#0f172a" font-size="11">−2</text><text x="250" y="220" text-anchor="middle" fill="#0f172a" font-size="11">2</text><text x="164" y="165" text-anchor="end" fill="#0f172a" font-size="11">3</text><text x="164" y="105" text-anchor="end" fill="#0f172a" font-size="11">7</text><text x="302" y="95" text-anchor="end" fill="#b45309" font-size="12">y = 7</text><text x="262" y="40" text-anchor="end" fill="#0f6e56" font-size="12">x ≥ 0</text><text x="78" y="40" text-anchor="start" fill="#64748b" font-size="12">x ≤ 0</text></g>
</svg>
:::

::: definition
**Bijection** — Soit I un intervalle de ℝ et f une fonction définie sur I. On dit que f réalise une bijection de I sur f(I) si, pour tout y de f(I), l'équation f(x) = y admet une unique solution dans I.
:::

::: exemple Les antécédents de g sur [0, +∞[

1. g′(x) = 2x > 0 sur ]0, +∞[ : g est strictement croissante sur [0, +∞[, avec g(0) = 3 et g(x) → +∞ quand x → +∞. Donc g([0, +∞[) = [3, +∞[.
2. Pour y ≥ 3, g(x) = y équivaut à x² = y − 3, d'où x = √(y − 3) ou x = −√(y − 3). Seule la première est positive : l'équation a une unique solution dans [0, +∞[, donc g réalise une bijection de [0, +∞[ sur [3, +∞[.
3. Pour h(x) = √(x − 3) sur [3, +∞[ et y ≥ 0, h(x) = y équivaut à x = y² + 3, qui est bien dans [3, +∞[ : h est aussi une bijection, de [3, +∞[ sur [0, +∞[.
4. On vérifie g∘h(x) = (√(x − 3))² + 3 = x pour x ≥ 3 et h∘g(x) = √(x²) = x pour x ≥ 0 : chaque fonction défait l'autre.

:::

::: piege
**Erreur : prendre [f(a), f(b)] pour l'image d'un intervalle sans vérifier la monotonie.** Pour f(x) = x² sur [−2, 1], on calcule f(−2) = 4 et f(1) = 1 et l'on écrit f([−2, 1]) = [1, 4]. L'erreur tente parce qu'elle marche pour une fonction croissante. Mais f(0) = 0 est plus petit que 1 : f décroît puis croît, et l'image est [0, 4]. En outre f(−1) = f(1) = 1 : l'équation f(x) = 1 a deux solutions dans [−2, 1], donc f n'est pas une bijection de [−2, 1].
:::

::: propriete
**Théorème** : si f est strictement monotone sur un intervalle I, alors f réalise une bijection de I sur f(I). En effet, deux réels distincts de I ont des images distinctes, donc l'unicité est acquise ; l'existence vient de ce que y est pris dans f(I).
**Image d'un intervalle** (f continue, strictement croissante) : f([a, b]) = [f(a), f(b)] ; f([a, b[) = [f(a), lim_{x→b⁻} f(x)[ ; f(]a, b[) = ]lim_{x→a⁺} f(x), lim_{x→b⁻} f(x)[. Si f est strictement décroissante, on échange les deux bornes.
Cas limite : la continuité seule ne suffit pas. Une fonction continue sur [1, +∞[ avec f(1) = 2 et f(x) → 3 en +∞ peut monter puis redescendre et reprendre deux fois la même valeur : elle ne réalise pas forcément une bijection sur [2, 3[.
:::

::: verifie À toi : bijection et image
Montrer que f(x) = x² + 2x réalise une bijection de I = ]−∞, −1] sur un intervalle J à préciser.

---

f′(x) = 2x + 2 < 0 sur ]−∞, −1[ : f est strictement décroissante sur I, donc bijective de I sur f(I). On échange les bornes : f(−1) = −1 et f(x) → +∞ quand x → −∞, d'où J = [−1, +∞[.
:::

::: retenir
f strictement monotone sur I ⟹ f bijection de I sur f(I) ; l'image se lit avec les valeurs et les limites aux bornes, bornes échangées si f décroît.
:::

## 🗝️ La fonction réciproque, le chemin du retour

Reprenons g(x) = x² + 3 sur [0, +∞[ : chaque y ≥ 3 a un seul antécédent. La machine qui, à y, renvoie cet antécédent existe donc : c'est y ↦ √(y − 3), la fonction h de la section précédente.
Comment la construire quand on ne la devine pas ?

::: definition
**Fonction réciproque** — Soit f une bijection d'un intervalle I sur f(I). On appelle fonction réciproque de f, et on note f⁻¹, la fonction définie sur f(I) qui, à tout y de f(I), associe l'unique solution dans I de l'équation f(x) = y.
**Conséquence** : pour tout x de I et tout y de f(I), f(x) = y si et seulement si f⁻¹(y) = x ; f⁻¹∘f(x) = x pour tout x de I et f∘f⁻¹(y) = y pour tout y de f(I).
:::

::: exemple Expliciter la réciproque de √(1 + x²)

1. g(x) = √(1 + x²) sur [0, +∞[ : g′(x) = x/√(1 + x²) > 0 sur ]0, +∞[, g(0) = 1 et g(x) → +∞. Donc g est une bijection de [0, +∞[ sur [1, +∞[.
2. On part de y = g(x) avec y ≥ 1 : y² = 1 + x², donc x² = y² − 1.
3. On garde la seule solution positive, puisque x doit être dans [0, +∞[ : x = √(y² − 1).
4. Ainsi g⁻¹(y) = √(y² − 1) sur [1, +∞[. Vérification : g(2) = √5 et g⁻¹(√5) = √4 = 2 ✓.

:::

::: exemple Une fonction égale à sa propre réciproque

1. f(x) = 1/x est strictement décroissante sur ]0, +∞[, et f(]0, +∞[) = ]0, +∞[ : c'est une bijection de ]0, +∞[ sur lui-même.
2. De y = 1/x on tire x = 1/y : f⁻¹(y) = 1/y, donc f⁻¹ = f.
3. Autrement dit f∘f(x) = x pour tout x > 0 : appliquer f deux fois ramène au point de départ.

:::

::: piege
**Erreur : garder les deux solutions ou confondre f⁻¹ et 1/f.** Pour g(x) = √(1 + x²), on écrit g⁻¹(y) = ±√(y² − 1). L'erreur tente parce que l'équation du second degré a deux racines. Mais la racine négative n'est pas dans I = [0, +∞[ : une réciproque est une fonction, avec une seule valeur par y. Autre confusion : g⁻¹(√5) = 2, alors que 1/g(√5) = 1/√6 ; la notation −1 en exposant ne désigne pas un inverse multiplicatif.
:::

::: propriete
**Méthode** : pour expliciter f⁻¹, on part de y = f(x), on résout en x, puis on garde la seule solution qui appartient à I. On écrit le résultat avec y variable de f(I).
Cas limite : pour f(x) = 1/x, la résolution donne x = 1/y sans aucune racine à choisir ; mais pour une fonction du second degré, le choix de la bonne racine dépend toujours de I.
:::

::: verifie À toi : expliciter f⁻¹
Expliciter la réciproque de f(x) = x² + 2x sur I = ]−∞, −1].

---

On a vu que f est une bijection de I sur [−1, +∞[. De y = (x + 1)² − 1 on tire (x + 1)² = y + 1, donc x + 1 = ±√(y + 1). Comme x ≤ −1, x + 1 ≤ 0 : on garde le signe moins, d'où f⁻¹(y) = −1 − √(y + 1). Vérification : f(−4) = 16 − 8 = 8 et f⁻¹(8) = −1 − 3 = −4 ✓.
:::

::: retenir
f(x) = y ⟺ f⁻¹(y) = x ; pour expliciter f⁻¹, on résout y = f(x) en x et on garde la solution qui est dans I.
:::

## 🪞 Deux courbes, un seul miroir : la droite Δ : y = x

Le point M(2, 7) est sur la courbe de g(x) = x² + 3, puisque g(2) = 7. Comme h(7) = √4 = 2, le point M′(7, 2) est sur la courbe de h. Les coordonnées de M et de M′ sont échangées.
Que peut-on dire des deux courbes, dans un repère orthonormé ?

::: figure Les courbes de g (vert) et de h (orange) se déduisent l'une de l'autre en repliant le plan le long de Δ : M(2 ; 7) devient M′(7 ; 2)
<svg viewBox="0 0 320 268">
<title>Courbes de g (x ↦ x² + 3 sur [0 ; +∞[) et de h (x ↦ √(x − 3) sur [3 ; +∞[), symétriques par rapport à la droite y = x</title>
<line x1="27" y1="244" x2="300" y2="244" stroke="#0f172a" stroke-width="1.6"/>
<line x1="36" y1="256" x2="36" y2="7" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="300,244 292,240 292,248" fill="#0f172a"/>
<polygon points="36,7 32,15 40,15" fill="#0f172a"/>
<line x1="36" y1="244" x2="264" y2="16" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="6 4"/>
<polyline points="36,154 37.5,153.9 39,153.7 40.5,153.3 42,152.8 43.5,152.1 45,151.3 46.5,150.3 48,149.2 49.5,147.9 51,146.5 52.5,144.9 54,143.2 55.5,141.3 57,139.3 58.5,137.1 60,134.8 61.5,132.3 63,129.7 64.5,126.9 66,124 67.5,120.9 69,117.7 70.5,114.3 72,110.8 73.5,107.1 75,103.3 76.5,99.3 78,95.2 79.5,90.9 81,86.5 82.5,81.9 84,77.2 85.5,72.3 87,67.3 88.5,62.1 90,56.8 91.5,51.3 93,45.7 94.5,39.9 96,34 97.5,27.9 99,21.7" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/>
<polyline points="126,244 129,234.5 132,230.6 135,227.6 138,225 141,222.8 144,220.8 147,218.9 150,217.2 153,215.5 156,214 159,212.5 162,211.1 165,209.8 168,208.5 171,207.3 174,206.1 177,204.9 180,203.8 183,202.6 186,201.6 189,200.5 192,199.5 195,198.5 198,197.5 201,196.6 204,195.6 207,194.7 210,193.8 213,192.9 216,192 219,191.2 222,190.3 225,189.5 228,188.7 231,187.9 234,187.1 237,186.3 240,185.5 243,184.8 246,184 249,183.3 252,182.5 255,181.8 258,181.1 261,180.4 264,179.7 267,179 270,178.3 273,177.6 276,176.9 279,176.3 282,175.6 285,174.9 288,174.3 291,173.6" fill="none" stroke="#b45309" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/>
<line x1="96" y1="34" x2="246" y2="184" stroke="#0f172a" stroke-width="1.2" stroke-dasharray="3 3"/>
<circle cx="96" cy="34" r="4" fill="#0f172a"/>
<circle cx="246" cy="184" r="4" fill="#0f172a"/>
<line x1="66" y1="241" x2="66" y2="247" stroke="#0f172a" stroke-width="1.2"/>
<line x1="96" y1="241" x2="96" y2="247" stroke="#0f172a" stroke-width="1.2"/>
<line x1="126" y1="241" x2="126" y2="247" stroke="#0f172a" stroke-width="1.2"/>
<line x1="156" y1="241" x2="156" y2="247" stroke="#0f172a" stroke-width="1.2"/>
<line x1="186" y1="241" x2="186" y2="247" stroke="#0f172a" stroke-width="1.2"/>
<line x1="216" y1="241" x2="216" y2="247" stroke="#0f172a" stroke-width="1.2"/>
<line x1="246" y1="241" x2="246" y2="247" stroke="#0f172a" stroke-width="1.2"/>
<line x1="276" y1="241" x2="276" y2="247" stroke="#0f172a" stroke-width="1.2"/>
<line x1="33" y1="214" x2="39" y2="214" stroke="#0f172a" stroke-width="1.2"/>
<line x1="33" y1="184" x2="39" y2="184" stroke="#0f172a" stroke-width="1.2"/>
<line x1="33" y1="154" x2="39" y2="154" stroke="#0f172a" stroke-width="1.2"/>
<line x1="33" y1="124" x2="39" y2="124" stroke="#0f172a" stroke-width="1.2"/>
<line x1="33" y1="94" x2="39" y2="94" stroke="#0f172a" stroke-width="1.2"/>
<line x1="33" y1="64" x2="39" y2="64" stroke="#0f172a" stroke-width="1.2"/>
<line x1="33" y1="34" x2="39" y2="34" stroke="#0f172a" stroke-width="1.2"/>
<g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="66" y="258" text-anchor="middle" fill="#0f172a" font-size="11">1</text><text x="96" y="258" text-anchor="middle" fill="#0f172a" font-size="11">2</text><text x="126" y="258" text-anchor="middle" fill="#0f172a" font-size="11">3</text><text x="156" y="258" text-anchor="middle" fill="#0f172a" font-size="11">4</text><text x="186" y="258" text-anchor="middle" fill="#0f172a" font-size="11">5</text><text x="216" y="258" text-anchor="middle" fill="#0f172a" font-size="11">6</text><text x="246" y="258" text-anchor="middle" fill="#0f172a" font-size="11">7</text><text x="276" y="258" text-anchor="middle" fill="#0f172a" font-size="11">8</text><text x="30" y="218" text-anchor="end" fill="#0f172a" font-size="11">1</text><text x="30" y="188" text-anchor="end" fill="#0f172a" font-size="11">2</text><text x="30" y="158" text-anchor="end" fill="#0f172a" font-size="11">3</text><text x="30" y="128" text-anchor="end" fill="#0f172a" font-size="11">4</text><text x="30" y="98" text-anchor="end" fill="#0f172a" font-size="11">5</text><text x="30" y="68" text-anchor="end" fill="#0f172a" font-size="11">6</text><text x="30" y="38" text-anchor="end" fill="#0f172a" font-size="11">7</text><text x="89" y="31" text-anchor="end" fill="#0f172a" font-size="13">M</text><text x="242" y="208" text-anchor="start" fill="#0f172a" font-size="13">M′</text><text x="76.5" y="115" text-anchor="start" fill="#0f6e56" font-size="13">C_g</text><text x="192" y="218" text-anchor="start" fill="#b45309" font-size="13">C_h</text><text x="222" y="34" text-anchor="start" fill="#64748b" font-size="12">Δ : y = x</text></g>
</svg>
:::

::: propriete
**Symétrie des courbes** : dans un repère orthonormé, les courbes d'une bijection f et de sa réciproque f⁻¹ sont symétriques par rapport à la droite Δ : y = x. En effet, M(x, y) appartient à C_f si et seulement si y = f(x) avec x ∈ I, c'est-à-dire x = f⁻¹(y) avec y ∈ f(I), c'est-à-dire M′(y, x) appartient à C_{f⁻¹}.
:::

::: exemple Lire la courbe de h « à l'envers »

1. Sur la courbe de g, on lit g(0) = 3, g(1) = 4 et g(2) = 7.
2. Par l'équivalence f(x) = y ⟺ f⁻¹(y) = x, on en tire h(3) = 0, h(4) = 1 et h(7) = 2, sans calcul de racine.
3. Les deux courbes sont symétriques, mais la droite y = x ne les coupe pas : x² + 3 = x n'a pas de solution, car son discriminant 1 − 12 est négatif.

:::

::: piege
**Erreur : lire f⁻¹(7) en regardant l'abscisse 7 de la courbe de g.** L'erreur tente parce qu'on lit toujours une courbe de gauche à droite. Mais on cherche l'antécédent de 7, c'est-à-dire l'abscisse du point d'ordonnée 7 : c'est 2. Regarder l'abscisse 7 donne g(7) = 52, une toute autre quantité.
:::

::: propriete
Le tableau de variation de f⁻¹ s'obtient en échangeant les lignes de x et de f(x). La symétrie échange aussi les axes : une asymptote horizontale y = ℓ de C_f devient une asymptote verticale x = ℓ de C_{f⁻¹}, et une asymptote verticale x = ℓ devient horizontale y = ℓ. Si f(a) = a, le point (a, a) est sur C_f et sur C_{f⁻¹}.
Cas limite : cette symétrie suppose un repère orthonormé ; dans un repère dont les unités diffèrent, les deux courbes ne se déduisent plus l'une de l'autre par un pliage.
:::

::: verifie À toi : miroir
Une bijection f vérifie f(4) = 4 et sa courbe passe par A(1, 5). Quels points sont sur la courbe de f⁻¹ ?

---

On échange les coordonnées. A(1, 5) donne le point (5, 1), puisque f(1) = 5 équivaut à f⁻¹(5) = 1. Le point (4, 4) est sur Δ : il est son propre symétrique, et il appartient aux deux courbes.
:::

::: retenir
Dans un repère orthonormé, C_{f⁻¹} est le symétrique de C_f par rapport à Δ : y = x ; (a, b) ∈ C_f ⟺ (b, a) ∈ C_{f⁻¹} ; les asymptotes échangent leur direction.
:::

## 🧭 Réciproque d'une fonction continue strictement monotone

Sur [−π/2, π/2], la fonction sin est croissante, de −1 à 1. Tu sais que sin(π/6) = 1/2 ; inversement, l'angle de [−π/2, π/2] dont le sinus vaut 1/2 est π/6.
La fonction qui, à un sinus, rend l'angle est-elle continue ? Croît-elle aussi ?

::: propriete
**Théorème** : si f est continue et strictement monotone sur un intervalle I, alors sa réciproque f⁻¹ est continue et strictement monotone sur l'intervalle f(I), et varie dans le même sens que f.
La continuité de f⁻¹ est admise. Pour la monotonie, si f est croissante et si l'on avait y₁ < y₂ avec f⁻¹(y₁) ≥ f⁻¹(y₂), la croissance de f donnerait y₁ ≥ y₂, contradiction.
:::

::: exemple Les valeurs de la réciproque du sinus

1. f(x) = sin x sur I = [−π/2, π/2] : f′(x) = cos x > 0 sur ]−π/2, π/2[, donc f est strictement croissante, continue, et f(I) = [−1, 1].
2. f⁻¹ est donc continue et strictement croissante sur [−1, 1].
3. On lit les valeurs sur le cercle trigonométrique, en restant dans [−π/2, π/2] : f⁻¹(1/2) = π/6, f⁻¹(−√3/2) = −π/3, f⁻¹(√2/2) = π/4, f⁻¹(1) = π/2. Vérification : sin(−π/3) = −√3/2 ✓.

:::

::: piege
**Erreur : croire que la réciproque inverse le sens de variation.** Pour f(x) = x² + 3 croissante sur [0, +∞[, on affirme que sa réciproque est décroissante, « puisque c'est l'inverse ». L'erreur tente à cause du mot. Mais h(x) = √(x − 3) vérifie h(4) = 1 < h(7) = 2 : elle est croissante comme f. La symétrie par rapport à Δ conserve le sens de parcours des courbes. « Même sens » ne veut d'ailleurs pas dire « même signe » : f(x) = x + 10 est positive sur [−1, 1] alors que f⁻¹(y) = y − 10 change de signe sur [9, 11].
:::

::: verifie À toi : le sens de variation
f(x) = 2 + 1/x sur ]0, +∞[. Donner f(I), la réciproque et son sens de variation.

---

f′(x) = −1/x² < 0 : f est continue et strictement décroissante, avec f(x) → +∞ en 0⁺ et f(x) → 2 en +∞, donc f(I) = ]2, +∞[. De y = 2 + 1/x on tire x = 1/(y − 2) : f⁻¹(y) = 1/(y − 2) sur ]2, +∞[. Elle est décroissante, comme f, ce que confirme sa dérivée −1/(y − 2)² < 0.
:::

::: retenir
f continue et strictement monotone sur I ⟹ f⁻¹ continue et strictement monotone sur f(I), dans le même sens que f.
:::

## ⚡ Dériver la réciproque sans jamais l'expliciter

La tangente à la courbe de g(x) = x² + 3 au point M(2, 7) a pour pente g′(2) = 4. Le pliage sur Δ échange les axes : la tangente en M′(7, 2) à la courbe de h doit avoir une pente 1/4. Et c'est bien le cas : h′(x) = 1/(2√(x − 3)) donne h′(7) = 1/4.
Peut-on obtenir cette pente sans connaître h ?

::: propriete
**Théorème** : soit f une bijection d'un intervalle ouvert I sur f(I), a un réel de I et b = f(a). Si f est dérivable en a et si f′(a) ≠ 0, alors f⁻¹ est dérivable en b et (f⁻¹)′(b) = 1/f′(a).
**Corollaire** : si f est dérivable sur I et si f′(x) ≠ 0 pour tout x de I, alors f⁻¹ est dérivable sur f(I) et (f⁻¹)′(y) = 1/f′(f⁻¹(y)) pour tout y de f(I).
Dans ces formules, a = f⁻¹(b) : il faut d'abord retrouver a.
:::

::: exemple Un nombre dérivé sans expression de f⁻¹

1. f(x) = x/(1 + x²) sur [1, +∞[ : f′(x) = (1 − x²)/(1 + x²)² < 0 sur ]1, +∞[, f(1) = 1/2 et f(x) → 0. Donc f est une bijection de [1, +∞[ sur ]0, 1/2].
2. On veut (f⁻¹)′(3/10). On cherche a tel que f(a) = 3/10 : 10a = 3 + 3a², soit 3a² − 10a + 3 = 0, de racines 3 et 1/3. Seule a = 3 est dans [1, +∞[.
3. f′(3) = (1 − 9)/10² = −2/25, non nul.
4. Donc (f⁻¹)′(3/10) = 1/f′(3) = −25/2. Vérification par l'expression f⁻¹(y) = (1 + √(1 − 4y²))/(2y) : le calcul direct en y = 3/10 redonne −25/2 ✓.

:::

::: piege
**Erreur : dériver au mauvais point.** Pour g(x) = x² + 3 sur [0, +∞[, on veut (g⁻¹)′(7) et l'on écrit 1/g′(7) = 1/14. L'erreur tente parce qu'on cherche « la dérivée en 7 ». Mais la formule est 1/g′(a) avec a = g⁻¹(7) = 2 : (g⁻¹)′(7) = 1/g′(2) = 1/4, ce qui concorde avec h′(7) = 1/4 trouvé plus haut.
:::

Si f′(a) = 0, la tangente à C_f au point d'abscisse a est horizontale ; par symétrie, la tangente à C_{f⁻¹} est verticale et f⁻¹ n'est pas dérivable en b. C'est le cas pour f = cos sur [0, π], qui est une bijection de [0, π] sur [−1, 1].

::: figure Les demi-tangentes horizontales de C_f en (0 ; 1) et en (π ; −1) deviennent des demi-tangentes verticales de C_{f⁻¹} en (1 ; 0) et en (−1 ; π)
<svg viewBox="0 0 270 262">
<title>Courbe de cos sur [0 ; π] et courbe de sa réciproque, symétriques par rapport à y = x ; les tangentes horizontales de la première deviennent verticales pour la seconde</title>
<line x1="6" y1="184" x2="230.4" y2="184" stroke="#0f172a" stroke-width="1.6"/>
<line x1="72" y1="245.6" x2="72" y2="25.6" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="230.4,184 222.4,180 222.4,188" fill="#0f172a"/>
<polygon points="72,25.6 68,33.6 76,33.6" fill="#0f172a"/>
<line x1="14.8" y1="241.2" x2="217.2" y2="38.8" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="6 4"/>
<polyline points="72,140 74.3,140.1 76.6,140.2 78.9,140.5 81.2,141 83.5,141.5 85.8,142.2 88.1,142.9 90.4,143.8 92.7,144.8 95,145.9 97.3,147.1 99.6,148.4 101.9,149.8 104.3,151.3 106.6,152.9 108.9,154.6 111.2,156.3 113.5,158.1 115.8,160 118.1,162 120.4,164 122.7,166.1 125,168.2 127.3,170.4 129.6,172.6 131.9,174.9 134.2,177.1 136.5,179.4 138.8,181.7 141.1,184 143.4,186.3 145.7,188.6 148,190.9 150.3,193.1 152.6,195.4 154.9,197.6 157.2,199.8 159.5,201.9 161.8,204 164.2,206 166.5,208 168.8,209.9 171.1,211.7 173.4,213.4 175.7,215.1 178,216.7 180.3,218.2 182.6,219.6 184.9,220.9 187.2,222.1 189.5,223.2 191.8,224.2 194.1,225.1 196.4,225.8 198.7,226.5 201,227 203.3,227.5 205.6,227.8 207.9,227.9 210.2,228" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/>
<polyline points="116,184 115.9,181.7 115.8,179.4 115.5,177.1 115,174.8 114.5,172.5 113.8,170.2 113.1,167.9 112.2,165.6 111.2,163.3 110.1,161 108.9,158.7 107.6,156.4 106.2,154.1 104.7,151.7 103.1,149.4 101.4,147.1 99.7,144.8 97.9,142.5 96,140.2 94,137.9 92,135.6 89.9,133.3 87.8,131 85.6,128.7 83.4,126.4 81.1,124.1 78.9,121.8 76.6,119.5 74.3,117.2 72,114.9 69.7,112.6 67.4,110.3 65.1,108 62.9,105.7 60.6,103.4 58.4,101.1 56.2,98.8 54.1,96.5 52,94.2 50,91.8 48,89.5 46.1,87.2 44.3,84.9 42.6,82.6 40.9,80.3 39.3,78 37.8,75.7 36.4,73.4 35.1,71.1 33.9,68.8 32.8,66.5 31.8,64.2 30.9,61.9 30.2,59.6 29.5,57.3 29,55 28.5,52.7 28.2,50.4 28.1,48.1 28,45.8" fill="none" stroke="#b45309" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/>
<line x1="72" y1="140" x2="87.4" y2="140" stroke="#7c3aed" stroke-width="2.2"/>
<line x1="194.8" y1="228" x2="210.2" y2="228" stroke="#7c3aed" stroke-width="2.2"/>
<line x1="116" y1="184" x2="116" y2="168.6" stroke="#7c3aed" stroke-width="2.2"/>
<line x1="28" y1="61.2" x2="28" y2="45.8" stroke="#7c3aed" stroke-width="2.2"/>
<circle cx="72" cy="140" r="4" fill="#0f172a"/>
<circle cx="210.2" cy="228" r="4" fill="#0f172a"/>
<circle cx="116" cy="184" r="4" fill="#0f172a"/>
<circle cx="28" cy="45.8" r="4" fill="#0f172a"/>
<line x1="116" y1="181" x2="116" y2="187" stroke="#0f172a" stroke-width="1.2"/>
<line x1="28" y1="181" x2="28" y2="187" stroke="#0f172a" stroke-width="1.2"/>
<line x1="210.2" y1="181" x2="210.2" y2="187" stroke="#0f172a" stroke-width="1.2"/>
<line x1="69" y1="140" x2="75" y2="140" stroke="#0f172a" stroke-width="1.2"/>
<line x1="69" y1="228" x2="75" y2="228" stroke="#0f172a" stroke-width="1.2"/>
<line x1="69" y1="45.8" x2="75" y2="45.8" stroke="#0f172a" stroke-width="1.2"/>
<g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="116" y="199" text-anchor="middle" fill="#0f172a" font-size="11">1</text><text x="28" y="199" text-anchor="middle" fill="#0f172a" font-size="11">−1</text><text x="210.2" y="199" text-anchor="middle" fill="#0f172a" font-size="11">π</text><text x="66" y="144" text-anchor="end" fill="#0f172a" font-size="11">1</text><text x="66" y="232" text-anchor="end" fill="#0f172a" font-size="11">−1</text><text x="66" y="49.8" text-anchor="end" fill="#0f172a" font-size="11">π</text><text x="178.8" y="213.8" text-anchor="start" fill="#0f6e56" font-size="13">C_f</text><text x="40" y="87.2" text-anchor="start" fill="#b45309" font-size="13">C_f⁻¹</text><text x="221.6" y="39.2" text-anchor="start" fill="#64748b" font-size="12">Δ</text></g>
</svg>
:::

::: exemple Dérivabilité de la réciproque du cosinus

1. f′(x) = −sin x < 0 sur ]0, π[ : f est strictement décroissante, de f(0) = 1 à f(π) = −1.
2. En 0 : f⁻¹(0) = π/2 et f′(π/2) = −1 ≠ 0, donc (f⁻¹)′(0) = 1/(−1) = −1.
3. Sur ]−1, 1[ : a = f⁻¹(y) est dans ]0, π[ où sin a > 0, donc sin a = √(1 − y²) et (f⁻¹)′(y) = −1/√(1 − y²).
4. En 1 et −1, f′(0) = f′(π) = 0 : C_{f⁻¹} a une demi-tangente verticale à gauche en 1 et à droite en −1, donc f⁻¹ n'est pas dérivable en ces points.

:::

::: propriete
Quand f′(a) ≠ 0, f⁻¹ est dérivable en f(a) de nombre dérivé 1/f′(a). Quand f′(a) = 0 (tangente horizontale), la courbe de f⁻¹ a une tangente verticale en f(a) et f⁻¹ n'y est pas dérivable. Réciproquement, une tangente verticale de C_f (taux d'accroissement de limite infinie) donne une tangente horizontale de C_{f⁻¹} : f⁻¹ est dérivable de nombre dérivé 0.
Cas limite : si a est une extrémité de I, on raisonne sur la demi-tangente, du côté où f est définie.
:::

::: verifie À toi : un nombre dérivé
f(x) = 2x³ + x sur ℝ est une bijection de ℝ sur ℝ. Calculer (f⁻¹)′(3).

---

On cherche a tel que f(a) = 3 : f(1) = 2 + 1 = 3, donc a = 1. Puis f′(x) = 6x² + 1 > 0 et f′(1) = 7. D'où (f⁻¹)′(3) = 1/7, sans résoudre l'équation du troisième degré.
:::

::: retenir
(f⁻¹)′(b) = 1/f′(a) avec a = f⁻¹(b) et f′(a) ≠ 0 ; si f′(a) = 0, la courbe de f⁻¹ a une tangente verticale en b.
:::

## 🔮 La fonction racine nᵉ

Un cube plein a un volume V = a³ (en cm³). La fonction a ↦ a³ est strictement croissante de [0, +∞[ sur [0, +∞[ : à chaque volume correspond une seule arête. Pour V = 125, l'arête est 5, puisque 5³ = 125.
Quel nom donner à la fonction qui, au volume, associe l'arête ?

::: definition
**Fonction racine nᵉ** — Soit n un entier supérieur ou égal à 2. La fonction x ↦ xⁿ réalise une bijection de ℝ₊ sur ℝ₊ ; sa réciproque, strictement croissante de ℝ₊ sur ℝ₊, est appelée fonction racine nᵉ.
**Notation** : l'image d'un réel positif x est notée ⁿ√x et se lit « racine nᵉ de x ». Pour n = 2, ²√x = √x.
**Conséquence** : pour tous réels positifs x et y, y = xⁿ si et seulement si x = ⁿ√y.
:::

::: exemple Calculer des racines nᵉˢ

1. ∛343 : on cherche x ≥ 0 tel que x³ = 343 ; 7³ = 343, donc ∛343 = 7.
2. ⁴√81 : 3⁴ = 81, donc ⁴√81 = 3.
3. ⁶√(2⁻¹²) : (2⁻²)⁶ = 2⁻¹² avec 2⁻² > 0, donc ⁶√(2⁻¹²) = 2⁻² = 1/4.

:::

::: piege
**Erreur : diviser par n au lieu de chercher une puissance.** On écrit ⁴√16 = 16/4 = 4. L'erreur tente à cause de la ressemblance avec « racine carrée = moitié ». Mais ⁴√16 est le réel positif x tel que x⁴ = 16 : c'est 2, car 2⁴ = 16, alors que 4⁴ = 256. Autre piège : ⁿ√ ne s'applique qu'à des réels positifs, donc ∛(−8) n'a pas de sens ici.
:::

::: propriete
Pour x ≥ 0, ⁿ√(xⁿ) = x et (ⁿ√x)ⁿ = x, car les deux fonctions xⁿ et ⁿ√x sont réciproques l'une de l'autre sur ℝ₊. La fonction ⁿ√ est continue et strictement croissante sur [0, +∞[.
Cas limite : ⁿ√0 = 0 et ⁿ√1 = 1, quel que soit n.
:::

::: verifie À toi : racines nᵉˢ
Calculer ⁵√243 et ⁶√(1/64).

---

3⁵ = 243 et 3 > 0, donc ⁵√243 = 3. Puis (1/2)⁶ = 1/64 et 1/2 > 0, donc ⁶√(1/64) = 1/2.
:::

::: retenir
ⁿ√ est la réciproque de x ↦ xⁿ sur ℝ₊ : y = xⁿ ⟺ x = ⁿ√y, pour x et y positifs.
:::

## 🧮 Opérations sur les radicaux

Un cube de volume 54 cm³ a pour arête ∛54 ≈ 3,78 cm. Comme 54 = 27 × 2 et 27 = 3³, on peut espérer une écriture plus simple.
Comment calculer avec les racines nᵉˢ sans calculatrice ?

::: propriete
**Opérations sur les radicaux** : soit deux entiers n ≥ 2 et p ≥ 2, et deux réels positifs a et b. Alors ⁿ√(aⁿ) = a ; (ⁿ√a)ⁿ = a ; ⁿ√(a·b) = ⁿ√a·ⁿ√b ; ⁿ√(a/b) = ⁿ√a/ⁿ√b si b ≠ 0 ; ⁿ√a = ⁿᵖ√(aᵖ) ; (ⁿ√a)ᵖ = ⁿ√(aᵖ) ; ⁿ√(ᵖ√a) = ⁿᵖ√a.
Elles découlent de la définition : par exemple, (ⁿ√a·ⁿ√b)ⁿ = a·b, donc ⁿ√a·ⁿ√b est la racine nᵉ de a·b.
:::

::: exemple Simplifier et comparer

1. ∛54 = ∛(27 × 2) = ∛27 × ∛2 = 3∛2, car 3³ = 27 : on extrait le cube parfait.
2. √(∛729) = ⁶√729 = ⁶√(3⁶) = 3, en composant les racines.
3. ∛(2√2) = √2, car (√2)³ = 2√2.
4. Comparer ⁶√(2⁴) et ⁴√(2³) : on met au même indice 12 = PPCM(6, 4). ⁶√(2⁴) = ¹²√((2⁴)²) = ¹²√(2⁸) et ⁴√(2³) = ¹²√((2³)³) = ¹²√(2⁹). Comme 2⁸ < 2⁹ et que ¹²√ est croissante, ⁶√(2⁴) < ⁴√(2³).
5. Résoudre ⁴√x = ∛2 dans ℝ₊ : x = (∛2)⁴ = ∛(2⁴) = ∛16 = 2∛2. Vérification : ⁴√(2∛2) = ∛2, car (∛2)⁴ = 2∛2 ✓.

:::

::: piege
**Erreur : ⁿ√(a + b) = ⁿ√a + ⁿ√b.** On écrit ∛(1 + 7) = ∛1 + ∛7. L'erreur tente parce que la racine ressemble à une multiplication par un facteur. Mais ∛(1 + 7) = ∛8 = 2, alors que ∛1 + ∛7 ≈ 1 + 1,91 = 2,91. Les règles portent sur les produits et les quotients, jamais sur les sommes. Autre piège : la comparaison de deux radicaux dépend de la position de x par rapport à 1 (voir la section suivante).
:::

::: verifie À toi : comparer deux racines
Comparer ∛3 et ⁴√5.

---

On met au même indice 12 : ∛3 = ¹²√(3⁴) = ¹²√81 et ⁴√5 = ¹²√(5³) = ¹²√125. Comme 81 < 125 et que ¹²√ est croissante, ∛3 < ⁴√5.
:::

::: retenir
Les racines nᵉˢ se multiplient et se divisent, mais ne s'additionnent pas ; pour comparer, on met au même indice avec ⁿ√a = ⁿᵖ√(aᵖ).
:::

## 📐 Dérivée de x ↦ ⁿ√x et étude de ∛x, ⁴√x, ⁶√x

Un cube de volume V a pour arête a(V) = ∛V. Si V passe de 125 à 125,1 cm³, l'arête passe de 5 cm à un peu plus de 5,0013 cm.
À quelle vitesse l'arête croît-elle avec le volume ?

::: propriete
**Théorème** : pour tout entier n ≥ 2, la fonction f : x ↦ ⁿ√x est continue sur [0, +∞[ et dérivable sur ]0, +∞[, avec f′(x) = 1/(n·ⁿ√(xⁿ⁻¹)) pour tout x > 0.
**Démonstration** : f est la réciproque de g(x) = xⁿ, dérivable avec g′(x) = nxⁿ⁻¹ qui ne s'annule pas sur ]0, +∞[ ; donc f′(x) = 1/g′(f(x)) = 1/(n·(ⁿ√x)ⁿ⁻¹) = 1/(n·ⁿ√(xⁿ⁻¹)).
:::

::: exemple La vitesse de l'arête et un nombre dérivé

1. Pour n = 3 en x = 125 : f′(125) = 1/(3·∛(125²)) = 1/(3 × 25) = 1/75, car ∛(125²) = 5² = 25.
2. Contrôle : 0,1/75 ≈ 0,0013, ce qui donne bien 5,0013 pour ∛125,1.
3. La limite lim_{x→81} (⁴√x − 3)/(x − 81) est le nombre dérivé de ⁴√ en 81, c'est-à-dire 1/(4·⁴√(81³)) = 1/(4 × 27) = 1/108.

:::

**En 0**, le taux d'accroissement de ⁿ√ est ⁿ√x/x = 1/ⁿ√(xⁿ⁻¹), qui tend vers +∞ quand x → 0⁺ : la fonction n'est pas dérivable à droite en 0, et sa courbe y admet une demi-tangente verticale. C'est cohérent avec la section précédente : la tangente de x ↦ xⁿ en 0 est horizontale.

::: figure Les courbes de ∛x, ⁴√x et ⁶√x partent de l'origine avec une tangente verticale et se croisent en (1 ; 1) : au-delà de 1, ⁶√x est la plus basse ; avant 1, c'est la plus haute
<svg viewBox="0 0 342 205">
<title>Courbes de x ↦ ∛x, ⁴√x et ⁶√x sur [0 ; 3] : elles passent par (0 ; 0) et (1 ; 1), tangente verticale en 0</title>
<line x1="25.4" y1="176" x2="335" y2="176" stroke="#0f172a" stroke-width="1.6"/>
<line x1="34" y1="184.6" x2="34" y2="16.9" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="335,176 327,172 327,180" fill="#0f172a"/>
<polygon points="34,16.9 30,24.9 38,24.9" fill="#0f172a"/>
<line x1="120" y1="90" x2="120" y2="176" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="3 3"/>
<polyline points="34,176 34.4,161.3 34.9,157.5 35.3,154.8 35.7,152.7 36.1,150.9 36.6,149.3 37,147.9 37.4,146.6 37.9,145.4 38.3,144.3 38.7,143.3 39.2,142.3 39.6,141.4 40,140.6 40.5,139.7 40.9,138.9 41.3,138.2 41.7,137.5 42.2,136.8 42.6,136.1 43,135.4 43.5,134.8 43.9,134.2 44.3,133.6 44.8,133 45.2,132.4 45.6,131.9 46,131.3 46.5,130.8 46.9,130.3 47.3,129.8 47.8,129.3 48.2,128.8 48.6,128.4 49,127.9 49.5,127.4 49.9,127 50.3,126.6 50.8,126.1 51.2,125.7 52.9,124.1 54.6,122.6 56.4,121.1 58.1,119.7 59.8,118.4 61.5,117.2 63.2,116 65,114.8 66.7,113.7 68.4,112.6 70.1,111.6 71.8,110.6 73.6,109.6 75.3,108.7 77,107.7 78.7,106.8 80.4,106 82.2,105.1 83.9,104.3 85.6,103.5 87.3,102.7 89,101.9 90.8,101.1 92.5,100.4 94.2,99.6 95.9,98.9 97.6,98.2 99.4,97.5 101.1,96.8 102.8,96.2 104.5,95.5 106.2,94.9 108,94.2 109.7,93.6 111.4,93 113.1,92.4 114.8,91.8 116.6,91.2 118.3,90.6 120,90 121.7,89.4 123.4,88.9 125.2,88.3 126.9,87.8 128.6,87.2 130.3,86.7 132,86.2 133.8,85.6 135.5,85.1 137.2,84.6 138.9,84.1 140.6,83.6 142.4,83.1 144.1,82.6 145.8,82.1 147.5,81.7 149.2,81.2 151,80.7 152.7,80.3 154.4,79.8 156.1,79.3 157.8,78.9 159.6,78.4 161.3,78 163,77.6 164.7,77.1 166.4,76.7 168.2,76.3 169.9,75.8 171.6,75.4 173.3,75 175,74.6 176.8,74.2 178.5,73.8 180.2,73.4 181.9,73 183.6,72.6 185.4,72.2 187.1,71.8 188.8,71.4 190.5,71 192.2,70.6 194,70.2 195.7,69.9 197.4,69.5 199.1,69.1 200.8,68.7 202.6,68.4 204.3,68 206,67.6 207.7,67.3 209.4,66.9 211.2,66.6 212.9,66.2 214.6,65.9 216.3,65.5 218,65.2 219.8,64.8 221.5,64.5 223.2,64.1 224.9,63.8 226.6,63.5 228.4,63.1 230.1,62.8 231.8,62.5 233.5,62.2 235.2,61.8 237,61.5 238.7,61.2 240.4,60.9 242.1,60.5 243.8,60.2 245.6,59.9 247.3,59.6 249,59.3 250.7,59 252.4,58.7 254.2,58.4 255.9,58 257.6,57.7 259.3,57.4 261,57.1 262.8,56.8 264.5,56.5 266.2,56.2 267.9,56 269.6,55.7 271.4,55.4 273.1,55.1 274.8,54.8 276.5,54.5 278.2,54.2 280,53.9 281.7,53.6 283.4,53.4 285.1,53.1 286.8,52.8 288.6,52.5 290.3,52.2 292,52" fill="none" stroke="#7c3aed" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"/>
<polyline points="34,176 34.4,153.1 34.9,148.8 35.3,145.9 35.7,143.7 36.1,141.8 36.6,140.2 37,138.8 37.4,137.5 37.9,136.4 38.3,135.3 38.7,134.4 39.2,133.4 39.6,132.6 40,131.8 40.5,131 40.9,130.3 41.3,129.6 41.7,128.9 42.2,128.3 42.6,127.6 43,127 43.5,126.5 43.9,125.9 44.3,125.4 44.8,124.9 45.2,124.4 45.6,123.9 46,123.4 46.5,122.9 46.9,122.5 47.3,122 47.8,121.6 48.2,121.2 48.6,120.8 49,120.4 49.5,120 49.9,119.6 50.3,119.2 50.8,118.9 51.2,118.5 52.9,117.1 54.6,115.8 56.4,114.6 58.1,113.4 59.8,112.4 61.5,111.3 63.2,110.3 65,109.4 66.7,108.5 68.4,107.6 70.1,106.8 71.8,106 73.6,105.2 75.3,104.4 77,103.7 78.7,103 80.4,102.3 82.2,101.6 83.9,100.9 85.6,100.3 87.3,99.7 89,99.1 90.8,98.5 92.5,97.9 94.2,97.3 95.9,96.8 97.6,96.2 99.4,95.7 101.1,95.2 102.8,94.7 104.5,94.2 106.2,93.7 108,93.2 109.7,92.7 111.4,92.2 113.1,91.8 114.8,91.3 116.6,90.9 118.3,90.4 120,90 121.7,89.6 123.4,89.2 125.2,88.7 126.9,88.3 128.6,87.9 130.3,87.5 132,87.1 133.8,86.7 135.5,86.4 137.2,86 138.9,85.6 140.6,85.2 142.4,84.9 144.1,84.5 145.8,84.2 147.5,83.8 149.2,83.5 151,83.1 152.7,82.8 154.4,82.5 156.1,82.1 157.8,81.8 159.6,81.5 161.3,81.1 163,80.8 164.7,80.5 166.4,80.2 168.2,79.9 169.9,79.6 171.6,79.3 173.3,79 175,78.7 176.8,78.4 178.5,78.1 180.2,77.8 181.9,77.5 183.6,77.2 185.4,76.9 187.1,76.7 188.8,76.4 190.5,76.1 192.2,75.8 194,75.6 195.7,75.3 197.4,75 199.1,74.8 200.8,74.5 202.6,74.2 204.3,74 206,73.7 207.7,73.5 209.4,73.2 211.2,73 212.9,72.7 214.6,72.5 216.3,72.2 218,72 219.8,71.7 221.5,71.5 223.2,71.3 224.9,71 226.6,70.8 228.4,70.6 230.1,70.3 231.8,70.1 233.5,69.9 235.2,69.6 237,69.4 238.7,69.2 240.4,69 242.1,68.7 243.8,68.5 245.6,68.3 247.3,68.1 249,67.9 250.7,67.6 252.4,67.4 254.2,67.2 255.9,67 257.6,66.8 259.3,66.6 261,66.4 262.8,66.2 264.5,66 266.2,65.8 267.9,65.6 269.6,65.4 271.4,65.2 273.1,65 274.8,64.8 276.5,64.6 278.2,64.4 280,64.2 281.7,64 283.4,63.8 285.1,63.6 286.8,63.4 288.6,63.2 290.3,63 292,62.8" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"/>
<polyline points="34,176 34.4,140.4 34.9,136.1 35.3,133.3 35.7,131.2 36.1,129.5 36.6,128.1 37,126.8 37.4,125.7 37.9,124.7 38.3,123.8 38.7,123 39.2,122.2 39.6,121.5 40,120.8 40.5,120.2 40.9,119.5 41.3,119 41.7,118.4 42.2,117.9 42.6,117.4 43,116.9 43.5,116.5 43.9,116 44.3,115.6 44.8,115.2 45.2,114.8 45.6,114.4 46,114 46.5,113.7 46.9,113.3 47.3,113 47.8,112.6 48.2,112.3 48.6,112 49,111.7 49.5,111.4 49.9,111.1 50.3,110.8 50.8,110.5 51.2,110.2 52.9,109.2 54.6,108.2 56.4,107.3 58.1,106.4 59.8,105.6 61.5,104.9 63.2,104.2 65,103.5 66.7,102.8 68.4,102.2 70.1,101.6 71.8,101 73.6,100.4 75.3,99.9 77,99.4 78.7,98.9 80.4,98.4 82.2,97.9 83.9,97.5 85.6,97 87.3,96.6 89,96.2 90.8,95.8 92.5,95.4 94.2,95 95.9,94.6 97.6,94.2 99.4,93.8 101.1,93.5 102.8,93.1 104.5,92.8 106.2,92.5 108,92.1 109.7,91.8 111.4,91.5 113.1,91.2 114.8,90.9 116.6,90.6 118.3,90.3 120,90 121.7,89.7 123.4,89.4 125.2,89.2 126.9,88.9 128.6,88.6 130.3,88.4 132,88.1 133.8,87.8 135.5,87.6 137.2,87.3 138.9,87.1 140.6,86.9 142.4,86.6 144.1,86.4 145.8,86.2 147.5,85.9 149.2,85.7 151,85.5 152.7,85.3 154.4,85 156.1,84.8 157.8,84.6 159.6,84.4 161.3,84.2 163,84 164.7,83.8 166.4,83.6 168.2,83.4 169.9,83.2 171.6,83 173.3,82.8 175,82.6 176.8,82.4 178.5,82.2 180.2,82 181.9,81.9 183.6,81.7 185.4,81.5 187.1,81.3 188.8,81.1 190.5,81 192.2,80.8 194,80.6 195.7,80.5 197.4,80.3 199.1,80.1 200.8,80 202.6,79.8 204.3,79.6 206,79.5 207.7,79.3 209.4,79.1 211.2,79 212.9,78.8 214.6,78.7 216.3,78.5 218,78.4 219.8,78.2 221.5,78.1 223.2,77.9 224.9,77.8 226.6,77.6 228.4,77.5 230.1,77.3 231.8,77.2 233.5,77.1 235.2,76.9 237,76.8 238.7,76.6 240.4,76.5 242.1,76.4 243.8,76.2 245.6,76.1 247.3,75.9 249,75.8 250.7,75.7 252.4,75.5 254.2,75.4 255.9,75.3 257.6,75.2 259.3,75 261,74.9 262.8,74.8 264.5,74.6 266.2,74.5 267.9,74.4 269.6,74.3 271.4,74.1 273.1,74 274.8,73.9 276.5,73.8 278.2,73.7 280,73.5 281.7,73.4 283.4,73.3 285.1,73.2 286.8,73.1 288.6,73 290.3,72.8 292,72.7" fill="none" stroke="#b45309" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"/>
<circle cx="120" cy="90" r="4" fill="#0f172a"/>
<line x1="120" y1="173" x2="120" y2="179" stroke="#0f172a" stroke-width="1.2"/>
<line x1="206" y1="173" x2="206" y2="179" stroke="#0f172a" stroke-width="1.2"/>
<line x1="292" y1="173" x2="292" y2="179" stroke="#0f172a" stroke-width="1.2"/>
<line x1="31" y1="90" x2="37" y2="90" stroke="#0f172a" stroke-width="1.2"/>
<g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="120" y="190" text-anchor="middle" fill="#0f172a" font-size="11">1</text><text x="206" y="190" text-anchor="middle" fill="#0f172a" font-size="11">2</text><text x="292" y="190" text-anchor="middle" fill="#0f172a" font-size="11">3</text><text x="28" y="94" text-anchor="end" fill="#0f172a" font-size="11">1</text><text x="296" y="49" text-anchor="start" fill="#7c3aed" font-size="12">∛x</text><text x="296" y="65.8" text-anchor="start" fill="#0f6e56" font-size="12">⁴√x</text><text x="296" y="84.7" text-anchor="start" fill="#b45309" font-size="12">⁶√x</text></g>
</svg>
:::

Chacune de ces trois fonctions est continue et strictement croissante sur [0, +∞[, dérivable sur ]0, +∞[ avec une dérivée positive. Elles tendent vers +∞ : pour tout A > 0, ⁿ√x ≥ A dès que x ≥ Aⁿ. Écrites avec l'indice 12, ⁶√x = ¹²√(x²), ⁴√x = ¹²√(x³) et ∛x = ¹²√(x⁴) : pour x > 1 on a x² < x³ < x⁴, donc ⁶√x < ⁴√x < ∛x, et c'est l'inverse pour 0 < x < 1.

::: piege
**Erreur : croire que ⁿ√ est dérivable partout où elle est définie.** On écrit « ∛x est définie et continue en 0, donc dérivable en 0 ». L'erreur tente parce qu'on associe continuité et dérivabilité. Mais le taux ∛x/x = 1/∛(x²) tend vers +∞ : il y a une demi-tangente verticale. De même, « ⁴√x ≥ ∛x pour tout x > 0 » est faux : pour x = 16, ⁴√16 = 2 mais ∛16 ≈ 2,52.
:::

::: verifie À toi : un nombre dérivé de racine
Calculer le nombre dérivé de x ↦ ⁶√x en 64.

---

f′(64) = 1/(6·⁶√(64⁵)). Comme 64 = 2⁶, ⁶√(64⁵) = ⁶√(2³⁰) = 2⁵ = 32. Donc f′(64) = 1/(6 × 32) = 1/192.
:::

::: retenir
(ⁿ√x)′ = 1/(n·ⁿ√(xⁿ⁻¹)) pour x > 0 ; ⁿ√ n'est pas dérivable à droite en 0 (demi-tangente verticale).
:::

> 🏆 Quatrième porte franchie, héros : tu sais reconnaître une bijection, construire et lire f⁻¹, la tracer par un pliage sur Δ : y = x, la dériver sans l'écrire, et tu as gagné les racines nᵉˢ pour les études de fonctions du bac.
