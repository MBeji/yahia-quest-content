# ⚔️ Arithmétique — le royaume des entiers et l'art de conclure sans diviser

> 💡 «Le bon arithméticien ne pose pas la division : il regarde les chiffres, et il sait déjà.»

Tu poses des divisions depuis l'école primaire. Cette quête change de regard : on ne cherche plus le résultat, on cherche le **reste** — et surtout, on apprend à le connaître **sans poser l'opération**. Deux ou trois chiffres suffisent alors à trancher : ce nombre est-il divisible par 4 ? par 9 ? par 11 ? Ces réflexes servent partout, du contrôle d'un code-barres au calcul d'un jour de la semaine.

## 🏰 La division euclidienne, socle de tout le chapitre

> **Retenir (division euclidienne).** a et b désignent deux entiers naturels tels que b ≠ 0. On admet l'existence d'un couple **unique** (q, r) d'entiers naturels tels que a = bq + r avec 0 ≤ r < b. Le nombre a est le **dividende**, b le **diviseur**, q le **quotient** et r le **reste**.

Deux mots comptent dans cet encadré. **Unique** : il n'y a pas deux façons d'écrire cette division. Et **0 ≤ r < b** : le reste est toujours **strictement inférieur au diviseur**. Tant qu'il reste plus que le diviseur, la division n'est pas terminée.

_Exemple détaillé_ : divisons 347 par 15. On cherche le plus grand multiple de 15 inférieur ou égal à 347. Comme 15 × 23 = 345 et 15 × 24 = 360, c'est 345. Donc 347 = 15 × 23 + 2, avec **q = 23** et **r = 2** — et 0 ≤ 2 < 15 ✓.

::: figure Sur la droite des multiples de 15, le nombre 347 tombe juste après 345 = 15 × 23 : le quotient se lit sur le multiple atteint, et le reste est l'écart qui subsiste
<svg viewBox="0 0 460 170">
<line x1="25" y1="80" x2="440" y2="80" stroke="#0f172a" stroke-width="2"/>
<path d="M431 73 L442 80 L431 87" fill="none" stroke="#0f172a" stroke-width="2"/>
<g stroke="#0f172a" stroke-width="2">
<line x1="70" y1="72" x2="70" y2="88"/>
<line x1="230" y1="72" x2="230" y2="88"/>
<line x1="390" y1="72" x2="390" y2="88"/>
</g>
<circle cx="251" cy="80" r="5" fill="#b91c1c"/>
<line x1="251" y1="38" x2="251" y2="72" stroke="#b91c1c" stroke-width="1.4" stroke-dasharray="4 3"/>
<path d="M230 90 L230 98 L251 98 L251 90" fill="none" stroke="#b91c1c" stroke-width="1.8"/>
<g font-size="13" font-weight="700" fill="#b91c1c">
<text x="251" y="30" text-anchor="middle">a = 347</text>
<text x="241" y="116" text-anchor="middle">r = 2</text>
</g>
<g font-size="13" font-weight="700" fill="#0f172a" text-anchor="middle">
<text x="70" y="136">330</text>
<text x="230" y="136">345</text>
<text x="390" y="136">360</text>
</g>
<g font-size="12" fill="#475569" text-anchor="middle">
<text x="70" y="155">15 × 22</text>
<text x="230" y="155">15 × 23</text>
<text x="390" y="155">15 × 24</text>
</g>
</svg>
:::

**Lire un reste sur une calculatrice.** L'écran affiche 347 ÷ 15 = 23,133333. Le quotient est la **partie entière** de cet affichage, soit 23 ; le reste s'obtient ensuite par soustraction : r = 347 − 15 × 23 = **2**.

> ⚠️ Les décimales affichées ne sont **pas** le reste. Lire « 13 » dans 23,**13**3333 est l'erreur la plus fréquente du chapitre : ces décimales valent r/b, pas r.

## 🔗 Diviseurs, multiples, et ce qu'on en déduit

Dire que **b divise a** (ou que a est un **multiple** de b), c'est dire que le reste de la division de a par b est nul, autrement dit qu'il existe un entier k tel que a = kb. On dit alors aussi que b est un **diviseur** de a.

De l'écriture a = bq + r découle une conséquence qu'on utilisera sans cesse : **a − r est un multiple de b**. Un reste imposé se transforme donc toujours en une divisibilité exacte.

> **Retenir.** Soit n un entier naturel non nul qui divise x et qui divise y (avec x ≥ y). Alors n divise **px** pour tout entier p, n divise **x + y** et n divise **x − y**.

