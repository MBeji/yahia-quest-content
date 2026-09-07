# ⚙️ Ouvrir la boîte noire — chaînes fonctionnelles et F.A.S.T.

> 💡 «Le cahier des charges dit ce que la machine doit faire. À toi de trouver comment elle le fait — et avec quoi.»

Une micro-fraiseuse usine une pièce presque toute seule : on lui donne un fichier, elle rend un objet. Vue de l'extérieur, c'est une **boîte noire**. Ce chapitre l'ouvre. Tu vas d'abord apprendre à **décomposer** n'importe quel système automatisé en **chaînes fonctionnelles**. Tu descendras ensuite, avec le diagramme **F.A.S.T.**, de la fonction de service jusqu'au composant qui la réalise. C'est la compétence de base du technicien : savoir dire *quelle pièce sert à quoi, et pourquoi elle est là*.

## 🎯 L'analyse fonctionnelle interne : du besoin au composant

Le besoin, lui, est déjà exprimé. Il est consigné dans le **CdCF** (cahier des charges fonctionnel), qui énonce les **fonctions de service** que le produit doit rendre. L'analyse fonctionnelle **interne** commence exactement là où celle-ci s'arrête.

::: definition L'analyse fonctionnelle interne
Elle consiste à **rechercher les fonctions techniques, les solutions constructives et les composants** qui doivent satisfaire aux **fonctions de service**.
:::

Quatre mots à ne jamais confondre — ils forment l'échelle que tu vas descendre :

| Terme                    | Ce qu'il désigne                                        | Sur la micro-fraiseuse            |
| ------------------------ | ------------------------------------------------------- | --------------------------------- |
| **Fonction de service**  | ce que le produit rend à l'utilisateur                  | FS1 : usiner une pièce            |
| **Fonction technique**   | ce que le produit doit faire en interne pour y parvenir | positionner et maintenir l'outil  |
| **Processeur**           | l'organe qui remplit la fonction                        | la broche et son moteur           |
| **Solution / composant** | la pièce réelle qu'on retrouve au dessin d'ensemble     | la pince porte-outil              |

## 🤖 Un système automatisé, deux chaînes

::: definition Système automatisé
Un système automatisé est composé de plusieurs éléments qui exécutent un ensemble de tâches **programmées** sans que l'intervention de l'homme ne soit nécessaire.
:::

Tout système automatisé se lit sur **deux étages** :

- la **chaîne d'information** — la partie qui **capte** l'information et qui la **traite** ;
- la **chaîne d'énergie** — l'ensemble des procédés qui vont **réaliser une action**.

La première **commande**, la seconde **agit**. Entre les deux circulent des **ordres**.

## 📡 La chaîne d'information : Acquérir → Traiter → Communiquer

::: definition Les trois fonctions de la chaîne d'information
- **Acquérir** : fonction qui permet de **prélever des informations** à l'aide de **capteurs**.
- **Traiter** : c'est la **partie commande**, composée d'un **automate** ou d'un **microcontrôleur**.
- **Communiquer** : cette fonction assure l'**interface** entre l'utilisateur, éventuellement d'autres systèmes, et l'environnement de la partie commande.
:::

En **entrée** : la consigne de l'utilisateur et les informations extérieures au système. En **sortie** : une information pour l'utilisateur, et des **ordres pour la chaîne d'énergie**.

