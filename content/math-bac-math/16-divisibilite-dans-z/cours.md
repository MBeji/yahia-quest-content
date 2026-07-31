# ⚔️ Divisibilité dans ℤ — quand le reste dit tout

> 💡 «Pascal, en 1654, promettait de reconnaître “à la simple inspection de ses chiffres” si un nombre en divise un autre. Son secret tient en une phrase : ne regarde plus les nombres, regarde leurs restes.»

Depuis quinze chapitres tu travailles avec des fonctions, des courbes, des vecteurs — des objets continus. Ici tout change : **ℕ est l'ensemble des entiers naturels, ℤ celui des entiers relatifs**, et on n'en sortira pas. Pas de limite, pas de dérivée : une seule opération, la division, et une seule question — que reste-t-il ? Tu vas découvrir que ce reste, à lui seul, suffit à prédire le chiffre des unités de 9²⁰⁰⁷ sans jamais calculer 9²⁰⁰⁷.

## 🏰 Diviser, c'est écrire a = dq

Prends l'entier a = 599873120. Il se coupe en quatre parts entières : a = 4 × 149968280. Il se coupe aussi en onze parts, au signe près : a = −11 × (−54533920). Mais se coupe-t-il en six ? Garde la question en tête — on y répondra au dernier paragraphe du chapitre, sans poser une seule division.

> **Définition** — « Soit a un entier et d un entier non nul. On dit que d est un **diviseur** de a ou que a est **divisible** par d, s'il existe un entier q tel que a = dq. »

> **Vocabulaire** — « Si un entier a est divisible par un entier d non nul, on dit que a est un **multiple** de d. »

Deux remarques qui évitent la moitié des erreurs de signe. D'abord, **si d divise a, alors −d divise a** : a = dq s'écrit aussi a = (−d)(−q). Ensuite, les multiples de d forment l'ensemble

$$ dℤ = {dq, q ∈ ℤ} $$

_Exemple détaillé_ — l'ensemble D_a de tous les diviseurs de quelques entiers :

| a         | D_a                                     | Pourquoi                                     |
| --------- | --------------------------------------- | -------------------------------------------- |
| −15       | {−15, −5, −3, −1, 1, 3, 5, 15}          | 15 = 3 × 5, et chaque diviseur va par paire ± |
| 143       | {−143, −13, −11, −1, 1, 11, 13, 143}    | 143 = 11 × 13                                |
| −143      | {−143, −13, −11, −1, 1, 11, 13, 143}    | a et −a ont **exactement** les mêmes diviseurs |
| 1 et −1   | {−1, 1}                                 | 1 = dq impose d = 1 ou d = −1                |
| 0         | tous les entiers non nuls               | 0 = d × 0 pour **tout** d ≠ 0                |
| p premier | {−p, −1, 1, p}                          | définition même d'un nombre premier          |

> ⚠️ **0 est le champion des multiples, jamais un diviseur.** Tout entier non nul divise 0, mais 0 ne divise rien : la définition exige d ≠ 0. Et « d divise a » ne dit rien sur les tailles quand a = 0 : 1000 divise 0 alors que 1000 > 0.

Trois propriétés font tout le travail du chapitre :

> **Propriétés** — « Soit a et b deux entiers non nuls et c un entier. • Si a divise b et b divise a, alors **a = b ou a = −b**. • Si a divise b et b divise c, alors **a divise c**. • Si a divise b et a divise c, alors **a divise αb + βc** pour tous entiers α et β. »

_Exemple détaillé (la combinaison linéaire)_ — 7 divise 21 et 7 divise 35. Alors 7 divise 4 × 21 − 3 × 35. _Contrôle_ : 4 × 21 = 84, 3 × 35 = 105, donc 84 − 105 = −21 = 7 × (−3) ✓.

