# ⚔️ Parallélisme dans l'espace — quand les directions se répondent

> 💡 «Deux rails ne se rencontrent jamais, et pourtant le train les suit tous les deux : dans l'espace, le parallélisme est la boussole qui mène d'une droite à un plan, puis d'un plan à un autre.»

Au chapitre précédent, tu as appris à décider si des droites ou des plans se coupent. Ici, on étudie les positions où rien ne se coupe : le parallélisme, de droite à droite, de droite à plan, de plan à plan.
Huit étapes t'y conduisent : les droites parallèles, leur transitivité, la droite parallèle à un plan, le théorème du toit, les plans parallèles, la preuve qu'ils le sont, le plan qui les traverse, et enfin les sections planes d'un solide. L'orthogonalité est l'objet du chapitre suivant : ici, on n'en a pas besoin.
Les dessins sont en perspective cavalière : la face de devant est en vraie grandeur, les arêtes qui fuient sont tracées obliques. Les droites parallèles de l'espace y restent parallèles, les alignements et les milieux sont conservés, les arêtes cachées sont en tirets ; en revanche les angles et les longueurs des fuyantes sont déformés, et un dessin ne prouve jamais rien à lui seul.

## 🛤️ Droites parallèles : un plan, une direction

Dans le tétraèdre ABCD, I est le milieu de [AB] et J celui de [CD] ; K est le milieu de [IJ] et L celui de [BJ]. Sur le dessin, la droite (KL) a l'air parallèle à (AB), mais le dessin aplatit l'espace.
Que faut-il vérifier pour que cette impression devienne une preuve ?

::: definition
Deux droites de l'espace sont **parallèles** lorsqu'un même plan les contient et qu'elles y sont parallèles au sens de la géométrie plane.
Deux droites parallèles sont **confondues**, ou **strictement parallèles** quand elles sont distinctes et sans point commun.
:::

::: figure Le tétraèdre ABCD : le plan teinté (IBJ) contient (AB), en orange, et (KL), en vert ; c'est ce plan commun qui rend le parallélisme possible
<svg viewBox="20 -6 276 252"><path d="M158 222 L272 222 L185 96.2 Z" fill="#0f6e56" opacity="0.13"/><path d="M272 222 L137.5 174.1" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M44 222 L137.5 174.1" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M137.5 174.1 L232.5 18.3" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M44 222 L272 222" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M272 222 L232.5 18.3" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M44 222 L232.5 18.3" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M158 222 L185 96.2" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M272 222 L185 96.2" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M44 222 L272 222" fill="none" stroke="#b45309" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/><path d="M171.5 159.1 L228.5 159.1" fill="none" stroke="#0f6e56" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><g fill="#0f172a"><circle cx="44" cy="222" r="3.8"/><circle cx="272" cy="222" r="3.8"/><circle cx="137.5" cy="174.1" r="3.8"/><circle cx="232.5" cy="18.3" r="3.8"/></g><g fill="#94a3b8"><circle cx="158" cy="222" r="3.6"/><circle cx="185" cy="96.2" r="3.6"/></g><g fill="#0f6e56"><circle cx="171.5" cy="159.1" r="4.2"/><circle cx="228.5" cy="159.1" r="4.2"/></g><g font-size="15" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="33" y="234" text-anchor="middle" fill="#0f172a">A</text><text x="283" y="236" text-anchor="middle" fill="#0f172a">B</text><text x="125.5" y="170.1" text-anchor="middle" fill="#0f172a">C</text><text x="232.5" y="8.3" text-anchor="middle" fill="#0f172a">D</text><text x="158" y="239" text-anchor="middle" fill="#0f172a">I</text><text x="197" y="100.2" text-anchor="middle" fill="#0f172a">J</text><text x="160.5" y="162.1" text-anchor="middle" fill="#0f6e56">K</text><text x="225.5" y="150.1" text-anchor="middle" fill="#0f6e56">L</text></g></svg>
:::

Sur la figure, (AB) et (KL) sont toutes deux dans le plan teinté (IBJ) : on peut donc leur appliquer la géométrie plane.

::: exemple (KL) est parallèle à (AB), pas à pas

1. I, B et J ne sont pas alignés, car J n'est pas sur (AB) : sinon les quatre sommets seraient coplanaires. Ils déterminent le plan (IBJ), d'après l'axiome 1.
2. K est sur (IJ) et L sur (BJ), deux droites de ce plan : K et L sont dans (IBJ), d'après l'axiome 2.
3. Dans le triangle IBJ, K est le milieu de [IJ] et L celui de [BJ] : la droite des milieux donne (KL) ∥ (IB), car la géométrie plane vaut dans chaque plan (axiome 4).
4. (IB) est la droite (AB), puisque I est sur (AB). Les droites (KL) et (AB) sont dans un même plan et parallèles dans ce plan : elles sont parallèles dans l'espace, et distinctes, car K n'est pas sur (AB), sinon (IK) = (IJ) = (AB) contiendrait J.

:::

::: piege Conclure au parallélisme parce que le dessin le montre
Un élève écrit « (KL) ∥ (AB), ça se voit : elles sont toutes deux horizontales sur la figure ». Cela tente parce qu'en géométrie plane le dessin suffit souvent.
Mais le dessin est l'ombre aplatie d'un solide, et deux droites non coplanaires peuvent y paraître parallèles. Ici, c'est la preuve dans le plan (IBJ) qui décide : on la fait, on ne la lit pas.
:::

::: propriete

