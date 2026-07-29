# ⚔️ Similitudes — quand les figures cessent d'être égales pour devenir semblables

> 💡 «Une carte au 1/25 000 n'est pas le pays, et pourtant tous ses angles sont justes : c'est exactement ce qu'une similitude sait faire.»

Dans tout ce chapitre, **le plan est orienté dans le sens direct**. Au chapitre 11 tu as appris qu'une isométrie ne déforme rien ; au chapitre 12, que son écriture complexe est z′ = az + b **ou** z′ = az̄ + b, toujours avec **|a| = 1**. Cette contrainte |a| = 1, c'était la promesse « les longueurs ne changent pas ». Ce chapitre la **lève** : on garde a ≠ 0 quelconque, on pose k = |a|, et toutes les longueurs se retrouvent multipliées par k. Les figures ne sont plus **égales** : elles sont **semblables**. En 1872, dans son programme d'Erlangen, Felix Klein rangeait justement déplacements, symétries et similitudes dans une même famille — le **groupe principal** de la géométrie euclidienne — parce que ce sont eux qui laissent intactes les propriétés métriques. Voici cette famille, complète.

## 🏰 Le premier étage : homothéties et translations

Tu connais déjà l'outil qui agrandit sans tourner.

> **Définition (rappel)** — « Soit I un point et k un réel non nul. On appelle **homothétie de centre I et de rapport k** l'application du plan dans lui-même qui à tout point M associe l'unique point M′ tel que IM′⃗ = kIM⃗. »

> **Théorème (propriété caractéristique)** — « Soit k un réel non nul et différent de 1. Une application f est une homothétie de rapport k, si et seulement si, pour tous points M et N d'images M′ et N′ par f, M′N′⃗ = kMN⃗. »

> **Théorème** — « Toute homothétie conserve les mesures des angles orientés. »

::: figure Chaque point s'éloigne de I le long de sa propre demi-droite, dans le même rapport k = 1,8 : la figure grandit sans tourner ni se retourner.
<svg viewBox="0 0 290 235"><path d="M138 156 L246 156 L192 48 Z" fill="#0f6e56" opacity="0.12"/><g fill="none" stroke="#94a3b8" stroke-width="1.3" stroke-dasharray="5 4"><path d="M30 210 L148.8 150.6"/><path d="M30 210 L267.6 150.6"/><path d="M30 210 L208.2 31.8"/></g><path d="M90 180 L150 180 L120 120 Z" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><path d="M138 156 L246 156 L192 48 Z" fill="none" stroke="#0f6e56" stroke-width="2" stroke-linejoin="round"/><g fill="#0f172a"><circle cx="30" cy="210" r="4.5"/><circle cx="90" cy="180" r="4"/><circle cx="150" cy="180" r="4"/><circle cx="120" cy="120" r="4"/></g><g fill="#0f6e56"><circle cx="138" cy="156" r="4"/><circle cx="246" cy="156" r="4"/><circle cx="192" cy="48" r="4"/></g><g font-size="15" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="20" y="224" text-anchor="middle" fill="#0f172a">I</text><text x="82" y="196" text-anchor="middle" fill="#0f172a">A</text><text x="156" y="196" text-anchor="middle" fill="#0f172a">B</text><text x="112" y="110" text-anchor="middle" fill="#0f172a">C</text><text x="132" y="148" text-anchor="middle" fill="#0f6e56">A′</text><text x="256" y="168" text-anchor="middle" fill="#0f6e56">B′</text><text x="200" y="40" text-anchor="middle" fill="#0f6e56">C′</text></g></svg>
:::

> **Théorème (composées)** — « La composée de deux homothéties de rapports respectifs k₁ et k₂ est une homothétie de rapport k₁k₂ si k₁k₂ ≠ 1, une translation si k₁k₂ = 1. » Et : « La composée d'une translation et d'une homothétie de rapport k ≠ 1 est une homothétie de rapport k. »

_Exemple détaillé_ — soit h₁ = h(A, 2) avec A(0, 0) et h₂ = h(B, 1/3) avec B(3, 0). Le rapport de h₂∘h₁ vaut 2 × 1/3 = **2/3** ≠ 1 : c'est une homothétie. Son centre est son point fixe. Écrivons l'application : h₁(M) = 2M, puis h₂(N) = B + (1/3)(N − B), donc

$$ h₂∘h₁(M) = (3, 0) + (1/3)(2M − (3, 0)) = (2, 0) + (2/3)M $$

Le point fixe Ω vérifie Ω = (2, 0) + (2/3)Ω, soit (1/3)Ω = (2, 0) et **Ω(6, 0)**. _Contrôle_ — h₁(6, 0) = (12, 0), puis h₂(12, 0) = (3, 0) + (1/3)(9, 0) = (6, 0) ✓. En échangeant l'ordre, h₁∘h₂(M) = (4, 0) + (2/3)M a le **même rapport 2/3** mais le centre Ω′(12, 0) : _contrôle_ — h₂(12, 0) = (6, 0) puis h₁(6, 0) = (12, 0) ✓.

