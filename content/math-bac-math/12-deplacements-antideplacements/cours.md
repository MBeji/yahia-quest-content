# ⚔️ Déplacements et antidéplacements — le plan qui garde ou renverse son sens

> 💡 «Deux figures peuvent avoir exactement les mêmes mesures et rester impossibles à superposer sans quitter la feuille : entre elles, il y a un miroir.»

Dans tout ce chapitre, **le plan est orienté dans le sens direct**. Au chapitre précédent, tu as appris qu'une isométrie conserve les distances, qu'elle se décompose en **au plus trois symétries orthogonales**, et que ses points fixes la trahissent. Il manquait un mot pour dire ce qui sépare une rotation d'une symétrie : le **sens**. Euler l'avait déjà remarqué au XVIIIᵉ siècle — un déplacement du plan n'est jamais qu'une rotation, une translation, ou une translation suivie d'une symétrie. Ce chapitre installe ce vocabulaire, en fait un outil de reconnaissance imparable, et l'écrit en nombres complexes.

## 🏰 Une isométrie garde le sens, ou le renverse

Prends le triangle direct A(0, 0), B(1, 0), D(0, 1) : l'angle orienté (AB⃗, AD⃗) vaut π/2.

Applique-lui la **symétrie orthogonale d'axe (AB)** : A et B ne bougent pas, et D(0, 1) devient D′(0, −1). Alors (A′B′⃗, A′D′⃗) = ((1, 0), (0, −1)) : cet angle vaut **−π/2**. La mesure a changé de signe.

Applique-lui maintenant la **rotation r de centre I(1/2, 1/2) et d'angle π/2** : on trouve A′(1, 0), B′(1, 1), D′(0, 0), donc A′B′⃗ = (0, 1) et A′D′⃗ = (−1, 0) : l'angle vaut **+π/2**, inchangé.

> **Théorème** — « Toute symétrie orthogonale change les mesures des angles orientés en leurs opposées. (On dit qu'une symétrie orthogonale change l'orientation). »

