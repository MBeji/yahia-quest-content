# ⚙️ La maquette du moteur à explosion : du piston à la vitesse choisie

> 💡 «Un moteur qui brûle du carburant ne sait que pousser un piston, une fois sur quatre. Tout le reste, la bielle, le volant, l'embrayage, la boîte, sert à transformer cette poussée en une rotation que les roues peuvent suivre.»

Ce chapitre poursuit le thème « Transmission de puissance » avec la **maquette d'un moteur à explosion** : un moteur à quatre cylindres, son **embrayage**, sa **boîte de vitesses** à cinq vitesses et marche arrière, et le **synchroniseur** de cette boîte. On y reprend les notations des chapitres précédents : **r** pour le rapport de transmission, **N** pour une vitesse de rotation en tr/min, **Ct** et **f** pour l'embrayage.

> 🗡️ Le manuel ne donne **aucun corrigé**, et son dessin d'ensemble n'est pas reproduit ici. Les schémas sont donc des **schémas de principe**, redessinés pour expliquer. Quand un nombre vient du manuel (diamètre de piston 85 mm, N1 = 1 600 tr/min, nombres de dents de la nomenclature), le texte le dit ; quand c'est une **valeur d'entraînement** (rayon de vilebrequin, dents des roues à compter sur la maquette), il le dit aussi : avec tes mesures, tu refais le calcul.

## 🔥 Les quatre temps : un seul travaille

Tu fais tourner le vilebrequin de la maquette à la manivelle : le piston monte, descend, monte, descend. Mais le moteur d'une voiture ne « pousse » pas à chaque va-et-vient.

Combien de ces mouvements servent réellement à produire de l'énergie ?

