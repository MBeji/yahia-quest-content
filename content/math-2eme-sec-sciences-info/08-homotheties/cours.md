# ⚔️ Homothéties — agrandir et réduire sans déformer

> 💡 «Un point fixe, un nombre, et tout le plan se dilate. Les droites restent droites, les parallèles restent parallèles, les angles ne bougent pas : seules les longueurs changent, et toutes dans le même rapport.»

Une **application du plan** associe à chaque point M un unique point M', appelé son image. Tu en connais déjà plusieurs, et elles ont un point commun : elles déplacent la figure sans jamais changer sa taille. L'homothétie fait autre chose. Elle règle un **zoom** : elle conserve la forme et détruit la taille, ce qui en fait l'outil naturel des agrandissements, des réductions, des échelles — et, plus inattendu, des démonstrations d'alignement.

## 🔍 D'où vient l'idée : le zoom du plan

Prends un trapèze ABCD et applique-lui deux traitements. Le premier le fait glisser : chaque sommet part dans la même direction, sur la même longueur. Le second l'éloigne d'un point fixe I en doublant chaque distance : IA'⃗ = 2IA⃗, IB'⃗ = 2IB⃗, et ainsi de suite.

Compare les résultats. Dans les deux cas, la figure obtenue a la **même forme** que la figure de départ, et ses côtés sont **parallèles** aux côtés d'origine. Mais dans le premier cas les longueurs, le périmètre et l'aire sont **inchangés** ; dans le second, chaque longueur a **doublé**, le périmètre aussi — et l'aire, elle, a été **multipliée par 4**. C'est ce second traitement que l'on appelle une homothétie.

> 🗡️ Le **pantographe** est la version en bois de ce chapitre : un parallélogramme articulé qui, pendant que la pointe N suit un dessin, fait tracer par la pointe M une figure homothétique de celle-ci. Employé dès la fin du XVIᵉ siècle, il a reçu sa forme actuelle de Langlois en 1743, et le rapport de la reproduction se règle en déplaçant un simple point de fixation le long d'une des tiges.

## 🎯 L'homothétie : un centre, un rapport

> **Définition (homothétie).** Soit I un point du plan et k un réel **non nul**. L'application qui à tout point M du plan associe l'unique point M' tel que
>
> $$ IM'⃗ = kIM⃗ $$
>
> est appelée **homothétie de centre I et de rapport k**. On la note h_(I,k). Ainsi h_(I,k)(M) = M' équivaut à IM'⃗ = kIM⃗. Le point M' est l'**image** de M ; le point M est l'**antécédent** de M'.

Deux données suffisent donc à décrire complètement la transformation : **le centre** (un point) et **le rapport** (un réel non nul). Tout le reste en découle.

> **Retenir (les conséquences immédiates).**
>
> - Un point et son image sont **alignés avec le centre** : IM'⃗ est un multiple de IM⃗.
> - Le centre est son propre image : **h_(I,k)(I) = I**. On dit que I est le **point invariant** de l'homothétie.
> - L'égalité se retourne : IM'⃗ = kIM⃗ équivaut à IM⃗ = (1/k)IM'⃗. Tout point admet donc **un unique antécédent**, et la transformation qui ramène M' sur M est l'homothétie de **même centre** et de rapport **1/k**.

::: figure Le rapport k commande deux choses à la fois : le côté et la taille. Avec k = 2 l'image M₁ reste du côté de M et s'éloigne deux fois plus de I ; avec k = −1,5 l'image M₂ passe de l'autre côté de I. Dans les deux cas I, M et l'image sont alignés
<svg viewBox="0 0 340 210">
<path d="M60 178.3 L292 43" fill="none" stroke="#94a3b8" stroke-width="1.6"/>
<g fill="#0f172a"><circle cx="160" cy="120" r="5"/><circle cx="220" cy="85" r="5"/></g>
<g fill="#0f6e56"><circle cx="280" cy="50" r="5"/><circle cx="70" cy="172.5" r="5"/></g>
<g font-size="15" font-weight="700" text-anchor="middle" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">
<text x="152" y="140" fill="#0f172a">I</text>
<text x="228" y="76" fill="#0f172a">M</text>
<text x="286" y="42" fill="#0f6e56">M₁</text>
<text x="62" y="192" fill="#0f6e56">M₂</text>
</g>
<g font-size="11" fill="#94a3b8" text-anchor="middle">
<text x="258" y="86">k = 2</text>
<text x="118" y="152">k = −1,5</text>
</g>
</svg>
:::