- Par un point A de l'espace passe une droite parallèle à une droite donnée Δ, et une seule : elle est dans le plan défini par Δ et A, où la géométrie plane donne une seule parallèle.
- Deux droites strictement parallèles sont contenues dans un plan, et un seul.

Cas limite : si A est sur Δ, la parallèle à Δ passant par A est Δ elle-même.
:::

::: verifie
Dans le même tétraèdre, montrer que (IL) est parallèle à (AJ).

---

A, B et J ne sont pas alignés : ils déterminent le plan (ABJ), qui contient I (sur (AB)) et L (sur (BJ)). Dans le triangle ABJ, I est le milieu de [AB] et L celui de [BJ] : la droite des milieux donne (IL) ∥ (AJ). Les deux droites sont parallèles dans un même plan, donc parallèles dans l'espace.
:::

::: retenir
Deux droites de l'espace sont parallèles quand un plan les contient et qu'elles y sont parallèles ; par un point passe une seule parallèle à une droite donnée, et deux parallèles strictes fixent un plan.
:::

## 🔗 Deux parallèles à une même droite, et le plan qui les traverse

Dans le tétraèdre ABCD, on joint les milieux I, J, K, L de [AB], [BC], [CD] et [DA]. Les quatre points semblent former un quadrilatère plat, aux côtés opposés parallèles ; pourtant rien ne dit qu'ils sont dans un même plan.
Comment le prouver, et peut-on alors parler de parallélogramme ?

::: figure Les milieux I, J, K et L des arêtes [AB], [BC], [CD] et [DA] : le quadrilatère IJKL est teinté ; (IJ) et (KL) ont la direction de l'arête (AC), (JK) et (IL) celle de (BD)
<svg viewBox="20 -6 276 252"><path d="M158 222 L204.7 198.1 L185 96.2 L138.2 120.2 Z" fill="#0f6e56" opacity="0.18"/><path d="M272 222 L137.5 174.1" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M44 222 L137.5 174.1" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M137.5 174.1 L232.5 18.3" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M44 222 L272 222" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M272 222 L232.5 18.3" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M44 222 L232.5 18.3" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M158 222 L204.7 198.1" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M204.7 198.1 L185 96.2" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M185 96.2 L138.2 120.2" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M138.2 120.2 L158 222" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/><g fill="#0f172a"><circle cx="44" cy="222" r="3.8"/><circle cx="272" cy="222" r="3.8"/><circle cx="137.5" cy="174.1" r="3.8"/><circle cx="232.5" cy="18.3" r="3.8"/></g><g fill="#0f6e56"><circle cx="158" cy="222" r="4.2"/><circle cx="204.7" cy="198.1" r="4.2"/><circle cx="185" cy="96.2" r="4.2"/><circle cx="138.2" cy="120.2" r="4.2"/></g><g font-size="15" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="33" y="234" text-anchor="middle" fill="#0f172a">A</text><text x="283" y="236" text-anchor="middle" fill="#0f172a">B</text><text x="125.5" y="170.1" text-anchor="middle" fill="#0f172a">C</text><text x="232.5" y="8.3" text-anchor="middle" fill="#0f172a">D</text><text x="158" y="239" text-anchor="middle" fill="#0f6e56">I</text><text x="217.7" y="204.1" text-anchor="middle" fill="#0f6e56">J</text><text x="198" y="92.2" text-anchor="middle" fill="#0f6e56">K</text><text x="126.2" y="118.2" text-anchor="middle" fill="#0f6e56">L</text></g></svg>
:::

Sur la figure, [IJ] et [KL] sont dans deux faces différentes, ABC et ACD, et pourtant elles ont toutes deux la direction de l'arête (AC).

::: exemple IJKL est un parallélogramme

1. Dans la face ABC, I et J sont les milieux de [AB] et [BC] : (IJ) ∥ (AC). Dans la face ACD, K et L sont les milieux de [CD] et [DA] : (KL) ∥ (AC), par la droite des milieux.
2. (IJ) et (KL) sont parallèles à une même droite, donc parallèles entre elles : on admet que deux droites parallèles à une même troisième sont parallèles.
3. Elles sont distinctes : sinon cette droite serait dans (ABC) et dans (ACD), donc égale à (AC), qui ne contient pas I. Deux droites strictement parallèles sont dans un plan : I, J, K, L sont coplanaires.
4. De même, (JK) et (IL) sont parallèles à (BD), dans les faces BCD et ABD, donc parallèles entre elles, et elles sont dans ce même plan puisque J, K, I, L y sont.
5. Dans ce plan, IJKL a ses côtés opposés parallèles deux à deux : c'est un parallélogramme.

:::

::: piege Déduire « parallélogramme » de côtés opposés égaux
Un élève calcule IJ = KL = AC/2 et JK = LI = BD/2, et conclut aussitôt « IJKL est un parallélogramme ». Cela tente parce que, dans un plan, des côtés opposés égaux deux à deux suffisent.
Mais dans l'espace ces égalités ne disent pas que les points sont coplanaires : le quadrilatère ABCD d'un tétraèdre où AB = CD et BC = DA a ses côtés opposés égaux et n'est pas plan. Il faut d'abord prouver le parallélisme, qui donne le plan.
:::

::: propriete

- Deux droites parallèles à une même troisième sont parallèles entre elles.
- Si deux droites sont parallèles, tout plan qui coupe l'une coupe aussi l'autre.

