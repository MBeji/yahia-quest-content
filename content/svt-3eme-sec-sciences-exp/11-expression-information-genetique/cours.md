# 🧪 L'expression de l'information génétique — du gène à la protéine

> 💡 «Un livre de recettes n'a jamais fait cuire un gâteau : il faut un cuisinier, des ingrédients et de l'énergie. Dans la cellule, le gène est la recette, et la protéine est le gâteau.»

Huit notions pour suivre la recette de bout en bout : le lien entre gène, enzyme et phénotype (albinisme, phénylcétonurie), la protéine et ses acides aminés, le ribosome, l'ARN messager, les autres acteurs (ARNt, ATP, enzymes), la transcription, le code génétique et la traduction. On suppose acquis que l'ADN est une double hélice dont l'information est l'ordre des bases, et qu'un gène porte l'information d'un caractère (chapitre précédent).

## 🎨 Un gène, une enzyme, un phénotype : albinisme et phénylcétonurie

Deux enfants jouent côte à côte. L'un a la peau très foncée ; l'autre, albinos, a la peau et les cheveux totalement décolorés. Les deux mangent la même chose et possèdent les mêmes cellules de peau, les mélanocytes.
Qu'est-ce qui manque à l'enfant albinos, et qu'est-ce qui commande cette production ?

::: definition
**Mélanine** — pigment foncé fabriqué par les **mélanocytes**, cellules de la peau : plus ils en produisent, plus la peau est foncée.
**Enzyme** — protéine qui active (catalyse) une réaction biochimique, c'est-à-dire la transformation d'une substance en une autre.
**Génotype** — l'information génétique portée par l'ADN ; **phénotype** — son expression, ici la couleur de la peau.
:::

::: figure Chaîne de biosynthèse de la mélanine : chaque flèche est une réaction activée par une enzyme (E1, E2), chaque enzyme est sous le contrôle de sa propre information génétique
<svg viewBox="0 0 460 270">
<title>Chaîne de biosynthèse de la mélanine : aliments, phénylalanine, tyrosine, mélanine, avec les enzymes E1 et E2 contrôlées par deux informations génétiques</title>
<rect x="20" y="14" width="140" height="34" rx="8" fill="#e0f2fe" stroke="#0f172a" stroke-width="1.8"/>
<text x="90" y="36" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a">Aliments</text>
<rect x="20" y="84" width="140" height="34" rx="8" fill="#e0f2fe" stroke="#0f172a" stroke-width="1.8"/>
<text x="90" y="106" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a">Phénylalanine</text>
<rect x="20" y="154" width="140" height="34" rx="8" fill="#e0f2fe" stroke="#0f172a" stroke-width="1.8"/>
<text x="90" y="176" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a">Tyrosine</text>
<rect x="20" y="224" width="140" height="34" rx="8" fill="#e0f2fe" stroke="#0f172a" stroke-width="1.8"/>
<text x="90" y="246" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a">Mélanine</text>
<line x1="90" y1="48" x2="90.0" y2="80.0" stroke="#0f172a" stroke-width="2"/><polygon points="90,84 86.5,76.8 93.5,76.8" fill="#0f172a"/>
<line x1="90" y1="118" x2="90.0" y2="150.0" stroke="#0f172a" stroke-width="2"/><polygon points="90,154 86.5,146.8 93.5,146.8" fill="#0f172a"/>
<line x1="90" y1="188" x2="90.0" y2="220.0" stroke="#0f172a" stroke-width="2"/><polygon points="90,224 86.5,216.8 93.5,216.8" fill="#0f172a"/>
<circle cx="122" cy="136" r="13" fill="#fef3c7" stroke="#0f172a" stroke-width="1.6"/>
<text x="122" y="140" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">E1</text>
<text x="144" y="140" text-anchor="start" font-size="11" font-weight="600" fill="#0f172a">phénylalanine hydroxylase</text>
<rect x="372" y="114" width="82" height="44" rx="8" fill="#dcfce7" stroke="#0f6e56" stroke-width="1.8"/>
<text x="413" y="132" text-anchor="middle" font-size="11" font-weight="600" fill="#0f172a">Information</text>
<text x="413" y="147" text-anchor="middle" font-size="11" font-weight="600" fill="#0f172a">génétique 1</text>
<circle cx="122" cy="206" r="13" fill="#fef3c7" stroke="#0f172a" stroke-width="1.6"/>
<text x="122" y="210" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">E2</text>
<text x="144" y="210" text-anchor="start" font-size="11" font-weight="600" fill="#0f172a">tyrosinase</text>
<rect x="372" y="184" width="82" height="44" rx="8" fill="#dcfce7" stroke="#0f6e56" stroke-width="1.8"/>
<text x="413" y="202" text-anchor="middle" font-size="11" font-weight="600" fill="#0f172a">Information</text>
<text x="413" y="217" text-anchor="middle" font-size="11" font-weight="600" fill="#0f172a">génétique 2</text>
<line x1="370" y1="136" x2="296" y2="136" stroke="#0f6e56" stroke-width="1.6" stroke-dasharray="5 4"/>
<line x1="370" y1="206" x2="228" y2="206" stroke="#0f6e56" stroke-width="1.6" stroke-dasharray="5 4"/>
</svg>
:::

Si E2 manque, la flèche tyrosine vers mélanine est coupée ; si E1 manque, c'est la flèche phénylalanine vers tyrosine. La tyrosine peut aussi venir directement de l'alimentation.

::: exemple Exploiter deux documents : l'albinisme et la phénylcétonurie

1. **Observer l'albinisme.** Chez la personne normale, les mélanocytes fabriquent de la mélanine ; chez l'albinos, la peau est décolorée, donc il n'y a pas de mélanine. *Pourquoi : la couleur dépend de la quantité de mélanine produite.*
2. **Localiser la panne.** La tyrosine est disponible, mais la mélanine ne se forme pas : c'est l'étape tyrosine vers mélanine qui échoue, donc l'enzyme E2, la tyrosinase, n'est pas produite. *Pourquoi : sans l'enzyme, la réaction n'a pas lieu.*
3. **Observer la phénylcétonurie.** L'urine des enfants malades contient beaucoup d'acide phénylcétonurique (nom donné par le manuel ; le chimiste dit acide phénylpyruvique), et d'autant plus que l'alimentation est riche en phénylalanine ; la phénylalanine et cet acide s'accumulent dans le tissu nerveux et entraînent une déficience intellectuelle sévère. *Pourquoi : la phénylalanine, mal transformée en tyrosine, s'accumule et se retrouve en partie sous forme de cet acide : l'enzyme E1, la phénylalanine hydroxylase, fait défaut.*
4. **Conclure.** Dans les deux cas, le phénotype résulte de l'incapacité de fabriquer une enzyme, et chaque enzyme est commandée par une information génétique.
5. **Répondre à la question du manuel.** Une personne phénylcétonurique n'est pas forcément albinos : E1 et E2 dépendent de deux informations génétiques différentes. Si seule celle de E1 est modifiée, la tyrosinase est produite et la mélanine peut se former à partir de la tyrosine apportée par l'alimentation. *Pourquoi : deux enzymes, deux informations génétiques, deux pannes indépendantes.*

:::

::: piege
**Erreur : croire que l'albinos n'a pas de mélanocytes.** « Pas de mélanine, donc pas de cellules pour en fabriquer » tente parce que l'absence de couleur semble tout effacer. Mais l'albinos possède des mélanocytes ; ils ne produisent pas de mélanine parce qu'ils sont incapables de fabriquer la tyrosinase.
:::

> ⚠️ Ne confonds pas la **tyrosine**, substance de départ transformée en mélanine, et la **tyrosinase**, l'enzyme qui active cette transformation. De même pour la phénylalanine et la phénylalanine hydroxylase.

::: propriete
**De l'information génétique au phénotype.** Quand un phénotype dépend d'une réaction biochimique, l'information génétique le détermine en commandant la fabrication de la protéine qui l'active, ici une enzyme : une information génétique, une protéine, un phénotype.
Cas limite : toute protéine n'est pas une enzyme. L'ovalbumine, protéine du blanc d'œuf, est fabriquée par les cellules de l'oviducte de la poule puis excrétée : c'est une protéine excrétée, qui participe à la structure de l'œuf, et non une protéine de structure des cellules. On distingue ainsi des protéines de fonction (enzymes, hormones), des protéines de structure (qui entrent dans la constitution des cellules) et des protéines excrétées.
:::

