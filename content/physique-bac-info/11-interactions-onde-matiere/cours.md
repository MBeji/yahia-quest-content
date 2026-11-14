# 🌐 Les interactions onde-matière — quand l'onde rencontre un obstacle

> 💡 « Le son contourne l'angle d'un mur, la lumière projette une ombre nette : tout dépend de la taille de l'obstacle comparée à la longueur d'onde. »

Dans le chapitre précédent, une onde mécanique s'éloignait de sa source sans rien rencontrer. Ici elle rencontre une fente, un obstacle ou la surface séparant deux milieux, et la lumière subit des épreuves semblables. Dix notions te mènent de la diffraction à la dispersion : la diffraction d'une onde mécanique, la figure de diffraction de la lumière, l'onde lumineuse, le quotient λ/a, la demi-largeur angulaire θ, la réflexion d'un ébranlement, la réflexion d'une onde, la réfraction, la dispersion de la lumière et le milieu dispersif. On suppose connus λ = v·T (chapitre précédent), les lois de Descartes pour la lumière (réflexion i = i′ ; réfraction n₁ sin i₁ = n₂ sin i₂) et le fait que la lumière blanche se décompose en couleurs.

## 🕳️ La diffraction d'une onde mécanique : l'onde qui contourne

Dans une cuve à ondes, une lame vibrante de fréquence N = 16 Hz envoie des rides rectilignes de célérité 0,24 m/s sur une ouverture formée par deux plaques de plexiglas. On règle la largeur a de l'ouverture : 4,0 cm, puis 1,5 cm, puis 0,5 cm.
Que devient l'onde de l'autre côté de l'ouverture, et sa longueur d'onde change-t-elle ?

::: definition
**Diffraction** — La **diffraction** est la modification du trajet d'une onde, et donc de sa forme, au voisinage d'une fente ou d'un obstacle dont la largeur a est de l'ordre de la longueur d'onde λ. Une onde plane qui traverse l'ouverture se propage ensuite dans plusieurs directions de part et d'autre de la direction d'incidence : c'est une **onde diffractée**, qui a la même longueur d'onde que l'onde incidente.
:::

::: figure Les mêmes rides rectilignes (en vert) devant trois ouvertures : a = 4,0 cm, a = 1,5 cm et a = 0,5 cm ; I est le milieu de l'ouverture, et la flèche de la première vue donne l'écart λ = 1,5 cm entre deux rides consécutives
<svg viewBox="0 0 340 200"><title>Rides rectilignes qui traversent une ouverture de largeur a = 4,0 cm, puis 1,5 cm, puis 0,5 cm : la longueur d'onde λ = 1,5 cm reste la même de part et d'autre</title><rect x="2" y="8" width="108" height="152" fill="none" stroke="#cbd5e1" stroke-width="1"/><line x1="44" y1="10" x2="44" y2="64" stroke="#0f172a" stroke-width="4.5"/><line x1="44" y1="104" x2="44" y2="158" stroke="#0f172a" stroke-width="4.5"/><line x1="29" y1="14" x2="29" y2="154" stroke="#0f6e56" stroke-width="2"/><line x1="14" y1="14" x2="14" y2="154" stroke="#0f6e56" stroke-width="2"/><polyline points="56,56 58,61 59,67 59,101 58,107 56,112" fill="none" stroke="#0f6e56" stroke-width="2" stroke-linejoin="round"/><polyline points="71,56 73,61 74,67 74,101 73,107 71,112" fill="none" stroke="#0f6e56" stroke-width="2" stroke-linejoin="round"/><polyline points="86,56 88,61 89,67 89,101 88,107 86,112" fill="none" stroke="#0f6e56" stroke-width="2" stroke-linejoin="round"/><circle cx="44" cy="84" r="2.6" fill="#d97706" stroke="#0f172a" stroke-width="1"/><text x="56" y="178" text-anchor="middle" fill="#0f172a" font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">a = 4,0 cm</text><text x="56" y="194" text-anchor="middle" fill="#0f6e56" font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">≈ 2,7 λ</text><rect x="115" y="8" width="108" height="152" fill="none" stroke="#cbd5e1" stroke-width="1"/><line x1="157" y1="10" x2="157" y2="76.5" stroke="#0f172a" stroke-width="4.5"/><line x1="157" y1="91.5" x2="157" y2="158" stroke="#0f172a" stroke-width="4.5"/><line x1="142" y1="14" x2="142" y2="154" stroke="#0f6e56" stroke-width="2"/><line x1="127" y1="14" x2="127" y2="154" stroke="#0f6e56" stroke-width="2"/><polyline points="168.15,73.96 168.66,74.56 169.14,75.18 169.58,75.83 169.99,76.5 170.37,77.19 170.7,77.9 171,78.62 171.27,79.36 171.49,80.12 171.67,80.88 171.82,81.65 171.92,82.43 171.98,83.21 172,84 171.98,84.79 171.92,85.57 171.82,86.35 171.67,87.12 171.49,87.88 171.27,88.64 171,89.38 170.7,90.1 170.37,90.81 169.99,91.5 169.58,92.17 169.14,92.82 168.66,93.44 168.15,94.04" fill="none" stroke="#0f6e56" stroke-width="2" stroke-linejoin="round"/><polyline points="179.29,63.93 180.31,65.12 181.27,66.37 182.16,67.66 182.98,69 183.73,70.38 184.41,71.8 185.01,73.25 185.53,74.73 185.98,76.24 186.34,77.76 186.63,79.31 186.84,80.86 186.96,82.43 187,84 186.96,85.57 186.84,87.14 186.63,88.69 186.34,90.24 185.98,91.76 185.53,93.27 185.01,94.75 184.41,96.2 183.73,97.62 182.98,99 182.16,100.34 181.27,101.63 180.31,102.88 179.29,104.07" fill="none" stroke="#0f6e56" stroke-width="2" stroke-linejoin="round"/><polyline points="190.44,53.89 191.97,55.68 193.41,57.55 194.74,59.49 195.97,61.5 197.1,63.57 198.11,65.7 199.01,67.87 199.8,70.09 200.47,72.35 201.02,74.64 201.45,76.96 201.75,79.3 201.94,81.64 202,84 201.94,86.36 201.75,88.7 201.45,91.04 201.02,93.36 200.47,95.65 199.8,97.91 199.01,100.13 198.11,102.3 197.1,104.43 195.97,106.5 194.74,108.51 193.41,110.45 191.97,112.32 190.44,114.11" fill="none" stroke="#0f6e56" stroke-width="2" stroke-linejoin="round"/><circle cx="157" cy="84" r="2.6" fill="#d97706" stroke="#0f172a" stroke-width="1"/><text x="169" y="178" text-anchor="middle" fill="#0f172a" font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">a = 1,5 cm</text><text x="169" y="194" text-anchor="middle" fill="#0f6e56" font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">= λ</text><rect x="228" y="8" width="108" height="152" fill="none" stroke="#cbd5e1" stroke-width="1"/><line x1="270" y1="10" x2="270" y2="81.5" stroke="#0f172a" stroke-width="4.5"/><line x1="270" y1="86.5" x2="270" y2="158" stroke="#0f172a" stroke-width="4.5"/><line x1="255" y1="14" x2="255" y2="154" stroke="#0f6e56" stroke-width="2"/><line x1="240" y1="14" x2="240" y2="154" stroke="#0f6e56" stroke-width="2"/><polyline points="271.31,69.06 272.88,69.28 274.42,69.67 275.91,70.21 277.34,70.92 278.68,71.77 279.93,72.75 281.06,73.87 282.07,75.09 282.94,76.42 283.67,77.83 284.25,79.31 284.66,80.84 284.92,82.41 285,84 284.92,85.59 284.66,87.16 284.25,88.69 283.67,90.17 282.94,91.58 282.07,92.91 281.06,94.13 279.93,95.25 278.68,96.23 277.34,97.08 275.91,97.79 274.42,98.33 272.88,98.72 271.31,98.94" fill="none" stroke="#0f6e56" stroke-width="2" stroke-linejoin="round"/><polyline points="272.61,54.11 275.76,54.56 278.84,55.33 281.83,56.43 284.67,57.83 287.36,59.53 289.85,61.51 292.12,63.73 294.14,66.19 295.89,68.84 297.35,71.66 298.5,74.62 299.33,77.69 299.83,80.83 300,84 299.83,87.17 299.33,90.31 298.5,93.38 297.35,96.34 295.89,99.16 294.14,101.81 292.12,104.27 289.85,106.49 287.36,108.47 284.67,110.17 281.83,111.57 278.84,112.67 275.76,113.44 272.61,113.89" fill="none" stroke="#0f6e56" stroke-width="2" stroke-linejoin="round"/><polyline points="273.92,39.17 278.64,39.84 283.26,41 287.74,42.64 292.01,44.75 296.04,47.3 299.78,50.26 303.18,53.6 306.21,57.28 308.83,61.26 311.02,65.49 312.75,69.93 313.99,74.53 314.75,79.24 315,84 314.75,88.76 313.99,93.47 312.75,98.07 311.02,102.51 308.83,106.74 306.21,110.72 303.18,114.4 299.78,117.74 296.04,120.7 292.01,123.25 287.74,125.36 283.26,127 278.64,128.16 273.92,128.83" fill="none" stroke="#0f6e56" stroke-width="2" stroke-linejoin="round"/><circle cx="270" cy="84" r="2.6" fill="#d97706" stroke="#0f172a" stroke-width="1"/><text x="282" y="178" text-anchor="middle" fill="#0f172a" font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">a = 0,5 cm</text><text x="282" y="194" text-anchor="middle" fill="#0f6e56" font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">≈ λ/3</text><line x1="29" y1="26" x2="17" y2="26" stroke="#0f172a" stroke-width="1.4"/><polygon points="14,26 19,23.9 19,28.1" fill="#0f172a"/><polygon points="29,26 24,28.1 24,23.9" fill="#0f172a"/><text x="21.5" y="20" text-anchor="middle" fill="#0f6e56" font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">λ</text><text x="52" y="79" text-anchor="start" fill="#d97706" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">I</text></svg>
:::

Sur la figure, l'écart entre deux rides consécutives est le même avant et après l'ouverture, alors que leur forme passe de droite à circulaire quand a diminue.

::: exemple Comparer a et λ, puis décrire l'onde derrière l'ouverture (N = 16 Hz ; v = 0,24 m/s)

1. λ = v/N = 0,24/16 = 0,015 m = 1,5 cm, car λ = v·T est la distance entre deux rides consécutives.
2. a = 4,0 cm ≈ 2,7 λ : l'ouverture est grande devant λ et les rides restent presque rectilignes, déformées seulement près des bords.
3. a = 1,5 cm = λ : les rides ressortent circulaires, de centre I, dans une zone triangulaire de sommet I.
4. a = 0,5 cm ≈ λ/3 : les rides sont quasi circulaires, de centre I, et occupent tout le demi-plan derrière l'ouverture.
5. Dans les trois cas, on mesure toujours 1,5 cm entre deux rides consécutives après l'ouverture : λ′ = λ, car la fréquence N et la célérité v ne changent pas.

:::

::: piege
**Erreur : croire qu'il faut a < λ pour qu'il y ait diffraction.** À l'étape 3, a = λ et les rides sont déjà circulaires. L'erreur tente parce qu'on retient « fente très petite ». Mais la diffraction devient nette dès que a est de l'ordre de λ, et elle l'est d'autant plus que a est petite devant λ.
:::

