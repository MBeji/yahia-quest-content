# ⚔️ Géométrie dans l'espace — le produit qui dresse la normale

> 💡 «Dans le plan, une droite se donne par une équation. Dans l'espace, c'est un plan qui en a une — et la droite, elle, se raconte en paramètres. Tout le chapitre tient dans cette bascule.»

Dans tout ce chapitre, **l'espace est orienté dans le sens direct**. Tu sais déjà calculer un produit scalaire dans le plan, écrire l'équation d'une droite, mesurer une distance. L'espace ajoute une troisième coordonnée — et surtout une opération nouvelle, le **produit vectoriel**, qui n'existe qu'ici : à deux vecteurs il associe un troisième vecteur, perpendiculaire aux deux. Gibbs l'a écrit sous cette forme en 1881, pour ses étudiants de physique. C'est l'outil qui fabrique les vecteurs normaux, les aires, les volumes et presque toutes les distances de ce chapitre.

## 🏰 Lire une figure de l'espace, et la coder en trois nombres

Une feuille est plate ; l'espace ne l'est pas. Toutes les figures de ce chapitre utilisent donc **la même** convention de dessin, la **perspective cavalière** : les directions horizontale et verticale sont vraies, la troisième — la **fuyante**, celle qui s'enfonce dans la profondeur — est tracée à 30° vers le haut et **réduite de moitié**. Les arêtes qu'on ne verrait pas sont en **pointillés**.

::: figure Le cube ABCDEFGH en perspective cavalière : le sommet D est caché derrière le solide, donc ses trois arêtes [AD], [DC] et [DH] sont en pointillés. Toutes les figures du chapitre se lisent avec cette même convention.
<svg viewBox="0 0 215 222"><path d="M60 195 L150 195 L189 172.5 L99 172.5 Z" fill="#0f6e56" opacity="0.10"/><path d="M60 195 L150 195 M150 195 L189 172.5 M189 172.5 L189 82.5 M189 82.5 L99 82.5 M99 82.5 L60 105 M60 105 L60 195 M150 195 L150 105 M150 105 L60 105 M150 105 L189 82.5" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><path d="M60 195 L99 172.5 M99 172.5 L189 172.5 M99 172.5 L99 82.5" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-dasharray="5 4"/><g fill="#0f172a"><circle cx="60" cy="195" r="3.5"/><circle cx="150" cy="195" r="3.5"/><circle cx="189" cy="172.5" r="3.5"/><circle cx="60" cy="105" r="3.5"/><circle cx="150" cy="105" r="3.5"/><circle cx="189" cy="82.5" r="3.5"/><circle cx="99" cy="82.5" r="3.5"/></g><circle cx="99" cy="172.5" r="3.5" fill="#94a3b8"/><g font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="50" y="210" text-anchor="middle" fill="#0f172a">A</text><text x="154" y="212" text-anchor="middle" fill="#0f172a">B</text><text x="200" y="184" text-anchor="middle" fill="#0f172a">C</text><text x="86" y="168" text-anchor="middle" fill="#94a3b8">D</text><text x="49" y="100" text-anchor="middle" fill="#0f172a">E</text><text x="157" y="99" text-anchor="middle" fill="#0f172a">F</text><text x="201" y="76" text-anchor="middle" fill="#0f172a">G</text><text x="94" y="74" text-anchor="middle" fill="#0f172a">H</text></g></svg>
:::

Sur ce cube d'arête 1, le repère **(A, AB⃗, AD⃗, AE⃗)** est orthonormé direct : c'est le repère qu'on choisit dans neuf exercices sur dix. Les huit sommets s'y lisent immédiatement : A(0, 0, 0), B(1, 0, 0), C(1, 1, 0), D(0, 1, 0), E(0, 0, 1), F(1, 0, 1), G(1, 1, 1), H(0, 1, 1).

Le produit scalaire, lui, se définit exactement comme dans le plan.

> **Définition** — « Soit A, B et C des points. Le produit scalaire des vecteurs AB⃗ et AC⃗ est le réel défini par • AB⃗ . AC⃗ = 0, si AB⃗ = 0⃗ ou AC⃗ = 0⃗. • AB⃗ . AC⃗ = AB.AC.cos BAĈ, si AB⃗ et AC⃗ sont non nuls. • AB⃗ . AB⃗ = AB⃗² = ‖AB⃗‖². »

> **Propriétés** — « Pour tous vecteurs u⃗, v⃗ et w⃗ de l'espace et tous réels α et β • u⃗.v⃗ = v⃗.u⃗. • u⃗.(v⃗ + w⃗) = u⃗.v⃗ + u⃗.w⃗. • (αu⃗).v⃗ = u⃗.(αv⃗) = α(u⃗.v⃗). • (αu⃗).(βv⃗) = αβ(u⃗.v⃗). »

> **Expression analytique** — « Soit (O, i⃗, j⃗, k⃗) un repère orthonormé de l'espace. Pour tous vecteurs u⃗(x, y, z) et v⃗(x′, y′, z′), u⃗.v⃗ = xx′ + yy′ + zz′ et ‖u⃗‖ = √(x² + y² + z²). Pour tous points M(x, y, z) et M′(x′, y′, z′), MM′ = √((x − x′)² + (y − y′)² + (z − z′)²). »

Deux vecteurs non nuls sont **orthogonaux** si et seulement si leur produit scalaire est nul. C'est la seule façon raisonnable de prouver une perpendicularité dans l'espace : on calcule, on ne regarde pas.

_Exemple détaillé_ — cube d'arête a, repère (A, AB⃗, AD⃗, AE⃗) mais avec l'unité a. Alors A(0, 0, 0), B(a, 0, 0), C(a, a, 0), D(0, a, 0), E(0, 0, a), F(a, 0, a), G(a, a, a), H(0, a, a), et AF⃗ = (a, 0, a). On lit chaque second vecteur par différence de coordonnées :

