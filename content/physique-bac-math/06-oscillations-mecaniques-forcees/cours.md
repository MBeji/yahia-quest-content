# 🎢 Les oscillations mécaniques forcées — quand le moteur impose sa cadence

> 💡 «Un pendule qu'on abandonne oscille à sa façon, puis s'arrête ; poussé en cadence par un moteur, il oscille à la façon du moteur, et, si la cadence est juste, il se déchaîne.»

Au chapitre précédent, un pendule élastique oscillait librement : à sa période propre T₀ = 2π√(m/k), puis de plus en plus faiblement à cause des frottements. Attache maintenant l'extrémité de son ressort à un excentrique entraîné par un moteur : les oscillations ne s'éteignent plus, et leur amplitude dépend de la fréquence du moteur jusqu'à devenir très grande pour une fréquence précise. Huit notions racontent cela : le régime forcé, l'équation différentielle établie par la relation fondamentale de la dynamique, la construction de Fresnel (amplitude et retard de phase), la résonance d'élongation, l'influence de l'amortissement, l'impédance mécanique et la résonance de vitesse, la puissance moyenne, puis la vitesse critique d'un véhicule. On suppose acquis le pendule élastique libre et amorti (fréquence propre N₀, frottement visqueux f = −h·v), la représentation de Fresnel d'une grandeur sinusoïdale et le circuit RLC forcé du chapitre 4, dont on réutilise l'analogie.

## 🎛️ Les oscillations forcées : excitateur et résonateur

Un palet de masse m = 0,100 kg, relié à un ressort de raideur k = 6,5 N/m, glisse sur un banc à coussin d'air. Lâché seul, il oscille à sa fréquence propre N₀ et s'arrête peu à peu. On fixe maintenant l'autre bout du ressort à un excentrique entraîné par un moteur qui tourne à 1,5 tour par seconde : l'excentrique pousse et tire sans cesse l'extrémité B du ressort.
Le palet oscille-t-il à N₀ ou au rythme du moteur, et pendant combien de temps ?

::: definition
**Régime forcé** — Le moteur à excentrique, qui apporte périodiquement de l'énergie et impose sa fréquence N, est l'**excitateur**. Le système {palet, ressort}, contraint d'osciller à cette fréquence, est le **résonateur**. En régime permanent, les oscillations ne s'amortissent plus : elles sont **forcées**, sinusoïdales et de même fréquence N que l'excitateur. Avec ω = 2πN :

$$ x(t) = X_m sin(ωt + φ) $$
:::

::: figure Le moteur à excentrique impose le mouvement du point B, extrémité du ressort : le moteur est l'excitateur, le système {ressort, palet S} est le résonateur, et x mesure la position du palet par rapport à O
<svg viewBox="0 0 340 174"><title>Pendule élastique horizontal sur banc à coussin d'air : un moteur à excentrique impose le mouvement de l'extrémité B du ressort, le palet S suit</title><line x1="20" y1="118" x2="320" y2="118" stroke="#94a3b8" stroke-width="2" stroke-linecap="round"/><circle cx="30" cy="123" r="1.6" fill="#94a3b8"/><circle cx="50" cy="123" r="1.6" fill="#94a3b8"/><circle cx="70" cy="123" r="1.6" fill="#94a3b8"/><circle cx="90" cy="123" r="1.6" fill="#94a3b8"/><circle cx="110" cy="123" r="1.6" fill="#94a3b8"/><circle cx="130" cy="123" r="1.6" fill="#94a3b8"/><circle cx="150" cy="123" r="1.6" fill="#94a3b8"/><circle cx="170" cy="123" r="1.6" fill="#94a3b8"/><circle cx="190" cy="123" r="1.6" fill="#94a3b8"/><circle cx="210" cy="123" r="1.6" fill="#94a3b8"/><circle cx="230" cy="123" r="1.6" fill="#94a3b8"/><circle cx="250" cy="123" r="1.6" fill="#94a3b8"/><circle cx="270" cy="123" r="1.6" fill="#94a3b8"/><circle cx="290" cy="123" r="1.6" fill="#94a3b8"/><circle cx="310" cy="123" r="1.6" fill="#94a3b8"/><circle cx="52" cy="70" r="26" fill="#ffffff" stroke="#0f172a" stroke-width="1.8"/><text x="52" y="66" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">M</text><circle cx="66" cy="78" r="4" fill="#0f6e56"/><line x1="66" y1="78" x2="118" y2="100" stroke="#0f6e56" stroke-width="2" stroke-linecap="round"/><circle cx="118" cy="100" r="3.5" fill="#0f172a"/><text x="118" y="92" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">B</text><polyline points="118,100 132,91 144,109 156,91 168,109 180,91 192,109 204,91 216,109 226,100" fill="none" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round"/><rect x="226" y="84" width="40" height="32" fill="#ffffff" stroke="#0f172a" stroke-width="1.8"/><text x="246" y="104" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">S</text><line x1="246" y1="56" x2="246" y2="82" stroke="#0f172a" stroke-width="1.2" stroke-dasharray="3 3" stroke-linecap="round"/><line x1="246" y1="56" x2="306" y2="56" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><polygon points="312,56 304,52 304,60" fill="#0f172a"/><text x="312" y="52" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x</text><text x="246" y="48" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">O</text><line x1="24" y1="148" x2="132" y2="148" stroke="#0f6e56" stroke-width="2" stroke-linecap="round"/><line x1="24" y1="142" x2="24" y2="148" stroke="#0f6e56" stroke-width="2" stroke-linecap="round"/><line x1="132" y1="142" x2="132" y2="148" stroke="#0f6e56" stroke-width="2" stroke-linecap="round"/><text x="78" y="166" text-anchor="middle" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">excitateur</text><line x1="148" y1="148" x2="270" y2="148" stroke="#b45309" stroke-width="2" stroke-linecap="round"/><line x1="148" y1="142" x2="148" y2="148" stroke="#b45309" stroke-width="2" stroke-linecap="round"/><line x1="270" y1="142" x2="270" y2="148" stroke="#b45309" stroke-width="2" stroke-linecap="round"/><text x="209" y="166" text-anchor="middle" font-size="12" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">résonateur</text></svg>
:::

Sur la figure, le point vert est l'excentrique : en tournant, il pousse et tire B, donc le ressort ; c'est ce mouvement imposé qui entretient l'oscillation du palet.

::: figure Enregistrement x(t) du palet en régime permanent, à partir d'un instant pris pour t = 0 : amplitude 3,0 cm, trois oscillations complètes en 2,0 s ; le point orange marque x(0) = +2,6 cm, avec x croissant
<svg viewBox="0 0 340 214"><title>Enregistrement x(t) en régime permanent : sinusoïde d'amplitude 3 cm, trois oscillations complètes en 2 s, qui vaut +2,6 cm à t = 0 en croissant</title><line x1="54" y1="163.3" x2="322" y2="163.3" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/><line x1="54" y1="142.2" x2="322" y2="142.2" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/><line x1="54" y1="121.1" x2="322" y2="121.1" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/><line x1="54" y1="78.9" x2="322" y2="78.9" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/><line x1="54" y1="57.8" x2="322" y2="57.8" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/><line x1="54" y1="36.7" x2="322" y2="36.7" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/><line x1="121" y1="176" x2="121" y2="24" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/><line x1="188" y1="176" x2="188" y2="24" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/><line x1="255" y1="176" x2="255" y2="24" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/><line x1="322" y1="176" x2="322" y2="24" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/><line x1="54" y1="100" x2="324" y2="100" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><polygon points="330,100 322,96 322,104" fill="#0f172a"/><line x1="54" y1="176" x2="54" y2="22" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><polygon points="54,16 50,24 58,24" fill="#0f172a"/><line x1="121" y1="97" x2="121" y2="103" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><text x="121" y="190" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0,5</text><line x1="188" y1="97" x2="188" y2="103" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><text x="188" y="190" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><line x1="255" y1="97" x2="255" y2="103" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><text x="255" y="190" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1,5</text><line x1="322" y1="97" x2="322" y2="103" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><text x="322" y="190" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><line x1="51" y1="163.3" x2="54" y2="163.3" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><text x="47" y="167.3" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−3</text><line x1="51" y1="142.2" x2="54" y2="142.2" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><text x="47" y="146.2" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−2</text><line x1="51" y1="121.1" x2="54" y2="121.1" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><text x="47" y="125.1" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">−1</text><line x1="51" y1="78.9" x2="54" y2="78.9" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><text x="47" y="82.9" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">+1</text><line x1="51" y1="57.8" x2="54" y2="57.8" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><text x="47" y="61.8" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">+2</text><line x1="51" y1="36.7" x2="54" y2="36.7" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><text x="47" y="40.7" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">+3</text><text x="320" y="206" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">t (s)</text><text x="62" y="20" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x (cm)</text><polyline points="54,45.2 55.5,42.1 57,39.8 58.5,38.1 60,37 61.4,36.7 62.9,37 64.4,38.1 65.9,39.8 67.4,42.1 68.9,45.2 70.4,48.8 71.9,52.9 73.4,57.6 74.8,62.8 76.3,68.3 77.8,74.2 79.3,80.4 80.8,86.8 82.3,93.4 83.8,100 85.3,106.6 86.8,113.2 88.2,119.6 89.7,125.8 91.2,131.7 92.7,137.2 94.2,142.4 95.7,147.1 97.2,151.2 98.7,154.8 100.2,157.9 101.6,160.2 103.1,161.9 104.6,163 106.1,163.3 107.6,163 109.1,161.9 110.6,160.2 112.1,157.9 113.6,154.8 115,151.2 116.5,147.1 118,142.4 119.5,137.2 121,131.7 122.5,125.8 124,119.6 125.5,113.2 127,106.6 128.4,100 129.9,93.4 131.4,86.8 132.9,80.4 134.4,74.2 135.9,68.3 137.4,62.8 138.9,57.6 140.4,52.9 141.8,48.8 143.3,45.2 144.8,42.1 146.3,39.8 147.8,38.1 149.3,37 150.8,36.7 152.3,37 153.8,38.1 155.2,39.8 156.7,42.1 158.2,45.2 159.7,48.8 161.2,52.9 162.7,57.6 164.2,62.8 165.7,68.3 167.2,74.2 168.6,80.4 170.1,86.8 171.6,93.4 173.1,100 174.6,106.6 176.1,113.2 177.6,119.6 179.1,125.8 180.6,131.7 182,137.2 183.5,142.4 185,147.1 186.5,151.2 188,154.8 189.5,157.9 191,160.2 192.5,161.9 194,163 195.4,163.3 196.9,163 198.4,161.9 199.9,160.2 201.4,157.9 202.9,154.8 204.4,151.2 205.9,147.1 207.4,142.4 208.8,137.2 210.3,131.7 211.8,125.8 213.3,119.6 214.8,113.2 216.3,106.6 217.8,100 219.3,93.4 220.8,86.8 222.2,80.4 223.7,74.2 225.2,68.3 226.7,62.8 228.2,57.6 229.7,52.9 231.2,48.8 232.7,45.2 234.2,42.1 235.6,39.8 237.1,38.1 238.6,37 240.1,36.7 241.6,37 243.1,38.1 244.6,39.8 246.1,42.1 247.6,45.2 249,48.8 250.5,52.9 252,57.6 253.5,62.8 255,68.3 256.5,74.2 258,80.4 259.5,86.8 261,93.4 262.4,100 263.9,106.6 265.4,113.2 266.9,119.6 268.4,125.8 269.9,131.7 271.4,137.2 272.9,142.4 274.4,147.1 275.8,151.2 277.3,154.8 278.8,157.9 280.3,160.2 281.8,161.9 283.3,163 284.8,163.3 286.3,163 287.8,161.9 289.2,160.2 290.7,157.9 292.2,154.8 293.7,151.2 295.2,147.1 296.7,142.4 298.2,137.2 299.7,131.7 301.2,125.8 302.6,119.6 304.1,113.2 305.6,106.6 307.1,100 308.6,93.4 310.1,86.8 311.6,80.4 313.1,74.2 314.6,68.3 316,62.8 317.5,57.6 319,52.9 320.5,48.8 322,45.2" fill="none" stroke="#1d4ed8" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"/><circle cx="54" cy="45.2" r="4" fill="#b45309"/><line x1="61.4" y1="32" x2="150.8" y2="32" stroke="#0f6e56" stroke-width="1.8" stroke-linecap="round"/><line x1="61.4" y1="28" x2="61.4" y2="36" stroke="#0f6e56" stroke-width="1.8" stroke-linecap="round"/><line x1="150.8" y1="28" x2="150.8" y2="36" stroke="#0f6e56" stroke-width="1.8" stroke-linecap="round"/><text x="106.1" y="26" text-anchor="middle" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">T</text></svg>
:::