_Exemple détaillé_ : 7 divise 91 et 7 divise 56. Donc 7 divise 91 + 56 = 147, 7 divise 91 − 56 = 35, et 7 divise 5 × 91 = 455. On vérifie : 147 = 7 × 21, 35 = 7 × 5 et 455 = 7 × 65 ✓.

> 🗡️ La règle se combine : si n divise x et y, alors n divise **px − qy** pour tous entiers p et q. C'est l'outil qui fait tomber les problèmes où l'inconnue disparaît. Si n divise x = 2k + 5 et y = k + 1, alors n divise x − 2y = 2k + 5 − 2k − 2 = 3 : n ne peut valoir que 1 ou 3.

## 🔢 Les critères qui se lisent sur les derniers chiffres

Tout repose sur une même idée : découper le nombre en une partie qui est **sûrement** un multiple du diviseur, plus un petit reste visible.

- **Par 2 et par 5.** Tout entier s'écrit n = 10q + u, où u est son **chiffre des unités**. Comme 10q est un multiple de 2 et de 5, n et u laissent le **même reste** dans la division par 2 (resp. par 5). D'où : n est divisible par 2 (resp. par 5) si et seulement si u l'est.
- **Par 4 et par 25.** On écrit n = 100a + b, où b est le nombre formé par les **deux derniers chiffres**. Comme 100 = 4 × 25, le terme 100a est un multiple de 4 et de 25 : n et b laissent le même reste par 4 (resp. par 25).
- **Par 8.** On écrit n = 1000a + b, où b est le nombre formé par les **trois derniers chiffres**. Comme 1000 = 8 × 125, n et b laissent le même reste par 8.

| Diviseur | On regarde                | Exemple                              |
| -------- | ------------------------- | ------------------------------------ |
| 2 et 5   | le chiffre des unités     | 4617 → 7 : reste 1 par 2, reste 2 par 5 |
| 4 et 25  | les deux derniers chiffres | 9548 → 48 = 4 × 12 : divisible par 4 |
| 8        | les trois derniers chiffres | 73542 → 542 = 8 × 67 + 6 : reste 6  |

_Exemple détaillé_ : quel est le reste de 73542 dans la division par 8 ? On garde 542, puis 542 = 8 × 67 + 6. Le reste cherché est donc **6**, sans avoir posé la division de 73542 ✓.

> ⚠️ Un nombre pair n'est pas forcément divisible par 4, et un nombre divisible par 4 ne l'est pas forcément par 8 : 3214 est pair, mais 14 = 4 × 3 + 2, donc 3214 n'est pas divisible par 4.

## ➕ Les critères qui se lisent sur la somme des chiffres

Prenons un entier de quatre chiffres, n = 1000a + 100b + 10c + d, et notons S = a + b + c + d la **somme de ses chiffres**. On écrit :

$$ n = 999a + 99b + 9c + (a + b + c + d) = 999a + 99b + 9c + S $$

Les nombres 999, 99 et 9 sont tous des multiples de 9, donc aussi de 3. Ainsi n − S est un multiple de 9, et **n et S laissent le même reste** dans la division par 3 comme dans la division par 9. Le raisonnement vaut quel que soit le nombre de chiffres.

> **Retenir.** Un entier est divisible par 3 (resp. par 9) si et seulement si la somme de ses chiffres l'est ; et le reste de sa division par 3 (resp. par 9) est le reste de cette somme.

_Exemple détaillé_ : pour 5384, S = 5 + 3 + 8 + 4 = 20, et 20 = 9 × 2 + 2. Le reste de 5384 par 9 vaut donc **2** ✓. Attention à finir le travail : répondre 20 revient à donner la somme, pas le reste.

_Exemple détaillé (chiffre inconnu)_ : dans 83a6, quel chiffre a rend l'entier divisible par 9 ? La somme vaut 8 + 3 + a + 6 = 17 + a. Comme a est un chiffre, 17 + a est compris entre 17 et 26 : le seul multiple de 9 possible est 18, d'où **a = 1**. On vérifie : 8316 = 9 × 924 ✓.

> ⚠️ Ne confonds pas les deux critères. La somme des chiffres de 8346 vaut 21 : c'est un multiple de 3, mais pas de 9. Donc 8346 est divisible par 3 et pas par 9.

## ⚡ Le critère par 11 : la somme alternée