::: propriete
**Ce qui reste vrai** — Un obstacle de largeur a donne le même phénomène qu'une fente de largeur a. Après la diffraction, l'onde garde sa longueur d'onde, et aussi sa fréquence et sa célérité puisque le milieu ne change pas. Cas limite : pour a très grande devant λ, la déformation des rides est imperceptible dans la cuve. Pour mémoire, Huygens (1629-1695) interprète la diffraction en faisant de chaque point d'une surface d'onde une source secondaire d'ondelettes circulaires ; quand a est petite devant λ, l'ouverture se comporte comme une source secondaire unique, d'où les rides circulaires (lecture seulement, on ne s'en sert pas pour calculer).
:::

::: verifie À toi : un son et un faisceau lumineux devant une porte
Une porte ouverte a pour largeur a = 0,90 m. Un son de fréquence 400 Hz (v = 340 m/s) et un faisceau de lumière de longueur d'onde 6 × 10⁻⁷ m la traversent. Dans quel cas la diffraction est-elle perceptible ?

---

Pour le son, λ = v/N = 340/400 = 0,85 m : λ est de l'ordre de a, donc le son se diffracte et on l'entend aussi à côté de la porte, derrière le mur. Pour la lumière, a/λ = 0,90/(6 × 10⁻⁷) = 1,5 × 10⁶ : a est très grande devant λ, la diffraction est imperceptible et la porte projette une ombre nette.
:::

::: retenir
Une fente ou un obstacle de largeur a de l'ordre de λ transforme une onde plane en onde diffractée, de même longueur d'onde.
:::

## 🔦 La figure de diffraction de la lumière : une tache bien plus large que la fente

Un laser rouge de longueur d'onde 633 nm éclaire un écran placé à D = 2 m : on y voit une petite tache. On interpose un diaphragme dont la fente verticale a une largeur a réglable. Si la lumière ne faisait que se propager en ligne droite, la tache serait une bande de la largeur de la fente, de plus en plus fine quand on resserre la fente.
Que voit-on réellement sur l'écran ?

::: definition
**Figure de diffraction** — Une fente fine, ou un obstacle fin comme un fil, éclairée par un laser donne sur l'écran une figure étalée perpendiculairement à la fente : une **tache centrale** brillante, de largeur L (distance entre les milieux des deux bandes sombres qui l'encadrent), et de part et d'autre des **taches latérales** moins brillantes, séparées par des zones sombres. Ces taches sont les **franges de diffraction** ; un trou circulaire donne des **anneaux de diffraction**.
:::

::: figure Écran vu de face pour une fente verticale de 0,6 mm : la tache centrale, la plus large et la plus brillante, mesure L = 4,2 mm entre les milieux des bandes sombres qui l'encadrent, et les taches latérales sont alignées horizontalement
<svg viewBox="0 0 340 152"><title>Écran vu de face pour une fente verticale de 0,6 mm et un écran à 2 m : tache centrale de largeur L = 4,2 mm entre les milieux des bandes sombres, taches latérales plus étroites</title><rect x="10" y="22" width="320" height="60" fill="#111827" stroke="#0f172a" stroke-width="1.5"/><rect x="129.5" y="23" width="81" height="58" fill="#ef4444" opacity="1.0"/><rect x="213.5" y="23" width="39" height="58" fill="#ef4444" opacity="0.55"/><rect x="87.5" y="23" width="39" height="58" fill="#ef4444" opacity="0.55"/><rect x="255.5" y="23" width="39" height="58" fill="#ef4444" opacity="0.4"/><rect x="45.5" y="23" width="39" height="58" fill="#ef4444" opacity="0.4"/><rect x="297.5" y="23" width="31" height="58" fill="#ef4444" opacity="0.3"/><rect x="11.5" y="23" width="31" height="58" fill="#ef4444" opacity="0.3"/><line x1="10" y1="98" x2="330" y2="98" stroke="#0f172a" stroke-width="1.4"/><line x1="30" y1="98" x2="30" y2="102" stroke="#0f172a" stroke-width="1.2"/><line x1="50" y1="98" x2="50" y2="105" stroke="#0f172a" stroke-width="1.2"/><text x="50" y="118" text-anchor="middle" fill="#0f172a" font-size="10" font-weight="600" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−6</text><line x1="70" y1="98" x2="70" y2="102" stroke="#0f172a" stroke-width="1.2"/><line x1="90" y1="98" x2="90" y2="105" stroke="#0f172a" stroke-width="1.2"/><text x="90" y="118" text-anchor="middle" fill="#0f172a" font-size="10" font-weight="600" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−4</text><line x1="110" y1="98" x2="110" y2="102" stroke="#0f172a" stroke-width="1.2"/><line x1="130" y1="98" x2="130" y2="105" stroke="#0f172a" stroke-width="1.2"/><text x="130" y="118" text-anchor="middle" fill="#0f172a" font-size="10" font-weight="600" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−2</text><line x1="150" y1="98" x2="150" y2="102" stroke="#0f172a" stroke-width="1.2"/><line x1="170" y1="98" x2="170" y2="105" stroke="#0f172a" stroke-width="1.2"/><text x="170" y="118" text-anchor="middle" fill="#0f172a" font-size="10" font-weight="600" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><line x1="190" y1="98" x2="190" y2="102" stroke="#0f172a" stroke-width="1.2"/><line x1="210" y1="98" x2="210" y2="105" stroke="#0f172a" stroke-width="1.2"/><text x="210" y="118" text-anchor="middle" fill="#0f172a" font-size="10" font-weight="600" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><line x1="230" y1="98" x2="230" y2="102" stroke="#0f172a" stroke-width="1.2"/><line x1="250" y1="98" x2="250" y2="105" stroke="#0f172a" stroke-width="1.2"/><text x="250" y="118" text-anchor="middle" fill="#0f172a" font-size="10" font-weight="600" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4</text><line x1="270" y1="98" x2="270" y2="102" stroke="#0f172a" stroke-width="1.2"/><line x1="290" y1="98" x2="290" y2="105" stroke="#0f172a" stroke-width="1.2"/><text x="290" y="118" text-anchor="middle" fill="#0f172a" font-size="10" font-weight="600" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">6</text><line x1="310" y1="98" x2="310" y2="102" stroke="#0f172a" stroke-width="1.2"/><text x="170" y="134" text-anchor="middle" fill="#0f172a" font-size="11" font-weight="600" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">position sur l'écran (mm)</text><line x1="128" y1="16" x2="208.4" y2="16" stroke="#d97706" stroke-width="1.8"/><polygon points="212,16 206,18.52 206,13.48" fill="#d97706"/><polygon points="128,16 134,13.48 134,18.52" fill="#d97706"/><text x="170" y="12" text-anchor="middle" fill="#d97706" font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">L</text></svg>
:::

Sur la figure, la graduation en millimètres permet de lire L ; la fente est verticale et les taches s'alignent horizontalement, donc perpendiculairement à la fente.

::: exemple Interpréter la figure (laser de 633 nm, fente verticale, écran à D = 2 m)

1. Pour a = 0,6 mm, on lit L = 4,2 mm, soit 7 fois la largeur de la fente : si la lumière allait en ligne droite, la tache ferait 0,6 mm.
2. On resserre la fente à a = 0,3 mm : la tache centrale mesure L′ = 8,4 mm = 2L. Elle s'élargit quand la fente se resserre, ce que la propagation rectiligne ne peut pas expliquer.
3. Les taches latérales sont moins brillantes que la tache centrale et séparées d'elle par des zones sombres : la lumière a été étalée dans plusieurs directions, comme une onde diffractée.
4. Par rapprochement avec l'onde mécanique, la propagation de la lumière dans un milieu transparent ou dans le vide est celle d'une **onde lumineuse**.

:::

::: piege
**Erreur : croire qu'une fente plus fine donne une tache plus fine.** Pour a = 0,3 mm, on mesure 8,4 mm, deux fois plus qu'avec 0,6 mm (étape 2). L'erreur tente parce qu'on se représente un faisceau comme des rayons qui passent ou non. Mais, pour un même laser et un même écran, plus la fente est fine, plus la figure s'étale.
:::

::: propriete
**Ce qui reste vrai** — Un obstacle de largeur a donne la même figure qu'une fente de largeur a : un fil de diamètre d donne celle d'une fente de largeur d. La figure a les symétries de l'objet : des taches alignées pour une fente rectangulaire, des anneaux pour un trou circulaire. Cas limite : a = 0,6 mm vaut environ 950 λ, et la diffraction se mesure pourtant, parce que l'étalement angulaire, très petit, est multiplié par la distance D de l'écran (notion 5).
:::

::: verifie À toi : un fil horizontal
Un fil horizontal de diamètre 0,6 mm est tendu devant le laser de 633 nm, l'écran étant toujours à 2 m. Dans quelle direction les taches sont-elles alignées, et quelle est la largeur de la tache centrale ?

---

Le fil joue le rôle d'une fente horizontale de largeur 0,6 mm : la lumière s'étale perpendiculairement au fil, donc les taches sont alignées verticalement. Comme pour la fente de 0,6 mm, la tache centrale mesure L = 4,2 mm (étape 1).
:::

::: retenir
Une fente fine ou un fil donne une tache centrale large, entourée de taches latérales alignées perpendiculairement à l'obstacle : la propagation rectiligne est mise en défaut et la lumière est une onde.
:::

## 〰️ L'onde lumineuse : célérité c, période T et longueur d'onde

Si la lumière est une onde, elle a comme les rides de la cuve une période temporelle T et une période spatiale λ. Une mesure donne à une radiation rouge la fréquence ν = 4,57 × 10¹⁴ Hz (on note ν la fréquence d'une radiation lumineuse, et N celle d'une onde mécanique).
Quelles sont sa période et sa longueur d'onde dans l'air ?

::: definition
**Onde lumineuse** — La propagation de la lumière dans un milieu transparent ou dans le vide est celle d'une **onde lumineuse**. Elle a une période temporelle T, de fréquence ν = 1/T, et une période spatiale λ. Dans le vide, toutes les ondes lumineuses se propagent à la même célérité c = 3,00 × 10⁸ m/s, et la longueur d'onde dans le vide λ₀ vérifie :

$$ λ₀ = c·T = c/ν $$

Dans l'air, on assimile la célérité à c avec une bonne approximation.
:::

::: exemple Période et longueur d'onde de la radiation rouge (ν = 4,57 × 10¹⁴ Hz, dans l'air)

1. T = 1/ν = 1/(4,57 × 10¹⁴) = 2,19 × 10⁻¹⁵ s, car la fréquence est l'inverse de la période.
2. Dans l'air, la célérité est celle du vide : c = 3,00 × 10⁸ m/s, car l'air est assimilé au vide.
3. λ₀ = c/ν = 3,00 × 10⁸/(4,57 × 10¹⁴) = 6,56 × 10⁻⁷ m = 656 nm, car λ₀ = c·T.
4. Contrôle : c·T = 3,00 × 10⁸ × 2,188 × 10⁻¹⁵ = 6,56 × 10⁻⁷ m ✓.

:::

::: piege
**Erreur : multiplier c par la fréquence au lieu de la diviser.** On trouverait 3,00 × 10⁸ × 4,57 × 10¹⁴ = 1,4 × 10²³ m, une longueur absurde. L'erreur tente parce que la relation entre vitesse, longueur d'onde et fréquence s'écrit avec un produit quand on cherche la célérité. Mais ici on cherche une longueur : c est en m/s et ν en s⁻¹, donc c/ν est bien en mètres.
:::

::: propriete
**Ce qui reste vrai** — Toutes les radiations ont la même célérité c dans le vide, donc λ₀ = c/ν : plus la fréquence est grande, plus la longueur d'onde dans le vide est petite. Dans le tableau de la notion 9, ν va de 3,91 à 6,92 × 10¹⁴ Hz pour λ₀ allant de 0,767 à 0,433 µm : les radiations rouges ont les plus grandes longueurs d'onde du spectre visible et les bleues les plus petites : le rouge (0,656 µm) a ainsi une longueur d'onde plus grande que le vert. Cas limite : cette relation vaut dans le vide et dans l'air ; dans un verre la célérité n'est plus c.
:::

::: verifie À toi : une radiation violette
Une radiation violette a pour fréquence ν = 7,5 × 10¹⁴ Hz. Calculer sa période T et sa longueur d'onde λ₀ dans le vide.

