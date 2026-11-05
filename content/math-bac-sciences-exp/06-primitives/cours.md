# ⚔️ Primitives — retrouver la fonction d'après sa pente

> 💡 «Dériver, tu sais faire. Primitiver, c'est remonter la rivière : retrouver la fonction dont on ne connaît que la pente.»

Jusqu'ici, on te donnait une fonction F et tu calculais F′. Ce chapitre inverse la flèche : on te donne f, et tu cherches une fonction F dont la dérivée est exactement f. Lagrange l'a nommée en 1797 la **fonction primitive**. Huit notions te mènent de la définition jusqu'à l'étude d'une primitive que tu ne sais même pas écrire. Tu n'as presque rien à apprendre par cœur : chaque formule de primitive est une formule de dérivée lue à l'envers. On suppose acquis la dérivation (chapitre 3) et les fonctions réciproques (chapitre 4).

## 🏰 Primitive : retrouver la fonction d'après sa pente

Sur ℝ, prends F(x) = x³ + 2x² − x + 2 et f(x) = 3x² + 4x − 1. En dérivant F, on trouve F′(x) = 3x² + 4x − 1 : c'est exactement f. On dit que F « remonte » f.
Comment vérifier qu'une fonction en remonte une autre, et toute fonction a-t-elle une telle « remontée » ?

::: definition
**Primitive** — Soit f et F deux fonctions définies sur un intervalle I. On dit que F est une primitive de f sur I lorsque F est dérivable sur I et que F′(x) = f(x) pour tout x de I.
:::

::: exemple Vérifier qu'une fonction est une primitive

