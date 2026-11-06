# ⚔️ Nombres complexes — des nombres qui rangent le plan

> 💡 «Dans ℝ, un carré n'est jamais négatif. Dans ℂ, x² + 1 = 0 a enfin ses solutions, et chaque nombre devient un point que l'on peut mesurer et déplacer.»

Bienvenue, héros de la section Sciences de l'informatique. Au XVIᵉ siècle, Cardan puis Bombelli rencontrent des racines de nombres négatifs en résolvant des équations du troisième degré, et ils osent calculer avec : leurs résultats finaux, réels, sont justes. La lettre i viendra bien plus tard, avec Euler. Huit étapes te mènent de la définition de ℂ aux équations de degré supérieur à deux : forme algébrique et calculs, plan complexe, conjugué, colinéarité et orthogonalité, module, lieux de points, racines carrées et second degré, factorisation. On suppose acquis le second degré dans ℝ, les vecteurs du plan et leur produit scalaire.

## 🏰 Forme algébrique et calculs dans ℂ

Dans ℕ, l'équation x + 1 = 0 n'a pas de solution : on a inventé ℤ. Dans ℤ, 2x + 1 = 0 n'en a pas : on a inventé ℚ. Dans ℚ, x² − 2 = 0 n'en a pas : on a inventé ℝ.
Dans ℝ, x² + 1 = 0 n'en a pas non plus, puisqu'un carré réel est positif ou nul. Peut-on agrandir encore l'ensemble des nombres pour que cette équation ait une solution, sans perdre les règles de calcul ?

::: definition
**Les nombres complexes.** On admet qu'il existe un ensemble, noté **ℂ**, tel que :

- ℂ contient ℝ, et l'on y additionne et multiplie avec les mêmes règles que dans ℝ ;
- ℂ contient un nombre **i**, non réel, tel que i² = −1 ;
- tout nombre z de ℂ s'écrit **de façon unique** z = a + ib, avec a et b réels.

L'écriture z = a + ib est la **forme algébrique** de z. Le réel a est sa **partie réelle**, notée Re(z) ; le réel b est sa **partie imaginaire**, notée Im(z). Si b = 0, z est réel ; si a = 0, z est un **imaginaire pur**.
:::

::: exemple Lire une forme algébrique, résoudre par identification
1. Pour z = 3 − 2i, Re(z) = 3 et Im(z) = −2 : la partie imaginaire est le réel qui multiplie i, signe compris.
2. 5 = 5 + 0i est réel, 4i = 0 + 4i est imaginaire pur, et 0 est à la fois l'un et l'autre.
3. Cherchons le réel x tel que x² − x + i(2x + 1) = 6 − 3i. La forme algébrique est unique : on égale les parties imaginaires, 2x + 1 = −3, donc x = −2.
4. Contrôle sur les parties réelles : (−2)² − (−2) = 4 + 2 = 6 ✓.

:::

::: piege Mettre le i dans la partie imaginaire
Pour z = 3 − 2i, on écrit « Im(z) = −2i ». Cela tente parce que le i est écrit juste à côté du −2. Mais Im(z) est un **réel** : c'est le coefficient de i, soit −2. Le nombre −2i est un imaginaire pur, pas un réel.
:::

::: propriete
Pour tous nombres complexes z et z′ :

- z est réel ⟺ Im(z) = 0 ; z est imaginaire pur ⟺ Re(z) = 0 ;
- z = z′ ⟺ Re(z) = Re(z′) et Im(z) = Im(z′).

Pour calculer, on développe comme dans ℝ et l'on remplace i² par −1. Les puissances de i se répètent tous les 4 crans : i² = −1, i³ = −i, i⁴ = 1, i⁵ = i, et ainsi de suite. Pour calculer iⁿ, on garde le reste r de la division de n par 4 et l'on calcule i élevé à la puissance r.

Cas limite : 0 est le seul nombre à la fois réel et imaginaire pur.
:::

::: exemple Calculer dans ℂ
1. Pour z = 2 − 3i et z′ = 1 + i : z + z′ = 3 − 2i, et 3z = 6 − 9i.
2. zz′ = (2 − 3i)(1 + i) = 2 + 2i − 3i − 3i² = 5 − i : on développe, puis i² = −1 change −3i² en +3.
3. (1 + i)² = 1 + 2i + i² = 2i, donc (1 + i)³ = 2i(1 + i) = 2i + 2i² = −2 + 2i.
4. 186 = 4 × 46 + 2, donc i¹⁸⁶ = i² = −1.
5. (1 − i)² = −2i, donc (1 − i)⁴⁰ = (−2i)²⁰ = 2²⁰ × i²⁰ = 2²⁰, car 20 est multiple de 4.

:::

::: verifie
Calculer (2 + i)(3 − 2i), puis i¹¹³.

---

(2 + i)(3 − 2i) = 6 − 4i + 3i − 2i² = 6 − i + 2 = 8 − i, car −2i² vaut +2. Puis 113 = 4 × 28 + 1, donc i¹¹³ = i : on ne garde que le reste de 113 dans la division par 4.
:::

::: retenir
Tout complexe s'écrit de façon unique a + ib ; deux complexes sont égaux si et seulement si leurs parties réelles et leurs parties imaginaires le sont ; on calcule comme dans ℝ avec i² = −1, et les puissances de i se répètent tous les 4 crans.
:::

## 🧭 Le plan complexe : affixes de points et de vecteurs

Un point du plan se repère par deux coordonnées, un nombre complexe par deux réels a et b. Le déplacement du point A(1 ; 2) au point B(4 ; 1) est le vecteur de coordonnées (3 ; −1).
Peut-on retrouver ce déplacement en soustrayant deux nombres complexes ?

