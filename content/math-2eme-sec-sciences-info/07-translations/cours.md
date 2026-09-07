# ⚔️ Translations — quand tout le plan se met à glisser

> 💡 «Une seule flèche, et le plan entier part d'un bloc : rien ne s'étire, rien ne tourne, tout se retrouve à l'identique un peu plus loin.»

Jusqu'ici les points restaient sagement en place et c'était le calcul qui bougeait. On change de métier : on fabrique maintenant des **machines à déplacer les points**. La plus simple de toutes, la translation, pousse chaque point du plan dans la même direction, dans le même sens et sur la même longueur. Sa puissance ne tient pas à sa définition, qui s'écrit en une ligne, mais à la liste de tout ce qu'elle **ne casse pas** : longueurs, angles, alignements, milieux, barycentres, tangences. C'est ce catalogue de conservations qui, à la fin du chapitre, réduira des problèmes de lieux et de constructions redoutables à un tracé de deux minutes.

## 🗺️ Une application du plan dans le plan

Avant de déplacer, il faut dire proprement ce que « déplacer » veut dire.

> **Définition (application).** Lorsqu'on associe à tout point M du plan un seul point M', on définit une **application du plan dans lui-même**. Si on désigne par f cette application, alors on écrit f : P → P, M ↦ M'. M' s'appelle l'**image** du point M par l'application f. M s'appelle **antécédent** du point M' par l'application f.

L'**image** est le point d'arrivée, l'**antécédent** le point de départ : ces deux mots ne s'échangent jamais. Et le mot « seul » n'est pas décoratif — un point de départ n'a qu'un seul point d'arrivée, sans quoi le mot « application » ne s'applique pas.

Tu manipules déjà des applications du plan depuis plusieurs années, sans les avoir nommées ainsi.

| l'application                       | ce qu'elle fait au point M                                          |
| ----------------------------------- | ------------------------------------------------------------------- |
| la symétrie centrale de centre I    | son image M' est telle que I est le milieu de [MM']                 |
| la symétrie orthogonale d'axe D     | son image M' est le symétrique de M par rapport à la droite D       |
| le quart de tour direct de centre I | son image M' se déduit de M par un quart de tour autour de I        |
| le quart de tour indirect de centre I | même chose, mais dans l'autre sens de rotation autour de I        |

::: figure La symétrie centrale de centre I fait correspondre au point M un point M' unique : M' est l'image de M, M est l'antécédent de M', et I tombe exactement au milieu — les deux petits traits marquent les deux longueurs égales
<svg viewBox="0 0 320 180">
<path d="M70 50 L250 140" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-dasharray="6 4"/>
<path d="M117.7 67.1 L112.3 77.9 M207.7 112.1 L202.3 122.9" fill="none" stroke="#94a3b8" stroke-width="2"/>
<g fill="#0f172a"><circle cx="70" cy="50" r="5"/><circle cx="250" cy="140" r="5"/></g>
<circle cx="160" cy="95" r="5" fill="#0f6e56"/>
<g font-size="15" font-weight="700" text-anchor="middle" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">
<text x="62" y="38" fill="#0f172a">M</text>
<text x="264" y="158" fill="#0f172a">M'</text>
<text x="160" y="82" fill="#0f6e56">I</text>
</g>
</svg>
:::

## ➡️ La translation de vecteur u⃗

Une application est libre de faire n'importe quoi. La translation, elle, obéit à une consigne d'une simplicité désarmante : **le même vecteur pour tout le monde**.

> **Définition (translation).** Soit u⃗ un vecteur. L'application du plan dans lui-même qui à tout point M associe l'unique point M' tel que MM'⃗ = u⃗ est appelée **translation de vecteur u⃗**. Elle est notée t_u⃗. On écrit t_u⃗ : P → P, M ↦ t_u⃗(M) = M'.
>
> $$ t_u⃗(M) = M' ⟺ MM'⃗ = u⃗ $$

Le vecteur se lit **de l'antécédent vers l'image**, jamais dans l'autre sens : c'est MM'⃗ qui vaut u⃗, pas M'M⃗.

