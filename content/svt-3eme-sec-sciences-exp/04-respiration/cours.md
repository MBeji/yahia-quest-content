# 🔋 La respiration cellulaire — dégrader le glucose, produire l'ATP

> 💡 «Au repos, tu consommes 0,25 litre d'oxygène par minute ; un athlète à l'effort en consomme 4 à 5 litres. Que devient tout cet oxygène, et à quoi sert-il ?»

Chacune de tes cellules a besoin d'énergie en permanence, et la tire surtout du glucose. Huit notions montrent comment : le bilan de la respiration cellulaire, la déshydrogénation et les enzymes, la mitochondrie, la glycolyse, le cycle de Krebs et la chaîne respiratoire, l'ATP, le bilan en ATP, enfin la fermentation lactique quand l'oxygène manque. On suppose acquis que les poumons amènent le dioxygène, que le sang le transporte jusqu'aux cellules, et, du chapitre précédent, qu'une enzyme est un catalyseur sensible à la température.

## ⚗️ Le bilan de la respiration cellulaire : d'où viennent le CO₂ et l'eau ?

Les poumons ne font qu'amener le dioxygène : c'est dans chaque cellule que le glucose est dégradé. Pour 100 cm³ de sang qui traverse un muscle, le manuel mesure à l'entrée 20 cm³ d'O₂ et 40 cm³ de CO₂, à la sortie 12 cm³ d'O₂ et 48 cm³ de CO₂.
Que devient l'oxygène qui a disparu, et de quels atomes est fait le CO₂ qui est apparu ?

::: definition
**Respiration cellulaire** — dégradation de nutriments, surtout du glucose, dans la cellule : elle consomme du dioxygène, rejette du CO₂ et de l'eau, et produit de l'énergie.
**Métabolite** — molécule organique riche en énergie que la cellule dégrade (le glucose, par exemple).
**Traceur** — atome d'une molécule remplacé par un isotope repérable, ce qui permet de suivre son trajet. Le ¹⁴C est radioactif ; le ¹⁸O est un isotope lourd de l'oxygène, stable, repéré par sa masse.
**Décarboxylation** — réaction qui retire un atome de carbone du métabolite sous forme de CO₂.
:::

Deux cultures de cellules ont été suivies avec des traceurs :

| Expérience | Traceur                         | Résultat                                             |
| ---------- | ------------------------------- | ---------------------------------------------------- |
| 1          | glucose dont le carbone est ¹⁴C | le CO₂ rejeté est marqué                             |
| 2          | dioxygène ¹⁸O₂ ajouté au milieu | le CO₂ formé n'est pas marqué ; l'eau produite l'est |

::: figure Le carbone marqué du glucose se retrouve dans le CO₂, l'oxygène marqué du dioxygène se retrouve dans l'eau
<svg viewBox="0 0 340 192">

<title>Deux expériences de marquage : où vont le carbone du glucose et l'oxygène du dioxygène</title>
<text x="10" y="16" text-anchor="start" font-size="11" font-weight="700" fill="#0f172a">Expérience 1 : glucose marqué</text><rect x="10" y="24" width="120" height="50" rx="6" fill="#fde68a" stroke="#0f172a" stroke-width="2"/><text x="70" y="42" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a">glucose</text><text x="70" y="56" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a">C₆H₁₂O₆</text><text x="70" y="69" text-anchor="middle" font-size="9" font-weight="400" fill="#b91c1c">carbone marqué ¹⁴C</text><line x1="134" y1="49" x2="196" y2="49" stroke="#0f6e56" stroke-width="2.5"/>
<polygon points="196,49 187,53.5 187,44.5" fill="#0f6e56"/><rect x="200" y="24" width="130" height="50" rx="6" fill="#e2e8f0" stroke="#0f172a" stroke-width="2"/><text x="265" y="42" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a">CO₂ rejeté</text><text x="265" y="62" text-anchor="middle" font-size="10" font-weight="400" fill="#b91c1c">carbone ¹⁴C : marqué</text><text x="10" y="100" text-anchor="start" font-size="11" font-weight="700" fill="#0f172a">Expérience 2 : dioxygène marqué</text><rect x="10" y="108" width="120" height="50" rx="6" fill="#bae6fd" stroke="#0f172a" stroke-width="2"/><text x="70" y="126" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a">dioxygène</text><text x="70" y="140" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a">O₂</text><text x="70" y="153" text-anchor="middle" font-size="9" font-weight="400" fill="#b91c1c">oxygène marqué ¹⁸O</text><line x1="134" y1="133" x2="196" y2="133" stroke="#0f6e56" stroke-width="2.5"/>
<polygon points="196,133 187,137.5 187,128.5" fill="#0f6e56"/><rect x="200" y="108" width="130" height="50" rx="6" fill="#bae6fd" stroke="#0f172a" stroke-width="2"/><text x="265" y="126" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a">eau produite</text><text x="265" y="140" text-anchor="middle" font-size="11" font-weight="400" fill="#0f172a">H₂O</text><text x="265" y="153" text-anchor="middle" font-size="10" font-weight="400" fill="#b91c1c">oxygène ¹⁸O : marqué</text><text x="170" y="182" text-anchor="middle" font-size="10" font-weight="400" fill="#0f172a">Le CO₂ formé dans l'expérience 2 n'est pas marqué</text>
</svg>
:::

Chaque ligne de la figure reprend une ligne du tableau : le marqueur à gauche est celui qu'on introduit, le marqueur à droite est celui qu'on retrouve.

::: exemple Exploiter les expériences de marquage

1. Analyser l'expérience 1 : seul le glucose porte du ¹⁴C, et le CO₂ rejeté en porte aussi.
2. Interpréter : un carbone marqué ne peut venir que de la molécule qui le portait. Le carbone du CO₂ vient donc du glucose (décarboxylation).
3. Analyser l'expérience 2 : le ¹⁸O du dioxygène se retrouve dans l'eau produite, mais pas dans le CO₂.
4. Interpréter : le dioxygène respiratoire ne sert pas à fabriquer le CO₂ ; son oxygène aboutit dans l'eau.
5. Conclure : glucose + dioxygène donnent CO₂ + eau + énergie, soit C₆H₁₂O₆ + 6 O₂ → 6 CO₂ + 6 H₂O + énergie. Le sang du muscle perd 20 − 12 = 8 cm³ d'O₂ et gagne 48 − 40 = 8 cm³ de CO₂ : même volume, comme 6 O₂ pour 6 CO₂.

:::

::: piege
**Erreur : croire que l'oxygène respiré se transforme en CO₂.** « On inspire de l'O₂ et on expire du CO₂, donc l'un devient l'autre » tente parce que les deux gaz s'échangent au même endroit. Mais les traceurs montrent que le carbone du CO₂ vient du glucose, et que l'oxygène respiré aboutit dans l'eau.
:::

::: propriete
**Bilan de la respiration cellulaire.** C₆H₁₂O₆ + 6 O₂ → 6 CO₂ + 6 H₂O + énergie. Le CO₂ vient du carbone du glucose ; le dioxygène forme l'eau ; l'énergie libérée est utilisée par la cellule.
Cas limite : cette équation n'est qu'un bilan, la dégradation passe par de nombreuses réactions successives. Les acides aminés et les acides gras peuvent aussi être dégradés, le glucose restant la source d'énergie principale.
:::

::: verifie À toi : un double marquage
On cultive des cellules avec du glucose marqué au ¹⁴C et du dioxygène marqué au ¹⁸O. Dans quels produits retrouve-t-on chaque marqueur ?

---

Le ¹⁴C, porté par le carbone du glucose, se retrouve dans le CO₂ rejeté. Le ¹⁸O, porté par le dioxygène, se retrouve dans l'eau produite, pas dans le CO₂ : chaque marqueur suit sa propre voie.
:::

::: retenir
La respiration cellulaire dégrade le glucose avec du dioxygène : C₆H₁₂O₆ + 6 O₂ → 6 CO₂ + 6 H₂O + énergie ; les traceurs montrent que le carbone du CO₂ vient du glucose et que l'oxygène du dioxygène aboutit dans l'eau.
:::

