# ⚔️ Fonctions réciproques — remonter le courant de la fonction

> 💡 «Une fonction transporte x vers y ; sa réciproque est le chemin du retour. Sache quand ce chemin existe, et tu sauras résoudre toute équation f(x) = y.»

Jusqu'ici tu partais toujours de x pour obtenir y. Retourne la question : **connaissant y, peux-tu retrouver x — et un seul ?** Quand la réponse est oui, la fonction est une **bijection**, et le chemin du retour porte un nom : la **fonction réciproque** f⁻¹. Tu vas apprendre à garantir son existence (par la stricte monotonie du chapitre 3), à lire sa courbe (un simple miroir), à la dériver sans jamais l'expliciter, et à en tirer une famille toute neuve de fonctions : les racines nᵉᵐᵉˢ. C'est le chapitre qui débloque ln, exp et Arcsin plus loin — et qui alimente presque tous les problèmes d'analyse du bac.

## 🏰 Bijection : une équation, une seule solution

Prends g définie sur ]−∞, 0] par g(x) = 2x² − 3, et cherche les antécédents de 5. L'équation 2x² − 3 = 5 donne x² = 4, donc x = −2 ou x = 2 ; mais **2 n'est pas dans ]−∞, 0]**. Il ne reste qu'**une** solution : x = −2. Ce « exactement une » est toute la notion.

> **Définition — bijection** — « Soit I un intervalle de ℝ et f une fonction définie sur I. On dit que f réalise une bijection de I sur f(I) (ou que f est une bijection de I sur f(I)), si pour tout y de f(I), l'équation f(x) = y admet une unique solution dans I. »