Cas limite : le point d'intersection est sur la droite, pas forcément sur le segment dessiné. Dans un cube ABCDEFGH, les arêtes (AE) et (CG) sont parallèles ; le plan (EBD) coupe (AE) en E, donc il coupe (CG), mais en un point situé sous C, hors de l'arête [CG].
:::

::: verifie
Dans un tétraèdre ABCD, M, N, Q et P sont les milieux de [AB], [AC], [CD] et [BD]. Montrer que MNQP est un parallélogramme.

---

Dans les faces ABC et BCD, (MN) ∥ (BC) et (PQ) ∥ (BC) par la droite des milieux : (MN) ∥ (PQ). Elles sont distinctes et parallèles, donc dans un même plan : M, N, Q, P sont coplanaires. De même (NQ) ∥ (AD) dans la face ACD et (MP) ∥ (AD) dans la face ABD : (NQ) ∥ (MP). Dans ce plan, les côtés opposés sont parallèles deux à deux : MNQP est un parallélogramme.
:::

::: retenir
Deux droites parallèles à une même troisième sont parallèles, et un plan qui coupe l'une de deux parallèles coupe l'autre ; deux parallèles strictes donnent un plan, donc un parallélogramme quand les côtés opposés sont parallèles deux à deux.
:::

## 🪟 Une droite parallèle à un plan

Le plan de la face BCGF d'un cube de verre est teinté comme une vitre. L'arête (EH) du dessus ne touche jamais cette vitre, même prolongée.
Est-ce du parallélisme, et comment le prouver sans mesurer de distance ?

::: definition
Une droite D est **parallèle à un plan** P lorsqu'elle est parallèle à une droite de P ; on écrit D // P.
Si de plus D et P n'ont aucun point commun, D est **strictement parallèle** à P.
:::

::: figure Le plan teinté (BCG) contient (FG), en vert ; la droite (EH), en orange, est parallèle à (FG), donc au plan
<svg viewBox="34 20 236 236"><path d="M196 230 L243.6 182.4 L243.6 46.4 L196 94 Z" fill="#0f6e56" opacity="0.14"/><path d="M243.6 182.4 L107.6 182.4" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M60 230 L107.6 182.4" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M107.6 182.4 L107.6 46.4" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M60 230 L196 230" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M196 230 L243.6 182.4" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M60 94 L196 94" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M196 94 L243.6 46.4" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M243.6 46.4 L107.6 46.4" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M60 94 L107.6 46.4" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M196 230 L196 94" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M60 230 L60 94" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M243.6 182.4 L243.6 46.4" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M196 94 L243.6 46.4" fill="none" stroke="#0f6e56" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/><path d="M60 94 L107.6 46.4" fill="none" stroke="#b45309" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/><g fill="#0f172a"><circle cx="60" cy="230" r="3.8"/><circle cx="196" cy="230" r="3.8"/><circle cx="243.6" cy="182.4" r="3.8"/><circle cx="107.6" cy="182.4" r="3.8"/><circle cx="60" cy="94" r="3.8"/><circle cx="196" cy="94" r="3.8"/><circle cx="243.6" cy="46.4" r="3.8"/><circle cx="107.6" cy="46.4" r="3.8"/></g><g font-size="15" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="49" y="242" text-anchor="middle" fill="#0f172a">A</text><text x="207" y="244" text-anchor="middle" fill="#0f172a">B</text><text x="256.6" y="188.4" text-anchor="middle" fill="#0f172a">C</text><text x="95.6" y="184.4" text-anchor="middle" fill="#0f172a">D</text><text x="48" y="91" text-anchor="middle" fill="#0f172a">E</text><text x="192" y="83" text-anchor="middle" fill="#0f172a">F</text><text x="256.6" y="42.4" text-anchor="middle" fill="#0f172a">G</text><text x="103.6" y="35.4" text-anchor="middle" fill="#0f172a">H</text></g></svg>
:::

Sur la figure, (FG) est la droite du plan à laquelle (EH) est parallèle : elle tient le rôle de la « droite de P » de la définition.

::: exemple (EH) est parallèle au plan (BCG)

1. E, F, G, H sont les sommets du carré de la face du dessus : (EH) ∥ (FG), côtés opposés d'un carré.
2. F et G sont dans le plan (BCG), donc (FG) ⊂ (BCG), d'après l'axiome 2.
3. (EH) est parallèle à une droite du plan : (EH) // (BCG).
4. Elle est même strictement parallèle : un point commun M à (EH) et à (BCG) serait dans le plan de la face EFGH, qui coupe (BCG) suivant (FG) ; M serait alors sur (FG) et sur (EH), strictement parallèles, ce qui est impossible.

:::

::: piege Croire qu'une droite parallèle à un plan l'est à toutes ses droites
Un élève écrit « (EH) // (BCG), donc (EH) ∥ (BG), puisque (BG) est dans ce plan ». Cela tente parce que « parallèle au plan » sonne comme « parallèle à tout ce qu'il contient ».
Mais (EH) n'est parallèle qu'aux droites du plan qui ont sa direction, comme (FG) et (BC). Avec (BG), elle n'a aucun point commun et aucun plan ne les contient toutes deux : elles sont non coplanaires.
:::

::: propriete

- D // P équivaut à : D est parallèle à une droite de P.
- Si D est parallèle à P, toute droite parallèle à D qui passe par un point de P est contenue dans P : la parallèle à (EH) menée par F est (FG), dans (BCG).
- Si deux droites sont parallèles, tout plan parallèle à l'une est parallèle à l'autre : (AD) ∥ (EH) et (EH) // (BCG), donc (AD) // (BCG).

