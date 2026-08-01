# ⚔️ Identité de Bézout — la combinaison qui fabrique le PGCD

> 💡 «Deux entiers premiers entre eux ne partagent aucun diviseur — et c'est précisément pour cela qu'on peut fabriquer 1 en les combinant. Tout le chapitre tient dans cette équivalence.»

Dans tout ce chapitre, ℕ désigne l'ensemble des entiers naturels et ℤ celui des entiers relatifs. Tu sais déjà, depuis le chapitre précédent, poser une division euclidienne dans ℤ, manipuler les congruences modulo n et t'en servir pour calculer un reste. Il te manque une seule chose : un outil qui **relie deux entiers entre eux**. Cet outil, c'est le PGCD, et son point culminant est une égalité découverte par Bachet de Méziriac et popularisée par Bézout au XVIIIᵉ siècle : quand a et b sont premiers entre eux, on peut toujours écrire **au + bv = 1**. C'est ce qui fait marcher les inverses modulaires, les équations en nombres entiers — et le chiffrement RSA, dont la clé de déchiffrement se calcule exactement par cette identité.

Notation du chapitre : **a ∧ b** désigne le PGCD de a et b, **a ∨ b** leur PPCM.

## 🏰 Le PGCD et l'algorithme d'Euclide

Deux entiers non nuls ont toujours des diviseurs communs (au moins 1 et −1) et ces diviseurs sont en nombre fini. Le plus grand d'entre eux mérite un nom, et surtout une caractérisation utilisable.

> **Théorème et définition (PGCD)** — « Si a et b sont deux entiers non nuls, alors il existe un unique entier naturel d qui vérifie les deux conditions suivantes : 1. d divise a et d divise b, 2. Si un entier k divise a et b alors il divise d. L'entier d défini plus haut est noté a ∧ b et appelé le plus grand commun diviseur de a et b. »

La condition 2 est la vraie définition : a ∧ b n'est pas seulement le plus grand, c'est celui que **tous les autres divisent**. C'est cette forme qu'on utilise dans les démonstrations.

> **Conséquences** — « Pour tous entiers a et b non nuls, a ∧ b > 0. Pour tous entiers a et b non nuls, a ∧ b = |a| ∧ |b|. »

Les signes ne comptent donc jamais : on travaille sur les valeurs absolues.

> **Propriétés** — « Soit a et b deux entiers non nuls. • Si b divise a alors a ∧ b = |b|. • Si b ne divise pas a et si r est le reste modulo b de a alors a ∧ b = b ∧ r. • a ∧ b = b ∧ a. • Pour tout entier non nul k, ka ∧ kb = |k|(a ∧ b). • a ∧ (b ∧ c) = (a ∧ b) ∧ c. »

La deuxième propriété est un moteur : elle **remplace le couple (a, b) par un couple plus petit (b, r)**, et on recommence. Les restes décroissent strictement, donc le procédé s'arrête. C'est l'**algorithme d'Euclide**, et le PGCD est le **dernier reste non nul**.

_Exemple détaillé_ — calculons 4851 ∧ 616 en enchaînant les divisions euclidiennes :

$$ 4851 = 616 × 7 + 539 ; 616 = 539 × 1 + 77 ; 539 = 77 × 7 + 0 $$

Le dernier reste non nul est 77, donc **4851 ∧ 616 = 77**. _Contrôle_ — 4851 = 77 × 63 et 616 = 77 × 8 : 77 divise bien les deux ✓. De plus 63 = 3² × 7 et 8 = 2³ n'ont aucun facteur commun, donc on ne peut pas faire mieux ✓.

_Exemple détaillé (avec un signe)_ — 462 ∧ (−1155) = 462 ∧ 1155. On divise : 1155 = 462 × 2 + 231, puis 462 = 231 × 2 + 0. D'où **462 ∧ (−1155) = 231**. _Contrôle_ — 462 = 231 × 2 et 1155 = 231 × 5 ✓, et 2 ∧ 5 = 1 ✓.

Le PGCD sert aussi quand les entiers dépendent d'un paramètre : on ne calcule plus, on **combine**. Tout diviseur commun de a et b divise αa + βb, pour tous entiers α et β.

