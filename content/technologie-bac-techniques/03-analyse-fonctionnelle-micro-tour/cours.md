# ⚙️ Le micro-tour et la loi des deux chaînes

> 💡 «Trois machines, trois carrosseries — une seule charpente. Quand tu auras vu la même architecture sous la micro-fraiseuse, l'imprimante 3D et le micro-tour, tu sauras lire n'importe quel système automatisé, même un que tu n'as jamais rencontré.»

Tu as déjà démonté deux systèmes par la pensée. Voici le troisième — et cette fois on ne s'arrête pas à la machine : on en tire le **modèle général**. C'est la dernière marche du thème, celle où les trois activités se referment en une seule loi.

## 🏭 Le support : un micro-tour à commande numérique

Le **micro-tour** est une **machine-outil à commande numérique** : un ordinateur, muni d'un logiciel qui assure la **lecture et le traitement du G-code**, la pilote. Le **G-code** est le langage qui décrit les opérations à effectuer ; le fichier d'usinage lui-même est produit en amont par un **logiciel de F.A.O.** (Fabrication Assistée par Ordinateur).

La machine et sa commande se composent essentiellement d'un **ordinateur** et de ses périphériques, du **logiciel de F.A.O.**, d'**actionneurs** (les moteurs), de **capteurs**, et d'**organes de sécurité** — le **carter** (capot de sécurité) et le **bouton d'arrêt d'urgence**.

Côté mécanique : la pièce à usiner est placée dans le **mandrin (8)** et serrée par ses **mors** ; un moteur met en rotation le mandrin fixé sur la **broche (11)**. L'outil coupant est positionné et serré par des vis dans la **tourelle porte-outil (5)**, elle-même montée sur le **chariot porte-outil (7)** — que le texte de la machine appelle aussi le **chariot transversal (29)**. Le **traînard (31)** se déplace suivant l'**axe Z** (le long de la pièce) et le chariot porte-outil suivant l'**axe X** (**perpendiculairement** à l'axe de la pièce, pour l'en approcher ou l'en éloigner). La **poupée mobile (1)** permet enfin les opérations de **pointage, centrage, perçage et alésage en bout de pièce**. La commande manuelle des chariots reste possible par les **volants (40)**, et le **tambour gradué (2)** comme l'**indicateur de position (33)** affichent la position atteinte.

::: figure Vue de dessus du micro-tour : la pièce tourne dans le mandrin, l'outil l'attaque par le côté ; il longe la pièce suivant Z et s'approche de son axe suivant X
<svg viewBox="0 0 400 215">
<rect x="24" y="170" width="352" height="26" fill="#0f6e56" opacity="0.12"/>
<rect x="24" y="170" width="352" height="26" fill="none" stroke="#0f172a" stroke-width="2"/>
<g stroke="#0f172a" stroke-width="1.5"><path d="M52 196 L43 206 M76 196 L67 206 M100 196 L91 206 M124 196 L115 206 M148 196 L139 206 M172 196 L163 206 M196 196 L187 206 M220 196 L211 206 M244 196 L235 206 M268 196 L259 206 M292 196 L283 206 M316 196 L307 206 M340 196 L331 206 M364 196 L355 206"/></g>
<rect x="32" y="76" width="72" height="94" fill="#0f6e56" opacity="0.12"/>
<rect x="32" y="76" width="72" height="94" fill="none" stroke="#0f172a" stroke-width="2"/>
<rect x="104" y="78" width="26" height="52" fill="#0f6e56" opacity="0.20"/>
<rect x="104" y="78" width="26" height="52" fill="none" stroke="#0f172a" stroke-width="2"/>
<rect x="130" y="90" width="112" height="28" fill="#fde68a"/>
<rect x="130" y="90" width="112" height="28" fill="none" stroke="#0f172a" stroke-width="2"/>
<rect x="286" y="76" width="66" height="94" fill="#0f6e56" opacity="0.12"/>
<rect x="286" y="76" width="66" height="94" fill="none" stroke="#0f172a" stroke-width="2"/>
<rect x="262" y="98" width="24" height="12" fill="none" stroke="#0f172a" stroke-width="1.5"/>
<path d="M262 98 L246 104 L262 110 Z" fill="#0f172a"/>
<rect x="168" y="152" width="80" height="22" fill="#0f6e56" opacity="0.12"/>
<rect x="168" y="152" width="80" height="22" fill="none" stroke="#0f172a" stroke-width="2"/>
<rect x="184" y="132" width="48" height="20" fill="#0f6e56" opacity="0.12"/>
<rect x="184" y="132" width="48" height="20" fill="none" stroke="#0f172a" stroke-width="2"/>
<path d="M202 132 L208 118 L214 132 Z" fill="#0f172a"/>
<path d="M238 141 L216 128" fill="none" stroke="#94a3b8" stroke-width="1.2"/>
<path d="M356 32 H384" fill="none" stroke="#0f172a" stroke-width="2"/>
<path d="M376 27 L386 32 L376 37 Z" fill="#0f172a"/>
<path d="M356 32 V56" fill="none" stroke="#0f172a" stroke-width="2"/>
<path d="M351 48 L356 58 L361 48 Z" fill="#0f172a"/>
<g paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" fill="#0f172a" text-anchor="middle">
<text x="68" y="116" font-size="10" font-weight="700">Broche</text>
<text x="68" y="132" font-size="10" font-weight="700">(11)</text>
<text x="117" y="70" font-size="9">Mandrin (8)</text>
<text x="186" y="109" font-size="11" font-weight="700">Pièce</text>
<text x="319" y="118" font-size="10" font-weight="700">Poupée</text>
<text x="319" y="134" font-size="9">mobile (1)</text>
<text x="208" y="168" font-size="9">Traînard (31)</text>
<text x="240" y="146" font-size="8" text-anchor="start">Outil (27)</text>
<text x="40" y="190" font-size="9" text-anchor="start">Banc (22)</text>
<text x="392" y="26" font-size="12" font-weight="700">Z</text>
<text x="346" y="58" font-size="12" font-weight="700">X</text>
</g>
</svg>
:::