::: verifie À toi : une chaîne inventée
Dans une chaîne A, B, C (donnée d'illustration), A devient B grâce à l'enzyme E1 et B devient C grâce à l'enzyme E2. Une personne ne fabrique pas E2. Quelle substance n'est plus fabriquée, et laquelle risque de s'accumuler ?

---

C n'est plus fabriquée, car B ne peut plus se transformer en C sans E2 ; B, qui n'est plus consommée, risque de s'accumuler, comme la phénylalanine quand E1 manque.
:::

::: retenir
Un phénotype comme la couleur de la peau dépend de la capacité de fabriquer une protéine : l'albinos ne fabrique pas la tyrosinase, le phénylcétonurique ne fabrique pas la phénylalanine hydroxylase, et chaque enzyme est sous le contrôle d'une information génétique.
:::

## 🔗 La protéine : une chaîne d'acides aminés

L'hémoglobine transporte l'oxygène, l'insuline agit sur la glycémie, la tyrosinase active la formation de la mélanine : trois protéines de rôles et de formes très différents. Pourtant, toutes sont construites avec les mêmes vingt acides aminés.
Qu'est-ce qui fait que deux protéines diffèrent ?

::: definition
**Acide aminé** — petite molécule de formule générale R–CH(NH2)–COOH ; il en existe 20 sortes dans les êtres vivants, notées par des abréviations (Met, Cys, Val, Glu…).
**Liaison peptidique** — liaison entre le groupement COOH d'un acide aminé et le groupement NH2 d'un autre. Deux acides aminés ainsi liés forment un **dipeptide**.
**Polypeptide** — chaîne d'acides aminés unis par des liaisons peptidiques. Une **protéine** est une macromolécule formée d'un grand nombre d'acides aminés.
:::

::: figure Un tripeptide : trois acides aminés enchaînés, deux liaisons peptidiques (en vert) entre le groupement CO d'un acide aminé et le groupement NH du suivant
<svg viewBox="0 0 484 172">
<title>Tripeptide : trois acides aminés H2N-CH(R)-CO enchaînés, deux liaisons peptidiques entre CO et NH</title>
<rect x="14" y="46" width="136" height="92" rx="12" fill="#e0f2fe" stroke="#0f172a" stroke-width="1.5"/>
<text x="82" y="156" text-anchor="middle" font-size="11" font-weight="600" fill="#0f172a">acide aminé 1</text>
<rect x="168" y="46" width="132" height="92" rx="12" fill="#e0f2fe" stroke="#0f172a" stroke-width="1.5"/>
<text x="234" y="156" text-anchor="middle" font-size="11" font-weight="600" fill="#0f172a">acide aminé 2</text>
<rect x="318" y="46" width="152" height="92" rx="12" fill="#e0f2fe" stroke="#0f172a" stroke-width="1.5"/>
<text x="394" y="156" text-anchor="middle" font-size="11" font-weight="600" fill="#0f172a">acide aminé 3</text>
<line x1="50" y1="110" x2="420" y2="110" stroke="#64748b" stroke-width="2"/>
<line x1="132" y1="110" x2="190" y2="110" stroke="#0f6e56" stroke-width="5"/>
<line x1="282" y1="110" x2="340" y2="110" stroke="#0f6e56" stroke-width="5"/>
<rect x="18" y="98" width="35" height="24" rx="6" fill="#ffffff" stroke="#0f172a" stroke-width="1.3"/>
<text x="36" y="115" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">H2N</text>
<rect x="72" y="98" width="28" height="24" rx="6" fill="#ffffff" stroke="#0f172a" stroke-width="1.3"/>
<text x="86" y="115" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">CH</text>
<rect x="118" y="98" width="28" height="24" rx="6" fill="#ffffff" stroke="#0f172a" stroke-width="1.3"/>
<text x="132" y="115" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">CO</text>
<rect x="176" y="98" width="28" height="24" rx="6" fill="#ffffff" stroke="#0f172a" stroke-width="1.3"/>
<text x="190" y="115" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">NH</text>
<rect x="222" y="98" width="28" height="24" rx="6" fill="#ffffff" stroke="#0f172a" stroke-width="1.3"/>
<text x="236" y="115" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">CH</text>
<rect x="268" y="98" width="28" height="24" rx="6" fill="#ffffff" stroke="#0f172a" stroke-width="1.3"/>
<text x="282" y="115" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">CO</text>
<rect x="326" y="98" width="28" height="24" rx="6" fill="#ffffff" stroke="#0f172a" stroke-width="1.3"/>
<text x="340" y="115" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">NH</text>
<rect x="372" y="98" width="28" height="24" rx="6" fill="#ffffff" stroke="#0f172a" stroke-width="1.3"/>
<text x="386" y="115" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">CH</text>
<rect x="415" y="98" width="42" height="24" rx="6" fill="#ffffff" stroke="#0f172a" stroke-width="1.3"/>
<text x="436" y="115" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">COOH</text>
<line x1="86" y1="98" x2="86" y2="76" stroke="#0f172a" stroke-width="1.5"/>
<circle cx="86" cy="66" r="12" fill="#fde68a" stroke="#0f172a" stroke-width="1.5"/>
<text x="86" y="70" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a">R1</text>
<line x1="236" y1="98" x2="236" y2="76" stroke="#0f172a" stroke-width="1.5"/>
<circle cx="236" cy="66" r="12" fill="#fde68a" stroke="#0f172a" stroke-width="1.5"/>
<text x="236" y="70" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a">R2</text>
<line x1="386" y1="98" x2="386" y2="76" stroke="#0f172a" stroke-width="1.5"/>
<circle cx="386" cy="66" r="12" fill="#fde68a" stroke="#0f172a" stroke-width="1.5"/>
<text x="386" y="70" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a">R3</text>
<text x="161" y="20" text-anchor="middle" font-size="11" font-weight="600" fill="#0f6e56">liaison peptidique</text>
<line x1="161" y1="26" x2="161" y2="100" stroke="#0f6e56" stroke-width="1.5" stroke-dasharray="4 3"/>
<text x="311" y="20" text-anchor="middle" font-size="11" font-weight="600" fill="#0f6e56">liaison peptidique</text>
<line x1="311" y1="26" x2="311" y2="100" stroke="#0f6e56" stroke-width="1.5" stroke-dasharray="4 3"/>
</svg>
:::

Le même motif H2N–CH–CO se répète ; seul le groupe R, propre à chaque acide aminé, change. Entre deux acides aminés voisins, une liaison peptidique : trois acides aminés, deux liaisons.

::: exemple Compter les liaisons et comparer deux chaînes

1. **Représenter la chaîne.** La chaîne B de l'insuline humaine compte 30 acides aminés alignés (Phe–Val–Asn–…–Thr). *Pourquoi : un polypeptide est une chaîne linéaire de maillons.*
2. **Compter les jonctions.** Avec 2 acides aminés il y a 1 liaison, avec 3 il y en a 2 (voir le dessin) : avec 30 il y en a 29. *Pourquoi : chaque liaison se trouve entre deux voisins, il y a donc un maillon de plus que de jonctions.*
3. **Refaire pour la chaîne A.** 21 acides aminés, donc 20 liaisons. *Pourquoi : même raisonnement, nombre d'acides aminés moins un.*
4. **Comparer deux chaînes.** Phe–Val–Asn et Asn–Val–Phe contiennent les mêmes acides aminés et le même nombre de liaisons (2), mais dans un ordre différent : ce sont deux polypeptides différents. *Pourquoi : une protéine se définit par le nombre et l'ordre de ses acides aminés.*

:::

::: piege
**Erreur : compter autant de liaisons que d'acides aminés.** « 30 acides aminés, donc 30 liaisons » tente parce qu'on compte des objets. Mais une liaison relie deux acides aminés voisins : sur une chaîne de 30, il y en a 29.
:::

::: propriete
**Ce qui distingue deux protéines.** Deux protéines diffèrent par le nombre de leurs acides aminés, par leur ordre et, en conséquence, par leur forme dans l'espace et leur fonction. La séquence d'acides aminés est déterminée par l'information génétique : changer un seul acide aminé, comme Glu en Val dans l'hémoglobine du chapitre précédent, donne une protéine différente.
Cas limite : un dipeptide ne compte qu'une seule liaison peptidique.
:::

::: verifie À toi : douze maillons
Un polypeptide compte 12 acides aminés. Combien de liaisons peptidiques contient-il ? Si l'on échange l'ordre de deux acides aminés, ce nombre change-t-il ?

---

Il contient 12 − 1 = 11 liaisons, une entre chaque couple de voisins. Échanger deux acides aminés ne change pas ce nombre, qui ne dépend que du nombre d'acides aminés ; mais le polypeptide obtenu est différent, car l'ordre a changé.
:::

::: retenir
Une protéine est une chaîne d'acides aminés unis par des liaisons peptidiques (une de moins que d'acides aminés) ; ce sont leur nombre et leur ordre, déterminés par l'information génétique, qui distinguent les protéines.
:::

