# 🧲 La bobine et le dipôle RL — le courant qui se fait attendre

> 💡 «Un résistor laisse passer le courant ; une bobine, elle, discute chaque variation. Tout le chapitre est ce bras de fer.»

Approche un aimant d'une bobine fermée : un courant naît sans pile ni générateur. Place la même bobine dans un circuit et ferme l'interrupteur : le courant arrive en retard. Huit notions expliquent ces deux surprises : l'induction et la loi de Lenz, l'auto-induction, la tension aux bornes d'une bobine, l'énergie magnétique, l'établissement puis la rupture du courant dans un dipôle RL, la constante de temps τ et les applications.

## 🧲 L'induction électromagnétique et la loi de Lenz

Une bobine est fermée sur un résistor, sans pile ni générateur. On approche d'une de ses faces le pôle nord d'un barreau aimanté : un oscilloscope branché aux bornes du résistor enregistre une impulsion de tension, puis plus rien dès que l'aimant s'arrête. On éloigne l'aimant : l'impulsion change de signe.
Pourquoi ce courant apparaît-il, et pourquoi change-t-il de sens ?

::: definition
**Induction électromagnétique** — Toute variation du champ magnétique au voisinage d'un circuit fermé fait naître dans ce circuit un courant, appelé **courant induit**. La cause de la variation est l'**inducteur** (un aimant qu'on déplace, ou un circuit voisin parcouru par un courant variable) ; le circuit où naît le courant est l'**induit**. Le courant induit est d'autant plus intense que la variation est rapide.
:::

::: definition
**Loi de Lenz** — Le courant induit a un sens tel qu'il s'oppose, par ses effets, à la cause qui lui donne naissance.
:::

::: figure Le pôle nord s'approche : B, le champ de l'aimant, augmente dans la bobine ; le champ induit b lui est opposé et la bobine présente sa face nord à l'aimant
<svg viewBox="0 0 340 180"><title>Aimant dont le pôle nord s'approche d'une bobine : champ inducteur B, champ induit b, faces nord et sud de la bobine</title><rect x="20" y="75" width="50" height="40" fill="#bfdbfe" stroke="#0f172a" stroke-width="2"/><rect x="70" y="75" width="50" height="40" fill="#fecaca" stroke="#0f172a" stroke-width="2"/><text x="45" y="101" text-anchor="middle" font-size="15" font-weight="700" fill="#1d4ed8" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">S</text><text x="95" y="101" text-anchor="middle" font-size="15" font-weight="700" fill="#b91c1c" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">N</text><line x1="30" y1="56" x2="88.8" y2="56" stroke="#0f172a" stroke-width="2.4" stroke-linecap="round"/><polygon points="96,56 88,60 88,52" fill="#0f172a"/><text x="63" y="47" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">v</text><ellipse cx="212" cy="95" rx="6" ry="34" fill="none" stroke="#0f172a" stroke-width="2"/><ellipse cx="228" cy="95" rx="6" ry="34" fill="none" stroke="#0f172a" stroke-width="2"/><ellipse cx="244" cy="95" rx="6" ry="34" fill="none" stroke="#0f172a" stroke-width="2"/><ellipse cx="260" cy="95" rx="6" ry="34" fill="none" stroke="#0f172a" stroke-width="2"/><ellipse cx="276" cy="95" rx="6" ry="34" fill="none" stroke="#0f172a" stroke-width="2"/><line x1="128" y1="95" x2="188.8" y2="95" stroke="#0f172a" stroke-width="2.6" stroke-linecap="round"/><polygon points="196,95 188,99 188,91" fill="#0f172a"/><text x="160" y="84" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">B</text><line x1="272" y1="122" x2="223.2" y2="122" stroke="#0f6e56" stroke-width="2.8" stroke-linecap="round"/><polygon points="216,122 224,118 224,126" fill="#0f6e56"/><text x="246" y="141" text-anchor="middle" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">b</text><text x="204" y="164" text-anchor="middle" font-size="14" font-weight="700" fill="#b91c1c" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">N</text><text x="284" y="164" text-anchor="middle" font-size="14" font-weight="700" fill="#1d4ed8" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">S</text><line x1="205" y1="141" x2="205" y2="148" stroke="#94a3b8" stroke-width="1.2" stroke-linecap="round"/><line x1="284" y1="141" x2="284" y2="148" stroke="#94a3b8" stroke-width="1.2" stroke-linecap="round"/></svg>
:::

Sur la figure, B et b sont les champs notés B⃗ et b⃗ dans le raisonnement : B est le champ de l'aimant (inducteur), b celui du courant induit, et les lettres N et S sous la bobine nomment ses deux faces.

::: exemple Un pôle nord qu'on approche

1. Le pôle nord arrive en face de la bobine. Le champ B⃗ de l'aimant pénètre dans la bobine en allant vers la droite, et sa valeur ‖B⃗‖ augmente, puisque l'aimant se rapproche.
2. La loi de Lenz demande que le courant induit s'oppose à cette augmentation : son champ b⃗ est de sens contraire à B⃗, donc dirigé vers la gauche à l'intérieur de la bobine.
3. Un champ qui sort par la face de gauche caractérise une face nord : la bobine présente sa face nord au pôle nord de l'aimant. Deux faces de même nom se repoussent, ce qui freine l'approche : le courant induit « s'oppose bien à la cause ».
4. Le sens du courant dans les spires se déduit de celui de b⃗ par la règle du bonhomme d'Ampère.

:::

::: piege
**Erreur : croire qu'un aimant collé à la bobine y entretient un courant.** « L'aimant est tout près, le champ est fort, donc le courant induit est fort. » L'erreur tente parce que la proximité donne un champ intense et qu'on attend un effet intense. Or seule la **variation** de ‖B⃗‖ compte : aimant immobile, même collé à la bobine, ‖B⃗‖ est constant et aucun courant n'apparaît : dans l'exemple, le courant n'existe que pendant l'approche.
:::

::: propriete
**Ce qui reste vrai à chaque fois** — Si ‖B⃗‖ augmente, b⃗ est opposé à B⃗ (répulsion bobine-aimant) ; si ‖B⃗‖ diminue, b⃗ a le même sens que B⃗ (attraction). Inverser le pôle présenté, ou le sens du déplacement, inverse le sens du courant induit, donc le signe de la tension aux bornes du résistor ; un déplacement plus rapide donne une impulsion plus grande. Le courant induit est dû à une **f.e.m. d'induction**, répartie dans tout le circuit induit : elle naît et cesse avec la cause, et si le circuit induit est ouvert elle se manifeste par une tension à ses bornes. Cas limite : le courant inducteur d'un circuit voisin est continu et constant, donc le champ ne varie pas et rien n'est induit.
:::

::: verifie À toi : le pôle nord qu'on éloigne
On éloigne le pôle nord de la face de gauche d'une bobine fermée. Quel champ la bobine crée-t-elle par rapport à B⃗, quelle face présente-t-elle à l'aimant, et la force entre eux est-elle attractive ou répulsive ?

---

Le champ B⃗ de l'aimant va toujours vers la droite dans la bobine, mais sa valeur ‖B⃗‖ diminue. La bobine doit s'opposer à cette diminution : b⃗ a le même sens que B⃗, donc il sort par la face de droite (face nord), et la face de gauche, en regard de l'aimant, est une face sud. Face sud contre pôle nord : attraction, qui retient l'aimant qu'on éloigne.
:::

::: retenir
Toute variation du champ magnétique près d'un circuit fermé y induit un courant, d'autant plus intense que la variation est rapide, et son sens est tel que ses effets s'opposent à la cause (loi de Lenz).
:::

## 🔁 L'auto-induction et la f.e.m. e = −L di/dt

On fait traverser une bobine longue, en série avec un résistor, par un courant triangulaire délivré par un générateur basses fréquences : i monte régulièrement, puis redescend régulièrement. À l'oscilloscope, la tension de la bobine n'est pas triangulaire : c'est un créneau, constant pendant la montée et de signe contraire pendant la descente.
Quelle grandeur de la bobine suit la pente de i(t) plutôt que i lui-même ?

::: definition
**Auto-induction** — Quand le courant qui traverse une bobine varie, son propre champ varie : la bobine est à la fois inducteur et induit, et elle devient le siège d'une f.e.m. d'auto-induction e = −L di/dt. La constante L est l'**inductance** de la bobine, exprimée en henry (H).
:::

::: figure Le courant triangulaire (en haut) a des pentes opposées et égales ; la f.e.m. e(t) (en bas) est un créneau : négative quand i croît, positive quand i décroît
<svg viewBox="0 0 340 240"><title>Courant i(t) triangulaire (0 à 60 mA en 5 ms, retour à 0 en 5 ms) et force électromotrice e(t) en créneaux de −0,30 V puis +0,30 V</title><line x1="50" y1="100" x2="322" y2="100" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><polygon points="326,100 318,104 318,96" fill="#0f172a"/><line x1="50" y1="100" x2="50" y2="18" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><polygon points="50,14 54,22 46,22" fill="#0f172a"/><line x1="50" y1="190" x2="322" y2="190" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><polygon points="326,190 318,194 318,186" fill="#0f172a"/><line x1="50" y1="190" x2="50" y2="142" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><polygon points="50,138 54,146 46,146" fill="#0f172a"/><polyline points="50,100 175,30 300,100" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><line x1="175" y1="30" x2="175" y2="232" stroke="#94a3b8" stroke-width="1.2" stroke-linecap="round" stroke-dasharray="3 3"/><line x1="300" y1="100" x2="300" y2="232" stroke="#94a3b8" stroke-width="1.2" stroke-linecap="round" stroke-dasharray="3 3"/><line x1="50" y1="30" x2="175" y2="30" stroke="#94a3b8" stroke-width="1.2" stroke-linecap="round" stroke-dasharray="3 3"/><polyline points="50,230 175,230 175,150 300,150 300,230 325,230" fill="none" stroke="#b45309" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><text x="58" y="22" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">i (mA)</text><text x="44" y="34" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">60</text><text x="175" y="116" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">5</text><text x="300" y="116" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">10</text><text x="322" y="90" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">t (ms)</text><text x="58" y="146" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">e (V)</text><text x="44" y="154" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">+0,30</text><text x="44" y="234" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−0,30</text><text x="322" y="180" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">t (ms)</text></svg>
:::

Chaque palier de e(t) correspond à une pente de i(t) : la montée donne le palier négatif, la descente le palier positif, ce qui explique le signe − de la formule.

::: exemple Lire e(t) sur le courant de la figure, avec L = 25 mH

1. Montée : i passe de 0 à 60 mA en 5 ms, donc di/dt = 0,060 A / 0,005 s = 12 A/s, la pente de i(t) (on convertit les mA et les ms avant de diviser).
2. e = −L di/dt = −0,025 × 12 = −0,30 V : négative, car i croît et la f.e.m. s'oppose à cette croissance.
3. Descente : la pente vaut −12 A/s, donc e = −0,025 × (−12) = +0,30 V : positive, car i décroît et la f.e.m. s'oppose à cette décroissance.
4. Contrôle : les pentes sont opposées et égales, donc les deux paliers de e(t) sont opposés et de même valeur absolue ✓.

:::

::: piege
**Erreur : croire qu'une bobine s'oppose au courant lui-même, comme un résistor.** « Le courant est grand (1,5 A), donc la bobine le freine beaucoup. » L'erreur tente parce que, pour un résistor, la tension U = R I suit la valeur de I. Pour la bobine, e = −L di/dt : avec un courant constant de 1,5 A, di/dt = 0 donc e = 0, et la bobine ne s'oppose à rien (hors sa résistance r). Elle s'oppose aux **variations** de i : elle retarde le courant, elle ne le bloque pas.
:::

::: propriete
**Signe de e, facteurs de L** — Si i croît, e < 0 ; si i décroît, e > 0 : e s'oppose toujours à la variation de i. La même variation de i, faite deux fois plus vite, double |e| puisque di/dt double. Sans noyau de fer, L ne dépend que de la géométrie : elle augmente avec le nombre N de spires et avec la section, diminue quand la longueur ℓ augmente, et ne dépend ni de i ni de la tension. Un noyau de fer doux fait augmenter L, mais e = −L di/dt cesse alors d'être valable. Une bobine d'inductance L non nulle est dite **inductive**, **purement inductive** si de plus sa résistance est nulle. Ordre de grandeur : un solénoïde de 150 spires, 15 cm de long, 3 cm de diamètre a L = 140 μH.
:::

::: verifie À toi : une f.e.m. à calculer
Dans une bobine d'inductance L = 0,80 H, le courant passe régulièrement de 0,10 A à 0,50 A en 20 ms. Calculer e.

---

On a di/dt = (0,50 − 0,10) / 0,020 = 20 A/s, puis e = −L di/dt = −0,80 × 20 = −16 V. Le résultat est négatif parce que i croît : la f.e.m. s'oppose à l'augmentation du courant, comme sur la montée de la figure.
:::

::: retenir
Une bobine d'inductance L parcourue par un courant variable est le siège d'une f.e.m. d'auto-induction e = −L di/dt, de signe opposé à la variation de i ; sans noyau, L ne dépend que de la géométrie.
:::

## 📏 La tension aux bornes d'une bobine

Une bobine réelle est un long fil enroulé : elle a donc une résistance r, en plus de son inductance L. On branche un voltmètre à ses bornes.
Que lit-on quand le courant varie, que lit-on quand il est constant, et le résultat dépend-il du sens dans lequel on compte le courant ?

::: definition
**Tension aux bornes d'une bobine (L, r)** — Une bobine se modélise par une f.e.m. e en série avec la résistance r. Quand i va de A vers B, la tension fléchée à l'opposé du courant (convention récepteur) vaut u_AB = L di/dt + r i, car u_AB = −e + r i et e = −L di/dt.
:::

::: figure Le modèle de la bobine : la f.e.m. e, orientée dans le sens de i, est en série avec r ; la tension u_AB est fléchée à l'opposé de i
<svg viewBox="0 0 340 180"><title>Modèle d'une bobine : une f.e.m. e orientée comme le courant i, en série avec la résistance r ; la tension u_AB est fléchée à l'opposé de i</title><line x1="40" y1="70" x2="82" y2="70" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><circle cx="100" cy="70" r="18" fill="#ffffff" stroke="#0f172a" stroke-width="2"/><line x1="118" y1="70" x2="150" y2="70" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><circle cx="150" cy="70" r="3.5" fill="#0f172a"/><line x1="150" y1="70" x2="172" y2="70" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><rect x="172" y="58" width="56" height="24" fill="#ffffff" stroke="#0f172a" stroke-width="2"/><line x1="228" y1="70" x2="262" y2="70" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><circle cx="40" cy="70" r="3.8" fill="#0f172a"/><circle cx="262" cy="70" r="3.8" fill="#0f172a"/><text x="40" y="92" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">A</text><text x="150" y="92" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">C</text><text x="262" y="92" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">B</text><text x="200" y="75" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">r</text><text x="81" y="56" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−</text><text x="119" y="56" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">+</text><line x1="60" y1="36" x2="120.8" y2="36" stroke="#0f6e56" stroke-width="2.4" stroke-linecap="round"/><polygon points="128,36 120,40 120,32" fill="#0f6e56"/><text x="94" y="28" text-anchor="middle" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">i</text><line x1="88" y1="106" x2="104.8" y2="106" stroke="#b91c1c" stroke-width="2.2" stroke-linecap="round"/><polygon points="112,106 104,110 104,102" fill="#b91c1c"/><text x="100" y="122" text-anchor="middle" font-size="12" font-weight="700" fill="#b91c1c" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">e</text><line x1="258" y1="148" x2="51.2" y2="148" stroke="#b45309" stroke-width="2.2" stroke-linecap="round"/><polygon points="44,148 52,144 52,152" fill="#b45309"/><text x="151" y="168" text-anchor="middle" font-size="12" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">u_AB</text></svg>
:::

Entre A et C, la flèche de e est dans le sens de i, donc u_AC = −e ; entre C et B, la loi d'Ohm donne u_CB = r i : la somme est u_AB = −e + r i.

::: exemple Bobine L = 60 mH, r = 15 Ω, courant i(t) = 2,0 t (i en A, t en s) de A vers B

1. On dérive : di/dt = 2,0 A/s, donc le terme inductif vaut L di/dt = 0,060 × 2,0 = 0,12 V.
2. À t = 0,10 s, i = 0,20 A et le terme résistif vaut r i = 15 × 0,20 = 3,0 V, par la loi d'Ohm appliquée au fil.
3. u_AB = 0,12 + 3,0 = 3,12 V.
4. Même bobine, courant constant de 0,30 A : di/dt = 0, donc u_AB = r i = 4,5 V. En régime permanent la bobine se comporte comme un simple résistor de résistance r, et u_AB = 0 si r = 0.

:::

::: piege
**Erreur : appliquer u_AB = L di/dt + r i quand le courant circule de B vers A.** Soit L = 0,30 H, r = 10 Ω et un courant de B vers A, de 0,20 A, qui croît de 5,0 A/s. Le calcul 0,30 × 5,0 + 10 × 0,20 = 3,5 V est juste, mais c'est la valeur de u_BA, la tension fléchée à l'opposé du courant : u_AB = −3,5 V. L'erreur tente parce qu'on retient la formule avec « u_AB » écrit dedans et qu'on oublie la condition sur le sens de i.
:::

::: propriete
**Trois cas à reconnaître** — Courant constant : u = r i (et 0 si r = 0). Résistance négligeable : u = L di/dt. Courant coupé très brusquement : di/dt est énorme, le terme L di/dt écrase r i et la tension devient très grande. Quand i(t) est un polynôme, on dérive terme à terme (la dérivée de a t² est 2 a t). La formule vaut pour la tension fléchée à l'opposé du courant : courant de A vers B, tension u_AB ; courant de B vers A, tension u_BA, d'où u_AB = −(L di/dt + r i).
:::

::: verifie À toi : u(t) avec un courant qui monte
Une bobine d'inductance 80 mH et de résistance 20 Ω est parcourue de A vers B par un courant i(t) = 3,0 t (i en A, t en s). Calculer u_AB à t = 0,10 s.

---

On a di/dt = 3,0 A/s, donc L di/dt = 0,080 × 3,0 = 0,24 V. À t = 0,10 s, i = 0,30 A et r i = 20 × 0,30 = 6,0 V. Le courant va de A vers B, donc u_AB = 0,24 + 6,0 = 6,24 V, les deux termes s'ajoutant.
:::

::: retenir
Une bobine (L, r) traversée par i de A vers B présente la tension u_AB = L di/dt + r i ; à courant constant il ne reste que r i.
:::

## 🔋 L'énergie magnétique et l'étincelle de rupture

À la rupture du courant dans une bobine, une étincelle jaillit entre les contacts de l'interrupteur : c'est le principe de l'allumeur d'une cuisinière à gaz ou du soudage à l'arc. La puissance que reçoit la bobine s'écrit p = u_AB × i = r i² + L i di/dt. Le premier terme est la chaleur dégagée par effet Joule.
Où va le second terme, et d'où vient l'étincelle ?

::: definition
**Énergie magnétique** — Le terme L i di/dt est la puissance magnétique p_L : c'est la dérivée de ½ L i², et il sert à emmagasiner dans la bobine l'énergie magnétique E_L = ½ L i², en joule (J) avec L en henry et i en ampère. La bobine est un réservoir **temporaire** : elle stocke de l'énergie tant qu'un courant la traverse et la restitue quand i diminue.
:::

::: exemple Une bobine L = 2,0 H parcourue par I = 0,30 A, dont on coupe le courant en Δt = 1,5 ms

1. Énergie stockée : E_L = ½ × 2,0 × (0,30)² = 0,5 × 2,0 × 0,090 = 0,090 J = 90 mJ.
2. Coupure brusque : le courant tombe de 0,30 A à 0 en 1,5 ms, donc |e| ≈ L Δi/Δt = 2,0 × 0,30 / 0,0015 = 400 V.
3. Quatre cents volts apparaissent alors que le circuit n'est alimenté que par quelques volts : l'air entre les contacts s'ionise et laisse jaillir l'étincelle. Les 90 mJ sont restitués en à peu près une milliseconde.
4. Une diode branchée aux bornes de l'ensemble bobine-résistor, dans le sens qui la bloque tant que le générateur alimente le circuit, laisse passer le courant de la bobine après l'ouverture : il décroît alors sans coupure brutale, et l'interrupteur est protégé.

:::

::: piege
**Erreur : « en régime permanent, e = 0, donc la bobine ne contient plus d'énergie ».** L'erreur tente parce qu'on confond ce qui **varie** (di/dt, qui règle e) et ce qui est **stocké** (i, qui règle E_L). Avec I = 0,30 A et L = 2,0 H, les 90 mJ de l'étape 1 restent stockés tant que le courant circule, même constant.
:::

::: propriete
**Ce qu'il faut savoir manier** — E_L croît comme i² : doubler i multiplie E_L par 4. E_L est nulle si i = 0, ne dépend pas du sens du courant, et une variation d'énergie se calcule par ½ L i₂² − ½ L i₁², jamais par ½ L (i₂ − i₁)². La bobine est un réservoir temporaire (l'énergie disparaît avec le courant), alors qu'un condensateur chargé et isolé garde la sienne : c'est un réservoir permanent. Un courant coupé en un temps très court Δt donne |e| ≈ L Δi/Δt, d'autant plus grande que Δt est petit.
:::

::: verifie À toi : énergie puis surtension
Une bobine d'inductance 0,50 H est parcourue par un courant de 0,20 A, que l'on coupe en 2,0 ms. Calculer E_L, puis la valeur absolue approchée de la f.e.m. d'auto-induction.

---

E_L = ½ × 0,50 × (0,20)² = 0,5 × 0,50 × 0,040 = 0,010 J = 10 mJ. Le courant varie de 0,20 A en 2,0 ms, donc |e| ≈ L Δi/Δt = 0,50 × 0,20 / 0,0020 = 50 V : une coupure brusque donne une tension bien supérieure à celle du générateur.
:::

::: retenir
Une bobine parcourue par i emmagasine l'énergie E_L = ½ L i², réservoir temporaire que la rupture du courant restitue sous forme d'une grande f.e.m. |e| ≈ L Δi/Δt.
:::

## 📈 L'établissement du courant dans un dipôle RL

On ferme K sur un circuit en série : générateur de f.e.m. E = 6,0 V, bobine (L = 0,10 H, r = 10 Ω) et résistor R₀ = 40 Ω. Un résistor seul porterait le courant à sa valeur finale d'un coup. Ici, la tension u_BM aux bornes de R₀, image de l'intensité, monte progressivement sur l'oscilloscope.
Quelle loi donne i(t), et vers quelle valeur le courant tend-il ?

::: definition
**Dipôle RL, échelon de tension** — Un dipôle RL associe en série une bobine (L, r) et un résistor R₀ : sa résistance totale est R = R₀ + r. Soumis à un échelon de tension (on passe de 0 à E à t = 0), il est parcouru par un courant qui traverse un **régime transitoire** avant d'atteindre le **régime permanent**, de valeur I₀ = E/R, où la bobine se comporte comme un résistor de résistance r.
:::

::: figure Le dipôle RL : la bobine (L, r) entre A et B, le résistor R₀ entre B et M ; la diode D relie M à A et reste bloquée tant que K est fermé
<svg viewBox="0 0 340 190"><title>Circuit série : générateur E, interrupteur K, bobine (L, r) entre A et B, résistor R₀ entre B et M, diode D reliant M à A</title><line x1="50" y1="45" x2="95" y2="45" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><line x1="130" y1="45" x2="165" y2="45" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><line x1="165" y1="45" x2="185" y2="45" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><line x1="95" y1="45" x2="125" y2="29" stroke="#0f172a" stroke-width="2" stroke-linecap="round"/><circle cx="95" cy="45" r="3.5" fill="#0f172a"/><circle cx="130" cy="45" r="3.5" fill="#0f172a"/><path d="M185 45 a7.5 10 0 0 1 15 0 a7.5 10 0 0 1 15 0 a7.5 10 0 0 1 15 0 a7.5 10 0 0 1 15 0" fill="none" stroke="#0f172a" stroke-width="2"/><line x1="245" y1="45" x2="268" y2="45" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><circle cx="268" cy="45" r="3.5" fill="#0f172a"/><line x1="268" y1="45" x2="268" y2="82" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><rect x="260" y="82" width="16" height="40" fill="#ffffff" stroke="#0f172a" stroke-width="2"/><line x1="268" y1="122" x2="268" y2="160" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><line x1="268" y1="160" x2="50" y2="160" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><line x1="50" y1="45" x2="50" y2="84" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><line x1="50" y1="116" x2="50" y2="160" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><circle cx="50" cy="100" r="16" fill="#ffffff" stroke="#0f172a" stroke-width="2"/><text x="50" y="105" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">E</text><text x="68" y="91" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">+</text><text x="68" y="121" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−</text><line x1="165" y1="45" x2="165" y2="78" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><line x1="165" y1="104" x2="165" y2="160" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><polygon points="154,104 176,104 165,80" fill="#fde68a" stroke="#0f172a" stroke-width="2"/><line x1="153" y1="78" x2="177" y2="78" stroke="#0f172a" stroke-width="2.4" stroke-linecap="round"/><circle cx="165" cy="45" r="3.5" fill="#0f172a"/><circle cx="165" cy="160" r="3.5" fill="#0f172a"/><text x="165" y="31" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">A</text><text x="258" y="31" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">B</text><text x="165" y="178" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">M</text><text x="110" y="17" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">K</text><text x="215" y="26" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">L, r</text><text x="254" y="106" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">R₀</text><text x="190" y="100" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">D</text><line x1="60" y1="31" x2="78.8" y2="31" stroke="#0f6e56" stroke-width="2.4" stroke-linecap="round"/><polygon points="86,31 78,35 78,27" fill="#0f6e56"/><text x="73" y="22" text-anchor="middle" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">i</text><line x1="243" y1="62" x2="196.2" y2="62" stroke="#b45309" stroke-width="2" stroke-linecap="round"/><polygon points="189,62 197,58 197,66" fill="#b45309"/><text x="216" y="76" text-anchor="middle" font-size="11" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">u_AB</text><line x1="300" y1="150" x2="300" y2="65.2" stroke="#b45309" stroke-width="2" stroke-linecap="round"/><polygon points="300,58 304,66 296,66" fill="#b45309"/><text x="305" y="112" text-anchor="start" font-size="11" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">u_BM</text></svg>
:::

Les lettres A, B, M de la figure sont celles de l'exemple : u_AB est la tension de la bobine, u_BM celle de R₀. En reliant la masse de l'oscilloscope à M, la voie sur B donne u_BM = R₀ i, image de i(t) ; la voie sur A donne u_AM = E ; la tension de la bobine est la différence u_AB = u_AM − u_BM, voie A moins voie B.

::: exemple Établir i(t) puis lire la solution

1. Loi des mailles : u_AB + u_BM = E, car, K fermé, le générateur impose E entre A et M.
2. On remplace u_AB = L di/dt + r i et u_BM = R₀ i, d'où L di/dt + R i = E avec R = R₀ + r. En divisant par L et en posant τ = L/R : di/dt + i/τ = E/L.
3. On cherche i = A e^(−αt) + B avec i(0) = 0, car la bobine interdit tout saut de courant : A + B = 0.
4. On reporte dans l'équation. Le facteur de e^(−αt) doit être nul pour tout t, donc α = 1/τ ; le terme constant donne B/τ = E/L, soit B = E/R, puis A = −E/R.
5. Résultat : i(t) = (E/R)(1 − e^(−t/τ)). Numériquement, R = 50 Ω, I₀ = 6,0 / 50 = 0,12 A et τ = 0,10 / 50 = 2,0 ms.
6. Tension de la bobine, par la loi des mailles : u_AB = E − R₀ i. À t = 0, i = 0 et u_AB = E = 6,0 V ; en régime permanent, u_AB = 6,0 − 40 × 0,12 = 1,2 V, soit r I₀ ✓.

:::

::: figure La courbe i(t) du circuit de l'exemple (E = 6,0 V, R = 50 Ω, L = 0,10 H) : elle part de 0 sans saut, monte en exponentielle (transitoire) et se stabilise à I₀ au bout d'environ 5τ (permanent)
<svg viewBox="0 0 340 215"><title>Courbe i(t) d'établissement : montée exponentielle de 0 vers l'asymptote I₀ = 0,12 A, atteinte à 1 % près au bout de 5τ</title><line x1="50" y1="190" x2="324" y2="190" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><polygon points="328,190 320,194 320,186" fill="#0f172a"/><line x1="50" y1="190" x2="50" y2="24" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><polygon points="50,20 54,28 46,28" fill="#0f172a"/><line x1="50" y1="40" x2="300" y2="40" stroke="#94a3b8" stroke-width="1.2" stroke-linecap="round" stroke-dasharray="3 3"/><line x1="300" y1="40" x2="300" y2="190" stroke="#94a3b8" stroke-width="1.2" stroke-linecap="round" stroke-dasharray="3 3"/><line x1="100" y1="95.18" x2="100" y2="190" stroke="#94a3b8" stroke-width="1.2" stroke-linecap="round" stroke-dasharray="3 3"/><polyline points="50,190 56.25,172.37 62.5,156.82 68.75,143.09 75,130.98 81.25,120.29 87.5,110.85 93.75,102.53 100,95.18 106.25,88.7 112.5,82.98 118.75,77.93 125,73.47 131.25,69.54 137.5,66.07 143.75,63 150,60.3 156.25,57.91 162.5,55.81 168.75,53.95 175,52.31 181.25,50.87 187.5,49.59 193.75,48.46 200,47.47 206.25,46.59 212.5,45.82 218.75,45.13 225,44.53 231.25,44 237.5,43.53 243.75,43.11 250,42.75 256.25,42.42 262.5,42.14 268.75,41.89 275,41.67 281.25,41.47 287.5,41.3 293.75,41.15 300,41.01 306.25,40.89 312.5,40.79" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><text x="58" y="18" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">i (A)</text><text x="44" y="44" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0,12</text><text x="44" y="194" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><text x="100" y="206" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">τ = 2,0</text><text x="300" y="206" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">5τ = 10</text><text x="324" y="182" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">t (ms)</text><text x="150" y="32" text-anchor="start" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">I₀ = E/R</text></svg>
:::

L'asymptote de la figure est I₀ = E/R, et τ = L/R règle la rapidité de la montée.

::: piege
**Erreur : calculer I₀ = E/R₀ en oubliant le fil de la bobine.** Ici E/R₀ = 6,0 / 40 = 0,15 A, alors que I₀ = 0,12 A (étape 5). L'erreur tente parce que R₀ est le seul « vrai » résistor du schéma et que la bobine passe pour un fil. Or une bobine réelle a une résistance r : en régime permanent elle équivaut à un résistor r, qui s'ajoute à R₀ dans R = R₀ + r.
:::

::: propriete
**Les valeurs aux deux extrémités** — À t = 0 : i = 0, u_BM = 0 et u_AB = E. Pour t → ∞ : i = I₀ = E/R, u_BM = R₀ E/R et u_AB = r E/R, nulle seulement si r = 0 (auquel cas u_AB = E e^(−t/τ)). Le régime permanent est atteint, à 1 % près, au bout d'environ 5τ.
:::

::: verifie À toi : un autre dipôle RL
Un dipôle RL est formé d'un générateur de f.e.m. E = 9,0 V, d'une bobine (L = 0,12 H, r = 6,0 Ω) et d'un résistor R₀ = 24 Ω. Calculer I₀ et τ, puis la tension de la bobine à t = 0 et en régime permanent.

---

R = R₀ + r = 30 Ω, donc I₀ = E/R = 9,0 / 30 = 0,30 A et τ = L/R = 0,12 / 30 = 4,0 ms. À t = 0, le courant est nul : toute la tension du générateur est aux bornes de la bobine, u_AB = 9,0 V. En régime permanent, di/dt = 0, donc u_AB = r I₀ = 6,0 × 0,30 = 1,8 V.
:::

::: retenir
Un dipôle RL soumis à un échelon E a pour courant i(t) = (E/R)(1 − e^(−t/τ)), avec R = R₀ + r et τ = L/R : il part de 0 et tend vers I₀ = E/R.
:::

## 📉 La rupture du courant dans un dipôle RL

Le régime permanent est établi dans le circuit de la section précédente (I₀ = 0,12 A) et on ouvre K. Sans diode, le courant voudrait tomber à zéro d'un coup et la bobine l'interdirait : c'est l'étincelle. Avec la diode D de la figure du circuit, supposée idéale, le courant de la bobine a un chemin : bobine, résistor R₀, diode.
Comment i évolue-t-il, et que devient la tension aux bornes de la bobine ?

::: definition
**Rupture du courant** — Après l'ouverture de K, l'intensité i ne s'annule pas brusquement : elle décroît de façon continue en exponentielle selon i(t) = (E/R) e^(−t/τ), avec R = R₀ + r et τ = L/R. Elle vérifie di/dt + i/τ = 0, équation à second membre nul.
:::

::: figure À l'ouverture de K, l'intensité i reste continue et décroît en exponentielle, mais la tension u_AB de la bobine saute de +1,2 V à −4,8 V avant de tendre vers 0
<svg viewBox="0 0 340 245"><title>À l'ouverture de K (t = 0) : l'intensité i reste continue et décroît en exponentielle, alors que la tension u_AB de la bobine saute de +1,2 V à −4,8 V avant de tendre vers 0</title><line x1="40" y1="88" x2="322" y2="88" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><polygon points="326,88 318,92 318,84" fill="#0f172a"/><line x1="40" y1="88" x2="40" y2="20" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><polygon points="40,16 44,24 36,24" fill="#0f172a"/><line x1="40" y1="160" x2="322" y2="160" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><polygon points="326,160 318,164 318,156" fill="#0f172a"/><line x1="40" y1="160" x2="40" y2="122" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><polygon points="40,118 44,126 36,126" fill="#0f172a"/><line x1="40" y1="160" x2="40" y2="238" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><polyline points="40,26 77.5,26 77.5,26 83.75,33.29 90,39.71 96.25,45.39 102.5,50.4 108.75,54.81 115,58.71 121.25,62.15 127.5,65.19 133.75,67.87 140,70.24 146.25,72.32 152.5,74.17 158.75,75.79 165,77.23 171.25,78.49 177.5,79.61 183.75,80.6 190,81.47 196.25,82.23 202.5,82.91 208.75,83.51 215,84.04 221.25,84.5 227.5,84.91 233.75,85.28 240,85.6 246.25,85.88 252.5,86.13 258.75,86.35 265,86.54 271.25,86.71 277.5,86.86 283.75,87 290,87.12 296.25,87.22 302.5,87.31 308.75,87.39 315,87.46 321.25,87.53 327.5,87.58" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><polyline points="40,142.6 77.5,142.6 77.5,229.6 77.5,229.6 83.75,221.42 90,214.2 96.25,207.84 102.5,202.21 108.75,197.25 115,192.88 121.25,189.01 127.5,185.6 133.75,182.6 140,179.94 146.25,177.6 152.5,175.53 158.75,173.71 165,172.09 171.25,170.67 177.5,169.42 183.75,168.31 190,167.34 196.25,166.47 202.5,165.71 208.75,165.04 215,164.45 221.25,163.93 227.5,163.47 233.75,163.06 240,162.7 246.25,162.38 252.5,162.1 258.75,161.85 265,161.64 271.25,161.44 277.5,161.27 283.75,161.12 290,160.99 296.25,160.88 302.5,160.77 308.75,160.68 315,160.6 321.25,160.53 327.5,160.47" fill="none" stroke="#b45309" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><line x1="77.5" y1="16" x2="77.5" y2="238" stroke="#94a3b8" stroke-width="1.2" stroke-linecap="round" stroke-dasharray="3 3"/><text x="48" y="14" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">i (A)</text><text x="34" y="30" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0,12</text><text x="48" y="128" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">u_AB (V)</text><text x="34" y="146.6" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">+1,2</text><text x="34" y="233.6" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−4,8</text><text x="87.5" y="104" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><text x="327.5" y="104" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">10</text><text x="322" y="80" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">t (ms)</text><text x="322" y="152" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">t (ms)</text></svg>
:::

Les courbes sont celles du dipôle de la section précédente, avec t = 0 à l'ouverture : i est continue en t = 0, u_AB est discontinue.

::: exemple Rupture dans le dipôle E = 6,0 V, r = 10 Ω, R₀ = 40 Ω, L = 0,10 H

1. Plus de générateur : u_AB + u_BM = 0, la diode passante jouant le rôle d'un fil. Avec u_AB = L di/dt + r i et u_BM = R₀ i, on obtient L di/dt + R i = 0, soit di/dt + i/τ = 0 avec le même τ = L/R = 2,0 ms, puisque la résistance totale est la même qu'à l'établissement.
2. On cherche i = A e^(−αt) avec i(0⁺) = I₀ = 0,12 A, car la bobine interdit tout saut de courant : A = I₀ et α = 1/τ, donc i(t) = I₀ e^(−t/τ).
3. Valeurs : i(τ) = 0,12 × 0,37 ≈ 0,044 A ; au bout de 5τ = 10 ms, i est quasi nul.
4. Tension : u_AB = −u_BM = −R₀ i. À t = 0⁺, u_AB = −40 × 0,12 = −4,8 V, alors que juste avant elle valait r I₀ = +1,2 V : elle saute de −6,0 V, soit −E, alors que i n'a pas bougé.
5. F.e.m. : u_AB = −e + r i donne e = r i − u_AB = (r + R₀) i = R i. À t = 0⁺, e = R I₀ = 50 × 0,12 = 6,0 V = E, positive : elle s'oppose à la diminution du courant.

:::

::: piege
**Erreur : garder E dans l'équation après l'ouverture.** On écrit « u_AB + u_BM = E, comme avant », et l'on retrouve un courant qui remonte vers I₀. L'erreur tente parce que l'équation de l'établissement est encore fraîche en mémoire. Or K ouvert retire le générateur de la boucle bobine-R₀-diode : le second membre vaut 0 (étape 1), et le courant ne fait que décroître.
:::

::: propriete
**Continuité et saut** — L'intensité i dans la bobine est continue, car l'énergie ½ L i² ne peut pas changer brusquement : il faudrait une puissance infinie. La tension u_AB est discontinue : elle passe de r I₀ à −R₀ I₀, soit un saut de −E ; si r = 0, elle passe de 0 à −E. À l'ouverture, e(0⁺) = R I₀ = E. La constante de temps est la même qu'à l'établissement, et le courant est quasi nul après 5τ.
:::

::: verifie À toi : une rupture à calculer
Dipôle RL en régime permanent : E = 10 V, R₀ = 45 Ω, r = 5,0 Ω, L = 0,20 H. On ouvre K, la diode conduisant. Calculer u_AB juste après l'ouverture, la f.e.m. e à cet instant et l'intensité à t = τ.

---

R = 50 Ω, I₀ = 10 / 50 = 0,20 A et τ = 0,20 / 50 = 4,0 ms. Juste après l'ouverture, i vaut encore I₀ et u_AB = −R₀ I₀ = −45 × 0,20 = −9,0 V. La f.e.m. vaut e = R I₀ = 50 × 0,20 = 10 V, égale à E. À t = τ, i = 0,37 I₀ = 0,37 × 0,20 ≈ 0,074 A.
:::

::: retenir
À la rupture, i(t) = (E/R) e^(−t/τ) décroît sans saut, alors que la tension u_AB de la bobine saute de r I₀ à −R₀ I₀ (un saut de −E).
:::

## ⏱️ La constante de temps τ = L/R

Deux dipôles RL identiques, sauf que dans l'un la résistance totale est doublée : le courant s'y installe deux fois plus vite. Dans un autre, on a doublé l'inductance : il s'installe plus lentement.
Quelle grandeur chiffre cette lenteur, et comment la lire sur un oscillogramme, celui de i(t) comme celui de la tension u_L de la bobine ?

::: definition
**Constante de temps** — La constante de temps d'un dipôle RL est τ = L/R, en seconde (L en henry, R en ohm). Elle renseigne sur le retard avec lequel s'établit le régime permanent, ou avec lequel s'éteint le courant à la rupture. La durée pour atteindre une même fraction de la valeur finale est proportionnelle à τ, donc proportionnelle à L et inversement proportionnelle à R.
:::

::: figure La tension u_L(t) de la bobine du dipôle précédent : de 6,0 V vers l'asymptote 1,2 V ; la tangente à l'origine coupe l'asymptote en t = 2,0 ms (τ), pas l'axe des temps (2,5 ms)
<svg viewBox="0 0 340 225"><title>Courbe u_L(t) de la tension de la bobine à l'établissement : de 6,0 V vers l'asymptote 1,2 V ; la tangente à l'origine coupe l'asymptote en t = 2,0 ms, l'axe des temps en 2,5 ms</title><line x1="50" y1="190" x2="326" y2="190" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><polygon points="330,190 322,194 322,186" fill="#0f172a"/><line x1="50" y1="190" x2="50" y2="22" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><polygon points="50,18 54,26 46,26" fill="#0f172a"/><line x1="50" y1="158" x2="330" y2="158" stroke="#94a3b8" stroke-width="1.2" stroke-linecap="round" stroke-dasharray="3 3"/><polyline points="50,30 58,42.18 66,53.2 74,63.18 82,72.2 90,80.36 98,87.75 106,94.44 114,100.49 122,105.96 130,110.91 138,115.39 146,119.45 154,123.12 162,126.44 170,129.44 178,132.16 186,134.62 194,136.84 202,138.86 210,140.68 218,142.33 226,143.82 234,145.17 242,146.39 250,147.49 258,148.49 266,149.4 274,150.22 282,150.96 290,151.63 298,152.23 306,152.78 314,153.28 322,153.73 330,154.13" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><polyline points="50,30 130,158" fill="none" stroke="#b45309" stroke-width="2.2" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="7 4"/><polyline points="130,158 150,190" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="3 3"/><line x1="50" y1="110.91" x2="130" y2="110.91" stroke="#94a3b8" stroke-width="1.2" stroke-linecap="round" stroke-dasharray="3 3"/><line x1="130" y1="110.91" x2="130" y2="190" stroke="#94a3b8" stroke-width="1.2" stroke-linecap="round" stroke-dasharray="3 3"/><circle cx="130" cy="110.91" r="3.8" fill="#0f6e56"/><circle cx="130" cy="158" r="3.8" fill="#b45309"/><text x="58" y="16" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">u_L (V)</text><text x="44" y="34" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">6,0</text><text x="44" y="162" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1,2</text><text x="44" y="114.91" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">≈ 3,0</text><text x="124" y="206" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2,0</text><text x="160" y="221" text-anchor="middle" font-size="12" font-weight="700" fill="#64748b" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2,5</text><text x="326" y="182" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">t (ms)</text></svg>
:::

Sur la figure, u_L ne tend pas vers 0 mais vers r I₀ = 1,2 V : c'est donc l'**asymptote** que la tangente à l'origine rejoint à l'abscisse τ.

::: exemple Lire τ sur la courbe u_L(t) de la figure

1. Lecture : u_L part de E = 6,0 V et tend vers l'asymptote 1,2 V.
2. La tangente à l'origine rejoint l'asymptote en t = 2,0 ms, donc τ = 2,0 ms.
3. Contrôle par l'écart à l'asymptote : à t = τ, cet écart (initialement 6,0 − 1,2 = 4,8 V) est multiplié par 0,37, d'où u_L(τ) ≈ 1,2 + 0,37 × 4,8 ≈ 3,0 V, ordonnée du point marqué sur la courbe ✓.
4. Inductance : R = R₀ + r = 40 + 10 = 50 Ω, donc L = τ R = 2,0 × 10⁻³ × 50 = 0,10 H ; les unités s'accordent, des ohms multipliés par des secondes donnent des henrys.
5. Le régime permanent est atteint au bout d'environ 5τ = 10 ms.

:::

::: piege
**Erreur : lire τ là où la tangente coupe l'axe des temps.** Pour u_L(t), cela donne ici 2,5 ms au lieu de 2,0 ms. L'erreur tente parce qu'à la rupture de i(t) la tangente à l'origine coupe bien l'axe des temps en τ. Mais la courbe u_L(t) tend vers 1,2 V, pas vers 0 : le point de repère est l'asymptote, jamais l'axe des temps (étape 2).
:::

::: figure La courbe i(t) d'établissement : la tangente à l'origine atteint l'asymptote I₀ à l'abscisse τ, et le point d'ordonnée 0,63 I₀ a la même abscisse
<svg viewBox="0 0 340 215"><title>Courbe i(t) d'établissement avec la tangente à l'origine, qui atteint l'asymptote I₀ = 0,12 A à l'abscisse τ, et le point d'ordonnée 0,63 I₀ à la même abscisse</title><line x1="50" y1="190" x2="324" y2="190" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><polygon points="328,190 320,194 320,186" fill="#0f172a"/><line x1="50" y1="190" x2="50" y2="24" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><polygon points="50,20 54,28 46,28" fill="#0f172a"/><line x1="50" y1="40" x2="300" y2="40" stroke="#94a3b8" stroke-width="1.2" stroke-linecap="round" stroke-dasharray="3 3"/><polyline points="50,190 56.25,172.37 62.5,156.82 68.75,143.09 75,130.98 81.25,120.29 87.5,110.85 93.75,102.53 100,95.18 106.25,88.7 112.5,82.98 118.75,77.93 125,73.47 131.25,69.54 137.5,66.07 143.75,63 150,60.3 156.25,57.91 162.5,55.81 168.75,53.95 175,52.31 181.25,50.87 187.5,49.59 193.75,48.46 200,47.47 206.25,46.59 212.5,45.82 218.75,45.13 225,44.53 231.25,44 237.5,43.53 243.75,43.11 250,42.75 256.25,42.42 262.5,42.14 268.75,41.89 275,41.67 281.25,41.47 287.5,41.3 293.75,41.15 300,41.01 306.25,40.89 312.5,40.79" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><polyline points="50,190 100,40" fill="none" stroke="#b45309" stroke-width="2.2" stroke-linejoin="round" stroke-linecap="round" stroke-dasharray="7 4"/><line x1="100" y1="40" x2="100" y2="190" stroke="#94a3b8" stroke-width="1.2" stroke-linecap="round" stroke-dasharray="3 3"/><line x1="50" y1="95.18" x2="100" y2="95.18" stroke="#94a3b8" stroke-width="1.2" stroke-linecap="round" stroke-dasharray="3 3"/><circle cx="100" cy="40" r="3.8" fill="#b45309"/><circle cx="100" cy="95.18" r="3.8" fill="#0f6e56"/><text x="58" y="18" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">i (A)</text><text x="44" y="44" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0,12</text><text x="44" y="99.18" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0,076</text><text x="100" y="206" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">τ</text><text x="324" y="182" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">t (ms)</text><text x="110" y="117.18" text-anchor="start" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0,63 I₀</text></svg>
:::

La tangente à l'origine de i(t) a pour pente I₀/τ : elle atteint I₀ au bout de la durée τ, et c'est aussi à cette abscisse que la courbe passe par 0,63 I₀.

::: propriete
**Les lectures de τ** — Calcul direct : τ = L/R. Établissement de i(t) : la tangente à l'origine coupe l'asymptote I₀ en τ, et i(τ) = 0,63 I₀. Rupture de i(t) : la tangente à l'origine coupe l'axe des temps en τ, et i(τ) = 0,37 I₀. Courbe u_L(t) : la tangente à l'origine coupe l'asymptote en τ. À τ, i n'est pas encore à I₀ : il faut 5τ pour être à 1 % près. Doubler R divise τ par 2 (et I₀ aussi, puisque I₀ = E/R) ; doubler L double τ sans changer I₀.
:::

::: verifie À toi : dimensionner un dipôle RL
On dispose d'une bobine L = 0,30 H avec r = 20 Ω. On veut τ = 1,0 ms. Quelle résistance totale R faut-il, quelle valeur donner à R₀, et quel courant I₀ obtient-on avec E = 6,0 V ?

---

De τ = L/R on tire R = L/τ = 0,30 / 0,0010 = 300 Ω. Comme R = R₀ + r, on a R₀ = 300 − 20 = 280 Ω. Le courant final est I₀ = E/R = 6,0 / 300 = 0,020 A, soit 20 mA.
:::

::: retenir
La constante de temps τ = L/R chiffre la durée du transitoire : tangente à l'origine rejoignant l'asymptote en τ, 63 % de I₀ atteints à τ à l'établissement, 37 % restants à la rupture, régime permanent vers 5τ.
:::

## 🔌 L'alternateur et le transformateur

La plaque d'une cuisinière à induction reste froide, et pourtant la casserole posée dessus chauffe. Dans la plaque, un circuit est parcouru par un courant alternatif. Dans un alternateur, un aimant tourne devant des bobines. Dans un transformateur, deux bobines sont face à face.
Qu'ont en commun ces dispositifs, et que doit-il se passer pour qu'ils fonctionnent ?

::: definition
**Alternateur et transformateur** — Un **alternateur** convertit de l'énergie mécanique en énergie électrique par induction : un inducteur fait varier le champ magnétique à travers un induit (des bobines). Dans l'alternateur d'une voiture, l'induit est fixe (stator) et l'inducteur, un aimant multipolaire, tourne (rotor) ; la fréquence de la tension est liée à la fréquence de rotation. Un **transformateur** est un quadripôle formé de deux bobines (primaire et secondaire) : il abaisse ou élève une tension alternative.
:::

::: figure Un alternateur : l'aimant (rotor) tourne entre des bobines fixes (stator) ; il fait varier le champ à travers elles et y induit le courant
<svg viewBox="0 0 340 185"><title>Alternateur : un aimant (rotor) tourne entre des bobines fixes (stator) dans lesquelles apparaît le courant induit</title><circle cx="170" cy="100" r="46" fill="#f1f5f9" stroke="#0f172a" stroke-width="2"/><rect x="142" y="88" width="28" height="24" fill="#fecaca" stroke="#0f172a" stroke-width="2"/><rect x="170" y="88" width="28" height="24" fill="#bfdbfe" stroke="#0f172a" stroke-width="2"/><text x="156" y="105" text-anchor="middle" font-size="14" font-weight="700" fill="#b91c1c" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">N</text><text x="184" y="105" text-anchor="middle" font-size="14" font-weight="700" fill="#1d4ed8" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">S</text><rect x="36" y="60" width="40" height="80" fill="#ffffff" stroke="#0f172a" stroke-width="2"/><line x1="42" y1="66" x2="42" y2="134" stroke="#0f6e56" stroke-width="2.2" stroke-linecap="round"/><line x1="49" y1="66" x2="49" y2="134" stroke="#0f6e56" stroke-width="2.2" stroke-linecap="round"/><line x1="56" y1="66" x2="56" y2="134" stroke="#0f6e56" stroke-width="2.2" stroke-linecap="round"/><line x1="63" y1="66" x2="63" y2="134" stroke="#0f6e56" stroke-width="2.2" stroke-linecap="round"/><line x1="70" y1="66" x2="70" y2="134" stroke="#0f6e56" stroke-width="2.2" stroke-linecap="round"/><rect x="264" y="60" width="40" height="80" fill="#ffffff" stroke="#0f172a" stroke-width="2"/><line x1="270" y1="66" x2="270" y2="134" stroke="#0f6e56" stroke-width="2.2" stroke-linecap="round"/><line x1="277" y1="66" x2="277" y2="134" stroke="#0f6e56" stroke-width="2.2" stroke-linecap="round"/><line x1="284" y1="66" x2="284" y2="134" stroke="#0f6e56" stroke-width="2.2" stroke-linecap="round"/><line x1="291" y1="66" x2="291" y2="134" stroke="#0f6e56" stroke-width="2.2" stroke-linecap="round"/><line x1="298" y1="66" x2="298" y2="134" stroke="#0f6e56" stroke-width="2.2" stroke-linecap="round"/><path d="M 140 52 A 36 36 0 0 1 200 52" fill="none" stroke="#b45309" stroke-width="2.4"/><polygon points="200,52 191.28,46.99 198.78,42.01" fill="#b45309"/><text x="170" y="26" text-anchor="middle" font-size="12" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">rotation</text><text x="56" y="160" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">stator</text><text x="284" y="160" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">stator</text><text x="170" y="170" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">rotor</text><line x1="76" y1="100" x2="124" y2="100" stroke="#94a3b8" stroke-width="1.4" stroke-linecap="round" stroke-dasharray="3 3"/><line x1="216" y1="100" x2="264" y2="100" stroke="#94a3b8" stroke-width="1.4" stroke-linecap="round" stroke-dasharray="3 3"/></svg>
:::

Sur la figure, l'aimant est l'inducteur et les bobines fixes sont l'induit : le courant utile naît dans le stator.

::: exemple Pourquoi la casserole chauffe sur une plaque à induction

1. Sous la plaque, un circuit inducteur est parcouru par un courant alternatif, donc il crée un champ magnétique qui varie sans cesse.
2. Le fond métallique de la casserole, fermé sur lui-même, est un circuit induit placé dans ce champ variable : un courant induit y apparaît.
3. Ce courant dissipe de l'énergie par effet Joule dans le métal : la casserole chauffe, alors que la plaque, qui ne contient aucun circuit induit, reste froide.
4. L'énergie vient du générateur qui alimente le circuit inducteur ; la loi de Lenz explique que le courant induit s'oppose à la variation de champ, ce qui fait payer au générateur l'énergie dissipée.

:::

::: piege
**Erreur : confondre inducteur et induit dans l'alternateur.** L'aimant qui tourne est l'**inducteur** (il impose la variation du champ) ; ce sont les bobines fixes du stator qui sont l'**induit** (elles fournissent le courant). L'erreur tente parce que l'aimant « produit » le champ et qu'on le prend pour la source du courant : la source du courant est l'induit.
:::

::: propriete
**Condition de fonctionnement** — Tous ces dispositifs exigent un champ qui **varie**. Un alternateur dont l'aimant tourne plus vite produit une tension de fréquence plus grande et un courant induit plus intense, puisque la variation est plus rapide. Un transformateur ne fonctionne qu'en régime variable : sous tension continue, son primaire est parcouru par un courant constant, donc le champ ne varie pas et le secondaire reste sans tension. Cas limite : rotor à l'arrêt, aucun courant induit.
:::

::: verifie À toi : un transformateur sur une pile
Un transformateur est branché sur une pile. Un voltmètre est placé aux bornes du secondaire. Que lit-il quand le courant du primaire est établi et constant ? Et à l'instant précis où l'on ferme l'interrupteur ?

---

Quand le courant du primaire est constant, le champ ne varie plus : aucune f.e.m. n'est induite et le voltmètre lit 0 V. À la fermeture, le courant du primaire passe de 0 à sa valeur finale : le champ varie un très court instant et le voltmètre indique brièvement une tension, qui disparaît quand le courant est établi.
:::

::: retenir
Un alternateur convertit de l'énergie mécanique en énergie électrique par induction ; un transformateur n'abaisse ou n'élève qu'une tension alternative, car un courant constant n'induit rien.
:::

> 🏆 Quête franchie, héros ! Tu sais lire Lenz sur un aimant, calculer e et u_AB, chiffrer l'énergie d'une bobine, suivre l'établissement et la rupture d'un dipôle RL et en tirer τ sur i(t) comme sur u_L(t). Le prochain chapitre fait osciller tout cela.
