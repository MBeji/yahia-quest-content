# ⚔️ Isométries du plan — les transformations qui ne déforment rien

> 💡 «Une figure qu'on déplace reste la même figure. Tout le chapitre tient dans cette évidence — et dans la liste, étonnamment courte, des applications qui la respectent.»

L'_Encyclopédie méthodique_ de D'Alembert et Diderot consacrait déjà un article aux « figures isométriques », et rappelait que Jacques Bernoulli fut « le premier qui l'ait traité avec exactitude », avant qu'Euler n'en tire « plusieurs morceaux très profonds ». Toi, tu connais déjà les acteurs : depuis le collège tu manipules **translations**, **symétries orthogonales**, **symétries centrales** et **rotations**. Ce chapitre change de point de vue. Au lieu de les étudier une par une, on part d'une **unique propriété** — conserver les distances — et on démontre qu'il n'existe presque rien d'autre. Dans tout le chapitre, le plan est **orienté dans le sens direct** (p.36).

## 🏰 La définition : conserver les distances

Prends une feuille calque, décalque un triangle, puis glisse le calque, retourne-le, fais-le tourner. Les longueurs dessinées n'ont pas bougé d'un millimètre. C'est exactement ce que formalise la définition.

> **Définition** (p.36) — « Une application du plan dans lui-même est une isométrie si elle conserve les distances. C'est-à-dire, si M′N′ = MN pour tous points M et N du plan d'images respectives M′ et N′. »

Le mot **application** compte : à tout point M du plan, f associe **un** point M′ = f(M). On dit que f **fixe** un point M₀ (ou que M₀ est **invariant**) lorsque f(M₀) = M₀.

::: figure Le triangle MNP et son image M′N′P′ par une rotation de centre I : la figure a bougé, mais aucune longueur n'a changé — MN = M′N′, NP = N′P′, PM = P′M′.
<svg viewBox="0 0 340 260"><path d="M55 150 L105 105 L120 180 Z" fill="#0f6e56" opacity="0.12"/><path d="M55 150 L105 105 L120 180 Z" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><path d="M240 95 L285 145 L210 160 Z" fill="#0f6e56" opacity="0.12"/><path d="M240 95 L285 145 L210 160 Z" fill="none" stroke="#0f6e56" stroke-width="2" stroke-linejoin="round"/><g stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="5 4" fill="none"><path d="M175 215 L55 150"/><path d="M175 215 L240 95"/></g><g fill="#0f172a"><circle cx="55" cy="150" r="4"/><circle cx="105" cy="105" r="4"/><circle cx="120" cy="180" r="4"/><circle cx="175" cy="215" r="3.5"/></g><g fill="#0f6e56"><circle cx="240" cy="95" r="4"/><circle cx="285" cy="145" r="4"/><circle cx="210" cy="160" r="4"/></g><g font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="42" y="146" text-anchor="middle" fill="#0f172a">M</text><text x="103" y="94" text-anchor="middle" fill="#0f172a">N</text><text x="118" y="199" text-anchor="middle" fill="#0f172a">P</text><text x="242" y="84" text-anchor="middle" fill="#0f6e56">M′</text><text x="299" y="150" text-anchor="middle" fill="#0f6e56">N′</text><text x="197" y="172" text-anchor="middle" fill="#0f6e56">P′</text><text x="175" y="234" text-anchor="middle" fill="#0f172a">I</text></g></svg>
:::

_Exemple détaillé (une symétrie orthogonale est une isométrie)_ — plaçons l'axe Δ sur l'axe des abscisses d'un repère orthonormé (O, i⃗, j⃗). Alors S_Δ envoie M(x, y) sur M′(x, −y) et N(x₁, y₁) sur N′(x₁, −y₁). Donc :

$$ M′N′² = (x₁ − x)² + (−y₁ + y)² = (x₁ − x)² + (y₁ − y)² = MN² $$

Les distances étant positives, M′N′ = MN ✓. _Contrôle chiffré_ : M(1, 2) et N(4, 6) donnent MN = 5 ; leurs images M′(1, −2) et N′(4, −6) donnent M′N′ = √(9 + 16) = 5 ✓.

> **Conséquences** (p.37) — « • L'identité du plan, les translations, les symétries orthogonales et les rotations sont des isométries. • Les images de deux points distincts du plan par une isométrie sont deux points distincts. »

Le second point est immédiat : si M ≠ N alors MN > 0, donc M′N′ = MN > 0 et M′ ≠ N′. Une isométrie est donc toujours **injective**.

_Exemple détaillé (test express par les complexes)_ — l'application g qui à M d'affixe z associe M′ d'affixe z′ = ((−1 + i√3)/2)·z est-elle une isométrie ? Posons a = (−1 + i√3)/2. Alors |a| = √(1/4 + 3/4) = 1, et pour deux points d'affixes z et z₁ : |z′₁ − z′| = |a(z₁ − z)| = |a|·|z₁ − z| = |z₁ − z|. Donc **g est une isométrie** ✓. _Contrôle numérique_ : M(2, 0) a pour image l'affixe 2a = −1 + i√3, soit M′(−1 ; 1,732) ; N(0, 1) a pour image i·a = (−√3 − i)/2, soit N′(−0,866 ; −0,5). On calcule MN = √(4 + 1) = √5 ≈ 2,236 et M′N′ = √(0,134² + 2,232²) = √5,000 ≈ 2,236 ✓.