Deux repères d'usinage complètent la description, et il ne faut jamais les confondre : l'**origine machine Om** est la **position de la machine en butée** — fixée par construction ; l'**origine pièce Op** est **définie par l'opérateur** sur le brut qu'il vient de monter.

> ⚠️ Om est une propriété de la machine, Op une décision de l'opérateur. Changer de pièce change Op, jamais Om.

## 🧠 La chaîne d'information : acquérir, traiter, communiquer

Un **système automatisé** est composé de plusieurs éléments qui exécutent un ensemble de **tâches programmées** sans que l'intervention de l'homme soit nécessaire. Pour le décrire, on le coupe en **deux chaînes** de blocs fonctionnels.

La **chaîne d'information** est la partie du système qui **capte l'information et la traite**. Elle compte trois blocs :

| Bloc             | Ce qu'il fait                                                                                      |
| ---------------- | -------------------------------------------------------------------------------------------------- |
| **Acquérir**     | prélever des informations à l'aide de **capteurs**                                                 |
| **Traiter**      | la **partie commande** : un automate ou un **microcontrôleur**                                     |
| **Communiquer**  | assurer l'**interface** entre l'utilisateur, les autres systèmes, l'environnement et la partie commande |

Elle reçoit en entrée la **consigne de l'utilisateur** et les **informations extérieures au système** ; elle produit en sortie l'**information pour l'utilisateur** et les **ordres pour la chaîne d'énergie**.

## ⚡ La chaîne d'énergie : alimenter, distribuer, convertir, transmettre

La **chaîne d'énergie** est l'ensemble des procédés qui vont **réaliser l'action**. Elle compte quatre blocs :

| Bloc             | Ce qu'il fait                                                                                         |
| ---------------- | ------------------------------------------------------------------------------------------------------- |
| **Alimenter**    | mettre en forme l'**énergie externe** en une énergie compatible avec l'action à créer                  |
| **Distribuer**   | distribuer l'énergie à l'actionneur — par un **distributeur**, un **contacteur** ou une **carte de puissance** |
| **Convertir**    | l'organe de conversion, appelé **actionneur** : un vérin, un moteur…                                   |
| **Transmettre**  | acheminer et adapter l'énergie mécanique par les **organes de transmission de mouvement et d'effort**  |

Elle reçoit une **énergie d'entrée** à gauche, les **ordres** par le haut, et rend à droite la **réalisation de l'action**.

> ⚠️ La synthèse officielle interrompt son énumération d'organes de transmission au milieu d'une phrase (« engrenages, courroies, ») : la liste imprimée est inachevée, ne la prends pas pour un inventaire complet. Retiens la **fonction**, pas la liste — engrenage, poulie-courroie, chaîne, accouplement, vis-écrou, réducteur : tout organe qui transporte ou adapte l'énergie mécanique remplit **Transmettre**.

> 💡 Ne t'étonne pas si le diagramme du micro-tour et celui de la synthèse générale ne se ressemblent pas tout à fait : le premier écrit son bloc d'entrée **Alimenter/Stocker** — la variante retenue quand le système **stocke** de l'énergie — et il ajoute après Transmettre un **cinquième bloc**, laissé vide à compléter, d'où sort la flèche **Pertes**. La synthèse, elle, s'en tient aux quatre blocs et à la sortie « réalisation de l'action ». Quatre blocs ou cinq, ce sont les mêmes fonctions dans le même ordre.