Sur la figure, l'amplitude X_m se lit de l'axe t à une crête, la période T entre deux crêtes consécutives, et la phase φ se déduit de la valeur de x à t = 0 et du sens de variation de la courbe.

::: exemple Lire l'enregistrement et écrire x(t) (m = 0,100 kg ; k = 6,5 N/m ; moteur à 1,5 tr/s)

1. Entre t = 0 et t = 2,0 s, la courbe compte 3 oscillations complètes : T = 2,0 / 3 = 0,67 s et N = 1/T = 1,5 Hz, c'est la fréquence du moteur, 1,5 tr/s.
2. N₀ = (1/2π)√(k/m) = (1/2π)√(6,5/0,100) = 8,06/6,28 = 1,28 Hz. Comme N ≠ N₀, le palet n'oscille pas librement : ce sont des oscillations forcées.
3. L'amplitude se lit de l'axe à la crête : X_m = 3,0 cm = 3,0 × 10⁻² m.
4. À t = 0, x = X_m sin φ = +2,6 cm, donc sin φ = 2,6/3,0 = 0,87 : φ = π/3 ou 2π/3. La courbe est croissante à t = 0 (cos φ > 0), donc φ = π/3 rad.
5. ω = 2πN = 3π = 9,42 rad/s, d'où x(t) = 3,0 × 10⁻² sin(9,42 t + π/3), x en mètre.

:::

::: piege
**Erreur : croire que le palet oscille à sa fréquence propre N₀.** L'enregistrement donne N = 1,5 Hz (étape 1), alors que N₀ = 1,28 Hz (étape 2). L'erreur tente parce qu'un pendule abandonné à lui-même oscille à N₀. Mais en régime forcé la fréquence est celle de l'excitateur : N₀ n'intervient plus que dans l'amplitude.
:::

::: propriete
**Ce qui reste vrai** — En régime permanent, x(t) a la fréquence N de l'excitateur, quels que soient m, k et le frottement ; seules l'amplitude X_m et la phase φ dépendent du pendule. Une fréquence en tr/min se convertit en Hz en divisant par 60. Cas limite : si N est égale à N₀, les oscillations restent forcées, et c'est au voisinage de N₀ que l'amplitude devient grande (maximum de X_m à N_r, un peu en dessous de N₀ ; maximum de V_m exactement à N₀ : notions 4 et 6).
:::

::: verifie À toi : un autre enregistrement
Avec le même palet, le moteur est réglé sur une autre fréquence. L'enregistrement donne une sinusoïde d'amplitude 4,0 cm qui vaut +2,0 cm à t = 0 en décroissant, avec 6 oscillations complètes en 5,0 s. Donner N, la phase φ et x(t) ; les oscillations sont-elles forcées ?

---

Six périodes en 5,0 s donnent T = 5,0/6 = 0,83 s, donc N = 1,2 Hz. À t = 0, sin φ = 2,0/4,0 = 1/2 et la courbe décroît (cos φ < 0), donc φ = 5π/6 rad. Avec ω = 2πN = 2,4π = 7,54 rad/s, x(t) = 4,0 × 10⁻² sin(7,54 t + 5π/6). N = 1,2 Hz est la fréquence du moteur et diffère de N₀ = 1,28 Hz : les oscillations sont forcées.
:::

::: retenir
Le moteur (excitateur) impose sa fréquence N au pendule (résonateur) : en régime permanent x = X_m sin(2πNt + φ), à la fréquence N et non à N₀.
:::

## 🧮 L'équation différentielle établie par la relation fondamentale de la dynamique

Garde le même palet (m = 0,100 kg ; k = 6,5 N/m) et fixe-lui une plaque qui le freine : le frottement est visqueux, f = −h·v avec h = 0,60 kg/s (valeur d'illustration). L'extrémité B du ressort est toujours imposée par l'excentrique, qui la déplace de x_B = (X_B)_m sin ωt avec (X_B)_m = 2,0 cm (valeur d'illustration).
Que donne la relation fondamentale de la dynamique appliquée au palet, et que devient l'excitateur dans l'équation obtenue ?

::: definition
**Équation du pendule forcé** — Dans le repère galiléen (O, i), lié au laboratoire, O étant la position de repos du palet, les forces sur le palet sont : le poids P et la réaction R du coussin d'air, qui se compensent ; la tension T du ressort ; le frottement f = −h·v. Comme B se déplace, le ressort est allongé de x − x_B, donc T = −k(x − x_B). La relation fondamentale de la dynamique, projetée sur l'axe, s'écrit m·a = T + f, soit :

$$ m·d²x/dt² + h·dx/dt + k·x = k·x_B $$

Le second membre a la dimension d'une force : tout se passe comme si le palet recevait la force excitatrice F = k·x_B = F_m sin ωt, avec F_m = k·(X_B)_m. L'équation du régime forcé est :

$$ m·d²x/dt² + h·dx/dt + k·x = F_m sin ωt $$

Elle admet une solution particulière sinusoïdale x = X_m sin(ωt + φ), à la pulsation ω de l'excitateur : c'est le régime permanent observé.
:::

::: figure Forces sur le palet S à l'instant de l'exemple, où il se déplace vers les x positifs avec la vitesse v : la tension T du ressort (vert, 0,0975 N) et le frottement f (orange, 0,090 N) pointent tous deux vers les x négatifs, alors que le poids P et la réaction R se compensent
<svg viewBox="0 0 340 176"><title>Forces sur le palet S : le poids P et la réaction R se compensent ; la tension T du ressort et le frottement f pointent tous deux vers les x négatifs alors que la vitesse v est vers les x positifs</title><line x1="60" y1="112" x2="322" y2="112" stroke="#94a3b8" stroke-width="2" stroke-linecap="round"/><rect x="170" y="72" width="64" height="40" fill="#ffffff" stroke="#0f172a" stroke-width="1.8"/><text x="202" y="97" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">S</text><polyline points="34,92 46,92 54,80 66,104 78,80 90,104 102,80 114,104 126,80 138,104 150,92 170,92" fill="none" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round"/><circle cx="34" cy="92" r="3.5" fill="#0f172a"/><text x="34" y="80" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">B</text><line x1="170" y1="80" x2="111.4" y2="80" stroke="#0f6e56" stroke-width="2.6" stroke-linecap="round"/><polygon points="105,80 113,76.4 113,83.6" fill="#0f6e56"/><text x="150" y="66" text-anchor="middle" font-size="13" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">T</text><line x1="170" y1="106" x2="116.4" y2="106" stroke="#b45309" stroke-width="2.6" stroke-linecap="round"/><polygon points="110,106 118,102.4 118,109.6" fill="#b45309"/><text x="140" y="124" text-anchor="middle" font-size="13" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">f</text><line x1="190" y1="92" x2="190" y2="145.6" stroke="#0f172a" stroke-width="2.2" stroke-linecap="round"/><polygon points="190,152 186.4,144 193.6,144" fill="#0f172a"/><text x="180" y="150" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">P</text><line x1="214" y1="92" x2="214" y2="38.4" stroke="#0f172a" stroke-width="2.2" stroke-linecap="round"/><polygon points="214,32 217.6,40 210.4,40" fill="#0f172a"/><text x="224" y="40" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">R</text><line x1="246" y1="92" x2="283.6" y2="92" stroke="#1d4ed8" stroke-width="2.4" stroke-linecap="round"/><polygon points="290,92 282,95.6 282,88.4" fill="#1d4ed8"/><text x="268" y="84" text-anchor="middle" font-size="13" font-weight="700" fill="#1d4ed8" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">v</text><line x1="250" y1="148" x2="299.6" y2="148" stroke="#0f172a" stroke-width="1.8" stroke-linecap="round"/><polygon points="306,148 298,151.6 298,144.4" fill="#0f172a"/><text x="310" y="142" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">i</text><text x="250" y="164" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">O</text><line x1="250" y1="138" x2="250" y2="148" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/></svg>
:::

Sur la figure, la tension T et le frottement f s'opposent au déplacement de S ; P et R, verticaux et de même norme, ne contribuent pas à l'équation sur l'axe.

