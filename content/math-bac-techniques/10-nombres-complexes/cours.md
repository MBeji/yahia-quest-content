# ⚔️ Nombres complexes — des nombres qui ont une direction

> 💡 «Un réel se place sur une droite ; un complexe se place dans le plan, et il y emporte une longueur, une direction et toute la trigonométrie.»

Ce chapitre ajoute aux réels un nombre i tel que i² = −1. On y calcule comme d'habitude, puis on découvre que chaque nombre complexe est un point du plan : son module est une distance, son argument est un angle. Huit notions, de la forme algébrique aux ensembles de points. Les équations du second degré dans ℂ sont l'objet du chapitre suivant.

## 🏰 Forme algébrique et conjugué

Aucun réel ne vérifie x² = −1, puisqu'un carré réel est positif ou nul. On ajoute alors aux réels un nombre i tel que i² = −1, et l'on veut calculer avec lui comme d'habitude. Par exemple, que valent (2 + 3i)(1 − 2i) et (2 + 3i)/(1 − 2i) ?
Un produit se développe-t-il comme dans ℝ, et comment diviser par un nombre qui contient i ?

::: definition
Tout nombre complexe z s'écrit de façon unique **z = a + ib**, avec a et b réels et i² = −1 : c'est la **forme algébrique**. Le réel a est la **partie réelle**, Re(z) = a ; le réel b est la **partie imaginaire**, Im(z) = b. L'ensemble des nombres complexes se note ℂ.
Le **conjugué** de z = a + ib est le nombre z̄ = a − ib.
:::

::: figure Le conjugué de z est le symétrique de z par rapport à l'axe des réels : même partie réelle, parties imaginaires opposées
<svg viewBox="0 0 300 250">
<title>Le point M d'affixe 3 + 2i et le point M′ d'affixe 3 − 2i sont symétriques par rapport à l'axe des réels</title>
<path d="M30 125 H270" fill="none" stroke="#0f172a" stroke-width="1.6"/>
<path d="M70 245 V5" fill="none" stroke="#0f172a" stroke-width="1.6"/>
<path d="M270 125 l-8 -4 l0 8 z" fill="#0f172a"/>
<path d="M70 5 l-4 8 l8 0 z" fill="#0f172a"/>
<path d="M110 122 V128" stroke="#0f172a" stroke-width="1.2"/>
<text x="110" y="141" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">1</text>
<path d="M150 122 V128" stroke="#0f172a" stroke-width="1.2"/>
<text x="150" y="141" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">2</text>
<path d="M190 122 V128" stroke="#0f172a" stroke-width="1.2"/>
<text x="190" y="141" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">3</text>
<path d="M67 85 H73" stroke="#0f172a" stroke-width="1.2"/>
<text x="63" y="89" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">i</text>
<path d="M67 45 H73" stroke="#0f172a" stroke-width="1.2"/>
<text x="63" y="49" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">2i</text>
<path d="M67 165 H73" stroke="#0f172a" stroke-width="1.2"/>
<text x="63" y="169" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">−i</text>
<path d="M67 205 H73" stroke="#0f172a" stroke-width="1.2"/>
<text x="63" y="209" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">−2i</text>
<text x="64" y="140" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">O</text>
<path d="M190 45 L190 205" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-dasharray="5 4"/>
<path d="M70 125 L190 45" fill="none" stroke="#0f6e56" stroke-width="2.2"/>
<path d="M70 125 L190 205" fill="none" stroke="#b45309" stroke-width="2.2"/>
<circle cx="190" cy="45" r="4" fill="#0f172a"/>
<circle cx="190" cy="205" r="4" fill="#0f172a"/>
<text x="198" y="41" text-anchor="start" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">M(z), z = 3 + 2i</text>
<text x="198" y="219" text-anchor="start" font-size="12" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">M′(z̄), z̄ = 3 − 2i</text>
</svg>
:::

La figure place z = a + ib au point de coordonnées (a ; b), comme la notion suivante le justifie : le conjugué z̄ a la même partie réelle a et la partie imaginaire opposée −b, c'est le symétrique de z par rapport à l'axe des réels.

::: exemple Produit et quotient de 2 + 3i et 1 − 2i

1. On développe comme dans ℝ : (2 + 3i)(1 − 2i) = 2 − 4i + 3i − 6i².
2. Or i² = −1, donc −6i² = +6 : le produit vaut 8 − i.
3. Pour le quotient, on multiplie haut et bas par le conjugué du dénominateur, 1 + 2i, car (1 − 2i)(1 + 2i) = 1 + 4 = 5 est un réel.
4. (2 + 3i)/(1 − 2i) = (2 + 3i)(1 + 2i)/5 = (2 + 4i + 3i − 6)/5 = (−4 + 7i)/5. Contrôle : (−4 + 7i)/5 × (1 − 2i) = (−4 + 8i + 7i + 14)/5 = (10 + 15i)/5 = 2 + 3i ✓.

:::

::: piege
**Erreur : écrire (3 + 2i)(3 − 2i) = 9 − 4 = 5.** L'erreur tente parce que (a + b)(a − b) = a² − b² avec b = 2i. Mais b² = (2i)² = 4i² = −4, donc −b² = +4. Le produit vaut 9 + 4 = 13, qui est bien a² + b² avec a = 3 et b = 2.
:::

