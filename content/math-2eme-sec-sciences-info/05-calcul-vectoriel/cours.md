# ⚔️ Calcul vectoriel — quand la géométrie devient un calcul

> 💡 «Une flèche, deux nombres. À partir de là, un alignement, un parallélisme ou un angle droit ne se discutent plus : ils se calculent.»

Tu sais déjà reconnaître deux vecteurs égaux et construire une somme à la règle. Cette quête change d'arme : on donne aux vecteurs une **algèbre** (une addition, une multiplication par un réel), puis on les traduit en **couples de nombres**. Dès lors, « ces trois points sont alignés », « ces deux droites sont parallèles », « ces deux droites sont perpendiculaires » deviennent trois petits calculs qu'on ne peut plus rater. C'est l'outil qui portera toute la géométrie des années suivantes.

## 🧭 Rappel : le vecteur, un déplacement qu'on peut recopier

Un vecteur AB⃗ est déterminé par trois données : une **direction** (celle de la droite (AB)), un **sens** (de A vers B) et une **longueur** (la distance AB). Deux vecteurs sont **égaux** lorsqu'ils ont ces trois caractères en commun ; on peut donc recopier une flèche ailleurs dans le plan sans changer le vecteur.

> **Retenir.** AB⃗ = CD⃗ **si et seulement si** le quadrilatère ABDC est un parallélogramme, c'est-à-dire si et seulement si [AD] et [BC] ont le même milieu. En particulier AA⃗ = BB⃗ : c'est le **vecteur nul**, noté 0⃗, le seul vecteur sans direction ni sens.

Attention à l'ordre des lettres : le parallélogramme associé à AB⃗ = CD⃗ se lit **ABDC**, pas ABCD. On retient plutôt le critère des milieux, qui ne se trompe jamais.

## ➕ Additionner : la somme, l'opposé et la relation de Chasles

> **Définition (somme).** Soient u⃗ et v⃗ deux vecteurs, A un point du plan, B le point tel que u⃗ = AB⃗ et C le point tel que v⃗ = AC⃗. Soit D le point tel que [BC] et [AD] aient le même milieu. On appelle **vecteur somme** de u⃗ et v⃗ le vecteur w⃗ tel que w⃗ = AD⃗. Le vecteur w⃗ est noté u⃗ + v⃗.

::: figure Construction de la somme : u⃗ = AB⃗ et v⃗ = AC⃗ portés par la même origine A ; le point D est choisi pour que [AD] et [BC] aient le même milieu I, et alors u⃗ + v⃗ = AD⃗
<svg viewBox="0 0 340 230">
<path d="M170 150 L220 30 M110 70 L220 30 M170 150 L110 70" fill="none" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="6 4"/>
<path d="M60 190 L170 150" fill="none" stroke="#0f6e56" stroke-width="2.5"/>
<polygon points="170,150 159.5,159.1 156.1,149.7" fill="#0f6e56"/>
<path d="M60 190 L110 70" fill="none" stroke="#0f6e56" stroke-width="2.5"/>
<polygon points="110,70 109.6,83.9 100.4,80.1" fill="#0f6e56"/>
<path d="M60 190 L220 30" fill="none" stroke="#0f172a" stroke-width="2.8"/>
<polygon points="220,30 214,43.8 206.2,36" fill="#0f172a"/>
<g fill="#0f172a"><circle cx="60" cy="190" r="4"/><circle cx="170" cy="150" r="4"/><circle cx="110" cy="70" r="4"/><circle cx="220" cy="30" r="4"/><circle cx="140" cy="110" r="4.5"/></g>
<g font-size="15" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">
<text x="50" y="204" text-anchor="middle">A</text>
<text x="182" y="162" text-anchor="middle">B</text>
<text x="100" y="60" text-anchor="middle">C</text>
<text x="234" y="28" text-anchor="middle">D</text>
<text x="132" y="126" text-anchor="middle">I</text>
</g>
</svg>
:::

Cette construction donne aussitôt les propriétés de l'addition, valables pour tous vecteurs u⃗, v⃗, w⃗ :

$$ u⃗ + v⃗ = v⃗ + u⃗ ; u⃗ + (v⃗ + w⃗) = (u⃗ + v⃗) + w⃗ ; u⃗ + 0⃗ = 0⃗ + u⃗ = u⃗ $$

