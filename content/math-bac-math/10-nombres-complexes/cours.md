# ⚔️ Nombres complexes — l'algèbre qui dessine le plan

> 💡 «Un nombre dont le carré vaut −1 n'existe pas sur la droite réelle. Il existe dans le plan — et il y range toutes les distances, tous les angles et toutes les rotations.»

À partir de la seconde moitié du XVIIᵉ siècle, les géomètres écrivent √−1 sans trop savoir ce qu'ils manipulent. En 1748, Euler pose e^(ix) = cos x + i sin x, formule dont on a dit qu'elle réunit « les symboles les plus importants » : l'arithmétique par 0 et 1, l'algèbre par i, la géométrie par π, l'analyse par e. Ce chapitre ouvre le **tome 2** et te donne cet outil : il résout **toutes** les équations du second degré, et transforme un calcul de longueurs et d'angles en un simple quotient.

## 🏰 L'ensemble ℂ : forme algébrique et conjugué

Tu sais déjà que x² + 1 = 0 n'a pas de solution réelle : un carré est toujours positif. On construit alors un ensemble plus grand où cette équation a une solution.

> **Théorème et définition (rappel)** (p.6) — « Il existe un ensemble appelé ensemble des nombres complexes, noté ℂ et vérifiant les propriétés ci-dessous. 1. L'ensemble ℂ contient l'ensemble des nombres réels ℝ. 2. Il existe un élément de ℂ, noté i, tel que i² = −1. 3. L'ensemble ℂ est muni d'une addition et d'une multiplication qui vérifient les mêmes propriétés que l'addition et la multiplication dans ℝ. 4. Tout élément z de ℂ s'écrit de façon unique sous la forme z = a + ib, où a et b sont des réels. »

L'écriture z = a + ib est la **forme algébrique** (ou cartésienne) de z ; a = Re(z) est sa **partie réelle**, b = Im(z) sa **partie imaginaire** (un réel, pas un imaginaire). Le mot « de façon unique » est le moteur de tout le chapitre : identifier deux complexes, c'est identifier deux couples de réels.

> **Conséquences** (p.6) — « Soit z = a + ib et z′ = a′ + ib′, où a, a′, b et b′ sont des réels. Alors z = z′, si et seulement si, a = a′ et b = b′. z = 0, si et seulement si, a = b = 0. z est réel, si et seulement si, b = 0. z est imaginaire, si et seulement si, a = 0. »

On calcule dans ℂ **exactement** comme dans ℝ, avec la seule règle supplémentaire i² = −1.

_Exemple détaillé_ — écrivons (2 − 2i)(1 + i)² sous forme algébrique. D'abord (1 + i)² = 1 + 2i + i² = 1 + 2i − 1 = **2i**. Donc :

$$ (2 − 2i)(1 + i)² = (2 − 2i) × 2i = 4i − 4i² = 4i + 4 = 4 + 4i $$

_Contrôle par un autre chemin_ : (2 − 2i)(1 + i) = 2 + 2i − 2i + 2 = 4, puis 4 × (1 + i) = 4 + 4i ✓.

Pour diviser, on multiplie haut et bas par le **conjugué** du dénominateur. Le conjugué de z = a + ib est z̄ = a − ib.

_Exemple détaillé_ — calculons z/z′ pour z = 1 + 2i et z′ = i. Comme ī = −i et i(−i) = 1 :

$$ (1 + 2i)/i = (1 + 2i)(−i)/(i × (−i)) = (−i − 2i²)/1 = 2 − i $$

_Contrôle par réinjection_ : (2 − i) × i = 2i − i² = 2i + 1 = 1 + 2i ✓.

> **Propriétés** (p.7) — « Pour tous nombres complexes z et z′, (z + z′)‾ = z̄ + z̄′ ; (zz′)‾ = z̄ z̄′ ; (zⁿ)‾ = (z̄)ⁿ ; n ∈ ℕ\*. Pour tout nombre complexe z et tout nombre complexe non nul z′, (z/z′)‾ = z̄/z̄′ ; (1/z′ⁿ)‾ = 1/(z̄′)ⁿ, n ∈ ℤ. z + z̄ = 2 Re(z) ; z − z̄ = 2i Im(z) ; zz̄ = (Re(z))² + (Im(z))². z = z̄, si et seulement si, z est réel. z = −z̄, si et seulement si, z est imaginaire. »

Les deux dernières lignes sont des **tests** que tu utiliseras sans arrêt : « z est réel » se démontre en prouvant z = z̄, « z est imaginaire » en prouvant z = −z̄.

_Exemple détaillé (équation)_ — résolvons (z − i)/(z + i) = 2i, avec z ≠ −i. On chasse le dénominateur : z − i = 2i(z + i) = 2iz + 2i² = 2iz − 2. D'où z − 2iz = −2 + i, soit z(1 − 2i) = −2 + i, puis :

$$ z = (−2 + i)/(1 − 2i) = (−2 + i)(1 + 2i)/(1² + 2²) = (−2 − 4i + i − 2)/5 = (−4 − 3i)/5 $$

_Contrôle par réinjection_ : z = −0,8 − 0,6i, donc z − i = −0,8 − 1,6i et z + i = −0,8 + 0,4i ; le quotient vaut (−0,8 − 1,6i)(−0,8 − 0,4i)/0,8 = 1,6i/0,8 = 2i ✓.

> ⚠️ **i² = −1, mais i⁴ = 1.** Les puissances de i tournent de 4 en 4 : i⁰ = 1, i¹ = i, i² = −1, i³ = −i, i⁴ = 1… Pour iⁿ, divise n par 4 et ne garde que le reste. Et surtout : **ℂ n'est pas ordonné** — écrire « z > 0 » ou « Δ < 0 » pour un complexe n'a aucun sens.

## 🗺️ Le plan complexe : affixes, module et distances