---

T = 1/ν = 1/(7,5 × 10¹⁴) = 1,33 × 10⁻¹⁵ s, et λ₀ = c/ν = 3,00 × 10⁸/(7,5 × 10¹⁴) = 4,0 × 10⁻⁷ m = 400 nm : une fréquence plus grande que celle du rouge donne une longueur d'onde plus petite.
:::

::: retenir
La lumière est une onde de période T et de fréquence ν = 1/T ; dans le vide, λ₀ = c·T = c/ν avec c = 3,00 × 10⁸ m/s.
:::

## 📐 Le quotient λ/a : de quoi dépend la netteté de la diffraction

Dans la cuve, on garde N = 15 Hz et a = 1,5 cm et on augmente la profondeur d'eau. Avec le laser, on garde D = 2 m et on réduit la largeur a, puis on passe du laser rouge au laser vert.
Quelles grandeurs règlent la netteté de la diffraction ?

Mesures de la largeur L de la tache centrale (D = 2 m), pour des fentes de largeur a :

| a (10⁻³ m)         | 0,10 | 0,14 | 0,20 | 0,25 |
| ------------------ | ---- | ---- | ---- | ---- |
| 1/a (10³ m⁻¹)      | 10,0 | 7,1  | 5,0  | 4,0  |
| L laser rouge (mm) | 25   | 18   | 12   | 10   |
| L laser vert (mm)  | 21   | 15   | 10   | 8    |

::: figure Les mesures du tableau portées en L en fonction de 1/a : les quatre points de chaque laser sont alignés sur une droite passant par l'origine, et la droite du laser rouge est au-dessus de celle du laser vert
<svg viewBox="0 0 340 226"><title>Largeur L de la tache centrale en fonction de 1/a pour un laser rouge et un laser vert, écran à D = 2 m : deux droites passant par l'origine, la rouge au-dessus de la verte</title><line x1="50" y1="186" x2="50" y2="36" stroke="#e2e8f0" stroke-width="1"/><text x="50" y="200" text-anchor="middle" fill="#0f172a" font-size="10" font-weight="600" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><line x1="106" y1="186" x2="106" y2="36" stroke="#e2e8f0" stroke-width="1"/><text x="106" y="200" text-anchor="middle" fill="#0f172a" font-size="10" font-weight="600" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><line x1="162" y1="186" x2="162" y2="36" stroke="#e2e8f0" stroke-width="1"/><text x="162" y="200" text-anchor="middle" fill="#0f172a" font-size="10" font-weight="600" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4</text><line x1="218" y1="186" x2="218" y2="36" stroke="#e2e8f0" stroke-width="1"/><text x="218" y="200" text-anchor="middle" fill="#0f172a" font-size="10" font-weight="600" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">6</text><line x1="274" y1="186" x2="274" y2="36" stroke="#e2e8f0" stroke-width="1"/><text x="274" y="200" text-anchor="middle" fill="#0f172a" font-size="10" font-weight="600" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">8</text><line x1="330" y1="186" x2="330" y2="36" stroke="#e2e8f0" stroke-width="1"/><text x="330" y="200" text-anchor="middle" fill="#0f172a" font-size="10" font-weight="600" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">10</text><line x1="50" y1="186" x2="330" y2="186" stroke="#e2e8f0" stroke-width="1"/><text x="44" y="190" text-anchor="end" fill="#0f172a" font-size="10" font-weight="600" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><line x1="50" y1="164.57" x2="330" y2="164.57" stroke="#e2e8f0" stroke-width="1"/><text x="44" y="168.57" text-anchor="end" fill="#0f172a" font-size="10" font-weight="600" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4</text><line x1="50" y1="143.14" x2="330" y2="143.14" stroke="#e2e8f0" stroke-width="1"/><text x="44" y="147.14" text-anchor="end" fill="#0f172a" font-size="10" font-weight="600" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">8</text><line x1="50" y1="121.71" x2="330" y2="121.71" stroke="#e2e8f0" stroke-width="1"/><text x="44" y="125.71" text-anchor="end" fill="#0f172a" font-size="10" font-weight="600" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">12</text><line x1="50" y1="100.29" x2="330" y2="100.29" stroke="#e2e8f0" stroke-width="1"/><text x="44" y="104.29" text-anchor="end" fill="#0f172a" font-size="10" font-weight="600" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">16</text><line x1="50" y1="78.86" x2="330" y2="78.86" stroke="#e2e8f0" stroke-width="1"/><text x="44" y="82.86" text-anchor="end" fill="#0f172a" font-size="10" font-weight="600" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">20</text><line x1="50" y1="57.43" x2="330" y2="57.43" stroke="#e2e8f0" stroke-width="1"/><text x="44" y="61.43" text-anchor="end" fill="#0f172a" font-size="10" font-weight="600" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">24</text><line x1="50" y1="36" x2="330" y2="36" stroke="#e2e8f0" stroke-width="1"/><text x="44" y="40" text-anchor="end" fill="#0f172a" font-size="10" font-weight="600" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">28</text><line x1="50" y1="186" x2="336" y2="186" stroke="#0f172a" stroke-width="1.8"/><line x1="50" y1="186" x2="50" y2="28" stroke="#0f172a" stroke-width="1.8"/><text x="190" y="216" text-anchor="middle" fill="#0f172a" font-size="11" font-weight="600" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1/a (10³ m⁻¹)</text><text x="52" y="24" text-anchor="start" fill="#0f172a" font-size="11" font-weight="600" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">L (mm)</text><line x1="50" y1="186" x2="330" y2="52.07" stroke="#c2410c" stroke-width="2"/><circle cx="330" cy="52.07" r="3.6" fill="#c2410c" stroke="#0f172a" stroke-width="1"/><circle cx="248.8" cy="89.57" r="3.6" fill="#c2410c" stroke="#0f172a" stroke-width="1"/><circle cx="190" cy="121.71" r="3.6" fill="#c2410c" stroke="#0f172a" stroke-width="1"/><circle cx="162" cy="132.43" r="3.6" fill="#c2410c" stroke="#0f172a" stroke-width="1"/><text x="326" y="44.07" text-anchor="end" fill="#c2410c" font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">laser rouge</text><line x1="50" y1="186" x2="330" y2="76.18" stroke="#15803d" stroke-width="2"/><circle cx="330" cy="73.5" r="3.6" fill="#15803d" stroke="#0f172a" stroke-width="1"/><circle cx="248.8" cy="105.64" r="3.6" fill="#15803d" stroke="#0f172a" stroke-width="1"/><circle cx="190" cy="132.43" r="3.6" fill="#15803d" stroke="#0f172a" stroke-width="1"/><circle cx="162" cy="143.14" r="3.6" fill="#15803d" stroke="#0f172a" stroke-width="1"/><text x="326" y="68.18" text-anchor="end" fill="#15803d" font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">laser vert</text></svg>
:::

Sur le graphique, chaque point est une ligne du tableau ; la pente de chaque droite est la constante k de la relation L = k/a.

::: exemple La cuve : λ/a avec la profondeur (N = 15 Hz ; a = 1,5 cm)

1. À la profondeur e₁, la célérité est v₁ = 0,21 m/s : λ₁ = v₁/N = 0,21/15 = 1,4 cm, donc λ₁/a = 1,4/1,5 = 0,93 et a ≈ λ₁.
2. À la profondeur e₂ = 3e₁, la célérité est v₂ = 0,36 m/s : λ₂ = 0,36/15 = 2,4 cm, donc λ₂/a = 1,6 et a < λ₂.
3. Dans le premier cas les rides sont circulaires dans une zone triangulaire ; dans le second elles sont quasi circulaires. La diffraction est plus marquée avec le quotient λ/a le plus grand.

:::

::: exemple Le laser : L en fonction de a (D = 2 m)

1. La fente passe de a = 0,10 mm à 0,20 mm, donc elle double ; L passe de 25 mm à 12 mm, soit à peu près la moitié : L diminue quand a augmente.
2. On calcule le produit L·a du laser rouge : 25 × 0,10 = 2,5 ; 18 × 0,14 = 2,52 ; 12 × 0,20 = 2,4 ; 10 × 0,25 = 2,5 (en 10⁻⁶ m²). Il est constant : L = k/a avec k ≈ 2,5 × 10⁻⁶ m², ce qui explique les points alignés avec l'origine sur le graphique.
3. Pour le laser vert, L·a vaut 2,1 ; 2,1 ; 2,0 ; 2,0 : k ≈ 2,05 × 10⁻⁶ m², plus petite que celle du rouge.
4. Pour un même a, L(rouge) > L(vert) alors que λ(rouge) > λ(vert) : L augmente avec λ.

:::

::: piege
**Erreur : croire que L est proportionnelle à a.** En doublant a de 0,10 à 0,20 mm, on attendrait L = 2 × 25 = 50 mm. La mesure est de 12 mm (étape 1 du laser). L'erreur tente parce que « plus grand a, plus grande tache » paraît naturel. Mais c'est le produit L·a qui reste constant : L et a varient en sens inverse.
:::

::: propriete
**Ce qui reste vrai** — Le phénomène de diffraction dépend du quotient λ/a : il est d'autant plus marqué que λ/a est grand, c'est-à-dire que a est petit ou λ grande. Pour la lumière, L = k/a, la constante k dépendant de λ (et de D). Cas limite : pour a très grande devant λ, la diffraction est imperceptible, comme dans la cuve pour a = 4,0 cm devant λ = 1,5 cm.
:::

::: verifie À toi : une autre fente avec le laser rouge
Avec le laser rouge de la mesure (k ≈ 2,5 × 10⁻⁶ m², D = 2 m), on utilise une fente de largeur a = 0,50 mm. Quelle largeur L attend-on pour la tache centrale ?

---

L = k/a = 2,5 × 10⁻⁶/(5,0 × 10⁻⁴) = 5,0 × 10⁻³ m = 5,0 mm. C'est cohérent avec le tableau : a plus grande que 0,25 mm donne L plus petite que 10 mm.
:::

::: retenir
La diffraction est d'autant plus marquée que λ/a est grand : L = k/a, et L croît avec λ.
:::

## 📏 La demi-largeur angulaire θ : L = 2λD/a

Dans le tableau précédent, L est une distance sur l'écran : elle dépend de l'endroit où on l'a placé. Pour la fente de a = 0,10 mm et le laser rouge, L = 25 mm à D = 2 m.
Quelle grandeur ne dépend pas de la place de l'écran, et comment relier L à λ, a et D ?

::: definition
**Demi-largeur angulaire** — La **demi-largeur angulaire** θ de la tache centrale est l'angle, vu depuis la fente, entre l'axe du montage et la direction du bord de la tache (le milieu de la première bande sombre). Dans le triangle de la figure, tg θ = L/(2D) ; pour un petit angle, exprimé en radians, tg θ ≈ θ, donc :

$$ θ ≈ L/(2D) $$
:::

