# ⚔️ Probabilités — du risque d'un client à la loi d'un gain

> 💡 « Une probabilité conditionnelle, c'est la même probabilité, calculée dans un monde plus petit : celui que l'on vient d'apprendre. »

Bienvenue, héros de l'Économie et gestion. Une banque se demande si une alerte de risque désigne vraiment les mauvais dossiers, un forain veut savoir si sa tombola rapporte, un commercial veut estimer ses signatures : toutes ces décisions se prennent sous incertitude. Huit étapes te mènent de la probabilité conditionnelle à la loi binomiale : probabilité conditionnelle, composées et arbre pondéré, indépendance, probabilités totales, formule de Bayes, espérance, variance et écart type, schéma de Bernoulli. On suppose acquis le dénombrement (le nombre C(n ; k) de façons de choisir k éléments parmi n) et, pour un seul calcul de la fin, le logarithme. Les calculs se font à la main, la calculatrice servant de contrôle.

## 🔵 La probabilité conditionnelle

Dans un magasin d'électroménager de Sfax, 200 clients ont été interrogés : 120 possèdent la carte de fidélité (événement F), 70 ont acheté un appareil (événement A), et 56 clients possèdent la carte et ont acheté.
Si l'on sait qu'un client possède la carte, quelle est la probabilité qu'il ait acheté ?

::: definition
Soit p une probabilité sur l'ensemble des issues, A un événement de probabilité non nulle et B un événement quelconque. La **probabilité de B sachant A** est le réel
$$ p(B/A) = p(A ∩ B) / p(A) $$
On la note aussi p_A(B). Le « sachant A » remplace l'ensemble des issues par les seules issues de A.
:::

::: exemple Les clients du magasin
1. On connaît p(F) = 120/200 = 0,6, car 120 clients sur 200 ont la carte.
2. On connaît p(A ∩ F) = 56/200 = 0,28, car 56 clients ont la carte et ont acheté.
3. Donc p(A/F) = 0,28/0,6 = 7/15 ≈ 0,467, par la définition.
4. Contrôle par le nouveau monde : parmi les 120 détenteurs de la carte, 56 ont acheté, et 56/120 = 7/15 ✓.
5. Pour comparaison, p(A) = 70/200 = 0,35 : savoir que le client a la carte fait monter la probabilité d'achat.

:::

::: piege Retourner le « sachant » ou garder l'intersection
On répond p(F/A) = 56/70 = 0,8, ou bien p(A ∩ F) = 0,28, pour la question « sachant la carte, quelle probabilité d'achat ? ». Cela tente car les trois nombres 56, 70 et 120 sont sous les yeux. Mais p(A/F) et p(F/A) répondent à deux questions différentes : le dénominateur est le nombre de l'événement qu'on **sait** réalisé, ici 120, d'où 56/120 ≈ 0,467.
:::

::: propriete
- Le dénominateur est toujours la probabilité de l'événement donné comme connu : p(B/A) se divise par p(A), p(A/B) par p(B).
- On a toujours 0 ≤ p(B/A) ≤ 1, et p(B/A) = 1 quand A est contenu dans B.

Cas limite : si A et B sont incompatibles, p(A ∩ B) = 0 donc p(B/A) = 0 : savoir A réalisé exclut B, et p(A ∪ B) = p(A) + p(B).
:::

::: verifie
Dans un lycée de 400 élèves, 250 apprennent l'allemand (événement G), et parmi eux 100 participent au club théâtre (événement T). On choisit un élève qui apprend l'allemand : quelle est la probabilité qu'il fasse du théâtre ?

---

Le « sachant G » restreint le monde aux 250 germanistes, car le dénominateur est l'événement connu. Sur ces 250, 100 font du théâtre : 100/250 = 0,4. Par la définition, p(T ∩ G) = 100/400 = 0,25 et p(G) = 250/400 = 0,625, d'où 0,25/0,625 = 0,4 ✓.
:::

::: retenir
p(B/A) = p(A ∩ B)/p(A) : on divise par la probabilité de l'événement que l'on sait réalisé, et p(B/A) ≠ p(A/B) en général.
:::

