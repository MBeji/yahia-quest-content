# ⚔️ Équations à coefficients complexes — là où chaque équation trouve ses solutions

> 💡 «Dans ℝ, une équation peut rester sans réponse ; dans ℂ, elle en trouve toujours, pourvu qu'on sache extraire une racine carrée.»

Ce chapitre prolonge les nombres complexes : on y extrait des racines carrées, on résout le second degré même quand les coefficients ne sont pas réels, on cherche les racines nièmes, puis on ramène les équations de degré 3, 4 ou 6 au second degré. Huit notions, de la racine carrée d'un complexe aux équations qui dépendent d'un paramètre θ. Le plan est rapporté à un repère orthonormé direct (O, u⃗, v⃗), et l'on emploie l'écriture exponentielle du chapitre précédent.

## 🔍 Racines carrées d'un complexe : le système

Dans ℝ, l'équation x² = 9 a deux solutions, 3 et −3, et x² = −1 n'en a aucune. Dans ℂ, que devient z² = −15 + 8i ?
Existe-t-il un complexe dont le carré vaut −15 + 8i, et combien en existe-t-il ?

::: definition
Soit Z un nombre complexe. On appelle **racine carrée** de Z tout complexe z tel que z² = Z.
Exemples : i et −i sont les racines carrées de −1 ; 1 + i est une racine carrée de 2i, car (1 + i)² = 2i.
:::

::: exemple Racines carrées de Z = −15 + 8i

On pose z = x + iy avec x et y réels, donc z² = x² − y² + 2ixy.

1. Deux complexes égaux ont mêmes parties réelle et imaginaire : z² = Z donne x² − y² = −15 et 2xy = 8.
2. On ajoute une équation tirée du module, car |z²| = |z|² = x² + y² : x² + y² = |Z| = √(15² + 8²) = √289 = 17.
3. En additionnant puis en soustrayant les deux équations en x² et y² : 2x² = 2, donc x² = 1 ; 2y² = 32, donc y² = 16. Ainsi x = ±1 et y = ±4.
4. Le produit 2xy = 8 est positif, donc x et y ont le même signe : on garde (1 ; 4) et (−1 ; −4). Les racines carrées sont 1 + 4i et −1 − 4i. Contrôle : (1 + 4i)² = 1 + 8i + 16i² = −15 + 8i ✓.

:::

::: piege
**Erreur : garder les quatre couples (±1 ; ±4).** L'erreur tente parce que x² = 1 et y² = 16 laissent quatre combinaisons de signes. Mais l'équation 2xy = 8 en écarte deux : (1 − 4i)² = 1 − 8i − 16 = −15 − 8i, ce qui n'est pas Z. Un complexe non nul n'a que deux racines carrées.
:::

::: propriete
Soit Z = a + ib un complexe non nul. L'équation z² = Z, avec z = x + iy, équivaut au système :
$$ x² − y² = a ;  2xy = b ;  x² + y² = √(a² + b²) $$
Z admet exactement deux racines carrées, opposées l'une de l'autre : si z en est une, l'autre est −z.
Cas limites : si Z est un réel négatif, comme −9, alors 2xy = 0 et x² − y² = −9 < 0 imposent x = 0 et y² = 9 et les racines carrées sont 3i et −3i ; si Z = 0, son unique racine carrée est 0.
:::

::: verifie À toi : racines carrées de 8 + 6i
Trouver les racines carrées de 8 + 6i.

---

On a |Z| = √(64 + 36) = 10, donc x² − y² = 8 et x² + y² = 10, d'où x² = 9 et y² = 1. Comme 2xy = 6 > 0, x et y ont le même signe : les racines carrées sont 3 + i et −3 − i. Contrôle : (3 + i)² = 9 + 6i − 1 = 8 + 6i ✓.
:::

::: retenir
Pour z² = a + ib, on résout x² − y² = a, 2xy = b et x² + y² = √(a² + b²) ; il y a deux racines carrées opposées, et le signe de 2xy dit si x et y ont le même signe ou des signes contraires.
:::

## 📐 Racines carrées : l'écriture exponentielle

Le système marche toujours, mais il est long. Quand Z est donné par son module et son argument, mettre au carré revient à élever le module au carré et à doubler l'argument (chapitre précédent). Peut-on remonter ce chemin ?
Cherchons les racines carrées de Z = −2 + 2i√3, dont le module vaut 4 et l'argument 2π/3.

