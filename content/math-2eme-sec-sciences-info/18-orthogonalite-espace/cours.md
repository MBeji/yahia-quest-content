# ⚔️ Orthogonalité dans l'espace — l'angle droit qui ne se touche pas

> 💡 «Dans l'espace, deux droites peuvent former un angle droit sans jamais se rencontrer : savoir le voir, puis le prouver, c'est lire une salle, un pylône ou un solide comme un architecte.»

Au chapitre précédent, le parallélisme est devenu un outil : on s'en sert ici sans le redémontrer, avec le théorème de Pythagore et les aires du triangle.
Huit étapes conduisent aux angles droits de l'espace : droites orthogonales, droite perpendiculaire à un plan, projeté orthogonal, perpendiculaires et parallèles, théorème des trois perpendiculaires, plan médiateur, axe d'un cercle, plans perpendiculaires. Sur tous les dessins, les arêtes cachées sont en tirets.

## 📐 Droites orthogonales : un angle droit sans point commun

Sur une boîte à chaussures, l'arête [AB] du fond et l'arête verticale [CC′] de l'autre côté ne se touchent pas, et pourtant elles semblent « à angle droit ».
Comment mesurer l'angle de deux droites qui ne se coupent pas ?

::: definition
Deux droites de l'espace sont **orthogonales** lorsque leurs parallèles menées par un même point sont perpendiculaires (par un point, il passe une seule parallèle à une droite donnée).
Deux droites **perpendiculaires** sont deux droites orthogonales qui se coupent. On écrit (AB) ⊥ (CC′).
:::

::: figure Dans le cube ABCDA′B′C′D′, la parallèle à (CC′) menée par B est (BB′) : elle est perpendiculaire à (AB), donc (AB) et (CC′) sont orthogonales sans point commun
<svg viewBox="10 6 199 199"><path d="M185.2 142 L73.2 142" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M34 181.2 L73.2 142" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M73.2 142 L73.2 30" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M34 181.2 L146 181.2" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M146 181.2 L185.2 142" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M34 69.2 L146 69.2" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M146 69.2 L185.2 30" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M185.2 30 L73.2 30" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M34 69.2 L73.2 30" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M146 181.2 L146 69.2" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M34 181.2 L34 69.2" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M185.2 142 L185.2 30" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M34 181.2 L146 181.2" fill="none" stroke="#0f6e56" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/><path d="M185.2 142 L185.2 30" fill="none" stroke="#b45309" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/><path d="M146 181.2 L146 69.2" fill="none" stroke="#b45309" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/><path d="M130.6 181.2 L130.6 165.8 L146 165.8" fill="none" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/><g fill="#0f172a"><circle cx="34" cy="181.2" r="3.8"/><circle cx="146" cy="181.2" r="3.8"/><circle cx="185.2" cy="142" r="3.8"/><circle cx="73.2" cy="142" r="3.8"/><circle cx="34" cy="69.2" r="3.8"/><circle cx="146" cy="69.2" r="3.8"/><circle cx="185.2" cy="30" r="3.8"/><circle cx="73.2" cy="30" r="3.8"/></g><g font-size="15" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="23" y="193.2" text-anchor="middle" fill="#0f172a">A</text><text x="157" y="195.2" text-anchor="middle" fill="#0f172a">B</text><text x="198.2" y="146" text-anchor="middle" fill="#0f172a">C</text><text x="62.2" y="140" text-anchor="middle" fill="#0f172a">D</text><text x="22" y="67.2" text-anchor="middle" fill="#0f172a">A′</text><text x="150" y="60.2" text-anchor="middle" fill="#0f172a">B′</text><text x="198.2" y="25" text-anchor="middle" fill="#0f172a">C′</text><text x="69.2" y="20" text-anchor="middle" fill="#0f172a">D′</text></g></svg>
:::

Sur la figure, on a fait glisser (CC′) le long de la face jusqu'en (BB′) : l'angle droit marqué en B est l'angle des deux droites de départ.

::: exemple La boîte : (AB) et (CC′)

1. On mène par B la parallèle à (CC′) : c'est (BB′), car BCC′B′ est un rectangle dont les côtés opposés [BB′] et [CC′] sont parallèles.
2. (BB′) et (AB) se coupent en B à angle droit, car ABB′A′ est une face carrée du cube.
3. Les parallèles menées par B aux deux droites sont donc perpendiculaires : (AB) et (CC′) sont orthogonales, bien qu'elles n'aient aucun point commun.

:::

::: exemple Deux diagonales de faces : (AB′) et (CD′)

1. A′D′CB est un rectangle, car [BC] et [A′D′] sont parallèles et de même longueur : (CD′) est parallèle à (BA′).
2. (AB′) et (BA′) sont les deux diagonales du carré ABB′A′ : elles sont perpendiculaires.
3. Une parallèle à (BA′) est orthogonale à (AB′), donc (CD′) et (AB′) sont orthogonales, sans point commun et non parallèles.

:::

::: piege Croire que deux droites orthogonales se coupent
Un élève voit que (AB′) et (CD′) n'ont aucun point commun et conclut qu'elles ne peuvent pas former un angle droit. Cela tente parce que, dans un plan, un angle droit suppose que les droites se rencontrent.
Mais dans l'espace deux droites peuvent n'être ni sécantes ni parallèles : on mesure leur angle en les ramenant en un même point par des parallèles, comme dans la définition.
:::

::: propriete

- Si deux droites sont orthogonales, toute droite parallèle à l'une est orthogonale à l'autre.
- Deux droites perpendiculaires sont orthogonales ; la réciproque est fausse.

Cas limite : des droites parallèles ne sont jamais orthogonales, et des droites sécantes ne le sont que si leur angle est droit : (AB) et (AB′) se coupent en A avec un angle de 45°.
:::

::: verifie
Dans le cube ABCDA′B′C′D′, montrer que (A′B) et (DC′) sont orthogonales.

---

ADC′B′ est un rectangle, car [AD] et [B′C′] sont parallèles et de même longueur : (DC′) est parallèle à (AB′). Les droites (A′B) et (AB′) sont les diagonales du carré ABB′A′, donc perpendiculaires. Une parallèle à (AB′) est orthogonale à (A′B) : (DC′) et (A′B) sont orthogonales.
:::

::: retenir
Deux droites sont orthogonales quand leurs parallèles menées par un même point sont perpendiculaires : elles n'ont pas besoin de se couper, et des droites perpendiculaires sont des orthogonales qui se coupent.
:::

## 🚩 Droite perpendiculaire à un plan : deux directions suffisent

Un charpentier plante un mât [AM] de 4 m dans une cour plane. Il contrôle son équerre dans deux directions du sol, puis fixe un câble de M à un point C du sol situé à 3 m du pied A, hors de ces deux directions.
Pour calculer le câble par Pythagore, il faut un angle droit en A pour cette troisième direction aussi : deux contrôles suffisent-ils ?

