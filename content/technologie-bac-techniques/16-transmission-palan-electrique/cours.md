# 🏗️ Le palan électrique : freiner, limiter, démultiplier

> 💡 « Un palan lève une tonne avec un moteur de 0,8 kW. Il y arrive parce que son réducteur ralentit énormément la rotation, et il reste sûr parce qu'un frein retient la charge et qu'un limiteur protège la mécanique. »

Ce chapitre clôt le thème **Transmission de puissance**, après l'embrayage, le tour, la boîte de vitesses, la fraiseuse et le moteur à explosion. Le support est un **palan électrique à chaîne** de 1 000 kg : un moteur de 0,8 kW, un **réducteur à double train épicycloïdal**, un **frein de levage à disque** et un **limiteur de couple**, qui font tourner une **noix** sur laquelle s'enroule la chaîne. Le dossier technique donne une vitesse de levage de 3,6 m/min, un dessin d'ensemble (échelle 1:2) et une nomenclature de 40 repères.

Le chapitre a deux parties. Les sections 1 à 7 suivent les activités du palan : son frein, son limiteur, son train épicycloïdal. Les sections 8 à 12 reprennent la **synthèse du thème** : classer les transmissions, comparer les formules de couple, transformer un mouvement, calculer une cylindrée. Les notations des chapitres précédents reviennent : Ct, f, n, Rm, et N pour une vitesse de rotation en tr/min. Le mot r a deux sens : le **rayon intérieur** d'une couronne de friction (sections 3, 4 et 9) et le **rapport de transmission** (sections 6 à 8) ; le texte dit chaque fois lequel.

> 🗡️ Les schémas de ce cours sont des **schémas de principe**, redessinés pour expliquer : les dessins d'ensemble du manuel (p.203 et p.204) ne sont pas reproduits, et le manuel ne donne aucun corrigé. Quand une valeur est lue dans le manuel (nomenclature, caractéristiques), le texte le dit ; quand elle est choisie pour s'entraîner, il parle d'**illustration** ; quand un point relève d'un **principe** de mécanique plutôt que du dessin, il le dit aussi.

## 🏗️ Du moteur à la charge : la chaîne du palan

Un palan soulève 1 000 kg à 3,6 m/min avec un moteur de 0,8 kW. Le moteur tourne vite avec un petit couple, alors que la noix doit tourner lentement avec un grand couple. Entre les deux, plusieurs organes se partagent le travail.

Lequel fait quoi, et comment le consigne-t-on ?

::: definition Le diagramme FAST descriptif du palan
Comme au premier thème, le **diagramme FAST** décompose une **fonction principale** (FP) en **fonctions techniques** (FT) et nomme, en face de chacune, le composant qui la réalise. Pour le palan, FP est **déplacer la charge**.

| Fonction technique | Composant |
| --- | --- |
| FT211 : créer le couple | moteur électrique |
| FT212 : adapter le couple | réducteur à double train épicycloïdal |
| FT22 : supporter la charge | crochet et chaîne (donné par le manuel) |
| FT23 : entraîner la chaîne | noix (donnée par le manuel) |
| FT3 : protéger le palan contre les surcharges | limiteur de couple |
| FT4 : immobiliser la charge | frein à disque |

La fonction FT1, suspendre le palan, relève du dossier technique et n'est pas étudiée ici.
:::

::: figure La chaîne de puissance du palan, du haut vers le bas. Chaque bloc porte le composant et, à droite, la fonction technique qu'il réalise. Le frein et le limiteur sont deux fonctions réunies dans un même mécanisme, placé sur l'arbre de transmission (2), avant le réducteur
<svg viewBox="0 0 340 290"><title>La chaîne de puissance du palan et les fonctions techniques de son FAST</title><rect x="10" y="8" width="226" height="34" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round" /><text x="123" y="29" font-size="11" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Moteur électrique (rotor 3)</text><rect x="244" y="10" width="90" height="30" fill="#ffffff" stroke="#0f172a" stroke-width="1.0" stroke-linejoin="round" /><text x="289" y="23" font-size="9.5" font-weight="700" text-anchor="middle" fill="#0f172a" >FT211</text><text x="289" y="35" font-size="9" font-weight="500" text-anchor="middle" fill="#0f172a" >Créer le couple</text><line x1="123" y1="42" x2="123" y2="50" stroke="#0f172a" stroke-width="1.8" stroke-linecap="round" /><polygon points="123 56 120 50 126 50" fill="#0f172a" stroke="#0f172a" stroke-width="1" stroke-linejoin="round" stroke-linecap="round" /><rect x="10" y="56" width="226" height="34" fill="#fde68a" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round" /><text x="123" y="77" font-size="11" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Frein + limiteur (arbre 2)</text><rect x="244" y="58" width="90" height="30" fill="#ffffff" stroke="#0f172a" stroke-width="1.0" stroke-linejoin="round" /><text x="289" y="71" font-size="9" font-weight="700" text-anchor="middle" fill="#0f172a" >FT3 Protéger</text><text x="289" y="83" font-size="9" font-weight="700" text-anchor="middle" fill="#0f172a" >FT4 Immobiliser</text><line x1="123" y1="90" x2="123" y2="98" stroke="#0f172a" stroke-width="1.8" stroke-linecap="round" /><polygon points="123 104 120 98 126 98" fill="#0f172a" stroke="#0f172a" stroke-width="1" stroke-linejoin="round" stroke-linecap="round" /><rect x="10" y="104" width="226" height="34" fill="#bbf7d0" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round" /><text x="123" y="125" font-size="11" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Réducteur à double train épicycloïdal</text><rect x="244" y="106" width="90" height="30" fill="#ffffff" stroke="#0f172a" stroke-width="1.0" stroke-linejoin="round" /><text x="289" y="119" font-size="9.5" font-weight="700" text-anchor="middle" fill="#0f172a" >FT212</text><text x="289" y="131" font-size="9" font-weight="500" text-anchor="middle" fill="#0f172a" >Adapter le couple</text><line x1="123" y1="138" x2="123" y2="146" stroke="#0f172a" stroke-width="1.8" stroke-linecap="round" /><polygon points="123 152 120 146 126 146" fill="#0f172a" stroke="#0f172a" stroke-width="1" stroke-linejoin="round" stroke-linecap="round" /><rect x="10" y="152" width="226" height="34" fill="#e2e8f0" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round" /><text x="123" y="173" font-size="11" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Noix de levage (5)</text><rect x="244" y="154" width="90" height="30" fill="#ffffff" stroke="#0f172a" stroke-width="1.0" stroke-linejoin="round" /><text x="289" y="167" font-size="9.5" font-weight="700" text-anchor="middle" fill="#0f172a" >FT23</text><text x="289" y="179" font-size="9" font-weight="500" text-anchor="middle" fill="#0f172a" >Entraîner la chaîne</text><line x1="123" y1="186" x2="123" y2="194" stroke="#0f172a" stroke-width="1.8" stroke-linecap="round" /><polygon points="123 200 120 194 126 194" fill="#0f172a" stroke="#0f172a" stroke-width="1" stroke-linejoin="round" stroke-linecap="round" /><rect x="10" y="200" width="226" height="34" fill="#e2e8f0" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round" /><text x="123" y="221" font-size="11" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Chaîne et crochet</text><rect x="244" y="202" width="90" height="30" fill="#ffffff" stroke="#0f172a" stroke-width="1.0" stroke-linejoin="round" /><text x="289" y="215" font-size="9.5" font-weight="700" text-anchor="middle" fill="#0f172a" >FT22</text><text x="289" y="227" font-size="9" font-weight="500" text-anchor="middle" fill="#0f172a" >Supporter la charge</text><line x1="123" y1="234" x2="123" y2="242" stroke="#0f172a" stroke-width="1.8" stroke-linecap="round" /><polygon points="123 248 120 242 126 242" fill="#0f172a" stroke="#0f172a" stroke-width="1" stroke-linejoin="round" stroke-linecap="round" /><rect x="10" y="248" width="226" height="34" fill="#fdba74" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round" /><text x="123" y="269" font-size="11" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Charge (1 000 kg au plus)</text></svg>
:::

Les repères de la figure viennent de la nomenclature : le rotor (3) du moteur, l'arbre (2), la noix (5). Le frein-limiteur reçoit la rotation à la vitesse du moteur et la transmet au réducteur sans la changer ; c'est le réducteur qui la ralentit.

::: exemple Compléter la colonne des composants (lecture du dossier)
Le manuel laisse en pointillés quatre composants du FAST ; on les retrouve dans la composition du palan et dans la description du mécanisme.

1. **FT211, créer le couple** : la composition cite d'abord « un moteur électrique (Pm = 0,8 kW) », qui fournit la rotation.
2. **FT212, adapter le couple** : « un réducteur à double train épicycloïdal » transmet la rotation de l'arbre (2) à la noix (5) en la ralentissant.
3. **FT3, protéger contre les surcharges** : la description dit qu'une charge excessive provoque un glissement, ce qui préserve le système. C'est le rôle du **limiteur de couple**.
4. **FT4, immobiliser la charge** : le palan s'arrête de lui-même quand on le désalimente. C'est le rôle du **frein de levage à disque**.

:::

::: piege Le frein et le limiteur ne font pas le même travail
Les deux sont des disques pressés par un ressort, dans un même mécanisme : on les prend pour une seule pièce. Pourtant, le **frein** immobilise la charge quand on ne lève plus (FT4), alors que le **limiteur** protège la mécanique quand la charge est trop lourde pendant le levage (FT3). Les deux ont chacun leur ressort et leur disque.
:::