::: figure Schéma vu de dessus (angle exagéré) : la fente de centre I, l'écran à la distance D, la largeur L de la tache centrale et l'angle θ entre l'axe et la direction d'un bord de la tache
<svg viewBox="0 0 340 216"><title>Schéma vu de dessus (angle exagéré) : la fente de centre I, l'écran à la distance D, la largeur L de la tache centrale et la demi-largeur angulaire θ entre l'axe et la direction d'un bord de la tache</title><line x1="290" y1="18" x2="290" y2="190" stroke="#0f172a" stroke-width="3"/><text x="290" y="206" text-anchor="middle" fill="#0f172a" font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">écran</text><line x1="46" y1="52" x2="46" y2="98" stroke="#0f172a" stroke-width="4"/><line x1="46" y1="110" x2="46" y2="156" stroke="#0f172a" stroke-width="4"/><text x="46" y="172" text-anchor="middle" fill="#0f172a" font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">fente</text><circle cx="46" cy="104" r="2.8" fill="#d97706" stroke="#0f172a" stroke-width="1"/><text x="38" y="108" text-anchor="end" fill="#d97706" font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">I</text><line x1="46" y1="104" x2="290" y2="104" stroke="#64748b" stroke-width="1.4" stroke-dasharray="6 4"/><text x="246" y="98" text-anchor="middle" fill="#64748b" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">axe</text><line x1="46" y1="104" x2="283.91" y2="48.62" stroke="#d97706" stroke-width="1.8"/><polygon points="288,47.67 281.85,52.12 280.52,46.39" fill="#d97706"/><line x1="46" y1="104" x2="283.91" y2="159.38" stroke="#d97706" stroke-width="1.8"/><polygon points="288,160.33 280.52,161.61 281.85,155.88" fill="#d97706"/><line x1="304" y1="47.67" x2="304" y2="156.73" stroke="#0f6e56" stroke-width="1.8"/><polygon points="304,160.33 301.48,154.33 306.52,154.33" fill="#0f6e56"/><polygon points="304,47.67 306.52,53.67 301.48,53.67" fill="#0f6e56"/><text x="320" y="108" text-anchor="start" fill="#0f6e56" font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">L</text><line x1="46" y1="156" x2="286.4" y2="156" stroke="#0f172a" stroke-width="1.6"/><polygon points="290,156 284,158.52 284,153.48" fill="#0f172a"/><polygon points="46,156 52,153.48 52,158.52" fill="#0f172a"/><text x="168" y="172" text-anchor="middle" fill="#0f172a" font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">D</text><polyline points="100.56,91.4 100.9,92.96 101.19,94.52 101.44,96.09 101.64,97.66 101.8,99.24 101.91,100.83 101.98,102.41 102,104" fill="none" stroke="#d97706" stroke-width="1.8" stroke-linejoin="round"/><text x="120" y="96" text-anchor="middle" fill="#d97706" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">θ</text><line x1="284" y1="47.67" x2="290" y2="47.67" stroke="#0f172a" stroke-width="1.4"/><line x1="284" y1="160.33" x2="290" y2="160.33" stroke="#0f172a" stroke-width="1.4"/></svg>
:::

Sur le schéma, D se mesure de la fente à l'écran et L sur l'écran ; c'est le demi-segment L/2 qui est vu sous l'angle θ depuis I.

::: exemple Établir θ = λ/a à partir des mesures (D = 2 m)

1. Laser rouge, a = 0,10 mm et L = 25 mm : θ = L/(2D) = 25 × 10⁻³/4 = 6,25 × 10⁻³ rad.
2. Pour a = 0,25 mm et L = 10 mm : θ = 10 × 10⁻³/4 = 2,5 × 10⁻³ rad. Les produits θ·a valent 6,25 × 10⁻⁷ m dans les deux cas, donc θ·a est constant.
3. Cette constante, 625 nm, est voisine de la longueur d'onde du laser rouge, 633 nm : θ·a/λ ≈ 1. Pour le laser vert, θ·a = k/(2D) = 2,05 × 10⁻⁶/4 = 5,1 × 10⁻⁷ m, voisin de sa longueur d'onde (environ 514 nm) : même résultat.
4. On en tire θ = λ/a, puis, comme L = 2Dθ, la relation L = 2λD/a.

:::

::: exemple Appliquer les relations (diode laser de 650 nm ; a = 0,13 mm ; D = 3,0 m)

1. θ = λ/a = 650 × 10⁻⁹/(1,3 × 10⁻⁴) = 5,0 × 10⁻³ rad : c'est un petit angle, donc tg θ ≈ θ est justifié.
2. L = 2Dθ = 2 × 3,0 × 5,0 × 10⁻³ = 3,0 × 10⁻² m = 30 mm.
3. On rapproche l'écran à D′ = 1,5 m : L′ = 2D′θ = 15 mm, mais θ reste 5,0 × 10⁻³ rad, car il ne dépend que de λ et de a.

:::

::: piege
**Erreur : écrire θ = L/D.** Pour L = 30 mm et D = 3,0 m, on trouverait 1,0 × 10⁻² rad, le double de la valeur de l'étape 1. L'erreur tente parce qu'une longueur divisée par une distance donne un angle. Mais L est la largeur totale de la tache, de bord à bord, alors que θ ne concerne qu'un côté de l'axe : c'est la moitié L/2 qui est vue sous θ.
:::

::: propriete
**Ce qui reste vrai** — Pour une fente de largeur a éclairée par une lumière de longueur d'onde λ : θ = λ/a et L = 2λD/a. L'angle θ ne dépend que de λ et de a ; L est proportionnelle à λ et à D, inversement proportionnelle à a ; une tache latérale a pour largeur L/2, la moitié de celle de la tache centrale. Cas limite : ces relations valent pour de petits angles. Pour un trou circulaire de diamètre a, la tache centrale a pour demi-largeur angulaire θ = 1,22 λ/a et pour rayon r = 1,22 λD/a (formule donnée dans les exercices).
:::

::: verifie À toi : retrouver la longueur d'onde
Une fente de largeur a = 80 µm, éclairée par un laser, donne sur un écran à D = 2,0 m une tache centrale de largeur L = 3,2 cm. Calculer λ et la largeur d'une tache latérale.

---

λ = a·L/(2D) = 8,0 × 10⁻⁵ × 3,2 × 10⁻²/(2 × 2,0) = 6,4 × 10⁻⁷ m = 640 nm, d'après L = 2λD/a. Une tache latérale a pour largeur L/2 = 1,6 cm.
:::

::: retenir
θ ≈ L/(2D) = λ/a, donc L = 2λD/a : θ ne dépend pas de D, et la tache latérale mesure L/2.
:::

## 🪢 La réflexion d'un ébranlement : incident, réfléchi

Une corde est tendue horizontalement entre une main A et un mur B où elle est attachée. La main donne une secousse brève vers le haut : une bosse de 2,0 cm de hauteur part vers B. On refait l'expérience en remplaçant le mur par un anneau léger, qui glisse sans frottement sur une tige verticale.
Que devient la bosse en arrivant à l'extrémité B dans chaque cas ?

::: definition
**Ébranlement incident, ébranlement réfléchi** — Quand un ébranlement atteint l'extrémité B du milieu de propagation, il repart en sens contraire : l'ébranlement qui arrive est l'ébranlement **incident**, celui qui repart est l'ébranlement **réfléchi**. L'extrémité est **fixe** (corde attachée au mur) ou **libre** (corde accrochée à l'anneau glissant).
:::

::: figure Une bosse (en vert) arrive à droite à la date t₁ ; à la date t₂ l'ébranlement réfléchi (en rouge) revient vers la gauche : à l'extrémité libre il est une bosse, à l'extrémité fixe un creux
<svg viewBox="0 0 340 266"><title>Ébranlement incident (vert) puis ébranlement réfléchi (rouge) sur une corde : à l'extrémité B libre la bosse revient en bosse, à l'extrémité B fixe elle revient en creux</title><text x="24" y="16" text-anchor="start" fill="#0f172a" font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">B libre</text><polyline points="30,40 32,40 34,40 36,40 38,40 40,40 42,40 44,40 46,40 48,40 50,40 52,40 54,39.99 56,39.99 58,39.98 60,39.95 62,39.91 64,39.85 66,39.74 68,39.56 70,39.29 72,38.88 74,38.29 76,37.47 78,36.38 80,34.97 82,33.23 84,31.17 86,28.84 88,26.33 90,23.76 92,21.31 94,19.15 96,17.45 98,16.37 100,16 102,16.37 104,17.45 106,19.15 108,21.31 110,23.76 112,26.33 114,28.84 116,31.17 118,33.23 120,34.97 122,36.38 124,37.47 126,38.29 128,38.88 130,39.29 132,39.56 134,39.74 136,39.85 138,39.91 140,39.95 142,39.98 144,39.99 146,39.99 148,40 150,40 152,40 154,40 156,40 158,40 160,40 162,40 164,40 166,40 168,40 170,40 172,40 174,40 176,40 178,40 180,40 182,40 184,40 186,40 188,40 190,40 192,40 194,40 196,40 198,40 200,40 202,40 204,40 206,40 208,40 210,40 212,40 214,40 216,40 218,40 220,40 222,40 224,40 226,40 228,40 230,40 232,40 234,40 236,40 238,40 240,40 242,40 244,40 246,40 248,40 250,40 252,40 254,40 256,40 258,40 260,40 262,40 264,40 266,40 268,40 270,40 272,40 274,40 276,40 278,40 280,40 282,40 284,40 286,40 288,40 290,40 292,40 294,40 296,40 298,40 300,40" fill="none" stroke="#0f6e56" stroke-width="2.4" stroke-linejoin="round"/><text x="26" y="44" text-anchor="end" fill="#0f172a" font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">t₁</text><polyline points="30,100 32,100 34,100 36,100 38,100 40,100 42,100 44,100 46,100 48,100 50,100 52,100 54,100 56,100 58,100 60,100 62,100 64,100 66,100 68,100 70,100 72,100 74,100 76,100 78,100 80,100 82,100 84,100 86,100 88,100 90,100 92,100 94,100 96,100 98,100 100,100 102,100 104,100 106,100 108,100 110,100 112,100 114,100 116,100 118,100 120,100 122,100 124,100 126,100 128,100 130,100 132,100 134,100 136,100 138,100 140,100 142,100 144,100 146,100 148,100 150,100 152,100 154,99.99 156,99.99 158,99.98 160,99.95 162,99.91 164,99.85 166,99.74 168,99.56 170,99.29 172,98.88 174,98.29 176,97.47 178,96.38 180,94.97 182,93.23 184,91.17 186,88.84 188,86.33 190,83.76 192,81.31 194,79.15 196,77.45 198,76.37 200,76 202,76.37 204,77.45 206,79.15 208,81.31 210,83.76 212,86.33 214,88.84 216,91.17 218,93.23 220,94.97 222,96.38 224,97.47 226,98.29 228,98.88 230,99.29 232,99.56 234,99.74 236,99.85 238,99.91 240,99.95 242,99.98 244,99.99 246,99.99 248,100 250,100 252,100 254,100 256,100 258,100 260,100 262,100 264,100 266,100 268,100 270,100 272,100 274,100 276,100 278,100 280,100 282,100 284,100 286,100 288,100 290,100 292,100 294,100 296,100 298,100 300,100" fill="none" stroke="#c2410c" stroke-width="2.4" stroke-linejoin="round"/><text x="26" y="104" text-anchor="end" fill="#0f172a" font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">t₂</text><line x1="120" y1="58" x2="156.4" y2="58" stroke="#0f6e56" stroke-width="1.6"/><polygon points="160,58 154,60.52 154,55.48" fill="#0f6e56"/><line x1="180" y1="118" x2="143.6" y2="118" stroke="#c2410c" stroke-width="1.6"/><polygon points="140,118 146,115.48 146,120.52" fill="#c2410c"/><line x1="300" y1="10" x2="300" y2="130" stroke="#64748b" stroke-width="2.2" stroke-dasharray="5 3"/><circle cx="300" cy="40" r="5.5" fill="#ffffff" stroke="#0f172a" stroke-width="2"/><circle cx="300" cy="100" r="5.5" fill="#ffffff" stroke="#0f172a" stroke-width="2"/><text x="24" y="148" text-anchor="start" fill="#0f172a" font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">B fixe</text><polyline points="30,172 32,172 34,172 36,172 38,172 40,172 42,172 44,172 46,172 48,172 50,172 52,172 54,171.99 56,171.99 58,171.98 60,171.95 62,171.91 64,171.85 66,171.74 68,171.56 70,171.29 72,170.88 74,170.29 76,169.47 78,168.38 80,166.97 82,165.23 84,163.17 86,160.84 88,158.33 90,155.76 92,153.31 94,151.15 96,149.45 98,148.37 100,148 102,148.37 104,149.45 106,151.15 108,153.31 110,155.76 112,158.33 114,160.84 116,163.17 118,165.23 120,166.97 122,168.38 124,169.47 126,170.29 128,170.88 130,171.29 132,171.56 134,171.74 136,171.85 138,171.91 140,171.95 142,171.98 144,171.99 146,171.99 148,172 150,172 152,172 154,172 156,172 158,172 160,172 162,172 164,172 166,172 168,172 170,172 172,172 174,172 176,172 178,172 180,172 182,172 184,172 186,172 188,172 190,172 192,172 194,172 196,172 198,172 200,172 202,172 204,172 206,172 208,172 210,172 212,172 214,172 216,172 218,172 220,172 222,172 224,172 226,172 228,172 230,172 232,172 234,172 236,172 238,172 240,172 242,172 244,172 246,172 248,172 250,172 252,172 254,172 256,172 258,172 260,172 262,172 264,172 266,172 268,172 270,172 272,172 274,172 276,172 278,172 280,172 282,172 284,172 286,172 288,172 290,172 292,172 294,172 296,172 298,172 300,172" fill="none" stroke="#0f6e56" stroke-width="2.4" stroke-linejoin="round"/><text x="26" y="176" text-anchor="end" fill="#0f172a" font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">t₁</text><polyline points="30,232 32,232 34,232 36,232 38,232 40,232 42,232 44,232 46,232 48,232 50,232 52,232 54,232 56,232 58,232 60,232 62,232 64,232 66,232 68,232 70,232 72,232 74,232 76,232 78,232 80,232 82,232 84,232 86,232 88,232 90,232 92,232 94,232 96,232 98,232 100,232 102,232 104,232 106,232 108,232 110,232 112,232 114,232 116,232 118,232 120,232 122,232 124,232 126,232 128,232 130,232 132,232 134,232 136,232 138,232 140,232 142,232 144,232 146,232 148,232 150,232 152,232 154,232.01 156,232.01 158,232.02 160,232.05 162,232.09 164,232.15 166,232.26 168,232.44 170,232.71 172,233.12 174,233.71 176,234.53 178,235.62 180,237.03 182,238.77 184,240.83 186,243.16 188,245.67 190,248.24 192,250.69 194,252.85 196,254.55 198,255.63 200,256 202,255.63 204,254.55 206,252.85 208,250.69 210,248.24 212,245.67 214,243.16 216,240.83 218,238.77 220,237.03 222,235.62 224,234.53 226,233.71 228,233.12 230,232.71 232,232.44 234,232.26 236,232.15 238,232.09 240,232.05 242,232.02 244,232.01 246,232.01 248,232 250,232 252,232 254,232 256,232 258,232 260,232 262,232 264,232 266,232 268,232 270,232 272,232 274,232 276,232 278,232 280,232 282,232 284,232 286,232 288,232 290,232 292,232 294,232 296,232 298,232 300,232" fill="none" stroke="#c2410c" stroke-width="2.4" stroke-linejoin="round"/><text x="26" y="236" text-anchor="end" fill="#0f172a" font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">t₂</text><line x1="120" y1="190" x2="156.4" y2="190" stroke="#0f6e56" stroke-width="1.6"/><polygon points="160,190 154,192.52 154,187.48" fill="#0f6e56"/><line x1="180" y1="214" x2="143.6" y2="214" stroke="#c2410c" stroke-width="1.6"/><polygon points="140,214 146,211.48 146,216.52" fill="#c2410c"/><line x1="300" y1="142" x2="300" y2="266" stroke="#0f172a" stroke-width="4"/><line x1="300" y1="146" x2="309" y2="139" stroke="#0f172a" stroke-width="1.4"/><line x1="300" y1="156" x2="309" y2="149" stroke="#0f172a" stroke-width="1.4"/><line x1="300" y1="166" x2="309" y2="159" stroke="#0f172a" stroke-width="1.4"/><line x1="300" y1="176" x2="309" y2="169" stroke="#0f172a" stroke-width="1.4"/><line x1="300" y1="186" x2="309" y2="179" stroke="#0f172a" stroke-width="1.4"/><line x1="300" y1="196" x2="309" y2="189" stroke="#0f172a" stroke-width="1.4"/><line x1="300" y1="206" x2="309" y2="199" stroke="#0f172a" stroke-width="1.4"/><line x1="300" y1="216" x2="309" y2="209" stroke="#0f172a" stroke-width="1.4"/><line x1="300" y1="226" x2="309" y2="219" stroke="#0f172a" stroke-width="1.4"/><line x1="300" y1="236" x2="309" y2="229" stroke="#0f172a" stroke-width="1.4"/><line x1="300" y1="246" x2="309" y2="239" stroke="#0f172a" stroke-width="1.4"/><line x1="300" y1="256" x2="309" y2="249" stroke="#0f172a" stroke-width="1.4"/><text x="298" y="14" text-anchor="middle" fill="#0f172a" font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">B</text></svg>
:::