::: definition
Le plan est rapporté à un repère orthonormé (O, e⃗₁, e⃗₂). Au point M(a, b) on associe le complexe z = a + ib, son **affixe**, noté Aff(M) ou z_M ; on dit que M est l'**image** de z et l'on note M(z). De même, le vecteur u⃗(a, b) a pour affixe a + ib, noté Aff(u⃗). Le plan ainsi repéré est le **plan complexe** ; l'axe des abscisses est l'**axe réel**, celui des ordonnées l'**axe imaginaire**.
:::

::: figure Le parallélogramme ABDC : ses diagonales [AD] et [BC] se coupent en leur milieu I, que l'on retrouve par le calcul sur les affixes.
<svg viewBox="0 0 290 220">
<title>Plan complexe : parallélogramme ABDC avec A(1 + 2i), B(4 + i), C(2 + 4i), D(5 + 3i) ; ses diagonales [AD] et [BC] ont le même milieu I</title>
<line x1="14" y1="190" x2="286" y2="190" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="286,190 278,194 278,186" fill="#0f172a"/>
<line x1="30" y1="206" x2="30" y2="6" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="30,6 34,14 26,14" fill="#0f172a"/>
<line x1="70" y1="187" x2="70" y2="193" stroke="#0f172a" stroke-width="1.2"/><text x="70" y="205" text-anchor="middle" fill="#0f172a" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text>
<line x1="110" y1="187" x2="110" y2="193" stroke="#0f172a" stroke-width="1.2"/><text x="110" y="205" text-anchor="middle" fill="#0f172a" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text>
<line x1="150" y1="187" x2="150" y2="193" stroke="#0f172a" stroke-width="1.2"/><text x="150" y="205" text-anchor="middle" fill="#0f172a" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">3</text>
<line x1="190" y1="187" x2="190" y2="193" stroke="#0f172a" stroke-width="1.2"/><text x="190" y="205" text-anchor="middle" fill="#0f172a" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4</text>
<line x1="230" y1="187" x2="230" y2="193" stroke="#0f172a" stroke-width="1.2"/><text x="230" y="205" text-anchor="middle" fill="#0f172a" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">5</text>
<line x1="27" y1="150" x2="33" y2="150" stroke="#0f172a" stroke-width="1.2"/><text x="22" y="154" text-anchor="end" fill="#0f172a" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text>
<line x1="27" y1="110" x2="33" y2="110" stroke="#0f172a" stroke-width="1.2"/><text x="22" y="114" text-anchor="end" fill="#0f172a" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text>
<line x1="27" y1="70" x2="33" y2="70" stroke="#0f172a" stroke-width="1.2"/><text x="22" y="74" text-anchor="end" fill="#0f172a" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">3</text>
<line x1="27" y1="30" x2="33" y2="30" stroke="#0f172a" stroke-width="1.2"/><text x="22" y="34" text-anchor="end" fill="#0f172a" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4</text>
<polygon points="70,110 190,150 230,70 110,30" fill="rgba(15,110,86,0.10)" stroke="#0f6e56" stroke-width="2.2"/>
<line x1="190" y1="150" x2="110" y2="30" stroke="#64748b" stroke-width="1.5" stroke-dasharray="5 4"/><line x1="70" y1="110" x2="230" y2="70" stroke="#64748b" stroke-width="1.5" stroke-dasharray="5 4"/>
<circle cx="70" cy="110" r="3.6" fill="#0f172a" stroke="#0f172a" stroke-width="1"/><circle cx="190" cy="150" r="3.6" fill="#0f172a" stroke="#0f172a" stroke-width="1"/><circle cx="110" cy="30" r="3.6" fill="#0f172a" stroke="#0f172a" stroke-width="1"/><circle cx="230" cy="70" r="3.6" fill="#0f172a" stroke="#0f172a" stroke-width="1"/><circle cx="150" cy="90" r="3.6" fill="#d97706" stroke="#0f172a" stroke-width="1"/>
<g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="64" y="125" text-anchor="end" fill="#0f172a" font-size="13">A</text><text x="198" y="164" text-anchor="start" fill="#0f172a" font-size="13">B</text><text x="104" y="24" text-anchor="end" fill="#0f172a" font-size="13">C</text><text x="238" y="66" text-anchor="start" fill="#0f172a" font-size="13">D</text><text x="156" y="82" text-anchor="start" fill="#d97706" font-size="13">I</text><text x="278" y="205" text-anchor="end" fill="#64748b" font-size="11">axe réel</text><text x="38" y="14" text-anchor="start" fill="#64748b" font-size="11">axe imaginaire</text></g>
</svg>
:::

L'abscisse 1 de A est la partie réelle de son affixe 1 + 2i, et son ordonnée 2 en est la partie imaginaire : lire un point sur le dessin, c'est lire un complexe.

::: exemple Du dessin aux affixes (A(1 + 2i), B(4 + i), C(2 + 4i))
1. Aff(AB⃗) = z_B − z_A = (4 + i) − (1 + 2i) = 3 − i : arrivée moins départ, comme pour les coordonnées.
2. Le milieu I de [BC] a pour affixe (z_B + z_C)/2 = (6 + 5i)/2 = 3 + (5/2)i : c'est la moyenne des deux affixes.
3. D est le symétrique de A par rapport à I, donc I est le milieu de [AD] : z_D = 2z_I − z_A = (6 + 5i) − (1 + 2i) = 5 + 3i.
4. Aff(CD⃗) = (5 + 3i) − (2 + 4i) = 3 − i = Aff(AB⃗) : deux vecteurs de même affixe sont égaux, donc AB⃗ = CD⃗ et ABDC est un parallélogramme.
5. Pour M(x, y), z = (x − 3) + i(2x − y) est réel ⟺ 2x − y = 0 (la droite y = 2x), et imaginaire pur ⟺ x − 3 = 0 (la droite x = 3).