Cas limite : une droite contenue dans P est parallèle à P, mais pas strictement : (FG) // (BCG).
:::

::: verifie
Dans le même cube, la droite (AE) est-elle parallèle au plan (BCG) ? Est-elle strictement parallèle ?

---

(AE) ∥ (BF), côtés opposés du carré ABFE, et (BF) ⊂ (BCG) car B et F sont dans ce plan : (AE) // (BCG). Elle est strictement parallèle : un point commun serait dans le plan de la face ABFE, qui coupe (BCG) suivant (BF), donc sur (BF) et sur (AE), strictement parallèles, ce qui est impossible.
:::

::: retenir
Une droite est parallèle à un plan quand elle est parallèle à l'une de ses droites, pas à toutes ; la parallèle menée d'un point du plan à une droite parallèle à ce plan reste dans le plan.
:::

## 🏠 Le théorème du toit

Un toit à deux pans : les deux gouttières sont des droites parallèles, et chaque pan est un plan qui contient l'une d'elles. Les deux pans se rejoignent suivant le faîte.
Le faîte est-il parallèle aux gouttières, ou les coupe-t-il ? La même question se pose dans une pyramide dont la base est un trapèze : les deux côtés parallèles de la base jouent le rôle des gouttières.

::: figure La pyramide SABCD, de base le trapèze ABCD avec (AB) ∥ (CD) : les arêtes du plan (SAB) sont en vert, celles du plan (SCD) en orange, et la droite Δ passe par S
<svg viewBox="16 9 354 240"><path d="M240.6 33.2 L40 225 L260 225 Z" fill="#0f6e56" opacity="0.14"/><path d="M335.7 175.7 L186.1 175.7" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M40 225 L186.1 175.7" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M186.1 175.7 L240.6 33.2" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M40 225 L260 225" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M260 225 L335.7 175.7" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M40 225 L240.6 33.2" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M260 225 L240.6 33.2" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M335.7 175.7 L240.6 33.2" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M240.6 33.2 L335.7 175.7" fill="none" stroke="#b45309" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/><path d="M240.6 33.2 L186.1 175.7" fill="none" stroke="#b45309" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M335.7 175.7 L186.1 175.7" fill="none" stroke="#b45309" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M240.6 33.2 L40 225" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/><path d="M240.6 33.2 L260 225" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/><path d="M40 225 L260 225" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/><path d="M73.4 33.2 L346.2 33.2" fill="none" stroke="#0f172a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/><g fill="#0f172a"><circle cx="40" cy="225" r="3.8"/><circle cx="260" cy="225" r="3.8"/><circle cx="335.7" cy="175.7" r="3.8"/><circle cx="186.1" cy="175.7" r="3.8"/><circle cx="240.6" cy="33.2" r="3.8"/></g><g font-size="15" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="29" y="238" text-anchor="middle" fill="#0f172a">A</text><text x="271" y="239" text-anchor="middle" fill="#0f172a">B</text><text x="348.7" y="180.7" text-anchor="middle" fill="#0f172a">C</text><text x="175.1" y="173.7" text-anchor="middle" fill="#0f172a">D</text><text x="238.6" y="23.2" text-anchor="middle" fill="#0f172a">S</text></g><g font-size="16" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="347.2" y="25.2" text-anchor="middle" fill="#0f6e56">Δ</text></g></svg>
:::

Sur la figure, (AB) et (CD) sont les gouttières, les plans (SAB) et (SCD) les deux pans, et Δ la droite que l'on cherche : leur intersection.

::: exemple Construire (SAB) ∩ (SCD)

1. S est commun aux deux plans, qui sont distincts : leur intersection est une droite Δ passant par S, d'après l'axiome 3.
2. (AB) est dans (SAB) et parallèle à (CD), donc parallèle au plan (SCD) ; elle est aussi parallèle au plan (SAB) qui la contient.
3. (AB) est donc parallèle à deux plans sécants : elle est parallèle à leur droite d'intersection, d'après la propriété ci-dessous. Ainsi Δ ∥ (AB), et aussi Δ ∥ (CD).
4. Δ est la parallèle à (AB) menée par S : elle est tracée sur la figure.

:::

::: piege Appliquer le toit à deux droites qui ne sont pas parallèles
Pour construire (SAD) ∩ (SBC), un élève trace de même la parallèle à (AD) passant par S. Cela tente parce que la même pyramide vient de donner une parallèle par S.
Mais (AD) et (BC) sont les côtés non parallèles du trapèze : ils se coupent en un point M, commun aux deux plans. L'intersection est la droite (SM), parallèle ni à (AD) ni à (BC).
:::

::: propriete

- Si une droite est parallèle à deux plans sécants, elle est parallèle à leur droite d'intersection.
- **Théorème du toit** : si D et D′ sont parallèles, si P contient D et P′ contient D′, et si P et P′ sont sécants suivant Δ, alors Δ est parallèle à D et à D′.

Cas limite : si D et D′ se coupent en un point M, Δ passe par M et n'est en général parallèle ni à D ni à D′ : le théorème exige des droites parallèles.
:::

::: verifie
La base de la pyramide SABCD est cette fois un parallélogramme (AB ∥ CD et AD ∥ BC). Construire (SAD) ∩ (SBC).

---

S est commun aux deux plans, qui sont distincts : l'intersection est une droite Δ′ passant par S. Ici (AD) ∥ (BC), avec (AD) ⊂ (SAD) et (BC) ⊂ (SBC) : le théorème du toit s'applique, et Δ′ est la parallèle à (AD) et à (BC) menée par S.
:::