::: figure Trois points quelconques et leurs images : les trois flèches ont la même direction, le même sens et la même longueur que u⃗ — c'est tout le plan qui part d'un bloc, pas seulement ces trois points
<svg viewBox="0 0 340 220">
<g fill="none" stroke="#0f6e56" stroke-width="2" stroke-dasharray="6 4">
<path d="M70 55 L160.9 27.7"/><path d="M135 120 L225.9 92.7"/><path d="M85 165 L175.9 137.7"/>
</g>
<g fill="#0f6e56"><polygon points="170,25 160.9,32.9 158.0,23.4"/><polygon points="235,90 225.9,97.9 223.0,88.4"/><polygon points="185,135 175.9,142.9 173.0,133.4"/></g>
<path d="M30 200 L120.4 172.9" fill="none" stroke="#0f172a" stroke-width="3"/>
<polygon points="130,170 120.9,177.9 118.0,168.4" fill="#0f172a"/>
<g fill="#0f172a"><circle cx="70" cy="55" r="4.5"/><circle cx="135" cy="120" r="4.5"/><circle cx="85" cy="165" r="4.5"/></g>
<g fill="#0f6e56"><circle cx="170" cy="25" r="4.5"/><circle cx="235" cy="90" r="4.5"/><circle cx="185" cy="135" r="4.5"/></g>
<g font-size="15" font-weight="700" text-anchor="middle" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">
<text x="58" y="48" fill="#0f172a">M</text><text x="182" y="18" fill="#0f6e56">M'</text>
<text x="124" y="113" fill="#0f172a">N</text><text x="248" y="84" fill="#0f6e56">N'</text>
<text x="73" y="158" fill="#0f172a">P</text><text x="197" y="130" fill="#0f6e56">P'</text>
<text x="75" y="212" fill="#0f172a">u⃗</text>
</g>
</svg>
:::