::: definition
Une droite est **perpendiculaire à un plan** si et seulement si elle est orthogonale à deux droites sécantes de ce plan. On écrit D ⊥ P.
:::

::: figure Le mât [AM], contrôlé à l'équerre le long de (AB) et de (AD) : ces deux droites du sol sont sécantes en A, et le câble [MC] vise un point C hors de ces deux droites
<svg viewBox="-17 58 281 177"><path d="M5.4 212.6 L185.4 212.6 L242.1 155.9 L62.1 155.9 Z" fill="#0f6e56" opacity="0.1"/><path d="M5.4 212.6 L185.4 212.6 L242.1 155.9 L62.1 155.9 Z" fill="none" stroke="#94a3b8" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/><path d="M60 200 L162 200" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M60 200 L95.7 164.3" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M60 200 L139.2 174.8" fill="none" stroke="#0f6e56" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/><path d="M60 200 L60 80" fill="none" stroke="#0f172a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/><path d="M60 80 L139.2 174.8" fill="none" stroke="#b45309" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/><path d="M73.5 200 L73.5 186.5 L60 186.5" fill="none" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/><path d="M64.7 195.3 L64.7 181.8 L60 186.5" fill="none" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/><g fill="#0f172a"><circle cx="60" cy="200" r="3.8"/><circle cx="60" cy="80" r="3.8"/><circle cx="162" cy="200" r="3.8"/><circle cx="95.7" cy="164.3" r="3.8"/></g><g fill="#b45309"><circle cx="139.2" cy="174.8" r="3.8"/></g><g font-size="15" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="49" y="214" text-anchor="middle" fill="#0f172a">A</text><text x="60" y="70" text-anchor="middle" fill="#0f172a">M</text><text x="174" y="205" text-anchor="middle" fill="#0f172a">B</text><text x="107.7" y="169.3" text-anchor="middle" fill="#0f172a">D</text><text x="152.2" y="179.8" text-anchor="middle" fill="#b45309">C</text></g><g font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="50" y="144" text-anchor="middle" fill="#0f172a">4</text></g></svg>
:::

Sur la figure, les deux angles droits marqués en A sont les deux contrôles ; (AB) et (AD) sont les deux droites sécantes de la définition.

::: exemple Le câble du mât

1. (AM) est orthogonale à (AB) et à (AD), deux droites sécantes du sol : (AM) est perpendiculaire au sol, par définition.
2. Donc (AM) est orthogonale à toutes les droites du sol, en particulier à (AC) (propriété admise, énoncée plus bas) : le triangle AMC est rectangle en A.
3. MC² = AM² + AC² = 16 + 9 = 25, par le théorème de Pythagore : le câble mesure 5 m.

:::

::: figure Dans le tétraèdre régulier ABCD, I est le milieu de [CD] : (AI) et (BI) sont perpendiculaires à (CD) et définissent le plan (ABI)
<svg viewBox="21 -1 260 250"><path d="M162.6 22.8 L257.2 153.7 L115.3 207.2 Z" fill="#0f6e56" opacity="0.14"/><path d="M257.2 153.7 L44.8 189.4" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M44.8 189.4 L185.8 225.1" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M257.2 153.7 L185.8 225.1" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M162.6 22.8 L44.8 189.4" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M162.6 22.8 L185.8 225.1" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M162.6 22.8 L257.2 153.7" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M162.6 22.8 L115.3 207.2" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/><path d="M257.2 153.7 L115.3 207.2" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M162.6 22.8 L257.2 153.7" fill="none" stroke="#0f6e56" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/><path d="M127.1 210.2 L131.6 192.5 L119.9 189.5" fill="none" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/><g fill="#0f172a"><circle cx="162.6" cy="22.8" r="3.8"/><circle cx="257.2" cy="153.7" r="3.8"/><circle cx="44.8" cy="189.4" r="3.8"/><circle cx="185.8" cy="225.1" r="3.8"/></g><g fill="#0f6e56"><circle cx="115.3" cy="207.2" r="3.8"/></g><g font-size="15" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="162.6" y="12.8" text-anchor="middle" fill="#0f172a">A</text><text x="259.2" y="143.7" text-anchor="middle" fill="#0f172a">B</text><text x="32.8" y="199.4" text-anchor="middle" fill="#0f172a">C</text><text x="197.8" y="237.1" text-anchor="middle" fill="#0f172a">D</text><text x="115.3" y="224.2" text-anchor="middle" fill="#0f6e56">I</text></g></svg>
:::

::: exemple Les arêtes opposées d'un tétraèdre régulier

Dans un tétraèdre régulier ABCD (toutes les arêtes égales), I est le milieu de [CD]. Montrons que (AB) et (CD) sont orthogonales.

1. Le triangle ACD est équilatéral et I est le milieu de [CD] : la médiane (AI) est aussi une hauteur, donc (AI) ⊥ (CD).
2. De même dans BCD : (BI) ⊥ (CD).
3. (AI) et (BI) sont distinctes, sinon A, B, C et D seraient coplanaires ; elles se coupent en I : ce sont deux droites sécantes du plan (ABI).
4. (CD) est orthogonale à deux sécantes de (ABI), donc perpendiculaire à ce plan, donc orthogonale à toute droite de (ABI), en particulier à (AB).

:::

::: piege Se contenter d'une seule droite du plan
Dans le cube ABCDA′B′C′D′, un élève sait que (AD′) est orthogonale à (AB) et conclut que (AD′) est perpendiculaire au plan (ABC). Cela tente parce qu'une orthogonalité est déjà vérifiée.
Mais une seule droite ne suffit pas : (AD′) fait un angle de 45° avec (AD), autre droite de (ABC), car ADD′A′ est un carré dont (AD′) est une diagonale.
:::

::: propriete
Si une droite est perpendiculaire à un plan, elle est orthogonale à toutes les droites de ce plan (propriété admise).
Cas limite : cela vaut même pour les droites du plan qui ne la coupent pas : dans le cube, (AA′) est orthogonale à (BD), sans point commun.
:::

::: verifie
Un poteau [AM] de 12 m est contrôlé à l'équerre le long de deux droites sécantes du sol. Un câble relie M à un point C du sol, à 5 m du pied A, hors de ces deux droites. Quelle est sa longueur ?

---

Le poteau est orthogonal à deux sécantes du sol, donc perpendiculaire au sol, donc orthogonal à (AC) : AMC est rectangle en A. MC² = 12² + 5² = 144 + 25 = 169, donc MC = 13 m.
:::

::: retenir
Une droite orthogonale à deux droites sécantes d'un plan est perpendiculaire à ce plan, donc orthogonale à toutes ses droites ; une seule droite ne suffit pas.
:::