::: propriete
Pour z = a + ib et z′ = a′ + ib′ (a, b, a′, b′ réels) :
z + z̄ = 2a ; z − z̄ = 2ib ; z × z̄ = a² + b², un réel positif ou nul.
Le conjugué respecte les opérations : le conjugué de z + z′ est z̄ + z̄′, celui de z × z′ est z̄ × z̄′, celui de zⁿ est (z̄)ⁿ (n entier naturel non nul), celui de z/z′ est z̄/z̄′ (z′ ≠ 0).
z est réel ⇔ Im(z) = 0 ⇔ z = z̄. z est imaginaire pur ⇔ Re(z) = 0 ⇔ z = −z̄ (z non nul).
Cas limite : z = 0 est réel, mais on ne le compte pas parmi les imaginaires purs (l'égalité z = −z̄ y est vraie aussi). Deux complexes sont égaux si et seulement si ils ont la même partie réelle et la même partie imaginaire.
:::

::: methode Calculer iⁿ
Les puissances de i se répètent de 4 en 4 : i⁰ = 1, i¹ = i, i² = −1, i³ = −i, i⁴ = 1.

1. On divise n par 4 et on garde le reste r : iⁿ = iʳ, car i⁴ = 1.
2. i²⁰²⁶ : 2026 = 4 × 506 + 2, donc i²⁰²⁶ = i² = −1.
3. i⁻⁷ : −7 = 4 × (−2) + 1, donc i⁻⁷ = i. Contrôle : i⁷ = i³ = −i et 1/(−i) = i ✓.

:::

::: verifie À toi : un quotient
Écrire (3 − i)/(1 + i) sous forme algébrique.

---

On multiplie haut et bas par le conjugué du dénominateur, 1 − i, pour obtenir un dénominateur réel : (3 − i)(1 − i)/((1 + i)(1 − i)) = (3 − 3i − i + i²)/2 = (2 − 4i)/2 = 1 − 2i. Contrôle : (1 − 2i)(1 + i) = 1 + i − 2i − 2i² = 3 − i ✓.
:::

::: retenir
z = a + ib et z̄ = a − ib ; z × z̄ = a² + b² est un réel positif ; on divise en multipliant par le conjugué du dénominateur ; z est réel ⇔ z = z̄ et imaginaire pur ⇔ z = −z̄ et z ≠ 0.
:::

## 🗺️ Affixe, module et distance

Sur l'écran d'un traceur, un point se repère par un couple (x ; y), et sa distance au centre se calcule avec Pythagore : le point (3 ; 4) est à √(9 + 16) = 5 du centre. Un nombre complexe peut coder ce point, et l'on voudrait que sa « taille » redonne cette distance.
Comment mesurer, avec des complexes, la distance d'un point à l'origine, puis la distance entre deux points ?

::: definition
Le plan est rapporté à un repère orthonormé direct (O, u⃗, v⃗). L'**affixe** du point M(x ; y) est le complexe z_M = x + iy ; M est l'**image** de z. L'**affixe du vecteur** AB⃗ est z_B − z_A.
Le **module** de z = a + ib est le réel positif |z| = √(a² + b²) = √(z × z̄).
:::

::: figure Le module |z| est la longueur OM ; la distance MN est le module de la différence des affixes
<svg viewBox="0 0 300 250">
<title>Le module de 3 + 4i est la distance OM = 5 ; la distance MN entre M(3 + 4i) et N(−1 + 2i) est le module de la différence −4 − 2i, soit 2√5</title>
<path d="M4 205 H270" fill="none" stroke="#0f172a" stroke-width="1.6"/>
<path d="M80 243 V15" fill="none" stroke="#0f172a" stroke-width="1.6"/>
<path d="M270 205 l-8 -4 l0 8 z" fill="#0f172a"/>
<path d="M80 15 l-4 8 l8 0 z" fill="#0f172a"/>
<path d="M118 202 V208" stroke="#0f172a" stroke-width="1.2"/>
<text x="118" y="221" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">1</text>
<path d="M156 202 V208" stroke="#0f172a" stroke-width="1.2"/>
<text x="156" y="221" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">2</text>
<path d="M194 202 V208" stroke="#0f172a" stroke-width="1.2"/>
<text x="194" y="221" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">3</text>
<path d="M232 202 V208" stroke="#0f172a" stroke-width="1.2"/>
<text x="232" y="221" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">4</text>
<path d="M77 167 H83" stroke="#0f172a" stroke-width="1.2"/>
<text x="73" y="171" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">i</text>
<path d="M77 129 H83" stroke="#0f172a" stroke-width="1.2"/>
<text x="73" y="133" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">2i</text>
<path d="M77 91 H83" stroke="#0f172a" stroke-width="1.2"/>
<text x="73" y="95" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">3i</text>
<path d="M77 53 H83" stroke="#0f172a" stroke-width="1.2"/>
<text x="73" y="57" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">4i</text>
<text x="74" y="220" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">O</text>
<path d="M194 53 L194 205" fill="none" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="5 4"/>
<path d="M194 53 L80 53" fill="none" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="5 4"/>
<path d="M80 205 L194 53" fill="none" stroke="#0f6e56" stroke-width="2.6"/>
<path d="M194 53 L42 129" fill="none" stroke="#b45309" stroke-width="2.4"/>
<circle cx="194" cy="53" r="4" fill="#0f172a"/>
<circle cx="42" cy="129" r="4" fill="#0f172a"/>
<text x="145" y="145" text-anchor="start" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">|z| = OM = 5</text>
<text x="202" y="49" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">M(3 + 4i)</text>
<text x="36" y="145" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">N(−1 + 2i)</text>
<text x="114" y="67" text-anchor="start" font-size="12" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">MN = 2√5</text>
</svg>
:::

Sur la figure, |z| est la longueur OM, hypoténuse du triangle de côtés 3 et 4 ; et la distance MN est le module de l'affixe du vecteur MN⃗, c'est-à-dire de z_N − z_M.

::: exemple Distances OM et MN pour M(3 + 4i) et N(−1 + 2i)

1. OM = |3 + 4i| = √(9 + 16) = 5, le module est la distance à l'origine.
2. L'affixe du vecteur MN⃗ est z_N − z_M = (−1 − 3) + (2 − 4)i = −4 − 2i, car on retranche l'origine du vecteur à son extrémité.
3. MN = |−4 − 2i| = √(16 + 4) = √20 = 2√5. Contrôle sur la figure : écart horizontal 4 et écart vertical 2, donc √(4² + 2²) = √20 ✓.

:::

::: exemple Les règles du module, sans figure

1. |zz′| = |z| × |z′| ; |z/z′| = |z|/|z′| (z′ ≠ 0) ; |zⁿ| = |z|ⁿ ; |z̄| = |z|.
2. |(1 + i√3)⁴ (1 − i)⁶| = |1 + i√3|⁴ × |1 − i|⁶ = 2⁴ × (√2)⁶ = 16 × 8 = 128.
3. |(3 + 4i)/(1 − i)²| = |3 + 4i|/|1 − i|² = 5/2. Contrôle : (1 − i)² = −2i, de module 2 ✓.

:::

::: exemple Reconnaître un triangle par les modules

1. Soit O, A(2 + 2i) et B(2 − 2i). OA = |2 + 2i| = 2√2 et OB = |2 − 2i| = 2√2 : le triangle est isocèle en O.
2. AB = |z_B − z_A| = |−4i| = 4.
3. OA² + OB² = 8 + 8 = 16 = AB² : par la réciproque de Pythagore, le triangle est rectangle en O. Il est rectangle isocèle en O.

:::

::: piege
**Erreur : écrire |3 + 4i| = 3 + 4 = 7.** L'erreur tente parce qu'on additionne les deux « morceaux » du nombre. Mais le module est une longueur en diagonale : √(3² + 4²) = 5, et 7 serait la longueur du chemin par les axes. De même, |z + z′| n'est pas |z| + |z′| en général.
:::

::: propriete
Pour tous complexes z et z′ : |z| ≥ 0, et |z| = 0 ⇔ z = 0 ; |z + z′| ≤ |z| + |z′| (inégalité triangulaire).
L'égalité |z + z′| = |z| + |z′| a lieu quand z′ = λz avec λ ≥ 0 (ou z = 0), c'est-à-dire quand les deux vecteurs ont le même sens.
Cas limite : avec z = 3 + 4i et z′ = −3 + 4i, |z + z′| = |8i| = 8 < 10 = |z| + |z′| ; avec z = 1 + i et z′ = 2 + 2i, |z + z′| = |3 + 3i| = 3√2 = √2 + 2√2 : égalité.
:::

::: verifie À toi : une distance
Calculer la distance entre A(1 − i) et B(−4 + 11i).

---

L'affixe du vecteur AB⃗ est z_B − z_A = (−4 − 1) + (11 + 1)i = −5 + 12i. La distance est le module de cette différence : AB = √(25 + 144) = √169 = 13.
:::

::: retenir
|a + ib| = √(a² + b²) est la distance OM ; la distance entre deux points est AB = |z_B − z_A| ; le module respecte produit, quotient et puissance mais |z + z′| ≤ |z| + |z′|.
:::

## 🧭 Argument d'un nombre complexe non nul

Un radar ne donne pas seulement la distance d'un avion au centre : il donne aussi son cap. Deux points peuvent être à la même distance de O sans être dans la même direction, et le module ne distingue pas 1 + i de −1 + i.
Comment mesurer la direction de OM avec un seul nombre, et comment la retrouver à partir de a et b ?

::: definition
Soit z un complexe non nul et M son image. Un **argument** de z est toute mesure, en radians, de l'angle orienté (u⃗, OM⃗). On note arg(z) = θ + 2kπ, avec k entier : un argument n'est défini qu'à 2π près. Le nombre 0 n'a pas d'argument.
Cas particuliers : z réel strictement positif, arg(z) = 0 ; z réel strictement négatif, arg(z) = π ; z = ib avec b > 0, arg(z) = π/2 ; z = ib avec b < 0, arg(z) = −π/2.
:::

::: figure L'argument de z est la mesure de l'angle orienté de u vers OM, ici 3π/4 pour un point du deuxième quadrant
<svg viewBox="0 0 300 230">
<title>Le point M d'affixe −1 + i est dans le deuxième quadrant : l'angle orienté de u vers OM mesure 3π/4</title>
<path d="M16 170 H280" fill="none" stroke="#0f172a" stroke-width="1.6"/>
<path d="M160 230 V26" fill="none" stroke="#0f172a" stroke-width="1.6"/>
<path d="M280 170 l-8 -4 l0 8 z" fill="#0f172a"/>
<path d="M160 26 l-4 8 l8 0 z" fill="#0f172a"/>
<path d="M40 167 V173" stroke="#0f172a" stroke-width="1.2"/>
<text x="40" y="186" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">−2</text>
<path d="M100 167 V173" stroke="#0f172a" stroke-width="1.2"/>
<text x="100" y="186" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">−1</text>
<path d="M220 167 V173" stroke="#0f172a" stroke-width="1.2"/>
<text x="220" y="186" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">1</text>
<path d="M157 110 H163" stroke="#0f172a" stroke-width="1.2"/>
<text x="153" y="114" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">i</text>
<path d="M157 50 H163" stroke="#0f172a" stroke-width="1.2"/>
<text x="153" y="54" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">2i</text>
<text x="154" y="185" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">O</text>
<path d="M100 110 L100 170" fill="none" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="5 4"/>
<path d="M100 110 L160 110" fill="none" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="5 4"/>
<path d="M160 170 L100 110" fill="none" stroke="#0f6e56" stroke-width="2.6"/>
<path d="M194 170 A34 34 0 0 0 135.96 145.96" fill="none" stroke="#b45309" stroke-width="2"/>
<circle cx="100" cy="110" r="4" fill="#0f172a"/>
<text x="92" y="104" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">M(−1 + i)</text>
<text x="175" y="137" text-anchor="start" font-size="12" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">θ = 3π/4</text>
<text x="122" y="164" text-anchor="end" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">|z| = √2</text>
</svg>
:::

Sur la figure, l'arc orange est l'angle de u⃗ vers OM⃗ : sa mesure 3π/4 est un argument de z = −1 + i, et le point est bien dans le deuxième quadrant.

::: methode Trouver un argument de z = a + ib

1. On calcule le module r = |z| = √(a² + b²).
2. On cherche θ tel que cos θ = a/r et sin θ = b/r : il faut les deux, car chacun seul laisse deux angles possibles.
3. On contrôle avec le quadrant du point : les signes de a et de b doivent être ceux de cos θ et de sin θ.

:::

::: exemple Deux arguments

1. z = −1 + i : r = √2, cos θ = −1/√2 = −√2/2 et sin θ = √2/2. Le point est dans le deuxième quadrant, donc θ = 3π/4.
2. z = −√3 − i : r = 2, cos θ = −√3/2 et sin θ = −1/2. Le point est dans le troisième quadrant, donc θ = −5π/6 (ou 7π/6).

:::

::: piege
**Erreur : arg(−1 − i) = π/4, parce que b/a = 1.** L'erreur tente parce que tan(π/4) = 1 et que la calculatrice rend π/4 pour arctan 1. Mais arctan ne renvoie que des angles du premier et du quatrième quadrant. Ici cos θ = −√2/2 et sin θ = −√2/2 sont négatifs : le point est dans le troisième quadrant et θ = −3π/4.
:::

::: propriete
Pour z non nul et λ réel non nul :
arg(z̄) = −arg(z) ; arg(−z) = arg(z) + π ; arg(λz) = arg(z) si λ > 0 ; arg(λz) = arg(z) + π si λ < 0 (à 2π près).
Avec z = −1 + i, d'argument 3π/4 : z̄ = −1 − i a pour argument −3π/4 ; −z = 1 − i a pour argument 3π/4 + π = 7π/4, c'est-à-dire −π/4 ; −2z = 2 − 2i a aussi pour argument −π/4.
Cas limite : ces règles ne disent rien de z + z′ : l'argument d'une somme n'est pas la somme des arguments.
:::

::: verifie À toi : le quadrant tranche
Trouver un argument de z = 2 − 2i√3.

---

|z| = √(4 + 12) = 4, donc cos θ = 2/4 = 1/2 et sin θ = −2√3/4 = −√3/2. Le sinus est négatif, donc le point est dans le quatrième quadrant et θ = −π/3. Contrôle : 4(cos(−π/3) + i sin(−π/3)) = 4(1/2 − i√3/2) = 2 − 2i√3 ✓.
:::

::: retenir
Un argument de z est une mesure de (u⃗, OM⃗), défini à 2π près ; on le cherche par cos θ = a/r et sin θ = b/r avec le quadrant ; arg(z̄) = −arg(z) et arg(−z) = arg(z) + π.
:::

## 📐 Forme trigonométrique

Un bateau se repère par ses coordonnées (a ; b) sur la carte, ou par sa distance au port et son cap : 2 milles dans la direction 60°. Les deux écritures décrivent le même point.
Comment écrire un complexe avec sa distance r et son angle θ, et que deviennent alors le produit, le quotient et les puissances ?

::: definition
Soit z un complexe non nul, r = |z| et θ un argument de z. La **forme trigonométrique** de z est :
z = r(cos θ + i sin θ), notée [r, θ], avec r > 0
Les nombres a = r cos θ et b = r sin θ relient forme algébrique et forme trigonométrique.
:::

::: figure Les coordonnées polaires (r ; θ) repèrent M autant que (a ; b) : a = r cos θ et b = r sin θ
<svg viewBox="0 0 330 250">
<title>Le point M d'affixe 1 + i√3 repéré par ses coordonnées polaires : distance r = 2 à l'origine et angle θ = π/3</title>
<path d="M14 210 H322" fill="none" stroke="#0f172a" stroke-width="1.6"/>
<path d="M70 266 V42" fill="none" stroke="#0f172a" stroke-width="1.6"/>
<path d="M322 210 l-8 -4 l0 8 z" fill="#0f172a"/>
<path d="M70 42 l-4 8 l8 0 z" fill="#0f172a"/>
<path d="M140 207 V213" stroke="#0f172a" stroke-width="1.2"/>
<text x="140" y="226" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">1</text>
<path d="M210 207 V213" stroke="#0f172a" stroke-width="1.2"/>
<text x="210" y="226" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">2</text>
<path d="M280 207 V213" stroke="#0f172a" stroke-width="1.2"/>
<text x="280" y="226" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">3</text>
<path d="M67 140 H73" stroke="#0f172a" stroke-width="1.2"/>
<text x="63" y="144" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">i</text>
<path d="M67 70 H73" stroke="#0f172a" stroke-width="1.2"/>
<text x="63" y="74" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">2i</text>
<text x="64" y="225" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">O</text>
<path d="M140 88.76 L140 210" fill="none" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="5 4"/>
<path d="M140 88.76 L70 88.76" fill="none" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="5 4"/>
<path d="M70 210 L140 88.76" fill="none" stroke="#0f6e56" stroke-width="2.6"/>
<path d="M106 210 A36 36 0 0 0 88 178.82" fill="none" stroke="#b45309" stroke-width="2"/>
<circle cx="140" cy="88.76" r="4" fill="#0f172a"/>
<circle cx="140" cy="210" r="3" fill="#0f172a"/>
<circle cx="70" cy="88.76" r="3" fill="#0f172a"/>
<text x="148" y="84.76" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">M(1 + i√3)</text>
<text x="97" y="151.38" text-anchor="end" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">r = 2</text>
<text x="110.5" y="193.6" text-anchor="start" font-size="12" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">θ = π/3</text>
<text x="140" y="242" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">a = 1</text>
<text x="105" y="80.76" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">b = √3</text>
</svg>
:::

Sur la figure, le point M a pour coordonnées (a ; b) = (1 ; √3) ou pour coordonnées polaires (r ; θ) = (2 ; π/3) : la projection de OM sur l'axe des réels est a = r cos θ, sur l'axe des imaginaires b = r sin θ.

::: exemple De l'algébrique au trigonométrique, et retour

1. z = 1 + i√3 : r = √(1 + 3) = 2, cos θ = 1/2 et sin θ = √3/2, donc θ = π/3 et z = 2(cos π/3 + i sin π/3) = [2, π/3].
2. Contrôle : 2(1/2 + i√3/2) = 1 + i√3 ✓.
3. Dans l'autre sens, 4(cos(2π/3) + i sin(2π/3)) = 4(−1/2 + i√3/2) = −2 + 2i√3, car cos(2π/3) = −1/2 et sin(2π/3) = √3/2.

:::

::: piege
**Erreur : prendre 2(cos π/3 − i sin π/3) pour une forme trigonométrique.** L'erreur tente parce que le signe « − » semble une variante inoffensive. Mais la forme exige un « + » entre cos θ et i sin θ avec le même θ. Comme cos π/3 = cos(−π/3) et −sin π/3 = sin(−π/3), ce nombre est 2(cos(−π/3) + i sin(−π/3)) = [2, −π/3] : c'est le conjugué de [2, π/3].
:::

::: propriete
Soit z = [r, θ] et z′ = [r′, θ′] deux complexes non nuls, et n un entier :
z × z′ = [r r′, θ + θ′] ; z/z′ = [r/r′, θ − θ′] ; 1/z = [1/r, −θ] ; z̄ = [r, −θ] ; zⁿ = [rⁿ, nθ]
Les modules se multiplient, les arguments s'additionnent. Cas limite : le module reste positif, et si l'angle sort de ]−π ; π] on lui ajoute ou retranche 2π ; ainsi [4, −π] = [4, π] = −4.
:::

