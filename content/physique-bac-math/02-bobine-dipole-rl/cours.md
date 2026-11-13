# 🧲 La bobine et le dipôle RL — quand le courant se fait désirer

> 💡 «Une bobine n'aime pas qu'on la brusque : elle freine toute variation du courant qui la traverse. Tout le chapitre tient dans cette phrase.»

Branche une bobine sur un milliampèremètre, approche un aimant : un courant naît sans aucun générateur. Place la même bobine dans un circuit, ferme l'interrupteur : le courant arrive avec du retard. Huit notions expliquent ces deux surprises : l'induction et la loi de Lenz, l'auto-induction, la tension aux bornes d'une bobine, l'énergie magnétique, l'établissement puis la rupture du courant dans un dipôle RL, la constante de temps, et enfin l'alternateur et le transformateur. On suppose acquis le champ magnétique d'une bobine et d'un aimant, la loi d'Ohm, la loi des mailles, la dérivée et l'exponentielle (comme pour le dipôle RC du chapitre précédent).

## 🧲 L'induction électromagnétique et la loi de Lenz

Une bobine est fermée sur un milliampèremètre à zéro central, sans pile ni générateur. On approche d'une de ses faces le pôle nord d'un barreau aimanté : l'aiguille dévie, puis revient à zéro dès qu'on arrête de bouger. On éloigne l'aimant : l'aiguille dévie dans l'autre sens. Aimant immobile, même collé à la bobine : rien.
D'où vient ce courant, et dans quel sens circule-t-il ?

::: definition
**Induction électromagnétique** — Toute variation du champ magnétique au voisinage d'un circuit fermé produit dans ce circuit un courant, appelé **courant induit**. Ce qui provoque la variation (un aimant qu'on déplace, une bobine parcourue par un courant variable) est l'**inducteur** ; le circuit où naît le courant est l'**induit**. Le courant induit est d'autant plus intense que la variation est plus rapide.
:::

::: definition
**Loi de Lenz** — Le courant induit a un sens tel qu'il s'oppose, par ses effets, à la cause qui lui donne naissance.
:::

::: figure Le pôle nord de l'aimant s'approche : le champ inducteur B augmente dans la bobine, le champ induit b est de sens contraire et la bobine présente sa face nord à l'aimant
<svg viewBox="0 0 340 180"><title>Aimant dont le pôle nord s'approche d'une bobine : champ inducteur B, champ induit b, faces nord et sud de la bobine</title><rect x="20" y="75" width="50" height="40" fill="#bfdbfe" stroke="#0f172a" stroke-width="2"/><rect x="70" y="75" width="50" height="40" fill="#fecaca" stroke="#0f172a" stroke-width="2"/><text x="45" y="100" text-anchor="middle" font-size="15" font-weight="700" fill="#1d4ed8" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">S</text><text x="95" y="100" text-anchor="middle" font-size="15" font-weight="700" fill="#b91c1c" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">N</text><line x1="30" y1="56" x2="96" y2="56" stroke="#0f172a" stroke-width="2.4" stroke-linecap="round"/><polygon points="104,56 96,52 96,60" fill="#0f172a"/><text x="66" y="47" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">v</text><ellipse cx="212" cy="95" rx="6" ry="34" fill="none" stroke="#0f172a" stroke-width="2"/><ellipse cx="228" cy="95" rx="6" ry="34" fill="none" stroke="#0f172a" stroke-width="2"/><ellipse cx="244" cy="95" rx="6" ry="34" fill="none" stroke="#0f172a" stroke-width="2"/><ellipse cx="260" cy="95" rx="6" ry="34" fill="none" stroke="#0f172a" stroke-width="2"/><ellipse cx="276" cy="95" rx="6" ry="34" fill="none" stroke="#0f172a" stroke-width="2"/><line x1="128" y1="95" x2="188" y2="95" stroke="#0f172a" stroke-width="2.6" stroke-linecap="round"/><polygon points="196,95 188,91 188,99" fill="#0f172a"/><text x="160" y="84" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">B</text><line x1="270" y1="118" x2="220" y2="118" stroke="#0f6e56" stroke-width="2.8" stroke-linecap="round"/><polygon points="212,118 220,114 220,122" fill="#0f6e56"/><text x="246" y="137" text-anchor="middle" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">b</text><text x="205" y="160" text-anchor="middle" font-size="14" font-weight="700" fill="#b91c1c" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">N</text><text x="285" y="160" text-anchor="middle" font-size="14" font-weight="700" fill="#1d4ed8" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">S</text><line x1="205" y1="140" x2="205" y2="146" stroke="#94a3b8" stroke-width="1.2" stroke-linecap="round"/><line x1="285" y1="140" x2="285" y2="146" stroke="#94a3b8" stroke-width="1.2" stroke-linecap="round"/></svg>
:::

Sur la figure, B est le champ de l'aimant (inducteur) et b celui du courant induit : ce sont les deux flèches du raisonnement qui suit, et les lettres N et S sous la bobine nomment ses deux faces.

::: exemple Deux déplacements, deux sens de courant

1. On approche le pôle nord (face de gauche). Le champ B⃗ de l'aimant traverse la bobine vers la droite et sa valeur ‖B⃗‖ augmente, puisque l'aimant se rapproche.
2. La bobine doit s'opposer à cette augmentation (loi de Lenz) : son champ b⃗ est de sens contraire à B⃗, donc dirigé vers la gauche à l'intérieur.
3. Un champ qui sort par la face de gauche signale une face nord : la bobine présente une face nord au pôle nord. Deux pôles de même nom se repoussent, ce qui freine l'approche.
4. On éloigne maintenant le pôle sud, toujours face à la bobine. Le champ B⃗ traverse la bobine vers l'aimant (les lignes de champ rentrent dans un pôle sud) et sa valeur diminue.
5. La bobine doit compenser cette diminution : b⃗ a le même sens que B⃗, donc il sort par la face en regard, qui est une face nord. Face nord contre pôle sud : attraction, qui retient l'aimant.
6. Dans les deux cas, le sens du courant se déduit de celui de b⃗ par la règle du bonhomme d'Ampère.