Le plan est muni d'un repère orthonormé **direct** (O, u⃗, v⃗). À tout point M de coordonnées (a, b) on associe le complexe z = a + ib, appelé **affixe** de M, et on note M(z). Réciproquement, tout complexe a son point image : ℂ et le plan se correspondent point par point.

L'affixe d'un vecteur w⃗ = MN⃗ est z_N − z_M, et cette correspondance est linéaire : Aff(αw⃗ + βw₁⃗) = α Aff(w⃗) + β Aff(w₁⃗).

Le **module** de z = a + ib est le réel positif |z| = √(a² + b²) = OM. Et, en appliquant cela au vecteur MN⃗ :

$$ MN = |z_N − z_M| $$

C'est la clé de tout le chapitre : **un module est une longueur**.

::: figure Le module |z| est la longueur OM, et |z_N − z_M| la longueur MN : lire un module, c'est lire une distance sur la figure.
<svg viewBox="0 0 340 260"><path d="M20 190 H330" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M110 245 V20" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M330 190 l-8 -4 l0 8 z" fill="#0f172a"/><path d="M110 20 l-4 8 l8 0 z" fill="#0f172a"/><path d="M230 110 V190 M230 110 H110" fill="none" stroke="#94a3b8" stroke-width="1.3" stroke-dasharray="5 4"/><path d="M110 190 L230 110" fill="none" stroke="#0f6e56" stroke-width="2.6"/><path d="M230 110 L70 150" fill="none" stroke="#b45309" stroke-width="2.2"/><path d="M110 190 L150 190 M110 190 L110 150" fill="none" stroke="#0f172a" stroke-width="3.4"/><g fill="#0f172a"><circle cx="230" cy="110" r="4"/><circle cx="70" cy="150" r="4"/><circle cx="230" cy="190" r="3"/><circle cx="110" cy="110" r="3"/></g><g font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="100" y="206" text-anchor="end" fill="#0f172a">O</text><text x="230" y="206" text-anchor="middle" fill="#0f172a">3</text><text x="102" y="114" text-anchor="end" fill="#0f172a">2</text><text x="238" y="102" fill="#0f172a">M(3 + 2i)</text><text x="62" y="142" text-anchor="end" fill="#0f172a">N(−1 + i)</text><text x="168" y="176" fill="#0f6e56">|z|</text><text x="140" y="148" text-anchor="middle" fill="#b45309">MN</text><text x="152" y="204" text-anchor="middle" fill="#0f172a">u</text><text x="98" y="154" text-anchor="end" fill="#0f172a">v</text></g></svg>
:::

> **Propriétés** (p.9) — « Soit deux nombres complexes z et z′. |z| = 0, si et seulement si, z = 0 ; |z + z′| ≤ |z| + |z′| ; |kz| = |k||z|, k ∈ ℝ. |zz′| = |z||z′| ; |z̄| = |z| ; |z|² = zz̄ ; |zⁿ| = |z|ⁿ, n ∈ ℕ\*. |1/z| = 1/|z|, z ≠ 0 ; |z′/z| = |z′|/|z|, z ≠ 0 ; |1/zⁿ| = 1/|z|ⁿ, z ≠ 0 et n ∈ ℤ. »

_Exemple détaillé_ — pour z = 2 − i et z′ = −3 + 4i : |z| = √5 et |z′| = 5, donc |zz′| = 5√5, |z/z′| = √5/5, |z⁴| = (√5)⁴ = 25 et |(z̄z′)²| = (√5 × 5)² = 125. _Contrôle direct du premier_ : zz′ = −6 + 8i + 3i + 4 = −2 + 11i, de module √125 = 5√5 ✓. En revanche |z + z′| = |−1 + 3i| = √10 ≈ 3,16, **strictement inférieur** à |z| + |z′| ≈ 7,24 : l'inégalité triangulaire est bien une inégalité.

_Exemple détaillé (géométrie par les modules)_ — soit A(1 + i√3) et B(1 − i√3) : OA = √(1 + 3) = 2 = OB, donc OAB est **isocèle en O**. Pour que OADB soit un losange, les diagonales [OD] et [AB] doivent avoir le même milieu, d'où z_D = z_A + z_B = **2**. _Contrôle des quatre côtés_ : OA = 2, AD = |1 − i√3| = 2, DB = |−1 − i√3| = 2, BO = 2 ✓.

**Deux ensembles de points à reconnaître immédiatement.** Le premier traduit « distance à un point fixe » :

$$ |z − ω| = r  (r > 0)  ⟺  M appartient au cercle de centre Ω(ω) et de rayon r $$

::: figure Tous les points à distance 2 du point Ω forment un cercle : l'équation |z − 1 + 2i| = 2 se lit « ΩM = 2 ».
<svg viewBox="0 0 300 250"><path d="M20 90 H285" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M140 235 V15" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M285 90 l-8 -4 l0 8 z" fill="#0f172a"/><path d="M140 15 l-4 8 l8 0 z" fill="#0f172a"/><circle cx="170" cy="150" r="60" fill="#0f6e56" opacity="0.10"/><circle cx="170" cy="150" r="60" fill="none" stroke="#0f6e56" stroke-width="2.4"/><path d="M170 150 L230 150" fill="none" stroke="#b45309" stroke-width="2.2"/><g fill="#0f172a"><circle cx="170" cy="150" r="4"/></g><g font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="131" y="84" text-anchor="end" fill="#0f172a">O</text><text x="166" y="144" text-anchor="end" fill="#0f172a">Ω</text><text x="202" y="143" text-anchor="middle" fill="#b45309">2</text></g></svg>
:::

Le second traduit « équidistance de deux points fixes » :

$$ |z − a| = |z − b| ⟺ MA = MB ⟺ M appartient à la médiatrice de [AB] $$