## ⬇️ Projeté orthogonal : la perpendiculaire issue d'un point

Dans une salle cubique d'arête 6 m, un projecteur est fixé au milieu I de l'arête [A′B′] du plafond A′B′C′D′. Le sol est ABCD.
Quel point du sol est à la verticale du projecteur, et quelle distance sépare I du coin C du sol ?

::: definition
Par un point M, il passe une seule droite perpendiculaire à un plan P, que M soit dans P ou non (propriété admise). Son point commun H avec P est le **projeté orthogonal** de M sur P.
Si M est dans P, son projeté est M lui-même. Par un point, il passe aussi un seul plan perpendiculaire à une droite donnée.
:::

::: figure La salle cubique d'arête 6 : J, milieu de [AB], est le projeté orthogonal de I sur le sol ; le triangle IJC est rectangle en J et la distance IC est en tirets, à l'intérieur du cube
<svg viewBox="10 6 250 250"><path d="M236.5 180 L86.5 180" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M34 232.5 L86.5 180" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M86.5 180 L86.5 30" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M34 232.5 L184 232.5" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M184 232.5 L236.5 180" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M34 82.5 L184 82.5" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M184 82.5 L236.5 30" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M236.5 30 L86.5 30" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M34 82.5 L86.5 30" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M184 232.5 L184 82.5" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M34 232.5 L34 82.5" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M236.5 180 L236.5 30" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M109 82.5 L109 232.5" fill="none" stroke="#0f6e56" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/><path d="M109 232.5 L236.5 180" fill="none" stroke="#b45309" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M109 215 L122.3 209.5 L122.3 227" fill="none" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/><g fill="#0f172a"><circle cx="34" cy="232.5" r="3.8"/><circle cx="184" cy="232.5" r="3.8"/><circle cx="236.5" cy="180" r="3.8"/><circle cx="86.5" cy="180" r="3.8"/><circle cx="34" cy="82.5" r="3.8"/><circle cx="184" cy="82.5" r="3.8"/><circle cx="236.5" cy="30" r="3.8"/><circle cx="86.5" cy="30" r="3.8"/><circle cx="109" cy="82.5" r="3.8"/><circle cx="109" cy="232.5" r="3.8"/></g><g font-size="15" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="23" y="244.5" text-anchor="middle" fill="#0f172a">A</text><text x="195" y="246.5" text-anchor="middle" fill="#0f172a">B</text><text x="249.5" y="184" text-anchor="middle" fill="#0f172a">C</text><text x="75.5" y="178" text-anchor="middle" fill="#0f172a">D</text><text x="22" y="80.5" text-anchor="middle" fill="#0f172a">A′</text><text x="188" y="73.5" text-anchor="middle" fill="#0f172a">B′</text><text x="249.5" y="25" text-anchor="middle" fill="#0f172a">C′</text><text x="82.5" y="20" text-anchor="middle" fill="#0f172a">D′</text><text x="109" y="72.5" text-anchor="middle" fill="#0f6e56">I</text><text x="109" y="249.5" text-anchor="middle" fill="#0f6e56">J</text></g><path d="M109 82.5 L236.5 180" fill="none" stroke="#b45309" stroke-width="3.0" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/></svg>
:::

Sur la figure, (IJ) est la perpendiculaire au sol menée par I : J est le point du sol à la verticale du projecteur.

::: exemple Le projecteur de la salle

1. A′I et AJ sont parallèles et égaux à 3 : AJIA′ est un rectangle, donc (IJ) est parallèle à (AA′).
2. (AA′) est orthogonale à (AB) et à (AD), car ce sont des faces carrées ; leur parallèle (IJ) l'est aussi. (AB) et (AD) sont sécantes dans le sol : (IJ) est perpendiculaire au sol et J est le projeté de I.
3. IJ = 6 et le triangle IJC est rectangle en J : JC² = JB² + BC² = 9 + 36 = 45, puis IC² = IJ² + JC² = 36 + 45 = 81, donc IC = 9 m.

:::

::: figure Le tétraèdre OABC avec OA = 2, OB = 3, OC = 6 : les angles en O sont droits, et (OC) est perpendiculaire au plan (OAB)
<svg viewBox="24 33 104 208"><path d="M50 215 L102 215 L77.3 187.7 Z" fill="#0f6e56" opacity="0.14"/><path d="M102 215 L77.3 187.7" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M77.3 187.7 L50 215" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M77.3 187.7 L50 59" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M102 215 L50 215" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M102 215 L50 59" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M50 59 L50 215" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M50 202 L63 202 L63 215" fill="none" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/><path d="M50 202 L54.5 197.4 L54.5 210.4" fill="none" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/><g fill="#0f172a"><circle cx="50" cy="215" r="3.8"/><circle cx="102" cy="215" r="3.8"/><circle cx="77.3" cy="187.7" r="3.8"/><circle cx="50" cy="59" r="3.8"/></g><g font-size="15" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="39" y="227" text-anchor="middle" fill="#0f172a">O</text><text x="114" y="228" text-anchor="middle" fill="#0f172a">A</text><text x="89.3" y="183.7" text-anchor="middle" fill="#0f172a">B</text><text x="50" y="49" text-anchor="middle" fill="#0f172a">C</text></g></svg>
:::

::: exemple La hauteur d'un tétraèdre

Rappel : le volume d'une pyramide vaut le tiers de l'aire de la base multipliée par la hauteur, la hauteur étant la distance du sommet à son projeté orthogonal sur la base.

1. (OC) est orthogonale à (OA) et à (OB), sécantes dans (OAB) : (OC) ⊥ (OAB), donc O est le projeté de C sur (OAB) et la hauteur vaut OC = 6.
2. OAB est rectangle en O : son aire vaut 2 × 3 / 2 = 3.
3. Volume : 3 × 6 / 3 = 6.

:::

::: piege Croire qu'un point du plan n'a pas de projeté
Un élève cherche le projeté de J, qui est déjà dans le sol, et répond qu'il n'existe pas, ou en trace plusieurs. Cela tente parce qu'on imagine toujours le point loin du plan.
Mais par J il passe une seule perpendiculaire au sol : elle le coupe en J lui-même, et le projeté de J est J.
:::

::: propriete

- Par un point, il passe une seule droite perpendiculaire à un plan, et un seul plan perpendiculaire à une droite.
- Si H est le projeté de M sur P, pour tout point N de P : MN² = MH² + HN², car (MH) est orthogonale à (HN).

Cas limite : si M est dans P, alors H = M et MH = 0.
:::

::: verifie
Dans un cube d'arête 4, I est le milieu de [A′B′] et J celui de [AB]. Calculer la distance IC, C étant un sommet du sol.

---

