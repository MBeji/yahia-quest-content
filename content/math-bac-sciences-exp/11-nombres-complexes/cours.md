# ⚔️ Nombres complexes — l'algèbre qui dessine le plan

> 💡 «Un nombre dont le carré vaut −1 n'existe pas sur la droite réelle. Il existe dans le plan — et il y range les distances, les angles et les directions.»

En 1740, Euler écrit cos x = ½(e^(x√−1) + e^(−x√−1)) ; en 1748, il pose e^(x√−1) = cos x + √−1 sin x. De cette dernière formule, Dantzig dit qu'elle contient « les symboles les plus importants » : l'arithmétique par 0 et 1, l'algèbre par −1, la géométrie par π et l'analyse par e. Ce chapitre ouvre le **tome 2** : huit notions te mènent de la définition de ℂ jusqu'à la linéarisation de sin⁵x. Chaque notion garde la même route : on part d'une situation, on nomme, on regarde, on calcule, on se méfie du piège, puis on vérifie seul.

## 🏰 L'ensemble ℂ : forme algébrique et conjugué

Un ingénieur écrit l'équation x² + 1 = 0 et constate qu'elle n'a aucune solution réelle : un carré réel est toujours positif.
Faut-il renoncer à la résoudre, ou agrandir l'ensemble des nombres jusqu'à ce qu'elle ait une solution ?

::: definition
**Théorème et définition** (p.6) — « Il existe un ensemble appelé ensemble des nombres complexes, noté ℂ et vérifiant les propriétés ci-dessous. 1. L'ensemble ℂ contient l'ensemble ℝ des nombres réels. 2. Il existe un élément de ℂ, noté i, tel que i² = −1. 3. L'ensemble ℂ est muni d'une addition et d'une multiplication qui vérifient les mêmes propriétés que l'addition et la multiplication dans ℝ. 4. Tout élément z de ℂ s'écrit de façon unique sous la forme z = a + ib, où a et b sont des réels. »
:::

L'écriture z = a + ib est la **forme algébrique** de z : a est sa partie réelle Re(z), b sa partie imaginaire Im(z) — un **réel**, jamais « ib ». Le mot « unique » est le moteur du chapitre : deux complexes sont égaux si et seulement si leurs parties réelles sont égales **et** leurs parties imaginaires aussi ; z est réel si b = 0, imaginaire si a = 0. Le **conjugué** de z = a + ib est le nombre z̄ = a − ib.

::: exemple Calculer, puis résoudre grâce à l'unicité

1. Développer (2 − 2i)(1 + i)². **Premier geste** : (1 + i)² = 1 + 2i + i² = 2i, puisque i² = −1. Donc (2 − 2i) × 2i = 4i − 4i² = 4 + 4i. Contrôle par un autre chemin : (2 − 2i)(1 + i) = 2 + 2i − 2i + 2 = 4, puis 4(1 + i) = 4 + 4i ✓.
2. Diviser : (1 + i√3)/(√3 − i). On multiplie haut et bas par le conjugué du dénominateur, √3 + i, pour que le dénominateur devienne réel : (1 + i√3)(√3 + i)/((√3)² + 1²) = (√3 + i + 3i + i²√3)/4 = 4i/4 = i. Contrôle par réinjection : i × (√3 − i) = i√3 + 1 ✓.
3. Résoudre 2z + z̄ = 9 − 3i. On pose z = x + iy avec x et y réels : 2z + z̄ = 3x + iy. Par unicité de la forme algébrique, 3x = 9 et y = −3, donc z = 3 − 3i. Contrôle : 2(3 − 3i) + (3 + 3i) = 9 − 3i ✓.
4. Conjugué d'une puissance. Pour z = −1 + 2i : z² = 1 − 4i + 4i² = −3 − 4i, de conjugué −3 + 4i. Et (z̄)² = (−1 − 2i)² = 1 + 4i − 4 = −3 + 4i : même résultat ✓.

:::

::: propriete
**Propriétés du conjugué** (p.7) — « • Pour tous nombres complexes z et z′, (z + z′)‾ = z̄ + z̄′ ; (zz′)‾ = z̄ z̄′ ; (zⁿ)‾ = (z̄)ⁿ ; n ∈ ℕ*. • Pour tout nombre complexe z et tout nombre complexe non nul z′, (z/z′)‾ = z̄/z̄′ ; (1/z′ⁿ)‾ = 1/(z̄′)ⁿ, n ∈ ℤ. • z + z̄ = 2 Re(z) ; z − z̄ = 2i Im(z) ; zz̄ = (Re(z))² + (Im(z))². • z = z̄, si et seulement si, z est réel. • z = −z̄, si et seulement si, z est imaginaire. »
:::

Les deux dernières lignes sont des **tests** : pour montrer qu'un nombre est réel, on montre qu'il est égal à son conjugué ; pour montrer qu'il est imaginaire, on montre qu'il est l'opposé de son conjugué.

::: piege
**Erreur : confondre conjugué et opposé.** Pour z = 5 − 2i, on est tenté d'écrire z̄ = −5 + 2i. Or c'est −z, l'opposé, qui change les deux signes. Le conjugué ne change que le signe de la partie imaginaire : z̄ = 5 + 2i. Piège voisin : i² = −1 mais i⁴ = 1, car les puissances de i tournent de 4 en 4 (i, −1, −i, 1). Et ℂ n'est pas ordonné : écrire « z > 0 » pour un complexe non réel n'a aucun sens.
:::

::: verifie À toi : l'unicité en action
Résoudre z + 3z̄ = 8 − 4i, d'inconnue z ∈ ℂ.

---

On pose z = x + iy : z + 3z̄ = 4x − 2iy. Par unicité, 4x = 8 et −2y = −4, donc x = 2 et y = 2, soit z = 2 + 2i. Contrôle : (2 + 2i) + 3(2 − 2i) = 8 − 4i ✓.
:::