::: retenir
Si deux plans sécants contiennent chacun l'une de deux droites parallèles, leur droite d'intersection leur est parallèle ; sans parallélisme des deux droites, elle passe par leur point commun.
:::

## 🏢 Plans parallèles : ce que cela entraîne

Deux planchers consécutifs d'un immeuble sont des plans parallèles. Un câble tendu sur l'un est-il parallèle à l'autre ?
Un poteau qui traverse le premier plancher traverse-t-il le second ?

::: definition
Deux plans sont **parallèles** lorsqu'ils n'ont aucun point commun ou lorsqu'ils sont confondus.
Quand ils n'ont aucun point commun, ils sont **strictement parallèles**.
:::

::: figure Les plans P et Q sont strictement parallèles ; la droite en orange perce P en M et ressort en N par Q
<svg viewBox="6 27 306 231"><path d="M30 215 L242.8 215 L288 169.8 L75.2 169.8 Z" fill="#0f6e56" opacity="0.12"/><path d="M30 215 L242.8 215 L288 169.8 L75.2 169.8 Z" fill="none" stroke="#0f172a" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/><path d="M30 116.2 L242.8 116.2 L288 71 L75.2 71 Z" fill="#0f6e56" opacity="0.12"/><path d="M30 116.2 L242.8 116.2 L288 71 L75.2 71 Z" fill="none" stroke="#0f172a" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/><path d="M105.4 234.6 L212.6 51.4" fill="none" stroke="#b45309" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/><g fill="#b45309"><circle cx="127.8" cy="196.4" r="4.4"/><circle cx="190.2" cy="89.6" r="4.4"/></g><g font-size="15" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="138.8" y="211.4" text-anchor="middle" fill="#b45309">M</text><text x="201.2" y="83.6" text-anchor="middle" fill="#b45309">N</text></g><g font-size="16" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="234.8" y="207" text-anchor="middle" fill="#0f6e56">P</text></g><g font-size="16" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="234.8" y="108.2" text-anchor="middle" fill="#0f6e56">Q</text></g></svg>
:::

Sur la figure, la droite qui perce P en M rencontre aussi Q en N : c'est l'une des trois conséquences du parallélisme de deux plans.

::: exemple Dans le cube, (ABC) et (EFG)

Les plans (ABC) et (EFG) sont ceux de la base et du dessus d'un cube ABCDEFGH : ils sont strictement parallèles.

1. (BD) est dans (ABC), et (BD) ∥ (FH) car BDHF est un rectangle ; (FH) est dans (EFG). Donc (BD) est parallèle au plan (EFG).
2. I et J sont les milieux de [AE] et de [BF] : (IJ) ∥ (AB), droite des milieux du rectangle ABFE, donc (IJ) est parallèle au plan (ABC). Elle l'est aussi à (EFG), qui est parallèle à (ABC).
3. (AG) perce (ABC) en A. Elle perce aussi (EFG) : G est sur (AG) et dans (EFG), c'est son point commun avec ce plan.

:::

::: piege Croire toutes les droites de deux plans parallèles parallèles entre elles
Un élève affirme que (BD) et (EG) sont parallèles, puisqu'elles sont dans deux plans parallèles. Cela tente parce que les plans le sont.
Mais (BD) est parallèle au plan (EFG), pas à chacune de ses droites : (BD) ∥ (FH), pas à (EG). Les droites (BD) et (EG) n'ont aucun point commun et aucun plan ne les contient : elles sont non coplanaires.
:::

::: propriete
Si deux plans P et Q sont parallèles, alors :

- toute droite de P est parallèle à Q ;
- toute droite parallèle à P est parallèle à Q ;
- toute droite qui perce P perce aussi Q.

Cas limite : si P et Q sont confondus, toute droite de P est dans Q : elle lui est parallèle, mais pas strictement.
:::

::: verifie
Dans le même cube, I est le milieu de [AE]. Montrer que (BI) est parallèle au plan (DCG).

---

(BI) est dans le plan (ABF) ; les faces opposées ABFE et DCGH sont dans des plans parallèles, (ABF) ∥ (DCG). Toute droite de l'un de deux plans parallèles est parallèle à l'autre : (BI) // (DCG).
:::

::: retenir
Si deux plans sont parallèles, toute droite de l'un est parallèle à l'autre, toute parallèle à l'un l'est à l'autre, et toute droite qui perce l'un perce l'autre ; mais leurs droites ne sont pas toutes parallèles entre elles.
:::

## 🧭 Prouver que deux plans sont parallèles

Dans la pyramide SABCD de base carrée, I, J et K sont les milieux de [SA], [SB] et [SC]. Le plan (IJK) semble flotter au-dessus du plan de la base (ABC). Comment prouver que ces deux plans ne se rencontrent jamais, sans parcourir l'espace pour le vérifier ?