> **Remarque (l'antécédent existe et il est unique).** Donne-toi un point M' quelconque. Le point M tel que MM'⃗ = u⃗ est entièrement déterminé : **tout point du plan admet un antécédent, et un seul**, par une translation. Rien ne se perd, rien ne se dédouble.

_Exemple détaillé (d'où sortent les translations)_ : prends deux points distincts I et J. Applique à un point M la symétrie centrale de centre I, ce qui donne M₁, puis à M₁ la symétrie centrale de centre J, ce qui donne M'. Comme I est le milieu de [MM₁], on a MM₁⃗ = 2MI⃗ ; comme J est le milieu de [M₁M'], on a M₁M'⃗ = 2M₁J⃗. En écrivant enfin M₁J⃗ = M₁I⃗ + IJ⃗ = −MI⃗ + IJ⃗, il vient

$$ MM'⃗ = 2MI⃗ + 2(−MI⃗ + IJ⃗) = 2IJ⃗ $$

Le résultat ne dépend plus du point M : **enchaîner deux symétries centrales, c'est effectuer la translation de vecteur 2IJ⃗**.

## 🔑 La propriété caractéristique — la clé du chapitre

Voici l'énoncé qui sert dans presque tous les exercices : il reconnaît une translation sans jamais avoir à deviner son vecteur.

> **Propriété caractéristique.** Soit f une application du plan dans lui-même, qui à M associe M' et à N associe N'. Alors
>
> $$ f est une translation ⟺ M'N'⃗ = MN⃗ pour tous points M et N $$

Le sens direct dit qu'une translation transporte le vecteur MN⃗ sans le modifier ; la réciproque dit que **cette seule condition suffit** à garantir qu'on a affaire à une translation.

> **Conséquence.** Une translation **conserve les distances** : MN = M'N'. Elle **conserve le parallélisme** : les droites (MN) et (M'N') sont parallèles. Et si les quatre points ne sont pas alignés, le quadrilatère MM'N'N est un **parallélogramme**.

::: figure Le segment [M'N'] se déduit de [MN] sans déformation : les deux flèches grises portent le même vecteur, donc M'N'⃗ = MN⃗ et le quadrilatère MM'N'N a ses côtés opposés parallèles et de même longueur
<svg viewBox="0 0 320 200">
<path d="M60 60 L130 145" fill="none" stroke="#0f172a" stroke-width="2.2"/>
<path d="M190 45 L260 130" fill="none" stroke="#0f6e56" stroke-width="2.6"/>
<g fill="none" stroke="#94a3b8" stroke-width="1.8" stroke-dasharray="6 4">
<path d="M60 60 L180.1 46.1"/><path d="M130 145 L250.1 131.1"/>
</g>
<g fill="#94a3b8"><polygon points="190,45 180.6,50.6 179.6,41.7"/><polygon points="260,130 250.6,135.6 249.6,126.7"/></g>
<g fill="#0f172a"><circle cx="60" cy="60" r="4.5"/><circle cx="130" cy="145" r="4.5"/></g>
<g fill="#0f6e56"><circle cx="190" cy="45" r="4.5"/><circle cx="260" cy="130" r="4.5"/></g>
<g font-size="15" font-weight="700" text-anchor="middle" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">
<text x="48" y="52" fill="#0f172a">M</text>
<text x="118" y="162" fill="#0f172a">N</text>
<text x="200" y="36" fill="#0f6e56">M'</text>
<text x="274" y="140" fill="#0f6e56">N'</text>
</g>
</svg>
:::

**Reconnaître une translation cachée dans une somme vectorielle.** Quand une application est décrite par une égalité du type MM'⃗ = somme de vecteurs partant de M, il suffit de vérifier que cette somme **ne dépend pas de M**. Le chapitre du barycentre a donné le critère : une somme pondérée dont les coefficients totalisent **zéro** est un vecteur constant.

_Exemple détaillé_ : A, B et C sont trois points fixes, et à tout point M on associe M' tel que MM'⃗ = MA⃗ + MB⃗ − 2MC⃗. Les coefficients 1, 1 et −2 totalisent 0. On ramène tout au point C, avec MA⃗ = MC⃗ + CA⃗ et MB⃗ = MC⃗ + CB⃗ :

$$ MM'⃗ = (1 + 1 − 2)MC⃗ + CA⃗ + CB⃗ = CA⃗ + CB⃗ $$

Le point M a disparu : l'application est la **translation de vecteur CA⃗ + CB⃗**.

_Exemple détaillé (une variante à connaître)_ : A et B sont fixes, et à tout point M on associe N tel que AN⃗ = 3AM⃗ − 2BM⃗. Alors MN⃗ = AN⃗ − AM⃗ = 2AM⃗ − 2BM⃗ = 2(AM⃗ − BM⃗) = 2AB⃗. Ce vecteur est constant : c'est la **translation de vecteur 2AB⃗**.

> ⚠️ **Attention au sens — deux cas se ressemblent et ne donnent pas le même résultat.**
> Ici les deux vecteurs ont la **même extrémité** M : AM⃗ − BM⃗ = AM⃗ + MB⃗ = **AB⃗**, on va donc du
> **premier point de départ vers le second**. C'est l'inverse du cas où les deux vecteurs ont la
> **même origine** : MS⃗ − MT⃗ = MS⃗ + TM⃗ = **TS⃗**, où l'on va de la seconde extrémité vers la
> première. Dans les deux cas, la seule chose à faire est d'appliquer Chasles ; retenir un sens
> sans regarder quelle lettre est commune, c'est se tromper une fois sur deux.

> ⚠️ Une somme de coefficients nulle ne signifie pas la même chose ici et au chapitre précédent. Là-bas, elle interdisait l'existence d'un barycentre ; ici, c'est exactement elle qui **garantit** que le vecteur est constant, donc qu'on tient une translation.

## 🛡️ Tout ce qu'une translation conserve

C'est le cœur du chapitre, et il tient dans un tableau. Chaque ligne est un outil de démonstration à part entière.

| ce qui est conservé  | l'énoncé officiel                                                                                     |
| -------------------- | ------------------------------------------------------------------------------------------------------ |
| les distances        | A'B' = AB pour tous points A et B                                                                     |
| les angles           | une translation conserve les mesures d'angles                                                         |
| l'alignement         | les images, par une translation, de points alignés sont des points alignés                            |
| le milieu            | l'image du milieu de [AB] est le milieu de [A'B']                                                     |
| le barycentre        | l'image du barycentre de (A, α) et (B, β) est le barycentre de (A', α) et (B', β)                     |
| le parallélisme      | les images de deux droites parallèles sont deux droites parallèles                                    |
| l'orthogonalité      | les images de deux droites perpendiculaires sont deux droites perpendiculaires                        |
| le contact           | les images d'une droite et d'un cercle tangents sont une droite et un cercle tangents                 |

> **Retenir (conservation des grandeurs).** Une translation conserve les distances. Une translation conserve les angles. L'image d'un polygone par une translation est un polygone qui lui est **superposable**.

_Exemple détaillé_ : le triangle ABC a pour périmètre 21 cm et son angle en B mesure 35°. Son image A'B'C' par n'importe quelle translation a donc pour périmètre 21 cm et un angle en B' de 35°. La longueur du vecteur de la translation n'intervient **jamais** dans ces valeurs : elle dit où la figure est allée, pas comment elle a changé — puisqu'elle n'a pas changé.

> 🗡️ Les coefficients d'un barycentre ne bougent pas non plus. Si G est le barycentre de (A, 3) et (B, 4), son image G' est le barycentre de (A', 3) et (B', 4) — les mêmes coefficients, appliqués aux points images.

## 🎯 Les images des objets usuels

Conserver les grandeurs, c'est bien ; savoir dessiner l'image d'une figure entière, c'est mieux.

| l'objet                            | son image par la translation de vecteur u⃗                                     |
| ---------------------------------- | ------------------------------------------------------------------------------- |
| une droite D                       | une droite parallèle à D                                                       |
| un segment [AB]                    | le segment [A'B'], de même longueur que [AB]                                   |
| une demi-droite                    | une demi-droite, d'origine l'image de l'origine                                 |
| un cercle de centre O et de rayon r | le cercle de **même rayon** r, de centre l'image de O                          |

Le cas du cercle mérite une phrase à lui seul : **le rayon ne change pas**, seul le centre voyage. Une translation ne grossit ni ne rétrécit quoi que ce soit — c'est un simple glissement.

::: figure Le cercle image a exactement le même rayon que le cercle de départ : seul son centre a glissé du vecteur de la translation, et tout point du premier cercle glisse du même vecteur pour atterrir sur le second
<svg viewBox="0 0 340 220">
<circle cx="85" cy="115" r="52" fill="none" stroke="#0f172a" stroke-width="2.2"/>
<circle cx="225" cy="115" r="52" fill="#0f6e56" opacity="0.12"/>
<circle cx="225" cy="115" r="52" fill="none" stroke="#0f6e56" stroke-width="2.6"/>
<path d="M85 115 L48.2 78.2" fill="none" stroke="#0f172a" stroke-width="1.6"/>
<path d="M225 115 L188.2 78.2" fill="none" stroke="#0f6e56" stroke-width="1.6"/>
<g fill="none" stroke="#94a3b8" stroke-width="1.8" stroke-dasharray="6 4"><path d="M85 115 L215 115"/><path d="M48.2 78.2 L178.2 78.2"/></g>
<g fill="#94a3b8"><polygon points="225,115 215,119.5 215,110.5"/><polygon points="188.2,78.2 178.2,82.7 178.2,73.7"/></g>
<g fill="#0f172a"><circle cx="85" cy="115" r="4.5"/><circle cx="48.2" cy="78.2" r="4.5"/></g>
<g fill="#0f6e56"><circle cx="225" cy="115" r="4.5"/><circle cx="188.2" cy="78.2" r="4.5"/></g>
<g font-size="15" font-weight="700" text-anchor="middle" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">
<text x="76" y="134" fill="#0f172a">O</text>
<text x="36" y="70" fill="#0f172a">M</text>
<text x="216" y="134" fill="#0f6e56">O'</text>
<text x="178" y="70" fill="#0f6e56">M'</text>
</g>
</svg>
:::

_Exemple détaillé (la médiatrice)_ : la médiatrice de [AB] est la droite perpendiculaire à (AB) passant par le milieu de [AB]. Une translation conserve le milieu **et** l'orthogonalité : l'image de cette droite est donc perpendiculaire à (A'B') et passe par le milieu de [A'B']. L'image de la médiatrice de [AB] est la **médiatrice de [A'B']**.

> ⚠️ Ne confonds pas « l'image de la droite (AB) » et « la droite des images ». Ce sont heureusement les mêmes ici, mais l'image d'une droite est bien la **droite entière** décrite par les images de tous ses points, pas seulement le segment que tu as tracé.

## 🔎 Lieux et constructions : la translation comme méthode

Deux familles de problèmes se résolvent presque mécaniquement dès qu'on repère la bonne translation.

**Les problèmes de lieux.** On cherche l'**ensemble des points** vérifiant une condition — on dit aussi le **lieu géométrique** de ces points. La méthode du manuel tient en trois temps : une **phase expérimentale** (on place plusieurs positions et on observe), une **conjecture** (on nomme la figure obtenue), puis la **démonstration** (on prouve que le point cherché est l'image d'un point connu par une translation fixe).

_Exemple détaillé_ : le point M décrit un cercle de centre O et de rayon 4 cm, et le point N est défini par MN⃗ = u⃗, où u⃗ est un vecteur fixé. Alors N est l'image de M par la translation de vecteur u⃗. Quand M parcourt tout le cercle, N parcourt donc son image : le lieu de N est le **cercle de rayon 4 cm centré en l'image de O**.

**Les problèmes de construction.** On y raisonne par **analyse et synthèse** : on *suppose le problème résolu*, on lit sur la figure la translation qui relie les inconnues, on en déduit un tracé, puis on vérifie que ce tracé répond bien à la question.

_Exemple détaillé_ : deux droites D et Δ et deux points A et B sont donnés ; on cherche M sur D et N sur Δ tels que ABMN soit un parallélogramme. Supposons-le construit. ABMN est un parallélogramme signifie AB⃗ = NM⃗, c'est-à-dire que M est l'image de N par la translation de vecteur AB⃗. Comme N décrit Δ, le point M appartient à l'**image de Δ** par cette translation. Il appartient aussi à D : on le trouve donc à l'intersection de D et de cette image, et N s'en déduit en remontant le vecteur.

::: figure L'image Δ' de la droite Δ (en pointillés) coupe la droite D exactement au point M cherché ; il ne reste qu'à revenir en arrière du vecteur AB⃗ pour placer N sur Δ, et ABMN est bien un parallélogramme
<svg viewBox="0 0 340 210">
<polygon points="35,60 125,25 222,107 132,142" fill="#0f6e56" opacity="0.12"/>
<path d="M30 190 L251 86" fill="none" stroke="#0f172a" stroke-width="2.2"/>
<path d="M157 3 L272 187" fill="none" stroke="#0f172a" stroke-width="2.2"/>
<path d="M120 155 L307 67" fill="none" stroke="#0f6e56" stroke-width="2.2" stroke-dasharray="7 5"/>
<polygon points="35,60 125,25 222,107 132,142" fill="none" stroke="#0f6e56" stroke-width="2"/>
<g fill="#0f172a"><circle cx="35" cy="60" r="4.5"/><circle cx="125" cy="25" r="4.5"/></g>
<g fill="#0f6e56"><circle cx="222" cy="107" r="5"/><circle cx="132" cy="142" r="5"/></g>
<g font-size="15" font-weight="700" text-anchor="middle" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">
<text x="24" y="53" fill="#0f172a">A</text>
<text x="133" y="18" fill="#0f172a">B</text>
<text x="234" y="100" fill="#0f6e56">M</text>
<text x="122" y="158" fill="#0f6e56">N</text>
<text x="22" y="202" fill="#0f172a">Δ</text>
<text x="283" y="197" fill="#0f172a">D</text>
<text x="318" y="60" fill="#0f6e56">Δ'</text>
</g>
</svg>
:::

_Exemple détaillé (le triangle des milieux)_ : dans un triangle ABC, appelle K le milieu de [AB] et J le milieu de [AC]. Alors KJ⃗ = AJ⃗ − AK⃗ = ½AC⃗ − ½AB⃗ = **½BC⃗** : le segment qui joint deux milieux porte exactement la moitié du troisième côté, et il devient donc le vecteur d'une translation toute trouvée. C'est ce genre de lecture qui permet de reconstruire un triangle dont on ne connaît que les milieux de ses côtés.

**Le problème du pont.** Deux berges parallèles séparent une ville A d'une ville B ; le pont [MN] doit traverser perpendiculairement aux berges, donc le vecteur MN⃗ est **le même quelle que soit la position choisie**. Le trajet AM + MN + NB ne peut être raccourci que sur AM + NB, puisque MN est fixe. On translate A du vecteur MN⃗ en un point A' : alors AM = A'N, et le trajet à minimiser devient A'N + NB, minimal lorsque N appartient au segment [A'B]. Il suffit donc de joindre A' à B.

::: figure Une fois A translaté du vecteur du pont en A', le trajet à raccourcir devient une simple ligne brisée A'-N-B : elle est la plus courte quand elle est droite, ce qui place N à l'intersection de [A'B] avec la berge opposée
<svg viewBox="0 0 340 230">
<rect x="20" y="90" width="300" height="40" fill="#bae6fd"/>
<path d="M20 90 H320 M20 130 H320" fill="none" stroke="#0f172a" stroke-width="2"/>
<path d="M60 40 L160 90" fill="none" stroke="#0f172a" stroke-width="2.2"/>
<path d="M160 130 L290 195" fill="none" stroke="#0f172a" stroke-width="2.2"/>
<path d="M160 90 L160 130" fill="none" stroke="#0f6e56" stroke-width="4"/>
<path d="M60 40 L60 69" fill="none" stroke="#94a3b8" stroke-width="1.8" stroke-dasharray="6 4"/>
<polygon points="60,80 55,69 65,69" fill="#94a3b8"/>
<path d="M60 80 L290 195" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-dasharray="4 4"/>
<path d="M160 102 L172 102 L172 90" fill="none" stroke="#0f6e56" stroke-width="1.6"/>
<g fill="#0f172a"><circle cx="60" cy="40" r="4.5"/><circle cx="290" cy="195" r="4.5"/></g>
<g fill="#0f6e56"><circle cx="160" cy="90" r="4.5"/><circle cx="160" cy="130" r="4.5"/></g>
<circle cx="60" cy="80" r="4.5" fill="#94a3b8"/>
<g font-size="15" font-weight="700" text-anchor="middle" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">
<text x="50" y="32" fill="#0f172a">A</text>
<text x="302" y="207" fill="#0f172a">B</text>
<text x="146" y="84" fill="#0f6e56">M</text>
<text x="146" y="148" fill="#0f6e56">N</text>
<text x="42" y="90" fill="#94a3b8">A'</text>
</g>
</svg>
:::

## 🏛️ Math et culture : paver le plan

**Paver**, c'est couvrir le plan avec des figures identiques, sans laisser de trou et sans chevauchement — exactement ce que fait une translation répétée. Trois polygones réguliers seulement y parviennent seuls : le **triangle équilatéral**, le **carré** et l'**hexagone régulier**. La raison est arithmétique : les angles réunis en un même sommet doivent totaliser 360°, et 360 doit donc être un multiple de l'angle du polygone — ce qui marche pour 60°, 90° et 120°, mais pas pour les 108° du pentagone régulier.

::: figure Trois hexagones se rejoignent en chaque sommet, marqué ici en couleur : leurs trois angles de 120° totalisent exactement 360°, et c'est pour cela que le pavage se referme sans trou
<svg viewBox="0 0 315 220">
<g fill="#0f6e56" opacity="0.10"><path d="M75.0 45.0 L60.0 71.0 L30.0 71.0 L15.0 45.0 L30.0 19.0 L60.0 19.0 ZM75.0 97.0 L60.0 122.9 L30.0 122.9 L15.0 97.0 L30.0 71.0 L60.0 71.0 ZM75.0 148.9 L60.0 174.9 L30.0 174.9 L15.0 148.9 L30.0 122.9 L60.0 122.9 ZM120.0 71.0 L105.0 97.0 L75.0 97.0 L60.0 71.0 L75.0 45.0 L105.0 45.0 ZM120.0 122.9 L105.0 148.9 L75.0 148.9 L60.0 122.9 L75.0 97.0 L105.0 97.0 ZM120.0 174.9 L105.0 200.9 L75.0 200.9 L60.0 174.9 L75.0 148.9 L105.0 148.9 ZM165.0 45.0 L150.0 71.0 L120.0 71.0 L105.0 45.0 L120.0 19.0 L150.0 19.0 ZM165.0 97.0 L150.0 122.9 L120.0 122.9 L105.0 97.0 L120.0 71.0 L150.0 71.0 ZM165.0 148.9 L150.0 174.9 L120.0 174.9 L105.0 148.9 L120.0 122.9 L150.0 122.9 ZM210.0 71.0 L195.0 97.0 L165.0 97.0 L150.0 71.0 L165.0 45.0 L195.0 45.0 ZM210.0 122.9 L195.0 148.9 L165.0 148.9 L150.0 122.9 L165.0 97.0 L195.0 97.0 ZM210.0 174.9 L195.0 200.9 L165.0 200.9 L150.0 174.9 L165.0 148.9 L195.0 148.9 ZM255.0 45.0 L240.0 71.0 L210.0 71.0 L195.0 45.0 L210.0 19.0 L240.0 19.0 ZM255.0 97.0 L240.0 122.9 L210.0 122.9 L195.0 97.0 L210.0 71.0 L240.0 71.0 ZM255.0 148.9 L240.0 174.9 L210.0 174.9 L195.0 148.9 L210.0 122.9 L240.0 122.9 ZM300.0 71.0 L285.0 97.0 L255.0 97.0 L240.0 71.0 L255.0 45.0 L285.0 45.0 ZM300.0 122.9 L285.0 148.9 L255.0 148.9 L240.0 122.9 L255.0 97.0 L285.0 97.0 ZM300.0 174.9 L285.0 200.9 L255.0 200.9 L240.0 174.9 L255.0 148.9 L285.0 148.9 Z"/></g>
<g fill="none" stroke="#0f172a" stroke-width="1.6" stroke-linejoin="round"><path d="M75.0 45.0 L60.0 71.0 L30.0 71.0 L15.0 45.0 L30.0 19.0 L60.0 19.0 ZM75.0 97.0 L60.0 122.9 L30.0 122.9 L15.0 97.0 L30.0 71.0 L60.0 71.0 ZM75.0 148.9 L60.0 174.9 L30.0 174.9 L15.0 148.9 L30.0 122.9 L60.0 122.9 ZM120.0 71.0 L105.0 97.0 L75.0 97.0 L60.0 71.0 L75.0 45.0 L105.0 45.0 ZM120.0 122.9 L105.0 148.9 L75.0 148.9 L60.0 122.9 L75.0 97.0 L105.0 97.0 ZM120.0 174.9 L105.0 200.9 L75.0 200.9 L60.0 174.9 L75.0 148.9 L105.0 148.9 ZM165.0 45.0 L150.0 71.0 L120.0 71.0 L105.0 45.0 L120.0 19.0 L150.0 19.0 ZM165.0 97.0 L150.0 122.9 L120.0 122.9 L105.0 97.0 L120.0 71.0 L150.0 71.0 ZM165.0 148.9 L150.0 174.9 L120.0 174.9 L105.0 148.9 L120.0 122.9 L150.0 122.9 ZM210.0 71.0 L195.0 97.0 L165.0 97.0 L150.0 71.0 L165.0 45.0 L195.0 45.0 ZM210.0 122.9 L195.0 148.9 L165.0 148.9 L150.0 122.9 L165.0 97.0 L195.0 97.0 ZM210.0 174.9 L195.0 200.9 L165.0 200.9 L150.0 174.9 L165.0 148.9 L195.0 148.9 ZM255.0 45.0 L240.0 71.0 L210.0 71.0 L195.0 45.0 L210.0 19.0 L240.0 19.0 ZM255.0 97.0 L240.0 122.9 L210.0 122.9 L195.0 97.0 L210.0 71.0 L240.0 71.0 ZM255.0 148.9 L240.0 174.9 L210.0 174.9 L195.0 148.9 L210.0 122.9 L240.0 122.9 ZM300.0 71.0 L285.0 97.0 L255.0 97.0 L240.0 71.0 L255.0 45.0 L285.0 45.0 ZM300.0 122.9 L285.0 148.9 L255.0 148.9 L240.0 122.9 L255.0 97.0 L285.0 97.0 ZM300.0 174.9 L285.0 200.9 L255.0 200.9 L240.0 174.9 L255.0 148.9 L285.0 148.9 Z"/></g>
<circle cx="75" cy="97" r="6" fill="#b45309"/>
</svg>
:::

Ces motifs répétés ont nourri un art entier : les **mosaïques** de Rome et de Byzance, puis les pavages géométriques de Grenade, de Séville et du Maroc, où le procédé atteint son sommet.

> 🏆 Quête franchie, héros : tu sais reconnaître une application, définir une translation par son vecteur, la démasquer derrière une somme vectorielle constante, énumérer tout ce qu'elle conserve, dessiner l'image d'une droite, d'un segment ou d'un cercle, et t'en servir pour trouver un lieu ou réussir une construction. Au chapitre suivant, l'application ne se contentera plus de glisser : elle agrandira et réduira les figures.
