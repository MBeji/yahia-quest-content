# ⚔️ Probabilités — dompter le hasard, de l'urne à la courbe

> 💡 «Le hasard ne se prévoit pas, il se mesure : un nombre entre 0 et 1 pour un événement, une loi pour une variable, une aire pour une durée.»

Ce chapitre apprend à mesurer le hasard, puis à le résumer par une moyenne et un écart. Huit notions : l'espace probabilisé fini, la probabilité conditionnelle et l'indépendance, l'arbre pondéré avec les formules des probabilités totales et de Bayes, la variable aléatoire et sa loi, l'espérance et la variance, le schéma de Bernoulli et la loi binomiale, les variables continues avec la loi uniforme, la loi exponentielle. Les nombres Cₙᵏ et Aₙᵏ du dénombrement sont supposés connus ; le calcul intégral des chapitres précédents sert pour les densités.

## 🎲 Espace probabilisé fini : la définition et ses règles

Un dé truqué sort le numéro k avec une chance proportionnelle à k : le 6 est six fois plus probable que le 1. Les faces ne sont plus équiprobables, et l'on veut pourtant la probabilité de « obtenir un résultat pair ».
Quelles règles minimales un nombre p(A) doit-il respecter pour être une probabilité, et comment calculer avec elles ?

::: definition
Soit Ω l'ensemble fini des issues d'une expérience aléatoire (l'**univers**) et 𝒫(Ω) l'ensemble de ses parties. Une **probabilité** sur Ω est une application p de 𝒫(Ω) dans [0 ; 1] telle que :
- p(Ω) = 1 ;
- p(A ∪ B) = p(A) + p(B) pour tous événements A et B tels que A ∩ B = ∅.

Le triplet (Ω, 𝒫(Ω), p) est un **espace probabilisé fini**.
:::

::: definition
**Vocabulaire.** Toute partie de Ω est un **événement** ; un singleton est un événement **élémentaire** ; Ω est l'événement **certain** et ∅ l'événement **impossible**. A ∩ B se lit « A et B », A ∪ B se lit « A ou B ». Deux événements sont **incompatibles** si A ∩ B = ∅ ; ils sont **contraires** si A ∪ B = Ω et A ∩ B = ∅, et l'on note A̅ le contraire de A.
:::

::: exemple Le dé truqué
1. Posons p({k}) = c × k pour k de 1 à 6. Les événements élémentaires sont incompatibles deux à deux et leur réunion est Ω, donc p(Ω) = 1 donne c × (1 + 2 + … + 6) = 21c = 1, soit c = 1/21.
2. Soit A « le résultat est pair » = {2 ; 4 ; 6}. Par additivité, p(A) = (2 + 4 + 6)/21 = 12/21 = 4/7.
3. Le contraire de A est {1 ; 3 ; 5} : p(A̅) = 1 − 4/7 = 3/7, et l'on vérifie (1 + 3 + 5)/21 = 9/21 = 3/7 ✓.
4. Soit B « au moins 5 » = {5 ; 6}, avec p(B) = 11/21 et A ∩ B = {6} de probabilité 6/21. Alors p(A ∪ B) = 12/21 + 11/21 − 6/21 = 17/21 ✓, car {2 ; 4 ; 5 ; 6} donne bien (2 + 4 + 5 + 6)/21.

:::

::: piege
**Erreur : additionner p(A) + p(B) quand les événements se chevauchent.** Ici 12/21 + 11/21 = 23/21, un nombre supérieur à 1 : impossible pour une probabilité. Le résultat 6 est compté dans A et dans B ; on retranche p(A ∩ B).
:::

::: propriete
Dans un espace probabilisé fini :
- p(∅) = 0 et p(A̅) = 1 − p(A) ;
- p(A ∪ B) = p(A) + p(B) − p(A ∩ B), et p(A ∪ B) = p(A) + p(B) si A et B sont incompatibles ;
- si A ⊂ B, alors p(A) ≤ p(B) ;
- si les événements élémentaires sont **équiprobables**, p(A) = card A / card Ω.

Cas limite : l'équiprobabilité est une hypothèse, pas une règle. Pour le dé truqué, p(A) ≠ 3/6.
:::

::: verifie À toi : les puces
Dans un lot de 50 puces, 7 ont un défaut de gravure, 5 un défaut de soudure et 2 les deux. On prend une puce au hasard, chaque puce ayant la même chance. Quelle est la probabilité qu'elle n'ait aucun défaut ?

---

Les puces sont équiprobables. Celles qui ont au moins un défaut sont 7 + 5 − 2 = 10, car les 2 puces à deux défauts sont comptées deux fois : p(au moins un défaut) = 10/50 = 1/5. Le contraire donne p(aucun défaut) = 1 − 1/5 = 4/5.
:::

::: retenir
Une probabilité vaut 1 sur Ω et s'additionne sur les événements incompatibles ; on en déduit p(A̅) = 1 − p(A) et p(A ∪ B) = p(A) + p(B) − p(A ∩ B).
:::

## 🔍 Probabilité conditionnelle et indépendance

Une salle machine compte 50 clés USB : 30 de marque A et 20 de marque B. Parmi elles, 3 de marque A et 4 de marque B sont défectueuses. On prend une clé au hasard.
Elle est défectueuse : quelle est la chance qu'elle soit de marque A ? Savoir qu'elle est défectueuse change-t-il les chances ?

::: definition
Soit B un événement tel que p(B) ≠ 0. La **probabilité conditionnelle de A sachant B**, notée p(A/B) ou p_B(A), est le réel
$$ p(A/B) = p(A ∩ B) / p(B) $$
:::

| Clés | Marque A | Marque B | Total |
| --- | --- | --- | --- |
| Défectueuses | 3 | 4 | 7 |
| En état | 27 | 16 | 43 |
| Total | 30 | 20 | 50 |

La ligne « défectueuses » est le nouvel univers : 7 clés, dont 3 de marque A. C'est ce que calcule le quotient p(A ∩ D)/p(D) du tableau.

::: exemple Les clés défectueuses
1. Notons A « marque A » et D « défectueuse » : p(D) = 7/50 et p(A ∩ D) = 3/50.
2. On divise par la probabilité de ce que l'on sait : p(A/D) = (3/50)/(7/50) = 3/7.
3. Dans l'autre sens, p(D/A) = (3/50)/(30/50) = 3/30 = 1/10 : une clé de marque A sur dix est défectueuse.
4. Contrôle : p(A) × p(D/A) = 0,6 × 0,1 = 0,06 = 3/50 = p(A ∩ D) ✓, on retrouve l'intersection en multipliant p(A) par p(D/A).

:::

::: piege
**Erreur : confondre p(A/D) et p(D/A).** Les deux ont le même numérateur p(A ∩ D) mais pas le même dénominateur : ici 3/7 ≈ 0,43 contre 1/10. L'événement placé après « sachant que » est celui par lequel on divise.
:::

::: propriete
Si p(A) ≠ 0 et p(B) ≠ 0 : p(A ∩ B) = p(A) × p(B/A) = p(B) × p(A/B). Si p(B) ≠ 0 : p(A̅/B) = 1 − p(A/B).

Cas limite : si p(B) = 0, le quotient n'existe pas et p(A/B) n'est pas défini.
:::

Dans l'exemple, être de marque A rend-il la clé plus fragile ? On compare p(D/A) = 0,1 à p(D) = 7/50 = 0,14 : ce n'est pas pareil.

::: definition
Deux événements A et B sont **indépendants** si p(A ∩ B) = p(A) × p(B). Si p(B) ≠ 0, c'est équivalent à p(A/B) = p(A) : savoir que B est réalisé ne change pas la probabilité de A.
:::

::: exemple Marque et défaut
1. p(A) × p(D) = 0,6 × 0,14 = 0,084, alors que p(A ∩ D) = 0,06.
2. Les deux nombres diffèrent : A et D ne sont pas indépendants, la marque influence la probabilité d'être défectueux.

:::

::: piege
**Erreur : prendre « incompatibles » pour « indépendants ».** Si A ∩ B = ∅ avec p(A) et p(B) non nuls, alors p(A ∩ B) = 0 est différent de p(A) × p(B) : deux événements incompatibles de probabilités non nulles sont au contraire dépendants.
:::

::: verifie À toi : indépendants ou non ?
On donne p(A) = 0,5 ; p(B) = 0,2 et p(A ∩ B) = 0,1. A et B sont-ils indépendants ? Calculer p(A/B).

---

p(A) × p(B) = 0,5 × 0,2 = 0,1 = p(A ∩ B) : les événements sont indépendants. On le retrouve avec la conditionnelle : p(A/B) = p(A ∩ B)/p(B) = 0,1/0,2 = 0,5 = p(A).
:::

::: retenir
p(A/B) = p(A ∩ B)/p(B) : on divise par la probabilité de ce que l'on sait ; A et B sont indépendants si p(A ∩ B) = p(A) × p(B), ce qui ne veut pas dire incompatibles.
:::

## 🌳 Arbre pondéré, probabilités totales et formule de Bayes

Une messagerie analyse ses pièces jointes : 60 % sont des documents, 30 % des images et 10 % des exécutables. Le filtre lève une alerte pour 1 % des documents, 2 % des images et 20 % des exécutables.
Quelle part des pièces jointes déclenche une alerte ? Et quand une alerte retentit, quelle est la chance que ce soit un exécutable ?

::: definition
Des événements A₁, …, Aₙ forment une **partition** de Ω s'ils sont non vides, deux à deux incompatibles, et de réunion Ω. Dans un **arbre pondéré**, on multiplie les probabilités le long d'un chemin, et les branches issues d'un même nœud ont une somme égale à 1.
:::

::: figure Trois types de fichiers, puis l'alerte E : on multiplie le long d'un chemin, et les trois produits en face de E s'additionnent pour donner p(E)
<svg viewBox="0 0 380 250">
<title>Arbre pondéré : trois types de fichiers A₁, A₂, A₃ de probabilités 0,6 ; 0,3 ; 0,1, puis E avec 0,01 ; 0,02 ; 0,2</title>
<path d="M20 125 L120 40" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round"/>
<path d="M20 125 L120 125" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round"/>
<path d="M20 125 L120 210" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round"/>
<circle cx="20" cy="125" r="5" fill="#0f172a" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="120" cy="40" r="5" fill="#0f172a" stroke="#0f172a" stroke-width="1.2"/>
<text x="58" y="75.5" text-anchor="middle" font-size="12" fill="#0f6e56" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0,6</text>
<text x="120" y="28" text-anchor="middle" font-size="13" fill="#0f172a" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">A₁</text>
<path d="M120 40 L250 20" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round"/>
<circle cx="250" cy="20" r="4" fill="#0f172a" stroke="#0f172a" stroke-width="1.2"/>
<text x="185" y="24.0" text-anchor="middle" font-size="12" fill="#0f6e56" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0,01</text>
<text x="262" y="24" text-anchor="start" font-size="13" fill="#0f172a" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">E</text>
<path d="M120 40 L250 60" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round"/>
<circle cx="250" cy="60" r="4" fill="#0f172a" stroke="#0f172a" stroke-width="1.2"/>
<text x="185" y="62.0" text-anchor="middle" font-size="12" fill="#0f6e56" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0,99</text>
<text x="262" y="64" text-anchor="start" font-size="13" fill="#0f172a" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">E̅</text>
<text x="300" y="24" text-anchor="start" font-size="12" fill="#b45309" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0,006</text>
<circle cx="120" cy="125" r="5" fill="#0f172a" stroke="#0f172a" stroke-width="1.2"/>
<text x="58" y="118.0" text-anchor="middle" font-size="12" fill="#0f6e56" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0,3</text>
<text x="120" y="113" text-anchor="middle" font-size="13" fill="#0f172a" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">A₂</text>
<path d="M120 125 L250 105" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round"/>
<circle cx="250" cy="105" r="4" fill="#0f172a" stroke="#0f172a" stroke-width="1.2"/>
<text x="185" y="109.0" text-anchor="middle" font-size="12" fill="#0f6e56" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0,02</text>
<text x="262" y="109" text-anchor="start" font-size="13" fill="#0f172a" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">E</text>
<path d="M120 125 L250 145" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round"/>
<circle cx="250" cy="145" r="4" fill="#0f172a" stroke="#0f172a" stroke-width="1.2"/>
<text x="185" y="147.0" text-anchor="middle" font-size="12" fill="#0f6e56" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0,98</text>
<text x="262" y="149" text-anchor="start" font-size="13" fill="#0f172a" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">E̅</text>
<text x="300" y="109" text-anchor="start" font-size="12" fill="#b45309" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0,006</text>
<circle cx="120" cy="210" r="5" fill="#0f172a" stroke="#0f172a" stroke-width="1.2"/>
<text x="58" y="181.5" text-anchor="middle" font-size="12" fill="#0f6e56" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0,1</text>
<text x="120" y="198" text-anchor="middle" font-size="13" fill="#0f172a" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">A₃</text>
<path d="M120 210 L250 190" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round"/>
<circle cx="250" cy="190" r="4" fill="#0f172a" stroke="#0f172a" stroke-width="1.2"/>
<text x="185" y="194.0" text-anchor="middle" font-size="12" fill="#0f6e56" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0,2</text>
<text x="262" y="194" text-anchor="start" font-size="13" fill="#0f172a" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">E</text>
<path d="M120 210 L250 230" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round"/>
<circle cx="250" cy="230" r="4" fill="#0f172a" stroke="#0f172a" stroke-width="1.2"/>
<text x="185" y="232.0" text-anchor="middle" font-size="12" fill="#0f6e56" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0,8</text>
<text x="262" y="234" text-anchor="start" font-size="13" fill="#0f172a" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">E̅</text>
<text x="300" y="194" text-anchor="start" font-size="12" fill="#b45309" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0,02</text>
</svg>
:::

Sur la figure, A₁, A₂, A₃ sont les documents, les images et les exécutables, et E l'alerte ; le nombre à droite de E est la probabilité du chemin, par exemple p(A₃ ∩ E) = 0,1 × 0,2 = 0,02.

::: exemple Les pièces jointes
1. Les trois chemins qui aboutissent à E sont disjoints : p(E) = 0,6 × 0,01 + 0,3 × 0,02 + 0,1 × 0,2 = 0,006 + 0,006 + 0,02 = 0,032.
2. On cherche p(A₃/E) = p(A₃ ∩ E)/p(E) : le chemin A₃ → E, divisé par la probabilité de E.
3. p(A₃/E) = 0,02/0,032 = 5/8 = 0,625 : plus d'une alerte sur deux vient d'un exécutable, alors que les exécutables ne sont que 10 % des fichiers.

:::

::: piege
**Erreur : prendre p(E/A₃) = 0,2 pour p(A₃/E).** Le taux 0,2 répond à « parmi les exécutables, combien déclenchent l'alerte ? », la question posée est « parmi les alertes, combien viennent d'exécutables ? » : 0,625. Autre erreur, moyenner les taux sans les pondérer : (1 + 2 + 20)/3 ≈ 7,7 % au lieu de 3,2 %.
:::

::: propriete
Soit A₁, …, Aₙ une partition de Ω et E un événement de probabilité non nulle.
- **Probabilités totales** : p(E) = p(E/A₁) p(A₁) + … + p(E/Aₙ) p(Aₙ). Avec n = 2, p(E) = p(E/A) p(A) + p(E/A̅) p(A̅).
- **Bayes** : pour tout k, p(Aₖ/E) = p(E/Aₖ) p(Aₖ) / [p(E/A₁) p(A₁) + … + p(E/Aₙ) p(Aₙ)].

Bayes remonte de l'effet à la cause : on connaît p(E/Aₖ), on cherche p(Aₖ/E).
:::

::: verifie À toi : la cause d'une alerte
Avec le même filtre, quelle est la probabilité qu'une alerte provienne d'un document ?

---

p(A₁/E) = p(A₁ ∩ E)/p(E) = (0,6 × 0,01)/0,032 = 0,006/0,032 = 3/16 = 0,1875. Le dénominateur est le p(E) des probabilités totales, le numérateur est le chemin qui passe par A₁.
:::

::: retenir
p(E) additionne les chemins qui aboutissent à E, chacun pondéré par sa branche ; la formule de Bayes divise le chemin voulu par p(E) pour passer de p(E/Aₖ) à p(Aₖ/E).
:::

## 📊 Variable aléatoire discrète : loi et fonction de répartition

On lance deux fois un dé tétraédrique (quatre faces numérotées de 1 à 4) et l'on note X le plus grand des deux numéros. Les 16 couples sont équiprobables.
Quelles valeurs X peut-elle prendre, avec quelles probabilités ? Et quelle est la chance que X soit au plus égal à 3 ?

::: definition
Une **variable aléatoire** X sur Ω est une application de Ω dans ℝ. Si X(Ω) = {x₁ ; … ; xₙ}, on note p(X = xᵢ) la probabilité que X prenne la valeur xᵢ. La **loi de probabilité** de X est l'application P_X qui à xᵢ associe p(X = xᵢ) ; la somme de ces probabilités vaut 1.
La **fonction de répartition** de X est la fonction F définie sur ℝ par F(x) = p(X ≤ x).
:::

| xᵢ | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- |
| p(X = xᵢ) | 1/16 | 3/16 | 5/16 | 7/16 |

Le tableau est la loi de X : X = k regroupe les couples dont le maximum est k, soit 2k − 1 couples (1, 3, 5, 7). Leur total fait bien 16.

::: figure La fonction F monte par paliers : elle saute de p(X = k) en chaque valeur k de X, et vaut 1 à partir de 4
<svg viewBox="0 0 340 230">
<title>Fonction de répartition F en escalier : 0 avant 1, puis 1/16, 1/4, 9/16 et 1 à partir de 4</title>
<path d="M40 190 L330 190" fill="none" stroke="#0f172a" stroke-width="1.8" stroke-linecap="round"/>
<path d="M50 200 L50 30" fill="none" stroke="#0f172a" stroke-width="1.8" stroke-linecap="round"/>
<text x="330" y="208" text-anchor="end" font-size="13" fill="#0f172a" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">x</text>
<text x="36" y="34" text-anchor="end" font-size="12" fill="#0f172a" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">F(x)</text>
<path d="M50 190 L105 190" fill="none" stroke="#0f6e56" stroke-width="3" stroke-linecap="round"/>
<path d="M105 180.6 L160 180.6" fill="none" stroke="#0f6e56" stroke-width="3" stroke-linecap="round"/>
<path d="M160 152.5 L215 152.5" fill="none" stroke="#0f6e56" stroke-width="3" stroke-linecap="round"/>
<path d="M215 105.6 L270 105.6" fill="none" stroke="#0f6e56" stroke-width="3" stroke-linecap="round"/>
<path d="M270 40 L325 40" fill="none" stroke="#0f6e56" stroke-width="3" stroke-linecap="round"/>
<circle cx="105" cy="180.6" r="4.5" fill="#0f6e56" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="160" cy="152.5" r="4.5" fill="#0f6e56" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="215" cy="105.6" r="4.5" fill="#0f6e56" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="270" cy="40" r="4.5" fill="#0f6e56" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="105" cy="190" r="4.5" fill="#ffffff" stroke="#0f172a" stroke-width="1.5"/>
<circle cx="160" cy="180.6" r="4.5" fill="#ffffff" stroke="#0f172a" stroke-width="1.5"/>
<circle cx="215" cy="152.5" r="4.5" fill="#ffffff" stroke="#0f172a" stroke-width="1.5"/>
<circle cx="270" cy="105.6" r="4.5" fill="#ffffff" stroke="#0f172a" stroke-width="1.5"/>
<path d="M105 190 L105 195" fill="none" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="105" y="210" text-anchor="middle" font-size="12" fill="#0f172a" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">1</text>
<path d="M160 190 L160 195" fill="none" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="160" y="210" text-anchor="middle" font-size="12" fill="#0f172a" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">2</text>
<path d="M215 190 L215 195" fill="none" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="215" y="210" text-anchor="middle" font-size="12" fill="#0f172a" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">3</text>
<path d="M270 190 L270 195" fill="none" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="270" y="210" text-anchor="middle" font-size="12" fill="#0f172a" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">4</text>
<path d="M46 180.6 L50 180.6" fill="none" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="42" y="184.6" text-anchor="end" font-size="12" fill="#0f172a" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">1/16</text>
<path d="M46 152.5 L50 152.5" fill="none" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="42" y="156.5" text-anchor="end" font-size="12" fill="#0f172a" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">1/4</text>
<path d="M46 105.6 L50 105.6" fill="none" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="42" y="109.6" text-anchor="end" font-size="12" fill="#0f172a" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">9/16</text>
<path d="M46 40 L50 40" fill="none" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="42" y="44" text-anchor="end" font-size="12" fill="#0f172a" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">1</text>
</svg>
:::

Sur la figure, le palier de hauteur 9/16 sur [3 ; 4[ est F(3) = 1/16 + 3/16 + 5/16 : chaque saut est une probabilité du tableau.

::: exemple Le plus grand numéro
1. p(X = 3) : les couples de maximum 3 sont (3, 1), (3, 2), (3, 3), (1, 3), (2, 3), soit 5/16.
2. F(3) = p(X ≤ 3) = 1/16 + 3/16 + 5/16 = 9/16, et l'on contrôle 1 − p(X = 4) = 1 − 7/16 = 9/16 ✓.
3. p(2 < X ≤ 4) = F(4) − F(2) = 1 − 4/16 = 3/4, ce que confirment 5/16 + 7/16 = 12/16.

:::

::: piege
**Erreur : lire p(2 ≤ X ≤ 4) comme F(4) − F(2).** F(4) − F(2) ne compte que les valeurs situées après 2 : il manque p(X = 2) = 3/16. Pour garder la valeur 2, on retranche F(1) : p(2 ≤ X ≤ 4) = 1 − 1/16 = 15/16.
:::

::: propriete
Pour une variable aléatoire X et des réels a ≤ b :
- Σ p(X = xᵢ) = 1, et p(X ≤ a) + p(X > a) = 1 ;
- p(a < X ≤ b) = F(b) − F(a) ;
- F est constante sur chaque intervalle [xᵢ ; xᵢ₊₁[, vaut 0 avant x₁ et 1 à partir de xₙ.

Cas limite : p(X < xᵢ) est F juste avant le saut, soit p(X ≤ xᵢ₋₁), et non F(xᵢ).
:::

::: verifie À toi : le plus petit numéro
Avec les mêmes deux lancers, Y est le plus petit des deux numéros. Calculer p(Y ≥ 3).

---

Y ≥ 3 signifie que les deux numéros valent 3 ou 4 : 2 × 2 = 4 couples sur 16, donc p(Y ≥ 3) = 4/16 = 1/4. Autre route : p(Y ≥ 3) = 1 − p(Y ≤ 2), le contraire.
:::

::: retenir
La loi de X liste p(X = xᵢ) avec une somme égale à 1 ; F(x) = p(X ≤ x) monte par paliers et p(a < X ≤ b) = F(b) − F(a).
:::

## 💰 Espérance, variance et écart-type

On joue au dé tétraédrique précédent : le gain en dinars est X, le plus grand des deux numéros. Combien gagne-t-on en moyenne sur un très grand nombre de parties ?
Et les gains s'écartent-ils beaucoup de cette moyenne ?

::: definition
Si X(Ω) = {x₁ ; … ; xₙ}, l'**espérance** de X est E(X) = Σ xᵢ p(X = xᵢ). La **variance** est V(X) = Σ (xᵢ − E(X))² p(X = xᵢ) et l'**écart-type** est σ(X) = √V(X).
:::

::: exemple Le jeu du plus grand numéro
1. E(X) = 1 × 1/16 + 2 × 3/16 + 3 × 5/16 + 4 × 7/16 = (1 + 6 + 15 + 28)/16 = 50/16 = 25/8 = 3,125.
2. Pour la variance, on peut passer par E(X²) = (1 + 4 × 3 + 9 × 5 + 16 × 7)/16 = 170/16 = 85/8, la même somme avec les carrés des valeurs.
3. V(X) = E(X²) − (E(X))² = 85/8 − 625/64 = 680/64 − 625/64 = 55/64.
4. σ(X) = √55/8 ≈ 0,93 dinar : l'écart typique autour de la moyenne 3,125 est d'environ 0,93 dinar.

:::

::: propriete
Pour des variables aléatoires X et Y définies sur Ω et un réel a :
- E(X + a) = E(X) + a, E(aX) = aE(X) et E(X + Y) = E(X) + E(Y) ;
- V(X) = E(X²) − (E(X))², V(X + a) = V(X) et V(aX) = a²V(X) ;
- σ(X + a) = σ(X) et σ(aX) = |a| σ(X).

Cas limite : a = 0 donne V(aX) = 0, car 0 × X est constante.
:::

::: exemple Changer de variable
1. Y = 2X − 1 : E(Y) = 2 × 25/8 − 1 = 21/4 = 5,25, car l'espérance est linéaire.
2. V(Y) = 2² × 55/64 = 55/16 : le facteur 2 est élevé au carré et le « −1 » ne change rien à la dispersion.
3. Soit M le plus petit numéro : sa loi est 7/16, 5/16, 3/16, 1/16 pour 1, 2, 3, 4 et E(M) = 30/16 = 15/8. Alors E(X + M) = 25/8 + 15/8 = 5, qui est bien l'espérance de la somme des deux numéros, 2,5 + 2,5.

:::

::: piege
**Erreur : écrire V(aX) = aV(X) ou V(X + a) = V(X) + a.** Un facteur 3 multiplie les écarts par 3, donc leurs carrés par 9 : V(3X) = 9V(X). Décaler toutes les valeurs de a ne change pas leur dispersion : V(X + a) = V(X).
:::

::: verifie À toi : un gain transformé
X a pour espérance 1 et pour variance 4. Calculer E(Z) et V(Z) pour Z = 5 − 3X.

---

E(Z) = 5 − 3 × E(X) = 5 − 3 = 2 par linéarité. Pour la variance, le « 5 » ne compte pas et le facteur −3 passe au carré : V(Z) = (−3)² × V(X) = 9 × 4 = 36, soit σ(Z) = 3σ(X) = 6.
:::

::: retenir
E(X) = Σ xᵢ p(X = xᵢ) est linéaire (E(X + Y) = E(X) + E(Y)) ; V(X) = E(X²) − (E(X))² et V(aX + b) = a²V(X).
:::

## 🔁 Schéma de Bernoulli et loi binomiale

On envoie 6 paquets de données ; chacun arrive avec la probabilité 0,9, indépendamment des autres. Soit X le nombre de paquets arrivés.
Quelle est la probabilité d'en recevoir exactement 5 ? Et d'en recevoir au moins 5 ?

::: definition
Une **épreuve de Bernoulli** a deux issues : le **succès** S, de probabilité p, et l'**échec** S̅. Un **schéma de Bernoulli** de paramètres n et p répète n fois la même épreuve, de façon indépendante. Le nombre X de succès suit la **loi binomiale** de paramètres n et p, notée ℬ(n ; p).
:::

Un chemin de l'arbre à k succès et n − k échecs a la probabilité pᵏ(1 − p)ⁿ⁻ᵏ, et il y a Cₙᵏ chemins de ce type : c'est l'origine de la formule ci-dessous.

::: exemple Les paquets envoyés
1. Les 6 envois sont identiques et indépendants, et chacun est un succès (arrivé) avec p = 0,9 : X suit ℬ(6 ; 0,9).
2. p(X = 5) = C₆⁵ × 0,9⁵ × 0,1 = 6 × 0,59049 × 0,1 = 0,354294, soit environ 0,354.
3. « Au moins 5 » veut dire 5 ou 6 : p(X = 6) = 0,9⁶ = 0,531441, donc p(X ≥ 5) = 0,354294 + 0,531441 = 0,885735 ≈ 0,886.
4. E(X) = 6 × 0,9 = 5,4 paquets et V(X) = 6 × 0,9 × 0,1 = 0,54.

:::

::: piege
**Erreur : traiter « au plus » comme « au moins ».** Pour la même loi, « au plus 4 » est p(X ≤ 4) = 1 − p(X ≥ 5) ≈ 0,114, tandis que « au moins 5 » vaut 0,886. Le contraire de « au moins 5 » est « au plus 4 », jamais « au plus 5 ». Autre faute : oublier le coefficient Cₙᵏ, qui compte les chemins.
:::

::: propriete
Si X suit ℬ(n ; p), alors (théorème admis) :
- p(X = k) = Cₙᵏ pᵏ (1 − p)ⁿ⁻ᵏ pour k de 0 à n ;
- E(X) = np et V(X) = np(1 − p).

Cas limite : si l'on tire sans remise dans une urne, la probabilité de succès change d'un tirage à l'autre, les épreuves ne sont pas indépendantes et ce n'est pas un schéma de Bernoulli.
:::

::: verifie À toi : cinq envois
Cinq envois indépendants réussissent chacun avec la probabilité 0,7. Quelle est la probabilité d'exactement 4 réussites ?

---

Le nombre de réussites suit ℬ(5 ; 0,7). p(X = 4) = C₅⁴ × 0,7⁴ × 0,3 = 5 × 0,2401 × 0,3 = 0,36015. Le facteur 5 compte les places possibles de l'unique échec.
:::

::: retenir
Pour n épreuves identiques et indépendantes : p(X = k) = Cₙᵏ pᵏ(1 − p)ⁿ⁻ᵏ, E(X) = np et V(X) = np(1 − p) ; « au moins » passe par le contraire « au plus ».
:::

## 🌊 Variable continue : densité, loi uniforme et probabilités géométriques

Un transfert de fichier se termine à un instant X, en secondes, compris entre 0 et 3, et les fins tardives sont plus probables que les précoces. X prend toutes les valeurs d'un intervalle : 1,2 s, 1,2037 s…
Quelle est la probabilité que X soit exactement 1 ? Et qu'il soit compris entre 1 et 2 ?

::: definition
Une variable aléatoire est **continue** si elle peut prendre n'importe quelle valeur d'un intervalle [a ; b]. Sa **densité de probabilité** est une fonction f positive et continue sur [a ; b] telle que
$$ ∫ₐᵇ f(x)dx = 1 $$
Pour a ≤ s ≤ t ≤ b, la probabilité p(s ≤ X ≤ t) est l'aire sous la courbe de f entre s et t :
$$ p(s ≤ X ≤ t) = ∫ₛᵗ f(x)dx $$
La fonction de répartition est F(t) = p(X ≤ t) = ∫ₐᵗ f(x)dx.
:::

::: figure La probabilité de [1 ; 2] est l'aire colorée sous la courbe de f(t) = t²/9 : 7/27, soit environ 0,26
<svg viewBox="0 0 340 250">
<title>Densité f(t) = t²/9 sur [0 ; 3] ; l'aire sous la courbe entre 1 et 2 vaut 7/27, environ 0,26</title>
<path d="M40 200 L330 200" fill="none" stroke="#0f172a" stroke-width="1.8" stroke-linecap="round"/>
<path d="M50 206 L50 30" fill="none" stroke="#0f172a" stroke-width="1.8" stroke-linecap="round"/>
<text x="330" y="218" text-anchor="end" font-size="13" fill="#0f172a" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">t</text>
<polygon points="130,200 130.0,182.2 136.7,179.1 143.3,175.8 150.0,172.2 156.7,168.4 163.3,164.3 170.0,160.0 176.7,155.4 183.3,150.6 190.0,145.6 196.7,140.2 203.3,134.7 210.0,128.9 210,200" fill="#0f6e56" fill-opacity="0.22" stroke="none"/>
<polyline points="50.0,200.0 56.7,199.9 63.3,199.5 70.0,198.9 76.7,198.0 83.3,196.9 90.0,195.6 96.7,194.0 103.3,192.1 110.0,190.0 116.7,187.7 123.3,185.1 130.0,182.2 136.7,179.1 143.3,175.8 150.0,172.2 156.7,168.4 163.3,164.3 170.0,160.0 176.7,155.4 183.3,150.6 190.0,145.6 196.7,140.2 203.3,134.7 210.0,128.9 216.7,122.8 223.3,116.5 230.0,110.0 236.7,103.2 243.3,96.2 250.0,88.9 256.7,81.4 263.3,73.6 270.0,65.6 276.7,57.3 283.3,48.8 290.0,40.0" fill="none" stroke="#0f6e56" stroke-width="3" stroke-linejoin="round"/>
<path d="M130 200 L130 182.2" fill="none" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round" stroke-dasharray="4 3"/>
<path d="M210 200 L210 128.9" fill="none" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round" stroke-dasharray="4 3"/>
<path d="M50 200 L50 205" fill="none" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="50" y="220" text-anchor="middle" font-size="12" fill="#0f172a" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0</text>
<path d="M130 200 L130 205" fill="none" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="130" y="220" text-anchor="middle" font-size="12" fill="#0f172a" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">1</text>
<path d="M210 200 L210 205" fill="none" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="210" y="220" text-anchor="middle" font-size="12" fill="#0f172a" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">2</text>
<path d="M290 200 L290 205" fill="none" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="290" y="220" text-anchor="middle" font-size="12" fill="#0f172a" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">3</text>
<path d="M46 40 L50 40" fill="none" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
<text x="42" y="44" text-anchor="end" font-size="12" fill="#0f172a" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">1</text>
<text x="170.0" y="178" text-anchor="middle" font-size="14" fill="#0f172a" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">7/27</text>
<text x="250.0" y="80.9" text-anchor="middle" font-size="15" fill="#0f6e56" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">f</text>
</svg>
:::

Sur la figure, la courbe est celle de f et la surface colorée est p(1 ≤ X ≤ 2) : une probabilité est une aire, jamais la hauteur de la courbe.

::: exemple Le transfert de fichier
1. f(t) = t²/9 est positive et continue sur [0 ; 3], avec ∫₀³ (t²/9)dt = [t³/27]₀³ = 27/27 = 1 ✓ : c'est une densité.
2. p(1 ≤ X ≤ 2) = ∫₁² (t²/9)dt = [t³/27]₁² = 8/27 − 1/27 = 7/27 ≈ 0,26.
3. p(X = 1) = ∫₁¹ (t²/9)dt = 0 : l'aire d'un segment vertical est nulle. Donc p(X < 2) = p(X ≤ 2) = F(2) = 8/27.

:::

::: piege
**Erreur : prendre la valeur f(1) pour une probabilité.** On écrirait p(X = 1) = 1/9, ce qui est faux. Une densité peut même dépasser 1 (la constante 2 sur [0 ; 1/2] est une densité) : seule l'aire est une probabilité, et p(X = a) = 0 pour une variable continue.
:::

::: definition
La **loi uniforme** sur [a ; b] est la loi continue de densité constante f = 1/(b − a). Pour s et t dans [a ; b] :
$$ p(s ≤ X ≤ t) = (t − s)/(b − a) $$
Sa fonction de répartition vaut 0 si x < a, (x − a)/(b − a) si a ≤ x < b, et 1 si x ≥ b. Un point M choisi au hasard sur un segment suit cette loi : la probabilité ne dépend que des longueurs.
:::

::: exemple Un point au hasard sur un segment
1. M est choisi au hasard sur [AB] avec AB = 10 : x = AM suit la loi uniforme sur [0 ; 10].
2. Cherchons p(AM × MB ≥ 21). Comme MB = 10 − x, la condition s'écrit x(10 − x) ≥ 21, soit x² − 10x + 21 ≤ 0, donc (x − 3)(x − 7) ≤ 0 et 3 ≤ x ≤ 7.
3. p(3 ≤ X ≤ 7) = (7 − 3)/(10 − 0) = 4/10 = 0,4.

:::

::: verifie À toi : l'attente
Un client arrive à un instant X choisi au hasard dans [0 ; 8] minutes (loi uniforme). Calculer p(X ≥ 6).

---

La densité est constante, égale à 1/(8 − 0) = 1/8. p(6 ≤ X ≤ 8) = (8 − 6)/(8 − 0) = 2/8 = 1/4 : la probabilité est la longueur de l'intervalle favorable divisée par la longueur totale.
:::

::: retenir
Une densité f est positive avec ∫ₐᵇ f(x)dx = 1 et p(s ≤ X ≤ t) = ∫ₛᵗ f(x)dx : une aire ; pour la loi uniforme, p(s ≤ X ≤ t) = (t − s)/(b − a).
:::

## ⏳ Loi exponentielle, survie et algorithme

Un site reçoit des visites, et le temps X entre deux visites consécutives, en minutes, suit la loi de densité f(x) = 0,5 e^(−0,5x) pour x ≥ 0 : les courts intervalles sont fréquents, les longs de plus en plus rares, sans borne.
Quelle est la probabilité qu'on attende au moins 3 minutes ? Et entre 1 et 4 minutes ?

::: definition
Soit λ > 0. La **loi exponentielle de paramètre λ** a pour densité f(x) = λ e^(−λx) sur [0 ; +∞[. Si X la suit, pour 0 ≤ a ≤ b :
- p(a ≤ X ≤ b) = e^(−λa) − e^(−λb) et p(X ≥ a) = e^(−λa) ;
- F(x) = 1 − e^(−λx) si x ≥ 0, et F(x) = 0 si x < 0.

:::

Ces formules viennent d'une intégrale : l'aire entre a et b est ∫ₐᵇ λe^(−λx)dx = [−e^(−λx)]ₐᵇ = e^(−λa) − e^(−λb). La **fonction de survie** S(x) = p(X > x) = e^(−λx) donne la probabilité de « durer plus de x ».

::: exemple Les visites du site
1. Ici λ = 0,5 : p(X ≥ 3) = e^(−0,5 × 3) = e^(−1,5) ≈ 0,223.
2. p(1 ≤ X ≤ 4) = e^(−0,5) − e^(−2) ≈ 0,6065 − 0,1353 = 0,471.
3. Sachant que l'on a déjà attendu 2 minutes, la probabilité d'attendre au moins 6 minutes est p(X ≥ 6/X ≥ 2) = p(X ≥ 6)/p(X ≥ 2) = e^(−3)/e^(−1) = e^(−2) ≈ 0,135, car (X ≥ 6) ⊂ (X ≥ 2) et la formule de la conditionnelle s'applique.

:::

::: piege
**Erreur : écrire p(X ≥ a) = 1 − e^(−λa).** Cette valeur est F(a), la probabilité d'attendre moins de a. Pour p(X ≥ 3) elle donne 0,777 au lieu de 0,223. Autre faute : oublier le facteur λ dans l'exposant et calculer e^(−3) ≈ 0,05.
:::

Un programme (le manuel l'écrit en Pascal) lit les bornes a et b puis calcule la probabilité de [a ; b]. En pseudo-code, pour une loi uniforme sur [A ; B] ou une loi exponentielle de paramètre λ :

```
si loi uniforme sur [A ; B] :  p ← (b − a)/(B − A)
si loi exponentielle :         p ← exp(−λ × a) − exp(−λ × b)
afficher p
```

::: exemple Tracer le programme
1. Loi exponentielle avec λ = 0,5, a = 1 et b = 4 : l'ordinateur évalue exp(−0,5) = 0,6065 puis exp(−2) = 0,1353.
2. Il affiche p = 0,6065 − 0,1353 = 0,4712, le résultat de l'exemple précédent.
3. Pour une loi uniforme sur [0 ; 10] avec a = 2 et b = 5, p = (5 − 2)/(10 − 0) = 0,3. Écrire 1/(b − a) serait une faute : c'est la hauteur de la densité, pas une probabilité.

:::

::: verifie À toi : durée de vie
La durée de vie X d'un disque, en années, suit la loi exponentielle de paramètre 0,1. Calculer p(X ≥ 5) et la probabilité qu'il tombe en panne avant 5 ans.

---

p(X ≥ 5) = e^(−0,1 × 5) = e^(−0,5) ≈ 0,607. La panne avant 5 ans est l'événement contraire, donc F(5) = 1 − e^(−0,5) ≈ 0,393 ; les deux probabilités ont pour somme 1.
:::

::: retenir
Loi exponentielle de paramètre λ : p(X ≥ a) = e^(−λa), p(a ≤ X ≤ b) = e^(−λa) − e^(−λb) et F(x) = 1 − e^(−λx) ; un programme calcule une probabilité, pas une densité.
:::

> 🏆 Treizième porte franchie, héros. Tu mesures le hasard avec une probabilité, tu conditionnes, tu remontes aux causes par Bayes, tu résumes une variable par sa loi, sa moyenne et son écart, tu comptes les succès d'un schéma de Bernoulli et tu lis une probabilité comme une aire sous une densité. Prochaine étape : la révision du programme.
