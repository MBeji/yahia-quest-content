# ⚔️ Suites arithmétiques — avancer toujours du même pas

> 💡 «Un escalier régulier ne se décrit pas marche par marche : il suffit de dire d'où l'on part et de combien on monte à chaque fois. C'est tout le chapitre — et c'est ce qui permet d'atteindre le millième terme sans écrire les neuf cent quatre-vingt-dix-neuf précédents.»

Tu viens de passer trois chapitres à faire bouger des points. On change de terrain : ici, ce sont des **nombres** qui se succèdent, chacun à sa place dans une file. Le jeu consiste à trouver la loi qui les fabrique, puis à s'en servir pour sauter directement là où l'on veut aller.

## 🔢 Une suite : à chaque rang, son nombre

Les Pythagoriciens empilaient des cailloux en triangle. Un caillou, puis une rangée de deux, puis une rangée de trois, et ainsi de suite. À chaque figure correspond un nombre de cailloux, et à chaque **rang** correspond une seule valeur.

::: figure Les nombres triangulaires : la figure de rang n s'obtient en ajoutant à la précédente une rangée d'un point de plus, ce qui donne T₁ = 1, T₂ = 3, T₃ = 6 puis T₄ = 10 — à chaque rang, un nombre et un seul
<svg viewBox="0 0 340 120">
<g fill="#0f6e56">
<circle cx="45" cy="30" r="5"/>
<circle cx="120" cy="30" r="5"/><circle cx="112.5" cy="46" r="5"/><circle cx="127.5" cy="46" r="5"/>
<circle cx="205" cy="30" r="5"/><circle cx="197.5" cy="46" r="5"/><circle cx="212.5" cy="46" r="5"/><circle cx="190" cy="62" r="5"/><circle cx="205" cy="62" r="5"/><circle cx="220" cy="62" r="5"/>
<circle cx="300" cy="30" r="5"/><circle cx="292.5" cy="46" r="5"/><circle cx="307.5" cy="46" r="5"/><circle cx="285" cy="62" r="5"/><circle cx="300" cy="62" r="5"/><circle cx="315" cy="62" r="5"/><circle cx="277.5" cy="78" r="5"/><circle cx="292.5" cy="78" r="5"/><circle cx="307.5" cy="78" r="5"/><circle cx="322.5" cy="78" r="5"/>
</g>
<g font-size="14" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">
<text x="45" y="104">T₁ = 1</text>
<text x="120" y="104">T₂ = 3</text>
<text x="205" y="104">T₃ = 6</text>
<text x="300" y="104">T₄ = 10</text>
</g>
</svg>
:::

Cette correspondance «un rang, un nombre» porte un nom officiel.

> **Définition (suite).** Soit n₀ un entier naturel. Lorsqu'à tout entier naturel n supérieur ou égal à n₀ on associe un réel unique U(n), on dit que l'on a défini une **suite de nombres réels**. Le réel U(n) s'appelle le **terme général** de la suite et se note **Uₙ**. La suite se note **(Uₙ)ₙ≥ₙ₀** ou **(Uₙ)**.

L'entier n est l'**indice** (ou le rang) du terme ; Uₙ est le **terme** lui-même. Ce sont deux objets différents, et les confondre est la première source d'erreurs du chapitre.

_Exemple détaillé_ : la suite définie par Uₙ = (3n + 1)/4 pour tout n ∈ ℕ donne U₀ = 1/4, puis U₁ = 4/4 = 1, puis U₅ = 16/4 = 4. Et sans écrire les cent premiers termes, U₁₀₀ = 301/4 = 75,25.

> ⚠️ Uₙ n'est pas «U multiplié par n». L'indice n désigne la **place** du terme dans la file, exactement comme le numéro d'un dossard désigne un coureur sans dire à quelle vitesse il court.

## 🎛️ Deux façons de présenter une suite

Une même suite s'écrit de deux manières, et savoir passer de l'une à l'autre est une compétence à part entière.

> **Retenir (modes de présentation).** Une suite peut être définie **par son terme général** — une formule qui donne Uₙ directement à partir de n — ou **par son premier terme et une relation de récurrence** — une formule qui donne chaque terme à partir du précédent.

| présentation                  | ce qu'on écrit                    | comment on obtient U₃                    |
| ----------------------------- | --------------------------------- | ---------------------------------------- |
| terme général                 | Uₙ = 4n + 1                       | on remplace n par 3 : U₃ = 13            |
| premier terme et récurrence   | U₀ = 1 et Uₙ₊₁ = Uₙ + 4           | on monte marche par marche : 1, 5, 9, 13 |