> **Théorème** — « La composée de deux symétries orthogonales conserve les mesures des angles orientés. (On dit que la composée de deux symétries orthogonales conserve l'orientation). »

::: figure Le triangle du bas est l'image du triangle du haut par la symétrie d'axe (AB) : mêmes longueurs, mêmes angles géométriques — mais la flèche de parcours A → B → D s'est retournée.
<svg viewBox="0 0 240 265"><path d="M73 137 L153 137 L73 57 Z" fill="#0f6e56" opacity="0.12"/><path d="M73 137 L153 137 L73 217 Z" fill="#b45309" opacity="0.12"/><path d="M73 137 L153 137 L73 57 Z" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><path d="M73 137 L153 137 L73 217 Z" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><path d="M35 137 H225" fill="none" stroke="#0f6e56" stroke-width="2" stroke-dasharray="8 5"/><path d="M110 110 A 12 12 0 0 0 90 110" fill="none" stroke="#0f6e56" stroke-width="2"/><path d="M90 117 L85 108 L95 108 Z" fill="#0f6e56"/><path d="M90 164 A 12 12 0 0 1 110 164" fill="none" stroke="#b45309" stroke-width="2"/><path d="M110 171 L105 162 L115 162 Z" fill="#b45309"/><g fill="#0f172a"><circle cx="73" cy="137" r="4"/><circle cx="153" cy="137" r="4"/><circle cx="73" cy="57" r="4"/><circle cx="73" cy="217" r="4"/></g><g font-size="15" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="60" y="155" text-anchor="middle" fill="#0f172a">A</text><text x="163" y="155" text-anchor="middle" fill="#0f172a">B</text><text x="73" y="45" text-anchor="middle" fill="#0f172a">D</text><text x="73" y="236" text-anchor="middle" fill="#0f172a">D′</text><text x="212" y="128" text-anchor="middle" fill="#0f6e56">(AB)</text></g></svg>
:::

> **Définition** — « On appelle **déplacement** toute isométrie qui conserve les mesures des angles orientés. On appelle **antidéplacement** toute isométrie qui change les mesures des angles orientés en leurs opposées. »

Le tableau de classification des isométries du plan tient alors en cinq lignes (les deux dernières colonnes viennent du chapitre 11) :

| Isométrie              | Nature             | Décomposition minimale         | Points fixes         |
| ---------------------- | ------------------ | ------------------------------ | -------------------- |
| Identité               | **Déplacement**    | 0 symétrie                     | tout le plan         |
| Translation (u⃗ ≠ 0⃗)   | **Déplacement**    | 2 symétries d'axes parallèles  | aucun                |
| Rotation (θ ≠ 0)       | **Déplacement**    | 2 symétries d'axes sécants     | un seul (le centre)  |
| Symétrie orthogonale   | **Antidéplacement**| 1 symétrie                     | une droite (l'axe)   |
| Symétrie glissante     | **Antidéplacement**| 3 symétries                    | aucun                |

> ⚠️ Un antidéplacement reste une **isométrie** : il conserve les distances, les angles **géométriques** (non orientés), le parallélisme, les milieux. Il ne renverse que le **signe** des angles orientés. Dire « la symétrie ne conserve pas les angles » est faux ; elle ne conserve pas les angles **orientés**.

## ⚡ Compter les symétries : le critère de reconnaissance

Une symétrie orthogonale renverse le sens ; en composer deux le rétablit. Donc la composée de **n** symétries orthogonales conserve l'orientation si et seulement si **n est pair**. Comme toute isométrie se décompose en au plus trois symétries orthogonales (chapitre 11), il ne reste que deux cas.

> **Théorème** — « Une isométrie est un déplacement, si et seulement si, elle est la composée de deux symétries orthogonales. Une isométrie est un antidéplacement, si et seulement si, elle est une symétrie orthogonale ou la composée de trois symétries orthogonales. »

Ce critère de parité se propage à toutes les compositions :

> **Théorème** — « • La composée de deux déplacements est un déplacement. • La composée de deux antidéplacements est un déplacement. • La composée d'un déplacement et d'un antidéplacement est un antidéplacement. • La réciproque d'un déplacement est un déplacement. • La réciproque d'un antidéplacement est un antidéplacement. »

Retiens-le comme une règle de signes : déplacement = **+1**, antidéplacement = **−1**, et la nature d'une composée est le **produit** des signes. Ainsi S₃∘S₂∘S₁ vaut (−1)³ = −1 : c'est un antidéplacement, quelles que soient les trois droites.

::: figure Composer deux symétries d'axes sécants fait tourner M de deux fois l'angle des axes : c'est la machine qui fabrique toutes les rotations.
<svg viewBox="0 0 340 250"><circle cx="170" cy="130" r="102" fill="none" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4 4"/><path d="M50 130 H300" fill="none" stroke="#0f172a" stroke-width="2"/><path d="M70 188 L270 72" fill="none" stroke="#0f172a" stroke-width="2"/><path d="M170 130 L205 34 M170 130 L205 226 M170 130 L104 52" fill="none" stroke="#0f6e56" stroke-width="2"/><path d="M225 130 A 55 55 0 0 0 218 103" fill="none" stroke="#b45309" stroke-width="2"/><path d="M184 92 A 40 40 0 0 0 144 99" fill="none" stroke="#b45309" stroke-width="2"/><g fill="#0f172a"><circle cx="170" cy="130" r="4"/></g><g fill="#0f6e56"><circle cx="205" cy="34" r="4"/><circle cx="205" cy="226" r="4"/><circle cx="104" cy="52" r="4"/></g><g font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="158" y="147" text-anchor="middle" fill="#0f172a">O</text><text x="216" y="26" text-anchor="middle" fill="#0f6e56">M</text><text x="218" y="242" text-anchor="middle" fill="#0f6e56">M₁</text><text x="90" y="44" text-anchor="middle" fill="#0f6e56">M₂</text><text x="294" y="146" text-anchor="middle" fill="#0f172a">D</text><text x="282" y="66" text-anchor="middle" fill="#0f172a">D′</text><text x="236" y="118" text-anchor="middle" fill="#b45309">α</text><text x="160" y="78" text-anchor="middle" fill="#b45309">2α</text></g></svg>
:::

_Exemple détaillé_ — soit D une droite, O un point de D, et R la rotation de centre O et d'angle π/3. Quelle est la nature de S_D∘R ?

**Compte** : R vaut 2 symétries, S_D en vaut 1, total 3 → **antidéplacement**. **Identification** : d'après le chapitre 11, R = S_D∘S_Δ où Δ est la droite passant par O telle que 2(Δ, D) ≡ π/3, soit (Δ, D) ≡ π/6. Alors :

$$ S_D∘R = S_D∘(S_D∘S_Δ) = (S_D∘S_D)∘S_Δ = S_Δ $$

C'est donc la **symétrie orthogonale** d'axe Δ, la droite passant par O et faisant l'angle −π/6 avec D. _Contrôle_ — un antidéplacement qui fixe un point ne peut être qu'une symétrie orthogonale (tableau ci-dessus) : ici O est fixe par R et par S_D, donc par la composée ✓.

## 🛡️ Deux points suffisent

Un déplacement est une transformation très rigide : connaître l'image de **deux** points la détermine entièrement.

> **Théorème** — « Deux déplacements qui coïncident sur deux points distincts sont égaux. Deux antidéplacements qui coïncident sur deux points distincts sont égaux. »

> **Théorème** — « Soit A, B, C et D des points du plan tels que AB⃗ = CD⃗ et AB⃗ ≠ 0⃗. Il existe un unique déplacement qui envoie A sur C et B sur D. Il existe un unique antidéplacement qui envoie A sur C et B sur D. »

En pratique, la condition qui sert est celle des **longueurs** : dès que **AB = CD ≠ 0**, il existe exactement **un** déplacement et **un** antidéplacement envoyant A sur C et B sur D — pas un de plus, pas un de moins. C'est sous cette forme que le manuel l'utilise dans ses exercices résolus, et c'est la clé de tous les problèmes « déterminer toutes les isométries telles que… » : la réponse en compte toujours exactement deux.

_Exemple détaillé_ — soit ABCD le carré direct A(0, 0), B(1, 0), C(1, 1), D(0, 1), de centre I(1/2, 1/2). Cherchons les isométries f telles que f(A) = B et f(B) = C.

D'abord l'existence : AB = 1 et BC = 1, donc AB = BC ≠ 0 → il y a **exactement deux** solutions, un déplacement et un antidéplacement. Traitons le déplacement, noté f. Son angle est θ = (AB⃗, BC⃗) = ((1, 0), (0, 1)) ≡ π/2 [2π] : comme θ ≢ 0 [2π], **f est une rotation d'angle π/2** (section suivante). Son centre Ω vérifie f(Ω) = Ω, donc ΩB = f(Ω)f(A) = ΩA : il est sur la médiatrice de [AB], d'équation x = 1/2. De même ΩC = f(Ω)f(B) = ΩB le place sur la médiatrice de [BC], d'équation y = 1/2. Donc **Ω = I**.

_Contrôle_ — la rotation de centre I et d'angle π/2 envoie effectivement A(0, 0) sur B(1, 0), puis B sur C : elle fait tourner le carré direct d'un quart de tour ✓. L'antidéplacement, lui, sera identifié dans la dernière section : ce n'est pas une symétrie orthogonale.

> ⚠️ « Deux isométries qui coïncident sur deux points sont égales » est **faux** sans l'hypothèse de même nature. L'identité et la symétrie S_D coïncident sur tous les points de D — mais l'une est un déplacement, l'autre un antidéplacement. Il faut deux **déplacements**, ou deux **antidéplacements**.

## 🔮 L'angle d'un déplacement : translation ou rotation

> **Théorème et définition** — « Soit f un déplacement et A, B, C et D des points du plan tels que AB⃗ ≠ 0⃗ et CD⃗ ≠ 0⃗. Si A′, B′, C′ et D′ sont les images respectives par f des points A, B, C et D, alors (AB⃗, A′B′⃗) ≡ (CD⃗, C′D′⃗) [2π]. En désignant par θ une mesure de l'angle (AB⃗, A′B′⃗), on dit que f est un **déplacement d'angle θ**. »

Autrement dit : un déplacement fait tourner **tous** les vecteurs du même angle. Ce nombre θ ne dépend pas du couple de points choisi — c'est la carte d'identité du déplacement.

::: figure Les deux couples de vecteurs tournent exactement du même quart de tour : cet angle ne dépend pas des points choisis, il appartient au déplacement.
<svg viewBox="0 0 280 250"><path d="M177 172 L219 130" fill="none" stroke="#0f172a" stroke-width="2.2"/><path d="M219 130 l-10 1 l1 9 z" fill="#0f172a"/><path d="M93 88 L51 46" fill="none" stroke="#0f172a" stroke-width="2.2"/><path d="M51 46 l1 10 l9 -1 z" fill="#0f172a"/><path d="M135 214 L177 214" fill="none" stroke="#0f6e56" stroke-width="2.2"/><path d="M177 214 l-9 -5 l0 10 z" fill="#0f6e56"/><path d="M135 130 L135 88" fill="none" stroke="#0f6e56" stroke-width="2.2"/><path d="M135 88 l-5 9 l10 0 z" fill="#0f6e56"/><g fill="#0f172a"><circle cx="177" cy="172" r="3.5"/><circle cx="93" cy="88" r="3.5"/></g><g fill="#0f6e56"><circle cx="135" cy="214" r="3.5"/><circle cx="135" cy="130" r="3.5"/></g><g font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="185" y="188" text-anchor="middle" fill="#0f172a">A</text><text x="233" y="126" text-anchor="middle" fill="#0f172a">B</text><text x="82" y="104" text-anchor="middle" fill="#0f172a">A′</text><text x="40" y="42" text-anchor="middle" fill="#0f172a">B′</text><text x="126" y="231" text-anchor="middle" fill="#0f6e56">C</text><text x="188" y="231" text-anchor="middle" fill="#0f6e56">D</text><text x="120" y="128" text-anchor="middle" fill="#0f6e56">C′</text><text x="121" y="84" text-anchor="middle" fill="#0f6e56">D′</text></g></svg>
:::

> **Corollaire 1** — « Soit f un déplacement d'angle θ. Si θ = 2kπ, k ∈ ℤ alors f est une **translation**. Si θ ≠ 2kπ, k ∈ ℤ alors f est une **rotation d'angle θ**. »

> **Corollaire 2** — « • Si f est un déplacement d'angle θ et g est un déplacement d'angle θ′, alors f∘g est un déplacement d'angle θ + θ′. • Si f est un déplacement d'angle θ, alors f⁻¹ est un déplacement d'angle −θ. »

_Exemple détaillé_ — reprends le carré direct A(0, 0), B(1, 0), C(1, 1), D(0, 1). Soit g le déplacement tel que g(A) = D et g(B) = C. Son angle est (AB⃗, DC⃗) = ((1, 0), (1, 0)) ≡ 0 [2π] : **g est une translation**, nécessairement de vecteur AD⃗ = (0, 1). _Contrôle_ — la translation de vecteur (0, 1) envoie A(0, 0) sur (0, 1) = D ✓ et B(1, 0) sur (1, 1) = C ✓.

Compare avec l'exemple précédent : mêmes points de départ, une image changée, et la nature bascule de la rotation à la translation. **C'est l'angle, et lui seul, qui décide.**

> ⚠️ L'angle d'un déplacement se lit entre un vecteur MN⃗ et **son image** M′N′⃗ — jamais entre M et son image. L'angle (MO⃗, MM′⃗) n'a aucune raison de valoir θ.

## 🧮 Composer des déplacements

**a) Deux translations.**

> **Théorème (rappel)** — « La composée de deux translations t_u⃗ et t_v⃗ est la translation t_(u⃗+v⃗) = t_u⃗∘t_v⃗ = t_v⃗∘t_u⃗ = t_(v⃗+u⃗). »

Les translations commutent : leurs angles valent 0, et 0 + 0 = 0.

**b) Deux rotations.**

