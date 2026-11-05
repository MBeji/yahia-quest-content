# ⚔️ Droites et plans de l'espace — tenir l'espace avec des équations

> 💡 «Un point se donne par trois nombres, une droite par un point et une direction, un plan par un point et deux directions : tout le reste n'est que du calcul.»

Ce chapitre apprend à décrire les droites et les plans de l'espace par des nombres, puis à trancher leurs positions relatives par le calcul : parallèles, sécants, confondus ou sans rapport. Huit notions, du déterminant qui teste la colinéarité et la coplanarité jusqu'à la section d'un tétraèdre par un plan. L'espace est rapporté à un repère cartésien (O, i⃗, j⃗, k⃗), pas forcément orthonormé : on n'utilisera ni distance ni angle, seulement la colinéarité et la coplanarité.

## 🔍 Colinéaire ? Coplanaire ? Le déterminant tranche

Un charpentier veut couvrir les quatre sommets A(1, 0, 2), B(3, 1, 1), C(0, 2, 3) et D(2, 3, 4) d'une charpente avec une seule plaque plane.
Est-ce possible ? Autrement dit, les points A, B, C et D sont-ils dans un même plan ? La réponse se lit dans les composantes des vecteurs AB⃗, AC⃗ et AD⃗.

::: definition
Dans la base (i⃗, j⃗, k⃗), soit u⃗(a, b, c), v⃗(a′, b′, c′) et w⃗(a″, b″, c″). Les trois **déterminants d'ordre 2** de u⃗ et v⃗ sont ab′ − a′b, ac′ − a′c et bc′ − b′c. Le **déterminant d'ordre 3** de u⃗, v⃗, w⃗ est le nombre
$$ det(u⃗, v⃗, w⃗) = a(b′c″ − b″c′) − b(a′c″ − a″c′) + c(a′b″ − a″b′) $$
Trois vecteurs sont **coplanaires** si leurs représentants issus d'un même point sont dans un même plan.
:::

::: figure Le point D est à la verticale du plan (ABC), au-dessus du point D′ de ce plan : D n'est pas dans le plan (ABC), donc AB⃗, AC⃗ et AD⃗ ne sont pas coplanaires
<svg viewBox="0 0 340 250">
<title>Le plan (ABC) en parallélogramme ABD′C et le point D hors de ce plan</title>
<path d="M97 99.6 L77.9 216 L228.2 150.4 L247.2 34 Z" fill="#0f6e56" fill-opacity="0.14" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round"/>
<path d="M228.2 150.4 L262.1 57.3" fill="none" stroke="#b45309" stroke-width="2" stroke-dasharray="5 4" stroke-linecap="round"/>
<path d="M97 99.6 L78.8 210.7" fill="none" stroke="#0f6e56" stroke-width="2.2" stroke-linecap="round"/><path d="M77.9 216 L75 206.4 L83.8 207.8 Z" fill="#0f6e56"/>
<path d="M97 99.6 L242.3 36.2" fill="none" stroke="#0f6e56" stroke-width="2.2" stroke-linecap="round"/><path d="M247.2 34 L240.8 41.7 L237.2 33.5 Z" fill="#0f6e56"/>
<circle cx="97" cy="99.6" r="4" fill="#0f172a"/>
<circle cx="77.9" cy="216" r="4" fill="#0f172a"/>
<circle cx="247.2" cy="34" r="4" fill="#0f172a"/>
<circle cx="228.2" cy="150.4" r="3.5" fill="#94a3b8"/>
<circle cx="262.1" cy="57.3" r="5" fill="#b45309"/>
<text x="85" y="103.6" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">A</text>
<text x="89.9" y="222" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">B</text>
<text x="235.2" y="30" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">C</text>
<text x="242.2" y="156.4" text-anchor="middle" font-size="13" font-weight="700" fill="#475569" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">D′</text>
<text x="276.1" y="53.3" text-anchor="middle" font-size="13" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">D</text>
</svg>
:::

Sur la figure, D′ est le quatrième sommet du parallélogramme ABD′C, dans le plan (ABC) : D est au-dessus de D′, donc hors de ce plan, et AB⃗, AC⃗, AD⃗ ne sont pas coplanaires. Le déterminant le confirme par le calcul.

::: exemple Les sommets A, B, C, D sont-ils coplanaires ?

1. On calcule les composantes (extrémité moins origine) : AB⃗(2, 1, −1), AC⃗(−1, 2, 1) et AD⃗(1, 3, 2).
2. A, B, C, D sont coplanaires si et seulement si AB⃗, AC⃗, AD⃗ le sont, c'est-à-dire si leur déterminant est nul.
3. Chaque parenthèse du déterminant est un déterminant d'ordre 2 formé avec les composantes de AC⃗ et AD⃗, les deux derniers vecteurs : b′c″ − b″c′ = 2×2 − 3×1 = 1 ; a′c″ − a″c′ = (−1)×2 − 1×1 = −3 ; a′b″ − a″b′ = (−1)×3 − 1×2 = −5.
4. Alors det = 2×1 − 1×(−3) + (−1)×(−5) = 2 + 3 + 5 = 10. Ce nombre n'est pas nul : les quatre points ne sont pas coplanaires, et une seule plaque plane ne suffit pas.

:::

::: exemple Deux vecteurs colinéaires ?
Pour u⃗(2, −4, 6) et v⃗(−1, 2, −3) :

1. Coordonnées en x et y : ab′ − a′b = 2×2 − (−1)×(−4) = 4 − 4 = 0.
2. Coordonnées en x et z : ac′ − a′c = 2×(−3) − (−1)×6 = −6 + 6 = 0.
3. Coordonnées en y et z : bc′ − b′c = (−4)×(−3) − 2×6 = 12 − 12 = 0.
4. Les trois déterminants sont nuls : u⃗ et v⃗ sont colinéaires, et l'on voit que v⃗ = −(1/2) u⃗.

:::

::: piege
**Erreur : ne calculer qu'un seul des trois déterminants d'ordre 2.** L'erreur tente parce que, dans le plan, un seul déterminant suffit. Mais dans l'espace, u⃗(1, 2, 3) et v⃗(2, 4, 7) donnent ab′ − a′b = 1×4 − 2×2 = 0, alors que ac′ − a′c = 1×7 − 2×3 = 1 : ils ne sont pas colinéaires. Il faut les trois déterminants.
:::

::: propriete
Dans la base (i⃗, j⃗, k⃗) :
- u⃗ et v⃗ sont colinéaires si et seulement si les trois déterminants d'ordre 2 sont nuls ;
- u⃗, v⃗, w⃗ sont coplanaires si et seulement si det(u⃗, v⃗, w⃗) = 0 ;
- quatre points A, B, C, D sont coplanaires si et seulement si AB⃗, AC⃗, AD⃗ le sont.

Cas limite : si l'un des vecteurs est nul ou si deux d'entre eux sont colinéaires, le déterminant est nul, car trois vecteurs dont deux sont colinéaires sont toujours coplanaires.
:::

::: verifie À toi : une valeur de m pour la coplanarité
Pour quelle valeur de m les vecteurs u⃗(1, 0, 2), v⃗(−1, 1, 0) et w⃗(m, 3, 4) sont-ils coplanaires ?

