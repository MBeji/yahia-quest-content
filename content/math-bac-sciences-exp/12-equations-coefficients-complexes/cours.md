# ⚔️ Équations à coefficients complexes — quand chaque équation trouve ses racines

> 💡 «Dans ℝ, une équation peut rester sans réponse ; dans ℂ, elle en trouve autant que son degré, pourvu qu'on sache les chercher.»

Ce chapitre prolonge les nombres complexes : on résout zⁿ = 1 puis zⁿ = a, on extrait des racines carrées, on résout le second degré à coefficients complexes, on factorise les degrés supérieurs et l'on suit des solutions qui dépendent d'un paramètre θ. Huit notions, des racines de l'unité jusqu'aux lieux de points. Le plan est rapporté à un repère orthonormé direct (O, u⃗, v⃗) et l'on emploie l'écriture exponentielle du chapitre précédent.

## 🔄 Racines nièmes de l'unité et le nombre j

Dans ℝ, l'équation x³ = 1 n'a qu'une solution, 1. Dans ℂ, le nombre j = (−1 + i√3)/2 la vérifie aussi : j² = (−1 − i√3)/2, puis j³ = j² × j = (1 + 3)/4 = 1.
Combien de complexes z vérifient zⁿ = 1, et où sont-ils dans le plan ?

::: definition
Soit n un entier, n ≥ 2. On appelle **racine nième de l'unité** tout complexe z tel que zⁿ = 1.
Exemples : 1 et −1 sont les racines carrées de l'unité ; 1, i, −1 et −i sont les racines quatrièmes de l'unité.
:::

::: figure Les six solutions de z⁶ = 1 sont les sommets d'un hexagone régulier inscrit dans le cercle trigonométrique, deux sommets voisins étant séparés de l'angle π/3
<svg viewBox="0 0 300 260">
<title>Les six solutions de z⁶ = 1 : sommets d'un hexagone régulier inscrit dans le cercle trigonométrique, espacés de l'angle π/3</title>
<path d="M10 130 H290" fill="none" stroke="#0f172a" stroke-width="1.6"/>
<path d="M150 250 V10" fill="none" stroke="#0f172a" stroke-width="1.6"/>
<path d="M290 130 l-8 -4 l0 8 z" fill="#0f172a"/>
<path d="M150 10 l-4 8 l8 0 z" fill="#0f172a"/>
<path d="M250 127 V133" stroke="#0f172a" stroke-width="1.2"/>
<text x="258" y="148" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">1</text>
<path d="M50 127 V133" stroke="#0f172a" stroke-width="1.2"/>
<text x="50" y="146" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">−1</text>
<path d="M147 30 H153" stroke="#0f172a" stroke-width="1.2"/>
<text x="140" y="22" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">i</text>
<path d="M147 230 H153" stroke="#0f172a" stroke-width="1.2"/>
<text x="143" y="234" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">−i</text>
<text x="144" y="145" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">O</text>
<circle cx="150" cy="130" r="100" fill="none" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="5 4"/>
<path d="M250 130 L200 43.4 L100 43.4 L50 130 L100 216.6 L200 216.6 Z" fill="#0f6e56" opacity="0.1"/>
<path d="M250 130 L200 43.4 L100 43.4 L50 130 L100 216.6 L200 216.6 Z" fill="none" stroke="#0f6e56" stroke-width="2" stroke-linejoin="round"/>
<path d="M150 130 L250 130" fill="none" stroke="#b45309" stroke-width="2.2"/>
<path d="M150 130 L200 43.4" fill="none" stroke="#b45309" stroke-width="2.2"/>
<path d="M180 130 A30 30 0 0 0 165 104" fill="none" stroke="#b45309" stroke-width="1.6"/>
<circle cx="250" cy="130" r="4" fill="#0f6e56"/>
<circle cx="200" cy="43.4" r="4" fill="#0f6e56"/>
<circle cx="100" cy="43.4" r="4" fill="#0f6e56"/>
<circle cx="50" cy="130" r="4" fill="#0f6e56"/>
<circle cx="100" cy="216.6" r="4" fill="#0f6e56"/>
<circle cx="200" cy="216.6" r="4" fill="#0f6e56"/>
<text x="182" y="114" text-anchor="start" font-size="11" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">π/3</text>
<text x="258" y="124" text-anchor="start" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">z₀ = 1</text>
<text x="206" y="35.4" text-anchor="start" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">z₁</text>
<text x="94" y="35.4" text-anchor="end" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">z₂</text>
<text x="42" y="124" text-anchor="end" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">z₃ = −1</text>
<text x="94" y="234.6" text-anchor="end" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">z₄</text>
<text x="206" y="234.6" text-anchor="start" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">z₅</text>
</svg>
:::

Sur la figure, les six points sont à la distance 1 de O et chacun s'obtient du précédent en tournant de π/3 = 2π/6.

::: exemple Résoudre z⁶ = 1 et sommer les solutions

