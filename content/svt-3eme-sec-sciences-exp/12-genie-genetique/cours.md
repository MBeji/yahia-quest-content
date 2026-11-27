# 🧪 Le génie génétique — faire fabriquer une protéine par la cellule d'un autre

> 💡 «Longtemps, pour soigner un enfant trop petit, on a prélevé l'hormone de croissance dans l'hypophyse de personnes décédées. Aujourd'hui, ce sont des bactéries qui la fabriquent : quelqu'un leur a donné le bon gène.»

Huit notions pour comprendre comment : ce qu'est le génie génétique et ce qu'il apporte, les cinq étapes du transfert d'un gène, l'obtention du gène, son repérage par une sonde, sa greffe dans un plasmide, le repérage des bactéries transformées, leur multiplication, enfin l'expression du gène et la récolte de la protéine. On suppose acquis qu'un gène s'exprime en deux temps, transcription en ARNm puis traduction en protéine, et qu'une cellule se divise en deux cellules identiques.

## 🧬 Le génie génétique : ce qu'il permet et ce qu'il risque

Un enfant dont l'hypophyse fabrique trop peu d'hormone de croissance reste de petite taille. On lui injectait l'hormone extraite d'hypophyses humaines prélevées après le décès : ces extraits, parfois mal purifiés, pouvaient transmettre des virus, et l'hormone d'un animal ne convient pas.
Comment obtenir l'hormone humaine sans prélever d'organe humain ?

::: definition
**Génie génétique** — ensemble des techniques de manipulation des gènes et de leur transfert dans un autre organisme (bactérie, levure, plante, animal).
**OGM** (organisme génétiquement modifié, ou organisme transgénique) — organisme dont l'ADN a reçu un gène étranger, introduit au laboratoire. Il acquiert un caractère nouveau, que ses descendants héritent aussi.
:::

| Organisme transformé       | Gène étranger introduit                  | Protéine fabriquée ou caractère obtenu                    |
| -------------------------- | ---------------------------------------- | --------------------------------------------------------- |
| Colibacille                | gène humain de l'insuline (depuis 1979)  | insuline humaine pour les diabétiques insulino-dépendants |
| Colibacille                | gène humain de l'hormone de croissance   | hormone de croissance humaine, sans extrait d'hypophyse          |
| Levure                     | gène de protéines de surface du virus de l'hépatite B | protéines servant à fabriquer un vaccin      |
| Tabac                      | gène de la bactérie Bacillus thuringiensis | protéine toxique pour les larves d'insectes             |
| Tomate, tabac, pomme de terre | gène de résistance à l'herbicide BASTA | enzyme qui dégrade l'herbicide : plants résistants        |

Dans les deux premières lignes, le schéma est le même : un gène humain placé dans une bactérie, qui fabrique la protéine humaine (données du manuel).

::: exemple Reconnaître un OGM sur un cas

1. Repérer le gène étranger : pour le tabac, c'est le gène d'une bactérie, Bacillus thuringiensis. Un OGM est défini par un gène venu d'ailleurs.
2. Repérer le caractère nouveau : le tabac fabrique une protéine toxique pour les insectes. Un gène inséré se traduit par un caractère.
3. Comparer avec le témoin : le tabac naturel est ravagé par les larves, le tabac transgénique y résiste. La différence vient du gène ajouté.
4. Conclure : le tabac transgénique est un OGM, car son ADN a reçu un gène étranger, introduit au laboratoire.

:::

::: piege
**Erreur : prendre un OGM pour une race obtenue par croisements.** « L'Homme a choisi les plants aux caractères voulus, c'est un OGM » tente parce que, dans les deux cas, l'Homme modifie une lignée. Mais en sélectionnant, il trie des caractères qui existent déjà dans l'espèce (le maïs sélectionné à partir de la téosinte) ; pour un OGM, il fait entrer dans l'ADN un gène qui vient d'un autre organisme.
:::

::: propriete
**Objectifs et débat.** Le génie génétique vise à identifier le génome d'une espèce, à comprendre le fonctionnement de gènes, à produire en quantité industrielle une substance utile (insuline, hormone de croissance, vaccins), et à conférer un caractère nouveau à une plante ou à un animal.
Les OGM divisent : certains y voient un progrès médical, agricole et écologique ; d'autres craignent la propagation non contrôlée des gènes manipulés. Risques cités : un gène de résistance à un antibiotique, associé au gène utile, pourrait passer à l'animal ou à l'Homme ; un gène de résistance à un herbicide pourrait passer à des « mauvaises » plantes ; pour le consommateur, le principal risque évoqué est l'allergie à la protéine fabriquée, pas une modification de son propre ADN.
Cas limite : on peut aussi introduire un gène normal dans des cellules d'un malade pour le soigner. En 1990, des lymphocytes d'une fillette privée du gène de l'enzyme ADA ont été cultivés, ont reçu le gène normal, puis ont été réinjectés : c'est la thérapie génique.
:::

::: verifie À toi : la présure
Des chercheurs introduisent dans des levures le gène de la présure du veau, enzyme qui fait cailler le lait. Les levures transformées fabriquent la présure, et leurs descendantes aussi. Ces levures sont-elles des OGM ?

---

Oui : leur ADN a reçu un gène étranger, celui du veau, introduit au laboratoire, et il leur donne un caractère nouveau, la synthèse de présure, que leurs descendantes héritent.
:::

::: retenir
Le génie génétique manipule les gènes ; un OGM est un organisme dont l'ADN a reçu un gène étranger, utile en médecine et en agriculture mais discuté pour ses risques.
:::

