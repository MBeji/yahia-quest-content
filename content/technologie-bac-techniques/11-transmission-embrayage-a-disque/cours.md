# ⚙️ L'embrayage à disque : relier, couper, calculer le couple

> 💡 « Un embrayage ne fait rien tourner : il décide seulement si ce qui tourne d'un côté entraîne ce qui attend de l'autre. Et comme il le fait par frottement, on peut calculer jusqu'où il tient. »

Ce chapitre ouvre le thème **Transmission de puissance**. Jusqu'ici tu lisais des plans et tu jugeais des assemblages ; ici tu suis la rotation du moteur jusqu'à l'arbre de la boîte de vitesses (**BDV**), puis tu calcules ce que l'organe placé entre les deux peut transmettre. Le thème s'ouvre par l'**embrayage** ; les freins, les boîtes de vitesses, la transformation de mouvement et les machines thermiques viennent ensuite.

Le support est la **maquette d'un embrayage à disque** : un socle et un bâti, une **manivelle (23)** qui joue le moteur, un **système de commande à pédale (18)**. Deux compétences sont travaillées : **rechercher les constituants** d'une chaîne de transmission (CD 1.3) et **déterminer ses caractéristiques** (CD 2.3). Le dossier technique donne un dessin d'ensemble à l'**échelle 3:10** et une **nomenclature de 38 repères**.

> 🗡️ Les schémas de ce cours sont des **schémas de principe**, redessinés pour expliquer : ils ne remplacent pas le dessin d'ensemble du manuel, que tu gardes sous les yeux pour relever les repères et les diamètres. Quand un point relève d'un principe de mécanique plutôt que du dessin du manuel, le cours le dit.

## 🦶 Embrayer, débrayer : relier ou couper à volonté

Sur la maquette, tourne la manivelle (23) — c'est le moteur — pédale appuyée, puis pédale relâchée, et regarde l'arbre de sortie (29), celui qui va vers la boîte de vitesses. Il ne réagit pas de la même façon dans les deux cas.

Pour changer de rapport, la boîte ne doit plus être entraînée par un moteur qui continue de tourner. Comment nommer le dispositif qui permet cette coupure, et comment décrire ses deux états ?

::: definition L'embrayage et ses deux positions
Un **embrayage** est un dispositif d'**accouplement temporaire** placé entre le moteur et la boîte de vitesses : il permet de **rompre, puis de rétablir**, la transmission du mouvement de rotation. Il a deux positions :

- **embrayée** : l'embrayage transmet **intégralement** la puissance fournie ;
- **débrayée** : la transmission est **interrompue**.

On change de rapport dans la boîte en position débrayée.
:::

| Pédale | Position | Arbre d'entrée (23) | Arbre de sortie (29) |
| --- | --- | --- | --- |
| **Relâchée** | embrayée | en rotation | en rotation |
| **Appuyée** | débrayée | en rotation | au repos |

Le tableau se lit colonne par colonne : l'arbre d'entrée tourne tant qu'on tourne la manivelle ; seul l'arbre de sortie change d'état, et c'est la pédale qui décide.

::: exemple Remplir le tableau de la maquette
On tourne la manivelle (23) dans les deux cas et on observe l'arbre de sortie (29).

1. **Pédale relâchée** : l'arbre de sortie tourne avec la manivelle. La rotation est transmise : l'embrayage est **embrayé**.
2. **Pédale appuyée** : l'arbre de sortie reste au repos alors que la manivelle tourne. La rotation n'est plus transmise : l'embrayage est **débrayé**.
3. **Fonction du mécanisme** : permettre ou interrompre, à volonté, la transmission de la rotation entre l'arbre d'entrée et l'arbre de sortie.

:::