::: verifie
Quel composant réalise « adapter le couple » dans le palan, et quel composant « entraîne la chaîne » ?
---
Le **réducteur à double train épicycloïdal** adapte le couple (FT212) : il ralentit la rotation et augmente le couple. La **noix** (5) entraîne la chaîne (FT23), parce que la chaîne s'enroule sur elle.
:::

## 🧲 Libre ou freiné : le frein à disque du palan

Une charge de 1 000 kg est accrochée au palan. Si le courant disparaît, elle ne doit pas retomber. Le manuel demande le type de commande du frein, s'il est libre ou freiné, la forme de ses surfaces de contact, son type et la raison de ce choix.

Comment un frein peut-il retenir la charge quand rien ne l'alimente ?

::: definition Frein à disque à commande électromagnétique
Un **frein** ralentit ou immobilise une pièce en rotation par frottement. Celui du palan est un **frein à disque** : le **disque-frein (28)** est lié en rotation à l'arbre de transmission (2) par des **cannelures**, mais il peut glisser le long de l'arbre. Ses surfaces de contact sont **planes**, perpendiculaires à l'axe : l'effort de serrage est **axial**.

La **commande** est **électromagnétique** : un électro-aimant (31) l'actionne, et un ressort (30) fait le serrage.

- **Sous tension** (montée, descente) : l'électro-aimant est plaqué sur le disque d'ancrage (29), le ressort (30) est comprimé, la garniture (33) est décollée du disque : le frein est **libre**.
- **Hors tension** : le ressort (30) repousse l'électro-aimant (31) et sa garniture (33) sur le disque-frein (28) : le palan est **freiné**.
:::

::: figure Principe du frein-limiteur, en demi-coupe au-dessus de l'arbre (2). En haut, sous tension : l'électro-aimant (31) est plaqué sur le disque d'ancrage (29) et la garniture (33) laisse un jeu devant le disque-frein (28). En bas, hors tension : le ressort (30) a repoussé l'électro-aimant et la garniture serre le disque. Les écarts sont exagérés, et le dessin d'après la description du manuel n'est pas le dessin d'ensemble
<svg viewBox="0 0 340 296"><title>Le frein-limiteur du palan sous tension puis hors tension</title><rect x="24" y="95" width="285" height="10" fill="#e2e8f0" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round" /><line x1="168" y1="95" x2="168" y2="105" stroke="#0f172a" stroke-width="0.8" stroke-linecap="round" /><line x1="174" y1="95" x2="174" y2="105" stroke="#0f172a" stroke-width="0.8" stroke-linecap="round" /><line x1="180" y1="95" x2="180" y2="105" stroke="#0f172a" stroke-width="0.8" stroke-linecap="round" /><line x1="186" y1="95" x2="186" y2="105" stroke="#0f172a" stroke-width="0.8" stroke-linecap="round" /><line x1="192" y1="95" x2="192" y2="105" stroke="#0f172a" stroke-width="0.8" stroke-linecap="round" /><rect x="48" y="22" width="27" height="73" fill="#cbd5e1" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round" /><rect x="105" y="28" width="30" height="67" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round" /><rect x="108" y="34" width="24" height="16" fill="#fdba74" stroke="#0f172a" stroke-width="1.0" stroke-linejoin="round" /><rect x="135" y="28" width="9" height="67" fill="#fdba74" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round" /><polyline points="75 74.9 79.3 80.9 83.6 68.9 87.9 80.9 92.1 68.9 96.4 80.9 100.7 68.9 105 74.9" fill="none" stroke="#0f172a" stroke-width="1.5" stroke-linejoin="round" stroke-linecap="round" /><rect x="168" y="24" width="21" height="71" fill="#bbf7d0" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round" /><rect x="189" y="24" width="21" height="71" fill="#fde68a" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round" /><rect x="189" y="77" width="42" height="18" fill="#fef3c7" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round" /><polyline points="220.5 61.5 228.2 67.5 236 55.5 243.8 67.5 251.5 55.5 259.2 67.5 267 61.5" fill="none" stroke="#0f172a" stroke-width="1.5" stroke-linejoin="round" stroke-linecap="round" /><rect x="267" y="30" width="12" height="43" fill="#cbd5e1" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round" /><text x="61.5" y="16" font-size="10" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">29</text><text x="120" y="16" font-size="10" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">31</text><text x="178.5" y="16" font-size="10" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">28</text><text x="203.5" y="16" font-size="10" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">26</text><text x="244.5" y="16" font-size="10" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">36</text><text x="273" y="16" font-size="10" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><text x="145" y="109" font-size="10" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">33</text><text x="88.5" y="92.9" font-size="10" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">30</text><text x="216" y="120" font-size="10" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">20</text><text x="72" y="120" font-size="9.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">arbre (2)</text><line x1="145" y1="51.5" x2="163" y2="51.5" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round" /><polygon points="167 51.5 163 53.5 163 49.5" fill="#0f172a" stroke="#0f172a" stroke-width="1" stroke-linejoin="round" stroke-linecap="round" /><line x1="167" y1="51.5" x2="149" y2="51.5" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round" /><polygon points="145 51.5 149 49.5 149 53.5" fill="#0f172a" stroke="#0f172a" stroke-width="1" stroke-linejoin="round" stroke-linecap="round" /><text x="156" y="46.5" font-size="9" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">jeu</text><text x="170" y="136" font-size="11" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Sous tension : frein libre</text><line x1="10" y1="146" x2="330" y2="146" stroke="#94a3b8" stroke-width="1.0" stroke-linecap="round" stroke-dasharray="5 4" /><rect x="24" y="245" width="285" height="10" fill="#e2e8f0" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round" /><line x1="168" y1="245" x2="168" y2="255" stroke="#0f172a" stroke-width="0.8" stroke-linecap="round" /><line x1="174" y1="245" x2="174" y2="255" stroke="#0f172a" stroke-width="0.8" stroke-linecap="round" /><line x1="180" y1="245" x2="180" y2="255" stroke="#0f172a" stroke-width="0.8" stroke-linecap="round" /><line x1="186" y1="245" x2="186" y2="255" stroke="#0f172a" stroke-width="0.8" stroke-linecap="round" /><line x1="192" y1="245" x2="192" y2="255" stroke="#0f172a" stroke-width="0.8" stroke-linecap="round" /><rect x="48" y="172" width="27" height="73" fill="#cbd5e1" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round" /><rect x="129" y="178" width="30" height="67" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round" /><rect x="132" y="184" width="24" height="16" fill="#fdba74" stroke="#0f172a" stroke-width="1.0" stroke-linejoin="round" /><rect x="159" y="178" width="9" height="67" fill="#fdba74" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round" /><polyline points="75 224.9 80.4 230.9 85.8 218.9 91.2 230.9 96.6 218.9 102 230.9 107.4 218.9 112.8 230.9 118.2 218.9 123.6 230.9 129 224.9" fill="none" stroke="#0f172a" stroke-width="1.5" stroke-linejoin="round" stroke-linecap="round" /><rect x="168" y="174" width="21" height="71" fill="#bbf7d0" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round" /><rect x="189" y="174" width="21" height="71" fill="#fde68a" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round" /><rect x="189" y="227" width="42" height="18" fill="#fef3c7" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round" /><polyline points="220.5 211.5 228.2 217.5 236 205.5 243.8 217.5 251.5 205.5 259.2 217.5 267 211.5" fill="none" stroke="#0f172a" stroke-width="1.5" stroke-linejoin="round" stroke-linecap="round" /><rect x="267" y="180" width="12" height="43" fill="#cbd5e1" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round" /><text x="61.5" y="166" font-size="10" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">29</text><text x="144" y="166" font-size="10" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">31</text><text x="178.5" y="166" font-size="10" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">28</text><text x="203.5" y="166" font-size="10" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">26</text><text x="244.5" y="166" font-size="10" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">36</text><text x="273" y="166" font-size="10" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1</text><text x="169" y="259" font-size="10" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">33</text><text x="100.5" y="242.9" font-size="10" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">30</text><text x="216" y="270" font-size="10" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">20</text><text x="72" y="270" font-size="9.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">arbre (2)</text><text x="170" y="286" font-size="11" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Hors tension : palan freiné</text></svg>
:::

Sur la figure, le ressort (30) est plus court quand l'électro-aimant est plaqué sur (29) : il est comprimé, donc il n'impose rien au disque. Le jeu cité par le manuel est la course que l'électro-aimant parcourt entre ses deux états (principe).

| État | Électro-aimant (31) | Ressort (30) | Garniture (33) et disque (28) |
| --- | --- | --- | --- |
| **Libre** | alimenté, plaqué sur (29) | comprimé | décollée, disque libre de tourner |
| **Freiné** | non alimenté, repoussé | moins comprimé, il pousse | serrée contre le disque, rotation arrêtée |

::: exemple Quel état dans quelle situation ? (principe)
1. **Montée de la charge** : l'électro-aimant est sous tension, donc plaqué sur (29) : le frein est **libre** et le disque (28) tourne avec l'arbre.
2. **L'opérateur lâche le bouton** : plus de courant, l'électro-aimant ne retient plus rien ; le ressort (30) le repousse sur (28) : le palan est **freiné**.
3. **Coupure de courant en plein levage** : même état qu'à l'étape 2, pour la même raison. La charge reste suspendue.
4. **Lire un dessin** : on regarde où est l'électro-aimant. Contre le disque d'ancrage (29) : libre. Garniture (33) contre le disque (28) : freiné.