## 🗺️ Les cinq étapes : du gène à la protéine récoltée

Pour que des bactéries fabriquent l'hormone de croissance humaine, plusieurs opérations s'enchaînent.
Si on commençait par la bactérie, que lui mettrait-on dedans ? Par quoi faut-il donc commencer, et comment savoir que le transfert a réussi ?

::: definition
**Cellule hôte** — cellule qui reçoit le gène étranger (ici un colibacille, bactérie *Escherichia coli*).
**Vecteur** — molécule d'ADN, le plus souvent un plasmide, qui transporte le gène jusque dans la cellule hôte.
**ADN recombiné** — ADN du vecteur dans lequel le gène étranger a été inséré.
:::

::: figure Les cinq étapes du transfert d'un gène, dans l'ordre : du gène à la protéine
<svg viewBox="0 0 340 270">
<title>Cinq étapes numérotées : obtenir le gène, l'introduire dans une bactérie, repérer les bactéries transformées, cloner et exprimer le gène, extraire la protéine</title>
<g font-size="14" font-weight="700" fill="#0f172a">
<rect x="20" y="8" width="300" height="38" rx="8" fill="#bbf7d0" stroke="#0f172a" stroke-width="1.8"/>
<text x="170" y="32" text-anchor="middle">1 · Obtenir le gène</text>
<rect x="20" y="62" width="300" height="38" rx="8" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.8"/>
<text x="170" y="86" text-anchor="middle">2 · L'introduire dans une bactérie</text>
<rect x="20" y="116" width="300" height="38" rx="8" fill="#fde68a" stroke="#0f172a" stroke-width="1.8"/>
<text x="170" y="140" text-anchor="middle">3 · Repérer les bactéries transformées</text>
<rect x="20" y="170" width="300" height="38" rx="8" fill="#fecaca" stroke="#0f172a" stroke-width="1.8"/>
<text x="170" y="194" text-anchor="middle">4 · Cloner et exprimer le gène</text>
<rect x="20" y="224" width="300" height="38" rx="8" fill="#e9d5ff" stroke="#0f172a" stroke-width="1.8"/>
<text x="170" y="248" text-anchor="middle">5 · Extraire la protéine</text>
</g>
<g fill="#0f172a">
<path d="M160 47 L180 47 L170 60 Z"/>
<path d="M160 101 L180 101 L170 114 Z"/>
<path d="M160 155 L180 155 L170 168 Z"/>
<path d="M160 209 L180 209 L170 222 Z"/>
</g>
</svg>
:::

Chaque flèche relie une étape à celle qui la suit : l'étape 3 vérifie ce que l'étape 2 vient de faire, l'étape 5 récolte ce que l'étape 4 a fait produire.

::: exemple Suivre l'hormone de croissance

1. Étape 1 : on prélève l'ARNm de l'hormone dans des cellules de l'hypophyse humaine et on en fabrique une copie d'ADN, le gène (ADNc). Il faut le gène en main avant tout.
2. Étape 2 : on greffe cette copie dans un plasmide, qui entre dans des colibacilles. Le gène a besoin d'un vecteur pour traverser jusqu'à la cellule hôte.
3. Étape 3 : on repère les colibacilles qui ont capté le plasmide. Toutes ne l'ont pas fait, et seules les transformées serviront.
4. Étape 4 : on cultive les bactéries repérées : elles se multiplient et fabriquent l'hormone. Cultiver des bactéries non transformées ne produirait rien.
5. Étape 5 : on fait sortir l'hormone des bactéries et on la récolte, car les colibacilles ne la sécrètent pas.

:::

::: piege
**Erreur : changer l'ordre des étapes.** « On repère d'abord les bactéries transformées, ensuite on leur donne le gène » tente parce que « repérer » semble une préparation. Mais on ne peut repérer que ce qui a déjà été fait : il faut d'abord introduire le gène. On repère ensuite, pour ne multiplier que les bonnes bactéries, avant de récolter la protéine.
:::

::: propriete
**Ordre fixe.** Obtenir le gène, l'introduire dans une cellule hôte, repérer les cellules transformées, les cloner et faire exprimer le gène, extraire la protéine.
Cas limite : la cellule hôte peut être une levure plutôt qu'une bactérie (vaccin contre l'hépatite B) ; les étapes gardent le même ordre.
:::

::: verifie À toi : un ordre à justifier
Dans la figure, l'étape « Repérer les bactéries transformées » arrive juste avant « Cloner et exprimer le gène ». Pourquoi ne peut-on pas échanger ces deux étapes ?

---

Si on clonait avant de repérer, on multiplierait aussi les bactéries qui n'ont pas reçu le gène. On repère d'abord, pour ne cloner que les bactéries transformées.
:::

::: retenir
Les cinq étapes, dans cet ordre : obtenir le gène, l'introduire dans une bactérie, repérer les bactéries transformées, les cloner et exprimer le gène, extraire la protéine.
:::

## ✂️ Obtenir le gène : deux voies

Un chromosome humain porte des centaines à des milliers de gènes alignés le long d'une seule molécule d'ADN. Celui de l'hormone de croissance n'en est qu'une petite portion.
Comment obtenir ce gène seul, prêt à être transféré ?

::: definition
**Enzyme de restriction** (endonucléase) — enzyme d'origine bactérienne qui coupe l'ADN à des séquences précises, ses sites de coupure.
**Transcriptase reverse** — enzyme d'origine virale qui fabrique un brin d'**ADN** à partir d'un brin d'**ARNm**.
**ADNc** — ADN copie : copie en ADN d'un ARNm, d'abord simple brin, puis complétée en double brin.
:::