$$ AF⃗.AB⃗ = a² ; AF⃗.DC⃗ = a² ; AF⃗.DG⃗ = 2a² ; AF⃗.DH⃗ = a² ; AF⃗.DE⃗ = a² $$

_Détail des calculs_ — AB⃗ = (a, 0, 0) donne a·a + 0 + 0 = a². DC⃗ = C − D = (a, 0, 0), même calcul, a². DG⃗ = G − D = (a, 0, a) donne a·a + 0 + a·a = 2a². DH⃗ = H − D = (0, 0, a) donne 0 + 0 + a·a = a². DE⃗ = E − D = (0, −a, a) donne 0 + 0 + a·a = a². _Contrôle_ — AF⃗.DC⃗ = AF⃗.AB⃗ était prévisible : DC⃗ = AB⃗ ✓.

_Exemple détaillé (une perpendicularité)_ — cube d'arête 1 : montrons que la diagonale (AG) est **perpendiculaire au plan (BDE)**. On a AG⃗ = (1, 1, 1), BD⃗ = D − B = (−1, 1, 0) et BE⃗ = E − B = (−1, 0, 1). Alors AG⃗.BD⃗ = −1 + 1 + 0 = 0 ✓ et AG⃗.BE⃗ = −1 + 0 + 1 = 0 ✓. Comme BD⃗ et BE⃗ ne sont pas colinéaires, ils dirigent le plan (BDE) : AG⃗ est orthogonal à **deux directions non colinéaires** du plan, donc à ce plan tout entier.

> 🗡️ Pour montrer qu'une droite est perpendiculaire à un plan, il faut **deux** produits scalaires nuls, avec deux vecteurs **non colinéaires** du plan. Un seul ne prouve rien : une droite peut être orthogonale à une direction d'un plan sans lui être perpendiculaire.

## ⚡ Le produit vectoriel : un vecteur qui sort du plan

Dans le plan, deux vecteurs n'engendrent rien de nouveau. Dans l'espace, ils désignent une direction privilégiée : celle qui leur est perpendiculaire à tous les deux. C'est ce vecteur que le produit vectoriel construit.

> **Définition** — « Soit A, B et C des points de l'espace. Le produit vectoriel de AB⃗ par AC⃗ est le vecteur noté AB⃗∧AC⃗ et défini comme suit • si AB⃗ et AC⃗ colinéaires, alors AB⃗∧AC⃗ = 0⃗, • si AB⃗ et AC⃗ ne sont pas colinéaires, alors • AB⃗∧AC⃗ est orthogonal à AB⃗ et à AC⃗, • (AB⃗, AC⃗, AB⃗∧AC⃗) est une base directe, • ‖AB⃗∧AC⃗‖ = AB.AC.sin BAĈ. »

Trois exigences, et elles déterminent le vecteur sans ambiguïté : la **direction** (perpendiculaire au plan des deux), le **sens** (règle de la base directe), la **longueur** (avec un sinus, là où le produit scalaire prenait un cosinus).

::: figure Le vecteur u⃗∧v⃗ se dresse perpendiculairement au plan de u⃗ et de v⃗ ; sa longueur n'est pas quelconque, c'est exactement l'aire du parallélogramme colorié.
<svg viewBox="0 0 240 205"><path d="M55 175 L151 175 L216.6 151 L120.6 151 Z" fill="#0f6e56" opacity="0.14"/><path d="M55 175 L151 175 L216.6 151 L120.6 151 Z" fill="none" stroke="#0f172a" stroke-width="1.4"/><path d="M55 175 L145 175" fill="none" stroke="#0f172a" stroke-width="2.4"/><path d="M151 175 l-11 -5 l0 10 z" fill="#0f172a"/><path d="M55 175 L110.3 154.8" fill="none" stroke="#0f172a" stroke-width="2.4"/><path d="M120.6 151 L111.7 158.6 L108.9 151 Z" fill="#0f172a"/><path d="M55 175 L55 79" fill="none" stroke="#0f6e56" stroke-width="3"/><path d="M55 71 l-6 11 l12 0 z" fill="#0f6e56"/><path d="M55 163 L67 163 L67 175" fill="none" stroke="#0f6e56" stroke-width="1.6"/><circle cx="55" cy="175" r="4" fill="#0f172a"/><g font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="44" y="191" text-anchor="middle" fill="#0f172a">A</text><text x="108" y="193" text-anchor="middle" fill="#0f172a">u⃗</text><text x="80" y="152" text-anchor="middle" fill="#0f172a">v⃗</text><text x="55" y="62" text-anchor="middle" fill="#0f6e56">u⃗∧v⃗</text></g></svg>
:::

> **Propriétés** — « Soit u⃗ et v⃗ deux vecteurs et α, β deux réels. • u⃗∧u⃗ = 0⃗. • u⃗∧v⃗ = 0⃗, si et seulement si, u⃗ et v⃗ sont colinéaires. • u⃗∧v⃗ = −(v⃗∧u⃗), u⃗∧(v⃗ + w⃗) = u⃗∧v⃗ + u⃗∧w⃗, αu⃗∧βv⃗ = αβ(u⃗∧v⃗). »

> **Composantes** — « L'espace est muni d'une base orthonormée directe (i⃗, j⃗, k⃗). Pour tous vecteurs u⃗(a, b, c) et v⃗(a′, b′, c′), u⃗∧v⃗ = (bc′ − cb′)i⃗ + (ca′ − ac′)j⃗ + (ab′ − ba′)k⃗. »

Pour ne jamais te tromper de signe, écris les deux triplets l'un sous l'autre et **saute la ligne de la coordonnée cherchée** :

