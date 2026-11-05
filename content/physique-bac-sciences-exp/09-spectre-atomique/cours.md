# ⚛️ Spectre atomique — la carte d'identité lumineuse de l'atome

> 💡 «Un atome n'a droit qu'à quelques couleurs, les siennes : lis-les dans un spectre, et tu sais qui est là.»

Au chapitre précédent, un prisme étalait la lumière blanche en un arc-en-ciel continu. Une lampe d'éclairage public au sodium, elle, ne donne qu'une teinte orangée, et la lumière d'une étoile lointaine révèle de quoi elle est faite. Ce chapitre explique pourquoi : l'énergie d'un atome ne prend que certaines valeurs, et chaque saut entre deux valeurs libère ou absorbe une lumière de couleur bien précise.

## 🛰️ Du satellite à l'atome : l'énergie peut-elle varier de façon continue ?

Un satellite d'observation orbite à quelques centaines de kilomètres, un satellite géostationnaire à plusieurs dizaines de milliers : en lui fournissant de l'énergie, on peut le placer à n'importe quelle distance intermédiaire. L'électron d'un atome d'hydrogène est lui aussi attiré par un noyau, et il devrait se comporter de même si les lois de Newton suffisaient.
Peut-on décrire l'atome comme un petit système solaire ?

::: definition
**Énergie d'un système** — Pour un système macroscopique (satellite, avion), l'énergie mécanique (cinétique + potentielle) varie de façon **continue** quand le système échange de l'énergie avec l'extérieur : toutes les valeurs sont permises. Dans l'atome d'hydrogène, le noyau (charge +e) et l'électron (charge −e) s'attirent par la force coulombienne, de valeur :

$$ F = k·e²/r² $$

avec k = 9×10⁹ N·m²·C⁻², e = 1,6×10⁻¹⁹ C la charge élémentaire et r la distance noyau–électron. Le modèle **planétaire** (Rutherford) place l'électron sur une orbite circulaire autour du noyau, comme un satellite autour de la Terre.
:::

::: exemple Force subie par l'électron de l'atome d'hydrogène (r = 5,3×10⁻¹¹ m, ordre de grandeur donné du rayon de l'atome)

1. Le noyau et l'électron portent des charges opposées de valeur e : la force est attractive et vaut F = k·e²/r².
2. e² = (1,6×10⁻¹⁹)² = 2,56×10⁻³⁸ C² et r² = (5,3×10⁻¹¹)² = 2,8×10⁻²¹ m², car on élève au carré le nombre et la puissance de 10.
3. F = 9×10⁹ × 2,56×10⁻³⁸ / 2,8×10⁻²¹ = 8,2×10⁻⁸ N ; contrôle d'unité : N·m²·C⁻² × C² / m² = N ✓.
4. Cette force est dirigée vers le noyau : sur une orbite circulaire, l'électron a une accélération centripète.
5. Or, selon la loi de Maxwell, une charge électrique accélérée rayonne de l'énergie : l'énergie de l'atome diminuerait, r diminuerait, et l'électron finirait par s'écraser sur le noyau. La mécanique de Newton prévoit donc un atome instable, ce que l'observation contredit.

:::

::: piege
**Erreur : conclure que l'orbite est stable parce que la force est centripète.** Pour un satellite neutre, la force de gravitation suffit à expliquer une orbite durable (étape 4). L'erreur tente parce que la force coulombienne a la même forme que la gravitation. Mais l'électron est une charge électrique accélérée : il rayonne, ce que le satellite ne fait pas (étape 5). L'orbite de Newton ne peut donc pas décrire l'atome.
:::

::: propriete
**Ce qui reste vrai** — La mécanique de Newton décrit bien les systèmes macroscopiques, dont l'énergie varie de façon continue ; elle échoue pour l'interaction électron–noyau à l'échelle de l'atome, et il faut une autre idée sur l'énergie (notions 2 et 3). Cas limite : la force F = k·e²/r² est correcte, mais elle varie en 1/r² : si r double, F est divisée par 4.
:::

::: verifie À toi : un électron deux fois plus loin
Le même électron se trouve à r' = 1,06×10⁻¹⁰ m du noyau. Calculer la force F' et la comparer à F = 8,2×10⁻⁸ N.

---

r' = 2r, donc r'² = 4r² et F' = k·e²/r'² = F/4 = 8,2×10⁻⁸ / 4 ≈ 2,05×10⁻⁸ N. Contrôle direct : 9×10⁹ × 2,56×10⁻³⁸ / 1,12×10⁻²⁰ = 2,05×10⁻⁸ N ✓. La force varie en 1/r² : doubler la distance la divise par 4, et non par 2.
:::

::: retenir
L'énergie d'un système macroscopique varie de façon continue ; pour l'atome, la mécanique de Newton prévoit un électron qui rayonne et s'écrase : elle ne suffit pas.
:::

## ⚡ Franck et Hertz : l'atome ne reçoit pas n'importe quelle énergie

On bombarde de la vapeur de mercure, sous faible pression, avec des électrons de même énergie cinétique Ec que l'on augmente peu à peu. Un analyseur placé après la vapeur compte les électrons qui l'atteignent avec l'énergie Ec. Si un atome acceptait n'importe quelle énergie, chaque électron lui en céderait un peu dès le début.
Que mesure-t-on réellement quand Ec augmente ?

::: definition
**Expérience de Franck et Hertz (1914)** — On mesure le rapport Nc/Ne, où Ne est le nombre d'électrons émis par seconde par le canon et Nc le nombre d'électrons comptés par seconde par l'analyseur avec l'énergie Ec. Un choc est **élastique** si l'électron ne cède aucune énergie à l'atome, **inélastique** s'il lui en cède.
:::