::: figure Deux voies pour obtenir le gène : couper l'ADN et repérer le gène, ou copier l'ARNm en ADNc
<svg viewBox="0 0 380 250">
<title>Deux voies : ADN coupé par des enzymes de restriction puis gène repéré par une sonde ; ARNm copié en ADNc simple brin puis double brin par la transcriptase reverse</title>
<text x="10" y="22" font-size="13" font-weight="700" fill="#0f172a">Voie 1 : à partir de l'ADN</text>
<g font-size="11" fill="#0f172a" font-weight="700" text-anchor="middle">
<rect x="10" y="32" width="110" height="62" rx="8" fill="#bbf7d0" stroke="#0f172a" stroke-width="1.8"/>
<text x="65" y="56">ADN extrait</text><text x="65" y="72">des cellules</text>
<rect x="140" y="32" width="110" height="62" rx="8" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.8"/>
<text x="195" y="52">coupé par les</text><text x="195" y="67">enzymes de</text><text x="195" y="82">restriction</text>
<rect x="270" y="32" width="100" height="62" rx="8" fill="#fde68a" stroke="#0f172a" stroke-width="1.8"/>
<text x="320" y="56">gène repéré</text><text x="320" y="72">par une sonde</text>
</g>
<text x="10" y="138" font-size="13" font-weight="700" fill="#0f172a">Voie 2 : à partir de l'ARNm</text>
<g font-size="11" fill="#0f172a" font-weight="700" text-anchor="middle">
<rect x="10" y="148" width="110" height="62" rx="8" fill="#bbf7d0" stroke="#0f172a" stroke-width="1.8"/>
<text x="65" y="172">ARNm de la</text><text x="65" y="188">protéine visée</text>
<rect x="140" y="148" width="110" height="62" rx="8" fill="#fecaca" stroke="#0f172a" stroke-width="1.8"/>
<text x="195" y="168">copié en ADNc</text><text x="195" y="183">simple brin par la</text><text x="195" y="198">transcriptase reverse</text>
<rect x="270" y="148" width="100" height="62" rx="8" fill="#fde68a" stroke="#0f172a" stroke-width="1.8"/>
<text x="320" y="172">ADNc</text><text x="320" y="188">double brin</text>
</g>
<g fill="#0f172a">
<path d="M122 55 L138 63 L122 71 Z"/>
<path d="M252 55 L268 63 L252 71 Z"/>
<path d="M122 171 L138 179 L122 187 Z"/>
<path d="M252 171 L268 179 L252 187 Z"/>
</g>
</svg>
:::

Les deux lignes mènent à un gène prêt à être transféré. La voie 1 repose sur la coupe (cette notion) et le repérage par une sonde (notion suivante) ; la voie 2 repose sur la transcriptase reverse.

::: exemple Copier l'ARNm de l'hormone de croissance

1. Choisir les cellules : on prélève l'ARNm de l'hormone dans des cellules de l'hypophyse humaine, car ce sont elles qui fabriquent cette hormone.
2. Copier l'ARNm en ADN : la transcriptase reverse lit l'ARNm et fabrique un brin d'ADN complémentaire. Son nom dit « reverse » : elle fait l'inverse de la transcription, de l'ARN vers l'ADN.
3. Compléter : le brin d'ADN est complété en ADNc double brin, une molécule d'ADN comme les autres.
4. Conclure : l'ADNc est une copie du gène de l'hormone, prête à être greffée.

:::

::: piege
**Erreur : croire que la transcriptase reverse fabrique de l'ARN à partir de l'ADN.** Cette idée tente parce que son nom ressemble à celui de la transcription, qui va de l'ADN à l'ARNm. Mais « reverse » signifie inverse : elle lit l'ARNm et fabrique de l'ADN.
:::

::: propriete
**Deux voies.** Voie 1 : extraire l'ADN, le fragmenter avec des enzymes de restriction, repérer le gène avec une sonde. Voie 2 : prélever l'ARNm de la protéine visée et le copier en ADNc avec la transcriptase reverse.
Cas limite : l'ADN d'une cellule contient tous les gènes, mais l'ARNm d'une protéine n'existe que dans les cellules qui l'expriment : pour l'hormone de croissance, il faut des cellules de l'hypophyse.
:::

::: verifie À toi : l'insuline
On dispose de l'ARNm de l'insuline. Quelle enzyme permet d'en obtenir une copie d'ADN, et quelle molécule cette enzyme lit-elle ?

---

La transcriptase reverse : elle lit l'ARNm et fabrique un brin d'ADN complémentaire, qu'on complète en ADNc double brin.
:::

::: retenir
On obtient un gène soit en coupant l'ADN avec des enzymes de restriction puis en repérant le gène, soit en copiant l'ARNm en ADNc avec la transcriptase reverse.
:::

## 🎣 Repérer un gène avec une sonde radioactive

Après la coupe par les enzymes de restriction, l'ADN d'une cellule est en milliers de fragments mélangés, et un seul porte le gène cherché. On compare souvent la méthode à une pêche à l'hameçon : on jette un appât dans le mélange.
Comment retrouver le bon fragment parmi tous les autres ?