::: figure Les deux chaînes de tout système automatisé : celle du haut décide, celle du bas agit ; le seul lien qui descend de l'une à l'autre est la flèche « Ordres », et elle entre dans le bloc Distribuer
<svg viewBox="0 0 480 300">
<text x="242" y="26" font-size="13" font-weight="700" fill="#0f172a" text-anchor="middle">Chaîne d'information</text>
<g fill="#0f6e56" opacity="0.12"><rect x="86" y="54" width="92" height="46" rx="6"/><rect x="196" y="54" width="92" height="46" rx="6"/><rect x="306" y="54" width="92" height="46" rx="6"/></g>
<g fill="none" stroke="#0f172a" stroke-width="2"><rect x="86" y="54" width="92" height="46" rx="6"/><rect x="196" y="54" width="92" height="46" rx="6"/><rect x="306" y="54" width="92" height="46" rx="6"/></g>
<g fill="none" stroke="#0f172a" stroke-width="2"><path d="M26 77 H78"/><path d="M178 77 H188"/><path d="M288 77 H298"/><path d="M398 77 H448"/></g>
<g fill="#0f172a"><path d="M78 72 L86 77 L78 82 Z"/><path d="M188 72 L196 77 L188 82 Z"/><path d="M298 72 L306 77 L298 82 Z"/><path d="M448 72 L456 77 L448 82 Z"/></g>
<g fill="#0f6e56" opacity="0.12"><rect x="44" y="204" width="88" height="46" rx="6"/><rect x="148" y="204" width="88" height="46" rx="6"/><rect x="252" y="204" width="88" height="46" rx="6"/><rect x="356" y="204" width="88" height="46" rx="6"/></g>
<g fill="none" stroke="#0f172a" stroke-width="2"><rect x="44" y="204" width="88" height="46" rx="6"/><rect x="148" y="204" width="88" height="46" rx="6"/><rect x="252" y="204" width="88" height="46" rx="6"/><rect x="356" y="204" width="88" height="46" rx="6"/></g>
<g fill="none" stroke="#0f172a" stroke-width="2"><path d="M6 227 H36"/><path d="M132 227 H140"/><path d="M236 227 H244"/><path d="M340 227 H348"/><path d="M444 227 H466"/></g>
<g fill="#0f172a"><path d="M36 222 L44 227 L36 232 Z"/><path d="M140 222 L148 227 L140 232 Z"/><path d="M244 222 L252 227 L244 232 Z"/><path d="M348 222 L356 227 L348 232 Z"/><path d="M466 222 L474 227 L466 232 Z"/></g>
<path d="M242 100 V160 H192 V196" fill="none" stroke="#0f6e56" stroke-width="2.5"/>
<path d="M187 196 L192 204 L197 196 Z" fill="#0f6e56"/>
<text x="244" y="278" font-size="13" font-weight="700" fill="#0f172a" text-anchor="middle">Chaîne d'énergie</text>
<g font-size="12" font-weight="700" fill="#0f172a" text-anchor="middle">
<text x="132" y="82">Acquérir</text><text x="242" y="82">Traiter</text><text x="352" y="82">Communiquer</text>
<text x="88" y="232">Alimenter</text><text x="192" y="232">Distribuer</text><text x="296" y="232">Convertir</text><text x="400" y="232">Transmettre</text>
</g>
<g font-size="9" fill="#0f172a" text-anchor="middle">
<text x="56" y="68">Consignes</text><text x="427" y="68">Infos</text><text x="21" y="218">Énergie</text><text x="459" y="218">Action</text>
</g>
<text x="250" y="146" font-size="11" font-weight="700" fill="#0f6e56" text-anchor="start">Ordres</text>
</svg>
:::

## 🔗 Les deux chaînes du micro-tour, bloc par bloc

Applique le modèle à la machine. Côté **information** : les **interrupteurs et boutons poussoirs** acquièrent, le **microcontrôleur** traite, l'**écran** communique. L'**encodeur (16)** est lui aussi un capteur : quelle que soit la grandeur qu'il mesure, il relève d'**Acquérir**. Cette chaîne reçoit le programme **G-code**, les consignes de l'utilisateur et les informations de l'environnement ; en retour, le **fonctionnement de la machine** lui renvoie ses propres informations.

Côté **énergie** : l'**unité d'alimentation** alimente, la **carte de puissance** distribue, les **moteurs pas à pas** des axes X et Z et le **moteur électrique** de la broche convertissent, les **éléments de transmission** transmettent. La machine compte donc **trois actionneurs** en tout.

> 🗡️ Suis la **nature de l'énergie** le long de la chaîne : elle reste **électrique** tant qu'elle n'a pas atteint l'actionneur, elle devient **mécanique** dès qu'elle en sort. Le bloc Convertir est la frontière — c'est même sa définition.

Aucune conversion n'est parfaite : à chaque étage, une part de l'énergie s'échappe en échauffement et en frottements. C'est la sortie **Pertes**.