(IJ) est perpendiculaire au sol et J en est le projeté de I, donc IJC est rectangle en J. IJ = 4 et JC² = JB² + BC² = 4 + 16 = 20, donc IC² = 16 + 20 = 36 et IC = 6.
:::

::: retenir
Par un point de l'espace passe une seule perpendiculaire à un plan ; son pied est le projeté orthogonal, et MN² = MH² + HN² pour tout point N du plan.
:::

## 🧱 Perpendiculaires et parallèles : deux fils à plomb

Deux fils à plomb pendent d'un plafond plat, l'un de 7 dm et l'autre de 4 dm, accrochés à 4 dm l'un de l'autre. Les poids M et N sont-ils éloignés de beaucoup ?
Pour calculer comme dans un plan, il faut d'abord que les deux fils soient dans un même plan : rien ne le dit encore.

::: figure Les fils [AM] et [BN] sont perpendiculaires au plafond : parallèles, ils sont dans un même plan, en vert, où le point H est tel que (NH) soit parallèle à (AB)
<svg viewBox="-24 -27 244 262"><path d="M-4.3 45.7 L146.5 45.7 L199.2 -7 L48.4 -7 Z" fill="#94a3b8" opacity="0.16"/><path d="M-4.3 45.7 L146.5 45.7 L199.2 -7 L48.4 -7 Z" fill="none" stroke="#94a3b8" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/><path d="M50 33 L141.5 3.9 L141.5 107.9 L50 215 Z" fill="#0f6e56" opacity="0.12"/><path d="M50 33 L141.5 3.9" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M50 33 L50 215" fill="none" stroke="#0f172a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/><path d="M141.5 3.9 L141.5 107.9" fill="none" stroke="#0f172a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/><path d="M50 215 L141.5 107.9" fill="none" stroke="#b45309" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/><path d="M141.5 107.9 L50 137" fill="none" stroke="#b45309" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M61.7 33 L61.7 44.7 L50 44.7" fill="none" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/><path d="M50 125.3 L60.3 122 L60.3 133.7" fill="none" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/><g fill="#0f172a"><circle cx="50" cy="33" r="3.8"/><circle cx="141.5" cy="3.9" r="3.8"/><circle cx="50" cy="215" r="3.8"/><circle cx="141.5" cy="107.9" r="3.8"/></g><g fill="#b45309"><circle cx="50" cy="137" r="3.8"/></g><g font-size="15" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="38" y="29" text-anchor="middle" fill="#0f172a">A</text><text x="153.5" y="-0.1" text-anchor="middle" fill="#0f172a">B</text><text x="38" y="219" text-anchor="middle" fill="#0f172a">M</text><text x="154.5" y="112.9" text-anchor="middle" fill="#0f172a">N</text><text x="38" y="141" text-anchor="middle" fill="#b45309">H</text></g><g font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="40" y="89" text-anchor="middle" fill="#0f172a">7</text></g><g font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="153.5" y="63.9" text-anchor="middle" fill="#0f172a">4</text></g><g font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="101.8" y="10.4" text-anchor="middle" fill="#0f172a">4</text></g></svg>
:::

Sur la figure, les angles droits en A et en H sont ceux du rectangle ABNH, tracé dans le plan des deux fils.

::: exemple La distance MN

1. (AM) et (BN) sont perpendiculaires au plafond : elles sont parallèles, car deux droites perpendiculaires à un même plan sont parallèles.
2. Parallèles, elles sont coplanaires : A, B, N et M sont dans un même plan.
3. H est le point de [AM] tel que (NH) soit parallèle à (AB) : ABNH est un rectangle, donc AH = BN = 4 et NH = AB = 4, d'où HM = 7 − 4 = 3.
4. MHN est rectangle en H : MN² = 3² + 4² = 25, donc MN = 5 dm.

:::

::: piege Croire que des fils de longueurs différentes ne sont pas parallèles
Un élève dit que les fils n'ont pas la même longueur, donc qu'ils ne sont pas parallèles et qu'on ne peut pas les mettre dans un seul plan. Cela tente parce qu'on associe « parallèle » à « pareil ».
Mais la longueur n'a aucun rapport avec la direction : les deux fils sont perpendiculaires au même plafond, donc parallèles.
:::

::: propriete

- Deux droites perpendiculaires à un même plan sont parallèles ; deux plans perpendiculaires à une même droite sont parallèles.
- Si deux droites sont parallèles, tout plan perpendiculaire à l'une est perpendiculaire à l'autre.
- Si deux plans sont parallèles, toute droite perpendiculaire à l'un est perpendiculaire à l'autre.

Cas limite : deux droites perpendiculaires à une même droite ne sont pas parallèles en général : (AB) et (AD) sont toutes deux perpendiculaires à (AA′) dans le cube, et elles se coupent en A.
:::

::: verifie
Deux fils à plomb de 10 dm et de 4 dm pendent d'un plafond plat, accrochés à 8 dm l'un de l'autre. Quelle est la distance entre les deux poids ?

---

Les fils sont perpendiculaires au plafond, donc parallèles, donc dans un même plan. Dans ce plan, le rectangle formé donne un côté de 8 et un côté 10 − 4 = 6 : MN² = 8² + 6² = 100, donc MN = 10 dm.
:::

::: retenir
Deux droites perpendiculaires à un même plan sont parallèles, donc coplanaires ; deux plans perpendiculaires à une même droite sont parallèles ; ce n'est pas vrai de deux perpendiculaires à une même droite.
:::

## 🔺 Théorème des trois perpendiculaires

Un pylône [AM] de 6 m est planté en A, perpendiculairement à un champ plat, à 8 m d'une route rectiligne D (8 m est la distance de A à la route, mesurée à l'équerre : H est le point de la route le plus proche de A).
Le câble [MH] est-il perpendiculaire à la route ? Quelle est alors la distance de M à un point K de la route situé à 24 m de H ?