| coordonnée cherchée | on barre  | on calcule en croix |
| ------------------- | --------- | ------------------- |
| la 1ʳᵉ (i⃗)          | a et a′   | b c′ − c b′         |
| la 2ᵉ (j⃗)           | b et b′   | c a′ − a c′         |
| la 3ᵉ (k⃗)           | c et c′   | a b′ − b a′         |

_Exemple détaillé_ — repère orthonormé direct, A(1, 0, −1), B(1, −2, 1), C(0, −1, 2). Alors AB⃗ = (0, −2, 2) et AC⃗ = (−1, −1, 3), donc :

$$ AB⃗∧AC⃗ = ((−2)(3) − (2)(−1) ; (2)(−1) − (0)(3) ; (0)(−1) − (−2)(−1)) = (−4, −2, −2) $$

_Contrôle par orthogonalité (à faire systématiquement)_ — avec AB⃗ : 0·(−4) + (−2)(−2) + 2·(−2) = 0 + 4 − 4 = 0 ✓. Avec AC⃗ : (−1)(−4) + (−1)(−2) + 3·(−2) = 4 + 2 − 6 = 0 ✓. Les deux produits scalaires sont nuls : le calcul est juste.

_Suite — l'angle géométrique BAĈ._ On a ‖AB⃗∧AC⃗‖ = √(16 + 4 + 4) = √24 = 2√6, ‖AB⃗‖ = √8 = 2√2 et ‖AC⃗‖ = √11. Donc sin BAĈ = 2√6/(2√2·√11) = √(3/11). Par ailleurs AB⃗.AC⃗ = 0 + 2 + 6 = 8, donc cos BAĈ = 8/(2√22) = 4/√22. _Contrôle_ — cos² + sin² = 16/22 + 6/22 = 1 ✓. Comme cos BAĈ ≈ 0.853, on obtient **BAĈ ≈ 0.5 rad** (à 0.1 près).

> ⚠️ Le produit vectoriel **n'est pas commutatif** : u⃗∧v⃗ = −(v⃗∧u⃗). Il n'est pas non plus simplifiable : de u⃗∧v⃗ = u⃗∧w⃗ on ne peut **pas** conclure v⃗ = w⃗ (prends u⃗ = v⃗ et w⃗ = 2v⃗ : les deux produits valent 0⃗). Et u⃗∧v⃗ est un **vecteur**, alors que u⃗.v⃗ est un **réel** — écrire « u⃗∧v⃗ = 0 » sans la flèche est une faute.

## 🧮 Déterminant, aires et volumes

Un produit vectoriel suivi d'un produit scalaire donne un réel : le **produit mixte**. C'est le déterminant de trois vecteurs, et il mesure des volumes.

> **Propriété** — « L'espace est muni d'un repère orthonormé direct (O, i⃗, j⃗, k⃗). Pour tous vecteurs u⃗, v⃗ et w⃗, (u⃗∧v⃗).w⃗ = (w⃗∧u⃗).v⃗ = (v⃗∧w⃗).u⃗ = det(u⃗, v⃗, w⃗). »

La permutation **circulaire** ne change rien ; échanger deux vecteurs change le signe. Et le déterminant est nul si et seulement si les trois vecteurs sont **coplanaires** — c'est le test de coplanarité de tout le chapitre.

> **Aires** — « L'aire du parallélogramme ABCD est égale à ‖AB⃗∧AD⃗‖. L'aire du triangle ABD est égale à (1/2)‖AB⃗∧AD⃗‖. »

> **Volume d'un tétraèdre** — « Le volume d'un tétraèdre ABCD est égal à (1/6)|(BC⃗∧BD⃗).BA⃗|. »

> **Théorème** — « Le volume d'un parallélépipède ABCDEFGH est égal à |(AB⃗∧AD⃗).AE⃗|. »

::: figure Le volume du parallélépipède, c'est l'aire de la base ABCD — égale à ‖AB⃗∧AD⃗‖ — multipliée par la hauteur h ; le produit mixte |(AB⃗∧AD⃗).AE⃗| fait exactement ce produit en une seule opération.
<svg viewBox="0 0 258 222"><path d="M45 195 L143 195 L193.4 174 L95.4 174 Z" fill="#0f6e56" opacity="0.14"/><path d="M45 195 L143 195 M143 195 L193.4 174 M193.4 174 L230.5 91.8 M230.5 91.8 L132.5 91.8 M132.5 91.8 L82.1 112.8 M82.1 112.8 L45 195 M143 195 L180.1 112.8 M180.1 112.8 L82.1 112.8 M180.1 112.8 L230.5 91.8" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><path d="M45 195 L95.4 174 M95.4 174 L193.4 174 M95.4 174 L132.5 91.8" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-dasharray="5 4"/><path d="M82.1 112.8 L82.1 189.8" fill="none" stroke="#b45309" stroke-width="1.8" stroke-dasharray="4 3"/><path d="M45 195 L45 133" fill="none" stroke="#0f6e56" stroke-width="2.6"/><path d="M45 125 l-6 11 l12 0 z" fill="#0f6e56"/><g fill="#0f172a"><circle cx="45" cy="195" r="3.5"/><circle cx="143" cy="195" r="3.5"/><circle cx="193.4" cy="174" r="3.5"/><circle cx="82.1" cy="112.8" r="3.5"/><circle cx="180.1" cy="112.8" r="3.5"/><circle cx="230.5" cy="91.8" r="3.5"/><circle cx="132.5" cy="91.8" r="3.5"/></g><circle cx="95.4" cy="174" r="3.5" fill="#94a3b8"/><g font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="36" y="211" text-anchor="middle" fill="#0f172a">A</text><text x="147" y="212" text-anchor="middle" fill="#0f172a">B</text><text x="204" y="185" text-anchor="middle" fill="#0f172a">C</text><text x="86" y="167" text-anchor="middle" fill="#94a3b8">D</text><text x="71" y="107" text-anchor="middle" fill="#0f172a">E</text><text x="189" y="107" text-anchor="middle" fill="#0f172a">F</text><text x="241" y="86" text-anchor="middle" fill="#0f172a">G</text><text x="127" y="82" text-anchor="middle" fill="#0f172a">H</text><text x="33" y="122" text-anchor="middle" fill="#0f6e56">n⃗</text><text x="92" y="155" text-anchor="middle" fill="#b45309">h</text></g></svg>
:::

