# ⚔️ Séries statistiques à deux caractères — du nuage à la droite de prévision

> 💡 «Une seule mesure décrit une série ; deux mesures prises sur les mêmes individus racontent comment elles varient ensemble.»

Bienvenue, héros de la section Sciences de l'informatique. Le 1ᵉʳ janvier 1801, l'astronome Piazzi repère un astre inconnu, puis le perd de vue. À partir de ses quelques observations, Gauss calcule par la méthode des moindres carrés où le retrouver : l'astre réapparaît à la place prévue. Huit étapes te mènent de cette méthode : les rappels sur une variable (moyenne, écart-type, puis médiane et quartiles), le nuage de points et la droite de Mayer, la covariance, le coefficient de corrélation linéaire, la droite des moindres carrés, la seconde droite de régression et les ajustements non affines. Tu réutilises les fonctions affines, ln et exp ; chaque calcul se fait à la main, puis le tableur ou la calculatrice servent de contrôle.

## 📊 Moyenne, variance et écart-type : résumer une série

Un devoir d'informatique est noté sur 40. Voici les notes des 20 élèves de la classe.

| Note X      | 16  | 20  | 24  | 28  | 32  | 36  | Total |
| ----------- | --- | --- | --- | --- | --- | --- | ----- |
| Effectif nᵢ | 1   | 2   | 7   | 7   | 2   | 1   | 20    |

Comment résumer la classe par un nombre « du milieu » et par un nombre qui dit si les notes sont serrées ou éparpillées ? Et que deviennent ces deux nombres si le professeur ramène les notes sur 20 et ajoute un point de bonus ?

::: definition
Pour une série statistique (xᵢ, nᵢ) d'effectif total N = Σ nᵢ, on appelle :

- **moyenne** le réel X̄ = Σ nᵢxᵢ / N ;
- **variance** le réel V(X) = Σ nᵢ(xᵢ − X̄)² / N, qui mesure l'écart quadratique moyen autour de X̄ ;
- **écart-type** le réel σ(X) = √V(X).

:::

::: exemple Moyenne et écart-type du devoir

1. X̄ = (1 × 16 + 2 × 20 + 7 × 24 + 7 × 28 + 2 × 32 + 1 × 36) / 20 = 520 / 20 = 26 : chaque note compte autant de fois que son effectif.
2. La moyenne des carrés vaut (256 + 800 + 4032 + 5488 + 2048 + 1296) / 20 = 13920 / 20 = 696.
3. V(X) = 696 − 26² = 696 − 676 = 20 : on retranche le carré de la moyenne, ce qui évite de calculer six écarts.
4. σ(X) = √20 ≈ 4,47 points.
5. Contrôle : l'intervalle [X̄ − σ ; X̄ + σ] ≈ [21,5 ; 30,5] contient les notes 24 et 28, soit 14 élèves sur 20, donc 70 % de la classe ✓.

:::

::: exemple Changer le barème
Le professeur ramène les notes sur 20 et ajoute 1 point : Y = 0,5X + 1.

1. Ȳ = 0,5 × 26 + 1 = 14 : la moyenne subit la même transformation que les notes.
2. Chaque écart à la moyenne est multiplié par 0,5, car le « +1 » décale toute la série sans changer les écarts : yᵢ − Ȳ = 0,5(xᵢ − X̄). Donc V(Y) = 0,5² × 20 = 5.
3. σ(Y) = √5 ≈ 2,24 = 0,5 × σ(X) : l'écart-type est multiplié par 0,5 et le bonus n'y joue aucun rôle.

:::

::: piege
**Erreur : appliquer le changement affine à l'écart-type comme à la moyenne.** On écrit σ(Y) = 0,5 × 4,47 + 1 ≈ 3,24, parce que la moyenne a bien subi « × 0,5 puis + 1 ». Mais le +1 translate toute la série et ne change aucune distance entre les notes : la bonne valeur est σ(Y) = 0,5 × 4,47 ≈ 2,24.
:::

::: propriete
Pour une série (xᵢ, nᵢ) d'effectif total N :
$$ X̄ = Σ nᵢxᵢ / N $$
$$ V(X) = Σ nᵢxᵢ² / N − X̄² $$
$$ σ(X) = √V(X) $$
Si Y = aX + b, alors Ȳ = aX̄ + b, V(Y) = a²V(X) et σ(Y) = |a| σ(X).
Cas limites : si a < 0, l'écart-type reste positif (σ(−3X + 4) = 3σ(X)) ; si a = 0, la série est constante et σ(Y) = 0.
:::

::: verifie À toi : la note sur 10
Le professeur ramène aussi les notes sur 10 : Z = X / 4. Calcule Z̄ et σ(Z) pour ce devoir.

---

Z̄ = 26 / 4 = 6,5, car la moyenne suit la même transformation. Ici a = 1/4, donc V(Z) = (1/4)² × 20 = 1,25 et σ(Z) = √1,25 ≈ 1,12, soit σ(X) / 4 = 4,47 / 4 ≈ 1,12 : l'écart-type est multiplié par |a|.
:::

::: retenir
Moyenne = Σ nᵢxᵢ / N, variance = moyenne des carrés − carré de la moyenne, écart-type = √variance ; avec Y = aX + b, la moyenne devient aX̄ + b et l'écart-type |a| σ(X).
:::

## 📦 Médiane, quartiles et boîte à moustaches

Quinze élèves notent leur durée de trajet (en minutes) entre la maison et le lycée, rangée dans l'ordre croissant : 5, 8, 10, 10, 12, 15, 15, 18, 20, 22, 25, 25, 30, 35, 50. La moyenne est 20 min, mais l'élève qui met 50 min la tire vers le haut.
Quel nombre donne le trajet « du milieu » sans se laisser tromper par une valeur extrême, et comment dessiner toute la série avec seulement cinq nombres ?

::: definition
Pour une série rangée dans l'ordre croissant :

- la **médiane** Me partage la série en deux groupes de même effectif ;
- les **quartiles** Q₁ et Q₃ la partagent en quatre groupes de même effectif ; l'**intervalle interquartile** [Q₁ ; Q₃] contient 50 % des valeurs et l'**écart interquartile** est Q₃ − Q₁ ;
- Q₁ est la valeur de rang ⌈N/4⌉ et Q₃ celle de rang ⌈3N/4⌉, où ⌈t⌉ est le plus petit entier supérieur ou égal à t.