> ⚠️ Le rapport d'une composée d'homothéties se lit tout de suite (c'est le produit), mais **jamais le centre** : il faut le calculer comme point fixe. Et h₁∘h₂ ≠ h₂∘h₁ dès que les centres diffèrent.

_Exemple (le cas limite)_ — h(A, 2)∘h(B, 1/2) avec A(0, 0) et B(2, 0) : ici k₁k₂ = 1. On obtient M ↦ 2[(1, 0) + M/2] = (2, 0) + M : c'est la **translation** de vecteur (2, 0), qui n'a aucun point fixe ✓.

> **Théorème (homothétie et nombres complexes)** — « L'application f est une homothétie de rapport k ≠ 1, si et seulement si, il existe un nombre complexe b tel que z′ = kz + b. De plus, l'affixe z_A du centre A vérifie z_A = b/(1 − k). » Ici **k est réel** : c'est ce qui distingue l'homothétie de tout le reste.

_Exemple détaillé_ — z′ = −2z + 3 : le coefficient −2 est **réel**, donc c'est l'homothétie de rapport −2 et de centre d'affixe 3/(1 − (−2)) = 3/3 = 1. _Contrôle_ — −2 × 1 + 3 = 1 ✓, le point d'affixe 1 est bien fixe. De même z′ = 4z + 1 − i est l'homothétie de rapport 4 et de centre (1 − i)/(1 − 4) = (−1 + i)/3 ; _contrôle_ — 4(−1 + i)/3 + 1 − i = (−4 + 4i + 3 − 3i)/3 = (−1 + i)/3 ✓.

## ⚡ Similitude de rapport k : la définition

Une homothétie multiplie les distances par |k| ; une isométrie les laisse intactes. Un seul mot couvre les deux.

> **Définition** — « Soit k un réel **strictement positif**. On appelle **similitude de rapport k**, toute application du plan dans lui-même telle que pour tous points A et B d'images respectives A′ et B′, **A′B′ = k·AB**. »

> **Exemples** — « Les isométries sont des similitudes de rapport 1. Toute homothétie de rapport k est une similitude de rapport |k|. »

> **Théorème** — « La composée de deux similitudes de rapports respectifs k et k′ est une similitude de rapport kk′. »

> **Théorème (la carte d'identité)** — « Une application du plan dans lui-même est une similitude, si et seulement si, elle est **la composée d'une homothétie et d'une isométrie**. »

Ce dernier théorème est le mode d'emploi du chapitre : toute similitude = « une isométrie, puis un zoom ». Le zoom apporte le rapport k, l'isométrie apporte le reste (angle, sens, position).

::: figure Même forme, deux tailles : une isométrie (k = 1) reproduit la figure à l'identique, une similitude de rapport 1,5 la reproduit à l'échelle — les trois côtés sont multipliés par 1,5, l'angle droit reste droit.
<svg viewBox="0 0 270 175"><path d="M20 140 L74 140 L20 68 Z" fill="#0f6e56" opacity="0.10"/><path d="M150 140 L231 140 L150 32 Z" fill="#0f6e56" opacity="0.10"/><path d="M20 140 L74 140 L20 68 Z" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><path d="M150 140 L231 140 L150 32 Z" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><path d="M20 128 L32 128 L32 140" fill="none" stroke="#0f172a" stroke-width="1.8"/><path d="M150 126 L164 126 L164 140" fill="none" stroke="#0f172a" stroke-width="1.8"/><g fill="#0f172a"><circle cx="20" cy="140" r="3.5"/><circle cx="74" cy="140" r="3.5"/><circle cx="20" cy="68" r="3.5"/><circle cx="150" cy="140" r="3.5"/><circle cx="231" cy="140" r="3.5"/><circle cx="150" cy="32" r="3.5"/></g><g font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="10" y="156" text-anchor="middle" fill="#0f172a">A</text><text x="80" y="156" text-anchor="middle" fill="#0f172a">B</text><text x="10" y="62" text-anchor="middle" fill="#0f172a">C</text><text x="140" y="156" text-anchor="middle" fill="#0f172a">A′</text><text x="239" y="156" text-anchor="middle" fill="#0f172a">B′</text><text x="140" y="26" text-anchor="middle" fill="#0f172a">C′</text><text x="47" y="156" text-anchor="middle" fill="#0f6e56">3</text><text x="34" y="106" text-anchor="middle" fill="#0f6e56">4</text><text x="58" y="96" text-anchor="middle" fill="#0f6e56">5</text><text x="190" y="156" text-anchor="middle" fill="#0f6e56">4,5</text><text x="166" y="88" text-anchor="middle" fill="#0f6e56">6</text><text x="202" y="80" text-anchor="middle" fill="#0f6e56">7,5</text></g></svg>
:::

_Exemple détaillé_ — soit f : z ↦ (1 + i)z + 2. Prenons A(0), B(1), C(i). Alors A′ = 2, B′ = 3 + i, C′ = (1 + i)i + 2 = 1 + i. On mesure : AB = 1 et A′B′ = |3 + i − 2| = |1 + i| = **√2** ; BC = |i − 1| = √2 et B′C′ = |1 + i − 3 − i| = 2 = √2 × √2 ✓. Le rapport vaut donc k = √2 = |1 + i| — **le module du coefficient**. C'est la règle générale du chapitre.

## 🛡️ Ce qu'une similitude garde, ce qu'elle multiplie

Une similitude n'est jamais qu'une isométrie suivie d'un zoom : tout ce qu'une isométrie conservait est conservé, à cela près que les **longueurs sont multipliées par k**.

> **Théorème (produit scalaire)** — « Pour tous points A, B, C et D, d'images respectives A′, B′, C′ et D′ par une similitude de rapport k, **A′B′⃗·C′D′⃗ = k²·AB⃗·CD⃗**. »

> **Propriétés** — « • Une similitude de rapport k est une **bijection** et sa réciproque est une similitude de rapport **1/k**. • Une similitude conserve les **angles géométriques**. • Elle conserve l'**orthogonalité**. • Elle conserve l'**alignement** et le **barycentre**. • Elle transforme un segment en un segment, une droite en une droite. • Elle conserve le **parallélisme**. • Elle transforme un cercle en un cercle et conserve le **contact**. • Si AB⃗ = aCD⃗ + bEF⃗ avec a, b réels, alors A′B′⃗ = aC′D′⃗ + bE′F′⃗. »

De la formule du produit scalaire découle le fait le plus utile en exercice : **les aires sont multipliées par k²**. L'image d'un triangle d'aire 𝒜 par une similitude de rapport 1/2 a pour aire 𝒜/4, pas 𝒜/2.

> ⚠️ Le rapport k agit sur les **longueurs** (× k), sur les **produits scalaires et les aires** (× k²), et **pas du tout** sur les angles. Confondre les deux exposants est l'erreur la plus fréquente du chapitre.

> **Théorème** — « Deux similitudes qui coïncident sur trois points non alignés coïncident sur tout le plan. » Et, comme pour les isométries : « (f∘g)⁻¹ = g⁻¹∘f⁻¹ ; f = g, si et seulement si, h∘f = h∘g. »

**Triangles semblables.** Deux triangles ABC et A′B′C′ sont dits **semblables** s'il existe une similitude qui envoie A, B et C sur A′, B′ et C′.

> **Théorème** — Les triangles ABC et A′B′C′ sont semblables **si et seulement si** A′B′/AB = A′C′/AC = B′C′/BC, ce qui équivaut encore à Â = Â′, B̂ = B̂′ et Ĉ = Ĉ′.

_Exemple détaillé_ — soit ABC rectangle en A avec AB = 3, AC = 4, BC = 5, et A′B′C′ tel que A′B′ = 4,5, A′C′ = 6, B′C′ = 7,5. Les trois quotients valent 4,5/3 = 1,5 · 6/4 = 1,5 · 7,5/5 = 1,5 : les triangles sont **semblables** de rapport k = 1,5. Donc A′B′C′ est lui aussi **rectangle en A′**. _Contrôle par les aires_ — l'aire de ABC vaut (3 × 4)/2 = 6, celle de A′B′C′ vaut (4,5 × 6)/2 = 13,5, et 13,5 = 6 × 1,5² = 6 × 2,25 ✓.

## 🔮 Directe ou indirecte : le sens revient

Au chapitre 12, une isométrie se rangeait en déplacement ou antidéplacement selon qu'elle conservait ou renversait les angles **orientés**. Comme une similitude est « homothétie ∘ isométrie » et qu'une homothétie conserve toujours les angles orientés, c'est **l'isométrie du couple** qui décide.

> **Définition** — « On dit qu'une similitude est **directe** si elle est la composée d'une homothétie et d'un **déplacement**. On dit qu'une similitude est **indirecte** si elle est la composée d'une homothétie et d'un **antidéplacement**. »

> **Conséquence** — « Toute similitude directe conserve les mesures des angles orientés. Toute similitude indirecte change les mesures des angles orientés en leurs **opposées**. »

::: figure Les deux images ont le même rapport et donc les mêmes longueurs entre elles, mais seule celle du milieu tourne dans le même sens que l'original : à droite, le parcours P → Q → R s'est inversé.
<svg viewBox="0 0 330 145"><path d="M18 110 L70 110 L44 71 Z" fill="#0f6e56" opacity="0.10"/><path d="M148 97 L148 34.6 L101.2 65.8 Z" fill="#0f6e56" opacity="0.10"/><path d="M252 97 L252 34.6 L298.8 65.8 Z" fill="#b45309" opacity="0.12"/><g fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"><path d="M18 110 L70 110 L44 71 Z"/><path d="M148 97 L148 34.6 L101.2 65.8 Z"/><path d="M252 97 L252 34.6 L298.8 65.8 Z"/></g><g fill="none" stroke="#0f6e56" stroke-width="1.8"><path d="M50.89 102.79 A9 9 0 1 0 35.54 93.92"/><path d="M139.29 71.59 A9 9 0 1 0 123.94 62.72"/></g><g fill="#0f6e56"><path d="M34.51 96.74 L33.75 90.07 L39.39 92.13 Z"/><path d="M122.91 65.54 L122.15 58.87 L127.79 60.93 Z"/></g><path d="M260.71 71.59 A9 9 0 1 1 276.06 62.72" fill="none" stroke="#b45309" stroke-width="1.8"/><path d="M277.09 65.54 L277.85 58.87 L272.21 60.93 Z" fill="#b45309"/><g fill="#0f172a"><circle cx="18" cy="110" r="3.5"/><circle cx="70" cy="110" r="3.5"/><circle cx="44" cy="71" r="3.5"/><circle cx="148" cy="97" r="3.5"/><circle cx="148" cy="34.6" r="3.5"/><circle cx="101.2" cy="65.8" r="3.5"/><circle cx="252" cy="97" r="3.5"/><circle cx="252" cy="34.6" r="3.5"/><circle cx="298.8" cy="65.8" r="3.5"/></g><g font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="12" y="126" text-anchor="middle" fill="#0f172a">P</text><text x="76" y="126" text-anchor="middle" fill="#0f172a">Q</text><text x="44" y="62" text-anchor="middle" fill="#0f172a">R</text><text x="139" y="112" text-anchor="middle" fill="#0f172a">P′</text><text x="148" y="27" text-anchor="middle" fill="#0f172a">Q′</text><text x="90" y="62" text-anchor="middle" fill="#0f172a">R′</text><text x="260" y="112" text-anchor="middle" fill="#0f172a">P″</text><text x="252" y="27" text-anchor="middle" fill="#0f172a">Q″</text><text x="310" y="62" text-anchor="middle" fill="#0f172a">R″</text></g></svg>
:::

> **Théorème (règle des signes)** — « • La composée de deux similitudes **directes** est directe. • La composée de deux similitudes **indirectes** est **directe**. • La composée d'une directe et d'une indirecte est **indirecte**. • La réciproque d'une directe est directe, celle d'une indirecte est indirecte. »

Retiens-le comme au chapitre 12 : directe = **+1**, indirecte = **−1**, et la nature d'une composée est le **produit** des signes.

> **Théorème (existence et unicité)** — « Soit A, B, C et D des points du plan tels que A ≠ B et C ≠ D. Il existe une **unique** similitude directe qui envoie A sur C et B sur D. Il existe une **unique** similitude indirecte qui envoie A sur C et B sur D. »

C'est la clé de tous les problèmes « déterminer la similitude qui envoie… » : la réponse en compte toujours exactement **deux**, une par sens. Et, contrairement au chapitre 12, **aucune condition sur les longueurs** n'est requise — AB et CD peuvent être quelconques, le rapport s'ajuste tout seul : k = CD/AB.

_Exemple détaillé_ — comparons f : z ↦ 2iz + 1 et g : z ↦ 2iz̄ + 1 sur le triangle direct A(0, 0), B(1, 0), C(0, 1). Par f : A′(1, 0), B′ = 2i + 1 → (1, 2), C′ = 2i·i + 1 = −1 → (−1, 0). Par g : A″(1, 0), B″ = 2i + 1 → (1, 2), C″ = 2i(−i) + 1 = 3 → (3, 0). Les deux images de A et B coïncident, mais pas celle de C. Vérifions le sens sur l'angle en premier sommet : pour ABC, (AB⃗, AC⃗) = ((1, 0), (0, 1)) ≡ **+π/2** ; pour l'image par f, (A′B′⃗, A′C′⃗) = ((0, 2), (−2, 0)) ≡ **+π/2** ✓ conservé ; pour l'image par g, (A″B″⃗, A″C″⃗) = ((0, 2), (2, 0)) ≡ **−π/2** ✓ renversé. La **barre de conjugaison** est le seul signe distinctif.

## 🧮 Similitude directe : angle, centre, forme réduite

Une similitude directe fait tourner tous les vecteurs du même angle — exactement comme un déplacement.

> **Théorème et définition (angle)** — « Soit f une similitude directe et A, B, C, D des points tels que AB ≠ 0 et CD ≠ 0, d'images A′, B′, C′, D′. Alors (AB⃗, A′B′⃗) ≡ (CD⃗, C′D′⃗) [2π]. En désignant par θ une mesure de l'angle (AB⃗, A′B′⃗), on dit que f est une **similitude directe d'angle θ**. »

> **Théorème** — « Si f et g sont des similitudes directes d'angles θ et θ′, alors f∘g est d'angle **θ + θ′**, et f⁻¹ est d'angle **−θ**. » (Les rapports, eux, se multiplient : kk′ et 1/k.)

> **Théorème (centre)** — « Toute similitude directe de rapport différent de 1 admet un **unique point fixe**, appelé **centre** de la similitude. »

> **Conséquence (éléments caractéristiques)** — « Une similitude directe de rapport k ≠ 1 est parfaitement déterminée par son **centre**, son **rapport** et son **angle**. Une application f est la similitude directe de centre I, de rapport k ≠ 1 et d'angle θ, si et seulement si, pour tout M ≠ I d'image M′, **IM′ = k·IM** et **(IM⃗, IM′⃗) ≡ θ [2π]**. »

> **Théorème (forme réduite)** — « Toute similitude directe de centre I, de rapport k ≠ 1 et d'angle θ se décompose sous la forme **f = h∘r = r∘h**, où h est l'homothétie de centre I et de rapport k et r la rotation de centre I et d'angle θ. »

::: figure Tourner d'abord puis agrandir (par M₁), ou agrandir d'abord puis tourner (par M₂) : les deux chemins aboutissent au même M′ — c'est toute la forme réduite f = h∘r = r∘h.
<svg viewBox="0 0 240 240"><g fill="none" stroke="#94a3b8" stroke-width="1.3" stroke-dasharray="5 4"><path d="M35 215 L195 167"/><path d="M35 215 L101.1 61.6"/></g><g fill="none" stroke="#0f6e56" stroke-width="1.8"><path d="M135 185 A104.4 104.4 0 0 0 76.3 119.1"/><path d="M195 167 A167.05 167.05 0 0 0 101.1 61.6"/></g><g fill="none" stroke="#b45309" stroke-width="1.8" stroke-dasharray="6 4"><path d="M76.3 119.1 L101.1 61.6"/><path d="M135 185 L195 167"/></g><g fill="#0f172a"><circle cx="35" cy="215" r="4.5"/><circle cx="135" cy="185" r="4"/><circle cx="101.1" cy="61.6" r="4.5"/></g><g fill="#0f6e56"><circle cx="76.3" cy="119.1" r="4"/><circle cx="195" cy="167" r="4"/></g><g font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="24" y="228" text-anchor="middle" fill="#0f172a">I</text><text x="144" y="199" text-anchor="middle" fill="#0f172a">M</text><text x="62" y="113" text-anchor="middle" fill="#0f6e56">M₁</text><text x="207" y="178" text-anchor="middle" fill="#0f6e56">M₂</text><text x="103" y="52" text-anchor="middle" fill="#0f172a">M′</text></g></svg>
:::

_Exemple détaillé_ — soit ABCD le carré direct A(0, 0), B(1, 0), C(1, 1), D(0, 1), de centre O(1/2, 1/2), et S la similitude directe de **centre D** qui envoie O sur C.

**Rapport** : k = DC/DO. Ici DC = 1 et DO = √((1/2)² + (1/2)²) = √2/2, donc k = 1/(√2/2) = **√2**. **Angle** : θ = (DO⃗, DC⃗) = ((1/2, −1/2), (1, 0)). En complexes, (1)/((1 − i)/2) = 2/(1 − i) = 1 + i, d'argument **π/4**. Donc S a pour éléments caractéristiques (D, √2, π/4), et sa forme réduite est S = h(D, √2)∘r(D, π/4).

**Image de A** : en écriture complexe avec z_D = i, S(z) = √2·e^(iπ/4)(z − i) + i = (1 + i)(z − i) + i. Pour A (z = 0) : (1 + i)(−i) + i = (−i + 1) + i = 1, donc **S(A) = B**. _Contrôle par les éléments caractéristiques_ — DA = 1 et DB = √(1² + 1²) = √2 = √2 × DA ✓ ; et (DA⃗, DB⃗) = ((0, −1), (1, −1)) donne en complexes (1 − i)/(−i) = 1 + i, d'argument π/4 ✓.

**Image de C** : (1 + i)(1 + i − i) + i = (1 + i) + i = 1 + 2i, soit **S(C) = (1, 2)**. _Contrôle_ — DC′ = √(1² + 1²) = √2 = √2 × DC ✓, et (DC⃗, DC′⃗) = ((1, 0), (1, 1)) ≡ π/4 ✓. _Contrôle de la commutation_ — par r(D, π/4) d'abord, A ↦ D + e^(iπ/4)(−i) = i + (1 − i)/√2 ; puis par h(D, √2) : i + √2 × (1 − i)/√2 = i + 1 − i = 1 = B ✓, le même résultat que h∘r.

::: figure La similitude de centre D, de rapport √2 et d'angle π/4 : chaque point s'écarte de D d'un huitième de tour et de √2 fois plus loin — O part sur C, et C sur C′.
<svg viewBox="0 0 200 230"><path d="M60 200 L130 200 L130 130 L60 130 Z" fill="#0f6e56" opacity="0.10"/><path d="M60 200 L130 200 L130 130 L60 130 Z" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><path d="M81.2 151.2 A30 30 0 0 0 90 130" fill="none" stroke="#b45309" stroke-width="1.8"/><g fill="none" stroke="#0f6e56" stroke-width="1.8" stroke-dasharray="6 4"><path d="M95 165 L126 134"/><path d="M130 130 L130 66"/></g><g fill="#0f6e56"><path d="M130 130 L127.17 138.49 L121.51 132.83 Z"/><path d="M130 60 L125 70 L135 70 Z"/></g><g fill="#0f172a"><circle cx="60" cy="200" r="4"/><circle cx="130" cy="200" r="4"/><circle cx="130" cy="130" r="4"/><circle cx="60" cy="130" r="5"/><circle cx="95" cy="165" r="4"/><circle cx="130" cy="60" r="4"/></g><g font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="50" y="216" text-anchor="middle" fill="#0f172a">A</text><text x="140" y="216" text-anchor="middle" fill="#0f172a">B</text><text x="144" y="126" text-anchor="middle" fill="#0f172a">C</text><text x="48" y="124" text-anchor="middle" fill="#0f172a">D</text><text x="103" y="178" text-anchor="middle" fill="#0f172a">O</text><text x="142" y="56" text-anchor="middle" fill="#0f172a">C′</text><text x="97" y="152" text-anchor="middle" fill="#b45309">π/4</text></g></svg>
:::

> 🗡️ **Construire le centre sans repère.** Si f envoie A sur B et C sur D, son centre I vérifie IA/IB = AC/BD = 1/k et (IA⃗, IB⃗) ≡ θ. Or l'ensemble des M tels que MA = k′MB (k′ ≠ 1) est un **cercle** — celui de diamètre [GG′], G et G′ étant les barycentres de (A, 1), (B, −k′) et de (A, 1), (B, k′) — et l'ensemble des M tels que (MA⃗, MB⃗) ≡ θ [2π] est un **arc de cercle** d'extrémités A et B. Le centre est leur intersection.

## 📐 Similitudes directes et nombres complexes

Le plan est rapporté à un repère orthonormé **direct** (O, i⃗, j⃗). C'est ici que la frontière du chapitre 12 tombe pour de bon.

> **Théorème** — « L'application f est une similitude directe de centre I, de rapport k ≠ 1 et d'angle θ, si et seulement si, il existe deux nombres complexes a et b tels que **z′ = az + b**, avec **a = ke^(iθ)** et **z_I = b/(1 − a)**. »

Tout se lit donc sur le seul coefficient a : **k = |a|** et **θ = arg(a)**.

| Coefficient a       | Nature de z′ = az + b                       | Élément à calculer     |
| ------------------- | ------------------------------------------- | ---------------------- |
| a = 1               | translation de vecteur d'affixe b           | aucun centre           |
| a réel, a ≠ 1       | **homothétie** de rapport a                 | centre b/(1 − a)       |
| \|a\| = 1, a ≠ 1    | **rotation** d'angle arg(a) (chapitre 12)   | centre b/(1 − a)       |
| \|a\| ≠ 1, a non réel | **similitude directe** de rapport \|a\|, d'angle arg(a) | centre b/(1 − a) |

_Exemple détaillé_ — soit f : z ↦ 2iz + 3 − i. Ici a = 2i : **k = |2i| = 2** et **θ = arg(2i) = π/2**. Le centre :

$$ z_I = (3 − i)/(1 − 2i) = (3 − i)(1 + 2i)/((1)² + (2)²) = (3 + 6i − i + 2)/5 = (5 + 5i)/5 = 1 + i $$

_Contrôle_ — 2i(1 + i) + 3 − i = 2i − 2 + 3 − i = 1 + i ✓, le point I(1, 1) est bien fixe. _Contrôle du rapport et de l'angle sur un couple_ — avec B(i) et C(−1) : B′ = 2i·i + 3 − i = 1 − i et C′ = −2i + 3 − i = 3 − 3i. Alors BC⃗ a pour affixe −1 − i et B′C′⃗ a pour affixe 2 − 2i ; leur quotient (2 − 2i)/(−1 − i) = 4i/2 = **2i** ✓ : module 2, argument π/2, conformément à a.

_Exemple_ — z′ = −2iz + 3 : a = −2i donne k = 2 et θ = −π/2, centre 3/(1 + 2i) = 3(1 − 2i)/5 = (3 − 6i)/5. _Contrôle_ — −2i(3 − 6i)/5 + 3 = (−6i − 12)/5 + 3 = (3 − 6i)/5 ✓.

> ⚠️ Avant de calculer quoi que ce soit, **regarde a**. Si |a| = 1, tu es encore au chapitre 12 (isométrie) : z′ = e^(iπ/6)z + 1 est une **rotation** d'angle π/6, pas une similitude de rapport ≠ 1. Si a est **réel**, l'angle est 0 (a > 0) ou π (a < 0) et c'est une **homothétie** — de rapport a, qui peut être négatif, alors que le rapport de similitude, lui, vaut |a| et reste positif.

> 🗡️ Ce piège est le cœur du QCM classique : la forme réduite de r(Ω, π/6)∘h(Ω, −2) n'est **pas** r(Ω, π/6)∘h(Ω, 2). En effet a = e^(iπ/6) × (−2) = 2e^(i(π/6 + π)) = 2e^(i7π/6) = 2e^(−i5π/6). La forme réduite est donc **r(Ω, −5π/6)∘h(Ω, 2)** : un rapport négatif « coûte » un demi-tour supplémentaire.

## ⚔️ Similitudes indirectes : centre, axe, forme réduite

Passons de l'autre côté du miroir. Le rôle que la rotation jouait pour les similitudes directes, la **symétrie orthogonale** le joue ici.

> **Théorème et définition (centre)** — « Une similitude indirecte de rapport différent de 1 admet un **unique point fixe**, appelé **centre** de la similitude. »

> **Théorème (forme réduite)** — « Soit f une similitude indirecte de centre I et de rapport k ≠ 1, h l'homothétie de centre I et de rapport k. Il existe une droite D telle que f se décompose de manière unique sous la forme **f = h∘S_D = S_D∘h**. La droite D est l'ensemble des points M tels que **IM′⃗ = kIM⃗**, où M′ = f(M) ; on l'appelle l'**axe** de f. »

> **Conséquences** — « Une similitude indirecte de rapport ≠ 1 est parfaitement déterminée par son **rapport**, son **centre** et son **axe**. L'axe D et la perpendiculaire à D passant par I sont **globalement invariants**. Et **f∘f est l'homothétie de centre I et de rapport k²**. »

> **Propriété (la bissectrice)** — « Si u⃗ dirige l'axe D, alors (u⃗, IM′⃗) ≡ −(u⃗, IM⃗) [2π] pour tout M ≠ I. La droite D porte donc la **bissectrice intérieure** de l'angle MIM′. »

::: figure On retourne M autour de l'axe D, puis on l'éloigne de I dans le rapport k = 2 : l'axe porte la bissectrice de l'angle M I M′, les deux angles marqués étant opposés.
<svg viewBox="0 0 300 200"><path d="M15 120 H290" fill="none" stroke="#0f172a" stroke-width="2"/><g fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-dasharray="6 4"><path d="M130 165 L130 75"/></g><g fill="none" stroke="#0f6e56" stroke-width="2"><path d="M40 120 L130 165"/><path d="M40 120 L220 30"/></g><g fill="none" stroke="#b45309" stroke-width="1.8"><path d="M75 120 A35 35 0 0 1 71.3 135.7"/><path d="M75 120 A35 35 0 0 0 71.3 104.3"/></g><g fill="#0f172a"><circle cx="40" cy="120" r="5"/><circle cx="130" cy="165" r="4"/><circle cx="130" cy="75" r="4"/><circle cx="220" cy="30" r="4"/></g><g font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="30" y="112" text-anchor="middle" fill="#0f172a">I</text><text x="130" y="182" text-anchor="middle" fill="#0f172a">M</text><text x="130" y="66" text-anchor="middle" fill="#0f172a">M₁</text><text x="231" y="26" text-anchor="middle" fill="#0f172a">M′</text><text x="280" y="110" text-anchor="middle" fill="#0f172a">D</text><text x="87" y="136" text-anchor="middle" fill="#b45309">α</text><text x="87" y="112" text-anchor="middle" fill="#b45309">α</text></g></svg>
:::

> **Théorème (écriture complexe)** — « L'application f est une similitude indirecte de centre I et de rapport k ≠ 1, si et seulement si, il existe deux complexes a et b tels que **z′ = az̄ + b**. Dans ce cas **k = |a|** et **z_I = (a·b̄ + b)/(1 − |a|²)**. »

La formule du centre n'est pas à apprendre par cœur : elle se retrouve. Le point fixe vérifie z = az̄ + b ; en conjuguant, z̄ = āz + b̄ ; en substituant, z = a(āz + b̄) + b = |a|²z + ab̄ + b, d'où z(1 − |a|²) = ab̄ + b. La condition |a| ≠ 1 est exactement ce qui rend la division licite.

_Exemple détaillé_ — soit f : z ↦ 2z̄ + 3i. Ici a = 2, donc **k = |2| = 2** ≠ 1. **Centre** : z_I = (2 × conj(3i) + 3i)/(1 − 4) = (−6i + 3i)/(−3) = **i**, soit I(0, 1). _Contrôle_ — 2·conj(i) + 3i = −2i + 3i = i ✓. **Axe** : c'est l'ensemble des M tels que IM′⃗ = 2IM⃗, c'est-à-dire z′ − i = 2(z − i) :

$$ 2z̄ + 3i − i = 2z − 2i ⟺ 2z̄ = 2z − 4i ⟺ z̄ = z − 2i $$

Avec z = x + iy : x − iy = x + iy − 2i donne −y = y − 2, soit **y = 1**. L'axe est la droite D d'équation y = 1 — qui passe bien par I(0, 1) ✓, comme l'exige la forme réduite. **Forme réduite** : f = h(I, 2)∘S_D = S_D∘h(I, 2).

_Contrôle sur deux points_ — M(2, 0) : par la définition, f(2) = 4 + 3i, donc M′(4, 3). Par h∘S_D : S_D(2, 0) = (2, 2), puis h(I, 2) donne (0, 1) + 2×(2, 1) = (4, 3) ✓. Par S_D∘h : h(I, 2)(2, 0) = (0, 1) + 2×(2, −1) = (4, −1), puis S_D donne (4, 3) ✓ — les deux ordres coïncident. Second point, M(0, 0) : f(0) = 3i → (0, 3) ; et S_D(0, 0) = (0, 2) puis h(I, 2) donne (0, 1) + 2×(0, 1) = (0, 3) ✓.

_Contrôle par f∘f_ — f∘f(z) = 2·conj(2z̄ + 3i) + 3i = 2(2z − 3i) + 3i = 4z − 3i ; et l'homothétie de centre I(i) et de rapport 4 s'écrit 4(z − i) + i = 4z − 3i ✓ : on retrouve bien h(I, k²).

_Exemple détaillé (avec un a non réel)_ — soit f : z ↦ −2iz̄ + 6. Alors k = |−2i| = 2 et z_I = (−2i × 6 + 6)/(1 − 4) = (6 − 12i)/(−3) = **−2 + 4i**. _Contrôle_ — −2i·conj(−2 + 4i) + 6 = −2i(−2 − 4i) + 6 = 4i − 8 + 6 = −2 + 4i ✓. **Axe** : z′ − z_I = 2(z − z_I) s'écrit −2iz̄ + 8 − 4i = 2z + 4 − 8i, soit −2iz̄ = 2z − 4 − 4i, puis z̄ = iz + 2 − 2i. Avec z = x + iy, le membre de droite vaut (2 − y) + i(x − 2), et l'identification avec x − iy donne x = 2 − y : l'axe est la droite **x + y = 2**. _Contrôle_ — I(−2, 4) vérifie −2 + 4 = 2 ✓ ; et pour M(2, 0), point de l'axe, f(2) = −4i + 6 → M′(6, −4) avec IM⃗ = (4, −4) et IM′⃗ = (8, −8) = 2·IM⃗ ✓, exactement la caractérisation de l'axe.

> ⚠️ Si **|a| = 1**, z′ = az̄ + b n'est pas une similitude indirecte de centre unique : c'est un **antidéplacement** (chapitre 12), symétrie orthogonale ou symétrie glissante. La formule du centre se divise alors par 1 − 1 = 0 — c'est le signal.

> ⚠️ Une similitude indirecte n'a **pas d'angle**. Elle a un **axe**. Chercher « l'angle » d'une similitude indirecte est une faute de définition, pas une étourderie de calcul.

## 👑 Méthode : identifier une similitude à tous les coups

Face à « déterminer la nature et les éléments caractéristiques de f », déroule toujours le même algorithme.

| Étape | Question                        | Outil                                                                        |
| ----- | ------------------------------- | ---------------------------------------------------------------------------- |
| 1     | Quel est le rapport k ?         | k = A′B′/AB · k = \|a\| en complexes · produit des rapports pour une composée |
| 2     | Directe ou indirecte ?          | signe d'un angle orienté image · barre de conjugaison · règle des signes      |
| 3     | Si k = 1 ?                      | c'est une **isométrie** — retour aux chapitres 11 et 12                       |
| 4     | Si directe : angle θ            | θ = (AB⃗, A′B′⃗) = arg(a) · somme des angles pour une composée                |
| 5     | Centre I                        | unique point fixe : z = az + b ou z = az̄ + b · ou par cercle et arc capable  |
| 6     | Si indirecte : axe D            | l'ensemble des M tels que IM′⃗ = kIM⃗ · ou la bissectrice de MIM′             |
| 7     | Vérification                    | tester la forme réduite obtenue sur un **second** point                       |

_Exemple détaillé (synthèse)_ — soit ABCD le carré direct A(0, 0), B(2, 0), C(2, 2), D(0, 2), I(1, 0) le milieu de [AB] et J(2, 1) le milieu de [BC]. D'après le théorème d'existence, il existe exactement **deux** similitudes envoyant A sur I et B sur J : une directe et une indirecte. Déterminons-les.

**La directe S.** Rapport : k = IJ/AB = √(1² + 1²)/2 = **√2/2**. Angle : θ = (AB⃗, IJ⃗) = ((2, 0), (1, 1)) ≡ **π/4**. Écriture complexe z′ = az + b : de S(0) = 1 on tire b = 1, et de S(2) = 2 + i on tire 2a + 1 = 2 + i, donc **a = (1 + i)/2**. _Contrôle_ — |a| = √2/2 ✓ et arg(a) = π/4 ✓, conformes au rapport et à l'angle lus géométriquement. Centre : z_Ω = b/(1 − a) = 1/(1 − (1 + i)/2) = 2/(1 − i) = **1 + i**, soit **Ω(1, 1) : le centre du carré**. _Contrôle_ — a(1 + i) + b = (1 + i)²/2 + 1 = 2i/2 + 1 = 1 + i ✓. Forme réduite : S = h(Ω, √2/2)∘r(Ω, π/4).

_Que devient le carré ?_ S(C) = a(2 + 2i) + 1 = (1 + i)² + 1 = 1 + 2i → (1, 2), milieu de [DC] ; S(D) = a(2i) + 1 = (1 + i)i + 1 = i → (0, 1), milieu de [AD]. **S envoie le carré sur le carré de ses milieux** — et le rapport √2/2 avec l'angle π/4 sont exactement ceux qui relient un carré à son carré médian ✓.

**L'indirecte g.** Même méthode avec z′ = az̄ + b : de g(0) = 1 on tire b = 1, et de g(2) = 2 + i on tire 2a + 1 = 2 + i, donc a = (1 + i)/2 aussi (car A et B sont sur l'axe des réels — les deux similitudes ne se séparent qu'ailleurs). Rapport k = |a| = √2/2 ✓, identique. Centre : z_Ω′ = (a·b̄ + b)/(1 − |a|²) = ((1 + i)/2 + 1)/(1 − 1/2) = ((3 + i)/2) × 2 = **3 + i**, soit Ω′(3, 1). _Contrôle_ — a·conj(3 + i) + b = (1 + i)(3 − i)/2 + 1 = (4 + 2i)/2 + 1 = 3 + i ✓.

_Contrôle du sens_ — g(C) = a·conj(2 + 2i) + 1 = (1 + i)(1 − i) + 1 = 3 → (3, 0). Or pour A, B, C l'angle (AB⃗, AC⃗) = ((2, 0), (2, 2)) ≡ **+π/4**, tandis que pour les images (I(1, 0), J(2, 1), (3, 0)) l'angle (IJ⃗, I(3,0)⃗) = ((1, 1), (2, 0)) ≡ **−π/4** ✓ : g renverse bien l'orientation, et son image de C diffère de celle par S. Les deux similitudes annoncées par le théorème sont donc bien distinctes, et toutes deux identifiées.

> 🏆 Treizième porte franchie, héros : tu sais reconnaître une similitude à son seul coefficient, la trancher entre directe et indirecte d'un coup d'œil sur la barre de conjugaison, en extraire centre, rapport, angle ou axe, et la réduire à h∘r ou h∘S_D. Avec ce chapitre, la trilogie des transformations du plan est complète — égalité, sens, échelle. Au chapitre suivant, tu quitteras les transformations pour les **coniques** : ellipse, parabole, hyperbole, ces courbes que l'on obtient en tranchant un cône, et dont les similitudes gardent précieusement l'excentricité.