> **Théorème** — « La composée de deux rotations r et r′ d'angles θ et θ′ et de centres respectifs O et O′ est soit une translation de vecteur non nul, soit une rotation d'angle non nul. Si θ + θ′ ≡ 0 [2π], il s'agit d'une **translation** de vecteur non nul. Si θ + θ′ ≠ 2kπ, k ∈ ℤ, il s'agit d'une **rotation d'angle θ + θ′**. »

_Exemple détaillé_ — soit r la rotation de centre O(0, 0) et d'angle π/2, et r′ la rotation de centre A(1, 0) et d'angle π/2. Comme θ + θ′ = π ≢ 0 [2π], f = r∘r′ est une **rotation d'angle π**, c'est-à-dire une **symétrie centrale**. Reste le centre : il suffit de suivre **un** point bien choisi. Prenons M(1/2, 1) :

$$ r′(M) = M₁(0, −1/2)     puis     r(M₁) = M₂(1/2, 0) $$

Le centre Ω d'une symétrie centrale est le milieu de [MM₂], donc **Ω(1/2, 1/2)**. _Contrôle sur un second point_ — r′(O) = (1, −1) puis r((1, −1)) = (1, 1) ; or le symétrique de O(0, 0) par rapport à Ω(1/2, 1/2) est bien (1, 1) ✓. Deux points concordants, l'identification est sûre.