## 🏭 Le ribosome : l'atelier de fabrication des protéines

Les cellules des glandes digestives fabriquent sans cesse des enzymes, et celles des glandes qui sécrètent l'insuline ou le glucagon, des hormones de nature protéique. Or l'ADN reste dans le noyau, alors que les protéines se fabriquent dans le cytoplasme.
Dans quel organite, précisément, les acides aminés sont-ils assemblés ?

::: definition
**Ribosome** — organite du cytoplasme formé de protéines et d'ARN, constitué de deux sous-unités, une petite et une grande : c'est là que les protéines sont assemblées.
**Polysome** — ensemble de ribosomes liés par un même filament.
**Érythroblaste** — cellule précurseur des hématies (globules rouges ou érythrocytes), encore pourvue d'un noyau et de ribosomes. L'hématie mûre a perdu son noyau et ses ribosomes.
:::

::: figure Un polysome : quatre ribosomes (deux sous-unités chacun) enfilés sur un même filament d'ARNm ; la chaîne d'acides aminés qu'ils portent s'allonge de 2 à 8 maillons dans le sens de déplacement
<svg viewBox="0 0 490 266">
<title>Polysome : quatre ribosomes sur un filament d'ARNm, portant des chaînes de 2, 4, 6 et 8 acides aminés</title>
<line x1="20" y1="190" x2="470" y2="190" stroke="#0f6e56" stroke-width="4"/>
<circle cx="100" cy="148" r="4.2" fill="#c4b5fd" stroke="#0f172a" stroke-width="1"/>
<circle cx="100" cy="139" r="4.2" fill="#c4b5fd" stroke="#0f172a" stroke-width="1"/>
<ellipse cx="100" cy="170" rx="26" ry="16" fill="#bae6fd" stroke="#0f172a" stroke-width="1.6"/>
<ellipse cx="100" cy="199" rx="20" ry="9" fill="#7dd3fc" stroke="#0f172a" stroke-width="1.6"/>
<circle cx="190" cy="148" r="4.2" fill="#c4b5fd" stroke="#0f172a" stroke-width="1"/>
<circle cx="190" cy="139" r="4.2" fill="#c4b5fd" stroke="#0f172a" stroke-width="1"/>
<circle cx="190" cy="130" r="4.2" fill="#c4b5fd" stroke="#0f172a" stroke-width="1"/>
<circle cx="190" cy="121" r="4.2" fill="#c4b5fd" stroke="#0f172a" stroke-width="1"/>
<ellipse cx="190" cy="170" rx="26" ry="16" fill="#bae6fd" stroke="#0f172a" stroke-width="1.6"/>
<ellipse cx="190" cy="199" rx="20" ry="9" fill="#7dd3fc" stroke="#0f172a" stroke-width="1.6"/>
<circle cx="280" cy="148" r="4.2" fill="#c4b5fd" stroke="#0f172a" stroke-width="1"/>
<circle cx="280" cy="139" r="4.2" fill="#c4b5fd" stroke="#0f172a" stroke-width="1"/>
<circle cx="280" cy="130" r="4.2" fill="#c4b5fd" stroke="#0f172a" stroke-width="1"/>
<circle cx="280" cy="121" r="4.2" fill="#c4b5fd" stroke="#0f172a" stroke-width="1"/>
<circle cx="280" cy="112" r="4.2" fill="#c4b5fd" stroke="#0f172a" stroke-width="1"/>
<circle cx="280" cy="103" r="4.2" fill="#c4b5fd" stroke="#0f172a" stroke-width="1"/>
<ellipse cx="280" cy="170" rx="26" ry="16" fill="#bae6fd" stroke="#0f172a" stroke-width="1.6"/>
<ellipse cx="280" cy="199" rx="20" ry="9" fill="#7dd3fc" stroke="#0f172a" stroke-width="1.6"/>
<circle cx="370" cy="148" r="4.2" fill="#c4b5fd" stroke="#0f172a" stroke-width="1"/>
<circle cx="370" cy="139" r="4.2" fill="#c4b5fd" stroke="#0f172a" stroke-width="1"/>
<circle cx="370" cy="130" r="4.2" fill="#c4b5fd" stroke="#0f172a" stroke-width="1"/>
<circle cx="370" cy="121" r="4.2" fill="#c4b5fd" stroke="#0f172a" stroke-width="1"/>
<circle cx="370" cy="112" r="4.2" fill="#c4b5fd" stroke="#0f172a" stroke-width="1"/>
<circle cx="370" cy="103" r="4.2" fill="#c4b5fd" stroke="#0f172a" stroke-width="1"/>
<circle cx="370" cy="94" r="4.2" fill="#c4b5fd" stroke="#0f172a" stroke-width="1"/>
<circle cx="370" cy="85" r="4.2" fill="#c4b5fd" stroke="#0f172a" stroke-width="1"/>
<ellipse cx="370" cy="170" rx="26" ry="16" fill="#bae6fd" stroke="#0f172a" stroke-width="1.6"/>
<ellipse cx="370" cy="199" rx="20" ry="9" fill="#7dd3fc" stroke="#0f172a" stroke-width="1.6"/>
<line x1="150" y1="238" x2="326.0" y2="238.0" stroke="#0f172a" stroke-width="2.2"/><polygon points="330,238 322.8,241.5 322.8,234.5" fill="#0f172a"/>
<text x="240" y="256" text-anchor="middle" font-size="11" font-weight="600" fill="#0f172a">sens de déplacement des ribosomes</text>
<text x="20" y="224" text-anchor="start" font-size="11" font-weight="700" fill="#0f6e56">ARNm</text>
<text x="40" y="180" text-anchor="middle" font-size="1" font-weight="700" fill="#0f172a"></text>
<text x="445" y="212" text-anchor="middle" font-size="1" font-weight="700" fill="#0f172a"></text>
</svg>
:::

Plus la chaîne portée par un ribosome est longue, plus ce ribosome est avancé sur le filament : les quatre ribosomes travaillent en même temps, à des stades différents.

| Cellule | Noyau | Ribosomes | Fabrique l'hémoglobine |
| --- | --- | --- | --- |
| Érythroblaste | oui | oui | oui |
| Hématie | non | non | non |

::: exemple Exploiter des constats puis une expérience

1. **Premier constat.** Les cellules des glandes à enzymes digestives ou à hormones protéiques sont particulièrement riches en ribosomes ; les autres cellules en ont peu. *Pourquoi : on compare le nombre de ribosomes à l'intensité de la synthèse de protéines.*
2. **Deuxième constat.** L'érythroblaste, qui a un noyau et des ribosomes, fabrique l'hémoglobine ; l'hématie, sans noyau et sans ribosomes, en est incapable. *Pourquoi : le lien entre ribosomes et synthèse se confirme.*
3. **Prendre du recul.** L'hématie n'a ni ribosomes ni noyau : le tableau seul ne permet pas de désigner le ribosome. *Pourquoi : deux différences vont ensemble, il faut une expérience pour les séparer.*
4. **Tester.** On cultive des érythroblastes avec des acides aminés marqués au carbone 14 (¹⁴C) : la radioactivité se retrouve dans les ribosomes et dans l'hémoglobine synthétisée. *Pourquoi : un marqueur radioactif permet de suivre le devenir des acides aminés, qui sont utilisés au niveau des ribosomes puis incorporés à la protéine.*
5. **Conclure.** Les protéines sont assemblées dans le cytoplasme, au niveau des ribosomes, et non dans le noyau où se trouve l'ADN.

:::

::: piege
**Erreur : placer la fabrication des protéines dans le noyau.** « L'ADN commande tout, donc les protéines s'y fabriquent » tente parce que l'information est dans le noyau. Mais le noyau garde l'information ; l'assemblage des acides aminés se fait dans le cytoplasme, sur les ribosomes.
:::