::: figure La pyramide SABCD, de base le carré ABCD ; les points I, J, K sont les milieux de [SA], [SB], [SC] et le plan (IJK) est teinté
<svg viewBox="16 15 306 234"><path d="M104.5 131.9 L205.7 131.9 L233.4 104.2 Z" fill="#0f6e56" opacity="0.22"/><path d="M297.8 169.6 L95.4 169.6" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M40 225 L95.4 169.6" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M95.4 169.6 L168.9 38.9" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M40 225 L242.4 225" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M242.4 225 L297.8 169.6" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M40 225 L168.9 38.9" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M242.4 225 L168.9 38.9" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M297.8 169.6 L168.9 38.9" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M104.5 131.9 L205.7 131.9" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/><path d="M205.7 131.9 L233.4 104.2" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/><path d="M104.5 131.9 L233.4 104.2" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><g fill="#0f172a"><circle cx="40" cy="225" r="3.8"/><circle cx="242.4" cy="225" r="3.8"/><circle cx="297.8" cy="169.6" r="3.8"/><circle cx="95.4" cy="169.6" r="3.8"/><circle cx="168.9" cy="38.9" r="3.8"/></g><g fill="#0f6e56"><circle cx="104.5" cy="131.9" r="4.2"/><circle cx="205.7" cy="131.9" r="4.2"/><circle cx="233.4" cy="104.2" r="4.2"/></g><g font-size="15" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="29" y="238" text-anchor="middle" fill="#0f172a">A</text><text x="253.4" y="239" text-anchor="middle" fill="#0f172a">B</text><text x="310.8" y="174.6" text-anchor="middle" fill="#0f172a">C</text><text x="84.4" y="167.6" text-anchor="middle" fill="#0f172a">D</text><text x="166.9" y="28.9" text-anchor="middle" fill="#0f172a">S</text><text x="93.5" y="135.9" text-anchor="middle" fill="#0f6e56">I</text><text x="217.7" y="135.9" text-anchor="middle" fill="#0f6e56">J</text><text x="246.4" y="107.2" text-anchor="middle" fill="#0f6e56">K</text></g></svg>
:::

Sur la figure, la droite (IJ) est dessinée parallèle à (AB), et (JK) parallèle à (BC) : ce sont ces deux directions qui décident.

::: exemple (IJK) est parallèle à (ABC)

1. Dans le triangle SAB, I et J sont les milieux de [SA] et [SB] : (IJ) ∥ (AB), par la droite des milieux.
2. Dans le triangle SBC, J et K sont les milieux de [SB] et [SC] : (JK) ∥ (BC).
3. I, J, K ne sont pas alignés, sinon (AB) et (BC) seraient parallèles, alors qu'elles se coupent en B. Donc (IJ) et (JK) sont deux droites sécantes en J, contenues dans (IJK).
4. (AB) et (BC) sont deux droites sécantes en B, contenues dans (ABC), et chacune est parallèle à l'une des deux autres : le plan (IJK) est parallèle au plan (ABC).

:::

::: piege Croire qu'une seule paire de parallèles suffit
Un élève remarque que (FG) ∥ (BC) dans le cube ABCDEFGH, avec (BC) dans (ABC) et (FG) dans (DFG), et conclut (ABC) // (DFG). Cela tente parce qu'une paire de parallèles est un vrai indice.
Mais il en faut deux, de directions différentes : les plans (ABC) et (DFG) ont en commun le point D, ils sont sécants. Une seule direction commune laisse les plans libres de se croiser.
:::

::: propriete

- Deux plans sont parallèles dès que deux droites sécantes de l'un sont parallèles à deux droites sécantes de l'autre.
- Par un point de l'espace passe un plan parallèle à un plan donné, et un seul : on le construit avec ce critère.
- Deux plans parallèles à un même troisième sont parallèles entre eux.

Cas limite : si les deux droites de l'un étaient parallèles entre elles, le critère ne prouverait rien : il faut des droites sécantes.
:::

::: verifie
Dans la même pyramide, I′, J′ et K′ sont les points de [SA], [SB] et [SC] tels que SI′ = (1/3) SA, SJ′ = (1/3) SB et SK′ = (1/3) SC. Montrer que (I′J′K′) // (ABC).

---

Dans le triangle SAB, SI′/SA = SJ′/SB = 1/3 : la réciproque de Thalès donne (I′J′) ∥ (AB). De même dans SBC, (J′K′) ∥ (BC). Les droites (I′J′) et (J′K′) sont sécantes en J′, (AB) et (BC) sécantes en B, et elles sont parallèles deux à deux : par le critère, les plans (I′J′K′) et (ABC) sont parallèles.
:::

::: retenir
Pour prouver que deux plans sont parallèles, on montre que deux droites sécantes de l'un sont parallèles à deux droites sécantes de l'autre ; une seule direction commune ne suffit pas.
:::

## 🔪 Un plan qui coupe deux plans parallèles

Dans un tétraèdre ABCD, I est le point de [DA] tel que DI = (2/5) DA. Le plan qui passe par I parallèlement à la base (ABC) coupe [DB] en J et [DC] en K ; la base mesure BC = 10 cm. Que mesure JK ?