::: figure Les points équidistants de A(1) et de B(−i) se placent tous sur une même droite : la médiatrice de [AB], qui coupe [AB] en son milieu et perpendiculairement.
<svg viewBox="0 0 300 250"><path d="M20 120 H285" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M150 235 V15" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M285 120 l-8 -4 l0 8 z" fill="#0f172a"/><path d="M150 15 l-4 8 l8 0 z" fill="#0f172a"/><path d="M60 30 L240 210" fill="none" stroke="#0f6e56" stroke-width="2.6"/><path d="M190 120 L150 160" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-dasharray="5 4"/><path d="M90 60 L190 120 M90 60 L150 160" fill="none" stroke="#b45309" stroke-width="1.8"/><g fill="#0f172a"><circle cx="190" cy="120" r="4"/><circle cx="150" cy="160" r="4"/><circle cx="90" cy="60" r="4"/><circle cx="170" cy="140" r="3"/></g><g font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="141" y="113" text-anchor="end" fill="#0f172a">O</text><text x="197" y="114" fill="#0f172a">A</text><text x="141" y="172" text-anchor="end" fill="#0f172a">B</text><text x="82" y="52" text-anchor="end" fill="#b45309">M</text><text x="180" y="152" fill="#94a3b8">I</text><text x="236" y="226" text-anchor="end" fill="#0f6e56">y = −x</text></g></svg>
:::

_Contrôle de la figure_ — A(1) et B(−i) ont pour coordonnées (1 ; 0) et (0 ; −1). Un point (x ; y) vérifie MA = MB ⟺ (x − 1)² + y² = x² + (y + 1)² ⟺ −2x = 2y ⟺ **y = −x**. Le milieu I(0,5 ; −0,5) est bien sur cette droite ✓, et pour M(−1,5 ; 1,5) on trouve MA = |−2,5 + 1,5i| = √8,5 et MB = |−1,5 + 2,5i| = √8,5 ✓.

**Colinéarité et orthogonalité.** Enfin, deux tests qui transforment une question de géométrie en un calcul :

> **Propriété** (p.8) — « Soit w⃗ et w₁⃗ deux vecteurs tels que w₁⃗ est non nul. Les vecteurs w⃗ et w₁⃗ sont colinéaires, si et seulement si, z_w⃗/z_w₁⃗ est réel. »

> **Propriété** (p.8) — « Soit w⃗ et w₁⃗ deux vecteurs tels que w₁⃗ est non nul. Les vecteurs w⃗ et w₁⃗ sont orthogonaux, si et seulement si, z_w⃗/z_w₁⃗ est imaginaire. »

_Exemple détaillé_ — soit A(2 − 2i). Alors M(z) ∈ (OA) ⟺ z/(2 − 2i) est réel ⟺ z = k(2 − 2i), k ∈ ℝ : la droite (OA) est exactement l'ensemble de ces affixes. _Contrôle_ : k = 1/2 donne 1 − i, de coordonnées (1 ; −1), aligné avec O et A(2 ; −2) ✓. De même, avec A(1 + 2i), la perpendiculaire à (OA) en O est l'ensemble des affixes ik(1 + 2i) : pour k = 1 on obtient −2 + i, et (1 ; 2)·(−2 ; 1) = −2 + 2 = 0 ✓.

> 🗡️ **Le réflexe « quotient »** : trois questions de géométrie se ramènent au même calcul. Le **module** d'un quotient donne un **rapport de longueurs**, sa **nature** (réel / imaginaire) donne **parallélisme / perpendicularité**, et son **argument** — la section suivante — donne l'**angle**.

## 🔮 Argument et écriture trigonométrique

Un point du plan ne se repère pas seulement par ses coordonnées : on peut aussi donner sa distance à O et la direction dans laquelle il se trouve. Pour z **non nul**, d'image M, on appelle **argument** de z toute mesure de l'angle orienté (u⃗, OM⃗), et on note arg(z) ≡ θ [2π] : un argument n'est défini qu'**à 2π près**, et **0 n'a pas d'argument**.

En projetant M sur les deux axes, on lit a = |z| cos θ et b = |z| sin θ, donc :

$$ cos θ = a/√(a² + b²)  et  sin θ = b/√(a² + b²) $$

::: figure Le couple (|z| ; θ) repère M aussi bien que (a ; b) : la partie réelle est |z| cos θ, la partie imaginaire |z| sin θ.
<svg viewBox="0 0 300 260"><path d="M25 180 H285" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M120 245 V20" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M285 180 l-8 -4 l0 8 z" fill="#0f172a"/><path d="M120 20 l-4 8 l8 0 z" fill="#0f172a"/><path d="M180 76 V180 M180 76 H120" fill="none" stroke="#94a3b8" stroke-width="1.3" stroke-dasharray="5 4"/><path d="M120 180 L180 76" fill="none" stroke="#0f6e56" stroke-width="2.6"/><path d="M155 180 A 35 35 0 0 0 137.5 149.7" fill="none" stroke="#b45309" stroke-width="2"/><g fill="#0f172a"><circle cx="180" cy="76" r="4"/><circle cx="180" cy="180" r="3"/><circle cx="120" cy="76" r="3"/></g><g font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="111" y="194" text-anchor="end" fill="#0f172a">O</text><text x="180" y="196" text-anchor="middle" fill="#0f172a">a</text><text x="112" y="80" text-anchor="end" fill="#0f172a">b</text><text x="190" y="68" fill="#0f172a">M(z)</text><text x="142" y="132" text-anchor="end" fill="#0f6e56">|z|</text><text x="152" y="168" fill="#b45309">θ</text></g></svg>
:::

> **Écriture trigonométrique** (encart p.11) — « Soit z un nombre complexe non nul tel que arg(z) ≡ θ [2π]. Alors z = |z|(cos θ + i sin θ). L'écriture précédente est appelée écriture trigonométrique de z. »

_Exemple détaillé_ — mettons z = −2√3 + 2i sous forme trigonométrique. **Module** : |z| = √(12 + 4) = √16 = **4**. **Argument** : cos θ = −2√3/4 = −√3/2 et sin θ = 2/4 = 1/2. _Contrôle par le quadrant_ : Re(z) < 0 et Im(z) > 0, donc M est dans le **deuxième quadrant**, et θ doit être entre π/2 et π — c'est θ = **5π/6** (et non −5π/6 ni π/6, qui donneraient les bons cosinus ou sinus mais le mauvais quadrant). D'où :