::: propriete
**Où se fabriquent les protéines.** La synthèse des protéines a lieu dans le cytoplasme, au niveau des ribosomes. Dans un polysome, plusieurs ribosomes lisent le même filament en même temps ; le plus avancé porte la chaîne la plus longue.
Cas limite : une cellule privée de ribosomes, comme l'hématie, ne peut plus fabriquer d'hémoglobine.
:::

::: verifie À toi : la cellule à insuline
Les cellules du pancréas qui sécrètent l'insuline contiennent-elles beaucoup ou peu de ribosomes ? Justifie.

---

Beaucoup : l'insuline est une hormone de nature protéique, donc ces cellules fabriquent d'énormes quantités de protéines, comme les cellules des glandes digestives ; or la synthèse des protéines se fait aux ribosomes.
:::

::: retenir
Les protéines sont assemblées dans le cytoplasme, au niveau des ribosomes (deux sous-unités), souvent en polysomes, et non dans le noyau.
:::

## 📨 L'ARN messager : la copie qui voyage

L'information est dans l'ADN, au noyau ; la fabrication se fait dans le cytoplasme. Quelque chose doit faire le lien. Au microscope électronique, les ribosomes d'un polysome sont tous enfilés sur un long filament.
Que contient ce filament, et d'où vient-il ?

::: definition
**ARN messager (ARNm)** — acide ribonucléique formé d'un seul brin (monocaténaire), polymère de nucléotides.
Chaque **ribonucléotide** associe un sucre à 5 carbones, le **ribose**, un acide phosphorique et une base azotée : adénine (A), guanine (G), cytosine (C) ou **uracile (U)**.
:::

| | ADN | ARNm |
| --- | --- | --- |
| Nombre de brins | deux (double hélice) | un seul |
| Sucre | désoxyribose | ribose |
| Bases | A, T, G, C | A, U, G, C |
| Lieu | noyau (chromosomes) | synthétisé dans le noyau, puis dans le cytoplasme |

::: figure Un brin d'ARNm de cinq nucléotides : une chaîne alternant acide phosphorique (P) et ribose (R), avec une base azotée accrochée sous chaque ribose
<svg viewBox="0 0 420 180">
<title>Un brin d'ARNm de cinq nucléotides : chaîne P R P R, avec une base azotée A, G, U, C, A sous chaque ribose</title>
<line x1="20" y1="60" x2="395" y2="60" stroke="#64748b" stroke-width="3"/>
<circle cx="40" cy="60" r="12" fill="#fde68a" stroke="#0f172a" stroke-width="1.6"/>
<text x="40" y="64" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">P</text>
<polygon points="72,48 84,57 80,72 64,72 60,57" fill="#dcfce7" stroke="#0f172a" stroke-width="1.6"/>
<text x="72" y="67" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">R</text>
<line x1="72" y1="72" x2="72" y2="102" stroke="#0f172a" stroke-width="1.6"/>
<rect x="55" y="102" width="34" height="32" rx="6" fill="#fde68a" stroke="#0f172a" stroke-width="1.6"/>
<text x="72" y="125" text-anchor="middle" font-size="15" font-weight="700" fill="#0f172a">A</text>
<circle cx="110" cy="60" r="12" fill="#fde68a" stroke="#0f172a" stroke-width="1.6"/>
<text x="110" y="64" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">P</text>
<polygon points="142,48 154,57 150,72 134,72 130,57" fill="#dcfce7" stroke="#0f172a" stroke-width="1.6"/>
<text x="142" y="67" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">R</text>
<line x1="142" y1="72" x2="142" y2="102" stroke="#0f172a" stroke-width="1.6"/>
<rect x="125" y="102" width="34" height="32" rx="6" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.6"/>
<text x="142" y="125" text-anchor="middle" font-size="15" font-weight="700" fill="#0f172a">G</text>
<circle cx="180" cy="60" r="12" fill="#fde68a" stroke="#0f172a" stroke-width="1.6"/>
<text x="180" y="64" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">P</text>
<polygon points="212,48 224,57 220,72 204,72 200,57" fill="#dcfce7" stroke="#0f172a" stroke-width="1.6"/>
<text x="212" y="67" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">R</text>
<line x1="212" y1="72" x2="212" y2="102" stroke="#0f172a" stroke-width="1.6"/>
<rect x="195" y="102" width="34" height="32" rx="6" fill="#fed7aa" stroke="#0f172a" stroke-width="1.6"/>
<text x="212" y="125" text-anchor="middle" font-size="15" font-weight="700" fill="#0f172a">U</text>
<circle cx="250" cy="60" r="12" fill="#fde68a" stroke="#0f172a" stroke-width="1.6"/>
<text x="250" y="64" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">P</text>
<polygon points="282,48 294,57 290,72 274,72 270,57" fill="#dcfce7" stroke="#0f172a" stroke-width="1.6"/>
<text x="282" y="67" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">R</text>
<line x1="282" y1="72" x2="282" y2="102" stroke="#0f172a" stroke-width="1.6"/>
<rect x="265" y="102" width="34" height="32" rx="6" fill="#fecaca" stroke="#0f172a" stroke-width="1.6"/>
<text x="282" y="125" text-anchor="middle" font-size="15" font-weight="700" fill="#0f172a">C</text>
<circle cx="320" cy="60" r="12" fill="#fde68a" stroke="#0f172a" stroke-width="1.6"/>
<text x="320" y="64" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">P</text>
<polygon points="352,48 364,57 360,72 344,72 340,57" fill="#dcfce7" stroke="#0f172a" stroke-width="1.6"/>
<text x="352" y="67" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">R</text>
<line x1="352" y1="72" x2="352" y2="102" stroke="#0f172a" stroke-width="1.6"/>
<rect x="335" y="102" width="34" height="32" rx="6" fill="#fde68a" stroke="#0f172a" stroke-width="1.6"/>
<text x="352" y="125" text-anchor="middle" font-size="15" font-weight="700" fill="#0f172a">A</text>
<text x="20" y="168" text-anchor="start" font-size="11" font-weight="600" fill="#0f172a">P : acide phosphorique</text>
<text x="200" y="168" text-anchor="start" font-size="11" font-weight="600" fill="#0f172a">R : ribose</text>
<text x="290" y="168" text-anchor="start" font-size="11" font-weight="600" fill="#0f172a">A, G, U, C : bases azotées</text>
</svg>
:::

La séquence A, G, U, C, A est l'information : elle est écrite comme sur l'ADN, mais avec U à la place de T.

::: exemple Exploiter l'expérience des œufs de grenouille
On injecte à des œufs de grenouille des molécules isolées de filaments de polysomes d'érythroblastes, puis on les place avec des œufs normaux dans un milieu riche en acides aminés radioactifs.

| Lot d'œufs | Molécules injectées | Hémoglobine radioactive |
| --- | --- | --- |
| Traité | filaments de polysomes d'érythroblastes | présente |
| Témoin | aucune | absente |

1. **Comparer les deux lots.** Même milieu, même espèce : seule l'injection diffère. *Pourquoi : la différence de résultat ne peut venir que de ce qui diffère.*
2. **Interpréter.** Des œufs qui ne fabriquent pas d'hémoglobine en fabriquent dès qu'on leur injecte ces molécules : elles orientent le cytoplasme vers la synthèse d'une protéine précise. *Pourquoi : elles portent l'information qui détermine laquelle.*
3. **Nommer.** L'analyse chimique montre un acide ribonucléique : l'ARN messager. *Pourquoi : « messager » parce qu'il transmet l'information.*
4. **Relier à l'ADN.** Dans le noyau d'une cellule active, on voit l'ARNm se former au contact d'un brin d'ADN. *Pourquoi : un produit fabriqué sur un modèle porte l'information de ce modèle.*
5. **Répondre à la question.** Le filament est de l'ARNm, synthétisé dans le noyau à partir d'un brin d'ADN, puis envoyé au cytoplasme.

:::

::: piege
**Erreur : croire que l'ARN contient de la thymine, comme l'ADN.** « Même alphabet, donc mêmes bases » tente parce que A, G et C sont communes. Mais dans l'ARN, l'uracile remplace la thymine : l'ARNm ne contient jamais de T. Le messager est un acide ribonucléique, pas un acide désoxyribonucléique.
:::