::: definition
**Sonde moléculaire radioactive** — séquence de nucléotides marquée radioactivement, complémentaire du gène recherché.
**Hybridation** — fixation de la sonde sur la séquence qui lui est complémentaire, par complémentarité des bases.
**Électrophorèse** — séparation des fragments d'ADN dans un champ électrique, sur un gel d'agarose, selon leur taille.
**Autoradiographie** — image qui montre où se trouve la radioactivité, donc où la sonde s'est fixée.
:::

::: figure Données d'illustration : gel après électrophorèse (à gauche) et autoradiographie (à droite), pistes T+ (témoin positif), éch. (échantillon) et T− (témoin négatif) ; ligne verte pointillée au niveau du signal
<svg viewBox="0 0 340 250">
<title>Gel avec trois pistes et autoradiographie : un signal à la même hauteur dans le témoin positif et l'échantillon, aucun dans le témoin négatif</title>
<g font-size="12" font-weight="700" fill="#0f172a" text-anchor="middle">
<text x="50" y="32">T+</text><text x="90" y="32">éch.</text><text x="130" y="32">T−</text>
<text x="220" y="32">T+</text><text x="260" y="32">éch.</text><text x="300" y="32">T−</text>
</g>
<rect x="30" y="40" width="120" height="170" fill="#e2e8f0" stroke="#0f172a" stroke-width="1.8"/>
<g fill="#94a3b8">
<rect x="40" y="40" width="20" height="6"/><rect x="80" y="40" width="20" height="6"/><rect x="120" y="40" width="20" height="6"/>
</g>
<g fill="#475569">
<rect x="38" y="80" width="24" height="5"/><rect x="38" y="120" width="24" height="5"/><rect x="38" y="160" width="24" height="5"/>
<rect x="78" y="80" width="24" height="5"/><rect x="78" y="100" width="24" height="5"/><rect x="78" y="120" width="24" height="5"/><rect x="78" y="160" width="24" height="5"/>
<rect x="118" y="90" width="24" height="5"/><rect x="118" y="110" width="24" height="5"/><rect x="118" y="140" width="24" height="5"/>
</g>
<rect x="200" y="40" width="120" height="170" fill="#0f172a" stroke="#0f172a" stroke-width="1.8"/>
<g fill="#fde047">
<ellipse cx="220" cy="122" rx="12" ry="4"/><ellipse cx="260" cy="122" rx="12" ry="4"/>
</g>
<path d="M30 122 L320 122" fill="none" stroke="#0f6e56" stroke-width="1.5" stroke-dasharray="4 3"/>
<g font-size="11" font-weight="700" fill="#0f172a" text-anchor="middle">
<text x="90" y="230">Après électrophorèse</text>
<text x="260" y="230">Autoradiographie</text>
</g>
</svg>
:::

Dans la figure, chaque bande du gel est un groupe de fragments de même taille ; chaque tache jaune de l'autoradiographie est un endroit où la sonde s'est fixée.

::: exemple Lire une autoradiographie

1. Vérifier le témoin positif, qui contient le gène : il donne un signal, donc la sonde fonctionne.
2. Vérifier le témoin négatif, qui ne contient pas le gène : il ne donne aucun signal, donc la sonde ne se fixe pas au hasard.
3. Lire l'échantillon : un signal apparaît à la même hauteur que celui du témoin positif. Les fragments de cette bande ont la même taille et se sont hybridés avec la sonde : ils portent le gène.
4. Conclure : l'échantillon contient le gène, dans la bande marquée. Les autres bandes de l'échantillon, sans signal, ne portent pas le gène : la sonde ne se fixe pas sur tous les fragments.

:::

::: piege
**Erreur : croire que la sonde se fixe sur tous les fragments d'ADN.** « Toutes les bandes de l'échantillon portent le gène » tente parce que toutes les bandes sont visibles sur le gel. Mais le gel montre tous les fragments, alors que l'autoradiographie ne montre que ceux qui se sont hybridés : la sonde ne se fixe que sur la séquence complémentaire du gène.
:::

::: propriete
**La méthode en cinq temps.** Fragmenter l'ADN avec des enzymes de restriction, séparer les fragments par électrophorèse, séparer les deux brins (dénaturation) et les transférer sur un filtre de nitrocellulose, hybrider avec la sonde, révéler par autoradiographie.
Cas limite : si le témoin positif ne donne aucun signal, l'expérience n'est pas valable : la sonde n'a pas fonctionné, et l'absence de signal dans l'échantillon ne prouve pas l'absence du gène.
:::

::: verifie À toi : un témoin muet
Sur une autre autoradiographie, le témoin positif et l'échantillon ne montrent aucun signal. Peut-on conclure que l'échantillon ne contient pas le gène ?

---

Non : le témoin positif contient le gène mais ne donne aucun signal, donc la sonde n'a pas fonctionné et l'expérience n'est pas valable.
:::

::: retenir
Une sonde radioactive complémentaire du gène se fixe uniquement sur lui ; l'autoradiographie le révèle, et les témoins positif et négatif valident l'expérience.
:::

## 🧷 Greffer le gène : enzymes de restriction, ligase et plasmide

On tient maintenant un gène. Mais une bactérie ne fabrique la protéine que si le gène entre dans son ADN. Le colibacille porte, en plus de son chromosome, de petits anneaux d'ADN dans son cytoplasme.
Comment y accrocher le gène, et par quelle porte l'y faire entrer ?

::: definition
**Plasmide** — petite molécule d'ADN circulaire, située dans le cytoplasme d'une bactérie, en plus du chromosome. Il sert de vecteur.
**ADN ligase** — enzyme qui soude deux fragments d'ADN : la « colle » moléculaire.
**Plasmide recombiné** — plasmide dans lequel le gène étranger a été soudé.
Une enzyme de restriction joue le rôle de « ciseaux » moléculaires.
:::