## 🌳 Probabilités composées et arbre pondéré

Une agence de voyage reçoit 35 % de ses réservations en ligne (événement E) ; parmi les réservations en ligne, 10 % sont annulées (événement N). Elle veut la probabilité qu'une réservation soit à la fois en ligne et annulée.
Comment retrouver une intersection quand on connaît une probabilité et une probabilité conditionnelle ?

::: definition
**Probabilités composées** : pour deux événements, p(A ∩ B) = p(A) × p(B/A), c'est la définition de p(B/A) multipliée par p(A). Pour n événements,
$$ p(A₁ ∩ A₂ ∩ … ∩ Aₙ) = p(A₁) × p(A₂/A₁) × p(A₃/A₁ ∩ A₂) × … × p(Aₙ/A₁ ∩ … ∩ Aₙ₋₁) $$
Dans un **arbre pondéré**, chaque branche porte une probabilité conditionnelle, la somme des branches issues d'un même nœud vaut 1, et la probabilité d'un chemin est le produit des probabilités de ses branches.
:::

::: figure L'arbre de l'agence : deux nœuds, quatre chemins, et la probabilité de chaque chemin inscrite à droite ; en additionnant les quatre feuilles on retrouve 1
<svg viewBox="0 0 340 240">
<title>Arbre pondéré : réservation en ligne (0,35) ou en agence (0,65), puis annulée ou maintenue, avec les quatre probabilités de chemins</title>
<line x1="26" y1="120" x2="120" y2="62" stroke="#0f172a" stroke-width="1.6"/>
<line x1="26" y1="120" x2="120" y2="178" stroke="#0f172a" stroke-width="1.6"/>
<line x1="120" y1="62" x2="206" y2="30" stroke="#0f172a" stroke-width="1.6"/>
<line x1="120" y1="62" x2="206" y2="94" stroke="#0f172a" stroke-width="1.6"/>
<line x1="120" y1="178" x2="206" y2="146" stroke="#0f172a" stroke-width="1.6"/>
<line x1="120" y1="178" x2="206" y2="210" stroke="#0f172a" stroke-width="1.6"/>
<circle cx="26" cy="120" r="4" fill="#0f172a"/>
<circle cx="120" cy="62" r="4" fill="#0f172a"/>
<circle cx="120" cy="178" r="4" fill="#0f172a"/>
<circle cx="206" cy="30" r="4" fill="#0f172a"/>
<circle cx="206" cy="94" r="4" fill="#0f172a"/>
<circle cx="206" cy="146" r="4" fill="#0f172a"/>
<circle cx="206" cy="210" r="4" fill="#0f172a"/>
<text x="56" y="82" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0,35</text>
<text x="56" y="168" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0,65</text>
<text x="113" y="50" text-anchor="end" font-size="13" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">E</text>
<text x="113" y="198" text-anchor="end" font-size="13" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">Ē</text>
<text x="150" y="38" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0,10</text>
<text x="150" y="96" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0,90</text>
<text x="150" y="146" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0,04</text>
<text x="150" y="208" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0,96</text>
<text x="216" y="34" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">E ∩ N : 0,035</text>
<text x="216" y="98" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">E ∩ N̄ : 0,315</text>
<text x="216" y="150" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">Ē ∩ N : 0,026</text>
<text x="216" y="214" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">Ē ∩ N̄ : 0,624</text>
</svg>
:::

Sur la figure, les nombres 0,35 et 0,65 sont p(E) et p(Ē), et les nombres 0,10, 0,90, 0,04 et 0,96 sont des probabilités conditionnelles, de la forme p(N/E) ou p(N/Ē).

::: exemple Les réservations de l'agence
1. Le chemin E puis N porte 0,35 puis 0,10, car la branche de droite est p(N/E).
2. On multiplie : p(E ∩ N) = 0,35 × 0,10 = 0,035, par la formule des composées.
3. De même p(Ē ∩ N) = 0,65 × 0,04 = 0,026 ; les deux autres feuilles valent 0,315 et 0,624.
4. Contrôle : 0,035 + 0,315 + 0,026 + 0,624 = 1 ✓, car les quatre chemins épuisent toutes les issues.
5. Avec n événements, tirons sans remise 3 boules d'un sac de 5 rouges et 3 bleues : p(R₁ ∩ R₂ ∩ R₃) = 5/8 × 4/7 × 3/6 = 60/336 = 5/28. À chaque tirage, une boule rouge et une boule de moins : c'est le « sachant » qui change la composition du sac.