> **Définition (opposé).** Pour tout vecteur u⃗, l'unique vecteur v⃗ tel que u⃗ + v⃗ = 0⃗ s'appelle l'**opposé** de u⃗ ; il est noté −u⃗. Ainsi u⃗ + (−u⃗) = (−u⃗) + u⃗ = 0⃗. On note u⃗ − v⃗ le vecteur u⃗ + (−v⃗).

L'opposé, c'est le même déplacement parcouru à l'envers : **BA⃗ = −AB⃗**. Et la construction précédente, écrite avec des points enchaînés, donne le théorème le plus utilisé du chapitre :

$$ Relation de Chasles : AB⃗ + BC⃗ = AC⃗, quels que soient les points A, B et C $$

Le secret est toujours le même : le point d'**arrivée** du premier vecteur est le point de **départ** du second. En particulier AB⃗ + BA⃗ = AA⃗ = 0⃗.

_Exemple détaillé_ : simplifions AB⃗ + CD⃗ + BC⃗. On remet les points bout à bout : AB⃗ + BC⃗ + CD⃗, et Chasles agit deux fois — AB⃗ + BC⃗ = AC⃗, puis AC⃗ + CD⃗ = **AD⃗**.

> 🗡️ Retiens la règle « même origine » : **AB⃗ − AC⃗ = CB⃗** (on va de la seconde extrémité vers la première). C'est la transformation qui débloque presque tous les exercices d'écriture vectorielle.

## ✖️ Multiplier un vecteur par un réel

> **Définition (produit par un réel).** Soient u⃗ un vecteur non nul, A et B les points tels que u⃗ = AB⃗, α un réel et M le point de la droite (AB) d'abscisse α dans le repère (A, B). On appelle **vecteur produit** de u⃗ par α le vecteur v⃗ tel que v⃗ = AM⃗ ; il est noté α.u⃗ ou αu⃗. Le produit du vecteur nul par α est le vecteur nul : α.0⃗ = 0⃗.

::: figure Sur la droite (AB) munie du repère (A, B) : AB⃗ = u⃗ (abscisse 1), AM⃗ = 2u⃗ (abscisse 2) et AN⃗ = −(1/2)u⃗ (abscisse −1/2) — le réel étire ou raccourcit la flèche, et son signe décide du sens
<svg viewBox="0 0 340 150">
<path d="M25 100 L315 100" fill="none" stroke="#0f172a" stroke-width="2"/>
<polygon points="322,100 310,105 310,95" fill="#0f172a"/>
<g stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="4 4">
<path d="M75 100 L75 30 M110 100 L110 30 M180 100 L180 70 M250 100 L250 50"/>
</g>
<path d="M110 75 L180 75" fill="none" stroke="#0f6e56" stroke-width="2.5"/>
<polygon points="180,75 170,79.5 170,70.5" fill="#0f6e56"/>
<path d="M110 55 L250 55" fill="none" stroke="#0f6e56" stroke-width="2.5"/>
<polygon points="250,55 240,59.5 240,50.5" fill="#0f6e56"/>
<path d="M110 35 L75 35" fill="none" stroke="#b91c1c" stroke-width="2.5"/>
<polygon points="75,35 85,39.5 85,30.5" fill="#b91c1c"/>
<g fill="#0f172a"><circle cx="110" cy="100" r="4"/><circle cx="180" cy="100" r="4"/><circle cx="250" cy="100" r="4"/><circle cx="75" cy="100" r="4"/></g>
<g font-size="15" font-weight="700" fill="#0f172a" text-anchor="middle" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">
<text x="75" y="122">N</text><text x="110" y="122">A</text><text x="180" y="122">B</text><text x="250" y="122">M</text>
<text x="75" y="141">−1/2</text><text x="110" y="141">0</text><text x="180" y="141">1</text><text x="250" y="141">2</text>
</g>
</svg>
:::

Toutes les règles de calcul de ℝ se transportent, pour tous réels α, β et tous vecteurs u⃗, v⃗ :

$$ 1.u⃗ = u⃗ ; (−1).u⃗ = −u⃗ ; α(βu⃗) = (αβ)u⃗ ; αu⃗ + βu⃗ = (α + β)u⃗ ; α(u⃗ + v⃗) = αu⃗ + αv⃗ $$