_Exemple détaillé_ — pour tout entier n, on pose a = n − 2 et b = 3n + 1 (avec a et b non nuls). Soit d un diviseur commun de a et b. Alors d divise 3a = 3n − 6, donc d divise b − 3a = (3n + 1) − (3n − 6) = **7**. Comme 7 est premier, d ∈ {1, 7} et a ∧ b vaut 1 ou 7. Et a ∧ b = 7 si et seulement si 7 divise n − 2, c'est-à-dire **n ≡ 2 (mod 7)** ; sinon a ∧ b = 1. _Contrôle sur trois valeurs_ — n = 9 (≡ 2 mod 7) : a = 7, b = 28, PGCD 7 ✓. n = 16 (≡ 2 mod 7) : a = 14, b = 49, PGCD 7 ✓. n = 3 : a = 1, b = 10, PGCD 1 ✓.

> 🗡️ Pour un PGCD de deux expressions en n, cherche la **combinaison qui élimine n**. Ici 3a et b : le coefficient 3 devant n dans b impose de multiplier a par 3. Le résultat obtenu (7) borne toutes les valeurs possibles du PGCD.

## ⚡ Entiers premiers entre eux et lemme de Gauss

> **Définition** — « Deux entiers non nuls a et b sont dits premiers entre eux, si a ∧ b = 1. »

Attention : « premiers entre eux » ne veut pas dire « premiers ». 8 et 9 sont premiers entre eux sans qu'aucun des deux ne soit premier.

> **Théorème** — « Soit a et b deux entiers non nuls. Alors il existe un unique couple d'entiers (a′, b′) tel que a = (a ∧ b)a′, b = (a ∧ b)b′ et a′ ∧ b′ = 1. »

Autrement dit : on peut toujours **mettre le PGCD en facteur** et ce qui reste est premier entre eux. C'est la réduction de départ de presque tout exercice.

_Exemple détaillé_ — a = −60 et b = 84. On a 84 = 60 × 1 + 24, 60 = 24 × 2 + 12, 24 = 12 × 2 + 0, donc a ∧ b = 12. Alors a′ = −60/12 = **−5** et b′ = 84/12 = **7**. _Contrôle_ — 12 × (−5) = −60 ✓, 12 × 7 = 84 ✓ et (−5) ∧ 7 = 5 ∧ 7 = 1 ✓.

> **Lemme de Gauss** — « Soit a, b et c trois entiers non nuls. Si a ∧ b = 1 et a divise bc alors a divise c. »

C'est le théorème le plus utilisé du chapitre. Il autorise la seule « simplification » légitime en arithmétique : si a divise un produit et qu'il est premier avec l'un des facteurs, il divise l'autre.

_Exemple détaillé_ — 7 divise 5n. Comme 7 ∧ 5 = 1, le lemme de Gauss donne **7 divise n**. _Contre-exemple qui montre l'importance de l'hypothèse_ — 6 divise 4 × 3 = 12, mais 6 ne divise ni 4 ni 3 : ici 6 ∧ 4 = 2 ≠ 1, le lemme ne s'applique pas.

> **Théorème** — « Soit a et b deux entiers naturels non nuls et n un entier. Si a ∧ b = 1, n ≡ 0 (mod a) et n ≡ 0 (mod b) alors n ≡ 0 (mod ab). »

_Exemple détaillé_ — déterminons le reste de 129286 modulo 221, sachant que 221 = 13 × 17. On a 129285 = 13 × 9945, donc 129286 ≡ 1 (mod 13) ; et 129285 = 17 × 7605, donc 129286 ≡ 1 (mod 17). L'entier n = 129286 − 1 est donc divisible par 13 et par 17, qui sont premiers entre eux : il est divisible par 221. **129286 ≡ 1 (mod 221).** _Contrôle_ — 129285 = 221 × 585 ✓.

> ⚠️ L'hypothèse a ∧ b = 1 n'est pas décorative. Un entier divisible par 4 **et** par 6 n'est pas forcément divisible par 24 : 12 l'est par 4 et par 6, pas par 24. En revanche, divisible par 4 et par 9 ⇒ divisible par 36, car 4 ∧ 9 = 1.

Ce théorème règle aussi les équations **homogènes**. Pour ax + by = 0 avec d = a ∧ b, a = da′, b = db′ : l'équation devient a′x = −b′y ; a′ divise b′y et a′ ∧ b′ = 1, donc a′ divise y, disons y = −a′k, d'où x = b′k.