Le point de départ : 11 divise 10² − 1 = 99, et 11 divise 10³ + 1 = 1001. Plus généralement 11 divise 10^(2k) − 1 et 10^(2k+1) + 1. Les puissances de 10 d'exposant pair valent donc « 1 de plus » qu'un multiple de 11, et celles d'exposant impair « 1 de moins » : les chiffres entrent alternativement avec le signe + et le signe −.

On numérote les chiffres **de droite à gauche** : le chiffre des unités est de rang 1, celui des dizaines de rang 2, et ainsi de suite. On note **S₁** la somme des chiffres de rang impair, **S₂** la somme des chiffres de rang pair, et l'on forme la **somme alternée** :

$$ d = S₁ − S₂ $$

> **Retenir.** Si d ≥ 0, l'entier est divisible par 11 si et seulement si d l'est, et le reste de sa division par 11 est le reste de d. Si d < 0, on ajoute à d un multiple de 11 pour le rendre positif : on choisit p tel que d + 11p ≥ 0, et on conclut sur d + 11p.

_Exemple détaillé_ : pour 2749, les rangs impairs portent 9 et 7, les rangs pairs portent 4 et 2. Donc S₁ = 9 + 7 = 16, S₂ = 4 + 2 = 6 et d = 16 − 6 = **10**. Comme 0 ≤ 10 < 11, le reste de 2749 par 11 vaut **10** : ce nombre n'est pas divisible par 11 ✓.

_Exemple détaillé (cas d < 0)_ : pour 7392, S₁ = 2 + 3 = 5 et S₂ = 9 + 7 = 16, donc d = 5 − 16 = −11. On ajoute 11 : d + 11 = 0, qui est bien divisible par 11. Donc **7392 est divisible par 11**, et son reste est 0. On vérifie : 7392 = 11 × 672 ✓.

> ⚠️ Le critère de 11 n'est pas celui de 9 : la somme des chiffres de 7362 vaut 18, ce nombre est donc divisible par 9 — mais sa somme alternée vaut 2 − 6 + 3 − 7 = −8, et 7362 n'est pas divisible par 11.

## 🔮 Facteurs premiers, PGCD, PPCM et entiers premiers entre eux

Un entier supérieur ou égal à 2 est **premier** lorsque ses seuls diviseurs sont 1 et lui-même (2, 3, 5, 7, 11, 13, …). Tout entier supérieur ou égal à 2 se décompose d'une seule façon en **produit de facteurs premiers**.

_Exemple détaillé_ : 252 = 4 × 63 = 2² × 3² × 7, et 600 = 8 × 75 = 2³ × 3 × 5². Une décomposition n'est achevée que si **chaque** facteur est premier : écrire 252 = 2² × 63 ou 252 = 2 × 3² × 14 donne bien 252, mais 63 et 14 ne sont pas premiers.

Sur ces décompositions, tout se lit :

- le **PGCD** (plus grand commun diviseur) prend les facteurs **communs**, chacun au **plus petit** exposant : PGCD(252 ; 600) = 2² × 3 = **12** ;
- le **PPCM** (plus petit commun multiple) prend **tous** les facteurs, chacun au **plus grand** exposant : PPCM(252 ; 600) = 2³ × 3² × 5² × 7 = **12600**.

_Exemple détaillé (application)_ : pour découper une plaque de 60 cm sur 84 cm en carrés identiques les plus grands possibles, le côté de ces carrés doit diviser 60 **et** 84 : c'est PGCD(60 ; 84). Or 60 = 2² × 3 × 5 et 84 = 2² × 3 × 7, donc PGCD(60 ; 84) = 2² × 3 = **12** cm ; on obtient alors 60 ÷ 12 = 5 carrés en largeur et 84 ÷ 12 = 7 en longueur, soit 5 × 7 = **35** carrés ✓. La règle vaut pour trois nombres comme pour deux : PGCD(60 ; 84 ; 90) garde les facteurs communs aux **trois** décompositions, chacun au plus petit exposant. Comme 90 = 2 × 3² × 5, seuls 2 et 3 sont communs aux trois, et PGCD(60 ; 84 ; 90) = 2 × 3 = **6**.

> 🗡️ Le réflexe à garder : _la plus grande pièce identique_ se lit sur le PGCD, et _le nombre de pièces_ s'obtient ensuite en divisant chaque dimension par ce PGCD.

Deux entiers sont **premiers entre eux** lorsque leur PGCD vaut 1, c'est-à-dire lorsqu'ils n'ont aucun facteur premier commun. Ainsi 328 = 2³ × 41 et 299 = 13 × 23 sont premiers entre eux.