> **Retenir.** αu⃗ = 0⃗ **si et seulement si** α = 0 **ou** u⃗ = 0⃗. C'est la règle du produit nul, transposée aux vecteurs : elle autorise à « simplifier par α » dès que α n'est pas nul.

_Exemple détaillé_ : simplifions 4u⃗ + 9u⃗ − 6u⃗. On additionne les coefficients : 4 + 9 − 6 = 7, donc le résultat est **7u⃗**. De même 5(u⃗ + 2v⃗) − 3u⃗ = 5u⃗ + 10v⃗ − 3u⃗ = **2u⃗ + 10v⃗**.

> ⚠️ Un vecteur ne se multiplie **pas** par un vecteur dans ce chapitre : les écritures u⃗v⃗ ou u⃗² n'ont aucun sens ici. Seuls un **réel** et un **vecteur** se multiplient.

## 🧲 Vecteurs colinéaires : alignement et parallélisme

> **Définition.** Deux vecteurs sont dits **colinéaires** lorsque l'un est le produit de l'autre par un réel. Le vecteur nul est colinéaire à tout vecteur.

Deux vecteurs colinéaires portent la même direction. Le signe du coefficient dit le reste : si u⃗ = αv⃗ avec α > 0, les deux vecteurs ont le **même sens** ; avec α < 0, ils sont de **sens contraires**.

> **Retenir (les deux traductions à connaître par cœur).**
>
> - A, B et C (avec A ≠ B) sont **alignés** ⟺ AB⃗ et AC⃗ sont colinéaires ⟺ il existe un réel x tel que AC⃗ = xAB⃗.
> - Les droites (AB) et (CD) sont **parallèles** ⟺ AB⃗ et CD⃗ sont colinéaires.

_Exemple détaillé_ : posons p⃗ = 3(u⃗ − v⃗) + 2v⃗ et q⃗ = 2(v⃗ − 3u⃗). On développe : p⃗ = 3u⃗ − 3v⃗ + 2v⃗ = **3u⃗ − v⃗**, puis q⃗ = 2v⃗ − 6u⃗ = **−2(3u⃗ − v⃗)**. Donc q⃗ = −2p⃗ : les vecteurs p⃗ et q⃗ sont colinéaires, et p⃗ = −(1/2)q⃗. La méthode ne change jamais : on développe les deux écritures sur les mêmes vecteurs, puis on factorise l'une pour faire apparaître l'autre.

## 🧮 Base et composantes : le vecteur devient un couple de nombres

> **Définition (base, composantes).** On appelle **base** de l'ensemble des vecteurs du plan tout couple (i⃗ ; j⃗) de vecteurs **non colinéaires**. Tout vecteur u⃗ du plan s'écrit alors de **façon unique** sous la forme u⃗ = xi⃗ + yj⃗ ; le couple (x, y) est appelé couple de **composantes** du vecteur u⃗ dans la base (i⃗ ; j⃗). On note u⃗(x ; y).

L'unicité est ce qui rend le calcul possible : deux vecteurs sont égaux **si et seulement si** ils ont les mêmes composantes. Le vecteur nul a pour composantes (0 ; 0), i⃗ a pour composantes (1 ; 0) et j⃗ a pour composantes (0 ; 1).

> **Retenir (calcul sur les composantes).** Si u⃗(x ; y) et v⃗(x' ; y') dans une même base, alors u⃗ + v⃗ a pour composantes (x + x' ; y + y') et αu⃗ a pour composantes (αx ; αy).

_Exemple détaillé_ : pour u⃗(4 ; −3), le vecteur 2u⃗ a pour composantes (2 × 4 ; 2 × (−3)) = **(8 ; −6)**. On multiplie **chaque** composante par le réel — jamais une seule, et jamais en l'ajoutant.

Décomposer un vecteur dans une base, c'est justement retrouver ce couple : on écrit u⃗ = xi⃗ + yj⃗ et on **identifie** les coefficients de i⃗ et de j⃗ des deux côtés, exactement comme on identifie les coefficients de deux polynômes égaux.

> **Vocabulaire et notation (déterminant).** Le réel xy' − x'y est appelé le **déterminant** des vecteurs u⃗(x ; y) et v⃗(x' ; y') dans la base (i⃗ ; j⃗).