::: figure Les deux racines carrées z₁ et z₂ de Z sont opposées et leur module 2 est la racine carrée de |Z| = 4 ; l'argument de z₁ est la moitié de celui de Z
<svg viewBox="0 0 300 262">
<title>Le point Z d'argument 2π/3 et de module 4, et ses deux racines carrées z₁ (argument π/3, module 2) et z₂ = −z₁, symétriques par rapport à l'origine</title>
<path d="M34.8 170 H279.6" fill="none" stroke="#0f172a" stroke-width="1.6"/>
<path d="M150 256.4 V18.8" fill="none" stroke="#0f172a" stroke-width="1.6"/>
<path d="M279.6 170 l-8 -4 l0 8 z" fill="#0f172a"/>
<path d="M150 18.8 l-4 8 l8 0 z" fill="#0f172a"/>
<path d="M186 167 V173" stroke="#0f172a" stroke-width="1.2"/>
<text x="186" y="186" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">1</text>
<path d="M222 167 V173" stroke="#0f172a" stroke-width="1.2"/>
<text x="222" y="186" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">2</text>
<path d="M258 167 V173" stroke="#0f172a" stroke-width="1.2"/>
<text x="258" y="186" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">3</text>
<path d="M114 167 V173" stroke="#0f172a" stroke-width="1.2"/>
<text x="114" y="186" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">−1</text>
<path d="M78 167 V173" stroke="#0f172a" stroke-width="1.2"/>
<text x="78" y="186" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">−2</text>
<path d="M147 134 H153" stroke="#0f172a" stroke-width="1.2"/>
<text x="143" y="138" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">i</text>
<path d="M147 98 H153" stroke="#0f172a" stroke-width="1.2"/>
<text x="143" y="102" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">2i</text>
<path d="M147 62 H153" stroke="#0f172a" stroke-width="1.2"/>
<text x="143" y="66" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">3i</text>
<path d="M147 206 H153" stroke="#0f172a" stroke-width="1.2"/>
<text x="143" y="210" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">−i</text>
<path d="M147 242 H153" stroke="#0f172a" stroke-width="1.2"/>
<text x="143" y="246" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">−2i</text>
<text x="144" y="185" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">O</text>
<circle cx="150" cy="170" r="72" fill="none" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="5 4"/>
<path d="M114 232.4 L186 107.6" fill="none" stroke="#0f6e56" stroke-width="2.4"/>
<path d="M150 170 L78 45.3" fill="none" stroke="#b45309" stroke-width="2.4"/>
<path d="M172 170 A22 22 0 0 0 161 150.9" fill="none" stroke="#0f6e56" stroke-width="1.6"/>
<path d="M194 170 A44 44 0 0 0 128 131.9" fill="none" stroke="#b45309" stroke-width="1.6"/>
<circle cx="78" cy="45.3" r="4" fill="#b45309"/>
<circle cx="186" cy="107.6" r="4" fill="#0f6e56"/>
<circle cx="114" cy="232.4" r="4" fill="#0f6e56"/>
<text x="87" y="43.3" text-anchor="start" font-size="12" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">Z, |Z| = 4</text>
<text x="194" y="103.6" text-anchor="start" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">z₁, |z₁| = 2</text>
<text x="104" y="236.4" text-anchor="end" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">z₂ = −z₁</text>
<text x="177" y="161" text-anchor="start" font-size="11" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">π/3</text>
<text x="104" y="126" text-anchor="end" font-size="11" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">2π/3</text>
</svg>
:::

Sur la figure, z₁ a pour argument π/3, moitié de 2π/3, et pour module 2, tel que 2² = 4 ; z₂ est le symétrique de z₁ par rapport à O.

::: exemple Les racines carrées de Z = −2 + 2i√3

1. Module et argument de Z : |Z| = √(4 + 12) = 4, cos θ = −2/4 = −1/2 et sin θ = 2√3/4 = √3/2, donc θ = 2π/3 et Z = 4 e^(i2π/3).
2. On prend la racine carrée du module et la moitié de l'argument : z₁ = √4 · e^(iπ/3) = 2 e^(iπ/3), car (2 e^(iπ/3))² = 4 e^(i2π/3).
3. L'autre racine est l'opposée : z₂ = −z₁ = 2 e^(i4π/3), car −e^(iπ/3) = e^(i(π/3 + π)).
4. En forme algébrique, z₁ = 2(1/2 + i√3/2) = 1 + i√3 et z₂ = −1 − i√3. Contrôle : (1 + i√3)² = 1 + 2i√3 − 3 = −2 + 2i√3 ✓.

:::

::: exemple Un réel négatif et un imaginaire pur

1. Z = −3 = 3 e^(iπ) donne z₁ = √3 · e^(iπ/2) = i√3, donc les racines carrées de −3 sont i√3 et −i√3.
2. Z = −2i = 2 e^(−iπ/2) donne z₁ = √2 · e^(−iπ/4) = √2(√2/2 − i√2/2) = 1 − i, et z₂ = −1 + i. Contrôle : (1 − i)² = 1 − 2i − 1 = −2i ✓.

:::

::: piege
**Erreur : diviser le module par 2 en même temps que l'argument.** L'erreur tente parce qu'on « coupe en deux » les deux données de Z. Mais le module de z doit vérifier |z|² = |Z|, donc |z| = √|Z|. Dans l'exemple, √4 et 4/2 valent tous deux 2, ce qui cache la faute ; avec Z = 16 e^(iπ/3), le module de z est √16 = 4 et non 16/2 = 8.
:::

::: propriete
Soit Z = λ e^(iα) un complexe non nul (λ > 0). L'équation z² = Z admet deux solutions opposées :
$$ z₁ = √λ · e^(iα/2)  et  z₂ = −z₁ = √λ · e^(i(α/2 + π)) $$
Cas limites : un réel positif c a pour racines carrées √c et −√c ; un réel négatif −c s'écrit c e^(iπ), de racines carrées i√c et −i√c. Choisir α + 2π au lieu de α change z₁ en −z₁ : on retrouve les mêmes deux racines.
:::

::: verifie À toi : une racine carrée sous forme exponentielle
Donner les racines carrées de Z = 2 − 2i√3.

---

On a |Z| = √(4 + 12) = 4, cos θ = 1/2 et sin θ = −√3/2, donc θ = −π/3 et Z = 4 e^(−iπ/3). Alors z₁ = √4 · e^(−iπ/6) = 2(√3/2 − i/2) = √3 − i et z₂ = −z₁ = −√3 + i. Contrôle : (√3 − i)² = 3 − 2i√3 − 1 = 2 − 2i√3 ✓.
:::

::: retenir
Si Z = λ e^(iα), ses racines carrées sont √λ e^(iα/2) et son opposée : racine carrée du module, moitié de l'argument.
:::