---

On écrit det = 0 : b′c″ − b″c′ = 1×4 − 3×0 = 4 ; a′c″ − a″c′ = (−1)×4 − m×0 = −4 ; a′b″ − a″b′ = (−1)×3 − m×1 = −3 − m. Alors det = 1×4 − 0×(−4) + 2×(−3 − m) = −2 − 2m, nul pour m = −1. Contrôle : w⃗(−1, 3, 4) = 2u⃗ + 3v⃗, car 2×1 + 3×(−1) = −1, 3×1 = 3 et 2×2 = 4 ✓.
:::

::: retenir
Deux vecteurs sont colinéaires si les trois déterminants d'ordre 2 sont nuls ; trois vecteurs (ou quatre points, par les vecteurs AB⃗, AC⃗, AD⃗) sont coplanaires si le déterminant d'ordre 3 est nul.
:::

## 🧭 Une droite se décrit avec un paramètre

Un drone part du point A(2, −1, 3) et vole en ligne droite : à chaque minute, il avance de 3 unités selon i⃗, de 2 selon j⃗ et descend de 6 selon k⃗.
Où se trouve-t-il après λ minutes, et comment décrire par des nombres toute la droite qu'il suit ?

::: definition
Soit A(x₀, y₀, z₀) un point et u⃗(a, b, c) un vecteur non nul. La droite D passant par A et de **vecteur directeur** u⃗ est l'ensemble des points M tels que AM⃗ = λu⃗ avec λ réel. En coordonnées, M(x, y, z) est sur D si et seulement s'il existe un réel λ tel que
$$ x = x₀ + λa ;  y = y₀ + λb ;  z = z₀ + λc $$
Ce système, où λ décrit ℝ, est une **représentation paramétrique** de D.
:::

::: figure La droite D passe par A avec le vecteur directeur u⃗ : chaque valeur de λ donne un point, λ = 0 pour A et λ = 1 pour B = A + u⃗
<svg viewBox="0 0 340 250">
<title>Droite D de point A et de vecteur directeur u, avec les points obtenus pour λ = −1, 0, 1, 2</title>
<path d="M89.7 40 L250.3 210" fill="none" stroke="#0f172a" stroke-width="2.2" stroke-linecap="round"/>
<path d="M147.7 101.4 L188.6 144.7" fill="none" stroke="#0f6e56" stroke-width="3" stroke-linecap="round"/><path d="M192.3 148.6 L182.8 145.2 L189.4 139 Z" fill="#0f6e56"/>
<circle cx="103.1" cy="54.2" r="4.5" fill="#0f172a"/>
<circle cx="147.7" cy="101.4" r="4.5" fill="#0f6e56"/>
<circle cx="192.3" cy="148.6" r="4.5" fill="#0f6e56"/>
<circle cx="236.9" cy="195.8" r="4.5" fill="#0f172a"/>
<text x="147.1" y="58.2" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">λ = −1</text>
<text x="193.7" y="97.4" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">A (λ = 0)</text>
<text x="238.3" y="146.6" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">B (λ = 1)</text>
<text x="276.9" y="193.8" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">λ = 2</text>
<text x="158" y="125" text-anchor="middle" font-size="13" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">u⃗</text>
</svg>
:::

Sur la figure, B est la position du drone après une minute : B = A + u⃗ avec u⃗(3, 2, −6). Dans chaque équation, la constante est la coordonnée de A et le coefficient de λ est celle de u⃗.

::: exemple La droite (AB) pour A(2, −1, 3) et B(5, 1, −3)

1. Le vecteur directeur est AB⃗ = (5 − 2, 1 − (−1), −3 − 3) = (3, 2, −6) : c'est le déplacement du drone en une minute.
2. On écrit A + λAB⃗ : x = 2 + 3λ ; y = −1 + 2λ ; z = 3 − 6λ.
3. Contrôle : pour λ = 1, on retrouve (5, 1, −3) = B ✓.
4. C(8, 3, −9) est-il sur la droite ? La première équation donne 2 + 3λ = 8, donc λ = 2 ; avec cette valeur, y = −1 + 4 = 3 et z = 3 − 12 = −9 : les trois coordonnées conviennent, donc C ∈ (AB).
5. Pour F(8, 3, −8), la valeur λ = 2 convient pour x et y, mais z = −9 ≠ −8 : F ∉ (AB). Une même valeur de λ doit convenir aux trois équations.

:::

::: piege
**Erreur : lire le vecteur directeur dans les constantes.** L'erreur tente parce que ce sont les premiers nombres écrits. Mais pour D : x = 4 − λ ; y = 1 + 2λ ; z = −2 + 5λ, les constantes (4, 1, −2) sont les coordonnées d'un point (celui obtenu pour λ = 0), et le vecteur directeur est formé des coefficients de λ : (−1, 2, 5).
:::

::: propriete
La droite D(A, u⃗) a pour représentation paramétrique le système ci-dessus, et un point est sur D si et seulement si **une même valeur** de λ convient aux trois équations.
Une droite a une infinité de représentations paramétriques : on peut changer de point de départ ou remplacer u⃗ par un multiple non nul. Deux droites D(A, u⃗) et D(A′, v⃗) sont parallèles si et seulement si u⃗ et v⃗ sont colinéaires.
Cas limite : si une coordonnée de u⃗ est nulle, la coordonnée correspondante reste constante. Pour A(4, 0, 2) et u⃗(0, 1, 3), on obtient x = 4 ; y = λ ; z = 2 + 3λ : tous les points de D ont pour abscisse 4.
:::

::: verifie À toi : une droite avec une coordonnée constante
Donner une représentation paramétrique de la droite (EF) pour E(0, 4, −1) et F(2, 4, 5), puis dire si G(3, 4, 8) appartient à (EF).

---

On a EF⃗(2, 0, 6), donc x = 2λ ; y = 4 ; z = −1 + 6λ : la coordonnée y du vecteur est nulle, donc y reste constant. Pour G, x = 2λ = 3 donne λ = 3/2, puis z = −1 + 9 = 8 et y = 4 : les trois équations conviennent avec la même valeur de λ, donc G ∈ (EF).
:::

::: retenir
Une droite se donne par un point A et un vecteur directeur u⃗ : x = x₀ + λa, y = y₀ + λb, z = z₀ + λc ; la constante est le point, le coefficient de λ est la direction, et une seule valeur de λ doit convenir aux trois équations.
:::

## 🪞 Droite : le système de deux équations

Dans une salle, le mur du fond et le plafond se rencontrent suivant une arête, qui est une droite.
Pour la décrire sans paramètre, il suffit de donner l'équation du mur et celle du plafond : l'arête est l'ensemble des points qui vérifient les deux. Comment passer de cette description à la précédente, et inversement ?

::: definition
Une droite D peut aussi être décrite par un système de deux équations du premier degré en x, y, z, dont chacune est l'équation d'un plan (notion 5) : D est l'intersection de ces deux plans. Ce système est une **représentation cartésienne** de D.
:::

Voici la droite (AB) du drone dans les deux écritures ; l'exemple montre comment passer de l'une à l'autre.

