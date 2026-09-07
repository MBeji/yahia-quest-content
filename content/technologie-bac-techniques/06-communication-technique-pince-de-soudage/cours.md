# ⚡ La pince de soudage — 72 repères sous pression

> 💡 «Deux chapitres t'ont appris à lire un plan. En voici un de 72 repères, avec un vérin dedans : c'est là qu'on voit qui sait vraiment lire.»

Tu sais déjà décoder un dessin d'ensemble en deux temps, fermer une chaîne de cotes et choisir la coupe qui montre ce qu'il faut montrer. Le support de ce chapitre monte d'un cran : une **pince de soudage par point** qui assemble les châssis et les carrosseries d'automobile, actionnée par un **vérin pneumatique**, et dont la nomenclature aligne **72 repères**. Trois choses y sont neuves — un **actionneur pneumatique** avec ses deux chambres et ses joints, un **mécanisme de bras articulés** dont le pivot se démonte en maintenance, et un **dessin de définition entièrement coté**, avec ses spécifications géométriques et son état de surface. Et une question nouvelle en cotation : non plus *installer* une condition, mais **vérifier** qu'une condition déjà cotée tient.

## 🔥 Souder par points : ce que la machine doit produire

La pince supporte les deux **électrodes E1 et E2** et permet leur déplacement fonctionnel. Elle assemble des tôles **sans métal d'apport** : rien ne vient se déposer entre les pièces, elles fondent l'une dans l'autre.

::: definition Le cycle du soudage par point
Les pièces sont **maintenues en contact** sous un **effort d'accostage** exercé par les deux électrodes. Un courant de **basse tension** et de **forte intensité** passe alors dans une zone très localisée. Ce courant induit un **chauffage par effet Joule** provoquant la **fusion** des pièces dans la zone de leur contact : le **noyau**. Après **coupure du courant**, l'effort, **toujours appliqué**, **forge** la soudure. Une succession de points de soudage réalise une **liaison complète indémontable** entre deux tôles.
:::

Retiens l'ordre des cinq temps, il commande tout le reste : **accoster** → **faire passer le courant** → **fondre (le noyau se forme)** → **couper le courant, l'effort restant appliqué : la soudure est forgée** → **desserrer et passer au point suivant**.

::: figure Les deux électrodes serrent les tôles, et le courant ne fond que la petite lentille de métal située entre elles : c'est le noyau, et c'est lui, une fois forgé, qui devient le point de soudure
<svg viewBox="0 0 460 250"><g fill="none" stroke="#0f172a" stroke-width="2"><path d="M200 12 V40"/><path d="M200 222 V194"/></g><g fill="#0f172a"><polygon points="200,52 193,38 207,38"/><polygon points="200,182 193,196 207,196"/></g><g font-size="13" font-weight="700" fill="#0f172a"><text x="212" y="28">F</text><text x="212" y="214">F</text></g><polygon points="178,56 222,56 210,104 190,104" fill="#d97706" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><polygon points="190,130 210,130 222,178 178,178" fill="#d97706" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><rect x="80" y="104" width="240" height="13" fill="#cbd5e1" stroke="#0f172a" stroke-width="2"/><rect x="80" y="117" width="240" height="13" fill="#e2e8f0" stroke="#0f172a" stroke-width="2"/><ellipse cx="200" cy="117" rx="17" ry="10" fill="#ef4444" stroke="#0f172a" stroke-width="1.6"/><g fill="none" stroke="#0f172a" stroke-width="1.8"><path d="M217 76 H378 V90"/><path d="M378 144 V158 H217"/></g><rect x="352" y="90" width="52" height="54" fill="#ffffff" stroke="#0f172a" stroke-width="2"/><g fill="none" stroke="#0f172a" stroke-width="1.6"><path d="M366 100 a5 5 0 0 1 0 10 a5 5 0 0 1 0 10 a5 5 0 0 1 0 10 a5 5 0 0 1 0 10"/><path d="M390 100 a5 5 0 0 0 0 10 a5 5 0 0 0 0 10 a5 5 0 0 0 0 10 a5 5 0 0 0 0 10"/><path d="M375 96 V138 M381 96 V138"/></g><g fill="none" stroke="#0f172a" stroke-width="1"><path d="M154 74 H182"/><path d="M154 160 H182"/><path d="M88 146 L104 131"/><path d="M186 124 L120 196"/></g><g font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="150" y="78" text-anchor="end">E1</text><text x="150" y="164" text-anchor="end">E2</text><text x="6" y="150">Tôles à souder</text><text x="116" y="200" text-anchor="end">Noyau</text></g></svg>
:::

> ⚠️ L'erreur classique est de croire que l'effort ne sert qu'à faire passer le courant. Il sert **deux fois** : d'abord à **accoster** (mettre et garder les tôles en contact), puis, **après** la coupure du courant, à **forger** le noyau pendant qu'il se solidifie. Relâcher trop tôt, c'est rater le point.

## 📋 Lire une nomenclature de 72 repères

Sur un mécanisme de cette taille, la nomenclature n'est plus une annexe : c'est **le dictionnaire du dessin**. Elle porte cinq colonnes — **Rep.**, **Nbr.**, **Désignation**, **Matière**, **Observation** — et chacune se lit.