::: definition Moteur thermique à combustion interne, cycle à quatre temps
Un **moteur thermique à combustion interne** brûle un mélange de **carburant et de comburant** (l'air) **dans** le cylindre et transforme l'énergie thermique de cette combustion en énergie mécanique. Le **cycle** est l'ensemble des phases qui se succèdent : ici **quatre temps**, chacun correspondant à **une course** du piston, c'est-à-dire un trajet entre ses deux positions extrêmes. Le seul temps qui fournit de l'énergie est le **temps moteur** ; les trois autres sont **résistants**.
:::

::: figure Les quatre temps, de gauche à droite, avec la soupape d'admission à gauche et celle d'échappement à droite de chaque cylindre. La flèche rouge donne le sens du piston. Schéma de principe
<svg viewBox="0 0 460 190"><title>Les quatre temps du cycle : admission, compression, explosion-détente, échappement</title><rect x="34" y="36" width="48" height="48" fill="#dbeafe" stroke="#0f172a" stroke-width="0" stroke-linejoin="round"/><line x1="34" y1="36" x2="34" y2="142" stroke="#0f172a" stroke-width="2.5" stroke-linecap="round"/><line x1="82" y1="36" x2="82" y2="142" stroke="#0f172a" stroke-width="2.5" stroke-linecap="round"/><rect x="31" y="28" width="54" height="8" fill="#94a3b8" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><line x1="45" y1="20" x2="45" y2="45" stroke="#0f172a" stroke-width="2" stroke-linecap="round"/><rect x="38" y="45" width="14" height="3.5" fill="#334155" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round"/><line x1="71" y1="20" x2="71" y2="38" stroke="#0f172a" stroke-width="2" stroke-linecap="round"/><rect x="64" y="38" width="14" height="3.5" fill="#334155" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round"/><line x1="58" y1="20" x2="58" y2="36" stroke="#64748b" stroke-width="3" stroke-linecap="round"/><rect x="36" y="84" width="44" height="14" fill="#94a3b8" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><line x1="58" y1="98" x2="58" y2="150" stroke="#0f172a" stroke-width="3" stroke-linecap="round"/><line x1="58" y1="52" x2="58" y2="71" stroke="#dc2626" stroke-width="2.5" stroke-linecap="round"/><polygon points="58,78 54.9,71 61.1,71" fill="#dc2626"/><text x="58" y="170" font-size="12" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">1. Admission</text><rect x="149" y="36" width="48" height="48" fill="#fde68a" stroke="#0f172a" stroke-width="0" stroke-linejoin="round"/><line x1="149" y1="36" x2="149" y2="142" stroke="#0f172a" stroke-width="2.5" stroke-linecap="round"/><line x1="197" y1="36" x2="197" y2="142" stroke="#0f172a" stroke-width="2.5" stroke-linecap="round"/><rect x="146" y="28" width="54" height="8" fill="#94a3b8" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><line x1="160" y1="20" x2="160" y2="38" stroke="#0f172a" stroke-width="2" stroke-linecap="round"/><rect x="153" y="38" width="14" height="3.5" fill="#334155" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round"/><line x1="186" y1="20" x2="186" y2="38" stroke="#0f172a" stroke-width="2" stroke-linecap="round"/><rect x="179" y="38" width="14" height="3.5" fill="#334155" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round"/><line x1="173" y1="20" x2="173" y2="36" stroke="#64748b" stroke-width="3" stroke-linecap="round"/><rect x="151" y="84" width="44" height="14" fill="#94a3b8" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><line x1="173" y1="98" x2="173" y2="150" stroke="#0f172a" stroke-width="3" stroke-linecap="round"/><line x1="173" y1="78" x2="173" y2="59" stroke="#dc2626" stroke-width="2.5" stroke-linecap="round"/><polygon points="173,52 176.2,59 169.8,59" fill="#dc2626"/><text x="173" y="170" font-size="12" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">2. Compression</text><rect x="264" y="36" width="48" height="48" fill="#fdba74" stroke="#0f172a" stroke-width="0" stroke-linejoin="round"/><line x1="264" y1="36" x2="264" y2="142" stroke="#0f172a" stroke-width="2.5" stroke-linecap="round"/><line x1="312" y1="36" x2="312" y2="142" stroke="#0f172a" stroke-width="2.5" stroke-linecap="round"/><rect x="261" y="28" width="54" height="8" fill="#94a3b8" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><line x1="275" y1="20" x2="275" y2="38" stroke="#0f172a" stroke-width="2" stroke-linecap="round"/><rect x="268" y="38" width="14" height="3.5" fill="#334155" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round"/><line x1="301" y1="20" x2="301" y2="38" stroke="#0f172a" stroke-width="2" stroke-linecap="round"/><rect x="294" y="38" width="14" height="3.5" fill="#334155" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round"/><line x1="288" y1="20" x2="288" y2="36" stroke="#64748b" stroke-width="3" stroke-linecap="round"/><rect x="266" y="84" width="44" height="14" fill="#94a3b8" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><line x1="288" y1="98" x2="288" y2="150" stroke="#0f172a" stroke-width="3" stroke-linecap="round"/><line x1="288" y1="52" x2="288" y2="71" stroke="#dc2626" stroke-width="2.5" stroke-linecap="round"/><polygon points="288,78 284.9,71 291.1,71" fill="#dc2626"/><text x="288" y="170" font-size="12" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">3. Explosion-détente</text><rect x="379" y="36" width="48" height="48" fill="#e5e7eb" stroke="#0f172a" stroke-width="0" stroke-linejoin="round"/><line x1="379" y1="36" x2="379" y2="142" stroke="#0f172a" stroke-width="2.5" stroke-linecap="round"/><line x1="427" y1="36" x2="427" y2="142" stroke="#0f172a" stroke-width="2.5" stroke-linecap="round"/><rect x="376" y="28" width="54" height="8" fill="#94a3b8" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><line x1="390" y1="20" x2="390" y2="38" stroke="#0f172a" stroke-width="2" stroke-linecap="round"/><rect x="383" y="38" width="14" height="3.5" fill="#334155" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round"/><line x1="416" y1="20" x2="416" y2="45" stroke="#0f172a" stroke-width="2" stroke-linecap="round"/><rect x="409" y="45" width="14" height="3.5" fill="#334155" stroke="#0f172a" stroke-width="1.2" stroke-linejoin="round"/><line x1="403" y1="20" x2="403" y2="36" stroke="#64748b" stroke-width="3" stroke-linecap="round"/><rect x="381" y="84" width="44" height="14" fill="#94a3b8" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><line x1="403" y1="98" x2="403" y2="150" stroke="#0f172a" stroke-width="3" stroke-linecap="round"/><line x1="403" y1="78" x2="403" y2="59" stroke="#dc2626" stroke-width="2.5" stroke-linecap="round"/><polygon points="403,52 406.1,59 399.9,59" fill="#dc2626"/><text x="403" y="170" font-size="12" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">4. Échappement</text></svg>
:::

| Temps | Piston | Soupapes | Ce qui se passe |
| --- | --- | --- | --- |
| 1. Admission | descend | soupape d'admission ouverte | le cylindre aspire le mélange air-carburant |
| 2. Compression | monte | toutes fermées | le mélange est comprimé |
| 3. Explosion-détente | descend | toutes fermées | le mélange s'enflamme, la pression des gaz **pousse** le piston : temps moteur |
| 4. Échappement | monte | soupape d'échappement ouverte | le piston chasse les gaz brûlés |

La colonne des soupapes est un **principe** de fonctionnement : c'est ce qui permet de lire un temps sur un dessin en coupe sans le nom écrit dessous.

::: exemple Compter les courses, les tours et les temps moteur
Un cylindre tourne à 1 200 tr/min (valeur d'entraînement).
1. **Un cycle** compte 4 temps, donc **4 courses**. Une course est un aller ou un retour du piston : 4 courses font 2 allers-retours.
2. Un aller-retour du piston correspond à **un tour** du vilebrequin : le cycle dure donc **2 tours**.
3. À 1 200 tr/min, le vilebrequin fait 1 200 / 2 = **600 cycles par minute**, soit 10 par seconde.
4. Un seul temps est moteur par cycle : le cylindre **pousse 10 fois par seconde**, et les trois autres temps consomment de l'énergie.

:::

::: piege La compression n'est pas un temps moteur
« Le mélange est comprimé, il y a de la pression, donc ça pousse. » La pression de la compression s'oppose au piston qui monte : il faut **fournir** de l'énergie pour comprimer. Ce qui pousse le piston, c'est la pression **après** l'inflammation, au troisième temps. C'est pour lier ces temps résistants que le moteur a besoin d'un volant (section suivante).
:::

::: verifie
Un cylindre effectue 3 cycles. Combien de courses de piston, combien de tours de vilebrequin, combien de temps moteur ?
---
**12 courses** (3 × 4), **6 tours** (2 tours par cycle) et **3 temps moteur** (un par cycle).
:::

## 🔁 Du piston au vilebrequin : course et cylindrée

Le piston ne sait aller qu'en ligne droite, alors que les roues tournent. Il faut une pièce qui transforme le va-et-vient en rotation.

De combien le piston se déplace-t-il alors, et quel volume balaie-t-il ?

::: definition Le mécanisme bielle-manivelle
La **bielle** relie le **piston** au **vilebrequin**. Le vilebrequin joue le rôle de la **manivelle** de rayon **R** : il tourne autour de son axe O. Le piston joue le rôle du **coulisseau** et le **cylindre** celui de la **glissière** : le piston ne fait que **translater** dans son cylindre. Ses positions extrêmes sont le **point mort haut** (PMH) et le **point mort bas** (PMB) ; la distance qui les sépare est la **course** c.
:::

::: figure Le mécanisme du moteur : O est l'axe du vilebrequin, A le point où la bielle s'y articule, B le point où elle s'articule au piston. Les pointillés marquent les deux positions extrêmes. Schéma de principe
<svg viewBox="0 0 460 290"><title>Mécanisme bielle-manivelle : piston, bielle, vilebrequin, cylindre, course entre PMH et PMB</title><line x1="94" y1="62" x2="94" y2="218" stroke="#0f172a" stroke-width="2.5" stroke-linecap="round"/><line x1="146" y1="62" x2="146" y2="218" stroke="#0f172a" stroke-width="2.5" stroke-linecap="round"/><rect x="90" y="54" width="60" height="8" fill="#94a3b8" stroke="#0f172a" stroke-width="1.8" stroke-linejoin="round"/><line x1="60" y1="110" x2="250" y2="110" stroke="#64748b" stroke-width="1.5" stroke-linecap="round" stroke-dasharray="6 4"/><line x1="60" y1="190" x2="250" y2="190" stroke="#64748b" stroke-width="1.5" stroke-linecap="round" stroke-dasharray="6 4"/><circle cx="120" cy="250" r="40" fill="none" stroke="#64748b" stroke-width="1.5" stroke-dasharray="5 4"/><rect x="98" y="115.1" width="44" height="28" fill="#fecaca" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><line x1="150.6" y1="224.3" x2="120" y2="129.1" stroke="#15803d" stroke-width="7" stroke-linecap="round"/><line x1="150.6" y1="224.3" x2="120" y2="129.1" stroke="#bbf7d0" stroke-width="3.5" stroke-linecap="round"/><line x1="120" y1="250" x2="150.6" y2="224.3" stroke="#1d4ed8" stroke-width="7" stroke-linecap="round"/><line x1="120" y1="250" x2="150.6" y2="224.3" stroke="#bfdbfe" stroke-width="3.5" stroke-linecap="round"/><circle cx="120" cy="250" r="5" fill="#0f172a" stroke="#0f172a" stroke-width="1.5"/><circle cx="150.6" cy="224.3" r="4.5" fill="#ffffff" stroke="#0f172a" stroke-width="2"/><circle cx="120" cy="129.1" r="4.5" fill="#ffffff" stroke="#0f172a" stroke-width="2"/><text x="106" y="266" font-size="12" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">O</text><text x="164.6" y="228.3" font-size="12" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">A</text><text x="154" y="133.1" font-size="12" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">B</text><line x1="212" y1="113" x2="212" y2="181" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><polygon points="212,187 209.3,181 214.7,181" fill="#0f172a"/><line x1="212" y1="187" x2="212" y2="119" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round"/><polygon points="212,113 214.7,119 209.3,119" fill="#0f172a"/><text x="236" y="154" font-size="12" font-weight="600" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">c = 2R</text><text x="66" y="105" font-size="11" font-weight="600" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">PMH</text><text x="66" y="185" font-size="11" font-weight="600" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">PMB</text><text x="147.3" y="249.1" font-size="12" font-weight="600" text-anchor="start" fill="#1d4ed8" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">R</text><text x="320" y="94" font-size="11.5" font-weight="600" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">piston (coulisseau)</text><line x1="318" y1="90" x2="150" y2="121.1" stroke="#64748b" stroke-width="1.2" stroke-linecap="round"/><text x="320" y="150" font-size="11.5" font-weight="600" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">bielle</text><line x1="318" y1="146" x2="138.3" y2="176.7" stroke="#64748b" stroke-width="1.2" stroke-linecap="round"/><text x="320" y="268" font-size="11.5" font-weight="600" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">vilebrequin (manivelle)</text><line x1="318" y1="264" x2="138.3" y2="240.1" stroke="#64748b" stroke-width="1.2" stroke-linecap="round"/><text x="320" y="40" font-size="11.5" font-weight="600" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">cylindre (glissière)</text><line x1="318" y1="36" x2="148" y2="70" stroke="#64748b" stroke-width="1.2" stroke-linecap="round"/></svg>
:::

Au PMH, O, A et B sont alignés avec A du côté du piston : B est à la distance L + R de O (L est la longueur de la bielle). Au PMB, A est du côté opposé : B est à L − R. La course est la différence.

::: propriete Course et rayon
La course vaut **le double du rayon du vilebrequin** :

$$ c = 2 × R $$
:::

Le tableau des mouvements se lit ainsi : le **piston** reçoit la poussée des gaz, c'est le **mouvement d'entrée** (translation) ; le **vilebrequin** livre le **mouvement de sortie** (rotation continue). La transformation est **réversible** : si on fait tourner le vilebrequin, comme avec la manivelle de la maquette, le piston se déplace. Aux points morts, la bielle ne peut plus faire tourner le vilebrequin ; c'est le **volant moteur**, solidaire du vilebrequin, qui lui fait passer ces points et lisse la rotation entre les temps moteur.

::: definition La cylindrée
Le **volume balayé** par un piston est le volume que le piston traverse entre le PMH et le PMB : (surface du piston) × (course). La **cylindrée** est ce volume multiplié par le nombre de cylindres :

$$ cylindrée = (π × d² / 4) × c × nombre de cylindres $$

avec d le diamètre du piston. On l'exprime en litre : 1 L = 1 dm³ = 1 000 cm³ = 1 000 000 mm³.
:::

::: exemple La cylindrée de la maquette
Données du manuel : d = 85 mm, 4 cylindres. La course se mesure sur la maquette ; on prend ici R = 40 mm (valeur d'entraînement).
1. **Course** : c = 2 × 40 = **80 mm**, car c = 2R.
2. **Surface du piston** : π × 85² / 4 ≈ 5 675 mm², car la surface d'un disque est π d² / 4.
3. **Volume balayé** : 5 675 × 80 ≈ 453 960 mm³ ≈ **454 cm³**.
4. **Cylindrée** : 454 × 4 ≈ 1 816 cm³, soit **1,82 L**.

:::

::: piege Le diamètre n'est pas le rayon
Remplacer d par 85 dans « π × r² » donne un volume **quatre fois trop grand** (7,26 L au lieu de 1,82 L) : la surface est π (d/2)² = π d² / 4. Et oublier le nombre de cylindres divise le résultat par 4. Contrôle : une cylindrée de voiture courante est de 1 à 3 L.
:::

::: verifie
Un moteur à 3 cylindres a des pistons de 60 mm de diamètre et une course de 70 mm. Quelle est sa cylindrée en litre ?
---
Surface : π × 60² / 4 ≈ 2 827 mm² ; volume balayé : 2 827 × 70 ≈ 197 920 mm³ ; × 3 cylindres ≈ 593 760 mm³, soit **0,59 L**.
:::

## 🧭 La vitesse du piston : de ω à V_B

Le vilebrequin tourne à un régime donné, N1 = 1 600 tr/min pour la maquette. Le point A de la manivelle tourne sur un cercle, le point B du piston glisse sur une droite, et une bielle rigide les relie.

À quelle vitesse bouge A, puis le piston lui-même ?

::: definition ω, V_A et l'équiprojectivité
La **vitesse angulaire** ω (en rad/s) se déduit de la vitesse de rotation N (en tr/min) :

$$ ω = 2π × N / 60 $$

Le point A du vilebrequin décrit un cercle de rayon R : sa vitesse **V_A** est **tangente au cercle**, donc perpendiculaire à OA, et sa norme vaut (R en mètre pour avoir des m/s) :

$$ V_A = ω × R $$

Le **théorème de l'équiprojectivité** s'applique à deux points d'un même solide, ici A et B de la bielle : les **projections** de V_A et V_B sur la droite AB sont **égales**.
:::

::: figure Deux positions de la même mécanique. À gauche, la manivelle est perpendiculaire à l'axe du cylindre : V_A et V_B sont parallèles et leurs projections sur AB (traits violets) sont égales. À droite, le piston est au PMH : V_A est perpendiculaire à AB et sa projection sur AB est nulle. Schéma de principe, sans échelle
<svg viewBox="0 0 460 280"><title>Équiprojectivité : manivelle horizontale, puis piston au point mort haut</title><line x1="80" y1="38.3" x2="80" y2="214" stroke="#64748b" stroke-width="1.2" stroke-linecap="round" stroke-dasharray="8 3 2 3"/><rect x="64" y="99.3" width="32" height="18" fill="#fecaca" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><circle cx="80" cy="200" r="40" fill="none" stroke="#64748b" stroke-width="1.3" stroke-dasharray="5 4"/><line x1="80" y1="200" x2="120" y2="200" stroke="#1d4ed8" stroke-width="6" stroke-linecap="round"/><line x1="120" y1="200" x2="80" y2="108.3" stroke="#15803d" stroke-width="6" stroke-linecap="round"/><line x1="120" y1="150" x2="101.7" y2="158" stroke="#64748b" stroke-width="1.2" stroke-linecap="round" stroke-dasharray="4 3"/><line x1="80" y1="58.3" x2="61.7" y2="66.3" stroke="#64748b" stroke-width="1.2" stroke-linecap="round" stroke-dasharray="4 3"/><line x1="120" y1="200" x2="101.7" y2="158" stroke="#7c3aed" stroke-width="4.5" stroke-linecap="round"/><line x1="80" y1="108.3" x2="61.7" y2="66.3" stroke="#7c3aed" stroke-width="4.5" stroke-linecap="round"/><line x1="120" y1="200" x2="120" y2="158" stroke="#dc2626" stroke-width="2.5" stroke-linecap="round"/><polygon points="120,150 123.6,158 116.4,158" fill="#dc2626"/><line x1="80" y1="108.3" x2="80" y2="66.3" stroke="#dc2626" stroke-width="2.5" stroke-linecap="round"/><polygon points="80,58.3 83.6,66.3 76.4,66.3" fill="#dc2626"/><circle cx="80" cy="200" r="4" fill="#0f172a" stroke="#0f172a" stroke-width="1.5"/><circle cx="120" cy="200" r="4" fill="#ffffff" stroke="#0f172a" stroke-width="2"/><circle cx="80" cy="108.3" r="4" fill="#ffffff" stroke="#0f172a" stroke-width="2"/><text x="66" y="214" font-size="12" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">O</text><text x="132" y="215" font-size="12" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">A</text><text x="104" y="112.3" font-size="12" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">B</text><text x="128" y="148" font-size="12" font-weight="600" text-anchor="start" fill="#dc2626" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">V</text><text x="135.9" y="151" font-size="9.0" font-weight="600" text-anchor="start" fill="#dc2626" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">A</text><text x="88" y="56.3" font-size="12" font-weight="600" text-anchor="start" fill="#dc2626" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">V</text><text x="95.9" y="59.3" font-size="9.0" font-weight="600" text-anchor="start" fill="#dc2626" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">B</text><text x="115" y="238" font-size="11.5" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Manivelle perpendiculaire à l'axe</text><text x="115" y="254" font-size="11.5" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">projections égales sur AB, donc</text><text x="88" y="270" font-size="11.5" font-weight="600" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">V</text><text x="95.6" y="273" font-size="8.6" font-weight="600" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">B</text><text x="100.9" y="270" font-size="11.5" font-weight="600" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"> = </text><text x="124" y="270" font-size="11.5" font-weight="600" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">V</text><text x="131.6" y="273" font-size="8.6" font-weight="600" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">A</text><line x1="340" y1="36" x2="340" y2="214" stroke="#64748b" stroke-width="1.2" stroke-linecap="round" stroke-dasharray="8 3 2 3"/><rect x="324" y="51" width="32" height="18" fill="#fecaca" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><circle cx="340" cy="200" r="40" fill="none" stroke="#64748b" stroke-width="1.3" stroke-dasharray="5 4"/><line x1="340" y1="200" x2="340" y2="160" stroke="#1d4ed8" stroke-width="6" stroke-linecap="round"/><line x1="340" y1="160" x2="340" y2="60" stroke="#15803d" stroke-width="6" stroke-linecap="round"/><line x1="340" y1="160" x2="384" y2="160" stroke="#dc2626" stroke-width="2.5" stroke-linecap="round"/><polygon points="392,160 384,163.6 384,156.4" fill="#dc2626"/><circle cx="340" cy="200" r="4" fill="#0f172a" stroke="#0f172a" stroke-width="1.5"/><circle cx="340" cy="160" r="4" fill="#ffffff" stroke="#0f172a" stroke-width="2"/><circle cx="340" cy="60" r="4" fill="#ffffff" stroke="#0f172a" stroke-width="2"/><text x="326" y="214" font-size="12" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">O</text><text x="326" y="164" font-size="12" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">A</text><text x="366" y="64" font-size="12" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">B</text><text x="396" y="164" font-size="12" font-weight="600" text-anchor="start" fill="#dc2626" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">V</text><text x="403.9" y="167" font-size="9.0" font-weight="600" text-anchor="start" fill="#dc2626" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">A</text><text x="340" y="238" font-size="11.5" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Piston au point mort haut</text><text x="292" y="254" font-size="11.5" font-weight="600" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">V</text><text x="299.6" y="257" font-size="8.6" font-weight="600" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">A</text><text x="304.9" y="254" font-size="11.5" font-weight="600" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"> perpendiculaire à AB, donc</text><text x="322" y="270" font-size="11.5" font-weight="600" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">V</text><text x="329.6" y="273" font-size="8.6" font-weight="600" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">B</text><text x="334.9" y="270" font-size="11.5" font-weight="600" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round"> = 0</text></svg>
:::

::: exemple De N1 = 1 600 tr/min à la vitesse du piston
On garde R = 40 mm (valeur d'entraînement) ; N1 et l'échelle 0,3 m/s pour 1 mm sont ceux du manuel.
1. **ω** = 2π × 1 600 / 60 ≈ **167,6 rad/s**, car un tour fait 2π rad et une minute 60 s.
2. **V_A** = ω × R = 167,6 × 0,040 ≈ **6,70 m/s**, avec R converti en mètre. On la trace tangente au cercle.
3. **Longueur sur le dessin** : 6,70 / 0,3 ≈ **22,3 mm**, car 1 mm représente 0,3 m/s.
4. **V_B**, manivelle perpendiculaire à l'axe : V_A et V_B sont parallèles, donc elles font le même angle avec AB ; des projections égales imposent alors des normes égales : **V_B = V_A ≈ 6,70 m/s**.
5. **V_B**, piston au PMH : V_A ⟂ AB, sa projection est nulle, donc la projection de V_B aussi : **V_B = 0**, le piston s'arrête avant de repartir.

:::

::: piege La vitesse du piston n'est pas constante
Le vilebrequin tourne à N constant, donc V_A garde toujours la même norme. Mais V_B vaut 6,70 m/s dans une position, **0** au PMH et au PMB : on ne peut pas recopier V_A. Autre piège de calcul : garder R en millimètre donne un V_A mille fois trop grand, en m/s.
:::

::: verifie
Un moteur tourne à 1 200 tr/min ; R = 50 mm. Calcule ω puis V_A.
---
ω = 2π × 1 200 / 60 ≈ **125,7 rad/s** ; V_A = 125,7 × 0,050 ≈ **6,28 m/s**.
:::

## 🚪 La came, le poussoir et la soupape

Les gaz doivent entrer au bon moment et sortir au bon moment, une fois par cycle.

Qui ouvre les soupapes, au bon instant ?

::: definition Came, poussoir, soupape
La maquette compte **8 soupapes pour 4 cylindres**, soit deux par cylindre : l'une d'**admission**, l'autre d'**échappement** (principe). Une soupape ouvre ou ferme le passage des gaz entre le cylindre et l'extérieur. Un **ressort** la rappelle en position fermée.

L'**arbre à cames** tourne d'un mouvement **continu** ; chaque **came** pousse un **poussoir** qui se déplace en **translation alternative** et commande la soupape. Le contour de la came est son **profil** : un **cercle minimal** sur lequel le poussoir ne bouge pas (soupape fermée), et un bossage qui le soulève.
:::

::: figure Une came tournante et son poussoir. Le profil est le cercle minimal (pointillés) sur un demi-tour, puis le bossage sur l'autre demi-tour ; la flèche donne le sens de rotation. Schéma de principe, bossage exagéré
<svg viewBox="0 0 400 260"><title>Came tournante et poussoir : cercle minimal et bossage sur un demi-tour</title><polygon points="150,100 155.6,96.9 161.8,94.6 168.5,93 175.6,92.4 183,92.8 190.4,94.3 197.8,96.9 204.8,100.6 211.4,105.4 217.3,111.1 222.4,117.8 226.5,125.1 229.5,133.1 231.4,141.4 232,150 231.4,158.6 229.5,166.9 226.5,174.9 222.4,182.2 217.3,188.9 211.4,194.6 204.8,199.4 197.8,203.1 190.4,205.7 183,207.2 175.6,207.6 168.5,207 161.8,205.4 155.6,203.1 150,200 144.8,199.7 139.6,198.9 134.5,197.6 129.7,195.7 125,193.3 120.6,190.5 116.5,187.2 112.8,183.5 109.5,179.4 106.7,175 104.3,170.3 102.4,165.5 101.1,160.4 100.3,155.2 100,150 100.3,144.8 101.1,139.6 102.4,134.5 104.3,129.7 106.7,125 109.5,120.6 112.8,116.5 116.5,112.8 120.6,109.5 125,106.7 129.7,104.3 134.5,102.4 139.6,101.1 144.8,100.3" fill="#fde68a" stroke="#0f172a" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round"/><circle cx="150" cy="150" r="50" fill="none" stroke="#b45309" stroke-width="1.8" stroke-dasharray="6 4"/><circle cx="150" cy="150" r="5" fill="#0f172a" stroke="#0f172a" stroke-width="1.5"/><rect x="140" y="38" width="20" height="62" fill="#bbf7d0" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="128" y="22" width="44" height="16" fill="#bfdbfe" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><path d="M 170 150 A 20 20 0 0 0 130 150" fill="none" stroke="#dc2626" stroke-width="2.5" stroke-linecap="round"/><polygon points="130,159 123,148 137,148" fill="#dc2626"/><text x="260" y="62" font-size="11.5" font-weight="600" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">poussoir</text><line x1="258" y1="58" x2="162" y2="70" stroke="#64748b" stroke-width="1.2" stroke-linecap="round"/><text x="260" y="150" font-size="11.5" font-weight="600" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">came</text><line x1="258" y1="146" x2="230" y2="148" stroke="#64748b" stroke-width="1.2" stroke-linecap="round"/><text x="260" y="232" font-size="11.5" font-weight="600" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">cercle minimal</text><line x1="258" y1="228" x2="185" y2="185" stroke="#b45309" stroke-width="1.2" stroke-linecap="round"/></svg>
:::

Pour un tour de l'arbre à cames, le manuel décrit trois phases : **demi-tour** sur le cercle minimal (soupape fermée, course nulle), **quart de tour** de descente (la soupape s'ouvre), **quart de tour** de montée (elle se referme).

::: exemple La vitesse de l'arbre à cames
Le vilebrequin tourne à N1 = 1 600 tr/min (donnée du manuel).
1. Une soupape donnée s'ouvre **une seule fois par cycle** : le cycle dure **2 tours** de vilebrequin.
2. Sa came doit donc faire **un tour par cycle**, soit un tour pour 2 tours de vilebrequin.
3. L'arbre à cames tourne **deux fois moins vite** : 1 600 / 2 = **800 tr/min**. C'est le rapport que doit réaliser la chaîne de distribution qui relie les deux arbres (principe).

:::

::: propriete Un système à came : irréversible, avec glissement
- Le poussoir **ne peut pas** faire tourner la came : le mouvement ne passe que dans un sens, le système est **irréversible**.
- Le contact poussoir-came se fait par **glissement**. Pour réduire le frottement, une solution constructive est de munir le poussoir d'un **galet** : le contact devient un **roulement**.
:::

::: piege Le ressort ferme la soupape, il ne l'ouvre pas
Le ressort rappelle la soupape sur son siège, ce qui ferme la chambre de combustion, et garde le poussoir en contact avec la came. L'**ouverture** vient de la came. Une soupape sans ressort resterait ouverte dès que la came l'aurait poussée.
:::

::: verifie
Le poussoir repose sur le cercle minimal de sa came. La soupape est-elle ouverte ? Et si l'arbre à cames tourne à 600 tr/min, à quelle vitesse tourne le vilebrequin ?
---
Elle est **fermée** : sur le cercle minimal, le poussoir ne bouge pas. Le vilebrequin tourne deux fois plus vite : **1 200 tr/min**.
:::

## 🦶 Débrayer : de la fourchette au plateau

Le moteur de la maquette tourne en permanence ; pour changer de vitesse, il faut couper un instant la liaison avec la boîte. Un simple coup de pied suffit pourtant à desserrer un disque pressé avec force.

Comment ?

::: definition L'embrayage à diaphragme de la maquette
L'**embrayage** relie à volonté le volant moteur à l'arbre d'embrayage, donc à la boîte. Sur la maquette, la **fourchette (18)** pousse la **butée (13)** contre le **diaphragme (11)**, pièce élastique qui se déforme et fait **reculer le plateau (8)** : c'est le **débrayage**. Quand la fourchette revient sous l'action de son ressort (24), le plateau serre de nouveau le **disque porte-garniture (26)** contre le volant : c'est l'**embrayage**.
:::

::: figure En haut, la chaîne du débrayage, d'un organe au suivant. En bas, le disque pris entre le volant et le plateau (embrayé), puis libéré quand le plateau recule (débrayé). Schéma de principe : les organes sont alignés sur l'axe
<svg viewBox="0 0 460 262"><title>Chaîne de débrayage, puis disque serré (embrayé) ou libre (débrayé)</title><rect x="14" y="24" width="88" height="44" fill="#fed7aa" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><text x="58" y="44" font-size="12" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">fourchette</text><text x="58" y="60" font-size="11.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">(18)</text><line x1="102" y1="46" x2="121" y2="46" stroke="#dc2626" stroke-width="2.5" stroke-linecap="round"/><polygon points="128,46 121,49.1 121,42.9" fill="#dc2626"/><rect x="128" y="24" width="88" height="44" fill="#e9d5ff" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><text x="172" y="44" font-size="12" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">butée</text><text x="172" y="60" font-size="11.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">(13)</text><line x1="216" y1="46" x2="235" y2="46" stroke="#dc2626" stroke-width="2.5" stroke-linecap="round"/><polygon points="242,46 235,49.1 235,42.9" fill="#dc2626"/><rect x="242" y="24" width="88" height="44" fill="#fde68a" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><text x="286" y="44" font-size="12" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">diaphragme</text><text x="286" y="60" font-size="11.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">(11)</text><line x1="330" y1="46" x2="349" y2="46" stroke="#dc2626" stroke-width="2.5" stroke-linecap="round"/><polygon points="356,46 349,49.1 349,42.9" fill="#dc2626"/><rect x="356" y="24" width="88" height="44" fill="#bbf7d0" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><text x="400" y="44" font-size="12" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">plateau</text><text x="400" y="60" font-size="11.5" font-weight="500" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">(8)</text><text x="230" y="14" font-size="11.5" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Débrayage : la poussée traverse la chaîne</text><rect x="30" y="120" width="26" height="90" fill="#bfdbfe" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="56" y="128" width="6" height="74" fill="#fde68a" stroke="#0f172a" stroke-width="1.5" stroke-linejoin="round"/><rect x="62" y="128" width="6" height="74" fill="#cbd5e1" stroke="#0f172a" stroke-width="1.5" stroke-linejoin="round"/><rect x="68" y="128" width="6" height="74" fill="#fde68a" stroke="#0f172a" stroke-width="1.5" stroke-linejoin="round"/><rect x="74" y="120" width="26" height="90" fill="#bbf7d0" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><text x="42" y="226" font-size="11" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">volant</text><text x="65" y="242" font-size="11" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">disque</text><text x="87" y="226" font-size="11" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">plateau</text><text x="70" y="112" font-size="12" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Embrayé</text><rect x="270" y="120" width="26" height="90" fill="#bfdbfe" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="296" y="128" width="6" height="74" fill="#fde68a" stroke="#0f172a" stroke-width="1.5" stroke-linejoin="round"/><rect x="302" y="128" width="6" height="74" fill="#cbd5e1" stroke="#0f172a" stroke-width="1.5" stroke-linejoin="round"/><rect x="308" y="128" width="6" height="74" fill="#fde68a" stroke="#0f172a" stroke-width="1.5" stroke-linejoin="round"/><rect x="340" y="120" width="26" height="90" fill="#bbf7d0" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><text x="282" y="226" font-size="11" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">volant</text><text x="305" y="242" font-size="11" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">disque</text><text x="353" y="226" font-size="11" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">plateau</text><text x="310" y="112" font-size="12" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Débrayé</text><line x1="327" y1="110" x2="353" y2="110" stroke="#dc2626" stroke-width="2.5" stroke-linecap="round"/><polygon points="360,110 353,113.2 353,106.8" fill="#dc2626"/><text x="366" y="114" font-size="11" font-weight="600" text-anchor="start" fill="#dc2626" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">recule</text></svg>
:::

::: exemple Que devient le disque ?
On appuie sur la pédale de la maquette et on tourne le vilebrequin à la manivelle.
1. Le plateau (8) a **reculé** : il ne presse plus le disque (26) contre le volant.
2. Sans pression il n'y a plus de frottement, donc le volant ne peut plus entraîner le disque.
3. Le disque **ne tourne pas** ; relâche la pédale, le ressort rappelle la fourchette, le plateau serre et le disque **tourne avec le volant**.

:::

::: piege Le pied débraye
On pense qu'appuyer sur la pédale « enclenche » l'embrayage. C'est le contraire : **pédale appuyée**, le disque est libre (débrayé) ; **pédale relâchée**, il est serré (embrayé). L'effort du pied sert à **vaincre** l'élasticité du diaphragme, pas à transmettre la puissance.
:::

::: verifie
Dans la chaîne du débrayage, quelle pièce reçoit directement la poussée de la fourchette, et quelle pièce recule en dernier ?
---
La **butée (13)** reçoit la poussée ; le **plateau (8)** recule en dernier, après la déformation du diaphragme.
:::

## 🔗 Du volant à l'arbre : le couple que le disque peut transmettre

Embrayé, le disque transmet la puissance du moteur, mais pas sans limite.

Quel couple peut-il transmettre sans glisser, et que font les autres pièces autour de lui ?

::: definition Couple transmissible, couronne, moyeu amortisseur
Le **couple transmissible Ct** est le couple maximal que l'embrayage transmet sans glisser. Comme au chapitre sur l'embrayage à disque, il est **proportionnel** à quatre grandeurs : le **nombre de surfaces en contact** n, le **coefficient de frottement** f des garnitures, l'**effort presseur** (celui qui serre le disque) et le **rayon d'action** Rm.

Deux autres pièces ont chacune une fonction : la **couronne dentée (7)**, montée sur le volant, laisse le **démarreur** lancer le moteur ; les **ressorts du moyeu amortisseur (30)** absorbent les **à-coups de couple** avant l'arbre d'embrayage.
:::

La puissance suit donc un trajet : **volant (27) → disque porte-garniture (26) → moyeu amortisseur (30) → arbre d'embrayage (17) → boîte**. Le volant et le disque se lient par **adhérence** (frottement), comme au chapitre sur l'embrayage à disque.

::: exemple Quand l'effort presseur baisse
Un embrayage est réglé pour transmettre Ct = 100 N·m (valeur d'entraînement). Les éléments élastiques se fatiguent et l'effort presseur perd 20 %.
1. Ct est **proportionnel** à l'effort presseur : n, f et Rm n'ont pas changé.
2. Ct devient 100 × 0,8 = **80 N·m**.
3. Si le moteur demande un couple supérieur, par exemple 90 N·m, le disque **glisse** : Ct est un maximum, pas une consigne.

:::

::: piege La vitesse de rotation ne change pas Ct
« Le moteur tourne plus vite, donc il transmet plus. » La **vitesse** n'apparaît pas dans les facteurs de Ct ; le **couple** demandé, lui, peut dépasser Ct, et alors le disque patine. On évite aussi de confondre l'effort presseur, noté N au chapitre sur l'embrayage à disque, avec la vitesse de rotation N, notée de la même lettre.
:::

::: verifie
Citer les quatre grandeurs dont Ct dépend, et dire ce que devient Ct si le coefficient de frottement double.
---
Le nombre de surfaces n, le coefficient de frottement f, l'effort presseur et le rayon moyen Rm. Ct est proportionnel à f : **il double**.
:::

## 🕹️ Les six positions du levier : rapport et sens

Le levier de la maquette occupe six positions, de A à F : cinq vitesses et la marche arrière.

Pour chacune, quelles roues transmettent, et avec quel rapport ?

::: definition Pignon arbré, pignon fou, baladeur
Un **pignon arbré** est taillé dans son arbre : il tourne toujours avec lui. Un **pignon fou** tourne **librement** sur son arbre tant qu'un **baladeur** ne l'a pas lié à lui. Les **trois baladeurs** de la nomenclature se partagent les vitesses : le baladeur (17) sert la 1re et la 2e, le (18) la 3e, le (19) la 4e et la 5e. La marche arrière a **sa propre fourchette (33)**, et son pignon (13) est porté par l'axe (30).
:::

Comme au chapitre sur la boîte de vitesses, le rapport d'une vitesse est le **produit** des rapports de chaque paire : r = Z menante / Z menée, de l'entrée vers la sortie. Le nombre d'engrènements extérieurs donne le sens.

::: figure La première vitesse en principe : (1) mène (2), puis (10) mène (9), que le baladeur (17) lie à l'arbre de sortie. Les pointillés rouges relient les roues qui engrènent ; les tailles ne sont pas proportionnelles aux nombres de dents. Schéma de principe
<svg viewBox="0 0 460 205"><title>Schéma de principe de la première vitesse : (1)-(2), puis (10)-(9) lié à la sortie par le baladeur (17)</title><line x1="20" y1="50" x2="170" y2="50" stroke="#0f172a" stroke-width="3" stroke-linecap="round"/><line x1="40" y1="150" x2="420" y2="150" stroke="#0f172a" stroke-width="3" stroke-linecap="round"/><line x1="170" y1="50" x2="440" y2="50" stroke="#0f172a" stroke-width="3" stroke-linecap="round"/><text x="96" y="40" font-size="11" font-weight="600" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">arbre d'entrée (14)</text><text x="436" y="78" font-size="11" font-weight="600" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">arbre de sortie (16)</text><text x="300" y="172" font-size="11" font-weight="600" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">arbre intermédiaire (15)</text><rect x="70" y="28" width="10" height="44" fill="#bfdbfe" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><text x="75" y="20" font-size="11" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">(1)</text><rect x="70" y="128" width="10" height="44" fill="#bbf7d0" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><text x="75" y="190" font-size="11" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">(2)</text><line x1="75" y1="72" x2="75" y2="128" stroke="#dc2626" stroke-width="2.5" stroke-linecap="round" stroke-dasharray="5 3"/><rect x="250" y="128" width="10" height="44" fill="#bbf7d0" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><text x="255" y="190" font-size="11" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">(10)</text><rect x="250" y="28" width="10" height="44" fill="#fde68a" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><text x="255" y="20" font-size="11" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">(9)</text><line x1="255" y1="72" x2="255" y2="128" stroke="#dc2626" stroke-width="2.5" stroke-linecap="round" stroke-dasharray="5 3"/><rect x="296" y="34" width="20" height="32" fill="#fed7aa" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><text x="306" y="98" font-size="11" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">baladeur (17)</text><line x1="306" y1="84" x2="306" y2="66" stroke="#64748b" stroke-width="1.2" stroke-linecap="round"/></svg>
:::

::: exemple La première vitesse
Le manuel donne les paires de la 1re : (Z1, Z2) puis (Z9, Z10), avec Z1 = 37, Z2 = 47, Z10 = 13 et Z9 = 37. On les parcourt dans l'ordre de la puissance : (1) mène (2), puis (10) mène (9).
1. **Premier étage** : 37 / 47, car (1) est la menante.
2. **Second étage** : 13 / 37 : (10) est la menante, (9) la menée.
3. **Rapport** : r1 = (37 / 47) × (13 / 37) = **13 / 47 ≈ 0,277** : les 37 se simplifient. La 1re est une **réduction** (r < 1), comme on l'attend d'une première.
4. **Sens** : deux engrènements extérieurs, nombre pair : **même sens**, comme l'indique le manuel.
5. **Tours** : pour 10 tours de l'arbre d'entrée, l'arbre de sortie fait 10 × 13 / 47 ≈ **2,77 tours**.

L'ordre « (10) mène (9) » est une **lecture** de la nomenclature, pas un corrigé : une première vitesse doit réduire, et seule cette orientation donne r < 1.
:::

Pour la **2e vitesse**, le manuel laisse en blanc les nombres de dents des roues (7) et (8) : on les compte sur la maquette. Avec des valeurs d'entraînement Z8 = 21 et Z7 = 33 : r2 = (37 / 47) × (21 / 33) ≈ **0,50**. Pour la 4e, le manuel donne directement **r = 1** : l'arbre de sortie tourne comme l'entrée. Pour reculer, il faut un nombre **impair** d'engrènements extérieurs : le pignon de marche arrière (13) sert de pignon de renvoi, et le sens de sortie s'**inverse**.

::: piege La première a le plus petit rapport
« La 1re est le plus grand rapport », dit-on au volant. Mais r = N sortie / N entrée : en 1re, r1 ≈ 0,277 est le **plus petit** des rapports avant (0,50 en 2e avec les valeurs d'entraînement, 1 en 4e). Le conducteur parle de la **réduction** 47 / 13 ≈ 3,6, le technicien du rapport r, qui est son inverse.
:::

::: verifie
En 1re, le moteur tourne à 2 000 tr/min, embrayé. Quelle est la vitesse de l'arbre de sortie ?
---
N sortie = 2 000 × 13 / 47 ≈ **553 tr/min**.
:::

## 🚗 De la roue au compteur : retrouver les vitesses

Un véhicule roule à 30 km/h, et le compteur de vitesse est entraîné par un câble tiré de la boîte.

Quelle vitesse de rotation pour l'arbre de sortie, et pour ce câble ?

::: definition La prise de mouvement du compteur
Une **vis sans fin** (21) engrène avec une **roue** (20) : un tour de la vis fait avancer la roue d'**autant de dents que de filets**. Le rapport de vitesse est donc **r = nombre de filets / nombre de dents de la roue**. Le **câble du compteur** est entraîné par la roue.
:::

L'énoncé du manuel suppose que le **pont arrière ne change pas la vitesse** : l'arbre de sortie tourne donc exactement comme la roue.

::: exemple De 30 km/h à la vitesse du câble
Données du manuel : V = 30 km/h, diamètre de pneu 60 cm, 1re vitesse. Le nombre de filets et de dents est à compter sur la maquette ; on prend 1 filet et 15 dents (valeurs d'entraînement).
1. **Unités** : 30 km/h = 30 000 m / 60 min = **500 m/min**, et d = **0,6 m**.
2. **Un tour de roue** avance de π × d = π × 0,6 ≈ 1,885 m, car c'est le périmètre du pneu.
3. **Vitesse de la roue** : 500 / 1,885 ≈ **265 tr/min**, donc l'arbre de sortie N16 = **265 tr/min**.
4. **Le moteur**, en 1re : N = 265 × 47 / 13 ≈ **959 tr/min**, puisque r1 = 13 / 47.
5. **Le câble** : r = 1 / 15, donc 265 / 15 ≈ **17,7 tr/min**.

:::

::: piege Choisir la 1re vitesse ne change pas N16
La 1re vitesse n'intervient pas dans N16 : l'arbre de sortie tourne comme la roue, quelle que soit la vitesse engagée. Elle intervient dans la **vitesse du moteur** (étape 4). Autre piège : on prend le diamètre pour un rayon, et le périmètre est π d, pas π d / 2.
:::

::: verifie
Un véhicule roule à 36 km/h, pneu de 0,5 m de diamètre. Quelle est la vitesse de rotation de la roue ?
---
36 km/h = 600 m/min ; périmètre π × 0,5 ≈ 1,571 m ; N = 600 / 1,571 ≈ **382 tr/min**.
:::

## 🔄 Le synchroniseur : égaliser avant d'emboîter

Quand on passe une vitesse, le pignon fou à lier tourne à une vitesse différente de celle de l'arbre qui le reçoit. Si on les emboîtait brutalement, les crabots se heurteraient.

Comment égaliser leurs vitesses d'abord ?

::: definition Le synchroniseur
Le **synchroniseur** égalise les vitesses de deux pièces **avant** de les lier par **crabotage** (chapitre sur la boîte de vitesses). Il comprend le **moyeu** (lié à l'arbre), le **baladeur** qui coulisse, des **clavettes**, la **bague de synchronisation** à surface conique, et le pignon fou à lier. Au départ, le baladeur est au **point mort** : la bague ne touche pas le cône du pignon fou. Le passage se fait ensuite **en deux temps**.
:::

::: figure Le synchroniseur en trois états. Point mort : la bague ne touche pas le pignon fou. Temps 1 : le baladeur pousse la bague par la clavette, la bague frotte sur le pignon fou. Temps 2 : le baladeur avance, la clavette s'efface (pointillés) et ses dents s'entrelacent avec celles du pignon fou. Schéma de principe, pièces alignées sur l'axe
<svg viewBox="0 0 460 430"><title>Synchroniseur, schéma de principe : point mort, synchronisation, crabotage</title><rect x="20" y="120" width="420" height="12" fill="#e2e8f0" stroke="#0f172a" stroke-width="1.5" stroke-linejoin="round"/><rect x="40" y="60" width="110" height="60" fill="#bfdbfe" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="150" y="70" width="12" height="4" fill="#60a5fa" stroke="#0f172a" stroke-width="1.3" stroke-linejoin="round"/><rect x="150" y="76" width="12" height="4" fill="#60a5fa" stroke="#0f172a" stroke-width="1.3" stroke-linejoin="round"/><rect x="150" y="82" width="12" height="4" fill="#60a5fa" stroke="#0f172a" stroke-width="1.3" stroke-linejoin="round"/><rect x="270" y="92" width="70" height="28" fill="#fde68a" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="160" y="90" width="36" height="22" fill="#e9d5ff" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="196" y="48" width="150" height="12" fill="#bbf7d0" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="196" y="60" width="10" height="28" fill="#bbf7d0" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="176" y="67" width="20" height="4" fill="#4ade80" stroke="#0f172a" stroke-width="1.3" stroke-linejoin="round"/><rect x="176" y="73" width="20" height="4" fill="#4ade80" stroke="#0f172a" stroke-width="1.3" stroke-linejoin="round"/><rect x="176" y="79" width="20" height="4" fill="#4ade80" stroke="#0f172a" stroke-width="1.3" stroke-linejoin="round"/><rect x="196" y="90" width="16" height="18" fill="#1d4ed8" stroke="#0f172a" stroke-width="1.4" stroke-linejoin="round"/><text x="95" y="94" font-size="11" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">pignon fou</text><text x="305" y="109" font-size="11" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">moyeu</text><text x="22" y="38" font-size="12" font-weight="600" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Point mort</text><text x="358" y="54" font-size="11" font-weight="600" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">baladeur</text><line x1="354" y1="52" x2="346" y2="54" stroke="#64748b" stroke-width="1.2" stroke-linecap="round"/><text x="358" y="82" font-size="11" font-weight="600" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">clavette</text><line x1="354" y1="80" x2="212" y2="98" stroke="#64748b" stroke-width="1.2" stroke-linecap="round"/><text x="358" y="148" font-size="11" font-weight="600" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">bague de synchronisation</text><line x1="354" y1="144" x2="180" y2="112" stroke="#64748b" stroke-width="1.2" stroke-linecap="round"/><rect x="20" y="260" width="420" height="12" fill="#e2e8f0" stroke="#0f172a" stroke-width="1.5" stroke-linejoin="round"/><rect x="40" y="200" width="110" height="60" fill="#bfdbfe" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="150" y="210" width="12" height="4" fill="#60a5fa" stroke="#0f172a" stroke-width="1.3" stroke-linejoin="round"/><rect x="150" y="216" width="12" height="4" fill="#60a5fa" stroke="#0f172a" stroke-width="1.3" stroke-linejoin="round"/><rect x="150" y="222" width="12" height="4" fill="#60a5fa" stroke="#0f172a" stroke-width="1.3" stroke-linejoin="round"/><rect x="270" y="232" width="70" height="28" fill="#fde68a" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="150" y="230" width="36" height="22" fill="#e9d5ff" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="186" y="188" width="150" height="12" fill="#bbf7d0" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="186" y="200" width="10" height="28" fill="#bbf7d0" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="166" y="207" width="20" height="4" fill="#4ade80" stroke="#0f172a" stroke-width="1.3" stroke-linejoin="round"/><rect x="166" y="213" width="20" height="4" fill="#4ade80" stroke="#0f172a" stroke-width="1.3" stroke-linejoin="round"/><rect x="166" y="219" width="20" height="4" fill="#4ade80" stroke="#0f172a" stroke-width="1.3" stroke-linejoin="round"/><rect x="186" y="230" width="16" height="18" fill="#1d4ed8" stroke="#0f172a" stroke-width="1.4" stroke-linejoin="round"/><text x="95" y="234" font-size="11" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">pignon fou</text><text x="305" y="249" font-size="11" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">moyeu</text><text x="22" y="178" font-size="12" font-weight="600" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Temps 1 : synchronisation</text><rect x="20" y="400" width="420" height="12" fill="#e2e8f0" stroke="#0f172a" stroke-width="1.5" stroke-linejoin="round"/><rect x="40" y="340" width="110" height="60" fill="#bfdbfe" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="150" y="350" width="12" height="4" fill="#60a5fa" stroke="#0f172a" stroke-width="1.3" stroke-linejoin="round"/><rect x="150" y="356" width="12" height="4" fill="#60a5fa" stroke="#0f172a" stroke-width="1.3" stroke-linejoin="round"/><rect x="150" y="362" width="12" height="4" fill="#60a5fa" stroke="#0f172a" stroke-width="1.3" stroke-linejoin="round"/><rect x="270" y="372" width="70" height="28" fill="#fde68a" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="150" y="370" width="36" height="22" fill="#e9d5ff" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="172" y="328" width="150" height="12" fill="#bbf7d0" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="172" y="340" width="10" height="28" fill="#bbf7d0" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="152" y="347" width="20" height="4" fill="#4ade80" stroke="#0f172a" stroke-width="1.3" stroke-linejoin="round"/><rect x="152" y="353" width="20" height="4" fill="#4ade80" stroke="#0f172a" stroke-width="1.3" stroke-linejoin="round"/><rect x="152" y="359" width="20" height="4" fill="#4ade80" stroke="#0f172a" stroke-width="1.3" stroke-linejoin="round"/><rect x="186" y="370" width="16" height="18" fill="none" stroke="#0f172a" stroke-width="1.4" stroke-linejoin="round" stroke-dasharray="3 2"/><text x="95" y="374" font-size="11" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">pignon fou</text><text x="305" y="389" font-size="11" font-weight="600" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">moyeu</text><text x="22" y="318" font-size="12" font-weight="600" text-anchor="start" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">Temps 2 : crabotage</text></svg>
:::

| Temps | Ce qui se déplace | Résultat |
| --- | --- | --- |
| 1. Synchronisation | le baladeur pousse la bague par les clavettes | la bague frotte sur le cône ; le pignon fou prend sa vitesse |
| 2. Crabotage | le baladeur poursuit, les clavettes s'effacent | les crabots s'emboîtent ; pignon fou et moyeu sont liés, à la même vitesse |

::: exemple Enclencher la 5e vitesse
1. **Point mort** : le baladeur (18) est au repos, la bague n'est pas en contact avec le pignon fou (5).
2. **Temps 1**, car la bague doit toucher avant tout : on déplace le baladeur vers le pignon fou ; il entraîne la bague par les clavettes ; le **frottement** conique fait tourner le pignon fou comme la bague.
3. **Temps 2**, une fois les vitesses égales : le baladeur poursuit, les clavettes s'effacent, le **crabotage** s'effectue et le pignon fou (5) est lié au moyeu (26).

:::

::: piege Frottement d'abord, obstacle ensuite
Le synchroniseur ne remplace pas le crabotage : il le **prépare**. La synchronisation utilise l'**adhérence** (le frottement du cône), qui peut glisser ; le crabotage utilise l'**obstacle** (les crabots), qui ne glisse pas. Inverser les temps reviendrait à emboîter avant d'avoir égalisé.
:::

::: verifie
À quel temps les vitesses du pignon fou et de la bague s'égalisent-elles, et qu'est-ce qui le permet ?
---
Au **temps 1**, par le **frottement** de la bague sur le cône du pignon fou.
:::

## 🧭 La méthode qui reste : six marches

Devant le moteur et sa chaîne, reprends toujours cet ordre :

1. **Compter les temps** : quatre courses, deux tours, un seul temps moteur.
2. **Transformer** : course c = 2R, cylindrée = volume balayé × nombre de cylindres.
3. **Mesurer le mouvement** : ω = 2πN / 60, V_A = ω R, puis l'équiprojectivité pour V_B.
4. **Commander** : came, poussoir, ressort ; arbre à cames deux fois plus lent que le vilebrequin.
5. **Transmettre** : embrayage (fourchette, butée, diaphragme, plateau), puis boîte (r = produit des Z menante / Z menée) et sens.
6. **Choisir** : baladeur et synchroniseur, synchroniser avant de craboter.

::: retenir
Un moteur à **quatre temps** n'a qu'un temps **moteur** par **deux tours** ; le mécanisme **bielle-manivelle** transforme la translation en rotation avec c = 2R ; la **cylindrée** est le volume balayé fois le nombre de cylindres ; l'**embrayage** relie ou coupe par **adhérence**, la **boîte** adapte par r, et le **synchroniseur** égalise les vitesses **avant** le **crabotage**.
:::

> 🏆 Du piston aux roues, tu as suivi toute la chaîne. La maquette n'a plus de secret : il ne reste qu'à la mettre à l'épreuve.