::: figure Deux quarts de tour autour de centres différents composent un demi-tour : Ω est le milieu de [MM₂], et il n'est ni O ni A.
<svg viewBox="0 0 240 265"><path d="M113 58 L58 223" fill="none" stroke="#94a3b8" stroke-width="1.8" stroke-dasharray="6 4"/><path d="M58 223 l9 -4 l-6 -8 z" fill="#94a3b8"/><path d="M58 223 L113 168" fill="none" stroke="#94a3b8" stroke-width="1.8" stroke-dasharray="6 4"/><path d="M113 168 l-10 0 l4 9 z" fill="#94a3b8"/><path d="M113 58 L113 168" fill="none" stroke="#0f6e56" stroke-width="2.4"/><g fill="#0f172a"><circle cx="58" cy="168" r="4"/><circle cx="168" cy="168" r="4"/></g><g fill="#0f6e56"><circle cx="113" cy="58" r="4"/><circle cx="58" cy="223" r="4"/><circle cx="113" cy="168" r="4"/><circle cx="113" cy="113" r="5"/></g><g font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="46" y="162" text-anchor="middle" fill="#0f172a">O</text><text x="178" y="162" text-anchor="middle" fill="#0f172a">A</text><text x="113" y="46" text-anchor="middle" fill="#0f6e56">M</text><text x="44" y="240" text-anchor="middle" fill="#0f6e56">M₁</text><text x="130" y="184" text-anchor="middle" fill="#0f6e56">M₂</text><text x="129" y="110" text-anchor="middle" fill="#0f6e56">Ω</text><text x="76" y="120" text-anchor="middle" fill="#94a3b8">r′</text><text x="70" y="205" text-anchor="middle" fill="#94a3b8">r</text></g></svg>
:::