_Exemple détaillé (aire)_ — cube d'arête 1, repère (A, AB⃗, AD⃗, AE⃗) ; I, J, K et L sont les centres des faces ABFE, BCGF, CDHG et ADHE. En moyennant les quatre sommets de chaque face : I(1/2, 0, 1/2), J(1, 1/2, 1/2), K(1/2, 1, 1/2), L(0, 1/2, 1/2). Alors IJ⃗ = (1/2, 1/2, 0) et IL⃗ = (−1/2, 1/2, 0), donc :

$$ IJ⃗∧IL⃗ = ((1/2)(0) − (0)(1/2) ; (0)(−1/2) − (1/2)(0) ; (1/2)(1/2) − (1/2)(−1/2)) = (0, 0, 1/2) $$

_Contrôle_ — (0, 0, 1/2).IJ⃗ = 0 ✓ et (0, 0, 1/2).IL⃗ = 0 ✓. L'aire de IJKL vaut donc ‖(0, 0, 1/2)‖ = **1/2**, et celle du triangle IJK **1/4**. _Second contrôle, par une autre route_ — LK⃗ = K − L = (1/2, 1/2, 0) = IJ⃗, donc IJKL est bien un parallélogramme ; de plus ‖IJ⃗‖ = ‖IL⃗‖ = √2/2 et IJ⃗.IL⃗ = −1/4 + 1/4 + 0 = 0 : c'est un **carré** de côté √2/2, d'aire (√2/2)² = 1/2 ✓. Les deux méthodes concordent.

_Exemple détaillé (volume)_ — tétraèdre ABCD avec A(0, 0, 0), B(2, 0, 0), C(0, 3, 0), D(0, 0, 4). On applique la formule à la lettre : BC⃗ = (−2, 3, 0), BD⃗ = (−2, 0, 4), BA⃗ = (−2, 0, 0).

$$ BC⃗∧BD⃗ = ((3)(4) − (0)(0) ; (0)(−2) − (−2)(4) ; (−2)(0) − (3)(−2)) = (12, 8, 6) $$

_Contrôle_ — (12, 8, 6).BC⃗ = −24 + 24 + 0 = 0 ✓ et (12, 8, 6).BD⃗ = −24 + 0 + 24 = 0 ✓. Puis (BC⃗∧BD⃗).BA⃗ = −24, d'où V = (1/6)·24 = **4**. _Contrôle par une seconde méthode_ — la base ABC est le triangle rectangle en A de côtés 2 et 3, d'aire 3 ; la hauteur issue de D vaut 4 car (AD) ⊥ (ABC) ; donc V = (1/3)·3·4 = 4 ✓.

> 🗡️ Le produit mixte est **signé** : le déterminant peut sortir négatif. Les formules d'aire et de volume prennent toujours une **valeur absolue** ou une **norme**. Un volume négatif est le signe qu'on a oublié les barres, pas que la figure est retournée.

## 📐 Droites, plans, sphères : leurs équations

**Une droite se paramètre.** Elle est décrite par un point et un vecteur directeur.

> **Représentation paramétrique** — « Soit A un point, u⃗ un vecteur non nul et D la droite passant par A et de vecteur directeur u⃗. Alors D(A, u⃗) = {M ; AM⃗ = αu⃗, où α est un réel}. »

En coordonnées, avec A(x₀, y₀, z₀) et u⃗(a, b, c), cela donne le système paramétré, α parcourant ℝ :

$$ x = x₀ + αa ; y = y₀ + αb ; z = z₀ + αc $$

**Un plan a une équation cartésienne.**

> **Plan par un point et deux vecteurs** — « Soit A un point, u⃗ et v⃗ deux vecteurs non colinéaires et P le plan passant par A et de vecteurs directeurs u⃗ et v⃗. Alors P(A, u⃗, v⃗) = {M ; det(AM⃗, u⃗, v⃗) = 0}. »

En repère orthonormé, cette condition s'écrit (u⃗∧v⃗).AM⃗ = 0 : le vecteur n⃗ = u⃗∧v⃗ est **normal** au plan, et le plan devient l'ensemble des M tels que n⃗.AM⃗ = 0, c'est-à-dire **ax + by + cz + d = 0** avec n⃗(a, b, c). Réciproquement, toute équation ax + by + cz + d = 0 avec (a, b, c) ≠ (0, 0, 0) est celle d'un plan de vecteur normal (a, b, c). **C'est la clé de lecture la plus rentable du chapitre : les coefficients de l'équation sont les coordonnées d'un vecteur normal.**

_Exemple détaillé_ — A(2, 0, −1), B(1, −1, 0), C(0, 1, 4). On a AB⃗ = (−1, −1, 1) et AC⃗ = (−2, 1, 5), donc :

$$ AB⃗∧AC⃗ = ((−1)(5) − (1)(1) ; (1)(−2) − (−1)(5) ; (−1)(1) − (−1)(−2)) = (−6, 3, −3) $$

_Contrôle_ — (−6, 3, −3).AB⃗ = 6 − 3 − 3 = 0 ✓ et (−6, 3, −3).AC⃗ = 12 + 3 − 15 = 0 ✓. Ce vecteur est non nul, donc A, B et C ne sont **pas alignés**. On simplifie par −3 : n⃗(2, −1, 1) est encore normal. L'équation est 2x − y + z + d = 0 ; en y injectant A(2, 0, −1) : 4 − 0 − 1 + d = 0, donc d = −3.

