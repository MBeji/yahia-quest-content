# 📜 Résumé : Translations

- **Application du plan dans le plan** : associer à tout point M un **seul** point M' définit une application f : P → P, M ↦ M'. M' est l'**image** de M, M est l'**antécédent** de M'. Exemples déjà connus : symétrie centrale, symétrie orthogonale, quart de tour direct, quart de tour indirect.
- **Définition (translation)** : pour un vecteur u⃗ donné, la **translation de vecteur u⃗**, notée t_u⃗, associe à tout point M l'unique point M' tel que **MM'⃗ = u⃗**. Autrement dit **t_u⃗(M) = M' ⟺ MM'⃗ = u⃗**. Le vecteur se lit de l'antécédent vers l'image, jamais l'inverse. Tout point admet **un seul** antécédent.
- **Deux symétries centrales** : la symétrie de centre I suivie de la symétrie de centre J est la **translation de vecteur 2IJ⃗** (MM'⃗ = 2MI⃗ + 2M₁J⃗ = 2IJ⃗, indépendant de M).
- **Propriété caractéristique** : **f est une translation ⟺ M'N'⃗ = MN⃗ pour tous points M et N**. Conséquences immédiates : MN = M'N' (les distances sont conservées), (MN) ∥ (M'N') (le parallélisme est conservé), et MM'N'N est un **parallélogramme** si les quatre points ne sont pas alignés.
::: figure Toute la carte de révision tient dans cette image : les deux flèches grises sont le même vecteur u⃗, et le segment image se déduit du segment de départ sans la moindre déformation — donc M'N'⃗ = MN⃗
<svg viewBox="0 0 260 140">
<path d="M40 45 L85 105" fill="none" stroke="#0f172a" stroke-width="2.2"/>
<path d="M150 35 L195 95" fill="none" stroke="#0f6e56" stroke-width="2.6"/>
<g fill="none" stroke="#94a3b8" stroke-width="1.8" stroke-dasharray="6 4"><path d="M40 45 L140 35.9"/><path d="M85 105 L185 95.9"/></g>
<g fill="#94a3b8"><polygon points="150,35 140.4,39.9 139.7,31.9"/><polygon points="195,95 185.4,99.9 184.7,91.9"/></g>
<g fill="#0f172a"><circle cx="40" cy="45" r="4.5"/><circle cx="85" cy="105" r="4.5"/></g>
<g fill="#0f6e56"><circle cx="150" cy="35" r="4.5"/><circle cx="195" cy="95" r="4.5"/></g>
<g font-size="14" font-weight="700" text-anchor="middle" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">
<text x="28" y="38" fill="#0f172a">M</text>
<text x="73" y="120" fill="#0f172a">N</text>
<text x="160" y="28" fill="#0f6e56">M'</text>
<text x="208" y="106" fill="#0f6e56">N'</text>
</g>
</svg>
:::

- **Reconnaître une translation cachée** : si MM'⃗ est une somme pondérée dont les **coefficients totalisent 0**, cette somme est un vecteur **constant**, donc l'application est une translation. Exemples : MM'⃗ = MA⃗ + MB⃗ − 2MC⃗ = **CA⃗ + CB⃗** ; AN⃗ = 3AM⃗ − 2BM⃗ donne MN⃗ = **2BA⃗**.
- **Conservations** : une translation conserve les **distances**, les **angles**, l'**alignement**, le **milieu**, le **barycentre** (mêmes coefficients sur les points images), le **parallélisme**, l'**orthogonalité** et le **contact** (une tangente reste tangente). L'image d'un polygone est un polygone qui lui est **superposable** — même périmètre, mêmes angles, quel que soit u⃗.
- **Images des objets usuels** : une droite D → une **droite parallèle** à D ; un segment [AB] → le segment [A'B'] **de même longueur** ; une demi-droite → une demi-droite ; un cercle de centre O et de rayon r → le cercle de **même rayon** r centré en l'image de O. Le rayon ne change jamais : seul le centre voyage.
- **Médiatrice** : milieu conservé + orthogonalité conservée ⟹ l'image de la médiatrice de [AB] est la **médiatrice de [A'B']**.
- **Problèmes de lieux** : on cherche l'**ensemble des points** (le **lieu géométrique**) vérifiant une condition. Méthode en trois temps : **phase expérimentale**, **conjecture**, **démonstration**. Exemple : si M décrit un cercle de centre O et de rayon 4 cm et si MN⃗ = u⃗ est fixe, alors N décrit le cercle de rayon 4 cm centré en l'image de O.
- **Problèmes de construction** : méthode **analyse/synthèse** — on *suppose le problème résolu*, on lit la translation qui relie les inconnues, on trace, on vérifie. Exemple : pour ABMN parallélogramme avec M sur D et N sur Δ, AB⃗ = NM⃗ donne M à l'intersection de D et de **l'image de Δ** par la translation de vecteur AB⃗.
- **Triangle des milieux** : si K et J sont les milieux de [AB] et [AC], alors **KJ⃗ = ½BC⃗**, donc la translation de vecteur KJ⃗ envoie B sur le milieu de [BC].
- **Problème du pont** : deux berges parallèles, un pont [MN] perpendiculaire donc de vecteur MN⃗ **fixe**. On translate A du vecteur MN⃗ en A' ; alors AM = A'N et le trajet minimal s'obtient pour N à l'intersection de [A'B] avec la berge opposée.
- **Math et culture — pavages** : paver, c'est couvrir le plan sans trou ni chevauchement. Seuls le **triangle équilatéral** (60°), le **carré** (90°) et l'**hexagone régulier** (120°) pavent seuls, car les angles réunis en un sommet doivent totaliser **360°** — ce qu'interdisent les 108° du pentagone régulier.