:::

::: piege Soustraire dans le mauvais sens
On écrit Aff(AB⃗) = z_A − z_B = −3 + i. Cela tente parce que A est nommé en premier. Mais AB⃗ va de A vers B : on retranche le départ à l'arrivée, z_B − z_A = 3 − i. Le nombre z_A − z_B est l'affixe du vecteur opposé BA⃗.
:::

::: propriete
- Aff(AB⃗) = z_B − z_A ; I est le milieu de [AB] ⟺ z_I = (z_A + z_B)/2.
- Pour tout réel k, Aff(ku⃗) = k Aff(u⃗) ; et Aff(u⃗ + v⃗) = Aff(u⃗) + Aff(v⃗).
- z est réel ⟺ M(z) est sur l'axe réel ; z est imaginaire pur ⟺ M(z) est sur l'axe imaginaire ; M(z) et M′(−z) sont symétriques par rapport à O.

Cas limite : l'origine O, d'affixe 0, est le seul point situé sur les deux axes à la fois.
:::

::: verifie
Les points E et F ont pour affixes −1 + i et 3 − 2i. Donner l'affixe de EF⃗ et celle du milieu de [EF].

---

Aff(EF⃗) = z_F − z_E = (3 − 2i) − (−1 + i) = 4 − 3i : arrivée moins départ. Le milieu a pour affixe (z_E + z_F)/2 = (2 − i)/2 = 1 − (1/2)i : on prend la moyenne.
:::

::: retenir
Le point M(a, b) a pour affixe a + ib ; Aff(AB⃗) = z_B − z_A, le milieu de [AB] a pour affixe (z_A + z_B)/2, et Aff est linéaire sur les vecteurs.
:::

## 🪞 Le conjugué et la division

Pour écrire 1/(2 + √3) sans racine au dénominateur, on multiplie par 2 − √3 : le produit (2 + √3)(2 − √3) = 4 − 3 = 1 est rationnel.
Avec 1/(1 + i), le produit (1 + i)(1 − i) = 1 − i² = 2 est réel. Peut-on toujours rendre un dénominateur réel, et comment ?

::: definition
Le **conjugué** de z = a + ib est le nombre **z̄ = a − ib**. Le produit z z̄ = (a + ib)(a − ib) = a² + b² est un réel positif ou nul.
:::

::: figure M′(z̄), M″(−z) et M‴(−z̄) sont les symétriques de M(z) par rapport à l'axe réel, au point O et à l'axe imaginaire (ici z = 3 + 2i).
<svg viewBox="0 0 300 205">
<title>Plan complexe : M(z) avec z = 3 + 2i et ses trois symétriques M′(z̄) par rapport à l'axe réel, M″(−z) par rapport à O, M‴(−z̄) par rapport à l'axe imaginaire</title>
<line x1="12" y1="100" x2="288" y2="100" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="288,100 280,104 280,96" fill="#0f172a"/>
<line x1="150" y1="193" x2="150" y2="7" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="150,7 154,15 146,15" fill="#0f172a"/>
<polygon points="240,40 240,160 60,160 60,40" fill="none" stroke-dasharray="5 4" stroke="#64748b" stroke-width="1.5"/>
<line x1="240" y1="40" x2="60" y2="160" stroke="#0f6e56" stroke-width="2"/>
<circle cx="240" cy="40" r="3.8" fill="#0f172a" stroke="#0f172a" stroke-width="1"/><circle cx="240" cy="160" r="3.8" fill="#0f172a" stroke="#0f172a" stroke-width="1"/><circle cx="60" cy="160" r="3.8" fill="#0f172a" stroke="#0f172a" stroke-width="1"/><circle cx="60" cy="40" r="3.8" fill="#0f172a" stroke="#0f172a" stroke-width="1"/><g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="248" y="34" text-anchor="start" fill="#0f172a" font-size="13">M(z)</text><text x="248" y="174" text-anchor="start" fill="#0f172a" font-size="13">M′(z̄)</text><text x="52" y="174" text-anchor="end" fill="#0f172a" font-size="13">M″(−z)</text><text x="52" y="34" text-anchor="end" fill="#0f172a" font-size="13">M‴(−z̄)</text><text x="285" y="128" text-anchor="end" fill="#64748b" font-size="11">axe réel</text><text x="158" y="10" text-anchor="start" fill="#64748b" font-size="11">axe imaginaire</text></g>
</svg>
:::

Le point M′ a la même abscisse que M et une ordonnée opposée : c'est le signe de la partie imaginaire, et d'elle seule, qui change dans z̄.

::: exemple Diviser et conjuguer
1. (2 − 3i)/(1 + i) : on multiplie haut et bas par le conjugué 1 − i du dénominateur, ce qui rend celui-ci réel : (1 + i)(1 − i) = 2. D'où (2 − 3i)(1 − i)/2 = (2 − 2i − 3i + 3i²)/2 = (−1 − 5i)/2 = −1/2 − (5/2)i.
2. Contrôle : (−1/2 − (5/2)i)(1 + i) = −1/2 − i/2 − (5/2)i − (5/2)i² = 2 − 3i ✓.
3. Le conjugué de (1 + 2i)³ est (1 − 2i)³, puisque le conjugué d'une puissance est la puissance du conjugué : (1 − 2i)² = −3 − 4i, puis (1 − 2i)(−3 − 4i) = −3 − 4i + 6i + 8i² = −11 + 2i.
4. Pour z = 4 − 5i : z + z̄ = 8 = 2Re(z), un réel ; z − z̄ = −10i = 2i Im(z), un imaginaire pur.

:::