_Exemple détaillé (l'entier 4200³ + 3521¹⁰ est-il divisible par 7 ?)_ — 4200 = 7 × 600, donc 7 divise 4200 et donc 4200³. De même 3521 = 7 × 503, donc 7 divise 3521¹⁰. La troisième propriété avec α = β = 1 conclut : **oui**, 7 divise la somme. _Contrôle des deux produits_ : 7 × 600 = 4200 ✓ et 7 × 503 = 3521 ✓.

_Exemple détaillé (l'entier 260²⁶⁰ + 11 est-il divisible par −13 ?)_ — 260 = 13 × 20, donc 13 divise 260²⁶⁰. Si 13 divisait la somme, il diviserait la différence (somme) − 260²⁶⁰ = 11 — or 13 ne divise pas 11. Donc **non**, et comme d et −d ont les mêmes multiples, −13 ne la divise pas non plus.

_Exercice résolu (le grand classique)_ — **déterminer tous les entiers n tels que n − 1 divise n + 10.** L'astuce est toujours la même : faire apparaître le diviseur dans le dividende. Comme n + 10 = (n − 1) + 11 et que n − 1 divise n − 1, la troisième propriété donne

$$ n − 1 divise n + 10 ⟺ n − 1 divise 11 ⟺ n − 1 ∈ {−11, −1, 1, 11} $$

d'où **n ∈ {−10, 0, 2, 12}**. _Contrôle des quatre valeurs_ : n = −10 donne −11 et 0, et −11 divise 0 ✓ ; n = 0 donne −1 et 10 ✓ ; n = 2 donne 1 et 12 ✓ ; n = 12 donne 11 et 22 = 11 × 2 ✓.

> 🗡️ Même recette pour « n divise n − 6 » : n − 6 = n − 6, donc n divise (n − 6) − n = −6, donc n divise 6 et n ∈ {−6, −3, −2, −1, 1, 2, 3, 6}. **On soustrait pour faire disparaître la partie encombrante**, on n'essaie jamais les valeurs une à une.

## ⚡ La division euclidienne : un quotient, un reste, et rien d'autre

Une calculatrice affiche 12345 ÷ 57 = 216,5789474. L'entier caché derrière cet affichage, c'est la **partie entière**.

> **Rappel** — « Pour tout réel x, il existe un entier unique n tel que n ≤ x < n + 1. Cet entier n est appelé **partie entière** du réel x. »

Le piège arrive dès que les signes s'en mêlent : le quotient ne se définit pas de la même façon selon le signe du diviseur.

> **Définition (quotient)** — « Soit a et b deux entiers avec b non nul. On appelle **quotient** de a par b l'entier q défini de la manière suivante : • q est le **plus grand entier inférieur ou égal** à a/b si b > 0 ; • q est le **plus petit entier supérieur ou égal** à a/b si b < 0. »

> **Définition (reste)** — « Soit a et b deux entiers avec b non nul. On appelle **reste** de a par b l'entier r tel que **r = a − bq**, où q est le quotient de a par b. »

Les deux définitions se résument en un seul théorème, celui qu'on cite en copie :

> **Théorème (division euclidienne)** — « Pour tout entier a et pour tout entier b non nul, il existe un **couple unique** d'entiers (q, r) tel que **a = bq + r et 0 ≤ r < |b|**. »

> **Conséquence** — « Le reste de tout entier n dans la division euclidienne par un entier non nul b est un élément de l'ensemble **{0, 1, 2, …, |b| − 1}**. »

_Exemple détaillé (les quatre combinaisons de signes, avec a = 47 et b = 5)_ :

| a   | b   | a/b  | Règle appliquée     | q   | r = a − bq        | Contrôle du reste |
| --- | --- | ---- | ------------------- | --- | ----------------- | ----------------- |
| 47  | 5   | 9,4  | plus grand ≤ 9,4    | 9   | 47 − 45 = **2**   | 0 ≤ 2 < 5 ✓       |
| −47 | 5   | −9,4 | plus grand ≤ −9,4   | −10 | −47 + 50 = **3**  | 0 ≤ 3 < 5 ✓       |
| 47  | −5  | −9,4 | plus petit ≥ −9,4   | −9  | 47 − 45 = **2**   | 0 ≤ 2 < 5 ✓       |
| −47 | −5  | 9,4  | plus petit ≥ 9,4    | 10  | −47 + 50 = **3**  | 0 ≤ 3 < 5 ✓       |

Lis la colonne des restes : **le reste ne dépend que de a et de la valeur absolue de b**, jamais du signe de b. Seul le quotient change.

::: figure Entre les deux multiples de 5 qui l'encadrent, −47 se loge à 3 crans au-dessus de celui de gauche : ce décalage, toujours pris vers la droite et donc jamais négatif, est le reste.
<svg viewBox="0 0 340 118"><path d="M20 62 H320" fill="none" stroke="#94a3b8" stroke-width="1.5"/><path d="M100 55 V69 M140 55 V69 M180 55 V69 M220 55 V69" fill="none" stroke="#94a3b8" stroke-width="1.2"/><path d="M60 62 H180" fill="none" stroke="#0f6e56" stroke-width="4"/><path d="M60 50 V74 M260 50 V74" fill="none" stroke="#0f172a" stroke-width="2.2"/><path d="M180 40 V54" fill="none" stroke="#b45309" stroke-width="1.4"/><circle cx="180" cy="62" r="5" fill="#b45309"/><g font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="180" y="34" text-anchor="middle" fill="#b45309">a = −47</text><text x="118" y="50" text-anchor="middle" fill="#0f6e56">r = 3</text></g><g font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="60" y="94" text-anchor="middle" fill="#0f172a">5 × (−10) = −50</text><text x="260" y="94" text-anchor="middle" fill="#0f172a">5 × (−9) = −45</text></g></svg>
:::

> ⚠️ **Le quotient de −20 par 7 n'est pas −2.** On a −20/7 ≈ −2,857 et b > 0 : le plus grand entier **inférieur ou égal** à −2,857 est **−3**, donc q = −3 et r = −20 + 21 = 1. Avec q = −2 on obtiendrait r = −20 + 14 = −6, un reste négatif : impossible. **Le test 0 ≤ r < |b| tranche toujours.**

_Exemple détaillé (des grands nombres, à la calculatrice)_ — soit a = 12354878 et b = 23458. La calculatrice donne a/b ≈ 526,6807, donc **q = 526** et r = 12354878 − 23458 × 526. _Contrôle_ : 23458 × 526 = 12338908, donc r = 12354878 − 12338908 = **15970**, et 0 ≤ 15970 < 23458 ✓. Avec a = −12354878 et b = 23458 : −526,6807 a pour partie entière **−527**, et r = −12354878 + 23458 × 527 = −12354878 + 12362366 = **7488** ✓. Remarque le contrôle croisé : 15970 + 7488 = 23458 = |b|, comme il se doit pour deux opposés non multiples de b.

_Exercice résolu_ — **déterminer l'ensemble E des entiers a tels que |a| < 53 et dont le reste dans la division par 11 vaut 3.** Le reste vaut 3, donc a = 11q + 3 avec q entier. La condition |11q + 3| < 53 s'écrit −53 < 11q + 3 < 53, soit **−56 < 11q < 50**, soit −5,09 < q < 4,54, donc q ∈ {−5, −4, −3, −2, −1, 0, 1, 2, 3, 4}. En reportant :

$$ E = {−52, −41, −30, −19, −8, 3, 14, 25, 36, 47} $$

_Contrôle des bords_ : q = −5 donne −52 et |−52| = 52 < 53 ✓ ; q = −6 donnerait −63, écarté ✓ ; q = 4 donne 47 ✓ ; q = 5 donnerait 58, écarté ✓.

Enfin, le cas b = 2 a son vocabulaire officiel : **les entiers pairs sont ceux dont le reste modulo 2 vaut 0, les impairs ceux dont le reste vaut 1**. Conséquence utile : **a et a² ont toujours la même parité**, car a = 2k donne a² = 4k² (pair) et a = 2k + 1 donne a² = 4k² + 4k + 1 (impair).

_Exemple détaillé_ — quel est le reste de (n + 1)³ − n³ dans la division par 6 ? On développe : (n + 1)³ − n³ = 3n² + 3n + 1 = **3n(n + 1) + 1**. Or n et n + 1 sont consécutifs, donc n(n + 1) est pair : 3n(n + 1) est un multiple de 6. Le reste vaut donc **1**, pour tout n. _Contrôle_ : n = 1 donne 8 − 1 = 7 = 6 + 1 ✓ ; n = 2 donne 27 − 8 = 19 = 18 + 1 ✓ ; n = 3 donne 64 − 27 = 37 = 36 + 1 ✓.

## 🔮 Congruence modulo n : ranger les entiers par leur reste

Regarde les quatre entiers −19, −129, 124 et 13610, et divise-les par 11 :

| a     | Division euclidienne par 11 | Reste |
| ----- | --------------------------- | ----- |
| −19   | −19 = 11 × (−2) + 3         | 3     |
| −129  | −129 = 11 × (−12) + 3       | 3     |
| 124   | 124 = 11 × 11 + 3           | 3     |
| 13610 | 13610 = 11 × 1237 + 3       | 3     |

_Contrôle_ : 11 × (−2) = −22 et −22 + 3 = −19 ✓ ; 11 × (−12) = −132 et −132 + 3 = −129 ✓ ; 11 × 11 = 121 et 121 + 3 = 124 ✓ ; 11 × 1237 = 13607 et 13607 + 3 = 13610 ✓. Ces quatre nombres n'ont rien en commun **sauf leur reste** — et c'est précisément ce lien qu'on nomme.

> **Définition et notation** — « Soit n un entier naturel non nul et a et b deux entiers. On dit que a est **congru à b modulo n** si **a − b est un multiple de n**. On note alors **a ≡ b (mod n)**. »

> **Théorème et définition** — « Soit n un entier naturel non nul. Pour tout entier a, il existe un **unique** entier r appartenant à {0, …, n − 1} tel que a ≡ r (mod n). On dit que r est le **reste modulo n** de a. »

> **Conséquence** — « Deux entiers sont congrus modulo n **si, et seulement si, ils ont le même reste modulo n**. »

Les quatre nombres du tableau vérifient donc −19 ≡ −129 ≡ 124 ≡ 13610 ≡ 3 (mod 11). Deux cas particuliers à mémoriser : **a ≡ 0 (mod n) signifie exactement « n divise a »**, et a ≡ a (mod n) toujours.

> **Propriétés** — « Soit a, b et c trois entiers et n un entier naturel non nul. • a ≡ a (mod n). • Si a ≡ b (mod n) alors **b ≡ a (mod n)**. • Si a ≡ b (mod n) et b ≡ c (mod n), alors **a ≡ c (mod n)**. »

_Exemple détaillé (cinq affirmations à trancher)_ — on teste chaque fois si la **différence** est un multiple du module :

| Affirmation           | Différence | Multiple du module ?     | Verdict                     |
| --------------------- | ---------- | ------------------------ | --------------------------- |
| 31 ≡ 3 (mod 7)        | 28         | 28 = 7 × 4               | **vrai**                    |
| −31 ≡ 1 (mod 5)       | −32        | 32 n'est pas multiple de 5 | **faux** (−31 ≡ 4 (mod 5)) |
| −2 ≡ 2 (mod 4)        | −4         | −4 = 4 × (−1)            | **vrai**                    |
| 914 ≡ 21 (mod 19)     | 893        | 893 = 19 × 47            | **vrai**                    |
| 914 ≡ −21 (mod 47)    | 935        | 935 = 47 × 19 + 42       | **faux** (914 ≡ 21 (mod 47)) |

_Contrôle de la dernière ligne_ : 47 × 19 = 893 et 914 − 893 = 21, donc le reste de 914 modulo 47 est 21, pas −21 — dont le reste vaut 47 − 21 = 26. La différence entre les deux est 42, non nulle modulo 47 ✓.

> ⚠️ **Congru n'est pas égal.** −2 ≡ 2 (mod 4) est vrai alors que −2 ≠ 2 : la congruence ne compare pas les nombres, elle compare leurs **restes**. Et le module n est toujours un entier naturel **non nul** ; « modulo 0 » n'existe pas.

_Exemple détaillé_ — montrer que (−2)^s et (−2)^(s+1) ont le même reste modulo 3, pour tout entier naturel s. On calcule la différence : (−2)^(s+1) − (−2)^s = (−2)^s × (−2 − 1) = **−3 × (−2)^s**, qui est un multiple de 3 ✓. _Contrôle_ : s = 2 donne 4 et −8, or 4 = 3 × 1 + 1 et −8 = 3 × (−3) + 1 : reste 1 des deux côtés ✓.

## 🧮 Calculer avec les congruences

Tout l'intérêt de la notation tient dans une seule page : **les congruences s'additionnent, se multiplient et s'élèvent à une puissance comme des égalités**.

> **Propriétés (compatibilité avec les opérations)** — « Soit a, b, c et d quatre entiers et n un entier naturel non nul. • Si a ≡ b (mod n) et si c ≡ d (mod n), alors **a + c ≡ b + d (mod n)** et **a × c ≡ b × d (mod n)**. • Si a ≡ b (mod n) alors **ha ≡ hb (mod n)** pour tout entier h et **a^m ≡ b^m (mod n)** pour tout entier m > 0. »

_Exercice résolu_ — **déterminer le reste modulo 17 de 55348932 × 1968755.** Personne ne calcule ce produit : on réduit chaque facteur d'abord.

- 55348932 = 17 × 3255819 + 9, donc 55348932 ≡ **9** (mod 17). _Contrôle_ : 17 × 3255819 = 55348923, et 55348923 + 9 = 55348932 ✓.
- 1968755 = 17 × 115809 + 2, donc 1968755 ≡ **2** (mod 17). _Contrôle_ : 17 × 115809 = 1968753, et 1968753 + 2 = 1968755 ✓.

Le produit vérifie alors 55348932 × 1968755 ≡ 9 × 2 = 18 (mod 17), et 18 ≡ 1 (mod 17). Le reste cherché est **1**.

_Exemple détaillé (une batterie d'expressions)_ — soit a ≡ 3 (mod 15) et b ≡ 11 (mod 15). On remplace, on réduit :

| Expression | Calcul sur les restes | Reste modulo 15 |
| ---------- | --------------------- | --------------- |
| a + b      | 3 + 11 = 14           | **14**          |
| a − b      | 3 − 11 = −8           | **7** (−8 + 15) |
| −a         | −3                    | **12**          |
| ab         | 3 × 11 = 33 = 30 + 3  | **3**           |
| −a²b       | −(9 × 11) = −99       | **6** (−99 + 105) |
| ab²        | 3 × 121               | **3**           |

_Contrôle de la dernière ligne_ : 121 = 15 × 8 + 1, donc b² ≡ 1 et ab² ≡ 3 × 1 = 3 ✓. _Contrôle de l'avant-dernière_ : 99 = 15 × 6 + 9, donc a²b ≡ 9 et −a²b ≡ −9 ≡ 6 (mod 15) ✓ — les deux chemins concordent.

> ⚠️ **On ne simplifie jamais une congruence par un facteur commun.** De 2 × 3 ≡ 2 × 8 (mod 10) — vrai, puisque 16 − 6 = 10 — on ne peut **pas** déduire 3 ≡ 8 (mod 10), qui est faux (la différence 5 n'est pas multiple de 10). La division n'est pas dans la liste des propriétés, et cette ligne coûte des points chaque année.

> ⚠️ **On ne réduit jamais l'exposant modulo n.** De 2 ≡ 2 (mod 3) et 4 ≡ 1 (mod 3), on serait tenté d'écrire 2⁴ ≡ 2¹ (mod 3) : faux, car 2⁴ = 16 ≡ 1 tandis que 2¹ ≡ 2. **L'exposant se réduit modulo la période, pas modulo n** — c'est l'objet de l'avant-dernière section.

## 📐 Les tableaux de congruence : balayer tous les restes

Quand l'énoncé dit « pour tout entier a », il n'y a que n cas à examiner : les n restes possibles. On dresse alors un **tableau de congruence**, et la démonstration devient un balayage fini.

_Exemple détaillé (les restes possibles d'un carré)_ — modulo 6, un entier a a pour reste 0, 1, 2, 3, 4 ou 5. On élève au carré et on réduit :

| Reste de a  | 0   | 1   | 2   | 3   | 4    | 5    |
| ----------- | --- | --- | --- | --- | ---- | ---- |
| a²          | 0   | 1   | 4   | 9   | 16   | 25   |
| Reste de a² | 0   | 1   | 4   | **3** | **4** | **1** |

Les restes possibles de a² modulo 6 sont donc **{0, 1, 3, 4}** : un carré n'est **jamais** congru à 2 ni à 5 modulo 6. _Contrôle_ : 9 = 6 + 3 ✓, 16 = 12 + 4 ✓, 25 = 24 + 1 ✓.

_Exercice résolu_ — **déterminer tous les entiers a et b tels que ab ≡ 1 (mod 6).** On note r et r′ les restes de a et b, et on dresse la table des restes de rr′ :

| × (mod 6) | 0   | 1   | 2   | 3   | 4   | 5     |
| --------- | --- | --- | --- | --- | --- | ----- |
| **0**     | 0   | 0   | 0   | 0   | 0   | 0     |
| **1**     | 0   | 1   | 2   | 3   | 4   | 5     |
| **2**     | 0   | 2   | 4   | 0   | 2   | 4     |
| **3**     | 0   | 3   | 0   | 3   | 0   | 3     |
| **4**     | 0   | 4   | 2   | 0   | 4   | 2     |
| **5**     | 0   | 5   | 4   | 3   | 2   | **1** |

Le chiffre 1 n'apparaît qu'en deux cases : (1, 1) et (5, 5). Donc **ab ≡ 1 (mod 6) ⟺ (a ≡ 1 et b ≡ 1) ou (a ≡ 5 et b ≡ 5) modulo 6**. _Contrôle_ : 5 × 5 = 25 = 24 + 1 ✓ ; 7 × 11 = 77 = 72 + 5, non ✓ cohérent car 7 ≡ 1 mais 11 ≡ 5.

Le même balayage **résout les équations de congruence**, celles qu'aucune division ne saurait résoudre :

| Équation dans ℤ    | Balayage des restes                     | Solutions                       |
| ------------------ | --------------------------------------- | ------------------------------- |
| 2x ≡ 4 (mod 10)    | 2x prend 0, 2, 4, 6, 8, 0, 2, 4, 6, 8   | x ≡ 2 ou x ≡ 7 (mod 10)         |
| 4x ≡ 8 (mod 10)    | 4x prend 0, 4, 8, 2, 6, 0, 4, 8, 2, 6   | x ≡ 2 ou x ≡ 7 (mod 10)         |
| x² ≡ 0 (mod 4)     | carrés modulo 4 : 0, 1, 0, 1            | x ≡ 0 ou x ≡ 2 (mod 4)          |
| x² ≡ 3 (mod 4)     | carrés modulo 4 : 0, 1, 0, 1            | **aucune solution**             |
| x² ≡ 4 (mod 11)    | carrés modulo 11 : 0, 1, 4, 9, 5, 3, 3, 5, 9, 4, 1 | x ≡ 2 ou x ≡ 9 (mod 11) |
| x² ≡ −1 (mod 11)   | −1 ≡ 10, absent de la liste des carrés  | **aucune solution**             |

_Contrôle_ : pour 2x ≡ 4 (mod 10), x = 7 donne 14 − 4 = 10 ✓ ; pour x² ≡ 4 (mod 11), x = 9 donne 81 = 77 + 4 ✓.

> 🗡️ Deux solutions pour 2x ≡ 4 (mod 10), aucune pour x² ≡ 3 (mod 4) : une congruence n'est **ni** une équation ordinaire **ni** garantie d'avoir une solution unique. Le balayage est la seule méthode fiable, et il est court : n cas.

_Exercice résolu (un tableau à trois étages)_ — **déterminer les restes possibles modulo 9 de a⁹ − a.** On écrit a⁹ = (a³)³ et on empile les lignes :

| Reste de a     | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   |
| -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Reste de a³    | 0   | 1   | 8   | 0   | 1   | 8   | 0   | 1   | 8   |
| Reste de a⁹    | 0   | 1   | 8   | 0   | 1   | 8   | 0   | 1   | 8   |
| Reste de a⁹ − a | 0  | 0   | 6   | 6   | 6   | 3   | 3   | 3   | 0   |

_Contrôle de la ligne a³_ : 2³ = 8 ✓ ; 3³ = 27 = 27 + 0 ✓ ; 4³ = 64 = 63 + 1 ✓ ; 5³ = 125 = 117 + 8 ✓ ; 6³ = 216 = 216 + 0 ✓ ; 7³ = 343 = 342 + 1 ✓ ; 8³ = 512 = 504 + 8 ✓. _Contrôle de la ligne a⁹_ : elle se déduit de la précédente puisque 0³ ≡ 0, 1³ ≡ 1 et 8³ ≡ (−1)³ = −1 ≡ 8. Les restes possibles sont donc **{0, 3, 6}** : a⁹ − a est toujours un multiple de 3. _Contrôle numérique_ : a = 2 donne 2⁹ − 2 = 510 = 9 × 56 + 6 ✓ ; a = 5 donne 5⁹ − 5 = 1953120, dont la somme des chiffres 1 + 9 + 5 + 3 + 1 + 2 + 0 = 21 laisse le reste 3 modulo 9 ✓.

## ⚔️ Grandes puissances : la période, puis Fermat

Comment calculer le reste de 247³⁴⁹ modulo 7 sans écrire ce monstre ? En trois gestes, toujours les mêmes.

**Geste 1 — réduire la base.** **Geste 2 — trouver la période des puissances.** **Geste 3 — réduire l'exposant modulo la période.**

_Exercice résolu_ — **reste de 247³⁴⁹ modulo 7.** _Geste 1_ : 247 = 7 × 35 + 2, donc 247 ≡ 2 (mod 7). _Geste 2_ : on liste les puissances de 2 modulo 7 — 2⁰ ≡ 1, 2¹ ≡ 2, 2² ≡ 4, 2³ = 8 ≡ 1. La suite **recommence tous les 3 crans** :

| k modulo 3   | 0   | 1   | 2   |
| ------------ | --- | --- | --- |
| Reste de 2ᵏ  | 1   | 2   | 4   |

_Geste 3_ : 349 = 3 × 116 + 1, donc 349 ≡ 1 (mod 3), et **247³⁴⁹ ≡ 2 (mod 7)**. _Contrôle_ : 7 × 35 = 245 et 245 + 2 = 247 ✓ ; 3 × 116 = 348 et 348 + 1 = 349 ✓ ; 2³ = 8 = 7 + 1 ✓.

_Exercice résolu (le raccourci du −1)_ — **reste de 298³⁴⁹ modulo 13.** On a 298 = 13 × 22 + 12, donc 298 ≡ 12 ≡ **−1** (mod 13). Comme 349 est impair, 298³⁴⁹ ≡ (−1)³⁴⁹ = −1 ≡ **12** (mod 13). _Contrôle_ : 13 × 22 = 286 et 286 + 12 = 298 ✓.

> 🗡️ **Cherche toujours si la base est congrue à −1 ou à 1** : la période tombe alors à 2 ou à 1, et l'exercice se termine en une ligne. Exemples : 50⁹⁹ modulo 7, avec 50 = 49 + 1 ≡ 1, vaut **1** ; et 50⁹⁹ modulo 17, avec 50 = 34 + 16 ≡ −1, vaut **16**.

_Exemple détaillé (le chiffre des unités)_ — le chiffre des unités d'un entier, c'est son reste modulo 10. Or 9 ≡ −1 (mod 10), donc 9²⁰⁰⁷ ≡ (−1)²⁰⁰⁷ = −1 ≡ **9** et 9²⁰⁰⁸ ≡ (−1)²⁰⁰⁸ = **1**. _Contrôle sur de petits exposants_ : 9¹ = 9 ✓, 9² = 81 se termine par 1 ✓, 9³ = 729 se termine par 9 ✓.

_Exemple détaillé (période 4)_ — reste de 5^(202020202041) modulo 13. On a 5² = 25 ≡ −1 (mod 13), donc 5⁴ ≡ 1 : la période vaut 4. Un entier est congru modulo 4 à ses deux derniers chiffres, ici 41 = 40 + 1 ≡ 1 (mod 4). Donc le reste vaut **5**. Avec l'exposant 555555555555, dont les deux derniers chiffres 55 = 52 + 3 donnent 3, le reste vaut 5³ = 125 ≡ **8** (mod 13). _Contrôle_ : 5⁴ = 625 = 13 × 48 + 1 ✓ et 125 = 13 × 9 + 8 ✓.

Reste un théorème qui donne la période **sans la chercher**, quand le module est premier :

> **Théorème de Fermat** — « Pour tout entier naturel a et tout nombre premier p **ne divisant pas a**, **a^(p−1) ≡ 1 (mod p)**. »

_Contrôle du théorème_ : avec p = 7, 2⁶ = 64 = 63 + 1 ≡ 1 ✓ et 3⁶ = 729 = 728 + 1 = 7 × 104 + 1 ≡ 1 ✓.

_Exemple détaillé_ — pour quels entiers a a-t-on a^600 ≡ 1 (mod 7) ? Comme 600 = 6 × 100, on écrit a^600 = (a⁶)^100. Si 7 ne divise pas a, Fermat donne a⁶ ≡ 1, donc a^600 ≡ 1^100 = **1**. Si 7 divise a, alors a^600 ≡ 0. La réponse est donc : **exactement les entiers non divisibles par 7**.

_Exemple détaillé_ — montrer que 7 divise (a³ − 1)(a⁴ + a) pour tout entier naturel a. On factorise : (a³ − 1)(a⁴ + a) = (a³ − 1) × a × (a³ + 1) = **a(a⁶ − 1)**. Si 7 divise a, c'est fini. Sinon Fermat donne a⁶ ≡ 1 (mod 7), donc 7 divise a⁶ − 1 ✓. _Contrôle_ : a = 2 donne (8 − 1)(16 + 2) = 7 × 18 = 126 = 7 × 18 ✓ ; a = 3 donne (27 − 1)(81 + 3) = 26 × 84 = 2184 = 7 × 312 ✓.

> ⚠️ **Fermat exige les deux hypothèses.** Si p n'est pas premier, tout s'effondre : avec p = 6, on aurait 2⁵ ≡ 1 (mod 6), or 2⁵ = 32 = 30 + 2 ≡ 2. Et si p divise a, a^(p−1) ≡ 0, jamais 1.

> 🗡️ Fermat sert aussi à fabriquer des exposants : les **nombres de Fermat** F_n = 2^(2ⁿ) + 1 valent F₀ = 3, F₁ = 5, F₂ = 17, F₃ = 257, F₄ = 65537 — tous premiers. Fermat croyait qu'ils l'étaient tous ; F₅ ne l'est pas, car 641 le divise. _Contrôle de F₃_ : 2^(2³) + 1 = 2⁸ + 1 = 257 ✓.

## 👑 Les critères de divisibilité : la méthode de Pascal

Reste la promesse de l'épigraphe. Pascal l'a formulée ainsi : pour tester la divisibilité par A, il suffit de connaître **les restes des puissances successives de 10 modulo A** — car tout entier s'écrit avec des puissances de 10.

$$ n = c₀ + c₁ × 10 + c₂ × 10² + … donc n ≡ c₀ + c₁ × (reste de 10) + c₂ × (reste de 10²) + … $$

Selon le module, la liste des restes de 10ᵏ est si simple que le critère se lit d'un coup d'œil :

| Module | Restes de 10ᵏ                   | Critère obtenu                                     |
| ------ | ------------------------------- | -------------------------------------------------- |
| 9      | 1, 1, 1, 1, …                   | n ≡ **somme des chiffres** f(n) (mod 9)            |
| 3      | 1, 1, 1, 1, …                   | n ≡ **somme des chiffres** f(n) (mod 3)            |
| 11     | 1, −1, 1, −1, …                 | n ≡ **somme alternée** des chiffres (mod 11)       |
| 4      | 1, 2, 0, 0, …                   | n ≡ ses **deux derniers chiffres** (mod 4)         |
| 111    | 1, 10, 100, 1, 10, 100, …       | n ≡ **somme de ses blocs de 3 chiffres** (mod 111) |

_Justification des lignes 1 et 3_ : 10 ≡ 1 (mod 9) donne 10ᵏ ≡ 1 pour tout k ; 10 ≡ −1 (mod 11) donne 10ᵏ ≡ (−1)ᵏ. _Justification de la ligne 5_ : 1000 = 111 × 9 + 1, donc 1000 ≡ 1 (mod 111) ✓, et les blocs de trois chiffres sont exactement les coefficients des puissances de 1000.

_Exemple détaillé (on liquide la question du premier paragraphe)_ — a = 599873120.

- **Par 4** : ses deux derniers chiffres forment 20 = 4 × 5, donc **4 divise a** — ce que confirme l'écriture a = 4 × 149968280 du début du chapitre ✓.
- **Par 11** : somme alternée depuis les unités, 0 − 2 + 1 − 3 + 7 − 8 + 9 − 9 + 5 = **0**, multiple de 11, donc **11 divise a** — ce que confirme a = −11 × (−54533920) ✓.
- **Par 3** : somme des chiffres 5 + 9 + 9 + 8 + 7 + 3 + 1 + 2 + 0 = **44**, et 44 = 3 × 14 + 2, donc a ≡ 2 (mod 3) : **3 ne divise pas a**, donc 6 non plus. Il **n'existe aucun entier s tel que −a = 6s** ✓. _Contrôle direct_ : 3 × 199957706 = 599873118, et a − 599873118 = 2 ✓.

_Exemple détaillé (les blocs de trois)_ — 111111, 100010001 et 100010000001 sont-ils divisibles par 111 ? On découpe par tranches de trois chiffres depuis la droite et on somme :

- 111111 → 111 + 111 = 222 = 111 × 2 ✓ **divisible**
- 100010001 → 100 + 010 + 001 = 111 ✓ **divisible**
- 100010000001 → 100 + 010 + 000 + 001 = 111 ✓ **divisible**

Aucune division posée, et pourtant les trois réponses sont sûres. _Contrôle du premier_ : 111 × 1001 = 111111 ✓.

Il reste le cas que Pascal citait lui-même, le plus riche : **le module 7**, où les restes des puissances de 10 ne se stabilisent jamais mais **se répètent avec une période de 6**.

::: figure Les restes de 10⁰ à 10⁵ modulo 7 sont tous différents, puis 10⁶ retombe sur 1 et la suite recommence : la période observée par Pascal fait exactement six crans.
<svg viewBox="0 0 500 136"><g fill="none" stroke="#0f172a" stroke-width="1.6"><rect x="14" y="26" width="62" height="46" rx="8"/><rect x="96" y="26" width="62" height="46" rx="8"/><rect x="178" y="26" width="62" height="46" rx="8"/><rect x="260" y="26" width="62" height="46" rx="8"/><rect x="342" y="26" width="62" height="46" rx="8"/><rect x="424" y="26" width="62" height="46" rx="8"/></g><g fill="none" stroke="#0f172a" stroke-width="1.6"><path d="M78 49 H90"/><path d="M160 49 H172"/><path d="M242 49 H254"/><path d="M324 49 H336"/><path d="M406 49 H418"/></g><g fill="#0f172a"><path d="M90 45 L96 49 L90 53 Z"/><path d="M172 45 L178 49 L172 53 Z"/><path d="M254 45 L260 49 L254 53 Z"/><path d="M336 45 L342 49 L336 53 Z"/><path d="M418 45 L424 49 L418 53 Z"/></g><path d="M455 74 C455 104, 45 104, 45 80" fill="none" stroke="#0f6e56" stroke-width="1.8"/><path d="M41 86 L45 76 L49 86 Z" fill="#0f6e56"/><g font-size="14" font-weight="700" text-anchor="middle" fill="#0f172a"><text x="45" y="47">10⁰</text><text x="127" y="47">10¹</text><text x="209" y="47">10²</text><text x="291" y="47">10³</text><text x="373" y="47">10⁴</text><text x="455" y="47">10⁵</text><text x="45" y="65">≡ 1</text><text x="127" y="65">≡ 3</text><text x="209" y="65">≡ 2</text><text x="291" y="65">≡ 6</text><text x="373" y="65">≡ 4</text><text x="455" y="65">≡ 5</text></g><text x="250" y="126" font-size="12" font-weight="700" text-anchor="middle" fill="#0f6e56">10⁶ ≡ 1 (mod 7) : la roue a fait un tour</text></svg>
:::

_Contrôle de la roue_ : 10 = 7 + 3 ✓ ; 100 = 98 + 2 ✓ ; 1000 = 994 + 6 ✓ ; puis chaque cran se déduit du précédent en multipliant par 3 — 6 × 3 = 18 ≡ 4 ✓, 4 × 3 = 12 ≡ 5 ✓, 5 × 3 = 15 ≡ 1 ✓.

_Exemple détaillé_ — reste de 2024 modulo 7 par la méthode de Pascal : 2024 = 2 × 10³ + 0 × 10² + 2 × 10 + 4 ≡ 2 × 6 + 0 + 2 × 3 + 4 = 12 + 6 + 4 = 22 ≡ **1** (mod 7). _Contrôle_ : 7 × 289 = 2023, donc 2024 = 7 × 289 + 1 ✓.

> ⚠️ Pour la somme alternée du critère de 11, **on part des unités**, pas du chiffre de gauche : c'est 10⁰ qui porte le signe +. Commencer par la gauche donne le bon résultat au signe près — donc la bonne conclusion pour la divisibilité, mais un **reste faux** dès qu'on demande le reste.

> 🏆 Seizième porte franchie, héros : tu sais lire un entier par son reste, poser une division euclidienne dans les quatre configurations de signes, balayer un tableau de congruence et dompter une puissance de dix chiffres. Mais une question reste sans outil : quand deux entiers n'ont **aucun** diviseur commun, que peut-on en tirer ? C'est tout le chapitre suivant — PGCD, algorithme d'Euclide et **identité de Bézout**.