## 🧮 Le second degré à coefficients complexes

Pour résoudre z² + (1 − 4i)z − 5 − 5i = 0, on pense au discriminant. Mais dans ℂ, Δ sera un complexe, qui n'est ni positif ni négatif.
Que faire d'un Δ sans signe ? Les racines carrées du paragraphe précédent vont répondre.

::: definition
Soient a, b et c trois complexes avec a ≠ 0. L'équation **az² + bz + c = 0** est une **équation du second degré à coefficients complexes** ; le complexe **Δ = b² − 4ac** est son **discriminant**.
:::

::: exemple Résoudre z² + (1 − 4i)z − 5 − 5i = 0

1. Ici a = 1, b = 1 − 4i et c = −5 − 5i : Δ = (1 − 4i)² − 4(−5 − 5i) = 1 − 8i − 16 + 20 + 20i = 5 + 12i.
2. On cherche une racine carrée δ de Δ par le système : x² − y² = 5, 2xy = 12 et x² + y² = √(25 + 144) = 13. D'où x² = 9, y² = 4 et xy > 0, donc δ = 3 + 2i. Contrôle : (3 + 2i)² = 9 + 12i − 4 = 5 + 12i ✓.
3. On applique z = (−b ± δ)/(2a) : z′ = (−1 + 4i − 3 − 2i)/2 = −2 + i et z″ = (−1 + 4i + 3 + 2i)/2 = 1 + 3i.
4. Contrôle par réinjection de z′ : (−2 + i)² = 3 − 4i et (1 − 4i)(−2 + i) = 2 + 9i, donc 3 − 4i + 2 + 9i − 5 − 5i = 0 ✓.

:::

::: piege
**Erreur : conclure « Δ = 5 + 12i n'est pas positif, donc pas de solution ».** L'erreur tente parce que, dans ℝ, un discriminant négatif ferme la porte. Mais dans ℂ on n'a pas besoin du signe de Δ : on a besoin d'une racine carrée de Δ, et tout complexe en possède. De même, δ n'est pas « √Δ » : la notation √ est réservée aux réels positifs, et Δ a deux racines carrées.
:::

::: exemple Un discriminant nul

Résolvons z² − 2iz − 1 = 0, où b = −2i s'écrit 2b′ avec b′ = −i.

1. Le discriminant réduit est Δ′ = b′² − ac = (−i)² − 1 × (−1) = −1 + 1 = 0.
2. Δ′ = 0 donne une racine double, z = −b′/a = i. Contrôle : (z − i)² = z² − 2iz + i² = z² − 2iz − 1 ✓.

:::

::: propriete
Soit az² + bz + c = 0, avec a ∈ ℂ*, b et c complexes, et Δ = b² − 4ac.
Si Δ ≠ 0, il y a deux solutions distinctes z′ = (−b − δ)/(2a) et z″ = (−b + δ)/(2a), où δ est une racine carrée de Δ ; l'autre racine carrée −δ échange simplement z′ et z″.
Si Δ = 0, il y a une racine double z′ = z″ = −b/(2a).
Dans tous les cas, az² + bz + c = a(z − z′)(z − z″).
Si b = 2b′, on peut employer Δ′ = b′² − ac (alors Δ = 4Δ′) : z = (−b′ ± δ′)/a, où δ′ est une racine carrée de Δ′.
:::

::: verifie À toi : un discriminant imaginaire pur
Résoudre z² − (3 + 3i)z + 5i = 0.

---

Δ = (3 + 3i)² − 4 × 5i = 18i − 20i = −2i. Une racine carrée de −2i est 1 − i, car (1 − i)² = −2i. Alors z = ((3 + 3i) ± (1 − i))/2, soit z′ = (2 + 4i)/2 = 1 + 2i et z″ = (4 + 2i)/2 = 2 + i. Contrôle par réinjection de z″ : (2 + i)² = 3 + 4i, (3 + 3i)(2 + i) = 3 + 9i, donc 3 + 4i − 3 − 9i + 5i = 0 ✓.
:::

::: retenir
Δ = b² − 4ac est un complexe : on en cherche une racine carrée δ et z = (−b ± δ)/(2a) ; Δ = 0 donne la racine double −b/(2a) ; az² + bz + c = a(z − z′)(z − z″).
:::

## ⚖️ Somme et produit des racines

Dans z² − (5 + i)z + 6 + 3i = 0, on constate que 3 est solution : 9 − 15 − 3i + 6 + 3i = 0.
Faut-il calculer Δ pour trouver l'autre solution, ou le polynôme la livre-t-il déjà ?

::: exemple L'autre racine sans calculer Δ

1. D'après la factorisation az² + bz + c = a(z − z′)(z − z″), le développement donne az² − a(z′ + z″)z + a z′z″, donc z′ + z″ = −b/a = 5 + i.
2. L'autre racine vaut alors (5 + i) − 3 = 2 + i, car la somme des deux racines est 5 + i.
3. Contrôle par le produit : 3 × (2 + i) = 6 + 3i = c/a ✓.

:::

::: exemple Deux complexes de somme et de produit donnés

On cherche z′ et z″ avec z′ + z″ = 4 − i et z′z″ = 5 + i.

1. Ce sont les solutions de z² − Sz + P = 0, soit z² − (4 − i)z + 5 + i = 0, car z² − Sz + P = (z − z′)(z − z″).
2. Δ = (4 − i)² − 4(5 + i) = 16 − 8i − 1 − 20 − 4i = −5 − 12i. Le système donne x² − y² = −5 et x² + y² = 13, d'où x² = 4 et y² = 9 ; 2xy = −12 < 0, donc x et y sont de signes contraires et δ = 2 − 3i.
3. Alors z′ = ((4 − i) − (2 − 3i))/2 = 1 + i et z″ = ((4 − i) + (2 − 3i))/2 = 3 − 2i. Contrôle : somme 4 − i ✓ et produit (1 + i)(3 − 2i) = 3 − 2i + 3i + 2 = 5 + i ✓.

