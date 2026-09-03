# ⚔️ Barycentre — quand les points reçoivent un poids

> 💡 «Deux points, deux nombres, et un seul point d'équilibre. Tout ce que la géométrie appelle "milieu", "centre de gravité" ou "point de concours" n'est qu'un réglage de poids.»

Au chapitre précédent, les points étaient tous égaux devant le calcul vectoriel. Ici, on leur accroche des **coefficients** — des poids — et on cherche le point qui les équilibre. Cette idée minuscule range d'un coup une longue liste de résultats : le milieu, le centre de gravité, le partage d'un segment dans un rapport donné, l'alignement de trois points construits, le concours de trois droites. Et elle donne une méthode unique là où il fallait auparavant une astuce par figure.

## ⚖️ D'où vient l'idée : la moyenne pondérée et le point d'équilibre

Tu connais déjà la **moyenne pondérée**. Un élève obtient 15 au devoir de contrôle (coefficient 2) et 9 au devoir de synthèse (coefficient 3) : sa moyenne n'est pas 12, mais

$$ (2 × 15 + 3 × 9) / (2 + 3) = (30 + 27) / 5 = 11,4 $$

La note la plus lourde tire la moyenne vers elle. Place maintenant ces notes sur une droite graduée : le résultat n'est plus un nombre isolé, c'est un **point**, situé entre les deux autres et plus près du plus lourd. C'est exactement l'idée du barycentre.

::: figure Sur une droite graduée, A a pour abscisse 1 (coefficient 4) et B pour abscisse 11 (coefficient 1). Le point d'équilibre G a pour abscisse (4 × 1 + 1 × 11)/5 = 3 : il se tient tout près de A, quatre fois plus lourd que B
<svg viewBox="0 0 340 140">
<path d="M18 80 L316 80" fill="none" stroke="#0f172a" stroke-width="2"/>
<polygon points="323,80 311,85 311,75" fill="#0f172a"/>
<path d="M28 75 L28 85 M51 75 L51 85 M74 75 L74 85 M97 75 L97 85 M120 75 L120 85 M143 75 L143 85 M166 75 L166 85 M189 75 L189 85 M212 75 L212 85 M235 75 L235 85 M258 75 L258 85 M281 75 L281 85 M304 75 L304 85" fill="none" stroke="#0f172a" stroke-width="1.5"/>
<g fill="#0f172a"><circle cx="51" cy="80" r="5"/><circle cx="281" cy="80" r="5"/></g>
<circle cx="97" cy="80" r="6" fill="#0f6e56"/>
<g font-size="12" fill="#0f172a" text-anchor="middle">
<text x="28" y="102">0</text><text x="74" y="102">2</text><text x="120" y="102">4</text><text x="166" y="102">6</text><text x="212" y="102">8</text><text x="258" y="102">10</text><text x="304" y="102">12</text>
</g>
<g font-size="15" font-weight="700" text-anchor="middle" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">
<text x="51" y="58" fill="#0f172a">A</text>
<text x="281" y="58" fill="#0f172a">B</text>
<text x="97" y="58" fill="#0f6e56">G</text>
<text x="51" y="128" fill="#94a3b8">4</text>
<text x="281" y="128" fill="#94a3b8">1</text>
</g>
</svg>
:::

> 🗡️ La même idée est physique : suspends une tige rigide portant deux masses en A et en B ; elle s'équilibre en un point G unique, d'autant plus proche de A que la masse accrochée en A est grande. C'est la loi du levier, étudiée par **Archimède** (Syracuse, IIIᵉ siècle avant J.-C.), et c'est cet équilibre que le mot « barycentre » désigne.

## 🎯 Le barycentre de deux points pondérés

Le couple formé d'un point et d'un réel s'appelle un **point pondéré** ; le réel est le **coefficient** du point.