:::

::: piege Multiplier sans conditionner
Pour deux boules rouges tirées sans remise du même sac, on écrit p(R₁ ∩ R₂) = 5/8 × 5/8 = 25/64. Cela tente car la formule des indépendants est celle qu'on a le plus souvent utilisée. Mais sans remise, le deuxième tirage dépend du premier : il faut la probabilité conditionnelle 4/7, d'où 5/8 × 4/7 = 5/14.
:::

::: propriete
- La somme des probabilités des branches d'un même nœud vaut 1 ; une probabilité de chemin est un produit.
- Une probabilité de branche non initiale est toujours conditionnelle à tout le chemin qui y mène.

Cas limite : si p(A₁) = 0, tout le chemin a une probabilité nulle, quel que soit le reste du produit.
:::

::: verifie
Une boîte de 6 stylos contient 2 stylos secs. On en prend deux successivement, sans remise : quelle est la probabilité que les deux soient secs ?

---

Au premier tirage, 2 secs sur 6 : p = 2/6. Sachant un sec déjà sorti, il reste 1 sec sur 5 stylos : p = 1/5. Par les composées, 2/6 × 1/5 = 2/30 = 1/15.
:::

::: retenir
p(A ∩ B) = p(A) × p(B/A) ; sur un arbre pondéré on multiplie le long d'un chemin, la somme des branches d'un nœud vaut 1.
:::

## 🔗 Événements indépendants

Dans une entreprise de 120 salariés, 48 sont des femmes (événement F), 30 travaillent à temps partiel (événement T), et 12 sont des femmes à temps partiel.
Le fait d'être une femme change-t-il la chance d'être à temps partiel ?

::: definition
Deux événements A et B sont **indépendants** si et seulement si
$$ p(A ∩ B) = p(A) × p(B) $$
Si p(A) ≠ 0 et p(B) ≠ 0, cela revient à p(B/A) = p(B), ou encore à p(A/B) = p(A) : savoir l'un ne change pas la probabilité de l'autre.
:::

::: exemple Les salariés à temps partiel
1. On calcule p(F) = 48/120 = 0,4 et p(T) = 30/120 = 0,25.
2. On calcule p(F ∩ T) = 12/120 = 0,1.
3. On compare : p(F) × p(T) = 0,4 × 0,25 = 0,1 = p(F ∩ T), donc F et T sont indépendants, par la définition.
4. Contrôle : p(T/F) = 12/48 = 0,25 = p(T) ✓ : parmi les femmes, la part du temps partiel est celle de toute l'entreprise.

:::

::: piege Confondre indépendants et incompatibles
On se dit « être une femme et être à temps partiel ne s'influencent pas », donc p(F ∩ T) = 0. Cela tente car « sans influence » et « sans rapport » semblent proches de « sans point commun ». Mais des événements incompatibles n'ont aucune issue commune : p(A ∩ B) = 0, alors que des indépendants se produisent ensemble avec la probabilité p(A) × p(B), ici 0,1.
:::

::: propriete
- Pour tester l'indépendance, on compare p(A ∩ B) au produit p(A) × p(B) ; si les deux nombres diffèrent, les événements ne sont pas indépendants.
- Deux événements incompatibles, de probabilités non nulles, ne sont jamais indépendants : p(A ∩ B) = 0 alors que p(A) × p(B) > 0.

Cas limite : un événement de probabilité nulle est indépendant de tout autre événement, puisque les deux membres de l'égalité valent 0.
:::

::: verifie
Deux événements A et B vérifient p(A) = 0,5, p(B) = 0,3 et p(A ∪ B) = 0,65. Sont-ils indépendants ?

---

