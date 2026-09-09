# ⚔️ Suites géométriques — quand chaque terme multiplie le précédent

> 💡 «Ajouter fait avancer ; multiplier fait décoller. Une suite géométrique est la machine la plus simple qui existe pour fabriquer une croissance — ou une disparition — foudroyante.»

Tu viens de rencontrer des suites où l'on passe d'un terme au suivant en **ajoutant** toujours le même nombre. Change une seule chose dans cette règle — remplace l'addition par la **multiplication** — et tu obtiens une machine d'une tout autre puissance. C'est elle qui décrit un loyer qui grimpe de 5 % par an, un capital placé à intérêts composés, la pression qui tombe quand on monte en altitude, une audience qui s'effrite semaine après semaine. Toutes ces situations ont la même mécanique, et ce chapitre te donne les trois formules qui la maîtrisent : le **terme général**, la **somme**, et la lecture du **comportement** à long terme.

## 🌱 Multiplier au lieu d'ajouter : la définition

Une maison est louée 200 dinars par mois, et le loyer augmente de **5 % chaque année**. Augmenter de 5 %, c'est ajouter 5 centièmes de la valeur, donc **multiplier par 1,05**. Le loyer suit alors :

$$ 200 → 210 → 220,50 → 231,525 → … $$

Aucune différence constante ici : d'une année à l'autre on gagne 10 dinars, puis 10,50, puis 11,03. Ce qui est constant, c'est le **quotient** : chaque loyer vaut 1,05 fois le précédent. Voilà la règle du chapitre.

> **Définition (encadré officiel).** On dit qu'une suite (Uₙ) est **géométrique**, s'il existe un réel q tel que pour tout entier naturel n on a **Uₙ₊₁ = q Uₙ**. Le nombre réel q est appelé **raison** de cette suite.

> **Remarque (encadré officiel).** Si a, b, c, d, … sont des termes consécutifs d'une suite géométrique, on dit qu'ils sont **en progression géométrique**.

::: figure Même départ, deux règles : la suite sombre ajoute 3 à chaque pas, la suite verte multiplie par 2. Elles coïncident encore au rang 2, puis la multiplicative décroche définitivement — c'est toute la différence entre ajouter et multiplier
<svg viewBox="0 0 340 250">
<path d="M50 30 L50 210 M40 205 L310 205" fill="none" stroke="#0f172a" stroke-width="1.8"/>
<polyline points="55,194.69 115,179.22 175,163.75 235,148.28 295,132.81" fill="none" stroke="#0f172a" stroke-width="2.4"/>
<polyline points="55,194.69 115,184.38 175,163.75 235,122.5 295,40" fill="none" stroke="#0f6e56" stroke-width="2.6"/>
<g fill="#0f172a"><circle cx="55" cy="194.69" r="3.6"/><circle cx="115" cy="179.22" r="3.6"/><circle cx="175" cy="163.75" r="3.6"/><circle cx="235" cy="148.28" r="3.6"/><circle cx="295" cy="132.81" r="3.6"/></g>
<g fill="#0f6e56"><circle cx="115" cy="184.38" r="3.6"/><circle cx="235" cy="122.5" r="3.6"/><circle cx="295" cy="40" r="3.6"/></g>
<path d="M65 50 L95 50" fill="none" stroke="#0f6e56" stroke-width="2.6"/>
<path d="M65 72 L95 72" fill="none" stroke="#0f172a" stroke-width="2.4"/>
<g font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">
<text x="102" y="55" fill="#0f6e56">vₙ = 2 × 2ⁿ</text>
<text x="102" y="77" fill="#0f172a">uₙ = 2 + 3n</text>
</g>
<g font-size="13" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">
<text x="55" y="222">0</text><text x="115" y="222">1</text><text x="175" y="222">2</text><text x="235" y="222">3</text><text x="295" y="222">4</text>
<text x="320" y="222">n</text>
</g>
</svg>
:::

> ⚠️ **Le piège numéro un du chapitre** : la raison d'une suite géométrique se **multiplie**, elle ne s'ajoute pas. Si tu lis « raison 3 », cela veut dire ×3 à chaque pas, pas +3. Une suite qui gagne toujours le même nombre est **arithmétique** ; une suite qui garde le même quotient est **géométrique**.

Pour décider si une suite est géométrique, il n'y a qu'un test : **calculer le quotient uₙ₊₁/uₙ et vérifier qu'il ne dépend pas de n**.

_Exemple détaillé_ : la suite uₙ = 2 × 3ⁿ est géométrique, car

$$ uₙ₊₁/uₙ = (2 × 3ⁿ⁺¹)/(2 × 3ⁿ) = 3 $$