$$ z = 4(cos(5π/6) + i sin(5π/6)) $$

_Contrôle par retour à la forme algébrique_ : 4(−√3/2 + i × 1/2) = −2√3 + 2i ✓, on retombe sur le point de départ.

> **Propriétés** (p.11) — « Soit z un nombre complexe non nul et k un réel non nul. arg(z̄) ≡ −arg(z) [2π]. arg(−z) ≡ π + arg(z) [2π]. Si k > 0 alors arg(kz) ≡ arg(z) [2π]. Si k < 0 alors arg(kz) ≡ π + arg(z) [2π]. »

| nombre     | module    | argument | lecture géométrique                      |
| ---------- | --------- | -------- | ---------------------------------------- |
| z̄          | \|z\|     | −θ       | symétrique de M par rapport à (O, u⃗)     |
| −z         | \|z\|     | θ + π    | symétrique de M par rapport à O          |
| kz (k > 0) | k\|z\|    | θ        | M s'éloigne de O sur la même demi-droite |
| kz (k < 0) | \|k\|\|z\| | θ + π   | M passe de l'autre côté de O             |

_Contrôle sur l'exemple précédent_ : −z = 2√3 − 2i a pour cosinus √3/2 et pour sinus −1/2, donc un argument −π/6 ; or 5π/6 + π = 11π/6 ≡ −π/6 [2π] ✓.

> **Propriétés** (p.12) — « Soit deux nombres complexes non nuls z et z′. arg(zz′) ≡ arg(z) + arg(z′) [2π]. arg(1/z) ≡ −arg(z) [2π]. arg(z′/z) ≡ arg(z′) − arg(z) [2π]. arg(zⁿ) ≡ n arg(z) [2π], n ∈ ℤ. Pour tout nombre complexe non nul z et tout entier n, zⁿ = |z|ⁿ(cos nθ + i sin nθ). La formule précédente est appelée formule de Moivre. »

**Le multiplier, c'est additionner les angles.** Le module se multiplie, l'argument s'ajoute : voilà pourquoi la forme trigonométrique règne sur les puissances.

_Exemple détaillé (Moivre)_ — calculons (1 + i)⁶. On a |1 + i| = √2 et arg(1 + i) ≡ π/4 (car cos = sin = √2/2, premier quadrant). Moivre donne :

$$ (1 + i)⁶ = (√2)⁶(cos(6π/4) + i sin(6π/4)) = 8(cos(3π/2) + i sin(3π/2)) = 8(0 − i) = −8i $$

_Contrôle par un autre chemin_ : (1 + i)² = 2i, donc (1 + i)⁶ = (2i)³ = 8i³ = **−8i** ✓.

_Exemple_ — (√3 + i)⁵ : module 2, argument π/6, donc 32(cos(5π/6) + i sin(5π/6)) = **−16√3 + 16i**. _Contrôle_ : le module vaut 16 × 2 = 32 = 2⁵ ✓ et le point est dans le deuxième quadrant, comme l'annonce 5π/6 ✓.

> ⚠️ **Le cosinus seul ne suffit jamais.** cos θ = √2/2 admet deux solutions dans ]−π, π] : π/4 et −π/4. C'est le **signe de la partie imaginaire** (donc du sinus) qui tranche. Vérifie toujours ton argument en regardant dans quel quadrant se trouve le point.

## ⚡ L'écriture exponentielle re^(iθ)

Euler a remarqué que la fonction θ ↦ cos θ + i sin θ transforme les sommes en produits, exactement comme une exponentielle. On lui en donne donc la notation.

> **Notation** (p.17) — « Pour tout réel θ, on note e^(iθ) le nombre complexe cos θ + i sin θ. »

> **Conséquences** (p.17) — « e^(i0) = 1, e^(iπ/2) = i, e^(−iπ/2) = −i, e^(iπ) = −1. Pour tout réel θ et tout entier k, e^(iθ) = e^(i(θ+2kπ)). Pour tout réel θ, |e^(iθ)| = 1 et (e^(iθ))‾ = e^(−iθ) et −e^(iθ) = e^(i(θ+π)). »

> **Propriétés** (p.17) — « Soit deux réels θ et θ′. e^(iθ)·e^(iθ′) = e^(i(θ+θ′)) ; 1/e^(iθ) = e^(−iθ) ; e^(iθ)/e^(iθ′) = e^(i(θ−θ′)) ; (e^(iθ))ⁿ = e^(inθ), n ∈ ℤ. »

> **Théorème et définition** (p.18) — « Tout nombre complexe non nul z, s'écrit sous la forme z = re^(iθ), où r = |z| et arg(z) ≡ θ [2π]. L'écriture z = re^(iθ), r > 0 est appelée écriture exponentielle de z. »

_Exemple détaillé_ — soit z = √3 + i = 2e^(iπ/6) et z′ = −1 + i = √2 e^(i3π/4) (module √2 ; cos = −√2/2 et sin = √2/2, deuxième quadrant). On en déduit d'un trait :

$$ zz′ = 2√2 e^(i11π/12)  et  z/z′ = √2 e^(−i7π/12) $$

_Contrôles_ : π/6 = 2π/12 et 3π/4 = 9π/12, donc somme 11π/12 et différence −7π/12 ✓ ; module du quotient 2/√2 = √2 ✓.

_Exemple détaillé (le calcul que le bac adore)_ — calculons (1 + i)¹⁴/(√3 − i)⁸ sous forme algébrique. On passe **tout** en exponentielle : 1 + i = √2 e^(iπ/4) et √3 − i = 2e^(−iπ/6). Donc :

$$ (1 + i)¹⁴ = (√2)¹⁴ e^(i14π/4) = 128 e^(i7π/2) = 128 e^(i3π/2) $$