::: exemple Un quotient de puissances

1. 1 + i√3 = [2, π/3], donc (1 + i√3)⁶ = [2⁶, 6 × π/3] = [64, 2π] = 64.
2. 1 − i = [√2, −π/4], donc (1 − i)⁴ = [(√2)⁴, 4 × (−π/4)] = [4, −π] = −4.
3. Le quotient vaut 64/(−4) = −16. Contrôle algébrique : (1 − i)² = −2i, donc (1 − i)⁴ = (−2i)² = −4 ✓ ; et (1 + i√3)³ = (−2 + 2i√3)(1 + i√3) = −2 − 2i√3 + 2i√3 − 6 = −8, donc (1 + i√3)⁶ = 64 ✓.

:::

::: verifie À toi : un produit d'angles
Calculer [3, 5π/6] × [2, π/6] et donner le résultat sous forme algébrique.

---

Les modules se multiplient, 3 × 2 = 6, et les arguments s'additionnent, 5π/6 + π/6 = π. Le produit est [6, π] = 6(cos π + i sin π) = 6 × (−1) = −6.
:::

::: retenir
z = r(cos θ + i sin θ) avec r = |z| > 0 et θ = arg(z) ; a = r cos θ et b = r sin θ ; modules multipliés et arguments additionnés dans un produit : [r, θ] × [r′, θ′] = [r r′, θ + θ′].
:::