::: exemple Forces, accélération et équation à un instant (m = 0,100 kg ; k = 6,5 N/m ; h = 0,60 kg/s ; (X_B)_m = 2,0 cm)

1. Sur l'axe (O, i), il ne reste que la tension T et le frottement f, puisque P et R se compensent.
2. À un instant, x = +2,0 cm, x_B = +0,50 cm et v = +0,15 m/s. Le ressort est allongé de x − x_B = 1,5 cm, donc T = −k(x − x_B) = −6,5 × 0,015 = −0,0975 N, et f = −h·v = −0,60 × 0,15 = −0,090 N.
3. La relation m·a = T + f donne a = (−0,0975 − 0,090)/0,100 = −1,9 m/s².
4. Contrôle : m·a + h·v + k·x = −0,1875 + 0,090 + 0,130 = +0,0325 N, égal à k·x_B = 6,5 × 0,0050 = 0,0325 N ✓. Le second membre est bien k·x_B, et il n'est pas nul.
5. Avec (X_B)_m = 2,0 cm, la valeur maximale de la force excitatrice est F_m = k·(X_B)_m = 6,5 × 0,020 = 0,13 N ; à cet instant, F = 0,0325 N.

:::

::: piege
**Erreur : écrire T = −k·x, comme si l'extrémité B du ressort était fixe.** Dans l'exemple, on trouverait T = −6,5 × 0,020 = −0,13 N au lieu de −0,0975 N (étape 2), et l'équation m·x″ + h·x′ + k·x = 0 des oscillations libres amorties. L'erreur tente parce que, pour un ressort fixé, la tension est −k·x. Mais ici B se déplace : le ressort est allongé de x − x_B, et c'est le terme k·x_B qui apporte l'énergie.
:::

::: propriete
**Ce qui reste vrai** — Le second membre est une force sinusoïdale F = k·x_B, de pulsation ω = 2πN et d'amplitude F_m = k·(X_B)_m : plus l'excentrique déplace B, plus la force est grande. La solution de régime permanent a la pulsation ω de l'excitateur, et non la pulsation propre ω₀ = √(k/m). Cas limite : si B est immobile (x_B = 0), la force est nulle et on retrouve l'équation des oscillations libres amorties, dont la solution s'éteint.
:::

::: verifie À toi : un autre instant
Même pendule. À un autre instant, x_B = −1,5 cm, x = +0,50 cm et v = −0,10 m/s. Calculer T, f, puis l'accélération a.

---

Le ressort est allongé de x − x_B = 0,50 − (−1,5) = 2,0 cm, donc T = −6,5 × 0,020 = −0,13 N. Le frottement vaut f = −0,60 × (−0,10) = +0,060 N. Alors a = (T + f)/m = (−0,13 + 0,060)/0,100 = −0,70 m/s². Contrôle : m·a + h·v + k·x = −0,070 − 0,060 + 0,0325 = −0,0975 N = k·x_B = 6,5 × (−0,015) ✓.
:::

::: retenir
La relation fondamentale de la dynamique donne m·d²x/dt² + h·dx/dt + k·x = k·x_B = F_m sin ωt, avec F_m = k·(X_B)_m ; le second membre n'est pas nul.
:::

## 📐 La construction de Fresnel : amplitude et retard de phase

Même palet, même plaque (m = 0,100 kg ; k = 6,5 N/m ; h = 0,60 kg/s) et F_m = 0,13 N. On règle le moteur sur ω = 5,0 rad/s (N = 0,80 Hz). L'enregistrement est sinusoïdal à cette pulsation, mais on ne connaît ni son amplitude ni sa phase.
Comment les calculer à partir de l'équation différentielle, et que dire de la phase de x par rapport à la force excitatrice ?

::: definition
**Amplitude et retard de phase** — Prenons l'origine des temps sur la force, F = F_m sin ωt, et x = X_m sin(ωt + φ) ; alors v = dx/dt = X_m ω sin(ωt + φ + π/2) et a = d²x/dt² = X_m ω² sin(ωt + φ + π). L'équation différentielle devient la somme de trois sinusoïdes égale à F, que la construction de Fresnel représente par les vecteurs OA₁ (norme kX_m, angle φ), OA₂ (norme hωX_m, angle φ + π/2), OA₃ (norme mω²X_m, angle φ + π) et OA (norme F_m, angle 0) :

$$ OA₁ + OA₂ + OA₃ = OA $$

OA₁ et OA₃ sont opposés et OA₂ leur est perpendiculaire : le théorème de Pythagore donne F_m² = (k − mω²)²X_m² + h²ω²X_m², d'où :

$$ X_m = F_m / √(h²ω² + (k − mω²)²) $$

et le déphasage φ de x par rapport à F vérifie cos φ = (k − mω²)·X_m / F_m et sin φ = −hω·X_m / F_m, soit tan φ = hω / (mω² − k).
:::

::: figure Construction de Fresnel pour m = 0,100 kg, k = 6,5 N/m, h = 0,60 kg/s, F_m = 0,13 N et ω = 5,0 rad/s : les trois vecteurs mis bout à bout (kX_m = 0,169 N, hωX_m = 0,078 N, mω²X_m = 0,065 N) se referment sur F_m, horizontal, et φ est l'angle entre kX_m et l'horizontale
<svg viewBox="0 0 340 190"><title>Construction de Fresnel d'un pendule forcé : trois vecteurs kXm, hωXm et mω²Xm mis bout à bout se referment sur Fm, horizontal ; l'angle φ entre kXm et l'horizontale est sous celle-ci</title><line x1="16" y1="58" x2="239" y2="58" stroke="#94a3b8" stroke-width="1.4" stroke-dasharray="4 4" stroke-linecap="round"/><line x1="36" y1="58" x2="179" y2="165.2" stroke="#1d4ed8" stroke-width="2.6" stroke-linecap="round"/><polygon points="184.7,169.5 175.1,167.4 180,160.9" fill="#1d4ed8"/><line x1="184.7" y1="169.5" x2="231.9" y2="106.7" stroke="#b45309" stroke-width="2.6" stroke-linecap="round"/><polygon points="236.2,100.9 234,110.5 227.6,105.7" fill="#b45309"/><line x1="236.2" y1="100.9" x2="184.8" y2="62.3" stroke="#0f6e56" stroke-width="2.6" stroke-linecap="round"/><polygon points="179,58 188.6,60.2 183.8,66.6" fill="#0f6e56"/><line x1="36" y1="58" x2="171" y2="58" stroke="#0f172a" stroke-width="3.2" stroke-linecap="round"/><polygon points="179,58 169,62.5 169,53.5" fill="#0f172a"/><text x="104.4" y="129.8" text-anchor="end" font-size="12" font-weight="700" fill="#1d4ed8" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">kXm</text><text x="216.5" y="145.2" text-anchor="start" font-size="12" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">hωXm</text><text x="217.6" y="77.5" text-anchor="start" font-size="12" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">mω²Xm</text><text x="107.5" y="49" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Fm</text><polyline points="70,58 70,59.1 69.9,60.2 69.8,61.3 69.7,62.4 69.6,63.4 69.4,64.5 69.1,65.6 68.9,66.7 68.6,67.7 68.3,68.8 67.9,69.8 67.5,70.8 67.1,71.8 66.6,72.8 66.1,73.8 65.6,74.7 65,75.7 64.5,76.6 63.8,77.5 63.2,78.4" fill="none" stroke="#0f172a" stroke-width="1.4" stroke-linejoin="round" stroke-linecap="round"/><text x="86" y="72" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">φ</text><circle cx="36" cy="58" r="3.5" fill="#0f172a"/><text x="28" y="52" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">O</text><text x="187" y="50" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">A</text></svg>
:::

Sur la figure, le vecteur kX_m, plus long que mω²X_m, domine : il est sous l'horizontale, donc φ est négatif. Le vecteur hωX_m est perpendiculaire aux deux autres.

| Pulsation | Vecteur dominant | Déphasage φ de x par rapport à F |
| --- | --- | --- |
| ω < ω₀ (k > mω²) | kX_m | −π/2 < φ < 0 |
| ω = ω₀ (k = mω²) | aucun : ils se compensent | φ = −π/2 |
| ω > ω₀ (k < mω²) | mω²X_m | −π < φ < −π/2 |

Dans le tableau, φ est négatif dans les trois lignes : x est en retard de phase sur la force, d'autant plus que la fréquence est grande.

::: exemple Calculer X_m et φ pour ω = 5,0 rad/s, puis pour ω = 10 rad/s (m = 0,100 kg ; k = 6,5 N/m ; h = 0,60 kg/s ; F_m = 0,13 N)

1. Pour ω = 5,0 rad/s : h·ω = 0,60 × 5,0 = 3,0 N/m et m·ω² = 0,100 × 25 = 2,5 N/m, donc k − mω² = 6,5 − 2,5 = 4,0 N/m. On a ω < ω₀ = √(k/m) = 8,06 rad/s.
2. X_m = F_m / √(3,0² + 4,0²) = 0,13 / 5,0 = 2,6 × 10⁻² m = 2,6 cm : un triangle de côtés 3, 4 et 5.
3. cos φ = (k − mω²)·X_m / F_m = 4,0 × 0,026 / 0,13 = 0,80 et sin φ = −hω·X_m / F_m = −3,0 × 0,026 / 0,13 = −0,60, donc φ = −0,64 rad (−37°) : on est bien dans l'intervalle −π/2 < φ < 0.
4. Contrôle des vecteurs : kX_m = 0,169 N, hωX_m = 0,078 N et mω²X_m = 0,065 N ; leur projection sur l'axe des phases vaut 0,169 × 0,80 + 0,078 × 0,60 − 0,065 × 0,80 = 0,130 N = F_m ✓.
5. Pour ω = 10 rad/s (ω > ω₀) : h·ω = 6,0 N/m et k − mω² = 6,5 − 10 = −3,5 N/m, donc X_m = 0,13 / √(6,0² + 3,5²) = 0,13 / 6,95 = 1,9 cm, cos φ = −0,50 et sin φ = −0,86 : φ = −2,10 rad (−120°), dans l'intervalle −π < φ < −π/2.

:::

::: piege
**Erreur : additionner les termes comme des nombres, X_m = F_m / (hω + k − mω²).** Dans l'exemple, cela donnerait 0,13 / (3,0 + 4,0) = 1,9 cm au lieu de 2,6 cm (étape 2). L'erreur tente parce que les deux termes sont en N/m. Mais les forces de frottement et de rappel ne sont pas en phase : leurs vecteurs de Fresnel sont perpendiculaires, et ils se composent par Pythagore.
:::

