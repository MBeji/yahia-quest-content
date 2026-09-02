# 📜 Résumé : Calcul vectoriel

- **Égalité et vecteur nul** : AB⃗ = CD⃗ ⟺ ABDC est un parallélogramme ⟺ [AD] et [BC] ont le même milieu. Le vecteur nul est 0⃗ = AA⃗, et BA⃗ = −AB⃗.
- **Somme** : u⃗ = AB⃗ et v⃗ = AC⃗ ; si [AD] et [BC] ont le même milieu, alors u⃗ + v⃗ = AD⃗. L'addition est commutative, associative, a pour élément neutre 0⃗, et tout vecteur a un **opposé** (u⃗ + (−u⃗) = 0⃗ ; u⃗ − v⃗ signifie u⃗ + (−v⃗)).
- **Relation de Chasles** : AB⃗ + BC⃗ = AC⃗ (l'arrivée du premier est le départ du second) ; AB⃗ + BA⃗ = 0⃗ ; et la règle « même origine » **AB⃗ − AC⃗ = CB⃗**.
- **Produit par un réel** : 1.u⃗ = u⃗ ; (−1).u⃗ = −u⃗ ; α(βu⃗) = (αβ)u⃗ ; αu⃗ + βu⃗ = (α + β)u⃗ ; α(u⃗ + v⃗) = αu⃗ + αv⃗. Et αu⃗ = 0⃗ ⟺ α = 0 ou u⃗ = 0⃗. Exemple : 4u⃗ + 9u⃗ − 6u⃗ = 7u⃗.
- **Colinéarité** : u⃗ et v⃗ sont colinéaires lorsque l'un est le produit de l'autre par un réel (même sens si le coefficient est positif, sens contraires s'il est négatif). A, B, C alignés ⟺ AB⃗ et AC⃗ colinéaires ; (AB) ∥ (CD) ⟺ AB⃗ et CD⃗ colinéaires.
- **Base et composantes** : une **base** (i⃗ ; j⃗) est un couple de vecteurs **non colinéaires** ; tout vecteur s'écrit alors de façon unique u⃗ = xi⃗ + yj⃗, noté u⃗(x ; y). Composantes : u⃗ + v⃗(x + x' ; y + y') et αu⃗(αx ; αy). Ainsi 2u⃗ pour u⃗(4 ; −3) donne (8 ; −6).
- **Déterminant** : le réel xy' − x'y (produits **en croix**). Condition analytique de colinéarité : u⃗ et v⃗ sont colinéaires ⟺ xy' − x'y = 0. Exemple : u⃗(5 ; 2) et v⃗(3 ; −1) ont pour déterminant −5 − 6 = −11 ≠ 0, donc ils forment une base.
- **Repère cartésien** (O, i⃗, j⃗) : OM⃗ = xi⃗ + yj⃗ définit les coordonnées M(x, y) ; O est l'origine, (O, i⃗) l'axe des abscisses, (O, j⃗) l'axe des ordonnées. **AB⃗(x_B − x_A ; y_B − y_A)** (arrivée moins départ). ABCD est un parallélogramme ⟺ AB⃗ = DC⃗ — c'est ainsi qu'on trouve un quatrième sommet.
- **Norme** : ‖u⃗‖ = AB si u⃗ = AB⃗ ; u⃗ est **unitaire** lorsque ‖u⃗‖ = 1 (‖u⃗(3 ; −4)‖ = 5, donc (1/5)u⃗ est unitaire). ‖u⃗‖ = 0 ⟺ u⃗ = 0⃗ ; ‖αu⃗‖ = |α| × ‖u⃗‖ (valeur absolue) ; ‖u⃗ + v⃗‖ ≤ ‖u⃗‖ + ‖v⃗‖.
- **Orthogonalité** : u⃗ ⊥ v⃗ lorsque leurs droites support sont perpendiculaires (0⃗ est orthogonal à tout vecteur). Une base est **orthonormée** si i⃗ ⊥ j⃗ et ‖i⃗‖ = ‖j⃗‖ = 1.
- **Les trois formules du repère orthonormé** : ‖u⃗(x ; y)‖ = √(x² + y²) ; AB = √((x_B − x_A)² + (y_B − y_A)²) ; u⃗ ⊥ v⃗ ⟺ xx' + yy' = 0. Ne pas confondre avec la colinéarité xy' − x'y = 0.
- **Milieu** : I milieu de [AB] ⟺ IA⃗ + IB⃗ = 0⃗ ⟺ AI⃗ = (1/2)AB⃗ ; et pour tout point M, **MA⃗ + MB⃗ = 2MI⃗**.
- **Centre de gravité** : G centre de gravité de ABC ⟺ GA⃗ + GB⃗ + GC⃗ = 0⃗ ; **AG⃗ = (2/3)AI⃗** avec I milieu de [BC] ; et pour tout point M, **MA⃗ + MB⃗ + MC⃗ = 3MG⃗**.
- **Thalès vectoriel** : si M ∈ (AB), N ∈ (AC) et (MN) ∥ (BC), alors AM⃗ = xAB⃗ entraîne AN⃗ = xAC⃗ et MN⃗ = xBC⃗. Version « trois parallèles » (**théorème de la projection**) : AB⃗ = xAC⃗ entraîne A'B'⃗ = xA'C'⃗.
- **Enrichissement** : avec O centre du cercle circonscrit et H défini par OH⃗ = OA⃗ + OB⃗ + OC⃗, on a OH⃗ = 3OG⃗, donc O, G et H sont alignés sur la **droite d'Euler** — et H est l'**orthocentre** du triangle.