::: piege Confondre z̄ et −z
Pour z = 3 − 5i, on écrit z̄ = −3 + 5i. Cela tente parce que « conjuguer » semble vouloir dire « changer les signes ». Mais z̄ ne change que le signe de la partie imaginaire : z̄ = 3 + 5i, symétrique de z par rapport à l'axe réel. Changer les deux signes donne −z = −3 + 5i, symétrique par rapport à O.
:::

::: propriete
Pour tous complexes z et z′, et tout entier n ≥ 1 :

- conj(z̄) = z ; conj(z + z′) = z̄ + z̄′ ; conj(zz′) = z̄ z̄′ ; conj(zⁿ) = (z̄)ⁿ ;
- si z′ ≠ 0 : conj(1/z′) = 1/z̄′ et conj(z/z′) = z̄/z̄′, et 1/z′ = z̄′/(z′ z̄′) ;
- z + z̄ = 2Re(z) et z − z̄ = 2i Im(z) ;
- z est réel ⟺ z = z̄ ; z est imaginaire pur ⟺ z = −z̄.

Cas limite : 0 vérifie à la fois z = z̄ et z = −z̄, puisqu'il est réel et imaginaire pur.
:::

::: verifie
Écrire (4 + i)/(2 − 3i) sous forme algébrique.

---

Le conjugué du dénominateur est 2 + 3i et (2 − 3i)(2 + 3i) = 4 + 9 = 13, un réel. Le numérateur devient (4 + i)(2 + 3i) = 8 + 12i + 2i + 3i² = 5 + 14i. Donc le quotient vaut (5 + 14i)/13 = 5/13 + (14/13)i.
:::

::: retenir
Le conjugué de a + ib est a − ib ; il commute avec la somme, le produit, la puissance et le quotient ; z z̄ = a² + b² est réel, ce qui permet de diviser en multipliant par le conjugué du dénominateur.
:::

## 📐 Colinéarité et orthogonalité par le produit z̄z′

Soit u⃗(2 ; 1), v⃗(6 ; 3) et w⃗(−1 ; 2). On voit que v⃗ = 3u⃗, donc u⃗ et v⃗ sont colinéaires, et que 2 × (−1) + 1 × 2 = 0, donc u⃗ et w⃗ sont orthogonaux.
Calculons, avec z = 2 + i : z̄z′ pour z′ = 6 + 3i donne (2 − i)(6 + 3i) = 15, un réel ; pour z′ = −1 + 2i il donne (2 − i)(−1 + 2i) = 5i, un imaginaire pur. Est-ce un hasard ?

::: exemple Calculer z̄z′ en coordonnées
1. Pour z = a + ib et z′ = a′ + ib′, on a z̄z′ = (a − ib)(a′ + ib′).
2. On développe avec i² = −1 : z̄z′ = (aa′ + bb′) + i(ab′ − a′b).
3. La partie réelle aa′ + bb′ est le produit scalaire u⃗ · v⃗. La partie imaginaire ab′ − a′b est le déterminant de u⃗ et v⃗, nul exactement quand les vecteurs sont colinéaires.
4. Pour u⃗(2 ; 1) et v⃗(6 ; 3) : produit scalaire 15, déterminant 2 × 3 − 6 × 1 = 0, donc z̄z′ = 15 ✓. Pour w⃗(−1 ; 2) : produit scalaire 0, déterminant 2 × 2 − (−1) × 1 = 5, donc z̄z′ = 5i ✓.

:::

::: propriete
Soit u⃗ et v⃗ deux vecteurs **non nuls**, d'affixes z et z′. Alors :

- u⃗ et v⃗ sont colinéaires ⟺ z̄z′ est réel ;
- u⃗ et v⃗ sont orthogonaux ⟺ z̄z′ est imaginaire pur.

Cas limite : si l'un des vecteurs est nul, z̄z′ = 0 est à la fois réel et imaginaire pur, et le critère ne dit plus rien.
:::

::: exemple Aligner et perpendiculaire
1. A(1 + i), B(4 + 2i), C(7 + 3i) : AB⃗ a pour affixe 3 + i et AC⃗ a pour affixe 6 + 2i. Or (3 − i)(6 + 2i) = 18 + 6i − 6i − 2i² = 20, un réel : AB⃗ et AC⃗ sont colinéaires, donc A, B et C sont alignés.
2. A(3 + i), B(2), C(2i) : BA⃗ a pour affixe 1 + i et BC⃗ a pour affixe −2 + 2i. Or (1 − i)(−2 + 2i) = −2 + 2i + 2i − 2i² = 4i, un imaginaire pur : BA⃗ ⟂ BC⃗, donc ABC est rectangle en B. Contrôle : 1 × (−2) + 1 × 2 = 0 ✓.

:::

::: piege Intervertir « réel » et « imaginaire pur »
On écrit « z̄z′ est réel, donc u⃗ et v⃗ sont orthogonaux », en pensant au produit scalaire. Mais pour u⃗(2 ; 1) et v⃗(6 ; 3), z̄z′ = 15 est réel et les vecteurs sont **colinéaires**. La partie réelle est le produit scalaire, la partie imaginaire est le déterminant : z̄z′ réel signifie déterminant nul, donc colinéarité ; z̄z′ imaginaire pur signifie produit scalaire nul, donc orthogonalité.
:::

::: verifie
Les vecteurs u⃗ et v⃗ ont pour affixes 3 + 2i et −4 + 6i. Sont-ils colinéaires, orthogonaux, ou ni l'un ni l'autre ?

---

z̄z′ = (3 − 2i)(−4 + 6i) = −12 + 18i + 8i − 12i² = −12 + 26i + 12 = 26i, un imaginaire pur : u⃗ et v⃗ sont orthogonaux. Contrôle par le produit scalaire : 3 × (−4) + 2 × 6 = 0 ✓.
:::