:::

::: piege Une coupure de courant ne lâche pas la charge
On croit qu'un frein « électrique » freine quand il est alimenté, donc qu'une panne de courant le libère. C'est l'inverse : le courant **desserre**, c'est le ressort qui **serre**. Une panne laisse le ressort agir, et la charge reste retenue. Le frein est un frein de sécurité.
:::

::: propriete Pourquoi un frein à disque ici (principe)
Les surfaces planes, serrées dans le sens de l'axe, tiennent dans un faible volume et ne poussent pas latéralement sur l'arbre : c'est adapté à un mécanisme logé dans le carter d'un palan. La commande par ressort assure l'immobilisation même sans courant. Ce sont deux raisons distinctes, l'une pour le disque, l'autre pour la commande.
:::

::: verifie
Sur un dessin, la garniture (33) touche le disque (28) et le ressort (30) est moins comprimé que sur l'autre vue. Le palan est-il libre ou freiné ?
---
Il est **freiné** : le ressort a repoussé l'électro-aimant et sa garniture sur le disque, ce qui ne peut arriver que si l'électro-aimant n'est plus alimenté. Libre, il serait plaqué sur le disque d'ancrage (29).
:::

## 🧮 Le couple de freinage

Le manuel donne la formule du couple de freinage, le coefficient de frottement f = 0,4 et l'effort du ressort (30), F30 = 500 N. Il demande de relever sur le dessin le nombre de surfaces de frottement n et les rayons r et R, puis de calculer le couple, et d'expliquer comment le faire varier.

De quoi dépend ce couple, et comment le calculer sans se tromper d'unité ?

::: definition Le couple de freinage Cf
Pour un frein à disque à surfaces planes, le manuel donne :

$$ Cf = (2/3) × F30 × f × n × (R³ − r³) / (R² − r²) $$

On la lit comme celle de l'embrayage (chapitres précédents), en deux temps :

$$ Rm = (2/3) × (R³ − r³) / (R² − r²) $$

$$ Cf = n × f × F30 × Rm $$

F30 est l'effort presseur, produit par le ressort (30) ; f le coefficient de frottement ; **n le nombre de surfaces de frottement** ; R et r les rayons extérieur et intérieur de la couronne de friction, relevés sur le dessin d'ensemble.
:::

::: exemple Calculer Cf avec des valeurs d'entraînement
Le manuel donne f = 0,4 et F30 = 500 N. Les valeurs de n, r et R se relèvent sur le dessin ; on prend ici, **pour s'entraîner** : n = 2, R = 45 mm et r = 30 mm.

1. **Rayon d'action.**

$$ Rm = (2/3) × (45³ − 30³) / (45² − 30²) = (2/3) × 64 125 / 1 125 = 38 mm $$

Contrôle : r < Rm < R, soit 30 < 38 < 45 : le résultat est plausible.
2. **Effort de frottement.** n × f × F30 = 2 × 0,4 × 500 = 400 N : c'est l'effort que le frottement oppose, pour les deux surfaces.
3. **Couple.** Cf = 400 × 38 = 15 200 N·mm, soit **15,2 N·m**. Les rayons sont en mm, donc le couple sort en N·mm : on convertit à la fin.

:::

::: piege n compte des surfaces, pas des pièces
Un disque garni sur ses deux faces et pincé des deux côtés offre **deux** surfaces de frottement, et non une. Écrire n = 1 divise le couple par deux. On compte donc les **contacts** qui frottent sur le dessin, pas les disques.
:::

::: propriete Faire varier le couple de freinage
Cf est proportionnel à n, à f et à F30 : doubler l'un double Cf, et F30 = 0 donne Cf = 0. Pour augmenter le couple de freinage sans changer le frein, on agit sur l'**effort du ressort** (30), en le remplaçant par un ressort plus raide ou en le comprimant davantage (principe). Changer de garniture (autre f), ajouter une surface de friction (n plus grand) ou élargir la couronne (R plus grand) augmente aussi Cf. La vitesse de rotation ne figure pas dans la formule.
:::

::: verifie
Même f = 0,4 et même ressort (F30 = 500 N), mais n = 1, R = 30 mm et r = 20 mm. Que vaut Cf, en N·m ?
---
Rm = (2/3) × (30³ − 20³) / (30² − 20²) = (2/3) × 19 000 / 500 ≈ 25,3 mm (entre 20 et 30 : plausible). Cf = 1 × 0,4 × 500 × 25,3 ≈ 5 070 N·mm, soit **5,07 N·m**. Une seule surface, donc moitié moins de force de frottement qu'avec deux.
:::

## 🛡️ Le limiteur de couple : glisser pour protéger

Le palan ne doit pas casser quand la charge est trop lourde. Le manuel demande l'utilité du limiteur, son symbole, les mobilités de cinq pièces dans deux régimes (couple inférieur ou supérieur au couple nominal), le fonctionnement en surcharge et le moyen d'augmenter le couple transmis.

Que fait le limiteur, et quelles pièces bougent encore quand il glisse ?

::: definition Le limiteur de couple et son couple nominal
Un **limiteur de couple** transmet la rotation **jusqu'à un couple préréglé**, le **couple nominal** C_nominal, et **interrompt la transmission au-delà**. Dans le palan, le **disque-frein (28)**, lié à l'arbre (2), est pressé par le ressort (36) contre le **disque limiteur (26)**, lié au planétaire (20) : la rotation passe par **adhérence**. Si la charge est excessive, (28) **glisse** sur (26), ce qui préserve l'ensemble contre toute rupture.

Le couple transmissible se calcule comme celui d'un embrayage : le manuel donne, pour un limiteur,

$$ Ct = (2/3) × F × f × (R³ − r³) / (R² − r²) $$

où F est l'effort du ressort. Il n'y écrit pas n : cela revient à une seule surface ; avec n surfaces, on multiplie par n comme à l'embrayage (principe).
:::

::: figure Les quatre symboles de la synthèse, d'après la description du manuel. Tous sont un rectangle traversé par l'arbre. L'embrayage a deux traits verticaux affrontés au centre ; le limiteur y ajoute un trait horizontal qui les relie, et son cadre est interrompu en haut et en bas. L'accouplement rigide a deux traits barrés d'une croix, l'accouplement élastique deux traits reliés par une diagonale
<svg viewBox="0 0 340 208"><title>Symboles normalisés de l'embrayage, du limiteur de couple et de deux accouplements</title><rect x="30" y="20" width="110" height="62" fill="#ffffff" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round" /><line x1="12" y1="51" x2="158" y2="51" stroke="#0f172a" stroke-width="2.2" stroke-linecap="round" /><line x1="79" y1="35" x2="79" y2="67" stroke="#0f172a" stroke-width="2.2" stroke-linecap="round" /><line x1="91" y1="35" x2="91" y2="67" stroke="#0f172a" stroke-width="2.2" stroke-linecap="round" /><polyline points="241 20 200 20 200 82 241 82" fill="none" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" /><polyline points="269 20 310 20 310 82 269 82" fill="none" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" /><line x1="182" y1="51" x2="328" y2="51" stroke="#0f172a" stroke-width="2.2" stroke-linecap="round" /><line x1="249" y1="35" x2="249" y2="67" stroke="#0f172a" stroke-width="2.2" stroke-linecap="round" /><line x1="261" y1="35" x2="261" y2="67" stroke="#0f172a" stroke-width="2.2" stroke-linecap="round" /><line x1="249" y1="35" x2="261" y2="35" stroke="#0f172a" stroke-width="2.2" stroke-linecap="round" /><rect x="30" y="112" width="110" height="62" fill="#ffffff" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round" /><line x1="12" y1="143" x2="158" y2="143" stroke="#0f172a" stroke-width="2.2" stroke-linecap="round" /><line x1="76" y1="123" x2="76" y2="163" stroke="#0f172a" stroke-width="2.2" stroke-linecap="round" /><line x1="71" y1="137" x2="81" y2="149" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round" /><line x1="71" y1="149" x2="81" y2="137" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round" /><line x1="94" y1="123" x2="94" y2="163" stroke="#0f172a" stroke-width="2.2" stroke-linecap="round" /><line x1="89" y1="137" x2="99" y2="149" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round" /><line x1="89" y1="149" x2="99" y2="137" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round" /><rect x="200" y="112" width="110" height="62" fill="#ffffff" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round" /><line x1="182" y1="143" x2="328" y2="143" stroke="#0f172a" stroke-width="2.2" stroke-linecap="round" /><line x1="246" y1="123" x2="246" y2="163" stroke="#0f172a" stroke-width="2.2" stroke-linecap="round" /><line x1="264" y1="123" x2="264" y2="163" stroke="#0f172a" stroke-width="2.2" stroke-linecap="round" /><line x1="246" y1="157" x2="264" y2="129" stroke="#0f172a" stroke-width="1.8" stroke-linecap="round" /><text x="85" y="106" font-size="10.5" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Embrayage</text><text x="255" y="106" font-size="10.5" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Limiteur de couple</text><text x="85" y="198" font-size="10.5" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Accouplement rigide</text><text x="255" y="198" font-size="10.5" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Accouplement élastique</text></svg>
:::

