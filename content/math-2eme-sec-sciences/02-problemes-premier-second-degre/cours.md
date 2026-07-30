# ⚔️ Problèmes du premier degré et problèmes du second degré

> 💡 «Tout problème qui résiste finit par céder : traduis-le en équation, et l'équation te livrera sa réponse.»

Te voilà devant l'arme la plus polyvalente du programme, héros. Un énoncé en français — une aire, une vitesse, un terrain, une chute de pierre — devient une **équation**, et l'équation se résout par une méthode sûre. Tu connais déjà le premier degré ; tu vas maintenant maîtriser le **second degré**, son **discriminant**, le **signe du trinôme** et les inéquations qui en découlent. C'est l'outil que tu utiliseras toute l'année, et bien au-delà.

## 🧭 Mettre un problème en équation

La méthode est toujours la même, en quatre temps :

1. **Choisir l'inconnue** et dire précisément ce qu'elle représente (« soit x la longueur du côté, en cm »).
2. **Traduire** chaque donnée de l'énoncé par une **égalité** (équation) ou une **inégalité** (inéquation).
3. **Résoudre** l'équation ou l'inéquation obtenue.
4. **Vérifier et interpréter** : on **rejette** les solutions qui n'ont pas de sens dans le problème (une longueur négative, un effectif non entier) ou qui sortent de l'ensemble de résolution.

_Exemple détaillé_ : « Je pense à un nombre, je lui retranche 5, je multiplie le résultat par 2, j'ajoute 6, je divise par 5 et j'obtiens 2. » Soit x ce nombre : (2(x − 5) + 6)/5 = 2, donc 2(x − 5) + 6 = 10, puis 2x − 10 + 6 = 10, soit 2x = 14 et **x = 7**. Vérification : 7 − 5 = 2 ; 2 × 2 = 4 ; 4 + 6 = 10 ; 10/5 = 2 ✓.

> ⚠️ Dans une **inéquation**, multiplier ou diviser les deux membres par un nombre **négatif change le sens** de l'inégalité. Ainsi −2x + 1 > 7 donne −2x > 6, puis **x < −3** (et non x > −3).

## 🧮 Premier degré : valeur absolue, quotients et radicaux

**Valeur absolue.** |x − a| se lit « distance entre x et a ». Pour k > 0 :

$$ |X| = k ⇔ X = k ou X = −k $$

$$ |X| ≤ k ⇔ −k ≤ X ≤ k $$

$$ |X| ≥ k ⇔ X ≤ −k ou X ≥ k $$

Si k = 0, |X| = 0 équivaut à X = 0 ; si k < 0, l'équation |X| = k n'a **aucune** solution. Enfin |A| = |B| équivaut à A = B ou A = −B.

_Exemple détaillé_ : |2x + 3| = 5 donne 2x + 3 = 5 (soit x = 1) ou 2x + 3 = −5 (soit x = −4). Les solutions sont **−4 et 1**.

::: figure Les solutions de |x − 3| = 2 sont les points situés à la distance 2 du point d'abscisse 3 : x = 1 et x = 5
<svg viewBox="0 0 340 100">
<line x1="20" y1="55" x2="312" y2="55" fill="none" stroke="#0f172a" stroke-width="1.8"/>
<path d="M318 55 l-9 -4.5 l0 9 z" fill="#0f172a"/>
<g stroke="#0f172a" stroke-width="1.5">
<line x1="40" y1="50" x2="40" y2="60"/><line x1="80" y1="50" x2="80" y2="60"/><line x1="120" y1="50" x2="120" y2="60"/><line x1="160" y1="50" x2="160" y2="60"/><line x1="200" y1="50" x2="200" y2="60"/><line x1="240" y1="50" x2="240" y2="60"/><line x1="280" y1="50" x2="280" y2="60"/>
</g>
<path d="M80 45 Q 120 24 160 45" fill="none" stroke="#0f6e56" stroke-width="1.8"/>
<path d="M160 45 Q 200 24 240 45" fill="none" stroke="#0f6e56" stroke-width="1.8"/>
<g fill="#0f172a"><circle cx="160" cy="55" r="4"/></g>
<g fill="#b91c1c"><circle cx="80" cy="55" r="4.5"/><circle cx="240" cy="55" r="4.5"/></g>
<g font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">
<text x="40" y="78" text-anchor="middle" fill="#0f172a">0</text>
<text x="80" y="78" text-anchor="middle" fill="#b91c1c">1</text>
<text x="120" y="78" text-anchor="middle" fill="#0f172a">2</text>
<text x="160" y="78" text-anchor="middle" fill="#0f172a">3</text>
<text x="200" y="78" text-anchor="middle" fill="#0f172a">4</text>
<text x="240" y="78" text-anchor="middle" fill="#b91c1c">5</text>
<text x="280" y="78" text-anchor="middle" fill="#0f172a">6</text>
<text x="120" y="29" text-anchor="middle" fill="#0f6e56">2</text>
<text x="200" y="29" text-anchor="middle" fill="#0f6e56">2</text>
</g>
</svg>
:::