1. F(x) = 1/x et f(x) = −1/x² sur I = [1, +∞[ : F est dérivable sur I et F′(x) = −1/x² = f(x) ✓ (on dérive le candidat F, jamais f).
2. F(x) = x² et f(x) = 2x sur I = ℝ : F′(x) = 2x = f(x) ✓.
3. F(x) = tan x et f(x) = 1/cos²x sur I = ]−π/2, π/2[ : F′(x) = 1 + tan²x = (cos²x + sin²x)/cos²x = 1/cos²x = f(x) ✓. L'intervalle compte : tan n'est pas définie en π/2, la vérification n'a de sens que sur ]−π/2, π/2[.

:::

::: piege
**Erreur : lire la définition à l'envers.** Avec F(x) = x³ et f(x) = 3x², on a F′ = f : F est une primitive de f. Mais f′(x) = 6x n'est pas F : f n'est pas une primitive de F. L'erreur tente parce que « être la primitive de » ressemble à une relation symétrique. Elle ne l'est pas : le rôle de la dérivée est tenu par f, jamais par F. Dans le doute, dérive la fonction que tu proposes comme primitive.
:::

Toute fonction a-t-elle une primitive ? Le programme répond par un théorème d'existence, admis.

::: propriete
**Théorème (admis)** : toute fonction continue sur un intervalle I admet au moins une primitive sur I.
Il garantit l'existence sans fournir de recette. Il s'invoque dès qu'on demande de « montrer que f possède des primitives sur I » : il suffit de justifier la continuité de f sur I.
Cas limite : f(x) = |x| est continue sur ℝ mais pas dérivable en 0 ; elle a pourtant des primitives, par exemple F(x) = x|x|/2 (F(x) = x²/2 pour x ≥ 0 et −x²/2 pour x ≤ 0, de dérivée |x| des deux côtés). C'est la continuité de f qui compte, pas sa dérivabilité.
:::

Puisque F′ = f, le signe de f commande les variations de F : là où f > 0, F croît ; là où f < 0, F décroît ; si f s'annule en changeant de signe, F a un extremum. Par exemple, f(x) = 2x − 6 est négative sur ]−∞, 3[ et positive sur ]3, +∞[ : toute primitive de f décroît puis croît, avec un minimum en 3.

::: verifie À toi : vérifier une primitive
Montrer que F(x) = (x − 1)/(x + 1) est une primitive de f(x) = 2/(x + 1)² sur ]−1, +∞[.

---

F est dérivable sur ]−1, +∞[ (le dénominateur ne s'annule pas). Par la formule du quotient, F′(x) = ((x + 1) − (x − 1))/(x + 1)² = 2/(x + 1)² = f(x) ✓. C'est la définition : on dérive F, on retombe sur f, sur tout l'intervalle.
:::

::: retenir
F est une primitive de f sur I quand F′ = f en tout point de I ; toute fonction continue sur un intervalle en possède une ; on valide toujours une primitive en la dérivant.
:::

## ⚡ Toutes les primitives, et une seule sous condition

Reprends F(x) = x³ − x² − 4x, primitive de f(x) = 3x² − 2x − 4. Ajoute 3 à F, ou retranche 3 : la dérivée ne change pas, donc F + 3 et F − 3 sont aussi des primitives de f.
Combien f a-t-elle de primitives, et comment en isoler une seule ?

::: figure Les courbes C_F (vert), C₁ (orange) et C₂ (gris), celles de F, F + 3 et F − 3, se déduisent l'une de l'autre par une translation verticale : à chaque abscisse, la pente est la même
<svg viewBox="0 0 340 260">
<title>Courbe de F(x) = x³ − x² − 4x sur [0 ; 3] et ses deux translatées verticales de ±3</title>
<line x1="30" y1="135" x2="318" y2="135" stroke="#0f172a" stroke-width="1.6"/>
<line x1="60" y1="248" x2="60" y2="10" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="318,135 310,131 310,139" fill="#0f172a"/>
<polygon points="60,10 56,18 64,18" fill="#0f172a"/>
<polyline points="60.0,99.0 63.8,101.4 67.7,103.9 71.5,106.4 75.3,109.0 79.2,111.6 83.0,114.2 86.8,116.8 90.7,119.4 94.5,121.9 98.3,124.5 102.2,127.0 106.0,129.5 109.8,132.0 113.7,134.4 117.5,136.7 121.3,138.9 125.2,141.1 129.0,143.2 132.8,145.1 136.7,147.0 140.5,148.7 144.3,150.3 148.2,151.8 152.0,153.1 155.8,154.3 159.7,155.3 163.5,156.1 167.3,156.8 171.2,157.2 175.0,157.5 178.8,157.5 182.7,157.4 186.5,157.0 190.3,156.3 194.2,155.4 198.0,154.3 201.8,152.9 205.7,151.2 209.5,149.3 213.3,147.0 217.2,144.4 221.0,141.6 224.8,138.4 228.7,134.9 232.5,131.1 236.3,126.9 240.2,122.3 244.0,117.4 247.8,112.2 251.7,106.5 255.5,100.5 259.3,94.0 263.2,87.2 267.0,79.9 270.8,72.2 274.7,64.1 278.5,55.5 282.3,46.5 286.2,37.0 290.0,27.0" fill="none" stroke="#b45309" stroke-width="2.2" stroke-dasharray="6 3" stroke-linejoin="round"/>
<polyline points="60.0,171.0 63.8,173.4 67.7,175.9 71.5,178.4 75.3,181.0 79.2,183.6 83.0,186.2 86.8,188.8 90.7,191.4 94.5,193.9 98.3,196.5 102.2,199.0 106.0,201.5 109.8,204.0 113.7,206.4 117.5,208.7 121.3,210.9 125.2,213.1 129.0,215.2 132.8,217.1 136.7,219.0 140.5,220.7 144.3,222.3 148.2,223.8 152.0,225.1 155.8,226.3 159.7,227.3 163.5,228.1 167.3,228.8 171.2,229.2 175.0,229.5 178.8,229.5 182.7,229.4 186.5,229.0 190.3,228.3 194.2,227.4 198.0,226.3 201.8,224.9 205.7,223.2 209.5,221.3 213.3,219.0 217.2,216.4 221.0,213.6 224.8,210.4 228.7,206.9 232.5,203.1 236.3,198.9 240.2,194.3 244.0,189.4 247.8,184.2 251.7,178.5 255.5,172.5 259.3,166.0 263.2,159.2 267.0,151.9 270.8,144.2 274.7,136.1 278.5,127.5 282.3,118.5 286.2,109.0 290.0,99.0" fill="none" stroke="#64748b" stroke-width="2.2" stroke-dasharray="6 3" stroke-linejoin="round"/>
<polyline points="60.0,135.0 63.8,137.4 67.7,139.9 71.5,142.4 75.3,145.0 79.2,147.6 83.0,150.2 86.8,152.8 90.7,155.4 94.5,157.9 98.3,160.5 102.2,163.0 106.0,165.5 109.8,168.0 113.7,170.4 117.5,172.7 121.3,174.9 125.2,177.1 129.0,179.2 132.8,181.1 136.7,183.0 140.5,184.7 144.3,186.3 148.2,187.8 152.0,189.1 155.8,190.3 159.7,191.3 163.5,192.1 167.3,192.8 171.2,193.2 175.0,193.5 178.8,193.5 182.7,193.4 186.5,193.0 190.3,192.3 194.2,191.4 198.0,190.3 201.8,188.9 205.7,187.2 209.5,185.3 213.3,183.0 217.2,180.4 221.0,177.6 224.8,174.4 228.7,170.9 232.5,167.1 236.3,162.9 240.2,158.3 244.0,153.4 247.8,148.2 251.7,142.5 255.5,136.5 259.3,130.0 263.2,123.2 267.0,115.9 270.8,108.2 274.7,100.1 278.5,91.5 282.3,82.5 286.2,73.0 290.0,63.0" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/>
<line x1="213.34" y1="147" x2="213.34" y2="219" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="213.34" cy="147" r="3.5" fill="#b45309"/>
<circle cx="213.34" cy="183" r="3.5" fill="#0f6e56"/>
<circle cx="213.34" cy="219" r="3.5" fill="#64748b"/>
<g font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">
<text x="296.01" y="31" fill="#b45309">C₁</text>
<text x="296.01" y="67" fill="#0f6e56">C_F</text>
<text x="296.01" y="103" fill="#64748b">C₂</text>
<text x="221.34" y="169.0" fill="#0f172a">+ 3</text>
<text x="221.34" y="205.0" fill="#0f172a">− 3</text>
<text x="290.01" y="151" text-anchor="middle" fill="#0f172a">3</text>
<text x="52" y="22" text-anchor="end" fill="#0f172a">y</text>
</g>
</svg>
:::

Sur la figure, C_F, C₁ et C₂ ont la même pente à chaque abscisse : ce sont les courbes de F, de F + 3 et de F − 3. On passe de l'une à l'autre par une translation de vecteur colinéaire à j⃗.

::: propriete
**Théorème** : soit f continue sur un intervalle I. Si F et G sont deux primitives de f sur I, alors F − G est constante sur I.
En effet, (F − G)′ = F′ − G′ = f − f = 0 sur I, et une fonction de dérivée nulle sur un intervalle y est constante.
**Corollaire** : pour tout x₀ de I et tout réel y₀, f possède une unique primitive F sur I telle que F(x₀) = y₀.
Existence : si G est une primitive de f, alors F(x) = G(x) − G(x₀) + y₀ convient. Unicité : deux telles primitives diffèrent d'une constante, nulle puisqu'elles coïncident en x₀.
:::

::: exemple Une primitive qui prend une valeur imposée

1. f(x) = √x − x sur ]0, +∞[. On propose F(x) = (2/3)x√x − (1/2)x². Pour vérifier : (2/3)x√x = (2/3)x^(3/2) se dérive en (2/3)(3/2)x^(1/2) = √x, et −(1/2)x² en −x. Donc F′ = f ✓.
2. Toutes les primitives de f sont F + c, avec c constante (théorème).
3. On veut G(1) = 2. Or F(1) = 2/3 − 1/2 = 1/6, donc c = 2 − 1/6 = 11/6 (la condition fixe c).
4. G(x) = (2/3)x√x − (1/2)x² + 11/6, et G(1) = 1/6 + 11/6 = 2 ✓.

:::

::: piege
**Erreur : appliquer le théorème sur un ensemble qui n'est pas un intervalle.** Sur ℝ*, f(x) = 3/x⁴ a pour primitive F(x) = −1/x³. Soit G la fonction égale à F + 2 sur ]0, +∞[ et à F − 1 sur ]−∞, 0[. Elle est dérivable sur ℝ* et G′ = f, donc G est une primitive de f sur ℝ*. Pourtant G − F vaut 2 d'un côté et −1 de l'autre : elle n'est pas constante. L'erreur tente parce que « deux primitives diffèrent d'une constante » se retient sans son hypothèse. Il faut un intervalle : on travaille séparément sur ]0, +∞[ et sur ]−∞, 0[.
:::

::: verifie À toi : fixer la constante
Déterminer la primitive F de f(x) = 9x² − 2 sur ℝ telle que F(1) = 4.

---

Les primitives de f sont 3x³ − 2x + c (on dérive pour contrôler : 9x² − 2 ✓). La condition donne F(1) = 3 − 2 + c = 1 + c = 4, donc c = 3 et F(x) = 3x³ − 2x + 3. Contrôle : F(1) = 3 − 2 + 3 = 4 ✓.
:::

::: retenir
Deux primitives de f sur un intervalle diffèrent d'une constante (courbes translatées verticalement) ; une condition F(x₀) = y₀ fixe la constante et isole une primitive unique.
:::

## 🔮 Primitives usuelles et linéarité

Dérive cos(3x) : tu trouves −3 sin(3x). Lue à l'envers, cette formule donne une primitive de sin(3x). Chaque ligne de ta table des dérivées fournit ainsi une ligne de la table des primitives.
Comment la lire dans l'autre sens sans se tromper de signe ni de facteur ?

Dans la table, c désigne une constante réelle ; ω et φ sont des réels avec ω ≠ 0.

| Fonction f              | Sur I                | Une primitive F            |
| ----------------------- | -------------------- | -------------------------- |
| x ↦ a (constante)       | ℝ                    | x ↦ ax + c                 |
| x ↦ xⁿ (n ∈ ℕ\*)        | ℝ                    | x ↦ x^(n+1)/(n+1) + c      |
| x ↦ 1/xⁿ (n ≥ 2 entier) | ]0, +∞[ (ou ]−∞, 0[) | x ↦ x^(−n+1)/(−n+1) + c    |
| x ↦ √x                  | [0, +∞[              | x ↦ (2/3)x√x + c           |
| x ↦ 1/√x                | ]0, +∞[              | x ↦ 2√x + c                |
| x ↦ cos x               | ℝ                    | x ↦ sin x + c              |
| x ↦ sin x               | ℝ                    | x ↦ −cos x + c             |
| x ↦ cos(ωx + φ)         | ℝ                    | x ↦ (1/ω) sin(ωx + φ) + c  |
| x ↦ sin(ωx + φ)         | ℝ                    | x ↦ −(1/ω) cos(ωx + φ) + c |
| x ↦ 1 + tan²x           | ]−π/2, π/2[          | x ↦ tan x + c              |

::: propriete
**Linéarité** : si F et G sont des primitives de f et g sur I, alors F + G est une primitive de f + g, et λF est une primitive de λf pour tout réel λ. On primitive donc une somme terme à terme, et un facteur constant sort.
Ce théorème découle des opérations sur les dérivées : (F + G)′ = f + g et (λF)′ = λf.
:::

::: exemple Primitiver terme à terme

1. f(x) = −3/x² + 2/√x sur ]0, +∞[. Une primitive de 1/x² est −1/x, donc −3/x² donne 3/x ; une primitive de 1/√x est 2√x, donc 2/√x donne 4√x. D'où F(x) = 3/x + 4√x ; contrôle : F′(x) = −3/x² + 4/(2√x) = −3/x² + 2/√x ✓.
2. f(x) = 2/x³ − 3/x⁴ sur [−3, −1]. Avec n = 3, 1/x³ donne x^(−2)/(−2) = −1/(2x²), donc 2/x³ donne −1/x² ; avec n = 4, 1/x⁴ donne −1/(3x³), donc −3/x⁴ donne 1/x³. D'où F(x) = −1/x² + 1/x³ ; contrôle : F′(x) = 2/x³ − 3/x⁴ ✓.
3. f(x) = cos(−2x) + sin(5x) sur ℝ. Ici ω = −2 puis ω = 5 : cos(−2x) donne (1/(−2)) sin(−2x) = (1/2) sin(2x), et sin(5x) donne −(1/5) cos(5x). D'où F(x) = (1/2) sin(2x) − (1/5) cos(5x) ; contrôle : F′(x) = cos(2x) + sin(5x), et cos(2x) = cos(−2x) car le cosinus est pair ✓.

:::

::: piege
**Erreur : deux oublis qui reviennent toujours.** Sur 1/x², on écrit « 1/x ». Or (1/x)′ = −1/x² : l'oubli du signe moins renverse tout, la bonne primitive est −1/x. Sur cos(3x), on écrit « sin(3x) ». Or (sin 3x)′ = 3cos(3x) : il manque le facteur 1/ω, la bonne primitive est (1/3) sin(3x). Dans les deux cas, un seul geste suffit à repérer la faute : dériver ta réponse.
:::

La linéarité s'arrête à la somme et au produit par un réel : il n'y a aucune formule pour la primitive d'un produit ou d'un quotient. Avec f = g = 1 sur ℝ et F = G = x, on a (F × G)′ = (x²)′ = 2x, qui n'est pas f × g = 1.

::: verifie À toi : une table, un facteur, un signe
Déterminer une primitive de f(x) = 5/x² − sin(2x + 1) sur ]0, +∞[.

---

5/x² donne 5 × (−1/x) = −5/x (ligne 1/xⁿ avec n = 2). sin(2x + 1) donne −(1/2) cos(2x + 1) (ligne sin(ωx + φ) avec ω = 2), donc −sin(2x + 1) donne +(1/2) cos(2x + 1). D'où F(x) = −5/x + (1/2) cos(2x + 1). Contrôle : F′(x) = 5/x² − (1/2) × 2 sin(2x + 1) = 5/x² − sin(2x + 1) ✓.
:::

::: retenir
Une primitive usuelle se lit dans la table (signe de 1/xⁿ, facteur 1/ω) ; une somme et un facteur constant se primitivent terme à terme ; aucune formule pour un produit.
:::

## 🌀 Formes composées (1) : puissances et racines

Dériver (x² − x + 3)² donne 2(x² − x + 3)(2x − 1) : le facteur 2x − 1 est la dérivée de l'intérieur. Lue à l'envers, cette formule dit qu'une primitive de (2x − 1)(x² − x + 3) est (x² − x + 3)²/2.
Comment repérer une telle fonction u cachée dans l'écriture de f ?

::: propriete
**Formes composées** : soit u une fonction dérivable sur I.

| f              | Condition sur I         | Une primitive F |
| -------------- | ----------------------- | --------------- |
| u′uⁿ (n ∈ ℕ\*) | aucune                  | u^(n+1)/(n+1)   |
| u′/uⁿ (n ≥ 2)  | u ne s'annule pas sur I | u^(−n+1)/(−n+1) |
| u′/√u          | u strictement positive  | 2√u             |
| u′√u           | u positive              | (2/3)u√u        |

Chaque ligne est une dérivée composée du chapitre 3 lue à l'envers.
:::

::: methode
**Reconnaître le motif** : (1) repérer un candidat u (le contenu d'une parenthèse, d'une racine ou d'un dénominateur) ; (2) calculer u′ ; (3) comparer u′ au facteur présent dans f ; (4) ajuster par une constante multiplicative si besoin ; (5) dériver pour contrôler. Cas limite : l'ajustement n'est permis que si le facteur manquant est une constante.
:::

::: exemple Trois fonctions, trois motifs, une condition initiale

1. f(x) = (2x − 1)(x² − x + 3) sur ℝ, avec F(1) = 2. On pose u(x) = x² − x + 3, donc u′(x) = 2x − 1 : f = u′u, ligne n = 1. Une primitive est u²/2, d'où F(x) = (x² − x + 3)²/2 + c. Comme u(1) = 3, F(1) = 9/2 + c = 2 donne c = −5/2.
2. f(x) = (6x − 1)/(3x² − x)² sur ]1, +∞[, avec F(2) = 0. On pose u(x) = 3x² − x, u′(x) = 6x − 1, et u ne s'annule pas sur ]1, +∞[ : f = u′/u². La table donne u^(−1)/(−1) = −1/u, d'où F(x) = −1/(3x² − x) + c. Comme u(2) = 10, F(2) = −1/10 + c = 0 donne c = 1/10.
3. f(x) = tan²x/cos²x sur ]−π/2, π/2[, avec F(−π/4) = −1. On pose u(x) = tan x, u′(x) = 1/cos²x : f = u′u². Une primitive est u³/3, d'où F(x) = (tan³x)/3 + c. Comme tan(−π/4) = −1, F(−π/4) = −1/3 + c = −1 donne c = −2/3.

:::

::: exemple Les motifs avec une racine

1. f(x) = (2x − 1)/√(x² − x) sur ]1, +∞[. On pose u(x) = x² − x, strictement positive sur ]1, +∞[, et u′(x) = 2x − 1 : f = u′/√u, d'où F(x) = 2√(x² − x). Contrôle : F′(x) = 2 × (2x − 1)/(2√(x² − x)) = f(x) ✓.
2. f(x) = x√(x² + 1) sur ℝ. On pose u(x) = x² + 1, u′(x) = 2x : il manque un facteur 2, constant, donc f = (1/2)u′√u. D'où F(x) = (1/2) × (2/3)u√u = (1/3)(x² + 1)√(x² + 1). Contrôle : F = (1/3)u^(3/2) se dérive en (1/3)(3/2)u^(1/2) × 2x = x√(x² + 1) ✓.

:::

::: piege
**Erreur : compenser un facteur manquant qui dépend de x.** Pour f(x) = (x² + 1)⁴, on voit u = x² + 1 et l'on aimerait écrire (x² + 1)⁵/5, mais u′ = 2x n'apparaît pas. On « corrige » en divisant par 2x : (x² + 1)⁵/(10x). Cette fonction n'est pas une primitive de f : en la dérivant, le quotient fait apparaître d'autres termes. L'erreur tente parce que l'ajustement par une constante marche très bien. Ici le facteur manquant est 2x, une fonction : le motif est absent. On développe alors f(x) = x⁸ + 4x⁶ + 6x⁴ + 4x² + 1, dont une primitive est x⁹/9 + 4x⁷/7 + 6x⁵/5 + 4x³/3 + x.
:::

::: verifie À toi : poser u et ajuster
Déterminer la primitive F de f(x) = 3x²/(x³ + 4)² sur [0, +∞[ telle que F(0) = 0.

---

On pose u(x) = x³ + 4, strictement positive sur [0, +∞[, et u′(x) = 3x² : f = u′/u², sans facteur à ajuster. La ligne u′/uⁿ avec n = 2 donne −1/u, donc F(x) = −1/(x³ + 4) + c. Condition : F(0) = −1/4 + c = 0, d'où c = 1/4 et F(x) = −1/(x³ + 4) + 1/4.
:::

::: retenir
Pour u′uⁿ, u′/uⁿ, u′/√u et u′√u, on pose u, on calcule u′, on ajuste par une constante, puis on dérive pour contrôler.
:::

## 🧩 Formes composées (2) : produit, quotient, composée

Dériver x sin x donne sin x + x cos x : un produit se dérive en deux termes. Dériver sin x / x donne (x cos x − sin x)/x². Lues à l'envers, ces formules donnent des primitives qu'aucune table ne contient.
Comment reconnaître, dans f, une dérivée de produit, de quotient ou de composée ?

::: propriete
**Formes composées** : soit u, v dérivables sur I et w dérivable sur u(I).

| f              | Condition sur I         | Une primitive F |
| -------------- | ----------------------- | --------------- |
| u′v + v′u      | aucune                  | u·v             |
| (u′v − v′u)/v² | v ne s'annule pas sur I | u/v             |
| u′ · (w′∘u)    | aucune                  | w∘u             |

La troisième ligne est la dérivée de w∘u, lue à l'envers : (w∘u)′ = u′ · (w′∘u).
:::

::: exemple Reconnaître le produit, le quotient, la composée

1. f(x) = sin x + x cos x sur ℝ. Avec u(x) = x et v(x) = sin x, on a u′v + v′u = sin x + x cos x : f = (x sin x)′, donc F(x) = x sin x.
2. f(x) = (x cos x − sin x)/x² sur ]0, +∞[. Avec u(x) = sin x et v(x) = x, on a u′v − v′u = x cos x − sin x et v ne s'annule pas : F(x) = (sin x)/x. Contrôle : F′(x) = (x cos x − sin x)/x² ✓.
3. f(x) = x² sin(x³ + 1) sur ℝ. On pose u(x) = x³ + 1, u′(x) = 3x² : f = (1/3) u′ sin(u). Comme −cos est une primitive de sin, F(x) = −(1/3) cos(x³ + 1). Contrôle : F′(x) = −(1/3) × (−sin(x³ + 1)) × 3x² = f(x) ✓.
4. f(x) = cos(√x)/√x sur ]0, +∞[. On pose u(x) = √x, u′(x) = 1/(2√x) : f = 2u′ cos(u), donc F(x) = 2 sin(√x).
5. f(x) = x sin x sur ℝ. On dérive x cos x : (x cos x)′ = cos x − x sin x, donc x sin x = cos x − (x cos x)′ et F(x) = sin x − x cos x. Contrôle : F′(x) = cos x − (cos x − x sin x) = x sin x ✓.

:::

::: piege
**Erreur : F(2x) comme primitive de f(2x).** Avec f = cos et F = sin, on est tenté de dire que x ↦ sin(2x) est une primitive de x ↦ cos(2x). Mais (sin 2x)′ = 2cos(2x) : la dérivée de F(2x) est 2f(2x), pas f(2x). La bonne primitive de x ↦ f(2x) est x ↦ F(2x)/2. C'est le même facteur 1/ω que sur les lignes trigonométriques de la table.
:::

::: verifie À toi : une composée à ajuster
Déterminer une primitive de f(x) = x cos(x²) sur ℝ.

---

On pose u(x) = x², u′(x) = 2x. Il manque le facteur constant 2 : f = (1/2) u′ cos(u). Comme sin est une primitive de cos, F(x) = (1/2) sin(x²). Contrôle : F′(x) = (1/2) cos(x²) × 2x = x cos(x²) ✓.
:::

::: retenir
u′v + v′u a pour primitive uv ; (u′v − v′u)/v² a pour primitive u/v ; u′(w′∘u) a pour primitive w∘u. Pour composer, on ajuste les constantes et on contrôle par dérivation.
:::

## 📐 Réécrire avant de primitiver

Que faire de f(x) = (2x³ − 11x² + 20x − 10)/(x − 2)² ? Aucun motif n'apparaît. Même embarras pour sin²x ou sin³x, qui ne figurent dans aucune table.
Quand aucun motif ne se montre, quelle est la bonne attitude : forcer, ou transformer l'écriture de f ?

::: methode
**Transformer d'abord** : on ne force jamais un motif. On réécrit f jusqu'à obtenir des formes connues. Trois réécritures couvrent l'essentiel du programme : (1) décomposer une fraction rationnelle sous la forme ax + b + c/(x − 2)² ; (2) linéariser un carré ou un cube de sinus ou de cosinus avec cos 2x = 1 − 2 sin²x = 2 cos²x − 1, ou avec sin²x + cos²x = 1 ; (3) passer par tan, avec tan²x = (1 + tan²x) − 1.
:::

::: exemple Décomposer une fraction

1. On cherche a, b, c tels que f(x) = ax + b + c/(x − 2)² sur ]2, +∞[. En réduisant au même dénominateur, (ax + b)(x − 2)² + c = ax³ + (b − 4a)x² + (4a − 4b)x + (4b + c).
2. Par identification avec 2x³ − 11x² + 20x − 10 : a = 2, puis b − 4a = −11 donne b = −3 ; contrôle sur le terme en x : 4a − 4b = 8 + 12 = 20 ✓ ; enfin 4b + c = −10 donne c = 2.
3. Donc f(x) = 2x − 3 + 2/(x − 2)², et une primitive est F(x) = x² − 3x − 2/(x − 2). Contrôle : F′(x) = 2x − 3 + 2/(x − 2)² ✓.

:::

::: exemple Linéariser un carré, découper un cube

1. f(x) = sin²x sur ℝ. On part de sin²x = (1 − cos 2x)/2 : une primitive est F(x) = x/2 − (1/4) sin(2x). Contrôle : F′(x) = 1/2 − (1/2) cos(2x) = sin²x ✓.
2. g(x) = sin³x sur ℝ. On écrit sin³x = sin x(1 − cos²x) = sin x − sin x cos²x. Le premier terme donne −cos x. Pour le second, on pose u = cos x, u′ = −sin x : −sin x cos²x = u′u², de primitive u³/3. D'où G(x) = −cos x + (cos³x)/3. Contrôle : G′(x) = sin x − sin x cos²x = sin³x ✓.

:::

::: piege
**Erreur : primitiver une puissance de sin comme si l'intérieur était u′.** On écrit « sin³x/3 » comme primitive de sin²x, en oubliant que la ligne u′uⁿ exige la présence de u′. Or (sin³x/3)′ = sin²x cos x : le facteur cos x, absent de f, s'est glissé dans la dérivée. Il n'y a pas de u′ dans sin²x : on linéarise.
:::

::: verifie À toi : le cube de cosinus
Déterminer une primitive de f(x) = cos³x sur ℝ, sur le modèle de sin³x.

---

On découpe cos³x = cos x(1 − sin²x) = cos x − cos x sin²x. Le premier terme donne sin x. Pour le second, u = sin x, u′ = cos x : cos x sin²x = u′u², de primitive sin³x/3. D'où F(x) = sin x − (sin³x)/3. Contrôle : F′(x) = cos x − sin²x cos x = cos x(1 − sin²x) = cos³x ✓.
:::

::: retenir
Sans motif visible, on réécrit : décomposition en ax + b + c/(x − 2)², linéarisation de sin² et cos², découpage de sin³ et cos³, passage par tan.
:::

## 🧪 Applications : remonter d'un taux à une grandeur

Un taux instantané de variation est une dérivée. Si une réaction produit une substance à un certain rythme, ou si un mobile subit une accélération, retrouver la quantité produite ou la vitesse, c'est primitiver.
Où entre alors la condition initiale, et combien en faut-il quand on remonte deux fois ?

::: exemple Un taux de production, puis un mobile

1. Chimie. La quantité produite pendant les dix premières secondes est de 12 g ; ensuite, le taux instantané est Q′(t) = 40/t² + 200/t³ (en g/s) pour t ≥ 10. Une primitive de 40/t² est −40/t, une primitive de 200/t³ est 200 × t^(−2)/(−2) = −100/t². Donc Q(t) = −40/t − 100/t² + c, et Q(10) = −4 − 1 + c = 12 donne c = 17. D'où Q(t) = 17 − 40/t − 100/t². Contrôle : Q′(t) = 40/t² + 200/t³ ✓.
2. Limite. Q est croissante (Q′ > 0) et tend vers 17 quand t tend vers +∞ : la production plafonne à 17 g, elle n'atteint jamais 20 g.
3. Cinématique. Un mobile part de l'abscisse 1 avec une vitesse de 2 m/s ; son accélération est a(t) = 6t (en m/s²). Comme v′ = a, v(t) = 3t² + c, et v(0) = 2 donne v(t) = 3t² + 2. Comme x′ = v, x(t) = t³ + 2t + c′, et x(0) = 1 donne x(t) = t³ + 2t + 1.

:::

::: piege
**Erreur : une seule constante pour deux remontées.** Dans le cas du mobile, on oublie v(0) = 2 et l'on pose v(t) = 3t² : on obtient ensuite x(t) = t³ + 1, sans le terme 2t, et la position à t = 2 est fausse. Chaque primitivation introduit sa propre constante et réclame sa propre condition initiale : deux remontées, deux données.
:::

::: verifie À toi : deux remontées
Un mobile part de l'origine avec une vitesse nulle ; son accélération est a(t) = 6 − 6t (en m/s²). Déterminer sa position à l'instant t = 2.

---

Première remontée : v(t) = 6t − 3t² + c, et v(0) = 0 donne c = 0. Seconde remontée : x(t) = 3t² − t³ + c′, et x(0) = 0 donne c′ = 0. Donc x(2) = 12 − 8 = 4 m. Contrôle : x′(t) = 6t − 3t² = v(t) et v′(t) = 6 − 6t = a(t) ✓.
:::

::: verifie À toi : une accélération avec racine
Un mobile a une vitesse initiale de 3 m/s ; son accélération est a(t) = 1 − 1/(2(√(t + 1))³). Déterminer sa vitesse v(t).

---

On cherche v telle que v′ = a. Avec u(t) = √(t + 1), u′(t) = 1/(2√(t + 1)), et 1/(2(√(t + 1))³) = u′/u², de primitive −1/u. Donc v(t) = t + 1/√(t + 1) + c, et v(0) = 1 + c = 3 donne c = 2 : v(t) = t + 1/√(t + 1) + 2. Contrôle : v′(t) = 1 − 1/(2(t + 1)√(t + 1)) = a(t) ✓.
:::

::: retenir
Une grandeur est une primitive de son taux ; chaque remontée consomme une condition initiale (deux remontées, deux données).
:::

## 🔭 Étudier une primitive sans l'écrire

Soit f(x) = (1 + x²)/(1 + x + x²) sur [0, +∞[. Aucun motif, aucune réécriture : on ne sait pas écrire une primitive de f. Pourtant f est continue, donc elle en possède. Et le signe de f, joint aux théorèmes des chapitres 3 et 4, apprend beaucoup sur F.
Que peut-on affirmer d'une primitive F que l'on ne sait pas écrire ?

::: figure La courbe de f reste entre les droites y = 2/3 et y = 1 : elle part du point (0 ; 1), atteint son minimum 2/3 en x = 1, puis remonte vers 1
<svg viewBox="0 0 340 260">
<title>Courbe de f(x) = (1 + x²)/(1 + x + x²) sur [0 ; 6], comprise entre les droites y = 2/3 et y = 1</title>
<line x1="30" y1="215" x2="318" y2="215" stroke="#0f172a" stroke-width="1.6"/>
<line x1="50" y1="240" x2="50" y2="14" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="318,215 310,211 310,219" fill="#0f172a"/>
<polygon points="50,14 46,22 54,22" fill="#0f172a"/>
<line x1="50" y1="25" x2="300" y2="25" stroke="#b45309" stroke-width="1.6" stroke-dasharray="6 3"/>
<line x1="50" y1="88.33333333333334" x2="300" y2="88.33333333333334" stroke="#64748b" stroke-width="1.6" stroke-dasharray="6 3"/>
<line x1="90" y1="88.33333333333334" x2="90" y2="215" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="3 3"/>
<polyline points="50.0,25.0 52.0,34.0 54.0,42.1 56.0,49.3 58.0,55.6 60.0,61.2 62.0,66.0 64.0,70.2 66.0,73.7 68.0,76.7 70.0,79.3 72.0,81.4 74.0,83.2 76.0,84.6 78.0,85.7 80.0,86.6 82.0,87.3 84.0,87.8 86.0,88.1 88.0,88.3 90.0,88.3 92.0,88.3 94.0,88.1 96.0,87.9 98.0,87.6 100.0,87.3 102.0,86.9 104.0,86.5 106.0,86.0 108.0,85.5 110.0,85.0 112.0,84.5 114.0,83.9 116.0,83.4 118.0,82.8 120.0,82.2 122.0,81.6 124.0,81.0 126.0,80.5 128.0,79.9 130.0,79.3 132.0,78.7 134.0,78.1 136.0,77.6 138.0,77.0 140.0,76.4 142.0,75.9 144.0,75.3 146.0,74.8 148.0,74.2 150.0,73.7 152.0,73.2 154.0,72.7 156.0,72.2 158.0,71.7 160.0,71.2 162.0,70.7 164.0,70.2 166.0,69.8 168.0,69.3 170.0,68.8 172.0,68.4 174.0,68.0 176.0,67.5 178.0,67.1 180.0,66.7 182.0,66.3 184.0,65.9 186.0,65.5 188.0,65.1 190.0,64.7 192.0,64.3 194.0,64.0 196.0,63.6 198.0,63.2 200.0,62.9 202.0,62.5 204.0,62.2 206.0,61.8 208.0,61.5 210.0,61.2 212.0,60.9 214.0,60.6 216.0,60.2 218.0,59.9 220.0,59.6 222.0,59.3 224.0,59.1 226.0,58.8 228.0,58.5 230.0,58.2 232.0,57.9 234.0,57.7 236.0,57.4 238.0,57.1 240.0,56.9 242.0,56.6 244.0,56.4 246.0,56.1 248.0,55.9 250.0,55.6 252.0,55.4 254.0,55.2 256.0,54.9 258.0,54.7 260.0,54.5 262.0,54.3 264.0,54.1 266.0,53.9 268.0,53.6 270.0,53.4 272.0,53.2 274.0,53.0 276.0,52.8 278.0,52.6 280.0,52.4 282.0,52.3 284.0,52.1 286.0,51.9 288.0,51.7 290.0,51.5" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/>
<circle cx="50" cy="25" r="3.5" fill="#0f172a"/>
<circle cx="90" cy="88.33333333333334" r="3.5" fill="#0f172a"/>
<g font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">
<text x="44" y="29" text-anchor="end" fill="#b45309">1</text>
<text x="44" y="92.33333333333334" text-anchor="end" fill="#64748b">2/3</text>
<text x="90" y="231" text-anchor="middle" fill="#0f172a">1</text>
<text x="290" y="231" text-anchor="middle" fill="#0f172a">6</text>
<text x="178.0" y="19" fill="#b45309">y = 1</text>
<text x="178.0" y="104.33333333333334" fill="#64748b">y = 2/3</text>
<text x="234.0" y="41.660687593423035" fill="#0f6e56">C_f</text>
</g>
</svg>
:::

La figure montre f décroissant de 1 à 2/3 puis remontant vers 1 : la courbe reste entre les droites y = 2/3 et y = 1.

::: exemple Encadrer, borner, inverser

1. Variations de f : f′(x) = (x² − 1)/(1 + x + x²)² ; f décroît de f(0) = 1 à f(1) = 2/3 sur [0, 1], puis croît vers sa limite 1 en +∞. Donc 2/3 ≤ f(t) ≤ 1 pour tout t ≥ 0.
2. Soit F la primitive de f qui s'annule en 0. Comme F′ = f, on a 2/3 ≤ F′ ≤ 1 sur [0, x] ; l'inégalité des accroissements finis donne (2/3)x ≤ F(x) − F(0) ≤ x, soit (2/3)x ≤ F(x) ≤ x.
3. Limite : (2/3)x tend vers +∞, donc lim F = +∞ en +∞. De plus F′ = f > 0 : F est strictement croissante.
4. F est continue et strictement croissante de [0, +∞[ vers [0, +∞[ : c'est une bijection (chapitre 4). Pour chaque entier m ≥ 0, il existe donc un unique réel x_m = F⁻¹(m) tel que F(x_m) = m.
5. La réciproque F⁻¹ est croissante, donc (x_m) est croissante. Elle est de plus minorée par m : de (2/3)x_m ≤ m ≤ x_m, on tire m ≤ x_m ≤ (3/2)m, donc x_m tend vers +∞.

:::

::: exemple Une primitive définie par une composée

Soit G la primitive de 1/(1 + x²) sur ℝ qui s'annule en 0, et u(t) = G(tan t) sur ]−π/2, π/2[. Alors u′(t) = G′(tan t) × (1 + tan²t) = (1 + tan²t)/(1 + tan²t) = 1, donc u(t) = t + c, et u(0) = G(0) = 0 donne u(t) = t. Comme 1 = tan(π/4), G(1) = u(π/4) = π/4.

:::

::: piege
**Erreur : conclure que F tend vers 1 parce que f tend vers 1.** Ici f(t) tend vers 1 en +∞, et l'on pourrait écrire « lim F = 1 ». C'est faux : F′ proche de 1 signifie que F grandit à peu près comme x, pas que F se stabilise. L'encadrement (2/3)x ≤ F(x) montre au contraire que F tend vers +∞. Une primitive ne se stabilise que si f devient nulle assez vite, ce qui n'est pas le cas ici.
:::

::: verifie À toi : l'étape de la bijection
Dans l'exemple, justifier que F réalise une bijection de [0, +∞[ sur [0, +∞[.

---

F est dérivable donc continue, et F′ = f > 0 sur [0, +∞[ : F est strictement croissante. Elle part de F(0) = 0 et, d'après (2/3)x ≤ F(x), tend vers +∞ en +∞. Une fonction continue et strictement croissante prend toutes les valeurs entre sa valeur en 0 et sa limite : F([0, +∞[) = [0, +∞[, et F est bijective de [0, +∞[ sur [0, +∞[.
:::

::: retenir
Sans écrire F, on lit f : son signe donne les variations de F, ses bornes m ≤ f ≤ M donnent mx ≤ F(x) ≤ Mx, et F′ > 0 donne une bijection dont la réciproque définit des suites comme x_m.
:::

> 🏆 Sixième porte franchie, héros. Tu sais reconnaître une primitive, prouver son existence par la continuité, décrire toute la famille à une constante près, en isoler une par une condition initiale, et calculer : fonctions usuelles, linéarité, formes composées, réécritures. Au chapitre suivant, la primitive devient une aire sous la courbe : la machinerie prend le nom d'intégrale.