1. D'après la propriété ci-dessous, avec n = 6, les solutions sont z_k = e^(i2kπ/6) = e^(ikπ/3), pour k ∈ {0 ; 1 ; … ; 5}.
2. On les écrit : z₀ = 1, z₁ = e^(iπ/3), z₂ = e^(i2π/3), z₃ = e^(iπ) = −1, z₄ = e^(i4π/3) et z₅ = e^(i5π/3).
3. Il y a exactement six solutions, chacune étant la précédente tournée de π/3.
4. Leur somme est nulle. En effet z_k = z₁^k, donc 1 + z₁ + … + z₁⁵ = (z₁⁶ − 1)/(z₁ − 1) = 0, car z₁⁶ = 1 et z₁ ≠ 1. Contrôle : z₁ + z₅ = 2cos(π/3) = 1, z₂ + z₄ = 2cos(2π/3) = −1 et 1 + z₃ = 0, soit 1 − 1 + 0 = 0 ✓.

:::

::: piege
**Erreur : prendre pour arguments kπ/n au lieu de 2kπ/n.** L'erreur tente parce que π/n « partage le demi-tour » et que l'on retient « diviser par n ». Mais pour n = 6, le nombre e^(iπ/6) a pour puissance sixième e^(iπ) = −1, et non 1. Le tour complet est 2π : les arguments des racines de l'unité sont les multiples de 2π/n.
:::

::: propriete
Pour tout entier n ≥ 2, l'équation zⁿ = 1 admet exactement n solutions distinctes :
$$ z_k = e^(i2kπ/n),  k ∈ {0 ; 1 ; … ; n − 1} $$
Pour n ≥ 3, leurs images sont les sommets d'un polygone régulier à n côtés inscrit dans le cercle trigonométrique.
Cas limite : n = 2 donne 1 et −1 (deux points, pas de polygone).
Le cas n = 3 donne 1, j et j², avec j = e^(i2π/3) = (−1 + i√3)/2 : j³ = 1, j² = j̄ = (−1 − i√3)/2, 1 + j + j² = 0, et pour tout entier naturel n : j^(3n) = 1, j^(3n+1) = j, j^(3n+2) = j̄.
:::

::: verifie À toi : les racines huitièmes de l'unité
Résoudre z⁸ = 1, puis donner la solution d'argument 3π/4 sous forme algébrique.

---

On a z_k = e^(i2kπ/8) = e^(ikπ/4) pour k = 0, 1, …, 7 : ce sont les sommets d'un octogone régulier. La solution d'argument 3π/4 est z₃ = cos(3π/4) + i sin(3π/4) = (−√2 + i√2)/2. Contrôle : z₃⁸ = e^(i6π) = 1 ✓.
:::

::: retenir
zⁿ = 1 a exactement n solutions e^(i2kπ/n), k = 0, …, n − 1, sommets d'un polygone régulier inscrit dans le cercle trigonométrique ; j = e^(i2π/3) vérifie j³ = 1 et 1 + j + j² = 0.
:::

## 🔶 Racines nièmes d'un complexe

Le nombre 2e^(iπ/6) a pour cube 8e^(iπ/2) = 8i. C'est donc une solution de z³ = 8i.
Comment trouver toutes les autres, sachant maintenant résoudre z³ = 1 ?

::: definition
Soient n ≥ 2 un entier et a un complexe non nul. On appelle **racine nième** de a tout complexe z tel que zⁿ = a.
Exemple : −2i est une racine cubique de 8i, car (−2i)³ = −8i³ = 8i.
:::

::: figure Les trois solutions de z³ = 8i sont sur le cercle de centre O et de rayon 2 et forment un triangle équilatéral ; z₀ a pour argument π/6
<svg viewBox="0 0 320 266">
<title>Les trois solutions de z³ = 8i : √3 + i, −√3 + i et −2i, sommets d'un triangle équilatéral inscrit dans le cercle de centre O et de rayon 2</title>
<path d="M10 130 H310" fill="none" stroke="#0f172a" stroke-width="1.6"/>
<path d="M160 256 V4" fill="none" stroke="#0f172a" stroke-width="1.6"/>
<path d="M310 130 l-8 -4 l0 8 z" fill="#0f172a"/>
<path d="M160 4 l-4 8 l8 0 z" fill="#0f172a"/>
<path d="M220 127 V133" stroke="#0f172a" stroke-width="1.2"/>
<text x="220" y="146" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">1</text>
<path d="M280 127 V133" stroke="#0f172a" stroke-width="1.2"/>
<text x="280" y="146" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">2</text>
<path d="M100 127 V133" stroke="#0f172a" stroke-width="1.2"/>
<text x="100" y="146" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">−1</text>
<path d="M40 127 V133" stroke="#0f172a" stroke-width="1.2"/>
<text x="40" y="146" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">−2</text>
<path d="M157 70 H163" stroke="#0f172a" stroke-width="1.2"/>
<text x="153" y="74" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">i</text>
<path d="M157 10 H163" stroke="#0f172a" stroke-width="1.2"/>
<text x="153" y="14" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">2i</text>
<path d="M157 190 H163" stroke="#0f172a" stroke-width="1.2"/>
<text x="153" y="194" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">−i</text>
<text x="154" y="145" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">O</text>
<circle cx="160" cy="130" r="120" fill="none" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="5 4"/>
<path d="M263.9 70 L56.1 70 L160 250 Z" fill="#0f6e56" opacity="0.1"/>
<path d="M263.9 70 L56.1 70 L160 250 Z" fill="none" stroke="#0f6e56" stroke-width="2" stroke-linejoin="round"/>
<path d="M160 130 L263.9 70" fill="none" stroke="#b45309" stroke-width="2.2"/>
<path d="M208 130 A48 48 0 0 0 201.6 106" fill="none" stroke="#b45309" stroke-width="1.6"/>
<circle cx="263.9" cy="70" r="4" fill="#0f6e56"/>
<circle cx="56.1" cy="70" r="4" fill="#0f6e56"/>
<circle cx="160" cy="250" r="4" fill="#0f6e56"/>
<text x="212.4" y="115.6" text-anchor="start" font-size="11" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">π/6</text>
<text x="263.9" y="60" text-anchor="middle" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">z₀ = √3 + i</text>
<text x="56.1" y="60" text-anchor="middle" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">z₁ = −√3 + i</text>
<text x="170" y="256" text-anchor="start" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">z₂ = −2i</text>
</svg>
:::

