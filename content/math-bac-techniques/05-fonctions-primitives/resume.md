# 📜 Résumé : Fonctions primitives

- **Primitive** : F est une primitive de f sur un intervalle I si F est dérivable sur I et F′ = f ; on vérifie en dérivant F (jamais f), et F doit être dérivable en tout point de I.
- **Toutes les primitives** : toute fonction continue sur un intervalle I admet des primitives sur I ; si F en est une, ce sont exactement les F + c, c réel ; hors d'un intervalle (par exemple ℝ*), deux primitives peuvent différer de constantes différentes.
- **Condition initiale** : sur un intervalle I, pour a dans I et b réel, il existe une seule primitive F de f avec F(a) = b ; on pose F = F₀ + c et c = b − F₀(a) ; une aire sous une droite depuis 0 en est un exemple.
- **Primitives usuelles** : ax, xⁿ⁺¹/(n + 1) pour n entier différent de −1 (sur ]−∞ ; 0[ ou ]0 ; +∞[ si n ≤ −2), 2√x pour 1/√x, sin x, −cos x, tan x, −cotan x ; pour cos(ax + b) et sin(ax + b), on divise par a ; la fonction 1/x n'est pas dans ce tableau.
- **Linéarité** : αF + βG est une primitive de αf + βg ; elle vaut pour les sommes et les constantes, pas pour les produits ; F + G est une primitive de 2f, pas de f.
- **u′uⁿ et u′/√u** : uⁿ⁺¹/(n + 1) pour n entier différent de −1 (u non nul si n < 0), 2√u pour u′/√u avec u > 0 ; on compense la constante manquante devant u′.
- **Produit, quotient, composée** : u′v + v′u a pour primitive uv ; (u′v − v′u)/v² a pour primitive u/v ; (v′∘u)u′ a pour primitive v∘u ; la primitive de sin est −cos.
- **Réécrire** : développer ou découper, linéariser sin a cos b et cos a cos b, écrire sin³x = sin x (1 − cos²x), identifier ax + b + c/(x − 1)² ; on contrôle toujours en dérivant.
