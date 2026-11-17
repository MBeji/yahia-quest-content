# 🔋 Étude de la pile Daniell — quand une réaction fait circuler le courant

> 💡 «Une pile est une réaction d'oxydoréduction dont on a séparé les deux acteurs : les électrons n'ont plus d'autre chemin que le fil.»

Une lame de zinc et une lame de cuivre plongées dans deux béchers suffisent à allumer un petit récepteur, sans générateur : où est la source du courant, et comment prévoir son sens ? Huit notions répondent : le transfert direct d'électrons, la pile et la demi-pile, le fonctionnement de la pile Daniell, le pont salin, la représentation d'une pile, la force électromotrice, les piles du même type et les micropiles de la corrosion. On suppose acquis le couple redox Ox/Red, les équations formelles d'oxydation et de réduction, et l'équation bilan d'une réaction d'oxydoréduction.

## ⚡ Le transfert direct d'électrons : oxydant, réducteur et couple

Un clou de fer plongé dans une solution bleue de sulfate de cuivre (II) se couvre en quelques minutes d'un dépôt rouge, et la teinte bleue s'estompe.
Quelle espèce donne des électrons, laquelle en reçoit, et que disent les deux couples en jeu ?

::: definition
**Réducteur, oxydant, couple** — Un réducteur est une entité chimique qui peut perdre des électrons ; un oxydant est une entité qui peut en gagner. Un couple redox se note Ox/Red (forme oxydée / forme réduite) et se traduit par l'équation formelle a Ox + n e⁻ ⇄ b Red.
Une réaction d'oxydoréduction est une réaction où des électrons passent d'un réducteur à un oxydant : Ox₁ + Red₂ → Red₁ + Ox₂. Lorsque les deux réactifs sont en contact, le transfert d'électrons est dit **direct**.
:::

::: exemple Le clou de fer dans le sulfate de cuivre (II)

1. Le dépôt rouge est du cuivre métallique : les ions Cu²⁺ gagnent des électrons, Cu²⁺ + 2 e⁻ ⇄ Cu ; Cu²⁺ est l'oxydant du couple Cu²⁺/Cu, car il capte des électrons.
2. Le clou est attaqué : le fer passe en solution sous forme d'ions Fe²⁺, Fe ⇄ Fe²⁺ + 2 e⁻ ; Fe est le réducteur du couple Fe²⁺/Fe, car il cède des électrons.
3. Le fer cède 2 électrons et le cuivre en capte 2 : les électrons s'annulent dans le bilan, Fe + Cu²⁺ → Fe²⁺ + Cu, avec une flèche simple parce que c'est la réaction qui se produit effectivement.
4. Le transfert est direct : le fer et les ions Cu²⁺ sont en contact à la surface du clou, les électrons passent de l'un à l'autre sans aucun fil.

:::

::: piege
**Erreur : appeler « réducteur » l'espèce qui est réduite.** On lit « les ions cuivre sont réduits » et l'on range Cu²⁺ parmi les réducteurs. L'erreur tente parce que les deux mots se ressemblent ; mais le réducteur est celui qui cède des électrons, donc celui qui est oxydé : ici Fe, tandis que Cu²⁺, qui est réduit, est l'oxydant.
:::

::: propriete
**Les électrons s'équilibrent** — Dans une réaction d'oxydoréduction, le réducteur cède autant d'électrons que l'oxydant en reçoit, et aucun électron ne figure dans le bilan : on multiplie chaque demi-équation par le coefficient qui égalise les électrons.
Cas : Cu + 2 Ag⁺ → Cu²⁺ + 2 Ag ; un atome de cuivre cède 2 électrons alors que chaque ion Ag⁺ n'en reçoit qu'un, d'où le coefficient 2 devant Ag⁺ et devant Ag.
Cas limite : un métal plongé dans une solution de ses propres ions (Fe dans Fe²⁺) ne subit aucune transformation d'ensemble, car les deux espèces appartiennent au même couple.
:::

::: verifie À toi : le zinc dans le nitrate de plomb (II)
Une lame de zinc plongée dans une solution de nitrate de plomb (II) se recouvre d'un dépôt gris de plomb. Écrire les deux demi-équations et le bilan.

---

Le plomb se dépose : Pb²⁺ + 2 e⁻ ⇄ Pb, les ions Pb²⁺ sont l'oxydant. Le zinc est attaqué : Zn ⇄ Zn²⁺ + 2 e⁻, c'est le réducteur. Chaque partenaire échange 2 électrons, qui disparaissent du bilan : Zn + Pb²⁺ → Zn²⁺ + Pb.
:::

::: retenir
Un réducteur cède des électrons, un oxydant en capte ; dans le bilan d'une réaction redox aucun électron n'apparaît, et les électrons cédés égalent les électrons captés.
:::

## 🍋 La pile électrochimique et la demi-pile

