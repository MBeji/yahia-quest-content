# ⚔️ Produit scalaire et produit vectoriel dans l'espace — mesurer l'espace par le calcul

> 💡 «Le produit scalaire dit si deux directions sont perpendiculaires ; le produit vectoriel fabrique la direction perpendiculaire à deux autres, et mesure au passage une aire.»

Ce chapitre arme l'espace de deux outils de calcul. On rappelle d'abord le déterminant de trois vecteurs et le produit scalaire, puis on oriente l'espace : c'est ce qui permet de définir le produit vectoriel, d'en tirer une aire, une distance et, avec le déterminant, un volume. Huit notions. Sauf mention contraire, l'espace est rapporté à un repère orthonormé direct (O, i⃗, j⃗, k⃗), terme précisé dans la troisième notion.

## 🧮 Le déterminant de trois vecteurs et la coplanarité

Sur un dessin, un point peut sembler flotter au-dessus du plan de trois autres sans qu'on puisse le vérifier à l'œil. Comment trancher, à partir des seules coordonnées, si quatre points A, B, C, D sont dans un même plan ?
Existe-t-il un nombre qui vaut 0 exactement quand ils le sont ?

::: definition
Soit 𝓑 une base de l'espace, et u⃗(a ; b ; c), v⃗(a′ ; b′ ; c′), w⃗(a″ ; b″ ; c″) trois vecteurs. Le **déterminant** de (u⃗, v⃗, w⃗) dans la base 𝓑 est le réel :
$$ det(u⃗, v⃗, w⃗) = a(b′c″ − c′b″) − b(a′c″ − c′a″) + c(a′b″ − b′a″) $$
:::

::: exemple Quatre points sont-ils coplanaires ?

Dans un repère de l'espace, on donne A(1 ; 2 ; 0), B(0 ; −1 ; 1), C(−1 ; 0 ; 2), D(0 ; 1 ; 0) et E(1 ; 2 ; −2). On étudie d'abord A, B, C, D.

1. On forme trois vecteurs issus du même point A : AB⃗(−1 ; −3 ; 1), AC⃗(−2 ; −2 ; 2) et AD⃗(−1 ; −1 ; 0).
2. Les trois parenthèses valent b′c″ − c′b″ = (−2) × 0 − 2 × (−1) = 2, puis a′c″ − c′a″ = (−2) × 0 − 2 × (−1) = 2, puis a′b″ − b′a″ = (−2)(−1) − (−2)(−1) = 0.
3. Donc det(AB⃗, AC⃗, AD⃗) = (−1) × 2 − (−3) × 2 + 1 × 0 = 4. Ce nombre est non nul : A, B, C, D ne sont pas coplanaires.
4. Pour B, C, D, E, on part de B : BC⃗(−1 ; 1 ; 1), BD⃗(0 ; 2 ; −1) et BE⃗(1 ; 3 ; −3). Les parenthèses valent −3, 1 et −2, d'où det(BC⃗, BD⃗, BE⃗) = (−1)(−3) − 1 × 1 + 1 × (−2) = 0 : B, C, D, E sont coplanaires. Contrôle : BE⃗ = −BC⃗ + 2BD⃗, car (1 ; −1 + 4 ; −1 − 2) = (1 ; 3 ; −3) ✓.

:::

::: piege
**Erreur : mettre dans le déterminant les coordonnées des points au lieu de celles de vecteurs issus d'un même point.** L'erreur tente parce que les coordonnées sont sous les yeux. Pour B, C, D de l'exemple, le déterminant des coordonnées vaut −1, alors que det(AB⃗, AC⃗, AD⃗) = 4 : le résultat dépendrait du choix de l'origine O, ce qui n'a aucun sens pour une question de coplanarité. On forme toujours AB⃗, AC⃗, AD⃗ à partir d'un seul des quatre points.
:::

::: propriete
Quatre points A, B, C, D de l'espace sont **coplanaires** si et seulement si det(AB⃗, AC⃗, AD⃗) = 0 dans une base quelconque de l'espace.
Cas limite : si trois des points sont alignés, ou si deux sont confondus, le déterminant est nul aussi, et les quatre points sont bien dans un même plan.
:::

::: verifie À toi : coplanaires ou non ?
Dans un repère de l'espace, les points K(0 ; 1 ; 1), L(2 ; 2 ; 0), M(1 ; 0 ; 3) et N(5 ; 2 ; 2) sont-ils coplanaires ?

---

KL⃗(2 ; 1 ; −1), KM⃗(1 ; −1 ; 2) et KN⃗(5 ; 1 ; 1). Les trois parenthèses valent (−1) × 1 − 2 × 1 = −3, puis 1 × 1 − 2 × 5 = −9, puis 1 × 1 − (−1) × 5 = 6, d'où det(KL⃗, KM⃗, KN⃗) = 2 × (−3) − 1 × (−9) + (−1) × 6 = −3. Ce nombre est non nul : les quatre points ne sont pas coplanaires, même si N est tout près du plan (KLM) : le point N′(5 ; 2 ; 1) = K + 2KL⃗ + KM⃗, lui, y serait.
:::

::: retenir
Le déterminant de (AB⃗, AC⃗, AD⃗) est nul si et seulement si A, B, C, D sont coplanaires ; il se calcule avec des vecteurs issus d'un même point.
:::

## 📐 Le produit scalaire dans l'espace

Dans un cube ABCDEFGH d'arête a, les segments [AF] et [DE] sont des diagonales de deux faces voisines, et [DG] une troisième. Sont-ils perpendiculaires ? Quel angle forment (AF) et (DE) ?
Comment répondre sans construire aucun angle, à partir des seules arêtes ?

::: definition
Soient A, B, C trois points de l'espace. Le **produit scalaire** des vecteurs AB⃗ et AC⃗ est le réel noté AB⃗ . AC⃗ défini par : AB⃗ . AC⃗ = 0 si AB⃗ ou AC⃗ est nul, et sinon
$$ AB⃗ . AC⃗ = AB × AC × cos BÂC $$
En particulier AB⃗ . AB⃗ = ‖AB⃗‖² = AB².
:::

