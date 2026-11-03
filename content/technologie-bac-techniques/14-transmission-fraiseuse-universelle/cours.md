# 🛠️ La fraiseuse universelle : freiner, régler, avancer

> 💡 «Une fraiseuse ne coupe bien que si trois choses sont maîtrisées : l'arrêt de sa broche, sa vitesse de rotation et l'avance de la pièce. Ce chapitre ouvre le capot sur chacune des trois.»

Ce chapitre poursuit le thème « Transmission de puissance », après l'embrayage, le tour et la boîte de vitesses d'automobile. Le support est la **fraiseuse universelle** (« Milko-12 » pour le frein, « Milko-14 » sur la photo de la boîte), étudiée en trois volets : son **frein électromagnétique** en bout d'arbre moteur, sa **boîte de vitesses**, qui règle la vitesse de la broche, et son **système vis-écrou**, qui avance la table. Les notations des chapitres précédents reviennent : Ct, f, N, Rm, r.

> 🗡️ Les schémas de ce cours sont des **schémas de principe**, redessinés pour expliquer : les dessins d'ensemble du manuel (échelles 1:2, 1:4 et 1:5) ne sont pas reproduits, et le manuel ne donne aucun corrigé. Quand un point relève d'un **principe** de mécanique plutôt que du dessin, le texte le dit ; quand une valeur est choisie pour s'entraîner, il parle d'**illustration** ; quand elle vient de la nomenclature ou de la plaque, il le précise.

> 🛡️ **Consignes de sécurité du manuel.** La fraiseuse n'est d'abord **pas sous tension**. On retire la cage du ventilateur (1) en rangeant ses vis, **puis** on met la machine sous tension, **puis** on la lance avec le bouton d'essai, à bonne distance du moteur. Tout se fait avec précaution, en présence du professeur.

## 🧲 Qui bouge dans le frein ? Mouvements et classes

La plupart des fraiseuses ont un frein, pour deux raisons : gagner du temps au changement de pièce quand les opérations sont très courtes, et **arrêter la broche immédiatement** en cas d'accident (outil ou pièce cassés, blessure). Sur la « Milko-12 », c'est un **frein électromagnétique à disque**, monté en bout d'arbre moteur.

Quand l'arbre tourne, quelles pièces tournent avec lui, lesquelles vont et viennent, lesquelles ne bougent jamais ?

::: definition Tournante, glissante, fixe
On juge le mouvement d'une pièce **par rapport au bâti** de la machine :
- **tournante** : elle tourne autour de l'axe de l'arbre ;
- **glissante** : elle se déplace en translation, ici le long de l'axe, sans tourner ;
- **fixe** : elle ne bouge pas du tout.

Les pièces sans **aucun mouvement relatif** forment une **classe d'équivalence** (chapitre sur la poupée mobile). Le manuel donne celle du bâti : A = { 1, 3, 4, 5, 6, 8, 10, 13, 15, BE11, 12, 22, 20 }.
:::

::: figure Demi-coupe de principe du frein, vu serré. Gris : pièces fixes de la classe A ; vert : pièces qui tournent avec l'arbre moteur (21) ; bleu : le plateau mobile (17), qui glisse le long de l'axe sans tourner ; jaune : les garnitures. Les écarts sont exagérés
<svg viewBox="0 0 340 212"><title>Demi-coupe de principe d'un frein électromagnétique à disque, en état serré, avec les mouvements des pièces</title><rect x="15" y="126" width="300" height="8" fill="#bbf7d0" stroke="#0f172a" stroke-width="1.4" stroke-linejoin="round"/><rect x="45" y="62" width="54" height="44" fill="#cbd5e1" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><rect x="102" y="110" width="24" height="16" fill="#bbf7d0" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><rect x="108" y="74" width="12" height="36" fill="#bbf7d0" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><rect x="99" y="74" width="9" height="22" fill="#fde68a" stroke="#0f172a" stroke-width="1.4" stroke-linejoin="round"/><rect x="120" y="74" width="9" height="22" fill="#fde68a" stroke="#0f172a" stroke-width="1.4" stroke-linejoin="round"/><rect x="195" y="58" width="84" height="50" fill="#cbd5e1" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><rect x="195" y="64" width="27" height="18" fill="#fdba74" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><rect x="129" y="62" width="18" height="44" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><polyline points="147 96 151.8 96 154.2 100 159 92 163.8 100 168.6 92 173.4 100 178.2 92 183 100 187.8 92 190.2 96 195 96" fill="none" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round" stroke-linecap="round"/><line x1="9" y1="134" x2="321" y2="134" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round" stroke-dasharray="7 4"/><text x="60" y="10" font-size="9.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">flasque (10)</text><line x1="72" y1="62" x2="60" y2="13" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round"/><text x="118" y="26" font-size="9.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">disque (16)</text><line x1="114" y1="74" x2="118" y2="29" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round"/><text x="196" y="10" font-size="9.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">plateau mobile (17)</text><line x1="138" y1="62" x2="196" y2="13" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round"/><text x="295" y="10" font-size="9.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">armature (4)</text><line x1="255" y1="58" x2="295" y2="13" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round"/><text x="246" y="26" font-size="9.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">bobine (22)</text><line x1="208.5" y1="64" x2="246" y2="29" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round"/><text x="268" y="166" font-size="9.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">arbre moteur (21)</text><line x1="268" y1="134" x2="268" y2="169" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round"/><line x1="171" y1="90" x2="171" y2="56" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round"/><text x="173" y="50" font-size="9.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">ressort (7)</text><rect x="14" y="177" width="10" height="10" fill="#cbd5e1" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round"/><text x="28" y="186" font-size="9.5" font-weight="500" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">fixe : classe A</text><rect x="150" y="177" width="10" height="10" fill="#bbf7d0" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round"/><text x="164" y="186" font-size="9.5" font-weight="500" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">tourne avec l'arbre</text><rect x="14" y="194" width="10" height="10" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round"/><text x="28" y="203" font-size="9.5" font-weight="500" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">glisse sans tourner</text><rect x="150" y="194" width="10" height="10" fill="#fde68a" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round"/><text x="164" y="203" font-size="9.5" font-weight="500" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">garniture</text></svg>
:::

Dans A, on reconnaît l'armature (4), le flasque (10), le stator (12), la bobine (22), les goujons (8) et le câble (20) : tout ce qui tient au bâti. Le disque (16) n'y figure pas.

::: exemple Classer quatre pièces du frein (principe)
1. **Armature de bobine (4)** : elle est dans A, donc sans mouvement relatif avec le bâti : **fixe**.
2. **Flasque (10)** : il est dans A aussi : **fixe**.
3. **Disque de frein (16)** : il n'est pas dans A et l'arbre moteur (21) l'entraîne : **tournante**.
4. **Plateau mobile (17)** : il n'est pas dans A, donc il bouge par rapport au bâti. Son rôle est d'aller et venir le long de l'axe pour pincer ou lâcher le disque : **glissante**.