::: figure La chaîne d'information de la micro-fraiseuse : elle acquiert, traite, puis renvoie une information à l'utilisateur et des ordres à la chaîne d'énergie.
<svg viewBox="0 0 420 152">
<g fill="#0f6e56" opacity="0.12"><rect x="52" y="46" width="92" height="46" rx="6"/><rect x="164" y="46" width="92" height="46" rx="6"/><rect x="276" y="46" width="92" height="46" rx="6"/></g>
<g fill="none" stroke="#0f172a" stroke-width="2"><rect x="52" y="46" width="92" height="46" rx="6"/><rect x="164" y="46" width="92" height="46" rx="6"/><rect x="276" y="46" width="92" height="46" rx="6"/><path d="M6 69 H42"/><path d="M144 69 H154"/><path d="M256 69 H266"/><path d="M368 69 H400"/><path d="M384 69 V116"/></g>
<g fill="#0f172a"><polygon points="52,69 42,64 42,74"/><polygon points="164,69 154,64 154,74"/><polygon points="276,69 266,64 266,74"/><polygon points="410,69 400,64 400,74"/><polygon points="384,124 379,114 389,114"/></g>
<g font-size="10" font-weight="700" text-anchor="middle" fill="#0f172a"><text x="98" y="74">Acquérir</text><text x="210" y="74">Traiter</text><text x="322" y="74">Communiquer</text></g>
<g font-size="9" fill="#0f6e56" text-anchor="middle"><text x="98" y="110">capteurs, boutons</text><text x="210" y="110">microprocesseur</text><text x="322" y="110">écran, voyants</text></g>
<g font-size="9" fill="#0f172a"><text x="4" y="86">Consignes</text><text x="418" y="60" text-anchor="end">Utilisateur</text><text x="384" y="140" text-anchor="middle">Ordres</text></g>
</svg>
:::

Sur la micro-fraiseuse, l'information d'entrée vient du **programme G-code** de l'utilisateur, de l'environnement et du fonctionnement même de la machine. Les processeurs sont les **interrupteurs, boutons poussoirs et capteurs** (Acquérir), le **microprocesseur** (Traiter), l'**écran et les voyants** (Communiquer).

> 🗡️ Un **capteur** est toujours du côté information, jamais du côté énergie : il ne transporte aucune puissance, il **renseigne**. Le **capteur de portière** de la micro-fraiseuse relève donc de la fonction **Acquérir**.

## ⚡ La chaîne d'énergie : Alimenter → Distribuer → Convertir → Transmettre

::: definition Les quatre fonctions de la chaîne d'énergie
- **Alimenter** (le manuel écrit aussi **Alimenter/Stocker** quand le système stocke son énergie) : mise en forme de l'énergie externe en une énergie **compatible** pour créer une action.
- **Distribuer** : distribution de l'énergie à l'actionneur, réalisée par un **distributeur**, un **contacteur** (interrupteur commandé à distance) ou une **carte de puissance**. C'est ce bloc qui **reçoit les ordres** de la chaîne d'information.
- **Convertir** : l'organe de conversion d'énergie, appelé **actionneur**, peut être un **vérin**, un **moteur**…
- **Transmettre** : fonction remplie par l'ensemble des **organes mécaniques de transmission de mouvement et d'effort** : engrenages, courroies, accouplements, systèmes vis-écrou.
:::

La sortie de la chaîne, c'est la **réalisation de l'action** — et, au passage, des **pertes**.

::: figure La chaîne d'énergie de la micro-fraiseuse : l'énergie reste électrique (EE) jusqu'au moteur, qui la rend mécanique (EM) ; les ordres arrivent sur le bloc Distribuer.
<svg viewBox="0 0 480 152">
<g fill="#0f6e56" opacity="0.12"><rect x="36" y="64" width="78" height="46" rx="6"/><rect x="132" y="64" width="78" height="46" rx="6"/><rect x="228" y="64" width="78" height="46" rx="6"/><rect x="324" y="64" width="78" height="46" rx="6"/></g>
<g fill="none" stroke="#0f172a" stroke-width="2"><rect x="36" y="64" width="78" height="46" rx="6"/><rect x="132" y="64" width="78" height="46" rx="6"/><rect x="228" y="64" width="78" height="46" rx="6"/><rect x="324" y="64" width="78" height="46" rx="6"/><path d="M4 87 H26"/><path d="M114 87 H122"/><path d="M210 87 H218"/><path d="M306 87 H314"/><path d="M402 87 H466"/><path d="M171 30 V56"/></g>
<g fill="#0f172a"><polygon points="36,87 26,82 26,92"/><polygon points="132,87 122,82 122,92"/><polygon points="228,87 218,82 218,92"/><polygon points="324,87 314,82 314,92"/><polygon points="476,87 466,82 466,92"/><polygon points="171,64 166,54 176,54"/></g>
<g font-size="10" font-weight="700" text-anchor="middle" fill="#0f172a"><text x="75" y="92">Alimenter</text><text x="171" y="92">Distribuer</text><text x="267" y="92">Convertir</text><text x="363" y="92">Transmettre</text></g>
<g font-size="9" fill="#0f6e56" text-anchor="middle"><text x="123" y="78">EE</text><text x="219" y="78">EE</text><text x="315" y="78">EM</text><text x="434" y="78">EM</text><text x="75" y="126">prise secteur</text><text x="171" y="126">carte de puissance</text><text x="267" y="126">moteurs</text><text x="363" y="126">accouplement,</text><text x="363" y="138">vis et noix</text></g>
<g font-size="9" fill="#0f172a"><text x="4" y="54">Source d'énergie</text><text x="476" y="54" text-anchor="end">Action réalisée</text><text x="171" y="22" text-anchor="middle">Ordres</text></g>
</svg>
:::