::: figure La même charpente, remplie pour le micro-tour : sous chaque fonction, le composant qui la réalise ; sur les flèches, la nature de l'énergie — électrique jusqu'aux moteurs, mécanique après eux
<svg viewBox="0 0 480 320">
<text x="242" y="24" font-size="12" font-weight="700" fill="#0f172a" text-anchor="middle">Chaîne d'information</text>
<g fill="#0f6e56" opacity="0.12"><rect x="86" y="48" width="92" height="56" rx="6"/><rect x="196" y="48" width="92" height="56" rx="6"/><rect x="306" y="48" width="92" height="56" rx="6"/></g>
<g fill="none" stroke="#0f172a" stroke-width="2"><rect x="86" y="48" width="92" height="56" rx="6"/><rect x="196" y="48" width="92" height="56" rx="6"/><rect x="306" y="48" width="92" height="56" rx="6"/></g>
<g fill="none" stroke="#0f172a" stroke-width="2"><path d="M26 76 H78"/><path d="M178 76 H188"/><path d="M288 76 H298"/><path d="M398 76 H448"/></g>
<g fill="#0f172a"><path d="M78 71 L86 76 L78 81 Z"/><path d="M188 71 L196 76 L188 81 Z"/><path d="M298 71 L306 76 L298 81 Z"/><path d="M448 71 L456 76 L448 81 Z"/></g>
<text x="244" y="200" font-size="12" font-weight="700" fill="#0f172a" text-anchor="middle">Chaîne d'énergie</text>
<g fill="#0f6e56" opacity="0.12"><rect x="44" y="214" width="88" height="56" rx="6"/><rect x="148" y="214" width="88" height="56" rx="6"/><rect x="252" y="214" width="88" height="56" rx="6"/><rect x="356" y="214" width="88" height="56" rx="6"/></g>
<g fill="none" stroke="#0f172a" stroke-width="2"><rect x="44" y="214" width="88" height="56" rx="6"/><rect x="148" y="214" width="88" height="56" rx="6"/><rect x="252" y="214" width="88" height="56" rx="6"/><rect x="356" y="214" width="88" height="56" rx="6"/></g>
<g fill="none" stroke="#0f172a" stroke-width="2"><path d="M6 242 H36"/><path d="M132 242 H140"/><path d="M236 242 H244"/><path d="M340 242 H348"/><path d="M444 242 H466"/></g>
<g fill="#0f172a"><path d="M36 237 L44 242 L36 247 Z"/><path d="M140 237 L148 242 L140 247 Z"/><path d="M244 237 L252 242 L244 247 Z"/><path d="M348 237 L356 242 L348 247 Z"/><path d="M466 237 L474 242 L466 247 Z"/></g>
<path d="M242 104 V160 H192 V206" fill="none" stroke="#0f6e56" stroke-width="2.5"/>
<path d="M187 206 L192 214 L197 206 Z" fill="#0f6e56"/>
<path d="M400 270 V286" fill="none" stroke="#94a3b8" stroke-width="2"/>
<path d="M395 286 L400 294 L405 286 Z" fill="#94a3b8"/>
<g font-size="12" font-weight="700" fill="#0f172a" text-anchor="middle">
<text x="132" y="72">Acquérir</text><text x="242" y="72">Traiter</text><text x="352" y="72">Communiquer</text>
</g>
<g font-size="11" font-weight="700" fill="#0f172a" text-anchor="middle">
<text x="88" y="238">Alimenter</text><text x="192" y="238">Distribuer</text><text x="296" y="238">Convertir</text><text x="400" y="238">Transmettre</text>
</g>
<g font-size="8" fill="#0f172a" text-anchor="middle">
<text x="132" y="90">Boutons poussoirs</text><text x="242" y="90">Microcontrôleur</text><text x="352" y="90">Écran</text>
<text x="88" y="257">Unité d'alimentation</text><text x="192" y="257">Carte de puissance</text><text x="296" y="257">Moteurs</text><text x="400" y="257">Poulies, vis, écrou</text>
<text x="56" y="66">G-code</text><text x="427" y="66">Affichage</text><text x="21" y="233">Secteur</text>
</g>
<g font-size="10" font-weight="700" fill="#0f6e56" text-anchor="middle">
<text x="140" y="232">EE</text><text x="244" y="232">EE</text><text x="348" y="232">EM</text><text x="459" y="232">EM</text>
</g>
<text x="250" y="150" font-size="10" font-weight="700" fill="#0f6e56" text-anchor="start">Ordres</text>
<text x="400" y="308" font-size="9" fill="#94a3b8" text-anchor="middle">Pertes</text>
<text x="14" y="308" font-size="8" fill="#0f172a" text-anchor="start">EE : énergie électrique — EM : énergie mécanique</text>
</svg>
:::

## 🌳 Le F.A.S.T. : descendre de la fonction jusqu'au composant

Les chaînes disent **où** l'énergie et l'information passent. Le **F.A.S.T.** dit **par quoi**. C'est la méthode de l'**analyse fonctionnelle interne** : le besoin étant déjà exprimé dans le cahier des charges fonctionnel, elle consiste à rechercher les **fonctions techniques**, les **solutions constructives** et les **composants** qui satisfont chaque **fonction de service**. Ce besoin, c'est l'**analyse fonctionnelle externe** qui l'a exprimé et qui a rédigé ce cahier des charges : elle précède l'analyse interne, elle n'est pas au programme de cette séquence, et on part de son résultat.