::: figure Le plasmide ouvert et le gène (vert) ont des extrémités complémentaires, AATT en face de TTAA ; l'ADN ligase les soude et donne le plasmide recombiné
<svg viewBox="0 0 340 190">
<title>Plasmide ouvert avec un gène aux extrémités complémentaires, puis plasmide recombiné refermé par l'ADN ligase</title>
<path d="M85.39 67.71 A45 45 0 1 1 54.61 67.71" fill="none" stroke="#0f172a" stroke-width="3"/>
<rect x="30" y="12" width="80" height="14" rx="4" fill="#0f6e56" stroke="#0f172a" stroke-width="1.5"/>
<g font-size="10" font-weight="700" fill="#ffffff" text-anchor="middle">
<text x="50" y="23">TTAA</text><text x="90" y="23">AATT</text>
</g>
<g font-size="10" font-weight="700" fill="#0f172a" text-anchor="middle">
<text x="30" y="64">AATT</text><text x="110" y="64">TTAA</text>
</g>
<text x="170" y="104" font-size="12" font-weight="700" fill="#0f172a" text-anchor="middle">ADN ligase</text>
<path d="M138 112 L202 112" fill="none" stroke="#0f172a" stroke-width="2"/>
<path d="M200 105 L212 112 L200 119 Z" fill="#0f172a"/>
<circle cx="270" cy="110" r="45" fill="none" stroke="#0f172a" stroke-width="3"/>
<path d="M254.61 67.71 A45 45 0 0 1 285.39 67.71" fill="none" stroke="#0f6e56" stroke-width="7"/>
<g font-size="12" font-weight="700" fill="#0f172a" text-anchor="middle">
<text x="70" y="178">plasmide ouvert + gène</text>
<text x="270" y="178">plasmide recombiné</text>
</g>
</svg>
:::

Dans la figure, le segment vert est le gène à greffer : ses extrémités se placent en face de celles du plasmide ouvert, puis la ligase les relie.

::: exemple Construire un plasmide recombiné

1. Couper le plasmide avec une enzyme de restriction : il s'ouvre en deux extrémités, AATT d'un côté et TTAA de l'autre. Le plasmide doit être ouvert pour recevoir quelque chose.
2. Couper le gène avec la même enzyme : ses extrémités sont complémentaires de celles du plasmide, AATT en face de TTAA (A avec T, T avec A).
3. Mélanger : les extrémités complémentaires se rapprochent et se maintiennent l'une contre l'autre.
4. Souder avec l'ADN ligase : le plasmide se referme, gène compris. C'est le plasmide recombiné.
5. Mélanger les plasmides recombinés aux colibacilles dans un milieu de culture : certaines bactéries captent spontanément un plasmide et sont transformées.

:::

::: piege
**Erreur : croire qu'on peut ouvrir le plasmide avec n'importe quelle enzyme de restriction.** « Toutes les enzymes de restriction coupent, donc l'une vaut l'autre » tente parce que le rôle est le même. Mais chaque enzyme coupe à sa propre séquence et laisse ses propres extrémités : en général, une autre enzyme laisse d'autres extrémités, qui ne sont plus complémentaires, et le gène ne s'accroche pas. Il faut la même enzyme pour le gène et pour le plasmide.
:::

::: propriete
**Trois outils, trois gestes.** L'enzyme de restriction coupe l'ADN, l'ADN ligase le soude, le plasmide transporte le gène.
Cas limite : la ligase colle des molécules d'ADN, pas des bactéries ; et la bactérie qui reçoit le plasmide est la cellule hôte, le plasmide est le vecteur.
:::

::: verifie À toi : l'extrémité à trouver
Un plasmide ouvert porte à une extrémité la séquence AATT. Quelle séquence doit porter l'extrémité du gène placée en face, et pourquoi ?

---

TTAA : les extrémités doivent être complémentaires (A avec T, A avec T, T avec A, T avec A) pour que les deux molécules s'accrochent avant d'être soudées.
:::

::: retenir
Une même enzyme de restriction coupe le plasmide et le gène, qui se rejoignent par leurs extrémités complémentaires, puis l'ADN ligase les soude en plasmide recombiné.
:::

## 🧫 Repérer les colibacilles transformés

Après le mélange, certains colibacilles ont capté un plasmide recombiné et d'autres non. Au microscope comme à l'œil nu, elles se ressemblent toutes.
Comment les distinguer, pour ne garder que les transformées ?

::: definition
**Gène marqueur** — gène de résistance à un antibiotique, par exemple la streptomycine, associé au gène étranger sur le même plasmide recombiné.
**Bactérie transformée** — bactérie qui a capté un plasmide recombiné.
Les colibacilles naturels sont **sensibles** à la streptomycine : ils ne se développent pas en sa présence.
:::

