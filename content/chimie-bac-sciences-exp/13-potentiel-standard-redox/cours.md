# 🧪 Potentiel standard d'un couple redox — de la f.é.m. à la force des oxydants

> 💡 «Une f.é.m. se calcule : la différence de deux potentiels standards dit dans quel sens une pile débite et lequel de deux oxydants l'emporte.»

Une pile Daniell neuve affiche 1,10 V, la même pile presque épuisée n'en affiche presque plus, et une pile zinc-plomb en donne environ 0,63 : une seule loi relie-t-elle ces valeurs aux concentrations, et peut-on classer d'un coup tous les oxydants sans monter toutes les piles ? Sept notions répondent : la loi de la f.é.m., la pile usée et la constante K, la comparaison de deux oxydants, l'électrode normale à hydrogène, le potentiel d'électrode et le potentiel standard, la relation E° = E°_D − E°_G, et le classement électrochimique. On suppose acquis la pile Daniell, son symbole, son équation chimique associée et E = V_D − V_G (chapitre 12), ainsi que la fonction Π, la constante K et la comparaison de Π et de K (chapitre 5).

## 📈 La f.é.m. dépend des concentrations : E = E° − (0,06/n) log Π

Une pile Daniell réalisée avec des solutions à 1,0 mol·L⁻¹ affiche 1,10 V. En TP, avec [Zn²⁺] = 0,010 mol·L⁻¹ et [Cu²⁺] = 1,0 mol·L⁻¹, le voltmètre monte à 1,16 V ; avec [Zn²⁺] = 1,0 mol·L⁻¹ et [Cu²⁺] = 0,010 mol·L⁻¹, il tombe à 1,04 V (valeurs d'illustration calculées à 25 °C, proches des mesures).
Existe-t-il une loi qui donne la f.é.m. pour n'importe quelles concentrations ?

::: definition
**Loi de la f.é.m. d'une pile du type Daniell** — Pour la pile M₂ | M₂ⁿ⁺ || M₁ⁿ⁺ | M₁, d'équation chimique associée M₂ + M₁ⁿ⁺ ⇄ M₂ⁿ⁺ + M₁, la f.é.m. à 25 °C est :
E = E° − (0,06/n) log Π
Ici Π = [M₂ⁿ⁺]/[M₁ⁿ⁺] est la fonction usuelle des concentrations (les métaux solides n'y figurent pas), n est le nombre d'électrons de l'équation, et E° est la f.é.m. standard : la valeur de E quand Π = 1.
:::

::: figure Droite E = f(log Π) de la pile Daniell : les points sont calculés avec E = 1,10 − 0,03 log Π ; la droite coupe l'axe des ordonnées en E° = 1,10 V (Π = 1) et sa pente vaut −0,03 V par unité de log Π
<svg viewBox="0 0 340 250"><title>Droite E en fonction de log Π pour la pile Daniell</title>
<line x1="50" y1="200" x2="320" y2="200" stroke="#cbd5e1" stroke-width="0.8"/>
<text x="44" y="203.0" text-anchor="end" font-size="9" font-weight="600" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">1,00</text>
<line x1="50" y1="160" x2="320" y2="160" stroke="#cbd5e1" stroke-width="0.8"/>
<text x="44" y="163.0" text-anchor="end" font-size="9" font-weight="600" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">1,05</text>
<line x1="50" y1="120" x2="320" y2="120" stroke="#cbd5e1" stroke-width="0.8"/>
<text x="44" y="123.0" text-anchor="end" font-size="9" font-weight="600" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">1,10</text>
<line x1="50" y1="80" x2="320" y2="80" stroke="#cbd5e1" stroke-width="0.8"/>
<text x="44" y="83.0" text-anchor="end" font-size="9" font-weight="600" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">1,15</text>
<line x1="50" y1="40" x2="320" y2="40" stroke="#cbd5e1" stroke-width="0.8"/>
<text x="44" y="43.0" text-anchor="end" font-size="9" font-weight="600" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">1,20</text>
<line x1="50" y1="200" x2="50" y2="205" stroke="#0f172a" stroke-width="1.2"/>
<text x="50" y="217" text-anchor="middle" font-size="9" font-weight="600" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">−3</text>
<line x1="104" y1="200" x2="104" y2="205" stroke="#0f172a" stroke-width="1.2"/>
<text x="104" y="217" text-anchor="middle" font-size="9" font-weight="600" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">−2</text>
<line x1="158" y1="200" x2="158" y2="205" stroke="#0f172a" stroke-width="1.2"/>
<text x="158" y="217" text-anchor="middle" font-size="9" font-weight="600" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">−1</text>
<line x1="212" y1="200" x2="212" y2="205" stroke="#0f172a" stroke-width="1.2"/>
<text x="212" y="217" text-anchor="middle" font-size="9" font-weight="600" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">0</text>
<line x1="266" y1="200" x2="266" y2="205" stroke="#0f172a" stroke-width="1.2"/>
<text x="266" y="217" text-anchor="middle" font-size="9" font-weight="600" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">1</text>
<line x1="320" y1="200" x2="320" y2="205" stroke="#0f172a" stroke-width="1.2"/>
<text x="320" y="217" text-anchor="middle" font-size="9" font-weight="600" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">2</text>
<line x1="50" y1="200" x2="324" y2="200" stroke="#0f172a" stroke-width="1.6"/>
<line x1="50" y1="200" x2="50" y2="34" stroke="#0f172a" stroke-width="1.6"/>
<text x="188" y="236" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">log Π</text>
<text x="28" y="28" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">E (V)</text>
<line x1="212" y1="200" x2="212" y2="120" stroke="#b45309" stroke-width="1.2" stroke-dasharray="4 3"/>
<line x1="50" y1="120" x2="212" y2="120" stroke="#b45309" stroke-width="1.2" stroke-dasharray="4 3"/>
<line x1="50" y1="48" x2="320" y2="168" stroke="#1d4ed8" stroke-width="2"/>
<circle cx="50" cy="48" r="3.6" fill="#f59e0b" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="104" cy="72" r="3.6" fill="#f59e0b" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="158" cy="96" r="3.6" fill="#f59e0b" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="212" cy="120" r="3.6" fill="#f59e0b" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="266" cy="144" r="3.6" fill="#f59e0b" stroke="#0f172a" stroke-width="1.2"/>
<circle cx="320" cy="168" r="3.6" fill="#f59e0b" stroke="#0f172a" stroke-width="1.2"/>
<text x="112" y="114.0" text-anchor="middle" font-size="9" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">E° = 1,10 V pour Π = 1</text>
<text x="262" y="118.0" text-anchor="middle" font-size="9" font-weight="700" fill="#1d4ed8" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">pente −0,03 V</text>
</svg>
:::

Sur la figure, l'ordonnée à l'origine de la droite (log Π = 0, donc Π = 1) est E° = 1,10 V, et sa pente −0,03 V est le coefficient −0,06/n de la formule avec n = 2.

::: exemple Les deux piles du TP

1. L'équation associée est Zn + Cu²⁺ ⇄ Zn²⁺ + Cu avec n = 2 : le zinc cède 2 électrons et chaque ion Cu²⁺ en capte 2 ; le coefficient de log Π vaut donc 0,06/2 = 0,03 V.
2. Pour [Zn²⁺] = 0,010 et [Cu²⁺] = 1,0 mol·L⁻¹ : Π = 0,010/1,0 = 0,010, car Zn et Cu, solides, n'entrent pas dans Π ; ainsi log Π = −2.
3. E = 1,10 − 0,03 × (−2) = 1,10 + 0,06 = 1,16 V, la valeur mesurée : un Π petit donne un logarithme négatif, qui fait monter E au-dessus de E°.
4. Pour [Zn²⁺] = 1,0 et [Cu²⁺] = 0,010 mol·L⁻¹ : Π = 100, log Π = 2 et E = 1,10 − 0,06 = 1,04 V, encore la valeur mesurée ; avec Π = 1, on retrouve E = E° = 1,10 V.

:::

::: piege
**Erreur : écrire Π à l'envers, avec [Cu²⁺] au numérateur.** On place l'ion qui réagit au-dessus parce qu'on s'attend à un rapport « réactifs sur produits ». Mais Π se lit produits sur réactifs de l'équation associée, donc [Zn²⁺]/[Cu²⁺] ; avec [Zn²⁺] = 0,010 et [Cu²⁺] = 1,0 mol·L⁻¹, l'écriture inversée donne Π = 100 et E = 1,04 V au lieu de 1,16 V : le sens de variation de E est faussé.
:::

::: propriete
**E est une fonction affine de log Π** — À température fixée, E est une fonction affine de log Π : l'ordonnée à l'origine est E° (valeur pour Π = 1), la pente est −0,06/n. Dans une pile qui débite, [Zn²⁺] croît et [Cu²⁺] décroît : Π augmente et E diminue.
Cas : la pente vaut −0,06 V pour n = 1, −0,03 V pour n = 2 et −0,02 V pour n = 3.
Cas limite : le coefficient 0,06 n'est valable qu'à 25 °C ; à une autre température, il est différent.
:::

::: verifie À toi : une pile zinc-plomb
La pile Zn | Zn²⁺ (0,10 mol·L⁻¹) || Pb²⁺ (0,0010 mol·L⁻¹) | Pb a pour f.é.m. standard E° = 0,63 V. Calculer sa f.é.m. à 25 °C.

---

L'équation associée est Zn + Pb²⁺ ⇄ Zn²⁺ + Pb, avec n = 2, donc un coefficient 0,03 V. Π = [Zn²⁺]/[Pb²⁺] = 0,10/0,0010 = 100, log Π = 2. E = 0,63 − 0,03 × 2 = 0,57 V : Π > 1, donc E est inférieure à E°.
:::

::: retenir
À 25 °C, E = E° − (0,06/n) log Π, avec Π = produits/réactifs de l'équation associée, solides exclus : E est affine en log Π, vaut E° pour Π = 1 et diminue quand Π augmente.
:::

## ⚖️ Pile usée, Π = K et la constante d'équilibre

Une pile Daniell débite pendant des heures, puis le courant s'éteint : le voltmètre indique 0 V, alors que les ions Zn²⁺ et Cu²⁺ sont toujours dans les béchers. La pile est « usée », pas détruite.
Que vaut Π à cet instant, et que dit cet état sur la constante d'équilibre K ?

::: definition
**Pile usée et constante d'équilibre** — Une pile est usée quand son système chimique a atteint l'équilibre : le courant est nul, la f.é.m. s'annule, E = 0, et Π = K.
En remplaçant dans la loi de la f.é.m. : 0 = E° − (0,06/n) log K, d'où E° = (0,06/n) log K, soit K = 10^(nE°/0,06).
:::

::: exemple La pile Daniell usée

1. À l'équilibre, E = 0 car le courant est nul, et Π = K car le système n'évolue plus ; la loi s'écrit 0 = 1,10 − 0,03 log K.
2. On isole log K : log K = 2 × 1,10/0,06 = 36,67, puisque n = 2 et E° = 1,10 V.
3. K = 10^36,67 ≈ 4,6 × 10³⁶ ; ce nombre immense dit que, à l'équilibre, [Zn²⁺]/[Cu²⁺] vaut 4,6 × 10³⁶ : il ne reste pratiquement plus d'ions Cu²⁺, la réaction est quasi totale.
4. Avec un autre couple, Fe | Fe²⁺ || Cu²⁺ | Cu de E° = 0,78 V, le même calcul donne log K = 2 × 0,78/0,06 = 26 et K = 10²⁶ : K ne dépend que de E° et de n.
5. Bilan à volumes égaux : si la pile part de [Zn²⁺] = [Cu²⁺] = 0,10 mol·L⁻¹ avec deux compartiments de même volume, la réaction quasi totale consomme pratiquement tous les ions Cu²⁺ (0,10 mol·L⁻¹) et fait apparaître autant d'ions Zn²⁺ dans l'autre bécher : [Zn²⁺] final = 0,10 + 0,10 = 0,20 mol·L⁻¹, et [Cu²⁺] final = 0,20/K, valeur négligeable.

:::

::: piege
**Erreur : croire qu'une pile usée a une f.é.m. égale à E°.** On retient que E° est « la f.é.m. standard » et on l'attribue à l'état final. Mais E° n'est la valeur de E que pour Π = 1 : une pile usée a Π = K, donc E = 0, et c'est précisément ce qui permet de calculer K à partir de E°.
:::

::: propriete
**K se lit sur E°** — log K = nE°/0,06 : le signe de E° est celui de log K. E° > 0 donne K > 1, E° < 0 donne K < 1, E° = 0 donne K = 1. K ne dépend que de la paire de couples redox, de n et de la température.
Cas : E° = 0,30 V avec n = 2 donne log K = 10, soit K = 10¹⁰.
Cas limite : un K immense indique qu'une réaction est possible et quasi totale, mais ne dit rien de sa vitesse (voir la dernière notion).
:::

::: verifie À toi : une pile nickel-cuivre
La pile Ni | Ni²⁺ || Cu²⁺ | Cu a pour f.é.m. standard E° = 0,60 V. Que vaut sa constante d'équilibre K à 25 °C ?

---

L'équation associée est Ni + Cu²⁺ ⇄ Ni²⁺ + Cu, avec n = 2. Une pile usée a E = 0 et Π = K, donc log K = nE°/0,06 = 2 × 0,60/0,06 = 20, soit K = 10²⁰. K est très supérieur à 1, comme E° > 0.
:::

::: retenir
Pile usée : courant nul, E = 0, Π = K ; d'où E° = (0,06/n) log K, soit K = 10^(nE°/0,06), du même signe que E°.
:::

## 🥊 Comparer deux oxydants et prévoir le sens d'évolution

Un clou de fer plongé dans du nitrate de plomb (II) se couvre d'un dépôt de plomb gris ; une lame de plomb dans une solution de sulfate de fer (II) ne change pas.
Quel oxydant est le plus fort, Fe²⁺ ou Pb²⁺, et comment le dire sans refaire l'expérience, ni pour ces concentrations ni pour d'autres ?

::: definition
**Comparaison par le signe de E°** — Pour la pile Red₂ | Ox₂ || Ox₁ | Red₁ de f.é.m. standard E° : si E° > 0 (K > 1), Ox₁ est un oxydant plus fort que Ox₂ et Red₂ un réducteur plus fort que Red₁ ; si E° < 0 (K < 1), c'est l'inverse.
Le sens d'évolution pour des concentrations quelconques se lit sur le signe de E : E > 0 correspond à Π < K, la réaction directe de l'équation associée ; E < 0 correspond à Π > K, la réaction inverse.
:::

::: exemple Fer et plomb

1. Pour la pile Fe | Fe²⁺ || Pb²⁺ | Pb avec [Fe²⁺] = [Pb²⁺] = 0,050 mol·L⁻¹, Π = 1, donc E = E° ; on mesure +0,31 V.
2. log K = 2 × 0,31/0,06 = 10,3, soit K ≈ 2 × 10¹⁰ : K > 1, puisque E° > 0.
3. Pb²⁺ (Ox₁, à droite) est donc un oxydant plus fort que Fe²⁺, et Fe (Red₂) un réducteur plus fort que Pb : le clou de fer s'attaque bien dans le plomb.
4. Pour [Fe²⁺] = 0,50 et [Pb²⁺] = 0,010 mol·L⁻¹, Π = 50, bien inférieur à K : la réaction directe Fe + Pb²⁺ → Fe²⁺ + Pb est spontanée, comme le confirme E = 0,31 − 0,03 × log 50 = 0,31 − 0,05 = +0,26 V > 0.

:::

::: piege
**Erreur : conclure qu'aucune réaction n'est possible parce que E° est négatif.** Prenons Sn | Sn²⁺ || Ni²⁺ | Ni avec E° = −0,12 V : on pense « K < 1, donc rien ne se passe ». Mais K = 10^(2 × (−0,12)/0,06) = 10⁻⁴ n'interdit pas la réaction : pour [Sn²⁺] = 1,0 × 10⁻⁶ et [Ni²⁺] = 1,0 mol·L⁻¹, Π = 10⁻⁶ < K et E = −0,12 + 0,03 × 6 = +0,06 V > 0, donc Sn + Ni²⁺ → Sn²⁺ + Ni est spontanée. Le signe de E° compare les oxydants à Π = 1 ; le sens d'un mélange donné se juge en comparant Π à K.
:::

::: propriete
**Trois lectures d'un même fait** — E° > 0, K > 1 et « Ox₁ plus fort que Ox₂ » disent la même chose ; de même E > 0, Π < K et « la réaction directe est spontanée », puisque E = (0,06/n)(log K − log Π). À l'équilibre, Π = K et E = 0.
Cas : dans Fe | Fe²⁺ || Pb²⁺ | Pb, Π = 50 < K, E > 0 : réaction directe ; avec Π > K, E serait négative et la réaction inverse spontanée.
Cas limite : quand E° est voisin de zéro, un écart de concentrations suffit à renverser le sens : le signe de E° ne décide plus seul.
:::

::: verifie À toi : cobalt et zinc
La pile Co | Co²⁺ || Zn²⁺ | Zn a pour f.é.m. standard E° = −0,48 V. Quel est l'oxydant le plus fort, Co²⁺ ou Zn²⁺, et que vaut K ?

---

E° < 0 : Ox₁ = Zn²⁺, à droite, est l'oxydant le plus faible ; Co²⁺ est donc le plus fort et Co un réducteur plus faible que Zn. K = 10^(2 × (−0,48)/0,06) = 10⁻¹⁶, très inférieur à 1, ce qui confirme que la réaction directe Co + Zn²⁺ → Co²⁺ + Zn n'est pas spontanée dans les conditions standard.
:::

::: retenir
Pile Red₂ | Ox₂ || Ox₁ | Red₁ : E° > 0 signifie K > 1 et Ox₁ plus fort que Ox₂ ; pour un mélange donné, E > 0 équivaut à Π < K et donne la réaction directe.
:::

## ⚗️ L'électrode normale à hydrogène

Pour classer dix couples redox deux à deux, il faudrait monter 45 piles et mesurer 45 f.é.m. En mesurant plutôt chaque couple une seule fois, contre le même partenaire, on n'aurait que dix piles.
Quel partenaire choisir, et comment le réaliser, puisqu'un des deux couples est un gaz ?

::: definition
**Demi-pile à hydrogène et électrode normale à hydrogène** — Le couple de référence est H₃O⁺/H₂. La demi-pile à hydrogène est une lame de platine platiné plongée dans une solution aqueuse acide, où l'on envoie du dihydrogène gazeux au contact de la lame.
L'**électrode normale à hydrogène (E.N.H.)** est cette demi-pile dans les conditions normales : pression de H₂ égale à 1 atm (1,013 × 10⁵ Pa, soit 760 mmHg) et [H₃O⁺] = 1 mol·L⁻¹.
:::

::: figure Électrode normale à hydrogène : le dihydrogène arrive à 1 atm au contact de la lame de platine platiné, plongée dans une solution acide où [H₃O⁺] = 1 mol·L⁻¹
<svg viewBox="0 0 300 250"><title>Électrode normale à hydrogène</title>
<rect x="60" y="120" width="180" height="90" fill="#bae6fd" stroke="none"/>
<path d="M60 90 V210 H240 V90" stroke="#0f172a" stroke-width="1.6" fill="none"/>
<rect x="112" y="36" width="16" height="150" fill="#f1f5f9" stroke="#0f172a" stroke-width="1.4"/>
<rect x="146" y="112" width="24" height="84" fill="#64748b" stroke="#0f172a" stroke-width="1.4"/>
<line x1="158" y1="112" x2="158" y2="50" stroke="#0f172a" stroke-width="1.6"/>
<circle cx="120" cy="196" r="3" fill="#ffffff" stroke="#0f172a" stroke-width="1"/>
<circle cx="126" cy="204" r="2.5" fill="#ffffff" stroke="#0f172a" stroke-width="1"/>
<circle cx="134" cy="194" r="3" fill="#ffffff" stroke="#0f172a" stroke-width="1"/>
<circle cx="140" cy="186" r="2.5" fill="#ffffff" stroke="#0f172a" stroke-width="1"/>
<circle cx="138" cy="172" r="2.5" fill="#ffffff" stroke="#0f172a" stroke-width="1"/>
<line x1="120" y1="20" x2="120" y2="40" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="120,46 116,38 124,38" fill="#0f172a"/>
<text x="120" y="14" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">H₂, P = 1 atm</text>
<text x="214" y="150" text-anchor="middle" font-size="9" font-weight="600" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">lame de</text>
<text x="214" y="162" text-anchor="middle" font-size="9" font-weight="600" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">platine platiné</text>
<line x1="170" y1="152" x2="190" y2="152" stroke="#0f172a" stroke-width="1.2"/>
<text x="165" y="44" text-anchor="start" font-size="9" font-weight="600" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">vers le circuit</text>
<text x="150" y="228" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">solution acide : [H₃O⁺] = 1 mol·L⁻¹</text>
</svg>
:::

Sur la figure, la lame de platine platiné est le conducteur électronique du couple H₃O⁺/H₂, et la solution acide en est le conducteur ionique.

::: exemple Pourquoi du platine platiné

1. Le dihydrogène est un gaz non conducteur : il faut une lame métallique pour échanger les électrons avec lui.
2. Cette lame doit être inattaquable : un métal comme le zinc serait oxydé par les ions H₃O⁺ de la solution et fausserait la demi-pile, alors que le platine ne l'est pas.
3. Le platine est « platiné », c'est-à-dire recouvert d'une couche poreuse de platine : elle fixe le dihydrogène à sa surface et favorise le transfert d'électrons.
4. Avec ce partenaire unique, dix couples demandent dix mesures, une par couple contre l'E.N.H., au lieu de 10 × 9/2 = 45 piles.

:::

::: piege
**Erreur : appeler E.N.H. n'importe quelle demi-pile à hydrogène.** On le fait dès que le dihydrogène, le platine et un acide sont réunis. Mais avec [H₃O⁺] = 0,10 mol·L⁻¹, la demi-pile fonctionne comme une électrode à hydrogène sans être une E.N.H. : ce sont les conditions imposées, 1 atm et 1 mol·L⁻¹, qui en font une référence reproductible, la même d'un laboratoire à l'autre.
:::

::: propriete
**Les conditions de l'E.N.H.** — Une demi-pile à hydrogène est une E.N.H. si P(H₂) = 1 atm = 1,013 × 10⁵ Pa et si [H₃O⁺] = 1 mol·L⁻¹, avec une lame de platine platiné.
Cas : le mot « électrode » désigne à la rigueur la lame seule, mais on l'emploie par abus de langage pour la demi-pile entière, comme dans « électrode normale à hydrogène ».
Cas limite : sans lame métallique, le dihydrogène seul ne peut ni donner ni recevoir d'électrons du circuit : la demi-pile n'existerait pas.
:::

::: verifie À toi : une autre demi-pile à hydrogène
Une demi-pile à hydrogène est réalisée avec une solution où [H₃O⁺] = 1,0 mol·L⁻¹, mais le dihydrogène est sous 2 atm. Est-ce une E.N.H. ?

---

Non. Une E.N.H. exige les deux conditions en même temps : [H₃O⁺] = 1 mol·L⁻¹ et P(H₂) = 1 atm. Ici la concentration convient, mais la pression est double : c'est une demi-pile à hydrogène quelconque, pas la référence.
:::

::: retenir
L'E.N.H. est la demi-pile H₃O⁺/H₂ à lame de platine platiné, avec P(H₂) = 1 atm = 1,013 × 10⁵ Pa et [H₃O⁺] = 1 mol·L⁻¹ : la référence commune des couples.
:::

## 🎯 Potentiel d'électrode et potentiel standard

L'E.N.H. est le partenaire commun. On la branche à gauche d'une demi-pile de zinc, puis à gauche d'une demi-pile de cuivre, et on lit le voltmètre : −0,76 V d'un côté, +0,34 V de l'autre.
Que représentent ces deux nombres, et que vaut celui du couple H₃O⁺/H₂ lui-même ?

::: definition
**Potentiel d'électrode et potentiel standard d'électrode** — Le potentiel d'électrode E(Ox/Red) d'un couple est, par définition, la f.é.m. de la pile formée de l'E.N.H. à gauche et de la demi-pile du couple à droite.
Le **potentiel standard d'électrode** E°(Ox/Red) est la valeur de cette f.é.m. quand Π = 1 ; pour un couple Mⁿ⁺/M, c'est quand [Mⁿ⁺] = 1 mol·L⁻¹.
:::

::: figure Pile E.N.H. à gauche, lame de zinc dans Zn²⁺ à 1,0 mol·L⁻¹ à droite, reliées par un pont salin : le voltmètre, branché entre la borne de gauche et celle de droite, indique −0,76 V
<svg viewBox="0 0 360 270"><title>Pile E.N.H. à gauche et Zn dans Zn²⁺ à droite, voltmètre indiquant −0,76 V</title>
<rect x="20" y="140" width="120" height="90" fill="#bae6fd" stroke="none"/>
<path d="M20 110 V230 H140 V110" stroke="#0f172a" stroke-width="1.6" fill="none"/>
<rect x="220" y="140" width="120" height="90" fill="#e2e8f0" stroke="none"/>
<path d="M220 110 V230 H340 V110" stroke="#0f172a" stroke-width="1.6" fill="none"/>
<rect x="52" y="100" width="12" height="100" fill="#f1f5f9" stroke="#0f172a" stroke-width="1.4"/>
<rect x="86" y="132" width="20" height="74" fill="#64748b" stroke="#0f172a" stroke-width="1.4"/>
<line x1="96" y1="132" x2="96" y2="60" stroke="#0f172a" stroke-width="1.6"/>
<rect x="276" y="112" width="20" height="104" fill="#94a3b8" stroke="#0f172a" stroke-width="1.4"/>
<line x1="286" y1="112" x2="286" y2="60" stroke="#0f172a" stroke-width="1.6"/>
<path d="M120 172 V120 H240 V172" stroke="#475569" stroke-width="11" fill="none"/>
<path d="M120 172 V120 H240 V172" stroke="#fde68a" stroke-width="7" fill="none"/>
<circle cx="190" cy="44" r="22" fill="#ffffff" stroke="#0f172a" stroke-width="1.6"/>
<text x="190" y="50" text-anchor="middle" font-size="16" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">V</text>
<path d="M96 60 V44 H168" stroke="#0f172a" stroke-width="1.6" fill="none"/>
<path d="M286 60 V44 H212" stroke="#0f172a" stroke-width="1.6" fill="none"/>
<text x="190" y="88" text-anchor="middle" font-size="11" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">E = −0,76 V</text>
<text x="58" y="96" text-anchor="middle" font-size="9" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">H₂, 1 atm</text>
<text x="80" y="248" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">E.N.H.</text>
<text x="80" y="262" text-anchor="middle" font-size="9" font-weight="600" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">[H₃O⁺] = 1 mol·L⁻¹</text>
<text x="280" y="248" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">Zn dans Zn²⁺</text>
<text x="280" y="262" text-anchor="middle" font-size="9" font-weight="600" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">[Zn²⁺] = 1,0 mol·L⁻¹</text>
<text x="96" y="76" text-anchor="middle" font-size="9" font-weight="600" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">gauche</text>
<text x="286" y="76" text-anchor="middle" font-size="9" font-weight="600" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">droite</text>
</svg>
:::

Sur la figure, le voltmètre mesure E = V_D − V_G entre la lame de zinc (droite) et l'E.N.H. (gauche) : comme [Zn²⁺] = 1,0 mol·L⁻¹, donc Π = 1, ce nombre est le potentiel standard E°(Zn²⁺/Zn) = −0,76 V.

::: exemple Zinc, cuivre et hydrogène

1. Pour Pt | H₂ (1 atm) | H₃O⁺ (1 mol·L⁻¹) || Cu²⁺ (1,0 mol·L⁻¹) | Cu, on lit +0,34 V ; Π = 1, donc E = E° et E°(Cu²⁺/Cu) = +0,34 V.
2. Pour le zinc, on lit −0,76 V avec [Zn²⁺] = 1,0 mol·L⁻¹ : E°(Zn²⁺/Zn) = −0,76 V ; l'équation associée est H₂ + Zn²⁺ + 2 H₂O ⇄ 2 H₃O⁺ + Zn.
3. E < 0 : la borne + est à gauche, du côté de l'E.N.H., et le zinc est la borne − ; c'est la réaction inverse qui a lieu, Zn + 2 H₃O⁺ → Zn²⁺ + H₂ + 2 H₂O, donc le zinc est oxydé par H₃O⁺.
4. Pour H₃O⁺/H₂ lui-même, on relie deux E.N.H. : la pile est parfaitement symétrique, V_D = V_G et E = 0, donc E°(H₃O⁺/H₂) = 0 V ; c'est une conséquence de la définition choisie, et elle vaut à toute température.

:::

::: piege
**Erreur : lire E°(Zn²⁺/Zn) = −0,76 V comme « la lame de zinc est au potentiel −0,76 V ».** On prend le voltmètre pour un instrument qui donne le potentiel absolu d'une lame. Mais il indique une différence V_D − V_G entre deux bornes : −0,76 V est la f.é.m. d'une pile précise, avec l'E.N.H. à gauche ; ce nombre compare le couple à H₃O⁺/H₂ et ne mesure pas le potentiel électrique d'une lame isolée.
:::

::: propriete
**Lire un potentiel standard** — Pour un couple Ox/Red : E° > 0 signifie que Ox est un oxydant plus fort que H₃O⁺ (et Red un réducteur plus faible que H₂) ; E° < 0 signifie l'inverse. Le signe de E° est celui de log K pour l'équation associée à la pile avec l'E.N.H.
Cas : Cu²⁺/Cu (+0,34 V) : Cu²⁺ est un oxydant plus fort que H₃O⁺ ; Zn²⁺/Zn (−0,76 V) : Zn²⁺ est plus faible que H₃O⁺.
Cas limite : avec l'E.N.H. à droite et la lame de zinc à gauche, la même pile donnerait +0,76 V ; le signe d'une f.é.m. dépend du schéma, et E°(Zn²⁺/Zn) a une valeur unique parce que l'E.N.H. est toujours à gauche.
:::

::: verifie À toi : le nickel contre l'E.N.H.
Dans la pile Pt | H₂ (1 atm) | H₃O⁺ (1,0 mol·L⁻¹) || Ni²⁺ (1,0 mol·L⁻¹) | Ni, le voltmètre indique −0,26 V. Donner E°(Ni²⁺/Ni), la borne + et la réaction spontanée.

---

Π = 1, donc E° = E = −0,26 V. E < 0 : la borne + est à gauche, côté E.N.H., et le nickel est la borne − : il est oxydé par H₃O⁺. La réaction spontanée est Ni + 2 H₃O⁺ → Ni²⁺ + H₂ + 2 H₂O, et Ni²⁺ est un oxydant plus faible que H₃O⁺.
:::

::: retenir
E°(Ox/Red) est la f.é.m. de la pile E.N.H. à gauche | couple à droite, pour Π = 1 ; E°(H₃O⁺/H₂) = 0 V ; E° > 0 : Ox plus fort que H₃O⁺.
:::

## ➖ La f.é.m. standard d'une pile : E° = E°_D − E°_G

Dans le tableau des potentiels, Ni²⁺/Ni et Fe²⁺/Fe ont chacun leur valeur, mesurée une seule fois contre l'E.N.H.
Peut-on en déduire la f.é.m. d'une pile fer-nickel que personne n'a montée, et son signe ?

::: definition
**f.é.m. à partir des potentiels d'électrode** — La f.é.m. d'une pile est la différence des potentiels d'électrode des couples de droite et de gauche : E = E_D − E_G. Avec Π = 1, la f.é.m. standard est E° = E°_D − E°_G.
Les E_D et E_G sont des potentiels d'électrode (définis contre l'E.N.H.), à ne pas confondre avec V_D et V_G, les potentiels électriques des bornes.
:::

::: exemple Une pile fer-nickel

1. Pour Fe | Fe²⁺ || Ni²⁺ | Ni, le couple de droite est Ni²⁺/Ni et celui de gauche Fe²⁺/Fe : l'écriture du symbole fixe les rôles.
2. E° = E°(Ni²⁺/Ni) − E°(Fe²⁺/Fe) = −0,26 − (−0,44) = +0,18 V, d'après l'échelle des potentiels standards de la dernière notion.
3. E° > 0 : Ni²⁺ est un oxydant plus fort que Fe²⁺ et la réaction Fe + Ni²⁺ → Fe²⁺ + Ni est spontanée ; K = 10^(2 × 0,18/0,06) = 10⁶.
4. Pour [Fe²⁺] = 1,0 et [Ni²⁺] = 0,010 mol·L⁻¹ : Π = 100 et E = 0,18 − 0,03 × 2 = 0,12 V ; avec le schéma inversé, Ni | Ni²⁺ || Fe²⁺ | Fe, la même pile standard aurait E° = −0,18 V.

:::

::: piege
**Erreur : soustraire dans le mauvais sens, E° = E°_G − E°_D.** On range les couples dans l'ordre de lecture du tableau et on soustrait « le premier du second ». Pour la pile Fe | Fe²⁺ || Ni²⁺ | Ni, cela donne −0,44 − (−0,26) = −0,18 V, au lieu de +0,18 V ; le signe faux ferait croire que Ni²⁺ est un oxydant plus faible que Fe²⁺, ce qu'aucun clou de fer dans du sulfate de nickel ne confirme. C'est toujours la droite moins la gauche du schéma.
:::

::: propriete
**E° ne dépend pas de l'écriture de l'équation** — Si l'on multiplie l'équation associée par 2, n double et K devient K², donc log K double : E° = (0,06/n) log K est inchangé.
Cas : Fe + Ni²⁺ ⇄ Fe²⁺ + Ni a n = 2 et K = 10⁶ ; 2 Fe + 2 Ni²⁺ ⇄ 2 Fe²⁺ + 2 Ni a n = 4 et K′ = K² = 10¹², d'où E° = (0,06/4) × 12 = 0,18 V.
Cas limite : dans ce chapitre, les deux couples d'une pile échangent le même nombre d'électrons (n = 2 ou n = 3 ici) ; E° se calcule toujours par la différence des deux potentiels standards.
:::

::: verifie À toi : cobalt et cuivre
On donne E°(Co²⁺/Co) = −0,28 V et E°(Cu²⁺/Cu) = +0,34 V. Calculer E° de Co | Co²⁺ || Cu²⁺ | Cu, puis de Cu | Cu²⁺ || Co²⁺ | Co.

---

Pour Co | Co²⁺ || Cu²⁺ | Cu, droite moins gauche : E° = 0,34 − (−0,28) = +0,62 V. Pour Cu | Cu²⁺ || Co²⁺ | Co, les rôles sont échangés : E° = −0,28 − 0,34 = −0,62 V. C'est la même pile écrite à l'envers : la valeur absolue est la même, seul le signe suit le schéma.
:::

::: retenir
E° = E°_D − E°_G, la droite moins la gauche du schéma ; E° ne change pas si l'on double l'équation, et il change de signe si l'on échange les deux demi-piles.
:::

## 📊 Le classement électrochimique et les réactions prévues

Une lame de nickel plongée dans une solution bleue de sulfate de cuivre (II) se couvre de cuivre rouge ; une lame de cuivre plongée dans une solution de nickel (II) ne donne rien.
Faut-il tester chaque couple deux à deux, ou un seul tableau de potentiels suffit-il à prévoir ?

::: definition
**Classement électrochimique** — Plus le potentiel standard d'un couple est élevé, plus sa forme oxydée est un oxydant fort, et plus sa forme réduite est un réducteur faible. Ranger les couples par E° croissants donne l'échelle des oxydants du plus faible au plus fort.
Cette classification ne dépend pas du nombre d'électrons de l'équation écrite.
:::

::: figure Échelle des potentiels standards de neuf couples à 25 °C (extrait d'un tableau de valeurs) : le pouvoir oxydant de la forme oxydée croît vers le haut, et H₃O⁺/H₂ (0,00 V) sépare les couples dont E° est négatif de ceux dont E° est positif
<svg viewBox="0 0 340 300"><title>Échelle des potentiels standards de quelques couples à 25 °C</title>
<line x1="170" y1="22" x2="170" y2="272" stroke="#0f172a" stroke-width="1.8"/>
<text x="170" y="12" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">oxydant plus fort ▲</text>
<text x="170" y="292" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">oxydant plus faible ▼</text>
<line x1="160" y1="27.6" x2="180" y2="27.6" stroke="#0f172a" stroke-width="1.8"/>
<text x="154" y="31.1" text-anchor="end" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">Ag⁺/Ag  +0,80 V</text>
<line x1="160" y1="62.4" x2="180" y2="62.4" stroke="#0f172a" stroke-width="1.8"/>
<text x="186" y="65.9" text-anchor="start" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">Cu²⁺/Cu  +0,34 V</text>
<line x1="160" y1="88.2" x2="180" y2="88.2" stroke="#b45309" stroke-width="1.8"/>
<text x="154" y="91.7" text-anchor="end" font-size="10" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">H₃O⁺/H₂  0,00 V</text>
<line x1="160" y1="98.0" x2="180" y2="98.0" stroke="#0f172a" stroke-width="1.8"/>
<text x="186" y="101.5" text-anchor="start" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">Pb²⁺/Pb  −0,13 V</text>
<line x1="160" y1="107.9" x2="180" y2="107.9" stroke="#0f172a" stroke-width="1.8"/>
<text x="154" y="111.4" text-anchor="end" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">Ni²⁺/Ni  −0,26 V</text>
<line x1="160" y1="121.5" x2="180" y2="121.5" stroke="#0f172a" stroke-width="1.8"/>
<text x="186" y="125.0" text-anchor="start" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">Fe²⁺/Fe  −0,44 V</text>
<line x1="160" y1="145.8" x2="180" y2="145.8" stroke="#0f172a" stroke-width="1.8"/>
<text x="154" y="149.3" text-anchor="end" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">Zn²⁺/Zn  −0,76 V</text>
<line x1="160" y1="213.9" x2="180" y2="213.9" stroke="#0f172a" stroke-width="1.8"/>
<text x="186" y="217.4" text-anchor="start" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">Al³⁺/Al  −1,66 V</text>
<line x1="160" y1="267.7" x2="180" y2="267.7" stroke="#0f172a" stroke-width="1.8"/>
<text x="154" y="271.2" text-anchor="end" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">Mg²⁺/Mg  −2,37 V</text>
</svg>
:::

Sur la figure, pour des concentrations voisines de 1 mol·L⁻¹, un oxydant peut réagir avec tout réducteur situé au-dessous de lui (réaction possible, parfois trop lente pour être observée), et H₃O⁺/H₂ à 0,00 V sépare les métaux que l'acide peut attaquer (E° < 0) de ceux qu'il n'attaque pas (E° > 0).

::: exemple Nickel, cuivre et acide

1. Nickel dans Cu²⁺ : E°(Cu²⁺/Cu) = +0,34 V est supérieur à E°(Ni²⁺/Ni) = −0,26 V ; Cu²⁺ est l'oxydant le plus fort et Ni le réducteur le plus fort, donc Ni + Cu²⁺ → Ni²⁺ + Cu, ce que l'on observe.
2. Cuivre dans Ni²⁺ : Ni²⁺ est l'oxydant le plus faible des deux et Cu le réducteur le plus faible : aucune réaction.
3. Fer dans une solution acide : E°(Fe²⁺/Fe) = −0,44 V est inférieur à 0, donc H₃O⁺ est un oxydant plus fort que Fe²⁺ et Fe + 2 H₃O⁺ → Fe²⁺ + H₂ + 2 H₂O a lieu.
4. Cuivre dans une solution acide : E°(Cu²⁺/Cu) = +0,34 V est supérieur à 0 ; Cu²⁺ est plus oxydant que H₃O⁺ et le cuivre n'est pas attaqué : un seul tableau a prévu les quatre expériences.

:::

::: piege
**Erreur : penser que le couple au potentiel le plus élevé est celui du meilleur réducteur.** On associe « potentiel élevé » à « puissant ». Mais un E° élevé caractérise un oxydant fort : Ag⁺/Ag (+0,80 V) est le couple de l'oxydant le plus fort de l'échelle et de son réducteur le plus faible, l'argent ; le meilleur réducteur du tableau est le magnésium, au bas de l'échelle (−2,37 V).
:::

::: propriete
**Prévoir une réaction métal-ion** — Quand un métal M₂ plonge dans une solution d'ions M₁ⁿ⁺ de même charge, à des concentrations voisines de 1 mol·L⁻¹, M₂ est oxydé si E°(M₁ⁿ⁺/M₁) > E°(M₂ⁿ⁺/M₂) ; sinon il ne se passe rien.
Cas : le zinc dans Fe²⁺ réagit (−0,44 V > −0,76 V), le fer dans Zn²⁺ non ; quand les E° sont voisins ou les concentrations très éloignées de 1 mol·L⁻¹, on compare Π et K.
Cas limite : une réaction prévue possible peut être si lente qu'on ne l'observe pas (équilibre métastable) : le tableau dit ce qui est possible, pas à quelle vitesse.
:::

::: verifie À toi : fer et zinc
On plonge une lame de fer dans une solution de sulfate de zinc à 1,0 mol·L⁻¹, puis une lame de zinc dans une solution de sulfate de fer (II) à 1,0 mol·L⁻¹. Dans quel cas y a-t-il une réaction ?

---

E°(Zn²⁺/Zn) = −0,76 V est inférieur à E°(Fe²⁺/Fe) = −0,44 V : Fe²⁺ est l'oxydant le plus fort et Zn le réducteur le plus fort. Le zinc dans Fe²⁺ réagit, Zn + Fe²⁺ → Zn²⁺ + Fe ; le fer dans Zn²⁺ ne réagit pas, car Zn²⁺ est l'oxydant le plus faible.
:::

::: retenir
Plus E° est élevé, plus l'oxydant est fort et le réducteur faible : à des concentrations voisines de 1 mol·L⁻¹, un oxydant peut réagir avec les réducteurs situés sous lui ; H₃O⁺/H₂ à 0 V sépare les métaux que les acides peuvent attaquer de ceux qu'ils n'attaquent pas.
:::

> 🏆 Tu sais désormais calculer la f.é.m. d'une pile quelles que soient les concentrations, en déduire K, et classer les oxydants d'un coup d'œil sur l'échelle des potentiels standards.
