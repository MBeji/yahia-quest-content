# ⚔️ Arithmétique — Euclide et le secret des restes

> 💡 «Deux nombres cachent un diviseur commun que personne ne voit : l'algorithme d'Euclide le fait sortir en quelques divisions, sans jamais factoriser. Il a vingt-trois siècles, et ton programme le fait tourner en une boucle.»

Bienvenue, héros de la section Sciences de l'informatique. Ici, plus de courbes ni de limites : on ne manipule que des entiers, et une seule question revient, que reste-t-il quand on divise ? Huit étapes t'y conduisent : multiples et diviseurs, division euclidienne, congruences, calcul avec les congruences, critères de divisibilité (et clé ISBN), PGCD et algorithme d'Euclide, théorème de Bézout, lemme de Gauss et équations ax + by = c. Chaque algorithme du chapitre se programme en quelques lignes.

## 🧮 Multiples et diviseurs dans ℤ

Un magasin range 24 chaises en rangées de même longueur : 6 chaises par rangée font 4 rangées, mais 5 par rangée est impossible.
Quelles longueurs de rangée conviennent, et que devient la réponse dans ℤ, où les nombres peuvent être négatifs ou nuls ?

::: definition
Soient a et b deux entiers relatifs. **a est un multiple de b** s'il existe un entier relatif k tel que a = kb.

Si b ≠ 0, on dit aussi que **b divise a** (ou que a est divisible par b), et l'on note b | a.
:::

::: exemple Les diviseurs de 24
1. 24 = 1 × 24 = 2 × 12 = 3 × 8 = 4 × 6 : les diviseurs positifs sont 1, 2, 3, 4, 6, 8, 12 et 24.
2. Chaque égalité 24 = d × k s'écrit aussi 24 = (−d) × (−k) : si d divise 24, alors −d divise 24.
3. Dans ℤ, les diviseurs de 24 sont donc ±1, ±2, ±3, ±4, ±6, ±8, ±12 et ±24, soit 16 diviseurs.
4. Un diviseur d de a ≠ 0 vérifie −|a| ≤ d ≤ |a| (un multiple non nul de d a une valeur absolue au moins égale à |d|), donc la liste est finie.

:::

::: piege Traiter 0 comme un entier ordinaire
**Erreur : écrire « 5 ne divise pas 0 » ou « 0 divise 0 ».** Cela tente parce que 0 est plus petit que 5 et que 0 = 0 × 0 ressemble à une division. Mais 0 = 5 × 0 est bien de la forme kb, donc 5 divise 0 ; plus généralement, tout entier non nul divise 0. En revanche, 0 ne divise aucun entier, pas même 0, car la définition exige b ≠ 0.
:::

::: propriete
Soient a, b et c des entiers non nuls.

- Si a divise b et b divise a, alors a = b ou a = −b.
- Si a divise b et b divise c, alors a divise c (transitivité).
- Si a divise b et a divise c, alors a divise nb + mc pour tous entiers relatifs n et m.

Cas limite : « a = b ou a = −b » ne donne pas toujours a = b : 3 divise −3 et −3 divise 3, sans que 3 = −3.
:::

::: exemple Les entiers n tels que n + 3 divise 3n + 7
1. On fait apparaître le diviseur : 3n + 7 = 3(n + 3) − 2.
2. Si n + 3 divise 3n + 7, il divise aussi 3n + 7 − 3(n + 3) = −2 (combinaison linéaire de 3n + 7 et de n + 3).
3. Réciproquement, si n + 3 divise 2, il divise 3(n + 3) − 2 = 3n + 7. Donc n + 3 divise 3n + 7 si et seulement si n + 3 divise 2.
4. Les diviseurs de 2 sont −2, −1, 1 et 2, d'où n ∈ {−5 ; −4 ; −2 ; −1}.
5. Contrôle : pour n = −4, n + 3 = −1 et 3n + 7 = −5 ; −1 divise −5 ✓.

:::

::: verifie
Trouve tous les entiers n tels que n − 1 divise n + 5.

---

n + 5 = (n − 1) + 6, donc n − 1 divise n + 5 si et seulement si n − 1 divise 6 : on a retiré le multiple de n − 1 par combinaison linéaire. Les diviseurs de 6 sont ±1, ±2, ±3 et ±6, donc n − 1 prend ces huit valeurs et n ∈ {−5 ; −2 ; −1 ; 0 ; 2 ; 3 ; 4 ; 7}. Contrôle : n = 7 donne 6 | 12 ✓.
:::

::: retenir
b divise a si a = kb avec k entier (b ≠ 0) ; les diviseurs vont par paires ±, tout entier non nul divise 0, et pour « n − c divise une expression en n », on retire un multiple de n − c pour se ramener à un diviseur d'un entier fixé.
:::