_Exemple détaillé_ : la suite définie par W₀ = 1 et Wₙ₊₁ = √(1 + Wₙ) donne W₁ = √2 ≈ 1,414 puis W₂ = √(1 + √2) ≈ 1,554. Ici aucune formule directe simple n'existe : la récurrence est le seul chemin.

> ⚠️ Avec une relation de récurrence, **on ne saute pas**. Pour obtenir U₅ il faut avoir calculé U₁, U₂, U₃ et U₄ auparavant. C'est précisément ce défaut que la suite arithmétique va faire disparaître.

## ➕ La suite arithmétique : toujours le même pas

Range les entiers qui laissent le reste 3 dans la division par 5, du plus petit au plus grand : 3, 8, 13, 18, 23… D'un terme au suivant, on ajoute toujours 5. Le pas ne change jamais.

> **Définition (suite arithmétique).** On dit qu'une suite (Uₙ) est **arithmétique** s'il existe un réel r tel que, pour tout entier naturel n, on a **Uₙ₊₁ = Uₙ + r**. Le nombre réel r est appelé **raison** de cette suite.

> **Remarque (vocabulaire officiel).** Si a, b, c, d… sont des termes consécutifs d'une suite arithmétique, on dit qu'ils sont **en progression arithmétique**.

::: figure L'escalier de la raison : d'un rang au suivant, le point monte toujours de la même hauteur, et cette hauteur est la raison r — c'est exactement ce qu'affirme l'égalité Uₙ₊₁ = Uₙ + r
<svg viewBox="0 0 340 220">
<path d="M40 190 L322 190 M40 196 L40 28" fill="none" stroke="#0f172a" stroke-width="2"/>
<polygon points="316,186 328,190 316,194" fill="#0f172a"/>
<polygon points="36,34 40,22 44,34" fill="#0f172a"/>
<g fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-dasharray="5 4">
<path d="M55 170 L110 170 M110 140 L165 140 M165 110 L220 110 M220 80 L275 80"/>
</g>
<g fill="none" stroke="#0f6e56" stroke-width="2.2">
<path d="M110 170 L110 143 M165 140 L165 113 M220 110 L220 83 M275 80 L275 53"/>
</g>
<g fill="#0f6e56">
<polygon points="106,149 110,138 114,149"/><polygon points="161,119 165,108 169,119"/><polygon points="216,89 220,78 224,89"/><polygon points="271,59 275,48 279,59"/>
<circle cx="55" cy="170" r="4.5"/><circle cx="110" cy="140" r="4.5"/><circle cx="165" cy="110" r="4.5"/><circle cx="220" cy="80" r="4.5"/><circle cx="275" cy="50" r="4.5"/>
</g>
<g font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">
<g text-anchor="middle" fill="#0f172a">
<text x="55" y="160">U₀</text><text x="110" y="130">U₁</text><text x="165" y="100">U₂</text><text x="220" y="70">U₃</text><text x="275" y="40">U₄</text>
<text x="55" y="207">0</text><text x="110" y="207">1</text><text x="165" y="207">2</text><text x="220" y="207">3</text><text x="275" y="207">4</text>
<text x="316" y="207">n</text>
</g>
<g fill="#0f6e56">
<text x="118" y="158">+ r</text><text x="173" y="128">+ r</text><text x="228" y="98">+ r</text><text x="283" y="68">+ r</text>
</g>
</g>
</svg>
:::

Pour **prouver** qu'une suite est arithmétique, on ne regarde pas quelques termes : on calcule la différence Uₙ₊₁ − Uₙ et on vérifie qu'elle ne dépend pas de n.

_Exemple détaillé_ : soit Uₙ = n/5 − 4. Alors Uₙ₊₁ − Uₙ = (n + 1)/5 − 4 − (n/5 − 4) = 1/5. La différence vaut 1/5 quel que soit n : la suite est arithmétique de raison **1/5**.

_Exemple détaillé (le contre-exemple)_ : soit Uₙ = n². Alors Uₙ₊₁ − Uₙ = (n + 1)² − n² = 2n + 1. Cette différence **dépend de n** : elle vaut 1, puis 3, puis 5. La suite des carrés n'est donc **pas** arithmétique.

> 🗡️ Une différence constante suffit, mais il faut qu'elle le soit **pour tout n**. Vérifier sur trois termes ne prouve rien : c'est le calcul littéral de Uₙ₊₁ − Uₙ qui fait la démonstration.

## 🎯 Le terme général : sauter directement au rang n