$$ (√3 − i)⁸ = 2⁸ e^(−i8π/6) = 256 e^(−i4π/3) = 256 e^(i2π/3) $$

Le quotient vaut donc (128/256) e^(i(3π/2 − 2π/3)) = (1/2) e^(i5π/6) = (1/2)(−√3/2 + i/2) = **−√3/4 + i/4**. _Contrôle_ : le module trouvé est √(3/16 + 1/16) = √(4/16) = 1/2 ✓, exactement 128/256.

**Deux factorisations à connaître par cœur.** En mettant en facteur « la moitié de l'angle », on transforme une somme en produit :

$$ 1 + e^(iθ) = e^(iθ/2)(e^(−iθ/2) + e^(iθ/2)) = 2 cos(θ/2) e^(iθ/2) $$

$$ 1 − e^(iθ) = e^(iθ/2)(e^(−iθ/2) − e^(iθ/2)) = −2i sin(θ/2) e^(iθ/2) $$

_Exemple détaillé_ — écrivons z = 1 + e^(i2π/5) sous forme exponentielle. Avec θ = 2π/5 : z = 2cos(π/5) e^(iπ/5). Comme cos(π/5) ≈ 0,809 est **positif**, le module est bien 2cos(π/5) ≈ 1,618 et un argument est π/5. _Contrôle numérique_ : e^(i2π/5) = cos 72° + i sin 72° ≈ 0,309 + 0,951i, donc z ≈ 1,309 + 0,951i, de module √(1,714 + 0,904) ≈ 1,618 ✓ et d'argument arctan(0,951/1,309) ≈ 36° = π/5 ✓.

> ⚠️ **2cos(θ/2) n'est un module que s'il est positif.** Si cos(θ/2) < 0, le facteur est négatif : il faut alors écrire 2cos(θ/2) = −|2cos(θ/2)| et ajouter π à l'argument. Même remarque pour sin(θ/2) dans la seconde factorisation.

> 🗡️ **Les sommes trigonométriques par l'exponentielle.** Pour calculer S = 1 + cos θ + … + cos nθ, forme S + iS′ = 1 + e^(iθ) + … + e^(inθ) : c'est une **suite géométrique** de raison e^(iθ), donc S + iS′ = (1 − e^(i(n+1)θ))/(1 − e^(iθ)). Les deux factorisations ci-dessus finissent le travail, et S est la partie réelle du résultat.

## 📐 Angles orientés : lire une figure dans un quotient

Voici le théorème qui rend les complexes irrésistibles en géométrie.

> **Théorème** (p.14) — « Le plan est muni d'un repère orthonormé direct (O, u⃗, v⃗). Soit A, B, C et D des points d'affixes respectives z_A, z_B, z_C et z_D et tels que AB ≠ 0 et CD ≠ 0. Alors (u⃗, AB⃗) ≡ arg(z_B − z_A) [2π] et (AB⃗, CD⃗) ≡ arg((z_D − z_C)/(z_B − z_A)) [2π]. »

> **Conséquence** (p.15) — « (z_D − z_C)/(z_B − z_A) = (CD/AB)(cos θ + i sin θ) avec (AB⃗, CD⃗) ≡ θ [2π]. »

Un seul quotient porte donc **deux** informations : son module est le rapport des longueurs, son argument est l'angle entre les deux vecteurs. D'où les trois tests d'usage courant, avec A, B, C deux à deux distincts :

| on veut montrer que… | on calcule Z = (z_C − z_A)/(z_B − z_A) et on vérifie… |
| -------------------- | ------------------------------------------------------ |
| A, B, C sont alignés | Z est **réel** (arg ≡ 0 [π]) |
| (AB) ⊥ (AC) | Z est **imaginaire** (arg ≡ π/2 [π]) |
| ABC est isocèle en A | \|Z\| = 1 |
| ABC est équilatéral | \|Z\| = 1 et arg(Z) ≡ ±π/3 [2π] |

_Exemple détaillé_ — soit A(4), B(1 + i√3), C(1 − i√3). Les trois côtés : AB = |−3 + i√3| = √(9 + 3) = 2√3 ; AC = |−3 − i√3| = 2√3 ; BC = |−2i√3| = 2√3. **ABC est équilatéral** ✓. _Contrôle par l'angle_ : Z = (−3 − i√3)/(−3 + i√3) ; en multipliant haut et bas par (−3 − i√3), le dénominateur vaut 12 et le numérateur (−3 − i√3)² = 9 + 6i√3 − 3 = 6 + 6i√3, d'où Z = (1 + i√3)/2, de module 1 et d'argument π/3 ✓.