:::

::: piege
**Erreur : écrire z′ + z″ = b/a, sans le signe moins.** L'erreur tente parce que b est « le coefficient de z ». Dans z² − (5 + i)z + 6 + 3i, on aurait b/a = −5 − i, puis une autre racine −5 − i − 3 = −8 − i, qui ne vérifie pas le produit : 3 × (−8 − i) = −24 − 3i ≠ 6 + 3i. La somme est −b/a, le produit est c/a.
:::

::: propriete
Si z′ et z″ sont les racines de az² + bz + c = 0 (a ≠ 0), alors :
$$ z′ + z″ = −b/a  et  z′ z″ = c/a $$
Réciproquement, deux complexes de somme S et de produit P sont les solutions de z² − Sz + P = 0.
Cas limite : pour une racine double (Δ = 0), z′ = z″ = −b/(2a), donc la somme vaut 2z′ et le produit z′².
:::

::: verifie À toi : l'autre racine, avec a différent de 1
L'équation 2z² − (6 + 2i)z + 4 + 4i = 0 admet pour solution 1 + i. Trouver l'autre solution sans calculer Δ.

---

La somme des racines est −b/a = (6 + 2i)/2 = 3 + i, donc l'autre racine vaut (3 + i) − (1 + i) = 2. Contrôle par le produit : c/a = (4 + 4i)/2 = 2 + 2i et (1 + i) × 2 = 2 + 2i ✓.
:::

::: retenir
z′ + z″ = −b/a et z′z″ = c/a : connaissant une racine, on trouve l'autre sans Δ ; deux complexes de somme S et de produit P sont les solutions de z² − Sz + P = 0.
:::

## 🪞 Coefficients réels : des solutions conjuguées

Dans ℝ, l'équation z² + 6z + 25 = 0 n'a pas de solution, puisque Δ = 36 − 100 est négatif. Que donne-t-elle dans ℂ ?
Et les deux solutions qu'on va trouver ont-elles un lien entre elles ?

::: figure Les deux solutions −3 + 4i et −3 − 4i sont symétriques par rapport à l'axe des réels : ce sont des conjuguées
<svg viewBox="0 0 300 250">
<title>Les deux solutions −3 + 4i et −3 − 4i de z² + 6z + 25 = 0 sont symétriques par rapport à l'axe des réels</title>
<path d="M38.2 125 H256.6" fill="none" stroke="#0f172a" stroke-width="1.6"/>
<path d="M215 249.8 V0.2" fill="none" stroke="#0f172a" stroke-width="1.6"/>
<path d="M256.6 125 l-8 -4 l0 8 z" fill="#0f172a"/>
<path d="M215 0.2 l-4 8 l8 0 z" fill="#0f172a"/>
<path d="M137 122 V128" stroke="#0f172a" stroke-width="1.2"/>
<text x="137" y="141" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">−3</text>
<path d="M163 122 V128" stroke="#0f172a" stroke-width="1.2"/>
<text x="163" y="141" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">−2</text>
<path d="M189 122 V128" stroke="#0f172a" stroke-width="1.2"/>
<text x="189" y="141" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">−1</text>
<path d="M241 122 V128" stroke="#0f172a" stroke-width="1.2"/>
<text x="241" y="141" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">1</text>
<path d="M212 99 H218" stroke="#0f172a" stroke-width="1.2"/>
<text x="208" y="103" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">i</text>
<path d="M212 73 H218" stroke="#0f172a" stroke-width="1.2"/>
<text x="208" y="77" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">2i</text>
<path d="M212 47 H218" stroke="#0f172a" stroke-width="1.2"/>
<text x="208" y="51" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">3i</text>
<path d="M212 21 H218" stroke="#0f172a" stroke-width="1.2"/>
<text x="208" y="25" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">4i</text>
<path d="M212 151 H218" stroke="#0f172a" stroke-width="1.2"/>
<text x="208" y="155" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">−i</text>
<path d="M212 177 H218" stroke="#0f172a" stroke-width="1.2"/>
<text x="208" y="181" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">−2i</text>
<path d="M212 203 H218" stroke="#0f172a" stroke-width="1.2"/>
<text x="208" y="207" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">−3i</text>
<path d="M212 229 H218" stroke="#0f172a" stroke-width="1.2"/>
<text x="208" y="233" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">−4i</text>
<text x="209" y="140" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">O</text>
<path d="M137 21 L137 229" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-dasharray="5 4"/>
<path d="M215 125 L137 21" fill="none" stroke="#0f6e56" stroke-width="2.2"/>
<path d="M215 125 L137 229" fill="none" stroke="#b45309" stroke-width="2.2"/>
<circle cx="137" cy="21" r="4" fill="#0f6e56"/>
<circle cx="137" cy="229" r="4" fill="#b45309"/>
<text x="128" y="19" text-anchor="end" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">z′ = −3 + 4i</text>
<text x="128" y="243" text-anchor="end" font-size="12" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">z″ = −3 − 4i</text>
</svg>
:::

Sur la figure, z′ et z″ ont la même partie réelle −3 et des parties imaginaires opposées 4 et −4 : z″ est le conjugué de z′.

::: exemple Résoudre z² + 6z + 25 = 0