::: propriete
**Ce qui reste vrai** — Pour h > 0, sin φ = −hω·X_m / F_m est négatif : φ est compris entre −π et 0, et x est en retard de phase sur la force excitatrice à toute fréquence. Aux basses fréquences φ est proche de 0 (x presque en phase avec F), aux hautes fréquences proche de −π (presque en opposition). Cas limite : à ω = ω₀, k − mω² = 0, donc φ = −π/2 et X_m = F_m/(h·ω₀), quelle que soit la valeur de h.
:::

::: verifie À toi : un autre pendule
m = 0,20 kg, k = 15 N/m, h = 1,2 kg/s, F_m = 0,65 N, ω = 10 rad/s. Calculer X_m, cos φ et sin φ, puis dire dans quel intervalle se trouve φ.

---

h·ω = 12 N/m et k − mω² = 15 − 20 = −5,0 N/m, donc X_m = 0,65 / √(12² + 5,0²) = 0,65 / 13 = 5,0 × 10⁻² m = 5,0 cm. Alors cos φ = −5,0 × 0,050 / 0,65 = −0,38 et sin φ = −12 × 0,050 / 0,65 = −0,92. Comme ω = 10 rad/s dépasse ω₀ = √75 = 8,7 rad/s, φ est dans l'intervalle −π < φ < −π/2 : φ = −1,97 rad.
:::

::: retenir
Fresnel compose kX_m, hωX_m et mω²X_m : X_m = F_m / √(h²ω² + (k − mω²)²), et x est en retard de phase sur F (φ < 0), de −π/2 exactement à ω = ω₀.
:::

## 📈 La résonance d'élongation

Fais croître la fréquence du moteur de 0 à 2 Hz sur ce pendule (m = 0,100 kg ; k = 6,5 N/m ; h = 0,60 kg/s ; F_m = 0,13 N). À très basse fréquence, le ressort est tiré lentement et X_m ≈ F_m/k = 2,0 cm. Puis l'amplitude grandit, passe par un maximum, et retombe.
Où se trouve ce maximum : à la fréquence propre N₀, ou ailleurs ?

::: definition
**Résonance d'élongation** — L'amplitude X_m est maximale quand le dénominateur √(h²ω² + (k − mω²)²) est minimal, c'est-à-dire quand sa dérivée par rapport à ω s'annule : 2h²ω − 4mω(k − mω²) = 0. Comme ω ≠ 0, cela donne h² = 2m(k − mω²), d'où ω_r² = ω₀² − h²/(2m²). La fréquence de l'excitateur pour laquelle X_m est maximale, appelée **fréquence de résonance**, est légèrement inférieure à la fréquence propre N₀ = (1/2π)√(k/m) :

$$ N_r = √(N₀² − h²/(8π²m²)) $$

Cette résonance n'existe que si h² < 2mk, c'est-à-dire h < h_l = m·ω₀·√2 = √(2mk) ; sinon le radicande n'est pas positif.
:::

::: figure Courbe X_m(N) pour m = 0,100 kg, k = 6,5 N/m, h = 0,60 kg/s et F_m = 0,13 N : le maximum (point orange) est à N_r = 1,09 Hz, à gauche de N₀ = 1,28 Hz (pointillés noirs) ; la courbe part de F_m/k = 2,0 cm
<svg viewBox="0 0 340 226"><title>Courbe de résonance d'élongation Xm(N) pour m = 0,100 kg, k = 6,5 N/m, h = 0,60 kg/s et Fm = 0,13 N : le maximum, à Nr = 1,09 Hz, est à gauche de N0 = 1,28 Hz ; la courbe part de Fm/k = 2,0 cm</title><line x1="54" y1="134.6" x2="324" y2="134.6" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/><line x1="54" y1="91.1" x2="324" y2="91.1" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/><line x1="54" y1="47.7" x2="324" y2="47.7" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/><line x1="121.5" y1="178" x2="121.5" y2="26" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/><line x1="189" y1="178" x2="189" y2="26" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/><line x1="256.5" y1="178" x2="256.5" y2="26" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/><line x1="324" y1="178" x2="324" y2="26" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/><line x1="54" y1="178" x2="326" y2="178" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><polygon points="332,178 324,174 324,182" fill="#0f172a"/><line x1="54" y1="178" x2="54" y2="24" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><polygon points="54,18 50,26 58,26" fill="#0f172a"/><line x1="121.5" y1="175" x2="121.5" y2="181" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><text x="121.5" y="192" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0,5</text><line x1="189" y1="175" x2="189" y2="181" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><text x="189" y="192" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1,0</text><line x1="256.5" y1="175" x2="256.5" y2="181" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><text x="256.5" y="192" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1,5</text><line x1="324" y1="175" x2="324" y2="181" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><text x="324" y="192" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2,0</text><line x1="51" y1="134.6" x2="54" y2="134.6" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><text x="47" y="138.6" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><line x1="51" y1="91.1" x2="54" y2="91.1" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><text x="47" y="95.1" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><line x1="51" y1="47.7" x2="54" y2="47.7" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><text x="47" y="51.7" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">3</text><text x="322" y="208" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">N (Hz)</text><text x="62" y="22" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Xm (cm)</text><polyline points="54,91.1 55.7,91.1 57.4,91.1 59.1,91.1 60.8,91 62.4,91 64.1,90.9 65.8,90.9 67.5,90.8 69.2,90.7 70.9,90.5 72.6,90.4 74.2,90.3 75.9,90.1 77.6,90 79.3,89.8 81,89.6 82.7,89.4 84.4,89.2 86.1,89 87.8,88.7 89.4,88.5 91.1,88.2 92.8,87.9 94.5,87.6 96.2,87.3 97.9,87 99.6,86.7 101.2,86.3 102.9,86 104.6,85.6 106.3,85.2 108,84.8 109.7,84.4 111.4,84 113.1,83.5 114.8,83.1 116.4,82.6 118.1,82.1 119.8,81.6 121.5,81.1 123.2,80.6 124.9,80 126.6,79.5 128.2,78.9 129.9,78.3 131.6,77.7 133.3,77.1 135,76.5 136.7,75.8 138.4,75.2 140.1,74.5 141.8,73.8 143.4,73.1 145.1,72.4 146.8,71.7 148.5,70.9 150.2,70.2 151.9,69.4 153.6,68.7 155.2,67.9 156.9,67.2 158.6,66.4 160.3,65.6 162,64.8 163.7,64 165.4,63.3 167.1,62.5 168.8,61.7 170.4,61 172.1,60.2 173.8,59.5 175.5,58.8 177.2,58.1 178.9,57.4 180.6,56.7 182.2,56.1 183.9,55.5 185.6,55 187.3,54.5 189,54 190.7,53.6 192.4,53.2 194.1,52.9 195.8,52.6 197.4,52.4 199.1,52.3 200.8,52.3 202.5,52.3 204.2,52.4 205.9,52.5 207.6,52.8 209.2,53.1 210.9,53.5 212.6,54 214.3,54.5 216,55.2 217.7,55.9 219.4,56.7 221.1,57.6 222.8,58.5 224.4,59.5 226.1,60.6 227.8,61.7 229.5,62.9 231.2,64.1 232.9,65.4 234.6,66.7 236.2,68.1 237.9,69.5 239.6,70.9 241.3,72.4 243,73.9 244.7,75.4 246.4,76.9 248.1,78.4 249.8,79.9 251.4,81.4 253.1,83 254.8,84.5 256.5,86 258.2,87.5 259.9,89 261.6,90.5 263.2,92 264.9,93.4 266.6,94.8 268.3,96.3 270,97.7 271.7,99 273.4,100.4 275.1,101.7 276.8,103 278.4,104.3 280.1,105.6 281.8,106.8 283.5,108.1 285.2,109.3 286.9,110.4 288.6,111.6 290.2,112.7 291.9,113.8 293.6,114.9 295.3,116 297,117 298.7,118 300.4,119 302.1,120 303.8,120.9 305.4,121.8 307.1,122.7 308.8,123.6 310.5,124.5 312.2,125.4 313.9,126.2 315.6,127 317.2,127.8 318.9,128.6 320.6,129.3 322.3,130.1 324,130.8" fill="none" stroke="#1d4ed8" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"/><line x1="227.2" y1="178" x2="227.2" y2="26" stroke="#0f172a" stroke-width="1.4" stroke-dasharray="5 4" stroke-linecap="round"/><text x="232.2" y="36" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">N₀</text><line x1="201.3" y1="178" x2="201.3" y2="52.3" stroke="#b45309" stroke-width="1.4" stroke-dasharray="3 3" stroke-linecap="round"/><circle cx="201.3" cy="52.3" r="4" fill="#b45309"/><text x="195.3" y="43.3" text-anchor="end" font-size="12" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Nr</text><circle cx="54" cy="91.1" r="3.5" fill="#0f6e56"/><text x="62" y="84.1" text-anchor="start" font-size="11" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Fm/k</text></svg>
:::

Sur la figure, le point orange est le maximum de la courbe ; sa position N_r est celle donnée par la formule, et la droite en pointillés repère N₀.

Pour ce pendule, le calcul donne les mesures suivantes (valeurs calculées avec la formule de X_m) :

| N (Hz) | 0 | 0,5 | 0,8 | 1,0 | 1,1 | 1,3 | 1,6 | 2,0 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| X_m (cm) | 2,00 | 2,23 | 2,61 | 2,86 | 2,89 | 2,65 | 1,85 | 1,09 |

Dans le tableau, le plus grand X_m est 2,89 cm, pour N = 1,1 Hz : le maximum se lit entre 1,0 et 1,3 Hz, du côté des fréquences inférieures à N₀.

::: exemple Lire N_r sur le tableau, puis la calculer (m = 0,100 kg ; k = 6,5 N/m ; h = 0,60 kg/s ; F_m = 0,13 N)

