# ⚡ Le condensateur et le dipôle RC — maîtriser le temps d'une charge

> 💡 «Dans un circuit RC, le temps n'est pas un détail : c'est un nombre, τ, qu'on calcule et qu'on lit sur une courbe.»

Un chargeur, un flash, un défibrillateur : chacun stocke de l'énergie dans un **condensateur** puis la libère au bon moment. Huit notions te conduisent de la définition du composant jusqu'à la loi exponentielle de sa charge et de sa décharge : le condensateur, l'intensité algébrique et i = dq/dt, la capacité q = C·u_C, le condensateur plan, l'énergie emmagasinée, la charge d'un dipôle RC, sa décharge et la constante de temps τ. On suppose acquises la loi d'Ohm, la loi des mailles, la relation Q = I·Δt et la convention récepteur.

## 🏰 Le condensateur : stocker des charges sans les laisser passer

On branche un condensateur neutre aux bornes d'un générateur, avec un galvanomètre, ampèremètre très sensible, dans le circuit. L'aiguille dévie, puis revient à zéro alors que le circuit reste fermé.
Où sont passées les charges, et pourquoi le courant s'arrête-t-il ?

::: definition
**Condensateur** — Un condensateur est un dipôle formé de deux plaques conductrices très proches, les **armatures**, séparées par un isolant, le **diélectrique** (air, papier imbibé de paraffine, céramique, mica, alumine…). Ses deux bornes sont reliées directement aux armatures. Il se représente par deux traits parallèles. Si les armatures sont planes et parallèles, le condensateur est dit **plan**.
:::

Dans le montage de la figure, K en position 1 relie le condensateur au générateur à travers le résistor R ; K en position 2 isole le générateur et ferme le condensateur sur R seul.

::: figure Montage de charge et de décharge : le sens positif du courant i est orienté vers l'armature A, et la tension u_C est fléchée en sens opposé, de B vers A
<svg viewBox="0 0 390 190"><title>Circuit de charge et de décharge : générateur E, commutateur K, résistor R, condensateur C, avec le courant i orienté vers A et la tension u_C</title><line x1="40" y1="30" x2="40" y2="76" stroke="#0f172a" stroke-width="1.6"/><line x1="28" y1="78" x2="52" y2="78" stroke="#0f172a" stroke-width="2.6"/><line x1="33" y1="88" x2="47" y2="88" stroke="#0f172a" stroke-width="2.6"/><line x1="40" y1="90" x2="40" y2="160" stroke="#0f172a" stroke-width="1.6"/><text x="30" y="66" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">+</text><text x="30" y="112" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">E</text><line x1="40" y1="30" x2="90" y2="30" stroke="#0f172a" stroke-width="1.6"/><line x1="40" y1="160" x2="300" y2="160" stroke="#0f172a" stroke-width="1.6"/><line x1="90" y1="90" x2="90" y2="160" stroke="#0f172a" stroke-width="1.6"/><circle cx="90" cy="30" r="3.2" fill="#fff" stroke="#0f172a" stroke-width="1"/><circle cx="90" cy="90" r="3.2" fill="#fff" stroke="#0f172a" stroke-width="1"/><line x1="140" y1="60" x2="90" y2="30" stroke="#0f172a" stroke-width="2.4"/><line x1="140" y1="60" x2="90" y2="90" stroke="#94a3b8" stroke-width="1.6" stroke-dasharray="4 3"/><circle cx="140" cy="60" r="3.6" fill="#0f172a" stroke="#0f172a" stroke-width="1"/><line x1="140" y1="60" x2="175" y2="60" stroke="#0f172a" stroke-width="1.6"/><rect x="175" y="52" width="50" height="16" fill="#fff7ed" stroke="#0f172a" stroke-width="1.8"/><line x1="225" y1="60" x2="300" y2="60" stroke="#0f172a" stroke-width="1.6"/><circle cx="300" cy="60" r="3.4" fill="#0f172a" stroke="#0f172a" stroke-width="1"/><line x1="300" y1="60" x2="300" y2="102" stroke="#0f172a" stroke-width="1.6"/><line x1="285" y1="102" x2="315" y2="102" stroke="#0f172a" stroke-width="2.6"/><line x1="285" y1="112" x2="315" y2="112" stroke="#0f172a" stroke-width="2.6"/><line x1="300" y1="112" x2="300" y2="160" stroke="#0f172a" stroke-width="1.6"/><circle cx="300" cy="160" r="3.4" fill="#0f172a" stroke="#0f172a" stroke-width="1"/><text x="84" y="22" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><text x="80" y="104" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><text x="120" y="66" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">K</text><text x="200" y="46" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">R</text><text x="312" y="56" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">A</text><text x="312" y="176" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">B</text><text x="330" y="86" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">C</text><line x1="236" y1="44" x2="274" y2="44" stroke="#c2410c" stroke-width="1.8"/><polygon points="282,44 274,48 274,40" fill="#c2410c"/><text x="259" y="36" text-anchor="middle" font-size="12" font-weight="700" fill="#c2410c" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">i</text><line x1="346" y1="146" x2="346" y2="78" stroke="#0f6e56" stroke-width="1.8"/><polygon points="346,70 350,78 342,78" fill="#0f6e56"/><text x="352" y="112" text-anchor="start" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">u<tspan font-size="9" dy="3">C</tspan></text></svg>
:::

Le sens de la flèche i et celui de la flèche u_C se lisent ainsi : le courant arrive sur l'armature A, la tension se mesure entre A et B.

::: exemple Suivre les électrons dans le circuit

1. Les armatures sont neutres. K passe en 1 : des électrons quittent A vers le pôle + du générateur, d'autres partent du pôle − vers B. Le courant conventionnel arrive donc sur A, puisqu'il va en sens inverse des électrons.
2. A porte alors +q et B porte −q. Aucun électron ne traverse le diélectrique, car il est isolant : le courant n'existe que dans les fils.
3. Quand la tension entre A et B égale celle du générateur, le transfert cesse : i = 0 et le condensateur est **chargé**.
4. K passe en 2 : l'attraction entre +q et −q ramène des électrons de B vers A à travers R, donc un courant de sens contraire à celui de la charge, jusqu'à ce que A et B soient neutres : le condensateur est **déchargé**.

:::

> ⚠️ Piège classique : « le courant traverse le condensateur ». Non : des électrons arrivent sur une armature et quittent l'autre, mais rien ne passe par le diélectrique. Ne confonds pas non plus la **charge q** du condensateur, qui est une grandeur, avec le **phénomène de charge**, qui est une évolution dans le temps.

::: propriete
**Ce qu'il faut savoir** — Un condensateur stocke des charges opposées, +q sur une armature et −q sur l'autre. Il se charge sous une tension continue et se décharge lorsqu'on le ferme sur un récepteur ; un condensateur neutre n'a rien à restituer.
:::

::: verifie À toi : les deux armatures
Un condensateur isolé porte −8,0 µC sur son armature B. Quelle charge porte A, et un électron a-t-il traversé le diélectrique pour la lui donner ?

---

A porte +8,0 µC : les deux armatures portent des charges opposées. Non, aucun électron n'a traversé : le diélectrique est isolant, la charge de A vient du fil, par départ d'électrons.
:::

::: retenir
Un condensateur, c'est deux armatures séparées par un isolant : il stocke +q et −q, et rien ne passe par le diélectrique.
:::

## 🧭 L'intensité algébrique et la relation i = dq/dt

Sur l'écran d'un oscilloscope, la tension aux bornes du résistor est positive pendant la charge, négative pendant la décharge, alors que le résistor ne change pas.
Comment un seul symbole i décrit-il un courant dans les deux sens, et comment le relier à la charge stockée ?