Un diagramme F.A.S.T. répond à trois questions clés :

- **Comment accomplit-on cette fonction ?** — on avance vers la droite ;
- **Pourquoi réalise-t-on cette fonction ?** — on remonte vers la gauche ;
- **Quand on fait cette fonction, quelles autres fonctions doivent être faites ?** — on lit verticalement.

Il se dessine en trois colonnes : **fonction de service**, puis **fonctions techniques**, puis **solutions technologiques**. Deux opérateurs relient les branches : **ET** lorsque plusieurs solutions sont nécessaires **ensemble** pour une même fonction, **OU** lorsque les branches sont **alternatives**.

Sur le micro-tour, la fonction **FT5121 « Interposer une liaison hélicoïdale »** se lit avec un **ET** : il faut **assurer la rotation de la vis (26)** ET **assurer la translation de l'écrou (25)** ; retire l'une des deux et le traînard n'avance plus.

::: figure Le F.A.S.T. se lit dans les deux sens : vers la droite il répond à « Comment ? », vers la gauche à « Pourquoi ? » ; l'opérateur ET relie deux solutions toutes deux nécessaires, l'opérateur OU sépare des branches alternatives
<svg viewBox="0 0 460 315">
<g font-size="10" font-weight="700" fill="#0f172a" text-anchor="middle">
<text x="70" y="26">Fonction de service</text><text x="230" y="26">Fonctions techniques</text><text x="390" y="26">Solutions technologiques</text>
</g>
<g fill="#0f6e56" opacity="0.12"><rect x="20" y="110" width="100" height="44" rx="5"/><rect x="180" y="54" width="100" height="38" rx="5"/><rect x="180" y="113" width="100" height="38" rx="5"/><rect x="180" y="196" width="100" height="38" rx="5"/><rect x="340" y="54" width="104" height="38" rx="5"/><rect x="340" y="102" width="104" height="36" rx="5"/><rect x="340" y="148" width="104" height="36" rx="5"/><rect x="340" y="196" width="104" height="38" rx="5"/></g>
<g fill="none" stroke="#0f172a" stroke-width="2"><rect x="20" y="110" width="100" height="44" rx="5"/><rect x="180" y="54" width="100" height="38" rx="5"/><rect x="180" y="113" width="100" height="38" rx="5"/><rect x="180" y="196" width="100" height="38" rx="5"/><rect x="340" y="54" width="104" height="38" rx="5"/><rect x="340" y="102" width="104" height="36" rx="5"/><rect x="340" y="148" width="104" height="36" rx="5"/><rect x="340" y="196" width="104" height="38" rx="5"/></g>
<g fill="none" stroke="#0f172a" stroke-width="1.8"><path d="M120 132 H150"/><path d="M150 73 V215"/><path d="M150 73 H172"/><path d="M150 132 H172"/><path d="M150 215 H172"/><path d="M280 73 H332"/><path d="M280 132 H310"/><path d="M310 120 V166"/><path d="M310 120 H332"/><path d="M310 166 H332"/><path d="M280 215 H332"/></g>
<g fill="#0f172a"><path d="M172 68 L180 73 L172 78 Z"/><path d="M172 127 L180 132 L172 137 Z"/><path d="M172 210 L180 215 L172 220 Z"/><path d="M332 68 L340 73 L332 78 Z"/><path d="M332 115 L340 120 L332 125 Z"/><path d="M332 161 L340 166 L332 171 Z"/><path d="M332 210 L340 215 L332 220 Z"/></g>
<rect x="139" y="87" width="22" height="16" rx="3" fill="#ffffff" stroke="#0f6e56" stroke-width="1.5"/>
<text x="150" y="99" font-size="9" font-weight="700" fill="#0f6e56" text-anchor="middle">OU</text>
<rect x="299" y="135" width="22" height="16" rx="3" fill="#ffffff" stroke="#0f6e56" stroke-width="1.5"/>
<text x="310" y="147" font-size="9" font-weight="700" fill="#0f6e56" text-anchor="middle">ET</text>
<g font-size="10" fill="#0f172a" text-anchor="middle">
<text x="70" y="128">Fonction</text><text x="70" y="143">de service</text>
<text x="230" y="70">Fonction</text><text x="230" y="85">technique 1</text>
<text x="230" y="129">Fonction</text><text x="230" y="144">technique 2</text>
<text x="230" y="212">Fonction</text><text x="230" y="227">technique 3</text>
<text x="392" y="77">Solution 1</text><text x="392" y="124">Solution 2</text><text x="392" y="170">Solution 3</text><text x="392" y="219">Solution 4</text>
</g>
<path d="M60 266 H392" fill="none" stroke="#0f6e56" stroke-width="2"/>
<path d="M392 261 L400 266 L392 271 Z" fill="#0f6e56"/>
<path d="M400 292 H68" fill="none" stroke="#0f6e56" stroke-width="2"/>
<path d="M68 287 L60 292 L68 297 Z" fill="#0f6e56"/>
<g font-size="11" font-weight="700" fill="#0f6e56" text-anchor="middle">
<text x="230" y="259">Comment ?</text><text x="230" y="308">Pourquoi ?</text>
</g>
</svg>
:::