_Exemple détaillé_ — 21x + 35y = 0. Ici 21 ∧ 35 = 7, a′ = 3, b′ = 5 : les solutions sont les couples **(5k, −3k), k ∈ ℤ**. _Contrôle sur deux valeurs_ — k = 1 : 21 × 5 + 35 × (−3) = 105 − 105 = 0 ✓ ; k = −2 : 21 × (−10) + 35 × 6 = −210 + 210 = 0 ✓.

## 🧮 Le PPCM, le miroir du PGCD

> **Théorème et définition (PPCM)** — « Pour tous entiers a et b non nuls il existe un unique entier m strictement positif qui vérifie les deux conditions suivantes. • m est un multiple de a et b, • tout multiple commun de a et b est un multiple de m. L'entier m ainsi défini est le plus petit commun multiple de a et b et est noté a ∨ b. »

> **Conséquences** — « • Pour tous entiers a et b non nuls, a ∨ b = |a| ∨ |b|. • Pour tous entiers a et b non nuls, (a ∨ b) × (a ∧ b) = |ab|. »

La seconde égalité est la formule de travail : **on calcule le PGCD par Euclide, puis on en déduit le PPCM**, jamais l'inverse.

> **Propriétés** — « Soit a et b deux entiers non nuls. • Si b divise a alors a ∨ b = |a|. • Pour tout entier non nul k, ka ∨ kb = |k|(a ∨ b). • a ∨ b = b ∨ a. • a ∨ (b ∨ c) = (a ∨ b) ∨ c. »

_Exemple détaillé_ — a = 495 et b = 2541. Euclide : 2541 = 495 × 5 + 66 ; 495 = 66 × 7 + 33 ; 66 = 33 × 2 + 0, donc **a ∧ b = 33**. Puis a ∨ b = (495 × 2541)/33 = 495 × 77 = **38115**. _Contrôle_ — 38115/495 = 77 ✓ et 38115/2541 = 15 ✓ : c'est bien un multiple commun. Et 77 ∧ 15 = 1, donc on ne peut pas descendre plus bas ✓.

_Exemple détaillé (un système)_ — cherchons les entiers a et b tels que ab = −1176 et a ∨ b = 84. De (a ∨ b)(a ∧ b) = |ab| on tire a ∧ b = 1176/84 = **14**. On écrit alors a = 14a′, b = 14b′ avec a′ ∧ b′ = 1 ; l'égalité ab = −1176 donne 196 a′b′ = −1176, soit a′b′ = **−6**. Les couples d'entiers premiers entre eux de produit −6 sont (1, −6), (−6, 1), (−1, 6), (6, −1), (2, −3), (−3, 2), (−2, 3), (3, −2). _Contrôle sur un couple_ — a′ = 2, b′ = −3 donnent a = 28 et b = −42 : ab = −1176 ✓, 28 ∧ 42 = 14 ✓ et 28 ∨ 42 = 1176/14 = 84 ✓.

Enfin, l'ensemble des multiples d'un entier a se note **aℤ = {aq, q ∈ ℤ}**. Dire que n est multiple commun de a et b, c'est dire que n appartient à aℤ ∩ bℤ — et ce dernier ensemble est exactement (a ∨ b)ℤ.

## 🔮 Inverses modulo b

Dans ℤ, seuls 1 et −1 sont inversibles. Modulo b, beaucoup plus d'entiers le deviennent — et le critère est justement d'être premier avec b.

> **Théorème (inverse modulo b)** — « Soit a et b deux entiers naturels non nuls tels que b ≥ 2 et a ∧ b = 1. Alors il existe un unique entier non nul u appartenant à {0, 1, ..., b − 1} tel que au ≡ 1 (mod b). On dit que u est un inverse de a modulo b. »

_Exemple détaillé_ — déterminons un inverse de 4 modulo 13. On cherche u tel que 4u soit congru à 1 : la division 40 = 3 × 13 + 1 donne directement **u = 10**. Les solutions dans ℤ de 4x ≡ 1 (mod 13) sont donc les x ≡ 10 (mod 13), c'est-à-dire **x = 10 + 13k, k ∈ ℤ**. _Contrôle sur deux valeurs_ — x = 10 : 4 × 10 = 40 = 3 × 13 + 1 ✓ ; x = 23 : 4 × 23 = 92 = 7 × 13 + 1 ✓.