## ⚡ Forme exponentielle et formule de Moivre

Dans [r, θ] × [r′, θ′] = [r r′, θ + θ′], les modules se multiplient et les angles s'additionnent : c'est la règle des puissances aᵖ × aᵠ = aᵖ⁺ᵠ, où les exposants s'ajoutent. On cherche une écriture qui fasse de cette ressemblance une égalité.
Quelle notation transforme les angles en exposants, et que devient alors une puissance entière ?

::: definition
Pour tout réel θ, on pose **e^(iθ) = cos θ + i sin θ**. C'est le nombre de module 1 et d'argument θ. Si z = [r, θ], son **écriture exponentielle** est z = r e^(iθ).
Valeurs à connaître : e^(i0) = 1, e^(iπ/2) = i, e^(iπ) = −1, e^(−iπ/2) = −i.
:::

::: propriete
Pour z = r e^(iθ) et z′ = r′ e^(iθ′), et n entier :
z × z′ = r r′ e^(i(θ + θ′)) ; z/z′ = (r/r′) e^(i(θ − θ′)) ; 1/z = (1/r) e^(−iθ) ; z̄ = r e^(−iθ) ; zⁿ = rⁿ e^(inθ)
**Formule de Moivre** : pour tout réel θ et tout entier n, (cos θ + i sin θ)ⁿ = cos(nθ) + i sin(nθ).
**Réel ou imaginaire pur** : z est réel ⇔ arg(z) = kπ (k entier) ou z = 0 ; z est imaginaire pur ⇔ arg(z) = π/2 + kπ.
:::

