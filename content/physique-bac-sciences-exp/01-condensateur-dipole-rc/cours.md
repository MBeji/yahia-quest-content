# ⚡ Le condensateur et le dipôle RC — stocker une charge, mesurer le temps

> 💡 «Un condensateur se remplit comme un réservoir, mais le robinet s'appelle une résistance : plus il est étroit, plus le plein est lent.»

Le flash d'un appareil photo se charge en quelques secondes puis se vide en un éclair : derrière ce petit miracle se cache le **condensateur**. Huit notions te mènent de sa définition jusqu'à la loi exponentielle qui règle sa charge et sa décharge : le condensateur et son fonctionnement, l'intensité algébrique et i = dq/dt, la capacité q = C·u, le condensateur plan, l'énergie emmagasinée, la charge puis la décharge d'un dipôle RC, et la constante de temps τ. On suppose acquises la loi d'Ohm, la loi des mailles et la relation Q = I·Δt.

## 🏰 Le condensateur : deux armatures qui stockent des charges

Dans un flash, une pile charge lentement un composant, qui restitue ensuite son énergie d'un coup.
Que contient ce composant, et comment « garde-t-il » quelque chose entre la charge et l'éclair ?

::: definition
**Condensateur** — Un condensateur est un composant électrique formé de deux plaques conductrices très faiblement espacées, les **armatures**, séparées par un isolant, le **diélectrique** (air, papier imbibé de paraffine, céramique, mica, alumine…). C'est un dipôle : ses deux bornes sont reliées directement à ses armatures.
:::

Regarde le montage de charge et de décharge : le générateur de f.é.m. E, le résistor R, le condensateur C et le commutateur K, qui relie le point D soit au pôle + du générateur (position 1), soit à la borne B (position 2).