_Suite — réduire d'abord._ Résolvons 43x ≡ 1 (mod 13). Comme 43 = 3 × 13 + 4, on a 43 ≡ 4 (mod 13), donc l'équation équivaut à 4x ≡ 1 (mod 13) : mêmes solutions **x = 10 + 13k**. _Contrôle_ — x = 10 : 43 × 10 = 430 = 33 × 13 + 1 ✓ (429 = 33 × 13).

_Exemple détaillé (second membre quelconque)_ — 5x ≡ 2 (mod 17). Un inverse de 5 modulo 17 est 7, car 5 × 7 = 35 = 2 × 17 + 1. On multiplie les deux membres par 7 : x ≡ 14 (mod 17). **Solutions : x = 14 + 17k, k ∈ ℤ.** _Contrôle sur deux valeurs_ — x = 14 : 5 × 14 = 70 = 4 × 17 + 2 ✓ ; x = 31 : 5 × 31 = 155 = 9 × 17 + 2 ✓.

> ⚠️ Si a ∧ b ≠ 1, a n'a **aucun** inverse modulo b. Il n'existe pas d'entier u tel que 6u ≡ 1 (mod 9) : tout multiple de 6 est multiple de 3, donc 6u − 1 n'est jamais divisible par 3, encore moins par 9. Vérifie toujours a ∧ b = 1 **avant** de chercher un inverse.

## 👑 L'identité de Bézout et l'algorithme d'Euclide étendu

> **Théorème (Identité de Bezout)** — « Deux entiers non nuls a et b sont premiers entre eux, si et seulement si, il existe deux entiers u et v tels que au + bv = 1. »

Le sens direct fabrique l'égalité ; le sens réciproque est immédiat et redoutablement utile : **s'il existe une seule combinaison au + bv qui vaille 1, alors a ∧ b = 1**. En effet, a ∧ b divise a et b, donc au + bv = 1, donc il divise 1.

> **Corollaire** — « Soit a et b deux entiers non nuls et d = a ∧ b. Alors il existe deux entiers u et v tels que au + bv = d. »

> ⚠️ Le corollaire n'est **pas** une équivalence : de au + bv = d on ne peut conclure que d est le PGCD, seulement que a ∧ b divise d. Ainsi 4 × 2 + 6 × 1 = 14, et pourtant 4 ∧ 6 = 2, pas 14. Seul le cas d = 1 donne une équivalence — c'est tout l'intérêt du théorème de Bézout.

**Comment trouver le couple (u, v) ?** En remontant les divisions d'Euclide : on exprime le dernier reste non nul à l'aide des deux précédents, puis on remplace de proche en proche.

_Exemple détaillé (la remontée)_ — cherchons u et v tels que 51u + 22v = 1. Euclide d'abord : 51 = 22 × 2 + 7 ; 22 = 7 × 3 + 1 ; 7 = 1 × 7 + 0. Le PGCD vaut 1, l'identité existe. On remonte :

$$ 1 = 22 − 3 × 7 = 22 − 3 × (51 − 2 × 22) = 7 × 22 − 3 × 51 $$

D'où **u = −3 et v = 7**. _Contrôle par réinjection_ — 51 × (−3) + 22 × 7 = −153 + 154 = 1 ✓.

Pour de plus grands nombres, la remontée devient pénible. On lui préfère le **tableau de l'algorithme d'Euclide étendu**, qui descend une seule fois. On y suit trois colonnes (r, u, v) avec la propriété invariante **r = au + bv**, initialisées par (a, 1, 0) et (b, 0, 1) ; à chaque division de quotient q, la nouvelle ligne est l'ancienne avant-dernière moins q fois la dernière, colonne par colonne.

_Exemple détaillé (le tableau)_ — a = 2015 et b = 2007.

| division euclidienne | q   | r    | u    | v    | contrôle r = 2015u + 2007v |
| -------------------- | --- | ---- | ---- | ---- | -------------------------- |
| —                    | —   | 2015 | 1    | 0    | 2015 ✓                     |
| —                    | —   | 2007 | 0    | 1    | 2007 ✓                     |
| 2015 = 2007 × 1 + 8  | 1   | 8    | 1    | −1   | 2015 − 2007 = 8 ✓          |
| 2007 = 8 × 250 + 7   | 250 | 7    | −250 | 251  | −503750 + 503757 = 7 ✓     |
| 8 = 7 × 1 + 1        | 1   | 1    | 251  | −252 | 505765 − 505764 = 1 ✓      |
| 7 = 1 × 7 + 0        | 7   | 0    | —    | —    | on s'arrête                |