$$ (ABC) : 2x − y + z − 3 = 0 $$

_Contrôle sur les deux autres points_ — B(1, −1, 0) : 2 + 1 + 0 − 3 = 0 ✓. C(0, 1, 4) : 0 − 1 + 4 − 3 = 0 ✓.

**Une sphère aussi a une équation.**

> **Sphère** — « Soit A un point, R un réel strictement positif et S la sphère de centre A et de rayon R. Alors S = {M ; AM = R}. »

En repère orthonormé, avec A(x₀, y₀, z₀), cela s'écrit (x − x₀)² + (y − y₀)² + (z − z₀)² = R². Une équation développée du type x² + y² + z² + ax + by + cz + d = 0 se ramène à cette forme en **complétant les trois carrés** ; on obtient une sphère si et seulement si le second membre obtenu est strictement positif.

_Exemple détaillé_ — S : x² + y² + z² + 2x − 4y + 2z = 3. On regroupe : (x + 1)² − 1 + (y − 2)² − 4 + (z + 1)² − 1 = 3, donc (x + 1)² + (y − 2)² + (z + 1)² = 9. C'est la sphère de **centre I(−1, 2, −1) et de rayon R = 3**. _Contrôle_ — le point A(−3, 1, 1) : 4 + 1 + 4 = 9 ✓, il appartient bien à S.

> ⚠️ Une droite de l'espace **n'a pas** d'équation cartésienne unique : ax + by + cz + d = 0 décrit un **plan**. Une droite se donne soit en paramétrique, soit comme **intersection de deux plans** (un système de deux équations).

## 🔮 Distances, tangence, positions relatives

> **Distance d'un point à un plan** — « Soit un plan P d'équation ax + by + cz + d = 0 et A(x₀, y₀, z₀) un point de l'espace. La distance de A à P est le réel, noté d(A, P), égal à |ax₀ + by₀ + cz₀ + d| / √(a² + b² + c²). »

::: figure La distance de M au plan P ne se mesure pas dans n'importe quelle direction : c'est la longueur MH le long de la normale n⃗ — la plus courte de toutes.
<svg viewBox="0 0 250 198"><path d="M30 170 L186 170 L227.6 146 L71.6 146 Z" fill="#0f6e56" opacity="0.12"/><path d="M30 170 L186 170 L227.6 146 L71.6 146 Z" fill="none" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round"/><path d="M120.2 81.5 L120.2 159.5" fill="none" stroke="#b45309" stroke-width="2.2" stroke-dasharray="5 4"/><path d="M120.2 159.5 L130.2 159.5 L130.2 149.5" fill="none" stroke="#b45309" stroke-width="1.5"/><path d="M181.2 152 L181.2 110" fill="none" stroke="#0f6e56" stroke-width="2.6"/><path d="M181.2 102 l-6 11 l12 0 z" fill="#0f6e56"/><circle cx="120.2" cy="81.5" r="4" fill="#0f172a"/><circle cx="120.2" cy="159.5" r="4" fill="#b45309"/><circle cx="181.2" cy="152" r="3" fill="#0f6e56"/><g font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="120" y="70" text-anchor="middle" fill="#0f172a">M</text><text x="108" y="176" text-anchor="middle" fill="#b45309">H</text><text x="88" y="120" text-anchor="middle" fill="#b45309">d(M, P)</text><text x="194" y="112" text-anchor="middle" fill="#0f6e56">n⃗</text><text x="203" y="180" text-anchor="middle" fill="#0f172a">P</text></g></svg>
:::

_Exemple détaillé_ — P : 2x − y + z − 3 = 0 et M(1, 1, 1). Alors d(M, P) = |2 − 1 + 1 − 3| / √(4 + 1 + 1) = 1/√6 = **√6/6 ≈ 0.408**. _Contrôle par une seconde méthode (le projeté)_ — le projeté H de M sur P s'obtient en descendant le long de n⃗(2, −1, 1) : H = M − t·n⃗ avec t = (2 − 1 + 1 − 3)/6 = −1/6, donc H = (1, 1, 1) + (1/6)(2, −1, 1) = (4/3, 5/6, 7/6). Vérifions que H est bien sur P : 8/3 − 5/6 + 7/6 − 3 = 8/3 + 2/6 − 3 = 3 − 3 = 0 ✓. Et MH = ‖(1/3, −1/6, 1/6)‖ = √(4/36 + 1/36 + 1/36) = √6/6 ✓. Même résultat par deux chemins.

> **Distance d'un point à une droite** — « Soit D une droite de vecteur directeur u⃗ et A un point de D. La distance d'un point M de l'espace à la droite D est le réel d(M, D) = ‖MA⃗∧u⃗‖ / ‖u⃗‖. »

::: figure Le parallélogramme bâti sur MA⃗ et u⃗ a pour aire ‖MA⃗∧u⃗‖ ; sa base mesure ‖u⃗‖, donc sa hauteur — la distance de M à la droite — est le quotient des deux.
<svg viewBox="0 0 265 185"><path d="M111.3 133.1 L30 150 L144.4 150 L225.7 133.1 Z" fill="#0f6e56" opacity="0.14"/><path d="M111.3 133.1 L30 150 L144.4 150 L225.7 133.1 Z" fill="none" stroke="#0f172a" stroke-width="1.3"/><path d="M12 150 L250 150" fill="none" stroke="#0f172a" stroke-width="2"/><path d="M111.3 133.1 L38 148.3" fill="none" stroke="#0f172a" stroke-width="2.2"/><path d="M30 150 l10 -5 l1 9 z" fill="#0f172a"/><path d="M30 150 L136 150" fill="none" stroke="#0f6e56" stroke-width="3"/><path d="M144.4 150 l-11 -5 l0 10 z" fill="#0f6e56"/><path d="M111.3 133.1 L82 150" fill="none" stroke="#b45309" stroke-width="2" stroke-dasharray="5 4"/><g fill="#0f172a"><circle cx="30" cy="150" r="4"/><circle cx="111.3" cy="133.1" r="4"/></g><circle cx="82" cy="150" r="3.5" fill="#b45309"/><g font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="24" y="166" text-anchor="middle" fill="#0f172a">A</text><text x="111" y="123" text-anchor="middle" fill="#0f172a">M</text><text x="74" y="167" text-anchor="middle" fill="#b45309">H</text><text x="120" y="167" text-anchor="middle" fill="#0f6e56">u⃗</text><text x="62" y="130" text-anchor="middle" fill="#0f172a">MA⃗</text><text x="243" y="143" text-anchor="middle" fill="#0f172a">D</text></g></svg>
:::

