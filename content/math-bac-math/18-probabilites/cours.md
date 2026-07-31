# ⚔️ Probabilités — du dénombrement aux lois du hasard

> 💡 «Un joueur demande à Pascal comment partager la mise d'un tournoi interrompu. La question paraît anodine ; la réponse a fondé une science. Depuis, on ne subit plus le hasard : on le calcule.»

Tu sais déjà compter des objets et manipuler des ensembles — réunion, intersection, complémentaire. Ce chapitre transforme ce comptage en **mesure du hasard** : chaque événement reçoit un nombre entre 0 et 1, et ces nombres obéissent à des règles aussi strictes que celles de l'algèbre. Tu y réinvestiras deux outils déjà acquis : les **suites** (chapitre 2) pour les modèles qui se répètent d'un jour à l'autre, et le **calcul intégral** (chapitre 6) pour les deux lois continues de la fin. C'est le dernier chapitre d'analyse du hasard avant les statistiques.

## 🧮 Compter avant de calculer

Avant toute probabilité, il faut savoir **combien** de résultats une expérience peut donner. Trois questions suffisent à choisir le bon outil : y a-t-il **remise** ? l'**ordre** compte-t-il ? prend-on **tous** les éléments ?

> **Définition (dénombrement)** — « Soit E = {a₁, a₂, ..., aₙ} un ensemble à n éléments et p un entier naturel non nul. • Le nombre des p-uplets d'éléments de E est l'entier nᵖ. • Le nombre de n-uplets d'éléments de E deux à deux distincts est l'entier n!. • Si 1 ≤ p ≤ n alors • le nombre des p-uplets d'éléments de E deux à deux distincts est l'entier A_n^p = n!/(n − p)!, • le nombre de parties à p éléments de E est l'entier C_n^p = n!/((n − p)!p!). (L'entier C_n^p est aussi noté (n parmi p) et on convient que C_n^0 = 1). »