::: retenir
Pour deux vecteurs non nuls d'affixes z et z′ : z̄z′ réel ⟺ colinéaires, z̄z′ imaginaire pur ⟺ orthogonaux, car z̄z′ = produit scalaire + i × déterminant.
:::

## 📏 Module et distances

Un robot part de O et rejoint le point M(4 + 3i). Le théorème de Pythagore donne OM = √(4² + 3²) = 5. Or z z̄ = (4 + 3i)(4 − 3i) = 16 + 9 = 25, et √25 = 5.
Est-ce un hasard, et que vaut la distance entre deux points quelconques du plan complexe ?

::: definition
Le **module** du complexe z = a + ib est le réel positif **|z| = √(z z̄) = √(a² + b²)**. C'est la distance OM, où M est l'image de z. Pour deux points A et B : **AB = |z_B − z_A|**.
:::

::: figure OM = |z| est l'hypoténuse du triangle de côtés 4 et 3, et MN est le module de la différence z_N − z_M.
<svg viewBox="0 0 300 195">
<title>Plan complexe : OM = |4 + 3i| = 5 lu dans le triangle rectangle de côtés 4 et 3, et MN = |z_N − z_M| pour N(−1 + i)</title>
<line x1="13.2" y1="150" x2="262.8" y2="150" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="262.8,150 254.8,154 254.8,146" fill="#0f172a"/>
<line x1="90" y1="166" x2="90" y2="15.6" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="90,15.6 94,23.6 86,23.6" fill="#0f172a"/>
<line x1="58" y1="147" x2="58" y2="153" stroke="#0f172a" stroke-width="1.2"/><text x="58" y="165" text-anchor="middle" fill="#0f172a" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−1</text>
<line x1="122" y1="147" x2="122" y2="153" stroke="#0f172a" stroke-width="1.2"/><text x="122" y="165" text-anchor="middle" fill="#0f172a" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text>
<line x1="154" y1="147" x2="154" y2="153" stroke="#0f172a" stroke-width="1.2"/><text x="154" y="165" text-anchor="middle" fill="#0f172a" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text>
<line x1="186" y1="147" x2="186" y2="153" stroke="#0f172a" stroke-width="1.2"/><text x="186" y="165" text-anchor="middle" fill="#0f172a" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">3</text>
<line x1="218" y1="147" x2="218" y2="153" stroke="#0f172a" stroke-width="1.2"/><text x="218" y="165" text-anchor="middle" fill="#0f172a" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4</text>
<line x1="87" y1="118" x2="93" y2="118" stroke="#0f172a" stroke-width="1.2"/><text x="82" y="122" text-anchor="end" fill="#0f172a" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text>
<line x1="87" y1="86" x2="93" y2="86" stroke="#0f172a" stroke-width="1.2"/><text x="82" y="90" text-anchor="end" fill="#0f172a" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text>
<line x1="87" y1="54" x2="93" y2="54" stroke="#0f172a" stroke-width="1.2"/><text x="82" y="58" text-anchor="end" fill="#0f172a" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">3</text>
<line x1="218" y1="54" x2="218" y2="150" stroke="#64748b" stroke-width="1.5" stroke-dasharray="5 4"/>
<line x1="90" y1="150" x2="218" y2="150" stroke="#0f172a" stroke-width="3.2"/><line x1="218" y1="150" x2="218" y2="54" stroke="#0f172a" stroke-width="3.2"/>
<path d="M 210 150 L 210 142 L 218 142" fill="none" stroke="#0f172a" stroke-width="1.2"/>
<line x1="90" y1="150" x2="218" y2="54" stroke="#0f6e56" stroke-width="2.8"/><line x1="218" y1="54" x2="58" y2="118" stroke="#d97706" stroke-width="2.4"/>
<circle cx="218" cy="54" r="3.8" fill="#0f172a" stroke="#0f172a" stroke-width="1"/><circle cx="58" cy="118" r="3.8" fill="#0f172a" stroke="#0f172a" stroke-width="1"/><g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="83" y="164" text-anchor="end" fill="#0f172a" font-size="13">O</text><text x="226" y="50" text-anchor="start" fill="#0f172a" font-size="13">M(4 + 3i)</text><text x="52" y="110" text-anchor="middle" fill="#0f172a" font-size="13">N(−1 + i)</text><text x="210" y="134" text-anchor="end" fill="#0f6e56" font-size="13">OM = |z| = 5</text><text x="132" y="74" text-anchor="end" fill="#d97706" font-size="13">MN</text><text x="226" y="106" text-anchor="start" fill="#0f172a" font-size="13">3</text></g>
</svg>
:::

Le segment OM du dessin a pour longueur |4 + 3i| = 5 ; le segment MN a pour longueur |z_N − z_M|, le module de la différence des affixes.

::: exemple Modules et distances
1. |4 + 3i| = √(16 + 9) = 5 : c'est OM dans la figure.
2. Pour N(−1 + i) : z_N − z_M = (−1 + i) − (4 + 3i) = −5 − 2i, donc MN = |−5 − 2i| = √(25 + 4) = √29.
3. O, A(2) et B(1 + i√3) : OA = 2, OB = |1 + i√3| = √(1 + 3) = 2 et AB = |−1 + i√3| = 2. Les trois côtés sont égaux : OAB est équilatéral.
4. |(√3 + i)⁵/(1 − i)³| = |√3 + i|⁵/|1 − i|³ = 2⁵/(√2)³ = 32/(2√2) = 8√2, car le module d'une puissance et celui d'un quotient se calculent facteur par facteur.

:::