On retrouve d'abord l'intersection par p(A ∪ B) = p(A) + p(B) − p(A ∩ B), donc p(A ∩ B) = 0,5 + 0,3 − 0,65 = 0,15. Or p(A) × p(B) = 0,5 × 0,3 = 0,15 : l'égalité est vraie, donc A et B sont indépendants.
:::

::: retenir
A et B sont indépendants si p(A ∩ B) = p(A) × p(B) ; indépendants et incompatibles sont deux notions différentes, et même opposées quand les probabilités sont non nulles.
:::

## 🧮 La formule des probabilités totales

Une usine fabrique ses pneus sur trois chaînes : la chaîne 1 produit 50 % des pneus, la chaîne 2 en produit 30 % et la chaîne 3 en produit 20 %. Les taux de défaut sont de 2 %, 3 % et 5 % respectivement.
Quelle est la probabilité qu'un pneu pris au hasard soit défectueux ?

::: definition
Des événements A₁, A₂, …, Aₙ forment une **partition** s'ils sont deux à deux incompatibles, de probabilités non nulles, et de réunion égale à l'ensemble des issues. Alors, pour tout événement B,
$$ p(B) = p(B/A₁) × p(A₁) + p(B/A₂) × p(A₂) + … + p(B/Aₙ) × p(Aₙ) $$
Chaque terme est la probabilité d'un chemin de l'arbre qui aboutit à B.
:::

::: exemple Les pneus défectueux
1. Les chaînes 1, 2 et 3 forment une partition, car chaque pneu vient d'une seule chaîne et d'au moins une.
2. Chemin par la chaîne 1 : 0,50 × 0,02 = 0,010, c'est p(D/A₁) × p(A₁).
3. Chemin par la chaîne 2 : 0,30 × 0,03 = 0,009 ; chemin par la chaîne 3 : 0,20 × 0,05 = 0,010.
4. On additionne les trois chemins qui aboutissent à D : p(D) = 0,010 + 0,009 + 0,010 = 0,029, soit 2,9 %.

:::

::: piege Faire la moyenne simple des taux
On calcule (2 + 3 + 5)/3 ≈ 3,33 %. Cela tente car trois taux se résument naturellement par leur moyenne. Mais les chaînes ne produisent pas le même nombre de pneus : il faut pondérer chaque taux par la part de la chaîne, ce qui donne 2,9 % et non 3,33 %.
:::

::: propriete
- La probabilité totale est une moyenne des taux conditionnels pondérée par les probabilités de la partition.
- Les poids p(A₁), …, p(Aₙ) doivent sommer à 1 ; sinon la famille n'est pas une partition.

Cas limite : si tous les taux p(B/Aᵢ) sont égaux à un même nombre t, alors p(B) = t, quels que soient les poids.
:::

::: verifie
Un atelier reçoit 70 % de ses pièces de la machine X et 30 % de la machine Y ; les taux de défaut sont de 1 % pour X et 4 % pour Y. Quelle est la probabilité qu'une pièce soit défectueuse ?

---

X et Y forment une partition, car chaque pièce vient d'une seule machine. Les deux chemins qui aboutissent au défaut valent 0,70 × 0,01 = 0,007 et 0,30 × 0,04 = 0,012. On les additionne : 0,007 + 0,012 = 0,019.
:::

::: retenir
p(B) = Σ p(B/Aᵢ) × p(Aᵢ) pour une partition (Aᵢ) : on additionne les chemins de l'arbre qui mènent à B, chaque taux étant pondéré.
:::

## 🔁 La formule de Bayes

Une banque classe 10 % de ses dossiers de crédit comme « à risque » (événement R). Son logiciel déclenche une alerte (événement S) pour 80 % des dossiers à risque et pour 10 % des dossiers sans risque.
Quand une alerte se déclenche, quelle est la probabilité que le dossier soit réellement à risque ?

::: definition
Si 0 < p(A) < 1 et p(B) ≠ 0, la **formule de Bayes** retrouve la cause à partir de l'effet :
$$ p(A/B) = p(A) × p(B/A) / [ p(A) × p(B/A) + p(Ā) × p(B/Ā) ] $$
Le dénominateur est p(B) par les probabilités totales avec la partition A, Ā.
:::