| Rep. | Nbr. | Désignation                        | Matière        | Observation    |
| ---- | ---- | ---------------------------------- | -------------- | -------------- |
| 1    | 1    | Tige avant                         | C18            | chromée        |
| 2    | 1    | Tourillon avant du vérin           | A-S5U3         |                |
| 6    | 1    | Bras                               |                |                |
| 9    | 1    | Chape M20 L=60                     | S235           |                |
| 12   | 1    | Bague isolante Ø24xØ30x20          | Nylatron       |                |
| 14   | 1    | Axe Ø20x80                         | Acier STUB     |                |
| 19   | 1    | Tige filetée M20x150               |                | NF E 22.163    |
| 30   | 1    | Bague frittée 20x24x20             | FP15           |                |
| 34   | 4    | Tube                               | Bakélite       |                |
| 40   | 1    | Pastille de butée                  | Acier STUB     | Montée serrée  |
| 42   | 2    | Écrou HM M10                       |                | NF E 25.405    |
| 51   | 2    | Piston                             | EN AW 2017 A   |                |
| 64   | 2    | Joint de piston                    |                |                |
| 69   | 2    | Bague de guidage                   | Cu Sn 8 Pb 2   |                |
| 71   | 2    | Vis CHC M8x75                      |                |                |
| 72   | 2    | Goupille de positionnement 8x90    |                |                |

::: retenir Quatre réflexes de lecture
- **Une ligne dont la colonne « Matière » est vide et qui porte une norme (NF E …) est un composant normalisé** : vis, écrou, goupille, rondelle, joint. On ne le fabrique pas, on l'**achète** — sa norme suffit à le définir. Toutes les autres lignes, celles des pièces **usinées pour cette machine**, portent une matière.
- **Une bague se désigne Ø intérieur × Ø extérieur × longueur.** « Bague frittée 20x24x20 » : elle s'enfile sur un Ø20 et loge dans un Ø24, sur 20 mm de long.
- **Une lettre M suivie d'un nombre est un filetage métrique.** La « Chape M20 L=60 » et la « Tige filetée M20x150 » partagent le même M20 : elles se vissent l'une dans l'autre.
- **La colonne « Observation » impose une condition de montage** : « Montée serrée » veut dire emmanchée en force, sans autre fixation ; « chromée » annonce un traitement de surface de la tige.
:::

Le dossier technique comporte **deux dessins d'ensemble** : la pince à l'**échelle 1:5** et le vérin pneumatique à l'**échelle 7:12**. Les deux sont des **réductions** — 1 ÷ 5 = 0,2 et 7 ÷ 12 ≈ 0,58 sont inférieurs à 1 — mais le vérin est **moins réduit**, donc dessiné plus grand relativement, pour qu'on y distingue ses joints.

> 🗡️ Un dessin d'ensemble aussi chargé se lit à coups de **coupes locales** : la pince en porte sept (A-A, B-B, C-C, D-D, E-E, F-F, G-G). Une mention entre parenthèses sous le titre d'une vue — « **Coupe D-D (sans 1, 2, 9, 19, 21 et 70)** » — signifie que ces pièces ont été **volontairement omises du dessin de cette vue** pour la rendre lisible. Elles sont bien montées sur la machine : elles ne sont simplement pas dessinées **là**.

## 💨 Le vérin pneumatique : deux chambres, une tige

C'est lui qui **convertit l'énergie pneumatique en énergie mécanique** et ferme la pince. Le **piston** sépare le tube en **deux chambres** étanches ; le manuel les repère **R1** et **R2**.

::: definition Le vérin à double effet
Un vérin **à double effet** est alimenté **alternativement** dans l'une puis dans l'autre de ses deux chambres. Mettre sous pression la chambre **côté fond** pousse le piston vers l'avant : la **tige sort**. Mettre sous pression la chambre **côté tige** le repousse vers l'arrière : la **tige rentre**. Aucun ressort n'intervient — les deux mouvements sont commandés.
:::