Le signe de k dit **de quel côté** de I se place l'image ; la valeur absolue de k dit **de combien** on s'éloigne du centre. Quatre situations se présentent, et il faut savoir les lire d'un coup d'œil.

| valeur de k | position de M' | effet sur les longueurs |
| --- | --- | --- |
| k > 1 | du même côté de I que M, plus loin | agrandissement |
| k = 1 | M' = M : l'application ne bouge rien | aucune |
| 0 < k < 1 | du même côté de I que M, plus près | réduction |
| k < 0 | de l'autre côté de I | agrandissement si k < −1, réduction si −1 < k < 0 |

> ⚠️ Le cas **k = −1** mérite son nom : IM'⃗ = −IM⃗ signifie que I est le milieu de [MM']. L'homothétie de rapport −1 n'est rien d'autre que la **symétrie centrale** de centre I.

_Exemple détaillé_ : h est l'homothétie de centre I et de rapport −3, et A un point tel que IA = 2 cm. Alors IA'⃗ = −3IA⃗ : le point A' se trouve sur la droite (IA), **de l'autre côté** de I, à la distance IA' = |−3| × 2 = 6 cm. Le signe a choisi le côté, la valeur absolue a fixé la distance.

## 📐 Construire l'image, retrouver le centre

**Construire l'image d'un point** est immédiat : on trace la droite (IM), puis on y reporte la longueur |k| × IM à partir de I, du bon côté. Pour k = 3 on reporte trois fois IM au-delà de M ; pour k = 1/2 on prend le milieu de [IM] ; pour k = −2 on repart de I dans l'autre sens sur une longueur double.

**Retrouver le centre** est le problème inverse, et c'est lui qui sert dans les exercices. On connaît deux points A et B et leurs images A' et B' ; on cherche I.

> **Retenir (construction du centre).** Si A' et B' sont les images de deux points distincts A et B par une homothétie, alors le centre de cette homothétie est le **point d'intersection des droites (AA') et (BB')**.

La raison est directement la définition : le centre est aligné avec A et A', donc il est sur (AA') ; il est aligné avec B et B', donc il est sur (BB'). Comme ces deux droites ne sont pas parallèles dès que la figure n'est pas dégénérée, elles se coupent en un seul point, qui est le centre cherché.

::: figure Les deux droites (AA') et (BB') se coupent au centre I de l'homothétie : c'est ainsi qu'on le construit quand il n'est pas donné. Ici le rapport vaut 2, et l'on voit déjà que le segment [A'B'] est parallèle à [AB] et deux fois plus long
<svg viewBox="0 0 340 230">
<path d="M75 205 L286 142" fill="none" stroke="#94a3b8" stroke-width="1.4"/>
<path d="M75 205 L229 40" fill="none" stroke="#94a3b8" stroke-width="1.4"/>
<path d="M165 178 L145 130" fill="none" stroke="#0f172a" stroke-width="2.4"/>
<path d="M255 151 L215 55" fill="none" stroke="#0f6e56" stroke-width="2.4"/>
<g fill="#0f172a"><circle cx="75" cy="205" r="5"/><circle cx="165" cy="178" r="4"/><circle cx="145" cy="130" r="4"/></g>
<g fill="#0f6e56"><circle cx="255" cy="151" r="4"/><circle cx="215" cy="55" r="4"/></g>
<g font-size="15" font-weight="700" text-anchor="middle" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">
<text x="66" y="222" fill="#0f172a">I</text>
<text x="174" y="194" fill="#0f172a">A</text>
<text x="132" y="124" fill="#0f172a">B</text>
<text x="266" y="164" fill="#0f6e56">A'</text>
<text x="224" y="46" fill="#0f6e56">B'</text>
</g>
</svg>
:::