| Situation                                | Modèle              | Nombre                    |
| ---------------------------------------- | ------------------- | ------------------------- |
| tirages successifs **avec** remise       | p-uplets            | nᵖ                        |
| tirages successifs **sans** remise       | arrangements        | A_n^p = n!/(n − p)!       |
| tirage **simultané** (l'ordre ne dit rien) | combinaisons        | C_n^p = n!/((n − p)!p!)   |
| on range **tous** les éléments           | permutations        | n!                        |

_Exemple détaillé (avec remise)_ — une urne contient trois boules numérotées 1, 2, 3 ; on effectue 4 tirages avec remise. Le nombre de résultats est 3⁴ = **81**.

_Contrôle par décomposition_ — classons ces 81 tirages selon le nombre k de fois où sort le 3 : il faut choisir les k rangs concernés parmi 4, puis remplir les 4 − k rangs restants avec 1 ou 2. Cela donne C_4^k × 2^(4−k), soit 1 × 16 = 16, 4 × 8 = 32, 6 × 4 = 24, 4 × 2 = 8 et 1 × 1 = 1. Total : 16 + 32 + 24 + 8 + 1 = **81** ✓. Les deux chemins concordent.

_Exemple détaillé (sans remise, ordonné)_ — huit coureurs, un podium (1ᵉʳ, 2ᵉ, 3ᵉ) : A_8^3 = 8!/5! = 8 × 7 × 6 = **336**.

_Exemple détaillé (simultané)_ — choisir 3 coureurs parmi 8 pour une photo, sans ordre : C_8^3 = 8!/(5!3!) = 336/6 = **56**.

> 🗡️ Ces deux résultats ne sont pas indépendants : **A_n^p = p! × C_n^p**. Chaque groupe de 3 coureurs se range de 3! = 6 façons sur un podium, et 56 × 6 = 336 ✓. Choisir, c'est ranger puis oublier l'ordre.

Deux relations complètent la boîte à outils. D'abord la **symétrie** C_n^p = C_n^(n−p) : choisir les p élus revient à choisir les n − p recalés. Ensuite le **compte total des parties** :

$$ C_n^0 + C_n^1 + ... + C_n^n = 2ⁿ $$

_Contrôle_ — pour n = 4 : 1 + 4 + 6 + 4 + 1 = 16 = 2⁴ ✓. Pour n = 5 : 1 + 5 + 10 + 10 + 5 + 1 = 32 = 2⁵ ✓. Un ensemble à n éléments possède donc **2ⁿ parties** : chaque élément est pris ou laissé, indépendamment des autres.

Enfin, une partie à p éléments peut être classée selon ce qu'elle fait de deux éléments fixés a et b : elle les contient tous les deux, ou exactement un des deux, ou aucun. D'où **C_n^p = C_(n−2)^(p−2) + 2C_(n−2)^(p−1) + C_(n−2)^p**.

_Contrôle_ — n = 6 et p = 3 : le membre de gauche vaut C_6^3 = 20 ; celui de droite C_4^1 + 2C_4^2 + C_4^3 = 4 + 12 + 4 = **20** ✓.

> ⚠️ Le piège numéro un du chapitre : **« successivement » ou « simultanément » ?** Tirer deux boules l'une après l'autre sans remise donne A_5^2 = 20 résultats ; les tirer d'un seul geste n'en donne que C_5^2 = 10, exactement deux fois moins. Lis l'énoncé avant de compter, jamais après.

## 🎲 Univers, événements et probabilité

> **Définition (expérience aléatoire, univers)** — « Une expérience aléatoire est une expérience dont le résultat est soumis au hasard et est donc imprévisible. L'ensemble E des issues d'une expérience aléatoire est appelé univers. Les éléments de E sont appelés événements élémentaires. Une partie A de E est appelée événement. »

> **Définition (probabilité)** — « Soit E l'univers d'une expérience aléatoire et 𝒫(E) l'ensemble des événements de E. On appelle probabilité sur E, toute application p, de 𝒫(E) dans [0, 1] vérifiant les conditions ci-dessous. • L'image p(E) de E est égale à 1. • L'image p(∅) de l'ensemble vide est égale à 0. • L'image p(A) d'un événement A, est la somme des images des événements élémentaires de A, c'est-à-dire p(A) = Σ_(aᵢ ∈ A) p(aᵢ). »

Le triplet (E, 𝒫(E), p) est un **espace probabilisé fini**. E est l'événement **certain**, ∅ l'événement **impossible**, A̅ l'événement **contraire** de A ; deux événements sont **incompatibles** lorsque leur intersection est vide.

> **Propriétés** — « Soit (E, 𝒫(E), p) un espace probabilisé et A et B deux événements de E. • p(A̅) = 1 − p(A). • p(A ∪ B) = p(A) + p(B) − p(A ∩ B). • Si A ∩ B = ∅ alors p(A ∪ B) = p(A) + p(B). • Si A₁, A₂, ..., A_k sont des événements deux à deux incompatibles, alors p(A₁ ∪ A₂ ∪ ... ∪ A_k) = p(A₁) + p(A₂) + ... + p(A_k). »

_Exemple détaillé (un dé pipé)_ — un dé a six faces numérotées de 1 à 6, mais il est truqué : la probabilité du 6 est le **triple** de celle de chacune des cinq autres faces. Notons x cette probabilité commune. La somme des probabilités élémentaires vaut 1 :

$$ 5x + 3x = 8x = 1, donc x = 1/8 et p(6) = 3/8 $$

_Contrôle_ — 5 × 1/8 + 3/8 = 5/8 + 3/8 = 8/8 = 1 ✓. La loi est cohérente.

Calculons alors : A « obtenir un nombre pair » = {2, 4, 6} donne p(A) = 1/8 + 1/8 + 3/8 = **5/8** ; B « obtenir un multiple de 3 » = {3, 6} donne p(B) = 1/8 + 3/8 = **1/2** ; et D « pair **ou** multiple de 3 » = {2, 3, 4, 6} donne p(D) = 1/8 + 1/8 + 1/8 + 3/8 = **3/4**.

_Contrôle par la formule de la réunion_ — A ∩ B = {6}, de probabilité 3/8. Donc p(A ∪ B) = 5/8 + 1/2 − 3/8 = 5/8 + 4/8 − 3/8 = 6/8 = **3/4** ✓. Le comptage direct et la formule donnent le même nombre.

_Exemple détaillé (deux défauts)_ — sur 1000 appareils, 60 présentent le défaut D₁, 50 le défaut D₂ et 20 les deux. Alors p(D₁) = 0,06, p(D₂) = 0,05 et p(D₁ ∩ D₂) = 0,02. La probabilité d'avoir **au moins un** défaut vaut 0,06 + 0,05 − 0,02 = **0,09**, donc celle de n'en avoir **aucun** vaut 1 − 0,09 = **0,91**. Et la probabilité d'avoir **exactement un** défaut est 0,09 − 0,02 = **0,07**.

_Contrôle_ — « D₁ seul » a pour probabilité 0,06 − 0,02 = 0,04 et « D₂ seul » 0,05 − 0,02 = 0,03 ; ces deux événements sont incompatibles, donc leur réunion vaut 0,04 + 0,03 = **0,07** ✓.

> ⚠️ p(A ∪ B) = p(A) + p(B) **seulement** si A ∩ B = ∅. Additionner sans retrancher l'intersection compte deux fois les issues communes : ici on aurait trouvé 0,11 au lieu de 0,09.

## 🎯 L'équiprobabilité : compter suffit

> **Définition et théorème (équiprobabilité)** — « Soit E l'univers d'une expérience aléatoire dans une situation d'équiprobabilité et 𝒫(E) l'ensemble des parties de E. L'application p définie de 𝒫(E) dans [0, 1] par p(a) = 1/card(E), pour tout événement élémentaire a de E est une probabilité sur E, appelée probabilité uniforme. »

> **Propriété** — « Si (E, 𝒫(E), p) est un espace probabilisé tel que la probabilité p est uniforme, alors p(A) = card(A)/card(E), pour tout événement A de E. »

Une pièce bien équilibrée, un dé non pipé, un tirage au hasard : toutes les issues ont la même probabilité. Le calcul de probabilité devient alors un pur exercice de **dénombrement** — et la section précédente prend tout son sens.

_Exemple détaillé (deux dés)_ — on jette un dé rouge et un dé vert, faces numérotées de 1 à 6. Les dés étant discernables par leur couleur, l'univers est E = {(i, j) ; 1 ≤ i ≤ 6 et 1 ≤ j ≤ 6}, de cardinal 6 × 6 = **36**. L'événement A « le même chiffre sur les deux dés » = {(i, i)} a pour cardinal 6, donc p(A) = 6/36 = **1/6**, et « deux chiffres distincts » vaut 1 − 1/6 = **5/6**.

_Contrôle_ — comptons directement les couples distincts : 6 × 5 = 30, et 30/36 = 5/6 ✓.

_Exemple détaillé (un code)_ — un code comporte deux lettres (26 possibles) suivies de deux chiffres. Le nombre de codes est 26² × 10² = 676 × 100 = **67600**.

- **commencer par A** : 1 × 26 × 10 × 10 = 2600 codes, soit 2600/67600 = **1/26**. _Contrôle_ : la première lettre est tirée au hasard parmi 26, sa probabilité d'être A vaut évidemment 1/26 ✓.
- **contenir les lettres A et Z** : les deux lettres sont A et Z dans un ordre ou l'autre, soit 2 × 100 = 200 codes, d'où 200/67600 = **1/338**. _Contrôle_ : 67600 ÷ 200 = 338 ✓.
- **ne contenir aucun chiffre pair** : chaque chiffre est pris dans {1, 3, 5, 7, 9}, soit 676 × 25 = 16900 codes, d'où 16900/67600 = **1/4**. _Contrôle_ : les deux chiffres sont indépendants et chacun est impair avec probabilité 5/10, donc (1/2)² = 1/4 ✓.

> ⚠️ L'équiprobabilité n'est **pas** un droit acquis : elle se justifie (« pièce bien équilibrée », « au hasard », « indiscernables au toucher »). Sur le dé pipé de la section précédente, écrire p(A) = card(A)/6 aurait donné 1/2 au lieu de 5/8.

## 🌳 Probabilité conditionnelle et arbre pondéré

Une information nouvelle change une probabilité. Sonne à la porte d'une famille de deux enfants : la probabilité que les deux soient des filles vaut 1/4. Mais si c'est une **fille** qui ouvre, l'univers se réduit aux trois familles comportant au moins une fille, et cette probabilité devient 1/3.

> **Théorème** — « Soit (E, 𝒫(E), p) un espace probabilisé et B un événement tel que p(B) ≠ 0. L'application p_B de 𝒫(E) dans [0, 1], définie par p_B(A) = p(A ∩ B)/p(B), pour tout événement A, est une probabilité sur E. »

> **Définition** — « L'application p_B ainsi définie s'appelle probabilité B-conditionnelle. Le réel p_B(A) est noté p(A/B) (on lit "probabilité de A, sachant B"). »

En multipliant par p(B), on obtient la formule la plus utilisée du chapitre :

$$ p(A ∩ B) = p(B) × p(A/B) $$

C'est exactement ce que dessine un **arbre pondéré** : chaque chemin part de la racine, et la probabilité du chemin est le **produit** des probabilités portées par ses branches. Deux règles de lecture, à vérifier systématiquement :

1. les branches issues d'un **même nœud** portent des probabilités de somme **1** ;
2. la probabilité d'un événement est la **somme** des probabilités des chemins qui y mènent.

_Exemple détaillé (dépistage)_ — dans une population, 10 % des individus sont malades. Sur 100 malades, 98 ont un test positif ; sur 100 non-malades, une seule personne a un test positif. Notons M « la personne est malade » et T « le test est positif ». On lit p(M) = 0,1, p(M̅) = 0,9, p(T/M) = 0,98, p(T̅/M) = 0,02, p(T/M̅) = 0,01 et p(T̅/M̅) = 0,99.

Les quatre chemins donnent : p(M ∩ T) = 0,1 × 0,98 = **0,098** ; p(M ∩ T̅) = 0,1 × 0,02 = **0,002** ; p(M̅ ∩ T) = 0,9 × 0,01 = **0,009** ; p(M̅ ∩ T̅) = 0,9 × 0,99 = **0,891**.

_Contrôle_ — ces quatre événements forment une partition de l'univers, leur somme doit valoir 1 : 0,098 + 0,002 + 0,009 + 0,891 = **1,000** ✓. Et 0,1 × 0,98 se retrouve aussi en écrivant 98/1000 : sur 1000 personnes, 100 sont malades et 98 d'entre elles sont positives ✓.

::: figure Sur chaque nœud, les deux branches portent des probabilités de somme 1 ; on multiplie le long d'un chemin pour obtenir la probabilité écrite à droite, et les quatre résultats additionnés valent exactement 1.
<svg viewBox="0 0 340 250"><g fill="none" stroke="#0f172a" stroke-width="2"><path d="M45 125 L150 65"/><path d="M45 125 L150 185"/><path d="M150 65 L250 35"/><path d="M150 65 L250 95"/><path d="M150 185 L250 155"/><path d="M150 185 L250 215"/></g><g fill="#0f172a"><circle cx="45" cy="125" r="4"/><circle cx="150" cy="65" r="4.5"/><circle cx="150" cy="185" r="4.5"/><circle cx="250" cy="35" r="4"/><circle cx="250" cy="95" r="4"/><circle cx="250" cy="155" r="4"/><circle cx="250" cy="215" r="4"/></g><g font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" fill="#0f6e56"><text x="97" y="88" text-anchor="middle">0,1</text><text x="97" y="166" text-anchor="middle">0,9</text><text x="200" y="42" text-anchor="middle">0,98</text><text x="200" y="92" text-anchor="middle">0,02</text><text x="200" y="162" text-anchor="middle">0,01</text><text x="200" y="212" text-anchor="middle">0,99</text></g><g font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" fill="#0f172a"><text x="150" y="53" text-anchor="middle">M</text><text x="150" y="205" text-anchor="middle">M̅</text><text x="261" y="40" text-anchor="middle">T</text><text x="261" y="100" text-anchor="middle">T̅</text><text x="261" y="160" text-anchor="middle">T</text><text x="261" y="220" text-anchor="middle">T̅</text></g><g font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" fill="#b45309"><text x="276" y="40" text-anchor="start">0,098</text><text x="276" y="100" text-anchor="start">0,002</text><text x="276" y="160" text-anchor="start">0,009</text><text x="276" y="220" text-anchor="start">0,891</text></g></svg>
:::

> ⚠️ p(A/B) et p(B/A) sont **deux nombres différents** : ici p(T/M) = 0,98 mais, on va le voir, p(M/T) ≈ 0,92. Confondre les deux est l'erreur classique — et la plus coûteuse — de tout le chapitre.

## 🔗 Événements indépendants

> **Définition** — « On dit que deux événements A et B sont indépendants lorsque p(A ∩ B) = p(A) × p(B). Dans le cas où p(B) ≠ 0, la réalisation de B n'influence pas celle de A, c'est-à-dire p(A/B) = p(A). »

_Exemple détaillé_ — on jette un dé équilibré. Soit A « obtenir un nombre pair » = {2, 4, 6}, B « obtenir un multiple de 3 » = {3, 6} et C « obtenir un multiple de 6 » = {6}. On a p(A) = 3/6 = 1/2, p(B) = 2/6 = 1/3 et p(C) = 1/6.

- A ∩ B = {6}, donc p(A ∩ B) = 1/6 ; et p(A) × p(B) = (1/2)(1/3) = **1/6**. Les deux nombres coïncident : **A et B sont indépendants** ✓.
- A ∩ C = {6}, donc p(A ∩ C) = 1/6 ; mais p(A) × p(C) = (1/2)(1/6) = **1/12 ≠ 1/6**. **A et C ne sont pas indépendants**.

_Contrôle par le conditionnel_ — p(B/A) = p(A ∩ B)/p(A) = (1/6)/(1/2) = 1/3 = p(B) ✓ : savoir que le résultat est pair ne change rien à la chance d'être multiple de 3. En revanche p(C/A) = (1/6)/(1/2) = 1/3, très loin de p(C) = 1/6 : savoir que le nombre est pair **double** la chance qu'il soit multiple de 6.

_Second exemple_ — l'animateur d'un jeu offre au hasard deux cadeaux à trois candidats A, B et C (un candidat peut en recevoir deux). Il y a 3 × 3 = 9 attributions équiprobables. L'événement « A ne reçoit aucun cadeau » exige que les deux cadeaux aillent à B ou C : 2 × 2 = 4 cas, soit 4/9 ; de même 4/9 pour B. Leur intersection « ni A ni B » signifie que C reçoit tout : 1 cas, soit 1/9. Or (4/9)(4/9) = 16/81, tandis que 1/9 = 9/81 : **les deux événements ne sont pas indépendants**.

> ⚠️ **Indépendant n'est pas incompatible** — c'est même presque le contraire. Si A et B sont incompatibles avec p(A) > 0 et p(B) > 0, alors p(A ∩ B) = 0 alors que p(A)p(B) > 0 : ils ne sont **jamais** indépendants. Incompatible parle des issues, indépendant parle de l'information.

## 🧭 Probabilités totales et retour aux causes

> **Définition (partition)** — « Soit E un ensemble fini, les parties B₁, B₂, ..., Bₙ forment une partition de E lorsqu'ils sont deux à deux disjoints et leur réunion est E. »

> **Théorème (formule des probabilités totales)** — « Soit (E, 𝒫(E), p) un espace probabilisé, B₁, B₂, ..., Bₙ des événements formant une partition de E tels que pour tout i, p(Bᵢ) ≠ 0. Alors pour tout événement A, p(A) = Σ_(i=1)^(n) p(A ∩ Bᵢ) = Σ_(i=1)^(n) p(Bᵢ)·p_Bᵢ(A). »

Autrement dit : on découpe l'univers en scénarios exclusifs, on calcule A dans chacun, puis on additionne en pondérant par le poids du scénario. Sur un arbre, cela revient à **additionner tous les chemins qui aboutissent à A**.

_Exemple détaillé (trois machines)_ — dans une usine, la machine A produit le tiers des ampoules, la machine B le quart, la machine C le reste. Le poids de C vaut 1 − 1/3 − 1/4 = 12/12 − 4/12 − 3/12 = **5/12**. Sur 1000 ampoules, A en livre 2 défectueuses, B en livre 10 et C en livre 5 : p(D/A) = 0,002, p(D/B) = 0,01 et p(D/C) = 0,005.

$$ p(D) = (1/3)(0,002) + (1/4)(0,01) + (5/12)(0,005) $$

Réduisons au dénominateur 12000 : (1/3)(2/1000) = 8/12000, (1/4)(10/1000) = 30/12000 et (5/12)(5/1000) = 25/12000. D'où p(D) = 63/12000 = **0,00525**, et la probabilité que l'ampoule fonctionne vaut 1 − 0,00525 = **0,99475**.

_Contrôle par les effectifs_ — imaginons 12000 ampoules : A en produit 4000 (dont 4000 × 0,002 = 8 défectueuses), B en produit 3000 (dont 30) et C en produit 5000 (dont 25). Total : 8 + 30 + 25 = 63 défectueuses sur 12000, soit 63 ÷ 12000 = **0,00525** ✓. Et 4000 + 3000 + 5000 = 12000 ✓, la partition est bien complète.

Une fois p(A) connue, on peut **remonter la flèche** : on ne demande plus « quelle chance de tomber en panne sachant la machine ? », mais « quelle chance que ce soit la machine A, sachant que l'ampoule est défectueuse ? ». Il suffit de revenir à la définition.

$$ p(A/D) = p(A ∩ D)/p(D) = (8/12000)/(63/12000) = 8/63 ≈ 0,127 $$

_Contrôle_ — sur les 63 ampoules défectueuses de notre population fictive, 8 viennent de A : la fréquence 8/63 ≈ 0,127 est bien celle qu'on vient de calculer ✓. Remarque au passage que A produit le tiers du stock mais seulement 12,7 % des rebuts : c'est la machine la plus fiable.

_Exemple détaillé (retour au dépistage)_ — reprenons l'arbre de la section précédente. T est atteint par deux chemins, donc p(T) = 0,098 + 0,009 = **0,107**. Puis :

$$ p(M/T) = p(M ∩ T)/p(T) = 0,098/0,107 = 98/107 ≈ 0,916 $$

_Contrôle_ — p(T̅) = 0,002 + 0,891 = 0,893 = 1 − 0,107 ✓, et p(M̅/T) = 0,009/0,107 = 9/107 ≈ 0,084, avec 0,916 + 0,084 = 1 ✓.

> 🗡️ Sur un arbre, **on multiplie en descendant, on additionne en travers**. Descendre un chemin = probabilités composées ; rassembler les chemins d'un même événement = probabilités totales ; repartir d'un résultat vers sa cause = un simple quotient.

## 📊 Variable aléatoire : loi, espérance, variance

> **Définition (aléa numérique)** — « Soit (E, 𝒫(E), p) un espace probabilisé. On appelle aléa numérique ou variable aléatoire toute application X : E → ℝ. »

L'événement {a ∈ E ; X(a) = xᵢ} se note (X = xᵢ), et X(E) désigne l'ensemble des valeurs prises par X.

> **Définition (loi de probabilité)** — « Soit (E, 𝒫(E), p) un espace probabilisé et X une variable aléatoire. On appelle loi de probabilité de X ou distribution de X, l'application P_X : X(E) → [0, 1], xᵢ ↦ p(X = xᵢ). »

> **Conséquence** — « Si X est une variable aléatoire sur E telle que X(E) = {x₁, x₂, ..., xₙ}, alors Σ_(i=1)^(n) p(X = xᵢ) = 1. »

> **Définitions (espérance, variance, écart-type)** — « On appelle espérance mathématique ou moyenne de X le nombre E(X) = Σ_(i=1)^(n) xᵢpᵢ. On appelle variance de X le nombre V(X) = E((X − E(X))²). On appelle écart-type de X le nombre σ(X) = √(V(X)). »

Deux outils rendent ces calculs praticables : la **linéarité** E(αX) = αE(X) et E(X + Y) = E(X) + E(Y), et la **formule de Kœnig** :

$$ V(X) = E(X²) − (E(X))² $$

_Exemple détaillé_ — une urne contient deux boules numérotées 4 et trois boules numérotées −2, indiscernables au toucher. On tire **simultanément** deux boules et on note X la somme des deux numéros. L'univers compte C_5^2 = **10** tirages équiprobables.

| Tirage             | Dénombrement           | Valeur de X       | p(X = x) |
| ------------------ | ---------------------- | ----------------- | -------- |
| deux boules « 4 »  | C_2^2 = 1              | 4 + 4 = 8         | 1/10     |
| une de chaque      | 2 × 3 = 6              | 4 + (−2) = 2      | 6/10     |
| deux boules « −2 » | C_3^2 = 3              | (−2) + (−2) = −4  | 3/10     |

_Contrôle de la loi_ — 1/10 + 6/10 + 3/10 = 10/10 = **1** ✓, et le dénombrement se recoupe : 1 + 6 + 3 = 10 = C_5^2 ✓.

$$ E(X) = 8 × 1/10 + 2 × 6/10 + (−4) × 3/10 = 0,8 + 1,2 − 1,2 = 0,8 $$

_Contrôle par linéarité_ — X est la somme des numéros des deux boules tirées. Chaque boule tirée porte en moyenne (2 × 4 + 3 × (−2))/5 = (8 − 6)/5 = 0,4. Par linéarité de l'espérance, E(X) = 2 × 0,4 = **0,8** ✓ — et cet argument reste valable même si les deux tirages ne sont pas indépendants.

Passons à la dispersion. E(X²) = 64 × 1/10 + 4 × 6/10 + 16 × 3/10 = 6,4 + 2,4 + 4,8 = **13,6**, d'où :

$$ V(X) = 13,6 − 0,8² = 13,6 − 0,64 = 12,96 et σ(X) = √12,96 = 3,6 $$

_Contrôle par la définition_ — V(X) = Σ pᵢ(xᵢ − 0,8)² = 0,1 × 7,2² + 0,6 × 1,2² + 0,3 × (−4,8)² = 0,1 × 51,84 + 0,6 × 1,44 + 0,3 × 23,04 = 5,184 + 0,864 + 6,912 = **12,96** ✓. Et 3,6² = 12,96 ✓.

::: figure La hauteur de chaque bâton est la probabilité de la valeur écrite en dessous : additionnées, ces trois hauteurs valent exactement 1, et le point d'équilibre de la figure est l'espérance 0,8.
<svg viewBox="0 0 340 240"><path d="M55 190 H318" fill="none" stroke="#0f172a" stroke-width="2"/><path d="M55 198 V40" fill="none" stroke="#0f172a" stroke-width="2"/><g fill="#0f6e56" opacity="0.25"><path d="M73 190 V148 H107 V190 Z"/><path d="M153 190 V106 H187 V190 Z"/><path d="M233 190 V176 H267 V190 Z"/></g><g fill="none" stroke="#0f6e56" stroke-width="2.2"><path d="M73 190 V148 H107 V190"/><path d="M153 190 V106 H187 V190"/><path d="M233 190 V176 H267 V190"/></g><g font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" fill="#0f172a"><text x="90" y="209" text-anchor="middle">−4</text><text x="170" y="209" text-anchor="middle">2</text><text x="250" y="209" text-anchor="middle">8</text><text x="326" y="196" text-anchor="middle">X</text><text x="46" y="44" text-anchor="middle">p</text></g><g font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" fill="#0f6e56"><text x="90" y="140" text-anchor="middle">0,3</text><text x="170" y="98" text-anchor="middle">0,6</text><text x="250" y="168" text-anchor="middle">0,1</text></g></svg>
:::

> ⚠️ La variance n'est **jamais** négative : si ton calcul donne E(X²) < (E(X))², l'erreur est en amont. Et n'oublie pas d'élever les valeurs au carré, pas les probabilités : E(X²) = Σ xᵢ²pᵢ.

## 📈 La fonction de répartition

> **Définition** — « Soit (E, 𝒫(E), p) un espace probabilisé et X une variable aléatoire sur E. On appelle fonction de répartition de X, l'application définie de ℝ dans [0, 1] par F : x ↦ p(X ≤ x). »

Pour une variable **discrète**, F est une fonction **en escalier** : elle vaut 0 avant la plus petite valeur, 1 à partir de la plus grande, et fait en chaque xᵢ un **saut de hauteur p(X = xᵢ)**. Elle est croissante, et constante entre deux valeurs consécutives.

_Exemple détaillé_ — reprenons la variable X de la section précédente, de valeurs −4 (probabilité 0,3), 2 (probabilité 0,6) et 8 (probabilité 0,1).

| Intervalle    | F(x) = p(X ≤ x) | Calcul            |
| ------------- | --------------- | ----------------- |
| x < −4        | 0               | aucune valeur atteinte |
| −4 ≤ x < 2    | 0,3             | 0,3               |
| 2 ≤ x < 8     | 0,9             | 0,3 + 0,6         |
| x ≥ 8         | 1               | 0,3 + 0,6 + 0,1   |

_Contrôle_ — les trois sauts valent 0,3 − 0 = 0,3 ; 0,9 − 0,3 = 0,6 ; 1 − 0,9 = 0,1 : ce sont exactement les probabilités de la loi ✓. Et p(X > 2) = 1 − F(2) = 1 − 0,9 = 0,1 = p(X = 8) ✓.

> 🗡️ La fonction de répartition contient **toute** la loi : les valeurs prises sont les abscisses des sauts, et chaque probabilité est la hauteur du saut correspondant. Lire un graphique en escalier, c'est reconstruire la loi.

## ⚡ La loi binomiale

Une même épreuve, répétée à l'identique, indépendamment, avec seulement deux issues possibles : c'est le schéma le plus fréquent de tout le programme.

> **Théorème et définition** — « Soit une expérience aléatoire constituée de n épreuves identiques, indépendantes et n'ayant que deux issues : succès ou échec. Soit p la probabilité de l'événement succès. On considère la variable aléatoire X associant à cette expérience le nombre de succès réalisés au cours des n épreuves. Alors la loi de probabilité de X est donnée par p(X = k) = C_n^k pᵏ (1 − p)^(n−k), k ∈ {0, 1, ..., n}. On dit que X suit une loi binomiale de paramètre (n, p). »

On note cette loi **B(n, p)** ; le cas n = 1 s'appelle **loi de Bernoulli**. La formule se lit directement sur l'arbre : C_n^k compte les chemins ayant k succès, pᵏ(1 − p)^(n−k) est la probabilité de chacun d'eux.

> **Espérance et variance** — « Soit X une variable aléatoire suivant à une loi binomiale B(n, p). On a E(X) = np, V(X) = np(1 − p) et σ(X) = √(np(1 − p)). »

_Exemple détaillé (petit n, tout vérifiable)_ — un joueur de fléchettes atteint sa cible avec la probabilité 0,9. Sur **deux** tirs, X suit B(2 ; 0,9) : p(X = 0) = (0,1)² = **0,01**, p(X = 1) = 2 × 0,9 × 0,1 = **0,18**, p(X = 2) = (0,9)² = **0,81**.

_Contrôle de la loi_ — 0,01 + 0,18 + 0,81 = **1,00** ✓.

_Contrôle des formules_ — la formule donne E(X) = 2 × 0,9 = 1,8 ; le calcul direct donne 0 × 0,01 + 1 × 0,18 + 2 × 0,81 = 0,18 + 1,62 = **1,8** ✓. Pour la variance, la formule donne 2 × 0,9 × 0,1 = 0,18 ; le calcul direct donne E(X²) = 0 × 0,01 + 1 × 0,18 + 4 × 0,81 = 3,42, puis V(X) = 3,42 − 1,8² = 3,42 − 3,24 = **0,18** ✓.

_Exemple détaillé (n = 10)_ — sur dix tirs, Y suit B(10 ; 0,9). La probabilité de réaliser exactement neuf succès vaut :

$$ p(Y = 9) = C_10^9 × (0,9)⁹ × (0,1)¹ = 10 × 0,387 420 489 × 0,1 ≈ 0,387 $$

Et E(Y) = 10 × 0,9 = **9** tirs réussis en moyenne, avec σ(Y) = √(10 × 0,9 × 0,1) = √0,9 ≈ **0,95**.

_Exemple détaillé (« au moins un »)_ — on lance n fois un dé équilibré et on note A l'événement « obtenir **au moins un** 6 ». Passer par le contraire évite d'additionner n termes : A̅ signifie n échecs consécutifs, de probabilité (5/6)ⁿ.

$$ p(A) = 1 − (5/6)ⁿ $$

Pour n = 3, cela vaut 1 − 125/216 = **91/216 ≈ 0,421**. Combien de lancers faut-il pour atteindre 0,9 ? Il faut (5/6)ⁿ ≤ 0,1. Or (5/6)¹² ≈ 0,112 donne p(A) ≈ 0,888 < 0,9, tandis que (5/6)¹³ ≈ 0,0935 donne p(A) ≈ **0,906 ≥ 0,9**. Le nombre cherché est donc **n = 13**.

> ⚠️ La loi binomiale exige des épreuves **indépendantes et identiques** — donc, dans une urne, des tirages **avec remise**. Un tirage **sans remise** modifie la composition de l'urne à chaque étape : la probabilité de succès change, et la loi n'est plus binomiale. C'est le contre-exemple que les énoncés adorent glisser.

## 🌊 Deux lois continues : uniforme et exponentielle

Jusqu'ici X ne prenait qu'un nombre fini de valeurs. Quand elle peut prendre **toutes** les valeurs d'un intervalle — un temps d'attente, une durée de vie —, on ne peut plus additionner des probabilités élémentaires : on **intègre une densité**, exactement comme au chapitre 6.

> **Définition (loi uniforme)** — « Soit un intervalle [a, b] (a < b). La fonction f définie sur [a, b] par f(x) = 1/(b − a) est appelée densité de la loi de probabilité uniforme sur [a, b]. […] On dit qu'une variable aléatoire X à valeurs dans [a, b] suit la loi de probabilité uniforme P si P(c ≤ X ≤ d) = (d − c)/(b − a). »

La probabilité d'un intervalle ne dépend donc que de sa **longueur**, pas de sa position. Sa fonction de répartition est une rampe : F(x) = 0 si x < a, (x − a)/(b − a) sur [a, b], et 1 si x > b.

_Exemple détaillé_ — un bus passe toutes les 20 minutes ; le temps d'attente X suit la loi uniforme sur [0, 20].

- attendre entre 2 et 5 minutes : (5 − 2)/20 = 3/20 = **0,15** ;
- attendre entre 10 et 13 minutes : (13 − 10)/20 = 3/20 = **0,15** — même longueur, même probabilité ;
- attendre moins de 3 minutes : (3 − 0)/20 = **0,15** ; attendre plus de 3 minutes : (20 − 3)/20 = 17/20 = **0,85**.

_Contrôle_ — 0,15 + 0,85 = **1** ✓, comme l'exigent deux événements contraires.

> **Définition (loi exponentielle)** — « Soit λ un réel strictement positif. La fonction f définie sur [0, +∞[ par f(t) = λe^(−λt) est appelée densité de loi exponentielle. […] On dit qu'une variable aléatoire X suit la loi exponentielle de paramètre λ, si P(c ≤ X ≤ d) = ∫_c^d λe^(−λx) dx = e^(−λc) − e^(−λd) et P(X ≥ c) = e^(−λc). »

Trois formules suffisent, toutes issues d'une primitive de λe^(−λx), à savoir −e^(−λx) :

$$ P(X ≥ c) = e^(−λc) et P(0 ≤ X ≤ c) = 1 − e^(−λc) et P(c ≤ X ≤ d) = e^(−λc) − e^(−λd) $$

_Exemple détaillé_ — la durée de vie X d'une machine, en années, suit la loi exponentielle de paramètre λ = 0,2.

- P(X ≥ 10) = e^(−0,2 × 10) = e^(−2) ≈ **0,135** ;
- P(X ≤ 10) = 1 − e^(−2) ≈ **0,865**. _Contrôle_ : 0,135 + 0,865 = 1 ✓ ;
- P(5 ≤ X ≤ 8) = e^(−1) − e^(−1,6) ≈ 0,368 − 0,202 = **0,166** ;
- P(X = 10) = **0** : sur une loi continue, chaque valeur isolée est de probabilité nulle.

_Recherche de la médiane_ — cherchons c tel que P(X ≤ c) = P(X ≥ c). Comme les deux membres sont contraires, chacun vaut 0,5, d'où e^(−0,2c) = 0,5, puis −0,2c = ln 0,5 et enfin c = (ln 2)/0,2 ≈ **3,47 ans**.

_Contrôle_ — e^(−0,2 × 3,466) = e^(−0,693) ≈ 0,500 ✓ : une machine sur deux tombe en panne avant 3,47 ans, alors que sa durée de vie peut en principe être aussi longue qu'on veut.

> ⚠️ Sur une loi continue, P(X = c) = 0 ne signifie **pas** que l'événement est impossible : le bus finit bien par arriver à un instant précis. Conséquence pratique : les inégalités strictes et larges donnent la même probabilité, P(X < c) = P(X ≤ c). Pour ces deux lois, on ne calcule que des probabilités d'intervalles.

> 🏆 Dix-huitième porte franchie, héros : tu sais compter les possibles, pondérer les scénarios, remonter d'un effet à sa cause, résumer une expérience en une seule variable et lui attacher une moyenne, une dispersion et une loi — discrète ou continue. Au chapitre suivant, on quitte le hasard pour les données réelles : les **statistiques** décrivent ce que les probabilités avaient prévu.