::: definition
**Intensité algébrique** — On choisit un **sens positif** pour le courant. L'intensité i est positive si le courant circule dans ce sens, négative s'il circule en sens contraire. La **charge q du condensateur** est la charge de l'armature vers laquelle ce sens positif est orienté. En convention récepteur, la flèche tension u_C = u_AB est de sens opposé à la flèche i (en convention générateur, utilisée pour le générateur, u et i sont fléchées dans le même sens).
:::

::: propriete
**Relation fondamentale** — Entre les instants t et t + Δt, le courant apporte Δq à l'armature qui porte q ; l'intensité est la quantité d'électricité transportée par unité de temps :

$$ i = dq/dt $$

avec dq/dt la limite de Δq/Δt quand Δt tend vers 0.
:::

::: exemple Un signe qui dit le sens

1. Le sens positif est orienté vers A. Pendant une charge à rythme constant, q passe de 0 à 30 µC en 6,0 s : i = Δq/Δt = 30 µC / 6,0 s = +5,0 µA, car q augmente.
2. Pendant une décharge, q passe de 24 µC à 6,0 µC en 1,5 s : i = (6,0 − 24) µC / 1,5 s = −12 µA, car q diminue.
3. Le signe − ne dit pas que le courant est faible : il dit qu'il circule dans le sens contraire au sens positif. Sur l'oscilloscope, u_R = R·i est donc négative quand i < 0.
4. Si q reste constante, Δq = 0 donc i = 0, que le condensateur soit chargé ou neutre.

:::

> ⚠️ Piège classique : « une intensité est toujours positive ». Seule sa valeur absolue l'est. Pour un courant de décharge, orienté en sens contraire du sens positif choisi pour la charge, i est **négative**.

::: verifie À toi : retrouver la variation de charge
Pendant 2,0 s, l'intensité vaut i = −8,0 µA. Que dit ce résultat de la charge q de l'armature repérée ?

---

Comme i = Δq/Δt, Δq = i·Δt = −8,0 µA × 2,0 s = −16 µC : la charge q diminue de 16 µC, ce qui correspond bien à un courant de sens contraire au sens positif.
:::

::: retenir
i est algébrique et i = dq/dt : positive si le courant va dans le sens choisi, négative sinon.
:::

## 📐 La capacité q = C·u_C et le farad

On charge un condensateur avec un **générateur de courant** qui débite toujours I = 60 µA, et on relève u_C toutes les 10 s.
Comment la tension évolue-t-elle quand la charge s'accumule ?

| t (s) | 0 | 10 | 20 | 30 | 40 |
| --- | --- | --- | --- | --- | --- |
| u_C (V) | 0 | 1,2 | 2,4 | 3,6 | 4,8 |

::: figure Les quatre mesures sont alignées avec l'origine : u_C = k·t, avec k = 4,8 V / 40 s = 0,12 V·s⁻¹
<svg viewBox="0 0 340 230"><title>Mesures de u_C en fonction du temps à courant constant : quatre points alignés sur une droite passant par l'origine</title><line x1="52" y1="22" x2="52" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="120.5" y1="22" x2="120.5" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="189" y1="22" x2="189" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="257.5" y1="22" x2="257.5" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="326" y1="22" x2="326" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="52" y1="190" x2="326" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="52" y1="162" x2="326" y2="162" stroke="#e2e8f0" stroke-width="1"/><line x1="52" y1="134" x2="326" y2="134" stroke="#e2e8f0" stroke-width="1"/><line x1="52" y1="106" x2="326" y2="106" stroke="#e2e8f0" stroke-width="1"/><line x1="52" y1="78" x2="326" y2="78" stroke="#e2e8f0" stroke-width="1"/><line x1="52" y1="50" x2="326" y2="50" stroke="#e2e8f0" stroke-width="1"/><line x1="52" y1="22" x2="326" y2="22" stroke="#e2e8f0" stroke-width="1"/><line x1="52" y1="190" x2="332" y2="190" stroke="#0f172a" stroke-width="1.6"/><line x1="52" y1="196" x2="52" y2="16" stroke="#0f172a" stroke-width="1.6"/><polygon points="336,190 328,186 328,194" fill="#0f172a"/><polygon points="52,12 48,20 56,20" fill="#0f172a"/><line x1="52" y1="187" x2="52" y2="193" stroke="#0f172a" stroke-width="1.2"/><text x="52" y="206" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><line x1="120.5" y1="187" x2="120.5" y2="193" stroke="#0f172a" stroke-width="1.2"/><text x="120.5" y="206" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">10</text><line x1="189" y1="187" x2="189" y2="193" stroke="#0f172a" stroke-width="1.2"/><text x="189" y="206" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">20</text><line x1="257.5" y1="187" x2="257.5" y2="193" stroke="#0f172a" stroke-width="1.2"/><text x="257.5" y="206" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">30</text><line x1="326" y1="187" x2="326" y2="193" stroke="#0f172a" stroke-width="1.2"/><text x="326" y="206" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">40</text><line x1="49" y1="162" x2="55" y2="162" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="166" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><line x1="49" y1="134" x2="55" y2="134" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="138" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><line x1="49" y1="106" x2="55" y2="106" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="110" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">3</text><line x1="49" y1="78" x2="55" y2="78" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="82" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4</text><line x1="49" y1="50" x2="55" y2="50" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="54" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">5</text><line x1="49" y1="22" x2="55" y2="22" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="26" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">6</text><text x="322" y="224" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">t (s)</text><text x="60" y="14" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">u_C (V)</text><line x1="52" y1="190" x2="326" y2="55.6" stroke="#0f6e56" stroke-width="2.6"/><circle cx="120.5" cy="156.4" r="3.6" fill="#c2410c" stroke="#0f172a" stroke-width="1"/><circle cx="189" cy="122.8" r="3.6" fill="#c2410c" stroke="#0f172a" stroke-width="1"/><circle cx="257.5" cy="89.2" r="3.6" fill="#c2410c" stroke="#0f172a" stroke-width="1"/><circle cx="326" cy="55.6" r="3.6" fill="#c2410c" stroke="#0f172a" stroke-width="1"/><line x1="326" y1="190" x2="326" y2="55.6" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="3 3"/><line x1="52" y1="55.6" x2="326" y2="55.6" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="5 4"/><text x="230.1" y="98.8" text-anchor="end" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">u_C = k t</text></svg>
:::

La droite passe par l'origine : u_C est proportionnelle à t. Comme q = I·t avec I constant, u_C est aussi proportionnelle à q.

::: definition
**Capacité** — La charge d'un condensateur est proportionnelle à la tension à ses bornes : **q = C·u_C**. Le coefficient C est la **capacité** ; elle ne dépend que de la géométrie et du diélectrique. Elle s'exprime en **farad** (F) : 1 F est la capacité d'un condensateur qui prend 1 C sous 1 V. Sous-multiples : 1 mF = 10⁻³ F, 1 µF = 10⁻⁶ F, 1 nF = 10⁻⁹ F, 1 pF = 10⁻¹² F.
:::

| Type de condensateur | Mica, céramique | Polypropylène | Électrochimique |
| --- | --- | --- | --- |
| Ordre de grandeur de C | pF à nF | nF à µF | µF à F |

::: exemple Trouver C avec la pente de la droite

