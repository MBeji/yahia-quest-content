# ⚔️ Primitives — remonter le courant de la dérivée

> 💡 «Dériver, tu sais faire. Primitiver, c'est remonter la rivière : retrouver la fonction dont on ne connaît que la pente.»

Jusqu'ici tu as toujours joué dans le même sens : on te donnait F, tu calculais F′. Ce chapitre inverse la flèche. On te donne f, et tu cherches une fonction F dont la dérivée est exactement f. Lagrange l'a nommée en 1797 la **fonction primitive**. C'est l'outil qui transforme une vitesse en distance parcourue, un débit en quantité produite — et c'est la clé qui ouvre le chapitre des intégrales. Bonne nouvelle : tu n'as rien de neuf à apprendre par cœur. Chaque formule de primitive est une formule de dérivée que tu connais déjà, lue à l'envers.

## 🏰 Qu'est-ce qu'une primitive ?

Prends f(x) = 3x² + 4x − 1 et F(x) = x³ + 2x² − x + 2. Dérive F : F′(x) = 3x² + 4x − 1. On retombe exactement sur f. On dit que F est **une** primitive de f.

> **Définition — primitive** — « Soit f et F deux fonctions définies sur un intervalle I. On dit que F est une primitive de f sur I lorsque F est dérivable sur I et F′(x) = f(x), pour tout x de I. »

Retiens les deux exigences : F doit être **dérivable sur I**, et l'égalité F′ = f doit valoir **en tout point de I**. La primitive se définit toujours **sur un intervalle**, jamais « en un point ».

> 🗡️ **Le réflexe de vérification.** Tu ne « trouves » jamais une primitive : tu la propose puis tu la **dérives**. Si tu retombes sur f, c'est gagné, et la preuve tient en une ligne. Fais-le systématiquement, même en devoir.