> ⚠️ **Conserver les distances, ce n'est pas conserver les coordonnées.** Une isométrie a le droit de tout déplacer : la seule chose interdite est de rapprocher ou d'éloigner deux points l'un de l'autre.

## ⚡ Le produit scalaire, les angles et les configurations

Comment démontrer qu'une isométrie conserve les **angles**, alors que la définition ne parle que de longueurs ? Par le produit scalaire, qui relie les deux : AB⃗·AC⃗ = ½(AB² + AC² − BC²) — une expression **uniquement** faite de distances.

> **Théorème** (p.37) — « Une application du plan dans lui-même est une isométrie, si et seulement si, elle conserve le produit scalaire. Une application f est une isométrie, si et seulement si, AB⃗·AC⃗ = A′B′⃗·A′C′⃗ pour tous points A, B et C d'images respectives A′, B′ et C′. »

> **Corollaire** (p.37) — « Soit f une isométrie du plan. Si A, B et C sont trois points deux à deux distincts, d'images respectives A′, B′ et C′, alors BAC^ = B′A′C′^. On dit qu'une isométrie conserve les mesures des angles géométriques. »

> **Conséquence** (p.38) — « Les images par une isométrie de trois points non alignés sont trois points non alignés. »

_Exemple détaillé (l'angle droit survit)_ — soit f définie par x′ = (√2/2)(x − y) et y′ = (√2/2)(x + y). Prenons A(0, 0), B(2, 0), C(0, 3) : l'angle BAC^ est droit. Les images sont A′(0, 0), B′(√2, √2) et C′(−3√2/2 ; 3√2/2). Alors :

$$ A′B′⃗·A′C′⃗ = √2 × (−3√2/2) + √2 × (3√2/2) = −3 + 3 = 0 $$

L'angle A′ est droit lui aussi ✓. _Contrôle_ : AB = 2 et A′B′ = √(2 + 2) = 2 ✓ ; AC = 3 et A′C′ = √(4,5 + 4,5) = 3 ✓.

Une isométrie transporte donc tout le **repérage** d'une figure, pas seulement ses longueurs.

> **Théorème** (p.38) — « Soit f une isométrie, A, B et C trois points non alignés du plan et A′, B′ et C′ leurs images respectives. Si le repère (A, AB⃗, AC⃗) est orthonormé alors le repère (A′, A′B′⃗, A′C′⃗) est orthonormé. De plus, pour tout point M d'image M′, AM⃗ = x·AB⃗ + y·AC⃗ avec x et y réels, implique que A′M′⃗ = x·A′B′⃗ + y·A′C′⃗. »

> **Théorème** (p.39) — « Soit f une isométrie et A, B, C et D des points d'images respectives A′, B′, C′ et D′ par f. Si AB⃗ = α·CD⃗ alors A′B′⃗ = α·C′D′⃗, où α est un réel. »

Autrement dit : **les coordonnées d'un point ne changent pas** quand on lit la figure dans son propre repère. Toutes les configurations usuelles suivent.

> **(Action sur les configurations usuelles)** (p.39) — « • Une isométrie conserve le barycentre de deux points. En particulier une isométrie conserve le milieu d'un segment. • L'image d'une droite par une isométrie est une droite. • L'image d'un segment par une isométrie est un segment qui lui est isométrique. • Les images de deux droites parallèles par une isométrie sont deux droites parallèles (on dit qu'une isométrie conserve le parallélisme). • L'image d'un parallélogramme par une isométrie est un parallélogramme. • Les images de deux droites perpendiculaires par une isométrie sont deux droites perpendiculaires (on dit qu'une isométrie conserve l'orthogonalité). • L'image d'un cercle par une isométrie est un cercle qui lui est isométrique. • L'image par une isométrie de la tangente en un point M à un cercle est la tangente au cercle image, au point M′ image de M (on dit qu'une isométrie conserve le contact). »

_Exemple détaillé (le milieu suit)_ — soit r la rotation de centre O et d'angle π/2, qui envoie M(x, y) sur M′(−y, x). Prenons A(2, 0) et B(0, 4), de milieu I(1, 2). Alors A′(0, 2), B′(−4, 0), et le milieu de [A′B′] est ((0 − 4)/2 ; (2 + 0)/2) = (−2 ; 1). Or r(I) = r(1, 2) = (−2, 1) : **c'est le même point** ✓.

> 🗡️ **La méthode qui résout la moitié des exercices** : pour montrer qu'une figure image est un carré, un rectangle, un losange, ne recalcule rien. Écris la propriété caractéristique de la figure de départ (longueurs égales, côtés parallèles, angle droit) et dis que l'isométrie la transporte. C'est tout.

## 🛡️ Bijectivité et isométrie réciproque