Le dernier reste non nul est 1 : 2015 ∧ 2007 = 1, et la ligne correspondante livre **2015 × 251 + 2007 × (−252) = 1**. _Contrôle final_ — 251 × 2015 = 505765 et 252 × 2007 = 505764 : la différence vaut bien 1 ✓. _Second contrôle, par la remontée_ — 1 = 8 − 7 = 8 − (2007 − 250 × 8) = 251 × 8 − 2007 = 251 × (2015 − 2007) − 2007 = 251 × 2015 − 252 × 2007 ✓. Les deux méthodes donnent le même couple.

_Exemple détaillé (le corollaire, d ≠ 1)_ — a = 391 et b = 323. Euclide : 391 = 323 × 1 + 68 ; 323 = 68 × 4 + 51 ; 68 = 51 × 1 + 17 ; 51 = 17 × 3 + 0, donc **391 ∧ 323 = 17**. Remontée : 17 = 68 − 51 = 68 − (323 − 4 × 68) = 5 × 68 − 323 = 5 × (391 − 323) − 323, d'où

$$ 391 × 5 − 323 × 6 = 17 $$

_Contrôle_ — 1955 − 1938 = 17 ✓. On en déduit gratuitement une solution de 391x − 323y = 204 : comme 204 = 17 × 12, il suffit de multiplier par 12, ce qui donne **(60, 72)**. _Contrôle_ — 391 × 60 − 323 × 72 = 23460 − 23256 = 204 ✓.

> 🗡️ Le couple (u, v) n'est **jamais unique** : si au + bv = d, alors a(u + b/d) + b(v − a/d) = d aussi. Une correction qui affiche un autre couple que le tien n'est pas forcément en désaccord — réinjecte, c'est le seul juge.

## 📐 Les équations ax + by = c

> **Théorème** — « Soit a, b et c trois entiers et d = a ∧ b. L'équation ax + by = c admet des solutions dans ℤ × ℤ, si et seulement si, d divise c. »

Le sens « si d ne divise pas c, pas de solution » est immédiat : d divise ax + by pour tous x et y, donc il devrait diviser c. Le sens réciproque est exactement le corollaire de Bézout : on écrit au + bv = d, on multiplie par c/d, et on tient une solution.

La résolution complète suit toujours les **quatre mêmes étapes** :

| étape | ce qu'on fait                                     | outil                                      |
| ----- | ------------------------------------------------- | ------------------------------------------ |
| 1     | calculer d = a ∧ b et tester si d divise c        | algorithme d'Euclide                       |
| 2     | diviser toute l'équation par d                    | on obtient a′x + b′y = c′ avec a′ ∧ b′ = 1 |
| 3     | trouver une solution particulière (x₀, y₀)        | Bézout, puis multiplication par c′         |
| 4     | soustraire et conclure : a′(x − x₀) = −b′(y − y₀) | lemme de Gauss                             |

_Exemple détaillé (le cas de base)_ — résolvons 7x + 11y = 1. On a 7 ∧ 11 = 1, donc il y a des solutions. Une solution particulière saute aux yeux : 7 × 8 = 56 et 11 × 5 = 55, donc **(x₀, y₀) = (8, −5)**, et 56 − 55 = 1 ✓. Pour la forme générale, on soustrait les deux égalités :

$$ 7(x − 8) + 11(y + 5) = 0 $$

Donc 7(x − 8) = −11(y + 5). L'entier 7 divise 11(y + 5) et 7 ∧ 11 = 1 : par le **lemme de Gauss**, 7 divise y + 5, soit y + 5 = 7k avec k ∈ ℤ. En reportant, 7(x − 8) = −77k, donc x − 8 = −11k. L'ensemble des solutions est

$$ S = {(8 − 11k, −5 + 7k), k ∈ ℤ} $$

_Contrôle sur trois valeurs du paramètre_ — k = 0 : 7 × 8 + 11 × (−5) = 56 − 55 = 1 ✓ ; k = 1 : 7 × (−3) + 11 × 2 = −21 + 22 = 1 ✓ ; k = −1 : 7 × 19 + 11 × (−12) = 133 − 132 = 1 ✓.