Sur la figure, les points sont à la distance 2 de O et espacés de 2π/3, comme les racines cubiques de l'unité, mais le triangle a tourné de π/6.

::: exemple Résoudre z³ = 8i

1. Une solution est z′ = 2e^(iπ/6) : son module vérifie 2³ = 8 et son argument est le tiers de π/2, argument de 8i.
2. On a z³ = 8i = z′³, donc (z/z′)³ = 1 : z/z′ est une racine cubique de l'unité, soit z/z′ = e^(i2kπ/3) avec k ∈ {0 ; 1 ; 2}.
3. Alors z_k = 2e^(i(π/6 + 2kπ/3)) : z₀ = 2e^(iπ/6) = √3 + i, z₁ = 2e^(i5π/6) = −√3 + i et z₂ = 2e^(i3π/2) = −2i.
4. Contrôle : (−2i)³ = 8i ✓. Le côté du triangle vaut |z₀ − z₁| = |2√3| = 2√3, c'est-à-dire le rayon multiplié par √3.

:::

::: piege
**Erreur : prendre pour module |a|/n.** L'erreur tente parce qu'on « divise tout par n » pour l'argument. Mais le module de z vérifie |z|ⁿ = |a|. Pour z³ = 64, le module n'est pas 64/3 : il vaut 4, car 4³ = 64. Le module se traite par une puissance, l'argument par une division.
:::

::: propriete
Soient a un complexe non nul d'argument θ et n ≥ 2 un entier. On note r le réel strictement positif tel que rⁿ = |a|. L'équation zⁿ = a admet exactement n solutions distinctes :
$$ z_k = r e^(i(θ/n + 2kπ/n)),  k ∈ {0 ; 1 ; … ; n − 1} $$
Pour n ≥ 3, leurs images sont les sommets d'un polygone régulier inscrit dans le cercle de centre O et de rayon r. Son côté vaut |z₁ − z₀| = 2r sin(π/n) : r√3 pour n = 3, r√2 pour n = 4 et r pour n = 6.
Cas limite : pour n = 2, on trouve deux solutions opposées : tout complexe non nul a deux racines carrées opposées.
:::

::: verifie À toi : les racines quatrièmes de −4
Résoudre z⁴ = −4 sous forme exponentielle, puis algébrique, et donner le côté du carré formé par leurs images.

---

On a |−4| = 4, donc r⁴ = 4 et r = √2 ; l'argument de −4 est π, donc θ/4 = π/4. Alors z_k = √2 e^(i(π/4 + kπ/2)) : z₀ = √2 e^(iπ/4) = 1 + i, z₁ = −1 + i, z₂ = −1 − i et z₃ = 1 − i. Le côté vaut |z₁ − z₀| = 2, soit r√2 = √2 × √2 ✓. Contrôle : (1 + i)⁴ = (2i)² = −4 ✓.
:::

::: retenir
zⁿ = a, avec a non nul, a exactement n solutions r e^(i(θ/n + 2kπ/n)) où rⁿ = |a| : les sommets d'un polygone régulier inscrit dans le cercle de rayon r ; on ramène l'équation à zⁿ = 1 en divisant par une solution.
:::

## 🔍 Racines carrées d'un complexe

Le cas n = 2 est déjà réglé quand on connaît le module et l'argument. Mais pour d = 3 − 4i, l'argument n'est pas un angle usuel.
Existe-t-il un moyen de trouver z tel que z² = 3 − 4i en restant en forme algébrique ?

::: exemple Les racines carrées de d = 3 − 4i

On pose z = x + iy avec x et y réels, donc z² = x² − y² + 2ixy.

1. Deux complexes égaux ont mêmes parties réelle et imaginaire : z² = d donne x² − y² = 3 et 2xy = −4.
2. On ajoute une équation tirée du module, car |z²| = |z|² : x² + y² = |d| = √(9 + 16) = 5.
3. En additionnant puis en soustrayant : 2x² = 8, donc x² = 4 ; 2y² = 2, donc y² = 1. Ainsi x = ±2 et y = ±1.
4. Le produit 2xy = −4 est négatif, donc x et y sont de signes contraires : on garde (2 ; −1) et (−2 ; 1). Les racines carrées sont 2 − i et −2 + i. Contrôle : (2 − i)² = 4 − 4i − 1 = 3 − 4i ✓.

:::

::: piege
**Erreur : garder les quatre couples (±2 ; ±1).** L'erreur tente parce que x² = 4 et y² = 1 laissent quatre combinaisons de signes. Mais l'équation 2xy = −4 en écarte deux : (2 + i)² = 3 + 4i, ce qui n'est pas d. Un complexe non nul n'a que deux racines carrées.
:::

::: exemple Par l'écriture exponentielle : les racines carrées de −4i