::: retenir
Tout complexe s'écrit de façon unique a + ib ; le conjugué ne change que le signe de b, et « z = z̄ » (réel) ou « z = −z̄ » (imaginaire) sont les deux tests à retenir.
:::

## 🧭 Affixe, colinéarité et orthogonalité

Un drone se repère par deux coordonnées.
Comment les ranger dans un seul nombre, pour que le déplacement d'un point à un autre devienne une simple soustraction, et que « parallèle » ou « perpendiculaire » se lise dans un quotient ?

::: definition
**Affixe** (p.7) — « Le plan est muni d'un repère orthonormé direct (O, u⃗, v⃗). • L'affixe d'un point M(a, b) du plan est le nombre complexe z = a + ib noté Aff(M) ou z_M. On dit aussi que le point M(a, b) est l'image de z. • Soit w⃗ un vecteur et M et N deux points tels que w⃗ = MN⃗. Alors l'affixe du vecteur w⃗ est le nombre complexe noté Aff(w⃗) ou z_w⃗, vérifiant z_w⃗ = z_N − z_M. • Pour tous vecteurs w⃗ et w₁⃗ et tous réels α et β, Aff(αw⃗ + βw₁⃗) = αAff(w⃗) + βAff(w₁⃗). »
:::

On note M(z) le point d'affixe z. Les symétries se lisent directement sur l'affixe z = a + ib de M :

| symétrique de M par rapport à… | affixe | pourquoi |
| --- | --- | --- |
| l'axe des abscisses | z̄ = a − ib | (a ; b) → (a ; −b) |
| l'axe des ordonnées | −z̄ = −a + ib | (a ; b) → (−a ; b) |
| le point O | −z = −a − ib | (a ; b) → (−a ; −b) |

::: exemple Affixes de vecteurs, centre de gravité, alignement

1. Soit A(i), B(1 − 3i) et C(1 + 2i). Le vecteur OB⃗ − 2OC⃗ a pour affixe (1 − 3i) − 2(1 + 2i) = −1 − 7i ; il suffit d'appliquer la linéarité.
2. Le vecteur AB⃗ a pour affixe z_B − z_A = 1 − 4i et AC⃗ pour affixe 1 + i. Donc −AB⃗ + (3/2)AC⃗ a pour affixe −1 + 4i + 3/2 + (3/2)i = 1/2 + (11/2)i.
3. Le centre de gravité G du triangle ABC a pour affixe la moyenne des trois affixes : (i + 1 − 3i + 1 + 2i)/3 = 2/3. Contrôle sur les coordonnées : les abscisses 0, 1 et 1 ont pour moyenne 2/3 et les ordonnées 1, −3 et 2 ont pour moyenne 0 ✓.
4. Soit A(2 − 2i) et B(−1 + i). Aff(OA⃗) = 2 − 2i = −2(−1 + i) = −2 Aff(OB⃗) : les vecteurs OA⃗ et OB⃗ sont colinéaires, donc O, A et B sont alignés.

:::

Le point 4 se généralise : c'est la propriété suivante, et sa jumelle sur l'orthogonalité.

::: propriete
**Colinéarité** (p.8) — « Soit w⃗ et w₁⃗ deux vecteurs tels que w₁⃗ ≠ 0⃗. Les vecteurs w⃗ et w₁⃗ sont colinéaires, si et seulement si, z_w⃗/z_w₁⃗ est réel. » **Orthogonalité** (p.8) — « Soit w⃗ et w₁⃗ deux vecteurs tels que w₁⃗ ≠ 0⃗. w⃗ et w₁⃗ sont orthogonaux, si et seulement si, z_w⃗/z_w₁⃗ est imaginaire. »
**Démonstration.** Colinéaires ⟺ w⃗ = kw₁⃗ avec k réel ⟺ z_w⃗ = k z_w₁⃗ ⟺ z_w⃗/z_w₁⃗ = k, réel. Pour l'orthogonalité, posons z_w⃗ = a + ib et z_w₁⃗ = a′ + ib′ : le quotient vaut ((aa′ + bb′) + i(a′b − ab′))/(a′² + b′²). Il est imaginaire si et seulement si aa′ + bb′ = 0, c'est-à-dire si et seulement si le produit scalaire de (a ; b) et (a′ ; b′) est nul. ∎
:::

Contrôle sur l'orthogonalité : avec A(1 + 2i) et B = i(1 + 2i) = −2 + i, le quotient z_B/z_A = i est imaginaire, et en effet (1 ; 2) · (−2 ; 1) = −2 + 2 = 0 ✓.

::: piege
**Erreur : inverser les deux critères.** On retient « quotient réel » et « quotient imaginaire » mais on attribue le premier à la perpendicularité. Test express : prends w⃗ = w₁⃗ (même vecteur) ; le quotient vaut 1, réel, et les vecteurs sont bien parallèles. Un quotient **réel** donne donc le **parallélisme**, un quotient **imaginaire** la **perpendicularité**.
:::

::: verifie À toi : colinéaires ?
Les vecteurs d'affixes 3 − 6i et −1 + 2i sont-ils colinéaires ?

---

Le quotient (3 − 6i)/(−1 + 2i) = −3(−1 + 2i)/(−1 + 2i) = −3 est réel : oui, ils sont colinéaires (de sens contraires, le premier étant −3 fois le second).
:::

::: retenir
L'affixe de MN⃗ est z_N − z_M ; un quotient d'affixes de vecteurs **réel** signifie colinéaires, **imaginaire** signifie orthogonaux.
:::

## 📏 Module, distances et lieux de points

Deux balises sont posées en M(3 + 2i) et N(−1 + i).
Peut-on obtenir la distance MN sans sortir la règle, à partir des seuls nombres complexes ?

::: definition
**Module** (p.9) — « Soit z = a + ib et M(a, b) le point d'affixe z. On appelle module de z le réel positif, noté |z|, défini par |z| = OM = √(a² + b²). Pour tous points M et N d'affixes z_M et z_N, |z_N − z_M| = MN. »
:::