::: figure Le cube ABCDEFGH d'arête a : la diagonale AF de la face avant (en vert) et la diagonale DE de la face de gauche (en orange). D est caché derrière le cube, donc ses arêtes sont en pointillés.
<svg viewBox="0 0 250 232">
<title>Cube ABCDEFGH d'arête a : les diagonales de face AF en vert et DE en orange</title>
<polygon points="36,200 136,200 136,100 36,100" fill="#0f6e56" opacity="0.1"/>
<line x1="179.3" y1="175" x2="79.3" y2="175" stroke="#94a3b8" stroke-width="1.6" stroke-dasharray="5 4"/>
<line x1="79.3" y1="175" x2="36" y2="200" stroke="#94a3b8" stroke-width="1.6" stroke-dasharray="5 4"/>
<line x1="79.3" y1="175" x2="79.3" y2="75" stroke="#94a3b8" stroke-width="1.6" stroke-dasharray="5 4"/>
<line x1="36" y1="200" x2="136" y2="200" stroke="#0f172a" stroke-width="2"/>
<line x1="136" y1="200" x2="179.3" y2="175" stroke="#0f172a" stroke-width="2"/>
<line x1="36" y1="100" x2="136" y2="100" stroke="#0f172a" stroke-width="2"/>
<line x1="136" y1="100" x2="179.3" y2="75" stroke="#0f172a" stroke-width="2"/>
<line x1="179.3" y1="75" x2="79.3" y2="75" stroke="#0f172a" stroke-width="2"/>
<line x1="79.3" y1="75" x2="36" y2="100" stroke="#0f172a" stroke-width="2"/>
<line x1="36" y1="200" x2="36" y2="100" stroke="#0f172a" stroke-width="2"/>
<line x1="136" y1="200" x2="136" y2="100" stroke="#0f172a" stroke-width="2"/>
<line x1="179.3" y1="175" x2="179.3" y2="75" stroke="#0f172a" stroke-width="2"/>
<line x1="36" y1="200" x2="128.22" y2="107.78" stroke="#0f6e56" stroke-width="2.6"/>
<polygon points="136,100 131.49,111.05 124.95,104.51" fill="#0f6e56"/>
<path d="M102 131 h16 m-3 -2.5 l3 2.5 l-3 2.5" fill="none" stroke="#0f6e56" stroke-width="1.3"/>
<text x="110" y="144" text-anchor="middle" fill="#0f6e56" font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">AF</text>
<line x1="79.3" y1="175" x2="41.5" y2="109.53" stroke="#b45309" stroke-width="2.6"/>
<polygon points="36,100 45.5,107.22 37.5,111.84" fill="#b45309"/>
<path d="M39.98 138 h16 m-3 -2.5 l3 2.5 l-3 2.5" fill="none" stroke="#b45309" stroke-width="1.3"/>
<text x="47.98" y="151" text-anchor="middle" fill="#b45309" font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">DE</text>
<circle cx="36" cy="200" r="3.5" fill="#0f172a"/>
<circle cx="136" cy="200" r="3.5" fill="#0f172a"/>
<circle cx="179.3" cy="175" r="3.5" fill="#0f172a"/>
<circle cx="79.3" cy="175" r="3.5" fill="#94a3b8"/>
<circle cx="36" cy="100" r="3.5" fill="#0f172a"/>
<circle cx="136" cy="100" r="3.5" fill="#0f172a"/>
<circle cx="179.3" cy="75" r="3.5" fill="#0f172a"/>
<circle cx="79.3" cy="75" r="3.5" fill="#0f172a"/>
<text x="24" y="216" text-anchor="middle" fill="#0f172a" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">A</text>
<text x="146" y="218" text-anchor="middle" fill="#0f172a" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">B</text>
<text x="193.3" y="180" text-anchor="middle" fill="#0f172a" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">C</text>
<text x="67.3" y="169" text-anchor="middle" fill="#94a3b8" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">D</text>
<text x="24" y="98" text-anchor="middle" fill="#0f172a" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">E</text>
<text x="124" y="92" text-anchor="middle" fill="#0f172a" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">F</text>
<text x="193.3" y="69" text-anchor="middle" fill="#0f172a" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">G</text>
<text x="75.3" y="65" text-anchor="middle" fill="#0f172a" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">H</text>
</svg>
:::

Sur la figure, AF et DE sont deux diagonales de faces voisines, qui ne se coupent pas : leur angle ne se lit pas sur le dessin, il se calcule.

::: exemple Calculer AF⃗ . DG⃗ et AF⃗ . DE⃗ dans le cube d'arête a

1. Le quadrilatère ADGF est un rectangle (AD et FG sont égaux et parallèles, et AD est perpendiculaire à AF) : donc AF⃗ = DG⃗. Alors AF⃗ . DG⃗ = AF⃗ . AF⃗ = AF² = (a√2)² = 2a².
2. Pour AF⃗ . DE⃗, on se place dans le repère (A ; AB⃗/a, AD⃗/a, AE⃗/a), orthonormé. Les coordonnées sont F(a ; 0 ; a), D(0 ; a ; 0), E(0 ; 0 ; a), d'où AF⃗(a ; 0 ; a) et DE⃗(0 ; −a ; a).
3. Le produit vaut a × 0 + 0 × (−a) + a × a = a². Les normes sont ‖AF⃗‖ = ‖DE⃗‖ = a√2.
4. Par la définition, cos(AF⃗, DE⃗) = a²/(a√2 × a√2) = 1/2 : l'angle des deux diagonales vaut 60° (π/3 rad). Contrôle : AF⃗ − DE⃗ = (a ; a ; 0) = AC⃗, de norme a√2 ; les trois longueurs ‖AF⃗‖, ‖DE⃗‖ et ‖AF⃗ − DE⃗‖ sont égales, ce sont celles d'un triangle équilatéral, donc 60° ✓.

:::

::: piege
**Erreur : appliquer xx′ + yy′ + zz′ dans un repère seulement orthogonal.** L'erreur tente parce que les trois vecteurs du repère sont perpendiculaires deux à deux. Mais (O, j⃗ + k⃗, k⃗ − j⃗, i⃗) est orthogonal sans être orthonormé : ‖j⃗ + k⃗‖ = ‖k⃗ − j⃗‖ = √2. Le vecteur de coordonnées (1 ; 1 ; 0) dans ce repère est (j⃗ + k⃗) + (k⃗ − j⃗) = 2k⃗, de carré scalaire 4, alors que la formule donnerait 1 + 1 + 0 = 2.
:::

::: propriete
Pour tous vecteurs u⃗, v⃗, w⃗ et tous réels α, β : u⃗ . v⃗ = v⃗ . u⃗ ; u⃗ . (v⃗ + w⃗) = u⃗ . v⃗ + u⃗ . w⃗ ; (αu⃗) . (βv⃗) = αβ (u⃗ . v⃗).
Le repère (O, i⃗, j⃗, k⃗) est **orthonormé** si ‖i⃗‖ = ‖j⃗‖ = ‖k⃗‖ = 1 et i⃗ . j⃗ = i⃗ . k⃗ = j⃗ . k⃗ = 0. Dans un tel repère, pour u⃗(x ; y ; z) et v⃗(x′ ; y′ ; z′) :
$$ u⃗ . v⃗ = xx′ + yy′ + zz′ $$
$$ ‖u⃗‖ = √(x² + y² + z²) $$
$$ MM′ = √((x − x′)² + (y − y′)² + (z − z′)²) $$
Deux vecteurs sont **orthogonaux** si et seulement si leur produit scalaire est nul. Cas limite : le vecteur nul est orthogonal à tout vecteur.
:::

::: verifie À toi : un angle obtus
Dans le cube d'arête 1 muni du repère orthonormé (A ; AB⃗, AD⃗, AE⃗), calculer EG⃗ . GB⃗ puis l'angle des vecteurs EG⃗ et GB⃗.

---

E(0 ; 0 ; 1), G(1 ; 1 ; 1) et B(1 ; 0 ; 0) donnent EG⃗(1 ; 1 ; 0) et GB⃗(0 ; −1 ; −1), donc EG⃗ . GB⃗ = 0 − 1 + 0 = −1. Les normes valent ‖EG⃗‖ = ‖GB⃗‖ = √2, d'où cos(EG⃗, GB⃗) = −1/(√2 × √2) = −1/2 : l'angle des deux vecteurs vaut 120°. L'angle géométrique EGB du triangle, lui, vaut 60° : c'est celui des vecteurs GE⃗ et GB⃗, de produit scalaire +1.
:::

::: retenir
Le produit scalaire est un réel : en repère orthonormé, u⃗ . v⃗ = xx′ + yy′ + zz′, ‖u⃗‖ = √(x² + y² + z²), et u⃗ . v⃗ = 0 si et seulement si u⃗ et v⃗ sont orthogonaux.
:::

## 🧭 L'orientation de l'espace

Une main gauche et une main droite ont les mêmes doigts, et aucun déplacement ne superpose l'une à l'autre. Il en va de même des repères de l'espace : (O, i⃗, j⃗, k⃗) et (O, j⃗, i⃗, k⃗) ont les mêmes axes, mais pas le même « sens ».
Comment les distinguer par une règle précise, sans parler de main ?