_Exemple détaillé_ — vérifions que F(x) = tan x est une primitive de f(x) = 1/cos²x sur ]−π/2, π/2[. F est dérivable sur cet intervalle et F′(x) = 1 + tan²x. Or 1 + tan²x = 1 + sin²x/cos²x = (cos²x + sin²x)/cos²x = 1/cos²x = f(x). ✓

_Exemple_ — sur [1, +∞[, F(x) = 1/x a pour dérivée F′(x) = −1/x² : F est une primitive de f(x) = −1/x² sur cet intervalle.

Toute fonction admet-elle une primitive ? Le programme répond par un théorème, admis :

> **Théorème (admis) — existence** — « Toute fonction continue sur un intervalle I admet au moins une primitive sur I. »

C'est un théorème d'**existence** : il garantit qu'une primitive existe, sans donner la moindre recette pour l'écrire. Il s'invoque à chaque fois qu'un énoncé demande « montrer que f possède des primitives sur I » — il suffit alors de justifier la **continuité** de f sur I.

_Exemple_ — f(x) = |x| est continue sur ℝ (elle n'est pourtant pas dérivable en 0) : par le théorème, elle admet au moins une primitive sur ℝ. Continuité, et non dérivabilité : c'est bien la continuité de f qui est l'hypothèse.

## ⚡ Toutes les primitives d'une même fonction

Reprends F(x) = x³ + 2x² − x + 2, primitive de f(x) = 3x² + 4x − 1. La fonction G(x) = x³ + 2x² − x + 7 a exactement la même dérivée. En ajoutant n'importe quelle constante, on fabrique une nouvelle primitive : il y en a donc une **infinité**. Et ce sont les seules.

> **Théorème — deux primitives diffèrent d'une constante** — « Soit f une fonction continue sur un intervalle I. Si F et G sont deux primitives de f sur I, alors la fonction F − G est constante sur I. »

_Démonstration_ — pour tout x de I, (F − G)′(x) = F′(x) − G′(x) = f(x) − f(x) = 0. Une fonction de dérivée nulle sur un **intervalle** est constante sur cet intervalle. Donc F − G est constante.

Géométriquement, les courbes de deux primitives d'une même fonction se déduisent l'une de l'autre par une **translation verticale** : elles ont partout la même pente, donc la même forme, à une hauteur près.

::: figure Les trois courbes ont partout la même pente : ce sont les primitives d'une même fonction, empilées par translation verticale de vecteur colinéaire à j⃗.
<svg viewBox="0 0 320 210"><path d="M40 190 H305" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M45 200 V20" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M305 190 l-7 -3.5 l0 7 z" fill="#0f172a"/><path d="M45 20 l-3.5 7 l7 0 z" fill="#0f172a"/><path d="M60 150 C110 90 160 170 290 80" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linecap="round"/><path d="M60 150 C110 90 160 170 290 80" fill="none" stroke="#b45309" stroke-width="2.2" stroke-dasharray="6 4" stroke-linecap="round" transform="translate(0,-45)"/><path d="M60 150 C110 90 160 170 290 80" fill="none" stroke="#64748b" stroke-width="2.2" stroke-dasharray="6 4" stroke-linecap="round" transform="translate(0,32)"/><line x1="225" y1="76" x2="225" y2="31" stroke="#0f172a" stroke-width="1.2"/><line x1="225" y1="76" x2="225" y2="108" stroke="#0f172a" stroke-width="1.2"/><text x="232" y="52" font-size="11" font-weight="700" fill="#b45309">+ c₁</text><text x="232" y="100" font-size="11" font-weight="700" fill="#64748b">+ c₂</text><text x="100" y="128" font-size="12" font-weight="700" fill="#0f6e56">C_F</text></svg>
:::

> ⚠️ Le théorème exige un **intervalle**. Sur ]−∞, 0[ ∪ ]0, +∞[, qui n'en est pas un, deux primitives de x ↦ 1/x² peuvent différer d'une constante sur ]0, +∞[ et d'une **autre** constante sur ]−∞, 0[. Précise toujours l'intervalle de travail.

Puisque toutes les primitives ne diffèrent que d'une constante, une seule information supplémentaire suffit à en isoler une : une **condition initiale**.

> **Corollaire — primitive vérifiant une condition initiale** — « Soit f une fonction continue sur un intervalle I. Soit x₀ un réel de I et y₀ un réel. Alors il existe une unique primitive F de f sur I telle que F(x₀) = y₀. »

_Démonstration_ — l'unicité vient du théorème précédent : deux telles primitives diffèrent d'une constante, nulle puisqu'elles coïncident en x₀. Pour l'existence, si G est une primitive quelconque de f sur I, la fonction F définie par F(x) = G(x) − G(x₀) + y₀ est dérivable, vérifie F′ = G′ = f et F(x₀) = y₀.

_Exemple détaillé_ — soit f(x) = √x − x sur ]0, +∞[. Cherchons la primitive G telle que G(1) = 2. On part de F(x) = (2/3)x√x − (1/2)x². Vérification par dérivation : (2/3)x√x = (2/3)x^(3/2) se dérive en (2/3) × (3/2) × x^(1/2) = √x, et −(1/2)x² se dérive en −x. Donc F′ = f ✓. Toutes les primitives sont F + c. Or F(1) = 2/3 − 1/2 = 1/6, et on veut la valeur 2 : c = 2 − 1/6 = 11/6. D'où

$$ G(x) = (2/3)x√x − (1/2)x² + 11/6 $$

## 🔮 Les primitives des fonctions usuelles

Voici la table de référence : c'est ta table des dérivées, lue de droite à gauche. Ici c désigne une constante réelle quelconque, et ω et φ des réels avec ω ≠ 0.

| Fonction f              | Sur I                     | Une primitive F           |
| ----------------------- | ------------------------- | ------------------------- |
| x ↦ a (constante)       | ℝ                         | x ↦ ax + c                |
| x ↦ xⁿ (n ∈ ℕ\*)        | ℝ                         | x ↦ x^(n+1)/(n+1) + c     |
| x ↦ 1/xⁿ (n ≥ 2 entier) | ]0, +∞[ (ou ]−∞, 0[)      | x ↦ x^(−n+1)/(−n+1) + c   |
| x ↦ √x                  | [0, +∞[                   | x ↦ (2/3)x√x + c          |
| x ↦ 1/√x                | ]0, +∞[                   | x ↦ 2√x + c               |
| x ↦ cos x               | ℝ                         | x ↦ sin x + c             |
| x ↦ sin x               | ℝ                         | x ↦ −cos x + c            |
| x ↦ cos(ωx + φ)         | ℝ                         | x ↦ (1/ω) sin(ωx + φ) + c |
| x ↦ sin(ωx + φ)         | ℝ                         | x ↦ −(1/ω) cos(ωx + φ) + c |
| x ↦ 1 + tan²x           | ]−π/2, π/2[               | x ↦ tan x + c             |

_Exemple détaillé_ — primitive de f(x) = 1/x³ sur ]0, +∞[. Ici n = 3, donc F(x) = x^(−2)/(−2) = −1/(2x²). Dérivons pour vérifier : F(x) = −(1/2)x^(−2), donc F′(x) = −(1/2) × (−2)x^(−3) = 1/x³ ✓.

> ⚠️ Le signe de la ligne 1/xⁿ trompe tout le monde. La primitive de 1/x² **n'est pas** 1/x mais **−1/x** (dérive 1/x : tu obtiens −1/x², pas 1/x²). Un seul remède : dériver ta réponse.

> 🗡️ **Le facteur 1/ω se perd tout le temps.** Une primitive de cos(3x) est (1/3)sin(3x), pas sin(3x). Vérifie : ((1/3)sin(3x))′ = (1/3) × 3cos(3x) = cos(3x) ✓. Règle générale : quand l'intérieur est **affine**, la primitive porte le facteur 1 divisé par le coefficient de x.

## 🧮 Linéarité : découper la fonction en morceaux

Une somme se primitive terme à terme, un facteur constant sort. C'est ce qui rend les polynômes immédiats.

> **Théorème — linéarité** — « Soit F et G deux primitives respectives de deux fonctions f et g sur un intervalle I. • La fonction F + G est une primitive sur I de f + g. • Soit λ un réel. La fonction λF est une primitive sur I de λf. »

_Exemple détaillé_ — soit f(x) = −3/x² + 2/√x sur ]0, +∞[. On traite chaque morceau : une primitive de 1/x² est −1/x, donc de −3/x² on tire 3/x ; une primitive de 1/√x est 2√x, donc de 2/√x on tire 4√x. Ainsi F(x) = 3/x + 4√x. Vérification : F′(x) = −3/x² + 4 × 1/(2√x) = −3/x² + 2/√x ✓.

_Exemple détaillé_ — soit f(x) = cos(−2x) + sin(5x) sur ℝ. Pour cos(−2x), ω = −2 : on obtient (−1/2)sin(−2x), qui se simplifie en (1/2)sin(2x). Pour sin(5x), ω = 5 : on obtient −(1/5)cos(5x). D'où F(x) = (1/2)sin(2x) − (1/5)cos(5x). Vérification : F′(x) = (1/2) × 2cos(2x) − (1/5) × (−5 sin(5x)) = cos(2x) + sin(5x), et cos(2x) = cos(−2x) car le cosinus est pair ✓.

> ⚠️ La linéarité s'arrête à la somme et au produit par un réel. **Il n'existe aucune formule pour la primitive d'un produit ou d'un quotient.** Si F primitive f et G primitive g, F × G n'est presque jamais une primitive de f × g : prends f = g = 1 sur ℝ, F = G = x ; alors (F × G)′ = (x²)′ = 2x, qui n'est pas f × g = 1.

## 🌀 Les formes composées — le cœur du calcul

Quand on ne reconnaît pas une fonction usuelle, on cherche un **motif** : une fonction u et sa dérivée u′ qui apparaissent ensemble. Chaque ligne du tableau ci-dessous est une formule de dérivation composée du chapitre 3, lue à l'envers. u et v désignent deux fonctions dérivables sur I.

| Fonction f          | Condition sur I           | Une primitive F     |
| ------------------- | ------------------------- | ------------------- |
| u′uⁿ (n ∈ ℕ\*)      | —                         | u^(n+1)/(n+1)       |
| u′v + v′u           | —                         | u·v                 |
| u′/uⁿ (n ≥ 2 entier) | u ne s'annule pas sur I   | u^(−n+1)/(−n+1)     |
| (u′v − v′u)/v²      | v ne s'annule pas sur I   | u/v                 |
| u′/√u               | u strictement positive    | 2√u                 |
| u′√u                | u positive                | (2/3)u√u            |
| u′ · ⁿ√(u^(1−n)) (n ≥ 2) | u strictement positive | n · ⁿ√u             |
| u′ (w′∘u)           | w dérivable sur u(I)      | w∘u                 |

La **méthode** est toujours la même : repérer un candidat u (le contenu d'une parenthèse, d'une racine, d'un dénominateur), calculer u′, puis ajuster par une constante multiplicative pour faire apparaître exactement le motif.

_Exemple détaillé (u′uⁿ)_ — soit f(x) = (2x − 1)(x² − x + 3) sur ℝ, et cherchons la primitive F telle que F(1) = 2. On pose u(x) = x² − x + 3 ; alors u′(x) = 2x − 1, et f = u′u : c'est la ligne 1 avec n = 1. Donc u²/2 convient, et F(x) = (x² − x + 3)²/2 + c. Vérification : ((x² − x + 3)²/2)′ = (1/2) × 2(x² − x + 3)(2x − 1) = f(x) ✓. Condition : u(1) = 3, donc (1/2) × 9 + c = 2, d'où c = −5/2 et

$$ F(x) = (x² − x + 3)²/2 − 5/2 $$

_Exemple détaillé (u′/uⁿ)_ — soit f(x) = (6x − 1)/(3x² − x)² sur ]1, +∞[, avec F(2) = 0. On pose u(x) = 3x² − x, donc u′(x) = 6x − 1 et f = u′/u² (u ne s'annule pas sur ]1, +∞[). La table donne u^(−1)/(−1) = −1/u. Vérification : (−u^(−1))′ = u^(−2)u′ = u′/u² ✓. Donc F(x) = −1/(3x² − x) + c. Or u(2) = 10 : −1/10 + c = 0 donne c = 1/10, et F(x) = −1/(3x² − x) + 1/10.

_Exemple détaillé (u′√u)_ — soit f(x) = x√(x² + 1) sur ℝ. On pose u(x) = x² + 1, u′(x) = 2x. Il manque un facteur 2 : f = (1/2) × u′√u. La table donne (2/3)u√u pour u′√u, donc F(x) = (1/2) × (2/3)(x² + 1)√(x² + 1) = (1/3)(x² + 1)√(x² + 1). Vérification : F(x) = (1/3)u^(3/2), donc F′(x) = (1/3) × (3/2)u^(1/2) × u′ = (1/2)√(x² + 1) × 2x = x√(x² + 1) ✓.

_Exemple détaillé (u′/√u)_ — soit f(x) = (2x − 1)/√(x² − x) sur ]1, +∞[. Avec u(x) = x² − x, strictement positive sur ]1, +∞[, et u′(x) = 2x − 1, on lit directement F(x) = 2√(x² − x). Vérification : F′(x) = 2 × u′/(2√u) = (2x − 1)/√(x² − x) ✓.

_Exemple détaillé (u′(w′∘u))_ — soit f(x) = x² sin(x³ + 1) sur ℝ. On pose u(x) = x³ + 1, donc u′(x) = 3x² : f = (1/3) u′ sin(u). Comme −cos est une primitive de sin, F(x) = −(1/3)cos(x³ + 1). Vérification : F′(x) = −(1/3) × (−sin(x³ + 1)) × 3x² = x² sin(x³ + 1) ✓.

_Exemple détaillé (racine d'une fonction affine)_ — soit f(x) = √(2 − x) sur ]−∞, 2], avec F(1) = 0. On pose u(x) = 2 − x, u′(x) = −1, donc f = −u′√u. D'où F(x) = −(2/3)(2 − x)√(2 − x) + c. Vérification : −(2/3)u^(3/2) se dérive en −(2/3) × (3/2)u^(1/2) × (−1) = √(2 − x) ✓. Condition : en x = 1, u = 1 et −(2/3) + c = 0, donc c = 2/3.

> ⚠️ **Le piège du « facteur qui manque ».** Pour primitiver x(x² + 1)⁵, on ne peut pas écrire (x² + 1)⁶/6 : il faudrait u′ = 2x, or on n'a que x. On compense par une constante : F(x) = (1/2) × (x² + 1)⁶/6 = (x² + 1)⁶/12. Cet ajustement n'est possible que si le facteur manquant est une **constante** — jamais si c'est une fonction de x.

> ⚠️ **F(2x) n'est pas une primitive de f(2x).** Si F′ = f, alors (F(2x))′ = 2f(2x). La bonne primitive de x ↦ f(2x) est x ↦ F(2x)/2. Même logique que le facteur 1/ω des lignes trigonométriques.

## 📐 Réécrire avant de primitiver

Quand aucun motif n'apparaît, on ne force pas : on **transforme l'écriture** de f jusqu'à tomber sur des formes connues. Trois techniques couvrent l'essentiel du programme.

**1. Décomposer une fraction rationnelle.** _Exemple détaillé_ — soit f(x) = (2x³ − 11x² + 20x − 10)/(x − 2)² sur ]2, +∞[. On cherche a, b, c tels que f(x) = ax + b + c/(x − 2)². En réduisant au même dénominateur : (ax + b)(x − 2)² + c = ax³ + (b − 4a)x² + (4a − 4b)x + (4b + c). L'identification donne a = 2, puis b − 4a = −11 donc b = −3 ; on contrôle 4a − 4b = 8 + 12 = 20 ✓ ; enfin 4b + c = −10 donne c = 2. Donc f(x) = 2x − 3 + 2/(x − 2)², dont une primitive est

$$ F(x) = x² − 3x − 2/(x − 2) $$

Vérification : F′(x) = 2x − 3 + 2/(x − 2)² (car (−2/(x − 2))′ = 2/(x − 2)²) ✓.

**2. Utiliser une identité trigonométrique.** Un carré ou un cube de sinus/cosinus ne figure dans aucune table : on le **linéarise**.

_Exemple détaillé_ — pour f(x) = sin²x, on part de sin²x = (1 − cos 2x)/2. Une primitive est alors F(x) = x/2 − (1/4)sin(2x). Vérification : F′(x) = 1/2 − (1/4) × 2cos(2x) = (1 − cos 2x)/2 = sin²x ✓. De même, cos²x = (1 + cos 2x)/2 donne x/2 + (1/4)sin(2x).

_Exemple détaillé_ — pour g(x) = sin³x, on écrit sin³x = sin x(1 − cos²x) = sin x − sin x cos²x. Le premier terme se primitive en −cos x. Le second est un motif : avec u = cos x, u′ = −sin x, on a −sin x cos²x = u′u², dont une primitive est u³/3. D'où G(x) = −cos x + cos³x/3. Vérification : G′(x) = sin x + (3cos²x × (−sin x))/3 = sin x − sin x cos²x = sin³x ✓. Le même découpage sur cos³x = cos x(1 − sin²x) donne sin x − sin³x/3.

**3. Passer par tan.** _Exemple détaillé_ — pour f(x) = tan²x sur ]−π/2, π/2[, on utilise tan²x = (1 + tan²x) − 1 : F(x) = tan x − x, puisque (tan x − x)′ = 1 + tan²x − 1 = tan²x ✓. Plus subtil, f(x) = tan³x/cos²x se lit u′u³ avec u = tan x et u′ = 1 + tan²x = 1/cos²x : une primitive est tan⁴x/4.

## 🧪 Applications : remonter d'un taux à une quantité

C'est ici que la primitive prend son sens physique. Un taux instantané de variation est une **dérivée** ; retrouver la grandeur elle-même, c'est primitiver. La condition initiale est alors une mesure : la quantité déjà produite, la vitesse au départ, la position de départ.

_Exemple détaillé (chimie)_ — la quantité produite pendant les dix premières secondes d'une expérience est de 12 g. Au bout de t secondes (t ≥ 10), le taux de production instantané est Q′(t) = 40/t² + 200/t³ (en g/s). Cherchons Q. Une primitive de 40/t² est −40/t ; une primitive de 200/t³ est 200 × t^(−2)/(−2) = −100/t². Donc Q(t) = −40/t − 100/t² + c. La condition Q(10) = 12 donne −4 − 1 + c = 12, soit c = 17, et

$$ Q(t) = 17 − 40/t − 100/t² $$

Vérification : Q′(t) = 40/t² + 200/t³ ✓. Peut-on atteindre 20 g ? Non : quand t tend vers +∞, Q(t) tend vers 17, et Q est croissante, donc Q(t) < 17 pour tout t. La production plafonne sous 17 g.

_Exemple détaillé (cinématique)_ — un mobile part de l'origine avec une vitesse de 3 m/s, et son accélération est a(t) = 2t (en m/s²). Comme v′ = a, on a v(t) = t² + c, et v(0) = 3 donne v(t) = t² + 3. Comme x′ = v, on a x(t) = t³/3 + 3t + c′, et x(0) = 0 donne x(t) = t³/3 + 3t. Vérification : x′(t) = t² + 3 = v(t) et v′(t) = 2t = a(t) ✓. Deux primitivations successives, deux conditions initiales.

> 🗡️ **Deux primitivations = deux constantes.** Chaque « remontée » introduit sa propre constante, donc réclame sa propre condition initiale. Une équation du type f″ = g ne se résout complètement qu'avec **deux** données (par exemple f(0) et f′(0)).

> 🏆 Cinquième porte franchie, héros. Tu sais reconnaître une primitive, prouver qu'elle existe par la continuité, décrire toute la famille à une constante près, en isoler une par une condition initiale, et calculer : fonctions usuelles, linéarité, formes composées, réécritures. Garde ces réflexes bien affûtés — au chapitre suivant, la primitive devient une **aire** sous la courbe, et cette machinerie prend le nom d'intégrale.
