# 📜 Résumé : Notion de polynômes

- **Fonction** : à tout x de E on associe au plus un réel y = f(x). L'**ensemble de définition** D regroupe les x pour lesquels f(x) existe (on écarte les dénominateurs nuls et les racines carrées de nombres négatifs). y est l'**image** de x, x est **un** antécédent de y (une image est unique, un antécédent ne l'est pas).
- **Fonction polynôme** : f(x) = aₙxⁿ + … + a₁x + a₀, les aᵢ sont les **coefficients**. Ni |x|, ni √x, ni (3x − 1)/(x + 2) ne sont des polynômes.
- **Degré** : écriture unique avec aₙ ≠ 0 ⇒ d°(P) = n. Le polynôme nul n'a pas de degré, un polynôme constant est de degré 0. Vocabulaire : terme constant a₀, terme du plus haut degré aₙxⁿ (coefficient **dominant** aₙ), monôme, binôme (degré 1), trinôme (degré 2). Le degré n'est pas le nombre de termes.
- **Égalité** : un polynôme est nul si et seulement si tous ses coefficients sont nuls ; deux polynômes sont égaux si et seulement s'ils ont même degré et mêmes coefficients de même rang (**méthode d'identification**). Coïncider en quelques valeurs ne suffit pas.
- **Opérations** : d°(fg) = d°(f) + d°(g) et le coefficient dominant du produit est le produit des coefficients dominants ; d°(αf) = d°(f) pour α ≠ 0. Le degré d'une **somme** peut baisser (3x² − x + 4 additionné à −3x² + 2x − 1 donne x + 3).
- **Racine** : α est racine de f lorsque f(α) = 0. Un polynôme de degré n (n ≥ 2) admet **au plus n** racines ⇒ un polynôme de degré ≤ n ayant plus de n racines distinctes est le **polynôme nul**.
- **Factorisation** : si α est racine de f (degré n ≥ 1), alors f(x) = (x − α)g(x) avec d°(g) = n − 1 ; avec k racines, f(x) = (x − α₁)…(x − α_k)g(x) et d°(g) = n − k. On cherche une **racine apparente** (1, −1, 2, −2…) puis on obtient g par identification. La racine −3 donne le facteur (x + 3).
- **Équations et signe** : un produit est nul si l'un de ses facteurs l'est ⇒ on résout après factorisation ; pour comparer, on étudie le **signe de la différence factorisée** (un facteur au carré ne change pas le signe). Exemple : V(x) = x(60 − 2x)² est maximal pour x = 10, avec V(10) = 16 000 cm³.
- **Fonction rationnelle** : h = f/g avec f et g polynômes ; D = les réels qui n'annulent pas g. On factorise puis on simplifie, mais les valeurs interdites restent exclues de D.
- **Relations racines / coefficients (degré 3)** : si ax³ + bx² + cx + d a trois racines α, β, γ, alors α + β + γ = −b/a, αβ + βγ + γα = c/a et αβγ = −d/a ; d'où 1/α + 1/β + 1/γ = (αβ + βγ + γα)/(αβγ) sans résoudre l'équation.
- **Polynôme symétrique de degré 3** : ax³ + bx² + bx + a admet toujours −1 pour racine, et vaut (x + 1)(ax² + (b − a)x + a).
- **Éléments simples et télescopage** : 1/(k(k + 1)) = 1/k − 1/(k + 1), donc 1/(1×2) + … + 1/(n(n + 1)) = 1 − 1/(n + 1) = n/(n + 1).
- **Enrichissement** : la **division suivant les puissances décroissantes** factorise aussi — 6x³ + x² + 8x − 5 = (2x − 1)(3x² + 2x + 5).