Une isométrie est injective (deux points distincts ont des images distinctes). Est-elle **surjective** ? Oui, et c'est le théorème qui autorise à « revenir en arrière ».

> **Théorème et définition** (p.39) — « Une isométrie f est une bijection du plan dans lui-même. L'application du plan dans lui-même qui à tout point N du plan associe son unique antécédent M par f est une isométrie appelée réciproque de f et notée f⁻¹. »

L'idée de la démonstration : on fixe trois points non alignés A, B, C avec (A, AB⃗, AC⃗) orthonormé. Le repère image (A′, A′B′⃗, A′C′⃗) est orthonormé lui aussi. Tout point N s'écrit alors A′N⃗ = x·A′B′⃗ + y·A′C′⃗, et le **seul** antécédent possible est le point M de coordonnées (x, y) dans le repère de départ.

> **(Conséquences)** (p.39) — « Pour toute isométrie f et tout point M, f(M) = N, si et seulement si, f⁻¹(N) = M. La réciproque d'une symétrie orthogonale est elle-même. La réciproque d'une symétrie centrale est elle-même. La réciproque d'une translation de vecteur u⃗ est la translation de vecteur −u⃗. La réciproque d'une rotation de centre I et d'angle α est la rotation de centre I et d'angle −α. »

| isométrie f              | réciproque f⁻¹                    |
| ------------------------ | --------------------------------- |
| identité Id              | Id                                |
| symétrie orthogonale S_D | S_D (elle-même)                   |
| symétrie centrale S_I    | S_I (elle-même)                   |
| translation t_u⃗          | t_(−u⃗)                            |
| rotation de centre I, angle α | rotation de centre I, angle −α |

_Exemple détaillé_ — vérifions que S_D est sa propre réciproque sur Δ = axe des abscisses : S_Δ(x, y) = (x, −y), puis S_Δ(x, −y) = (x, y). On retrouve le point de départ, donc S_Δ∘S_Δ = Id ✓ et S_Δ⁻¹ = S_Δ. En revanche t_u⃗∘t_u⃗ = t_(2u⃗) ≠ Id dès que u⃗ ≠ 0⃗ : une translation n'est **pas** sa propre réciproque.

> ⚠️ Seules les symétries (orthogonales et centrales) sont **involutives**, c'est-à-dire égales à leur réciproque. Écrire r∘r = Id pour une rotation r d'angle α est faux : r∘r est la rotation d'angle 2α, et elle ne vaut Id que si 2α ≡ 0 [2π].

## 🔮 Composer deux isométries

Enchaîner deux transformations, c'est composer. Si M′ = f(M) et M″ = g(M′), alors M″ = (g∘f)(M).

> **Théorème** (p.40) — « La composée de deux isométries est une isométrie. »

La preuve tient en une ligne de distances : M′N′ = MN (car f est une isométrie), puis M″N″ = M′N′ (car g en est une), donc M″N″ = MN ✓. La composition est **associative** : (g∘f)∘h = g∘(f∘h), mais elle n'est **pas commutative** en général.

> **Théorème** (p.42) — « Soit f et g deux isométries. g = f⁻¹, si et seulement si, f∘g = Id, où Id désigne l'identité du plan. »

> **Propriété** (p.42) — « Si f et g sont deux isométries, alors (f∘g)⁻¹ = g⁻¹∘f⁻¹. »

> **Propriété** (p.42) — « Soit f, g et h trois isométries. f = g, si et seulement si, h∘f = h∘g. »

_Exemple détaillé (réciproques)_ — soit A, B, C trois points non alignés. La réciproque de S_(AB)∘S_(AC) est (S_(AB)∘S_(AC))⁻¹ = S_(AC)⁻¹∘S_(AB)⁻¹ = **S_(AC)∘S_(AB)** — les deux facteurs s'échangent. De même, la réciproque de t_(AB⃗)∘S_(AC)∘t_(−BC⃗) est t_(BC⃗)∘S_(AC)∘t_(−AB⃗). _Contrôle_ : on remonte la chaîne **à l'envers**, en remplaçant chaque facteur par sa réciproque ✓.

Le cœur du chapitre est le cas où les deux facteurs sont des **symétries orthogonales**.

> **Théorème** (p.41, axes sécants) — « La composée de deux symétries orthogonales d'axes sécants est une rotation. Plus précisément, si D et D′ sont deux droites sécantes en un point I et de vecteurs directeurs respectifs u⃗ et u′⃗ et si S_D et S_D′ sont les symétries orthogonales d'axes respectifs D et D′, alors S_D′∘S_D est la rotation de centre I et d'angle α où α ≡ 2(u⃗, u′⃗) [2π]. »