::: figure Le piston coupe le tube en deux chambres ; selon l'orifice alimenté, il part vers la droite (la tige sort) ou vers la gauche (elle rentre) — et l'on voit du même coup que la chambre avant est amputée du volume de la tige
<svg viewBox="0 0 460 240"><g fill="#0f6e56" opacity="0.10"><rect x="56" y="42" width="26" height="116"/><rect x="82" y="42" width="274" height="16"/><rect x="82" y="142" width="274" height="16"/><rect x="356" y="42" width="44" height="48"/><rect x="356" y="110" width="44" height="48"/></g><path d="M56.0 149.0 L65 158 M56.0 140.0 L74 158 M56.0 131.0 L82 157 M56.0 122.0 L82 148 M56.0 113.0 L82 139 M56.0 104.0 L82 130 M56.0 95.0 L82 121 M56.0 86.0 L82 112 M56.0 77.0 L82 103 M56.0 68.0 L82 94 M56.0 59.0 L82 85 M56.0 50.0 L82 76 M57 42 L82 67 M66 42 L82 58 M75 42 L82 49" fill="none" stroke="#0f172a" stroke-width="0.9"/><path d="M82.0 49.0 L91 58 M84 42 L100 58 M93 42 L109 58 M102 42 L118 58 M111 42 L127 58 M120 42 L136 58 M129 42 L145 58 M138 42 L154 58 M147 42 L163 58 M156 42 L172 58 M165 42 L181 58 M174 42 L190 58 M183 42 L199 58 M192 42 L208 58 M201 42 L217 58 M210 42 L226 58 M219 42 L235 58 M228 42 L244 58 M237 42 L253 58 M246 42 L262 58 M255 42 L271 58 M264 42 L280 58 M273 42 L289 58 M282 42 L298 58 M291 42 L307 58 M300 42 L316 58 M309 42 L325 58 M318 42 L334 58 M327 42 L343 58 M336 42 L352 58 M345 42 L356 53 M354 42 L356 44" fill="none" stroke="#0f172a" stroke-width="0.9"/><path d="M82.0 149.0 L91 158 M84 142 L100 158 M93 142 L109 158 M102 142 L118 158 M111 142 L127 158 M120 142 L136 158 M129 142 L145 158 M138 142 L154 158 M147 142 L163 158 M156 142 L172 158 M165 142 L181 158 M174 142 L190 158 M183 142 L199 158 M192 142 L208 158 M201 142 L217 158 M210 142 L226 158 M219 142 L235 158 M228 142 L244 158 M237 142 L253 158 M246 142 L262 158 M255 142 L271 158 M264 142 L280 158 M273 142 L289 158 M282 142 L298 158 M291 142 L307 158 M300 142 L316 158 M309 142 L325 158 M318 142 L334 158 M327 142 L343 158 M336 142 L352 158 M345 142 L356 153 M354 142 L356 144" fill="none" stroke="#0f172a" stroke-width="0.9"/><path d="M356.0 51.0 L365.0 42.0 M356.0 60.0 L374.0 42.0 M356.0 69.0 L383.0 42.0 M356.0 78.0 L392.0 42.0 M356.0 87.0 L400 43.0 M362.0 90.0 L400 52.0 M371.0 90.0 L400 61.0 M380.0 90.0 L400 70.0 M389.0 90.0 L400 79.0 M398.0 90.0 L400 88.0" fill="none" stroke="#0f172a" stroke-width="0.9"/><path d="M356.0 119.0 L365.0 110.0 M356.0 128.0 L374.0 110.0 M356.0 137.0 L383.0 110.0 M356.0 146.0 L392.0 110.0 M356.0 155.0 L400 111.0 M362.0 158.0 L400 120.0 M371.0 158.0 L400 129.0 M380.0 158.0 L400 138.0 M389.0 158.0 L400 147.0 M398.0 158.0 L400 156.0" fill="none" stroke="#0f172a" stroke-width="0.9"/><g fill="none" stroke="#0f172a" stroke-width="2"><rect x="56" y="42" width="26" height="116"/><rect x="82" y="42" width="274" height="16"/><rect x="82" y="142" width="274" height="16"/><rect x="356" y="42" width="44" height="48"/><rect x="356" y="110" width="44" height="48"/></g><g fill="#ffffff" stroke="#0f172a" stroke-width="2"><rect x="96" y="14" width="12" height="44"/><rect x="330" y="14" width="12" height="44"/></g><rect x="204" y="90" width="234" height="20" fill="#e2e8f0" stroke="#0f172a" stroke-width="2"/><rect x="168" y="58" width="36" height="84" fill="#bfdbfe" stroke="#0f172a" stroke-width="2"/><g fill="#0f172a"><rect x="174" y="56" width="24" height="8"/><rect x="174" y="136" width="24" height="8"/></g><g fill="#0f6e56" stroke="#0f172a" stroke-width="1.2"><rect x="360" y="82" width="18" height="8"/><rect x="360" y="110" width="18" height="8"/></g><g fill="#0f172a"><rect x="382" y="82" width="8" height="8"/><rect x="382" y="110" width="8" height="8"/></g><g fill="#ef4444" stroke="#0f172a" stroke-width="1"><rect x="392" y="82" width="8" height="8"/><rect x="392" y="110" width="8" height="8"/></g><g fill="none" stroke="#0f172a" stroke-width="1"><path d="M200 30 V56"/><path d="M69 158 V202"/><path d="M270 158 V202"/><path d="M356 174 H400 M378 174 V202"/><path d="M420 84 V90"/></g><g font-size="11" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="200" y="24">piston (51) et son joint (64)</text><text x="69" y="214">fond (48)</text><text x="270" y="214">tube (47)</text><text x="378" y="214">guidage et joints de tige</text><text x="420" y="80">tige (1)</text></g><g font-size="11" font-weight="700" text-anchor="middle" fill="#0f6e56" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="125" y="104">chambre arrière</text><text x="280" y="76">chambre avant</text></g></svg>
:::

Le vérin ne se réduit pas à son piston. Trois familles de pièces l'entourent, et chacune a une raison d'être :

| Famille                | Repères de la nomenclature                   | Rôle                                                                    |
| ---------------------- | -------------------------------------------- | ----------------------------------------------------------------------- |
| **Guidage**            | bagues de guidage (59), (65), en bronze      | guider la tige en translation sur une portée d'usure remplaçable        |
| **Amortissement**      | bagues d'amortissement avant (53), arrière (58) | freiner le piston à l'approche de la fin de course                   |
| **Maintien du corps**  | 4 tirants M6 (54), 4 écrous (56), 4 rondelles (57) | serrer le fond et le nez contre les deux extrémités du tube        |

::: propriete Étanchéité statique, étanchéité dynamique
- Une étanchéité est **statique** quand les deux surfaces qu'elle sépare **ne bougent pas** l'une par rapport à l'autre : c'est le rôle des **joints toriques** (66), (67), (68), simplement serrés entre deux pièces assemblées.
- Elle est **dynamique** quand une surface **glisse** contre l'autre : le **joint de piston** (64) entre le piston et le tube, le **joint de tige** (61) autour de la tige qui coulisse, et le **joint racleur** (60), qui **essuie la tige** à chaque rentrée pour que poussières et projections n'entrent pas dans le vérin.
:::

> ⚠️ Le joint de piston et le joint de tige se confondent facilement. Le **joint de piston** empêche l'air de passer **d'une chambre à l'autre** ; le **joint de tige** empêche l'air de **sortir du vérin** le long de la tige. Deux fuites différentes, deux joints différents.

À pression égale, l'effort **en sortie** de tige est plus grand qu'en **rentrée** : côté fond, l'air pousse sur **tout** le disque du piston ; côté tige, il ne pousse plus que sur une **couronne**, la section de la tige étant retranchée.

## ⚡ Faire passer le courant là où il faut

Une pince de soudage fait circuler un courant de **forte intensité**. Ce courant doit traverser **les tôles**, et elles seules : s'il trouvait un chemin par la structure, l'électrode E1 et l'électrode E2 seraient court-circuitées et le point ne se formerait pas. D'où une famille de pièces qu'on ne trouve dans aucune autre machine du thème : les **isolants**.