Le limiteur se distingue de l'embrayage par ce trait qui relie les deux traits verticaux : les deux parties restent liées tant que le couple est inférieur au couple préréglé. Les deux accouplements de la figure reviennent à la section 8.

Le tableau du manuel se remplit avec 1 pour « il y a mouvement » et 0 pour « pas de mouvement », l'électro-aimant (31) étant alimenté (le frein est libre).

| | C < C_nominal | C > C_nominal |
| --- | --- | --- |
| Arbre de transmission (2) | 1 | 1 |
| Disque (28) | 1 | 1 |
| Disque (26) | 1 | 0 |
| Planétaire (20) | 1 | 0 |
| Noix de levage (5) | 1 | 0 |

::: exemple Remplir la colonne C > C_nominal (lecture de principe)
1. **Le moteur continue de tourner.** L'arbre (2) est relié au rotor, donc 1. Le disque (28) est lié à l'arbre par cannelures, donc 1 aussi.
2. **Le glissement a lieu entre (28) et (26).** C'est la surface d'adhérence qui lâche : (28) tourne, mais (26) n'est plus entraîné.
3. **Le côté sortie s'arrête.** (26) est lié au planétaire (20), lui-même relié au réducteur puis à la noix (5) : on lit 0 pour (26), (20) et (5). La charge n'est pas soulevée.
4. **Pour revenir à C < C_nominal**, on retire la surcharge : l'adhérence reprend et tout le monde tourne de nouveau (colonne de gauche).

:::

::: piege Un limiteur ne coupe pas le moteur
Au-delà du couple nominal, ce n'est pas le palan entier qui s'arrête : le moteur, l'arbre (2) et le disque (28) tournent toujours, seule la partie liée au planétaire s'arrête. Le limiteur **laisse glisser**, et il retransmet de lui-même dès que le couple redescend.
:::

::: propriete Augmenter le couple transmis
Comme pour un embrayage, Ct est proportionnel à l'effort du ressort : pour **augmenter** le couple nominal, on **comprime davantage le ressort (36)**, par exemple en serrant l'écrou qui maintient l'ensemble sur l'arbre (principe). Un ressort moins comprimé fait glisser le limiteur plus tôt.
:::

::: verifie
Le couple dépasse le couple nominal. Quel disque continue de tourner avec l'arbre (2) alors que le planétaire (20) s'arrête, et pourquoi ?
---
Le **disque-frein (28)** : il est lié à l'arbre par cannelures, donc entraîné par le moteur. C'est lui qui glisse sur le disque limiteur (26), lequel s'arrête avec le planétaire (20).
:::

## 🪐 Le train épicycloïdal : pièces et dents

La noix doit tourner à une trentaine de tours par minute, quand le moteur en fait plus de mille. Il faut diviser la vitesse par environ 48, dans un carter compact. Le palan utilise deux trains épicycloïdaux en série. Le manuel donne la denture de la couronne (89 dents), d'un satellite (37 dents) et d'un planétaire (15 dents), et demande les deux dentures manquantes.

Comment les retrouver ?

::: definition Le train épicycloïdal et ses quatre pièces
Un train d'engrenages est **épicycloïdal** quand une ou plusieurs roues, les **satellites**, tournent autour d'axes qui **ne sont pas fixes** par rapport au bâti. Il comporte :

- le **planétaire** : la roue centrale à denture extérieure (20 au premier étage, 15 au second) ;
- les **satellites** : les roues qui l'entourent (19 au premier étage, 13 au second) ;
- le **porte-satellites** : la pièce qui porte les axes des satellites (16, puis 9) ;
- la **couronne** : la roue à denture intérieure (37), liée au carter dans le palan.
:::

::: figure Vue de face du premier étage, schéma de principe aux dimensions proportionnelles aux nombres de dents. La couronne (37) entoure trois satellites (19), engrenés avec le planétaire central (20) ; le porte-satellites (16) est la plaque bleue qui relie les axes des satellites. Sur la verticale, le rayon primitif de la couronne se décompose en r20 puis deux fois r19
<svg viewBox="0 0 340 276"><title>Vue de face du premier étage épicycloïdal du palan</title><circle cx="170" cy="136" r="134" fill="#cbd5e1" stroke="#0f172a" stroke-width="1.6"/><circle cx="170" cy="136" r="120" fill="#ffffff" stroke="#0f172a" stroke-width="1.4"/><circle cx="170" cy="65.9" r="49.9" fill="#bbf7d0" stroke="#0f172a" stroke-width="1.6"/><circle cx="109.3" cy="171.1" r="49.9" fill="#bbf7d0" stroke="#0f172a" stroke-width="1.6"/><circle cx="230.7" cy="171.1" r="49.9" fill="#bbf7d0" stroke="#0f172a" stroke-width="1.6"/><circle cx="170" cy="136" r="20.2" fill="#fde68a" stroke="#0f172a" stroke-width="1.6"/><polygon points="170 65.9 109.3 171.1 230.7 171.1" fill="#3b82f6" stroke="#1d4ed8" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round" fill-opacity="0.35"/><circle cx="170" cy="65.9" r="3.5" fill="#0f172a" stroke="#0f172a" stroke-width="1"/><circle cx="109.3" cy="171.1" r="3.5" fill="#0f172a" stroke="#0f172a" stroke-width="1"/><circle cx="230.7" cy="171.1" r="3.5" fill="#0f172a" stroke="#0f172a" stroke-width="1"/><circle cx="170" cy="136" r="2.5" fill="#0f172a" stroke="#0f172a" stroke-width="1"/><line x1="170" y1="136" x2="170" y2="115.8" stroke="#ea580c" stroke-width="4" stroke-linecap="round" /><line x1="170" y1="115.8" x2="170" y2="16" stroke="#15803d" stroke-width="4" stroke-linecap="round" /><text x="194" y="128" font-size="10" font-weight="700" text-anchor="middle" fill="#c2410c" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">r20</text><text x="200" y="81.9" font-size="10" font-weight="700" text-anchor="middle" fill="#166534" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2 × r19</text><text x="66" y="32" font-size="11" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">37</text><text x="101.3" y="191.1" font-size="11" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">19</text><text x="170" y="153" font-size="11" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">20</text><text x="170" y="168.1" font-size="11" font-weight="700" text-anchor="middle" fill="#1d4ed8" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">16</text></svg>
:::

Sur la figure, en partant du centre vers le haut, on traverse le rayon du planétaire, puis le diamètre d'un satellite : c'est ce qui permet de relier les dentures.

::: exemple Retrouver Z20 et Z13
Le manuel donne Z37 = 89, Z19 = 37 et Z15 = 15. Deux roues engrenées ont le **même module** m (chapitre sur la boîte de vitesses), donc un diamètre primitif d = m × Z, proportionnel au nombre de dents.

1. **Condition géométrique.** Le diamètre de la couronne est égal à celui du planétaire plus **deux fois** celui d'un satellite, car le satellite est traversé une fois de chaque côté du planétaire : d37 = d20 + 2 × d19. En nombres de dents, Z37 = Z20 + 2 × Z19.
2. **Premier étage.** Z20 = Z37 − 2 × Z19 = 89 − 2 × 37 = 89 − 74 = **15 dents**.
3. **Second étage.** Z37 = Z15 + 2 × Z13, donc Z13 = (89 − 15) / 2 = 74 / 2 = **37 dents**.
4. **Remarque.** Les deux étages ont les mêmes dentures (15 et 37 dents) et la même couronne de 89 dents : ils sont identiques.

:::

::: piege Le satellite compte deux fois
Écrire Z37 = Z20 + Z19 oublie qu'un satellite se trouve de chaque côté du planétaire sur un diamètre. Avec les nombres du manuel, on trouverait Z20 = 89 − 37 = 52 dents, et non 15 : ce planétaire serait presque aussi large que le satellite et n'engrènerait pas avec la couronne. Le contrôle est simple : Z37 − Z20 doit être **pair**, puisque c'est 2 × Z19.
:::

::: verifie
Un autre train a une couronne de 70 dents et un planétaire de 20 dents. Combien de dents pour chaque satellite ?
---
Z37 = Z20 + 2 × Zs donne Zs = (70 − 20) / 2 = **25 dents**. On soustrait d'abord les dents du planétaire, puis on divise par 2 parce que le satellite compte deux fois. Contrôle : 20 + 2 × 25 = 70, et 70 − 20 = 50 est bien pair.
:::

## ➗ La formule de Willis : le rapport d'un étage et du palan

Dans le palan, la couronne est bloquée, le planétaire (20) reçoit la rotation du moteur et le porte-satellites (16) la restitue. Les satellites tournent sur eux-mêmes et autour du centre à la fois.

Comment calculer la vitesse de sortie, alors que les roues ne tournent pas toutes autour d'un axe fixe ?