> **Définition (barycentre de deux points).** Soient A et B deux points du plan et α, β deux réels tels que **α + β ≠ 0**. Il existe un point G et un seul vérifiant
>
> $$ αGA⃗ + βGB⃗ = 0⃗ $$
>
> Ce point est appelé le **barycentre des points pondérés (A, α) et (B, β)**. On dit aussi que G est le barycentre des points A et B **affectés des coefficients** α et β.

Deux choses sont à retenir dans cette définition, et elles se perdent facilement.

- Chaque vecteur **part de G** et va vers son point : GA⃗ pour A, GB⃗ pour B.
- Chaque vecteur est multiplié par le coefficient **de son propre point** : α va avec A, β avec B.

> ⚠️ La condition **α + β ≠ 0** n'est pas décorative : c'est elle qui rend le point unique, et c'est par cette somme qu'il faudra diviser pour le placer. Si α + β = 0, il n'existe **aucun** barycentre — nous verrons plus bas ce qui se passe alors.

Pour construire G, on ne garde jamais la relation sous cette forme : on la ramène à une origine. En écrivant GA⃗ = −AG⃗ et GB⃗ = AB⃗ − AG⃗, la définition devient −αAG⃗ + β(AB⃗ − AG⃗) = 0⃗, soit −(α + β)AG⃗ + βAB⃗ = 0⃗.

> **Retenir (les deux écritures de position).** Si G est le barycentre des points pondérés (A, α) et (B, β), alors
>
> $$ AG⃗ = (β/(α+β)) AB⃗ et BG⃗ = (α/(α+β)) BA⃗ $$
>
> En particulier **G appartient toujours à la droite (AB)**, puisque AG⃗ est un multiple de AB⃗.

Le numérateur est le coefficient du point d'**arrivée** du vecteur — c'est l'erreur la plus fréquente du chapitre que de mettre celui du point de départ.

_Exemple détaillé_ : G est le barycentre des points pondérés (A, 3) et (B, 7). La somme des coefficients vaut 10, donc AG⃗ = (7/10)AB⃗ : le point G est aux sept dixièmes du chemin de A vers B, donc nettement plus près de B — le point le plus lourd attire, exactement comme la note de plus fort coefficient tire la moyenne.

## 🧭 Où se trouve G ? Le signe des coefficients décide

Le facteur β/(α + β) dit tout. S'il est compris entre 0 et 1, le point reste entre A et B ; s'il est négatif, on part de A dans l'autre sens ; s'il dépasse 1, on franchit B.

> **Retenir (position sur la droite).** Le point G est dans le **segment [AB]** exactement lorsque α et β sont de **même signe** (tous deux positifs ou tous deux négatifs). Si les deux coefficients sont de signes contraires, G est sur la droite (AB) mais **à l'extérieur** du segment, du côté du point qui porte le coefficient de plus grande valeur absolue.

::: figure Sur la droite (AB) : le barycentre de (A, 3) et (B, 1) vérifie AG⃗ = (1/4)AB⃗ et reste dans le segment ; celui de (A, 4) et (B, −1) vérifie AG⃗ = −(1/3)AB⃗ et sort derrière A ; celui de (A, 1) et (B, −4) vérifie AG⃗ = (4/3)AB⃗ et sort au-delà de B
<svg viewBox="0 0 340 150">
<path d="M35 90 L312 90" fill="none" stroke="#0f172a" stroke-width="2"/>
<g fill="#0f172a"><circle cx="110" cy="90" r="5"/><circle cx="230" cy="90" r="5"/></g>
<g fill="#0f6e56"><circle cx="140" cy="90" r="5"/></g>
<g fill="#b91c1c"><circle cx="70" cy="90" r="5"/><circle cx="270" cy="90" r="5"/></g>
<g font-size="15" font-weight="700" text-anchor="middle" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">
<text x="110" y="76" fill="#0f172a">A</text>
<text x="230" y="76" fill="#0f172a">B</text>
<text x="142" y="118" fill="#0f6e56">G₁</text>
<text x="70" y="118" fill="#b91c1c">G₂</text>
<text x="270" y="118" fill="#b91c1c">G₃</text>
</g>
<g font-size="11" fill="#94a3b8" text-anchor="middle">
<text x="142" y="138">(3 ; 1)</text><text x="70" y="138">(4 ; −1)</text><text x="270" y="138">(1 ; −4)</text>
</g>
</svg>
:::