::: exemple Une puissance, et un contrôle algébrique

1. z = −1 + i : r = √2 et θ = 3π/4, donc z = √2 e^(i3π/4).
2. z⁴ = (√2)⁴ e^(i4 × 3π/4) = 4 e^(i3π) = 4 e^(iπ) = −4, car on retranche 2π à l'angle.
3. Contrôle : z² = 1 − 2i + i² = −2i, et (−2i)² = −4 ✓.

:::

::: figure Multiplier z par z′, c'est multiplier les modules et additionner les arguments : π/4 + π/6 = 5π/12
<svg viewBox="0 -10 335 270">
<title>Les points z = 1 + i, z′ = √3 + i et zz′ : l'argument de zz′, 5π/12, est la somme π/4 + π/6 des arguments</title>
<path d="M8 235 H328" fill="none" stroke="#0f172a" stroke-width="1.6"/>
<path d="M40 267 V-5" fill="none" stroke="#0f172a" stroke-width="1.6"/>
<path d="M328 235 l-8 -4 l0 8 z" fill="#0f172a"/>
<path d="M40 -5 l-4 8 l8 0 z" fill="#0f172a"/>
<path d="M120 232 V238" stroke="#0f172a" stroke-width="1.2"/>
<text x="120" y="251" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">1</text>
<path d="M200 232 V238" stroke="#0f172a" stroke-width="1.2"/>
<text x="200" y="251" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">2</text>
<path d="M280 232 V238" stroke="#0f172a" stroke-width="1.2"/>
<text x="280" y="251" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">3</text>
<path d="M37 155 H43" stroke="#0f172a" stroke-width="1.2"/>
<text x="33" y="159" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">i</text>
<path d="M37 75 H43" stroke="#0f172a" stroke-width="1.2"/>
<text x="33" y="79" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">2i</text>
<path d="M37 -5 H43" stroke="#0f172a" stroke-width="1.2"/>
<text x="33" y="-1" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">3i</text>
<text x="34" y="250" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">O</text>
<path d="M40 235 L178.56 155" fill="none" stroke="#94a3b8" stroke-width="2"/>
<path d="M40 235 L120 155" fill="none" stroke="#0f6e56" stroke-width="2.2"/>
<path d="M40 235 L98.56 16.44" fill="none" stroke="#b45309" stroke-width="2.6"/>
<path d="M98 235 A58 58 0 0 0 90.23 206" fill="none" stroke="#94a3b8" stroke-width="2"/>
<path d="M76.37 214 A42 42 0 0 0 50.87 194.43" fill="none" stroke="#b45309" stroke-width="2"/>
<circle cx="120" cy="155" r="4" fill="#0f172a"/>
<circle cx="178.56" cy="155" r="4" fill="#0f172a"/>
<circle cx="98.56" cy="16.44" r="4" fill="#0f172a"/>
<text x="106.56" y="20.44" text-anchor="start" font-size="12" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">zz′</text>
<text x="114" y="147" text-anchor="end" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">z</text>
<text x="186.56" y="159" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">z′</text>
<text x="118" y="225" text-anchor="start" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">π/6</text>
<text x="54" y="175.4" text-anchor="start" font-size="11" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">+ π/4</text>
</svg>
:::

La figure place z = 1 + i, z′ = √3 + i et leur produit : l'angle de zz′ est la somme π/4 + π/6, et son module est le produit √2 × 2.

::: exemple Les valeurs exactes de cos(5π/12) et sin(5π/12)

1. z = 1 + i = √2 e^(iπ/4) et z′ = √3 + i = 2 e^(iπ/6), donc zz′ = 2√2 e^(i5π/12), car π/4 + π/6 = 5π/12.
2. En forme algébrique, zz′ = √3 + i + i√3 + i² = (√3 − 1) + i(√3 + 1).
3. On identifie : 2√2 cos(5π/12) = √3 − 1 et 2√2 sin(5π/12) = √3 + 1. D'où cos(5π/12) = (√3 − 1)/(2√2) = (√6 − √2)/4 et sin(5π/12) = (√6 + √2)/4. Contrôle : ≈ 0,259 et 0,966, ce sont cos 75° et sin 75° ✓.

:::

::: exemple Quand une puissance est réelle ou imaginaire pure

1. (1 + i)ⁿ = (√2)ⁿ e^(inπ/4). Il est réel ⇔ nπ/4 = kπ ⇔ n multiple de 4. Pour n = 4 : (1 + i)⁴ = (2i)² = −4 ✓.
2. Il est imaginaire pur ⇔ nπ/4 = π/2 + kπ ⇔ n = 2 + 4k. Pour n = 2 : (1 + i)² = 2i ✓.

:::

::: piege
**Erreur : écrire (2 e^(iπ/6))³ = 8 e^(iπ/6).** L'erreur tente parce que le module est bien élevé au cube et que l'on oublie l'angle. Mais l'exposant multiplie aussi l'argument : (r e^(iθ))ⁿ = rⁿ e^(inθ). Ici (2 e^(iπ/6))³ = 8 e^(iπ/2) = 8i. Contrôle : 2 e^(iπ/6) = √3 + i, et (√3 + i)³ = (2 + 2i√3)(√3 + i) = 8i ✓.
:::

::: verifie À toi : une puissance de 1 − i
Écrire (1 − i)⁶ sous forme algébrique, en passant par la forme exponentielle.

---

1 − i = √2 e^(−iπ/4), donc (1 − i)⁶ = (√2)⁶ e^(−i6π/4) = 8 e^(−i3π/2). On ajoute 2π à l'angle : −3π/2 + 2π = π/2, d'où 8 e^(iπ/2) = 8i. Contrôle : (1 − i)² = −2i et (−2i)³ = −8i³ = 8i ✓.
:::

::: retenir
e^(iθ) = cos θ + i sin θ ; z = r e^(iθ) ; produit et quotient : on multiplie ou divise les modules et on additionne ou retranche les angles ; zⁿ = rⁿ e^(inθ) (Moivre) ; z est réel ⇔ arg(z) = kπ.
:::

## 🌀 Formules d'Euler et linéarisation

Au chapitre sur le calcul intégral, on ne sait pas trouver à vue une primitive de cos²x. En revanche, une primitive de cos(2x) est immédiate. Si l'on savait écrire cos²x comme une somme de termes en cos(kx), l'intégrale se calculerait.
Comment transformer une puissance de cos x ou de sin x en somme de cosinus et de sinus d'angles multiples de x ?

::: propriete
**Formules d'Euler** : pour tout réel θ,
cos θ = (e^(iθ) + e^(−iθ))/2 et sin θ = (e^(iθ) − e^(−iθ))/(2i)
:::