::: propriete
**L'ARNm, intermédiaire entre le noyau et le ribosome.** L'ARNm est synthétisé dans le noyau à partir d'un brin d'ADN, passe dans le cytoplasme et oriente, au niveau des ribosomes, la synthèse d'une protéine déterminée.
Cas limite : l'ADN chromosomique ne quitte pas le noyau ; c'est sa copie de passage, l'ARNm, qui sort.
:::

::: verifie À toi : ADN ou ARN ?
Une molécule extraite d'une cellule possède un seul brin, du ribose et les bases A, U, G et C. Est-ce de l'ADN ou de l'ARN ? Quels indices permettent de le dire à coup sûr ?

---

C'est de l'ARN. Le ribose (l'ADN a du désoxyribose) et l'uracile (l'ADN a de la thymine) suffisent chacun à le montrer ; le simple brin confirme.
:::

::: retenir
L'ARN messager est un polymère à un seul brin (ribose, bases A, U, G, C), synthétisé dans le noyau à partir d'un brin d'ADN : il transporte l'information jusqu'aux ribosomes.
:::

## ⚙️ ARNt, ATP, enzymes : les autres acteurs

Au laboratoire, un chercheur mélange dans un tube de l'ARNm, des ribosomes, de l'ATP et des acides aminés radioactifs. Aucune protéine n'apparaît. Il manque encore des acteurs.
Lesquels, et comment le prouver ?

::: definition
**ARN de transfert (ARNt)** — petite molécule d'ARN d'environ 75 nucléotides, spécifique d'un seul acide aminé, qu'elle fixe et conduit au ribosome. Elle porte un triplet de bases, l'**anticodon**.
**ATP** — molécule qui fournit l'énergie de la synthèse.
**Enzymes** — activent des réactions de la synthèse, par exemple la fixation d'un acide aminé sur son ARNt ; des ions (Mg²⁺, PO₄³⁻) interviennent aussi.
:::

::: figure Un ARNt chargé de méthionine (schéma très simplifié) : l'acide aminé est fixé à une extrémité, l'anticodon UAC se trouve à l'autre
<svg viewBox="0 0 330 250">
<title>ARNt chargé de méthionine : l'acide aminé est fixé à une extrémité, l'anticodon UAC se trouve à l'autre</title>
<path d="M120 70 L120 168 Q120 192 150 192 Q180 192 180 168 L180 70" fill="#fef3c7" stroke="#0f172a" stroke-width="3" stroke-linejoin="round"/>
<line x1="180" y1="70" x2="180" y2="50" stroke="#0f172a" stroke-width="3"/>
<circle cx="180" cy="36" r="17" fill="#c4b5fd" stroke="#0f172a" stroke-width="1.8"/>
<text x="180" y="41" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a">Met</text>
<rect x="122" y="204" width="26" height="28" rx="5" fill="#fed7aa" stroke="#0f172a" stroke-width="1.6"/>
<text x="135" y="224" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">U</text>
<rect x="150" y="204" width="26" height="28" rx="5" fill="#fde68a" stroke="#0f172a" stroke-width="1.6"/>
<text x="163" y="224" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">A</text>
<rect x="178" y="204" width="26" height="28" rx="5" fill="#fecaca" stroke="#0f172a" stroke-width="1.6"/>
<text x="191" y="224" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">C</text>
<text x="100" y="120" text-anchor="end" font-size="13" font-weight="700" fill="#0f172a">ARNt</text>
<text x="214" y="224" text-anchor="start" font-size="12" font-weight="600" fill="#0f172a">anticodon</text>
<text x="212" y="40" text-anchor="start" font-size="11" font-weight="600" fill="#0f172a">acide aminé fixé</text>
</svg>
:::

L'anticodon désigne l'acide aminé que porte l'ARNt : ici, UAC va avec la méthionine.

Résultats de synthèse protéique in vitro (« homogénéat total » : broyat de foie de lapin dont les organites sont intacts) :

| Expérience | Protéine radioactive synthétisée |
| --- | --- |
| Homogénéat total + acides aminés radioactifs | oui |
| Homogénéat total + acides aminés radioactifs + DNP (substance qui empêche la production d'ATP ; le manuel écrit : « bloque l'utilisation de l'ATP ») | non |
| Homogénéat total bouilli + acides aminés radioactifs | non |
| ARNm + ribosomes + acides aminés radioactifs | non |
| ARNm + ribosomes + ATP + acides aminés radioactifs | non |

::: exemple Lire un tableau de synthèse in vitro

1. **Ligne 1, la référence.** L'homogénéat total fabrique de la protéine radioactive : tous les acteurs nécessaires sont présents. *Pourquoi : c'est l'expérience qui réussit.*
2. **Ligne 2.** Avec le DNP, plus de synthèse : l'ATP est indispensable. *Pourquoi : c'est la seule différence avec la ligne 1, et elle prive la synthèse d'énergie.*
3. **Ligne 3.** Bouilli, l'homogénéat ne synthétise plus : des constituants que la chaleur détruit, comme les enzymes, sont indispensables. *Pourquoi : l'ébullition, seule différence, détruit les protéines.*
4. **Lignes 4 et 5.** ARNm et ribosomes, avec ou sans ATP, ne font rien : ils sont nécessaires mais ne suffisent pas. *Pourquoi : l'homogénéat complet réussit, il contient donc d'autres acteurs.*
5. **Conclure.** Le tableau montre qu'il manque d'autres acteurs que l'ARNm et les ribosomes. D'autres expériences montrent que les acides aminés radioactifs se fixent sur des ARN différents de l'ARNm, les ARNt ; avec les enzymes et l'ATP, ils complètent le dispositif.

:::

::: piege
**Erreur : croire que l'ARNm et les ribosomes suffisent.** « L'un porte l'information, l'autre fabrique : on a tout » tente parce que ce sont les deux acteurs les plus visibles. Mais les lignes 4 et 5 du tableau montrent qu'ils ne produisent aucune protéine seuls, même avec de l'ATP.
:::

::: propriete
**Les acteurs de la synthèse et leur rôle.** L'ARNm porte l'information et détermine la protéine fabriquée ; le ribosome est seulement le lieu d'assemblage ; l'ARNt amène l'acide aminé qui correspond à un codon ; l'ATP apporte l'énergie ; les enzymes activent les réactions. Chaque ARNt n'étant spécifique que d'un acide aminé et les acides aminés étant au nombre de 20, il existe au moins 20 types d'ARNt.
Cas limite : il suffit qu'un acteur manque (ATP bloqué, enzymes détruites) pour arrêter la synthèse, mais en réunir deux ou trois ne suffit pas tant qu'il en manque encore.
:::

::: verifie À toi : sans ARNt
On refait l'expérience avec un homogénéat auquel on a retiré tous les ARNt (donnée d'illustration). La synthèse a-t-elle lieu ? Avec quelles lignes du tableau ce résultat se range-t-il ?

---

Non : sans ARNt, aucun acide aminé n'est conduit au ribosome en face des codons. Ce résultat rejoint les lignes 4 et 5, où des acteurs manquent aussi.
:::

::: retenir
La synthèse protéique réunit l'ARNm, les ribosomes, les ARNt (au moins 20 types, chacun spécifique d'un acide aminé), l'ATP et des enzymes : aucun ne suffit seul.
:::

## 📝 La transcription : du gène à l'ARNm

Dans le noyau d'une cellule très active, on voit l'ARNm se former au contact d'un brin d'ADN, comme une arête de poisson qui s'en détache. L'ADN est écrit avec A, T, G, C ; l'ARNm avec A, U, G, C.
Comment l'ordre des bases de l'ADN se retrouve-t-il dans l'ARNm ?

::: definition
**Transcription** — synthèse d'un ARNm à partir d'un brin d'ADN, dans le noyau, par une enzyme, l'**ARN polymérase**, selon la complémentarité des bases : A de l'ADN avec U, T avec A, G avec C, C avec G.
**Brin transcrit** — brin d'ADN qui sert de modèle.
**Codon** — triplet de bases de l'ARNm.
:::

> 🗡️ Le manuel appelle aussi « brin codant » le brin qui sert de modèle ; dans l'usage courant, ce nom désigne l'autre brin, celui qui a la séquence de l'ARNm. Ici, on dit toujours **brin transcrit**.

::: figure Transcription : chaque base de l'ARNm (rangée du bas) est complémentaire de la base du brin transcrit placée au-dessus d'elle ; les douze bases forment quatre codons
<svg viewBox="0 0 460 200">
<title>Transcription : chaque base de l'ARNm est complémentaire de la base du brin transcrit placée au-dessus d'elle ; l'ARNm se lit en quatre codons</title>
<text x="24" y="22" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a">brin transcrit de l'ADN</text>
<text x="24" y="190" text-anchor="start" font-size="12" font-weight="700" fill="#0f6e56">ARNm synthétisé</text>
<rect x="31" y="34" width="26" height="28" rx="5" fill="#fde68a" stroke="#0f172a" stroke-width="1.5"/>
<text x="44" y="54" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">A</text>
<line x1="44" y1="64" x2="44" y2="106" stroke="#64748b" stroke-width="1.6" stroke-dasharray="4 3"/>
<rect x="31" y="108" width="26" height="28" rx="5" fill="#fed7aa" stroke="#0f6e56" stroke-width="2"/>
<text x="44" y="128" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">U</text>
<rect x="65" y="34" width="26" height="28" rx="5" fill="#fecaca" stroke="#0f172a" stroke-width="1.5"/>
<text x="78" y="54" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">C</text>
<line x1="78" y1="64" x2="78" y2="106" stroke="#64748b" stroke-width="1.6" stroke-dasharray="4 3"/>
<rect x="65" y="108" width="26" height="28" rx="5" fill="#bfdbfe" stroke="#0f6e56" stroke-width="2"/>
<text x="78" y="128" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">G</text>
<rect x="99" y="34" width="26" height="28" rx="5" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.5"/>
<text x="112" y="54" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">G</text>
<line x1="112" y1="64" x2="112" y2="106" stroke="#64748b" stroke-width="1.6" stroke-dasharray="4 3"/>
<rect x="99" y="108" width="26" height="28" rx="5" fill="#fecaca" stroke="#0f6e56" stroke-width="2"/>
<text x="112" y="128" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">C</text>
<rect x="133" y="34" width="26" height="28" rx="5" fill="#fed7aa" stroke="#0f172a" stroke-width="1.5"/>
<text x="146" y="54" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">T</text>
<line x1="146" y1="64" x2="146" y2="106" stroke="#64748b" stroke-width="1.6" stroke-dasharray="4 3"/>
<rect x="133" y="108" width="26" height="28" rx="5" fill="#fde68a" stroke="#0f6e56" stroke-width="2"/>
<text x="146" y="128" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">A</text>
<rect x="167" y="34" width="26" height="28" rx="5" fill="#fed7aa" stroke="#0f172a" stroke-width="1.5"/>
<text x="180" y="54" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">T</text>
<line x1="180" y1="64" x2="180" y2="106" stroke="#64748b" stroke-width="1.6" stroke-dasharray="4 3"/>
<rect x="167" y="108" width="26" height="28" rx="5" fill="#fde68a" stroke="#0f6e56" stroke-width="2"/>
<text x="180" y="128" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">A</text>
<rect x="201" y="34" width="26" height="28" rx="5" fill="#fecaca" stroke="#0f172a" stroke-width="1.5"/>
<text x="214" y="54" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">C</text>
<line x1="214" y1="64" x2="214" y2="106" stroke="#64748b" stroke-width="1.6" stroke-dasharray="4 3"/>
<rect x="201" y="108" width="26" height="28" rx="5" fill="#bfdbfe" stroke="#0f6e56" stroke-width="2"/>
<text x="214" y="128" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">G</text>
<rect x="235" y="34" width="26" height="28" rx="5" fill="#fecaca" stroke="#0f172a" stroke-width="1.5"/>
<text x="248" y="54" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">C</text>
<line x1="248" y1="64" x2="248" y2="106" stroke="#64748b" stroke-width="1.6" stroke-dasharray="4 3"/>
<rect x="235" y="108" width="26" height="28" rx="5" fill="#bfdbfe" stroke="#0f6e56" stroke-width="2"/>
<text x="248" y="128" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">G</text>
<rect x="269" y="34" width="26" height="28" rx="5" fill="#fed7aa" stroke="#0f172a" stroke-width="1.5"/>
<text x="282" y="54" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">T</text>
<line x1="282" y1="64" x2="282" y2="106" stroke="#64748b" stroke-width="1.6" stroke-dasharray="4 3"/>
<rect x="269" y="108" width="26" height="28" rx="5" fill="#fde68a" stroke="#0f6e56" stroke-width="2"/>
<text x="282" y="128" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">A</text>
<rect x="303" y="34" width="26" height="28" rx="5" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.5"/>
<text x="316" y="54" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">G</text>
<line x1="316" y1="64" x2="316" y2="106" stroke="#64748b" stroke-width="1.6" stroke-dasharray="4 3"/>
<rect x="303" y="108" width="26" height="28" rx="5" fill="#fecaca" stroke="#0f6e56" stroke-width="2"/>
<text x="316" y="128" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">C</text>
<rect x="337" y="34" width="26" height="28" rx="5" fill="#fde68a" stroke="#0f172a" stroke-width="1.5"/>
<text x="350" y="54" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">A</text>
<line x1="350" y1="64" x2="350" y2="106" stroke="#64748b" stroke-width="1.6" stroke-dasharray="4 3"/>
<rect x="337" y="108" width="26" height="28" rx="5" fill="#fed7aa" stroke="#0f6e56" stroke-width="2"/>
<text x="350" y="128" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">U</text>
<rect x="371" y="34" width="26" height="28" rx="5" fill="#fed7aa" stroke="#0f172a" stroke-width="1.5"/>
<text x="384" y="54" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">T</text>
<line x1="384" y1="64" x2="384" y2="106" stroke="#64748b" stroke-width="1.6" stroke-dasharray="4 3"/>
<rect x="371" y="108" width="26" height="28" rx="5" fill="#fde68a" stroke="#0f6e56" stroke-width="2"/>
<text x="384" y="128" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">A</text>
<rect x="405" y="34" width="26" height="28" rx="5" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.5"/>
<text x="418" y="54" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">G</text>
<line x1="418" y1="64" x2="418" y2="106" stroke="#64748b" stroke-width="1.6" stroke-dasharray="4 3"/>
<rect x="405" y="108" width="26" height="28" rx="5" fill="#fecaca" stroke="#0f6e56" stroke-width="2"/>
<text x="418" y="128" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">C</text>
<path d="M31 144 L31 150 L125 150 L125 144" fill="none" stroke="#0f6e56" stroke-width="2"/>
<text x="78.0" y="166" text-anchor="middle" font-size="11" font-weight="600" fill="#0f6e56">codon 1</text>
<path d="M133 144 L133 150 L227 150 L227 144" fill="none" stroke="#0f6e56" stroke-width="2"/>
<text x="180.0" y="166" text-anchor="middle" font-size="11" font-weight="600" fill="#0f6e56">codon 2</text>
<path d="M235 144 L235 150 L329 150 L329 144" fill="none" stroke="#0f6e56" stroke-width="2"/>
<text x="282.0" y="166" text-anchor="middle" font-size="11" font-weight="600" fill="#0f6e56">codon 3</text>
<path d="M337 144 L337 150 L431 150 L431 144" fill="none" stroke="#0f6e56" stroke-width="2"/>
<text x="384.0" y="166" text-anchor="middle" font-size="11" font-weight="600" fill="#0f6e56">codon 4</text>
</svg>
:::

Les couleurs rappellent les bases : en face de A, U ; en face de T, A ; en face de G, C ; en face de C, G. Trois bases du brin transcrit donnent un codon.

::: exemple Transcrire un brin (données d'illustration)
Brin transcrit : ACGTTCCTGATG.

1. **Repérer le modèle.** C'est le brin donné : l'ARNm se construit en face de lui. *Pourquoi : l'ARN polymérase s'appuie sur ce brin.*
2. **Apparier base par base.** A donne U, C donne G, G donne C, T donne A, T donne A, C donne G, C donne G, T donne A, G donne C, A donne U, T donne A, G donne C. *Pourquoi : complémentarité, et l'ARN n'a pas de thymine.*
3. **Écrire l'ARNm.** UGCAAGGACUAC.
4. **Grouper en codons.** UGC AAG GAC UAC : 12 bases, soit 4 codons. *Pourquoi : un codon est un groupe de 3 bases consécutives.*

:::

::: piege
**Erreur : recopier le brin transcrit en remplaçant seulement T par U.** « ACGTTC… devient ACGUUC… » tente parce que « U remplace T » est la seule différence retenue entre ADN et ARN. Mais l'ARNm est complémentaire du brin transcrit : UGCAAG… et non ACGUUC…
:::

::: propriete
**Transcription et gène.** La transcription se déroule dans le noyau ; l'ARNm est complémentaire du brin transcrit (donc identique à l'autre brin d'ADN, avec U à la place de T). On appelle **gène** la séquence de triplets de bases de l'ADN transcrite en codons d'ARNm et qui détermine la synthèse d'une protéine : dans ce programme, un gène, une protéine.
Cas limite : l'ARNm ne copie qu'une portion d'un seul brin, un gène, et non toute la molécule d'ADN.
:::

::: verifie À toi : un autre brin
Brin transcrit : TACGGATCA (donnée d'illustration). Écris l'ARNm et découpe-le en codons.

---

On apparie base par base : T donne A, A donne U, C donne G, G donne C, G donne C, A donne U, T donne A, C donne G, A donne U. L'ARNm est AUGCCUAGU, soit AUG CCU AGU : neuf bases, trois codons.
:::

::: retenir
La transcription copie, dans le noyau, un gène en ARNm par complémentarité avec le brin transcrit (A–U, T–A, G–C, C–G).
:::

## 🔠 Le code génétique : des codons aux acides aminés

L'ARNm s'écrit avec 4 sortes de bases, les protéines avec 20 sortes d'acides aminés.
Combien de bases faut-il pour désigner un seul acide aminé, et comment lit-on la correspondance ?

::: definition
**Code génétique** — correspondance entre les codons de l'ARNm et les acides aminés.
**Codon d'initiation** — AUG, qui désigne la méthionine ; la traduction commence à lui.
**Codons stop** — UAA, UAG et UGA : ils ne désignent aucun acide aminé et arrêtent la traduction.
:::

Le code génétique (tableau du manuel) : première lettre du codon en ligne, deuxième en colonne, troisième précisée dans la case.

| 1ʳᵉ lettre | 2ᵉ lettre U | 2ᵉ lettre C | 2ᵉ lettre A | 2ᵉ lettre G |
| --- | --- | --- | --- | --- |
| **U** | UUU, UUC : phénylalanine ; UUA, UUG : leucine | UCU, UCC, UCA, UCG : sérine | UAU, UAC : tyrosine ; UAA, UAG : stop | UGU, UGC : cystéine ; UGA : stop ; UGG : tryptophane |
| **C** | CUU, CUC, CUA, CUG : leucine | CCU, CCC, CCA, CCG : proline | CAU, CAC : histidine ; CAA, CAG : glutamine | CGU, CGC, CGA, CGG : arginine |
| **A** | AUU, AUC, AUA : isoleucine ; AUG : méthionine | ACU, ACC, ACA, ACG : thréonine | AAU, AAC : asparagine ; AAA, AAG : lysine | AGU, AGC : sérine ; AGA, AGG : arginine |
| **G** | GUU, GUC, GUA, GUG : valine | GCU, GCC, GCA, GCG : alanine | GAU, GAC : acide aspartique ; GAA, GAG : acide glutamique | GGU, GGC, GGA, GGG : glycine |

Par exemple, GAU se trouve ligne G, colonne A : acide aspartique.

::: exemple Compter les bases nécessaires, puis lire un ARNm
1. **Combien de bases par acide aminé ?** Une base : 4 possibilités, moins que 20. Deux bases : 4 × 4 = 16, encore moins que 20. Trois bases : 4 × 4 × 4 = 64, au moins 20. *Pourquoi : il faut au moins une combinaison par acide aminé : le codon est un triplet.*
2. **Découper l'ARNm.** AUG UGC GAU AGG GUA CCC GAU UAG, à partir de AUG. *Pourquoi : la lecture commence au codon d'initiation, et les triplets se suivent sans se chevaucher ; une lecture décalée d'une base donnerait d'autres codons, donc d'autres acides aminés.*
3. **Lire chaque codon dans le tableau.** AUG : Met ; UGC : Cys ; GAU : Asp ; AGG : Arg ; GUA : Val ; CCC : Pro ; GAU : Asp. *Pourquoi : la ligne donne la première lettre, la colonne la deuxième.*
4. **S'arrêter au stop.** UAG ne désigne aucun acide aminé : la lecture s'arrête. Le polypeptide est Met–Cys–Asp–Arg–Val–Pro–Asp, soit 7 acides aminés pour 8 codons. *Pourquoi : un codon stop commande la fin de la synthèse.*

:::

::: piege
**Erreur : croire qu'à chaque acide aminé correspond un seul codon.** « 20 acides aminés, donc 20 codons » tente parce qu'on associe un mot à un objet. Mais le code compte 64 codons : 61 désignent un acide aminé (la leucine en a 6) et 3 sont des codons stop. À l'inverse, dans le tableau, chaque codon n'a qu'une signification.
:::

> ⚠️ UAA est un codon stop, pas un codon d'initiation : la traduction commence à AUG.

> ⚠️ AUG n'est pas qu'un signal de départ : il est traduit, et le polypeptide commence par Met.

::: propriete
**Le code génétique.** Les codons sont des triplets : 64 codons, dont 61 pour les acides aminés et 3 stop. AUG, codon d'initiation, désigne la méthionine. Plusieurs codons désignent le même acide aminé (6 pour la leucine, la sérine et l'arginine) ; chaque codon n'a qu'une seule signification. Le code est utilisé par tous les êtres vivants.
Cas limite : la méthionine et le tryptophane n'ont qu'un codon chacun ; pour eux seuls, on retrouve le codon à partir de l'acide aminé.
:::

::: verifie À toi : un petit ARNm
Quel polypeptide l'ARNm AUGGAAGUUUAG fournit-il ?

---

On découpe : AUG GAA GUU UAG. Le tableau donne méthionine, acide glutamique, valine, puis UAG, codon stop. Le polypeptide est Met–Glu–Val : 3 acides aminés pour 4 codons.
:::

::: retenir
Le code génétique associe à chaque codon de l'ARNm (triplet) un acide aminé ou un arrêt : AUG initie la traduction, UAA, UAG et UGA l'arrêtent, et plusieurs codons peuvent désigner le même acide aminé.
:::

## 🧵 La traduction : construire le polypeptide

L'ARNm, sorti du noyau, arrive au ribosome ; les ARNt, chacun chargé de son acide aminé, attendent dans le cytoplasme.
Comment les acides aminés s'enchaînent-ils dans l'ordre exact fixé par les codons ?

::: definition
**Traduction** — synthèse d'un polypeptide à partir d'un ARNm, dans le cytoplasme, au niveau des ribosomes. Elle comprend trois phases : **initiation**, **élongation** et **terminaison**.
**Anticodon** — triplet de bases d'un ARNt, complémentaire d'un codon de l'ARNm.
**Site P** et **site A** — les deux emplacements du ribosome où se fixent les ARNt.
**Translocation** — déplacement du ribosome d'un codon à l'autre sur l'ARNm.
:::

::: figure Élongation : le ribosome lit AUG et UGC ; les ARNt de la méthionine (anticodon UAC) et de la cystéine (anticodon ACG) occupent les sites P et A, et une liaison peptidique relie leurs acides aminés
<svg viewBox="0 0 480 290">
<title>Élongation : le ribosome lit AUG et UGC ; les ARNt de méthionine (anticodon UAC) et de cystéine (anticodon ACG) sont sur les sites P et A, une liaison peptidique relie leurs acides aminés</title>
<rect x="46" y="58" width="190" height="104" rx="20" fill="#e0f2fe" stroke="#0f172a" stroke-width="1.8"/>
<rect x="46" y="166" width="190" height="34" rx="14" fill="#bae6fd" stroke="#0f172a" stroke-width="1.8"/>
<text x="95" y="78" text-anchor="middle" font-size="11" font-weight="600" fill="#0f172a">site P</text>
<text x="185" y="78" text-anchor="middle" font-size="11" font-weight="600" fill="#0f172a">site A</text>
<polygon points="82,108 108,108 138,204 52,204" fill="#fef3c7" stroke="#0f172a" stroke-width="1.6"/>
<circle cx="95" cy="94" r="15" fill="#c4b5fd" stroke="#0f172a" stroke-width="1.6"/>
<text x="95" y="98" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a">Met</text>
<rect x="53" y="204" width="24" height="24" rx="4" fill="#fed7aa" stroke="#0f172a" stroke-width="1.4"/>
<text x="65" y="221" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a">U</text>
<rect x="83" y="204" width="24" height="24" rx="4" fill="#fde68a" stroke="#0f172a" stroke-width="1.4"/>
<text x="95" y="221" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a">A</text>
<rect x="113" y="204" width="24" height="24" rx="4" fill="#fecaca" stroke="#0f172a" stroke-width="1.4"/>
<text x="125" y="221" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a">C</text>
<polygon points="172,108 198,108 228,204 142,204" fill="#fef3c7" stroke="#0f172a" stroke-width="1.6"/>
<circle cx="185" cy="94" r="15" fill="#c4b5fd" stroke="#0f172a" stroke-width="1.6"/>
<text x="185" y="98" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a">Cys</text>
<rect x="143" y="204" width="24" height="24" rx="4" fill="#fde68a" stroke="#0f172a" stroke-width="1.4"/>
<text x="155" y="221" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a">A</text>
<rect x="173" y="204" width="24" height="24" rx="4" fill="#fecaca" stroke="#0f172a" stroke-width="1.4"/>
<text x="185" y="221" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a">C</text>
<rect x="203" y="204" width="24" height="24" rx="4" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.4"/>
<text x="215" y="221" text-anchor="middle" font-size="13" font-weight="700" fill="#0f172a">G</text>
<line x1="110" y1="94" x2="170" y2="94" stroke="#0f6e56" stroke-width="5"/>
<text x="140" y="38" text-anchor="middle" font-size="11" font-weight="600" fill="#0f6e56">liaison peptidique</text>
<line x1="140" y1="43" x2="140" y2="90" stroke="#0f6e56" stroke-width="1.5" stroke-dasharray="4 3"/>
<rect x="50" y="244" width="30" height="28" fill="#fde68a" stroke="#0f172a" stroke-width="1.2"/>
<text x="65" y="264" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">A</text>
<rect x="80" y="244" width="30" height="28" fill="#fed7aa" stroke="#0f172a" stroke-width="1.2"/>
<text x="95" y="264" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">U</text>
<rect x="110" y="244" width="30" height="28" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.2"/>
<text x="125" y="264" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">G</text>
<rect x="140" y="244" width="30" height="28" fill="#fed7aa" stroke="#0f172a" stroke-width="1.2"/>
<text x="155" y="264" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">U</text>
<rect x="170" y="244" width="30" height="28" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.2"/>
<text x="185" y="264" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">G</text>
<rect x="200" y="244" width="30" height="28" fill="#fecaca" stroke="#0f172a" stroke-width="1.2"/>
<text x="215" y="264" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">C</text>
<line x1="140" y1="240" x2="140" y2="276" stroke="#0f172a" stroke-width="2.4"/>
<rect x="230" y="244" width="30" height="28" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.2"/>
<text x="245" y="264" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">G</text>
<rect x="260" y="244" width="30" height="28" fill="#fde68a" stroke="#0f172a" stroke-width="1.2"/>
<text x="275" y="264" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">A</text>
<rect x="290" y="244" width="30" height="28" fill="#fed7aa" stroke="#0f172a" stroke-width="1.2"/>
<text x="305" y="264" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">U</text>
<line x1="230" y1="240" x2="230" y2="276" stroke="#0f172a" stroke-width="2.4"/>
<rect x="320" y="244" width="30" height="28" fill="#fde68a" stroke="#0f172a" stroke-width="1.2"/>
<text x="335" y="264" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">A</text>
<rect x="350" y="244" width="30" height="28" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.2"/>
<text x="365" y="264" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">G</text>
<rect x="380" y="244" width="30" height="28" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.2"/>
<text x="395" y="264" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">G</text>
<line x1="320" y1="240" x2="320" y2="276" stroke="#0f172a" stroke-width="2.4"/>
<line x1="65" y1="230" x2="65" y2="243" stroke="#64748b" stroke-width="1.4" stroke-dasharray="3 2"/>
<line x1="95" y1="230" x2="95" y2="243" stroke="#64748b" stroke-width="1.4" stroke-dasharray="3 2"/>
<line x1="125" y1="230" x2="125" y2="243" stroke="#64748b" stroke-width="1.4" stroke-dasharray="3 2"/>
<line x1="155" y1="230" x2="155" y2="243" stroke="#64748b" stroke-width="1.4" stroke-dasharray="3 2"/>
<line x1="185" y1="230" x2="185" y2="243" stroke="#64748b" stroke-width="1.4" stroke-dasharray="3 2"/>
<line x1="215" y1="230" x2="215" y2="243" stroke="#64748b" stroke-width="1.4" stroke-dasharray="3 2"/>
<text x="420" y="264" text-anchor="start" font-size="12" font-weight="700" fill="#0f6e56">ARNm</text>
<text x="246" y="100" text-anchor="start" font-size="11" font-weight="600" fill="#0f172a">grande sous-unité</text>
<text x="246" y="187" text-anchor="start" font-size="11" font-weight="600" fill="#0f172a">petite sous-unité</text>
</svg>
:::

Chaque lettre de l'anticodon est complémentaire de la lettre du codon placée sous elle : UAC lit AUG, ACG lit UGC.

::: exemple Suivre la traduction d'un ARNm
ARNm : AUG UGC GAU AGG GUA CCC GAU UAG.

1. **Initiation.** La petite sous-unité se place sur l'ARNm au niveau de AUG ; l'ARNt d'anticodon UAC, chargé de méthionine, se fixe sur le site P ; la grande sous-unité s'associe. *Pourquoi : UAC est complémentaire de AUG, et la traduction commence au codon d'initiation.*
2. **Premier tour d'élongation.** Le codon UGC appelle l'ARNt d'anticodon ACG, chargé de cystéine, qui se fixe sur le site A ; une liaison peptidique relie la méthionine à la cystéine ; l'ARNt du site P est libéré ; le ribosome avance d'un codon. *Pourquoi : l'anticodon doit être complémentaire du codon, ce qui impose l'acide aminé.*
3. **Tours suivants.** Même enchaînement pour GAU, AGG, GUA, CCC, GAU (ARNt d'anticodons CUA, UCC, CAU, GGG, CUA) : la chaîne devient Met–Cys–Asp–Arg–Val–Pro–Asp. *Pourquoi : chaque tour ajoute un acide aminé, dans l'ordre des codons.*
4. **Terminaison.** Le ribosome atteint UAG, codon stop ; les deux sous-unités se séparent et le polypeptide de 7 acides aminés (6 liaisons peptidiques) est libéré. *Pourquoi : un codon stop ne désigne aucun acide aminé, il commande l'arrêt.*

:::

::: piege
**Erreur : croire que l'anticodon est identique au codon.** « Le codon AUG appelle un ARNt d'anticodon AUG » tente parce qu'on pense « lecture = même écriture ». Mais l'anticodon est complémentaire du codon : AUG est lu par UAC.
:::

> ⚠️ Le codon stop ne désigne aucun acide aminé : un polypeptide de n acides aminés correspond à n codons lus plus un codon stop, et les bases situées après le premier codon stop ne sont pas traduites.

::: propriete
**La traduction.** Trois phases : initiation (sur AUG, ARNt de méthionine sur le site P), élongation (appel d'un ARNt par complémentarité codon–anticodon, liaison peptidique grâce à l'énergie, translocation, puis répétition) et terminaison (codon stop, dissociation, libération). Le polypeptide se replie ensuite en protéine fonctionnelle. La chaîne complète : gène, ARNm, polypeptide, protéine, phénotype.
Cas limite : pour un polypeptide de n acides aminés, il faut un ARNm d'au moins 3 × (n + 1) bases, codon stop compris.
:::

::: verifie À toi : de la protéine à l'ARNm
Un polypeptide compte 9 acides aminés. Combien de codons, codon stop compris, l'ARNm doit-il comporter au minimum, et donc combien de bases ?

---

9 codons pour les 9 acides aminés, plus 1 codon stop : 10 codons. Chaque codon comptant 3 bases, l'ARNm compte au moins 10 × 3 = 30 bases.
:::

::: retenir
La traduction se fait au ribosome en trois phases : l'ARNt dont l'anticodon est complémentaire du codon apporte son acide aminé, une liaison peptidique l'ajoute à la chaîne, et un codon stop met fin à la synthèse.
:::

> 🏆 Chapitre franchi, héros : tu sais comment un gène devient une protéine, de la transcription dans le noyau à la traduction au ribosome. Prochaine quête : comment on manipule cette information en génie génétique.