::: figure Courbe Nc/Ne = f(Ec) pour le mercure : palier à 1 jusqu'à 4,9 eV, chute brutale en 4,9 eV, puis second palier plus bas (la hauteur du second palier est tracée à titre d'illustration ; seul le seuil 4,9 eV est une donnée)
<svg viewBox="0 0 340 190"><title>Courbe schématique Nc/Ne en fonction de Ec pour la vapeur de mercure : palier à 1 jusqu'à 4,9 eV, chute brutale en 4,9 eV, puis second palier plus bas</title><line x1="50" y1="160" x2="320" y2="160" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><polygon points="320,160 313,156.5 313,163.5" fill="#0f172a"/><line x1="50" y1="160" x2="50" y2="22" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><polygon points="50,20 46.5,27 53.5,27" fill="#0f172a"/><line x1="150" y1="40" x2="150" y2="160" stroke="#94a3b8" stroke-width="1.2" stroke-linecap="round" stroke-dasharray="4 3"/><line x1="50" y1="40" x2="320" y2="40" stroke="#94a3b8" stroke-width="1.0" stroke-linecap="round" stroke-dasharray="2 3"/><path d="M50 40 L150 40 L156 100 L310 100" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><text x="40" y="44" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">1</text><text x="40" y="164" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0</text><text x="150" y="176" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">4,9</text><text x="50" y="176" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">0</text><text x="56" y="16" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">Nc/Ne</text><text x="318" y="152" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">Ec (eV)</text></svg>
:::

Sur la courbe, le palier Nc/Ne = 1 correspond aux chocs élastiques (aucun électron perdu) et la chute en Ec = 4,9 eV marque l'apparition des chocs inélastiques.

::: exemple Lire la courbe et suivre un électron (mercure, seuil 4,9 eV)

1. Pour Ec = 3,0 eV, on lit Nc/Ne = 1 : tous les électrons ressortent avec 3,0 eV, car 3,0 eV < 4,9 eV et l'atome ne peut rien accepter : les chocs sont élastiques.
2. Pour Ec ≥ 4,9 eV, on lit Nc/Ne < 1 : certains électrons ne sont plus comptés avec l'énergie Ec, car ils ont cédé 4,9 eV à un atome de mercure, qui passe à un état excité (chocs inélastiques).
3. Un électron de Ec = 6,5 eV subit un tel choc : par conservation de l'énergie, il repart avec 6,5 − 4,9 = 1,6 eV.
4. Il n'a pas cédé 6,5 eV, ni 1,6 eV, ni 3,0 eV : l'atome n'accepte que 4,9 eV. L'énergie transférée est quantifiée.

:::

::: piege
**Erreur : croire que l'atome absorbe toute l'énergie de l'électron qui le heurte.** Pour Ec = 6,5 eV, on annoncerait un électron qui repart avec 0 eV (étape 3). L'erreur tente parce qu'une chute de Nc/Ne ressemble à « l'électron a été absorbé ». Mais l'atome ne prend que 4,9 eV : le reste, 1,6 eV, demeure de l'énergie cinétique de l'électron.
:::

::: propriete
**Ce qui reste vrai** — Tant que Ec est inférieure à l'énergie minimale que l'atome peut accepter (4,9 eV pour le mercure), les chocs sont élastiques et Nc/Ne = 1. Au-delà, l'atome ne reçoit qu'une valeur particulière, ici 4,9 eV, et l'électron garde le reste en énergie cinétique. L'énergie échangée entre un atome et le milieu extérieur est donc quantifiée. Cas limite : pour Ec = 4,9 eV tout juste, la cession est possible, mais l'électron n'a plus d'énergie cinétique après le choc.
:::

::: verifie À toi : un électron de 5,5 eV
Un électron de Ec = 5,5 eV heurte un atome de mercure au repos dans son état fondamental. Peut-il lui céder de l'énergie ? Avec quelle énergie cinétique repart-il ?

---

Oui, car 5,5 eV ≥ 4,9 eV : le choc peut être inélastique. L'atome ne prend que 4,9 eV, donc l'électron repart avec 5,5 − 4,9 = 0,6 eV d'énergie cinétique, et non avec 0 eV.
:::

::: retenir
Un atome ne reçoit d'un électron que des quantités d'énergie bien précises (4,9 eV pour le mercure) ; en dessous, les chocs sont élastiques.
:::

## 🪜 Niveaux d'énergie : fondamental, états excités, transition

Franck et Hertz ont vu que le mercure accepte 4,9 eV et rien entre 0 et 4,9 eV. Dès 1913, Niels Bohr avait fait un pari : les variations d'énergie d'un atome sont quantifiées, et l'atome n'existe que dans certains états d'énergie bien définis.
Comment représenter ces états, et que veut dire « passer de l'un à l'autre » ?

::: definition
**Niveaux d'énergie** — L'énergie d'un atome ne peut prendre que des valeurs discrètes, propres à l'atome : ce sont ses **niveaux d'énergie** Eₙ, rangés sur un axe vertical. Le niveau le plus bas est l'**état fondamental**, le plus stable ; les niveaux supérieurs sont les **états excités**. Le passage d'un niveau à un autre s'appelle une **transition**. Sa variation d'énergie est ΔE = E(final) − E(initial) : positive si l'atome absorbe de l'énergie, négative s'il en cède.
:::