Sur la figure, la flèche verte est le sens de propagation de l'ébranlement incident, la flèche rouge celui de l'ébranlement réfléchi ; seul le sens de déformation de ce dernier dépend de l'extrémité.

::: exemple Suivre une bosse de 2,0 cm sur une corde AB de longueur 3,0 m (v = 6,0 m/s)

1. B fixe : la bosse haute de 2,0 cm atteint B et repart sous forme d'un creux de 2,0 cm : même amplitude, sens de déformation contraire.
2. B libre : la bosse repart sous forme d'une bosse de 2,0 cm : même amplitude, même sens de déformation.
3. Dans les deux cas, l'ébranlement réfléchi se propage de B vers A à la même célérité, 6,0 m/s, puisque la corde est la même : l'aller-retour dure 2 × AB/v = 2 × 3,0/6,0 = 1,0 s.

:::

::: piege
**Erreur : croire que la réflexion renverse toujours l'ébranlement.** Au mur (étape 1) la bosse devient un creux, mais à l'anneau (étape 2) elle reste une bosse. L'erreur tente parce que le mur est le cas que l'on imagine d'abord. Mais le signe de l'ébranlement réfléchi dépend de la nature de l'extrémité, fixe ou libre.
:::

::: propriete
**Ce qui reste vrai** — Un ébranlement réfléchi a une amplitude comparable à celle de l'ébranlement incident (ici la même, l'amortissement étant négligeable). La réflexion sur une extrémité libre se fait sans changement de signe ; sur une extrémité fixe, avec changement de signe. Cas limite : l'ébranlement réfléchi repart toujours vers la source, dans le sens opposé à celui de l'ébranlement incident.
:::

::: verifie À toi : un creux sur une extrémité fixe
Sur une corde AB de longueur 4,5 m, où la célérité vaut 5,0 m/s, un creux de 3,0 cm part de A vers l'extrémité B, qui est fixe. Quel est l'ébranlement réfléchi, et au bout de quelle durée est-il de retour en A ?

---

La réflexion sur une extrémité fixe change le signe : le creux de 3,0 cm repart sous forme d'une bosse de 3,0 cm. Il revient en A après 2 × AB/v = 2 × 4,5/5,0 = 1,8 s.
:::

::: retenir
L'ébranlement réfléchi garde l'amplitude de l'incident ; il change de signe sur une extrémité fixe et non sur une extrémité libre.
:::

## 🪞 La réflexion d'une onde : λ′ = λ et i = i′

Dans la cuve, une plaque de plastique plane P est immergée en partie : les rides rectilignes de la lame arrivent obliquement sur elle. On voit apparaître, en plus des rides incidentes, d'autres rides rectilignes de l'autre côté de la normale à la plaque.
Quelle règle lie la direction et l'écartement de ces rides à ceux des rides incidentes ?

::: definition
**Réflexion d'une onde plane** — Une onde plane qui rencontre un obstacle plan donne naissance à une onde plane réfléchie. L'**angle d'incidence** i est l'angle entre la direction de l'onde incidente et la normale à l'obstacle au point d'incidence I ; l'**angle de réflexion** i′ est l'angle entre la direction de l'onde réfléchie et la même normale.
:::

::: figure Onde plane incidente (crêtes vertes) sur un obstacle plan sous l'incidence i = 40° ; les crêtes réfléchies (rouges) sont symétriques par rapport à la normale (pointillés) ; les flèches orange donnent les directions de propagation
<svg viewBox="0 0 340 210"><title>Onde plane qui arrive sur un obstacle plan sous l'incidence i = 40° et onde réfléchie sous l'angle i′ = i : les crêtes sont perpendiculaires aux directions de propagation</title><line x1="40" y1="176" x2="300" y2="176" stroke="#0f172a" stroke-width="4"/><line x1="44" y1="176" x2="36" y2="185" stroke="#0f172a" stroke-width="1.3"/><line x1="56" y1="176" x2="48" y2="185" stroke="#0f172a" stroke-width="1.3"/><line x1="68" y1="176" x2="60" y2="185" stroke="#0f172a" stroke-width="1.3"/><line x1="80" y1="176" x2="72" y2="185" stroke="#0f172a" stroke-width="1.3"/><line x1="92" y1="176" x2="84" y2="185" stroke="#0f172a" stroke-width="1.3"/><line x1="104" y1="176" x2="96" y2="185" stroke="#0f172a" stroke-width="1.3"/><line x1="116" y1="176" x2="108" y2="185" stroke="#0f172a" stroke-width="1.3"/><line x1="128" y1="176" x2="120" y2="185" stroke="#0f172a" stroke-width="1.3"/><line x1="140" y1="176" x2="132" y2="185" stroke="#0f172a" stroke-width="1.3"/><line x1="152" y1="176" x2="144" y2="185" stroke="#0f172a" stroke-width="1.3"/><line x1="164" y1="176" x2="156" y2="185" stroke="#0f172a" stroke-width="1.3"/><line x1="176" y1="176" x2="168" y2="185" stroke="#0f172a" stroke-width="1.3"/><line x1="188" y1="176" x2="180" y2="185" stroke="#0f172a" stroke-width="1.3"/><line x1="200" y1="176" x2="192" y2="185" stroke="#0f172a" stroke-width="1.3"/><line x1="212" y1="176" x2="204" y2="185" stroke="#0f172a" stroke-width="1.3"/><line x1="224" y1="176" x2="216" y2="185" stroke="#0f172a" stroke-width="1.3"/><line x1="236" y1="176" x2="228" y2="185" stroke="#0f172a" stroke-width="1.3"/><line x1="248" y1="176" x2="240" y2="185" stroke="#0f172a" stroke-width="1.3"/><line x1="260" y1="176" x2="252" y2="185" stroke="#0f172a" stroke-width="1.3"/><line x1="272" y1="176" x2="264" y2="185" stroke="#0f172a" stroke-width="1.3"/><line x1="284" y1="176" x2="276" y2="185" stroke="#0f172a" stroke-width="1.3"/><line x1="296" y1="176" x2="288" y2="185" stroke="#0f172a" stroke-width="1.3"/><text x="300" y="202" text-anchor="end" fill="#0f172a" font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">obstacle plan</text><line x1="170" y1="176" x2="170" y2="50" stroke="#64748b" stroke-width="1.4" stroke-dasharray="6 4"/><text x="174" y="48" text-anchor="start" fill="#64748b" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">normale</text><line x1="131.27" y1="156.29" x2="157.31" y2="134.43" stroke="#0f6e56" stroke-width="2.2"/><line x1="105.55" y1="125.64" x2="131.6" y2="103.79" stroke="#0f6e56" stroke-width="2.2"/><line x1="182.69" y1="134.43" x2="208.73" y2="156.29" stroke="#c2410c" stroke-width="2.2"/><line x1="208.4" y1="103.79" x2="234.45" y2="125.64" stroke="#c2410c" stroke-width="2.2"/><line x1="98.01" y1="90.2" x2="165.37" y2="170.48" stroke="#d97706" stroke-width="1.8"/><polygon points="168.07,173.7 161.32,170.23 165.82,166.45" fill="#d97706"/><line x1="171.93" y1="173.7" x2="239.29" y2="93.42" stroke="#d97706" stroke-width="1.8"/><polygon points="241.99,90.2 239.74,97.46 235.24,93.68" fill="#d97706"/><polyline points="150.72,153.02 152.37,151.73 154.1,150.56 155.92,149.51 157.8,148.59 159.74,147.81 161.73,147.16 163.76,146.66 165.82,146.29 167.91,146.07 170,146" fill="none" stroke="#d97706" stroke-width="1.6" stroke-linejoin="round"/><polyline points="170,146 172.09,146.07 174.18,146.29 176.24,146.66 178.27,147.16 180.26,147.81 182.2,148.59 184.08,149.51 185.9,150.56 187.63,151.73 189.28,153.02" fill="none" stroke="#d97706" stroke-width="1.6" stroke-linejoin="round"/><text x="156" y="138" text-anchor="middle" fill="#d97706" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">i</text><text x="186" y="138" text-anchor="middle" fill="#d97706" font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">i′</text><circle cx="170" cy="176" r="3" fill="#d97706" stroke="#0f172a" stroke-width="1"/><text x="94" y="76" text-anchor="middle" fill="#0f6e56" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">onde incidente</text><text x="256" y="78" text-anchor="middle" fill="#c2410c" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">onde réfléchie</text></svg>
:::