On enfonce une lame de cuivre et une lame de zinc dans un citron et on les relie à un milliampèremètre : l'aiguille dévie, sans générateur ni autre liaison que l'appareil.
D'où vient ce courant, et pourquoi faut-il deux lames de métaux différents ?

::: definition
**Pile électrochimique et demi-pile** — Une pile électrochimique est un dispositif qui fournit du courant électrique grâce à une réaction chimique spontanée.
Une demi-pile correspond à un couple redox : c'est un conducteur électronique (métal, alliage ou graphite) au contact d'un conducteur ionique (solution d'électrolyte).
:::

::: exemple Le citron à deux lames
1. Dans le fil, le courant est un déplacement d'électrons ; ces électrons ont été cédés par un réducteur, qui ne peut être que le zinc, car le cuivre n'est pas attaqué.
2. Le jus de citron contient des ions H₃O⁺ ; le cuivre est moins réducteur que le dihydrogène H₂, alors que le zinc l'est davantage : seul le zinc réagit, Zn + 2 H₃O⁺ → Zn²⁺ + H₂ + 2 H₂O.
3. Les électrons cédés par le zinc quittent la lame par le fil, traversent le milliampèremètre et sont captés par les ions H₃O⁺ du côté du cuivre : le transfert est **indirect**, car il passe par le circuit extérieur (une partie du zinc réagit aussi directement avec l'acide à sa surface).
4. Dans le fil, le courant circule donc de la lame de cuivre vers la lame de zinc, en sens inverse des électrons.

:::

::: piege
**Erreur : croire que le courant est un mouvement d'électrons dans tout le circuit.** On l'affirme parce que le fil et l'électrode le montrent. Mais dans la solution, aucun électron ne circule : le courant y est dû au déplacement d'ions positifs et négatifs ; seul le circuit extérieur est parcouru par des électrons.
:::

::: propriete
**L'origine du courant** — Une pile débite un courant parce qu'une réaction d'oxydoréduction spontanée s'y produit, et que les électrons échangés passent par le circuit extérieur. Pour que le transfert soit sûrement indirect, on place chaque couple dans sa demi-pile : ici Zn²⁺/Zn dans l'une, H₃O⁺/H₂ dans l'autre.
Cas : dans la pile au citron, le zinc touche aussi les ions H₃O⁺ du jus, si bien qu'une partie du transfert reste directe ; la pile Daniell, qui place chaque couple dans son bécher, n'a pas ce défaut.
Cas limite : si l'on ouvre le circuit, le courant s'annule et la réaction s'arrête.
:::

::: verifie À toi : une demi-pile de plomb
Une lame de plomb plonge dans une solution de nitrate de plomb (II). Est-ce une demi-pile ? Quel couple redox la forme, et quels sont ses deux conducteurs ?

---

Oui : c'est une demi-pile, car elle correspond à un couple redox, Pb²⁺/Pb. Le conducteur électronique est la lame de plomb, métal qui échange les électrons ; le conducteur ionique est la solution de nitrate de plomb (II), qui apporte les ions Pb²⁺.
:::

::: retenir
Une pile débite grâce à une réaction redox spontanée dont les électrons passent par le circuit extérieur ; chaque couple occupe une demi-pile (conducteur électronique + conducteur ionique).
:::

## 🔌 La pile Daniell : bornes, anode, cathode et sens du courant

On prépare deux béchers, l'un avec une lame de zinc dans du sulfate de zinc à 0,10 mol·L⁻¹, l'autre avec une lame de cuivre dans du sulfate de cuivre (II) à 0,10 mol·L⁻¹, reliés par un pont salin ; on branche un résistor et un milliampèremètre, puis on ferme l'interrupteur.
Que voit-on, et quelle réaction fait vivre ce montage ?

::: definition
**Pile Daniell, anode et cathode** — La pile Daniell comprend deux compartiments : le métal cuivre au contact d'un sel de cuivre (II), et le métal zinc au contact d'un sel de zinc (II), réunis par une jonction (pont salin ou paroi poreuse).
L'électrode où se produit une oxydation est l'**anode** ; celle où se produit une réduction est la **cathode**.
:::

::: figure Pile Daniell en fonctionnement : les électrons e⁻ vont du zinc (anode, borne −) vers le cuivre (cathode, borne +) à travers le résistor R, le courant I va en sens inverse, et le pont salin laisse passer K⁺ et Cl⁻
<svg viewBox="0 0 340 272"><title>Pile Daniell en fonctionnement</title>
<rect x="25" y="146" width="110" height="78" rx="0" fill="#e2e8f0" stroke="none" stroke-width="0"/>
<rect x="205" y="146" width="110" height="78" rx="0" fill="#7dd3fc" stroke="none" stroke-width="0"/>
<path d="M24 116 V224 H136 V116" stroke="#0f172a" stroke-width="1.6" fill="none"/>
<path d="M204 116 V224 H316 V116" stroke="#0f172a" stroke-width="1.6" fill="none"/>
<rect x="58" y="86" width="12" height="124" rx="0" fill="#94a3b8" stroke="#0f172a" stroke-width="1.4"/>
<rect x="268" y="86" width="12" height="124" rx="0" fill="#c2410c" stroke="#0f172a" stroke-width="1.4"/>
<path d="M118 190 V104 H222 V190" stroke="#475569" stroke-width="11" fill="none"/>
<path d="M118 190 V104 H222 V190" stroke="#fde68a" stroke-width="7" fill="none"/>
<path d="M64 86 V40 H146" stroke="#0f172a" stroke-width="1.6" fill="none"/>
<path d="M194 40 H274 V86" stroke="#0f172a" stroke-width="1.6" fill="none"/>
<rect x="146" y="32" width="48" height="16" rx="2" fill="#ffffff" stroke="#0f172a" stroke-width="1.4"/>
<text x="170" y="44" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">R</text>
<circle cx="64" cy="64" r="7" fill="#ffffff" stroke="#0f172a" stroke-width="1.4"/>
<text x="64" y="68" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">−</text>
<circle cx="274" cy="64" r="7" fill="#ffffff" stroke="#0f172a" stroke-width="1.4"/>
<text x="274" y="68" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">+</text>
<line x1="84" y1="26" x2="124" y2="26" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="130,26 122,22 122,30" fill="#0f172a"/>
<text x="106" y="18" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">e⁻</text>
<line x1="126" y1="56" x2="86" y2="56" stroke="#b45309" stroke-width="1.6"/>
<polygon points="80,56 88,52 88,60" fill="#b45309"/>
<text x="106" y="70" text-anchor="middle" font-size="10" font-weight="700" fill="#b45309" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">I</text>
<text x="170" y="92" text-anchor="middle" font-size="9" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">K⁺ →</text>
<text x="170" y="128" text-anchor="middle" font-size="9" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">← Cl⁻</text>
<text x="41" y="180" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">Zn</text>
<text x="297" y="180" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">Cu</text>
<text x="92" y="206" text-anchor="middle" font-size="9" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">Zn²⁺</text>
<text x="247" y="206" text-anchor="middle" font-size="9" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">Cu²⁺</text>
<text x="80" y="242" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">anode (oxydation)</text>
<text x="260" y="242" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">cathode (réduction)</text>
<text x="80" y="258" text-anchor="middle" font-size="10" font-weight="600" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">Zn → Zn²⁺ + 2 e⁻</text>
<text x="260" y="258" text-anchor="middle" font-size="10" font-weight="600" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">Cu²⁺ + 2 e⁻ → Cu</text>
</svg>
:::

Sur la figure, la lame de zinc porte la borne − et la demi-équation d'oxydation : c'est l'anode. La lame de cuivre porte la borne + et la demi-équation de réduction : c'est la cathode.

::: exemple Lire les observations de la pile Daniell

1. Le courant circule dans le fil de la lame de cuivre vers la lame de zinc : la lame de cuivre est la borne +, la lame de zinc la borne −, car le courant sort d'une pile par sa borne +.
2. Un dépôt de cuivre se forme sur la lame de cuivre : Cu²⁺ + 2 e⁻ → Cu est une réduction, donc cette lame est la cathode.
3. La masse de la lame de zinc diminue : Zn → Zn²⁺ + 2 e⁻ est une oxydation, donc cette lame est l'anode.
4. Les électrons partent de l'anode, parcourent le fil et arrivent à la cathode, en sens inverse du courant ; le bilan est Zn + Cu²⁺ → Zn²⁺ + Cu, avec [Zn²⁺] qui augmente et [Cu²⁺] qui diminue.

:::

::: piege
**Erreur : croire que le courant sort de la pile par la borne négative.** Les électrons quittent la pile par la borne −, et l'on confond leur sens avec celui du courant. Or le courant électrique est orienté par convention en sens inverse des électrons : dans le circuit extérieur il sort par la borne +, ici le cuivre, et rentre par la borne −, ici le zinc.
:::

::: propriete
**Polarité d'une pile qui débite** — Dans une pile en fonctionnement, l'anode est la borne − et la cathode la borne +. Dans le circuit extérieur, les électrons vont de l'anode vers la cathode et le courant de la cathode vers l'anode. La pile est un dipôle dissymétrique : on ne peut pas permuter ses deux bornes.
Cas : la pile Daniell, avec le zinc comme borne − et le cuivre comme borne +.
Cas limite : en circuit ouvert, les bornes gardent leur polarité (+ sur le cuivre) mais aucun courant ne circule et la transformation chimique s'arrête.
:::

::: verifie À toi : une pile fer-cuivre
Dans une pile formée d'une lame de fer dans Fe²⁺ et d'une lame de cuivre dans Cu²⁺, la lame de fer s'amincit et le cuivre se dépose sur la lame de cuivre. Quelle est l'anode, quelle est la borne −, et que vaut le bilan ?

---

La lame de fer s'amincit : Fe → Fe²⁺ + 2 e⁻ est une oxydation, donc le fer est l'anode et la borne −. Le cuivre se dépose : Cu²⁺ + 2 e⁻ → Cu est une réduction, donc le cuivre est la cathode et la borne +. Le bilan est Fe + Cu²⁺ → Fe²⁺ + Cu.
:::

::: retenir
Dans une pile qui débite : anode (oxydation) = borne −, cathode (réduction) = borne + ; électrons de l'anode vers la cathode dans le fil, courant en sens inverse.
:::

## 🌉 Le pont salin : fermer le circuit sans mélanger

On retire le pont salin de la pile Daniell : l'aiguille retombe à zéro presque aussitôt, alors que le fil relie toujours les deux lames.
Que fait le pont salin que le fil ne peut pas faire ?

::: definition
**Pont salin** — Tube en U rempli d'une solution gélifiée de chlorure de potassium (KCl), ou papier filtre imbibé de cette solution, dont les extrémités plongent dans les deux compartiments. Une paroi poreuse peut le remplacer.
Il assure la continuité électrique entre les deux demi-piles, sans introduire de nouveau couple redox et sans laisser les solutions se mélanger.
:::

::: exemple Suivre les ions dans la pile Daniell

1. Dans le compartiment du zinc, Zn → Zn²⁺ + 2 e⁻ fabrique des ions positifs : sans compensation, la solution cesserait d'être neutre et la réaction se bloquerait.
2. Dans le compartiment du cuivre, les ions Cu²⁺ disparaissent : ce sont alors des charges négatives qui restent en excès.
3. Les ions Cl⁻ du pont migrent vers le compartiment du zinc et les ions K⁺ vers celui du cuivre : chaque solution reste électriquement neutre.
4. Dans le pont, le courant est dû au déplacement d'ions K⁺ et Cl⁻ ; à l'intérieur de la pile il va du zinc vers le cuivre, ce qui ferme la boucle avec le courant extérieur, qui va du cuivre vers le zinc.

:::

::: piege
**Erreur : croire que des électrons traversent le pont salin.** On le pense parce que le pont « ferme le circuit ». Mais les électrons ne circulent que dans les conducteurs électroniques, fils et électrodes ; dans le pont, la solution est un conducteur ionique et le courant est porté par K⁺ et Cl⁻.
:::

::: propriete
**Le rôle du pont salin** — Le pont salin assure le passage du courant entre les deux compartiments par le déplacement des ions, maintient chaque solution électriquement neutre, ne fait intervenir aucun nouveau couple redox et empêche les solutions de se mélanger.
Cas : un vase poreux remplit le même rôle ; la pile Daniell mesurée avec lui donne encore 1,10 V environ.
Cas limite : sans jonction entre les compartiments, le circuit est ouvert, le courant s'annule et la réaction s'arrête.
:::

::: verifie À toi : le pont d'une pile magnésium-zinc
Dans la pile Mg | Mg²⁺ || Zn²⁺ | Zn, le magnésium s'oxyde. Vers quel compartiment migrent les ions K⁺ et Cl⁻ du pont salin ?

---

Le magnésium s'oxyde dans le compartiment de gauche : les ions Mg²⁺ y apparaissent, donc les ions Cl⁻ migrent vers la gauche pour compenser. Dans le compartiment de droite, les ions Zn²⁺ disparaissent, donc les ions K⁺ migrent vers la droite. Le courant ionique va ainsi de la gauche vers la droite à l'intérieur de la pile.
:::

::: retenir
Le pont salin laisse migrer K⁺ et Cl⁻ : K⁺ vers le compartiment de la cathode, Cl⁻ vers celui de l'anode, pour garder les solutions neutres et fermer le circuit sans mélange.
:::

## ✍️ Représenter une pile : symbole et équation associée

Deux élèves dessinent la même pile Daniell : l'un place le zinc à gauche, l'autre le cuivre à gauche.
Comment écrire chaque schéma sans ambiguïté, et quelle équation chimique lui associer ?

::: definition
**Symbole d'une pile et équation associée** — Une pile du type Daniell se symbolise par Red₁ | Ox₁ || Ox₂ | Red₂, avec les concentrations quand on les connaît : le trait simple sépare deux phases, le double trait représente la jonction (pont salin ou paroi poreuse). Ne pas le confondre avec le trait incliné du couple Ox/Red.
L'équation chimique associée s'écrit Red₁ + Ox₂ ⇄ Ox₁ + Red₂ : chaque réducteur se trouve du même côté dans l'équation et dans le symbole.
:::

Pour la pile Daniell, les deux élèves obtiennent :

- zinc à gauche : Zn | Zn²⁺ (0,10 mol·L⁻¹) || Cu²⁺ (0,10 mol·L⁻¹) | Cu, avec l'équation Zn + Cu²⁺ ⇄ Zn²⁺ + Cu ;
- cuivre à gauche : Cu | Cu²⁺ (0,10 mol·L⁻¹) || Zn²⁺ (0,10 mol·L⁻¹) | Zn, avec l'équation Cu + Zn²⁺ ⇄ Cu²⁺ + Zn.

Dans chaque ligne, le réducteur écrit à gauche du symbole est aussi le premier réactif de l'équation.

::: exemple Écrire la pile Daniell avec le cuivre à gauche

1. Les deux réducteurs sont Cu et Zn ; on place Cu à gauche : la demi-pile de gauche est la lame de cuivre dans une solution d'ions Cu²⁺, car chaque métal côtoie ses propres ions.
2. La demi-pile de droite est la lame de zinc dans une solution d'ions Zn²⁺ ; on ajoute le pont salin entre les deux sur le schéma.
3. Le symbole se lit de gauche à droite avec les concentrations : Cu | Cu²⁺ (0,10 mol·L⁻¹) || Zn²⁺ (0,10 mol·L⁻¹) | Zn.
4. Le réducteur de gauche, Cu, est aussi à gauche dans l'équation : Cu + Zn²⁺ ⇄ Cu²⁺ + Zn, avec la double flèche car l'équation est une convention d'écriture.

:::

::: piege
**Erreur : écrire l'équation associée avec les réducteurs du mauvais côté.** Pour la pile Cu | Cu²⁺ || Zn²⁺ | Zn, on écrit machinalement Zn + Cu²⁺ ⇄ Zn²⁺ + Cu, l'équation habituelle de la pile Daniell. Elle tente parce qu'on la connaît par cœur ; mais elle est associée au schéma où le zinc est à gauche. Ici le cuivre est à gauche, donc l'équation est Cu + Zn²⁺ ⇄ Cu²⁺ + Zn.
:::

::: propriete
**Convention de l'équation associée** — À toute représentation d'une pile, on associe l'équation dont les deux réducteurs sont placés du côté qu'ils occupent dans la représentation. L'équation associée ne dit pas quelle réaction a lieu ; elle fixe seulement l'écriture de référence. On peut partir de l'équation : on dessine alors la pile conforme à cette écriture.
Cas : Ni | Ni²⁺ || Zn²⁺ | Zn se lit avec l'équation Ni + Zn²⁺ ⇄ Ni²⁺ + Zn.
Cas limite : l'équation inverse Zn + Ni²⁺ ⇄ Zn²⁺ + Ni décrit la pile écrite dans l'autre sens, Zn | Zn²⁺ || Ni²⁺ | Ni.
:::

::: verifie À toi : de l'équation à la pile
On donne l'équation associée Zn + Ni²⁺ ⇄ Zn²⁺ + Ni. Écrire le symbole de la pile correspondante.

---

Le réducteur de gauche dans l'équation est Zn : il se place à gauche de la pile, au contact de ses ions Zn²⁺. Le réducteur de droite est Ni, au contact des ions Ni²⁺. Le symbole est Zn | Zn²⁺ || Ni²⁺ | Ni.
:::

::: retenir
Symbole Red₁ | Ox₁ || Ox₂ | Red₂ ; équation associée Red₁ + Ox₂ ⇄ Ox₁ + Red₂ : chaque réducteur du même côté dans le symbole et dans l'équation.
:::

## 📏 La force électromotrice : le signe de E dit la réaction

On branche un voltmètre sur la pile Daniell : il affiche +1,10 V ou −1,10 V selon que sa borne COM touche le zinc ou le cuivre.
Laquelle de ces deux valeurs est la tension de la pile, et que nous apprend son signe ?

::: definition
**Force électromotrice (f.é.m.)** — La force électromotrice E d'une pile est la différence de potentiel, en circuit ouvert, entre sa borne de droite et sa borne de gauche : E = V_D − V_G.
C'est une grandeur algébrique, de signe positif ou négatif. Le voltmètre affiche le potentiel de la borne reliée à son entrée V moins celui de la borne reliée à COM : pour lire E, on relie COM à la borne de gauche.
:::

::: figure Mesure de E pour la pile Zn | Zn²⁺ (0,10 mol·L⁻¹) || Cu²⁺ (0,10 mol·L⁻¹) | Cu : COM sur la borne de gauche, l'afficheur indique V_D − V_G (valeur mesurée pour des concentrations égales)
<svg viewBox="0 0 340 232"><title>Mesure de la f.é.m. de la pile Daniell au voltmètre</title>
<rect x="25" y="142" width="110" height="40" rx="0" fill="#e2e8f0" stroke="none" stroke-width="0"/>
<rect x="205" y="142" width="110" height="40" rx="0" fill="#7dd3fc" stroke="none" stroke-width="0"/>
<path d="M24 122 V182 H136 V122" stroke="#0f172a" stroke-width="1.6" fill="none"/>
<path d="M204 122 V182 H316 V122" stroke="#0f172a" stroke-width="1.6" fill="none"/>
<rect x="58" y="104" width="12" height="60" rx="0" fill="#94a3b8" stroke="#0f172a" stroke-width="1.4"/>
<rect x="268" y="104" width="12" height="60" rx="0" fill="#c2410c" stroke="#0f172a" stroke-width="1.4"/>
<path d="M118 160 V112 H222 V160" stroke="#475569" stroke-width="11" fill="none"/>
<path d="M118 160 V112 H222 V160" stroke="#fde68a" stroke-width="7" fill="none"/>
<rect x="128" y="14" width="84" height="48" rx="5" fill="#f1f5f9" stroke="#0f172a" stroke-width="1.4"/>
<text x="170" y="40" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">1,10 V</text>
<circle cx="140" cy="62" r="4" fill="#0f172a" stroke="#0f172a" stroke-width="1.4"/>
<circle cx="200" cy="62" r="4" fill="#0f172a" stroke="#0f172a" stroke-width="1.4"/>
<path d="M140 62 V80 H64 V104" stroke="#0f172a" stroke-width="1.6" fill="none"/>
<path d="M200 62 V80 H274 V104" stroke="#0f172a" stroke-width="1.6" fill="none"/>
<text x="130" y="76" text-anchor="end" font-size="9" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">COM</text>
<text x="210" y="76" text-anchor="start" font-size="9" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">V</text>
<text x="92" y="158" text-anchor="middle" font-size="9" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">Zn²⁺</text>
<text x="247" y="158" text-anchor="middle" font-size="9" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">Cu²⁺</text>
<text x="80" y="200" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">V_G (zinc)</text>
<text x="260" y="200" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">V_D (cuivre)</text>
<text x="170" y="224" text-anchor="middle" font-size="11" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">E = V_D − V_G = +1,10 V</text>
</svg>
:::

Sur la figure, V_G est le potentiel de la borne de zinc, reliée à COM, et V_D celui de la borne de cuivre : l'afficheur donne directement E = V_D − V_G.

::: exemple Interpréter E = +1,10 V pour la pile Daniell

1. E = V_D − V_G = V_Cu − V_Zn = +1,10 V, donc V_Cu > V_Zn : la borne de droite, le cuivre, est la borne +.
2. La borne + est à droite : dans le circuit extérieur, les électrons vont de la gauche vers la droite, du zinc vers le cuivre, car ils quittent la borne −.
3. La réaction directe de l'équation associée a lieu : Zn + Cu²⁺ → Zn²⁺ + Cu.
4. On permute les deux demi-piles : avec le cuivre à gauche, E = V_Zn − V_Cu = −1,10 V ; la polarité et la réaction n'ont pas changé, seul le signe de E a changé.

:::

::: piege
**Erreur : croire qu'une f.é.m. négative signifie que la pile ne débite pas.** Un signe moins semble signaler une panne. Il indique seulement que la borne + est à gauche dans le schéma choisi : la pile Cu | Cu²⁺ || Zn²⁺ | Zn, avec E = −1,10 V, débite exactement comme l'autre, par la même réaction Zn + Cu²⁺ → Zn²⁺ + Cu.
:::

::: propriete
**Le signe de E** — Pour une pile représentée par un schéma donné :
- si E > 0, la borne + est à droite, la réaction directe de l'équation associée a lieu, et les électrons vont de la gauche vers la droite ;
- si E < 0, la borne + est à gauche, c'est la réaction inverse qui a lieu, et les électrons vont de la droite vers la gauche ;
- le signe de E dépend du schéma, alors que la polarité et la réaction spontanée n'en dépendent pas.

Cas : Zn à gauche, E = +1,10 V ; cuivre à gauche, E = −1,10 V ; si COM est sur la borne de droite, l'afficheur indique −E et non E.
Cas limite : si E = 0, le contenu de la pile est en équilibre dynamique pour l'équation associée, aucune réaction spontanée n'a lieu et la pile ne débite pas.
:::

::: verifie À toi : lire une mesure
Pour la pile Pb | Pb²⁺ (0,10 mol·L⁻¹) || Zn²⁺ (0,10 mol·L⁻¹) | Zn, le voltmètre dont la borne COM touche le plomb affiche −0,63 V. Quelle est la borne +, quelle réaction a lieu, et quel est le sens des électrons ?

---

COM est sur la borne de gauche, donc la lecture est E = V_Zn − V_Pb = −0,63 V < 0 : la borne + est à gauche, le plomb. C'est la réaction inverse de Pb + Zn²⁺ ⇄ Pb²⁺ + Zn qui a lieu : Zn + Pb²⁺ → Zn²⁺ + Pb. Les électrons vont de la droite vers la gauche, du zinc vers le plomb.
:::

::: retenir
E = V_D − V_G en circuit ouvert : E > 0 ⇒ réaction directe, borne + à droite ; E < 0 ⇒ réaction inverse, borne + à gauche ; E = 0 ⇒ équilibre, pas de courant.
:::

## 🔩 Les piles du type pile Daniell : généraliser et classer les métaux

Quatre lames (zinc, fer, cuivre, plomb) et les solutions de leurs ions à concentrations égales sont disponibles.
Combien de piles distinctes peut-on monter, et comment prévoir dans chacune le métal qui est attaqué ?

::: definition
**Pile du type pile Daniell** — Pile formée de deux demi-piles M₁ⁿ⁺/M₁ et M₂ⁿ⁺/M₂ : deux métaux attaquables, chacun au contact de la solution de ses ions, avec la même charge n pour les deux ions (n = m dans ce chapitre).
Avec M₂ à gauche : M₂ | M₂ⁿ⁺ || M₁ⁿ⁺ | M₁, équation associée M₂ + M₁ⁿ⁺ ⇄ M₂ⁿ⁺ + M₁, et E = V_M1 − V_M2.
:::

::: exemple Quatre métaux, six piles

1. Chaque pile associe deux couples différents parmi quatre : 4 × 3 ÷ 2 = 6 piles ; écrire Zn-Cu ou Cu-Zn donne la même pile, vue sous deux schémas.
2. Pour la pile Cu | Cu²⁺ (1,0 mol·L⁻¹) || Pb²⁺ (1,0 mol·L⁻¹) | Pb, on mesure E = V_Pb − V_Cu = −0,47 V : E < 0, donc la borne + est à gauche, sur le cuivre.
3. C'est la réaction inverse de Cu + Pb²⁺ ⇄ Cu²⁺ + Pb qui a lieu, Pb + Cu²⁺ → Pb²⁺ + Cu : la lame de plomb s'amincit et du cuivre se dépose.
4. Le plomb est donc oxydé en présence de Cu²⁺ : il est plus réducteur que le cuivre. En lisant de la même façon les six piles, on classe les quatre métaux.

:::

::: piege
**Erreur : croire que le métal du compartiment de gauche est toujours celui qui est attaqué.** On généralise la pile Daniell, où le zinc, placé à gauche, s'oxyde. L'erreur tente parce qu'elle réussit dans ce seul schéma ; mais dans Cu | Cu²⁺ || Pb²⁺ | Pb, c'est le plomb, à droite, qui s'oxyde. La position n'est qu'une convention d'écriture : le signe de E désigne le métal attaqué.
:::

::: propriete
**Prévoir dans une pile du type Daniell** — Pour les concentrations utilisées, le métal le plus réducteur des deux s'oxyde : sa lame s'amincit et elle forme la borne −, tandis que les ions de l'autre métal se déposent sur l'autre lame. Si le métal de gauche est le plus réducteur, E > 0 ; sinon E < 0.
Cas : Zn | Zn²⁺ || Pb²⁺ | Pb donne E ≈ +0,63 V, le zinc est plus réducteur que le plomb ; Fe | Fe²⁺ || Zn²⁺ | Zn donne E ≈ −0,35 V, le zinc est plus réducteur que le fer.
Cas limite : un couple sans électrode métallique attaquable (Fe³⁺/Fe²⁺, H₃O⁺/H₂) n'entre pas dans cette famille de piles ; un couple dont l'ion n'a pas la même charge sort du cadre de ce chapitre, limité à n = m.
:::

::: verifie À toi : compter les piles réalisables
Avec les couples Zn²⁺/Zn, Ni²⁺/Ni, Cu²⁺/Cu, Al³⁺/Al et Ag⁺/Ag, combien de piles du type Daniell (ions de même charge) peut-on construire ?

---

Seuls les couples dont l'ion porte la charge 2+ peuvent s'associer : Zn²⁺/Zn, Ni²⁺/Ni et Cu²⁺/Cu. Al³⁺ (charge 3+) et Ag⁺ (charge 1+) n'ont aucun partenaire de même charge. Avec 3 couples, on forme 3 × 2 ÷ 2 = 3 piles.
:::

::: retenir
Dans une pile du type Daniell (ions de même charge), le métal le plus réducteur s'oxyde et forme la borne − ; le signe de E, lu avec le schéma, désigne ce métal.
:::

## 🌊 Les micropiles : la corrosion du fer en eau salée

Une tôle de fer ou la coque d'un navire laissée dans l'eau de mer se couvre de rouille, sans qu'on voie ni pile ni fil.
Où sont les électrodes, où est le fil, et quelles réactions s'y produisent ?

::: definition
**Corrosion et micropile** — La corrosion est l'oxydation d'un métal par un oxydant du milieu, souvent le dioxygène dissous. La corrosion du fer en eau salée est de nature électrochimique : une micropile se forme, dont une zone de la surface est l'anode (siège de l'oxydation) et une autre la cathode (siège de la réduction).
Le métal lui-même relie les deux zones et joue le rôle du fil, en court-circuit ; l'eau salée est l'électrolyte. La corrosion commence de préférence aux rayures et aux irrégularités du métal.
:::

::: figure Micropile sous une goutte d'eau salée posée sur du fer : l'anode est au centre, les cathodes sont à la périphérie, et les électrons e⁻ circulent dans le métal du centre vers les bords
<svg viewBox="0 76 340 154"><title>Micropile de corrosion sous une goutte d eau salée</title>
<path d="M90 140 Q170 40 250 140 Z" stroke="#0f172a" stroke-width="1.6" fill="#bae6fd"/>
<rect x="30" y="140" width="280" height="30" rx="0" fill="#94a3b8" stroke="#0f172a" stroke-width="1.4"/>
<rect x="140" y="134" width="60" height="8" rx="0" fill="#dc2626" stroke="none" stroke-width="0"/>
<rect x="94" y="134" width="36" height="8" rx="0" fill="#2563eb" stroke="none" stroke-width="0"/>
<rect x="210" y="134" width="36" height="8" rx="0" fill="#2563eb" stroke="none" stroke-width="0"/>
<text x="170" y="104" text-anchor="middle" font-size="10" font-weight="600" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">eau salée</text>
<text x="70" y="160" text-anchor="middle" font-size="9" font-weight="600" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">tôle de fer</text>
<line x1="160" y1="161" x2="124" y2="161" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="118,161 126,157 126,165" fill="#0f172a"/>
<line x1="180" y1="161" x2="216" y2="161" stroke="#0f172a" stroke-width="1.6"/>
<polygon points="222,161 214,157 214,165" fill="#0f172a"/>
<text x="142" y="155" text-anchor="middle" font-size="9" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">e⁻</text>
<text x="198" y="155" text-anchor="middle" font-size="9" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">e⁻</text>
<text x="113" y="187" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">cathode</text>
<text x="170" y="187" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">anode</text>
<text x="227" y="187" text-anchor="middle" font-size="10" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">cathode</text>
<text x="170" y="205" text-anchor="middle" font-size="10" font-weight="600" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">anode : Fe → Fe²⁺ + 2 e⁻</text>
<text x="170" y="221" text-anchor="middle" font-size="10" font-weight="600" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3" stroke-linejoin="round">cathode : O₂ + 2 H₂O + 4 e⁻ → 4 OH⁻</text>
</svg>
:::

Sur la figure, la zone rouge au centre est l'anode, où le fer s'oxyde, et les zones bleues sur les bords sont des cathodes, où le dioxygène est réduit.

::: exemple Une goutte d'eau salée sur la tôle de fer

1. Au centre de la goutte, le fer s'oxyde : Fe → Fe²⁺ + 2 e⁻, car cette zone cède des électrons ; c'est l'anode.
2. À la périphérie, le dioxygène dissous est réduit : O₂ + 2 H₂O + 4 e⁻ → 4 OH⁻, car cette zone capte des électrons ; c'est une cathode : le dioxygène se dissout plus facilement à la périphérie, plus exposée à l'air.
3. Les électrons circulent dans la tôle, de l'anode vers les cathodes ; dans la goutte, ce sont les ions qui assurent le courant.
4. Pour égaliser les électrons, on double la demi-équation du fer : 2 Fe + O₂ + 2 H₂O → 2 Fe²⁺ + 4 OH⁻, bilan où 4 électrons cédés valent 4 électrons captés.

:::

::: piege
**Erreur : croire que la cathode est toujours le pôle négatif.** On associe « cathode » à « moins ». Or, dans une pile, la cathode est le siège de la réduction et constitue le pôle + : c'est le cas de l'électrode de cuivre de la pile Daniell, et des zones périphériques de la micropile.
:::

::: propriete
**Se protéger de la corrosion** — On protège le fer en l'isolant du milieu par un revêtement non métallique (peinture, vernis, plastique) ou métallique (chrome, nickel), ou en lui associant un métal plus réducteur, qui s'oxyde à sa place.
Cas : le zinc est plus réducteur que le fer (pile Fe-Zn) ; une coque couverte de zinc voit le zinc s'oxyder en premier.
Cas limite : un revêtement rayé laisse le fer au contact de l'eau salée, et la micropile se reforme.
:::

::: verifie À toi : une goutte sur le zinc
Une goutte d'eau salée est posée sur une tôle de zinc. Quelle demi-équation se produit à l'anode, laquelle à la cathode, et que valent les électrons échangés ?

---

À l'anode, le zinc s'oxyde : Zn → Zn²⁺ + 2 e⁻. À la cathode, le dioxygène dissous est réduit, comme pour le fer : O₂ + 2 H₂O + 4 e⁻ → 4 OH⁻. Pour égaliser les électrons, il faut doubler la demi-équation du zinc : 4 électrons cédés par 2 Zn, 4 électrons captés par O₂.
:::

::: retenir
Corrosion du fer en eau salée = micropile : anode Fe → Fe²⁺ + 2 e⁻, cathode O₂ + 2 H₂O + 4 e⁻ → 4 OH⁻ ; la cathode, siège de la réduction, est le pôle +.
:::

> 🏆 Tu sais désormais lire une pile : le fil et le pont salin se partagent les électrons et les ions, l'anode est la borne −, et le signe de E, lu avec le schéma, dit quelle réaction a lieu et dans quel sens.