## ✂️ La division euclidienne : un quotient, un reste

Une salle de cinéma compte 12 places par rangée et accueille 487 spectateurs : combien de rangées pleines, et combien de personnes dans la dernière ?
Ce partage est clair pour des entiers positifs. Mais que valent le quotient et le reste de −487 par 12, ou d'un nombre divisé par un diviseur négatif ?

::: definition
**Théorème (admis).** Soient a un entier relatif et b un entier relatif non nul. Il existe un unique couple (q ; r) d'entiers relatifs tel que

$$ a = bq + r et 0 ≤ r < |b| $$

Effectuer la **division euclidienne** de a (le dividende) par b (le diviseur), c'est trouver ce couple : q est le **quotient** et r le **reste**.
:::

::: exemple La salle de cinéma : 487 par 12, puis −487 par 12
1. 12 × 40 = 480 ≤ 487 < 492 = 12 × 41, donc q = 40 et r = 487 − 480 = 7, avec 0 ≤ 7 < 12 : 487 = 12 × 40 + 7.
2. Pour −487, on encadre entre deux multiples consécutifs de 12 : −492 ≤ −487 < −480, car 12 × (−41) = −492.
3. Le quotient est le multiple en dessous : q = −41, et r = −487 − 12 × (−41) = −487 + 492 = 5.
4. Contrôle : 12 × (−41) + 5 = −492 + 5 = −487 ✓ et 0 ≤ 5 < 12 ✓.

:::

| a   | b   | q   | r   | Écriture            |
| --- | --- | --- | --- | ------------------- |
| 25  | 4   | 6   | 1   | 25 = 4 × 6 + 1      |
| 25  | −4  | −6  | 1   | 25 = (−4)(−6) + 1   |
| −25 | 4   | −7  | 3   | −25 = 4 × (−7) + 3  |
| −25 | −4  | 7   | 3   | −25 = (−4) × 7 + 3  |

Dans ce tableau, le reste est le même pour b et −b : il ne dépend que de a et de |b|, et seul le signe du quotient change.

::: piege Accepter un reste négatif
**Erreur : écrire −25 = 4 × (−6) − 1 et annoncer « reste −1 ».** Cela tente parce que −6 est l'entier le plus proche de −25/4 = −6,25 quand on arrondit vers 0. Mais le reste doit vérifier 0 ≤ r < |b|, et −1 n'est pas positif. On descend au multiple de 4 situé en dessous de −25, c'est-à-dire −28 = 4 × (−7), et l'on obtient −25 = 4 × (−7) + 3.
:::

::: propriete
Si a = bq + r avec 0 ≤ r < |b| :

- b divise a si et seulement si r = 0 ;
- le reste est l'un des |b| entiers 0, 1, …, |b| − 1 : classer les entiers selon leur reste par b, c'est les répartir en |b| familles.

Cas limite : si 0 ≤ a < |b|, alors q = 0 et r = a. Par exemple 7 = 12 × 0 + 7.
:::

::: exemple Montrer que n(n² + 2) est un multiple de 3 pour tout entier n
1. Le reste de n par 3 vaut 0, 1 ou 2 : n s'écrit 3k, 3k + 1 ou 3k + 2 avec k entier.
2. Si n = 3k, le facteur n est un multiple de 3, donc le produit aussi.
3. Si n = 3k + 1, n² + 2 = 9k² + 6k + 3 = 3(3k² + 2k + 1), multiple de 3.
4. Si n = 3k + 2, n² + 2 = 9k² + 12k + 6 = 3(3k² + 4k + 2), multiple de 3.
5. Les trois cas épuisent les restes possibles : la conclusion vaut pour tout n.

:::

::: verifie
Donne la division euclidienne de −130 par 8, puis par −8.

---

Les multiples de 8 qui encadrent −130 sont −136 = 8 × (−17) et −128 : −136 ≤ −130 < −128. Le reste est −130 − (−136) = 6, avec 0 ≤ 6 < 8. Par 8 : −130 = 8 × (−17) + 6. Par −8, le reste est le même et le quotient change de signe : −130 = (−8) × 17 + 6.
:::

::: retenir
Pour tout a et tout b non nul, a = bq + r avec 0 ≤ r < |b| de façon unique ; le reste est toujours positif, il ne dépend pas du signe de b, et pour a négatif on prend le multiple de b situé en dessous.
:::

## 🔮 Les congruences modulo n

Un jeudi, on prépare un événement dans 100 jours. Quel jour de la semaine sera-t-on ?
Le calendrier se répète tous les 7 jours : seul compte le reste de 100 dans la division par 7, et deux nombres de jours qui ont le même reste donnent le même jour. Comment écrire cela proprement ?