::: exemple Les dossiers à risque
1. Alerte et risque : p(R ∩ S) = 0,10 × 0,80 = 0,08, par les composées.
2. Alerte sans risque : p(R̄ ∩ S) = 0,90 × 0,10 = 0,09, car 90 % des dossiers sont sans risque.
3. Alerte au total : p(S) = 0,08 + 0,09 = 0,17, par les probabilités totales.
4. Donc p(R/S) = 0,08/0,17 = 8/17 ≈ 0,471, par la définition d'une probabilité conditionnelle.
5. Contrôle : sur 1 000 dossiers, 170 alertes dont 80 à risque, et 80/170 ≈ 0,471 ✓.

:::

::: piege Prendre p(S/R) pour p(R/S)
On annonce « le logiciel a raison dans 80 % des cas, donc un dossier alerté est à risque avec la probabilité 0,8 ». Cela tente car 0,8 est le seul grand nombre de l'énoncé. Mais 0,8 est p(S/R), la chance qu'un dossier à risque déclenche l'alerte ; la question porte sur l'autre sens, p(R/S) ≈ 0,471, qui tient compte des fausses alertes (0,09 sur 0,17).
:::

::: propriete
- La formule de Bayes inverse un conditionnement : de p(B/A) on passe à p(A/B), en divisant par p(B).
- Le résultat dépend de la probabilité de départ p(A) : une cause rare produit beaucoup de fausses alertes.

Cas limite : si p(B/Ā) = 0 (aucune fausse alerte), alors p(A/B) = 1.
:::

::: verifie
Une chaîne de montage classe 20 % de ses lots comme douteux (événement R) ; un contrôle les signale (événement S) dans 90 % des lots douteux et dans 15 % des autres. Un lot est signalé : quelle est la probabilité qu'il soit douteux ?

---

Les deux chemins qui aboutissent au signalement valent p(R ∩ S) = 0,20 × 0,90 = 0,18 et p(R̄ ∩ S) = 0,80 × 0,15 = 0,12, donc p(S) = 0,30. Par Bayes, p(R/S) = 0,18/0,30 = 0,6, soit 60 %.
:::

::: retenir
p(A/B) = p(A) × p(B/A) / p(B), avec p(B) calculé par les probabilités totales ; p(B/A) et p(A/B) sont deux nombres distincts.
:::

## 🎲 Variable aléatoire, loi et espérance

Un forain vend 100 billets de tombola à 1 DT. Un billet gagne 50 DT, quatre billets gagnent 10 DT chacun et les 95 autres ne gagnent rien. Un joueur achète un billet.
En moyenne, gagne-t-il ou perd-il de l'argent à chaque billet ?

::: definition
Une **variable aléatoire** X sur l'ensemble des issues est une application qui associe à chaque issue un nombre réel. Sa **loi de probabilité** est la donnée des valeurs xᵢ et des probabilités pᵢ = p(X = xᵢ), avec p₁ + … + pₙ = 1. Son **espérance** est
$$ E(X) = x₁p₁ + x₂p₂ + … + xₙpₙ $$
c'est la moyenne des valeurs pondérées par leurs probabilités. Pour un gain algébrique, le jeu est **équitable** si E(X) = 0, **favorable** si E(X) > 0 et **défavorable** si E(X) < 0.
:::

::: exemple La tombola du forain
1. Le gain algébrique X est la somme reçue moins la mise de 1 DT : X vaut 49 (billet à 50 DT), 9 (billet à 10 DT) ou −1 (billet perdant).
2. Les probabilités sont 1/100 = 0,01, 4/100 = 0,04 et 95/100 = 0,95, de somme 1 ✓.
3. Alors E(X) = 49 × 0,01 + 9 × 0,04 + (−1) × 0,95 = 0,49 + 0,36 − 0,95 = −0,10.
4. Conclusion : E(X) < 0, le jeu est défavorable ; le joueur perd en moyenne 0,10 DT par billet.

:::

