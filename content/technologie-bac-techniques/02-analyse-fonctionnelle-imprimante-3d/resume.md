# 📜 Résumé : Dans les entrailles de l'imprimante 3D

- **Le procédé FDM.** Une **cartouche chauffante** fond le filament, la **buse** en **calibre** la section, la matière est déposée **couche par couche** sur le **plateau porte-pièce** (chauffé, il améliore l'**adhésion**), et le plateau **descend** d'une couche entre chaque passage. Le **galet cranté** et le **galet presseur** avancent le fil **par adhérence** ; la **thermistance** surveille la température ; le **ventilateur** et le **dissipateur** refroidissent la tête.
- **Trois axes, trois solutions.** La **tête** se déplace suivant **X** et **Y** (moteur + **système poulies-courroie**, guidage par **douilles à billes** sur **colonnes rectifiées**) ; le **plateau mobile** se déplace suivant **Z** (moteur → poulies-courroies → **tiges filetées T8** → **trois écrous T8** solidaires du plateau). Retiens la différence : **transmettre** conserve la nature du mouvement, **transformer** la change — et **c'est le montage qui décide** : la même courroie **transmet** sur Z (vers les tiges filetées) et **transforme** sur X (elle est fixée sur la tête).
- **Le système automatisé.** Plusieurs éléments exécutant des **tâches programmées** **sans intervention de l'homme**. Il se décompose en **deux chaînes fonctionnelles** : la chaîne d'information envoie des **ordres** à la chaîne d'énergie, sur le bloc **Distribuer**.

::: figure L'architecture complète en une image : trois blocs qui savent, quatre blocs qui agissent, et les ordres qui descendent de l'une à l'autre — sur Distribuer
<svg viewBox="0 0 380 182">
<g font-size="11" font-weight="700" fill="#0f172a">
<text x="14" y="20">chaîne d'information</text>
<text x="14" y="120">chaîne d'énergie</text>
</g>
<g fill="#0f6e56" fill-opacity="0.12" stroke="#0f172a" stroke-width="2">
<rect x="14" y="32" width="76" height="36"/>
<rect x="106" y="32" width="76" height="36"/>
<rect x="198" y="32" width="76" height="36"/>
</g>
<g fill="#0f6e56" fill-opacity="0.12" stroke="#0f172a" stroke-width="2">
<rect x="14" y="132" width="76" height="36"/>
<rect x="106" y="132" width="76" height="36"/>
<rect x="198" y="132" width="76" height="36"/>
<rect x="290" y="132" width="76" height="36"/>
</g>
<g stroke="#0f172a" stroke-width="2" fill="#0f172a">
<path d="M90 50 H100"/><path d="M96 46 L106 50 L96 54 Z"/>
<path d="M182 50 H192"/><path d="M188 46 L198 50 L188 54 Z"/>
<path d="M90 150 H100"/><path d="M96 146 L106 150 L96 154 Z"/>
<path d="M182 150 H192"/><path d="M188 146 L198 150 L188 154 Z"/>
<path d="M274 150 H284"/><path d="M280 146 L290 150 L280 154 Z"/>
</g>
<g fill="none" stroke="#0f6e56" stroke-width="2"><path d="M236 68 V96 H144 V126"/></g>
<path d="M140 120 L144 130 L148 120 Z" fill="#0f6e56"/>
<g font-size="10" font-weight="700" fill="#0f172a" text-anchor="middle">
<text x="52" y="54">Acquérir</text><text x="144" y="54">Traiter</text><text x="236" y="54">Communiquer</text>
<text x="52" y="154">Alimenter</text><text x="144" y="154">Distribuer</text><text x="236" y="154">Convertir</text><text x="328" y="154">Transmettre</text>
</g>
<text x="190" y="90" font-size="10" font-weight="700" fill="#0f6e56" text-anchor="middle" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">ordres</text>
</svg>
:::

- **La chaîne d'information : Acquérir → Traiter → Communiquer.** Elle **capte** l'information et la **traite**. **Acquérir** = prélever des informations par des **capteurs** ; **Traiter** = la **partie commande** (automate ou microcontrôleur) ; **Communiquer** = l'**interface** avec l'utilisateur et les autres systèmes. Sur l'imprimante : **capteurs fin de course** et **thermistance** → **carte électronique** → **fils de liaison** et **afficheur**, l'entrée étant le programme **G-code**.
- **La chaîne d'énergie : Alimenter → Distribuer → Convertir → Transmettre.** C'est l'ensemble des procédés qui **réalisent l'action**. **Alimenter** met en forme l'énergie externe (**bloc d'alimentation** : 220 V AC → 24 V DC), **Distribuer** l'envoie à l'actionneur (**contrôleur de moteur pas à pas**), **Convertir** est l'**actionneur** (**moteur pas à pas**), **Transmettre** regroupe les **organes mécaniques** (poulies, courroies, vis-écrou). Natures d'énergie : **EE, EE, EM, EM** — l'énergie ne change de nature qu'à **Convertir**, et une **branche de chauffe** convertit en plus l'électrique en **thermique** (résistance chauffante). Chaque bloc génère des **pertes**.
- **Le cahier des charges fonctionnel.** Chaque fonction de service porte une **expression**, des **critères d'appréciation** et des **niveaux assortis d'une flexibilité** (la tolérance). **FP** = raison d'être (impression 200×200×200 mm ±5 mm, précision 0,2 mm ±0,1 mm) ; **FC** = contraintes du milieu extérieur (filament Ø 1,75 mm ±0,05 mm ; 220 V AC et 24 V DC ; G-code par USB ou carte Micro-SD ; 7 kg ±50 g sur 3 points d'appui minimum).
- **Le diagramme F.A.S.T.** Trois colonnes — **fonction de service**, **fonctions techniques**, **solutions technologiques** — et trois questions clés : **Comment ?** (vers la droite), **Pourquoi ?** (vers la gauche), **Quand ?** Deux opérateurs relient les branches : **ET** (les solutions se cumulent) et **OU** (elles s'excluent). Sur chaque axe, l'arbre suit la même grammaire — **convertir → (transmettre si besoin) → transformer → guider**, l'ordre des lignes suivant le montage : l'étape *transmettre* n'apparaît **que là où la rotation doit voyager**, comme sur l'axe Z (courroie du moteur vers les deux tiges filetées).