::: definition
Soient n un entier naturel non nul, a et b deux entiers relatifs. **a et b sont congrus modulo n** lorsqu'ils ont le même reste dans la division euclidienne par n. On note

$$ a ≡ b [n] $$

**Théorème.** a ≡ b [n] si et seulement si a − b est un multiple de n.
:::

::: exemple Le jour de la semaine dans 100 jours
1. 100 = 7 × 14 + 2 : le reste de 100 par 7 est 2, donc 100 ≡ 2 [7].
2. Avancer de 100 jours, c'est avancer d'autant de jours que 2 (les semaines entières ramènent au même jour).
3. Jeudi + 2 jours = samedi.
4. Contrôle par le théorème : 100 − 2 = 98 = 7 × 14, multiple de 7 ✓.

:::

| Affirmation   | Différence | Multiple de n ?     | Verdict |
| ------------- | ---------- | ------------------- | ------- |
| 14 ≡ 2 [6]    | 12         | 12 = 6 × 2          | vraie   |
| −2 ≡ 5 [7]    | −7         | −7 = 7 × (−1)       | vraie   |
| 27 ≡ −3 [10]  | 30         | 30 = 10 × 3         | vraie   |
| 41 ≡ 3 [8]    | 38         | 38 = 8 × 4 + 6      | fausse  |

La colonne « Différence » est celle du théorème : c'est elle qu'on teste, jamais les nombres eux-mêmes.

::: piege Prendre n'importe quel représentant pour le reste
**Erreur : lire 17 ≡ −3 [5] et conclure « le reste de 17 par 5 est −3 ».** Cela tente parce que l'égalité est vraie : 17 − (−3) = 20 est un multiple de 5. Mais un reste appartient à {0, …, n − 1}, et −3 n'y est pas. Le reste de 17 par 5 est 2, et −3 ≡ 2 [5] parce que −3 − 2 = −5.
:::

::: propriete
Soient n un entier naturel non nul et a, b, c des entiers relatifs.

- a ≡ a [n] (réflexivité).
- Si a ≡ b [n], alors b ≡ a [n] (symétrie).
- Si a ≡ b [n] et b ≡ c [n], alors a ≡ c [n] (transitivité).
- a ≡ r [n], où r est le reste de a par n ; et a ≡ 0 [n] signifie exactement que n divise a.

Cas limite : modulo 1, tous les entiers sont congrus ; le module 0 n'existe pas, car n doit être non nul.
:::

::: verifie
Aujourd'hui est un lundi. Quel jour sera-t-on dans 45 jours ? Justifie avec une congruence.

---

45 = 7 × 6 + 3, donc 45 ≡ 3 [7] : on avance de 3 jours dans la semaine, les six semaines entières ne changent rien. Lundi + 3 jours = jeudi. Contrôle : 45 − 3 = 42 = 7 × 6 est bien un multiple de 7.
:::

::: retenir
a ≡ b [n] signifie « même reste dans la division par n », ou encore « n divise a − b » ; un reste est dans {0, …, n − 1}, et la congruence compare les restes, pas les nombres.
:::

## 🧬 Calculer avec les congruences : grandes puissances et nombres de Mersenne

Un tableur calcule les restes de 5ⁿ par 13 : pour n = 0, 1, 2, 3, 4, 5, il affiche 1, 5, 12, 8, 1, 5.
Le nombre 5²⁰²⁶ compte plus de 1 400 chiffres, aucune calculatrice ne l'affiche : son reste par 13 se lit-il pourtant sans le calculer ?

| n     | 0 | 1 | 2  | 3   | 4   | 5    |
| ----- | - | - | -- | --- | --- | ---- |
| 5ⁿ    | 1 | 5 | 25 | 125 | 625 | 3125 |
| reste | 1 | 5 | 12 | 8   | 1   | 5    |

Dans ce tableau, les restes reviennent à 1 en n = 4, puis recommencent la même suite 5, 12, 8 : les puissances de 5 modulo 13 se répètent avec une période de 4.

::: propriete
Soient n un entier naturel non nul et a, b, c, d des entiers relatifs tels que a ≡ b [n] et c ≡ d [n]. Alors

- a + c ≡ b + d [n] et a − c ≡ b − d [n] ;
- a × c ≡ b × d [n] ;
- aᵖ ≡ bᵖ [n] pour tout entier naturel p.
:::

::: exemple Le reste de 5²⁰²⁶ par 13
1. 5⁴ = 625 = 13 × 48 + 1, donc 5⁴ ≡ 1 [13].
2. 2026 = 4 × 506 + 2, donc 5²⁰²⁶ = (5⁴)⁵⁰⁶ × 5².
3. Les puissances respectent les congruences : (5⁴)⁵⁰⁶ ≡ 1⁵⁰⁶ = 1 [13].
4. Le produit respecte les congruences : 5²⁰²⁶ ≡ 1 × 25 [13], et 25 = 13 × 1 + 12.
5. Le reste est 12, ce que confirme la ligne n = 2 du tableau, car 2026 et 2 ont le même reste par 4.