_Exemple (le cas limite)_ — garde r (centre O, angle π/2) mais prends r′ de centre A(1, 0) et d'angle **−π/2**. Alors θ + θ′ = 0 : la composée est une **translation**. Son vecteur se lit sur une image : r′(O) = (1, 1) puis r((1, 1)) = (−1, 1), donc le vecteur est (−1, 1). _Contrôle_ — r′(A) = A puis r(A) = (0, 1) : de A(1, 0) à (0, 1), le vecteur est bien (−1, 1) ✓.

**c) Une rotation et une translation.**

> **Théorème** — « La composée d'une translation et d'une rotation d'angle non nul θ est une **rotation d'angle θ**. »

_Exemple détaillé_ — soit t la translation de vecteur u⃗(2, 0) et r la rotation de centre O(0, 0) et d'angle π/2. Les deux composées sont des rotations d'angle π/2, mais **pas les mêmes** : le centre de f = r∘t est (−1, 1), celui de g = t∘r est (1, 1) (vérification en nombres complexes à la section suivante). _Contrôle_ — f((−1, 1)) : la translation donne (1, 1), la rotation d'angle π/2 donne (−1, 1) ✓ point fixe. g((1, 1)) : la rotation donne (−1, 1), la translation donne (1, 1) ✓ point fixe.

_Exemple_ — pour u⃗ ≠ 0⃗ et A un point, t_u⃗∘S_A est la composée d'une rotation d'angle π et d'une translation : c'est une **rotation d'angle π**, donc une **symétrie centrale**. Avec A = O(0, 0) et u⃗(2, 0) : S_A(M) = −M puis on ajoute (2, 0) ; le point (1, 0) est fixe, donc le centre est (1, 0). _Contrôle_ — M(3, 1) → S_A → (−3, −1) → +u⃗ → (−1, −1), et le symétrique de (3, 1) par rapport à (1, 0) est bien (−1, −1) ✓.

> 🗡️ Pour une composée, ne cherche **jamais** l'image d'un point quelconque : prends un point que l'une des deux transformations laisse fixe (un centre, un sommet). Le calcul se réduit de moitié.

> ⚠️ La composition **n'est pas commutative** : r∘t et t∘r ont le même angle mais des centres différents. L'ordre d'écriture compte, et f∘g signifie « g d'abord ».

## 📐 Déplacements et nombres complexes

Le plan est rapporté à un repère orthonormé **direct** (O, i⃗, j⃗).

> **Théorème** — « L'application f est une **translation** de vecteur u⃗, si et seulement si, il existe un nombre complexe b tel que z′ = z + b où b est l'affixe de u⃗. »

> **Théorème** — « L'application f est une **rotation** d'angle non nul θ et de centre I, si et seulement si, il existe deux nombres complexes a et b tels que z′ = az + b, avec a = e^(iθ), a ≠ 1 et z_I = b/(1 − a) est l'affixe de I. »

Un déplacement s'écrit donc toujours **z′ = az + b avec |a| = 1** : si a = 1 c'est une translation, sinon une rotation d'angle θ = arg(a) et de centre b/(1 − a).

_Exemple détaillé_ — soit f : z ↦ e^(iπ/3)·z + 2. Ici a = e^(iπ/3) ≠ 1 et |a| = 1 : f est une rotation d'angle π/3. Son centre :

$$ z_I = 2/(1 − e^(iπ/3)) = 2/(1/2 − i√3/2) = 2/e^(−iπ/3) = 2e^(iπ/3) = 1 + i√3 $$