:::

::: piege
**Erreur : croire que le champ induit b⃗ est toujours opposé à B⃗.** À l'approche du pôle nord (étape 2), b⃗ est bien opposé à B⃗ ; à l'éloignement du pôle sud (étape 5), b⃗ a le même sens que B⃗. L'erreur tente parce que « s'oppose » évoque un sens contraire. Or la loi de Lenz s'oppose à la **variation** de ‖B⃗‖ : contre une augmentation, b⃗ est opposé à B⃗ ; contre une diminution, b⃗ renforce B⃗.
:::

::: propriete
**Ce qui reste vrai à chaque fois** — Variation de ‖B⃗‖ vers le haut : b⃗ opposé à B⃗, répulsion bobine-aimant. Variation vers le bas : b⃗ de même sens que B⃗, attraction. Le signe de la tension aux bornes d'une résistance en série change quand on inverse le déplacement. Cas limite : aimant immobile, ou bobine voisine parcourue par un courant continu constant, donc champ constant : aucun courant induit, même si le champ est intense.
:::

::: verifie À toi : le pôle sud qu'on approche
On approche le pôle sud d'un aimant de la face de gauche d'une bobine fermée. Quelle face la bobine présente-t-elle à l'aimant, et la force entre eux est-elle attractive ou répulsive ?

---

Le champ B⃗ de l'aimant traverse la bobine vers l'aimant (il rentre dans le pôle sud) et sa valeur augmente. La loi de Lenz impose un champ b⃗ opposé, donc dirigé vers la droite : il sort par la face de droite, qui est la face nord, si bien que la face de gauche, en regard de l'aimant, est une face sud. Face sud contre pôle sud : les deux se repoussent, ce qui s'oppose bien à l'approche.
:::

::: retenir
Toute variation du champ magnétique près d'un circuit fermé y induit un courant, d'autant plus intense que la variation est rapide, et son sens est tel que ses effets s'opposent à la cause (loi de Lenz).
:::

## 🔁 L'auto-induction et la force électromotrice e = −L di/dt

Deux branches en parallèle sur un même générateur : l'une contient un résistor et une lampe L1, l'autre une bobine et une lampe L2, le résistor et la bobine ayant la même résistance. À la fermeture, L1 brille aussitôt ; L2 met quelques millièmes de secondes à atteindre le même éclat. Une fois le régime établi, les deux lampes brillent pareil.
Qu'est-ce qui retarde le courant dans la bobine ?

::: definition
**Auto-induction** — Quand le courant qui traverse une bobine varie, son propre champ varie : la bobine est à la fois inducteur et induit, et elle est le siège d'une force électromotrice (f.e.m.) d'auto-induction e = −L di/dt. La grandeur L est l'**inductance** de la bobine, en henry (H).
:::

::: figure Une même bobine : quand i(t) monte de 0 à 100 mA en 20 ms puis retombe en 5 ms, la f.e.m. e(t) reste constante sur chaque phase, négative à la montée et positive à la descente
<svg viewBox="0 0 340 215"><title>Courant i(t) en dents de scie et force électromotrice e(t) en créneaux</title><line x1="50" y1="95" x2="322" y2="95" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><line x1="50" y1="95" x2="50" y2="14" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><polygon points="326,95 318,91 318,99" fill="#0f172a"/><polygon points="50,10 46,18 54,18" fill="#0f172a"/><polyline points="50,95 250,35 300,95" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><line x1="250" y1="35" x2="250" y2="175" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="3 3" stroke-linecap="round"/><line x1="300" y1="95" x2="300" y2="175" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="3 3" stroke-linecap="round"/><line x1="50" y1="35" x2="250" y2="35" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="3 3" stroke-linecap="round"/><text x="60" y="20" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">i (mA)</text><text x="44" y="38" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">100</text><text x="250" y="110" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">20</text><text x="302" y="110" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">25</text><text x="322" y="60" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">t (ms)</text><line x1="50" y1="175" x2="322" y2="175" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><line x1="50" y1="175" x2="50" y2="112" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><polygon points="326,175 318,171 318,179" fill="#0f172a"/><polygon points="50,108 46,116 54,116" fill="#0f172a"/><polyline points="50,187.5 250,187.5 250,125 300,125 300,175 322,175" fill="none" stroke="#b45309" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><text x="60" y="118" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">e (V)</text><text x="44" y="129" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">+1,0</text><text x="44" y="201.5" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−0,25</text></svg>
:::

Chaque palier de e(t) correspond à une pente de i(t) : la montée lente donne un petit palier négatif, la descente rapide un grand palier positif, d'où le signe − de la formule e = −L di/dt.

::: exemple Lire e(t) sur la courbe i(t) de la figure, avec L = 50 mH

1. Montée : di/dt = 0,100 A / 0,020 s = 5,0 A/s, la pente de i(t) (on convertit les ms en s).
2. e = −L di/dt = −0,050 × 5,0 = −0,25 V. Elle est négative, car i croît et la f.e.m. s'oppose à cette croissance.
3. Descente : di/dt = −0,100 A / 0,005 s = −20 A/s, donc e = −0,050 × (−20) = +1,0 V. Elle est positive, car i décroît et la f.e.m. s'oppose à cette décroissance.
4. Contrôle : la descente est 4 fois plus rapide que la montée, donc |e| est 4 fois plus grand (1,0 / 0,25 = 4) ✓.

