# 🖨️ Dans les entrailles de l'imprimante 3D

> 💡 «Tu sais ce que fait une imprimante 3D. L'analyse fonctionnelle interne répond à la question suivante : **par quoi** le fait-elle, et **pourquoi** ce composant-là plutôt qu'un autre ? Ouvre le capot : chaque pièce va se révéler être la réponse à une question précise.»

Le besoin, lui, est déjà exprimé : le cahier des charges fonctionnel le fixe. L'**analyse fonctionnelle interne** consiste à rechercher les **fonctions techniques**, les **solutions constructives** et les **composants** qui satisfont une fonction de service. Trois outils la mènent : les **chaînes fonctionnelles**, le **diagramme F.A.S.T.** et le **dossier technique** de la machine.

## 🖨️ La machine : fondre, déposer, recommencer

L'impression 3D **FDM** (dépôt de filament fondu) consiste à **fondre un filament** puis à le **déposer couche par couche** à l'aide d'une **buse d'impression**. Entre chaque couche, le **plateau descend** pour laisser la place à l'extrusion de la suivante. Le cycle se répète jusqu'à ce que la pièce soit entièrement réalisée.

::: figure Le plateau descend d'une épaisseur de couche à chaque passage : la pièce ne monte pas, c'est le plateau qui s'éloigne de la buse
<svg viewBox="0 0 340 235">
<path d="M160 14 V45" stroke="#0f172a" stroke-width="5" stroke-linecap="round"/>
<rect x="125" y="45" width="70" height="55" fill="#0f6e56" fill-opacity="0.12" stroke="#0f172a" stroke-width="2"/>
<path d="M135 100 L185 100 L170 128 L150 128 Z" fill="#0f6e56" fill-opacity="0.2" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/>
<path d="M160 128 V137" stroke="#0f6e56" stroke-width="4" stroke-linecap="round"/>
<g stroke="#0f172a" stroke-width="1.5" fill="#0f6e56">
<rect x="85" y="137" width="75" height="12" fill-opacity="0.4"/>
<rect x="85" y="149" width="160" height="12" fill-opacity="0.22"/>
<rect x="85" y="161" width="160" height="12" fill-opacity="0.22"/>
<rect x="85" y="173" width="160" height="12" fill-opacity="0.22"/>
</g>
<rect x="65" y="185" width="200" height="14" fill="#94a3b8" fill-opacity="0.45" stroke="#0f172a" stroke-width="2"/>
<path d="M290 148 V192" stroke="#0f172a" stroke-width="2"/>
<path d="M284 188 L290 200 L296 188 Z" fill="#0f172a"/>
<g font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">
<text x="150" y="32" text-anchor="end">filament</text>
<text x="203" y="120">buse</text>
<text x="165" y="219" text-anchor="middle">plateau</text>
<text x="290" y="142" text-anchor="middle">Z</text>
</g>
</svg>
:::

Tout se joue dans la **tête d'impression**. Chacun de ses composants remplit **une** fonction, et une seule :