_Suite — changer le second membre._ Pour 7x + 11y = 2, on multiplie la solution particulière par 2 : (16, −10), et 112 − 110 = 2 ✓. Les solutions sont **(16 − 11k, −10 + 7k)**. _Contrôle_ — k = 1 : 7 × 5 + 11 × (−3) = 35 − 33 = 2 ✓ ; k = 2 : 7 × (−6) + 11 × 4 = −42 + 44 = 2 ✓. Le **pas** (−11, 7) ne dépend que de a et b, jamais de c : seul le point de départ change.

Géométriquement, les solutions d'une équation ax + by = c sont les points à coordonnées entières situés sur une droite — et ils y sont régulièrement espacés.

::: figure Les solutions entières de 2x + 3y = 1 sont les points à coordonnées entières de la droite d'équation 2x + 3y = 1 ; on passe de chacune à la suivante par le même pas (−3, 2), d'où la forme (2 − 3k, −1 + 2k).
<svg viewBox="0 0 265 205"><path d="M25 20V180 M45 20V180 M65 20V180 M85 20V180 M105 20V180 M145 20V180 M165 20V180 M185 20V180 M205 20V180 M225 20V180 M245 20V180 M25 20H245 M25 40H245 M25 60H245 M25 80H245 M25 120H245 M25 140H245 M25 160H245 M25 180H245" fill="none" stroke="#cbd5e1" stroke-width="0.8"/><path d="M25 100H245 M125 20V180" fill="none" stroke="#0f172a" stroke-width="1.6"/><path d="M25 26.67 L245 173.33" fill="none" stroke="#0f6e56" stroke-width="2.4"/><path d="M165 120 L113.32 85.55" fill="none" stroke="#b45309" stroke-width="2" stroke-dasharray="5 4"/><path d="M105 80 L115.54 82.22 L111.10 88.88 Z" fill="#b45309"/><g fill="#0f172a"><circle cx="225" cy="160" r="4"/><circle cx="165" cy="120" r="4"/><circle cx="105" cy="80" r="4"/><circle cx="45" cy="40" r="4"/></g><g font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="222" y="177" text-anchor="middle" fill="#0f172a">(5, −3)</text><text x="182" y="137" text-anchor="middle" fill="#0f172a">(2, −1)</text><text x="86" y="72" text-anchor="middle" fill="#0f172a">(−1, 1)</text><text x="62" y="32" text-anchor="middle" fill="#0f172a">(−4, 3)</text><text x="163" y="94" text-anchor="middle" fill="#b45309">(−3, 2)</text><text x="68" y="22" text-anchor="middle" fill="#0f6e56">2x + 3y = 1</text><text x="252" y="112" text-anchor="middle" fill="#0f172a">x</text><text x="134" y="27" text-anchor="middle" fill="#0f172a">y</text></g></svg>
:::

_Exemple détaillé (le cas d ≠ 1)_ — résolvons 46x + 115y = a selon les valeurs de l'entier a. Euclide : 115 = 46 × 2 + 23 ; 46 = 23 × 2 + 0, donc **46 ∧ 115 = 23**. L'équation a des solutions **si et seulement si 23 divise a**.

- **a = 15** : 23 ne divise pas 15, donc **aucune solution**.
- **a = 23** : on divise tout par 23 et on obtient 2x + 5y = 1. Une solution particulière : (3, −1), car 6 − 5 = 1 ✓. Puis 2(x − 3) = −5(y + 1) ; comme 2 ∧ 5 = 1, Gauss donne y + 1 = 2k, puis x − 3 = −5k. **S = {(3 − 5k, −1 + 2k), k ∈ ℤ}.** _Contrôle sur trois valeurs_ — k = 0 : 46 × 3 + 115 × (−1) = 138 − 115 = 23 ✓ ; k = 1 : 46 × (−2) + 115 × 1 = −92 + 115 = 23 ✓ ; k = −1 : 46 × 8 + 115 × (−3) = 368 − 345 = 23 ✓.
- **a = 230 = 23 × 10** : on multiplie la solution particulière par 10, soit (30, −10), le pas restant (−5, 2). **S = {(30 − 5k, −10 + 2k), k ∈ ℤ}.** _Contrôle sur deux valeurs_ — k = 0 : 1380 − 1150 = 230 ✓ ; k = 2 : 46 × 20 + 115 × (−6) = 920 − 690 = 230 ✓.

> ⚠️ Le pas de la solution générale se calcule **après** division par d : il vaut (−b/d, a/d), et non (−b, a). Pour 46x + 115y = 23, écrire (3 − 115k, −1 + 46k) ne donne qu'une partie des solutions — on en rate 22 sur 23. Divise d'abord, paramètre ensuite.

