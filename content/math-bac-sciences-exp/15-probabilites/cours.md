# ⚔️ Probabilités sur un ensemble fini — mesurer le hasard

> 💡 «Quand un tournoi s'interrompt avant la fin, qui mérite quelle part du prix ? De cette seule question est né le calcul des probabilités.»

Ce chapitre apprend à compter les issues d'une expérience, à donner à chaque événement un nombre entre 0 et 1, puis à corriger ce nombre quand une information tombe. Huit notions : les listes et les arrangements, les combinaisons, la probabilité sur un ensemble fini, l'équiprobabilité, la probabilité conditionnelle, l'indépendance, les probabilités totales et, pour finir, les suites de probabilités qui se répètent d'un jour à l'autre. On y réutilise les suites géométriques et leurs limites du chapitre 2.

## 🔢 Compter des listes : p-uplets et arrangements

Un cadenas à trois molettes porte sur chacune les lettres A, B, C et D. Combien de codes différents peut-il afficher ?
Et si un jury décerne l'or, l'argent et le bronze à trois finalistes différents choisis parmi six, combien de podiums sont possibles ?
Dans les deux cas, on compte des listes ordonnées ; la différence tient à une seule question : un élément peut-il resservir ?

::: definition
Soit E un ensemble à n éléments et p un entier naturel non nul.
- Un **p-uplet** d'éléments de E est une liste ordonnée de p éléments, répétitions permises. Il y en a **nᵖ**.
- Si 1 ≤ p ≤ n, un **arrangement** de p éléments de E est un p-uplet d'éléments **deux à deux distincts**. Il y en a
$$ A_n^p = n!/(n − p)! = n × (n − 1) × ... × (n − p + 1) $$
- Les n-uplets d'éléments deux à deux distincts (p = n) sont les rangements de tous les éléments : il y en a **n!**.

:::

::: exemple Les codes du cadenas
1. Chaque molette tourne indépendamment des autres et peut afficher n'importe quelle lettre : un code est un 3-uplet d'éléments de {A, B, C, D}, répétitions permises (le code AAB existe).
2. Chaque molette offre 4 lettres : 4 × 4 × 4 = 4³ = **64** codes.
3. Contrôle : les codes qui commencent par A sont 4 × 4 = 16, et la première molette a 4 lettres possibles, donc 4 × 16 = 64 ✓.

:::

::: exemple Les podiums
1. L'ordre compte (l'or n'est pas le bronze) et un finaliste ne reçoit qu'une médaille : c'est un arrangement de 3 éléments parmi 6.
2. 6 choix pour l'or, puis 5 pour l'argent (le vainqueur est déjà placé), puis 4 pour le bronze : 6 × 5 × 4 = **120** podiums.
3. Avec la formule : A_6^3 = 6!/3! = 720/6 = 120 ✓.

:::

::: exemple Au moins un 1 en quatre tirages
Une urne contient quatre boules numérotées 1, 2, 3, 4 ; on tire quatre fois une boule en la remettant à chaque fois.
1. Les tirages forment un 4-uplet de {1, 2, 3, 4} : 4⁴ = 256 tirages en tout.
2. Les tirages **sans** aucun 1 n'utilisent que 3 numéros à chaque rang : 3⁴ = 81.
3. Un tirage est soit sans 1, soit avec au moins un 1 : il y a 256 − 81 = **175** tirages avec au moins un 1.

:::

::: piege
**Erreur : changer de modèle sans se demander si un élément peut resservir.** Pour le cadenas, A_4^3 = 4 × 3 × 2 = 24 oublie tous les codes qui répètent une lettre (AAB, ABA, …) : il en manque 40. Pour les podiums, 6³ = 216 autorise le même finaliste à gagner l'or et l'argent. La question à poser avant de compter : « le même élément peut-il apparaître deux fois dans la liste ? »
:::

::: propriete
- Répétitions permises (tirages avec remise, codes) : **nᵖ** listes.
- Éléments tous distincts (tirages sans remise, podiums) : **A_n^p = n!/(n − p)!**, et **n!** quand p = n.
- Cas limite : si p > n, aucun arrangement n'existe (on ne peut pas choisir 5 finalistes tous différents quand il n'y en a que 4) ; la formule A_n^p ne vaut que pour p ≤ n.

:::

::: verifie À toi : codes et listes distinctes
Un code se compose de 4 chiffres pris dans {1, 2, 3, 4, 5, 6}. Combien de codes existent si les chiffres peuvent se répéter ? Combien si les 4 chiffres doivent être deux à deux distincts ?

---

Répétitions permises : un 4-uplet d'un ensemble à 6 éléments, soit 6⁴ = 1296 codes. Chiffres distincts : un arrangement, soit A_6^4 = 6 × 5 × 4 × 3 = 360 codes. Le second modèle est une partie du premier, ce qui explique que 360 < 1296.
:::

::: retenir
Compter des listes ordonnées : nᵖ si un élément peut resservir, A_n^p = n!/(n − p)! s'ils sont tous distincts.
:::

## 🤝 Choisir sans ordre : les combinaisons

Une entraîneuse choisit quatre athlètes parmi les neuf de son club pour un relais, sans fixer leur ordre de passage. Combien de groupes différents peut-elle former ?
Le groupe {Amel, Bilel, Chedly, Dora} est le même quelle que soit la façon de l'écrire : l'ordre ne compte plus.

