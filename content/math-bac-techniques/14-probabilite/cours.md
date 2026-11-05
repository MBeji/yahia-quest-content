# ⚔️ Probabilité sur un ensemble fini — mesurer le hasard sans le subir

> 💡 «Le hasard ne se dompte pas, il se mesure : un nombre entre 0 et 1, et quelques règles qui ne trompent jamais.»

Ce chapitre apprend à donner un nombre à un événement aléatoire, puis à le recalculer quand une information arrive. Huit notions : le langage des événements et la probabilité, la probabilité uniforme, le dénombrement des tirages, la probabilité conditionnelle, l'indépendance, les probabilités composées avec l'arbre pondéré, les probabilités totales et la formule de Bayes. Tu réutilises les arrangements Aₙᵖ et les combinaisons Cₙᵖ vus en dénombrement ; toutes les expériences ont un nombre fini de résultats.

## 🎲 Événements et probabilité : le langage et les règles

Dans un lycée, 45 % des élèves font du sport, 30 % font de la musique et 12 % font les deux. On interroge un élève au hasard.
Quelle est la probabilité qu'il pratique au moins l'une des deux activités ? Et qu'il n'en pratique aucune ?

::: definition
Une expérience aléatoire a un ensemble fini de résultats possibles, noté Ω et appelé **univers**. Un **événement** est une partie A de Ω ; un événement formé d'un seul résultat est **élémentaire**, Ω est l'événement **certain** et ∅ l'événement **impossible**.
A ∩ B se lit « A et B » ; A ∪ B se lit « A ou B » (l'un au moins) ; A̅ est l'événement **contraire** de A (il est réalisé quand A ne l'est pas) ; A et B sont **incompatibles** si A ∩ B = ∅.
:::

::: definition
Une **probabilité** p associe à chaque événement un nombre de [0 ; 1] de sorte que p(Ω) = 1 et que p(A ∪ B) = p(A) + p(B) quand A et B sont incompatibles.
:::

::: figure Le sport (A) et la musique (B) se chevauchent : les 0,12 du milieu sont comptés une seule fois, et les 0,37 hors des cercles sont les élèves sans activité
<svg viewBox="0 0 340 230">
<title>Sport (A) et musique (B) : les quatre régions de probabilités 0,33 ; 0,12 ; 0,18 et 0,37</title>
<rect x="14" y="14" width="312" height="202" rx="6" fill="none" stroke="#0f172a" stroke-width="1.8"/>
<circle cx="130" cy="115" r="72" fill="#0f6e56" fill-opacity="0.14" stroke="#0f172a" stroke-width="2"/>
<circle cx="210" cy="115" r="72" fill="#b45309" fill-opacity="0.14" stroke="#0f172a" stroke-width="2"/>
<text x="88" y="56" text-anchor="middle" font-size="15" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">A</text>
<text x="252" y="56" text-anchor="middle" font-size="15" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">B</text>
<text x="310" y="36" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">Ω</text>
<text x="98" y="120" text-anchor="middle" font-size="15" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0,33</text>
<text x="170" y="120" text-anchor="middle" font-size="15" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0,12</text>
<text x="242" y="120" text-anchor="middle" font-size="15" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0,18</text>
<text x="40" y="200" text-anchor="middle" font-size="15" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0,37</text>
</svg>
:::

Sur la figure, A est le cercle de gauche et B celui de droite ; la zone commune est A ∩ B. Les quatre régions ne se recouvrent pas : leurs probabilités s'additionnent.

::: exemple Sport ou musique ?

1. Données : p(A) = 0,45, p(B) = 0,30 et p(A ∩ B) = 0,12. Les 0,12 sont comptés dans p(A) et dans p(B), donc « sport seul » vaut 0,45 − 0,12 = 0,33 et « musique seule » 0,30 − 0,12 = 0,18.
2. Au moins une activité : p(A ∪ B) = p(A) + p(B) − p(A ∩ B) = 0,45 + 0,30 − 0,12 = 0,63, car l'intersection a été comptée deux fois et on la retire une fois.
3. Aucune activité : c'est le contraire de A ∪ B, donc 1 − 0,63 = 0,37.
4. Contrôle : 0,33 + 0,12 + 0,18 + 0,37 = 1,00 ✓, les quatre régions couvrent Ω.

:::

::: piege
**Erreur : additionner p(A) + p(B) sans retrancher p(A ∩ B).** L'erreur tente parce que « ou » ressemble à « plus ». Ici elle donne 0,45 + 0,30 = 0,75 au lieu de 0,63, et avec p(A) = 0,70 et p(B) = 0,60 elle donnerait 1,30, un nombre impossible. Les élèves des deux activités sont comptés deux fois : on retranche 0,12.
:::

::: propriete
Pour des événements A et B d'un univers fini :
- p(A̅) = 1 − p(A), et p(∅) = 0 ;
- p(A ∪ B) = p(A) + p(B) − p(A ∩ B) ;
- si A ⊂ B, alors p(B \ A) = p(B) − p(A), donc p(A) ≤ p(B).

Cas limite : si A et B sont incompatibles, p(A ∩ B) = 0 et la formule se réduit à p(A ∪ B) = p(A) + p(B).
:::

::: verifie À toi : le double défaut
Dans un lot de pièces, 8 % ont un défaut d'aspect (A), 5 % un défaut de taille (B) et 11 % ont au moins un des deux défauts. Quelle proportion de pièces cumule les deux défauts ?

---

On part de p(A ∪ B) = p(A) + p(B) − p(A ∩ B), donc p(A ∩ B) = p(A) + p(B) − p(A ∪ B) = 0,08 + 0,05 − 0,11 = 0,02. Les pièces cumulant les deux défauts sont comptées deux fois dans 0,08 + 0,05 = 0,13 : l'excédent sur 0,11 est exactement 0,02, soit 2 %.
:::

::: retenir
La probabilité d'un événement vaut 1 moins celle de son contraire, et p(A ∪ B) = p(A) + p(B) − p(A ∩ B) : on retranche l'intersection comptée deux fois.
:::

## 🎯 Probabilité uniforme : compter suffit

On lance deux dés équilibrés, un rouge et un vert. Les 36 couples (rouge, vert) ont-ils tous la même chance d'apparaître ?
Si oui, comment trouver la probabilité d'obtenir une somme égale à 8 ?

::: definition
Quand tous les événements élémentaires ont la même probabilité, la probabilité est **uniforme** (on dit aussi qu'il y a **équiprobabilité**). Avec Ω = {ω₁, …, ωₙ}, chaque événement élémentaire a pour probabilité 1/n = 1/card Ω, et pour tout événement A :
$$ p(A) = card A / card Ω $$
C'est le nombre de cas favorables divisé par le nombre de cas possibles.
:::

::: figure Le tableau des 36 couples avec leur somme : les cinq cases colorées sont les couples de somme 8, sur une diagonale
<svg viewBox="0 0 340 262">
<title>Les 36 couples (dé rouge, dé vert) et leur somme ; ceux de somme 8 sont colorés</title>
<text x="186" y="18" text-anchor="middle" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">dé vert</text>
<text x="24" y="146" text-anchor="middle" font-size="12" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">dé</text>
<text x="24" y="161" text-anchor="middle" font-size="12" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">rouge</text>
<text x="86" y="34" text-anchor="middle" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">1</text>
<text x="126" y="34" text-anchor="middle" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">2</text>
<text x="166" y="34" text-anchor="middle" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">3</text>
<text x="206" y="34" text-anchor="middle" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">4</text>
<text x="246" y="34" text-anchor="middle" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">5</text>
<text x="286" y="34" text-anchor="middle" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">6</text>
<text x="54" y="62" text-anchor="middle" font-size="12" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">1</text>
<text x="54" y="96" text-anchor="middle" font-size="12" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">2</text>
<text x="54" y="130" text-anchor="middle" font-size="12" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">3</text>
<text x="54" y="164" text-anchor="middle" font-size="12" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">4</text>
<text x="54" y="198" text-anchor="middle" font-size="12" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">5</text>
<text x="54" y="232" text-anchor="middle" font-size="12" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">6</text>
<rect x="66" y="40" width="40" height="34" fill="none" stroke="#0f172a" stroke-width="1.2"/>
<text x="86" y="62" text-anchor="middle" font-size="13" font-weight="400" fill="#0f172a">2</text>
<rect x="106" y="40" width="40" height="34" fill="none" stroke="#0f172a" stroke-width="1.2"/>
<text x="126" y="62" text-anchor="middle" font-size="13" font-weight="400" fill="#0f172a">3</text>
<rect x="146" y="40" width="40" height="34" fill="none" stroke="#0f172a" stroke-width="1.2"/>
<text x="166" y="62" text-anchor="middle" font-size="13" font-weight="400" fill="#0f172a">4</text>
<rect x="186" y="40" width="40" height="34" fill="none" stroke="#0f172a" stroke-width="1.2"/>
<text x="206" y="62" text-anchor="middle" font-size="13" font-weight="400" fill="#0f172a">5</text>
<rect x="226" y="40" width="40" height="34" fill="none" stroke="#0f172a" stroke-width="1.2"/>
<text x="246" y="62" text-anchor="middle" font-size="13" font-weight="400" fill="#0f172a">6</text>
<rect x="266" y="40" width="40" height="34" fill="none" stroke="#0f172a" stroke-width="1.2"/>
<text x="286" y="62" text-anchor="middle" font-size="13" font-weight="400" fill="#0f172a">7</text>
<rect x="66" y="74" width="40" height="34" fill="none" stroke="#0f172a" stroke-width="1.2"/>
<text x="86" y="96" text-anchor="middle" font-size="13" font-weight="400" fill="#0f172a">3</text>
<rect x="106" y="74" width="40" height="34" fill="none" stroke="#0f172a" stroke-width="1.2"/>
<text x="126" y="96" text-anchor="middle" font-size="13" font-weight="400" fill="#0f172a">4</text>
<rect x="146" y="74" width="40" height="34" fill="none" stroke="#0f172a" stroke-width="1.2"/>
<text x="166" y="96" text-anchor="middle" font-size="13" font-weight="400" fill="#0f172a">5</text>
<rect x="186" y="74" width="40" height="34" fill="none" stroke="#0f172a" stroke-width="1.2"/>
<text x="206" y="96" text-anchor="middle" font-size="13" font-weight="400" fill="#0f172a">6</text>
<rect x="226" y="74" width="40" height="34" fill="none" stroke="#0f172a" stroke-width="1.2"/>
<text x="246" y="96" text-anchor="middle" font-size="13" font-weight="400" fill="#0f172a">7</text>
<rect x="266" y="74" width="40" height="34" fill="#b45309" fill-opacity="0.28" stroke="#0f172a" stroke-width="1.2"/>
<text x="286" y="96" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a">8</text>
<rect x="66" y="108" width="40" height="34" fill="none" stroke="#0f172a" stroke-width="1.2"/>
<text x="86" y="130" text-anchor="middle" font-size="13" font-weight="400" fill="#0f172a">4</text>
<rect x="106" y="108" width="40" height="34" fill="none" stroke="#0f172a" stroke-width="1.2"/>
<text x="126" y="130" text-anchor="middle" font-size="13" font-weight="400" fill="#0f172a">5</text>
<rect x="146" y="108" width="40" height="34" fill="none" stroke="#0f172a" stroke-width="1.2"/>
<text x="166" y="130" text-anchor="middle" font-size="13" font-weight="400" fill="#0f172a">6</text>
<rect x="186" y="108" width="40" height="34" fill="none" stroke="#0f172a" stroke-width="1.2"/>
<text x="206" y="130" text-anchor="middle" font-size="13" font-weight="400" fill="#0f172a">7</text>
<rect x="226" y="108" width="40" height="34" fill="#b45309" fill-opacity="0.28" stroke="#0f172a" stroke-width="1.2"/>
<text x="246" y="130" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a">8</text>
<rect x="266" y="108" width="40" height="34" fill="none" stroke="#0f172a" stroke-width="1.2"/>
<text x="286" y="130" text-anchor="middle" font-size="13" font-weight="400" fill="#0f172a">9</text>
<rect x="66" y="142" width="40" height="34" fill="none" stroke="#0f172a" stroke-width="1.2"/>
<text x="86" y="164" text-anchor="middle" font-size="13" font-weight="400" fill="#0f172a">5</text>
<rect x="106" y="142" width="40" height="34" fill="none" stroke="#0f172a" stroke-width="1.2"/>
<text x="126" y="164" text-anchor="middle" font-size="13" font-weight="400" fill="#0f172a">6</text>
<rect x="146" y="142" width="40" height="34" fill="none" stroke="#0f172a" stroke-width="1.2"/>
<text x="166" y="164" text-anchor="middle" font-size="13" font-weight="400" fill="#0f172a">7</text>
<rect x="186" y="142" width="40" height="34" fill="#b45309" fill-opacity="0.28" stroke="#0f172a" stroke-width="1.2"/>
<text x="206" y="164" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a">8</text>
<rect x="226" y="142" width="40" height="34" fill="none" stroke="#0f172a" stroke-width="1.2"/>
<text x="246" y="164" text-anchor="middle" font-size="13" font-weight="400" fill="#0f172a">9</text>
<rect x="266" y="142" width="40" height="34" fill="none" stroke="#0f172a" stroke-width="1.2"/>
<text x="286" y="164" text-anchor="middle" font-size="13" font-weight="400" fill="#0f172a">10</text>
<rect x="66" y="176" width="40" height="34" fill="none" stroke="#0f172a" stroke-width="1.2"/>
<text x="86" y="198" text-anchor="middle" font-size="13" font-weight="400" fill="#0f172a">6</text>
<rect x="106" y="176" width="40" height="34" fill="none" stroke="#0f172a" stroke-width="1.2"/>
<text x="126" y="198" text-anchor="middle" font-size="13" font-weight="400" fill="#0f172a">7</text>
<rect x="146" y="176" width="40" height="34" fill="#b45309" fill-opacity="0.28" stroke="#0f172a" stroke-width="1.2"/>
<text x="166" y="198" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a">8</text>
<rect x="186" y="176" width="40" height="34" fill="none" stroke="#0f172a" stroke-width="1.2"/>
<text x="206" y="198" text-anchor="middle" font-size="13" font-weight="400" fill="#0f172a">9</text>
<rect x="226" y="176" width="40" height="34" fill="none" stroke="#0f172a" stroke-width="1.2"/>
<text x="246" y="198" text-anchor="middle" font-size="13" font-weight="400" fill="#0f172a">10</text>
<rect x="266" y="176" width="40" height="34" fill="none" stroke="#0f172a" stroke-width="1.2"/>
<text x="286" y="198" text-anchor="middle" font-size="13" font-weight="400" fill="#0f172a">11</text>
<rect x="66" y="210" width="40" height="34" fill="none" stroke="#0f172a" stroke-width="1.2"/>
<text x="86" y="232" text-anchor="middle" font-size="13" font-weight="400" fill="#0f172a">7</text>
<rect x="106" y="210" width="40" height="34" fill="#b45309" fill-opacity="0.28" stroke="#0f172a" stroke-width="1.2"/>
<text x="126" y="232" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a">8</text>
<rect x="146" y="210" width="40" height="34" fill="none" stroke="#0f172a" stroke-width="1.2"/>
<text x="166" y="232" text-anchor="middle" font-size="13" font-weight="400" fill="#0f172a">9</text>
<rect x="186" y="210" width="40" height="34" fill="none" stroke="#0f172a" stroke-width="1.2"/>
<text x="206" y="232" text-anchor="middle" font-size="13" font-weight="400" fill="#0f172a">10</text>
<rect x="226" y="210" width="40" height="34" fill="none" stroke="#0f172a" stroke-width="1.2"/>
<text x="246" y="232" text-anchor="middle" font-size="13" font-weight="400" fill="#0f172a">11</text>
<rect x="266" y="210" width="40" height="34" fill="none" stroke="#0f172a" stroke-width="1.2"/>
<text x="286" y="232" text-anchor="middle" font-size="13" font-weight="400" fill="#0f172a">12</text>
</svg>
:::

Sur la figure, une case est un couple (rouge, vert) : card Ω = 36, et chaque case a la même probabilité 1/36 parce que les deux dés sont équilibrés. Les cases colorées sont les cas favorables.

::: exemple La somme vaut 8

1. L'univers est l'ensemble des couples (r, v) : card Ω = 6 × 6 = 36, chaque dé ayant 6 faces. Ils sont équiprobables, car les dés sont équilibrés.
2. Somme 8 : (2 ; 6), (3 ; 5), (4 ; 4), (5 ; 3) et (6 ; 2), donc 5 cas favorables, les cases colorées.
3. p = card A / card Ω = 5/36.

:::

::: exemple Le plus grand des deux résultats vaut 4

1. Même univers : card Ω = 36.
2. Le plus grand vaut 4 si l'un des dés donne 4 et l'autre au plus 4 : (4 ; 1), (4 ; 2), (4 ; 3), (4 ; 4), puis (1 ; 4), (2 ; 4), (3 ; 4), soit 7 couples ((4 ; 4) n'est compté qu'une fois).
3. p = 7/36.

:::

::: piege
**Erreur : prendre pour univers les sommes {2, 3, …, 12} comme si elles étaient équiprobables.** L'erreur tente parce qu'il n'y a que 11 valeurs et qu'on dirait « 1 chance sur 11 ». Mais la somme 2 n'a qu'un couple, (1 ; 1), alors que la somme 7 en a six : les sommes ne sont pas équiprobables, les couples le sont. La probabilité de la somme 8 est 5/36, pas 1/11.
:::

::: propriete
Pour appliquer p(A) = card A / card Ω, il faut que les événements élémentaires soient équiprobables, et l'énoncé le dit : dé équilibré, boule tirée au hasard, jetons indiscernables.
Cas limite : un dé truqué où la probabilité de chaque face est proportionnelle à son numéro n'est pas uniforme. Comme 1 + 2 + … + 6 = 21, la face i a pour probabilité i/21, et p(pair) = (2 + 4 + 6)/21 = 12/21 = 4/7, et non 3/6.
:::

::: verifie À toi : un produit impair
On lance deux dés équilibrés. Quelle est la probabilité que le produit des deux résultats soit impair ?

---

L'univers est formé des 36 couples équiprobables. Un produit est impair si et seulement si les deux facteurs sont impairs : 3 choix pour chaque dé, donc 3 × 3 = 9 cas favorables. Ainsi p = 9/36 = 1/4.
:::

::: retenir
En équiprobabilité, p(A) = card A / card Ω : on compte les couples ou les tirages équiprobables, jamais des valeurs qui ne le sont pas.
:::

## 🧮 Dénombrer les tirages : avec remise, sans remise, simultané

Un sac contient 8 jetons, 5 rouges et 3 verts. On en tire trois.
Le nombre de tirages possibles change-t-il selon qu'on remet chaque jeton, qu'on ne le remet pas ou qu'on prend les trois d'un seul geste ? Et la probabilité d'obtenir trois jetons rouges ?

::: definition
Pour 1 ≤ p ≤ n, le nombre d'**arrangements** de p éléments parmi n est Aₙᵖ = n(n − 1)(n − 2)…(n − p + 1), et le nombre de **combinaisons** est Cₙᵖ = Aₙᵖ / p! = n! / (p!(n − p)!).
Un arrangement tient compte de l'ordre, une combinaison non : chaque groupe de p éléments donne p! arrangements.
:::

Le mode de tirage fixe le nombre de cas possibles :

| Tirage | L'ordre | Un cas possible | card Ω |
| --- | --- | --- | --- |
| successifs avec remise | compte | p-uplet, répétitions possibles | nᵖ |
| successifs sans remise | compte | p-uplet d'éléments distincts | Aₙᵖ |
| simultanés | ne compte pas | partie de p éléments | Cₙᵖ |

Sur le tableau, on lit la question à se poser : « remet-on le jeton ? l'ordre compte-t-il ? ». Les jetons du sac étant tirés au hasard, chaque cas possible est équiprobable.

::: exemple Les trois jetons rouges

1. Avec remise : 8 choix à chaque tirage, donc card Ω = 8³ = 512 ; cas favorables 5³ = 125, donc p = 125/512.
2. Sans remise : card Ω = A₈³ = 8 × 7 × 6 = 336 (un jeton de moins à chaque tirage) ; cas favorables A₅³ = 5 × 4 × 3 = 60, donc p = 60/336 = 5/28.
3. Simultané : card Ω = C₈³ = 336/3! = 336/6 = 56 ; cas favorables C₅³ = 10, donc p = 10/56 = 5/28.
4. Les deux derniers résultats coïncident : « trois rouges » ne dépend pas de l'ordre, et chaque groupe compte 3! = 6 fois au numérateur comme au dénominateur.

:::

::: exemple Au moins un jeton vert (tirage simultané)

1. Le contraire de « au moins un vert » est « aucun vert », c'est-à-dire trois rouges, de probabilité 5/28.
2. Donc p(au moins un vert) = 1 − 5/28 = 23/28.

:::

::: piege
**Erreur : compter le numérateur en combinaisons et le dénominateur en arrangements.** L'erreur tente parce que les deux formules sont proches. Avec C₅³ = 10 et A₈³ = 336, on trouverait 10/336 = 5/168 au lieu de 5/28. Les cas favorables et les cas possibles se comptent toujours de la même façon, avec ou sans l'ordre.
:::

::: methode
Pour une probabilité de tirage :
1. lire le mode : avec remise, sans remise ou simultané ;
2. choisir nᵖ, Aₙᵖ ou Cₙᵖ pour card Ω ;
3. compter les cas favorables de la même façon ;
4. diviser, ou passer par le contraire quand « au moins » est demandé.

Cas limite : si on tire tous les éléments à la fois (p = n), Cₙⁿ = 1 : un seul tirage possible.
:::

::: verifie À toi : deux jetons de même couleur
On tire simultanément 2 jetons dans le même sac (5 rouges, 3 verts). Quelle est la probabilité qu'ils soient de la même couleur ?

---

card Ω = C₈² = 28. Deux jetons de même couleur : deux rouges, C₅² = 10 façons, ou deux verts, C₃² = 3 façons ; ces deux cas sont incompatibles, donc 10 + 3 = 13 cas favorables. Ainsi p = 13/28 : on a compté favorables et possibles en combinaisons, sans ordre.
:::

::: retenir
Avec remise, nᵖ ; sans remise, Aₙᵖ ; simultané, Cₙᵖ : on compte favorables et possibles de la même façon, et « au moins un » passe par le contraire.
:::

## 🔎 Probabilité conditionnelle : quand une information arrive

Un club compte 80 adhérents : 44 filles et 36 garçons. On rencontre un adhérent au hasard et on apprend que c'est une fille.
Parmi les filles, 28 font de la natation et 16 du football. Quelle est la probabilité qu'elle fasse de la natation, sachant que c'est une fille ?

::: definition
Soit B un événement tel que p(B) ≠ 0. La **probabilité de A sachant B**, notée p(A/B) (ou p_B(A)), est le nombre
$$ p(A/B) = p(A ∩ B) / p(B) $$
L'information « B est réalisé » remplace l'univers Ω par B.
:::

Le tableau des effectifs du club :

| | Football | Natation | Total |
| --- | --- | --- | --- |
| Garçons | 24 | 12 | 36 |
| Filles | 16 | 28 | 44 |
| Total | 40 | 40 | 80 |

Sur le tableau, la ligne « Filles » est le nouvel univers : ses 44 adhérentes remplacent les 80 adhérents, et la case « Filles, Natation » est A ∩ B.

::: exemple Une fille fait-elle de la natation ?

1. Notons F « l'adhérent est une fille » et N « il fait de la natation » : p(F) = 44/80 = 11/20 et p(N ∩ F) = 28/80 = 7/20.
2. p(N/F) = p(N ∩ F) / p(F) = (7/20)/(11/20) = 7/11, soit environ 0,64.
3. Contrôle sur le tableau : 28 nageuses parmi 44 filles, 28/44 = 7/11 ✓, le même nombre.
4. Sans l'information, p(N) = 40/80 = 1/2, différent de 7/11 : savoir que c'est une fille change la probabilité.

:::

::: piege
**Erreur : confondre p(N/F) et p(F/N).** L'erreur tente parce que les deux contiennent N et F et le même numérateur 28. Mais p(F/N) = 28/40 = 7/10 répond à une autre question (parmi les nageurs, quelle part de filles ?). Le dénominateur est toujours l'événement placé après « sachant » : ici 44 filles pour p(N/F), 40 nageurs pour p(F/N).
:::

::: propriete
Soit B un événement tel que p(B) ≠ 0 :
- p(Ω/B) = 1 ;
- si A₁ et A₂ sont incompatibles, p(A₁ ∪ A₂ / B) = p(A₁/B) + p(A₂/B) ;
- p(A̅ / B) = 1 − p(A/B).

Cas limite : on ne conditionne jamais par un événement de probabilité nulle, car la division par p(B) n'aurait pas de sens.
Dans l'exemple, p(N̅ / F) = 1 − 7/11 = 4/11 = 16/44 : ce sont les footballeuses ✓.
:::

::: verifie À toi : le premier dé vaut 3
On lance deux dés équilibrés. Sachant que le premier donne 3, quelle est la probabilité que la somme soit au moins égale à 8 ?

---

Notons B « le premier dé donne 3 » et S « la somme est au moins 8 » : p(B) = 6/36 et p(S ∩ B) = 2/36, car le deuxième dé doit donner 5 ou 6. Donc p(S/B) = (2/36)/(6/36) = 1/3. On retrouve le même nombre en comptant dans le nouvel univers B : 2 cas sur 6.
:::

::: retenir
p(A/B) = p(A ∩ B) / p(B) : on divise par la probabilité de ce qu'on sait, et p(A/B) ≠ p(B/A) en général.
:::

## 🔗 Événements indépendants

On lance deux dés équilibrés et on note la somme des deux résultats.
Si l'on sait que le premier dé a donné 6, la chance que la somme soit paire change-t-elle ?

::: definition
Deux événements A et B sont **indépendants** si et seulement si
$$ p(A ∩ B) = p(A) × p(B) $$
Si p(B) ≠ 0, cela équivaut à p(A/B) = p(A) : savoir que B est réalisé ne modifie pas la probabilité de A.
:::

| Événement | Probabilité |
| --- | --- |
| A « le premier dé donne 6 » | 6/36 = 1/6 |
| B « la somme est paire » | 18/36 = 1/2 |
| A ∩ B | 3/36 = 1/12 |
| p(A) × p(B) | 1/6 × 1/2 = 1/12 |

Sur le tableau, la dernière ligne égale la troisième : c'est la définition de l'indépendance, lue sur les nombres. B est réalisé quand les deux dés ont même parité (3 × 3 + 3 × 3 = 18 couples), et A ∩ B contient (6 ; 2), (6 ; 4) et (6 ; 6).

::: exemple Le premier dé et la parité de la somme

1. Les 36 couples sont équiprobables : p(A) = 6/36 = 1/6, p(B) = 18/36 = 1/2 et p(A ∩ B) = 3/36 = 1/12.
2. p(A) × p(B) = 1/12 et p(A ∩ B) = 1/12 : ils sont égaux, donc A et B sont indépendants.
3. Contrôle par le conditionnel : p(B/A) = (1/12)/(1/6) = 1/2 = p(B) ✓. Savoir que le premier dé vaut 6 ne change pas la chance d'une somme paire.

:::

::: exemple Le premier dé et une somme égale à 12

1. Soit C « la somme vaut 12 » : p(C) = 1/36 et A ∩ C = {(6 ; 6)}, donc p(A ∩ C) = 1/36.
2. p(A) × p(C) = 1/6 × 1/36 = 1/216, différent de 1/36 : A et C ne sont pas indépendants.
3. Contrôle : p(C/A) = (1/36)/(1/6) = 1/6, bien supérieur à p(C) = 1/36 : savoir que le premier dé vaut 6 rend la somme 12 six fois plus probable.

:::

::: piege
**Erreur : croire que des événements incompatibles sont indépendants.** L'erreur tente parce que « incompatible » et « indépendant » semblent dire « sans lien ». Soit D « le premier dé donne 1 » : A et D sont incompatibles, p(A ∩ D) = 0, alors que p(A) × p(D) = 1/36 ≠ 0. Si A est réalisé, D ne peut plus l'être : le lien est total, pas nul.
:::

::: propriete
Si A et B sont indépendants, alors A̅ et B̅ le sont aussi (et réciproquement).
Contrôle sur l'exemple : p(A̅ ∩ B̅) = 1 − p(A ∪ B) = 1 − (1/6 + 1/2 − 1/12) = 5/12, et p(A̅) × p(B̅) = 5/6 × 1/2 = 5/12 ✓.
Cas limite : deux événements incompatibles de probabilités non nulles ne sont jamais indépendants.
:::

::: verifie À toi : hebdomadaires et mensuels
Dans un sondage, 25 % des personnes lisent un hebdomadaire (H), 40 % un mensuel (M) et 10 % lisent les deux. H et M sont-ils indépendants ?

---

On compare p(H ∩ M) = 0,10 à p(H) × p(M) = 0,25 × 0,40 = 0,10 : les deux nombres sont égaux, donc H et M sont indépendants. Contrôle : p(M/H) = 0,10/0,25 = 0,40 = p(M).
:::

::: retenir
A et B sont indépendants si p(A ∩ B) = p(A) × p(B) : on le vérifie par le calcul, et incompatible n'est pas indépendant.
:::

## 🌳 Probabilités composées et arbre pondéré

Dans un atelier, la machine M produit 30 % des vis et la machine N le reste. 5 % des vis de M sont défectueuses, et 2 % de celles de N.
On prend une vis au hasard : quelle est la probabilité qu'elle vienne de M et qu'elle soit défectueuse ?

::: definition
Un **arbre pondéré** représente une succession d'événements : chaque branche porte la probabilité de l'événement qu'elle atteint, **sachant** les événements précédents du chemin. Deux règles : les branches issues d'un même nœud ont une somme égale à 1, et la probabilité d'un chemin est le **produit** des probabilités de ses branches.
:::

::: figure L'arbre de l'atelier : sur chaque nœud les deux branches ont pour somme 1, et la probabilité d'un chemin s'écrit à son extrémité
<svg viewBox="0 0 400 250">
<title>Arbre des vis : machine M ou N, puis vis défectueuse D ou non</title>
<g fill="none" stroke="#0f172a" stroke-width="2">
<path d="M24 125.0 L112 59.0"/>
<path d="M112 59.0 L206 26.0"/>
<path d="M112 59.0 L206 92.0"/>
<path d="M24 125.0 L112 191.0"/>
<path d="M112 191.0 L206 158.0"/>
<path d="M112 191.0 L206 224.0"/>
</g>
<circle cx="24" cy="125.0" r="4.5" fill="#0f172a"/>
<circle cx="112" cy="59.0" r="4.5" fill="#0f172a"/>
<circle cx="112" cy="191.0" r="4.5" fill="#0f172a"/>
<text x="68.0" y="85.0" text-anchor="middle" font-size="13" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0,3</text>
<text x="116" y="50.0" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">M</text>
<circle cx="206" cy="26.0" r="4" fill="#b45309"/>
<text x="159.0" y="35.5" text-anchor="middle" font-size="13" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0,05</text>
<text x="216" y="30.0" text-anchor="start" font-size="12" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">p(M ∩ D) = 0,015</text>
<circle cx="206" cy="92.0" r="4" fill="#0f172a"/>
<text x="159.0" y="90.5" text-anchor="middle" font-size="13" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0,95</text>
<text x="216" y="96.0" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">p(M ∩ D̅) = 0,285</text>
<text x="68.0" y="173.0" text-anchor="middle" font-size="13" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0,7</text>
<text x="116" y="213.0" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">N</text>
<circle cx="206" cy="158.0" r="4" fill="#0f172a"/>
<text x="159.0" y="167.5" text-anchor="middle" font-size="13" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0,02</text>
<text x="216" y="162.0" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">p(N ∩ D) = 0,014</text>
<circle cx="206" cy="224.0" r="4" fill="#0f172a"/>
<text x="159.0" y="222.5" text-anchor="middle" font-size="13" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0,98</text>
<text x="216" y="228.0" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">p(N ∩ D̅) = 0,686</text>
</svg>
:::

Sur la figure, M puis D est le chemin du haut : ses branches portent 0,3 puis 0,05, et p(M ∩ D) = 0,3 × 0,05 est écrit à son extrémité. La branche « 0,05 » est p(D/M), non p(D).

::: exemple La vis vient de M et elle est défectueuse

1. Notons M « la vis vient de M », N « la vis vient de N », D « la vis est défectueuse » : p(M) = 0,3, p(N) = 0,7, p(D/M) = 0,05 et p(D/N) = 0,02.
2. Chemin M puis D : p(M ∩ D) = p(M) × p(D/M) = 0,3 × 0,05 = 0,015, car 0,05 est la probabilité de D une fois M connu.
3. Les autres chemins : p(M ∩ D̅) = 0,3 × 0,95 = 0,285, p(N ∩ D) = 0,7 × 0,02 = 0,014 et p(N ∩ D̅) = 0,7 × 0,98 = 0,686.
4. Contrôle : 0,015 + 0,285 + 0,014 + 0,686 = 1 ✓, les quatre chemins couvrent Ω.

:::

::: exemple Trois tirages sans remise : rouge, rouge, blanche

Une urne contient 6 boules rouges et 4 blanches ; on tire trois boules successivement, sans remise.

1. Premier tirage : p(R₁) = 6/10.
2. Après une rouge, il reste 5 rouges et 4 blanches : p(R₂/R₁) = 5/9.
3. Après deux rouges, il reste 4 rouges et 4 blanches : p(B₃/R₁ ∩ R₂) = 4/8.
4. p(R₁ ∩ R₂ ∩ B₃) = 6/10 × 5/9 × 4/8 = 120/720 = 1/6.

:::

::: piege
**Erreur : utiliser les probabilités de départ à chaque tirage sans remise.** L'erreur tente parce qu'on recopie 6/10 à chaque rang. Elle donne 6/10 × 6/10 × 4/10 = 0,144 au lieu de 1/6 ≈ 0,167. Après chaque tirage la composition de l'urne change : on multiplie des probabilités conditionnelles, calculées sur l'urne restante.
:::

::: propriete
Si p(A) ≠ 0 et p(B) ≠ 0 :
$$ p(A ∩ B) = p(A) × p(B/A) = p(B) × p(A/B) $$
et, si p(A ∩ B) ≠ 0 :
$$ p(A ∩ B ∩ C) = p(A) × p(B/A) × p(C/(A ∩ B)) $$
Cas limite : si A et B sont indépendants, p(B/A) = p(B) et on retrouve p(A ∩ B) = p(A) × p(B).
:::

::: verifie À toi : le lecteur étudiant
Dans une bibliothèque, 55 % des lecteurs sont des étudiants ; parmi eux, 20 % empruntent un manuel. Quelle est la probabilité qu'un lecteur pris au hasard soit un étudiant qui emprunte un manuel ?

---

Notons E « le lecteur est un étudiant » et M « il emprunte un manuel » : p(E) = 0,55 et p(M/E) = 0,20, car 20 % se calcule parmi les étudiants. Alors p(E ∩ M) = p(E) × p(M/E) = 0,55 × 0,20 = 0,11, soit 11 % des lecteurs.
:::

::: retenir
Dans un arbre, on multiplie le long d'un chemin : p(A ∩ B) = p(A) × p(B/A), et chaque branche est conditionnelle à ce qui précède.
:::

## 🧩 Probabilités totales : additionner les chemins

Trois ateliers A₁, A₂ et A₃ fabriquent respectivement 45 %, 35 % et 20 % des pièces d'une usine, avec 2 %, 3 % et 5 % de pièces défectueuses.
On prend une pièce au hasard : quelle est la probabilité qu'elle soit défectueuse ?

::: definition
Des événements A₁, A₂, …, Aₙ de probabilités non nulles forment une **partition** de Ω s'ils sont deux à deux incompatibles et si leur réunion est Ω : chaque résultat appartient à un seul d'entre eux.
:::

::: figure L'arbre des trois ateliers : D est atteint par trois chemins incompatibles, ceux qui sont colorés
<svg viewBox="0 0 400 290">
<title>Arbre des trois ateliers : atelier d'origine, puis pièce défectueuse D ou non</title>
<g fill="none" stroke="#0f172a" stroke-width="2">
<path d="M24 145.0 L112 49.8"/>
<path d="M112 49.8 L206 26.0"/>
<path d="M112 49.8 L206 73.6"/>
<path d="M24 145.0 L112 145.0"/>
<path d="M112 145.0 L206 121.2"/>
<path d="M112 145.0 L206 168.8"/>
<path d="M24 145.0 L112 240.2"/>
<path d="M112 240.2 L206 216.4"/>
<path d="M112 240.2 L206 264.0"/>
</g>
<circle cx="24" cy="145.0" r="4.5" fill="#0f172a"/>
<circle cx="112" cy="49.8" r="4.5" fill="#0f172a"/>
<circle cx="112" cy="145.0" r="4.5" fill="#0f172a"/>
<circle cx="112" cy="240.2" r="4.5" fill="#0f172a"/>
<text x="68.0" y="90.4" text-anchor="middle" font-size="13" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0,45</text>
<text x="116" y="40.8" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">A₁</text>
<circle cx="206" cy="26.0" r="4" fill="#b45309"/>
<text x="159.0" y="30.9" text-anchor="middle" font-size="13" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0,02</text>
<text x="216" y="30.0" text-anchor="start" font-size="12" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">p(A₁ ∩ D) = 0,009</text>
<circle cx="206" cy="73.6" r="4" fill="#0f172a"/>
<text x="159.0" y="76.7" text-anchor="middle" font-size="13" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0,98</text>
<text x="216" y="77.6" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">p(A₁ ∩ D̅) = 0,441</text>
<text x="68.0" y="138.0" text-anchor="middle" font-size="13" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0,35</text>
<text x="116" y="136.0" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">A₂</text>
<circle cx="206" cy="121.2" r="4" fill="#b45309"/>
<text x="159.0" y="126.1" text-anchor="middle" font-size="13" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0,03</text>
<text x="216" y="125.2" text-anchor="start" font-size="12" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">p(A₂ ∩ D) = 0,0105</text>
<circle cx="206" cy="168.8" r="4" fill="#0f172a"/>
<text x="159.0" y="171.9" text-anchor="middle" font-size="13" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0,97</text>
<text x="216" y="172.8" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">p(A₂ ∩ D̅) = 0,3395</text>
<text x="68.0" y="207.6" text-anchor="middle" font-size="13" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0,2</text>
<text x="116" y="262.2" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">A₃</text>
<circle cx="206" cy="216.4" r="4" fill="#b45309"/>
<text x="159.0" y="221.3" text-anchor="middle" font-size="13" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0,05</text>
<text x="216" y="220.4" text-anchor="start" font-size="12" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">p(A₃ ∩ D) = 0,01</text>
<circle cx="206" cy="264.0" r="4" fill="#0f172a"/>
<text x="159.0" y="267.1" text-anchor="middle" font-size="13" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0,95</text>
<text x="216" y="268.0" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">p(A₃ ∩ D̅) = 0,19</text>
</svg>
:::

Sur la figure, les trois chemins colorés aboutissent à D ; leurs probabilités, à droite, s'additionnent. Les trois branches issues de la racine ont pour somme 0,45 + 0,35 + 0,20 = 1.

::: exemple La pièce est défectueuse

1. Chaque pièce vient d'un atelier et d'un seul : A₁, A₂, A₃ forment une partition, de poids 0,45 + 0,35 + 0,20 = 1.
2. Chemins vers D : p(A₁ ∩ D) = 0,45 × 0,02 = 0,009, p(A₂ ∩ D) = 0,35 × 0,03 = 0,0105 et p(A₃ ∩ D) = 0,20 × 0,05 = 0,010.
3. D est la réunion de ces trois événements incompatibles, donc p(D) = 0,009 + 0,0105 + 0,010 = 0,0295, soit 2,95 %.
4. Contrôle : 2,95 % est compris entre 2 % et 5 %, et plus proche de 3 % que de 5 %, car les deux plus gros ateliers ont de faibles taux ✓.

:::

::: piege
**Erreur : faire la moyenne simple des taux.** L'erreur tente parce que « moyenne » semble équitable : (2 + 3 + 5)/3 = 3,33 %. Mais les ateliers ne produisent pas autant : l'atelier A₃ ne fait que 20 % des pièces, et le taux de chaque atelier est pondéré par sa part. Le bon résultat est 2,95 %, pas 3,33 %.
:::

::: propriete
Si A₁, …, Aₙ forment une partition de Ω, alors pour tout événement B :
$$ p(B) = p(A₁) × p(B/A₁) + p(A₂) × p(B/A₂) + … + p(Aₙ) × p(B/Aₙ) $$
Avec la partition {A, A̅}, où 0 < p(A) < 1 : p(B) = p(A) × p(B/A) + p(A̅) × p(B/A̅).
Cas limite : si p(B/A) = p(B/A̅) = q, alors p(B) = q, car p(A) × q + p(A̅) × q = q : l'information A ne change rien.
:::

::: verifie À toi : deux urnes
On choisit au hasard (avec la probabilité 1/2 chacune) l'urne U₁ (2 rouges, 3 noires) ou l'urne U₂ (4 rouges, 1 noire), puis on y tire une boule. Quelle est la probabilité qu'elle soit rouge ?

---

U₁ et U₂ forment une partition de poids 1/2 chacune, avec p(R/U₁) = 2/5 et p(R/U₂) = 4/5. Donc p(R) = 1/2 × 2/5 + 1/2 × 4/5 = 1/5 + 2/5 = 3/5 : on additionne les deux chemins qui mènent à « rouge », chacun pondéré par le poids de son urne.
:::

::: retenir
p(B) = Σ p(Aₖ) × p(B/Aₖ) : sur l'arbre, on additionne tous les chemins qui aboutissent à B, après avoir multiplié le long de chacun.
:::

## ↩️ Formule de Bayes : remonter aux causes

Une maladie touche 1 personne sur 100. Un test est positif chez 95 % des malades, mais aussi chez 4 % des personnes saines.
Ton test est positif : quelle est la probabilité que tu sois vraiment malade ? Est-elle proche de 95 % ?

::: figure L'arbre du dépistage : T est atteint par les deux chemins colorés, mais un seul passe par M
<svg viewBox="0 0 400 250">
<title>Arbre du dépistage : malade M ou non, puis test positif T ou négatif</title>
<g fill="none" stroke="#0f172a" stroke-width="2">
<path d="M24 125.0 L112 59.0"/>
<path d="M112 59.0 L206 26.0"/>
<path d="M112 59.0 L206 92.0"/>
<path d="M24 125.0 L112 191.0"/>
<path d="M112 191.0 L206 158.0"/>
<path d="M112 191.0 L206 224.0"/>
</g>
<circle cx="24" cy="125.0" r="4.5" fill="#0f172a"/>
<circle cx="112" cy="59.0" r="4.5" fill="#0f172a"/>
<circle cx="112" cy="191.0" r="4.5" fill="#0f172a"/>
<text x="68.0" y="85.0" text-anchor="middle" font-size="13" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0,01</text>
<text x="116" y="50.0" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">M</text>
<circle cx="206" cy="26.0" r="4" fill="#b45309"/>
<text x="159.0" y="35.5" text-anchor="middle" font-size="13" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0,95</text>
<text x="216" y="30.0" text-anchor="start" font-size="12" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">p(M ∩ T) = 0,0095</text>
<circle cx="206" cy="92.0" r="4" fill="#0f172a"/>
<text x="159.0" y="90.5" text-anchor="middle" font-size="13" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0,05</text>
<text x="216" y="96.0" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">p(M ∩ T̅) = 0,0005</text>
<text x="68.0" y="173.0" text-anchor="middle" font-size="13" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0,99</text>
<text x="116" y="213.0" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">M̅</text>
<circle cx="206" cy="158.0" r="4" fill="#b45309"/>
<text x="159.0" y="167.5" text-anchor="middle" font-size="13" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0,04</text>
<text x="216" y="162.0" text-anchor="start" font-size="12" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">p(M̅ ∩ T) = 0,0396</text>
<circle cx="206" cy="224.0" r="4" fill="#0f172a"/>
<text x="159.0" y="222.5" text-anchor="middle" font-size="13" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0,96</text>
<text x="216" y="228.0" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">p(M̅ ∩ T̅) = 0,9504</text>
</svg>
:::

Sur la figure, la première branche porte p(M) = 0,01 et la dernière p(T/M̅) = 0,04. Savoir que T est réalisé, c'est ne garder que les deux chemins colorés.

::: exemple Le test est positif

1. Notons M « la personne est malade » et T « le test est positif » : p(M) = 0,01, p(T/M) = 0,95 et p(T/M̅) = 0,04.
2. Chemins vers T : p(M ∩ T) = 0,01 × 0,95 = 0,0095 et p(M̅ ∩ T) = 0,99 × 0,04 = 0,0396.
3. Probabilités totales : p(T) = 0,0095 + 0,0396 = 0,0491.
4. Définition du conditionnel : p(M/T) = p(M ∩ T) / p(T) = 0,0095/0,0491 = 95/491, soit environ 0,19.
5. Contrôle sur 10 000 personnes : 100 malades dont 95 positives, et 9 900 saines dont 396 positives ; sur 95 + 396 = 491 positives, 95 sont malades : 95/491 ✓.

:::

::: exemple Retour aux causes : quel atelier ?

On reprend l'usine des trois ateliers : p(D) = 0,0295. Une pièce défectueuse est choisie ; de quel atelier vient-elle ?

1. p(A₁/D) = p(A₁ ∩ D) / p(D) = 0,009/0,0295 = 18/59 ≈ 0,31.
2. p(A₂/D) = 0,0105/0,0295 = 21/59 ≈ 0,36.
3. p(A₃/D) = 0,010/0,0295 = 20/59 ≈ 0,34.
4. Contrôle : 18/59 + 21/59 + 20/59 = 1 ✓. L'atelier A₃ ne fait que 20 % des pièces mais 34 % des pièces défectueuses.

:::

::: piege
**Erreur : lire « test fiable à 95 % » comme « si le test est positif, malade à 95 % ».** L'erreur tente parce que les deux phrases parlent de 95 %. Mais 95 % est p(T/M), alors que la question est p(M/T) : on conditionne par T, non par M. La maladie est rare, donc la plupart des positifs sont des faux positifs : p(M/T) ≈ 0,19.
:::

::: propriete
Si p(A) ≠ 0 et 0 < p(B) < 1 :
$$ p(B/A) = p(B) × p(A/B) / [p(B) × p(A/B) + p(B̅) × p(A/B̅)] $$
Le numérateur est p(B ∩ A), et le dénominateur est p(A) obtenu par les probabilités totales.
Cas limite : si p(A/B̅) = 0, le dénominateur égale le numérateur et p(B/A) = 1. Un test sans faux positif rend sûre la maladie d'un positif.
:::

::: verifie À toi : de quelle boîte vient la fiche
On choisit au hasard (avec la probabilité 1/2 chacune) la boîte B₁, qui contient 1 fiche gagnante sur 4, ou la boîte B₂, qui en contient 3 sur 4, puis on y tire une fiche. Elle est gagnante : quelle est la probabilité qu'elle vienne de B₂ ?

---

Notons G « la fiche est gagnante ». p(B₂ ∩ G) = 1/2 × 3/4 = 3/8 et p(G) = 1/2 × 1/4 + 1/2 × 3/4 = 1/8 + 3/8 = 4/8 par les probabilités totales. Bayes donne p(B₂/G) = (3/8)/(4/8) = 3/4 : sur les quatre huitièmes de gagnantes, trois viennent de B₂.
:::

::: retenir
Bayes remonte de l'effet à la cause : p(B/A) = p(B ∩ A) / p(A), avec p(A) donné par les probabilités totales ; p(B/A) n'est pas p(A/B).
:::

> 🏆 Les huit notions sont acquises : tu écris le langage des événements, tu comptes par équiprobabilité et par dénombrement, tu conditionnes, tu testes l'indépendance, tu multiplies le long d'un arbre, tu additionnes ses chemins et tu remontes aux causes par la formule de Bayes. Prochaine étape : les variables aléatoires réelles.