::: figure Le point e^(iθ) et son symétrique e^(−iθ) ont une somme réelle : leur milieu a pour affixe cos θ, d'où la formule d'Euler
<svg viewBox="0 0 340 250">
<title>Les points e^(iθ) et e^(−iθ) sont symétriques par rapport à l'axe des réels ; leur somme est réelle et vaut 2cos θ (ici θ = π/4)</title>
<path d="M10 125 H330" fill="none" stroke="#0f172a" stroke-width="1.6"/>
<path d="M100 245 V5" fill="none" stroke="#0f172a" stroke-width="1.6"/>
<path d="M330 125 l-8 -4 l0 8 z" fill="#0f172a"/>
<path d="M100 5 l-4 8 l8 0 z" fill="#0f172a"/>
<path d="M200 122 V128" stroke="#0f172a" stroke-width="1.2"/>
<text x="200" y="141" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">1</text>
<path d="M97 25 H103" stroke="#0f172a" stroke-width="1.2"/>
<text x="93" y="29" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">i</text>
<path d="M97 225 H103" stroke="#0f172a" stroke-width="1.2"/>
<text x="93" y="229" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">−i</text>
<text x="94" y="140" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">O</text>
<circle cx="100" cy="125" r="100" fill="none" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="5 4"/>
<path d="M170.71 54.29 L241.42 125" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-dasharray="5 4"/>
<path d="M170.71 195.71 L241.42 125" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-dasharray="5 4"/>
<path d="M100 125 L170.71 54.29" fill="none" stroke="#0f6e56" stroke-width="2.4"/>
<path d="M100 125 L170.71 195.71" fill="none" stroke="#b45309" stroke-width="2.4"/>
<path d="M100 125 L241.42 125" fill="none" stroke="#0f172a" stroke-width="2.6"/>
<path d="M130 125 A30 30 0 0 0 121.21 103.79" fill="none" stroke="#0f6e56" stroke-width="2"/>
<circle cx="170.71" cy="54.29" r="4" fill="#0f172a"/>
<circle cx="170.71" cy="195.71" r="4" fill="#0f172a"/>
<circle cx="241.42" cy="125" r="4" fill="#0f172a"/>
<text x="164.71" y="46.29" text-anchor="end" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">e<tspan dy="-5" font-size="9">iθ</tspan></text>
<text x="164.71" y="211.71" text-anchor="end" font-size="12" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">e<tspan dy="-5" font-size="9">−iθ</tspan></text>
<text x="245.42" y="145" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">2cos θ</text>
<text x="134" y="119" text-anchor="start" font-size="11" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">θ</text>
</svg>
:::

Sur la figure, e^(iθ) et e^(−iθ) sont conjugués : leur somme est réelle et vaut 2 cos θ, deux fois la partie réelle de e^(iθ) ; leur différence, 2i sin θ, est imaginaire pure.

::: methode Linéariser une puissance ou un produit de cos x et de sin x

1. On remplace cos x ou sin x par sa formule d'Euler, et l'on développe avec le binôme : (a + b)² = a² + 2ab + b², (a + b)³ = a³ + 3a²b + 3ab² + b³, (a + b)⁴ = a⁴ + 4a³b + 6a²b² + 4ab³ + b⁴.
2. On regroupe les termes conjugués : e^(ikx) + e^(−ikx) = 2 cos(kx) et e^(ikx) − e^(−ikx) = 2i sin(kx).
3. On simplifie par les constantes : il ne reste que des cos(kx) ou des sin(kx) au premier degré.

:::

::: exemple Linéariser cos²x, puis intégrer

1. cos²x = ((e^(ix) + e^(−ix))/2)² = (e^(2ix) + 2 + e^(−2ix))/4, par le carré d'une somme, avec e^(ix) × e^(−ix) = 1.
2. e^(2ix) + e^(−2ix) = 2 cos 2x, donc cos²x = (2 cos 2x + 2)/4 = (1 + cos 2x)/2. Contrôle : x = 0 donne 1 = (1 + 1)/2 ✓ ; x = π/2 donne 0 = (1 − 1)/2 ✓.
3. Une primitive de cos²x est donc x/2 + sin(2x)/4. Contrôle : la dérivée est 1/2 + cos(2x)/2 = cos²x ✓.

:::

::: exemple Linéariser un produit : cos²x sin x

1. On remplace chaque facteur par sa formule d'Euler, en reprenant le carré déjà calculé : cos²x sin x = (e^(2ix) + 2 + e^(−2ix))/4 × (e^(ix) − e^(−ix))/(2i).
2. On développe le produit des parenthèses : e^(3ix) − e^(ix) + 2e^(ix) − 2e^(−ix) + e^(−ix) − e^(−3ix) = (e^(3ix) − e^(−3ix)) + (e^(ix) − e^(−ix)) = 2i sin 3x + 2i sin x.
3. On divise par 4 × 2i = 8i : cos²x sin x = (sin x + sin 3x)/4. Contrôle : x = π/6 donne 3/4 × 1/2 = 3/8 et (1/2 + 1)/4 = 3/8 ✓.

:::

::: exemple Le chemin inverse : cos 3x avec Moivre

1. Par Moivre, cos 3x + i sin 3x = (cos x + i sin x)³. Le binôme avec a = cos x et b = i sin x donne cos³x + 3i cos²x sin x − 3 cos x sin²x − i sin³x, car (i sin x)² = −sin²x et (i sin x)³ = −i sin³x.
2. On identifie les parties réelles : cos 3x = cos³x − 3 cos x sin²x.
3. Avec sin²x = 1 − cos²x : cos 3x = cos³x − 3 cos x + 3 cos³x = 4 cos³x − 3 cos x. Contrôle : x = 0 donne 1 = 4 − 3 ✓.

:::

::: piege
**Erreur : écrire ((e^(ix) + e^(−ix))/2)² = (e^(2ix) + e^(−2ix))/4, donc cos²x = cos(2x)/2.** L'erreur tente parce que l'on oublie le double produit du carré d'une somme. Mais (a + b)² = a² + 2ab + b² : le terme 2 e^(ix) e^(−ix) = 2 subsiste. Test avec x = 0 : cos²0 = 1 alors que cos(0)/2 = 1/2.
:::

::: verifie À toi : le sinus de 3x
Avec la méthode de Moivre, exprimer sin 3x en fonction de sin x seulement.

---

Les parties imaginaires de (cos x + i sin x)³ donnent sin 3x = 3 cos²x sin x − sin³x. On remplace cos²x par 1 − sin²x : sin 3x = 3(1 − sin²x) sin x − sin³x = 3 sin x − 3 sin³x − sin³x = 3 sin x − 4 sin³x. Contrôle : x = π/2 donne sin(3π/2) = −1 = 3 − 4 ✓.
:::

::: retenir
cos θ = (e^(iθ) + e^(−iθ))/2 et sin θ = (e^(iθ) − e^(−iθ))/(2i) ; pour linéariser, on développe avec le binôme puis on regroupe les couples e^(ikx), e^(−ikx) ; pour exprimer cos nx ou sin nx, on développe (cos x + i sin x)ⁿ.
:::

## 📏 Angles orientés, colinéarité et orthogonalité

Un géomètre connaît seulement les affixes de trois balises A, B et C. Il veut savoir, sans tracer, si elles sont alignées ou si le triangle est rectangle isocèle. Il lui faut lire un angle et un rapport de longueurs dans les nombres.
Quelle quantité, calculée à partir des affixes, contient à la fois l'angle (AB⃗, AC⃗) et le rapport AC/AB ?