Les **rondelles isolantes** (11) Ø20xØ75x2, les **bagues isolantes** (12) et (13), les **isolants** (31), (33), (35) et les **tubes** (34) sont en **Nylatron** et en **Bakélite** — deux matières plastiques **isolantes**. Elles s'intercalent à chaque articulation entre les deux bras, et **coupent électriquement** ce que la mécanique doit laisser assemblé.

::: figure L'empilage se lit dans les désignations : l'axe fait Ø20, la bague frittée va de Ø20 à Ø24, la bague isolante de Ø24 à Ø30 — chaque diamètre extérieur est le diamètre intérieur du suivant
<svg viewBox="0 0 340 260"><circle cx="120" cy="130" r="60" fill="#fde68a" stroke="#0f172a" stroke-width="2"/><circle cx="120" cy="130" r="48" fill="#c98a3a" stroke="#0f172a" stroke-width="2"/><circle cx="120" cy="130" r="40" fill="#94a3b8" stroke="#0f172a" stroke-width="2"/><path d="M80 130 H160" fill="none" stroke="#0f172a" stroke-width="1.2"/><g fill="#0f172a"><polygon points="80,130 90,126 90,134"/><polygon points="160,130 150,126 150,134"/></g><g fill="none" stroke="#0f172a" stroke-width="1"><path d="M162 88 L232 52"/><path d="M165 114 L232 92"/><path d="M79 115 L34 84"/><path d="M70 150 L30 190"/><path d="M120 170 V212"/></g><g font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="120" y="126" text-anchor="middle">Ø20</text><text x="236" y="48">Ø30</text><text x="236" y="88">Ø24</text><text x="30" y="80" text-anchor="end">(30)</text><text x="26" y="194" text-anchor="end">(12)</text><text x="120" y="226" text-anchor="middle">(14)</text></g></svg>
:::

::: exemple Vérifier un empilage sur la seule nomenclature
« Axe Ø20x80 » (14) · « Bague frittée 20x24x20 » (30) · « Bague isolante Ø24xØ30x20 » (12).
L'axe fait 20 ; la bague frittée a un **alésage de 20** — elle s'enfile dessus ✓ — et un **extérieur de 24** ; la bague isolante a un **alésage de 24** — elle s'enfile sur la précédente ✓. Les **longueurs concordent** aussi : 20 et 20. Et le couple court se lit pareil : bague frittée 20x24x**12** (32) avec bague isolante Ø24xØ30x**12** (13).
:::

> 🗡️ La bague **frittée** assure le **guidage** (c'est un coussinet), la bague **isolante** assure la **coupure électrique**. Deux fonctions, deux pièces, l'une dans l'autre : c'est exactement ce que la lecture analytique doit savoir séparer.

## 🔗 Le pivot du bras : deux bagues, deux paliers, MIP et MAP

Le **bras (6)** pivote sur le **tourillon avant du vérin (2)**. Cette liaison **pivot** n'est pas obtenue par une bague unique, mais par **deux bagues de guidage (69) et (69')**, en bronze Cu Sn 8 Pb 2, logées dans **deux paliers rapportés** — le **palier arrière (21)** et le **palier avant (70)** — eux-mêmes **encastrés** sur le bras.

::: propriete Pourquoi deux appuis, et pourquoi écartés
Deux bagues **écartées** définissent l'axe du pivot et empêchent le bras de **basculer** autour de lui. Une bague unique, si longue soit-elle, laisse toujours un débattement angulaire. Et le **bronze** joue le rôle du coussinet : c'est la pièce **tendre et remplaçable** qui s'use à la place de l'axe et du logement.
:::

L'encastrement des paliers sur le bras est réalisé par **deux vis CHC M8x75 (71)** et **deux goupilles de positionnement 8x90 (72)**. Ce n'est pas un doublon : ce sont **deux fonctions différentes**.

::: definition Mise en position et maintien en position
- **MIP — mise en position** : donner à la pièce sa position exacte, et la lui redonner à l'identique après chaque démontage. C'est le rôle des **goupilles de positionnement**, cylindres pleins **ajustés** dans des alésages précis.
- **MAP — maintien en position** : presser les pièces l'une contre l'autre pour qu'elles ne bougent plus. C'est le rôle des **vis**, qui créent l'**adhérence** par serrage.
:::