_Exemple détaillé (nature d'un triangle)_ — soit B(3 + 3i) et C(1 − i) : z_B/z_C = (3 + 3i)(1 + i)/2 = (3 + 6i − 3)/2 = **3i**. Module 3, donc OB = 3 × OC ; argument π/2, donc (OC⃗, OB⃗) ≡ π/2 : le triangle OBC est **rectangle en O**, mais **pas isocèle** (OB = 3√2, OC = √2 ; rapport 3 ✓).

**Ensembles de points définis par un argument.** Deux configurations reviennent sans cesse :

- arg(z − z_A) ≡ θ [2π] décrit la **demi-droite** d'origine A dirigée par l'angle θ, **privée de A** (une droite entière correspondrait à [π]) ;
- arg((z − z_A)/(z − z_B)) ≡ θ [2π] décrit un **arc de cercle** passant par A et B, privé de A et B.

_Exemple détaillé (arc capable)_ — cherchons l'ensemble E des M(z) tels que arg((z − i)/(z − 1)) ≡ π/2 [2π], avec A(1) et B(i). D'après le théorème, cette quantité mesure (MA⃗, MB⃗) : **M voit [AB] sous un angle orienté droit**, donc E est contenu dans le **cercle de diamètre [AB]**, de centre Ω((1 + i)/2) et de rayon AB/2 = √2/2. L'angle étant imposé à 2π près, seul **l'un des deux arcs** convient. _Contrôle sur deux points_ : pour z = 0, (−i)/(−1) = i, d'argument π/2 ✓ — donc O ∈ E ; pour z = 1 + i, 1/i = −i, d'argument −π/2 ✗. Conclusion : **E est l'arc situé du côté de O, privé de A et B.**

::: figure Tout point M de l'arc coloré voit [AB] sous un angle orienté de +π/2 ; l'autre arc, lui, correspond à −π/2 et n'appartient pas à l'ensemble.
<svg viewBox="0 0 300 260"><path d="M25 180 H280" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M100 240 V25" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M280 180 l-8 -4 l0 8 z" fill="#0f172a"/><path d="M100 25 l-4 8 l8 0 z" fill="#0f172a"/><circle cx="135" cy="145" r="49.5" fill="none" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="5 4"/><path d="M170 180 A 49.5 49.5 0 0 0 100 110" fill="none" stroke="#0f6e56" stroke-width="3.2"/><path d="M135 194.5 L170 180 M135 194.5 L100 110" fill="none" stroke="#b45309" stroke-width="1.8"/><path d="M146.1 189.9 L141.5 178.8 L130.4 183.4" fill="none" stroke="#b45309" stroke-width="1.6"/><g fill="#0f172a"><circle cx="170" cy="180" r="4"/><circle cx="100" cy="110" r="4"/><circle cx="100" cy="180" r="3.5"/><circle cx="135" cy="194.5" r="4"/></g><g font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="176" y="197" fill="#0f172a">A(1)</text><text x="92" y="104" text-anchor="end" fill="#0f172a">B(i)</text><text x="92" y="196" text-anchor="end" fill="#0f172a">O</text><text x="137" y="214" text-anchor="middle" fill="#b45309">M</text></g></svg>
:::

> ⚠️ **[2π] ou [π], ce n'est pas la même figure.** Avec [π], la condition « (MA⃗, MB⃗) ≡ π/2 » donne le **cercle entier** de diamètre [AB] privé de A et B ; avec [2π], elle n'en garde qu'**un arc**. Teste toujours un point pour savoir lequel.

## 🗝️ L'équation zⁿ = a : les racines nièmes

Dans ℝ, x³ = 1 n'a qu'une solution. Dans ℂ, elle en a trois — et l'écriture exponentielle les donne toutes.

> **Théorème et définition** (p.19) — « Pour tout entier naturel non nul n, l'équation zⁿ = 1 admet dans ℂ n solutions distinctes définies par zₖ = e^(i·2kπ/n), l'entier k appartenant à {0, 1, …, (n − 1)}. Les solutions de l'équation zⁿ = 1 sont appelées racines nièmes de l'unité. »

> **Conséquence** (p.20) — « Le plan est muni d'un repère orthonormé direct (O, u⃗, v⃗). Lorsque n ≥ 3, les points images des racines nièmes de l'unité sont les sommets d'un polygone régulier inscrit dans le cercle trigonométrique. »

_Exemple détaillé (n = 3)_ — les racines cubiques de l'unité sont 1, j = e^(i2π/3) = −1/2 + i√3/2 et j² = e^(i4π/3) = −1/2 − i√3/2 = j̄. _Contrôles_ : j³ = e^(i2π) = 1 ✓ ; et 1 + j + j² = 1 + (−1/2 − 1/2) + i(√3/2 − √3/2) = **0** ✓ — cette somme nulle est l'identité la plus utile du chapitre. Plus généralement, la somme des n racines nièmes de l'unité est nulle dès que n ≥ 2.

> **Théorème et définition** (p.21) — « Soit a un nombre complexe non nul d'argument θ et n un entier naturel non nul. L'équation zⁿ = a admet dans ℂ, n solutions distinctes définies par zₖ = r·e^(i(θ/n + 2kπ/n)), k ∈ {0, 1, …, n − 1}, où r est le réel strictement positif tel que rⁿ = |a|. »

> **Conséquence** (p.22) — « Le plan complexe est muni d'un repère orthonormé direct (O, u⃗, v⃗). Lorsque n ≥ 3, les points images des racines nièmes d'un nombre complexe non nul sont les sommets d'un polygone régulier inscrit dans le cercle de centre O et de rayon r tel que rⁿ = |a|. »

**La méthode, en trois gestes** : mettre a sous forme exponentielle |a|e^(iθ) ; prendre la racine nième **réelle positive** du module ; partager l'argument par n et ajouter les n multiples de 2π/n.

_Exemple détaillé_ — résolvons z³ = 8i. Ici a = 8i = 8e^(iπ/2), donc r³ = 8 ⇒ r = 2, et les solutions sont zₖ = 2e^(i(π/6 + 2kπ/3)) pour k ∈ {0 ; 1 ; 2} :

$$ z₀ = 2e^(iπ/6) = √3 + i,  z₁ = 2e^(i5π/6) = −√3 + i,  z₂ = 2e^(i3π/2) = −2i $$

_Contrôle par réinjection_ : (√3 + i)² = 3 + 2i√3 − 1 = 2 + 2i√3, puis (2 + 2i√3)(√3 + i) = 2√3 + 2i + 6i − 2√3 = **8i** ✓. Et (−2i)³ = −8i³ = **8i** ✓.

::: figure Les trois racines cubiques de 8i se posent sur un même cercle de rayon 2, espacées de 2π/3 : elles sont les sommets d'un triangle équilatéral.
<svg viewBox="0 0 300 260"><path d="M25 130 H285" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M150 245 V20" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M285 130 l-8 -4 l0 8 z" fill="#0f172a"/><path d="M150 20 l-4 8 l8 0 z" fill="#0f172a"/><circle cx="150" cy="130" r="90" fill="none" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="5 4"/><path d="M227.9 85 L72.1 85 L150 220 Z" fill="#0f6e56" opacity="0.10"/><path d="M227.9 85 L72.1 85 L150 220 Z" fill="none" stroke="#0f6e56" stroke-width="2.2" stroke-linejoin="round"/><path d="M150 130 L227.9 85" fill="none" stroke="#b45309" stroke-width="2"/><g fill="#0f172a"><circle cx="227.9" cy="85" r="4"/><circle cx="72.1" cy="85" r="4"/><circle cx="150" cy="220" r="4"/></g><g font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="238" y="80" fill="#0f172a">z₀</text><text x="62" y="80" text-anchor="end" fill="#0f172a">z₁</text><text x="150" y="240" text-anchor="middle" fill="#0f172a">z₂</text><text x="141" y="146" text-anchor="end" fill="#0f172a">O</text><text x="198" y="112" text-anchor="middle" fill="#b45309">2</text></g></svg>
:::

**Les racines carrées par la méthode algébrique.** Quand l'argument de a n'est pas remarquable, on cherche z = x + iy directement. L'égalité z² = u, avec le module en renfort, donne un système de trois équations :

$$ x² − y² = Re(u),  2xy = Im(u),  x² + y² = |u| $$

_Exemple détaillé_ — racines carrées de u = 3 − 4i. Ici |u| = √(9 + 16) = 5, donc x² − y² = 3, 2xy = −4 et x² + y² = 5. En additionnant puis soustrayant les deux équations extrêmes : 2x² = 8 ⇒ x² = 4, et 2y² = 2 ⇒ y² = 1. Comme 2xy = −4 < 0, x et y sont de **signes contraires** : les couples sont (2 ; −1) et (−2 ; 1). Les racines carrées de u sont donc **2 − i** et **−2 + i**. _Contrôle par réinjection_ : (2 − i)² = 4 − 4i + i² = 3 − 4i ✓.

> ⚠️ **N'écris jamais « √z » pour un complexe.** Un complexe non nul a **deux** racines carrées opposées, et aucune n'est « la » bonne : la notation √ est réservée aux réels positifs. On dit « une racine carrée de Δ », jamais « la racine de Δ ». De même, n'oublie jamais qu'il y a exactement **n** racines nièmes : si tu n'en trouves que deux pour n = 3, tu as perdu une valeur de k.

## 🛡️ Équations du second degré, et au-delà

Dans ℂ, le discriminant n'a plus de signe — mais il a toujours des racines carrées, et cela suffit.

> **Théorème** (p.24) — « Soit a, b et c des nombres complexes tels que a ≠ 0. L'équation az² + bz + c = 0, admet dans ℂ, deux solutions (éventuellement confondues) définies par z₁ = (−b + δ)/2a et z₂ = (−b − δ)/2a, où δ est une racine carrée du discriminant Δ = b² − 4ac. »

> **Conséquences** (p.24) — « Si z₁ et z₂ sont les solutions de az² + bz + c = 0, a ≠ 0, alors az² + bz + c = a(z − z₁)(z − z₂), z₁ + z₂ = −b/a et z₁z₂ = c/a. »

**Méthode** : calculer Δ = b² − 4ac ; en chercher **une** racine carrée δ (à vue si Δ est réel, par la méthode algébrique sinon) ; conclure par (−b ± δ)/2a ; vérifier avec la somme et le produit.

_Exemple détaillé (coefficients réels)_ — résolvons z² − 2z + 2 = 0. Δ = 4 − 8 = −4, dont les racines carrées sont ±2i ; on prend δ = 2i. Alors z₁ = (2 + 2i)/2 = **1 + i** et z₂ = (2 − 2i)/2 = **1 − i**. _Contrôle par réinjection_ : (1 + i)² − 2(1 + i) + 2 = 2i − 2 − 2i + 2 = 0 ✓. _Contrôle par somme-produit_ : (1 + i) + (1 − i) = 2 = −b/a ✓ et (1 + i)(1 − i) = 1 + 1 = 2 = c/a ✓.

Les deux racines sont **conjuguées** : c'est toujours le cas quand a, b, c sont réels — mais **uniquement** dans ce cas.

_Exemple détaillé (coefficients complexes)_ — résolvons z² − (5 − i)z + 8 − i = 0. Le discriminant vaut :

$$ Δ = (5 − i)² − 4(8 − i) = 25 − 10i − 1 − 32 + 4i = −8 − 6i $$

On cherche δ = x + iy par la méthode algébrique : x² − y² = −8, 2xy = −6, x² + y² = |−8 − 6i| = 10. D'où x² = 1 et y² = 9, avec xy < 0 : δ = **1 − 3i** (on vérifie (1 − 3i)² = 1 − 6i − 9 = −8 − 6i ✓). Alors :

$$ z₁ = ((5 − i) + (1 − 3i))/2 = (6 − 4i)/2 = 3 − 2i  et  z₂ = ((5 − i) − (1 − 3i))/2 = (4 + 2i)/2 = 2 + i $$

_Contrôle par somme-produit_ : z₁ + z₂ = 5 − i ✓ ; z₁z₂ = (3 − 2i)(2 + i) = 6 + 3i − 4i + 2 = 8 − i ✓. _Contrôle par réinjection de z₁_ : (3 − 2i)² = 5 − 12i ; (5 − i)(3 − 2i) = 15 − 10i − 3i − 2 = 13 − 13i ; donc 5 − 12i − 13 + 13i + 8 − i = 0 ✓. Remarque : ici z₂ ≠ z̄₁ — les coefficients ne sont pas tous réels.

**Degré 3 et plus.** On ne sait pas résoudre en général : on **devine** une racine (souvent réelle ou imaginaire pure, et l'énoncé y invite), puis on factorise.

> **Théorème** (p.25) — « Soit a₁, a₂, …, aₙ des nombres complexes tels que aₙ ≠ 0, n ≥ 2. Soit P(z) = aₙzⁿ + a_(n−1)z^(n−1) + … + a₁z + a₀. Si z₀ est un zéro de P, alors P(z) = (z − z₀)g(z), où g(z) est de la forme aₙz^(n−1) + b_(n−2)z^(n−2) + … + b₀, avec b₀, b₁, …, b_(n−2) complexes. »

_Exemple détaillé_ — résolvons (E) : z³ + (1 − 4i)z² − (7 + 3i)z + 6i − 2 = 0. Cherchons une racine **imaginaire pure** z₀ = 2i : (2i)³ = −8i ; (1 − 4i)(2i)² = (1 − 4i)(−4) = −4 + 16i ; −(7 + 3i)(2i) = −14i + 6 ; reste 6i − 2. Somme des parties réelles : −4 + 6 − 2 = 0 ; somme des parties imaginaires : −8 + 16 − 14 + 6 = 0. Donc z₀ = 2i est bien racine ✓. La factorisation s'écrit alors :

$$ z³ + (1 − 4i)z² − (7 + 3i)z + 6i − 2 = (z − 2i)(z² + (1 − 2i)z − 3 − i) $$

Il reste un second degré : Δ = (1 − 2i)² + 4(3 + i) = 1 − 4i − 4 + 12 + 4i = **9**, donc δ = 3 et z = (−(1 − 2i) ± 3)/2, soit z₁ = (2 + 2i)/2 = **1 + i** et z₂ = (−4 + 2i)/2 = **−2 + i**. L'ensemble des solutions est S = {2i ; 1 + i ; −2 + i}. _Contrôle par réinjection de −2 + i dans le facteur du second degré_ : (−2 + i)² = 3 − 4i et (1 − 2i)(−2 + i) = −2 + i + 4i + 2 = 5i, donc 3 − 4i + 5i − 3 − i = 0 ✓.

> ⚠️ **« Δ < 0 » ne veut rien dire dans ℂ.** Le discriminant est un nombre complexe : on ne compare pas, on **extrait une racine carrée**. Et l'équation a toujours deux solutions, confondues seulement si Δ = 0. Autre piège : ne conclus jamais « les racines sont conjuguées » sans avoir vérifié que **tous** les coefficients sont réels.

## 🧪 Nombres complexes et trigonométrie

En lisant la notation e^(iθ) à l'envers, on récupère cos et sin — et on transforme la trigonométrie en algèbre.

> **Théorème** (p.26) — « Pour tout réel x et pour tout entier n, (cos x + i sin x)ⁿ = cos(nx) + i sin(nx) (Formule de Moivre). Pour tout réel x, cos x = (e^(ix) + e^(−ix))/2 et sin x = (e^(ix) − e^(−ix))/2i (Formules d'Euler). »

**Sens 1 — Moivre développe les angles multiples.** On écrit cos nx + i sin nx = (cos x + i sin x)ⁿ, on développe par le binôme de Newton, puis on identifie parties réelles et imaginaires.

_Exemple détaillé_ — pour n = 3, le binôme donne (cos x + i sin x)³ = (cos³x − 3 cos x sin²x) + i(3 cos²x sin x − sin³x), puisque i² = −1 et i³ = −i. Par identification :

$$ cos 3x = cos³x − 3 cos x sin²x  et  sin 3x = 3 cos²x sin x − sin³x $$

_Contrôle numérique en x = π/6_ : cos 3x = cos(π/2) = 0, et (√3/2)³ − 3(√3/2)(1/2)² = 3√3/8 − 3√3/8 = 0 ✓ ; sin 3x = 1, et 3(3/4)(1/2) − (1/2)³ = 9/8 − 1/8 = 1 ✓.

**Sens 2 — Euler linéarise les puissances.** _Linéariser_ cosⁿx ou sinⁿx, c'est l'écrire comme une **somme** de cos kx et sin kx — la forme qui se primitive et s'intègre (chapitres 5 et 6).

_Exemple détaillé_ — linéarisons cos³x. On part de cos x = (e^(ix) + e^(−ix))/2 :

$$ cos³x = (1/8)(e^(ix) + e^(−ix))³ = (1/8)(e^(3ix) + 3e^(ix) + 3e^(−ix) + e^(−3ix)) $$

En regroupant les termes conjugués deux à deux : e^(3ix) + e^(−3ix) = 2cos 3x et e^(ix) + e^(−ix) = 2cos x, d'où :

$$ cos³x = (1/8)(2 cos 3x + 6 cos x) = (1/4)cos 3x + (3/4)cos x $$

_Contrôle en x = 0_ : 1 = 1/4 + 3/4 ✓. _Contrôle en x = π/3_ : cos³(π/3) = (1/2)³ = 1/8, et (1/4)cos π + (3/4)(1/2) = −1/4 + 3/8 = 1/8 ✓.

Le même calcul avec sin x = (e^(ix) − e^(−ix))/2i donne, pour la puissance cinquième, sin⁵x = (1/16)(sin 5x − 5 sin 3x + 10 sin x). _Contrôle en x = π/2_ : sin⁵ = 1, et (1/16)(1 + 5 + 10) = 1 ✓.

> 🗡️ **Comment savoir dans quel sens aller ?** Si tu veux **développer** cos nx en puissances de cos x et sin x → Moivre. Si tu veux **abaisser** les puissances pour intégrer → Euler. Une intégrale du type ∫ cos³x dx se calcule toujours après linéarisation.

> ⚠️ Dans la formule d'Euler du sinus, le dénominateur est **2i**, pas 2. Oublier le i change le résultat de facteur imaginaire — c'est l'erreur de linéarisation la plus fréquente. Vérifie ta linéarisation en testant une valeur particulière : c'est immédiat et imparable.

> 🏆 Dixième porte franchie, héros : tu es entré dans le tome 2 par la grande salle. Tu sais lire un complexe de trois façons — algébrique, trigonométrique, exponentielle — et passer de l'une à l'autre à volonté ; tu transformes une longueur en module, un angle en argument, un lieu géométrique en équation. Garde ces armes bien en main : au chapitre suivant, les **isométries du plan** vont demander exactement ce langage, et les similitudes t'attendent juste derrière.