::: figure Trois niveaux d'un atome : la flèche montante de E₁ à E₃ est une absorption (l'énergie augmente), la flèche descendante de E₃ à E₂ est une émission (l'énergie diminue) ; l'espacement des traits suit les valeurs
<svg viewBox="0 0 340 196"><title>Trois niveaux d'énergie E₁, E₂, E₃ d'un atome : une flèche montante de E₁ à E₃ (absorption) et une flèche descendante de E₃ à E₂ (émission)</title><line x1="30" y1="20" x2="30" y2="176" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><polygon points="30,14 26.5,21 33.5,21" fill="#0f172a"/><text x="36" y="14" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">Énergie</text><line x1="60" y1="62" x2="200" y2="62" stroke="#0f172a" stroke-width="2.6" stroke-linecap="round"/><text x="205" y="66" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">E₃ = −3,0 eV</text><line x1="60" y1="104" x2="200" y2="104" stroke="#0f172a" stroke-width="2.6" stroke-linecap="round"/><text x="205" y="108" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">E₂ = −6,0 eV</text><line x1="60" y1="160" x2="200" y2="160" stroke="#0f172a" stroke-width="2.6" stroke-linecap="round"/><text x="205" y="164" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">E₁ = −10,0 eV</text><text x="130" y="190" text-anchor="middle" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">état fondamental : E₁</text><line x1="90" y1="158" x2="90" y2="69" stroke="#b45309" stroke-width="2.0" stroke-linecap="round"/><polygon points="90,64 86.5,71 93.5,71" fill="#b45309"/><text x="90" y="52" text-anchor="middle" font-size="12" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">absorption</text><line x1="170" y1="64" x2="170" y2="97" stroke="#1d4ed8" stroke-width="2.0" stroke-linecap="round"/><polygon points="170,102 166.5,95 173.5,95" fill="#1d4ed8"/><text x="145" y="82" text-anchor="end" font-size="12" font-weight="700" fill="#1d4ed8" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">émission</text></svg>
:::

Sur le dessin, plus un trait est haut, plus l'énergie est grande ; E₁ = −10,0 eV, le trait le plus bas, est le fondamental.

::: exemple Absorption ou émission ? (E₁ = −10,0 eV ; E₂ = −6,0 eV ; E₃ = −3,0 eV)

1. L'état fondamental est le niveau le plus bas, c'est-à-dire le plus négatif : E₁ = −10,0 eV.
2. De E₁ à E₃, l'énergie passe de −10,0 à −3,0 eV : elle augmente, l'atome doit recevoir ΔE = E₃ − E₁ = +7,0 eV.
3. De E₃ à E₂, elle passe de −3,0 à −6,0 eV : elle diminue, l'atome cède ΔE = E₂ − E₃ = −3,0 eV.
4. Un photon de 6,0 eV ou de 8,0 eV ne convient pas pour aller de E₁ à E₃ : seul un photon d'énergie exactement égale à l'écart, 7,0 eV, est absorbé (un électron, lui, peut céder 7,0 eV et garder le reste).

:::

::: piege
**Erreur : prendre pour fondamental le niveau de plus petite valeur absolue.** On désignerait E₃ = −3,0 eV, parce que 3,0 est le plus petit nombre (étape 1). L'erreur tente parce qu'on lit les énergies sans leur signe. Mais −10,0 eV est inférieur à −3,0 eV : le fondamental est le niveau le plus bas, le plus négatif.
:::

::: propriete
**Ce qui reste vrai** — Chaque atome possède sa propre suite de niveaux. Un atome dans son état fondamental est au plus stable ; un apport d'énergie extérieur (choc, photon) peut le placer dans un état excité. Cas limite : un photon d'énergie inférieure à l'énergie d'ionisation, qui ne correspond à aucun écart entre deux niveaux, n'est pas absorbé (notion 7) ; un électron qui heurte l'atome peut, lui, céder un écart inférieur à son énergie cinétique (notion 2).
:::

::: verifie À toi : un autre atome
Un atome a pour niveaux E₁ = −9,0 eV, E₂ = −5,0 eV, E₃ = −2,5 eV. Quelle énergie faut-il lui fournir pour passer du fondamental à E₃ ? Que se passe-t-il lors de la transition de E₂ à E₁ ?

---

Le fondamental est E₁ (le plus bas). ΔE = E₃ − E₁ = −2,5 − (−9,0) = +6,5 eV : l'énergie augmente, il faut fournir 6,5 eV. De E₂ à E₁, ΔE = −9,0 − (−5,0) = −4,0 eV : l'énergie diminue, l'atome cède 4,0 eV.
:::

::: retenir
L'énergie d'un atome est quantifiée : elle ne prend que les valeurs de ses niveaux, du fondamental (le plus bas) aux états excités ; une transition change l'énergie de ΔE = E(final) − E(initial).
:::

## 💡 Le photon : l'énergie d'une lumière de longueur d'onde λ

Une lampe au sodium éclaire la route d'une lumière orangée de longueur d'onde λ = 589 nm. Pour passer d'un niveau à un autre, un atome échange de l'énergie par paquets de lumière, et un paquet ne transporte pas n'importe quelle énergie.
Comment relier la couleur d'une lumière, donc sa longueur d'onde, à l'énergie d'un de ses paquets ?

::: definition
**Photon** — Une radiation de fréquence ν est un flux de **photons**, particules sans masse et sans charge, d'énergie W = hν, appelée **quantum d'énergie**. Avec ν = c/λ :

$$ W = h·ν = h·c/λ $$

avec h = 6,62×10⁻³⁴ J·s, c = 3,00×10⁸ m/s, et l'électron-volt : 1 eV = 1,6×10⁻¹⁹ J. Lors d'une transition entre deux niveaux, l'énergie échangée est W = |ΔE|. Domaines : ultraviolet (UV) pour λ < 400 nm, visible de 400 nm à 800 nm, infrarouge (IR) au-delà.
:::

::: exemple Énergie d'un photon de la lampe au sodium (λ = 589 nm)

1. λ = 589 nm = 5,89×10⁻⁷ m : on convertit en mètres avant tout calcul, car c est en m/s.
2. ν = c/λ = 3,00×10⁸ / 5,89×10⁻⁷ = 5,09×10¹⁴ Hz, car la fréquence est le quotient de la célérité par la longueur d'onde.
3. W = h·ν = 6,62×10⁻³⁴ × 5,09×10¹⁴ = 3,37×10⁻¹⁹ J, car h est en J·s.
4. W = 3,37×10⁻¹⁹ / 1,6×10⁻¹⁹ = 2,11 eV, car on divise par 1,6×10⁻¹⁹ J pour passer des joules aux électron-volts.
5. Contrôle : λ = h·c/W = 6,62×10⁻³⁴ × 3,00×10⁸ / 3,37×10⁻¹⁹ = 5,89×10⁻⁷ m ✓.

:::

::: piege
**Erreur : utiliser l'énergie en eV directement dans ν = W/h.** On trouverait ν = 2,11 / 6,62×10⁻³⁴ = 3,2×10³³ Hz au lieu de 5,09×10¹⁴ Hz (étape 4), une fréquence absurde pour de la lumière. L'erreur tente parce que l'énoncé donne souvent W en eV. Mais h est en J·s : il faut d'abord convertir W en joules.
:::

::: propriete
**Ce qui reste vrai** — W est proportionnelle à ν et inversement proportionnelle à λ : plus la longueur d'onde est petite, plus le photon est énergétique. Avec h·c = 1,99×10⁻²⁵ J·m, on a λ = h·c/W. Cas limite : un photon visible (de 400 nm à 800 nm) a une énergie comprise entre 1,55 eV et 3,10 eV ; en dehors, il est ultraviolet (plus énergétique) ou infrarouge (moins énergétique).
:::

::: verifie À toi : un photon ultraviolet
Un photon a pour longueur d'onde λ = 300 nm. Calculer son énergie en joules, puis en eV, et préciser son domaine.

---

λ = 300 nm = 3,00×10⁻⁷ m. W = h·c/λ = 6,62×10⁻³⁴ × 3,00×10⁸ / 3,00×10⁻⁷ = 6,62×10⁻¹⁹ J, soit 6,62×10⁻¹⁹ / 1,6×10⁻¹⁹ = 4,14 eV. Comme 300 nm < 400 nm, ce photon est ultraviolet, plus énergétique que ceux du visible (au plus 3,10 eV).
:::

::: retenir
Un photon de fréquence ν et de longueur d'onde λ a pour énergie W = hν = hc/λ ; lors d'une transition, W = |ΔE| (convertir l'eV en J et le nm en m).
:::

## ⚛️ L'atome d'hydrogène : ses niveaux Eₙ = −E₀/n²

Un seul électron, un seul proton : l'hydrogène est l'atome le plus simple, et Bohr a pu proposer un modèle pour lui. Il suppose le noyau fixe (sa masse est 1836 fois celle de l'électron), l'électron sur des orbites circulaires bien déterminées, dites stationnaires, et un échange d'énergie avec l'extérieur seulement quand l'électron passe d'une orbite à une autre.
Quelles énergies ce modèle attribue-t-il à l'atome ?

::: definition
**Niveaux de l'hydrogène** — L'énergie de l'atome d'hydrogène, en eV, vaut :

$$ Eₙ = −E₀/n² $$

avec E₀ = 13,6 eV et n entier supérieur ou égal à 1. Pour n = 1, E₁ = −13,6 eV : c'est l'état fondamental. Pour n > 1, l'atome est dans un état excité. Quand n devient très grand, Eₙ tend vers 0 : l'électron est séparé du proton, l'atome est **ionisé**. L'**énergie d'ionisation** est l'énergie minimale à fournir pour ioniser l'atome.
:::

::: figure Niveaux de l'hydrogène : plus n augmente, plus les niveaux se resserrent vers 0 eV ; la flèche part du fondamental n = 1 jusqu'à l'atome ionisé (espacements non à l'échelle)
<svg viewBox="0 0 360 204"><title>Niveaux d'énergie de l'atome d'hydrogène pour n de 1 à 5 et niveau de l'atome ionisé, avec la flèche d'ionisation depuis le fondamental ; espacements non à l'échelle</title><line x1="30" y1="24" x2="30" y2="196" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><polygon points="30,17 26.5,24 33.5,24" fill="#0f172a"/><text x="36" y="14" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">Énergie (eV)</text><line x1="60" y1="30" x2="220" y2="30" stroke="#0f172a" stroke-width="2.0" stroke-linecap="round" stroke-dasharray="5 3"/><text x="225" y="34" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">n → ∞ : 0 eV (ionisé)</text><line x1="60" y1="58" x2="220" y2="58" stroke="#0f172a" stroke-width="2.6" stroke-linecap="round"/><text x="225" y="62" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">n = 5 : −0,54 eV</text><line x1="60" y1="78" x2="220" y2="78" stroke="#0f172a" stroke-width="2.6" stroke-linecap="round"/><text x="225" y="82" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">n = 4 : −0,85 eV</text><line x1="60" y1="104" x2="220" y2="104" stroke="#0f172a" stroke-width="2.6" stroke-linecap="round"/><text x="225" y="108" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">n = 3 : −1,51 eV</text><line x1="60" y1="138" x2="220" y2="138" stroke="#0f172a" stroke-width="2.6" stroke-linecap="round"/><text x="225" y="142" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">n = 2 : −3,40 eV</text><line x1="60" y1="182" x2="220" y2="182" stroke="#0f172a" stroke-width="2.6" stroke-linecap="round"/><text x="225" y="186" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">n = 1 : −13,6 eV</text><line x1="110" y1="180" x2="110" y2="37" stroke="#b45309" stroke-width="2.0" stroke-linecap="round"/><polygon points="110,32 106.5,39 113.5,39" fill="#b45309"/><text x="98" y="120" text-anchor="end" font-size="12" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">13,6 eV</text><text x="98" y="133" text-anchor="end" font-size="11" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">pour ioniser</text></svg>
:::

Sur le dessin, les énergies sont toutes négatives, et la flèche d'ionisation va de −13,6 eV à 0 eV : elle mesure E₀.

::: exemple Niveaux et ionisation de l'hydrogène

1. Eₙ = −13,6/n², car c'est la formule de Bohr.
2. E₁ = −13,6/1 = −13,60 eV ; E₂ = −13,6/4 = −3,40 eV ; E₃ = −13,6/9 = −1,51 eV ; E₄ = −13,6/16 = −0,85 eV : on divise par n², le carré de n.
3. Les énergies augmentent vers 0 quand n croît : les niveaux se resserrent.
4. Ionisation depuis le fondamental : 0 − (−13,6) = 13,6 eV, soit 13,6 × 1,6×10⁻¹⁹ = 2,18×10⁻¹⁸ J.
5. Depuis n = 2, il suffit de 0 − (−3,40) = 3,40 eV : l'énergie d'ionisation dépend du niveau de départ.

:::

::: piege
**Erreur : diviser par n au lieu de n².** On écrirait E₂ = −13,6/2 = −6,8 eV au lieu de −3,40 eV (étape 2). L'erreur tente parce que n apparaît en bas de la fraction et que le carré s'oublie. Mais Bohr donne −13,6/n² : pour n = 2, le dénominateur vaut 4.
:::

::: propriete
**Ce qui reste vrai** — Pour l'hydrogène, −13,6 eV ≤ Eₙ < 0 : toutes les énergies liées sont négatives, et 0 correspond à l'atome ionisé. Cas limite : n = 1 est le niveau le plus bas ; pour un atome déjà excité, l'énergie d'ionisation est plus petite que 13,6 eV (3,40 eV depuis n = 2).
:::

::: verifie À toi : n = 5
Calculer E₅ et l'énergie à fournir pour ioniser un atome d'hydrogène qui se trouve au niveau n = 3.

---

E₅ = −13,6/5² = −13,6/25 = −0,54 eV, en divisant par n² = 25. Pour n = 3 : E₃ = −13,6/9 = −1,51 eV, donc il faut 0 − (−1,51) = 1,51 eV pour atteindre 0 eV, l'atome ionisé.
:::

::: retenir
Pour l'hydrogène, Eₙ = −13,6/n² (eV) ; le fondamental est E₁ = −13,6 eV, et l'ionisation depuis le fondamental demande 13,6 eV.
:::

## 🌈 Spectres continu, d'émission et d'absorption

Un prisme étale la lumière d'une lampe à incandescence en un arc-en-ciel continu. Placée devant un spectroscope, une lampe à vapeur d'hydrogène ne donne que quelques raies fines. Et si l'on fait traverser de la vapeur d'hydrogène par de la lumière blanche, l'arc-en-ciel se creuse de raies noires.
Que racontent ces trois spectres sur les atomes qui les produisent ?

::: definition
**Spectres** — Un spectroscope disperse la lumière avec un **réseau** ou un prisme. Le **spectre continu** de la lumière blanche contient toutes les couleurs. Le **spectre d'émission** d'une vapeur d'atomes est un spectre de raies : quelques raies colorées fines sur un fond sombre. Le **spectre d'absorption** s'obtient en faisant traverser la vapeur par de la lumière blanche : c'est le spectre continu auquel manquent des raies, qui apparaissent noires (cannelures).
:::

::: figure Hydrogène, même échelle de longueurs d'onde : en émission, quatre raies colorées brillantes sur fond noir ; en absorption, quatre raies noires exactement aux mêmes positions sur le spectre continu
<svg viewBox="0 0 340 158"><title>Spectre d'émission et spectre d'absorption de l'hydrogène dans le visible, à la même échelle de longueurs d'onde : quatre raies colorées brillantes sur fond noir, quatre raies noires aux mêmes positions sur fond continu</title><defs><linearGradient id="sp-a" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#7c3aed"/><stop offset="0.17" stop-color="#2563eb"/><stop offset="0.33" stop-color="#06b6d4"/><stop offset="0.5" stop-color="#22c55e"/><stop offset="0.67" stop-color="#eab308"/><stop offset="0.83" stop-color="#f97316"/><stop offset="1" stop-color="#dc2626"/></linearGradient></defs><rect x="20" y="24" width="300" height="30" fill="#111827" stroke="#0f172a" stroke-width="1.5"/><line x1="30" y1="24" x2="30" y2="54" stroke="#7c3aed" stroke-width="3.0" stroke-linecap="round"/><text x="30" y="17" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">Hδ</text><line x1="54" y1="24" x2="54" y2="54" stroke="#4338ca" stroke-width="3.0" stroke-linecap="round"/><text x="54" y="17" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">Hγ</text><line x1="106" y1="24" x2="106" y2="54" stroke="#2563eb" stroke-width="3.0" stroke-linecap="round"/><text x="106" y="17" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">Hβ</text><line x1="276" y1="24" x2="276" y2="54" stroke="#ea580c" stroke-width="3.0" stroke-linecap="round"/><text x="276" y="17" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">Hα</text><text x="170" y="70" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">émission</text><rect x="20" y="78" width="300" height="30" fill="url(#sp-a)" stroke="#0f172a" stroke-width="1.5"/><line x1="30" y1="78" x2="30" y2="108" stroke="#111827" stroke-width="3.0" stroke-linecap="round"/><line x1="54" y1="78" x2="54" y2="108" stroke="#111827" stroke-width="3.0" stroke-linecap="round"/><line x1="106" y1="78" x2="106" y2="108" stroke="#111827" stroke-width="3.0" stroke-linecap="round"/><line x1="276" y1="78" x2="276" y2="108" stroke="#111827" stroke-width="3.0" stroke-linecap="round"/><text x="170" y="124" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">absorption</text><line x1="20" y1="130" x2="20" y2="136" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><text x="20" y="150" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">400 nm</text><line x1="120" y1="130" x2="120" y2="136" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><text x="120" y="150" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">500 nm</text><line x1="220" y1="130" x2="220" y2="136" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><text x="220" y="150" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">600 nm</text><line x1="320" y1="130" x2="320" y2="136" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><text x="320" y="150" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">700 nm</text></svg>
:::

Sur le dessin, chaque raie noire d'absorption se trouve à la position d'une raie brillante d'émission : c'est le renversement des raies.

::: exemple Identifier un élément par son spectre d'absorption

1. Un spectre d'absorption montre, sur fond continu, trois raies noires à 434 nm, 486 nm et 656 nm.
2. Par le renversement des raies, ces raies noires sont aux positions des raies d'émission du même élément : on compare aux tableaux d'émission.
3. L'hydrogène émet à 410, 434, 486 et 656 nm : les trois valeurs y figurent. L'hélium (447, 502, 588, 668 nm) et le sodium (589 nm) n'ont aucune de ces valeurs.
4. L'élément est l'hydrogène ; la raie à 410 nm n'a simplement pas été relevée. Le spectre joue le rôle de carte d'identité de l'élément.

:::

::: piege
**Erreur : lire une raie noire comme l'absence de l'élément.** On dirait que l'hydrogène manque à 486 nm (étape 3), puisque la raie y est noire. L'erreur tente parce qu'une raie noire ressemble à un « trou » de lumière. Mais ce trou est creusé par les atomes d'hydrogène eux-mêmes, qui absorbent cette radiation : sa présence révèle l'élément.
:::

::: propriete
**Ce qui reste vrai** — Chaque élément chimique a son spectre de raies, en émission comme en absorption, et les deux spectres sont superposables. Le spectre d'un mélange est la superposition des spectres de ses éléments. Interprétation : pour s'exciter, un atome n'absorbe que des photons dont l'énergie est égale à l'écart entre deux de ses niveaux, et en se désexcitant il émet des photons de même énergie, d'où des raies et non un arc-en-ciel continu. Cas limite : une vapeur ne contenant qu'un seul élément peut ne montrer qu'une raie très marquée dans le visible, comme le sodium à 589 nm.
:::

::: verifie À toi : un mélange
Une lampe émet des raies à 410, 434, 486, 589 et 656 nm. L'hydrogène émet à 410, 434, 486 et 656 nm ; le sodium émet à 589 nm. Que contient la lampe ?

---

Les raies 410, 434, 486 et 656 nm sont celles de l'hydrogène. La raie à 589 nm n'appartient pas à l'hydrogène : c'est celle du sodium. Le spectre d'un mélange superpose ceux de ses éléments : la lampe contient de l'hydrogène et du sodium.
:::

::: retenir
Un spectre de raies d'émission ou d'absorption est la carte d'identité d'un élément : les raies noires d'absorption sont aux positions des raies brillantes d'émission.
:::

## 🔬 Les raies de l'hydrogène : calculer la couleur d'une transition

Les niveaux Eₙ de l'hydrogène et l'énergie W = hν d'un photon permettent de prédire les raies que la lampe émet. L'atome n'a pourtant qu'un électron, et la lampe montre quatre raies visibles.
Quelle transition donne la raie rouge, et que se passe-t-il quand un photon arrive sur l'atome au lieu d'en partir ?

::: definition
**Raie d'une transition** — Une raie correspond à une transition entre deux niveaux n < p ; le photon émis ou absorbé porte W = Eₚ − Eₙ = E₀·(1/n² − 1/p²). Une **série** regroupe les raies qui aboutissent au même niveau n : Lyman (n = 1), Balmer (n = 2), Paschen (n = 3), Brackett (n = 4), Pfund (n = 5).
:::

::: exemple Longueur d'onde de la raie rouge : transition de n = 3 à n = 2 (E₀ = 13,6 eV)

1. ΔE = E₂ − E₃ = −3,40 − (−1,51) = −1,89 eV : l'énergie diminue, l'atome émet un photon d'énergie W = |ΔE| = 1,89 eV.
2. En joules : W = 1,89 × 1,6×10⁻¹⁹ = 3,02×10⁻¹⁹ J, car 1 eV = 1,6×10⁻¹⁹ J.
3. λ = h·c/W = 1,99×10⁻²⁵ / 3,02×10⁻¹⁹ = 6,57×10⁻⁷ m = 657 nm, car W = h·c/λ.
4. 657 nm est dans l'intervalle 400 nm à 800 nm : la raie est visible, rouge-orangée. Les valeurs mesurées donnent 656 nm : l'écart d'un nanomètre vient des arrondis de h, de c et de e.

:::

::: methode Une transition entre deux niveaux n < p de l'hydrogène

1. Énergie du photon : W = Eₚ − Eₙ = E₀·(1/n² − 1/p²), positive, en eV.
2. Émission (de p vers n) : l'atome perd W et émet un photon d'énergie W. Absorption (de n vers p) : l'atome absorbe un photon seulement si son énergie est exactement W ; sinon le photon est diffusé.
3. Longueur d'onde : λ = h·c/W, avec W en joules.
4. Si W est au moins égale à l'énergie d'ionisation, le photon peut être absorbé : l'atome est ionisé et l'électron éjecté emporte l'excédent W − Eᵢ (Eᵢ = 13,6 eV depuis le fondamental, 3,40 eV depuis n = 2) en énergie cinétique. Un électron incident de Ec ≥ W peut aussi exciter l'atome par choc.

:::

::: figure Émission de l'hydrogène par séries : les flèches qui arrivent sur n = 1 forment la série de Lyman, sur n = 2 la série de Balmer, sur n = 3 la série de Paschen (espacements non à l'échelle)
<svg viewBox="0 0 310 210"><title>Diagramme des niveaux n = 1 à 5 de l'atome d'hydrogène : flèches d'émission vers n = 1 (série de Lyman), vers n = 2 (série de Balmer) et vers n = 3 (série de Paschen) ; espacements non à l'échelle</title><line x1="40" y1="58" x2="250" y2="58" stroke="#0f172a" stroke-width="2.6" stroke-linecap="round"/><text x="256" y="62" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">n = 5</text><line x1="40" y1="78" x2="250" y2="78" stroke="#0f172a" stroke-width="2.6" stroke-linecap="round"/><text x="256" y="82" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">n = 4</text><line x1="40" y1="104" x2="250" y2="104" stroke="#0f172a" stroke-width="2.6" stroke-linecap="round"/><text x="256" y="108" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">n = 3</text><line x1="40" y1="138" x2="250" y2="138" stroke="#0f172a" stroke-width="2.6" stroke-linecap="round"/><text x="256" y="142" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">n = 2</text><line x1="40" y1="182" x2="250" y2="182" stroke="#0f172a" stroke-width="2.6" stroke-linecap="round"/><text x="256" y="186" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">n = 1</text><line x1="40" y1="30" x2="250" y2="30" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round" stroke-dasharray="5 3"/><text x="256" y="34" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">∞</text><line x1="60" y1="138" x2="60" y2="177" stroke="#7c3aed" stroke-width="1.8" stroke-linecap="round"/><polygon points="60,182 56.5,175 63.5,175" fill="#7c3aed"/><line x1="74" y1="104" x2="74" y2="177" stroke="#7c3aed" stroke-width="1.8" stroke-linecap="round"/><polygon points="74,182 70.5,175 77.5,175" fill="#7c3aed"/><line x1="88" y1="78" x2="88" y2="177" stroke="#7c3aed" stroke-width="1.8" stroke-linecap="round"/><polygon points="88,182 84.5,175 91.5,175" fill="#7c3aed"/><text x="74" y="198" text-anchor="middle" font-size="12" font-weight="700" fill="#7c3aed" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">Lyman</text><line x1="130" y1="104" x2="130" y2="133" stroke="#dc2626" stroke-width="1.8" stroke-linecap="round"/><polygon points="130,138 126.5,131 133.5,131" fill="#dc2626"/><line x1="144" y1="78" x2="144" y2="133" stroke="#dc2626" stroke-width="1.8" stroke-linecap="round"/><polygon points="144,138 140.5,131 147.5,131" fill="#dc2626"/><line x1="158" y1="58" x2="158" y2="133" stroke="#dc2626" stroke-width="1.8" stroke-linecap="round"/><polygon points="158,138 154.5,131 161.5,131" fill="#dc2626"/><text x="144" y="158" text-anchor="middle" font-size="12" font-weight="700" fill="#dc2626" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">Balmer</text><line x1="200" y1="78" x2="200" y2="99" stroke="#0f172a" stroke-width="1.8" stroke-linecap="round"/><polygon points="200,104 196.5,97 203.5,97" fill="#0f172a"/><line x1="214" y1="58" x2="214" y2="99" stroke="#0f172a" stroke-width="1.8" stroke-linecap="round"/><polygon points="214,104 210.5,97 217.5,97" fill="#0f172a"/><text x="207" y="122" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">Paschen</text></svg>
:::

Voici la première raie de chaque série, calculée comme dans l'exemple :

| Série    | Niveau d'arrivée | Première raie | λ calculée | Domaine     |
| -------- | ---------------- | ------------- | ---------- | ----------- |
| Lyman    | n = 1            | 2 → 1         | 122 nm     | ultraviolet |
| Balmer   | n = 2            | 3 → 2         | 657 nm     | visible     |
| Paschen  | n = 3            | 4 → 3         | 1,88 µm    | infrarouge  |
| Brackett | n = 4            | 5 → 4         | 4,06 µm    | infrarouge  |
| Pfund    | n = 5            | 6 → 5         | 7,47 µm    | infrarouge  |

La série de Balmer contient les quatre raies visibles Hα (3 → 2, 657 nm), Hβ (4 → 2, 487 nm), Hγ (5 → 2, 435 nm) et Hδ (6 → 2, 411 nm).

::: exemple Trois photons arrivent sur un atome d'hydrogène fondamental (10,2 eV ; 11,0 eV ; 15,5 eV)

1. À partir de n = 1, les écarts sont E₂ − E₁ = 10,2 eV, E₃ − E₁ = 12,09 eV, E₄ − E₁ = 12,75 eV, et l'ionisation demande 13,6 eV.
2. 10,2 eV est exactement l'écart vers n = 2 : le photon est absorbé et l'atome passe à n = 2.
3. 11,0 eV ne correspond à aucun écart et reste inférieur à 13,6 eV : le photon n'est pas absorbé, il est diffusé avec la même énergie.
4. 15,5 eV dépasse 13,6 eV : le photon est absorbé, l'atome est ionisé, et l'électron éjecté emporte 15,5 − 13,6 = 1,9 eV d'énergie cinétique.

:::

::: piege
**Erreur : prendre l'énergie d'un niveau pour celle du photon.** Pour la transition de 3 à 2, on poserait W = |E₂| = 3,40 eV, d'où λ = 365 nm au lieu de 657 nm (étape 1). L'erreur tente parce que les énergies Eₙ sont celles qu'on vient de calculer. Mais le photon porte l'écart entre deux niveaux, |E₃ − E₂| = 1,89 eV, jamais l'énergie d'un seul niveau.
:::

::: propriete
**Ce qui reste vrai** — Émission et absorption entre les mêmes niveaux mettent en jeu le même écart d'énergie, donc la même longueur d'onde : raie brillante et raie noire sont superposées. Les raies d'une série sont d'autant plus énergétiques que le niveau d'arrivée est bas. Cas limite : à partir de 13,6 eV, l'atome fondamental peut absorber un photon d'énergie quelconque, l'excédent allant à l'électron ; en dessous, seules les valeurs exactes des écarts sont absorbées.
:::

::: verifie À toi : de n = 4 à n = 2
Un atome d'hydrogène passe du niveau n = 4 au niveau n = 2. Calculer l'énergie du photon émis, puis sa longueur d'onde.

---

ΔE = E₂ − E₄ = −3,40 − (−0,85) = −2,55 eV : l'atome émet un photon d'énergie W = |ΔE| = 2,55 eV = 2,55 × 1,6×10⁻¹⁹ = 4,08×10⁻¹⁹ J. Alors λ = h·c/W = 1,99×10⁻²⁵ / 4,08×10⁻¹⁹ = 4,87×10⁻⁷ m = 487 nm : c'est la raie bleue Hβ de la série de Balmer.
:::

::: retenir
Pour une transition de l'hydrogène, W = |ΔE| = E₀·(1/n² − 1/p²) puis λ = hc/W ; un photon n'est absorbé que s'il apporte exactement l'écart entre deux niveaux, ou au moins 13,6 eV depuis le fondamental.
:::

## 🔭 Lire la lumière d'un alliage ou d'une étoile

Un métallurgiste veut connaître la composition d'un alliage ; un astrophysicien, celle d'une étoile qu'aucune sonde n'atteindra. Ni l'un ni l'autre ne peut en prélever un morceau.
Que peut-on apprendre en n'analysant que la lumière reçue ?

::: definition
**Analyse spectrale** — Le spectre d'un corps est la superposition des spectres de ses éléments. En chimie, un arc électrique excite l'alliage : la **position** des raies d'émission identifie les éléments, leur **intensité** donne les proportions. En astrophysique, le cœur très chaud d'une étoile émet un spectre continu ; sa couche superficielle, plus froide, absorbe certaines radiations : on reçoit un spectre continu parcouru de raies noires, qui renseignent sur la composition, la température et la vitesse.
:::

| Couleur de l'étoile | Exemple    | Température de surface |
| ------------------- | ---------- | ---------------------- |
| rouge               | Bételgeuse | 2500 °C                |
| jaune               | Soleil     | 5500 °C                |
| blanche             | Sirius     | 10000 °C               |
| bleue               | Rigel      | 20000 °C               |

Dans le tableau, plus l'étoile est chaude, plus sa couleur se déplace du rouge vers le bleu, et plus son spectre continu s'étend vers le violet.

::: figure Raies d'absorption de l'hydrogène au laboratoire, puis dans une étoile qui s'éloigne : toutes les raies sont décalées vers le rouge (le décalage est exagéré sur le dessin)
<svg viewBox="0 0 340 160"><title>Raies d'absorption de l'hydrogène en laboratoire puis dans le spectre d'une étoile qui s'éloigne : les trois raies sont décalées vers le rouge, c'est-à-dire vers les grandes longueurs d'onde, d'un décalage exagéré sur le dessin</title><defs><linearGradient id="sp-b" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#7c3aed"/><stop offset="0.17" stop-color="#2563eb"/><stop offset="0.33" stop-color="#06b6d4"/><stop offset="0.5" stop-color="#22c55e"/><stop offset="0.67" stop-color="#eab308"/><stop offset="0.83" stop-color="#f97316"/><stop offset="1" stop-color="#dc2626"/></linearGradient></defs><rect x="20" y="22" width="300" height="30" fill="url(#sp-b)" stroke="#0f172a" stroke-width="1.5"/><line x1="54" y1="22" x2="54" y2="52" stroke="#111827" stroke-width="3.0" stroke-linecap="round"/><line x1="106" y1="22" x2="106" y2="52" stroke="#111827" stroke-width="3.0" stroke-linecap="round"/><line x1="276" y1="22" x2="276" y2="52" stroke="#111827" stroke-width="3.0" stroke-linecap="round"/><text x="20" y="15" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">laboratoire</text><rect x="20" y="80" width="300" height="30" fill="url(#sp-b)" stroke="#0f172a" stroke-width="1.5"/><line x1="68" y1="80" x2="68" y2="110" stroke="#111827" stroke-width="3.0" stroke-linecap="round"/><line x1="120" y1="80" x2="120" y2="110" stroke="#111827" stroke-width="3.0" stroke-linecap="round"/><line x1="290" y1="80" x2="290" y2="110" stroke="#111827" stroke-width="3.0" stroke-linecap="round"/><text x="170" y="124" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">étoile qui s'éloigne</text><line x1="106" y1="66" x2="120" y2="66" stroke="#b45309" stroke-width="1.8" stroke-linecap="round"/><polygon points="124,66 117,62.5 117,69.5" fill="#b45309"/><text x="130" y="70" text-anchor="start" font-size="11" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">vers le rouge</text><line x1="20" y1="132" x2="20" y2="138" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><text x="20" y="152" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">400 nm</text><line x1="120" y1="132" x2="120" y2="138" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><text x="120" y="152" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">500 nm</text><line x1="220" y1="132" x2="220" y2="138" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><text x="220" y="152" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">600 nm</text><line x1="320" y1="132" x2="320" y2="138" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><text x="320" y="152" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">700 nm</text></svg>
:::

Sur le dessin, une raie du spectre de l'étoile se trouve à une longueur d'onde plus grande que la même raie au laboratoire : c'est l'effet Doppler-Fizeau.

::: exemple Lire le spectre d'une étoile (valeurs données pour l'exemple)