::: figure Deux fixations, deux métiers : à gauche la vis, dont la tête serre dans son lamage ; à droite la goupille, cylindre plein sans tête ni filetage, qui ne serre rien mais impose la position
<svg viewBox="0 0 360 220"><g fill="#0f6e56" opacity="0.10"><rect x="24" y="132" width="312" height="64"/><rect x="48" y="72" width="264" height="60"/></g><path d="M24.0 186.0 L34 196 M24.0 176.0 L44 196 M24.0 166.0 L54 196 M24.0 156.0 L64 196 M24.0 146.0 L74 196 M24.0 136.0 L84 196 M30 132 L94 196 M40 132 L104 196 M50 132 L114 196 M60 132 L124 196 M70 132 L134 196 M80 132 L144 196 M90 132 L154 196 M100 132 L164 196 M110 132 L174 196 M120 132 L184 196 M130 132 L194 196 M140 132 L204 196 M150 132 L214 196 M160 132 L224 196 M170 132 L234 196 M180 132 L244 196 M190 132 L254 196 M200 132 L264 196 M210 132 L274 196 M220 132 L284 196 M230 132 L294 196 M240 132 L304 196 M250 132 L314 196 M260 132 L324 196 M270 132 L334 196 M280 132 L336 188 M290 132 L336 178 M300 132 L336 168 M310 132 L336 158 M320 132 L336 148 M330 132 L336 138" fill="none" stroke="#0f172a" stroke-width="0.9"/><path d="M48.0 82.0 L58.0 72.0 M48.0 92.0 L68.0 72.0 M48.0 102.0 L78.0 72.0 M48.0 112.0 L88.0 72.0 M48.0 122.0 L98.0 72.0 M48.0 132.0 L108.0 72.0 M58.0 132.0 L118.0 72.0 M68.0 132.0 L128.0 72.0 M78.0 132.0 L138.0 72.0 M88.0 132.0 L148.0 72.0 M98.0 132.0 L158.0 72.0 M108.0 132.0 L168.0 72.0 M118.0 132.0 L178.0 72.0 M128.0 132.0 L188.0 72.0 M138.0 132.0 L198.0 72.0 M148.0 132.0 L208.0 72.0 M158.0 132.0 L218.0 72.0 M168.0 132.0 L228.0 72.0 M178.0 132.0 L238.0 72.0 M188.0 132.0 L248.0 72.0 M198.0 132.0 L258.0 72.0 M208.0 132.0 L268.0 72.0 M218.0 132.0 L278.0 72.0 M228.0 132.0 L288.0 72.0 M238.0 132.0 L298.0 72.0 M248.0 132.0 L308.0 72.0 M258.0 132.0 L312 78.0 M268.0 132.0 L312 88.0 M278.0 132.0 L312 98.0 M288.0 132.0 L312 108.0 M298.0 132.0 L312 118.0 M308.0 132.0 L312 128.0" fill="none" stroke="#0f172a" stroke-width="0.9"/><g fill="none" stroke="#0f172a" stroke-width="2"><rect x="24" y="132" width="312" height="64"/><rect x="48" y="72" width="264" height="60"/></g><g fill="#e2e8f0" stroke="#0f172a" stroke-width="2"><rect x="88" y="72" width="24" height="22"/><rect x="94" y="94" width="12" height="38"/><rect x="94" y="132" width="12" height="46"/></g><rect x="94" y="76" width="12" height="10" fill="#0f172a"/><g fill="none" stroke="#0f172a" stroke-width="1"><path d="M94 138 L106 142 M94 146 L106 150 M94 154 L106 158 M94 162 L106 166 M94 170 L106 174"/></g><rect x="232" y="72" width="16" height="112" fill="#e2e8f0" stroke="#0f172a" stroke-width="2"/><g fill="none" stroke="#0f172a" stroke-width="1.4"><path d="M232 78 L238 72 M248 78 L242 72 M232 178 L238 184 M248 178 L242 184"/></g><g font-size="14" font-weight="700" text-anchor="middle" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="100" y="62">1</text><text x="240" y="62">2</text><text x="176" y="108">palier (21)</text><text x="176" y="170">bras (6)</text></g></svg>
:::

> ⚠️ Une goupille ne serre pas et une vis ne positionne pas. Une vis traverse toujours un trou **de passage** un peu plus large qu'elle — sinon on ne pourrait pas la monter ; c'est ce jeu qui rend une **goupille** indispensable dès qu'on veut retrouver la position exacte au remontage.

Sur le même bras, un autre sous-ensemble règle l'**écartement des électrodes** : une **vis H M10x60 (41)** et une **vis HC M10x70 à bout bombé (43)** viennent en butée contre les **pastilles de butée (40) et (45)**, en acier STUB, **montées serrées**. Chaque vis se bloque à la position voulue par un **écrou HM M10 (42)** qui fait **contre-écrou**. La pastille, dure et remplaçable, **matérialise la butée** et encaisse le matage à la place du bras.

## 🧰 Préparer l'intervention : le filogramme

Une défectuosité déclenche le **changement des deux bagues de guidage (69)** du tourillon (2) avec le bras (6). Avant de toucher un outil, on écrit le **graphe de démontage**, dit **filogramme** : une colonne verticale portant le **repère d'ordre**, sur laquelle se détachent les pièces déposées, avec l'**outillage** de chaque opération.

::: figure Le filogramme descend du repère d'ordre 1 jusqu'au sous-ensemble restant ; la branche 2 se subdivise, parce qu'une fois les goupilles chassées, il faut déposer chaque palier avant d'extraire sa bague
<svg viewBox="0 0 476 310"><g font-size="10" font-weight="700" fill="#0f6e56"><text x="4" y="14">Repère</text><text x="4" y="27">d'ordre</text><text x="372" y="30">Outillage</text></g><rect x="120" y="8" width="140" height="28" rx="4" fill="#0f6e56" opacity="0.16"/><rect x="120" y="8" width="140" height="28" rx="4" fill="none" stroke="#0f172a" stroke-width="2"/><path d="M190 36 V272" fill="none" stroke="#0f172a" stroke-width="2"/><g fill="none" stroke="#0f172a" stroke-width="2"><path d="M190 64 H228"/><path d="M190 104 H228"/><path d="M260 118 V246"/><path d="M260 140 H298"/><path d="M260 176 H298"/><path d="M260 212 H298"/><path d="M260 246 H298"/></g><g fill="#0f172a"><polygon points="238,64 228,59 228,69"/><polygon points="238,104 228,99 228,109"/><polygon points="308,140 298,135 298,145"/><polygon points="308,176 298,171 298,181"/><polygon points="308,212 298,207 298,217"/><polygon points="308,246 298,241 298,251"/></g><g fill="#bfdbfe" stroke="#0f172a" stroke-width="2"><rect x="238" y="50" width="44" height="28" rx="4"/><rect x="238" y="90" width="44" height="28" rx="4"/><rect x="308" y="126" width="52" height="28" rx="4"/><rect x="308" y="162" width="52" height="28" rx="4"/><rect x="308" y="198" width="52" height="28" rx="4"/><rect x="308" y="232" width="52" height="28" rx="4"/></g><rect x="116" y="274" width="148" height="28" rx="4" fill="#0f6e56" opacity="0.16"/><rect x="116" y="274" width="148" height="28" rx="4" fill="none" stroke="#0f172a" stroke-width="2"/><g font-size="11" font-weight="700" text-anchor="middle" fill="#0f172a"><text x="190" y="27">Pince de soudage</text><text x="260" y="69">71</text><text x="260" y="109">72</text><text x="334" y="145">70 + 69</text><text x="334" y="181">69</text><text x="334" y="217">21 + 69'</text><text x="334" y="251">69'</text><text x="190" y="293">Sous-ensemble restant</text></g><g font-size="11" font-weight="700" text-anchor="end" fill="#0f6e56"><text x="184" y="60">1</text><text x="184" y="100">2</text><text x="254" y="136">2.1</text><text x="254" y="172">2.2</text><text x="254" y="208">2.3</text><text x="254" y="242">2.4</text></g><g font-size="9" fill="#0f172a"><text x="372" y="68">Clé à six pans</text><text x="372" y="108">Chasse-goupille</text><text x="372" y="144">Manuelle</text><text x="372" y="180">Extracteur</text><text x="372" y="216">Manuelle</text><text x="372" y="250">Extracteur</text></g></svg>
:::