> ⚠️ Piège classique : **Convertir n'est pas Transmettre**. Convertir **change la nature** de l'énergie — l'électrique devient mécanique — et c'est le rôle du moteur. Transmettre **garde** cette énergie mécanique et l'achemine jusqu'à la pièce mobile : accouplement, vis, noix. Dans toute la chaîne, la nature de l'énergie ne change qu'**une seule fois**, au niveau de l'actionneur.

## 🔩 Le support d'étude : la micro-fraiseuse

La **C.F.A.O.** permet, à l'aide de logiciels spécifiques, de dessiner la pièce et d'optimiser les trajectoires de sa découpe. On peut ensuite lancer une **simulation** avant l'usinage, ou éditer un **prototype** avant de lancer la production. Les machines utilisées en C.F.A.O. sont principalement des **ordinateurs** et des **machines de fabrication**.

La micro-fraiseuse réunit quatre ensembles :

- un **ordinateur** — unité centrale et périphériques ;
- un **directeur de commande numérique**, ou **DCN** : la carte de commande ;
- un **logiciel de C.F.A.O.**, qui sert à créer le **fichier d'usinage** ;
- des **moteurs, chariots, bâti, boutons et capteurs**.

Ses mouvements : le **chariot transversal** et la **table** portant la pièce se déplacent en **translation** suivant les axes **x** et **y**. L'**outil**, lui, se déplace **verticalement** suivant l'axe **z** et **tourne autour de ce même axe**.

Deux origines à ne jamais confondre :

- **Om**, origine machine : la position de la machine **en butée** ;
- **Op**, origine pièce : elle est **définie par l'opérateur**.

> ⚠️ Avant toute manipulation : enclencher le **bouton d'arrêt d'urgence**, utiliser les **clés appropriées**, porter des **gants résistants aux coupures**. Une machine-outil ne pardonne rien.

## 🛠️ Le chariot transversal, de la prise secteur au mouvement

Le **chariot transversal** porte la table et la pièce, et se déplace en translation suivant **(oy)**. Suis l'énergie, bloc par bloc :

la **prise secteur** (Alimenter) → la **carte de puissance** (Distribuer) → le **moteur** (Convertir) → l'**accouplement**, la **vis de manœuvre** et la **noix** (Transmettre) → le chariot avance.

Chaque organe porte son nom au dessin d'ensemble. La **semelle** et le **bâti** portent tout l'ensemble et lui donnent sa rigidité. L'**accouplement**, ici, est un simple **manchon** : un manchon relie deux arbres bout à bout et leur impose la même rotation.