::: piege Oublier la mise dans le gain
On calcule E = 50 × 0,01 + 10 × 0,04 = 0,90 et on conclut que le joueur gagne 0,90 DT en moyenne. Cela tente car les montants affichés sont ceux des lots. Mais 0,90 est l'espérance de la somme reçue, avant de payer son billet : le gain algébrique soustrait la mise, d'où −0,10.
:::

::: propriete
- La loi d'une variable aléatoire se lit dans un tableau (xᵢ ; pᵢ) dont la ligne des probabilités somme à 1.
- L'espérance se calcule sur les valeurs de X, pas sur les issues : les issues de même valeur se regroupent.

Cas limite : l'espérance n'est pas forcément une valeur prise par X ; ici −0,10 n'est ni 49, ni 9, ni −1.
:::

::: verifie
On mise 2 DT sur un dé équilibré : si le 6 sort, on reçoit 9 DT, sinon on ne reçoit rien. Le jeu est-il équitable, favorable ou défavorable ?

---

Le gain algébrique vaut 9 − 2 = 7 avec la probabilité 1/6, et −2 avec la probabilité 5/6. Donc E(X) = 7/6 − 10/6 = −1/2 = −0,5. Comme E(X) < 0, le jeu est défavorable.
:::

::: retenir
E(X) = Σ xᵢpᵢ ; pour un gain algébrique on soustrait la mise, et le signe de E(X) décide : équitable à 0, favorable au-dessus, défavorable au-dessous.
:::

## 📏 Variance et écart type

Un traiteur compte, chaque soir, le nombre X de commandes spéciales qu'il reçoit : 0, 1, 2 ou 3 avec les probabilités 0,1 ; 0,3 ; 0,4 et 0,2.
La moyenne dit où se situe X ; comment mesurer de combien X s'en écarte d'ordinaire ?

::: definition
La **variance** de X, d'espérance E(X), est la moyenne pondérée des carrés des écarts à l'espérance :
$$ V(X) = (x₁ − E(X))²p₁ + … + (xₙ − E(X))²pₙ = E(X²) − [E(X)]² $$
où E(X²) = x₁²p₁ + … + xₙ²pₙ. L'**écart type** est σ(X) = √V(X).
:::

::: exemple Les commandes du traiteur
1. L'espérance vaut E(X) = 0 × 0,1 + 1 × 0,3 + 2 × 0,4 + 3 × 0,2 = 1,7 commande.
2. On calcule E(X²) = 0 × 0,1 + 1 × 0,3 + 4 × 0,4 + 9 × 0,2 = 3,7, car on met les valeurs au carré avant de pondérer.
3. Alors V(X) = 3,7 − 1,7² = 3,7 − 2,89 = 0,81, par la forme développée.
4. Donc σ(X) = √0,81 = 0,9 commande.
5. Contrôle par la définition : 0,289 + 0,147 + 0,036 + 0,338 = 0,81 ✓.

:::

::: piege Oublier la racine ou le carré de la moyenne
On annonce σ(X) = 0,81, ou V(X) = 3,7. Cela tente car 0,81 est le nombre qu'on vient d'obtenir et 3,7 est « le calcul des carrés ». Mais σ est la racine de V, et E(X²) doit être diminué de [E(X)]² : l'écart type vaut 0,9, dans la même unité que X.
:::

::: propriete
- V(X) ≥ 0 toujours ; V(X) = 0 seulement si X prend une seule valeur.
- Si X est en dinars, V(X) est en dinars au carré et σ(X) en dinars, comme les valeurs de X : on commente σ, pas V.

Cas limite : V(X) = E(X²) − [E(X)]² ne peut être négatif ; un résultat négatif signale une erreur de calcul.
:::

::: verifie
Une variable X prend la valeur 0 avec la probabilité 0,8 et la valeur 10 avec la probabilité 0,2. Calculer V(X) et σ(X).

---

E(X) = 10 × 0,2 = 2 et E(X²) = 100 × 0,2 = 20. Alors V(X) = 20 − 2² = 16, et σ(X) = √16 = 4, dans la même unité que X.
:::

