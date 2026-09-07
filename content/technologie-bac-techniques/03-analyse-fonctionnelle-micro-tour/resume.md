# 📜 Résumé : Le micro-tour et la loi des deux chaînes

- **Le micro-tour** : machine-outil à **commande numérique**, pilotée par un ordinateur qui lit et traite le **G-code** ; le fichier d'usinage est créé par un **logiciel de F.A.O.** La pièce est serrée par les **mors** du **mandrin (8)** monté sur la **broche (11)** ; l'outil est serré dans la **tourelle porte-outil (5)** ; le **traînard (31)** avance suivant **Z**, le **chariot porte-outil (7)** suivant **X** ; la **poupée mobile (1)** perce et alèse en bout de pièce.
- **Om et Op** : l'**origine machine Om** est la position de la machine **en butée** (fixée par construction) ; l'**origine pièce Op** est **définie par l'opérateur**.
- **Système automatisé** : ensemble d'éléments qui exécutent des **tâches programmées** sans intervention de l'homme. On le décrit par **deux chaînes**.
- **Chaîne d'information** — capte et traite l'information : **Acquérir** (les capteurs) → **Traiter** (la partie commande : automate ou microcontrôleur) → **Communiquer** (l'interface avec l'utilisateur et l'environnement). Entrées : consigne de l'utilisateur, informations extérieures. Sorties : information pour l'utilisateur, **ordres pour la chaîne d'énergie**.
- **Chaîne d'énergie** — réalise l'action : **Alimenter** (mise en forme de l'énergie externe) → **Distribuer** (distributeur, contacteur, carte de puissance) → **Convertir** (l'**actionneur** : moteur, vérin) → **Transmettre** (les organes de transmission de mouvement et d'effort). Les **ordres** entrent sur **Distribuer** ; la sortie parasite est celle des **Pertes**.

::: figure Les deux chaînes à retenir par cœur, et l'unique flèche qui descend de l'une à l'autre
<svg viewBox="0 0 440 200">
<g fill="#0f6e56" opacity="0.12"><rect x="76" y="30" width="86" height="40" rx="5"/><rect x="178" y="30" width="86" height="40" rx="5"/><rect x="280" y="30" width="86" height="40" rx="5"/></g>
<g fill="none" stroke="#0f172a" stroke-width="2"><rect x="76" y="30" width="86" height="40" rx="5"/><rect x="178" y="30" width="86" height="40" rx="5"/><rect x="280" y="30" width="86" height="40" rx="5"/></g>
<g fill="none" stroke="#0f172a" stroke-width="2"><path d="M162 50 H170"/><path d="M264 50 H272"/></g>
<g fill="#0f172a"><path d="M170 45 L178 50 L170 55 Z"/><path d="M272 45 L280 50 L272 55 Z"/></g>
<g fill="#0f6e56" opacity="0.12"><rect x="26" y="140" width="86" height="40" rx="5"/><rect x="128" y="140" width="86" height="40" rx="5"/><rect x="230" y="140" width="86" height="40" rx="5"/><rect x="332" y="140" width="86" height="40" rx="5"/></g>
<g fill="none" stroke="#0f172a" stroke-width="2"><rect x="26" y="140" width="86" height="40" rx="5"/><rect x="128" y="140" width="86" height="40" rx="5"/><rect x="230" y="140" width="86" height="40" rx="5"/><rect x="332" y="140" width="86" height="40" rx="5"/></g>
<g fill="none" stroke="#0f172a" stroke-width="2"><path d="M112 160 H120"/><path d="M214 160 H222"/><path d="M316 160 H324"/></g>
<g fill="#0f172a"><path d="M120 155 L128 160 L120 165 Z"/><path d="M222 155 L230 160 L222 165 Z"/><path d="M324 155 L332 160 L324 165 Z"/></g>
<path d="M221 70 V104 H171 V132" fill="none" stroke="#0f6e56" stroke-width="2.5"/>
<path d="M166 132 L171 140 L176 132 Z" fill="#0f6e56"/>
<g font-size="12" font-weight="700" fill="#0f172a" text-anchor="middle">
<text x="119" y="55">Acquérir</text><text x="221" y="55">Traiter</text><text x="323" y="55">Communiquer</text>
<text x="69" y="165">Alimenter</text><text x="171" y="165">Distribuer</text><text x="273" y="165">Convertir</text><text x="375" y="165">Transmettre</text>
</g>
<text x="229" y="98" font-size="11" font-weight="700" fill="#0f6e56" text-anchor="start">Ordres</text>
</svg>
:::

- **Les deux chaînes du micro-tour** : **boutons poussoirs** → Acquérir (l'**encodeur (16)**, capteur, y appartient aussi), **microcontrôleur** → Traiter, **écran** → Communiquer ; **unité d'alimentation** → Alimenter, **carte de puissance** → Distribuer, **moteurs pas à pas (38) et moteur électrique (21)** → Convertir, **éléments de transmission** → Transmettre. L'énergie est **électrique** jusqu'à l'actionneur, **mécanique** après lui : EE, EE, EM, EM.
- **Le F.A.S.T.** : méthode de l'**analyse fonctionnelle interne** — chercher les fonctions techniques, les solutions constructives et les composants qui satisfont chaque fonction de service. Trois colonnes : **fonction de service** → **fonctions techniques** → **solutions technologiques**. Vers la droite on répond à **« Comment ? »**, vers la gauche à **« Pourquoi ? »**, verticalement à **« Quand ? »**. Opérateur **ET** = solutions nécessaires ensemble ; opérateur **OU** = branches alternatives.
- **FP1 du micro-tour** : fixer la pièce (mandrin et mors) · fixer l'outil (tourelle et vis) · alimenter (unité d'alimentation) · commander (ordinateur et microcontrôleur) · déplacer l'outil selon X et Z · animer la pièce en rotation · sécuriser (**carter** et **bouton d'arrêt d'urgence**).
- **La chaîne de l'axe Z** : **moteur pas à pas (38)** → **accouplement (37)** → **vis mère (26)** tournant dans son **palier (45)** à **butées à billes (44)** → **écrou (25)** → **traînard (31)**, guidé par le **banc (22)**.
- **Les quatre liaisons** : **encastrement** (aucun mouvement — l'écrou sur le traînard, le mandrin sur la broche) · **pivot** (rotation seule — la vis dans son palier, la broche sur ses roulements) · **glissière** (translation seule — le traînard sur le banc) · **hélicoïdale** (rotation **couplée** à une translation — la vis et l'écrou).
- **Le schéma cinématique** : le mécanisme réduit à ses **seules liaisons** — chaque pièce devient un trait, le **bâti** se reconnaît à ses **hachures** —, et chaque liaison y porte la **fonction technique** qu'elle satisfait : l'accouplement (37) → **FT512111**, le pivot de la vis dans son palier → **FT512112**, l'hélicoïdale vis-écrou → **FT5121**, l'encastrement écrou/traînard → **FT512121**, la glissière du traînard sur le banc → **FT513**.
- **La chaîne FT6** : **moteur électrique (21)** → **poulies-courroie** (poulie motrice (20), courroie crantée (19), poulie réceptrice (13)) → **clavette parallèle (15)** → **broche (11)** guidée par **deux roulements à rouleaux coniques (10)** → **mandrin (8)** encastré par **trois goujons M8×28 (52)**.