1. On a −4i = 4e^(−iπ/2), donc le module de z vérifie |z|² = 4, soit |z| = 2, et son argument est −π/4.
2. Alors z₁ = 2e^(−iπ/4) = 2(√2/2 − i√2/2) = √2 − i√2, et z₂ = −z₁ = −√2 + i√2. Contrôle : (√2 − i√2)² = 2 − 4i − 2 = −4i ✓.

:::

::: methode Trouver les racines carrées de d = a + ib
1. Poser z = x + iy : l'équation z² = d entraîne le système
$$ x² − y² = a ;  2xy = b ;  x² + y² = |d| $$
2. Ajouter et retrancher la première et la troisième relation pour obtenir x², puis y², donc x et y au signe près.
3. Parmi les quatre couples de signes (±x ; ±y), le signe de 2xy = b n'en garde que deux : z et −z, les deux racines carrées, opposées l'une de l'autre. Si d = r e^(iθ), elles valent √r e^(iθ/2) et son opposée.

Cas limites : un réel négatif −c a pour racines carrées i√c et −i√c (2xy = 0 et x² − y² < 0 imposent x = 0) ; pour d = 0, la seule racine carrée est 0.
:::

::: verifie À toi : racines carrées de 12 − 16i
Trouver les racines carrées de 12 − 16i.

---

On a |d| = √(144 + 256) = 20, donc x² − y² = 12 et x² + y² = 20, d'où x² = 16 et y² = 4. Comme 2xy = −16 < 0, x et y sont de signes contraires : les racines carrées sont 4 − 2i et −4 + 2i. Contrôle : (4 − 2i)² = 16 − 16i − 4 = 12 − 16i ✓.
:::

::: retenir
Pour z² = a + ib, on résout x² − y² = a, 2xy = b et x² + y² = |d| ; il y a deux racines carrées opposées, et le signe de 2xy dit si x et y ont le même signe ou des signes contraires.
:::

## 🧮 Le second degré dans ℂ

Pour résoudre z² + 2iz − 7/4 − i = 0, on peut reconnaître un début de carré : (z + i)² = z² + 2iz − 1.
Si l'on sait extraire une racine carrée, cette idée résout-elle toute équation du second degré, même avec des coefficients complexes ?

::: exemple Compléter le carré dans z² + 2iz − 7/4 − i = 0

1. On a z² + 2iz = (z + i)² + 1, donc l'équation s'écrit (z + i)² + 1 − 7/4 − i = 0, soit (z + i)² = 3/4 + i = (3 + 4i)/4.
2. Or ((2 + i)/2)² = (4 + 4i − 1)/4 = (3 + 4i)/4. Les racines carrées de (3 + 4i)/4 sont donc ±(2 + i)/2.
3. Ainsi z + i = ±(2 + i)/2, d'où z = 1 − i/2 ou z = −1 − 3i/2. Contrôle de z = 1 − i/2 : z² = 3/4 − i et 2iz = 2i + 1, donc z² + 2iz − 7/4 − i = 3/4 − i + 2i + 1 − 7/4 − i = 0 ✓.

:::

::: exemple Résoudre z² − (1 − i)z + 2 − 2i = 0 avec le discriminant

1. Ici a = 1, b = −(1 − i) et c = 2 − 2i : Δ = (1 − i)² − 4(2 − 2i) = −2i − 8 + 8i = −8 + 6i.
2. On cherche une racine carrée δ de Δ : x² − y² = −8, 2xy = 6 et x² + y² = |Δ| = 10, d'où x² = 1, y² = 9 et xy > 0, donc δ = 1 + 3i. Contrôle : (1 + 3i)² = 1 + 6i − 9 = −8 + 6i ✓.
3. On applique z = (−b ± δ)/(2a) : z′ = ((1 − i) + (1 + 3i))/2 = 1 + i et z″ = ((1 − i) − (1 + 3i))/2 = −2i.
4. Contrôle par réinjection de z′ : (1 + i)² = 2i et (1 − i)(1 + i) = 2, donc 2i − 2 + 2 − 2i = 0 ✓.

:::

::: piege
**Erreur : développer (1 − i)² comme 1² − i².** L'erreur tente parce que l'on retient « le carré d'une différence » sans le double produit. Cela donnerait (1 − i)² = 1 + 1 = 2 et Δ = 2 − 8 + 8i = −6 + 8i, dont les racines carrées ±√2(1 + 2i) conduisent à des solutions qui ne vérifient pas l'équation. Mais (1 − i)² = 1 − 2i + i² = −2i : le terme −2i est le double produit, et c'est lui qui fait réussir le calcul.
:::

::: propriete
Soit az² + bz + c = 0, avec a, b et c complexes, a ≠ 0, et Δ = b² − 4ac. L'équation admet deux solutions, éventuellement confondues :
$$ z₁ = (−b + δ)/(2a)  et  z₂ = (−b − δ)/(2a) $$
où δ est une racine carrée de Δ ; l'autre racine carrée −δ échange simplement z₁ et z₂. De plus az² + bz + c = a(z − z₁)(z − z₂).
Cas limites : si Δ = 0, les deux solutions sont confondues et valent −b/(2a) : z² − 2(1 + i)z + 2i = 0 a Δ = 0 et pour seule solution 1 + i. Si Δ est un réel négatif, δ = i√(−Δ) : z² + z + 1 = 0 a Δ = −3 et pour solutions (−1 ± i√3)/2, c'est-à-dire j et j².
:::