::: propriete
Soit A, B, C, D quatre points avec A ≠ B et C ≠ D. Les angles se lisent dans les arguments :
(u⃗, AB⃗) = arg(z_B − z_A) et (AB⃗, CD⃗) = arg((z_D − z_C)/(z_B − z_A)) (à 2π près)
De plus CD/AB = |(z_D − z_C)/(z_B − z_A)|.
**Colinéarité** : AB⃗ et CD⃗ sont colinéaires ⇔ (z_D − z_C)/(z_B − z_A) est réel.
**Orthogonalité** : AB⃗ et CD⃗ sont orthogonaux ⇔ (z_D − z_C)/(z_B − z_A) est imaginaire pur (non nul).
:::

::: figure Le quotient (z_C − z_A)/(z_B − z_A) = i signifie AC = AB et un angle droit en A
<svg viewBox="0 0 300 260">
<title>Le triangle ABC avec A(1 + i), B(4 + 2i) et C(4i) : en A, les côtés AB et AC sont perpendiculaires et de même longueur √10</title>
<path d="M20.8 225 H289.6" fill="none" stroke="#0f172a" stroke-width="1.6"/>
<path d="M40 244.2 V13.8" fill="none" stroke="#0f172a" stroke-width="1.6"/>
<path d="M289.6 225 l-8 -4 l0 8 z" fill="#0f172a"/>
<path d="M40 13.8 l-4 8 l8 0 z" fill="#0f172a"/>
<path d="M88 222 V228" stroke="#0f172a" stroke-width="1.2"/>
<text x="88" y="241" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">1</text>
<path d="M136 222 V228" stroke="#0f172a" stroke-width="1.2"/>
<text x="136" y="241" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">2</text>
<path d="M184 222 V228" stroke="#0f172a" stroke-width="1.2"/>
<text x="184" y="241" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">3</text>
<path d="M232 222 V228" stroke="#0f172a" stroke-width="1.2"/>
<text x="232" y="241" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">4</text>
<path d="M37 177 H43" stroke="#0f172a" stroke-width="1.2"/>
<text x="33" y="181" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">i</text>
<path d="M37 129 H43" stroke="#0f172a" stroke-width="1.2"/>
<text x="33" y="133" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">2i</text>
<path d="M37 81 H43" stroke="#0f172a" stroke-width="1.2"/>
<text x="33" y="85" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">3i</text>
<path d="M37 33 H43" stroke="#0f172a" stroke-width="1.2"/>
<text x="33" y="37" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">4i</text>
<text x="34" y="240" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">O</text>
<polygon points="88,177 232,129 40,33" fill="#0f6e56" fill-opacity="0.10" stroke="#0f6e56" stroke-width="2.4"/>
<path d="M96.54 174.15 L93.69 165.62 L85.15 168.46" fill="none" stroke="#0f172a" stroke-width="1.4"/>
<circle cx="88" cy="177" r="4" fill="#0f172a"/>
<circle cx="232" cy="129" r="4" fill="#0f172a"/>
<circle cx="40" cy="33" r="4" fill="#0f172a"/>
<text x="94" y="193" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">A(1 + i)</text>
<text x="214" y="150" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">B(4 + 2i)</text>
<text x="48" y="29" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">C(4i)</text>
</svg>
:::

Sur la figure, A(1 + i), B(4 + 2i) et C(4i) donnent z_B − z_A = 3 + i et z_C − z_A = −1 + 3i : le quotient des deux contient l'angle droit en A et l'égalité des longueurs AB et AC.

::: exemple Un triangle rectangle isocèle

1. Les affixes des vecteurs sont z_B − z_A = 3 + i et z_C − z_A = −1 + 3i.
2. Quotient : (−1 + 3i)/(3 + i) = (−1 + 3i)(3 − i)/10 = (−3 + i + 9i + 3)/10 = 10i/10 = i.
3. |i| = 1 donne AC = AB, et arg(i) = π/2 donne (AB⃗, AC⃗) = π/2 : le triangle est rectangle isocèle en A. Contrôle : AB = AC = √10, et le produit scalaire 3 × (−1) + 1 × 3 = 0 ✓.

:::

::: exemple Aligner, et rendre perpendiculaire

1. A(1 + i), B(3 + 2i), C(7 + 4i) : (z_C − z_A)/(z_B − z_A) = (6 + 3i)/(2 + i) = 3, un réel, donc A, B, C sont alignés, avec AC⃗ = 3 AB⃗.
2. A(1), B(2 + i), C(0), D(−2 + 2i) : (z_D − z_C)/(z_B − z_A) = (−2 + 2i)/(1 + i) = (−2 + 2i)(1 − i)/2 = 4i/2 = 2i, un imaginaire pur. Donc (AB) ⟂ (CD), avec CD = 2 AB.

:::

::: piege
**Erreur : lire l'angle (AB⃗, AC⃗) dans arg(z_C/z_B).** L'erreur tente parce que le quotient des affixes semble une bonne « comparaison » de B et de C. Mais un angle de vecteurs exige des différences. Avec A(1 + i), B(4 + 2i), C(4i) : z_C/z_B = 4i/(4 + 2i) = (2 + 4i)/5, d'argument environ 63°, alors que l'angle en A est droit. Il faut aussi respecter l'ordre : (AC⃗, AB⃗) = arg(1/i) = −π/2, l'opposé.
:::

::: verifie À toi : un triangle équilatéral
Montrer que A(0), B(2) et C(1 + i√3) forment un triangle équilatéral.

---

Les affixes des vecteurs sont z_B − z_A = 2 et z_C − z_A = 1 + i√3. Le quotient (1 + i√3)/2 = 1/2 + i√3/2 = cos π/3 + i sin π/3 est de module 1 : AC = AB. Son argument est π/3 : l'angle en A mesure 60°. Un triangle isocèle d'angle au sommet 60° est équilatéral.
:::

::: retenir
(AB⃗, CD⃗) = arg((z_D − z_C)/(z_B − z_A)) et CD/AB est le module de ce quotient ; quotient réel ⇔ vecteurs colinéaires ; quotient imaginaire pur ⇔ vecteurs orthogonaux.
:::

## 🎯 Ensembles de points décrits par une équation en z

Un capitaine veut rester à 2 milles d'une bouée Ω. Tous les points M qui conviennent forment une courbe qu'il sait nommer, mais l'équation qui la décrit est écrite avec des nombres complexes.
Comment lire géométriquement une équation du type |z − a| = r, ou une condition « réel » ou « imaginaire pur » sur un quotient ?

