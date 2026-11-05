# 📜 Résumé : Limite et continuité

- **Prolongement par continuité** : f se prolonge en x₀ si lim f(x) existe et vaut un réel ℓ ; on simplifie le 0/0, on calcule ℓ, puis on pose g(x₀) = ℓ. Limite infinie ou inexistante : pas de prolongement.
- **Limite et ordre** : si h ≤ f ≤ g et lim h = lim g = ℓ, alors lim f = ℓ ; si |f − ℓ| ≤ |g| et lim g = 0, alors lim f = ℓ ; si f ≥ g et lim g = +∞, alors lim f = +∞. Une inégalité stricte devient large à la limite.
- **Fonctions monotones et limites** : croissante et majorée (ou décroissante et minorée) : limite finie ℓ, pas forcément égale au majorant ; croissante et non majorée : +∞ ; décroissante et non minorée : −∞.
- **Limite d'une composée** : si lim f = ℓ et g est continue en ℓ, alors lim g∘f = g(ℓ) ; sinon on utilise la limite de g en ℓ, même infinie. √(x²) = |x|. Changement de variable : x → +∞ devient X = 1/x → 0⁺.
- **Image d'un intervalle** : l'image d'un intervalle par une fonction continue est un intervalle ; celle de [a ; b] est [min ; max], qui vaut [f(a) ; f(b)] quand f est croissante ([f(b) ; f(a)] si elle est décroissante), pas en général. Sans continuité, l'image peut ne pas être un intervalle.
- **Théorème des valeurs intermédiaires** : f continue, k entre f(a) et f(b) : f(x) = k a une solution dans [a ; b]. Si f(a) × f(b) < 0, f s'annule dans ]a ; b[ ; avec la stricte monotonie, une seule fois. La réciproque est fausse.
- **Dichotomie** : on coupe [a ; b] au milieu c et on garde la moitié où f change de signe ; l'amplitude est divisée par 2 à chaque étape, elle vaut (b − a)/2ⁿ après n étapes.
- **Comportement asymptotique** : limite infinie en a : asymptote x = a ; limite finie b à l'infini : y = b ; sinon a = lim f/x : infini, branche parabolique de direction (Oy) ; 0, direction (Ox) ; réel non nul, on calcule lim [f(x) − ax] : réel b, asymptote y = ax + b ; infini, branche parabolique de direction y = ax. Étudier +∞ et −∞ séparément.