::: definition
Soit (O, i⃗, j⃗, k⃗) un repère, et I, J, K les points tels que OI⃗ = i⃗, OJ⃗ = j⃗, OK⃗ = k⃗. Un **observateur d'Ampère** est placé le long de (OK), les pieds en O, et regarde dans la direction de (OI) ; le plan (OIK) partage l'espace en deux demi-espaces, l'un à sa gauche et l'autre à sa droite.
Le repère est **direct** si (OJ) est dans le demi-espace à gauche de l'observateur, **indirect** si (OJ) est à sa droite. Une base (i⃗, j⃗, k⃗) est directe ou indirecte selon que le repère (O, i⃗, j⃗, k⃗) l'est (le point O n'y change rien). **Orienter l'espace**, c'est choisir l'un de ces repères ; l'espace est orienté dans le sens direct s'il est muni d'un repère direct, dans le sens indirect s'il est muni d'un repère indirect.
:::

::: figure À gauche, le repère (O, i⃗, j⃗, k⃗) : l'observateur debout sur k⃗ qui regarde vers i⃗ a j⃗ à sa gauche, le repère est direct. À droite, les noms i⃗ et j⃗ sont échangés : j⃗ est maintenant à sa droite, le repère est indirect.
<svg viewBox="0 0 360 225">
<title>Deux repères : à gauche (O, i, j, k), à droite le même dessin où i et j sont échangés</title>
<line x1="40" y1="175" x2="133.5" y2="175" stroke="#0f6e56" stroke-width="2.6"/>
<polygon points="144.5,175 133.5,179.62 133.5,170.38" fill="#0f6e56"/>
<line x1="40" y1="175" x2="92.18" y2="144.88" stroke="#b45309" stroke-width="2.6"/>
<polygon points="101.7,139.38 94.49,148.88 89.87,140.87" fill="#b45309"/>
<line x1="40" y1="175" x2="40" y2="67.25" stroke="#0f172a" stroke-width="2.6"/>
<polygon points="40,56.25 44.62,67.25 35.38,67.25" fill="#0f172a"/>
<circle cx="40" cy="175" r="3.5" fill="#0f172a"/>
<text x="28" y="189" text-anchor="middle" fill="#0f172a" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">O</text>
<path d="M148.5 178 h8 m-3 -2.5 l3 2.5 l-3 2.5" fill="none" stroke="#0f6e56" stroke-width="1.3"/>
<text x="152.5" y="191" text-anchor="middle" fill="#0f6e56" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">i</text>
<path d="M111.7 122.38 h8 m-3 -2.5 l3 2.5 l-3 2.5" fill="none" stroke="#b45309" stroke-width="1.3"/>
<text x="115.7" y="135.38" text-anchor="middle" fill="#b45309" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">j</text>
<path d="M48 49.25 h8 m-3 -2.5 l3 2.5 l-3 2.5" fill="none" stroke="#0f172a" stroke-width="1.3"/>
<text x="52" y="62.25" text-anchor="middle" fill="#0f172a" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">k</text>
<line x1="235" y1="175" x2="328.5" y2="175" stroke="#0f6e56" stroke-width="2.6"/>
<polygon points="339.5,175 328.5,179.62 328.5,170.38" fill="#0f6e56"/>
<line x1="235" y1="175" x2="287.18" y2="144.88" stroke="#b45309" stroke-width="2.6"/>
<polygon points="296.7,139.38 289.49,148.88 284.87,140.87" fill="#b45309"/>
<line x1="235" y1="175" x2="235" y2="67.25" stroke="#0f172a" stroke-width="2.6"/>
<polygon points="235,56.25 239.62,67.25 230.38,67.25" fill="#0f172a"/>
<circle cx="235" cy="175" r="3.5" fill="#0f172a"/>
<text x="223" y="189" text-anchor="middle" fill="#0f172a" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">O</text>
<path d="M343.5 178 h8 m-3 -2.5 l3 2.5 l-3 2.5" fill="none" stroke="#0f6e56" stroke-width="1.3"/>
<text x="347.5" y="191" text-anchor="middle" fill="#0f6e56" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">j</text>
<path d="M306.7 122.38 h8 m-3 -2.5 l3 2.5 l-3 2.5" fill="none" stroke="#b45309" stroke-width="1.3"/>
<text x="310.7" y="135.38" text-anchor="middle" fill="#b45309" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">i</text>
<path d="M243 49.25 h8 m-3 -2.5 l3 2.5 l-3 2.5" fill="none" stroke="#0f172a" stroke-width="1.3"/>
<text x="247" y="62.25" text-anchor="middle" fill="#0f172a" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">k</text>
<text x="90" y="208" text-anchor="middle" fill="#0f172a" font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">direct</text>
<text x="285" y="208" text-anchor="middle" fill="#0f172a" font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">indirect</text>
</svg>
:::

Sur la figure, un seul geste change l'orientation : échanger deux vecteurs.

::: exemple Orienter trois bases dans un cube

Le cube ABCDEFGH est muni du repère orthonormé direct (A ; AB⃗, AD⃗, AE⃗). Les bases suivantes sont-elles directes ?

1. (AE⃗, AD⃗, AB⃗) : on a échangé AB⃗ et AE⃗ dans (AB⃗, AD⃗, AE⃗), donc la base est indirecte.
2. (EF⃗, HD⃗, FG⃗) : EF⃗ = AB⃗, HD⃗ = −AE⃗ et FG⃗ = AD⃗, donc la base est (AB⃗, −AE⃗, AD⃗). Échanger AD⃗ et AE⃗ rend la base indirecte, et remplacer AE⃗ par son opposé change encore l'orientation : la base est directe.
3. (CG⃗, DC⃗, BC⃗) : CG⃗ = AE⃗, DC⃗ = AB⃗ et BC⃗ = AD⃗, donc la base est (AE⃗, AB⃗, AD⃗). C'est une permutation circulaire de (AB⃗, AD⃗, AE⃗) : la base est directe. Contrôle : (AE⃗, AB⃗, AD⃗) → (AB⃗, AE⃗, AD⃗) → (AB⃗, AD⃗, AE⃗) par deux échanges, donc l'orientation est conservée.

:::

::: piege
**Erreur : croire qu'une permutation circulaire change l'orientation.** L'erreur tente parce que l'ordre des vecteurs a bien changé. Mais (j⃗, k⃗, i⃗) s'obtient de (i⃗, j⃗, k⃗) par deux échanges successifs, (i⃗, j⃗, k⃗) → (j⃗, i⃗, k⃗) → (j⃗, k⃗, i⃗) : l'orientation change deux fois, donc elle est conservée, et (j⃗, k⃗, i⃗) est directe.
:::

::: propriete
Une base de l'espace orienté est directe ou indirecte, et :
• échanger deux de ses vecteurs change son orientation ;
• une permutation circulaire des trois vecteurs la conserve ;
• remplacer un vecteur par son opposé la change.
Un plan P de l'espace orienté est orienté en choisissant un point C de la perpendiculaire à P en O : un repère (O, OA⃗, OB⃗) de P est direct si (O, OA⃗, OB⃗, OC⃗) est direct dans l'espace.
Cas limite : choisir C de l'autre côté de P renverse l'orientation du plan, qui dépend donc de ce choix.
:::

::: verifie À toi : indirecte ou directe ?
Dans le même cube, la base (BF⃗, CD⃗, AD⃗) est-elle directe ?

---

BF⃗ = AE⃗, CD⃗ = −AB⃗ et AD⃗ = AD⃗ : la base est (AE⃗, −AB⃗, AD⃗). La base (AE⃗, AB⃗, AD⃗) est directe (permutation circulaire), et remplacer AB⃗ par son opposé change l'orientation : la base (BF⃗, CD⃗, AD⃗) est indirecte.
:::

::: retenir
Échanger deux vecteurs ou en remplacer un par son opposé change l'orientation d'une base ; une permutation circulaire la conserve.
:::

## ✖️ Le produit vectoriel : définition

AB⃗ et AD⃗ sont deux arêtes d'un cube d'arête 1, et AE⃗ est perpendiculaire aux deux. Mais −AE⃗ l'est aussi, et 5AE⃗ également : il y a une infinité de vecteurs orthogonaux à AB⃗ et AD⃗.
Comment en désigner un seul, avec sa direction, son sens et sa longueur imposés, à partir des deux vecteurs ?

::: definition
Soient u⃗ et v⃗ deux vecteurs, dans l'espace orienté. Le **produit vectoriel** de u⃗ par v⃗ est le vecteur noté **u⃗ ∧ v⃗** défini ainsi :
• si u⃗ et v⃗ sont colinéaires, u⃗ ∧ v⃗ = 0⃗ ;
• sinon, u⃗ ∧ v⃗ est orthogonal à u⃗ et à v⃗, la base (u⃗, v⃗, u⃗ ∧ v⃗) est directe, et
$$ ‖u⃗ ∧ v⃗‖ = ‖u⃗‖ × ‖v⃗‖ × sin α $$
où α est la mesure en radians de l'angle géométrique de deux représentants de u⃗ et v⃗ de même origine.
:::

::: figure Le vecteur u⃗ ∧ v⃗ (en orange) se dresse perpendiculairement au plan de u⃗ et v⃗ (en vert), ce que marquent les deux petits angles droits en O ; le trièdre (u⃗, v⃗, u⃗ ∧ v⃗) est direct.
<svg viewBox="0 0 270 215">
<title>Le vecteur u∧v est perpendiculaire au plan de u et v, et (u, v, u∧v) est directe</title>
<polygon points="40,190 157,190 211.04,158.8 94.04,158.8" fill="#0f6e56" opacity="0.12"/>
<polyline points="157,190 211.04,158.8 94.04,158.8" fill="none" stroke="#94a3b8" stroke-width="1.4"/>
<line x1="40" y1="190" x2="146" y2="190" stroke="#0f6e56" stroke-width="2.6"/>
<polygon points="157,190 146,194.62 146,185.38" fill="#0f6e56"/>
<line x1="40" y1="190" x2="84.51" y2="164.3" stroke="#0f6e56" stroke-width="2.6"/>
<polygon points="94.04,158.8 86.82,168.3 82.2,160.3" fill="#0f6e56"/>
<line x1="40" y1="190" x2="40" y2="68.4" stroke="#b45309" stroke-width="2.6"/>
<polygon points="40,57.4 44.62,68.4 35.38,68.4" fill="#b45309"/>
<polyline points="50.14,190 50.14,179.86 40,179.86" fill="none" stroke="#0f172a" stroke-width="1.4"/>
<polyline points="44.39,187.47 44.39,177.32 40,179.86" fill="none" stroke="#0f172a" stroke-width="1.4"/>
<circle cx="40" cy="190" r="3.5" fill="#0f172a"/>
<text x="28" y="204" text-anchor="middle" fill="#0f172a" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">O</text>
<path d="M157 193 h8 m-3 -2.5 l3 2.5 l-3 2.5" fill="none" stroke="#0f6e56" stroke-width="1.3"/>
<text x="161" y="206" text-anchor="middle" fill="#0f6e56" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">u</text>
<path d="M104.04 143.8 h8 m-3 -2.5 l3 2.5 l-3 2.5" fill="none" stroke="#0f6e56" stroke-width="1.3"/>
<text x="108.04" y="156.8" text-anchor="middle" fill="#0f6e56" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">v</text>
<path d="M63 52.4 h22 m-3 -2.5 l3 2.5 l-3 2.5" fill="none" stroke="#b45309" stroke-width="1.3"/>
<text x="74" y="65.4" text-anchor="middle" fill="#b45309" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">u∧v</text>
</svg>
:::

Sur la figure, u⃗ ∧ v⃗ est le vecteur qui se dresse au-dessus du plan des deux autres : sa direction, son sens et sa longueur sont fixés par la définition. Cette définition tient parce que, pour une base (i⃗, j⃗) d'un plan et un réel d > 0, il existe un seul vecteur k⃗ de norme d, orthogonal à i⃗ et j⃗, tel que (i⃗, j⃗, k⃗) soit directe (théorème d'existence, admis).