> 🗡️ Une fois le centre trouvé, le rapport se lit sur n'importe quel couple de points correspondants : sa **valeur absolue** est le quotient IA'/IA, et son **signe** est positif si A et A' sont du même côté de I, négatif sinon.

## ⚡ La propriété caractéristique

Voici le théorème qui fait tout le travail. Il transforme une information sur **les points** en une information sur **les vecteurs**, et c'est de lui que découlent toutes les conservations du chapitre.

> **Retenir (propriété caractéristique).** Si M' et N' sont les images respectives de M et N par l'homothétie de rapport k, alors
>
> $$ M'N'⃗ = kMN⃗ $$

La démonstration tient en une ligne de Chasles : M'N'⃗ = M'I⃗ + IN'⃗ = −kIM⃗ + kIN⃗ = k(IN⃗ − IM⃗) = kMN⃗.

> **Retenir (les deux conséquences).** Si A' et B' sont les images de A et B par une homothétie de rapport k, alors
>
> $$ (AB) est parallèle à (A'B') et A'B' = |k| × AB $$

Lis bien ces deux résultats : le premier porte sur les **vecteurs** et garde le signe de k ; le second porte sur des **longueurs**, qui sont positives, et ne retient donc que **|k|**.

> ⚠️ C'est l'erreur numéro un du chapitre. Avec k = −4 et AB = 3 cm, on a A'B'⃗ = −4AB⃗ — un vecteur de sens contraire — mais A'B' = 4 × 3 = **12 cm**, jamais «−12 cm». Une longueur ne peut pas être négative.

_Exemple détaillé_ : ABC est un triangle tel que AB = 5 cm, et A'B'C' son image par une homothétie de rapport −2/5. Alors A'B'⃗ = −(2/5)AB⃗ : les deux vecteurs sont de sens contraires, les droites (AB) et (A'B') sont parallèles, et A'B' = (2/5) × 5 = 2 cm. Le rapport étant négatif de valeur absolue plus petite que 1, la figure image est à la fois **retournée** et **réduite**.

## 🛡️ Ce qu'une homothétie conserve — et ce qu'elle change

Le tableau suivant est à connaître par cœur : il répond d'avance à la moitié des questions du chapitre.

| objet de départ | image par h_(I,k) |
| --- | --- |
| une droite D ne passant pas par I | une droite parallèle à D, distincte de D |
| une droite passant par I | **elle-même** (globalement invariante) |
| un segment [AB] | le segment [A'B'], dont la longueur est AB multipliée par la valeur absolue de k |
| une demi-droite | une demi-droite de même direction |
| un cercle de centre O et de rayon R | le cercle de centre h(O), de rayon R multiplié par la **valeur absolue de k** |

> **Retenir (les sept conservations).** Une homothétie conserve **l'alignement**, **le milieu**, **le barycentre**, les **mesures d'angles**, le **parallélisme**, l'**orthogonalité** et le **contact** (deux figures tangentes ont des images tangentes).