Partons de U₀ et ajoutons la raison, encore et encore. Pour arriver au rang n, combien de fois faut-il ajouter r ? Une fois pour passer de U₀ à U₁, une deuxième pour aller à U₂… donc exactement **n fois**.

> **Retenir (terme général).** Soit (Uₙ) une suite arithmétique de premier terme U₀ et de raison r. On a, pour tout n ∈ ℕ :
>
> $$ Uₙ = U₀ + nr $$
>
> et, plus généralement, pour tous entiers naturels n et p :
>
> $$ Uₙ = Uₚ + (n − p)r $$
>
> en particulier, lorsque la suite commence au rang 1 : **Uₙ = U₁ + (n − 1)r**.

> ⚠️ Le piège du chapitre tient en un mot : **c'est le nombre de PAS qui multiplie r, pas le nombre de TERMES.** De U₀ à U₇ il y a huit termes mais **sept** pas, donc U₇ = U₀ + 7r. Écrire U₇ = U₀ + 8r, ou partir de U₁ en gardant nr, décale tout le calcul d'une raison.

_Exemple détaillé_ : une suite arithmétique vérifie U₀ = −4 et r = 3/2. Son terme général est Uₙ = −4 + 3n/2, d'où U₆ = −4 + 9 = 5.

_Exemple détaillé (avec deux termes quelconques)_ : une suite arithmétique de raison 3/4 vérifie U₁₀₀ = 74. Alors U₂₄₈ = U₁₀₀ + (248 − 100) × 3/4 = 74 + 148 × 3/4 = 74 + 111 = **185**.

La même formule, lue à l'envers, donne la raison quand on connaît deux termes :

$$ r = (Uₙ − Uₚ)/(n − p) $$

_Exemple détaillé_ : si U₀ = 8 et U₇ = −13, alors r = (−13 − 8)/(7 − 0) = −21/7 = **−3**. Vérification : U₇ = 8 + 7 × (−3) = 8 − 21 = −13 ✓.

## 📈 Représentation graphique : des points alignés

Plaçons dans un repère les points Aₙ de coordonnées (n ; Uₙ). Comme Uₙ = U₀ + nr, l'ordonnée est une fonction affine de l'abscisse : les points se posent tous sur une même droite.

> **Retenir (représentation graphique).** Les points Aₙ(n ; Uₙ) d'une suite arithmétique appartiennent à la droite de **pente r** et d'**ordonnée à l'origine U₀**, c'est-à-dire à la droite d'équation y = rx + U₀.

::: figure Les cinq points Aₙ(n ; Uₙ) de la suite de premier terme 1 et de raison 2 sont alignés : d'un point au suivant on avance de 1 en abscisse et on monte de r en ordonnée, ce qui est exactement la pente de la droite
<svg viewBox="0 0 340 240">
<g fill="none" stroke="#94a3b8" stroke-width="1" stroke-dasharray="4 4">
<path d="M45 182 L290 182 M45 110 L290 110 M45 38 L290 38"/>
<path d="M105 30 L105 205 M160 30 L160 205 M215 30 L215 205 M270 30 L270 205"/>
</g>
<path d="M28 200 L325 200 M50 215 L50 20" fill="none" stroke="#0f172a" stroke-width="2"/>
<polygon points="319,196 331,200 319,204" fill="#0f172a"/>
<polygon points="46,26 50,14 54,26" fill="#0f172a"/>
<path d="M35 191.8 L292 23.6" fill="none" stroke="#0f6e56" stroke-width="2"/>
<g fill="none" stroke="#0f172a" stroke-width="1.6" stroke-dasharray="4 3">
<path d="M105 146 L160 146 L160 110"/>
</g>
<g fill="#0f6e56">
<circle cx="50" cy="182" r="4.5"/><circle cx="105" cy="146" r="4.5"/><circle cx="160" cy="110" r="4.5"/><circle cx="215" cy="74" r="4.5"/><circle cx="270" cy="38" r="4.5"/>
</g>
<g font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">
<g text-anchor="middle" fill="#0f6e56">
<text x="66" y="178">A₀</text><text x="121" y="142">A₁</text><text x="176" y="106">A₂</text><text x="231" y="70">A₃</text><text x="286" y="34">A₄</text>
</g>
<g text-anchor="middle" fill="#0f172a">
<text x="105" y="216">1</text><text x="160" y="216">2</text><text x="215" y="216">3</text><text x="270" y="216">4</text>
<text x="42" y="216">O</text><text x="330" y="192">n</text><text x="68" y="26">Uₙ</text>
<text x="132" y="160">1</text><text x="174" y="130">r</text>
</g>
<g text-anchor="end" fill="#0f172a">
<text x="44" y="187">1</text><text x="44" y="115">5</text><text x="44" y="43">9</text>
</g>
</g>
</svg>
:::