::: retenir
V(X) = E(X²) − [E(X)]² ≥ 0 et σ(X) = √V(X) : l'écart type mesure la dispersion dans l'unité de X.
:::

## 📞 Schéma de Bernoulli et loi binomiale

Un centre d'appels de Tunis contacte 6 clients ; chaque appel aboutit à une vente avec la probabilité 0,2, indépendamment des autres.
Quelle est la probabilité d'obtenir exactement 2 ventes, et combien de ventes peut-on attendre en moyenne ?

::: definition
Une **épreuve de Bernoulli** est une expérience à deux issues : succès S de probabilité p, échec de probabilité q = 1 − p. Répéter n fois, de façon identique et indépendante, une épreuve de Bernoulli forme un **schéma de Bernoulli**. Le nombre X de succès suit alors la **loi binomiale** de paramètres (n ; p) :
$$ p(X = k) = C(n ; k) × pᵏ × qⁿ⁻ᵏ, pour k = 0, 1, …, n $$
On admet E(X) = n × p et V(X) = n × p × q.
:::

::: exemple Les appels du centre
1. Un appel est une épreuve de Bernoulli avec p = 0,2 et q = 0,8 ; six appels indépendants forment un schéma, donc X suit la loi binomiale de paramètres (6 ; 0,2).
2. Pour k = 2 : C(6 ; 2) = 15 chemins comportent deux succès, chacun de probabilité 0,2² × 0,8⁴.
3. Donc p(X = 2) = 15 × 0,04 × 0,4096 = 0,24576 ≈ 0,246.
4. L'événement « au moins une vente » est le contraire de « aucune vente » : p(X ≥ 1) = 1 − 0,8⁶ = 1 − 0,262144 ≈ 0,738.
5. Enfin E(X) = 6 × 0,2 = 1,2 vente et V(X) = 6 × 0,2 × 0,8 = 0,96, d'où σ(X) ≈ 0,98.

:::

::: piege Oublier le nombre de chemins
On calcule p(X = 2) = 0,2² × 0,8⁴ = 0,016384 ≈ 0,016. Cela tente car la probabilité d'un chemin se lit directement sur l'arbre. Mais ce nombre est celui d'**un seul** ordre des succès, par exemple S, S, E, E, E, E ; les 15 ordres possibles sont tous acceptables, d'où le facteur C(6 ; 2) = 15 et le résultat 0,246.
:::

::: propriete
- Pour appliquer la loi binomiale, on vérifie trois points : deux issues, probabilité p constante, épreuves indépendantes.
- Pour une probabilité « au moins un », on passe au contraire : p(X ≥ 1) = 1 − qⁿ ; pour que cette quantité dépasse un seuil s, on résout qⁿ ≤ 1 − s avec ln.
- Un test de contrôle accepte souvent un nombre de succès situé dans l'intervalle [E(X) − 2σ(X) ; E(X) + 2σ(X)] ; dans le centre d'appels, [1,2 − 1,96 ; 1,2 + 1,96] accepte de 0 à 3 ventes.

Cas limite : pour n = 1, la loi binomiale est la loi de Bernoulli : p(X = 1) = p et p(X = 0) = q.
:::

::: verifie
Un technicien contrôle 5 pièces indépendantes, chacune acceptée avec la probabilité 0,4. Quelle est la probabilité que 3 exactement soient acceptées ?

---

X suit la loi binomiale de paramètres (5 ; 0,4), car les pièces sont indépendantes avec une probabilité constante. On a C(5 ; 3) = 10, donc p(X = 3) = 10 × 0,4³ × 0,6² = 10 × 0,064 × 0,36 = 0,2304.
:::

::: retenir
Pour n épreuves de Bernoulli identiques et indépendantes, p(X = k) = C(n ; k) pᵏ qⁿ⁻ᵏ, E(X) = np et V(X) = npq.
:::

> 🏆 Tu sais conditionner, pondérer un arbre, inverser une alerte avec Bayes, juger un jeu par son espérance et modéliser des répétitions par la loi binomiale. Prochaine étape : les graphes, qui modélisent des réseaux de décision.