::: figure Circuit de charge et de décharge : en position 1 le générateur charge le condensateur à travers R, en position 2 le condensateur se ferme sur R ; la flèche i indique le sens positif choisi (vers l'armature A)
<svg viewBox="0 0 340 175"><title>Circuit de charge et de décharge : générateur E, commutateur K, résistor R, condensateur C</title><line x1="40" y1="40" x2="110" y2="40" stroke="#0f172a" stroke-width="1.6"/><line x1="40" y1="40" x2="40" y2="85" stroke="#0f172a" stroke-width="1.6"/><line x1="40" y1="95" x2="40" y2="150" stroke="#0f172a" stroke-width="1.6"/><line x1="28" y1="85" x2="52" y2="85" stroke="#0f172a" stroke-width="2.6"/><line x1="33" y1="95" x2="47" y2="95" stroke="#0f172a" stroke-width="2.6"/><line x1="40" y1="150" x2="270" y2="150" stroke="#0f172a" stroke-width="1.6"/><line x1="110" y1="110" x2="110" y2="150" stroke="#0f172a" stroke-width="1.6"/><circle cx="110" cy="40" r="3.2" fill="#fff" stroke="#0f172a" stroke-width="1"/><circle cx="110" cy="110" r="3.2" fill="#fff" stroke="#0f172a" stroke-width="1"/><circle cx="170" cy="75" r="3.6" fill="#0f172a" stroke="#0f172a" stroke-width="1"/><line x1="170" y1="75" x2="110" y2="40" stroke="#0f172a" stroke-width="2.4"/><line x1="170" y1="75" x2="110" y2="110" stroke="#94a3b8" stroke-width="1.6" stroke-dasharray="4 3"/><line x1="170" y1="75" x2="200" y2="75" stroke="#0f172a" stroke-width="1.6"/><rect x="200" y="67" width="40" height="16" fill="#fff7ed" stroke="#0f172a" stroke-width="1.8"/><line x1="240" y1="75" x2="270" y2="75" stroke="#0f172a" stroke-width="1.6"/><circle cx="270" cy="75" r="3.2" fill="#0f172a" stroke="#0f172a" stroke-width="1"/><line x1="270" y1="75" x2="270" y2="105" stroke="#0f172a" stroke-width="1.6"/><line x1="255" y1="105" x2="285" y2="105" stroke="#0f172a" stroke-width="2.6"/><line x1="255" y1="115" x2="285" y2="115" stroke="#0f172a" stroke-width="2.6"/><line x1="270" y1="115" x2="270" y2="150" stroke="#0f172a" stroke-width="1.6"/><circle cx="270" cy="150" r="3.2" fill="#0f172a" stroke="#0f172a" stroke-width="1"/><text x="28" y="70" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">+</text><text x="28" y="112" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">E</text><text x="110" y="30" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><text x="98" y="118" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><text x="148" y="64" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">K</text><text x="170" y="95" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">D</text><text x="220" y="60" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">R</text><text x="284" y="72" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">A</text><text x="284" y="160" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">B</text><text x="296" y="114" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">C</text><line x1="205" y1="97" x2="243" y2="97" stroke="#c2410c" stroke-width="1.8"/><polygon points="251,97 243,93 243,101" fill="#c2410c"/><text x="228" y="115" text-anchor="middle" font-size="12" font-weight="700" fill="#c2410c" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">i</text></svg>
:::

Sur la figure, K en position 1 ferme la maille générateur – R – condensateur ; K en position 2 isole le générateur et ferme le condensateur sur le résistor.

::: exemple Suivre les électrons pendant la charge puis la décharge

1. Les armatures A et B sont d'abord neutres. K passe en 1 : des électrons quittent l'armature A vers le pôle + et d'autres partent du pôle − vers B, car le générateur impose sa tension aux bornes du condensateur.
2. A porte alors la charge +q et B la charge −q ; aucun électron ne traverse le diélectrique, qui est isolant : le courant circule seulement dans les fils.
3. Le courant s'arrête quand la tension entre A et B est égale à celle du générateur. Si on ouvre le circuit puis qu'on le referme, plus rien ne bouge : le condensateur est **chargé**.
4. K passe en 2 : l'attraction entre +q et −q ramène des électrons de B vers A à travers R, donc un courant de sens contraire à celui de la charge, jusqu'à ce que A et B soient de nouveau neutres : le condensateur est **déchargé**.

:::

> ⚠️ Piège classique : « le courant traverse le condensateur ». Non : pendant la charge, des électrons arrivent sur une armature et en quittent l'autre, mais le diélectrique ne laisse rien passer. Ne confonds pas non plus la **charge q** d'un condensateur (une grandeur) avec le **phénomène de charge** (une évolution dans le temps).

::: propriete
**Ce qu'il faut savoir** — Un condensateur stocke des charges électriques : +q sur une armature, −q sur l'autre. Il se charge sous une tension continue, se décharge quand on le ferme sur un récepteur, et ne se décharge pas s'il est neutre.
:::

::: verifie À toi : décharger un condensateur neutre
Un condensateur déchargé est relié à un résistor, K en position 2, sans jamais avoir été chargé. Observe-t-on un courant ?

---

Non : la décharge restitue des charges stockées, et un condensateur neutre n'en a pas (+q = −q = 0). On ne peut décharger qu'un condensateur d'abord chargé.
:::

::: retenir
Un condensateur, c'est deux armatures conductrices séparées par un isolant : il stocke +q et −q sans que rien ne traverse le diélectrique.
:::

## 🧭 L'intensité algébrique et la relation i = dq/dt

Dans le même fil, le courant de charge va vers A et le courant de décharge en revient.
Comment un seul symbole i peut-il dire les deux sens, et comment relier i à la charge stockée ?

::: definition
**Intensité algébrique** — On choisit arbitrairement un **sens positif** pour le courant. L'intensité i est positive si le courant circule dans ce sens, négative s'il circule en sens contraire. La **charge q du condensateur** est celle de l'armature vers laquelle le sens positif est orienté.
:::

::: propriete
**Relation fondamentale** — Entre t et t + Δt, le courant apporte la quantité d'électricité Δq à l'armature qui porte q ; l'intensité est la quantité d'électricité transportée par unité de temps :

$$ i = dq/dt  (limite de Δq/Δt quand Δt tend vers 0) $$
:::

::: exemple Deux sens, un seul signe

1. Le sens positif est orienté vers l'armature A. Pendant une charge, q passe de 0 à 12 µC en 3,0 s à rythme constant : i = Δq/Δt = 12 µC / 3,0 s = +4,0 µA, car q augmente.
2. Pendant une décharge, q passe de 30 µC à 18 µC en 2,0 s : i = (18 − 30) µC / 2,0 s = −6,0 µA, car q diminue.
3. Le signe − ne dit pas que l'intensité est « petite » : il dit que le courant circule de 6,0 µA dans le sens **contraire** au sens positif choisi.
4. Si q reste constante (condensateur isolé, chargé ou non), Δq = 0 donc i = 0.

:::

> ⚠️ Piège classique : « une intensité est toujours positive ». Ce n'est vrai que de sa valeur absolue : l'intensité d'un courant de décharge est **négative** dans le sens positif choisi pour la charge. Sur un oscillogramme, une tension u_R = R·i négative signale i < 0.

::: verifie À toi : lire un signe
Sur un oscilloscope, u_R = R·i passe de +4 V (K en 1) à −4 V (K en 2). Que dit ce changement de signe pour i ?

---

Comme R > 0, u_R et i ont le même signe : i est positif pendant la charge et négatif pendant la décharge. Le courant a changé de sens, ce qui est cohérent avec q qui augmentait puis diminue (i = dq/dt).
:::

::: retenir
i est une grandeur algébrique liée à la charge par i = dq/dt : positif si le courant va dans le sens choisi, négatif sinon.
:::

## 📐 La capacité : q = C·u_C

Charge un condensateur avec un **générateur de courant** qui débite toujours I = 50 µA, et relève la tension u_C à ses bornes toutes les 4 s. Comment la tension grandit-elle avec la charge accumulée ?

| t (s) | 0 | 4 | 8 | 12 | 16 |
| --- | --- | --- | --- | --- | --- |
| u_C (V) | 0 | 2,0 | 4,0 | 6,0 | 8,0 |

::: figure Les mesures sont alignées sur une droite passant par l'origine : u_C = k·t avec k = 0,50 V·s⁻¹
<svg viewBox="0 0 340 230"><title>Droite u_C = k t passant par l'origine, avec les quatre mesures du tableau</title><line x1="52" y1="22" x2="52" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="120.5" y1="22" x2="120.5" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="189" y1="22" x2="189" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="257.5" y1="22" x2="257.5" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="326" y1="22" x2="326" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="52" y1="190" x2="326" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="52" y1="148" x2="326" y2="148" stroke="#e2e8f0" stroke-width="1"/><line x1="52" y1="106" x2="326" y2="106" stroke="#e2e8f0" stroke-width="1"/><line x1="52" y1="64" x2="326" y2="64" stroke="#e2e8f0" stroke-width="1"/><line x1="52" y1="22" x2="326" y2="22" stroke="#e2e8f0" stroke-width="1"/><line x1="52" y1="190" x2="332" y2="190" stroke="#0f172a" stroke-width="1.6"/><line x1="52" y1="196" x2="52" y2="16" stroke="#0f172a" stroke-width="1.6"/><polygon points="336,190 328,186 328,194" fill="#0f172a"/><polygon points="52,12 48,20 56,20" fill="#0f172a"/><line x1="52" y1="187" x2="52" y2="193" stroke="#0f172a" stroke-width="1.2"/><text x="52" y="208" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><line x1="120.5" y1="187" x2="120.5" y2="193" stroke="#0f172a" stroke-width="1.2"/><text x="120.5" y="208" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4</text><line x1="189" y1="187" x2="189" y2="193" stroke="#0f172a" stroke-width="1.2"/><text x="189" y="208" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">8</text><line x1="257.5" y1="187" x2="257.5" y2="193" stroke="#0f172a" stroke-width="1.2"/><text x="257.5" y="208" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">12</text><line x1="326" y1="187" x2="326" y2="193" stroke="#0f172a" stroke-width="1.2"/><text x="326" y="208" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">16</text><line x1="49" y1="190" x2="55" y2="190" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="194" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><line x1="49" y1="148" x2="55" y2="148" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="152" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><line x1="49" y1="106" x2="55" y2="106" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="110" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4</text><line x1="49" y1="64" x2="55" y2="64" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="68" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">6</text><line x1="49" y1="22" x2="55" y2="22" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="26" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">8</text><text x="322" y="224" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">t (s)</text><text x="60" y="14" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">u_C (V)</text><line x1="52" y1="190" x2="326" y2="22" stroke="#0f6e56" stroke-width="2.6"/><circle cx="120.5" cy="148" r="3.6" fill="#c2410c" stroke="#0f172a" stroke-width="1"/><circle cx="189" cy="106" r="3.6" fill="#c2410c" stroke="#0f172a" stroke-width="1"/><circle cx="257.5" cy="64" r="3.6" fill="#c2410c" stroke="#0f172a" stroke-width="1"/><circle cx="326" cy="22" r="3.6" fill="#c2410c" stroke="#0f172a" stroke-width="1"/><text x="211.2" y="73" text-anchor="end" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">u_C = k t</text></svg>
:::

La droite passe par l'origine : u_C est proportionnelle à t, et comme q = I·t (I constant), u_C est aussi proportionnelle à q.

::: definition
**Capacité** — La charge q d'un condensateur est proportionnelle à la tension u_C à ses bornes : **q = C·u_C**. Le coefficient C est la **capacité** du condensateur ; elle ne dépend que de sa géométrie et du diélectrique. Son unité est le **farad** (F) : 1 F est la capacité d'un condensateur qui prend la charge de 1 C sous 1 V.
:::

::: exemple Trouver C à partir de la pente

1. La droite donne u_C = k·t avec k = 8,0 V / 16 s = 0,50 V·s⁻¹.
2. Comme q = I·t, on a u_C = (I/C)·t, donc k = I/C et C = I/k.
3. C = 50·10⁻⁶ A / 0,50 V·s⁻¹ = 1,0·10⁻⁴ F = 100 µF.
4. Vérification en t = 8 s : q = I·t = 50 µA × 8 s = 400 µC et q/u_C = 400 µC / 4,0 V = 100 µF ✓.

:::

> ⚠️ Piège classique : les préfixes. Le farad est une très grande unité : 1 mF = 10⁻³ F, 1 µF = 10⁻⁶ F, 1 nF = 10⁻⁹ F, 1 pF = 10⁻¹² F. Oublier de convertir un µF en F fausse le résultat d'un facteur un million. Ordres de grandeur : µF à F pour un condensateur électrochimique, pF à nF pour le mica ou la céramique.

::: verifie À toi : tension atteinte
Un générateur de courant débite I = 20 µA pendant 10 s dans un condensateur de 47 µF initialement neutre. Quelle tension à ses bornes ?

---

q = I·t = 20 µA × 10 s = 200 µC, puis u_C = q/C = 200 µC / 47 µF ≈ 4,3 V (les µ se simplifient : 200·10⁻⁶ / 47·10⁻⁶).
:::

::: retenir
q = C·u_C : à C fixée, la charge est proportionnelle à la tension ; C se mesure en farads (µF, nF, pF dans la pratique).
:::

## 🧱 Le condensateur plan et ses limites de tension

Pourquoi un condensateur au mica est-il minuscule tandis qu'un électrochimique est plus gros qu'une pile ? Qu'est-ce qui, dans la construction d'un condensateur, fixe sa capacité ?

::: figure Un condensateur plan : deux armatures parallèles de surface S en regard, écartées de e, séparées par un diélectrique de permittivité ε
<svg viewBox="0 0 340 175"><title>Condensateur plan : deux armatures de surface S écartées de e autour d'un diélectrique</title><rect x="70" y="60" width="180" height="8" fill="#94a3b8" stroke="#0f172a" stroke-width="1.6"/><rect x="70" y="68" width="180" height="44" fill="#fed7aa" stroke="#0f172a" stroke-width="1.2"/><rect x="70" y="112" width="180" height="8" fill="#94a3b8" stroke="#0f172a" stroke-width="1.6"/><line x1="160" y1="60" x2="160" y2="28" stroke="#0f172a" stroke-width="1.6"/><line x1="160" y1="120" x2="160" y2="152" stroke="#0f172a" stroke-width="1.6"/><line x1="268" y1="68" x2="268" y2="112" stroke="#0f172a" stroke-width="1.6"/><polygon points="268,68 264,76 272,76" fill="#0f172a"/><polygon points="268,112 264,104 272,104" fill="#0f172a"/><text x="284" y="94" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">e</text><text x="160" y="22" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">A</text><text x="160" y="166" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">B</text><text x="160" y="94" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">diélectrique (ε)</text><text x="100" y="52" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">armature, surface S</text></svg>
:::

La figure montre les trois grandeurs qui fixent C : la surface S des armatures en regard, leur écartement e et le diélectrique, de permittivité ε.

::: propriete
**Capacité d'un condensateur plan** — La capacité est proportionnelle à S et inversement proportionnelle à e :

$$ C = ε·S/e $$

ε est la **permittivité absolue** du diélectrique, en F·m⁻¹. Pour le vide, ε₀ = 1/(36π·10⁹) ≈ 8,85·10⁻¹² F·m⁻¹ ; celle de l'air est pratiquement égale à ε₀. La **permittivité relative** ε_r = ε/ε₀ donne C = ε_r·ε₀·S/e. Quelques ε_r : air 1 ; papier paraffiné 2 à 2,5 ; polystyrène 2 à 3 ; verre 4 à 7 ; mica 5 à 8 ; céramique 15 à 2500.
:::

::: exemple Capacité d'un condensateur au mica

1. Données : S = 0,50 m², e = 0,20 mm, ε_r = 5 (mica). On convertit d'abord e = 0,20 mm = 2,0·10⁻⁴ m, car ε₀ est en F·m⁻¹.
2. ε = ε_r·ε₀ = 5 × 8,85·10⁻¹² ≈ 4,4·10⁻¹¹ F·m⁻¹.
3. C = ε·S/e = 4,4·10⁻¹¹ × 0,50 / 2,0·10⁻⁴ ≈ 1,1·10⁻⁷ F, soit 0,11 µF.
4. Si on double e, S et ε_r étant inchangés, C est divisée par 2 : on gagne en capacité en rapprochant les armatures.

:::

> ⚠️ Piège classique : laisser e en millimètres (ou S en cm²) dans la formule. Le résultat est alors faux d'un facteur 1000 (ou 10 000). Convertis toujours en mètres et en m² avant de calculer.

::: propriete
**Tensions caractéristiques** — Une tension trop élevée fait jaillir une étincelle dans le diélectrique : c'est le **claquage**. La **tension de claquage** est la plus petite tension (en valeur absolue) qui fait jaillir cette étincelle. La **tension de service**, indiquée sur le boîtier, est la tension nominale : elle est nettement inférieure à la tension de claquage.
:::

::: verifie À toi : changer le diélectrique
On remplace l'air (ε_r = 1) d'un condensateur plan par du verre (ε_r = 5), sans toucher à S ni à e. Comment varie C ?

---

C = ε_r·ε₀·S/e est proportionnelle à ε_r : C est multipliée par 5, puisque S, e et ε₀ ne changent pas.
:::

::: retenir
C = ε·S/e = ε_r·ε₀·S/e pour un condensateur plan ; la tension de service reste nettement sous la tension de claquage.
:::

## 🔋 L'énergie emmagasinée par un condensateur

Un condensateur chargé alimente un petit moteur ou allume une diode quand on le ferme dessus, sans générateur.
Combien d'énergie contient-il, et de quoi dépend-elle ?

::: definition
**Énergie emmagasinée** — Un condensateur est un réservoir d'énergie potentielle électrique (ou électrostatique). Sous la tension u, l'énergie qu'il emmagasine vaut, avec C en F, u en V et E_C en J :

$$ E_C = ½·C·u² = q²/(2C) = ½·q·u $$
:::

Les trois écritures sont équivalentes, car q = C·u : on choisit celle qui utilise les données de l'énoncé. Cette énergie est restituée à la décharge : en chaleur dans les conducteurs, en énergie cinétique dans un moteur, en lumière dans une DEL.

::: exemple Énergie d'un condensateur de 100 µF sous 12 V

1. Avec la tension : E_C = ½ × 100·10⁻⁶ F × (12 V)² = ½ × 100·10⁻⁶ × 144 = 7,2·10⁻³ J.
2. Avec la charge : q = C·u = 100·10⁻⁶ × 12 = 1,2·10⁻³ C, puis ½·q·u = ½ × 1,2·10⁻³ × 12 = 7,2·10⁻³ J ✓.
3. Avec q²/(2C) : (1,2·10⁻³)² / (2 × 100·10⁻⁶) = 1,44·10⁻⁶ / 2,0·10⁻⁴ = 7,2·10⁻³ J ✓.

:::

> ⚠️ Piège classique : « si je double la tension, j'ai deux fois plus d'énergie ». Non : u est au carré, donc doubler u multiplie E_C par **4**. Autre oubli fréquent : le facteur ½.

::: propriete
**Proportionnalités** — À tension fixée, E_C est proportionnelle à C : doubler C double E_C. À capacité fixée, E_C est proportionnelle à u² (et à q²) : doubler u (ou q) multiplie E_C par 4.
:::

::: verifie À toi : une énergie
Quelle énergie emmagasine un condensateur de 470 µF chargé sous 5,0 V ?

---

E_C = ½·C·u² = ½ × 470·10⁻⁶ × 25 = 5,9·10⁻³ J, soit environ 5,9 mJ ; on a bien mis la tension au carré et gardé le facteur ½.
:::

::: retenir
E_C = ½·C·u² = q²/(2C) = ½·q·u : proportionnelle à C, au carré de u ; restituée intégralement à la décharge.
:::

## ⏱️ La charge d'un dipôle RC

On ferme K en position 1 sur un condensateur neutre associé à un résistor. La tension u_C ne saute pas à E : elle évolue progressivement.
Selon quelle loi, et que devient le courant pendant ce temps ?

::: definition
**Dipôle RC et échelon de tension** — Un dipôle RC est un résistor de résistance R associé en série avec un condensateur de capacité C. Quand la tension à ses bornes passe brusquement de 0 à une valeur constante E, on dit qu'il reçoit un **échelon de tension**. La charge du condensateur n'est pas instantanée : c'est un **phénomène transitoire**.
:::

Pour la décrire, on applique la loi des mailles au circuit de charge, avec i = dq/dt = C·du_C/dt et u_R = R·i.

::: exemple Mettre en équation puis résoudre

1. Loi des mailles : u_R + u_C − E = 0, soit R·i + u_C = E.
2. Avec i = C·du_C/dt : **u_C + RC·du_C/dt = E**. On pose τ = RC, d'où du_C/dt + u_C/τ = E/τ (en q : dq/dt + q/τ = E/R).
3. On cherche une solution de la forme u_C(t) = B + A·e^(−αt). À t = 0, u_C = 0 donne B = −A, donc u_C = A(e^(−αt) − 1).
4. On remplace dans l'équation : −A + (1 − ατ)·A·e^(−αt) = E, vraie pour tout t. Donc A = −E et 1 − ατ = 0, soit α = 1/τ.
5. D'où la solution, puis q = C·u_C et i = dq/dt :

$$ u_C(t) = E·(1 − e^(−t/τ))   q(t) = Q₀·(1 − e^(−t/τ))   i(t) = I₀·e^(−t/τ) $$

avec Q₀ = C·E et I₀ = E/R.

:::

Voici la courbe de u_C(t) pour E = 10 V, R = 2,0 kΩ et C = 5,0 µF, donc τ = RC = 2,0·10³ × 5,0·10⁻⁶ = 1,0·10⁻² s = 10 ms.

::: figure La tension u_C part de 0, croît de plus en plus lentement et s'approche de l'asymptote u_C = E = 10 V (τ = 10 ms)
<svg viewBox="0 0 340 230"><title>Courbe de charge u_C(t) croissante vers l'asymptote E = 10 V</title><line x1="52" y1="22" x2="52" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="97.7" y1="22" x2="97.7" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="143.3" y1="22" x2="143.3" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="189" y1="22" x2="189" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="234.7" y1="22" x2="234.7" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="280.3" y1="22" x2="280.3" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="326" y1="22" x2="326" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="52" y1="190" x2="326" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="52" y1="156.4" x2="326" y2="156.4" stroke="#e2e8f0" stroke-width="1"/><line x1="52" y1="122.8" x2="326" y2="122.8" stroke="#e2e8f0" stroke-width="1"/><line x1="52" y1="89.2" x2="326" y2="89.2" stroke="#e2e8f0" stroke-width="1"/><line x1="52" y1="55.6" x2="326" y2="55.6" stroke="#e2e8f0" stroke-width="1"/><line x1="52" y1="22" x2="326" y2="22" stroke="#e2e8f0" stroke-width="1"/><line x1="52" y1="190" x2="332" y2="190" stroke="#0f172a" stroke-width="1.6"/><line x1="52" y1="196" x2="52" y2="16" stroke="#0f172a" stroke-width="1.6"/><polygon points="336,190 328,186 328,194" fill="#0f172a"/><polygon points="52,12 48,20 56,20" fill="#0f172a"/><line x1="52" y1="187" x2="52" y2="193" stroke="#0f172a" stroke-width="1.2"/><text x="52" y="208" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><line x1="97.7" y1="187" x2="97.7" y2="193" stroke="#0f172a" stroke-width="1.2"/><text x="97.7" y="208" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">10</text><line x1="143.3" y1="187" x2="143.3" y2="193" stroke="#0f172a" stroke-width="1.2"/><text x="143.3" y="208" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">20</text><line x1="189" y1="187" x2="189" y2="193" stroke="#0f172a" stroke-width="1.2"/><text x="189" y="208" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">30</text><line x1="234.7" y1="187" x2="234.7" y2="193" stroke="#0f172a" stroke-width="1.2"/><text x="234.7" y="208" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">40</text><line x1="280.3" y1="187" x2="280.3" y2="193" stroke="#0f172a" stroke-width="1.2"/><text x="280.3" y="208" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">50</text><line x1="326" y1="187" x2="326" y2="193" stroke="#0f172a" stroke-width="1.2"/><text x="326" y="208" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">60</text><line x1="49" y1="190" x2="55" y2="190" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="194" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><line x1="49" y1="156.4" x2="55" y2="156.4" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="160.4" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><line x1="49" y1="122.8" x2="55" y2="122.8" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="126.8" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4</text><line x1="49" y1="89.2" x2="55" y2="89.2" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="93.2" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">6</text><line x1="49" y1="55.6" x2="55" y2="55.6" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="59.6" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">8</text><line x1="49" y1="22" x2="55" y2="22" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="26" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">10</text><text x="322" y="224" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">t (ms)</text><text x="60" y="14" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">u_C (V)</text><line x1="52" y1="22" x2="326" y2="22" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="5 4"/><text x="322" y="16" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">E</text><polyline points="52,190 54.3,181.8 56.6,174 58.9,166.6 61.1,159.5 63.4,152.8 65.7,146.5 68,140.4 70.3,134.6 72.5,129.1 74.8,123.9 77.1,118.9 79.4,114.2 81.7,109.7 84,105.4 86.2,101.4 88.5,97.5 90.8,93.8 93.1,90.3 95.4,87 97.7,83.8 100,80.8 102.2,77.9 104.5,75.2 106.8,72.6 109.1,70.1 111.4,67.8 113.7,65.6 115.9,63.4 118.2,61.4 120.5,59.5 122.8,57.7 125.1,55.9 127.3,54.3 129.6,52.7 131.9,51.2 134.2,49.8 136.5,48.4 138.8,47.1 141.1,45.9 143.3,44.7 145.6,43.6 147.9,42.6 150.2,41.6 152.5,40.6 154.8,39.7 157,38.8 159.3,38 161.6,37.2 163.9,36.5 166.2,35.8 168.4,35.1 170.7,34.5 173,33.9 175.3,33.3 177.6,32.7 179.9,32.2 182.2,31.7 184.4,31.2 186.7,30.8 189,30.4 191.3,30 193.6,29.6 195.8,29.2 198.1,28.8 200.4,28.5 202.7,28.2 205,27.9 207.3,27.6 209.6,27.3 211.8,27.1 214.1,26.8 216.4,26.6 218.7,26.4 221,26.2 223.2,26 225.5,25.8 227.8,25.6 230.1,25.4 232.4,25.2 234.7,25.1 236.9,24.9 239.2,24.8 241.5,24.6 243.8,24.5 246.1,24.4 248.4,24.3 250.7,24.2 252.9,24.1 255.2,24 257.5,23.9 259.8,23.8 262.1,23.7 264.4,23.6 266.6,23.5 268.9,23.5 271.2,23.4 273.5,23.3 275.8,23.3 278.1,23.2 280.3,23.1 282.6,23.1 284.9,23 287.2,23 289.5,22.9 291.8,22.9 294,22.8 296.3,22.8 298.6,22.8 300.9,22.7 303.2,22.7 305.4,22.7 307.7,22.6 310,22.6 312.3,22.6 314.6,22.5 316.9,22.5 319.1,22.5 321.4,22.5 323.7,22.4 326,22.4" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"/></svg>
:::

La courbe commence avec une forte pente puis s'aplatit sur l'asymptote d'ordonnée E : le « E » de la formule est cette asymptote.

::: exemple Valeurs à t = 20 ms

1. t/τ = 20 ms / 10 ms = 2 et e^(−2) ≈ 0,135.
2. u_C = E(1 − e^(−2)) = 10 × (1 − 0,135) ≈ 8,6 V.
3. i = I₀·e^(−2) avec I₀ = E/R = 10 / 2,0·10³ = 5,0 mA, donc i ≈ 5,0 × 0,135 ≈ 0,68 mA, positif pendant la charge.
4. Q₀ = C·E = 5,0·10⁻⁶ × 10 = 50 µC est la charge maximale, atteinte quand t tend vers l'infini.

:::

> ⚠️ Piège classique : « le condensateur est déchargé donc i = 0 à t = 0 ». Faux : c'est la **tension** u_C qui vaut 0 à t = 0 (elle ne peut pas sauter). Toute la tension E se retrouve alors aux bornes de R, donc i(0) = E/R = I₀, le maximum. C'est à la **fin** de la charge que i tend vers 0 et que u_C tend vers E.

::: propriete
**Charge d'un dipôle RC** — Au début : u_C = 0 et i = E/R. À la fin : u_C = E, q = C·E et i = 0. Entre les deux, u_C et q croissent exponentiellement tandis que i décroît exponentiellement. Pour visualiser i, on lit u_R = R·i sur une voie de l'oscilloscope (générateur à masse flottante, masse en A : Y1 donne u_DA = R·i ; Y2, avec le bouton INV, donne u_AB = u_C).
:::

::: verifie À toi : une charge numérique
E = 9,0 V, R = 3,0 kΩ, C = 4,0 µF. Donne τ, I₀ et la tension à t = τ.

---

τ = R·C = 3,0·10³ × 4,0·10⁻⁶ = 1,2·10⁻² s = 12 ms ; I₀ = E/R = 9,0 / 3,0·10³ = 3,0 mA ; à t = τ, u_C = E(1 − e^(−1)) = 9,0 × 0,63 ≈ 5,7 V.
:::

::: retenir
Charge : u_C = E(1 − e^(−t/τ)), q = Q₀(1 − e^(−t/τ)), i = I₀·e^(−t/τ) avec τ = RC, Q₀ = CE, I₀ = E/R.
:::

## 🔻 La décharge d'un condensateur dans un résistor

Le condensateur est chargé sous E et on bascule K en position 2 : il se ferme sur R, sans générateur. Comment u_C, q et i évoluent-ils, et dans quel sens circule le courant ?

::: exemple Mettre en équation puis résoudre

1. Loi des mailles : u_C + u_R = 0, soit u_C + R·i = 0. Avec i = C·du_C/dt : **u_C + RC·du_C/dt = 0** : l'équation n'a pas de second membre.
2. Solution de la forme u_C = A·e^(−αt). À t = 0, u_C = E donne A = E.
3. On remplace dans l'équation : (−α + 1/τ)·A·e^(−αt) = 0 pour tout t, donc α = 1/τ.
4. Avec q = C·u_C et i = dq/dt :

$$ u_C(t) = E·e^(−t/τ)   q(t) = Q₀·e^(−t/τ)   i(t) = −I₀·e^(−t/τ) $$

avec Q₀ = C·E et I₀ = E/R.

:::

::: figure Décharge pour E = 10 V et τ = 10 ms : u_C part de E et tend vers 0 ; la tangente à l'origine coupe l'axe des temps en t = τ, où u_C vaut 0,37 E
<svg viewBox="0 0 340 230"><title>Courbe de décharge u_C(t) décroissante depuis E = 10 V, avec sa tangente à l'origine</title><line x1="52" y1="22" x2="52" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="97.7" y1="22" x2="97.7" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="143.3" y1="22" x2="143.3" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="189" y1="22" x2="189" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="234.7" y1="22" x2="234.7" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="280.3" y1="22" x2="280.3" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="326" y1="22" x2="326" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="52" y1="190" x2="326" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="52" y1="156.4" x2="326" y2="156.4" stroke="#e2e8f0" stroke-width="1"/><line x1="52" y1="122.8" x2="326" y2="122.8" stroke="#e2e8f0" stroke-width="1"/><line x1="52" y1="89.2" x2="326" y2="89.2" stroke="#e2e8f0" stroke-width="1"/><line x1="52" y1="55.6" x2="326" y2="55.6" stroke="#e2e8f0" stroke-width="1"/><line x1="52" y1="22" x2="326" y2="22" stroke="#e2e8f0" stroke-width="1"/><line x1="52" y1="190" x2="332" y2="190" stroke="#0f172a" stroke-width="1.6"/><line x1="52" y1="196" x2="52" y2="16" stroke="#0f172a" stroke-width="1.6"/><polygon points="336,190 328,186 328,194" fill="#0f172a"/><polygon points="52,12 48,20 56,20" fill="#0f172a"/><line x1="52" y1="187" x2="52" y2="193" stroke="#0f172a" stroke-width="1.2"/><text x="52" y="208" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><line x1="97.7" y1="187" x2="97.7" y2="193" stroke="#0f172a" stroke-width="1.2"/><text x="97.7" y="208" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">10</text><line x1="143.3" y1="187" x2="143.3" y2="193" stroke="#0f172a" stroke-width="1.2"/><text x="143.3" y="208" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">20</text><line x1="189" y1="187" x2="189" y2="193" stroke="#0f172a" stroke-width="1.2"/><text x="189" y="208" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">30</text><line x1="234.7" y1="187" x2="234.7" y2="193" stroke="#0f172a" stroke-width="1.2"/><text x="234.7" y="208" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">40</text><line x1="280.3" y1="187" x2="280.3" y2="193" stroke="#0f172a" stroke-width="1.2"/><text x="280.3" y="208" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">50</text><line x1="326" y1="187" x2="326" y2="193" stroke="#0f172a" stroke-width="1.2"/><text x="326" y="208" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">60</text><line x1="49" y1="190" x2="55" y2="190" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="194" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><line x1="49" y1="156.4" x2="55" y2="156.4" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="160.4" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><line x1="49" y1="122.8" x2="55" y2="122.8" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="126.8" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4</text><line x1="49" y1="89.2" x2="55" y2="89.2" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="93.2" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">6</text><line x1="49" y1="55.6" x2="55" y2="55.6" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="59.6" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">8</text><line x1="49" y1="22" x2="55" y2="22" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="26" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">10</text><text x="322" y="224" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">t (ms)</text><text x="60" y="14" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">u_C (V)</text><line x1="52" y1="22" x2="97.7" y2="190" stroke="#c2410c" stroke-width="1.8" stroke-dasharray="6 3"/><line x1="97.7" y1="128.2" x2="97.7" y2="190" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="3 3"/><line x1="52" y1="128.2" x2="97.7" y2="128.2" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="3 3"/><polyline points="52,22 54.3,30.2 56.6,38 58.9,45.4 61.1,52.5 63.4,59.2 65.7,65.5 68,71.6 70.3,77.4 72.5,82.9 74.8,88.1 77.1,93.1 79.4,97.8 81.7,102.3 84,106.6 86.2,110.6 88.5,114.5 90.8,118.2 93.1,121.7 95.4,125 97.7,128.2 100,131.2 102.2,134.1 104.5,136.8 106.8,139.4 109.1,141.9 111.4,144.2 113.7,146.4 115.9,148.6 118.2,150.6 120.5,152.5 122.8,154.3 125.1,156.1 127.3,157.7 129.6,159.3 131.9,160.8 134.2,162.2 136.5,163.6 138.8,164.9 141.1,166.1 143.3,167.3 145.6,168.4 147.9,169.4 150.2,170.4 152.5,171.4 154.8,172.3 157,173.2 159.3,174 161.6,174.8 163.9,175.5 166.2,176.2 168.4,176.9 170.7,177.5 173,178.1 175.3,178.7 177.6,179.3 179.9,179.8 182.2,180.3 184.4,180.8 186.7,181.2 189,181.6 191.3,182 193.6,182.4 195.8,182.8 198.1,183.2 200.4,183.5 202.7,183.8 205,184.1 207.3,184.4 209.6,184.7 211.8,184.9 214.1,185.2 216.4,185.4 218.7,185.6 221,185.8 223.2,186 225.5,186.2 227.8,186.4 230.1,186.6 232.4,186.8 234.7,186.9 236.9,187.1 239.2,187.2 241.5,187.4 243.8,187.5 246.1,187.6 248.4,187.7 250.7,187.8 252.9,187.9 255.2,188 257.5,188.1 259.8,188.2 262.1,188.3 264.4,188.4 266.6,188.5 268.9,188.5 271.2,188.6 273.5,188.7 275.8,188.7 278.1,188.8 280.3,188.9 282.6,188.9 284.9,189 287.2,189 289.5,189.1 291.8,189.1 294,189.2 296.3,189.2 298.6,189.2 300.9,189.3 303.2,189.3 305.4,189.3 307.7,189.4 310,189.4 312.3,189.4 314.6,189.5 316.9,189.5 319.1,189.5 321.4,189.5 323.7,189.6 326,189.6" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"/><circle cx="97.7" cy="128.2" r="3.6" fill="#0f6e56" stroke="#0f172a" stroke-width="1"/><text x="107.7" y="120.2" text-anchor="start" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0,37 E</text><text x="101.7" y="182" text-anchor="start" font-size="12" font-weight="700" fill="#c2410c" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">τ</text><text x="82" y="44" text-anchor="start" font-size="12" font-weight="700" fill="#c2410c" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">tangente</text></svg>
:::

La courbe est l'image « retournée » de la charge : u_C part de E et tend vers 0, sans jamais couper l'axe en un temps fini.

::: figure Le courant i part de +I₀ pendant la charge, tend vers 0, puis se retourne à −I₀ à la bascule de K en 2 (I₀ = 5,0 mA, τ = 10 ms)
<svg viewBox="0 0 340 230"><title>Intensité i(t) : positive pendant la charge, négative pendant la décharge</title><line x1="52" y1="22" x2="52" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="97.7" y1="22" x2="97.7" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="143.3" y1="22" x2="143.3" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="189" y1="22" x2="189" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="234.7" y1="22" x2="234.7" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="280.3" y1="22" x2="280.3" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="326" y1="22" x2="326" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="52" y1="176" x2="326" y2="176" stroke="#e2e8f0" stroke-width="1"/><line x1="52" y1="106" x2="326" y2="106" stroke="#e2e8f0" stroke-width="1"/><line x1="52" y1="36" x2="326" y2="36" stroke="#e2e8f0" stroke-width="1"/><line x1="52" y1="106" x2="332" y2="106" stroke="#0f172a" stroke-width="1.6"/><line x1="52" y1="196" x2="52" y2="16" stroke="#0f172a" stroke-width="1.6"/><polygon points="336,106 328,102 328,110" fill="#0f172a"/><polygon points="52,12 48,20 56,20" fill="#0f172a"/><line x1="52" y1="103" x2="52" y2="109" stroke="#0f172a" stroke-width="1.2"/><text x="52" y="122" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><line x1="97.7" y1="103" x2="97.7" y2="109" stroke="#0f172a" stroke-width="1.2"/><text x="97.7" y="122" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">20</text><line x1="143.3" y1="103" x2="143.3" y2="109" stroke="#0f172a" stroke-width="1.2"/><text x="143.3" y="122" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">40</text><line x1="189" y1="103" x2="189" y2="109" stroke="#0f172a" stroke-width="1.2"/><text x="189" y="122" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">60</text><line x1="234.7" y1="103" x2="234.7" y2="109" stroke="#0f172a" stroke-width="1.2"/><text x="234.7" y="122" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">80</text><line x1="280.3" y1="103" x2="280.3" y2="109" stroke="#0f172a" stroke-width="1.2"/><text x="280.3" y="122" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">100</text><line x1="326" y1="103" x2="326" y2="109" stroke="#0f172a" stroke-width="1.2"/><text x="326" y="122" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">120</text><line x1="49" y1="176" x2="55" y2="176" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="180" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−5</text><line x1="49" y1="106" x2="55" y2="106" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="110" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><line x1="49" y1="36" x2="55" y2="36" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="40" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">5</text><text x="322" y="224" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">t (ms)</text><text x="60" y="14" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">i (mA)</text><line x1="189" y1="22" x2="189" y2="190" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="5 4"/><text x="195" y="27.6" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">K en 2</text><text x="86" y="30" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">K en 1</text><polyline points="52,36 53.1,39.4 54.3,42.7 55.4,45.8 56.6,48.7 57.7,51.5 58.9,54.1 60,56.7 61.1,59.1 62.3,61.4 63.4,63.5 64.6,65.6 65.7,67.6 66.8,69.5 68,71.2 69.1,72.9 70.3,74.5 71.4,76.1 72.5,77.5 73.7,78.9 74.8,80.2 76,81.5 77.1,82.7 78.3,83.8 79.4,84.9 80.5,85.9 81.7,86.9 82.8,87.9 84,88.7 85.1,89.6 86.2,90.4 87.4,91.1 88.5,91.9 89.7,92.6 90.8,93.2 92,93.8 93.1,94.4 94.2,95 95.4,95.5 96.5,96 97.7,96.5 98.8,97 100,97.4 101.1,97.8 102.2,98.2 103.4,98.6 104.5,99 105.7,99.3 106.8,99.6 107.9,100 109.1,100.3 110.2,100.5 111.4,100.8 112.5,101.1 113.7,101.3 114.8,101.5 115.9,101.7 117.1,102 118.2,102.1 119.4,102.3 120.5,102.5 121.6,102.7 122.8,102.8 123.9,103 125.1,103.1 126.2,103.3 127.3,103.4 128.5,103.5 129.6,103.7 130.8,103.8 131.9,103.9 133.1,104 134.2,104.1 135.3,104.2 136.5,104.3 137.6,104.4 138.8,104.4 139.9,104.5 141.1,104.6 142.2,104.7 143.3,104.7 144.5,104.8 145.6,104.8 146.8,104.9 147.9,105 149,105 150.2,105.1 151.3,105.1 152.5,105.1 153.6,105.2 154.8,105.2 155.9,105.3 157,105.3 158.2,105.3 159.3,105.4 160.5,105.4 161.6,105.4 162.7,105.5 163.9,105.5 165,105.5 166.2,105.5 167.3,105.6 168.4,105.6 169.6,105.6 170.7,105.6 171.9,105.6 173,105.7 174.2,105.7 175.3,105.7 176.4,105.7 177.6,105.7 178.7,105.7 179.9,105.7 181,105.8 182.2,105.8 183.3,105.8 184.4,105.8 185.6,105.8 186.7,105.8 187.9,105.8 189,105.8" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"/><line x1="189" y1="105.8" x2="189" y2="176" stroke="#0f6e56" stroke-width="1.6" stroke-dasharray="2 3"/><polyline points="189,176 190.1,172.6 191.3,169.3 192.4,166.2 193.6,163.3 194.7,160.5 195.8,157.9 197,155.3 198.1,152.9 199.3,150.6 200.4,148.5 201.6,146.4 202.7,144.4 203.8,142.5 205,140.8 206.1,139.1 207.3,137.5 208.4,135.9 209.6,134.5 210.7,133.1 211.8,131.8 213,130.5 214.1,129.3 215.3,128.2 216.4,127.1 217.5,126.1 218.7,125.1 219.8,124.1 221,123.3 222.1,122.4 223.2,121.6 224.4,120.9 225.5,120.1 226.7,119.4 227.8,118.8 229,118.2 230.1,117.6 231.2,117 232.4,116.5 233.5,116 234.7,115.5 235.8,115 236.9,114.6 238.1,114.2 239.2,113.8 240.4,113.4 241.5,113 242.7,112.7 243.8,112.4 244.9,112 246.1,111.7 247.2,111.5 248.4,111.2 249.5,110.9 250.7,110.7 251.8,110.5 252.9,110.3 254.1,110 255.2,109.9 256.4,109.7 257.5,109.5 258.6,109.3 259.8,109.2 260.9,109 262.1,108.9 263.2,108.7 264.4,108.6 265.5,108.5 266.6,108.3 267.8,108.2 268.9,108.1 270.1,108 271.2,107.9 272.3,107.8 273.5,107.7 274.6,107.6 275.8,107.6 276.9,107.5 278.1,107.4 279.2,107.3 280.3,107.3 281.5,107.2 282.6,107.2 283.8,107.1 284.9,107 286,107 287.2,106.9 288.3,106.9 289.5,106.9 290.6,106.8 291.8,106.8 292.9,106.7 294,106.7 295.2,106.7 296.3,106.6 297.5,106.6 298.6,106.6 299.7,106.5 300.9,106.5 302,106.5 303.2,106.5 304.3,106.4 305.4,106.4 306.6,106.4 307.7,106.4 308.9,106.4 310,106.3 311.2,106.3 312.3,106.3 313.4,106.3 314.6,106.3 315.7,106.3 316.9,106.3 318,106.2 319.1,106.2 320.3,106.2 321.4,106.2 322.6,106.2 323.7,106.2 324.9,106.2 326,106.2" fill="none" stroke="#c2410c" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"/></svg>
:::

Sur le graphe, le saut de +I₀ à −I₀ montre que le courant de décharge circule en sens contraire de celui de charge, ce que traduit le signe moins de i(t).

::: exemple Valeurs à t = τ (E = 10 V, R = 2,0 kΩ, C = 5,0 µF)

1. τ = 10 ms et e^(−1) ≈ 0,37 : u_C(τ) = 10 × 0,37 ≈ 3,7 V.
2. I₀ = E/R = 5,0 mA, donc i(τ) = −5,0 × 0,37 ≈ −1,8 mA : négatif, car le courant va à contre-sens du sens positif de la charge.
3. L'énergie emmagasinée au départ, ½·C·E² = ½ × 5,0·10⁻⁶ × 100 = 2,5·10⁻⁴ J, est dissipée peu à peu par effet Joule dans R.

:::

> ⚠️ Piège classique : écrire i(t) = + I₀·e^(−t/τ) pour la décharge. Le signe + décrirait un courant de même sens que celui de la charge, alors que q diminue : i = dq/dt est négatif.

::: propriete
**Décharge d'un dipôle RC** — u_C = E·e^(−t/τ) décroît de E vers 0 ; q = Q₀·e^(−t/τ) tend vers 0 ; i = −I₀·e^(−t/τ) est négatif et tend vers 0 par valeurs négatives. Toute l'énergie ½·C·E² est finalement dissipée dans le résistor.
:::

::: verifie À toi : une décharge numérique
E = 8,0 V, R = 4,0 kΩ, C = 1,5 µF. Quelles valeurs de u_C et de i à t = 12 ms ?

---

τ = RC = 4,0·10³ × 1,5·10⁻⁶ = 6,0 ms, donc t = 2τ et e^(−2) ≈ 0,135. u_C = 8,0 × 0,135 ≈ 1,1 V ; I₀ = 8,0 / 4,0·10³ = 2,0 mA, donc i = −2,0 × 0,135 ≈ −0,27 mA (négatif : décharge).
:::

::: retenir
Décharge : u_C = E·e^(−t/τ), q = Q₀·e^(−t/τ), i = −I₀·e^(−t/τ) : le courant est négatif et toute l'énergie finit en chaleur dans R.
:::

## 🎯 La constante de temps τ = RC

Avec C fixé, une résistance plus grande ralentit la charge ; avec R fixé, une capacité plus grande aussi.
Comment résumer en un seul nombre la rapidité d'un dipôle RC, et comment le lire sur une courbe ?

::: definition
**Constante de temps** — **τ = R·C**. Elle a la dimension d'un temps : avec R en ohms et C en farads, τ s'exprime en secondes. C'est la grandeur qui renseigne sur la rapidité de la charge et de la décharge : plus τ est petite, plus elles sont rapides.
:::

Pour C = 10 µF, la durée d'une charge presque complète est proportionnelle à R, donc à τ :

| R | 1,0 kΩ | 2,0 kΩ | 4,0 kΩ |
| --- | --- | --- | --- |
| τ = RC | 10 ms | 20 ms | 40 ms |
| durée de charge à 99 % (≈ 4,6 τ) | 46 ms | 92 ms | 184 ms |

::: figure Deux lectures de τ sur la courbe de charge (E = 10 V, τ = 10 ms) : la tangente à l'origine coupe l'asymptote u_C = E en t = τ, et la courbe passe par 0,63 E à t = τ
<svg viewBox="0 0 340 230"><title>Courbe de charge avec sa tangente à l'origine et le point d'ordonnée 0,63 E</title><line x1="52" y1="22" x2="52" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="97.7" y1="22" x2="97.7" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="143.3" y1="22" x2="143.3" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="189" y1="22" x2="189" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="234.7" y1="22" x2="234.7" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="280.3" y1="22" x2="280.3" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="326" y1="22" x2="326" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="52" y1="190" x2="326" y2="190" stroke="#e2e8f0" stroke-width="1"/><line x1="52" y1="156.4" x2="326" y2="156.4" stroke="#e2e8f0" stroke-width="1"/><line x1="52" y1="122.8" x2="326" y2="122.8" stroke="#e2e8f0" stroke-width="1"/><line x1="52" y1="89.2" x2="326" y2="89.2" stroke="#e2e8f0" stroke-width="1"/><line x1="52" y1="55.6" x2="326" y2="55.6" stroke="#e2e8f0" stroke-width="1"/><line x1="52" y1="22" x2="326" y2="22" stroke="#e2e8f0" stroke-width="1"/><line x1="52" y1="190" x2="332" y2="190" stroke="#0f172a" stroke-width="1.6"/><line x1="52" y1="196" x2="52" y2="16" stroke="#0f172a" stroke-width="1.6"/><polygon points="336,190 328,186 328,194" fill="#0f172a"/><polygon points="52,12 48,20 56,20" fill="#0f172a"/><line x1="52" y1="187" x2="52" y2="193" stroke="#0f172a" stroke-width="1.2"/><text x="52" y="208" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><line x1="97.7" y1="187" x2="97.7" y2="193" stroke="#0f172a" stroke-width="1.2"/><text x="97.7" y="208" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">10</text><line x1="143.3" y1="187" x2="143.3" y2="193" stroke="#0f172a" stroke-width="1.2"/><text x="143.3" y="208" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">20</text><line x1="189" y1="187" x2="189" y2="193" stroke="#0f172a" stroke-width="1.2"/><text x="189" y="208" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">30</text><line x1="234.7" y1="187" x2="234.7" y2="193" stroke="#0f172a" stroke-width="1.2"/><text x="234.7" y="208" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">40</text><line x1="280.3" y1="187" x2="280.3" y2="193" stroke="#0f172a" stroke-width="1.2"/><text x="280.3" y="208" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">50</text><line x1="326" y1="187" x2="326" y2="193" stroke="#0f172a" stroke-width="1.2"/><text x="326" y="208" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">60</text><line x1="49" y1="190" x2="55" y2="190" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="194" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><line x1="49" y1="156.4" x2="55" y2="156.4" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="160.4" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><line x1="49" y1="122.8" x2="55" y2="122.8" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="126.8" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4</text><line x1="49" y1="89.2" x2="55" y2="89.2" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="93.2" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">6</text><line x1="49" y1="55.6" x2="55" y2="55.6" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="59.6" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">8</text><line x1="49" y1="22" x2="55" y2="22" stroke="#0f172a" stroke-width="1.2"/><text x="45" y="26" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">10</text><text x="322" y="224" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">t (ms)</text><text x="60" y="14" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">u_C (V)</text><line x1="52" y1="22" x2="326" y2="22" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="5 4"/><text x="322" y="16" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">E</text><line x1="52" y1="190" x2="97.7" y2="22" stroke="#c2410c" stroke-width="1.8" stroke-dasharray="6 3"/><line x1="97.7" y1="22" x2="97.7" y2="190" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="3 3"/><line x1="52" y1="83.8" x2="97.7" y2="83.8" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="3 3"/><polyline points="52,190 54.3,181.8 56.6,174 58.9,166.6 61.1,159.5 63.4,152.8 65.7,146.5 68,140.4 70.3,134.6 72.5,129.1 74.8,123.9 77.1,118.9 79.4,114.2 81.7,109.7 84,105.4 86.2,101.4 88.5,97.5 90.8,93.8 93.1,90.3 95.4,87 97.7,83.8 100,80.8 102.2,77.9 104.5,75.2 106.8,72.6 109.1,70.1 111.4,67.8 113.7,65.6 115.9,63.4 118.2,61.4 120.5,59.5 122.8,57.7 125.1,55.9 127.3,54.3 129.6,52.7 131.9,51.2 134.2,49.8 136.5,48.4 138.8,47.1 141.1,45.9 143.3,44.7 145.6,43.6 147.9,42.6 150.2,41.6 152.5,40.6 154.8,39.7 157,38.8 159.3,38 161.6,37.2 163.9,36.5 166.2,35.8 168.4,35.1 170.7,34.5 173,33.9 175.3,33.3 177.6,32.7 179.9,32.2 182.2,31.7 184.4,31.2 186.7,30.8 189,30.4 191.3,30 193.6,29.6 195.8,29.2 198.1,28.8 200.4,28.5 202.7,28.2 205,27.9 207.3,27.6 209.6,27.3 211.8,27.1 214.1,26.8 216.4,26.6 218.7,26.4 221,26.2 223.2,26 225.5,25.8 227.8,25.6 230.1,25.4 232.4,25.2 234.7,25.1 236.9,24.9 239.2,24.8 241.5,24.6 243.8,24.5 246.1,24.4 248.4,24.3 250.7,24.2 252.9,24.1 255.2,24 257.5,23.9 259.8,23.8 262.1,23.7 264.4,23.6 266.6,23.5 268.9,23.5 271.2,23.4 273.5,23.3 275.8,23.3 278.1,23.2 280.3,23.1 282.6,23.1 284.9,23 287.2,23 289.5,22.9 291.8,22.9 294,22.8 296.3,22.8 298.6,22.8 300.9,22.7 303.2,22.7 305.4,22.7 307.7,22.6 310,22.6 312.3,22.6 314.6,22.5 316.9,22.5 319.1,22.5 321.4,22.5 323.7,22.4 326,22.4" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"/><circle cx="97.7" cy="83.8" r="3.6" fill="#0f6e56" stroke="#0f172a" stroke-width="1"/><text x="137.7" y="99.8" text-anchor="middle" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0,63 E</text><text x="93.7" y="182" text-anchor="end" font-size="12" font-weight="700" fill="#c2410c" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">τ</text><text x="109.7" y="38" text-anchor="start" font-size="12" font-weight="700" fill="#c2410c" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">tangente</text></svg>
:::

Sur la figure, la tangente à l'origine (pointillés orange) rejoint l'asymptote d'ordonnée E à l'abscisse τ, et la verticale de cette abscisse coupe la courbe à l'ordonnée 0,63 E.

::: exemple Trouver τ de trois façons

1. **Par calcul** : τ = R·C, par exemple 2,0 kΩ × 5,0 µF = 10 ms.
2. **Par la tangente à l'origine** : u_C = a·t avec a = (du_C/dt) à t = 0 = E/τ ; cette droite atteint u_C = E quand E·t/τ = E, donc en t = τ. Pour la décharge, elle coupe l'axe des temps en t = τ ; pour i(t), la tangente à l'origine coupe l'axe des temps en t = τ.
3. **Par la lecture de 0,63 E** (charge) : pour t = τ, u_C = E(1 − e^(−1)) ≈ 0,63 E. En décharge, u_C(τ) = E·e^(−1) ≈ 0,37 E.
4. **Durée « complète »** : u_C ≥ 0,99 E équivaut à e^(−t/τ) ≤ 0,01, soit t ≥ τ·Log 100 = 2·τ·Log 10 ≈ 4,6 τ (Log désigne le logarithme népérien, comme dans le manuel), donc t ≃ 5 τ. À 1 ‰ près, t ≥ τ·Log 1000 ≈ 6,9 τ ≃ 7 τ.

:::

> ⚠️ Piège classique : prendre τ pour la durée totale de la charge. À t = τ, la charge n'est faite qu'à **63 %** ; il faut environ 5 τ pour la terminer à 1 % près.

::: propriete
**Récapitulation** — Pour une charge, u_C vaut 0, 0,63 E, 0,99 E, 0,999 E aux instants 0, τ, 4,6 τ, 6,9 τ ; pour une décharge, E, 0,37 E, 0,01 E, 0,001 E aux mêmes instants. Cas limite : t = 0 donne le début, et u_C n'atteint E (ou 0) qu'au bout d'une durée infinie.
:::

::: verifie À toi : lire τ
Sur une courbe de charge d'asymptote E = 6,0 V, on lit que u_C = 3,8 V à t = 8 ms. Que vaut τ, et quelle est la résistance si C = 2,0 µF ?

---

3,8 V ≈ 0,63 × 6,0 V : c'est l'ordonnée 0,63 E, donc l'abscisse lue est τ = 8 ms. Alors R = τ/C = 8·10⁻³ / 2,0·10⁻⁶ = 4,0·10³ Ω = 4,0 kΩ.
:::

::: retenir
τ = RC en secondes : 63 % de E à t = τ (en charge), 37 % de E (en décharge), tangente à l'origine qui coupe l'asymptote en τ, et charge terminée vers 5 τ.
:::

> 🏆 Tu sais désormais lire le temps dans une courbe : un nombre, τ, résume toute la dynamique d'un dipôle RC.