::: definition La formule de Willis
On repère les vitesses de rotation par rapport au bâti : n pour une roue, n_ps pour le porte-satellites. Pour les deux roues extrêmes A (entrée) et B (l'autre roue centrale), le manuel donne :

$$ (n_B − n_ps) / (n_A − n_ps) = (−1)^k × Produit des Z menantes / Produit des Z menées $$

où **k** est le nombre de **contacts extérieurs** de la chaîne de A vers B. Le membre de droite est la formule du train ordinaire de la boîte de vitesses : la formule de Willis revient à regarder le train **depuis le porte-satellites**, comme s'il était immobile.
:::

::: exemple Le rapport du premier étage
A = planétaire (20), B = couronne (37). La couronne est bloquée : n37 = 0.

1. **Contacts.** De 20 vers 37, la chaîne passe par le satellite (19) : le contact 20/19 est extérieur, le contact 19/37 est intérieur. Donc k = 1.
2. **Dents.** Les menantes sont 20 et 19, les menées 19 et 37 : le satellite se simplifie, il reste Z20 / Z37 = 15 / 89.
3. **Équation.** (0 − n_ps) / (n20 − n_ps) = −15 / 89, donc 89 × n_ps = 15 × (n20 − n_ps), soit 104 × n_ps = 15 × n20.
4. **Rapport d'étage.** r1 = n_ps / n20 = 15 / 104 ≈ **0,144**. Il est positif : le porte-satellites tourne dans le **même sens** que le planétaire, environ 7 fois plus lentement.
5. **Rapport global.** Le second étage est identique, et son entrée est la sortie du premier (principe du double train en série) : r = r1 × r2 = (15 / 104)² ≈ **0,0208**, soit environ 1 / 48.

:::

::: piege Le résultat dépend de la pièce bloquée
Appliquer la formule sans tenir compte du porte-satellites, c'est lire n37 / n20 = −15 / 89 ≈ −0,169 : c'est le rapport quand le **porte-satellites** est bloqué, avec un signe négatif. Ici la couronne est bloquée et le porte-satellites tourne : le rapport est 15 / 104, positif et un peu plus petit. Avant de calculer, on écrit toujours quelle pièce est fixe, laquelle est l'entrée, laquelle est la sortie.
:::

::: propriete Les trois cas du train
Avec Z1 le planétaire et Z4 la couronne (notations de la synthèse), le rapport dépend de la partie bloquée :

| Partie bloquée | Entrée | Sortie | Rapport |
| --- | --- | --- | --- |
| Couronne (4) | planétaire (1) | porte-satellites | Z1 / (Z1 + Z4) |
| Planétaire (1) | couronne (4) | porte-satellites | Z4 / (Z1 + Z4) |
| Porte-satellites | planétaire (1) | couronne (4) | −Z1 / Z4 |

Avec Z1 = 15 et Z4 = 89 : 0,144 (le cas du palan), 0,856, et −0,169. Le signe négatif du dernier cas dit que la sortie tourne en **sens inverse** : porte-satellites bloqué, le train se comporte comme un train ordinaire. Les deux premiers rapports s'ajoutent à 1 : c'est un contrôle.
:::

::: verifie
Un étage a un planétaire de 20 dents et une couronne de 60 dents ; la couronne est bloquée et le planétaire est l'entrée. Quel est le rapport vers le porte-satellites, et dans quel sens tourne-t-il ?
---
Rapport = Z1 / (Z1 + Z4) = 20 / (20 + 60) = **0,25** : couronne bloquée, c'est le premier cas du tableau, que la formule de Willis établit avec k = 1. Il est positif, donc le porte-satellites tourne dans le même sens que le planétaire, quatre fois plus lentement.
:::

## 🏋️ De la noix au moteur : vitesse, puissance, charge

Le manuel donne la vitesse de levage V = 3,6 m/min, le diamètre d'enroulement de la chaîne sur la noix d5 = 42 mm, la puissance du moteur Pm = 800 W et le rendement du palan η = 0,75. Il demande la vitesse de la noix, celle du moteur et la charge maximale.

Quelles relations relient ces grandeurs ?

::: definition Quatre relations de puissance et de vitesse
La synthèse du thème donne les relations suivantes.

- Vitesse d'un point d'un lien flexible (courroie ou chaîne) sur une poulie ou un pignon : V = (d / 2) × ω = R × ω.
- Puissance d'une force : P = F × V, avec P en W, F en N et V en m/s.
- Puissance d'un couple : P = C × ω, avec ω = 2π × N / 60 (ω en rad/s, N en tr/min).
- Rendement : η = P sortie / P entrée.

Une puissance s'exprime aussi en cheval : 1 cv = 736 W.
:::

::: exemple Du palan au moteur (valeurs du manuel)
1. **Vitesse de la noix.** Les unités d'abord : V = 3,6 m/min = 0,06 m/s et R5 = 0,021 m. ω5 = V / R5 = 0,06 / 0,021 ≈ 2,857 rad/s, donc N5 = 60 × ω5 / (2π) ≈ **27,3 tr/min**.
2. **Vitesse du moteur.** Le frein et le limiteur ne changent pas la vitesse : le moteur tourne comme le planétaire (20). Le réducteur ralentit de 0,0208 : N moteur = 27,28 / 0,0208 ≈ **1 312 tr/min**.
3. **Puissance utile.** Le rendement dit ce qui arrive à la charge : P utile = η × Pm = 0,75 × 800 = 600 W.
4. **Charge maximale.** F = P utile / V = 600 / 0,06 = **10 000 N**, soit 1 000 kg avec g = 10 N/kg : c'est la charge maximale du dossier.
5. **En chevaux.** 800 W / 736 ≈ 1,09 cv, puisque 1 cv = 736 W.

:::

::: piege Les mètres par minute ne vont pas avec les watts
Diviser 600 W par 3,6 donnerait 167 N, soit seulement 17 kg : P = F × V suppose V en **m/s**. De même, prendre le diamètre à la place du rayon dans V = (d / 2) × ω double le rayon et divise N5 par deux. On convertit les unités, puis on vérifie l'ordre de grandeur : ici 10 000 N pour une tonne.
:::

::: verifie
Un autre palan lève à V = 6 m/min avec une noix de diamètre d'enroulement 60 mm. Quelle est la vitesse de rotation de sa noix ?
---
V = 6 m/min : un tour de noix enroule π × d = π × 0,060 ≈ 0,1885 m de chaîne, donc N = 6 / 0,1885 ≈ **31,8 tr/min**. Même résultat par V = (d / 2) × ω : ω = 0,10 / 0,030 ≈ 3,33 rad/s, soit 31,8 tr/min.
:::

## 🗂️ Synthèse : classer les transmissions

Depuis le début du thème, on a rencontré des organes très différents : un embrayage, un limiteur, un frein, une boîte de vitesses, un train épicycloïdal, une vis, une bielle. Le manuel les range dans un organigramme.

Selon quels critères, et dans quelle case va chacun ?

::: definition La fonction transmission de puissance et son organigramme
La **transmission de puissance** est la fonction la plus courante des chaînes mécaniques : entraîner un **arbre récepteur** à partir d'un **arbre moteur** plus ou moins éloigné, par des moyens de transmission (engrenages, poulies-courroie, pignons-chaîne, embrayage...). Le manuel classe d'abord selon que le mouvement **change de nature** ou non, puis selon que la **vitesse angulaire** change ou non.
:::

::: figure L'organigramme de la synthèse. La transmission sans transformation de mouvement garde une rotation à la sortie ; on y distingue les organes qui laissent la vitesse angulaire inchangée de ceux qui la modifient. La transmission avec transformation change la nature du mouvement
<svg viewBox="0 0 340 240"><title>Organigramme de la transmission de puissance sans et avec transformation de mouvement</title><rect x="65" y="6" width="210" height="26" fill="#e2e8f0" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round" /><text x="170" y="23" font-size="11" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Transmission de puissance</text><line x1="170" y1="32" x2="170" y2="42" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round" /><line x1="110" y1="42" x2="280" y2="42" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round" /><line x1="110" y1="42" x2="110" y2="52" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round" /><line x1="280" y1="42" x2="280" y2="52" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round" /><rect x="5" y="52" width="210" height="28" fill="#bbf7d0" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round" /><text x="110" y="70" font-size="10.5" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Sans transformation de mouvement</text><rect x="225" y="52" width="110" height="28" fill="#fdba74" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round" /><text x="280" y="64" font-size="9.5" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Avec transformation</text><text x="280" y="75" font-size="9.5" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">de mouvement</text><line x1="110" y1="80" x2="110" y2="90" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round" /><line x1="58" y1="90" x2="164" y2="90" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round" /><line x1="58" y1="90" x2="58" y2="100" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round" /><line x1="164" y1="90" x2="164" y2="100" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round" /><line x1="280" y1="80" x2="280" y2="100" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round" /><rect x="5" y="100" width="106" height="134" fill="#dcfce7" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round" /><text x="58" y="114" font-size="9.5" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Sans modification</text><text x="58" y="125" font-size="9.5" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">de vitesse angulaire</text><text x="58" y="146" font-size="9.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Accouplements</text><text x="58" y="163" font-size="9.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Embrayages</text><text x="58" y="180" font-size="9.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Limiteurs de couple</text><text x="58" y="197" font-size="9.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Freins</text><rect x="115" y="100" width="100" height="134" fill="#dcfce7" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round" /><text x="165" y="114" font-size="9.5" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Avec modification</text><text x="165" y="125" font-size="9.5" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">de vitesse angulaire</text><text x="165" y="146" font-size="9.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Boîtes de vitesses</text><text x="165" y="160" font-size="9.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Trains</text><text x="165" y="178" font-size="9.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">épicycloïdaux</text><rect x="225" y="100" width="110" height="134" fill="#ffedd5" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round" /><text x="280" y="122" font-size="9.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Vis-écrou</text><text x="280" y="141" font-size="9.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Excentrique</text><text x="280" y="160" font-size="9.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Cames</text><text x="280" y="179" font-size="9.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Bielle-manivelle</text><text x="280" y="198" font-size="9.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Pignon-crémaillère</text><text x="280" y="217" font-size="9.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Liens flexibles</text></svg>
:::

Les accouplements se rangent en trois familles, repérées par leur symbole : **rigides**, **élastiques** et **flexibles**. L'embrayage transmet la puissance à volonté et se dit **progressif** (par adhérence) ou **instantané** (par obstacle). Le limiteur interrompt la transmission au-delà d'un couple préréglé. Le frein ralentit ou arrête.

::: exemple Classer les organes du palan
1. **Réducteur à double train épicycloïdal** : il modifie la vitesse angulaire (il la divise par 48), la sortie reste une rotation : sans transformation, **avec modification** de vitesse.
2. **Limiteur de couple** : il transmet la rotation telle quelle, tant que le couple est inférieur au couple préréglé : sans transformation, **sans modification** de vitesse.
3. **Frein à disque** : il ralentit ou arrête une rotation sans la convertir en autre chose : même case que le limiteur.
4. **Noix et chaîne** : la rotation de la noix devient une translation de la chaîne, V = R × ω : **avec transformation** de mouvement (le manuel range les liens flexibles de ce côté).

:::

::: piege Un frein n'est pas un réducteur
Frein et réducteur ralentissent tous deux, mais pas de la même façon : un frein dissipe de l'énergie en chaleur et retient ; un réducteur **transmet** la puissance en changeant le rapport vitesse-couple. De plus, un embrayage, un limiteur ou un frein ne changent pas le rapport des vitesses quand ils transmettent : les ranger avec les boîtes de vitesses est une erreur de branche.
:::

::: verifie
Dans l'organigramme, dans quelle branche range-t-on la boîte de vitesses, et dans laquelle l'embrayage ?
---
La boîte de vitesses est dans la transmission **sans transformation de mouvement, avec modification** de la vitesse angulaire (elle change le rapport). L'embrayage est dans la même transmission sans transformation, mais **sans modification** de vitesse (il relie ou coupe).
:::

## 🔗 Synthèse : une seule formule de couple pour quatre organes

L'embrayage, le limiteur, le frein du palan : tous transmettent un couple par frottement. Le manuel donne quatre formules qui se ressemblent beaucoup.

Qu'ont-elles en commun, et que change un cône à la place d'un plan ?

::: definition La famille des formules de couple
Pour des surfaces **planes**, l'effort de frottement multiplié par le rayon d'action donne le couple. F désigne l'effort presseur : c'est le N du chapitre sur l'embrayage, que la synthèse du manuel note N dans la formule et F dans sa légende, ici écrit F pour ne pas le confondre avec une vitesse de rotation.

- embrayage plan : Ct = (2/3) × n × f × F × (R³ − r³) / (R² − r²) ;
- limiteur : Ct = (2/3) × F × f × (R³ − r³) / (R² − r²) ;
- frein à disque : Cf = (2/3) × F × n × f × (R³ − r³) / (R² − r²).

Pour des surfaces **coniques**, le manuel écrit :

$$ Ct = (2/3) × (F / sin α) × f × (R³ − r³) / (R² − r²) $$

où F est l'effort axial et α l'angle de la surface avec l'axe (le manuel ne légende pas α : c'est le repère habituel, principe).
:::

