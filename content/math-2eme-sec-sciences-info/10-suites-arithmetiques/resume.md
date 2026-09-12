# 📜 Résumé : Suites arithmétiques

- **Notion de suite** : à tout entier naturel n ≥ n₀ on associe un réel unique, noté **Uₙ** et appelé **terme général** ; la suite se note **(Uₙ)ₙ≥ₙ₀** ou **(Uₙ)**. L'entier n est l'**indice** (le rang) ; Uₙ est le terme. Exemple : Uₙ = (3n + 1)/4 donne U₀ = 1/4, U₁ = 1, U₅ = 4.
- **Deux modes de présentation** : par le **terme général** (une formule qui donne Uₙ à partir de n, donc un accès direct) ou par le **premier terme et une relation de récurrence** (chaque terme se déduit du précédent, donc marche par marche). Exemple : Uₙ = 4n + 1 et « U₀ = 1 et Uₙ₊₁ = Uₙ + 4 » décrivent la même suite.
- **Définition** : (Uₙ) est **arithmétique** s'il existe un réel r tel que **Uₙ₊₁ = Uₙ + r** pour tout entier naturel n ; r est la **raison**. Des termes consécutifs d'une telle suite sont dits **en progression arithmétique**.
- **Méthode de reconnaissance** : calculer **Uₙ₊₁ − Uₙ** littéralement et vérifier que le résultat **ne dépend pas de n**. Uₙ = n/5 − 4 donne 1/5 (arithmétique, r = 1/5) ; Uₙ = n² donne 2n + 1 (non arithmétique).
- **Terme général** : **Uₙ = U₀ + nr**, plus généralement **Uₙ = Uₚ + (n − p)r**, et **Uₙ = U₁ + (n − 1)r** si la suite commence au rang 1. C'est le nombre de **pas** qui multiplie r : de U₀ à U₇ il y a sept pas. Lue à l'envers, la formule donne **r = (Uₙ − Uₚ)/(n − p)** : avec U₀ = 8 et U₇ = −13, r = −21/7 = −3.
- **Représentation graphique** : les points **Aₙ(n ; Uₙ)** sont **alignés** sur la droite de **pente r** et d'**ordonnée à l'origine U₀**, d'équation y = rx + U₀. Réciproquement, des points Aₙ situés sur y = −2x + 9 donnent r = −2, U₀ = 9 et Uₙ = 9 − 2n.

::: figure Une suite arithmétique se lit d'un coup d'œil sur un graphique : les points Aₙ(n ; Uₙ) sont alignés, la droite part de U₀ sur l'axe des ordonnées et monte de r chaque fois que l'abscisse avance de 1
<svg viewBox="0 0 220 160">
<path d="M25 130 L200 130 M40 142 L40 18" fill="none" stroke="#0f172a" stroke-width="1.8"/>
<polygon points="195,126 205,130 195,134" fill="#0f172a"/>
<polygon points="36,23 40,13 44,23" fill="#0f172a"/>
<path d="M30 124.4 L165 24.1" fill="none" stroke="#0f6e56" stroke-width="1.8"/>
<g fill="none" stroke="#0f172a" stroke-width="1.4" stroke-dasharray="4 3"><path d="M75 91 L110 91 L110 65"/></g>
<g fill="#0f6e56"><circle cx="40" cy="117" r="4"/><circle cx="75" cy="91" r="4"/><circle cx="110" cy="65" r="4"/><circle cx="145" cy="39" r="4"/></g>
<g font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">
<text x="28" y="121" text-anchor="end">U₀</text>
<text x="118" y="84" text-anchor="start">r</text>
<g text-anchor="middle">
<text x="75" y="144">1</text><text x="110" y="144">2</text><text x="145" y="144">3</text><text x="192" y="122">n</text>
</g>
</g>
</svg>
:::

- **Somme de termes consécutifs** : **S = n × (a + b)/2**, où n est le **nombre de termes**, a le premier et b le dernier — soit « nombre de termes × (premier + dernier)/2 ». Cas de base : **1 + 2 + … + n = n(n + 1)/2**.
- **Compter les termes, le piège du chapitre** : de U₀ à Uₙ il y a **n + 1** termes, de Uₚ à Uₙ il y en a **n − p + 1**. Ainsi U₄₅ + … + U₃₈₁ compte 337 termes, et avec U₀ = 3 et r = 2, la somme U₅ + … + U₅₀ vaut 46 × (13 + 103)/2 = **2668**.
- **Moyenne arithmétique** : si a, b et c sont trois termes consécutifs, alors **b = (a + c)/2**. Exemple : dans 7 ; x ; 19, on a x = 26/2 = 13.
- **Sommes remarquables** : **1 + 3 + 5 + … + (2n − 1) = n²** ; la somme de toutes les cases d'une table de multiplication de 1 à n vaut (1 + 2 + … + n)² ; identité d'**Al Karagi** : 1³ + 2³ + … + n³ = (1 + 2 + … + n)². Et deux suites **non** arithmétiques à connaître de nom : la suite de **Syracuse** (5, 16, 8, 4, 2, 1) et la suite de **Robinson** (1, 11, 21, 1211, 111221).