:::

::: piege Réduire l'exposant modulo n
**Erreur : écrire 5²⁰²⁶ ≡ 5¹¹ [13] parce que 2026 ≡ 11 [13].** Cela tente parce que la congruence s'applique à la base et qu'on la croit valable partout. Mais la propriété ne réduit que la base : l'exposant, lui, se réduit modulo la période des puissances, ici 4. La preuve que ce calcul est faux : 5¹¹ = (5⁴)² × 5³ ≡ 125 ≡ 8 [13], alors que le reste est 12.
:::

::: methode Reste de aᵏ modulo n

1. Réduire la base : remplacer a par son reste modulo n (ou par −1 quand a ≡ −1 [n]).
2. Calculer les restes de a, a², a³, … jusqu'à retrouver 1 : si le premier retour à 1 se produit en aᵖ, la période est p.
3. Écrire k = pq + s avec 0 ≤ s < p, puis a^k = (a^p)^q × a^s ≡ a^s [n].

Cas limite : si k est un multiple de p, alors s = 0 et aᵏ ≡ 1 [n]. Si a ≡ −1 [n], alors aᵏ ≡ (−1)ᵏ [n], égal à 1 pour k pair et à −1 pour k impair.
:::

::: exemple Le chiffre des unités de 7²⁰²⁶ (reste modulo 10)
1. 7¹ = 7, 7² = 49 ≡ 9, 7³ ≡ 9 × 7 = 63 ≡ 3 et 7⁴ ≡ 3 × 7 = 21 ≡ 1 [10] : la période est 4.
2. 2026 = 4 × 506 + 2, donc 7²⁰²⁶ ≡ 7² ≡ 9 [10].
3. Le chiffre des unités est le reste modulo 10 : c'est 9.

:::

::: exemple Les nombres de Mersenne : M₁₅ = 2¹⁵ − 1 est-il premier ?
1. Un nombre de Mersenne est de la forme Mₙ = 2ⁿ − 1.
2. 2³ = 8 ≡ 1 [7] car 7 = 2³ − 1. Donc 2¹⁵ = (2³)⁵ ≡ 1⁵ = 1 [7].
3. Ainsi 7 divise 2¹⁵ − 1 = 32767, qui n'est pas premier : 32767 = 7 × 4681.
4. Même raisonnement pour tout n = pq : 2ᵖ ≡ 1 [2ᵖ − 1], donc 2ⁿ = (2ᵖ)^q ≡ 1 et 2ᵖ − 1 divise 2ⁿ − 1.
5. Donc, si 2ⁿ − 1 est premier, alors n est premier. La réciproque est fausse : 11 est premier, mais M₁₁ = 2047 = 23 × 89.

:::

::: verifie
Quel est le reste de 4²⁰²⁵ modulo 7 ?

---

4¹ = 4, 4² = 16 ≡ 2 et 4³ = 64 = 7 × 9 + 1 ≡ 1 [7] : la période est 3. Comme 2025 = 3 × 675, l'exposant est un multiple de la période et 4²⁰²⁵ = (4³)⁶⁷⁵ ≡ 1⁶⁷⁵ = 1 [7]. Le reste est 1 : on a réduit l'exposant modulo la période 3, pas modulo 7.
:::

::: retenir
Les congruences s'additionnent, se multiplient et s'élèvent à une puissance ; pour aᵏ modulo n, on cherche la période des puissances de a puis on réduit l'exposant modulo cette période, jamais modulo n.
:::

## 🔎 Critères de divisibilité et clé ISBN

Un nombre est-il multiple de 9 sans qu'on le divise ? Pour 2457, on additionne les chiffres : 2 + 4 + 5 + 7 = 18, multiple de 9, et en effet 2457 = 9 × 273.
Pourquoi cette somme répond-elle, et existe-t-il un test aussi simple pour 4, 11 ou 7 ?

::: propriete
Un entier n s'écrit n = aₖ10ᵏ + … + a₁10 + a₀, où les aᵢ sont ses chiffres. Les puissances de 10 ont des restes très simples :

| Test sur n      | Raison                             | Critère                                              |
| --------------- | ---------------------------------- | ---------------------------------------------------- |
| 3 et 9          | 10 ≡ 1 [9], donc 10ᵏ ≡ 1           | n ≡ somme de ses chiffres                            |
| 4 et 25         | 100 ≡ 0 [4] et [25]                | divisible si ses deux derniers chiffres le sont      |
| 8 et 125        | 1000 ≡ 0 [8] et [125]              | divisible si ses trois derniers chiffres le sont     |
| 11              | 10 ≡ −1 [11], donc 10ᵏ ≡ (−1)ᵏ     | n ≡ a₀ − a₁ + a₂ − a₃ + … (somme alternée)           |
| 7               | n = 10a + b = 7(a + b) + 3(a − 2b) | 7 divise n si et seulement si 7 divise a − 2b        |

