# 🎓 Le choix d'investissement — flux, VAN et délai de récupération

> 💡 « Un dinar d'aujourd'hui vaut plus qu'un dinar de demain : on compare les projets à la même date. »

La Savonnerie Jlassi, à Sousse, hésite : acheter une chaudière neuve coûte cher, et les gains n'arriveront que dans les années à venir. Comment savoir si le jeu en vaut la chandelle ? Ce chapitre donne huit repères : ce qu'est un investissement et quand il est rentable, les flux nets de trésorerie, l'actualisation, la valeur actualisée nette (VAN), le calcul de la VAN avec cash-flow constant, la valeur résiduelle, le délai de récupération à cash-flow constant, puis à cash-flow variable, enfin les critères de rejet et de sélection.

Les entreprises et les chiffres de ce chapitre sont des valeurs choisies pour s'entraîner, pas des données réelles. Les montants sont en dinars (D). Les décimales s'écrivent avec une virgule.

## 🏗️ Investir : un pari sur des recettes futures

La Savonnerie Jlassi paie la chaudière aujourd'hui, mais ses économies de combustible s'étaleront sur plusieurs années. Que risque-t-elle ?
Comment sait-on qu'un projet vaut la dépense ?

::: definition
Un **investissement** consiste à employer un capital dans une opération dont l'entreprise attend un profit sur plusieurs années. Il engage des capitaux importants pour une longue durée. On investit pour **accroître la capacité de production**, **améliorer la productivité** ou **renouveler les équipements**.

L'entreprise échange une dépense **certaine** (en partie immédiate) contre des recettes **espérées**, donc futures : c'est à la fois un pari et un risque.

Le projet entraîne aussi de nouvelles dépenses (matières premières, frais commerciaux). Il est **rentable** si les recettes futures, une fois ces nouvelles dépenses déduites, dépassent le coût initial. Cela ne suffit pourtant pas : il faut comparer les sommes à une même date (voir l'actualisation).

Dans les exercices, le coût initial retenu est le prix d'acquisition hors taxe, augmenté des frais d'installation hors taxe.
:::

::: exemple La chaudière de la Savonnerie Jlassi
Valeurs d'illustration : chaudière à 80 000 D hors taxe, installation à 4 000 D hors taxe ; elle ferait économiser 30 000 D par an pendant 3 ans, déduction faite des nouvelles dépenses.

1. Coût initial : 80 000 + 4 000 = 84 000 D, payé tout de suite et avec certitude.
2. Gains espérés : 30 000 × 3 = 90 000 D, étalés sur 3 ans.
3. 90 000 est supérieur à 84 000, mais l'écart est mince et les gains sont lointains : on ne peut pas conclure sans actualiser. Si la machine tombait en panne dès l'année 2, le pari serait perdu.
:::

::: piege Conclure à la rentabilité parce que les recettes dépassent le coût
On écrit « 90 000 D de gains contre 84 000 D de coût : le projet est rentable ». Cela tente parce que 90 000 est plus grand que 84 000. Mais les gains arrivent après la dépense, et un dinar reçu dans trois ans vaut moins qu'un dinar versé aujourd'hui : il faut les actualiser avant de comparer.
:::

::: verifie
Une conserverie de Bizerte étudie une ligne de mise en boîte à 150 000 D. Les recettes futures, nouvelles dépenses déduites, totalisent 170 000 D sur 6 ans. Peut-elle déjà dire que le projet est rentable ?

---

Non. 170 000 est supérieur à 150 000, mais ces recettes sont étalées sur six ans : il faut les actualiser à la date de l'achat avant de comparer avec les 150 000 D versés tout de suite.
:::

::: retenir
Investir, c'est échanger une dépense certaine contre des recettes futures espérées. Pour être rentable, un projet doit rapporter plus que son coût, nouvelles dépenses déduites et sommes comparées à la même date.
:::

## 💵 Les flux nets de trésorerie d'exploitation (la CAF du projet)

La chaudière fait économiser du combustible, mais elle s'use et l'État prélève l'impôt sur le gain. Quel argent entre réellement dans la caisse chaque année ?
Pourquoi le résultat comptable ne répond-il pas à la question ?

::: definition
Les **flux nets de trésorerie d'exploitation** (ou **cash-flows**, ou **capacité d'autofinancement**, CAF, du projet) sont les ressources réellement créées chaque année par l'investissement. La CAF a été vue au chapitre précédent : ici, on la calcule pour le seul projet. Ils se calculent par ce tableau :