::: figure Demi-coupe de deux surfaces de friction. À gauche, plane : la surface (en rouge) est perpendiculaire à l'axe, α = 90°. À droite, conique : la surface est inclinée d'un angle α < 90° avec l'axe. La force F est axiale dans les deux cas
<svg viewBox="0 0 340 188"><title>Surface de friction plane et surface de friction conique en demi-coupe</title><line x1="10" y1="160" x2="160" y2="160" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round" stroke-dasharray="8 3 2 3" /><polygon points="40 50 90 50 90 140 40 140" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.4" stroke-linejoin="round" stroke-linecap="round" /><polygon points="90 50 130 50 130 140 90 140" fill="#bbf7d0" stroke="#0f172a" stroke-width="1.4" stroke-linejoin="round" stroke-linecap="round" /><line x1="90" y1="50" x2="90" y2="140" stroke="#dc2626" stroke-width="3.2" stroke-linecap="round" /><line x1="8" y1="95" x2="34" y2="95" stroke="#0f172a" stroke-width="1.8" stroke-linecap="round" /><polygon points="40 95 34 98 34 92" fill="#0f172a" stroke="#0f172a" stroke-width="1" stroke-linejoin="round" stroke-linecap="round" /><text x="20" y="86" font-size="11" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">F</text><polyline points="90 128 102 128 102 140 90 140" fill="none" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round" stroke-linecap="round" /><text x="100" y="175" font-size="11" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">α = 90°</text><text x="85" y="42" font-size="11" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Plane</text><line x1="180" y1="160" x2="335" y2="160" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round" stroke-dasharray="8 3 2 3" /><polygon points="205 140 235 140 315 93.8 315 56 205 56" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.4" stroke-linejoin="round" stroke-linecap="round" /><polygon points="235 140 315 93.8 330 93.8 330 140 235 140" fill="#bbf7d0" stroke="#0f172a" stroke-width="1.4" stroke-linejoin="round" stroke-linecap="round" /><line x1="235" y1="140" x2="315" y2="93.8" stroke="#dc2626" stroke-width="3.2" stroke-linecap="round" /><line x1="235" y1="140" x2="297" y2="140" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round" stroke-dasharray="4 3" /><path d="M 271 140 A 36 36 0 0 0 266.2 122" fill="none" stroke="#0f172a" stroke-width="1.4"/><text x="287" y="132" font-size="12" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">α</text><line x1="176" y1="95" x2="199" y2="95" stroke="#0f172a" stroke-width="1.8" stroke-linecap="round" /><polygon points="205 95 199 98 199 92" fill="#0f172a" stroke="#0f172a" stroke-width="1" stroke-linejoin="round" stroke-linecap="round" /><text x="190" y="86" font-size="11" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">F</text><text x="265" y="42" font-size="11" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Conique</text><text x="265" y="175" font-size="11" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">α < 90°</text><line x1="170" y1="36" x2="170" y2="180" stroke="#94a3b8" stroke-width="1.0" stroke-linecap="round" stroke-dasharray="4 4" /></svg>
:::

Avec α = 90°, sin α = 1 et la formule du cône redevient celle d'une seule surface plane : les formules forment bien une famille.

::: exemple Plan ou cône ? (illustration)
Même effort F = 200 N, même f = 0,3, mêmes rayons R = 45 mm et r = 30 mm (donc (2/3) × (R³ − r³) / (R² − r²) = 38 mm, comme à la section 3).

1. **Surface plane**, une seule surface : Ct = 0,3 × 200 × 38 = 2 280 N·mm = **2,28 N·m**.
2. **Cône d'angle α = 30°** : sin 30° = 0,5, donc F / sin α = 400 N. Ct = 0,3 × 400 × 38 = 4 560 N·mm = **4,56 N·m**.
3. **Comparaison.** Le cône transmet **deux fois plus** pour le même effort axial : il presse plus fort sur ses surfaces inclinées, car 1 / sin 30° = 2.

:::

::: piege Le cône ne diminue pas le couple
Utiliser F × sin α au lieu de F / sin α donnerait 100 N, donc un couple de 1,14 N·m et la conclusion fausse que le cône est moins efficace. Comme sin α est inférieur à 1, **diviser** par lui **augmente** l'effort. Plus l'angle est petit, plus l'effet est fort.
:::

::: verifie
Pour α = 90°, que devient la formule du cône, et à quoi correspond cette surface ?
---
sin 90° = 1, donc F / sin α = F : on retrouve la formule d'**une** surface plane (n = 1). Un cône d'angle 90° avec l'axe est un simple plan perpendiculaire à l'axe.
:::

## 🔄 Synthèse : de la rotation à la translation

La noix du palan transforme la rotation en translation de la chaîne, avec V = R × ω. La synthèse en cite d'autres : la vis-écrou et le pignon-crémaillère.

Quelle relation donne le déplacement obtenu pour une rotation donnée, et quel piège guette l'unité de l'angle ?

::: definition Déplacement pour une rotation θ
Pour un mécanisme qui transforme une rotation en translation, le **déplacement** x est proportionnel à l'angle θ **exprimé en radians** :

- **vis-écrou** : x = (P / 2π) × θ, où P est le pas de la vis ; un tour (θ = 2π) donne x = P ;
- **pignon-crémaillère** : x = R × θ, où R est le rayon du pignon ; la vitesse linéaire vaut V = (d / 2) × ω = R × ω ;
- **lien flexible** (courroie ou chaîne) : V = (d / 2) × ω = R × ω pour un point du lien.

Le facteur qui multiplie θ est un **rayon équivalent** : R, ou P / 2π pour la vis.
:::