| Composant                              | Ce qu'il fait, exactement                                              |
| -------------------------------------- | ---------------------------------------------------------------------- |
| **Galet cranté** + **galet presseur**  | pincent le filament et l'avancent ou le reculent **par adhérence**     |
| **Cartouche chauffante**               | **fond** le filament                                                   |
| **Thermistance**                       | **contrôle** la température (c'est un capteur)                         |
| **Buse** Ø 0,4 mm                      | **calibre** la section du filament déposé                              |
| **Ventilateur** + **dissipateur**      | **refroidissent** constamment la tête d'impression                     |
| **Plateau porte-pièce**                | reçoit les couches ; **chauffé**, il améliore l'**adhésion**           |

> ⚠️ Piège classique : croire que la buse fond la matière. Non — c'est la **cartouche chauffante** qui fond, la **buse** ne fait que **calibrer** la section de ce qui sort. Deux fonctions, deux composants.

## 🧭 Trois axes, trois solutions constructives

Pour empiler des couches dans l'espace, il faut trois translations. La machine se les partage : la **tête d'impression** se déplace suivant **X** et **Y**, le **plateau mobile** suivant **Z**.

::: figure Les trois translations ne sont pas portées par le même élément : deux pour la tête, une pour le plateau
<svg viewBox="0 0 340 250">
<path d="M70 80 L250 80 L250 200 L70 200 Z" fill="#0f6e56" fill-opacity="0.06" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/>
<path d="M70 80 L115 45 L295 45 L250 80" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/>
<path d="M250 200 L295 165 L295 45" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/>
<path d="M70 200 L115 165 L295 165 M115 165 L115 45" fill="none" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="5 4"/>
<path d="M95 175 L225 175 L270 140 L140 140 Z" fill="#94a3b8" fill-opacity="0.4" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/>
<rect x="140" y="103" width="46" height="26" fill="#0f6e56" fill-opacity="0.25" stroke="#0f172a" stroke-width="2"/>
<path d="M155 129 L175 129 L167 141 L163 141 Z" fill="#0f6e56" fill-opacity="0.35" stroke="#0f172a" stroke-width="1.5" stroke-linejoin="round"/>
<g stroke="#0f172a" stroke-width="2" fill="#0f172a">
<path d="M104 93 H226"/><path d="M110 89 L100 93 L110 97 Z"/><path d="M220 89 L230 93 L220 97 Z"/>
<path d="M252 141 L286 115"/><path d="M259 138 L248 144 L250 133 Z"/><path d="M279 118 L290 112 L288 123 Z"/>
<path d="M88 168 V126"/><path d="M84 162 L88 172 L92 162 Z"/><path d="M84 132 L88 122 L92 132 Z"/>
</g>
<g font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">
<text x="238" y="97">X</text>
<text x="296" y="110">Y</text>
<text x="88" y="115" text-anchor="middle">Z</text>
<text x="163" y="99" text-anchor="middle" font-size="11">tête</text>
<text x="182" y="192" text-anchor="middle" font-size="11">plateau</text>
</g>
</svg>
:::

Chaque axe a sa propre solution constructive :

- **Axe X** — le **moteur d'axe X** entraîne un **système poulies-courroie** ; la **courroie crantée** est **fixée sur la tête d'impression** et la fait donc translater. Son guidage est assuré par des **douilles à billes**, montées sur la **platine d'axe X**, qui glissent sur **deux colonnes rectifiées**.
- **Axe Y** — le **moteur d'axe Y** entraîne **deux systèmes poulies-courroies** ; la courroie liée à la **platine** assure la translation suivant Y par rapport au bâti.
- **Axe Z** — le **moteur à arbre fileté** transmet sa rotation aux **deux tiges filetées T8** par un **système poulies-courroies**. Les **trois écrous T8**, assemblés sur le plateau mobile, transforment cette rotation en **translation du plateau** suivant Z. Pourquoi **trois** écrous pour **deux** tiges ? Parce que la nomenclature compte un **troisième filetage T8** : l'**arbre du moteur** lui-même. Le plateau est donc entraîné en **trois points**.

| Élément mobile         | X   | Y   | Z   |
| ---------------------- | --- | --- | --- |
| **Tête d'impression**  | ✔   | ✔   | —   |
| **Plateau mobile**     | —   | —   | ✔   |

> ⚠️ Le piège le plus rentable du chapitre : **transmettre n'est pas transformer** — et c'est le **montage**, pas la pièce, qui décide. *Transmettre* conserve la **nature** du mouvement : sur l'axe **Z**, la courroie relie l'arbre moteur aux deux tiges filetées, rotation à l'entrée, rotation à la sortie. *Transformer* la **change** : sur l'axe **X**, la même technologie de courroie est **fixée sur la tête d'impression**, donc rotation à l'entrée, **translation** à la sortie. Le couple tige filetée + écrou T8 transforme lui aussi, sur l'axe Z, juste après la courroie. Une poulie-courroie n'est donc pas « toujours une transmission » : **regarde ce qui entre et ce qui sort**, jamais l'étiquette de la pièce.

## 🤖 Un système automatisé, deux chaînes

::: definition Le système automatisé
Un **système automatisé** est composé de plusieurs éléments qui exécutent un ensemble de **tâches programmées** sans que l'**intervention de l'homme** ne soit nécessaire.
:::

On le décompose toujours en **deux chaînes fonctionnelles** qui travaillent ensemble : la **chaîne d'information**, qui sait, et la **chaîne d'énergie**, qui agit. Le lien décisif entre elles porte un nom : la chaîne d'information envoie des **ordres** à la chaîne d'énergie, et ces ordres arrivent sur le bloc **Distribuer**.

## 📡 La chaîne d'information : Acquérir → Traiter → Communiquer

C'est la partie du système automatisé qui **capte** l'information et qui la **traite**. On la découpe en trois blocs fonctionnels.

::: figure Le sens de lecture ne change jamais : on acquiert d'abord, on traite ensuite, on communique enfin — et c'est de là que partent les ordres
<svg viewBox="0 0 380 210">
<g fill="#0f6e56" fill-opacity="0.12" stroke="#0f172a" stroke-width="2">
<rect x="40" y="64" width="84" height="46"/>
<rect x="148" y="64" width="84" height="46"/>
<rect x="256" y="64" width="84" height="46"/>
</g>
<g stroke="#0f172a" stroke-width="2" fill="#0f172a">
<path d="M124 87 H142"/><path d="M138 83 L148 87 L138 91 Z"/>
<path d="M232 87 H250"/><path d="M246 83 L256 87 L246 91 Z"/>
<path d="M6 87 H34"/><path d="M30 83 L40 87 L30 91 Z"/>
<path d="M340 87 H366"/><path d="M362 83 L372 87 L362 91 Z"/>
<path d="M82 150 V116"/><path d="M78 122 L82 112 L86 122 Z"/>
<path d="M298 110 V148"/><path d="M294 142 L298 152 L302 142 Z"/>
</g>
<g font-size="12" font-weight="700" fill="#0f172a" text-anchor="middle">
<text x="82" y="92">Acquérir</text>
<text x="190" y="92">Traiter</text>
<text x="298" y="92">Communiquer</text>
</g>
<g font-size="11" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">
<text x="6" y="56">G-code</text>
<text x="372" y="56" text-anchor="end">utilisateur</text>
<text x="82" y="166" text-anchor="middle">capteurs</text>
<text x="298" y="172" text-anchor="middle">ordres</text>
</g>
</svg>
:::

::: definition Les trois fonctions de la chaîne d'information

- **Acquérir** : fonction qui permet de **prélever des informations** à l'aide de **capteurs**.
- **Traiter** : c'est la **partie commande**, composée d'un **automate** ou d'un **microcontrôleur**.
- **Communiquer** : cette fonction assure l'**interface** entre l'utilisateur et/ou d'autres systèmes et l'environnement de la partie commande.

:::

Sur l'imprimante 3D, l'entrée est le **programme G-code** et les processeurs sont les suivants :

| Bloc            | Processeur sur l'imprimante 3D                                            |
| --------------- | ------------------------------------------------------------------------- |
| **Acquérir**    | les **capteurs** — trois capteurs fin de course, et la **thermistance**    |
| **Traiter**     | la **carte électronique**                                                 |
| **Communiquer** | les **fils de liaison**, l'information ressortant vers l'**afficheur**     |

> 🗡️ La thermistance mesure une température : elle **prélève une information**. Elle appartient donc à la chaîne d'**information**, bloc **Acquérir** — alors même qu'elle est vissée sur la partie la plus chaude de la chaîne d'énergie.

## ⚡ La chaîne d'énergie : Alimenter → Distribuer → Convertir → Transmettre

On appelle **chaîne d'énergie** l'ensemble des procédés qui vont **réaliser une action**. Quatre blocs, dans cet ordre :

::: figure Les ordres venus de la chaîne d'information n'entrent pas n'importe où : ils arrivent sur Distribuer, qui décide alors de laisser passer l'énergie
<svg viewBox="0 0 400 190">
<g fill="#0f6e56" fill-opacity="0.12" stroke="#0f172a" stroke-width="2">
<rect x="22" y="72" width="76" height="44"/>
<rect x="114" y="72" width="76" height="44"/>
<rect x="206" y="72" width="76" height="44"/>
<rect x="298" y="72" width="76" height="44"/>
</g>
<g stroke="#0f172a" stroke-width="2" fill="#0f172a">
<path d="M2 94 H16"/><path d="M12 90 L22 94 L12 98 Z"/>
<path d="M98 94 H108"/><path d="M104 90 L114 94 L104 98 Z"/>
<path d="M190 94 H200"/><path d="M196 90 L206 94 L196 98 Z"/>
<path d="M282 94 H292"/><path d="M288 90 L298 94 L288 98 Z"/>
<path d="M374 94 H388"/><path d="M384 90 L394 94 L384 98 Z"/>
<path d="M152 34 V66"/><path d="M148 60 L152 70 L156 60 Z"/>
</g>
<g font-size="11" font-weight="700" fill="#0f172a" text-anchor="middle">
<text x="60" y="98">Alimenter</text>
<text x="152" y="98">Distribuer</text>
<text x="244" y="98">Convertir</text>
<text x="336" y="98">Transmettre</text>
</g>
<g font-size="10" font-weight="700" fill="#0f6e56" text-anchor="middle" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">
<text x="12" y="86">EE</text><text x="106" y="86">EE</text><text x="198" y="86">EE</text><text x="290" y="86">EM</text><text x="384" y="86">EM</text>
</g>
<g font-size="11" fill="#0f172a" text-anchor="middle" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">
<text x="152" y="26">ordres</text>
<text x="380" y="118">action</text>
</g>
</svg>
:::

::: definition Les quatre fonctions de la chaîne d'énergie

- **Alimenter** : mise en forme de l'énergie **externe** en une énergie **compatible** pour créer une action.
- **Distribuer** : distribution de l'énergie à l'**actionneur**, réalisée par un distributeur, un contacteur ou une **carte de puissance**.
- **Convertir** : l'organe de conversion d'énergie, appelé **actionneur**, peut être un vérin, un moteur…
- **Transmettre** : fonction remplie par l'ensemble des **organes mécaniques** de transmission de mouvement et d'effort : engrenages, courroies…

:::

| Bloc             | Processeur sur l'imprimante 3D                                   | Énergie en entrée → en sortie |
| ---------------- | ---------------------------------------------------------------- | ------------------------------ |
| **Alimenter**    | le **bloc d'alimentation** (220 V AC du secteur → 24 V DC)       | électrique → électrique        |
| **Distribuer**   | le **contrôleur de moteur pas à pas**                            | électrique → électrique        |
| **Convertir**    | le **moteur pas à pas** (l'actionneur)                           | électrique → **mécanique**     |
| **Transmettre**  | les **éléments de transmission** (poulies, courroies, vis-écrou) | mécanique → mécanique          |

Les liaisons portent donc, dans l'ordre : **EE**, **EE**, **EM**, **EM** — l'énergie ne change de nature qu'au passage de **Convertir**. À chaque conversion et à chaque transmission, une partie de l'énergie est perdue : ce sont les **pertes**, que le diagramme fait sortir des blocs.

> 🗡️ La chaîne d'énergie n'est pas toujours une simple file. Sur l'imprimante 3D, **Distribuer** alimente une **seconde branche de conversion** : une **résistance chauffante** qui convertit l'énergie **électrique** en énergie **thermique** (Eth) pour fondre le filament. Un actionneur ne produit donc pas forcément du mouvement.

## 📋 Le cahier des charges fonctionnel

Le **CdCF** exprime le besoin **avant** toute analyse interne. Chaque **fonction de service** y est décrite par une **expression**, des **critères d'appréciation** et, pour chaque critère, un **niveau** assorti d'une **flexibilité** — la tolérance acceptée autour du niveau. La **fonction principale (FP)** est la raison d'être du produit ; les **fonctions contraintes (FC)** sont les adaptations imposées par le milieu extérieur.

| F.S.    | Expression                                            | Critères                              | Niveaux – flexibilités                      |
| ------- | ----------------------------------------------------- | ------------------------------------- | ------------------------------------------- |
| **FP**  | Permettre l'impression d'une pièce à partir d'un modèle numérique | taille maximale · précision | 200×200×200 mm ±5 mm · 0,2 mm ±0,1 mm       |
| **FC2** | Être compatible avec le fil d'impression              | matière · diamètre du filament        | plastique (PLA-ABS…) · Ø 1,75 mm ±0,05 mm   |
| **FC4** | S'alimenter en énergie électrique                     | tension du secteur · tension d'alimentation | U = 220 V AC ±20 V · UE = 24 V DC ±2 V |
| **FC7** | Communiquer avec l'ordinateur                         | type de fichier · interface · stockage | G-code (ISO) · USB · carte Micro-SD        |
| **FC8** | Être stable                                           | poids · surface d'appui               | 7 kg ±50 g · 3 points au minimum            |

> ⚠️ Ce tableau est un **extrait** : il ne porte que FP, FC2, FC4, FC7 et FC8. L'absence de FC1, FC3, FC5 et FC6 ne signifie pas qu'elles n'existent pas — simplement qu'elles ne sont pas reproduites.

## 🌳 Le diagramme F.A.S.T.

::: definition La méthode F.A.S.T.

La méthode **F.A.S.T.** aide à penser le problème de façon **objective** et détermine la portée du projet en illustrant les **relations logiques** entre les fonctions. Un diagramme F.A.S.T. aborde **trois questions clés** : *Comment accomplit-on cette fonction ?*, *Pourquoi réalise-t-on cette fonction ?*, *Quand on fait cette fonction, quelles autres fonctions doivent être faites ?*

:::

Le diagramme se lit sur **trois colonnes**, de gauche à droite : la **fonction de service**, les **fonctions techniques** qui la satisfont, puis les **solutions technologiques** qui réalisent chacune d'elles. En avançant vers la droite on répond à « **Comment ?** » ; en remontant vers la gauche, à « **Pourquoi ?** » ; la question « **Quand ?** » se lit verticalement, le long des branches parallèles, là où se placent les opérateurs **ET** (les solutions se cumulent) et **OU** (elles s'excluent).

::: figure En allant vers la droite on répond à « Comment ? », en remontant vers la gauche à « Pourquoi ? » — et deux opérateurs relient les branches : ET quand les solutions se cumulent, OU quand elles s'excluent
<svg viewBox="0 0 380 264">
<g font-size="10" font-weight="700" fill="#0f172a" text-anchor="middle">
<text x="60" y="18">Fonction de service</text>
<text x="190" y="18">Fonctions techniques</text>
<text x="319" y="18">Solutions</text>
</g>
<rect x="14" y="100" width="92" height="44" fill="#0f6e56" fill-opacity="0.22" stroke="#0f172a" stroke-width="2"/>
<g fill="#0f6e56" fill-opacity="0.12" stroke="#0f172a" stroke-width="2">
<rect x="140" y="43" width="100" height="34"/>
<rect x="140" y="105" width="100" height="34"/>
<rect x="140" y="173" width="100" height="34"/>
</g>
<g fill="#94a3b8" fill-opacity="0.25" stroke="#0f172a" stroke-width="2">
<rect x="272" y="46" width="94" height="28"/>
<rect x="272" y="92" width="94" height="28"/>
<rect x="272" y="126" width="94" height="28"/>
<rect x="272" y="176" width="94" height="28"/>
</g>
<g fill="none" stroke="#0f172a" stroke-width="2">
<path d="M106 122 H123"/><path d="M123 60 V190"/>
<path d="M123 60 H140"/><path d="M123 122 H140"/><path d="M123 190 H140"/>
<path d="M240 60 H272"/><path d="M240 190 H272"/>
<path d="M240 122 H256"/><path d="M256 106 V140"/><path d="M256 106 H272"/><path d="M256 140 H272"/>
</g>
<g font-size="12" font-weight="700" fill="#0f172a" text-anchor="middle">
<text x="60" y="127">FS</text>
<text x="190" y="65">FT1</text><text x="190" y="127">FT2</text><text x="190" y="195">FT3</text>
<text x="319" y="65">S1</text><text x="319" y="111">S2</text><text x="319" y="145">S3</text><text x="319" y="195">S4</text>
</g>
<g font-size="10" font-weight="700" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">
<text x="119" y="92" text-anchor="end">OU</text>
<text x="252" y="127" text-anchor="end">ET</text>
</g>
<g stroke="#0f172a" stroke-width="2" fill="#0f172a">
<path d="M130 232 H252"/><path d="M246 228 L258 232 L246 236 Z"/>
<path d="M258 252 H136"/><path d="M142 248 L130 252 L142 256 Z"/>
</g>
<g font-size="10" font-weight="700" fill="#0f172a" text-anchor="middle" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">
<text x="194" y="228">Comment ?</text>
<text x="194" y="248">Pourquoi ?</text>
</g>
</svg>
:::

Appliqué à la fonction principale de l'imprimante — **FP1 : permettre l'impression d'une pièce à partir d'un modèle numérique** — l'arbre se déploie en quatre fonctions techniques : **FT1** recevoir et transmettre l'information (c'est la chaîne d'information tout entière qui la remplit), **FT2** déposer la matière sur le plateau porte-pièce, **FT3** déplacer la tête d'impression, **FT4** déplacer le plateau mobile (7) suivant l'axe Z. Les trois dernières se décomposent encore : **FT2** en **FT21** alimenter en fil d'impression, **FT22** chauffer la matière et **FT23** calibrer la matière fondue ; **FT3** en **FT31** déplacer la tête suivant X et **FT32** la déplacer suivant Y. Un cran plus bas encore, on atteint les composants :

| Sous-fonction de **FT21 : alimenter en fil d'impression**       | Composant                                             |
| --------------------------------------------------------------- | ----------------------------------------------------- |
| FT211 : convertir l'énergie électrique en énergie de rotation   | le **moteur pas à pas** de la tête (stator + rotor)   |
| FT212 : guider le fil d'impression                              | les **tubes guides** en PTFE et le raccord pneumatique |
| FT213 : transformer la rotation en translation du filament      | le **galet cranté** et le **galet presseur**          |

| Sous-fonction de **FT31 : déplacer la tête suivant X**          | Composant                                             |
| --------------------------------------------------------------- | ----------------------------------------------------- |
| FT311 : convertir l'énergie électrique en énergie de rotation   | le **moteur d'axe X**                                 |
| FT312 : transformer la rotation en translation de la tête       | le **système poulies-courroie** d'axe X               |
| FT313 : guider la tête en translation                           | les **douilles à billes** sur deux **colonnes rectifiées** |

| Sous-fonction de **FT4 : déplacer le plateau mobile (7) suivant Z** | Composant                                         |
| --------------------------------------------------------------- | ----------------------------------------------------- |
| FT41 : convertir l'énergie électrique en énergie de rotation    | le **moteur d'axe Z** à arbre fileté                  |
| FT42 : transmettre la rotation aux deux tiges filetées          | le **système poulies-courroies** d'axe Z              |
| FT43 : transformer la rotation en translation du plateau        | les **tiges filetées T8** et les **trois écrous T8**  |
| FT44 : guider en translation le plateau                         | les **colonnes de guidage** d'axe Z et leurs douilles |

> 🗡️ Relis ces trois tableaux : c'est la même **grammaire** qui revient. On **convertit** l'électricité en rotation, on **transforme** cette rotation en translation, et on **guide** la translation obtenue. Ce qui change d'un axe à l'autre, c'est ce qui s'intercale : sur **Z**, une étape **transmettre** est nécessaire pour porter la rotation du moteur jusqu'aux deux tiges filetées (FT42) ; sur **X**, la courroie fait le trajet **et** la transformation d'un seul tenant, il n'y a donc pas d'étape *transmettre* ; sur le fil, il n'y en a pas davantage, et le guidage y est même listé **avant** la transformation (FT212 avant FT213). L'ordre des lignes suit le montage, pas une formule. Retiens la grammaire, puis demande-toi à chaque fois : de quoi ai-je besoin **entre** le moteur et l'organe qui bouge ?

> 🏆 Le capot est refermé, héros. Tu sais découper une machine en deux chaînes, nommer le processeur de chaque bloc, lire un extrait de CdCF et dérouler un arbre F.A.S.T. jusqu'au composant. La prochaine séquence te demandera de **lire le dessin** qui porte tous ces repères — et tu sauras déjà à quoi chacun sert.