::: figure Le moteur tourne, la vis tourne, mais la noix — solidaire du chariot — ne peut pas tourner : elle est obligée d'avancer, et le chariot avec elle.
<svg viewBox="0 0 440 166">
<rect x="248" y="40" width="162" height="30" rx="4" fill="#bfdbfe" stroke="#0f172a" stroke-width="2"/>
<rect x="118" y="98" width="68" height="40" rx="4" fill="#fde68a" stroke="#0f172a" stroke-width="2"/>
<rect x="196" y="106" width="32" height="24" rx="3" fill="#0f6e56" opacity="0.18"/>
<g fill="none" stroke="#0f172a" stroke-width="2"><rect x="196" y="106" width="32" height="24" rx="3"/><circle cx="70" cy="118" r="17"/><path d="M118 118 H88"/><path d="M186 118 H196"/><rect x="302" y="70" width="44" height="66" rx="3"/><path d="M256 26 H402"/></g>
<path d="M228 118 H404" fill="none" stroke="#0f172a" stroke-width="3"/>
<g fill="none" stroke="#0f172a" stroke-width="1.5"><path d="M236 110 L243 126"/><path d="M250 110 L257 126"/><path d="M264 110 L271 126"/><path d="M278 110 L285 126"/><path d="M292 110 L299 126"/><path d="M306 110 L313 126"/><path d="M320 110 L327 126"/><path d="M334 110 L341 126"/><path d="M348 110 L355 126"/><path d="M362 110 L369 126"/><path d="M376 110 L383 126"/></g>
<path d="M250 100 A 16 16 0 0 1 274 100" fill="none" stroke="#0f6e56" stroke-width="2"/>
<g fill="#0f172a"><circle cx="70" cy="101" r="4"/><polygon points="250,26 260,21 260,31"/><polygon points="408,26 398,21 398,31"/></g>
<polygon points="278,104 268,101 274,93" fill="#0f6e56"/>
<g font-size="11" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="329" y="60">chariot</text><text x="152" y="122">moteur</text><text x="324" y="92">noix</text><text x="416" y="30">y</text></g>
<g font-size="10" text-anchor="middle" fill="#0f172a"><text x="70" y="152">volant</text><text x="212" y="152">accouplement</text><text x="340" y="152">vis de manœuvre</text></g>
</svg>
:::

Deux détails de conception valent d'être vus :

- le moteur possède **deux sorties d'arbre** : l'une entraîne la vis par l'accouplement — c'est le **mode automatique** ; l'autre reçoit le **volant de manœuvre**, que l'on tourne à la main — c'est le **mode manuel** ;
- la vis tourne, la **noix** ne le peut pas : la **rotation** devient une **translation**. Le chariot est en outre **guidé en translation** par un **guidage prismatique**, doté d'un dispositif de **rattrapage de jeu**.

## 🌳 Le diagramme F.A.S.T.

La méthode **F.A.S.T.** aide à penser le problème de façon objective et permet de **déterminer la portée du projet en illustrant les relations logiques entre les fonctions**. Elle pose trois questions clés :

- **Comment** accomplit-on cette fonction ?
- **Pourquoi** réalise-t-on cette fonction ?
- **Quand** on fait cette fonction, quelles autres fonctions doivent être faites ?

Le diagramme se lit en **trois colonnes** : **fonction de service** → **fonctions techniques** → **solutions technologiques**. On descend vers la droite en répondant « **Comment ?** » ; on remonte vers la gauche en répondant « **Pourquoi ?** ». Deux opérateurs relient les branches : **ET**, quand toutes les solutions reliées sont nécessaires **ensemble** ; **OU**, quand les branches sont des solutions **alternatives**.