::: figure Le module |z| est la longueur OM, et |z_N − z_M| la longueur MN : lire un module, c'est lire une distance sur la figure.
<svg viewBox="-30 0 370 260"><path d="M20 190 H330" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M110 245 V20" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M330 190 l-8 -4 l0 8 z" fill="#0f172a"/><path d="M110 20 l-4 8 l8 0 z" fill="#0f172a"/><path d="M230 110 V190 M230 110 H110" fill="none" stroke="#94a3b8" stroke-width="1.3" stroke-dasharray="5 4"/><path d="M110 190 L230 110" fill="none" stroke="#0f6e56" stroke-width="2.6"/><path d="M230 110 L70 150" fill="none" stroke="#b45309" stroke-width="2.2"/><path d="M110 190 L150 190 M110 190 L110 150" fill="none" stroke="#0f172a" stroke-width="3.4"/><g fill="#0f172a"><circle cx="230" cy="110" r="4"/><circle cx="70" cy="150" r="4"/><circle cx="230" cy="190" r="3"/><circle cx="110" cy="110" r="3"/></g><g font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="100" y="206" text-anchor="end" fill="#0f172a">O</text><text x="230" y="206" text-anchor="middle" fill="#0f172a">3</text><text x="102" y="114" text-anchor="end" fill="#0f172a">2</text><text x="238" y="102" fill="#0f172a">M(3 + 2i)</text><text x="62" y="142" text-anchor="end" fill="#0f172a">N(−1 + i)</text><text x="168" y="176" fill="#0f6e56">|z|</text><text x="140" y="148" text-anchor="middle" fill="#b45309">MN</text><text x="152" y="204" text-anchor="middle" fill="#0f172a">u</text><text x="98" y="154" text-anchor="end" fill="#0f172a">v</text></g></svg>
:::

::: propriete
**Propriétés du module** (p.10) — « Soit deux nombres complexes z et z′. |z| = 0, si et seulement si, z = 0 ; |z + z′| ≤ |z| + |z′| ; |kz| = |k||z|, k ∈ ℝ. |zz′| = |z||z′| ; |z̄| = |z| ; |z|² = zz̄ ; |zⁿ| = |z|ⁿ, n ∈ ℕ*. |1/z| = 1/|z|, z ≠ 0 ; |z′/z| = |z′|/|z|, z ≠ 0 ; |1/zⁿ| = 1/|z|ⁿ, z ≠ 0 et n ∈ ℤ. »
:::

::: exemple Modules, nature d'un triangle

1. Pour M(3 + 2i) et N(−1 + i) : MN = |−4 − i| = √(16 + 1) = √17. C'est la figure ci-dessus, lue en un calcul.
2. Soit A(1 + i√3) et B(1 − i√3). OA = √(1 + 3) = 2, OB = 2 et AB = |−2i√3| = 2√3 : OAB est **isocèle en O**, mais pas équilatéral, puisque AB ≠ 2.
3. Modules de puissances et de quotients : |1 + i| = √2, donc |(1 + i)⁵| = (√2)⁵ = 4√2, et |(1 + i)¹¹/(1 − i)⁶| = (√2)¹¹/(√2)⁶ = (√2)⁵ = 4√2. Contrôle direct : (1 + i)² = 2i, donc (1 + i)⁴ = −4 et (1 + i)⁵ = −4 − 4i, de module 4√2 ✓.
4. Soit A(2 + i), B(−1) et C(3 − 2i). AB² = |3 + i|² = 10, AC² = |−1 + 3i|² = 10 et BC² = |4 − 2i|² = 20. Comme AB = AC et AB² + AC² = BC², le triangle ABC est isocèle **et** rectangle en A (réciproque de Pythagore).

:::

**Trois lieux à reconnaître.** Chacun se traduit en une distance.

::: exemple Cercles et médiatrices

1. |z − 1 + 2i| = 2 s'écrit |z − (1 − 2i)| = 2, c'est-à-dire ΩM = 2 avec Ω(1 − 2i) : le **cercle** de centre Ω et de rayon 2.
2. |z + 2 − i| = |z̄ − 2 + 2i|. Un complexe et son conjugué ont même module : |z̄ − 2 + 2i| = |z − 2 − 2i|. Avec K(−2 + i) et L(2 + 2i), l'égalité devient KM = LM : M décrit la **médiatrice** de [KL].
3. Le quotient (z − i)/(z − 1) est imaginaire (z ≠ 1). Avec A(i) et B(1), c'est le quotient des affixes de AM⃗ et BM⃗ : AM⃗ et BM⃗ sont orthogonaux, ou M = A. L'ensemble est le **cercle de diamètre [AB] privé de B**, de centre Ω((1 + i)/2) et de rayon √2/2. Contrôle : O vérifie (−i)/(−1) = i, imaginaire, et OΩ = √2/2 ✓.

:::

::: figure Le cercle de diamètre [AB] : tout point M du cercle, distinct de A et de B, voit [AB] sous un angle droit, donc AM⃗ et BM⃗ sont orthogonaux ; B, où le quotient n'existe pas, est exclu.
<svg viewBox="0 0 300 250"><path d="M20 190 H285" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M100 245 V15" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M285 190 l-8 -4 l0 8 z" fill="#0f172a"/><path d="M100 15 l-4 8 l8 0 z" fill="#0f172a"/><circle cx="140" cy="150" r="56.6" fill="#0f6e56" opacity="0.08"/><circle cx="140" cy="150" r="56.6" fill="none" stroke="#0f6e56" stroke-width="2.6"/><path d="M100 110 L180 190" fill="none" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="5 4"/><path d="M168.3 101 L100 110 M168.3 101 L180 190" fill="none" stroke="#b45309" stroke-width="1.8"/><path d="M157.4 102.4 L158.8 113.4 L169.7 111.9" fill="none" stroke="#b45309" stroke-width="1.6"/><circle cx="100" cy="110" r="4" fill="#0f172a"/><circle cx="168.3" cy="101" r="4" fill="#0f172a"/><circle cx="140" cy="150" r="3" fill="#94a3b8"/><circle cx="100" cy="190" r="3" fill="#0f172a"/><circle cx="180" cy="190" r="4" fill="#ffffff" stroke="#0f172a" stroke-width="2"/><g font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="92" y="206" text-anchor="end" fill="#0f172a">O</text><text x="92" y="114" text-anchor="end" fill="#0f172a">A(i)</text><text x="188" y="206" text-anchor="start" fill="#0f172a">B(1)</text><text x="176.3" y="95" text-anchor="start" fill="#b45309">M</text><text x="150" y="148" text-anchor="start" fill="#94a3b8">Ω</text></g></svg>
:::