1. Le spectre est continu et s'étend jusqu'au violet : l'étoile est chaude, plutôt blanche ou bleue que rouge.
2. Des raies noires apparaissent à 410, 434, 486 et 656 nm, très marquées : par le renversement des raies, la couche superficielle contient de l'hydrogène, et comme ses raies sont les plus noires, il y est le plus abondant. Une raie plus fine à 589 nm révèle du sodium.
3. La raie Hα, mesurée à 656 nm au laboratoire, est observée à 658 nm : sa longueur d'onde a augmenté, donc sa fréquence a diminué (ν = c/λ).
4. Un décalage vers le rouge signifie que l'étoile s'éloigne ; un décalage vers le violet signifierait qu'elle se rapproche.

:::

::: piege
**Erreur : associer le rouge à la chaleur.** On dirait que Bételgeuse, étoile rouge, est la plus chaude du tableau (étape 1). L'erreur tente parce que la braise et la flamme rouge évoquent la chaleur. Mais pour les étoiles, c'est l'inverse : les rouges sont les plus froides (2500 °C) et les bleues les plus chaudes (20000 °C).
:::

::: propriete
**Ce qui reste vrai** — La position des raies donne la composition, leur noirceur l'abondance relative, l'extension du spectre vers le violet la température, et le décalage des raies le sens du mouvement par rapport à nous. Cas limite : l'effet Doppler-Fizeau indique ici seulement le sens (éloignement ou rapprochement) ; le calcul de la vitesse n'est pas au programme.
:::

::: verifie À toi : une étoile qui s'approche ?
La raie Hβ, mesurée à 486 nm au laboratoire, est observée à 484 nm dans le spectre d'une étoile. L'étoile s'approche-t-elle ou s'éloigne-t-elle ?

---

La longueur d'onde a diminué (484 nm < 486 nm), donc la fréquence a augmenté : la raie est décalée vers le violet. Un décalage vers le violet correspond à un rapprochement : l'étoile s'approche de nous.
:::

::: retenir
La position des raies donne la composition, l'extension du spectre la température, et le décalage vers le rouge ou le violet indique si l'astre s'éloigne ou s'approche.
:::

> 🏆 Quête franchie, héros ! Tu sais pourquoi la mécanique de Newton échoue pour l'atome, lire l'expérience de Franck et Hertz, placer les niveaux d'énergie d'un atome, relier un photon à sa longueur d'onde, calculer les niveaux et les raies de l'hydrogène, distinguer spectres d'émission et d'absorption, et lire dans la lumière d'une étoile sa composition, sa température et son mouvement. Le noyau t'attend au chapitre suivant.