::: figure Le pylône [AM], la route D, H le pied de la perpendiculaire à D issue de A, et le plan (AHM) en vert : la route est perpendiculaire à (AH) et à (AM), donc à (MH)
<svg viewBox="-19 41 320 155"><path d="M-3.4 180.4 L161.6 180.4 L284.8 57.2 L119.8 57.2 Z" fill="#0f6e56" opacity="0.08"/><path d="M-3.4 180.4 L161.6 180.4 L284.8 57.2 L119.8 57.2 Z" fill="none" stroke="#94a3b8" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/><path d="M117.6 180.4 L240.8 57.2" fill="none" stroke="#0f172a" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/><path d="M45 165 L133 165 L45 99 Z" fill="#0f6e56" opacity="0.16"/><path d="M45 165 L45 99" fill="none" stroke="#0f172a" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/><path d="M45 165 L133 165" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M45 99 L133 165" fill="none" stroke="#b45309" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/><path d="M45 99 L225.4 72.6" fill="none" stroke="#0f6e56" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/><path d="M56 165 L56 154 L45 154" fill="none" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/><path d="M115.4 165 L121.6 158.8 L139.2 158.8" fill="none" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/><path d="M124.2 158.4 L128.1 154.6 L136.8 161.2" fill="none" stroke="#b45309" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/><g fill="#0f172a"><circle cx="45" cy="165" r="3.8"/><circle cx="45" cy="99" r="3.8"/><circle cx="225.4" cy="72.6" r="3.8"/></g><g fill="#b45309"><circle cx="133" cy="165" r="3.8"/></g><g font-size="15" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="34" y="177" text-anchor="middle" fill="#0f172a">A</text><text x="45" y="89" text-anchor="middle" fill="#0f172a">M</text><text x="120" y="177" text-anchor="middle" fill="#b45309">H</text><text x="237.4" y="77.6" text-anchor="middle" fill="#0f172a">K</text></g><g font-size="14" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="148" y="183" text-anchor="middle" fill="#0f172a">D</text></g><g font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="35" y="136" text-anchor="middle" fill="#0f172a">6</text></g><g font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="91" y="180" text-anchor="middle" fill="#0f172a">8</text></g></svg>
:::

Sur la figure, l'angle droit en A est celui du pylône, et celui en H le long de la route est celui du théorème : (MH) ⊥ D.

::: exemple La route et le pylône

1. (AH) ⊥ D, par construction de H dans le plan du champ.
2. (AM) est perpendiculaire au champ, donc orthogonale à D, qui est dans le champ.
3. D est orthogonale à (AH) et à (AM), deux sécantes du plan (AHM) : D est perpendiculaire à (AHM), donc orthogonale à (MH), qui est dans ce plan.
4. MH² = AM² + AH² = 36 + 64 = 100, donc MH = 10 ; puis MHK est rectangle en H : MK² = MH² + HK² = 100 + 576 = 676, donc MK = 26 m.

:::

::: piege Conclure avec une seule perpendiculaire
Un élève sait que (AH) ⊥ D et écrit « donc (MH) ⊥ D ». Cela tente parce que (MH) part de H comme (AH).
Mais D ⊥ (AH) ne dit rien des autres droites passant par H : c'est D ⊥ (AM), grâce au pylône perpendiculaire au champ, qui complète les deux sécantes (AH) et (AM) du plan (AHM).
:::

::: propriete
**Théorème des trois perpendiculaires.** Soit Δ perpendiculaire à un plan P en A, D une droite de P ne passant pas par A, H le projeté orthogonal de A sur D et M un point de Δ distinct de A : alors (MH) est perpendiculaire à D.
Cas limite : si D passe par A, alors H = A et (MH) = Δ, qui est orthogonale à D directement.
:::

::: verifie
Un pylône [AM] de 15 m est perpendiculaire à un champ plat en A. H est le point d'une route D (dans le champ) le plus proche de A, avec AH = 8 m. Quelle est la distance de M à la route ?

---

(AH) ⊥ D et (AM) ⊥ D, deux sécantes du plan (AHM) : D est orthogonale à (MH), donc MH est la perpendiculaire menée de M à D. AMH est rectangle en A : MH² = 15² + 8² = 225 + 64 = 289, donc MH = 17 m.
:::

::: retenir
Si Δ est perpendiculaire à P en A, H le pied de la perpendiculaire à D issue de A dans P, alors (MH) ⊥ D pour tout M de Δ : deux perpendiculaires du plan (AHM) pour D, pas une.
:::

## ⚖️ Plan médiateur d'un segment

Deux balises A et B sont distantes de 8 km. Un drone doit rester à égale distance des deux balises ; à un instant, il est à 5 km de chacune.
Son trajet est-il une droite ? Et à quelle distance est-il du milieu I des deux balises ?

::: definition
Le **plan médiateur** d'un segment [AB] est le plan perpendiculaire à (AB) en son milieu I.
**Théorème** : l'ensemble des points équidistants de A et de B est le plan médiateur de [AB].
:::

::: figure Le plan médiateur de [AB] en vert, perpendiculaire à (AB) en son milieu I : le point M du plan est à égale distance de A et de B
<svg viewBox="27 12 276 285"><path d="M133.5 279.5 L196.5 216.5 L196.5 30.5 L133.5 93.5 Z" fill="#0f6e56" opacity="0.13"/><path d="M133.5 279.5 L196.5 216.5 L196.5 30.5 L133.5 93.5 Z" fill="none" stroke="#0f6e56" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/><path d="M45 170 L285 170" fill="none" stroke="#0f172a" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/><path d="M183.9 79.1 L45 170" fill="none" stroke="#b45309" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/><path d="M183.9 79.1 L285 170" fill="none" stroke="#b45309" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/><path d="M165 170 L183.9 79.1" fill="none" stroke="#0f6e56" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/><path d="M180 170 L183.2 154.8 L168.2 154.8" fill="none" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/><g fill="#0f172a"><circle cx="45" cy="170" r="3.8"/><circle cx="285" cy="170" r="3.8"/><circle cx="183.9" cy="79.1" r="3.8"/></g><g fill="#0f6e56"><circle cx="165" cy="170" r="3.8"/></g><g font-size="15" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="34" y="176" text-anchor="middle" fill="#0f172a">A</text><text x="297" y="176" text-anchor="middle" fill="#0f172a">B</text><text x="183.9" y="69.1" text-anchor="middle" fill="#b45309">M</text><text x="154" y="186" text-anchor="middle" fill="#0f6e56">I</text></g><g font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="170.6" y="111.5" text-anchor="middle" fill="#0f172a">3</text></g><g font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="103" y="188" text-anchor="middle" fill="#0f172a">4</text></g><g font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="227" y="188" text-anchor="middle" fill="#0f172a">4</text></g><g font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="104.4" y="114.6" text-anchor="middle" fill="#0f172a">5</text></g><g font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="244.4" y="114.6" text-anchor="middle" fill="#0f172a">5</text></g></svg>
:::

Sur la figure, tout point M du plan vert vérifie MA = MB, et (IM) est dans le plan donc perpendiculaire à (AB).

::: exemple Le drone

1. MA = MB = 5 : M est dans le plan médiateur de [AB], par le théorème, et non sur une droite.
2. (AB) est perpendiculaire au plan médiateur et (MI) est dans ce plan : (MI) ⊥ (AB), donc MIA est rectangle en I, avec AI = 4.
3. MI² = MA² − AI² = 25 − 16 = 9, donc MI = 3 km.

:::