::: figure Le cercle d'équation |z − 1 + 2i| = 2 : tous les points M à distance 2 du point Ω(1 − 2i).
<svg viewBox="0 0 300 250"><path d="M20 90 H285" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M140 235 V15" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M285 90 l-8 -4 l0 8 z" fill="#0f172a"/><path d="M140 15 l-4 8 l8 0 z" fill="#0f172a"/><circle cx="170" cy="150" r="60" fill="#0f6e56" opacity="0.10"/><circle cx="170" cy="150" r="60" fill="none" stroke="#0f6e56" stroke-width="2.4"/><path d="M170 150 L230 150" fill="none" stroke="#b45309" stroke-width="2.2"/><g fill="#0f172a"><circle cx="170" cy="150" r="4"/></g><g font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="131" y="84" text-anchor="end" fill="#0f172a">O</text><text x="166" y="144" text-anchor="end" fill="#0f172a">Ω</text><text x="202" y="143" text-anchor="middle" fill="#b45309">2</text></g></svg>
:::

::: piege
**Erreur : additionner les modules.** On écrit |z + z′| = |z| + |z′|. Avec z = 1 + i et z′ = 1 − i, |z + z′| = |2| = 2, alors que |z| + |z′| = 2√2 ≈ 2,83. L'inégalité triangulaire |z + z′| ≤ |z| + |z′| est une inégalité : l'égalité n'arrive que pour deux nombres de même direction. En revanche, le module d'un **produit** se multiplie bien : |zz′| = |z||z′|.
:::

::: verifie À toi : reconnaître le lieu
Quel est l'ensemble des points M d'affixe z tels que |z + 2i| = 3 ?

---

|z + 2i| = |z − (−2i)| = 3 signifie ΩM = 3 avec Ω(−2i) : c'est le cercle de centre Ω(−2i) et de rayon 3.
:::

::: retenir
|z| est la distance OM et |z_N − z_M| la distance MN ; |z − a| = r donne un cercle, |z − a| = |z − b| une médiatrice, et un quotient imaginaire un cercle de diamètre.
:::

## 🔮 Argument et écriture trigonométrique

Un radar donne la position d'un avion par sa distance au poste et sa direction.
Les deux nombres (a ; b) sont une façon de le repérer ; existe-t-il un couple « distance, direction » qui le repère tout aussi bien ?

::: definition
**Argument** (p.10) — « Le plan est muni d'un repère orthonormé direct (O, u⃗, v⃗). Soit z un nombre complexe non nul et M son image. On appelle argument de z et on note arg(z) toute mesure de l'angle (u⃗, OM⃗). » Un argument n'est défini qu'à 2π près, et 0 n'en a pas.
:::

::: figure Le couple (|z| ; θ) repère M aussi bien que (a ; b) : la partie réelle est |z| cos θ, la partie imaginaire |z| sin θ.
<svg viewBox="0 0 300 260"><path d="M25 180 H285" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M120 245 V20" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M285 180 l-8 -4 l0 8 z" fill="#0f172a"/><path d="M120 20 l-4 8 l8 0 z" fill="#0f172a"/><path d="M180 76 V180 M180 76 H120" fill="none" stroke="#94a3b8" stroke-width="1.3" stroke-dasharray="5 4"/><path d="M120 180 L180 76" fill="none" stroke="#0f6e56" stroke-width="2.6"/><path d="M155 180 A 35 35 0 0 0 137.5 149.7" fill="none" stroke="#b45309" stroke-width="2"/><g fill="#0f172a"><circle cx="180" cy="76" r="4"/><circle cx="180" cy="180" r="3"/><circle cx="120" cy="76" r="3"/></g><g font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="111" y="194" text-anchor="end" fill="#0f172a">O</text><text x="180" y="196" text-anchor="middle" fill="#0f172a">a</text><text x="112" y="80" text-anchor="end" fill="#0f172a">b</text><text x="190" y="68" fill="#0f172a">M(z)</text><text x="142" y="132" text-anchor="end" fill="#0f6e56">|z|</text><text x="152" y="168" fill="#b45309">θ</text></g></svg>
:::

::: propriete
**Écriture trigonométrique** (p.12) — « Soit z un nombre complexe non nul tel que arg(z) ≡ θ [2π]. Alors z = |z|(cos θ + i sin θ). L'écriture précédente est appelée écriture trigonométrique de z. » **Cosinus et sinus d'un argument** (p.12) — « Soit un nombre complexe non nul z = a + ib, a et b des réels. arg(z) ≡ θ [2π], si et seulement si, cos θ = a/√(a² + b²) et sin θ = b/√(a² + b²). »
:::

::: exemple Trouver module et argument

1. z = −2√3 + 2i. **Module** : |z| = √(12 + 4) = 4. **Argument** : cos θ = −2√3/4 = −√3/2 et sin θ = 2/4 = 1/2. Re(z) < 0 et Im(z) > 0, donc M est dans le deuxième quadrant, et θ = 5π/6. Ainsi z = 4(cos(5π/6) + i sin(5π/6)). Contrôle : 4(−√3/2 + i/2) = −2√3 + 2i ✓.
2. z = 1 + 9i. cos θ = 1/√82 ≈ 0,11 et sin θ > 0 ; une calculatrice donne θ ≈ 1,46 (à 10⁻² près), dans le premier quadrant ✓.
3. Valeurs lues : 4 a pour argument 0 ; −1 + i√3 a pour module 2 et pour argument 2π/3 ; 1 − i√3 a pour module 2 et pour argument −π/3.