:::

::: piege
**Erreur : relier e à la valeur de i au lieu de sa variation.** « Plus le courant est intense, plus e est grande » est faux : avec un courant constant de 2 A, di/dt = 0, donc e = 0. L'erreur tente parce que, pour un résistor, la tension U = R × I suit bien la valeur de I. Pour une bobine, c'est la rapidité de variation di/dt qui compte, jamais la valeur de i seule.
:::

::: propriete
**Signe de e et facteurs de L** — Si i croît, di/dt > 0 et e < 0 ; si i décroît, e > 0 : le signe − traduit la loi de Lenz, e s'oppose toujours à la variation de i. Sans noyau de fer, l'inductance ne dépend que de la géométrie de la bobine : elle augmente avec le nombre N de spires et avec la section, et diminue quand la longueur augmente ; elle ne dépend ni de i, ni de la tension, ni de la fréquence. Les bobines usuelles ont L bien inférieure à 1 H. Cas limite : courant constant, e = 0. Un noyau de fer doux augmente L, mais e = −L di/dt cesse alors d'être valable.
:::

::: verifie À toi : une f.e.m. à calculer
Une bobine d'inductance L = 0,40 H est parcourue par un courant qui passe régulièrement de 0,30 A à 0,10 A en 50 ms. Calculer e.

---

On a di/dt = (0,10 − 0,30) / 0,050 = −4,0 A/s, puis e = −L di/dt = −0,40 × (−4,0) = +1,6 V. Le résultat est positif parce que i décroît : la f.e.m. s'oppose à la diminution du courant, comme dans le cas de la descente de la figure.
:::

::: retenir
Une bobine d'inductance L parcourue par un courant variable est le siège d'une f.e.m. d'auto-induction e = −L di/dt, de signe opposé à la variation de i, et L ne dépend que de la géométrie.
:::

## 📏 La tension aux bornes d'une bobine

Une bobine réelle est un long fil enroulé : il a donc une résistance r, en plus de l'effet d'auto-induction.
Si tu mesures la tension à ses bornes, que lis-tu quand le courant varie, et que lis-tu quand il ne varie plus ?

::: definition
**Tension aux bornes d'une bobine (L, r)** — Une bobine se modélise par une inductance L en série avec un résistor de résistance r. Quand le courant i la traverse de A vers B, la tension vaut u_AB = L di/dt + r i. Elle vient de u_AB = −e + r i avec e = −L di/dt.
:::

::: exemple Bobine L = 0,20 H, r = 5,0 Ω, courant i(t) = 0,30 t (en A, t en s) de A vers B

1. On dérive : di/dt = 0,30 A/s, donc le terme inductif vaut L di/dt = 0,20 × 0,30 = 0,060 V.
2. Le terme résistif vaut r i = 5,0 × 0,30 t = 1,5 t (en V), car la loi d'Ohm s'applique au fil de la bobine.
3. u_AB = 0,060 + 1,5 t ; à t = 2,0 s, u_AB = 0,060 + 3,0 = 3,06 V.
4. Courant constant I = 0,40 A : di/dt = 0, donc u_AB = r I = 5,0 × 0,40 = 2,0 V. En régime permanent, la bobine se comporte comme un simple résistor de résistance r.

:::