## 🧪 Déshydrogénation et enzymes : des réactions catalysées

On sait que l'oxygène du dioxygène aboutit dans l'eau. D'où vient l'hydrogène de cette eau ? Pour le suivre, on place du muscle dans un liquide physiologique contenant du bleu de méthylène, sous une couche d'huile qui isole le tube de l'oxygène de l'air.
Le muscle agit-il sur le bleu de méthylène, et ces réactions ont-elles besoin d'enzymes ?

::: definition
**Déshydrogénation** — réaction qui arrache de l'hydrogène (H₂) à un métabolite et le transfère à un accepteur ou à un transporteur.
**Bleu de méthylène** — accepteur d'hydrogène : bleu sous sa forme oxydée (Bm), incolore sous sa forme réduite (BmH₂).
**Liquide de Ringer** — liquide physiologique qui garde le tissu vivant.
**Filtrat** — liquide obtenu en filtrant un broyat de muscle ou de foie frais.
:::

| Famille d'enzymes respiratoires | Ce qu'elle catalyse                                               |
| ------------------------------- | ----------------------------------------------------------------- |
| décarboxylases                  | le retrait d'un CO₂ au métabolite                                 |
| déshydrogénases                 | le transfert de H₂ du métabolite à un transporteur                |
| oxydases                        | la fixation de l'hydrogène arraché au métabolite sur le dioxygène |

::: figure À l'abri de l'air, seul le tube 2, qui contient du muscle frais, perd sa couleur bleue
<svg viewBox="0 0 340 226">

<title>Trois tubes sous une couche d'huile : seul le tube 2, avec le muscle frais, est décoloré</title>
<path d="M51 80 L51 160 A19 19 0 0 0 89 160 L89 80 Z" fill="#3b82f6" stroke="none"/><rect x="51" y="66" width="38" height="14" fill="#fde047" stroke="none"/><path d="M50 44 L50 160 A20 20 0 0 0 90 160 L90 44" fill="none" stroke="#0f172a" stroke-width="2"/><text x="70" y="34" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">1</text><text x="70" y="196" text-anchor="middle" font-size="10" font-weight="400" fill="#0f172a">Ringer + bleu</text><text x="70" y="214" text-anchor="middle" font-size="11" font-weight="700" fill="#1d4ed8">bleu</text><path d="M151 80 L151 160 A19 19 0 0 0 189 160 L189 80 Z" fill="#f8fafc" stroke="none"/><rect x="151" y="66" width="38" height="14" fill="#fde047" stroke="none"/><ellipse cx="170" cy="138" rx="11" ry="8" fill="#b91c1c" stroke="#0f172a" stroke-width="1.5"/><path d="M150 44 L150 160 A20 20 0 0 0 190 160 L190 44" fill="none" stroke="#0f172a" stroke-width="2"/><text x="170" y="34" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">2</text><text x="170" y="196" text-anchor="middle" font-size="10" font-weight="400" fill="#0f172a">+ muscle frais</text><text x="170" y="214" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a">incolore</text><path d="M251 80 L251 160 A19 19 0 0 0 289 160 L289 80 Z" fill="#3b82f6" stroke="none"/><rect x="251" y="66" width="38" height="14" fill="#fde047" stroke="none"/><ellipse cx="270" cy="138" rx="11" ry="8" fill="#a8a29e" stroke="#0f172a" stroke-width="1.5"/><path d="M250 44 L250 160 A20 20 0 0 0 290 160 L290 44" fill="none" stroke="#0f172a" stroke-width="2"/><text x="270" y="34" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">3</text><text x="270" y="196" text-anchor="middle" font-size="10" font-weight="400" fill="#0f172a">+ muscle bouilli</text><text x="270" y="214" text-anchor="middle" font-size="11" font-weight="700" fill="#1d4ed8">bleu</text><text x="8" y="76" text-anchor="start" font-size="10" font-weight="400" fill="#0f172a">huile</text><line x1="36" y1="73" x2="50" y2="73" stroke="#64748b" stroke-width="1.2"/>
</svg>
:::

Le tube 1 est le témoin : sans muscle, le bleu reste bleu. Dans le tube 2 le bleu devient incolore (BmH₂) : le muscle frais lui a cédé de l'hydrogène, sans dioxygène (déshydrogénation). Dans le tube 3, le muscle bouilli ne fait rien : l'ébullition détruit ce qui rend la réaction possible. Une seconde expérience teste cette idée sur un filtrat, avec du glucose et du bleu de méthylène dans chaque tube (résultats attendus du manuel) :

| Tube | Contenu                   | Température | Bleu de méthylène | Glucose |
| ---- | ------------------------- | ----------- | ----------------- | ------- |
| 1    | sans filtrat              | 37 °C       | bleu              | présent |
| 2    | filtrat de muscle         | 37 °C       | décoloré          | absent  |
| 3    | filtrat de muscle bouilli | 37 °C       | bleu              | présent |
| 4    | filtrat de muscle         | 0 °C        | bleu              | présent |

::: exemple Les réactions respiratoires impliquent-elles des enzymes ?

1. Analyser : seul le tube 2 est décoloré, et son glucose a disparu ; les trois autres restent bleus avec leur glucose.
2. Tube 1 contre tube 2 : sans filtrat, rien ne se passe. Une substance du filtrat déshydrogène le glucose, sans qu'il faille une cellule entière.
3. Tube 2 contre tube 3 : l'ébullition supprime l'effet. La substance est détruite par la chaleur.
4. Tube 2 contre tube 4 : à 0 °C, rien non plus. Son action dépend de la température et elle est efficace près de 37 °C.
5. Conclure : une substance détruite par la chaleur, inactive au froid et efficace vers 37 °C se comporte comme une enzyme. L'hypothèse « les réactions respiratoires sont enzymatiques » est validée.

:::

::: piege
**Erreur : croire que le froid du tube 4 a détruit l'enzyme comme l'ébullition du tube 3.** Dans les deux tubes la réaction est arrêtée, d'où la tentation de leur donner la même cause. Mais le froid inactive seulement l'enzyme, qui redevient active à 37 °C ; l'ébullition la dénature, et pour toujours.
:::

::: propriete
**Les réactions respiratoires sont enzymatiques.** Chacune est catalysée par une enzyme spécifique : décarboxylases, déshydrogénases, oxydases. La température doit rester proche de celle du corps.
Cas limite : glucose et bleu de méthylène seuls (tube 1) ne réagissent pas : sans enzyme active, un métabolite n'est pas déshydrogéné.
:::

::: verifie À toi : le rôle de l'huile
Pourquoi la couche d'huile est-elle indispensable pour affirmer que le bleu de méthylène est décoloré sans l'aide du dioxygène ?

---

L'huile empêche le dioxygène de l'air d'entrer dans le tube. La décoloration a donc lieu en l'absence de dioxygène : le muscle cède de l'hydrogène au bleu de méthylène, ce qui prouve que la déshydrogénation est une réaction distincte de l'utilisation du dioxygène.
:::

::: retenir
La déshydrogénation transfère l'hydrogène d'un métabolite à un accepteur (bleu de méthylène décoloré) ; filtrat bouilli ou glacé inactif : les réactions respiratoires sont catalysées par des enzymes (décarboxylases, déshydrogénases, oxydases).
:::

## 🏭 La mitochondrie, siège de la respiration

Les cellules du foie et des muscles, très actives, renferment de nombreuses mitochondries. Des levures cultivées avec du dioxygène grandissent, se divisent et développent beaucoup de mitochondries ; sans dioxygène, leur croissance ralentit et leurs mitochondries sont rares et peu développées.
Est-ce la mitochondrie qui respire ?