::: exemple Quelques produits vectoriels dans le cube d'arête 1

Le cube ABCDEFGH d'arête 1 est muni du repère orthonormé direct (A ; AB⃗, AD⃗, AE⃗). Déterminer AB⃗ ∧ AD⃗, AB⃗ ∧ FG⃗, EF⃗ ∧ EF⃗ et EF⃗ ∧ GH⃗.

1. AB⃗ et AD⃗ ne sont pas colinéaires. AE⃗ est orthogonal aux deux, la base (AB⃗, AD⃗, AE⃗) est directe, et l'angle est droit : ‖AB⃗ ∧ AD⃗‖ = 1 × 1 × sin(π/2) = 1 = ‖AE⃗‖. Donc AB⃗ ∧ AD⃗ = AE⃗.
2. FG⃗ = AD⃗, donc AB⃗ ∧ FG⃗ = AB⃗ ∧ AD⃗ = AE⃗.
3. Un vecteur est colinéaire à lui-même : EF⃗ ∧ EF⃗ = 0⃗.
4. GH⃗ = −EF⃗ est colinéaire à EF⃗ : EF⃗ ∧ GH⃗ = 0⃗.

:::

::: exemple Une norme avec l'angle

Deux vecteurs u⃗ et v⃗ de normes 6 et 4 forment un angle géométrique de 30°.

1. Le produit vectoriel a pour norme ‖u⃗ ∧ v⃗‖ = 6 × 4 × sin 30° = 24 × 1/2 = 12.
2. Le produit scalaire vaut u⃗ . v⃗ = 6 × 4 × cos 30° = 24 × √3/2 = 12√3.
3. Contrôle : ‖u⃗ ∧ v⃗‖² + (u⃗ . v⃗)² = 144 + 432 = 576 = (6 × 4)² ✓, car sin² + cos² = 1.

:::

::: piege
**Erreur : confondre « colinéaires » et « orthogonaux ».** L'erreur tente parce que les deux produits annulent un cas particulier. Mais u⃗ ∧ v⃗ = 0⃗ signifie colinéaires, et u⃗ . v⃗ = 0 signifie orthogonaux. Pour AB⃗ et AD⃗, perpendiculaires, on a AB⃗ . AD⃗ = 0 et pourtant AB⃗ ∧ AD⃗ = AE⃗ est de norme maximale 1.
:::

::: verifie À toi : l'ordre compte
Dans le même cube, déterminer AD⃗ ∧ AB⃗ puis AE⃗ ∧ AB⃗.

---

AD⃗ ∧ AB⃗ est orthogonal à AD⃗ et AB⃗, de norme 1, avec (AD⃗, AB⃗, AD⃗ ∧ AB⃗) directe. Comme (AD⃗, AB⃗, AE⃗) est indirecte (un échange), le vecteur qui la rend directe est −AE⃗ : AD⃗ ∧ AB⃗ = −AE⃗. Pour AE⃗ ∧ AB⃗, c'est AD⃗ : (AE⃗, AB⃗, AD⃗) est une permutation circulaire de (AB⃗, AD⃗, AE⃗), donc directe.
:::

::: retenir
u⃗ ∧ v⃗ est un vecteur orthogonal à u⃗ et v⃗, nul si et seulement si u⃗ et v⃗ sont colinéaires, de norme ‖u⃗‖ ‖v⃗‖ sin α, qui complète (u⃗, v⃗) en une base directe.
:::