::: figure Données d'illustration : la même suspension de bactéries étalée sur deux boîtes, sans antibiotique (à gauche) et avec streptomycine (à droite) ; chaque point jaune est une colonie
<svg viewBox="0 0 340 200">
<title>Deux boîtes de Petri : de nombreuses colonies sur le milieu nutritif seul, deux colonies sur le milieu avec streptomycine</title>
<circle cx="90" cy="95" r="62" fill="#fef9c3" stroke="#0f172a" stroke-width="2"/>
<circle cx="250" cy="95" r="62" fill="#fef9c3" stroke="#0f172a" stroke-width="2"/>
<g fill="#f59e0b" stroke="#92400e" stroke-width="1">
<circle cx="70" cy="68" r="5"/><circle cx="95" cy="58" r="5"/><circle cx="118" cy="78" r="5"/><circle cx="58" cy="92" r="5"/>
<circle cx="84" cy="86" r="5"/><circle cx="108" cy="102" r="5"/><circle cx="73" cy="115" r="5"/><circle cx="99" cy="126" r="5"/>
<circle cx="128" cy="98" r="5"/><circle cx="52" cy="72" r="5"/><circle cx="88" cy="108" r="5"/><circle cx="120" cy="120" r="5"/>
<circle cx="66" cy="132" r="5"/><circle cx="104" cy="76" r="5"/>
<circle cx="235" cy="85" r="5"/><circle cx="265" cy="112" r="5"/>
</g>
<g font-size="11" font-weight="700" fill="#0f172a" text-anchor="middle">
<text x="90" y="178">milieu nutritif seul</text>
<text x="250" y="178">milieu nutritif + streptomycine</text>
</g>
</svg>
:::

Dans la figure, la boîte de gauche montre toutes les bactéries vivantes ; celle de droite ne garde que celles qui résistent à la streptomycine.

::: exemple Exploiter les deux boîtes

1. Analyser : sans antibiotique, de nombreuses colonies se développent ; avec streptomycine, il n'en reste que deux.
2. Interpréter : les colibacilles naturels sont sensibles à la streptomycine et ne s'y développent pas. Les deux colonies de la boîte de droite résistent : elles portent le gène de résistance.
3. Relier au plasmide : ce gène est sur le plasmide recombiné, avec le gène étranger. Les bactéries qui résistent ont donc capté le plasmide.
4. Conclure : seules les deux colonies de la boîte de droite sont transformées. On les prélève pour la suite, et les autres bactéries sont écartées.

:::

::: piege
**Erreur : croire que l'antibiotique élimine les bactéries transformées.** « L'antibiotique tue les bactéries qui ont reçu le gène » tente parce qu'un antibiotique sert d'ordinaire à détruire des bactéries. Mais ici les bactéries transformées portent le gène de résistance : c'est l'antibiotique qui tue les bactéries non transformées, et les survivantes sont les transformées.
:::

::: propriete
**Le principe de la sélection.** On associe au gène utile un gène de résistance à un antibiotique, on cultive en présence de cet antibiotique : seules les bactéries transformées survivent.
Cas limite : la résistance prouve que le plasmide est entré dans la bactérie, pas que la protéine est déjà fabriquée ; une bactérie sans plasmide, ou avec un plasmide dépourvu de ce gène, reste sensible.
:::

::: verifie À toi : des bactéries sans plasmide
On étale sur un milieu avec streptomycine des colibacilles qui n'ont jamais reçu de plasmide. Combien de colonies attend-on, et pourquoi ?

---

Aucune : ces colibacilles sont sensibles à la streptomycine, car ils n'ont pas le gène de résistance, et ne se développent pas en sa présence.
:::

::: retenir
Un gène de résistance à un antibiotique, porté par le plasmide recombiné, permet de sélectionner les bactéries transformées : seules elles survivent à l'antibiotique.
:::

## 🔁 Cloner le gène : une bactérie, des milliards

Une seule bactérie transformée ne fabriquera jamais assez de protéine pour un traitement. Mais un colibacille se divise en deux environ toutes les 20 minutes quand les conditions sont bonnes.
Combien de bactéries descendent d'une seule en une heure, puis en une journée ?

::: definition
**Bipartition** — division d'une bactérie en deux cellules filles identiques.
**Clone** — ensemble d'individus génétiquement identiques issus d'un même individu. Les bactéries d'un clone portent toutes le plasmide recombiné, donc le gène greffé : c'est le **clonage** du gène.
:::

::: figure Données d'illustration : nombre de bactéries issues d'une seule, toutes les 20 minutes ; chaque barre double la précédente
<svg viewBox="0 0 340 240">
<title>Diagramme en barres : nombre de bactéries issues d'une seule bactérie, 1, 2, 4, 8, 16 puis 32 toutes les 20 minutes</title>
<path d="M50 200 L320 200 M50 200 L50 30" fill="none" stroke="#0f172a" stroke-width="2"/>
<g fill="#0f6e56" opacity="0.85" stroke="#0f172a" stroke-width="1">
<rect x="66" y="195" width="28" height="5"/><rect x="106" y="190" width="28" height="10"/><rect x="146" y="180" width="28" height="20"/>
<rect x="186" y="160" width="28" height="40"/><rect x="226" y="120" width="28" height="80"/><rect x="266" y="40" width="28" height="160"/>
</g>
<g font-size="11" font-weight="700" fill="#0f172a" text-anchor="middle">
<text x="80" y="190">1</text><text x="120" y="185">2</text><text x="160" y="175">4</text>
<text x="200" y="155">8</text><text x="240" y="115">16</text><text x="280" y="35">32</text>
<text x="80" y="216">0</text><text x="120" y="216">20</text><text x="160" y="216">40</text>
<text x="200" y="216">60</text><text x="240" y="216">80</text><text x="280" y="216">100</text>
<text x="185" y="233">temps (min)</text>
</g>
<g font-size="10" font-weight="700" fill="#0f172a" text-anchor="end">
<text x="44" y="204">0</text><text x="44" y="164">8</text><text x="44" y="124">16</text><text x="44" y="84">24</text><text x="44" y="44">32</text>
</g>
<text x="14" y="120" font-size="11" font-weight="700" fill="#0f172a" text-anchor="middle" transform="rotate(-90 14 120)">nombre de bactéries</text>
</svg>
:::