Sur la figure, i et i′ se mesurent avec la normale, et non avec la surface de l'obstacle ; les crêtes sont perpendiculaires aux directions de propagation.

::: exemple Mesurer i, puis prévoir l'onde réfléchie (N = 14 Hz ; rides espacées de 1,8 cm)

1. Les rides incidentes font un angle de 35° avec la plaque. La direction de propagation est perpendiculaire aux rides et la normale perpendiculaire à la plaque : l'angle des rides avec la plaque est donc égal à l'angle i entre la direction et la normale. Ainsi i = 35°.
2. L'onde réfléchie vérifie i′ = i = 35° ; ses rides font elles aussi 35° avec la plaque, de l'autre côté de la normale.
3. Leur écartement reste 1,8 cm : λ′ = λ, car le milieu et la fréquence ne changent pas, donc v = λ·N = 0,018 × 14 = 0,25 m/s est inchangée.

:::

::: figure Amplitude du signal reçu par le récepteur R en fonction de l'angle i′, l'émetteur E étant fixé à i = 30° ; le maximum est repéré en pointillés orange
<svg viewBox="0 0 340 226"><title>Amplitude du signal reçu par le récepteur en fonction de l'angle i′, pour un émetteur fixé à i = 30°</title><line x1="50" y1="186" x2="50" y2="36" stroke="#e2e8f0" stroke-width="1"/><text x="50" y="200" text-anchor="middle" fill="#0f172a" font-size="10" font-weight="600" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><line x1="80" y1="186" x2="80" y2="36" stroke="#e2e8f0" stroke-width="1"/><text x="80" y="200" text-anchor="middle" fill="#0f172a" font-size="10" font-weight="600" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">10</text><line x1="110" y1="186" x2="110" y2="36" stroke="#e2e8f0" stroke-width="1"/><text x="110" y="200" text-anchor="middle" fill="#0f172a" font-size="10" font-weight="600" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">20</text><line x1="140" y1="186" x2="140" y2="36" stroke="#e2e8f0" stroke-width="1"/><text x="140" y="200" text-anchor="middle" fill="#0f172a" font-size="10" font-weight="600" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">30</text><line x1="170" y1="186" x2="170" y2="36" stroke="#e2e8f0" stroke-width="1"/><text x="170" y="200" text-anchor="middle" fill="#0f172a" font-size="10" font-weight="600" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">40</text><line x1="200" y1="186" x2="200" y2="36" stroke="#e2e8f0" stroke-width="1"/><text x="200" y="200" text-anchor="middle" fill="#0f172a" font-size="10" font-weight="600" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">50</text><line x1="230" y1="186" x2="230" y2="36" stroke="#e2e8f0" stroke-width="1"/><text x="230" y="200" text-anchor="middle" fill="#0f172a" font-size="10" font-weight="600" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">60</text><line x1="260" y1="186" x2="260" y2="36" stroke="#e2e8f0" stroke-width="1"/><text x="260" y="200" text-anchor="middle" fill="#0f172a" font-size="10" font-weight="600" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">70</text><line x1="290" y1="186" x2="290" y2="36" stroke="#e2e8f0" stroke-width="1"/><text x="290" y="200" text-anchor="middle" fill="#0f172a" font-size="10" font-weight="600" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">80</text><line x1="320" y1="186" x2="320" y2="36" stroke="#e2e8f0" stroke-width="1"/><text x="320" y="200" text-anchor="middle" fill="#0f172a" font-size="10" font-weight="600" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">90</text><line x1="50" y1="186" x2="320" y2="186" stroke="#e2e8f0" stroke-width="1"/><text x="44" y="190" text-anchor="end" fill="#0f172a" font-size="10" font-weight="600" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0,0</text><line x1="50" y1="156" x2="320" y2="156" stroke="#e2e8f0" stroke-width="1"/><text x="44" y="160" text-anchor="end" fill="#0f172a" font-size="10" font-weight="600" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0,2</text><line x1="50" y1="126" x2="320" y2="126" stroke="#e2e8f0" stroke-width="1"/><text x="44" y="130" text-anchor="end" fill="#0f172a" font-size="10" font-weight="600" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0,4</text><line x1="50" y1="96" x2="320" y2="96" stroke="#e2e8f0" stroke-width="1"/><text x="44" y="100" text-anchor="end" fill="#0f172a" font-size="10" font-weight="600" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0,6</text><line x1="50" y1="66" x2="320" y2="66" stroke="#e2e8f0" stroke-width="1"/><text x="44" y="70" text-anchor="end" fill="#0f172a" font-size="10" font-weight="600" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0,8</text><line x1="50" y1="36" x2="320" y2="36" stroke="#e2e8f0" stroke-width="1"/><text x="44" y="40" text-anchor="end" fill="#0f172a" font-size="10" font-weight="600" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1,0</text><line x1="50" y1="186" x2="326" y2="186" stroke="#0f172a" stroke-width="1.8"/><line x1="50" y1="186" x2="50" y2="28" stroke="#0f172a" stroke-width="1.8"/><text x="185" y="216" text-anchor="middle" fill="#0f172a" font-size="11" font-weight="600" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">i′ (degrés)</text><text x="52" y="24" text-anchor="start" fill="#0f172a" font-size="11" font-weight="600" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">amplitude (mV)</text><polyline points="50,114 65,96 95,69 110,60 125,51 140,48 155,52.5 170,58.5 185,69 215,97.5 230,112.5 260,129 290,162 320,171" fill="none" stroke="#0f6e56" stroke-width="1.6" stroke-linejoin="round"/><circle cx="50" cy="114" r="3.4" fill="#0f6e56" stroke="#0f172a" stroke-width="1"/><circle cx="65" cy="96" r="3.4" fill="#0f6e56" stroke="#0f172a" stroke-width="1"/><circle cx="95" cy="69" r="3.4" fill="#0f6e56" stroke="#0f172a" stroke-width="1"/><circle cx="110" cy="60" r="3.4" fill="#0f6e56" stroke="#0f172a" stroke-width="1"/><circle cx="125" cy="51" r="3.4" fill="#0f6e56" stroke="#0f172a" stroke-width="1"/><circle cx="140" cy="48" r="3.4" fill="#0f6e56" stroke="#0f172a" stroke-width="1"/><circle cx="155" cy="52.5" r="3.4" fill="#0f6e56" stroke="#0f172a" stroke-width="1"/><circle cx="170" cy="58.5" r="3.4" fill="#0f6e56" stroke="#0f172a" stroke-width="1"/><circle cx="185" cy="69" r="3.4" fill="#0f6e56" stroke="#0f172a" stroke-width="1"/><circle cx="215" cy="97.5" r="3.4" fill="#0f6e56" stroke="#0f172a" stroke-width="1"/><circle cx="230" cy="112.5" r="3.4" fill="#0f6e56" stroke="#0f172a" stroke-width="1"/><circle cx="260" cy="129" r="3.4" fill="#0f6e56" stroke="#0f172a" stroke-width="1"/><circle cx="290" cy="162" r="3.4" fill="#0f6e56" stroke="#0f172a" stroke-width="1"/><circle cx="320" cy="171" r="3.4" fill="#0f6e56" stroke="#0f172a" stroke-width="1"/><line x1="140" y1="186" x2="140" y2="36" stroke="#d97706" stroke-width="1.6" stroke-dasharray="5 3"/><text x="145" y="178" text-anchor="start" fill="#d97706" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">i = 30°</text></svg>
:::

Sur le graphique, chaque point est une mesure de l'amplitude du microphone R relié à un oscilloscope, un émetteur de son E (haut-parleur) étant fixé à i = 30° devant l'obstacle plan.

::: exemple Réfléchir une onde sonore sur un obstacle plan (i = 30°)

1. L'amplitude vaut 0,48 mV pour i′ = 0°, croît (0,78 mV à 15°, 0,90 mV à 25°) jusqu'à 0,92 mV pour i′ = 30°, puis décroît (0,85 mV à 40°) jusqu'à 0,10 mV à 90°.
2. Le maximum est atteint pour i′ = 30° = i : la direction de l'onde sonore réfléchie vérifie i′ = i, comme dans la cuve.
3. Le signal n'est pas nul en dehors de cette direction : l'onde sonore n'est pas un faisceau infiniment fin, elle subit un peu de diffraction. On la limite en travaillant à des fréquences de l'ordre du mégahertz : λ = v/N = 340/10⁶ = 3,4 × 10⁻⁴ m, très petite devant l'obstacle.

:::

::: piege
**Erreur : mesurer i entre le rayon incident et la surface de l'obstacle.** Un rayon qui fait 25° avec la plaque a un angle d'incidence i = 90° − 25° = 65°, pas 25°. L'erreur tente parce que la surface est la ligne la plus visible du schéma. Mais la loi i = i′ se formule avec la normale : sur la figure, i est compté à partir de la ligne en pointillés.
:::

::: propriete
**Ce qui reste vrai** — Une onde plane réfléchie sur un obstacle plan vérifie λ′ = λ et i′ = i, ce qui rappelle la seconde loi de Descartes pour la lumière. Condition : les dimensions de l'obstacle doivent être très supérieures à λ ; sinon l'onde le contourne et c'est la diffraction qui l'emporte. Cas limite : dans une pièce vide, les murs sont très grands devant λ et réfléchissent le son, ce qui fait « résonner » la pièce ; des meubles de l'ordre du mètre, voisins de λ, diffractent les sons, et les tissus, tapis ou tentures absorbent plutôt qu'ils ne réfléchissent.
:::

::: verifie À toi : un émetteur d'ultrasons
Un émetteur ultrasonore de fréquence 40 kHz envoie dans l'air (v = 340 m/s) un faisceau sur un mur plan sous l'incidence i = 25°. Sous quel angle faut-il placer le récepteur pour recevoir le signal maximal, et le mur de 3 m de côté est-il bien un obstacle pour cette onde ?

---

Le signal est maximal pour i′ = i = 25°. La longueur d'onde est λ = v/N = 340/(4,0 × 10⁴) = 8,5 × 10⁻³ m = 8,5 mm, très petite devant 3 m : le mur est un grand obstacle, la diffraction est négligeable et la loi i′ = i s'applique.
:::

::: retenir
Une onde plane réfléchie sur un obstacle plan garde sa longueur d'onde et vérifie i′ = i, angles comptés avec la normale ; l'obstacle doit être grand devant λ.
:::

## 🔀 La réfraction d'une onde mécanique : λ₁ sin i₂ = λ₂ sin i₁