Dans la dernière ligne, b est le chiffre des unités et a le nombre formé par les autres chiffres.
:::

::: exemple Les tests sur 2457 et sur 6748
1. 2457 : 2 + 4 + 5 + 7 = 18 est un multiple de 9, donc 2457 est divisible par 9, et par 3.
2. Modulo 11, la somme alternée part des unités : 7 − 5 + 4 − 2 = 4, qui n'est pas multiple de 11. Donc 2457 n'est pas divisible par 11 (son reste est 4).
3. 6748 = 10 × 674 + 8, donc a = 674 et b = 8, et a − 2b = 674 − 16 = 658.
4. On recommence : 658 = 10 × 65 + 8 donne 65 − 16 = 49 = 7 × 7. Donc 7 divise 658, puis 7 divise 6748 (6748 = 7 × 964).

:::

::: piege Juger la divisibilité par 4 sur le dernier chiffre
**Erreur : dire « 1326 est divisible par 4 puisqu'il finit par 6, un chiffre pair ».** Cela tente parce que 4 divise tous les nombres pairs de petite taille. Mais 100 ≡ 0 [4] ne dépend que de ce qui précède les deux derniers chiffres : il faut regarder 26. Or 26 = 4 × 6 + 2 n'est pas multiple de 4, donc 1326 ne l'est pas (1326 = 4 × 331 + 2).
:::

Pourquoi le test de 7 est-il une équivalence ? Si 7 divise n = 7(a + b) + 3(a − 2b), il divise 3(a − 2b). Alors il divise 15(a − 2b) − 14(a − 2b) = a − 2b, par combinaison linéaire de deux multiples de 7. Réciproquement, si 7 divise a − 2b, il divise n.

::: exemple La clé du code ISBN 0-306-40615-?
1. Un ISBN-10 est formé de neuf chiffres a₁ a₂ … a₉ suivis d'une clé. On calcule S = a₁ + 2a₂ + 3a₃ + … + 9a₉ : le chiffre aᵢ est multiplié par son poids i.
2. La clé est le reste de S par 11, écrit X quand ce reste vaut 10.
3. Ici S = 0 + 2×3 + 3×0 + 4×6 + 5×4 + 6×0 + 7×6 + 8×1 + 9×5 = 6 + 24 + 20 + 42 + 8 + 45 = 145.
4. 145 = 11 × 13 + 2 : la clé est 2, et le code complet est 0-306-40615-2.
5. Si l'on se trompe sur un chiffre de poids i, S change d'un nombre δ ; tant que 11 ne divise pas δ, la clé recalculée diffère de la clé imprimée et l'erreur se voit. Par exemple, changer le chiffre de poids 3 de 4 unités fait varier S de 12, qui n'est pas multiple de 11.

:::

::: verifie
Calcule la clé de l'ISBN 2-07-036822-?

---

Les neuf chiffres sont 2, 0, 7, 0, 3, 6, 8, 2, 2. Donc S = 2 + 0 + 21 + 0 + 15 + 36 + 56 + 16 + 18 = 164. Alors 164 = 11 × 14 + 10, le reste vaut 10 et la clé s'écrit X : le code complet est 2-07-036822-X.
:::

::: retenir
On lit la divisibilité d'un entier sur ses chiffres grâce aux restes de 10ᵏ : somme des chiffres pour 3 et 9, deux derniers chiffres pour 4 et 25, somme alternée pour 11 ; la clé ISBN est le reste modulo 11 de a₁ + 2a₂ + … + 9a₉.
:::

## 📐 PGCD, PPCM et algorithme d'Euclide

Un carreleur doit couvrir un sol de 252 cm sur 198 cm avec des carreaux carrés, tous identiques, sans aucune découpe.
Quel est le plus grand côté de carreau possible ? Ce côté divise à la fois 252 et 198 : il faut un moyen de le trouver sans lister tous les diviseurs.

::: definition
Soient a et b deux entiers relatifs non nuls.

- Le **PGCD** de a et b, noté a ∧ b, est le plus grand entier qui divise à la fois a et b.
- Le **PPCM** de a et b, noté a ∨ b, est le plus petit entier strictement positif qui est à la fois multiple de a et de b.
- a et b sont **premiers entre eux** lorsque a ∧ b = 1.
:::