Le **diagramme en boîte** (boîte à moustaches) dessine les cinq nombres : minimum, Q₁, Me, Q₃, maximum.
:::

::: figure Diagramme en boîte des trajets : la boîte va de Q₁ à Q₃ et contient 50 % des élèves, le trait vert marque la médiane, les moustaches vont jusqu'au minimum et au maximum
<svg viewBox="0 0 340 170">
<title>Diagramme en boîte des durées de trajet en minutes : minimum 5, Q₁ = 10, médiane 18, Q₃ = 25, maximum 50</title>
<line x1="22" y1="118" x2="22" y2="122" stroke="#0f172a" stroke-width="1.2"/>
<text x="22" y="134" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >0</text>
<line x1="81.2" y1="118" x2="81.2" y2="122" stroke="#0f172a" stroke-width="1.2"/>
<text x="81.2" y="134" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >10</text>
<line x1="140.4" y1="118" x2="140.4" y2="122" stroke="#0f172a" stroke-width="1.2"/>
<text x="140.4" y="134" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >20</text>
<line x1="199.6" y1="118" x2="199.6" y2="122" stroke="#0f172a" stroke-width="1.2"/>
<text x="199.6" y="134" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >30</text>
<line x1="258.8" y1="118" x2="258.8" y2="122" stroke="#0f172a" stroke-width="1.2"/>
<text x="258.8" y="134" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >40</text>
<line x1="318" y1="118" x2="318" y2="122" stroke="#0f172a" stroke-width="1.2"/>
<text x="318" y="134" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >50</text>
<path d="M22 118 L318 118" fill="none" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/>
<text x="318" y="149" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >durée (min)</text>
<line x1="51.6" y1="75" x2="81.2" y2="75" stroke="#0f172a" stroke-width="2" stroke-linecap="round"/>
<line x1="170" y1="75" x2="318" y2="75" stroke="#0f172a" stroke-width="2" stroke-linecap="round"/>
<line x1="51.6" y1="66" x2="51.6" y2="84" stroke="#0f172a" stroke-width="2" stroke-linecap="round"/>
<line x1="318" y1="66" x2="318" y2="84" stroke="#0f172a" stroke-width="2" stroke-linecap="round"/>
<rect x="81.2" y="58" width="88.8" height="34" fill="#0f6e56" fill-opacity="0.12" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/>
<line x1="128.6" y1="58" x2="128.6" y2="92" stroke="#0f6e56" stroke-width="3" stroke-linecap="round"/>
<text x="51.6" y="50" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >min = 5</text>
<text x="128.6" y="50" text-anchor="middle" font-size="11" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >Me = 18</text>
<text x="294" y="50" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >max = 50</text>
<text x="81.2" y="108" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >Q₁ = 10</text>
<text x="170" y="108" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >Q₃ = 25</text>
</svg>
:::

Sur la figure, la boîte part de Q₁ = 10 et finit à Q₃ = 25 : sa largeur est l'écart interquartile, et chacune des quatre parties du diagramme contient environ un quart des élèves.

::: exemple Les cinq nombres des trajets

1. N = 15 est impair : Me est la valeur de rang (15 + 1) / 2 = 8, donc Me = 18 min.
2. Q₁ a pour rang ⌈15/4⌉ = ⌈3,75⌉ = 4, donc Q₁ = 10 min. Q₃ a pour rang ⌈45/4⌉ = ⌈11,25⌉ = 12, donc Q₃ = 25 min.
3. L'écart interquartile vaut 25 − 10 = 15 min, avec un minimum de 5 et un maximum de 50.
4. La moyenne (20) dépasse la médiane (18) : remplacer 50 par 100 laisserait Me inchangée mais ferait monter la moyenne. La médiane résiste aux valeurs extrêmes.

:::

::: exemple Quartiles d'une série en classes
Un site compte 80 abonnés ; le tableau donne leur durée de connexion (en min).