_Suite — quand l'équation n'est pas du premier degré._ Une équation en nombres entiers qui contient des carrés ne se traite **pas** par Bézout : on la **factorise**, et le produit obtenu ne laisse plus qu'un nombre fini de cas. Trois gestes : ramener l'équation à un **produit de deux facteurs entiers** égal à un entier connu, **énumérer les couples de diviseurs** de cet entier — les négatifs compris —, puis **résoudre chaque système** et ne garder que les couples **entiers**. La **parité** élimine souvent la moitié des cas : deux facteurs dont la somme est paire sont de même parité.

_Exemple détaillé_ — résolvons x² − y² = 12 dans ℤ × ℤ. On factorise : **(x − y)(x + y) = 12**. La somme des deux facteurs vaut (x − y) + (x + y) = 2x, elle est paire, donc les deux facteurs sont de même parité ; leur produit 12 étant pair, ils sont tous deux **pairs**. Restent les couples (x − y, x + y) ∈ {(2, 6), (6, 2), (−2, −6), (−6, −2)}. Le couple (2, 6) donne 2x = 2 + 6 = 8 puis x = 4, et 2y = 6 − 2 = 4 puis y = 2. En traitant les trois autres de même : **S = {(4, 2), (4, −2), (−4, 2), (−4, −2)}**. _Contrôle par réinjection des quatre couples_ — seuls des carrés interviennent, donc les quatre donnent le même calcul : 4² − 2² = 16 − 4 = 12 ✓. _Contrôle des cas écartés_ — le couple (1, 12) donnerait 2x = 13, donc x = 6,5, qui n'est pas entier ✓ ; le couple (3, 4) donnerait 2x = 7, non entier lui aussi ✓. C'est bien la parité qui les condamne, et non un calcul de plus.

## 🛡️ Deux congruences à la fois

Un système {x ≡ a (mod m), x ≡ b (mod n)} avec m ∧ n = 1 se résout entièrement avec ce qui précède : on paramètre la première congruence, on l'injecte dans la seconde, et on résout une congruence linéaire par inverse. C'est le cas particulier du théorème des restes chinois que le programme demande.

_Exemple détaillé_ — résolvons {x ≡ 6 (mod 9), x ≡ 8 (mod 11)}. On a 9 ∧ 11 = 1, donc le système a des solutions. La première congruence s'écrit **x = 6 + 9t**, t ∈ ℤ. On reporte dans la seconde : 6 + 9t ≡ 8 (mod 11), soit 9t ≡ 2 (mod 11). Un inverse de 9 modulo 11 est 5, car 9 × 5 = 45 = 4 × 11 + 1 ✓. En multipliant par 5 : t ≡ 10 (mod 11), soit t = 10 + 11s. D'où

$$ x = 6 + 9(10 + 11s) = 96 + 99s, s ∈ ℤ $$

Les solutions sont donc les **x ≡ 96 (mod 99)**. _Contrôle sur deux valeurs_ — x = 96 : 96 = 9 × 10 + 6, reste 6 modulo 9 ✓, et 96 = 11 × 8 + 8, reste 8 modulo 11 ✓. x = 195 : 195 = 9 × 21 + 6 ✓ et 195 = 11 × 17 + 8 ✓.

Le module de la conclusion est 99 = 9 × 11 : c'est le théorème de la section 2 qui le garantit, puisque 9 et 11 sont premiers entre eux. Si les modules ne l'étaient pas, le système pourrait être **impossible** — {x ≡ 1 (mod 4), x ≡ 2 (mod 6)} n'a aucune solution, car x devrait être impair d'après la première et pair d'après la seconde.

> 🏆 Dix-septième porte franchie, héros : tu sais dérouler l'algorithme d'Euclide, le remonter pour fabriquer une identité de Bézout, inverser un entier modulo un autre, décider en une ligne si une équation ax + by = c a des solutions et les décrire toutes, et faire tenir deux congruences ensemble. Et surtout, tu as pris le réflexe qui sauve à l'examen : **tout couple de Bézout se réinjecte dans au + bv = d, toute solution générale se teste sur deux valeurs du paramètre**. Avec ce chapitre s'achève le socle d'arithmétique du programme — celui-là même qui, à la fin, fait tourner le chiffrement RSA.