Cette lecture fonctionne dans les deux sens, et c'est le second sens qui rapporte le plus en exercice.

_Exemple détaillé_ : les points Aₙ(n ; Uₙ) sont tous sur la droite d'équation y = −2x + 9. On lit alors directement r = −2 et U₀ = 9, donc Uₙ = 9 − 2n, et par exemple U₆ = 9 − 12 = **−3**.

> 🗡️ Une raison positive fait monter la droite, une raison négative la fait descendre, et une raison nulle la rend horizontale — tous les termes sont alors égaux à U₀.

## 🧮 La somme de termes consécutifs

On raconte que le jeune Gauss, à qui l'on demandait la somme 1 + 2 + … + 100, la trouva en quelques secondes. Son idée : écrire la somme une seconde fois **à l'envers**, puis additionner colonne par colonne. Chaque colonne donne le même total.

::: figure La somme 1 + 2 + … + 6 empilée sur elle-même retournée : chaque colonne totalise 7, et les six colonnes forment un rectangle — d'où 2S = 6 × 7 et S = 21
<svg viewBox="0 0 300 200">
<g stroke="#0f172a" stroke-width="1.6">
<rect x="50" y="165" width="30" height="15" fill="#0f6e56" fill-opacity="0.35"/><rect x="50" y="75" width="30" height="90" fill="#94a3b8" fill-opacity="0.25"/>
<rect x="86" y="150" width="30" height="30" fill="#0f6e56" fill-opacity="0.35"/><rect x="86" y="75" width="30" height="75" fill="#94a3b8" fill-opacity="0.25"/>
<rect x="122" y="135" width="30" height="45" fill="#0f6e56" fill-opacity="0.35"/><rect x="122" y="75" width="30" height="60" fill="#94a3b8" fill-opacity="0.25"/>
<rect x="158" y="120" width="30" height="60" fill="#0f6e56" fill-opacity="0.35"/><rect x="158" y="75" width="30" height="45" fill="#94a3b8" fill-opacity="0.25"/>
<rect x="194" y="105" width="30" height="75" fill="#0f6e56" fill-opacity="0.35"/><rect x="194" y="75" width="30" height="30" fill="#94a3b8" fill-opacity="0.25"/>
<rect x="230" y="90" width="30" height="90" fill="#0f6e56" fill-opacity="0.35"/><rect x="230" y="75" width="30" height="15" fill="#94a3b8" fill-opacity="0.25"/>
</g>
<path d="M272 75 L272 180" fill="none" stroke="#0f172a" stroke-width="1.4"/>
<g fill="#0f172a"><polygon points="268,84 272,73 276,84"/><polygon points="268,171 272,182 276,171"/></g>
<g font-size="11" font-weight="700" text-anchor="middle" fill="#0f172a">
<text x="65" y="177">1</text><text x="101" y="169">2</text><text x="137" y="162">3</text><text x="173" y="154">4</text><text x="209" y="147">5</text><text x="245" y="139">6</text>
<text x="65" y="124">6</text><text x="101" y="117">5</text><text x="137" y="109">4</text><text x="173" y="102">3</text><text x="209" y="94">2</text><text x="245" y="87">1</text>
</g>
<g font-size="14" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">
<text x="155" y="50">2S = 6 × 7 = 42</text>
<text x="284" y="132">7</text>
</g>
</svg>
:::

> **Retenir (somme de n termes consécutifs).** Soit S une somme de n termes consécutifs d'une suite arithmétique, de premier terme a et de dernier terme b. Alors :
>
> $$ S = n × (a + b)/2 $$
>
> autrement dit S = nombre de termes × (premier + dernier)/2. Cas particulier fondamental :
>
> $$ 1 + 2 + … + n = n(n + 1)/2 $$

Reste à compter les termes, et c'est là que tout se joue.

> ⚠️ **Le nombre de termes d'une somme n'est pas le dernier indice.** De U₀ à Uₙ il y a **n + 1** termes ; de Uₚ à Uₙ il y en a **n − p + 1**. Oublier ce «+ 1» est l'erreur la plus fréquente du chapitre, et elle survit à tout le reste du calcul.

_Exemple détaillé_ : la somme U₄₅ + U₄₆ + … + U₃₈₁ compte 381 − 45 + 1 = **337** termes.