::: propriete
Soit A(a) et B(b) deux points distincts, M(z) un point du plan et r > 0.
|z − a| = r ⇔ AM = r : M décrit le cercle de centre A et de rayon r.
|z − a| = |z − b| ⇔ MA = MB : M décrit la médiatrice de [AB].
Pour Z = (z − a)/(z − b) avec z ≠ b : Z est réel ⇔ M appartient à la droite (AB) ; Z est imaginaire pur non nul ⇔ MA ⟂ MB, c'est-à-dire M appartient au cercle de diamètre [AB].
Cas limite : dans le dernier cas, M ≠ A et M ≠ B ; et dans tous les cas z = b est exclu, puisque Z n'y est pas défini.
:::

::: methode Un ensemble par le calcul, quand la lecture géométrique manque

1. On pose z = x + iy et on traduit la condition par une équation en x et y : un module au carré devient (x − p)² + (y − q)² = r², un quotient réel ou imaginaire pur s'étudie avec ses parties réelle et imaginaire.
2. On reconnaît la droite ou le cercle, avec son centre, son rayon ou son équation.
3. On retire les points où l'expression n'est pas définie, et ceux que la condition exclut.

:::

::: exemple Un cercle et une médiatrice

1. |z − 2 + i| = 3 s'écrit |z − (2 − i)| = 3 : M décrit le cercle de centre Ω(2 − i) et de rayon 3. Contrôle : (x − 2)² + (y + 1)² = 9 ✓.
2. |z − 2| = |z − 2i| : avec A(2) et B(2i), M décrit la médiatrice de [AB]. Par le calcul : (x − 2)² + y² = x² + (y − 2)² ⇔ −4x + 4 = −4y + 4 ⇔ y = x. Contrôle : le milieu I(1 + i) vérifie bien y = x ✓.

:::

::: figure Pour A(2) et B(2i), les points M tels que (z − 2)/(z − 2i) soit réel forment la droite (AB) privée de B, et ceux où il est imaginaire pur le cercle de diamètre [AB] privé de A et de B
<svg viewBox="0 0 300 250">
<title>Le cercle de diamètre [AB] et la droite (AB), avec A(2) et B(2i) : sur le cercle, l'angle en M est droit ; sur la droite, M, A et B sont alignés</title>
<path d="M16 205 H258" fill="none" stroke="#0f172a" stroke-width="1.6"/>
<path d="M60 249 V29" fill="none" stroke="#0f172a" stroke-width="1.6"/>
<path d="M258 205 l-8 -4 l0 8 z" fill="#0f172a"/>
<path d="M60 29 l-4 8 l8 0 z" fill="#0f172a"/>
<path d="M115 202 V208" stroke="#0f172a" stroke-width="1.2"/>
<text x="115" y="221" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">1</text>
<path d="M170 202 V208" stroke="#0f172a" stroke-width="1.2"/>
<text x="170" y="221" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">2</text>
<path d="M225 202 V208" stroke="#0f172a" stroke-width="1.2"/>
<text x="225" y="221" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">3</text>
<path d="M57 150 H63" stroke="#0f172a" stroke-width="1.2"/>
<text x="53" y="154" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">i</text>
<path d="M57 95 H63" stroke="#0f172a" stroke-width="1.2"/>
<text x="53" y="99" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">2i</text>
<path d="M57 40 H63" stroke="#0f172a" stroke-width="1.2"/>
<text x="53" y="44" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">3i</text>
<text x="54" y="220" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">O</text>
<circle cx="115" cy="150" r="77.78" fill="#0f6e56" fill-opacity="0.10"/>
<circle cx="115" cy="150" r="77.78" fill="none" stroke="#0f6e56" stroke-width="2.4"/>
<path d="M32.5 67.5 L203 238" fill="none" stroke="#b45309" stroke-width="2.4"/>
<path d="M185.49 117.13 L170 205" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-dasharray="5 4"/>
<path d="M185.49 117.13 L60 95" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-dasharray="5 4"/>
<path d="M184.11 125.01 L176.23 123.62 L177.62 115.74" fill="none" stroke="#0f172a" stroke-width="1.4"/>
<circle cx="170" cy="205" r="4" fill="#0f172a"/>
<circle cx="60" cy="95" r="4" fill="#0f172a"/>
<circle cx="185.49" cy="117.13" r="3.5" fill="#0f172a"/>
<circle cx="115" cy="150" r="3" fill="#0f172a"/>
<text x="180" y="227" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">A(2)</text>
<text x="52" y="89" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">B(2i)</text>
<text x="193.49" y="111.13" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">M</text>
<text x="109" y="166" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">I</text>
<text x="39.25" y="70.5" text-anchor="start" font-size="12" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">(AB)</text>
</svg>
:::

La figure montre, pour A(2) et B(2i), les deux ensembles du quotient Z = (z − 2)/(z − 2i) : la droite (AB) et le cercle de diamètre [AB], de centre I(1 + i).

::: exemple Quand Z = (z − 2)/(z − 2i) est réel, puis imaginaire pur

1. Avec z = x + iy, Z = (x − 2 + iy)/(x + i(y − 2)). On multiplie par le conjugué du dénominateur : le numérateur devient (x − 2 + iy)(x − i(y − 2)).
2. Partie réelle du numérateur : x(x − 2) + y(y − 2) = x² + y² − 2x − 2y. Partie imaginaire : xy − (x − 2)(y − 2) = 2x + 2y − 4. Le dénominateur x² + (y − 2)² est positif.
3. Z est réel ⇔ 2x + 2y − 4 = 0 ⇔ x + y = 2 : la droite (AB), privée de B. Z est imaginaire pur ⇔ x² + y² − 2x − 2y = 0 ⇔ (x − 1)² + (y − 1)² = 2 : le cercle de centre I(1 + i) et de rayon √2, privé de A et de B. Contrôle : AB = |2i − 2| = 2√2, dont la moitié est √2 ✓.

:::

::: piege
**Erreur : dire que Z est réel sur la droite (AB) tout entière.** L'erreur tente parce que le quotient réel traduit l'alignement, et que (AB) contient les deux points. Mais Z n'est pas défini au point B, où le dénominateur est nul. De même, au point A, Z = 0 n'est pas un imaginaire pur non nul : le cercle de diamètre [AB] est privé de A et de B.
:::

::: verifie À toi : une médiatrice
Déterminer l'ensemble des points M(z) tels que |z + 1| = |z − 3i|.

---

C'est l'ensemble des points équidistants de A(−1) et de B(3i) : la médiatrice de [AB]. Par le calcul, (x + 1)² + y² = x² + (y − 3)² ⇔ 2x + 1 = −6y + 9 ⇔ x + 3y = 4. Contrôle : le milieu de [AB], (−1/2 ; 3/2), vérifie −1/2 + 9/2 = 4 ✓.
:::

::: retenir
|z − a| = r est un cercle de centre A ; |z − a| = |z − b| est la médiatrice de [AB] ; (z − a)/(z − b) réel donne la droite (AB) privée de B, imaginaire pur le cercle de diamètre [AB] privé de A et de B.
:::

> 🏆 Les huit portes sont franchies : tu sais calculer dans ℂ, lire un module comme une distance et un argument comme un angle, passer d'une forme à l'autre, linéariser avec Euler, et traduire une équation en z en droite ou en cercle. Prochaine étape : les équations à coefficients complexes.