L'outillage n'est pas décoratif — il **révèle le montage** :

| Outillage                | Opération                                       | Ce que l'outil dit                                         |
| ------------------------ | ----------------------------------------------- | ---------------------------------------------------------- |
| Clé à six pans           | déposer les deux vis (71)                       | ce sont des vis **CHC**, à six pans **creux**              |
| Chasse-goupille          | déposer les deux goupilles (72)                 | la goupille est **ajustée**, elle se chasse                |
| Manuelle                 | déposer le palier (70), puis le palier (21)     | rien ne les retient une fois vis et goupilles ôtées        |
| Extracteur de coussinet  | déposer la bague (69), puis la bague (69')      | la bague est **montée serrée** : il faut un effort         |

::: propriete La règle d'or du remontage
Le **montage reprend le démontage à l'envers** : la dernière pièce déposée est la première remontée. Le graphe de montage se dessine en **râteau** — une progression sur laquelle chaque composant vient se greffer dans l'ordre.
:::

## 📏 Cotation fonctionnelle : poser une condition, puis la vérifier

::: definition Le but de la cotation fonctionnelle
Un mécanisme est constitué de nombreuses pièces. Pour qu'il puisse fonctionner correctement, certaines **conditions** doivent être respectées — **jeux, dépassements, serrages**. La cotation fonctionnelle a pour but de définir les **cotes nominales** et les **IT** (intervalles de tolérance) de chaque pièce afin que ces conditions soient respectées, donc d'assurer l'**interchangeabilité** des pièces, et de **minimiser les coûts de fabrication** en donnant les tolérances **les plus larges possibles**.
:::

L'interchangeabilité n'est pas une élégance de bureau d'études : c'est du **temps d'intervention**. Si les bagues (69) sont cotées correctement, la bague de rechange sortie du magasin se monte **sans retouche, sans réglage, sans essai** — et la pince repart. Sinon, l'intervention devient un ajustage.

Une condition ne tient jamais à une seule pièce : elle se **ferme** sur une **chaîne de cotes**, avec **une seule cote par pièce traversée**. Une cote parcourue **dans le sens de la condition** est **positive**, une cote parcourue **en sens inverse** est **négative**.

::: figure La condition Ja se referme sur quatre pièces : on part d'une face du bras, on traverse une bague, le tourillon, l'autre bague, et on arrive sur l'autre face du bras — le jeu et les collerettes sont volontairement exagérés, sinon on ne les verrait pas
<svg viewBox="0 0 440 300"><g fill="#0f6e56" opacity="0.10"><rect x="40" y="44" width="30" height="150"/><rect x="364" y="44" width="30" height="150"/><rect x="40" y="194" width="354" height="30"/></g><path d="M40.0 185.0 L49 194 M40.0 176.0 L58 194 M40.0 167.0 L67 194 M40.0 158.0 L70 188 M40.0 149.0 L70 179 M40.0 140.0 L70 170 M40.0 131.0 L70 161 M40.0 122.0 L70 152 M40.0 113.0 L70 143 M40.0 104.0 L70 134 M40.0 95.0 L70 125 M40.0 86.0 L70 116 M40.0 77.0 L70 107 M40.0 68.0 L70 98 M40.0 59.0 L70 89 M40.0 50.0 L70 80 M43 44 L70 71 M52 44 L70 62 M61 44 L70 53" fill="none" stroke="#0f172a" stroke-width="0.9"/><path d="M364.0 185.0 L373 194 M364.0 176.0 L382 194 M364.0 167.0 L391 194 M364.0 158.0 L394 188 M364.0 149.0 L394 179 M364.0 140.0 L394 170 M364.0 131.0 L394 161 M364.0 122.0 L394 152 M364.0 113.0 L394 143 M364.0 104.0 L394 134 M364.0 95.0 L394 125 M364.0 86.0 L394 116 M364.0 77.0 L394 107 M364.0 68.0 L394 98 M364.0 59.0 L394 89 M364.0 50.0 L394 80 M367 44 L394 71 M376 44 L394 62 M385 44 L394 53" fill="none" stroke="#0f172a" stroke-width="0.9"/><path d="M40.0 215.0 L49 224 M40.0 206.0 L58 224 M40.0 197.0 L67 224 M46 194 L76 224 M55 194 L85 224 M64 194 L94 224 M73 194 L103 224 M82 194 L112 224 M91 194 L121 224 M100 194 L130 224 M109 194 L139 224 M118 194 L148 224 M127 194 L157 224 M136 194 L166 224 M145 194 L175 224 M154 194 L184 224 M163 194 L193 224 M172 194 L202 224 M181 194 L211 224 M190 194 L220 224 M199 194 L229 224 M208 194 L238 224 M217 194 L247 224 M226 194 L256 224 M235 194 L265 224 M244 194 L274 224 M253 194 L283 224 M262 194 L292 224 M271 194 L301 224 M280 194 L310 224 M289 194 L319 224 M298 194 L328 224 M307 194 L337 224 M316 194 L346 224 M325 194 L355 224 M334 194 L364 224 M343 194 L373 224 M352 194 L382 224 M361 194 L391 224 M370 194 L394 218 M379 194 L394 209 M388 194 L394 200" fill="none" stroke="#0f172a" stroke-width="0.9"/><path d="M40 44 H70 V194 H364 V44 H394 V224 H40 Z" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><g fill="#0f6e56" opacity="0.35"><rect x="70" y="72" width="12" height="94"/><rect x="46" y="90" width="24" height="58"/><rect x="352" y="72" width="12" height="94"/><rect x="364" y="90" width="24" height="58"/></g><g fill="none" stroke="#0f172a" stroke-width="2"><path d="M82 72 H70 V90 H46 V148 H70 V166 H82"/><path d="M352 72 H364 V90 H388 V148 H364 V166 H352"/><path d="M82 72 V166"/><path d="M352 72 V166"/></g><rect x="82" y="56" width="250" height="126" fill="#bfdbfe" stroke="#0f172a" stroke-width="2"/><path d="M20 119 H414" fill="none" stroke="#94a3b8" stroke-width="1" stroke-dasharray="14 3 3 3"/><g fill="none" stroke="#0f6e56" stroke-width="2.5"><path d="M332 56 V72"/><path d="M352 56 V72"/></g><g fill="none" stroke="#0f172a" stroke-width="1"><path d="M82 182 V250"/><path d="M332 182 V250"/><path d="M70 224 V274"/><path d="M364 224 V274"/></g><g fill="none" stroke="#0f172a" stroke-width="1.2"><path d="M88 244 H326"/><path d="M76 268 H358"/></g><g fill="#0f172a"><polygon points="82,244 92,240 92,248"/><polygon points="332,244 322,240 322,248"/><polygon points="70,268 80,264 80,272"/><polygon points="364,268 354,264 354,272"/></g><g fill="none" stroke="#0f172a" stroke-width="1"><path d="M76 72 V30 H44"/><path d="M358 72 V30 H392"/></g><g font-size="13" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="207" y="240" text-anchor="middle">a2</text><text x="217" y="264" text-anchor="middle">a6</text><text x="40" y="34" text-anchor="end">a69</text><text x="396" y="34">a69'</text><text x="342" y="48" text-anchor="middle" fill="#0f6e56">Ja</text></g><g font-size="12" font-weight="700" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="207" y="124" text-anchor="middle">(2)</text><text x="217" y="213" text-anchor="middle">(6)</text><text x="58" y="124" text-anchor="middle">(69)</text><text x="376" y="124" text-anchor="middle">(69')</text></g></svg>
:::