_Exemple détaillé_ : cherchons le barycentre des points pondérés (A, 1) et (B, −4). La somme vaut 1 + (−4) = −3, non nulle, donc le point existe, et AG⃗ = (−4/−3)AB⃗ = (4/3)AB⃗. Le facteur 4/3, positif et supérieur à 1, fait partir de A vers B puis franchir B d'un tiers de la longueur AB. C'est bien ce qu'annonce la règle des signes, puisque 1 et −4 sont de signes contraires.

## 🔁 Homogénéité, et le cas du milieu

> **Retenir (homogénéité).** Pour tout réel **k non nul**, le barycentre des points pondérés (A, kα) et (B, kβ) est le **même** que celui de (A, α) et (B, β). Un même nombre non nul appliqué à tous les coefficients à la fois ne déplace pas le point.

La raison tient en une ligne : le facteur de position ne change pas, car kβ/(kα + kβ) = β/(α + β) après simplification par k. Rien n'oblige k à être positif : les coefficients −6 et −4 donnent le même point que 3 et 2.

_Exemple détaillé_ : les points pondérés (A, 4) et (B, 6) ont pour barycentre celui de (A, 2) et (B, 3), obtenu en divisant par 2. On aime réduire ainsi les coefficients avant de calculer : AG⃗ = (3/5)AB⃗ se lit plus vite que (6/10)AB⃗.

> **Retenir (le milieu).** Le barycentre des points pondérés (A, 1) et (B, 1) est le **milieu de [AB]**, et par homogénéité celui de (A, k) et (B, k) l'est aussi, pour tout k non nul. Réciproquement, deux coefficients égaux désignent toujours ce milieu.

> ⚠️ Ne confonds pas « coefficients **égaux** » et « coefficients **opposés** ». Les premiers donnent le milieu ; les seconds ne donnent rien du tout, puisque leur somme est nulle.

## 🚫 Quand la somme des coefficients est nulle

C'est le piège classique du chapitre, et il se reconnaît en une addition.

> **Retenir.** Si α + β = 0, les points pondérés (A, α) et (B, β) n'admettent **aucun barycentre**. Mieux : pour tout point M du plan, la somme αMA⃗ + βMB⃗ est alors un **vecteur constant**, qui ne dépend pas de M. Le même phénomène vaut pour trois points dès que α + β + γ = 0.

Le calcul est court. Avec β = −α, on a αMA⃗ − αMB⃗ = α(MA⃗ − MB⃗) = αBA⃗ : le point M a disparu.

_Exemple détaillé (trois points)_ : réduisons MA⃗ + 4MB⃗ − 5MC⃗, dont les coefficients ont pour somme 1 + 4 − 5 = 0. On ramène tout au point C : MA⃗ = MC⃗ + CA⃗ et MB⃗ = MC⃗ + CB⃗, donc

$$ MA⃗ + 4MB⃗ − 5MC⃗ = (1 + 4 − 5)MC⃗ + CA⃗ + 4CB⃗ = CA⃗ + 4CB⃗ $$

Le résultat ne contient plus M : c'est un vecteur **fixe**, entièrement déterminé par le triangle. Une condition portant sur sa norme n'a donc que deux issues possibles : ou bien elle est remplie par **tous** les points du plan, ou bien elle ne l'est par **aucun** — jamais par un cercle.

## 🧮 La fonction vectorielle de Leibniz

Voici l'outil qui fait tout le travail dans les exercices. Il transforme une somme portant sur plusieurs points en **un seul** vecteur.

> **Retenir (fonction vectorielle de Leibniz).** Si G est le barycentre des points pondérés (A, α) et (B, β), alors pour **tout** point M du plan
>
> $$ αMA⃗ + βMB⃗ = (α + β) MG⃗ $$