::: piege
**Erreur : écrire u_AB = −L di/dt + r i.** Le signe − appartient à la f.e.m. e = −L di/dt, pas à la tension. Pour une bobine de résistance négligeable dont le courant croît, e est négative (elle s'oppose), mais u_AB = +L di/dt est positive : c'est la tension que le circuit doit fournir pour forcer le courant à croître. Avec les données de l'exemple, l'erreur donnerait −0,060 + 1,5 t au lieu de 0,060 + 1,5 t.
:::

::: propriete
**Trois cas à reconnaître** — Courant constant : u_AB = r i (la bobine n'est qu'un résistor, et u_AB = 0 si r = 0). Résistance négligeable : u_AB = L di/dt. Courant coupé très brusquement : di/dt est énorme, le terme L di/dt l'emporte sur r i et la tension aux bornes devient très grande.
:::

::: verifie À toi : une bobine sans résistance
Une bobine d'inductance 80 mH, de résistance négligeable, voit son courant monter régulièrement de 0 à 60 mA en 30 ms. Quelle est la tension à ses bornes ?

---

La résistance est négligeable, donc u_AB = L di/dt. Ici di/dt = 0,060 / 0,030 = 2,0 A/s, d'où u_AB = 0,080 × 2,0 = 0,16 V, positive puisque le courant croît.
:::

::: retenir
Une bobine (L, r) traversée par i de A vers B présente la tension u_AB = L di/dt + r i : seul r compte quand le courant est constant.
:::

## 🔋 L'énergie magnétique et l'étincelle de rupture

Coupe brusquement le courant dans une bobine : une étincelle jaillit à l'interrupteur, comme si la bobine rendait quelque chose. La puissance qu'elle reçoit s'écrit p = u_AB × i = r i² + L i di/dt. Le premier terme est la chaleur dégagée par effet Joule.
Où va le second ?

::: definition
**Énergie magnétique** — Le terme L i di/dt est la dérivée de ½ L i² : il sert à emmagasiner dans la bobine l'énergie magnétique E_L = ½ L i², en joule (J) avec L en henry et i en ampère. La bobine est un réservoir **temporaire** : tant qu'un courant la traverse, elle stocke de l'énergie ; quand i diminue, elle la restitue et joue le rôle de générateur.
:::

::: exemple Une bobine L = 0,25 H parcourue par I = 0,40 A, coupée en Δt = 1,0 ms

1. Énergie stockée : E_L = ½ × 0,25 × (0,40)² = 0,5 × 0,25 × 0,16 = 0,020 J = 20 mJ.
2. Coupure brusque : le courant tombe de 0,40 A à 0 en 1,0 ms, donc |e| ≈ L Δi/Δt = 0,25 × 0,40 / 0,0010 = 100 V.
3. Cent volts alors que le circuit n'est alimenté que par quelques volts : l'air entre les contacts s'ionise, c'est l'étincelle de rupture. Les 20 mJ ne disparaissent pas, ils sont restitués en environ 1 ms.
4. Une diode branchée en sens inverse du générateur ne conduit pas pendant l'établissement ; à la rupture, elle offre au courant de la bobine un chemin sans coupure brutale et protège l'interrupteur.

:::

::: piege
**Erreur : « la bobine garde son énergie comme un condensateur ».** Un condensateur chargé puis débranché conserve son énergie ; une bobine, non : E_L = ½ L i² s'annule dès que i s'annule. L'erreur tente parce que les deux sont des « réservoirs d'énergie ». Le condensateur est un réservoir permanent, la bobine un réservoir temporaire.
:::

::: propriete
**Ce qu'il faut savoir manier** — E_L croît comme i² : doubler i multiplie E_L par 4. E_L ne dépend pas du sens du courant et vaut zéro si i = 0. Une variation d'énergie se calcule par ½ L i₂² − ½ L i₁², jamais par ½ L (i₂ − i₁)². Un courant coupé en un temps très court Δt donne |e| ≈ L Δi/Δt, d'autant plus grande que Δt est petit.
:::

::: verifie À toi : doubler le courant
Une bobine L = 80 mH est parcourue par 0,30 A. Calculer E_L, puis dire sans refaire le calcul de l'énergie ce qu'elle devient pour 0,60 A.

---

E_L = ½ × 0,080 × (0,30)² = 0,5 × 0,080 × 0,090 = 3,6 mJ. Comme E_L est proportionnelle à i², doubler le courant multiplie l'énergie par 2² = 4 : E_L = 14,4 mJ pour 0,60 A.
:::

::: retenir
Une bobine parcourue par i emmagasine l'énergie E_L = ½ L i², réservoir temporaire que la rupture du courant restitue au circuit.
:::

## 📈 L'établissement du courant dans un dipôle RL

On ferme K sur un circuit en série : un générateur de f.e.m. E = 12 V, une bobine (L = 0,30 H, r = 10 Ω) et un résistor R₀ = 50 Ω. Un résistor seul porterait le courant à sa valeur finale d'un coup. Ici, l'oscilloscope branché aux bornes de R₀ montre une montée progressive.
Quelle loi donne i(t), et vers quelle valeur le courant tend-il ?

::: definition
**Dipôle RL, échelon de tension** — Un dipôle RL associe en série une bobine (L, r) et un résistor R₀ : sa résistance totale est R = R₀ + r. Soumis à un échelon de tension (on passe de 0 à E à t = 0), il est parcouru par un courant qui traverse un **régime transitoire** avant d'atteindre un **régime permanent**, de valeur I₀ = E/R, où la bobine se comporte comme un résistor de résistance r.
:::

::: figure Le dipôle RL : la bobine (L, r) entre A et B, le résistor R₀ entre B et M ; la diode D relie M à A et reste bloquée tant que K est fermé
<svg viewBox="0 0 340 195"><title>Circuit série : générateur E, interrupteur K, bobine (L, r) entre A et B, résistor R₀ entre B et M, diode D entre M et A</title><line x1="50" y1="40" x2="95" y2="40" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><line x1="130" y1="40" x2="190" y2="40" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><line x1="95" y1="40" x2="125" y2="24" stroke="#0f172a" stroke-width="2" stroke-linecap="round"/><circle cx="95" cy="40" r="3.5" fill="#0f172a"/><circle cx="130" cy="40" r="3.5" fill="#0f172a"/><path d="M190 40 a8.75 11 0 0 1 17.5 0 a8.75 11 0 0 1 17.5 0 a8.75 11 0 0 1 17.5 0 a8.75 11 0 0 1 17.5 0" fill="none" stroke="#0f172a" stroke-width="2"/><line x1="260" y1="40" x2="290" y2="40" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><line x1="290" y1="40" x2="290" y2="82" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><line x1="290" y1="124" x2="290" y2="160" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><rect x="282" y="82" width="16" height="42" fill="#ffffff" stroke="#0f172a" stroke-width="2"/><line x1="290" y1="160" x2="50" y2="160" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><line x1="50" y1="40" x2="50" y2="84" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><line x1="50" y1="116" x2="50" y2="160" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><circle cx="50" cy="100" r="16" fill="#ffffff" stroke="#0f172a" stroke-width="2"/><text x="50" y="105" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">E</text><text x="70" y="92" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">+</text><text x="70" y="122" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−</text><line x1="165" y1="40" x2="165" y2="74" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><line x1="165" y1="100" x2="165" y2="160" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><polygon points="154,100 176,100 165,76" fill="#fde68a" stroke="#0f172a" stroke-width="2"/><line x1="153" y1="74" x2="177" y2="74" stroke="#0f172a" stroke-width="2.4" stroke-linecap="round"/><circle cx="165" cy="40" r="3.5" fill="#0f172a"/><circle cx="165" cy="160" r="3.5" fill="#0f172a"/><text x="165" y="28" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">A</text><text x="272" y="30" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">B</text><text x="165" y="178" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">M</text><text x="110" y="14" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">K</text><text x="225" y="18" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">L, r</text><text x="318" y="107" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">R₀</text><text x="190" y="98" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">D</text><line x1="60" y1="28" x2="84" y2="28" stroke="#0f6e56" stroke-width="2.4" stroke-linecap="round"/><polygon points="92,28 84,24 84,32" fill="#0f6e56"/><text x="76" y="19" text-anchor="middle" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">i</text></svg>
:::

Les lettres A, B, M de la figure sont celles de l'exemple : u_AB est la tension de la bobine et u_BM celle du résistor R₀.

::: figure Le courant d'un dipôle RL soumis à un échelon : il part de 0 sans saut, monte en exponentielle (transitoire) et se stabilise à I₀ au bout d'environ 5τ (permanent)
<svg viewBox="0 0 340 242"><title>Courbe i(t) d'établissement du courant : montée exponentielle vers l'asymptote I₀, régime transitoire puis régime permanent</title><line x1="50" y1="190" x2="328" y2="190" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><line x1="50" y1="190" x2="50" y2="20" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><polygon points="332,190 324,186 324,194" fill="#0f172a"/><polygon points="50,16 46,24 54,24" fill="#0f172a"/><line x1="50" y1="50" x2="326" y2="50" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="5 4" stroke-linecap="round"/><polyline points="50,190 54,176.7 58,164.6 62,153.7 66,143.8 70,134.9 74,126.8 78,119.5 82,112.9 86,106.9 90,101.5 94,96.6 98,92.2 102,88.2 106,84.5 110,81.2 114,78.3 118,75.6 122,73.1 126,70.9 130,68.9 134,67.1 138,65.5 142,64 146,62.7 150,61.5 154,60.4 158,59.4 162,58.5 166,57.7 170,57 174,56.3 178,55.7 182,55.2 186,54.7 190,54.2 194,53.8 198,53.5 202,53.1 206,52.8 210,52.6 214,52.3 218,52.1 222,51.9 226,51.7 230,51.6 234,51.4 238,51.3 242,51.2 246,51 250,50.9 254,50.9 258,50.8 262,50.7 266,50.6 270,50.6 274,50.5 278,50.5 282,50.4 286,50.4 290,50.3 294,50.3 298,50.3 302,50.3 306,50.2 310,50.2 314,50.2 318,50.2 322,50.2" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"/><line x1="250" y1="190" x2="250" y2="50" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="3 3" stroke-linecap="round"/><text x="44" y="54" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">I₀</text><text x="44" y="204" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><text x="250" y="206" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">5τ</text><text x="60" y="16" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">i</text><text x="322" y="206" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">t</text><line x1="52" y1="220" x2="246" y2="220" stroke="#0f6e56" stroke-width="2" stroke-linecap="round"/><line x1="254" y1="220" x2="322" y2="220" stroke="#b45309" stroke-width="2" stroke-linecap="round"/><text x="151" y="234" text-anchor="middle" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">régime transitoire</text><text x="286" y="234" text-anchor="middle" font-size="12" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">permanent</text></svg>
:::

La courbe est celle du circuit ci-dessus avec E = 12 V, R = 60 Ω et L = 0,30 H : l'asymptote I₀ de la figure est la valeur E/R, et τ la constante de temps qui règle la montée.

::: exemple Établir i(t) puis lire la solution

1. Loi des mailles : u_AB + u_BM = E, car le générateur impose E entre A et M.
2. On remplace : u_AB = L di/dt + r i (notion précédente) et u_BM = R₀ i (loi d'Ohm), d'où L di/dt + (R₀ + r) i = E, soit di/dt + (R/L) i = E/L. On pose τ = L/R : di/dt + i/τ = E/L.
3. On cherche i = A e^(−αt) + B avec i(0) = 0, car la bobine interdit tout saut de courant : A + B = 0.
4. On reporte dans l'équation. Le facteur de e^(−αt) doit s'annuler pour tout t, donc α = 1/τ. Le terme constant donne B/τ = E/L, soit B = E/R, et A = −E/R.
5. Résultat : i(t) = (E/R)(1 − e^(−t/τ)). Numériquement, R = 60 Ω, I₀ = 12 / 60 = 0,20 A et τ = 0,30 / 60 = 5,0 ms.
6. Tension de la bobine : u_AB = L di/dt + r i = E e^(−t/τ) + r (E/R)(1 − e^(−t/τ)). À t = 0, u_AB = E = 12 V (i = 0, toute la tension est aux bornes de la bobine) ; pour t → ∞, u_AB = r I₀ = 10 × 0,20 = 2,0 V.

:::

::: piege
**Erreur : « en régime permanent, la tension aux bornes de la bobine est nulle ».** Elle l'est seulement si r = 0. Ici, r = 10 Ω et I₀ = 0,20 A : u_AB = r I₀ = 2,0 V (étape 6). L'erreur tente parce qu'on retient « le courant continu traverse une bobine comme un fil ». Le terme L di/dt est bien nul quand i est constant, mais le terme r i subsiste.
:::

::: propriete
**Les valeurs aux deux extrémités** — À t = 0 : i = 0 et u_AB = E. Pour t → ∞ : i = I₀ = E/R et u_AB = rE/R. Si r = 0 : u_AB = E e^(−t/τ) tend vers 0 et u_BM tend vers E. Le régime permanent est atteint, à 1 % près, au bout d'environ 5τ.
:::

::: verifie À toi : un autre dipôle RL
Un dipôle RL est formé d'un générateur de f.e.m. E = 10 V, d'une bobine (L = 0,12 H, r = 4,0 Ω) et d'un résistor R₀ = 36 Ω. Calculer I₀ et τ, puis la tension de la bobine à t = 0 et en régime permanent.

---

R = R₀ + r = 40 Ω, donc I₀ = E/R = 10 / 40 = 0,25 A et τ = L/R = 0,12 / 40 = 3,0 ms. À t = 0, le courant est nul : tout E est aux bornes de la bobine, u_AB = 10 V. En régime permanent, di/dt = 0, donc u_AB = r I₀ = 4,0 × 0,25 = 1,0 V.
:::

::: retenir
Un dipôle RL soumis à un échelon E a pour courant i(t) = (E/R)(1 − e^(−t/τ)) avec R = R₀ + r et τ = L/R : il part de 0 et tend vers I₀ = E/R.
:::

## 📉 La rupture du courant dans un dipôle RL

Le régime permanent est établi (I₀ = 0,20 A) et on ouvre K. Sans diode, le courant voudrait tomber à zéro d'un coup et la bobine refuserait : c'est l'étincelle.
Avec la diode D de la figure du circuit, le courant de la bobine a un chemin : bobine, résistor R₀, diode. Comment i évolue-t-il, et que devient la tension aux bornes de la bobine ?

::: definition
**Rupture du courant** — Après l'ouverture de K, l'intensité i ne s'annule pas brusquement : elle décroît de façon continue en exponentielle selon i(t) = (E/R) e^(−t/τ), avec R = R₀ + r et τ = L/R. Elle vérifie di/dt + i/τ = 0.
:::

::: figure À l'ouverture de K, l'intensité i reste continue et décroît en exponentielle, mais la tension u_AB de la bobine saute de +2,0 V à −10 V avant de tendre vers 0
<svg viewBox="0 0 340 240"><title>À l'ouverture de K : l'intensité i(t) décroît de façon continue en exponentielle, la tension u_AB saute de +2,0 V à −10 V puis tend vers 0</title><line x1="30" y1="100" x2="322" y2="100" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><line x1="30" y1="100" x2="30" y2="12" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><polygon points="326,100 318,96 318,104" fill="#0f172a"/><polygon points="30,8 26,16 34,16" fill="#0f172a"/><polyline points="30,30 94,30 94,30 98,36.7 102,42.7 106,48.1 110,53.1 114,57.5 118,61.6 122,65.2 126,68.5 130,71.5 134,74.2 138,76.7 142,78.9 146,80.9 150,82.7 154,84.4 158,85.9 162,87.2 166,88.4 170,89.5 174,90.5 178,91.4 182,92.2 186,93 190,93.6 194,94.3 198,94.8 202,95.3 206,95.7 210,96.1 214,96.5 218,96.8 222,97.1 226,97.4 230,97.7 234,97.9 238,98.1 242,98.3 246,98.4 250,98.6 254,98.7 258,98.8 262,99 266,99.1 270,99.1 274,99.2 278,99.3 282,99.4 286,99.4 290,99.5 294,99.5" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><line x1="94" y1="12" x2="94" y2="232" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="4 3" stroke-linecap="round"/><text x="24" y="34" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0,20</text><text x="36" y="14" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">i (A)</text><text x="94" y="114" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><text x="134" y="114" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">τ</text><text x="294" y="114" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">5τ</text><line x1="30" y1="160" x2="322" y2="160" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><line x1="30" y1="160" x2="30" y2="122" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><polygon points="326,160 318,156 318,164" fill="#0f172a"/><polygon points="30,118 26,126 34,126" fill="#0f172a"/><polyline points="30,148 94,148 94,220 94,220 98,214.3 102,209.1 106,204.4 110,200.2 114,196.4 118,192.9 122,189.8 126,187 130,184.4 134,182.1 138,180 142,178.1 146,176.4 150,174.8 154,173.4 158,172.1 162,171 166,169.9 170,169 174,168.1 178,167.3 182,166.6 186,166 190,165.4 194,164.9 198,164.5 202,164 206,163.6 210,163.3 214,163 218,162.7 222,162.4 226,162.2 230,162 234,161.8 238,161.6 242,161.5 246,161.3 250,161.2 254,161.1 258,161 262,160.9 266,160.8 270,160.7 274,160.7 278,160.6 282,160.5 286,160.5 290,160.4 294,160.4" fill="none" stroke="#b45309" stroke-width="2.8" stroke-linejoin="round" stroke-linecap="round"/><text x="36" y="126" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">u_AB (V)</text><text x="24" y="152" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">+2,0</text><text x="24" y="224" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−10</text></svg>
:::

Les deux courbes sont celles du dipôle de la section précédente (E = 12 V, r = 10 Ω, R₀ = 50 Ω, τ = 5,0 ms) après l'ouverture de K à t = 0.

::: exemple Rupture dans le dipôle E = 12 V, r = 10 Ω, R₀ = 50 Ω, L = 0,30 H

1. Après l'ouverture, plus de générateur : u_AB + u_BM = 0, la diode passante agissant comme un fil. Avec u_AB = L di/dt + r i et u_BM = R₀ i, on obtient L di/dt + R i = 0, soit di/dt + i/τ = 0.
2. On cherche i = A e^(−αt) avec i(0) = I₀ = E/R = 0,20 A, car la bobine empêche tout saut de courant : A = I₀. On reporte : α = 1/τ, donc i(t) = I₀ e^(−t/τ), avec τ = 5,0 ms.
3. Valeurs : i(τ) = 0,20 × e^(−1) ≈ 0,074 A et, à t = 3τ = 15 ms, i ≈ 0,20 × 0,050 = 0,010 A.
4. Tension : l'équation donne L di/dt = −R i, donc u_AB = L di/dt + r i = −R i + r i = −R₀ i = −R₀ I₀ e^(−t/τ). À t = 0⁺ : u_AB = −50 × 0,20 = −10 V.
5. Avant l'ouverture, u_AB = r I₀ = 2,0 V ; juste après, −10 V. La tension saute de −12 V, soit −E, alors que i n'a pas bougé.

:::

::: piege
**Erreur : « à l'ouverture de K, le courant s'annule aussitôt ».** C'est ce que ferait un résistor seul. Pour la bobine, i est **continu** : sa valeur juste après l'ouverture est égale à sa valeur juste avant (étape 2). L'erreur tente parce qu'on pense « circuit ouvert, donc plus de courant ». Ce qui saute à l'ouverture, c'est la tension u_AB (étape 5), pas l'intensité.
:::

::: propriete
**Continuité et saut** — L'intensité i dans la bobine est continue, car l'énergie ½ L i² ne peut pas changer brusquement : cela demanderait une puissance infinie. La tension u_AB, elle, est discontinue : elle passe de r I₀ à −R₀ I₀, soit un saut de −E. Cas limite : si r = 0, u_AB passe de 0 à −E. Après 5τ, le courant est quasiment nul.
:::

::: verifie À toi : une rupture à calculer
Dipôle RL en régime permanent : E = 6,0 V, R₀ = 24 Ω, r = 6,0 Ω, L = 0,15 H. On ouvre K (la diode conduit). Calculer u_AB juste après l'ouverture, puis i à t = 10 ms.

---

R = 30 Ω, I₀ = 6,0 / 30 = 0,20 A et τ = 0,15 / 30 = 5,0 ms. Juste après l'ouverture, i vaut encore I₀ et u_AB = −R₀ I₀ = −24 × 0,20 = −4,8 V. À t = 10 ms = 2τ, i = I₀ e^(−2) = 0,20 × 0,135 ≈ 0,027 A.
:::

::: retenir
À la rupture, i(t) = (E/R) e^(−t/τ) décroît sans saut, alors que la tension u_AB de la bobine saute de r I₀ à −R₀ I₀.
:::

## ⏱️ La constante de temps τ = L/R

Deux montages identiques, sauf que dans l'un on a doublé la résistance : le courant s'y installe plus vite. Dans un autre, on a doublé l'inductance : il s'installe plus lentement.
Quelle grandeur chiffre cette lenteur, et comment la lire sur une courbe ?

::: definition
**Constante de temps** — La constante de temps d'un dipôle RL est τ = L/R, en seconde (L en henry, R en ohm). Elle renseigne sur le retard avec lequel s'établit le régime permanent, ou avec lequel s'éteint le courant à la rupture. La durée pour atteindre une même fraction de la valeur finale est proportionnelle à τ, donc proportionnelle à L et inversement proportionnelle à R.
:::

::: figure Deux lectures de τ sur la courbe d'établissement : la tangente à l'origine (pointillés) coupe l'asymptote I₀ à l'abscisse τ, et le point d'ordonnée 0,63 I₀ a la même abscisse τ
<svg viewBox="0 0 340 215"><title>Courbe i(t) d'établissement avec la tangente à l'origine qui coupe l'asymptote I₀ en t = τ, et le point d'ordonnée 0,63 I₀ à la même abscisse</title><line x1="50" y1="190" x2="328" y2="190" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><line x1="50" y1="190" x2="50" y2="20" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><polygon points="332,190 324,186 324,194" fill="#0f172a"/><polygon points="50,16 46,24 54,24" fill="#0f172a"/><line x1="50" y1="50" x2="326" y2="50" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="5 4" stroke-linecap="round"/><line x1="50" y1="190" x2="90" y2="50" stroke="#b45309" stroke-width="2" stroke-dasharray="6 4" stroke-linecap="round"/><line x1="90" y1="50" x2="90" y2="190" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="3 3" stroke-linecap="round"/><line x1="50" y1="101.5" x2="90" y2="101.5" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="3 3" stroke-linecap="round"/><polyline points="50,190 54,176.7 58,164.6 62,153.7 66,143.8 70,134.9 74,126.8 78,119.5 82,112.9 86,106.9 90,101.5 94,96.6 98,92.2 102,88.2 106,84.5 110,81.2 114,78.3 118,75.6 122,73.1 126,70.9 130,68.9 134,67.1 138,65.5 142,64 146,62.7 150,61.5 154,60.4 158,59.4 162,58.5 166,57.7 170,57 174,56.3 178,55.7 182,55.2 186,54.7 190,54.2 194,53.8 198,53.5 202,53.1 206,52.8 210,52.6 214,52.3 218,52.1 222,51.9 226,51.7 230,51.6 234,51.4 238,51.3 242,51.2 246,51 250,50.9 254,50.9 258,50.8 262,50.7 266,50.6 270,50.6 274,50.5 278,50.5 282,50.4 286,50.4 290,50.3 294,50.3 298,50.3 302,50.3 306,50.2 310,50.2 314,50.2 318,50.2 322,50.2" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"/><circle cx="90" cy="50" r="3.5" fill="#b45309"/><circle cx="90" cy="101.5" r="3.5" fill="#0f6e56"/><text x="44" y="54" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">I₀</text><text x="44" y="105.5" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0,63 I₀</text><text x="90" y="206" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">τ</text><text x="60" y="16" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">i</text><text x="322" y="206" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">t</text><text x="100" y="120" text-anchor="start" font-size="12" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">tangente</text></svg>
:::

Sur la figure, la tangente à l'origine a pour pente I₀/τ : elle atteint I₀ au bout de la durée τ, et c'est aussi à cette abscisse que la courbe passe par 0,63 I₀.

::: exemple Lire τ, puis r et L, sur un enregistrement (E = 12 V, R₀ = 50 Ω, I₀ = 0,20 A)

1. Sur l'enregistrement de ce circuit (axe des temps gradué en ms, valeurs d'illustration), la tangente à l'origine coupe l'asymptote I₀ = 0,20 A à l'abscisse τ = 5,0 ms, comme sur la figure.
2. Contrôle par la seconde méthode : i(τ) = 0,63 × 0,20 = 0,126 A, ordonnée du point de la courbe d'abscisse 5,0 ms ✓.
3. La résistance totale vient de I₀ = E/R : R = 12 / 0,20 = 60 Ω, donc r = R − R₀ = 60 − 50 = 10 Ω.
4. On en tire L = τ R = 5,0 × 10⁻³ × 60 = 0,30 H. Les unités s'accordent : des ohms par des secondes donnent des henrys, et L/R a bien la dimension d'un temps.
5. Le régime permanent est atteint au bout d'environ 5τ = 25 ms.

:::

::: piege
**Erreur : croire que le courant atteint I₀ à t = τ.** À t = τ, i = 0,63 I₀ seulement (étape 2) ; il faut environ 5τ pour être à 1 % de I₀. L'erreur tente parce que la tangente rejoint l'asymptote à l'abscisse τ et qu'on confond la droite avec la courbe : la courbe, elle, passe sous la tangente.
:::

::: propriete
**Quatre façons d'obtenir τ** — Calcul direct : τ = L/R. Tangente à l'origine : à l'établissement elle coupe l'asymptote I₀ en τ, à la rupture elle coupe l'axe des temps en τ. Valeur de 63 % : à l'établissement i(τ) = 0,63 I₀. Valeur de 37 % : à la rupture i(τ) = 0,37 I₀. Doubler R divise τ par 2 (et I₀ aussi, puisque I₀ = E/R) ; doubler L double τ sans changer I₀.
:::

::: verifie À toi : doubler la résistance
Dans le dipôle de l'exemple (E = 12 V, R = 60 Ω, L = 0,30 H), on double la résistance totale. Calculer τ', I₀' et la durée du transitoire.

---

On a R' = 120 Ω, donc τ' = L/R' = 0,30 / 120 = 2,5 ms, soit la moitié de τ. Le courant final devient I₀' = 12 / 120 = 0,10 A, moitié de I₀ aussi. Le régime permanent s'installe en 5τ' = 12,5 ms, deux fois plus vite.
:::

::: retenir
La constante de temps τ = L/R chiffre la durée du transitoire : 63 % de I₀ atteints à τ à l'établissement, 37 % restants à τ à la rupture, régime permanent vers 5τ.
:::

## 🔌 L'alternateur et le transformateur

La lampe d'un vélo s'allume quand on pédale. Le gros transformateur d'un poste électrique, lui, ne sert à rien s'il est branché sur une pile. Les deux reposent sur l'induction.
Comment l'alternateur produit-il le courant, et pourquoi le transformateur exige-t-il une tension alternative ?

::: definition
**Alternateur et transformateur** — Un **alternateur** transforme de l'énergie mécanique en énergie électrique par induction : un inducteur (aimant en rotation) fait varier le champ magnétique à travers un induit (bobines). Dans l'alternateur d'une voiture, l'induit est fixe (stator) et l'inducteur, un aimant multipolaire, tourne (rotor) ; la fréquence est liée à la fréquence de rotation de l'inducteur. Un **transformateur** est un quadripôle (primaire et secondaire) qui permet d'abaisser ou d'élever une tension alternative.
:::

::: exemple Pourquoi un transformateur ne fonctionne qu'en alternatif

1. Primaire sous tension continue : après la mise sous tension, le courant du primaire est constant.
2. Un courant constant crée un champ magnétique constant, dans lequel baigne le secondaire.
3. Le champ ne varie pas : aucune induction, donc aucune tension au secondaire (hors l'instant de la fermeture).
4. Primaire sous tension alternative : le courant varie sans cesse, le champ aussi, et une f.e.m. induite apparaît au secondaire : c'est la condition de fonctionnement.

:::

::: piege
**Erreur : confondre inducteur et induit dans l'alternateur.** L'aimant qui tourne est l'**inducteur** (il impose la variation du champ) ; ce sont les bobines fixes du stator qui sont l'**induit** (elles fournissent le courant). L'erreur tente parce que l'aimant « produit » le champ et qu'on le prend pour la source du courant : la source du courant, c'est l'induit.
:::

::: propriete
**Rapidité et fréquence** — Plus l'inducteur tourne vite, plus le champ varie vite : la fréquence de la tension augmente avec la fréquence de rotation, et le courant induit est plus intense, puisque la variation est plus rapide. Cas limite : rotor à l'arrêt, champ constant, aucun courant induit.
:::

::: verifie À toi : un rotor deux fois plus rapide
Un alternateur de voiture tourne deux fois plus vite. Que deviennent la fréquence de la tension produite et l'intensité du courant induit ?

---

La fréquence est liée à la fréquence de rotation de l'inducteur : elle double. De plus, le champ varie plus vite, et un courant induit est d'autant plus intense que la variation est rapide : l'intensité augmente aussi.
:::

::: retenir
Un alternateur convertit de l'énergie mécanique en énergie électrique par induction ; un transformateur ne fonctionne qu'en alternatif, car un courant constant n'induit rien.
:::

> 🏆 Quête franchie, héros ! Tu sais lire Lenz sur un aimant, calculer e et u_AB, chiffrer l'énergie d'une bobine, tracer l'établissement et la rupture d'un dipôle RL et en tirer τ. Le prochain chapitre fait osciller tout cela.