$$ Ja = a6 − a2 − a69 − a69' $$

::: propriete Les trois formules, et l'ordre dans lequel on s'en sert
$$ Ja maxi = Σ(cotes +) maxi − Σ(cotes −) mini $$
$$ Ja mini = Σ(cotes +) mini − Σ(cotes −) maxi $$
$$ IT(Ja) = somme de TOUS les IT de la chaîne = Ja maxi − Ja mini $$
Les tolérances **s'ajoutent**, elles ne se compensent jamais. On calcule donc **l'IT d'abord** : il dit tout de suite si la condition est **réalisable**.
:::

::: methode Vérifier une condition déjà cotée
Poser une condition et **vérifier** une condition sont deux exercices différents. Vérifier, c'est répondre à une question fermée : *les cotes existantes garantissent-elles la condition ?* On procède en trois temps.

1. **Comparer les IT.** Si IT(chaîne) > IT(condition), la condition est **impossible** quelles que soient les valeurs nominales : aucun déplacement du nominal ne rattrapera un intervalle trop large. Il faut **resserrer** au moins une cote.
2. Si l'IT passe, **calculer Ja maxi et Ja mini** avec les deux formules croisées.
3. **Conclure** en confrontant l'intervalle [Ja mini ; Ja maxi] obtenu à l'intervalle exigé. Les **deux** bornes doivent tenir : un jeu qui reste positif mais devient trop grand est un **échec**, exactement comme un jeu qui devient négatif.
:::

::: exemple Une condition qui ne passe pas
On exige 0 ≤ Ja ≤ 0,2 avec a6 = 57,40 ± 0,05 · a2 = 54 ± 0,02 · a69 = a69' = 1,60 ± 0,02.
IT(chaîne) = 0,10 + 0,04 + 0,04 + 0,04 = **0,22**, alors que IT(condition) = 0,20 − 0 = **0,20**.
0,22 > 0,20 ⇒ la condition est **impossible** telle quelle. On le confirme par les extrêmes :
Ja maxi = 57,45 − 53,98 − 1,58 − 1,58 = **0,31** ✓ (> 0,2 : trop de jeu)
Ja mini = 57,35 − 54,02 − 1,62 − 1,62 = **0,09** ✓ (≥ 0 : celle-là passe)
Il faut **gagner au moins 0,02 mm** sur la somme des IT — par exemple en cotant le bras a6 = 57,30 ± 0,02, ce qui donne alors Ja maxi = 0,18 et Ja mini = 0,02.
:::

> ⚠️ Le piège de cet exercice : constater que Ja mini vaut 0,09, se dire « le jeu reste positif, donc les pièces ne coincent pas », et conclure que tout va bien. **Une condition a deux bornes.** 0,31 mm de jeu maximal viole la limite haute aussi sûrement qu'un jeu négatif violerait la limite basse.