::: figure Les deux symétries laissent M à la même distance de I : IM = IM′ = IM″. Le point ne s'éloigne pas, il tourne — et il tourne du double de l'angle formé par les deux axes.
<svg viewBox="0 0 340 260"><path d="M30 140 H310" fill="none" stroke="#0f172a" stroke-width="2"/><path d="M55.3 220.3 L284.7 59.7" fill="none" stroke="#0f172a" stroke-width="2"/><g stroke="#0f6e56" stroke-width="1.8" fill="none"><path d="M170 140 L99.3 210.7"/><path d="M170 140 L99.3 69.3"/><path d="M170 140 L212.3 230.6"/></g><g stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="5 4" fill="none"><path d="M99.3 210.7 L99.3 69.3"/><path d="M99.3 69.3 L212.3 230.6"/></g><g fill="#0f172a"><circle cx="170" cy="140" r="4"/></g><g fill="#0f6e56"><circle cx="99.3" cy="210.7" r="4"/><circle cx="99.3" cy="69.3" r="4"/><circle cx="212.3" cy="230.6" r="4"/></g><g font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="163" y="131" text-anchor="middle" fill="#0f172a">I</text><text x="87" y="224" text-anchor="middle" fill="#0f6e56">M</text><text x="86" y="62" text-anchor="middle" fill="#0f6e56">M′</text><text x="226" y="244" text-anchor="middle" fill="#0f6e56">M″</text><text x="302" y="134" text-anchor="middle" fill="#0f172a">D</text><text x="300" y="52" text-anchor="middle" fill="#0f172a">D′</text></g></svg>
:::

_Exemple détaillé_ — dans un repère orthonormé, prenons D = (Ox) de vecteur directeur u⃗ = i⃗, et D′ la droite passant par O de vecteur directeur u′⃗ tel que (u⃗, u′⃗) = π/6. Alors S_D′∘S_D doit être la rotation de centre O et d'angle 2 × π/6 = **π/3**. Vérifions sur deux points.

- M(1, 0) : M ∈ D donc S_D(M) = M ; puis la symétrie d'axe D′ envoie (1, 0) sur (cos(π/3) ; sin(π/3)) = (1/2 ; √3/2). Or la rotation d'angle π/3 envoie (1, 0) sur (cos(π/3) ; sin(π/3)) ✓.
- N(0, 1) : S_D(N) = (0, −1) ; puis S_D′(0, −1) = (−√3/2 ; 1/2). Or la rotation d'angle π/3 envoie (0, 1) sur (−sin(π/3) ; cos(π/3)) = (−√3/2 ; 1/2) ✓.

_Contrôle de l'ordre_ — S_D∘S_D′ envoie M(1, 0) sur (1/2 ; −√3/2) : c'est la rotation d'angle **−π/3**. Composer dans l'autre sens change le signe de l'angle.

> **Conséquence** (p.41, axes perpendiculaires) — « La composée de deux symétries orthogonales d'axes perpendiculaires D et D′ en I est la symétrie centrale de centre I, et dans ce cas S_D∘S_D′ = S_D′∘S_D. »

_Exemple détaillé_ — D = (Ox) et D′ = (Oy), donc I = O. Pour M(3, 2) : S_D(M) = (3, −2), puis S_D′(3, −2) = (−3, −2) = S_O(M) ✓. Et dans l'autre ordre : S_D′(3, 2) = (−3, 2), puis S_D(−3, 2) = (−3, −2) : **le même point** ✓. C'est bien le seul cas où deux symétries orthogonales distinctes commutent, car l'angle 2 × (π/2) = π est son propre opposé modulo 2π.

> **Théorème** (p.41, axes parallèles) — « La composée de deux symétries orthogonales d'axes parallèles est une translation. Plus précisément, si D et D′ sont deux droites parallèles et si S_D et S_D′ sont les symétries orthogonales d'axes respectifs D et D′, alors S_D′∘S_D est la translation de vecteur 2IJ⃗, où I est un point de D et J est le projeté orthogonal de I sur D′. »

::: figure Le point traverse deux fois : il ressort sur la même perpendiculaire aux axes, décalé d'exactement le double de l'écart entre les deux droites.
<svg viewBox="0 0 340 260"><path d="M120 30 V240" fill="none" stroke="#0f172a" stroke-width="2"/><path d="M200 30 V240" fill="none" stroke="#0f172a" stroke-width="2"/><path d="M120 205 H200" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-dasharray="5 4"/><path d="M70 80 H230" fill="none" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="5 4"/><path d="M70 100 H220" fill="none" stroke="#0f6e56" stroke-width="2.4"/><path d="M219 94 L230 100 L219 106 Z" fill="#0f6e56"/><g fill="#0f6e56"><circle cx="70" cy="80" r="4"/><circle cx="170" cy="80" r="4"/><circle cx="230" cy="80" r="4"/></g><g fill="#0f172a"><circle cx="120" cy="205" r="4"/><circle cx="200" cy="205" r="4"/></g><g font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="66" y="68" text-anchor="middle" fill="#0f6e56">M</text><text x="170" y="68" text-anchor="middle" fill="#0f6e56">M′</text><text x="234" y="68" text-anchor="middle" fill="#0f6e56">M″</text><text x="113" y="222" text-anchor="middle" fill="#0f172a">I</text><text x="207" y="222" text-anchor="middle" fill="#0f172a">J</text><text x="120" y="24" text-anchor="middle" fill="#0f172a">D</text><text x="200" y="24" text-anchor="middle" fill="#0f172a">D′</text></g></svg>
:::