La démonstration insère G dans chaque terme : α(MG⃗ + GA⃗) + β(MG⃗ + GB⃗) redonne (α + β)MG⃗ augmenté du bloc αGA⃗ + βGB⃗, lequel s'évanouit — c'est très exactement ce qui définit G.

_Exemple détaillé_ : G est le barycentre des points pondérés (A, 3) et (B, 2). Alors 3MA⃗ + 2MB⃗ = 5MG⃗ pour tout point M. En particulier, avec M = A : 2AB⃗ = 5AG⃗, ce qui redonne AG⃗ = (2/5)AB⃗.

> 🗡️ Le facteur qui sort est la **somme** des coefficients, jamais leur nombre ni la somme de leurs valeurs absolues. Avec les coefficients 5 et −2, le facteur est 3, pas 7.

**Première application : les ensembles de points (lignes de niveau).** Une condition portant sur la norme d'une somme pondérée se ramène à une condition sur une seule distance.

_Exemple détaillé_ : soit G le barycentre des points pondérés (A, 3) et (B, 2) ; cherchons l'ensemble des points M tels que ‖3MA⃗ + 2MB⃗‖ = 20. La réduction donne ‖5MG⃗‖ = 20, et comme ‖5MG⃗‖ = 5 × MG, la condition s'écrit 5 × MG = 20, soit MG = 4. L'ensemble des points M est donc le **cercle centré en G, de rayon 4**.

## 🔺 Trois points pondérés, isobarycentre et centre de gravité

Tout se transpose mot pour mot.

> **Définition (barycentre de trois points).** Soient A, B, C trois points et α, β, γ trois réels tels que **α + β + γ ≠ 0**. Il existe un unique point G vérifiant
>
> $$ αGA⃗ + βGB⃗ + γGC⃗ = 0⃗ $$
>
> C'est le **barycentre des points pondérés (A, α), (B, β) et (C, γ)**. Lorsque α = β = γ, le point G s'appelle l'**isobarycentre** de A, B et C.

> **Retenir (Leibniz à trois points).** Avec S = α + β + γ non nul, pour tout point M du plan
>
> $$ αMA⃗ + βMB⃗ + γMC⃗ = S × MG⃗ $$
>
> Appliquée en M = A, cette égalité donne directement la position de G dans le triangle :
>
> $$ AG⃗ = (β/S) AB⃗ + (γ/S) AC⃗ $$

_Exemple détaillé_ : G est le barycentre des points pondérés (A, 4), (B, 1) et (C, 3). La somme vaut S = 8, donc AG⃗ = (1/8)AB⃗ + (3/8)AC⃗. Chacun des deux vecteurs est pesé par le coefficient du sommet vers lequel il pointe, le tout rapporté au total 8 ; le coefficient de A, lui, ne figure nulle part, puisque AA⃗ est nul.

> **Retenir (isobarycentre et centre de gravité).** L'isobarycentre de trois points **non alignés** A, B et C est le **centre de gravité** du triangle ABC, c'est-à-dire le point de concours de ses médianes. Il vérifie GA⃗ + GB⃗ + GC⃗ = 0⃗, et pour tout point M : MA⃗ + MB⃗ + MC⃗ = 3MG⃗.

L'homogénéité vaut aussi pour trois points : multiplier α, β et γ par un même réel non nul ne déplace pas G.

## 🧩 Le barycentre partiel : regrouper deux points

C'est le théorème le plus rentable du chapitre. Il autorise à traiter trois points comme deux : un couple de points pondérés cède la place à son seul barycentre.