::: figure Le tétraèdre ABCD coupé par le plan (IJK), parallèle à la base (ABC) : les points I, J et K sont sur les arêtes [DA], [DB] et [DC]
<svg viewBox="20 -6 276 252"><path d="M157.1 99.8 L248.3 99.8 L194.5 80.6 Z" fill="#0f6e56" opacity="0.22"/><path d="M272 222 L137.5 174.1" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M44 222 L137.5 174.1" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M137.5 174.1 L232.5 18.3" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M44 222 L272 222" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M272 222 L232.5 18.3" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M44 222 L232.5 18.3" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M157.1 99.8 L248.3 99.8" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/><path d="M248.3 99.8 L194.5 80.6" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M157.1 99.8 L194.5 80.6" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><g fill="#0f172a"><circle cx="44" cy="222" r="3.8"/><circle cx="272" cy="222" r="3.8"/><circle cx="137.5" cy="174.1" r="3.8"/><circle cx="232.5" cy="18.3" r="3.8"/></g><g fill="#0f6e56"><circle cx="157.1" cy="99.8" r="4.2"/><circle cx="248.3" cy="99.8" r="4.2"/><circle cx="194.5" cy="80.6" r="4.2"/></g><g font-size="15" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="33" y="234" text-anchor="middle" fill="#0f172a">A</text><text x="283" y="236" text-anchor="middle" fill="#0f172a">B</text><text x="125.5" y="170.1" text-anchor="middle" fill="#0f172a">C</text><text x="232.5" y="8.3" text-anchor="middle" fill="#0f172a">D</text><text x="145.1" y="103.8" text-anchor="middle" fill="#0f6e56">I</text><text x="261.3" y="102.8" text-anchor="middle" fill="#0f6e56">J</text><text x="182.5" y="78.6" text-anchor="middle" fill="#0f6e56">K</text></g></svg>
:::

Sur la figure, le plan (DAB) coupe les deux plans parallèles suivant (AB) et (IJ), et le plan (DBC) suivant (BC) et (JK).

::: exemple La longueur JK

1. Le plan (DAB) coupe les plans parallèles (ABC) et (IJK) suivant (AB) et (IJ) : ces droites sont parallèles, car un même plan coupe deux plans parallèles suivant des droites parallèles.
2. Dans le triangle DAB, (IJ) ∥ (AB) : le théorème de Thalès donne DJ/DB = DI/DA = 2/5.
3. Le plan (DBC) coupe les mêmes plans parallèles suivant (BC) et (JK) : (JK) ∥ (BC).
4. Dans le triangle DBC, Thalès donne JK/BC = DJ/DB = 2/5, donc JK = (2/5) × 10 = 4 cm.

:::

::: piege Rapprocher deux droites d'intersection venues de deux plans sécants différents
Un élève écrit « (IJ) ∥ (BC) : l'une est dans (IJK), l'autre dans (ABC), qui sont parallèles ». Cela tente parce que la phrase « deux droites dans deux plans parallèles » semble suffire.
Mais (AB) et (IJ) sont parallèles parce qu'elles sont les traces d'un même plan, (DAB). (BC) vient d'un autre plan, (DBC) : (IJ) est parallèle à (AB), et (AB) coupe (BC) en B, donc (IJ) n'est pas parallèle à (BC).
:::

::: propriete
Si deux plans P et P′ sont parallèles, tout plan qui coupe P coupe aussi P′, et les deux droites d'intersection sont parallèles.

Cas limite : si P et P′ sont confondus, les deux droites d'intersection sont confondues : parallèles, mais pas strictement.
:::

::: verifie
Dans le même tétraèdre, AC = 12,5 cm. Calculer IK.

---

Le plan (DAC) coupe les plans parallèles (ABC) et (IJK) suivant (AC) et (IK) : (IK) ∥ (AC). Dans le triangle DAC, Thalès donne IK/AC = DI/DA = 2/5, donc IK = (2/5) × 12,5 = 5 cm.
:::

::: retenir
Un même plan qui coupe deux plans parallèles les coupe suivant deux droites parallèles ; on y applique Thalès dans le plan sécant, jamais entre des droites venues de plans sécants différents.
:::

## 🧀 Sections planes d'un solide

Un cube de fromage ABCDEFGH est tranché par un plan qui passe par trois points marqués : I milieu de [HE], J milieu de [AE] et K milieu de [CG]. La coupe est un polygone.
Combien a-t-il de côtés, et comment le tracer sans dessiner d'abord tout le plan ?

::: definition
La **section** d'un solide par un plan est l'ensemble de leurs points communs ; pour un polyèdre convexe, c'est un polygone dont chaque côté est dans une face du solide.
:::