::: definition
Soit E un ensemble à n éléments et p un entier avec 1 ≤ p ≤ n. Le nombre de **parties à p éléments** de E (les choix de p éléments sans tenir compte de l'ordre) est
$$ C_n^p = n!/((n − p)! p!) $$
On convient que C_n^0 = 1.
:::

::: exemple Les groupes de relais
1. On cherche les parties à 4 éléments d'un ensemble à 9 éléments : C_9^4.
2. Si l'ordre comptait, on aurait A_9^4 = 9 × 8 × 7 × 6 = 3024 listes.
3. Chaque groupe est écrit 4! = 24 fois dans ces listes (les 24 façons de ranger ses quatre membres) : on divise, 3024/24 = **126** groupes.
4. La formule redonne le même nombre : C_9^4 = 9!/(5! 4!) = 126 ✓.

:::

::: exemple Les anagrammes de SALSA
1. Une anagramme est un rangement des 5 lettres, mais les deux S sont indiscernables, et les deux A aussi : on ne peut pas utiliser 5!.
2. On choisit les 2 places des S parmi 5 : C_5^2 = 10. Il reste 3 places, dont on choisit les 2 places des A : C_3^2 = 3 ; le L prend la dernière.
3. Il y a 10 × 3 × 1 = **30** anagrammes. Contrôle : 5!/(2! × 2!) = 120/4 = 30 ✓.

:::

::: exemple Un cube peint, puis découpé
Un cube de 4 cm d'arête, peint sur ses 6 faces, est découpé en 64 petits cubes de 1 cm.
1. Un petit cube a 3 faces peintes s'il est un sommet (8), 2 faces s'il est sur une arête sans en être un sommet (12 arêtes × 2 = 24), 1 face s'il est au milieu d'une face (6 × 4 = 24), aucune s'il est intérieur (2³ = 8). Total : 8 + 24 + 24 + 8 = 64 ✓.
2. On prend 3 petits cubes d'un seul geste. Choisir **exactement deux** cubes à trois faces peintes parmi les 8 sommets, puis le troisième parmi les 56 cubes qui ne sont pas des sommets : C_8^2 × C_56^1 = 28 × 56 = **1568** prélèvements.
3. Aucun cube peint n'est pris si les 3 viennent des 8 cubes intérieurs : C_8^3 = 56, donc C_64^3 − 56 = 41664 − 56 = **41608** prélèvements contiennent au moins un cube peint.

:::

::: piege
**Erreur : compter des listes quand l'énoncé demande un groupe.** Pour le relais, A_9^4 = 3024 attribue un rang à chaque athlète, alors que le groupe {Amel, Bilel, Chedly, Dora} ne distingue personne : 3024 est 24 fois trop grand. Le mot « successivement » invite à ranger ; les mots « d'un seul geste », « simultanément », « un groupe », « un comité » annoncent des parties.
:::

::: propriete
- Le lien entre les deux modèles : **A_n^p = p! × C_n^p** (choisir, puis ranger les p choisis).
- Cas limite : C_n^n = 1 (un seul choix possible : tout prendre) et C_n^0 = 1 (ne rien prendre).
- Pour a et b deux éléments fixés de E (n ≥ 2, 2 ≤ p ≤ n), une partie à p éléments contient a et b, ou exactement l'un des deux, ou aucun des deux, d'où
$$ C_n^p = C_(n−2)^(p−2) + 2C_(n−2)^(p−1) + C_(n−2)^p $$
Contrôle pour n = 7 et p = 3 : C_7^3 = 35, et C_5^1 + 2C_5^2 + C_5^3 = 5 + 20 + 10 = 35 ✓.
- En fonction de n : C_n^2 = n(n − 1)/2 et C_n^3 = n(n − 1)(n − 2)/6 ; par exemple, une urne de n rouges et 2n noires dont on tire 2 boules d'un seul geste donne p(deux rouges) = C_n^2/C_(3n)^2 = (n − 1)/(3(3n − 1)), qui tend vers 1/9 quand n tend vers +∞.

:::

::: verifie À toi : groupe ou liste ?
Un conseil de classe compte 10 élèves. On choisit 3 délégués sans rôle particulier. Combien de choix ? Combien si l'on désigne un délégué, un adjoint et un trésorier ?

---

Trois délégués sans rôle forment une partie : C_10^3 = 10!/(7! 3!) = 120. Avec trois rôles distincts, l'ordre compte : A_10^3 = 10 × 9 × 8 = 720, ce qui vaut bien 3! × 120 = 6 × 120.
:::

::: retenir
Un choix sans ordre est une partie à p éléments : C_n^p = n!/((n − p)! p!), liée aux arrangements par A_n^p = p! × C_n^p.
:::

## 🎲 Univers, événements et probabilité

Un dé à six faces est truqué : la face 6 sort trois fois plus souvent que chacune des cinq autres. Quelle chance a-t-on d'obtenir un nombre pair ?
On ne peut plus répondre en comptant des faces : il faut d'abord dire précisément ce qu'est une « chance » et comment elle se répartit sur les résultats possibles.

::: definition
Une **expérience aléatoire** est une expérience dont le résultat est soumis au hasard. L'ensemble E de ses issues est l'**univers** ; ses éléments sont les **événements élémentaires** ; une partie A de E est un **événement**. E est l'événement **certain**, ∅ l'événement **impossible**, A̅ l'événement **contraire** de A, et deux événements sont **incompatibles** si leur intersection est vide.

Une **probabilité** sur E est une application p de l'ensemble 𝒫(E) des événements dans [0, 1] telle que p(E) = 1, p(∅) = 0 et, pour tout événement A,
$$ p(A) = Σ p(aᵢ) $$
la somme portant sur les événements élémentaires aᵢ de A. Le triplet (E, 𝒫(E), p) est un **espace probabilisé fini**.
:::

::: exemple Le vocabulaire sur E = {1, 2, …, 20}
Soit A « le nombre est multiple de 4 » et B « le nombre est multiple de 6 ».
1. A = {4, 8, 12, 16, 20} a 5 éléments, B = {6, 12, 18} en a 3.
2. A ∩ B = {12} : un seul nombre est multiple de 4 et de 6 ; donc A et B ne sont pas incompatibles.
3. A ∪ B = {4, 6, 8, 12, 16, 18, 20} compte 5 + 3 − 1 = 7 éléments (12 ne doit être compté qu'une fois) ; le contraire de A ∪ B en compte 20 − 7 = 13.
4. A ∩ B̅ s'obtient en retirant 12 de A : {4, 8, 16, 20}, soit 4 éléments.

:::

::: exemple Le dé truqué
1. Notons x la probabilité de chacune des faces 1 à 5 ; celle du 6 est 3x.
2. La somme des probabilités élémentaires vaut p(E) = 1 : 5x + 3x = 8x = 1, donc x = 1/8 et p(6) = 3/8.
3. L'événement « pair » est {2, 4, 6} : p = 1/8 + 1/8 + 3/8 = **5/8**. Contrôle : « impair » = {1, 3, 5} vaut 3/8, et 5/8 + 3/8 = 1 ✓.

:::

::: exemple Deux défauts sur 1000 appareils
Sur 1000 appareils, 60 présentent le défaut D₁, 50 le défaut D₂ et 20 les deux ; on en prend un au hasard.
1. p(D₁) = 0,06, p(D₂) = 0,05 et p(D₁ ∩ D₂) = 0,02.
2. « Au moins un défaut » est D₁ ∪ D₂ : p = 0,06 + 0,05 − 0,02 = **0,09** ; on retranche l'intersection pour ne pas la compter deux fois.
3. « Aucun défaut » est le contraire : 1 − 0,09 = **0,91**. « Un seul défaut » : 0,09 − 0,02 = **0,07**.

:::

::: figure Les 1000 appareils : 40 portent D₁ seul, 20 portent D₁ et D₂, 30 portent D₂ seul, et les 910 restants sont hors des deux disques
<svg viewBox="0 0 340 230"><title>Diagramme de Venn : 40 appareils avec D₁ seul, 20 avec les deux défauts, 30 avec D₂ seul, 910 sans défaut</title><rect x="15" y="15" width="310" height="200" rx="6" fill="none" stroke="#94a3b8" stroke-width="2"/><circle cx="125" cy="115" r="62" fill="#0f6e56" fill-opacity="0.12" stroke="#0f172a" stroke-width="2"/><circle cx="215" cy="115" r="62" fill="#b45309" fill-opacity="0.12" stroke="#0f172a" stroke-width="2"/><text x="100" y="60" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">D₁</text><text x="240" y="60" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">D₂</text><text x="30" y="34" text-anchor="start" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">E</text><text x="98" y="120" text-anchor="middle" font-size="15" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">40</text><text x="170" y="120" text-anchor="middle" font-size="15" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">20</text><text x="242" y="120" text-anchor="middle" font-size="15" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">30</text><text x="290" y="200" text-anchor="middle" font-size="15" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">910</text></svg>
:::

Chaque nombre de la figure est un effectif : 40 + 20 = 60 pour D₁, 20 + 30 = 50 pour D₂, et 40 + 20 + 30 + 910 = 1000. Diviser par 1000 donne les probabilités du calcul ci-dessus.

::: piege
**Erreur : additionner p(A) + p(B) sans retrancher l'intersection.** Ici 0,06 + 0,05 = 0,11 semble donner « au moins un défaut », mais les 20 appareils à deux défauts ont été comptés deux fois : la bonne valeur est 0,09. L'addition simple n'est permise que si A ∩ B = ∅.
:::

::: propriete
Pour des événements A et B d'un espace probabilisé fini :
- **p(A̅) = 1 − p(A)** ;
- **p(A ∪ B) = p(A) + p(B) − p(A ∩ B)** ;
- si A ∩ B = ∅, alors p(A ∪ B) = p(A) + p(B), et plus généralement pour des événements deux à deux incompatibles A₁, …, A_k, p(A₁ ∪ … ∪ A_k) = p(A₁) + … + p(A_k).

Cas limite : si A = E, p(A̅) = p(∅) = 0, ce qui est cohérent avec p(E) = 1.
:::

::: verifie À toi : retrouver une intersection
Deux événements A et B vérifient p(A) = 0,45, p(B) = 0,3 et p(A ∪ B) = 0,6. Calculer p(A ∩ B), puis la probabilité de ne réaliser ni A ni B.

---

On isole l'intersection dans p(A ∪ B) = p(A) + p(B) − p(A ∩ B) : p(A ∩ B) = 0,45 + 0,3 − 0,6 = 0,15. « Ni A ni B » est le contraire de A ∪ B : 1 − 0,6 = 0,4. On a utilisé la formule de la réunion, puis celle du contraire.
:::

::: retenir
Une probabilité sur un ensemble fini donne p(E) = 1 et p(A) = somme des probabilités des événements élémentaires de A, d'où p(A̅) = 1 − p(A) et p(A ∪ B) = p(A) + p(B) − p(A ∩ B).
:::

## 🎯 Équiprobabilité : compter suffit

On lance en même temps un dé rouge et un dé vert. Quelle est la chance d'obtenir deux fois le même chiffre ?
Rien ne distingue un résultat d'un autre : si les dés sont équilibrés, aucun des couples (rouge ; vert) n'est plus probable qu'un autre, et la réponse devient une affaire de comptage.

::: definition
Dans une situation d'**équiprobabilité** (tous les événements élémentaires ont la même chance), la **probabilité uniforme** donne à chaque événement élémentaire a la probabilité p(a) = 1/card(E), et pour tout événement A
$$ p(A) = card(A)/card(E) $$
:::

::: figure Les 36 couples (rouge ; vert) : les 6 cases colorées, de la diagonale, sont les couples (i ; i) où les deux dés montrent le même chiffre
<svg viewBox="0 0 340 270"><title>Grille des 36 couples (dé rouge, dé vert) avec la diagonale des couples (i, i) en couleur</title><rect x="70" y="40" width="34" height="34" fill="#0f6e56" fill-opacity="0.35" stroke="#94a3b8" stroke-width="1.2"/><rect x="70" y="74" width="34" height="34" fill="#ffffff" fill-opacity="1" stroke="#94a3b8" stroke-width="1.2"/><rect x="70" y="108" width="34" height="34" fill="#ffffff" fill-opacity="1" stroke="#94a3b8" stroke-width="1.2"/><rect x="70" y="142" width="34" height="34" fill="#ffffff" fill-opacity="1" stroke="#94a3b8" stroke-width="1.2"/><rect x="70" y="176" width="34" height="34" fill="#ffffff" fill-opacity="1" stroke="#94a3b8" stroke-width="1.2"/><rect x="70" y="210" width="34" height="34" fill="#ffffff" fill-opacity="1" stroke="#94a3b8" stroke-width="1.2"/><rect x="104" y="40" width="34" height="34" fill="#ffffff" fill-opacity="1" stroke="#94a3b8" stroke-width="1.2"/><rect x="104" y="74" width="34" height="34" fill="#0f6e56" fill-opacity="0.35" stroke="#94a3b8" stroke-width="1.2"/><rect x="104" y="108" width="34" height="34" fill="#ffffff" fill-opacity="1" stroke="#94a3b8" stroke-width="1.2"/><rect x="104" y="142" width="34" height="34" fill="#ffffff" fill-opacity="1" stroke="#94a3b8" stroke-width="1.2"/><rect x="104" y="176" width="34" height="34" fill="#ffffff" fill-opacity="1" stroke="#94a3b8" stroke-width="1.2"/><rect x="104" y="210" width="34" height="34" fill="#ffffff" fill-opacity="1" stroke="#94a3b8" stroke-width="1.2"/><rect x="138" y="40" width="34" height="34" fill="#ffffff" fill-opacity="1" stroke="#94a3b8" stroke-width="1.2"/><rect x="138" y="74" width="34" height="34" fill="#ffffff" fill-opacity="1" stroke="#94a3b8" stroke-width="1.2"/><rect x="138" y="108" width="34" height="34" fill="#0f6e56" fill-opacity="0.35" stroke="#94a3b8" stroke-width="1.2"/><rect x="138" y="142" width="34" height="34" fill="#ffffff" fill-opacity="1" stroke="#94a3b8" stroke-width="1.2"/><rect x="138" y="176" width="34" height="34" fill="#ffffff" fill-opacity="1" stroke="#94a3b8" stroke-width="1.2"/><rect x="138" y="210" width="34" height="34" fill="#ffffff" fill-opacity="1" stroke="#94a3b8" stroke-width="1.2"/><rect x="172" y="40" width="34" height="34" fill="#ffffff" fill-opacity="1" stroke="#94a3b8" stroke-width="1.2"/><rect x="172" y="74" width="34" height="34" fill="#ffffff" fill-opacity="1" stroke="#94a3b8" stroke-width="1.2"/><rect x="172" y="108" width="34" height="34" fill="#ffffff" fill-opacity="1" stroke="#94a3b8" stroke-width="1.2"/><rect x="172" y="142" width="34" height="34" fill="#0f6e56" fill-opacity="0.35" stroke="#94a3b8" stroke-width="1.2"/><rect x="172" y="176" width="34" height="34" fill="#ffffff" fill-opacity="1" stroke="#94a3b8" stroke-width="1.2"/><rect x="172" y="210" width="34" height="34" fill="#ffffff" fill-opacity="1" stroke="#94a3b8" stroke-width="1.2"/><rect x="206" y="40" width="34" height="34" fill="#ffffff" fill-opacity="1" stroke="#94a3b8" stroke-width="1.2"/><rect x="206" y="74" width="34" height="34" fill="#ffffff" fill-opacity="1" stroke="#94a3b8" stroke-width="1.2"/><rect x="206" y="108" width="34" height="34" fill="#ffffff" fill-opacity="1" stroke="#94a3b8" stroke-width="1.2"/><rect x="206" y="142" width="34" height="34" fill="#ffffff" fill-opacity="1" stroke="#94a3b8" stroke-width="1.2"/><rect x="206" y="176" width="34" height="34" fill="#0f6e56" fill-opacity="0.35" stroke="#94a3b8" stroke-width="1.2"/><rect x="206" y="210" width="34" height="34" fill="#ffffff" fill-opacity="1" stroke="#94a3b8" stroke-width="1.2"/><rect x="240" y="40" width="34" height="34" fill="#ffffff" fill-opacity="1" stroke="#94a3b8" stroke-width="1.2"/><rect x="240" y="74" width="34" height="34" fill="#ffffff" fill-opacity="1" stroke="#94a3b8" stroke-width="1.2"/><rect x="240" y="108" width="34" height="34" fill="#ffffff" fill-opacity="1" stroke="#94a3b8" stroke-width="1.2"/><rect x="240" y="142" width="34" height="34" fill="#ffffff" fill-opacity="1" stroke="#94a3b8" stroke-width="1.2"/><rect x="240" y="176" width="34" height="34" fill="#ffffff" fill-opacity="1" stroke="#94a3b8" stroke-width="1.2"/><rect x="240" y="210" width="34" height="34" fill="#0f6e56" fill-opacity="0.35" stroke="#94a3b8" stroke-width="1.2"/><text x="87.0" y="32" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">1</text><text x="58" y="62.0" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">1</text><text x="121.0" y="32" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">2</text><text x="58" y="96.0" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">2</text><text x="155.0" y="32" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">3</text><text x="58" y="130.0" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">3</text><text x="189.0" y="32" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">4</text><text x="58" y="164.0" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">4</text><text x="223.0" y="32" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">5</text><text x="58" y="198.0" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">5</text><text x="257.0" y="32" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">6</text><text x="58" y="232.0" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">6</text><text x="172" y="16" text-anchor="middle" font-size="12" font-weight="700" fill="#b91c1c" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">dé rouge</text><text x="24" y="146" text-anchor="middle" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">vert</text></svg>
:::

Le nombre de cases du tableau est card(E) = 6 × 6 = 36, et les cases colorées de la diagonale sont l'événement A « même chiffre » : card(A) = 6.

::: exemple Le même chiffre sur les deux dés
1. Les dés se distinguent par leur couleur : E = {(i ; j) | 1 ≤ i ≤ 6 et 1 ≤ j ≤ 6} compte 36 couples, tous équiprobables.
2. L'événement A « même chiffre » compte 6 couples (les cases de la diagonale) : p(A) = 6/36 = **1/6**.
3. « Chiffres distincts » est le contraire de A : 1 − 1/6 = **5/6**. Contrôle : 6 × 5 = 30 couples, et 30/36 = 5/6 ✓.

:::

::: exemple Les fusibles
Une boîte contient 10 fusibles dont 3 sont grillés ; on en prend 3 d'un seul geste, au hasard.
1. Un prélèvement simultané est une partie à 3 éléments, toutes équiprobables : card(E) = C_10^3 = 120.
2. « Aucun fusible grillé » : les 3 sont pris parmi les 7 bons, C_7^3 = 35 prélèvements. Donc p = 35/120 = **7/24**.
3. « Au moins un grillé » est le contraire : 1 − 7/24 = **17/24**.

:::

::: exemple Un code à deux lettres et deux chiffres
Un code comporte deux lettres (26 possibles) suivies de deux chiffres (10 possibles) ; on en tire un au hasard.
1. card(E) = 26 × 26 × 10 × 10 = 67600, par comptage de listes.
2. « Aucun chiffre pair » : chaque chiffre vient de {1, 3, 5, 7, 9}, soit 26 × 26 × 5 × 5 = 16900 codes.
3. p = 16900/67600 = **1/4**. Contrôle : chaque chiffre est impair avec la chance 5/10, et (1/2)² = 1/4 ✓.

:::

::: piege
**Erreur : prendre pour équiprobables des résultats qui ne le sont pas.** Avec deux dés, on peut être tenté de ne retenir que les 21 paires de chiffres {i, j} sans ordre ; mais la paire {3, 4} se réalise de deux façons ((3 ; 4) et (4 ; 3)) alors que {4, 4} d'une seule. La somme 7 a alors 3/21 = 1/7 « chance », au lieu de 6/36 = 1/6. Le bon univers est celui des 36 couples ordonnés, tous équiprobables.
:::

::: propriete
- L'univers doit être choisi de façon que ses éléments soient **équiprobables** ; on compte ensuite card(A) et card(E) avec les outils des deux premières sections (listes pour les tirages successifs, parties pour les tirages simultanés).
- Cas limite : l'équiprobabilité se **justifie** (« dé équilibré », « au hasard »). Sur le dé truqué de la section précédente, card(A)/card(E) donnerait 3/6 = 1/2 pour « pair », alors que la vraie valeur est 5/8.

:::

::: verifie À toi : la somme 9
On lance un dé rouge et un dé vert équilibrés. Quelle est la probabilité que la somme des deux chiffres soit 9 ?

---

L'univers est celui des 36 couples ordonnés, équiprobables. La somme vaut 9 pour (3 ; 6), (4 ; 5), (5 ; 4) et (6 ; 3) : 4 couples, donc p = 4/36 = 1/9. Les couples (4 ; 5) et (5 ; 4) comptent pour deux, comme dans le piège.
:::

::: retenir
En situation d'équiprobabilité, p(A) = card(A)/card(E) : une probabilité devient un dénombrement, à condition de justifier que les issues sont équiprobables.
:::

## 🌳 Probabilité conditionnelle et arbre pondéré

Une urne contient 4 boules rouges numérotées 1, 1, 1, 2 et 2 boules vertes numérotées 2, 2. On tire une boule au hasard. Quelle est la chance qu'elle porte le numéro 2 ?
Et si l'on apprend, sans la voir, qu'elle est rouge, cette chance change-t-elle ?

::: definition
Soit (E, 𝒫(E), p) un espace probabilisé fini et B un événement de probabilité non nulle. La **probabilité de A sachant B**, notée p(A/B) ou p_B(A), est
$$ p(A/B) = p(A ∩ B)/p(B) $$
L'application p_B est la **probabilité B-conditionnelle**. En multipliant par p(B), on obtient
$$ p(A ∩ B) = p(B) × p(A/B) $$
:::

::: exemple La boule rouge qui porte le 2
Notons R « la boule est rouge » et D « la boule porte le numéro 2 ».
1. Les 6 boules sont équiprobables : p(D) = 3/6 = 1/2 (le 2 est sur une rouge et deux vertes) et p(R) = 4/6 = 2/3.
2. p(R ∩ D) = 1/6, car une seule boule est rouge et porte le 2.
3. Sachant R, l'univers se réduit aux 4 boules rouges : p(D/R) = p(R ∩ D)/p(R) = (1/6)/(2/3) = **1/4**. Contrôle : une boule rouge sur quatre porte le 2 ✓.
4. L'information « rouge » a donc fait passer la chance du 2 de 1/2 à 1/4.

:::

::: propriete
L'application p_B est bien une probabilité sur E (p(B) ≠ 0) :
- p_B(E) = p(E ∩ B)/p(B) = p(B)/p(B) = 1 et p_B(∅) = 0 ;
- pour un événement A, p_B(A) = p(A ∩ B)/p(B) = Σ p(aᵢ)/p(B), la somme portant sur les événements élémentaires aᵢ de A ∩ B ;
- p_B(A) est donc la somme de nombres positifs et vaut au plus 1, puisque A ∩ B ⊂ B ; toutes les propriétés d'une probabilité (contraire, réunion) valent pour p_B, par exemple p(A/B) + p(A̅/B) = 1.

:::

Quand les événements se succèdent, un **arbre pondéré** dessine ces formules : les branches issues d'un même nœud portent des probabilités de somme 1, on **multiplie** le long d'un chemin, on **additionne** les chemins qui mènent au même événement.

::: exemple Un dépistage
Dans une population, 10 % des personnes sont malades. Un test est positif pour 98 malades sur 100 et pour 1 non-malade sur 100. Notons M « malade » et T « test positif ».
1. On lit p(M) = 0,1, p(M̅) = 0,9, p(T/M) = 0,98, p(T̅/M) = 0,02, p(T/M̅) = 0,01 et p(T̅/M̅) = 0,99.
2. Chaque chemin est une intersection : p(M ∩ T) = 0,1 × 0,98 = 0,098 ; p(M ∩ T̅) = 0,1 × 0,02 = 0,002 ; p(M̅ ∩ T) = 0,9 × 0,01 = 0,009 ; p(M̅ ∩ T̅) = 0,9 × 0,99 = 0,891.
3. Contrôle : 0,098 + 0,002 + 0,009 + 0,891 = 1 ✓.
4. Le test est positif par deux chemins : p(T) = 0,098 + 0,009 = **0,107**.
5. Un test négatif écarte-t-il la maladie ? p(M/T̅) = p(M ∩ T̅)/p(T̅) = 0,002/(1 − 0,107) = 0,002/0,893 ≈ **0,0022**.

:::

::: figure Sur chaque nœud, les deux branches ont une somme de probabilités égale à 1 ; le produit le long d'un chemin est écrit à droite, et les quatre produits additionnés valent 1
<svg viewBox="0 0 340 250"><title>Arbre pondéré du dépistage : malade ou non, puis test positif ou négatif</title><g fill="none" stroke="#0f172a" stroke-width="2"><path d="M45 125 L150 65"/><path d="M45 125 L150 185"/><path d="M150 65 L250 35"/><path d="M150 65 L250 95"/><path d="M150 185 L250 155"/><path d="M150 185 L250 215"/></g><g fill="#0f172a"><circle cx="45" cy="125" r="4"/><circle cx="150" cy="65" r="4.5"/><circle cx="150" cy="185" r="4.5"/><circle cx="250" cy="35" r="4"/><circle cx="250" cy="95" r="4"/><circle cx="250" cy="155" r="4"/><circle cx="250" cy="215" r="4"/></g><g font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" fill="#0f6e56"><text x="97" y="88" text-anchor="middle">0,1</text><text x="97" y="166" text-anchor="middle">0,9</text><text x="200" y="42" text-anchor="middle">0,98</text><text x="200" y="92" text-anchor="middle">0,02</text><text x="200" y="162" text-anchor="middle">0,01</text><text x="200" y="212" text-anchor="middle">0,99</text></g><g font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" fill="#0f172a"><text x="150" y="53" text-anchor="middle">M</text><text x="150" y="205" text-anchor="middle">M̅</text><text x="261" y="40" text-anchor="middle">T</text><text x="261" y="100" text-anchor="middle">T̅</text><text x="261" y="160" text-anchor="middle">T</text><text x="261" y="220" text-anchor="middle">T̅</text></g><g font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" fill="#b45309"><text x="276" y="40" text-anchor="start">0,098</text><text x="276" y="100" text-anchor="start">0,002</text><text x="276" y="160" text-anchor="start">0,009</text><text x="276" y="220" text-anchor="start">0,891</text></g></svg>
:::

Le nombre 0,098 de la première feuille est le produit 0,1 × 0,98 des deux branches du chemin M puis T, c'est-à-dire p(M ∩ T).

::: piege
**Erreur : confondre p(A/B) et p(B/A).** Ici p(T/M) = 0,98 : presque tous les malades sont positifs. Mais p(M/T) = p(M ∩ T)/p(T) = 0,098/0,107 ≈ 0,92 : sur 100 tests positifs, seuls 92 environ viennent de malades. Les deux nombres répondent à des questions différentes ; l'événement écrit avant la barre oblique est celui qu'on étudie, celui écrit après est l'information donnée.
:::

::: verifie À toi : le sens inverse
Dans l'urne du début de la section, on apprend que la boule porte le numéro 2. Quelle est la probabilité qu'elle soit rouge ?

---

On cherche p(R/D) = p(R ∩ D)/p(D) = (1/6)/(1/2) = 1/3 : parmi les 3 boules numéro 2, une seule est rouge. Ce n'est pas p(D/R) = 1/4 : l'information donnée a changé, donc le dénominateur aussi.
:::

::: retenir
p(A/B) = p(A ∩ B)/p(B) et p(A ∩ B) = p(B) × p(A/B) ; sur un arbre, on multiplie le long des chemins et on additionne les chemins qui mènent au même événement.
:::

## 🔗 Événements indépendants

On lance un dé équilibré. Savoir que le résultat est pair change-t-il la chance qu'il soit multiple de 3 ?
Dans la section précédente, une information changeait la probabilité. Ici on cherche le cas où elle ne la change pas.

::: definition
Deux événements A et B sont **indépendants** lorsque
$$ p(A ∩ B) = p(A) × p(B) $$
Lorsque p(B) ≠ 0, cela revient à p(A/B) = p(A) : la réalisation de B n'influence pas celle de A.
:::

::: exemple Un dé : pair, multiple de 3, multiple de 6
Soit A « pair » = {2, 4, 6}, B « multiple de 3 » = {3, 6} et C « multiple de 6 » = {6}. On a p(A) = 1/2, p(B) = 1/3 et p(C) = 1/6.
1. A ∩ B = {6}, donc p(A ∩ B) = 1/6. Or p(A) × p(B) = (1/2)(1/3) = 1/6 : les deux nombres coïncident, **A et B sont indépendants**.
2. A ∩ C = {6}, donc p(A ∩ C) = 1/6. Or p(A) × p(C) = (1/2)(1/6) = 1/12 ≠ 1/6 : **A et C ne sont pas indépendants**.
3. Contrôle par le conditionnel : p(B/A) = (1/6)/(1/2) = 1/3 = p(B), alors que p(C/A) = (1/6)/(1/2) = 1/3 est le double de p(C) = 1/6.

:::

::: exemple Deux dispositifs de sécurité
Deux dispositifs fonctionnent indépendamment ; le premier tombe en panne avec la probabilité 0,02 et le second avec la probabilité 0,05. Soit P₁ et P₂ les pannes.
1. Les deux pannes : p(P₁ ∩ P₂) = 0,02 × 0,05 = **0,001**, par indépendance.
2. Au moins un fonctionne : le contraire de « les deux sont en panne », soit 1 − 0,001 = **0,999**.
3. Au moins une panne : p(P₁ ∪ P₂) = 0,02 + 0,05 − 0,001 = **0,069**.
4. Seul le premier tombe en panne : p(P₁ ∩ P̅₂) = p(P₁) − p(P₁ ∩ P₂) = 0,02 − 0,001 = **0,019** ; on retire de P₁ le cas où le second est aussi en panne.

:::

::: piege
**Erreur : croire que « incompatibles » veut dire « indépendants ».** Sur un dé, A = {1, 2} et B = {5, 6} sont incompatibles : p(A ∩ B) = 0. Pourtant p(A) × p(B) = (1/3)(1/3) = 1/9 ≠ 0 : ils ne sont pas indépendants, et même au contraire, B réalisé interdit A. Deux événements incompatibles de probabilités non nulles ne sont jamais indépendants.
:::

::: propriete
- Pour tester l'indépendance, on compare **p(A ∩ B)** à **p(A) × p(B)** ; on ne le suppose jamais sans le dire.
- Si A et B sont indépendants, **p(A ∪ B) = p(A) + p(B) − p(A) × p(B)**, car p(A ∩ B) = p(A) × p(B).
- Cas limite : un événement de probabilité 0 ou 1 est indépendant de n'importe quel événement ; p(A ∩ B) et p(A) × p(B) sont alors tous les deux égaux à 0 ou à p(B).

:::

::: verifie À toi : l'union de deux indépendants
Deux événements indépendants A et B vérifient p(A) = 0,3 et p(B) = 0,5. Calculer p(A ∪ B).

---

Par indépendance, p(A ∩ B) = 0,3 × 0,5 = 0,15. Alors p(A ∪ B) = 0,3 + 0,5 − 0,15 = 0,65. L'addition simple 0,3 + 0,5 = 0,8 serait fausse : l'indépendance ne rend pas A et B incompatibles.
:::

::: retenir
A et B sont indépendants lorsque p(A ∩ B) = p(A) × p(B) ; ne pas confondre avec incompatibles, où p(A ∩ B) = 0.
:::

## 🧭 Partition et probabilités totales

Une usine possède trois machines. La machine A fabrique 1/3 de la production, la machine B 1/4 et la machine C le reste. Sur 1000 pièces fabriquées par A, 2 sont défectueuses ; sur 1000 fabriquées par B, 10 ; sur 1000 fabriquées par C, 5.
Quelle est la probabilité qu'une pièce prise au hasard dans la production soit défectueuse ?

::: definition
Des parties B₁, B₂, …, B_n de E forment une **partition** de E lorsqu'elles sont deux à deux disjointes et que leur réunion est E : chaque issue appartient à exactement une des parties.
:::

::: exemple La pièce défectueuse
1. A, B et C forment une partition de la production : toute pièce vient d'une seule machine. La part de C est 1 − 1/3 − 1/4 = 5/12.
2. Les taux de défaut sont p(D/A) = 0,002, p(D/B) = 0,01 et p(D/C) = 0,005.
3. Une pièce défectueuse vient de A, ou de B, ou de C, et ces cas s'excluent : p(D) = p(A) p(D/A) + p(B) p(D/B) + p(C) p(D/C) = (1/3)(0,002) + (1/4)(0,01) + (5/12)(0,005).
4. En douze millièmes : 8/12000 + 30/12000 + 25/12000 = 63/12000 = **0,00525**.
5. Pour une pièce défectueuse, la chance qu'elle vienne de A est p(A ∩ D)/p(D) = (8/12000)/(63/12000) = 8/63 ≈ **0,127**.

:::

::: figure Les parties B₁, B₂, B₃ découpent l'univers E en trois zones sans chevauchement ; l'événement A est découpé à son tour en trois morceaux A ∩ B₁, A ∩ B₂, A ∩ B₃
<svg viewBox="0 0 340 230"><title>Univers E partagé en trois parties B₁, B₂, B₃ ; l'événement A les rencontre toutes les trois</title><rect x="20" y="20" width="300" height="190" fill="none" stroke="#0f172a" stroke-width="2"/><path d="M120 20 L120 210 M195 20 L195 210" stroke="#0f172a" stroke-width="2"/><ellipse cx="170" cy="115" rx="110" ry="40" fill="#0f6e56" fill-opacity="0.18" stroke="#0f6e56" stroke-width="2.4"/><text x="70" y="45" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">B₁</text><text x="157" y="45" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">B₂</text><text x="257" y="45" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">B₃</text><text x="34" y="200" text-anchor="start" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">E</text><text x="92" y="119" text-anchor="middle" font-size="11" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">A∩B₁</text><text x="157" y="119" text-anchor="middle" font-size="11" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">A∩B₂</text><text x="241" y="119" text-anchor="middle" font-size="11" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">A∩B₃</text><text x="300" y="100" text-anchor="middle" font-size="14" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">A</text></svg>
:::

Sur la figure, les trois morceaux de A sont disjoints et leur réunion est A : c'est pourquoi les trois termes de la somme de l'usine ne se recouvrent pas.

::: exemple Trois séries d'un même examen
Un examen compte trois séries : la série 1 pour 40 % des candidats, la série 2 pour 35 %, la série 3 pour 25 %. Les taux de réussite sont 70 %, 60 % et 80 %.
1. Les trois séries forment une partition de l'ensemble des candidats.
2. La probabilité de réussir est p = 0,4 × 0,7 + 0,35 × 0,6 + 0,25 × 0,8 = 0,28 + 0,21 + 0,20 = **0,69**.
3. Contrôle : la réponse est comprise entre le plus petit taux (0,6) et le plus grand (0,8), comme une moyenne pondérée ✓.

:::

::: piege
**Erreur : appliquer la formule à des parties qui ne forment pas une partition.** Sur un dé, B₁ = {1, 2, 3, 4} et B₂ = {3, 4, 5, 6} couvrent E mais se chevauchent en {3, 4}. Pour A = {3}, la somme p(B₁) p(A/B₁) + p(B₂) p(A/B₂) = (2/3)(1/4) + (2/3)(1/4) = 1/3 donne le double de p(A) = 1/6 : le cas 3 est compté deux fois. Il faut des parties disjointes **et** de réunion E.
:::

::: propriete
Soit B₁, …, B_n une partition de E avec p(Bᵢ) ≠ 0 pour tout i. Pour tout événement A,
$$ p(A) = Σ p(A ∩ Bᵢ) = Σ p(Bᵢ) × p(A/Bᵢ) $$
- Raison : les A ∩ Bᵢ sont disjoints et leur réunion est A, donc leurs probabilités s'additionnent ; et p(A ∩ Bᵢ) = p(Bᵢ) × p(A/Bᵢ) par définition du conditionnel.
- Cas limite n = 2 : la partition {B, B̅}, c'est celle de l'arbre, et p(A) = p(B) p(A/B) + p(B̅) p(A/B̅).

:::

::: verifie À toi : trois moyens de transport
Un élève vient au lycée en bus (50 % des jours), en tram (30 %) ou à pied (20 %). Il arrive à l'heure avec les probabilités 0,8 ; 0,9 et 0,95 selon le cas. Quelle est la probabilité qu'il arrive à l'heure un jour pris au hasard ?

---

Bus, tram et à pied forment une partition des jours. p = 0,5 × 0,8 + 0,3 × 0,9 + 0,2 × 0,95 = 0,40 + 0,27 + 0,19 = 0,86. Chaque terme multiplie la part du moyen de transport par sa probabilité conditionnelle, puis on additionne les trois cas.
:::

::: retenir
Si B₁, …, B_n forment une partition de E, alors p(A) = Σ p(Bᵢ) × p(A/Bᵢ) : on additionne les chemins de l'arbre qui mènent à A.
:::

## 🔁 Les suites de probabilités qui se répètent

Une élève s'entraîne à la course. Si elle a couru la veille, elle court encore avec la probabilité 0,6 ; si elle n'a pas couru, elle court avec la probabilité 0,3. Elle court le jour 1.
Quelle est la chance qu'elle coure le jour n, et que devient-elle quand n devient très grand ?

::: definition
Quand l'événement du jour n + 1 dépend seulement de celui du jour n, on pose pₙ = p(Aₙ), α = p(Aₙ₊₁/Aₙ) et β = p(Aₙ₊₁/A̅ₙ). La partition {Aₙ, A̅ₙ} et la formule des probabilités totales donnent
$$ pₙ₊₁ = α pₙ + β (1 − pₙ) = (α − β) pₙ + β $$
La suite (pₙ) vérifie ainsi une relation de la forme **pₙ₊₁ = a pₙ + b**, avec a = α − β et b = β.
:::

::: exemple La course à pied
Soit Cₙ « elle court le jour n » et pₙ = p(Cₙ).
1. On lit α = p(Cₙ₊₁/Cₙ) = 0,6 et β = p(Cₙ₊₁/C̅ₙ) = 0,3.
2. D'après la partition {Cₙ, C̅ₙ} : pₙ₊₁ = 0,6 pₙ + 0,3 (1 − pₙ) = 0,3 pₙ + 0,3. Elle court le jour 1 : p₁ = 1, donc p₂ = 0,6 et p₃ = 0,3 × 0,6 + 0,3 = 0,48.
3. Une limite éventuelle ℓ vérifie ℓ = 0,3ℓ + 0,3, donc ℓ = 3/7. On pose qₙ = pₙ − 3/7.
4. Alors qₙ₊₁ = 0,3 pₙ + 0,3 − 3/7 = 0,3 (pₙ − 3/7) = 0,3 qₙ : la suite (qₙ) est **géométrique** de raison 0,3 et de premier terme q₁ = 1 − 3/7 = 4/7.
5. Donc pₙ = 3/7 + (4/7)(0,3)ⁿ⁻¹. Comme 0 < 0,3 < 1, (0,3)ⁿ⁻¹ tend vers 0 et (pₙ) tend vers **3/7 ≈ 0,43**. Contrôle : n = 2 donne 3/7 + (4/7)(0,3) = 0,6 ✓.

:::

::: figure Les points (n ; pₙ) pour n = 1, …, 6 : l'ordonnée passe de 1 à 0,6 puis à 0,48 et se rapproche de la droite en tirets d'ordonnée 3/7
<svg viewBox="0 0 340 250"><title>Points (n ; pₙ) pour n de 1 à 6, qui se rapprochent de la droite d'ordonnée 3/7</title><path d="M45 200 L320 200 M45 200 L45 20" stroke="#0f172a" stroke-width="1.8" fill="none"/><path d="M45 127.1 L320 127.1" stroke="#b45309" stroke-width="2" stroke-dasharray="6 4" fill="none"/><path d="M60 200 L60 30.0" stroke="#94a3b8" stroke-width="1.5"/><circle cx="60" cy="30.0" r="4.5" fill="#0f6e56"/><text x="60" y="216" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">1</text><path d="M105 200 L105 98.0" stroke="#94a3b8" stroke-width="1.5"/><circle cx="105" cy="98.0" r="4.5" fill="#0f6e56"/><text x="105" y="216" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">2</text><path d="M150 200 L150 118.4" stroke="#94a3b8" stroke-width="1.5"/><circle cx="150" cy="118.4" r="4.5" fill="#0f6e56"/><text x="150" y="216" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">3</text><path d="M195 200 L195 124.5" stroke="#94a3b8" stroke-width="1.5"/><circle cx="195" cy="124.5" r="4.5" fill="#0f6e56"/><text x="195" y="216" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">4</text><path d="M240 200 L240 126.4" stroke="#94a3b8" stroke-width="1.5"/><circle cx="240" cy="126.4" r="4.5" fill="#0f6e56"/><text x="240" y="216" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">5</text><path d="M285 200 L285 126.9" stroke="#94a3b8" stroke-width="1.5"/><circle cx="285" cy="126.9" r="4.5" fill="#0f6e56"/><text x="285" y="216" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">6</text><text x="290" y="119.14285714285715" text-anchor="middle" font-size="13" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">3/7</text><text x="30" y="204" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0</text><text x="30" y="34" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">1</text><text x="180" y="234" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">n</text><text x="84" y="30" text-anchor="start" font-size="11" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">p₁ = 1</text></svg>
:::

La droite en tirets de la figure est la limite ℓ = 3/7 du calcul : les points s'en approchent par le haut parce que q₁ = 4/7 est positif.

::: piege
**Erreur : oublier le cas où elle n'a pas couru la veille.** Écrire pₙ₊₁ = 0,6 pₙ + 0,3 oublie le facteur (1 − pₙ) : le second terme doit valoir 0,3 × (1 − pₙ), la probabilité de ne pas avoir couru la veille. Avec cette erreur, ℓ = 0,3/0,4 = 0,75 au lieu de 3/7 ≈ 0,43, et la suite ne reproduit même pas p₂ = 0,6 quand p₁ = 1.
:::

::: propriete
Si pₙ₊₁ = a pₙ + b avec a ≠ 1 :
- le réel ℓ = b/(1 − a) vérifie ℓ = aℓ + b, et la suite qₙ = pₙ − ℓ est **géométrique** de raison a ;
- donc **pₙ = ℓ + (p₁ − ℓ) aⁿ⁻¹**, et pₙ tend vers ℓ dès que |a| < 1.

Cas limite : si α = β (a = 0), la veille n'influence pas le lendemain : pₙ vaut β dès n = 2, quelle que soit p₁.
:::

::: verifie À toi : un abonné au métro
Un abonné prend le métro le jour 1. S'il l'a pris la veille, il le reprend avec la probabilité 0,8 ; sinon avec la probabilité 0,5. Écrire pₙ₊₁ en fonction de pₙ, puis donner la limite de (pₙ).

---

Ici α = 0,8 et β = 0,5, donc pₙ₊₁ = 0,8 pₙ + 0,5 (1 − pₙ) = 0,3 pₙ + 0,5. La limite ℓ vérifie ℓ = 0,3ℓ + 0,5, donc ℓ = 0,5/0,7 = 5/7 ; comme 0 < 0,3 < 1, la suite géométrique pₙ − 5/7 tend vers 0 et (pₙ) tend vers 5/7.
:::

::: retenir
Pour un phénomène qui se répète, pₙ₊₁ = (α − β) pₙ + β : la suite pₙ − ℓ est géométrique, et (pₙ) converge vers ℓ = β/(1 − α + β) dès que |α − β| < 1.
:::