_Exemple détaillé_ — D passe par A(1, 0, 0) et a pour vecteur directeur u⃗(0, 1, 1) ; M(2, 1, 0). Alors MA⃗ = A − M = (−1, −1, 0) et :

$$ MA⃗∧u⃗ = ((−1)(1) − (0)(1) ; (0)(0) − (−1)(1) ; (−1)(1) − (−1)(0)) = (−1, 1, −1) $$

_Contrôle_ — (−1, 1, −1).MA⃗ = 1 − 1 + 0 = 0 ✓ et (−1, 1, −1).u⃗ = 0 + 1 − 1 = 0 ✓. D'où d(M, D) = √3/√2 = **√6/2 ≈ 1.225**. _Contrôle par une seconde méthode (le projeté)_ — un point courant de D s'écrit P(1, t, t) ; MP⃗ = (−1, t − 1, t) est orthogonal à u⃗ quand (t − 1) + t = 0, soit t = 1/2. Alors MP⃗ = (−1, −1/2, 1/2) et ‖MP⃗‖ = √(1 + 1/4 + 1/4) = √(3/2) = √6/2 ✓.

**Sphère et plan.**

> **Théorème** — « Soit S une sphère de centre A et de rayon R. Soit P un plan, h la distance de A à P et H le projeté orthogonal de A sur P. L'intersection de S et P est • vide si h > R, • réduite au singleton {H} si h = R, • le cercle de rayon √(R² − h²) et de centre H si h < R. »

::: figure Vue en coupe (par le plan qui contient I et qui est perpendiculaire à P) — pas une perspective : le triangle rectangle en H donne d'un coup la relation R² = h² + r², donc le rayon r du cercle de section.
<svg viewBox="0 0 230 200"><circle cx="130" cy="105" r="70" fill="#0f6e56" opacity="0.10"/><circle cx="130" cy="105" r="70" fill="none" stroke="#0f172a" stroke-width="2"/><path d="M45 75 L215 75" fill="none" stroke="#0f172a" stroke-width="1.8"/><path d="M66.75 75 L193.25 75" fill="none" stroke="#0f6e56" stroke-width="3.4"/><path d="M130 105 L130 75" fill="none" stroke="#b45309" stroke-width="2.2"/><path d="M130 105 L193.25 75" fill="none" stroke="#0f172a" stroke-width="1.8" stroke-dasharray="5 4"/><path d="M130 85 L140 85 L140 75" fill="none" stroke="#b45309" stroke-width="1.5"/><g fill="#0f172a"><circle cx="130" cy="105" r="4"/><circle cx="193.25" cy="75" r="3.5"/></g><circle cx="130" cy="75" r="4" fill="#b45309"/><g font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="118" y="115" text-anchor="middle" fill="#0f172a">I</text><text x="124" y="65" text-anchor="middle" fill="#b45309">H</text><text x="141" y="97" text-anchor="middle" fill="#b45309">h</text><text x="171" y="99" text-anchor="middle" fill="#0f172a">R</text><text x="163" y="66" text-anchor="middle" fill="#0f6e56">r</text><text x="224" y="68" text-anchor="middle" fill="#0f172a">P</text><text x="130" y="192" text-anchor="middle" fill="#0f172a">S</text></g></svg>
:::

Le cas h = R est celui du **plan tangent**. Un plan tangent en un point A de la sphère est le plan passant par A et de vecteur normal **IA⃗**, où I est le centre.

_Exemple détaillé_ — S : centre I(−1, 2, −1), R = 3 ; A(−3, 1, 1) est sur S (vu plus haut). Le plan tangent en A a pour normale IA⃗ = (−2, −1, 2), d'où −2(x + 3) − (y − 1) + 2(z − 1) = 0, soit **2x + y − 2z + 7 = 0**. _Contrôle n° 1 (A appartient au plan)_ — 2(−3) + 1 − 2(1) + 7 = −6 + 1 − 2 + 7 = 0 ✓. _Contrôle n° 2 (la tangence)_ — d(I, plan) = |2(−1) + 2 − 2(−1) + 7| / √(4 + 1 + 4) = 9/3 = 3 = R ✓.

_Exemple détaillé (une section)_ — même sphère S, et le plan Q : 2x + y − 2z + 1 = 0. Alors h = d(I, Q) = |−2 + 2 + 2 + 1|/3 = 1 < 3 : l'intersection est un **cercle de rayon √(9 − 1) = 2√2**. Son centre est le projeté H de I sur Q : H = I − t·n⃗ avec t = 3/9 = 1/3 et n⃗(2, 1, −2), donc H = (−1 − 2/3, 2 − 1/3, −1 + 2/3) = (−5/3, 5/3, −1/3). _Contrôle_ — H dans Q : −10/3 + 5/3 + 2/3 + 3/3 = 0 ✓ ; et IH = ‖(−2/3, −1/3, 2/3)‖ = √(9/9) = 1 = h ✓.