## 🧩 Les propriétés du produit vectoriel et ses coordonnées

Dans un repère, on connaît les coordonnées de u⃗ et v⃗ : la définition, avec son angle, son sinus et son orientation, ne permet pas de calculer à la main.
Existe-t-il une formule en coordonnées, et peut-on développer un produit vectoriel comme un produit de nombres ?

::: exemple Les coordonnées de u⃗ ∧ v⃗, avec u⃗ = j⃗ − 2k⃗ et v⃗ = i⃗ + j⃗ − k⃗

1. Dans une base orthonormée directe, pour u⃗(a ; b ; c) et v⃗(a′ ; b′ ; c′), les coordonnées de u⃗ ∧ v⃗ sont (bc′ − cb′ ; ca′ − ac′ ; ab′ − ba′). Ici u⃗(0 ; 1 ; −2) et v⃗(1 ; 1 ; −1).
2. Première coordonnée : bc′ − cb′ = 1 × (−1) − (−2) × 1 = 1. Deuxième : ca′ − ac′ = (−2) × 1 − 0 × (−1) = −2. Troisième : ab′ − ba′ = 0 × 1 − 1 × 1 = −1.
3. Donc u⃗ ∧ v⃗ = (1 ; −2 ; −1). Contrôle : (1 ; −2 ; −1) . u⃗ = 0 − 2 + 2 = 0 et (1 ; −2 ; −1) . v⃗ = 1 − 2 + 1 = 0 ✓.

:::

::: exemple Développer avec les propriétés

On sait que ‖u⃗‖ = 1, ‖v⃗‖ = 4 et u⃗ . v⃗ = 2, et l'on pose w⃗ = 2 u⃗ ∧ v⃗ − 3v⃗. Calculer u⃗ . w⃗, v⃗ . w⃗ et ‖w⃗‖.

1. u⃗ ∧ v⃗ est orthogonal à u⃗ et à v⃗ : u⃗ . (u⃗ ∧ v⃗) = 0 et v⃗ . (u⃗ ∧ v⃗) = 0.
2. Par linéarité, u⃗ . w⃗ = 2 × 0 − 3 u⃗ . v⃗ = −6, et v⃗ . w⃗ = 2 × 0 − 3 ‖v⃗‖² = −48.
3. On a cos α = u⃗ . v⃗ / (‖u⃗‖ ‖v⃗‖) = 1/2, donc sin α = √3/2 et ‖u⃗ ∧ v⃗‖ = 1 × 4 × √3/2 = 2√3.
4. Les deux termes de w⃗ sont orthogonaux (le premier est orthogonal à v⃗) : ‖w⃗‖² = 4 × 12 + 9 × 16 = 192, donc ‖w⃗‖ = 8√3.

:::

::: exemple Résoudre u⃗ ∧ v⃗ = w⃗

Soient u⃗(1 ; 2 ; 2) et w⃗(2 ; 2 ; −3). Trouver tous les vecteurs v⃗ tels que u⃗ ∧ v⃗ = w⃗.

1. Un produit u⃗ ∧ v⃗ est orthogonal à u⃗ : il faut donc u⃗ . w⃗ = 0. C'est le cas, car 2 + 4 − 6 = 0.
2. Pour v⃗(x ; y ; z), les coordonnées de u⃗ ∧ v⃗ sont (2z − 2y ; 2x − z ; y − 2x). Le système 2z − 2y = 2, 2x − z = 2, y − 2x = −3 donne z = y + 1 et z = 2x − 2, donc y = 2x − 3.
3. Les solutions sont v⃗(x ; 2x − 3 ; 2x − 2), c'est-à-dire v⃗ = (0 ; −3 ; −2) + x (1 ; 2 ; 2). Contrôle : pour x = 0, u⃗ ∧ (0 ; −3 ; −2) = (2 × (−2) − 2 × (−3) ; 2 × 0 − 1 × (−2) ; 1 × (−3) − 0) = (2 ; 2 ; −3) ✓.
4. Deux solutions diffèrent d'un multiple de u⃗, puisque u⃗ ∧ u⃗ = 0⃗.

:::

::: piege
**Erreur : simplifier par u⃗ dans u⃗ ∧ v⃗ = u⃗ ∧ w⃗.** L'erreur tente parce qu'on simplifie par un facteur commun dans un produit de nombres. Avec u⃗ = i⃗, v⃗ = j⃗ et w⃗ = i⃗ + j⃗, on trouve u⃗ ∧ v⃗ = k⃗ et u⃗ ∧ w⃗ = i⃗ ∧ j⃗ + i⃗ ∧ i⃗ = k⃗ : les deux produits sont égaux, et pourtant v⃗ ≠ w⃗. La seule conclusion est que v⃗ − w⃗ est colinéaire à u⃗.
:::

::: propriete
Pour tous vecteurs u⃗, v⃗, w⃗ et tous réels a, b :
u⃗ ∧ u⃗ = 0⃗ ; u⃗ ∧ v⃗ = 0⃗ si et seulement si u⃗ et v⃗ sont colinéaires ; u⃗ ∧ v⃗ = −(v⃗ ∧ u⃗) ;
(au⃗) ∧ (bv⃗) = ab (u⃗ ∧ v⃗) ; (u⃗ + v⃗) ∧ w⃗ = u⃗ ∧ w⃗ + v⃗ ∧ w⃗ ; u⃗ ∧ (v⃗ + w⃗) = u⃗ ∧ v⃗ + u⃗ ∧ w⃗.
Dans une base orthonormée directe, pour u⃗(a ; b ; c) et v⃗(a′ ; b′ ; c′) (formule admise) :
$$ u⃗ ∧ v⃗ = (bc′ − cb′ ; ca′ − ac′ ; ab′ − ba′) $$
Cas limite : le produit vectoriel n'est ni commutatif, ni simplifiable, et u⃗ ∧ v⃗ = 0⃗ s'écrit avec la flèche, alors que u⃗ . v⃗ = 0 est un réel.
:::

::: verifie À toi : un produit vectoriel en coordonnées
Calculer u⃗ ∧ v⃗ pour u⃗(3 ; 1 ; −2) et v⃗(−1 ; 2 ; 2), puis contrôler le résultat.

---

Première coordonnée : 1 × 2 − (−2) × 2 = 6. Deuxième : (−2) × (−1) − 3 × 2 = −4. Troisième : 3 × 2 − 1 × (−1) = 7. Donc u⃗ ∧ v⃗ = (6 ; −4 ; 7). Contrôle : (6 ; −4 ; 7) . u⃗ = 18 − 4 − 14 = 0 et (6 ; −4 ; 7) . v⃗ = −6 − 8 + 14 = 0 ✓.
:::

::: retenir
En base orthonormée directe, u⃗ ∧ v⃗ = (bc′ − cb′ ; ca′ − ac′ ; ab′ − ba′) ; il change de signe quand on échange les facteurs, se développe comme une somme, mais ne se simplifie pas.
:::

## 📏 L'aire d'un parallélogramme et d'un triangle

Un panneau triangulaire a pour sommets A(1 ; 0 ; −1), B(1 ; −2 ; 1) et C(0 ; −1 ; 2), et un piquet P(3 ; 1 ; 0) est planté au pied du panneau. Quelle est l'aire du panneau, quel est son angle en A, et le piquet est-il perpendiculaire au panneau ?
Un seul produit vectoriel peut-il tout fournir ?