:::

::: propriete
**Arguments de z̄, −z, kz** (p.11) — « Soit z un nombre complexe non nul et k un réel non nul. arg(z̄) ≡ −arg(z) [2π]. arg(−z) ≡ π + arg(z) [2π]. Si k > 0 alors arg(kz) ≡ arg(z) [2π]. Si k < 0 alors arg(kz) ≡ π + arg(z) [2π]. »
:::

Ces règles sont les symétries de la section précédente, lues sur les angles : z̄ est le symétrique de M par rapport à l'axe des abscisses (angle opposé), −z le symétrique par rapport à O (demi-tour, soit π de plus). Contrôle sur l'exemple 1 : −z = 2√3 − 2i a pour cosinus √3/2 et pour sinus −1/2, donc un argument −π/6 ; or 5π/6 + π = 11π/6 ≡ −π/6 [2π] ✓.

::: piege
**Erreur : se fier au cosinus seul.** Pour z = −1 − i, cos θ = −√2/2 admet deux solutions dans ]−π ; π] : 3π/4 et −3π/4. C'est le signe de la partie imaginaire (donc du sinus) qui tranche : Im(z) < 0, le point est dans le troisième quadrant, θ = −3π/4. Regarde toujours dans quel quadrant tombe le point.
:::

::: verifie À toi : écrire sous forme trigonométrique
Donner l'écriture trigonométrique de z = −3 − 3i.

---

|z| = √(9 + 9) = 3√2. cos θ = −3/(3√2) = −√2/2 et sin θ = −√2/2 : le point est dans le troisième quadrant, donc θ = −3π/4 et z = 3√2(cos(−3π/4) + i sin(−3π/4)). Contrôle : 3√2 × (−√2/2) = −3 pour chaque partie ✓.
:::

::: retenir
Un complexe non nul est repéré par (|z| ; θ) avec cos θ = a/|z| et sin θ = b/|z| : le quadrant tranche entre deux angles de même cosinus.
:::

## ✖️ Argument d'un produit, d'une puissance : la formule de Moivre

Zoomer sur une photo multiplie les longueurs ; la tourner ajoute un angle.
Les deux gestes se combinent-ils en une seule multiplication par un nombre complexe ?

::: propriete
**Arguments d'un produit, d'un quotient, d'une puissance** (p.13) — « Soit z et z′ deux nombres complexes non nuls. arg(zz′) ≡ arg(z) + arg(z′) [2π]. arg(1/z) ≡ −arg(z) [2π] ; arg(z′/z) ≡ arg(z′) − arg(z) [2π]. arg(zⁿ) ≡ n arg(z) [2π], n ∈ ℕ ; arg(1/zⁿ) ≡ −n arg(z) [2π], n ∈ ℕ. »
**Formule de Moivre** — « Soit un nombre complexe non nul z = |z|(cos θ + i sin θ). Pour tout entier n, zⁿ = |z|ⁿ(cos(nθ) + i sin(nθ)). »
**Idée de la preuve.** Avec z = |z|(cos θ + i sin θ) et z′ = |z′|(cos θ′ + i sin θ′), les formules d'addition donnent zz′ = |z||z′|(cos(θ + θ′) + i sin(θ + θ′)) : les modules se multiplient, les arguments s'ajoutent. Pour zⁿ, on répète (récurrence sur n).
:::

::: exemple Puissances et valeurs exactes

1. (1 + i)⁶. |1 + i| = √2 et arg(1 + i) ≡ π/4. Moivre : (1 + i)⁶ = (√2)⁶(cos(6π/4) + i sin(6π/4)) = 8(cos(3π/2) + i sin(3π/2)) = −8i. Contrôle : (1 + i)² = 2i, donc (1 + i)⁶ = (2i)³ = 8i³ = −8i ✓.
2. (1 − i)⁹. |1 − i| = √2 et arg ≡ −π/4. Donc (1 − i)⁹ = (√2)⁹(cos(−9π/4) + i sin(−9π/4)) = 16√2 (cos(−π/4) + i sin(−π/4)) = 16√2 × (√2/2)(1 − i) = 16 − 16i. Contrôle : (1 − i)² = −2i, (1 − i)⁸ = (−2i)⁴ = 16, puis 16(1 − i) ✓.
3. Valeurs exactes de cos π/12 et sin π/12. Avec z₁ = 1 + i (module √2, argument π/4) et z₂ = √3 − i (module 2, argument −π/6), le produit z₁z₂ a pour module 2√2 et pour argument π/4 − π/6 = π/12. Mais z₁z₂ = (√3 + 1) + i(√3 − 1). En identifiant avec 2√2(cos π/12 + i sin π/12) : cos π/12 = (√3 + 1)/(2√2) = (√6 + √2)/4 et sin π/12 = (√3 − 1)/(2√2) = (√6 − √2)/4. Contrôle numérique : cos 15° ≈ 0,966 et (2,449 + 1,414)/4 ≈ 0,966 ✓.

:::

::: piege
**Erreur : traiter arg comme une fonction linéaire de la somme.** On écrit arg(z + z′) = arg(z) + arg(z′). Faux : seul le **produit** transforme la somme des arguments. Avec z = 1 et z′ = i, arg(z + z′) = arg(1 + i) = π/4, alors que arg z + arg z′ = 0 + π/2. De même, pour une puissance, on n'oublie pas l'un des deux gestes : l'argument est multiplié par n **et** le module est mis à la puissance n.
:::

::: verifie À toi : une puissance par Moivre
Calculer (√3 + i)⁶ sous forme algébrique.

---