1. Lecture : le maximum du tableau est 2,89 cm à N = 1,1 Hz, donc N_r ≈ 1,1 Hz.
2. N₀ = (1/2π)√(k/m) = 8,062/6,283 = 1,283 Hz, d'où N₀² = 1,646 Hz².
3. Condition : h² = 0,36 est inférieur à 2mk = 2 × 0,100 × 6,5 = 1,3 (soit h_l = 1,14 kg/s), donc la résonance d'élongation existe.
4. h²/(8π²m²) = 0,36 / (78,96 × 0,0100) = 0,456 Hz², donc N_r = √(1,646 − 0,456) = √1,190 = 1,09 Hz, en accord avec la lecture, et inférieure à N₀.
5. En N_r, ω_r = 2π × 1,09 = 6,86 rad/s : m·ω_r² = 4,70 N/m, h·ω_r = 4,11 N/m, donc X_m = 0,13 / √(4,11² + 1,80²) = 0,13 / 4,49 = 2,9 cm. En N₀, k − mω₀² = 0 et X_m = F_m/(h·ω₀) = 0,13 / (0,60 × 8,06) = 2,7 cm : plus petite.

:::

::: piege
**Erreur : croire que l'amplitude est maximale à N₀, comme l'intensité du circuit RLC.** Dans l'exemple, X_m vaut 2,7 cm à N₀ et 2,9 cm à N_r (étape 5) : le maximum est à N_r. L'erreur tente parce que « résonance » rappelle la fréquence propre. Mais le terme h²/(8π²m²) décale le maximum de X_m vers les basses fréquences, ici de 0,19 Hz.
:::

::: propriete
**Ce qui reste vrai** — Pour h > 0, N_r < N₀, et l'écart N₀ − N_r grandit avec h ; N_r se rapproche de N₀ quand h diminue. Pour N tendant vers 0, X_m tend vers F_m/k ; pour N très grand, X_m tend vers 0. Cas limite idéal : pour h = 0, N_r = N₀ et X_m deviendrait infinie, ce qu'aucun pendule réel n'atteint puisque les frottements existent toujours. Pour h ≥ h_l, il n'y a plus de maximum : X_m décroît dès N = 0.
:::

::: verifie À toi : une autre fréquence de résonance
m = 0,25 kg, k = 64 N/m, h = 2,0 kg/s. La résonance d'élongation existe-t-elle ? Calculer N₀ et N_r.

---

2mk = 2 × 0,25 × 64 = 32 est plus grand que h² = 4,0 : la résonance existe. ω₀² = k/m = 256 rad²/s², donc ω₀ = 16 rad/s et N₀ = 16/6,283 = 2,55 Hz. Ensuite ω_r² = ω₀² − h²/(2m²) = 256 − 4,0/0,125 = 224, donc ω_r = 14,97 rad/s et N_r = 14,97/6,283 = 2,38 Hz, inférieure à N₀.
:::

::: retenir
X_m est maximale pour N_r = √(N₀² − h²/(8π²m²)), inférieure à N₀, à condition que h² < 2mk.
:::

## 🎚️ L'influence de l'amortissement : résonance aiguë ou floue

Fixe sur le palet une plaque de plus en plus grande, qui freine de plus en plus l'air. Avec une petite plaque, le palet s'emballe nettement près de la bonne fréquence ; avec une très grande, il vibre à peine, quelle que soit la fréquence du moteur.
Comment le coefficient de frottement h transforme-t-il la courbe de résonance ?

::: definition
**Résonance aiguë, résonance floue** — Plus h est faible, plus le pic de X_m(N) est haut et étroit : la résonance est **aiguë**. Plus h est grand, plus le pic est bas et large : la résonance est **floue**, et N_r s'éloigne de N₀. Au-delà de h_l = m·ω₀·√2 = √(2mk), il n'y a plus de maximum : X_m décroît dès N = 0. Avec un amortissement très important, il n'y a plus de résonance et le régime forcé est dit **linéaire**.
:::