## ✏️ Le dessin de définition : cote, spécification, état de surface

::: definition Le dessin de définition
Il représente **une seule pièce** d'un ensemble ou d'un sous-ensemble, et la définit **complètement et sans ambiguïté**. Il prépare sa fabrication par cinq informations : la **matière**, la **forme**, la **cotation dimensionnelle**, les **spécifications géométriques** et la **qualité de l'état des surfaces**. Pour montrer les parties intérieures, on emploie les **coupes** et les **sections**.
:::

Le **palier arrière (21)** de la pince en est l'exemple complet. On y lit quatre langages différents, qu'il ne faut jamais confondre :

| Ce qu'on lit          | De quoi il s'agit                  | Comment ça se lit                                                                       |
| --------------------- | ---------------------------------- | ---------------------------------------------------------------------------------------- |
| **15 ± 0,02**         | cotation **dimensionnelle**        | une longueur et sa tolérance, en millimètres                                             |
| **Ø28 H7**, **Ø8 H7** | cotation dimensionnelle **ISO**    | un **alésage** (lettre **majuscule** H) de qualité 7 ; H ⇒ écart inférieur **nul**       |
| **⊥ 0,1 A**           | **spécification géométrique**      | un cadre à trois cases : symbole, valeur en mm, surface de référence                     |
| **Ra 1,6**            | **état de surface**                | rugosité arithmétique moyenne au plus égale à **1,6 micromètre**                         |

::: figure Un cadre de tolérance se lit toujours de gauche à droite en trois cases — ici : perpendicularité, 0,1 mm, par rapport à la surface A que le triangle noir désigne sur la pièce
<svg viewBox="0 0 380 210"><g fill="#0f6e56" opacity="0.10"><rect x="40" y="80" width="190" height="60"/></g><rect x="40" y="80" width="190" height="60" fill="none" stroke="#0f172a" stroke-width="2"/><circle cx="140" cy="110" r="22" fill="#ffffff" stroke="#0f172a" stroke-width="2"/><path d="M140 62 V158" fill="none" stroke="#0f172a" stroke-width="1" stroke-dasharray="12 3 3 3"/><polygon points="180,140 173,152 187,152" fill="#0f172a"/><path d="M180 152 V164" fill="none" stroke="#0f172a" stroke-width="1.4"/><rect x="166" y="164" width="28" height="22" fill="#ffffff" stroke="#0f172a" stroke-width="1.6"/><text x="180" y="180" font-size="13" font-weight="700" text-anchor="middle" fill="#0f172a">A</text><g fill="#ffffff" stroke="#0f172a" stroke-width="1.6"><rect x="250" y="40" width="30" height="26"/><rect x="280" y="40" width="42" height="26"/><rect x="322" y="40" width="30" height="26"/></g><g fill="none" stroke="#0f172a" stroke-width="2"><path d="M265 46 V60"/><path d="M257 60 H273"/></g><g font-size="13" font-weight="700" text-anchor="middle" fill="#0f172a"><text x="301" y="59">0,1</text><text x="337" y="59">A</text></g><path d="M250 53 H140 V62" fill="none" stroke="#0f172a" stroke-width="1"/><g fill="none" stroke="#0f172a" stroke-width="1"><path d="M265 66 V78"/><path d="M301 66 V92"/><path d="M337 66 V78"/><path d="M118 110 H112"/></g><g font-size="10" fill="#0f6e56" font-weight="700" text-anchor="middle"><text x="265" y="90">symbole</text><text x="301" y="104">tolérance (mm)</text><text x="337" y="90">référence</text></g><text x="108" y="114" font-size="12" font-weight="700" text-anchor="end" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round">Ø28 H7</text></svg>
:::

Le palier porte aussi des **chanfreins**, notés **1,5 × 45°** et **5 × 45°** : une **largeur** en millimètres suivie d'un **angle**. Un chanfrein **abat l'arête vive** laissée par l'usinage et **facilite l'engagement** de la pièce qui vient s'y emmancher.

::: retenir La cote fonctionnelle se reconnaît à sa tolérance
Chaque cote d'une chaîne se **reporte sur le dessin de définition de sa propre pièce** — jamais la condition, qui ne se fabrique pas. Sur un dessin, la cote issue de la chaîne est presque toujours **la plus serrée** : les cotes libres du palier arrière sont à ± 0,2, ses cotes d'usinage courantes à ± 0,05, et sa cote fonctionnelle à **± 0,02**.
:::

Et pour montrer l'intérieur sans encombrer le dessin, le répertoire est celui que tu connais : la **demi-coupe** pour les pièces **symétriques** (intérieur et extérieur dans une même vue), la **coupe à plans parallèles** (un trait d'axe marque le changement de plan), la **coupe brisée à plans sécants** (la partie non alignée pivote et se voit en **vraie grandeur**), et les **sections** — **sortie** à l'extérieur de la vue, **rabattue** en **trait fin** sur la vue elle-même — qui ne montrent **que la matière coupée**.

Enfin, la **modélisation numérique** : on crée l'objet **3D** par **ajout**, **soustraction** et **modification** de ses constituants dans un logiciel de modélisation, et l'on en tire ensuite la représentation **2D**. Le palier arrière (21) est justement la pièce que le manuel demande de modéliser — et il est le seul entièrement coté, ce n'est pas un hasard : on ne modélise bien que ce qui est défini sans ambiguïté.

> 🏆 Tu viens de lire une machine de 72 repères sans jamais la voir en vrai : son procédé, son actionneur, ses isolants, son pivot, son démontage, ses cotes et ses spécifications. Un dessin d'ensemble ne t'oppose plus sa taille — il t'oppose seulement des questions, et tu sais dans quel ordre les poser.