| Durée           | [0 ; 10[ | [10 ; 20[ | [20 ; 30[ | [30 ; 40[ | [40 ; 50[ |
| --------------- | -------- | --------- | --------- | --------- | --------- |
| Effectif        | 8        | 20        | 24        | 20        | 8         |
| Effectif cumulé | 8        | 28        | 52        | 72        | 80        |

1. Q₁ est la valeur de rang N/4 = 20. Le cumul passe de 8 à 28 dans la classe [10 ; 20[ : c'est la classe de Q₁.
2. On suppose les valeurs réparties uniformément dans la classe : (Q₁ − 10) / (20 − 10) = (20 − 8) / (28 − 8), donc Q₁ = 10 + 10 × 12/20 = 16 min.
3. De même, Me est la valeur de rang 40, dans [20 ; 30[ où le cumul passe de 28 à 52 : Me = 20 + 10 × (40 − 28)/(52 − 28) = 25 min.

:::

::: piege
**Erreur : donner le rang à la place de la valeur.** Pour 15 valeurs, on écrit Q₁ = 4, parce que le calcul ⌈15/4⌉ = 4 est celui qui vient d'être fait. Mais 4 est la position dans la liste rangée : Q₁ est la valeur qui occupe cette position, soit 10 min.
:::

::: propriete
Si N est pair, la médiane est la moyenne des deux valeurs centrales : pour 5, 7, 8, 12, Me = (7 + 8) / 2 = 7,5. Dans un diagramme en boîte, chacune des quatre parties (minimum–Q₁, Q₁–Me, Me–Q₃, Q₃–maximum) contient environ 25 % des valeurs. Pour une série en classes, on situe le rang dans les effectifs cumulés, puis on interpole linéairement dans la classe.
Cas limite : l'écart interquartile mesure la dispersion autour de la médiane sans dépendre des valeurs extrêmes, alors que l'écart-type en dépend.
:::

::: verifie À toi : le troisième quartile
Avec le tableau des 80 abonnés, calcule Q₃.

---

Q₃ est la valeur de rang 3N/4 = 60. Le cumul passe de 52 à 72 dans [30 ; 40[. Par interpolation, Q₃ = 30 + 10 × (60 − 52)/(72 − 52) = 30 + 4 = 34 min : on situe le rang dans la classe, puis on avance proportionnellement.
:::

::: retenir
Me coupe la série en deux moitiés, Q₁ et Q₃ en quarts ; la boîte de Q₁ à Q₃ contient 50 % des valeurs ; pour des classes, on repère le rang dans les effectifs cumulés puis on interpole.
:::

## 🔵 Nuage de points, point moyen et droite de Mayer

Le serveur du laboratoire d'informatique est testé six fois : à chaque essai, on relève le nombre X de dizaines d'utilisateurs connectés et le temps de réponse moyen Y (en ms).

| Essai | 1   | 2   | 3   | 4   | 5   | 6   |
| ----- | --- | --- | --- | --- | --- | --- |
| X     | 2   | 3   | 4   | 5   | 6   | 10  |
| Y     | 9   | 11  | 16  | 15  | 18  | 27  |

Comment représenter ces six couples, quel point les résume, et comment tracer une droite qui les suit sans la faire à l'œil ?

::: definition
Les n couples (xᵢ ; yᵢ) des valeurs de deux caractères X et Y observés sur les mêmes n individus forment une **série statistique à deux caractères**. Dans un repère orthogonal, les points Mᵢ(xᵢ ; yᵢ) forment le **nuage de points**, et le point G(X̄ ; Ȳ) est son **point moyen**.
:::

::: figure Les six points sont partagés par la parallèle pointillée à l'axe des ordonnées ; G₁ et G₂ (carrés verts) sont les points moyens des deux groupes, et la droite (G₁G₂) passe par G (croix ambre)
<svg viewBox="0 0 340 250">
<title>Nuage des six points (utilisateurs, temps de réponse), points moyens G₁(3 ; 12) et G₂(7 ; 20) des deux groupes, droite de Mayer y = 2x + 6 et point moyen G(5 ; 16)</title>
<line x1="94.7" y1="208" x2="94.7" y2="22" stroke="#e2e8f0" stroke-width="1"/>
<line x1="139.3" y1="208" x2="139.3" y2="22" stroke="#e2e8f0" stroke-width="1"/>
<line x1="184" y1="208" x2="184" y2="22" stroke="#e2e8f0" stroke-width="1"/>
<line x1="228.7" y1="208" x2="228.7" y2="22" stroke="#e2e8f0" stroke-width="1"/>
<line x1="273.3" y1="208" x2="273.3" y2="22" stroke="#e2e8f0" stroke-width="1"/>
<line x1="318" y1="208" x2="318" y2="22" stroke="#e2e8f0" stroke-width="1"/>
<line x1="50" y1="146" x2="318" y2="146" stroke="#e2e8f0" stroke-width="1"/>
<line x1="50" y1="84" x2="318" y2="84" stroke="#e2e8f0" stroke-width="1"/>
<line x1="50" y1="22" x2="318" y2="22" stroke="#e2e8f0" stroke-width="1"/>
<path d="M50 22 L50 208 L318 208" fill="none" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/>
<line x1="94.7" y1="208" x2="94.7" y2="212" stroke="#0f172a" stroke-width="1.2"/>
<text x="94.7" y="224" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >2</text>
<line x1="139.3" y1="208" x2="139.3" y2="212" stroke="#0f172a" stroke-width="1.2"/>
<text x="139.3" y="224" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >4</text>
<line x1="184" y1="208" x2="184" y2="212" stroke="#0f172a" stroke-width="1.2"/>
<text x="184" y="224" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >6</text>
<line x1="228.7" y1="208" x2="228.7" y2="212" stroke="#0f172a" stroke-width="1.2"/>
<text x="228.7" y="224" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >8</text>
<line x1="273.3" y1="208" x2="273.3" y2="212" stroke="#0f172a" stroke-width="1.2"/>
<text x="273.3" y="224" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >10</text>
<line x1="318" y1="208" x2="318" y2="212" stroke="#0f172a" stroke-width="1.2"/>
<text x="318" y="224" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >12</text>
<line x1="46" y1="146" x2="50" y2="146" stroke="#0f172a" stroke-width="1.2"/>
<text x="43" y="150" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >10</text>
<line x1="46" y1="84" x2="50" y2="84" stroke="#0f172a" stroke-width="1.2"/>
<text x="43" y="88" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >20</text>
<line x1="46" y1="22" x2="50" y2="22" stroke="#0f172a" stroke-width="1.2"/>
<text x="43" y="26" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >30</text>
<text x="318" y="237" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >X (dizaines d'utilisateurs)</text>
<text x="54" y="17" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >Y (ms)</text>
<line x1="150.5" y1="208" x2="150.5" y2="22" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round" stroke-dasharray="5 4"/>
<line x1="72.3" y1="158.4" x2="295.7" y2="34.4" stroke="#0f6e56" stroke-width="2.2" stroke-linecap="round"/>
<circle cx="94.7" cy="152.2" r="4" fill="#0f172a" stroke="#ffffff" stroke-width="1"/>
<circle cx="117" cy="139.8" r="4" fill="#0f172a" stroke="#ffffff" stroke-width="1"/>
<circle cx="139.3" cy="108.8" r="4" fill="#0f172a" stroke="#ffffff" stroke-width="1"/>
<circle cx="161.7" cy="115" r="4" fill="#0f172a" stroke="#ffffff" stroke-width="1"/>
<circle cx="184" cy="96.4" r="4" fill="#0f172a" stroke="#ffffff" stroke-width="1"/>
<circle cx="273.3" cy="40.6" r="4" fill="#0f172a" stroke="#ffffff" stroke-width="1"/>
<rect x="112" y="128.6" width="10" height="10" fill="#0f6e56" stroke="#ffffff" stroke-width="1"/>
<rect x="201.3" y="79" width="10" height="10" fill="#0f6e56" stroke="#ffffff" stroke-width="1"/>
<line x1="154.7" y1="101.8" x2="168.7" y2="115.8" stroke="#b45309" stroke-width="2.6" stroke-linecap="round"/><line x1="154.7" y1="115.8" x2="168.7" y2="101.8" stroke="#b45309" stroke-width="2.6" stroke-linecap="round"/>
<text x="101" y="123.6" text-anchor="middle" font-size="13" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >G₁</text>
<text x="206.3" y="70" text-anchor="middle" font-size="13" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >G₂</text>
<text x="177.7" y="122.8" text-anchor="middle" font-size="13" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >G</text>
</svg>
:::

Sur la figure, G₁(3 ; 12) est le point moyen des trois points de gauche, G₂(7 ; 20) celui des trois points de droite, et G(5 ; 16) se trouve sur la droite qui joint G₁ à G₂.

::: exemple La droite de Mayer du serveur

1. X̄ = 30 / 6 = 5 et Ȳ = 96 / 6 = 16, donc G(5 ; 16).
2. Les points sont déjà rangés par abscisses croissantes : on forme deux groupes de même effectif, {M₁, M₂, M₃} et {M₄, M₅, M₆}.
3. G₁((2 + 3 + 4)/3 ; (9 + 11 + 16)/3) = (3 ; 12) et G₂((5 + 6 + 10)/3 ; (15 + 18 + 27)/3) = (7 ; 20).
4. La pente de (G₁G₂) est (20 − 12) / (7 − 3) = 2, et y − 12 = 2(x − 3) donne y = 2x + 6.
5. Contrôle : pour G, 2 × 5 + 6 = 16 ✓. Prévision pour 80 utilisateurs (x = 8) : y = 22 ms.

:::

::: piege
**Erreur : partager les points sans les trier par abscisses croissantes.** Si le relevé est saisi dans le désordre, (10 ; 27), (2 ; 9), (5 ; 15), (6 ; 18), (3 ; 11), (4 ; 16), prendre les trois premiers couples tente parce que la liste est déjà coupée en deux. On obtient G₁(17/3 ; 17) et G₂(13/3 ; 15), donc la droite y = 1,5x + 8,5 au lieu de y = 2x + 6. Il faut d'abord ranger selon X.
:::

::: methode La droite de Mayer

1. Ranger les couples par valeurs croissantes de X.
2. Les partager en deux groupes de même effectif (à un près si n est impair).
3. Calculer le point moyen de chaque groupe, G₁ puis G₂.
4. Écrire l'équation de la droite (G₁G₂) : c'est la **droite de Mayer**.

Cas limite : G appartient toujours à (G₁G₂) ; en revanche, deux partages différents donnent deux droites de Mayer différentes, ce qui pose la question de la « meilleure » droite.

:::

::: verifie À toi : une autre série
Pour la série (1 ; 4), (3 ; 6), (5 ; 12), (7 ; 14), détermine la droite de Mayer, puis la prévision pour x = 10.

---

Les points sont rangés ; deux groupes de deux points : G₁((1 + 3)/2 ; (4 + 6)/2) = (2 ; 5) et G₂((5 + 7)/2 ; (12 + 14)/2) = (6 ; 13). La pente est (13 − 5) / (6 − 2) = 2, donc y − 5 = 2(x − 2), soit y = 2x + 1. Pour x = 10, y = 21.
:::

::: retenir
Le nuage est formé des points Mᵢ(xᵢ ; yᵢ), son point moyen est G(X̄ ; Ȳ), et la droite de Mayer est la droite (G₁G₂) des points moyens de deux moitiés du nuage rangé par abscisses croissantes.
:::

## 🤝 La covariance : varier ensemble

Dans le serveur, regarde les écarts à la moyenne (X̄ = 5, Ȳ = 16) : quand X dépasse 5, Y dépasse-t-il 16 ?

| xᵢ      | 2   | 3   | 4   | 5   | 6   | 10  |
| ------- | --- | --- | --- | --- | --- | --- |
| xᵢ − X̄  | −3  | −2  | −1  | 0   | 1   | 5   |
| yᵢ − Ȳ  | −7  | −5  | 0   | −1  | 2   | 11  |
| Produit | 21  | 10  | 0   | 0   | 2   | 55  |

Presque tous les produits sont positifs : les deux écarts ont le même signe. Comment résumer cela par un seul nombre ?

::: definition
La **covariance** de X et Y est le réel
$$ cov(X ; Y) = (1/n) Σ (xᵢ − X̄)(yᵢ − Ȳ) $$
C'est la moyenne des produits des écarts à la moyenne.
:::

Dans le tableau, la dernière ligne contient les produits (xᵢ − X̄)(yᵢ − Ȳ) : leur somme est 88.

::: exemple Les deux calculs de la covariance

1. Par la définition : cov(X ; Y) = 88 / 6 = 44/3 ≈ 14,67, positive car la plupart des produits sont positifs.
2. Développons (xᵢ − X̄)(yᵢ − Ȳ) = xᵢyᵢ − X̄yᵢ − Ȳxᵢ + X̄Ȳ. En faisant la moyenne, les deux termes du milieu valent chacun −X̄Ȳ, d'où cov(X ; Y) = (1/n) Σ xᵢyᵢ − X̄Ȳ.
3. Ici Σ xᵢyᵢ = 18 + 33 + 64 + 75 + 108 + 270 = 568, donc cov(X ; Y) = 568/6 − 5 × 16 = 94,67 − 80 ≈ 14,67 ✓ : les deux méthodes donnent le même résultat.

:::

::: piege
**Erreur : oublier de retrancher X̄Ȳ.** On calcule la moyenne des produits 568 / 6 ≈ 94,67 et l'on s'arrête, parce que cette moyenne ressemble déjà à une covariance. La valeur 94,67 est très loin de 14,67 : il faut retrancher X̄Ȳ = 5 × 16 = 80 pour obtenir la covariance.
:::

::: propriete
Pour une série double (xᵢ ; yᵢ) de n couples :

- cov(X ; Y) = (1/n) Σ xᵢyᵢ − X̄Ȳ et cov(X ; Y) = cov(Y ; X) ;
- cov(aX + b ; Y) = a cov(X ; Y) pour tous réels a et b ;
- cov(X ; X) = V(X) ;
- cov(X ; Y)² ≤ V(X) V(Y) (admis), donc |cov(X ; Y)| ≤ σ(X) σ(Y).

Cas limite : une covariance nulle ne signifie pas que les caractères sont sans lien, seulement que les produits positifs et négatifs se compensent. Et changer d'unité (a ≠ 1) change la covariance : elle n'est donc pas un indicateur de force.
:::

::: verifie À toi : un changement de variable
Dans le serveur, on remplace X par X′ = 2X − 1. Que vaut cov(X′ ; Y) ?

---

D'après cov(aX + b ; Y) = a cov(X ; Y) avec a = 2 et b = −1, cov(X′ ; Y) = 2 × 44/3 = 88/3 ≈ 29,33 : le facteur 2 multiplie la covariance, alors que la constante −1 ne joue aucun rôle.
:::

::: retenir
cov(X ; Y) = moyenne des produits xᵢyᵢ − X̄Ȳ ; elle a le signe de la liaison, vérifie cov(aX + b ; Y) = a cov(X ; Y), cov(X ; X) = V(X) et |cov| ≤ σ(X) σ(Y), mais dépend des unités.
:::

## 🎚️ Le coefficient de corrélation linéaire

Si l'on exprime les temps de réponse en secondes au lieu de millisecondes, la covariance du serveur est divisée par 1000 : 0,01467 au lieu de 14,67. La liaison est pourtant la même.
Comment fabriquer un nombre qui mesure la force de la liaison linéaire sans dépendre des unités ?

::: definition
Pour deux caractères non constants X et Y, le **coefficient de corrélation linéaire** est le réel
$$ r = cov(X ; Y) / (σ(X) σ(Y)) $$
:::

::: exemple Le serveur
Pour la série du serveur, cov(X ; Y) = 44/3.

1. Σ xᵢ² = 4 + 9 + 16 + 25 + 36 + 100 = 190, donc V(X) = 190/6 − 25 = 20/3 et σ(X) ≈ 2,582.
2. Σ yᵢ² = 81 + 121 + 256 + 225 + 324 + 729 = 1736, donc V(Y) = 1736/6 − 256 = 100/3 et σ(Y) ≈ 5,774.
3. r = (44/3) / (2,582 × 5,774) ≈ 14,667 / 14,907 ≈ 0,98.
4. |r| ≥ 0,75 : la corrélation linéaire est forte et le signe de r, positif, dit que Y croît avec X.

:::

::: exemple Un nuage sans forme linéaire
Les cinq points (−2 ; 4), (−1 ; 1), (0 ; 0), (1 ; 1), (2 ; 4) vérifient y = x². On a X̄ = 0 et Σ xᵢyᵢ = −8 − 1 + 0 + 1 + 8 = 0, donc cov(X ; Y) = 0 − 0 × Ȳ = 0 et r = 0, alors que Y est une fonction de X.
:::

::: piege
**Erreur : juger la force de la liaison au signe de r.** On lit r = −0,9 et l'on conclut « corrélation faible » parce que le nombre est négatif. Mais le signe indique seulement le sens de variation (Y diminue quand X augmente) ; la force se lit sur |r| = 0,9 ≥ 0,75 : la liaison est forte.
:::

::: propriete
Pour X et Y non constantes :

- −1 ≤ r ≤ 1, et |r| = 1 si et seulement si les points du nuage sont alignés ;
- r a le signe de cov(X ; Y) ;
- si a > 0, r(aX + b ; Y) = r(X ; Y) : r ne dépend ni de l'unité ni de l'origine (si a < 0, il change de signe) ;
- si |r| ≥ 0,75, la corrélation linéaire est **forte** et un ajustement affine est justifié ; si |r| < 0,75, elle est **faible**.

Cas limites : |r| = 0,75 compte comme forte ; r = 0 n'exclut pas un lien non affine, comme dans le nuage de la parabole.
:::

::: verifie À toi : une corrélation faible
Calcule r pour (1 ; 1), (2 ; 3), (3 ; 2), puis conclus.

---

X̄ = 2 et Ȳ = 2. Les produits d'écarts valent 1, 0 et 0, donc cov = 1/3. De plus V(X) = V(Y) = (1 + 0 + 1)/3 = 2/3, donc r = (1/3) / (2/3) = 0,5. Comme |r| < 0,75, la corrélation est faible : un ajustement affine n'est pas justifié.
:::

::: retenir
r = cov(X ; Y) / (σ(X) σ(Y)) est un nombre sans unité compris entre −1 et 1 ; |r| ≥ 0,75 signale une corrélation forte, le signe de r donne le sens, et r = 0 n'exclut pas un lien non affine.
:::

## 📈 La droite des moindres carrés et la prévision

Pour le serveur, la droite de Mayer est y = 2x + 6, mais un autre partage des points en donnerait une autre. Quelle droite choisir, sachant qu'aucune ne passe par les six points ?
Et jusqu'où peut-on se fier à une droite pour prévoir, y compris hors de la plage observée ?

::: definition
Soit D la droite d'équation y = ax + b et Pᵢ le point de D d'abscisse xᵢ. L'ajustement affine de Y en X par la **méthode des moindres carrés** choisit la droite qui rend minimale la somme
$$ S = Σ (MᵢPᵢ)² = Σ (yᵢ − (axᵢ + b))² $$
des carrés des écarts verticaux. Cette droite est la **droite de régression de Y en X**.
:::

::: figure Les segments pointillés verticaux relient chaque point Mᵢ au point Pᵢ de la droite D de même abscisse : la droite de régression rend la somme de leurs carrés minimale
<svg viewBox="0 0 340 330">
<title>Nuage des six points et droite D : y = 2,2x + 5, avec les écarts verticaux MᵢPᵢ en pointillés dont les carrés valent 0,16 ; 0,36 ; 4,84 ; 1 ; 0,04 et 0</title>
<line x1="75.5" y1="290" x2="75.5" y2="22" stroke="#e2e8f0" stroke-width="1"/>
<line x1="126.6" y1="290" x2="126.6" y2="22" stroke="#e2e8f0" stroke-width="1"/>
<line x1="177.6" y1="290" x2="177.6" y2="22" stroke="#e2e8f0" stroke-width="1"/>
<line x1="228.7" y1="290" x2="228.7" y2="22" stroke="#e2e8f0" stroke-width="1"/>
<line x1="279.7" y1="290" x2="279.7" y2="22" stroke="#e2e8f0" stroke-width="1"/>
<line x1="50" y1="238.5" x2="318" y2="238.5" stroke="#e2e8f0" stroke-width="1"/>
<line x1="50" y1="135.4" x2="318" y2="135.4" stroke="#e2e8f0" stroke-width="1"/>
<line x1="50" y1="32.3" x2="318" y2="32.3" stroke="#e2e8f0" stroke-width="1"/>
<path d="M50 22 L50 290 L318 290" fill="none" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/>
<line x1="75.5" y1="290" x2="75.5" y2="294" stroke="#0f172a" stroke-width="1.2"/>
<text x="75.5" y="306" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >2</text>
<line x1="126.6" y1="290" x2="126.6" y2="294" stroke="#0f172a" stroke-width="1.2"/>
<text x="126.6" y="306" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >4</text>
<line x1="177.6" y1="290" x2="177.6" y2="294" stroke="#0f172a" stroke-width="1.2"/>
<text x="177.6" y="306" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >6</text>
<line x1="228.7" y1="290" x2="228.7" y2="294" stroke="#0f172a" stroke-width="1.2"/>
<text x="228.7" y="306" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >8</text>
<line x1="279.7" y1="290" x2="279.7" y2="294" stroke="#0f172a" stroke-width="1.2"/>
<text x="279.7" y="306" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >10</text>
<line x1="46" y1="238.5" x2="50" y2="238.5" stroke="#0f172a" stroke-width="1.2"/>
<text x="43" y="242.5" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >10</text>
<line x1="46" y1="135.4" x2="50" y2="135.4" stroke="#0f172a" stroke-width="1.2"/>
<text x="43" y="139.4" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >20</text>
<line x1="46" y1="32.3" x2="50" y2="32.3" stroke="#0f172a" stroke-width="1.2"/>
<text x="43" y="36.3" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >30</text>
<text x="318" y="319" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >X (dizaines d'utilisateurs)</text>
<text x="54" y="17" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >Y (ms)</text>
<line x1="55.1" y1="262.8" x2="305.2" y2="40.6" stroke="#0f6e56" stroke-width="2.4" stroke-linecap="round"/>
<line x1="75.5" y1="248.8" x2="75.5" y2="244.6" stroke="#b45309" stroke-width="2.6" stroke-linecap="round" stroke-dasharray="4 3"/>
<line x1="101" y1="228.2" x2="101" y2="222" stroke="#b45309" stroke-width="2.6" stroke-linecap="round" stroke-dasharray="4 3"/>
<line x1="126.6" y1="176.6" x2="126.6" y2="199.3" stroke="#b45309" stroke-width="2.6" stroke-linecap="round" stroke-dasharray="4 3"/>
<line x1="152.1" y1="186.9" x2="152.1" y2="176.6" stroke="#b45309" stroke-width="2.6" stroke-linecap="round" stroke-dasharray="4 3"/>
<line x1="177.6" y1="156" x2="177.6" y2="153.9" stroke="#b45309" stroke-width="2.6" stroke-linecap="round" stroke-dasharray="4 3"/>
<line x1="279.7" y1="63.2" x2="279.7" y2="63.2" stroke="#b45309" stroke-width="2.6" stroke-linecap="round" stroke-dasharray="4 3"/>
<circle cx="75.5" cy="248.8" r="3.5" fill="#0f172a" stroke="#ffffff" stroke-width="1"/>
<circle cx="101" cy="228.2" r="3.5" fill="#0f172a" stroke="#ffffff" stroke-width="1"/>
<circle cx="126.6" cy="176.6" r="3.5" fill="#0f172a" stroke="#ffffff" stroke-width="1"/>
<circle cx="152.1" cy="186.9" r="3.5" fill="#0f172a" stroke="#ffffff" stroke-width="1"/>
<circle cx="177.6" cy="156" r="3.5" fill="#0f172a" stroke="#ffffff" stroke-width="1"/>
<circle cx="279.7" cy="63.2" r="3.5" fill="#0f172a" stroke="#ffffff" stroke-width="1"/>
<text x="315.2" y="54.6" text-anchor="middle" font-size="13" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >D</text>
</svg>
:::

Sur la figure, les écarts MᵢPᵢ entre les points et la droite D : y = 2,2x + 5 valent 0,4 ; 0,6 ; 2,2 ; 1 ; 0,2 et 0 : leurs carrés, 0,16 ; 0,36 ; 4,84 ; 1 ; 0,04 et 0, donnent la somme S = 6,4.

::: exemple Trouver la droite par un trinôme

1. Pour a fixé, S est un trinôme en b dont le minimum est atteint quand b est la moyenne des yᵢ − axᵢ, c'est-à-dire b = Ȳ − aX̄ : la droite passe par G.
2. Alors yᵢ − (axᵢ + b) = (yᵢ − Ȳ) − a(xᵢ − X̄). En développant et en faisant la somme, S(a) = n [a² V(X) − 2a cov(X ; Y) + V(Y)].
3. Comme V(X) > 0, c'est un trinôme en a, minimal pour a = 2 cov(X ; Y) / (2 V(X)) = cov(X ; Y) / V(X).
4. Pour le serveur : a = (44/3) / (20/3) = 2,2 et b = 16 − 2,2 × 5 = 5, donc y = 2,2x + 5.
5. Contrôle : S = 6,4 pour cette droite, alors que la droite de Mayer y = 2x + 6 donne 1 + 1 + 4 + 1 + 0 + 1 = 8 ✓ : la régression fait mieux.

:::

::: piege
**Erreur : minimiser la somme des écarts sans les élever au carré.** Pour toute droite qui passe par G, Σ (yᵢ − (axᵢ + b)) = 0, car les écarts positifs et négatifs se compensent. La droite horizontale y = 16 passe par G et annule donc cette somme, alors que Σ (yᵢ − 16)² = 200, bien plus que 6,4. Seuls les carrés empêchent la compensation.
:::

::: propriete
Si V(X) ≠ 0, la droite de régression de Y en X passe par G et a pour équation
$$ y = a (x − X̄) + Ȳ $$
$$ a = cov(X ; Y) / V(X) $$
Une valeur x₀ de X permet de prévoir Y par y₀ = ax₀ + b. Si x₀ est dans l'intervalle des valeurs observées, c'est une **interpolation** ; sinon c'est une **extrapolation**, qui suppose que le modèle reste plausible hors de cet intervalle.
Cas limite : pour le serveur (x entre 2 et 10), x = 7 donne y = 20,4 ms (interpolation), alors que x = 30 donne 71 ms (extrapolation, à ne croire que si la charge reste linéaire).
:::

::: verifie À toi : trois points
Détermine la droite de régression de Y en X pour (1 ; 2), (2 ; 3), (3 ; 7).

---

X̄ = 2, Ȳ = 4, Σ xᵢyᵢ = 29 donc cov = 29/3 − 8 = 5/3 ; V(X) = 14/3 − 4 = 2/3. Ainsi a = (5/3) / (2/3) = 2,5 et b = 4 − 2,5 × 2 = −1 : y = 2,5x − 1, qui passe par G(2 ; 4).
:::

::: retenir
La droite de régression de Y en X minimise Σ (yᵢ − (axᵢ + b))², passe par G et a pour pente a = cov(X ; Y) / V(X) ; on interpole dans la plage observée et l'on extrapole avec prudence.
:::

## 🔁 Les deux droites de régression

Le serveur permet aussi la question inverse : on mesure un temps de réponse Y et l'on veut estimer le nombre X de dizaines d'utilisateurs connectés.
Faut-il simplement isoler x dans y = 2,2x + 5 ?

::: definition
La **droite de régression de X en Y** est la droite D′ qui minimise la somme des carrés des écarts **horizontaux** : elle a pour équation x = a′y + b′, avec
$$ a′ = cov(X ; Y) / V(Y) $$
$$ b′ = X̄ − a′Ȳ $$
:::

::: figure Les deux droites de régression se coupent au point moyen G : D (trait plein) prévoit Y à partir de X, D′ (pointillés) prévoit X à partir de Y
<svg viewBox="0 0 340 250">
<title>Nuage des six points, droite D : y = 2,2x + 5 et droite D′ : x = 0,44y − 2,04, qui se coupent au point moyen G(5 ; 16)</title>
<line x1="94.7" y1="208" x2="94.7" y2="22" stroke="#e2e8f0" stroke-width="1"/>
<line x1="139.3" y1="208" x2="139.3" y2="22" stroke="#e2e8f0" stroke-width="1"/>
<line x1="184" y1="208" x2="184" y2="22" stroke="#e2e8f0" stroke-width="1"/>
<line x1="228.7" y1="208" x2="228.7" y2="22" stroke="#e2e8f0" stroke-width="1"/>
<line x1="273.3" y1="208" x2="273.3" y2="22" stroke="#e2e8f0" stroke-width="1"/>
<line x1="318" y1="208" x2="318" y2="22" stroke="#e2e8f0" stroke-width="1"/>
<line x1="50" y1="154.9" x2="318" y2="154.9" stroke="#e2e8f0" stroke-width="1"/>
<line x1="50" y1="101.7" x2="318" y2="101.7" stroke="#e2e8f0" stroke-width="1"/>
<line x1="50" y1="48.6" x2="318" y2="48.6" stroke="#e2e8f0" stroke-width="1"/>
<path d="M50 22 L50 208 L318 208" fill="none" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/>
<line x1="94.7" y1="208" x2="94.7" y2="212" stroke="#0f172a" stroke-width="1.2"/>
<text x="94.7" y="224" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >2</text>
<line x1="139.3" y1="208" x2="139.3" y2="212" stroke="#0f172a" stroke-width="1.2"/>
<text x="139.3" y="224" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >4</text>
<line x1="184" y1="208" x2="184" y2="212" stroke="#0f172a" stroke-width="1.2"/>
<text x="184" y="224" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >6</text>
<line x1="228.7" y1="208" x2="228.7" y2="212" stroke="#0f172a" stroke-width="1.2"/>
<text x="228.7" y="224" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >8</text>
<line x1="273.3" y1="208" x2="273.3" y2="212" stroke="#0f172a" stroke-width="1.2"/>
<text x="273.3" y="224" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >10</text>
<line x1="318" y1="208" x2="318" y2="212" stroke="#0f172a" stroke-width="1.2"/>
<text x="318" y="224" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >12</text>
<line x1="46" y1="154.9" x2="50" y2="154.9" stroke="#0f172a" stroke-width="1.2"/>
<text x="43" y="158.9" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >10</text>
<line x1="46" y1="101.7" x2="50" y2="101.7" stroke="#0f172a" stroke-width="1.2"/>
<text x="43" y="105.7" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >20</text>
<line x1="46" y1="48.6" x2="50" y2="48.6" stroke="#0f172a" stroke-width="1.2"/>
<text x="43" y="52.6" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >30</text>
<text x="318" y="237" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >X (dizaines d'utilisateurs)</text>
<text x="54" y="17" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >Y (ms)</text>
<line x1="50" y1="181.4" x2="318" y2="41.1" stroke="#0f6e56" stroke-width="2.4" stroke-linecap="round"/>
<line x1="50" y1="183.4" x2="318" y2="38.4" stroke="#b45309" stroke-width="2.4" stroke-linecap="round" stroke-dasharray="6 4"/>
<circle cx="94.7" cy="160.2" r="4" fill="#0f172a" stroke="#ffffff" stroke-width="1"/>
<circle cx="117" cy="149.5" r="4" fill="#0f172a" stroke="#ffffff" stroke-width="1"/>
<circle cx="139.3" cy="123" r="4" fill="#0f172a" stroke="#ffffff" stroke-width="1"/>
<circle cx="161.7" cy="128.3" r="4" fill="#0f172a" stroke="#ffffff" stroke-width="1"/>
<circle cx="184" cy="112.3" r="4" fill="#0f172a" stroke="#ffffff" stroke-width="1"/>
<circle cx="273.3" cy="64.5" r="4" fill="#0f172a" stroke="#ffffff" stroke-width="1"/>
<line x1="154.7" y1="116" x2="168.7" y2="130" stroke="#0f172a" stroke-width="2.6" stroke-linecap="round"/><line x1="154.7" y1="130" x2="168.7" y2="116" stroke="#0f172a" stroke-width="2.6" stroke-linecap="round"/>
<text x="177.7" y="137" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >G</text>
<text x="291.7" y="38.5" text-anchor="middle" font-size="13" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >D′</text>
<text x="312.8" y="63" text-anchor="middle" font-size="13" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" >D</text>
</svg>
:::

Sur la figure, les deux droites passent par G(5 ; 16) et sont presque confondues, car les points sont presque alignés.

::: exemple Les deux droites du serveur

1. a′ = (44/3) / (100/3) = 0,44 et b′ = 5 − 0,44 × 16 = −2,04, donc D′ : x = 0,44y − 2,04.
2. Pour un temps de réponse y = 30 ms, D′ donne x = 0,44 × 30 − 2,04 = 11,16 dizaines d'utilisateurs.
3. Isoler x dans D donnerait x = (30 − 5) / 2,2 ≈ 11,36 : ce n'est pas la même valeur, car D minimise les écarts verticaux et D′ les écarts horizontaux.
4. Contrôle : a × a′ = 2,2 × 0,44 = 0,968 = r² (r ≈ 0,984) ✓, et D, D′ passent par G(5 ; 16).

:::

::: piege
**Erreur : prendre pour D′ la droite D écrite à l'envers.** En isolant x dans y = 2,2x + 5, on trouve x = 0,4545y − 2,2727, avec la pente 1/a au lieu de a′. Cela tente parce que « x en fonction de y » est la même relation en apparence. Mais les deux pentes valent a′ = 0,44 et 1/a ≈ 0,4545 : elles ne coïncident que si |r| = 1.
:::

::: propriete
Avec cov(X ; Y) ≠ 0, D : y = ax + b et D′ : x = a′y + b′ vérifient :

- D et D′ passent par le point moyen G ;
- a et a′ ont le signe de cov(X ; Y), donc le même signe ;
- a × a′ = r², donc 0 ≤ a a′ ≤ 1 ; D et D′ sont confondues si et seulement si |r| = 1.

Cas limite : si cov(X ; Y) = 0, alors a = a′ = 0, D est la droite horizontale y = Ȳ, D′ la droite verticale x = X̄, et r = 0.
:::

::: verifie À toi : une série alignée
Une série vérifie cov(X ; Y) = 6, V(X) = 4 et V(Y) = 9. Calcule a, a′ et r².

---

a = 6/4 = 1,5 et a′ = 6/9 = 2/3. Le produit a a′ = 1,5 × 2/3 = 1 donne r² = 1, donc |r| = 1 : les points sont alignés et D et D′ sont confondues.
:::

::: retenir
D : y = ax + b avec a = cov / V(X) prévoit Y, D′ : x = a′y + b′ avec a′ = cov / V(Y) prévoit X ; elles se coupent en G, a et a′ ont le même signe, et a a′ = r².
:::

## 🔄 Les ajustements non affines : changer de variable

Les inscrits à une application (en centaines) sur cinq semaines : 6, 9, 14, 21, 32 pour x = 1, 2, 3, 4, 5. La droite des moindres carrés est y = 6,4x − 2,8 et r ≈ 0,97 ; pourtant les écarts de la droite aux points valent +2,4 ; −1,0 ; −2,4 ; −1,8 ; +2,8.
Ces signes + − − − + disent que le nuage se courbe : comment retrouver une droite pour prévoir ?

::: definition
Pour **ajuster** un nuage courbe, on cherche une transformation z = φ(y) (ou X = φ(x)) qui aligne les points. On ajuste alors z par une droite des moindres carrés, puis on revient à y par la fonction réciproque.
:::

| Modèle                      | Droite à ajuster                 | Retour à y          |
| --------------------------- | -------------------------------- | ------------------- |
| y = A e^(Bx) (exponentiel)  | z = ln y en fonction de x        | y = e^z             |
| y = k x^α (puissance)       | Y = ln y en fonction de X = ln x | y = e^Y             |
| y = (ax + b)² (parabolique) | z = √y en fonction de x          | y = z²              |
| y = λ / x (inverse)         | y en fonction de 1/x             | aucun, y est direct |

La première colonne du tableau est le modèle, la deuxième la droite à tracer, la troisième l'opération qui ramène à y.

::: exemple Les inscrits à l'application

1. Le nuage croît de plus en plus vite : on essaie un modèle exponentiel y = A eᴮˣ, donc z = ln y.
2. z = ln y vaut 1,79 ; 2,20 ; 2,64 ; 3,04 ; 3,47 pour x = 1, …, 5 : les points (x ; z) sont presque alignés (r ≈ 1,00).
3. La droite des moindres carrés de z en x est z = 0,42x + 1,37.
4. On revient à y : y = e^(0,42x + 1,37) = e^1,37 × e^(0,42x) ≈ 3,94 e^(0,42x).
5. Prévision pour la semaine x = 6 : z = 0,42 × 6 + 1,37 = 3,89, donc y = e^3,89 ≈ 48,9 centaines. La droite y = 6,4x − 2,8 donnerait 35,6, beaucoup trop bas.

:::

::: exemple Un modèle puissance
Les points (1 ; 3), (2 ; 8,5), (4 ; 24), (8 ; 68) suivent y = k xᵅ. Alors ln y = α ln x + ln k.

1. X = ln x et Y = ln y valent (0 ; 1,10), (0,69 ; 2,14), (1,39 ; 3,18), (2,08 ; 4,22).
2. La droite des moindres carrés est Y = 1,50X + 1,10, donc α = 1,5 et ln k = 1,10.
3. k = e^1,10 ≈ 3,0, d'où y ≈ 3x^1,5 : le coefficient directeur est l'exposant, et l'ordonnée à l'origine est ln k.

:::

::: piege
**Erreur : s'arrêter à la prévision de z.** Pour x = 6, on obtient z = 3,89 et l'on annonce « 3,89 centaines d'inscrits ». Cela tente parce que 3,89 vient d'un calcul de régression. Mais z est le logarithme de y : la prévision est y = e^3,89 ≈ 48,9 centaines.
:::

::: methode Avec un tableur
Dans Excel : saisir les deux colonnes, insérer un graphique en nuage de points, faire un clic droit sur un point, choisir « Ajouter une courbe de tendance », puis le type (linéaire, exponentielle, puissance ou polynomiale d'ordre 2) et cocher « Afficher l'équation sur le graphique ».

Le type exponentiel et le type puissance font exactement le calcul de ce cours (ajustement affine de ln y). Le type polynomial d'ordre 2 ajuste une parabole directement sur y par les moindres carrés. Pour nos inscrits, la courbe exponentielle affiche une équation de la forme y ≈ 3,9 e^(0,42x).

Cas limite : le logarithme n'existe que pour y > 0, donc ces deux types sont impossibles si une valeur de Y est négative ou nulle.
:::

::: verifie À toi : une racine carrée
Un nuage de points est ajusté en posant z = √y, et l'on trouve z = 0,5x + 1. Quelle valeur de y prévoit-on pour x = 6 ?

---

Pour x = 6, z = 0,5 × 6 + 1 = 4. Comme z = √y, on revient à y en élevant au carré : y = 4² = 16. Prévoir z = 4 ne suffit pas : la réponse à la question est y.
:::

::: retenir
Quand le nuage se courbe, on aligne les points par un changement de variable (ln y, ln x et ln y, √y, 1/x), on ajuste une droite, puis on revient à y par la fonction réciproque avant de prévoir.
:::

> 🏆 Douzième porte franchie, héros. Tu résumes une série par sa moyenne, son écart-type, sa médiane et ses quartiles, tu traces le nuage et la droite de Mayer, tu mesures la liaison par r, tu écris les deux droites des moindres carrés et tu redresses un nuage courbe par ln ou √. Au chapitre 13, les probabilités prendront le relais.