1. Ici Δ = 36 − 100 = −64, un réel négatif. Une racine carrée de −64 est 8i, car (8i)² = −64.
2. Alors z = (−6 ± 8i)/2, soit z′ = −3 + 4i et z″ = −3 − 4i, car on divise par 2a = 2.
3. Les deux solutions sont conjuguées. Contrôle : la somme vaut −6 = −b/a ✓ et le produit (−3 + 4i)(−3 − 4i) = 9 + 16 = 25 = c/a ✓.

:::

::: piege
**Erreur : « 1 + i est solution, donc 1 − i l'est aussi », dans une équation aux coefficients non réels.** L'erreur tente parce qu'on retient « les solutions sont conjuguées ». Pour z² − (3 + i)z + 2 + 2i = 0, on vérifie que 1 + i est solution : 2i − (3 + i)(1 + i) + 2 + 2i = 2i − 2 − 4i + 2 + 2i = 0. Mais pour 1 − i : −2i − (3 + i)(1 − i) + 2 + 2i = −2i − 4 + 2i + 2 + 2i = −2 + 2i ≠ 0. L'autre solution est 3 + i − (1 + i) = 2. La conjugaison exige des coefficients tous réels.
:::

::: propriete
Soit az² + bz + c = 0 avec a, b, c réels et a ≠ 0, et Δ = b² − 4ac, qui est alors un réel.
Si Δ > 0, deux solutions réelles distinctes ; si Δ = 0, une solution réelle double ; si Δ < 0, deux solutions complexes conjuguées :
$$ z′ = (−b − i√(−Δ))/(2a)  et  z″ = (−b + i√(−Δ))/(2a) $$
Réciproquement, si z² + αz + β = 0 a deux solutions conjuguées z′ et z̄′, alors α = −(z′ + z̄′) = −2 Re(z′) et β = z′ z̄′ = |z′|² sont réels.
Cas limite : « Δ < 0 » n'a de sens que parce que Δ est réel ; avec un coefficient non réel, Δ est un complexe qu'on ne compare pas à 0.
:::

::: verifie À toi : solutions conjuguées
Résoudre z² − 2z + 10 = 0, puis donner le produit des deux solutions.

---

Δ′ = (−1)² − 10 = −9 < 0, de racine carrée 3i, donc z = 1 ± 3i : les solutions sont 1 + 3i et 1 − 3i, conjuguées car les coefficients sont réels. Leur produit vaut |1 + 3i|² = 1 + 9 = 10 = c/a ✓.
:::

::: retenir
À coefficients réels et Δ < 0, les deux solutions sont conjuguées, de somme −b/a et de produit |z|² = c/a ; dès qu'un coefficient n'est pas réel, rien ne garantit la conjugaison.
:::

## 🔶 Racines nièmes d'un complexe

Dans ℝ, x³ = 8 n'a qu'une solution, 2. Dans ℂ, le nombre −1 + i√3 vérifie lui aussi (−1 + i√3)³ = 8, car (−1 + i√3)² = −2 − 2i√3 puis (−2 − 2i√3)(−1 + i√3) = 2 + 6 = 8.
Combien de complexes z vérifient z³ = 8, et où se trouvent-ils dans le plan ?

::: definition
Soient n un entier naturel non nul et Z un complexe non nul. On appelle **racine nième** de Z tout complexe z tel que zⁿ = Z. Si Z = 1, on dit que z est une **racine nième de l'unité**.
Exemple : 1, −1, i et −i sont les racines quatrièmes de 1.
:::

::: figure Les trois solutions de z³ = 8 : sur le cercle de centre O et de rayon 2, espacées de 2π/3, elles forment un triangle équilatéral
<svg viewBox="0 0 300 250">
<title>Les trois solutions de z³ = 8 : 2, −1 + i√3 et −1 − i√3, sommets d'un triangle équilatéral inscrit dans le cercle de centre O et de rayon 2</title>
<path d="M10 125 H275" fill="none" stroke="#0f172a" stroke-width="1.6"/>
<path d="M140 235 V10" fill="none" stroke="#0f172a" stroke-width="1.6"/>
<path d="M275 125 l-8 -4 l0 8 z" fill="#0f172a"/>
<path d="M140 10 l-4 8 l8 0 z" fill="#0f172a"/>
<path d="M190 122 V128" stroke="#0f172a" stroke-width="1.2"/>
<text x="190" y="141" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">1</text>
<path d="M90 122 V128" stroke="#0f172a" stroke-width="1.2"/>
<text x="90" y="141" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">−1</text>
<path d="M137 75 H143" stroke="#0f172a" stroke-width="1.2"/>
<text x="133" y="79" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">i</text>
<path d="M137 175 H143" stroke="#0f172a" stroke-width="1.2"/>
<text x="133" y="179" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">−i</text>
<text x="134" y="140" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">O</text>
<circle cx="140" cy="125" r="100" fill="none" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="5 4"/>
<path d="M240 125 L90 38.4 L90 211.6 Z" fill="#0f6e56" opacity="0.1"/>
<path d="M240 125 L90 38.4 L90 211.6 Z" fill="none" stroke="#0f6e56" stroke-width="2" stroke-linejoin="round"/>
<circle cx="240" cy="125" r="4" fill="#0f6e56"/>
<circle cx="90" cy="38.4" r="4" fill="#0f6e56"/>
<circle cx="90" cy="211.6" r="4" fill="#0f6e56"/>
<text x="248" y="119" text-anchor="start" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">z₀ = 2</text>
<text x="82" y="32.4" text-anchor="end" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">z₁ = −1 + i√3</text>
<text x="82" y="227.6" text-anchor="end" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">z₂ = −1 − i√3</text>
</svg>
:::