> 🗡️ Deux repères pour ne jamais les confondre : le PGCD **divise** les deux nombres (il est donc inférieur ou égal au plus petit), le PPCM est un **multiple** des deux (il est donc supérieur ou égal au plus grand). Un PGCD sert à faire des **paquets identiques** ; un PPCM sert à savoir quand deux **cycles** retombent ensemble.

## 🗝️ Les cinq méthodes du chapitre

1. **Chiffre inconnu.** On traduit le critère en une condition sur la somme des chiffres (ou sur la somme alternée), puis on cherche la seule valeur possible entre 0 et 9.
2. **Reste imposé.** De a = bq + r on tire que b divise a − r. Si la division de 1000 par n laisse 12 pour reste, alors n divise 1000 − 12 = 988, et de plus n > 12 puisque le reste est toujours inférieur au diviseur. Avec deux conditions de ce type, on cherche les diviseurs communs, c'est-à-dire les diviseurs du PGCD.
3. **Raisonner par cas sur le reste.** Tout entier n s'écrit 3k, 3k + 1 ou 3k + 2. On traite les trois cas : (3k)² = 3(3k²) laisse 0, (3k + 1)² = 3(3k² + 2k) + 1 laisse 1, et (3k + 2)² = 3(3k² + 4k + 1) + 1 laisse 1. Les seuls restes possibles de n² par 3 sont donc **0 et 1**.
4. **Chercher un cycle.** Le chiffre des unités de 3ⁿ se répète de 4 en 4 : 3, 9, 7, 1, puis 3, 9, 7, 1… Pour connaître celui de 3⁴¹, on divise l'exposant par 4 : 41 = 4 × 10 + 1, le reste est 1, le chiffre des unités est donc celui de 3¹, soit **3**. Le même réflexe donne les jours de la semaine : dans 100 jours, comme 100 = 7 × 14 + 2, on avance de **2** jours seulement.
5. **Croiser deux restes imposés.** Quand un entier doit laisser deux restes fixés dans deux divisions différentes, on écrit la liste des candidats de chaque condition et l'on prend le **premier terme commun**. Les entiers qui laissent 1 pour reste dans la division par 3 sont 1, 4, 7, 10, 13, 16… ; ceux qui laissent 2 pour reste dans la division par 4 sont 2, 6, 10, 14, 18… Le premier nombre présent dans les deux listes est **10**, et l'on vérifie 10 = 3 × 3 + 1 puis 10 = 4 × 2 + 2 ✓. Les entiers suivants s'obtiennent en ajoutant 12, le PPCM de 3 et de 4 : 22, 34, 46…

## 📜 Math et culture : la clé du code-barres et les nombres amiables

**La clé d'un code-barres.** Un code à 13 chiffres se termine par une **clé de contrôle** calculée pour que la somme des chiffres de rang impair, augmentée du **triple** de la somme des chiffres de rang pair, soit un multiple de 10 — ici les rangs se comptent **à partir de la gauche**, à l'inverse du critère de 11, qui les compte à partir des unités. Pour le code 619220260141, les rangs impairs donnent 6 + 9 + 2 + 2 + 0 + 4 = 23 et les rangs pairs 1 + 2 + 0 + 6 + 1 + 1 = 11. Le total vaut 23 + 3 × 11 = 56, il faut donc ajouter une clé de **4** pour atteindre 60 : la caisse rejette aussitôt tout code mal recopié.

**Les nombres amiables.** Deux entiers sont **amiables** lorsque chacun est la somme des diviseurs propres de l'autre (ses diviseurs autres que lui-même). Le couple le plus célèbre est 220 et 284 : les diviseurs propres de 220 sont 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 et 110, de somme 284 ; ceux de 284 sont 1, 2, 4, 71 et 142, de somme 220 ✓. Le savant bagdadien **Thabit Ibn Qurra** (836-901) en a donné une recette : si p = 3 × 2^(n−1) − 1, q = 3 × 2ⁿ − 1 et r = 9 × 2^(2n−1) − 1 sont tous trois premiers, alors 2ⁿ × p × q et 2ⁿ × r sont amiables. Pour n = 2 : p = 5, q = 11, r = 71, et l'on retrouve 2² × 5 × 11 = 220 et 2² × 71 = 284.

> 🏆 Quête franchie, héros : tu sais désormais encadrer une division, lire un reste sans la poser, débusquer un chiffre manquant et manier PGCD et PPCM. Garde ces réflexes au chaud — la géométrie du chapitre suivant te demandera la même rigueur, mais sur des vecteurs.