**Équations à quotients.** On détermine d'abord l'**ensemble de résolution** en écartant les valeurs qui annulent un dénominateur, puis on résout, puis on garde les solutions qui appartiennent à cet ensemble.

_Exemple détaillé_ : (x − 1)/(x + 3) = 2 se résout sur ℝ \ {−3}. On obtient x − 1 = 2(x + 3), soit x − 1 = 2x + 6, donc −x = 7 et **x = −7**, qui est bien différent de −3 ✓.

**Équations avec radicaux.** L'ensemble de résolution impose que chaque radicande soit **positif ou nul**. Pour k ≥ 0, √A = k équivaut à A = k² ; et √A = √B équivaut à A = B (sur le domaine). Pour une inéquation : √A ≥ √B équivaut à A ≥ B sur le domaine.

_Exemple détaillé_ : √(3 − 2x) = 5 se résout pour 3 − 2x ≥ 0, c'est-à-dire x ≤ 3/2. On élève au carré : 3 − 2x = 25, donc −2x = 22 et **x = −11**, qui vérifie bien x ≤ 3/2 ✓.

## ⚡ L'équation du second degré : forme canonique et discriminant

> **Définition.** Soient a, b et c trois réels avec a ≠ 0. L'équation ax² + bx + c = 0 est dite **équation du second degré** d'inconnue x.

En complétant le carré, on obtient la **forme canonique** du trinôme :

$$ ax² + bx + c = a[(x + b/(2a))² − (b² − 4ac)/(4a²)] $$

Le réel **Δ = b² − 4ac** s'appelle le **discriminant** de l'équation. Tout dépend de son signe :

| signe de Δ | nombre de racines | racines                                            |
| ---------- | ----------------- | -------------------------------------------------- |
| Δ < 0      | aucune racine     | —                                                  |
| Δ = 0      | une racine double | x₀ = −b/(2a)                                       |
| Δ > 0      | deux racines      | x₁ = (−b − √Δ)/(2a) **et** x₂ = (−b + √Δ)/(2a)     |

Toute solution de ax² + bx + c = 0 est aussi appelée **racine** de cette équation.

_Exemple détaillé_ : x² − 5x + 6 = 0 donne Δ = (−5)² − 4 × 1 × 6 = 25 − 24 = 1 > 0, donc √Δ = 1 et les racines sont (5 − 1)/2 = **2** et (5 + 1)/2 = **3** ✓.

**Discriminant réduit.** Quand b est pair, on pose b = 2b' et on gagne du temps avec Δ' = b'² − ac (on a Δ = 4Δ') : si Δ' = 0 la racine double est x₀ = −b'/a, et si Δ' > 0 les racines sont (−b' − √Δ')/a et (−b' + √Δ')/a.

_Exemple détaillé_ : 5x² − 16x + 3 = 0 avec b' = −8 : Δ' = 64 − 5 × 3 = 49, √Δ' = 7, donc les racines sont (8 − 7)/5 = **1/5** et (8 + 7)/5 = **3** ✓.