::: figure Pignon-crémaillère. Le pignon, de rayon R, tourne d'un angle θ ; son contact avec la crémaillère avance de x, longueur de l'arc de rayon R sur l'angle θ
<svg viewBox="0 0 340 160"><title>Un pignon de rayon R qui fait avancer une crémaillère de x</title><rect x="20" y="98" width="290" height="18" fill="#e2e8f0" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round" /><line x1="24" y1="98" x2="24" y2="116" stroke="#0f172a" stroke-width="0.8" stroke-linecap="round" /><line x1="40" y1="98" x2="40" y2="116" stroke="#0f172a" stroke-width="0.8" stroke-linecap="round" /><line x1="56" y1="98" x2="56" y2="116" stroke="#0f172a" stroke-width="0.8" stroke-linecap="round" /><line x1="72" y1="98" x2="72" y2="116" stroke="#0f172a" stroke-width="0.8" stroke-linecap="round" /><line x1="88" y1="98" x2="88" y2="116" stroke="#0f172a" stroke-width="0.8" stroke-linecap="round" /><line x1="104" y1="98" x2="104" y2="116" stroke="#0f172a" stroke-width="0.8" stroke-linecap="round" /><line x1="120" y1="98" x2="120" y2="116" stroke="#0f172a" stroke-width="0.8" stroke-linecap="round" /><line x1="136" y1="98" x2="136" y2="116" stroke="#0f172a" stroke-width="0.8" stroke-linecap="round" /><line x1="152" y1="98" x2="152" y2="116" stroke="#0f172a" stroke-width="0.8" stroke-linecap="round" /><line x1="168" y1="98" x2="168" y2="116" stroke="#0f172a" stroke-width="0.8" stroke-linecap="round" /><line x1="184" y1="98" x2="184" y2="116" stroke="#0f172a" stroke-width="0.8" stroke-linecap="round" /><line x1="200" y1="98" x2="200" y2="116" stroke="#0f172a" stroke-width="0.8" stroke-linecap="round" /><line x1="216" y1="98" x2="216" y2="116" stroke="#0f172a" stroke-width="0.8" stroke-linecap="round" /><line x1="232" y1="98" x2="232" y2="116" stroke="#0f172a" stroke-width="0.8" stroke-linecap="round" /><line x1="248" y1="98" x2="248" y2="116" stroke="#0f172a" stroke-width="0.8" stroke-linecap="round" /><line x1="264" y1="98" x2="264" y2="116" stroke="#0f172a" stroke-width="0.8" stroke-linecap="round" /><line x1="280" y1="98" x2="280" y2="116" stroke="#0f172a" stroke-width="0.8" stroke-linecap="round" /><line x1="296" y1="98" x2="296" y2="116" stroke="#0f172a" stroke-width="0.8" stroke-linecap="round" /><circle cx="100" cy="62" r="36" fill="#fde68a" stroke="#0f172a" stroke-width="1.6"/><circle cx="100" cy="62" r="2.5" fill="#0f172a" stroke="#0f172a" stroke-width="1.6"/><line x1="100" y1="62" x2="100" y2="98" stroke="#64748b" stroke-width="1.4" stroke-linecap="round" stroke-dasharray="4 3" /><line x1="100" y1="62" x2="136" y2="62" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round" /><path d="M 100 80 A 18 18 0 0 0 118 62" fill="none" stroke="#0f172a" stroke-width="1.4"/><text x="124" y="86" font-size="12" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">θ</text><text x="116" y="56" font-size="11" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">R</text><line x1="100" y1="116" x2="100" y2="132" stroke="#64748b" stroke-width="1.4" stroke-linecap="round" stroke-dasharray="4 3" /><line x1="156.5" y1="116" x2="156.5" y2="132" stroke="#0f172a" stroke-width="1.8" stroke-linecap="round" /><line x1="101" y1="128" x2="149.5" y2="128" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round" /><polygon points="155.5 128 149.5 131 149.5 125" fill="#0f172a" stroke="#0f172a" stroke-width="1" stroke-linejoin="round" stroke-linecap="round" /><text x="128.3" y="144" font-size="11" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">x = R × θ</text><text x="260" y="40" font-size="10" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Crémaillère</text><line x1="240" y1="46" x2="240" y2="100" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round" /><text x="100" y="20" font-size="10" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Pignon</text></svg>
:::

::: exemple Deux déplacements (illustration)
1. **Vis-écrou** : pas P = 4 mm, la vis fait 3 tours, soit θ = 3 × 2π = 6π rad. x = (4 / 2π) × 6π = **12 mm**, ce qui revient à 3 × P : le pas est le déplacement d'un tour.
2. **Pignon-crémaillère** : R = 20 mm, θ = 90° = π / 2 rad. x = 20 × π / 2 ≈ **31,4 mm**. L'angle est converti en radians **avant** de multiplier.
3. **Contrôle** : un tour complet du pignon donne x = 2π × R ≈ 125,7 mm, la circonférence : un quart de tour en donne le quart, soit 31,4 mm.

:::

::: piege L'angle en degrés ne se multiplie pas par le rayon
Écrire x = R × θ avec θ = 90 donnerait x = 20 × 90 = 1 800 mm, environ 57 fois trop. Les formules du manuel supposent θ en **radians** (le manuel parle de degrés pour θ, mais x = R × θ n'est vrai qu'en radians). On convertit avec 180° = π rad.
:::

::: verifie
Une vis de pas 6 mm tourne de 1,5 tour. De combien l'écrou avance-t-il, par x = (P / 2π) × θ ?
---
θ = 1,5 × 2π = 3π rad, donc x = (6 / 2π) × 3π = **9 mm**. On retrouve 1,5 × P : un tour vaut 2π radians, que la formule divise par 2π.
:::

## 📏 Synthèse : la course de l'excentrique et de la bielle-manivelle

Pour obtenir un va-et-vient régulier à partir d'une rotation continue, on peut utiliser un excentrique, une came ou une bielle-manivelle. Le manuel donne la course de deux d'entre eux.

Quelle longueur dans le dessin fixe la distance parcourue ?

::: definition Course et familles de cames
La **course** C est la distance parcourue par la pièce en translation entre ses deux positions extrêmes.

- **Excentrique** : un disque dont l'axe de rotation est décalé de la distance e (l'**excentricité**) par rapport à son centre : C = 2 × e.
- **Bielle-manivelle** : la manivelle (rayon R = OA) fait tourner la bielle (longueur L = AB), qui pousse le coulisseau ou le piston : C = 2 × R.
- **Cames** : le manuel en cite trois familles, **à disque**, **à tambour** et **à rainure**, sans donner de loi de levée.
:::

::: figure À gauche, la bielle-manivelle en ses deux positions extrêmes : le point B est en haut quand A est au plus haut, en bas quand A est au plus bas, et la distance entre les deux est la course C = 2R. À droite, l'excentrique : le disque, de centre décalé de e par rapport à l'axe, monte puis descend, et la course est 2e
<svg viewBox="0 0 340 232"><title>Course d'une bielle-manivelle et d'un excentrique</title><circle cx="80" cy="170" r="40" fill="none" stroke="#64748b" stroke-width="1.2" stroke-dasharray="4 3"/><circle cx="80" cy="170" r="3" fill="#0f172a" stroke="#0f172a" stroke-width="1.6"/><line x1="80" y1="170" x2="120" y2="170" stroke="#15803d" stroke-width="1.8" stroke-linecap="round" /><text x="102" y="164" font-size="10.5" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">R</text><line x1="77" y1="130" x2="77" y2="30" stroke="#1d4ed8" stroke-width="2.2" stroke-linecap="round" /><line x1="83" y1="210" x2="83" y2="110" stroke="#ea580c" stroke-width="2.2" stroke-linecap="round" /><rect x="68" y="21" width="24" height="12" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.4" stroke-linejoin="round" /><rect x="68" y="101" width="24" height="12" fill="#fed7aa" stroke="#0f172a" stroke-width="1.4" stroke-linejoin="round" fill-opacity="0.85"/><circle cx="80" cy="130" r="3" fill="#1d4ed8" stroke="#0f172a" stroke-width="1.6"/><circle cx="80" cy="210" r="3" fill="#ea580c" stroke="#0f172a" stroke-width="1.6"/><line x1="128" y1="27" x2="128" y2="107" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round" /><line x1="128" y1="62" x2="128" y2="31" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round" /><polygon points="128 27 130 31 126 31" fill="#0f172a" stroke="#0f172a" stroke-width="1" stroke-linejoin="round" stroke-linecap="round" /><line x1="128" y1="78" x2="128" y2="103" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round" /><polygon points="128 107 126 103 130 103" fill="#0f172a" stroke="#0f172a" stroke-width="1" stroke-linejoin="round" stroke-linecap="round" /><text x="142" y="74" font-size="11" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">C</text><line x1="94" y1="27" x2="132" y2="27" stroke="#64748b" stroke-width="0.8" stroke-linecap="round" stroke-dasharray="3 3" /><line x1="94" y1="107" x2="132" y2="107" stroke="#64748b" stroke-width="0.8" stroke-linecap="round" stroke-dasharray="3 3" /><text x="80" y="224" font-size="10.5" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Bielle-manivelle : C = 2R</text><circle cx="262" cy="152" r="36" fill="none" stroke="#ea580c" stroke-width="1.4" stroke-dasharray="5 3"/><circle cx="262" cy="124" r="36" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.6"/><circle cx="262" cy="138" r="3" fill="#0f172a" stroke="#0f172a" stroke-width="1.6"/><line x1="262" y1="138" x2="262" y2="124" stroke="#15803d" stroke-width="2.4" stroke-linecap="round" /><text x="274" y="135" font-size="10.5" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">e</text><line x1="240" y1="88" x2="284" y2="88" stroke="#1d4ed8" stroke-width="2.2" stroke-linecap="round" /><line x1="240" y1="116" x2="284" y2="116" stroke="#ea580c" stroke-width="2.2" stroke-linecap="round" /><line x1="312" y1="88" x2="312" y2="116" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round" /><line x1="312" y1="99" x2="312" y2="92" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round" /><polygon points="312 88 314 92 310 92" fill="#0f172a" stroke="#0f172a" stroke-width="1" stroke-linejoin="round" stroke-linecap="round" /><line x1="312" y1="105" x2="312" y2="112" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round" /><polygon points="312 116 310 112 314 112" fill="#0f172a" stroke="#0f172a" stroke-width="1" stroke-linejoin="round" stroke-linecap="round" /><text x="314" y="132" font-size="11" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">C</text><text x="262" y="224" font-size="10.5" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Excentrique : C = 2e</text><line x1="190" y1="18" x2="190" y2="214" stroke="#94a3b8" stroke-width="1.0" stroke-linecap="round" stroke-dasharray="4 4" /></svg>
:::