_Contrôle_ — on vérifie que I est fixe : e^(iπ/3)(1 + i√3) + 2 = e^(iπ/3)·2e^(iπ/3) + 2 = 2e^(2iπ/3) + 2 = (−1 + i√3) + 2 = 1 + i√3 ✓.

_Exemple_ — z′ = z + 1 + i est la **translation** de vecteur (1, 1). Et z′ = −z + 1 s'écrit avec a = −1 = e^(iπ) : c'est la rotation d'angle π, de centre 1/(1 − (−1)) = 1/2, donc la **symétrie centrale** de centre (1/2, 0).

_Exemple détaillé (retour sur r∘t et t∘r)_ — avec u⃗(2, 0) et r : z ↦ iz, on obtient f = r∘t : z ↦ i(z + 2) = iz + 2i, de centre 2i/(1 − i) = 2i(1 + i)/2 = **−1 + i** ; et g = t∘r : z ↦ iz + 2, de centre 2/(1 − i) = 2(1 + i)/2 = **1 + i**. Les deux centres annoncés plus haut sont confirmés ✓.

> 🗡️ **Passerelle du chapitre 11** — une isométrie s'écrit z′ = az + b **ou** z′ = az̄ + b, avec |a| = 1. Dans le second cas, l'image du vecteur d'affixe w est a·w̄, donc un angle arg(w₂/w₁) devient −arg(w₂/w₁) : la forme **conjuguée caractérise les antidéplacements**. C'est le test le plus rapide quand une isométrie est donnée par son écriture complexe : cherche la barre de conjugaison.

> ⚠️ La condition |a| = 1 n'est pas décorative. Si |a| ≠ 1, z′ = az + b n'est **plus** une isométrie : les distances sont multipliées par |a|. On quitte alors ce chapitre pour celui des **similitudes**.

## ⚔️ Antidéplacements : symétrie orthogonale ou symétrie glissante

> **Théorème** — « Une isométrie est un antidéplacement, si et seulement si, c'est la composée d'une symétrie orthogonale et d'une translation. »

Il n'existe donc que deux espèces d'antidéplacements. Si la translation est nulle — ou plus généralement si l'antidéplacement **possède un point fixe** — c'est une **symétrie orthogonale**. Sinon, c'est une **symétrie glissante**.

> **Théorème et définition (forme réduite)** — « Soit f une symétrie glissante. Il existe un unique vecteur non nul u⃗ et une droite D unique tels que f = t_u⃗∘S_D = S_D∘t_u⃗ où u⃗ est un **vecteur directeur de D**. Cette décomposition est appelée **forme réduite** de f. »

> **Vocabulaire** — « On dit que D est l'**axe** de la symétrie glissante et u⃗ son **vecteur**. L'axe et le vecteur d'une symétrie glissante sont ses éléments caractéristiques. »

::: figure Glisser puis retourner, ou retourner puis glisser : même image M′ — et le milieu I de [MM′] tombe toujours sur l'axe.
<svg viewBox="0 0 330 230"><path d="M25 130 H320" fill="none" stroke="#0f172a" stroke-width="2"/><path d="M40 130 L160 130" fill="none" stroke="#0f6e56" stroke-width="3.4"/><path d="M166 130 l-11 -5 l0 10 z" fill="#0f6e56"/><path d="M82 67 L82 187" fill="none" stroke="#94a3b8" stroke-width="1.8" stroke-dasharray="6 4"/><path d="M82 193 l-5 -9 l10 0 z" fill="#94a3b8"/><path d="M88 193 L202 193" fill="none" stroke="#94a3b8" stroke-width="1.8" stroke-dasharray="6 4"/><path d="M208 193 l-9 -5 l0 10 z" fill="#94a3b8"/><path d="M82 67 L208 193" fill="none" stroke="#b45309" stroke-width="1.6" stroke-dasharray="3 4"/><g fill="#0f172a"><circle cx="82" cy="67" r="4"/><circle cx="82" cy="193" r="4"/><circle cx="208" cy="193" r="4"/></g><g fill="#b45309"><circle cx="145" cy="130" r="4.5"/></g><g font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="82" y="55" text-anchor="middle" fill="#0f172a">M</text><text x="66" y="210" text-anchor="middle" fill="#0f172a">M₁</text><text x="216" y="210" text-anchor="middle" fill="#0f172a">M′</text><text x="152" y="150" text-anchor="middle" fill="#b45309">I</text><text x="100" y="120" text-anchor="middle" fill="#0f6e56">u⃗</text><text x="308" y="120" text-anchor="middle" fill="#0f172a">D</text></g></svg>
:::