> **Théorème (barycentre partiel).** Si G est le barycentre des points pondérés (A, α), (B, β) et (C, γ) et si **β + γ ≠ 0**, alors G est aussi le barycentre de (A, α) et (G', β + γ), où G' est le barycentre de (B, β) et (C, γ).

Le point de remplacement **récupère la somme** des deux coefficients effacés : c'est le détail que l'on oublie une fois sur deux. Et la condition β + γ ≠ 0 est indispensable, faute de quoi le point G' n'existe pas.

::: figure Regroupement dans le triangle ABC : J est le barycentre de (B, 3) et (C, 5), donc BJ⃗ = (5/8)BC⃗ ; le point J hérite du coefficient 8, et le barycentre G de (A, 2), (B, 3), (C, 5) est celui de (A, 2) et (J, 8), donc AG⃗ = (8/10)AJ⃗ = (4/5)AJ⃗
<svg viewBox="0 0 320 230">
<polygon points="150,25 50,195 270,185" fill="#0f6e56" opacity="0.10"/>
<polygon points="150,25 50,195 270,185" fill="none" stroke="#0f172a" stroke-width="2.2"/>
<path d="M150 25 L188 189" fill="none" stroke="#0f6e56" stroke-width="2.4"/>
<g fill="#0f172a"><circle cx="150" cy="25" r="4"/><circle cx="50" cy="195" r="4"/><circle cx="270" cy="185" r="4"/></g>
<g fill="#0f6e56"><circle cx="188" cy="189" r="5"/><circle cx="180" cy="156" r="5"/></g>
<g font-size="15" font-weight="700" text-anchor="middle" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">
<text x="150" y="16" fill="#0f172a">A</text>
<text x="36" y="212" fill="#0f172a">B</text>
<text x="284" y="198" fill="#0f172a">C</text>
<text x="194" y="212" fill="#0f6e56">J</text>
<text x="162" y="152" fill="#0f6e56">G</text>
</g>
</svg>
:::

_Exemple détaillé_ : G est le barycentre des points pondérés (A, 2), (B, 3) et (C, 5). Comme 3 + 5 = 8 n'est pas nul, on regroupe B et C en leur barycentre J, affecté du coefficient 8. Alors G est le barycentre de (A, 2) et (J, 8), d'où AG⃗ = (8/10)AJ⃗ = (4/5)AJ⃗. On a remplacé un problème à trois points par un problème à deux, et la construction devient immédiate.

> 🗡️ On peut regrouper **n'importe quelle** paire de points, à condition que la somme de leurs coefficients ne soit pas nulle. Choisir la bonne paire, c'est tout l'art des exercices d'alignement et de concours.

## 🏹 Trois usages du regroupement

**Alignement.** Si G est le barycentre de (A, α), (B, β), (C, γ) et si β + γ ≠ 0, alors G est sur la droite joignant A au barycentre G' de (B, β) et (C, γ) : les points A, G et G' sont **alignés**, et le regroupement le prouve sans aucun calcul de coordonnées. Le facteur de position (β + γ)/(α + β + γ) dit ensuite si G tombe entre A et G' — c'est le cas dès que les deux coefficients α et β + γ sont de même signe.

**Concours de droites.** Le même point G se regroupe de trois façons différentes. En regroupant B et C on le trouve sur une droite issue de A ; en regroupant A et C, sur une droite issue de B ; en regroupant A et B, sur une droite issue de C. Ces trois droites passent donc toutes par G : elles sont **concourantes**. Avec les coefficients 1, 1, 1, on retrouve le concours des médianes ; avec d'autres coefficients, on démontre de la même façon le concours de trois droites joignant chacune un sommet à un point du côté opposé.

**Ensembles de points.** Une condition sur ‖αMA⃗ + βMB⃗ + γMC⃗‖ se réduit à une condition sur MG dès que S = α + β + γ n'est pas nul : les points cherchés forment un **cercle centré en G**, dont le rayon s'obtient en divisant par |S|. Si S = 0, la somme est constante : ou bien tous les points conviennent, ou bien aucun.

## 📐 Construire le barycentre à la règle

Construire G revient toujours à réaliser l'égalité AG⃗ = (β/(α + β))AB⃗, c'est-à-dire à partager [AB] en α + β parts égales et à en compter β depuis A. Le manuel propose pour cela la **méthode des parallèles**, le partage classique par le théorème de Thalès, illustré ci-dessous.

::: figure Partage de [AB] en 5 parts égales pour construire le barycentre de (A, 3) et (B, 2) : on trace une demi-droite d'origine A, on y reporte 5 longueurs égales, on joint le cinquième point à B, puis on mène les parallèles à cette droite ; le point G cherché est le deuxième point de partage à partir de A, puisque AG⃗ = (2/5)AB⃗
<svg viewBox="0 0 340 200">
<path d="M40 150 L290 150" fill="none" stroke="#0f172a" stroke-width="2.4"/>
<path d="M40 150 L215 40" fill="none" stroke="#94a3b8" stroke-width="1.8"/>
<path d="M75 128 L90 150 M110 106 L140 150 M145 84 L190 150 M180 62 L240 150" fill="none" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="5 4"/>
<g fill="#94a3b8"><circle cx="90" cy="150" r="3"/><circle cx="190" cy="150" r="3"/><circle cx="240" cy="150" r="3"/></g>
<path d="M215 40 L290 150" fill="none" stroke="#0f172a" stroke-width="1.6"/>
<g fill="#94a3b8"><circle cx="75" cy="128" r="3.5"/><circle cx="110" cy="106" r="3.5"/><circle cx="145" cy="84" r="3.5"/><circle cx="180" cy="62" r="3.5"/><circle cx="215" cy="40" r="3.5"/></g>
<g fill="#0f172a"><circle cx="40" cy="150" r="5"/><circle cx="290" cy="150" r="5"/></g>
<circle cx="140" cy="150" r="6" fill="#0f6e56"/>
<g font-size="15" font-weight="700" text-anchor="middle" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">
<text x="34" y="172" fill="#0f172a">A</text>
<text x="296" y="172" fill="#0f172a">B</text>
<text x="140" y="176" fill="#0f6e56">G</text>
</g>
</svg>
:::

## 👑 Aller plus loin : deux résultats qui tombent tout seuls

**Le triangle des milieux.** Soient I, J et K les milieux respectifs de [BC], [CA] et [AB]. Pour tout point M du plan, les définitions des milieux donnent MI⃗ = (1/2)(MB⃗ + MC⃗), MJ⃗ = (1/2)(MC⃗ + MA⃗) et MK⃗ = (1/2)(MA⃗ + MB⃗). En additionnant, chacun des vecteurs MA⃗, MB⃗, MC⃗ apparaît deux fois avec le facteur 1/2 :

$$ MI⃗ + MJ⃗ + MK⃗ = MA⃗ + MB⃗ + MC⃗, quel que soit le point M $$

Une égalité valable pour tout M est une machine à conclusions : il suffit de choisir le bon M. Essaie avec le centre de gravité de ABC, et regarde ce que devient le membre de gauche.

**Le centre du cercle inscrit.** Notons a = BC, b = CA et c = AB les longueurs des côtés du triangle ABC. La bissectrice issue de A coupe [BC] en un point M qui vérifie MB/MC = c/b : ce point est donc le barycentre des points pondérés (B, b) et (C, c), affecté du coefficient b + c après regroupement. En reprenant le même raisonnement sur une deuxième bissectrice, on obtient le résultat annoncé.

> **Retenir (enrichissement).** Le centre du cercle inscrit dans le triangle ABC est le barycentre des points pondérés **(A, a), (B, b) et (C, c)**, où a, b et c sont les longueurs des côtés **opposés** aux sommets A, B et C. Les trois coefficients étant strictement positifs, ce point est bien intérieur au triangle.

> 🏆 Quête franchie, héros : tu sais poser un barycentre, le placer sur une droite, décider s'il tombe dans un segment, réduire n'importe quelle somme pondérée en un seul vecteur, regrouper des points pour prouver un alignement ou un concours, et reconnaître le piège de la somme nulle. Au chapitre suivant, ces points pondérés se mettront à bouger : les transformations du plan conservent précisément le barycentre.