1. La droite donne u_C = k·t avec k = 4,8 V / 40 s = 0,12 V·s⁻¹ (on lit un point éloigné de l'origine pour être précis).
2. Comme q = I·t et q = C·u_C, on obtient u_C = (I/C)·t, donc k = I/C et C = I/k.
3. C = 60·10⁻⁶ A / 0,12 V·s⁻¹ = 5,0·10⁻⁴ F = 500 µF.
4. Contrôle à t = 20 s : q = I·t = 60 µA × 20 s = 1,2 mC et q/u_C = 1,2·10⁻³ C / 2,4 V = 5,0·10⁻⁴ F ✓.

:::

> ⚠️ Piège classique : oublier un préfixe. Le farad est une très grande unité ; laisser un µF à la place d'un F fausse le résultat d'un facteur un million. Convertis avant de calculer.

::: propriete
**Charge à courant constant** — À C fixée, q est proportionnelle à u_C. Avec un courant constant I, u_C = (I/C)·t : la pente k de la droite vaut I/C. En général, C étant constante, i = dq/dt = C·du_C/dt : le signe de i est celui de la pente de u_C(t). Cas limite : à t = 0, q = 0 et u_C = 0 (condensateur neutre).
:::

::: verifie À toi : même montage, autres mesures
Avec I = 0,24 mA, la droite u_C(t) a pour pente k = 0,060 V·s⁻¹. Que vaut C ?

---

On a k = I/C donc C = I/k = 0,24·10⁻³ A / 0,060 V·s⁻¹ = 4,0·10⁻³ F = 4,0 mF : la pente est le rapport du courant à la capacité.
:::

::: retenir
q = C·u_C : à C fixée la charge est proportionnelle à la tension ; C se mesure en farads, avec ses sous-multiples µF, nF, pF.
:::

## 🧱 Le condensateur plan ; tensions de service et de claquage

Pour fabriquer un condensateur maison, on sépare deux feuilles d'aluminium par du papier. Qu'est-ce qui, dans la construction, fixe la capacité, et que se passe-t-il si la tension appliquée devient trop grande ?

::: figure Un condensateur plan : S est la surface des armatures en regard, e leur écartement, ε la permittivité du diélectrique qui les sépare
<svg viewBox="0 0 340 185"><title>Condensateur plan : deux armatures de surface S en regard, séparées par une distance e occupée par un diélectrique de permittivité ε</title><rect x="80" y="64" width="190" height="8" fill="#94a3b8" stroke="#0f172a" stroke-width="1.6"/><rect x="80" y="72" width="190" height="42" fill="#fed7aa" stroke="#0f172a" stroke-width="1.2"/><rect x="80" y="114" width="190" height="8" fill="#94a3b8" stroke="#0f172a" stroke-width="1.6"/><line x1="175" y1="64" x2="175" y2="30" stroke="#0f172a" stroke-width="1.6"/><line x1="175" y1="122" x2="175" y2="156" stroke="#0f172a" stroke-width="1.6"/><text x="175" y="22" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">A</text><text x="175" y="172" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">B</text><line x1="292" y1="72" x2="292" y2="114" stroke="#0f172a" stroke-width="1.6"/><polygon points="292,72 296,80 288,80" fill="#0f172a"/><polygon points="292,114 288,106 296,106" fill="#0f172a"/><text x="306" y="97" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">e</text><text x="175" y="98" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">diélectrique ε</text><text x="104" y="56" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">armature : surface S</text></svg>
:::

Ces trois grandeurs S, e et ε sont celles de la formule qui suit.

::: propriete
**Capacité d'un condensateur plan** — La capacité est proportionnelle à S et inversement proportionnelle à e :

$$ C = ε·S/e = ε_r·ε₀·S/e $$

ε est la **permittivité absolue** du diélectrique, en F·m⁻¹. Pour le vide, ε₀ = 1/(36π·10⁹) ≈ 8,8·10⁻¹² F·m⁻¹, valeur pratiquement égale pour l'air. La **permittivité relative** est ε_r = ε/ε₀. Quelques valeurs de ε_r : air 1 ; papier paraffiné 2 à 2,5 ; polystyrène 2 à 3 ; verre 4 à 7 ; mica 5 à 8 ; céramique 15 à 2500.
:::

::: exemple Capacité d'un condensateur au verre

1. Données : S = 0,20 m², e = 0,10 mm, verre avec ε_r = 4. On convertit e = 0,10 mm = 1,0·10⁻⁴ m, car ε₀ est en F·m⁻¹.
2. ε = ε_r·ε₀ = 4 × 8,8·10⁻¹² = 3,5·10⁻¹¹ F·m⁻¹ (la permittivité du verre est celle du vide multipliée par ε_r).
3. C = ε·S/e = 3,5·10⁻¹¹ × 0,20 / 1,0·10⁻⁴ = 7,0·10⁻⁸ F = 70 nF.
4. Si on rapproche les armatures jusqu'à e = 0,050 mm, C double, car e est au dénominateur.

:::

> ⚠️ Piège classique : garder e en millimètres ou S en cm² dans la formule. Le résultat est alors faux d'un facteur 1000 ou 10 000. Convertis e en mètres et S en m² avant de calculer.

::: propriete
**Tensions caractéristiques** — Si la tension est trop grande, une étincelle jaillit dans le diélectrique : c'est le **claquage**. La **tension de claquage** est la plus petite tension, en valeur absolue, qui fait jaillir cette étincelle. La **tension de service**, inscrite sur le boîtier, est la tension nominale ; elle est nettement inférieure à la tension de claquage.
:::

::: verifie À toi : changer de diélectrique
Dans le condensateur de l'exemple, on remplace le verre (ε_r = 4) par du mica (ε_r = 6), sans toucher à S ni à e. Que devient C ?

---

C = ε_r·ε₀·S/e est proportionnelle à ε_r, et S, e, ε₀ ne changent pas : C est multipliée par 6/4 = 1,5, soit 1,05·10⁻⁷ F, environ 0,11 µF.
:::

::: retenir
C = ε·S/e = ε_r·ε₀·S/e pour un condensateur plan, avec S en m² et e en m ; la tension de service reste nettement sous la tension de claquage.
:::

## 🔋 L'énergie emmagasinée par un condensateur

Un condensateur de grande capacité, chargé sous une tension réglable, fait tourner un petit moteur quand on le ferme dessus, puis le moteur s'arrête.
D'où vient l'énergie du moteur, et de quoi dépend la quantité d'énergie stockée ?

::: definition
**Énergie emmagasinée** — Un condensateur est un réservoir d'énergie potentielle électrique. Sous la tension u, avec C en F, u en V et E_C en J, il emmagasine :

$$ E_C = ½·C·u² = q²/(2C) = ½·q·u $$
:::

Les trois écritures sont équivalentes puisque q = C·u : on prend celle qui utilise les données de l'énoncé. À la décharge, cette énergie devient de la chaleur dans les conducteurs, de l'énergie cinétique dans un moteur ou de la lumière dans une DEL.

::: exemple Énergie d'un condensateur de 2200 µF sous 9,0 V

1. Avec la tension : E_C = ½ × 2200·10⁻⁶ F × (9,0 V)² = ½ × 2,2·10⁻³ × 81 = 8,9·10⁻² J.
2. Avec la charge : q = C·u = 2,2·10⁻³ × 9,0 = 1,98·10⁻² C, puis ½·q·u = ½ × 1,98·10⁻² × 9,0 = 8,9·10⁻² J ✓ : les deux écritures donnent le même résultat.
3. Si la tension passe de 9,0 V à 18 V, l'énergie est multipliée par 2² = 4, soit 0,36 J.

:::

> ⚠️ Piège classique : « si je double la tension, j'ai deux fois plus d'énergie ». Non : u est élevée au carré, donc doubler u multiplie E_C par **4**. Autre oubli fréquent : le facteur ½.

::: propriete
**Proportionnalités** — À tension fixée, E_C est proportionnelle à C. À capacité fixée, E_C est proportionnelle à u² (et à q²). Cas limite : à u = 0, E_C = 0.
:::

::: verifie À toi : une énergie
Quelle énergie emmagasine un condensateur de 1,0 mF chargé sous 12 V ?

---

E_C = ½·C·u² = ½ × 1,0·10⁻³ × 12² = ½ × 1,0·10⁻³ × 144 = 7,2·10⁻² J, soit 72 mJ : la tension est au carré et le facteur ½ est conservé.
:::

::: retenir
E_C = ½·C·u² = q²/(2C) = ½·q·u : proportionnelle à C et au carré de u, restituée à la décharge.
:::

## ⏱️ La charge d'un dipôle RC

On relie un condensateur neutre à un générateur de tension constante E à travers un résistor, et un voltmètre mesure u_C. L'aiguille ne saute pas à E : elle monte progressivement.
Selon quelle loi, et que devient le courant pendant ce temps ?

::: definition
**Dipôle RC et échelon de tension** — Un dipôle RC est un résistor de résistance R en série avec un condensateur de capacité C. Quand la tension à ses bornes passe brusquement de 0 à une valeur constante E, il reçoit un **échelon de tension**. La charge du condensateur n'est pas instantanée : c'est un **phénomène transitoire**.
:::

On applique la loi des mailles au circuit de charge, en convention récepteur, avec i = dq/dt = C·du_C/dt et u_R = R·i.

::: exemple Mettre en équation puis résoudre

1. Loi des mailles : u_R + u_C − E = 0, soit R·i + u_C = E (la tension du générateur se répartit entre R et C).
2. Avec i = C·du_C/dt : **u_C + RC·du_C/dt = E**. On pose τ = RC, d'où du_C/dt + u_C/τ = E/τ. En charge q, la même équation s'écrit dq/dt + q/τ = E/R ; en intensité, i + (1/τ)·∫ i dt = E/R.
3. On cherche u_C(t) = B + A·e^(−αt). À t = 0, u_C = 0 donne B = −A, donc u_C = A(e^(−αt) − 1).
4. On remplace dans l'équation : −A + (1 − ατ)·A·e^(−αt) = E pour tout t. Donc A = −E et 1 − ατ = 0, soit α = 1/τ.
5. D'où la solution, puis q = C·u_C et i = dq/dt :

$$ u_C(t) = E·(1 − e^(−t/τ)) $$

$$ q(t) = Q₀·(1 − e^(−t/τ)) $$

$$ i(t) = I₀·e^(−t/τ) $$

avec Q₀ = C·E et I₀ = E/R. À chaque instant, u_R = R·i = E·e^(−t/τ), donc u_R + u_C = E.

:::

Avec E = 6,0 V, R = 2,5 kΩ et C = 8,0 µF, on a τ = RC = 2,5·10³ × 8,0·10⁻⁶ = 0,020 s = 20 ms, I₀ = E/R = 2,4 mA et Q₀ = C·E = 48 µC.

::: figure La tension u_C part de 0, croît de moins en moins vite et tend vers l'asymptote E = 6,0 V ; à t = 40 ms, soit 2τ, elle vaut 5,2 V
<svg viewBox="0 0 340 230"><title>Courbe de charge u_C(t) pour E = 6,0 V et τ = 20 ms, avec le point relevé à t = 40 ms</title><line x1="52" y1="22" x2="52" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="97.7" y1="22" x2="97.7" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="143.3" y1="22" x2="143.3" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="189" y1="22" x2="189" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="234.7" y1="22" x2="234.7" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="280.3" y1="22" x2="280.3" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="326" y1="22" x2="326" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="52" y1="190" x2="326" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="52" y1="162" x2="326" y2="162" stroke="#e2e8f0" stroke-width="1"/><line x1="52" y1="134" x2="326" y2="134" stroke="#e2e8f0" stroke-width="1"/><line x1="52" y1="106" x2="326" y2="106" stroke="#e2e8f0" stroke-width="1"/><line x1="52" y1="78" x2="326" y2="78" stroke="#e2e8f0" stroke-width="1"/><line x1="52" y1="50" x2="326" y2="50" stroke="#e2e8f0" stroke-width="1"/><line x1="52" y1="22" x2="326" y2="22" stroke="#e2e8f0" stroke-width="1"/><line x1="52" y1="190" x2="332" y2="190" stroke="#0f172a" stroke-width="1.6"/><line x1="52" y1="196" x2="52" y2="16" stroke="#0f172a" stroke-width="1.6"/><polygon points="336,190 328,186 328,194" fill="#0f172a"/><polygon points="52,12 48,20 56,20" fill="#0f172a"/><line x1="52" y1="187" x2="52" y2="193" stroke="#0f172a" stroke-width="1.2"/><text x="52" y="206" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><line x1="97.7" y1="187" x2="97.7" y2="193" stroke="#0f172a" stroke-width="1.2"/><text x="97.7" y="206" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">20</text><line x1="143.3" y1="187" x2="143.3" y2="193" stroke="#0f172a" stroke-width="1.2"/><text x="143.3" y="206" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">40</text><line x1="189" y1="187" x2="189" y2="193" stroke="#0f172a" stroke-width="1.2"/><text x="189" y="206" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">60</text><line x1="234.7" y1="187" x2="234.7" y2="193" stroke="#0f172a" stroke-width="1.2"/><text x="234.7" y="206" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">80</text><line x1="280.3" y1="187" x2="280.3" y2="193" stroke="#0f172a" stroke-width="1.2"/><text x="280.3" y="206" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">100</text><line x1="326" y1="187" x2="326" y2="193" stroke="#0f172a" stroke-width="1.2"/><text x="326" y="206" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">120</text><line x1="49" y1="162" x2="55" y2="162" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="166" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><line x1="49" y1="134" x2="55" y2="134" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="138" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><line x1="49" y1="106" x2="55" y2="106" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="110" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">3</text><line x1="49" y1="78" x2="55" y2="78" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="82" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4</text><line x1="49" y1="50" x2="55" y2="50" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="54" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">5</text><line x1="49" y1="22" x2="55" y2="22" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="26" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">6</text><text x="322" y="224" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">t (ms)</text><text x="60" y="14" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">u_C (V)</text><line x1="52" y1="22" x2="326" y2="22" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="5 4"/><text x="322" y="16" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">E</text><polyline points="52,190 54.3,181.8 56.6,174 58.9,166.6 61.1,159.5 63.4,152.8 65.7,146.5 68,140.4 70.3,134.6 72.5,129.1 74.8,123.9 77.1,118.9 79.4,114.2 81.7,109.7 84,105.4 86.2,101.4 88.5,97.5 90.8,93.8 93.1,90.3 95.4,87 97.7,83.8 100,80.8 102.2,77.9 104.5,75.2 106.8,72.6 109.1,70.1 111.4,67.8 113.7,65.6 115.9,63.4 118.2,61.4 120.5,59.5 122.8,57.7 125.1,55.9 127.3,54.3 129.6,52.7 131.9,51.2 134.2,49.8 136.5,48.4 138.8,47.1 141.1,45.9 143.3,44.7 145.6,43.6 147.9,42.6 150.2,41.6 152.5,40.6 154.8,39.7 157,38.8 159.3,38 161.6,37.2 163.9,36.5 166.2,35.8 168.4,35.1 170.7,34.5 173,33.9 175.3,33.3 177.6,32.7 179.9,32.2 182.2,31.7 184.4,31.2 186.7,30.8 189,30.4 191.3,30 193.6,29.6 195.8,29.2 198.1,28.8 200.4,28.5 202.7,28.2 205,27.9 207.3,27.6 209.6,27.3 211.8,27.1 214.1,26.8 216.4,26.6 218.7,26.4 221,26.2 223.2,26 225.5,25.8 227.8,25.6 230.1,25.4 232.4,25.2 234.7,25.1 236.9,24.9 239.2,24.8 241.5,24.6 243.8,24.5 246.1,24.4 248.4,24.3 250.7,24.2 252.9,24.1 255.2,24 257.5,23.9 259.8,23.8 262.1,23.7 264.4,23.6 266.6,23.5 268.9,23.5 271.2,23.4 273.5,23.3 275.8,23.3 278.1,23.2 280.3,23.1 282.6,23.1 284.9,23 287.2,23 289.5,22.9 291.8,22.9 294,22.8 296.3,22.8 298.6,22.8 300.9,22.7 303.2,22.7 305.4,22.7 307.7,22.6 310,22.6 312.3,22.6 314.6,22.5 316.9,22.5 319.1,22.5 321.4,22.5 323.7,22.4 326,22.4" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"/><line x1="143.3" y1="190" x2="143.3" y2="44.7" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="3 3"/><line x1="52" y1="44.7" x2="143.3" y2="44.7" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="5 4"/><circle cx="143.3" cy="44.7" r="3.6" fill="#0f6e56" stroke="#0f172a" stroke-width="1"/><text x="151.3" y="62.7" text-anchor="start" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">5,2 V</text></svg>
:::

Sur la figure, E est l'asymptote horizontale de la courbe et τ = 20 ms l'échelle de temps qui règle sa montée.

::: exemple Valeurs à t = 40 ms

1. t/τ = 40 / 20 = 2 et e^(−2) ≈ 0,135.
2. u_C = E(1 − e^(−2)) = 6,0 × 0,865 ≈ 5,2 V, ce que montre le point de la figure.
3. i = I₀·e^(−2) = 2,4 × 0,135 ≈ 0,32 mA, positif pendant la charge.
4. Q₀ = 48 µC est la charge maximale, atteinte quand t tend vers l'infini.

:::

> ⚠️ Piège classique : « le condensateur est neutre donc i = 0 à t = 0 ». Faux : c'est la **tension** u_C qui vaut 0, et elle ne peut pas sauter. Toute la tension E se retrouve alors aux bornes de R, donc i(0) = E/R = I₀, le maximum. C'est en fin de charge que i tend vers 0.

::: propriete
**Charge d'un dipôle RC** — Au début u_C = 0 et i = E/R ; à la fin u_C = E, q = C·E et i = 0 ; entre les deux u_C et q croissent exponentiellement tandis que i décroît exponentiellement. Pour observer u_C(t) à l'oscilloscope, on relie la masse à B et l'entrée à A ; pour voir en même temps u_R = R·i, on place la masse en A (entre R et C), ce qui exige un générateur à masse flottante ; la voie branchée sur B affiche alors u_BA = −u_C, que le bouton INV remet dans le bon sens. Sans oscilloscope à mémoire, on alimente le dipôle par un GBF en créneaux pour répéter charges et décharges.
:::

::: verifie À toi : une charge numérique
E = 15 V, R = 5,0 kΩ, C = 2,0 µF. Donne τ, I₀ et la tension u_C à t = τ.

---

τ = R·C = 5,0·10³ × 2,0·10⁻⁶ = 1,0·10⁻² s = 10 ms ; I₀ = E/R = 15 / 5,0·10³ = 3,0 mA ; à t = τ, u_C = E(1 − e^(−1)) = 15 × 0,63 ≈ 9,5 V.
:::

::: retenir
Charge : u_C = E(1 − e^(−t/τ)), q = Q₀(1 − e^(−t/τ)), i = I₀·e^(−t/τ), avec τ = RC, Q₀ = CE, I₀ = E/R.
:::

## 🔻 La décharge d'un condensateur dans un résistor

Le condensateur est chargé sous E ; on bascule K en position 2 et il se ferme sur R, sans générateur.
Comment u_C, q et i évoluent-ils, et dans quel sens circule le courant ?

::: exemple Mettre en équation puis résoudre

1. Loi des mailles : u_C + u_R = 0, soit u_C + R·i = 0. Avec i = C·du_C/dt : **u_C + RC·du_C/dt = 0** ; il n'y a plus de second membre, faute de générateur ; de même, dq/dt + q/τ = 0.
2. On cherche u_C = A·e^(−αt). À t = 0, u_C = E donne A = E.
3. On remplace dans l'équation : (−α + 1/τ)·A·e^(−αt) = 0 pour tout t, donc α = 1/τ.
4. Avec q = C·u_C et i = dq/dt :

$$ u_C(t) = E·e^(−t/τ) $$

$$ q(t) = Q₀·e^(−t/τ) $$

$$ i(t) = −I₀·e^(−t/τ) $$

avec Q₀ = C·E et I₀ = E/R.

:::

Même circuit qu'avant : E = 6,0 V, τ = 20 ms, I₀ = 2,4 mA.

::: figure Décharge depuis E = 6,0 V : u_C part de E et tend vers 0 sans jamais s'annuler ; à t = τ = 20 ms elle vaut 2,2 V
<svg viewBox="0 0 340 230"><title>Courbe de décharge u_C(t) depuis E = 6,0 V avec τ = 20 ms, avec le point relevé à t = 20 ms</title><line x1="52" y1="22" x2="52" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="97.7" y1="22" x2="97.7" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="143.3" y1="22" x2="143.3" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="189" y1="22" x2="189" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="234.7" y1="22" x2="234.7" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="280.3" y1="22" x2="280.3" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="326" y1="22" x2="326" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="52" y1="190" x2="326" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="52" y1="162" x2="326" y2="162" stroke="#e2e8f0" stroke-width="1"/><line x1="52" y1="134" x2="326" y2="134" stroke="#e2e8f0" stroke-width="1"/><line x1="52" y1="106" x2="326" y2="106" stroke="#e2e8f0" stroke-width="1"/><line x1="52" y1="78" x2="326" y2="78" stroke="#e2e8f0" stroke-width="1"/><line x1="52" y1="50" x2="326" y2="50" stroke="#e2e8f0" stroke-width="1"/><line x1="52" y1="22" x2="326" y2="22" stroke="#e2e8f0" stroke-width="1"/><line x1="52" y1="190" x2="332" y2="190" stroke="#0f172a" stroke-width="1.6"/><line x1="52" y1="196" x2="52" y2="16" stroke="#0f172a" stroke-width="1.6"/><polygon points="336,190 328,186 328,194" fill="#0f172a"/><polygon points="52,12 48,20 56,20" fill="#0f172a"/><line x1="52" y1="187" x2="52" y2="193" stroke="#0f172a" stroke-width="1.2"/><text x="52" y="206" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><line x1="97.7" y1="187" x2="97.7" y2="193" stroke="#0f172a" stroke-width="1.2"/><text x="97.7" y="206" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">20</text><line x1="143.3" y1="187" x2="143.3" y2="193" stroke="#0f172a" stroke-width="1.2"/><text x="143.3" y="206" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">40</text><line x1="189" y1="187" x2="189" y2="193" stroke="#0f172a" stroke-width="1.2"/><text x="189" y="206" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">60</text><line x1="234.7" y1="187" x2="234.7" y2="193" stroke="#0f172a" stroke-width="1.2"/><text x="234.7" y="206" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">80</text><line x1="280.3" y1="187" x2="280.3" y2="193" stroke="#0f172a" stroke-width="1.2"/><text x="280.3" y="206" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">100</text><line x1="326" y1="187" x2="326" y2="193" stroke="#0f172a" stroke-width="1.2"/><text x="326" y="206" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">120</text><line x1="49" y1="162" x2="55" y2="162" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="166" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><line x1="49" y1="134" x2="55" y2="134" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="138" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><line x1="49" y1="106" x2="55" y2="106" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="110" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">3</text><line x1="49" y1="78" x2="55" y2="78" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="82" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4</text><line x1="49" y1="50" x2="55" y2="50" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="54" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">5</text><line x1="49" y1="22" x2="55" y2="22" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="26" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">6</text><text x="322" y="224" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">t (ms)</text><text x="60" y="14" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">u_C (V)</text><polyline points="52,22 54.3,30.2 56.6,38 58.9,45.4 61.1,52.5 63.4,59.2 65.7,65.5 68,71.6 70.3,77.4 72.5,82.9 74.8,88.1 77.1,93.1 79.4,97.8 81.7,102.3 84,106.6 86.2,110.6 88.5,114.5 90.8,118.2 93.1,121.7 95.4,125 97.7,128.2 100,131.2 102.2,134.1 104.5,136.8 106.8,139.4 109.1,141.9 111.4,144.2 113.7,146.4 115.9,148.6 118.2,150.6 120.5,152.5 122.8,154.3 125.1,156.1 127.3,157.7 129.6,159.3 131.9,160.8 134.2,162.2 136.5,163.6 138.8,164.9 141.1,166.1 143.3,167.3 145.6,168.4 147.9,169.4 150.2,170.4 152.5,171.4 154.8,172.3 157,173.2 159.3,174 161.6,174.8 163.9,175.5 166.2,176.2 168.4,176.9 170.7,177.5 173,178.1 175.3,178.7 177.6,179.3 179.9,179.8 182.2,180.3 184.4,180.8 186.7,181.2 189,181.6 191.3,182 193.6,182.4 195.8,182.8 198.1,183.2 200.4,183.5 202.7,183.8 205,184.1 207.3,184.4 209.6,184.7 211.8,184.9 214.1,185.2 216.4,185.4 218.7,185.6 221,185.8 223.2,186 225.5,186.2 227.8,186.4 230.1,186.6 232.4,186.8 234.7,186.9 236.9,187.1 239.2,187.2 241.5,187.4 243.8,187.5 246.1,187.6 248.4,187.7 250.7,187.8 252.9,187.9 255.2,188 257.5,188.1 259.8,188.2 262.1,188.3 264.4,188.4 266.6,188.5 268.9,188.5 271.2,188.6 273.5,188.7 275.8,188.7 278.1,188.8 280.3,188.9 282.6,188.9 284.9,189 287.2,189 289.5,189.1 291.8,189.1 294,189.2 296.3,189.2 298.6,189.2 300.9,189.3 303.2,189.3 305.4,189.3 307.7,189.4 310,189.4 312.3,189.4 314.6,189.5 316.9,189.5 319.1,189.5 321.4,189.5 323.7,189.6 326,189.6" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"/><line x1="97.7" y1="190" x2="97.7" y2="128.2" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="3 3"/><line x1="52" y1="128.2" x2="97.7" y2="128.2" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="5 4"/><circle cx="97.7" cy="128.2" r="3.6" fill="#0f6e56" stroke="#0f172a" stroke-width="1"/><text x="105.7" y="122.2" text-anchor="start" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2,2 V</text><text x="60" y="38" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">E = 6,0 V</text></svg>
:::

La courbe est l'image « retournée » de la charge : u_C est ici la valeur de départ E multipliée par e^(−t/τ).

::: figure Le courant i vaut +I₀ au début de la charge, tend vers 0, puis passe à −I₀ quand K bascule en 2 à t = 120 ms, et revient vers 0 par valeurs négatives (I₀ = 2,4 mA)
<svg viewBox="0 0 340 230"><title>Intensité i(t) : positive et décroissante pendant la charge, négative et croissante vers 0 pendant la décharge, après la bascule de K à t = 120 ms</title><line x1="52" y1="22" x2="52" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="106.8" y1="22" x2="106.8" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="161.6" y1="22" x2="161.6" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="216.4" y1="22" x2="216.4" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="271.2" y1="22" x2="271.2" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="326" y1="22" x2="326" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="52" y1="173.2" x2="326" y2="173.2" stroke="#e2e8f0" stroke-width="1"/><line x1="52" y1="139.6" x2="326" y2="139.6" stroke="#e2e8f0" stroke-width="1"/><line x1="52" y1="106" x2="326" y2="106" stroke="#e2e8f0" stroke-width="1"/><line x1="52" y1="72.4" x2="326" y2="72.4" stroke="#e2e8f0" stroke-width="1"/><line x1="52" y1="38.8" x2="326" y2="38.8" stroke="#e2e8f0" stroke-width="1"/><line x1="52" y1="106" x2="332" y2="106" stroke="#0f172a" stroke-width="1.6"/><line x1="52" y1="196" x2="52" y2="16" stroke="#0f172a" stroke-width="1.6"/><polygon points="336,106 328,102 328,110" fill="#0f172a"/><polygon points="52,12 48,20 56,20" fill="#0f172a"/><line x1="52" y1="103" x2="52" y2="109" stroke="#0f172a" stroke-width="1.2"/><text x="52" y="122" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><line x1="106.8" y1="103" x2="106.8" y2="109" stroke="#0f172a" stroke-width="1.2"/><text x="106.8" y="122" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">40</text><line x1="161.6" y1="103" x2="161.6" y2="109" stroke="#0f172a" stroke-width="1.2"/><text x="161.6" y="122" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">80</text><line x1="216.4" y1="103" x2="216.4" y2="109" stroke="#0f172a" stroke-width="1.2"/><text x="216.4" y="122" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">120</text><line x1="271.2" y1="103" x2="271.2" y2="109" stroke="#0f172a" stroke-width="1.2"/><text x="271.2" y="122" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">160</text><line x1="326" y1="103" x2="326" y2="109" stroke="#0f172a" stroke-width="1.2"/><text x="326" y="122" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">200</text><line x1="49" y1="173.2" x2="55" y2="173.2" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="177.2" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−2,4</text><line x1="49" y1="139.6" x2="55" y2="139.6" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="143.6" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−1,2</text><line x1="49" y1="72.4" x2="55" y2="72.4" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="76.4" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1,2</text><line x1="49" y1="38.8" x2="55" y2="38.8" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="42.8" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2,4</text><text x="322" y="97" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">t (ms)</text><text x="60" y="14" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">i (mA)</text><line x1="216.4" y1="190" x2="216.4" y2="22" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="5 4"/><polyline points="52,38.8 53.4,42.1 54.7,45.2 56.1,48.2 57.5,51 58.9,53.7 60.2,56.2 61.6,58.6 63,61 64.3,63.2 65.7,65.2 67.1,67.2 68.4,69.1 69.8,70.9 71.2,72.6 72.5,74.3 73.9,75.8 75.3,77.3 76.7,78.7 78,80 79.4,81.3 80.8,82.5 82.1,83.6 83.5,84.7 84.9,85.8 86.2,86.7 87.6,87.7 89,88.6 90.4,89.4 91.7,90.2 93.1,91 94.5,91.7 95.8,92.4 97.2,93.1 98.6,93.7 100,94.3 101.3,94.9 102.7,95.4 104.1,95.9 105.4,96.4 106.8,96.9 108.2,97.3 109.5,97.8 110.9,98.2 112.3,98.6 113.7,98.9 115,99.3 116.4,99.6 117.8,99.9 119.1,100.2 120.5,100.5 121.9,100.8 123.2,101 124.6,101.3 126,101.5 127.3,101.7 128.7,101.9 130.1,102.1 131.5,102.3 132.8,102.5 134.2,102.7 135.6,102.8 136.9,103 138.3,103.1 139.7,103.3 141.1,103.4 142.4,103.5 143.8,103.6 145.2,103.8 146.5,103.9 147.9,104 149.3,104.1 150.6,104.2 152,104.3 153.4,104.3 154.8,104.4 156.1,104.5 157.5,104.6 158.9,104.6 160.2,104.7 161.6,104.8 163,104.8 164.3,104.9 165.7,104.9 167.1,105 168.4,105 169.8,105.1 171.2,105.1 172.6,105.2 173.9,105.2 175.3,105.3 176.7,105.3 178,105.3 179.4,105.4 180.8,105.4 182.2,105.4 183.5,105.4 184.9,105.5 186.3,105.5 187.6,105.5 189,105.5 190.4,105.6 191.7,105.6 193.1,105.6 194.5,105.6 195.8,105.6 197.2,105.7 198.6,105.7 200,105.7 201.3,105.7 202.7,105.7 204.1,105.7 205.4,105.8 206.8,105.8 208.2,105.8 209.6,105.8 210.9,105.8 212.3,105.8 213.7,105.8 215,105.8 216.4,105.8" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"/><line x1="216.4" y1="105.8" x2="216.4" y2="173.2" stroke="#0f6e56" stroke-width="1.6" stroke-dasharray="2 3"/><polyline points="216.4,173.2 217.8,169.9 219.1,166.8 220.5,163.8 221.9,161 223.2,158.3 224.6,155.8 226,153.4 227.4,151 228.7,148.8 230.1,146.8 231.5,144.8 232.8,142.9 234.2,141.1 235.6,139.4 236.9,137.7 238.3,136.2 239.7,134.7 241.1,133.3 242.4,132 243.8,130.7 245.2,129.5 246.5,128.4 247.9,127.3 249.3,126.2 250.7,125.3 252,124.3 253.4,123.4 254.8,122.6 256.1,121.8 257.5,121 258.9,120.3 260.2,119.6 261.6,118.9 263,118.3 264.4,117.7 265.7,117.1 267.1,116.6 268.5,116.1 269.8,115.6 271.2,115.1 272.6,114.7 273.9,114.2 275.3,113.8 276.7,113.4 278.1,113.1 279.4,112.7 280.8,112.4 282.2,112.1 283.5,111.8 284.9,111.5 286.3,111.2 287.6,111 289,110.7 290.4,110.5 291.8,110.3 293.1,110.1 294.5,109.9 295.9,109.7 297.2,109.5 298.6,109.3 300,109.2 301.3,109 302.7,108.9 304.1,108.7 305.4,108.6 306.8,108.5 308.2,108.4 309.6,108.2 310.9,108.1 312.3,108 313.7,107.9 315,107.8 316.4,107.7 317.8,107.7 319.1,107.6 320.5,107.5 321.9,107.4 323.3,107.4 324.6,107.3 326,107.2" fill="none" stroke="#c2410c" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"/><text x="222.4" y="34" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">K en 2</text><text x="64.2" y="33.8" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">K en 1</text></svg>
:::

Sur le graphe, le courant, devenu presque nul en fin de charge, saute à −I₀ au moment de la bascule : le courant de décharge circule en sens contraire de celui de la charge.

::: exemple Valeurs à t = τ

1. t = τ = 20 ms et e^(−1) ≈ 0,37 : u_C(τ) = 6,0 × 0,37 ≈ 2,2 V.
2. i(τ) = −I₀·e^(−1) = −2,4 × 0,37 ≈ −0,88 mA : négatif, car q diminue.
3. L'énergie du départ, ½·C·E² = ½ × 8,0·10⁻⁶ × 36 = 1,4·10⁻⁴ J, est dissipée peu à peu par effet Joule dans R.

:::

> ⚠️ Piège classique : écrire i(t) = +I₀·e^(−t/τ) pour la décharge. Ce signe + décrirait un courant de même sens que celui de la charge, alors que q diminue : i = dq/dt est négatif.

::: propriete
**Décharge d'un dipôle RC** — u_C = E·e^(−t/τ) décroît de E vers 0 ; q = Q₀·e^(−t/τ) tend vers 0 ; i = −I₀·e^(−t/τ) est négatif et tend vers 0 par valeurs négatives. Toute l'énergie ½·C·E² finit en chaleur dans le résistor, quelle que soit R.
:::

::: verifie À toi : une décharge numérique
E = 12 V, R = 3,0 kΩ, C = 1,0 µF. Quelles valeurs de u_C et de i à t = 6,0 ms ?

---

τ = RC = 3,0·10³ × 1,0·10⁻⁶ = 3,0 ms, donc t = 2τ et e^(−2) ≈ 0,135. u_C = 12 × 0,135 ≈ 1,6 V ; I₀ = 12 / 3,0·10³ = 4,0 mA, donc i = −4,0 × 0,135 ≈ −0,54 mA (négatif : décharge).
:::

::: retenir
Décharge : u_C = E·e^(−t/τ), q = Q₀·e^(−t/τ), i = −I₀·e^(−t/τ) : le courant est négatif et l'énergie finit en chaleur dans R.
:::

## 🎯 La constante de temps τ = RC

Avec C fixée, une résistance plus grande ralentit la charge ; avec R fixée, une capacité plus grande aussi.
Comment résumer en un seul nombre la rapidité d'un dipôle RC, et comment le lire sur une courbe ?

::: definition
**Constante de temps** — **τ = R·C**. Elle a la dimension d'un temps : R = u/i et C = q/u = i·t/u, donc R·C = t, et τ s'exprime en secondes quand R est en ohms et C en farads. Plus τ est petite, plus la charge et la décharge sont rapides.
:::

Voici ce qu'on obtient en changeant R ou C, la durée de charge à 1 % près valant environ 4,6 τ :

| R | C | τ = RC | durée à 1 % près |
| --- | --- | --- | --- |
| 5 kΩ | 1,0 µF | 5,0 ms | 23 ms |
| 10 kΩ | 1,0 µF | 10 ms | 46 ms |
| 20 kΩ | 1,0 µF | 20 ms | 92 ms |
| 10 kΩ | 2,0 µF | 20 ms | 92 ms |

La durée est proportionnelle à R et à C, donc à leur produit : les deux dernières lignes ont le même τ, donc la même durée.

::: figure Lecture de τ sur la courbe de charge (E = 6,0 V) : la tangente à l'origine coupe l'asymptote d'ordonnée E à l'instant t = τ = 20 ms, et la courbe passe par 0,63 E à ce même instant
<svg viewBox="0 0 340 230"><title>Courbe de charge avec sa tangente à l'origine : elle coupe l'asymptote d'ordonnée E en t = τ, où la courbe vaut 0,63 E</title><line x1="52" y1="22" x2="52" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="97.7" y1="22" x2="97.7" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="143.3" y1="22" x2="143.3" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="189" y1="22" x2="189" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="234.7" y1="22" x2="234.7" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="280.3" y1="22" x2="280.3" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="326" y1="22" x2="326" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="52" y1="190" x2="326" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="52" y1="162" x2="326" y2="162" stroke="#e2e8f0" stroke-width="1"/><line x1="52" y1="134" x2="326" y2="134" stroke="#e2e8f0" stroke-width="1"/><line x1="52" y1="106" x2="326" y2="106" stroke="#e2e8f0" stroke-width="1"/><line x1="52" y1="78" x2="326" y2="78" stroke="#e2e8f0" stroke-width="1"/><line x1="52" y1="50" x2="326" y2="50" stroke="#e2e8f0" stroke-width="1"/><line x1="52" y1="22" x2="326" y2="22" stroke="#e2e8f0" stroke-width="1"/><line x1="52" y1="190" x2="332" y2="190" stroke="#0f172a" stroke-width="1.6"/><line x1="52" y1="196" x2="52" y2="16" stroke="#0f172a" stroke-width="1.6"/><polygon points="336,190 328,186 328,194" fill="#0f172a"/><polygon points="52,12 48,20 56,20" fill="#0f172a"/><line x1="52" y1="187" x2="52" y2="193" stroke="#0f172a" stroke-width="1.2"/><text x="52" y="206" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><line x1="97.7" y1="187" x2="97.7" y2="193" stroke="#0f172a" stroke-width="1.2"/><text x="97.7" y="206" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">20</text><line x1="143.3" y1="187" x2="143.3" y2="193" stroke="#0f172a" stroke-width="1.2"/><text x="143.3" y="206" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">40</text><line x1="189" y1="187" x2="189" y2="193" stroke="#0f172a" stroke-width="1.2"/><text x="189" y="206" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">60</text><line x1="234.7" y1="187" x2="234.7" y2="193" stroke="#0f172a" stroke-width="1.2"/><text x="234.7" y="206" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">80</text><line x1="280.3" y1="187" x2="280.3" y2="193" stroke="#0f172a" stroke-width="1.2"/><text x="280.3" y="206" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">100</text><line x1="326" y1="187" x2="326" y2="193" stroke="#0f172a" stroke-width="1.2"/><text x="326" y="206" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">120</text><line x1="49" y1="162" x2="55" y2="162" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="166" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><line x1="49" y1="134" x2="55" y2="134" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="138" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><line x1="49" y1="106" x2="55" y2="106" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="110" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">3</text><line x1="49" y1="78" x2="55" y2="78" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="82" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4</text><line x1="49" y1="50" x2="55" y2="50" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="54" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">5</text><line x1="49" y1="22" x2="55" y2="22" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="26" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">6</text><text x="322" y="224" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">t (ms)</text><text x="60" y="14" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">u_C (V)</text><line x1="52" y1="22" x2="326" y2="22" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="5 4"/><text x="322" y="16" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">E</text><line x1="52" y1="190" x2="97.7" y2="22" stroke="#c2410c" stroke-width="1.8" stroke-dasharray="6 3"/><polyline points="52,190 54.3,181.8 56.6,174 58.9,166.6 61.1,159.5 63.4,152.8 65.7,146.5 68,140.4 70.3,134.6 72.5,129.1 74.8,123.9 77.1,118.9 79.4,114.2 81.7,109.7 84,105.4 86.2,101.4 88.5,97.5 90.8,93.8 93.1,90.3 95.4,87 97.7,83.8 100,80.8 102.2,77.9 104.5,75.2 106.8,72.6 109.1,70.1 111.4,67.8 113.7,65.6 115.9,63.4 118.2,61.4 120.5,59.5 122.8,57.7 125.1,55.9 127.3,54.3 129.6,52.7 131.9,51.2 134.2,49.8 136.5,48.4 138.8,47.1 141.1,45.9 143.3,44.7 145.6,43.6 147.9,42.6 150.2,41.6 152.5,40.6 154.8,39.7 157,38.8 159.3,38 161.6,37.2 163.9,36.5 166.2,35.8 168.4,35.1 170.7,34.5 173,33.9 175.3,33.3 177.6,32.7 179.9,32.2 182.2,31.7 184.4,31.2 186.7,30.8 189,30.4 191.3,30 193.6,29.6 195.8,29.2 198.1,28.8 200.4,28.5 202.7,28.2 205,27.9 207.3,27.6 209.6,27.3 211.8,27.1 214.1,26.8 216.4,26.6 218.7,26.4 221,26.2 223.2,26 225.5,25.8 227.8,25.6 230.1,25.4 232.4,25.2 234.7,25.1 236.9,24.9 239.2,24.8 241.5,24.6 243.8,24.5 246.1,24.4 248.4,24.3 250.7,24.2 252.9,24.1 255.2,24 257.5,23.9 259.8,23.8 262.1,23.7 264.4,23.6 266.6,23.5 268.9,23.5 271.2,23.4 273.5,23.3 275.8,23.3 278.1,23.2 280.3,23.1 282.6,23.1 284.9,23 287.2,23 289.5,22.9 291.8,22.9 294,22.8 296.3,22.8 298.6,22.8 300.9,22.7 303.2,22.7 305.4,22.7 307.7,22.6 310,22.6 312.3,22.6 314.6,22.5 316.9,22.5 319.1,22.5 321.4,22.5 323.7,22.4 326,22.4" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"/><line x1="97.7" y1="190" x2="97.7" y2="22" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="3 3"/><line x1="52" y1="83.8" x2="97.7" y2="83.8" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="5 4"/><circle cx="97.7" cy="83.8" r="3.6" fill="#0f6e56" stroke="#0f172a" stroke-width="1"/><text x="107.7" y="101.8" text-anchor="start" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0,63 E</text><text x="93.7" y="182" text-anchor="end" font-size="12" font-weight="700" fill="#c2410c" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">τ</text><text x="68" y="52" text-anchor="start" font-size="12" font-weight="700" fill="#c2410c" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">tangente</text></svg>
:::

Sur la figure, la verticale de l'abscisse τ touche à la fois la tangente (en E) et la courbe (en 0,63 E).

::: exemple Lire τ avec la tangente à l'origine

1. Au départ, du_C/dt = E/τ, donc la tangente à l'origine a pour équation u_C = E·t/τ.
2. Elle atteint u_C = E quand E·t/τ = E, soit en t = τ : sur la figure, l'intersection avec l'asymptote est à 20 ms, donc τ = 20 ms.
3. Contrôle par le calcul : τ = R·C = 2,5 kΩ × 8,0 µF = 20 ms ✓.
4. En décharge, la tangente à l'origine coupe l'axe des temps en t = τ ; sur la courbe de i(t), elle coupe aussi l'axe des temps en t = τ.

:::

Une seconde lecture du même nombre s'appuie sur la valeur de la courbe à t = τ.

::: exemple Lire τ avec 0,63 E

1. À t = τ, u_C = E(1 − e^(−1)) ≈ 0,63 E : ici 0,63 × 6,0 V ≈ 3,8 V.
2. On cherche sur la courbe l'abscisse où u_C = 3,8 V : on trouve 20 ms, donc τ = 20 ms.
3. En décharge, u_C(τ) = E·e^(−1) ≈ 0,37 E.
4. Pour une durée « complète » : u_C ≥ 0,99 E équivaut à e^(−t/τ) ≤ 0,01, soit t ≥ τ·Log 100 = 2τ·Log 10 ≈ 4,6 τ (Log désigne le logarithme népérien), donc t ≃ 5 τ. À 1 ‰ près : t ≥ τ·Log 1000 ≈ 6,9 τ ≃ 7 τ.

:::

> ⚠️ Piège classique : prendre τ pour la durée totale de la charge. À t = τ, la charge n'est faite qu'à **63 %** ; il faut environ 5 τ pour la terminer à 1 % près.

::: propriete
**Récapitulation** — Pour une charge, u_C vaut 0, 0,63 E, 0,99 E, 0,999 E aux instants 0, τ, 4,6 τ, 6,9 τ ; pour une décharge, E, 0,37 E, 0,01 E, 0,001 E aux mêmes instants. Pour qu'une grandeur de la forme e^(−t/τ) tombe à une fraction x de sa valeur initiale, il faut t = τ·Log(1/x). Cas limite : u_C n'atteint E (ou 0) qu'au bout d'une durée infinie.
:::

::: verifie À toi : lire τ en décharge
Dans une décharge, la tangente à l'origine de u_C(t) coupe l'axe des temps à t = 36 ms et R = 12 kΩ. Que vaut C ?

---

La tangente à l'origine d'une décharge coupe l'axe des temps en t = τ, donc τ = 36 ms. Alors C = τ/R = 36·10⁻³ / 12·10³ = 3,0·10⁻⁶ F = 3,0 µF.
:::

::: retenir
τ = RC en secondes : 0,63 E à t = τ en charge, 0,37 E en décharge, tangente à l'origine qui coupe l'asymptote en τ, charge terminée vers 5 τ.
:::

> 🏆 Tu sais désormais lire le temps dans une courbe : un seul nombre, τ, résume toute la dynamique d'un dipôle RC.