> **Propriété** — « Soit f une symétrie glissante de vecteur u⃗ et d'axe D, M un point d'image M′ par f. • Le milieu de [MM′] appartient à D. • Si M est un point de D, alors u⃗ = MM′⃗. • f∘f est la translation de vecteur 2u⃗. »

Ces trois propriétés **sont** la méthode de reconnaissance : calcule f∘f ; si tu obtiens t_(2u⃗) avec u⃗ ≠ 0⃗, tu tiens le vecteur, et deux milieux [MM′] te donnent l'axe.

**Réduire un antidéplacement donné sous la forme t_v⃗∘S_D.** Si v⃗ n'est pas parallèle à D, décompose v⃗ = v₁⃗ + v₂⃗ avec v₁⃗ parallèle à D et v₂⃗ perpendiculaire à D. Alors t_(v₂⃗)∘S_D = S_(D′), où D′ est l'image de D par la translation de vecteur **½v₂⃗**, et la forme réduite est f = t_(v₁⃗)∘S_(D′).

::: figure La part de v⃗ perpendiculaire à l'axe ne fait que déplacer l'axe de la moitié : après réduction, il ne reste que la part parallèle v₁⃗.
<svg viewBox="0 0 290 260"><path d="M30 228 H265" fill="none" stroke="#0f172a" stroke-width="2"/><path d="M30 138 H265" fill="none" stroke="#0f6e56" stroke-width="2"/><path d="M53 228 L137 60" fill="none" stroke="#b45309" stroke-width="2.4"/><path d="M143 48 l-11 4 l9 5 z" fill="#b45309"/><path d="M53 228 L137 228" fill="none" stroke="#94a3b8" stroke-width="1.8" stroke-dasharray="6 4"/><path d="M143 228 l-9 -5 l0 10 z" fill="#94a3b8"/><path d="M143 228 L143 54" fill="none" stroke="#94a3b8" stroke-width="1.8" stroke-dasharray="6 4"/><path d="M143 48 l-5 9 l10 0 z" fill="#94a3b8"/><path d="M53 138 L137 138" fill="none" stroke="#0f6e56" stroke-width="3.4"/><path d="M143 138 l-11 -5 l0 10 z" fill="#0f6e56"/><g fill="#0f172a"><circle cx="53" cy="228" r="4"/></g><g font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="277" y="233" text-anchor="middle" fill="#0f172a">D</text><text x="275" y="132" text-anchor="middle" fill="#0f6e56">D′</text><text x="112" y="112" text-anchor="middle" fill="#b45309">v⃗</text><text x="95" y="248" text-anchor="middle" fill="#94a3b8">v₁⃗</text><text x="166" y="152" text-anchor="middle" fill="#94a3b8">v₂⃗</text><text x="68" y="126" text-anchor="middle" fill="#0f6e56">v₁⃗</text></g></svg>
:::

_Exemple détaillé_ — soit D l'axe des abscisses et f = t_v⃗∘S_D avec v⃗(2, 4). On décompose v⃗ = (2, 0) + (0, 4). La part perpendiculaire (0, 4) pousse l'axe de la moitié : D′ est la droite d'équation **y = 2**, et la forme réduite est f = t_((2, 0))∘S_(D′) : **axe y = 2, vecteur (2, 0)**.

_Contrôle sur deux points_ — M(1, 3) : par la définition, S_D(M) = (1, −3) puis +v⃗ donne (3, 1) ; par la forme réduite, S_(D′)(M) = (1, 1) puis +(2, 0) donne (3, 1) ✓. M(0, 0) : (0, 0) puis +v⃗ = (2, 4) ; et S_(D′)(0, 0) = (0, 4) puis +(2, 0) = (2, 4) ✓. _Contrôle par la propriété du milieu_ — le milieu de [(0, 0) ; (2, 4)] est (1, 2), qui appartient bien à y = 2 ✓.