Deux ingrédients, donc : l'**existence** d'une solution (elle est gratuite, puisque y est pris dans l'image f(I)) et son **unicité** (c'est elle qu'il faut gagner). Le chapitre 3 fournit l'outil décisif.

> **Théorème — monotonie stricte ⟹ bijection** — « Si f est une fonction strictement monotone sur un intervalle I, alors f réalise une bijection de I sur f(I). »

_Pourquoi ?_ Si deux réels distincts x₁ < x₂ de I avaient la même image, la stricte monotonie imposerait f(x₁) < f(x₂) ou f(x₁) > f(x₂) — jamais l'égalité. Deux antécédents distincts sont donc impossibles : l'unicité est acquise.

_Exemple détaillé_ — reprenons g(x) = 2x² − 3 sur I = ]−∞, 0]. Sa dérivée g′(x) = 4x est strictement négative sur ]−∞, 0[, donc g est **strictement décroissante** sur I : g réalise une bijection de I sur g(I). Reste à identifier g(I) : g est continue, g(0) = −3 et lim_{x→−∞} g(x) = +∞, donc **g(I) = [−3, +∞[**. Pour tout y ≥ −3, l'équation 2x² − 3 = y équivaut à x² = (y + 3)/2, dont l'unique solution négative est x = −√((y + 3)/2). _Vérification_ : pour y = 5, x = −√4 = −2 et g(−2) = 2 × 4 − 3 = 5 ✓.

Préciser l'intervalle image f(I) est **la moitié du travail** ; on le lit dans le tableau de variation, avec les limites aux bornes (chapitre 1).

| f continue et strictement **croissante** sur | f(I) vaut                                          |
| -------------------------------------------- | -------------------------------------------------- |
| [a, b]                                        | [f(a), f(b)]                                        |
| [a, b[                                        | [f(a), lim_{x→b⁻} f(x)[                             |
| ]a, b[                                        | ]lim_{x→a⁺} f(x), lim_{x→b⁻} f(x)[                  |

Si f est strictement **décroissante**, les mêmes formules s'appliquent en **échangeant les bornes** de l'intervalle image.

> ⚠️ **Continuité seule ne suffit pas.** Une fonction f continue sur [1, +∞[ avec f(1) = 2 et lim_{+∞} f = 3 ne réalise **pas** forcément une bijection sur [2, 3[ : rien ne l'empêche de monter puis redescendre et de reprendre deux fois la même valeur. Il faut la **stricte monotonie**.

> ⚠️ Toute fonction affine n'est pas une bijection de ℝ sur ℝ : x ↦ ax + b n'est strictement monotone que si **a ≠ 0**. Pour a = 0 la fonction est constante et f(ℝ) est réduit à {b}.

## 🗝️ La fonction réciproque, le chemin du retour

Puisque chaque y de f(I) a un antécédent et un seul, on peut définir la fonction qui à y associe cet antécédent.

> **Définition — fonction réciproque** — « Soit f une bijection d'un intervalle I sur f(I). On appelle fonction réciproque de f et on note f⁻¹ la fonction définie sur f(I) qui à tout y de f(I) associe l'unique solution dans I de l'équation f(x) = y. »

> **Conséquence** — « Soit f une bijection d'un intervalle I sur f(I) et f⁻¹ sa fonction réciproque. Pour tout x de I et tout y de f(I), f(x) = y, si et seulement si, f⁻¹(y) = x. f⁻¹∘f(x) = x, pour tout x de I et f∘f⁻¹(y) = y, pour tout y de f(I). »

Retiens l'équivalence **f(x) = y ⟺ f⁻¹(y) = x** : c'est l'outil universel, aussi bien pour calculer une valeur de f⁻¹ que pour la dériver plus loin. Noter aussi que f⁻¹ est une bijection de f(I) sur I, et que (f⁻¹)⁻¹ = f.

**Méthode pour expliciter f⁻¹** : partir de y = f(x), résoudre en x, puis **garder la seule solution appartenant à I**.

_Exemple détaillé_ — f(x) = x² − 4x + 1 sur I = [2, +∞[. Sa dérivée f′(x) = 2x − 4 est strictement positive sur ]2, +∞[ : f est strictement croissante, donc bijective. Avec f(2) = 4 − 8 + 1 = −3 et lim_{+∞} f = +∞, on a **J = f(I) = [−3, +∞[**. On écrit la forme canonique : y = (x − 2)² − 3, donc (x − 2)² = y + 3 et x − 2 = ±√(y + 3) ; comme x ≥ 2, on garde le signe +.

$$ f⁻¹(y) = 2 + √(y + 3), pour tout y de [−3, +∞[ $$

_Vérification_ : f⁻¹(1) = 2 + √4 = 4 et f(4) = 16 − 16 + 1 = 1 ✓.

_Exemple_ — f(x) = 1/x sur ℝ*₊ est strictement décroissante et f(ℝ*₊) = ℝ*₊. De y = 1/x on tire x = 1/y : **f⁻¹ = f**. Une fonction peut donc être sa propre réciproque.

> 🗡️ Ne confonds jamais **f⁻¹**, la fonction réciproque, avec **1/f**, l'inverse. Pour f(x) = x² − 4x + 1 sur [2, +∞[, f⁻¹(1) = 4 alors que 1/f(1) = 1/(−2) = −0,5.

## 🪞 Deux courbes, un seul miroir : la droite Δ : y = x

Dans un repère orthonormé, les points M₁(x, y) et M₂(y, x) sont symétriques par rapport à la droite Δ : y = x. Or M₁(x, y) appartient à C_f exactement quand y = f(x) avec x ∈ I, c'est-à-dire quand x = f⁻¹(y) avec y ∈ f(I) — c'est-à-dire quand M₂ appartient à C_{f⁻¹}. D'où :

> **Conséquence — symétrie des courbes** — « Les courbes respectives d'une bijection f et de sa réciproque f⁻¹ dans un repère orthonormé sont symétriques par rapport à la droite Δ : y = x. »

::: figure Le point M′ de C_{f⁻¹} s'obtient en repliant M de C_f par-dessus la droite Δ : les coordonnées s'échangent.
<svg viewBox="0 0 330 240"><path d="M28 200 H315" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M40 218 V20" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M315 200 l-7 -3.5 l0 7 z" fill="#0f172a"/><path d="M40 20 l-3.5 7 l7 0 z" fill="#0f172a"/><line x1="40" y1="200" x2="215" y2="25" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="5 4"/><polyline points="40,200 67,186 95,145 117,92 133,41" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"/><polyline points="40,200 54,172 95,145 148,123 199,106 227,99 260,90" fill="none" stroke="#b45309" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"/><line x1="117" y1="92" x2="148" y2="123" stroke="#0f172a" stroke-width="1.2" stroke-dasharray="3 3"/><circle cx="117" cy="92" r="4" fill="#0f172a"/><circle cx="148" cy="123" r="4" fill="#0f172a"/><text x="72" y="88" font-size="12" font-weight="700" fill="#0f172a">M(a, b)</text><text x="156" y="136" font-size="12" font-weight="700" fill="#0f172a">M′(b, a)</text><text x="216" y="32" font-size="12" font-weight="700" fill="#64748b">Δ : y = x</text><text x="138" y="36" font-size="12" font-weight="700" fill="#0f6e56">C_f</text><text x="262" y="86" font-size="12" font-weight="700" fill="#b45309">C_f⁻¹</text><text x="30" y="215" font-size="12" font-weight="700" fill="#0f172a">O</text></svg>
:::

En pratique : pour tracer C_{f⁻¹}, tu **ne calcules rien** — tu replies C_f par-dessus Δ. Les tableaux de variation se déduisent de la même façon : celui de f⁻¹ s'obtient en échangeant la ligne des x et la ligne des f(x).

_Exemple_ — si f est une bijection de [−2, +∞[ sur [−1, +∞[ avec f(−2) = −1, f(0) = 1 et f(2) = 3, alors f⁻¹(−1) = −2, f⁻¹(1) = 0 et f⁻¹(3) = 2 : on lit la courbe « à l'envers », en entrant par l'axe des ordonnées.

Ce pliage **échange les rôles des deux axes** : ce que C_f fait à l'horizontale, C_{f⁻¹} le fait à la verticale. En particulier, une **asymptote horizontale y = ℓ de C_f devient une asymptote verticale x = ℓ de C_{f⁻¹}** — et, dans l'autre sens, une asymptote verticale x = ℓ de C_f se replie en asymptote horizontale y = ℓ de C_{f⁻¹}. La justification tient en une phrase : dire que f(x) tend vers ℓ quand x devient arbitrairement grand, c'est exactement dire que f⁻¹(y) devient arbitrairement grand quand y tend vers ℓ. C'est le même mécanisme qui transformera plus loin une **tangente** horizontale de C_f (cas f′(a) = 0) en tangente verticale de C_{f⁻¹}.

_Exemple_ — f(x) = x/(x + 1) sur I = ]−1, +∞[ : f′(x) = 1/(x + 1)² > 0, donc f est strictement croissante, avec lim_{x→−1⁺} f = −∞ et lim_{x→+∞} f = 1, d'où J = ]−∞, 1[. C_f a l'asymptote verticale x = −1 et l'asymptote horizontale y = 1. De y = x/(x + 1) on tire x = y/(1 − y), donc f⁻¹(y) = y/(1 − y) : elle a bien l'asymptote **horizontale y = −1** (quand y → −∞) et l'asymptote **verticale x = 1** (quand y → 1⁻) ✓ — les deux asymptotes ont échangé leur nature.

> 🗡️ Si a vérifie f(a) = a, alors f⁻¹(a) = a : le point (a, a) appartient **aux deux courbes**, sur Δ. Résoudre f(x) = x fournit donc directement des points d'intersection de C_f et C_{f⁻¹} — un réflexe très rentable aux examens.

## 🧭 Réciproque d'une fonction continue strictement monotone

Une fois la bijection acquise par la monotonie, la réciproque hérite gratuitement de deux propriétés.

> **Théorème — réciproque d'une fonction strictement monotone** — « Si f est une fonction continue et strictement monotone sur un intervalle I alors sa réciproque f⁻¹ est continue et strictement monotone sur l'intervalle f(I) et varie dans le même sens que f. »

La continuité de f⁻¹ est **admise**. La monotonie, elle, se démontre par l'absurde : si f est croissante et si l'on avait y₁ < y₂ avec f⁻¹(y₁) ≥ f⁻¹(y₂), la croissance de f donnerait y₁ = f(f⁻¹(y₁)) ≥ f(f⁻¹(y₂)) = y₂, contradiction.

**« Même sens » veut dire : croissante ⟹ croissante, décroissante ⟹ décroissante.** C'est cohérent avec le miroir : la symétrie par rapport à Δ conserve le sens de parcours de la courbe.

_Exemple détaillé_ — f(x) = sin x sur I = [−π/2, π/2]. f est continue et f′(x) = cos x > 0 sur ]−π/2, π/2[ : f est strictement croissante, donc bijective de I sur J = [sin(−π/2), sin(π/2)] = **[−1, 1]**. Sa réciproque f⁻¹ est continue et strictement croissante sur [−1, 1]. On lit ses valeurs sur le cercle trigonométrique : f⁻¹(1/2) = π/6, f⁻¹(−√3/2) = −π/3, f⁻¹(√2/2) = π/4, f⁻¹(1) = π/2. _Vérification_ : sin(π/6) = 1/2 ✓, sin(−π/3) = −√3/2 ✓.

_Exemple_ — f(x) = 1/x sur ℝ*₊ est strictement **décroissante** ; sa réciproque f⁻¹(x) = 1/x est bien elle aussi strictement décroissante ✓.

> ⚠️ « Même sens de variation » ne veut pas dire « même signe ». Prends f(x) = x + 10 sur I = [−1, 1] : f est strictement positive sur I, mais f(I) = [9, 11] et f⁻¹(y) = y − 10 vaut −1 en 9 et 1 en 11 — elle **change** de signe. Le signe de f⁻¹ se lit sur I, pas sur f(I).

## ⚡ Dériver la réciproque sans jamais l'expliciter

Voici l'outil le plus rentable du chapitre : on dérive f⁻¹ **même quand on ne sait pas l'écrire**.

> **Théorème — dérivée de la réciproque en un point** — « Soit f une fonction strictement monotone d'un intervalle I sur f(I), a un réel de I et b = f(a). Si f est dérivable en a et si f′(a) ≠ 0, alors f⁻¹ est dérivable en b et (f⁻¹)′(b) = 1/f′(a). » (Ce résultat reste valable lorsqu'il s'agit de dérivée à droite ou à gauche en a.)

> **Corollaire — sur tout l'intervalle f(I)** — « Soit f une bijection d'un intervalle I sur f(I). Si f est dérivable sur I et f′(x) ≠ 0 pour tout x de I, alors f⁻¹ est dérivable sur f(I) et (f⁻¹)′(y) = 1/f′[f⁻¹(y)], pour tout y de f(I). »

$$ (f⁻¹)′(b) = 1/f′(a) avec b = f(a), c'est-à-dire a = f⁻¹(b) $$

_D'où vient la formule ?_ De f∘f⁻¹(y) = y : en dérivant les deux membres par la règle de la composée, (f⁻¹)′(y) × f′(f⁻¹(y)) = 1, donc (f⁻¹)′(y) = 1/f′(f⁻¹(y)).

_Exemple détaillé_ — f(x) = x/(1 + x²) sur I = [1, +∞[. On calcule f′(x) = ((1 + x²) − x × 2x)/(1 + x²)² = (1 − x²)/(1 + x²)², strictement négative sur ]1, +∞[ : f est strictement décroissante. Avec f(1) = 1/2 et lim_{+∞} f = 0, on obtient **J = ]0, 1/2]**. Calculons (f⁻¹)′(2/5). On cherche d'abord a tel que f(a) = 2/5 : a/(1 + a²) = 2/5 donne 2a² − 5a + 2 = 0, de racines 2 et 1/2 ; seule **a = 2** appartient à I. Ensuite f′(2) = (1 − 4)/(1 + 4)² = −3/25. Donc :

$$ (f⁻¹)′(2/5) = 1/f′(2) = 1/(−3/25) = −25/3 $$

_Vérification par l'expression explicite_ : y = x/(1 + x²) équivaut à yx² − x + y = 0, d'où x = (1 + √(1 − 4y²))/(2y) (racine ≥ 1). Un taux d'accroissement numérique entre y = 0,4 et y = 0,401 donne (1,991676 − 2)/0,001 ≈ −8,32, à comparer à −25/3 ≈ −8,33 ✓.

_Exemple_ — f(x) = x³ + x sur ℝ : f′(x) = 3x² + 1 > 0, donc f est une bijection de ℝ sur ℝ. Comme f(1) = 2, on a (f⁻¹)′(2) = 1/f′(1) = 1/4, sans jamais résoudre l'équation du troisième degré.

**Que se passe-t-il si f′(a) = 0 ?** La tangente à C_f en A(a, b) est horizontale ; par symétrie, la tangente à C_{f⁻¹} en A′(b, a) est **verticale** : f⁻¹ n'est pas dérivable en b, et le taux d'accroissement y tend vers +∞ ou −∞.

::: figure La tangente horizontale de C_f en O se replie en une tangente verticale de C_{f⁻¹} : en 0, la réciproque n'est pas dérivable.
<svg viewBox="0 0 300 220"><line x1="87" y1="173" x2="213" y2="47" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="5 4"/><polyline points="94,198 105,155 118,125 132,113 150,110 168,107 181,95 195,65 206,22" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"/><polyline points="62,166 105,155 135,141 147,128 150,110 153,92 165,78 195,65 238,54" fill="none" stroke="#b45309" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"/><line x1="105" y1="110" x2="195" y2="110" stroke="#7c3aed" stroke-width="2"/><line x1="150" y1="62" x2="150" y2="158" stroke="#7c3aed" stroke-width="2"/><circle cx="150" cy="110" r="4" fill="#0f172a"/><text x="205" y="20" font-size="12" font-weight="700" fill="#0f6e56">x ↦ x³</text><text x="240" y="52" font-size="12" font-weight="700" fill="#b45309">x ↦ ∛x</text><text x="60" y="106" font-size="11" font-weight="700" fill="#7c3aed">f′(0) = 0</text><text x="156" y="176" font-size="11" font-weight="700" fill="#7c3aed">tangente verticale</text></svg>
:::

_Exemple_ — f(x) = x³ sur ℝ est une bijection de ℝ sur ℝ, mais f′(0) = 0 : sa réciproque x ↦ ∛x n'est **pas** dérivable en 0.

## 🔮 La fonction racine nᵉᵐᵉ

Le théorème précédent construit une nouvelle famille de fonctions usuelles.

> **Théorème et définition — fonction racine nᵉᵐᵉ** — « Soit n un entier supérieur ou égal à 2. La fonction x ↦ xⁿ réalise une bijection de ℝ₊ sur ℝ₊. Elle admet une fonction réciproque strictement croissante de ℝ₊ sur ℝ₊, appelée fonction racine nᵉᵐᵉ. »

> **Notation** — « L'image d'un réel positif x par la fonction racine nᵉᵐᵉ est notée ⁿ√x et se lit "racine nᵉᵐᵉ de x". Lorsque n = 2 et pour x positif, ²√x = √x. »

> **Conséquence** — « Pour tous réels positifs x et y, y = xⁿ, si et seulement si, x = ⁿ√y. lim_{x→+∞} ⁿ√x = +∞. »

> ⚠️ **ⁿ√ ne s'applique qu'à des réels positifs**, quelle que soit la parité de n : ∛(−8) n'a pas de sens dans ce programme. Avant d'écrire ⁿ√(A), vérifie que A ≥ 0.

Les règles de calcul découlent toutes de la relation y = xⁿ ⟺ x = ⁿ√y.

> **Conséquence — opérations sur les radicaux** — « Soit deux entiers n et p tels que n ≥ 2 et p ≥ 2 et deux réels positifs a et b. Alors ⁿ√(aⁿ) = a ; (ⁿ√a)ⁿ = a ; ⁿ√(a·b) = ⁿ√a·ⁿ√b ; ⁿ√(a/b) = ⁿ√a/ⁿ√b, b ≠ 0 ; ⁿ√a = ⁿᵖ√(aᵖ) ; (ⁿ√a)ᵖ = ⁿ√(aᵖ) ; ⁿ√(ᵖ√a) = ⁿᵖ√a. »

_Exemples détaillés de simplification_ :

- ⁶√64 = ⁶√(2⁶) = **2** ✓ (2⁶ = 64).
- ∛(2⁶ × 3³) = ∛(2⁶) × ∛(3³) = 2² × 3 = **12** ✓ (12³ = 1728 = 64 × 27).
- √(∛729) = ⁶√729 = ⁶√(3⁶) = **3** ✓.
- ∛(2√2) = **√2**, car (√2)³ = 2√2 ✓.

_Exemple détaillé de comparaison_ — comparons ⁶√(2⁴) et ⁴√(2³). On **ramène au même indice** avec la règle ⁿ√a = ⁿᵖ√(aᵖ), en prenant 12 = PPCM(6, 4) :

$$ ⁶√(2⁴) = ¹²√((2⁴)²) = ¹²√(2⁸)     et     ⁴√(2³) = ¹²√((2³)³) = ¹²√(2⁹) $$

Comme 2⁸ < 2⁹ et que la fonction ¹²√ est croissante, **⁶√(2⁴) < ⁴√(2³)**.

> ⚠️ Ce résultat **s'inverse** pour les nombres entre 0 et 1 ! Pour x ≥ 0, ⁶√(x⁴) = ¹²√(x⁸) et ⁴√(x³) = ¹²√(x⁹) : si 0 ≤ x < 1 alors x⁹ < x⁸ donc ⁶√(x⁴) > ⁴√(x³) ; si x > 1 l'inégalité est dans l'autre sens. Autrement dit « ⁴√x ≥ ∛x pour tout x > 0 » est **faux** : pour x = 16, ⁴√16 = 2 alors que ∛16 ≈ 2,52.

La dérivée s'obtient par le théorème de la réciproque appliqué à g(x) = xⁿ, de dérivée g′(x) = nxⁿ⁻¹.

> **Théorème — dérivée de x ↦ ⁿ√x** — « Pour tout entier n ≥ 2, la fonction f : x ↦ ⁿ√x est continue sur [0, +∞[ et dérivable sur ]0, +∞[. De plus, f′(x) = 1/(n·ⁿ√(xⁿ⁻¹)), pour tout x > 0. »

_Démonstration_ — f = g⁻¹ avec g(x) = xⁿ. Pour y > 0, f′(y) = 1/g′(f(y)) = 1/(n × (ⁿ√y)ⁿ⁻¹) = 1/(n·ⁿ√(yⁿ⁻¹)), en utilisant (ⁿ√a)ᵖ = ⁿ√(aᵖ).

_Exemple détaillé_ — pour n = 3 en x = 8 : f′(8) = 1/(3 × ∛(8²)) = 1/(3 × ∛64) = 1/(3 × 4) = **1/12**. _Vérification numérique_ : (∛8,001 − ∛8)/0,001 ≈ (2,0000833 − 2)/0,001 ≈ 0,0833 ≈ 1/12 ✓.

_Exemple_ — la limite lim_{x→2} (∛x − ∛2)/(x − 2) est, par définition, le nombre dérivé de ∛ en 2, soit 1/(3 × ∛4) ≈ 0,21.

**En 0**, le taux d'accroissement vaut (ⁿ√x − 0)/(x − 0) = ⁿ√x/x, et comme ⁿ√x/x = 1/(ⁿ√(xⁿ⁻¹)) tend vers +∞ quand x → 0⁺, la fonction n'est **pas dérivable à droite en 0** : C_f y admet une **demi-tangente verticale**. C'est cohérent avec la section précédente : g′(0) = 0 pour g(x) = xⁿ.

_Exemple_ — équation ∛x = ⁴√2 dans ℝ₊. En élevant à la puissance 12 : x⁴ = 2³ = 8, donc **x = ⁴√8**. _Vérification_ : ∛(⁴√8) = ¹²√8 = ¹²√(2³) = ⁴√2 ✓.

## 🌀 Composée : la fonction x ↦ ⁿ√(u(x))

Dernière marche : la racine nᵉᵐᵉ d'une expression, qui se dérive comme toute composée (chapitre 3).

> **Théorème — dérivée de x ↦ ⁿ√(u(x))** — « Soit u une fonction dérivable et positive sur un intervalle I et un entier n ≥ 2. La fonction f : x ↦ ⁿ√(u(x)) est continue sur I et dérivable en tout réel x de I tel que u(x) ≠ 0. De plus, f′(x) = u′(x)/(n·ⁿ√(u(x)ⁿ⁻¹)), pour tout x de I tel que u(x) > 0. »

_Démonstration_ — f est la composée de x ↦ u(x) et de x ↦ ⁿ√x ; on applique (g∘u)′ = u′ × g′(u) avec g′(t) = 1/(n·ⁿ√(tⁿ⁻¹)).

Pour n = 2 on retrouve la formule connue (√u)′ = u′/(2√u).

_Exemple détaillé_ — f(x) = ∛(x² + 1) sur ℝ. Ici u(x) = x² + 1 > 0 partout et u′(x) = 2x, donc f est dérivable sur ℝ et :

$$ f′(x) = 2x/(3·∛((x² + 1)²)) $$

_Vérification numérique en x = 1_ : la formule donne 2/(3 × ∛4) ≈ 2/(3 × 1,5874) ≈ 0,420 ; le taux (f(1,001) − f(1))/0,001 ≈ (1,260341 − 1,259921)/0,001 ≈ 0,420 ✓. On en déduit au passage le signe de f′ : celui de x. La fonction f est donc décroissante sur ]−∞, 0] et croissante sur [0, +∞[, avec un minimum f(0) = 1 — et sa restriction à [0, +∞[ réalise une bijection de [0, +∞[ sur **[1, +∞[**.

_Exemple_ — h(x) = ⁴√(x² − 1) sur [1, +∞[ : u(x) = x² − 1, u′(x) = 2x, donc pour x > 1, h′(x) = 2x/(4·⁴√((x² − 1)³)) = x/(2·⁴√((x² − 1)³)) > 0. En x = 1, u s'annule : h n'y est **pas** dérivable (demi-tangente verticale).

> 🏆 Quatrième porte franchie, héros : tu sais reconnaître une bijection, construire et lire f⁻¹, la tracer d'un simple pliage sur Δ : y = x, et la dériver sans jamais l'écrire. Tu as gagné au passage les racines nᵉᵐᵉˢ, arme indispensable pour les études de fonctions du bac — et la clé qui ouvrira, aux chapitres 7 et 8, les portes de ln et exp.