et ce quotient ne dépend pas de n : la raison vaut 3. En revanche uₙ = 3ⁿ + 2 **ne l'est pas** : u₀ = 3, u₁ = 5, u₂ = 11, et les quotients 5/3 puis 11/5 ne sont pas égaux. La constante ajoutée casse tout.

_Exemple détaillé (un cas déguisé)_ : la suite uₙ = √(7ⁿ) semble étrangère au chapitre. Écris-la autrement : √(7ⁿ) = (√7)ⁿ. C'est donc u₀ = 1 et la raison **√7**. Retiens la méthode : **pour reconnaître une suite géométrique, essaie de l'écrire sous la forme u₀ qⁿ**.

## 🧮 Le terme général : atteindre uₙ d'un seul coup

Appliquer la règle mille fois pour obtenir u₁₀₀₀ serait absurde. Comme chaque pas multiplie par q, faire n pas revient à multiplier par q **n fois**, donc par qⁿ.

> **Retenir — Terme général (encadré officiel).** Soit (Vₙ) une suite géométrique de premier terme V₀ et de raison q ≠ 0. On a :
>
> $$ Vₙ = V₀ qⁿ, pour tout n ∈ ℕ ; Vₙ = Vₚ qⁿ⁻ᵖ ; en particulier Vₙ = V₁ qⁿ⁻¹ $$

_Exemple détaillé_ : (uₙ) est géométrique, u₀ = 2 et q = 5. Alors u₃ = 2 × 5³ = 2 × 125 = **250**. Et si l'on ne connaît que u₂ = 4 avec q = 3, on saute directement de 2 à 6, soit **4 pas** : u₆ = 4 × 3⁴ = 4 × 81 = **324**.

> ⚠️ **L'exposant compte des PAS, pas des rangs.** Pour aller de uₚ à uₙ il y a n − p pas, donc l'exposant est **n − p**. L'erreur classique consiste à écrire qⁿ là où il faut qⁿ⁻¹ (ou l'inverse) : on obtient alors un résultat q fois trop grand ou q fois trop petit. Avant de conclure, compte les flèches sur un brouillon.

> 🗡️ **Quand l'exposant est pair, il y a deux raisons.** De v₃ = 12 et v₅ = 48 on tire v₅ = v₃ q², donc q² = 4. Un carré vaut 4 pour **deux** valeurs : q = 2 **et** q = −2 (les deux marchent : 12 → 24 → 48, ou 12 → −24 → 48). Ne rends jamais une seule raison quand l'exposant obtenu est pair ; avec un exposant impair, en revanche, la raison est unique.

## 📈 Lire une suite géométrique sur un graphique

On représente une suite en plaçant les points **Aₙ(n ; uₙ)** : le rang en abscisse, le terme en ordonnée. Les points ne se relient pas par une droite — c'est justement ce qui les distingue d'une progression additive.

::: figure Les points Aₙ(n ; uₙ) d'une suite géométrique de raison plus petite que 1 : le premier point donne u₀ = 16, et chaque ordonnée est la moitié de la précédente, donc la raison vaut 1/2. Les points plongent vers l'axe sans jamais l'atteindre
<svg viewBox="0 0 330 240">
<path d="M52 32 L52 202 M42 195 L300 195" fill="none" stroke="#0f172a" stroke-width="1.8"/>
<g fill="none" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="5 4">
<path d="M52 120 L108 120 M108 120 L108 195"/>
</g>
<g fill="#0f6e56"><circle cx="52" cy="45" r="4.2"/><circle cx="108" cy="120" r="4.2"/><circle cx="164" cy="157.5" r="4.2"/><circle cx="220" cy="176.25" r="4.2"/><circle cx="276" cy="185.63" r="4.2"/></g>
<g font-size="13" font-weight="700" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">
<text x="45" y="49">16</text><text x="45" y="124">8</text><text x="45" y="161">4</text>
</g>
<g font-size="13" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">
<text x="52" y="213">0</text><text x="108" y="213">1</text><text x="164" y="213">2</text><text x="220" y="213">3</text><text x="276" y="213">4</text>
<text x="312" y="213">n</text>
</g>
</svg>
:::

Sur un tel graphique, deux lectures suffisent : le point d'abscisse 0 donne **u₀**, et le quotient de deux ordonnées **consécutives** donne **q**.

_Exemple détaillé_ : des points d'ordonnées 2 ; 6 ; 18 ; 54 aux rangs 0, 1, 2, 3 donnent u₀ = 2 et q = 6/2 = **3**. Attention au sens de la division : c'est le terme **suivant** divisé par le précédent. Et attention aussi à ne pas sauter un rang : 18/2 = 9 est le carré de la raison, pas la raison.

## ➕ La somme de termes consécutifs