Deux remarques que l'on oublie souvent. D'abord, «conserver les angles» veut dire que l'image d'un angle de 40° est un angle de 40° — le rapport k n'intervient **pas** : c'est bien pour cela que la figure image a la même **forme**. Ensuite, «conserver le barycentre» prolonge exactement le chapitre précédent sur les points pondérés : l'image du barycentre de (A, α) et (B, β) est le barycentre de (A', α) et (B', β), **avec les mêmes coefficients**.

::: figure L'image d'un cercle est un cercle : ici le rapport vaut 2, donc le centre O part en O' = h(O) et le rayon double. Le point M du cercle a pour image le point M' du cercle image, et les trois points I, O et O' sont alignés, comme le sont I, M et M'
<svg viewBox="0 0 340 220">
<path d="M25 195 L186 91.5" fill="none" stroke="#94a3b8" stroke-width="1.4"/>
<path d="M25 195 L179 19" fill="none" stroke="#94a3b8" stroke-width="1.4"/>
<circle cx="95" cy="150" r="35" fill="none" stroke="#0f172a" stroke-width="2.2"/>
<circle cx="165" cy="105" r="70" fill="#0f6e56" opacity="0.10"/>
<circle cx="165" cy="105" r="70" fill="none" stroke="#0f6e56" stroke-width="2.2"/>
<g fill="#0f172a"><circle cx="25" cy="195" r="5"/><circle cx="95" cy="150" r="4"/><circle cx="95" cy="115" r="4"/></g>
<g fill="#0f6e56"><circle cx="165" cy="105" r="4"/><circle cx="165" cy="35" r="4"/></g>
<g font-size="15" font-weight="700" text-anchor="middle" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">
<text x="18" y="212" fill="#0f172a">I</text>
<text x="84" y="146" fill="#0f172a">O</text>
<text x="84" y="110" fill="#0f172a">M</text>
<text x="154" y="100" fill="#0f6e56">O'</text>
<text x="156" y="28" fill="#0f6e56">M'</text>
</g>
</svg>
:::

_Exemple détaillé_ : le cercle C a pour centre O et pour rayon 6 cm ; h est l'homothétie de centre I et de rapport −1/3. L'image de C est le cercle de centre O' = h(O), placé de l'autre côté de I à la distance IO' = IO/3, et de rayon (1/3) × 6 = **2 cm**. Le signe a déplacé le centre, la valeur absolue a réduit le rayon.

## 🧮 Périmètre, aire : le rapport et son carré

Une homothétie multiplie **toutes** les longueurs par |k|. Un périmètre est une somme de longueurs : il est donc lui aussi multiplié par |k|. Une aire, elle, se mesure en unités de longueur **au carré**.

> **Retenir (grandeurs).** Si une figure de périmètre p et d'aire s a pour image par h_(I,k) une figure de périmètre p' et d'aire s', alors
>
> $$ p' = |k| × p et s' = k² × s $$

Le carré k² est toujours positif : c'est la seule formule du chapitre où le signe de k disparaît tout seul, sans qu'on ait à écrire une valeur absolue.

::: figure Avec k = 2 chaque longueur double, donc le périmètre double aussi — mais le grand rectangle contient exactement quatre copies du petit : l'aire, elle, est multipliée par 2² = 4
<svg viewBox="0 0 340 210">
<rect x="40" y="130" width="60" height="30" fill="#0f6e56" opacity="0.12"/>
<rect x="40" y="130" width="60" height="30" fill="none" stroke="#0f172a" stroke-width="2.2"/>
<rect x="150" y="100" width="120" height="60" fill="#0f6e56" opacity="0.12"/>
<rect x="150" y="100" width="120" height="60" fill="none" stroke="#0f172a" stroke-width="2.2"/>
<path d="M210 100 L210 160 M150 130 L270 130" fill="none" stroke="#0f6e56" stroke-width="1.4" stroke-dasharray="5 4"/>
<path d="M110 145 L134 145" fill="none" stroke="#94a3b8" stroke-width="1.8"/>
<polygon points="142,145 132,150 132,140" fill="#94a3b8"/>
<g font-size="12" fill="#94a3b8" text-anchor="middle"><text x="124" y="134">k = 2</text></g>
<g font-size="11" fill="#0f172a" text-anchor="middle">
<text x="70" y="182">aire s · périmètre p</text>
<text x="210" y="182">aire 4s · périmètre 2p</text>
</g>
</svg>
:::

_Exemple détaillé_ : un triangle de périmètre 21 cm et d'aire 18 cm² est transformé par une homothétie de rapport −3. Son image a pour périmètre |−3| × 21 = **63 cm** et pour aire (−3)² × 18 = 9 × 18 = **162 cm²**. Remarque le contraste : le périmètre a été multiplié par 3, l'aire par 9.

> ⚠️ Le piège symétrique existe : appliquer k² à un périmètre, ou |k| à une aire. Retiens la logique plutôt que les formules — une longueur se multiplie une fois, une aire deux fois.

## 🔵 Deux cercles, deux homothéties

Prends deux cercles de centres distincts et de rayons **différents**, R et R'. Chacun est l'image de l'autre par une homothétie — et il y en a exactement deux.

> **Retenir.** Deux cercles de rayons R ≠ R' et de centres distincts sont images l'un de l'autre par **exactement deux homothéties** : l'une de rapport **positif** R'/R, dont le centre I est extérieur au segment joignant les deux centres ; l'autre de rapport **négatif** −R'/R, dont le centre J est situé entre les deux centres. Les deux centres I et J sont sur la droite des centres.

Ces deux points ne sont pas des curiosités : ce sont eux qui commandent les **tangentes communes**. Les deux tangentes communes **extérieures** passent toutes deux par I, et les deux tangentes communes **intérieures** passent toutes deux par J. C'est la conservation du contact qui l'explique : une droite tangente à un cercle a pour image une droite tangente au cercle image, et une droite qui passe par le centre de l'homothétie est sa propre image — donc elle touche les deux cercles à la fois.

::: figure Les deux cercles se correspondent de deux façons : par l'homothétie de centre I et de rapport positif, et par celle de centre J et de rapport négatif. Les deux tangentes communes extérieures, tracées ici, se croisent exactement en I
<svg viewBox="0 0 340 220">
<path d="M18 120 L320 120" fill="none" stroke="#94a3b8" stroke-width="1.4"/>
<path d="M30.7 120 L313.9 37.4 M30.7 120 L313.9 202.6" fill="none" stroke="#0f6e56" stroke-width="1.6"/>
<circle cx="120" cy="120" r="25" fill="none" stroke="#0f172a" stroke-width="2.2"/>
<circle cx="245" cy="120" r="60" fill="none" stroke="#0f172a" stroke-width="2.2"/>
<g fill="#0f172a"><circle cx="120" cy="120" r="4"/><circle cx="245" cy="120" r="4"/></g>
<circle cx="30.7" cy="120" r="5" fill="#0f6e56"/>
<circle cx="156.8" cy="120" r="5" fill="#b91c1c"/>
<g font-size="15" font-weight="700" text-anchor="middle" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">
<text x="120" y="110" fill="#0f172a">O</text>
<text x="245" y="110" fill="#0f172a">O'</text>
<text x="28" y="143" fill="#0f6e56">I</text>
<text x="158" y="143" fill="#b91c1c">J</text>
</g>
</svg>
:::

> 🗡️ Si les deux rayons sont **égaux**, le rapport positif vaudrait 1 — or l'homothétie de rapport 1 ne déplace aucun point, donc elle ne peut pas envoyer un cercle sur un autre. Il ne reste alors qu'**une seule** homothétie, celle de rapport −1 : la symétrie centrale dont le centre est le milieu du segment joignant les deux centres.

## 🏹 Trouver un lieu de points

Voici l'usage le plus rentable du chapitre. Quand un point M **décrit** une courbe connue et qu'un second point M' se construit à partir de M par une relation vectorielle, il suffit de reconnaître une homothétie pour obtenir la courbe décrite par M'.

La méthode tient en trois temps : écrire la relation sous la forme IM'⃗ = kIM⃗ pour un point fixe I bien choisi ; en déduire que M' est l'image de M par h_(I,k) ; conclure en transformant la courbe de départ par le tableau des images.

_Exemple détaillé_ : A est un point fixe, et M décrit un cercle C de centre O et de rayon 6 cm. On note G le barycentre des points pondérés (A, 2) et (M, 3). D'après la fonction vectorielle de Leibniz, 2AA⃗ + 3AM⃗ = 5AG⃗, c'est-à-dire AG⃗ = (3/5)AM⃗. Le point G est donc l'image de M par l'homothétie de centre **A** et de rapport **3/5**. Quand M parcourt C, le point G parcourt donc le **cercle image** : celui de centre h(O), placé sur [AO) à la distance (3/5) × AO, et de rayon (3/5) × 6 = **3,6 cm**.

> 🗡️ Le point fixe qui sert de centre est toujours celui qui **ne bouge pas** dans l'énoncé : ici A. Cherche-le en premier, l'égalité vectorielle se met ensuite d'elle-même sous la bonne forme.

## 👑 Aller plus loin : droite et cercle d'Euler

Soit ABC un triangle, G son centre de gravité, et A', B', C' les milieux respectifs de [BC], [CA] et [AB]. Comme G est le barycentre de (A, 1), (B, 1) et (C, 1), le regroupement de B et C donne GA⃗ = −2GA'⃗, autrement dit GA'⃗ = −(1/2)GA⃗ : le point A' est l'**image de A** par l'homothétie de centre G et de rapport **−1/2**. Il en va de même pour B' et C'.

Notons h cette homothétie et suivons ce qu'elle fait des droites remarquables. La hauteur issue de A est la perpendiculaire à (BC) passant par A ; son image est une droite **parallèle** à cette hauteur — donc encore perpendiculaire à (BC) — passant par A', c'est-à-dire la **médiatrice de [BC]**. Les trois hauteurs de ABC ont donc pour images les trois médiatrices. Leur point de concours suit : l'image de l'**orthocentre** H est le **centre du cercle circonscrit** O.

> **Retenir (droite d'Euler).** h(H) = O donne GO⃗ = −(1/2)GH⃗ : les points **O, G et H sont alignés**, sur ce qu'on appelle la **droite d'Euler** du triangle, et l'on retrouve la relation OH⃗ = 3OG⃗.

L'image du cercle circonscrit à ABC est le cercle circonscrit à A'B'C'. Son centre est h(O), son rayon vaut |−1/2| × R, et un petit calcul montre que h(O) est le milieu de [OH].

> **Retenir (cercle d'Euler).** Le cercle circonscrit au triangle des milieux A'B'C' a pour centre le **milieu Ω de [OH]** et pour rayon **R/2**, où R est le rayon du cercle circonscrit à ABC. On l'appelle le **cercle d'Euler** du triangle.

::: figure Le triangle des milieux A'B'C' est l'image de ABC par l'homothétie de centre G et de rapport −1/2 : son cercle circonscrit, tracé en pointillé, est le cercle d'Euler, de rayon moitié de R et de centre le point Ω, milieu de [OH]. Les quatre points O, G, Ω et H sont alignés sur la droite d'Euler, tracée en rouge
<svg viewBox="0 0 340 240">
<path d="M60 40 L40 200 L300 190 Z" fill="none" stroke="#0f172a" stroke-width="2.2" stroke-linejoin="round"/>
<circle cx="116.2" cy="147.6" r="71.7" fill="none" stroke="#0f6e56" stroke-width="1.8" stroke-dasharray="6 5"/>
<path d="M170 195 L180 115 L50 120 Z" fill="none" stroke="#0f6e56" stroke-width="1.8" stroke-linejoin="round"/>
<path d="M48 164.8 L190 129.1" fill="none" stroke="#b91c1c" stroke-width="2"/>
<g fill="#0f172a"><circle cx="60" cy="40" r="4"/><circle cx="40" cy="200" r="4"/><circle cx="300" cy="190" r="4"/></g>
<g fill="#0f6e56"><circle cx="170" cy="195" r="4"/><circle cx="180" cy="115" r="4"/><circle cx="50" cy="120" r="4"/></g>
<g fill="#b91c1c"><circle cx="167.7" cy="134.7" r="4"/><circle cx="133.3" cy="143.3" r="4"/><circle cx="116.2" cy="147.6" r="4"/><circle cx="64.6" cy="160.6" r="4"/></g>
<g font-size="14" font-weight="700" text-anchor="middle" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">
<text x="52" y="32" fill="#0f172a">A</text>
<text x="30" y="218" fill="#0f172a">B</text>
<text x="312" y="204" fill="#0f172a">C</text>
<text x="176" y="213" fill="#0f6e56">A'</text>
<text x="196" y="106" fill="#0f6e56">B'</text>
<text x="36" y="112" fill="#0f6e56">C'</text>
<text x="182" y="150" fill="#b91c1c">O</text>
<text x="138" y="167" fill="#b91c1c">G</text>
<text x="108" y="136" fill="#b91c1c">Ω</text>
<text x="58" y="180" fill="#b91c1c">H</text>
</g>
</svg>
:::

> 🏆 Quête franchie, héros : tu sais poser une homothétie à partir de son centre et de son rapport, construire une image, retrouver un centre, lire le signe de k sur une figure, appliquer |k| aux longueurs et k² aux aires, transformer un cercle, reconnaître les deux homothéties qui échangent deux cercles et démonter un lieu de points en une ligne. Au chapitre suivant, la transformation change encore de nature : elle ne dilatera plus, elle fera **tourner**.