Sur la figure, la hauteur de la barre à 60 minutes est celle de 8 bactéries : trois doublements en une heure.

::: exemple Compter un clone

1. Compter les divisions : une heure compte trois fois 20 minutes, donc une journée de 24 h compte 24 × 3 = 72 divisions.
2. Compter les bactéries : chaque division double leur nombre, donc 72 divisions donnent 2⁷² ≈ 4,7 × 10²¹ bactéries à partir d'une seule. On multiplie par 2 à chaque fois, on n'ajoute pas 2.
3. Calculer la masse : une bactérie pèse environ 10⁻¹² g, donc 4,7 × 10²¹ × 10⁻¹² g = 4,7 × 10⁹ g, soit environ 4 700 tonnes.
4. Prolonger sur deux jours : 144 divisions donnent 2¹⁴⁴ ≈ 2,2 × 10⁴³ bactéries, soit environ 2,2 × 10²⁵ tonnes, près de 3 700 fois la masse de la Terre (6 × 10²¹ tonnes).
5. Conclure : ces chiffres supposent des conditions idéales, sans manque de nourriture, qui n'existent pas longtemps. Ils montrent pourquoi on choisit un colibacille : il se multiplie très vite.

:::

::: piege
**Erreur : compter les bactéries comme une somme, pas comme un doublement.** « Trois divisions donnent 3 bactéries, ou 6 » tente parce qu'on pense « une division, une bactérie de plus ». Mais chaque bactérie se divise : 1 devient 2, puis 4, puis 8. Le nombre est 2 puissance le nombre de divisions.
:::

::: propriete
**Clonage par bipartition.** Un clone issu d'une bactérie transformée compte 2ⁿ bactéries après n divisions, toutes porteuses du gène greffé. Le colibacille est choisi comme cellule hôte car il est facile à se procurer et à cultiver, et se multiplie vite ; c'est une cellule sans noyau véritable, mais qui possède ce qu'il faut pour fabriquer des protéines (chromosome, ribosomes).
Cas limite : une bactérie contient souvent plusieurs copies du plasmide, qui se répliquent avec elle.
:::

::: verifie À toi : quatre bactéries
On part de 4 bactéries transformées, qui se divisent toutes les 20 minutes. Combien y en a-t-il après une heure ?

---

Une heure compte 3 divisions : chaque bactérie est multipliée par 2 trois fois, soit par 8, donc 4 × 8 = 32 bactéries.
:::

::: retenir
La bipartition multiplie les bactéries par 2 à chaque division ; le clone qui en résulte porte partout le gène greffé, et le colibacille convient par sa multiplication rapide.
:::

## 🏭 Faire exprimer le gène et récolter la protéine

Le clone est prêt : des milliards de colibacilles portent le gène. Mais un gène étranger n'est pas lu automatiquement par une bactérie, et la protéine fabriquée n'est pas rejetée dans le milieu de culture.
Que faut-il autour du gène pour qu'il soit lu, et comment récupérer la protéine ?

::: definition
**Gène de structure** — gène qui code la protéine recherchée.
**Séquences régulatrices** — signaux d'ADN indispensables à son expression : le **promoteur**, placé avant le gène, et le **signal de fin de transcription**, placé après.
**Choc osmotique** — passage de la bactérie dans un milieu hypertonique, puis hypotonique, pour libérer la protéine.
**Lyse** — éclatement de la cellule.
:::

::: figure Le gène de structure est entouré de ses séquences régulatrices : le promoteur le précède, le signal de fin de transcription le suit
<svg viewBox="0 0 340 140">
<title>Segment d'ADN : promoteur, puis gène de structure, puis signal de fin de transcription, avec une flèche de lecture de gauche à droite</title>
<rect x="20" y="52" width="300" height="30" fill="#cbd5e1" stroke="#0f172a" stroke-width="1.8"/>
<rect x="60" y="52" width="60" height="30" fill="#bbf7d0" stroke="#0f172a" stroke-width="1.8"/>
<rect x="120" y="52" width="120" height="30" fill="#bfdbfe" stroke="#0f172a" stroke-width="1.8"/>
<rect x="240" y="52" width="50" height="30" fill="#fecaca" stroke="#0f172a" stroke-width="1.8"/>
<path d="M120 38 L286 38" fill="none" stroke="#0f172a" stroke-width="2"/>
<path d="M284 32 L296 38 L284 44 Z" fill="#0f172a"/>
<g font-size="11" font-weight="700" fill="#0f172a" text-anchor="middle">
<text x="90" y="100">promoteur</text>
<text x="180" y="100">gène de</text><text x="180" y="114">structure</text>
<text x="265" y="100">signal de fin</text><text x="265" y="114">de transcription</text>
<text x="203" y="30">lecture (transcription)</text>
</g>
</svg>
:::

Dans la figure, la transcription démarre juste après le promoteur (la flèche part de sa fin), traverse le gène de structure et s'arrête au signal de fin : c'est la portion d'ADN lue pour fabriquer l'ARNm. Le promoteur n'en fait pas partie : c'est le site où l'équipement de lecture se fixe.