**Positions relatives.** Deux droites de vecteurs directeurs u⃗ et v⃗, passant par A et B, sont **coplanaires** si et seulement si det(AB⃗, u⃗, v⃗) = 0. Elles sont alors parallèles si u⃗ et v⃗ sont colinéaires, sécantes sinon. Si le déterminant est non nul, elles ne sont **ni parallèles ni sécantes** : elles ne sont pas coplanaires, situation qui n'existe pas dans le plan.

_Exemple détaillé_ — D : (1 − α, 2 + α, −α) et Δ : (−β, 3, β). D passe par A(1, 2, 0) et a pour directeur u⃗(−1, 1, −1) ; Δ passe par B(0, 3, 0) et a pour directeur v⃗(−1, 0, 1). On calcule u⃗∧v⃗ = ((1)(1) − (−1)(0) ; (−1)(−1) − (−1)(1) ; (−1)(0) − (1)(−1)) = (1, 2, 1). _Contrôle_ — (1, 2, 1).u⃗ = −1 + 2 − 1 = 0 ✓ et (1, 2, 1).v⃗ = −1 + 0 + 1 = 0 ✓. Puis AB⃗ = (−1, 1, 0) et det = (u⃗∧v⃗).AB⃗ = −1 + 2 + 0 = **1 ≠ 0** : les droites **ne sont pas coplanaires**.

_Exemple détaillé (une intersection)_ — A(0, −1, 1), B(2, 1, 3) et Δ : (α, −2 + 2α, 1 + α). Le vecteur AB⃗ = (2, 2, 2) donne le directeur (1, 1, 1), donc (AB) : (t, −1 + t, 1 + t). Les directeurs (1, 1, 1) et (1, 2, 1) ne sont pas colinéaires. On résout : t = α et −1 + t = −2 + 2α donnent α = 1, et la troisième ligne 1 + t = 1 + α est alors satisfaite. **Les droites sont sécantes en I(1, 0, 2).** _Contrôle_ — sur (AB) avec t = 1 : (1, 0, 2) ✓ ; sur Δ avec α = 1 : (1, −2 + 2, 1 + 1) = (1, 0, 2) ✓.

> ⚠️ Dans l'espace, « non parallèles » n'entraîne **pas** « sécantes ». Avant d'écrire qu'un point d'intersection existe, il faut résoudre le système **complet** — les trois lignes — et vérifier que la troisième est compatible avec les deux premières.

## 🛡️ La translation de l'espace

> **Définition** — « Soit u⃗ un vecteur de l'espace. L'application qui à tout point M de l'espace associe l'unique point M′ tel que MM′⃗ = u⃗ est appelée translation de vecteur u⃗ et notée t_u⃗. Pour tous points M et M′ de l'espace, t_u⃗(M) = M′ équivaut à MM′⃗ = u⃗. »

> **Théorème** — « Toute translation de l'espace de vecteur u⃗ est bijective. Son application réciproque est la translation de vecteur −u⃗. »

> **Propriété caractéristique** — « Une application de l'espace dans lui-même est une translation, si et seulement si, pour tous points M et N d'images respectives M′ et N′, M′N′⃗ = MN⃗. »

C'est ce critère qui sert à **reconnaître** une translation cachée derrière une définition vectorielle : on calcule M′N′⃗ et on regarde s'il vaut MN⃗.

> **Conséquences et images** — « Toute translation conserve la distance et le produit scalaire. L'image d'une droite est une droite qui lui est parallèle ; l'image d'un plan est un plan qui lui est parallèle. Toute translation conserve le parallélisme, l'orthogonalité et le milieu. L'image d'une sphère S est une sphère S′ de même rayon et de centre l'image du centre. »

> **Invariance globale** — « Soit Γ une partie de l'espace. On dit que Γ est globalement invariante par une application f lorsque f(Γ) = Γ. »

> **Expression analytique** — « Soit u⃗(a, b, c). Si M(x, y, z) a pour image M′(x′, y′, z′) par t_u⃗, alors x′ = x + a ; y′ = y + b ; z′ = z + c. Réciproquement, l'application définie par ce système est la translation de vecteur u⃗(a, b, c). »

_Exemple détaillé_ — le plan P : x − z = 0 et la translation t de vecteur u⃗(−1, 0, 1). Pour trouver P′ = t(P), on **inverse** l'expression analytique : de x′ = x − 1 et z′ = z + 1 on tire x = x′ + 1 et z = z′ − 1 ; on injecte dans l'équation de P : (x′ + 1) − (z′ − 1) = 0, soit **P′ : x − z + 2 = 0**. _Contrôle sur deux points_ — O(0, 0, 0) ∈ P a pour image (−1, 0, 1), et −1 − 1 + 2 = 0 ✓ ; A(1, 4, 1) ∈ P (car 1 − 1 = 0) a pour image A′(0, 4, 2), et 0 − 2 + 2 = 0 ✓. Le plan image est bien **parallèle** à P : ils ont le même vecteur normal (1, 0, −1) ✓.

_Suite — une tangence conservée._ Soit S la sphère de centre A(1, 4, 1) et de rayon √2. Est-ce que P′ est tangent à S en A′ ? On calcule d(A, P′) = |1 − 1 + 2| / √2 = 2/√2 = √2 = R ✓ : le plan P′ est bien tangent à S. _Contrôle du point de contact_ — le projeté de A sur P′ est A − t·n⃗ avec n⃗(1, 0, −1) et t = (1 − 1 + 2)/2 = 1, soit (1, 4, 1) − (1, 0, −1) = (0, 4, 2) = A′ ✓.

> 🗡️ Pour l'image d'une surface par une transformation, ne cherche jamais l'équation « en avançant ». Écris les **anciennes** coordonnées en fonction des **nouvelles**, puis substitue. C'est la même méthode pour une translation et pour une homothétie.