_Exemple détaillé_ — D : y = 0 et D′ : y = 3, avec I = O(0, 0) et J(0, 3), donc IJ⃗ = (0 ; 3) et 2IJ⃗ = (0 ; 6). Pour M(1, 2) : S_D(M) = (1, −2), puis S_D′(1, −2) = (1 ; 6 − (−2)) = (1, 8). Et t_(2IJ⃗)(M) = (1 ; 2 + 6) = (1, 8) ✓. _Contrôle de l'ordre_ : S_D∘S_D′ donne (1, 2) → (1, 4) → (1, −4), soit la translation de vecteur (0 ; −6) = 2JI⃗ ✓.

> ⚠️ **L'ordre n'est jamais neutre** (sauf axes perpendiculaires). S_D′∘S_D et S_D∘S_D′ sont **réciproques** l'une de l'autre : même centre et angle opposé pour des axes sécants, vecteurs opposés pour des axes parallèles.

## 🧮 Les points fixes : la carte d'identité d'une isométrie

Voici l'idée maîtresse du chapitre : **on reconnaît une isométrie au nombre de points qu'elle laisse en place.** Le point de départ est un raisonnement de distances.

> **Théorème** (p.43) — « Soit f une isométrie différente de l'identité, A un point non fixe de f et A′ son image. Alors les points fixes de f, s'ils existent, se trouvent sur la médiatrice du segment [AA′]. »

En effet, si f(M) = M alors MA′ = f(M)f(A) = MA : M est équidistant de A et A′.

::: figure Un point fixe M vérifie MA = MA′ : il ne peut vivre que sur la médiatrice de [AA′] — toute la recherche des points fixes se joue là.
<svg viewBox="0 0 340 260"><path d="M80 70 L240 150" fill="none" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="5 4"/><path d="M204.7 20.6 L115.3 199.4" fill="none" stroke="#0f172a" stroke-width="2"/><path d="M170.7 115.4 L165.4 126.1 L154.6 120.7" fill="none" stroke="#0f172a" stroke-width="1.6"/><g stroke="#0f6e56" stroke-width="2" fill="none"><path d="M124.2 181.6 L80 70"/><path d="M124.2 181.6 L240 150"/></g><g fill="#0f172a"><circle cx="80" cy="70" r="4"/><circle cx="240" cy="150" r="4"/><circle cx="160" cy="110" r="3.5"/><circle cx="124.2" cy="181.6" r="4"/></g><g font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="70" y="60" text-anchor="middle" fill="#0f172a">A</text><text x="253" y="146" text-anchor="middle" fill="#0f172a">A′</text><text x="112" y="196" text-anchor="middle" fill="#0f6e56">M</text><text x="214" y="18" text-anchor="middle" fill="#0f172a">Δ</text></g></svg>
:::

De là découle toute la classification.

> **Théorème** (p.43) — « Une isométrie fixe trois points non alignés, si et seulement si, c'est l'identité du plan. »

> **Conséquence** (p.44) — « Si deux isométries f et g coïncident sur trois points non alignés, alors elles coïncident partout dans le plan. On dit qu'une isométrie est déterminée par la donnée de trois points non alignés et leurs images. »

> **Théorème** (p.44) — « Si une isométrie fixe deux points distincts A et B, alors elle fixe tous les points de la droite (AB). »

> **Théorème** (p.44) — « Si une isométrie f fixe deux points distincts A et B et si elle est différente de l'identité, alors f est la symétrie orthogonale d'axe (AB). »

> **Théorème** (p.44) — « Si une isométrie f fixe un unique point I alors f est une rotation de centre I et d'angle non nul. »

_Exemple détaillé (identifier par les images de trois points)_ — soit ABCD un carré direct, S la symétrie orthogonale d'axe la médiatrice de [BC] et T la translation de vecteur BC⃗. Plaçons A(0, 0), B(1, 0), C(1, 1), D(0, 1) : la médiatrice de [BC] est la droite y = 1/2 et BC⃗ = (0 ; 1). Donc S(x, y) = (x ; 1 − y) et T(x, y) = (x ; y + 1).

- **S∘T** (on applique T, puis S) : (x, y) ↦ (x ; y + 1) ↦ (x ; 1 − (y + 1)) = (x ; −y). Les images sont A ↦ A, B ↦ B et D(0, 1) ↦ (0, −1) ≠ D. L'isométrie fixe deux points distincts sans être l'identité : c'est **S_(AB)** ✓.
- **T∘S** : (x, y) ↦ (x ; 1 − y) ↦ (x ; 2 − y). Elle fixe C(1, 1) et D(0, 1), et envoie A(0, 0) sur (0, 2) : c'est **S_(DC)** ✓.
- **S∘T∘T∘S** = S_(AB)∘S_(DC) : deux axes **parallèles**, donc une translation. Avec I(0, 1) ∈ (DC) et son projeté J(0, 0) sur (AB), le vecteur vaut 2IJ⃗ = (0 ; −2) = 2DA⃗. _Contrôle direct_ : (x, y) ↦ (x ; 2 − y) ↦ (x ; −(2 − y)) = (x ; y − 2) ✓.