> 🗡️ La forme canonique n'est pas qu'un calcul : elle donne aussi le **minimum** (si a > 0) ou le **maximum** (si a < 0) du trinôme, atteint en x = −b/(2a). C'est elle qui résout les problèmes du type « hauteur maximale » ou « aire maximale ».

## 🔑 Somme et produit des racines

Lorsque l'équation admet deux racines x₁ et x₂ (Δ ≥ 0) :

$$ S = x₁ + x₂ = −b/a $$

$$ P = x₁ · x₂ = c/a $$

Deux cas particuliers font gagner un temps précieux :

- si **a + b + c = 0**, alors **1** est racine et l'autre racine vaut c/a ;
- si **a − b + c = 0**, alors **−1** est racine et l'autre racine vaut −c/a.

Réciproquement, deux nombres de somme S et de produit P sont les racines de l'équation x² − Sx + P = 0.

_Exemple détaillé_ : deux nombres ont pour somme 11 et pour produit 30 ; ils sont racines de x² − 11x + 30 = 0. Δ = 121 − 120 = 1, donc les nombres sont (11 − 1)/2 = **5** et (11 + 1)/2 = **6** ✓ (5 + 6 = 11 et 5 × 6 = 30).

## 📊 Signe du trinôme et inéquations du second degré

Soit f(x) = ax² + bx + c avec a ≠ 0 et Δ = b² − 4ac. La **factorisation** et le **signe** se lisent dans le même tableau :

| signe de Δ | factorisation      | signe de f(x)                                                                  |
| ---------- | ------------------ | ------------------------------------------------------------------------------ |
| Δ < 0      | impossible         | f(x) est du **signe de a** pour tout réel x                                    |
| Δ = 0      | a(x − x₀)²         | f(x) est du **signe de a** pour tout x ≠ x₀, et f(x₀) = 0                      |
| Δ > 0      | a(x − x₁)(x − x₂)  | signe de **a à l'extérieur** des racines, signe de **−a entre** les racines    |

::: figure Tableau de signes de f(x) = x² − 5x + 6 : ici a = 1 > 0, donc f est positif à l'extérieur des racines 2 et 3, et négatif entre elles
<svg viewBox="0 0 340 110">
<rect x="10" y="10" width="320" height="90" fill="none" stroke="#0f172a" stroke-width="1.8"/>
<line x1="10" y1="45" x2="330" y2="45" fill="none" stroke="#0f172a" stroke-width="1.8"/>
<line x1="70" y1="10" x2="70" y2="100" fill="none" stroke="#0f172a" stroke-width="1.8"/>
<line x1="160" y1="45" x2="160" y2="100" fill="none" stroke="#0f172a" stroke-width="1.2"/>
<line x1="235" y1="45" x2="235" y2="100" fill="none" stroke="#0f172a" stroke-width="1.2"/>
<g font-size="15" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">
<text x="40" y="33" text-anchor="middle">x</text>
<text x="95" y="33" text-anchor="middle">−∞</text>
<text x="160" y="33" text-anchor="middle">2</text>
<text x="235" y="33" text-anchor="middle">3</text>
<text x="300" y="33" text-anchor="middle">+∞</text>
<text x="40" y="80" text-anchor="middle">f(x)</text>
<text x="160" y="80" text-anchor="middle">0</text>
<text x="235" y="80" text-anchor="middle">0</text>
</g>
<g font-size="18" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">
<text x="115" y="81" text-anchor="middle" fill="#0f6e56">+</text>
<text x="198" y="81" text-anchor="middle" fill="#b91c1c">−</text>
<text x="285" y="81" text-anchor="middle" fill="#0f6e56">+</text>
</g>
</svg>
:::

Résoudre une **inéquation du second degré**, c'est donc lire ce tableau : on cherche les x où le signe voulu apparaît, en incluant les racines si l'inégalité est **large** (≤, ≥) et en les excluant si elle est **stricte** (<, >).