::: figure Le parallélogramme ABCD a pour base AB et pour hauteur h = DH. Sa diagonale [BD] le partage en deux triangles égaux : le triangle ABD en est la moitié.
<svg viewBox="0 0 290 210">
<title>Le parallélogramme ABCD, sa base AB, sa hauteur h = DH et l'angle α en A</title>
<polygon points="40,185 200,185 255,95 95,95" fill="#0f6e56" opacity="0.12"/>
<polyline points="40,185 200,185 255,95 95,95 40,185" fill="none" stroke="#0f172a" stroke-width="2.2"/>
<line x1="200" y1="185" x2="95" y2="95" stroke="#0f172a" stroke-width="1.6" stroke-dasharray="5 4"/>
<line x1="95" y1="95" x2="95" y2="185" stroke="#b45309" stroke-width="2.4" stroke-dasharray="5 4"/>
<polyline points="95,172 108,172 108,185" fill="none" stroke="#0f172a" stroke-width="1.4"/>
<polyline points="66,185 65.91,182.79 65.62,180.59 65.16,178.43 64.51,176.31 63.68,174.26 62.68,172.28 61.51,170.4 60.19,168.62 58.73,166.96 57.12,165.43 55.4,164.05 53.56,162.81" fill="none" stroke="#b45309" stroke-width="1.8"/>
<circle cx="40" cy="185" r="3.5" fill="#0f172a"/>
<text x="28" y="201" text-anchor="middle" fill="#0f172a" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">A</text>
<circle cx="200" cy="185" r="3.5" fill="#0f172a"/>
<text x="212" y="203" text-anchor="middle" fill="#0f172a" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">B</text>
<circle cx="255" cy="95" r="3.5" fill="#0f172a"/>
<text x="269" y="101" text-anchor="middle" fill="#0f172a" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">C</text>
<circle cx="95" cy="95" r="3.5" fill="#0f172a"/>
<text x="83" y="91" text-anchor="middle" fill="#0f172a" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">D</text>
<circle cx="95" cy="185" r="3.5" fill="#0f172a"/>
<text x="95" y="203" text-anchor="middle" fill="#0f172a" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">H</text>
<text x="82" y="145" text-anchor="middle" fill="#b45309" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">h</text>
<text x="74" y="174" text-anchor="middle" fill="#b45309" font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">α</text>
</svg>
:::

Sur la figure, l'aire du parallélogramme est base × hauteur = AB × h. Comme h = AD × sin α, cette aire vaut AB × AD × sin α, c'est-à-dire ‖AB⃗ ∧ AD⃗‖ d'après la définition du produit vectoriel.

::: exemple L'aire, l'angle et la perpendicularité du panneau

1. AB⃗(0 ; −2 ; 2), AC⃗(−1 ; −1 ; 3) et AB⃗ ∧ AC⃗ = ((−2) × 3 − 2 × (−1) ; 2 × (−1) − 0 × 3 ; 0 × (−1) − (−2)(−1)) = (−4 ; −2 ; −2). Ce vecteur est non nul : A, B, C ne sont pas alignés.
2. Sa norme vaut √(16 + 4 + 4) = √24 = 2√6 : c'est l'aire du parallélogramme construit sur AB⃗ et AC⃗. Le triangle ABC en vaut la moitié : √6.
3. Pour l'angle, ‖AB⃗‖ = 2√2 et ‖AC⃗‖ = √11, d'où sin A = 2√6 / (2√2 × √11) = √(3/11) ≈ 0,52 et A ≈ 0,55 rad. Contrôle : cos A = AB⃗ . AC⃗ / (‖AB⃗‖ ‖AC⃗‖) = 8/√88 ≈ 0,85, et 0,52² + 0,85² ≈ 1 ✓.
4. AP⃗(2 ; 1 ; 1) vérifie AP⃗ . AB⃗ = 0 − 2 + 2 = 0 et AP⃗ . AC⃗ = −2 − 1 + 3 = 0 : (AP) est orthogonale aux deux directions du plan, donc perpendiculaire au plan (ABC). On retrouve AB⃗ ∧ AC⃗ = −2 AP⃗, colinéaire à AP⃗ ✓.

:::

::: exemple La loi des sinus par le produit vectoriel

Soit ABC un triangle.

1. Comme BC⃗ = BA⃗ + AC⃗, on a BC⃗ ∧ BA⃗ = BA⃗ ∧ BA⃗ + AC⃗ ∧ BA⃗ = AC⃗ ∧ BA⃗ = AB⃗ ∧ AC⃗ (deux changements de signe).
2. De même CA⃗ ∧ CB⃗ = AB⃗ ∧ AC⃗. Les trois produits ont donc la même norme : AB × AC × sin A = BC × BA × sin B = CA × CB × sin C.
3. En divisant par AB × BC × CA, on obtient sin A / BC = sin B / CA = sin C / AB.

:::

::: piege
**Erreur : donner ‖AB⃗ ∧ AC⃗‖ comme aire du triangle.** L'erreur tente parce que cette norme est la quantité qu'on vient de calculer. Mais elle mesure le parallélogramme : pour le panneau, 2√6 est l'aire du parallélogramme et √6 celle du triangle.
:::

::: propriete
• L'aire d'un parallélogramme ABCD est ‖AB⃗ ∧ AD⃗‖ ; celle d'un triangle ABD est (1/2) ‖AB⃗ ∧ AD⃗‖.
• Trois points A, B, C sont alignés si et seulement si AB⃗ ∧ AC⃗ = 0⃗.
Cas limite : si A, B, D sont alignés, AB⃗ ∧ AD⃗ = 0⃗ et l'aire est nulle : le « triangle » ABD est aplati.
:::

::: verifie À toi : l'aire d'un triangle
Calculer l'aire du triangle PQR pour P(0 ; 1 ; 2), Q(1 ; 3 ; 2) et R(−1 ; 2 ; 4).

---

PQ⃗(1 ; 2 ; 0) et PR⃗(−1 ; 1 ; 2) donnent PQ⃗ ∧ PR⃗ = (2 × 2 − 0 × 1 ; 0 × (−1) − 1 × 2 ; 1 × 1 − 2 × (−1)) = (4 ; −2 ; 3), de norme √(16 + 4 + 9) = √29. C'est l'aire du parallélogramme : le triangle PQR en vaut la moitié, soit √29 / 2.
:::

::: retenir
‖AB⃗ ∧ AC⃗‖ est l'aire du parallélogramme construit sur AB⃗ et AC⃗, la moitié est l'aire du triangle ABC, et AB⃗ ∧ AC⃗ est orthogonal à AB⃗ et à AC⃗.
:::

## 📏 La distance d'un point à une droite

Un fil rectiligne tendu passe par A et dirigé par u⃗, et un point M est posé à côté. Quelle est la plus courte distance de M au fil, et faut-il chercher le point du fil le plus proche pour la connaître ?
Un produit vectoriel peut-il la donner d'un seul calcul ?

::: definition
La **distance** d'un point M à une droite D est la distance MH, où H est le projeté orthogonal de M sur D. Elle est notée d(M, D).
:::