- Augmentation du chiffre d'affaires
- − Dépenses supplémentaires d'exploitation (charges décaissables)
- − Dotations aux amortissements
- = **Résultat avant impôts**
- − Impôt supplémentaire (taux sur les bénéfices, 30 % dans nos exemples)
- = **Résultat net d'impôts**
- + Dotations aux amortissements
- = **Flux net de trésorerie** (CAF)

L'amortissement linéaire répartit le coût en parts égales : dotation = coût initial ÷ durée de vie. La dotation réduit le résultat, donc l'impôt, mais ne fait sortir aucun argent : on l'ajoute à la fin. Une dotation plus élevée réduit encore l'impôt : le flux net gagne alors (dotation en plus) × (taux d'impôt).
:::

::: exemple Les flux de la Verrerie Kamoun
Valeurs d'illustration : four de 120 000 D, durée de vie 4 ans, amortissement linéaire ; chiffre d'affaires supplémentaire de 100 000 D par an ; dépenses supplémentaires de 45 % du chiffre d'affaires ; impôt de 30 %.

1. Dotation annuelle : 120 000 ÷ 4 = 30 000 D.
2. Dépenses supplémentaires : 100 000 × 0,45 = 45 000 D. Résultat avant impôts : 100 000 − 45 000 − 30 000 = 25 000 D.
3. Impôt : 25 000 × 0,30 = 7 500 D. Résultat net d'impôts : 25 000 − 7 500 = 17 500 D.
4. Flux net : 17 500 + 30 000 = 47 500 D par an.
:::

::: piege Prendre le résultat net comme flux de trésorerie
On écrit « la Verrerie gagne 17 500 D par an ». Cela tente parce que 17 500 D est le résultat net, la dernière ligne qu'on calcule avec soin. Mais la dotation de 30 000 D a été retranchée sans aucun décaissement : le flux réel est 17 500 + 30 000 = 47 500 D.
:::

::: verifie
Une cartonnerie de Gabès investit 60 000 D (amortissement linéaire sur 5 ans). Chiffre d'affaires supplémentaire : 80 000 D par an ; dépenses supplémentaires : 40 000 D ; impôt de 30 %. Quel est le flux net annuel ?

---

Dotation : 60 000 ÷ 5 = 12 000 D. Résultat avant impôts : 80 000 − 40 000 − 12 000 = 28 000 D. Impôt : 8 400 D. Résultat net : 19 600 D. Flux net : 19 600 + 12 000 = 31 600 D.
:::

::: retenir
Flux net = résultat net d'impôts + dotations aux amortissements. On calcule l'impôt sur le résultat avant impôts, après avoir retranché les dotations.
:::

## ⏳ L'actualisation : ramener l'avenir à aujourd'hui

La Savonnerie Jlassi recevra 10 000 D dans trois ans. Vaut-il autant que 10 000 D en caisse aujourd'hui ?
Comment comparer deux sommes qui ne sont pas à la même date ?

::: definition
**Actualiser** une somme future, c'est calculer ce qu'elle vaut aujourd'hui, à la date de l'investissement (date 0). On utilise le **taux d'actualisation** i, choisi par l'entreprise, et la durée n en années :

valeur actuelle = somme × (1 + i)⁻ⁿ

Le coefficient (1 + i)⁻ⁿ est inférieur à 1 : plus la somme est lointaine, plus elle perd de valeur. Ce calcul permet de comparer des flux de dates différentes.
:::

::: exemple Actualiser deux sommes de la Savonnerie Jlassi
Valeurs d'illustration : taux d'actualisation de 10 %.

1. 10 000 D reçus dans 1 an valent 10 000 × 1,10⁻¹ = 9 090,91 D aujourd'hui.
2. 10 000 D reçus dans 3 ans valent 10 000 × 1,10⁻³ = 7 513,15 D aujourd'hui.
3. La somme lointaine est la plus dépréciée : on ne les additionne qu'une fois ramenées à la même date.
:::

::: piege Additionner des flux de dates différentes
On écrit « 10 000 + 10 000 + 10 000 = 30 000 D de gains ». Cela tente parce que le total paraît simple et plus grand que le coût. Mais ces trois sommes tombent à des dates différentes : on ne peut les additionner qu'après avoir actualisé chacune à la date 0.
:::

::: verifie
À 8 %, que vaut aujourd'hui une somme de 20 000 D reçue dans 2 ans ?

---

20 000 × 1,08⁻² = 20 000 × 0,857339 = 17 146,78 D.
:::

::: retenir
Actualiser, c'est multiplier par (1 + i)⁻ⁿ. Une somme future vaut moins qu'aujourd'hui, et d'autant moins qu'elle est lointaine.
:::

## 📊 La valeur actualisée nette (VAN)

Pour un four, on connaît le coût et les flux de chacune des trois années. Comment les résumer en un seul chiffre ?
Quel signe dit si le projet crée de la valeur ?

::: definition
La **valeur actualisée nette** (VAN) est la valeur totale créée par l'investissement, évaluée à la date de l'investissement :

VAN = flux net 1 × (1 + i)⁻¹ + flux net 2 × (1 + i)⁻² + … + flux net p × (1 + i)⁻ᵖ + valeur résiduelle × (1 + i)⁻ᵖ − I₀

i est le taux d'actualisation, I₀ l'investissement initial et p la durée du projet.

**Règle** : si la VAN est positive, les flux actualisés dépassent la dépense, l'investissement est jugé rentable. Si elle est négative, il ne l'est pas. Si elle est nulle, les flux actualisés couvrent juste la dépense : le projet rapporte exactement le taux d'actualisation, c'est la limite entre un projet rentable et un projet non rentable. Entre deux projets, on retient en principe la VAN la plus élevée.
:::

::: exemple La VAN du four de la Briqueterie Jlassi
Valeurs d'illustration : I₀ = 150 000 D ; flux nets de 60 000, 70 000 et 80 000 D sur 3 ans ; taux de 10 % ; pas de valeur résiduelle.

1. Année 1 : 60 000 × 1,10⁻¹ = 54 545,45 D.
2. Année 2 : 70 000 × 1,10⁻² = 57 851,24 D. Année 3 : 80 000 × 1,10⁻³ = 60 105,19 D.
3. Somme des flux actualisés : 172 501,88 D.
4. VAN = 172 501,88 − 150 000 = 22 501,88 D. Elle est positive : le projet est rentable.
:::

::: piege Oublier de retrancher le coût initial
On écrit « la VAN est 172 501,88 D ». Cela tente parce que c'est le résultat de la longue somme. Mais ce total est la valeur des flux ; la VAN est la valeur créée : il faut encore retrancher les 150 000 D dépensés.
:::

::: verifie
Un projet coûte 100 000 D. Ses flux actualisés totalisent 96 400 D. Quelle est la VAN, et que décide-t-on ?

---

VAN = 96 400 − 100 000 = −3 600 D. Elle est négative : le projet n'est pas rentable à ce taux.
:::

::: retenir
VAN = somme des flux actualisés (valeur résiduelle comprise) − I₀. Positive : rentable. Négative : non rentable.
:::

## 🧮 Une VAN plus rapide quand le flux est constant

Si la machine rapportait chaque année exactement la même somme pendant cinq ans, faudrait-il actualiser cinq fois ?
Existe-t-il un raccourci ?

::: definition
Quand le flux net est le même chaque année, sur p années, on met le flux en facteur :

flux actualisés = flux × [1 − (1 + i)⁻ᵖ] ÷ i

Le quotient [1 − (1 + i)⁻ᵖ] ÷ i est le coefficient d'actualisation d'une série de flux constants (il est donné par les tables financières). Alors VAN = flux × coefficient − I₀.
:::

::: exemple La VAN à flux constant de la Biscuiterie Mrad
Valeurs d'illustration : I₀ = 140 000 D ; flux net de 40 000 D pendant 5 ans ; taux de 10 %.

1. Coefficient : [1 − 1,10⁻⁵] ÷ 0,10 = 3,790787.
2. Flux actualisés : 40 000 × 3,790787 = 151 631,47 D.
3. VAN = 151 631,47 − 140 000 = 11 631,47 D : le projet est rentable.
:::

::: piege Appliquer le coefficient à des flux qui changent
On écrit « 55 000 × coefficient » alors que les flux valent 50 000 puis 60 000 puis 55 000. Cela tente parce que la moyenne paraît juste. Mais le raccourci ne vaut que si tous les flux sont égaux : sinon on actualise année par année.
:::

::: verifie
Un projet de 80 000 D donne 25 000 D par an pendant 4 ans, à 10 %. Le coefficient vaut 3,169865. Quelle est la VAN ?

---

Flux actualisés : 25 000 × 3,169865 = 79 246,63 D. VAN = 79 246,63 − 80 000 = −753,37 D : projet non rentable à ce taux.
:::

::: retenir
À flux constant : VAN = flux × [1 − (1 + i)⁻ᵖ] ÷ i − I₀. Si les flux diffèrent d'une année à l'autre, on actualise chacun séparément.
:::

## 🏷️ La valeur résiduelle : la revente en fin de projet

Après quelques années, la chaudière sera revendue. À quel prix ? Cette somme compte-t-elle dans le projet ?
Sur quelle base fixe-t-on ce prix quand le bien n'est pas totalement amorti ?

::: definition
La **valeur résiduelle** est la somme que rapporte le bien à la fin de la durée du projet. Dans les exercices de ce chapitre, elle est égale à la **valeur comptable nette** (VCN) :

VCN = coût initial − amortissements déjà pratiqués

Elle s'ajoute au dernier flux (année p) et s'actualise avec lui. On ne tient pas compte de l'impôt sur le résultat de la cession.

Attention : la durée de vie du bien (période d'amortissement) peut dépasser la durée du projet.
:::

::: exemple La revente d'une presse de la Menuiserie Triki
Valeurs d'illustration : presse de 100 000 D, amortie linéairement sur 10 ans, utilisée 6 ans puis revendue à sa VCN ; taux de 10 %.

1. Dotation annuelle : 100 000 ÷ 10 = 10 000 D.
2. Amortissements pratiqués en 6 ans : 6 × 10 000 = 60 000 D.
3. VCN = valeur résiduelle = 100 000 − 60 000 = 40 000 D.
4. Elle s'actualise à la date 6 : 40 000 × 1,10⁻⁶ = 22 578,96 D, à ajouter aux flux actualisés.
:::

::: piege Prendre le coût initial ou zéro comme valeur de revente
On écrit « la presse vaut encore 100 000 D » ou « elle ne vaut plus rien ». Cela tente parce que ce sont les deux nombres qu'on a sous les yeux. Mais ici la revente se fait à la VCN : coût initial moins les amortissements déjà pratiqués, soit 40 000 D.
:::

::: verifie
Un tour coûte 90 000 D, amorti linéairement sur 9 ans ; il est revendu à sa VCN après 4 ans. Quelle est la valeur résiduelle ?

---

Dotation : 90 000 ÷ 9 = 10 000 D. Amortissements pratiqués : 4 × 10 000 = 40 000 D. VCN : 90 000 − 40 000 = 50 000 D.
:::

::: retenir
Valeur résiduelle = VCN = coût initial − amortissements déjà pratiqués. Elle s'ajoute au dernier flux et s'actualise avec lui.
:::

## ⏱️ Le délai de récupération à cash-flow constant

Un banquier demande : « Dans combien de temps aurez-vous récupéré votre mise ? » Faut-il pour cela actualiser ?
Comment répondre quand les flux sont égaux ?

::: definition
Le **délai de récupération du capital investi** (DRCI) est le temps nécessaire pour récupérer les fonds investis, **sans actualisation** : on cherche quand les flux nets cumulés couvrent le coût.

Si le cash-flow est constant :

DRCI = coût de l'investissement ÷ cash-flow constant

Le résultat est en années ; la partie décimale se convertit en mois en la multipliant par 12.
:::

::: exemple Deux ateliers du même quartier
Valeurs d'illustration : l'Atelier Sfar investit 240 000 D pour un flux annuel constant de 50 000 D ; l'Atelier Bouzid investit 210 000 D pour 60 000 D par an.

1. Atelier Sfar : 240 000 ÷ 50 000 = 4,8 ans, soit 4 ans et 0,8 × 12 = 9,6 mois (environ 4 ans et 10 mois).
2. Atelier Bouzid : 210 000 ÷ 60 000 = 3,5 ans, soit 3 ans et 6 mois.
3. Le délai de Bouzid est plus court : son capital est récupéré plus vite.
:::

::: piege Actualiser les flux pour calculer le délai
On écrit « 210 000 ÷ (60 000 × 1,10⁻¹) ». Cela tente parce qu'on vient d'apprendre à actualiser. Mais le DRCI se calcule sans actualisation : on divise simplement le coût par le flux annuel.
:::

::: verifie
Un projet de 180 000 D rapporte 45 000 D par an, de façon constante. Quel est le délai de récupération ?

---

180 000 ÷ 45 000 = 4 ans.
:::

::: retenir
À cash-flow constant : DRCI = coût ÷ cash-flow, sans actualisation. La partie décimale × 12 donne les mois.
:::

## 📅 Le délai de récupération à cash-flow variable

Si les flux changent d'une année à l'autre, la division ne marche plus. Comment trouver à quel moment le total atteint le coût ?
Que fait-on quand le coût est atteint au milieu d'une année ?

::: definition
On calcule les **flux cumulés** année après année. On repère P tel que le cumul de l'année P soit inférieur au coût I₀, et le cumul de l'année P + 1 supérieur ou égal à I₀. Alors :

DRCI = P ans + (I₀ − cumul de P) × 360 ÷ flux de l'année (P + 1)

La fraction d'année est comptée en jours, sur une année de 360 jours.
:::

::: exemple Un projet à flux variables de la Fonderie Gharbi
Valeurs d'illustration : I₀ = 100 000 D ; flux de 30 000, 35 000, 25 000 et 40 000 D pendant 4 ans.

1. Cumuls : 30 000 ; 65 000 ; 90 000 ; 130 000.
2. Le coût est dépassé entre les années 3 et 4 : P = 3, cumul de P = 90 000 D, flux de l'année 4 = 40 000 D.
3. Jours : (100 000 − 90 000) × 360 ÷ 40 000 = 90 jours.
4. DRCI = 3 ans et 90 jours, soit 3 ans et 3 mois environ.
:::

::: piege Diviser le coût par le dernier flux ou par le flux moyen
On écrit « 100 000 ÷ 40 000 = 2,5 ans ». Cela tente parce que la division est rapide. Mais les flux ne sont pas constants : les premières années rapportent moins. Il faut cumuler les flux année par année.
:::

::: verifie
I₀ = 80 000 D ; flux annuels : 20 000, 30 000, 25 000, 35 000 D. Quel est le délai de récupération ?

---

Cumuls : 20 000 ; 50 000 ; 75 000 ; 110 000. P = 3, cumul de P = 75 000 D. Jours : (80 000 − 75 000) × 360 ÷ 35 000 = 51,43. DRCI = 3 ans et environ 51 jours.
:::

::: retenir
À cash-flow variable : DRCI = P ans + (I₀ − cumul de P) × 360 ÷ flux de l'année (P + 1), où P est la dernière année avant que le cumul ne couvre le coût.
:::

## ⚖️ Décider : rejeter, sélectionner

La Laiterie Ben Ali compare deux machines : l'une se rembourse vite, l'autre rapporte davantage. Laquelle choisir ?
Un même projet peut-il plaire à un critère et déplaire à l'autre ?

::: definition
Le DRCI est :

- un **critère de rejet** : on rejette tout projet dont le délai dépasse la **norme fixée par l'entreprise** ;
- un **critère de sélection** : entre plusieurs projets, on préfère le délai le plus court (le moins risqué).

La VAN, elle, retient la VAN positive (rentabilité) et la plus élevée entre deux projets. Les deux critères ne mesurent pas la même chose : le DRCI ignore l'actualisation et les flux qui suivent la récupération, la VAN prend en compte toute la durée. Ils peuvent donc conduire à des choix différents.
:::

::: exemple Deux critères, deux choix pour la Laiterie Ben Ali
Valeurs d'illustration : norme de l'entreprise : 3 ans. Projet X : coût 100 000 D, flux constant de 40 000 D pendant 5 ans. Projet Y : coût 100 000 D, flux constant de 45 000 D pendant 3 ans.

1. DRCI de X : 100 000 ÷ 40 000 = 2,5 ans ; DRCI de Y : 100 000 ÷ 45 000 = 2,22 ans. Les deux respectent la norme ; Y est le plus court.
2. VAN à 10 % : X : 40 000 × 3,790787 − 100 000 = 51 631,48 D ; Y : 45 000 × 2,486852 − 100 000 = 11 908,34 D.
3. Le DRCI préfère Y (plus rapide), la VAN préfère X (plus de valeur créée). Le choix dépend de l'objectif : sécurité ou création de valeur.
:::

::: piege Croire que le délai le plus court donne toujours le projet le plus rentable
On écrit « Y se récupère plus vite, donc Y est le meilleur ». Cela tente parce que récupérer vite rassure. Mais le délai ne mesure que la vitesse de récupération : X rapporte encore des flux en années 4 et 5, que Y n'a pas et que le délai ne voit pas.
:::

::: verifie
La norme est de 3 ans. Un projet a un DRCI de 3 ans et 8 mois. Que décide-t-on, selon ce seul critère ?

---

Le délai dépasse la norme : le projet est rejeté (critère de rejet).
:::

::: retenir
DRCI : rejet si le délai dépasse la norme, sélection du délai le plus court. VAN : positive, la plus élevée. Les deux critères peuvent diverger.
:::