::: piege Appuyer sur la pédale n'embraye pas
Le mot « embrayage » fait croire qu'appuyer sur la pédale embraye. C'est l'inverse : **pédale relâchée, embrayé** ; **pédale appuyée, débrayé**. Le pied sert à **couper**, et ce sont des ressorts qui maintiennent l'embrayage embrayé au repos (section sur l'effort presseur). Et l'arbre d'entrée ne s'arrête jamais : il tourne tant que le moteur tourne.
:::

::: propriete Embrayée : la même vitesse
Quand l'embrayage est embrayé et que la liaison ne glisse plus, l'arbre de sortie tourne à la **même vitesse de rotation** que l'arbre d'entrée : un embrayage transmet la puissance **sans modifier la vitesse angulaire**. Il ne réduit pas et ne multiplie pas ; c'est la boîte de vitesses qui modifiera la vitesse, plus loin dans le thème.

Cas limite : pendant l'instant où l'embrayage se referme, un court glissement existe. La règle vaut une fois l'embrayage complètement embrayé.
:::

::: verifie
On veut passer un rapport de la boîte de vitesses. L'embrayage doit-il être embrayé ou débrayé, et que fait-on de la pédale ?
---
Il doit être **débrayé** : la boîte n'est alors plus entraînée par le moteur, ce qui permet de changer de rapport. Pour débrayer, on **appuie** sur la pédale.
:::

## 🔗 Le trajet de la puissance : par où passe la rotation

Pédale relâchée, la rotation de la manivelle (23) arrive à l'arbre de sortie (29). Le manuel demande de compléter le cheminement : la manivelle, trois cases vides, l'arbre de sortie.

Quelles sont ces trois pièces, et laquelle des liaisons de la chaîne repose sur un serrage plutôt que sur une forme ?

::: definition Le cheminement du mouvement
Le **cheminement du mouvement** liste, dans l'ordre, les pièces par lesquelles passe la rotation, de l'**arbre d'entrée** à l'**arbre de sortie**. Dans un embrayage à disque, la transmission entre la partie motrice et le disque se fait **par adhérence** : le disque est **serré** entre le volant moteur et le plateau de pression, et ce sont ses garnitures qui frottent.
:::

::: figure Schéma de principe de l'embrayage en position embrayée, en demi-coupe. En vert, la partie motrice (arbre moteur, volant, plateau de pression, couvercle) ; en bleu, la partie menée (disque, arbre primaire) ; en jaune, les deux garnitures. Les ressorts plaquent le plateau contre le disque, serré lui-même contre le volant
<svg viewBox="0 0 520 300"><title>Schéma de principe de l'embrayage, position embrayée</title><line x1="10" y1="230" x2="420" y2="230" stroke="#64748b" stroke-width="1.2" stroke-dasharray="14 4 3 4"/><rect x="20" y="218" width="80" height="12" fill="#bbf7d0" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="96" y="64" width="24" height="166" fill="#bbf7d0" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><polygon points="96,52 268,52 268,160 256,160 256,60 110,60 110,64 96,64" fill="#bbf7d0" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="120" y="70" width="10" height="70" fill="#fde68a" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="138" y="70" width="10" height="70" fill="#fde68a" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="130" y="70" width="8" height="160" fill="#bfdbfe" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="130" y="218" width="270" height="12" fill="#bfdbfe" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="148" y="66" width="26" height="124" fill="#bbf7d0" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><polyline points="174,72 179.1,78 189.4,66 199.6,78 209.9,66 220.1,78 230.4,66 240.6,78 250.9,66 256,72" fill="none" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><line x1="204" y1="122" x2="256" y2="122" stroke="#475569" stroke-width="3"/><line x1="174" y1="100" x2="204" y2="100" stroke="#475569" stroke-width="3"/><line x1="204" y1="144" x2="204" y2="100" stroke="#334155" stroke-width="5" stroke-linecap="round"/><circle cx="204" cy="122" r="4.5" fill="#ffffff" stroke="#0f172a" stroke-width="1.8"/><rect x="216" y="132" width="28" height="24" fill="#fdba74" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="244" y="126" width="8" height="64" fill="#94a3b8" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><text x="108" y="150" font-size="11" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">24</text><text x="161" y="170" font-size="11" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">27</text><text x="230" y="148" font-size="11" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">14</text><text x="58" y="211" font-size="11" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">22</text><text x="412" y="226" font-size="11" font-weight="700" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">29</text><text x="220" y="97" font-size="11" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">32</text><text x="248" y="206" font-size="11" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">20</text><line x1="112" y1="40" x2="125" y2="71" stroke="#64748b" stroke-width="1.2"/><text x="112" y="34" font-size="11" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">37</text><line x1="140" y1="40" x2="134" y2="71" stroke="#64748b" stroke-width="1.2"/><text x="140" y="34" font-size="11" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">25</text><line x1="226" y1="40" x2="226" y2="70" stroke="#64748b" stroke-width="1.2"/><text x="226" y="34" font-size="11" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">26</text><line x1="262" y1="40" x2="262" y2="53" stroke="#64748b" stroke-width="1.2"/><text x="262" y="34" font-size="11" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">30</text><text x="10" y="262" font-size="10.5" font-weight="600" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">22 arbre moteur · 24 volant moteur · 25 disque d'embrayage · 37 garnitures</text><text x="10" y="277" font-size="10.5" font-weight="600" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">27 plateau de pression · 26 ressorts de pression · 30 couvercle</text><text x="10" y="292" font-size="10.5" font-weight="600" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">32 leviers de débrayage · 14 butée · 20 fourchette · 29 arbre primaire (BDV)</text></svg>
:::

Chaque nombre du schéma est un repère de la nomenclature : ce sont les pièces de la maquette. Le disque (25) est pris en sandwich entre le volant moteur (24) et le plateau de pression (27) ; seules ses garnitures (37), en jaune, frottent.

::: exemple Compléter le cheminement du mouvement
Principe de lecture : les repères et leurs désignations viennent de la nomenclature ; le dessin d'ensemble du manuel donne la réalisation exacte.

1. La manivelle (23) fait tourner l'**arbre moteur (22)** : c'est l'entrée de la chaîne.
2. L'arbre moteur porte le **volant moteur (24)** et le fait tourner avec lui.
3. Le volant entraîne le **disque d'embrayage (25)** par adhérence, grâce aux garnitures (37) serrées entre le volant et le plateau de pression (27) — celui-ci, muni des griffes (28), tourne avec le volant.
4. Le disque est lié à l'**arbre primaire de la BDV (29)** et le fait tourner : c'est la sortie.

Cheminement : **manivelle (23) → arbre moteur (22) → volant moteur (24) → disque (25) → arbre primaire (29)**.

:::

::: piege Du serrage, pas d'une forme
Entre le volant et le disque, rien n'est vissé, goupillé ni denté : seule la pression des garnitures entraîne le disque. Chercher une vis ou une clavette à cet endroit, c'est confondre l'**adhérence** et l'**obstacle** (les deux moyens de maintien du thème précédent). Conséquence : si le serrage faiblit, le disque glisse.
:::

::: verifie
Dans le cheminement manivelle (23) → arbre moteur (22) → volant (24) → disque (25) → arbre primaire (29), entre quelles pièces la transmission se fait-elle par adhérence ?
---
Entre le **volant moteur (24)** et le **disque (25)**, par les garnitures : le disque est serré contre le volant, et le plateau de pression le serre de l'autre côté. Les autres liaisons de la chaîne font tourner les pièces ensemble sans glissement : ce sont des liaisons solides.
:::

## 🕹️ La commande : de la pédale au plateau de pression

Les ressorts maintiennent le plateau (27) contre le disque. Pour débrayer, il faut le faire reculer malgré eux, depuis la pédale (18) placée à l'extérieur du mécanisme.

Quelles pièces portent l'effort du pied jusqu'au plateau, dans quel ordre, et de quel type est cette commande ?

::: definition Le système de commande
Le **système de commande** transmet l'action du pied sur la pédale (18) jusqu'au plateau de pression (27), pour le faire **reculer** et débrayer. D'après la description du fonctionnement, l'enchaînement est : **pédale (18) → fourchette (20) → butée d'embrayage (14) → leviers de débrayage (32) → plateau de pression (27)**.

La butée est une **butée à billes** : elle pousse sur les leviers, qui tournent avec l'embrayage, alors que la fourchette, qui pivote seulement autour de son axe (19), ne tourne pas avec lui. Dans la nomenclature, on la reconnaît à ses deux bagues (14), ses six billes (15) tenues par une cage (16), et sa douille (17).
:::

::: figure La chaîne de commande : cinq pièces, quatre actions. En vert, l'entrée (le pied sur la pédale) et la sortie (le plateau qui recule)
<svg viewBox="0 0 340 328"><title>Chaîne de commande de l'embrayage, de la pédale au plateau</title><rect x="20" y="14" width="220" height="40" fill="#bbf7d0" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><text x="130" y="39" font-size="12" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Pédale (18)</text><line x1="130" y1="54" x2="130" y2="72" stroke="#0f172a" stroke-width="2.2"/><polygon points="130,80 126,72 134,72" fill="#0f172a"/><text x="144" y="71" font-size="11" font-weight="600" text-anchor="start" fill="#64748b" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">la fait pivoter</text><rect x="20" y="80" width="220" height="40" fill="#e2e8f0" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><text x="130" y="105" font-size="12" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Fourchette (20)</text><line x1="130" y1="120" x2="130" y2="138" stroke="#0f172a" stroke-width="2.2"/><polygon points="130,146 126,138 134,138" fill="#0f172a"/><text x="144" y="137" font-size="11" font-weight="600" text-anchor="start" fill="#64748b" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">pousse</text><rect x="20" y="146" width="220" height="40" fill="#e2e8f0" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><text x="130" y="171" font-size="12" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Butée d'embrayage (14)</text><line x1="130" y1="186" x2="130" y2="204" stroke="#0f172a" stroke-width="2.2"/><polygon points="130,212 126,204 134,204" fill="#0f172a"/><text x="144" y="203" font-size="11" font-weight="600" text-anchor="start" fill="#64748b" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">pousse sur</text><rect x="20" y="212" width="220" height="40" fill="#e2e8f0" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><text x="130" y="237" font-size="12" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Leviers de débrayage (32)</text><line x1="130" y1="252" x2="130" y2="270" stroke="#0f172a" stroke-width="2.2"/><polygon points="130,278 126,270 134,270" fill="#0f172a"/><text x="144" y="269" font-size="11" font-weight="600" text-anchor="start" fill="#64748b" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">le fait reculer</text><rect x="20" y="278" width="220" height="40" fill="#bbf7d0" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><text x="130" y="303" font-size="12" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Plateau de pression (27)</text></svg>
:::

Entre la pédale et la fourchette, la nomenclature compte encore des pièces de liaison — tige de poussée (3), chape (6), rotule (7), levier de fourche (21) — dont l'ordre exact se lit sur le sous-dessin « Système de commande » du dessin d'ensemble ; ce cours ne le reproduit pas, et le schéma ci-dessus s'en tient aux pièces que la description du fonctionnement cite.

::: exemple Suivre l'effort quand on appuie sur la pédale
1. Le pied agit sur la pédale (18), qui entraîne la rotation de la fourchette (20).
2. La fourchette pousse la butée d'embrayage (14) contre les leviers (32).
3. Les leviers pivotent : la butée pousse l'une de leurs extrémités, l'autre extrémité tire le plateau en arrière (principe du levier : un bout avance, l'autre recule).
4. Le plateau (27) recule contre les ressorts (26) : il lâche le disque, l'embrayage est **débrayé**.
5. On relâche : les ressorts repoussent le plateau, les leviers et la butée reculent, la fourchette revient, l'embrayage est de nouveau **embrayé**. (La commande comporte aussi un ressort de rappel (5).)

:::

::: piege La pédale ne pousse pas le plateau contre le disque
Le plateau est déjà plaqué contre le disque par les ressorts quand on ne touche à rien. La commande agit **contre** eux : elle tire le plateau en arrière. L'effort du pied sert à **débrayer**, jamais à serrer le disque.
:::

::: propriete Le type de commande
On classe une commande d'après la façon dont l'effort du pied est transmis : **mécanique** quand il passe par des **pièces solides** (tiges, leviers, fourchette), **hydraulique** quand il passe par un **liquide sous pression** dans un cylindre.

La nomenclature de la maquette (38 repères) ne contient ni pompe, ni cylindre, ni tuyau : sa commande est **mécanique**. Cas voisin, hors maquette : la commande hydraulique d'une automobile ; on rencontre aussi des commandes pneumatiques (air comprimé) et électriques (actionneur), repères hors fiche.
:::

::: verifie
On relâche la pédale. Dans quel sens se déplace le plateau de pression (27) — vers le disque ou à l'opposé — et qui le pousse ?
---
Il se déplace **vers le disque**, poussé par les **ressorts de pression (26)** : une fois la commande relâchée, plus rien ne les retient, et le plateau serre de nouveau le disque contre le volant.
:::

## 👀 Lire la position sur un schéma : la garde

Un schéma d'embrayage est figé : pas de pédale à enfoncer, pas de manivelle à tourner. Le manuel en montre deux qui ne diffèrent que par la position de la butée et des leviers, et demande si chacun est embrayé ou débrayé.

À quels indices le voit-on, et pourquoi la butée ne touche-t-elle pas les leviers dans l'une des deux positions ?

::: definition La garde
En position embrayée, un petit jeu sépare la butée (14) des leviers (32) : c'est la **garde**. La butée ne commence à agir sur les leviers qu'après l'avoir parcourue. La nomenclature compte deux butées de réglage de garde (4), dont la désignation indique qu'elles servent à la régler.
:::

::: figure Les deux positions côte à côte, avec les mêmes repères que la figure 1. À gauche, embrayée : le plateau (27) touche le disque et la garde sépare la butée (14) du levier (32). À droite, débrayée : la butée pousse le levier, le plateau a reculé et laisse un jeu devant le disque
<svg viewBox="0 0 420 240"><title>Les deux positions de l'embrayage côte à côte</title><g transform="translate(-86,-18)"><line x1="90" y1="230" x2="286" y2="230" stroke="#64748b" stroke-width="1.2" stroke-dasharray="14 4 3 4"/><rect x="96" y="64" width="24" height="166" fill="#bbf7d0" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><polygon points="96,52 268,52 268,160 256,160 256,60 110,60 110,64 96,64" fill="#bbf7d0" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="120" y="70" width="10" height="70" fill="#fde68a" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="138" y="70" width="10" height="70" fill="#fde68a" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="130" y="70" width="8" height="160" fill="#bfdbfe" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="130" y="218" width="156" height="12" fill="#bfdbfe" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="148" y="66" width="26" height="124" fill="#bbf7d0" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><polyline points="174,72 179.1,78 189.4,66 199.6,78 209.9,66 220.1,78 230.4,66 240.6,78 250.9,66 256,72" fill="none" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><line x1="204" y1="122" x2="256" y2="122" stroke="#475569" stroke-width="3"/><line x1="174" y1="100" x2="204" y2="100" stroke="#475569" stroke-width="3"/><line x1="204" y1="144" x2="204" y2="100" stroke="#334155" stroke-width="5" stroke-linecap="round"/><circle cx="204" cy="122" r="4.5" fill="#ffffff" stroke="#0f172a" stroke-width="1.8"/><rect x="216" y="132" width="28" height="24" fill="#fdba74" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="244" y="126" width="8" height="64" fill="#94a3b8" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><text x="108" y="150" font-size="11" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">24</text><text x="161" y="170" font-size="11" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">27</text><text x="230" y="148" font-size="11" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">14</text><text x="220" y="97" font-size="11" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">32</text><text x="248" y="206" font-size="11" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">20</text><line x1="204" y1="166" x2="216" y2="166" stroke="#b91c1c" stroke-width="1.8"/><line x1="204" y1="160" x2="204" y2="172" stroke="#b91c1c" stroke-width="1.8"/><line x1="216" y1="160" x2="216" y2="172" stroke="#b91c1c" stroke-width="1.8"/><text x="210" y="187" font-size="11" font-weight="700" text-anchor="middle" fill="#b91c1c" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">garde</text></g><g transform="translate(124,-18)"><line x1="90" y1="230" x2="286" y2="230" stroke="#64748b" stroke-width="1.2" stroke-dasharray="14 4 3 4"/><rect x="96" y="64" width="24" height="166" fill="#bbf7d0" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><polygon points="96,52 268,52 268,160 256,160 256,60 110,60 110,64 96,64" fill="#bbf7d0" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="120" y="70" width="10" height="70" fill="#fde68a" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="138" y="70" width="10" height="70" fill="#fde68a" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="130" y="70" width="8" height="160" fill="#bfdbfe" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="130" y="218" width="156" height="12" fill="#bfdbfe" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="156" y="66" width="26" height="124" fill="#bbf7d0" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><polyline points="182,72 186.6,78 195.9,66 205.1,78 214.4,66 223.6,78 232.9,66 242.1,78 251.4,66 256,72" fill="none" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><line x1="204" y1="122" x2="256" y2="122" stroke="#475569" stroke-width="3"/><line x1="182" y1="100" x2="212" y2="101.5" stroke="#475569" stroke-width="3"/><line x1="196" y1="142.5" x2="212" y2="101.5" stroke="#334155" stroke-width="5" stroke-linecap="round"/><circle cx="204" cy="122" r="4.5" fill="#ffffff" stroke="#0f172a" stroke-width="1.8"/><rect x="196" y="132" width="28" height="24" fill="#fdba74" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="224" y="126" width="8" height="64" fill="#94a3b8" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><line x1="284" y1="176" x2="241" y2="176" stroke="#0f172a" stroke-width="2.4"/><polygon points="233,176 241,172 241,180" fill="#0f172a"/><text x="258.5" y="168" font-size="10.5" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">poussée</text><text x="108" y="150" font-size="11" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">24</text><text x="169" y="170" font-size="11" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">27</text><text x="210" y="148" font-size="11" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">14</text><text x="228" y="97" font-size="11" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">32</text><text x="228" y="206" font-size="11" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">20</text><line x1="148" y1="200" x2="156" y2="200" stroke="#b91c1c" stroke-width="1.8"/><line x1="148" y1="194" x2="148" y2="206" stroke="#b91c1c" stroke-width="1.8"/><line x1="156" y1="194" x2="156" y2="206" stroke="#b91c1c" stroke-width="1.8"/><text x="164" y="205" font-size="11" font-weight="700" text-anchor="start" fill="#b91c1c" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">jeu</text></g><text x="100" y="232" font-size="12" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">position embrayée</text><text x="310" y="232" font-size="12" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">position débrayée</text></svg>
:::

On lit la position **sur les pièces**, pas sur la pédale, absente du schéma :

| Indice | Embrayée | Débrayée |
| --- | --- | --- |
| Plateau (27) | contre le disque | reculé, un jeu devant le disque |
| Butée (14) et leviers (32) | séparés par la garde | butée en appui, qui pousse |
| Ressorts (26) | moins comprimés (plus longs) | plus comprimés (plus courts) |

::: exemple Lire deux schémas
Un premier schéma montre le plateau contre le disque, la butée à distance des leviers. Un second montre la butée en appui sur les leviers et un jeu devant le disque.

1. **Premier schéma** : le plateau serre le disque et la garde est visible : **embrayée**.
2. **Second schéma** : la garde est rattrapée, la butée pousse les leviers, ceux-ci ont fait reculer le plateau, d'où le jeu devant le disque : **débrayée**.
3. **Contrôle par les ressorts** : sur le second schéma ils sont plus courts, donc plus comprimés, comme il se doit quand le plateau recule.

:::

::: piege Une butée en contact n'est pas une butée qui embraye
On croit parfois que le contact de la butée avec les leviers « relie » les pièces, donc que l'embrayage est embrayé. C'est le contraire : la butée **pousse** les leviers, qui font reculer le plateau, donc l'embrayage est **débrayé**. En position embrayée, c'est la **garde** que l'on voit.
:::

::: propriete La garde est nécessaire
Si la garde était nulle, la butée appuierait en permanence sur les leviers : le plateau ne serait plus plaqué à fond contre le disque, les garnitures patineraient et s'useraient. C'est pourquoi on règle la garde (principe de mécanique général ; le manuel ne chiffre aucune garde).
:::

::: verifie
Sur un schéma, la butée est à distance des leviers et le plateau touche le disque. Quelle est la position, et comment s'appelle la distance qui sépare la butée des leviers ?
---
La position est **embrayée** : le plateau serre le disque. La distance entre la butée et les leviers est la **garde**.
:::

## 🔩 Seize ressorts, un effort presseur

Pour qu'un disque transmette un couple, il faut le serrer. Qui serre, et avec quelle force au total ? Le manuel demande les pièces qui créent l'effort presseur, le nombre et le rôle des ressorts, puis la valeur de l'effort presseur.

On connaît l'effort d'un seul ressort : Fr = 3,5 N. Que vaut l'effort de tous ensemble ?

::: definition L'effort presseur
L'**effort presseur**, noté **N**, est l'effort **axial** (le long de l'arbre) qui plaque le plateau de pression (27) contre le disque (25), lui-même serré contre le volant (24). Il est créé pendant l'embrayage par les **ressorts de pression (26)** : la nomenclature en compte **16**. Il se mesure en newtons : dans « N = 56 N », la première lettre est l'effort presseur, la seconde l'unité newton.
:::

::: exemple Calculer l'effort presseur de la maquette
Données : 16 ressorts de pression identiques, chacun développant **Fr = 3,5 N**.

1. Les ressorts sont identiques et poussent tous dans le même sens, vers le disque : leurs efforts **s'ajoutent**.
2. On multiplie l'effort d'un ressort par leur nombre.

$$ N = 16 × 3,5 = 56 N $$

3. Contrôle : 16 ressorts d'un peu plus de 3 N font un peu plus de 48 N ; 56 N est cohérent. Leur **rôle** : plaquer le plateau contre le disque, donc créer l'effort presseur qui rend la transmission par adhérence possible.

:::

::: piege Fr n'est pas N
**Fr** est l'effort d'**un seul** ressort ; **N** est l'effort de **tous**. Répondre « 3,5 N » à la question de l'effort presseur oublie quinze ressorts sur seize.
:::

::: propriete L'effort presseur est un produit
Quand les ressorts sont identiques et poussent tous dans le même sens :

$$ N = nombre de ressorts × Fr $$

Cas limite : si un ressort casse, il en reste 15 et N = 15 × 3,5 = 52,5 N. L'effort presseur diminue, et avec lui la capacité de l'embrayage à transmettre un couple (voir plus loin).
:::

::: verifie
Un autre embrayage a 10 ressorts de pression de 4,2 N chacun. Quel est son effort presseur ?
---
Les efforts s'ajoutent : N = 10 × 4,2 = **42 N**. C'est l'effort de tous les ressorts ensemble, pas celui d'un seul.
:::

## 🧲 Classer l'embrayage : progressif ou instantané, quelle surface

Le manuel précise que la transmission par adhérence offre une mise en charge progressive, qui évite les à-coups. Il demande ensuite de préciser le type de l'embrayage, puis celui de ses surfaces de friction.

Que veulent dire ces classements, et que répondre pour la maquette ?

::: definition Deux façons de classer un embrayage
- **Comment la transmission s'établit.** Un embrayage **progressif** transmet par adhérence : un bref glissement précède la transmission complète, ce qui évite les à-coups. Un embrayage **instantané** transmet sans glissement, par obstacle (des dents qui s'engagent), et la liaison s'établit d'un coup (exemple hors maquette : l'embrayage à crabots).
- **La forme des surfaces de friction.** Elles sont **planes** (perpendiculaires à l'axe), **coniques** ou **cylindriques**.
:::

::: figure Trois formes de surfaces de friction, en demi-coupe. La ligne rouge est la surface où deux pièces frottent : perpendiculaire à l'axe pour la forme plane, inclinée pour la forme conique, parallèle à l'axe pour la forme cylindrique
<svg viewBox="0 0 460 196"><title>Trois formes de surfaces de friction en demi-coupe</title><line x1="10" y1="150" x2="150" y2="150" stroke="#64748b" stroke-width="1.2" stroke-dasharray="14 4 3 4"/><rect x="35" y="50" width="22" height="100" fill="#bbf7d0" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="57" y="50" width="10" height="100" fill="#bfdbfe" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="67" y="50" width="22" height="100" fill="#bbf7d0" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><line x1="57" y1="50" x2="57" y2="150" stroke="#ef4444" stroke-width="4"/><line x1="67" y1="50" x2="67" y2="150" stroke="#ef4444" stroke-width="4"/><text x="80" y="180" font-size="12" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">plane</text><line x1="160" y1="150" x2="300" y2="150" stroke="#64748b" stroke-width="1.2" stroke-dasharray="14 4 3 4"/><polygon points="200,100 240,70 240,150 200,150" fill="#bfdbfe" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><polygon points="200,100 240,70 240,54 200,84" fill="#bbf7d0" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><line x1="200" y1="100" x2="240" y2="70" stroke="#ef4444" stroke-width="4"/><text x="220" y="180" font-size="12" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">conique</text><line x1="310" y1="150" x2="450" y2="150" stroke="#64748b" stroke-width="1.2" stroke-dasharray="14 4 3 4"/><rect x="340" y="66" width="70" height="22" fill="#bbf7d0" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="340" y="88" width="70" height="62" fill="#bfdbfe" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><line x1="340" y1="88" x2="410" y2="88" stroke="#ef4444" stroke-width="4"/><text x="375" y="180" font-size="12" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">cylindrique</text></svg>
:::

Dans le disque de la maquette, les deux faces garnies sont perpendiculaires à l'axe : on se trouve dans le premier cas du dessin.

::: exemple Classer l'embrayage de la maquette
1. **Établissement de la transmission** : les garnitures (37) sont serrées par les ressorts, la transmission est par adhérence et le manuel parle de mise en charge progressive : l'embrayage est **progressif**.
2. **Surfaces de friction** : le disque est un disque plat, ses garnitures frottent sur des faces perpendiculaires à l'axe : surfaces **planes**.
3. **Conclusion** : embrayage progressif, à surfaces de friction planes.

:::

::: piege Progressif ne veut pas dire partiel
« Progressif » décrit la **manière** dont la transmission s'établit — avec un bref glissement —, pas la puissance transmise ensuite. Une fois embrayé, un embrayage progressif transmet **intégralement** la puissance.
:::

::: verifie
On remplace le disque plat par deux pièces coniques emboîtées, toujours serrées par des ressorts. L'embrayage est-il progressif ou instantané ? Quelle est la forme de la surface ?
---
Il reste **progressif** : la transmission se fait toujours par serrage et frottement, donc par adhérence. La surface de friction est **conique** : sur une demi-coupe, sa trace est inclinée par rapport à l'axe.
:::

## 📐 Le couple transmissible : de la formule à la valeur de f

Le manuel fixe les données de l'étude : le couple maximum à transmettre **Ct = 3,2 N·m**, l'effort d'un ressort **Fr = 3,5 N**, les 16 ressorts, et les diamètres **D** et **d** du disque, à relever sur le dessin d'ensemble. Il demande quel coefficient de frottement **f** la garniture doit avoir.

Pour y répondre, il faut une formule qui relie le couple aux dimensions du disque et à l'effort presseur.

::: definition Le couple transmissible Ct
Le **couple transmissible** Ct est le **couple maximum** que l'embrayage transmet sans glisser. Pour un disque à surfaces planes, le manuel donne la formule :

$$ Ct = (2/3) × n × f × N × (R³ − r³) / (R² − r²) $$

On la lit en deux temps :

$$ Rm = (2/3) × (R³ − r³) / (R² − r²) $$

$$ Ct = n × f × N × Rm $$

**f × N** est l'effort de frottement sur une surface, **n** le nombre de surfaces, et **Rm** le rayon auquel on peut le supposer appliqué : on retrouve « un effort multiplié par un bras de levier ».
:::

| Symbole | Signification | Unité |
| --- | --- | --- |
| Ct | couple transmissible maximum | N·mm (ou N·m) |
| n | nombre de surfaces de friction | — |
| f | coefficient de frottement des garnitures | — |
| N | effort presseur | N |
| R | rayon extérieur de la couronne de friction, R = D/2 | mm |
| r | rayon intérieur de la couronne de friction, r = d/2 | mm |
| Rm | rayon d'action de la friction | mm |

> 🗡️ Le manuel n'imprime aucune légende de ces symboles : n, f et N se déduisent de ses questions, et, dans cette formule classique, R et r sont les rayons de la couronne de friction, donc D/2 et d/2. **Rm** est une notation de ce cours, pas du manuel.

::: figure La couronne de friction vue de face : le diamètre extérieur D et le diamètre intérieur d se mesurent sur le dessin ; le rayon extérieur R et le rayon intérieur r en sont les moitiés
<svg viewBox="0 0 260 226"><title>Couronne de friction vue de face : diamètres D et d, rayons R et r</title><circle cx="130" cy="118" r="84" fill="#fde68a" stroke="#0f172a" stroke-width="2"/><circle cx="130" cy="118" r="50" fill="#ffffff" stroke="#0f172a" stroke-width="2"/><line x1="38" y1="118" x2="222" y2="118" stroke="#64748b" stroke-width="1.1" stroke-dasharray="10 3 2 3"/><circle cx="130" cy="118" r="3" fill="#0f172a" stroke="#0f172a" stroke-width="1"/><line x1="46" y1="20" x2="46" y2="118" stroke="#64748b" stroke-width="1" stroke-dasharray="4 3"/><line x1="214" y1="20" x2="214" y2="118" stroke="#64748b" stroke-width="1" stroke-dasharray="4 3"/><line x1="47" y1="28" x2="206" y2="28" stroke="#0f172a" stroke-width="1.8"/><polygon points="213,28 206,31.5 206,24.5" fill="#0f172a"/><line x1="213" y1="28" x2="54" y2="28" stroke="#0f172a" stroke-width="1.8"/><polygon points="47,28 54,24.5 54,31.5" fill="#0f172a"/><text x="130" y="22" font-size="13" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">D</text><line x1="81" y1="102" x2="172" y2="102" stroke="#0f172a" stroke-width="1.8"/><polygon points="179,102 172,105.5 172,98.5" fill="#0f172a"/><line x1="179" y1="102" x2="88" y2="102" stroke="#0f172a" stroke-width="1.8"/><polygon points="81,102 88,98.5 88,105.5" fill="#0f172a"/><text x="130" y="96" font-size="13" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">d</text><line x1="130" y1="118" x2="196.2" y2="169.7" stroke="#ef4444" stroke-width="3"/><text x="188.3" y="156.2" font-size="13" font-weight="700" text-anchor="middle" fill="#ef4444" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">R</text><line x1="130" y1="118" x2="89" y2="146.7" stroke="#2563eb" stroke-width="3"/><text x="98.5" y="137.8" font-size="13" font-weight="700" text-anchor="middle" fill="#2563eb" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">r</text></svg>
:::

::: exemple Trouver le coefficient de frottement de la garniture
Données du manuel : Ct = 3,2 N·m, 16 ressorts de Fr = 3,5 N. Les diamètres sont à relever sur le dessin ; on prend ici des valeurs d'entraînement : D = 180 mm et d = 120 mm, donc 54 mm et 36 mm mesurés sur le papier.

1. **Rayons.** L'échelle 3:10 est une réduction : 3 mm de papier valent 10 mm réels. Donc 54 mm de papier valent 54 × 10 ÷ 3 = 180 mm, et 36 mm valent 120 mm. D'où **R = 180 ÷ 2 = 90 mm** et **r = 120 ÷ 2 = 60 mm**.
2. **n et N.** La nomenclature compte 2 garnitures (37), une par face du disque : **n = 2**. Et **N = 16 × 3,5 = 56 N**.
3. **Rayon d'action.**

$$ Rm = (2/3) × (90³ − 60³) / (90² − 60²) = (2/3) × 513 000 / 4 500 = 76 mm $$

Contrôle : r < Rm < R, soit 60 < 76 < 90 mm : le résultat est plausible.
4. **Unités.** Les rayons sont en mm : on exprime Ct en N·mm. Ct = 3,2 N·m = **3 200 N·mm**.
5. **On isole f.**

$$ f = Ct / (n × N × Rm) = 3 200 / (2 × 56 × 76) = 3 200 / 8 512 ≈ 0,376 $$

:::

::: piege Les diamètres ne vont pas dans la formule
Remplacer R et r par D et d double le rayon d'action : Rm = 152 mm, plus grand que R = 90 mm, ce qui est impossible. On trouverait alors f ≈ 0,19 au lieu de 0,38, et on choisirait une garniture trop faible. **Rm reste toujours entre r et R** : c'est le contrôle à faire.
:::

::: piege N·m et N·mm ne se mélangent pas
Avec des rayons en mm, Ct sort en N·mm. Poser 3,2 à la place de 3 200 donnerait un f mille fois trop petit. On convertit **avant** de calculer.
:::

::: propriete Ct est proportionnel à n, à f et à N
Dans Ct = n × f × N × Rm, doubler f, ou N, double Ct. Le rayon d'action Rm grandit quand R grandit : un disque plus large transmet plus de couple, toutes choses égales d'ailleurs. Et Ct est un **maximum** : si le couple à transmettre le dépasse, les garnitures glissent.

- f double, le reste inchangé : Ct double.
- Un ressort casse (N passe de 56 à 52,5 N) : Ct est multiplié par 52,5 ÷ 56 = 0,9375, soit une baisse de 6,25 %.
- Couple à transmettre de 4 N·m pour un Ct de 3,2 N·m : le disque patine.
:::

::: verifie
Un disque a n = 2, N = 40 N, f = 0,3, R = 50 mm et r = 30 mm. Quel est son couple transmissible, en N·m ?
---
Rayon d'action : Rm = (2/3) × (50³ − 30³) / (50² − 30²) = (2/3) × 98 000 / 1 600 ≈ 40,8 mm (entre 30 et 50 : plausible). Puis Ct = 2 × 0,3 × 40 × 40,8 ≈ 980 N·mm, soit **0,98 N·m**.
:::

## 🧱 Choisir la garniture : le matériau qui convient

Le manuel propose trois matériaux pour la garniture (37), avec leur coefficient de frottement : matériau 1, f = 0,4 ; matériau 2, f = 0,35 ; matériau 3, f = 0,3. Dans la section précédente, le calcul a donné f ≈ 0,376.

Lequel choisir, et comment justifier ce choix ? Comme Ct est proportionnel à f, chaque matériau donne son propre couple transmissible : il suffit de le calculer.

Avec n = 2, N = 56 N et Rm = 76 mm de la section précédente, Ct = 8 512 × f (en N·mm) :

| Matériau | f | Ct obtenu | Atteint 3,2 N·m ? |
| --- | --- | --- | --- |
| 1 | 0,4 | 3 404,8 N·mm, soit 3,40 N·m | oui |
| 2 | 0,35 | 2 979,2 N·mm, soit 2,98 N·m | non |
| 3 | 0,3 | 2 553,6 N·mm, soit 2,55 N·m | non |

Le tableau fait la comparaison : une ligne par matériau, et un seul atteint le couple demandé.

::: exemple Justifier le choix
1. **Rappeler** le f nécessaire : 0,376.
2. **Comparer** : 0,4 ≥ 0,376 ; mais 0,35 < 0,376 et 0,3 < 0,376.
3. **Vérifier** par le couple obtenu : seul le matériau 1 donne plus de 3,2 N·m (3,40 N·m).
4. **Conclure** : on choisit le **matériau 1**, car lui seul a un coefficient de frottement supérieur à celui que le calcul exige.

:::

::: piege Le plus proche par en dessous ne convient pas
Le matériau 2 (f = 0,35) paraît « presque » suffisant. Mais « presque » ne transmet pas : il donne 2,98 N·m, moins que les 3,2 N·m demandés, et l'embrayage patinerait.
:::

::: methode Choisir un matériau de garniture
Un matériau convient si son coefficient f est **au moins égal** au f calculé : le f calculé est le plus petit qui transmette le couple demandé.

1. **Calculer** le coefficient de frottement nécessaire pour transmettre Ct.
2. **Comparer** avec le tableau des matériaux.
3. **Retenir** ceux dont f est supérieur ou égal au f calculé.
4. **Justifier** par le couple obtenu avec chacun, comparé au couple demandé.

Cas limite : un f exactement égal au f calculé convient, sans marge ; en pratique on garde une marge (repère hors fiche).
:::

::: verifie
Un calcul donne f = 0,33. Quels matériaux du tableau (0,4 ; 0,35 ; 0,3) conviennent ?
---
Ceux dont f est au moins égal à 0,33 : les matériaux **1 (0,4) et 2 (0,35)**. Le matériau 3 (0,3) est plus petit que 0,33 : il ne transmettrait pas le couple demandé.
:::

## 🧭 La méthode qui reste : six marches

Devant un embrayage inconnu, tu reprends toujours cet ordre :

1. **Positions** : embrayée ou débrayée, et ce que fait la pédale.
2. **Puissance** : suivre la rotation de l'arbre d'entrée à l'arbre de sortie, et repérer la liaison par adhérence.
3. **Commande** : pédale → fourchette → butée → leviers → plateau.
4. **Lecture d'un schéma** : le plateau, la garde, les ressorts.
5. **Effort presseur** : N = nombre de ressorts × effort d'un ressort.
6. **Caractéristiques** : classer l'embrayage, calculer Ct ou f, puis choisir la garniture.

::: retenir
Un embrayage est un accouplement **temporaire** : **pédale relâchée**, il est embrayé (les ressorts serrent le disque, la transmission se fait par adhérence, à la même vitesse) ; **pédale appuyée**, la commande fait reculer le plateau et il est débrayé. Il se caractérise par son effort presseur **N = nombre de ressorts × Fr** et par son couple transmissible **Ct = n × f × N × Rm**, dont on tire le coefficient de frottement f de la garniture.
:::

> 🏆 Tu sais suivre la rotation et l'effort dans un embrayage, lire ses deux positions et calculer ce qu'il peut transmettre. La suite du thème, le frein, repart de ce même frottement.