::: verifie À toi : un discriminant à racine carrée simple
Résoudre z² − (5 + i)z + 8 + 4i = 0.

---

Δ = (5 + i)² − 4(8 + 4i) = 24 + 10i − 32 − 16i = −8 − 6i. Avec |Δ| = 10, on a x² − y² = −8 et x² + y² = 10, d'où x² = 1 et y² = 9 ; 2xy = −6 < 0, donc δ = 1 − 3i. Alors z = ((5 + i) ± (1 − 3i))/2, soit z′ = 3 − i et z″ = 2 + 2i. Contrôle : la somme vaut 5 + i ✓.
:::

::: retenir
Δ = b² − 4ac est un complexe sans signe : on en cherche une racine carrée δ et z = (−b ± δ)/(2a) ; Δ = 0 donne deux solutions confondues ; az² + bz + c = a(z − z₁)(z − z₂).
:::

## ⚖️ Somme et produit des solutions

L'équation z² − (2 + 3i)z − 1 + 3i = 0 admet pour solution 1 + i : (1 + i)² = 2i et (2 + 3i)(1 + i) = −1 + 5i, donc 2i + 1 − 5i − 1 + 3i = 0.
Faut-il calculer Δ pour trouver l'autre solution, ou les coefficients la livrent-ils déjà ?

::: exemple L'autre solution sans calculer Δ

1. D'après la factorisation az² + bz + c = a(z − z₁)(z − z₂), le développement donne az² − a(z₁ + z₂)z + a z₁z₂, donc z₁ + z₂ = −b/a et z₁z₂ = c/a.
2. Ici a = 1, b = −(2 + 3i) et c = −1 + 3i : la somme vaut 2 + 3i, donc l'autre solution est (2 + 3i) − (1 + i) = 1 + 2i.
3. Contrôle par le produit : (1 + i)(1 + 2i) = 1 + 2i + i − 2 = −1 + 3i = c/a ✓.

:::

::: exemple Deux complexes de somme et de produit donnés

On cherche z₁ et z₂ tels que z₁ + z₂ = 1 + 2i et z₁z₂ = −1 + i.

1. Ce sont les solutions de z² − Sz + P = 0, soit z² − (1 + 2i)z − 1 + i = 0, car z² − Sz + P = (z − z₁)(z − z₂).
2. Δ = (1 + 2i)² − 4(−1 + i) = −3 + 4i + 4 − 4i = 1, de racine carrée 1. Alors z = ((1 + 2i) ± 1)/2, soit 1 + i et i.
3. Contrôle : somme 1 + 2i ✓ et produit (1 + i) × i = i − 1 ✓.

:::

::: piege
**Erreur : prendre c pour le produit quand a ≠ 1.** L'erreur tente parce que, avec a = 1, le produit est bien c. Dans 2z² − 6z + 6 + 2i = 0, dont une solution est 1 + i, le produit vaut c/a = 3 + i et l'autre solution est (3 + i)/(1 + i) = 2 − i. Avec c = 6 + 2i, on trouverait 4 − 2i, et la somme 1 + i + 4 − 2i = 5 − i ne vaut pas −b/a = 3 : le contrôle croisé révèle la faute.
:::

::: propriete
Si z₁ et z₂ sont les solutions de az² + bz + c = 0, a ≠ 0, alors :
$$ z₁ + z₂ = −b/a  et  z₁ z₂ = c/a $$
Cas limite : si les deux solutions sont confondues (Δ = 0), leur valeur commune est −b/(2a), de somme −b/a.
:::

::: methode Trouver deux complexes de somme S et de produit P
1. Ces deux complexes sont les solutions de l'équation z² − Sz + P = 0.
2. Résoudre cette équation avec le discriminant Δ = S² − 4P et une racine carrée δ de Δ.
:::

::: verifie À toi : somme et produit donnés
Déterminer z₁ et z₂ tels que z₁ + z₂ = 4 + 2i et z₁z₂ = 3 + 6i.

---

Ce sont les solutions de z² − (4 + 2i)z + 3 + 6i = 0. Δ = (4 + 2i)² − 4(3 + 6i) = 12 + 16i − 12 − 24i = −8i, de racine carrée 2 − 2i, car (2 − 2i)² = −8i. Alors z = ((4 + 2i) ± (2 − 2i))/2, soit 3 et 1 + 2i. Contrôle : produit 3(1 + 2i) = 3 + 6i ✓.
:::

::: retenir
z₁ + z₂ = −b/a et z₁z₂ = c/a : connaissant une solution, on trouve l'autre sans Δ ; deux complexes de somme S et de produit P sont les solutions de z² − Sz + P = 0.
:::

## 🧩 Degré 3 : factoriser par un zéro

Dans ℂ, z³ − 1 = 0 a trois solutions. On en connaît une, z = 1, et l'on a z³ − 1 = (z − 1)(z² + z + 1).
Quand on connaît une solution d'une équation de degré 3, peut-on toujours se ramener au second degré ?