::: figure Le pavé de dimensions 2, 3 et 6 construit sur OA, OB, OC : son centre Ω est équidistant de O, A, B et C
<svg viewBox="26 11 130 238"><path d="M78.3 196.7 L132.3 196.7" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M78.3 196.7 L50 225" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M78.3 196.7 L78.3 34.7" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M104 225 L50 225" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/><path d="M104 225 L132.3 196.7" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/><path d="M50 63 L104 63" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/><path d="M104 63 L132.3 34.7" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/><path d="M78.3 34.7 L132.3 34.7" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/><path d="M50 63 L78.3 34.7" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/><path d="M104 225 L104 63" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/><path d="M50 63 L50 225" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/><path d="M132.3 196.7 L132.3 34.7" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/><path d="M50 225 L104 225" fill="none" stroke="#0f6e56" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/><path d="M50 225 L50 63" fill="none" stroke="#0f6e56" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/><path d="M104 225 L50 63" fill="none" stroke="#0f6e56" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/><path d="M50 225 L78.3 196.7" fill="none" stroke="#0f6e56" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M104 225 L78.3 196.7" fill="none" stroke="#0f6e56" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/><path d="M78.3 196.7 L50 63" fill="none" stroke="#0f6e56" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/><path d="M91.2 129.8 L50 225" fill="none" stroke="#b45309" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M91.2 129.8 L132.3 34.7" fill="none" stroke="#b45309" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><g fill="#0f172a"><circle cx="50" cy="225" r="3.8"/><circle cx="104" cy="225" r="3.8"/><circle cx="78.3" cy="196.7" r="3.8"/><circle cx="50" cy="63" r="3.8"/><circle cx="132.3" cy="196.7" r="3.8"/><circle cx="104" cy="63" r="3.8"/><circle cx="78.3" cy="34.7" r="3.8"/><circle cx="132.3" cy="34.7" r="3.8"/></g><g fill="#b45309"><circle cx="91.2" cy="129.8" r="3.8"/></g><g font-size="15" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="39" y="237" text-anchor="middle" fill="#0f172a">O</text><text x="116" y="239" text-anchor="middle" fill="#0f172a">A</text><text x="75.3" y="187.7" text-anchor="middle" fill="#0f172a">B</text><text x="39" y="63" text-anchor="middle" fill="#0f172a">C</text><text x="144.3" y="201.7" text-anchor="middle" fill="#0f172a">E</text><text x="117" y="65" text-anchor="middle" fill="#0f172a">F</text><text x="74.3" y="24.7" text-anchor="middle" fill="#0f172a">G</text><text x="145.3" y="29.7" text-anchor="middle" fill="#0f172a">R</text></g><g font-size="15" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="106.2" y="135.8" text-anchor="middle" fill="#b45309">Ω</text></g></svg>
:::

::: exemple Une sphère qui passe par quatre points

La **sphère circonscrite** à un tétraèdre est la sphère qui contient ses quatre sommets : son centre est équidistant des quatre sommets. Prenons OABC avec OA = 2, OB = 3, OC = 6, les arêtes [OA], [OB], [OC] étant deux à deux perpendiculaires.

1. On complète en pavé ; Ω est son centre. (OA) est perpendiculaire au plan (OBC) ; le plan parallèle à (OBC) mené par le milieu de [OA] lui est perpendiculaire en ce milieu : c'est le plan médiateur de [OA], et il contient Ω. Donc ΩO = ΩA.
2. De même, Ω est dans les plans médiateurs de [OB] et de [OC] : ΩO = ΩB = ΩC.
3. Le centre Ω du pavé est le milieu de sa grande diagonale [OR], avec OR = √(4 + 9 + 36) = 7 : le rayon de la sphère vaut 7/2 = 3,5.

:::

::: piege Prendre un plan qui passe par le milieu pour le plan médiateur
Un élève appelle plan médiateur de [AB] un plan qui contient le milieu I, par exemple un plan qui contient aussi la droite (AB). Cela tente parce que, dans le plan, la médiatrice passe par le milieu.
Mais il faut deux conditions : passer par I et être perpendiculaire à (AB). Un plan qui contient (AB) contient A, qui n'est pas équidistant de A et de B.
:::

::: propriete
Un point M est équidistant de A et de B si et seulement s'il est dans le plan médiateur de [AB].
Cas limite : A et B ne sont jamais dans le plan médiateur ; la droite (AB) le coupe en un seul point, le milieu I.
:::

> 🗡️ Pour minimiser MA + MC quand M décrit le plan médiateur de [AB], remplace MA par MB. Exemple : ABC rectangle en A avec AB = 4 et AC = 3 ; on a MA + MC = MB + MC ≥ BC = 5, avec égalité quand M est sur [BC], donc le minimum vaut 5.

::: verifie
Les points M, A et B vérifient MA = MB = 13 et AB = 24. À quelle distance M est-il du milieu I de [AB] ?

---

M est équidistant de A et de B : il est dans le plan médiateur de [AB], donc (MI) ⊥ (AB) et MIA est rectangle en I, avec AI = 12. MI² = 13² − 12² = 169 − 144 = 25, donc MI = 5.
:::

::: retenir
Le plan médiateur de [AB] est le plan perpendiculaire à (AB) en son milieu, et c'est l'ensemble des points équidistants de A et de B.
:::

## 🌐 Axe d'un cercle

Un bassin circulaire de rayon 5 m est éclairé par une lampe N suspendue à 12 m à la verticale du centre O.
Quelle distance sépare la lampe d'un point du bord ? Pourquoi est-ce la même pour tous les points du bord ?

::: definition
L'**axe** d'un cercle est la droite qui passe par son centre et qui est perpendiculaire à son plan.
**Théorème** : l'ensemble des points équidistants de tous les points d'un cercle est l'axe de ce cercle.
:::