::: figure Le point M, la droite D de vecteur directeur u⃗ passant par A, et le projeté orthogonal H de M sur D (angle droit en H). Pour tout autre point A de D, le segment MA (en pointillés gris) est plus long que MH, hypoténuse d'un triangle rectangle en H.
<svg viewBox="0 0 290 215">
<title>Le point M, la droite D, le projeté orthogonal H de M sur D et la distance MH</title>
<line x1="-8.64" y1="183.73" x2="305.15" y2="120.97" stroke="#0f172a" stroke-width="2.2"/>
<line x1="168.85" y1="51.35" x2="187.48" y2="144.51" stroke="#b45309" stroke-width="2.6" stroke-dasharray="5 4"/>
<line x1="168.85" y1="51.35" x2="60" y2="170" stroke="#94a3b8" stroke-width="1.6" stroke-dasharray="5 4"/>
<line x1="60" y1="170" x2="122.76" y2="157.45" stroke="#0f6e56" stroke-width="2.8"/>
<polygon points="133.55,155.29 123.66,161.98 121.85,152.92" fill="#0f6e56"/>
<polyline points="176.69,146.66 174.53,135.88 185.32,133.72" fill="none" stroke="#0f172a" stroke-width="1.4"/>
<circle cx="60" cy="170" r="3.5" fill="#0f172a"/>
<text x="56" y="188" text-anchor="middle" fill="#0f172a" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">A</text>
<circle cx="187.48" cy="144.51" r="3.5" fill="#b45309"/>
<text x="197.48" y="162.51" text-anchor="middle" fill="#b45309" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">H</text>
<circle cx="168.85" cy="51.35" r="3.5" fill="#0f172a"/>
<text x="168.85" y="41.35" text-anchor="middle" fill="#0f172a" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">M</text>
<path d="M133.55 134.29 h8 m-3 -2.5 l3 2.5 l-3 2.5" fill="none" stroke="#0f6e56" stroke-width="1.3"/>
<text x="137.55" y="147.29" text-anchor="middle" fill="#0f6e56" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">u</text>
<text x="297.15" y="136.97" text-anchor="middle" fill="#0f172a" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">D</text>
<text x="193.16" y="97.93" text-anchor="middle" fill="#b45309" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">d</text>
</svg>
:::

Sur la figure, MH est la plus courte des distances de M aux points de D, et c'est elle qu'on appelle distance. La preuve de la formule tient en deux lignes : MA⃗ = MH⃗ + HA⃗ et HA⃗ est colinéaire à u⃗, donc MA⃗ ∧ u⃗ = MH⃗ ∧ u⃗ ; comme MH⃗ est orthogonal à u⃗, ‖MH⃗ ∧ u⃗‖ = MH × ‖u⃗‖ × sin(π/2) = MH × ‖u⃗‖.

::: exemple La distance de M(3 ; 0 ; 5) à la droite D passant par A(1 ; −1 ; 0) de vecteur directeur u⃗(2 ; 1 ; 2)

1. MA⃗ a pour coordonnées (−2 ; −1 ; −5).
2. MA⃗ ∧ u⃗ = ((−1) × 2 − (−5) × 1 ; (−5) × 2 − (−2) × 2 ; (−2) × 1 − (−1) × 2) = (3 ; −6 ; 0), de norme √(9 + 36) = 3√5.
3. ‖u⃗‖ = √(4 + 1 + 4) = 3, donc d(M, D) = 3√5 / 3 = √5 ≈ 2,24.
4. Contrôle par Pythagore : AM² = 4 + 1 + 25 = 30 et la projection de AM⃗ sur u⃗ vaut AM⃗ . u⃗ / ‖u⃗‖ = (4 + 1 + 10)/3 = 5, donc d² = 30 − 25 = 5 ✓.

:::

::: piege
**Erreur : oublier de diviser par ‖u⃗‖.** L'erreur tente parce que le produit vectoriel est déjà un vecteur « de la bonne forme ». Pour la droite D passant par O de vecteur directeur u⃗(0 ; 0 ; 2) et le point M(3 ; 4 ; 7), on trouve MO⃗ ∧ u⃗ = (−8 ; 6 ; 0) de norme 10. Mais M est à 5 de l'axe : d = 10/‖u⃗‖ = 10/2 = 5. La norme du produit vectoriel est proportionnelle à celle de u⃗.
:::

::: propriete
Soit D une droite de vecteur directeur u⃗ et A un point de D. La distance d'un point M à D est
$$ d(M, D) = ‖MA⃗ ∧ u⃗‖ / ‖u⃗‖ $$
Cas limite : d(M, D) = 0 si et seulement si MA⃗ ∧ u⃗ = 0⃗, c'est-à-dire si M appartient à D.
:::

Pour décrire les points de D, on écrit AM⃗ = t u⃗ avec t réel : si A(xA ; yA ; zA) et u⃗(a ; b ; c), le point M(t) a pour coordonnées (xA + ta ; yA + tb ; zA + tc). La distance PM(t) d'un point P à ce point courant est minimale pour le projeté orthogonal de P sur D, et sa valeur minimale est d(P, D).

::: verifie À toi : une distance
Calculer la distance du point P(0 ; 1 ; 3) à la droite passant par B(1 ; 0 ; −1) de vecteur directeur u⃗(1 ; 2 ; 2).

---

PB⃗(1 ; −1 ; −4) et ‖u⃗‖ = 3. PB⃗ ∧ u⃗ = ((−1) × 2 − (−4) × 2 ; (−4) × 1 − 1 × 2 ; 1 × 2 − (−1) × 1) = (6 ; −6 ; 3), de norme √(36 + 36 + 9) = 9. Donc d(P, D) = 9/3 = 3.
:::

::: retenir
La distance de M à la droite (A, u⃗) est ‖MA⃗ ∧ u⃗‖ / ‖u⃗‖ : on divise par la norme du vecteur directeur.
:::

## 📦 Le volume d'un parallélépipède et d'un tétraèdre

Un cristal a la forme d'un parallélépipède construit sur trois arêtes AB⃗, AD⃗, AE⃗ issues d'un même sommet. Quel est son volume, et le déterminant de ces trois vecteurs, vu au début du chapitre, a-t-il un lien avec lui ?
Peut-on en déduire aussi le volume d'un tétraèdre ?

::: propriete
Dans un repère orthonormé direct, pour tous vecteurs u⃗, v⃗, w⃗, le réel (u⃗ ∧ v⃗) . w⃗ égale le déterminant de (u⃗, v⃗, w⃗) :
$$ (u⃗ ∧ v⃗) . w⃗ = (v⃗ ∧ w⃗) . u⃗ = (w⃗ ∧ u⃗) . v⃗ = det(u⃗, v⃗, w⃗) $$
:::