::: propriete
Soient n ≥ 2 et P(z) = aₙzⁿ + aₙ₋₁zⁿ⁻¹ + … + a₁z + a₀ avec aₙ ≠ 0. Si z₀ est un zéro de P, c'est-à-dire P(z₀) = 0, alors P(z) = (z − z₀)g(z), où g est de la forme aₙzⁿ⁻¹ + bₙ₋₂zⁿ⁻² + … + b₀, avec b₀, …, bₙ₋₂ complexes.
Conséquence : P(z) = 0 équivaut à z = z₀ ou g(z) = 0, et g est de degré n − 1.
:::

::: exemple Un zéro imaginaire pur : z³ + (1 − 4i)z² − (7 + 3i)z + 6i − 2 = 0

1. On pose z = iy avec y réel. En séparant parties réelle et imaginaire, l'équation devient (−y² + 3y − 2) + i(−y³ + 4y² − 7y + 6) = 0 : deux équations en y qui doivent s'annuler en même temps.
2. La partie réelle −y² + 3y − 2 = 0 donne y = 1 ou y = 2. La partie imaginaire vaut 2 pour y = 1 et −8 + 16 − 14 + 6 = 0 pour y = 2. Donc z₀ = 2i.
3. On factorise : (z − 2i)(z² + βz + γ) = z³ + (β − 2i)z² + (γ − 2iβ)z − 2iγ. En identifiant : β − 2i = 1 − 4i donne β = 1 − 2i ; γ − 2iβ = −7 − 3i donne γ = −3 − i ; contrôle sur le terme constant : −2iγ = 6i − 2 ✓.
4. Reste z² + (1 − 2i)z − 3 − i = 0. Δ = (1 − 2i)² + 4(3 + i) = −3 − 4i + 12 + 4i = 9, de racine carrée 3, donc z = (−(1 − 2i) ± 3)/2 : z = 1 + i ou z = −2 + i. Les solutions sont 2i, 1 + i et −2 + i.
5. Contrôle par réinjection de 1 + i : z² = 2i, z³ = −2 + 2i, (1 − 4i)(2i) = 8 + 2i et −(7 + 3i)(1 + i) = −4 − 10i, d'où (−2 + 2i) + (8 + 2i) + (−4 − 10i) + 6i − 2 = 0 ✓.

:::

::: piege
**Erreur : s'arrêter à la partie réelle.** L'erreur tente parce que −y² + 3y − 2 = 0 donne tout de suite deux valeurs, 1 et 2, et que l'on en garde une au hasard. Mais z = i n'est pas solution : pour y = 1, la partie imaginaire vaut 2, donc le premier membre vaut 2i et non 0. Il faut que les deux équations s'annulent pour la même valeur de y.
:::

::: methode Résoudre une équation de degré 3
1. Chercher un zéro z₀ : un entier simple, ou un imaginaire pur z = iy (deux équations en y à vérifier ensemble).
2. Factoriser par identification : P(z) = (z − z₀)(z² + βz + γ), en comparant les coefficients de z², de z et le terme constant.
3. Résoudre le second degré et conclure avec les trois solutions.

Cas limite : un zéro de P peut aussi être un zéro de g ; le facteur z − z₀ apparaît alors deux fois.
:::

::: verifie À toi : factoriser avec un zéro donné
Résoudre z³ − 4z² + (6 + i)z − 3 − i = 0, sachant que 1 est solution.

---

On écrit P(z) = (z − 1)(z² + βz + γ) = z³ + (β − 1)z² + (γ − β)z − γ. En identifiant, β − 1 = −4 donne β = −3, puis γ − β = 6 + i donne γ = 3 + i, et le terme constant −γ = −3 − i convient ✓. Reste z² − 3z + 3 + i = 0 : Δ = 9 − 12 − 4i = −3 − 4i, de racine carrée 1 − 2i, donc z = (3 ± (1 − 2i))/2, soit 2 − i et 1 + i. Les solutions sont 1, 1 + i et 2 − i.
:::

::: retenir
Si z₀ est un zéro de P, alors P(z) = (z − z₀)g(z) ; on devine z₀ (entier simple ou imaginaire pur iy), on identifie les coefficients de g puis on résout le second degré.
:::

## 🔁 Changer d'inconnue

L'équation z⁴ + (1 + i)z² + i = 0 est de degré 4, mais elle ne contient que z⁴ = (z²)² et z². Avec le second degré z² + (1 + i)z + i = 0, on sait déjà faire.
Peut-on résoudre l'équation de degré 4 en posant Z = z² ?

::: exemple z⁴ + (1 + i)z² + i = 0

1. On pose Z = z² : l'équation devient Z² + (1 + i)Z + i = 0. Δ = (1 + i)² − 4i = −2i, de racine carrée 1 − i, donc Z = (−(1 + i) ± (1 − i))/2 : Z = −i ou Z = −1.
2. On revient à z. Pour z² = −1 : z = i ou z = −i. Pour z² = −i = e^(−iπ/2) : z = ±e^(−iπ/4) = ±(√2/2)(1 − i).
3. L'équation a quatre solutions : i, −i, (√2/2)(1 − i) et −(√2/2)(1 − i). Contrôle : ((√2/2)(1 − i))² = (1/2)(−2i) = −i ✓.

:::

::: piege
**Erreur : s'arrêter à Z = −i et Z = −1.** L'erreur tente parce que l'équation en Z est résolue et semble terminée. Mais Z n'est qu'un intermédiaire : l'inconnue du problème est z, avec z² = Z, et chaque valeur de Z donne deux valeurs de z. L'équation de degré 4 a donc quatre solutions, pas deux.
:::