::: figure Extraction par choc osmotique : l'hormone (points rouges) se trouve entre la membrane et la coque ; en milieu hypertonique la membrane se rétracte et agrandit cet espace ; en milieu hypotonique son contenu est libéré
<svg viewBox="0 0 340 200">
<title>Deux bactéries : en milieu hypertonique la membrane cytoplasmique est rétractée avec l'hormone entre la membrane et la coque, en milieu hypotonique la cellule est gonflée et l'hormone est à l'extérieur</title>
<g font-size="12" font-weight="700" fill="#0f172a" text-anchor="middle">
<text x="85" y="22">milieu hypertonique</text>
<text x="255" y="22">milieu hypotonique</text>
</g>
<ellipse cx="85" cy="95" rx="62" ry="40" fill="none" stroke="#0f172a" stroke-width="3" stroke-dasharray="14 6"/>
<ellipse cx="85" cy="95" rx="42" ry="24" fill="#e0f2fe" stroke="#0f6e56" stroke-width="2.5"/>
<g fill="#dc2626" stroke="#7f1d1d" stroke-width="1">
<circle cx="35" cy="95" r="4"/><circle cx="43" cy="115" r="4"/><circle cx="135" cy="97" r="4"/><circle cx="127" cy="75" r="4"/><circle cx="85" cy="63" r="4"/><circle cx="85" cy="129" r="4"/>
</g>
<ellipse cx="255" cy="95" rx="62" ry="40" fill="#e0f2fe" stroke="#0f172a" stroke-width="3" stroke-dasharray="14 6"/>
<ellipse cx="255" cy="95" rx="57" ry="35" fill="none" stroke="#0f6e56" stroke-width="2.5"/>
<g fill="#dc2626" stroke="#7f1d1d" stroke-width="1">
<circle cx="190" cy="60" r="4"/><circle cx="187" cy="125" r="4"/><circle cx="325" cy="62" r="4"/><circle cx="322" cy="128" r="4"/><circle cx="255" cy="150" r="4"/>
</g>
<g font-size="11" font-weight="700" fill="#0f172a" text-anchor="middle">
<text x="85" y="178">hormone entre membrane et coque</text>
<text x="255" y="178">hormone hors de la bactérie</text>
</g>
</svg>
:::

Dans la figure, le trait vert est la membrane cytoplasmique et le trait épais pointillé est la coque. La figure ne dessine pas la sortie elle-même : au passage brutal en milieu hypotonique, la cellule gonfle et l'enveloppe se rompt un instant, ce qui libère l'hormone qui se trouvait entre la membrane et la coque.

::: exemple Du gène à l'hormone récoltée

1. Placer le gène entre ses signaux : le plasmide recombiné porte, dans l'ordre, promoteur, gène de structure, signal de fin. Sans promoteur devant le gène, la transcription ne démarre pas.
2. Cultiver en fermenteur : les bactéries se multiplient dans des conditions optimales. Chacune lit le gène (transcription en ARNm, traduction en protéine avec ses ribosomes) et fabrique l'hormone.
3. Constater le blocage : le colibacille n'est pas une cellule sécrétrice, donc l'hormone n'est pas rejetée dans le milieu. Elle se trouve entre la membrane et la coque, où la bactérie l'exporte, et il faut l'en libérer.
4. Choc osmotique, temps 1 : en milieu hypertonique, la bactérie perd de l'eau (plasmolyse) ; sa membrane se rétracte et agrandit l'espace entre la membrane et la coque, où se trouve l'hormone.
5. Choc osmotique, temps 2 : en milieu hypotonique, la bactérie reprend brutalement de l'eau (turgescence), gonfle, et le contenu de cet espace, hormone comprise, est libéré à travers la coque.

:::

::: piege
**Erreur : croire qu'un gène inséré s'exprime sans signaux.** « Le gène est dans le plasmide, la bactérie va donc le lire » tente parce que la bactérie possède tout l'équipement. Mais l'équipement ne démarre qu'à un promoteur et s'arrête au signal de fin : sans ces séquences, la transcription ne se fait pas.
:::

::: piege
**Erreur : inverser les deux temps du choc osmotique.** « On place d'abord les bactéries dans l'eau pure » tente parce que l'eau qui entre semble faire sortir la protéine. Mais le milieu hypertonique doit d'abord rétracter la membrane et agrandir l'espace où se trouve l'hormone ; le passage en milieu hypotonique vient ensuite libérer le contenu de cet espace.
:::

::: propriete
**Exprimer, puis extraire.** Le gène de structure s'exprime s'il est précédé d'un promoteur et suivi d'un signal de fin de transcription. La protéine se récolte par choc osmotique (hypertonique puis hypotonique) ou par lyse des bactéries.
Cas limite : après une lyse, la protéine est mêlée aux débris des cellules : il faut ensuite l'isoler de ces débris.
:::

::: verifie À toi : la lyse
Une équipe récolte la protéine par lyse des bactéries et non par choc osmotique. Que contient la solution obtenue, et quel travail reste-t-il ?

---

La lyse fait éclater les cellules : la solution contient la protéine mêlée aux débris cellulaires, et il reste à isoler la protéine de ces débris.
:::

::: retenir
Un gène s'exprime entre son promoteur et son signal de fin ; la protéine, qui n'est pas rejetée dans le milieu, se récolte par choc osmotique (hypertonique puis hypotonique) ou par lyse.
:::

> 🏆 Chapitre franchi, héros : tu sais pourquoi un gène humain peut être lu par un colibacille et comment on le lui fait fabriquer. Prochaine quête : d'où vient la diversité génétique des individus.
