# 🎢 Les oscillations mécaniques forcées — quand le moteur impose sa cadence

> 💡 «Un pendule qu'on abandonne oscille à sa façon, puis s'arrête ; un pendule qu'on pousse en cadence oscille à la façon de celui qui le pousse, et, si la cadence est juste, il finit par se déchaîner.»

Au chapitre précédent, un pendule élastique oscillait librement : à sa période propre T₀ = 2π√(m/k), puis de plus en plus faiblement à cause des frottements. Place maintenant l'extrémité de son ressort sur un moteur à excentrique : les oscillations ne s'éteignent plus, et leur amplitude dépend de la fréquence du moteur jusqu'à devenir très grande pour une fréquence précise. Huit notions racontent cela : le régime forcé, l'équation différentielle et la vitesse, l'amplitude et l'impédance mécanique, la résonance d'élongation, la résonance de vitesse, l'influence de l'amortissement, la puissance moyenne, puis la vitesse critique d'un véhicule. On suppose acquis le pendule élastique libre et amorti (fréquence propre N₀, frottement visqueux f = −h·v) ainsi que le circuit RLC forcé du chapitre 4 (résonances d'intensité et de charge, impédance), dont on réutilise l'analogie.

## 🎛️ Les oscillations forcées : excitateur et résonateur

Écarte un palet de masse m = 0,200 kg attaché à un ressort de raideur k = 8,0 N/m sur un banc à coussin d'air, puis lâche-le : il oscille à sa fréquence propre N₀ et s'arrête peu à peu. Fixe maintenant l'autre bout du ressort sur un moteur qui le pousse et le tire sans cesse, à raison de 0,80 tour par seconde.
Le palet oscille-t-il à N₀ ou au rythme du moteur, et pendant combien de temps ?

::: definition
**Oscillations forcées** — Un dispositif qui apporte périodiquement de l'énergie au pendule élastique, ici le moteur et son excentrique, est l'**excitateur** ; le pendule (palet et ressort) est le **résonateur**. Après un bref régime transitoire, en **régime permanent**, le résonateur oscille de façon sinusoïdale **à la fréquence N de l'excitateur** : x(t) = X_m sin(2πNt + φ_x). Les oscillations libres, elles, se font à la fréquence propre N₀ = (1/2π)√(k/m) et s'éteignent.
:::

::: figure Le moteur à excentrique impose le mouvement du point B, extrémité du ressort : le moteur est l'excitateur, le système {ressort, palet S} est le résonateur, et x mesure la position du palet par rapport à O
<svg viewBox="0 0 340 174"><title>Pendule élastique horizontal sur banc à coussin d'air : un moteur à excentrique impose le mouvement de l'extrémité B du ressort, le palet S suit</title><line x1="20" y1="118" x2="320" y2="118" stroke="#94a3b8" stroke-width="2" stroke-linecap="round"/><circle cx="30" cy="123" r="1.6" fill="#94a3b8"/><circle cx="50" cy="123" r="1.6" fill="#94a3b8"/><circle cx="70" cy="123" r="1.6" fill="#94a3b8"/><circle cx="90" cy="123" r="1.6" fill="#94a3b8"/><circle cx="110" cy="123" r="1.6" fill="#94a3b8"/><circle cx="130" cy="123" r="1.6" fill="#94a3b8"/><circle cx="150" cy="123" r="1.6" fill="#94a3b8"/><circle cx="170" cy="123" r="1.6" fill="#94a3b8"/><circle cx="190" cy="123" r="1.6" fill="#94a3b8"/><circle cx="210" cy="123" r="1.6" fill="#94a3b8"/><circle cx="230" cy="123" r="1.6" fill="#94a3b8"/><circle cx="250" cy="123" r="1.6" fill="#94a3b8"/><circle cx="270" cy="123" r="1.6" fill="#94a3b8"/><circle cx="290" cy="123" r="1.6" fill="#94a3b8"/><circle cx="310" cy="123" r="1.6" fill="#94a3b8"/><circle cx="52" cy="70" r="26" fill="#ffffff" stroke="#0f172a" stroke-width="1.8"/><text x="52" y="66" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">M</text><circle cx="66" cy="78" r="4" fill="#0f6e56"/><line x1="66" y1="78" x2="118" y2="100" stroke="#0f6e56" stroke-width="2" stroke-linecap="round"/><circle cx="118" cy="100" r="3.5" fill="#0f172a"/><text x="118" y="92" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">B</text><polyline points="118,100 132,91 144,109 156,91 168,109 180,91 192,109 204,91 216,109 226,100" fill="none" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round"/><rect x="226" y="84" width="40" height="32" fill="#ffffff" stroke="#0f172a" stroke-width="1.8"/><text x="246" y="104" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">S</text><line x1="246" y1="56" x2="246" y2="82" stroke="#0f172a" stroke-width="1.2" stroke-dasharray="3 3" stroke-linecap="round"/><line x1="246" y1="56" x2="306" y2="56" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><polygon points="312,56 304,52 304,60" fill="#0f172a"/><text x="312" y="52" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x</text><text x="246" y="48" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">O</text><line x1="24" y1="148" x2="132" y2="148" stroke="#0f6e56" stroke-width="2" stroke-linecap="round"/><line x1="24" y1="142" x2="24" y2="148" stroke="#0f6e56" stroke-width="2" stroke-linecap="round"/><line x1="132" y1="142" x2="132" y2="148" stroke="#0f6e56" stroke-width="2" stroke-linecap="round"/><text x="78" y="166" text-anchor="middle" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">excitateur</text><line x1="148" y1="148" x2="270" y2="148" stroke="#b45309" stroke-width="2" stroke-linecap="round"/><line x1="148" y1="142" x2="148" y2="148" stroke="#b45309" stroke-width="2" stroke-linecap="round"/><line x1="270" y1="142" x2="270" y2="148" stroke="#b45309" stroke-width="2" stroke-linecap="round"/><text x="209" y="166" text-anchor="middle" font-size="12" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">résonateur</text></svg>
:::

Sur la figure, le point vert est l'excentrique : en tournant, il pousse et tire B, donc le ressort ; c'est ce mouvement imposé qui entretient l'oscillation du palet.

::: figure Enregistrement x(t) du palet en régime permanent, à partir d'un instant pris pour t = 0 : amplitude 2,0 cm, période T = 1,25 s ; le point orange marque x(0) = −1,0 cm, avec x croissant
<svg viewBox="0 0 340 200"><title>Enregistrement x(t) en régime permanent : sinusoïde d'amplitude 2 cm, de période 1,25 s, qui vaut −1 cm à t = 0 en croissant</title><line x1="54" y1="163.7" x2="322" y2="163.7" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/><line x1="54" y1="132.8" x2="322" y2="132.8" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/><line x1="54" y1="71.2" x2="322" y2="71.2" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/><line x1="54" y1="40.3" x2="322" y2="40.3" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/><line x1="97.3" y1="28" x2="97.3" y2="176" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/><line x1="140.7" y1="28" x2="140.7" y2="176" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/><line x1="184" y1="28" x2="184" y2="176" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/><line x1="227.3" y1="28" x2="227.3" y2="176" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/><line x1="270.7" y1="28" x2="270.7" y2="176" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/><line x1="314" y1="28" x2="314" y2="176" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/><line x1="54" y1="102" x2="324" y2="102" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><polygon points="330,102 322,98 322,106" fill="#0f172a"/><line x1="54" y1="182" x2="54" y2="22" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><polygon points="54,16 50,24 58,24" fill="#0f172a"/><polyline points="54,132.8 55.1,129.4 56.2,125.9 57.2,122.3 58.3,118.6 59.4,114.8 60.5,111 61.6,107.2 62.7,103.3 63.8,99.4 64.8,95.6 65.9,91.7 67,87.9 68.1,84.2 69.2,80.5 70.2,76.9 71.3,73.4 72.4,70.1 73.5,66.8 74.6,63.7 75.7,60.7 76.8,57.9 77.8,55.3 78.9,52.9 80,50.6 81.1,48.6 82.2,46.8 83.2,45.2 84.3,43.8 85.4,42.6 86.5,41.7 87.6,41 88.7,40.5 89.8,40.3 90.8,40.4 91.9,40.7 93,41.2 94.1,42 95.2,43 96.2,44.2 97.3,45.7 98.4,47.4 99.5,49.3 100.6,51.4 101.7,53.7 102.8,56.2 103.8,58.9 104.9,61.7 106,64.7 107.1,67.9 108.2,71.2 109.2,74.6 110.3,78.1 111.4,81.7 112.5,85.4 113.6,89.2 114.7,93 115.8,96.8 116.8,100.7 117.9,104.6 119,108.4 120.1,112.3 121.2,116.1 122.2,119.8 123.3,123.5 124.4,127.1 125.5,130.6 126.6,133.9 127.7,137.2 128.8,140.3 129.8,143.3 130.9,146.1 132,148.7 133.1,151.1 134.2,153.4 135.2,155.4 136.3,157.2 137.4,158.8 138.5,160.2 139.6,161.4 140.7,162.3 141.8,163 142.8,163.5 143.9,163.7 145,163.6 146.1,163.3 147.2,162.8 148.2,162 149.3,161 150.4,159.8 151.5,158.3 152.6,156.6 153.7,154.7 154.8,152.6 155.8,150.3 156.9,147.8 158,145.1 159.1,142.3 160.2,139.3 161.2,136.1 162.3,132.8 163.4,129.4 164.5,125.9 165.6,122.3 166.7,118.6 167.8,114.8 168.8,111 169.9,107.2 171,103.3 172.1,99.4 173.2,95.6 174.2,91.7 175.3,87.9 176.4,84.2 177.5,80.5 178.6,76.9 179.7,73.4 180.8,70.1 181.8,66.8 182.9,63.7 184,60.7 185.1,57.9 186.2,55.3 187.3,52.9 188.3,50.6 189.4,48.6 190.5,46.8 191.6,45.2 192.7,43.8 193.8,42.6 194.8,41.7 195.9,41 197,40.5 198.1,40.3 199.2,40.4 200.2,40.7 201.3,41.2 202.4,42 203.5,43 204.6,44.2 205.7,45.7 206.8,47.4 207.8,49.3 208.9,51.4 210,53.7 211.1,56.2 212.2,58.9 213.2,61.7 214.3,64.7 215.4,67.9 216.5,71.2 217.6,74.6 218.7,78.1 219.8,81.7 220.8,85.4 221.9,89.2 223,93 224.1,96.8 225.2,100.7 226.2,104.6 227.3,108.4 228.4,112.3 229.5,116.1 230.6,119.8 231.7,123.5 232.8,127.1 233.8,130.6 234.9,133.9 236,137.2 237.1,140.3 238.2,143.3 239.3,146.1 240.3,148.7 241.4,151.1 242.5,153.4 243.6,155.4 244.7,157.2 245.8,158.8 246.8,160.2 247.9,161.4 249,162.3 250.1,163 251.2,163.5 252.3,163.7 253.3,163.6 254.4,163.3 255.5,162.8 256.6,162 257.7,161 258.8,159.8 259.8,158.3 260.9,156.6 262,154.7 263.1,152.6 264.2,150.3 265.2,147.8 266.3,145.1 267.4,142.3 268.5,139.3 269.6,136.1 270.7,132.8 271.8,129.4 272.8,125.9 273.9,122.3 275,118.6 276.1,114.8 277.2,111 278.2,107.2 279.3,103.3 280.4,99.4 281.5,95.6 282.6,91.7 283.7,87.9 284.8,84.2 285.8,80.5 286.9,76.9 288,73.4 289.1,70.1 290.2,66.8 291.2,63.7 292.3,60.7 293.4,57.9 294.5,55.3 295.6,52.9 296.7,50.6 297.8,48.6 298.8,46.8 299.9,45.2 301,43.8 302.1,42.6 303.2,41.7 304.2,41 305.3,40.5 306.4,40.3 307.5,40.4 308.6,40.7 309.7,41.2 310.8,42 311.8,43 312.9,44.2 314,45.7" fill="none" stroke="#1d4ed8" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"/><line x1="51" y1="163.7" x2="54" y2="163.7" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><text x="47" y="167.7" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−2</text><line x1="51" y1="132.8" x2="54" y2="132.8" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><text x="47" y="136.8" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−1</text><line x1="51" y1="102" x2="54" y2="102" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><line x1="51" y1="71.2" x2="54" y2="71.2" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><text x="47" y="75.2" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">+1</text><line x1="51" y1="40.3" x2="54" y2="40.3" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><text x="47" y="44.3" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">+2</text><text x="47" y="118" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><line x1="97.3" y1="99" x2="97.3" y2="105" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><text x="97.3" y="119" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0,5</text><line x1="140.7" y1="99" x2="140.7" y2="105" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><text x="140.7" y="119" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><line x1="184" y1="99" x2="184" y2="105" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><text x="184" y="119" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1,5</text><line x1="227.3" y1="99" x2="227.3" y2="105" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><text x="227.3" y="119" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><line x1="270.7" y1="99" x2="270.7" y2="105" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><text x="270.7" y="119" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2,5</text><line x1="314" y1="99" x2="314" y2="105" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><text x="314" y="119" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">3</text><text x="326" y="135" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">t (s)</text><text x="62" y="20" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x (cm)</text><circle cx="54" cy="132.8" r="4" fill="#b45309"/><line x1="90.1" y1="30.3" x2="198.4" y2="30.3" stroke="#0f6e56" stroke-width="1.8" stroke-linecap="round"/><line x1="90.1" y1="26.3" x2="90.1" y2="34.3" stroke="#0f6e56" stroke-width="1.8" stroke-linecap="round"/><line x1="198.4" y1="26.3" x2="198.4" y2="34.3" stroke="#0f6e56" stroke-width="1.8" stroke-linecap="round"/><text x="144.3" y="24.3" text-anchor="middle" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">T</text></svg>
:::

Sur la figure, l'amplitude X_m se lit de l'axe t à une crête, la période T entre deux crêtes consécutives, et la phase initiale φ_x se déduit de la valeur de x à t = 0.

::: exemple Lire l'enregistrement et écrire x(t) (m = 0,200 kg ; k = 8,0 N/m ; moteur à 0,80 tr/s)

1. Deux crêtes consécutives sont distantes de 1,25 s, donc T = 1,25 s et N = 1/T = 0,80 Hz : c'est la fréquence du moteur, 0,80 tr/s.
2. N₀ = (1/2π)√(k/m) = (1/2π)√(8,0/0,200) = 6,32/6,28 ≈ 1,0 Hz. Comme N ≠ N₀, le palet n'oscille pas librement : ce sont des oscillations forcées.
3. L'amplitude se lit de l'axe à la crête : X_m = 2,0 cm = 2,0 × 10⁻² m.
4. À t = 0, x = X_m sin φ_x = −1,0 cm, donc sin φ_x = −1,0/2,0 = −1/2 : φ_x = −π/6 ou −5π/6. La courbe est croissante à t = 0 (cos φ_x > 0), donc φ_x = −π/6 rad.
5. ω = 2πN = 1,6π ≈ 5,03 rad/s, d'où x(t) = 2,0 × 10⁻² sin(5,03 t − π/6), x en mètre.

:::

::: piege
**Erreur : croire que le palet oscille à sa fréquence propre N₀.** L'enregistrement donne N = 0,80 Hz (étape 1), alors que N₀ ≈ 1,0 Hz (étape 2). L'erreur tente parce qu'un pendule abandonné à lui-même oscille à N₀. Mais en régime forcé la fréquence est celle de l'excitateur : N₀ n'intervient plus que dans l'amplitude.
:::

::: propriete
**Ce qui reste vrai** — En régime permanent, x(t) et v(t) ont la fréquence N de l'excitateur, quels que soient m, k et les frottements ; seuls l'amplitude X_m et la phase φ_x dépendent du pendule. Cas limite : si N est égale à N₀, les oscillations restent forcées, et c'est précisément la situation où l'amplitude devient la plus grande (notions 4 et 5).
:::

::: verifie À toi : un autre enregistrement
Avec le même pendule, le moteur est réglé sur une autre fréquence. L'enregistrement montre une sinusoïde qui coupe l'axe t vers le haut à t = 0, d'amplitude 2,5 cm, avec quatre oscillations complètes en 2,0 s. Donner N, la phase φ_x et x(t) ; les oscillations sont-elles forcées ?

---

Quatre périodes en 2,0 s donnent T = 0,50 s, donc N = 2,0 Hz. La courbe part de 0 en croissant : sin φ_x = 0 et cos φ_x > 0, donc φ_x = 0. Avec ω = 2πN = 4π rad/s, x(t) = 2,5 × 10⁻² sin(4πt). N = 2,0 Hz est différente de N₀ ≈ 1,0 Hz et égale à la fréquence du moteur : les oscillations sont forcées.
:::

::: retenir
Le moteur (excitateur) impose sa fréquence N au pendule (résonateur) : en régime permanent x = X_m sin(2πNt + φ_x), à la fréquence N et non à N₀.
:::

## 🧮 L'équation différentielle et la vitesse

Au chapitre 4, le circuit RLC série forcé obéissait à L·q″ + R·q′ + q/C = u(t). Un pendule amorti possède, lui aussi, une inertie (la masse m), des frottements (h) et un rappel (k), et un excitateur le pousse.
Peut-on écrire l'équation de x(t) en recopiant celle du circuit, sans repartir de la mécanique ?

::: definition
**Équation du pendule forcé** — L'analogie électrique-mécanique associe q ↔ x, i ↔ v = dx/dt, L ↔ m, R ↔ h, 1/C ↔ k et u ↔ F. La force excitatrice a pour valeur algébrique F = F_m sin ωt, avec ω = 2πN. L'équation du circuit devient, en x puis en v :

$$ m·d²x/dt² + h·dx/dt + k·x = F_m sin ωt $$

$$ m·dv/dt + h·v + k·∫v dt = F_m sin ωt $$

Sa solution de régime permanent est sinusoïdale à la pulsation ω : x = X_m sin(ωt + φ_x) et v = V_m sin(ωt + φ_v), avec V_m = ω·X_m et φ_v = φ_x + π/2.
:::

::: exemple Écrire l'équation, la tester à un instant, passer de x à v (m = 0,200 kg ; k = 8,0 N/m ; h = 0,80 kg/s ; F_m = 0,10 N)

1. On remplace dans l'équation du circuit L par m, R par h et 1/C par k : le terme d'inertie, le terme de frottement et le terme de rappel du pendule prennent la place de ceux du circuit.
2. Avec les valeurs numériques : 0,200·x″ + 0,80·x′ + 8,0·x = F, où F est la valeur de la force excitatrice à l'instant considéré.
3. À un instant on mesure x = +1,2 cm, v = +0,080 m/s et a = x″ = −0,30 m/s². Alors F = 0,200 × (−0,30) + 0,80 × 0,080 + 8,0 × 0,012 = −0,060 + 0,064 + 0,096 = 0,10 N : c'est F_m, la force est à son maximum.
4. Si x = X_m sin(ωt + φ_x), alors v = dx/dt = ω·X_m cos(ωt + φ_x) = ω·X_m sin(ωt + φ_x + π/2) : la dérivée d'un sinus est un sinus avancé de π/2.
5. Pour X_m = 2,0 cm et ω = 5,0 rad/s, V_m = ω·X_m = 5,0 × 2,0 × 10⁻² = 0,10 m/s, et v est en avance de π/2 sur x.

:::

::: piege
**Erreur : écrire un second membre nul**, m·x″ + h·x′ + k·x = 0, comme pour les oscillations amorties du chapitre précédent. Dans l'exemple, la somme des trois termes vaut 0,10 N et non 0 (étape 3). L'erreur tente parce que l'équation ressemble à celle des oscillations libres amorties. Mais l'excitateur apporte la force F_m sin ωt : c'est elle qui empêche les oscillations de s'éteindre.
:::

::: propriete
**Ce qui reste vrai** — Les équations en x et en v se déduisent l'une de l'autre, puisque v = dx/dt. Dans les deux, la pulsation de la solution est celle de l'excitateur, et non ω₀ = √(k/m) ; V_m = ω·X_m et v avance de π/2 sur x. Cas limite : sans excitateur (F = 0) on retrouve l'équation des oscillations libres amorties, dont la solution s'éteint.
:::

::: verifie À toi : un autre instant
Même pendule. À un instant, x = −2,0 cm, v = 0 et a = +0,40 m/s². Calculer la valeur F de la force excitatrice.

---

Avec v = 0, le terme de frottement h·v est nul. F = m·a + h·v + k·x = 0,200 × 0,40 + 0 + 8,0 × (−0,020) = 0,080 − 0,16 = −0,080 N : le signe négatif signifie que la force pousse alors dans le sens des x négatifs.
:::

::: retenir
m·x″ + h·x′ + k·x = F_m sin ωt, soit m·dv/dt + h·v + k·∫v dt = F_m sin ωt ; v = V_m sin(ωt + φ_v) avec V_m = ω·X_m et φ_v = φ_x + π/2.
:::

## 📏 L'amplitude X_m et l'impédance mécanique

On garde le pendule (m = 0,200 kg ; k = 8,0 N/m), mais le palet porte maintenant une plaque qui lui donne un frottement visqueux h = 0,80 kg/s, et le moteur exerce une force d'amplitude F_m = 0,10 N. Si tu règles le moteur plus vite ou plus lentement, l'amplitude des oscillations change.
De combien dépend-elle de la fréquence réglée, et peut-on la calculer d'avance ?

::: definition
**Amplitude et impédance mécanique** — Par analogie avec Q_m = U_m/√(R²ω² + (Lω² − 1/C)²), l'amplitude des oscillations et celle de la vitesse sont, avec ω = 2πN :

$$ X_m = F_m / √(h²ω² + (mω² − k)²) $$

$$ V_m = ω·X_m = F_m / Z   avec   Z = √(h² + (mω − k/ω)²) $$

Z = F_m/V_m est l'**impédance mécanique** du pendule, en kg/s comme h. En fonction de N : X_m = F_m / √(4π²h²N² + (k − 4π²mN²)²).
:::

Pour ce pendule, le calcul donne les amplitudes suivantes (valeurs calculées avec la formule de X_m) :

| N (Hz) | 0 | 0,5 | 0,8 | 1,0 | 1,5 | 2,0 |
| --- | --- | --- | --- | --- | --- | --- |
| X_m (cm) | 1,25 | 1,53 | 2,01 | 1,99 | 0,81 | 0,39 |

Dans le tableau, X_m monte de 1,25 cm à environ 2 cm quand N s'approche de N₀ ≈ 1,0 Hz, puis retombe : la formule rend compte de cette variation avec N.

::: exemple Calculer X_m, V_m et Z pour ω = 5,0 rad/s (soit N ≈ 0,80 Hz)

1. h·ω = 0,80 × 5,0 = 4,0 N/m et m·ω² = 0,200 × 25 = 5,0 N/m, donc m·ω² − k = 5,0 − 8,0 = −3,0 N/m.
2. X_m = F_m / √(4,0² + (−3,0)²) = 0,10 / √25 = 0,10 / 5,0 = 2,0 × 10⁻² m : le carré rend le signe de −3,0 sans importance.
3. V_m = ω·X_m = 5,0 × 2,0 × 10⁻² = 0,10 m/s, puisque la vitesse est la dérivée de x.
4. Z = F_m / V_m = 0,10 / 0,10 = 1,0 kg/s. Contrôle avec la formule : √(h² + (mω − k/ω)²) = √(0,64 + (1,0 − 1,6)²) = √1,00 = 1,0 kg/s ✓.

:::

::: piege
**Erreur : mettre N à la place de ω dans la formule en ω.** Avec N = 0,80 au lieu de ω = 5,0, on trouve X_m = 0,10 / √(0,64² + (0,128 − 8,0)²) = 1,3 cm, au lieu de 2,0 cm (étape 2). L'erreur tente parce que N est la grandeur réglée sur le moteur. Mais les formules en h²ω² et mω² demandent la pulsation ω = 2πN ; la forme en N contient les facteurs 4π² pour cette raison.
:::

::: propriete
**Ce qui reste vrai** — X_m est proportionnelle à F_m et diminue quand h augmente. Pour N tendant vers 0, X_m tend vers F_m/k (ici 1,25 cm) : la force agit comme une force constante qui allonge le ressort. Pour N très grand, X_m tend vers 0 : l'inertie empêche le palet de suivre. Cas limite : sans frottement (h = 0), le dénominateur s'annule pour mω² = k, et X_m deviendrait infinie.
:::

::: verifie À toi : un autre pendule
m = 0,100 kg, k = 4,0 N/m, h = 0,80 kg/s, F_m = 0,50 N, ω = 10 rad/s. Calculer X_m, V_m et Z.

---

h·ω = 8,0 N/m et m·ω² − k = 10 − 4,0 = 6,0 N/m, donc X_m = 0,50 / √(8,0² + 6,0²) = 0,50 / 10 = 5,0 × 10⁻² m = 5,0 cm. Ensuite V_m = ω·X_m = 10 × 0,050 = 0,50 m/s et Z = F_m / V_m = 0,50 / 0,50 = 1,0 kg/s.
:::

::: retenir
X_m = F_m / √(h²ω² + (mω² − k)²) et V_m = F_m / Z avec Z = √(h² + (mω − k/ω)²) en kg/s, où ω = 2πN.
:::

## 📈 La résonance d'élongation

Fais croître la fréquence du moteur de 0 à 2 Hz. À très basse fréquence, le ressort est tiré lentement et X_m ≈ F_m/k = 1,25 cm. Puis l'amplitude grandit, passe par un maximum, et retombe.
Où se trouve ce maximum : à la fréquence propre N₀, comme on pourrait l'attendre, ou ailleurs ?

::: definition
**Résonance d'élongation** — L'amplitude X_m passe par un maximum pour une fréquence N_r de l'excitateur, appelée **fréquence de résonance**, légèrement inférieure à la fréquence propre N₀ = (1/2π)√(k/m) :

$$ N_r = √(N₀² − h²/(8π²m²)) $$

Cette résonance n'existe que si h² < 2mk ; sinon le radicande n'est pas positif et X_m décroît dès N = 0.
:::

::: figure Courbe X_m(N) pour m = 0,200 kg, k = 8,0 N/m, h = 0,80 kg/s et F_m = 0,10 N : le maximum (point orange) est à N_r = 0,90 Hz, à gauche de N₀ = 1,01 Hz (pointillés noirs) ; la courbe part de F_m/k = 1,25 cm
<svg viewBox="0 0 340 226"><title>Courbe de résonance d'élongation Xm(N) pour m = 0,200 kg, k = 8,0 N/m, h = 0,80 kg/s et Fm = 0,10 N : le maximum, à Nr = 0,90 Hz, est un peu à gauche de N0 = 1,01 Hz</title><line x1="54" y1="158.8" x2="320" y2="158.8" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/><line x1="54" y1="127.6" x2="320" y2="127.6" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/><line x1="54" y1="96.4" x2="320" y2="96.4" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/><line x1="54" y1="65.2" x2="320" y2="65.2" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/><line x1="54" y1="34" x2="320" y2="34" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/><line x1="54" y1="190" x2="322" y2="190" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><line x1="54" y1="190" x2="54" y2="30" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><polygon points="328,190 320,186 320,194" fill="#0f172a"/><polygon points="54,24 50,32 58,32" fill="#0f172a"/><line x1="51" y1="158.8" x2="54" y2="158.8" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><text x="48" y="162.8" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0,5</text><line x1="51" y1="127.6" x2="54" y2="127.6" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><text x="48" y="131.6" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><line x1="51" y1="96.4" x2="54" y2="96.4" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><text x="48" y="100.4" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1,5</text><line x1="51" y1="65.2" x2="54" y2="65.2" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><text x="48" y="69.2" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><line x1="51" y1="34" x2="54" y2="34" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><text x="48" y="38" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2,5</text><line x1="54" y1="190" x2="54" y2="193" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><text x="54" y="205" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><line x1="120.5" y1="190" x2="120.5" y2="193" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><text x="120.5" y="205" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0,5</text><line x1="187" y1="190" x2="187" y2="193" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><text x="187" y="205" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><line x1="253.5" y1="190" x2="253.5" y2="193" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><text x="253.5" y="205" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1,5</text><line x1="320" y1="190" x2="320" y2="193" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><text x="320" y="205" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><text x="324" y="220" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">N (Hz)</text><text x="62" y="22" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"></text><line x1="187.9" y1="190" x2="187.9" y2="40" stroke="#0f172a" stroke-width="1.4" stroke-dasharray="5 4" stroke-linecap="round"/><polyline points="54,112 54.7,112 55.3,112 56,112 56.7,112 57.3,112 58,111.9 58.7,111.9 59.3,111.9 60,111.9 60.6,111.8 61.3,111.8 62,111.8 62.6,111.7 63.3,111.7 64,111.7 64.6,111.6 65.3,111.6 66,111.5 66.6,111.4 67.3,111.4 68,111.3 68.6,111.2 69.3,111.2 70,111.1 70.6,111 71.3,110.9 72,110.9 72.6,110.8 73.3,110.7 74,110.6 74.6,110.5 75.3,110.4 75.9,110.3 76.6,110.2 77.3,110.1 77.9,110 78.6,109.9 79.3,109.7 79.9,109.6 80.6,109.5 81.3,109.3 81.9,109.2 82.6,109.1 83.3,108.9 83.9,108.8 84.6,108.6 85.3,108.5 85.9,108.3 86.6,108.2 87.2,108 87.9,107.8 88.6,107.7 89.2,107.5 89.9,107.3 90.6,107.1 91.2,107 91.9,106.8 92.6,106.6 93.2,106.4 93.9,106.2 94.6,106 95.2,105.8 95.9,105.5 96.6,105.3 97.2,105.1 97.9,104.9 98.6,104.6 99.2,104.4 99.9,104.2 100.5,103.9 101.2,103.7 101.9,103.4 102.5,103.2 103.2,102.9 103.9,102.6 104.5,102.4 105.2,102.1 105.9,101.8 106.5,101.5 107.2,101.2 107.9,100.9 108.5,100.6 109.2,100.3 109.9,100 110.5,99.7 111.2,99.4 111.9,99.1 112.5,98.8 113.2,98.4 113.8,98.1 114.5,97.7 115.2,97.4 115.8,97 116.5,96.7 117.2,96.3 117.8,96 118.5,95.6 119.2,95.2 119.8,94.8 120.5,94.4 121.2,94 121.8,93.6 122.5,93.2 123.2,92.8 123.8,92.4 124.5,92 125.2,91.6 125.8,91.1 126.5,90.7 127.2,90.2 127.8,89.8 128.5,89.4 129.1,88.9 129.8,88.4 130.5,88 131.1,87.5 131.8,87 132.5,86.5 133.1,86 133.8,85.6 134.5,85.1 135.1,84.6 135.8,84.1 136.5,83.6 137.1,83 137.8,82.5 138.5,82 139.1,81.5 139.8,81 140.4,80.4 141.1,79.9 141.8,79.4 142.4,78.8 143.1,78.3 143.8,77.7 144.4,77.2 145.1,76.6 145.8,76.1 146.4,75.6 147.1,75 147.8,74.5 148.4,73.9 149.1,73.4 149.8,72.8 150.4,72.3 151.1,71.8 151.8,71.2 152.4,70.7 153.1,70.2 153.8,69.6 154.4,69.1 155.1,68.6 155.7,68.1 156.4,67.6 157.1,67.1 157.7,66.6 158.4,66.2 159.1,65.7 159.7,65.3 160.4,64.8 161.1,64.4 161.7,64 162.4,63.6 163.1,63.2 163.7,62.9 164.4,62.5 165.1,62.2 165.7,61.9 166.4,61.6 167.1,61.3 167.7,61.1 168.4,60.9 169,60.7 169.7,60.5 170.4,60.4 171,60.2 171.7,60.1 172.4,60.1 173,60 173.7,60 174.4,60 175,60.1 175.7,60.1 176.4,60.2 177,60.4 177.7,60.5 178.4,60.7 179,60.9 179.7,61.2 180.3,61.5 181,61.8 181.7,62.1 182.3,62.5 183,62.9 183.7,63.3 184.3,63.8 185,64.3 185.7,64.8 186.3,65.3 187,65.9 187.7,66.5 188.3,67.1 189,67.7 189.7,68.4 190.3,69.1 191,69.8 191.7,70.5 192.3,71.3 193,72 193.7,72.8 194.3,73.6 195,74.4 195.6,75.2 196.3,76.1 197,76.9 197.6,77.8 198.3,78.7 199,79.6 199.6,80.5 200.3,81.4 201,82.3 201.6,83.2 202.3,84.1 203,85 203.6,85.9 204.3,86.9 205,87.8 205.6,88.7 206.3,89.6 206.9,90.6 207.6,91.5 208.3,92.4 208.9,93.3 209.6,94.3 210.3,95.2 210.9,96.1 211.6,97 212.3,97.9 212.9,98.8 213.6,99.7 214.3,100.6 214.9,101.5 215.6,102.3 216.3,103.2 216.9,104.1 217.6,104.9 218.3,105.8 218.9,106.6 219.6,107.4 220.2,108.3 220.9,109.1 221.6,109.9 222.2,110.7 222.9,111.5 223.6,112.3 224.2,113.1 224.9,113.8 225.6,114.6 226.2,115.3 226.9,116.1 227.6,116.8 228.2,117.5 228.9,118.3 229.6,119 230.2,119.7 230.9,120.4 231.6,121 232.2,121.7 232.9,122.4 233.6,123.1 234.2,123.7 234.9,124.3 235.5,125 236.2,125.6 236.9,126.2 237.5,126.8 238.2,127.5 238.9,128 239.5,128.6 240.2,129.2 240.9,129.8 241.5,130.4 242.2,130.9 242.9,131.5 243.5,132 244.2,132.6 244.9,133.1 245.5,133.6 246.2,134.1 246.8,134.6 247.5,135.2 248.2,135.7 248.8,136.1 249.5,136.6 250.2,137.1 250.8,137.6 251.5,138.1 252.2,138.5 252.8,139 253.5,139.4 254.2,139.9 254.8,140.3 255.5,140.7 256.2,141.2 256.8,141.6 257.5,142 258.2,142.4 258.8,142.8 259.5,143.2 260.1,143.6 260.8,144 261.5,144.4 262.1,144.8 262.8,145.2 263.5,145.5 264.1,145.9 264.8,146.3 265.5,146.6 266.1,147 266.8,147.3 267.5,147.7 268.1,148 268.8,148.4 269.5,148.7 270.1,149 270.8,149.3 271.5,149.7 272.1,150 272.8,150.3 273.4,150.6 274.1,150.9 274.8,151.2 275.4,151.5 276.1,151.8 276.8,152.1 277.4,152.4 278.1,152.7 278.8,153 279.4,153.2 280.1,153.5 280.8,153.8 281.4,154.1 282.1,154.3 282.8,154.6 283.4,154.9 284.1,155.1 284.8,155.4 285.4,155.6 286.1,155.9 286.8,156.1 287.4,156.4 288.1,156.6 288.7,156.8 289.4,157.1 290.1,157.3 290.7,157.5 291.4,157.8 292.1,158 292.7,158.2 293.4,158.4 294.1,158.7 294.7,158.9 295.4,159.1 296.1,159.3 296.7,159.5 297.4,159.7 298.1,159.9 298.7,160.1 299.4,160.3 300.1,160.5 300.7,160.7 301.4,160.9 302,161.1 302.7,161.3 303.4,161.5 304,161.7 304.7,161.9 305.4,162.1 306,162.2 306.7,162.4 307.4,162.6 308,162.8 308.7,162.9 309.4,163.1 310,163.3 310.7,163.5 311.4,163.6 312,163.8 312.7,164 313.3,164.1 314,164.3 314.7,164.4 315.3,164.6 316,164.8 316.7,164.9 317.3,165.1 318,165.2 318.7,165.4 319.3,165.5 320,165.7" fill="none" stroke="#1d4ed8" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"/><line x1="54" y1="112" x2="320" y2="112" stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="2 3" stroke-linecap="round"/><text x="320" y="107" text-anchor="end" font-size="10" font-weight="700" fill="#64748b" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">F<tspan dy="3" font-size="8">m</tspan><tspan dy="-3">/k = 1,25 cm</tspan></text><line x1="173.7" y1="190" x2="173.7" y2="60" stroke="#b45309" stroke-width="1.4" stroke-dasharray="2 3" stroke-linecap="round"/><circle cx="173.7" cy="60" r="4.5" fill="#b45309"/><text x="191.9" y="38" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">N<tspan dy="3" font-size="9">0</tspan></text><text x="167.7" y="218" text-anchor="end" font-size="12" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">N<tspan dy="3" font-size="9">r</tspan></text><text x="62" y="22" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">X<tspan dy="3" font-size="9">m</tspan><tspan dy="-3"> (cm)</tspan></text></svg>
:::

Sur la figure, le point orange est le maximum de la courbe ; sa position N_r est celle donnée par la formule, et la droite en pointillés repère N₀.

::: exemple Chercher N_r et comparer X_m en N_r et en N₀ (m = 0,200 kg ; k = 8,0 N/m ; h = 0,80 kg/s ; F_m = 0,10 N)

1. Condition : h² = 0,64 est inférieur à 2mk = 2 × 0,200 × 8,0 = 3,2, donc la résonance d'élongation existe.
2. N₀ = (1/2π)√(k/m) = 6,325/6,283 = 1,007 Hz, d'où N₀² = 1,013 Hz².
3. h²/(8π²m²) = 0,64 / (78,96 × 0,0400) = 0,203 Hz², donc N_r = √(1,013 − 0,203) = √0,810 = 0,900 Hz, inférieure à N₀.
4. En N_r, ω_r = 2π × 0,900 = 5,66 rad/s : m·ω_r² = 6,40 N/m, h·ω_r = 4,53 N/m, donc X_m = 0,10 / √(4,53² + (6,40 − 8,0)²) = 0,10 / 4,80 = 2,08 × 10⁻² m.
5. En N₀, m·ω₀² = k, le terme (mω² − k) s'annule et X_m = F_m/(h·ω₀) = 0,10 / (0,80 × 6,325) = 1,98 × 10⁻² m : plus petite que 2,08 cm, comme le montre la figure.

:::

::: piege
**Erreur : croire que l'amplitude est maximale à N₀, comme l'intensité du circuit RLC.** Dans l'exemple, X_m vaut 1,98 cm à N₀ et 2,08 cm à N_r (étapes 4 et 5) : le maximum est à N_r. L'erreur tente parce que « résonance » rappelle la fréquence propre, et que l'écart est ici de 0,1 Hz seulement. Mais le terme h²/(8π²m²) décale le maximum de X_m vers les basses fréquences.
:::

::: propriete
**Ce qui reste vrai** — Pour h > 0, N_r < N₀, et l'écart N₀ − N_r grandit avec h ; N_r se rapproche de N₀ quand h diminue. Cas limite idéal : pour h = 0, N_r = N₀ et X_m deviendrait infinie, ce qu'aucun pendule réel n'atteint puisque les frottements existent toujours. Pour h² ≥ 2mk, il n'y a plus de maximum : X_m diminue dès N = 0.
:::

::: verifie À toi : une autre fréquence de résonance
m = 0,50 kg, k = 50 N/m, h = 2,0 kg/s. La résonance d'élongation existe-t-elle ? Calculer N₀ et N_r.

---

2mk = 2 × 0,50 × 50 = 50 est plus grand que h² = 4,0 : la résonance existe. N₀ = (1/2π)√(50/0,50) = 10/6,283 = 1,59 Hz. Avec ω₀² = 100 rad²/s², ω_r² = ω₀² − h²/(2m²) = 100 − 4,0/0,50 = 92, donc ω_r = 9,59 rad/s et N_r = 9,59/6,283 = 1,53 Hz, inférieure à N₀.
:::

::: retenir
X_m est maximale pour N_r = √(N₀² − h²/(8π²m²)), inférieure à N₀, à condition que h² < 2mk.
:::

## 🚀 La résonance de vitesse et le retard de phase

Regarde maintenant la vitesse du palet plutôt que sa position. Son amplitude V_m = ω·X_m ne culmine pas là où X_m culmine, puisque ω change avec N.
Où V_m est-elle maximale, et comment se situent alors la vitesse, la position et la force excitatrice les unes par rapport aux autres ?

::: definition
**Résonance de vitesse** — V_m = F_m/Z est maximale quand Z est minimale, c'est-à-dire quand mω = k/ω : à la fréquence N_r = N₀, **quel que soit h**. Alors Z = h, V_m = F_m/h et la vitesse est **en phase** avec la force excitatrice. En général, le déphasage de v par rapport à F vérifie :

$$ tan(φ_v − φ_F) = (k/ω − mω) / h $$

et l'élongation, intégrale de la vitesse, est en retard de π/2 sur elle : φ_x = φ_v − π/2.
:::

| Fréquence | v par rapport à F | x par rapport à F |
| --- | --- | --- |
| N < N₀ | v en avance | x en retard de moins de π/2 |
| N = N₀ | v en phase | x en retard de π/2 |
| N > N₀ | v en retard | x en retard de plus de π/2 |

Dans le tableau, la ligne N = N₀ est celle de la résonance de vitesse ; x est en retard sur F dans les trois lignes, de plus en plus quand N augmente.

::: exemple Étudier le pendule à la résonance de vitesse (m = 0,200 kg ; k = 8,0 N/m ; h = 0,80 kg/s ; F_m = 0,10 N)

1. ω₀ = √(k/m) = 6,325 rad/s : m·ω₀ = 1,265 kg/s et k/ω₀ = 1,265 kg/s se compensent, donc Z = h = 0,80 kg/s.
2. V_m = F_m/h = 0,10 / 0,80 = 0,125 m/s : c'est le maximum de la vitesse, atteint à N₀ quelle que soit la valeur de h.
3. X_m = V_m/ω₀ = 0,125 / 6,325 = 1,98 × 10⁻² m, un peu moins que le maximum de l'élongation (2,08 cm en N_r).
4. tan(φ_v − φ_F) = (k/ω₀ − m·ω₀)/h = 0, donc φ_v = φ_F : v est en phase avec F, et φ_x = φ_F − π/2 : x est en retard de π/2 sur F.
5. Comparaison à ω = 5,0 rad/s (N < N₀) : tan(φ_v − φ_F) = (8,0/5,0 − 0,200 × 5,0)/0,80 = 0,75, donc φ_v − φ_F = +0,64 rad (v en avance), φ_x − φ_F = −π/2 + 0,64 = −0,93 rad, et V_m = 0,10 m/s est plus petite que 0,125 m/s.

:::

::: piege
**Erreur : croire qu'à la résonance de vitesse, c'est l'élongation x qui est en phase avec F.** Dans l'exemple, c'est la vitesse qui l'est (étape 4), et x est en retard de π/2. L'erreur tente parce que « résonance » évoque une mise en phase générale. Mais x est l'intégrale de v : elle est décalée de π/2 par rapport à la vitesse, donc de π/2 par rapport à F.
:::

::: propriete
**Ce qui reste vrai** — La résonance de vitesse a lieu à N₀ pour toute valeur de h, et V_m = F_m/h diminue quand h augmente. Aux basses fréquences, x est presque en phase avec F (φ_x − φ_F proche de 0) ; aux hautes fréquences, presque en opposition (proche de −π) ; pour h > 0, x est en retard sur F à toute fréquence. Cas limite : à N = N₀, le retard est exactement π/2.
:::

::: verifie À toi : la résonance d'un autre pendule
m = 0,50 kg, k = 50 N/m, h = 2,0 kg/s, F_m = 0,60 N, moteur réglé sur la résonance de vitesse. Calculer N, V_m, X_m, et dire de combien x est en retard sur F.

---

La résonance de vitesse a lieu à N₀ = (1/2π)√(k/m) = 1,59 Hz, avec ω₀ = 10 rad/s. Alors Z = h = 2,0 kg/s et V_m = F_m/h = 0,60 / 2,0 = 0,30 m/s, puis X_m = V_m/ω₀ = 0,30 / 10 = 3,0 × 10⁻² m = 3,0 cm. La vitesse est en phase avec F, donc x est en retard de π/2 rad sur F.
:::

::: retenir
V_m est maximale à N₀ quel que soit h (Z = h, V_m = F_m/h), avec v en phase avec F et x en retard de π/2 ; à toute fréquence x est en retard sur F.
:::

## 🎚️ L'influence de l'amortissement

Fixe sur le palet une plaque de plus en plus grande, qui freine de plus en plus l'air. Avec une petite plaque, le palet s'emballe nettement près de la bonne fréquence ; avec une très grande, il vibre à peine, quelle que soit la fréquence du moteur.
Comment le coefficient de frottement h transforme-t-il la courbe de résonance ?

::: definition
**Résonance aiguë, résonance floue** — Plus h est faible, plus le pic de X_m(N) est haut et étroit : la résonance est **aiguë**. Plus h est grand, plus le pic est bas et large : la résonance est **floue**, et N_r s'éloigne de N₀. Au-delà de h = √(2mk) = m·ω₀√2, il n'y a plus de maximum : X_m diminue dès N = 0 et l'amplitude reste petite. Avec un amortissement très important, il n'y a plus de résonance et le régime forcé est dit **linéaire**.
:::

::: figure Trois courbes X_m(N) pour m = 0,200 kg, k = 8,0 N/m et F_m = 0,10 N (valeurs d'illustration) : résonance aiguë à h = 0,20 kg/s, floue à h = 0,80 kg/s, absente à h = 1,9 kg/s ; les points marquent les maxima
<svg viewBox="0 0 340 226"><title>Trois courbes de résonance Xm(N) pour m = 0,200 kg, k = 8,0 N/m et Fm = 0,10 N : résonance aiguë à h = 0,20 kg/s, floue à 0,80 kg/s, absente à 1,9 kg/s</title><line x1="54" y1="151" x2="320" y2="151" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/><line x1="54" y1="112" x2="320" y2="112" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/><line x1="54" y1="73" x2="320" y2="73" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/><line x1="54" y1="34" x2="320" y2="34" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/><line x1="54" y1="190" x2="322" y2="190" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><line x1="54" y1="190" x2="54" y2="30" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><polygon points="328,190 320,186 320,194" fill="#0f172a"/><polygon points="54,24 50,32 58,32" fill="#0f172a"/><line x1="51" y1="151" x2="54" y2="151" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><text x="48" y="155" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><line x1="51" y1="112" x2="54" y2="112" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><text x="48" y="116" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4</text><line x1="51" y1="73" x2="54" y2="73" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><text x="48" y="77" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">6</text><line x1="51" y1="34" x2="54" y2="34" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><text x="48" y="38" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">8</text><line x1="54" y1="190" x2="54" y2="193" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><text x="54" y="205" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0</text><line x1="120.5" y1="190" x2="120.5" y2="193" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><text x="120.5" y="205" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0,5</text><line x1="187" y1="190" x2="187" y2="193" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><text x="187" y="205" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><line x1="253.5" y1="190" x2="253.5" y2="193" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><text x="253.5" y="205" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1,5</text><line x1="320" y1="190" x2="320" y2="193" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><text x="320" y="205" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><text x="324" y="220" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">N (Hz)</text><text x="62" y="22" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"></text><line x1="187.9" y1="190" x2="187.9" y2="40" stroke="#0f172a" stroke-width="1.4" stroke-dasharray="5 4" stroke-linecap="round"/><polyline points="54,165.6 54.7,165.6 55.3,165.6 56,165.6 56.7,165.6 57.3,165.6 58,165.6 58.7,165.6 59.3,165.6 60,165.6 60.6,165.6 61.3,165.6 62,165.5 62.6,165.5 63.3,165.5 64,165.5 64.6,165.5 65.3,165.5 66,165.4 66.6,165.4 67.3,165.4 68,165.4 68.6,165.3 69.3,165.3 70,165.3 70.6,165.2 71.3,165.2 72,165.2 72.6,165.2 73.3,165.1 74,165.1 74.6,165 75.3,165 75.9,165 76.6,164.9 77.3,164.9 77.9,164.8 78.6,164.8 79.3,164.7 79.9,164.7 80.6,164.6 81.3,164.6 81.9,164.5 82.6,164.5 83.3,164.4 83.9,164.4 84.6,164.3 85.3,164.2 85.9,164.2 86.6,164.1 87.2,164 87.9,164 88.6,163.9 89.2,163.8 89.9,163.8 90.6,163.7 91.2,163.6 91.9,163.5 92.6,163.5 93.2,163.4 93.9,163.3 94.6,163.2 95.2,163.1 95.9,163 96.6,162.9 97.2,162.8 97.9,162.7 98.6,162.6 99.2,162.5 99.9,162.4 100.5,162.3 101.2,162.2 101.9,162.1 102.5,162 103.2,161.9 103.9,161.8 104.5,161.6 105.2,161.5 105.9,161.4 106.5,161.3 107.2,161.1 107.9,161 108.5,160.9 109.2,160.7 109.9,160.6 110.5,160.4 111.2,160.3 111.9,160.1 112.5,160 113.2,159.8 113.8,159.7 114.5,159.5 115.2,159.3 115.8,159.1 116.5,159 117.2,158.8 117.8,158.6 118.5,158.4 119.2,158.2 119.8,158 120.5,157.8 121.2,157.6 121.8,157.4 122.5,157.2 123.2,157 123.8,156.7 124.5,156.5 125.2,156.3 125.8,156 126.5,155.8 127.2,155.5 127.8,155.2 128.5,155 129.1,154.7 129.8,154.4 130.5,154.1 131.1,153.8 131.8,153.5 132.5,153.2 133.1,152.9 133.8,152.6 134.5,152.3 135.1,151.9 135.8,151.6 136.5,151.2 137.1,150.8 137.8,150.4 138.5,150.1 139.1,149.7 139.8,149.2 140.4,148.8 141.1,148.4 141.8,147.9 142.4,147.5 143.1,147 143.8,146.5 144.4,146 145.1,145.5 145.8,145 146.4,144.4 147.1,143.8 147.8,143.2 148.4,142.6 149.1,142 149.8,141.4 150.4,140.7 151.1,140 151.8,139.3 152.4,138.6 153.1,137.8 153.8,137 154.4,136.2 155.1,135.4 155.7,134.5 156.4,133.6 157.1,132.6 157.7,131.7 158.4,130.7 159.1,129.6 159.7,128.5 160.4,127.4 161.1,126.2 161.7,125 162.4,123.7 163.1,122.3 163.7,120.9 164.4,119.5 165.1,118 165.7,116.4 166.4,114.7 167.1,113 167.7,111.2 168.4,109.3 169,107.3 169.7,105.2 170.4,103.1 171,100.8 171.7,98.4 172.4,95.9 173,93.4 173.7,90.7 174.4,87.9 175,84.9 175.7,81.9 176.4,78.7 177,75.5 177.7,72.1 178.4,68.7 179,65.2 179.7,61.7 180.3,58.2 181,54.7 181.7,51.4 182.3,48.1 183,45.1 183.7,42.4 184.3,40 185,38.1 185.7,36.6 186.3,35.7 187,35.4 187.7,35.6 188.3,36.5 189,38 189.7,40 190.3,42.4 191,45.3 191.7,48.6 192.3,52.1 193,55.8 193.7,59.7 194.3,63.6 195,67.5 195.6,71.4 196.3,75.3 197,79.1 197.6,82.7 198.3,86.3 199,89.7 199.6,93.1 200.3,96.2 201,99.3 201.6,102.2 202.3,105 203,107.7 203.6,110.2 204.3,112.6 205,114.9 205.6,117.2 206.3,119.3 206.9,121.3 207.6,123.2 208.3,125 208.9,126.8 209.6,128.5 210.3,130.1 210.9,131.6 211.6,133.1 212.3,134.5 212.9,135.9 213.6,137.2 214.3,138.4 214.9,139.6 215.6,140.8 216.3,141.9 216.9,143 217.6,144 218.3,145 218.9,145.9 219.6,146.8 220.2,147.7 220.9,148.6 221.6,149.4 222.2,150.2 222.9,151 223.6,151.7 224.2,152.4 224.9,153.1 225.6,153.8 226.2,154.5 226.9,155.1 227.6,155.7 228.2,156.3 228.9,156.9 229.6,157.5 230.2,158 230.9,158.5 231.6,159 232.2,159.5 232.9,160 233.6,160.5 234.2,161 234.9,161.4 235.5,161.8 236.2,162.3 236.9,162.7 237.5,163.1 238.2,163.5 238.9,163.9 239.5,164.2 240.2,164.6 240.9,165 241.5,165.3 242.2,165.7 242.9,166 243.5,166.3 244.2,166.6 244.9,166.9 245.5,167.2 246.2,167.5 246.8,167.8 247.5,168.1 248.2,168.4 248.8,168.6 249.5,168.9 250.2,169.2 250.8,169.4 251.5,169.7 252.2,169.9 252.8,170.2 253.5,170.4 254.2,170.6 254.8,170.8 255.5,171.1 256.2,171.3 256.8,171.5 257.5,171.7 258.2,171.9 258.8,172.1 259.5,172.3 260.1,172.5 260.8,172.7 261.5,172.9 262.1,173.1 262.8,173.2 263.5,173.4 264.1,173.6 264.8,173.8 265.5,173.9 266.1,174.1 266.8,174.2 267.5,174.4 268.1,174.6 268.8,174.7 269.5,174.9 270.1,175 270.8,175.2 271.5,175.3 272.1,175.4 272.8,175.6 273.4,175.7 274.1,175.9 274.8,176 275.4,176.1 276.1,176.2 276.8,176.4 277.4,176.5 278.1,176.6 278.8,176.7 279.4,176.9 280.1,177 280.8,177.1 281.4,177.2 282.1,177.3 282.8,177.4 283.4,177.5 284.1,177.6 284.8,177.7 285.4,177.9 286.1,178 286.8,178.1 287.4,178.2 288.1,178.3 288.7,178.4 289.4,178.5 290.1,178.5 290.7,178.6 291.4,178.7 292.1,178.8 292.7,178.9 293.4,179 294.1,179.1 294.7,179.2 295.4,179.3 296.1,179.3 296.7,179.4 297.4,179.5 298.1,179.6 298.7,179.7 299.4,179.7 300.1,179.8 300.7,179.9 301.4,180 302,180.1 302.7,180.1 303.4,180.2 304,180.3 304.7,180.3 305.4,180.4 306,180.5 306.7,180.6 307.4,180.6 308,180.7 308.7,180.8 309.4,180.8 310,180.9 310.7,181 311.4,181 312,181.1 312.7,181.1 313.3,181.2 314,181.3 314.7,181.3 315.3,181.4 316,181.4 316.7,181.5 317.3,181.6 318,181.6 318.7,181.7 319.3,181.7 320,181.8" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"/><polyline points="54,165.6 54.7,165.6 55.3,165.6 56,165.6 56.7,165.6 57.3,165.6 58,165.6 58.7,165.6 59.3,165.6 60,165.6 60.6,165.6 61.3,165.6 62,165.6 62.6,165.5 63.3,165.5 64,165.5 64.6,165.5 65.3,165.5 66,165.5 66.6,165.5 67.3,165.4 68,165.4 68.6,165.4 69.3,165.4 70,165.3 70.6,165.3 71.3,165.3 72,165.3 72.6,165.2 73.3,165.2 74,165.2 74.6,165.2 75.3,165.1 75.9,165.1 76.6,165.1 77.3,165 77.9,165 78.6,165 79.3,164.9 79.9,164.9 80.6,164.8 81.3,164.8 81.9,164.8 82.6,164.7 83.3,164.7 83.9,164.6 84.6,164.6 85.3,164.5 85.9,164.5 86.6,164.4 87.2,164.4 87.9,164.3 88.6,164.3 89.2,164.2 89.9,164.2 90.6,164.1 91.2,164 91.9,164 92.6,163.9 93.2,163.9 93.9,163.8 94.6,163.7 95.2,163.7 95.9,163.6 96.6,163.5 97.2,163.5 97.9,163.4 98.6,163.3 99.2,163.3 99.9,163.2 100.5,163.1 101.2,163 101.9,162.9 102.5,162.9 103.2,162.8 103.9,162.7 104.5,162.6 105.2,162.5 105.9,162.4 106.5,162.4 107.2,162.3 107.9,162.2 108.5,162.1 109.2,162 109.9,161.9 110.5,161.8 111.2,161.7 111.9,161.6 112.5,161.5 113.2,161.4 113.8,161.3 114.5,161.2 115.2,161.1 115.8,161 116.5,160.8 117.2,160.7 117.8,160.6 118.5,160.5 119.2,160.4 119.8,160.3 120.5,160.1 121.2,160 121.8,159.9 122.5,159.8 123.2,159.6 123.8,159.5 124.5,159.4 125.2,159.2 125.8,159.1 126.5,159 127.2,158.8 127.8,158.7 128.5,158.5 129.1,158.4 129.8,158.3 130.5,158.1 131.1,158 131.8,157.8 132.5,157.7 133.1,157.5 133.8,157.4 134.5,157.2 135.1,157.1 135.8,156.9 136.5,156.7 137.1,156.6 137.8,156.4 138.5,156.3 139.1,156.1 139.8,155.9 140.4,155.8 141.1,155.6 141.8,155.4 142.4,155.3 143.1,155.1 143.8,154.9 144.4,154.7 145.1,154.6 145.8,154.4 146.4,154.2 147.1,154.1 147.8,153.9 148.4,153.7 149.1,153.6 149.8,153.4 150.4,153.2 151.1,153 151.8,152.9 152.4,152.7 153.1,152.5 153.8,152.4 154.4,152.2 155.1,152.1 155.7,151.9 156.4,151.8 157.1,151.6 157.7,151.5 158.4,151.3 159.1,151.2 159.7,151 160.4,150.9 161.1,150.8 161.7,150.6 162.4,150.5 163.1,150.4 163.7,150.3 164.4,150.2 165.1,150.1 165.7,150 166.4,149.9 167.1,149.8 167.7,149.7 168.4,149.6 169,149.6 169.7,149.5 170.4,149.5 171,149.4 171.7,149.4 172.4,149.4 173,149.4 173.7,149.4 174.4,149.4 175,149.4 175.7,149.4 176.4,149.4 177,149.5 177.7,149.5 178.4,149.6 179,149.7 179.7,149.7 180.3,149.8 181,149.9 181.7,150 182.3,150.2 183,150.3 183.7,150.4 184.3,150.6 185,150.7 185.7,150.9 186.3,151 187,151.2 187.7,151.4 188.3,151.6 189,151.8 189.7,152 190.3,152.2 191,152.4 191.7,152.7 192.3,152.9 193,153.1 193.7,153.4 194.3,153.6 195,153.9 195.6,154.1 196.3,154.4 197,154.7 197.6,154.9 198.3,155.2 199,155.5 199.6,155.8 200.3,156 201,156.3 201.6,156.6 202.3,156.9 203,157.2 203.6,157.5 204.3,157.8 205,158.1 205.6,158.3 206.3,158.6 206.9,158.9 207.6,159.2 208.3,159.5 208.9,159.8 209.6,160.1 210.3,160.4 210.9,160.7 211.6,160.9 212.3,161.2 212.9,161.5 213.6,161.8 214.3,162.1 214.9,162.3 215.6,162.6 216.3,162.9 216.9,163.1 217.6,163.4 218.3,163.7 218.9,163.9 219.6,164.2 220.2,164.5 220.9,164.7 221.6,165 222.2,165.2 222.9,165.5 223.6,165.7 224.2,166 224.9,166.2 225.6,166.4 226.2,166.7 226.9,166.9 227.6,167.1 228.2,167.4 228.9,167.6 229.6,167.8 230.2,168 230.9,168.2 231.6,168.5 232.2,168.7 232.9,168.9 233.6,169.1 234.2,169.3 234.9,169.5 235.5,169.7 236.2,169.9 236.9,170.1 237.5,170.3 238.2,170.5 238.9,170.6 239.5,170.8 240.2,171 240.9,171.2 241.5,171.4 242.2,171.5 242.9,171.7 243.5,171.9 244.2,172.1 244.9,172.2 245.5,172.4 246.2,172.5 246.8,172.7 247.5,172.9 248.2,173 248.8,173.2 249.5,173.3 250.2,173.5 250.8,173.6 251.5,173.8 252.2,173.9 252.8,174.1 253.5,174.2 254.2,174.3 254.8,174.5 255.5,174.6 256.2,174.7 256.8,174.9 257.5,175 258.2,175.1 258.8,175.3 259.5,175.4 260.1,175.5 260.8,175.6 261.5,175.8 262.1,175.9 262.8,176 263.5,176.1 264.1,176.2 264.8,176.3 265.5,176.4 266.1,176.6 266.8,176.7 267.5,176.8 268.1,176.9 268.8,177 269.5,177.1 270.1,177.2 270.8,177.3 271.5,177.4 272.1,177.5 272.8,177.6 273.4,177.7 274.1,177.8 274.8,177.9 275.4,178 276.1,178.1 276.8,178.2 277.4,178.2 278.1,178.3 278.8,178.4 279.4,178.5 280.1,178.6 280.8,178.7 281.4,178.8 282.1,178.9 282.8,178.9 283.4,179 284.1,179.1 284.8,179.2 285.4,179.3 286.1,179.3 286.8,179.4 287.4,179.5 288.1,179.6 288.7,179.6 289.4,179.7 290.1,179.8 290.7,179.9 291.4,179.9 292.1,180 292.7,180.1 293.4,180.1 294.1,180.2 294.7,180.3 295.4,180.3 296.1,180.4 296.7,180.5 297.4,180.5 298.1,180.6 298.7,180.7 299.4,180.7 300.1,180.8 300.7,180.9 301.4,180.9 302,181 302.7,181 303.4,181.1 304,181.2 304.7,181.2 305.4,181.3 306,181.3 306.7,181.4 307.4,181.4 308,181.5 308.7,181.5 309.4,181.6 310,181.7 310.7,181.7 311.4,181.8 312,181.8 312.7,181.9 313.3,181.9 314,182 314.7,182 315.3,182.1 316,182.1 316.7,182.2 317.3,182.2 318,182.3 318.7,182.3 319.3,182.3 320,182.4" fill="none" stroke="#1d4ed8" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"/><polyline points="54,165.6 54.7,165.6 55.3,165.6 56,165.6 56.7,165.6 57.3,165.6 58,165.6 58.7,165.6 59.3,165.6 60,165.6 60.6,165.6 61.3,165.6 62,165.6 62.6,165.6 63.3,165.6 64,165.6 64.6,165.6 65.3,165.6 66,165.7 66.6,165.7 67.3,165.7 68,165.7 68.6,165.7 69.3,165.7 70,165.7 70.6,165.7 71.3,165.7 72,165.7 72.6,165.7 73.3,165.7 74,165.7 74.6,165.7 75.3,165.7 75.9,165.7 76.6,165.7 77.3,165.7 77.9,165.7 78.6,165.7 79.3,165.8 79.9,165.8 80.6,165.8 81.3,165.8 81.9,165.8 82.6,165.8 83.3,165.8 83.9,165.8 84.6,165.8 85.3,165.8 85.9,165.8 86.6,165.8 87.2,165.9 87.9,165.9 88.6,165.9 89.2,165.9 89.9,165.9 90.6,165.9 91.2,165.9 91.9,165.9 92.6,166 93.2,166 93.9,166 94.6,166 95.2,166 95.9,166 96.6,166.1 97.2,166.1 97.9,166.1 98.6,166.1 99.2,166.1 99.9,166.1 100.5,166.2 101.2,166.2 101.9,166.2 102.5,166.2 103.2,166.2 103.9,166.3 104.5,166.3 105.2,166.3 105.9,166.3 106.5,166.4 107.2,166.4 107.9,166.4 108.5,166.4 109.2,166.5 109.9,166.5 110.5,166.5 111.2,166.5 111.9,166.6 112.5,166.6 113.2,166.6 113.8,166.7 114.5,166.7 115.2,166.7 115.8,166.8 116.5,166.8 117.2,166.8 117.8,166.9 118.5,166.9 119.2,166.9 119.8,167 120.5,167 121.2,167 121.8,167.1 122.5,167.1 123.2,167.2 123.8,167.2 124.5,167.2 125.2,167.3 125.8,167.3 126.5,167.4 127.2,167.4 127.8,167.5 128.5,167.5 129.1,167.6 129.8,167.6 130.5,167.7 131.1,167.7 131.8,167.8 132.5,167.8 133.1,167.9 133.8,167.9 134.5,168 135.1,168 135.8,168.1 136.5,168.1 137.1,168.2 137.8,168.2 138.5,168.3 139.1,168.3 139.8,168.4 140.4,168.5 141.1,168.5 141.8,168.6 142.4,168.6 143.1,168.7 143.8,168.8 144.4,168.8 145.1,168.9 145.8,169 146.4,169 147.1,169.1 147.8,169.1 148.4,169.2 149.1,169.3 149.8,169.3 150.4,169.4 151.1,169.5 151.8,169.6 152.4,169.6 153.1,169.7 153.8,169.8 154.4,169.8 155.1,169.9 155.7,170 156.4,170 157.1,170.1 157.7,170.2 158.4,170.3 159.1,170.3 159.7,170.4 160.4,170.5 161.1,170.6 161.7,170.6 162.4,170.7 163.1,170.8 163.7,170.9 164.4,170.9 165.1,171 165.7,171.1 166.4,171.2 167.1,171.3 167.7,171.3 168.4,171.4 169,171.5 169.7,171.6 170.4,171.7 171,171.7 171.7,171.8 172.4,171.9 173,172 173.7,172 174.4,172.1 175,172.2 175.7,172.3 176.4,172.4 177,172.5 177.7,172.5 178.4,172.6 179,172.7 179.7,172.8 180.3,172.9 181,172.9 181.7,173 182.3,173.1 183,173.2 183.7,173.3 184.3,173.3 185,173.4 185.7,173.5 186.3,173.6 187,173.7 187.7,173.7 188.3,173.8 189,173.9 189.7,174 190.3,174.1 191,174.1 191.7,174.2 192.3,174.3 193,174.4 193.7,174.5 194.3,174.5 195,174.6 195.6,174.7 196.3,174.8 197,174.9 197.6,174.9 198.3,175 199,175.1 199.6,175.2 200.3,175.3 201,175.3 201.6,175.4 202.3,175.5 203,175.6 203.6,175.6 204.3,175.7 205,175.8 205.6,175.9 206.3,175.9 206.9,176 207.6,176.1 208.3,176.2 208.9,176.2 209.6,176.3 210.3,176.4 210.9,176.5 211.6,176.5 212.3,176.6 212.9,176.7 213.6,176.7 214.3,176.8 214.9,176.9 215.6,177 216.3,177 216.9,177.1 217.6,177.2 218.3,177.2 218.9,177.3 219.6,177.4 220.2,177.5 220.9,177.5 221.6,177.6 222.2,177.7 222.9,177.7 223.6,177.8 224.2,177.9 224.9,177.9 225.6,178 226.2,178.1 226.9,178.1 227.6,178.2 228.2,178.2 228.9,178.3 229.6,178.4 230.2,178.4 230.9,178.5 231.6,178.6 232.2,178.6 232.9,178.7 233.6,178.8 234.2,178.8 234.9,178.9 235.5,178.9 236.2,179 236.9,179.1 237.5,179.1 238.2,179.2 238.9,179.2 239.5,179.3 240.2,179.3 240.9,179.4 241.5,179.5 242.2,179.5 242.9,179.6 243.5,179.6 244.2,179.7 244.9,179.7 245.5,179.8 246.2,179.9 246.8,179.9 247.5,180 248.2,180 248.8,180.1 249.5,180.1 250.2,180.2 250.8,180.2 251.5,180.3 252.2,180.3 252.8,180.4 253.5,180.4 254.2,180.5 254.8,180.5 255.5,180.6 256.2,180.6 256.8,180.7 257.5,180.7 258.2,180.8 258.8,180.8 259.5,180.9 260.1,180.9 260.8,181 261.5,181 262.1,181.1 262.8,181.1 263.5,181.2 264.1,181.2 264.8,181.3 265.5,181.3 266.1,181.4 266.8,181.4 267.5,181.4 268.1,181.5 268.8,181.5 269.5,181.6 270.1,181.6 270.8,181.7 271.5,181.7 272.1,181.7 272.8,181.8 273.4,181.8 274.1,181.9 274.8,181.9 275.4,182 276.1,182 276.8,182 277.4,182.1 278.1,182.1 278.8,182.2 279.4,182.2 280.1,182.2 280.8,182.3 281.4,182.3 282.1,182.4 282.8,182.4 283.4,182.4 284.1,182.5 284.8,182.5 285.4,182.5 286.1,182.6 286.8,182.6 287.4,182.7 288.1,182.7 288.7,182.7 289.4,182.8 290.1,182.8 290.7,182.8 291.4,182.9 292.1,182.9 292.7,182.9 293.4,183 294.1,183 294.7,183 295.4,183.1 296.1,183.1 296.7,183.1 297.4,183.2 298.1,183.2 298.7,183.2 299.4,183.3 300.1,183.3 300.7,183.3 301.4,183.4 302,183.4 302.7,183.4 303.4,183.5 304,183.5 304.7,183.5 305.4,183.6 306,183.6 306.7,183.6 307.4,183.7 308,183.7 308.7,183.7 309.4,183.7 310,183.8 310.7,183.8 311.4,183.8 312,183.9 312.7,183.9 313.3,183.9 314,183.9 314.7,184 315.3,184 316,184 316.7,184.1 317.3,184.1 318,184.1 318.7,184.1 319.3,184.2 320,184.2" fill="none" stroke="#b45309" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"/><circle cx="187" cy="35.4" r="4.5" fill="#0f6e56"/><circle cx="173.7" cy="149.4" r="4.5" fill="#1d4ed8"/><text x="191.9" y="28" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">N<tspan dy="3" font-size="9">0</tspan></text><text x="62" y="22" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">X<tspan dy="3" font-size="9">m</tspan><tspan dy="-3"> (cm)</tspan></text><line x1="228" y1="40" x2="246" y2="40" stroke="#0f6e56" stroke-width="3" stroke-linecap="round"/><text x="252" y="44" text-anchor="start" font-size="11" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">h = 0,20 kg/s</text><line x1="228" y1="57" x2="246" y2="57" stroke="#1d4ed8" stroke-width="3" stroke-linecap="round"/><text x="252" y="61" text-anchor="start" font-size="11" font-weight="700" fill="#1d4ed8" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">h = 0,80 kg/s</text><line x1="228" y1="74" x2="246" y2="74" stroke="#b45309" stroke-width="3" stroke-linecap="round"/><text x="252" y="78" text-anchor="start" font-size="11" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">h = 1,9 kg/s</text></svg>
:::

Sur la figure, la courbe verte (h faible) est haute et étroite autour de N₀, la bleue est plus basse et plus large, la orange (h = 1,9 kg/s, au-delà du seuil de 1,79 kg/s) n'a plus de pic.

::: exemple Suivre N_r et le pic quand h augmente (m = 0,200 kg ; k = 8,0 N/m ; F_m = 0,10 N)

1. Seuil : h_lim = √(2mk) = √(2 × 0,200 × 8,0) = √3,2 = 1,79 kg/s ; on a N₀ = 1,007 Hz et F_m/k = 1,25 cm.
2. h = 0,20 kg/s : N_r = √(1,013 − 0,0127) = 1,000 Hz, presque N₀, et X_m(N_r) ≈ 7,9 cm : résonance très aiguë.
3. h = 0,80 kg/s : N_r = 0,900 Hz et X_m(N_r) ≈ 2,08 cm : le pic est plus bas et le maximum s'est décalé de 0,107 Hz sous N₀.
4. h = 1,2 kg/s : N_r = √(1,013 − 0,456) = 0,747 Hz et X_m(N_r) ≈ 1,50 cm, à peine plus que F_m/k = 1,25 cm : le pic s'efface.
5. h = 1,9 kg/s dépasse h_lim : le radicande 1,013 − 1,143 est négatif, il n'y a plus de maximum, et X_m décroît à partir de 1,25 cm (courbe orange).

:::

::: piege
**Erreur : croire que plus on amortit, plus N_r se rapproche de N₀.** Dans l'exemple, N_r vaut 1,000 Hz, puis 0,900 Hz, puis 0,747 Hz quand h augmente (étapes 2 à 4) : il s'éloigne de N₀ = 1,007 Hz. L'erreur tente parce que N₀ ne dépend pas de h et qu'on imagine le pic « fixé » là. Mais N_r contient le terme h²/(8π²m²), qui croît avec h : seule la résonance de vitesse reste en N₀.
:::

::: propriete
**Ce qui reste vrai** — À fréquence donnée, X_m diminue quand h augmente, puisque h figure au dénominateur. N₀ ne dépend que de m et de k, et la résonance de vitesse reste à N₀ pour tout h. Cas limite : pour h = h_lim, le maximum se confond avec N = 0 ; au-delà, X_m est partout inférieure à F_m/k.
:::

::: verifie À toi : avec ou sans résonance ?
m = 0,50 kg, k = 50 N/m. Pour h = 5,0 kg/s puis pour h = 8,0 kg/s, y a-t-il une résonance d'élongation ? Si oui, calculer N_r.

---

h_lim = √(2mk) = √50 = 7,07 kg/s. Pour h = 5,0 kg/s, h est inférieur à h_lim : il y a résonance, avec ω_r² = 100 − 25/(2 × 0,25) = 50, donc ω_r = 7,07 rad/s et N_r = 1,13 Hz (N₀ = 1,59 Hz). Pour h = 8,0 kg/s, h est supérieur à h_lim : ω_r² = 100 − 64/0,50 = −28 < 0, il n'y a pas de résonance d'élongation.
:::

::: retenir
Plus h est faible, plus la résonance est aiguë ; plus h est grand, plus elle est floue et plus N_r s'éloigne de N₀ ; pour h ≥ √(2mk), il n'y a plus de résonance d'élongation.
:::

## 🔌 La puissance mécanique moyenne

Pendant que le palet oscille, le moteur lui fournit de l'énergie et les frottements la transforment en chaleur. En régime permanent, l'énergie du pendule ne varie plus d'une période à l'autre : tout ce que le moteur apporte est dissipé par les frottements.
Quelle puissance moyenne le moteur fournit-il, et à quelle fréquence est-elle la plus grande ?

::: definition
**Puissance mécanique moyenne** — En régime sinusoïdal forcé, la puissance moyenne reçue par le pendule est, avec φ = φ_v − φ_F le déphasage entre v et F :

$$ P = ½·F_m·V_m·cos φ = ½·h·V_m² $$

Le facteur de puissance est cos φ = h/Z, et P s'exprime en watt. Elle est analogue à la puissance électrique moyenne du chapitre 4, avec F_m ↔ U_m, V_m ↔ I_m et h ↔ R.
:::

::: exemple Puissance du pendule à N₀ et à ω = 5,0 rad/s (m = 0,200 kg ; k = 8,0 N/m ; h = 0,80 kg/s ; F_m = 0,10 N)

1. À la résonance de vitesse, V_m = 0,125 m/s et φ = 0, donc cos φ = 1 et P = ½ × 0,10 × 0,125 × 1 = 6,25 × 10⁻³ W.
2. Contrôle avec l'autre forme : P = ½·h·V_m² = ½ × 0,80 × 0,125² = 6,25 × 10⁻³ W ✓, les deux expressions s'accordent.
3. À ω = 5,0 rad/s : V_m = 0,10 m/s et Z = 1,0 kg/s, donc cos φ = h/Z = 0,80 et P = ½ × 0,10 × 0,10 × 0,80 = 4,0 × 10⁻³ W, soit ½ × 0,80 × 0,10² = 4,0 × 10⁻³ W avec la seconde forme.
4. La puissance maximale est donc P₀ = F_m²/(2h) = 0,010 / 1,6 = 6,25 mW, atteinte à N₀ et non à N_r : le maximum de puissance suit celui de la vitesse.

:::

::: piege
**Erreur : oublier le facteur ½, et écrire P = F_m·V_m·cos φ.** À N₀, cela donnerait 12,5 mW au lieu de 6,25 mW (étape 1). L'erreur tente parce que, pour une force constante, la puissance vaut F·v. Mais F et v sont ici sinusoïdales : F_m et V_m sont des valeurs maximales, et la moyenne du produit de deux sinusoïdes introduit le facteur ½.
:::

::: propriete
**Ce qui reste vrai** — P = ½·h·V_m² (en W) est maximale à N₀ (résonance de puissance), avec P₀ = F_m²/(2h) : plus h est faible, plus la puissance maximale est grande. Loin de N₀, P tend vers 0. Cas limite : à N₀, cos φ = 1, et toute la puissance fournie par le moteur est dissipée par les frottements.
:::

::: verifie À toi : puissance à la résonance
Pour le pendule de la notion 5 (m = 0,50 kg, k = 50 N/m, h = 2,0 kg/s, F_m = 0,60 N) à la résonance de vitesse, calculer P par les deux formes.

---

À N₀, V_m = 0,30 m/s et cos φ = 1. P = ½ × 0,60 × 0,30 × 1 = 0,090 W, et ½·h·V_m² = ½ × 2,0 × 0,30² = 0,090 W : les deux formes donnent 90 mW.
:::

::: retenir
P = ½·F_m·V_m·cos φ = ½·h·V_m² en watt, avec cos φ = h/Z ; elle est maximale à N₀ : P₀ = F_m²/(2h).
:::

## 🌉 La résonance dans la vie : la vitesse critique

Sur un pont, des joints de dilatation reviennent tous les 12 m. Une voiture qui roule à vitesse constante en franchit un à intervalles réguliers : chaque joint la secoue. À certaines vitesses la caisse se met à tanguer fortement, à d'autres à peine.
À quelle vitesse la voiture est-elle la plus secouée ?

::: definition
**Vitesse critique** — Le profil de la route est l'excitateur, la suspension (ressort de raideur k, masse m de la voiture) est le résonateur. Une voiture de vitesse v franchit des bosses espacées de d avec la période T = d/v, soit la fréquence N = v/d. La caisse est la plus secouée quand cette fréquence est voisine de la fréquence propre de la suspension : T ≈ T₀ = 2π√(m/k). La vitesse correspondante est la **vitesse critique** v_c = d/T₀.
:::

::: figure Voiture roulant à la vitesse v sur une route à bosses régulièrement espacées de la distance d : la voiture franchit une bosse toutes les T = d/v secondes, et sa suspension (ressort vert) joue le rôle de résonateur
<svg viewBox="0 0 340 180"><title>Voiture roulant à vitesse v constante sur une route à bosses régulièrement espacées de d : chaque bosse secoue la suspension, ressort et masse de la voiture</title><polyline points="20,140 21,140 22,140 23,139.9 24,139.9 25,139.8 26,139.7 27,139.6 28,139.5 29,139.4 30,139.2 31,139.1 32,138.9 33,138.7 34,138.5 35,138.4 36,138.1 37,137.9 38,137.7 39,137.5 40,137.2 41,137 42,136.7 43,136.5 44,136.3 45,136 46,135.7 47,135.5 48,135.3 49,135 50,134.8 51,134.5 52,134.3 53,134.1 54,133.9 55,133.6 56,133.5 57,133.3 58,133.1 59,132.9 60,132.8 61,132.6 62,132.5 63,132.4 64,132.3 65,132.2 66,132.1 67,132.1 68,132 69,132 70,132 71,132 72,132 73,132.1 74,132.1 75,132.2 76,132.3 77,132.4 78,132.5 79,132.6 80,132.8 81,132.9 82,133.1 83,133.3 84,133.5 85,133.6 86,133.9 87,134.1 88,134.3 89,134.5 90,134.8 91,135 92,135.3 93,135.5 94,135.7 95,136 96,136.3 97,136.5 98,136.7 99,137 100,137.2 101,137.5 102,137.7 103,137.9 104,138.1 105,138.4 106,138.5 107,138.7 108,138.9 109,139.1 110,139.2 111,139.4 112,139.5 113,139.6 114,139.7 115,139.8 116,139.9 117,139.9 118,140 119,140 120,140 121,140 122,140 123,139.9 124,139.9 125,139.8 126,139.7 127,139.6 128,139.5 129,139.4 130,139.2 131,139.1 132,138.9 133,138.7 134,138.5 135,138.4 136,138.1 137,137.9 138,137.7 139,137.5 140,137.2 141,137 142,136.7 143,136.5 144,136.3 145,136 146,135.7 147,135.5 148,135.3 149,135 150,134.8 151,134.5 152,134.3 153,134.1 154,133.9 155,133.6 156,133.5 157,133.3 158,133.1 159,132.9 160,132.8 161,132.6 162,132.5 163,132.4 164,132.3 165,132.2 166,132.1 167,132.1 168,132 169,132 170,132 171,132 172,132 173,132.1 174,132.1 175,132.2 176,132.3 177,132.4 178,132.5 179,132.6 180,132.8 181,132.9 182,133.1 183,133.3 184,133.5 185,133.6 186,133.9 187,134.1 188,134.3 189,134.5 190,134.8 191,135 192,135.3 193,135.5 194,135.7 195,136 196,136.3 197,136.5 198,136.7 199,137 200,137.2 201,137.5 202,137.7 203,137.9 204,138.1 205,138.4 206,138.5 207,138.7 208,138.9 209,139.1 210,139.2 211,139.4 212,139.5 213,139.6 214,139.7 215,139.8 216,139.9 217,139.9 218,140 219,140 220,140 221,140 222,140 223,139.9 224,139.9 225,139.8 226,139.7 227,139.6 228,139.5 229,139.4 230,139.2 231,139.1 232,138.9 233,138.7 234,138.5 235,138.4 236,138.1 237,137.9 238,137.7 239,137.5 240,137.2 241,137 242,136.7 243,136.5 244,136.3 245,136 246,135.7 247,135.5 248,135.3 249,135 250,134.8 251,134.5 252,134.3 253,134.1 254,133.9 255,133.6 256,133.5 257,133.3 258,133.1 259,132.9 260,132.8 261,132.6 262,132.5 263,132.4 264,132.3 265,132.2 266,132.1 267,132.1 268,132 269,132 270,132 271,132 272,132 273,132.1 274,132.1 275,132.2 276,132.3 277,132.4 278,132.5 279,132.6 280,132.8 281,132.9 282,133.1 283,133.3 284,133.5 285,133.6 286,133.9 287,134.1 288,134.3 289,134.5 290,134.8 291,135 292,135.3 293,135.5 294,135.7 295,136 296,136.3 297,136.5 298,136.7 299,137 300,137.2 301,137.5 302,137.7 303,137.9 304,138.1 305,138.4 306,138.5 307,138.7 308,138.9 309,139.1 310,139.2 311,139.4 312,139.5 313,139.6 314,139.7 315,139.8 316,139.9 317,139.9 318,140 319,140 320,140" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/><rect x="76" y="60" width="88" height="28" fill="#ffffff" stroke="#0f172a" stroke-width="1.8"/><text x="120" y="79" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">voiture</text><polyline points="120,88 113,91 127,96 113,101 127,106 113,111 127,116 113,121 120,122" fill="none" stroke="#0f6e56" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round"/><circle cx="120" cy="131" r="9" fill="#ffffff" stroke="#0f172a" stroke-width="1.8"/><line x1="176" y1="74" x2="236" y2="74" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><polygon points="242,74 234,70 234,78" fill="#0f172a"/><text x="256" y="78" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">v</text><line x1="70" y1="134" x2="70" y2="158" stroke="#0f172a" stroke-width="1.2" stroke-dasharray="3 3" stroke-linecap="round"/><line x1="170" y1="134" x2="170" y2="158" stroke="#0f172a" stroke-width="1.2" stroke-dasharray="3 3" stroke-linecap="round"/><line x1="70" y1="152" x2="170" y2="152" stroke="#b45309" stroke-width="1.8" stroke-linecap="round"/><line x1="70" y1="147" x2="70" y2="157" stroke="#b45309" stroke-width="1.8" stroke-linecap="round"/><line x1="170" y1="147" x2="170" y2="157" stroke="#b45309" stroke-width="1.8" stroke-linecap="round"/><text x="120" y="171" text-anchor="middle" font-size="13" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">d</text></svg>
:::

Sur la figure, la distance d entre deux bosses est parcourue à la vitesse v en une durée T = d/v : c'est la période de l'excitation.

::: exemple Calculer la vitesse critique (m = 900 kg ; k = 4,0 × 10⁴ N/m ; d = 12 m)

1. La voiture franchit un joint toutes les T = d/v secondes, donc l'excitation a la période T = d/v.
2. T₀ = 2π√(m/k) = 2π√(900 / 4,0 × 10⁴) = 2π × 0,150 = 0,942 s : c'est la période propre de la suspension, avec N₀ = 1,06 Hz.
3. Les frottements sont faibles, donc la résonance a lieu pour T ≈ T₀ : d/v_c = T₀, d'où v_c = d/T₀ = 12 / 0,942 = 12,7 m/s.
4. Conversion : 12,7 m/s × 3,6 = 45,8 km/h. À 20 km/h (5,6 m/s), T = 12/5,6 = 2,2 s est très différente de T₀ : la voiture est à peine secouée.

:::

::: piege
**Erreur : oublier le facteur 2π dans la période propre, et écrire T₀ = √(m/k).** On trouverait T₀ = 0,150 s et v_c = 12 / 0,150 = 80 m/s, soit 288 km/h, valeur absurde pour une voiture (étape 2). L'erreur tente parce que la racine √(m/k) est la partie visible de la formule. Mais la période propre est T₀ = 2π√(m/k) : sans le 2π, la vitesse est surestimée d'un facteur 2π.
:::

::: methode

1. **Excitation** : calculer la période T = d/v (ou la fréquence N = v/d) à laquelle le véhicule franchit les bosses.
2. **Résonateur** : calculer la période propre de la suspension, T₀ = 2π√(m/k).
3. **Condition de résonance** : écrire T = T₀ (frottements faibles), d'où v_c = d/T₀ ; convertir en km/h en multipliant les m/s par 3,6.

**Une situation à retenir** : plus la suspension est amortie (amortisseurs), plus h est grand, et plus la résonance est floue : les secousses restent faibles même près de v_c.
:::

::: propriete
**Ce qui reste vrai** — La résonance se cherche (caisse d'un violon, baie où la marée est amplifiée : période propre voisine de 12 h) ou s'évite (pont, rotor mal équilibré d'une machine, carrosserie qui vibre : masselotte de plomb sur la jante, amortisseurs). À vitesse très faible, la voiture suit le profil de la route sans être secouée ; à vitesse très grande, les secousses sont trop rapides pour que la caisse réagisse. Cas limite : dans l'approximation T = T₀, v_c ne dépend ni de F_m ni de h, seulement de d, m et k.
:::

::: verifie À toi : un autre véhicule
Un camion de 4000 kg, dont la suspension a pour raideur k = 1,6 × 10⁵ N/m, roule sur une piste dont les bosses sont espacées de 8,0 m. Calculer T₀, puis la vitesse critique en m/s et en km/h.

---

T₀ = 2π√(m/k) = 2π√(4000 / 1,6 × 10⁵) = 2π × 0,158 = 0,993 s. La résonance a lieu pour d/v_c = T₀, donc v_c = 8,0 / 0,993 = 8,05 m/s, soit 8,05 × 3,6 = 29 km/h.
:::

::: retenir
La voiture est la plus secouée quand T = d/v = T₀ = 2π√(m/k), soit v_c = d/T₀ ; les amortisseurs rendent la résonance floue.
:::

> 🏆 Quête franchie, héros ! Tu sais lire un enregistrement forcé, écrire et tester l'équation du pendule, calculer l'amplitude et l'impédance, situer la résonance d'élongation sous N₀ et celle de vitesse en N₀, juger l'effet de l'amortissement, chiffrer une puissance et trouver la vitesse critique d'un véhicule. Les chapitres suivants quittent les oscillateurs pour les ondes.