Sur la figure, les trois points sont à la distance 2 de O, valeur de la racine cubique du module 8, et deux points voisins sont séparés de l'angle 2π/3, soit 2kπ/3 pour k = 0, 1, 2.

::: exemple Les solutions de z³ = 8

1. On écrit 8 = 8 e^(i0), de module r = 8 et d'argument θ = 0, avec n = 3.
2. Le module de z est la racine cubique réelle positive de 8, soit 2, car |z|³ = 8.
3. Les arguments sont (0 + 2kπ)/3 = 2kπ/3 pour k = 0, 1, 2 : z₀ = 2, z₁ = 2 e^(i2π/3) = −1 + i√3 et z₂ = 2 e^(i4π/3) = −1 − i√3.
4. Pour k = 3 on retombe sur 2 e^(i2π) = 2 = z₀ : il y a exactement trois solutions. Contrôle : z₁³ = 8 e^(i2π) = 8 ✓.

:::

::: exemple Un argument non nul : z⁴ = −8 + 8i√3

1. |Z| = √(64 + 192) = 16, cos θ = −8/16 = −1/2 et sin θ = 8√3/16 = √3/2, donc Z = 16 e^(i2π/3).
2. Le module de z est la racine quatrième réelle positive de 16, soit 2, et les arguments sont (2π/3 + 2kπ)/4 = π/6 + kπ/2 pour k = 0, 1, 2, 3.
3. z₀ = 2 e^(iπ/6) = √3 + i, z₁ = 2 e^(i2π/3) = −1 + i√3, z₂ = 2 e^(i7π/6) = −√3 − i et z₃ = 2 e^(i5π/3) = 1 − i√3. Contrôle : z₀⁴ = 16 e^(i2π/3) = Z ✓.

:::

::: piege
**Erreur : diviser l'argument par n sans ajouter 2kπ/n.** L'erreur tente parce que, dans ℝ, on prend une seule racine cubique. Pour z³ = 8, écrire seulement z = 2 e^(i0/3) = 2 fait croire que l'équation n'a qu'une solution. Mais l'argument de Z est connu à 2π près : chaque entier k donne une direction (θ + 2kπ)/n, et il y en a exactement n distinctes. Pour z⁴ = −8 + 8i√3, oublier k ne livre qu'une solution sur quatre.
:::

::: propriete
Soit Z = r e^(iθ), avec r > 0, et n ≥ 2 un entier. L'équation zⁿ = Z admet exactement n solutions distinctes :
$$ z_k = ⁿ√r · e^(i(θ + 2kπ)/n),  k ∈ {0 ; 1 ; … ; n − 1} $$
où ⁿ√r est la racine nième réelle positive de r. Leurs images sont les sommets d'un polygone régulier à n côtés inscrit dans le cercle de centre O et de rayon ⁿ√r : un triangle équilatéral pour n = 3, un carré pour n = 4, un pentagone régulier pour n = 5. Le côté du polygone est la distance |z₁ − z₀| = ⁿ√r · |e^(i2π/n) − 1| entre deux sommets voisins ; pour n = 6, les triangles OM_kM_(k+1) sont équilatéraux et le côté est égal au rayon.
Cas limite : z_k = z_k′ si et seulement si k − k′ est un multiple de n, d'où z_n = z₀.
Pour n = 3 et Z = 1, on pose j = e^(i2π/3) = (−1 + i√3)/2 : j³ = 1, j² = j̄ = 1/j et 1 + j + j² = 0.
:::

::: verifie À toi : les racines cubiques de −27
Donner les racines cubiques de −27 sous forme exponentielle puis algébrique.

---

On écrit −27 = 27 e^(iπ), de module 27 dont la racine cubique est 3, et les arguments sont (π + 2kπ)/3 : π/3, π et 5π/3. Les racines sont donc 3 e^(iπ/3) = (3 + 3i√3)/2, 3 e^(iπ) = −3 et 3 e^(i5π/3) = (3 − 3i√3)/2. Contrôle : (−3)³ = −27 ✓.
:::

::: retenir
zⁿ = r e^(iθ) a exactement n solutions ⁿ√r e^(i(θ + 2kπ)/n), k = 0, …, n − 1 : les sommets d'un polygone régulier inscrit dans le cercle de rayon ⁿ√r.
:::

## 🧩 Degré 3, 4 ou 6 : se ramener au second degré

Aucune formule simple ne résout z³ − 3z² + (3 + i)z − 2 − 2i = 0. L'énoncé annonce une solution imaginaire pure.
Comment la trouver, puis comment descendre au second degré que l'on sait résoudre ?

::: exemple Un degré 3 avec une racine imaginaire pure

1. On pose z = iy avec y réel : z³ = −iy³, −3z² = 3y² et (3 + i)z = 3iy − y. L'équation devient (3y² − y − 2) + i(−y³ + 3y − 2) = 0.
2. Il faut deux annulations à la fois. Partie réelle : 3y² − y − 2 = 0 donne y = 1 ou y = −2/3. Partie imaginaire : pour y = 1, −1 + 3 − 2 = 0 ✓, tandis que pour y = −2/3 elle ne s'annule pas. Donc z₀ = i.
3. On factorise : z³ − 3z² + (3 + i)z − 2 − 2i = (z − i)(z² + βz + γ). Le développement donne z³ + (β − i)z² + (γ − iβ)z − iγ. En identifiant, β − i = −3 donne β = −3 + i, puis γ − iβ = 3 + i donne γ = 2 − 2i ; contrôle sur le terme constant : −iγ = −2i + 2i² = −2 − 2i ✓.
4. Reste z² + (−3 + i)z + 2 − 2i = 0. Δ = (−3 + i)² − 4(2 − 2i) = 8 − 6i − 8 + 8i = 2i, de racine carrée 1 + i, donc z = (3 − i ± (1 + i))/2 : z = 2 ou z = 1 − i. Les solutions sont i, 2 et 1 − i. Contrôle : leur somme vaut i + 2 + (1 − i) = 3, l'opposé du coefficient −3 de z² ✓.