::: figure Le bassin de centre O et de rayon 5, avec l'axe (ON) : pour tout point A du bord, le triangle NOA est rectangle en O
<svg viewBox="47 31 166 211"><path d="M195 205 L197 202.6 L198.3 200.3 L198.8 198 L198.6 195.7 L197.7 193.6 L196 191.6 L193.5 189.8 L190.4 188.1 L186.6 186.6 L182.2 185.3 L177.2 184.2 L171.7 183.4 L165.8 182.7 L159.4 182.4 L152.8 182.2 L145.8 182.4 L138.7 182.7 L131.6 183.4 L124.3 184.2 L117.2 185.3 L110.2 186.6 L103.4 188.1 L96.9 189.8 L90.8 191.6 L85.1 193.6 L79.9 195.7 L75.2 198 L71.2 200.3 L67.7 202.6 L65 205 L63 207.4 L61.7 209.7 L61.2 212 L61.4 214.3 L62.3 216.4 L64 218.4 L66.5 220.2 L69.6 221.9 L73.4 223.4 L77.8 224.7 L82.8 225.8 L88.3 226.6 L94.2 227.3 L100.6 227.6 L107.2 227.8 L114.2 227.6 L121.3 227.3 L128.4 226.6 L135.7 225.8 L142.8 224.7 L149.8 223.4 L156.6 221.9 L163.1 220.2 L169.2 218.4 L174.9 216.4 L180.1 214.3 L184.8 212 L188.8 209.7 L192.3 207.4 L195 205 Z" fill="#0f6e56" opacity="0.12"/><path d="M195 205 L197 202.6 L198.3 200.3 L198.8 198 L198.6 195.7 L197.7 193.6 L196 191.6 L193.5 189.8 L190.4 188.1 L186.6 186.6 L182.2 185.3 L177.2 184.2 L171.7 183.4 L165.8 182.7 L159.4 182.4 L152.8 182.2 L145.8 182.4 L138.7 182.7 L131.6 183.4 L124.3 184.2 L117.2 185.3 L110.2 186.6 L103.4 188.1 L96.9 189.8 L90.8 191.6 L85.1 193.6 L79.9 195.7 L75.2 198 L71.2 200.3 L67.7 202.6 L65 205 L63 207.4 L61.7 209.7 L61.2 212 L61.4 214.3 L62.3 216.4 L64 218.4 L66.5 220.2 L69.6 221.9 L73.4 223.4 L77.8 224.7 L82.8 225.8 L88.3 226.6 L94.2 227.3 L100.6 227.6 L107.2 227.8 L114.2 227.6 L121.3 227.3 L128.4 226.6 L135.7 225.8 L142.8 224.7 L149.8 223.4 L156.6 221.9 L163.1 220.2 L169.2 218.4 L174.9 216.4 L180.1 214.3 L184.8 212 L188.8 209.7 L192.3 207.4 L195 205 Z" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><path d="M130 205 L130 49" fill="none" stroke="#0f172a" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/><path d="M130 205 L170.2 218" fill="none" stroke="#0f6e56" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/><path d="M130 49 L170.2 218" fill="none" stroke="#b45309" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/><path d="M130 192 L138 194.6 L138 207.6" fill="none" stroke="#0f172a" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/><g fill="#0f172a"><circle cx="130" cy="205" r="3.8"/><circle cx="130" cy="49" r="3.8"/><circle cx="170.2" cy="218" r="3.8"/></g><g font-size="15" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="118" y="217" text-anchor="middle" fill="#0f172a">O</text><text x="130" y="39" text-anchor="middle" fill="#b45309">N</text><text x="183.2" y="226" text-anchor="middle" fill="#0f172a">A</text></g><g font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="120" y="131" text-anchor="middle" fill="#0f172a">12</text></g><g font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="152.1" y="226.5" text-anchor="middle" fill="#0f172a">5</text></g><g font-size="13" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="165.1" y="131.5" text-anchor="middle" fill="#0f172a">13</text></g></svg>
:::

Sur la figure, (ON) est l'axe du bassin et NA est la distance de la lampe à un point A du bord.

::: exemple La lampe du bassin

1. N est sur l'axe : (ON) est perpendiculaire au plan du bassin, donc orthogonale à (OA), droite de ce plan.
2. NOA est rectangle en O : NA² = OA² + ON² = 25 + 144 = 169, donc NA = 13 m.
3. Le calcul ne dépend pas du point A choisi sur le bord : la lampe est à 13 m de chaque point du bord.

:::

::: piege Additionner le rayon et la hauteur
Un élève écrit NA = ON + OA = 12 + 5 = 17. Cela tente parce que le chemin de N à O puis de O à A mesure 17.
Mais [NA] est l'hypoténuse du triangle rectangle NOA : ce sont les carrés qui s'additionnent, NA² = 144 + 25 = 169, donc NA = 13.
:::

::: propriete
Si N est sur l'axe d'un cercle de centre O et de rayon r, avec ON = d, alors NA = √(r² + d²) pour tout point A du cercle.
Un point équidistant de trois points non alignés B, C et D est sur l'axe du cercle qui passe par ces trois points, car il est dans les plans médiateurs de [BC] et de [CD], qui se coupent suivant cet axe.
Cas limite : si d = 0, N est le centre O et NA = r.
:::

::: figure Le tétraèdre régulier ABCD d'arête 6 : A est équidistant de B, C et D, donc sur l'axe du cercle circonscrit à BCD, et son projeté H est le centre de ce cercle
<svg viewBox="21 -1 260 250"><path d="M257.2 153.7 L44.8 189.4" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M44.8 189.4 L185.8 225.1" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M257.2 153.7 L185.8 225.1" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M162.6 22.8 L44.8 189.4" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M162.6 22.8 L185.8 225.1" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M162.6 22.8 L257.2 153.7" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M162.6 22.8 L162.6 189.4" fill="none" stroke="#0f6e56" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M257.2 153.7 L162.6 189.4" fill="none" stroke="#b45309" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M44.8 189.4 L162.6 189.4" fill="none" stroke="#b45309" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M185.8 225.1 L162.6 189.4" fill="none" stroke="#b45309" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><g fill="#0f172a"><circle cx="162.6" cy="22.8" r="3.8"/><circle cx="257.2" cy="153.7" r="3.8"/><circle cx="44.8" cy="189.4" r="3.8"/><circle cx="185.8" cy="225.1" r="3.8"/></g><g fill="#0f6e56"><circle cx="162.6" cy="189.4" r="3.8"/></g><g font-size="15" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="162.6" y="12.8" text-anchor="middle" fill="#0f172a">A</text><text x="259.2" y="143.7" text-anchor="middle" fill="#0f172a">B</text><text x="32.8" y="199.4" text-anchor="middle" fill="#0f172a">C</text><text x="197.8" y="237.1" text-anchor="middle" fill="#0f172a">D</text><text x="161.6" y="207.4" text-anchor="middle" fill="#0f6e56">H</text></g></svg>
:::

::: exemple La hauteur d'un tétraèdre régulier

Dans un tétraèdre régulier ABCD d'arête 6, H est le projeté orthogonal de A sur (BCD). Rappel : la médiane d'un triangle équilatéral de côté 6 mesure 3√3.

1. AB = AC = AD : A est équidistant de B, C et D, donc A est sur l'axe du cercle circonscrit à BCD ; son projeté H est le centre de ce cercle.
2. BCD est équilatéral : son centre est aux deux tiers de la médiane, donc BH = 2 × 3√3 / 3 = 2√3, et BH² = 12.
3. AHB est rectangle en H : AH² = AB² − BH² = 36 − 12 = 24, donc AH = 2√6, soit environ 4,90.

:::

::: verifie
Un cercle de centre O et de rayon 8 est dans un plan P. N est un point de l'axe de ce cercle, avec ON = 6. Quelle est la distance de N à chaque point du cercle ?

---

N est sur l'axe, donc (ON) est orthogonale à toute droite de P, et NOA est rectangle en O pour tout point A du cercle. NA² = 8² + 6² = 64 + 36 = 100, donc NA = 10, la même valeur pour tous les points.
:::