|√3 + i| = 2 et arg ≡ π/6, donc (√3 + i)⁶ = 2⁶(cos π + i sin π) = −64. Contrôle : (√3 + i)² = 3 + 2i√3 − 1 = 2 + 2i√3 = 4(cos π/3 + i sin π/3), puis le cube de ce nombre vaut 64(cos π + i sin π) = −64 ✓.
:::

::: retenir
Pour un produit, les modules se multiplient et les arguments s'ajoutent ; zⁿ = |z|ⁿ(cos nθ + i sin nθ) pour tout entier n.
:::

## ⚡ L'écriture exponentielle re^(iθ)

Multiplier deux complexes de module 1 revient à additionner leurs angles : c'est exactement ce que fait une exponentielle, qui transforme les sommes en produits.
Peut-on garder une notation qui rappelle cette propriété ?

::: definition
**Notation** (p.13) — « Pour tout réel θ, on note e^(iθ) le nombre complexe cos θ + i sin θ. » Un point M appartient au cercle trigonométrique si et seulement si son affixe est e^(iθ), où θ ≡ (u⃗, OM⃗) [2π].
:::

::: figure Le cercle trigonométrique : le point d'affixe e^(iθ) a pour abscisse cos θ et pour ordonnée sin θ ; i = e^(iπ/2) et −1 = e^(iπ).
<svg viewBox="0 0 300 260"><path d="M20 135 H285" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M130 250 V15" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M285 135 l-8 -4 l0 8 z" fill="#0f172a"/><path d="M130 15 l-4 8 l8 0 z" fill="#0f172a"/><circle cx="130" cy="135" r="90" fill="none" stroke="#0f6e56" stroke-width="2.2"/><path d="M175 135 V57.1 M130 57.1 H175" fill="none" stroke="#94a3b8" stroke-width="1.3" stroke-dasharray="5 4"/><path d="M130 135 L175 57.1" fill="none" stroke="#b45309" stroke-width="2.4"/><path d="M156 135 A 26 26 0 0 0 143 112.5" fill="none" stroke="#b45309" stroke-width="2"/><circle cx="175" cy="57.1" r="4" fill="#0f172a"/><circle cx="130" cy="135" r="3" fill="#0f172a"/><circle cx="220" cy="135" r="3" fill="#0f172a"/><circle cx="130" cy="45" r="3" fill="#0f172a"/><circle cx="40" cy="135" r="3" fill="#0f172a"/><circle cx="130" cy="225" r="3" fill="#0f172a"/><g font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="122" y="151" text-anchor="end" fill="#0f172a">O</text><text x="183" y="51.1" text-anchor="start" fill="#0f172a">M(e<tspan font-size="9" dy="-5">iθ</tspan>)</text><text x="226" y="151" text-anchor="start" fill="#0f172a">1</text><text x="138" y="39" text-anchor="start" fill="#0f172a">i</text><text x="36" y="151" text-anchor="end" fill="#0f172a">−1</text><text x="138" y="239" text-anchor="start" fill="#0f172a">−i</text><text x="175" y="151" text-anchor="middle" fill="#0f172a">cos θ</text><text x="124" y="61.1" text-anchor="end" fill="#0f172a">sin θ</text><text x="162" y="123" text-anchor="start" fill="#b45309">θ</text></g></svg>
:::

::: propriete
**Conséquences** (p.14) — « • e^(i0) = 1, e^(iπ/2) = i, e^(−iπ/2) = −i, e^(iπ) = −1. • Pour tout réel θ et tout entier k, e^(iθ) = e^(i(θ+2kπ)). • Pour tout réel θ, |e^(iθ)| = 1 et (e^(iθ))‾ = e^(−iθ) et −e^(iθ) = e^(i(θ+π)). » **Propriétés** (p.14) — « Soit deux réels θ et θ′. e^(iθ)·e^(iθ′) = e^(i(θ+θ′)) ; 1/e^(iθ) = e^(−iθ) ; e^(iθ)/e^(iθ′) = e^(i(θ−θ′)) ; (e^(iθ))ⁿ = e^(inθ), n ∈ ℤ. » **Théorème et définition** (p.15) — « Tout nombre complexe non nul z, s'écrit sous la forme z = re^(iθ), où r = |z| et arg(z) ≡ θ [2π]. L'écriture z = re^(iθ) est appelée écriture exponentielle de z. »
:::

::: exemple Calculer en exponentielle