::: figure Le parallélépipède construit sur AB⃗, AD⃗ et AE⃗ : la base ABCD est dans un plan horizontal, AM⃗ = AB⃗ ∧ AD⃗ est vertical, et K est le projeté orthogonal de E sur la droite (AM).
<svg viewBox="0 0 290 232">
<title>Le parallélépipède construit sur AB, AD et AE : AM = AB∧AD est vertical, K est le projeté de E sur (AM)</title>
<polygon points="30,200 154,200 185,100.8 61,100.8" fill="#0f6e56" opacity="0.1"/>
<line x1="228.79" y1="178.3" x2="104.79" y2="178.3" stroke="#94a3b8" stroke-width="1.6" stroke-dasharray="5 4"/>
<line x1="104.79" y1="178.3" x2="30" y2="200" stroke="#94a3b8" stroke-width="1.6" stroke-dasharray="5 4"/>
<line x1="104.79" y1="178.3" x2="135.79" y2="79.1" stroke="#94a3b8" stroke-width="1.6" stroke-dasharray="5 4"/>
<line x1="30" y1="200" x2="154" y2="200" stroke="#0f172a" stroke-width="2"/>
<line x1="154" y1="200" x2="228.79" y2="178.3" stroke="#0f172a" stroke-width="2"/>
<line x1="61" y1="100.8" x2="185" y2="100.8" stroke="#0f172a" stroke-width="2"/>
<line x1="185" y1="100.8" x2="259.79" y2="79.1" stroke="#0f172a" stroke-width="2"/>
<line x1="259.79" y1="79.1" x2="135.79" y2="79.1" stroke="#0f172a" stroke-width="2"/>
<line x1="135.79" y1="79.1" x2="61" y2="100.8" stroke="#0f172a" stroke-width="2"/>
<line x1="30" y1="200" x2="61" y2="100.8" stroke="#0f172a" stroke-width="2"/>
<line x1="154" y1="200" x2="185" y2="100.8" stroke="#0f172a" stroke-width="2"/>
<line x1="228.79" y1="178.3" x2="259.79" y2="79.1" stroke="#0f172a" stroke-width="2"/>
<line x1="61" y1="100.8" x2="30" y2="100.8" stroke="#b45309" stroke-width="2.2" stroke-dasharray="5 4"/>
<line x1="30" y1="200" x2="30" y2="43.6" stroke="#b45309" stroke-width="2.8"/>
<polygon points="30,32.6 34.62,43.6 25.38,43.6" fill="#b45309"/>
<circle cx="30" cy="100.8" r="3.5" fill="#b45309"/>
<text x="16" y="38.6" text-anchor="middle" fill="#b45309" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">M</text>
<text x="16" y="104.8" text-anchor="middle" fill="#b45309" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">K</text>
<polyline points="40,100.8 40,110.8 30,110.8" fill="none" stroke="#0f172a" stroke-width="1.3"/>
<circle cx="30" cy="200" r="3.5" fill="#0f172a"/>
<circle cx="154" cy="200" r="3.5" fill="#0f172a"/>
<circle cx="104.79" cy="178.3" r="3.5" fill="#94a3b8"/>
<circle cx="228.79" cy="178.3" r="3.5" fill="#0f172a"/>
<circle cx="61" cy="100.8" r="3.5" fill="#0f172a"/>
<circle cx="185" cy="100.8" r="3.5" fill="#0f172a"/>
<circle cx="135.79" cy="79.1" r="3.5" fill="#0f172a"/>
<circle cx="259.79" cy="79.1" r="3.5" fill="#0f172a"/>
<text x="16" y="216" text-anchor="middle" fill="#0f172a" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">A</text>
<text x="164" y="218" text-anchor="middle" fill="#0f172a" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">B</text>
<text x="92.79" y="172.3" text-anchor="middle" fill="#94a3b8" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">D</text>
<text x="242.79" y="184.3" text-anchor="middle" fill="#0f172a" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">C</text>
<text x="59" y="89.8" text-anchor="middle" fill="#0f172a" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">E</text>
<text x="197" y="92.8" text-anchor="middle" fill="#0f172a" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">F</text>
<text x="131.79" y="69.1" text-anchor="middle" fill="#0f172a" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">H</text>
<text x="273.79" y="73.1" text-anchor="middle" fill="#0f172a" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">G</text>
</svg>
:::

Sur la figure, la base ABCD a pour aire ‖AB⃗ ∧ AD⃗‖ = AM. Le volume est cette aire multipliée par la hauteur AK, distance de E au plan de la base : V = AM × AK. Comme AM⃗ et AK⃗ sont colinéaires, AM × AK = |AM⃗ . AK⃗|. Enfin AE⃗ − AK⃗ = KE⃗ est orthogonal à AM⃗, donc AM⃗ . AE⃗ = AM⃗ . AK⃗, et V = |(AB⃗ ∧ AD⃗) . AE⃗| = |det(AB⃗, AD⃗, AE⃗)|.

::: exemple Le volume d'un parallélépipède

Dans un repère orthonormé direct, on donne O(0 ; 0 ; 0), A(1 ; 0 ; 0), B(0 ; 3 ; 0), C(−1 ; 3 ; 0), D(2 ; 2 ; 2), E(3 ; 2 ; 2), F(2 ; 5 ; 2), G(1 ; 5 ; 2). Montrer que OABCDEFG est un parallélépipède et calculer son volume.

1. OA⃗(1 ; 0 ; 0), OC⃗(−1 ; 3 ; 0) et OD⃗(2 ; 2 ; 2). On a OA⃗ + OC⃗ = (0 ; 3 ; 0) = OB⃗, donc OABC est un parallélogramme.
2. Les sommets du haut sont les translatés de ceux du bas par OD⃗ : OD⃗ + OA⃗ = (3 ; 2 ; 2) = OE⃗, OD⃗ + OB⃗ = (2 ; 5 ; 2) = OF⃗ et OD⃗ + OC⃗ = (1 ; 5 ; 2) = OG⃗. Le solide est un parallélépipède.
3. Son volume est |det(OA⃗, OC⃗, OD⃗)|. Les parenthèses valent 3 × 2 − 0 × 2 = 6, puis (−1) × 2 − 0 × 2 = −2, puis (−1) × 2 − 3 × 2 = −8, d'où det = 1 × 6 − 0 × (−2) + 0 × (−8) = 6. Le volume vaut 6.

:::

::: piege
**Erreur : garder le signe du déterminant et annoncer un volume négatif.** L'erreur tente parce que le calcul peut donner un nombre négatif. Mais un volume est positif : le signe de det dépend seulement de l'ordre des vecteurs, puisque det(OC⃗, OA⃗, OD⃗) = −6 pour ce même solide. On prend toujours la valeur absolue.
:::

::: propriete
L'espace est muni d'un repère orthonormé direct.
• Le volume d'un parallélépipède ABCDEFGH est |det(AB⃗, AD⃗, AE⃗)|.
• Le volume d'un tétraèdre ABCD est (1/6) |det(BC⃗, BD⃗, BA⃗)|, soit un sixième du parallélépipède construit sur les mêmes trois arêtes issues de B (et tout autre sommet convient comme origine).
Cas limite : un déterminant nul signifie que le « solide » est aplati dans un plan, donc de volume nul.
:::

::: exemple Un tétraèdre dans un cube

Le cube ABCDEFGH d'arête a est muni du repère orthonormé direct (A ; AB⃗/a, AD⃗/a, AE⃗/a), et M est le milieu de [BF]. Calculer le volume du tétraèdre MEBG, puis celui du solide obtenu en retirant ce tétraèdre au cube.

1. Les coordonnées sont B(a ; 0 ; 0), E(0 ; 0 ; a), G(a ; a ; a) et M(a ; 0 ; a/2), d'où BE⃗(−a ; 0 ; a), BG⃗(0 ; a ; a) et BM⃗(0 ; 0 ; a/2).
2. BG⃗ ∧ BM⃗ = (a × a/2 − a × 0 ; a × 0 − 0 × a/2 ; 0) = (a²/2 ; 0 ; 0), et det(BE⃗, BG⃗, BM⃗) = BE⃗ . (BG⃗ ∧ BM⃗) = −a × a²/2 = −a³/2.
3. Le volume du tétraèdre est (1/6) × a³/2 = a³/12.
4. Le solide restant a pour volume a³ − a³/12 = 11a³/12. Contrôle : pour a = 1, 1/12 + 11/12 = 1 ✓.

:::

Le volume d'un tétraèdre vaut aussi (1/3) × aire d'une face × hauteur issue du sommet opposé : connaissant le volume V par le déterminant et l'aire S de la face par un produit vectoriel, cette hauteur est h = 3V / S.

::: verifie À toi : le volume d'un tétraèdre
Calculer le volume du tétraèdre ABCD pour A(0 ; 0 ; 0), B(2 ; 0 ; 1), C(1 ; 3 ; 0) et D(0 ; 1 ; 4).

---

AB⃗(2 ; 0 ; 1), AC⃗(1 ; 3 ; 0) et AD⃗(0 ; 1 ; 4). AB⃗ ∧ AC⃗ = (0 × 0 − 1 × 3 ; 1 × 1 − 2 × 0 ; 2 × 3 − 0 × 1) = (−3 ; 1 ; 6), puis det = (−3) × 0 + 1 × 1 + 6 × 4 = 25. Le volume est (1/6) × |25| = 25/6.
:::

::: retenir
(u⃗ ∧ v⃗) . w⃗ est le déterminant de (u⃗, v⃗, w⃗) : sa valeur absolue est le volume du parallélépipède, son sixième celui du tétraèdre.
:::