Dans la cuve, une plaque de plexiglas posée au fond diminue la profondeur d'eau dans une moitié de la cuve. La lame vibrante envoie des rides rectilignes qui passent du milieu 1 (eau profonde) au milieu 2 (eau peu profonde) ; la surface de séparation est notée σ. Les rides sont plus serrées dans le milieu 2.
Qu'est-ce qui change au passage, et qu'est-ce qui reste identique ?

::: definition
**Transmission et réfraction** — Quand une onde passe d'un milieu 1 à un milieu 2, sa fréquence N, imposée par la source, ne change pas, mais sa célérité change, donc sa longueur d'onde (v = λ·N). Si l'onde arrive perpendiculairement à σ, sa direction ne change pas : c'est une simple **transmission**, et l'onde est dite **transmise**. Si elle arrive sous une incidence oblique i₁, sa direction change : c'est la **réfraction**, l'onde est dite **réfractée** et i₂ est l'angle de réfraction (comme i₁, il se compte avec la normale à σ).
:::

::: figure Rides rectilignes qui passent du milieu 1 (crêtes vertes) au milieu 2 (crêtes rouges) à travers la surface de séparation σ, avec i₁ = 30° ; les points I et I′ sont deux points voisins de σ, et les rides sont plus serrées (λ₂ < λ₁) dans le milieu 2
<svg viewBox="0 0 340 220"><title>Rides qui traversent une surface de séparation σ : λ₁ dans le milieu 1, λ₂ dans le milieu 2, angles i₁ = 30° et i₂ = 22,0°</title><line x1="14" y1="118" x2="326" y2="118" stroke="#0f172a" stroke-width="3"/><text x="322" y="112" text-anchor="end" fill="#0f172a" font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">σ</text><text x="24" y="26" text-anchor="start" fill="#0f172a" font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">milieu 1</text><text x="24" y="204" text-anchor="start" fill="#0f172a" font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">milieu 2</text><line x1="150" y1="34" x2="150" y2="204" stroke="#64748b" stroke-width="1.4" stroke-dasharray="6 4"/><text x="154" y="40" text-anchor="start" fill="#64748b" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">normale</text><line x1="70" y1="118" x2="121.96" y2="88" stroke="#0f6e56" stroke-width="2.2"/><line x1="70" y1="118" x2="5.11" y2="144.25" stroke="#c2410c" stroke-width="2.2"/><line x1="150" y1="118" x2="201.96" y2="88" stroke="#0f6e56" stroke-width="2.2"/><line x1="150" y1="118" x2="85.11" y2="144.25" stroke="#c2410c" stroke-width="2.2"/><line x1="230" y1="118" x2="281.96" y2="88" stroke="#0f6e56" stroke-width="2.2"/><line x1="230" y1="118" x2="165.11" y2="144.25" stroke="#c2410c" stroke-width="2.2"/><line x1="102.5" y1="35.73" x2="146.4" y2="111.76" stroke="#d97706" stroke-width="1.8"/><polygon points="148.5,115.4 142.45,110.81 147.55,107.87" fill="#d97706"/><line x1="151.12" y1="120.78" x2="184.05" y2="202.17" stroke="#d97706" stroke-width="1.8"/><polygon points="185.62,206.07 180.27,200.68 185.73,198.48" fill="#d97706"/><polyline points="132,86.82 133.66,85.92 135.36,85.11 137.1,84.39 138.88,83.76 140.68,83.23 142.52,82.79 144.37,82.44 146.24,82.2 148.12,82.05 150,82" fill="none" stroke="#d97706" stroke-width="1.6" stroke-linejoin="round"/><polyline points="163.5,151.37 162.21,151.87 160.9,152.31 159.57,152.7 158.23,153.05 156.88,153.34 155.51,153.58 154.14,153.76 152.76,153.89 151.38,153.97 150,154" fill="none" stroke="#d97706" stroke-width="1.6" stroke-linejoin="round"/><text x="124" y="74" text-anchor="middle" fill="#d97706" font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">i₁</text><text x="151.8" y="174" text-anchor="start" fill="#d97706" font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">i₂</text><circle cx="150" cy="118" r="3" fill="#d97706" stroke="#0f172a" stroke-width="1"/><circle cx="230" cy="118" r="3" fill="#d97706" stroke="#0f172a" stroke-width="1"/><text x="142" y="134" text-anchor="end" fill="#0f172a" font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">I</text><text x="236" y="134" text-anchor="start" fill="#0f172a" font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">I′</text><line x1="188.97" y1="95.5" x2="170.47" y2="63.46" stroke="#0f172a" stroke-width="1.4"/><polygon points="168.97,60.86 173.29,64.14 169.65,66.24" fill="#0f172a"/><polygon points="188.97,95.5 184.65,92.22 188.29,90.12" fill="#0f172a"/><text x="200.97" y="89.5" text-anchor="start" fill="#0f172a" font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">λ₁</text><line x1="108.28" y1="134.88" x2="118.41" y2="159.9" stroke="#0f172a" stroke-width="1.4"/><polygon points="119.53,162.69 115.71,158.84 119.61,157.26" fill="#0f172a"/><polygon points="108.28,134.88 112.11,138.72 108.21,140.3" fill="#0f172a"/><text x="100.28" y="150.88" text-anchor="end" fill="#0f172a" font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">λ₂</text></svg>
:::

Sur la figure, la distance entre deux crêtes consécutives est λ₁ dans le milieu 1 et λ₂ dans le milieu 2, et chaque crête prolonge celle de l'autre milieu au même point de σ.

::: exemple De l'eau profonde à l'eau peu profonde (N = 20 Hz ; v₁ = 0,32 m/s ; v₂ = 0,24 m/s)

1. λ₁ = v₁/N = 0,32/20 = 1,6 cm et λ₂ = v₂/N = 0,24/20 = 1,2 cm : N est la même des deux côtés, et λ varie comme v.
2. À l'incidence normale (i₁ = 0), l'onde est simplement transmise : sa direction ne change pas, seules v et λ changent.
3. Pour i₁ = 30°, λ₁ sin i₂ = λ₂ sin i₁ donne sin i₂ = (λ₂/λ₁) sin i₁ = 0,75 × 0,50 = 0,375, donc i₂ = 22,0°.
4. i₂ < i₁ : en entrant dans le milieu où elle est plus lente, l'onde se rapproche de la normale.

:::

::: piege
**Erreur : retourner le rapport des longueurs d'onde.** Avec sin i₂ = (λ₁/λ₂) sin i₁ = 1,33 × 0,50 = 0,667, on trouverait i₂ = 41,8°, plus grand que i₁ alors que l'onde ralentit. L'erreur tente parce qu'on hésite sur le sens du rapport. Mais le contrôle est simple : λ₂ < λ₁ doit donner un angle i₂ plus petit que i₁.
:::

::: propriete
**Ce qui reste vrai** — Au niveau de σ, l'onde subit un changement de direction et de longueur d'onde, et la réfraction suit λ₁ sin i₂ = λ₂ sin i₁. En effet, la distance II′ entre deux points voisins de σ vérifie II′ sin i₁ = λ₁ du côté 1 et II′ sin i₂ = λ₂ du côté 2 ; le quotient des deux donne λ₁/λ₂ = sin i₁/sin i₂. Avec λ = v·T, la même période T des deux côtés conduit à sin i₁/v₁ = sin i₂/v₂, la seconde loi de Descartes. Dans la cuve, la célérité est plus grande dans la zone la plus profonde. Cas limite : à l'incidence normale, i₁ = 0 donne i₂ = 0.
:::

::: verifie À toi : de l'eau peu profonde vers l'eau profonde
Une onde passe d'une zone où v₁ = 0,15 m/s vers une zone plus profonde où v₂ = 0,24 m/s, sous l'incidence i₁ = 20°. Calculer i₂ et dire si l'onde se rapproche ou s'écarte de la normale.

---

sin i₂ = (v₂/v₁) sin i₁ = (0,24/0,15) × sin 20° = 1,6 × 0,342 = 0,547, donc i₂ = 33,2°. L'onde entre dans le milieu où elle est plus rapide : i₂ > i₁, elle s'écarte de la normale.
:::

::: retenir
Au passage d'un milieu à l'autre, N reste, v et λ changent dans le même rapport, et sin i₁/v₁ = sin i₂/v₂ ; incidence normale : simple transmission.
:::

## 🌈 La dispersion de la lumière : mono- et polychromatique

Un laser He-Ne traverse un prisme de verre : la tache sur l'écran est déplacée, mais reste une tache rouge. Avec une lampe à lumière blanche (source, fente, lentille, prisme, écran), le même prisme donne une bande colorée qui va du rouge au violet.
Qu'est-ce qui distingue les deux faisceaux ?

::: definition
**Lumière monochromatique, polychromatique, dispersion** — Une lumière **monochromatique** n'est constituée que d'une seule radiation, caractérisée par sa fréquence ν et sa longueur d'onde dans le vide λ₀. Une lumière **polychromatique** est constituée de plusieurs radiations ; la lumière blanche en contient une infinité, du rouge au violet, et forme un spectre continu. Un prisme ne dévie pas toutes ces radiations du même angle D : c'est la **dispersion** de la lumière blanche, et la déviation d'une radiation dépend de sa fréquence ν.
:::

::: figure Un faisceau de lumière blanche traverse un prisme de verre : la lumière est déviée deux fois, à l'entrée puis à la sortie (air/verre/air), et le spectre qui sort va du rouge, le moins dévié, au bleu, le plus dévié
<svg viewBox="0 0 340 240"><title>Un faisceau de lumière blanche traverse un prisme de verre et ressort étalé en un spectre : le rouge est le moins dévié, le bleu le plus dévié</title><polygon points="170,34 94,170 246,170" fill="#e0f2fe" fill-opacity="0.7" stroke="#0f172a" stroke-width="2.2"/><line x1="24" y1="72.33" x2="123.67" y2="107.21" stroke="#0f172a" stroke-width="2.6"/><polygon points="128.2,108.8 119.54,109.33 121.76,102.99" fill="#0f172a"/><text x="70" y="62.33" text-anchor="middle" fill="#0f172a" font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">lumière blanche</text><line x1="128.2" y1="108.8" x2="211.8" y2="108.8" stroke="#475569" stroke-width="2.2"/><line x1="211.8" y1="108.8" x2="289.98" y2="132.25" stroke="#c2410c" stroke-width="2.2"/><polygon points="294,133.46 286.45,134.26 288.14,128.63" fill="#c2410c"/><text x="308" y="137.46" text-anchor="start" fill="#c2410c" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">rouge</text><line x1="211.8" y1="108.8" x2="290.18" y2="144.86" stroke="#15803d" stroke-width="2.2"/><polygon points="294,146.61 286.41,146.36 288.87,141.02" fill="#15803d"/><text x="308" y="150.61" text-anchor="start" fill="#15803d" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">vert</text><line x1="211.8" y1="108.8" x2="290.43" y2="157.55" stroke="#1d4ed8" stroke-width="2.2"/><polygon points="294,159.76 286.5,158.57 289.6,153.58" fill="#1d4ed8"/><text x="308" y="163.76" text-anchor="start" fill="#1d4ed8" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">bleu</text><line x1="300" y1="70" x2="300" y2="214" stroke="#0f172a" stroke-width="3"/><text x="300" y="232" text-anchor="middle" fill="#0f172a" font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">écran</text><text x="170" y="190" text-anchor="middle" fill="#0f172a" font-size="12" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">prisme</text></svg>
:::

Sur le schéma, le rayon blanc se sépare en rayons colorés qui ne sont pas déviés du même angle ; le bleu s'éloigne le plus de la direction d'incidence.

Indices d'un verre pour cinq radiations (ν : fréquence, λ₀ : longueur d'onde dans le vide) :

| Couleur      | ν (10¹⁴ Hz) | λ₀ (10⁻⁶ m) | Indice n |
| ------------ | ----------- | ----------- | -------- |
| rouge sombre | 3,91        | 0,767       | 1,511    |
| rouge        | 4,57        | 0,656       | 1,514    |
| jaune        | 5,10        | 0,588       | 1,517    |
| bleu vert    | 6,18        | 0,485       | 1,520    |
| bleu sombre  | 6,92        | 0,433       | 1,528    |