::: figure Le diagramme F.A.S.T. type : les solutions 2 et 3 sont reliées par ET, il faut les deux ; la bifurcation marquée OU sépare deux branches entre lesquelles on choisit.
<svg viewBox="0 0 470 232">
<g font-size="9" font-weight="700" text-anchor="middle" fill="#0f172a"><text x="62" y="18">Fonction de service</text><text x="223" y="18">Fonctions techniques</text><text x="391" y="18">Solutions technologiques</text></g>
<rect x="12" y="100" width="100" height="40" rx="4" fill="#0f6e56" opacity="0.16"/>
<g fill="#fbcfe8"><rect x="168" y="48" width="110" height="38" rx="4"/><rect x="168" y="104" width="110" height="38" rx="4"/><rect x="168" y="176" width="110" height="38" rx="4"/></g>
<g fill="#bfdbfe"><rect x="330" y="51" width="122" height="32" rx="4"/><rect x="330" y="96" width="122" height="32" rx="4"/><rect x="330" y="136" width="122" height="32" rx="4"/><rect x="330" y="179" width="122" height="32" rx="4"/></g>
<g fill="none" stroke="#0f172a" stroke-width="2"><rect x="12" y="100" width="100" height="40" rx="4"/><rect x="168" y="48" width="110" height="38" rx="4"/><rect x="168" y="104" width="110" height="38" rx="4"/><rect x="168" y="176" width="110" height="38" rx="4"/><rect x="330" y="51" width="122" height="32" rx="4"/><rect x="330" y="96" width="122" height="32" rx="4"/><rect x="330" y="136" width="122" height="32" rx="4"/><rect x="330" y="179" width="122" height="32" rx="4"/></g>
<g fill="none" stroke="#0f172a" stroke-width="1.8"><path d="M112 120 H140"/><path d="M140 67 V195"/><path d="M140 67 H158"/><path d="M140 123 H158"/><path d="M140 195 H158"/><path d="M278 67 H320"/><path d="M278 195 H320"/><path d="M278 123 H296"/><path d="M296 112 V152"/><path d="M296 112 H320"/><path d="M296 152 H320"/></g>
<g fill="#0f172a"><polygon points="168,67 158,62 158,72"/><polygon points="168,123 158,118 158,128"/><polygon points="168,195 158,190 158,200"/><polygon points="330,67 320,62 320,72"/><polygon points="330,112 320,107 320,117"/><polygon points="330,152 320,147 320,157"/><polygon points="330,195 320,190 320,200"/></g>
<circle cx="140" cy="88" r="12" fill="#ffffff" stroke="#0f172a" stroke-width="1.5" stroke-dasharray="3 3"/>
<circle cx="296" cy="132" r="12" fill="#ffffff" stroke="#0f172a" stroke-width="1.5" stroke-dasharray="3 3"/>
<g font-size="9" font-weight="700" text-anchor="middle" fill="#0f172a"><text x="140" y="92">OU</text><text x="296" y="136">ET</text></g>
<g font-size="12" font-weight="700" text-anchor="middle" fill="#0f172a"><text x="62" y="125">FS</text><text x="223" y="72">FT 1</text><text x="223" y="128">FT 2</text><text x="223" y="200">FT 3</text><text x="391" y="72">ST 1</text><text x="391" y="117">ST 2</text><text x="391" y="157">ST 3</text><text x="391" y="200">ST 4</text></g>
</svg>
:::

Sur la micro-fraiseuse, la fonction de service **FS1 « Usiner une pièce »** se décompose en quatre fonctions techniques de premier niveau :

| Fonction technique | Ce qu'elle exige                                              |
| ------------------ | ------------------------------------------------------------- |
| **FT1**            | Positionner et maintenir la pièce                             |
| **FT2**            | Positionner et maintenir l'outil                              |
| **FT3**            | Animer l'outil d'un mouvement de rotation autour de son axe z |
| **FT4**            | Assurer les déplacements relatifs de l'outil et de la pièce   |

Chaque fonction technique appelle ensuite son processeur ou son composant. La **pince porte-outil** maintient l'outil (FT2), et le **moteur de broche** le fait tourner (FT3). Le **directeur de commande numérique**, lui, pilote les déplacements (FT4).

Et l'on descend encore d'un cran sur la branche du déplacement du chariot transversal suivant (oy) :

- **déplacer manuellement** — utiliser un moteur à double sorties d'arbre, et tourner l'arbre moteur à la main → le **volant de manœuvre** ;
- **déplacer automatiquement** — gérer les ordres de commande → le **DCN** ; distribuer l'énergie électrique → la **carte de puissance** ; convertir l'énergie → le **moteur** ; transmettre la rotation de l'arbre moteur à la vis → l'**accouplement** ; transformer la rotation en translation → la **vis et sa noix** ; guider en translation et rattraper le jeu → le **guidage prismatique** et son réglage.

Cette branche montre les deux opérateurs à l'œuvre. **Déplacer manuellement** et **déplacer automatiquement** sont deux solutions **alternatives** : c'est un **OU**. À l'intérieur du mode automatique en revanche, gérer les ordres, distribuer, convertir, transmettre, transformer et guider sont toutes nécessaires **ensemble** : c'est un **ET**.

> 🏆 Première porte franchie, héros. Tu sais maintenant ouvrir n'importe quelle machine automatisée : deux chaînes, sept fonctions, et un arbre F.A.S.T. qui descend jusqu'à la vis. Garde cette méthode sous la main — au chapitre suivant, c'est le **dessin d'ensemble** lui-même qu'il faudra faire parler.