## 👑 L'homothétie de l'espace

> **Définition** — « Soit I un point de l'espace et k un réel non nul. L'application qui à tout point M associe l'unique point M′ tel que IM′⃗ = k IM⃗ est appelée homothétie de centre I et de rapport k, notée h_(I,k). »

> **Théorème** — « Toute homothétie de centre I et de rapport non nul k est une bijection de l'espace et admet pour réciproque l'homothétie de centre I et de rapport 1/k. »

> **Propriété caractéristique** — « Soit f une application de l'espace dans lui-même et k un réel non nul et différent de 1. f est une homothétie de rapport k, si et seulement si, pour tous points M et N d'images respectives M′ et N′, M′N′⃗ = k MN⃗. Conséquence : M′N′ = |k| MN. »

Une homothétie **ne conserve pas** les distances (sauf si |k| = 1) : elle les multiplie par |k|. Les aires sont donc multipliées par k², et les **volumes par |k|³**.

> **Images** — « L'image d'une droite par une homothétie est une droite qui lui est parallèle ; l'image d'un plan est un plan qui lui est parallèle. Toute homothétie conserve le parallélisme, l'orthogonalité et le milieu. L'image d'une sphère de centre I₀ et de rayon R est la sphère de centre l'image de I₀ et de rayon |k|R. Toute homothétie de l'espace conserve le contact. »

> **Expression analytique** — « Soit I(a, b, c) et k ≠ 0, k ≠ 1. Si M(x, y, z) a pour image M′(x′, y′, z′) par h_(I,k), alors x′ = kx + (1 − k)a ; y′ = ky + (1 − k)b ; z′ = kz + (1 − k)c. Réciproquement, l'application définie par x′ = kx + α ; y′ = ky + β ; z′ = kz + δ, avec k ≠ 1, est l'homothétie de rapport k et de centre I(α/(1 − k), β/(1 − k), δ/(1 − k)). »

_Exemple détaillé_ — I(1, −1, 2), k = 3. Comme 1 − k = −2, l'expression analytique est x′ = 3x − 2 ; y′ = 3y + 2 ; z′ = 3z − 4. _Contrôle_ — le centre doit être fixe : 3(1) − 2 = 1 ✓, 3(−1) + 2 = −1 ✓, 3(2) − 4 = 2 ✓.

Cherchons l'image R du plan Q : x + y − 1 = 0. On inverse : x = (x′ + 2)/3, y = (y′ − 2)/3. On substitue : (x′ + 2)/3 + (y′ − 2)/3 − 1 = 0, soit (x′ + y′)/3 = 1, donc **R : x + y − 3 = 0**. _Contrôle sur deux points_ — (1, 0, 0) ∈ Q a pour image (1, 2, −4), et 1 + 2 − 3 = 0 ✓ ; (0, 1, 5) ∈ Q a pour image (−2, 5, 11), et −2 + 5 − 3 = 0 ✓. Et R est bien **parallèle** à Q : même vecteur normal (1, 1, 0) ✓.

_Cas remarquable_ — le plan P : x − y + z − 4 = 0 contient le centre I, car 1 + 1 + 2 − 4 = 0 ✓. Son image est un plan parallèle à P passant par h(I) = I : c'est **P lui-même**. Un plan est globalement invariant par toutes les homothéties de centre I si et seulement si il contient I.

_Exemple détaillé (une sphère)_ — S : x² + y² + z² − 2x − 4y − 2z + 2 = 0. En complétant les carrés : (x − 1)² + (y − 2)² + (z − 1)² = 1 + 4 + 1 − 2 = 4, donc centre I₀(1, 2, 1) et R = 2. Son intersection avec le plan (O, i⃗, j⃗), d'équation z = 0, se trouve à la distance h = 1 < 2 du centre : c'est le **cercle de centre (1, 2, 0) et de rayon √(4 − 1) = √3**. _Contrôle direct_ — en posant z = 0 dans l'équation : (x − 1)² + (y − 2)² + 1 = 4, soit (x − 1)² + (y − 2)² = 3 ✓.

Appliquons maintenant h de centre Ω(1, 1, 0) et de rapport −3/2. Le nouveau centre est I₀′ = Ω + k·ΩI₀⃗ = (1, 1, 0) + (−3/2)(0, 1, 1) = **(1, −1/2, −3/2)**, et le rayon devient R′ = |−3/2|·2 = **3**. L'intersection de S′ avec z = 0 : h′ = 3/2 < 3, donc un cercle de rayon √(9 − 9/4) = √(27/4) = **3√3/2**, centré en (1, −1/2, 0). _Contrôle par une seconde méthode_ — l'homothétie multiplie toutes les longueurs par |k| = 3/2 ; le cercle de départ, de rayon √3, doit donc donner un cercle de rayon (3/2)√3 = 3√3/2 ✓. Les deux calculs concordent.

> ⚠️ Une homothétie de rapport k multiplie les **longueurs** par |k|, les **aires** par k², les **volumes** par |k|³ — jamais tout par k. L'image d'un cube d'arête a par une homothétie de rapport a est un cube d'arête a², donc de volume a⁶ : le piège classique consiste à écrire a³.

> 🏆 Quinzième porte franchie, héros : tu sais désormais poser un repère sur un cube, dresser une normale d'un seul produit vectoriel, transformer une aire ou un volume en déterminant, écrire les équations d'une droite, d'un plan et d'une sphère, et faire glisser ou dilater tout ça sans jamais perdre le contrôle. Et surtout, tu as pris l'habitude qui sauve à l'examen : **tout produit vectoriel se vérifie par deux produits scalaires nuls, toute distance se recoupe par une seconde méthode**. Au chapitre suivant, on quitte l'espace pour les entiers — divisibilité, congruences et nombres premiers t'attendent dans ℤ.