> **Retenir (condition analytique de colinéarité).** u⃗(x ; y) et v⃗(x' ; y') sont **colinéaires si et seulement si** leur déterminant est nul : xy' − x'y = 0.

_Exemple détaillé_ : u⃗(−3 ; 6) et v⃗(1 ; −2). Leur déterminant vaut (−3) × (−2) − 1 × 6 = 6 − 6 = **0** : ils sont colinéaires (on voit d'ailleurs que u⃗ = −3v⃗). En revanche u⃗(5 ; 2) et v⃗(3 ; −1) ont pour déterminant 5 × (−1) − 3 × 2 = −5 − 6 = **−11**, non nul : ils ne sont pas colinéaires, donc ils forment une base.

> ⚠️ Dans le déterminant, on multiplie **en croix** : xy' − x'y. Écrire xx' − yy' ou xy' + x'y donne un nombre qui ne veut rien dire. Un moyen de contrôle : le déterminant d'un vecteur avec lui-même doit toujours donner 0.

## 📍 Repère cartésien : les coordonnées d'un point

> **Définition (repère cartésien, coordonnées).** Soient O un point du plan et (i⃗ ; j⃗) une base. Le triplet (O, i⃗, j⃗) est appelé **repère cartésien** du plan. Pour tout point M, il existe un unique couple (x, y) de réels tel que OM⃗ = xi⃗ + yj⃗ : x est l'**abscisse** et y l'**ordonnée** du point M. On note M(x, y).

Le point O est l'**origine** du repère, la droite (O, i⃗) l'**axe des abscisses** et la droite (O, j⃗) l'**axe des ordonnées**.

> **Retenir (la formule de conversion).** Si A(x_A ; y_A) et B(x_B ; y_B), alors le vecteur AB⃗ a pour composantes **(x_B − x_A ; y_B − y_A)** : les coordonnées de l'arrivée moins celles du départ.

::: figure Dans le repère (O, i⃗, j⃗), les composantes de AB⃗ se lisent comme deux déplacements : 3 vers la droite et 2 vers le haut, soit AB⃗(3 ; 2) — exactement 4 − 1 et 3 − 1
<svg viewBox="0 0 340 250">
<g stroke="#e2e8f0" stroke-width="1">
<path d="M40 20 L40 230 M100 20 L100 230 M130 20 L130 230 M160 20 L160 230 M190 20 L190 230 M220 20 L220 230 M250 20 L250 230 M280 20 L280 230 M310 20 L310 230"/>
<path d="M25 230 L320 230 M25 170 L320 170 M25 140 L320 140 M25 110 L320 110 M25 80 L320 80 M25 50 L320 50"/>
</g>
<path d="M25 200 L318 200" fill="none" stroke="#0f172a" stroke-width="2"/>
<polygon points="325,200 313,205 313,195" fill="#0f172a"/>
<path d="M70 238 L70 22" fill="none" stroke="#0f172a" stroke-width="2"/>
<polygon points="70,15 65,27 75,27" fill="#0f172a"/>
<path d="M100 170 L190 170 L190 110" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-dasharray="6 4"/>
<path d="M100 170 L190 110" fill="none" stroke="#0f6e56" stroke-width="2.8"/>
<polygon points="190,110 182,121.4 176.4,113" fill="#0f6e56"/>
<path d="M70 200 L98 200" fill="none" stroke="#b91c1c" stroke-width="3"/>
<polygon points="102,200 92,204 92,196" fill="#b91c1c"/>
<path d="M70 200 L70 172" fill="none" stroke="#b91c1c" stroke-width="3"/>
<polygon points="70,168 66,178 74,178" fill="#b91c1c"/>
<g fill="#0f172a"><circle cx="100" cy="170" r="4"/><circle cx="190" cy="110" r="4"/><circle cx="70" cy="200" r="4"/></g>
<g font-size="15" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">
<text x="60" y="216" text-anchor="middle" fill="#0f172a">O</text>
<text x="92" y="186" text-anchor="middle" fill="#0f172a">A</text>
<text x="202" y="104" text-anchor="middle" fill="#0f172a">B</text>
<text x="145" y="188" text-anchor="middle" fill="#94a3b8">3</text>
<text x="204" y="146" text-anchor="middle" fill="#94a3b8">2</text>
<text x="92" y="216" text-anchor="middle" fill="#b91c1c">i</text>
<text x="56" y="180" text-anchor="middle" fill="#b91c1c">j</text>
</g>
</svg>
:::

_Exemple détaillé (le quatrième sommet)_ : soient A(1 ; −2), B(5 ; 1) et C(2 ; 4). Cherchons D pour que ABCD soit un parallélogramme. Le critère est AB⃗ = DC⃗. Or AB⃗(5 − 1 ; 1 − (−2)), c'est-à-dire AB⃗(4 ; 3). En notant D(x ; y), on a DC⃗(2 − x ; 4 − y), d'où 2 − x = 4 et 4 − y = 3 : x = −2 et y = 1. Donc **D(−2 ; 1)**.

> ⚠️ Dans ABCD, les côtés [AB] et [DC] sont **parallèles et de même sens** : le bon critère est AB⃗ = DC⃗, jamais AB⃗ = CD⃗ (qui donnerait un quadrilatère croisé). Une erreur d'ordre de lettres, et le point tombe ailleurs.

## 📏 Norme, distance et orthogonalité

> **Définition (norme).** Soient A et B les points tels que u⃗ = AB⃗. On appelle **norme** du vecteur u⃗ le réel noté ‖u⃗‖ et qui est égal à la longueur AB. Lorsque ‖u⃗‖ = 1, on dit que u⃗ est un vecteur **unitaire** (ou normé).

> **Retenir.** ‖u⃗‖ = 0 ⟺ u⃗ = 0⃗ ; ‖αu⃗‖ = |α| × ‖u⃗‖ ; ‖u⃗ + v⃗‖ ≤ ‖u⃗‖ + ‖v⃗‖ (**inégalité triangulaire**).

Le facteur est bien la **valeur absolue** de α : une longueur ne peut pas être négative. Si ‖u⃗‖ = 10, alors ‖−(3/5)u⃗‖ = (3/5) × 10 = **6**.

> **Définition (vecteurs orthogonaux).** Soient A, B et C les points tels que u⃗ = AB⃗ et v⃗ = AC⃗. On dit que u⃗ et v⃗ sont **orthogonaux** si les droites (AB) et (AC) sont perpendiculaires. Par convention, le vecteur nul est orthogonal à tout vecteur du plan. On note u⃗ ⊥ v⃗.

> **Définition (base et repère orthonormés).** Une base (i⃗ ; j⃗) est dite **orthonormée** lorsque i⃗ ⊥ j⃗ et ‖i⃗‖ = ‖j⃗‖ = 1. Le repère (O, i⃗, j⃗) est alors dit **orthonormé**.

C'est seulement dans une base orthonormée que les longueurs se calculent, grâce au théorème de Pythagore.

::: figure Dans une base orthonormée, le vecteur u⃗(3 ; 2) est l'hypoténuse d'un triangle rectangle de côtés 3 et 2 : sa norme vaut √(3² + 2²) = √13
<svg viewBox="0 0 300 240">
<g stroke="#e2e8f0" stroke-width="1">
<path d="M100 20 L100 230 M140 20 L140 230 M180 20 L180 230 M220 20 L220 230 M260 20 L260 230"/>
<path d="M25 160 L285 160 M25 120 L285 120 M25 80 L285 80 M25 40 L285 40"/>
</g>
<path d="M25 200 L278 200" fill="none" stroke="#0f172a" stroke-width="2"/>
<polygon points="285,200 273,205 273,195" fill="#0f172a"/>
<path d="M60 235 L60 27" fill="none" stroke="#0f172a" stroke-width="2"/>
<polygon points="60,20 55,32 65,32" fill="#0f172a"/>
<path d="M180 200 L180 120" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-dasharray="6 4"/>
<path d="M172 200 L172 192 L180 192" fill="none" stroke="#0f172a" stroke-width="1.6"/>
<path d="M60 200 L180 120" fill="none" stroke="#0f6e56" stroke-width="2.8"/>
<polygon points="180,120 172,131.4 166.4,123" fill="#0f6e56"/>
<g fill="#0f172a"><circle cx="60" cy="200" r="4"/><circle cx="180" cy="120" r="4"/><circle cx="180" cy="200" r="4"/></g>
<g font-size="15" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">
<text x="50" y="216" text-anchor="middle" fill="#0f172a">O</text>
<text x="192" y="114" text-anchor="middle" fill="#0f172a">M</text>
<text x="190" y="216" text-anchor="middle" fill="#0f172a">H</text>
<text x="120" y="218" text-anchor="middle" fill="#94a3b8">3</text>
<text x="196" y="166" text-anchor="middle" fill="#94a3b8">2</text>
<text x="104" y="148" text-anchor="middle" fill="#0f6e56">√13</text>
</g>
</svg>
:::

> **Retenir (les trois formules analytiques, dans un repère orthonormé).**
>
> - Norme : si u⃗(x ; y), alors ‖u⃗‖ = √(x² + y²).
> - Distance : si A(x_A ; y_A) et B(x_B ; y_B), alors AB = √((x_B − x_A)² + (y_B − y_A)²).
> - Orthogonalité : u⃗(x ; y) ⊥ v⃗(x' ; y') **si et seulement si** xx' + yy' = 0.

_Exemple détaillé (normaliser un vecteur)_ : ‖u⃗(3 ; −4)‖ = √(9 + 16) = √25 = **5**, donc u⃗ n'est pas unitaire ; en revanche (1/5)u⃗ l'est, puisque ‖(1/5)u⃗‖ = (1/5) × 5 = 1.

_Exemple détaillé_ : dans un repère orthonormé, A(2 ; −1) et B(−3 ; 11). Le vecteur AB⃗ a pour composantes (−3 − 2 ; 11 − (−1)), soit AB⃗(−5 ; 12). D'où AB = √((−5)² + 12²) = √(25 + 144) = √169 = **13**.

_Exemple détaillé_ : les vecteurs u⃗(3 ; 5) et v⃗(10 ; −6) sont-ils orthogonaux dans une base orthonormée ? On calcule xx' + yy' = 3 × 10 + 5 × (−6) = 30 − 30 = **0** : oui, ils sont orthogonaux. Leur déterminant, lui, vaut 3 × (−6) − 10 × 5 = −18 − 50 = −68, non nul : ils ne sont donc pas colinéaires, ce qui est rassurant.

> ⚠️ Ne confonds jamais les deux conditions : **xy' − x'y = 0** est la colinéarité (les deux droites sont parallèles) ; **xx' + yy' = 0** est l'orthogonalité (elles sont perpendiculaires). Le premier est une différence de produits croisés, le second une somme de produits en ligne.

## 🏛️ Vecteurs et configurations : milieu, centre de gravité, Thalès

Toute la géométrie du triangle se réécrit maintenant en une ligne de calcul.

> **Retenir (milieu).** I est le milieu de [AB] ⟺ IA⃗ + IB⃗ = 0⃗ ⟺ AI⃗ = (1/2)AB⃗. Et pour **tout** point M du plan : **MA⃗ + MB⃗ = 2MI⃗**.

La démonstration tient en deux lignes de Chasles : MA⃗ + MB⃗ = (MI⃗ + IA⃗) + (MI⃗ + IB⃗) = 2MI⃗ + (IA⃗ + IB⃗) = 2MI⃗ + 0⃗ = 2MI⃗.

> **Retenir (centre de gravité).** G est le **centre de gravité** du triangle ABC (le point de concours de ses médianes) ⟺ GA⃗ + GB⃗ + GC⃗ = 0⃗. Si I est le milieu de [BC], alors **AG⃗ = (2/3)AI⃗**. Et pour tout point M du plan : **MA⃗ + MB⃗ + MC⃗ = 3MG⃗**.

::: figure Les trois médianes du triangle ABC se coupent au centre de gravité G, situé aux deux tiers de chaque médiane à partir du sommet : AG⃗ = (2/3)AI⃗, où I est le milieu de [BC]
<svg viewBox="0 0 320 240">
<polygon points="150,40 60,200 260,200" fill="#0f6e56" opacity="0.10"/>
<polygon points="150,40 60,200 260,200" fill="none" stroke="#0f172a" stroke-width="2.2"/>
<path d="M60 200 L205 120 M260 200 L105 120" fill="none" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="6 4"/>
<path d="M150 40 L160 200" fill="none" stroke="#0f6e56" stroke-width="2.5"/>
<g fill="#0f172a"><circle cx="150" cy="40" r="4"/><circle cx="60" cy="200" r="4"/><circle cx="260" cy="200" r="4"/><circle cx="160" cy="200" r="4"/></g>
<circle cx="156.7" cy="146.7" r="5" fill="#0f6e56"/>
<g font-size="15" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">
<text x="150" y="28" text-anchor="middle" fill="#0f172a">A</text>
<text x="48" y="214" text-anchor="middle" fill="#0f172a">B</text>
<text x="272" y="214" text-anchor="middle" fill="#0f172a">C</text>
<text x="166" y="220" text-anchor="middle" fill="#0f172a">I</text>
<text x="172" y="142" text-anchor="middle" fill="#0f6e56">G</text>
</g>
</svg>
:::

Le calcul de MA⃗ + MB⃗ + MC⃗ suit le même schéma : MA⃗ + MB⃗ + MC⃗ = 3MG⃗ + (GA⃗ + GB⃗ + GC⃗) = 3MG⃗. C'est la relation qui transforme une condition sur trois points en une condition sur un seul.

_Exemple détaillé_ : cherchons l'ensemble des points M tels que ‖MA⃗ + MB⃗ + MC⃗‖ = 12, où G est le centre de gravité de ABC. On remplace : ‖3MG⃗‖ = 3 × MG, donc la condition s'écrit 3MG = 12, soit MG = 4. L'ensemble cherché est le **cercle de centre G et de rayon 4**.

> **Retenir (forme vectorielle du théorème de Thalès).** Soient ABC un triangle, M un point de (AB) et N un point de (AC) tels que (MN) et (BC) soient parallèles. Si AM⃗ = xAB⃗, alors **AN⃗ = xAC⃗ et MN⃗ = xBC⃗** : le même coefficient x commande les trois relations.

_Exemple détaillé_ : si M est le point de [AB] tel que AM⃗ = (3/4)AB⃗ et si la parallèle à (BC) passant par M coupe (AC) en N, alors AN⃗ = (3/4)AC⃗ et MN⃗ = **(3/4)BC⃗**. En particulier MN = (3/4) × BC.

> 🗡️ Le **théorème de la projection** est la version « trois parallèles » du même énoncé : si (AA'), (BB') et (CC') sont trois droites parallèles et si AB⃗ = xAC⃗, alors A'B'⃗ = xA'C'⃗. Le coefficient traverse la projection sans changer.

## 👑 Aller plus loin : l'orthocentre et la droite d'Euler

Un dernier résultat, spectaculaire, qui n'utilise que ce chapitre. Soit ABC un triangle, O le centre de son cercle circonscrit et G son centre de gravité. Définissons le point H par OH⃗ = OA⃗ + OB⃗ + OC⃗.

Comme MA⃗ + MB⃗ + MC⃗ = 3MG⃗ vaut pour tout point M, on a en particulier OA⃗ + OB⃗ + OC⃗ = 3OG⃗, donc **OH⃗ = 3OG⃗**. Les vecteurs OH⃗ et OG⃗ sont colinéaires : les points **O, G et H sont alignés**. La droite qui les porte s'appelle la **droite d'Euler** du triangle.

Et H n'est pas un point quelconque : c'est l'**orthocentre** de ABC, le point de concours des trois hauteurs. On le vérifie sur une hauteur : AH⃗ = AO⃗ + OH⃗ = AO⃗ + OA⃗ + OB⃗ + OC⃗ = OB⃗ + OC⃗. Or O est équidistant de B et de C, donc OB⃗ + OC⃗ = 2OI⃗ où I est le milieu de [BC] — et (OI) est la médiatrice de [BC], donc perpendiculaire à (BC). Ainsi (AH) ⊥ (BC) : la droite (AH) est bien la hauteur issue de A.

> 🏆 Quête franchie, héros : tu additionnes, tu multiplies, tu décomposes dans une base, tu lis une norme et tu tranches un alignement ou un angle droit par un simple calcul de composantes. Ces armes te suivront au chapitre suivant, où les points reçoivent des **poids**, puis dans toutes les transformations du plan.