Sur le micro-tour, la fonction principale **FP1 « Permettre à l'utilisateur de réaliser des pièces à partir d'un brut »** se décompose ainsi :

| Fonction technique                          | Ce qui la satisfait sur la machine                       |
| ------------------------------------------- | ---------------------------------------------------------- |
| FT1 — Fixer la pièce                        | le **mandrin (8)** et ses **mors**                        |
| FT2 — Fixer l'outil                         | la **tourelle porte-outil (5)** et ses **vis**            |
| FT3 — Alimenter la machine                  | l'**unité d'alimentation**                                |
| FT4 — Commander la machine                  | l'**ordinateur** et le **microcontrôleur**                |
| FT5 — Déplacer l'outil selon les axes X et Z | les chariots et leurs **moteurs pas à pas (38)**          |
| FT6 — Animer la pièce d'un mouvement de rotation | la **broche (11)** entraînée par le **moteur électrique (21)** |
| FT7 — Sécuriser la machine                  | le **carter** et le **bouton d'arrêt d'urgence**          |

## 🔩 Descendre jusqu'à la vis : la chaîne de l'axe Z

Prends FT5 et descends d'un cran : **FT51** déplace le **traînard (31)** suivant **Z**, **FT52** déplace le **chariot porte-outil (7)** suivant **X**. Descends encore sur FT51 : il faut **convertir l'énergie** (le moteur pas à pas), **transformer la rotation de l'arbre moteur en translation du traînard**, et — c'est **FT513** — **assurer le guidage en translation du traînard (31) suivant l'axe Z**.

Transformer une rotation en translation, c'est **interposer une liaison hélicoïdale** — la fonction **FT5121** — réalisée par le couple **vis mère (26) / écrou (25)**. Il faut alors deux choses : **assurer la rotation de la vis**, c'est-à-dire la lier à l'arbre moteur par l'**accouplement (37)** puis la **guider en rotation** (**FT512112**) dans son **palier (45)** équipé de **butées à billes (44)** ; et **assurer la translation de l'écrou**, en le liant au traînard.

Quatre liaisons mécaniques suffisent à tout décrire, et il faut savoir les distinguer :

| Liaison           | Ce qu'elle autorise                                        | Où sur l'axe Z                              |
| ----------------- | ------------------------------------------------------------ | --------------------------------------------- |
| **Encastrement**  | rien — aucun mouvement relatif                             | l'écrou (25) sur le traînard (31)            |
| **Pivot**         | la rotation seule autour d'un axe                          | la vis (26) dans son palier (45)             |
| **Glissière**     | la translation seule le long d'une direction               | le traînard (31) sur le banc (22)            |
| **Hélicoïdale**   | une rotation **couplée** à une translation                 | la vis (26) et l'écrou (25)                  |