::: piege Additionner les modules
On écrit |z + z′| = |z| + |z′|. Avec z = 3 + 4i et z′ = −3 + 4i, |z| = |z′| = 5, donc la somme des modules vaut 10. Mais z + z′ = 8i et |z + z′| = 8. On a seulement une inégalité : |z + z′| ≤ |z| + |z′|. Le module d'un **produit**, lui, se multiplie bien : |zz′| = |z||z′|.
:::

::: propriete
Pour tous complexes z et z′, tout réel k et tout entier n ≥ 1 :

- |z| = 0 ⟺ z = 0 ; |z|² = z z̄ ; |z̄| = |−z| = |z| ; |Re(z)| ≤ |z| et |Im(z)| ≤ |z| ;
- |zz′| = |z||z′| ; |kz| = |k||z| ; |zⁿ| = |z|ⁿ ;
- si z ≠ 0 : |1/z| = 1/|z| et |z′/z| = |z′|/|z| ;
- **inégalité triangulaire** : |z + z′| ≤ |z| + |z′|, car dans le triangle O, A(z), C(z + z′), la longueur OC ne dépasse pas OA + AC, et AC = |z′|.

Cas limite : l'égalité |z + z′| = |z| + |z′| a lieu pour z′ = 2z, deux nombres de même direction.
:::

::: verifie
Calculer |(2 − i)²(1 + 3i)|.

---

|(2 − i)²(1 + 3i)| = |2 − i|² × |1 + 3i| = 5 × √10 = 5√10, car le module d'un produit est le produit des modules et |2 − i|² = (√5)² = 5. Contrôle : (2 − i)² = 3 − 4i et (3 − 4i)(1 + 3i) = 15 + 5i, de module √250 = 5√10 ✓.
:::

::: retenir
|z| = √(z z̄) = √(a² + b²) = OM et AB = |z_B − z_A| ; le module se multiplie, se divise et se met à la puissance, mais seule une inégalité vaut pour la somme : |z + z′| ≤ |z| + |z′|.
:::

## 🎯 Lieux de points : cercles, médiatrices, droites

Un phare est placé en A(2i) et éclaire jusqu'à 3 km exactement ; deux antennes sont en P(−1) et Q(3i), et un drone M(z) doit rester à égale distance des deux.
Comment ces conditions s'écrivent-elles avec z, et quelles figures dessinent-elles ?

::: exemple Traduire un module en distance
1. |z − 2i| = 3 : z − 2i = z − z_A avec A(2i), donc AM = 3 : le cercle de centre A(2i) et de rayon 3.
2. |z + 1| = |z − 3i| : z + 1 = z − z_P avec P(−1) et z − 3i = z − z_Q avec Q(3i), donc PM = QM : la médiatrice de [PQ]. Contrôle : le milieu −1/2 + (3/2)i vérifie |1/2 + (3/2)i| = |−1/2 − (3/2)i| ✓.
3. |z̄ − 1 + i| = 2 : le conjugué de z̄ − 1 + i est z − 1 − i et deux conjugués ont le même module, donc |z − (1 + i)| = 2 : le cercle de centre Ω(1 + i) et de rayon 2.

:::

::: figure Le cercle de diamètre [AB], avec A(−i) et B(2) : en tout point M du cercle autre que A et B, les vecteurs MA⃗ et MB⃗ sont orthogonaux.
<svg viewBox="0 0 270 195">
<title>Plan complexe : le cercle de diamètre [AB] avec A(−i) et B(2), centre Ω(1 − i/2) ; en M(2 − i) du cercle, les vecteurs MA et MB sont orthogonaux</title>
<line x1="45" y1="70" x2="220" y2="70" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="220,70 212,74 212,66" fill="#0f172a"/>
<line x1="70" y1="170" x2="70" y2="25" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="70,25 74,33 66,33" fill="#0f172a"/>
<circle cx="120" cy="95" r="55.9" fill="rgba(15,110,86,0.08)" stroke="#0f6e56" stroke-width="2.4"/>
<line x1="70" y1="120" x2="170" y2="70" stroke="#64748b" stroke-width="1.6" stroke-dasharray="5 4"/>
<line x1="170" y1="120" x2="70" y2="120" stroke="#d97706" stroke-width="2.2"/><line x1="170" y1="120" x2="170" y2="70" stroke="#d97706" stroke-width="2.2"/>
<path d="M 161 120 L 161 111 L 170 111" fill="none" stroke="#d97706" stroke-width="1.2"/>
<circle cx="70" cy="120" r="3.8" fill="#0f172a" stroke="#0f172a" stroke-width="1"/><circle cx="170" cy="70" r="3.8" fill="#0f172a" stroke="#0f172a" stroke-width="1"/><circle cx="170" cy="120" r="3.8" fill="#0f172a" stroke="#0f172a" stroke-width="1"/><circle cx="120" cy="95" r="2.6" fill="#64748b" stroke="#64748b" stroke-width="1"/><g font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"><text x="63" y="136" text-anchor="end" fill="#0f172a" font-size="13">A(−i)</text><text x="178" y="64" text-anchor="start" fill="#0f172a" font-size="13">B(2)</text><text x="178" y="134" text-anchor="start" fill="#d97706" font-size="13">M(2 − i)</text><text x="118" y="88" text-anchor="middle" fill="#64748b" font-size="13">Ω</text><text x="217.5" y="85" text-anchor="end" fill="#64748b" font-size="11">axe réel</text><text x="78" y="27.5" text-anchor="start" fill="#64748b" font-size="11">axe imaginaire</text></g>
</svg>
:::

En M(2 − i), Aff(MA⃗) = −i − (2 − i) = −2 et Aff(MB⃗) = 2 − (2 − i) = i : le produit z̄z′ = (−2)(i) = −2i est imaginaire pur, ce qui traduit l'angle droit du dessin.