::: exemple Factoriser x⁶ + 1 en trinômes réels

1. Les solutions de z⁶ = −1 vérifient r = 1 et θ = π : z_k = e^(i(π/6 + kπ/3)), soit e^(iπ/6), i, e^(i5π/6), e^(i7π/6), −i et e^(i11π/6).
2. On regroupe les solutions deux à deux : (z − e^(iα))(z − e^(−iα)) = z² − 2cos α z + 1. Avec α = π/6, π/2 et 5π/6 : z⁶ + 1 = (z² − √3 z + 1)(z² + 1)(z² + √3 z + 1).
3. Contrôle : (z² − √3 z + 1)(z² + √3 z + 1) = (z² + 1)² − 3z² = z⁴ − z² + 1, puis (z⁴ − z² + 1)(z² + 1) = z⁶ + 1 ✓.

:::

::: exemple Une équation qui mêle z et z̄ : z⁵ = z̄

1. Les modules sont égaux : |z|⁵ = |z|, donc |z|(|z|⁴ − 1) = 0, soit z = 0 ou |z| = 1.
2. Si |z| = 1, alors z z̄ = 1 et z̄ = 1/z. L'équation devient z⁵ = 1/z, donc z⁶ = 1 : ce sont les six racines sixièmes de l'unité.
3. L'équation a sept solutions : 0 et les six racines sixièmes de l'unité. Contrôle : pour z = e^(iπ/3), z⁵ = e^(i5π/3) = e^(−iπ/3) = z̄ ✓.

:::

::: methode Se ramener à une équation connue
1. Si l'équation ne contient que des puissances de z² (ou de z³), poser Z = z² (ou Z = z³), résoudre en Z puis revenir à z avec les racines carrées (ou cubiques).
2. Pour zⁿ = −1, écrire les n solutions e^(iα) et regrouper celles qui ont des angles opposés : le produit (z − e^(iα))(z − e^(−iα)) est le trinôme réel z² − 2cos α z + 1.
3. Quand z et z̄ se mêlent, comparer les modules, puis utiliser z̄ = 1/z pour |z| = 1.

Cas limite : z = 0 est souvent solution d'une équation qui mêle z et z̄, et il ne faut pas le perdre en divisant par z.
:::

::: verifie À toi : une équation en z²
Résoudre z⁴ + (3 − 2i)z² − 6i = 0.

---

On pose Z = z² : Z² + (3 − 2i)Z − 6i = (Z + 3)(Z − 2i) = 0, donc Z = −3 ou Z = 2i. Pour z² = −3 : z = ±i√3. Pour z² = 2i : z = ±(1 + i), car (1 + i)² = 2i. Les quatre solutions sont i√3, −i√3, 1 + i et −1 − i. Contrôle : (i√3)⁴ + (3 − 2i)(−3) − 6i = 9 − 9 + 6i − 6i = 0 ✓.
:::

::: retenir
Pour z⁴ ou z⁶, on pose Z = z² ou Z = z³, on résout en Z puis on revient à z (quatre solutions pour un degré 4, six pour un degré 6) ; pour une équation qui mêle z et z̄, on compare d'abord les modules.
:::

## 🎯 Équations avec un paramètre θ et lieux de points

Pour chaque valeur de θ, l'équation z² − 2iz + 2ie^(iθ) − e^(2iθ) = 0 a deux solutions, donc deux points M₁ et M₂ du plan. Quand θ varie, ces points bougent.
Que décrivent-ils, et que dire de leur milieu ?