:::

::: piege Un roulement appartient à deux classes
Le manuel range **BE11**, la bague extérieure du roulement (11), dans A : elle est fixe. Sa bague intérieure, elle, suit l'arbre. On ne dit donc pas « un roulement est fixe » : on juge chaque bague, parce que c'est elle qui est liée à l'une ou à l'autre classe.
:::

::: verifie
Pourquoi le flasque (10) est-il dans la classe A alors que le disque (16) n'y est pas ?
---
Le flasque n'a **aucun mouvement relatif** par rapport au bâti : il est fixe, donc dans A. Le disque tourne avec l'arbre : il bouge par rapport au bâti, donc il appartient à une autre classe.
:::

## ⚡ Libre ou freiné ? La commande, la bobine et les ressorts

Un frein de sécurité doit serrer quand on a le plus besoin de lui, y compris si le courant disparaît. Le manuel fait calculer « l'effort presseur Fp fourni par les ressorts (7) » : ce sont donc les trois ressorts de la nomenclature qui serrent le disque.

À quoi sert alors la bobine (22), et que se passe-t-il quand on coupe le courant ?

::: definition Commande électrique et deux états du frein
La **commande** d'un frein est le moyen de lui donner l'ordre : **mécanique** (l'effort de la main ou du pied, transmis pièce par pièce : levier du frein de stationnement, pédale du tour) ou **électrique** (un courant dans une bobine). Ici elle est **électrique**. Dans le principe de ce frein :
- **bobine non excitée** (pas de courant) : les ressorts poussent le plateau mobile contre le disque, qui est pincé : le frein est **serré**, la broche est **freinée** ;
- **bobine excitée** (courant) : elle attire le plateau mobile et comprime les ressorts : le disque n'est plus pincé, le frein est **libre**.
:::

::: figure Les deux états du frein, en demi-coupe de principe. En haut, bobine non excitée : les ressorts poussent le plateau contre le disque, qui est pincé. En bas, bobine excitée : elle attire le plateau, les ressorts sont comprimés et le disque est libre. Les écarts sont exagérés : l'entrefer est exagéré, en réalité le plateau vient au contact de l'armature
<svg viewBox="0 0 310 298"><title>Les deux états du frein électromagnétique : bobine non excitée, puis bobine excitée</title><g transform="translate(0 0) scale(0.9)"><rect x="15" y="126" width="300" height="8" fill="#bbf7d0" stroke="#0f172a" stroke-width="1.4" stroke-linejoin="round"/><rect x="45" y="62" width="54" height="44" fill="#cbd5e1" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><rect x="102" y="110" width="24" height="16" fill="#bbf7d0" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><rect x="108" y="74" width="12" height="36" fill="#bbf7d0" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><rect x="99" y="74" width="9" height="22" fill="#fde68a" stroke="#0f172a" stroke-width="1.4" stroke-linejoin="round"/><rect x="120" y="74" width="9" height="22" fill="#fde68a" stroke="#0f172a" stroke-width="1.4" stroke-linejoin="round"/><rect x="195" y="58" width="84" height="50" fill="#cbd5e1" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><rect x="195" y="64" width="27" height="18" fill="#fdba74" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><rect x="129" y="62" width="18" height="44" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><polyline points="147 96 151.8 96 154.2 100 159 92 163.8 100 168.6 92 173.4 100 178.2 92 183 100 187.8 92 190.2 96 195 96" fill="none" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round" stroke-linecap="round"/><line x1="9" y1="134" x2="321" y2="134" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round" stroke-dasharray="7 4"/><text x="118" y="26" font-size="9.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">disque (16)</text><line x1="114" y1="74" x2="118" y2="29" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round"/><text x="196" y="10" font-size="9.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">plateau (17)</text><line x1="138" y1="62" x2="196" y2="13" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round"/><text x="246" y="26" font-size="9.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">bobine (22)</text><line x1="208.5" y1="64" x2="246" y2="29" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round"/><line x1="171" y1="90" x2="171" y2="56" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round"/><text x="173" y="50" font-size="9.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">ressort (7)</text></g><text x="150" y="138" font-size="11" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Bobine non excitée</text><g transform="translate(0 150) scale(0.9)"><rect x="15" y="126" width="300" height="8" fill="#bbf7d0" stroke="#0f172a" stroke-width="1.4" stroke-linejoin="round"/><rect x="45" y="62" width="54" height="44" fill="#cbd5e1" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><rect x="102" y="110" width="24" height="16" fill="#bbf7d0" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><rect x="108" y="74" width="12" height="36" fill="#bbf7d0" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><rect x="99" y="74" width="9" height="22" fill="#fde68a" stroke="#0f172a" stroke-width="1.4" stroke-linejoin="round"/><rect x="120" y="74" width="9" height="22" fill="#fde68a" stroke="#0f172a" stroke-width="1.4" stroke-linejoin="round"/><rect x="195" y="58" width="84" height="50" fill="#cbd5e1" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><rect x="195" y="64" width="27" height="18" fill="#fdba74" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><rect x="162" y="62" width="18" height="44" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><polyline points="180 96 183.8 96 185.6 100 189.4 92 191.2 96 195 96" fill="none" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round" stroke-linecap="round"/><line x1="9" y1="134" x2="321" y2="134" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round" stroke-dasharray="7 4"/><text x="118" y="26" font-size="9.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">disque (16)</text><line x1="114" y1="74" x2="118" y2="29" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round"/><text x="196" y="10" font-size="9.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">plateau (17)</text><line x1="171" y1="62" x2="196" y2="13" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round"/><text x="246" y="26" font-size="9.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">bobine (22)</text><line x1="208.5" y1="64" x2="246" y2="29" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round"/><line x1="187.5" y1="90" x2="187.5" y2="56" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round"/><text x="189.5" y="50" font-size="9.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">ressort (7)</text></g><text x="150" y="288" font-size="11" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Bobine excitée</text></svg>
:::

::: exemple Quel état dans quelle situation ? (principe)
1. **Arrêt d'urgence.** Le courant est coupé, la bobine n'est plus excitée : les ressorts repoussent le plateau, le disque est pincé et la broche s'arrête vite. C'est l'arrêt immédiat que la situation demande.
2. **Machine en marche.** La bobine est excitée, le plateau est attiré : le disque est libre. Sinon la broche tournerait en frottant sur les garnitures.
3. **Machine hors tension** (consigne de départ). Pas de courant, donc bobine non excitée : le frein est **serré** au repos.
4. **Lire le dessin d'ensemble.** Il montre le frein dans l'un de ces deux états : on regarde où se trouve le plateau, collé au disque (bobine non excitée) ou rapproché de l'armature (bobine excitée).

:::

::: piege La bobine ne freine pas : elle desserre
On croit que la bobine « fait le freinage », parce que le frein est dit électromagnétique. C'est l'inverse : le freinage vient des **ressorts** et la bobine l'annule tant qu'elle est alimentée. C'est pourquoi une coupure de courant freine au lieu de libérer.
:::

::: piege Écrou autofreiné : le frein est celui de l'écrou
Les trois écrous autofreinés (6) de la nomenclature ne participent pas au freinage de la broche : le mot décrit l'écrou lui-même. Son insert déformable serre le filet, si bien qu'il **ne se desserre pas seul** sous les vibrations du moteur. Leur rôle est de **garder l'assemblage serré**, comme la rondelle frein des chapitres sur les assemblages.
:::

::: verifie
On coupe le courant alors que la broche tourne. Le frein serre-t-il ou libère-t-il, et pourquoi ?
---
Il **serre** : sans courant, la bobine n'est plus excitée, donc elle n'attire plus le plateau mobile ; les ressorts le repoussent contre le disque, qui est pincé.
:::

## 🧮 Le couple de freinage : de Cf à l'effort de chaque ressort

Le manuel vise un couple de freinage **Cf = 18 N·m** avec un coefficient de frottement **f = 0,4**. Il demande l'effort presseur Fp que doivent fournir les ressorts (7), puis l'effort de **chaque** ressort.

La formule est connue, au nom des lettres près : comment la retourner pour isoler Fp ?

::: definition Le couple de freinage Cf
Pour un disque à surfaces planes, le manuel donne :

$$ Cf = (2/3) × Fp × f × n × (R³ − r³) / (R² − r²) $$

On la lit comme celle du couple transmissible Ct de l'embrayage, en deux temps :

$$ Rm = (2/3) × (R³ − r³) / (R² − r²) $$

$$ Cf = n × f × Fp × Rm $$

Ici l'effort presseur s'écrit **Fp** (le « N » de l'embrayage), pour ne pas le confondre avec une vitesse de rotation en tr/min. **n** est le nombre de surfaces de frottement, **R** et **r** les rayons extérieur et intérieur de la couronne de frottement, **Rm** le rayon d'action de la friction.
:::

::: exemple Trouver l'effort de chaque ressort (illustration)
Données du manuel : Cf = 18 N·m, f = 0,4, 3 ressorts (7). Valeurs d'entraînement, car R et r se relèvent sur le dessin : R = 60 mm et r = 40 mm. La nomenclature compte 2 garnitures (14) : on lit **n = 2**, une surface de frottement par garniture.
1. **Rayon d'action.** Rm = (2/3) × (60³ − 40³) / (60² − 40²) = (2/3) × 152 000 / 2 000 ≈ 50,7 mm. Contrôle : 40 < 50,7 < 60, c'est plausible.
2. **Unités.** Les rayons sont en mm : on exprime Cf en N·mm, soit 18 N·m = 18 000 N·mm.
3. **On isole Fp.** Fp = Cf / (n × f × Rm) = 18 000 / (2 × 0,4 × 50,7) ≈ **444 N** : c'est l'effort de **tous** les ressorts ensemble.
4. **Un ressort.** Les trois ressorts sont identiques : 444 / 3 ≈ **148 N** chacun. Contrôle : 3 × 148 = 444 N, et 2 × 0,4 × 444 × 50,7 ≈ 18 000 N·mm.

:::

::: piege Fp n'est pas l'effort d'un ressort
Fp est l'effort **total** que les ressorts exercent sur le disque. Lire 444 N comme l'effort d'un seul ressort donnerait trois fois trop d'effort, donc un frein qui serrerait trois fois trop fort. On divise par le nombre de ressorts **à la fin**, une fois Fp trouvé. Autres glissades classiques : mettre les diamètres à la place des rayons (Rm double, donc Fp est divisé par deux), oublier n, ou mélanger les unités : des rayons en mm donnent un Cf en N·mm.
:::

::: propriete Cf est proportionnel à n, à f et à Fp
Chaque facteur multiplie Cf : doubler l'un double Cf, et Fp = 0 donne Cf = 0 (sans effort presseur, le disque tourne librement). Tant que n, f et Rm ne changent pas, **Cf et Fp varient dans le même rapport**.

- Une des deux garnitures s'arrache : n passe de 2 à 1, Cf est divisé par 2 pour le même Fp.
- Un ressort sur les trois casse : Fp tombe aux 2/3, donc Cf aussi : 12 N·m au lieu de 18 dans l'exemple.
- Les garnitures s'usent et f baisse : Cf baisse.

La vitesse de rotation de l'arbre n'intervient pas dans la formule.
:::

::: verifie
Un frein a n = 2 surfaces de frottement, f = 0,4 et Rm = 45 mm. Les ressorts exercent Fp = 300 N en tout. Que vaut Cf, en N·m ?
---
Cf = 2 × 0,4 × 300 × 45 = 10 800 N·mm, soit **10,8 N·m**. Le rayon est en mm, donc le résultat sort en N·mm : on le convertit à la fin.
:::

## 🎚️ Douze vitesses de broche : lire la plaque

En usinage, la **vitesse de coupe** dépend de la matière usinée, du type d'opération, de l'outil et de l'état de surface souhaité. Aucune vitesse ne convient à tout : la fraiseuse est équipée d'un mécanisme qui règle la vitesse de la broche, la **boîte de vitesses**. Sa plaque en affiche les douze valeurs.

Comment retrouver une vitesse sur cette plaque, et pourquoi y en a-t-il douze ?

::: definition La gamme des vitesses et la combinaison des leviers
La **gamme des vitesses** est l'ensemble des vitesses de rotation de la broche que la machine peut atteindre, ici douze. La plaque se lit par ligne et par colonne : la **combinaison des leviers** (un levier A ou B, un levier 1, 2 ou 3) choisit la ligne, et un **repère de couleur** (■ ou □) choisit l'une des deux valeurs de la ligne.
:::

| Leviers | Colonne de gauche (tr/min) | Colonne de droite (tr/min) |
| --- | --- | --- |
| A / 1 | 50 | 128 |
| A / 2 | 240 | 92 |
| A / 3 | 68 | 180 |
| B / 1 | 910 | 352 |
| B / 2 | 653 | 1 700 |
| B / 3 | 1 280 | 490 |

Douze vaut 2 × 3 × 2 : deux positions du levier A / B, trois du levier 1 / 2 / 3, deux repères. Sur le schéma cinématique, trois baladeurs portent ces choix : un baladeur à trois positions (6, 7, 8) et deux à deux positions, soit 3 × 2 × 2 = 12 chaînes possibles.

::: exemple Ranger la gamme dans l'ordre croissant (plaque du manuel)
1. **Recopier** les douze valeurs, ligne après ligne : 50, 128, 240, 92, 68, 180, 910, 352, 653, 1 700, 1 280, 490.
2. **Trier** de la plus petite à la plus grande : 50, 68, 92, 128, 180, 240, 352, 490, 653, 910, 1 280, 1 700.
3. **Numéroter** : 50 est la 1ʳᵉ, 128 la 4ᵉ, 352 la 7ᵉ, 1 700 la 12ᵉ.
4. **Contrôler** : on retrouve bien douze valeurs, aucune n'a été oubliée ni comptée deux fois.

:::

::: piege L'ordre de lecture n'est pas l'ordre croissant
Lue ligne après ligne, la plaque donne 50, 128, 240, 92… : la suite monte, redescend, remonte. La **gamme croissante** demande de tout trier, colonnes comprises : la 2ᵉ vitesse n'est pas 128, c'est 68.
:::

::: verifie
Quel rang occupe 490 tr/min dans la gamme croissante des douze vitesses ?
---
Les valeurs plus petites que 490 sont 50, 68, 92, 128, 180, 240 et 352, soit sept : 490 est donc la **8ᵉ** vitesse.
:::

## 📏 Dents, module, entraxe : retrouver les roues d'une paire

Pour la paire de roues (7) et (16), le manuel donne le **module m = 3 mm**, l'**entraxe a = 87 mm** et le **rapport r = 12/17**. Il demande leurs nombres de dents et leurs diamètres, alors qu'aucun nombre de dents n'est donné dans l'énoncé.

Peut-on pourtant les retrouver ?

::: definition Diamètre primitif et entraxe
Pour deux roues cylindriques à denture droite de même module m (chapitre précédent), avec Z1 et Z2 dents :
- le **diamètre primitif** d'une roue est d = m × Z ;
- l'**entraxe** a est la distance entre les deux axes, égale à la **demi-somme** des diamètres : a = (d1 + d2) / 2 = m × (Z1 + Z2) / 2 ;
- le rapport vaut r = Z menante / Z menée.
:::

::: exemple Retrouver Z de la pièce (7) et de la pièce (16)
1. **La somme.** De a = m × (Z1 + Z2) / 2, on tire Z1 + Z2 = 2 × a / m = 2 × 87 / 3 = **58**.
2. **Le rapport.** r = 12/17 dit que Z1 et Z2 sont dans le rapport 12 pour 17 : Z1 = 12 k et Z2 = 17 k, où k est un entier.
3. **Résoudre.** 12 k + 17 k = 29 k = 58, donc k = 2 : Z1 = **24** et Z2 = **34**.
4. **Diamètres.** d1 = 3 × 24 = 72 mm et d2 = 3 × 34 = 102 mm. Contrôle : (72 + 102) / 2 = 87 mm.

La nomenclature donne bien Z7 = 24 et Z16 = 34.
:::

::: piege Le rapport ne donne pas les nombres de dents
r = 12/17 n'impose pas Z1 = 12 et Z2 = 17 : seul le **rapport** est fixé. C'est l'entraxe, par la somme Z1 + Z2, qui donne la taille de la paire. Et l'entraxe n'est pas la somme des diamètres, mais sa **moitié**.
:::

::: propriete Un entraxe fixe, une somme de dents fixe
Entre deux mêmes arbres, l'entraxe ne change pas quand le baladeur change de paire. À module égal, **toutes les paires possibles ont donc la même somme Z1 + Z2**. C'est le test pour savoir quelles roues peuvent s'engrener : pour l'étage de (7) et (16), les sommes valent 16 + 42 = 24 + 34 = 21 + 37 = 58. Une paire dont la somme diffère n'appartient pas à ce couple d'arbres.
:::

::: verifie
Deux roues de module 2 mm ont un entraxe de 50 mm et un rapport r = 2/3. Combien de dents chacune, et quels diamètres primitifs ?
---
Z1 + Z2 = 2 × 50 / 2 = 50. Avec Z1 = 2 k et Z2 = 3 k : 5 k = 50, donc k = 10 : **20 et 30 dents**. Les diamètres sont 2 × 20 = **40 mm** et 2 × 30 = **60 mm** (demi-somme : 50 mm).
:::

## ⛓️ Vitesses extrêmes : la chaîne cinématique mini et maxi

Le manuel demande le couple de roues en prise qui donne la **plus petite** vitesse de la broche, puis celui de la **plus grande**, avec r = N26 / Nm. Douze chaînes sont possibles.

Faut-il toutes les calculer pour trouver les deux extrêmes ?

::: definition Chaîne cinématique et rapport total
Une **chaîne cinématique** est la suite des paires en prise qui relie l'arbre moteur (5), de vitesse Nm, à la broche (26). Trois étages se suivent, et dans chacun le baladeur choisit une paire. Les rapports d'étage **se multiplient** :

$$ r = N26 / Nm = r1 × r2 × r3 $$
:::

::: figure Les trois étages de la boîte, de l'arbre moteur (5) à la broche (26). Chaque flèche est une paire que le baladeur peut mettre en prise, de la menante vers la menée, avec son rapport r. Un seul choix par étage : 3 × 2 × 2 = 12 vitesses. Schéma de principe
<svg viewBox="0 0 480 340"><title>Schéma de principe des trois étages de la boîte de vitesses de la fraiseuse, de l'arbre moteur à la broche</title><rect x="20" y="36" width="440" height="24" fill="#cbd5e1" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round"/><text x="240" y="52" font-size="11" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Broche (26)</text><rect x="20" y="126" width="440" height="24" fill="#cbd5e1" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round"/><text x="240" y="142" font-size="11" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Arbre intermédiaire cannelé (21)</text><rect x="20" y="216" width="440" height="24" fill="#cbd5e1" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round"/><text x="240" y="232" font-size="11" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Arbre intermédiaire (15)</text><rect x="20" y="306" width="440" height="24" fill="#cbd5e1" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round"/><text x="240" y="322" font-size="11" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Arbre moteur (5), vitesse Nm</text><line x1="90" y1="306" x2="90" y2="242" stroke="#0f172a" stroke-width="1.8" stroke-linecap="round"/><polygon points="93.5 249.2 90 242 86.5 249.2" fill="#0f172a" stroke="#0f172a" stroke-width="1" stroke-linejoin="round" stroke-linecap="round"/><text x="98" y="272" font-size="10.5" font-weight="700" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">6 → 17</text><text x="98" y="285" font-size="10.5" font-weight="500" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">r = 16/42</text><line x1="240" y1="306" x2="240" y2="242" stroke="#0f172a" stroke-width="1.8" stroke-linecap="round"/><polygon points="243.5 249.2 240 242 236.5 249.2" fill="#0f172a" stroke="#0f172a" stroke-width="1" stroke-linejoin="round" stroke-linecap="round"/><text x="248" y="272" font-size="10.5" font-weight="700" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">7 → 16</text><text x="248" y="285" font-size="10.5" font-weight="500" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">r = 24/34</text><line x1="390" y1="306" x2="390" y2="242" stroke="#0f172a" stroke-width="1.8" stroke-linecap="round"/><polygon points="393.5 249.2 390 242 386.5 249.2" fill="#0f172a" stroke="#0f172a" stroke-width="1" stroke-linejoin="round" stroke-linecap="round"/><text x="398" y="272" font-size="10.5" font-weight="700" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">8 → 13</text><text x="398" y="285" font-size="10.5" font-weight="500" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">r = 21/37</text><line x1="150" y1="216" x2="150" y2="152" stroke="#0f172a" stroke-width="1.8" stroke-linecap="round"/><polygon points="153.5 159.2 150 152 146.5 159.2" fill="#0f172a" stroke="#0f172a" stroke-width="1" stroke-linejoin="round" stroke-linecap="round"/><text x="158" y="182" font-size="10.5" font-weight="700" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">16 → 20</text><text x="158" y="195" font-size="10.5" font-weight="500" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">r = 34/34</text><line x1="330" y1="216" x2="330" y2="152" stroke="#0f172a" stroke-width="1.8" stroke-linecap="round"/><polygon points="333.5 159.2 330 152 326.5 159.2" fill="#0f172a" stroke="#0f172a" stroke-width="1" stroke-linejoin="round" stroke-linecap="round"/><text x="338" y="182" font-size="10.5" font-weight="700" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">14 → 23</text><text x="338" y="195" font-size="10.5" font-weight="500" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">r = 19/49</text><line x1="150" y1="126" x2="150" y2="62" stroke="#0f172a" stroke-width="1.8" stroke-linecap="round"/><polygon points="153.5 69.2 150 62 146.5 69.2" fill="#0f172a" stroke="#0f172a" stroke-width="1" stroke-linejoin="round" stroke-linecap="round"/><text x="158" y="92" font-size="10.5" font-weight="700" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">18 → 33</text><text x="158" y="105" font-size="10.5" font-weight="500" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">r = 56/34</text><line x1="330" y1="126" x2="330" y2="62" stroke="#0f172a" stroke-width="1.8" stroke-linecap="round"/><polygon points="333.5 69.2 330 62 326.5 69.2" fill="#0f172a" stroke="#0f172a" stroke-width="1" stroke-linejoin="round" stroke-linecap="round"/><text x="338" y="92" font-size="10.5" font-weight="700" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">19 → 31</text><text x="338" y="105" font-size="10.5" font-weight="500" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">r = 17/73</text></svg>
:::

Les nombres de dents viennent de la nomenclature. Les paires se retrouvent par la somme Z1 + Z2 de la section précédente : 58 pour l'étage 1, 68 pour l'étage 2, 90 pour l'étage 3.

::: exemple Les vitesses mini et maxi (Nm en illustration)
La plaque signalétique du moteur n'est pas reproduite : on prend **Nm = 1 450 tr/min** (valeur d'entraînement, courante pour un moteur à quatre pôles).
1. **Mini, étage par étage.** On garde dans chaque étage le plus petit rapport : 16/42 ≈ 0,381 (paire 6 → 17), puis 19/49 ≈ 0,388 (paire 14 → 23), puis 17/73 ≈ 0,233 (paire 19 → 31).
2. **Le produit.** r mini = 16 × 19 × 17 / (42 × 49 × 73) = 5 168 / 150 234 ≈ 0,0344, donc N26 mini = 1 450 × 0,0344 ≈ **49,9 tr/min**. La plaque porte 50 : l'accord est bon.
3. **Maxi, étage par étage.** On garde le plus grand rapport : 24/34 ≈ 0,706, puis 34/34 = 1, puis 56/34 ≈ 1,647.
4. **Le produit.** r maxi = 1 344 / 1 156 ≈ 1,163, donc N26 maxi = 1 450 × 1,163 ≈ **1 686 tr/min**. La plaque porte 1 700, à 1 % près.

:::

::: piege Le rapport inversé échange le mini et le maxi
Écrire r = Z menée / Z menante renverse chaque rapport : la chaîne « mini » devient la « maxi ». Le contrôle est immédiat : un pignon de 16 dents qui mène une roue de 42 ralentit, donc r est **inférieur à 1**.
:::

::: propriete Pour l'extrême, on choisit étage par étage
Les trois choix sont **libres** et tous les rapports sont positifs : un produit est le plus petit quand **chaque** facteur est le plus petit, le plus grand quand chacun est le plus grand. Il suffit donc de comparer les paires **dans chaque étage**, sans calculer les douze chaînes.
:::

::: verifie
Un étage offre deux paires : un pignon de 30 dents qui mène une roue de 60, ou un pignon de 45 qui mène une roue de 45. Laquelle donne la sortie la plus lente ?
---
30 / 60 = 0,5 et 45 / 45 = 1 : la première paire, de rapport **0,5**, est la plus lente. Les deux sommes valent 90, comme il se doit pour deux paires du même étage.
:::

## 🔋 Du moteur à la broche : puissance et couple

Une fois la vitesse de la broche connue, le manuel donne le rendement de la boîte, **η = 0,8**, et demande la puissance puis le couple en bout de broche aux deux vitesses extrêmes, C1 et C2.

Le couple est-il le même aux deux vitesses ?

::: definition Puissance à la broche et couple
La boîte perd une part de la puissance : P26 = η × Pm. Comme au tour, un couple C (N·m), une vitesse de rotation N (tr/min) et une puissance P (W) sont liés par :

$$ P = C × ω avec ω = 2π × N / 60 $$

Donc C = P / ω. À puissance donnée, le **couple est d'autant plus grand que la vitesse est basse**.
:::

::: exemple Les couples C1 et C2 (Pm en illustration)
La puissance Pm se lit sur la plaque du moteur, non reproduite : on prend **Pm = 3 kW**.
1. **Puissance à la broche.** P26 = 0,8 × 3 000 = **2 400 W**, la même aux deux vitesses.
2. **Vitesse mini.** ω1 = 2π × 49,9 / 60 ≈ 5,23 rad/s, donc C1 = 2 400 / 5,23 ≈ **459 N·m**.
3. **Vitesse maxi.** ω2 = 2π × 1 686 / 60 ≈ 176,6 rad/s, donc C2 = 2 400 / 176,6 ≈ **13,6 N·m**.
4. **Contrôle.** C1 / C2 ≈ 33,8, et N26 maxi / N26 mini = 1 686 / 49,9 ≈ 33,8 : le rapport des couples est l'inverse de celui des vitesses.

:::

::: piege La grande vitesse ne donne pas le grand couple
« Plus on tourne vite, plus la broche pousse fort » est faux : à puissance constante, le couple **baisse** quand la vitesse monte. C'est à la plus basse vitesse (50 tr/min) que la broche exerce le plus grand couple.
:::

::: verifie
Pm = 2 kW, η = 0,8, la broche tourne à 100 tr/min. Quel couple exerce-t-elle ?
---
P26 = 0,8 × 2 000 = 1 600 W ; ω = 2π × 100 / 60 ≈ 10,47 rad/s ; C = 1 600 / 10,47 ≈ **153 N·m**.
:::

## 🎯 Garder la vitesse choisie : la bille, le ressort et la vis de pression

On choisit une vitesse avec la poignée (48), puis on la lâche : la commande doit rester où on l'a mise, malgré les vibrations de la machine.

Comment une pièce que la main déplace sait-elle « s'arrêter » sur chaque position ?

::: definition L'indexage par bille et ressort
L'**indexage** maintient une commande dans l'une de ses **positions repérées**. Un ressort (45) pousse une bille (46) dans un **cran** de la pièce commandée. Pour changer de position, l'effort de la main repousse la bille hors du cran, puis elle retombe dans le cran suivant, ce qu'on sent comme un « clic ».
:::

Dans la solution d'origine, la bille est susceptible de s'éjecter, poussée par le ressort, au moment du montage ou du démontage. Le manuel demande de la modifier avec une **vis de pression** : elle facilite le montage et permet de régler la tension du ressort.

::: figure Le logement de la bille (46) et du ressort (45), sans puis avec vis de pression (51) ; à gauche, logement borgne d'origine ; La vis ferme le logement et règle la compression du ressort. Schéma de principe
<svg viewBox="0 0 480 212"><title>Logement de la bille et du ressort d'indexage, avec et sans vis de pression</title><rect x="20" y="20" width="100" height="100" fill="#cbd5e1" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><rect x="58" y="40" width="24" height="98" fill="#ffffff" stroke="#0f172a" stroke-width="1.4" stroke-linejoin="round"/><rect x="20" y="138" width="100" height="34" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><polygon points="58 138 70 150 82 138" fill="#ffffff" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round"/><circle cx="70" cy="130" r="9" fill="#bbf7d0" stroke="#0f172a" stroke-width="1.8"/><polyline points="70 40 70 46.8 76 50.1 64 56.9 76 63.6 64 70.4 76 77.1 64 83.9 76 90.6 64 97.4 76 104.1 64 110.9 70 114.2 70 121" fill="none" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round" stroke-linecap="round"/><text x="70" y="192" font-size="10.5" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Perçage borgne : la bille</text><text x="70" y="205" font-size="10.5" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">peut sauter au montage</text><rect x="270" y="20" width="100" height="100" fill="#cbd5e1" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><rect x="308" y="20" width="24" height="118" fill="#ffffff" stroke="#0f172a" stroke-width="1.4" stroke-linejoin="round"/><rect x="270" y="138" width="100" height="34" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><polygon points="308 138 320 150 332 138" fill="#ffffff" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round"/><circle cx="320" cy="130" r="9" fill="#bbf7d0" stroke="#0f172a" stroke-width="1.8"/><polyline points="320 40 320 46.8 326 50.1 314 56.9 326 63.6 314 70.4 326 77.1 314 83.9 326 90.6 314 97.4 326 104.1 314 110.9 320 114.2 320 121" fill="none" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round" stroke-linecap="round"/><rect x="306" y="22" width="28" height="16" fill="#fdba74" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><line x1="310" y1="22" x2="310" y2="38" stroke="#0f172a" stroke-width="1" stroke-linecap="round"/><line x1="316" y1="22" x2="316" y2="38" stroke="#0f172a" stroke-width="1" stroke-linecap="round"/><line x1="324" y1="22" x2="324" y2="38" stroke="#0f172a" stroke-width="1" stroke-linecap="round"/><line x1="330" y1="22" x2="330" y2="38" stroke="#0f172a" stroke-width="1" stroke-linecap="round"/><text x="320" y="192" font-size="10.5" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Vis de pression : logement</text><text x="320" y="205" font-size="10.5" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">fermé, tension réglable</text><line x1="79" y1="130" x2="128" y2="130" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round"/><text x="132" y="133" font-size="9.5" font-weight="500" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">bille (46)</text><line x1="72" y1="66" x2="128" y2="66" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round"/><text x="132" y="69" font-size="9.5" font-weight="500" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">ressort (45)</text><line x1="102" y1="160" x2="128" y2="160" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round"/><text x="132" y="163" font-size="9.5" font-weight="500" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">pièce commandée</text><line x1="320" y1="30" x2="372" y2="30" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round"/><text x="376" y="33" font-size="9.5" font-weight="500" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">vis de pression (51)</text></svg>
:::

::: exemple Ce que change la vis de pression (principe)
1. **Elle ferme le logement.** Une fois en place, la bille et le ressort ne peuvent plus sauter : le montage devient sûr.
2. **Elle règle la tension.** La visser davantage comprime le ressort : il pousse plus fort la bille, donc il faut plus d'effort pour sortir du cran. La dévisser fait l'inverse.
3. **Elle se monte en dernier.** On met la bille, puis le ressort, **puis** la vis de pression, qui ferme le logement et fixe la tension (ordre du graphe de montage, ou râteau, des chapitres sur le dessin d'ensemble).

:::

::: piege Plus de tension n'est pas toujours mieux
Visser la vis à fond rend la commande dure à manœuvrer ; la visser trop peu laisse la vitesse choisie se dérégler sous les vibrations. Le bon réglage est celui qui tient la position tout en laissant la main changer de cran.
:::

::: verifie
Quel est le double rôle de la vis de pression sur le logement de la bille ?
---
Elle **ferme le logement**, donc la bille ne s'éjecte plus au montage, et elle **règle la tension du ressort** : plus elle est vissée, plus le ressort est comprimé.
:::

## 🔩 La vis d'entraînement : pas, filets et course de la table

Pendant le fraisage, la pièce fixée sur la table avance : c'est le **mouvement d'avance**. Il se fait suivant trois axes (avance **longitudinale**, **transversale**, **verticale**), chacun en commande **manuelle** (volant) ou **automatique** (boîte d'avances), lente en phase de coupe, rapide pour l'approche à vide ou le dégagement de l'outil. Le manuel étudie la table longitudinale : on tourne le volant de n tours et on mesure la course C de la table.

Quel lien y a-t-il entre C, n et la vis d'entraînement (11) ?

::: definition Pas, filets, course
Le **pas** p d'une vis est la distance, mesurée le long de l'axe, entre deux crêtes voisines du filet. Une vis peut avoir un ou plusieurs **filets**, leur nombre est k. En un tour, la table avance de **k × p**. Pour n tours, la **course** est :

$$ C = n × k × p $$
:::

::: figure Deux vis vues de côté : les traits sont les crêtes du filet. À un filet, deux crêtes voisines sont séparées de p et l'écrou, donc la table, avance de p par tour. À deux filets (bleu et orange), deux crêtes voisines sont toujours séparées de p, mais chaque filet ne revient que tous les 2 p : l'écrou, donc la table, avance de 2 p par tour
<svg viewBox="0 0 340 236"><title>Vis à un filet et vis à deux filets vues de côté, avec le pas p entre deux crêtes voisines</title><rect x="20" y="40" width="300" height="50" fill="#f1f5f9" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><line x1="34" y1="90" x2="48" y2="40" stroke="#1d4ed8" stroke-width="3.2" stroke-linecap="round"/><line x1="64" y1="90" x2="78" y2="40" stroke="#1d4ed8" stroke-width="3.2" stroke-linecap="round"/><line x1="94" y1="90" x2="108" y2="40" stroke="#1d4ed8" stroke-width="3.2" stroke-linecap="round"/><line x1="124" y1="90" x2="138" y2="40" stroke="#1d4ed8" stroke-width="3.2" stroke-linecap="round"/><line x1="154" y1="90" x2="168" y2="40" stroke="#1d4ed8" stroke-width="3.2" stroke-linecap="round"/><line x1="184" y1="90" x2="198" y2="40" stroke="#1d4ed8" stroke-width="3.2" stroke-linecap="round"/><line x1="214" y1="90" x2="228" y2="40" stroke="#1d4ed8" stroke-width="3.2" stroke-linecap="round"/><line x1="244" y1="90" x2="258" y2="40" stroke="#1d4ed8" stroke-width="3.2" stroke-linecap="round"/><line x1="274" y1="90" x2="288" y2="40" stroke="#1d4ed8" stroke-width="3.2" stroke-linecap="round"/><line x1="123" y1="26" x2="108" y2="26" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><polygon points="115.2 22.5 108 26 115.2 29.5" fill="#0f172a" stroke="#0f172a" stroke-width="1" stroke-linejoin="round" stroke-linecap="round"/><line x1="123" y1="26" x2="138" y2="26" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><polygon points="130.8 29.5 138 26 130.8 22.5" fill="#0f172a" stroke="#0f172a" stroke-width="1" stroke-linejoin="round" stroke-linecap="round"/><line x1="108" y1="22" x2="108" y2="38" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round"/><line x1="138" y1="22" x2="138" y2="38" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round"/><text x="123" y="18" font-size="10" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">pas p</text><text x="330" y="24" font-size="9" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"></text><text x="170" y="112" font-size="10.5" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1 filet : un tour avance l'écrou de 1 pas</text><rect x="20" y="150" width="300" height="50" fill="#f1f5f9" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><line x1="34" y1="200" x2="48" y2="150" stroke="#1d4ed8" stroke-width="3.2" stroke-linecap="round"/><line x1="64" y1="200" x2="78" y2="150" stroke="#ea580c" stroke-width="3.2" stroke-linecap="round"/><line x1="94" y1="200" x2="108" y2="150" stroke="#1d4ed8" stroke-width="3.2" stroke-linecap="round"/><line x1="124" y1="200" x2="138" y2="150" stroke="#ea580c" stroke-width="3.2" stroke-linecap="round"/><line x1="154" y1="200" x2="168" y2="150" stroke="#1d4ed8" stroke-width="3.2" stroke-linecap="round"/><line x1="184" y1="200" x2="198" y2="150" stroke="#ea580c" stroke-width="3.2" stroke-linecap="round"/><line x1="214" y1="200" x2="228" y2="150" stroke="#1d4ed8" stroke-width="3.2" stroke-linecap="round"/><line x1="244" y1="200" x2="258" y2="150" stroke="#ea580c" stroke-width="3.2" stroke-linecap="round"/><line x1="274" y1="200" x2="288" y2="150" stroke="#1d4ed8" stroke-width="3.2" stroke-linecap="round"/><line x1="123" y1="136" x2="108" y2="136" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><polygon points="115.2 132.5 108 136 115.2 139.5" fill="#0f172a" stroke="#0f172a" stroke-width="1" stroke-linejoin="round" stroke-linecap="round"/><line x1="123" y1="136" x2="138" y2="136" stroke="#0f172a" stroke-width="1.4" stroke-linecap="round"/><polygon points="130.8 139.5 138 136 130.8 132.5" fill="#0f172a" stroke="#0f172a" stroke-width="1" stroke-linejoin="round" stroke-linecap="round"/><line x1="108" y1="132" x2="108" y2="148" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round"/><line x1="138" y1="132" x2="138" y2="148" stroke="#0f172a" stroke-width="1.0" stroke-linecap="round"/><text x="123" y="128" font-size="10" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">pas p</text><text x="170" y="222" font-size="10.5" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2 filets : un tour avance l'écrou de 2 pas</text></svg>
:::

::: exemple Du volant à la vitesse de la vis (valeurs d'illustration)
Le pas de la vis (11) se mesure sur la machine : on prend ici p = 6 mm.
1. **Mesurer C / n.** Pour n = 1, 2, 3 tours, on lit C = 6, 12 et 18 mm : C / n = 6 mm, égal au pas.
2. **Conclure sur les filets.** C / n = k × p donne k = 6 / 6 = 1 : la vis a **un filet**. Sur une autre vis de pas 4 mm, C / n = 8 mm donnerait k = 8 / 4 = 2 filets.
3. **Vitesse d'avance.** La table parcourt C = 0,30 m en t = 1 min : V = C / t = 0,30 m/min, soit **300 mm/min**.
4. **Vitesse de la vis.** Un tour avance la table de k × p = 6 mm, donc N11 = V / (k × p) = 300 / 6 = **50 tr/min**.

:::

::: piege Avec plusieurs filets, la course n'est pas n × p
Sur une vis à deux filets de pas 4 mm, la table avance de 8 mm par tour, pas de 4 : oublier k donne une course deux fois trop courte. Les deux grandeurs C / n et p ne coïncident que pour **un** filet, et c'est justement ce qui permet de compter les filets. Et en vitesse, le facteur 1 000 convertit les mètres en millimètres : 0,30 m/min = 300 mm/min.
:::

::: verifie
Une vis à 3 filets a un pas de 2 mm. Quelle est la course de la table pour 5 tours du volant ?
---
Un tour avance la table de 3 × 2 = 6 mm, donc 5 tours donnent C = 5 × 6 = **30 mm**.
:::

## 🔒 Irréversible mais pas sans jeu : l'inversion et le rattrapage

Poussez la table à la main : la vis ne tourne pas. Tournez le volant dans un sens, puis dans l'autre : la table, elle, ne repart pas tout de suite.

Deux observations, deux propriétés du vis-écrou : laquelle protège la machine, laquelle dégrade la précision ?

::: definition Réversible, irréversible, et le jeu
Une transformation de mouvement est **réversible** si la translation peut à son tour faire tourner la vis, **irréversible** sinon. Une vis-écrou à filet trapézoïdal usuel, à faible angle d'hélice, est généralement **irréversible** : le frottement dans le filet l'emporte sur la poussée. Pour une machine-outil, c'est voulu : les efforts de coupe poussent sur la table sans pouvoir la faire reculer en tournant la vis, donc la table garde sa position.

Le **jeu** est l'espace entre le filet de la vis et celui de l'écrou : le contact ne se fait que d'un côté. À l'**inversion** du sens de rotation, la vis tourne d'abord à vide sur ce jeu avant que la table ne bouge : le cadran gradué indique un déplacement que la table n'a pas fait.
:::

::: figure Le filet d'une vis (bleu) et la dent d'un écrou (orange), en coupe, avec un jeu dessiné exagéré. En 1 et en 3, la dent touche un flanc puis l'autre ; en 2, entre les deux, aucun flanc ne pousse. En 4, deux écrous, chacun appuyé sur un flanc opposé, suppriment le jeu
<svg viewBox="0 0 470 350"><title>Contact entre le filet d'une vis et la dent d'un écrou : jeu, inversion et rattrapage par deux écrous</title><g transform="translate(0 0)"><polygon points="18 112 30 80 50 80 62 112" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round"/><polygon points="78 112 90 80 110 80 122 112" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round"/><rect x="0" y="112" width="140" height="14" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><polygon points="38.8 52 93.2 52 72.4 104 59.6 104" fill="#fdba74" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round"/><rect x="18" y="34" width="128" height="18" fill="#fdba74" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><text x="95" y="150" font-size="9.5" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1. Sens 1 : le flanc de gauche pousse</text><text x="160" y="46" font-size="9.5" font-weight="700" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">écrou</text><text x="160" y="126" font-size="9.5" font-weight="700" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">vis</text></g><g transform="translate(0 0)"><polygon points="248 112 260 80 280 80 292 112" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round"/><polygon points="308 112 320 80 340 80 352 112" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round"/><rect x="230" y="112" width="140" height="14" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><polygon points="272.8 52 327.2 52 306.4 104 293.6 104" fill="#fdba74" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round"/><rect x="248" y="34" width="128" height="18" fill="#fdba74" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><text x="325" y="150" font-size="9.5" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2. À l'inversion : la vis tourne à vide</text></g><g transform="translate(0 170)"><polygon points="18 112 30 80 50 80 62 112" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round"/><polygon points="78 112 90 80 110 80 122 112" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round"/><rect x="0" y="112" width="140" height="14" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><polygon points="46.8 52 101.2 52 80.4 104 67.6 104" fill="#fdba74" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round"/><rect x="18" y="34" width="128" height="18" fill="#fdba74" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><text x="95" y="150" font-size="9.5" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">3. Sens 2 : le flanc de droite pousse</text></g><g transform="translate(0 170)"><polygon points="238 112 250 80 270 80 282 112" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round"/><polygon points="298 112 310 80 330 80 342 112" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round"/><polygon points="358 112 370 80 390 80 402 112" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round"/><rect x="220" y="112" width="200" height="14" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><polygon points="258.8 52 313.2 52 292.4 104 279.6 104" fill="#fdba74" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round"/><polygon points="326.8 52 381.2 52 360.4 104 347.6 104" fill="#fde68a" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round" stroke-linecap="round"/><rect x="236" y="34" width="90" height="18" fill="#fdba74" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><rect x="334" y="34" width="90" height="18" fill="#fde68a" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><text x="282" y="26" font-size="9.5" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">écrou fixe</text><text x="379" y="26" font-size="9.5" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">écrou réglable</text><text x="315" y="150" font-size="9.5" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4. Deux écrous : les deux flancs</text><text x="315" y="162" font-size="9.5" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">sont en contact, plus de jeu</text></g></svg>
:::

Le remède est le **rattrapage de jeu**. Le manuel montre un système à **écrou** et **écrou réglable** : le réglage force les deux écrous à s'appuyer sur des flancs opposés, comme en 4.

::: exemple Rattraper le jeu (principe, les repères ne sont pas transcrits)
1. **Desserrer le blocage** de l'écrou réglable (une vis de pression ou de blocage, à repérer sur le dessin d'ensemble et la nomenclature).
2. **Déplacer l'écrou réglable** jusqu'à ce que les deux flancs soient en contact : le jeu disparaît.
3. **Rebloquer** l'écrou réglable, pour que le réglage ne bouge plus.
4. **Contrôler** en tournant le volant dans les deux sens : la table doit suivre sans à-coup à l'inversion, et sans dureté excessive.

:::

::: piege Le jeu rattrapé n'est pas le jeu oublié
Serrer à l'excès supprime le jeu mais rend le volant dur et accélère l'usure : l'étape 4 sert à le vérifier. Et même bien réglé, un système garde un peu de jeu : pour atteindre une cote précise, on arrive toujours **dans le même sens**, et si on dépasse, on recule de plus que le jeu avant de repartir.
:::

::: verifie
Pourquoi la table ne bouge-t-elle pas tout de suite quand on inverse le sens de rotation du volant ?
---
À l'inversion, la vis doit d'abord traverser le **jeu** entre ses filets et ceux de l'écrou : tant qu'aucun flanc ne pousse l'écrou, la table reste immobile.
:::

## 🧭 La méthode qui reste : six marches

Devant une fraiseuse inconnue, tu reprends toujours cet ordre :

1. **Classer** les pièces du frein : tournante, glissante ou fixe, en s'appuyant sur la classe A du bâti ; une commande électrique, des ressorts qui serrent et une bobine qui desserre.
2. **Calculer le frein** : Cf = n × f × Fp × Rm, des rayons et un Cf dans les mêmes unités ; on divise Fp par le nombre de ressorts à la fin.
3. **Lire la plaque** : douze vitesses, 2 × 3 × 2, à trier pour la gamme croissante.
4. **Retrouver les paires** : entraxe fixe, somme Z1 + Z2 constante ; puis, étage par étage, le plus petit rapport pour le mini, le plus grand pour le maxi ; C = P / ω avec P26 = η × Pm.
5. **Indexer** : un ressort, une bille, un cran ; la vis de pression ferme et règle.
6. **Avancer** : C = n × k × p, V = C / t, N11 = V / (k × p) ; vis-écrou irréversible, jeu à l'inversion rattrapé par un second écrou.

::: retenir
Le frein de la fraiseuse **serre par ressorts** et se **desserre par la bobine**, avec **Cf = n × f × Fp × Rm** ; la boîte offre **douze vitesses** (3 × 2 × 2), ses paires partagent la **même somme de dents** et les extrêmes se trouvent **étage par étage** ; la table avance de **k × p** par tour d'une vis **irréversible**, dont le **jeu** se rattrape par un second écrou.
:::

> 🏆 La fraiseuse n'a plus de secret : tu sais l'arrêter, la régler et la faire avancer. La suite du thème t'attend, avec d'autres mécanismes.