::: exemple Quotient réel ou imaginaire pur
Soit A(−i), B(2) et Z = (z − 2)/(z + i), avec z = x + iy et (x ; y) ≠ (0 ; −1).

1. On multiplie par le conjugué du dénominateur x + i(y + 1), qui vaut x − i(y + 1) et donne le dénominateur réel D = x² + (y + 1)².
2. Le numérateur est (x − 2 + iy)(x − i(y + 1)) = (x² − 2x + y² + y) + i(−x + 2y + 2).
3. Donc Re(Z) = (x² − 2x + y² + y)/D et Im(Z) = (−x + 2y + 2)/D.
4. Z est réel ⟺ −x + 2y + 2 = 0 : la droite (AB), privée de A.
5. Z est imaginaire pur ⟺ x² − 2x + y² + y = 0 ⟺ (x − 1)² + (y + 1/2)² = 5/4 : le cercle de diamètre [AB], de centre Ω(1 − i/2), privé de A.

:::

::: piege Lire le centre avec le mauvais signe
Pour |z + 1| = 2, on dit « cercle de centre A(1) ». Cela tente parce que le signe + est écrit dans la formule. Mais z + 1 = z − (−1) : il faut lire z − (affixe du centre), donc le centre est le point d'affixe −1 et le rayon vaut 2.
:::

::: propriete
Soit A et B deux points distincts, d'affixes a et b, et r > 0.

- |z − a| = r : le cercle de centre A et de rayon r.
- |z − a| = |z − b| : la médiatrice de [AB].
- Pour Z = (z − b)/(z − a), avec z ≠ a : Z est le quotient des affixes de BM⃗ et AM⃗. Z réel ⟺ M est sur la droite (AB) ; Z imaginaire pur ⟺ M est sur le cercle de diamètre [AB]. Dans les deux cas le point A est exclu.

Cas limite : M = B donne Z = 0, à la fois réel et imaginaire pur, donc B est dans les deux ensembles.
:::

::: verifie
Soit A(i), B(1) et Z = (z − 1)/(z − i), avec z ≠ i. Décrire l'ensemble des points M(z) pour lesquels Z est réel, puis celui pour lesquels Z est imaginaire pur.

---

Z est le quotient des affixes de BM⃗ et AM⃗. Z réel ⟺ ces vecteurs sont colinéaires ⟺ M est sur la droite (AB), privée de A. Z imaginaire pur ⟺ ils sont orthogonaux ⟺ M est sur le cercle de diamètre [AB], de centre (1 + i)/2, privé de A.
:::

::: retenir
|z − a| = r est un cercle de centre A, |z − a| = |z − b| est la médiatrice de [AB], et le quotient (z − b)/(z − a) est réel sur la droite (AB) et imaginaire pur sur le cercle de diamètre [AB], A exclu.
:::

## 🔍 Racines carrées et second degré dans ℂ

Dans ℝ, x² = −4 n'a pas de solution. Dans ℂ, (2i)² = 4i² = −4 : z² = −4 a deux solutions, 2i et −2i.
Et pour z² = 5 − 12i, où ne se voit aucune solution évidente ?

::: exemple Racines carrées de 5 − 12i
1. On pose z = x + iy : z² = x² − y² + 2ixy = 5 − 12i, donc x² − y² = 5 et 2xy = −12.
2. Les modules sont égaux : |z|² = x² + y² = |5 − 12i| = 13.
3. On additionne puis on soustrait x² − y² = 5 et x² + y² = 13 : x² = 9 et y² = 4.
4. xy = −6 est négatif, donc x et y sont de signes contraires : z = 3 − 2i ou z = −3 + 2i. Contrôle : (3 − 2i)² = 9 − 12i − 4 = 5 − 12i ✓.

:::

::: piege Garder les quatre signes
Après x² = 9 et y² = 4, on écrit z = ±3 ± 2i, soit quatre solutions. Cela tente parce que x et y sont chacun défini au signe près. Mais z² = d n'a que **deux** solutions, opposées, et c'est le signe de xy, celui de Im(d), qui les choisit : 3 − 2i et −3 + 2i. Les deux autres, 3 + 2i et −3 − 2i, sont les racines carrées de 5 + 12i.
:::

::: propriete
- Tout complexe d non nul a deux **racines carrées** opposées (résultat admis). Pour d = a + ib : x² − y² = a, x² + y² = |d|, et xy a le signe de b.
- Si d est un réel positif, ses racines carrées sont ±√d ; s'il est négatif, elles sont ±i√(−d).
- Équation az² + bz + c = 0 (a ≠ 0, coefficients complexes), de discriminant Δ = b² − 4ac, et δ une racine carrée de Δ : si Δ = 0, une solution −b/(2a) ; sinon deux solutions (−b + δ)/(2a) et (−b − δ)/(2a).
- Si a, b, c sont réels et Δ < 0 : δ = i√(−Δ), et les solutions (−b ± i√(−Δ))/(2a) sont conjuguées.

Cas limite : l'algorithme ci-dessous échoue pour un réel négatif, car alors a + |d| = 0.
:::

L'algorithme du manuel donne une racine carrée de a + ib en pseudo-code, en combinant les deux premières relations :

```
modu ← √(a² + b²)
x ← √((a + modu)/2)
y ← b/(2x)        (division par 0 si x = 0)
```

::: exemple Résoudre dans ℂ
1. z² − 6z + 13 = 0 : Δ = 36 − 52 = −16 = (4i)², donc z = (6 ± 4i)/2 = 3 ± 2i.
2. z² − 3z + 3 + i = 0 : Δ = 9 − 4(3 + i) = −3 − 4i. Ses racines carrées vérifient x² + y² = 5 et x² − y² = −3, donc x² = 1, y² = 4, et xy est négatif : δ = 1 − 2i. Alors z = (3 + 1 − 2i)/2 = 2 − i ou z = (3 − 1 + 2i)/2 = 1 + i.
3. Contrôle : (2 − i) + (1 + i) = 3 et (2 − i)(1 + i) = 3 + i ✓.