:::

::: exemple Un degré 4 par changement d'inconnue : z⁴ − 8iz² − 25 = 0

1. On pose Z = z², ce qui donne Z² − 8iZ − 25 = 0. Le discriminant réduit est Δ′ = (−4i)² + 25 = 9, de racine carrée 3.
2. Alors Z = 4i ± 3 : Z′ = 3 + 4i et Z″ = −3 + 4i.
3. On revient à z. Pour z² = 3 + 4i, le système donne x² − y² = 3 et x² + y² = 5, d'où x² = 4, y² = 1 et xy > 0 : z = ±(2 + i). Pour z² = −3 + 4i, x² − y² = −3 et x² + y² = 5, d'où x² = 1, y² = 4 et xy > 0 : z = ±(1 + 2i).
4. L'équation a quatre solutions : 2 + i, −2 − i, 1 + 2i et −1 − 2i. Contrôle : (1 + 2i)² = −3 + 4i, puis (−3 + 4i)² − 8i(−3 + 4i) − 25 = −7 − 24i + 32 + 24i − 25 = 0 ✓.

:::

::: piege
**Erreur : s'arrêter à Z = 3 + 4i et Z = −3 + 4i.** L'erreur tente parce que l'équation en Z est résolue et a l'air terminée. Mais Z n'est qu'un intermédiaire : l'inconnue du problème est z, avec z² = Z, et chaque valeur de Z donne deux valeurs de z. L'équation de degré 4 a donc quatre solutions, pas deux.
:::

::: methode Ramener une équation au second degré
Pour une équation de degré 3 ou plus :

1. Chercher une racine z₀ : un entier simple, ou une racine imaginaire pure z = iy en séparant parties réelle et imaginaire (deux équations en y qui doivent avoir une solution commune).
2. Factoriser par identification : P(z) = (z − z₀)(z² + βz + γ), puis résoudre le second degré.
3. Si l'équation ne contient que des puissances de z² (ou de z³), poser Z = z² (ou Z = z³) : z⁴ + pz² + q = 0 et z⁶ + pz³ + q = 0 deviennent Z² + pZ + q = 0. Après avoir résolu en Z, revenir à z avec les racines carrées (ou nièmes).

Cas limite : une racine peut être double. Si P(z₀) = 0 et que le facteur du second degré s'annule aussi en z₀, la solution z₀ compte deux fois.
:::

::: verifie À toi : factoriser avec une racine donnée
Résoudre z³ − (2 + i)z² + (1 + 2i)z − i = 0, sachant que 1 est solution.

---

On écrit P(z) = (z − 1)(z² + βz + γ) = z³ + (β − 1)z² + (γ − β)z − γ. En identifiant, β − 1 = −(2 + i) donne β = −1 − i, puis γ − β = 1 + 2i donne γ = i, et le terme constant −γ = −i convient ✓. Reste z² − (1 + i)z + i = 0 : Δ = (1 + i)² − 4i = −2i, de racine carrée 1 − i, donc z = ((1 + i) ± (1 − i))/2, soit z = 1 ou z = i. Les solutions sont 1 (double) et i.
:::

::: retenir
On devine une racine (réelle, ou imaginaire pure z = iy) puis on factorise par identification ; pour z⁴ ou z⁶, on pose Z = z² ou Z = z³, on résout en Z, puis on revient à z.
:::

## 🎯 Équations avec un paramètre θ et lieu des points

Pour chaque valeur de θ, l'équation (E_θ) : z² − 2 e^(iθ) z + e^(2iθ) + 1 = 0 a deux solutions, donc deux points du plan. Quand θ varie dans ]0 ; π/2[, ces points bougent.
Que décrivent-ils, et que dire du triangle qu'ils forment avec l'origine ?