_Exemple détaillé (calcul complet)_ : soit (Uₙ) arithmétique avec U₀ = 3 et r = 2, et S = U₅ + U₆ + … + U₅₀. Le premier terme de la somme est U₅ = 3 + 10 = 13, le dernier est U₅₀ = 3 + 100 = 103, et il y a 50 − 5 + 1 = 46 termes. Donc S = 46 × (13 + 103)/2 = 46 × 58 = **2668**.

## ⚖️ La moyenne arithmétique

Trois termes consécutifs sont séparés par le même écart. Le terme du milieu est donc à égale distance de ses deux voisins : c'est leur moyenne.

> **Retenir (moyenne arithmétique).** Si a, b et c sont trois termes consécutifs d'une suite arithmétique, alors **b = (a + c)/2**. On dit que b est la **moyenne arithmétique** de a et c.

::: figure Le terme du milieu est à la même distance de ses deux voisins : les deux sauts valent r, donc b tombe exactement au milieu de a et c
<svg viewBox="0 0 300 120">
<path d="M30 70 L272 70" fill="none" stroke="#0f172a" stroke-width="2"/>
<polygon points="266,66 278,70 266,74" fill="#0f172a"/>
<g fill="none" stroke="#0f172a" stroke-width="1.6"><path d="M70 64 L70 76 M150 64 L150 76 M230 64 L230 76"/></g>
<g fill="none" stroke="#0f6e56" stroke-width="2"><path d="M70 62 Q110 34 150 62 M150 62 Q190 34 230 62"/></g>
<g fill="#0f172a"><circle cx="70" cy="70" r="4"/><circle cx="150" cy="70" r="4"/><circle cx="230" cy="70" r="4"/></g>
<g font-size="14" font-weight="700" text-anchor="middle" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">
<g fill="#0f6e56"><text x="110" y="30">+ r</text><text x="190" y="30">+ r</text></g>
<g fill="#0f172a"><text x="70" y="94">a</text><text x="150" y="94">b</text><text x="230" y="94">c</text></g>
</g>
</svg>
:::

_Exemple détaillé_ : si 7 ; x ; 19 sont trois termes consécutifs d'une suite arithmétique, alors x = (7 + 19)/2 = 26/2 = **13**. On vérifie que la raison est bien constante : 13 − 7 = 6 et 19 − 13 = 6 ✓.

## 👑 Aller plus loin : sommes remarquables et suites célèbres

**La somme des entiers impairs.** Additionne 1 + 3 + 5 + … + (2n − 1). Il y a n termes, le premier vaut 1 et le dernier 2n − 1, donc S = n × (1 + 2n − 1)/2 = n × 2n/2 = **n²**. La somme des n premiers nombres impairs est un carré parfait — un résultat que l'on démontre ici en une ligne.

**La table de Pythagore.** Additionne toutes les cases d'une table de multiplication allant de 1 à n. Chaque ligne k vaut k × (1 + 2 + … + n), donc le total vaut (1 + 2 + … + n)², c'est-à-dire le carré de la somme des n premiers entiers.

**L'identité d'Al Karagi.** Ce mathématicien de la fin du Xᵉ siècle, auteur d'_EL KAFI_, d'_Al Fakhri_ et d'_Al Badi_, a démontré — algébriquement et géométriquement — que 1³ + 2³ + … + n³ = (1 + 2 + … + n)². Pour n = 3 : 1 + 8 + 27 = 36 = 6² ✓.

**Deux suites qui ne sont pas arithmétiques.** La **suite de Syracuse** part d'un entier N et applique la règle « pair → N/2, impair → 3N + 1 » ; en partant de 5 on obtient 5, 16, 8, 4, 2, 1. Personne ne sait démontrer qu'elle finit toujours par atteindre 1, et la question est ouverte depuis plus de cinquante ans. La **suite de Robinson**, elle, se lit à voix haute : 1, puis 11 («un 1»), puis 21 («deux 1»), puis 1211, puis 111221. Ni l'une ni l'autre n'a de raison constante — voilà deux bons rappels que « suite » est un mot bien plus large que « suite arithmétique ».

> 🏆 Gate franchi, héros : tu sais lire une suite définie par son terme général ou par une récurrence, prouver qu'elle est arithmétique en calculant Uₙ₊₁ − Uₙ, atteindre n'importe quel rang avec Uₙ = Uₚ + (n − p)r, reconnaître l'alignement des points (n ; Uₙ), compter les termes d'une somme sans oublier le « + 1 » et appliquer S = nombre de termes × (premier + dernier)/2. Au chapitre suivant, le pas constant devient un **facteur** constant : place aux suites géométriques.