::: figure Les quatre liaisons de l'axe Z : le palier laisse la vis tourner sans reculer (pivot), la vis et l'écrou couplent la rotation à l'avance (hélicoïdale), l'écrou est encastré dans le traînard qu'il entraîne, et le banc impose la direction (glissière)
<svg viewBox="0 0 420 240">
<path d="M40 192 H392" fill="none" stroke="#0f172a" stroke-width="2"/>
<g stroke="#0f172a" stroke-width="1.3"><path d="M52 192 L43 202 M76 192 L67 202 M100 192 L91 202 M124 192 L115 202 M148 192 L139 202 M172 192 L163 202 M196 192 L187 202 M220 192 L211 202 M244 192 L235 202 M268 192 L259 202 M292 192 L283 202 M316 192 L307 202 M340 192 L331 202 M364 192 L355 202 M388 192 L379 202"/></g>
<rect x="120" y="180" width="200" height="12" fill="#0f6e56" opacity="0.12"/>
<rect x="120" y="180" width="200" height="12" fill="none" stroke="#0f172a" stroke-width="1.5"/>
<rect x="165" y="58" width="90" height="122" fill="#0f6e56" opacity="0.12"/>
<rect x="165" y="58" width="90" height="122" fill="none" stroke="#0f172a" stroke-width="2"/>
<rect x="316" y="96" width="76" height="48" fill="#0f6e56" opacity="0.12"/>
<rect x="316" y="96" width="76" height="48" fill="none" stroke="#0f172a" stroke-width="2"/>
<rect x="344" y="144" width="20" height="48" fill="#0f6e56" opacity="0.12"/>
<rect x="344" y="144" width="20" height="48" fill="none" stroke="#0f172a" stroke-width="1.5"/>
<rect x="292" y="110" width="10" height="20" fill="#ffffff" stroke="#0f172a" stroke-width="1.5"/>
<rect x="306" y="110" width="10" height="20" fill="#ffffff" stroke="#0f172a" stroke-width="1.5"/>
<path d="M96 120 H292" fill="none" stroke="#0f172a" stroke-width="3"/>
<g stroke="#0f6e56" stroke-width="2"><path d="M186 112 V128 M196 112 V128 M206 112 V128 M216 112 V128 M226 112 V128 M236 112 V128"/></g>
<path d="M88 128 L74 192 L102 192 Z" fill="#0f6e56" opacity="0.12"/>
<path d="M88 128 L74 192 L102 192 Z" fill="none" stroke="#0f172a" stroke-width="1.5"/>
<circle cx="88" cy="120" r="8" fill="#ffffff" stroke="#0f172a" stroke-width="2"/>
<path d="M64 126 L78 122" fill="none" stroke="#94a3b8" stroke-width="1.2"/>
<path d="M288 176 V182" fill="none" stroke="#94a3b8" stroke-width="1.2"/>
<g paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" text-anchor="middle">
<text x="210" y="80" font-size="11" font-weight="700" fill="#0f172a">Traînard (31)</text>
<text x="210" y="152" font-size="10" fill="#0f172a">Écrou (25)</text>
<text x="210" y="166" font-size="9" font-weight="700" fill="#0f6e56">encastrement</text>
<text x="128" y="142" font-size="9" fill="#0f172a">Vis mère (26)</text>
<text x="88" y="106" font-size="10" fill="#0f172a">(45)</text>
<text x="304" y="102" font-size="9" fill="#0f172a">(37)</text>
<text x="354" y="116" font-size="11" font-weight="700" fill="#0f172a">Moteur</text>
<text x="354" y="133" font-size="8" fill="#0f172a">pas à pas (38)</text>
<text x="56" y="186" font-size="9" fill="#0f172a">Bâti</text>
<text x="50" y="128" font-size="9" font-weight="700" fill="#0f6e56">pivot</text>
<text x="210" y="102" font-size="9" font-weight="700" fill="#0f6e56">hélicoïdale</text>
<text x="288" y="172" font-size="9" font-weight="700" fill="#0f6e56">glissière</text>
</g>
</svg>
:::

> 🗡️ Lis la chaîne dans le sens de l'énergie : le moteur pas à pas (38) tourne, l'accouplement (37) transmet cette rotation à la vis mère (26), la vis tourne dans son palier (45), l'écrou (25) — immobilisé en rotation — avance le long de la vis, et le traînard (31) qui le porte translate suivant Z.

> ⚠️ Piège classique : croire que le palier « bloque » la vis. Il doit au contraire la **laisser tourner** tout en **l'empêchant de se déplacer suivant son axe** — c'est le rôle des butées à billes. Si la vis pouvait reculer, sa rotation ne ferait plus avancer l'écrou.

### Le schéma cinématique : le mécanisme réduit à ses liaisons

Il existe un dessin qui ne retient d'un mécanisme **que ses liaisons** : le **schéma cinématique**. Chaque pièce y devient un simple trait ou un simple bloc, chaque liaison y prend son **symbole normalisé** — le **bâti** se reconnaît à ses **hachures**, la liaison **hélicoïdale** au trait **ondulé** tracé le long de la vis — et les formes réelles disparaissent : seuls comptent les mouvements autorisés.

Son intérêt : on y lit d'un coup d'œil **quelle fonction technique s'exerce à quel endroit**. Sur l'axe Z, l'**accouplement (37)** lie la vis à l'arbre moteur — c'est **FT512111** ; le **pivot** de la vis (26) dans son palier (45) la guide en rotation — **FT512112** ; la liaison **hélicoïdale** vis-écrou transforme cette rotation en translation — **FT5121** ; l'**encastrement** de l'écrou (25) dans le traînard (31) lui transmet cette translation — **FT512121** ; et la **glissière** du traînard sur le banc (22) lui impose sa direction — **FT513**. Poser une étiquette de fonction sur chacune de ces cinq liaisons, c'est exactement le geste que demande l'activité.