::: exemple Le carreleur : 252 ∧ 198 par divisions successives
1. Si a = bq + r, les diviseurs communs de a et b sont les mêmes que ceux de b et r (par combinaison linéaire dans les deux sens), donc a ∧ b = b ∧ r.
2. 252 = 198 × 1 + 54, donc 252 ∧ 198 = 198 ∧ 54.
3. 198 = 54 × 3 + 36, donc 198 ∧ 54 = 54 ∧ 36.
4. 54 = 36 × 1 + 18, donc 54 ∧ 36 = 36 ∧ 18.
5. 36 = 18 × 2 + 0 : 18 divise 36, donc 36 ∧ 18 = 18.
6. Le côté maximal est 18 cm, et les restes 54, 36, 18, 0 ont décru jusqu'à 0, ce qui assure que la suite s'arrête.

:::

Cette suite de divisions est l'**algorithme d'Euclide** : le PGCD est le dernier reste non nul. Il se programme par une boucle.

```
Tant que b ≠ 0 :
    r ← reste de a par b
    a ← b
    b ← r
afficher a
```

Trace pour a = 252 et b = 198 :

| Étape | a   | b   | r (reste de a par b) |
| ----- | --- | --- | -------------------- |
| 1     | 252 | 198 | 54                   |
| 2     | 198 | 54  | 36                   |
| 3     | 54  | 36  | 18                   |
| 4     | 36  | 18  | 0                    |

Après l'étape 4, la ligne suivante est (a ; b) = (18 ; 0) : la boucle s'arrête et affiche a = 18.

::: piege Confondre « premiers entre eux » et « premiers »
**Erreur : répondre « 8 et 15 ne sont pas premiers entre eux, car ni 8 ni 15 n'est un nombre premier ».** Cela tente parce que les deux expressions se ressemblent. Mais « premiers entre eux » parle du couple : 8 ∧ 15 = 1, puisque 8 = 15 × 0 + 8, 15 = 8 × 1 + 7, 8 = 7 × 1 + 1 donne un dernier reste non nul égal à 1. Aucun des deux n'est premier, et pourtant ils le sont entre eux.
:::

::: propriete
Soient a et b deux entiers non nuls et k un entier non nul.

- (ka) ∧ (kb) = |k| (a ∧ b).
- Les diviseurs communs de a et b sont exactement les diviseurs de a ∧ b.
- Si d = a ∧ b, alors a = da′ et b = db′ avec a′ ∧ b′ = 1 ; réciproquement, une telle écriture avec d > 0 donne d = a ∧ b.
- (a ∧ b) × (a ∨ b) = |ab|.

Cas limite : si b divise a, alors a ∧ b = |b| et a ∨ b = |a|. Pour les signes, a ∧ b = |a| ∧ |b|.
:::

::: exemple Le PPCM de 252 et 198, et le sens de a′ et b′
1. On a trouvé d = 18. Alors 252 = 18 × 14 et 198 = 18 × 11, avec 14 ∧ 11 = 1 : on a divisé par le PGCD.
2. (a ∧ b)(a ∨ b) = |ab| donne 252 ∨ 198 = 252 × 198 / 18 = 49896 / 18 = 2772.
3. Contrôle : 2772 = 252 × 11 = 198 × 14 est bien un multiple commun ✓.

:::

::: verifie
Calcule (−60) ∧ 45 par l'algorithme d'Euclide, puis (−60) ∨ 45.

---

Les signes ne comptent pas : (−60) ∧ 45 = 60 ∧ 45. Alors 60 = 45 × 1 + 15, puis 45 = 15 × 3 + 0, donc le dernier reste non nul est 15 et le PGCD vaut 15. Le PPCM vaut 60 × 45 / 15 = 180, un multiple commun de 60 et de 45 (180 = 60 × 3 = 45 × 4).
:::

::: retenir
a ∧ b est le dernier reste non nul de l'algorithme d'Euclide ; a ∧ b = b ∧ r, (a ∧ b)(a ∨ b) = |ab|, et « premiers entre eux » signifie a ∧ b = 1.
:::

## 🔗 Le théorème de Bézout et l'algorithme d'Euclide étendu

Deux bidons de 35 L et de 13 L servent à mesurer un seul litre : on remplit le premier u fois et on le vide, on remplit le second v fois, et la différence des volumes versés est de 1 L.
Cela revient à chercher des entiers relatifs u et v tels que 35u + 13v = 1. Un tel couple existe-t-il, et comment le trouve-t-on ?

::: propriete
**Théorème.** Soient a et b deux entiers non nuls et d = a ∧ b. Il existe deux entiers relatifs u et v tels que au + bv = d.

**Théorème de Bézout.** a et b sont premiers entre eux si et seulement si il existe u et v entiers relatifs tels que au + bv = 1. Cette égalité est une **relation de Bézout**.
:::