Reste le cas des isométries qui ne fixent **rien**.

> **Théorème** (p.45) — « Soit O un point du plan. Alors toute isométrie f se décompose de manière unique en la composée d'une translation et d'une isométrie g qui fixe O. »

> **Théorème** (p.46) — « Une isométrie qui n'a aucun point fixe est soit une translation de vecteur non nul, soit la composée d'une translation de vecteur non nul u⃗ et d'une symétrie orthogonale d'axe Δ tel que u⃗ est directeur de Δ. »

> **Définition** (p.47) — « La composée d'une translation de vecteur non nul u⃗ et d'une symétrie orthogonale d'axe Δ tel que u⃗ est directeur de Δ est appelée symétrie glissante. »

::: figure Une symétrie glissante fait alterner les points de part et d'autre de son axe, comme des empreintes de pas : aucun point ne reste en place, et deux applications successives donnent la translation t_(2u⃗).
<svg viewBox="0 0 340 260"><path d="M30 150 H320" fill="none" stroke="#0f172a" stroke-width="2"/><g stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="5 4" fill="none"><path d="M70 80 V220"/><path d="M180 220 V80"/></g><g stroke="#0f6e56" stroke-width="2.4" fill="none"><path d="M70 220 H170"/><path d="M180 80 H280"/></g><g fill="#0f6e56"><path d="M169 214 L180 220 L169 226 Z"/><path d="M279 74 L290 80 L279 86 Z"/></g><g fill="#0f172a"><circle cx="70" cy="80" r="4"/><circle cx="180" cy="220" r="4"/><circle cx="290" cy="80" r="4"/></g><g font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="62" y="70" text-anchor="middle" fill="#0f172a">M</text><text x="186" y="240" text-anchor="middle" fill="#0f172a">M′</text><text x="300" y="70" text-anchor="middle" fill="#0f172a">M″</text><text x="120" y="240" text-anchor="middle" fill="#0f6e56">u</text><text x="316" y="143" text-anchor="middle" fill="#0f172a">Δ</text></g></svg>
:::

_Exemple détaillé (une symétrie glissante n'a aucun point fixe)_ — prenons Δ = (Ox) et u⃗ = (3 ; 0), qui est bien directeur de Δ. Alors f = t_u⃗∘S_Δ envoie M(x, y) sur (x + 3 ; −y). Un point fixe exigerait −y = y, donc y = 0, **et** x + 3 = x, ce qui est impossible : f n'a **aucun** point fixe ✓. En revanche f∘f envoie M sur (x + 6 ; y) : c'est la translation t_(2u⃗). _Contrôle_ : M(1, 2) ↦ (4, −2) ↦ (7, 2) = M + (6 ; 0) ✓.

> ⚠️ Ne conclus pas trop vite « pas de point fixe ⟹ symétrie glissante » : la **translation de vecteur non nul** n'en a pas non plus. Le tri se fait ensuite : si f∘f = Id le candidat tombe, si f∘f est une translation non nulle il reste les deux cas, et c'est l'axe qui tranche.

## 📐 Décomposer toute isométrie en symétries orthogonales

Les symétries orthogonales sont les **briques** du plan : tout se construit avec elles, et jamais plus de trois.

> **Théorème** (p.47) — « Toute isométrie se décompose en au plus trois symétries orthogonales. »

> **Théorème** (p.48) — « Toute rotation est la composée de deux symétries orthogonales d'axes sécants. Plus précisément, soit r une rotation de centre I et d'angle θ et D une droite quelconque passant par I et de vecteur directeur u⃗. Alors r = S_D′∘S_D, où D′ est la droite passant par I et de vecteur directeur u′⃗ tel que 2(u⃗, u′⃗) ≡ θ [2π]. »

> **Conséquence** (p.48) — « Soit S_I la symétrie centrale de centre I et D une droite passant par I. Alors S_I = S_D′∘S_D = S_D∘S_D′, où D′ est la droite perpendiculaire à D en I. »

> **Théorème** (p.49) — « Toute translation est la composée de deux symétries orthogonales d'axes parallèles. Plus précisément, soit t_u⃗ la translation de vecteur non nul u⃗, D une droite quelconque de direction orthogonale à celle de u⃗ et H un point de D. Alors t_u⃗ = S_D′∘S_D, où D′ est la droite parallèle à D et passant par le point K tel que HK⃗ = ½ u⃗. »

Remarque essentielle : **la décomposition n'est pas unique**. On choisit **librement** le premier axe (pourvu qu'il passe par le centre pour une rotation, ou qu'il soit orthogonal à u⃗ pour une translation) ; le second est alors imposé. C'est ce degré de liberté qui permet de faire « télescoper » deux symétries dans un produit.

_Exemple détaillé (décomposer une rotation)_ — soit r la rotation de centre O et d'angle π/2. Choisissons D = (Ox), de vecteur directeur u⃗ = i⃗. Il faut u′⃗ avec 2(u⃗, u′⃗) ≡ π/2, donc (u⃗, u′⃗) = π/4 : D′ est la droite d'équation y = x. Vérifions r = S_D′∘S_D sur deux points.

- M(1, 0) : S_D(M) = (1, 0), puis la symétrie d'axe y = x échange les coordonnées : (0, 1). Et r(1, 0) = (0, 1) ✓.
- N(0, 1) : S_D(N) = (0, −1), puis S_D′(0, −1) = (−1, 0). Et r(0, 1) = (−1, 0) ✓.

Deux points non alignés avec le centre suffisent à conclure, puisqu'une isométrie est déterminée par trois points non alignés (ici O, M, N) ✓.

_Exemple détaillé (décomposer une translation)_ — soit t_u⃗ avec u⃗ = (4 ; 0). Prenons D : x = 0, orthogonale à u⃗, et H = O ; alors K vérifie HK⃗ = ½u⃗ = (2 ; 0), donc K(2, 0) et D′ : x = 2. Test sur M(1, 3) : S_D(M) = (−1, 3), puis S_D′(−1, 3) = (4 − (−1) ; 3) = (5, 3). Et M + u⃗ = (5, 3) ✓.

_Exemple détaillé (trois symétries qui se réduisent à une)_ — soit S₁ d'axe (Ox), S₂ d'axe y = x et S₃ d'axe (Oy) : les trois axes sont **concourants** en O. Calculons S₁∘S₂∘S₃ appliqué à M(x, y), de droite à gauche : S₃ donne (−x, y), puis S₂ échange les coordonnées et donne (y, −x), puis S₁ change le signe de l'ordonnée et donne (y, x). L'application finale est M(x, y) ↦ (y, x) : c'est la **symétrie orthogonale d'axe y = x** ✓. _Contrôle_ : M(3, 1) ↦ (−3, 1) ↦ (1, 3) ↦ (1, 3), et (1, 3) est bien le symétrique de (3, 1) par rapport à y = x ✓. Le résultat général (l'exercice résolu p.43) dit exactement cela : S₁∘S₂∘S₃ est une symétrie orthogonale **si et seulement si** D₁, D₂, D₃ sont parallèles ou concourantes.