::: figure Le schéma cinématique de l'axe Z : chaque pièce n'est plus qu'un trait ou un bloc, chaque liaison est entourée et porte la fonction technique qu'elle satisfait — le bâti, lui, se reconnaît à ses hachures
<svg viewBox="0 0 460 250">
<path d="M20 214 H440" fill="none" stroke="#0f172a" stroke-width="2"/>
<g stroke="#0f172a" stroke-width="1.3"><path d="M32 214 L23 224 M57 214 L48 224 M82 214 L73 224 M107 214 L98 224 M132 214 L123 224 M157 214 L148 224 M182 214 L173 224 M207 214 L198 224 M232 214 L223 224 M257 214 L248 224 M282 214 L273 224 M307 214 L298 224 M332 214 L323 224 M357 214 L348 224 M382 214 L373 224 M407 214 L398 224 M432 214 L423 224"/></g>
<g fill="none" stroke="#0f172a" stroke-width="2"><path d="M156 190 V214"/><path d="M294 190 V214"/><path d="M78 89 V214"/><path d="M378 104 V214"/></g>
<rect x="164" y="158" width="92" height="48" fill="#0f6e56" opacity="0.12"/>
<rect x="164" y="158" width="92" height="48" fill="none" stroke="#0f172a" stroke-width="2"/>
<path d="M150 190 H300" fill="none" stroke="#0f172a" stroke-width="2.5"/>
<rect x="336" y="56" width="84" height="48" fill="#0f6e56" opacity="0.12"/>
<rect x="336" y="56" width="84" height="48" fill="none" stroke="#0f172a" stroke-width="2"/>
<path d="M204 96 V158" fill="none" stroke="#0f172a" stroke-width="5"/>
<path d="M87 80 H336" fill="none" stroke="#0f172a" stroke-width="3"/>
<path d="M128 80 L132 72 L140 88 L148 72 L156 88 L164 72 L172 88 L180 72 L188 88 L196 72 L204 88 L212 72 L220 88 L228 72 L236 88 L244 80" fill="none" stroke="#0f6e56" stroke-width="2"/>
<rect x="182" y="64" width="44" height="32" fill="none" stroke="#0f172a" stroke-width="2"/>
<rect x="288" y="68" width="32" height="24" fill="none" stroke="#0f172a" stroke-width="2"/>
<circle cx="78" cy="80" r="9" fill="#ffffff" stroke="#0f172a" stroke-width="2"/>
<g fill="none" stroke="#0f6e56" stroke-width="1.6" stroke-dasharray="5 4">
<circle cx="78" cy="80" r="20"/><ellipse cx="204" cy="80" rx="36" ry="24"/><ellipse cx="204" cy="127" rx="22" ry="15"/><ellipse cx="210" cy="190" rx="42" ry="20"/><ellipse cx="304" cy="80" rx="26" ry="20"/>
</g>
<g fill="none" stroke="#0f6e56" stroke-width="1.2"><path d="M78 52 V60"/><path d="M204 52 V56"/><path d="M304 52 V60"/><path d="M178 126 H182"/><path d="M146 176 L170 182"/></g>
<g fill="none" stroke="#94a3b8" stroke-width="1.2"><path d="M248 66 L228 74"/><path d="M272 184 V188"/></g>
<g paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" font-size="9" font-weight="700" fill="#0f6e56" text-anchor="middle">
<text x="78" y="36">pivot (45)</text><text x="78" y="48">FT512112</text>
<text x="204" y="36">hélicoïdale</text><text x="204" y="48">FT5121</text>
<text x="304" y="36">accouplement (37)</text><text x="304" y="48">FT512111</text>
<text x="176" y="124" text-anchor="end">encastrement</text><text x="176" y="136" text-anchor="end">FT512121</text>
<text x="142" y="170" text-anchor="end">glissière</text><text x="142" y="182" text-anchor="end">FT513</text>
</g>
<g paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round" font-size="9" fill="#0f172a" text-anchor="middle">
<text x="140" y="106">(26)</text><text x="250" y="62" text-anchor="start">(25)</text><text x="190" y="172">(31)</text><text x="378" y="84">(38)</text><text x="272" y="180">(22)</text><text x="58" y="208">bâti</text>
</g>
</svg>
:::

## 🎯 Faire tourner la pièce : la chaîne FT6

Dernière branche, celle qui anime la pièce. Le **moteur électrique (21)** — un moteur à courant continu — convertit l'énergie électrique en énergie mécanique. Un **système poulies-courroie** (**poulie motrice (20)**, **courroie crantée (19)**, **poulie réceptrice (13)**) adapte cette rotation à la **broche (11)**. La poulie réceptrice est liée à la broche par une **clavette parallèle (15)**, qui transmet le couple. La broche est **guidée en rotation** par **deux roulements à rouleaux coniques (10)** : une liaison pivot. Enfin le **mandrin (8)** est assemblé sur la broche par **trois goujons M8×28 (52)** et leurs **rondelles Grower (53)** — un encastrement, sans lequel la pièce ne tournerait pas avec la broche. Le moteur lui-même est **lié au banc (22)** par l'assemblage boulonné que montre la coupe B-B : les **vis HC M6×25 (49)**, leurs **rondelles (48)** et leurs **rondelles Grower (50)**, serrées par les **écrous H (51)**.

> ⚠️ Avant toute manipulation réelle : enclencher le bouton d'arrêt d'urgence, utiliser les clés appropriées, porter des gants résistants aux coupures et ranger immédiatement les outils inutilisés.

> 🏆 Le thème est bouclé. Tu as vu la même architecture sous trois machines très différentes — c'est bien qu'elle ne décrit aucune d'elles en particulier, mais **tous les systèmes automatisés**. Emporte-la : dans l'axe suivant, chaque solution constructive que tu rencontreras aura déjà sa place dans une chaîne et une case de F.A.S.T.