::: figure Pour θ = π/3 (valeur d'illustration) : M₁ et M₂ sont sur les cercles de centres I(i) et J(−i) et de rayon 1, et l'angle en O est droit
<svg viewBox="0 0 300 300">
<title>Pour θ = π/3 : les points M₁ et M₂ d'affixes e^(iθ) + i et e^(iθ) − i, sur les cercles de centres I(i) et J(−i) et de rayon 1, avec l'angle droit en O</title>
<path d="M15 150 H225" fill="none" stroke="#0f172a" stroke-width="1.6"/>
<path d="M105 288 V12" fill="none" stroke="#0f172a" stroke-width="1.6"/>
<path d="M225 150 l-8 -4 l0 8 z" fill="#0f172a"/>
<path d="M105 12 l-4 8 l8 0 z" fill="#0f172a"/>
<path d="M165 147 V153" stroke="#0f172a" stroke-width="1.2"/>
<text x="165" y="166" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">1</text>
<path d="M102 90 H108" stroke="#0f172a" stroke-width="1.2"/>
<text x="98" y="94" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">i</text>
<path d="M102 30 H108" stroke="#0f172a" stroke-width="1.2"/>
<text x="98" y="34" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">2i</text>
<path d="M102 210 H108" stroke="#0f172a" stroke-width="1.2"/>
<text x="98" y="214" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">−i</text>
<path d="M102 270 H108" stroke="#0f172a" stroke-width="1.2"/>
<text x="98" y="274" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">−2i</text>
<text x="99" y="165" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">O</text>
<circle cx="105" cy="90" r="60" fill="none" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="5 4"/>
<circle cx="105" cy="210" r="60" fill="none" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="5 4"/>
<path d="M135 158 L135 38" fill="none" stroke="#0f6e56" stroke-width="2.4"/>
<path d="M105 150 L135 38" fill="none" stroke="#b45309" stroke-width="2.2"/>
<path d="M105 150 L135 158" fill="none" stroke="#b45309" stroke-width="2.2"/>
<path d="M108.6 136.5 L122.1 140.1 L118.5 153.6" fill="none" stroke="#b45309" stroke-width="1.6"/>
<circle cx="135" cy="38" r="4" fill="#0f172a"/>
<circle cx="135" cy="158" r="4" fill="#0f172a"/>
<circle cx="135" cy="98" r="3.5" fill="#0f6e56"/>
<circle cx="105" cy="90" r="3" fill="#94a3b8"/>
<circle cx="105" cy="210" r="3" fill="#94a3b8"/>
<text x="144" y="35" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">M₁</text>
<text x="145" y="180" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">M₂</text>
<text x="144" y="102" text-anchor="start" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">P</text>
<text x="113" y="94" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">I</text>
<text x="113" y="214" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">J</text>
</svg>
:::

Sur la figure, P a pour affixe e^(iθ), M₁ et M₂ sont P translaté de +i et de −i, et c'est cette translation qui fait de I(i) et J(−i) les centres des cercles décrits.

::: exemple Résoudre (E_θ) puis lire le lieu, pour θ ∈ ]0 ; π/2[

1. Ici b = −2 e^(iθ), donc b′ = −e^(iθ) et Δ′ = b′² − ac = e^(2iθ) − (e^(2iθ) + 1) = −1. Une racine carrée de −1 est i, donc z₁ = e^(iθ) + i et z₂ = e^(iθ) − i.
2. On isole e^(iθ) : z₁ − i = e^(iθ), donc |z₁ − i| = 1. Le point M₁ est sur le cercle de centre I(i) et de rayon 1 ; de même |z₂ + i| = 1 place M₂ sur le cercle de centre J(−i) et de rayon 1.
3. Les affixes sont z₁ = cos θ + i(1 + sin θ) et z₂ = cos θ + i(sin θ − 1) ; avec cos θ > 0 et sin θ > 0, chacun ne décrit qu'un quart de cercle, sans ses extrémités.
4. Le quotient z₁/z₂ = z₁ × (e^(−iθ) + i)/|z₂|² a pour numérateur (e^(iθ) + i)(e^(−iθ) + i) = 1 + 2i cos θ − 1 = 2i cos θ et pour dénominateur |z₂|² = cos²θ + (sin θ − 1)² = 2 − 2 sin θ. Donc z₁/z₂ = i cos θ/(1 − sin θ) est un imaginaire pur non nul : (OM₁) ⟂ (OM₂), le triangle OM₁M₂ est rectangle en O.

:::

::: piege
**Erreur : conclure « |z₁| = 1, donc M₁ est sur le cercle trigonométrique ».** L'erreur tente parce que z₁ contient e^(iθ), qui est de module 1. Mais z₁ = e^(iθ) + i : c'est z₁ − i qui a pour module 1. Pour θ = π/3, |z₁|² = cos²θ + (1 + sin θ)² = 1/4 + (1 + √3/2)² = 2 + √3 ≈ 3,73, loin de 1.
:::

::: methode Lire le lieu d'un point qui dépend de θ

1. Résoudre l'équation en gardant θ comme une constante : le discriminant réduit se simplifie souvent en un nombre fixe.
2. Écrire la solution sous la forme z = c + r e^(iθ) avec c et r constants : alors |z − c| = r, et M décrit le cercle de centre C(c) et de rayon r.
3. Borner θ pour dire si M décrit le cercle entier, un demi-cercle ou un arc, extrémités comprises ou non.
4. Pour un angle droit ou la nature d'un quadrilatère, former le quotient de deux différences d'affixes : réel pour l'alignement, imaginaire pur pour l'orthogonalité.

:::

::: verifie À toi : un autre lieu
Pour θ ∈ ]0 ; π[, on considère z² − 2 e^(iθ) z + e^(2iθ) + 4 = 0. Quel ensemble décrit le point M₁ dont l'affixe est la solution de plus grande partie imaginaire ?

---

Δ′ = e^(2iθ) − (e^(2iθ) + 4) = −4, de racine carrée 2i, donc z = e^(iθ) ± 2i. La solution de plus grande partie imaginaire est z₁ = e^(iθ) + 2i, et z₁ − 2i = e^(iθ) donne |z₁ − 2i| = 1 : M₁ est sur le cercle de centre d'affixe 2i et de rayon 1. Comme Im(z₁) = 2 + sin θ > 2 pour θ ∈ ]0 ; π[, il décrit le demi-cercle supérieur, sans ses extrémités.
:::

::: retenir
On résout avec θ constant, on écrit z = c + r e^(iθ) pour lire |z − c| = r, on borne θ pour savoir quelle partie du cercle est décrite, et l'on prouve un angle droit par un quotient imaginaire pur.
:::

> 🏆 Les huit portes sont franchies : tu extrais des racines carrées, tu résous le second degré dans ℂ, tu relies somme, produit et conjugaison, tu places les racines nièmes sur un polygone régulier et tu ramènes les degrés supérieurs au second. Prochaine étape : les droites et les plans de l'espace.