1. Passer à l'exponentielle. z = √3 + i = 2e^(iπ/6) et z′ = −1 + i = √2 e^(i3π/4) (module √2 ; cosinus −√2/2 et sinus √2/2, deuxième quadrant). D'un trait : zz′ = 2√2 e^(i11π/12), z̄ = 2e^(−iπ/6) et z/z′ = √2 e^(−i7π/12). Contrôle : π/6 = 2π/12 et 3π/4 = 9π/12, donc somme 11π/12 et différence −7π/12 ✓.
2. Autres nombres : 2i = 2e^(iπ/2) ; −3i = 3e^(−iπ/2) ; −5/2 = (5/2)e^(iπ) ; √3(1 + i) = √6 e^(iπ/4).
3. Un calcul de bac : (1 + i)¹⁴/(√3 − i)⁸ sous forme algébrique. 1 + i = √2 e^(iπ/4), donc (1 + i)¹⁴ = 128 e^(i7π/2) = 128 e^(i3π/2). √3 − i = 2e^(−iπ/6), donc (√3 − i)⁸ = 256 e^(−i4π/3) = 256 e^(i2π/3). Le quotient vaut (1/2) e^(i(3π/2 − 2π/3)) = (1/2) e^(i5π/6) = −√3/4 + i/4. Contrôle : module √(3/16 + 1/16) = 1/2 = 128/256 ✓.
4. Un lieu. z = 1 + i + e^(iθ), θ ∈ [0, 2π[. Le point B(1 + 2i) en fait partie, car i = e^(iπ/2) donne z_B pour θ = π/2. Avec A(1 + i), z − z_A = e^(iθ) donne AM = |e^(iθ)| = 1 : M décrit le **cercle de centre A et de rayon 1**, en entier puisque θ parcourt un tour. Si θ ne décrit que [0, π], M ne décrit que le demi-cercle supérieur ; avec −re^(iθ) = re^(i(θ+π)), c'est le demi-cercle inférieur.

:::

::: figure Le lieu z = 1 + i + e^(iθ) : à chaque θ, M se trouve à distance 1 de A(1 + i) dans la direction θ ; avec θ ∈ [0, 2π[, M fait le tour du cercle.
<svg viewBox="0 0 300 250"><path d="M20 200 H290" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M70 240 V10" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M290 200 l-8 -4 l0 8 z" fill="#0f172a"/><path d="M70 10 l-4 8 l8 0 z" fill="#0f172a"/><circle cx="130" cy="140" r="60" fill="#0f6e56" opacity="0.10"/><circle cx="130" cy="140" r="60" fill="none" stroke="#0f6e56" stroke-width="2.4"/><path d="M130 140 L176 101.4" fill="none" stroke="#b45309" stroke-width="2.2"/><path d="M130 140 H190" fill="none" stroke="#94a3b8" stroke-width="1.3" stroke-dasharray="5 4"/><path d="M154 140 A 24 24 0 0 0 148.4 124.6" fill="none" stroke="#b45309" stroke-width="2"/><circle cx="130" cy="140" r="4" fill="#0f172a"/><circle cx="130" cy="80" r="4" fill="#0f172a"/><circle cx="176" cy="101.4" r="4" fill="#0f172a"/><circle cx="70" cy="200" r="3" fill="#0f172a"/><g font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="62" y="216" text-anchor="end" fill="#0f172a">O</text><text x="130" y="160" text-anchor="middle" fill="#0f172a">A(1 + i)</text><text x="122" y="74" text-anchor="end" fill="#0f172a">B(1 + 2i)</text><text x="184" y="97.4" text-anchor="start" fill="#b45309">M</text><text x="160" y="134" text-anchor="start" fill="#b45309">θ</text><text x="196" y="156" text-anchor="start" fill="#94a3b8">1</text></g></svg>
:::

**Une factorisation à connaître : l'angle moitié.** Pour factoriser 1 + e^(iθ), on met e^(iθ/2) en facteur : 1 + e^(iθ) = e^(iθ/2)(e^(−iθ/2) + e^(iθ/2)) = 2cos(θ/2) e^(iθ/2). De même 1 − e^(iθ) = e^(iθ/2)(e^(−iθ/2) − e^(iθ/2)) = −2i sin(θ/2) e^(iθ/2).

::: exemple Écrire 1 + e^(iθ) en exponentielle

1. z = 1 + e^(i3π/5). Avec θ = 3π/5 : z = 2cos(3π/10) e^(i3π/10). Comme cos(3π/10) ≈ 0,588 > 0, le module est 2cos(3π/10) ≈ 1,18 et un argument est 3π/10. Contrôle numérique : e^(i3π/5) ≈ −0,309 + 0,951i, donc z ≈ 0,691 + 0,951i, de module ≈ 1,18 ✓.
2. Cas où le facteur est négatif : z = 1 + e^(i4π/3) = 2cos(2π/3) e^(i2π/3) = −e^(i2π/3) = e^(i5π/3) = e^(−iπ/3). Contrôle : 1 + (−1/2 − i√3/2) = 1/2 − i√3/2 = e^(−iπ/3) ✓.

:::

::: piege
**Erreur : prendre 2cos(θ/2) pour un module sans regarder son signe.** Un module est positif. Si cos(θ/2) < 0, il faut écrire 2cos(θ/2) = −|2cos(θ/2)| et ajouter π à l'argument, comme à l'exemple 2 : le « module » −1 n'existe pas, le bon module est 1 et l'argument −π/3. Même remarque pour le facteur sin(θ/2) de 1 − e^(iθ).
:::

::: verifie À toi : l'exponentielle de 1 − e^(iθ)
Écrire 1 − e^(iπ/2) sous forme exponentielle.

---

Avec θ = π/2 : 1 − e^(iπ/2) = −2i sin(π/4) e^(iπ/4) = −i√2 e^(iπ/4) = √2 e^(i(π/4 − π/2)) = √2 e^(−iπ/4). Contrôle : 1 − i = √2 e^(−iπ/4) ✓.
:::

::: retenir
Tout z non nul s'écrit re^(iθ) ; en exponentielle, produit, quotient et puissance se font en multipliant les modules et en combinant les angles ; 1 ± e^(iθ) se factorise par e^(iθ/2).
:::

## 🧪 Complexes et trigonométrie : Moivre et Euler

Peut-on retrouver cos 4x sans formule à apprendre par cœur ?
Les complexes le permettent : une même identité écrite de deux façons donne la formule.

::: propriete
**Moivre et Euler** (p.16) — « Pour tout réel x et pour tout entier n, (cos x + i sin x)ⁿ = cos(nx) + i sin(nx) (formule de Moivre). Pour tout réel x, cos x = (e^(ix) + e^(−ix))/2 et sin x = (e^(ix) − e^(−ix))/2i (formules d'Euler). »
:::

**Développer cos nx et sin nx.** On écrit cos nx + i sin nx = (cos x + i sin x)ⁿ, on développe par le binôme de Newton avec c = cos x et s = sin x, puis on identifie parties réelle et imaginaire.

::: exemple Exprimer cos 4x et sin 4x, et une identité en tangente

1. (c + is)⁴ = c⁴ + 4ic³s + 6i²c²s² + 4i³cs³ + i⁴s⁴ = (c⁴ − 6c²s² + s⁴) + i(4c³s − 4cs³), car i² = −1, i³ = −i et i⁴ = 1. Donc cos 4x = cos⁴x − 6cos²x sin²x + sin⁴x et sin 4x = 4cos³x sin x − 4cos x sin³x.
2. Contrôle en x = π/4 : c = s = √2/2, donc c⁴ = s⁴ = 1/4 et c²s² = 1/4. cos π = 1/4 − 6/4 + 1/4 = −1 ✓ et sin π = 4c³s − 4cs³ = 0 ✓.
3. Pour x ≠ (2k + 1)π/2, e^(2ix) = (1 + i tan x)/(1 − i tan x). En effet, 1 + i tan x = (cos x + i sin x)/cos x = e^(ix)/cos x et 1 − i tan x = e^(−ix)/cos x. Le quotient est e^(ix)/e^(−ix) = e^(2ix). Contrôle en x = π/4 : (1 + i)/(1 − i) = i = e^(iπ/2) ✓.

:::

::: piege
**Erreur : oublier que i² = −1 dans le binôme.** En développant (c + is)⁴, on est tenté de garder +6c²s² comme dans (c + s)⁴. Or le terme de rang 2 porte i² = −1, d'où −6c²s², et c'est ce signe qui donne cos 2x = c² − s² dans le cas n = 2. Contrôle utile : x = π/4 doit redonner cos π = −1.
:::

::: verifie À toi : cos 3x
Par Moivre, exprimer cos 3x en fonction de cos x et sin x.

---

(c + is)³ = c³ + 3ic²s + 3i²cs² + i³s³ = (c³ − 3cs²) + i(3c²s − s³). Donc cos 3x = cos³x − 3 cos x sin²x. Contrôle en x = π/6 : (√3/2)³ − 3(√3/2)(1/4) = 3√3/8 − 3√3/8 = 0 = cos(π/2) ✓.
:::

::: retenir
Moivre développe cos nx et sin nx en puissances de cos x et sin x, avec le binôme et i² = −1 ; la tangente donne e^(2ix) = (1 + i tan x)/(1 − i tan x).
:::

## 🔧 Linéariser avec Euler

Pour intégrer cos³x, il faudrait le ramener à une somme de cosinus d'angles multiples.
Quelle formule transforme une puissance en somme ?

::: definition
**Linéariser** (p.16) — « En transformant une expression contenant une puissance de cos x ou de sin x sous une forme qui ne contient aucun produit de fonctions circulaires, on dit qu'on a linéarisé l'expression donnée. »
:::

La méthode : on remplace cos x ou sin x par les formules d'Euler, on développe la puissance par le binôme, puis on regroupe les termes conjugués e^(ikx) + e^(−ikx) = 2cos kx et e^(ikx) − e^(−ikx) = 2i sin kx.

::: methode Linéariser cosⁿx ou sinⁿx
1. Écrire cos x = (e^(ix) + e^(−ix))/2 (ou sin x = (e^(ix) − e^(−ix))/2i, avec son i au dénominateur).
2. Développer la puissance par le binôme de Newton.
3. Regrouper les puissances opposées deux à deux en 2cos kx (pour cos) ou 2i sin kx (pour sin).
4. Contrôler sur une valeur particulière de x.
5. Pour un produit sinᵐx cosⁿx, remplacer chaque facteur par sa formule d'Euler, développer chaque puissance, puis le produit, et regrouper.
:::

::: exemple Linéariser cos³x puis sin⁵x

1. cos³x = (1/8)(e^(ix) + e^(−ix))³ = (1/8)(e^(3ix) + 3e^(ix) + 3e^(−ix) + e^(−3ix)). On regroupe : e^(3ix) + e^(−3ix) = 2cos 3x et e^(ix) + e^(−ix) = 2cos x, d'où cos³x = (1/8)(2cos 3x + 6cos x) = (1/4)cos 3x + (3/4)cos x. Contrôle en x = π/3 : cos³(π/3) = 1/8 et (1/4)cos π + (3/4)(1/2) = −1/4 + 3/8 = 1/8 ✓.
2. sin⁵x = (1/(2i)⁵)(e^(ix) − e^(−ix))⁵. Le binôme donne (e^(5ix) − e^(−5ix)) − 5(e^(3ix) − e^(−3ix)) + 10(e^(ix) − e^(−ix)) = 2i(sin 5x − 5 sin 3x + 10 sin x). Comme (2i)⁵ = 32i, sin⁵x = (1/16)(sin 5x − 5 sin 3x + 10 sin x). Contrôle en x = π/2 : sin⁵ = 1 et (1/16)(1 + 5 + 10) = 1 ✓.

:::

::: piege
**Erreur : oublier le i du dénominateur de sin x.** Écrire sin x = (e^(ix) − e^(−ix))/2 donne un résultat faux d'un facteur imaginaire. Pour une puissance impaire de sin, (2i)ⁿ vaut ±2ⁿ i et le i se simplifie avec celui du numérateur ; pour une puissance paire, (2i)ⁿ est réel et aucun i ne reste. Dans tous les cas, teste ton résultat en x = 0 et en x = π/2.
:::

::: verifie À toi : linéariser sin⁴x
Linéariser sin⁴x.

---

sin⁴x = (1/16)(e^(ix) − e^(−ix))⁴ car (2i)⁴ = 16. Le binôme donne (e^(4ix) + e^(−4ix)) − 4(e^(2ix) + e^(−2ix)) + 6 = 2cos 4x − 8cos 2x + 6, donc sin⁴x = (1/8)(cos 4x − 4cos 2x + 3). Contrôle : x = 0 donne (1 − 4 + 3)/8 = 0 ✓ et x = π/2 donne (1 + 4 + 3)/8 = 1 ✓.
:::

::: retenir
Linéariser, c'est écrire cos x ou sin x avec Euler, développer par le binôme, puis regrouper e^(ikx) ± e^(−ikx) en 2cos kx ou 2i sin kx.
:::

> 🏆 Onzième porte franchie, héros : tu lis un complexe de trois façons — algébrique, trigonométrique, exponentielle — et tu passes de l'une à l'autre à volonté. Tu transformes une longueur en module, une direction en argument, un lieu en équation. Garde ces armes en main : au chapitre suivant, les équations à coefficients complexes en auront besoin.