::: exemple Une relation de Bézout pour 35 et 13, par remontée
1. L'algorithme d'Euclide donne 35 = 13 × 2 + 9, puis 13 = 9 × 1 + 4, puis 9 = 4 × 2 + 1. Le dernier reste non nul est 1 : 35 ∧ 13 = 1.
2. On isole chaque reste : 9 = 35 − 2 × 13, puis 4 = 13 − 9, puis 1 = 9 − 2 × 4.
3. On remonte en remplaçant : 1 = 9 − 2(13 − 9) = 3 × 9 − 2 × 13.
4. On remplace encore 9 : 1 = 3(35 − 2 × 13) − 2 × 13 = 3 × 35 − 8 × 13.
5. Contrôle : 3 × 35 = 105 et 8 × 13 = 104, donc 105 − 104 = 1 ✓. Le couple (u ; v) = (3 ; −8) convient.

:::

Cette remontée se programme sans réécrire de formule : on garde pour chaque reste rₖ un couple (uₖ ; vₖ) tel que a × uₖ + b × vₖ = rₖ. On part de r₀ = a avec (1 ; 0) et de r₁ = b avec (0 ; 1), et pour chaque quotient qₖ de la division de rₖ₋₂ par rₖ₋₁ :

$$ rₖ = rₖ₋₂ − qₖ rₖ₋₁, uₖ = uₖ₋₂ − qₖ uₖ₋₁, vₖ = vₖ₋₂ − qₖ vₖ₋₁ $$

Trace pour a = 35 et b = 13 (chaque ligne se vérifie : 35uₖ + 13vₖ = rₖ) :

| k | quotient qₖ | rₖ | uₖ | vₖ |
| - | ----------- | -- | -- | -- |
| 0 |             | 35 | 1  | 0  |
| 1 |             | 13 | 0  | 1  |
| 2 | 2           | 9  | 1  | −2 |
| 3 | 1           | 4  | −1 | 3  |
| 4 | 2           | 1  | 3  | −8 |
| 5 | 4           | 0  |    |    |

La dernière ligne avec un reste non nul est k = 4 : r₄ = 1 = 35 × 3 + 13 × (−8), la relation de la remontée.

::: piege Croire qu'une relation avec 2 donne le PGCD 2
**Erreur : de 3 × 4 + 5 × (−2) = 2, conclure que 3 ∧ 5 = 2.** Cela tente parce que, dans la relation de Bézout, le second membre est bien le PGCD. Mais le théorème ne marche que dans un sens : au + bv = c prouve seulement que a ∧ b divise c. Ici 3 ∧ 5 = 1, qui divise 2. Seule la valeur c = 1 permet de conclure, avec le théorème de Bézout : 1 est atteint, donc a et b sont premiers entre eux.
:::

::: propriete
Soient a et b deux entiers non nuls.

- Le théorème de Bézout est un théorème d'existence, pas d'unicité : si (u ; v) convient, alors (u + b ; v − a) convient aussi, car a(u + b) + b(v − a) = au + bv.
- Tout diviseur commun à a et b divise a ∧ b.
- L'équation ax + by = c (c entier non nul) a des solutions entières si et seulement si c est un multiple de a ∧ b.

Cas limite : 6x + 9y = 10 n'a aucune solution entière, car 6 ∧ 9 = 3 ne divise pas 10.
:::

::: verifie
Trouve u et v entiers tels que 17u + 5v = 1.

---

17 = 5 × 3 + 2, puis 5 = 2 × 2 + 1 : le dernier reste non nul est 1, donc 17 ∧ 5 = 1 et la relation existe. On remonte : 1 = 5 − 2 × 2 = 5 − 2(17 − 3 × 5) = 7 × 5 − 2 × 17. Donc (u ; v) = (−2 ; 7). Contrôle : 17 × (−2) + 5 × 7 = −34 + 35 = 1 ✓.
:::

::: retenir
a ∧ b = 1 si et seulement si au + bv = 1 a une solution entière ; l'algorithme d'Euclide étendu la fournit, et ax + by = c est résoluble si et seulement si a ∧ b divise c.
:::

## 🧱 Le lemme de Gauss et les équations ax + by = c

Si 7 divise 5k, que peut-on dire de k ? Et si 6 divise 3 × 4 = 12, 6 divise-t-il 3 ou 4 ?
La simplification d'une divisibilité n'est pas toujours permise. Quelle condition la rend légitime, et comment s'en sert-on pour résoudre ax + by = c dans ℤ × ℤ ?

::: propriete
**Lemme de Gauss.** Soient a, b et c trois entiers non nuls. Si a divise bc et si a ∧ b = 1, alors a divise c.

**Corollaire.** Si a ∧ b = 1, si a divise c et si b divise c, alors ab divise c.
:::