| | Représentation paramétrique | Représentation cartésienne |
| --- | --- | --- |
| La droite (AB) | x = 2 + 3λ ; y = −1 + 2λ ; z = 3 − 6λ | 2x − 3y − 7 = 0 ; 2x + z − 7 = 0 |
| Trouver un point | choisir λ | résoudre le système |
| Tester un point | une même valeur de λ pour les trois coordonnées | vérifier les deux équations |

Dans chaque ligne, l'écriture de gauche et celle de droite décrivent la même droite : le paramètre λ a disparu à droite.

::: exemple De la forme paramétrique à la forme cartésienne
Pour D : x = 2 + 3λ ; y = −1 + 2λ ; z = 3 − 6λ.

1. On isole λ dans la première équation (son coefficient 3 n'est pas nul) : λ = (x − 2)/3.
2. On remplace dans y : y = −1 + 2(x − 2)/3, soit 3y = −3 + 2x − 4, donc 2x − 3y − 7 = 0. Le paramètre est éliminé.
3. On remplace dans z : z = 3 − 6(x − 2)/3 = 3 − 2(x − 2) = 7 − 2x, donc 2x + z − 7 = 0.
4. Contrôle : A(2, −1, 3) donne 4 + 3 − 7 = 0 et 4 + 3 − 7 = 0 ✓ ; B(5, 1, −3) donne 10 − 3 − 7 = 0 et 10 − 3 − 7 = 0 ✓.

:::

::: exemple De la forme cartésienne à la forme paramétrique
Pour D : x + 2y − z − 3 = 0 ; 2x − y + z = 0.

1. On additionne les deux équations pour éliminer z : 3x + y − 3 = 0, donc y = 3 − 3x.
2. On prend x comme paramètre : x = λ, donc y = 3 − 3λ.
3. La première équation donne z = x + 2y − 3 = λ + 6 − 6λ − 3 = 3 − 5λ.
4. Ainsi D : x = λ ; y = 3 − 3λ ; z = 3 − 5λ. Contrôle avec la deuxième équation : 2λ − (3 − 3λ) + (3 − 5λ) = 0 ✓. D passe par (0, 3, 3) et son vecteur directeur est (1, −3, −5).

:::

::: piege
**Erreur : ne garder qu'une seule des deux équations.** L'erreur tente parce qu'une équation a déjà permis de calculer z. Mais x + 2y − z − 3 = 0 seule est l'équation d'un plan : le point (3, 0, 0) la vérifie (3 − 3 = 0) sans être sur D, car 2×3 − 0 + 0 = 6 ≠ 0. Un point est sur D s'il vérifie les deux équations.
:::

::: propriete
Pour passer d'une représentation paramétrique à une cartésienne, on isole λ dans une équation dont le coefficient de λ n'est pas nul, puis on le reporte dans les deux autres. Pour passer d'une cartésienne à une paramétrique, on élimine une inconnue entre les deux équations, puis on prend une autre inconnue comme paramètre. Une droite a une infinité de représentations, paramétriques comme cartésiennes.
Cas limite : si une coordonnée de u⃗ est nulle, l'équation correspondante est déjà cartésienne. Pour x = 2λ ; y = 4 ; z = −1 + 6λ, le système y − 4 = 0 ; 3x − z − 1 = 0 convient.
:::

::: verifie À toi : de la forme cartésienne à la forme paramétrique
Donner une représentation paramétrique de D : x − y + z − 2 = 0 ; 2x + y − z − 1 = 0.

---

En additionnant les deux équations, y et z disparaissent : 3x − 3 = 0, donc x = 1. La première équation devient −y + z − 1 = 0, soit y = z − 1 ; en prenant z = λ, on obtient D : x = 1 ; y = −1 + λ ; z = λ. Contrôle avec la deuxième équation : 2 + (−1 + λ) − λ − 1 = 0 ✓.
:::

::: retenir
Une droite se décrit aussi par deux équations de plans : un point lui appartient s'il vérifie les deux, et l'on passe d'une écriture à l'autre en éliminant λ ou en prenant une inconnue comme paramètre.
:::

## ✂️ Deux droites : parallèles, sécantes ou non coplanaires

Deux câbles traversent un hangar. Le premier passe par A(1, 2, 0) avec la direction u⃗(2, −1, 1) ; le second passe par K(1, −3, 3) avec la direction v⃗(1, 2, −1).
Se croisent-ils, sont-ils parallèles, ou l'un passe-t-il au-dessus de l'autre sans le toucher ?

::: definition
Deux droites sont **coplanaires** s'il existe un plan qui les contient toutes les deux. Deux droites de l'espace sont dans l'une de ces quatre positions : **strictement parallèles** (aucun point commun), **confondues**, **sécantes** (un seul point commun) ou **non coplanaires** (aucun point commun et aucun plan ne les contient).
:::

::: figure Les quatre positions de deux droites : les trois premières cases sont planes, dans la dernière D′ passe au-dessus de D sans jamais la rencontrer
<svg viewBox="0 0 340 290">
<title>Deux droites parallèles, confondues, sécantes, puis non coplanaires, dans quatre cases</title>
<path d="M60.4 48.1 L24 75.9 L109.6 75.9 L146 48.1 Z" fill="#0f6e56" fill-opacity="0.1" stroke="#94a3b8" stroke-width="1" stroke-linejoin="round"/>
<path d="M55.9 54.3 L134.3 54.3" fill="none" stroke="#0f6e56" stroke-width="2.4" stroke-linecap="round"/>
<path d="M35.7 69.7 L114.1 69.7" fill="none" stroke="#b45309" stroke-width="2.4" stroke-linecap="round"/>
<text x="146.3" y="50.3" text-anchor="middle" font-size="13" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">D</text>
<text x="128.1" y="65.7" text-anchor="middle" font-size="13" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">D′</text>
<text x="85" y="126" text-anchor="middle" font-size="12" font-weight="600" fill="#475569" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">strictement parallèles</text>
<path d="M230.4 48.1 L194 75.9 L279.6 75.9 L316 48.1 Z" fill="#0f6e56" fill-opacity="0.1" stroke="#94a3b8" stroke-width="1" stroke-linejoin="round"/>
<path d="M215.8 62 L294.2 62" fill="none" stroke="#0f6e56" stroke-width="4.5" stroke-linecap="round"/>
<path d="M215.8 62 L294.2 62" fill="none" stroke="#b45309" stroke-width="1.6" stroke-dasharray="6 5" stroke-linecap="round"/>
<text x="211.8" y="86" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">D = D′</text>
<text x="255" y="126" text-anchor="middle" font-size="12" font-weight="600" fill="#475569" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">confondues</text>
<path d="M60.4 192.1 L24 219.9 L109.6 219.9 L146 192.1 Z" fill="#0f6e56" fill-opacity="0.1" stroke="#94a3b8" stroke-width="1" stroke-linejoin="round"/>
<path d="M45.8 206 L124.2 206" fill="none" stroke="#0f6e56" stroke-width="2.4" stroke-linecap="round"/>
<path d="M108.3 193.6 L76 218.4" fill="none" stroke="#b45309" stroke-width="2.4" stroke-linecap="round"/>
<circle cx="92.1" cy="206" r="4.5" fill="#0f172a"/>
<text x="81.1" y="200" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">I</text>
<text x="136.2" y="202" text-anchor="middle" font-size="13" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">D</text>
<text x="90" y="222.4" text-anchor="middle" font-size="13" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">D′</text>
<text x="85" y="270" text-anchor="middle" font-size="12" font-weight="600" fill="#475569" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">sécantes</text>
<path d="M230.4 209.5 L194 237.3 L279.6 237.3 L316 209.5 Z" fill="#0f6e56" fill-opacity="0.1" stroke="#94a3b8" stroke-width="1" stroke-linejoin="round"/>
<path d="M230.4 166.7 L194 194.5 L279.6 194.5 L316 166.7 Z" fill="#b45309" fill-opacity="0.08" stroke="#94a3b8" stroke-width="1" stroke-linejoin="round"/>
<path d="M215.8 223.4 L294.2 223.4" fill="none" stroke="#0f6e56" stroke-width="2.4" stroke-linecap="round"/>
<path d="M278.3 168.2 L246 193" fill="none" stroke="#b45309" stroke-width="2.4" stroke-linecap="round"/>
<text x="306.2" y="221.4" text-anchor="middle" font-size="13" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">D</text>
<text x="260" y="189" text-anchor="middle" font-size="13" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">D′</text>
<text x="255" y="270" text-anchor="middle" font-size="12" font-weight="600" fill="#475569" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">non coplanaires</text>
</svg>
:::

Sur la figure, les trois premières positions se dessinent dans un même plan ; dans la quatrième, D′ passe au-dessus de D, et aucun plan ne contient les deux droites.

::: exemple Les deux câbles se croisent-ils ?
Les deux droites sont D : x = 1 + 2λ ; y = 2 − λ ; z = λ et D′ : x = 1 + μ ; y = −3 + 2μ ; z = 3 − μ.

1. Les vecteurs directeurs sont u⃗(2, −1, 1) et v⃗(1, 2, −1). Le déterminant d'ordre 2 en x et y vaut 2×2 − 1×(−1) = 5 ≠ 0 : ils ne sont pas colinéaires, donc D et D′ ne sont ni parallèles ni confondues.
2. Un point commun correspond à une valeur λ sur D et à une valeur μ sur D′, a priori différentes : on écrit 1 + 2λ = 1 + μ ; 2 − λ = −3 + 2μ ; λ = 3 − μ.
3. La première équation donne μ = 2λ ; dans la deuxième, 2 − λ = −3 + 4λ, donc λ = 1 et μ = 2.
4. On vérifie la troisième : λ = 3 − μ donne 1 = 1 ✓. Le système a une solution : D et D′ sont sécantes en I, obtenu pour λ = 1, soit I(3, 1, 1). Avec μ = 2, on retrouve (3, 1, 1) ✓.

:::

::: exemple Trois autres positions
Soit D comme ci-dessus.

1. Si l'on change la constante de z dans D′ en z = 4 − μ, les vecteurs directeurs restent non colinéaires, et les deux premières équations donnent encore λ = 1 et μ = 2. La troisième devient λ = 4 − μ, soit 1 = 2 : le système n'a pas de solution, D et D′ sont non coplanaires.
2. Soit Δ de vecteur directeur (−4, 2, −2) passant par (5, 0, 1). Comme (−4, 2, −2) = −2u⃗, Δ est parallèle à D. Le point (5, 0, 1) est sur D si 1 + 2λ = 5, donc λ = 2, et alors z = 2 ≠ 1 : il n'est pas sur D, donc Δ est strictement parallèle à D.
3. Si Δ passait par (5, 0, 2), ce point serait sur D (λ = 2 donne (5, 0, 2)), et Δ serait confondue avec D.

:::

::: piege
**Erreur : appeler λ le paramètre des deux droites.** L'erreur tente parce qu'on écrit les deux systèmes avec la même lettre. Mais le point commun n'a aucune raison de correspondre à la même valeur sur les deux droites. Avec λ partout, 1 + 2λ = 1 + λ donne λ = 0, puis 2 − 0 = 2 ≠ −3 + 0 : on conclurait à tort « aucun point commun », alors que I(3, 1, 1) existe, pour λ = 1 sur D et μ = 2 sur D′.
:::

::: propriete
Soit D(A, u⃗) et D′(A′, v⃗) deux droites.
- Si u⃗ et v⃗ sont colinéaires, D et D′ sont parallèles : confondues si A ∈ D′, strictement parallèles sinon.
- Si u⃗ et v⃗ ne sont pas colinéaires, D et D′ sont sécantes quand le système en (λ, μ) a une solution, et non coplanaires quand il n'en a aucune.

Les droites parallèles, confondues ou sécantes sont coplanaires ; les droites non coplanaires ne le sont pas.
Cas limite : quand les vecteurs directeurs sont colinéaires, le système en (λ, μ) n'a jamais une solution unique : il en a une infinité (droites confondues) ou aucune (droites strictement parallèles).
:::

::: verifie À toi : sécantes ou non coplanaires ?
Soit D : x = 1 + λ ; y = 2λ ; z = −1 + λ et D′ : x = 4 − 2μ ; y = −1 + 3μ ; z = 2 − 2μ. Quelle est leur position relative ?

---

Les vecteurs directeurs (1, 2, 1) et (−2, 3, −2) ne sont pas colinéaires : 1×3 − (−2)×2 = 7 ≠ 0. On résout 1 + λ = 4 − 2μ ; 2λ = −1 + 3μ ; −1 + λ = 2 − 2μ. La première donne λ = 3 − 2μ, la deuxième 6 − 4μ = −1 + 3μ, donc μ = 1 et λ = 1. La troisième donne 0 = 0 ✓ : D et D′ sont sécantes en I(2, 2, 0).
:::

::: retenir
Vecteurs directeurs colinéaires : droites parallèles ou confondues, selon qu'un point de l'une est ou non sur l'autre ; sinon, on résout le système avec deux paramètres distincts λ et μ : une solution donne des droites sécantes, aucune des droites non coplanaires.
:::

## 🧱 Un plan : deux paramètres ou une équation

Trois piquets A(1, 0, 2), B(2, 2, 1) et C(0, 1, 4) tiennent une plaque plane.
Comment décrire tous les points du plan que prolonge cette plaque : avec des paramètres, comme pour une droite, ou avec une seule équation ?

::: definition
Soit A(x₀, y₀, z₀) un point et u⃗(a, b, c), v⃗(a′, b′, c′) deux vecteurs non colinéaires. Le plan P passant par A et de **vecteurs directeurs** u⃗ et v⃗ est l'ensemble des points M tels que AM⃗ = λu⃗ + μv⃗, avec λ et μ réels. En coordonnées :
$$ x = x₀ + λa + μa′ ;  y = y₀ + λb + μb′ ;  z = z₀ + λc + μc′ $$
Ce système, où (λ, μ) décrit ℝ², est une **représentation paramétrique** de P.
:::

::: figure Le plan P est parcouru par M = A + λu⃗ + μv⃗ : on part de A, on avance de λ fois u⃗, puis de μ fois v⃗ (ici λ = 1,5 et μ = 0,5)
<svg viewBox="0 0 340 250">
<title>Plan P de point A et de vecteurs directeurs u et v, avec un point M</title>
<path d="M97.6 138.2 L175.3 216 L242.4 111.8 L164.7 34 Z" fill="#0f6e56" fill-opacity="0.12" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round"/>
<path d="M114.7 132.5 L176.1 193.9" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-dasharray="5 4" stroke-linecap="round"/>
<path d="M176.1 193.9 L198.5 159.2" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-dasharray="5 4" stroke-linecap="round"/>
<path d="M114.7 132.5 L151.8 169.6" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linecap="round"/><path d="M155.6 173.5 L146.1 170.3 L152.4 163.9 Z" fill="#0f6e56"/>
<path d="M114.7 132.5 L156.5 67.6" fill="none" stroke="#b45309" stroke-width="2.6" stroke-linecap="round"/><path d="M159.4 63 L158.3 73 L150.8 68.2 Z" fill="#b45309"/>
<circle cx="114.7" cy="132.5" r="4" fill="#0f172a"/>
<circle cx="198.5" cy="159.2" r="5" fill="#0f172a"/>
<text x="102.7" y="138.5" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">A</text>
<text x="212.5" y="155.2" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">M</text>
<text x="155.6" y="165.5" text-anchor="middle" font-size="13" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">u⃗</text>
<text x="155.4" y="55" text-anchor="middle" font-size="13" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">v⃗</text>
<text x="256.4" y="111.8" text-anchor="middle" font-size="15" font-weight="700" fill="#475569" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">P</text>
</svg>
:::

Sur la figure, M s'obtient depuis A en avançant de λ fois u⃗ puis de μ fois v⃗ : λ et μ sont les deux « coordonnées » de M dans le plan.

::: exemple Le plan (ABC) : des paramètres à l'équation

1. AB⃗(1, 2, −1) et AC⃗(−1, 1, 2) ne sont pas colinéaires (1×1 − (−1)×2 = 3 ≠ 0) : A, B, C déterminent un plan.
2. Une représentation paramétrique est x = 1 + λ − μ ; y = 2λ + μ ; z = 2 − λ + 2μ.
3. M(x, y, z) est dans le plan si et seulement si AM⃗(x − 1, y, z − 2), AB⃗ et AC⃗ sont coplanaires, c'est-à-dire si leur déterminant est nul.
4. Avec (a, b, c) = (x − 1, y, z − 2) : b′c″ − b″c′ = 2×2 − 1×(−1) = 5 ; a′c″ − a″c′ = 1×2 − (−1)×(−1) = 1 ; a′b″ − a″b′ = 1×1 − (−1)×2 = 3. Le déterminant vaut 5(x − 1) − y + 3(z − 2), d'où l'équation 5x − y + 3z − 11 = 0.
5. Contrôle : A donne 5 − 0 + 6 − 11 = 0 ✓ ; B(2, 2, 1) donne 10 − 2 + 3 − 11 = 0 ✓ ; C(0, 1, 4) donne 0 − 1 + 12 − 11 = 0 ✓.

:::

::: piege
**Erreur : prendre (a, b, c) pour un vecteur du plan.** L'erreur tente parce que (5, −1, 3) est le premier triplet lu dans 5x − y + 3z − 11 = 0. Mais ce triplet n'est pas un vecteur du plan : 5×5 + (−1)×(−1) + 3×3 = 35 ≠ 0. Un vecteur u⃗(α, β, γ) est un vecteur de P si et seulement si aα + bβ + cγ = 0 ; par exemple AB⃗(1, 2, −1) : 5×1 − 1×2 + 3×(−1) = 0 ✓.
:::

::: propriete
L'espace est muni d'un repère (O, i⃗, j⃗, k⃗).
- Tout plan a une équation cartésienne ax + by + cz + d = 0, avec (a, b, c) ≠ (0, 0, 0) ; réciproquement, toute équation de cette forme est celle d'un plan.
- Un vecteur u⃗(α, β, γ) est un vecteur du plan P : ax + by + cz + d = 0 si et seulement si aα + bβ + cγ = 0.
- Pour passer de l'équation aux paramètres, on isole une inconnue et l'on prend les deux autres comme paramètres : pour 2x − y + 4z − 6 = 0, avec x = λ et z = μ, on obtient y = −6 + 2λ + 4μ.

Cas limite : si un coefficient est nul, le plan contient la direction de l'axe correspondant. Le plan 2x − 3z + 1 = 0 (b = 0) contient le vecteur j⃗(0, 1, 0), car 2×0 − 3×0 = 0.
:::

::: verifie À toi : équation du plan (ABC)
Donner une équation cartésienne du plan passant par A(0, 1, 1), B(1, 1, 3) et C(2, 0, 1).

---

AB⃗(1, 0, 2) et AC⃗(2, −1, 0) ne sont pas colinéaires (1×(−1) − 2×0 = −1 ≠ 0). Avec (a, b, c) = (x, y − 1, z − 1) : b′c″ − b″c′ = 0×0 − (−1)×2 = 2 ; a′c″ − a″c′ = 1×0 − 2×2 = −4 ; a′b″ − a″b′ = 1×(−1) − 2×0 = −1. Le déterminant vaut 2x + 4(y − 1) − (z − 1), d'où 2x + 4y − z − 3 = 0. Contrôle : A donne 0 + 4 − 1 − 3 = 0, B donne 2 + 4 − 3 − 3 = 0 et C donne 4 + 0 − 1 − 3 = 0 ✓.
:::

::: retenir
Un plan se donne par un point et deux vecteurs non colinéaires (deux paramètres) ou par une équation ax + by + cz + d = 0 ; M est dans le plan (ABC) si det(AM⃗, AB⃗, AC⃗) = 0, et u⃗(α, β, γ) est un vecteur du plan si aα + bβ + cγ = 0.
:::

## 🪟 Deux plans : parallèles ou sécants

Deux vitres sont posées dans un atelier : P : x + 2y + 3z − 4 = 0 et Q : 3x + 6y + 9z + 2 = 0.
Se coupent-elles, ou restent-elles parallèles ? Et si elles se coupent, suivant quelle droite ?

::: definition
Deux plans P et P′ sont **parallèles** si tout vecteur de l'un est un vecteur de l'autre : ils sont alors confondus (P = P′) ou strictement parallèles (P ∩ P′ = ∅). Sinon, ils sont **sécants** : il existe un vecteur de l'un qui n'est pas un vecteur de l'autre, et P ∩ P′ est une droite.
:::

::: figure Deux plans sont parallèles (distincts ou confondus) ou sécants : dans ce cas leur intersection est une droite D
<svg viewBox="0 0 340 170">
<title>Deux plans parallèles, confondus, puis sécants suivant une droite</title>
<path d="M38.9 68.1 L16 86.4 L77.1 86.4 L100 68.1 Z" fill="#0f6e56" fill-opacity="0.14" stroke="#0f172a" stroke-width="1.4" stroke-linejoin="round"/>
<path d="M38.9 43.6 L16 61.9 L77.1 61.9 L100 43.6 Z" fill="#b45309" fill-opacity="0.14" stroke="#0f172a" stroke-width="1.4" stroke-linejoin="round"/>
<text x="89.1" y="92.4" text-anchor="middle" font-size="13" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">P</text>
<text x="89.1" y="61.9" text-anchor="middle" font-size="13" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">Q</text>
<text x="58" y="150" text-anchor="middle" font-size="12" font-weight="600" fill="#475569" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">disjoints</text>
<path d="M150.9 55.8 L128 74.2 L189.1 74.2 L212 55.8 Z" fill="#0f6e56" fill-opacity="0.14" stroke="#0f172a" stroke-width="1.4" stroke-linejoin="round"/>
<text x="185.1" y="92.2" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">P = Q</text>
<text x="170" y="150" text-anchor="middle" font-size="12" font-weight="600" fill="#475569" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">confondus</text>
<path d="M262.9 65 L240 83.3 L301.1 83.3 L324 65 Z" fill="#0f6e56" fill-opacity="0.14" stroke="#0f172a" stroke-width="1.4" stroke-linejoin="round"/>
<path d="M251.5 86.4 L251.5 43.6 L312.5 43.6 L312.5 86.4 Z" fill="#b45309" fill-opacity="0.14" stroke="#0f172a" stroke-width="1.4" stroke-linejoin="round"/>
<path d="M251.5 74.2 L312.5 74.2" fill="none" stroke="#0f172a" stroke-width="3.4" stroke-linecap="round"/>
<text x="237.5" y="72.2" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">D</text>
<text x="313.1" y="89.3" text-anchor="middle" font-size="13" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">P</text>
<text x="324.5" y="43.6" text-anchor="middle" font-size="13" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">Q</text>
<text x="282" y="150" text-anchor="middle" font-size="12" font-weight="600" fill="#475569" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">sécants</text>
</svg>
:::

Dans les deux premières cases, P et Q ont les mêmes vecteurs : ils « penchent » pareil. Dans la troisième, un vecteur de Q sort de P, et leur intersection est la droite D.

::: exemple P et Q sont-ils parallèles ?

1. Les coefficients de P sont (1, 2, 3) et ceux de Q sont (3, 6, 9) = 3×(1, 2, 3) : ils sont proportionnels. Les vecteurs de P vérifient α + 2β + 3γ = 0, ce sont aussi ceux de Q (3α + 6β + 9γ = 0) : P et Q sont parallèles.
2. Sont-ils confondus ? Un plan confondu avec P aurait une équation multiple de celle de P, comme 3×(x + 2y + 3z − 4) = 3x + 6y + 9z − 12. Or Q a pour constante +2, pas −12 : les plans ne sont pas confondus.
3. Vérification sur un point : (4, 0, 0) est dans P (4 − 4 = 0), mais 3×4 + 2 = 14 ≠ 0 : il n'est pas dans Q. P et Q sont strictement parallèles.

:::

::: exemple Deux plans sécants
Soit P comme ci-dessus et R : 2x + y + 3z − 5 = 0.

1. Les coefficients (1, 2, 3) et (2, 1, 3) ne sont pas proportionnels : le vecteur (3, 0, −1) est dans P (3 + 0 − 3 = 0) mais pas dans R (6 + 0 − 3 = 3 ≠ 0). Les plans sont sécants.
2. On cherche P ∩ R. En soustrayant les deux équations, on élimine z : −x + y + 1 = 0, donc y = x − 1.
3. On reporte dans P : x + 2(x − 1) + 3z − 4 = 0, donc z = 2 − x.
4. Avec x = λ : D : x = λ ; y = −1 + λ ; z = 2 − λ. Contrôle avec R : 2λ + (−1 + λ) + 3(2 − λ) − 5 = 0 ✓.

:::

::: piege
**Erreur : conclure « confondus » dès que (a, b, c) sont proportionnels.** L'erreur tente parce que les deux équations se ressemblent beaucoup. Mais la proportionnalité de (a, b, c) ne donne que le parallélisme : il faut encore comparer d. Pour confondre P et Q, il faudrait que (1, 2, 3, −4) soit proportionnel à (3, 6, 9, 2), ce qui est faux : les deux plans ne se rencontrent pas.
:::

::: propriete
Soit P : ax + by + cz + d = 0 et P′ : a′x + b′y + c′z + d′ = 0.
- P et P′ sont parallèles si et seulement si (a, b, c) = k(a′, b′, c′) pour un réel k non nul. Si a′, b′, c′ sont tous non nuls, cela s'écrit a/a′ = b/b′ = c/c′.
- Ils sont confondus si de plus d = kd′, strictement parallèles sinon.
- Dans les autres cas, ils sont sécants suivant une droite, dont on obtient une représentation en résolvant le système des deux équations.

Cas limite : x + 2z − 1 = 0 et y − 2z + 4 = 0 ont pour coefficients (1, 0, 2) et (0, 1, −2), non proportionnels : les quotients a/a′ n'ont pas de sens ici (a′ = 0), mais les plans sont bien sécants.
:::

::: verifie À toi : parallèles, confondus ou sécants ?
Soit P : 2x − 4y + 6z + 1 = 0 et Q : −x + 2y − 3z + 5 = 0. Quelle est leur position relative ?

---

On a (2, −4, 6) = −2×(−1, 2, −3) : les coefficients sont proportionnels, donc les plans sont parallèles. Pour être confondus, il faudrait 1 = −2×5 = −10, ce qui est faux : P et Q sont strictement parallèles.
:::

::: retenir
Deux plans sont parallèles si (a, b, c) = k(a′, b′, c′), confondus si d = kd′ en plus, strictement parallèles sinon ; dans tous les autres cas, ils sont sécants suivant une droite.
:::

## 🎯 Droite et plan : un point, aucun, ou tous

Un rayon laser traverse un atelier : il suit la droite D : x = 1 + λ ; y = 3 + λ ; z = λ, et une vitre occupe le plan P : 2x − y + 3z − 7 = 0. Le rayon perce-t-il la vitre, la longe-t-il sans la toucher, ou est-il posé dessus ?

::: figure Une droite et un plan : un seul point commun (sécante), aucun (strictement parallèle) ou tous les points de la droite (incluse)
<svg viewBox="0 0 340 170">
<title>Droite sécante au plan, strictement parallèle au plan, incluse dans le plan</title>
<path d="M38.9 61.9 L16 80.3 L77.1 80.3 L100 61.9 Z" fill="#0f6e56" fill-opacity="0.14" stroke="#0f172a" stroke-width="1.4" stroke-linejoin="round"/>
<path d="M49.3 89.1 L65.3 48.7" fill="none" stroke="#b45309" stroke-width="2.6" stroke-linecap="round"/>
<circle cx="55.7" cy="72.9" r="4.5" fill="#0f172a"/>
<text x="44.7" y="80.9" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">I</text>
<text x="89.1" y="86.3" text-anchor="middle" font-size="13" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">P</text>
<text x="77.3" y="50.7" text-anchor="middle" font-size="13" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">D</text>
<text x="58" y="150" text-anchor="middle" font-size="12" font-weight="600" fill="#475569" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">sécante</text>
<path d="M150.9 61.9 L128 80.3 L189.1 80.3 L212 61.9 Z" fill="#0f6e56" fill-opacity="0.14" stroke="#0f172a" stroke-width="1.4" stroke-linejoin="round"/>
<path d="M137.2 51.6 L198.3 51.6" fill="none" stroke="#b45309" stroke-width="2.6" stroke-linecap="round"/>
<text x="201.1" y="86.3" text-anchor="middle" font-size="13" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">P</text>
<text x="210.3" y="49.6" text-anchor="middle" font-size="13" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">D</text>
<text x="170" y="150" text-anchor="middle" font-size="12" font-weight="600" fill="#475569" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">strictement parallèle</text>
<path d="M262.9 61.9 L240 80.3 L301.1 80.3 L324 61.9 Z" fill="#0f6e56" fill-opacity="0.14" stroke="#0f172a" stroke-width="1.4" stroke-linejoin="round"/>
<path d="M259.9 69.3 L299.6 76.6" fill="none" stroke="#b45309" stroke-width="2.6" stroke-linecap="round"/>
<text x="313.1" y="86.3" text-anchor="middle" font-size="13" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">P</text>
<text x="247.9" y="73.3" text-anchor="middle" font-size="13" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">D</text>
<text x="282" y="150" text-anchor="middle" font-size="12" font-weight="600" fill="#475569" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">incluse</text>
</svg>
:::

Sur la figure, trois cas : un point commun I (sécante), aucun point commun (strictement parallèle), ou tous les points de D (incluse). Le calcul qui suit les distingue.

::: exemple Où le rayon rencontre-t-il la vitre ?

1. Le vecteur directeur de D est u⃗(1, 1, 1). Test : 2×1 − 1 + 3×1 = 4 ≠ 0, donc u⃗ n'est pas un vecteur de P : D n'est pas parallèle à P, elle est sécante.
2. On reporte les expressions de x, y, z dans l'équation de P : 2(1 + λ) − (3 + λ) + 3λ − 7 = 4λ − 8 = 0, donc λ = 2.
3. On reporte λ = 2 dans D : I(3, 5, 2). Contrôle : 2×3 − 5 + 3×2 − 7 = 0 ✓.

:::

::: exemple Deux droites de même direction
Soit D′ : x = λ ; y = 5λ ; z = 3 + λ et D″ : x = 2 + λ ; y = 5λ ; z = 1 + λ, toutes deux de vecteur directeur (1, 5, 1).

1. Test : 2×1 − 5 + 3×1 = 0, donc (1, 5, 1) est un vecteur de P : D′ et D″ sont parallèles à P.
2. Pour D′, l'équation de P devient 2λ − 5λ + 3(3 + λ) − 7 = 2, soit 0×λ + 2 = 0 : aucune valeur de λ ne convient, D′ est strictement parallèle à P.
3. Pour D″, elle devient 2(2 + λ) − 5λ + 3(1 + λ) − 7 = 0 pour tout λ : tous les points de D″ sont dans P, D″ est incluse dans P.

:::

::: piege
**Erreur : conclure « aucun point commun » dès que le vecteur directeur est un vecteur du plan.** L'erreur tente parce que « parallèle » évoque deux objets qui ne se touchent pas. Mais D′ et D″ ont la même direction et sont toutes deux parallèles à P : l'une ne rencontre pas P, l'autre est contenue dans P. Il faut encore regarder l'équation en λ : 0×λ + 2 = 0 est impossible, 0×λ + 0 = 0 est toujours vraie.
:::

::: propriete
Soit D une droite de vecteur directeur u⃗ et P un plan.
- D est parallèle à P si et seulement si u⃗ est un vecteur de P ; sinon, D est sécante à P, en un seul point.
- En reportant la représentation paramétrique de D dans l'équation de P, on obtient une équation du type kλ = h. Si k ≠ 0, il y a une seule solution : un point d'intersection. Si k = 0 et h ≠ 0, aucune solution : D est strictement parallèle à P. Si k = 0 et h = 0, tout λ convient : D est incluse dans P.

Cas limite : si D est donnée par deux équations, D ∩ P est l'intersection de trois plans, étudiée à la notion suivante.
:::

::: verifie À toi : droite et plan
Soit P : x − y + 2z − 5 = 0 et D : x = 3 + λ ; y = −1 + 2λ ; z = 2 − λ. Quelle est leur position relative ?

---

Le vecteur directeur (1, 2, −1) donne 1 − 2 − 2 = −3 ≠ 0 : D est sécante à P. En reportant, (3 + λ) − (−1 + 2λ) + 2(2 − λ) − 5 = 3 − 3λ = 0, donc λ = 1, et le point d'intersection est (4, 1, 1). Contrôle : 4 − 1 + 2 − 5 = 0 ✓.
:::

::: retenir
Une droite est parallèle à un plan si son vecteur directeur est un vecteur du plan ; en reportant la droite dans l'équation du plan, kλ = h donne un point (k ≠ 0), aucun point (k = 0, h ≠ 0) ou tous les points (k = 0, h = 0).
:::

## 🔺 Trois plans et la section d'un tétraèdre

On coupe un tétraèdre ABCD par une lame plane qui passe par P ∈ [AB], Q ∈ [AC] et R ∈ [CD]. Quelle forme la coupe a-t-elle, et où la lame sort-elle de l'arête [BD] ? Chaque réponse est l'intersection de trois plans : le plan de la lame et les deux faces qui se rencontrent le long de l'arête.

On rapporte l'espace au repère (B, BC⃗, BD⃗, BA⃗), non orthonormé, ce qui ne gêne pas : les équations de plans et de droites n'utilisent ni distance ni angle. On a B(0, 0, 0), C(1, 0, 0), D(0, 1, 0), A(0, 0, 1), puis P(0, 0, 2/3) sur [BA], Q(1/2, 0, 1/2) sur [AC] et R(3/4, 1/4, 0) sur [CD].

::: figure La section du tétraèdre ABCD par le plan (PQR) est le quadrilatère PQRS ; M est le point où (PQ) coupe (BC), et S le point où (MR) coupe (BD)
<svg viewBox="0 0 340 250">
<title>Tétraèdre ABCD, points P, Q, R sur les arêtes, point M sur la droite BC et point S sur l'arête BD</title>
<path d="M80 71.7 L125 110 L167.5 172.5 L112 141 Z" fill="#0f6e56" fill-opacity="0.18"/>
<path d="M40 165 L220 105" fill="none" stroke="#94a3b8" stroke-width="1.8" stroke-dasharray="6 5" stroke-linecap="round"/>
<path d="M100 25 L40 165" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round"/>
<path d="M40 165 L150 195" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round"/>
<path d="M150 195 L100 25" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round"/>
<path d="M100 25 L220 105" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round"/>
<path d="M150 195 L220 105" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round"/>
<path d="M150 195 L260 225" fill="none" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="2 4" stroke-linecap="round"/>
<path d="M125 110 L260 225" fill="none" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="2 4" stroke-linecap="round"/>
<path d="M80 71.7 L125 110" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linecap="round"/>
<path d="M125 110 L167.5 172.5" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linecap="round"/>
<path d="M167.5 172.5 L112 141" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-dasharray="6 5" stroke-linecap="round"/>
<path d="M112 141 L80 71.7" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-dasharray="6 5" stroke-linecap="round"/>
<path d="M167.5 172.5 L260 225" fill="none" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="2 4" stroke-linecap="round"/>
<circle cx="100" cy="25" r="4" fill="#0f172a"/>
<circle cx="40" cy="165" r="4" fill="#0f172a"/>
<circle cx="150" cy="195" r="4" fill="#0f172a"/>
<circle cx="220" cy="105" r="4" fill="#0f172a"/>
<circle cx="80" cy="71.7" r="4.5" fill="#0f6e56"/>
<circle cx="125" cy="110" r="4.5" fill="#0f6e56"/>
<circle cx="167.5" cy="172.5" r="4.5" fill="#0f6e56"/>
<circle cx="112" cy="141" r="4.5" fill="#0f6e56"/>
<circle cx="260" cy="225" r="4.5" fill="#b45309"/>
<text x="100" y="15" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">A</text>
<text x="28" y="171" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">B</text>
<text x="150" y="213" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">C</text>
<text x="234" y="105" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">D</text>
<text x="68" y="71.7" text-anchor="middle" font-size="13" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">P</text>
<text x="121" y="98" text-anchor="middle" font-size="13" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">Q</text>
<text x="179.5" y="186.5" text-anchor="middle" font-size="13" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">R</text>
<text x="108" y="157" text-anchor="middle" font-size="13" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">S</text>
<text x="260" y="243" text-anchor="middle" font-size="13" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">M</text>
</svg>
:::

Sur la figure, la coupe est le quadrilatère PQRS. Les pointillés gris sont des prolongements : (PQ) coupe (BC) en M, puis (MR) coupe (BD) en S.

::: exemple La coupe du tétraèdre par le plan (PQR)

1. Équation de (PQR) : PQ⃗(1/2, 0, −1/6) et PR⃗(3/4, 1/4, −2/3) ne sont pas colinéaires ((1/2)×(1/4) − (3/4)×0 = 1/8 ≠ 0). On les remplace par des multiples entiers de même direction, u⃗(3, 0, −1) et v⃗(9, 3, −8) ; avec PM⃗(x, y, z − 2/3), le déterminant de PM⃗, u⃗, v⃗ vaut 3x + 15y + 9(z − 2/3) = 3x + 15y + 9z − 6, d'où x + 5y + 3z − 2 = 0. Contrôle : P donne 2 − 2 = 0, Q donne 1/2 + 3/2 − 2 = 0 et R donne 3/4 + 5/4 − 2 = 0 ✓.
2. M : le plan (PQR) coupe le plan (ABC) suivant (PQ), donc le point de (BC) qui est dans (PQR) est sur (PQ), c'est M. La droite (BC) est l'axe des abscisses, y = 0 et z = 0 : l'équation donne x = 2, d'où M(2, 0, 0), hors du segment [BC] où x varie de 0 à 1.
3. S : la droite (BD) est l'axe des ordonnées, x = 0 et z = 0 : l'équation donne 5y = 2, d'où S(0, 2/5, 0). Comme 0 ≤ 2/5 ≤ 1, S est sur l'arête [BD].
4. M, R, S sont dans le plan (BCD), z = 0, et dans le plan (PQR) : ils sont alignés. Contrôle : MR⃗(−5/4, 1/4, 0) et MS⃗(−2, 2/5, 0) donnent (−5/4)×(2/5) − (−2)×(1/4) = −1/2 + 1/2 = 0 ✓. La coupe est le quadrilatère PQRS, avec un sommet sur chacune des arêtes [AB], [AC], [CD], [BD].

:::

::: exemple Trois plans, trois issues
Soit P₁ : x + y + z − 6 = 0, P₂ : 2x − y + z − 3 = 0 et P₃ : x − y + 2z − 5 = 0.

1. On élimine y : P₁ + P₂ donne 3x + 2z − 9 = 0 et P₁ + P₃ donne 2x + 3z − 11 = 0.
2. On résout ce système de deux équations : on multiplie la première par 3 et la seconde par 2, ce qui donne 9x + 6z = 27 et 4x + 6z = 22 ; en soustrayant, 5x = 5, donc x = 1 et z = 3. La première équation de départ donne alors y = 6 − 1 − 3 = 2.
3. Contrôle : P₂ donne 2 − 2 + 3 − 3 = 0 et P₃ donne 1 − 2 + 6 − 5 = 0 ✓. Les trois plans ont un seul point commun, (1, 2, 3).
4. Si P₃ est remplacé par 3x + 2z − 9 = 0 (somme de P₁ et P₂), tous les points de P₁ ∩ P₂ le vérifient : les trois plans ont une droite commune. S'il est remplacé par 3x + 2z − 10 = 0, il contredit 3x + 2z − 9 = 0 : aucun point commun.

:::

::: piege
**Erreur : croire que trois plans sécants deux à deux ont toujours un point commun.** L'erreur tente parce que deux plans sécants font une droite, et qu'une droite rencontre en général un troisième plan. Mais P₁, P₂ et 3x + 2z − 10 = 0 ont des coefficients (1, 1, 1), (2, −1, 1) et (3, 0, 2) deux à deux non proportionnels, et pourtant aucun point commun : la droite P₁ ∩ P₂ est parallèle au troisième plan sans y être.
:::

::: propriete
Pour trois plans, on élimine une inconnue entre deux couples d'équations, puis on résout le système de deux équations obtenu : une solution unique donne un seul point commun, si deux des plans sont sécants, une équation conséquence des autres donne une droite commune, une contradiction donne l'ensemble vide.
Pour la section d'un tétraèdre ABCD par un plan : on se place dans le repère (B, BC⃗, BD⃗, BA⃗), on écrit l'équation du plan, puis on l'intersecte avec chaque arête (une droite) ; le point est sur l'arête si son paramètre est compris entre 0 et 1.
Cas limite : un plan parallèle à une arête ne la coupe pas, ou la contient.
:::

::: verifie À toi : l'intersection de trois plans
Déterminer les points communs aux plans x + y − z − 1 = 0, x − y + z − 3 = 0 et 2x + y + z − 7 = 0.

---

En additionnant les deux premières équations, y et z disparaissent : 2x − 4 = 0, donc x = 2. La première devient y − z = −1 et la troisième y + z = 3, donc y = 1 et z = 2. Contrôle avec la première : 2 + 1 − 2 − 1 = 0 ✓ ; avec la deuxième : 2 − 1 + 2 − 3 = 0 ✓ ; avec la troisième : 4 + 1 + 2 − 7 = 0 ✓. Les trois plans n'ont que le point (2, 1, 2) en commun.
:::

::: retenir
Trois plans se rencontrent en un point, suivant une droite ou pas du tout, et deux à deux sécants ne garantit rien ; la section d'un tétraèdre s'obtient en coupant le plan avec chaque arête dans le repère (B, BC⃗, BD⃗, BA⃗).
:::

> 🏆 Les huit notions sont acquises : tu testes la colinéarité et la coplanarité par les déterminants, tu décris droites et plans par des paramètres ou des équations, et tu tranches les positions relatives de deux droites, de deux plans, d'une droite et d'un plan, puis de trois plans. Prochaine étape : le produit scalaire, le produit vectoriel et le produit mixte.