_Exemple détaillé_ : −x² + 4x − 3 ≥ 0. Ici Δ = 16 − 12 = 4 et les racines sont 1 et 3. Comme a = −1 < 0, f est **négatif à l'extérieur** et **positif entre** les racines : l'ensemble des solutions est **[1 ; 3]** (bornes incluses car l'inégalité est large) ✓.

**Produits et quotients.** On étudie le signe de **chaque facteur** dans un même tableau, puis on multiplie les signes ligne par ligne. Pour un quotient, on ajoute les **valeurs interdites** (celles qui annulent le dénominateur), toujours **exclues** de l'ensemble des solutions.

_Exemple détaillé_ : (x − 1)(−2x + 3) ≥ 0. Le facteur x − 1 est négatif avant 1, positif après ; le facteur −2x + 3 est positif avant 3/2, négatif après. Le produit n'est positif que sur **[1 ; 3/2]** ✓.

> ⚠️ Le piège le plus fréquent : oublier le **signe de a**. Avec a < 0, le trinôme est positif **entre** les racines, pas à l'extérieur. Vérifie toujours en testant une valeur simple (par exemple x = 0) dans l'expression de départ.

## 🔄 Les équations qui se ramènent au second degré

- **Bicarrée** ax⁴ + bx² + c = 0 : on pose X = x², on résout aX² + bX + c = 0, puis on revient à x en ne gardant que les X ≥ 0 (chaque X > 0 donne deux valeurs de x, opposées).
- **Fractionnaire** : ensemble de résolution d'abord, puis on multiplie par le dénominateur pour obtenir une équation du second degré, puis on écarte les valeurs interdites.
- **Irrationnelle** : √A = B équivaut à « A = B² **et** B ≥ 0 ». Élever au carré peut créer de fausses solutions : la **vérification est obligatoire**.

_Exemple détaillé_ (bicarrée) : x⁴ − 5x² + 4 = 0. Avec X = x² : X² − 5X + 4 = 0, Δ = 25 − 16 = 9, donc X = 1 ou X = 4. On revient à x : x² = 1 donne x = −1 ou x = 1, et x² = 4 donne x = −2 ou x = 2. Les solutions sont **−2, −1, 1 et 2** ✓.

_Exemple détaillé_ (fractionnaire) : x + 8/x = 6. **L'ensemble de résolution d'abord** : le dénominateur x s'annule en 0, donc on résout sur ℝ \ {0}. On **multiplie les deux membres par x** (ce qui revient à tout mettre au même dénominateur x, puis à annuler le numérateur) : x² + 8 = 6x, d'où l'équation du second degré **x² − 6x + 8 = 0**. Son discriminant vaut Δ = (−6)² − 4 × 1 × 8 = 36 − 32 = 4, donc √Δ = 2 et les racines sont (6 − 2)/2 = **2** et (6 + 2)/2 = **4**. **Retour à l'ensemble de résolution** : 2 ≠ 0 et 4 ≠ 0, les deux valeurs sont donc acceptées ✓ (vérification : 2 + 8/2 = 2 + 4 = 6, et 4 + 8/4 = 4 + 2 = 6). Si l'une des racines trouvées avait été 0, il aurait fallu la **rejeter** : une valeur interdite n'est jamais solution de l'équation de départ.

_Exemple détaillé_ (irrationnelle) : √(x + 7) = x + 1. Il faut x + 7 ≥ 0 et x + 1 ≥ 0, donc x ≥ −1. En élevant au carré : x + 7 = x² + 2x + 1, soit x² + x − 6 = 0, Δ = 1 + 24 = 25, d'où x = 2 ou x = −3. On rejette −3 (qui ne vérifie pas x ≥ −1) : la seule solution est **x = 2** ✓ (√9 = 3 = 2 + 1).

> 🏆 Chapitre franchi, héros : tu sais traduire un problème, discuter un discriminant, factoriser un trinôme et lire son signe. Ces réflexes te serviront dès le chapitre suivant sur les polynômes, puis dans toute l'analyse de l'année.