Tout le chapitre se range dans un seul tableau.

> **Tableau de classification** (p.49)

| Nature de l'isométrie                              | Décomposition en symétries orthogonales                          | Ensemble des points fixes |
| -------------------------------------------------- | ---------------------------------------------------------------- | ------------------------- |
| Identité du plan                                   | S_D∘S_D                                                          | Tout le plan              |
| Symétrie orthogonale d'axe D                       | S_D                                                              | La droite D               |
| Rotation de centre I et d'angle θ, θ ≠ k2π ; k ∈ ℤ | S_D∘S_D′ (D ∩ D′ = {I})                                          | {I}                       |
| Translation de vecteur non nul                     | S_D∘S_D′ (D ∩ D′ = ∅)                                            | L'ensemble vide           |
| Symétrie glissante d'axe D et de vecteur u⃗         | S_D∘S_D′∘S_D″, (D ∩ D′ = ∅) et D perpendiculaire à D″            | L'ensemble vide           |

> 🗡️ **Lis le tableau dans les deux sens.** De gauche à droite, il donne la décomposition d'une isométrie connue. De droite à gauche — c'est le sens qui rapporte des points — il **identifie** une isométrie inconnue à partir de ses seuls points fixes : tout le plan, une droite, un point, ou rien.

## 🧪 Reconnaître une isométrie donnée par ses équations

À l'écrit, l'isométrie arrive rarement avec son nom. Elle arrive sous forme d'**équations analytiques** ou d'une **écriture complexe**. La méthode est toujours la même, en trois temps.

1. **Vérifier que c'est une isométrie** : montrer que M′N′ = MN (ou |z′₁ − z′₂| = |z₁ − z₂|).
2. **Chercher les points fixes** : résoudre f(M) = M.
3. **Conclure par le tableau de classification** selon l'ensemble obtenu.

_Exemple détaillé (équations analytiques)_ — soit f : x′ = (√2/2)x − (√2/2)y et y′ = (√2/2)x + (√2/2)y.

**Étape 1.** Posons a = x₁ − x et b = y₁ − y. Alors x′₁ − x′ = (√2/2)(a − b) et y′₁ − y′ = (√2/2)(a + b), donc :

$$ M′N′² = ½(a − b)² + ½(a + b)² = ½(a² − 2ab + b² + a² + 2ab + b²) = a² + b² = MN² $$

f est une isométrie ✓.

**Étape 2.** Un point fixe vérifie x = (√2/2)(x − y) et y = (√2/2)(x + y). La seconde équation donne x = (1 − √2/2)y/(√2/2) ; en reportant dans la première, on obtient (1 − √2/2)²y = −(√2/2)²y, soit ((1 − √2/2)² + ½)y = 0. Le coefficient vaut environ 0,0858 + 0,5 = 0,5858 ≠ 0, donc y = 0 puis x = 0 : **O est l'unique point fixe**.

**Étape 3.** Un unique point fixe ⟹ f est la **rotation de centre O et d'angle non nul**. L'angle se lit sur l'image de I(1, 0), qui est (√2/2 ; √2/2), d'argument π/4 : f est la rotation de centre O et d'angle **π/4** ✓. _Contrôle_ : M(2, 0) a pour image (√2 ; √2), à la distance √(2 + 2) = 2 de O, comme M ✓.