::: exemple 7 divise 5k : que dire de k ?
1. 7 ∧ 5 = 1, car 7 = 5 × 1 + 2, 5 = 2 × 2 + 1.
2. 7 divise 5k et 7 est premier avec 5 : le lemme de Gauss donne 7 | k.
3. Un exemple du corollaire : 4 ∧ 9 = 1, 4 | n et 9 | n donnent 36 | n.
4. Contrôle : n = 72 est multiple de 4 et de 9, et 72 = 36 × 2 ✓.

:::

::: piege Écrire « a divise bc donc a divise b ou c »
**Erreur : de 6 | 3 × 4, conclure que 6 divise 3 ou 4.** Cela tente parce que le résultat est vrai pour un nombre premier et qu'on généralise. Mais 6 | 12 alors que 6 ne divise ni 3 ni 4. Ici 6 ∧ 3 = 3 ≠ 1 : l'hypothèse de Gauss manque. De même, 4 | 12 et 6 | 12 ne donnent pas 24 | 12, car 4 ∧ 6 = 2.
:::

::: methode Résoudre ax + by = c dans ℤ × ℤ

1. Calculer d = a ∧ b. Si d ne divise pas c, il n'y a aucune solution. Sinon on divise a, b et c par d, et l'on obtient A, B, C avec A ∧ B = 1.
2. Trouver une solution particulière (x₀ ; y₀) de Ax + By = C : relation de Bézout de A et B, multipliée par C.
3. Soustraire : A(x − x₀) = −B(y − y₀). Comme A ∧ B = 1, Gauss donne B | x − x₀ ; on pose x = x₀ + Bk.
4. Reporter : y = y₀ − Ak. Les solutions sont les couples (x₀ + Bk ; y₀ − Ak), k ∈ ℤ.

:::

::: exemple Résoudre 35x + 13y = 7
1. 35 ∧ 13 = 1 divise 7 : il y a des solutions. La relation 3 × 35 − 8 × 13 = 1 donne, multipliée par 7, 21 × 35 − 56 × 13 = 7.
2. Une solution particulière est (x₀ ; y₀) = (21 ; −56). Contrôle : 735 − 728 = 7 ✓.
3. En soustrayant, 35(x − 21) = −13(y + 56). Donc 13 divise 35(x − 21) ; comme 13 ∧ 35 = 1, Gauss donne 13 | x − 21, soit x = 21 + 13k.
4. Alors 35 × 13k = −13(y + 56), d'où y = −56 − 35k.
5. Les solutions sont les couples (21 + 13k ; −56 − 35k), k ∈ ℤ. Pour k = −1 : (8 ; −21) et 280 − 273 = 7 ✓.

:::

::: exemple Quand a ∧ b ≠ 1 : 12x + 18y = 30, puis une congruence 6x ≡ 4 [14]
1. 12 ∧ 18 = 6 divise 30 : on divise tout par 6 et l'on résout 2x + 3y = 5. Une solution évidente est (1 ; 1).
2. Les solutions sont (1 + 3k ; 1 − 2k), k ∈ ℤ. Pour k = 1 : (4 ; −1) et 48 − 18 = 30 ✓.
3. Une congruence 6x ≡ 4 [14] équivaut à 6x − 4 = 14t, soit 6x − 14t = 4, une équation du type précédent. Ici 6 ∧ 14 = 2 divise 4 ; on obtient 3x ≡ 2 [7], d'où x ≡ 3 [7] : parmi les restes 0 à 6, seul x = 3 convient (3 × 3 = 9 ≡ 2 [7]).

:::

::: verifie
Résous 4x + 6y = 10 dans ℤ × ℤ.

---

4 ∧ 6 = 2 divise 10 : on divise par 2 et l'on résout 2x + 3y = 5. Une solution particulière est (1 ; 1), car 2 + 3 = 5. Alors 2(x − 1) = −3(y − 1), et comme 2 ∧ 3 = 1, Gauss donne 3 | x − 1 : x = 1 + 3k, puis y = 1 − 2k. Contrôle : k = 1 donne (4 ; −1) et 16 − 6 = 10 ✓. L'ensemble des solutions est {(1 + 3k ; 1 − 2k), k ∈ ℤ}.
:::

::: retenir
Si a divise bc et a ∧ b = 1, alors a divise c ; l'équation ax + by = c n'a de solution que si a ∧ b divise c, et ses solutions se déduisent d'une solution particulière (x₀ ; y₀) par (x₀ + Bk ; y₀ − Ak), avec A = a/(a ∧ b) et B = b/(a ∧ b).
:::

> 🏆 Porte franchie, héros : tu lis les entiers par leurs restes, tu fais tourner l'algorithme d'Euclide et tu résous ax + by = c dans ℤ. Au prochain chapitre, un nouvel ensemble de nombres t'attend : les complexes.