::: figure Trois courbes X_m(N) pour m = 0,100 kg, k = 6,5 N/m et F_m = 0,13 N (valeurs d'illustration) : résonance aiguë à h = 0,25 kg/s, floue à h = 0,60 kg/s, absente à h = 1,30 kg/s ; les points marquent les maxima
<svg viewBox="0 0 340 236"><title>Trois courbes de résonance Xm(N) pour m = 0,100 kg, k = 6,5 N/m et Fm = 0,13 N : résonance aiguë à h = 0,25 kg/s, floue à h = 0,60 kg/s, absente à h = 1,30 kg/s</title><line x1="54" y1="144.8" x2="324" y2="144.8" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/><line x1="54" y1="101.6" x2="324" y2="101.6" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/><line x1="54" y1="58.4" x2="324" y2="58.4" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/><line x1="121.5" y1="188" x2="121.5" y2="26" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/><line x1="189" y1="188" x2="189" y2="26" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/><line x1="256.5" y1="188" x2="256.5" y2="26" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/><line x1="324" y1="188" x2="324" y2="26" stroke="#e2e8f0" stroke-width="1" stroke-linecap="round"/><line x1="54" y1="188" x2="326" y2="188" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><polygon points="332,188 324,184 324,192" fill="#0f172a"/><line x1="54" y1="188" x2="54" y2="24" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><polygon points="54,18 50,26 58,26" fill="#0f172a"/><line x1="121.5" y1="185" x2="121.5" y2="191" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><text x="121.5" y="202" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">0,5</text><line x1="189" y1="185" x2="189" y2="191" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><text x="189" y="202" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1,0</text><line x1="256.5" y1="185" x2="256.5" y2="191" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><text x="256.5" y="202" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1,5</text><line x1="324" y1="185" x2="324" y2="191" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><text x="324" y="202" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2,0</text><line x1="51" y1="144.8" x2="54" y2="144.8" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><text x="47" y="148.8" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2</text><line x1="51" y1="101.6" x2="54" y2="101.6" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><text x="47" y="105.6" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4</text><line x1="51" y1="58.4" x2="54" y2="58.4" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><text x="47" y="62.4" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">6</text><text x="322" y="218" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">N (Hz)</text><text x="62" y="22" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Xm (cm)</text><line x1="227.2" y1="188" x2="227.2" y2="26" stroke="#0f172a" stroke-width="1.4" stroke-dasharray="5 4" stroke-linecap="round"/><text x="232.2" y="36" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">N₀</text><polyline points="54,144.8 55.4,144.8 56.7,144.8 58,144.8 59.4,144.8 60.8,144.7 62.1,144.7 63.5,144.7 64.8,144.6 66.2,144.6 67.5,144.5 68.8,144.5 70.2,144.4 71.5,144.4 72.9,144.3 74.2,144.2 75.6,144.2 77,144.1 78.3,144 79.7,143.9 81,143.8 82.3,143.7 83.7,143.6 85,143.4 86.4,143.3 87.8,143.2 89.1,143 90.5,142.9 91.8,142.8 93.2,142.6 94.5,142.4 95.8,142.3 97.2,142.1 98.6,141.9 99.9,141.7 101.2,141.5 102.6,141.3 104,141.1 105.3,140.9 106.7,140.7 108,140.4 109.3,140.2 110.7,139.9 112,139.7 113.4,139.4 114.8,139.1 116.1,138.8 117.4,138.5 118.8,138.2 120.2,137.9 121.5,137.6 122.8,137.2 124.2,136.9 125.5,136.5 126.9,136.2 128.2,135.8 129.6,135.4 130.9,135 132.3,134.5 133.6,134.1 135,133.6 136.3,133.2 137.7,132.7 139.1,132.2 140.4,131.7 141.8,131.1 143.1,130.6 144.4,130 145.8,129.4 147.1,128.8 148.5,128.2 149.8,127.6 151.2,126.9 152.6,126.2 153.9,125.5 155.2,124.7 156.6,124 157.9,123.2 159.3,122.4 160.7,121.5 162,120.6 163.4,119.7 164.7,118.8 166.1,117.8 167.4,116.8 168.8,115.7 170.1,114.6 171.4,113.5 172.8,112.3 174.2,111.1 175.5,109.8 176.9,108.5 178.2,107.2 179.6,105.7 180.9,104.3 182.2,102.8 183.6,101.2 184.9,99.6 186.3,97.9 187.7,96.1 189,94.3 190.3,92.4 191.7,90.5 193.1,88.5 194.4,86.4 195.8,84.3 197.1,82.1 198.5,79.9 199.8,77.6 201.2,75.3 202.5,72.9 203.9,70.6 205.2,68.2 206.5,65.8 207.9,63.4 209.2,61.1 210.6,58.9 211.9,56.8 213.3,54.8 214.7,52.9 216,51.3 217.3,49.8 218.7,48.7 220.1,47.8 221.4,47.2 222.8,47 224.1,47.1 225.4,47.6 226.8,48.4 228.2,49.5 229.5,51 230.8,52.7 232.2,54.8 233.6,57.1 234.9,59.5 236.2,62.2 237.6,64.9 239,67.8 240.3,70.8 241.6,73.7 243,76.7 244.3,79.7 245.7,82.7 247,85.6 248.4,88.5 249.8,91.3 251.1,94 252.4,96.7 253.8,99.3 255.2,101.8 256.5,104.2 257.9,106.5 259.2,108.8 260.6,111 261.9,113.1 263.2,115.1 264.6,117 266,118.9 267.3,120.7 268.6,122.5 270,124.1 271.4,125.7 272.7,127.3 274,128.8 275.4,130.2 276.8,131.6 278.1,132.9 279.4,134.2 280.8,135.4 282.1,136.6 283.5,137.8 284.9,138.9 286.2,139.9 287.6,141 288.9,142 290.2,142.9 291.6,143.9 292.9,144.8 294.3,145.6 295.6,146.5 297,147.3 298.4,148.1 299.7,148.8 301.1,149.6 302.4,150.3 303.8,151 305.1,151.7 306.5,152.3 307.8,153 309.1,153.6 310.5,154.2 311.8,154.8 313.2,155.3 314.6,155.9 315.9,156.4 317.2,157 318.6,157.5 319.9,158 321.3,158.4 322.6,158.9 324,159.4" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"/><circle cx="223" cy="47" r="4" fill="#0f6e56"/><polyline points="54,144.8 55.4,144.8 56.7,144.8 58,144.8 59.4,144.8 60.8,144.8 62.1,144.7 63.5,144.7 64.8,144.7 66.2,144.6 67.5,144.6 68.8,144.6 70.2,144.5 71.5,144.5 72.9,144.4 74.2,144.4 75.6,144.3 77,144.2 78.3,144.2 79.7,144.1 81,144 82.3,144 83.7,143.9 85,143.8 86.4,143.7 87.8,143.6 89.1,143.5 90.5,143.4 91.8,143.3 93.2,143.2 94.5,143.1 95.8,142.9 97.2,142.8 98.6,142.7 99.9,142.5 101.2,142.4 102.6,142.3 104,142.1 105.3,142 106.7,141.8 108,141.7 109.3,141.5 110.7,141.3 112,141.1 113.4,141 114.8,140.8 116.1,140.6 117.4,140.4 118.8,140.2 120.2,140 121.5,139.8 122.8,139.6 124.2,139.4 125.5,139.2 126.9,138.9 128.2,138.7 129.6,138.5 130.9,138.2 132.3,138 133.6,137.7 135,137.5 136.3,137.2 137.7,137 139.1,136.7 140.4,136.4 141.8,136.2 143.1,135.9 144.4,135.6 145.8,135.3 147.1,135 148.5,134.8 149.8,134.5 151.2,134.2 152.6,133.9 153.9,133.6 155.2,133.3 156.6,132.9 157.9,132.6 159.3,132.3 160.7,132 162,131.7 163.4,131.4 164.7,131.1 166.1,130.8 167.4,130.5 168.8,130.2 170.1,129.9 171.4,129.6 172.8,129.3 174.2,129 175.5,128.7 176.9,128.4 178.2,128.1 179.6,127.9 180.9,127.6 182.2,127.4 183.6,127.1 184.9,126.9 186.3,126.7 187.7,126.5 189,126.3 190.3,126.2 191.7,126 193.1,125.9 194.4,125.7 195.8,125.6 197.1,125.6 198.5,125.5 199.8,125.5 201.2,125.5 202.5,125.5 203.9,125.5 205.2,125.6 206.5,125.6 207.9,125.7 209.2,125.9 210.6,126 211.9,126.2 213.3,126.4 214.7,126.7 216,126.9 217.3,127.2 218.7,127.5 220.1,127.8 221.4,128.2 222.8,128.6 224.1,129 225.4,129.4 226.8,129.8 228.2,130.3 229.5,130.7 230.8,131.2 232.2,131.7 233.6,132.3 234.9,132.8 236.2,133.3 237.6,133.9 239,134.5 240.3,135 241.6,135.6 243,136.2 244.3,136.8 245.7,137.4 247,138 248.4,138.6 249.8,139.2 251.1,139.8 252.4,140.4 253.8,141 255.2,141.6 256.5,142.2 257.9,142.8 259.2,143.4 260.6,144 261.9,144.6 263.2,145.2 264.6,145.8 266,146.4 267.3,146.9 268.6,147.5 270,148 271.4,148.6 272.7,149.1 274,149.7 275.4,150.2 276.8,150.7 278.1,151.2 279.4,151.7 280.8,152.2 282.1,152.7 283.5,153.2 284.9,153.7 286.2,154.2 287.6,154.6 288.9,155.1 290.2,155.5 291.6,156 292.9,156.4 294.3,156.8 295.6,157.2 297,157.7 298.4,158.1 299.7,158.5 301.1,158.8 302.4,159.2 303.8,159.6 305.1,160 306.5,160.3 307.8,160.7 309.1,161 310.5,161.4 311.8,161.7 313.2,162.1 314.6,162.4 315.9,162.7 317.2,163 318.6,163.3 319.9,163.6 321.3,163.9 322.6,164.2 324,164.5" fill="none" stroke="#1d4ed8" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"/><circle cx="201.3" cy="125.5" r="4" fill="#1d4ed8"/><polyline points="54,144.8 55.4,144.8 56.7,144.8 58,144.8 59.4,144.8 60.8,144.8 62.1,144.8 63.5,144.8 64.8,144.9 66.2,144.9 67.5,144.9 68.8,144.9 70.2,144.9 71.5,144.9 72.9,145 74.2,145 75.6,145 77,145 78.3,145.1 79.7,145.1 81,145.1 82.3,145.2 83.7,145.2 85,145.2 86.4,145.3 87.8,145.3 89.1,145.4 90.5,145.4 91.8,145.5 93.2,145.5 94.5,145.6 95.8,145.6 97.2,145.7 98.6,145.7 99.9,145.8 101.2,145.8 102.6,145.9 104,146 105.3,146 106.7,146.1 108,146.2 109.3,146.3 110.7,146.3 112,146.4 113.4,146.5 114.8,146.6 116.1,146.7 117.4,146.8 118.8,146.9 120.2,147 121.5,147.1 122.8,147.2 124.2,147.3 125.5,147.4 126.9,147.5 128.2,147.6 129.6,147.7 130.9,147.8 132.3,148 133.6,148.1 135,148.2 136.3,148.3 137.7,148.5 139.1,148.6 140.4,148.7 141.8,148.9 143.1,149 144.4,149.2 145.8,149.3 147.1,149.5 148.5,149.6 149.8,149.8 151.2,149.9 152.6,150.1 153.9,150.3 155.2,150.4 156.6,150.6 157.9,150.8 159.3,150.9 160.7,151.1 162,151.3 163.4,151.5 164.7,151.6 166.1,151.8 167.4,152 168.8,152.2 170.1,152.4 171.4,152.6 172.8,152.8 174.2,153 175.5,153.2 176.9,153.4 178.2,153.6 179.6,153.8 180.9,154 182.2,154.2 183.6,154.4 184.9,154.6 186.3,154.8 187.7,155 189,155.2 190.3,155.4 191.7,155.6 193.1,155.8 194.4,156 195.8,156.2 197.1,156.5 198.5,156.7 199.8,156.9 201.2,157.1 202.5,157.3 203.9,157.5 205.2,157.7 206.5,158 207.9,158.2 209.2,158.4 210.6,158.6 211.9,158.8 213.3,159 214.7,159.2 216,159.5 217.3,159.7 218.7,159.9 220.1,160.1 221.4,160.3 222.8,160.5 224.1,160.7 225.4,160.9 226.8,161.1 228.2,161.4 229.5,161.6 230.8,161.8 232.2,162 233.6,162.2 234.9,162.4 236.2,162.6 237.6,162.8 239,163 240.3,163.2 241.6,163.4 243,163.6 244.3,163.8 245.7,164 247,164.2 248.4,164.4 249.8,164.6 251.1,164.8 252.4,164.9 253.8,165.1 255.2,165.3 256.5,165.5 257.9,165.7 259.2,165.9 260.6,166.1 261.9,166.2 263.2,166.4 264.6,166.6 266,166.8 267.3,166.9 268.6,167.1 270,167.3 271.4,167.5 272.7,167.6 274,167.8 275.4,168 276.8,168.1 278.1,168.3 279.4,168.5 280.8,168.6 282.1,168.8 283.5,168.9 284.9,169.1 286.2,169.2 287.6,169.4 288.9,169.6 290.2,169.7 291.6,169.9 292.9,170 294.3,170.2 295.6,170.3 297,170.4 298.4,170.6 299.7,170.7 301.1,170.9 302.4,171 303.8,171.1 305.1,171.3 306.5,171.4 307.8,171.5 309.1,171.7 310.5,171.8 311.8,171.9 313.2,172.1 314.6,172.2 315.9,172.3 317.2,172.5 318.6,172.6 319.9,172.7 321.3,172.8 322.6,172.9 324,173.1" fill="none" stroke="#b45309" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"/><text x="214.8" y="49.8" text-anchor="end" font-size="11" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">h = 0,25</text><text x="137.7" y="111.3" text-anchor="middle" font-size="11" font-weight="700" fill="#1d4ed8" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">h = 0,60</text><text x="175.5" y="164.2" text-anchor="middle" font-size="11" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">h = 1,30</text></svg>
:::

Sur la figure, la courbe verte (h faible) est haute et étroite près de N₀, la bleue est plus basse et plus large, la orange (h = 1,30 kg/s, au-delà du seuil h_l = 1,14 kg/s) n'a plus de pic.

::: exemple Suivre N_r et le pic quand h augmente (m = 0,100 kg ; k = 6,5 N/m ; F_m = 0,13 N)

1. Seuil : h_l = √(2mk) = √(2 × 0,100 × 6,5) = √1,3 = 1,14 kg/s ; on a N₀ = 1,283 Hz (N₀² = 1,646 Hz²) et F_m/k = 2,0 cm.
2. h = 0,25 kg/s : N_r = √(1,646 − 0,079) = 1,25 Hz, presque N₀, et X_m(N_r) = 6,5 cm : résonance aiguë.
3. h = 0,60 kg/s : N_r = 1,09 Hz et X_m(N_r) = 2,9 cm : le pic est plus bas et le maximum s'est décalé de 0,19 Hz sous N₀.
4. h = 1,0 kg/s : N_r = √(1,646 − 1,267) = 0,62 Hz et X_m(N_r) = 2,1 cm, à peine plus que F_m/k = 2,0 cm : le pic s'efface.
5. h = 1,30 kg/s dépasse h_l : le radicande 1,646 − 2,140 est négatif, il n'y a plus de maximum, et X_m décroît à partir de 2,0 cm (courbe orange).

:::

::: piege
**Erreur : croire que seul le pic s'abaisse, la fréquence de résonance restant N₀.** Dans l'exemple, N_r vaut 1,25 Hz, puis 1,09 Hz, puis 0,62 Hz quand h augmente (étapes 2 à 4) : elle s'éloigne de N₀ = 1,283 Hz. L'erreur tente parce que N₀ ne dépend pas de h. Mais N_r contient le terme h²/(8π²m²), qui croît avec h : le maximum de l'amplitude se décale vers les basses fréquences.
:::

::: propriete
**Ce qui reste vrai** — À fréquence donnée, X_m diminue quand h augmente, puisque h figure au dénominateur. N₀ ne dépend que de m et de k. Plus le frottement est fort, plus la résonance est floue, jusqu'à disparaître pour h ≥ h_l. Cas limite : sans frottement (h = 0), la résonance serait infiniment aiguë, avec N_r = N₀ ; pour h = h_l, le maximum se confond avec N = 0.
:::

::: verifie À toi : avec ou sans résonance ?
m = 0,25 kg, k = 64 N/m. Pour h = 4,0 kg/s puis pour h = 6,0 kg/s, y a-t-il une résonance d'élongation ? Si oui, calculer N_r.

---

h_l = √(2mk) = √32 = 5,66 kg/s. Pour h = 4,0 kg/s, h est inférieur à h_l : il y a résonance, avec ω_r² = 256 − 16/(2 × 0,0625) = 128, donc ω_r = 11,3 rad/s et N_r = 1,80 Hz (N₀ = 2,55 Hz). Pour h = 6,0 kg/s, h est supérieur à h_l : ω_r² = 256 − 36/0,125 = −32 < 0, il n'y a pas de résonance d'élongation.
:::

::: retenir
Plus h est faible, plus la résonance est aiguë ; plus h est grand, plus elle est floue et plus N_r s'éloigne de N₀ ; pour h ≥ √(2mk), il n'y a plus de résonance d'élongation.
:::

## 🚀 L'impédance mécanique et la résonance de vitesse

Regarde maintenant la vitesse du palet plutôt que sa position. Au chapitre 4, le circuit RLC série a une résonance d'intensité exactement à N₀, quelle que soit la résistance. Le pendule se comporte comme ce circuit avec les correspondances U_m ↔ F_m, I_m ↔ V_m (valeur maximale de la vitesse), R ↔ h, L ↔ m et 1/C ↔ k.
Où la vitesse est-elle maximale, et comment se situent alors v et x par rapport à la force ?

::: definition
**Impédance mécanique et résonance de vitesse** — Par analogie avec le circuit, V_m = F_m/Z, où l'impédance mécanique est :

$$ Z = √(h² + (mω − k/ω)²) $$

Z = F_m/V_m s'exprime en kg/s, comme h. Elle est minimale pour mω = k/ω, c'est-à-dire à la fréquence N₀, quel que soit h : c'est la **résonance de vitesse**, avec Z = h et V_m = F_m/h. Alors v est en phase avec F. En général, le déphasage de v par rapport à F vérifie tan(φ_v − φ_F) = (k/ω − mω)/h.
:::

| Circuit RLC série forcé | Pendule élastique forcé |
| --- | --- |
| u = U_m sin(ωt + φ_u) | F = F_m sin(ωt + φ_F) |
| I_m = U_m/Z, avec Z = √(R² + (Lω − 1/(Cω))²) | V_m = F_m/Z, avec Z = √(h² + (mω − k/ω)²) |
| Résonance d'intensité : I_m = U_m/R, à N = N₀ | Résonance de vitesse : V_m = F_m/h, à N = N₀ |
| tan(φ_i − φ_u) = (1/(Cω) − Lω)/R | tan(φ_v − φ_F) = (k/ω − mω)/h |

Dans le tableau, chaque ligne mécanique se déduit de la ligne électrique en remplaçant R par h, L par m, 1/C par k, U_m par F_m et I_m par V_m.

| Fréquence | v par rapport à F | x par rapport à F |
| --- | --- | --- |
| N < N₀ | v en avance | x en retard de moins de π/2 |
| N = N₀ | v en phase | x en retard de π/2 |
| N > N₀ | v en retard | x en retard de plus de π/2 |

Dans ce second tableau, la ligne N = N₀ est celle de la résonance de vitesse ; la colonne de x est celle de la construction de Fresnel (notion 3).

::: exemple Étudier le pendule à la résonance de vitesse (m = 0,100 kg ; k = 6,5 N/m ; h = 0,60 kg/s ; F_m = 0,13 N)

1. ω₀ = √(k/m) = √65 = 8,06 rad/s : m·ω₀ = 0,806 kg/s et k/ω₀ = 0,806 kg/s se compensent, donc Z = h = 0,60 kg/s.
2. V_m = F_m/h = 0,13 / 0,60 = 0,217 m/s : c'est le maximum de la vitesse, atteint à N₀ quelle que soit la valeur de h.
3. tan(φ_v − φ_F) = (k/ω₀ − mω₀)/h = 0 : v est en phase avec F, et x est en retard de π/2 sur F (notion 3, cas ω = ω₀).
4. Pour ω = 5,0 rad/s (N < N₀) : Z = √(0,60² + (0,100 × 5,0 − 6,5/5,0)²) = √(0,36 + 0,64) = 1,0 kg/s, donc V_m = 0,13 m/s, plus petite que 0,217 m/s ; tan(φ_v − φ_F) = (1,30 − 0,50)/0,60 = 1,33, donc φ_v − φ_F = +0,93 rad : v est en avance sur F.
5. En N_r = 1,09 Hz, ω_r = 6,86 rad/s : Z = √(0,36 + (0,686 − 0,948)²) = 0,655 kg/s et V_m = 0,13/0,655 = 0,198 m/s, plus petite aussi que 0,217 m/s : la vitesse n'est pas maximale en N_r.

:::

::: piege
**Erreur : croire que la vitesse est maximale à N_r, comme l'élongation.** Dans l'exemple, V_m vaut 0,198 m/s en N_r (étape 5) et 0,217 m/s en N₀ (étape 2). L'erreur tente parce que les deux phénomènes portent le même nom de résonance. Mais l'élongation, grandeur qui s'obtient en intégrant la vitesse, a un maximum décalé par le terme h²/(8π²m²), alors que V_m = F_m/Z est maximale quand Z est minimale, donc en N₀.
:::

::: propriete
**Ce qui reste vrai** — Z ≥ h à toute fréquence, avec égalité à N₀ ; V_m = F_m/h est maximale en N₀ et diminue quand h augmente. Pour N < N₀, v est en avance sur F et x en retard de moins de π/2 ; pour N > N₀, v est en retard et x en retard de plus de π/2. Cas limite : à N = N₀, v est exactement en phase avec F et x exactement en retard de π/2.
:::

::: verifie À toi : la résonance d'un autre pendule
m = 0,20 kg, k = 20 N/m, h = 0,80 kg/s, F_m = 0,40 N, moteur réglé sur la résonance de vitesse. Calculer N, Z, V_m, X_m, et dire de combien x est en retard sur F.

---

La résonance de vitesse a lieu à N₀ = (1/2π)√(k/m) = 10/6,283 = 1,59 Hz, avec ω₀ = 10 rad/s. Alors Z = h = 0,80 kg/s et V_m = F_m/h = 0,40 / 0,80 = 0,50 m/s. Comme k − mω₀² = 0, X_m = F_m/(h·ω₀) = 0,40 / (0,80 × 10) = 5,0 × 10⁻² m = 5,0 cm. La vitesse est en phase avec F, donc x est en retard de π/2 rad sur F.
:::

::: retenir
V_m = F_m/Z avec Z = √(h² + (mω − k/ω)²) en kg/s ; V_m est maximale à N₀ quel que soit h (Z = h, V_m = F_m/h), v en phase avec F et x en retard de π/2.
:::

## 🔌 La puissance mécanique moyenne

Pendant que le palet oscille, le moteur lui fournit de l'énergie et les frottements la transforment en chaleur. En régime permanent, l'énergie du pendule ne varie plus d'une période à l'autre : tout ce que le moteur apporte est dissipé par les frottements. Le pendule garde les mêmes valeurs que précédemment (h = 0,60 kg/s ; F_m = 0,13 N).
Quelle puissance moyenne le moteur fournit-il, et à quelle fréquence est-elle la plus grande ?

::: definition
**Puissance mécanique moyenne** — En régime sinusoïdal forcé, la puissance moyenne reçue par le pendule est, avec φ = φ_v − φ_F le déphasage entre v et F :

$$ P = ½·F_m·V_m·cos φ = ½·h·V_m² $$

Le facteur de puissance est cos φ = h/Z, et P s'exprime en watt. Elle est analogue à la puissance électrique moyenne du chapitre 4, avec F_m ↔ U_m, V_m ↔ I_m et h ↔ R.
:::

::: exemple Puissance à N₀ et à ω = 5,0 rad/s (m = 0,100 kg ; k = 6,5 N/m ; h = 0,60 kg/s ; F_m = 0,13 N)

1. À la résonance de vitesse, V_m = 0,217 m/s et φ = 0, donc cos φ = 1 et P = ½ × 0,13 × 0,217 × 1 = 1,41 × 10⁻² W, soit 14,1 mW.
2. Contrôle avec l'autre forme : P = ½·h·V_m² = ½ × 0,60 × 0,217² = 1,41 × 10⁻² W ✓, les deux expressions s'accordent.
3. À ω = 5,0 rad/s : Z = 1,0 kg/s et V_m = 0,13 m/s, donc cos φ = h/Z = 0,60 et P = ½ × 0,13 × 0,13 × 0,60 = 5,07 × 10⁻³ W, soit ½ × 0,60 × 0,13² = 5,07 × 10⁻³ W avec la seconde forme.
4. La puissance maximale est P₀ = F_m²/(2h) = 0,13² / 1,2 = 14,1 mW, atteinte en N₀ et non en N_r : en N_r, V_m = 0,198 m/s donne P = ½ × 0,60 × 0,198² = 11,8 mW, plus petite.

:::

::: piege
**Erreur : oublier le facteur de puissance cos φ, et écrire P = ½·F_m·V_m.** À ω = 5,0 rad/s, cela donnerait 8,45 mW au lieu de 5,07 mW (étape 3). L'erreur tente parce que F_m et V_m sont les deux grandeurs connues. Mais F et v ne sont pas en phase en dehors de N₀ : seule la part de la force en phase avec v travaille, et le facteur cos φ = h/Z la mesure.
:::

::: propriete
**Ce qui reste vrai** — P = ½·h·V_m² est maximale à N₀, où P₀ = F_m²/(2h) : plus h est faible, plus la puissance maximale est grande. Loin de N₀, P tend vers 0. Cas limite : à N₀, cos φ = 1, et toute la puissance fournie par le moteur est dissipée par les frottements.
:::

::: verifie À toi : puissance d'un autre pendule
m = 0,20 kg, k = 20 N/m, h = 4,0 kg/s, F_m = 0,50 N, ω = 20 rad/s. Calculer Z, V_m, cos φ, puis P par les deux formes.

---

mω = 4,0 kg/s et k/ω = 1,0 kg/s, donc Z = √(4,0² + 3,0²) = 5,0 kg/s. Alors V_m = F_m/Z = 0,50 / 5,0 = 0,10 m/s et cos φ = h/Z = 0,80. P = ½ × 0,50 × 0,10 × 0,80 = 0,020 W, et ½·h·V_m² = ½ × 4,0 × 0,10² = 0,020 W : les deux formes donnent 20 mW.
:::

::: retenir
P = ½·F_m·V_m·cos φ = ½·h·V_m² en watt, avec cos φ = h/Z ; elle est maximale à N₀ : P₀ = F_m²/(2h).
:::

## 🌉 La résonance dans la vie : la vitesse critique

Sur une piste saharienne, des bosses reviennent tous les 20 m. Une voiture qui roule à vitesse constante en franchit une à intervalles réguliers : chaque bosse secoue la caisse. À certaines vitesses la caisse se met à tanguer fortement, à d'autres à peine.
À quelle vitesse la voiture est-elle la plus secouée ?

::: definition
**Vitesse critique** — Le profil de la route est l'excitateur, la suspension (ressort de raideur k, masse m de la voiture) est le résonateur. Une voiture de vitesse v franchit des bosses espacées de d avec la période T = d/v, soit la fréquence N = v/d. La caisse est la plus secouée quand cette fréquence est voisine de la fréquence propre de la suspension : T ≈ T₀ = 2π√(m/k). La vitesse correspondante est la **vitesse critique** v_c = d/T₀.
:::

::: figure Voiture roulant à la vitesse v sur une route à bosses régulièrement espacées de la distance d : la voiture franchit une bosse toutes les T = d/v secondes, et sa suspension (ressort vert) joue le rôle de résonateur
<svg viewBox="0 0 340 180"><title>Voiture roulant à vitesse v constante sur une route à bosses régulièrement espacées de d : chaque bosse secoue la suspension, ressort et masse de la voiture</title><polyline points="20,140 21,140 22,140 23,139.9 24,139.9 25,139.8 26,139.7 27,139.6 28,139.5 29,139.4 30,139.2 31,139.1 32,138.9 33,138.7 34,138.5 35,138.4 36,138.1 37,137.9 38,137.7 39,137.5 40,137.2 41,137 42,136.7 43,136.5 44,136.3 45,136 46,135.7 47,135.5 48,135.3 49,135 50,134.8 51,134.5 52,134.3 53,134.1 54,133.9 55,133.6 56,133.5 57,133.3 58,133.1 59,132.9 60,132.8 61,132.6 62,132.5 63,132.4 64,132.3 65,132.2 66,132.1 67,132.1 68,132 69,132 70,132 71,132 72,132 73,132.1 74,132.1 75,132.2 76,132.3 77,132.4 78,132.5 79,132.6 80,132.8 81,132.9 82,133.1 83,133.3 84,133.5 85,133.6 86,133.9 87,134.1 88,134.3 89,134.5 90,134.8 91,135 92,135.3 93,135.5 94,135.7 95,136 96,136.3 97,136.5 98,136.7 99,137 100,137.2 101,137.5 102,137.7 103,137.9 104,138.1 105,138.4 106,138.5 107,138.7 108,138.9 109,139.1 110,139.2 111,139.4 112,139.5 113,139.6 114,139.7 115,139.8 116,139.9 117,139.9 118,140 119,140 120,140 121,140 122,140 123,139.9 124,139.9 125,139.8 126,139.7 127,139.6 128,139.5 129,139.4 130,139.2 131,139.1 132,138.9 133,138.7 134,138.5 135,138.4 136,138.1 137,137.9 138,137.7 139,137.5 140,137.2 141,137 142,136.7 143,136.5 144,136.3 145,136 146,135.7 147,135.5 148,135.3 149,135 150,134.8 151,134.5 152,134.3 153,134.1 154,133.9 155,133.6 156,133.5 157,133.3 158,133.1 159,132.9 160,132.8 161,132.6 162,132.5 163,132.4 164,132.3 165,132.2 166,132.1 167,132.1 168,132 169,132 170,132 171,132 172,132 173,132.1 174,132.1 175,132.2 176,132.3 177,132.4 178,132.5 179,132.6 180,132.8 181,132.9 182,133.1 183,133.3 184,133.5 185,133.6 186,133.9 187,134.1 188,134.3 189,134.5 190,134.8 191,135 192,135.3 193,135.5 194,135.7 195,136 196,136.3 197,136.5 198,136.7 199,137 200,137.2 201,137.5 202,137.7 203,137.9 204,138.1 205,138.4 206,138.5 207,138.7 208,138.9 209,139.1 210,139.2 211,139.4 212,139.5 213,139.6 214,139.7 215,139.8 216,139.9 217,139.9 218,140 219,140 220,140 221,140 222,140 223,139.9 224,139.9 225,139.8 226,139.7 227,139.6 228,139.5 229,139.4 230,139.2 231,139.1 232,138.9 233,138.7 234,138.5 235,138.4 236,138.1 237,137.9 238,137.7 239,137.5 240,137.2 241,137 242,136.7 243,136.5 244,136.3 245,136 246,135.7 247,135.5 248,135.3 249,135 250,134.8 251,134.5 252,134.3 253,134.1 254,133.9 255,133.6 256,133.5 257,133.3 258,133.1 259,132.9 260,132.8 261,132.6 262,132.5 263,132.4 264,132.3 265,132.2 266,132.1 267,132.1 268,132 269,132 270,132 271,132 272,132 273,132.1 274,132.1 275,132.2 276,132.3 277,132.4 278,132.5 279,132.6 280,132.8 281,132.9 282,133.1 283,133.3 284,133.5 285,133.6 286,133.9 287,134.1 288,134.3 289,134.5 290,134.8 291,135 292,135.3 293,135.5 294,135.7 295,136 296,136.3 297,136.5 298,136.7 299,137 300,137.2 301,137.5 302,137.7 303,137.9 304,138.1 305,138.4 306,138.5 307,138.7 308,138.9 309,139.1 310,139.2 311,139.4 312,139.5 313,139.6 314,139.7 315,139.8 316,139.9 317,139.9 318,140 319,140 320,140" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/><rect x="76" y="60" width="88" height="28" fill="#ffffff" stroke="#0f172a" stroke-width="1.8"/><text x="120" y="79" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">voiture</text><polyline points="120,88 113,91 127,96 113,101 127,106 113,111 127,116 113,121 120,122" fill="none" stroke="#0f6e56" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round"/><circle cx="120" cy="131" r="9" fill="#ffffff" stroke="#0f172a" stroke-width="1.8"/><line x1="176" y1="74" x2="236" y2="74" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><polygon points="242,74 234,70 234,78" fill="#0f172a"/><text x="256" y="78" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">v</text><line x1="70" y1="134" x2="70" y2="158" stroke="#0f172a" stroke-width="1.2" stroke-dasharray="3 3" stroke-linecap="round"/><line x1="170" y1="134" x2="170" y2="158" stroke="#0f172a" stroke-width="1.2" stroke-dasharray="3 3" stroke-linecap="round"/><line x1="70" y1="152" x2="170" y2="152" stroke="#b45309" stroke-width="1.8" stroke-linecap="round"/><line x1="70" y1="147" x2="70" y2="157" stroke="#b45309" stroke-width="1.8" stroke-linecap="round"/><line x1="170" y1="147" x2="170" y2="157" stroke="#b45309" stroke-width="1.8" stroke-linecap="round"/><text x="120" y="171" text-anchor="middle" font-size="13" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">d</text></svg>
:::

Sur la figure, la distance d entre deux bosses est parcourue à la vitesse v en une durée T = d/v : c'est la période de l'excitation.

::: exemple Calculer la vitesse critique (m = 1000 kg ; k = 4,0 × 10⁴ N/m ; d = 20 m)

1. La voiture franchit une bosse toutes les T = d/v secondes, donc l'excitation a la période T = d/v.
2. T₀ = 2π√(m/k) = 2π√(1000 / 4,0 × 10⁴) = 2π × 0,158 = 0,993 s : c'est la période propre de la suspension, avec N₀ = 1,01 Hz.
3. Les frottements sont faibles, donc la résonance a lieu pour T ≈ T₀ : d/v_c = T₀, d'où v_c = d/T₀ = 20 / 0,993 = 20,1 m/s.
4. Conversion : 20,1 m/s × 3,6 = 72,5 km/h. À 30 km/h (8,3 m/s), T = 20/8,3 = 2,4 s est très différente de T₀ : la voiture est à peine secouée.

:::

::: piege
**Erreur : oublier de convertir les m/s en km/h.** On annoncerait v_c = 20 km/h, soit près de quatre fois moins que la valeur correcte de 72,5 km/h (étape 4). L'erreur tente parce que d est en mètres et T₀ en secondes : le quotient sort naturellement en m/s, et le nombre 20 « ressemble » à une vitesse de route. Mais pour une vitesse en km/h, il faut multiplier les m/s par 3,6.
:::

::: methode

1. **Excitation** : calculer la période T = d/v (ou la fréquence N = v/d) à laquelle le véhicule franchit les bosses.
2. **Résonateur** : calculer la période propre de la suspension, T₀ = 2π√(m/k).
3. **Condition de résonance** : écrire T = T₀ (frottements faibles), d'où v_c = d/T₀ ; convertir en km/h en multipliant les m/s par 3,6.

**Une situation à retenir** : plus la suspension est amortie (amortisseurs), plus h est grand, et plus la résonance est floue : les secousses restent faibles même près de v_c.
:::

::: propriete
**Ce qui reste vrai** — La résonance se cherche (caisse d'un violon, baie où la marée est amplifiée : période propre voisine de 12 h) ou s'évite (pont suspendu d'Angers en 1850, où une troupe marchait au pas cadencé ; pont de Tacoma en 1940, sous des rafales périodiques ; rotor mal équilibré d'une machine, carrosserie qui vibre : masselotte de plomb sur la jante, amortisseurs). À vitesse très faible, la voiture suit le profil de la route sans être secouée ; à vitesse très grande, les secousses sont trop rapides pour que la caisse réagisse. Cas limite : dans l'approximation T = T₀, v_c ne dépend ni de F_m ni de h, seulement de d, m et k.
:::

::: verifie À toi : un autre véhicule
Un autobus de 6000 kg, dont la suspension a pour raideur k = 1,5 × 10⁵ N/m, roule sur une route dont les joints sont espacés de 10 m. Calculer T₀, puis la vitesse critique en m/s et en km/h.

---

T₀ = 2π√(m/k) = 2π√(6000 / 1,5 × 10⁵) = 2π × 0,200 = 1,26 s. La résonance a lieu pour d/v_c = T₀, donc v_c = 10 / 1,26 = 7,96 m/s, soit 7,96 × 3,6 = 28,7 km/h.
:::

::: retenir
La voiture est la plus secouée quand T = d/v = T₀ = 2π√(m/k), soit v_c = d/T₀ ; les amortisseurs rendent la résonance floue.
:::

> 🏆 Quête franchie, héros ! Tu sais lire un enregistrement forcé, établir l'équation du pendule, calculer l'amplitude et le retard de phase par la construction de Fresnel, situer la résonance d'élongation sous N₀ et celle de vitesse en N₀, juger l'effet de l'amortissement, chiffrer une puissance et trouver la vitesse critique d'un véhicule. Les chapitres suivants quittent les oscillateurs pour les ondes.