_Exemple détaillé (écriture complexe, cas z′ = az + b)_ — soit f : z′ = iz − 1 − i. Comme |i| = 1, on a |z′₁ − z′| = |i||z₁ − z| = |z₁ − z| : f est une isométrie ✓. Points fixes : z = iz − 1 − i ⟺ z(1 − i) = −1 − i ⟺ z = (−1 − i)/(1 − i). En multipliant haut et bas par 1 + i : z = (−1 − i)(1 + i)/2 = (−1 − i − i − i²)/2 = (−2i)/2 = **−i**. Point fixe unique Ω(0, −1), donc f est la rotation de centre Ω et d'angle arg(i) = **π/2** ✓. _Contrôle_ : M(1, 0) a pour image z′ = i − 1 − i = −1, soit M′(−1, 0). Le vecteur ΩM⃗ = (1 ; 1) devient ΩM′⃗ = (−1 ; 1) — c'est bien l'image de (1 ; 1) par la rotation d'angle π/2 ✓, et les deux longueurs valent √2.

_Exemple détaillé (écriture complexe, cas z′ = az̄ + b)_ — soit f : z′ = i·z̄. La conjugaison conserve les modules, donc |z′₁ − z′| = |i(z̄₁ − z̄)| = |z̄₁ − z̄| = |z₁ − z| : f est une isométrie ✓. En posant z = x + iy, on trouve z′ = i(x − iy) = y + ix, c'est-à-dire x′ = y et y′ = x. Les points fixes vérifient x = y : l'ensemble des points fixes est la **droite d'équation y = x**. D'après le tableau, f est la **symétrie orthogonale d'axe y = x** ✓.

::: figure Les points fixes de z ↦ i·z̄ dessinent exactement la droite y = x : c'est l'axe de la symétrie, et M(3, 1) a bien pour image M′(1, 3), symétrique par rapport à cette droite.
<svg viewBox="0 0 340 260"><g stroke="#94a3b8" stroke-width="1"><path d="M100 40 V215 M140 40 V215 M180 40 V215 M220 40 V215 M260 40 V215"/><path d="M60 175 H300 M60 135 H300 M60 95 H300 M60 55 H300"/></g><path d="M35 215 H315" fill="none" stroke="#0f172a" stroke-width="1.8"/><path d="M60 240 V28" fill="none" stroke="#0f172a" stroke-width="1.8"/><path d="M315 215 l-8 -4 l0 8 z" fill="#0f172a"/><path d="M60 28 l-4 8 l8 0 z" fill="#0f172a"/><path d="M60 215 L240 35" fill="none" stroke="#b45309" stroke-width="2.2"/><path d="M180 175 L100 95" fill="none" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="5 4"/><g fill="#0f6e56"><circle cx="180" cy="175" r="4.5"/><circle cx="100" cy="95" r="4.5"/></g><circle cx="140" cy="135" r="3.5" fill="#b45309"/><g font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="194" y="184" text-anchor="middle" fill="#0f6e56">M</text><text x="86" y="88" text-anchor="middle" fill="#0f6e56">M′</text><text x="50" y="232" text-anchor="middle" fill="#0f172a">O</text><text x="266" y="40" text-anchor="middle" fill="#b45309">y = x</text><text x="100" y="232" text-anchor="middle" fill="#0f172a">1</text><text x="140" y="232" text-anchor="middle" fill="#0f172a">2</text><text x="180" y="232" text-anchor="middle" fill="#0f172a">3</text><text x="48" y="180" text-anchor="middle" fill="#0f172a">1</text><text x="48" y="140" text-anchor="middle" fill="#0f172a">2</text><text x="48" y="100" text-anchor="middle" fill="#0f172a">3</text></g></svg>
:::

_Exemple_ — avec f : z′ = z̄ + 2, on obtient x′ = x + 2 et y′ = −y. Un point fixe imposerait y = 0 et x = x + 2 : **impossible**. Aucun point fixe et f n'est pas une translation (elle retourne le plan) : c'est la **symétrie glissante** d'axe (Ox) et de vecteur (2 ; 0) ✓.

> ⚠️ Une écriture en **z** (z′ = az + b) et une écriture en **z̄** (z′ = az̄ + b) ne donnent jamais le même genre d'isométrie. Vérifie toujours **|a| = 1** avant tout : si |a| ≠ 1, l'application n'est pas une isométrie et rien de ce chapitre ne s'applique.

> 🏆 Onzième porte franchie, héros. Tu tiens désormais la carte complète du plan : une isométrie conserve distances, angles, milieux et parallélisme ; elle est bijective ; elle se compose ; et surtout elle se **lit** dans ses points fixes — tout le plan, une droite, un point, ou rien du tout. Cinq natures, trois symétries orthogonales au maximum. Au chapitre suivant, on reprendra cette même liste et on la coupera en deux selon que la figure garde ou retourne son orientation : ce sera l'affaire des déplacements et des antidéplacements.