Comment additionner 1 + 2 + 4 + … + 2⁹ sans poser dix additions ? L'astuce officielle tient en deux lignes. On pose S = 1 + q + q² + … + qⁿ⁻¹, on multiplie tout par q, puis on soustrait : dans S − qS, tous les termes du milieu disparaissent et il ne reste que S − qS = 1 − qⁿ. Il n'y a plus qu'à diviser par 1 − q.

> **Retenir — Somme de termes consécutifs (encadré officiel).** La somme S de **n termes consécutifs** d'une suite géométrique de raison q (**q ≠ 1**) est
>
> $$ S = a × (1 − qⁿ)/(1 − q), où a est le premier terme $$
>
> autrement dit S = premier terme × (1 − (raison)^(nombre de termes))/(1 − raison). **Si q = 1, alors S = na.** En particulier
>
> $$ 1 + q + q² + … + qⁿ = (1 − qⁿ⁺¹)/(1 − q), q ≠ 1 ; et si q = 1, 1 + q + … + qⁿ = n + 1 $$

_Exemple détaillé (« Quitte ou double »)_ : ton ami te donne 1 dinar le premier jour, 2 le deuxième, 4 le troisième, en doublant chaque jour pendant 10 jours. Ici a = 1, q = 2 et le **nombre de termes** est 10 :

$$ S = 1 × (1 − 2¹⁰)/(1 − 2) = (1 − 1024)/(−1) = 1023 dinars $$

C'est plus que les 1000 dinars que rapporteraient 100 dinars par jour pendant 10 jours — et l'écart n'a fait que commencer.

> ⚠️ **Le n de la formule est le NOMBRE DE TERMES, pas le rang du dernier.** Dans 1 + 2 + … + 2⁹, le dernier terme porte l'exposant 9 mais il y a **10** termes (de 2⁰ à 2⁹). Écrire 2⁹ − 1 = 511 au lieu de 2¹⁰ − 1 = 1023 est l'erreur la plus fréquente du chapitre. Compte les termes, ne recopie pas l'exposant.

> ⚠️ **La formule ne couvre pas q = 1.** Si q = 1, le dénominateur 1 − q vaut 0 et le numérateur aussi : la formule ne dit rien. Mais la situation est la plus simple qui soit — tous les termes sont égaux à a — donc la somme de n d'entre eux vaut **na**. Pour a = 7 et 12 termes : S = 12 × 7 = 84, et surtout pas 0.

## 🔗 La moyenne géométrique

Trois termes consécutifs d'une suite géométrique sont liés par une relation qui permet de retrouver celui du milieu.

Si a, b, c sont consécutifs, alors b = aq et c = bq, donc b/a = c/b. En multipliant en croix :

$$ b² = ac $$

> **Retenir (moyenne géométrique).** Si a, b et c sont, dans cet ordre, trois termes consécutifs d'une suite géométrique, alors **b² = ac**. Lorsque les trois termes sont strictement positifs, on écrit **b = √(ac)** et l'on dit que b est la **moyenne géométrique** de a et c.

_Exemple détaillé_ : 3 ; b ; 27 sont en progression géométrique avec b > 0. Alors b² = 3 × 27 = 81, donc b = **9**. On vérifie : 3 ; 9 ; 27 a bien pour raison 3.

> ⚠️ Ne confonds pas avec la **moyenne arithmétique** (a + c)/2, qui est le terme du milieu d'une progression **additive**. Pour 3 et 27 elle vaudrait 15, ce qui ne donne aucun quotient constant. Multiplication d'un côté, addition de l'autre : le nom de la moyenne suit le nom de la progression.

## 🔭 Comment se comportent les termes quand n grandit

Recopie une suite géométrique dans un tableur, tire la formule vers le bas sur quarante lignes, et le comportement saute aux yeux. Il ne dépend que de la raison.

| raison q            | ce que font les termes                                  | exemple (u₀ = 1)          |
| ------------------- | ------------------------------------------------------- | ------------------------- |
| \|q\| > 1           | ils grandissent en valeur absolue, sans limite          | q = 3 : 1 ; 3 ; 9 ; 27 …  |
| \|q\| < 1           | ils se rapprochent de 0 sans jamais l'atteindre         | q = 0,5 : 1 ; 0,5 ; 0,25 … |
| q = 1               | la suite est **constante**                              | 1 ; 1 ; 1 ; 1 …           |
| q < 0               | les signes **alternent** à chaque pas                   | q = −2 : 1 ; −2 ; 4 ; −8 … |