::: retenir
L'axe d'un cercle est l'ensemble des points équidistants de tous ses points, et un point de l'axe à la distance d du centre est à √(r² + d²) de chaque point du cercle.
:::

## 📚 Plans perpendiculaires : un mur sur le sol

Un maçon accroche un fil à plomb au mur : le fil est une droite du mur, perpendiculaire au sol. Le mur est-il perpendiculaire au sol, et le sol au mur ?
Que faut-il vérifier au juste pour affirmer que deux plans sont perpendiculaires ?

::: definition
Deux plans sont **perpendiculaires** lorsque l'un d'eux contient une droite perpendiculaire à l'autre.
:::

::: figure Dans le cube d'arête 6, les plans (ACC′A′) en vert et (BDD′B′) en orange se coupent suivant la droite (OO′) : O et O′ sont les centres de ABCD et de A′B′C′D′
<svg viewBox="10 6 250 250"><path d="M34 232.5 L236.5 180 L236.5 30 L34 82.5 Z" fill="#0f6e56" opacity="0.16"/><path d="M184 232.5 L86.5 180 L86.5 30 L184 82.5 Z" fill="#b45309" opacity="0.14"/><path d="M236.5 180 L86.5 180" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M34 232.5 L86.5 180" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M86.5 180 L86.5 30" fill="none" stroke="#94a3b8" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M34 232.5 L184 232.5" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M184 232.5 L236.5 180" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M34 82.5 L184 82.5" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M184 82.5 L236.5 30" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M236.5 30 L86.5 30" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M34 82.5 L86.5 30" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M184 232.5 L184 82.5" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M34 232.5 L34 82.5" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M236.5 180 L236.5 30" fill="none" stroke="#0f172a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M34 232.5 L236.5 180" fill="none" stroke="#0f6e56" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M34 82.5 L236.5 30" fill="none" stroke="#0f6e56" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/><path d="M184 232.5 L86.5 180" fill="none" stroke="#b45309" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><path d="M184 82.5 L86.5 30" fill="none" stroke="#b45309" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/><path d="M135.2 206.2 L135.2 56.2" fill="none" stroke="#0f172a" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="5 4"/><g fill="#0f172a"><circle cx="34" cy="232.5" r="3.8"/><circle cx="184" cy="232.5" r="3.8"/><circle cx="236.5" cy="180" r="3.8"/><circle cx="86.5" cy="180" r="3.8"/><circle cx="34" cy="82.5" r="3.8"/><circle cx="184" cy="82.5" r="3.8"/><circle cx="236.5" cy="30" r="3.8"/><circle cx="86.5" cy="30" r="3.8"/><circle cx="135.2" cy="206.2" r="3.8"/><circle cx="135.2" cy="56.2" r="3.8"/></g><g font-size="15" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="23" y="244.5" text-anchor="middle" fill="#0f172a">A</text><text x="195" y="246.5" text-anchor="middle" fill="#0f172a">B</text><text x="249.5" y="184" text-anchor="middle" fill="#0f172a">C</text><text x="75.5" y="178" text-anchor="middle" fill="#0f172a">D</text><text x="22" y="80.5" text-anchor="middle" fill="#0f172a">A′</text><text x="188" y="73.5" text-anchor="middle" fill="#0f172a">B′</text><text x="249.5" y="25" text-anchor="middle" fill="#0f172a">C′</text><text x="82.5" y="20" text-anchor="middle" fill="#0f172a">D′</text><text x="147.2" y="220.2" text-anchor="middle" fill="#0f172a">O</text><text x="147.2" y="48.2" text-anchor="middle" fill="#0f172a">O′</text></g></svg>
:::

Sur la figure, la droite (BD) du plan orange est perpendiculaire au plan vert, ce qui rend les deux plans perpendiculaires.

::: exemple Les deux plans diagonaux du cube

1. (BD) ⊥ (AC), car ce sont les diagonales du carré ABCD.
2. (BD) ⊥ (AA′), car (AA′) est perpendiculaire à (ABC), qui contient (BD).
3. (AC) et (AA′) sont sécantes dans (ACC′A′) : (BD) est perpendiculaire à ce plan, et (BD) est dans (BDD′B′) : les deux plans sont perpendiculaires.
4. Contrôle : O est le projeté de B sur (ACC′A′), donc BO = 3√2, et (BO) est perpendiculaire à (OA′). OA′² = OA² + AA′² = 18 + 36 = 54, puis BA′² = BO² + OA′² = 18 + 54 = 72 et BA′ = 6√2, la diagonale du carré ABB′A′ : ✓.

:::

::: piege Croire que deux plans perpendiculaires à un même plan sont parallèles
Un élève sait que (ABB′A′) et (ADD′A′) sont perpendiculaires à (ABC) et en conclut qu'ils sont parallèles. Cela tente parce que, pour deux droites perpendiculaires à un même plan, la conclusion est vraie.
Mais ces deux plans se coupent suivant (AA′) : deux plans perpendiculaires à un même plan se coupent suivant une droite perpendiculaire à ce plan.
:::

::: propriete

- Si deux plans sont perpendiculaires, toute droite de l'un perpendiculaire à leur droite d'intersection est perpendiculaire à l'autre plan.
- Si deux plans sécants sont perpendiculaires à un même plan, leur droite d'intersection est perpendiculaire à ce plan.
- Si deux plans sont parallèles, tout plan perpendiculaire à l'un est perpendiculaire à l'autre.

Cas limite : une droite d'un des plans non perpendiculaire à l'intersection ne l'est pas à l'autre plan : (AB′), dans (ABB′A′), n'est pas perpendiculaire à (ABC).
:::

::: verifie
Dans le cube ABCDA′B′C′D′, montrer que les plans (ABB′A′) et (BCC′B′) sont perpendiculaires.

---

(AB) est orthogonale à (BC) et à (BB′), car ABCD et ABB′A′ sont des carrés ; ces deux droites sont sécantes en B dans (BCC′B′). Donc (AB) est perpendiculaire à (BCC′B′). Comme (AB) est dans (ABB′A′), les deux plans sont perpendiculaires.
:::

::: retenir
Deux plans sont perpendiculaires quand l'un contient une droite perpendiculaire à l'autre ; deux plans perpendiculaires à un même plan se coupent suivant une droite perpendiculaire à ce plan.
:::

> 🏆 Quête franchie, héros : tu sais décider si deux droites sont orthogonales, prouver qu'une droite est perpendiculaire à un plan, projeter un point, passer du parallélisme à la perpendicularité, appliquer le théorème des trois perpendiculaires, utiliser le plan médiateur, l'axe d'un cercle et les plans perpendiculaires. Ces outils serviront dans tous les calculs de solides.