::: figure Pour θ = π/3 (valeur d'illustration) : M₁ est sur le cercle C₁ de centre O, M₂ sur le cercle C₂ de centre 2i, et le milieu I de [M₁M₂] est le point fixe d'affixe i
<svg viewBox="0 0 320 320">
<title>Pour θ = π/3 : M₁ d'affixe e^(iθ) sur le cercle C₁ de centre O et de rayon 1, M₂ d'affixe 2i − e^(iθ) sur le cercle C₂ de centre 2i et de rayon 1, et I d'affixe i au milieu de [M₁M₂]</title>
<path d="M14.4 236 H306.8" fill="none" stroke="#0f172a" stroke-width="1.6"/>
<path d="M130 324.4 V-2" fill="none" stroke="#0f172a" stroke-width="1.6"/>
<path d="M306.8 236 l-8 -4 l0 8 z" fill="#0f172a"/>
<path d="M130 -2 l-4 8 l8 0 z" fill="#0f172a"/>
<path d="M198 233 V239" stroke="#0f172a" stroke-width="1.2"/>
<text x="198" y="252" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">1</text>
<path d="M62 233 V239" stroke="#0f172a" stroke-width="1.2"/>
<text x="62" y="252" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">−1</text>
<path d="M127 100 H133" stroke="#0f172a" stroke-width="1.2"/>
<text x="123" y="104" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">2i</text>
<path d="M127 304 H133" stroke="#0f172a" stroke-width="1.2"/>
<text x="123" y="308" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">−i</text>
<text x="124" y="251" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">O</text>
<circle cx="130" cy="236" r="68" fill="none" stroke="#0f6e56" stroke-width="1.6" stroke-dasharray="5 4"/>
<circle cx="130" cy="100" r="68" fill="none" stroke="#b45309" stroke-width="1.6" stroke-dasharray="5 4"/>
<path d="M164 177.1 L96 158.9" fill="none" stroke="#0f172a" stroke-width="2.2"/>
<path d="M130 236 L164 177.1" fill="none" stroke="#0f6e56" stroke-width="1.8"/>
<path d="M130 100 L96 158.9" fill="none" stroke="#b45309" stroke-width="1.8"/>
<circle cx="164" cy="177.1" r="4" fill="#0f6e56"/>
<circle cx="96" cy="158.9" r="4" fill="#b45309"/>
<circle cx="130" cy="168" r="3.5" fill="#0f172a"/>
<text x="172" y="193.1" text-anchor="start" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">M₁</text>
<text x="88" y="152.9" text-anchor="end" font-size="12" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">M₂</text>
<text x="138" y="162" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">I</text>
<text x="197.7" y="282.6" text-anchor="start" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">C₁</text>
<text x="197.7" y="61.4" text-anchor="start" font-size="12" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">C₂</text>
</svg>
:::

Sur la figure, M₂ est le symétrique de M₁ par rapport à I, et les deux cercles de rayon 1 sont symétriques l'un de l'autre par rapport à I.

::: exemple Résoudre l'équation puis lire les lieux, pour θ ∈ [0 ; 2π[

1. On a a = 1, b = −2i et c = 2ie^(iθ) − e^(2iθ), donc Δ = −4 − 4(2ie^(iθ) − e^(2iθ)) = 4(e^(2iθ) − 2ie^(iθ) − 1) = 4(e^(iθ) − i)². Une racine carrée de Δ est δ = 2(e^(iθ) − i).
2. Alors z = (2i ± 2(e^(iθ) − i))/2 : z₁ = e^(iθ) et z₂ = 2i − e^(iθ).
3. On a |z₁| = 1 : M₁ décrit le cercle C₁ de centre O et de rayon 1. On a z₂ − 2i = −e^(iθ), donc |z₂ − 2i| = 1 : M₂ décrit le cercle C₂ de centre d'affixe 2i et de rayon 1.
4. Le milieu I de [M₁M₂] a pour affixe (z₁ + z₂)/2 = i : c'est un point fixe. Et (M₁M₂)² = |2i − 2e^(iθ)|² = 4(cos²θ + (1 − sin θ)²) = 8(1 − sin θ), maximal pour sin θ = −1, soit θ = 3π/2 et M₁M₂ = 4. Contrôle pour θ = π/3 : M₁ = 1/2 + i√3/2 et M₂ = −1/2 + i(2 − √3/2), d'où (M₁M₂)² = 1 + (2 − √3)² = 8 − 4√3 = 8(1 − √3/2) ✓.

:::

::: piege
**Erreur : conclure « M₂ est sur le cercle trigonométrique, car z₂ contient e^(iθ) ».** L'erreur tente parce que e^(iθ) est de module 1. Mais z₂ = 2i − e^(iθ) : c'est z₂ − 2i qui a pour module 1. Pour θ = π/3, |z₂|² = 1/4 + (2 − √3/2)² = 5 − 2√3 ≈ 1,54, loin de 1.
:::

::: methode Lire le lieu d'un point qui dépend de θ
1. Résoudre l'équation en gardant θ comme une constante : le discriminant se met souvent sous la forme d'un carré.
2. Écrire la solution sous la forme z = c + r e^(iθ) avec c et r constants : alors |z − c| = r, et M décrit le cercle de centre C(c) et de rayon r quand θ décrit [0 ; 2π[.
3. Borner θ pour savoir si M décrit le cercle entier ou seulement un arc, extrémités comprises ou non.
4. Pour un milieu, une distance ou un alignement, calculer avec les affixes : (z₁ + z₂)/2, |z₂ − z₁|, ou le quotient de deux différences d'affixes, réel pour l'alignement.

Cas limite : si θ ne décrit que ]0 ; π[, le point M ne décrit qu'un demi-cercle, sans ses extrémités.
:::

::: verifie À toi : un autre lieu
Pour θ ∈ [0 ; 2π[, on considère z² − 2iz − 1 − 9e^(2iθ) = 0. Montrer que ses solutions sont i + 3e^(iθ) et i − 3e^(iθ), puis déterminer l'ensemble décrit par le point M₁ d'affixe i + 3e^(iθ).

---

On a Δ = (−2i)² − 4(−1 − 9e^(2iθ)) = −4 + 4 + 36e^(2iθ) = (6e^(iθ))², donc z = (2i ± 6e^(iθ))/2 = i ± 3e^(iθ). Pour M₁, z₁ − i = 3e^(iθ), donc |z₁ − i| = 3 : M₁ décrit le cercle de centre d'affixe i et de rayon 3, entièrement lorsque θ décrit [0 ; 2π[. Contrôle pour θ = 0 : z₁ = i + 3 et (i + 3)² − 2i(i + 3) − 1 − 9 = 8 + 6i + 2 − 6i − 10 = 0 ✓.
:::

::: retenir
On résout avec θ constant, on écrit z = c + r e^(iθ) pour lire |z − c| = r, on borne θ pour savoir quelle partie du cercle est décrite, et l'on calcule milieux et distances avec les affixes.
:::

> 🏆 Les huit portes sont franchies : tu places les racines nièmes sur un polygone régulier, tu extrais des racines carrées, tu résous le second degré dans ℂ, tu relies somme et produit des solutions et tu ramènes les degrés supérieurs au second. Prochaine étape : la suite du programme.