:::

::: verifie
Déterminer les racines carrées de −8 + 6i.

---

On cherche x² − y² = −8 et x² + y² = |−8 + 6i| = 10 : x² = 1 et y² = 9. Comme xy a le signe de 6, il est positif : x et y ont le même signe, d'où ±(1 + 3i). Contrôle : (1 + 3i)² = 1 + 6i − 9 = −8 + 6i ✓.
:::

::: retenir
Les racines carrées de a + ib se trouvent avec x² − y² = a, x² + y² = |d| et le signe de xy ; l'équation du second degré se résout par Δ = b² − 4ac et une racine carrée δ de Δ, même à coefficients complexes.
:::

## 🧩 Factoriser pour se ramener au second degré

L'équation z³ − 1 = 0 a une solution évidente, z = 1. Un polynôme de degré 3 qui s'annule en 1 se factorise par (z − 1).
Comment faire sortir les deux autres solutions, et que dessinent-elles dans le plan ?

::: exemple L'équation z³ − 1 = 0 et le nombre j
1. Comme 1 est solution, z³ − 1 = (z − 1)(az² + bz + c) = az³ + (b − a)z² + (c − b)z − c. On identifie : a = 1, b − a = 0, c − b = 0 et −c = −1, donc a = b = c = 1.
2. Il reste z² + z + 1 = 0 : Δ = 1 − 4 = −3, δ = i√3, donc z = (−1 ± i√3)/2. On note j = (−1 + i√3)/2 ; l'autre solution est j̄.
3. Les trois solutions sont 1, j et j̄ ; on a donc j³ = 1, et j² + j + 1 = 0 donne j² = −1 − j = j̄.
4. Pour A(1), B(j), C(j̄) : AB = |j − 1| = |(−3 + i√3)/2| = √12/2 = √3, BC = |j − j̄| = |i√3| = √3, et AC = |j̄ − 1| = |j − 1| = √3, car un nombre et son conjugué ont le même module : ABC est équilatéral.

:::

::: propriete
Soit T(z) = az² + bz + c (a ≠ 0), de solutions z′ et z″ :

- z′ + z″ = −b/a, z′z″ = c/a et T(z) = a(z − z′)(z − z″) ;
- si a + b + c = 0, les solutions sont 1 et c/a ; si a − b + c = 0, elles sont −1 et −c/a.

Cas limite : pour une solution double (Δ = 0), z′ = z″ = −b/(2a).
:::

::: methode
Pour résoudre une équation de degré 3 dont on connaît une solution z₀ : (1) écrire P(z) = (z − z₀)(az² + bz + c) et identifier les coefficients ; (2) résoudre az² + bz + c = 0 ; (3) donner z₀ et ces deux solutions.

Pour une équation bicarrée az⁴ + bz² + c = 0 : poser Z = z², résoudre en Z, puis chercher les racines carrées de chaque solution Z. Pour toute équation où une même expression de z se répète : poser Z égal à cette expression, résoudre en Z, puis revenir à z.

Cas limite : la dernière étape ne s'oublie pas, et l'expression posée doit être définie (z ≠ i dans l'exemple ci-dessous).
:::

::: exemple Poser Z
1. z⁴ + 6z² + 25 = 0 : avec Z = z², Z² + 6Z + 25 = 0, Δ = 36 − 100 = −64, donc Z = −3 ± 4i. Les racines carrées de −3 + 4i sont ±(1 + 2i), celles de −3 − 4i sont ±(1 − 2i) : quatre solutions.
2. ((z + 2)/(z − i))² − 2(z + 2)/(z − i) + 2 = 0, z ≠ i : avec Z = (z + 2)/(z − i), Z² − 2Z + 2 = 0, Δ = −4, donc Z = 1 ± i.
3. Pour Z = 1 + i : z + 2 = (1 + i)(z − i) = (1 + i)z + 1 − i, donc iz = 1 + i et z = 1 − i.
4. Pour Z = 1 − i : z + 2 = (1 − i)(z − i) = (1 − i)z − 1 − i, donc −iz = 3 + i et z = −1 + 3i.

:::

::: piege Oublier de revenir à z
Pour z⁴ + 6z² + 25 = 0, on s'arrête à « les solutions sont −3 + 4i et −3 − 4i ». Cela tente parce que l'équation en Z est résolue. Mais Z = z² est une inconnue auxiliaire : −3 ± 4i sont les valeurs de z², pas de z. Il reste à prendre leurs racines carrées.
:::

::: verifie
Résoudre z⁴ − 5z² − 36 = 0 dans ℂ.

---

On pose Z = z² : Z² − 5Z − 36 = 0, Δ = 25 + 144 = 169, donc Z = (5 ± 13)/2, soit 9 ou −4. Il faut revenir à z : z² = 9 donne z = ±3, et z² = −4 donne z = ±2i. Les quatre solutions sont 3, −3, 2i et −2i.
:::

::: retenir
Une solution connue permet de factoriser par (z − z₀) et de se ramener au second degré ; une équation bicarrée ou à expression répétée se résout en posant Z, puis en revenant à z.
:::

> 🏆 Dixième porte franchie, héros. Tu écris un complexe sous sa forme algébrique, tu le places dans le plan, tu le conjugues, tu mesures des distances avec son module, tu décris des cercles et des médiatrices, et tu résous des équations jusqu'au degré 4. Au chapitre 11, les systèmes d'équations linéaires prendront le relais.