_Exemple détaillé (l'antidéplacement du carré, promis plus haut)_ — reprenons A(0, 0), B(1, 0), C(1, 1), D(0, 1) et l'unique antidéplacement g tel que g(A) = B et g(B) = C. En écriture complexe, un antidéplacement s'écrit z′ = az̄ + b avec |a| = 1 ; de g(0) = 1 on tire b = 1, et de g(1) = 1 + i on tire a + 1 = 1 + i, donc **a = i** et g : z ↦ iz̄ + 1.

_A-t-il un point fixe ?_ Avec z = x + iy, iz̄ + 1 = (y + 1) + ix ; l'égalité avec x + iy impose x = y + 1 et y = x, soit x = x + 1 : **impossible**. Donc g n'est pas une symétrie orthogonale, c'est une **symétrie glissante**. Son vecteur : g∘g(z) = i·conj(iz̄ + 1) + 1 = i(−iz + 1) + 1 = z + 1 + i, donc 2u⃗ = (1, 1) et **u⃗ = (1/2, 1/2)**. Son axe : les milieux de [A g(A)] et [B g(B)] valent I(1/2, 0) et J(1, 1/2) — les milieux de deux côtés du carré. L'axe est donc la droite **(IJ)**, d'équation y = x − 1/2, et l'on remarque que u⃗ = IJ⃗ ✓ (il dirige bien l'axe).

_Contrôle_ — la symétrie d'axe y = x − 1/2 envoie (x, y) sur (y + 1/2, x − 1/2). Pour A(0, 0) : (1/2, −1/2), puis + u⃗ donne (1, 0) = B ✓. Pour B(1, 0) : (1/2, 1/2), puis + u⃗ donne (1, 1) = C ✓. Les deux images demandées sont retrouvées.

> ⚠️ Une symétrie glissante n'est **jamais** involutive : f∘f = t_(2u⃗) ≠ Id. En revanche f⁻¹ est la symétrie glissante de **même axe** et de vecteur **−u⃗**. Et la composée de deux symétries glissantes est un **déplacement** (deux antidéplacements → produit des signes = +1), jamais une symétrie glissante.

## 👑 Méthode : identifier une isométrie, à tous les coups

Face à « déterminer la nature et les éléments caractéristiques de f », déroule toujours le même algorithme.

| Étape | Question                              | Outil                                                                 |
| ----- | ------------------------------------- | --------------------------------------------------------------------- |
| 1     | Déplacement ou antidéplacement ?      | parité du nombre de symétries · barre de conjugaison en complexes     |
| 2     | Si déplacement : quel angle θ ?       | (AB⃗, A′B′⃗) · somme des angles composés · θ ≡ 0 ⇒ translation        |
| 3     | Si antidéplacement : un point fixe ?  | oui ⇒ symétrie orthogonale · non ⇒ symétrie glissante                 |
| 4     | Éléments caractéristiques             | un point image bien choisi ; centre, vecteur, ou f∘f = t_(2u⃗) + milieux |
| 5     | Vérification                          | tester l'application obtenue sur un **second** point                  |

_Exemple détaillé (synthèse)_ — carré direct A(0, 0), B(1, 0), C(1, 1), D(0, 1) ; K(1/2, 1) le milieu de [CD]. Déterminons l'antidéplacement g tel que g(B) = K et g(K) = A.

**Étape 0 — existence** : BK = √((1/2)² + 1²) = √5/2 et KA = √((1/2)² + 1²) = √5/2, donc BK = KA ≠ 0 : g existe et est unique. **Étape 3 — point fixe ?** Les médiatrices de [BK] et de [KA] sont distinctes (la première passe par (3/4, 1/2), la seconde par (1/4, 1/2), avec des directions différentes), donc g n'a pas de droite de points fixes : c'est une **symétrie glissante**. **Étape 4 — éléments** : les milieux de [B g(B)] et de [K g(K)] valent (3/4, 1/2) et (1/4, 1/2) ; ils sont sur l'axe, donc l'axe est la droite **y = 1/2**, c'est-à-dire (LJ) avec L(0, 1/2) et J(1, 1/2) milieux de [DA] et [BC]. Le vecteur se lit sur g∘g(B) = g(K) = A : g∘g = t_(2u⃗) envoie B(1, 0) sur A(0, 0), donc 2u⃗ = (−1, 0) et **u⃗ = (−1/2, 0) = ½BA⃗**.

**Étape 5 — vérification** : la symétrie d'axe y = 1/2 suivie de la translation de vecteur (−1/2, 0) envoie (x, y) sur (x − 1/2, 1 − y). Pour B(1, 0) : (1/2, 1) = K ✓. Pour K(1/2, 1) : (0, 0) = A ✓. L'axe y = 1/2 dirige bien u⃗(−1/2, 0) ✓. Identification confirmée.

> 🏆 Douzième porte franchie, héros : tu sais désormais lire le **sens** d'une isométrie, la ranger en deux clans, additionner des angles pour identifier une composée à vue, et réduire n'importe quel antidéplacement à un axe et un vecteur. Garde bien ton écriture complexe z′ = az + b : au chapitre suivant, on lâchera la contrainte |a| = 1 — les figures cesseront d'être égales pour devenir **semblables**, et tu entreras dans le monde des similitudes.