::: definition
**Mitochondrie** — organite du cytoplasme, siège de la respiration cellulaire.
**Milieu aérobie / anaérobie** — avec / sans dioxygène.
**Membrane externe, membrane interne** — les deux enveloppes de la mitochondrie.
**Crêtes** — replis de la membrane interne. **Espace intermembranaire** — entre les deux membranes. **Matrice** — intérieur délimité par la membrane interne.
**Sphères pédonculaires** — petites sphères portées par les crêtes.
:::

::: figure Une mitochondrie : la membrane interne forme des crêtes, la matrice remplit l'intérieur
<svg viewBox="0 0 400 232">

<title>Schéma d'une mitochondrie : deux membranes, des crêtes, la matrice</title>
<ellipse cx="140" cy="130" rx="110" ry="76" fill="#fde68a" stroke="#0f172a" stroke-width="2.5"/><polygon points="46,130 50,112.11 54,104.97 58,99.69 62,95.4 66,91.77 70,88.62 74,85.85 78,83.4 82,81.21 86,79.25 90,77.5 94,75.93 94,107.89 106,107.89 106,72.2 110,71.24 114,70.42 118,69.72 122,69.15 126,68.69 130,68.35 134,68.13 138,68.01 142,68.01 146,68.13 150,68.35 154,68.69 158,69.15 162,69.72 166,70.42 170,71.24 174,72.2 174,107.89 186,107.89 186,75.93 190,77.5 194,79.25 198,81.21 202,83.4 206,85.85 210,88.62 214,91.77 218,95.4 222,99.69 226,104.97 230,112.11 234,130 234,130 230,147.89 226,155.03 220,162.55 220,134.23 208,134.23 208,172.81 202,176.6 198,178.79 194,180.75 190,182.5 186,184.07 182,185.47 178,186.71 174,187.8 170,188.76 166,189.58 162,190.28 158,190.85 154,191.31 150,191.65 146,191.87 146,158 134,158 134,191.87 130,191.65 126,191.31 122,190.85 118,190.28 114,189.58 110,188.76 106,187.8 102,186.71 98,185.47 94,184.07 90,182.5 86,180.75 82,178.79 78,176.6 74,174.15 70,171.38 66,168.23 62,164.6 58,160.31 54,155.03 50,147.89 46,130" fill="#fef9c3" stroke="#0f6e56" stroke-width="2.5" stroke-linejoin="round"/><line x1="94" y1="87.89" x2="91" y2="87.89" stroke="#0f172a" stroke-width="1.2"/><circle cx="88" cy="87.89" r="3" fill="#fb923c" stroke="#0f172a" stroke-width="1.2"/><line x1="94" y1="98.89" x2="91" y2="98.89" stroke="#0f172a" stroke-width="1.2"/><circle cx="88" cy="98.89" r="3" fill="#fb923c" stroke="#0f172a" stroke-width="1.2"/><text x="160" y="134" text-anchor="middle" fill="#0f172a" font-size="11" font-weight="700" paint-order="stroke" stroke="#ffffff" stroke-width="3.5" stroke-linejoin="round">matrice</text><line x1="258" y1="30" x2="232" y2="88.34" stroke="#475569" stroke-width="1"/><text x="262" y="34" text-anchor="start" font-size="10.5" font-weight="700" fill="#0f172a">membrane externe</text><line x1="258" y1="62" x2="222" y2="99.69" stroke="#475569" stroke-width="1"/><text x="262" y="66" text-anchor="start" font-size="10.5" font-weight="700" fill="#0f172a">membrane interne</text><line x1="258" y1="126" x2="242" y2="130" stroke="#475569" stroke-width="1"/><text x="262" y="130" text-anchor="start" font-size="10.5" font-weight="700" fill="#0f172a">espace intermembranaire</text><line x1="258" y1="172" x2="220" y2="148.23" stroke="#475569" stroke-width="1"/><text x="262" y="176" text-anchor="start" font-size="10.5" font-weight="700" fill="#0f172a">crête</text><line x1="85" y1="92.89350809683074" x2="70" y2="28" stroke="#475569" stroke-width="1"/><text x="8" y="24" text-anchor="start" font-size="10.5" font-weight="700" fill="#0f172a">sphère pédonculaire</text>
</svg>
:::

Chaque nom du schéma désigne une partie bien repérée : la crête est un repli de la membrane interne, la matrice est ce que cette membrane entoure. Les analyses chimiques complètent le dessin :

| Partie           | Composition                                                                                      |
| ---------------- | ------------------------------------------------------------------------------------------------ |
| membrane externe | comparable à la membrane plasmique : 40 % de lipides, 60 % de protéines                          |
| membrane interne | riche en protéines (80 %), avec des enzymes d'oxydoréduction et de production d'énergie          |
| matrice          | de nombreuses enzymes : déshydrogénases, décarboxylases, transporteurs d'électrons et de protons |

::: exemple Prouver que la mitochondrie respire

1. Analyser les levures : avec dioxygène, croissance et mitochondries développées ; sans dioxygène, croissance ralentie et mitochondries rares. Les mitochondries se développent avec le dioxygène : elles sont peut-être impliquées dans la respiration.
2. Tester l'hypothèse : on isole les mitochondries d'un broyat de foie ou de muscle (par centrifugation), on les place dans un milieu nutritif coupé de l'air, et on mesure le taux d'O₂.
3. Analyser la mesure : le taux d'O₂ du milieu diminue au cours du temps. Seules les mitochondries sont dans le milieu : ce sont elles qui consomment le dioxygène.
4. Compléter avec la composition : la matrice porte des déshydrogénases et des décarboxylases, la membrane interne des enzymes d'oxydoréduction et de production d'énergie.
5. Conclure : la mitochondrie est le siège de la respiration cellulaire, avec des réactions dans la matrice et sur la membrane interne.

:::

::: piege
**Erreur : confondre les parties de la mitochondrie.** « Les crêtes sont des replis de la membrane externe » ou « la matrice est l'espace entre les deux membranes » tentent parce que les noms se ressemblent sur un schéma. Mais les crêtes replient la membrane interne, la matrice est l'intérieur qu'elle entoure, et l'espace intermembranaire se trouve entre les deux membranes.
:::

::: propriete
**La mitochondrie est le siège de la respiration cellulaire.** Elle consomme du dioxygène, et ses enzymes se trouvent dans la matrice et sur la membrane interne (crêtes).
Cas limite : en milieu anaérobie les mitochondries de levure sont rares et peu développées, mais pas absentes ; leur nombre suit les besoins en énergie de la cellule.
:::

::: verifie À toi : pourquoi les isoler ?
Pourquoi isoler les mitochondries avant de mesurer l'O₂ prouve-t-il davantage que d'observer des cellules entières ?

---

Dans une cellule entière, d'autres structures pourraient consommer le dioxygène. Une fois isolées dans un milieu coupé de l'air, seules les mitochondries peuvent le faire : si l'O₂ baisse, c'est bien elles qui respirent.
:::