::: figure Le cube ABCDEFGH et le plan (IJK) : la section est l'hexagone IJLNKP ; M est un point auxiliaire, sur le prolongement de [DH] au-dessus de H
<svg viewBox="34 -57 257 333"><path d="M86.6 71.4 L60 174 L136 250 L238.6 223.4 L265.2 120.8 L189.2 44.8 Z" fill="#0f6e56" opacity="0.2"/><path d="M265.2 196.8 L113.2 196.8" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M60 250 L113.2 196.8" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M113.2 196.8 L113.2 44.8" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M60 250 L212 250" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M212 250 L265.2 196.8" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M60 98 L212 98" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M212 98 L265.2 44.8" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M265.2 44.8 L113.2 44.8" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M60 98 L113.2 44.8" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M212 250 L212 98" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M60 250 L60 98" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M265.2 196.8 L265.2 44.8" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M86.6 71.4 L113.2 -31.2" fill="none" stroke="#94a3b8" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/><path d="M60 174 L86.6 71.4" fill="none" stroke="#94a3b8" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/><path d="M113.2 44.8 L113.2 -31.2" fill="none" stroke="#94a3b8" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/><path d="M113.2 -31.2 L189.2 44.8" fill="none" stroke="#94a3b8" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/><path d="M86.6 71.4 L60 174" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M60 174 L136 250" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/><path d="M136 250 L238.6 223.4" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M238.6 223.4 L265.2 120.8" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/><path d="M265.2 120.8 L189.2 44.8" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M189.2 44.8 L86.6 71.4" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/><g fill="#0f172a"><circle cx="60" cy="250" r="3.8"/><circle cx="212" cy="250" r="3.8"/><circle cx="265.2" cy="196.8" r="3.8"/><circle cx="113.2" cy="196.8" r="3.8"/><circle cx="60" cy="98" r="3.8"/><circle cx="212" cy="98" r="3.8"/><circle cx="265.2" cy="44.8" r="3.8"/><circle cx="113.2" cy="44.8" r="3.8"/></g><g fill="#0f6e56"><circle cx="86.6" cy="71.4" r="4.2"/><circle cx="60" cy="174" r="4.2"/><circle cx="136" cy="250" r="4.2"/><circle cx="238.6" cy="223.4" r="4.2"/><circle cx="265.2" cy="120.8" r="4.2"/><circle cx="189.2" cy="44.8" r="4.2"/></g><g font-size="15" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="49" y="262" text-anchor="middle" fill="#0f172a">A</text><text x="223" y="264" text-anchor="middle" fill="#0f172a">B</text><text x="278.2" y="202.8" text-anchor="middle" fill="#0f172a">C</text><text x="101.2" y="198.8" text-anchor="middle" fill="#0f172a">D</text><text x="48" y="110" text-anchor="middle" fill="#0f172a">E</text><text x="208" y="113" text-anchor="middle" fill="#0f172a">F</text><text x="278.2" y="40.8" text-anchor="middle" fill="#0f172a">G</text><text x="99.2" y="50.8" text-anchor="middle" fill="#0f172a">H</text><text x="74.6" y="65.4" text-anchor="middle" fill="#0f6e56">I</text><text x="48" y="178" text-anchor="middle" fill="#0f6e56">J</text><text x="278.2" y="124.8" text-anchor="middle" fill="#0f6e56">K</text><text x="136" y="267" text-anchor="middle" fill="#0f6e56">L</text><text x="251.6" y="235.4" text-anchor="middle" fill="#0f6e56">N</text><text x="189.2" y="33.8" text-anchor="middle" fill="#0f6e56">P</text></g><g fill="#0f172a"><circle cx="113.2" cy="-31.2" r="4.2"/></g><g font-size="15" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="101.2" y="-35.2" text-anchor="middle" fill="#0f172a">M</text></g></svg>
:::

Sur la figure, chaque côté de l'hexagone est dans une face : IJ dans la face ADHE, JL dans ABFE, LN dans ABCD, NK dans BCGF, KP dans CDHG, PI dans EFGH.

::: exemple La section du cube par (IJK)

1. I et J sont dans la face ADHE : le segment [IJ] est un côté de la section.
2. Dans cette face, (IJ) ∥ (AH), droite des milieux du triangle EAH, et (AH) coupe (DH) : (IJ) et (DH) se coupent en un point M, commun au plan (IJK) et au plan de la face CDHG.
3. K et M sont dans la face CDHG : la trace du plan sur cette face est (MK), qui coupe [GH] en P. Le côté est [KP].
4. Les faces ADHE et BCGF sont parallèles : le plan, qui coupe ADHE suivant (IJ), coupe BCGF suivant la parallèle à (IJ) menée par K, qui rencontre [BC] en N. Le côté est [KN].
5. De même, CDHG et ABFE sont parallèles : la trace sur ABFE est la parallèle à (MK) menée par J, qui rencontre [AB] en L. Le côté est [JL].
6. Sur EFGH et sur ABCD, on joint P à I, puis L à N : ces deux côtés sont parallèles, les faces étant parallèles. La section est l'hexagone IJLNKP, un côté par face. On peut vérifier que ses sommets sont les milieux de six arêtes.

:::

::: piege Joindre deux points qui ne sont pas dans une même face
Un élève relie I à K « parce que ce sont deux points du plan ». Cela tente parce que (IK) est bien contenue dans le plan (IJK).
Mais [IK] traverse l'intérieur du cube : I est sur [HE], K sur [CG], et aucune face ne contient les deux. Un côté de section est toujours dans une face : on ne joint que deux points d'une même face.
:::

::: methode Tracer la section d'un solide par un plan

1. Joindre deux points donnés qui sont dans une même face : c'est un côté.
2. Prolonger ce côté jusqu'à une arête d'une autre face : on obtient un point auxiliaire, commun au plan et à cette face, comme M.
3. Dans une face parallèle à une face déjà traitée, tracer la parallèle au côté déjà obtenu.
4. Fermer le polygone : un côté par face traversée, donc six au plus pour un cube.

Cas limite : si le côté tracé est parallèle à l'arête que l'on voulait couper, il n'y a pas de point auxiliaire : la trace sur la face voisine est alors parallèle à ce côté.
:::

::: verifie
Pour la même section, justifier que le côté de la section sur la face ABCD est parallèle à [PI].

---

Les faces ABCD et EFGH sont parallèles. Le plan (IJK) coupe EFGH suivant (PI) et ABCD suivant (LN) : un même plan qui coupe deux plans parallèles les coupe suivant des droites parallèles, donc (LN) ∥ (PI).
:::

::: retenir
La section d'un cube par un plan a un côté par face traversée, six au plus ; on la trace en joignant deux points d'une même face, en cherchant un point auxiliaire, puis en menant des parallèles dans les faces parallèles.
:::

> 🏆 Quête franchie, héros : tu sais prouver que des droites sont parallèles, enchaîner les parallèles, reconnaître une droite parallèle à un plan, appliquer le théorème du toit, utiliser des plans parallèles, prouver leur parallélisme, couper deux plans parallèles par un troisième et tracer la section d'un solide. Le chapitre suivant ajoute l'orthogonalité.