::: figure Une raison négative (ici q = −2, avec u₀ = 1) fait sauter les termes d'un côté à l'autre de l'axe : un rang sur deux est positif, et l'écart à l'axe grandit à chaque pas
<svg viewBox="0 0 330 250">
<path d="M45 25 L45 228 M42 155 L300 155" fill="none" stroke="#0f172a" stroke-width="1.8"/>
<g fill="none" stroke="#94a3b8" stroke-width="1.6">
<path d="M60 155 L60 147.19 M115 155 L115 170.63 M170 155 L170 123.75 M225 155 L225 217.5 M280 155 L280 30"/>
</g>
<g fill="#0f6e56"><circle cx="60" cy="147.19" r="4.2"/><circle cx="115" cy="170.63" r="4.2"/><circle cx="170" cy="123.75" r="4.2"/><circle cx="225" cy="217.5" r="4.2"/><circle cx="280" cy="30" r="4.2"/></g>
<g font-size="13" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">
<text x="60" y="138">1</text><text x="115" y="186">−2</text><text x="170" y="114">4</text><text x="225" y="234">−8</text><text x="280" y="21">16</text>
<text x="312" y="150">n</text>
</g>
<g font-size="13" font-weight="700" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="38" y="151">0</text></g>
</svg>
:::

> 🗡️ **Trouver un rang seuil : à la calculatrice.** « Au bout de combien de semaines une audience qui perd 10 % par semaine passe-t-elle sous la moitié ? » On multiplie par 0,9 à chaque semaine et l'on calcule les puissances successives : 0,9⁶ = 0,531… (encore au-dessus de la moitié), puis 0,9⁷ = 0,478… (en dessous). La réponse est **7 semaines**. À ce niveau, ce genre de seuil se cherche par essais successifs à la calculatrice, pas par une formule.

> ⚠️ Décroître **ne veut pas dire** raison négative. Une suite qui décroît vers 0 comme 16 ; 8 ; 4 ; 2 a une raison **positive** (1/2) plus petite que 1. C'est le **signe** de q qui fait alterner, c'est sa **taille** qui fait grandir ou rétrécir.

## 👑 Aller plus loin : trois classiques qui tombent en devoir

**Placer son argent : annuel ou semestriel ?** Un capital de 8000 dinars est placé un an. À 4 % l'an, il devient 8000 × 1,04 = 8320 dinars. À 2 % le semestre, il subit **deux** multiplications : 8000 × 1,02² = 8000 × 1,0404 = 8323,20 dinars. Le placement semestriel rapporte 3,20 dinars de plus. La raison est structurelle : au deuxième semestre, les intérêts du premier rapportent à leur tour. C'est tout le sens des **intérêts composés**.

**Les grains de blé de l'échiquier.** La légende raconte que l'inventeur du jeu d'échecs demanda au roi 1 grain de blé sur la première case, 2 sur la deuxième, 4 sur la troisième, en doublant jusqu'à la 64ᵉ. Le total est la somme de 64 termes de raison 2 partant de 1, soit **2⁶⁴ − 1** grains — de quoi charger des milliers de bateaux. Le roi croyait payer une poignée de blé.

**Les nombres parfaits.** Un entier est dit **parfait** lorsqu'il est égal à la somme de ses diviseurs propres : 6 = 1 + 2 + 3, puis 28, 496, 8128. Euclide en donne la fabrique : si p = 2ⁿ⁺¹ − 1 est **premier**, alors N = 2ⁿ × p est parfait. Pour n = 4 : p = 2⁵ − 1 = 31, qui est premier, et N = 16 × 31 = **496**. Les nombres 2ⁿ⁺¹ − 1 premiers portent le nom de **nombres de Mersenne**.

> 🗡️ **Le pont entre les deux familles de suites.** Si une suite (uₙ) vérifie uₙ₊₁ = uₙ + 3 (elle est arithmétique de raison 3) et si l'on pose vₙ = 2^uₙ, alors vₙ₊₁/vₙ = 2^(uₙ + 3)/2^uₙ = 2³ = 8 : la suite (vₙ) est **géométrique de raison 8**. L'exponentielle transforme une addition d'exposants en une multiplication — c'est le mécanisme qui relie les deux chapitres.

> 🗡️ Et la devinette qui résume tout : un nénuphar double de surface chaque jour et couvre le lac au bout de 10 jours. Quel jour couvrait-il la **moitié** du lac ? Le 9ᵉ, bien sûr — en remontant d'un seul pas, on divise par 2. Une croissance géométrique reste presque invisible… jusqu'à l'avant-dernier instant.

> 🏆 Quête franchie, héros : tu sais reconnaître une suite géométrique par son quotient constant, calculer n'importe quel terme avec u₀ qⁿ ou uₚ qⁿ⁻ᵖ, lire un premier terme et une raison sur un graphique, sommer n termes consécutifs sans oublier le cas q = 1, manier la moyenne géométrique et prévoir le comportement des termes selon la raison. Le prochain gate quitte les suites pour un objet plus vaste, qui les contient toutes : les **fonctions**.