::: retenir
La mitochondrie, délimitée par deux membranes (la membrane interne forme les crêtes, la matrice est l'intérieur), consomme le dioxygène : elle est le siège de la respiration cellulaire.
:::

## ✂️ La glycolyse : du glucose à l'acide pyruvique

On place des mitochondries isolées dans un milieu où l'on mesure l'O₂. Avec du glucose seul, le taux d'O₂ reste constant ; dès qu'on ajoute de l'acide pyruvique, il baisse. Les mitochondries n'utilisent donc pas le glucose directement.
D'où vient l'acide pyruvique, et où le glucose est-il dégradé ?

::: definition
**Acide pyruvique** (C₃H₄O₃) — métabolite à trois atomes de carbone.
**Hyaloplasme** — partie liquide du cytoplasme, en dehors des organites.
**Glycolyse** — suite de réactions enzymatiques, dans le hyaloplasme, qui dégrade une molécule de glucose en deux molécules d'acide pyruvique.
**Dégradation anaérobie** — qui n'utilise pas de dioxygène.
:::

::: figure La glycolyse a lieu dans le hyaloplasme ; chaque acide pyruvique formé passe ensuite dans la mitochondrie
<svg viewBox="0 0 340 170">

<title>Glycolyse : une molécule de glucose donne deux acides pyruviques dans le hyaloplasme</title>
<rect x="6" y="22" width="328" height="140" rx="14" fill="#f8fafc" stroke="#64748b" stroke-width="1.5"/><text x="16" y="38" text-anchor="start" font-size="11" font-weight="700" fill="#0f172a">hyaloplasme</text><circle cx="24" cy="100" r="7" fill="#fde68a" stroke="#0f172a" stroke-width="1.5"/><circle cx="41" cy="100" r="7" fill="#fde68a" stroke="#0f172a" stroke-width="1.5"/><circle cx="58" cy="100" r="7" fill="#fde68a" stroke="#0f172a" stroke-width="1.5"/><circle cx="75" cy="100" r="7" fill="#fde68a" stroke="#0f172a" stroke-width="1.5"/><circle cx="92" cy="100" r="7" fill="#fde68a" stroke="#0f172a" stroke-width="1.5"/><circle cx="109" cy="100" r="7" fill="#fde68a" stroke="#0f172a" stroke-width="1.5"/><line x1="24" y1="100" x2="109" y2="100" stroke="#0f172a" stroke-width="1.5"/><text x="66" y="124" text-anchor="middle" font-size="10" font-weight="400" fill="#0f172a">glucose (6 C)</text><line x1="122" y1="100" x2="150" y2="100" stroke="#0f6e56" stroke-width="2.5"/>
<polygon points="150,100 141,104.5 141,95.5" fill="#0f6e56"/><text x="136" y="90" text-anchor="middle" font-size="10" font-weight="700" fill="#0f6e56">glycolyse</text><line x1="166" y1="78" x2="200" y2="78" stroke="#0f172a" stroke-width="1.5"/><circle cx="166" cy="78" r="7" fill="#fdba74" stroke="#0f172a" stroke-width="1.5"/><circle cx="183" cy="78" r="7" fill="#fdba74" stroke="#0f172a" stroke-width="1.5"/><circle cx="200" cy="78" r="7" fill="#fdba74" stroke="#0f172a" stroke-width="1.5"/><line x1="166" y1="126" x2="200" y2="126" stroke="#0f172a" stroke-width="1.5"/><circle cx="166" cy="126" r="7" fill="#fdba74" stroke="#0f172a" stroke-width="1.5"/><circle cx="183" cy="126" r="7" fill="#fdba74" stroke="#0f172a" stroke-width="1.5"/><circle cx="200" cy="126" r="7" fill="#fdba74" stroke="#0f172a" stroke-width="1.5"/><text x="183" y="62" text-anchor="middle" font-size="9.5" font-weight="400" fill="#0f172a">acide pyruvique (3 C)</text><text x="183" y="148" text-anchor="middle" font-size="9.5" font-weight="400" fill="#0f172a">acide pyruvique (3 C)</text><ellipse cx="292" cy="102" rx="34" ry="24" fill="#fecdd3" stroke="#0f172a" stroke-width="2"/><text x="292" y="106" text-anchor="middle" font-size="9" font-weight="400" fill="#0f172a">mitochondrie</text><line x1="208" y1="80" x2="256" y2="94" stroke="#0f6e56" stroke-width="2"/>
<polygon points="256,94 246.1,95.8 248.62,87.16" fill="#0f6e56"/><line x1="208" y1="124" x2="256" y2="110" stroke="#0f6e56" stroke-width="2"/>
<polygon points="256,110 248.62,116.84 246.1,108.2" fill="#0f6e56"/>
</svg>
:::

Le glucose compte 6 carbones, chaque acide pyruvique 3 : le dessin montre une chaîne de 6 ronds qui devient deux chaînes de 3 ronds.

::: exemple Du glucose à l'acide pyruvique, atome par atome

1. Compter les carbones : C₆H₁₂O₆ en a 6, C₃H₄O₃ en a 3. Une molécule de glucose donne donc 6 ÷ 3 = 2 molécules d'acide pyruvique.
2. Comparer les hydrogènes : 2 C₃H₄O₃ contiennent 8 H, le glucose 12 H. Il manque 4 H.
3. Ces 4 H (soit 2 H₂) sont arrachés au métabolite : c'est une déshydrogénation, l'hydrogène étant pris en charge par des transporteurs.
4. Écrire le bilan : C₆H₁₂O₆ → 2 C₃H₄O₃ + 4 H. Vérification : 6 C = 2 × 3 C ; 12 H = 8 H + 4 H ; 6 O = 2 × 3 O.
5. Aucun dioxygène n'intervient : la glycolyse est une dégradation anaérobie, qui précède l'entrée dans la mitochondrie.

:::

::: piege
**Erreur : croire que le glucose est dégradé dans la mitochondrie.** « La mitochondrie produit l'énergie, donc c'est elle qui reçoit le glucose » tente parce qu'on associe cet organite à tout le métabolisme énergétique. Mais les mitochondries isolées n'utilisent pas le glucose : il est transformé en acide pyruvique dans le hyaloplasme, et seul l'acide pyruvique entre dans la mitochondrie.
:::

::: propriete
**La glycolyse dégrade 1 glucose (6 C) en 2 acides pyruviques (3 C) dans le hyaloplasme, sans dioxygène.** La mitochondrie reçoit ensuite l'acide pyruvique.
Cas limite : sans dioxygène la glycolyse a lieu quand même, puisqu'elle n'en utilise pas : l'acide pyruvique se forme dans le hyaloplasme.
:::

::: verifie À toi : trois molécules de glucose
On dégrade 3 molécules de glucose par glycolyse. Combien d'acides pyruviques obtient-on, et combien d'atomes de carbone contiennent-ils au total ?

---

Chaque glucose donne 2 acides pyruviques : 3 × 2 = 6 acides pyruviques. Chacun a 3 carbones : 6 × 3 = 18 carbones, soit les 3 × 6 = 18 carbones des 3 glucoses : aucun carbone n'est perdu pendant la glycolyse.
:::

::: retenir
La glycolyse, anaérobie, a lieu dans le hyaloplasme : C₆H₁₂O₆ → 2 C₃H₄O₃ + 4 H ; la mitochondrie reçoit l'acide pyruvique, pas le glucose.
:::

## 🔄 Cycle de Krebs et chaîne respiratoire : du CO₂ à l'eau

Chaque acide pyruvique entre dans la mitochondrie. À la fin, il n'en reste que du CO₂ et de l'eau, et le dioxygène a été consommé.
Le CO₂ et l'eau se forment-ils au même endroit, et de la même façon ?

::: definition
**Acétyl-coenzyme A** — métabolite à 2 atomes de carbone, formé quand l'acide pyruvique (3 C) perd un CO₂ et de l'hydrogène (décarboxylation + déshydrogénation).
**Cycle de Krebs** — suite cyclique de décarboxylations et de déshydrogénations, dans la matrice. M4, M5, M6 : métabolites à 4, 5, 6 carbones.
**Transporteur T / TH₂** — T reçoit l'hydrogène arraché au métabolite et devient TH₂ (transporteur réduit).
**Chaîne respiratoire** — chaîne de transporteurs d'électrons et de protons, dans la membrane interne (crêtes).
:::

::: figure Dans la matrice le cycle perd du CO₂ et charge des transporteurs en hydrogène ; sur les crêtes la chaîne forme l'eau avec le dioxygène
<svg viewBox="0 0 400 308">

<title>Dans la matrice le cycle de Krebs libère du CO₂ et charge des transporteurs en hydrogène ; sur les crêtes la chaîne respiratoire forme l'eau</title>
<rect x="8" y="8" width="384" height="172" rx="12" fill="#fefce8" stroke="#64748b" stroke-width="1.5"/><text x="18" y="26" text-anchor="start" font-size="11" font-weight="700" fill="#0f172a">matrice</text><rect x="8" y="196" width="384" height="108" rx="12" fill="#ecfeff" stroke="#64748b" stroke-width="1.5"/><text x="18" y="214" text-anchor="start" font-size="11" font-weight="700" fill="#0f172a">crêtes (membrane interne)</text><rect x="16" y="44" width="108" height="28" rx="5" fill="#fdba74" stroke="#0f172a" stroke-width="1.5"/><text x="70" y="62" text-anchor="middle" font-size="9" font-weight="400" fill="#0f172a">acide pyruvique (3 C)</text><line x1="70" y1="74" x2="70" y2="112" stroke="#0f172a" stroke-width="2"/>
<polygon points="70,112 65.5,103 74.5,103" fill="#0f172a"/><rect x="16" y="114" width="108" height="28" rx="5" fill="#fde68a" stroke="#0f172a" stroke-width="1.5"/><text x="70" y="132" text-anchor="middle" font-size="9.5" font-weight="400" fill="#0f172a">acétyl-CoA (2 C)</text><line x1="124" y1="52" x2="156" y2="36" stroke="#ef4444" stroke-width="2"/>
<polygon points="156,36 149.96,44.05 145.94,36" fill="#ef4444"/><text x="188" y="36" text-anchor="middle" font-size="9.5" font-weight="700" fill="#ef4444">CO₂ + TH₂</text><line x1="248.02" y1="56.02" x2="277.98" y2="85.98" stroke="#0f172a" stroke-width="2"/>
<polygon points="277.98,85.98 269.49,83.15 275.15,77.49" fill="#0f172a"/><line x1="277.98" y1="110.02" x2="248.02" y2="139.98" stroke="#0f172a" stroke-width="2"/>
<polygon points="248.02,139.98 250.85,131.49 256.51,137.15" fill="#0f172a"/><line x1="223.98" y1="139.98" x2="194.02" y2="110.02" stroke="#0f172a" stroke-width="2"/>
<polygon points="194.02,110.02 202.51,112.85 196.85,118.51" fill="#0f172a"/><line x1="194.02" y1="85.98" x2="223.98" y2="56.02" stroke="#0f172a" stroke-width="2"/>
<polygon points="223.98,56.02 221.15,64.51 215.49,58.85" fill="#0f172a"/><circle cx="236" cy="44" r="15" fill="#fde68a" stroke="#0f172a" stroke-width="1.8"/><text x="236" y="48" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a">M6</text><circle cx="290" cy="98" r="15" fill="#fde68a" stroke="#0f172a" stroke-width="1.8"/><text x="290" y="102" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a">M5</text><circle cx="236" cy="152" r="15" fill="#fde68a" stroke="#0f172a" stroke-width="1.8"/><text x="236" y="156" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a">M4</text><circle cx="182" cy="98" r="15" fill="#fde68a" stroke="#0f172a" stroke-width="1.8"/><text x="182" y="102" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a">M4</text><text x="236" y="102" text-anchor="middle" font-size="9" font-weight="700" fill="#0f172a">cycle de Krebs</text><line x1="124" y1="128" x2="165" y2="106" stroke="#0f172a" stroke-width="2"/>
<polygon points="165,106 159.2,114.22 154.94,106.29" fill="#0f172a"/><text x="308" y="70" text-anchor="middle" font-size="9.5" font-weight="700" fill="#ef4444">CO₂ + TH₂</text><text x="308" y="136" text-anchor="middle" font-size="9.5" font-weight="700" fill="#ef4444">CO₂ + TH₂</text><text x="180" y="158" text-anchor="middle" font-size="9.5" font-weight="700" fill="#0f6e56">TH₂</text><line x1="236" y1="169" x2="236" y2="224" stroke="#0f6e56" stroke-width="2.5"/>
<polygon points="236,224 231.5,215 240.5,215" fill="#0f6e56"/><text x="260" y="190" text-anchor="start" font-size="9.5" font-weight="700" fill="#0f6e56">TH₂</text><text x="256" y="288" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a">chaîne de transporteurs</text><rect x="219" y="232" width="34" height="24" rx="4" fill="#a7f3d0" stroke="#0f172a" stroke-width="1.5"/><text x="236" y="248" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a">T</text><line x1="255" y1="244" x2="272" y2="244" stroke="#0f172a" stroke-width="2"/>
<polygon points="272,244 265,247.5 265,240.5" fill="#0f172a"/><rect x="274" y="232" width="34" height="24" rx="4" fill="#a7f3d0" stroke="#0f172a" stroke-width="1.5"/><text x="291" y="248" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a">T</text><line x1="310" y1="244" x2="327" y2="244" stroke="#0f172a" stroke-width="2"/>
<polygon points="327,244 320,247.5 320,240.5" fill="#0f172a"/><circle cx="348" cy="244" r="20" fill="#bae6fd" stroke="#0f172a" stroke-width="1.8"/><text x="348" y="241" text-anchor="middle" font-size="9.5" font-weight="700" fill="#0f172a">½ O₂</text><text x="348" y="253" text-anchor="middle" font-size="8.5" font-weight="400" fill="#0f172a">+ 2H⁺</text><line x1="348" y1="266" x2="348" y2="284" stroke="#0f172a" stroke-width="2"/>
<polygon points="348,284 344.5,277 351.5,277" fill="#0f172a"/><text x="348" y="298" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a">H₂O</text>
</svg>
:::

Le dessin se lit de haut en bas : le CO₂ part de la matrice, le dioxygène n'apparaît qu'en bas, au dernier maillon de la chaîne, avec l'eau.

::: exemple Compter les CO₂ formés à partir d'une molécule de glucose

1. La glycolyse donne 2 acides pyruviques à 3 carbones.
2. Chaque acide pyruvique (3 C) perd 1 CO₂ (et de l'hydrogène, capté par un transporteur) en devenant acétyl-coenzyme A (2 C) : 1 CO₂.
3. L'acétyl-coenzyme A se fixe sur un métabolite à 4 C pour donner un métabolite à 6 C, qui perd 1 CO₂ (M6 → M5), puis 1 CO₂ (M5 → M4) : 2 CO₂ de plus.
4. Un acide pyruvique forme donc 1 + 2 = 3 CO₂ ; deux acides pyruviques en forment 2 × 3 = 6.
5. Vérification : les 6 carbones du glucose sont devenus 6 CO₂, comme le dit l'équation du bilan.

:::

::: exemple Suivre l'hydrogène jusqu'à l'eau

1. Les transporteurs T ont pris l'hydrogène des métabolites dans la matrice : ils sont devenus TH₂.
2. Sur les crêtes, TH₂ libère 2 H⁺ et 2 e⁻ et redevient T, prêt à reprendre de l'hydrogène.
3. Les électrons passent de transporteur en transporteur jusqu'au dioxygène : ½ O₂ + 2 e⁻ → O²⁻ (activation de l'oxygène).
4. Les protons rencontrent l'ion O²⁻ : 2 H⁺ + O²⁻ → H₂O, grâce à une oxydase.
5. Le dioxygène n'est donc utilisé qu'à la fin de la chaîne, et l'eau ne se forme que là.

:::

::: piege
**Erreur : placer la formation du CO₂ sur les crêtes, ou celle de l'eau dans la matrice.** Le cycle tourne dans la matrice, et on le prend facilement pour la source de tout. Mais le CO₂ se forme par décarboxylation dans la matrice, tandis que le dioxygène est consommé et l'eau formée sur les crêtes.
:::

Les trois étapes se rangent par lieu :

| Étape               | Lieu                       | Ce qui s'y passe                                  |
| ------------------- | -------------------------- | ------------------------------------------------- |
| glycolyse           | hyaloplasme                | glucose → 2 acides pyruviques                     |
| cycle de Krebs      | matrice de la mitochondrie | décarboxylations (CO₂) et déshydrogénations (TH₂) |
| chaîne respiratoire | crêtes de la mitochondrie  | TH₂ → T ; ½ O₂ + 2 e⁻ → O²⁻ ; 2 H⁺ + O²⁻ → H₂O    |

::: propriete
**Trois étapes, trois lieux : hyaloplasme, matrice, crêtes.** Le CO₂ se forme dans la matrice ; le dioxygène est consommé et l'eau formée sur les crêtes.
Cas limite : aucun CO₂ ne se forme à la chaîne respiratoire, et le dioxygène n'intervient qu'à son dernier maillon.
:::

::: verifie À toi : un seul acide pyruvique
Combien de molécules de CO₂ un seul acide pyruvique forme-t-il dans la mitochondrie, et dans quel compartiment ?

---

Il en forme 3 : 1 quand il perd un carbone pour donner l'acétyl-coenzyme A, puis 2 dans le cycle (M6 → M5 et M5 → M4). Ces décarboxylations ont toutes lieu dans la matrice.
:::

::: retenir
Dans la matrice, l'acide pyruvique est décarboxylé (6 CO₂ par glucose) et les transporteurs se chargent en hydrogène (TH₂) ; sur les crêtes, la chaîne respiratoire les décharge et le dioxygène forme l'eau.
:::

## ⚡ L'ATP, la molécule qui stocke et fournit l'énergie

La bombe calorimétrique mesure l'énergie chimique d'un aliment en le brûlant : la chaleur dégagée l'égale. Dans une cellule qui respire, la chaleur dégagée est plus faible : une partie de l'énergie est stockée dans des molécules. L'une d'elles, l'ATP, est consommée en masse : un colibacille (une bactérie) en croissance en utilise plus de deux millions de molécules par seconde.
Comment l'énergie entre-t-elle dans l'ATP, puis en ressort-elle ?

::: definition
**ATP (adénosine triphosphate)** — adénine + ribose + 3 groupements phosphate (P), dont les deux derniers sont reliés par des liaisons riches en énergie (~).
**ADP, AMP** — mêmes molécules avec 2 puis 1 groupement phosphate.
**Hydrolyse de l'ATP** — ATP + H₂O → ADP + P + énergie, catalysée par l'ATPase. Réaction exergonique : elle libère de l'énergie.
**Phosphorylation** — fixation d'un groupement phosphate ; ici ADP + P + énergie → ATP + H₂O, catalysée par l'ATP synthétase. Réaction endergonique : elle consomme de l'énergie.
:::

::: figure L'ATP porte trois phosphates, dont deux liaisons riches en énergie ; l'ADP en a deux, l'AMP un
<svg viewBox="0 0 340 134">

<title>Structure de l'ATP : adénine, ribose et trois groupements phosphate</title>
<rect x="10" y="30" width="66" height="34" rx="6" fill="#bfdbfe" stroke="#0f172a" stroke-width="2"/><text x="43" y="51" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a">adénine</text><rect x="92" y="30" width="58" height="34" rx="6" fill="#bbf7d0" stroke="#0f172a" stroke-width="2"/><text x="121" y="51" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a">ribose</text><line x1="76" y1="47" x2="92" y2="47" stroke="#0f172a" stroke-width="2.5"/><line x1="150" y1="47" x2="172" y2="47" stroke="#0f172a" stroke-width="2.5"/><rect x="172" y="30" width="34" height="34" rx="6" fill="#fed7aa" stroke="#0f172a" stroke-width="2"/><text x="189" y="52" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">P</text><rect x="222" y="30" width="34" height="34" rx="6" fill="#fed7aa" stroke="#0f172a" stroke-width="2"/><text x="239" y="52" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">P</text><rect x="272" y="30" width="34" height="34" rx="6" fill="#fed7aa" stroke="#0f172a" stroke-width="2"/><text x="289" y="52" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">P</text><path d="M206 47 q4 -8 8 0 t8 0" fill="none" stroke="#ef4444" stroke-width="2.2"/><path d="M256 47 q4 -8 8 0 t8 0" fill="none" stroke="#ef4444" stroke-width="2.2"/><line x1="10" y1="80" x2="150" y2="80" stroke="#0f172a" stroke-width="1.5"/><line x1="10" y1="76" x2="10" y2="80" stroke="#0f172a" stroke-width="1.5"/><line x1="150" y1="76" x2="150" y2="80" stroke="#0f172a" stroke-width="1.5"/><text x="156" y="84" text-anchor="start" font-size="10" font-weight="700" fill="#0f172a">adénosine</text><line x1="10" y1="94" x2="206" y2="94" stroke="#0f172a" stroke-width="1.5"/><line x1="10" y1="90" x2="10" y2="94" stroke="#0f172a" stroke-width="1.5"/><line x1="206" y1="90" x2="206" y2="94" stroke="#0f172a" stroke-width="1.5"/><text x="212" y="98" text-anchor="start" font-size="10" font-weight="700" fill="#0f172a">AMP</text><line x1="10" y1="108" x2="256" y2="108" stroke="#0f172a" stroke-width="1.5"/><line x1="10" y1="104" x2="10" y2="108" stroke="#0f172a" stroke-width="1.5"/><line x1="256" y1="104" x2="256" y2="108" stroke="#0f172a" stroke-width="1.5"/><text x="262" y="112" text-anchor="start" font-size="10" font-weight="700" fill="#0f172a">ADP</text><line x1="10" y1="122" x2="306" y2="122" stroke="#0f172a" stroke-width="1.5"/><line x1="10" y1="118" x2="10" y2="122" stroke="#0f172a" stroke-width="1.5"/><line x1="306" y1="118" x2="306" y2="122" stroke="#0f172a" stroke-width="1.5"/><text x="312" y="126" text-anchor="start" font-size="10" font-weight="700" fill="#0f172a">ATP</text><text x="10" y="14" text-anchor="start" font-size="10" font-weight="700" fill="#ef4444">~ : liaison riche en énergie</text>
</svg>
:::

Sur le dessin, chaque crochet englobe un phosphate de plus : l'adénosine n'en a aucun, l'AMP un, l'ADP deux, l'ATP trois.

::: figure Le cycle ATP–ADP : l'hydrolyse libère l'énergie utilisable, la phosphorylation la remet en réserve
<svg viewBox="0 0 340 196">

<title>Le cycle ATP–ADP : l'hydrolyse libère de l'énergie, la phosphorylation en consomme</title>
<rect x="14" y="76" width="84" height="42" rx="8" fill="#fed7aa" stroke="#0f172a" stroke-width="2"/><text x="56" y="102" text-anchor="middle" font-size="15" font-weight="700" fill="#0f172a">ATP</text><rect x="242" y="76" width="84" height="42" rx="8" fill="#e2e8f0" stroke="#0f172a" stroke-width="2"/><text x="284" y="102" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">ADP + P</text><path d="M98 82 Q170 8 232 76" fill="none" stroke="#0f6e56" stroke-width="2.5"/><polygon points="242,82 228,72 226,86" fill="#0f6e56"/><text x="170" y="28" text-anchor="middle" font-size="10.5" font-weight="700" fill="#0f6e56">hydrolyse (ATPase)</text><text x="170" y="42" text-anchor="middle" font-size="10" font-weight="400" fill="#0f172a">énergie libérée</text><path d="M242 112 Q170 186 108 118" fill="none" stroke="#ef4444" stroke-width="2.5"/><polygon points="98,112 112,112 106,126" fill="#ef4444"/><text x="170" y="170" text-anchor="middle" font-size="10.5" font-weight="700" fill="#ef4444">phosphorylation (ATP synthétase)</text><text x="170" y="184" text-anchor="middle" font-size="10" font-weight="400" fill="#0f172a">énergie consommée</text>
</svg>
:::

Les flèches du second dessin sont celles de la définition : la flèche du haut est l'hydrolyse, celle du bas la phosphorylation.

::: exemple Suivre l'énergie d'un cycle ATP–ADP

1. L'hydrolyse de 1 mole d'ATP libère 30,5 kJ (7,3 kcal). Pour 2 moles : 2 × 30,5 = 61 kJ, utilisables par la cellule (synthèses, contraction).
2. Il reste 2 moles d'ADP et 2 moles de P, qui ne peuvent plus fournir cette énergie.
3. Pour refaire l'ATP, la phosphorylation doit y remettre la même énergie : 30,5 kJ par mole, soit 61 kJ pour 2 moles. Elle est endergonique.
4. Cette énergie vient de la dégradation du glucose (glycolyse, cycle de Krebs, chaîne respiratoire).
5. L'ATP fait la navette : formé quand le glucose est dégradé, hydrolysé quand la cellule travaille.

:::

::: piege
**Erreur : inverser l'hydrolyse et la phosphorylation.** « Fabriquer l'ATP libère de l'énergie » tente parce qu'on associe l'ATP à l'énergie produite. Mais c'est l'hydrolyse de l'ATP qui libère de l'énergie, et la phosphorylation de l'ADP qui en consomme, en la prenant à la dégradation du glucose.
:::

::: propriete
**L'ATP relie la production et l'utilisation de l'énergie.** Il se forme au cours de la dégradation des nutriments, qui lui apporte l'énergie, et il est hydrolysé pour la libérer. La cellule renouvelle sans cesse son ATP : une bactérie en croissance en consomme plus de deux millions de molécules par seconde.
Cas limite : la phosphorylation est couplée à la respiration. Des mitochondries isolées ne consomment que lentement le dioxygène tant qu'on ne leur fournit pas d'ADP et de phosphate.
:::

::: verifie À toi : trois moles d'ATP
Une cellule hydrolyse 3 moles d'ATP. Quelle énergie libère-t-elle, et quelle réaction reforme l'ATP ?

---

3 × 30,5 = 91,5 kJ sont libérés. L'ATP est reformé par la phosphorylation de l'ADP, endergonique, qui consomme au moins cette énergie prise à la dégradation du glucose.
:::

::: retenir
L'ATP (adénine, ribose, 3 phosphates) libère 30,5 kJ par mole quand l'ATPase l'hydrolyse en ADP + P ; l'ATP synthétase le reforme par phosphorylation, avec l'énergie de la dégradation du glucose.
:::

## 🧮 Le bilan énergétique : combien d'ATP pour une molécule de glucose ?

Une mole de glucose, brûlée dans une bombe calorimétrique, dégage 2830 kJ sous forme de chaleur. Dans les cellules, sa dégradation libère la même énergie, mais une partie est mise en réserve dans l'ATP.
Combien d'ATP forme-t-elle, et quelle part de l'énergie est ainsi récupérée ?

::: definition
**Bilan énergétique de la respiration** — nombre d'ATP formés par molécule de glucose dégradée : 36, dont 2 à la glycolyse (hyaloplasme), 2 au cycle de Krebs (matrice) et 32 à la chaîne respiratoire (crêtes).
**Énergie dissipée** — énergie non stockée dans l'ATP, libérée sous forme de chaleur.
:::

::: figure La chaîne respiratoire forme à elle seule 32 des 36 ATP
<svg viewBox="0 0 360 178">

<title>Répartition des 36 ATP : 2 à la glycolyse, 2 au cycle de Krebs, 32 à la chaîne respiratoire</title>
<text x="10" y="16" text-anchor="start" font-size="11" font-weight="700" fill="#0f172a">ATP formés par molécule de glucose</text><text x="122" y="51" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a">glycolyse</text><rect x="130" y="34" width="12" height="26" fill="#fdba74" stroke="#0f172a" stroke-width="1.5"/><text x="148" y="52" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a">2</text><text x="122" y="89" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a">cycle de Krebs</text><rect x="130" y="72" width="12" height="26" fill="#fde68a" stroke="#0f172a" stroke-width="1.5"/><text x="148" y="90" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a">2</text><text x="122" y="127" text-anchor="end" font-size="11" font-weight="400" fill="#0f172a">chaîne respiratoire</text><rect x="130" y="110" width="192" height="26" fill="#a7f3d0" stroke="#0f172a" stroke-width="1.5"/><text x="328" y="128" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a">32</text><line x1="130" y1="28" x2="130" y2="150" stroke="#0f172a" stroke-width="2"/><line x1="130" y1="150" x2="328" y2="150" stroke="#0f172a" stroke-width="2"/><line x1="130" y1="150" x2="130" y2="155" stroke="#0f172a" stroke-width="1.5"/><text x="130" y="168" text-anchor="middle" font-size="10" font-weight="400" fill="#0f172a">0</text><line x1="190" y1="150" x2="190" y2="155" stroke="#0f172a" stroke-width="1.5"/><text x="190" y="168" text-anchor="middle" font-size="10" font-weight="400" fill="#0f172a">10</text><line x1="250" y1="150" x2="250" y2="155" stroke="#0f172a" stroke-width="1.5"/><text x="250" y="168" text-anchor="middle" font-size="10" font-weight="400" fill="#0f172a">20</text><line x1="310" y1="150" x2="310" y2="155" stroke="#0f172a" stroke-width="1.5"/><text x="310" y="168" text-anchor="middle" font-size="10" font-weight="400" fill="#0f172a">30</text><text x="350" y="16" text-anchor="end" font-size="11" font-weight="700" fill="#0f172a">total : 36 ATP</text>
</svg>
:::

Chaque barre du graphique est une étape du tableau précédent ; la longueur de la barre est le nombre d'ATP formés.

::: exemple Quelle part de l'énergie du glucose est stockée dans l'ATP ?

1. Total d'ATP par glucose : 2 + 2 + 32 = 36.
2. Énergie stockée par mole de glucose : 36 × 30,5 = 1098 kJ, puisque chaque mole d'ATP en met 30,5 kJ en réserve.
3. Énergie totale libérée par une mole de glucose : 2830 kJ.
4. Part stockée : 1098 ÷ 2830 ≈ 0,39, soit environ 39 %.
5. Le reste, 2830 − 1098 = 1732 kJ, est dissipé en chaleur : voilà pourquoi la chaleur dégagée par la cellule reste inférieure à l'énergie chimique du glucose.

:::

::: piege
**Erreur : croire que la glycolyse fournit l'essentiel de l'ATP.** « C'est la première étape, donc la plus productive » tente parce qu'on la place en tête du schéma. Mais la glycolyse forme 2 ATP sur 36 : c'est la chaîne respiratoire qui en forme 32, soit environ 89 %.
:::

::: propriete
**La respiration forme 36 ATP par glucose (2 + 2 + 32), l'essentiel sur la chaîne respiratoire.** Environ 39 % de l'énergie du glucose est stockée dans l'ATP, le reste est dissipé en chaleur.
Cas limite : sans dioxygène, la chaîne respiratoire ne fonctionne plus. La fermentation lactique (dernière notion) ne forme que l'ATP de la glycolyse : 2 ATP par glucose.
:::

::: verifie À toi : 72 ATP
Une cellule forme 72 ATP en dégradant du glucose par respiration. Combien de molécules de glucose a-t-elle dégradées, et combien d'ATP viennent de la chaîne respiratoire ?

---

Chaque glucose donne 36 ATP : 72 ÷ 36 = 2 molécules de glucose. Chacune forme 32 ATP sur la chaîne respiratoire : 2 × 32 = 64 ATP.
:::

::: retenir
La respiration forme 36 ATP par glucose (2 glycolyse, 2 cycle de Krebs, 32 chaîne respiratoire) : environ 39 % de l'énergie du glucose est stockée dans l'ATP, le reste est dissipé en chaleur.
:::

## 🏃 Quand l'oxygène manque : fermentation lactique et dette d'oxygène

Après un effort intense, l'analyse du muscle révèle de l'acide lactique, qui n'intervient pas dans la respiration. Pourtant un coureur de 100 m dépense 200 kJ en consommant seulement 0,5 litre de dioxygène, alors que cette énergie en exigerait 10 litres par la respiration.
Comment le muscle fournit-il de l'énergie quand le dioxygène manque ?

::: definition
**Fermentation lactique** — en l'absence de dioxygène, l'acide pyruvique reçoit de l'hydrogène et devient de l'acide lactique : CH₃–CO–COOH + H₂ → CH₃–CHOH–COOH. La dégradation s'arrête là, l'acide lactique contenant encore de l'énergie : la fermentation fournit 210 kJ par mole de glucose, contre 2830 kJ pour la respiration.
**Dette (ou manque) d'oxygène** — dioxygène qui a manqué pendant l'épreuve : différence entre le dioxygène théoriquement nécessaire (si toute l'énergie venait de la respiration) et le dioxygène réellement consommé. Elle est remboursée après l'effort, d'où l'essoufflement.
:::

Les données moyennes d'athlètes (document 28 du manuel) donnent, pour chaque épreuve, l'énergie dépensée et le dioxygène théorique ; la dette et la part de la respiration sont calculées ci-dessous.

| Épreuve  | Énergie dépensée | O₂ théorique | O₂ consommé | Dette d'O₂ | Part de la respiration |
| -------- | ---------------- | ------------ | ----------- | ---------- | ---------------------- |
| 100 m    | 200 kJ           | 10 L         | 0,5 L       | 9,5 L      | 5 %                    |
| 800 m    | 520 kJ           | 26 L         | 9 L         | 17 L       | 35 %                   |
| 1500 m   | 720 kJ           | 36 L         | 19 L        | 17 L       | 53 %                   |
| 10 000 m | 3000 kJ          | 150 L        | 133 L       | 17 L       | 89 %                   |
| 42 186 m | 14 000 kJ        | 700 L        | 685 L       | 15 L       | 98 %                   |

::: figure Plus l'épreuve est longue, plus la part de l'énergie fournie par la respiration augmente : 5 % au 100 m, 98 % au marathon
<svg viewBox="0 0 340 172">

<title>Part de la respiration dans l'énergie dépensée selon l'épreuve : 5 % au 100 m, 98 % au marathon</title>
<text x="10" y="14" text-anchor="start" font-size="11" font-weight="700" fill="#0f172a">Part de l'énergie fournie par la respiration (%)</text><line x1="54" y1="150" x2="334" y2="150" stroke="#cbd5e1" stroke-width="1"/><text x="48" y="154" text-anchor="end" font-size="10" font-weight="400" fill="#0f172a">0</text><line x1="54" y1="95" x2="334" y2="95" stroke="#cbd5e1" stroke-width="1"/><text x="48" y="99" text-anchor="end" font-size="10" font-weight="400" fill="#0f172a">50</text><line x1="54" y1="40" x2="334" y2="40" stroke="#cbd5e1" stroke-width="1"/><text x="48" y="44" text-anchor="end" font-size="10" font-weight="400" fill="#0f172a">100</text><rect x="63" y="144.5" width="38" height="5.5" fill="#a7f3d0" stroke="#0f172a" stroke-width="1.5"/><text x="82" y="139.5" text-anchor="middle" font-size="10.5" font-weight="700" fill="#0f172a">5 %</text><text x="82" y="165" text-anchor="middle" font-size="9.5" font-weight="400" fill="#0f172a">100 m</text><rect x="119" y="111.5" width="38" height="38.5" fill="#a7f3d0" stroke="#0f172a" stroke-width="1.5"/><text x="138" y="106.5" text-anchor="middle" font-size="10.5" font-weight="700" fill="#0f172a">35 %</text><text x="138" y="165" text-anchor="middle" font-size="9.5" font-weight="400" fill="#0f172a">800 m</text><rect x="175" y="91.7" width="38" height="58.3" fill="#a7f3d0" stroke="#0f172a" stroke-width="1.5"/><text x="194" y="86.7" text-anchor="middle" font-size="10.5" font-weight="700" fill="#0f172a">53 %</text><text x="194" y="165" text-anchor="middle" font-size="9.5" font-weight="400" fill="#0f172a">1500 m</text><rect x="231" y="52.1" width="38" height="97.9" fill="#a7f3d0" stroke="#0f172a" stroke-width="1.5"/><text x="250" y="47.1" text-anchor="middle" font-size="10.5" font-weight="700" fill="#0f172a">89 %</text><text x="250" y="165" text-anchor="middle" font-size="9.5" font-weight="400" fill="#0f172a">10 000 m</text><rect x="287" y="42.2" width="38" height="107.8" fill="#a7f3d0" stroke="#0f172a" stroke-width="1.5"/><text x="306" y="37.2" text-anchor="middle" font-size="10.5" font-weight="700" fill="#0f172a">98 %</text><text x="306" y="165" text-anchor="middle" font-size="9.5" font-weight="400" fill="#0f172a">42 186 m</text><line x1="54" y1="36" x2="54" y2="150" stroke="#0f172a" stroke-width="2"/><line x1="54" y1="150" x2="334" y2="150" stroke="#0f172a" stroke-width="2"/>
</svg>
:::

Chaque barre est la dernière colonne du tableau. Le dioxygène théorique vaut l'énergie divisée par 20 kJ par litre : 2830 kJ pour 6 × 22,4 = 134,4 L d'O₂ font environ 21 kJ par litre, que le manuel arrondit à 20. Le calcul donne la part de la respiration ; le reste est la part des voies sans dioxygène, qui comprennent la fermentation lactique étudiée ici mais aussi d'autres sources, comme les réserves musculaires d'ATP et de phosphocréatine.

::: exemple Partager l'énergie d'un 800 m entre respiration et voie sans dioxygène

1. Analyser : dépense 520 kJ, dioxygène théorique 520 ÷ 20 = 26 L, dioxygène consommé 9 L.
2. Dette d'oxygène : 26 − 9 = 17 L.
3. Part de la respiration : 9 ÷ 26 ≈ 0,35, soit 35 % de l'énergie (9 L × 20 kJ/L = 180 kJ sur 520 kJ).
4. Part restante : 17 ÷ 26 ≈ 65 % (340 kJ), fournie sans dioxygène (voie anaérobie, dont la fermentation lactique étudiée ici).
5. Vérifier : 180 kJ + 340 kJ = 520 kJ, la dépense totale. Sur 100 m, la part de la respiration tombe à 5 % ; sur le marathon, elle monte à 98 %.

:::

::: piege
**Erreur : croire que sans dioxygène le muscle ne peut plus produire d'énergie.** « Sans dioxygène, plus d'énergie : le muscle devrait s'arrêter » tente parce qu'on associe énergie et respiration. Mais la fermentation lactique fournit de l'énergie sans dioxygène, bien moins qu'avec lui : 210 kJ par glucose, plus de 13 fois moins que les 2830 kJ de la respiration.
:::

::: propriete
**Avec dioxygène : respiration (CO₂ + H₂O, 2830 kJ par mole de glucose). Sans dioxygène : fermentation lactique (acide lactique, 210 kJ).** Le muscle utilise les deux voies ; plus l'effort est intense et bref, plus la part fournie sans dioxygène (voie anaérobie, dont la fermentation lactique) est grande.
Cas limite : même sur 100 m, le muscle consomme un peu de dioxygène (0,5 L) : la respiration ne s'arrête jamais complètement.
:::

::: verifie À toi : le 10 000 m
Sur 10 000 m, le dioxygène théorique est de 150 L et le dioxygène consommé de 133 L. Calcule la dette d'oxygène et la part de la respiration.

---

Dette : 150 − 133 = 17 L. Part de la respiration : 133 ÷ 150 ≈ 0,89, soit environ 89 % ; les 11 % restants sont fournis sans dioxygène (voie anaérobie).
:::

::: retenir
Sans dioxygène, l'acide pyruvique devient de l'acide lactique (210 kJ par glucose, contre 2830 par respiration) ; la dette (ou manque) d'oxygène est le dioxygène théorique moins le dioxygène consommé, et la part de la respiration vaut le consommé divisé par le théorique.
:::

> 🏆 Chapitre franchi, héros : tu sais comment la cellule dégrade le glucose, où, avec quelles enzymes, et comment elle récupère l'énergie dans l'ATP. Prochaine quête : les risques des aliments contaminés.