Dans le tableau, l'indice n augmente quand la fréquence augmente, donc du rouge sombre au bleu sombre.

::: exemple Comparer la déviation du rouge sombre et du bleu sombre (hémicylindre de verre ; i = 45°)

1. Le faisceau arrive en I, centre de la face plane de l'hémicylindre. Les lois de Descartes donnent sin i = n sin r, car l'indice de l'air vaut 1.
2. Rouge sombre (n = 1,511) : sin r = 0,7071/1,511 = 0,4680, donc r = 27,90°.
3. Bleu sombre (n = 1,528) : sin r = 0,7071/1,528 = 0,4628, donc r = 27,57°.
4. Le rayon sort de l'hémicylindre selon un rayon, sans nouvelle déviation : D = i − r, soit 17,10° pour le rouge sombre et 17,43° pour le bleu sombre.
5. Le bleu sombre est plus dévié, d'environ 0,3° : l'indice du verre n'est pas le même pour les deux radiations.

:::

::: piege
**Erreur : croire que la radiation de plus grande longueur d'onde est la plus déviée.** Le rouge sombre a la plus grande longueur d'onde du tableau (0,767 µm), et c'est la moins déviée (17,10° contre 17,43°, étape 4). L'erreur tente parce qu'on associe « plus grand » à « plus loin ». Mais la déviation croît avec l'indice n, et n croît avec la fréquence ν, donc décroît quand λ₀ augmente.
:::

::: propriete
**Ce qui reste vrai** — La lumière blanche est polychromatique : elle résulte de la superposition d'une infinité de radiations, du rouge au violet. Dans le verre, l'indice augmente du rouge au bleu, donc le bleu est plus dévié que le rouge. Une lumière monochromatique est seulement déviée, sans être étalée. Cas limite : sous l'incidence i = 0, sin r = 0 pour toutes les radiations, donc il n'y a ni déviation ni dispersion sur la face plane.
:::

::: verifie À toi : le bleu vert
Même hémicylindre, mais i = 35° et une radiation bleu vert d'indice n = 1,520. Calculer r et D, puis comparer à la radiation rouge (n = 1,514), dont la déviation vaut D = 12,74°.

---

sin r = sin 35°/1,520 = 0,5736/1,520 = 0,3773, donc r = 22,17° et D = 35 − 22,17 = 12,83°. D(bleu vert) = 12,83° est plus grande que D(rouge) = 12,74° : son indice est plus grand, donc r est plus petit et la déviation plus grande.
:::

::: retenir
La lumière blanche est polychromatique : un prisme dévie chaque radiation d'un angle différent (dispersion), le bleu plus que le rouge ; une lumière monochromatique est seulement déviée.
:::

## 🔬 Le milieu dispersif : quand la célérité dépend de la fréquence

Dans le verre, l'indice n n'est pas le même pour toutes les couleurs, et n est relié à la célérité de la lumière. Une onde mécanique peut-elle aussi être « dispersée » ?
La célérité dépend-elle de la fréquence, que devient la longueur d'onde dans le verre, et comment le vérifier avec des rides ?

::: definition
**Milieu dispersif** — Un milieu est **dispersif** pour une onde de fréquence N (ou ν) lorsque la célérité v de cette onde ne dépend pas uniquement des propriétés du milieu, mais aussi de la fréquence ; si v est indépendante de la fréquence, le milieu est **non dispersif**. Pour une radiation de fréquence ν qui entre dans un milieu transparent d'indice n, sa fréquence ne change pas, sa célérité devient v = c/n et sa longueur d'onde λ = v/ν = λ₀/n :

$$ v = c/n $$

$$ λ = v/ν = λ₀/n $$

Le verre est un milieu dispersif pour la lumière : sa célérité dépend de ν.
:::

::: figure Indice n du verre en fonction de la fréquence ν : les cinq points du tableau montent du rouge sombre (ν = 3,91 × 10¹⁴ Hz) au bleu sombre (ν = 6,92 × 10¹⁴ Hz)
<svg viewBox="0 0 340 216"><title>Indice n du verre en fonction de la fréquence ν : cinq points qui montent du rouge sombre au bleu sombre</title><line x1="60" y1="176" x2="60" y2="26" stroke="#e2e8f0" stroke-width="1"/><text x="60" y="190" text-anchor="middle" fill="#0f172a" font-size="10" font-weight="600" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">3</text><line x1="100" y1="176" x2="100" y2="26" stroke="#e2e8f0" stroke-width="1"/><text x="100" y="190" text-anchor="middle" fill="#0f172a" font-size="10" font-weight="600" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4</text><line x1="140" y1="176" x2="140" y2="26" stroke="#e2e8f0" stroke-width="1"/><text x="140" y="190" text-anchor="middle" fill="#0f172a" font-size="10" font-weight="600" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">5</text><line x1="180" y1="176" x2="180" y2="26" stroke="#e2e8f0" stroke-width="1"/><text x="180" y="190" text-anchor="middle" fill="#0f172a" font-size="10" font-weight="600" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">6</text><line x1="220" y1="176" x2="220" y2="26" stroke="#e2e8f0" stroke-width="1"/><text x="220" y="190" text-anchor="middle" fill="#0f172a" font-size="10" font-weight="600" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">7</text><line x1="60" y1="176" x2="220" y2="176" stroke="#e2e8f0" stroke-width="1"/><text x="54" y="180" text-anchor="end" fill="#0f172a" font-size="10" font-weight="600" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1,505</text><line x1="60" y1="146" x2="220" y2="146" stroke="#e2e8f0" stroke-width="1"/><text x="54" y="150" text-anchor="end" fill="#0f172a" font-size="10" font-weight="600" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1,510</text><line x1="60" y1="116" x2="220" y2="116" stroke="#e2e8f0" stroke-width="1"/><text x="54" y="120" text-anchor="end" fill="#0f172a" font-size="10" font-weight="600" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1,515</text><line x1="60" y1="86" x2="220" y2="86" stroke="#e2e8f0" stroke-width="1"/><text x="54" y="90" text-anchor="end" fill="#0f172a" font-size="10" font-weight="600" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1,520</text><line x1="60" y1="56" x2="220" y2="56" stroke="#e2e8f0" stroke-width="1"/><text x="54" y="60" text-anchor="end" fill="#0f172a" font-size="10" font-weight="600" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1,525</text><line x1="60" y1="26" x2="220" y2="26" stroke="#e2e8f0" stroke-width="1"/><text x="54" y="30" text-anchor="end" fill="#0f172a" font-size="10" font-weight="600" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1,530</text><line x1="60" y1="176" x2="228" y2="176" stroke="#0f172a" stroke-width="1.8"/><line x1="60" y1="176" x2="60" y2="18" stroke="#0f172a" stroke-width="1.8"/><text x="140" y="206" text-anchor="middle" fill="#0f172a" font-size="11" font-weight="600" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">ν (10¹⁴ Hz)</text><text x="62" y="12" text-anchor="start" fill="#0f172a" font-size="11" font-weight="600" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">indice n</text><polyline points="96.4,140 122.8,122 144,104 187.2,86 216.8,38" fill="none" stroke="#64748b" stroke-width="1.4" stroke-linejoin="round"/><circle cx="96.4" cy="140" r="4" fill="#c2410c" stroke="#0f172a" stroke-width="1"/><circle cx="122.8" cy="122" r="4" fill="#c2410c" stroke="#0f172a" stroke-width="1"/><circle cx="144" cy="104" r="4" fill="#d97706" stroke="#0f172a" stroke-width="1"/><circle cx="187.2" cy="86" r="4" fill="#0f766e" stroke="#0f172a" stroke-width="1"/><circle cx="216.8" cy="38" r="4" fill="#1d4ed8" stroke="#0f172a" stroke-width="1"/></svg>
:::

Sur le graphique, n augmente avec ν ; comme v = c/n, la célérité diminue du rouge au bleu dans le verre.

::: exemple La radiation bleu vert dans le verre (ν = 6,18 × 10¹⁴ Hz ; n = 1,520 ; c = 3,00 × 10⁸ m/s)

1. Dans le vide : λ₀ = c/ν = 3,00 × 10⁸/(6,18 × 10¹⁴) = 4,85 × 10⁻⁷ m = 485 nm.
2. Dans le verre : v = c/n = 3,00 × 10⁸/1,520 = 1,97 × 10⁸ m/s, car la lumière est ralentie par le milieu.
3. La fréquence ne change pas : λ = v/ν = 1,97 × 10⁸/(6,18 × 10¹⁴) = 3,19 × 10⁻⁷ m = 319 nm.
4. Contrôle : λ₀/n = 485/1,520 = 319 nm ✓.

:::

::: exemple Les ondes à la surface de l'eau (cuve à ondes, profondeur fixée)

1. On fait varier la fréquence N de la lame, que l'on impose aussi au stroboscope pour immobiliser les rides : N = 10 Hz, 20 Hz, 30 Hz donnent λ = 21 mm, 11 mm, 8 mm.
2. La célérité v = λ·N vaut 0,21 m/s, 0,22 m/s, 0,24 m/s : le milieu est le même, mais v augmente avec N.
3. L'eau est donc un milieu dispersif pour les ondes à sa surface : des ondes de fréquences différentes y avancent à des célérités différentes, et les plus rapides se détachent à l'avant d'une perturbation, comme derrière un bateau. Dans ce tableau, ce sont les plus hautes fréquences.

:::

::: piege
**Erreur : conclure qu'un milieu est dispersif parce que la célérité change quand on change la profondeur.** Dans la cuve, v passe de 0,21 à 0,36 m/s quand l'épaisseur d'eau triple (notion 4) : on pourrait conclure « dispersif ». Mais on a alors changé le milieu, pas la fréquence. Pour juger, on garde le même milieu et on change N : v augmente avec N dans l'exemple précédent, donc l'eau est dispersive pour ces ondes.
:::

::: propriete
**Ce qui reste vrai** — Comme n ≥ 1, on a v ≤ c et λ ≤ λ₀ dans un milieu transparent, la fréquence restant celle de la source. Dans le verre, n augmente avec ν : le bleu est plus lent, donc plus dévié, que le rouge. L'air est un exemple de milieu non dispersif pour les ondes sonores : deux notes de hauteurs différentes émises en même temps sont perçues par l'auditeur au même instant. Cas limite : dans le vide, v = c pour toutes les radiations.
:::

::: verifie À toi : le rouge sombre
Pour la radiation rouge sombre du tableau (ν = 3,91 × 10¹⁴ Hz ; n = 1,511), calculer λ₀, v et λ dans le verre, et comparer v à celle du bleu vert (1,97 × 10⁸ m/s).

---

λ₀ = c/ν = 3,00 × 10⁸/(3,91 × 10¹⁴) = 7,67 × 10⁻⁷ m = 767 nm ; v = c/n = 3,00 × 10⁸/1,511 = 1,99 × 10⁸ m/s ; λ = λ₀/n = 767/1,511 = 508 nm. Sa célérité 1,99 × 10⁸ m/s est plus grande que celle du bleu vert : dans le verre, la fréquence la plus basse est la plus rapide.
:::

::: retenir
Un milieu est dispersif si v dépend de la fréquence : pour la lumière dans un milieu d'indice n, v = c/n et λ = λ₀/n ; le verre et l'eau (ondes de surface) sont dispersifs, l'air (son) ne l'est pas.
:::

> 🏆 Quête franchie, héros ! Tu sais décrire la diffraction d'une onde mécanique et de la lumière, juger sa netteté par le quotient λ/a, calculer L et θ, suivre un ébranlement réfléchi, appliquer i = i′ et la loi de la réfraction d'une onde mécanique, expliquer la dispersion de la lumière blanche et distinguer un milieu dispersif d'un milieu qui ne l'est pas.