Dans les deux dessins, la course est le double d'une longueur de décalage (R ou e), et la longueur de la bielle (L) n'y intervient pas.

::: exemple Lire une course (illustration)
1. **Bielle-manivelle** : R = 40 mm et L = 100 mm. Les deux positions extrêmes de B diffèrent de (L + R) − (L − R) = 2R, donc C = **80 mm**. L ne figure pas dans le résultat.
2. **Excentrique** : le centre du disque est à e = 14 mm de l'axe ; le point haut du disque est au plus haut quand le centre est au-dessus de l'axe, au plus bas quand il est en dessous : C = 2 × 14 = **28 mm**.
3. **Sens inverse** : pour une course voulue de 60 mm, il faut e = 30 mm ou R = 30 mm.

:::

::: piege La bielle ne fixe pas la course
On croit que la course dépend de la longueur de la bielle, parce que c'est la pièce la plus visible. Une bielle plus longue éloigne le piston de l'axe mais ne change pas la distance entre ses deux positions extrêmes : seul le **rayon de la manivelle** compte.
:::

::: verifie
Un excentrique doit donner une course de 18 mm. Quelle excentricité faut-il ?
---
C = 2 × e donne e = 18 / 2 = **9 mm**. La course est le double de l'excentricité, parce que le point haut du disque s'élève de e au-dessus de l'axe puis descend de e en dessous.
:::

## 🔥 Synthèse : machines thermiques et cylindrée

Un moteur d'automobile transforme de l'énergie thermique en énergie mécanique. Le manuel définit les machines thermiques, rappelle les cycles à quatre et à deux temps, et donne deux formules de cylindrée.

Que mesure la cylindrée, et comment la calcule-t-on à partir du cylindre ?

::: definition Machine thermique et cylindrée
Une **machine thermique** est un convertisseur d'énergie qui transforme l'énergie thermique en énergie mécanique ou inversement. Le **moteur à explosion** en est un exemple :

- **4 temps** : le cycle comprend quatre phases, **admission**, **compression**, **détente** et **échappement** ;
- **2 temps** : le cycle n'a que deux temps, plusieurs phases étant faites en même temps.

La **cylindrée** est le **volume balayé par le piston** au cours d'une course. Pour un cylindre d'alésage D (diamètre) et de course L :

$$ V = π × D² × L / 4 $$

La cylindrée totale est C = V × n, avec n le nombre de cylindres (le manuel note C la cylindrée, qui n'est ici ni une course ni un couple).
:::

::: figure Un cylindre avec son piston aux deux positions extrêmes, le point mort haut (PMH) et le point mort bas (PMB). Le volume balayé (en bleu) est un cylindre de diamètre D, l'alésage, et de hauteur L, la course
<svg viewBox="0 0 340 224"><title>Cylindre, piston aux points morts haut et bas, alésage D et course L</title><rect x="92" y="76" width="96" height="74" fill="#bfdbfe" stroke="#0f172a" stroke-width="0.8" stroke-linejoin="round" fill-opacity="0.8"/><polyline points="90 30 90 208 190 208 190 30" fill="none" stroke="#0f172a" stroke-width="2.2" stroke-linejoin="round" stroke-linecap="round" /><rect x="92" y="62" width="96" height="14" fill="#e2e8f0" stroke="#0f172a" stroke-width="1.4" stroke-linejoin="round" stroke-dasharray="5 3"/><rect x="92" y="150" width="96" height="14" fill="#cbd5e1" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round" /><text x="82" y="73" font-size="10" font-weight="700" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">PMH</text><text x="82" y="161" font-size="10" font-weight="700" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">PMB</text><line x1="90" y1="20" x2="190" y2="20" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round" /><line x1="120" y1="20" x2="94" y2="20" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round" /><polygon points="90 20 94 18 94 22" fill="#0f172a" stroke="#0f172a" stroke-width="1" stroke-linejoin="round" stroke-linecap="round" /><line x1="160" y1="20" x2="186" y2="20" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round" /><polygon points="190 20 186 22 186 18" fill="#0f172a" stroke="#0f172a" stroke-width="1" stroke-linejoin="round" stroke-linecap="round" /><text x="140" y="15" font-size="11" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">D</text><line x1="218" y1="76" x2="218" y2="164" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round" /><line x1="218" y1="116" x2="218" y2="80" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round" /><polygon points="218 76 220 80 216 80" fill="#0f172a" stroke="#0f172a" stroke-width="1" stroke-linejoin="round" stroke-linecap="round" /><line x1="218" y1="124" x2="218" y2="160" stroke="#0f172a" stroke-width="1.2" stroke-linecap="round" /><polygon points="218 164 216 160 220 160" fill="#0f172a" stroke="#0f172a" stroke-width="1" stroke-linejoin="round" stroke-linecap="round" /><line x1="184" y1="76" x2="223" y2="76" stroke="#64748b" stroke-width="0.8" stroke-linecap="round" stroke-dasharray="3 3" /><line x1="184" y1="164" x2="223" y2="164" stroke="#64748b" stroke-width="0.8" stroke-linecap="round" stroke-dasharray="3 3" /><text x="234" y="124" font-size="11" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">L</text><text x="140" y="128" font-size="10" font-weight="700" text-anchor="middle" fill="#1d4ed8" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">volume balayé</text></svg>
:::

Le volume balayé est celui d'un cylindre droit : aire du disque (π × D² / 4) multipliée par la hauteur L. Le manuel imprime, sous sa figure, une puissance 4 à la place du carré ; la formule exacte est celle du volume d'un cylindre, avec D².

::: exemple Calculer une cylindrée (illustration)
Un moteur à 4 cylindres a un alésage D = 70 mm et une course L = 80 mm.

1. **Un cylindre.** V = π × 70² × 80 / 4 = π × 4 900 × 20 ≈ 307 876 mm³.
2. **Unité.** 1 cm³ = 1 000 mm³ : V ≈ **307,9 cm³** par cylindre.
3. **Total.** C = V × n = 307,9 × 4 ≈ 1 231,5 cm³, soit **1,23 L** environ.

:::

::: piege Le diamètre se met au carré, pas à la puissance 4
Mettre D à la puissance 4 (comme sur la figure du manuel) donnerait un résultat dimensionnellement faux : un volume s'exprime en longueur au cube, ici D² × L. Autre erreur fréquente : oublier le nombre de cylindres, ce qui donne la cylindrée d'un seul.
:::

::: verifie
Un cylindre a un alésage D = 80 mm et une course L = 90 mm. Quel est son volume, en cm³ ?
---
V = π × 80² × 90 / 4 = π × 1 600 × 90 ≈ 452 389 mm³, soit **452,4 cm³** (division par 1 000 pour passer de mm³ à cm³). Le D est au carré : 80² = 6 400.
:::

## 🧭 La méthode qui reste : six marches

Devant un mécanisme de transmission inconnu, tu reprends toujours cet ordre :

1. **Situer** : écrire le FAST, repérer l'entrée et la sortie, ranger l'organe dans l'organigramme.
2. **Frein et limiteur** : commande par électro-aimant et ressort, libre sous tension, freiné hors tension ; Cf et Ct = n × f × F × Rm, avec n le nombre de surfaces.
3. **Train épicycloïdal** : trouver les dents par Z couronne = Z planétaire + 2 × Z satellite, puis nommer la pièce bloquée, l'entrée et la sortie avant d'appliquer Willis.
4. **Chaîne cinématique** : multiplier les rapports d'étage, puis N5 = V / (π × d), N moteur = N5 / r.
5. **Puissance** : P = F × V, P = C × ω, rendement η = P sortie / P entrée, en m/s et en rad/s.
6. **Synthèse** : choisir la formule selon le mécanisme (plan, cône, vis, crémaillère, excentrique, bielle-manivelle) et convertir les unités.

::: retenir
Un frein de palan est **libre sous tension et freiné hors tension** (le ressort serre) ; le limiteur **glisse** au-delà du couple nominal ; un train épicycloïdal à **couronne bloquée** a un rapport **Z1 / (Z1 + Z4)** après avoir trouvé ses dents par **Z couronne = Z planétaire + 2 × Z satellite** ; la charge maximale vient de **P utile = η × Pm = F × V** ; et toutes les formules de couple sont un **effort de frottement multiplié par un rayon d'action**.
:::

> 🏆 Le palan n'a plus de secret : tu sais le freiner, le protéger, calculer sa démultiplication et sa charge, et tu as relié tous les mécanismes du thème dans une même vue. La suite du programme t'attend, avec le comportement des solides déformables.
