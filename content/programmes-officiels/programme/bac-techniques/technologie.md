# Technologie (Génie mécanique) — Baccalauréat Sciences techniques · programme officiel CNP

> **Sources** (voir README § « Sources officielles combinées ») :
>
> - **Guide enseignant** (programme) : **aucun au corpus CNP pour ce couple.** Le catalogue des
>   346 PDF ne contient, pour la matière 28 (technologie) en 4ème année secondaire, que des
>   manuels d'activités destinés à l'élève — aucun guide méthodologique / dossier pédagogique.
>   **Conséquence assumée** : le manuel élève fait référence, et la fiche ne peut pas citer de
>   compétence terminale ni de progression trimestrielle « officielle » autres que celles que le
>   manuel affiche lui-même (§1).
> - **Manuel élève** (contenu/exemples/exercices) : `228462P01.pdf` + `228462P02.pdf` —
>   « TECHNOLOGIE — Génie mécanique — Manuel d'activités — 4ème année Sciences Techniques »,
>   République Tunisienne, Ministère de l'Éducation, Centre National Pédagogique.
>   **288 pages imprimées**, pagination **continue** sur les deux tomes : tome 1 = p.1–144,
>   tome 2 = p.145–288. **Pages lues** : voir le registre `suivi/bac-techniques.json` (la fiche
>   ne redéclare pas ce que le registre calcule).
>
> **Transcrit le** : 2026-09-06. **Statut** : transcription fidèle (source unique — manuel élève).
> **Langue d'enseignement** : `fr`. **gradeSlug** : `bac-techniques`.
> **subject id** attendu : `technologie-bac-techniques`.

> ⚠️ **Ce que cette fiche NE couvre PAS.** La technologie du bac Sciences techniques se partage
> en deux spécialités, et le corpus CNP porte les deux : le **génie mécanique** (228462, ici) et
> le **génie électrique** (`228461P01/P02/P03`, 3 tomes, ≈ 122 Mo). Le génie électrique n'est
> **pas** revendiqué par cette fiche et reste libre pour une autre session — R-4 n'autorisant
> qu'une fiche par code source, le laisser non réclamé est ce qui permet de l'ouvrir sans
> collision. Toute génération issue de cette fiche ne couvre donc que la moitié « génie
> mécanique » de la matière.

## 1. Cadre & compétences (les objectifs généraux)

Le manuel n'étant accompagné d'aucun guide enseignant au corpus, le cadre transcrit ci-dessous
est celui que le manuel affiche lui-même (Introduction p.6–7, Carte du manuel p.8–11).

### 1.1 Enjeux du curriculum de la discipline (p.6, verbatim)

> Les principaux enjeux du curriculum de la discipline sont :
>
> - L'activité de l'apprenant soit fondamentale ;
> - Le savoir devient un construit et non plus un donné ;
> - Les apprentissages seront motivants et significatifs ;
> - Les apprentissages disciplinaires seront orientés vers des acquis fonctionnels ;
> - Les valeurs sociétales et humanistes et les intelligences de l'apprenant participent au
>   développement des compétences de vie.

Le manuel précise sa propre place (p.6) : il « constitue un cadre de référence pour la formation
dans la discipline technologie », « est conçu de façon à respecter la progression des
apprentissages et les thèmes du curriculum de technologie en quatrième année sciences techniques
de génie mécanique », et propose « une combinaison de connaissances et de compétences dans la
spécialité de génie mécanique ».

### 1.2 Les trois compétences disciplinaires (p.8, verbatim)

| Code    | Compétence disciplinaire                                                                              |
| ------- | ------------------------------------------------------------------------------------------------------ |
| **CD1** | S'approprier des connaissances et des habiletés pour résoudre des problèmes d'ordre scientifique et technologique. |
| **CD2** | Mobiliser ses connaissances et ses habiletés pour concevoir, créer et réaliser des produits technologiques. |
| **CD3** | Communiquer à l'aide de textes, codes et langages scientifiques et technologiques.                     |

⚠️ **Notation à connaître pour lire la suite de la fiche** : chaque page d'activité du manuel
affiche, dans un bandeau en haut à gauche, les compétences visées sous la forme **`CD 1.3`,
`CD 2.3`, `CD 1.9`** — c'est-à-dire la compétence disciplinaire suivie du numéro de sa
**composante**. Le manuel **n'imprime nulle part la liste de ces composantes numérotées** : ni la
carte du manuel (p.8–11), ni l'introduction ne les détaillent. Les codes sont donc transcrits
**tels qu'affichés**, sans être développés — les développer serait une invention (§6).

### 1.3 Les trois axes du manuel

Les **intitulés** sont ceux de la carte du manuel (p.8), verbatim. La colonne « pages » n'y figure
pas : elle est **déduite du sommaire (p.4–5)** et confirmée par les en-têtes courants — elle est
donnée ici parce qu'elle sert, pas parce que la source l'imprime.

| Axe       | Intitulé (verbatim p.8)              | Pages (déduites du sommaire) |
| --------- | ------------------------------------ | ---------------------------- |
| **AXE 1** | L'analyse fonctionnelle              | 12–40                        |
| **AXE 2** | L'analyse structurelle et conception | 41–251                       |
| **AXE 3** | La réalisation et la production      | 252–288                      |

> En cohérence avec le curriculum de la discipline, le manuel considère que l'observation, le
> questionnement, l'expérimentation et l'argumentation sont essentiels dans l'apprentissage de la
> technologie. (p.8)

### 1.4 Compétences de vie (p.10–11)

Le manuel adosse aux activités un référentiel de **compétences de vie** en quatre dimensions,
signalées par des logos dans les activités. Transcription des **quatre tableaux** de la p.10 (un par dimension), réunis ici en un seul par ajout d'une colonne « Dimension ». Titre imprimé de la page : « Légende des compétences de vie et les éducations à… » :

| Dimension          | Compétences essentielles                          | Compétences associées (verbatim)                                                                                                                                                                                                            |
| ------------------ | ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Cognitive**      | Créativité                                        | Pensée novatrice, pensée divergente, formulation des idées, analyse et synthèse, capacité d'agir…                                                                                                                                            |
| **Cognitive**      | Pensée critique                                   | Compétences métacognitives (penser à réfléchir/réfléchir à la pensée), questionnement, interprétation de l'information et synthèse, l'écoute, l'autoprotection, la responsabilité sociale…                                                  |
| **Cognitive**      | Résolution de problèmes                           | Curiosité, attention, pensée analytique, engagement actif…                                                                                                                                                                                  |
| **Instrumentale**  | Coopération                                       | Travail d'équipe pour atteindre des objectifs communs, collaboration dans le lieu de travail, respect des autres…                                                                                                                            |
| **Instrumentale**  | Négociation                                       | Capacités d'influence et de leadership, coopération, relation avec la clientèle, planification de carrière, communication efficace…                                                                                                          |
| **Instrumentale**  | Prise de décisions                                | Planification d'actions, établissement d'objectifs, compétences de leadership, prise de risques, compétences en matière de sûreté, raisonnement éthique…                                                                                     |
| **Personnelle**    | Autogestion                                       | Auto-efficacité, établissement d'objectifs, planification de vie, autonomie, capacité d'agir, auto-assistance, motivation…                                                                                                                   |
| **Personnelle**    | Résilience                                        | Cran, détermination, contrôle du stress, adaptabilité, auto-efficacité, auto-développement, capacité d'agir, régulation émotionnelle et comportementale, adaptation à l'adversité, préparation aux urgences…                               |
| **Personnelle**    | Communication                                     | Gestion des relations, réalisation personnelle, auto-présentation, écoute active, communication, empathie bidirectionnelle, affirmation de soi appropriée…                                                                                   |
| **Sociale**        | Respect de la diversité                           | Tolérance active et interaction sociale, estime de soi, maîtrise de soi, pensée analytique, écoute active…                                                                                                                                   |
| **Sociale**        | Empathie                                          | Compréhension des autres, intérêt pour les autres, identification des comportements abusifs et non abusifs, comportement altruiste, gestion de conflits, résolution de conflits, compréhension et gestion de ses émotions…                  |
| **Sociale**        | Participation                                     | Dialogue, écoute active, pensée analytique et critique, confiance en soi, capacité d'agir                                                                                                                                                    |

La roue p.11 regroupe ces douze compétences en quatre finalités : **APPRENTISSAGE** (créativité,
pensée critique, résolution des problèmes), **EMPLOYABILITÉ** (coopération, négociation, prise de
décisions), **DÉVELOPPEMENT PERSONNEL** (communication, résilience, autogestion) et **CITOYENNETÉ
ACTIVE** (participation, empathie, respect de la diversité). Les sigles imprimés dans les logos
sont : CREA, CRITI, R.PRO, COOP, NEGO, DECI, A.GES, RESI, COMM, PARTI, EMPA, DIVER.

> **Remarque:** L'indication des logos des compétences de vie dans les activités, signifie que
> l'apprenant est amené à les développer soit en autonomie, soit à travers des activités
> collectives. (p.11)

## 2. Plan annuel — thèmes, activités et contenus transcrits

Ce qui suit est la transcription du manuel, thème par thème et **activité par activité**, dans
l'ordre des pages. Chaque activité est restituée avec son support, ses ressources, ses données
chiffrées et son travail demandé question par question ; les encadrés officiels sont en citation.

### AXE 1 — L'analyse fonctionnelle (p.12–40)

#### Thème : Analyse fonctionnelle interne d'un produit (p.12–40)

**Page d'ouverture (p.12).** Bandeaux successifs imprimés en tête de page :

> **AXE 1**
> **ANALYSE FONCTIONNELLE**
>
> **THÈME**
> **TYPOLOGIE DES ASSEMBLAGES**
>
> **SÉQUENCE**
> **Analyse fonctionnelle interne d'un produit**
>
> **COMPOSANTES DES COMPÉTENCES DISCIPLINAIRES**
> CD 1.2: Décomposer un produit en chaines fonctionnelles.
> CD 1.4: Ordonner les fonctions techniques qui contribuent à la satisfaction des fonctions d'usage.
> CD 1.5: Rechercher les processeurs, les solutions constructives et les composants associés aux fonctions techniques.

⚠️ Le bandeau « THÈME » de la p.12 porte **TYPOLOGIE DES ASSEMBLAGES** [sic] : c'est le thème de
l'AXE 2 (p.87–128). Le sommaire p.4, le bandeau « SÉQUENCE » de cette même page et l'en-tête
courant de **toutes** les pages 13 à 40 donnent le thème réel : « Analyse fonctionnelle interne
d'un produit ». Erreur de gabarit de la source, signalée en § Incertitudes.

**Tableau « Analyse fonctionnelle interne d'un produit » (p.12)** — trois colonnes : `CD`,
`Savoirs et savoir-faire`, `Critères d'évaluation`. Transcription verbatim :

| CD | Savoirs et savoir-faire | Critères d'évaluation |
| --- | --- | --- |
| CD 1.2 | Organisation fonctionnelle d'un produit: <br> - Chaines fonctionnelles. <br> - Fonctions techniques associées aux fonctions de service. <br> - Composants assurant une fonction technique. | - Décomposition correcte du produit en chaine fonctionnelle. |
| CD 1.4 | *(idem — la cellule « Savoirs et savoir-faire » est fusionnée sur les 3 lignes)* | - Repérage adéquat des solutions techniques et des processeurs. |
| CD 1.5 | *(idem)* | - Justification adéquate des solutions choisies |

*(La dernière cellule est imprimée sans point final.)*

La page porte en bas un **QR code étiqueté `PDF`** (ressource numérique du thème).

**Compétences affichées dans l'en-tête des pages d'activité** : les pages de présentation des
supports (p.13, 14, 15, 19–25, 31–34) n'affichent **aucun** code CD ; toutes les pages de travail
de l'élève (p.16, 17, 18, 26, 27, 28, 29, 30, 35, 36, 37, 38, 39, 40) affichent **CD 2.2** et
**CD 3.8** dans la pastille de gauche. Les pages 16, 26 et 35 portent en plus les deux pictogrammes
de tête **COMM** et **COOP**.

---

##### Activité 1 — Micro-fraiseuse (p.13–18)

- **Système / support d'étude** : **Micro-fraiseuse** — machine-outil de C F A O (fraisage à
  commande numérique). L'étude porte plus précisément sur son **chariot transversal** (c'est le
  titre du cartouche du dessin d'ensemble, p.15).
- **Compétences affichées** : aucune sur p.13–15 ; **CD 2.2** et **CD 3.8** sur p.16, 17 et 18
  (+ pictogrammes **COMM** / **COOP** sur p.16).

###### Présentation du support d'activité (p.13–15)

**1. Mise en situation (p.13)** — texte verbatim :

> La C F A O permet, à l'aide de logiciels spécifiques de dessiner la pièce et d'optimiser les
> trajectoires de sa découpe. On pourra avec la C F A O lancer une simulation avant l'usinage ou
> éditer un prototype avant de lancer la production.
> Les machines utilisées en conception et fabrication assistée par ordinateur (C F A O) sont
> principalement des ordinateurs et des machines de fabrication.
> La micro-fraiseuse, qui fait l'objet de notre étude, est composée essentiellement comme
> l'indique la figure ci-dessous :
> - D'un ordinateur (unité centrale et ses périphériques).
> - D'un directeur de commande numérique (Carte de commande).
> - D'un logiciel de C F A O servant à créer le fichier d'usinage.
> - De moteurs, chariots, bâti, boutons, capteurs ….

**Figure p.13** : photographie de l'installation — à gauche l'ordinateur (écran, unité centrale,
clavier, souris), à droite la micro-fraiseuse dans son carter bleu, portière ouverte. Quatre
légendes fléchées : **Moteur broche**, **Chariot longitudinal**, **Bâti**, **Chariot transversal**.

**2. Caractéristiques de la micro-fraiseuse (p.13)** — texte verbatim :

> Le chariot transversal et la table de la machine portant la pièce (voir figure à la page
> suivante) se déplacent respectivement en translation suivant les 2 axes x et y.
> L'outil se déplace verticalement suivant l'axe z et tourne autour de cet axe.
> On appelle :
> - Om : origine machine, c'est la position de la machine en butée.
> - Op : origine pièce, définie par l'opérateur.

**Figure p.14** (vue 3D du sous-ensemble chariot transversal, en haut de page) — 9 légendes
fléchées : **Vis de manoeuvre**, **Noix**, **Table**, **Chariot transversal**, **Moteur d'axe X**,
**Moteur d'axe Y**, **Volant**, **Bâti**, **Semelle**, **Accouplement**.

**3. Nomenclature (p.14)** — 20 repères, verbatim :

| Rep. | Nbr. | Désignation | Matière | Observation |
| --- | --- | --- | --- | --- |
| 1 | 1 | Semelle | EN-GJL-200 | |
| 2 | 1 | Chariot transversal | C 60 | |
| 3 | 1 | Support de connexion | C 60 | |
| 4 | 1 | Support électromoteur | EN-GJL-200 | |
| 5 | 1 | Moteur | | |
| 6 | 5 | Vis à tête cylindrique à six pans creux ISO 4762-M4×12 | | |
| 7 | 1 | Volant de manœuvre | | |
| 8 | 1 | Arbre moteur | | |
| 9 | 1 | Manchon | | |
| 10 | 4 | Vis tête cylindrique à six pans creux ISO 4762-M4×16 | | |
| 11 | 1 | Vis de manœuvre | | |
| 12 | 1 | Noix du chariot longitidunal [sic] | Cu Zn 10 | |
| 13 | 3 | Cale | Cu Sn 8 | |
| 14 | 10 | Vis sans tête à six pans creux à téton long ISO 4728-M4×16 | | |
| 15 | 10 | Ecrou bas hexagonal ISO 4035- M4 | | |
| 16 | 1 | Cale | Cu Sn 8 | |
| 17 | 1 | Axe | C 35 | |
| 18 | 1 | Poignet | PVC | |
| 19 | 4 | Vis tête cylindrique à six pans creux ISO 4762-M4×20 | | |
| 20 | 1 | Noix du chariot transversal | Cu Zn 10 | |

**4. Dessin d'ensemble (p.15)** — planche pleine page, imprimée **en rotation de 90°**.
Cartouche : **« Chariot Transversal "Micro-Fraiseuse" »**, **Echelle : 2:5**, symbole de projection
européenne (cône). Contenu de la planche :

- **Vue principale en coupe** (coupe longitudinale du chariot), avec le trièdre **x, y, z** en
  haut à gauche. Repères pointés : **1** (semelle), **2** (chariot transversal, légendé « Table »
  au-dessus du repère 2), **12**, **11**, **3**, **4**, **10**, **9**, **8**, **19**, **5**, **6**,
  **7**, **18**, **17**. Plans de coupe repérés **A-A**, **B-B**, et zone de détail **C**.
- **Coupe A - A** (en haut à droite) : repères **16** et **13** pointés.
- **Détail C à l'échelle 1:1** : repères **13**, **14**, **15** (cale + vis sans tête + écrou).
- **Coupe B - B à l'échelle 1:1** (en bas à droite) : repères **5**, **10**, **11**, **9**, **4**.
- **QR code étiqueté `PDF`** en bas à gauche de la planche.

Aucune cote chiffrée n'est portée sur cette planche : seules les échelles (2:5, 1:1) sont données.

###### I. Situation déclenchante (p.16)

Encadré officiel, verbatim :

> Le besoin étant exprimé dans le CdCF de la micro-fraiseuse.
> L'analyse fonctionnelle interne consiste à rechercher les fonctions techniques, les solutions
> constructives et les composants qui doivent satisfaire aux fonctions de service.
> **Comment procéder pour faire cette analyse ?**

###### II. Travail demandé (p.16–18)

**A. Chaines fonctionnelles (p.16)**

Consigne verbatim :

> Compléter l'architecture fonctionnelle de la micro-fraiseuse (chaine d'énergie, chaine
> d'information).

Diagramme à compléter (les `…………` sont les cases laissées vides par le manuel) :

- **Chaîne d'information** — trois blocs en série : **Acquérir** → **Traiter** → **Communiquer**.
  - Entrée de gauche : « Information provenant d'un programme G-code de l'utilisateur et de
    l'environnement ».
  - Sortie de droite : « Utilisateur ».
  - Retour bas : « Information provenant du fonctionnement de la micro-fraiseuse ».
  - Processeurs déjà donnés sous les blocs : Acquérir → « Interrupteurs / Boutons poussoirs /
    Capteurs… » ; Traiter → « Micro-processeur » ; Communiquer → « Ecran / Voyants… ».
- Liaison verticale entre les deux chaînes : « **Ordres à exécuter de la chaine d'information** ».
- **Chaîne d'énergie** — quatre blocs en série puis une case vide :
  **Alimenter/Stocker** → **Distribuer** → **Convertir** → **Transmettre** → `…………` (bloc final
  à nommer, celui de l'action), avec la sortie « **Pertes** » et deux libellés à compléter
  (`…………………..` au-dessus et `……………………..` en dessous du bloc final).
  - Entrée de gauche : « Source d'énergie ».
  - Natures d'énergie portées sur les liaisons : **EE\*** (Alimenter→Distribuer), **EE\***
    (Distribuer→Convertir), **EM\*\*** (Convertir→Transmettre), **EM\*\*** (Transmettre→bloc final).
  - Processeurs déjà donnés (avec photo) : Alimenter/Stocker → « Unité d'alimentation : Prise
    secteur » ; Distribuer → « Carte de puissance » ; Convertir → « Actionneurs / Moteurs X, Y, Z /
    Moteur broche » ; Transmettre → « Elément de transmission de puissance ».
- Légende imprimée : **(\*) : énergie électrique ; (\*\*) : énergie mécanique**

**B. Mise en œuvre de la micro-fraiseuse (p.17)**

Consignes de sécurité (imprimées en rouge, avec le pictogramme triangulaire ⚠) — verbatim :

> Respecter les règles de sécurité durant le déroulement de l'activité.
> Enclencher le bouton d'arrêt d'urgence. Utiliser les clés appropriées.
> Effectuer les manipulations avec des gants résistants aux coupures.

Questions :

1. « Citer dans l'ordre les étapes à entreprendre pour monter l'outil fraise à deux lèvres de
   diamètre **3mm**. » *(4 lignes pointillées de réponse — la source imprime « 3mm », sans espace)*
2. « Justifier la présence du **capteur de portière**. » *(2 lignes pointillées)*
3. « La machine et le fichier G-code étant préparés à l'avance par l'enseignant. Charger
   « G-code » et régler l'origine pièce et suivre les étapes de fabrication de la pièce. »

Ressource associée : photo de la **Pince porte-outil** (légendée, flèche rouge) et un **QR code
étiqueté `Gcode`** donnant le fichier G-code.

**C. Fonctions techniques associées aux fonctions de service (FAST) (p.17–18)**

*Question 1 (p.17)* — consigne verbatim :

> 1. Compléter le diagramme d'analyse fonctionnelle FAST partiel descriptif ci-dessous de la
>    fonction de service FS1.

Arbre imprimé (colonnes : **Fonction technique FT** | **Processeur**) :

| Fonction de service | Fonction technique FT | Processeur |
| --- | --- | --- |
| **FS1 : Usiner une pièce** | FT1 : Positionner et maintenir la pièce | *(à compléter)* |
| | FT2 : Positionner et maintenir l'outil | *(à compléter)* |
| | FT3 : Animer l'outil d'un mouvement de rotation autour de son axe Z | *(à compléter)* |
| | FT4 : Assurer les déplacements relatifs de l'outil et de la pièce. | *(2 cases à compléter)* puis **Directeur de commande DCN** *(déjà donné)* |

*Question 2 (p.18)* — consigne verbatim :

> 2. En se référant au dessin d'ensemble de la micro-fraiseuse, on demande de compléter le
>    diagramme F.A.S.T relatif à la fonction technique FT4 en indiquant les composants.

Colonne de droite intitulée **Composants** — toutes les cases sont vides (2 lignes pointillées
chacune, 3 lignes pour les cases de FT4271 et FT4272). Arbre imprimé :

- **FT4: Animer la pièce d'un mouvement de translation suivant (oy).**
  - **FT41 : Déplacer manuellement le chariot transversal suivant (oy)**
    - FT411 : Utiliser un moteur à double sorties d'arbre → *composant à trouver*
    - FT412 : Tourner l'arbre moteur manuellement → *composant à trouver*
  - **FT42 : Déplacer le chariot transversal automatiquement suivant (oy)**
    - FT421 : Gérer les ordres de commandes → *composant à trouver*
    - FT422 : Convertir les consignes numériques en signaux analogiques → *composant à trouver*
    - FT423 : Distribuer l'énergie électrique → *composant à trouver*
    - FT424 : Convertir l'énergie → *composant à trouver*
    - FT425 : Transmettre le mouvement de rotation de l'arbre moteur à la **vis (11)** → *composant à trouver*
    - FT426 : Transformer le mouvement de rotation en translation → *composant à trouver*
    - FT427 : Guider en translation
      - FT4271 : Prévoir un guidage prismatique → *composant à trouver*
      - FT4272 : Régler et rattraper le jeu. → *composant à trouver*

⚠️ **Contradiction interne de la source** : FT4 est libellée « Assurer les déplacements relatifs
de l'outil et de la pièce. » en p.17 et « Animer la pièce d'un mouvement de translation suivant
(oy). » en p.18. Signalée en § Incertitudes.

- **Données numériques de l'énoncé (activité 1)** : outil fraise à deux lèvres **Ø 3 mm** (p.17) ;
  échelles de la planche **2:5**, **1:1** (détail C), **1:1** (coupe B-B) (p.15) ; vis
  **ISO 4762-M4×12** (×5), **ISO 4762-M4×16** (×4), **ISO 4728-M4×16** (×10),
  **ISO 4762-M4×20** (×4), écrous **ISO 4035-M4** (×10) (p.14) ; matières **EN-GJL-200**, **C 60**,
  **C 35**, **Cu Zn 10**, **Cu Sn 8**, **PVC** (p.14).
- **Vocabulaire & terminologie officielle (activité 1)** : C F A O ; directeur de commande
  numérique (carte de commande) / DCN ; chariot longitudinal, chariot transversal, table, bâti,
  semelle, noix, vis de manœuvre, volant de manœuvre, accouplement, manchon, moteur broche,
  pince porte-outil, capteur de portière ; origine machine **Om**, origine pièce **Op** ; chaine
  d'énergie / chaine d'information ; Acquérir, Traiter, Communiquer ; Alimenter/Stocker,
  Distribuer, Convertir, Transmettre ; énergie électrique (EE), énergie mécanique (EM) ; pertes ;
  fonction de service **FS1**, fonctions techniques **FT**, processeur, composant ; diagramme
  **FAST / F.A.S.T** ; guidage prismatique, rattrapage de jeu.

---

##### Activité 2 — Imprimante 3D (p.19–30)

- **Système / support d'étude** : **Imprimante 3D** de type **FDM** (dépôt de filament fondu),
  volume utile 200×200×200 mm.
- **Compétences affichées** : aucune sur p.19–25 ; **CD 2.2** et **CD 3.8** sur p.26 à 30
  (+ **COMM** / **COOP** sur p.26).

###### Présentation du support d'activité (p.19–25)

**1. Mise en situation (p.19)** — texte verbatim :

> L'impression 3D FDM consiste à fondre un filament et à le déposer couche par couche à l'aide
> d'une buse d'impression. Entre chaque couche, le plateau d'impression descend afin de permettre
> l'extrusion de la couche suivante. Ce procédé de dépôt de couches fondues se répète jusqu'à ce
> que l'objet conçu soit entièrement réalisé par l'imprimante 3D.

**Figures p.19** : deux photographies de la même imprimante 3D (châssis rouge/noir, écran tactile
en façade, bobine de filament en fond de bac) — vue capot ouvert et vue capot fermé.

**Principe de fonctionnement (p.19)** — sous-titre imprimé en rouge, suivi de « (voir dessins
pages 21, 22 et 23) ». Texte verbatim :

> La tête d'impression, est dotée d'un moteur pas à pas (43 + 44), le galet cranté (46) entraine
> le filament (58) contre le galet presseur (59), par adhérence pour l'avancer ou le reculer, cela
> permet de gérer d'une manière précise la quantité de matière à utiliser. La cartouche chauffante
> (67) permet de fondre le filament, la thermistance (66) permet de contrôler la température. Le
> filament fondu est poussé à travers la buse (57) pour calibrer la section du filament à déposer.
> La matière extrudée est déposée en fines couches sur le plateau (8), qui peut être chauffé pour
> améliorer l'adhésion. Le ventilateur (63) et le dissipateur thermique (62) permettent de
> refroidir constamment la tête d'impression.

Suite du principe (p.20) — texte verbatim :

> Le moteur d'axe X(12), entraine un système poulies-courroie, la courroie(13) est fixée sur la
> tête d'impression assurant sa translation suivant X par rapport au bâti, son guidage en
> translation est assuré par des douilles à billes (50) montées sur la platine d'axe X(35) qui
> glisse sur deux colonnes rectifiées (21).
>
> La tête d'impression, se déplace selon Y par l'intermédiaire du moteur d'axe Y(17) qui entraine
> deux systèmes poulies-courroies, la courroie (18) liée à la platine assure sa translation
> suivant Y par rapport au bâti.
>
> Le moteur d'axe Z à arbre fileté (24+25) transmet le mouvement de rotation aux deux tiges
> filetées (27), par l'intermédiaire d'un système poulies-courroies. Les trois écrous T8 (28),
> assemblés sur le plateau(7) transforment cette rotation en translation suivant l'axe Z de ce
> dernier.

**2. Extrait du cahier des charges fonctionnel de l'imprimante 3D (p.20)** — tableau verbatim
(colonnes : `F. S`, `Expression`, `Critères d'appréciation`, `Niveaux- Flexibilités`) :

| F. S | Expression | Critères d'appréciation | Niveaux- Flexibilités |
| --- | --- | --- | --- |
| FP | Permettre l'impression d'une pièce à partir d'un modèle numérique | -Taille maximale <br> -Précision d'impression | 200x200x200mm ±5mm <br> 0.2 mm ±0.1mm |
| FC2 | Être compatible avec le fil d'impression | -Matière du filament <br> -Diamètre de filament | Matière plastique (PLA-ABS...) <br> Ø1.75mm ±0.05 mm |
| FC4 | S'alimenter en énergie électrique | -Tension du secteur <br> -Tension d'alimentation | U =220V AC ±20V <br> UE=24V DC ±2V |
| FC7 | Communiquer avec l'ordinateur | -Type de fichier <br> -Interface de connexion <br> -Stockage amovible | ISO (Gcode) <br> USB <br> Catre Micro-SD [sic] |
| FC8 | Être stable | -Poids <br> -Surface d'appui | 7Kg ±50g <br> 3 points au minimum |

*(Le CdCF imprimé ne comporte que FP, FC2, FC4, FC7 et FC8 — c'est un « extrait » ; FC1, FC3, FC5
et FC6 ne figurent pas.)*

**3. Dessins d'ensembles (p.21–23)** — trois planches pleines pages, imprimées **en rotation de
90°**, chacune avec son cartouche et un **QR code étiqueté `PDF`**.

*Planche p.21* — cartouche : **« Imprimante 3D »**, **Echelle : 1:6**, projection européenne.
Elle regroupe quatre représentations :
- **Vue d'ensemble en perspective** de la machine complète, repères pointés : **13, 8, 29, 21, 35,
  34, 10, 20, 36, 16, 6, 14, 7, 23, 22, 5, 9, 3, 30, 4, 27, 1, 11, 2, 12, 15, 18, 19, 17, 25, 26**,
  avec la mention **« (2),(3),(4),(5) et (9) en coupe locale »** et un repère de détail **A**.
- **« Assemblage de (12) avec (15) — Echelle:3:10 »** (vue éclatée) : repères **12, 32, 33, 19, 15**.
- **« DÉTAIL A — Echelle:2:5 »** : repères **31, 27, 28**.
- **Sous-ensemble d'axe Z en perspective** (trièdre X, Y, Z) : repères **30, 27, 25, 20, 24, 14, 26**.

*Planche p.22* — cartouche : **« Tête d'impression en vue éclatée »**, **Echelle : 1:2**. Contient :
- La **vue éclatée** de la tête d'impression, repères pointés : **48, 49, 47, 38, 37, 50, 35, 43,
  44, 40, 55, 46, 41, 54, 60, 59, 62, 68, 65, 64, 67, 66, 39, 56, 36, 58, 61, 45, 63, 53, 42, 57,
  52, 69, 51**.
- **« Ensemble monté — Echelle:1:2 »** (perspective de la tête assemblée).
- **« Système d'entraînement du fil seul — Echelle:3:10 »** (perspective du seul extrudeur).

*Planche p.23* — cartouche : **« Tête d'impression »**, **Echelle : 5:6**. Contient :
- une **vue de dessus** : repères **55, 39, 52, 51, 42, 36, 56, 53** ;
- une **coupe A-A** : repères **41, 63, 40, 38, 65, 68, 64, 47, 54, 48, 45, 62, 49, 37, 50** ;
- une **vue de face** avec le plan de coupe **A-A** : repères **43, 67, 66, 69** ;
- **« Détail C — Echelle:5:3 »** : repères **64, 57** (bloc chauffant + buse) ;
- **« Détail B — Echelle:5:3 »** : repères **46, 35, 58, 59, 60, 44** (galet cranté / galet
  presseur / filament) ; repères de zones **B** et **C** portés sur la coupe A-A.

**4. Nomenclature (p.24–25)** — 69 repères, verbatim :

| Rep. | Nbr. | Désignation | Matière | Observation |
| --- | --- | --- | --- | --- |
| 1 | 1 | Ecran tactile | | |
| 2 | 1 | Cache châssis avant | | |
| 3 | 1 | Cache châssis latéral | | |
| 4 | 1 | Châssis avant | | |
| 5 | 1 | Châssis latéral | | |
| 6 | 1 | Plateau supérieur fixe | | |
| 7 | 1 | Plateau mobile | | |
| 8 | 1 | Plateau porte-pièce | | |
| 9 | 1 | Plateau inférieur fixe | | |
| 10 | 1 | Tête d'impression | | |
| 11 | 1 | Bobine filament | PLA | |
| 12 | 1 | Moteur d'axe X (SL42STH34-1504A) | | |
| 13 | 1 | Courroie crantée ouverte d'axe X | | GT2 |
| 14 | 4 | Poulie folle lisse ; Øarbre=3mm | | |
| 15 | 1 | Platine mobile d'axe Y | ABS | |
| 16 | 1 | Platine guide d'axe Y | ABS | |
| 17 | 1 | Moteur d'axe Y (SL42STH34-1504A) | | |
| 18 | 1 | Courroie crantée ouverte d'axe Y | | GT2 |
| 19 | 2 | Poulie dentée Z=20 ; Øarbre=5mm | | GT2 |
| 20 | 5 | Poulie dentée Z=20 ; Øarbre=8mm | | GT2 |
| 21 | 2 | Colonne rectifiée de guidage d'axe X | | |
| 22 | 1 | Courroie crantée fermée d'axe Y | | GT2 |
| 23 | 2 | Colonne rectifiée de guidage d'axe Y | | |
| 24 | 1 | Stator moteur d'axe Z (SL42STH34-1504A) | | |
| 25 | 1 | Arbre moteur fileté d'axe Z | | T8 |
| 26 | 1 | Courroie crantée fermée d'axe Z | | GT2 |
| 27 | 2 | Tige filetée d'entraînement | | T8 |
| 28 | 3 | Écrou T8 | | |
| 29 | 1 | Arbre lisse | | |
| 30 | 2 | Colonne de guidage d'axe Z | | Rectifiée |
| 31 | 2 | Douille à billes à bride | | LMF8LUU |
| 32 | 3 | Capteur fin de course | | |
| 33 | 2 | Douille à billes | | LM8LUU |
| 34 | 1 | Pièce à imprimer | PLA | |
| 35 | 1 | Platine mobile d'axe X | ABS | |
| 36 | 1 | Tube guide extérieur | PTFE | |
| 37 | 1 | Insert  M3x4 | CuZn10 | |
| 38 | 1 | Support de montage | S 235 | |
| 39 | 1 | Levier presseur | ABS | |
| 40 | 1 | Corps d'extrudeuse | ABS | |
| 41 | 1 | Ressort cylindrique de compression | 55 Cr 3 | |
| 42 | 2 | Vis sans tête à six pans creux M3x3 ISO 4026 | | |
| 43 | 1 | Stator moteur (SL42STH40-1504A) | | |
| 44 | 1 | Rotor moteur | | |
| 45 | 2 | Vis sans tête à six pans creux M4x4 ISO 4026 | | |
| 46 | 1 | Galet cranté d'entrainement | | |
| 47 | 1 | Capot | ABS | |
| 48 | 1 | Vis à tête cylindrique bombée à six pans creux M3x10 ISO 7380 | | |
| 49 | 1 | Vis à tête cylindrique bombée à six pans creux M3x8 ISO 7380 | | |
| 50 | 2 | Douille à billes | | LM8LUU |
| 51 | 2 | Vis à tête cylindrique bombée à empreinte cruciforme M2x16 ISO 7045 | | |
| 52 | 2 | Vis à tête cylindrique bombée à empreinte cruciforme M2x8 ISO 7045 | | |
| 53 | 3 | Vis à tête cylindrique à six pans creux M3x20 ISO 4762 | | |
| 54 | 1 | Coussinet cylindrique de centrage | CuSn8Pb | |
| 55 | 1 | Vis à tête fraisée à six pans creux M3x10 ISO 10642 | | |
| 56 | 1 | Raccord pneumatique PC4-M6 | | |
| 57 | 1 | Buse Ø 0.4mm | CuZn15 | |
| 58 | 1 | Filament | PLA | |
| 59 | 1 | Galet presseur | | |
| 60 | 1 | Roulement BC | | |
| 61 | 1 | Palier porte galet | ABS | |
| 62 | 1 | Dissipateur thermique | EN AW-1050 | |
| 63 | 1 | Ventilateur brushless BEF0412MS | | |
| 64 | 1 | Bloc chauffant | EN AW-1050 | |
| 65 | 1 | Tube d'alimentation | X5 Cr Ni 18-10 | |
| 66 | 1 | Thermistance | | NTC 100K |
| 67 | 1 | Cartouche chauffante | | 24V-40W |
| 68 | 1 | Tube guide intérieur | PTFE | |
| 69 | 1 | Tuyère | ABS | |

###### I. Situation déclenchante (p.26)

Encadré officiel, verbatim :

> Le besoin étant exprimé dans le CdCF de l'imprimante 3D.
> L'analyse fonctionnelle interne consiste à rechercher les fonctions techniques, les solutions
> constructives et les composants qui doivent satisfaire une fonction de service.
> **Comment procéder pour faire cette analyse ?**

###### II. Travail demandé (p.26–30)

Consignes de sécurité en tête du travail demandé (p.26, avec pictogramme ⚠) — verbatim :

> - Ne jamais toucher à l'intérieur de l'imprimante 3D pendant le fonctionnement.
> - A l'arrêt de la machine, vérifier le refroidissement total de l'ensemble avant la manipulation.
> - Déconnecter le bloc d'alimentation du secteur en cas d'urgence.
> - Placer l'imprimante 3D dans un endroit propre et bien aéré.
> - Toutes les manipulations seront faites en présence de l'enseignant.

**A. Mise en œuvre de l'imprimante 3D — Préparation de la machine (p.26)**

1. « Justifier l'utilisation des pièces **(36)** et **(56)** » *(1 ligne pointillée)*
   — c'est-à-dire le **tube guide extérieur PTFE** et le **raccord pneumatique PC4-M6**.
2. « Mettre la machine sous tension, sur l'écran tactile, toucher : » *(suivi de trois captures
   d'écran annotées d'un doigt : menu **System / Tool / Print** → sous-menu **Manual / Preheat /
   Filament / Level / Fan / Stop / Z offset / Back** → pavé de déplacement **X, Y, Z, E**, avec une
   barre de choix du pas dont seuls les boutons **0.01mm** et **10mm** sont lisibles — les deux
   boutons intermédiaires sont masqués par la main du doigt : `[?]` et `[?]`)*. Puis :

   > Après l'observation des mouvements, compléter le tableau suivant en cochant la case
   > appropriée :

   Tableau à compléter (toutes cases vides) :

   | | Déplacements : X | Déplacements : Y | Déplacements : Z |
   | --- | --- | --- | --- |
   | Tête d'impression | | | |
   | Plateau mobile | | | |

3. « Pour vérifier l'écoulement correct de la matière fondue, toucher : » *(captures d'écran :
   menu **Manual / Preheat / Filament / Level / Fan / Stop / Z offset / Back**, puis la commande
   d'extrusion **E1** avec les affichages de température **23/200** puis **200/200**)*.

**Impression de la pièce (p.27)** — texte verbatim :

> La machine et le fichier G-code étant préparés à l'avance par l'enseignant.
> Toucher [pictogramme **Print**] et charger le fichier permettant d'obtenir un support de
> rangement des clés.
> Ficher G-CODE : [QR code étiqueté **ZIP**]
> Suivre les étapes de fabrication de la pièce.

*(La pièce à fabriquer est un support de rangement de clés ; une photo de jeu de clés mâles et
d'un tournevis illustre la page. « Ficher G-CODE » est imprimé ainsi [sic] pour « Fichier ».)*

**B. Chaines fonctionnelles (p.27)**

Consigne verbatim :

> Compléter l'architecture fonctionnelle de l'imprimante 3D (chaine d'énergie, chaine
> d'information).

Diagramme à compléter :

- **Chaîne d'information** : **Acquérir** → **Traiter** → **Communiquer**, sortie « Afficheur ».
  Entrées de gauche : « **Programme GCODE** » (en rouge). Processeurs déjà donnés : Acquérir →
  « Capteurs » (photo d'un micro-interrupteur) ; Traiter → « Carte électronique » ; Communiquer →
  « Fils de liaison ». Liaison vers le bas étiquetée « **Ordres** ».
- **Chaîne d'énergie** : **Alimenter** → **Distribuer** → **Convertir** → **Transmettre** →
  bloc final `………` (5 lignes vides à remplir), avec la sortie « **Pertes** » et deux libellés
  `………………` à compléter (au-dessus et au-dessous du bloc final). Entrée de gauche : « **E.E\*** ».
  Natures d'énergie sur les liaisons : **EE\***, **EE\***, **EM\*\***, **EM\*\***.
  Processeurs déjà donnés (avec photos) : Alimenter → « Bloc d'alimentation » ; Distribuer →
  « Contrôleur moteur pas à pas » ; Convertir → « Moteur pas à pas » ; Transmettre → « Eléments de
  transmission ».
- **Deuxième branche de conversion** (dérivée de Distribuer) : un second bloc **Convertir**,
  alimenté en **EE\*** et sortant en **E<sub>Th</sub>\*\*\***, dont le processeur donné est la
  « Résistance chauffante ».
- Légende imprimée : **(\*) : Énergie électrique ; (\*\*) : Énergie mécanique ;
  (\*\*\*) : Énergie thermique**

**C. Fonctions techniques associées aux fonctions de service (FAST) (p.28–30)**

*Question 1 (p.28)* — consigne verbatim :

> 1. Inscrire les solutions constructives associées aux fonctions techniques qui contribuent à la
>    satisfaction de la fonction principale FP : « Permettre l'impression d'une pièce à partir d'un
>    modèle numérique ».

Colonne de droite : **Solutions associées aux fonctions techniques** (toutes vides). Arbre imprimé :

- **FP1 : Permettre l'impression d'une pièce à partir d'un modèle numérique**
  - **FT1 : Recevoir et transmettre l'information** → *solution à trouver*
  - **FT2 : Déposer la matière sur le plateau porte-pièce (8)**
    - FT21 : Alimenter en fil d'impression → *solution à trouver*
    - FT22 : Chauffer la matière → *solution à trouver*
    - FT23 : Calibrer la matière fondue → *solution à trouver*
  - **FT3 : Déplacer la tête d'impression**
    - FT31 : Déplacer la tête d'impression suivant l'axe X → *solution à trouver*
    - FT32 : Déplacer la tête d'impression suivant l'axe Y → *solution à trouver*
  - **FT4 : Déplacer le plateau (7) suivant l'axe Z** *(pas de case solution sur cette ligne)*

*Question 2 (p.29)* — consigne verbatim :

> 2. En se référant au dossier technique, compléter le diagramme F.A.S.T relatif à la fonction
>    technique FT21 : « Alimenter en fil d'impression » en indiquant les noms de composants.

Colonne **Composants** (vide). Arbre :

- **FT21 : Alimenter en fil d'impression**
  - FT211 : Convertir l'énergie électrique en énergie mécanique de rotation → *composant à trouver*
  - FT212 : Guider le fil d'impression → *composant à trouver*
  - FT213 : Transformer le mouvement de rotation en mouvement de translation du **filament (58)** → *composant à trouver*

*Question 3 (p.29)* — consigne verbatim :

> 3. En se référant au dossier technique, compléter le diagramme F.A.S.T relatif à la fonction
>    technique FT31 : « déplacer la tête d'impression suivant l'axe X» en indiquant les noms de
>    composants.

Colonne **Composants** (vide). Arbre :

- **FT31 : Déplacer la tête d'impression suivant l'axe X**
  - FT311 : Convertir l'énergie électrique en énergie mécanique de rotation → *composant à trouver*
  - FT312 : Transformer le mouvement de rotation en mouvement de translation de la tête d'impression → *composant à trouver*
  - FT313 : Guider la tête d'impression en translation → *composant à trouver*

*Question 4 (p.30)* — consigne verbatim :

> 4. En se référant au dossier technique, compléter le diagramme F.A.S.T relatif à la fonction
>    technique FT4 : « déplacer le plateau (7) suivant l'axe Z» en indiquant les noms de
>    composants.

Colonne **Composants** (vide, 2 lignes pointillées par case). Arbre :

- **FT4 : Déplacer le plateau (7) suivant l'axe Z**
  - FT41 : Convertir l'énergie électrique en énergie mécanique de rotation → *composant à trouver*
  - FT42 : Transmettre le mouvement de rotation de l'**arbre moteur (25)** aux deux **tiges filetées d'entraînement (27)** → *composant à trouver*
  - FT43 : Transformer le mouvement de rotation en mouvement de translation du **plateau (7)** → *composant à trouver*
  - FT44 : Guider en translation le **plateau (7)** → *composant à trouver*

- **Données numériques de l'énoncé (activité 2)** : taille maximale imprimable
  **200×200×200 mm ±5 mm** ; précision d'impression **0.2 mm ±0.1 mm** ; filament **Ø 1.75 mm
  ±0.05 mm**, matière plastique (PLA-ABS...) ; tension secteur **U = 220 V AC ±20 V** ; tension
  d'alimentation **UE = 24 V DC ±2 V** ; poids **7 Kg ±50 g** ; **3 points d'appui au minimum**
  (p.20). Buse **Ø 0.4 mm** ; poulies folles **Øarbre = 3 mm** ; poulies dentées **Z = 20** avec
  **Øarbre = 5 mm** et **Øarbre = 8 mm** ; courroies **GT2** ; tiges filetées et arbre moteur
  **T8** ; **3 écrous T8** ; **2 colonnes rectifiées** de guidage X et **2** de guidage Y ;
  **2 colonnes de guidage d'axe Z** ; douilles **LM8LUU** et **LMF8LUU** ; thermistance
  **NTC 100K** ; cartouche chauffante **24 V-40 W** ; ventilateur **BEF0412MS** ; moteurs
  **SL42STH34-1504A** (X, Y, Z) et **SL42STH40-1504A** (extrudeur) ; **3 capteurs fin de course**
  (p.24-25). Températures affichées à l'écran : **23/200** puis **200/200** ; pas de déplacement
  **0.01mm** et **10mm** (les deux pas intermédiaires sont masqués sur la photo, `[?]`) (p.26).
  Échelles des planches : **1:6** (p.21), **3:10**, **2:5**, **1:2** (p.22), **5:6** et **5:3**
  (p.23).
- **Vocabulaire & terminologie officielle (activité 2)** : impression 3D **FDM** ; buse
  d'impression, plateau d'impression, extrusion, couches fondues ; tête d'impression, galet cranté
  d'entraînement, galet presseur, cartouche chauffante, thermistance, dissipateur thermique,
  ventilateur brushless, bloc chauffant, tuyère, tube guide intérieur / extérieur, raccord
  pneumatique, coussinet cylindrique de centrage, palier porte galet ; système poulies-courroie,
  courroie crantée ouverte / fermée, poulie dentée, poulie folle lisse, douille à billes (à bride),
  colonne rectifiée, tige filetée d'entraînement, écrou T8, platine mobile / platine guide,
  capteur fin de course ; cahier des charges fonctionnel (**CdCF**), fonction principale **FP**,
  fonctions contraintes **FC2, FC4, FC7, FC8**, critères d'appréciation, niveaux-flexibilités ;
  Gcode / G-code ; solutions constructives ; **F.A.S.T**.

---

##### Activité 3 — Micro-tour (p.31–38)

- **Système / support d'étude** : **Micro-tour** à commande numérique (tour CNC de table).
- **Compétences affichées** : aucune sur p.31–34 ; **CD 2.2** et **CD 3.8** sur p.35 à 38
  (+ **COMM** / **COOP** sur p.35).

###### Présentation du support d'activité (p.31–34)

**1. Mise en situation (p.31)** — texte verbatim :

> Le Micro-tour (représenté ci-dessous) est une machine-outil à commande numérique. Elle est
> commandée par ordinateur muni d'un logiciel qui assure la lecture et le traitement du G-code
> (le langage qui décrit les opérations à effectuer).
> Actuellement, on peut utiliser un logiciel ayant des fonctions optimisées qui rendent rapide et
> facile la génération de programmes nécessaires à un usinage.

**Figure p.31** : photographie du micro-tour (bâti noir, capot rouge, carter de protection
transparent) accompagnée de l'ordinateur (écran affichant le logiciel de CN, unité centrale,
clavier, souris).

**2. Description de la machine (voir machine et dessin d'ensemble) (p.31–32)** — texte verbatim :

> Les vis d'entraînement du traînard et du chariot transversal sont commandées par des moteurs
> pas à pas.
>
> La commande manuelle des chariots est accessible au moyen de volants.
>
> La broche est entraînée par un moteur à courant continu et un système de transmission par
> poulies courroie.
>
> La machine et sa commande sont constituées essentiellement par:
> - Un ordinateur (unité centrale et ses périphériques)
> - Un logiciel de F.A.O servant à créer le fichier d'usinage.
> - Des actionneurs (moteurs), des capteurs et des organes de sécurité (carter et bouton d'arrêt
>   d'urgence).
>
> La pièce à usiner est placée dans le mandrin et serrée par l'intermédiaire des mors. Un moteur
> permet la mise en rotation du mandrin fixé sur la broche. L'outil coupant, est positionné et
> serré à l'aide des vis (41) dans un porte-outil (5). Le porte-outil (5) est mis en place sur un
> chariot porte-outil (7). Le chariot transversal d'axe X et longitudinal d'axe Z assurent les
> mouvements de l'outil par des moteurs d'avance (38).
>
> La poupée mobile permet de réaliser des opérations de pointage, centrage, perçage et alésage en
> bout de pièce.
>
> Pratiquement, on distingue :
> - L'origine machine **Om**. C'est la position de la machine en butée.
> - L'origine pièce **Op**, est définie par l'opérateur.

**Figure p.32** : photographie du micro-tour, capot de sécurité relevé, avec 9 légendes fléchées
portant les repères de nomenclature : **Chariot porte outil (7)**, **Capot de sécurité**,
**Mandrin porte pièce (8)**, **Poupée mobile (1)**, **Bouton d'arrêt d'urgence**, **Moteur
d'entraînement du Traînard (38)**, **Vis mère (26)**, **Banc (22)**, **Moteur d'entraînement du
chariot porte outil**.

**3. Dessin d'ensemble (p.33)** — planche pleine page. Cartouche : **« MICRO TOUR »**,
**Echelle : 1:5**, projection européenne, **QR code étiqueté `PDF`**. Contenu :
- **Vue principale en coupe longitudinale** (trièdre Y en haut, Z à droite) : repères pointés
  **14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 37, 15, 16, 17, 38, 39, 18, 19, 20, 21, 22, 23,
  24, 25, 26, 40** ; plans de coupe **A-A**, **B-B**, **C-C** ; zones de détail **D** et **E**.
- **Coupe B-B (Echelle:2:5)** : repères **21, 51, 50, 49, 22, 48**, avec la mention **« Vue suivant
  F »** et le repère de sens **F**.
- **Coupe C-C** (sous-ensemble chariot transversal / traînard, axe **X**) : repères **41, 32, 33,
  34, 35, 36, 27, 28, 29, 30, 31**, plan de coupe **A-A** repris.
- **détail D (Echelle :1:2)** : repère **42**.
- **détail E (Echelle :4:5)** : repère **43**, axe **Z**.
- **Détail du palier de vis mère** (en bas à gauche) : repères **47, 26, 44, 45, 46**, axe **Z**.

**Figure p.34** (en haut de page) : **« Sous-ensemble support pièce (Echelle : 1:2) »** — coupe du
mandrin et de la broche, repères **53, 9, 52, 11, 8** et la légende **« Pièce »**.

**4. Nomenclature (p.34)** — 53 repères, imprimée en deux colonnes (Rep. | Nbr. | Désignation),
sans colonnes Matière / Observation. Verbatim :

| Rep. | Nbr. | Désignation |
| --- | --- | --- |
| 1 | 1 | Poupée mobile |
| 2 | 1 | Tambour gradué |
| 3 | 1 | Palier |
| 4 | 1 | Vis d'entraînement chariot porte-outil |
| 5 | 1 | Tourelle porte-outil |
| 6 | 1 | Poignée de blocage |
| 7 | 1 | Chariot porte-outil |
| 8 | 1 | Mandrin |
| 9 | 1 | Couvercle |
| 10 | 2 | Roulement à rouleaux coniques |
| 11 | 1 | Broche |
| 12 | 6 | Vis à tête cylindrique à six pans creux |
| 13 | 1 | Poulie réceptrice |
| 14 | 1 | Flasque |
| 15 | 1 | Clavette parallèle |
| 16 | 1 | Encodeur |
| 17 | 2 | Écrou à encoches KM-M38 |
| 18 | 1 | Cage |
| 19 | 1 | Courroie crantée |
| 20 | 1 | Poulie motrice |
| 21 | 1 | Moteur électrique |
| 22 | 1 | Banc |
| 23 | 1 | Contre glissière |
| 24 | 1 | Axe de centrage |
| 25 | 1 | Écrou de la vis mère |
| 26 | 1 | Vis mère du traînard |
| 27 | 1 | Outil |
| 28 | 1 | Écrou de guidage chariot transversal |
| 29 | 1 | Chariot transversal |
| 30 | 1 | Vis de manœuvre chariot transversal |
| 31 | 1 | Traînard |
| 32 | 1 | Cale |
| 33 | 1 | Indicateur de position |
| 34 | 1 | Palier |
| 35 | 2 | Butée à billes |
| 36 | 1 | Tablier de chariot |
| 37 | 2 | Accouplement |
| 38 | 2 | Moteur pas à pas |
| 39 | 2 | Vis HC M6x8 |
| 40 | 2 | Volant |
| 41 | 6 | Vis CHC M6x25 à téton long |
| 42 | 2 | Vis CHC M6 x 20 |
| 43 | 1 | Roulement |
| 44 | 2 | Butée à billes |
| 45 | 1 | Palier vis mère |
| 46 | 2 | Écrou à encoches  KM-M10 |
| 47 | 2 | Vis CHC M5 x 16 |
| 48 | 2 | Rondelle |
| 49 | 2 | Vis HC M6 x 25 |
| 50 | 2 | Rondelle Grower |
| 51 | 2 | Écrou H |
| 52 | 3 | Goujon M8 x 28 |
| 53 | 3 | Rondelle Grower |

###### I. Situation déclenchante (p.35)

Encadré officiel, verbatim :

> Le besoin étant exprimé dans le CdCF du micro-tour.
> L'analyse fonctionnelle interne consiste à rechercher les fonctions techniques, les solutions
> constructives et les composants qui doivent satisfaire chaque fonction de service.
> **Comment procéder pour faire cette analyse ?**

###### II. Travail demandé (p.35–38)

**A. Chaines fonctionnelles (p.35)**

Consigne verbatim :

> Compléter l'architecture fonctionnelle du micro-tour (chaine d'énergie, chaine d'information).

Diagramme à compléter :

- **Chaîne d'information** : **Acquérir** → **Traiter** → **Communiquer**, sortie « Utilisateur ».
  Entrée de gauche : « Information provenant d'un programme G-CODE, de l'utilisateur et de
  l'environnement ». Retour bas : « Information provenant du fonctionnement du micro-tour ».
  Processeurs déjà donnés : Acquérir → « Interrupteurs / Boutons poussoirs » ; Traiter →
  « Microcontrôleur » ; Communiquer → « Ecran ».
- Liaison verticale : « **Ordres à exécuter de la chaine d'information** ».
- **Chaîne d'énergie** : **Alimenter/Stocker** → **Distribuer** → **Convertir** → **Transmettre** →
  bloc final `…………` (4 lignes vides), sortie « **Pertes** », deux libellés `…………………`
  à compléter. Entrée de gauche : « Source d'énergie ». Natures d'énergie : **EE\***, **EE\***,
  **EM\*\***, **EM\*\***. Processeurs déjà donnés (photos) : Alimenter/Stocker → « Unité
  d'alimentation : » ; Distribuer → « Carte de puissance » ; Convertir → « Moteurs pas à pas X, Z »
  **et** « Moteur électrique » ; Transmettre → « Eléments de transmission ».
- Légende imprimée : **(\*) : énergie électrique ; (\*\*) : énergie mécanique**

**B. Mise en œuvre du micro-tour (p.36)**

Consignes de sécurité (en rouge, pictogramme ⚠) — verbatim :

> - Respecter les règles de sécurité durant le déroulement de l'activité.
> - Enclencher le bouton d'arrêt d'urgence. Utiliser les clés appropriées.
> - Effectuer les manipulations avec des gants résistants aux coupures.
> - Ranger immédiatement les outils non utilisés.

Questions :

1. « Citer dans l'ordre les étapes à entreprendre pour monter l'outil dans la tourelle porte
   outils. » *(3 lignes pointillées)*
2. « Comment entreprendre pour monter une pièce de grand diamètre dans le mandrin ? »
   *(3 lignes pointillées)*
3. « La machine et le fichier G-code étant préparés à l'avance par l'enseignant. Charger
   « G-code », régler l'origine pièce et observer les étapes de fabrication de la pièce. »
   *(QR code étiqueté `Gcode`)*

**C. Fonctions techniques associées aux fonctions de service (FAST) (p.36–38)**

Phrase de cadrage (p.36) : « En se référant au micro-tour et à son dessin d'ensemble. »

*Question 1 (p.36)* — consigne verbatim :

> 1. Compléter, le diagramme d'analyse fonctionnelle FAST descriptif, partiel ci-dessous du
>    micro-tour, en indiquant les solutions associées aux fonctions techniques correspondantes à
>    la fonction principale FP1.

Arbre imprimé (colonne de solutions non intitulée, cases vides à 2 lignes) :

- **FP1 : Permettre à l'utilisateur de réaliser des pièces à partir de brut**
  - FT1 : Fixer la pièce → *solution à trouver*
  - FT2 : Fixer l'outil → *solution à trouver*
  - FT3 : Alimenter la machine → *solution à trouver*
  - FT4 : Commander la machine → *solution à trouver*
  - FT5 : Déplacer l'outil selon l'axe X et l'axe Z → *(pas de case en regard)*
  - FT6 : Animer la pièce d'un mouvement de rotation → *(pas de case en regard)*
  - FT7 : Sécuriser la machine → *solution à trouver*

*Question 2 (p.37)* — consigne verbatim :

> 2. Compléter le diagramme F.A.S.T relatif à la fonction technique : FT5 : « Déplacer l'outil
>    selon l'axe X et l'axe Z »

Colonne **Solutions associées aux fonctions techniques** (cases vides). Arbre :

- **FT5 : Déplacer l'outil selon l'axe X et l'axe Z**
  - **FT51 : Déplacer le traînard (31) suivant l'axe Z** → *solution à trouver*
    - FT511 : Convertir l'énergie → *solution à trouver*
    - FT512 : Transformer la rotation de l'**arbre moteur (38)** en translation du **traînard (31)**
      suivant l'axe Z *(pas de case solution)*
      - **FT5121:....................................** *(intitulé lui-même à compléter par l'élève)*
    - FT513 : Assurer le guidage en translation du **traînard (31)** suivant l'axe Z →
      *solution à trouver*
  - **FT52 : Déplacer le chariot porte outil (7) suivant l'axe X** *(pas de case solution, pas de
    sous-arbre)*

*Question 3 (p.37)* — consigne verbatim :

> 3. Compléter le diagramme FAST relatif à la fonction technique FT5121

Colonne **Solutions technologiques** (cases vides). Arbre :

- **FT5121 : Interposer une liaison hélicoïdale**
  - **FT51211 : Assurer la rotation de la vis (26)**
    - FT512111 : Lier la vis à l'arbre moteur → *solution à trouver*
    - FT512112 : Guider la vis en rotation → *solution à trouver*
  - **FT51212 : Assurer la translation de l'écrou (25)**
    - FT512121 : Lier l'écrou au **traînard (31)** → *solution à trouver*

*Question 4 (p.38)* — consigne verbatim :

> 4. Compléter le schéma cinématique en précisant l'emplacement de chaque fonction technique
>    figurant dans les F.A.S.T. qui précèdent.

**Schéma cinématique à compléter (p.38)** : schéma cinématique plan de la chaîne
moteur → vis mère → traînard. Éléments donnés : la légende **Traînard** (flèche vers la liaison
supérieure), la légende **Moteur (38)** (boîtier à droite), le repère **FT₅₁₃** (flèche vers la
liaison basse) et le symbole de bâti (hachures) sous l'ensemble. Trois liaisons de la chaîne sont
entourées de bulles en pointillés avec des étiquettes vides `………` à renseigner (au-dessus de la
liaison hélicoïdale, du palier intermédiaire et de l'accouplement moteur), plus une étiquette vide
`………` sur la gauche. La liaison hélicoïdale (symbole en trait bleu ondulé) et l'axe de la vis
sont tracés ; la liaison glissière du traînard est en trait rouge.

*Question 5 (p.38)* — consigne verbatim :

> 5. Compléter le diagramme F.A.S.T relatif à la fonction technique FT6 : « Animer la pièce d'un
>    mouvement de rotation » en indiquant les noms de composants.

Colonne **Processeurs** (cases vides). Arbre :

- **FT6 : Animer la pièce d'un mouvement de rotation**
  - FT61 : Convertir l'énergie électrique en énergie mécanique → *processeur à trouver*
  - FT62 : Adapter l'énergie mécanique en rotation à la **broche (11)** → *deux cases processeur à
    trouver*
  - FT63 : Lier la **poulie réceptrice (13)** à la **broche (11)** → *processeur à trouver*
  - FT64 : Assurer Le guidage en rotation de la **broche (11)** → *processeur à trouver*
  - FT65 : Lier le **mandrin porte pièce (8)** à la **broche (11)** → *processeur à trouver*
  - FT66 : Lier le moteur au **banc de la machine (22)** → *processeur à trouver*

- **Données numériques de l'énoncé (activité 3)** : échelles de la planche p.33 — **1:5**
  (ensemble), **2:5** (coupe B-B), **1:2** (détail D), **4:5** (détail E) ; **1:2** pour le
  sous-ensemble support pièce (p.34). Éléments filetés de la nomenclature : **Vis HC M6x8** (×2),
  **Vis CHC M6x25 à téton long** (×6), **Vis CHC M6 x 20** (×2), **Vis CHC M5 x 16** (×2),
  **Vis HC M6 x 25** (×2), **Goujon M8 x 28** (×3), **Écrou à encoches KM-M38** (×2),
  **Écrou à encoches KM-M10** (×2) ; **2 moteurs pas à pas (38)**, **2 volants (40)**,
  **2 accouplements (37)**, **2 roulements à rouleaux coniques (10)**, **4 butées à billes**
  (2 en rep. 35 + 2 en rep. 44), **6 vis à tête cylindrique à six pans creux (12)**.
- **Vocabulaire & terminologie officielle (activité 3)** : machine-outil à commande numérique ;
  G-code ; **F.A.O** ; traînard, chariot transversal, chariot porte-outil, tourelle porte-outil,
  porte-outil, tablier de chariot, banc, contre glissière, vis mère, écrou de la vis mère, palier
  vis mère, vis d'entraînement, vis de manœuvre, volant, tambour gradué, indicateur de position ;
  broche, mandrin (porte pièce), mors, poupée mobile, flasque, clavette parallèle, poulie motrice /
  poulie réceptrice, courroie crantée, encodeur, cage, axe de centrage, écrou à encoches, rondelle
  Grower, vis à téton long ; moteur pas à pas, moteur à courant continu, moteur d'avance,
  microcontrôleur, carte de puissance ; opérations de pointage, centrage, perçage, alésage ;
  origine machine **Om**, origine pièce **Op** ; **liaison hélicoïdale**, guidage en translation,
  guidage en rotation, **schéma cinématique** ; carter et bouton d'arrêt d'urgence, capot de
  sécurité.

---

##### Synthèse — Analyse fonctionnelle interne d'un produit (p.39–40)

*(Bandeau « Synthèse » en tête de la p.39 ; en-tête CD 2.2 / CD 3.8 sur les deux pages.)*

**1. Auto-évaluation (p.39)** — verbatim :

> Tester vos connaissances avec les Quiz avant de passer à la synthèse.

*(Accompagné d'un **QR code étiqueté `EXE`** donnant accès aux quiz.)*

**2. Synthèse architecture fonctionnelle d'un système technique (p.39)** — encadré officiel
(fond vert), verbatim :

> Un système automatisé est composé de plusieurs éléments qui exécutent un ensemble de tâches
> programmées sans que l'intervention de l'homme ne soit nécessaire.
>
> **1. Chaîne d'information**
>
> C'est la partie du système automatisé qui capte l'information et qui la traite.
> On peut découper cette chaîne en plusieurs blocs fonctionnels.
>
> *(schéma : **Acquérir** → **Traiter** → **Communiquer** ; entrées à gauche « Consigne de
> l'utilisateur » et « Information extérieure au système » ; sorties à droite « Information pour
> l'utilisateur » et « Ordres pour la chaîne d'énergie »)*
>
> - **Acquérir :** Fonction qui permet de prélever des informations à l'aide de capteurs.
> - **Traiter :** C'est la partie commande composée d'un automate ou d'un microcontrôleur.
> - **Communiquer :** Cette fonction assure l'interface entre l'utilisateur et/ou d'autres
>   systèmes et l'environnement de la partie commande.
>
> **2. Chaîne d'énergie**
>
> Dans un système automatisé, on appelle une chaîne d'énergie l'ensemble des procédés qui vont
> réaliser une action.
> On peut découper cette chaîne en plusieurs blocs fonctionnels.
>
> *(schéma : **Alimenter** → **Distribuer** → **Convertir** → **Transmettre** ; entrée à gauche
> « Energie d'entrée » ; entrée verticale « Ordres » au-dessus du bloc Distribuer ; sortie à
> droite « Réalisation de l'action »)*
>
> - **Alimenter :** Mise en forme de l'énergie externe en énergie compatible pour créer une
>   action.
> - **Distribuer :** Distribution de l'énergie à l'actionneur réalisée par un distributeur, un
>   contacteur (interrupteur commandé à distance) ou une carte de puissance.
> - **Convertir :** L'organe de conversion d'énergie appelé actionneur peut être un vérin, un
>   moteur…
> - **Transmettre :** Cette fonction est remplie par l'ensemble des organes mécaniques de
>   transmission de mouvement et d'effort : engrenages, courroies,

*(La dernière phrase de la p.39 s'arrête bien sur « engrenages, courroies, » — virgule finale,
énumération inachevée dans la source ; elle n'est pas reprise en p.40.)*

**3. Fonctions techniques associées aux fonctions de service (p.40)** — encadré officiel
(fond vert), verbatim :

> La méthode F.A.S.T aide à penser au problème de façon objective et permet de déterminer la
> portée du projet en illustrant les relations logiques entre les fonctions.
> Un diagramme F.A.S.T aborde trois questions clés :
> - Comment accomplit-on cette fonction ?
> - Pourquoi réalise-t-on cette fonction ?
> - Quand on fait cette fonction, quelles autres fonctions doivent être faites ?
>
> Le diagramme suivant illustre la façon dont une fonction est étendue dans les directions
> «Quand ?», «Comment ?» et «Pourquoi ?» d'un diagramme F.A.S.T.

**Diagramme type F.A.S.T (p.40)** — trois colonnes titrées **Fonction de service** |
**Fonctions techniques** | **Solutions technologiques**. Structure imprimée :

- **Fonction de service** (bloc vert) se décompose en :
  - **Fonctions techniques 1** (bloc rose) → **Solutions technologiques 1** (bloc bleu)
  - **Fonctions techniques 2** (bloc rose) → **Solutions technologiques 2** *et*
    **Solutions technologiques 3** (bloc bleu), les deux solutions étant reliées par un
    opérateur **ET** (flèches en pointillés)
  - **Fonctions techniques 3** (bloc rose) → **Solutions technologiques 4** (bloc bleu)
- L'opérateur **OU** (flèches en pointillés) est porté à la bifurcation qui sépare la branche
  directe de **Fonctions techniques 1** du tronc vertical desservant **Fonctions techniques 2**
  et **3**.

**Savoirs plus (p.40)** — verbatim :

> **Savoirs plus** (espace réservé pour les remarques, astuces, conseils… à rédiger par
> l'apprenant)

*(Suivi de 15 lignes pointillées vierges.)*

En pied de p.40 : **« Grille d'évaluation des savoirs et savoir-faire de l'apprenant »** avec un
**QR code étiqueté `PDF`**.

##### Bornes de scope observées — p.12–40

- ✅ INCLUS :
  - **Décomposition d'un produit en chaînes fonctionnelles** : chaîne d'information
    (Acquérir / Traiter / Communiquer) et chaîne d'énergie (Alimenter ou Alimenter-Stocker /
    Distribuer / Convertir / Transmettre), avec identification des **processeurs** de chaque bloc
    et des **natures d'énergie** échangées (EE électrique, EM mécanique, E<sub>Th</sub> thermique)
    et des **pertes** — traité trois fois, sur trois supports (p.16, 27, 35) et synthétisé p.39.
  - **Fonctions techniques associées aux fonctions de service** via le **diagramme F.A.S.T**
    descriptif : construction de l'arbre FS/FP → FT → sous-FT → processeur / composant / solution
    constructive (p.17, 18, 28, 29, 30, 36, 37, 38), et la règle générale + les opérateurs **OU** /
    **ET** en synthèse p.40.
  - **Trois supports d'étude complets** avec dossier technique : micro-fraiseuse (dessin d'ensemble
    du chariot transversal + nomenclature 20 repères), imprimante 3D (3 planches + nomenclature
    69 repères + extrait de CdCF), micro-tour (dessin d'ensemble + nomenclature 53 repères).
  - **Mise en œuvre réelle des machines** : montage d'outil, réglage de l'origine pièce, chargement
    d'un fichier G-code, observation des déplacements, vérification de l'écoulement de matière —
    avec les consignes de sécurité associées (p.17, 26, 36).
  - **Lecture d'un extrait de CdCF** (FP / FC, critères d'appréciation, niveaux-flexibilités) —
    uniquement pour l'imprimante 3D (p.20).
  - **Lecture / complètement d'un schéma cinématique** (une seule occurrence : p.38).
  - Notions d'**origine machine (Om)** et d'**origine pièce (Op)** (p.13 et p.32).
- ⛔ EXCLU / seulement mentionné :
  - **L'analyse fonctionnelle EXTERNE** (bête à cornes, pieuvre, rédaction du CdCF) : le CdCF est
    posé comme **déjà exprimé** (« Le besoin étant exprimé dans le CdCF… », p.16, 26, 35) ; seul
    un **extrait** de CdCF est fourni, jamais construit.
  - **Le G-code lui-même** : le langage est nommé (p.31) et les fichiers sont fournis par QR code,
    mais aucune instruction, aucune syntaxe, aucune programmation n'est enseignée. Les fichiers
    sont « préparés à l'avance par l'enseignant » (p.17, 27, 36).
  - **Les conditions de coupe, la génération de trajectoires, la simulation d'usinage** : la C F A O
    et la F.A.O sont citées (p.13, 31) sans être traitées.
  - **La modélisation / le dimensionnement des liaisons et des solutions constructives** : la
    typologie des assemblages, la transmission de puissance et le comportement du solide déformable
    sont les thèmes de l'AXE 2 (p.87 et suivantes) ; ici on **nomme** guidage prismatique, liaison
    hélicoïdale, rattrapage de jeu sans les étudier.
  - **L'électronique de commande** : carte de puissance, microcontrôleur, DCN, encodeur, capteurs
    fin de course sont désignés comme processeurs, jamais analysés.
  - **Toutes les cases des diagrammes et des tableaux à compléter sont vierges** dans le manuel
    d'activités : aucun corrigé, aucune solution n'est imprimée dans cette tranche (le manuel est
    un manuel d'**activités** ; aucun guide enseignant n'accompagne le couple).
  - **La grille d'évaluation** (p.40) et les **quiz d'auto-évaluation** (p.39) ne sont pas imprimés :
    ils sont renvoyés à des ressources externes par QR code (`PDF`, `EXE`).

### AXE 2 — L'analyse structurelle et conception (p.41–251)

#### Thème : COMMUNICATION TECHNIQUE (p.41–86)

*(Le thème est transcrit en entier ci-dessous, p.41 à p.86.)*

##### Ouverture du thème — Séquence « Définition des éléments d'un produit » (p.41)

Page d'ouverture, composée de quatre bandeaux empilés puis d'un tableau.

Bandeaux, transcrits tels qu'imprimés :

> **AXE 2**
> **ANALYSE STRUCTURELLE ET CONCEPTION**
>
> **THÈME**
> **COMMUNICATION TECHNIQUE**
>
> **SÉQUENCE**
> **Définition des éléments d'un produit**

Encadré **COMPOSANTES DES COMPÉTENCES DISCIPLINAIRES** (verbatim) :

> **CD 3.2: Décoder un dessin d'ensemble.**
> **CD 3.5: Déterminer une condition fonctionnelle.**
> **CD 3.7: Tracer une chaine de cotes et calculer une cote fonctionnelle.**
> **CD 2.5: Modéliser une pièce d'un mécanisme en 3D et 2D en utilisant des logiciels appropriés.**
> **CD 3.3: Représenter le dessin de définition d'une pièce extraite d'un système.**

Tableau « **Définition des éléments d'un produit** » (colonnes : CD / Savoirs et savoir-faire /
Critères d'évaluation). La colonne « Savoirs et savoir-faire » est une cellule unique fusionnée
en regard des cinq CD ; les critères sont répartis en quatre cellules.

| CD | Savoirs et savoir-faire | Critères d'évaluation |
| --- | --- | --- |
| CD 3.2 | **Définition des éléments d'un produit:**<br>- Lecture d'un dessin d'ensemble.<br>-Graphe de montage et démontage.<br>- Cotation fonctionnelle.<br>- Représentation d'un produit fini :<br>•Coupes particulières.<br>•Sections.<br>- Modélisation numérique (3D et 2D).<br>- Désignation des matériaux (Rappel). | Décodage adéquat d'un dessin d'ensemble. |
| CD 3.5 | *(cellule fusionnée, voir ci-dessus)* | *(vide — un QR code « PDF » occupe la case)* |
| CD 3.7 | *(cellule fusionnée)* | Calcul correct des cotes fonctionnelles. |
| CD 3.3 | *(cellule fusionnée)* | Respect avec exactitude des règles et des conventions de représentation. |
| CD 2.5 | *(cellule fusionnée)* | Modélisation exacte d'une pièce en 3D et 2D. |

- **Ressource numérique** : un QR code étiqueté **PDF** est placé dans le tableau (p.41).
- **Bandeau de page (p.42 à p.64)** : toutes les pages de la séquence portent le bandeau jaune
  « **DÉFINITION DES ELEMENTS D'UN PRODUIT** » [sic — « ELEMENTS » sans accent]. La pastille bleue
  de gauche porte la ou les compétences travaillées (CD 3.2, CD 3.5, CD 3.7, CD 3.3) sur les pages
  de travail, et **reste vide sur les pages de présentation de support** (p.42–44, p.51–52,
  p.60–64).

---

##### Activité 1 — Perceuse sensitive : Présentation du support d'activité (p.42–44)

- **Système / support d'étude** : **perceuse sensitive** (machine-outil de perçage).
- **Compétences affichées** : aucune pastille CD sur p.42, p.43 et p.44 (la pastille du bandeau
  est vide sur ces trois pages de présentation).
- **Mise en situation (p.42, verbatim)** :

  > **1. Mise en situation**
  > La perceuse sensitive est une machine-outil servant à réaliser des opérations de perçage.
  > Elle se compose essentiellement :
  > - D'un moteur électrique ;
  > - D'un système de transmission de mouvement ;
  > - D'une colonne ;
  > - D'une broche et un mandrin portant l'outil ;
  > - D'un étau pour le maintien de la pièce.

- **Photo légendée (p.42)** : perspective couleur de la perceuse, sept annotations —
  « Bloc de transmission », « Couvercle », « Moteur électrique », « Mandrin », « Etau » [sic —
  sans accent], « Colonne », « Support ». Le bloc de transmission (poulies étagées + courroie)
  est cerclé en pointillés rouges.

- **Description (p.42, verbatim)** :

  > **2. Description**
  > Le dessin d'ensemble représente partiellement la partie de transmission de puissance de la
  > perceuse ainsi que le mécanisme de commande de déplacement de la broche.

- **Dessin d'ensemble (p.43)** — cartouche : **« Perceuse sensitive »**, **Echelle: 3:5**,
  symbole de disposition des vues (projection européenne). Le dessin comporte :
  - une **coupe B-B** (moitié haute) montrant l'ensemble poulie étagée / moyeu / broche /
    roulements ; repères portés à gauche, de haut en bas : **12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1** ;
    à droite, de haut en bas : **17, 16, 15, 14, 13**. Axe **y** en haut ;
  - une **coupe A-A** (moitié basse) montrant le boîtier de commande ; repères à gauche :
    **21, 20, 19, 18** ; à droite : **23, 22, 25, 24**. Axes **x** et **z** ;
  - les plans de coupe repérés **A-A**, **B-B**, **C-C**, **D-D** sur les vues ;
  - une **coupe D-D (5 seule)**, **Echelle: 1:1** — section circulaire de la broche (5) montrant
    la forme carrée du tronçon guidé ;
  - une **coupe C-C**, **Echelle: 1:1** — section du ressort spiral logé dans le couvercle ;
  - une **perspective annotée** du mécanisme de commande : « **Foureau (4) (crémaillère)** »
    [sic — « Foureau », alors que la nomenclature p.44 écrit « Fourreau »], « **Pignon (13)** »,
    « **Bras de commande (24)** » ;
  - une **perspective annotée** du ressort spiral : « **Ressort (22)** », « **Couvercle (21)** ».

- **Nomenclature (p.44)** — 25 repères :

| Rep. | Nbr. | Désignation | Matière | Observation |
| --- | --- | --- | --- | --- |
| 1 | 2 | Roulement à une rangée de billes à contact radial | 100 Cr6 | |
| 2 | 1 | Bague entretoise | C60 | |
| 3 | 1 | Bâti | EN GJL 250 | |
| 4 | 1 | Fourreau | C35 | |
| 5 | 1 | Broche | C35 | |
| 6 | 1 | Anneau élastique pour arbre | | |
| 7 | 1 | Rondelle plate | | |
| 8 | 2 | Roulement à une rangée de billes à contact radial | 100 Cr6 | |
| 9 | 1 | Bague entretoise | C60 | |
| 10 | 1 | Anneau élastique pour alésage | | |
| 11 | 1 | Moyeu | 36 Ni Cr Mo16 | |
| 12 | 1 | Poulie étagée | Al Si 10 Mg | |
| 13 | 1 | Pignon | C35 | |
| 14 | 1 | Anneau élastique pour arbre | | |
| 15 | 1 | Boîtier | EN GJL 200 | |
| 16 | 4 | Vis à tête cylindrique à six pans creux | | |
| 17 | 1 | Écrou spécial | | |
| 18 | 1 | Écrou-frein | | |
| 19 | 1 | Vis sans tête à six pans creux à téton long | | |
| 20 | 1 | Anneau élastique pour arbre | | |
| 21 | 1 | Couvercle | C60 | |
| 22 | 1 | Ressort spiral | 60 Si Cr 7 | |
| 23 | 2 | Écrou hexagonal | | |
| 24 | 3 | Bras de commande | S235 | |
| 25 | 1 | Coussinet | Cu Sn 8 | |

- **Vocabulaire & terminologie officielle** : perceuse sensitive, machine-outil, perçage, bloc de
  transmission, broche, mandrin, fourreau (crémaillère), pignon, bras de commande, poulie étagée,
  moyeu, ressort spiral, coussinet, bague entretoise, anneau élastique (pour arbre / pour alésage),
  écrou-frein, vis sans tête à téton long, bâti, boîtier.

---

##### Activité 1.1 (p.45–46)

*(Intitulé porté par le sommaire p.4 : « Lecture d'un dessin d'ensemble ». La page elle-même
n'imprime que « Activité 1.1 ».)*

- **Système / support d'étude** : perceuse sensitive (dossier technique p.42–44).
- **Compétences affichées** : **CD 3.2** (p.45 et p.46).
- **Pictogrammes de compétences transversales (p.45)** : **COOP**, **CREA**.
- **Ressources fournies** : dossier technique de la « Perceuse Sensitive » (dessin d'ensemble
  p.43, nomenclature p.44) ; la machine réelle (manipulation) ; un tableau Fonction/Processeur à
  compléter (p.45) ; un tableau des liaisons mécaniques à compléter (p.46).
- **Données numériques de l'énoncé** : foret de **diamètre 5 mm** ; trou débouchant de
  **diamètre 5 mm** (p.45).

- **Encadrés officiels (verbatim)** :

  > **I. Situation déclenchante**
  > Un dessin d'ensemble est destiné à mettre en évidence comment des pièces sont assemblées les
  > unes avec les autres afin de comprendre le fonctionnement d'un système.
  > **Comment peut-on décoder un dessin d'ensemble et découvrir ses détails ?**

  Consigne de sécurité imprimée en rouge, avec pictogramme triangulaire d'avertissement :

  > Vérifier les consignes de sécurité à respecter relativement à cette activité.

- **Travail demandé** :

  **A. Préparation de la machine pour une opération de perçage**

  1. Monter un foret de diamètre 5mm dans le mandrin et fixer la pièce.
  2. Régler en hauteur le plateau porte pièce.
  3. Mettre la machine en marche en présence de l'enseignant.
  4. Percer un trou débouchant de diamètre 5mm.

  **B. Analyse fonctionnelle** — « En se référant au dossier technique de la "Perceuse
  Sensitive" ; »

  1. Déterminer :
     - La fonction globale ……
     - La matière d'œuvre entrante ……
     - La matière d'œuvre sortante ……
  2. Compléter le tableau suivant soit par la fonction technique, soit par le processeur associé.

     | Fonction | Processeur |
     | --- | --- |
     | Fixer la poulie étagée (12) au moyeu (11) | *(à compléter)* |
     | *(à compléter)* | Deux roulements (8) |
     | Guider en translation la broche (5) par rapport au moyeu (11) | *(à compléter)* |
     | Guider en rotation la broche (5) | *(à compléter)* |
     | *(à compléter)* | Vis sans tête (19) + Écrou frein (18) |

  3. Par quoi est assurée la liaison encastrement entre le moyeu (11) et la poulie étagée (12)?
     (Obstacle ou Adhérence) : …… / Justifier : ……
  4. Décrire les fonctions des pièces suivantes :
     - Ressort (22) : ……
     - Coussinet (25) : ……
     - Écrou (18) + Vis sans tête (19) : ……
     - Les deux écrous (23) : ……
  5. Pourquoi le constructeur a-t-il choisi la forme carrée pour le guidage en translation de la
     broche par rapport au moyeu (11) ? Proposer une autre solution technologique.
     …… / Autre solution : ……
  6. Donner la désignation normalisée des composants suivants. (Voir dessin d'ensemble)
     - L'élément (8) : ……
     - L'élément (19) : ……
     - L'élément (20) : ……
  7. Déchiffrer les désignations des matériaux suivants :
     - 100 Cr 6 : ……
     - EN GJL 250 : ……
     - Al Si 10 Mg : ……
  8. Remplir le tableau des liaisons mécaniques suivant :

     | Repères | Nature de la liaison | Symbole |
     | --- | --- | --- |
     | (13)/(3) | *(à compléter)* | *(à compléter)* |
     | (4)/(13) | *(à compléter)* | *(à compléter)* |
     | (4)/(3) | *(à compléter)* | *(à compléter)* |
     | (4)/(3+18+19) | *(à compléter)* | *(à compléter)* |

- **Vocabulaire & terminologie officielle** : dessin d'ensemble, décoder, fonction globale,
  matière d'œuvre entrante / sortante, fonction technique, processeur, liaison encastrement,
  obstacle / adhérence, désignation normalisée, guidage en translation, guidage en rotation,
  nature de la liaison, symbole (de liaison).

---

##### Activité 1.2 — Graphe de montage et de démontage (p.47)

- **Système / support d'étude** : perceuse sensitive.
- **Compétences affichées** : **CD 3.2**.
- **Pictogramme de compétence transversale** : **CREA**.
- **Ressources fournies** : un **graphe de démontage « filogramme » partiel** accompagné d'un
  tableau Outillages / Observations ; un **graphe de montage « râteau »** partiel sur trame
  quadrillée.
- **Données numériques de l'énoncé** : outillage « **Clé plate de 8** » (deux fois).

- **Encadré officiel (verbatim)** :

  > **I. Situation problème**
  > Dans le cadre d'une maintenance corrective, l'équipe chargée d'entretien a décidé de changer
  > le ressort défectueux (22) ;
  > **Comment doit-on procéder pour le changer ?**

  *(Sur cette page, la rubrique « II. Travail demandé » n'est pas imprimée : elle est remplacée
  par le titre en gras « Graphe de montage et de démontage ».)*

- **Travail demandé** :

  1. Compléter le graphe de démontage "filogramme" partiel ci-dessous relatif à la perceuse
     sensitive, permettant l'intervention pour remplacer le ressort défectueux (22).

     Structure du filogramme imprimé (axe vertical intitulé « **Repère d'ordre** ») : boîte de
     tête « **Perceuse sensitive** » ; sorties numérotées **1 → « 23' »**, **2 → « .... »**
     (à compléter), **3 → « ............. »** (à compléter), puis une sous-étape
     **3.1 → « ..... »** (à compléter) et une boîte « **21** » ; boîte de pied
     « **Sous- ensemble restant** ».

     Tableau associé, imprimé en regard :

     | Outillages | Observations |
     | --- | --- |
     | Clé plate de 8 | Prévoir deux clés — Déposer le contre écrou (23') |
     | Clé plate de 8 | Déposer l'écrou (23) |
     | Manuelle | Déposer le couvercle (21) avec le ressort (22) |
     | Extracteur de ressort | Extraire le ressort (22) à changer |

  2. Compléter le graphe de montage "râteau" ci-dessous relatif à la perceuse sensitive pour le
     changement du ressort (22).

     Trame quadrillée pré-remplie : colonne de boîtes **23'**, **23**, **22**, **21** ; boîte
     « **Sous- ensemble restant « Cabestan »** » ; flèche vers « **Ensemble perceuse sensitive** ».

- **Vocabulaire & terminologie officielle** : maintenance corrective, graphe de démontage,
  filogramme, graphe de montage, râteau, repère d'ordre, sous-ensemble restant, contre écrou,
  extracteur de ressort, cabestan.

- **Remarque de lecture** : le repère **23'** (contre-écrou) est utilisé ici et sur la figure de
  la p.48, alors que la nomenclature p.44 ne porte que le repère **23 — Écrou hexagonal, Nbr. 2**.

---

##### Activité 1.3 (p.48–49)

*(Intitulé porté par le sommaire p.4 : « Cotation fonctionnelle ». La page n'imprime que
« Activité 1.3 ».)*

- **Système / support d'étude** : perceuse sensitive.
- **Compétences affichées** : **CD 3.5** et **CD 3.7** (p.48 et p.49).
- **Pictogrammes de compétences transversales (p.48)** : **COMM**, **COOP**, **CRITI**.
- **Ressources fournies** : trois figures à annoter — (a) p.48, coupe partielle du boîtier de
  commande support de la condition **JA** ; (b) p.49, dessin de définition partiel du **pignon
  (13)** ; (c) p.49, coupe de l'ensemble poulie/moyeu/broche support des conditions **JB** et
  **JC** ; (d) p.49, dessin de définition partiel du **Moyeu (11)**.
- **Données numériques de l'énoncé (p.48, question 4)** :
  **0 ≤ JA ≤ 0,2 ; A3 = 58±0,02 ; A20 = 1h11 ; A25 = 2±0,02**.

- **Encadré officiel (verbatim, p.48)** :

  > **I. Situation problème**
  > La détermination des côtes [sic] d'une pièce, nécessite le respect d'une (ou des) condition
  > (s) fonctionnelle(s), assurant le bon fonctionnement du mécanisme ;
  > **Comment doit-on procéder pour justifier ces conditions et tracer leurs chaines de cotes ?**

- **Travail demandé** :

  1. Justifier la présence de la condition JA ……
  2. Tracer la chaîne de cotes relative à la condition JA.

     Figure (p.48) : coupe verticale du boîtier de commande. Repères portés en haut :
     **21, 22, 23, 23'** ; à gauche, de haut en bas : **20, 25, 3, 19, 18, 13, 24**. La condition
     **JA** est figurée à droite par une flèche verticale (jeu axial du sous-ensemble ressort /
     couvercle sur l'axe du pignon).
  3. Établir les équations permettant de trouver :
     - J<sub>A</sub> = ……
     - J<sub>AMaxi</sub> = ……
     - J<sub>Amin</sub> = ……
  4. A partir de la chaine de cotes relative à la condition JA, Calculer la cote tolérancée
     A<sub>13</sub> de la pièce (13). On donne : 0≤JA≤0,2 ; A3 = 58<sup>±0,02</sup> ; A20 = 1h11;
     A25 = 2<sup>±0,02</sup>
  5. Sur le dessin de définition du pignon (13), porter la cote fonctionnelle relative à la
     condition JA.

     Figure (p.49) : dessin de définition partiel du pignon **(13)** — arbre étagé avec denture,
     tronçon fileté et extrémité prismatique, dessiné sans cotes.
  6. La condition J<sub>C</sub> est-elle minimale ou maximale ? Justifier.
  7. Tracer ci-dessous les chaînes de cotes relatives aux deux conditions J<sub>B</sub> et
     J<sub>C</sub>.

     Figure (p.49) : coupe de l'ensemble poulie étagée / moyeu / broche / roulements. Repères
     portés à gauche, de haut en bas : **17, 12, 11, 10, 16, 8', 9, 8, 3, 15, 7, 14**. Trois
     repérages de conditions à droite : **JB** (en haut), **Jeu** (au milieu), **JC** (en bas) ;
     une ligne horizontale repérée « **Plan de Jauge** » traverse la vue.
  8. Sur le dessin de définition du Moyeu (11), porter les cotes fonctionnelles relatives aux
     conditions J<sub>B</sub> et J<sub>C</sub>.

     Figure (p.49) : dessin de définition partiel du moyeu **(11)** — pièce tubulaire étagée en
     coupe, avec repère **11** et une ligne repérée « **Plan de Jauge** ».

- **Vocabulaire & terminologie officielle** : condition fonctionnelle, chaîne de cotes, cote
  fonctionnelle, cote tolérancée, condition minimale / maximale, plan de jauge, jeu, dessin de
  définition, tolérance ISO (h11).

- **Remarque de lecture** : le repère **8'** (p.49) désigne le second roulement de la paire
  repérée **8** (Nbr. 2) à la nomenclature p.44 ; il n'a pas de ligne propre au tableau.

---

##### Activité 1.4 (p.50)

*(Intitulé porté par le sommaire p.4 : « Dessin de définition ». La page n'imprime que
« Activité 1.4 ».)*

- **Système / support d'étude** : perceuse sensitive — pièces **fourreau (4)** et **moyeu (11)**.
- **Compétences affichées** : **CD 3.3**, **CD 3.5**, **CD 3.7**.
- **Pictogrammes de compétences transversales** : **COMM**, **COOP**, **CREA**.
- **Ressources fournies** : deux amorces de dessin de définition à compléter (fourreau (4) et
  moyeu (11)), avec cadres de tolérances géométriques et symboles d'état de surface déjà placés.
- **Données numériques de l'énoncé** : **Echelle 3:4** (les deux dessins).

- **Encadré officiel (verbatim)** :

  > **I. Situation problème**
  > Certaines pièces présentent des formes situées dans des plans parallèles ou sécants. Une coupe
  > particulière est nécessaire pour montrer ces formes sur une même vue.
  > **Quelle méthode peut-on utiliser pour réaliser cette coupe ?**

- **Travail demandé** :

  1. Compléter le dessin de définition du fourreau (4) à l'échelle 3:4 par :
     - La vue de face en coupe B-B ;
     - La vue de droite en coupe A-A ;
     - Inscrire les spécifications géométriques et les états de surfaces demandés.
     - Placer la tolérance nécessaire au bon fonctionnement du mécanisme.

     Figure : à gauche la vue **A-A** (contour circulaire, plan de coupe **B-B** repéré, cadre de
     tolérance géométrique vide, référence **A**) ; à droite la vue **B-B** (fourreau en long,
     plan de coupe **A-A** repéré, deux cadres de tolérance vides, un symbole de rugosité,
     un repère de référence). Mention **Echelle: 3:4**.
  2. Compléter le dessin de définition du moyeu (11) par :
     - La vue de face en demi coupe A-A ;
     - La vue de gauche en coupe B-B.

     Figure : moyeu **11** dessiné en long (alésage conique, tronçon fileté croisé), plans de
     coupe **A-A** et **B-B** repérés, vue de gauche amorcée par un cercle. Mention
     **Echelle: 3:4**.
  3. Modéliser le fourreau (4) en utilisant des logiciels appropriés.

- **Vocabulaire & terminologie officielle** : coupe particulière, plans parallèles ou sécants,
  vue de face, vue de droite, vue de gauche, demi coupe, spécifications géométriques, états de
  surfaces, tolérance, modélisation, dessin de définition.

---

##### Activité 2 — Poupée mobile : Présentation du support d'activité (p.51–52)

- **Système / support d'étude** : **poupée mobile** d'un **tour**.
- **Compétences affichées** : aucune pastille CD sur p.51 et p.52.
- **Mise en situation (p.51, verbatim)** :

  > **1. Mise en situation**
  > La poupée mobile d'un tour sert essentiellement à :
  > - Maintenir les pièces longues à usiner (montage mixte ; montage entre pointes).
  > - Supporter un mandrin de perçage (opérations : centrage, perçage...)
  > - Centrer l'outil.

  Une perspective couleur de la poupée mobile accompagne le texte (non légendée).

- **Nomenclature (p.51)** — 28 repères :

| Rep. | Nbr. | Désignation | Matière | Observation |
| --- | --- | --- | --- | --- |
| 1 | 1 | Banc | ENGJL200 | |
| 2 | 1 | Semelle | ENGJL200 | |
| 3 | 1 | Lardon | S275 | |
| 4 | 1 | Corps | ENGJL200 | |
| 5 | 1 | Clavette à ergot | S275 | |
| 6 | 1 | Pointe | | |
| 7 | 1 | Fourreau | 35NiCr6 | Trempé, rectifié |
| 8 | 1 | Écrou | S275 | |
| 9 | 1 | Manette | S275 | |
| 10 | 1 | Vis de manœuvre | 35NiCr6 | |
| 11 | 1 | Écrou | CuSn10P | |
| 12 | 4 | Vis à tête Hexagonale ISO4014-M6x60 | C30 | |
| 13 | 4 | Graisseur | | |
| 14 | 1 | Poignée | S275 | |
| 15 | 1 | Palier | ENGJL200 | |
| 16 | 1 | Bague vernier | | |
| 17 | 1 | Volant | ENGJL200 | |
| 18 | 1 | Vis à tête cylindrique à six pans creux ISO4762-M10x70 | | |
| 19 | 1 | Tampon | C30 | |
| 20 | 1 | Contre-tampon | C30 | |
| 21 | 1 | Goupille cylindrique ISO 8734-12x30-A | | |
| 22 | 1 | Anneau élastique | | |
| 23 | 1 | Axe–excentrique | C40 | |
| 24 | 1 | Manette | S275 | |
| 25 | 4 | Vis à tête cylindrique à six pans creux ISO 4762-M6x35 | | |
| 26 | 1 | Tirant | S 275 | |
| 27 | 1 | Écrou spécial | S 275 | |
| 28 | 1 | Bride | ENGJL200 | |

- **Dessin d'ensemble (p.52)** — cartouche : **« Poupée mobile »**, **Echelle: 1:4**, symbole de
  disposition des vues. Le dessin, imprimé en rotation (à lire page tournée), comporte :
  - une **coupe B-B**, portant la mention « **9-14-17 non représentées** » ; repères visibles :
    **18, 19, 20, 22, 23** ; axes **z** et **y** ; plan de coupe **A-A** repéré ;
  - une **coupe A-A** (vue principale) ; repères portés à gauche, de haut en bas : **21, 17, 16,
    15, 14, 13, 12, 11, 10, 9, 8, 7, 6** ; en bas : **5, 4, 3, 2, 28, 1** ; à droite : **24, 25,
    26, 27** ; axe **x** ; plans de coupe **A**, **B** et zones de détail **A** et **B** repérées ;
  - un **détail B**, **Echelle 1:1** — repères **25**, **15**, **4** ;
  - un **détail A**, **Echelle 1:1** — repères **4**, **12**, **11**, **7** ;
  - un **QR code étiqueté PDF**.

- **Vocabulaire & terminologie officielle** : poupée mobile, tour, montage mixte, montage entre
  pointes, mandrin de perçage, centrage, banc, semelle, lardon, corps, clavette à ergot, pointe,
  fourreau, vis de manœuvre, graisseur, bague vernier, volant, tampon / contre-tampon, goupille
  cylindrique, axe–excentrique, tirant, bride, palier.

---

##### Activité 2.1 (p.53–54)

*(Intitulé porté par le sommaire p.4 : « Lecture d'un dessin d'ensemble ». La page n'imprime que
« Activité 2.1 ».)*

- **Système / support d'étude** : poupée mobile (dossier technique p.51–52).
- **Compétences affichées** : **CD 3.2** (p.53 et p.54).
- **Pictogrammes de compétences transversales (p.53)** : **COMM**, **COOP**.
- **Ressources fournies** : la machine réelle (manipulation) ; un **diagramme FAST** partiel à
  compléter (p.53) ; un tableau de **classes d'équivalences cinématiques** à compléter et un
  **schéma cinématique** partiel à annoter (p.54).
- **Données numériques de l'énoncé** : « un foret de diamètre … mm » (valeur laissée en pointillés
  par le manuel, à choisir avec l'enseignant) ; matériaux à déchiffrer **S 275**,
  **35 Ni Cr 6**, **C30**.

- **Encadré officiel (verbatim, p.53)** :

  > **I. Situation déclenchante**
  > Un dessin d'ensemble est destiné à mettre en évidence comment des pièces sont assemblées les
  > unes avec les autres afin de comprendre le fonctionnement d'un système.
  > **Comment peut-on décoder un dessin d'ensemble et découvrir ses détails ?**

  Consigne de sécurité imprimée en rouge, avec pictogramme triangulaire :

  > Vérifier les consignes de sécurité à respecter relativement à cette activité.

  Consigne intermédiaire imprimée en gras entre les étapes 6 et 7 :

  > **Appeler l'enseignant pour choisir le diamètre de perçage et les conditions de coupe.**

- **Travail demandé** :

  **A. Préparation de la poupée pour une opération de perçage**

  1. Tourner le volant (17) à l'aide de la manette (24) pour démonter la pointe (6).
  2. Monter un mandrin de perçage à la place de la pointe (6).
  3. Monter un foret à centrer dans le mandrin de perçage.
  4. Fixer la pièce dans le mandrin porte pièce.
  5. Débloquer la poupée à l'aide du poignée (14), puis la déplacer près de la pièce à percer.
  6. Bloquer la poupée
  *(consigne en gras : appeler l'enseignant — voir ci-dessus)*
  7. Mettre la machine en marche en présence de l'enseignant.
  8. Tourner doucement le volant (17) jusqu'à l'exécution du centrage.
  9. Arrêter la machine, changer le foret à centrer par un foret de diamètre … mm.
  10. Mettre la machine en marche et terminer le perçage.
  11. Arrêter la machine, démonter la pièce et le mandrin de perçage, nettoyer la machine et
      ranger les outils.

  **B. Analyse fonctionnelle**

  1. Compléter le diagramme FAST de la "Poupée mobile" ;

     Diagramme FAST imprimé (colonne de droite intitulée « **Composants** ») :

     | Niveau | Contenu imprimé |
     | --- | --- |
     | FP | **FP:** Supporter un mandrin de perçage |
     | FT1 | FT1: Maintenir en position la poupée par rapport au banc → *(case à compléter)* → composants : **(14) ;(23) ;(26) ;(27) et (28)** |
     | FT2 | FT2: Assurer le déplacement du mandrin par rapport à la poupée → *(case à compléter)* → **FT211** Guider la vis de manœuvre (10) en rotation → *(composants à compléter)* ; **FT212** Guider le fourreau (7) en translation → *(composants à compléter)* |
     | FT3 | FT3: Maintenir le mandrin en position voulue → **FT31: Bloquer le fourreau à la position voulue** → *(composants à compléter)* |

  2. Justifier la présence des formes suivantes :
     - La forme conique à l'intérieur du fourreau (7) : ……
     - Deux méplats sur la manette (24) : ……
     - La rainure sur l'écrou (11) : ……
  3. Déchiffrer les désignations des matériaux des pièces suivantes :
     - La manette (9) est en S 275 : ……
     - La vis de manœuvre (10) est en 35 Ni Cr 6 : ……
     - Le tampon (19) est en C30 : ……
  4. Donner la fonction de chaque élément suivant :
     - Lardon (3) : ……
     - Graisseurs (13) : ……

  **C. Analyse du fonctionnement**

  1. Compléter les classes d'équivalences cinématiques ci-dessous par les pièces :1 ; 3 ; 5 ; 6 ;
     11 ; 12 ; 13 et 15.

     | Classe | Contenu imprimé |
     | --- | --- |
     | A | 2; …………… |
     | B | 6 ; …………… |
     | C | 10 ; …………… |

     Une figure accompagne le tableau : **schéma cinématique** partiel en perspective (liaison
     pivot, liaison glissière hachurée au bâti, liaison hélicoïdale figurée par un ressort/filet),
     avec trois étiquettes en pointillés à renseigner.

  2. Décrire la solution constructive réalisant la liaison encastrement entre le tampon (19) +
     contre tampon (20) et le fourreau (7), pendant la phase de blocage de ce dernier. ……
  3. Quelle est la solution technologique utilisée pour le guidage en translation de la semelle
     (2) par rapport au banc (1) ? Comment est rattrapé le jeu dans ce cas ? ……

- **Vocabulaire & terminologie officielle** : diagramme FAST, FP / FT / FT211 / FT212 / FT31,
  composants, classe d'équivalence cinématique, schéma cinématique, solution constructive,
  liaison encastrement, guidage en translation, rattrapage de jeu, méplat, rainure, forme conique,
  foret à centrer, conditions de coupe.

- **Remarque de lecture** : le matériau de la vis de manœuvre (10) est écrit **35NiCr6** à la
  nomenclature p.51 et **35 Ni Cr 6** dans la question 3 p.54 (même désignation, deux graphies).

---

##### Activité 2.2 — Graphe de montage et de démontage (p.55)

- **Système / support d'étude** : poupée mobile.
- **Compétences affichées** : **CD 3.2**.
- **Pictogrammes de compétences transversales** : **DECI**, **CREA**.
- **Ressources fournies** : un **graphe de démontage « filogramme » partiel** avec tableau
  Outillages / Observations ; un **graphe de montage « râteau »** partiel sur trame quadrillée.
- **Données numériques de l'énoncé** : « Déposer les **4** vis (12) ».

- **Encadré officiel (verbatim)** :

  > **I. Situation Problème**
  > Dans le cadre d'une maintenance préventive, l'équipe chargée d'entretien a décidé de changer
  > l'écrou (11), vu l'augmentation du jeu de fonctionnement entre ce dernier et la vis de
  > manœuvre (10).
  > **Comment doit-on procéder pour le changer ?**

- **Travail demandé** :

  **A. Graphe de montage et de démontage**

  1. Compléter le graphe de démontage "filogramme" partiel ci-dessous relatif à la poupée mobile,
     permettant l'intervention pour remplacer l'écrou (11).

     Structure du filogramme imprimé (axe vertical « **Repère d'ordre** ») : boîte de tête
     « **Poupée mobile** » ; sorties **1 → « 8, 9 »**, **2 → « 17 »**,
     **3 → « ........................... »** (à compléter), puis **3.1 → « ... »** (à compléter)
     et **3.2 → « 11 »** ; boîte « **6, 7** » ; boîte de pied « **Sous- ensemble restant** ».

     Tableau associé :

     | Outillages | Observations |
     | --- | --- |
     | Manuelle | Liberer [sic] le forreau [sic] (7) |
     | Manuelle | Manoeuvrer le volant (17) |
     | Manuelle | Déposer (6 ;7 ;11 ;12) |
     | Clé à pipe | Déposer les 4 vis (12) |
     | Extracteur | Déposer l'écrou (11) à changer |

  2. Compléter le graphe de montage "râteau" ci-dessous relatif à la poupée mobile assurant le
     remplacement de l'écrou (11).

     Trame quadrillée pré-remplie : colonne de boîtes **12**, **11**, **6, 7** ; boîte
     « **Sous- ensemble restant "Fourreau"** » ; flèche vers « **Ensemble poupée mobile** ».

- **Vocabulaire & terminologie officielle** : maintenance préventive, jeu de fonctionnement,
  filogramme, graphe de montage « râteau », repère d'ordre, sous-ensemble restant, clé à pipe,
  extracteur.

---

##### Activité 2.3 (p.56–57)

*(Intitulé porté par le sommaire p.4 : « Cotation fonctionnelle ». La page n'imprime que
« Activité 2.3 ».)*

- **Système / support d'étude** : poupée mobile.
- **Compétences affichées** : **CD 3.5** et **CD 3.7** (p.56 et p.57).
- **Pictogrammes de compétences transversales (p.56)** : **COOP**, **R. PRO**.
- **Ressources fournies** : figure p.56 — coupe partielle du corps/palier/volant portant les
  conditions **JA<sub>Maxi</sub>**, **JB** et un **Jeu** ; deux dessins de définition partiels
  (pièces **10** et **15**) ; figure p.57 — coupe partielle banc/semelle/corps/bride portant les
  conditions **JC** et **JD** ; dessin de définition partiel du **corps (4)**.
- **Données numériques de l'énoncé (p.57, question 6)** :
  **D4 = 43,25 ±0,04 ; D23 = 45 ; D22 = 1,75h11**.

- **Encadré officiel (verbatim, p.56)** :

  > **I. Situation Problème**
  > La détermination des côtes [sic] d'une pièce, nécessite le respect d'une (ou des) condition
  > (s) (Serrage ; Jeu …), assurant le bon fonctionnement du mécanisme.
  > **Comment doit-on procéder pour justifier ces conditions et tracer leurs chaînes de côtes [sic] ?**

- **Travail demandé** :

  1. Justifier la présence des conditions :
     - J<sub>A</sub> : ……
     - J<sub>B</sub> : ……
  2. Tracer les chaînes de cotes relatives aux deux conditions J<sub>A</sub> et J<sub>B</sub>.

     Figure (p.56) : coupe partielle de l'assemblage corps / palier / volant. Repères portés en
     haut, de gauche à droite : **4, 10, 15, 21, 17** ; repère **24** à droite (manette).
     Trois repérages de conditions : **Jeu** (au centre), **JA<sub>Maxi</sub>** et **JB** (en
     bas) ; une cote encadrée **17** est amorcée sous la chaîne JA<sub>Maxi</sub>.
  3. Reporter les cotes fonctionnelles sur les dessins de définition des pièces suivantes:

     Deux dessins de définition partiels, dessinés sans cotes : la **vis de manœuvre (10)** (à
     gauche, arbre avec tête et perçage transversal) et le **palier (15)** (à droite, pièce en
     coupe, alésage central).
  4. Justifier la présence des deux conditions J<sub>C</sub> et J<sub>D</sub> :
     - J<sub>C</sub> : ……
     - J<sub>D</sub> : ……
  5. Tracer les chaines de cotes installant les conditions J<sub>C</sub> et J<sub>D</sub>.

     Figure (p.57) : coupe partielle banc / semelle / corps / bride avec l'axe-excentrique.
     Repères portés à gauche, de haut en bas : **22, 23, 4, 2, 1, 28, 27** ; repère **26** en bas.
     Condition **J<sub>D</sub>** repérée en haut (verticale), condition **J<sub>C</sub>** repérée
     à droite.
  6. A partir de la chaîne de cotes relative à J<sub>D</sub>, calculer J<sub>DMaxi</sub> ;
     J<sub>Dmin</sub> et ITJ<sub>D</sub>
     On donne : D4 = 43,25 ±0,04 ; D23 = 45 ; D22 = 1,75h11.
     J<sub>DMaxi</sub> = ………… ; J<sub>Dmin</sub> = ………… ; ITJ<sub>D</sub> = …………
  7. Reporter les cotes fonctionnelles relatives aux corps [sic] (4) sur son dessin de définition
     ci-dessous :

     Dessin de définition partiel du **corps (4)** en coupe, sans cotes.

- **Vocabulaire & terminologie officielle** : condition de serrage, condition de jeu, chaîne de
  cotes, cote fonctionnelle, J<sub>Maxi</sub> / J<sub>min</sub>, IT (intervalle de tolérance),
  tolérance ISO (h11), dessin de définition.

---

##### Activité 2.4 (p.58–59)

*(Intitulé porté par le sommaire p.4 : « Dessin de définition ». La page n'imprime que
« Activité 2.4 ».)*

- **Système / support d'étude** : poupée mobile — pièces **fourreau (7)** et **palier (15)**.
- **Compétences affichées** : **CD 3.5** et **CD 3.7** (p.58 et p.59).
- **Pictogrammes de compétences transversales (p.58)** : **COOP**, **CREA**.
- **Ressources fournies** : amorces de dessin de définition à compléter — fourreau (7) (p.58,
  vue en long amorcée + vue de gauche circulaire amorcée) ; palier (15) (p.59, vue **A-A**,
  vue **A**, vue de dessus, cadres de spécifications géométriques vides).
- **Données numériques de l'énoncé** : **Echelle: 3:4** (p.58 et p.59).

- **Encadré officiel (verbatim, p.58)** :

  > **I. Situation Problème**
  > Certaines pièces présentent des formes situées dans des plans parallèles ou sécants. Une coupe
  > particulière est nécessaire pour montrer ces formes sur une même vue.
  > **Quelle méthode peut-on utiliser pour réaliser cette coupe ?**

- **Travail demandé** :

  **A. Fourreau (7)**

  1. Compléter le dessin de définition du fourreau (7) par :
     - La vue de face en coupe A-A ;
     - La vue de gauche.
  2. Inscrire la rugosité que vous attribuez à la surface A.

     Figure (p.58) : vue en long du fourreau, cassure conventionnelle, repère de surface **A** et
     symbole de rugosité vide ; à droite, vue de gauche amorcée (cercle avec plans de coupe **A**
     repérés et un logement de clavette esquissé). Mention **Echelle: 3:4**.
  3. Modéliser (en 3D) le fourreau (7) en utilisant des logiciels appropriés.

  **B. Palier (15)**

  1. Compléter la vue de face ;
  2. Compléter la vue de droite en coupe A-A (sans détails cachés) ;
  3. Compléter la vue de dessus ;
  4. Inscrire dans les cadres prévus les spécifications géométriques ;
  5. Inscrire les rugosités des surfaces fonctionnelles ;
  6. *(p.59)* Modéliser (en 2D) le palier (15) en utilisant des logiciels appropriés.

     Figures (p.59) : vue **A-A** amorcée avec repère de surface **A** et deux symboles de
     rugosité ; vue **A** carrée à angles arrondis avec quatre trous de fixation et plans de
     coupe **A** repérés ; vue de dessus du palier avec deux cadres de tolérance géométrique
     vides. Mention **Echelle: 3:4**.

- **Vocabulaire & terminologie officielle** : coupe particulière, vue de face / de gauche / de
  droite / de dessus, détails cachés, rugosité, surfaces fonctionnelles, spécifications
  géométriques, modélisation 2D / 3D.

---

##### Activité 3 — Pince de soudage : Présentation du support d'activité (p.60–64, début)

*(Le travail demandé de cette activité est transcrit plus bas, aux sous-activités 3.1
« Lecture d'un dessin d'ensemble » (p.65–68) et 3.2 « Cotation fonctionnelle » (p.69–74) : la
présentation du support et son travail demandé sont donc décrits en deux endroits.)*

- **Système / support d'étude** : **pince de soudage par point** (soudage de tôles de châssis et
  carrosseries automobiles), actionnée par un **vérin pneumatique**.
- **Compétences affichées** : aucune pastille CD sur p.60, p.61, p.62, p.63 et p.64.
- **Mise en situation (p.60, verbatim)** :

  > **1. Mise en situation**
  > Le système étudié est une pince de soudage qui supporte les deux électrodes E1 et E2 et permet
  > leur déplacement fonctionnel. Ce procédé est plus particulièrement utilisé dans la réalisation
  > des châssis et carrosseries des voitures.

  Perspective couleur légendée : « **Tôles à souder** », « **Eléctrode E1** » [sic],
  « **Eléctrode E2** » [sic], « **Vérin** ».

- **Ressources numériques (p.60)** : trois QR codes étiquetés « **Animation pince** »,
  « **Animation vérin** », « **Réalité augmentée** ». Un quatrième QR code étiqueté **PDF** figure
  sur le dessin d'ensemble p.61 et un autre p.62.

- **Description de fonctionnement (p.60, verbatim)** :

  > **2. Description de fonctionnement de la pince de soudage par point**
  > Ce système permet le soudage des pièces en tôle à assembler sans métal d'apport. Les pièces
  > sont maintenues en contact sous un effort d'accostage exercé par les deux électrodes. Un
  > courant de basse tension et de forte intensité passe alors dans une zone très localisée.
  > Ce courant induit un chauffage par effet Joule provoquant la fusion des pièces dans la zone de
  > leur contact (noyau). Après coupure du courant, l'effort, toujours appliqué, forge la soudure.
  > Une succession de points de soudage permet de réaliser des liaisons complètes indémontables
  > entre deux tôles.

  Schéma de principe associé (p.60), annoté : « **Effort** » (**F**), « **Electrode** » (deux
  fois, haut et bas), « **Noyau** », « **Alimentation électrique** » (transformateur figuré par
  deux enroulements), et deux flèches **F** opposées.

- **Dessins d'ensembles (p.61)** — cartouche : **« Pince de soudage »**, **Echelle : 1:5**,
  symbole de disposition des vues. Dessin imprimé en rotation (à lire page tournée) ; il comporte :
  - la vue principale **A-A**, annotée « **Tôles à souder** », « **Electrode E1** »,
    « **Electrode E2** », repère du trièdre **x / y / z** (origine **O**) ; repères visibles :
    **17, 46, 5, 7, 40, 41, 42, 16, 6, 43, 45, 21, 1, 2** ; plans de coupe **B**, **C**, **D**,
    **E**, **F**, **G** repérés ;
  - une **coupe F-F** — repères **39**, **16** ;
  - une **coupe B-B** — repères **22, 30, 29, 11, 12, 14, 13, 44** ;
  - une **coupe C-C** — repères **5, 23, 24, 25, 31, 32** ;
  - une **coupe G-G (sans les pièces 20)** — repères **27, 28, 5, 3** ;
  - une **coupe E-E** — repères **7, 36, 15, 19, 9, 10** ;
  - une **coupe D-D (sans 1, 2, 9,19,21 et 70)** — repères **4, 26, 18, 3, 20, 37, 38** ;
  - une pièce plate repérée **33, 34, 35** (empilage d'isolants) et les repères **8**, **9** ;
  - deux vues de **Détail - Echelle 1:3**.

- **Dessin d'ensemble du vérin (p.62)** — cartouche : **« VERIN PNEUMATIQUE (Pince de soudage) »**,
  **Echelle : 7:12**. Dessin imprimé en rotation ; il comporte :
  - une **coupe B-B** (bloc arrière) — repères **70, 71, 72, 6, 21** ; plan de coupe **A** repéré ;
  - une **coupe A-A** (vérin complet en long) — repères portés en haut, de gauche à droite :
    **55, 58, 51, 53, 52, 49, 65, 63, 64, 68, 67, 61**, puis **59, 62, 60** et **6** ; repères
    portés en bas : **69, 2, 48, 56, 57, 66, 50, 47, 54, 1** ; deux repères de chambre
    **R1** et **R2** ; plan de coupe **B** repéré ;
  - une **vue extérieure** (non coupée) du vérin, en bas à droite ;
  - l'annotation fléchée « **Alimentation en air comprimé (sortie de tige)** » ;
  - un QR code étiqueté **PDF**.

- **Nomenclature (p.63–64)** — 72 repères. En haut de la p.63 le manuel imprime le titre
  « **4. Description de fonctionnement de la pince de soudage par point** » alors que la page ne
  contient que le tableau de nomenclature (voir § Incertitudes). Le tableau se poursuit p.64 sans
  titre, avec seulement sa ligne d'en-tête.

| Rep. | Nbr. | Désignation | Matière | Observation |
| --- | --- | --- | --- | --- |
| 1 | 1 | Tige avant | C18 | chromée |
| 2 | 1 | Tourillon avant du vérin | A-S5U3 | |
| 3 | 1 | Guide droit | 25CrMo4 | bruni et traité |
| 4 | 1 | Guide gauche | 25CrMo4 | bruni et traité |
| 5 | 1 | Bras | | |
| 6 | 1 | Bras | | |
| 7 | 1 | Biellette | 35CrMo4 | |
| 8 | 1 | Suspension | S235 | |
| 9 | 1 | Chape M20 L=60 | S235 | |
| 10 | 6 | Rondelle d'arrêt d'axe | S235 | |
| 11 | 4 | Rondelle isolante Ø20xØ75x2 | Nylatron | |
| 12 | 1 | Bague isolante Ø24xØ30x20 | Nylatron | |
| 13 | 1 | Bague isolante Ø24xØ30x12 | Nylatron | |
| 14 | 1 | Axe Ø20x80 | Acier STUB | |
| 15 | 1 | Axe Ø16x43 | Acier STUB | |
| 16 | 1 | Bride taraudée Ø20 | S235 | |
| 17 | 1 | Bride lamée Ø20 | S235 | |
| 18 | 1 | Entretoise | | |
| 19 | 1 | Tige filetée M20x150 | | NF E 22.163 |
| 20 | 2 | Tôle de protection | S235 | |
| 21 | 1 | Palier arrière | S235 | |
| 22 | 1 | Axe Ø20x50 | Acier STUB | |
| 23 | 4 | Coussinet | Cu Sn 8 Pb 2 | |
| 24 | 1 | Axe Ø16x59 | Acier STUB | |
| 25 | 6 | Vis CHC M5x6 | | NF E 25.125 |
| 26 | 2 | Vis CHC M5x16 | | NF E 25.125 |
| 27 | 1 | Écrou HM M4 | | NF E 25.405 |
| 28 | 1 | Vis HC M4x20 bout tronconique (TR) | | NF E 27.182 |
| 29 | 6 | Vis FHC M6x10 | | NF E 27.160 |
| 30 | 1 | Bague frittée 20x24x20 | FP15 | |
| 31 | 2 | Isolant | Nylatron | |
| 32 | 2 | Bague frittée 20x24x12 | FP15 | |
| 33 | 4 | Isolant | Nylatron | |
| 34 | 4 | Tube | Bakélite | |
| 35 | 1 | Isolant | Nylatron | |
| 36 | 1 | Bague frittée 16x22x20 | FP15 | |
| 37 | 4 | Goupille de positionnement 8x16 à trou fileté | | NF E 27.475 |
| 38 | 4 | Vis CHC M8x25 | | NF E 25.125 |
| 39 | 4 | Vis CHC M6x25 | | NF E 25.125 |
| 40 | 1 | Pastille de butée | Acier STUB | Montée serrée |
| 41 | 1 | Vis H M 10x60 | | NF E 25.112 |
| 42 | 2 | Écrou HM M10 | | NF E 25.405 |
| 43 | 1 | Vis HC M10x70 bout bombé (BB) | | NF E 27.180 |
| 44 | 1 | Bague frittée 20x24x20 | FP15 | |
| 45 | 1 | Pastille de butée | Acier STUB | Montée serrée |
| 46 | 1 | Joint torique 19,6x2,4 | | NF E 27.180 |
| 47 | 1 | Tube | S275 | |
| 48 | 1 | Fond | A-S5U3 | |
| 49 | 1 | Tige intermédiaire | C18 | chromé |
| 50 | 1 | Palier intermédiaire | A-S5U3 | |
| 51 | 2 | Piston | EN AW 2017 A | |
| 52 | 1 | Flasque | EN AW 2017 A | |
| 53 | 1 | Bague d'amortissement avant | | |
| 54 | 4 | Tirant M6 | | |
| 55 | 1 | Écrou de tige M 12 | | |
| 56 | 4 | Écrou H M6 | | NF E 25.401 |
| 57 | 4 | Rondelle L6 | | NF E 25.513 |
| 58 | 1 | Bague d'amortissement arrière | | |
| 59 | 1 | Bague de guidage avant | Cu Sn 8 Pb 2 | |
| 60 | 1 | Joint racleur | | |
| 61 | 1 | Joint de tige avant | | |
| 62 | 1 | Anneau élastique d'arrêt | | |
| 63 | 1 | Joint de tige arrière | | |
| 64 | 2 | Joint de piston | | |
| 65 | 1 | Bague de guidage intermédiaire | Cu Sn 8 Pb 2 | |
| 66 | 1 | Joint torique 20x3 | | |
| 67 | 4 | Joint torique 56x1 | | |
| 68 | 1 | Joint torique | | |
| 69 | 2 | Bague de guidage | Cu Sn 8 Pb 2 | |
| 70 | 1 | Palier avant | S235 | |
| 71 | 2 | Vis CHC M8x75 | | |
| 72 | 2 | Goupille de positionnement 8x90 | | |

- **Vocabulaire & terminologie officielle** : soudage par point, électrode, effort d'accostage,
  métal d'apport, effet Joule, noyau, forgeage de la soudure, liaison complète indémontable,
  vérin pneumatique, tige, piston, flasque, bague d'amortissement, bague de guidage, joint
  torique / racleur / de tige / de piston, tirant, tourillon, biellette, chape, coussinet, bague
  frittée, rondelle isolante, bague isolante, goupille de positionnement, bride taraudée / lamée,
  pastille de butée ; désignations normalisées **Vis CHC / FHC / HC / H**, **Écrou HM / H**,
  normes **NF E**.

##### Bornes de scope observées — p.41–64

- ✅ INCLUS : ouverture de la séquence « Définition des éléments d'un produit » (p.41, avec ses
  5 composantes de compétences CD 3.2 / 3.5 / 3.7 / 2.5 / 3.3 et sa grille de critères) ;
  **lecture / décodage d'un dessin d'ensemble** (repérage des pièces, fonctions des pièces,
  liaisons mécaniques et leurs symboles, désignation normalisée des composants, déchiffrage des
  désignations de matériaux, obstacle vs adhérence) ; **analyse fonctionnelle** (fonction globale,
  matière d'œuvre entrante/sortante, tableau fonction ↔ processeur, diagramme **FAST** avec FP /
  FT / sous-FT et colonne composants) ; **analyse du fonctionnement** (classes d'équivalence
  cinématique, schéma cinématique, solution constructive, rattrapage de jeu) ; **graphes de
  montage et de démontage** (filogramme avec repère d'ordre, tableau outillages/observations,
  graphe « râteau », sous-ensemble restant) en contexte de maintenance **corrective** (p.47) et
  **préventive** (p.55) ; **cotation fonctionnelle** (justification d'une condition, tracé de
  chaîne de cotes, équations J / J<sub>Maxi</sub> / J<sub>min</sub> / IT, calcul d'une cote
  tolérancée, report de la cote fonctionnelle sur un dessin de définition, notion de plan de
  jauge, condition mini/maxi) ; **dessin de définition** (vue de face/droite/gauche/dessus, coupe,
  demi-coupe, coupe particulière pour formes en plans parallèles ou sécants, spécifications
  géométriques, états de surface / rugosité) ; **modélisation 2D et 3D** sur logiciel ;
  **manipulation réelle** sur perceuse sensitive et poupée mobile avec consignes de sécurité.
- ⛔ EXCLU / seulement mentionné dans cette tranche :
  - Les **sections** annoncées dans la colonne « Savoirs et savoir-faire » p.41 ne sont travaillées
    dans aucune des activités 1.x / 2.x de la tranche (seules les coupes le sont) — elles doivent
    l'être plus loin dans le thème (p.65–86, voir plus bas).
  - La **désignation des matériaux (Rappel)** annoncée p.41 n'est jamais exposée comme cours : elle
    n'apparaît que par des questions de déchiffrage (p.46 q.7, p.54 q.3).
  - La **CD 2.5** (modélisation 3D/2D) est annoncée p.41 mais n'apparaît **jamais en pastille de
    page** dans la tranche, alors que trois questions demandent explicitement de modéliser
    (p.50 q.3, p.58 A.3, p.59 q.6).
  - Le **logiciel de modélisation n'est jamais nommé** : le manuel écrit seulement « des logiciels
    appropriés ».
  - Le **calcul du vérin pneumatique** (efforts, pressions, débits) n'est pas abordé : le vérin
    n'est présent que comme dessin d'ensemble (p.62) et nomenclature.
  - **Aucun encadré de cours, de synthèse ou de « Je retiens »** dans toute la tranche : les seuls
    encadrés sont les « Situation déclenchante » / « Situation problème » de chaque sous-activité.
    Le manuel est un **manuel d'activités**, il pose des questions et ne donne aucun corrigé —
    toutes les réponses sont laissées en pointillés.
  - L'**activité 3 (Pince de soudage)** se poursuit au-delà de sa présentation : ses
    sous-activités **3.1** (p.65–68) et **3.2** (p.69–74) sont transcrites plus bas dans
    cette même section. Les p.60–64 ne portent, elles, que le dossier technique (mise en
    situation, dessins d'ensemble, nomenclature) — aucune question n'y est imprimée.

##### Activité 3 (suite) — Pince de soudage (p.65–74)

> Cette tranche reprend l'Activité 3 en cours de route : elle ouvre à la page 65, sur la
> sous-activité « Activité 3.1 ». La présentation du support (mise en situation, dessin
> d'ensemble, nomenclature de la pince de soudage) est imprimée p.60–64 et transcrite ci-dessus.
> Bandeau de page commun à toute la tranche : **« DÉFINITION DES ELEMENTS D'UN PRODUIT »**
> (« ELEMENTS » sans accent, tel qu'imprimé) — c'est le titre courant du thème
> « Communication technique ».

---

###### Activité 3.1 (p.65–68)

- **Système / support d'étude** : pince de soudage (par points) à commande pneumatique — pièces
  citées : tourillon (2), guides (3) et (4), bras mâle (5), bras (6), biellette (7) — aussi
  appelée « levier (7) » p.67, chape (9), palier arrière (21), palier avant (70), bagues de
  guidage (69) et (69'), vis (71), goupilles (72), tige avant du vérin (1), vis (41) et (43),
  écrou (42), pastilles (40) et (45), électrodes E1 et E2.
- **Compétences affichées** : `CD 3.2` (bandeau de p.65 à p.68).
- **Pictogrammes de compétence transversale** (têtes de couleur, en tête d'activité p.65) :
  `R.PRO` (vert) et `CRITI` (bleu).
- **Titre imprimé** : la page ne porte que « **Activité 3.1** » — aucun sous-titre imprimé
  (le sommaire p.4 l'appelle « 3.1 Lecture d'un dessin d'ensemble »).

**I. Situation problème** (encadré bleu, p.65) :

> Une défectuosité de fonctionnement de la pince de soudage déclenche une intervention de
> changement des deux bagues de guidage (69) du tourillon (2) avec le bras (6). Avant de passer
> à l'action de démontage et de montage nous devons poser la question suivante :
> **Comment décoder le dessin d'ensemble de la pince de soudage ?**

- **Ressources fournies** : dossier technique de la pince de soudage ; dessins d'ensemble de la
  pince et du vérin pneumatique + nomenclature (imprimés hors tranche, p.60–64) ; schéma
  cinématique à compléter (p.66) ; séquences de montage/démontage des bagues (renvoi p.68) ;
  **QR-code « Vid »** (vidéo) en bas de p.68.
- **Données numériques de l'énoncé** : aucune valeur chiffrée dans cette sous-activité (les
  seuls nombres sont des repères de nomenclature).

**II. Travail demandé**

**A. Analyse fonctionnelle** (p.65–66) — « En se référant au dossier technique de la pince de soudage. »

1. « Rechercher les matières d'œuvre d'entrée et de sortie et la fonction globale de la pince. »
   Trois lignes à compléter : « Matière d'œuvre d'entrée : … », « Matière d'œuvre de sortie : … »,
   « Fonction globale : … ».
2. « L'alimentation du vérin pneumatique permet la fermeture de la pince et le soudage des tôles,
   compléter le diagramme FAST descriptif relatif à la fonction principale «Permettre à
   l'utilisateur de souder les tôles». »
   Diagramme FAST imprimé (colonne de droite intitulée « **Fonction associée ou solutions
   constructives** », 6 cases vides) :
   - **FP** : « Permettre à l'utilisateur de souder les tôles »
   - **FT1** : « Convertir l'énergie pneumatique en énergie mécanique » → **1** case vide
   - **FT2** : « Assurer le contact de l'électrode E1 liée au bras (6) avec les éléments à souder »
     → **2** cases vides
   - **FT3** : « Positionner l'électrode E2 face à l'électrode E1 en contact avec les éléments à
     souder » → **2** cases vides
   - **FT4** : « Créer l'effort d'accostage et convertir l'énergie électrique en chauffage par
     effet joule » → **1** case vide
3. « Citer les fonctions des pièces suivantes : » — « Les vis (41) et (43) : … » ; « L'écrou (42) : … » ;
   « Les pastilles (40) et (45) : … »
4. « Que se passe-t-il à l'arrêt d'alimentation du vérin ? » (2 lignes)
5. « Expliquer comment agit l'opérateur pour régler l'angle d'écartement entre les deux électrodes
   E1 et E2 de la pince de soudage ? » (3 lignes)

**B. Analyse du fonctionnement** (p.66) — « En se référant aux dessins d'ensembles et à la nomenclature. »

1. « Compléter le schéma cinématique de la pince de soudage en plaçant les repères des pièces
   principales. »
   *Schéma cinématique imprimé (p.66)* : mécanisme plan tracé en couleurs dans le repère
   `(O ; x, y, z)` (z sortant, symbole ⊙). Liaisons pivot figurées par des cercles aux points
   **A, B, C, D, E** ; deux points repérés **F** et **G** sur les extrémités actives ; une liaison
   glissière figurée par un rectangle (pivot glissant) entre B et A. Le point **C** et le point
   **D** portent le symbole de bâti (hachures) ; le bloc « **Bâti** » est hachuré en bas à droite.
   Annotations imprimées : « Tôles à souder (fixes par rapport au bâti) », « Electrode E1 »,
   « Electrode E2 », « **S1** », « **S2** », « **S3** ». Quatre lignes de rappel pointillées
   (leaders vides) attendent les repères des pièces à placer par l'élève.
2. « Chercher les classes d'équivalences des pièces cinématiquement liées suivantes : »
   Tableau à trois lignes à compléter :
   | Classe | Amorce imprimée |
   | --- | --- |
   | S1 | `1 ; …` (3 lignes vides) |
   | S2 | `2 ; …` (3 lignes vides) |
   | S3 | `3 ; …` (3 lignes vides) |
3. « Colorier sur toutes les vues du dessin d'ensemble du vérin pneumatique les sous-ensembles
   S1 et S2 avec deux couleurs différentes. »

**C. Analyse des solutions constructives** (p.67)

1. « Décrire la solution constructive réalisant la liaison encastrement entre le bras (6) et les
   pièces rapportées (palier arrière (21) et palier avant (70)). » (2 lignes)
2. « Donner les repères et les désignations des pièces assurant la liaison pivot entre le corps du
   vérin (2) et le bras (6). » (2 lignes)
3. « Justifier le choix du matériau de ces pièces. » (2 lignes)
4. « Compléter le tableau ci-dessous en indiquant les composants associés aux diverses fonctions. »

   | Fonction | Composants |
   | --- | --- |
   | Lier la tige avant du vérin (1) à la chape (9). | (à compléter) |
   | Guider la biellette (7) en rotation par rapport à la chape (9). | (à compléter, 2 lignes) |
   | Guider le bras (6) en rotation. | (à compléter) |
   | Réaliser la liaison pivot entre le levier (7) et le bras mâle (5). | (à compléter) |
   | Lier l'électrode E1 au bras (6). | (à compléter) |
   | Lier l'électrode E2 au bras (5). | (à compléter) |
   | Lier les deux guides (3) et (4). | (à compléter) |

5. « Compléter le tableau ci- dessous en indiquant à chaque composant la désignation normalisée du
   matériau correspondant et sa signification. »

   | Nom et repère du composant | Désignation normalisée | Signification de la désignation normalisée du matériau |
   | --- | --- | --- |
   | Tige avant (1) | … | … |
   | Biellette (7) | … | … |
   | Bague de guidage (69) | … | … |

**D. Graphe de montage et démontage** (p.68) — « Consulter les sequences [sic] de montage et de
démontage des bagues. »

1. « Compléter le graphe de démontage "filogramme" partiel ci-dessous relatif à la pince de
   soudage, permettant l'intervention pour remplacer les bagues de guidage défectueuses (69) et
   (69'). »
   *Filogramme imprimé* : tête « **Pince de soudage** », colonne verticale « **Repère d'ordre** »,
   pied « **Sous- ensemble restant** ». Branches :
   - `1` → boîte **71**
   - `2` → boîte **72**, d'où part une sous-branche :
     - `2.1` → boîte **vide** (à compléter)
     - `2.2` → boîte **69**
     - `2.3` → boîte **vide** (à compléter)
     - `2.4` → boîte **69'**
     - fin de sous-branche : boîtes **21** et **70** côte à côte
   *Tableau « Outillages / Observations » associé (6 lignes, entièrement imprimé)* :

   | Outillages | Observations |
   | --- | --- |
   | Clé à six pans | Déposer les deux vis (71) |
   | Chasse goupille | Déposer les deux goupilles (72) |
   | Manuelle | Déposer le palier (70) avec la bague (69) |
   | Extracteur de coussinet | Déposer la bague de guidage (69) à changer |
   | Manuelle | Déposer le palier (21) avec la bague (69') |
   | Extracteur de coussinet | Déposer la bague de guidage (69') à changer |

2. « Compléter le graphe de montage "râteau" ci-dessous relatif à la pince de soudage pour le
   changement des bagues (69) et (69'). »
   *Râteau imprimé sur papier quadrillé* : colonne de boîtes, de haut en bas — **71**, **72**,
   **21**, **69'**, **70**, **69** ; puis boîte « **Sous- ensemble restant "Vérin"** » → flèche →
   « **Ensemble pince de soudage** ». Tout le reste du quadrillage est vierge (le graphe est à
   achever par l'élève).
   En bas de page : **QR-code encadré, étiquette jaune « Vid »**.

- **Vocabulaire & terminologie officielle (p.65–68)** : matière d'œuvre d'entrée / de sortie,
  fonction globale, diagramme FAST descriptif, fonction principale (FP), fonction technique (FT),
  fonction associée, solution constructive, schéma cinématique, classe d'équivalence, pièces
  cinématiquement liées, sous-ensemble, liaison encastrement, liaison pivot, désignation normalisée
  du matériau, graphe de démontage « filogramme », graphe de montage « râteau », repère d'ordre,
  sous-ensemble restant, outillages, chasse goupille, extracteur de coussinet, clé à six pans,
  bague de guidage, palier avant / palier arrière, tourillon, biellette, chape, effet joule,
  effort d'accostage.

---

###### Activité 3.2 (p.69–74)

- **Système / support d'étude** : la même pince de soudage — sous-ensembles étudiés : liaison
  bras (6) / tourillon (2) par bagues (69) et paliers (21) et (70) ; guidage du bras mâle (5) dans
  l'ensemble solidaire (3 ; 4) par coussinets (23).
- **Compétences affichées** : `CD 3.5` et `CD 3.7` (bandeau de p.69 à p.74).
- **Pictogrammes** (p.69) : `R.PRO`, `CRITI`, `CREA`.
- **Titre imprimé** : « **Activité 3.2** » seul (le sommaire p.4 l'appelle « 3.2 Cotation
  fonctionnelle »).

**I. Situation problème** (encadré bleu, p.69) :

> Le montage et le bon fonctionnement de la pince de soudage exigent un ensemble de conditions et
> un dimensionnement précis des différentes pièces qui le constituent.
> **Comment doit-on procéder ?**

- **Ressources fournies** : dessin d'ensemble du vérin pneumatique ; dessin d'ensemble de la pince
  de soudage ; dessins partiels en coupe (p.69 et p.70) ; dessins 3D des pièces (tourillon (2)
  p.71, palier avant (70) p.72, biellette (7) p.73, palier arrière (21) p.74) ; vues incomplètes à
  compléter ; dessin de définition amorcé de la bague (69) (p.69).

**II. Travail demandé**

**A. « Comment déterminer une condition fonctionnelle et chercher une cote fonctionnelle ? »** (p.69)

Énoncé imprimé : « Pour réduire le temps d'interchangeabilité des deux bagues (69) de guidage du
tourillon (2) avec le bras (6), on est amené à chercher les cotes fonctionnelles intervenantes
sachant que 0≤Ja≤0,2. »

- **Données numériques (p.69)** :
  - `0 ≤ Ja ≤ 0,2`
  - `a₂ = 54±0.02`
  - `a₆ = 27±0.02`
  - `a₂₁ = a₇₀ = 15±0.02`
  - Dessin de définition de la bague (69) : longueur totale **`16,5±0,2`**
  *(le manuel mélange les séparateurs décimaux : « 0,2 » à la virgule et « 0.02 » au point)*

1. « Traçage d'une chaîne de cotes — Sur le dessin ci-dessous, tracer la chaîne de cotes relative
   à la condition Ja. »
   *Dessin partiel imprimé (haut-droite p.69)* : coupe de l'assemblage bras (6) / tourillon (2),
   repères pointés **71** (vis à six pans creux), **72** (goupille), **70** (palier avant), **69**
   (bague), à gauche ; **6** (bras), **21** (palier arrière), **2** (tourillon), à droite. Deux
   cotes de diamètre `Ø …` vides sur la bague. La condition **Ja** est portée en bas à droite du
   dessin (point + flèche).
2. « Calcul de la cote fonctionnelle a₆₉ — Sachant que a₂ = 54±0.02 ; a₆ = 27±0.02 ; a₂₁ = a₇₀ = 15±0.02 »
   - a. « Déterminer les équations de : » `J_aMaxi = …` ; `J_amini = …` ; `a₆₉Maxi = …` ; `a₆₉mini = …`
   - b. « Calculer a₆₉ » (7 lignes)
   - c. « Inscrire dans les cadres prévues les spécifications géométriques. »
   - d. « Inscrire les ajustements. »
   - e. « Reporter les cotes fonctionnelles sur le dessin de définition de la bague (69). »
   *Dessin de définition amorcé de la bague (69) (bas-droite p.69)* : bague à collerette en coupe,
   deux cadres de tolérance géométrique vides référencés au **datum A** (`|__|…….| A |`, deux
   occurrences), le repère de référence **A** posé sur le cylindre extérieur, deux cotes `Ø …`
   vides et la cote de longueur **16,5±0,2**.
3. « Mise en place d'une cote condition : Représenter et tracer sur le dessin partiel la condition
   **Jb** permettant la détermination de la longueur de la vis (71). »

**B. « Comment vérifier une condition fonctionnelle ? »** (p.70)

Énoncé imprimé : « Le sous ensemble (5 ; B1 ; B1' ; 24 ; 27 ; 28) est en liaison pivot avec les
coussinets (23), qui sont logés dans une rainure de l'ensemble solidaire (3 ; 4) de manière à
provoquer le coulissement du bras. »

1. « Justifier la présence de la cote condition Jc » (5 lignes)
2. « La condition Jc est-elle maximale ou minimale? Justifier : … » (6 lignes)
3. « Tracer la chaîne de cote relative à la condition Jc... »
4. « La condition Jc est-elle maximale ou minimale ? Justifier : … » (6 lignes)
5. « Tracer la chaîne de cotes relative à la condition Jc... »
6. « Conclure: » (5 lignes)

*Deux dessins partiels en coupe, l'un pour les questions 1–3, l'autre pour les questions 4–6*, qui
représentent le même sous-ensemble **dans deux positions extrêmes du coulissement** (le jeu `j`
noté en haut change de côté d'un dessin à l'autre) ; la cote condition **`Jc...`** est amorcée en
bas de chacun. Repères pointés, dessin 1 : à gauche **5, 4, B1', 23', 20, 18, 26** ; à droite
**3, B1, 23, 24, 25**. Dessin 2 : à gauche **4, B1', 23', 20, 18, 26** ; à droite **5, 3, B1, 23,
24, 25**.

**C. Représentation d'un produit fini** (p.71–74)

**1. Dessin de définition du tourillon (2)** (p.71) — *Échelle imprimée : `Echelle:2:3`*
- Données : « Le dessin d'ensemble du vérin pneumatique. » ; « Le dessin en 3D du tourillon (2). » ;
  « La vue de face, la vue de gauche et la vue de dessus incomplètes. »
- Travail demandé :
  a. « Compléter la vue de face en coupe A-A. »
  b. « La vue de gauche. »
  c. « La vue de dessus. »
  d. « Inscrire les spécifications géométriques et l'état de surface demandé. »
  e. « Reporter la cote fonctionnelle issue de la chaine de cotes. »
- Figure : photo 3D du tourillon (corps prismatique percé, avec téton cylindrique latéral et
  trous taraudés) ; vue en coupe **A-A** partielle ; vue avec traces du plan de coupe **A-A** ;
  troisième vue partielle. Deux cotes `Ø …` vides, un symbole d'état de surface vide, trois cadres
  de tolérance géométrique vides référencés **A**, et le repère de référence **A**.

**2. Dessin de définition du palier avant (70)** (p.72) — *Échelle imprimée : `Echelle:1:2`*
- Données : « Le dessin d'ensemble du vérin pneumatique. » ; « Le dessin en 3D du palier avant (70). » ;
  « La vue de face et la vue de droite incomplètes. »
- Travail demandé :
  a. « Compléter la vue de face. »
  b. « Compléter la vue de droite en coupe B-B »
  c. « Représenter la section sortie C-C. »
  d. « Inscrire les spécifications géométriques et les états de surface demandés. »
  e. « Reporter la cote fonctionnelle issue de la chaine de cotes. »
- Figure : photo 3D du palier (plaque à quatre trous et un grand alésage) ; vue **B-B** partielle ;
  vue de face avec traces des plans de coupe **B-B** et **C-C** ; libellé **C-C** posé sans dessin
  (la section sortie est à produire par l'élève). Quatre cadres de tolérance géométrique vides
  (dont trois référencés **A**), repère de référence **A**, un symbole d'état de surface vide.

**3. Dessin de définition de la biellette (7)** (p.73) — *Échelle imprimée : `Echelle:1:3`*
- Données : « Le dessin d'ensemble de la pince de soudage. » ; « Le dessin en 3D de la biellette (7). » ;
  « La vue de face, la vue de gauche et la vue de droite incomplètes. »
- Travail demandé :
  a. « Compléter la vue de droite en coupe D-D sans details [sic] cachés. »
  b. « La section sortie E-E. »
  c. « La vue de gauche. »
- Figure : photo 3D de la biellette (bras coudé chapé à une extrémité, deux alésages à l'autre) ;
  vue **D-D** partielle à gauche ; vue de face complète avec traces des plans de coupe **D-D** et
  **E-E** ; troisième vue partielle à droite ; libellé **E-E** posé sans dessin.

**4. Modélisation numérique (3D et 2D)** (p.74) — *Échelle imprimée : `Echelle: 5:6`*
- Données : « Le dessin d'ensemble du vérin pneumatique. » ; « Le dessin en 3D du palier arrière (21). » ;
  « La vue de face et la vue de droite en coupe A-A. »
- Travail demandé : « Modéliser le palier arrière (21) en utilisant des logiciels appropriés. »
- **Dessin de définition COMPLET du palier arrière (21), coté** (seule pièce entièrement cotée de
  la tranche) — valeurs imprimées :
  - *Vue en coupe A-A* : `32±0,05` (largeur) ; `86±0,2` (hauteur totale partielle) ;
    `23±0,02` ; `10±0,04` ; `35±0,02` ; `15±0,02` ; chanfrein `1,5x45°` ; taraudage **`M8`** ;
    état de surface **`Ra1,6`** ; référence **A** ; tolérance de perpendicularité **`⊥ 0,1 A`**.
  - *Vue de face* : `34±0,05` ; `14±0,02` ; `10±0,02` ; `105±0,2` ; `45±0,2` ; chanfreins `5x45°` ;
    alésages **`Ø8 H7`** et **`Ø28 H7`** ; traces du plan de coupe **A-A**.
  - Photo 3D du palier arrière (plaque à quatre trous, puis embase percée d'un grand alésage).

- **Vocabulaire & terminologie officielle (p.69–74)** : condition fonctionnelle, cote condition,
  cote fonctionnelle, chaîne de cotes, interchangeabilité, jeu, ajustement, spécification
  géométrique, état de surface (Ra), dessin de définition, vue de face / de gauche / de droite /
  de dessus, coupe A-A, section sortie, produit fini, modélisation numérique (3D et 2D),
  coussinet, rainure, coulissement, ensemble solidaire, classe d'équivalence.

---

##### Activité 4 — Machine d'essai de traction (p.75–84)

###### Présentation du support d'activité (p.75–77)

- **Système / support d'étude** : **machine d'essai de traction** (essais de résistance des
  matériaux sur éprouvettes cylindriques).
- **Compétences affichées** : **aucune** — le médaillon bleu du bandeau est vide sur p.75, p.76 et
  p.77 (les CD reprennent p.78).
- **Bandeau titre** (p.75) : onglet « **Activité 4** » + cartouche « **Machine d'essai de traction** ».

**1. Mise en situation** (p.75) — texte imprimé :

> La machine d'essai de traction est prévue pour la réalisation des essais de résistance de
> matériaux sur des éprouvettes cylindriques. La force de traction est obtenue à l'aide d'un
> cylindre de commande à vis (pompe) qui transmet la force à un vérin hydraulique (vérin
> vertical).
> La force exercée sur l'éprouvette est mesurée par un manomètre gradué en KN.
> Les déformations des éprouvettes sont mesurées à l'aide d'un comparateur à cadran gradué en
> centième de mm (Un tour complet de l'aiguille correspond à un déplacement vertical de 1 mm).

- **Données numériques (p.75)** : manomètre gradué en **KN** [sic, majuscules] ; comparateur à
  cadran gradué au **centième de mm** ; **1 tour d'aiguille = 1 mm** de déplacement vertical.
- **Photo annotée de la machine** (p.75), légendes imprimées : « Traverse mobile supérieure »,
  « Comparateur à cadran », « Traverse fixe supérieure », « Noix », « Pompe hydraulique »,
  « Manivelle », « Manette » (colonne de gauche) ; « Indicateur de charge », « Traverse mobile
  inférieure », « Vérin vertical », « Traverse fixe inférieure » (colonne de droite).
  *(« Noix » ne figure pas à la nomenclature p.77.)*

**2. Dessin d'ensemble** (p.76)

- Dessin d'ensemble unique, en coupe partielle, du bâti complet de la machine : de bas en haut,
  plaque d'appui / support (19, 20) et traverse fixe inférieure (1), pompe hydraulique (4) avec
  manivelle (3) et manette, vérin vertical (2), traverse mobile inférieure (7), colonnes fixes (5)
  et mobiles (17), traverse fixe supérieure (8) portant le mors fixe (9), traverse mobile
  supérieure (14) portant la butée (10), mors mobile (16) et arbres (15), écrous (6, 12) et
  rondelles (13), coussinets (18), vis de fixation (21) et vis (11).
- **Repères pointés sur le dessin** : 1 à 21 (les 21 repères de la nomenclature).
- **Vues et annotations** : « **Vue suivant F de (14)** » (petite vue à trois trous, en haut) ;
  flèche de sens d'observation « **F** » ; légendes « **Comparateur à cadran** » et
  « **Indicateur de charge** » (les deux appareils sont dessinés, non repérés).
- **Cartouche imprimé** : symbole de projection (méthode européenne : cône tronqué + cercles
  concentriques) | « **Echelle 3:10** » | « **Machine d'essai de traction** ».

**3. Nomenclature** (p.77) — transcrite intégralement telle qu'imprimée :

| Rep. | Nbr. | Désignation | Matière | Observation |
| --- | --- | --- | --- | --- |
| 1 | 1 | Traverse fixe inférieure | S 185 | |
| 2 | 1 | Vérin hydraulique | | |
| 3 | 1 | Manivelle | Al Cu 4 Mg | |
| 4 | 1 | Pompe hydraulique | | |
| 5 | 2 | Colonne fixe | 35 Cr Mo 4 | Chromée |
| 6 | 2 | Ecrou hexagonal, M18 | | |
| 7 | 1 | Traverse mobile inférieure | S185 | |
| 8 | 1 | Traverse fixe supérieure | S185 | |
| 9 | 1 | Mors fixe | 35 Cr Mo 4 | Chromée |
| 10 | 1 | Butée | C 30 | |
| 11 | 2 | Vis à tête cylindrique à six pans creux M4-6 | | |
| 12 | 9 | Ecrou hexagonal, M16 | | |
| 13 | 9 | Rondelle plate M16 | S 185 | |
| 14 | 1 | Traverse mobile supérieure | S 185 | |
| 15 | 2 | Arbre | C 30 | |
| 16 | 1 | Mors mobile | 35 Cr Mo 4 | Chromée |
| 17 | 2 | Colonne mobile | 35 Cr Mo 4 | Chromée |
| 18 | 2 | Coussinet | Cu sn 8 | |
| 19 | 1 | Plaque d'appui | S 185 | |
| 20 | 1 | Support | S 185 | |
| 21 | 1 | Vis de fixation | | |

*(Orthographe de la source conservée : « Ecrou » sans accent ; « S 185 » aux repères 1, 13, 14, 19,
20 mais « S185 » aux repères 7 et 8 ; « Cu sn 8 » avec un s minuscule.)*

---

###### Activité 4.1 (p.78–81)

- **Compétences affichées** : `CD 3.2` (bandeau de p.78 à p.81).
- **Pictogrammes** (p.78) : `COOP` (jaune) et `CRITI` (bleu).
- **Titre imprimé** : « **Activité 4.1** » seul (sommaire p.4 : « 4.1 Lecture d'un dessin d'ensemble »).

**I. Situation déclenchante** (encadré bleu, p.78) :

> Une défectuosité de fonctionnement de la machine d'essai de traction déclenche une intervention
> de changement des deux bagues de guidage de la traverse mobile.
> **Avant de passer à l'action de démontage et de remontage nous devons décoder le dessin
> d'ensemble de la machine d'essai de traction.**

- **Ressources fournies** : la machine d'essai de traction et son dossier technique ; le dessin
  d'ensemble p.76 et sa nomenclature p.77 ; un dessin partiel en coupe du guidage colonne mobile /
  coussinet (p.79) ; un pied à coulisse au 1/50 (mesure réelle demandée).
- **Données numériques de l'énoncé (p.79)** : pied à coulisse **au 1/50** ; diamètre nominal
  **extérieur** du coussinet **`D = 24mm`** ; `dmesuré = ……… mm` (à relever par l'élève).

**II. Travail demandé**

**A. Analyse fonctionnelle** (p.78–79) — « En se référant à la machine d'essai de traction et à son
dossier technique. »

1. « Rechercher les matières d'œuvres d'entrée et de sortie et la fonction globale du système. »
   Trois lignes : « Matière d'œuvre d'entrée : … », « Matière d'œuvre de sortie : … »,
   « Fonction globale : … ».
2. « Compléter le diagramme FAST descriptif relatif à la fonction principale. »
   *FAST imprimé (colonne de droite : « **Processeur ou solutions constructives** », 5 cases vides
   de 2 lignes chacune)* :
   - **FP** : « Réaliser l'essai de traction sur une éprouvette »
   - « Alimenter en énergie hydraulique » → 1 case vide
   - « Convertir l'énergie hydraulique en énergie mécanique » → 1 case vide
   - « Maintenir et créer l'effort de traction sur l'éprouvette » → 1 case vide
   - « Indiquer la valeur de l'effort de traction » → 1 case vide
   - « Indiquer la valeur de déformation » → 1 case vide
   *(les fonctions techniques ne sont pas numérotées FT1…FT5 ici, contrairement à p.65)*
3. « Justifier la présence des stries (moletage) sur le mors mobile (16). » (1 ligne)
4. « Expliquer comment agit l'opérateur pour fixer l'éprouvette sur la machine. » (3 lignes)

**B. Analyse de fonctionnement** (p.79) — « En se référant au dessin d'ensemble et à sa nomenclature. »

1. « Compléter les classes d'équivalences des pièces cinématiquement liées suivantes : »
   - `S1 = {14 ; ……………}`
   - `S2 = {8 ; ……………}`
2. « Colorier sur le dessin d'ensemble S1 et S2 avec deux couleurs différentes. »
3. « Déduire la liaison de S1 avec S2: … »
4. « Mettre une croix devant la solution adaptée par le constructeur. »
   *Arbre imprimé* : « Guider en translation S1 par rapport au bâti S2 » → « **Liaison glissière** »
   → quatre solutions, chacune suivie d'une case à cocher vide, dans cet ordre imprimé :
   1. « Arbre cannelé »
   2. « Clavette + forme cylindrique »
   3. « Par colonnes »
   4. « Vis à téton + forme cylindrique »

**C. Analyse des solutions constructives** (p.79–80)

1. « Justifier la présence des pièces (18) » (1 ligne)
2. « Justifier le choix du matériau pour ces pièces. » (2 lignes)
3. « Mesurer à l'aide d'un pied à coulisse au 1/50 le diamètre de la colonne (17) :
   dmesuré = ……… mm »
4. « Placer sur le dessin ci-contre l'ajustement relatif au montage des coussinets sachant que le
   diamètre nominal extérieur du coussinet est D = 24mm. »
   *Dessin partiel imprimé (droite p.79)* : coupe du guidage — colonne mobile **17** au centre,
   coussinet **18** en manchon, logé dans la traverse **8** ; deux lignes de cote vides en bas
   (l'une pour l'alésage du coussinet, l'autre pour l'alésage de logement).
5. « Compléter le tableau ci-dessous en indiquant les composants assurant chaque fonction. » (p.80)

   | Fonction | Composants / Solutions |
   | --- | --- |
   | Lier la traverse mobile supérieure (14) à la colonne mobile (17) | (à compléter) |
   | Guider la traverse mobile supérieure (14) en translation par rapport au bâti | (à compléter) |
   | Guider le mors mobile (16) en rotation | (à compléter) |
   | Lier le mors mobile (16) à l'arbre (15) | (à compléter) |
   | Lier le mors fixe (9) à la traverse fixe supérieure (8) | (à compléter) |
   | Lier la butée (10) à la traverse mobile supérieure (14) | (à compléter) |
   | Lier les colonnes fixes à la traverse fixe inférieure (1) et les supports (19) et (20) | (à compléter) |

6. « Compléter le tableau ci-dessous, par la désignation normalisée du matériau de chaque composant
   et sa signification. » (p.80)

   | Nom et repère du composant | Désignation normalisée | Signification de la désignation normalisée du matériau |
   | --- | --- | --- |
   | Manivelle (3) | … | … |
   | Colonne fixe (5) | … | … |
   | Traverse mobile supérieure (14) | … | … |
   | Butée (10) | … | … |
   | coussinet (18) | … | … |

**D. Graphe de montage et démontage** (p.80–81)

1. « Compléter le graphe de démontage partiel ci-après relatif à la machine de traction, permettant
   l'intervention pour remplacer les bagues de guidage défectueuses (18). »
   *Filogramme imprimé (p.81)* : tête « **Machine de traction** », colonne « **Repère d'ordre** »,
   pied « **Sous- ensemble restant** ». Branches et tableau associé :

   | Repère d'ordre | Machine de traction | Outillages | Observations |
   | --- | --- | --- | --- |
   | 1 | 12 | Clé plate 24 | Déposer les 4 écrous (12) de maintien de (8) et (14) |
   | 2 | 13 | ………… (à compléter) | Déposer les 4 rondelles (13) de maintien de (8) et (14) |
   | 3 | 14; ………… (à compléter) | ………… (à compléter) | Déposer le sous-ensemble traverse mobile supérieure |
   | 4 | 21 | Clé à six pans | ………… (à compléter) |
   | 5 | 8; ………… (à compléter) | Manuelle | ………… (à compléter) |
   | 5.1 | 18, ……. (à compléter) | Extracteur de coussinet | Déposer les 2 bagues (18) et (18') à changer |

   Fin de branche : boîte « **8; 9** », puis « Sous- ensemble restant ».
2. « Compléter le graphe de montage ci-dessous de la machine d'essai de traction après le
   changement des bagues (18). »
   *Râteau imprimé sur papier quadrillé*, colonne de boîtes de haut en bas : **12** ; **13** ;
   **10; …………** ; **21** ; **……** (boîte vide) ; **69** ; **8; 9** ; puis
   « **Sous- ensemble "Coulisseau"** » → flèche → « **Ensemble** » (une photo de la machine
   accompagne le mot « Ensemble »).
   ⚠ Le repère **69** n'existe pas dans la nomenclature de la machine (1→21) : c'est un repère de la
   pince de soudage — report manifeste du graphe de la p.68.

- **Vocabulaire & terminologie officielle (p.78–81)** : situation déclenchante, matière d'œuvre,
  fonction globale, diagramme FAST descriptif, processeur, solution constructive, stries /
  moletage, classe d'équivalence, liaison glissière, arbre cannelé, clavette, vis à téton, guidage
  par colonnes, coussinet / bague de guidage, ajustement, diamètre nominal, pied à coulisse au
  1/50, graphe de démontage, graphe de montage, sous-ensemble « Coulisseau », clé plate,
  extracteur de coussinet, éprouvette, bâti.

---

###### Activité 4.2 (p.82–84)

- **Compétences affichées** : `CD 3.5` et `CD 3.7` (bandeau de p.82 à p.84).
- **Pictogrammes** (p.82) : `COOP` (jaune) et `CREA` (bordeaux).
- **Titre imprimé** : « **Activité 4.2** » seul (sommaire p.4 : « 4.2 Cotation fonctionnelle »).

**I. Situation déclenchante** (encadré bleu, p.82) :

> Le montage et le bon fonctionnement de la machine de traction exigent un ensemble de conditions
> et un dimensionnement précis des différentes pièces qui le constituent.
> **Comment doit-on procéder pour vérifier ces conditions?**

- **Ressources fournies** : dessin d'ensemble de la machine et sa nomenclature ; dessin partiel en
  coupe portant les conditions Ja et Jb (p.82) ; dessins 3D de la traverse mobile supérieure (14)
  (p.83) et du mors mobile (16) en coupe (p.84) ; vues incomplètes à compléter.
- **Données numériques de l'énoncé (p.82)** :
  - `4 ≤ Jb ≤ 6`
  - `b₁₅ = 18±0,5`
  - Ajustement porté sur le dessin : **`Ø18H7/g6`**

**II. Travail demandé**

**A. Traçage des chaînes de cotes** (p.82)

1. « Justifier la présence des conditions fonctionnelles: » — `Ja : …` (2 lignes) ; `Jb : …` (2 lignes)
2. « Sur le dessin ci-contre, tracer les chaînes de cotes relatives à Ja et Jb »
3. « Déterminer les équations de : » `Ja = …` ; `Jamaxi = …` ; `Jamini = …` (2 lignes chacune)

*Dessin partiel imprimé (droite p.82)* : coupe verticale du haut de la machine — arbre **15** serré
par deux écrous superposés, écrou **12** et rondelle **13** sur la colonne mobile **17**, traverse
**14** en coupe, mors mobile **16** conique et moleté en bas. L'ajustement **`Ø18H7/g6`** est porté
sur la colonne (17) ; la condition **Ja** est amorcée en haut à droite, la condition **Jb** en bas
à gauche.

**B. Calcul de la cote fonctionnelle b₁₆** (p.82) — « Sachant que 4 ≤ Jb ≤ 6 ; b₁₅ = 18±0,5 ; »

1. « Déterminer les équations de : » `Jbmaxi = …` ; `Jbmini = …` ; `b₁₆maxi = …` ; `b₁₆mini = …`
2. « Calculer b₁₆ » (2 lignes)

**C. Dessin de définition de la traverse mobile supérieure (14)** (p.83)
- Données : « Le dessin d'ensemble de la machine d'essai de traction. » ; « Le dessin en 3D de la
  traverse mobile supérieure (14). » ; « La vue de face, la vue de gauche et la vue de dessous
  incomplètes. »
- Travail demandé :
  1. « Compléter la vue de face en coupe A-A. »
  2. « La vue de dessous. »
  3. « La section sortie B-B. »
  4. « Inscrire les spécifications géométriques demandées. »
  5. « Reporter la cote fonctionnelle issue de la chaine de cotes. »
- Figure : vue 3D orange de la traverse (bloc rectangulaire à deux gorges cylindriques et un
  alésage) ; vue de dessous partielle avec traces du plan **A-A** et une cote encadrée vide ; vue
  de face partielle avec traces du plan **B-B**, deux cadres de tolérance géométrique vides
  référencés **A** et le repère de référence **A** ; libellé **B-B** posé sans dessin. Aucune
  échelle imprimée sur cette page.

**D. Dessin de définition du mors mobile (16)** (p.84)
- Données : « Le dessin d'ensemble de la machine d'essai de traction. » ; « Le dessin en 3D en
  coupe du mors mobile (16). » ; « La vue de face et la vue de gauche incomplètes. »
- Travail demandé :
  1. « Compléter la vue de face. »
  2. « La vue de gauche ½ coupe B-B. »
  3. « Inscrire la spécification géométrique demandée. »
  4. « Reporter la cote fonctionnelle issue de la chaine de cotes. »
- Figure : vue 3D en coupe du mors mobile (pièce tronconique taraudée intérieurement, surface
  extérieure moletée) ; vue de face (cercle) avec traces du plan de coupe **B-B** ; vue de gauche
  partielle (silhouette tronconique) avec un cadre de tolérance géométrique vide référencé **A** et
  le repère de référence **A**. Aucune échelle imprimée.

**E. Modélisation numérique (3D et 2D).** (p.84)
- Données : « Le dessin d'ensemble de la machine d'essai de traction. »
- Travail demandé : « Démonter l'arbre (15) support du mors mobile (14) [sic — le mors mobile porte
  le repère (16) à la nomenclature ; (14) est la traverse mobile supérieure], en tenant compte des
  dimensions réelles, modéliser l'arbre (15) en utilisant les logiciels appropriés. »

- **Vocabulaire & terminologie officielle (p.82–84)** : condition fonctionnelle, chaîne de cotes,
  cote fonctionnelle, ajustement `H7/g6`, spécification géométrique, dessin de définition, coupe
  A-A, demi-coupe (½ coupe B-B), section sortie, vue de dessous, moletage, modélisation numérique.

---

##### Synthèse (p.85–86)

- **Compétences affichées** : `CD 3.2`, `CD 3.5`, `CD 3.7` (bandeau des deux pages).
- **Titre imprimé** : onglet « **Synthèse** » seul — le sous-titre « Communication technique » du
  sommaire n'est pas repris sur la page.

**1. Auto-évaluation** (p.85) — « Tester vos connaissances avant de passer à la synthèse avec les Quiz. »
Trois QR-codes encadrés, étiquetés en jaune :
- « **QUIZ lecture dessin d'ensemble** »
- « **QUIZ cotation fonctionnelle** »
- « **QUIZ dessin de définition** »

**2. Synthèse** (encadré vert, p.85–86) — transcription VERBATIM :

> **1. Lecture d'un dessin d'ensemble**
> La lecture d'un dessin d'ensemble se base sur deux étapes :
> - Lecture du dessin d'une manière synthétique : Observation globale des vues et leurs
>   correspondances et acquisition d'une idée sur la nomenclature.
> - Lecture du dessin d'une manière analytique :
>   **Analyse fonctionnelle :** identifier les matières d'œuvres entrante et sortante et la
>   fonction globale,
>   **Analyse du fonctionnement :** Chaîne cinématique ; les liaisons ; les composants…
>   **Analyse des solutions constructives :** avoir une idée sur l'approche techno-économique des
>   choix des solutions.
>
> **2. Graphe de montage et démontage**
> Le graphe de montage et celui de démontage sont des outils donnant un ordre chronologique pour
> le :
> - Montage d'un ensemble neuf
> - Démontage et le remontage d'un mécanisme dans les interventions de maintenance.
>
> **3. Cotation fonctionnelle**
> Un mécanisme est constitué de nombreuses pièces. Pour qu'il puisse fonctionner correctement,
> certaines conditions doivent être respectées (jeux, dépassements, serrages…). C'est le rôle de la
> cotation fonctionnelle qui a pour but :
> - De définir les cotes nominales et les IT de chaque pièce, afin que les conditions soient
>   respectées, et donc d'assurer l'interchangeabilité des pièces d'un mécanisme.
> - De minimiser les coûts de fabrication en donnant les plus larges tolérances possibles des cotes
>   à fabriquer.
>
> **4. Représentation d'un produit fini**
> **a. Dessin de définition**
> Ce dessin représente une seule pièce d'un ensemble ou d'un sous-ensemble. Il définit complètement
> et sans ambiguïté les exigences auxquelles doit satisfaire le produit. Il prépare à la fabrication
> de la pièce par les informations suivantes : matière, forme, cotation dimensionnelle,
> spécifications géométriques, qualité de l'état des surfaces à obtenir. Pour cela on est obligé
> parfois à utiliser les coupes et les sections afin de montrer les parties intérieures d'une pièce.
> **b. Demi-coupes**
> Les demi-coupes sont surtout employées pour les pièces symétriques, ils permettent de voir à la
> fois l'intérieur et l'extérieur de la pièce dans une même vue et par suite d'éviter la
> représentation des détails cachés.
> **c. Coupe brisée à plans sécants**
> La coupe par deux plans concourants permet de montrer, sur la même vue, des formes situées dans
> des plans de coupe sécants. Son emploi évite :
> - Une vue supplémentaire en coupe, suivant une direction oblique.
> - La représentation déformée de certains détails.
> **Remarque :** On ne dessine pas les parties cachées dans le plan rabattu, ces coupes ont la
> particularité de faire pivoter la partie non alignée dans la vue de coupe et de la présenter en
> vraie grandeur.
> **d. Coupe à plans parallèles**
> Cette coupe permet de montrer, sur la même vue, des formes situées dans des plans de coupe
> parallèles. Son emploi évite :
> - Soit une vue supplémentaire en coupe ;
> - Soit la représentation de détails cachés.
> **Méthode d'exécution** :
> - Couper différentes parties de la pièce par des plans parallèles.
> - Supposer ces plans ramenés, sur un seul plan de projection.
> - Repérage des changements de plan en traits forts.
> - Un trait d'axe indique le changement de plan.
> - Hachurage des surfaces avec décalage au changement de plan si cela améliore la clarté du dessin
>   ou comme une coupe simple.
> **e. Sections**
> La section permet la représentation de la section coupée seulement, sans représenter les détails
> derrière le plan de coupe.
> - **Section sortie**
> Elle est dessinée à l'extérieur de l'objet représenté, elle est placée le plus souvent soit dans
> le prolongement du plan de coupe, soit dans le prolongement de l'axe de pièce.
> - **Une section rabattue**
> Elle est rabattue directement sur la vue, dans ce cas elle se trace en trait fin. Le plan de coupe
> et les flèches du sens d'observation sont facultatifs.
>
> **5. Modélisation numérique (3D et 2D)**
> La modélisation tridimensionnelle, consiste à créer, par un logiciel de modélisation 3D, un objet
> en trois dimensions (objet 3D), par ajout, soustraction et modifications de ses constituants pour
> arriver ensuite à la représentation de cet objet en 2D.

**Savoirs plus** (p.86, hors encadré vert) :

> **Savoirs plus** (espace réservé pour les remarques, astuces, conseils… à rédiger par
> l'apprenant)

7 lignes pointillées vierges, puis, en pied de page : « **Grille d'évaluation des savoirs et
savoir-faire de l'apprenant** » suivi d'un **QR-code encadré, étiquette rouge « PDF »**.

- **Vocabulaire & terminologie officielle (p.85–86)** : lecture synthétique / analytique d'un
  dessin d'ensemble, analyse fonctionnelle, analyse du fonctionnement, analyse des solutions
  constructives, approche techno-économique, graphe de montage / de démontage, ordre chronologique,
  maintenance, cotation fonctionnelle, jeu, dépassement, serrage, cote nominale, **IT** (intervalle
  de tolérance), interchangeabilité, tolérance, dessin de définition, cotation dimensionnelle,
  spécification géométrique, état des surfaces, coupe, section, demi-coupe, coupe brisée à plans
  sécants, plans concourants, plan rabattu, vraie grandeur, coupe à plans parallèles, plan de
  projection, trait fort / trait d'axe / trait fin, hachurage, section sortie, section rabattue,
  sens d'observation, modélisation tridimensionnelle.

##### Bornes de scope observées — p.65–86

- ✅ **INCLUS** — traité explicitement à ce niveau :
  - **Lecture d'un dessin d'ensemble** en trois temps normés : analyse fonctionnelle (matières
    d'œuvre, fonction globale, FAST descriptif), analyse du fonctionnement (schéma cinématique,
    classes d'équivalence, liaisons), analyse des solutions constructives (fonction → composant,
    justification des matériaux).
  - **Diagramme FAST descriptif** à compléter (2 occurrences : p.65 avec FT numérotées, p.78 sans).
  - **Schéma cinématique** à compléter par les repères (p.66).
  - **Classes d'équivalence** de pièces cinématiquement liées (p.66, p.79).
  - **Désignation normalisée des matériaux** et sa signification (aciers `S 185`, `C 30`,
    `35 Cr Mo 4` ; alliage d'aluminium `Al Cu 4 Mg` ; bronze `Cu sn 8`).
  - **Graphes de montage / démontage** : filogramme (démontage, avec repère d'ordre, outillages,
    observations) et râteau (montage) — 2 exemples complets à compléter (p.68, p.80–81).
  - **Cotation fonctionnelle** : condition fonctionnelle, cote condition, traçage de chaîne de
    cotes, équations `Jmaxi` / `Jmini`, calcul d'une cote fonctionnelle (`a₆₉` p.69, `b₁₆` p.82),
    vérification d'une condition dans deux positions extrêmes (`Jc`, p.70), caractère maximal /
    minimal d'une condition.
  - **Ajustements** normalisés notés `H7/g6` (p.82) et `H7` seul (p.74) ; ajustement à placer par
    l'élève (p.79).
  - **Dessin de définition** : compléter vues de face / gauche / droite / dessus / dessous,
    coupe A-A, demi-coupe (½ coupe B-B), section sortie (B-B, C-C, E-E), spécifications
    géométriques encadrées avec référence (datum A), tolérance de perpendicularité `⊥ 0,1 A`,
    états de surface `Ra1,6`, chanfreins `1,5x45°` / `5x45°`, échelles (`2:3`, `1:2`, `1:3`, `5:6`,
    `3:10`), symbole de projection au cartouche.
  - **Modélisation numérique 3D et 2D** — énoncée comme travail à réaliser « en utilisant des
    logiciels appropriés » (p.74, p.84), sans nommer de logiciel.
  - **Mesure réelle** au pied à coulisse au 1/50 sur la machine (p.79) — le manuel demande une
    manipulation, pas seulement une lecture de plan.
- ⛔ **EXCLU / seulement mentionné** :
  - Aucun **calcul de résistance des matériaux** : la machine d'essai de traction sert de support de
    lecture de dessin ; l'essai de traction lui-même (courbe, Re, Rm) n'est pas traité ici — le
    thème « Comportement du solide déformable » est annoncé p.216–251.
  - Aucune **cotation de fabrication** ni gamme d'usinage : renvoyées à l'axe 3 (« Obtention des
    pièces », p.252–288).
  - **Aucun corrigé** : toutes les réponses sont des pointillés à remplir ; le manuel est un manuel
    d'activités.
  - Le **contenu des ressources numériques** n'est pas imprimé : QR « Vid » (p.68), 3 QR de quiz
    (p.85), QR « PDF » de la grille d'évaluation (p.86) — hors du livre.
  - Les **tables de tolérances / ajustements ISO** ne sont pas reproduites dans la tranche : elles
    sont supposées disponibles ailleurs (dossier technique / mémento).
  - **Aucune valeur numérique** n'est fournie pour les dessins de définition à compléter (p.71–73,
    p.83–84) : seul le palier arrière (21) p.74 est entièrement coté, parce qu'il sert de modèle.
  - Le sous-ensemble « Noix » figure sur la photo p.75 mais n'a **pas de repère** ni de ligne de
    nomenclature.

#### Thème : Typologie des assemblages (p.87–128)

**Page d'ouverture du thème (p.87)** — bandeaux imprimés, de haut en bas :

- **AXE 2 : ANALYSE STRUCTURELLE ET CONCEPTION**
- **THÈME : TYPOLOGIE DES ASSEMBLAGES**
- **SÉQUENCE :**
  - Les liaisons mécaniques.
  - Conception assistée par ordinateur (CAO).
- **COMPOSANTES DES COMPÉTENCES DISCIPLINAIRES :**

> CD 2.2: Concevoir une solution constructive en justifiant ses choix.
>
> CD 3.8: Établir ou compléter un schéma cinématique.

**Tableau « Typologie des assemblages » (p.87, encadré officiel, verbatim)** :

| CD | Savoirs et savoir-faire | Critères d'évaluation |
| --- | --- | --- |
| CD 2.2 | **Les liaisons mécaniques** — Fonction assemblage. — Fonction guidage en rotation : • Guidage en rotation par roulements à une rangée de billes à contact radial (rappel). • Guidage par roulements à contact oblique. | - Analyse et modélisation correctes des différentes liaisons mécaniques d'un système. - Conception pertinente d'une solution. - Argumentation correcte des solutions choisies. - Respect total des normes de représentation en vigueur. - Prise de décision et choix pertinents des solutions constructives. - Création d'idées nouvelles et réalisables. |
| CD 3.8 | - Conception assistée par ordinateur (CAO): Modélisation en 3D d'un assemblage. - Schéma cinématique. | - Établissement correct d'un schéma cinématique. |

*(La ligne « - Conception assistée par ordinateur (CAO): Modélisation en 3D d'un assemblage. » est imprimée à cheval sur la frontière des deux lignes CD 2.2 / CD 3.8 ; elle est rattachée ici à CD 3.8 avec « - Schéma cinématique. » — voir § Incertitudes.)*

Un QR code étiqueté **PDF** figure en bas à droite de la page.

---

##### Activité 1 — Tête universelle de la fraiseuse (p.88–103)

- **Système / support d'étude** : tête universelle de la fraiseuse « MILKO 14 » (machine-outil d'usinage par fraise).
- **Compétences affichées** : aucune pastille CD sur les pages de présentation (p.88–91) ; **CD 2.2 / CD 3.8** imprimées en tête des pages d'activités 1.1 à 1.5 (p.92–103). Bandeau de page : « TYPOLOGIE DES ASSEMBLAGES » (p.88–91), puis « TYPOLOGIE DES ASSEMBLAGES - ASSEMBLAGE » (p.92–103).
- **Mise en situation (p.88, § 1, verbatim)** :

> La fraiseuse est une machine-outil, permettant de réaliser différentes opérations d'usinage par un outil tournant appelé fraise sur une pièce fixée à la table. Le mouvement de coupe est donné à l'outil et celui d'avance est donné à la pièce.
>
> La tête de la fraiseuse universelle « **MILKO 14** », se compose de deux parties qui peuvent pivoter soit simultanément par rapport au bâti fixe, soit l'une par rapport à l'autre. La combinaison des deux rotations permet de donner à la broche toutes les orientations possibles.

- **Description de fonctionnement (p.88, § 2, verbatim)** :

> Le mouvement de rotation est transmis de l'arbre d'entrée horizontal, lié à la roue dentée (28), à la broche porte outil (36), par un engrenage cylindrique à denture droite (28,9) et deux renvois d'angle à 45° (14,26) et (22,42).

- **Ressources fournies** :
  - **p.88** — vue 3D en coupe de la tête universelle, repérée par étiquettes de texte (non par numéros) : *Bâti fixe*, *Arbre d'entrée*, *Carter*, *Arbre intermédiaire*, *Broche*, *Corps porte broche*. Trois QR codes : *Animation*, *Fichier source réalité augmentée*, *Démonstration réalité augmentée*.
  - **p.89** — § 3 **Dessin d'ensemble** : dessin technique en coupe, cartouche « **Tête universelle de fraiseuse** », **Echelle: 2:5**, symbole de projection (méthode européenne). Repères portés sur le dessin : rangée supérieure **35, 4, 16, 15, 14, 13, 29, 12, 2, 11, 10, 9, 8, 1, 7, 6, 5** ; colonne de gauche **47, 46, 45, 44, 43, 42, 41, 3** puis **34, 39, 40, E, 36, 37, 38, 49, 50** ; repère intérieur **48** ; côté droit **33**, **28**, **32, 31, 30** ; rangée inférieure **21, 17, 18, 19, 20, 22, 23, 24, 25, 26, 27** ; une flèche légendée « **Arbre d'entrée horizontal** ». QR code étiqueté **PDF**. Noter le repère **E** (lettre, non numéro) : c'est l'anneau dont la fonction est demandée en p.103 (question j).
  - **p.90–91** — § 4 **Nomenclature** (50 repères), reproduite ci-dessous.
- **Données numériques de l'énoncé** : engrenage cylindrique à denture droite (28,9) ; deux renvois d'angle à **45°** (14,26) et (22,42) ; échelle du dessin d'ensemble **2:5**.

**Nomenclature de la tête universelle de fraiseuse (p.90–91, verbatim)** :

| Rep. | Nbr. | Désignation | Matière | Observation |
| --- | --- | --- | --- | --- |
| 1 | 1 | Bâti fixe | EN-GJL-200 | |
| 2 | 1 | Carter | EN-GJL-200 | |
| 3 | 1 | Corps porte-broche | EN-GJL-200 | |
| 4 | 1 | Flasque | EN-GJL-200 | |
| 5 | 1 | Vis à tête hexagonale M8x25 | | ISO 4018 |
| 6 | 1 | Rondelle Grower | | |
| 7 | 1 | Rondelle d'appui | | |
| 8 | 1 | Clavette parallèle forme A 8x7x20 | | |
| 9 | 1 | Roue dentée : Z9=50 dents | C35 | |
| 10 | 1 | Écrou à encoches type KM-M30 | | |
| 11 | 1 | Rondelle frein type MB | | |
| 12 | 2 | Roulement………………... | | |
| 13 | 1 | Cales de réglage | | |
| 14 | 1 | Pignon arbré conique Z14=23 dents | C35 | |
| 15 | 1 | Vis à tête cylindrique à six pans creux M8x80 | | DIN 912 |
| 16 | 1 | Rondelle Grower | | |
| 17 | 1 | Arbre creux | C35 | |
| 18 | 1 | Cales de réglage | | |
| 19 | 2 | Butée à aiguilles | | |
| 20 | 2 | Douille à aiguilles | | |
| 21 | 3 | Vis à tête cylindrique à six pans creux M5x25 | | DIN 912 |
| 22 | 1 | Roue conique Z22=23 dents | C35 | |
| 23 | 1 | Vis à tête cylindrique à six pans creux M4x16 | | DIN 912 |
| 24 | 1 | Lardon | | |
| 25 | 1 | Bague de centrage | S275 | |
| 26 | 1 | Roue conique Z26=23 dents | C35 | |
| 27 | 1 | Écrou à encoches type KM-M25 | | |
| 28 | 1 | Roue dentée Z28=51 dents | C35 | |
| 29 | 1 | Anneau de levage mâle M10 | | |
| 30 | 2 | Goupille conique M6x60 | | ISO 8737 |
| 31 | 2 | Écrou hexagonal M6 | | ISO 4032 |
| 32 | 2 | Rondelle plate M6 | | DIN 126 |
| 33 | 2 | Tambour gradué | C35 | |
| 34 | 7 | Graisseur droit hexagonal M8 | | |
| 35 | 1 | Tirant (Vis CHC M16X100) | | DIN 912 |
| 36 | 1 | Broche | C35 | |
| 37 | 4 | Tenon d'entraînement | | |
| 38 | 6 | Vis à tête cylindrique à six pans creux M6x16 | | DIN 912 |
| 39 | 6 | Couvercle | S275 | |
| 40 | 1 | Roulement ……………………… | | |
| 41 | 1 | Cales de réglage | | |
| 42 | 1 | Roue conique Z42=23 dents | C35 | |
| 43 | 1 | Rondelle frein type MB | | |
| 44 | 1 | Écrou à encoches type KM-M40 | | |
| 45 | 1 | Roulement……………………….. | | |
| 46 | 1 | Joint | | |
| 47 | 1 | Écrou spécial | | |
| 48 | 1 | Boitier | EN-GJL-200 | |
| 49 | 1 | Mandrin porte-outil | | |
| 50 | 1 | Fraise à deux tailles | ARS | |

*(Les désignations des repères 12, 40 et 45 sont imprimées en pointillés — « Roulement…… » — : le type de roulement est volontairement laissé à compléter par l'élève.)*

- **Vocabulaire & terminologie officielle (p.88–91)** : machine-outil, opération d'usinage, outil tournant (fraise), mouvement de coupe / mouvement d'avance, bâti fixe, carter, corps porte-broche, broche porte outil, arbre d'entrée horizontal, arbre intermédiaire, engrenage cylindrique à denture droite, renvoi d'angle à 45°, dessin d'ensemble, nomenclature, flasque, clavette parallèle forme A, roue dentée, pignon arbré conique, roue conique, écrou à encoches type KM, rondelle frein type MB, rondelle Grower, butée à aiguilles, douille à aiguilles, lardon, bague de centrage, tambour gradué, graisseur droit hexagonal, tirant (vis CHC), tenon d'entraînement, cales de réglage, mandrin porte-outil, fraise à deux tailles, anneau de levage mâle, goupille conique.

---

###### Activité 1.1 (p.92–94)

- **Système / support d'étude** : assemblage de l'outil sur la broche verticale de la tête universelle (mandrin porte-outil 49 / broche 36).
- **Compétences affichées** : CD 2.2, CD 3.8. Pastilles de compétences transversales imprimées en tête : **COMM**, **COOP**, **CRITI**.
- **Mise en situation — « I. Situation déclenchante » (p.92, encadré, verbatim)** :

> Une opération d'usinage d'une rainure de clavette avec une fraise cylindrique à deux lèvres, impose le changement du mandrin porte-fraise à deux tailles diamètre 50 mm par un mandrin à pince.
>
> **Comment doit-on procéder pour changer l'outil sur la broche verticale ?**

- **Consignes de sécurité (p.92, imprimées en rouge, verbatim)** :

> Durant le déroulement de l'activité :
> Enclencher le bouton d'arrêt d'urgence et vérifier l'arrêt total de la broche avant de démonter la fraise.
> Effectuer les manipulations avec des gants résistants aux coupures.
> Ranger immédiatement les outils à la fin de l'activité.

- **Ressources fournies** : dessin d'ensemble et nomenclature p.89–91 ; **p.92** vue en perspective éclatée de l'ensemble outil/broche avec étiquettes *Tirant*, *Broche*, *Lardon*, *Porte-outil*, *Rainure*, accompagnée d'un trièdre repéré **Tx, Ty, Tz, Rx, Ry, Rz** ; **p.94** schéma cinématique partiel à compléter (voir plus bas).
- **Données numériques de l'énoncé** : fraise à deux tailles de **diamètre 50 mm** (répétée « diamètre 50mm » à la question 1) ; fraise cylindrique à deux lèvres ; repères (36) broche, (49) mandrin porte-outil, (9), (14), (42), (28), (22), (26), (17), (3).
- **Travail demandé** (titre imprimé : « **Analyse de l'assemblage d'outil sur la broche verticale.** ») :
  1. **(p.92)** « Enclencher la plus faible vitesse de la broche puis, citer dans l'ordre les étapes à entreprendre pour démonter l'outil de diamètre 50mm. » (3 lignes de pointillés)
  2. **(p.92)** « Après l'opération de démontage de l'outil, entourer sur le graphe suivant les éléments qui caractérisent la liaison entre la broche (36) et le mandrin porte outil (49). » — graphe imprimé entre deux cases **49** et **36** :

     | Ligne du graphe | Éléments proposés |
     | --- | --- |
     | Ligne du haut | c \| r \| dé \| a \| di |
     | Ligne du bas (chaque terme surmonté d'une barre = complément) | c \| r \| dé \| a \| di |

  3. **(p.92)** « Identification des surfaces fonctionnelles. »
     - a. « Sur la vue en perspective éclatée, colorier en rouge les surfaces de contact entre le cône porte-outil et la broche. »
     - b. **(p.93)** « Mettre en place le mandrin à pince, puis compléter le tableau suivant : » — tableau vierge à trois entrées :

       | Détail de l'assemblage | Mobilité supprimée : TX | TY | TZ | RX | RY | RZ | Nature des surfaces |
       | --- | --- | --- | --- | --- | --- | --- | --- |
       | Mandrin/Broche | | | | | | | |
       | Lardon/Rainure | | | | | | | |
       | Total | *(cellule unique fusionnée sur les six colonnes)* | | | | | | |

     - c. **(p.93)** « Donner le rôle des lardons ? » (2 lignes)
     - d. **(p.93)** « Déduire le rôle du tirant » (1 ligne)
     - e. **(p.93)** « Compléter le tableau suivant en indiquant les éléments et les surfaces participant aux assemblages : »

       | Assemblage | Mise en position (MIP) | Maintien en position (MAP) |
       | --- | --- | --- |
       | Roue dentée (9) /pignon arbré (14) | *(3 lignes vierges)* | *(3 lignes vierges)* |
       | Roue conique (42) /broche (36) | *(3 lignes vierges)* | *(3 lignes vierges)* |

     - f. **(p.93–94)** « Compléter le tableau suivant par les solutions constructives qui assurent les fonctions techniques permettant la transmission du mouvement de l'arbre d'entrée horizontal à la broche (36) : »

       | Fonction technique | Solution constructive |
       | --- | --- |
       | Entrainer la roue dentée (28) en rotation | Arbre d'entrée horizontal *(seule case pré-remplie)* |
       | Transmettre le mouvement de rotation de l'arbre d'entrée horizontal au pignon arbré (14). | *(à compléter)* |
       | Guider en rotation le pignon arbré (14). | *(à compléter)* |
       | Transmettre le mouvement de rotation du pignon arbré (14) à la broche (36). | *(à compléter)* |
       | Guider en rotation les pignons (22) et (26) / l'arbre creux (17). | *(à compléter)* |
       | Fixer l'arbre creux (17) sur le corps porte-broche (3). | *(à compléter)* |
       | Guider en rotation la broche (36). | *(à compléter)* |

     - g. **(p.94)** « En se référant au dossier technique de la tête de la fraiseuse universelle, compléter le schéma cinématique par les symboles normalisés des liaisons et les repères des pièces. » — schéma cinématique partiel imprimé : seul le repère **26** est donné ; sept emplacements en pointillés sont à renseigner ; étiquettes déjà présentes : *Broche (Porte outil)*, *Fraise à deux tailles*, *Arbre d'entrée horizontal*, *Moteur électrique + Boite des vitesses*, avec deux liaisons au bâti (hachures de bâti).
- **Vocabulaire & terminologie officielle** : situation déclenchante, mandrin porte-fraise, mandrin à pince, cône porte-outil, surfaces fonctionnelles, surfaces de contact, mobilité supprimée, nature des surfaces, mise en position (MIP), maintien en position (MAP), fonction technique, solution constructive, schéma cinématique, symboles normalisés des liaisons, dossier technique, lardon, tirant, rainure de clavette.

---

###### Activité 1.2 (p.95–96)

- **Système / support d'étude** : assemblage du carter (2) sur le bâti fixe (1) — orientation de la broche ; puis assemblage des roues coniques (22) et (26).
- **Compétences affichées** : CD 2.2, CD 3.8. Pastilles : **COMM**, **COOP**, **CRITI**.
- **Mise en situation — « I. Situation déclenchante » (p.95, encadré, verbatim)** :

> L'usinage d'une rainure en Vé exige l'orientation de l'axe de la broche de 45°par rapport à la position verticale.
>
> **Quels sont les éléments à manœuvrer pour effectuer cette opération ?**

- **Consigne de sécurité (p.95, en rouge, verbatim)** : « Respecter les règles de sécurité durant le déroulement de l'activité. »
- **Ressources fournies** : « En manipulant la machine et par référence aux dessins 3D ci-dessous. » — **p.95** : vue 3D éclatée du bâti fixe (1), du carter (2) et de sa visserie, avec repères **1**, **51**, **2**, et trois agrandissements **DÉTAIL A** (repères **53**, **52** et un repère en pointillés à trouver), **DÉTAIL B**, **DÉTAIL C**, plus une vue « **Perspective de (51)** » (vis à deux méplats) ; plusieurs bulles de repère sont laissées vides (« …. ») ; **p.96** : vue en perspective éclatée des roues coniques (3 vis, roue dentée, entretoise, couronne) et perspective en 1/4 de coupe des mêmes pièces, toutes bulles vides ; QR code **3D**.
- **Données numériques de l'énoncé** : orientation de l'axe de la broche à **45°** par rapport à la position verticale ; « les quatre écrous (53) » ; nomenclature partielle : M12x47 (6 vis), M12 (14 rondelles), M12 (8 écrous).

**Nomenclature partielle (p.95, verbatim)** :

| Rep. | Nbr. | Désignation | Matière | Observation |
| --- | --- | --- | --- | --- |
| 51 | 6 | Vis à deux méplats M12x47 | | |
| 52 | 14 | Rondelle plate M12 | | DIN 125 |
| 53 | 8 | Écrou hexagonal M12 | | DIN 6915 |

- **Travail demandé** (titre imprimé : « **Analyse de l'assemblage du carter (2) sur le bâti fixe (1).** ») :
  1. **(p.95)** « Desserrer légèrement les quatre écrous (53), puis essayer d'orienter le corps. » — « Constatation : …… »
  2. **(p.95)** « Donner le nom et le rôle de l'élément assurant le positionnement. »
  3. **(p.95)** « Comment procède-t-on pour le démonter ? »
  4. **(p.95–96)** « En se référant au dessin d'ensemble et la vue d'ensemble en perspective : »
     - a. « Indiquer sur la figure ci-dessus les repères des pièces manquants. »
     - b. « Pour une orientation quelconque de la broche, compléter le tableau suivant: »

       | Assemblage | Mise en position (MIP) | Maintien en position (MAP) |
       | --- | --- | --- |
       | Carter (2)/ bâti fixe(1) | *(2 lignes vierges)* | *(2 lignes vierges)* |
       | Nombre des mobilités supprimées | *(2 lignes vierges)* | *(2 lignes vierges)* |

  Puis, second bloc **(p.96)**, titre imprimé « **Analyse de l'assemblage des roues coniques.** » :
  1. « En se référant au dessin d'ensemble et la perspective en 1/4 de coupe ci-dessous: »
     - a. « Indiquer les repères manquants des pièces : » *(6 bulles vides sur la vue éclatée)*
     - b. « Compléter le tableau suivant en indiquant les éléments et les surfaces participant aux assemblages: »

       | Assemblage | Mise en position (MIP) | Maintien en position (MAP) |
       | --- | --- | --- |
       | Roue conique (22)/ Roue conique (26) | *(2 lignes vierges)* | *(2 lignes vierges)* |
       | Nombre des mobilités supprimées | *(2 lignes vierges)* | *(2 lignes vierges)* |

     - c. « Justifier l'utilisation des lardons (24) : » (2 lignes)
  2. « A l'aide de modeleur 3D SolidWorks, réaliser l'assemblage entre les roues coniques (22) et (26) : Emplacement du dossier contenant les pièces et les éléments standards » *(QR code étiqueté **3D**)*.
- **Vocabulaire & terminologie officielle** : rainure en Vé, orientation de l'axe de la broche, élément assurant le positionnement, perspective en 1/4 de coupe, vue d'ensemble en perspective, vis à deux méplats, rondelle plate, écrou hexagonal, nombre des mobilités supprimées, modeleur 3D SolidWorks, éléments standards, lardon.

---

###### Activité 1.3 (p.97–99)

- **Système / support d'étude** : assemblage de la tête universelle sur le bâti fraiseuse (62) ; puis assemblage de la roue dentée (28) avec l'arbre d'entrée horizontal (64).
- **Compétences affichées** : CD 2.2, CD 3.8. Pastilles imprimées p.98 : **COMM**, **COOP**, **CRITI**.
- **Ressources fournies** :
  - **p.97, § 1 « Vue d'ensemble en perspective éclatée »** : éclaté 3D de la tête, du coulisseau (61) et du bâti fraiseuse (62), avec les repères **55, 52, 56, 57, 60, 59, 58** (portés sur les agrandissements **DÉTAIL D**, **DÉTAIL E**, **DÉTAIL F**), **61**, **62**, **54**, **51**, **28**, plus une vue « **Perspective de (54)** » (vis à deux méplats longue) et les repères de zones **D**, **E**, **F**.
  - **p.97, § 2 « Nomenclature partielle »** (ci-dessous) ; mention « Voir également l'animation de démontage » + QR code **Vid**.
  - **p.99** : vue d'ensemble partielle 3D de la liaison roue dentée (28) / arbre d'entrée horizontal (64) avec repères **62**, **63**, **37**, **28**, **38**, **64** et trois agrandissements **DÉTAIL G**, **DÉTAIL H**, **DÉTAIL I** (zones repérées **G**, **H**, **I**), + nomenclature partielle 63–64.
- **Données numériques de l'énoncé** : fraise disque à **3 tailles** ; visserie M12x120, M12x50, M12x40, M12, M8x60, M8, M12x20.

**Nomenclature partielle (p.97, verbatim)** :

| Rep. | Nbr. | Désignation | Matière | Observation |
| --- | --- | --- | --- | --- |
| 54 | 2 | Vis à deux méplats M12x120 | | |
| 55 | 4 | Vis à tête hexagonale M12x50 | | |
| 56 | 2 | Vis à tête hexagonale M12x40 | | |
| 57 | 6 | Rondelle Grower M12 | | |
| 58 | 2 | Goupille conique M8x60 | | ISO 8737 |
| 59 | 2 | Rondelle plate M8 | | ISO 4032 [sic] |
| 60 | 2 | Écrou hexagonal M8 | | DIN 126 [sic] |
| 61 | 1 | Coulisseau | EN-GJL-200 | |
| 62 | 1 | Bâti fraiseuse | EN-GJL-200 | |

**Nomenclature partielle (p.99, verbatim)** :

| Rep. | Nbr. | Désignation | Matière | Observation |
| --- | --- | --- | --- | --- |
| 63 | 2 | Vis à tête cylindrique à six pans creux M12x20 | | DIN 912 |
| 64 | 1 | Arbre d'entrée horizontal | C35 | |

- **Mise en situation — « I. Situation déclenchante » (p.98, encadré, verbatim)** :

> Afin de réaliser une opération d'usinage par une fraise disque à 3 tailles, la fraiseuse doit être configurée à broche horizontale ceci débute par le démontage de la tête.
>
> **Comment entreprendre pour démonter la tête universelle ?**

- **Consignes de sécurité (p.98, en rouge, verbatim)** :

> Enclencher le bouton d'arrêt d'urgence de la machine.
> Utiliser les clés appropriées.
> Effectuer les manipulations avec des gants résistants aux coupures.

- **Travail demandé** (titre imprimé : « **Analyse de l'assemblage de la tête sur le bâti fraiseuse (62).** ») :
  1. **(p.98)** « Citer dans l'ordre les étapes à entreprendre pour démonter la tête ? » (3 lignes)
  2. **(p.98)** « Quelle [sic] est le rôle des rondelles (57) ? » (1 ligne)
  3. **(p.98)** « Donner le rôle de l'anneau de levage (29). » (2 lignes)
  4. **(p.98)** « Compléter le tableau d'assemblage suivant : »

     | Assemblage | Mise en position (MIP) | Maintien en position (MAP) |
     | --- | --- | --- |
     | Tête universelle/ bâti fraiseuse (62) | *(2 lignes vierges)* | *(2 lignes vierges)* |
     | Nombre des mobilités supprimées | *(2 lignes vierges)* | *(2 lignes vierges)* |

  5. **(p.98)** « Après le démontage et dégagement de la tête universelle, peu-t-on [sic] monter l'arbre porte fraise horizontal ? Justifier » (2 lignes)
  6. **(p.99)** Second bloc, titre imprimé « **Analyse de l'assemblage de la roue dentée (28) avec l'arbre d'entrée horizontal (64)** » — « A partir de la vue d'ensemble partiel, compléter le tableau suivant en indiquant les éléments, les formes et les surfaces participants aux assemblages: »

     | Assemblage | Mise en position (MIP) | Maintien en position (MAP) |
     | --- | --- | --- |
     | Roue dentée (28)/ arbre d'entrée horizontal (64) | *(2 lignes vierges)* | *(2 lignes vierges)* |
     | Nombre des mobilités supprimées | *(2 lignes vierges)* | *(2 lignes vierges)* |

- **Vocabulaire & terminologie officielle** : fraise disque à 3 tailles, configuration à broche horizontale, démontage de la tête, anneau de levage, coulisseau, bâti fraiseuse, arbre porte fraise horizontal, tenon d'entraînement, vue d'ensemble partielle, goupille conique, rondelle Grower.

---

###### Activité 1.4 (p.100–101)

- **Système / support d'étude** : solution constructive d'assemblage démontable entre le pignon arbré (14) et la roue conique (tête universelle).
- **Compétences affichées** : CD 2.2, CD 3.8. Pastilles : **COMM**, **COOP**, **CRITI**.
- **Mise en situation — « I. Situation problème » (p.100, encadré, verbatim)** :

> La détérioration d'une ou plusieurs dents au niveau du pignon arbré (14), exige le changement de ce dernier, donc un coût de réparation élevé.
>
> **Quelle solution d'assemblage peut-on adopter pour minimiser le coût et le temps de réparation à la fois ?**

- **Ressources fournies** : « **II. Travail demandé** (voir dessin d'ensemble) » (dessin d'ensemble p.89) ; diagramme F.A.S.T. des deux solutions S1/S2 (p.100) ; **p.101** vue en coupe partielle à compléter, portant les repères **65** (pièce à ajouter, non nomenclaturée dans cette tranche) et **14**, représentant la roue conique montée sur l'arbre ; deux vues 3D de l'assemblage roue conique/arbre avec clavette (en rouge) et deux QR codes **3D**.
- **Données numériques de l'énoncé** : barème de pondération **0 : Mauvais ; 1 : Moyen ; 2 : Bien ; 3 : Très bien** ; repères (14), (9), (65).
- **Travail demandé** :
  1. **(p.100)** « On désire chercher la solution constructive optimale assurant l'assemblage démontable entre l'arbre (9) et la roue conique par les solutions S1 et S2 ci-dessous : » — diagramme imprimé, fonction principale encadrée : « **Assurer une liaison encastrement entre l'arbre (14) et la roue conique.** »

     | Solution | Fonction technique | Solution constructive imprimée |
     | --- | --- | --- |
     | S1 | Lier en rotation | Clavette parallèle + rainures |
     | S1 | Lier en translation | Epaulement + Anneau élastique pour arbre |
     | S2 | Lier en rotation | Cannelures |
     | S2 | Lier en translation | Epaulement + Anneau élastique pour arbre |

  2. **(p.100)** « Critiquer et pondérer les deux solutions S1 et S2. » — tableau vierge à deux colonnes de notation :

     | Critères du choix d'une solution constructive associée à un assemblage | S1 | S2 |
     | --- | --- | --- |
     | Degré de précision de la mise en position | | |
     | Intensité des actions mécaniques transmissibles | | |
     | Fiabilité | | |
     | Maintenabilité | | |
     | Encombrement | | |
     | Esthétique | | |
     | Coût | | |

     Sous le tableau : « Attribuer : 0 : Mauvais ; 1 : Moyen ; 2 : Bien ; 3 : Très bien »
  3. **(p.101)** « Quelle solution doit-on choisir ? Justifier votre choix. » (2 lignes)
  4. **(p.101)** « On demande de compléter à l'échelle de dessin la représentation de la solution choisie. » — « **NB : Utiliser des composants normalisés.** »
  5. **(p.101)** « Réaliser l'assemblage des composants choisis en utilisant le modeleur 3D approprié. » *(deux QR codes **3D**)*
- **Vocabulaire & terminologie officielle** : situation problème, liaison encastrement, assemblage démontable, solution constructive optimale, F.A.S.T. (diagramme fonction technique → solution), lier en rotation / lier en translation, clavette parallèle + rainures, cannelures, épaulement, anneau élastique pour arbre, critères de choix (degré de précision de la mise en position, intensité des actions mécaniques transmissibles, fiabilité, maintenabilité, encombrement, esthétique, coût), pondération, composants normalisés, échelle de dessin, modeleur 3D.

---

###### Activité 1.5 (p.102–103)

- **Système / support d'étude** : guidages en rotation de la tête universelle — broche (36), puis roues coniques (22) et (26).
- **Compétences affichées** : CD 2.2, CD 3.8. Pastilles : **DECI**, **CRITI**.
- **Mise en situation — « I. Situation déclenchante » (p.102, encadré, verbatim)** :

> La tête universelle comporte plusieurs solutions constructives assurant la liaison pivot entre les différents organes de transmission.
>
> **Comment analyser et interpréter les guidages en rotation ?**

- **Ressources fournies** : dessin d'ensemble p.89 ; **p.102** schéma d'un arbre entre deux paliers, à compléter par les symboles des roulements et les arrêts en translation ; **p.103** vue éclatée 3D de la chaîne roues coniques / arbre creux, où seuls **22**, **25** et **26** sont donnés, sept bulles restant vides.
- **Données numériques de l'énoncé** : repères (36), (40), (45), (46), (E), (22), (25), (26) ; deux roulements pour le guidage de la broche.
- **Travail demandé** :
  1. **(p.102)** Titre imprimé : « **Étude de guidage de la broche (36).** » — « Le guidage en rotation de la broche (36) est assuré par deux roulements. »
     - a. « De quel type de roulements s'agit-il ? » (1 ligne)
     - b. « Justifier le choix de ce type de roulement. » (2 lignes)
     - c. « Compléter le schéma ci-dessous par les symboles des roulements et les arrêts en translation des bagues intérieures et extérieures. » *(schéma vierge : arbre + deux paliers hachurés)*
     - d. « Quel type de montage s'agit-il ? (Montage en « X » ; Montage en « O ») Justifier. » (2 lignes)
     - e. « Justifier la différence de dimensions des roulements (40) et (45). » (2 lignes)
     - f. « Par quoi est assuré le réglage du jeu de fonctionnement des roulements (40) et (45) ? » (2 lignes)
     - g. « Quel type de lubrifiant a-t-on utilisé ? Justifier. » (1 ligne)
     - h. **(p.103)** « Par quel élément est assurée cette lubrification ? » (1 ligne)
     - i. **(p.103)** « Quel est le rôle de l'élément (46) ? » (1 ligne)
     - j. **(p.103)** « Donner la fonction de l'anneau (E). » (1 ligne)
  2. **(p.103)** Titre imprimé : « **Étude de guidage des roues coniques (22) et (26).** »
     - a. « En se référant au dessin d'ensemble de la tête de la fraiseuse, compléter les repères manquants des pièces sur la vue éclatée ci-dessous : »
     - b. « Identifier les éléments de guidage en rotation des roues coniques (22) et (26). » (2 lignes)
     - c. « Quels sont les types des charges supportées par ces éléments ? » (2 lignes)
     - d. « Justifier le choix du constructeur de cette solution constructive. » (4 lignes)
- **Vocabulaire & terminologie officielle** : liaison pivot, organes de transmission, guidage en rotation, roulement, bagues intérieures et extérieures, arrêts en translation, montage en « X » / montage en « O », jeu de fonctionnement, lubrifiant, lubrification, charges supportées, symboles des roulements, vue éclatée.

---

##### Activité 2 — Extrudeuse de pâte à savon (p.104–112)

- **Système / support d'étude** : extrudeuse de pâte à savon (« Boudineuse ») — plus précisément son **réducteur à roue et vis sans fin**.
- **Compétences affichées** : aucune pastille CD sur les pages de présentation (p.104–106) ; **CD 2.2 / CD 3.8** en tête des activités 2.1 à 2.3 (p.107–112). Bandeau de page : « TYPOLOGIE DES ASSEMBLAGES - ASSEMBLAGE ».
- **Mise en situation (p.104, § 1, verbatim)** :

> L'extrudeuse de pâte à savon, appelée aussi « Boudineuse », permet de réaliser des barres de savon. Elle est constituée de différents modules dont le réducteur à roue et vis sans fin, qui fait l'objet d'étude dans cette activité.

- **Description du réducteur à roue et vis sans fin (p.104, § 2, verbatim)** :

> Le corps du réducteur est constitué par deux demi-carters fixés par des boulons. Il renferme un engrenage gauche constitué par une vis sans fin et une roue creuse. Le guidage des arbres est assuré par des roulements.

- **Ressources fournies** :
  - **p.104** — vue 3D de l'extrudeuse complète, étiquetée : *Moteur électrique*, *Grille de protection*, *Réducteur à roue et vis sans fin*, *Fourreau*, *Bâti*, *Cône d'extrusion*, *Vis d'extrusion*, *Trémie d'alimentation*, *Nez de sortie (filière)* ; photo 3D du réducteur en coupe ; QR code **Vid**.
  - **p.105** — § 3 **Dessin d'ensemble** : deux vues en coupe **A-A** et **B-B** (planche imprimée en rotation de 90°), cartouche « **REDUCTEUR A ROUE ET VIS SANS FIN** », **Echelle: 2:5**, symbole de projection ; note portée sur la planche : « **(le pied de positionnement (5) ramené dans le plan de coupe)** » ; axes **x**, **y**, **z** matérialisés ; repères : **21, 22, 23, 24, 25, 27** et **26** sur la vue A-A ; **11, 12, 13, 14, 28, 15, 16, 17, 18, 19, 20** en bandeau médian ; **10, 9, 8, 7, 6, 5, 4, 3, 2, 1** sur la vue B-B.
  - **p.106** — § 4 **Nomenclature** (28 repères), ci-dessous.
- **Données numériques de l'énoncé** : Z1 = 1 filet (vis sans fin) ; Z9 = 40 dents (roue creuse) ; échelle du dessin d'ensemble **2:5**.

**Nomenclature du réducteur à roue et vis sans fin (p.106, verbatim)** :

| Rep. | Nbr. | Désignation | Matière | Observation |
| --- | --- | --- | --- | --- |
| 1 | 1 | Vis sans fin | 20 Ni Cr Mo 2 | Z1 = 1 filet |
| 2 | 1 | Joint | | Standard |
| 3 | 1 | Couvercle creux | EN AW-2017 | Corroyé |
| 4 | 1 | Carter inférieur | EN AB-43 000 | |
| 5 | 2 | Pied de positionnement | S 275 | |
| 6 | 1 | Arbre | 42 Cr Mo 4 | |
| 7 | 1 | Clavette parallèle forme A | C 45 | |
| 8 | 1 | Carter supérieur | EN AB-43 000 | |
| 9 | 1 | Roue creuse | Cu Sn 12 | Z9 = 40 dents |
| 10 | 1 | Plaquette | | |
| 11 | 4 | Vis à tête cylindrique fendue | | Standard |
| 12 | 2 | Roulement à rouleaux coniques | | Standard |
| 13 | 1 | Couvercle | EN AB-43 000 | |
| 14 | 6 | Vis à tête hexagonale | | Standard |
| 15 | 6 | Écrou | | Standard |
| 16 | 1 | Anneau élastique pour arbre | | Standard |
| 17 | 1 | Voyant niveau d'huile | | |
| 18 | 1 | Couvercle | EN AB-43 000 | |
| 19 | 2 | Roulement à une rangée de billes à contact radial | 100 Cr 6 | Standard |
| 20 | 1 | Bouchon de vidange | | Standard |
| 21 | 1 | Axe moleté | | |
| 22 | 1 | Écrou | | Standard |
| 23 | 1 | Couvercle | EN AB-43 000 | |
| 24 | 1 | Joint feutre | | Standard |
| 25 | 16 | Vis à tête hexagonale | | Standard |
| 26 | 1 | Bague entretoise | E 295 | |
| 27 | 2 | Cales | | |
| 28 | 6 | Rondelle | | |

- **Vocabulaire & terminologie officielle (p.104–106)** : extrudeuse, boudineuse, barres de savon, module, réducteur à roue et vis sans fin, demi-carters, boulons, engrenage gauche, vis sans fin, roue creuse, guidage des arbres, roulements, fourreau, cône d'extrusion, vis d'extrusion, trémie d'alimentation, nez de sortie (filière), grille de protection, pied de positionnement, plan de coupe, plaquette, axe moleté, bague entretoise, joint feutre, voyant niveau d'huile, bouchon de vidange, cales, anneau élastique pour arbre.

---

###### Activité 2.1 (p.107–108)

- **Système / support d'étude** : assemblage du carter inférieur (4) et du carter supérieur (8) du réducteur.
- **Compétences affichées** : CD 2.2, CD 3.8. Pastilles : **R.PRO**, **CREA**.
- **Mise en situation — « I. Situation déclenchante » (p.107, encadré, verbatim)** :

> Pour s'adapter aux conditions d'utilisation, les réducteurs à engrenages doivent être robustes afin de résister aux conditions extrêmes (Corrosion, fonctionnement en permanence, poussière, etc…)
>
> **Comment peut-on mener une étude des liaisons qui répond à ces conditions ?**

- **Consigne de sécurité (p.107, en rouge, verbatim)** : « Le réducteur à roue et vis sans fin étant fourni, respecter les règles de sécurité durant le déroulement de l'activité. »
- **Ressources fournies** : « Après observation et manipulation du réducteur et par référence à son dossier technique. » ; dessin d'ensemble p.105 et nomenclature p.106 ; **p.108** deux vues du dessin (coupe **C-C** vue de dessus, et vue de face avec les traces de coupe **C**–**C**) portant les repères **15**, **28**, **14**, **4**, **5**, **8** et le repère d'axes **o, x, y, z**.
- **Données numériques de l'énoncé** : repères (4), (8), (5), (10), (21), (23) ; six degrés de liberté Tx, TY, Tz, Rx, Ry, Rz.
- **Travail demandé** :
  1. **(p.107)** « Donner la fonction globale du réducteur. » (1 ligne)
  2. **(p.107)** « Étude de l'assemblage du carter inférieur (4) par rapport au carter supérieur (8) » — graphe imprimé entre deux cases **4** et **8** :

     | Ligne du graphe | Éléments proposés |
     | --- | --- |
     | Ligne du haut | c \| r \| dé \| a \| di |
     | Ligne du bas (chaque terme surmonté d'une barre = complément) | c \| r \| dé \| a \| di |

     - a. « Entourer sur le graphe les éléments qui caractérisent cette liaison. »
     - b. « Démonter doucement le carter supérieur (8), puis identifier la nature des surfaces de contact entre les deux carters (4) et (8). Cocher la bonne réponse. » — deux cases à cocher : **Cylindrique** / **Plane**.
     - c. « Les pieds de positionnement (5) étant enlevés. Indiquer les mouvements supprimés entre les deux carters (4) et (8). » — tableau vierge à six colonnes : **Tx | TY | Tz | Rx | Ry | Rz**.
     - d. « En présence des pieds de positionnement (5) entre (4) et (8). Indiquer les mouvements supprimés entre les deux carters. » — second tableau vierge identique : **Tx | TY | Tz | Rx | Ry | Rz**.
     - e. « Donner le rôle de l'élément (5). » (2 lignes)
     - f. **(p.108)** « Sur les deux vues du dessin ci-dessous, colorier par différentes couleurs les éléments de fixation (Maintien), les éléments de position et les surfaces de contact. »
     - g. **(p.108)** « Compléter le tableau suivant en indiquant les éléments et les surfaces participant aux assemblages: »

       | Assemblage | Mise en position (MIP) | Maintien en position (MAP) |
       | --- | --- | --- |
       | Couvercle (23) / carters (4,8) | *(2 lignes vierges)* | *(2 lignes vierges)* |
       | Axe moleté (21) / plaquette (10) | *(2 lignes vierges)* | *(2 lignes vierges)* |

     - h. **(p.108)** « Remonter le carter supérieur (8) et ranger le matériel. »
- **Vocabulaire & terminologie officielle** : réducteurs à engrenages, conditions extrêmes (corrosion, fonctionnement en permanence, poussière), étude des liaisons, fonction globale, dossier technique, nature des surfaces de contact (cylindrique / plane), pieds de positionnement, mouvements supprimés, éléments de fixation (Maintien), éléments de position, mise en position (MIP), maintien en position (MAP).

---

###### Activité 2.2 (p.109–110)

- **Système / support d'étude** : liaison encastrement entre la roue creuse (9) et l'arbre (6) du réducteur, et son réglage axial.
- **Compétences affichées** : CD 2.2, CD 3.8. Pastilles : **R.PRO**, **CREA**.
- **Mise en situation — « I. Situation problème » (p.109, encadré, verbatim)** :

> La roue creuse nécessite un réglage axial pour assurer la portée correcte des dents
>
> **Quelle solution peut-on choisir pour réaliser ce réglage ?**

- **Ressources fournies** :
  - **p.109** — texte de cadrage : « Analyse de la solution constructive relative à la liaison encastrement entre la roue creuse (9) et l'arbre (6). Solution technologique : » suivi d'un **dessin en coupe de l'arbre (6) équipé**, repéré : **13, 27', 8, 12, 26, 9, 7, 6, 12', 27, 23** (noter les repères primés 27' et 12', qui désignent la seconde occurrence des cales (27) et du roulement à rouleaux coniques (12)).
  - **p.110** — dessin de la nouvelle solution à compléter, **Echelle:1:1**, repères **13, 27, 8, 12, 9, 7, 6, 12', 23** + une flèche légendée « **Cales** » ; QR code **DWG**.
- **Données numériques de l'énoncé** : repères (9), (6), (1), (12), (12'), (27), (27'), (7), (8), (13), (23), (26) ; échelle **1:1** du dessin p.110.
- **Travail demandé** :
  1. **(p.109)** « Compléter le F.A.S.T partiel suivant en indiquant les solutions constructives relatives aux fonctions techniques: » — diagramme imprimé, fonction encadrée « **Assemblage Roue creuse (9) / Arbre (6)** » :

     | Fonction technique | Solution constructive |
     | --- | --- |
     | Lier en rotation | *(2 lignes vierges)* |
     | Lier en translation | *(2 lignes vierges)* |

  2. **(p.110)** « Par quoi est assuré le réglage : »
     - a. « du jeu interne des roulements (12) et (12')? » (1 ligne)
     - b. « de la position axiale de la roue creuse (9) par rapport à la vis sans fin (1)? » (1 ligne)
  3. **(p.110)** « Pour donner plus de performance au réducteur, en évitant le réglage simultané , on propose de modifier partiellement la solution existante par une autre qui assure l'encastrement de la roue creuse (9) avec l'arbre (6) et son réglage axial.  Compléter le F.A.S.T partiel de la nouvelle solution. » — diagramme imprimé, fonction encadrée « **Assemblage Roue creuse (9) / Arbre (6)** » :

     | Fonction technique | Solution constructive |
     | --- | --- |
     | Lier en rotation | Clavette // + rainure *(case pré-remplie)* |
     | Lier en translation | *(2 lignes vierges)* |

  4. **(p.110)** « Compléter à l'échelle de dessin la nouvelle solution. » — « **NB : Utiliser des composants normalisés.** » *(dessin à l'échelle 1:1)*
  5. **(p.110)** « Refaire le même travail en utilisant le logiciel 2D approprié. » *(QR code **DWG**)*
- **Vocabulaire & terminologie officielle** : réglage axial, portée (correcte) des dents, liaison encastrement, solution technologique, F.A.S.T partiel, lier en rotation / lier en translation, clavette // (parallèle) + rainure, jeu interne des roulements, position axiale, réglage simultané, cales, composants normalisés, logiciel 2D.

---

###### Activité 2.3 (p.111–112)

- **Système / support d'étude** : guidage en rotation de la vis sans fin (1) du réducteur, et son remplacement par des roulements à billes à contact oblique.
- **Compétences affichées** : CD 2.2, CD 3.8. Pastilles : **COOP**, **R.PRO**, **CREA**.
- **Mise en situation — « I. Situation problème » (p.111, encadré, verbatim)** :

> Une inspection des roulements (19) avec la technologie des ultrasons, permet de détecter une défaillance précoce.
>
> Cette défaillance est une usure repérée au niveau du chemin des éléments roulants.
>
> **Comment peut-on remédier à ce problème ?**

- **Consigne de sécurité (p.111, en rouge, verbatim)** : « Respecter les règles de sécurité durant le déroulement de l'activité. »
- **Ressources fournies** : « Après observation et manipulation du réducteur et par référence à son dossier technique. » ; **p.112** schéma vierge arbre + deux paliers à compléter ; dessin en coupe du réducteur à compléter (**Echelle:3:4**) portant les repères **9**, **3**, **1**, **4**, **18** et les deux emplacements de roulements notés **R₁** et **R₂** ; QR code **DWG**.
- **Données numériques de l'énoncé** : repères (19), (1), (4), (3), (9), (18), R1, R2 ; échelle **3:4** du dessin p.112.
- **Travail demandé** (titre imprimé : « **Étude du guidage en rotation de la vis sans fin (1)** ») :
  1. **(p.111)** « Démonter le couvercle (4) puis la vis sans fin (1) et identifier le type de roulements choisi par le constructeur ? » (2 lignes)
  2. **(p.111)** « Critiquer le choix et le montage de ces roulements. » (7 lignes)
  3. **(p.111)** « L'étude faite sur l'usure des chemins des éléments roulants, exige le remplacement de ces roulements par une autre paire à billes à contact oblique. Quel type de montage faut-il adopter ? Justifier votre choix. » (8 lignes)
  4. **(p.112)** « Compléter le schéma ci-dessous par les symboles des roulements et les arrêts en translation des bagues intérieures et extérieures. » *(schéma vierge : arbre + deux paliers hachurés)*
  5. **(p.112)** « Compléter à l'échelle du dessin ci-dessous : »
     - « La représentation de la nouvelle solution de guidage de la vis sans fin (1) par les roulements R1 et R2 ; »
     - « L'étanchéité du réducteur ; »
     - « Les tolérances des portées des roulements et du joint. »
     - « **NB :** Utiliser des composants normalisés. »
  6. **(p.112)** « Refaire le même travail en utilisant le logiciel 2D approprié. » *(QR code **DWG**)*
- **Vocabulaire & terminologie officielle** : inspection par ultrasons, défaillance précoce, usure, chemin des éléments roulants, guidage en rotation, roulements à billes à contact oblique, type de montage, symboles des roulements, arrêts en translation des bagues intérieures et extérieures, étanchéité, tolérances des portées (des roulements et du joint), composants normalisés, logiciel 2D.

##### Bornes de scope observées — p.87–112

- ✅ **INCLUS** — traité explicitement, sur deux supports réels (tête universelle de fraiseuse MILKO 14 ; réducteur à roue et vis sans fin d'une extrudeuse de savon) :
  - Lecture d'un **dessin d'ensemble** coté et **échelonné** (2:5, 1:1, 3:4) avec **nomenclature** complète (50 puis 28 repères) et nomenclatures partielles (51–53, 54–62, 63–64).
  - **Caractérisation d'une liaison** par le graphe imprimé **c / r / dé / a / di** et leurs compléments barrés (p.92 entre 49 et 36 ; p.107 entre 4 et 8).
  - **Analyse d'assemblages** : mise en position (MIP) / maintien en position (MAP) ; **mobilités supprimées** exprimées en **Tx, Ty, Tz, Rx, Ry, Rz** ; nature des surfaces de contact (plane/cylindrique) ; nombre de mobilités supprimées.
  - **Solutions constructives d'encastrement** rencontrées ou proposées : clavette parallèle + rainures, cannelures, épaulement + anneau élastique pour arbre, lardons + rainures, tirant, tenons d'entraînement, goupilles coniques, pieds de positionnement, vis/écrous/rondelles (Grower, plate, frein MB), écrous à encoches type KM, cales de réglage.
  - **Choix argumenté d'une solution** : diagramme **F.A.S.T. partiel** (fonction → solution) et **grille de critères pondérée 0-3** (précision de MIP, actions transmissibles, fiabilité, maintenabilité, encombrement, esthétique, coût).
  - **Guidage en rotation par roulements** : identification du type (billes à contact radial, rouleaux coniques, butée/douille à aiguilles), **montage en « X » / en « O »**, réglage du jeu de fonctionnement et du jeu interne, différence de dimensions entre deux roulements, arrêts en translation des bagues, lubrification (type de lubrifiant, graisseur, joint feutre, voyant de niveau d'huile), étanchéité et **tolérances des portées**.
  - **Schéma cinématique** à compléter par les **symboles normalisés** des liaisons et les repères des pièces (p.94).
  - **CAO** : assemblage 3D sous **SolidWorks** (p.96, p.101), reprise en **2D / DWG** (p.110, p.112) ; ressources numériques par QR codes (PDF, animation, réalité augmentée, 3D, vidéo, DWG).
- ⛔ **EXCLU / seulement mentionné dans p.87–112** :
  - **Aucun encadré de cours, de synthèse, de « Retenir » ou de définition** : c'est un **manuel d'activités**. Tous les tableaux, graphes, F.A.S.T. et schémas sont imprimés **vierges**, à remplir par l'élève ; aucun corrigé n'est donné.
  - **Aucun tableau normalisé des liaisons mécaniques** (nom de la liaison / degrés de liberté / symbole / exemple) ni **aucune classe d'équivalence** dans cette tranche : les degrés de liberté n'apparaissent que sous forme de colonnes vides Tx…Rz à cocher (p.93, p.107). *(Le manuel en porte bien une : la **Synthèse du thème, p.127–128**, transcrite plus bas — elle donne les définitions de liaison, d'assemblage et de guidage en rotation que ces pages font seulement manipuler.)*
  - **Aucun calcul** : pas de dimensionnement, pas de durée de vie de roulement, pas de charge chiffrée, pas de rapport de transmission calculé (les nombres de dents sont donnés en nomenclature, jamais exploités numériquement ici).
  - Le repère **65** (p.101) et les repères manquants des vues éclatées (p.95, p.96, p.99, p.103) ne sont **pas** nomenclaturés : ils font partie du travail de l'élève.
  - Les désignations des roulements **12, 40 et 45** de la tête universelle sont imprimées en pointillés (à identifier par l'élève), donc **non renseignées par la source**.
  - La séquence annoncée p.87 (« Conception assistée par ordinateur (CAO) ») n'est pas traitée comme une leçon : elle n'apparaît que par consignes ponctuelles d'usage d'un modeleur 3D / d'un logiciel 2D.
  - Le contenu des ressources derrière les QR codes (animations, réalité augmentée, fichiers 3D/DWG/PDF) n'est pas transcriptible depuis la page.

##### Activité 3 — Chariot élévateur à trois roues · Présentation du support d'activité (p.113–116)

- **Système / support d'étude** : chariot élévateur à trois roues (chariot de manutention
  électrique), et plus précisément son **mécanisme de traction** (dessin d'ensemble p.114,
  échelle 1:2). Le même chariot sert de support aux quatre sous-activités 3.1 à 3.4 (p.117–126).
- **Compétences affichées** : **aucune** — les pages 113 à 116 ne portent pas de badge CD ;
  les badges « CD 2.2 / CD 3.8 » n'apparaissent qu'à partir de la p.117.
- **Bandeau de page** : « TYPOLOGIE DES ASSEMBLAGES - ASSEMBLAGE » (p.113, 114, 115, 116).
- **Titre imprimé** : pastille orange « Activité 3 » (p.113) + cartouche rouge
  « *Chariot élévateur à trois roues* » ; sous-titre bleu « Présentation du support d'activité ».
- **Structure imprimée de l'activité** : 1. Mise en situation (p.113) · 2. Dessin d'ensemble
  (p.114) · 3. Nomenclature (p.115–116).

- **Mise en situation** (texte intégral, p.113) :

  > Le chariot de manutention ci-contre est destiné au chargement-déchargement des palettes.
  > Ce chariot élévateur à trois roues est actionné par trois moteurs électriques alimentés par
  > une batterie 48v [sic] :
  > - Un moteur de traction qui entraîne la roue arrière motrice (44), pour déplacer le chariot,
  >   grâce au mécanisme de traction ;
  > - Un moteur de levée qui actionne un système hydraulique pour soulever ou déposer une charge ;
  > - Un moteur de direction de puissance 0,85 kW (voir schéma cinématique incomplet).

- **Ressources fournies** :
  - **Photographie légendée du chariot** (p.113) — repères textuels portés par flèches :
    « Rails de guidage de la charge », « Poste du conducteur », « Fourches »,
    « Roue arrière motrice ». Chariot à mât de levage avec fourches à l'avant, poste de conduite
    assis à l'arrière, roue arrière unique sous le contrepoids.
  - **Vue 3D écorchée du mécanisme de traction** (p.113) — le carter cylindrique est coupé pour
    montrer le train d'engrenages ; pièces repérées sur la vue :
    « Pignon conique (29) », « Roue conique (37) », « Pignon arbré (5) », « Bâti (46) »,
    « Roue dentée (12) », « Roue dentée (22) », « Roue arrière motrice (44) ».
  - **QR code « Vid »** (ressource vidéo) en bas de p.113.
  - **Dessin d'ensemble p.114** — coupe du mécanisme de traction. Cartouche :
    « Echelle: 1:2 » [sic, sans accent] + symbole de projection européenne ;
    désignations « Mécanisme de traction » / « Chariot élévateur à trois roues ».
    Annotations portées hors cadre : « Côté moteur de traction » (en haut, vers 50/49),
    « Poulie de freinage » (→ 31), « Partie fixée sur le châssis du chariot » (→ zone du 38),
    « Roue arrière motrice » (→ 44). **QR code « PDF »** (dossier technique).
    Repères débités sur le dessin : en haut 51, 50, 49, 27, 28, 29 ; colonne de gauche
    (haut → bas) 52, 26, 25, 24, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,
    48, 19 ; en bas 20, 21, 22, 23, 46 ; colonne de droite (haut → bas) 30, 53, 54, 31, 47, 32,
    33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45. Les 54 repères de la nomenclature sont
    tous présents sur le dessin.
  - **Nomenclature p.115–116** (54 repères), reproduite ci-dessous.

- **Données numériques de l'énoncé** (p.113 à p.116) :
  - batterie 48v [sic] ; moteur de direction : puissance **0,85 kW** ;
  - arbre d'entrée (27) : **N27 = 3000 tr/min** ; arbre moteur (51) : **Nm = 3000 tr/min** ;
  - dentures : pignon arbré (5) **Z5 = 17 dents** ; roue dentée (12) **Z12 = 60 dents** ;
    roue dentée (22) **Z22 = 85 dents** ; pignon conique (29) **Z29 = 16 dents** ;
    roue conique (37) **Z37 = 64 dents** ;
  - roue arrière motrice (44) : **diamètre d = 180 mm** ;
  - entretoises : (23) **L = 25**, (42) **L = 12** ;
  - anneaux élastiques pour alésage : **45 x 1,75** (rep. 6), **55 x 2** (rep. 20) ;
  - joint torique **21,89 x 2,62** (rep. 9) ; joints à lèvres type AS **35 x 47 x 7** (rep. 43)
    et **28 x 47 x 7** (rep. 47) ;
  - clavettes forme A : **8 x 7 x 18** (rep. 17 et 50), **6 x 6 x 20** (rep. 32),
    **6 x 6 x 21** (rep. 33) ;
  - visserie : ISO 4017 M8 x 20 (rep. 2, ×5) et M6 x 20 (rep. 14, ×5) ; ISO 4762 M5 x 10
    (rep. 24 ×4 et rep. 36 ×4), M8 x 22 (rep. 38, ×7), M8 x 16 (rep. 39, ×6), M10 x 20
    (rep. 52, ×6) ; ISO 4026 M4-6 (rep. 8) ; écrous ISO 4032 M12-08 (rep. 30) et M16-08
    (rep. 34) ; écrou à encoches ISO 2982-24 (rep. 18) ; rondelles W 8 (rep. 41, ×6) ;
  - échelle du dessin d'ensemble : **1:2**.

**Nomenclature — « Mécanisme de traction », repères 1 à 27 (p.115)**

En-têtes imprimés : `Rep. | Nbr. | Désignation | Matière | Observation`.
La colonne **Observation est vide sur la totalité de la nomenclature** (p.115 et p.116).
Convention de transcription : `—` = case vide dans la source.

| Rep. | Nbr. | Désignation | Matière | Observation |
| --- | --- | --- | --- | --- |
| 1 | 1 | Bâti partie supérieure | EN-GJL-200 | — |
| 2 | 5 | Vis à tête hexagonale ISO 4017 – M8 x 20 | 25 Cr Mo 4 | — |
| 3 | 1 | Roulement à une rangée de billes à contact radial | — | — |
| 4 | 1 | Bouchon de protection | — | — |
| 5 | 1 | Pignon arbré : Z5 = 17 dents | — | — |
| 6 | 1 | Anneau élastique pour alésage, 45 x 1,75 | C 60 | — |
| 7 | 1 | Roulement à une rangée de billes à contact radial | — | — |
| 8 | 1 | Vis sans tête à six pans creux à bout plat ISO 4026, M4-6 | 25 Cr Mo 4 | — |
| 9 | 1 | Joint torique 21,89 x 2,62. | — | — |
| 10 | 1 | Axe intermédiaire | C 35 | — |
| 11 | 1 | Couvercle de protection | — | — |
| 12 | 1 | Roue dentée : Z12 = 60 dents | — | — |
| 13 | 1 | Bague extérieure | — | — |
| 14 | 5 | Vis à tête hexagonale ISO 4017 – M6 x 20 | 25 Cr Mo 4 | — |
| 15 | 1 | Couvercle | E 360 | — |
| 16 | 1 | Bouchon de remplissage | Acier | — |
| 17 | 1 | Clavette forme A, 8 x 7 x 18 | C 35 | — |
| 18 | 1 | Écrou à encoches ISO 2982-24 | — | — |
| 19 | 1 | Roulement à une rangée de billes à contact radial | — | — |
| 20 | 1 | Anneau élastique pour alésage, 55 x 2 | C 60 | — |
| 21 | 1 | Bouchon de vidange | Acier | — |
| 22 | 1 | Roue dentée : Z22 = 85 dents | — | — |
| 23 | 1 | Entretoise : L = 25 | C 60 | — |
| 24 | 4 | Vis à tête cylindrique à six pans creux ISO 4762 – M5 x 10 | 25 Cr Mo 4 | — |
| 25 | 1 | Boîtier | EN-GJL-200 | — |
| 26 | 1 | Bague entretoise | E 360 | — |
| 27 | 1 | Arbre d'entrée N27 = 3000 tr/min | — | — |

**Nomenclature (suite) — repères 27 à 54 (p.116)**

La p.116 **répète la ligne 27** en tête de tableau (dernière ligne de la p.115 = première ligne
de la p.116), puis enchaîne sur 28 → 54.

| Rep. | Nbr. | Désignation | Matière | Observation |
| --- | --- | --- | --- | --- |
| 27 | 1 | Arbre d'entrée N27 = 3000 tr/min | — | — |
| 28 | 1 | Couvercle | E 360 | — |
| 29 | 1 | Pignon conique :Z29 = 16 dents [sic] | — | — |
| 30 | 1 | Écrou hexagonal ISO 4032 – M12 - 08 | — | — |
| 31 | 1 | Poulie de freinage | — | — |
| 32 | 1 | Clavette forme A, 6 x 6 x 20 | C 35 | — |
| 33 | 1 | Clavette forme A, 6 x 6 x 21 | C 35 | — |
| 34 | 1 | Ecrou hexagonal ISO 4032 – M16 - 08 [sic] | — | — |
| 35 | 1 | Roulement à une rangée de billes à contact radial | — | — |
| 36 | 4 | Vis à tête cylindrique à six pans creux ISO 4762 – M5 x 10 | 25 Cr Mo 4 | — |
| 37 | 1 | Roue conique : Z37 = 64 dents | — | — |
| 38 | 7 | Vis à tête cylindrique à six pans creux ISO 4762 – M8 x 22 | 25 Cr Mo 4 | — |
| 39 | 6 | Vis à tête cylindrique à six pans creux ISO 4762 – M8 x 16 | 25 Cr Mo 4 | — |
| 40 | 1 | Axe (porte roue) | Acier | — |
| 41 | 6 | Rondelle – W 8 | — | — |
| 42 | 1 | Entretoise : L = 12 | C 60 | — |
| 43 | 1 | Joint à lèvres, type AS, 35 x 47 x 7 | — | — |
| 44 | 1 | Roue arrière motrice : diamètre d=180mm | — | — |
| 45 | 1 | Roulement à aiguilles | — | — |
| 46 | 1 | Bâti partie inférieure | EN-GJL-200 | — |
| 47 | 1 | Joint à lèvres, type AS, 28 x 47 x 7 | — | — |
| 48 | 1 | Rondelle frein à longuettes | — | — |
| 49 | 1 | Roulement à une rangée de billes à contact radial | — | — |
| 50 | 1 | Clavette forme A, 8 x 7 x 18 | C 35 | — |
| 51 | [?] | Arbre moteur Nm = 3000 tr/min | — | — |
| 52 | 6 | Vis à tête cylindrique à six pans creux ISO 4762 – M10 x 20 | — | — |
| 53 | 1 | Cale | — | — |
| 54 | 1 | Couvercle | E 360 | — |

- **Travail demandé** : aucun sur p.113–116 — ces quatre pages sont le **dossier technique**
  (support) commun aux activités 3.1 à 3.4.
- **Vocabulaire & terminologie officielle** : chariot de manutention ; chariot élévateur à trois
  roues ; palette ; fourches ; rails de guidage de la charge ; poste du conducteur ; roue arrière
  motrice ; moteur de traction / de levée / de direction ; mécanisme de traction ; système
  hydraulique ; batterie ; schéma cinématique ; dessin d'ensemble ; nomenclature ; repère ;
  pignon arbré ; pignon conique ; roue conique ; roue dentée ; bâti (partie supérieure /
  inférieure) ; boîtier ; couvercle ; poulie de freinage ; axe (porte roue) ; arbre d'entrée ;
  arbre moteur ; entretoise ; bague entretoise ; bague extérieure ; anneau élastique pour
  alésage ; rondelle frein à longuettes ; écrou à encoches ; joint torique ; joint à lèvres type
  AS ; roulement à une rangée de billes à contact radial ; roulement à aiguilles ; clavette
  forme A ; bouchon de remplissage / de vidange / de protection ; cale ; échelle.

##### Activité 3.1 — Les assemblages (p.117–119)

- **Titre imprimé** : pastille « *Activité 3.1* » seule. Le bandeau des p.117–119 porte
  « TYPOLOGIE DES ASSEMBLAGES » **sans sous-titre** ; le titre « Les assemblages » est celui du
  sommaire (p.5).
- **Système / support d'étude** : chariot élévateur à trois roues — dossier technique p.113–116
  (dessin d'ensemble du mécanisme de traction + nomenclature).
- **Compétences affichées** : **CD 2.2** et **CD 3.8** (badges en tête de p.117, p.118, p.119).
  Pictogrammes de démarche imprimés en tête de p.117 : « **R. PRO** » (tête verte) et
  « **DECI** » (tête violette).
- **Mise en situation** — encadré « I. Situation déclenchante » (p.117), verbatim :

  > La résistance, la stabilité et la durée de vie d'un tel système, sont le résultat d'une
  > analyse minutieuse et critique de ses différentes liaisons et en particulier ses assemblages.
  > Elles sont les critères de mesure du niveau de sa performance.
  > **Examinons le fonctionnement du chariot élévateur et faisons une analyse critique qui
  > dévoile le niveau de sa performance.**

- **Ressources fournies** :
  - Dossier technique du chariot élévateur à trois roues (dessin d'ensemble p.114 + nomenclature
    p.115–116).
  - **Actigramme A-0 partiellement imprimé** (p.117) : boîte centrale **vide** (à compléter) ;
    deux entrées fléchées par le haut, imprimées — « Energie électrique et hydraulique » [sic,
    sans accent] et « Consigne du conducteur » ; à gauche, deux lignes de pointillés (entrée à
    compléter) ; à droite, « Signalisation », puis deux lignes de pointillés (sortie à compléter),
    puis « Bruit » ; sous la boîte, la mention **« Chariot élévateur »** reliée par une flèche
    montante.
  - **Dessin partiel en coupe** (p.117, à droite) de la liaison axe (40) / roue arrière motrice
    (44) : repères **39, 40, 41, 44** ; repère d'axes tracé au-dessous — **y** vers le haut,
    **x** vers la droite, **Oz** sortant (cercle pointé).
  - **Schéma cinématique minimal incomplet** du mécanisme de traction (p.119, question i.) :
    blocs rectangulaires « Moteur de traction » et « Moteur de direction » ; à gauche
    « **Courronne** de direction du chariot » [sic] ; deux blocs hachurés « Châssis du chariot »
    (gauche et droite) ; cadre en trait interrompu portant l'annotation « **Zone d'étude** » ;
    en bas, hachurage « **Sol** ». Repères annotés sur le schéma : **51, 27, 29, 31, 37, 5, 12,
    22, 40, 44**.
- **Données numériques de l'énoncé** : repères du dossier technique convoqués — arbre moteur
  (51), arbre d'entrée (27), pignon conique (29), pignon arbré (5), roue conique (37), roue
  dentée (22), roue dentée (12), axe (40), roue arrière motrice (44), poulie de freinage (31),
  vis (39) ×6, rondelle (41). Tableaux de degrés de liberté à 6 colonnes : **Tx | TY | Tz | Rx |
  Ry | Rz** (notation exacte du manuel, « TY » avec Y majuscule).
- **Travail demandé** (chapeau imprimé : « En se référant au dossier technique du chariot
  élévateur à trois roues. ») :
  1. **Compléter l'actigramme de niveau A-0 du chariot.** (p.117)
  2. **Étude de l'assemblage de l'axe (40) et la roue arrière motrice (44).** (p.117–118) :
     - a. **Colorier sur le dessin partiel ci-contre les surfaces de contacts entre (40) et
       (44).** (p.117)
     - b. **Identifier la nature des surfaces de contacts (Cocher les cases correspondantes).**
       (p.117) — quatre libellés encadrés, chacun suivi d'une case à cocher :
       « Surface cylindrique » · « Surface conique » · « Surface plane » · « Méplat ».
     - c. **Indiquer les mouvements supprimés par la surface de contact plane.** (p.118) —
       tableau vide à remplir : `Tx | TY | Tz | Rx | Ry | Rz`.
     - d. **Indiquer les mouvements supprimés par les surfaces de contact plane et cylindrique.**
       (p.118) — second tableau vide identique : `Tx | TY | Tz | Rx | Ry | Rz`.
     - e. **Combien reste de degrés de liberté à éliminer, pour avoir une liaison encastrement?
       Par quel composant(s) est (sont) éliminé(s) ?** (p.118, deux lignes de pointillés)
     - f. **Mettre une croix devant la ou les bonnes réponses.** (p.118) — quatre propositions,
       chacune suivie d'une case :
       - « La vis (39) assure le maintien en position »
       - « Les surfaces de contact assurent la mise en position »
       - « Les vis (39) éliminent les 6 degrés de libertés » [sic]
       - « Les vis (39) éliminent 1 seul degré de liberté »
     - g. **Compléter le tableau ci-dessous par les solutions constructives qui assurent les
       fonctions techniques permettant la transmission du mouvement de l'arbre (27) à la roue
       arrière motrice (44).** (p.118) — tableau à deux colonnes,
       `Fonction technique | Processeurs/Solution constructive`, colonne de droite entièrement
       en pointillés à remplir ; les 11 fonctions techniques imprimées sont, dans l'ordre :

       | # | Fonction technique (imprimée) | Processeurs/Solution constructive |
       | --- | --- | --- |
       | 1 | Convertir l'énergie électrique en énergie mécanique | (à compléter) |
       | 2 | Lier l'arbre moteur (51) à l'arbre d'entrée (27) | (à compléter) |
       | 3 | Guider en rotation l'arbre (27) | (à compléter) |
       | 4 | Lier le pignon conique (29) à l'arbre d'entrée (27) | (à compléter) |
       | 5 | Transmettre le mouvement de rotation de l'arbre (27) au pignon arbré (5) | (à compléter) |
       | 6 | Guider en rotation le pignon arbré (5) | (à compléter) |
       | 7 | Encastrer la roue conique (37) au pignon arbré (5) | (à compléter) |
       | 8 | Transmettre le mouvement de rotation du pignon arbré (5) à l'axe (40) | (à compléter) |
       | 9 | Encastrer la roue dentée (22) à l'axe (40) | (à compléter) |
       | 10 | Guider en rotation l'axe (40) | (à compléter) |
       | 11 | Lier l'axe (40) à la roue arrière motrice (44) | (à compléter) |

     - h. **Compléter le tableau suivant en indiquant les éléments, les formes et les surfaces
       participant aux assemblages:** (p.119) — tableau
       `Assemblage | Mise en position (MIP) | Maintien en position (MAP)`, trois lignes
       imprimées, colonnes MIP et MAP en pointillés (deux lignes chacune) :

       | Assemblage (imprimé) | Mise en position (MIP) | Maintien en position (MAP) |
       | --- | --- | --- |
       | Pignon conique (29) / arbre d'entrée (27) | (à compléter) | (à compléter) |
       | Pignon conique (37) / pignon arbré (5) [sic — la nomenclature p.116 désigne le rep. 37 « Roue conique »] | (à compléter) | (à compléter) |
       | Pignon arbré (5) / poulie de freinage (31) | (à compléter) | (à compléter) |

     - i. **Compléter le schéma cinématique minimal du mécanisme de traction.** (p.119)
- **Encadrés officiels (verbatim)** : l'unique encadré de l'activité 3.1 est la
  « I. Situation déclenchante » ci-dessus (p.117). Aucun encadré « Retenir » sur p.117–119.
- **Vocabulaire & terminologie officielle** : liaison ; assemblage ; actigramme de niveau A-0 ;
  matière d'œuvre / consigne / énergie électrique et hydraulique / signalisation / bruit ;
  surface de contact (cylindrique, conique, plane, méplat) ; degré de liberté ; mouvements
  supprimés ; Tx, TY, Tz, Rx, Ry, Rz ; liaison encastrement ; mise en position (MIP) ; maintien
  en position (MAP) ; fonction technique ; processeur / solution constructive ; encastrer ;
  guider en rotation ; lier ; transmettre le mouvement de rotation ; schéma cinématique
  minimal ; châssis ; couronne de direction ; zone d'étude.

##### Activité 3.2 — Guidage en rotation [de la roue avant] (p.120–122)

- **Titre imprimé** : pastille « *Activité 3.2* » (p.120 puis rappelée p.121). Les bandeaux des
  p.120, 121, 122 portent « TYPOLOGIE DES ASSEMBLAGES » **sans sous-titre** ; le titre
  « Guidage en rotation » est celui du sommaire (p.5). Le titre de travail imprimé en gras sur
  p.121 est : « **Étude du guidage en rotation de la roue avant du chariot élévateur à trois
  roues** ».
- **Système / support d'étude** : **mécanisme de roue avant** du chariot élévateur à trois roues
  (dessin d'ensemble propre, p.120, échelle 1:2) — support **distinct** du mécanisme de traction
  de l'activité 3.1, avec sa **propre nomenclature (repères 55 à 68)**.
- **Compétences affichées** : **CD 2.2** et **CD 3.8** (p.120, 121, 122). Pictogrammes en tête de
  p.121 : « **R. PRO** » et « **CREA** ».
- **Mise en situation** — encadré « I. Situation déclenchante » (p.121), verbatim :

  > Le constructeur a utilisé les roulements (63) pour le guidage en rotation des deux roues
  > avant (56).
  > **Comment analyser et interpréter le guidage en rotation des roues avant ?**

- **Ressources fournies** :
  - **1. Dessin d'ensemble** (p.120) : coupe du mécanisme de roue avant, repères débités
    68, 67, 66, 65, 64, 63, 62 (côté gauche/bas) et 55, 56, 57, 58, 59, 60, 61 (côté droit).
    Cartouche imprimé sous la nomenclature : « Echelle: 1:2 » + symbole de projection
    européenne ; désignations « **Mécanisme roue avant** » / « Chariot élévateur à trois roues ».
    En-têtes de la nomenclature imprimés **en bas du tableau** (convention dessin) :
    `Rep. | Nb. | DESIGNATION | MATIERE | Observation` [sic, DESIGNATION et MATIERE sans
    accents, « Nb. » au lieu de « Nbr. »], et les lignes se lisent **de bas en haut** (55 → 68).
  - **Schéma d'arbre/moyeu vierge** (p.121, question d.) : représentation en coupe d'un arbre
    plein entre deux portées de moyeu hachurées, sans symbole de roulement — à compléter.
  - **Logiciel « PyVot0.6 »** + copie d'écran du logiciel (p.122) : barre de menus
    « Fichier / Affichage / Insertion / Action / Aide », palettes « Éléments / Analyse »,
    « Roulements », « Arrêts », « Joints », sélecteur « Taille de roulement : petit / grand »,
    onglets « à billes / à rouleaux », vignettes de roulements, et un cadre
    « Cahier des Charges Fonctionnel » avec « Efforts sur l'arbre » (intensité et répartition,
    graduations « très faible »), « Coût admissible », « Lubrification - Etanchéité »,
    « Mobilité bagues/charge radiale » (« Bague tournante par rapport à la charge Radiale » :
    boutons « Intérieure » / « Extérieure »).
  - **QR code « ZIP »** en bas de p.122 (ressource logicielle à télécharger).
- **Données numériques de l'énoncé** : roue avant (56) **diamètre d = 180 mm** ; roulements (63)
  au nombre de **2** ; vis ISO 4017 M10x30 (rep. 66, ×4) ; vis ISO 4762 M8x25 (rep. 57, ×5) ;
  rondelles W10 (rep. 67, ×4), W8 (rep. 58, ×5), W12 (rep. 60) ; écrou hexagonal M12 (rep. 59) ;
  anneau élastique pour alésage **55 x 2** (rep. 64) ; échelle du dessin **1:2**.

**Nomenclature — « Mécanisme roue avant », repères 55 à 68 (p.120)**

Transcrite ici de 55 à 68 (le manuel l'imprime dans l'ordre inverse, 68 en haut).
Colonne **Observation vide** sur toutes les lignes ; `—` = case vide dans la source.

| Rep. | Nb. | DESIGNATION | MATIERE | Observation |
| --- | --- | --- | --- | --- |
| 55 | 1 | Châssis | EN-GJL-200 | — |
| 56 | 1 | Roue avant : diamètre d=180mm | — | — |
| 57 | 5 | Vis à tête cylindrique à six pans creux ISO 4762 - M8x25 | 25 Cr Mo 4 | — |
| 58 | 5 | Rondelle - W8 | — | — |
| 59 | 1 | Ecrou hexagonal M12 [sic] | — | — |
| 60 | 1 | Rondelle - W12 | — | — |
| 61 | 1 | Bague d'appui | S 275 | — |
| 62 | 1 | Bague entretoise | S 275 | — |
| 63 | 2 | Roulement à une rangée de billes à contact radial | — | — |
| 64 | 1 | Anneau élastique pour alésage, 55 x 2 | C 60 | — |
| 65 | 1 | Arbre support | C 35 | — |
| 66 | 4 | Vis à tête hexagonale ISO 4017 - M10x30 | 25 Cr Mo 4 | — |
| 67 | 4 | Rondelle - W10 | — | — |
| 68 | 1 | Moyeu | C 35 | — |

- **Travail demandé** :
  - Chapeau imprimé (p.121) : « **Étude du guidage en rotation de la roue avant du chariot
    élévateur à trois roues** ».
  1. **En se référant au dessin d'ensemble.** (p.121)
     - a. **Colorier l'ensemble des pièces en rotation.**
     - b. **De quel type de roulement s'agit-il ?** (une ligne de pointillés)
     - c. **Quelles sont les bagues montées serrées (extérieures ou intérieures) ?**
       (deux lignes de pointillés)
     - d. **Compléter le schéma ci-dessous en indiquant le symbole des roulements et
       l'emplacement des arrêts en translation des bagues intérieures et extérieurs.** [sic,
       « extérieurs » au masculin] — schéma arbre/moyeu vierge imprimé au-dessous.
     - e. **Le montage est-il à arbre tournant ou moyeu tournant, cocher la bonne réponse:** —
       deux propositions à cocher : « Arbre tournant » · « Moyeu tournant ».
       Puis, en ligne séparée : « **Inscrire sur le schéma ci-dessus les tolérances des portées
       des roulements.** »
     - f. **Justifier le choix de ce type de roulements.** (trois lignes de pointillés)
     - g. **Expliquer comment est réalisée la lubrification des roulements ?** (quatre lignes de
       pointillés)
  2. **Préciser dans le tableau ci-dessous les noms de tous les éléments et formes qui
     participent à l'arrêt des bagues extérieures et intérieures.** (p.122) — tableau
     `Bagues | Solutions` avec la colonne « Solutions » scindée en
     `Élément standard | Autre` ; deux lignes imprimées, « Intérieures » et « Extérieures »,
     toutes les cases en pointillés :

     | Bagues | Élément standard | Autre |
     | --- | --- | --- |
     | Intérieures | (à compléter) | (à compléter) |
     | Extérieures | (à compléter) | (à compléter) |

  3. **Exploitation du logiciel pivot sur ordinateur** (p.122) :
     « Lancer le logiciel « PyVot0.6 » qui va vous permettre de placer des roulements sur un
     arbre, des arrêts axiaux (épaulements, anneaux élastiques…). » puis les quatre consignes
     imprimées :
     - « Sélectionner les roulements qui conviennent. Puis les placer dans la fenêtre
       d'édition. »
     - « Placer ensuite les arrêts axiaux de la même façon en les sélectionnant. »
     - « Une fois le montage fini, cliquer sur « analyse » pour vérifier l'exactitude de montage
       de la roue avant. »
     - « Remettre le poste de travail à l'état initial. »
- **Encadrés officiels (verbatim)** : l'unique encadré de l'activité 3.2 est la
  « I. Situation déclenchante » ci-dessus (p.121).
- **Vocabulaire & terminologie officielle** : guidage en rotation ; roulement à une rangée de
  billes à contact radial ; bague intérieure / bague extérieure ; bague montée serrée ; arrêt en
  translation ; arrêt axial ; épaulement ; anneau élastique ; arbre tournant / moyeu tournant ;
  tolérance des portées de roulement ; lubrification ; symbole de roulement ; élément standard ;
  moyeu ; arbre support ; bague d'appui ; bague entretoise ; châssis ; roue avant ; cahier des
  charges fonctionnel ; étanchéité.

##### Activité 3.3 — Les assemblages (p.123–124)

- **Titre imprimé** : pastille « *Activité 3.3* ». Bandeau p.123 :
  « TYPOLOGIE DES ASSEMBLAGES / **LES ASSEMBLAGES** » ; bandeau p.124 :
  « TYPOLOGIE DES ASSEMBLAGES - ASSEMBLAGE ».
- **Système / support d'étude** : chariot élévateur à trois roues — **liaison complète entre
  l'axe (40) et la roue arrière motrice (44)** du mécanisme de traction (mêmes dessin d'ensemble
  p.114 et nomenclature p.115–116).
- **Compétences affichées** : **CD 2.2** et **CD 3.8** (p.123 et p.124). Pictogrammes en tête de
  p.123 : « **R. PRO** » et « **CREA** ».
- **Mise en situation** — encadré « I. Situation problème » (p.123), verbatim :

  > Le rôle important du chariot dans l'activité d'une entreprise, exige une interchangeabilité
  > rapide de sa roue arrière (44) après chaque dommage.
  > **Comment rendre ceci réel, fiable et performant ?**

- **Ressources fournies** :
  - **Graphe de liaison imprimé** (p.123, question 1) : deux blocs `40` et `44` reliés par cinq
    couples de caractères superposés — au-dessus de la barre `c`, `r`, `dé`, `a`, `di` ; au-
    dessous, leurs compléments surlignés d'une barre : `c̄`, `r̄`, `dé̄`, `ā`, `dī`.
  - **Graphe FAST des deux solutions S1 / S2** (p.123, question 2) — voir tableau ci-dessous.
  - **Tableau de pondération** vierge (p.124, question 1).
  - **Dessin partiel en coupe à compléter** (p.124, question 3) : coupe de la liaison
    axe/roue arrière motrice, repères débités **23, 46, 17, 18, 48, 19, 20, 22, 40, 43, 44, 45**.
  - **QR code « ZIP »** en bas de p.124 (modeleur 2D / fichiers de travail).
- **Données numériques de l'énoncé** : barème de pondération **0 : Mauvais ; 1 : Moyen ;
  2 : Bien ; 3 : Très bien** ; sept critères de choix ; deux solutions S1 et S2.
- **Travail demandé** :
  - Chapeau imprimé (p.123) : « **Analyse de la solution constructive relative à la liaison
    complète entre l'axe (40) et la roue arrière motrice (44).** »
  1. **Entourer sur le graphe les éléments qui caractérisent cette liaison.** (p.123)
  2. **Après une étude approfondie, l'équipe chargée de trouver une solution constructive fiable
     pour cet assemblage propose deux solutions S1 et S2 :** (p.123) — graphe imprimé, fonction
     racine encadrée « **Assurer une liaison encastrement entre l'axe (40) et la roue arrière
     motrice (44)** », puis :

     | Solution | Fonction technique | Solution constructive (imprimée) |
     | --- | --- | --- |
     | **S₁** | Lier en rotation | Clavette parallèle + rainures |
     | **S₁** | Lier en translation | Epaulement + rondelle d'appui + rondelle frein + écrou à encoches [sic, « Epaulement » sans accent] |
     | **S₂** | Lier en rotation | Cannelures |
     | **S₂** | Lier en translation | Epaulement + rondelle d'appui + écrou et contre écrou [sic] |

  *(la numérotation des questions **repart à 1** en haut de la p.124 — voir § Incertitudes)*
  1. **Critiquer et pondérer les deux solutions S1 et S2.** (p.124) — tableau à trois colonnes
     `Critères du choix d'une solution constructive associée à un assemblage | S1 | S2`, sept
     lignes imprimées, cases S1/S2 vides :

     | Critères du choix d'une solution constructive associée à un assemblage | S1 | S2 |
     | --- | --- | --- |
     | Degré de précision de la mise en position | (à remplir) | (à remplir) |
     | Intensité des actions mécaniques transmissibles | (à remplir) | (à remplir) |
     | Fiabilité | (à remplir) | (à remplir) |
     | Maintenabilité | (à remplir) | (à remplir) |
     | Encombrement | (à remplir) | (à remplir) |
     | Esthétique | (à remplir) | (à remplir) |
     | Coût | (à remplir) | (à remplir) |

     Consigne de barème imprimée sous le tableau, verbatim :
     > Attribuer :
     > 0 : Mauvais ; 1 : Moyen ; 2 : Bien ; 3 : Très bien

  2. **Quelle solution doit-on choisir ? Justifier votre choix.** (p.124, deux lignes de
     pointillés)
  3. **On demande de compléter à l'échelle de dessin la solution choisie.** (p.124)
     — **NB : Utiliser des composants normalisés.**
  4. **Refaire le même travail en utilisant le modeleur 2D approprié.** (p.124)
- **Encadrés officiels (verbatim)** : « I. Situation problème » (p.123) ci-dessus, et la
  consigne de barème de la p.124 ci-dessus. Aucun encadré « Retenir » sur p.123–124.
- **Vocabulaire & terminologie officielle** : interchangeabilité ; liaison complète ; liaison
  encastrement ; solution constructive ; graphe de liaison ; lier en rotation / lier en
  translation ; clavette parallèle + rainures ; cannelures ; épaulement ; rondelle d'appui ;
  rondelle frein ; écrou à encoches ; écrou et contre écrou ; critères de choix ; degré de
  précision de la mise en position ; intensité des actions mécaniques transmissibles ;
  fiabilité ; maintenabilité ; encombrement ; esthétique ; coût ; pondération ; composants
  normalisés ; modeleur 2D ; échelle de dessin.

##### Activité 3.4 — Guidage en rotation [du pignon arbré (5)] (p.125–126)

- **Titre imprimé** : pastille « *Activité 3.4* ». Bandeau des p.125 et p.126 :
  « TYPOLOGIE DES ASSEMBLAGES / **GUIDAGE EN ROTATION** » (le sous-titre est imprimé en petites
  capitales dans une police décorative). Titre de travail imprimé en gras (p.125) :
  « **Étude du guidage en rotation du pignon arbré (5)** ».
- **Système / support d'étude** : chariot élévateur à trois roues — **guidage en rotation du
  pignon arbré (5)** dans le mécanisme de traction (dessin d'ensemble p.114 + nomenclature
  p.115–116), puis **nouvelle conception** proposée p.126.
- **Compétences affichées** : **CD 2.2** et **CD 3.8** (p.125 et p.126). Pictogrammes en tête de
  p.125 : « **R. PRO** » et « **CREA** ».
- **Mise en situation** — encadré « I. Situation problème » (p.125), verbatim :

  > Le constructeur a utilisé pour le guidage en rotation du pignon arbré (5) deux roulements (3)
  > et (35). Ce type de roulements ne peut pas encaisser les efforts axiaux importants engendrés
  > par la forme conique du pignon (29) et la roue (37).
  > **Quelle solution peut-on adopter pour remédier à ce problème ?**

- **Ressources fournies** :
  - Dossier technique du chariot élévateur à trois roues (dessin d'ensemble p.114 + nomenclature
    p.115–116).
  - **Schéma arbre/moyeu vierge** (p.126, question 8) : coupe d'un arbre entre deux portées de
    moyeu hachurées, sans symbole de roulement — à compléter.
  - **Dessin de la nouvelle conception** (p.126, bas de page), **Echelle: 2:5** [sic, sans
    accent] : coupe montrant le pignon arbré guidé par **deux roulements à rouleaux coniques**
    montés en opposition, repérés « **R₁** » (à gauche) et « **R₂** » (à droite) ; autres
    repères portés sur le dessin : **1** (bâti partie supérieure, deux amorces), **5** (pignon
    arbré), **37** (roue conique), **31** (poulie de freinage), **33** (clavette), **34** (écrou
    hexagonal M16).
  - **QR code « ZIP »** en bas de p.126.
- **Données numériques de l'énoncé** : roulements existants **(3)** et **(35)** ; pignon conique
  **(29)** ; roue conique **(37)** ; couvercle **(54)** ; pignon arbré **(5)** ; échelle du
  dessin de la nouvelle conception **2:5**.
- **Travail demandé** (chapeau imprimé : « En se référant au dossier technique du chariot
  élévateur à trois roues. » puis « **Étude du guidage en rotation du pignon arbré (5)** » et
  « Le pignon arbré (5) est guidé en rotation par deux roulements (3) et (35). ») :
  1. **De quel type de roulement s'agit-il ?** (p.125, une ligne de pointillés)
  2. **Le montage de ces roulements est-il à : « Arbre tournant » ou à «Moyeu tournant » ?**
     (p.125, une ligne de pointillés)
  3. **Inscrire sur le dessin d'ensemble les tolérances des portées des roulements.** (p.125)
  4. **Critiquer le choix et le montage de ces roulements.** (p.125, quatre lignes de pointillés)
  5. **Pourquoi retrouve-t-on un réglage au niveau du couvercle (54) ?** (p.125, trois lignes de
     pointillés)
  6. **Pour remédier au problème des charges axiales engendrées par l'engrenage conique. Quel
     type de roulements faut-il choisir ? Justifier votre réponse.** (p.125, trois lignes de
     pointillés)
  7. **Quel type du montage faut-il adopter ?** (p.125) — deux propositions encadrées, chacune
     suivie d'une case à cocher : « **Montage en «O»** » · « **Montage en «X»** ».
  8. **En se référant au dessin de la nouvelle conception, Compléter le schéma ci-dessous en
     indiquant le symbole des roulements et l'emplacement des arrêts en translation des bagues
     intérieures et extérieures.** (p.126)
  9. **Compléter à l'échelle du dessin la représentation de la nouvelle solution de guidage du
     pignon arbré (5) ;** (p.126)
  10. **Assurer l'étanchéité du mécanisme ;** (p.126)
  11. **Inscrire les tolérances des portées des roulements et de la roue conique (37).** (p.126)
      — **NB : Utiliser des composants normalisés.**
  12. **Refaire le même travail en utilisant le logiciel 2D approprié.** (p.126)
- **Encadrés officiels (verbatim)** : « I. Situation problème » (p.125) ci-dessus. Aucun encadré
  « Retenir » sur p.125–126.
- **Vocabulaire & terminologie officielle** : guidage en rotation ; efforts axiaux / charges
  axiales ; engrenage conique ; pignon conique ; roue conique ; roulement à rouleaux coniques ;
  montage en « X » / montage en « O » ; arbre tournant / moyeu tournant ; arrêt en translation
  des bagues ; réglage (cale, couvercle) ; tolérance de portée ; étanchéité ; composants
  normalisés ; logiciel 2D.

##### Synthèse — Typologie des assemblages (p.127–128)

- **Titre imprimé** : pastille orange « *Synthèse* » (p.127 et p.128). Bandeau des deux pages :
  « TYPOLOGIE DES ASSEMBLAGES ».
- **Compétences affichées** : **CD 2.2** et **CD 3.8** (p.127 et p.128).
- **Structure imprimée** : 1. Auto-évaluation (p.127) · 2. Synthèse assemblage (p.127) ·
  3. Synthèse guidage en rotation (p.128) · « Savoirs plus » (p.127 et p.128) ·
  « Grille d'évaluation des savoirs et savoir-faire de l'apprenant » (p.128).

**1. Auto-évaluation (p.127)** — texte imprimé :

> Tester vos connaissances avant de passer à la synthèse avec les Quiz.

Deux bandeaux jaunes avec QR codes, marqués « **EXE** » : « **QUIZ Assemblage** » et
« **QUIZ guidage en rotation** ».

**2. Synthèse assemblage (p.127)** — encadré vert, verbatim :

> Un assemblage est un procédé permettant de lier entre elles plusieurs pièces pour former un
> ensemble. Chaque assemblage est distingué par ses degrés de liaisons, c'est-à-dire les
> mouvements relatifs indépendants interdits ou autorisés entre les pièces assemblées.
> Ceci nous ramène à distinguer deux assemblages appelés aussi liaisons :
> - Une liaison complète (0 degrés de mobilité) ;
> - Une liaison partielle (au moins 1 degré de mobilité).
>
> **1. Liaison complète démontable**
> La liaison est conçue de manière à être démontée sans détérioration importante des pièces liées
> ni les éléments de liaison, qui peuvent être généralement utilisés pour recréer un assemblage.
> En général l'assemblage est caractérisé par deux fonctions :
> - La mise en position (MIP), qui est le positionnement d'une pièce par rapport à une autre, on
>   peut envisager d'utiliser des surfaces : planes, cylindriques, coniques…
> - Le maintien en position (MAP), qui est responsable de la conservation du contact entre les
>   pièces positionnées à l'aide d'un obstacle démontable ou par adhérence.
>
> **2. Liaison partielle**
> La liaison est conçue de manière à autoriser au moins un degré de mobilité pour un
> fonctionnement donné de l'assemblage (pivot, glissière, hélicoïdale…).

Sous l'encadré (p.127), rubrique imprimée en rouge, verbatim :

> **Savoirs plus** (espace réservé pour les remarques, astuces, conseils… à rédiger par
> l'apprenant)

suivie de dix lignes de pointillés vierges.

**3. Synthèse guidage en rotation (p.128)** — encadré vert, verbatim :

> C'est la réalisation concrète d'une liaison pivot par plusieurs moyens de guidage, dont on
> distingue les roulements.
> Les roulements, (généralement montés par paire) sont choisis selon deux principaux critères :
> - Les charges à supporter et leurs directions ;
> - La vitesse à transmettre.
>
> Pour un guidage qui supporte des charges radiales et axiales importantes, on adopte des
> roulements à billes à contact oblique (vitesse importante) ou des roulements à rouleaux
> coniques (vitesse moyenne).
> Généralement pour un arbre tournant le montage est appelé en « X », pour le cas d'un moyeu
> (alésage) tournant le montage est appelé en « O ».
> Les arrêts axiaux des bagues intérieures et extérieures des roulements, sont au nombre de
> quatre, dont un qui fait le réglage comme indiqué sur l'exemple du montage en « X » ci-dessous.

**Figure de la synthèse (p.128, dans l'encadré vert)** : dessin en coupe d'un **montage en
« X »** — un arbre étagé guidé par deux roulements à billes à contact oblique montés en X dans
un logement. Annotations imprimées sur la figure : « **Cales de réglage** » (à gauche, sur les
cales sous le couvercle), « **Logement fixe** », « **Arbre tournant** », « **Joint** » (à
droite). Deux cotes de tolérance sont portées sur les portées de roulement :
**Ø…m6** (portée d'arbre, à gauche) et **Ø…H7** (alésage du logement, à droite) — les valeurs
nominales sont volontairement laissées en pointillés dans la source.

Sous l'encadré (p.128), la même rubrique verbatim :

> **Savoirs plus** (espace réservé pour les remarques, astuces, conseils… à rédiger par
> l'apprenant)

suivie de neuf lignes de pointillés vierges, puis, en bas de page, la mention et son QR code
« **PDF** » :

> Grille d'évaluation des savoirs et savoir-faire de l'apprenant

- **Vocabulaire & terminologie officielle (synthèse)** : assemblage ; degrés de liaisons ;
  mouvements relatifs indépendants ; liaison complète (0 degré de mobilité) ; liaison partielle
  (au moins 1 degré de mobilité) ; liaison complète démontable ; éléments de liaison ; mise en
  position (MIP) ; maintien en position (MAP) ; obstacle démontable ; adhérence ; surfaces
  planes / cylindriques / coniques ; pivot ; glissière ; hélicoïdale ; guidage en rotation ;
  liaison pivot ; roulement ; montés par paire ; charges radiales et axiales ; roulement à billes
  à contact oblique ; roulement à rouleaux coniques ; arbre tournant ; moyeu (alésage) tournant ;
  montage en « X » ; montage en « O » ; arrêts axiaux ; bagues intérieures et extérieures ;
  réglage ; cales de réglage ; logement fixe ; joint ; tolérances m6 / H7.

##### Bornes de scope observées — p.113–128

- ✅ **INCLUS** — ce que le manuel traite explicitement dans cette tranche :
  - **Analyse d'un assemblage réel** : identification des surfaces de contact (cylindrique,
    conique, plane, méplat), mouvements supprimés exprimés dans le repère `Tx TY Tz Rx Ry Rz`,
    décompte des degrés de liberté restants pour obtenir un **encastrement** (p.117–118).
  - **Couple MIP / MAP** : distinguer mise en position et maintien en position sur des
    assemblages concrets (pignon conique/arbre, roue conique/pignon arbré, pignon arbré/poulie)
    (p.119, p.127).
  - **Liaison complète vs liaison partielle**, liaison complète **démontable**, caractérisation
    d'une liaison par le graphe `c / r / dé / a / di` et ses compléments (p.123, p.127).
  - **Solutions constructives d'encastrement arbre-moyeu** : clavette parallèle + rainures,
    cannelures, épaulement + rondelle d'appui + rondelle frein + écrou à encoches, épaulement +
    rondelle d'appui + écrou et contre écrou (p.123).
  - **Choix argumenté entre deux solutions** par tableau de critères pondérés 0-3 (précision de
    MIP, actions transmissibles, fiabilité, maintenabilité, encombrement, esthétique, coût)
    (p.124).
  - **Guidage en rotation par roulements** : type de roulement, bagues montées serrées, arbre
    tournant / moyeu tournant, arrêts en translation des bagues (4 arrêts dont un de réglage),
    tolérances des portées (m6 / H7), lubrification et étanchéité, montages en « X » et en « O »,
    passage des roulements à billes à contact radial aux roulements à billes à contact oblique
    ou à rouleaux coniques quand les charges axiales deviennent importantes (p.121–122, p.125–126,
    p.128).
  - **Chaîne fonctionnelle du mécanisme de traction** : actigramme A-0, tableau
    fonction technique → processeur/solution constructive (11 fonctions), schéma cinématique
    minimal à compléter (p.117–119).
  - **Compléments de dessin à l'échelle** avec composants normalisés, et reprise du même travail
    sur **modeleur / logiciel 2D**, plus l'exploitation du logiciel **PyVot0.6** (p.122, p.124,
    p.126).
- ⛔ **EXCLU / seulement mentionné dans cette tranche** :
  - Les **calculs de dimensionnement** (durée de vie d'un roulement, charge équivalente, calcul
    de clavette ou de cannelure) : aucun n'est demandé — l'analyse reste qualitative et
    graphique.
  - Les **rapports de transmission / vitesses de sortie** : les nombres de dents (Z5, Z12, Z22,
    Z29, Z37) et les 3000 tr/min sont donnés par la nomenclature, mais **aucune question de la
    tranche ne demande de calculer un rapport ou une vitesse** (la transmission de puissance est
    le thème suivant, p.129-215).
  - Le **moteur de levée / système hydraulique** et la **direction** : cités dans la mise en
    situation (p.113) et présents sur le schéma cinématique (p.119), mais jamais étudiés.
  - Les **assemblages indémontables** (soudage, rivetage, collage, frettage) : la synthèse p.127
    ne détaille que la **liaison complète démontable** et la liaison partielle ; aucun paragraphe
    « liaison complète indémontable » n'est imprimé.
  - Les **autres moyens de guidage en rotation** (paliers lisses, coussinets, douilles à billes) :
    la synthèse p.128 dit « plusieurs moyens de guidage, dont on distingue les roulements » puis
    ne traite que les roulements.
  - Les **valeurs numériques des tolérances** : la figure p.128 laisse « Ø…m6 » et « Ø…H7 » avec
    le diamètre en pointillés ; aucun tableau IT n'est donné dans la tranche.
  - Les **corrigés** : toutes les cases, tableaux, pointillés et cases à cocher des p.117 à 126
    sont **vierges** (manuel d'activités) ; le quiz d'auto-évaluation et la grille d'évaluation
    sont renvoyés à des ressources externes par QR code (EXE, PDF).

#### Thème : TRANSMISSION DE PUISSANCE (p.129–215)

**Page d'ouverture du thème (p.129)** — bandeaux colorés empilés, transcrits fidèlement :

> **AXE 2**
> **ANALYSE STRUCTURELLE ET CONCEPTION**

> **THÈME**
> **TRANSMISSION DE PUISSANCE**

> **SÉQUENCE**
> - Transmission de puissance sans transformation de mouvement.
> - Transmission de puissance avec transformation de mouvement.
> - Machines thérmiques [sic]

> **COMPOSANTES DES COMPÉTENCES DISCIPLINAIRES**
> CD 1.3: Rechercher les constituants d'une chaine de transmission de puissance.
> CD 2.3: Déterminer les caractéristiques d'une transmission.
> CD 1.9: Décrire le principe de fonctionnement des machines thermiques.

**Tableau « Transmission de puissance » (p.129)** — colonnes : CD | Savoirs et savoir-faire |
Critères d'évaluation. (Dans l'imprimé, la cellule « Savoirs » couvre à la fois la ligne CD 1.3 et
la ligne CD 2.3 ; les critères, eux, sont distincts ligne par ligne.)

| CD | Savoirs et savoir-faire | Critères d'évaluation |
| --- | --- | --- |
| CD 1.3 | **Transmission de puissance sans transformation de mouvement:**<br>- Transmission sans modification de vitesse angulaire : accouplements, embrayages, limiteurs de couples et freins.<br>- Transmission avec modification de vitesse angulaire : engrenages, Boite de vitesses.<br>- Trains épicycloïdaux simples | - Détermination correcte des constituants d'une chaine de transmission.<br>- Résolution adéquate d'un problème. |
| CD 2.3 | *(même cellule « Savoirs » que CD 1.3, fusionnée dans l'imprimé)* | - Détermination correcte des caractéristiques d'une chaine de transmission.<br>- Résolution adéquate d'un problème. |
| CD 1.9 | **Transmission de puissance avec transformation de mouvement:**<br>Système vis écrou; excentriques; cames; bielle manivelle; pignon – crémaillère; liens flexibles.<br>**Machines thermiques:**<br>Principe de fonctionnement; composition; caractéristiques. | - Description correcte du fonctionnement d'un moteur 2 et 4 temps.<br>- Détermination correcte des caractéristiques d'une machine thermique. |

Un QR code étiqueté **PDF** figure en bas de la cellule « Critères » de CD 1.9 (p.129).

**Bandeau de tête des pages du thème** : « TRANSMISSION DE PUISSANCE » avec un sous-titre qui
change selon la sous-partie traitée — *Embrayage* (p.130–141), *Frein* (p.142–145), *Boîte de
vitesses* (p.146–150 et p.155–161), *Transformation de mouvement* (p.151–154), *Frein* (p.162).
Les pastilles de compétences **CD 1.3 / CD 2.3 / CD 1.9** sont imprimées en haut à gauche des
pages de travail demandé (p.133, 134, 135, 137, 140, 141, 144, 145, 148, 149, 150, 151, 152, 153,
154, 158, 159, 160, 161, 162) ; elles sont absentes des pages de présentation et de dossier
technique (p.130, 131, 132, 136, 138, 139, 142, 143, 146, 147, 155, 156, 157).

---

##### Activité 1 — Maquette d'embrayage à disque (p.130–135)

- **Système / support d'étude** : maquette d'un **embrayage à disque** (embrayage monodisque à
  ressorts hélicoïdaux, socle + bâti, manivelle d'entraînement, système de commande à pédale).
- **Compétences affichées** : CD 1.3, CD 2.3, CD 1.9 (pastilles imprimées à partir de la p.133).
- **Pictogrammes de compétences transversales (p.133)** : COMM, R. PRO, DECI.
- **Mise en situation (p.130)** :
  « Les figures ci-dessous représentent la maquette d'un embrayage à disque. »
  Deux photos-rendus 3D de la maquette (deux points de vue) : socle gris, deux flasques verts,
  disque transparent avec les ressorts et les leviers, arbres bleus, levier/fourchette gris,
  pédale et ressort de rappel.

  Texte imprimé sous les figures :
  « Ce système est un dispositif d'accouplement temporaire, permettant d'effectuer le changement
  des rapports de la boîte des vitesses. Du fait de sa transmission par adhérence, il offre une
  mise en charge progressive de l'accouplement, ce qui évite les à-coups.
  On distingue deux positions de fonctionnement :
  - **Position embrayée** : l'embrayage transmet intégralement la puissance fournie ;
  - **Position débrayée** : la transmission est interrompue. »

- **Fonctionnement (p.130, § 2)** :
  « L'action sur la pédale (18) entraine la rotation de la fourchette (20) qui pousse la butée
  d'embrayage (14) contre les leviers (32), qui pivotent de manière à faire reculer le plateau de
  pression (27) pour assurer le débrayage. Les ressorts (26) provoquent le retour de la fourchette
  (20) pour assurer l'embrayage. »
  Deux QR codes en bas de page : **Vid** et **PDF**.

- **Ressources fournies** :
  - **Dessin d'ensemble p.131**, cartouche « MAQUETTE D'UN EMBRAYAGE A DISQUE », **Echelle: 3:10**.
    Vue principale en coupe, repères portés : 36, 1, 17, 18, 14, 35, 32, 33, 34, 26, 38, 22 (en
    haut) ; 29, 10, 6 (à gauche) ; 13, 21, 19, 15, 30, 28, 31, 25, 27, 23 (en bas) ; une flèche
    indique « **Colle** » sur l'arbre moteur côté droit. Deux zones de détail repérées par les
    lettres **F** et **E**.
    Sous-dessin « **Système de commande** » : repères 9, 2, 18, 12, 14, 20, 16, 19, 21, 3, 8, 11,
    4, 5, 7 et zone de détail **G**.
    « **Détail E — Echelle: 3:5** » : repères 35, 27, 37, 24, 25.
    « **Détail G — Echelle: 3:5** » : repères 21, 7, 4.
    Un QR code **PDF**.
    ⚠️ Aucune cote chiffrée n'est portée sur ce dessin : les diamètres demandés en p.135 doivent
    être **relevés à la règle puis convertis par l'échelle 3:10**.
  - **Nomenclature p.132** (38 repères, deux demi-tableaux côte à côte) :

| Rep. | Nbr. | Désignation | Rep. | Nbr. | Désignation |
| --- | --- | --- | --- | --- | --- |
| 1 | 1 | Palier arbre récepteur | 20 | 1 | Fourchette |
| 2 | 2 | Vis à tête bombée M6 - 40 | 21 | 1 | Levier de fourche |
| 3 | 1 | Tige de poussée | 22 | 1 | Arbre moteur |
| 4 | 2 | Butée de réglage de garde | 23 | 1 | Manivelle |
| 5 | 1 | Ressort de rappel | 24 | 1 | Volant moteur |
| 6 | 1 | Chape | 25 | 1 | Disque d'embrayage |
| 7 | 1 | Rotule | 26 | 16 | Ressort de pression |
| 8 | 1 | Écrou hexagonal ISO 4034 - M6 | 27 | 1 | Plateau de pression |
| 9 | 2 | Écrou fin hexagonal ISO 4035 - M6 | 28 | 4 | Griffe |
| 10 | 1 | Vis à tête bombée M4 - 25 | 29 | 1 | Arbre primaire de la BDV |
| 11 | 1 | Écrou fin hexagonal ISO 4035 - M4 | 30 | 1 | Couvercle |
| 12 | 1 | Support butée | 31 | 8 | Vis à tête bombée M4 -10 |
| 13 | 1 | Semelle | 32 | 4 | Levier de débrayage |
| 14 | 2 | Bague de la butée | 33 | 4 | Axe d'écartement |
| 15 | 6 | Bille | 34 | 4 | Vis à tête bombée M6- 20 |
| 16 | 1 | Cage de la butée | 35 | 4 | Écrou Hm M10 |
| 17 | 1 | Douille de la butée | 36 | 2 | Coussinet |
| 18 | 1 | Pédale d'embrayage | 37 | 2 | Garniture |
| 19 | 1 | Axe de la fourchette | 38 | 1 | Palier arbre moteur |

  - **Deux perspectives 3D p.132** : « Système de commande » (repères 18, 12, 16, 14, 20, 19, 21,
    3, 6, 4, 5, 7, 8) et « Détail E » (repères 28, 33, 35, 16, 14, 15, 30, 24, 31, 27, 25, 26).
  - **Détail F p.134** (vue en coupe agrandie de la butée) : repères 17, 1, 14, 15.

- **Données numériques de l'énoncé (p.135, § C)** :
  - Couple transmissible maximum : **Ct = 3,2 Nm**
  - Effort presseur développé par **un** ressort : **Fr = 3,5 N**
  - Nombre de ressorts de pression (26) : **16** (donné par la nomenclature p.132)
  - Diamètres des surfaces de contact du disque avec les plateaux : **D = ........ mm ;
    d = ............ mm** (Relever les dimensions du dessin d'ensemble) — *le dessin d'ensemble
    de la maquette est p.131, échelle 3:10 ; la p.135 ne le précise pas.*
  - Table des matériaux candidats pour la garniture (37) :

| Matériau | Coefficient de frottement " f " |
| --- | --- |
| Matériau 1 | 0,4 |
| Matériau 2 | 0,35 |
| Matériau 3 | 0,3 |

- **Encadrés officiels (verbatim)** :

  > **I. Situation déclenchante** (p.133)
  > Le système d'embrayage comprend l'ensemble des pièces situées entre le moteur et la boite de
  > vitesses. Sa fonction est de permettre ou rompre la transmission de mouvement de rotation
  > entre le moteur et la boite.
  > **Comment analyser et interpréter cette fonction ?**

- **Formule du couple transmissible (p.135)** — imprimée en ligne de texte courant, hors
  de tout encadré, entre les données et la question a. :

  > Ct = (2/3) . n . f . N . (R³ - r³) / (R² - r²)

  *(imprimée avec la fraction 2/3 empilée et le quotient (R³ - r³)/(R² - r²) empilé. Le
  manuel n'imprime aucune légende des symboles : n, f et N sont identifiables par les
  questions a., b. et c. de la même page ; **R et r ne sont définis nulle part sur la p.135**
  — l'énoncé n'y donne que les diamètres D et d, à relever sur le dessin d'ensemble.)*

- **Travail demandé — II. Travail demandé (p.133–135)** :

  **A. Analyse fonctionnelle (p.133–134)**
  1. (p.133) « Tourner la manivelle (23) (pédale appuyée puis relâchée), observer le fonctionnement
     dans les deux cas et compléter le tableau ci-dessous (cocher la bonne réponse). »
     Tableau à cocher (cases vides) :

     | | Arbre d'entrée (23) — En rotation | Arbre d'entrée (23) — Au repos | Arbre de sortie (29) — En rotation | Arbre de sortie (29) — Au repos |
     | --- | --- | --- | --- | --- |
     | Pédale appuyée | | | | |
     | Pédale relâchée | | | | |

     Puis : « En déduire la fonction du mécanisme : …………… » (deux lignes de pointillés).
  2. (p.133) « Compléter la vue éclatée de la maquette d'embrayage par : Volant moteur – Disque
     embrayage – Support – Dispositif de commande. »
     Vue éclatée 3D de la maquette avec **4 cadres vides** à renseigner (dispositif de commande en
     haut à gauche, volant + disque à droite, disque d'embrayage sur son arbre en bas à gauche,
     support/bâti au centre).
  3. (p.134) « En se référant au mécanisme réel et à son dessin d'ensemble, compléter le
     cheminement de mouvement ci-dessous : »
     Chaîne imprimée : **Manivelle (23)** → ▭ → ▭ → ▭ → **Arbre de sortie (29)**
     (3 cases vides, chacune avec deux lignes de pointillés).
  4. (p.134) « Quelles sont les pièces qui créent l'effort presseur pendant l'embrayage? »
  5. (p.134) « Quel est le type de l'embrayage (instantané ou progressif) ? »
  6. (p.134) « Préciser le type de surface de friction de l'embrayage (Plane, conique, cylindrique) »
  7. (p.134) « Pour chacune des positions suivantes, compléter par : (Embrayée ou Débrayée) »
     Deux schémas cinématiques normalisés d'embrayage (bâti hachuré, arbre d'entrée à gauche,
     disque + ressorts, leviers, butée et commande à droite) diffèrent par la position de la butée
     et des leviers ; sous chacun : « Position ........................... ».

  **B. Étude de l'embrayage (p.134–135)**
  1. (p.134) « Appuyer sur la pédale (18) et observer le fonctionnement du dispositif de commande. »
     - a. « De quel type de commande s'agit-il ? »
     - b. « Colorier sur le dessin ci-contre la butée à billes. » *(dessin = Détail F, repères 17,
       1, 14, 15)*
     - c. (p.135) « En se référant au dessin d'ensemble et au mécanisme réel, compléter par les
       pièces principales le cheminement de commande ci-dessous. »
       Chaîne imprimée : **Pédale (18)** → ▭ → ▭ → ▭ → ▭ → **Plateau (27) + (28)**
       (4 cases vides) ; une flèche montante annotée **(10)** pointe sur la liaison
       Pédale (18) → 1ʳᵉ case, et une flèche montante annotée **(32)** pointe sur la liaison
       4ᵉ case → Plateau (27) + (28).
     - d. (p.135) « Donner le nombre et le rôle des ressorts (26) :
       - Nombre : ............ ;
       - Rôle : ………… »

  **C. Caractéristiques de l'embrayage (p.135)**
  Énoncé : « Choix du matériau de la garniture (37) ; Sachant que : … » *(données ci-dessus)*.
  - a. « A partir de la maquette d'embrayage relever le nombre de surfaces de friction.
    n = ................. »
  - b. « Calculer l'effort presseur N développé par les ressorts (26). »
  - c. « Calculer le coefficient de frottement "f ". »
  - d. « Choisir le type de matériau qui convient pour la garniture (37) afin de produire ce couple
    d'embrayage, justifier votre réponse. » *(tableau des 3 matériaux ci-dessus)*

- **Vocabulaire & terminologie officielle** : accouplement temporaire, transmission par adhérence,
  mise en charge progressive, à-coups, position embrayée / débrayée, effort presseur, surface de
  friction (plane / conique / cylindrique), embrayage instantané / progressif, butée à billes,
  fourchette, levier de débrayage, plateau de pression, disque d'embrayage, volant moteur,
  garniture, griffe, arbre primaire de la BDV, garde (butée de réglage de garde), coefficient de
  frottement, couple transmissible.

---

##### Activité 2 — Tour parallèle (p.136–154)

**Présentation du support d'activité (p.136)**

- **Système / support d'étude** : **tour parallèle** (machine-outil réelle de l'atelier ; la boîte
  de vitesses étudiée en 2.4 est celle d'un tour **« PINACHO »**).
- **Texte de présentation, verbatim (p.136)** :
  « Le tour parallèle est une machine-outil universelle servant à usiner des pièces mécaniques.
  Elle est essentiellement constituée :
  - D'un moteur électrique ;
  - D'une boîte des avances ;
  - D'une boîte de vitesses;
  - D'un système de maintien de la pièce ;
  - D'un traînard équipé par des chariots assurant le mouvement de l'outil ;
  - D'une poupée mobile pour le travail entre pointe et les opérations de perçage et d'alésage ;
  - D'une poupée fixe ;
  - D'un dispositif de transmission de mouvement de la boîte des avances au traînard;
  - D'un dispositif de freinage ;
  - D'un mécanisme de transmission des avances des chariots ;… »
- **Figure (p.136)** : schéma d'ensemble (vue de face) du tour, entièrement légendé. Étiquettes
  imprimées : *Poupée fixe, Mandrin, Tourelle, Chariot porte-outil, Chariot transversal, Poupée
  mobile, Boîte de vitesses, Boîte des avances, Courroie, Banc (glissière), Moteur électrique,
  Dispositif de freinage, Pédale de frein, Embrayage, Traînard, Mécanisme de l'avance.*
  Quatre zones sont cerclées en pointillés rouges (boîte de vitesses, embrayage/traînard,
  mécanisme d'avance, dispositif de freinage/moteur).

###### Activité 2.1 (p.137)

*(Aucun sous-titre n'est imprimé sous la pastille « Activité 2.1 » — voir § Incertitudes. Le
sommaire p.5 la désigne « Transmission de mouvement ». Bandeau de tête : « Embrayage ».)*

- **Compétences affichées** : CD 1.3, CD 2.3, CD 1.9. Pictogrammes : COMM, R. PRO, DECI.
- **Encadré officiel (verbatim)** :

  > **I. Situation déclenchante**
  > On veut réaliser l'embout d'un vérin à partir d'une barre d'aluminium de Ø30, pour cela nous
  > devrons utiliser le tour afin d'obtenir les diamètres demandés.
  > **Faisons les opérations d'usinage afin d'identifier les mouvements possibles des différents
  > organes de la machine.**

- **Consigne permanente (p.137, en rouge, avec pictogramme triangulaire « Sécurité »)** :
  « Vérifier les consignes de sécurité à respecter relativement à cette activité. »
  *(Cette même ligne est réimprimée en tête du « Travail demandé » des activités 2.2 p.140,
  2.3 p.144, 2.4 p.148, 2.5 p.151 et 3 p.158.)*
- **Données numériques de l'énoncé** : barre brute d'aluminium **Ø30**, **L = 42 mm** ; opération
  de chariotage à **Ø28**. Dessin 3D de la pièce à obtenir, coté : **Ø28**, **Ø24**, **20**, **40**
  (mm). QR code **Vid**.
- **Travail demandé (II)** :
  1. **Préparation de la machine pour une opération d'usinage**
     - a. « Monter la pièce brute de Ø30 et L=42mm. »
     - b. « Monter l'outil couteau et l'outil coudé. »
     - c. « Mettre la machine en marche en présence de l'enseignant. »
     - d. « Réaliser une opération de dressage, et chariotage Ø28. »
  2. **Les mouvements possibles sur le tour//**
     - a. « Sur un tour // le mouvement de coupe est donné à : (Cocher la ou (les) bonne(s)
       réponse(s)). » — cases à cocher : *La pièce ☐   l'outil ☐   le porte-outil ☐   le
       porte-pièce (mandrin) ☐*
     - b. « Sur un tour le mouvement d'avance est donné à : (Cocher la ou (les) bonne(s)
       réponse(s)). » — mêmes quatre cases : *La pièce ☐   l'outil ☐   le porte-outil ☐   le
       porte-pièce (mandrin) ☐*
  3. **Sécurité du tour**
     - a. « Citer deux risques majeurs que l'on peut encourir sur cette machine. »
     - b. « Citer deux dispositifs de sécurité sur cette machine. »
- **Vocabulaire & terminologie officielle** : dressage, chariotage, outil couteau, outil coudé,
  mouvement de coupe, mouvement d'avance, porte-pièce (mandrin), porte-outil, tour //.

###### Activité 2.2 — Dispositif d'embrayage du tour (p.138–141)

- **Système / support d'étude** : embrayage à disque du **tablier / boîte des avances** du tour
  parallèle, sur la barre de chariotage (embrayage limiteur de couple à friction).
- **Compétences affichées** : CD 1.3, CD 2.3, CD 1.9 (p.140–141). Pictogrammes (p.140) : COOP,
  R. PRO.
- **Ressources fournies** :
  - **Vue 3D en 1/4 de coupe (p.138)**, légendée : *Bâti, Barre de chariotage, Roulement à
    aiguilles, Butée, Butée à aiguilles, Arbre de sortie*. Repère de ressource : **QR49**, QR code
    **Vid**.
  - **Nomenclature p.138** (18 repères) :

| Rep. | Nbr. | Désignation | Matière | Observation |
| --- | --- | --- | --- | --- |
| 1 | 1 | Bâti | EN-GJL-200 | |
| 2 | 1 | Roulement à aiguilles | | |
| 3 | 1 | Arbre de sortie | C 40 | |
| 4 | 1 | Joint | | |
| 5 | 1 | Guide gauche de ressort | | |
| 6 | 1 | Ressort | | |
| 7 | 1 | Guide droit de ressort | | |
| 8 | 1 | Butée à aiguilles | | |
| 9 | 1 | Anneau élastique | | |
| 10 | 1 | Capot | EN-GJL-200 | |
| 11 | 1 | Ergot | | |
| 12 | 1 | Vis mère | C 40 | |
| 13 | 1 | Flasque | | |
| 14 | 1 | Plaquette de frottement | | |
| 15 | 1 | Barre de chariotage | | |
| 16 | 1 | Goupille | | |
| 17 | 1 | Manchon | | |
| 18 | 3 | Vis à tête fraisée fendue M5-20 | | |

  - **Dessin d'ensemble p.139**, cartouche « **TOUR PARALLELE — Embrayage** », **Echelle: 1:2**.
    Vue en coupe portant les repères 1 à 18 ; une flèche horizontale **F** indique le sens de
    l'effort presseur sur l'arbre de sortie. Sous la coupe : « **Vue suivant F (3 et 13) — Echelle
    reduit** [sic] » (vue circulaire montrant 4 vis réparties sur un cercle et le moletage), et
    deux vues de ressort en élévation repérées **D** et **C** (deux longueurs de ressort
    différentes, cotées symboliquement D et C).
    ⚠️ Aucune cote chiffrée n'est portée : les rayons R et r demandés en p.141 doivent être
    **relevés à la règle puis convertis par l'échelle 1:2**.
  - **Perspective éclatée de l'embrayage (p.140)** : toutes les pièces alignées, avec des lignes
    de repère **vides** que l'élève doit renseigner.
- **Encadré officiel (verbatim)** :

  > **I. Situation déclenchante** (p.140)
  > L'avance du traînard peut se réaliser à volonté via la position de la butée liée à la barre de
  > chariotage.
  > **Faisons l'étude du mécanisme de la transmission de mouvement de la boîte des avances au
  > traînard.**

- **Données numériques de l'énoncé (p.141, question i)** :
  - f : coefficient de frottement **f = 0,45**
  - n : nombre des surfaces de contact *(à relever)*
  - N : effort normal **N = 150 N**
  - R et r : rayons de la surface de contact (couronne), à relever sur le dessin d'ensemble p.139
- **Travail demandé (II, p.140–141)** :
  1. **Préparation de la machine pour une opération d'usinage** — « En présence de l'enseignant: »
     - a. « Régler la position de la butée de la barre de chariotage. »
     - b. « Mettre la machine en marche. »
     - c. « Faire le déplacement automatique du traînard. »
     - d. « Que se passe t-il si le traînard touche la butée (s'arrête / en mouvement) »
       - « Le traînard :……………………………….…… »
       - « La barre de chariotage :……………………….. »
       - « L'arbre d'entrée (3) :…………………………… »
  2. **Étude du mouvement de la barre de chariotage** — « En se référant au dessin d'ensemble
     partiel page 139 et sa nomenclature. »
     - a. « Inscrire sur la perspective éclatée de l'embrayage les repères des pièces. »
     - b. « Compléter le cheminement de transmission de puissance ci-dessous de l'arbre (3) à la
       barre de chariotage (15). »
       Chaîne imprimée en bulles : **(3)** → **(…)** → **(…)** → **(…)** → **(15)** ; sous chacune
       des 4 flèches, une flèche montante annotée respectivement **(18)**, **......**, **Adh**,
       **......**
     - c. (p.141) « La transmission de cet embrayage est assurée par (cocher la bonne réponse) :
       Obstacle ☐        Adhérence ☐ »
     - d. « Quel est le rôle du moletage réalisé sur le flasque (13) ? »
     - e. « Quel est le type de cet embrayage (cocher la bonne réponse) ?
       Progressif ☐        Instantanée ☐ » [sic : « Instantanée » accordé au féminin]
     - f. « Par quoi est assuré l'effort presseur ? »
     - g. « Quel est le type de commande de cet embrayage ? »
     - h. « L'embrayage est conçu de façon qu'on puisse régler le couple à transmettre, expliquer
       brièvement comment peut-on faire ce réglage. »
     - i. « **Calcul du couple transmissible** — Calculer le couple transmissible Ct sachant que
       l'embrayage transmet un couple de la boîte des avances à la barre de chariotage (15).
       On donne : … » *(données ci-dessus)*
       Trois cadres de réponse imprimés en bas de page : **R = .......................**,
       **r = .......................**, **C\_t = .......................**
       *(La formule à employer est celle encadrée p.135 ; elle n'est pas réimprimée ici.)*
- **Vocabulaire & terminologie officielle** : barre de chariotage, vis mère, traînard, butée de
  barre de chariotage, moletage, flasque, plaquette de frottement, butée à aiguilles, roulement à
  aiguilles, anneau élastique, ergot, manchon, transmission par obstacle / par adhérence,
  limiteur de couple (réglage du couple à transmettre), effort normal, surfaces de contact.

###### Activité 2.3 — Dispositif de freinage du tour (p.142–145)

- **Système / support d'étude** : **frein à sabot** (frein de secours) du tour parallèle, agissant
  sur la poulie motrice du moteur, commandé par pédale.
- **Compétences affichées** : CD 1.3, CD 2.3, CD 1.9 (p.144–145). Pictogrammes (p.144) : COOP,
  R. PRO. Bandeau de tête : « Frein ».
- **Ressources fournies** :
  - **Mécanisme en 3D (p.142)** : rendu vert du groupe moteur basculant sur son support, poulie
    motrice, sabot articulé, tige filetée, levier de commande et pédale. QR code **Vid**.
  - **Nomenclature p.142** (18 repères) :

| Rep. | Nbr. | Désignation | Matière | Observation |
| --- | --- | --- | --- | --- |
| 1 | 1 | Vis à tête cylindrique à six pans creux ISO 4762 | | |
| 2 | 1 | Cloche | | |
| 3 | 1 | Bague | S 235 | |
| 4 | 1 | Sabot | | |
| 5 | 1 | Douille | | |
| 6 | 1 | Garniture | Férodo | |
| 7 | 1 | Poulie motrice | | |
| 8 | 1 | Arbre moteur | | |
| 9 | 1 | Clavette parallèle | C 60 | |
| 10 | 1 | Rondelle plate | | |
| 11 | 1 | Vis à tête hexagonale ISO 4014-M8 | | |
| 12 | 1 | Levier de commande | S 275 | |
| 13 | 1 | Rondelle plate | | |
| 14 | 1 | Vis à tête hexagonale ISO 4014-M8 | | |
| 15 | 1 | Axe | | |
| 16 | 1 | Tige filetée | | |
| 17 | 1 | Pédale | | |
| 18 | 1 | Support moteur | | |

  - **Dessin d'ensemble p.143**, cartouche « **TOUR PARALLELE — Dispositif de freinage** »,
    **Echelle: 1:3**. Vue de face : repères *Courroie*, 6, 7, 2, 18, 4, 12, 16, 17 ; le plan de
    coupe **A-A** est repéré par deux flèches A.
    Coupe « **A-A (Echelle :1:1)** » : repères 3, 1, 2 (en haut à gauche), 4, 5, 6, 7, 8, 9, 10, 11
    (en bas à gauche), 12, 13, 14, 15 (en bas à droite).
  - **Épure cinématique cotée (p.145)** : dessin à l'échelle du mécanisme de freinage montrant la
    poulie, le *Sabot (4)* en **1ère position** (noir) et en **2ème position du sabot** (rouge), le
    *Levier de commande (12)*, la *Tige filetée (16)*, la *Pédale (17)*, les points **A**, **B**,
    **C**, **C'**, **D**, **E** et la vitesse angulaire **ω(17/18)** figurée par une flèche courbe.
- **Encadré officiel (verbatim)** :

  > **I. Situation déclenchante** (p.144)
  > L'arrêt du tour se fait par l'action d'un levier ou bouton d'arrêt d'urgence. Le tour est
  > équipé d'un « frein de secours », qui sert à garantir l'immobilisation du moteur à l'arrêt par
  > l'action d'une pédale.
  > **Réalisons l'étude de ce dispositif de freinage.**

- **Données numériques de l'énoncé (p.144, § 2)** :
  - Vitesse angulaire de la pédale : **ω(17/18) = 5 rd/s**
  - **ED = 90 mm** et **BC = 95 mm**
  - Échelle de tracé du vecteur vitesse (p.145) : **1 mm → 0,01 m/s**
  - Définition des points (tableau imprimé p.144) :

| | |
| --- | --- |
| • A: centre de la liaison pivot (4) – (18) | • D: centre de la liaison pivot (16) – (17) |
| • B: centre de la liaison pivot (12) – (18) | • E: centre de la liaison pivot (17) – (18) |
| • C: centre de la liaison pivot (16) – (12) | • ED = 90mm et BC = 95mm |

- **Travail demandé (II, p.144–145)** :
  1. **Étude du dispositif de freinage (p.144)** — « On désire étudier le dispositif de freinage du
     tour parallèle. En présence de l'enseignant: »
     - a. « Mettre la machine en marche en actionnant le bouton ou le levier de mise en marche puis
       l'arrêter avec le même bouton ou levier. Le mandrin est arrêté (cocher la bonne réponse).
       Lentement ☐        Immédiatement ☐ »
     - b. « Redémarrer la machine puis appuyer fortement sur la pédale de freinage. Le mandrin est
       arrêté (cocher la bonne réponse). Lentement ☐        Immédiatement ☐ »
     - c. « En se référant au dessin d'ensemble du dispositif de freinage du tour parallèle
       page 143. Donner le type de frein et sa commande. »
  2. **Étude cinématique du frein (p.144–145)** — énoncé verbatim :
     « Admettant que le frein à sabot fonctionne de la façon suivante (voir page 145) :
     L'opérateur exerce sur la pédale (17) une force provoquant sa rotation autour de E dans le
     sens indiqué par la flèche avec une vitesse angulaire ω(17/18) = 5 rd/s.
     La pédale agit sur le tirant (16) qui actionne le levier (12) pour le faire tourner autour de
     B. Ce levier entraîne la rotation du sabot (4) autour de A provoquant le freinage de la
     poulie (7). »
     - a. « Tracer et repérer la trajectoire TD(17/18) du point D(17/18) ; »
     - b. « Tracer et repérer la trajectoire TC(12/18) du point C(16/18) ; » [sic : indices
       hétérogènes — trajectoire indicée (12/18) pour un point indicé (16/18)]
     - c. « Calculer en m/s la vitesse instantanée V(D17/18) du point D(17/18). »
     - d. « Tracer et repérer le vecteur vitesse instantanée V(D17/18); Échelle 1mm→0,01m/s »
     - e. « Calculer la vitesse angulaire ω(12/18). »
     - f. « Déterminer graphiquement D' ( la deuxième position du point D) ; »
     - g. « Mesurer l'angle de rotation α(DED') de la pédale. »
- **Vocabulaire & terminologie officielle** : frein à sabot, frein de secours, garniture (Férodo),
  cloche, poulie motrice, tirant, tige filetée, levier de commande, liaison pivot, trajectoire,
  vitesse instantanée, vitesse angulaire (rd/s), échelle de vecteur vitesse, angle de rotation.

###### Activité 2.4 — Boîte de vitesses du tour (p.146–150)

- **Système / support d'étude** : **boîte de vitesses du tour « PINACHO »** (poulie d'entrée
  étagée + trains de baladeurs jusqu'à la broche).
- **Compétences affichées** : CD 1.3, CD 2.3, CD 1.9 (p.148–150). Pictogramme (p.148) : R. PRO.
- **Ressources fournies** :
  - **Dessin d'ensemble p.146**, cartouche « **TOUR "PINACHO" — Boîte de vitesses** »,
    **Echelle : 1:3**. Coupe longitudinale portant les repères 24, 32, 33, 4, 1, 2, 3, 6, 27, 7,
    28 (haut et droite) ; 34, 35, 20, 5, 8, 13, 14, 21, 22, 30, 31, 16 (gauche) ; 29, 9, 10, 23
    (droite) ; 17, 18, 19, 15, 11, 26, 12, 25 (bas). Deux QR codes **PDF**.
  - **Nomenclature p.147** (35 repères) :

| Rep. | Nbr. | Désignation | Matière | Observation |
| --- | --- | --- | --- | --- |
| 1 | 1 | Arbre | C40 | |
| 2 | 1 | Couronne dentée | C60 | |
| 3 | 1 | Baladeur | C40 | |
| 4 | 1 | Roue dentée | C60 | |
| 5 | 1 | Roue dentée | C60 | |
| 6 | 1 | Roue dentée | C60 | |
| 7 | 1 | Pignon arbré | C60 | |
| 8 | 1 | Baladeur | C60 | |
| 9 | 1 | Roue dentée | C60 | |
| 10 | 1 | Axe | C30 | |
| 11 | 1 | Roue dentée | C60 | |
| 12 | 1 | Roue dentée | C60 | |
| 13 | 1 | Pignon | C60 | |
| 14 | 1 | Axe | C30 | |
| 15 | 1 | Roue dentée | C60 | |
| 16 | 1 | Axe | C30 | |
| 17 | 1 | Axe | C30 | |
| 18 | 1 | Pignon | C60 | |
| 19 | 1 | Roue dentée | C60 | |
| 20 | 1 | Boitier | S235 | |
| 21 | 1 | Écrou spécial | S235 | |
| 22 | 1 | Broche | C40 | |
| 23 | 1 | Couvercle | S235 | |
| 24 | 1 | Poulie | Zamak3 | |
| 25 | 1 | Bague | S235 | |
| 26 | 1 | Bague | S235 | |
| 27 | 1 | Hélice | EN-AW 1050 | |
| 28 | 1 | Corps | EN-GJL 250 | |
| 29 | 1 | Boitier | S235 | |
| 30 | 1 | Couvercle | S235 | |
| 31 | 1 | Couvercle | S235 | |
| 32 | 1 | Clavette parallèle | C 60 | |
| 33 | 2 | Roulement à aiguilles | | |
| 34 | 1 | Rondelle | | |
| 35 | 1 | Écrou hexagonal M12 | | |

  - **Schéma cinématique de la boîte pour une vitesse préréglée (p.149)** : quatre lignes d'arbres
    étagées, avec **Poulie (24)** en entrée, l'arbre **1**, l'arbre **7**, l'arbre **10**, le
    **Bâti** et la **Broche (22)** en sortie. Roues repérées **Z₁, Z₂, Z₃** (baladeur de l'arbre 1),
    **Z₄, Z₅, Z₆**, **Z₇**, **Z₈, Z₉, Z₁₀**, **Z₁₁, Z₁₂**, **Z₁₃** et **Z₁₈**.
- **Encadré officiel (verbatim)** :

  > **I. Situation déclenchante** (p.148)
  > Pour pouvoir usiner des pièces de différents matériaux et des dimensions variées, ces tours
  > sont équipés d'une boîte de vitesses permettant la rotation du mandrin porte pièces à
  > différentes vitesses.
  > **Faisons l'étude de la boîte de vitesses du tour parallèle.**

- **Données numériques de l'énoncé** :
  - (p.148) chariotage d'une pièce en aluminium de **Ø24** avec un **outil à charioter en (A.R.S)** ;
    vitesse de coupe **Vc = 60 m/min**.
  - (p.149) vitesse de rotation du moteur en charge : **Nm = 1435 tr/min** ;
    rapport de transmission par poulie courroie : **r = 0,475**.
  - (p.149) nombre de dents des roues :

| Roues (Z\_i) | Z₁ | Z₂ | Z₃ | Z₄ | Z₅ | Z₆ | Z₇ | Z₈ | Z₉ | Z₁₀ | Z₁₁ | Z₁₂ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Nombre de dents | 32 | 37 | 25 | 24 | 19 | 31 | 14 | 25 | 42 | 19 | 34 | 57 |

  - (p.150) Puissance du moteur **Pm = 2,95 KW** ; rendement du système poulies-courroies
    **η = 0,8** ; rendement de la boite de vitesse **η = 0,9**.
- **Travail demandé (II, p.148–150)** :
  1. **Préparation de la machine pour une opération d'usinage (p.148)** — « Calcul de la vitesse de
     rotation (ou vitesse de rotation du mandrin) pour le chariotage d'une pièce en aluminium de
     Ø24 avec un outil à charioter en (A.R.S). »
     - a. « Donner la formule : N = ……………… » *(formule à écrire par l'élève ; non imprimée)*
     - b. « On donne : Vc = 60m/min — Calculer la vitesse de rotation N. »
       Cadre de réponse : **N\_calculée = ......................... tr/min**
     - c. « Choisir sur le tour la vitesse la plus proche. »
       Cadre de réponse : **N\_choisie = ......................... tr/min**
     - d. « Comment fait-on pour régler la vitesse de rotation du tour? »
     - e. « Qu'appelle t-on l'organe permettant la modification de vitesses? »
     - f. « Identifier le nombre de vitesses possibles de l'arbre broche. »
     - g. « Pouvons-nous réaliser le réglage de la vitesse si la machine est en marche? justifier : »
  2. **Étude cinématique (p.149–150)** — « La figure ci-dessous représente le schéma de la boîte de
     vitesses pour une vitesse préréglée. »
     - a. (p.150) « Calculer la vitesse de rotation de l'arbre (1). »
     - b. (p.150) « Compléter le tableau suivant en identifiant les couples des roues engrenées qui
       assurent l'entraînement de l'arbre broche (22), le rapport de transmission et la vitesse de
       rotation de la broche. »
       Tableau à 9 lignes, toutes vides :

       | Position | Couples des roues engrenées | Rapport de transmission r\_i | Vitesse de rotation N\_i |
       | --- | --- | --- | --- |
       | 1 | | | |
       | 2 | | | |
       | 3 | | | |
       | 4 | | | |
       | 5 | | | |
       | 6 | | | |
       | 7 | | | |
       | 8 | | | |
       | 9 | | | |

     - c. (p.150) « On donne : • Puissance du moteur Pm = 2,95 KW. • Rendement du système
       poulies-courroies : η = 0,8. • Rendement de la boite de vitesse est η = 0,9. »
       - « Calculer la puissance reçue par la broche. »
       - « Déterminer la valeur du couple maximal appliqué à la broche. »
- **Vocabulaire & terminologie officielle** : broche, mandrin porte pièces, baladeur, pignon arbré,
  couronne dentée, poulie courroie, vitesse de coupe Vc, vitesse de rotation N, A.R.S (acier rapide
  supérieur), rapport de transmission, rendement, puissance, couple maximal, boîtier, corps, hélice.

###### Activité 2.5 — Dispositif d'avance automatique du tour (p.151–154)

- **Système / support d'étude** : mécanisme d'avance (manuelle puis automatique) des chariots du
  tour parallèle — traînard, chariot transversal, chariot porte-outil.
- **Compétences affichées** : CD 1.3, CD 2.3, CD 1.9. Pictogrammes (p.151) : COMM, R. PRO.
  Bandeau de tête : « Transformation de mouvement ».
- **Encadré officiel (verbatim)** :

  > **I. Situation déclenchante** (p.151)
  > Le travail de tournage dépend non seulement de la vitesse de coupe (vitesse de rotation) mais
  > aussi de la vitesse d'avance. L'avance peut se réaliser manuellement ou automatiquement via la
  > barre de chariotage.
  > **Faisons l'étude du mécanisme de commande de l'avance.**

- **Ressources fournies** :
  - **Photo du tablier / traînard (p.151)** avec trois cadres d'étiquettes vides reliés par des
    flèches rouges aux trois manivelles.
  - **Schéma cinématique 3D des chariots (p.152)**, légendé *Outil, Roue dentée, crémaillère,
    Banc*, avec le trièdre **x, y, z**. QR code **PDF**.
  - **Deux schémas cinématiques 3D de l'avance automatique (p.153)** :
    – à gauche (avance longitudinale) : *Crémaillère, Chariot longitudinal, Barre de chariotage,
    Roue, Vis sans fin*, roues **Z₄, Z₂, Z₃, Z₁** ;
    – à droite (avance transversale) : *Vis de commande, Chariot transversal, Barre de chariotage,
    Roue, Vis sans fin*, roues **Z₅, Z₂, Z₁**.
- **Données numériques de l'énoncé (p.153–154)** :
  - Système vis-écrou de pas : **P = 5 mm**
  - Rapport de transmission roue et vis sans fin : **r = 1/40**
  - Nombre de dents des roues :

| Roues (Zi) | Z1 | Z2 | Z3 | Z4 | Z5 |
| --- | --- | --- | --- | --- | --- |
| Nombre de dents | 32 | 16 | 18 | 9 | 10 |

  - Vitesse de rotation de la barre de chariotage : **Nb = 210 trs/min** (question d) et
    **Nbmax = 210 trs/min** (question h).
- **Travail demandé (II, p.151–154)** :
  1. (p.151) « Sur la figure ci-dessous mettre en place les étiquettes suivantes:
     - Manivelle du traînard;
     - Manivelle du chariot transversal;
     - Manivelle du chariot porte outil. »
  2. (p.151) « Compléter le tableau ci-dessous en identifiant les graduations des tambours gradués
     des différents chariots du tour.
     - a. Mettre les tambours à 0.
     - b. Tourner les trois manivelles de un tour en mesurant le déplacement de chaque chariot avec
       un réglet.
     - c. Compter le nombre de divisions du tambour gradué.
     - d. Calculer la valeur du déplacement pour une division.
     - e. Calculer la valeur de la première graduation chiffrée. »
     Tableau (toutes cellules vides) :

     | Nom du chariot | Déplacement en mm pour 1 tour | Nombre de divisions du tambour gradué | Valeur pour une division | Valeur de la 1ère graduation chiffrée |
     | --- | --- | --- | --- | --- |
     | Traînard | | | | |
     | chariot transversal | | | | |
     | chariot porte outil | | | | |

  3. (p.152) **Etude de la commande manuelle des chariots**
     - a. « Colorier par différentes couleurs sur le schéma cinématique 3D ci-dessous les éléments
       de commande manuelle pour les mouvements relatifs suivants :
       - du chariot longitudinal par rapport au banc ;
       - du chariot transversal par rapport au chariot longitudinal ;
       - du chariot porte outil par rapport au chariot transversal ;
       - de la tourelle par rapport au chariot porte outil. »
     - b. « Compléter le tableau suivant : » (toutes cellules vides)

       | Nom du chariot | Mouvement d'entrée | Mouvement de sortie | Organe menant | Dispositif de transformation de mouvement |
       | --- | --- | --- | --- | --- |
       | Traînard | | | | |
       | chariot transversal | | | | |
       | chariot porte outil | | | | |

  4. (p.153–154) **Étude de la commande automatique des chariots.**
     Texte verbatim (p.153) : « En cas d'avance automatique, le mouvement de rotation de la barre
     de chariotage se transforme en avance longitudinale ou transversale du chariot porte-outil,
     par l'intermédiaire des engrenages situés dans le tablier. »
     - a. (p.153) « Compléter le graphe de la chaîne cinématique pour la position du levier de
       commande provoquant l'avance du chariot longitudinal. »
       Graphe imprimé : **Barre de chariotage** → ▭ → ▭ → ▭ ; puis (2ᵉ rangée, sens droite→gauche)
       ▭ → ▭ → **▭ / Crémaillère** → **Chariot longitudinal**.
     - b. (p.154) « Donner l'expression littérale de la vitesse de rotation de la manivelle de
       traînard Nz en fonction de la vitesse de rotation de la barre de chariotage Nb. »
     - c. (p.154) « Donner l'expression littérale de la vitesse d'avance du traînard Vz en fonction
       de la vitesse de rotation de la barre de chariotage Nb. »
     - d. (p.154) « Pour une vitesse Nb = 210 trs/min, calculer la vitesse d'avance Vz. »
     - e. (p.154) « Compléter le graphe de la chaîne cinématique pour la position du levier de
       commande provoquant l'avance du chariot transversal. »
       Graphe imprimé : **Barre de chariotage** → ▭ → ▭ → **Roue (Z₁)** ; puis (2ᵉ rangée, sens
       droite→gauche) ▭ → ▭ → ▭ → **Chariot transversal + écrou**.
     - f. (p.154) « Donner l'expression littérale de la vitesse de rotation de la vis de commande
       du chariot transversal Nx en fonction de la vitesse de rotation de la barre de chariotage
       Nb. »
     - g. (p.154) « Donner l'expression littérale de la vitesse d'avance du chariot transversal Vx
       en fonction de la vitesse de rotation de la barre de chariotage Nb. »
     - h. (p.154) « Calculer la vitesse d'avance Vx maximale (Nbmax = 210 trs/min). »
- **Vocabulaire & terminologie officielle** : traînard (chariot longitudinal), chariot transversal,
  chariot porte-outil, tourelle, banc, tablier, tambour gradué, graduation chiffrée, réglet,
  manivelle, barre de chariotage, système vis-écrou, pas P, roue et vis sans fin, pignon–crémaillère,
  organe menant, dispositif de transformation de mouvement, vitesse d'avance, avance longitudinale /
  transversale.

---

##### Activité 3 — Maquette de boîte de vitesses (p.155–162 ; la tranche s'arrête à la fin de la p.162)

- **Système / support d'étude** : **maquette d'une boîte de vitesses d'automobile à commande
  manuelle** (5 vitesses + marche arrière, 3 arbres) **et d'un frein à tambour de stationnement**
  accompagné de son levier.
- **Compétences affichées** : CD 1.3, CD 2.3, CD 1.9 (p.158–162). Pictogrammes (p.158) : COOP,
  R. PRO, CRITI. Bandeau de tête : « Boîte de vitesses » (p.155–161), « Frein » (p.162).
- **Avertissement de manipulation, verbatim (p.155)** :
  « La maquette de la boite de vitesses est fragile. Sa manipulation doit être à tour de rôle par
  les apprenants en présence obligatoire de l'enseignant. »
- **Mise en situation (p.155)** :
  « Chaîne de transmission de puissance d'un automobile à 2 roues motrices arrières : »
  Schéma-bloc imprimé (avec une photo sous chaque bloc — moteur, embrayage, boîte de vitesses,
  pont) :
  **Energie chimique** → **Transformer l'énergie** → *P, Nm* → **Transmettre ou non la puissance**
  → *P, Nm* → **Adapter le couple et la vitesse** → *P', N'* → **Répartir la vitesse sur les deux
  roues motrices arrières** → sorties **C₁.ω₁** et **C₂.ω₂**. QR code **PDF**.

  Puis : « Les figures ci-dessous représentent la maquette d'une boîte de vitesses à commande
  manuelle d'un automobile et d'un frein accompagné de son levier. La sélection des vitesses
  s'effectue à l'aide des fourchettes commandées par un levier de changement de vitesses. »
  **Fig.1** : photo de la maquette, repères 1 à 8. **Fig.2** : vue 3D éclatée-écorchée, légendée
  *Dispositif de commande, Arbre de sortie, Arbre d'entrée, Arbre intermédiaire*.
  Légende imprimée sous les figures :

| | |
| --- | --- |
| (1) : Levier de frein | (5) : Levier de changement de vitesse |
| (2) : Arbre d'entrée | (6) : Guide ressort |
| (3) : Secteur denté | (7) : Couvercle |
| (4) : Tige | (8) : Tringle |

- **Ressources fournies** :
  - **Dessin d'ensemble p.156**, cartouche « **Maquette de boîte de vitesses** », **Echelle: 1:2**
    (dessin imprimé tourné à 90°). Coupe portant les repères 1 à 38. En bas à droite, un croquis
    d'implantation des axes montrant les cercles primitifs **Z₃₁**, **Z₃₂** et **Z₃₃+Z₃₄** (train
    de marche arrière). QR code **PDF**.
  - **Nomenclature p.157** (38 repères ; les dentures sont données directement dans la
    désignation) :

| Rep. | Nbr. | Désignation | Rep. | Nbr. | Désignation |
| --- | --- | --- | --- | --- | --- |
| 1 | 1 | Arbre d'entrée | 20 | 1 | Ressort |
| 2 | 2 | Couvercle | 21 | 1 | Levier |
| 3 | 4 | Anneau élastique | 22 | 3 | Coulisseau |
| 4 | 4 | Roulement type BC | 23 | 1 | Fourchette |
| 5 | 1 | Pignon ; Z= 20 dents | 24 | 1 | Baladeur |
| 6 | 1 | Roue dentée ; Z= 43 dents | 25 | 1 | Coulisseau |
| 7 | 1 | Coussinet | 26 | 1 | Roue dentée ; Z= 38 dents |
| 8 | 4 | Flasque | 27 | 1 | Pignon ; Z= 20 dents |
| 9 | 12 | Tige | 28 | 3 | Tige |
| 10 | 1 | Coulisseau | 29 | 1 | Fourchette |
| 11 | 1 | Fourchette | 30 | 1 | Baladeur |
| 12 | 1 | Baladeur | 31 | 1 | Roue dentée ;Z= 45 dents |
| 13 | 1 | Pignon ; Z= 26 dents | 32 | 1 | Pignon ; Z= 15 dents |
| 14 | 1 | Roue dentée ; Z= 37 dents | 33 | 1 | Pignon ; Z= 22 dents |
| 15 | 1 | Bague | 34 | 1 | Pignon ; Z= 22 dents |
| 16 | 1 | Roue dentée ; Z= 31 dents | 35 | 1 | Arbre intermédiaire |
| 17 | 1 | Pignon ; Z= 27 dents | 36 | 1 | Arbre sortie |
| 18 | 1 | Couvercle | 37 | 2 | Flasque extérieur |
| 19 | 1 | Rotule | 38 | 1 | Couvercle |

  - **Schéma cinématique p.157** : arbre d'entrée (1) en haut, arbre intermédiaire au milieu, arbre
    de sortie (36) à droite. Repères portés sur le schéma : 5, 12, 13, 16, 24, 26, 30, 31 (rangée
    supérieure) et 6, 14, 17, 27, 32, 33, 34 (rangée inférieure) ; annotations des positions de
    baladeurs **V-IV**, **III-II**, **I-MA**.
  - **Fig.3 (p.161)** : vue 3D éclatée du **frein de stationnement à tambour**, légendée *Levier,
    Tirant, Biellette, Tige réglable, Bras, Came, Tambour, Machoires* [sic : sans cédille].
  - **Fig.4 (p.162)** : coupe circulaire du frein à tambour (deux mâchoires + ressort), avec
    **4 lignes de repère vides** à compléter et une seule étiquette imprimée : **Garniture**.
- **Encadré officiel (verbatim)** :

  > **I. Situation déclenchante** (p.158)
  > La boîte de vitesses, est un système mécanique de transmission de puissance, qui permet
  > d'engendrer différents rapports de vitesses du moteur aux roues motrices d'un véhicule.
  > La boîte est constituée de plusieurs éléments permettant le changement des différents rapports
  > de vitesses.
  > **Faisons une analyse de fonctionnement de cette boîte, pour identifier ses constituants.**

- **Données numériques de l'énoncé** :
  - Dentures : voir la nomenclature p.157 (Z₅=20, Z₆=43, Z₁₃=26, Z₁₄=37, Z₁₆=31, Z₁₇=27, Z₂₆=38,
    Z₂₇=20, Z₃₁=45, Z₃₂=15, Z₃₃=22, Z₃₄=22 dents).
  - (p.160) Points de lecture du graphique **N'₃₆ = f (N'₁)** : 1ᵉʳᵉ vitesse **N'₁ = 8** ;
    2ᵉᵐᵉ vitesse **N'₁ = 2,5** et **N'₃₆ = 0,64** ; 3ᵉᵐᵉ vitesse **N'₁ = 3,5** ;
    4ᵉᵐᵉ vitesse **N'₁ = 2** ; 5ᵉᵐᵉ vitesse **N'₁ = 1**.
  - (p.161) Vitesse de rotation du moteur : **Nm = 3000 tr/min**.
- **Travail demandé (II, p.158–162)** :

  **A. Analyse fonctionnelle (p.158–159)**
  1. (p.158) « Compléter l'actigramme A-0 ci-dessous : »
     Cadre **A-0** imprimé, portant en dessous la mention **Boite de vitesses** ; entrées, sorties,
     données de contrôle et fonction sont **toutes en pointillés** (à renseigner).
  2. (p.158) « En se référant à la maquette de la boîte de vitesses compléter le tableau de
     liaisons suivant : »

     | Liaison | Nom de la liaison |
     | --- | --- |
     | Levier (21) + (19) / Carter (38) + (18) + (20) | *(à compléter)* |
     | Roue dentée (31) / Arbre de sortie (36) | *(à compléter)* |
     | Arbre intermédiaire (35) / Flasques extérieurs (37) | *(à compléter)* |
     | Pignon (5) / Roue dentée (6) | *(à compléter)* |

  3. (p.158–159) « En observant la maquette de boîte de vitesses, Indiquer par une croix le(s)
     type(s) d'engrenage(s) utilisé(s) pour transmettre la puissance de l'arbre d'entrée (1) vers
     l'arbre de sortie (36). »
     Tableau de 4 colonnes, chacune illustrée d'une photo et suivie d'une case à cocher :
     **Engrenage conique | Engrenage hélicoïdal | Engrenage intérieur à denture droite | Engrenage
     extérieur à denture droite**.
  4. (p.159) « Pour les types d'engrenages identifiés dans la question précédente, indiquer dans le
     tableau suivant la ou les conditions d'engrènement. »
     Tableau : ligne de tête « **Nature de la denture** » couvrant deux colonnes
     « Denture ............. » et « Denture ............. » ; ligne « **Conditions d'engrènement** »
     avec trois lignes de pointillés dans chaque colonne.
  5. (p.159) « Compléter le tableau suivant en indiquant la solution technologique assurant chaque
     fonction. »

     | Fonction | Solution |
     | --- | --- |
     | Guider en rotation l'arbre (35) | *(à compléter)* |
     | Guider en translation la roue dentée (31) | *(à compléter)* |
     | Déplacer le baladeur (30) | *(à compléter)* |
     | Guider en translation le coulisseau (22) | *(à compléter)* |

  **B. Etude des caractéristiques de la transmission (p.159–161)**
  1. (p.159) « Dans quelle position peut-on avoir un rapport de transmission nul ? »
     Cases imprimées : **Point mort** [....]   **Marche Avant** [....]   **Marche Arrière** [....]
  2. (p.159) « Manœuvrer le levier de commande (21) et déduire le nombre de vitesses possibles »
  3. (p.159) « Expliquer pour quelle raison le constructeur a choisi des dentures droites pour la
     roue (34) de la marche arrière. »
  4. (p.159) « Justifier la présence des roues (33) et (34). »
  5. (p.159–160) « Pour chaque position du levier (21), compléter le tableau ci-dessous en
     identifiant les couples des roues engrenées qui assurent l'entraînement de l'arbre de sortie
     (36) et calculer le rapport de transmission correspondant. »

     | Position | Couples des roues dentées | Rapport de transmission « r » |
     | --- | --- | --- |
     | M. Arrière | (Z5 ,Z6) ;(Z32 ,Z33) ;(Z34,Z31) | *(à compléter)* |
     | 1 | *(à compléter)* | *(à compléter)* |
     | 2 | *(à compléter)* | *(à compléter)* |
     | 3 | *(à compléter)* | *(à compléter)* |
     | 4 | *(à compléter)* | *(à compléter)* |
     | 5 | *(à compléter)* | *(à compléter)* |

     *(Seule la ligne « M. Arrière » est pré-remplie ; elle sert de modèle. Les indices Z\_i y
     désignent les repères de nomenclature p.157.)*
  6. (p.160) « On donne la courbe du nombre de tours : N'36 = f (N'1) »
     Graphique imprimé : ordonnée **N'₃₆ (Nombre de tours de l'arbre de sortie)** graduée de 0,1 à
     2 par pas de 0,1 ; abscisse **N'₁ (Nombre de tours de l'arbre d'entrée)** graduée
     0 ; 0,5 ; 1 ; 1,5 ; 2 ; 2,5 ; 3 ; 3,5 ; 4 ; 4,5 ; 5 ; 5,5 ; 6 ; **6,6** [sic — la graduation
     régulière attendue serait 6,5] ; 7 ; 7,5 ; 8 ; 8,5 ; 9 ; 9,5 ; 10.
     Quatre droites passant par l'origine, étiquetées **5ème vitesse** (rouge, la plus raide),
     **4ème vitesse** (jaune), **3ème vitesse** (bleu foncé) et **1ère vitesse** (magenta, la moins
     raide). La courbe de la 2ᵉᵐᵉ vitesse est **absente** : c'est l'objet de la question b.
     - a. « A partir du graphique (voir page précédente), compléter le tableau suivant : »

       | | Nombre de tours de l'arbre d'entrée | Nombre de tours de l'arbre de sortie | Rapport de transmission |
       | --- | --- | --- | --- |
       | 1ère Vitesse | 8 | *(à compléter)* | *(à compléter)* |
       | 2ème Vitesse | 2,5 | 0,64 | *(à compléter)* |
       | 3ème Vitesse | 3,5 | *(à compléter)* | *(à compléter)* |
       | 4ème Vitesse | 2 | *(à compléter)* | *(à compléter)* |
       | 5ème Vitesse | 1 | *(à compléter)* | *(à compléter)* |

     - b. « En se référant au tableau ci-dessus, tracer sur le même graphique la courbe de nombres
       de tours correspondant à la 2ème vitesse. »
     - c. « Comparer les résultats des rapports des vitesses trouvés par la méthode graphique à ceux
       obtenus par la méthode analytique (voir question 5.). »
  7. (p.161) « En se référant à la maquette de la boîte de vitesses et au schéma cinématique du
     dossier technique, placer ci-dessous les baladeurs (12) et (24) pour obtenir la 3ème position
     du levier de commande (21). »
     Schéma cinématique identique à celui de la p.157, mais **les deux baladeurs (12) et (24) sont
     dessinés à l'écart, hors ligne d'arbre** (étiquetés « Baladeur 12 » et « Baladeur 24 »), et
     leurs emplacements sur les arbres sont laissés en **traits mixtes fins** ; repères présents sur
     le schéma : 5, 13, 16, 26, 30, 31, 33, 34, 6, 14, 17, 27, 32 ; annotations **V-IV**,
     **III-II**, **I-MA** ; **Arbre d'entrée (1)** et **Arbre de sortie (36)**.
  8. (p.161) « Pour quelle raison les roues (16) et (17) sont à dentures hélicoïdales ? »
  9. (p.161) « Par quoi est assurée l'obtention de la 3ème vitesse : (Crabotage / Adhérence) »
  10. (p.161) « Calculer la vitesse de rotation de l'arbre de sortie (36) pour cette position des
      baladeurs de la question 7. (On donne Nm = 3000tr/min). »

  **C. Etude du frein de stationnement (p.161–162)**
  *(La section s'ouvre p.161 sur la Fig.3 ; le questionnaire est imprimé p.162.)*
  1. (p.162) « Compléter le graphe des éléments qui participent au freinage. »
     Graphe imprimé : **Levier** → ▭ → ▭ → ▭ ; puis (2ᵉ rangée, sens droite→gauche)
     **Bras** → ▭ → ▭ → **Tambour**.
  2. (p.162) « Donner le nom du frein utilisé. »
  3. (p.162) « Identifier le type de commande de ce frein. »
  4. (p.162) « Identifier le mode d'action (radiale ou axiale ?). »
  5. (p.162) « En vous aidant de la maquette, compléter la désignation des pièces sur la (fig.4). »
  6. (p.162) « Donner le rôle du ressort. (Voir fig.4) »
  7. (p.162) « En manipulant le frein de la maquette, compléter (en mettant une croix) le tableau
     ci-dessous. »

     | Levier du frein à main | Tambour — Tourne | Tambour — Fixe |
     | --- | --- | --- |
     | Non actionné | | |
     | Actionné | | |

  8. (p.162) « En se référant à la (fig.3) ; Compléter, au crayon et au instruments [sic], la
     représentation du dispositif de freinage dans la position freinée. »
     Deux dessins circulaires imprimés côte à côte : **« Position : Libre »** (tambour + deux
     mâchoires + ressort déjà tracés) et **« Position: Freinée »** (tambour seul, l'intérieur est à
     compléter par l'élève).
- **Vocabulaire & terminologie officielle** : actigramme A-0, baladeur, fourchette, coulisseau,
  tringle, secteur denté, guide ressort, rotule, flasque extérieur, arbre d'entrée / intermédiaire /
  de sortie, carter, point mort, marche avant, marche arrière (M. Arrière), rapport de transmission
  nul, engrenage conique / hélicoïdal / intérieur à denture droite / extérieur à denture droite,
  conditions d'engrènement, nature de la denture, crabotage, adhérence, roue de renvoi (roues 33 et
  34), frein de stationnement, frein à tambour, mâchoires, came, bras, biellette, tige réglable,
  tirant, garniture, mode d'action radial / axial, méthode graphique / méthode analytique.

##### Bornes de scope observées — p.129–162

- ✅ **INCLUS** dans cette tranche, traité explicitement et intégralement :
  - **Embrayage à disque** : constitution (dessin d'ensemble + nomenclature 38 rep.), positions
    embrayée/débrayée, transmission par adhérence, mise en charge progressive, effort presseur,
    types de surface de friction, chaîne de commande, et le **calcul du couple transmissible
    Ct = (2/3)·n·f·N·(R³−r³)/(R²−r²)** avec choix de matériau de garniture par le coefficient de
    frottement (p.130–135).
  - **Embrayage limiteur de couple du tour** (barre de chariotage) : transmission par obstacle vs
    adhérence, embrayage progressif/instantané, moletage, réglage du couple à transmettre, calcul
    de Ct avec f = 0,45 et N = 150 N (p.138–141).
  - **Frein à sabot** : constitution, type de frein et sa commande, et une **étude cinématique
    graphique complète** (trajectoires, vitesse instantanée en m/s, vecteur vitesse à l'échelle
    1 mm → 0,01 m/s, vitesse angulaire par changement de solide, deuxième position, angle de
    rotation) — p.142–145.
  - **Boîte de vitesses du tour** : vitesse de coupe → vitesse de rotation (Vc = 60 m/min, Ø24),
    schéma cinématique à 12 roues, rapport de transmission par poulie-courroie, tableau des
    **9 positions** de baladeurs, chaîne de rendements (η poulies-courroies 0,8 × η BdV 0,9) et
    couple maximal à la broche (p.146–150).
  - **Transformation de mouvement** : commande manuelle et automatique des chariots, tambours
    gradués, **système vis-écrou (P = 5 mm)**, **roue et vis sans fin (r = 1/40)**,
    **pignon–crémaillère**, expressions littérales Nz(Nb), Vz(Nb), Nx(Nb), Vx(Nb) et applications
    numériques à Nb = 210 tr/min (p.151–154).
  - **Boîte de vitesses d'automobile (maquette)** : chaîne de transmission de puissance d'un
    véhicule 2 roues motrices arrières, actigramme A-0, tableau de liaisons, **typologie des
    engrenages et conditions d'engrènement**, solutions technologiques de guidage, rapports de
    transmission des 5 vitesses + marche arrière, exploitation d'un **graphique N'₃₆ = f(N'₁)** et
    confrontation graphique/analytique, positionnement des baladeurs, crabotage (p.155–161).
  - **Frein de stationnement à tambour** : graphe des éléments, nom du frein, type de commande,
    mode d'action radial/axial, rôle du ressort, comportement du tambour levier actionné/non
    actionné, tracé de la position freinée (p.161–162).
- ⛔ **EXCLU / seulement annoncé** à ce stade de la tranche :
  - **Machines thermiques** (CD 1.9) : annoncées dans la séquence et le tableau de compétences
    p.129, non traitées **dans ces pages** — le thème les traite plus loin, à l'activité 5.1
    « Machine thermique » (p.187–191).
  - **Trains épicycloïdaux simples** : annoncés p.129 (savoirs de CD 1.3/CD 2.3), non traités
    **dans ces pages** — le thème les traite plus loin, à l'activité 6.2 « Train épicycloïdal »
    (p.208–210) et dans la synthèse (p.211–215).
  - **Excentriques, cames, bielle-manivelle, liens flexibles** : annoncés p.129 comme
    transformations de mouvement ; la tranche ne traite explicitement que **vis-écrou** et
    **pignon–crémaillère** (p.151–154).
  - **Accouplements** et **limiteurs de couples** en tant que tels : cités p.129 ; seul
    l'embrayage-limiteur du tour (p.138–141) les approche.
  - **Formule de la vitesse de rotation N = f(Vc, D)** (p.148, question a) : **non imprimée** — le
    manuel demande à l'élève de la donner.
  - **Tableau des vitesses disponibles sur le tour** (p.148, question c « choisir sur le tour la
    vitesse la plus proche ») : **non imprimé** — la lecture se fait sur la machine réelle.
  - **Aucun corrigé, aucune synthèse encadrée de fin d'activité** dans cette tranche : le manuel
    est un *manuel d'activités* à trous ; il n'y a ni « Je retiens », ni « Retenir », ni
    « Rappel ». La seule règle générale énoncée dans la tranche est la formule de Ct (p.135), imprimée hors encadré ; les autres
    encadrés sont les **Situations déclenchantes** (p.133, 137, 140, 144, 148, 151, 158).
  - **Renvois hors tranche** : les QR codes (Vid / PDF, dont **QR49** p.138) pointent vers des
    ressources vidéo et PDF externes, non transcriptibles ici.
  - **Suite de l'Activité 3** : la p.162 se termine sur la question 8 du § C. L'**Activité 3**
    s'achève là ; la p.163 ouvre l'**Activité 4** (fraiseuse universelle).

##### Activité 4 — Fraiseuse universelle (p.163–180)

L'activité 4 se déroule en trois volets successifs, chacun avec sa propre présentation
(mise en situation + dessin d'ensemble + nomenclature) puis son travail demandé :
**4.1 Frein électromagnétique** (p.163–167), **4.2 Boîte de vitesses** (p.168–175),
**4.3 Transformation de mouvement — Vis écrou** (p.176–180).

---

###### Activité 4 — Présentation du support d'activité : Frein (p.163–165)

- **Système / support d'étude** : fraiseuse universelle « Milko-12 » ; zone d'étude = le frein
  électromagnétique en bout d'arbre moteur.
- **Compétences affichées** : aucune pastille CD sur p.163–165 (le bandeau ne porte que
  « TRANSMISSION DE PUISSANCE / Frein »).
- **Mise en situation (p.163, verbatim)** :

  > La fraiseuse est une machine-outil permettant de réaliser différentes opérations
  > d'usinage, la majorité de ces machines sont équipées de freins pour différentes
  > raisons :
  > - Pour de très courtes opérations il permet de gagner du temps au changement de
  >   pièce en minimisant le temps d'arrêt de l'outil.
  > - Dans le cas d'un accident (cassure de l'outil, de la pièce ou en cas de blessure) où
  >   l'arrêt immédiat de la broche de la machine sera indispensable.

- **Ressources fournies** :
  - p.163 : photographie de la fraiseuse universelle « Milko-12 », avec encart « Zone d'étude »
    agrandissant le frein. Éléments annotés sur l'encart : **Plateau mobile**, **Moteur**,
    **Disque frein**, **Bobine**. QR-code étiqueté **Vid** (vidéo).
  - p.164 : **dessin d'ensemble** en coupe du frein électromagnétique, repères 1 à 23.
    Cartouche : « Fraiseuse universelle — Frein électromagnétique », **Échelle 1:2**,
    symbole de projection européenne (cône + cercles).
  - p.165 : **nomenclature** complète (23 repères).

- **Nomenclature du frein électromagnétique (p.165)** :

| Rep. | Nbr. | Désignation | Matière | Observation |
| --- | --- | --- | --- | --- |
| 1 | 1 | Cage du ventilateur | S235 | |
| 2 | 1 | Ventilateur | PVC | |
| 3 | 3 | Écrou hexagonal ISO 4032 - M10 | | Standard |
| 4 | 1 | Armature de bobine | | |
| 5 | 3 | Écrou bas hexagonal ISO 4035 - M10 | | Standard |
| 6 | 3 | Écrou hexagonal autofreiné ISO 7040 - M10 | | Standard |
| 7 | 3 | Ressort | 51Cr V4 | |
| 8 | 3 | Goujon M10 | | Standard |
| 9 | 1 | Moyeu | C35 | |
| 10 | 1 | Flasque | | |
| 11 | 2 | Roulement rigide à billes | | |
| 12 | 1 | Stator | Al Si13 | |
| 13 | 1 | Bague entretoise | | |
| 14 | 2 | Garniture | | |
| 15 | 4 | Vis à tête cylindrique à six pans creux M8 | | Standard |
| 16 | 1 | Disque de frein | | |
| 17 | 1 | Plateau mobile | | |
| 18 | 1 | Clavette parallèle | | |
| 19 | 1 | Anneau élastique | | Standard |
| 20 | 1 | Câble d'alimentation | | |
| 21 | 1 | Arbre moteur | C40 | bout strié |
| 22 | 1 | Bobine | | |
| 23 | 1 | Bague de serrage | 51Cr V4 | |

- **Vocabulaire & terminologie officielle** : frein électromagnétique, disque de frein, plateau
  mobile, armature de bobine, bobine, stator, flasque, moyeu, garniture, bague entretoise,
  bague de serrage, goujon, écrou autofreiné, écrou bas, cage du ventilateur, broche.

---

###### Activité 4.1 — Frein (p.166–167)

- **Système / support d'étude** : frein électromagnétique de la fraiseuse universelle « Milko-12 »
  (dessin d'ensemble p.164, nomenclature p.165).
- **Compétences affichées** : p.166 sans pastille (picto **R. PRO**) ; p.167 **CD 2.2 / CD 3.8**.
- **Encadré « I. Situation déclenchante » (p.166, verbatim)** :

  > L'utilisation prolongée de la machine, exige un contrôle préventif visant les pannes
  > inopinées.
  >
  > **Dans notre cas l'organe ciblé pour cette vérification est le frein électromagnétique.**

- **Consignes de sécurité (p.166, verbatim)** — bloc rouge, accompagné des pictogrammes
  « Sécurité » (triangle rouge) et « Danger Electrique » :

  > **Consignes de sécurité**
  > Durant le déroulement de l'activité :
  > - Dans un premier temps la fraiseuse ne doit pas être sous tension
  > - Effectuer les manipulations avec des grandes précautions et en présence de votre professeur.

- **Ressources fournies** : dessin d'ensemble p.164 et sa nomenclature p.165 ; schéma cinématique
  partiel à compléter (p.166, en bas à droite) ; expression du couple de freinage donnée (p.167).
- **Données numériques de l'énoncé** : coefficient de frottement **f = 0,4** ; couple de freinage
  visé **Cf = 18 Nm** ; nombre de surfaces de frottement **n** et rayons **r**, **R** (en mm) à
  relever sur le dessin ; classe d'équivalence donnée
  **A = { 1, 3, 4, 5, 6, 8, 10, 13, 15, BE11, 12, 22, 20 }**.

- **Travail demandé (II. Travail demandé — p.166–167)** :
  1. Enlever avec précaution la cage du ventilateur (1), (Bien ranger les vis de fixation)
  2. Mettre sous tension la machine.
  3. Mettre en marche la machine avec le bouton d'essai (prendre une distance suffisante par
     rapport au moteur)
  4. En se référant au dessin d'ensemble et sa nomenclature, identifier la nature du mouvement
     des différentes pièces par rapport au bâti de la machine en mettant une croix dans la case
     correspondante. — Tableau à quatre colonnes **Pièce / Tournante / Glissante / Fixe**, lignes :

     | Pièce | Tournante | Glissante | Fixe |
     | --- | --- | --- | --- |
     | Disque de frein (16) | … | … | … |
     | Plateau mobile (17) | … | … | … |
     | Armature de bobine (4) | … | … | … |
     | Bride moteur (10) | … | … | … |

  5. Compléter les blocs cinématiques qui constituent le frein ainsi que le schéma cinématique
     (symboles normalisés et repères des classes d'équivalences).
     A = { 1, 3, 4, 5, 6, 8, 10, 13, 15, BE₁₁, 12, 22, 20 }
     B = { …………………………………………………… }
     C = { …………………………………………………… }
     D = { …………………………………………………… }
     *(Figure à droite : ébauche de schéma cinématique — un axe horizontal rouge, deux liaisons
     hachurées vertes, deux symboles de liaison encadrés d'une croix, un symbole de ressort en
     bas ; la classe **A** est fléchée, trois autres flèches partent de pointillés à renseigner.)*
  6. Quelle est le type de commande du frein ?
  7. Suite à l'état du dessin d'ensemble.
     a. Indiquer si la bobine (21) est excitée ou non, justifier votre réponse.
     b. Déduire dans ce cas si la fraiseuse est freinée ou libre.
  8. On donne l'expression du couple de freinage
     **Cf = (2/3) · Fp · f · n · (R³ − r³) / (R² − r²)** et le coefficient de frottement **f = 0,4**.
     a. Déduire du dessin d'ensemble le nombre de surfaces de frottement « n » et relever les
        rayons correspondants « r » et « R ».
        n = ………… ,  r = ………… mm ,  R = ………… mm
     b. Calculer l'effort presseur Fp fourni par les ressorts (7), permettant un couple de
        freinage **Cf = 18 Nm**.
     c. Déduire l'effort de chaque ressort.
  9. Donner le rôle des écrous hexagonaux autofreinés (6).

- **Formule imprimée dans l'énoncé de la question 8 (p.167, verbatim — non encadrée)** :

  > Cf = 2/3 · F<sub>p</sub> · f · n · (R³ - r³) / (R² - r²)

- **Vocabulaire & terminologie officielle** : couple de freinage, effort presseur, surfaces de
  frottement, coefficient de frottement, classes d'équivalence, blocs cinématiques, schéma
  cinématique, symboles normalisés, bâti, type de commande, bobine excitée, freinée / libre.

---

###### Activité 4.2 — Présentation du support d'activité : Boîte de vitesses (p.168–171)

- **Système / support d'étude** : boîte de vitesses de la fraiseuse universelle (photo p.168 :
  fraiseuse « Milko-14 », zone d'étude cadrée en rouge sur la colonne de la machine).
- **Compétences affichées** : aucune pastille CD sur p.168–171.
- **Mise en situation (p.168, verbatim)** :

  > Le principe de base de l'usinage est l'enlèvement de matière. Il est obtenu par la coupe du
  > matériau constituant la pièce.
  > En usinage, la vitesse de coupe dépend de la matière usinée, du type d'opération, de l'outil,
  > de l'état de surface souhaité, etc. C'est pour cette raison que la machine-outil est équipée
  > d'un mécanisme permettant le réglage de la vitesse de la broche après avoir choisi la vitesse
  > de coupe convenable. Dans notre cas on va s'intéresser à ce mécanisme qui est la boite de
  > vitesses de la fraiseuse universelle.

- **Ressources fournies** :
  - p.169 : **dessin d'ensemble** de la boîte de vitesses, deux vues en coupe superposées,
    repères 1 à 50. Cartouche : « Fraiseuse universelle — Boîte de vitesses »,
    **Echelle 1:4** [sic — « Echelle » sans accent], symbole de projection européenne.
    QR-code **PDF**. Note portée sur le dessin : « Nb: Les commandes des baladeurs sont
    ramennées [sic] dans le même plan ».
  - p.170–171 : **nomenclature** (repères 1 à 51, la ligne 51 étant volontairement laissée vide
    pour la pièce ajoutée à la question 5.b p.175).

- **Nomenclature de la boîte de vitesses (p.170–171)** :

| Rep. | Nbr. | Désignation | Matière | Observation |
| --- | --- | --- | --- | --- |
| 1 | 1 | Moteur électrique | | |
| 2 | 4 | Vis à tête hexagonale ISO 4014 - M10 | | Standard |
| 3 | 4 | Rondelle M10 | | Standard |
| 4 | 1 | Bâti | EN-GJL-200 | |
| 5 | 1 | Arbre moteur | C40 | |
| 6 | 1 | Pignon-baladeur | 20 Ni Cr Mo 2 | Z6 = 16 dents |
| 7 | 1 | Pignon | 20 Ni Cr Mo 2 | Z7 = 24 dents |
| 8 | 1 | Pignon | 20 Ni Cr Mo 2 | Z8 = 21 dents |
| 9 | 1 | Clavette parallèle | | Standard |
| 10 | 3 | Roulement rigide à billes | | Standard |
| 11 | 5 | Anneau élastique | | Standard |
| 12 | 3 | Bouchon | | Standard |
| 13 | 1 | Roue dentée | 20 Ni Cr Mo 2 | Z13 = 37 dents |
| 14 | 1 | Pignon | 20 Ni Cr Mo 2 | Z14 = 19 dents |
| 15 | 1 | Arbre intermédiaire | | |
| 16 | 1 | Roue dentée | 20 Ni Cr Mo 2 | Z16 = 34 dents |
| 17 | 1 | Roue dentée | 20 Ni Cr Mo 2 | Z17 = 42 dents |
| 18 | 1 | Roue dentée | 20 Ni Cr Mo 2 | Z18 = 56 dents |
| 19 | 1 | Pignon | 20 Ni Cr Mo 2 | Z19 = 17 dents |
| 20 | 1 | Pignon-baladeur | 20 Ni Cr Mo 2 | Z20 = 34 dents |
| 21 | 1 | Arbre intermédiaire cannelé | C40 | |
| 22 | 1 | Clavette parallèle | | Standard |
| 23 | 1 | Roue dentée | 20 Ni Cr Mo 2 | Z23 = 49 dents |
| 24 | 1 | Couvercle | EN-GJL-200 | |
| 25 | 1 | Roulement à rouleaux coniques | | Standard |
| 26 | 1 | Broche | C40 | Traité |
| 27 | 1 | Porte outil conique | C35 | Traité |
| 28 | 2 | Vis à tête cylindrique à six pans creux M6 | | Standard |
| 29 | 2 | Tenon | | |
| 30 | 3 | Vis à tête cylindrique à six pans creux M8 | | Standard |
| 31 | 1 | Roue dentée | 20 Ni Cr Mo 2 | Z31 = 73 dents |
| 32 | 1 | Clavette parallèle | | Standard |
| 33 | 1 | Pignon | 20 Ni Cr Mo 2 | Z33 = 34 dents |
| 34 | 1 | Écrou à encoches auto-freiné | | Standard |
| 35 | 2 | Roulement rigide à billes avec segment d'arrêt | | Standard |
| 36 | 1 | Roulement à rouleaux coniques | | Standard |
| 37 | 1 | Écrou à encoches auto-freiné | | Standard |
| 38 | 1 | Tirant de serrage | | |
| 39 | 1 | Couvercle | EN-GJL-200 | |
| 40 | 1 | Cale de réglage | | |
| 41 | 3 | Fourchette | | |
| 42 | 3 | Goupille élastique | | Standard |
| 43 | 2 | Axe | | |
| 44 | 3 | Plaque | | |
| 45 | 3 | Ressort | 51 Cr V 4 | |
| 46 | 3 | Bille | | |
| 47 | 3 | Barillet | | |
| 48 | 3 | Poignée | | |
| 49 | 1 | Joint plat | | |
| 50 | 1 | Bouchon | | Standard |
| 51 | … | ……………………………. | | |

- **Vocabulaire & terminologie officielle** : boîte de vitesses, pignon-baladeur, baladeur,
  arbre intermédiaire cannelé, broche, porte-outil conique, fourchette, barillet, tirant de
  serrage, cale de réglage, roulement à rouleaux coniques, écrou à encoches auto-freiné,
  vitesse de coupe, enlèvement de matière.

---

###### Activité 4.2 — Travail demandé : Boîte de vitesses (p.172–175)

- **Système / support d'étude** : boîte de vitesses de la fraiseuse universelle
  (dessin d'ensemble p.169, nomenclature p.170–171).
- **Compétences affichées** : **CD 2.2 / CD 3.8** (p.172, 173, 174, 175). Pictos p.172 :
  **COOP**, **DECI**, **CRITI**.
- **Encadré « I. Situation déclenchante » (p.172, verbatim)** :

  > Pour pouvoir usiner des pièces de différents matériaux avec des outils variés, les fraiseuses
  > sont équipées d'une boîte de vitesses permettant la rotation de la broche à différentes
  > vitesses.
  >
  > **Faisons l'étude de la boîte de vitesses de la fraiseuse.**

- **Ressources fournies** : machine réelle au laboratoire, plaque signalétique du moteur,
  tachymètre, plaque des vitesses de la machine (photo p.172), schéma cinématique de la boîte
  (p.173), dessin d'ensemble + nomenclature (p.169–171), figure partielle du barillet (p.175),
  grille de graphe de montage (p.175).

- **Données numériques de l'énoncé** :
  - Plaque des vitesses photographiée p.172 (12 vitesses lisibles, deux colonnes par ligne,
    sélection par un repère de couleur ■ / □, un levier **A / B** et un levier **1 / 2 / 3**) :

    | Position | Colonne gauche | Colonne droite |
    | --- | --- | --- |
    | A / 1 | 50 | 128 |
    | A / 2 | 240 | 92 |
    | A / 3 | 68 | 180 |
    | B / 1 | 910 | 352 |
    | B / 2 | 653 | 1700 |
    | B / 3 | 1280 | 490 |

  - Exemple de codage donné p.172 : « **Faiseuse** [sic] Milko : (■ / B / 1) → 352 ou
    (□ / A / 3) → 180 ».
  - Engrenage pignon (7) / roue (16) : **module m = 3 mm**, **entraxe a = 87 mm**,
    **rapport r = 12/17**.
  - **Rendement de la boîte de vitesses Ŋ = 0,8** [sic — glyphe imprimé à la place de η].
  - Puissance moteur **Pm** et fréquence de rotation **Nm** : à relever sur la plaque
    signalétique (cases vides dans le manuel).

- **Travail demandé (II. Travail demandé — p.172–175)** :
  1. Sur la machine :
     a. Identifier les caractéristiques du moteur inscrites sur la plaque signalétique.
        — Tableau à remplir : **Puissance (Pm)** | **Fréquence de rotation (Nm)**.
     b. Saisir la gamme des vitesses, puis remplir dans l'ordre croissant le tableau suivant
        selon le modèle de machine existant au laboratoire.
        — Deux tableaux de 6 colonnes (positions **1 à 6** puis **7 à 12**), lignes
        « Fréquence de rotation » et « \* Combinaison des levier » [sic].
        \* Exemple : Faiseuse [sic] Milko : (■ / B / 1) → 352 ou (□ / A / 3) → 180.
        D'autres modèles (plus anciens) peuvent être repérés par la position des leviers.
  2. Régler la vitesse la plus faible, puis mettre la machine en marche et à l'aide d'un
     tachymètre, mesurer la vitesse de rotation de la broche.
     - Vitesse réglée : N… = ……………………
     - Vitesse mesurée : N<sub>mesurée</sub> = ……………………
     Comparer les deux vitesses puis écrire vos constatations
  3. On Donne le schéma cinématique de la boite de vitesses de la fraiseuse
     a. Que signifie le symbole représenté à gauche du moteur ?
     b. Sachant que les roues dentées (7) et (16) sont cylindriques à denture droite,
        compléter le tableau si dessous [sic] :

        | Pignon - roue | Module m (mm) | Nombre de dents Z | Diamètre primitif d (mm) | Entraxe a (mm) | Rapport r |
        | --- | --- | --- | --- | --- | --- |
        | Pignon (7) | 3 | ……………… | ……………… | 87 | 12/17 |
        | Roue (16) | 3 | ……………… | ……………… | 87 | 12/17 |

        Calcul : ……………………………………………………………
  4. A partir du dessin d'ensemble de la boîte de vitesses et sa nomenclature.
     a. Identifier les couples des roues en prise assurant la plus petite vitesse de rotation
        et donner l'expression du rapport **r = N₂₆ / N<sub>m</sub>**
        r = N₂₆ / N<sub>m</sub> = (…… , ……) ; (…… , ……) ; (…… , ……) = ………………
     b. Calculer la vitesse de rotation de la broche (26) **N₂₆mini**.  → case encadrée :
        N₂₆mini = ………………
     c. Identifier les couples des roues en prise assurant la plus grande vitesse de rotation
        et donner l'expression du rapport **r = N₂₆ / N<sub>m</sub>**
        r = N₂₆ / N<sub>m</sub> = (…… , ……) ; (…… , ……) ; (…… , ……) = ………………
     d. Calculer la vitesse de rotation de la broche (26) **N₂₆maxi**.  → case encadrée :
        N₂₆maxi = ………………
     e. On donne le rendement de la boite de vitesses **Ŋ = 0,8** [sic pour η] ; Calculer la
        puissance sur la broche (26).
     f. Calculer le couple **C₁** à la broche pour la vitesse **N₂₆mini**  → case encadrée :
        C₁ = ………………
     g. Calculer le couple **C₂** à la broche pour la vitesse **N₂₆maxi**  → case encadrée :
        C₂ = ………………
  5. Etude du mécanisme de changement de vitesses
     a. Donner la fonction de la bille (46) et le ressort (45).
     b. La bille (46) est susceptible de s'éjecter facilement par le ressort (45) au moment de
        montage ou de démontage. On désire modifier la solution en utilisant une vis de pression
        permettant de faciliter le montage et régler la tension du ressort. Compléter cette
        solution à l'échelle du dessin ci-dessous.
        *(Dessin p.175 : coupe locale du barillet monté sur le bâti (4) et l'axe (43), avec les
        repères sortis 47 — barillet, 42 — goupille élastique, 46 — bille, 45 — ressort et
        51 — pièce nouvelle à dessiner ; à droite les repères 4 et 43 sur la coupe.)*
     c. Compléter le graphe de montage de la bille (46) relatif à la nouvelle solution.
        *(Grille quadrillée p.175 : trois cases vides empilées « …. » alimentent le bloc
        « Sous- ensemble restant "Barillet" », lui-même relié par une flèche au bloc
        « Ensemble boite de vitesses ».)*

- **Schéma cinématique de la boîte de vitesses (p.173) — description** : quatre lignes d'arbres
  horizontales superposées, tracées en couleurs.
  - En bas, l'**arbre moteur (5)** issu du bloc « **Moteur** » (avec, à gauche du moteur, un
    symbole à identifier — question 3.a) : il porte le pignon-baladeur triple **Z₆ – Z₇ – Z₈**.
  - Au-dessus, l'**arbre intermédiaire (15)** portant **Z₁₃**, **Z₁₄**, **Z₁₆**, **Z₁₇**, **Z₁₈**.
  - Au-dessus, l'**arbre intermédiaire cannelé (21)** portant **Z₁₉**, le baladeur **Z₂₀** et
    **Z₂₃**.
  - En haut, l'ensemble **broche (26+27)** portant **Z₃₁** et **Z₃₃**.
  - Les liaisons pivot sont figurées par des rectangles aux extrémités ; les repères 5, 15, 21 et
    26+27 sont fléchés sur le schéma.

- **Vocabulaire & terminologie officielle** : gamme des vitesses, combinaison des leviers,
  plaque signalétique, tachymètre, denture droite, module, diamètre primitif, entraxe, rapport de
  transmission, couples de roues en prise, rendement, couple à la broche, graphe de montage,
  sous-ensemble, vis de pression.

---

###### Activité 4.3 — Présentation du support d'activité : Transformation de mouvement - Vis écrou (p.176–178)

- **Système / support d'étude** : **table longitudinale** (chariot longitudinal) de la fraiseuse
  universelle. Zone d'étude fléchée sur la photo p.176 (bas de la machine).
- **Compétences affichées** : aucune pastille CD sur p.176–178.
- **Mise en situation (p.176, verbatim)** :

  > En fraisage le mouvement d'avance est communiqué à la pièce à usiner qui est fixée sur la
  > table de la machine. Ce mouvement peut être fait suivant trois axes différents ce qui donne
  > à la table trois types de mouvement d'avance :
  > - Avance longitudinale ;
  > - Avance transversale ;
  > - Avance verticale.
  >
  > Chaque type d'avance est commandé de deux manières :
  > - Commande manuelle ;
  > - Commande automatique.
  >
  > En mode automatique l'avance peut être soit lente (phase de coupe) soit rapide
  > (Approche à vide ou dégagement de l'outil).

- **Ressources fournies** :
  - p.176 : photo de la fraiseuse annotée **Pendentif de commande**, **Broche**, axes **X**,
    **y**, **z**, **Table (Chariot longitudinal)**, **Chariot transversal**, **Chariot vertical**,
    encart bleu « Zone d'etude » [sic — sans accent]. QR-code **PDF**.
  - p.177 : **dessin d'ensemble** « Fraiseuse universelle — Table longitudinale »,
    **Echelle 1:5** [sic], repères 1 à 48, vue principale en coupe + coupes **A-A** et **B-B**
    + un **Détail 1:3**. QR-code **PDF**.
  - p.178 : **nomenclature** sur deux colonnes (repères 1 à 46 seulement — voir § Incertitudes).

- **Nomenclature de la table longitudinale (p.178)** :

| Rep. | Nbr. | Désignation | | Rep. | Nbr. | Désignation |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 | Manette | | 24 | 1 | Écrou à encoche type KM M40 |
| 2 | 1 | Volant | | 25 | 1 | Chapeau de palier |
| 3 | 1 | Moyeu du volant | | 26 | 1 | Vis de pression M8 |
| 4 | 1 | Cadran gradué | | 27 | 1 | Écrou spécial M26 |
| 5 | 1 | Bague | | 28 | 1 | Écrou de réglage M26 |
| 6 | 4 | Vis à tête cylindrique à six pans creux M4 | | 29 | 1 | Chariot vertical |
| 7 | 1 | Butée à billes | | 30 | 2 | Capteur fin de course |
| 8 | 1 | Bague | | 31 | 1 | Goupille élastique |
| 9 | 1 | Palier avant | | 32 | 2 | Écrou à encoche type KM M25 |
| 10 | 12 | Vis à tête cylindrique à six pans creux M8 | | 33 | 2 | Rondelle frein type KB |
| 11 | 1 | Vis d'entraînement de la table | | 34 | 2 | Graisseur |
| 12 | 8 | Vis à tête hexagonale M12 | | 35 | 1 | Soufflet de protection |
| 13 | 4 | Manette indexable | | 36 | 4 | Butée de fin de course |
| 14 | 8 | Vis à tête hexagonale M10 | | 37 | 1 | Cale de réglage |
| 15 | 1 | Cale latérale | | 38 | 1 | Chariot longitudinal |
| 16 | 2 | Contre glissière | | 39 | 1 | Clavette |
| 17 | 1 | Chariot transversal | | 40 | 1 | Arbre intermédiaire |
| 18 | 1 | Anneau élastique | | 41 | 1 | Raccord |
| 19 | 1 | Cale | | 42 | 1 | Flexible d'évacuation |
| 20 | 1 | Chapeau de palier | | 43 | 1 | Bouton de manœuvre |
| 21 | 1 | Coussinet | | 44 | 1 | Vis de blocage |
| 22 | 1 | Roue conique | | 45 | 1 | Écrou de réglage |
| 23 | 1 | Roue conique | | 46 | 1 | Vis sans fin de réglage |

- **Vocabulaire & terminologie officielle** : mouvement d'avance, avance longitudinale /
  transversale / verticale, commande manuelle / automatique, phase de coupe, approche à vide,
  dégagement de l'outil, pendentif de commande, chariot, glissière / contre-glissière, cadran
  gradué, vis d'entraînement, butée à billes, écrou à encoche type KM, rondelle frein type KB,
  capteur fin de course, soufflet de protection, manette indexable.

---

###### Activité 4.3 — Travail demandé : Transformation de mouvement - Vis écrou (p.179–180)

- **Système / support d'étude** : système vis-écrou d'entraînement de la table longitudinale
  (dessin d'ensemble p.177, nomenclature p.178).
- **Compétences affichées** : **CD 2.2 / CD 3.8** (p.179 et p.180). Pictos p.179 : **COOP**,
  **R. PRO**, **DECI**.
- **Encadré « I. Situation déclenchante » (p.179, verbatim)** :

  > Le mouvement d'avance de la table (chariot longitudinal) de la fraiseuse, est obtenu à partir
  > d'un mouvement de rotation, délivré, soit directement par l'utilisateur à l'aide du volant, ou
  > automatiquement à l'aide d'une boite d'avance préréglée.
  >
  > **Faisons l'étude de transformation de mouvement de la rotation à la translation.**

- **Ressources fournies** : la machine réelle (marquage au stylo sur les chariots), deux
  photographies de la marque faite sur les chariots transversal et longitudinal (p.179, la seconde
  cotée **C**), un croquis de vis avec la cote **Pas** (p.179), un chronomètre (question 8),
  la figure explicative du rattrapage de jeu **Table / Vis / Écrou réglable / Écrou / Tambour
  gradué** (p.180), le dessin d'ensemble et sa nomenclature.

- **Données numériques de l'énoncé** :
  - Tableau de manipulation p.179 : **n : nombre de tours du volant = 1, 2, 3** ;
    lignes « C : déplacement de la table » et « Rapport C/n » à remplir.
  - **Pas** de la vis d'entraînement (11) : à mesurer, en mm.
  - Course **C** en m et temps **t** en min (question 8) → vitesse **V** en **m/min**.
  - **N₁₁** en **tr/min** (question 10).

- **Travail demandé (II. Travail demandé — p.179–180)** :

  **Manipulation** (p.179, verbatim) : « Au stylo, faire une marque sur les deux chariots
  transversal et longitudinal comme le montre la figure ci-contre, positionner le cadran à
  « 0 », tourner le volant puis mesurer le déplacement du chariot longitudinal pour chaque nombre
  de tours effectué. »

  1. Mesurer le Pas de la vis d'entraînement (11)  → Pas = ………………… mm.
  2. Comparer C/n par rapport à la valeur du pas mesurée sur la vis.  → C/n ………………… pas
  3. Vérifier sur la machine si la vis a un ou plusieurs filets …………………
  4. Conclusion : La course est exprimée : C = …………………
  5. En poussant la table longitudinalement peut-on avoir la rotation de la vis d'entraînement (11) ?
  6. La transformation de mouvement est-elle :  Réversible ☐   Irréversible ☐
  7. Expliquer brièvement ce choix pour une machine-outil.
  8. Choisir une vitesse sur la boite des avances. En chronométrant le déplacement entre les deux
     marques réalisées précédemment, déterminer la vitesse d'avance réelle.
     C = ……………… m ; t = ……………… min  ⟹  V = ……………… m/min
  9. Comparer les deux vitesses …………………
  10. A partir de la vitesse du tableau déterminer la vitesse de rotation de la vis d'entraînement.
      → N₁₁ = ……………… tr/min
  11. Le système vis-écrou est très pratique comme solution dans les machines-outils, le seul
      problème est le rattrapage du jeu à l'inversion de sens de déplacement de la table.
      En se référant au dessin d'ensemble, sa nomenclature et en vous aidant par la figure
      explicative ci-contre
      a. Donner les repères des pièces permettant le réglage (rattrapage) du jeu.
      b. Décrire dans l'ordre les opérations à réaliser pour faire ce réglage.

- **Vocabulaire & terminologie officielle** : système vis-écrou, pas, filet (vis à un ou plusieurs
  filets), course, transformation de mouvement réversible / irréversible, rattrapage du jeu,
  écrou réglable, tambour gradué, boîte d'avances, vitesse d'avance.

---

##### Activité 5 — Maquette moteur à explosion (p.181–200)

---

###### Activité 5 — Présentation du support d'activité : Machine thermique (p.181–186)

- **Système / support d'étude** : **maquette de moteur à explosion** (coupe pédagogique)
  comprenant, d'un bout à l'autre : **Boite de vitesses**, **Embrayage**, **Moteur thermique**
  (photo annotée p.181).
- **Compétences affichées** : aucune pastille CD sur p.181–186. QR-code **PDF** p.181, p.184,
  p.185.
- **Mise en situation (p.181, verbatim)** :

  > La maquette du moteur à explosion permet d'étudier le fonctionnement d'un moteur réel de
  > véhicule.

- **Cours « 2. Moteur thermique à combustion interne » (p.181, verbatim)** :

  > Le moteur thermique de cette maquette, transforme l'énergie thermique produite par la
  > combustion (carburant + comburant) en énergie motrice mécanique. C'est donc un moteur
  > thermique à combustion interne à pistons alternatifs.
  > L'énergie mécanique, est obtenue par transformation du mouvement de translation du piston en
  > mouvement de rotation continu de l'arbre de sortie (vilebrequin).

- **« a. Définition du cycle à 4 temps » (p.181, verbatim)** :

  > On appelle cycle l'ensemble des phases qui se succèdent dans le moteur. Dans notre cas, le
  > cycle comprend quatre phases ou quatre temps :

- **Le cycle à quatre temps (p.182)** — quatre figures en coupe d'un cylindre (soupapes en V,
  bougie, piston, bielle, vilebrequin), légendées de gauche à droite **Admission**,
  **Compression**, **Explosion - Détente**, **Echappement** ; la flèche rouge dans le cylindre
  indique le sens de déplacement du piston (descente / montée / descente / montée) et la flèche
  courbe le sens de rotation du vilebrequin. Texte verbatim :

  > - **Temps admission :** Aspiration mélange air-essence.
  > - **Temps compression :** Compression du mélange.
  > - **Temps combustion-détente :** Inflammation rapide du mélange provoquant une brusque montée
  >   en pression des gaz puis leur détente.
  > - **Temps échappement :** Évacuation des gaz brûlés.
  >
  > **Remarque :** On constate que seul le troisième temps fournit de l'énergie, c'est le temps
  > moteur, les trois autres temps sont résistants.

- **« b. Différents composants d'un moteur thermique » (p.182)** — deux figures :
  - Schéma de principe d'un cylindre, annoté : **Echappement**, **Admission**, **Soupape**,
    **Chambre**, **Piston**, **Bielle**, **Vilebrequin**.
  - Vue 3D écorchée d'un moteur 4 cylindres, annotée : **Arbre à cames**, **Piston**,
    **Volant moteur**, **Bielle**, **Vilebrequin**, **Carter inférieur**,
    **Chaîne de distribution**.

- **« c. Fonctionnement d'un moteur à quatre temps (voir dessin d'ensemble) » (p.183, verbatim)** :

  > Le moteur étudié est un moteur thermique à quatre temps, il se compose essentiellement d'un
  > bloc (14) comportant quatre cylindres recevant quatre pistons (5).
  > Les pistons, oscillent verticalement entre deux positions extrêmes appelées point mort haut
  > (PMH) et point mort bas (PMB). Une bielle (2) articulée à l'une de ses extrémités au piston
  > (5) et à l'autre à un arbre coudé (1) appelé vilebrequin, permet de transformer le mouvement
  > rectiligne alternatif du piston en un mouvement de rotation continu du vilebrequin et du
  > volant moteur (15).
  > La chambre de combustion, délimitée par le piston (5) et le cylindre, est fermée dans sa
  > partie supérieure par la culasse (11). Cette culasse est équipée de huit soupapes (12), ayant
  > un mouvement alternatif de translation grâce à un arbre à cames (9). Les cames sont
  > synchronisées à la rotation du vilebrequin, elles gèrent la circulation des gaz au travers du
  > moteur dans la chambre de combustion. Le moteur est caractérisé par sa cylindrée, qui est
  > égale au volume balayé par le piston, multiplié par le nombre de cylindres.
  > Un temps correspond à une course de piston dans le cylindre. Le cycle à quatre temps met en
  > œuvre quatre courses de piston (deux aller et retour) et correspond donc à deux tours du
  > vilebrequin.

- **Nomenclature du moteur à explosion (p.183)** :

| Rep. | Nbr. | Désignation | Matière | Observation |
| --- | --- | --- | --- | --- |
| 1 | 1 | Vilebrequin | 100 Cr Mo 7 | |
| 2 | 4 | Corps de bielle | C40 | |
| 3 | 4 | Axe du piston | C40 | |
| 4 | 4 | Coussinet | Cu Sn 10 Pb | |
| 5 | 4 | Piston | | |
| 6 | 4 | Segment coup de feu | | |
| 7 | 1 | Pignon | 20 Ni Cr Mo 2 | |
| 8 | 1 | Chaîne de distribution | | Standard |
| 9 | 1 | Arbre à cames | En-GJMB-450-6 | |
| 10 | 1 | Couvercle | | |
| 11 | 1 | Culasse | | |
| 12 | 8 | Soupape | | Standard |
| 13 | 1 | Joint de culasse | | Standard |
| 14 | 1 | Bloc moteur | | |
| 15 | 1 | Volant moteur | | |
| 16 | 5 | Coussinet en deux parties | Cu Sn 10 Pb | |
| 17 | 5 | Palier | | |
| 18 | 1 | Carter inférieur | | |
| 19 | 4 | Coussinet en deux parties | Cu Sn 10 Pb | |
| 20 | 4 | Chapeau de bielle | | |
| 21 | 16 | Ressort | 51 Cr V4 | |

- **Dessin d'ensemble du moteur à explosion (p.184)** : coupe longitudinale du moteur 4 cylindres,
  repères **1 à 21** placés sur les quatre bords. Cartouche : « **Moteur à explosion à quatre
  temps** », **Echelle :1:5** [sic], symbole de projection européenne. QR-code **PDF**.

- **« 5. Boite de vitesses » (p.185, verbatim)** :

  > La boite de vitesses est destinée à adapter la vitesse du véhicule aux différentes situations
  > de conduite.

- **Dessin d'ensemble de la boîte de vitesses (p.185)** : coupe de la boîte de vitesses de la
  maquette, repères **1 à 33** répartis sur les quatre bords. Note portée sur le dessin :
  « L'axe (30) porte pignon marche arrière (13) ramené dans le plan de coupe ».
  Cartouche : « **Boîte de vitesses** », **Echelle :1:5** [sic]. QR-code **PDF**.

- **Schéma cinématique de la boîte de vitesses (p.186)** : cinq trains repérés en chiffres
  romains **I, II, V, III, IV** entre l'arbre d'entrée (14) et l'arbre de sortie (16), plus le
  train de **marche arrière** noté **MA** à gauche. Repères fléchés en haut :
  11, 9, 17, 7, 5, 16, 18, 3, 19, 1, 14 ; en bas : 20, 13, 12, 10, 8, 6, 4, 2 ; à droite : **15**
  (arbre intermédiaire, ligne inférieure). Les liaisons pivot sont figurées par des rectangles,
  les baladeurs par des symboles à croix, le bâti par des hachures en bas à droite.

- **Nomenclature de la boîte de vitesses de la maquette (p.186)** :

| Rep. | Nbr. | Désignation | | Rep. | Nbr. | Désignation |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 | Pignon ; Z = 37 | | 18 | 1 | Baladeur 3<sup>ème</sup> vitesse |
| 2 | 1 | Pignon arbré ; Z = 47 | | 19 | 1 | Baladeur 4<sup>ème</sup> et 5<sup>ème</sup> vitesse |
| 3 | 1 | Pignon fou 4<sup>ème</sup> vitesse ; Z = 44 | | 20 | 1 | Roue dentée |
| 4 | 1 | Pignon arbré ; Z = 41 | | 21 | 1 | Vis sans fin pour câble compteur |
| 5 | 1 | Pignon fou 3<sup>ème</sup> vitesse ; Z = 31 | | 22 | 1 | Carter gauche |
| 6 | 1 | Pignon arbré ; Z = 47 | | 23 | 1 | Carter principal |
| 7 | 1 | Pignon fou 2<sup>ème</sup> vitesse ; Z = …. | | 24 | 1 | Carter droit |
| 8 | 1 | Pignon arbré ; Z = ….dents | | 25 | 3 | Fourchette |
| 9 | 1 | Pignon fou 1<sup>ère</sup> vitesse ; Z = 37 | | 26 | 3 | Moyeu de synchroniseur |
| 10 | 1 | Pignon arbré ; Z = 13 | | 27 | 3 | Tige de manœuvre |
| 11 | 1 | Roue dentée ; Z = 46 | | 28 | 2 | Roulement KB |
| 12 | 1 | Pignon ; Z = 25 | | 29 | 2 | Roulement BC |
| 13 | 1 | Pignon marche arrière ; Z = 17 | | 30 | 1 | Axe |
| 14 | 1 | Arbre d'entrée (Moteur) | | 31 | 1 | Bouchon de remplissage |
| 15 | 1 | Arbre intermédiaire | | 32 | 1 | Bouchon de vidange |
| 16 | 1 | Arbre de sortie | | 33 | 1 | Fourchette pour marche arrière |
| 17 | 1 | Baladeur 1<sup>ère</sup> et 2<sup>ème</sup> vitesse | | | | |

- **Vocabulaire & terminologie officielle** : moteur thermique à combustion interne, pistons
  alternatifs, carburant + comburant, cycle à 4 temps, admission / compression /
  combustion-détente (explosion-détente) / échappement, temps moteur, temps résistants,
  point mort haut (PMH), point mort bas (PMB), arbre coudé, vilebrequin, bielle, culasse,
  soupape, arbre à cames, came, chambre de combustion, cylindrée, volume balayé, course,
  segment coup de feu, coussinet en deux parties, chapeau de bielle, chaîne de distribution,
  volant moteur, carter inférieur, pignon fou, pignon arbré, baladeur, moyeu de synchroniseur,
  fourchette, marche arrière (MA).

---

###### Activité 5.1 — Machine thermique (p.187–191)

- **Système / support d'étude** : maquette du moteur à explosion (dessin d'ensemble p.184,
  nomenclature p.183).
- **Compétences affichées** : **CD 2.2 / CD 3.8** (p.187 à 191). Pictos p.187 : **COMM**,
  **R. PRO**.
- **Encadré « I. Situation déclenchante » (p.187, verbatim)** :

  > Le moteur à explosion est un moteur à combustion interne, principalement utilisé pour la
  > propulsion de différents véhicules mobiles (voiture, avion…), ainsi que pour des installations
  > fixes (pompe, groupe électrogène…)
  >
  > **Voyons comment ces moteurs transforment l'énergie chimique en puissance mécanique grâce à
  > des combustions très rapides ?**

- **Ressources fournies** : maquette réelle (manœuvre du piston, mesure à la règle métallique),
  photo de la maquette avec étiquettes à relier (p.187), photo en coupe des soupapes et
  évidements (p.188), photo de la culasse et des ressorts de soupapes (p.188), quatre figures
  a/b/c/d du mécanisme bielle-manivelle (p.188), figure cotée piston/bielle/vilebrequin (p.190),
  photo arbre à cames + poussoir (p.191), diagramme des espaces et cercle minimal (p.191),
  QR-code **Vid** (p.187).

- **Données numériques de l'énoncé** :
  - Diamètre du piston **85 mm** (question B.5) → cylindrée à calculer **en litre**.
  - Vitesse du vilebrequin à un régime donné **N₁ = 1600 tr/min** (p.190).
  - **Échelle des vitesses : 0,3 m/s → 1 mm** (p.190).
  - Diagramme des espaces de la came (p.191) : axe **Course (mm)** gradué 1, 3, 5, 7 ;
    axe **Temps (s)** gradué de 0 à 12. La courbe est nulle de 0 à ≈4 s, monte jusqu'à
    **7 mm** au voisinage de t = 6 s, redescend à zéro vers t = 8 s et reste nulle jusqu'à 12 s
    (repères verticaux tracés à t = 5, 6 et 7 s).
  - Phases de la came (p.191) : **Phase 1** — demi-tour (course nulle) ; **Phase 2** — quart de
    tour ; **Phase 3** — quart de tour.

- **Travail demandé — A. Analyse fonctionnelle (p.187–188)** :
  1. Quelle est la fonction globale du moteur à explosion ?
  2. Quelle est la matière d'œuvre entrante du moteur à explosion ?
  3. Quelle est la matière d'œuvre sortante du moteur à explosion ?
  4. Sur la figure ci-dessous de la maquette du moteur à explosion, relier par une flèche chaque
     terme, par l'élément qui lui correspond.
     — Étiquettes à relier : **Manette de commande**, **Arbre à came**, **Soupape**,
     **Cylindre**, **Piston**, **Boite de vitesses**, **Volant moteur**, **Vilebrequin**,
     **Bielle**.
  5. En se référant à la figure ci-contre, deux types de soupapes existent, (soupape gauche,
     soupape droite) donner leurs noms. *(Photo annotée **Soupape** et **Evidement**.)*
  6. Donner le rôle des soupapes.
  7. Par quoi est assurée l'étanchéité entre la chambre de combustion et le carter moteur ?
  8. Donner le rôle des évidements créés sur le carter moteur.
  9. En se référant à la figure ci-contre, expliquer le rôle des ressorts liés à chaque soupape.
  10. Donner le mode d'obtention de la culasse supportant les soupapes.

- **Travail demandé — B. Étude cinématique du mouvement de piston (p.188–190)** :
  1. Compléter ci-dessous :
     - Le schéma cinématique du mécanisme bielle manivelle sur la figure (a).
     - Les schémas du piston, bielle et vilebrequin sur les figures (c) et (d).
     - Indiquer la course du piston sur les figures (c) et (d).
     *(Quatre figures titrées **Schéma cinématique** (a — annotée Piston, Bielle, Vilebrequin,
     Carter), **Position intermédiaire du piston** (b), **Position haute du piston** (c),
     **Position basse du piston** (d).)*
  2. Manœuvrer la maquette pour mettre le piston en position haute, puis, mesurer la valeur
     réelle de la course du piston à l'aide d'une règle métallique.
  3. Trouver la relation de la course du piston en fonction du rayon de vilebrequin.
  4. Déduire la valeur du rayon de vilebrequin.
  5. Calculer en litre la cylindrée du moteur, sachant que le diamètre du piston est de **85 mm**.
  6. Pour le moteur, compléter le tableau des mouvements suivant (mettre une croix) :

     | | Mouvement d'entrée | Mouvement de sortie |
     | --- | --- | --- |
     | Vilebrequin | | |
     | Piston | | |

  7. Que peut-t-on [sic] dire de la transformation de mouvement ?
     Réversible ☐   Irréversible ☐
  8. Par quoi est assuré le mouvement continu du vilebrequin ?
  9. Donner à chaque terme général, le nom de l'élément qui lui correspond du moteur à explosion.

     | | Terme général | Désignation des pièces du moteur à explosion |
     | --- | --- | --- |
     | 1 | Manivelle | ……………………………… |
     | 2 | Bielle | ……………………………… |
     | 3 | Coulisseau | ……………………………… |
     | 4 | Glissière | ……………………………… |

     *(Schéma associé : manivelle **1** de rayon **R** tournant autour d'un bâti hachuré,
     point **A** en tête de manivelle, bielle **2**, coulisseau **3** au point **B** guidé dans
     la glissière **4** ; mentions **Rotation** et **Translation**.)*
  10. Détermination graphique de la vitesse linéaire du point B du piston.
      On donne : La vitesse du vilebrequin à un régime donné, est **N₁ = 1600 tr/min**.
      - Tracer sur la figure ci-contre, les trajectoires des deux points A et B en utilisant deux
        couleurs différentes.
      - Calculer la vitesse angulaire instantanée du vilebrequin : **ω₁**
      - Déterminer et représenter sur la même figure, la vitesse linéaire du point A : **V<sub>A/0</sub>**
        Échelle des vitesses : **0,3 m/s → 1 mm**
      - Représenter et déterminer graphiquement la norme de la vitesse du point B appartenant au
        piston par rapport à la partie fixe, en utilisant le **théorème de l'équiprojectivité**.
      *(Figure p.190 : piston en rouge portant le point **B**, bielle en vert, vilebrequin en bleu
      portant le point **A**, sens de rotation indiqué par une flèche courbe.)*

- **Travail demandé — C. Étude du système à came (p.191)** :

  Texte introductif (verbatim) :

  > En se référant à la maquette de moteur à explosion, la translation alternative des soupapes
  > « l'ouverture et la fermeture », est assurée par un système de transformation de mouvement de
  > rotation continu de l'arbre à cames, en un mouvement de translation rectiligne alternatif des
  > poussoirs.

  1. De quel type de cames s'agit-il ?
  2. Ce système est-il réversible ?
  3. Préciser le type de frottement entre Poussoir/ Came : (Glissement ; roulement)
  4. Proposer une autre solution constructive pour réduire le frottement.
  5. On désire tracer le profil de la came.
     La rotation de l'arbre à cames commande l'ouverture et la fermeture des soupapes.
     Pour un tour de l'arbre à cames on a trois phases :
     - Phase 1 : Fermeture de la soupape pendant un demi-tour (course nulle).
     - Phase 2 : Descente de la soupape pendant un quart de tour.
     - Phase 3 : Montée de la soupape pendant un quart de tour.
     A partir du diagramme des espaces ci-dessous, tracer le profil extérieur de la came.
     *(À droite : cercle de construction divisé en 12 secteurs, avec le **Cercle minimal**
     intérieur et l'origine **0** repérée à gauche ; sens de rotation fléché.)*

- **Vocabulaire & terminologie officielle** : fonction globale, matière d'œuvre entrante /
  sortante, évidement, mode d'obtention, mécanisme bielle-manivelle, manivelle, coulisseau,
  glissière, course du piston, rayon de vilebrequin, cylindrée, vitesse angulaire instantanée ω,
  vitesse linéaire V<sub>A/0</sub>, échelle des vitesses, théorème de l'équiprojectivité, came,
  poussoir, profil de came, cercle minimal, diagramme des espaces, frottement de glissement /
  de roulement, solution constructive.

---

###### Activité 5.2 — Présentation de l'embrayage (p.192–193)

- **Système / support d'étude** : **embrayage automobile** de la maquette du moteur à explosion.
- **Compétences affichées** : **CD 2.2 / CD 3.8** (p.192 et p.193).
- **« 1. Fonctionnement » (p.192, verbatim)** :

  > L'action sur la fourchette (18) pousse la butée d'embrayage (13) contre le diaphragme (11),
  > qui se déforme de manière à faire reculer le plateau (8) pour assurer le débrayage.
  > Le retour de la fourchette (18) par le ressort (24) assure l'embrayage.

- **Ressources fournies** : dessin d'ensemble p.193 (« **EMBRAYAGE AUTOMOBILE** »,
  **Echelle :1:2** [sic], repères 1 à 30, QR-code **PDF**) et nomenclature p.192.

- **Nomenclature de l'embrayage (p.192)** :

| Rep. | Nbr. | Désignation | Matière | Observation |
| --- | --- | --- | --- | --- |
| 1 | 1 | Arbre porte volant | C 60 | |
| 2 | 6 | Ressort d'embrayage | 60 Si Cr 7 | |
| 3 | 1 | Disque droit | C 35 | |
| 4 | 1 | Disque gauche | C 35 | |
| 5 | 12 | Rivet | | |
| 6 | 3 | Vis à tête cylindrique à six pans creux ISO 4762 | | |
| 7 | 1 | Couronne dentée | C 60 | |
| 8 | 1 | Plateau | EN-GJL-200 | |
| 9 | 1 | Couvercle | C 35 | |
| 10 | 1 | Carter | EN-MC 21 120 | |
| 11 | 4 | Diaphragme | | |
| 12 | 1 | Rivet | | |
| 13 | 1 | Butée d'embrayage | 10 Cr 6 | |
| 14 | 1 | Bague porte butée | S 235 | |
| 15 | 1 | Bague | Cu Sn 8 | |
| 16 | 1 | Joint à lèvre, type A | | |
| 17 | 1 | Arbre d'embrayage | C 60 | |
| 18 | 1 | Fourchette | C 35 | |
| 19 | 1 | Axe de fourchette | C 60 | |
| 20 | 1 | Levier ressort | 60 Si Cr 7 | |
| 21 | 1 | Membrane | | |
| 22 | 3 | Ressort de maintien | 60 Si Cr 7 | |
| 23 | 1 | Rivet | | |
| 24 | 1 | Ressort | 60 Si Cr 7 | |
| 25 | 3 | Vis sans tête fondue à bout plat ISO 4026 | | |
| 26 | 1 | Disque porte garniture | C 35 | |
| 27 | 1 | Volant | EN-GJL-200 | |
| 28 | 3 | Rivet | | |
| 29 | 4 | Vis à tête hexagonale ISO 40-18 | | |
| 30 | 1 | Moyeu amortisseur | C 35 | |

- **Vocabulaire & terminologie officielle** : embrayage, débrayage, fourchette, butée
  d'embrayage, diaphragme, plateau, disque porte garniture, moyeu amortisseur, couronne dentée,
  volant, joint à lèvre, levier ressort, ressort de maintien.

---

###### Activité 5.2 — Travail demandé : Embrayage (p.194–195)

- **Compétences affichées** : **CD 2.2 / CD 3.8** (p.194 et p.195). Picto p.194 : **DECI**.
- **Encadré « I. Situation déclenchante » (p.194, verbatim)** :

  > L'embrayage d'automobile, transmet à volonté la puissance du moteur à la boîte de vitesses,
  > puis, vers les roues. C'est grâce à l'embrayage et à la boite qu'on peut changer les rapports
  > de vitesses.
  >
  > **Faisons une analyse de fonctionnement de cet embrayage, pour identifier ses constituants.**

- **Ressources fournies** : dessin d'ensemble p.193 + nomenclature p.192 ; deux photographies de
  la maquette (p.194) à annoter ; photographie d'un kit d'embrayage réel (disque + mécanisme +
  butée) à légender (p.195) ; maquette réelle (manivelle + pédale d'embrayage).
- **Données numériques de l'énoncé** : repères à placer sur les photos —
  **(9 ; 7 ; 8 ; 30 ; 6 ; 11 ; 13 ; 18)** ; noms à placer sur le kit — **Couvercle – Plateau –
  Butée – Diaphragme – Disque porte garniture – Moyeu amortisseur**.

- **Travail demandé — A. Analyse fonctionnelle (p.194–195)** :
  1. Se référer au dessin d'ensemble de l'embrayage, pour placer les repères des pièces suivantes
     (9 ;7 ;8 ;30 ;6 ;11 ;13 ;18) sur les figures ci-dessous.
     *(Photo de gauche : 5 flèches à renseigner ; photo de droite : 3 flèches à renseigner.)*
  2. Citer les facteurs dont dépend le couple transmissible.
  3. Expliquer l'utilité de la couronne (7) montée sur le volant moteur (27).
  4. En se référant à la maquette du moteur à explosion, appuyer sur la pédale de l'embrayage,
     tourner le vilebrequin à l'aide de la manivelle et donner l'état du disque (26)
     (tourne ; ne tourne pas).
  5. Placer le nom de chaque constituant de l'embrayage à disque sur les figures ci-dessous:
     *Couvercle – Plateau – Butée – Diaphragme – Disque porte garniture – Moyeu amortisseur.*
     *(Photo p.195 : disque d'embrayage à garnitures et ressorts de moyeu, mécanisme à diaphragme
     et butée ; six traits de légende, trois en haut et trois en bas.)*
  6. Donner la fonction des ressorts situés sur le moyeu amortisseur

- **Vocabulaire & terminologie officielle** : couple transmissible, constituants de l'embrayage,
  embrayage à disque, couronne dentée (démarreur), pédale d'embrayage, moyeu amortisseur.

---

###### Activité 5.3 — Boîte de vitesses (p.196–198)

- **Système / support d'étude** : boîte de vitesses de la maquette du moteur à explosion
  (dessin d'ensemble p.185, schéma cinématique et nomenclature p.186).
- **Compétences affichées** : **CD 2.2 / CD 3.8** (p.196, 197, 198). Pictos p.196 : **COOP**,
  **R. PRO**.
- **Encadré « I. Situation déclenchante » (p.196, verbatim)** :

  > La boîte de vitesses, est un système mécanique de transmission de puissance, qui permet
  > d'engendrer différents rapports de vitesses du moteur aux roues motrices d'un véhicule.
  >
  > La boîte est constituée de plusieurs éléments permettant le changement des différents rapports
  > de vitesses.
  >
  > **Faisons une analyse de fonctionnement de cette boîte, pour identifier ses constituants.**

- **Ressources fournies** : mécanisme réel manipulable, schéma cinématique p.186, photo en coupe
  des arbres et pignons (p.196 et p.197), grille de la **grille de sélection**
  (1 3 5 / 2 4 MA), photo extérieure de la boîte avec deux éléments fléchés (p.197), photo de la
  prise de mouvement du compteur (p.198, repères **20** et **21** fléchés).

- **Données numériques de l'énoncé** :
  - Grille des vitesses reproduite deux fois (p.196 et p.197) :
    ligne du haut **1 | 3 | 5**, ligne du bas **2 | 4 | MA**.
  - Repères des composants donnés dans le tableau à compléter : **15**, **16**,
    **1-2-3-4-5-6-7-8-9-10**.
  - Six positions du levier **A à F** → ordres de vitesse **1ère, 2ème, 3ème, 4ème, 5ème, MA** ;
    couple d'engrenage donné pour A : **(Z1 , Z2) ; (Z9 , Z10)** ; rapport de transmission donné
    pour D : **1** ; sens de mouvement donné pour A : **Même sens**.
  - Nombres de dents (question B.2) : **Pignon (1) = 37 dents**, **Roue (2) = 47 dents**,
    **Pignon (7) = ……… dents**, **Roue (8) = ……… dents**.
  - Question B.4 : **10 tours** de l'arbre d'entrée (1) → **N₁₆** tours de l'arbre de sortie (16).
  - Question B.7.c : **Vitesse du véhicule V = 30 km/h** ; **Diamètre du pneu de la roue
    d<sub>pneu</sub> = 60 cm**.

- **Travail demandé — A. Analyse fonctionnelle (p.196–197)** :

  Consigne d'entrée (verbatim) : « En manipulant le mécanisme réel et en s'aidant du schéma
  cinématique et de la figure ci-contre de la boite de vitesses. »

  1. Compléter le tableau suivant :

     | Désignation des composants | Repères des composants | Fonction |
     | --- | --- | --- |
     | Arbre d'entrée | ………………… | Transmettre le mouvement de rotation à la boite de vitesses |
     | ……………………………… | 15 | ………………………………………………… |
     | Arbre de sortie | 16 | ………………………………………………… |
     | Engrenage à dentures droites | ………………… | ………………………………………………… |
     | ……………………………… | 1-2-3-4-5-6-7-8-9-10 | Adapter la vitesse en proposant plusieurs rapports |
     | Baladeurs | ………………… | ………………………………………………… |

  2. Identifier les éléments de guidage en rotation des arbres (15) et (16).
  3. Identifier le type de lubrification adoptée pour cette boite de vitesses.
  4. Donner les noms des deux éléments indiqués sur la figure ci-dessous:
     *(Photo extérieure du carter de boîte, deux flèches rouges pointant deux bouchons ; à droite,
     la grille de sélection 1 3 5 / 2 4 MA.)*

- **Travail demandé — B. Étude des caractéristiques de la transmission (p.197–198)** :
  1. On distingue 6 positions possibles du levier de vitesse. Pour chaque position, compléter sur
     le tableau suivant les couples d'engrenages, le rapport de transmission, l'ordre des vitesses
     et comparer les sens de mouvement.

     | Position du levier | Couples d'engrenage | Rapport de transmission | Ordre de vitesse | Sens de mouvement |
     | --- | --- | --- | --- | --- |
     | A | (Z1 , Z2) ; (Z9 , Z10) | ……………… | 1<sup>ère</sup> | Même sens |
     | B | ……………………… | ……………… | 2<sup>ème</sup> | ……………………… |
     | C | ……………………… | ……………… | 3<sup>ème</sup> | ……………………… |
     | D | ……………………… | 1 | 4<sup>ème</sup> | ……………………… |
     | E | ……………………… | ……………… | 5<sup>ème</sup> | ……………………… |
     | F | ……………………… | ……………… | MA | ……………………… |

  2. Compléter le tableau suivant relatif à la 2ème vitesse par les nombres de dents des roues
     (7) et (8).

     | | |
     | --- | --- |
     | Pignon (1) | 37 dents |
     | Roue (2) | 47 dents |
     | Pignon (7) | ……… dents |
     | Roue (8) | ……… dents |

  3. Calculer le rapport de transmission de cette vitesse **r₂**.
  4. Déterminer par calcul, le nombre de tours **N₁₆** effectué par l'arbre de sortie (16), pour
     **10 tours** de l'arbre d'entrée (1).
  5. Faire cette manipulation sur la maquette et déduire le nombre de tours de l'arbre de sortie
     **N'₁₆**.
  6. Comparer les deux résultats trouvés.
  7. La prise de mouvement au câble du compteur de vitesse est réalisée par le système roue et vis
     sans fin (21 ; 20) comme le montre la figure ci-contre.
     a. Compter le nombre de filets de la vis ainsi que le nombre de dents de la roue
     b. Calculer le rapport de vitesse de cet engrainement [sic] **(20)/(21)**.
     c. On suppose que le pont arrière ne varie pas la vitesse et que le premier rapport de la
        boite est sélectionné.
        On donne :
        - Vitesse du véhicule **V = 30 km/h** ;
        - Diamètre du pneu de la roue **d<sub>pneu</sub> = 60 cm** ;
        Calculer la vitesse de rotation de l'arbre de sortie (16) en **tr/min**.
     d. Déduire la vitesse de rotation du câble compteur

- **Vocabulaire & terminologie officielle** : rapports de vitesses, roues motrices, levier de
  vitesse, couples d'engrenage, rapport de transmission, ordre de vitesse, sens de mouvement,
  guidage en rotation, lubrification, bouchon de remplissage / de vidange, engrenage à dentures
  droites, système roue et vis sans fin, filets de la vis, câble compteur, pont arrière.

---

###### Activité 5.4 — Synchroniseur / Boîte de vitesses (p.199–200)

- **Système / support d'étude** : **synchroniseur** de la boîte de vitesses de la maquette
  (dessin d'ensemble de la page **185**, explicitement rappelé par le manuel).
- **Compétences affichées** : **CD 2.2 / CD 3.8** (p.199 et p.200). Pictos p.199 : **COOP**,
  **DECI**, **CRITI**. QR-code **Vid** p.200.
- **Encadré « I. Situation déclenchante » (p.199, verbatim)** :

  > Le synchroniseur est un dispositif égalisant la vitesse de deux arbres avant d'établir leurs
  > liaison par crabotage. Cette opération s'effectue à partir du point mort en deux temps.
  >
  > **Faisons une analyse de fonctionnement de ce dispositif.**

- **Ressources fournies** :
  - Consigne d'entrée (p.199, verbatim) : « En se référant au dessin d'ensemble de la page 185. »
  - **Vue éclatée 3D** du synchroniseur (p.199) : de gauche à droite, **Pignon fou (7)**, une
    bague, le moyeu et le baladeur, trois clavettes et un jonc, une bague, puis
    **Pignon fou (9)**. Six traits de légende à renseigner (trois en haut, trois en bas).
  - **Trois coupes couleur du synchroniseur** (p.199 bas, p.200 ×2) montrant, avec le même
    codage : le pignon fou **(5)** en vert, la **Bague de synchronisation** en violet, le
    baladeur **(18)** en rose, le moyeu **(26)** en jaune et les clavettes en bleu ; les flèches
    rouges donnent le sens de déplacement du baladeur et l'effort sur la clavette.
- **Données numériques de l'énoncé** : repères de la coupe **5**, **18**, **26** ;
  liste de termes à placer sur la vue éclatée : **Bague de synchronisation ; Baladeur ; Moyeu ;
  Clavette ; Ressort ; Bague de friction.**

- **Travail demandé (II. Travail demandé — p.199–200)** :
  1. Placer sur la vue éclatée suivante les noms des constituants du synchroniseur relatif à la
     1ère et 2ème vitesse : *Bague de synchronisation ; Baladeur ; Moyeu ; Clavette ; Ressort ;
     Bague de friction.*
  2. Pour enclencher la 5<sup>ème</sup> vitesse, compléter les paragraphes de la page suivante
     relatifs à chaque temps.

     **POINT MORT :** (texte donné, p.199, verbatim)

     > Le baladeur (18) est au point mort, la bague de synchronisation n'est pas en contact avec
     > le pignon fou (5) au niveau des surfaces coniques.

     **Temps 1 : SYNCHRONISATION** — texte à trous (p.200, verbatim, trous compris) :

     > …………………………………… se déplace en translation vers le pignon fou (5). (18) entraine la bague de
     > synchronisation par intermédiaire ……………………………… vers la gauche. En conséquence il y a
     > entraînement par …………………………, (5) tourne à la même vitesse que la bague de synchronisation.

     **Temps 2 : CRABOTAGE** — texte à trous (p.200, verbatim, trous compris) :

     > Le baladeur (18) poursuit sa translation vers ………………………… les clavettes s'effacent et
     > ………………………… s'effectue. Le pignon fou (5) et le moyeu (26) sont …………………… et tournent à la
     > même vitesse.

- **Vocabulaire & terminologie officielle** : synchroniseur, crabotage, point mort, bague de
  synchronisation, bague de friction, surfaces coniques, baladeur, moyeu, clavette, pignon fou,
  enclencher une vitesse, égalisation des vitesses.

##### Bornes de scope observées — p.163–200

- ✅ INCLUS :
  - **Frein électromagnétique** (p.163–167) : lecture de dessin d'ensemble + nomenclature,
    identification des mouvements (tournante / glissante / fixe), classes d'équivalence et schéma
    cinématique, type de commande, état excité / non excité de la bobine, et **calcul du couple de
    freinage** avec la formule fournie Cf = (2/3)·Fp·f·n·(R³−r³)/(R²−r²), f = 0,4, Cf = 18 Nm →
    effort presseur Fp puis effort par ressort. Rôle des écrous autofreinés.
  - **Boîte de vitesses de fraiseuse** (p.168–175) : plaque signalétique moteur, gamme des
    12 vitesses et combinaison des leviers, mesure au tachymètre, lecture du schéma cinématique,
    **engrenage cylindrique à denture droite** (module, nombre de dents, diamètre primitif,
    entraxe a = 87 mm, rapport r = 12/17), **chaînes cinématiques** mini et maxi de la broche
    (rapports r = N₂₆/N<sub>m</sub>), **rendement η = 0,8**, **puissance sur la broche** et
    **couples C₁ et C₂**, mécanisme d'indexage bille + ressort, modification constructive par
    vis de pression et **graphe de montage**.
  - **Transformation de mouvement vis-écrou** (p.176–180) : mesure expérimentale du rapport C/n
    et du **pas**, nombre de filets, expression de la course, **réversibilité / irréversibilité**,
    vitesse d'avance V = C/t, vitesse de rotation N₁₁ de la vis, **rattrapage du jeu** par écrou
    réglable.
  - **Moteur thermique à explosion** (p.181–191) : cycle à **quatre temps** (admission,
    compression, combustion-détente, échappement ; un seul temps moteur), composants du moteur,
    PMH/PMB, cylindrée = volume balayé × nombre de cylindres, **analyse fonctionnelle**
    (matière d'œuvre entrante/sortante), **mécanisme bielle-manivelle** (manivelle, bielle,
    coulisseau, glissière), course en fonction du rayon de vilebrequin, **cylindrée en litre**
    (Ø piston 85 mm), **cinématique graphique** (ω₁ à partir de N₁ = 1600 tr/min, V<sub>A/0</sub>,
    échelle 0,3 m/s → 1 mm, **théorème de l'équiprojectivité** pour V<sub>B</sub>), **système à
    came** (type de came, réversibilité, frottement poussoir/came, tracé du profil à partir du
    **diagramme des espaces** et du cercle minimal, phases 1/2 + 1/4 + 1/4 de tour).
  - **Embrayage automobile** (p.192–195) : chaîne fonctionnelle fourchette → butée → diaphragme →
    plateau (débrayage) et retour par ressort (embrayage), **facteurs dont dépend le couple
    transmissible**, rôle de la couronne dentée sur le volant, identification des constituants
    d'un embrayage à disque, rôle des ressorts du moyeu amortisseur.
  - **Boîte de vitesses automobile** (p.196–198) : composants et fonctions, guidage en rotation,
    lubrification, **6 positions du levier** (5 vitesses + MA) avec couples d'engrenage, rapports
    et sens de mouvement, calcul de **r₂**, nombre de tours de l'arbre de sortie, **roue et vis
    sans fin** du câble compteur, passage V = 30 km/h + d<sub>pneu</sub> = 60 cm → N₁₆ en tr/min.
  - **Synchroniseur** (p.199–200) : constituants, **point mort / synchronisation / crabotage**
    en deux temps.

- ⛔ EXCLU / seulement mentionné :
  - Le **pont arrière** est explicitement neutralisé par hypothèse (« On suppose que le pont
    arrière ne varie pas la vitesse », p.198) : il n'est pas étudié.
  - La **boite d'avances** de la fraiseuse est nommée (p.179 « boite d'avance préréglée », p.180
    « Choisir une vitesse sur la boite des avances ») mais son mécanisme n'est ni dessiné ni
    analysé dans cette tranche.
  - Le **pendentif de commande**, le **chariot transversal** et le **chariot vertical** sont
    nommés et localisés p.176, mais seul le **chariot longitudinal** est étudié.
  - Les **capteurs fin de course (30)** et **butées de fin de course (36)** figurent en
    nomenclature p.178 sans aucune question associée.
  - L'**allumage** (bougie, carburateur, circuit d'alimentation) apparaît sur les figures p.182 et
    p.181 mais n'est jamais traité : le manuel reste sur la mécanique.
  - Le **diagramme thermodynamique (P-V)** du cycle **n'est pas** présenté : le cycle à quatre
    temps est décrit par des **figures en coupe du cylindre** et par le texte des quatre temps
    (p.182), pas par un diagramme de Clapeyron ni par un calcul de rendement thermique.
  - Le **tracé du profil de came** est demandé graphiquement (p.191) mais aucune loi de mouvement
    (courbe d'accélération, came à galet dimensionnée) n'est donnée.
  - Le **synchroniseur** est étudié en fonctionnement (deux temps) : aucun calcul d'énergie de
    synchronisation ni de couple de friction n'est demandé.
  - Le **renvoi explicite hors tranche** : p.199 renvoie au dessin d'ensemble de la **page 185**
    (dans la tranche) ; aucun renvoi vers des pages postérieures à 200 n'apparaît.

##### Activité 6 — Palan électrique à chaine · Présentation du support d'activité (p.201–205)

- **Système / support d'étude** : palan électrique à chaine (levage industriel, capacité 1000 kg),
  équipé d'un moteur électrique, d'un réducteur à double train épicycloïdal et d'un mécanisme
  frein-limiteur de couple. Bandeau de page : « TRANSMISSION DE PUISSANCE » ; titre du support :
  « Palan électrique à chaine » (p.201).
- **Compétences affichées** : **aucune** sur les pages de présentation p.201 à p.205 (le bandeau ne
  porte pas de pastille CD). Les pastilles **CD 2.2 / CD 3.8** n'apparaissent qu'à partir de la
  p.206 (activités 6.1, 6.2 et Synthèse).
- **Mise en situation** (p.201, § 1) :

  > Le système objet d'étude est un palan électrique à chaine, conçu pour le levage industriel de
  > petite et moyenne capacité (1000 kg). Le palan se combine avec des chariots à déplacement
  > manuel ou électrique installés sur monorail, potence ou pont roulant.

- **Ressources fournies** :
  - p.201 : vue écorchée 3D du palan, légendée **Carter du palan**, **Noix de levage**,
    **Réducteur à double train épicycloïdal**, **Moteur électrique**, **Mécanisme limiteur-frein**,
    **Crochet de levage**, **Chaine calibrée à maillons** ; photo d'un palan complet (corps orange,
    marquage « 1 t », boîtier de commande pendant, crochet et chaine). Deux QR-codes : l'un marqué
    **« Vid »** (vidéo, en haut à droite), l'autre marqué **« PDF »** (en bas à droite).
  - p.202 : tableau de caractéristiques techniques + **schéma cinématique** du palan.
  - p.203 : **dessin d'ensemble** du palan complet (coupe longitudinale), échelle **1:2**,
    cartouche « Palan électrique à chaîne », QR-code **« PDF »**. Note portée sur le dessin :
    « Le guide chaîne n'est pas représenté dans cette vue ». Un maillon de chaine est repéré par
    la légende « Chaine ».
  - p.204 : **dessin d'ensemble de détail** du mécanisme frein-limiteur de couple, échelle **5:4**,
    cartouche « Palan électrique à chaîne / Mécanisme frein-limiteur de couple ». Une cote
    fonctionnelle est annotée **« Jeu »** (jeu axial entre l'électro-aimant (31) et le disque).
  - p.205 : **nomenclature** complète, 40 repères.
- **Données numériques de l'énoncé** (p.202, § 2 « Caractéristiques techniques ») :

  | Puissance | Vitesse de levage | Poids | Charge maximale |
  | --------- | ----------------- | ----- | --------------- |
  | 0.8 KW    | 3.6 m/min         | 27 Kg | 1000 Kg         |

  Composition (p.202) :

  > Le palan électrique à chaine est composé d' :
  > - Un moteur électrique (Pm = 0.8 KW).
  > - Un réducteur à double train épicycloïdal.
  > - Un frein de levage à disque.
  > - Un limiteur de couple.
  > - Une chaine calibrée à maillons d'acier à haute résistance.

- **Description de fonctionnement** (p.202, § 3 — « voir dessin d'ensemble ») :

  > Le réducteur à double train épicycloïdal assure la transmission de mouvement de rotation de
  > l'arbre de transmission (2) à la noix (5) qui entraine la chaine à l'extrémité de laquelle est
  > attachée la charge à soulever.

- **Description du mécanisme frein-limiteur de couple** (p.202, § 4) :

  > Le disque-frein (28) (non magnétique) est en liaison glissière par rapport à l'arbre de
  > transmission (2), grâce à des cannelures. Le reste du frein est lié en rotation par rapport au
  > carter(39).
  >
  > Le ressort (36) maintient en pression (28) sur (26). L'écrou (1) maintient l'ensemble sur (2).
  >
  > Pendant la montée ou la descente, l'électro-aimant (31) est sous tension et il est plaqué sur
  > le disque d'ancrage (29). Les disques (26) et (28) tournent librement et peuvent entraîner en
  > rotation le planétaire (20).
  >
  > Il y a freinage lorsque la bobine n'est plus alimentée et que le ressort (30) repousse (31) et
  > sa garniture (33) sur le disque de frein (28).
  >
  > Si la charge à soulever est excessive, il se produit un glissement entre (28) et (26). Cela
  > permet de préserver l'ensemble du système contre toute rupture intempestive.

- **Schéma cinématique** (p.202, § 5) : schéma linéaire en couleurs, arbre principal horizontal,
  bâti hachuré à gauche. Repères appelés en tête, de gauche à droite :
  **37+38+39**, **5**, **9+10**, **13**, **16+17**, **19**, **20+26**, **28**, **33**, **31** ;
  en flanc droit, deux repères supplémentaires : **30** et **36** (les deux ressorts, dessinés en
  zigzag). Deux légendes en bas : **« Moteur »** (à gauche, sur le bloc d'entrée) et
  **« Chaine »** (en bas à gauche, sur la boucle de chaine reliée au bâti). Le schéma montre
  symétriquement les deux étages de satellites (haut et bas de l'axe), les deux disques
  (frein / limiteur) hachurés en jaune-violet à droite et les deux ressorts.

- **Dessins d'ensemble** (p.203–204) : le dessin d'ensemble p.203 (coupe, échelle 1:2) appelle la
  **totalité des 40 repères** de la nomenclature : à gauche 27, 8, 34, 39, 17, 19, 18, 16, 14, 13,
  12, 11, 10, 9, 7, 6, 5 ; en haut 23, 31, 29, 36, 30, 24, 25 ; à droite 32, 33, 28, 26, 21, 22,
  20, 15, 37, 38 ; en bas 40, 35, 2, 1, 4, 3. Le dessin de détail p.204 (échelle 5:4) n'appelle
  que le mécanisme frein-limiteur : à gauche 39, 34, 28, 2, 20, 26, 33 ; à droite 23, 31, 29, 36,
  1, 30, 32, 24, 25 ; plus la cote **« Jeu »**.

- **Nomenclature** (p.205, § 7) — transcription intégrale :

  | Rep. | Nbr. | Désignation             | Matière               | Observation      |
  | ---- | ---- | ----------------------- | --------------------- | ---------------- |
  | 1    | 2    | Écrou auto-freiné M8    |                       |                  |
  | 2    | 1    | Arbre de transmission   | 35 Cr Mo 4            |                  |
  | 3    | 1    | Rotor (Assemblage)      |                       |                  |
  | 4    | 3    | Roulement BC            |                       | 6004 2RS1        |
  | 5    | 1    | Noix de levage          |                       |                  |
  | 6    | 1    | Roulement BC            |                       | 6005 2RS1        |
  | 7    | 1    | Anneau élastique        |                       |                  |
  | 8    | 1    | Bague de limiteur       |                       |                  |
  | 9    | 1    | Porte satellites 2ème étage |                   |                  |
  | 10   | 3    | Axe porte satellites    | 35 Cr Mo 4            | Serré sur 9      |
  | 11   | 2    | Rondelle                | Cu Sn 8               |                  |
  | 12   | 3    | Bague autolubrifiante   |                       |                  |
  | 13   | 3    | Satellite 2ème étage    |                       | Z13= ?           |
  | 14   | 6    | Rondelle de retenue     |                       | Standard         |
  | 15   | 1    | Planétaire 2ème étage   |                       | Z15= 15 dents    |
  | 16   | 1    | Porte satellites 1er étage |                    |                  |
  | 17   | 3    | Axe porte satellites    | 35 Cr Mo 4            | Serré sur 16     |
  | 18   | 3    | Bague autolubrifiante   |                       |                  |
  | 19   | 3    | Satellite 1er étage     |                       | Z19= 37 dents    |
  | 20   | 1    | Planétaire 1er étage    |                       | Z20 = ?          |
  | 21   | 1    | Joint torique           |                       |                  |
  | 22   | 1    | Roulement BC            |                       | 6005 2RSL        |
  | 23   | 3    | Vis de fixation         |                       |                  |
  | 24   | 3    | Vis de blocage          |                       |                  |
  | 25   | 3    | Écrou de réglage        |                       |                  |
  | 26   | 1    | Disque limiteur +garniture |                    |                  |
  | 27   | 1    | Joint à lèvres          |                       | Standard         |
  | 28   | 1    | Disque frein +garniture | X2 Cr Ni Mo 17-12-2   | Non magnétique   |
  | 29   | 1    | Disque d'ancrage        | S235                  |                  |
  | 30   | 1    | Ressort de frein        | 50 Cr V 4             |                  |
  | 31   | 1    | Electro-aimant          |                       |                  |
  | 32   | 1    | Corps magnétique        |                       |                  |
  | 33   | 1    | Disque fixe de friction |                       |                  |
  | 34   | 3    | Écrou spécial           |                       | Serré sur 33     |
  | 35   | 3    | Rondelle                |                       | Standard         |
  | 36   | 1    | Ressort de limiteur     | 50 Cr V 4             |                  |
  | 37   | 1    | Couronne                |                       | Z37= 89 dents    |
  | 38   | 1    | Carter principal        | EN-GJL-200            |                  |
  | 39   | 1    | Carter secondaire       | EN-GJL-200            |                  |
  | 40   | 1    | Couvercle               | EN-GJL-200            |                  |

- **Vocabulaire & terminologie officielle** : palan électrique à chaine, chariot, monorail,
  potence, pont roulant, noix de levage, crochet de levage, chaine calibrée à maillons, carter
  (principal / secondaire), réducteur à double train épicycloïdal, planétaire, satellite, porte
  satellites, couronne, arbre de transmission, cannelures, liaison glissière, disque-frein,
  disque limiteur, disque d'ancrage, disque fixe de friction, garniture, électro-aimant, bobine,
  corps magnétique, ressort de frein / de limiteur, écrou auto-freiné, écrou de réglage, vis de
  blocage, bague autolubrifiante, joint torique, joint à lèvres, roulement BC, anneau élastique,
  glissement, rupture intempestive.

---

##### Activité 6.1 — Frein - limiteur de couple (p.206–207)

- **Système / support d'étude** : le mécanisme frein-limiteur de couple du palan électrique à
  chaine (dessin d'ensemble p.204, nomenclature p.205).
- **Compétences affichées** : **CD 2.2**, **CD 3.8** (pastille en tête de page p.206 et p.207).
  Pictogrammes de démarche en tête de la p.206 : **« R. PRO »** (silhouette verte) et
  **« CRITI »** (silhouette bleu foncé).
- **Mise en situation — I. Situation déclenchante** (p.206, encadré bleu) :

  > Le palan est équipé d'un mécanisme limiteur-frein pour préserver l'ensemble et l'utilisateur à
  > la fois.
  >
  > **Faisons l'étude de ce mécanisme pour comprendre les phases de fonctionnement pour chaque
  > état.**

- **Ressources fournies** : dessin d'ensemble du mécanisme limiteur-frein (p.204), dessin
  d'ensemble général (p.203), nomenclature (p.205), description du § 4 de la p.202.
- **Données numériques de l'énoncé** :
  - coefficient de frottement **f = 0,4** (p.206, question 7) ;
  - effort presseur du ressort (30) : **F30 = 500 N** (p.206, question 7) ;
  - expression fournie du couple de freinage (p.206, question 7) :
    **C_f = (2/3) . F30 . f.n. (R³ - r³)/(R² - r²)** ;
  - « n », « r » et « R » sont à **relever sur le dessin d'ensemble** (valeurs non données).

- **Travail demandé — II. Travail demandé** :

  **A. Étude de frein** (p.206) — chapeau : « A partir du dessin d'ensemble du mécanisme
  limiteur-frein. »

  1. Quelle est le type de commande de frein ?
  2. Préciser et justifier si le palan est libre ou freiné.
  3. Quelle est la forme des surfaces de contact ?
  4. Déduire le type de ce frein.
  5. Justifier l'utilisation de ce type de frein.
  6. Indiquer les facteurs dont dépend le couple de freinage.
  7. L'expression du couple de freinage est : C_f = (2/3) . F30 . f.n. (R³ - r³)/(R² - r²), le
     coefficient de frottement, f = 0,4 et l'effort presseur du ressort (30), F30 = 500 N.
     En se référant au dessin d'ensemble du mécanisme limiteur-frein.
     - Relever le nombre de surfaces de frottement « n » et les rayons correspondants « r » et
       « R ».  n = …………… ,  r = …………… ,  R = ……………
     - Calculer le couple de freinage :
  8. Expliquer comment peut-on varier le couple de freinage.

  **B. Étude du limiteur de couple** (p.207)

  1. Quelle est l'utilité du limiteur de couple dans ce mécanisme?
  2. Représenter le symbole normalisé d'un limiteur de couple. *(zone de dessin vierge)*
  3. Compléter le tableau des mobilités cinématiques des composants suivants selon les deux
     conditions proposées (L'électro-aimant (31) étant actionné).
     (Par convention : 1 = Mouvement ; 0 = Pas de Mouvement)

     |                           | C < C_nominal | C > C_nominal |
     | ------------------------- | ------------- | ------------- |
     | Arbre de transmission (2) | …             | …             |
     | Disque(28)                | …             | …             |
     | Disque(26)                | …             | …             |
     | Planétaire (20)           | …             | …             |
     | Noix de levage (5)        | …             | …             |

  4. Décrire le fonctionnement si la charge à soulever est excessive.
  5. Quelle opération doit-on effectuer pour augmenter le couple à transmettre ?

- **Vocabulaire & terminologie officielle** : type de commande de frein, palan libre / freiné,
  forme des surfaces de contact, type de frein, couple de freinage, surfaces de frottement,
  coefficient de frottement, effort presseur, limiteur de couple, symbole normalisé, mobilités
  cinématiques, couple nominal (C_nominal), couple à transmettre.

---

##### Activité 6.2 — Train épicycloidal (p.208–210)

- **Système / support d'étude** : le palan électrique à chaine, réducteur à **double train
  épicycloïdal** (dossier technique p.201–205).
- **Compétences affichées** : **CD 2.2**, **CD 3.8** (pastille en tête des p.208, 209 et 210).
  Pictogrammes de démarche en tête de la p.208 : **« R. PRO »** (silhouette verte) et
  **« DECI »** (silhouette violette).
- **Mise en situation — I. Situation déclenchante** (p.208, encadré bleu) :

  > Dans les travaux de manutention industrielle, le palan électrique à chaine est indispensable
  > pour lever et déplacer les charges, ce qui évite tout effort physique du côté des travailleurs.
  >
  > **Comment procède-t-on pour caractériser et vérifier les performances cinématiques du palan
  > dans le cas de fonctionnement normal?**

- **Ressources fournies** : dossier technique du palan (p.201–205), QR-code **« PDF »** (p.208),
  diagramme FAST à compléter (p.208), chaîne de transmission de puissance à compléter (p.209),
  formule de Willis fournie (p.209).
- **Données numériques de l'énoncé** :
  - denture connue par la nomenclature p.205 : **Z15 = 15 dents** (planétaire 2ème étage),
    **Z19 = 37 dents** (satellite 1er étage), **Z37 = 89 dents** (couronne) ;
    **Z13 = ?** et **Z20 = ?** sont les inconnues à calculer ;
  - vitesse de montée de la charge : **V = 3,6 m/min** (p.210) ;
  - primitif d'enroulement de la chaîne sur la noix (5) : **d5 = 42 mm** (p.210) ;
  - puissance du moteur : **Pm = 800 W** (p.210) ;
  - rendement du palan : **η = 0.75** (p.210).

- **Travail demandé — II. Travail demandé** :

  **A. Analyse fonctionnelle** (p.208) — énoncé : « En se référant au dossier technique du palan
  électrique à chaine. Compléter le diagramme FAST descriptif relatif à la fonction principale :
  FP : Déplacer la charge. »

  Diagramme FAST imprimé (une colonne de droite est titrée **« Proceusseurs/Composants »**
  [sic — pour « Processeurs »]) ; les pointillés marquent les cases à compléter par l'élève :

  | Fonction | Sous-fonction | Processeurs/Composants (colonne de droite) |
  | -------- | ------------- | ------------------------------------------ |
  | **FP: Déplacer la charge** | **FT1 : Suspendre le palan** | *(à compléter)* |
  |  | **FT2 : Lever ou descendre la charge** → **FT21 : Convertir l'énergie** → **FT211 : Créer le couple** | *(à compléter)* |
  |  | **FT2** → **FT21** → **FT212 : Adapter le couple** | *(à compléter)* |
  |  | **FT2** → **FT22 : Supporter la charge** | **Crochet + chaine** *(donné)* |
  |  | **FT2** → **FT23 : Entrainer la chaine** | **Noix** *(donné)* |
  |  | **FT3 : Protéger le palan contre les surcharges** | *(à compléter)* |
  |  | **FT4 : Immobiliser la charge** | *(à compléter)* |

  **B. Étude cinématique du palan** (p.209–210)

  1. (p.209) Compléter le cheminement de transmission de puissance ci-dessous du rotor (3) à la
     noix (5).
     Chaîne imprimée sous forme de bulles reliées par des flèches ; les bulles « … » et certaines
     étiquettes de liaison sont à compléter. Structure exacte :
     - **1ère ligne (gauche → droite), 7 bulles** : **(3)** → … → … → … → … → … → … ;
       étiquettes des 6 liaisons, dans l'ordre : **« Cannelure »** (donnée, sous la flèche) ;
       *(pointillés à compléter, au-dessus)* ; **« Adhèrence »** [sic — pour « Adhérence »]
       (donnée, sous la flèche) ; **« Engrènement »** (donnée, sous la flèche) ;
       *(pointillés à compléter, au-dessus)* ; **« (17) »** (donné, au-dessus).
     - **Liaison verticale** de la dernière bulle de la ligne 1 vers la ligne 2 :
       *(pointillés à compléter)*.
     - **2ème ligne (droite → gauche), 4 bulles** : … → … → … → **(5)** ; étiquettes des 3
       liaisons, de droite à gauche : *(pointillés à compléter)* ; **« (10) »** (donné) ;
       *(pointillés à compléter)*.
  2. (p.209) Déterminer la condition géométrique d'engrènement en fonction des diamètres
     primitifs, puis calculer Z20 pour le premier étage et Z13 pour le deuxième étage.
  3. (p.209) Quelle remarque peut-on faire concernant les deux étages?
  4. (p.209) En utilisant la formule de Willis :

     > n_{s/ps} / n_{e/ps} = (n_s − n_ps) / (n_e − n_ps) = (− 1)^k · Produit (Zmenantes) / Produit (Zmenées)
     >
     > Avec : k : Le nombre de contacts extérieurs;
     > n_ps : La vitesse de rotation du porte satellite.

     a. (p.209) Exprimer puis calculer le rapport de transmission du 1er étage :
        Sachant que : La couronne planétaire (37) bloqué ;
        Le pignon planétaire (20) en entrée ;
        Le porte-satellite (16) en sortie.

     b. (p.210) Déduire et calculer le rapport global de transmission.

     c. (p.210) Calculer la vitesse de rotation de la noix (5) N5 sachant que :
        - La vitesse de la montée de la charge V = 3,6 m/min
        - Le primitif d'enroulement de la chaîne sur la noix (5) est d5 = 42 mm.

     d. (p.210) Calculer la vitesse de rotation du moteur N_moteur.

     e. (p.210) Calculer la valeur de la charge maximale à soulever en N sachant que :
        - La puissance de moteur est Pm = 800 W.
        - Le rendement du palan η = 0.75.

- **Vocabulaire & terminologie officielle** : diagramme FAST descriptif, fonction principale (FP),
  fonctions techniques (FT1…FT4, FT21, FT211, FT212, FT22, FT23), processeurs/composants,
  cheminement de transmission de puissance, cannelure, adhérence, engrènement, condition
  géométrique d'engrènement, diamètre primitif, formule de Willis, contacts extérieurs, porte
  satellite, roues menantes / menées, rapport de transmission (d'étage, global), couronne
  planétaire, pignon planétaire, primitif d'enroulement, rendement.

---

##### Synthèse — Transmission de puissance (p.211–215)

- **Compétences affichées** : **CD 2.2**, **CD 3.8** (pastille en tête des p.211 à 215).
- **Structure de la synthèse** : bandeau « **Synthèse** » (p.211), puis
  « **1. Auto-évaluation** » et « **2. Synthèse assemblage** » [sic — le titre annonce
  « assemblage » alors que la synthèse porte sur la transmission de puissance] ; sous ce dernier,
  la numérotation repart à 1 et court jusqu'à 5 (p.211 → p.215), suivie de l'espace
  « **Savoirs plus** » et de la mention finale « **Grille d'évaluation des savoirs et
  savoir-faire de l'apprenant** » (p.215, avec QR-code « PDF »).

**1. Auto-évaluation** (p.211) :

> Tester vos connaissances avant de passer à la synthèse avec les Quiz.

Deux QR-codes marqués **« EXE »** : **« QUIZ transmission de puissance »** (libellé surligné en
jaune) et **« QUIZ transformation de mouvement »**.

**2. Synthèse assemblage** — encadré de synthèse, verbatim (p.211–215) :

> **1. Fonction transmission de puissance**
>
> La transmission d'une puissance est la fonction la plus usuelle des chaînes mécaniques. Il
> s'agit d'entraîner un arbre récepteur à partir d'un arbre moteur plus ou moins éloigné par des
> moyens de transmission (engrenages, poulies -courroie, pignons et chaine, embrayage…).
>
> **2. Quelques notions**
>
> **a. Puissance P**
>
> La puissance est exprimée en Watt ; 1 Watt = 1 joule / 1 seconde = 1j / 1s ou j.s⁻¹
>
> Elle est exprimée aussi en cheval ; 1 cv = 736 W.
>
> - Puissance développée par une force : P = **F** . **V** *(F et V surmontés d'une flèche de
>   vecteur)* ; Avec P en (watt) ; F en (N) ; V en (m/s).
> - Puissance développée par un couple : P = C. ω ; avec P : puissance en (W) ; C : couple en
>   (Nm) ; ω : vitesse angulaire en (rad.s⁻¹) ; ω = 2.π.N / 60 ; N : vitesse de rotation en tr/min
>
> **b. Rendement ŋ** [sic — glyphe imprimé à la place de η]
>
> - Pour une énergie; η = Ws / We ; Ws : énergie de sortie et We : énergie d'entrée.
> - Pour une puissance ; η = Ps / Pe ; Ps : puissance de sortie et Pe : puissance d'entrée
>
> **3. Transmission de puissance sans transformation de mouvement**

Organigramme (p.211) — « **Transmission sans transformation de mouvement** » se divise en deux
branches :

| Branche | Familles listées |
| ------- | ---------------- |
| **Sans modification de vitesses angulaire** [sic] | Accouplements · Embrayages · Limiteurs de couples · Freins |
| **Avec modification de vitesses angulaire** [sic] | Boite de vitesses · Trains épicycloïdaux · … |

> **a. Les accouplements** *(p.212)*
>
> On distingue généralement 3 familles d'accouplements :
>
> - Rigides de symbole *(symbole imprimé : un rectangle traversé par l'arbre, contenant deux
>   traits verticaux barrés chacun d'une croix)*
> - Élastiques de symbole *(rectangle traversé par l'arbre, contenant deux traits verticaux reliés
>   par une diagonale montante)*
> - Flexibles de symbole *(même motif que l'élastique, le cadre du rectangle étant ouvert /
>   dégradé en bas à gauche)*
>
> **b. Les embrayages**
>
> L'embrayage a pour but de transmettre à volonté la puissance d'une partie motrice à une partie
> réceptrice. On distingue deux types : progressif et instantané.
>
> - **Symbole** *(rectangle traversé par l'arbre, avec deux courts traits horizontaux affrontés
>   au centre — les deux plateaux)*
> - **Couple transmissible par un embrayage à friction plane**
>
>   Ct = (2/3) . n . f . **N** . (R³ − r³) / (R² − r²)
>   *(la formule imprime « N » là où la légende ci-dessous définit « F » — voir § Incertitudes)*
>
>   ; Ct : Couple transmissible en N.m ; F : Effort presseur des surfaces de friction en N ;
>   f : Coefficient de frottement ; n : Nombre de surface de friction ; R : Rayon extérieur du
>   disque de friction en mètre ; r : Rayon intérieur du disque de friction en mètre.
>
>   *(Figure d'accompagnement : disque de friction vu de face, couronne rouge extérieure sur fond
>   bleu, cotée par deux flèches partant du centre — le rayon extérieur R et le rayon intérieur
>   r.)*
>
> - **Couple transmissible par un embrayage à friction conique**
>
>   C_t = (2/3) . (F / sinα) . f. R_moy   avec R_moy = (R³ − r³) / (R² − r²)
>
>   *(Figure d'accompagnement : demi-coupe d'un cône de friction, cotée R (rayon extérieur) et
>   r (rayon intérieur), axe en trait mixte.)*
>
> **c. Limiteurs de couple**
>
> La transmission est interrompue en cas de dépassement du couple préréglé.
>
> - **Symbole** *(rectangle traversé par l'arbre, deux traits verticaux affrontés au centre reliés
>   par un trait horizontal supérieur, et cadre interrompu au milieu en haut et en bas)*
> - **Couple transmissible par un limiteur de couple**
>
>   C_t = (2/3) . F . f. (R³ − r³) / (R² − r²)
>
> **d. Les freins**
>
> Le frein a comme fonction de ralentir ou arrêter un organe (un mécanisme) en mouvement.
>
> - **Symbole** *(arbre horizontal se terminant par un T, une flèche verticale descendante
>   appuyant sur la mâchoire, et à droite un cercle marqué « + » représentant le disque/tambour)*
> - **Couple de freinage (frein à disque)**
>
>   C_f = (2/3) . F . n . f. (R³ − r³) / (R² − r²)
>
> **e. Rapport de transmission par engrenage ordinaire** *(p.213)*
>
> r = (− 1)^k . Produit des Z menantes / Produit des Z menées
>
> **f. Rapport de transmission par trains épicycloïdaux**
>
> Un train d'engrenages est dit épicycloïdal quand, pendant le fonctionnement, une ou plusieurs
> roues dentées (appelées satellites) tournent autour d'axes qui ne sont pas fixes par rapport au
> bâti.
>
> Le rapport dépend de la partie bloquée pendant le fonctionnement.

Tableau des trois cas (p.213) — chaque colonne porte un schéma cinématique du même train
(planétaire 1, satellite 3, planétaire/couronne 4, porte-satellites PS), la partie bloquée étant
reliée au bâti hachuré :

| Planétaire (4) bloqué | Planétaire (1) bloqué | Porte-satellites (PS) bloqué |
| --------------------- | --------------------- | ---------------------------- |
| Schéma : repères 4 (bloqué, relié au bâti), PS, 3, 1 | Schéma : repères 1 (bloqué, relié au bâti), PS, 3, 4 | Schéma : repères PS (bloqué, relié au bâti), 4, 3, 1 |
| ω_{ps/4} / ω_{1/4} = Z₁ / (Z₁ + Z₄) | ω_{ps/1} / ω_{4/1} = Z₄ / (Z₁ + Z₄) | ω_{4/ps} / ω_{1/ps} = − Z₁ / Z₄ |

> **4. Transmission de puissance avec transformation de mouvement.**

Organigramme (p.213) — « **Transmission avec transformation de mouvement** » se ramifie en :
Système vis écrou · Excentrique · Cames · Bielle manivelle · Pignon crémaillère · Liens flexibles.

> **a. Système vis écrou**
>
> Pour une rotation θ de la vis on a un déplacement "x" de l'écrou :  x = (P / 2π) . θ
>
> **b. Excentrique**
>
> La course C = 2.e ; « e » est la valeur de l'excentricité.
>
> **c. Cames**
>
> On distingue 3 familles de type de cames (à disque, à tambour, à rainure).
>
> **d. Bielle-manivelle** *(p.214)*
>
> La course C = 2.R ; « R » est le rayon de la manivelle.
>
> *(Figure : schéma cinématique du système bielle-manivelle dans un repère (x, y) ; repères 1
> (manivelle), 2 (bielle), 3 (coulisseau/piston), 0 (bâti hachuré) ; points O (axe de rotation),
> A (maneton) et B (axe du piston) ; angle α entre OA et l'axe x ; annotations imprimées :
> « Rayon manivelle R = OA », « Longueur bielle L = AB », « Course C = 2R ».)*
>
> **e. Pignon-crémaillère**
>
> - **Déplacement linéaire**
>
>   Le déplacement linéaire "x" de la crémaillère pour une rotation θ en degrés : x = R .θ
>
> - **Vitesse linéaire V**   V = (d / 2) . ω = R . ω
>
> *(Figure : pignon denté (légendé « Pignon ») engrenant sur une crémaillère (légendée
> « Crémaillère ») ; ω, flèche de rotation rouge sur le pignon ; V, flèche de translation rouge
> horizontale.)*
>
> **f. Liens flexibles**
>
> Les liens flexibles sont soit une courroie avec poulies, soit une chaine avec pignons.
>
> La vitesse de déplacement linéaire d'un point du lien est :
>
> V = (d / 2) . ω = R . ω
>
> *(Photo d'accompagnement : module de translation à courroie crantée et chariot.)*
>
> **5. Machines thermiques**
>
> Une machine thermique est un convertisseur d'énergie qui permet de transformer l'énergie
> thermique en énergie mécanique ou inversement.

Schéma (p.214) : **Puissance thermique** ⟷ **Machines thermiques (Convertisseur)** ⟷ **Puissance
mécanique** (double flèche de part et d'autre du bloc central).

> **a. Moteur à explosion**
>
> - **Moteur 4 temps:** Le cycle de fonctionnement comporte quatre phases: Admission, compression,
>   détente et échappement.
> - **Moteur 2 temps:** Le cycle de fonctionnement comporte uniquement deux temps. En effet les
>   phases admission, compression et échappement du cycle 4 temps sont faites en même temps.
>
> - **Cylindrée** *(p.215)*
>
>   La cylindrée unitaire V :  V = (π . D²) / 4 . L
>
>   La cylindrée totale C : C = V.n (en mm³);
>   Avec D : diamètre du cylindre, nommé alésage : (souvent exprimé en mm) ;
>   L : la course, (souvent exprimée en mm);
>   n : nombre de cylindre.

Encadré-figure d'accompagnement (p.215, à droite) :

> **La cylindrée**
>
> **Définition:** La cylindrée est le volume décrit par une course du piston

*(Figure : piston au PMH et au PMB dans son cylindre, la « Course » cotée entre les deux
positions, puis le volume balayé représenté par un cylindre bleu coté « D » (diamètre) et
« Course » ; formule portée sous la figure : « Cylindrée = π.D⁴/4 · course » [sic — exposant 4
imprimé au lieu de 2].)*

**Savoirs plus** (p.215) :

> **Savoirs plus** (espace réservé pour les remarques, astuces, conseils… à rédiger par
> l'apprenant)

*(Suivent environ 25 lignes de pointillés vierges, puis, en pied de page, la mention
« Grille d'évaluation des savoirs et savoir-faire de l'apprenant » accompagnée d'un QR-code
« PDF ».)*

- **Vocabulaire & terminologie officielle de la synthèse** : chaîne mécanique, arbre moteur /
  arbre récepteur, moyens de transmission, puissance (watt, cheval), joule, couple, vitesse
  angulaire, vitesse de rotation, rendement, transmission sans / avec transformation de mouvement,
  accouplement (rigide, élastique, flexible), embrayage (progressif, instantané ; friction plane,
  friction conique), effort presseur, surfaces de friction, coefficient de frottement, rayon
  extérieur / intérieur, rayon moyen, limiteur de couple, couple préréglé, frein à disque, couple
  de freinage, rapport de transmission, roues menantes / menées, train épicycloïdal, satellite,
  planétaire, porte-satellites, bâti, système vis-écrou, excentricité, came (à disque, à tambour,
  à rainure), bielle-manivelle, manivelle, course, pignon-crémaillère, liens flexibles, courroie,
  poulie, machine thermique, convertisseur d'énergie, moteur à explosion 4 temps / 2 temps,
  admission, compression, détente, échappement, cylindrée unitaire / totale, alésage, PMH, PMB.

##### Bornes de scope observées — p.201–215

- ✅ INCLUS :
  - Dossier technique complet d'un palan électrique à chaine 1000 kg : mise en situation,
    caractéristiques (0.8 KW, 3.6 m/min, 27 Kg, 1000 Kg), description de fonctionnement,
    description littérale du mécanisme frein-limiteur, schéma cinématique, deux dessins d'ensemble
    (1:2 et 5:4) et nomenclature de 40 repères avec matières et observations (p.201–205).
  - Étude d'un **frein à disque à commande électromagnétique** : type de commande, état
    libre/freiné, forme des surfaces de contact, type de frein, justification, facteurs dont
    dépend le couple de freinage, **calcul numérique** du couple de freinage à partir de
    C_f = (2/3).F30.f.n.(R³−r³)/(R²−r²) avec f = 0,4 et F30 = 500 N, et moyens de le faire varier
    (p.206).
  - Étude d'un **limiteur de couple à friction** : utilité, symbole normalisé, tableau de mobilités
    cinématiques sous les deux régimes C < C_nominal et C > C_nominal, description du
    fonctionnement en surcharge, réglage pour augmenter le couple transmissible (p.207).
  - **Analyse fonctionnelle** : complètement d'un diagramme FAST descriptif (FP + FT1 à FT4,
    FT21/FT211/FT212, FT22, FT23) et de sa colonne processeurs/composants (p.208).
  - **Cinématique du train épicycloïdal** : chaîne de transmission de puissance à reconstituer du
    rotor (3) à la noix (5), condition géométrique d'engrènement en diamètres primitifs, calcul de
    Z20 et Z13, **formule de Willis** appliquée à un train à couronne bloquée, rapport d'étage puis
    rapport global, N5 à partir de V = 3,6 m/min et d5 = 42 mm, N_moteur, charge maximale en N à
    partir de Pm = 800 W et η = 0.75 (p.209–210).
  - **Synthèse du thème** : puissance (P = F.V, P = C.ω, ω = 2πN/60, 1 cv = 736 W), rendement
    (énergie et puissance), classement des transmissions sans transformation de mouvement
    (accouplements, embrayages, limiteurs, freins / boîte de vitesses, trains épicycloïdaux),
    symboles normalisés, couples transmissibles (embrayage plan, embrayage conique, limiteur) et
    couple de freinage, rapport d'engrenage ordinaire, **les trois cas de train épicycloïdal**
    (planétaire 4 bloqué, planétaire 1 bloqué, PS bloqué) ; transformations de mouvement
    (vis-écrou, excentrique, cames, bielle-manivelle, pignon-crémaillère, liens flexibles) ;
    machines thermiques, moteurs 4 et 2 temps, cylindrée unitaire et totale (p.211–215).
- ⛔ EXCLU / seulement mentionné :
  - Les **quiz d'auto-évaluation** (« QUIZ transmission de puissance », « QUIZ transformation de
    mouvement ») et la **grille d'évaluation des savoirs et savoir-faire de l'apprenant** ne sont
    **pas imprimés** : ils ne sont accessibles que par QR-code (p.211, p.215).
  - Les ressources numériques appelées par QR-code « Vid » (p.201) et « PDF » (p.201, p.203,
    p.208, p.215) ne sont pas reproduites dans le manuel.
  - Le **guide chaîne** est explicitement écarté du dessin d'ensemble : « Le guide chaîne n'est pas
    représenté dans cette vue » (p.203).
  - Les **cames** sont seulement citées par familles (à disque, à tambour, à rainure) — aucune loi
    de levée, aucun profil, aucun diagramme (p.213).
  - Les **machines thermiques** ne vont pas au-delà de la définition, des phases des cycles 4 et
    2 temps et des formules de cylindrée : ni diagramme (P,V), ni rendement thermodynamique, ni
    couple/puissance moteur (p.214–215).
  - Les **boîtes de vitesses** apparaissent uniquement comme une case de l'organigramme (p.211) ;
    aucune étude ne leur est consacrée dans la synthèse.
  - Le **symbole normalisé du limiteur de couple** demandé en 6.1-B.2 (p.207) n'est pas donné sur
    la page : la case est vierge (l'élève doit le tracer) ; il figure en revanche dans la synthèse
    (p.212).
  - La **couche « corrigé »** n'existe pas : toutes les questions des activités 6.1 et 6.2, ainsi
    que les cases du FAST, de la chaîne de transmission et du tableau de mobilités, sont laissées
    en pointillés à remplir.
  - Le paragraphe « **Savoirs plus** » (p.215) est un espace vierge réservé à l'apprenant, sans
    contenu imprimé.

#### Thème : COMPORTEMENT DES SOLIDES DÉFORMABLES (p.216–251)

**Page d'ouverture du thème (p.216)** — bandeaux successifs, transcrits tels qu'imprimés :

> **AXE 2**
> **ANALYSE STRUCTURELLE ET CONCEPTION**
>
> **THÈME**
> **COMPORTEMENT DES SOLIDES DÉFORMABLES**
>
> **SÉQUENCE**
> - Torsion simple
> - Flexion plane simple
> - Sollicitations composées
>
> **COMPOSANTES DES COMPÉTENCES DISCIPLINAIRES**
> CD 1.7: Retrouver les différentes sollicitations que subit un solide.
> CD 2.1: Dimensionner un composant mécanique et vérifier sa résistance.

Tableau « Carte du manuel » en bas de la p.216, intitulé **Comportement des solides déformables** :

| CD | Savoirs et savoir-faire | Critères d'évaluation |
| --- | --- | --- |
| CD 1.7 | **Torsion simple:** - Essai - Contrainte. - Condition de résistance. - Condition de rigidité. | - Détermination correcte des différentes types de sollicitations |
| CD 2.1 | **Flexion plane simple:** - Essai. - Contraintes. - Efforts tranchants. - Moments fléchissant. - Condition de résistance. **Sollicitations composées**: Condition de résistance. | - Dimensionnement correct d'un composant. - Vérification correcte de la résistance d'un composant. - Maitrise convenable des logiciels de calcul. |

*(Note : la répartition CD 1.7 / CD 2.1 des lignes du tableau est celle des deux cellules fusionnées imprimées ; « Condition de rigidité » est typographiquement rattachée au bloc CD 1.7, la suite au bloc CD 2.1.)*
Un QR-code marqué **PDF** figure en bas à droite de la p.216.

**Bandeaux d'en-tête (repères de lecture)** : p.217–221 « TORSION SIMPLE » ; p.222–226 « FLEXION PLANE SIMPLE » ; p.227–251 « COMPORTEMENT DU SOLIDE DEFORMABLE ». Les badges **CD 1.7 / CD 2.1** apparaissent en angle haut-gauche des pages de travail (p.219–221, 223–226, 229–232, 234–238, 242–244, 247–251) et sont absents des pages de présentation (p.216–218, 222, 227–228, 233, 239–241, 245–246).

---

##### Activité 1 — Banc d'essai de torsion (p.217–221)

- **Système / support d'étude** : banc d'essai de torsion (banc didactique à colonnes, éprouvette cylindrique horizontale, levier + mâchoires, comparateur à cadran, charge suspendue).
- **Compétences affichées** : CD 1.7 et CD 2.1 (imprimées en tête des p.219, 220, 221 ; les p.217–218 de présentation ne portent pas de badge). Pictogrammes de démarche en tête de la p.219 : **COOP** et **R. PRO**.
- **Mise en situation (p.217, verbatim)** :

  > Ce banc d'essai est destiné à :
  > - Étudier expérimentalement le comportement mécanique d'éprouvettes cylindriques sollicitées en torsion pure à partir de courbe moment de torsion/rotation axiale ;
  > - Étudier l'évolution des contraintes induites par la sollicitation de torsion dans l'éprouvette durant la phase de chargement (application du moment de torsion) et d'identifier expérimentalement la contrainte tangentielle.
  > - Déterminer le module d'élasticité transversale G d'un matériau.

- **Ressources fournies** :
  - **Photo-rendu 3D du banc (p.217)** : bâti bleu à deux montants reliés par deux colonnes cylindriques ; l'éprouvette (tige dorée) traverse le banc de part en part ; repères d'annotation **Comparateur à cadran**, **Eprouvette** [sic, sans accent], **Charge** (masse cylindrique suspendue à un levier coudé).
  - **Dispositif de l'essai (p.217, § 2)** — liste du matériel :
    - Banc d'essai ;
    - Support de charge (2,5 N) ;
    - 02 Masses de 5 N ;
    - 01 Masse de 10 N ;
    - 03 Éprouvettes métalliques de diamètre 8 mm, en acier, aluminium et laiton de longueur 600 mm.
    - Comparateur à cadran + support.
    - Pieds à coulisse au 1/50 + réglet.
  - **Dessin d'ensemble de l'appui support levier (p.218, § 3)** : à gauche une vue 3D annotée **Levier**, **Colonne**, **Eprouvette**, **Bouton de réglage** ; à droite une **coupe** en dessin technique de l'appui, avec les repères de nomenclature **1** à **6** en flèches (1 en haut à droite, puis 4, 5, 6 sur la droite ; 2 et 3 sur la gauche) et l'indication **Eprouvette**.
  - **Vue éclatée en 3D du levier et mâchoires (p.218, § 4)** : arbre-levier, **Mâchoire porte éprouvette**, **Mâchoire de fixation**, **Vis de pression**, roulement et anneau élastique, deux vis à tête cylindrique à six pans creux.
  - **Nomenclature (p.218, § 5)** — les colonnes *Matière* et *Observation* sont imprimées **vides** (à compléter par l'élève) :

    | Rep. | Nbr. | Désignation | Matière | Observation |
    | --- | --- | --- | --- | --- |
    | 1 | 1 | Portée réglable | *(vide)* | *(vide)* |
    | 2 | 1 | Appui | *(vide)* | *(vide)* |
    | 3 | 2 | Vis à tête cylindrique à six pans creux | *(vide)* | *(vide)* |
    | 4 | 1 | Roulement | *(vide)* | *(vide)* |
    | 5 | 1 | Anneau élastique pour arbre | *(vide)* | *(vide)* |
    | 6 | 1 | Mâchoire porte éprouvette | *(vide)* | *(vide)* |

  - **Schéma de principe de l'essai (p.219 et p.221, en marge)** : éprouvette cylindrique encastrée à gauche dans un bloc, de longueur repérée **x** ; à l'extrémité libre, un levier de longueur **r** portant la force **F** verticale descendante ; l'angle **α** repère la rotation de la section d'extrémité.

- **Données numériques de l'énoncé** :
  - Éprouvettes : diamètre **8 mm**, longueur **600 mm**, matériaux **acier, aluminium, laiton**.
  - Charges disponibles : support de charge **2,5 N** ; 2 masses de **5 N** ; 1 masse de **10 N**.
  - § 1 (p.219) : portées de fixation réglées à **x = 600 mm** ; charges du tableau **F = 2,5 ; 5 ; 7,5 ; 10 N**.
  - § 2 (p.220) : éprouvette **en aluminium**, charge **12.5 N (2.5 + 10)** ; longueurs **x = 500, 400, 300, 200 mm**.
  - § 3 (p.221) : portées réglées à **X = 500 mm** ; charges **F = 7.5 ; 12.5 ; 17.5 ; 22.5 N**.
  - Table des valeurs théoriques (p.221) : **G_th (GPa)** — Acier **80**, Laiton **37**, Aluminium **28**.
  - § 4 (p.221) : **Mt = 1608 N mm** ; **Reg = 48 N/mm²** ; **s = 3** ; poutre en **aluminium**.
  - Conversion de lecture répétée trois fois : **1 tour de l'aiguille du comparateur correspond à 1°**.

- **Situation déclenchante (p.219, encadré, verbatim)** :

  > Comment reconnaître les grandeurs qui permettent de déterminer :
  > - La résistance d'une poutre en torsion simple
  > - Le rapport entre le moment de torsion (Mt) et l'angle de rotation d'une section circulaire de trois éprouvettes (acier, laiton et  aluminium),.
  > - La résistance et la rigidité d'un composant sollicitée à la torsion ?

- **Consignes de sécurité (p.219, encadré, verbatim)** :

  > **Consignes de sécurité**
  > Vérifier les consignes de sécurité à respecter relativement à cette activité.

- **Travail demandé** :

  1. **(p.219) 1. Relation entre le moment de torsion (M_t) et l'angle relatif de torsion (α) — Éprouvette en acier.** Démarche imprimée :
     - Régler les portées de fixation sur support à x = 600 mm.
     - Placer une éprouvette à travers les éléments de fixation et la bloquer dans la portée fixe.
     - Fixer l'autre bout dans la machoire [sic].
     - Régler le dispositif de mesure de sorte que l'extrémité du comparateur soit exactement en face de l'entaille du levier.
     - Baisser le comparateur et régler l'aiguille à zéro en tournant son anneau extérieur.
     - Varier la charge comme c'est indiqué dans le tableau suivant ; relever l'angle relatif de torsion (α) et déterminer le moment de torsion correspondant.
     - **Remarque : 1** *tour de l'aiguille de comparateur correspond à 1°.*

     **Tableau de mesures** (à compléter) :

     | Charge F (N) | Moment de torsion Mt (N.mm) | Angle relatif de torsion α en (°) |
     | --- | --- | --- |
     | 2,5 | .................. | .................. |
     | 5 | .................. | .................. |
     | 7,5 | .................. | .................. |
     | 10 | .................. | .................. |

     **Tracer la courbe Mt = f(α)** — grille vierge, axe des ordonnées **Mt (N.mm)**, axe des abscisses **α (°)**, origine 0.

  2. **(p.220, haut) Interprétation et conclusion** : ................... (4 lignes pointillées à compléter).

  3. **(p.220) 2. Étude de la déformation angulaire.** « Dans cette partie, on étudie la dépendance de l'angle relatif de torsion de la longueur de l'éprouvette. » Démarche imprimée :
     - Placer une éprouvette en aluminium à travers les éléments de fixation et la bloquer dans la portée fixe.
     - Fixer l'autre bout dans la mâchoire.
     - Régler le dispositif de mesure de sorte que l'extrémité du comparateur soit exactement en face de l'entaille du levier.
     - Baisser le comparateur et régler l'aiguille à zéro.
     - Charger l'éprouvette avec 12.5N (2.5 + 10).
     - Varier la longueur de l'éprouvette comme c'est indiqué dans le tableau.
     - Relever l'angle relatif de torsion pour chaque longueur.
     - **N.B. :** *1 tour de l'aiguille du comparateur correspond à 1°*

     **a. Tableau de mesures** :

     | Longueur x (mm) | Angle relatif de torsion α en (°) |
     | --- | --- |
     | 500 | ................... |
     | 400 | ................... |
     | 300 | ................... |
     | 200 | ................... |

     **Tracer la courbe α = f(x)** — grille vierge, ordonnée **α (°)**, abscisse **x (mm)** graduée 0, 100, 200, 300, 400, 500, 600 ; mention **Echelle : 0,1° → 1mm**.

  4. **(p.220) b. Conclusion** : ................... (4 lignes à compléter).
  5. **(p.220) c. Déduire la valeur de l'angle unitaire de torsion pour le matériau proposé** (2 lignes à compléter).
  6. **(p.221) 3. Détermination du module d'élasticité transversale G — a. Démarche** :
     - Choisir une éprouvette, mesurer son diamètre puis calculer le moment quadratique polaire de la section I₀ ;
       **d = ................ ; I₀ = ................ ;**
     - Régler les portées de fixation sur support à **X = 500 mm** ;
     - Mesurer la longueur du levier **r = ................** ;
     - Varier l'intensité de la charge et completer [sic] le tableau suivant.
     - **N.B. :** *1 tour de l'aiguille du comparateur correspond à 1°.*

     **Tableau (p.221)** — colonnes imprimées : *Valeur de F (N)* | *r (mm)* | *Valeur de Mt (N.mm)* | *Angle relatif de torsion α (°)* | *Module d'élasticité transversale* → sous-colonnes *G (N/mm²)* et *G moyen (N/mm²)* :

     | Valeur de F (N) | r (mm) | Valeur de Mt (N.mm) | Angle relatif de torsion α (°) | G (N/mm²) | G moyen (N/mm²) |
     | --- | --- | --- | --- | --- | --- |
     | 7.5 | (cellule unique fusionnée : ..............) | .............. | .............. | .............. | (cellule unique fusionnée : ..............) |
     | 12.5 | | .............. | .............. | .............. | |
     | 17.5 | | .............. | .............. | .............. | |
     | 22.5 | | .............. | .............. | .............. | |

  7. **(p.221) b.** Donner l'expression du module d'élasticité transversale « G ». (2 lignes)
  8. **(p.221) c.** Compléter le tableau ci-dessus et déduire la valeur moyenne de G, **G_moyen**.
  9. **(p.221) d.** Comparer la valeur de **G_moyen** trouvée avec celle théorique.

     | Matière | Acier | Laiton | Aluminium |
     | --- | --- | --- | --- |
     | G_th (GPa) | 80 | 37 | 28 |

  10. **(p.221) 4. Calculer le diamètre (d) d'une poutre en aluminium pour qu'elle résiste en toute sécurité.** Sachant que :
      - Moment de torsion **Mt = 1608 N mm**.
      - Limite élastique au cisaillement **Reg = 48 N/mm²**.
      - Coefficient de sécurité **s = 3**.

- **Encadrés officiels (verbatim)** : les deux encadrés de cette activité sont la *Situation déclenchante* (p.219) et les *Consignes de sécurité* (p.219), déjà transcrits ci-dessus. Aucun encadré de cours/formule n'est donné dans l'activité 1 : les formules correspondantes sont renvoyées à la Synthèse (p.250).

- **Vocabulaire & terminologie officielle** : torsion pure / torsion simple, éprouvette, moment de torsion (Mt), angle relatif de torsion (α), angle unitaire de torsion, module d'élasticité transversale (G), moment quadratique polaire de la section (I₀), portée réglable, mâchoire porte éprouvette, comparateur à cadran, limite élastique au cisaillement (Reg), coefficient de sécurité (s), condition de résistance, condition de rigidité.

---

##### Activité 2 — Banc d'essais de flexion (p.222–226)

- **Système / support d'étude** : banc d'essais de flexion (même bâti bleu à deux montants et deux colonnes que le banc de torsion ; éprouvette posée sur deux appuis A et B, comparateur à cadran au milieu, charges suspendues).
- **Compétences affichées** : CD 1.7 et CD 2.1 (p.223 à 226). Pictogrammes en tête de la p.223 : **COOP** et **R. PRO**.
- **Mise en situation (p.222, verbatim)** :

  > Le banc d'essai permet :
  > - D'identifier la relation entre les efforts appliqués sur une poutre sollicitée en flexion et les déformations correspondantes.
  > - D'identifier les relations entre les dimensions de la poutre ainsi que la portée (distance entre les appuis) et la déformée.

- **Ressources fournies** :
  - **Photo-rendu 3D du banc (p.222)** : éprouvette plate posée sur deux appuis mobiles le long des colonnes, comparateur à cadran monté sur potence au milieu, masses cylindriques suspendues.
  - **Conditions de réalisation et moyens (p.222, § 2)** :
    - Banc d'essais de flexion
    - Support de charges de poids 2,5 N
    - Deux masses de poids 5 N
    - Une masse de poids 10 N
    - Trois éprouvettes en acier de sections différentes.
    - Trois éprouvettes métalliques (acier, aluminium et laiton) de section circulaire de diamètre 8 mm et de longueur 600 mm.
  - **Schéma de l'essai (p.223)** : poutre horizontale sur appui articulé en **A** (à gauche) et appui à rouleaux en **B** (à droite) ; charge **F** verticale descendante au milieu via un sabot ; comparateur au milieu mesurant la flèche **f** ; portée cotée **L** entre A et B ; déformée en pointillés.
  - **Quatre schémas de portée variable (p.224)** : mêmes appuis A et B, charge F centrale, cotes **200 mm**, **300 mm**, **400 mm**, **500 mm**, chacun avec la lecture **f = ...........**
  - **Schéma de l'étude théorique (p.225)** : poutre sur appuis **A** (articulé) et **B** (rouleaux), point **C** intermédiaire ; cotes **AC = 200 mm** et **CB = 300 mm** ; force **F** verticale descendante appliquée en C.
  - **Grilles de tracé vierges** : f(F) (p.223, ordonnée f (mm), abscisse F (N)) ; f(L) et f(L³) (p.224, ordonnée f (mm) graduée 0,1 / 0,2 / 0,3 / 0,4, abscisses L (mm) graduée 100…600 et L³ (mm³)).
  - **Logiciel** : « Winflex » (simulation, p.226).

- **Données numériques de l'énoncé** :
  - Charges disponibles : support **2,5 N**, deux masses de **5 N**, une masse de **10 N**.
  - Éprouvettes : trois en acier de sections différentes ; trois de section circulaire **Ø 8 mm**, longueur **600 mm** (acier, aluminium, laiton).
  - § A.1 (p.223) : distance entre appuis **A et B = 400 mm** ; charges **F = 5, 10, 15, 20 N**.
  - § A.2 (p.224) : masse de poids **10 N** ; **L = 200, 300, 400, 500 mm** ; **F = 10 N**.
  - § B (p.225) : poutre **de section circulaire pleine d = 8 mm**, **acier**, **Re = 240 MPa**, **E = 210 GPa**, **s = 3**, **F = 15 N** appliquée en C, **AC = 200 mm**, **CB = 300 mm**.
  - § 3 (p.226) : poutre en acier de section circulaire pleine **d = 8 mm**.

- **Situation déclenchante (p.223, encadré, verbatim)** :

  > Étudions expérimentalement le comportement d'une poutre soumise à des charges variables sollicitée à la flexion simple.
  >
  > **Comment peut-on déterminer et vérifier les conditions de résistance et de déformation?**

- **Consignes de sécurité (p.223, verbatim)** :

  > **Consignes de sécurité**
  > Vérifier les consignes de sécurité à respecter relatives à cette activité.

- **Travail demandé** :

  **A. Étude de la flèche**

  1. **(p.223) 1. Relation entre l'intensité de la charge et la flèche : f = f (F).** Démarche :
     - Choisir une éprouvette, relever les dimensions de la section (b et h) puis calculer le moment quadratique **I_GZ** ;
       **b = ................ ; h = ................ ; I_GZ = ................ ;**
     - Régler la distance entre les appuis A et B à 400 mm.
     - Placer l'éprouvette sur les deux appuis A et B et positionner la charge F au milieu
     - Placer le comparateur de sorte que son palpeur soit au milieu de l'éprouvette.
     - Mesurer la flèche et reporter le résultat pour chaque valeur de la charge dans le tableau suivant:

     | Charge F (N) | 5 | 10 | 15 | 20 |
     | --- | --- | --- | --- | --- |
     | Flèche f (mm) | .......... | .......... | .......... | .......... |

     - Tracer le diagramme f(F)
     - **Interprétation et conclusion :** (6 lignes à compléter)

  2. **(p.224) 2. Dépendance de la portée de la flèche : f = f(L).**
     - Utiliser une éprouvette de section rectangulaire mise à plat.
     - Utiliser une masse de poids 10N
     - **a.** Faire varier la distance « L » comme indiqué dans les figures suivantes et relever la valeur de la flèche correspondante indiquée par le comparateur. *(quatre figures cotées 200 / 300 / 400 / 500 mm, chacune avec « f = ........... »)*
     - **b.** Compléter le tableau suivant :

       **F = 10 N**

       | L (mm) | 200 | 300 | 400 | 500 |
       | --- | --- | --- | --- | --- |
       | L³ (mm³) | .......... | .......... | .......... | .......... |
       | f (mm) | .......... | .......... | .......... | .......... |
       | f/L | .......... | .......... | .......... | .......... |
       | f/L³ | .......... | .......... | .......... | .......... |

     - **c.** Tracer les deux courbes f(L) et f(L³)
     - **d. (p.225)** En se référant aux courbes choisir la formule adéquate en cochant la bonne réponse. *(quatre cases à cocher ; « k étant une constante »)*
       - f = k/L³ ☐
       - f = k.L³ ☐
       - f = k/L ☐
       - f = k.L ☐

  **B. Validation des résultats théoriques et de simulation par l'expérimentation sur le banc d'essai de flexion. (p.225)**

  Énoncé (verbatim) : « On se propose de vérifier les résultats théoriques et de simulation par un essai de flexion d'une poutre de section circulaire pleine de diamètre d = 8mm. La poutre est en acier de limite élastique Re = 240 MPa et de module d'Young E = 210 GPa supportée par deux appuis de niveau en A et B. On prendra un coefficient de sécurité s = 3. Une force verticale F = 15 N est appliquée au point C comme montrée sur la figure ci-dessous. »

  3. **1. Étude théorique (p.225)**
     - **a.** Calculer les réactions des appuis en A et B. (3 lignes)
     - **b.** Donner les expressions des moments fléchissants le long de la poutre. On déduire [sic] le moment de flexion maximal **M_fMaxi**. (3 lignes)
     - **c.** Calculer la contrainte maximale **σ_Maxi** dans cette poutre. (2 lignes)
     - **d.** Calculer le rapport **σ_Maxi/Rp** et conclure. (1 ligne)
  4. **2. Simulation (p.226)**
     - **a.** Utiliser les mêmes données de l'étude théorique pour déterminer le moment fléchissant "M_fzmaxi" et la contrainte maximale "σ_Maxi" par le logiciel "Winflex".
       **M_fzmaxi = ..................... σ_Maxi = ...................**
     - **b.** Relever la valeur de la flèche maximale et son abscisse (au point D).
       **f_Maxi = ................., AD = .................**
     - **c.** Comparer les valeurs obtenues de "M_fzmaxi" et "σ_Maxi" avec celles de l'étude théoriques [sic]. (2 lignes)
  5. **3. Étude expérimentale (p.226)**
     - Choisir la poutre en acier de section circulaire pleine de diamètre d = 8mm.
     - Régler la distance entre les appuis A et B et reposer la poutre.
     - Placer la charge F au point C.
     - Placer le comparateur au point D.
     - **a.** Relever la valeur de la flèche **f_Maxi**. **f_Maxi = .................**
     - **b.** Comparer les valeurs de la flèches [sic] trouvées par simulation et l'étude expérimentale. (1 ligne)

- **Encadrés officiels (verbatim)** : *Situation déclenchante* et *Consignes de sécurité* (p.223), transcrits ci-dessus. Pas de formule encadrée dans l'activité 2 ; renvoi implicite à la Synthèse p.251.

- **Vocabulaire & terminologie officielle** : flexion plane simple, flèche (f), portée (distance entre appuis), déformée, moment quadratique I_GZ, appuis de niveau, module d'Young E, limite élastique Re, contrainte maximale σ_Maxi, moment fléchissant / moment de flexion maximal M_fMaxi, M_fzmaxi, coefficient de sécurité s, résistance pratique Rp.

---

##### Activité 3 — Micro-tour (p.227–232)

- **Système / support d'étude** : **Micro-tour** — mécanisme d'entraînement de la broche (zone d'étude encerclée en pointillés sur la coupe locale 3D p.227).
- **Compétences affichées** : CD 1.7 et CD 2.1 (p.229–232). Pictogrammes en tête de la p.229 : **R. PRO** et **DECI**.
- **Mise en situation (p.227, verbatim)** :

  > La figure ci-dessous représente le mécanisme d'entraînement de la broche en coupe locale 3D d'un micro-tour. Ce mécanisme est représenté sur le dessin d'ensemble de la page suivante. Le mouvement de rotation, est transmis du moteur électrique (21) à la broche (11) par un système poulies-courroies. La broche est guidée en rotation par deux roulements à rouleaux coniques (10).

- **Ressources fournies** :
  - **Coupe locale 3D du micro-tour (p.227)** avec repère **Zone d'étude** (ellipse pointillée autour de la broche, du mandrin et des roulements).
  - **Nomenclature partielle (p.227, § 2)** — deux colonnes, repères 8 à 22 :

    | Rep. | Nbr. | Désignation | | Rep. | Nbr. | Désignation |
    | --- | --- | --- | --- | --- | --- | --- |
    | 8 | 1 | Mandrin | | 16 | 1 | Encodeur |
    | 9 | 3 | Écrou hexagonal | | 17 | 2 | Écrou à encoches |
    | 10 | 2 | Roulement à rouleaux coniques | | 18 | 1 | Cage |
    | 11 | 1 | Broche | | 19 | 1 | Courroie crantée |
    | 12 | 6 | Vis à tête cylindrique à six pans creux | | 20 | 1 | Poulie motrice |
    | 13 | 1 | Poulie réceptrice | | 21 | 1 | Moteur électrique |
    | 14 | 1 | Flasque | | 22 | 1 | Banc |
    | 15 | 1 | Clavette parallèle | | | | |

  - **Dessin d'ensemble (p.228, § 3)** : coupe du **MICRO TOUR — Mécanisme d'entraînement de la broche**, **Echelle : 2:5**, symbole de projection européenne dans le cartouche. Repères en flèches : **14, 13, 12, 11, 10, 9, 8** en haut (de gauche à droite), **15, 16, 17** à gauche, **18, 19, 20, 21, 22** en bas.
  - **Modélisation de la broche (11) dans le plan xy (p.229, figure)** : poutre horizontale portant, de gauche à droite, les points **O**, **A**, **B**, **C** ; cotes **OA = 40**, **AB = 80**, **BC = 60** (mm) ; **appui articulé (triangle plein) en A**, **appui à rouleaux en B** ; force **F₁₉/₁₃** verticale descendante appliquée en **O** ; effort **F_T** vertical ascendant appliqué en **C** ; sens positif des moments repéré par une flèche courbe **+** ; repère (x horizontal vers la droite, y vertical).

- **Données numériques de l'énoncé (p.229, verbatim)** :

  > Les données du problème sont :
  > - Puissance du moteur électrique (13) [sic] : P_m = 0.55 KW;
  > - Rendement du système poulies-courroie : η = 0.92;
  > - Vitesse de rotation du moteur : N_m = 750 tr/min;
  > - Diamètre de la poulie motrice (20) : D₂₀ = 24 mm;
  > - Diamètre de la poulie réceptrice (13) : D₁₃ = 48 mm;
  > - Diamètre de la pièce au cours d'usinage D_pièce = 18 mm;
  > - Module d'élasticité longitudinal de l'acier : E = 200 GPa
  > - La résistance pratique au glissement de l'acier est R_pg = 5 daN/mm² ;
  > - L'effort tangentiel appliqué par l'outil sur la pièce à usiner est F_T;
  > - La résultante des actions de la courroie sur la poulie réceptrice est F₁₉/₁₃ = 537 N ;
  > - Les actions des roulements sont R_A et R_B ;

  **Hypothèses (p.229, verbatim)** :

  > Dans ce qui suit nous supposons que :
  > - Toutes les liaisons sont parfaites;
  > - Les poids de toutes les pièces sont négligeables devant les actions mécaniques;
  > - L'arbre est assimilé à une poutre reposant sur deux appuis de niveau A et B;
  > - L'effort axial appliqué par l'outil sur la pièce est négligé.

  Cotes de la modélisation (p.229) : **OA = 40 mm ; AB = 80 mm ; BC = 60 mm** (soit x ∈ [0 ; 180 mm]).
  Autres valeurs imprimées dans les questions : **λ = R_pg/R_pe = 0.5** (p.232) ; **d/D = 0,8** (p.232).

- **Situation déclenchante (p.229, encadré, verbatim)** :

  > L'arbre de la broche, est un arbre de transmission qui subit des sollicitations dépendant de l'opération d'usinage et des paramètres de coupe.
  >
  > **Comment faire pour identifier ces sollicitations, vérifier la résistance et la rigidité de la broche au cours d'une opération de tronçonnage ?**

- **Travail demandé** :

  1. **(p.230)** Calculer la puissance **P₁₁** reçu par la broche (11). (2 lignes)
  2. **(p.230)** Déterminer le couple **C₁₁** appliqué à la broche (11). (4 lignes)

  **A. Étude statique (p.230)**

  3. Calculer l'effort tangentiel **F_T** appliqué par l'outil sur la pièce à usiner. (4 lignes)
  4. Étudier l'équilibre de l'ensemble et déterminer les actions des appuis simples en **A** et **B** : (12 lignes)
  5. Déduire la valeur du moment de torsion tout le long de la poutre. (4 lignes)
  6. Donner les expressions des moments fléchissant tout le long de la poutre et calculer leurs valeurs en **O, A, B et C**. Découpage imprimé (p.231) :
     - Entre O et A : **0 ≤ x ≤ 40 mm** (3 lignes)
     - Entre A et B : **40 ≤ x ≤ 120 mm** (3 lignes)
     - Entre B et C : **120 ≤ x ≤ 180 mm** (4 lignes)
  7. **(p.231)** Tracer respectivement sur les figures ci-dessous le diagramme des moments de torsion et le diagramme des moments de flexion.
     *(deux repères vierges superposés : le premier d'ordonnée **M_t (N.m)** et d'abscisse **x (mm)**, le second d'ordonnée **M_f (N.m)** et d'abscisse **x (mm)** ; sur chacun les verticales pointillées repèrent O, A, B, C ; mention « Echelle : ......... » en haut.)*
  8. **(p.232)** Indiquer la section la plus sollicitée de la broche. (1 ligne)
  9. **(p.232)** Déduire à quelle type [sic] de sollicitation est soumise la broche (11) ? justifier votre réponse. (1 ligne)

  **B. Étude de la résistance de la broche (11) (p.232)**

  10. Calculer le moment idéal de Flexion. *(formule fournie — voir encadré ci-dessous)* (3 lignes)
  11. Trouver le diamètre minimal pour que la broche (11) résiste en toute sécurité. (5 lignes)
  12. « Pour améliorer les performances de la machine (usinage des pièces longues, allègement de la broche...). On se propose de changer la section circulaire pleine par une section creuse dont le rapport des diamètres **d/D = 0,8** . Déterminer les diamètres extérieur **D_min** et intérieur **d_Max** de la broche. » (12 lignes)

- **Encadrés officiels (verbatim)** — formule imprimée à la question B.1 (p.232) :

  > Sachant que : M_fidéal = (1 − 1/(2λ)) . M_f + (1/(2λ)) . √(M_f² + M_t²)  ;
  >
  > Pour l'acier de la broche (11)  λ = R_pg / R_pe = 0.5

- **Vocabulaire & terminologie officielle** : broche, arbre de transmission, opération de tronçonnage, paramètres de coupe, système poulies-courroies, courroie crantée, roulement à rouleaux coniques, rendement η, effort tangentiel F_T, résistance pratique au glissement R_pg, résistance pratique à l'extension R_pe, moment de torsion, moment fléchissant, moment idéal de flexion M_fidéal, section la plus sollicitée, sollicitation composée, section creuse, diamètres D_min / d_Max.

---

##### Activité 4 — Touret à meuler (p.233–238)

- **Système / support d'étude** : **Touret à meuler** (machine d'enlèvement de matière par abrasion : ébavurage, affûtage).
- **Compétences affichées** : CD 1.7 et CD 2.1 (p.234–238 ; la p.233 de présentation ne porte pas de badge). Pictogrammes en tête de la p.235 : **R. PRO** et **DECI**.
- **Mise en situation (p.233, verbatim)** :

  > Le touret à meuler ci-dessous est une machine qui permet d'enlever la matière par abrasion (opérations d'ébavurage, d'affûtage…).
  > Il est constitué principalement d'un arbre entraîné en rotation par poulies-courroie et guidé par des roulements à billes. Une meule liée à l'arbre sert comme outil de meulage.

  puis : « Le schéma cinématique du touret à meuler est représenté par la figure ci-dessous. »

- **Ressources fournies** :
  - **Vue 3D en coupe et vue extérieure (p.233)**, annotées **Roulement**, **Arbre**, **Poulie**, **Meule**.
  - **Schéma cinématique (p.233, bas)** : ligne d'arbre horizontale (axe x) portant, de gauche à droite, **O** (plan de la meule), **A** (palier), **G**, **C** (palier), **B** (poulie) ; cotes **O→A = 100**, **A→C = 240**, **C→B = 90** (mm) ; **Bâti** hachuré sous les deux paliers ; **Arbre (1)** et **Poulie (2)** repérés ; sens positif **+** en flèche courbe. À gauche, vue de face de la meule (disque jaune) dans le plan (y, z) avec le point **D** en périphérie et l'effort **F_T** vertical ascendant ; à droite, vue de face de la poulie (disque bleu) dans le plan (y, z) avec **B'** et **B"** et les brins **t** et **T** verticaux descendants.
  - **Dessin d'ensemble (p.234, § 2)** : coupe longitudinale, **Echelle: 2:9**, cartouche **Touret à meuler**, symbole de projection européenne. Repères en flèches : **6, 1, 7, 8, 9** en haut ; **5, 3, 4, 10, 2** en bas.
  - **Nomenclature (p.234)** — imprimée de bas en haut sous le dessin :

    | Rep. | Nb. | Désignation | Matière | Observation |
    | --- | --- | --- | --- | --- |
    | 10 | 1 | Joint à lèvre | *(vide)* | *(vide)* |
    | 9 | 1 | Couvercle | S 275 | *(vide)* |
    | 8 | 1 | Boîtier | S 275 | *(vide)* |
    | 7 | 1 | Bague | S 275 | *(vide)* |
    | 6 | 2 | Roulement | *(vide)* | *(vide)* |
    | 5 | 2 | Flasque | S 275 | *(vide)* |
    | 4 | 1 | Bâti | EN-GJL-200 | *(vide)* |
    | 3 | 1 | Meule | *(vide)* | *(vide)* |
    | 2 | 1 | Poulie | S 275 | *(vide)* |
    | 1 | 1 | Arbre | S 275 | *(vide)* |

  - **Figure des actions sur la meule et la poulie (p.235, marge droite)** : deux cercles concentriques de rayons **r_m** (meule) et **r_p** (poulie) centrés en **O** ; **F_T** vertical ascendant appliqué en **D** ; **T** et **t** verticaux descendants ; axe **z** horizontal.
  - **Modèle de poutre (p.236, question 2)** : axe x avec **O, A, G, C, B** ; cotes **100 / 240 / 90** ; appui articulé en **A**, appui à rouleaux en **C** ; sens positif **+**.
  - **Diagrammes vierges (p.238, haut)** : repère **Mt (N.m)** / **x(mm)** puis repère **Mf (N.m)** / **x(mm)**, verticales pointillées repérant **O, A, G, C, B**, mention « Echelle:.................... ».
  - **QR-code marqué PDF** (p.235, marge droite).

- **Données numériques de l'énoncé (p.235, verbatim)** :

  > Dans ce qui suit nous supposons que toutes les liaisons sont parfaites.
  > On donne :
  > - AC = 240 mm ; AB = 330 mm et OA = 100 mm
  > - Rayon de la poulie (2) : r_p = BB' = 22 mm.
  > - Rayon de la meule (3) : r_m = OD = 75 mm.
  > - Les actions mécaniques qui s'exercent sur l'arbre (1) sont :
  >   • Les efforts appliqués par la pièce à ébavurer sur la meule se réduisent à l'effort tangentiel F_T = 110 N;
  >   • Les actions de la courroie sur la poulie (2) sont T et t avec  T ≈ 4.t.
  >   • Les actions des paliers sont : R_A et R_C.
  >   • Le poids du système {arbre (1) + poulie (2) + meule (3)} est P = 30 N appliqué au milieu d'OB.

  Autres valeurs imprimées : tableau p.236 (**F_T** : Ox = 0, Oy = **110 N** ; **T + t** au point B : Ox = 0, Oy = **− 625 N** ; **P** au point G : Oy = **30 N**) ; découpage en 4 sections p.237 (**0–100 / 100–215 / 215–340 / 340–430 mm**) ; **λ = R_pg/R_pe = 0.5** (p.238) ; acier **S275**, coefficient de sécurité **s = 2** (p.238).

- **Situation déclenchante (p.235, encadré, verbatim)** :

  > On se propose de rechercher le diamètre de l'arbre plein, du touret à meuler.
  >
  > **Comment faire pour dimensionner et pour vérifier la résistance et la rigidité d'un composant soumis à une sollicitation composée ?**

- **Travail demandé** :

  **A. Étude statique**

  1. **(p.235)** En écrivant la condition d'équilibre de l'ensemble {arbre (1) + poulie (2) + meule (3)} autour de l'axe x, déterminer les actions de la courroie sur la poulie (2). (8 lignes)
     Résultats à reporter en bas de page : **‖T‖ = ....................  ‖M_t‖ = ....................**
  2. **(p.236)** Représenter sur le modèle suivant de la poutre {arbre (1) + poulie (2) + meule (3)} les actions extérieures qui lui sont appliquées. *(figure du modèle O-A-G-C-B, cotes 100 / 240 / 90)*
  3. **(p.236)** Calculer **R_A** et **R_C** puis compléter le tableau suivant des actions mécaniques extérieures qui s'exercent sur la poutre :

     | Force | Point de réduction | Projection sur Ox | Projection sur Oy |
     | --- | --- | --- | --- |
     | F_T | O | 0 | 110 N |
     | R_A | A | 0 | ................ |
     | R_C | C | ................ | ................ |
     | P | G | ................ | 30 N |
     | T + t | B | 0 | − 625 N |

     (10 lignes de calcul à compléter sous le tableau)

  **B. Étude de la résistance de l'arbre porte meule (1) (p.237–238)**

  4. **(p.237)** Déduire la valeur du moment de torsion tout le long de la poutre. (2 lignes)
  5. **(p.237)** Donner les expressions des moments fléchissant tout le long de la poutre et calculer leurs valeurs en **O, A, G, C et B**. Découpage imprimé :
     - Section 1 : **0 ≤ x ≤ 100 mm** (4 lignes)
     - Section 2 : **100 ≤ x ≤ 215 mm** (4 lignes)
     - Section 3 : **215 ≤ x ≤ 340 mm** (5 lignes)
     - Section 4 : **340 ≤ x ≤ 430 mm** (5 lignes)
  6. **(p.237 fin → p.238 haut)** Tracer respectivement sur les figures ci-dessous le diagramme des moments de torsion et le diagramme des moments de flexion. *(les deux repères vierges annoncés en bas de la p.237 sont imprimés en haut de la p.238)*
  7. **(p.238)** Indiquer la section la plus sollicitée de l'arbre porte meule (1). (1 ligne)
  8. **(p.238)** Déduire à quelle type [sic] de sollicitation est soumis l'arbre porte meule (1) ? justifier votre réponse. (2 lignes)
  9. **(p.238)** Calculer le moment idéal de Flexion. *(formule fournie — voir encadré ci-dessous)* (2 lignes)
     Puis, imprimé entre les questions 6 et 7 : « L'arbre du touret à meuler est réalisé en acier S275. Le coéficient [sic] de sécurité est s=2. »
  10. **(p.238)** En utilisons [sic] la condition de résistance à la flexion trouver le diamètre minimal de l'arbre. (3 lignes)
  11. **(p.238)** Relever le diamètre du dessin d'ensemble et vérifier le choix du constructeur. (2 lignes)

- **Encadrés officiels (verbatim)** — formule imprimée à la question B.6 (p.238) :

  > Sachant que : M_fidéal = (1 − 1/(2λ)) . M_f + (1/(2λ)) . √(M_f² + M_t²)  ;
  >
  > Pour l'acier de l'arbre porte meule (1)  λ = R_pg / R_pe = 0.5

- **Vocabulaire & terminologie officielle** : touret à meuler, abrasion, ébavurage, affûtage, meule, arbre porte meule, poulies-courroie, roulements à billes, schéma cinématique, brins de courroie T et t, palier, condition d'équilibre autour de l'axe x, point de réduction, projection sur Ox / Oy, moment idéal de flexion, condition de résistance à la flexion, acier S275, EN-GJL-200.

---

##### Activité 5 — Machine de torsion de limes dentaires (p.239–244)

- **Système / support d'étude** : **Machine de torsion de limes dentaires** — plus précisément sa **boîte de vitesses** (mécanisme d'avance et de recul du traînard) ; composant dimensionné : le **pignon arbré (39)**.
- **Compétences affichées** : CD 1.7 et CD 2.1 (p.242–244 ; les p.239–241 de présentation ne portent pas de badge). Pictogrammes en tête de la p.242 : **R. PRO** et **DECI**.
- **Mise en situation (p.239, verbatim)** :

  > La machine (Fig.1) est destinée à la torsion des tiges meulées afin de les transformer en limes dentaires utilisées par les dentistes pour le traitement d'une dent infectée (Fig.2). La lime est composée d'une manche en plastique et d'une tige torsadée en acier inoxydable représentant sa partie active.
  >
  > Un mandrin assure le serrage de la tige sur sa partie cylindrique(Fig.1). L'opération de torsadage est assurée par la rotation du mandrin entraîné par le moteur Mt1. Le blocage de la tige au niveau de sa forme prismatique est efféctué [sic] par la pince à 4 mors. Le reglage [sic] de la longueur est éffectué [sic] par l'avance et le recul du traînard.
  > Le déplacement du traînard est assuré par un système vis-écrou et une boite de vitesses accouplée au moteur Mt2.

  **2. Description de fonctionnement du mécanisme d'avance et de recul du traînard (p.239, verbatim)** :

  > L'avance et le recul du traînard sont assurés par un système vis-écrou et un guidage prismatique (Fig.1).
  > L'écrou est fixé sur le traînard et la vis est animée d'un mouvement de rotation à l'aide de la boite de vitesses.
  > Le mouvement de rotation de l'arbre moteur (1) est transmis vers la vis mère (36) à travers un ensemble de roues dentées et l'un des deux embrayages E1 ou E2 selon la vitesse de déplacement du traînard. (Voir dessin d'ensemble).

- **Ressources fournies** :
  - **Fig. 1 (p.239)** : vue 3D de la machine annotée **Mandrin**, **Tige**, **Pince à 4 mors**, **Trainard** [sic], **Vis mère**, **Boite vitesse**, **Mt1** (moteur de torsadage, à gauche), **Mt2** (moteur d'avance, à droite), **Support** ; inscription « MACHINE DE TORSION DE LIMES DENTAIRES » sur le bâti.
  - **Fig. 2 (p.239)** : coupe anatomique d'une dent annotée **Lime dentaire** et **Dent infectée**.
  - **Dessin d'ensemble (p.240, § 3)** : coupe de la **BOÎTE DE VITESSES**, cartouche **MACHINE DE TORSION DE LIMES DENTAIRES**, **Echelle: 1:2**, symbole de projection européenne. Repères **1 → 45** disposés autour du dessin (1 à 17 en haut à gauche, 18 à 33 en bas, 34 à 36 en bas à droite, 37 à 45 en haut à droite) ; les deux embrayages sont annotés **E1** et **E2** ; le moteur est annoté **Moteur (Mt2)** ; un repère **S** figure au centre-droit. Un **QR-code marqué PDF** accompagne le dessin.
  - **Nomenclature complète (p.241, § 4)**, repères 1 à 45 :

    | Rep. | Nbr. | Désignation | | Rep. | Nbr. | Désignation |
    | --- | --- | --- | --- | --- | --- | --- |
    | 1 | 1 | Arbre moteur | | 24 | 1 | Arbre |
    | 2 | 1 | Vis de pression | | 25 | 4 | Clavette parallèle |
    | 3 | 7 | Vis CHc | | 26 | 2 | Anneau élastique |
    | 4 | 1 | Support moteur | | 27 | 2 | Bobine (KA2, KA3) |
    | 5 | 1 | Flasque droite | | 28 | 2 | Roulement BC |
    | 6 | 1 | Pignon | | 29 | 2 | Anneau élastique |
    | 7 | 1 | Carter | | 30 | 1 | Pignon arbré |
    | 8 | 2 | Cloche | | 31 | 1 | Flasque gauche |
    | 9 | 2 | Bague collectrice | | 32 | 1 | Roulement à aiguilles |
    | 10 | 1 | Pignon | | 33 | 1 | Roue dentée |
    | 11 | 1 | Clavette disque | | 34 | 1 | Vis CHc |
    | 12 | 2 | Roulement BC | | 35 | 1 | Bouchon de remplissage |
    | 13 | 1 | Bague entretoise | | 36 | 1 | Vis mère |
    | 14 | 1 | Anneau élastique | | 37 | 2 | Roulement BC |
    | 15 | 1 | Rondelle spéciale | | 38 | 1 | Couvercle |
    | 16 | 4 | Disque intérieur | | 39 | 1 | Pignon arbré |
    | 17 | 4 | Disque extérieur | | 40 | 2 | Plateau de pression |
    | 18 | 5 | Vis CHc | | 41 | 2 | Support bobine |
    | 19 | 1 | Roue dentée | | 42 | 1 | Roue dentée |
    | 20 | 1 | Manchon cannelé | | 43 | 1 | Bague à collerette |
    | 21 | 12 | Vis CHc | | 44 | 4 | Vis CHc |
    | 22 | 4 | Roulement BC | | 45 | 1 | Clavette parallèle |
    | 23 | 3 | Bague entretoise | | | | |

  - **Figure de l'action de la roue (33) sur le pignon arbré (39) (p.242, marge droite)** : cercle (roue) centré sur l'axe y ; en périphérie, point **D** (haut) et point **C** (juste au-dessous, sur l'axe) ; effort **F₃₃/₃₉** incliné, décomposé en **T** (tangentiel, horizontal) et **R** (radial, vertical descendant) ; l'angle entre **F₃₃/₃₉** et **T** est coté **20°** ; couple résistant **Cr** représenté par une flèche courbe ; axe **z** horizontal.
  - **Modèle de poutre du pignon arbré (39) (p.242, bas)** : axe x avec **A**, **C**, **B**, **D** ; cotes **A→C = 40**, **C→B = 50**, **B→D = 35** (mm) ; **R_A** vertical ascendant en A (appui articulé), **T** vertical descendant en C (appliqué depuis le point **D** situé au-dessus), **R_B** vertical ascendant en B (appui à rouleaux) ; sens positif **+** ; axe **z** vers le bas.
  - **Diagrammes vierges (p.243)** : repère **M_t (N.m)** / **x(mm)** et repère **M_f (N.m)** / **x(mm)**, verticales pointillées repérant **A, C, B, D**, mention « Echelle:.................... ».

- **Données numériques de l'énoncé (p.242, verbatim)** :

  > Hypothèses :
  > - Le pignon arbré (39) est assimilé à une poutre cylindrique à section creuse.
  > - Les poids des pièces sont négligés ainsi que les frottements.
  >
  > On donne :
  > - Rendement de la boite de vitesses ŋ = 0,97. [sic — glyphe « ŋ » imprimé à la place de η]
  > - Puissance du moteur P_m = 1000 Watts.
  > - La vis mère tourne à une vitesse constante N₃₆ = 70 tr/min.

  Autres valeurs imprimées : angle **20°** sur la figure de l'engrènement (p.242) ; cotes **40 / 50 / 35 mm** du modèle (p.242) ; découpage en 3 sections **0–40 / 40–90 / 90–125 mm** (p.243) ; **λ = R_pg/R_pe = 0.5** (p.244) ; acier **30CrNiMo16**, **Re = 700 MPa**, **s = 2**, **D = 3/2.d** (p.244).

- **Situation déclenchante (p.242, encadré, verbatim)** :

  > On se propose de déterminer les dimensions de la section creuse du pignon arbré (39) pour qu'il résiste en toute sécurité.
  >
  > **Comment faire pour dimensionner et vérifier un composant soumis à une sollicitation composée ?**

- **Travail demandé** :

  1. **(p.242)** Calculer la puissance transmise au pignon arbré (39). (2 lignes)
  2. **(p.242)** Déduire le couple exercé sur l'arbre (39): **C₃₉**. (2 lignes)

  **A. Étude statique (p.242)**

  3. L'action de la roue (33) sur le pignon arbré (39) est représentée sur la figure ci-contre.
     - **a.** Relever le rayon de la roue (39) sur le dessin d'ensemble et déterminer l'effort tangentiel **‖T‖**. (1 ligne)
     - **b.** Déterminer l'effort radial **‖R‖** (3 lignes)
  4. On suppose que l'effet de l'effort radial est négligeable devant l'effort tangentiel et en modélise [sic] le pignon arbré (39) par la figure ci-contre. *(figure du modèle A-C-B-D, cotes 40 / 50 / 35)*

  **B. Étude de la résistance du pignon arbré (39) (p.243–244)**

  5. **(p.243)** Déduire la valeur du moment de torsion tout le long de la poutre. (1 ligne)
  6. **(p.243)** Donner les expressions des moments fléchissant tout le long de la poutre et calculer leurs valeurs en **A, C, B et D**. Découpage imprimé :
     - Section 1 : **0 ≤ x ≤ 40 mm** (3 lignes)
     - Section 2 : **40 ≤ x ≤ 90 mm** (3 lignes)
     - Section 3 : **90 ≤ x ≤ 125 mm** (4 lignes)
  7. **(p.243)** Tracer respectivement sur les figures ci-dessous le diagramme des moments de torsion et le diagramme des moments de flexion.
  8. **(p.244)** Indiquer la section la plus sollicitée du pignon arbré (39). (1 ligne)
  9. **(p.244)** Déduire à quelle type [sic] de sollicitation est soumis le pignon arbré (39) ? justifier votre réponse. (3 lignes)
  10. **(p.244)** Calculer le moment idéal de flexion. *(formule fournie — voir encadré ci-dessous)* (4 lignes)
  11. **(p.244)** Le pignon arbré (39) est en acier **30CrNiMo16** de limite élastique **Re = 700 MPa**. Sachant que le coefficient de sécurité **s = 2**, déterminer **D_min** de la section creuse pour qu'il résiste en toute sécurité ; On prend **D = 3/2.d**. (7 lignes)
  12. **(p.244)** Déduire la valeur **d_Max**. (2 lignes)

- **Encadrés officiels (verbatim)** — formule imprimée à la question B.6 (p.244) :

  > Sachant que : M_fidéal = (1 − 1/(2λ)) . M_f + (1/(2λ)) . √(M_f² + M_t²)  ; Pour l'acier  λ = R_pg / R_pe = 0.5

- **Vocabulaire & terminologie officielle** : lime dentaire, tige meulée / torsadée, mandrin, pince à 4 mors, traînard, système vis-écrou, guidage prismatique, boîte de vitesses, vis mère, embrayages E1 / E2, pignon arbré, roue dentée, effort tangentiel T, effort radial R, couple résistant Cr, section creuse, acier 30CrNiMo16, limite élastique Re, coefficient de sécurité s.

---

##### Activité 6 — Grue d'atelier (p.245–249)

- **Système / support d'étude** : **Grue d'atelier** hydraulique ; composant dimensionné : la **flèche extensible** (tube de section carrée).
- **Compétences affichées** : CD 1.7 et CD 2.1 (p.247–249 ; les p.245–246 de présentation ne portent pas de badge). Pictogrammes en tête de la p.247 : **R. PRO** et **DECI**.
- **Mise en situation (p.245, verbatim)** :

  > Les grues d'atelier hydrauliques sont indispensables pour manœuvrer facilement sans le moindre effort et en toute sécurité des charges lourdes.
  > Elles sont utilisées pour réaliser des opérations de maintenance dans le domaine mécanique ou dans le domaine de manutention.

- **Ressources fournies** :
  - **Vue 3D de la grue (p.245)**, annotée **Flèche extensible**, **Charge à soulever**, **Manette de pompage**, **Vérin hydraulique**, **Support**.
  - **Caractéristiques techniques (p.245, § 2, verbatim)** :
    - Capacité maximale : 250 kg ;
    - La longueur de la flèche est extensible à 3 valeurs (895-1685 mm);
    - Hauteur de 540 à 2519 mm ;
    - Grue déplaçable et repliable ;
    - Vérin hydraulique double effets pour levage rapide, de course 495 mm, sa langueur [sic] maximale x_max = 1165 mm et sa longueur minimale x_min = 670 mm ;
  - **Dessin d'ensemble (p.246, § 3)** : trois vues (vue de côté, vue de face avec la charge, vue de dessus) ; **Echelle: 1:36** ; cartouche **Grue d'atelier** ; symbole de projection européenne. Points repérés sur la vue de face : **A** (pied de la flèche), **B** (attache du vérin sur la flèche), **C** (extrémité de la flèche / crochet), **D** (attache basse du vérin), **E** et **F** (extrémités du châssis au sol) ; repère **Charge**. Une vue de détail cinématique en bas à gauche donne **θ = 38°** (position haute) et **θ = 35°** (position basse), **H_maxi = 2519**, **H_mini = 540**, avec la mention manuscrite **« La flèche extensible est à sa longueur maximale »**. Repères de nomenclature **1** (vérin), **2** (flèche extensible), **3** (douille à aiguilles), **4** (crochet), **5** (roue), **6** (traverse coudée).
  - **Nomenclature (p.246)** :

    | Rep. | Nb. | Désignation | Matière | Observation |
    | --- | --- | --- | --- | --- |
    | 6 | 2 | Traverse coudée | S 355 | *(vide)* |
    | 5 | 3 | Roue | EN AW-2017 | *(vide)* |
    | 4 | 1 | Crochet | C 60 | *(vide)* |
    | 3 | 14 | Douille à aiguilles | *(vide)* | SKF |
    | 2 | 1 | Flèche extensible | S 355 | *(vide)* |
    | 1 | 1 | Vérin | EN AW-2017 | *(vide)* |

  - **Modèle de la flèche (p.247)** : poutre horizontale **A — B — C** (axe x, axe y vertical) ; **a** = distance A→B ; **L** = distance A→C ; effort **F_V** appliqué en **B**, incliné vers le haut à droite, l'angle avec l'axe de la poutre étant coté **β** ; charge **P** appliquée en **C**, dirigée vers le bas à gauche, l'angle avec l'axe étant coté **θ**.
  - **Diagrammes vierges (p.248)** : trois repères superposés — **N (N)** / **x(mm)**, **T_y (N)** / **x(mm)**, **M_fz (N.m)** / **x(mm)** — verticales pointillées repérant **A, B, C**, mention « Echelle:................... » sur chacun.
  - **Figure de la section (p.249, marge droite)** : tube de section carrée, côté extérieur coté **B** (horizontalement et verticalement), épaisseur cotée **T**, centre de gravité **G**, axes **y** (vertical) et **z** (horizontal).
  - **Trois figures de répartition de contraintes (p.249, question 4)** : *Contrainte induite par N* **+** *Contrainte induite par M_fz* **=** *Superposition des contraintes*, chacune tracée dans un repère (G, x, y) sur une section, avec mention « Echelle:................... ».

- **Données numériques de l'énoncé (p.247, § A, verbatim)** :

  > On donne : β = 51°, θ = 38°, AC = 1685mm, AB = 420mm, P = 2500 N.

  Autre donnée imprimée à la question 2 : **F_v = 10170 N**. Sections disponibles (p.249) : **70x70x5**, **80x80x5**, **90x90x5** ; acier **S355**, coefficient de sécurité **s = 4** ; abscisse d'étude **x = 200 mm**.

- **Situation déclenchante (p.247, encadré, verbatim)** :

  > Dimensionnement de la flèche de la grue dans la position la plus haute (θ = 38°).
  >
  > **Comment faire pour vérifier le dimensionnement de la flèche dans cette position ?**

  **Hypothèses (p.247, verbatim)** :

  > - Les poids des éléments de la grue sont négligés devant les efforts extérieurs.
  > - Toutes les liaisons sont supposées parfaites.

- **Travail demandé** :

  **A. La flèche atteint la hauteur maximale (p.247–248)**

  1. Représenter sur le modèle suivant de la flèche l'effort exercé en **A**.
     **Remarque (verbatim)** : « Pour des raisons de commodité de calcul, le repère lié à la flèche extensible est pivoté dans angle [sic] de θ = 38° par rapport à sa position réelle. »
  2. Compléter le tableau suivant des actions mécaniques extérieures qui s'exercent sur la flèche sachant que **Fv = 10170N**.

     | Force | Point d'application | Projection sur Ax | Projection sur Ay |
     | --- | --- | --- | --- |
     | F_A | A | ..................... | ..................... |
     | F_V | B | ..................... | ..................... |
     | P | C | ..................... | ..................... |

  3. Calculer les efforts tranchants, les efforts normaux et les moments fléchissants tout le long de la poutre.
     - Section 1 entre A et B : **0 ≤ x ≤ 420 mm** → **N = ........ ; T_y = ........ ; M_fz = ........**
     - Section 2 entre B et C : **420 ≤ x ≤ 1685 mm** → **N = ........ ; T_y = ........ ; M_fz = ........**
  4. **(p.248)** Tracer les diagrammes des efforts tranchants, normaux et des moments fléchissants. *(trois repères vierges N(N), T_y(N), M_fz(N.m))*
  5. **(p.248)** Compléter le tableau suivant en précisant les types de sollicitation dans chaque section.

     | Sections | Section 1  0 ≤ x ≤ 420mm | Section 2  420 ≤ x ≤ 1685mm |
     | --- | --- | --- |
     | Sollicitations | ..................... | ..................... |

  6. **(p.248)** Préciser le lieu de la section la plus sollicitée et en déduire les valeurs maximales de **M_fz** et **N**. (2 lignes)

  **B. Choix de la section de la flèche extensible (p.249)**

  Énoncé (verbatim) :

  > - La flèche extensible est faite d'un tube de section carrée supposé constante sur toute la longueur.
  > - Le constructeur a choisi l'acier S355 avec un coefficient de sécurité s=4.
  > Dans le magasin de matière première, on dispose de tubes carrés de trois sections différentes.

  7. Compléter les caractéristiques géométriques de chaque section dans le tableau suivant :

     | Section BxBxT | Section S (mm² × 10²) | I_GZ/V (mm³ x 10³) | σ_f (MPa) | σ_N (MPa) | σ_éq (MPa) |
     | --- | --- | --- | --- | --- | --- |
     | 70x70x5 | ............ | ............ | ............ | ............ | ............ |
     | 80x80x5 | ............ | ............ | ............ | ............ | ............ |
     | 90x90x5 | ............ | ............ | ............ | ............ | ............ |

  8. Calculer la contrainte pratique pour le matériau choisi. (2 lignes)
  9. D'après le tableau, choisir la section la plus convenable qui résiste en toute sécurité. (1 ligne)
  10. Pour une section droite **S_x** d'abscisse **x = 200 mm**, tracer l'allure des contraintes normales induites par **N** et **M_fz** et leur superposition. **Conclure :** (3 lignes)

- **Vocabulaire & terminologie officielle** : grue d'atelier hydraulique, flèche extensible, vérin hydraulique double effets, course, manette de pompage, manutention, capacité maximale, effort tranchant T_y, effort normal N, moment fléchissant M_fz, sollicitation composée (flexion-traction / flexion-compression), contrainte pratique, contrainte équivalente σ_éq, module I_GZ/V, acier S355, EN AW-2017, C 60, douille à aiguilles.

---

##### Synthèse — Comportement du solide déformable (p.250–251)

*(Bandeau imprimé « **Synthèse** » en tête de la p.250. En-tête courant des deux pages : « COMPORTEMENT DU SOLIDE DEFORMABLE », badges CD 1.7 / CD 2.1. Un QR-code marqué **EXE** figure en haut à droite de la p.250, un QR-code marqué **PDF** en bas à droite de la p.251.)*

**1. Auto-évaluation (p.250, verbatim)**

> Tester vos connaissances avant de passer à la synthèse avec les Quiz.

**2. Synthèse torsion simple (p.250, verbatim)**

> **a. Définition**
> Une poutre est sollicitée à la torsion lorsqu'elle est soumise à ses deux extrémités à des actions mécaniques qui se réduisent à deux couples égaux et opposés dont les axes sont confondus avec la ligne moyenne

> **b. Étude des déformations.**
> Angle unitaire de torsion  θ = α / L ;
> Avec:
> α : angle relatif de torsion en rd;
> θ: est exprimé en rd/mm;
> L : Longueur de l'éprouvette en mm.

*Figure associée (p.250, § b)* : à gauche, section circulaire de centre **G** montrant le rayon **GA** tourné en **GA'** de l'angle **α** ; à droite, cylindre d'axe **x** encastré à gauche (section **A₀ / G₀**) et sollicité par deux moments **Mt** opposés ; les sections successives **A₁, A₂, A** tournent des angles **α₁, α₂, α** aux abscisses **x₁, x₂, x** ; la génératrice initiale devient une hélice.

> **c. Étude des contraintes**
> La contrainte tangentielle en un point M de la section est: **τ = G . θ . ρ**
> Avec:
> G: Module d'élasticité transversale ou module de Coulomb en MPa ou Pa.
> ρ : Distance entre le centre et le point M en mm ou en m;
> La contrainte tangentielle  τ  est maximale pour ρ = R;

*Figure associée (p.250, § c)* : section circulaire **(S)** de centre **G** et de rayon **R**, point **M** à la distance **ρ** ; répartition linéaire des contraintes tangentielles le long d'un diamètre, valant **τ_max** en périphérie côté +y et **−τ_max** côté opposé, **τ** au point M ; axe **y** vertical.

> **d. Relation entre θ et le moment de torsion Mt:**
>
> **θ = M_t / (G . I₀)**
>
> Avec I_O : Moment quadratique polaire de la section exprimé en mm⁴ ou en m⁴.
> L'angle unitaire de torsion est exprimé en rad/mm ou en rad/m

> **e. Condition de rigidité : θ ≤ θ_limite**
>
> θ_limite est fixé par l'expérience

> **f. Relation entre τ et le moment de torsion Mt :**
>
> **τ = (M_t / I_o) . ρ**
>
> τ est maximale sur la génératrice la plus éloignée du centre : ρ = R
>
> **τ_maxi = M_t / (I_o / R)**

> **g. Condition de résistance :**
> Un arbre de section circulaire sollicité à la torsion peut résister en toute sécurité si  à cette sollicitation si : **τ_maxi ≤ R_pg** avec
> Avec : R_pg : Résistance pratique au glissement en MPa ou en Pa.   **R_pg = R_eg / s**
> Reg : Limite élastique au cisaillement ou au glissement en MPa ou en Pa.
> s: coefficient de sécurité

**3. Synthèse flexion plane simple (p.251, verbatim)**

> **a. Contrainte normale σ**
> σ : contrainte normale exprimée en MPa ou Pa
> I_Gz : moment quadratique par rapport à l'axe neutre Gz de la section de la poutre en(mm⁴)
> Pour un moment de flexion donné, la contrainte normale est proportionnelle à l'ordonnée (y) du point M.
>
> **σ = (M_fz / I_Gz) . y**
>
> σ est maximale lorsque (y) atteint sa valeur maximale (y_max). On pose  v = y_max en (mm)
>
> **σ_max = M_fz / (I_GZ / v)**
>
> La quantité  I_GZ / v  est appelée module de rigidité à la flexion exprimée en mm³ ou en m³

*Figure associée (p.251, § a)* : section **(S)** avec le centre de gravité **G**, axes **x** et **y**, point **M** d'ordonnée **y** ; répartition linéaire des contraintes normales sur la hauteur, valant **σ_max** en fibre inférieure et **−σ_max** en fibre supérieure, **σ** au point M.

> **b. Condition de résistance**
> Pour qu'une poutre, sollicitée à la flexion simple résiste en toute sécurité il faut que :
> **σ_max ≤ R_pe**  avec  **R_pe = R_e / s**; R_e est la limite élastique à la traction

**4. Synthèse sollicitations composées (p.251, verbatim)**

> **a. Flexion-traction / Flexion-compression**
> - **Contraintes normales**

*Figure associée (p.251)* : trois diagrammes de répartition sur une même section, reliés par « **=** » et « **+** » — (Traction + Flexion), portant le repère **Nouveau plan neutre**, égale (Traction) — répartition uniforme — plus (Flexion) — répartition linéaire ; chaque diagramme est tracé dans un repère (G, x, y).

> - **Condition de résistance**
> La sollicitation de traction-flexion augmente la zone de traction en déplaçant la ligne neutre au-dessus ou au dessous de la ligne moyenne. Dans ce cas pour qu'une poutre, résiste en toute sécurité il faut que :
>
> **‖N‖ / S + ‖M_fzmax‖ / (I_Gz / v) ≤ R_pe**

> **b. Flexion-torsion**
> Un arbre est soumis à une sollicitation de flexion-torsion si le moment résultant en G est :
> Dans ce cas le dimensionnement de l'arbre est déterminé à partir du moment idéal de flexion.
>
> **M_G = M_t . x⃗ + M_f . z⃗**
>
> - **Moment idéal de flexion**
>
> Avec  λ = Rpg / Rpe          **Mf_i = (1  [signe absent à l'impression]  1/(2λ)) Mf   [signe absent à l'impression]  (1/(2λ)) √(Mf² + Mt²)**
>
> Remarque: λ dépend de la nature des matériaux.

*(Sur la p.251, les signes « − » et « + » de cette dernière formule ne sont pas imprimés : deux espaces blancs subsistent à leur place. La forme complète, imprimée trois fois dans les activités — p.232, p.238 et p.244 — est : **M_fidéal = (1 − 1/(2λ)) . M_f + (1/(2λ)) . √(M_f² + M_t²)**.)*

Dernière ligne de la p.251 (verbatim) :

> Grille d'évaluation comportement des solides déformables

*(Cette ligne est un renvoi : la grille elle-même n'est pas imprimée dans les pages 250–251 ; elle est associée au QR-code « PDF » placé en regard.)*

---

##### Bornes de scope observées — p.216–251

- ✅ **INCLUS — traité explicitement à ce niveau** :
  - **Torsion simple** : définition (deux couples égaux et opposés d'axes confondus avec la ligne moyenne) ; essai expérimental sur banc (Mt = f(α), α = f(x), détermination de G) ; angle relatif de torsion α, angle unitaire de torsion θ = α/L ; contrainte tangentielle τ = G.θ.ρ et τ = (Mt/I₀).ρ ; τ_maxi = Mt/(I₀/R) ; moment quadratique polaire I₀ ; relation θ = Mt/(G.I₀) ; **condition de rigidité** θ ≤ θ_limite ; **condition de résistance** τ_maxi ≤ R_pg avec R_pg = R_eg/s ; valeurs théoriques de G pour acier / laiton / aluminium ; dimensionnement d'un diamètre en torsion.
  - **Flexion plane simple** : essai expérimental (flèche f = f(F), f = f(L), reconnaissance de la loi f = k.L³) ; réactions d'appuis sur deux appuis de niveau ; expressions et diagrammes des moments fléchissants ; contrainte normale σ = (M_fz/I_Gz).y ; σ_max = M_fz/(I_GZ/v) ; module I_GZ/v ; **condition de résistance** σ_max ≤ R_pe avec R_pe = R_e/s ; comparaison théorie / simulation (« Winflex ») / expérimentation.
  - **Sollicitations composées** : **flexion-torsion** (moment résultant M_G = M_t.x⃗ + M_f.z⃗, moment idéal de flexion M_fidéal, λ = R_pg/R_pe) appliquée trois fois (broche de micro-tour, arbre porte meule, pignon arbré) ; **flexion-traction / flexion-compression** (superposition des contraintes normales, déplacement de la ligne neutre, condition ‖N‖/S + ‖M_fzmax‖/(I_Gz/v) ≤ R_pe) appliquée à la flèche de grue ; dimensionnement de sections **pleines** et **creuses** (rapports d/D = 0,8 et D = 3/2.d) et choix d'une section **carrée creuse** dans un catalogue.
  - **Efforts tranchants T_y et efforts normaux N** : introduits et diagrammés une seule fois, dans l'activité 6 (grue d'atelier).
  - **Outillage** : logiciel de calcul **Winflex** (activité 2) ; QR-codes renvoyant à des ressources PDF/EXE (p.216, 235, 240, 250, 251).

- ⛔ **EXCLU / seulement mentionné, jamais traité dans ces pages** :
  - Les **encadrés de cours ne figurent que dans la Synthèse (p.250–251)** : les six activités ne contiennent aucune définition ni formule de cours, hormis la formule du moment idéal de flexion rappelée en note d'énoncé (p.232, 238, 244). Aucune démonstration n'est donnée.
  - **Traction / compression simples, cisaillement simple, flambage, matage** : jamais traités ici ; seuls la « limite élastique à la traction R_e » et le terme « limite élastique au cisaillement R_eg » sont utilisés comme données.
  - Le **calcul de la flèche** en flexion n'est jamais formalisé : la flèche est mesurée expérimentalement, lue en simulation, et la loi f = k.L³ est seulement *choisie* parmi quatre propositions ; aucune formule de flèche n'est imprimée dans la synthèse.
  - Le **θ_limite** est déclaré « fixé par l'expérience » : aucune valeur numérique n'est donnée nulle part dans la tranche.
  - Les **concentrations de contraintes**, la **fatigue**, les **contraintes de Von Mises / Tresca** ne sont pas nommées ; la contrainte équivalente apparaît uniquement comme colonne « σ_éq » d'un tableau à remplir (p.249), sans formule imprimée.
  - Les **colonnes « Matière » et « Observation » de la nomenclature p.218 sont vides** (travail d'élève) ; la nomenclature du micro-tour (p.227) est explicitement **partielle** (repères 8 à 22 seulement, les repères 1 à 7 ne sont jamais donnés).
  - La **« Grille d'évaluation comportement des solides déformables »** est annoncée en dernière ligne de la p.251 mais n'est pas imprimée : elle est renvoyée au QR-code PDF.
  - Les **corrigés** et toute valeur de résultat : aucune application numérique n'est résolue dans le manuel ; toutes les cases et lignes sont vierges.

### AXE 3 — La réalisation et la production (p.252–288)

#### Thème : Obtention des pièces (p.252–288)

##### Ouverture de l'AXE 3 et du thème (p.252)

Page d'ouverture en bandeaux colorés (bleu = axe, vert = thème, magenta = séquence, bleu clair =
compétences), avec deux QR-codes marqués **PDF**. Aucun numéro de page imprimé sur cette page.

- **Bandeaux d'ouverture (verbatim)** :

> **AXE 3**
> **RÉALISATION ET PRODUCTION**
>
> **THÈME**
> **OBTENTION DES PIÈCES**
>
> **SÉQUENCE**
> - Obtention des pièces par enlèvement de matière
> - Obtention des pièces par méthode additive
> - Métrologie
> - Plasturgie
>
> **COMPOSANTES DES COMPÉTENCES DISCIPLINAIRES**
> CD 3.9: Décoder un document de fabrication.
> CD 2.6: Mettre en œuvre les machines conventionnelles et les micro-machines à commande
> numérique (MOCN) pour réaliser une pièce simple.
> CD2.8 : Mettre en œuvre les composantes d'une chaine numérique de fabrication additive.
> CD2.7 : Contrôler une pièce.

- **Tableau « Obtention des pièces » (p.252)** — colonnes *CD* / *Savoirs et savoir-faire* /
  *Critères d'évaluation*. ⚠️ Dans la source, la colonne « Savoirs » est décalée d'une ligne par
  rapport aux étiquettes CD ; la transcription ci-dessous respecte la position imprimée de chaque
  bloc :

| CD | Savoirs et savoir-faire | Critères d'évaluation |
| --- | --- | --- |
| CD 3.9 | **Obtention des pièces par enlèvement de matière:**<br>- Contrainte d'antériorité (Rappel).<br>- Positionnement isostatique et moyen d'ablocage (Rappel).<br>- Cotes de fabrication.<br>- Lecture et rédaction d'un document de fabrication.<br>- Programmation simple en code ISO. | - Lecture correcte d'un document de fabrication.<br>- Détermination correcte des cotes de fabrication.<br>- Rédaction correcte d'un document de fabrication.<br>- Calcul exact de la vitesse de rotation et la vitesse d'avance. |
| CD 2.6 | - Réalisation des opérations d'usinage sur les machines conventionnelles et les micromachines.<br>**Obtention des pièces par méthode additive**: impression 3D. | - Programmation adéquate d'un usinage sur les machines à commande numérique (MOCN). |
| CD 2.8 | **Métrologie dimensionnelle et géométrique.**<br>**Plasturgie:** | - Impression 3D réussie. |
| CD 2.7 | Principe de: l'injection, l'injection-soufflage, l'extrusion gonflage, l'extrusion soufflage, thermoformage, rotomoulage | - Contrôle adéquat d'une pièce. |

- **Vocabulaire & terminologie officielle (p.252)** : enlèvement de matière ; méthode additive ;
  métrologie ; plasturgie ; contrainte d'antériorité ; positionnement isostatique ; moyen
  d'ablocage ; cotes de fabrication ; document de fabrication ; code ISO ; machines
  conventionnelles ; micromachines ; MOCN ; impression 3D ; injection ; injection-soufflage ;
  extrusion gonflage ; extrusion soufflage ; thermoformage ; rotomoulage.

---

##### Activité — Bateau à pédales (Plasturgie) (p.253–256)

- **Système / support d'étude** : un **pédalo** (bateau à pédales), produit complet en matières
  plastiques, avec sa coque, ses accessoires d'entraînement et son gouvernail.
- **Compétences affichées** : bandeau de tête **CD 3.9 / CD 2.6 / CD 2.8 / CD 2.7** (imprimé en
  pastille bleue sur p.255 ; absent des p.253, p.254 et p.256). En-tête courant des quatre
  pages : « OBTENTION DES PIECES » [sic, sans accent] / « **PLASTURGIE** ».
- **Pictogrammes de compétences transversales (p.255)** : **COMM**, **COOP**.
- **Ressources fournies** : dossier technique = Fig. 1 et Fig. 2 (p.253), planches photo des
  accessoires (p.253), nomenclature 18 repères (p.254), caractéristiques commerciales du pédalo
  (p.254), schéma du principe de rotomoulage en 4 vignettes (p.256), 3 photos d'objets à
  identifier (p.256). QR-codes **Vid** (vidéos) sur p.253, p.255 (×2) et p.256.

###### 1. Mise en situation (p.253)

> Un pédalo, ou bateau à pédales fig1 et 2, est un petit bateau dont le principe est de pédaler
> pour avancer grâce à des roues à aube (pales, hélice). C'est une activité qui se pratique sur
> les lacs, la mer ou certaines rivières, elle est accessible à tous et ne nécessite aucune
> compétence technique particulière.

**Figures (p.253)** — *décrites, non recopiées* :
- **Fig. 1** : photo du pédalo complet en vue 3/4 avant, avec auvent déployé. Repères fléchés
  visibles : **18** (toile/auvent), **6** (coque), **5** (poignée avec écrou), **16** (pale de
  roue, sous la coque), **2** (bielle, tube posé au sol devant le bateau).
- **Fig. 2** : photo du pédalo vu de dessus. Repères fléchés visibles : **6**, **5**, **1**
  (bouchon de drain), **8** (pédale), **10** (pédalier régulier), **14** (guidon et tige),
  **3** (dossier ajustable), **17** (couvercle pour glacière).
- **Accessoires d'entraînement** (4 vignettes photo) : **4** (moyeu, tube + visserie), **7**
  (bagues de roulement, 2 pièces bleues + 2 anneaux), **9** (étoile noire à 5 branches + vis),
  **16** (pale de roue noire).
- **Accessoires du gouvernail** (4 vignettes photo) : **11** (gouvernail, safran noir), **12**
  (axe de gouvernail, tube + bague), **13** (ensemble de coude régulier, pièce coudée noire +
  vis + écrou), **15** (perce-coque blanc).

###### 2. Nomenclature (p.254)

| Rep. | Nbr. | Désignation | Matière | Observation |
| ---: | ---: | --- | --- | --- |
| 1 | 1 | Bouchon de drain | Polyéthylène | |
| 2 | 1 | Bielle | Aluminium | |
| 3 | 2 | Dossier ajustable | Polyester | |
| 4 | 1 | Moyeu | Aluminium | |
| 5 | 1 | Poignée avec écrou | Phénoplaste | |
| 6 | 1 | Coque | Polyéthylène | |
| 7 | 4 | Bague de roulement | Polyoxyde de Méthylène | |
| 8 | 4 | Pédale | Phénoplaste | |
| 9 | 1 | Etoile | Plastique | |
| 10 | 2 | Pédalier régulier | Aluminium marin | |
| 11 | 1 | Gouvernail | Phénoplaste | |
| 12 | 1 | Axe de gouvernail | Acier inox | |
| 13 | 2 | Ensemble de coude régulier | Polyéthylène | |
| 14 | 1 | Guidon et tige | Acier inox | |
| 15 | 2 | Perce-coque | Phénoplaste | |
| 16 | 5 | Pale de roue | Polyéthylène | |
| 17 | 2 | Couvercle pour glacière | Polyéthylène | |
| 18 | 1 | Toile | Polyester | |

###### 3. Caractéristiques (p.254)

> Résistant : Grande résistance aux chocs.
> - **Confortable :** Permet de naviguer en tout confort grâce aux deux dossiers ajustables qui
>   s'adaptent pour les sièges orientés vers l'avant et vers l'arrière.
> - **Rangement :** Ce pédalo comprend quatre porte-verres et un compartiment de
>   réfrigération/stockage intégré équipé de couvercles solides. Il comprend également un auvent
>   pliable pour vous protéger pendant une journée au soleil.
> - **Haute capacité :** Le pédalo peut accueillir jusqu'à 5 personnes et a une capacité maximale
>   de 350 Kg.
> - **Transport facile :** Avec ses poignées de transport à l'avant et à l'arrière, il est facile
>   à transporter jusqu'au bord de l'eau.

###### I. Situation problème (p.255)

> Les techniques de transformation de la matière plastique diffèrent d'une pièce à une autre.
>
> **Qu'elles [sic] techniques peut-on adopter pour l'obtention des différents éléments du pédalo
> et en particulier la coque (6) ?**

###### II. Travail demandé (p.255–256)

Consigne d'entrée : « En se référant à la nomenclature et aux figures 1 et 2 du dossier
technique ».

1. **a.** « Compléter le tableau de tri des pièces. » — tableau à deux colonnes à remplir :
   *Pièces métalliques* / *Pièces non métalliques*, une seule ligne intitulée « Repères de
   pièces ». (Réponses non imprimées.)
2. **b.** « Citer les caractéristiques des deux familles de la matière plastique. » — deux
   amorces à compléter : « Les Thermoplastiques : … » et « Les Thermodurcissables : … ».
3. **c.** « Compléter le tableau ci-dessous en indiquant la matière plastique correspondante à
   chaque pièce du Pédalo. (Mettre une croix dans la case qui convient). » — tableau vide à
   3 colonnes *Pièce* / *Thermoplastique* / *Thermodurcissable*, lignes :
   **Dossier ajustable (3)** ; **Moulure (coque) (6)** [sic — la nomenclature p.254 désigne le
   repère 6 par « Coque »] ; **Bague de roulement (7)** ; **Perce-coque (15)**.
4. **d.** « La matière de la toile (18) du pédalo est le Polyester ; cette matière est-elle
   recyclable ? »
5. **e.** « Parmi les procédés de transformation de la matière plastique, on a la transformation
   par injection et par injection soufflage. Quelle est la différence entre les deux procédés? »
   — deux amorces à compléter : « Le principe de l'Injection : … » et « Le principe de
   l'injection soufflage : … ». Deux QR-codes **Vid** en marge.
6. *(p.256, suite de e.)* « La coque du pédalo est obtenu [sic] par rotomoulage, expliquer
   brièvement ce principe. » — 5 lignes à compléter, QR-code **Vid** en marge.
7. **f.** « Numéroter les étapes du principe de rotomoulage du Pédalo. » — s'appuie sur la figure
   à 4 vignettes ci-dessous.
8. **g.** « Compléter par vrai ou faux » — quatre affirmations, chacune suivie d'une case à
   cocher :
   - « Le rotomoulage a une capacité de produire des pièces d'une très grande complexité
     technique »
   - « Le rotomoulage permet une grande résistance aux pièces fabriquée [sic] »
   - « Le rotomoulage est adapté à la production des pièces en petite et moyenne séries avec un
     coût d'outillage relativement élevé »
   - « En rotomoulage, 90% seulement de la matière sera recyclée »
9. **h.** « Indiquer le type de procédé utilisé pour l'obtention de chaque objet : » — tableau à
   3 colonnes avec une photo par colonne et une ligne de pointillés à remplir :
   **Coque (6)** (photo de coque bleue et blanche) / **Dossier (3)** (photo de dossier bleu) /
   **Couvercle (17)** (photo de deux couvercles bleus nervurés).

**Figure du principe de rotomoulage (p.256)** — *décrite* : bandeau gris de 4 vignettes montrant
un moule en bout de bras oscillant. Légendes imprimées, dans l'ordre de lecture :
« Moule ouvert » + « Support du moule » + « Matière sous forme de poudre » (vignette 1) ;
« Mouvement de balancier » + « La matière fond et adhére [sic] au moule » (vignette 2) ;
« La matière cristallise et durcit » (vignette 3, avec pictogramme de ventilateur) ;
« Pièce réalisée » (vignette 4, moule rouvert et pièce verte extraite).

- **Vocabulaire & terminologie officielle (p.253–256)** : matière plastique ;
  thermoplastique / thermodurcissable ; polyéthylène ; polyester ; phénoplaste ; polyoxyde de
  méthylène ; aluminium marin ; acier inox ; recyclable ; injection ; injection soufflage ;
  rotomoulage ; roue à aube ; pale ; hélice ; coque ; gouvernail ; pédalier ; moyeu ;
  perce-coque ; bague de roulement.

---

##### Projet 1 — Maquette d'un train épicycloïdal (p.257–280)

Dossier de réalisation guidée en **20 étapes numérotées**, suivi d'un volet **fabrication
additive**. En-tête courant : « OBTENTION DES PIECES » / « **PROJET** » à partir de p.258
(⚠️ p.257 porte encore « PLASTURGIE » — voir § Incertitudes). Bandeau de tête **CD 3.9 / CD 2.6 /
CD 2.8 / CD 2.7** sur p.258 à p.280.

- **Système / support d'étude** : maquette de laboratoire d'un **train épicycloïdal** (train
  planétaire) à 3 satellites, entraînée à la main par un volant, montée sur semelle avec deux
  paliers, une couronne, un porte-satellite, un pignon et une roue.
- **Pictogrammes de compétences transversales (p.257)** : **COMM**, **COOP**, **R. PRO**, **CREA**.
- **Ressources fournies (tout le dossier)** : bête à cornes (p.257), diagramme pieuvre (p.258),
  tableau des fonctions de service (p.258), tri croisé + histogramme (p.258–259), cahier des
  charges fonctionnel (p.259), actigramme A-0 (p.259), 3 schémas de trains épicycloïdaux
  (p.260), FAST partiel (p.261), schéma cinématique (p.262), dessin 3D (p.265), perspective
  éclatée (p.266), dessin d'ensemble 4 vues (p.267), nomenclature 37 repères (p.268), 4 dessins
  de définition (p.269–272, p.277), feuille d'avant-projet d'étude de fabrication 2 pages
  (p.273–274), contrat de phase (p.275), tableau de programmation ISO (p.276, p.279), procédure
  d'usinage de la douille (p.277–278), fiche de fabrication additive (p.280). QR-codes **Vid**
  (p.262–263), **PDF** (p.269, p.272) et **ZIP** (p.280).

###### I. Situation problème (p.257)

> **A partir d'un mouvement d'entrée « source » à vitesse constante.**
> - **Transmettre deux puissances motrices de rotation en variant le couple et la vitesse aux
>   besoins du récepteur.**
> - **Permettre la réversibilité de la transmission.**
> - **Bon rendement.**
> - **Encombrement réduit.**
>
> **Comment étudier et concevoir un mécanisme de transmission qui répond à ces conditions ?**

###### II. Travail demandé (p.257)

> Faite [sic] une étude complète et structurée pour répondre à ce besoin tout en respectant les
> étapes de la démarche de projet et en exploitant les équipements et le matériel disponibles au
> laboratoire.

###### Étape 1 — Expression de besoin (p.257)

Diagramme « bête à cornes » du **Mécanisme de transmission** :
- *A qui rend-il service ?* → **Utilisateur**
- *Sur quoi agit-il ?* → **Deux puissances motrices de rotation**
- *Dans quel but ?* → **Transmettre deux puissances motrices de rotation en variant le couple et
  la vitesse aux besoins du récepteur.**

###### Étape 2 — Valider le besoin (p.257)

> **Pourquoi le produit existe-t-il ?**
> L'existence limitée des organes mécaniques qui transmettent deux mouvements de rotation à
> l'entrée en adaptant le couple et la vitesse aux besoins du récepteur.
> **Qu'est ce qui pourrait faire évoluer le besoin ?**
> Une nouvelle technologie.
> **Qu'est ce qui pourrait faire disparaitre ce besoin ?**
> La disparition de l'organe récepteur.
> Une nouvelle technologie à coût modéré.
> **Conclusion :** Le besoin est validé.

###### Étape 3 — Recensement des FS (p.258)

Diagramme pieuvre centré sur **MECANISME DE TRANSMISSION**, avec 8 milieux extérieurs :
**Organe récepteur** (FP1), **Energies mécaniques** (FC1), **Stabilité** (FC2), **Sécurité**
(FC3), **Milieu ambiant** (FC4), **Coût** (FC5), **Esthétique** (FC6), **Utilisateur** (FC7).
FP1 relie *Organe récepteur* et *Utilisateur*.

###### Étape 4 — Formulation des fonctions de service (p.258)

| F. S | Expression des fonctions de service |
| --- | --- |
| FP1 | Permettre à l'utilisateur la transmission de deux puissances mécaniques de rotation en variant le couple et la vitesse aux besoins du récepteur. |
| FC1 | Entrainer manuellement la maquette. |
| FC2 | Être stable en fonctionnement. |
| FC3 | Etre ergonomique et respecter les normes de sécurité. |
| FC4 | S'adapter à l'environnement. |
| FC5 | Avoir un coût modéré. |
| FC6 | Avoir une forme esthétiquement acceptable. |
| FC7 | S'adapter à la source de mouvement. |

###### Étape 5 — Valorisation et hiérarchisation des fonctions de service (p.258)

Tri croisé (chaque cellule = fonction gagnante / note de supériorité) :

| | FC1 | FC2 | FC3 | FC4 | FC5 | FC6 | FC7 | Points | % |
| --- | --- | --- | --- | --- | --- | --- | --- | ---: | ---: |
| **FP1** | FP1/2 | FP1/2 | FP1/2 | FP1/2 | FP1/3 | FP1/3 | FP1/2 | 16 | 32 |
| **FC1** | | FC1/2 | FC1/2 | FC1/2 | FC1/3 | FC1/2 | FC1/2 | 13 | 26 |
| **FC2** | | | FC2/1 | FC2/2 | FC2/3 | FC2/2 | FC2/1 | 9 | 18 |
| **FC3** | | | | FC3/0 | FC3/2 | FC3/1 | FC3/2 | 5 | 10 |
| **FC4** | | | | | FC4/1 | FC4/1 | FC4/1 | 3 | 6 |
| **FC5** | | | | | | FC6/1 | FC5/1 | 1 | 2 |
| **FC6** | | | | | | | FC7/2 | 1 | 2 |
| **FC7** | | | | | | | | 2 | 4 |
| | | | | | | | **Total** | **50** | **100%** |

Barème encadré (verbatim) :

> | 0 | Pas de supériorité |
> | 1 | Légèrement supérieure |
> | 2 | Moyennement supérieure |
> | 3 | Nettement supérieure |

###### Étape 6 — Histogramme des souhaits (p.259)

Diagramme en barres, ordonnée « Souhait en % » graduée 15 et 30, abscisse « Fonctions » ; barres
dans l'ordre **FP1, FC1, FC2, FC3, FC4, FC5, FC6, FC7**, décroissantes et conformes aux
pourcentages du tri croisé (32, 26, 18, 10, 6, 2, 2, 4).

###### Étape 7 — Cahier des charges fonctionnel (p.259)

| F. S | Expression | Critères d'appréciation | Niveaux | Flexibilités |
| --- | --- | --- | --- | --- |
| FP1 | Permettre à l'utilisateur la transmission de deux puissances mécaniques de rotation en variant le couple et la vitesse aux besoins du récepteur. | Puissance d'entrée<br>Rapports de vitesses r<br>Rendement | P = 10 W<br>r<sub>i</sub> de 0,25 à 4<br>η ≈ 0,9 | ± 1 W<br><br>± 0,05 |
| FC1 | Entrainer manuellement la maquette. | Couple<br>Vitesse | C ≈ 1 N.m<br>90 trs/min | ± 0,2 N.m<br>± 5 trs/min |
| FC2 | Être stable en fonctionnement. | Stabilité<br>Support<br>Encombrement<br>Masse. | L x H x l = 280x220x180<br>Masse = 2 Kg | ± 1 mm<br>± 50 g |
| FC3 | Etre ergonomique et respecter les normes de sécurité. | Sécurité<br>Norme en vigueur | | |
| FC4 | S'adapter à l'environnement. | Matériaux durables et sanitaire | | |
| FC5 | Avoir un coût modéré. | Coût | | |
| FC6 | Avoir une forme esthétiquement acceptable. | Forme<br>Couleur | Choix en fonction de la sensibilité de l'utilisateur | |
| FC7 | S'adapter à la source de mouvement. | Manœuvre manuelle<br>Vitesse de rotation | N<sub>maxi</sub> = 90 trs/min | |

###### Étape 8 — Modélisation (p.259)

Actigramme **A-0** : fonction centrale « Transmettre deux puissances mécaniques de rotation en
variant le couple et la vitesse aux besoins du récepteur » ; entrée matière « Deux puissances
mécaniques » ; sorties « Couple et vitesse au besoin du récepteur » et « Bruit » ; données de
contrôle « Réglage », « Contrôle », « Utilisateur » ; support « Mécanisme de transmission ».

###### Étape 9 — Approche fonctionnelle (p.260)

> Un train épicycloïdal (ou train planétaire) est un train d'engrenages dont au moins une roue
> dentée (appelée satellite) est en mouvement épicycloïdal par rapport au carter fixe.

Trois cas, chacun avec un texte, un actigramme simplifié et un schéma cinématique (éléments
repérés 1, 2, 3, 4 et « Bâti (0) ») :

- **Cas 1 : Transmettre et adapter** — *« On peut bloquer un élément et conserver une entrée, une
  sortie. On assure ainsi les mêmes fonctions qu'un réducteur classique mais avec des
  performances élevées (réduction d'encombrement). »*
  Actigramme : P1 → « Transmettre et adapter » → P3. Effets listés : *Adapter la puissance ;
  Augmenter le couple ; Réduire la vitesse.* Schéma : entrée **E₁**, sortie **S₃**.
- **Cas 2 : Transmettre et répartir** — *« On peut également transmettre et répartir la puissance
  d'un même moteur à 2 récepteurs différents (1E/2S). (Transmission classique ou intégrale de
  véhicule). »* Actigramme : P1 → « Transmettre et répartir » → P3 et P4. Effets : *Répartir la
  puissance ; Répartir le couple ; Différencier les vitesses.* Schéma : **E₁** en entrée, **S₃**
  et **S₄** en sorties.
- **Cas 3 : Transmettre et combiner** — *« On peut également gérer et optimiser 2 puissances
  motrices tout en variant la vitesse du récepteur (véhicule hybride). »* Actigramme : P1 et P3 →
  « Transmettre et combiner » → P4. Effets : *Combiner 2 puissances motrices ; Augmenter le
  couple ; Varier la vitesse.* Schéma : **E₁** et **E₃** en entrées, **S₄** en sortie.

###### Étape 10 — Recherche des solutions associées aux fonctions techniques (FAST) (p.261)

> **Le diagramme FAST partiel de la fonction FT1**
> Les solutions constructives associées aux fonctions techniques qui contribuent à la
> satisfaction de la fonction technique FT1 : « Transmettre manuellement un mouvement de rotation
> de l'arbre planétaire au satellite».

| Fonction | Énoncé | Solutions associées aux fonctions |
| --- | --- | --- |
| **FT1** | Transmettre manuellement un mouvement de rotation de l'arbre planétaire au satellite. | |
| **FT11** | Entrainer manuellement l'arbre d'entrée en rotation. | Manivelle / **Volant** *(retenue)* |
| **FT12** | Transmettre la vitesse de l'arbre planétaire au satellite. | |
| **FT121** | Lier l'arbre d'entrée à l'élément d'entraînement | **Liaison rigide démontable** *(retenue)* / Liaison rigide indémontable |
| **FT122** | Guider l'arbre d'entrée en rotation | Palier direct / Roulement / **Coussinet** *(retenue)* |
| **FT123** | Lier le planétaire à l'arbre d'entrée | **Liaison rigide démontable** *(retenue)* / Liaison rigide indémontable |
| **FT124** | Adapter le mouvement des satellites | **Engrenages : planétaire - satellites - couronne** *(retenue)* |

Légende imprimée : case jaune « : Solution retenue ».

> **Justification du choix des solutions constructives**
> On prend le cas d'un train épicycloïdal simple à trois satellites : les composants sont moins
> sollicités, dimensionnés en conséquence, donc moins volumineux et moins lourd. Le
> porte-satellite en particulier est parfois monté "flottant" et donc auto-centré par les
> satellites.
>
> **FT1** : le choix du volant est pris pour des raisons économique, ergonomique et de fabrication
> selon les équipements disponibles au laboratoire de GM.
> **FT121 et FT123** : le choix d'une liaison rigide est pris pour avoir une transmission de
> mouvement de rotation ; et démontable pour l'entretien et la maintenance.
> **FT122** : le guidage de l'arbre d'entrée en rotation par coussinet, résulte des efforts
> résistants et faible vitesse à transmettre.

###### Étape 11 — Schéma cinématique (p.262)

Schéma cinématique plan du train, repères **1, 2, 3, 4**, liaison au **Bâti (0)** (deux
hachurages de bâti), et un bloc encadré « **Roue** » relié en bas de chaîne par un dernier
engrenage. Tracé en 4 couleurs (rouge = arbre d'entrée, magenta = planétaire, vert = satellite /
sortie, bleu = couronne / porte-satellite).

###### Étape 12 — Étude cinématique (p.262–263)

**Données de l'énoncé** :
- Vitesse d'entrée **N<sub>e</sub> = 90 trs/min**, « c'est la vitesse du volant à entrainer ».
- **N<sub>s</sub>** = vitesse de rotation de sortie ; rapport de transmission **r = N<sub>s</sub>/N<sub>e</sub>**,
  « varie selon la configuration du train épicycloïdal ».
- Dentures : **Z₂₅ = Z₂₆ = 18 dents**, **Z₃₁ᵢₙₜ = 54 dents**, **Z₃₁ₑₓₜ = 72 dents** et
  **Z₃₃ = 24 dents**.

**Rapports de transmission possibles du train épicycloïdal** — 3 cas × 2 possibilités, chacun
résolu par la formule de Willis (QR-codes **Vid** en marge de chaque possibilité) :

| Cas | Possibilité | Formule de Willis imprimée | Résultat |
| --- | --- | --- | --- |
| **1er cas : couronne (31) bloquée** | 1ère : planétaire (26) menant ; porte satellite (11) mené | r₁ = N₁₁/N₂₆ = Z₂₆/(Z₃₁ᵢₙₜ + Z₂₆) = 18/(54 + 18) = 1/4 = 0.25 | N<sub>s</sub> = r₁·N<sub>e</sub> = 0,25 · 90 = **22,5 tr/min** ; réducteur non-inverseur. |
| | 2ème : porte satellite (11) menant ; planétaire (26) mené | r₁' = N₂₆/N₁₁ = (Z₃₁ᵢₙₜ + Z₂₆)/Z₂₆ = (54 + 18)/18 = 4 | N<sub>s</sub> = r₁'·N<sub>e</sub> = 4 · 90 = **360 tr/min** ; Multiplicateur non-inverseur |
| **2ème cas : planétaire (26) bloqué** | 1ère : Couronne (31) menant ; porte satellite (11) mené | r₂ = N₁₁/N₃₁ = Z₃₁ᵢₙₜ/(Z₃₁ᵢₙₜ + Z₂₆) = 54/(54 + 18) = 3/4 = 0.75 | N<sub>s</sub> = r₂·N<sub>e</sub> = 0,75 · 90 = **67,5 tr/min** ; réducteur non-inverseur |
| | 2ème : porte satellite (11) menant ; Couronne (31) menée | r₂' = N₃₁/N₁₁ = (Z₃₁ᵢₙₜ + Z₂₆)/Z₃₁ᵢₙₜ = (54 + 18)/54 = 4/3 = 1.33 | N<sub>s</sub> = r₂'·N<sub>e</sub> = 1,33 · 90 = **120 tr/min** ; Multiplicateur non-inverseur |
| **3ème cas : porte satellite (11) bloqué** *(p.263)* | 1ère : planétaire (26) menant ; Couronne (31) menée | r₃ = N₃₁/N₂₆ = −Z₂₆/Z₃₁ᵢₙₜ = −18/54 = −1/3 = − 0.33 | N<sub>s</sub> = r₃·N<sub>e</sub> = −0,33 · 90 = **−30 tr/min** ; réducteur inverseur |
| | 2ème : Couronne (31) menant ; planétaire (26) mené | r₃' = N₂₆/N₃₁ = −Z₃₁ᵢₙₜ/Z₂₆ = −54/18 = − 3 | N<sub>s</sub> = r₃'·N<sub>e</sub> = −3 · 90 = **−270 trs/min** ; Multiplicateur inverseur. |

###### Étape 13 — Statique (p.263)

> Couple appliqué par le volant (28)
> C₂₈ = F₂₈/₂₇ . R₂₈ = 1080 N.mm ; F₂₈/₂₇ = 30 N
> P₂₈ = C₂₈ . π . N<sub>e</sub> / 30 = 10.17 W
> Rendement η = 0.98

###### Étape 14 — RDM (p.263–264)

**a) Calcul de résistance des dentures (p.263)**

> **Calcul de résistance des dentures :**
> Pendant l'engrènement, les efforts de l'action inter dentaire sont exercés en M par le satellite
> (25) sur le planétaire (26).
>
> T : Effort tangentiel utile à la transmission
> R : Effort radial transmis aux paliers
>
> **Hypothèses :**
> - La denture de planétaire (26) est assimilée à une poutre encastrée, de section rectangulaire
>   pleine de section S = (k.m) . (π.m/2) sollicitée à la flexion ;
> - L'effort exercé en bout de dent (début d'engrènement) ;
> - Une seule dent en prise ;
> - Le planétaire (26) est en PLA de résistance pratique à l'extension R<sub>pe</sub> = 15 MPa.

Figures associées : profil de deux dents en prise (satellite **25** sur planétaire **26**) avec
la force **F₂₅/₂₆** décomposée en **T** (tangentiel) et **R** (radial), angle de pression **20°**
repéré ; puis modélisation en poutre encastrée en E, effort **T** appliqué à **2,25·m** de
l'encastrement, largeur de dent **k.m** et « Pas/2 » cotés.

Résultat imprimé :

> Le calcul nous donne : m<sub>mini</sub> ≥ 2,34 . √(T / (k . R<sub>pe</sub>)) en prenant K = 6 et T = 60 N ;
> on obtient : m<sub>mini</sub> ≥ 2,34 . √(60 / (6 . 15)) ; m<sub>mini</sub> ≥ 1,91 mm ; **choix m = 2 mm**

**b) Dimensionnement de l'arbre de planétaire (27) (p.264)**

> **Hypothèses :**
> - Toutes les pièces sont rigides et indéformables et toutes les liaisons sont parfaites.
> - Le poids est négligeable.
> - L'arbre est en PVC de résistance pratique à l'extension Rpe = 27,5 MPa.

Déroulé du calcul, verbatim des lignes imprimées :

> Vérification de la résistance de l'arbre du planétaire (27) à la flexion+torsion
> M<sub>t</sub> = C₂₈ = R₂₆ . T = 1080 N.mm avec : R₂₆ = m.Z₂₆/2 = 18 mm ; alors T = 60 N.
> - Les actions inconnues : F<sub>A</sub> = 470 N ; F<sub>B</sub> = 530 N
> - Le moment de flexion : Mf = 2400 N.mm
> - Le moment idéal : Mf<sub>idéal</sub> = √(Mf² + Mt²) = √((2400)² + (1080)²) = 2631,80 N.mm
> - Le diamètre minimal de l'arbre de planétaire (27) qui résiste à la flexion+torsion :
>   d₂₇ₘᵢₙᵢ ≥ ∛(32 . Mf<sub>idéal</sub> / (π . R<sub>pe</sub>)) ;
>   d₂₇ₘᵢₙᵢ ≥ ∛(32 . 2631,80 / (π . 27,5)) ; d₂₇ₘᵢₙᵢ ≥ 9,91 mm ; **choix d = 10 mm**

Schéma de la poutre (p.264) : axe x horizontal, points **O**, **A**, **B**, **C** ; force
**F₂₈/₂₇** appliquée en O (verticale vers le haut) ; appui A avec **F<sub>A</sub>** dirigée vers le
bas ; appui B avec **F<sub>B</sub>** dirigée vers le haut ; effort **T** vers le bas en C.
Cotes portées sur l'axe : **22,5** (O→A), **15** (A→B), **40** (B→C).

###### Étape 15 — Cotation fonctionnelle (p.264–265)

> Le bon fonctionnement de la maquette train épicycloïdal impose des conditions fonctionnelles
> telles que :

Deux extraits de dessin d'ensemble en coupe portent les chaînes de cotes :
- **Chaîne Ja** (pièces repérées 35, 33, 12, 5, 4, 32, 34) : **a₃₂ = Ja + a₃₅ + a₅ + a₄ + a₅' + a₃₄**
- **Chaîne Jb** (pièces repérées 17, 21, 22, 23) : **b₂₃ = Jb + b₁₇ + b₂₁ + b₂₂**
- **Chaîne Jc** : **c₂₂ = Jc + c₂₃**
- Note imprimée : *« **NB.** Pour le traçage de Jb, on suppose que (22) est en contact bilatéral
  avec (21) et (23) »*

Définitions des jeux (p.265) :

> Ja : Jeu fonctionnel axial pour assurer le guidage en rotation de l'arbre porte roue (32) par
> rapport au palier porte roue (4).
> Jb : Dépassement de taraudage sur le volant (17) assurant le serrage de la poignée (22).
> Jc : La tête cylindrique de la vis (23) est logée dans le lamage pour assurer la condition de
> sécurité.

###### Étape 16 — Dessin en 3D (p.265)

Vue 3D rendue en couleurs de la maquette assemblée : semelle grise en tôle pliée sur quatre
appuis, deux flasques circulaires (rouge à gauche portant le volant planétaire, verte à droite),
grande couronne dentée bleue à denture intérieure et extérieure, trois satellites rouges et un
satellite vert central, deux poignées noires cylindriques, une roue grise crantée en bas.

###### Étape 17 — Dessin en perspective éclatée (p.266)

Éclaté complet de la maquette dans un cadre, **repères 1 à 37** tous fléchés (repères visibles :
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37). Aucune cote.

###### Étape 18 — Dessin d'ensemble (p.267)

Dessin d'ensemble normalisé, cartouche : **Echelle : 2:5**, titre **« Maquette train
epicycloïdal »** [sic, sans accent], symbole de projection européenne.
Vues et coupes : **A-A** (coupe principale, repères fléchés 23, 22, 21, 16, 9, 10, 13, 24, 31,
25, 14, 26, 29, 15, 19, 3, 12, 17, 2, 20, 27, 18, 28, 37, 11, 6, 8, 30) ; **B-B** (repères 36,
33, 4, 35, 5, 32, 34 avec **Détail D — Echelle : 1:1**) ; **C-C** (vue de face, repères 1 et 7).
Traits de coupe A-A, B-B, C-C et détail D repérés sur les vues.

###### Étape 19 — Nomenclature (p.268)

| Rep. | Nbr. | Désignation | Matière | Observation |
| ---: | ---: | --- | --- | --- |
| 1 | 1 | Semelle | PVC | |
| 2 | 1 | Palier droit | PLA | |
| 3 | 4 | Coussinet à collerette | CuSn8P | Ø arbre 10 mm |
| 4 | 1 | Palier porte roue | PLA | |
| 5 | 2 | Coussinet à collerette | CuSn8P | Ø arbre 8 mm |
| 6 | 1 | Palier gauche | PLA | |
| 7 | 6 | Vis à tête cylindrique à six pans creux, M4-20 | | ISO 4762 |
| 8 | 6 | Rondelle plate M4 | | ISO 7092 |
| 9 | 1 | Disque volant satellite | PLA | |
| 10 | 3 | Arbre porte satellite | PVC | |
| 11 | 1 | Porte satellite | PLA | |
| 12 | 16 | Vis à tête fraisée à six pans creux, M4-16 | | ISO 10642 |
| 13 | 3 | Anneau élastique 10x1 | | |
| 14 | 3 | Rondelle plastique | PA 6 | |
| 15 | 1 | Arbre porte disque | PVC | |
| 16 | 2 | Clavette parallèle type C | | |
| 17 | 1 | Volant satellite | PLA | |
| 18 | 2 | Rondelle plate M8 | | ISO 4089 |
| 19 | 2 | Ecrou borgne M8 | | |
| 20 | 2 | Vis sans tête à six pans creux, M4-6 | | ISO 4026 |
| 21 | 2 | Ecrou hexagonal M8 | | ISO 7719 |
| 22 | 2 | Poignée | PA6 | |
| 23 | 2 | Vis à tête cylindrique fendue, M8-14-38 | | ISO 1580 |
| 24 | 5 | Coussinet | CuSn8P | |
| 25 | 3 | Satellite | PLA | m=2 ; Z=18 |
| 26 | 1 | Planétaire | PLA | m=2 ; Z=18 |
| 27 | 1 | Arbre planétaire | PVC | |
| 28 | 1 | Volant planétaire | PLA | |
| 29 | 1 | Porte planétaire | PLA | |
| 30 | 3 | Douille taraudé [sic] | PVC | |
| 31 | 1 | Couronne | PLA | m=2 ; Zint=54 ; Zext=72 |
| 32 | 1 | Arbre porte roue | PVC | |
| 33 | 1 | Pignon | PLA | m=2 ; Z= 24 |
| 34 | 1 | Anneau élastique, 8x0,7 | | |
| 35 | 1 | Rondelle plastique 8-14 | PA 6 | |
| 36 | 1 | Roue | PLA | |
| 37 | 1 | Goupille d'arrêt | C 30 | |

###### Étape 20 — Lecture et rédaction d'un document de fabrication (p.269–279)

**a) Dessin de définition de la semelle (1) (p.269)** — cartouche : Rp. 1, Nb. 1, *Semelle*,
matière **PVC**, **Echelle : 1:2**, « Maquette train epicycloïdal ». Vue de face (contour
octogonal à angles coupés) + coupe **C-C**. QR-code **PDF** en marge.
Cotes lisibles : épaisseur **10 (+0,1 / 0)** ; **66±0,1** ; **152,5±0,1** ; **214±0,1** ;
**250±0,2** ; **12±0,1** ; **15±0,2** ; **20,5±0,1** ; **30±0,1** ; **72±0,1** ; **84,5±0,1** ;
**160±0,2** ; chanfrein **30x45°** ; perçages **4xØ8** et **6xM4**.
Indications : **Ra 3,2** (état de surface général) ; **Tolérances générales ISO 2768 - mk**.

**b) Dessin de définition du porte satellite (11) (p.270)** — cartouche : Rp. 11, Nb. 1,
*Porte satellite*, matière **PLA**, **Echelle : 1:1**.
Vue de face (pièce à 3 bras à 120°) + coupe **A-A**.
Cotes lisibles : **R8** ; **R36** ; **R45** ; **Ø10H7** (×3, aux extrémités des bras) ;
**Ø16H7** (alésage central) ; **Ø4,5** ; **2,5x45°** ; **6 (+0,1 / 0)** ; **13±0,3**.
Tolérances explicitées : **Ø 16H7 = Ø 16 (+0,018 / 0)** ; **Ø 10H7 = Ø 10 (+0,015 / 0)**.
**Ra 3,2** ; **Tolérances générales ISO 2768 - mk**.

**c) Dessin de définition de l'arbre planétaire (27) (p.271)** — cartouche : Rp. 27, Nb. 1,
*Arbre planétaire*, matière **PVC**, **Echelle : 1:1**.
Vue de face en arbre étagé + coupe **A-A** + vue de gauche.
Cotes lisibles : **Ø8g6** ; **Ø9g6** ; **Ø10f7** ; **3N9** ; **M8** ; **3 (+0,1 / 0)** ;
**8 (+0,5 / 0)** ; **39 (+0,2 / 0)** ; **43±0,2** ; **7 (+0,1 / 0)** ; **6 (+0,1 / 0)** ;
**1±0,1** ; **2,5 (+0,1 / 0)** ; **0,25 (+0,1 / 0)** ; **0,5 (+0,1 / 0)** (×2) ;
**8 (+0,1 / 0)** ; **12±0,1** ; **69±0,05** ; **78±0,1**.
Spécifications géométriques cotées par rapport au référentiel **A** : symétrie **0,04 | A**
(×2) ; perpendicularité **⊥ 0,05 | A** ; coaxialité **Ø0,02 | A**.
Tolérances explicitées : **Ø 10f7 = Ø 10 (−0,013 / −0,028)** ; **Ø 9g6 = Ø 9 (−0,005 / −0,014)** ;
**Ø 8g6 = Ø 8 (−0,005 / −0,014)** ; **3N9 = 3 (−0,004 / −0,029)**.
**Ra 3,2** ; **Tolérances générales ISO 2768 - mk**.

**d) Dessin de définition de la couronne (31) (p.272)** — cartouche : Rp. 31, Nb. 1, *Couronne*,
matière **PLA**, **Echelle : 1:2**. QR-code **PDF** en marge.
Vue de face (couronne à denture intérieure et extérieure, 3 trous à 120°) + coupe **A-A**.
Cotes lisibles : **Ø 108** ; **Ø 144** ; **R 63** ; **Ø 10H7** (×3) ; **Ø 4,5** ;
**2,5x45°** ; **5 (+0,1 / 0)** ; **12±0,3**.
Tolérance explicitée : **Ø 10H7 = Ø 10 (+0,015 / 0)**.
Indications : **Chanfreins: 0,5x45° sauf indication** ; **Ra 3,2** ;
**Tolérances générales ISO 2768 - mk**.

**e) Feuille d'avant-projet d'étude de fabrication — arbre planétaire (27) (p.273–274)**

Consigne (p.273) : *« Lire et compléter les documents de fabrication, puis se référer de ces
documents, pour la réalisation des pièces demandées. »*

En-tête commun aux deux pages : **Feuille d'avant-projet d'étude de fabrication** —
Ensemble : Maquette train épicycloïdal · Élément : Arbre planétaire (27) · Matière : PVC ·
Nombre : Unitaire · Brut : Scié · **Bureau des méthodes** · pages **1/2** puis **2/2**.
Colonnes : *N° de phase* / *Désignation des phase-sous phase et opérations* /
*Machines-outils. Outils* / *Croquis de phase*.

| N° phase | Désignation des phase-sous phase et opérations | Machines-outils. Outils |
| ---: | --- | --- |
| **10** | Contrôle du brut | PC au 1/50 — croquis : **Ø12 ; L = 80** |
| **20** | **TOURNAGE**<br>Le référentiel est défini par : - Centrage long (1,2,3,4) - Appui ponctuel (5) - Serrage<br>a. Dresser (1) en finition directe Cm1= 79<sup>±0,5</sup><br>b. Charioter et dresser simultanément (2) et (3) en ébauche<br>c. Charioter et dresser simultanément (2) et (3) en demi-finition<br>d. Charioter et dresser simultanément (2) et (3) en finition en 2Cm2= Ø 10f7, Cm3= 40<sup>±0,5</sup><br>e. Charioter et dresser simultanément (4) et (5) en ébauche<br>f. Charioter et dresser simultanément (2) et (3) en demi-finition<br>g. Charioter et dresser simultanément (2) et (3) en finition 2Cm4= Ø 9g6 et Cm5= 71<sup>±0,1</sup><br>h. Chanfreiner (6):0,25 à 45°<br>i. Chanfreiner (7):0,25 à 45°<br>j. Centrer (8)<br>k. Percer (8) Co8 = 3,3<sup>±0,1</sup> | TP<br>Outil à charioter coudé en A.R.S<br>Outil à charioter couteau en A.R.S<br>Foret à center<br>Foret Ø3,3<br>CMD Ø10f7<br>CMD Ø9g6<br>Plaquette rugotest<br>PC au 1/50 |
| **30** | **TARAUDAGE MANUEL**<br>Le référentiel est défini par : - Centrage long (1,2,3,4) - Appui ponctuel (5) - Serrage<br>**Sécurité** *(en rouge)* - Ne pas mettre le tour sous tension<br>a. Tarauder (9) Co9=M4 | Tourne à gauche<br>Taraud ébauche M4<br>Taraud demi-finition M4<br>Taraud finition M4<br>Bague filetée M4 |
| **40** *(p.274)* | **TOURNAGE**<br>Le référentiel est défini par : (trois lignes de pointillés **à compléter par l'élève**)<br>a. Dresser (10) en finition directe Cm10 = 78<sup>±0,2</sup><br>b. Charioter (2) en ébauche<br>c. Charioter (2) en demi-finition<br>d. Charioter (2) en finition<br>e. Charioter et dresser simultanément (11) et (12) en ébauche<br>f. Charioter et dresser simultanément (11) et (12) en demi-finition<br>g. Charioter et dresser (11) et (12) en 2Cm10=Ø8g6 et Cm12= ?<br>h. Réaliser la gorge en 2Cm13=6.5<sup>±0,1</sup> et Cm13=69<sup>±0,05</sup><br>i. Chanfreiner (14) en : 0,5 à **45°**<br>j. Chanfreiner (15) en : 0,25 à 45°<br>**+ encadré « Recherche de Cm12: »** — 6 lignes de pointillés à compléter, le croquis de phase portant un « Graphe de transfert » repéré A | TP<br>Outil à charioter coudé en A.R.S<br>Outil à charioter couteau en A.R.S<br>Outil gorge A.R.S<br>CMD Ø10f7<br>CMD Ø8g6<br>PC au 1/50<br>Plaquette rugotest |
| **50** *(p.274)* | **FILETAGE MANUEL**<br>Le référentiel est défini par : - Centrage long (1,2,3,4) - Appui ponctuel (5) - Serrage<br>Sécurité - Ne pas mettre le tour sous tension<br>a. Fileter (2) en finition Co16=M8 | Porte – filières<br>Filière M8<br>Jauge de filetage |
| **60** *(p.274)* | **FRAISAGE**<br>Le référentiel est défini par : - Appui linéaire (1,2) - Appui linéaire (3,4) - Appui ponctuel (5) - Serrage<br>a. Rainurage de la pièce | MICRO-FRAISEUSE<br>Fraise à deux lèvres Ø3<br>Jauge de profondeur au 1/50 |

**f) Contrat de phase (p.275)** — **CONTRAT DE PHASE** · Ensemble : Maquette train épicycloïdal ·
Élément : Arbre planétaire 27 · **Phase N° 30** · Matière : PVC · Nombre : Unitaire ·
Bureau des méthodes · **1/1** · **Désignation : Tournage** · **Machine-outil : Tour parallèle**.
*(⚠️ la phase 30 de la FAPF p.273 est un taraudage manuel — voir § Incertitudes.)*
Croquis de phase : arbre étagé, symboles de mise en position 1, 2, 3, 4, 5 ; cotes machines
repérées **Cm10, Cm12, Cm13, 2Cm2, 2Cm11, 2Cm13, Co14** ; surfaces repérées 2, 10, 11, 12, 13,
14, 15.

Tableau des conditions de coupe (colonnes : *Désignation des opérations* / *Éléments de coupe*
[Vc (m/mn) · N (tr/mn) · f (mm/dent) · a (mm) · Vf (mm/min)] / *Outillage* [Fabrication ·
Vérification]) :

| Désignation des opérations | Vc (m/mn) | N (tr/mn) | a (mm) |
| --- | ---: | ---: | ---: |
| Dresser (10) en finition directe Cm10 = 78<sup>±0,2</sup> | 24 | 800 | 0.1 |
| Charioter (2) | | 800 | |
| Charioter et dresser simultanément (11) et (12) en ébauche | | | 0.1 |
| Charioter et dresser simultanément (11) et (12) en demi-finition | | 800 | |
| Charioter et dresser simultanément (11) et (12) en 2Cm11=Ø8g6 et Cm12=57<sup>±0,05</sup> | | | 0.1 |
| Réaliser la gorge en Cm13=69<sup>±0,1</sup> et 2Cm13=Ø6,5<sup>±0,1</sup> | | 800 | 0.2 |
| Chanfreiner (14) en : 0,5 à 45° | | 400 | |
| Chanfreiner (15) en : 0,25 à 45° | | | |

Outillage — *Fabrication* : « Outil à charioter coudé en A.R.S · Outil à charioter couteau en
A.R.S · Outil gorge en A.R.S » ; *Vérification* : « CMD Ø10f7 · CMD Ø8g6 · Plaquette rugotest ·
PC au 1/50 ». Les colonnes f (mm/dent) et Vf (mm/min) sont laissées vides.

**g) Préparation de la micro-fraiseuse — phase 60 de l'arbre planétaire (27) (p.276)**

Titre imprimé : « Dessin de définition de l'arbre planétaire (27) » *(reprise du titre de la
p.271 ; le contenu porte en réalité sur la programmation de la phase 60)*.

> On demande de préparer la machine micro-fraiseuse pour l'exécution de la phase 60 de l'arbre
> planétaire (27).
> a. Repérer les points qui définissent la trajectoire de l'outil et déterminer leurs coordonnées
> par rapport à l'origine pièce (OP) choisie.

- Tableau **Point / X / Y / Z** pour les points **1 à 8** — toutes les cases vides.
- Croquis coté de la pièce dans les plans (z,x) et (y,x) : cotes **7** (×3), **6**, **2,5**,
  **57** ; **OP** repérée en rouge sur l'extrémité gauche ; points 1 à 8 numérotés.
- **b.** « Donner les paramètres nécessaires à l'usinage de la pièce et compléter le programme en
  gcode » — trois amorces vides : **Vc = …** ; **N = …** ; **F= …**
- Tableau *Programme* / *Interprétation* à trous (les cases vides sont notées « … ») :

| Programme | Interprétation |
| --- | --- |
| % Phase 60 (Rainurage) | % : début de programme : phase 60 |
| N10 … M03 | M03 : rotation de la broche dans le sens horaire |
| N20 G95 T2 D2 M6 | G95 : avance exprimée en mm/tr |
| N30 … | G0 : avance rapide ; X=0 ; Y=0 ; Z=15 |
| N40 G1 F.1 Z-2 | G1 : interpolation linéaire ; Avance en mm/tr : … |
| N50 … | G1 : interpolation linéaire ; X= 6 ; Y=0 ; Z =-2 |
| N60 … | G0 : avance rapide ; Avance en mm/tr : … |
| N70 … | G0 : avance rapide ; X=53.5 ; Y=0 ; Z=15 |
| N80 … | G1 : interpolation linéaire ; Avance en mm/tr : … |
| N90 … | G1 : interpolation linéaire ; X= 60.5 ; Y=0 ; Z =-1.5 |
| N100 … | G0 : avance rapide ; Avance en mm/tr : … |
| N110 … | G0 : avance rapide ; X=60.5 ; Y=0 ; Z=15 |
| N120 … | M02 : fin du programme. |

Puis les consignes d'atelier :
> c. Ouvrir le logiciel Mach 3 (choisir le profil PX1).
> d. Ecrire le programme.
> e. Simuler le programme avant l'usinage.
> f. Appeler votre enseignant.
> g. Usiner la pièce.

**h) Dessin de définition et usinage de la douille taraudée (30) (p.277–279)**

> **Dessin de définition de la douille taraudée (30)**
> On veut préparer le micro-tour pour réaliser l'usinage de la douille taraudée (30).
> On donne le dessin de définition et la procédure d'usinage et le programme de la phase 20 de la
> pièce.

*Dessin de définition (p.277)* : coupe **A-A** + vue de gauche ; cotes **28** (longueur),
**Ø10**, **M4** ; indications imprimées : « Chanfreins: 0,5x45° » ; « Tolérances générales :
±0,1 » ; « Etat de surface général : Ra 3,2 » ; « Matière : PVC » ; **Echelle : 2:1**.

*Procédure d'usinage de la douille (p.277–278)* — colonnes *N° phase* / *Schéma* / *Machine* /
*Opération* / *Condition de coupe* :

| N° phase | Machine | Opération | Condition de coupe |
| ---: | --- | --- | --- |
| 10 | Scie mécanique | Ø12 ; L=30 — PC au 1/50 | |
| 20 | Micro-tour | Exécution de la phase 20 — Outil couteau | Vc=60 m/mn · N=1500 tr/mn · f=0.04 mm/tr |
| 30 | Micro-tour | Exécution de la phase 30 — Outil couteau | Vc=60 m/mn · N=1500 tr/mn · f=0.04 mm/tr |
| 40 *(p.278)* | Micro-tour | Exécution de la phase 40 — Mandrin de perçage · Foret à center · Foret Ø3,3 · Centrer et Percer Co1 = 3,3<sup>±0,1</sup> | Vc=60 m/mn · N=1500 tr/mn |
| 50 *(p.278)* | **Sécurité — Ne pas mettre le micro-tour sous tension** *(en rouge, à la place du nom de machine)* | Exécution de la phase 40 [sic] — Tourne à gauche · Taraud ébauche M4 · Taraud demi-finition M4 · Taraud finition M4 · Bague filetée M4 · Taraudage manuelle Co2=M4 | |

*Questions (p.278–279)* :
- **a.** « Repérer les points qui définissent la trajectoire de l'outil et déterminer leurs
  coordonnées par rapport à l'origine pièce (OP) choisie de la phase 30. »
  Croquis en repère (X, Z) avec **OP** en rouge et les points **1 à 7** placés.
  Tableau à compléter (valeurs déjà imprimées en gras ci-dessous, le reste en pointillés) :

  | Point | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
  | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
  | X | **8** | … | … | … | … | **8** | … |
  | Z | **-1** | … | … | … | … | … | **20** |

- **b.** (p.279) « On tenant [sic] compte des paramètres nécessaires à l'usinage de la pièce,
  écrire le programme en gcode de la phase 30. » — deux croquis de trajectoire côte à côte :
  celui de la phase 20 (points **A, B, C, D, E, F, G** et OP) et celui de la phase 30 (points
  **1 à 7** et OP). Tableau à deux colonnes, la gauche donnée, la droite à écrire :

  | Programme de la phase 20 | Programme de la phase 30 |
  | --- | --- |
  | % Phase 20 | … |
  | N10 S1500 M03 | N10 … |
  | N20 G95 T1 D1 M6 | N20 … |
  | N30 G00 X8 Z-1 (Approche) | N30 … X8 Z-1 … |
  | N40 G01 X0 Z-1 F0.04 (Dressage) | N40 … |
  | N50 G01 X4.5 Z-1 | N50 … |
  | N60 G01 X5 Z-1.5 | N60 … |
  | N70 G01 X5 Z-15 | N70 … |
  | N80 G01 X8 Z-15 | N80 … X8 Z-15 |
  | N90 G00 X8 Z20 (Dégagement) | N90 … X8 Z20 |
  | N100 M02 | N100 … |

- **c.** « On demande de préparer la machine micro-tour pour l'exécution de la phase 20. »
  1. Ouvrir le logiciel Mach 3 (choisir le profil PC1).
  2. Ecrire le programme.
  3. Simuler le programme avant l'usinage.
  4. Appeler votre enseignant.
  5. Usiner la pièce.

###### Obtention des pièces par méthode additive (p.280)

Fiche de fabrication additive du **porte satellite (11)** :
Ensemble : Maquette train épicycloïdal · Élément : Porte satellite (11) · Matière : PLA ·
Nombre : Unitaire · **Brut : Filament PLA**.
Colonnes *Etape* / *Démarche* / *Présentation* (capture d'écran ou photo par étape) :

| Etape | Démarche |
| ---: | --- |
| **1** | **CONCEPTION** (Logiciels 3D et 2D)<br>a. Modéliser la pièce en 3D à l'échelle 1<br>b. Modéliser la pièce à l'aide de référence<br>c. Mailler : exporter le fichier pour le tranchage en format .STL |
| **2** | **TRANCHAGE** (Logiciels Repetier-Host, Slicer ou Cura …)<br>a. régler la densité de remplissage et le type d'adhésion au plateau<br>b. Trancher et découper le fichier<br>c. Exporter le fichier format. STL en format.Gcode vers la carte SD. |
| **3** | **IMPRIMANTE 3D**<br>*Avertissement : toutes les manipulations seront faites à la présence de l'enseignant.* *(en rouge)*<br>d. Mettre l'imprimante 3D sous tension.<br>e. Insérer la carte SD<br>f. Lancer l'impression |

Mention finale : « Lien vers le répertoire contenant les fichiers .STL : » + QR-code **ZIP**.
*(La numérotation des sous-étapes court a, b, c puis d, e, f d'une ligne à l'autre : elle est
continue sur toute la fiche, pas remise à zéro à l'étape 3.)*

- **Vocabulaire & terminologie officielle (Projet 1)** : train épicycloïdal / train planétaire ;
  satellite ; planétaire ; couronne ; porte-satellite ; carter fixe ; formule de Willis ;
  réducteur / multiplicateur ; inverseur / non-inverseur ; rapport de transmission ; bête à
  cornes ; diagramme pieuvre ; fonction principale (FP) / fonction contrainte (FC) ; tri croisé ;
  cahier des charges fonctionnel ; critère d'appréciation ; niveau ; flexibilité ; actigramme
  A-0 ; FAST ; solution constructive ; schéma cinématique ; effort tangentiel / radial ; module
  m ; résistance pratique à l'extension R<sub>pe</sub> ; moment idéal ; cotation fonctionnelle ;
  jeu fonctionnel ; chaîne de cotes ; dessin de définition ; perspective éclatée ; nomenclature ;
  feuille d'avant-projet d'étude de fabrication ; contrat de phase ; phase / sous-phase ;
  référentiel de mise en position ; centrage long ; appui plan / linéaire / ponctuel ; serrage ;
  ablocage ; cote machine (Cm) / cote outil (Co) ; graphe de transfert ; dresser ; charioter ;
  chanfreiner ; centrer ; percer ; tarauder ; fileter ; rainurer ; ébauche / demi-finition /
  finition ; A.R.S ; CMD ; plaquette rugotest ; PC au 1/50 ; micro-tour ; micro-fraiseuse ;
  origine pièce (OP) ; code ISO / gcode ; Mach 3 ; fabrication additive ; tranchage ; .STL ;
  Gcode ; PLA ; PVC ; CuSn8P ; PA 6.

---

##### Projet 2 — Maquette mécanisme à came (p.281–284)

- **Système / support d'étude** : **banc didactique de mécanisme à came** — bâti vertical sur
  semelle, came montée sur un axe porte-tambour avec disque gradué, poussoir guidé en
  translation, mesure du déplacement par **comparateur à cadran**.
- **Compétences affichées** : bandeau **CD 3.9 / CD 2.6 / CD 2.8 / CD 2.7** ; en-tête courant
  « OBTENTION DES PIECES » / « PROJET ».
- **Pictogrammes de compétences transversales (p.281)** : **COMM**, **COOP**, **R. PRO**, **CREA**.
- **Ressources fournies** : modèle 3D photo-réaliste (p.281, + QR-code **ZIP**), dessin en vue
  éclatée (p.282), dessin d'ensemble à 4 vues (p.283), nomenclature 29 repères (p.284).

###### I. Situation problème (p.281)

> Les commandes à came font partie des transmissions irrégulières, qui sont utilisés [sic] pour
> transformer des mouvements d'entraînement circulaires réguliers, en mouvements entraînés
> irréguliers avec ou sans pause.
>
> La courbe de mouvement souhaitée est déterminée par la géométrie des corps de came, et produite
> par le balayage d'un contour ou d'un profil au niveau de ce que l'on appelle l'élément suiveur.
>
> **Comment étudier, concevoir et réaliser un banc didactique, permettant de démontrer de manière
> explicite la fonction d'une commande à came ?**

###### II. Travail demandé (p.281)

> Faite [sic] une étude complète et structurée pour répondre à ce besoin tout en respectant les
> étapes de la démarche de projet et en exploitant les équipements et le matériel disponible au
> laboratoire afin de développer les quatre compétences suivantes :
> - Décoder un document de fabrication.
> - Mettre en œuvre les machines conventionnelles et les micromachines à commande numérique
>   (MOCN) pour réaliser une pièce simple.
> - Mettre en œuvre les composantes d'une chaine numérique de fabrication additive.
> - Contrôler une pièce

###### Étape 1 — Modèle 3D de mécanisme à came (p.281)

Rendu 3D : socle noir sur quatre pieds, plaque support bleu clair verticale, comparateur à cadran
en haut relié à un poussoir vertical, disque gradué circulaire (graduation périphérique en
degrés) portant une came en forme de goutte, écrou moleté de blocage au centre.
QR-code **ZIP** en bas à gauche.

###### Étape 2 — Dessin en vue éclatée (p.282)

Éclaté complet du banc dans le plan de la page, **repères 1 à 29** tous fléchés (1, 2, 3, 4, 5,
6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29).
Aucune cote.

###### Étape 3 — Dessin d'ensemble (p.283)

Cartouche : **Echelle: 1:3**, titre **« Mécanisme à came »**, symbole de projection européenne.
Quatre vues : coupe **A-A** (repères fléchés 1, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11 à
gauche ; 2, 3, 4, 5, 6, 7, 8, 9, 10 à droite) ; vue de face (repères 1, 29, 8, 9) ;
coupe **B-B** (repères 29, 23, 24, 25) ; coupe **C-C** (repères 28, 4, 27, 26).
Traits de coupe A-A, B-B, C-C repérés sur les vues.

###### Étape 4 — Nomenclature (p.284)

| Rep. | Nbr. | Désignation | Matière | Observation |
| ---: | ---: | --- | --- | --- |
| 1 | 1 | Comparateur à cadran | | |
| 2 | 1 | Plaque support | PA 6 | |
| 3 | 1 | Glissière | | |
| 4 | 1 | Coulisseau de poussoir | | |
| 5 | 2 | Coussinet à collerette | CuSn8P | Arbre 14 mm |
| 6 | 1 | Axe porte tambour | | |
| 7 | 1 | Clavette disque 3x3.7 | | |
| 8 | 1 | Disque gradué | PLA | |
| 9 | 1 | Came | PLA | |
| 10 | 3 | Vis à tête cylindrique à six pans creux, M6-25 | | DIN 6912 |
| 11 | 4 | Pied | PLA | |
| 12 | 4 | Vis à tête cylindrique à six pans creux, M6-10 | | ISO 4762 |
| 13 | 1 | Semelle | PA 6 | |
| 14 | 2 | Vis à tête cylindrique à six pans creux, M3-6 | | ISO 4762 |
| 15 | 1 | Repère d'angle | | |
| 16 | 1 | Écrou moleté de blocage tambour | PLA | |
| 17 | 1 | Roulement à une rangée de billes à contact radial | | BC 8x22x7. |
| 18 | 1 | Axe de poussoir | | |
| 19 | 2 | Écrou moleté de blocage | | |
| 20 | 2 | Rondelle plate M8 | | ISO 7092 |
| 21 | 1 | Palier de poussoir | | |
| 22 | 1 | Corps de poussoir | | |
| 23 | 1 | Vis à tête cylindrique à six pans creux, M4-25 | | ISO 4762 |
| 24 | 1 | Support de comparateur | | |
| 25 | 1 | Vis à tête cylindrique à six pans creux, M4-25 | | ISO 4762 |
| 26 | 4 | Vis à tête cylindrique à six pans creux, M4-6 | | ISO 4762 |
| 27 | 2 | Vis à tête fraisée à empreinte cruciforme, M3-20 | | ISO 7046 |
| 28 | 6 | Vis à tête cylindrique à six pans creux, M4-16 | | ISO 4762 |
| 29 | 1 | Poussoir de comparateur | | |

- **Vocabulaire & terminologie officielle (Projet 2)** : commande à came ; transmission
  irrégulière ; mouvement d'entraînement circulaire régulier ; mouvement entraîné irrégulier ;
  corps de came ; contour / profil ; élément suiveur ; banc didactique ; comparateur à cadran ;
  poussoir ; coulisseau ; glissière ; disque gradué ; axe porte tambour ; écrou moleté de
  blocage ; repère d'angle ; roulement à une rangée de billes à contact radial ; coussinet à
  collerette ; clavette disque.

---

##### Synthèse — Synthèse obtention des pièces (p.285–286)

Bandeau **Synthèse** en tête de p.285, QR-code **EXE** (quiz d'auto-évaluation).

> **1. Auto-évaluation**
> Tester vos connaissances avant de passer à la synthèse avec les Quiz.

###### 1. Isostatisme (p.285)

> **1. Isostatisme**
> C'est l'élimination de six degrés de liberté de la pièce et du porte-pièce par un ensemble de
> composants de mise en position.
> Pour assurer une bonne précision à l'usinage, l'ensemble de ces composants doit permettre une
> mise en position identique après la pose d'une nouvelle pièce sur son porte-pièce.
>
> **a. Mise en position isostatique d'une pièce prismatique**
> **Mise en position (MIP)**
> - L'appui plan (1,2,3) élimine Rx, Rz et Ty.
> - L'appui linéaire (4,5) élimine Ry et Tx.
> - L'appui ponctuel (6) élimine Tz.
> **Maintien en position (MAP)**
> - Serrage contre (4,5).
>
> **b. Mise en position isostatique d'une pièce cylindrique courte**
> - Centrage long (1,2,3,4) élimine Ry, Rz, Ty et Tz.
> - Appui ponctuel (5) élimine Tx.
> - Serrage contre le centrage long.
> -
>
> **c. Mise en position isostatique d'une pièce cylindrique longue**
> - Centrage long (1,2,3,4) élimine Ry, Rz, Ty et Tz.
> - Appui ponctuel (5) élimine Tx.
> - Serrage contre le centrage long.
>
> **d. Surface de base**
> Une étude de ces spécifications dimensionnelles et géométriques est nécessaire afin de
> déterminer les surfaces d'appui appelées surfaces de base (SB).

*(⚠️ Les paragraphes b. et c. portent le même triplet de règles ; le b. comporte en outre un
tiret vide en fin de liste — voir § Incertitudes.)*

Schéma imprimé sous d. :
> SB → Elle peut être → **Sur surface usinée appelée surface de référence (SR)**
> SB → Elle peut être → **Sur surface brute appelée surface de départ (SD)**

Figures associées (p.285) : symbolisation technologique de la mise en position sur trois vues
pour chacun des trois cas (prismatique, cylindrique courte, cylindrique longue), avec les
numéros de normales de repérage 1 à 6 et les axes x, y, z.

###### 2. Les cotes de fabrication (p.285–286)

> **2. Les cotes de fabrication**
> Les cotes de fabrication (Cf) sont classées en trois catégories :
> - Les cotes machines (Cm) ;
> - Les cotes outils (Co) ;
> - Les cotes appareillage (Ca).
>
> **a. Les cotes machines**
> Cotes réalisées en contrôlant le déplacement produit par la machine entre l'outil et la pièce.
>
> **b. Les cotes outils**
> Cotes sur la pièce qui reproduisent les dimensions des outils ou sur des réglages des outils
>
> **c. Les cotes appareillage**
> Cotes sur les pièces résultant des dimensions d'appareillages, de montages, etc.
>
> **d. Transfert de cotes dimensionnelles**
> Si la cote de fabrication ne coïncide pas à une cote du dessin de définition.
> C'est une cote transférée.

Figures associées (p.286) : pour **a.** deux croquis d'usinage en tournage et en fraisage, avec
« Référentiel des côtes [sic] diamétrales », « Référentiel des cotes de longueurs », « Plans de
travail de l'outil », cotes Cm1 et Cm2 ; pour **b.** deux croquis (fraise à 3 tailles, train de
fraises) avec Cm1, Cm2, Co1, Co2, Co ; pour **c.** un croquis « Montage de d'usinage » [sic — « de » surnuméraire] + « Canon de
perçage » avec Ca1 et Ca2 ; pour **d.** un croquis de transfert avec **B=24<sup>±0,3</sup>**,
**A=18<sup>±0,2</sup>**, **Cf1** et **Cf2**.

###### 3. La métrologie (p.286)

> **3. La métrologie**
> La métrologie rassemble l'ensemble des techniques permettant de réaliser des mesures, de les
> interpréter et d'assurer leur fiabilité.
>
> **a. Contrôle par comparaison**
> La mesure par comparaison mécanique consiste à comparer les pièces à contrôler à une cale étalon
> de référence, généralement de même longueur nominale au moyen d'un comparateur.
>
> **b. Contrôles géométriques des pièces**

Figure de a. : photo légendée **Comparateur**, **Pièce à contrôler**, **Cale étalon**, **Marbre**.
Tableau de b. : trois colonnes illustrées — **Parallélisme** (tolérance ⫽ 0,1 | A, référence A),
**Perpendicularité** (tolérance ⊥ 0,1 | B, référence B, écart Δx = 0,06 relevé),
**Coaxialité** (tolérance Ø 0,1 | C, référence C).

---

##### Synthèse — Synthèse plasturgie (p.287–288)

Bandeau **Synthèse** en tête de p.287.

###### 1. La plasturgie (p.287)

> **1. La plasturgie**
> La plasturgie désigne la transformation du plastique en de nombreux objets de notre quotidien
> grâce à différentes techniques de transformation des polymères (extrusion, injection, impression
> 3D, thermoformage, etc.).

###### 2. Classification des plastiques (p.287)

> **2. Classification des plastiques**
> Les matières plastiques se transforment sous la chaleur et la pression.
>
> **a. Les thermoplastiques**
> Les thermoplastiques sont les matières plastiques les plus utilisées. Ils se ramollissent sous
> l'effet de la chaleur, ce qui permet de les modeler à une forme souhaitée. Une fois refroidi, le
> plastique durcit et garde sa forme. Cette opération peut être réalisée de manière répétée.
> Les thermoplastiques sont ainsi recyclables.
>
> **b. Les thermodurcissables**
> Les thermodurcissables sont des matériaux plastiques qui prennent une forme définitive après
> polymérisation.
> Cette propriété ne permet donc pas aux thermodurcissables d'être recyclés. Les
> thermodurcissables sont des matériaux solides et très résistants.
>
> **c. Les élastomères**
> Les élastomères sont des polymères qui présentent des propriétés élastiques. Ils peuvent
> supporter de grandes déformations avant rupture.
> On distingue 3 catégories : les caoutchoucs, les élastomères spéciaux et les élastomères très
> spéciaux.
>
> **d. Les composites**
> Un matériau composite est un matériau qui est constitué d'au moins deux matériaux de nature
> différente.
> Lorsque l'on combine deux matériaux ou plus, on obtient un matériau plus performant car ce
> dernier possède les propriétés de l'ensemble des matériaux utilisés.
> Aujourd'hui, les principales matières plastiques combinées sont les plastiques thermodurcissables
> (TD) et les plastiques thermoplastiques (TP).

Illustrations (p.287) : brosses à dents (thermoplastiques), boutons/molettes noirs
(thermodurcissables), sabots roses type crocs (élastomères), casque de football américain
(composites).

###### 3. Les procédés de mise en œuvre des matières plastiques (p.287–288)

> **3. Les procédés de mise en œuvre des matières plastiques**
>
> **a. L'impression 3D**
> L'impression 3D, aussi connu sous le nom de « fabrication additive » est un procédé permettant de
> créer des objets en 3 dimensions à l'aide d'une imprimante 3D.
>
> **b. L'injection**
> Dans le moulage par injection, la matière est fluidifiée dans un organe approprié puis injectée
> sous forte pression dans l'empreinte (ou les empreintes) du moule.
>
> **c. L'Injection-soufflage** *(p.288)*
> Cette technique est essentiellement réservée aux thermoplastiques.
> Ce procédé permet d'obtenir de type flacon (pharmacie, cosmétique) où les volumes doivent être
> très précis ainsi que des bouteilles légères pour boisson.
>
> **d. Extrusion-soufflage**
> Ce procédé consiste à combiner la technique de l'extrusion avec celle du soufflage.
>
> **e. Le thermoformage**
> Le thermoformage est une technique qui consiste à prendre un matériau sous forme de plaque
> (verre, plastique…), à le chauffer pour le ramollir, ainsi qu'à profiter de cette ductilité pour
> le mettre en forme avec un moule. Le matériau redurcit quand il refroidit, gardant cette forme.
>
> **f. Le rotomoulage**
> Le moulage par rotation est conçu pour réaliser des corps creux de toutes dimensions. La matière
> (thermoplastique) est introduite dans un moule sous forme de poudre très fine ou de liquide, le
> moule est fermé puis chauffé.
> Pendant que la matière devient fluide, l'ensemble est mis en double rotation (ou rotation plus
> une oscillation) pour que la matière tapisse toutes les parois. Lorsque la matière est fondue et
> correctement répartie dans l'empreinte, le moule est introduit dans un système de
> refroidissement.
> En rotomoulage, il n'y a aucune perte de matériau, toute la matière peut être 100% recyclée.

Figures associées (p.288) :
- **b. L'injection** : photo de bouchons/roulettes plastiques colorés.
- **c. L'Injection-soufflage** : photo de bouteilles PET à bouchon bleu.
- **d. Extrusion-soufflage** : bandeau de 5 vignettes montrant les phases successives
  (paraison extrudée entre deux demi-moules, gonflage, formage, refroidissement, éjection).
- **e. Le thermoformage** : schéma de ligne en 7 étapes numérotées et légendées —
  **1 Bobine**, **2 Préchauffage**, **3 Chauffage**, **4 Formage**, **5 Découpe**,
  **6 Empilage**, **7 Ramassage Conditionnement**.
- **f. Le rotomoulage** : schéma « UN PROCESS EN QUATRE ETAPES », légendes **Poudre**, **Moule**,
  **Pièce**, et quatre colonnes titrées **Chargement du moule**, **Chauffage**,
  **Refroidissement**, **Démoulage de la pièce**.

Dernière ligne imprimée du manuel (p.288), avec QR-code **PDF** :

> Grille d'évaluation des savoirs et savoir-faire de l'apprenant

- **Vocabulaire & terminologie officielle (Synthèses p.285–288)** : isostatisme ; degré de
  liberté ; porte-pièce ; mise en position (MIP) / maintien en position (MAP) ; appui plan /
  linéaire / ponctuel ; centrage long ; serrage ; surface de base (SB) ; surface de référence
  (SR) ; surface de départ (SD) ; cote de fabrication (Cf) ; cote machine (Cm) ; cote outil (Co) ;
  cote appareillage (Ca) ; transfert de cotes ; cote transférée ; montage d'usinage ; canon de
  perçage ; métrologie ; contrôle par comparaison ; cale étalon ; comparateur ; marbre ;
  parallélisme ; perpendicularité ; coaxialité ; plasturgie ; polymère ; thermoplastique ;
  thermodurcissable ; polymérisation ; élastomère ; caoutchouc ; composite ; TD / TP ;
  impression 3D / fabrication additive ; injection ; moule ; empreinte ; injection-soufflage ;
  extrusion ; extrusion-soufflage ; paraison ; thermoformage ; ductilité ; rotomoulage ;
  moulage par rotation ; corps creux ; double rotation ; recyclable.

##### Bornes de scope observées — p.252–288

- ✅ **INCLUS — plasturgie** : classification des plastiques (thermoplastiques,
  thermodurcissables, élastomères, composites) ; principes de l'impression 3D, de l'injection, de
  l'injection-soufflage, de l'extrusion-soufflage, du thermoformage et du rotomoulage, chacun
  défini en un paragraphe court + une figure de principe (p.287–288) ; application au pédalo
  (tri métallique/non métallique, association pièce ↔ famille de plastique, recyclabilité du
  polyester, procédé d'obtention par objet) (p.255–256).
- ✅ **INCLUS — obtention par enlèvement de matière** : isostatisme (prismatique, cylindrique
  courte, cylindrique longue), MIP/MAP, surfaces de base SB/SR/SD ; les trois catégories de cotes
  de fabrication (Cm, Co, Ca) et la notion de transfert de cote (p.285–286) ; lecture ET rédaction
  d'une feuille d'avant-projet d'étude de fabrication et d'un contrat de phase, sur une pièce
  réelle en PVC (p.273–275) ; opérations de tournage (dresser, charioter, gorge, chanfreiner,
  centrer, percer), taraudage et filetage manuels, rainurage en fraisage.
- ✅ **INCLUS — MOCN** : programmation ISO élémentaire sur micro-tour et micro-fraiseuse, limitée
  aux codes **G00/G0, G01/G1, G95, M03, M02, M6, T, D, S, F** et au repérage des points de
  trajectoire par rapport à l'origine pièce (OP) ; mise en œuvre via le logiciel **Mach 3**
  (profils PX1 et PC1) (p.276, p.278–279).
- ✅ **INCLUS — méthode additive** : chaîne numérique complète en 3 étapes (conception → tranchage
  → impression), logiciels cités **Repetier-Host, Slicer, Cura**, formats **.STL** et **.Gcode**,
  transfert par carte SD, matière **filament PLA** (p.280).
- ✅ **INCLUS — métrologie** : contrôle par comparaison (comparateur + cale étalon + marbre) et
  contrôles géométriques de parallélisme, perpendicularité et coaxialité (p.286).
- ✅ **INCLUS — démarche de projet complète** : le Projet 1 déroule 20 étapes, de l'expression du
  besoin jusqu'aux documents de fabrication et à l'impression 3D d'une pièce.
- ⛔ **EXCLU / seulement mentionné** :
  - **L'« extrusion gonflage »** est annoncée dans le tableau des savoirs p.252 mais **n'est pas
    traitée** : la synthèse plasturgie p.287–288 ne développe que impression 3D, injection,
    injection-soufflage, **extrusion-soufflage**, thermoformage et rotomoulage.
  - **L'extrusion seule** n'est citée que dans la définition de la plasturgie (p.287) et dans
    l'intitulé « extrusion-soufflage » — aucun principe propre n'en est donné.
  - **Le Projet 2 (mécanisme à came) s'arrête à la nomenclature (p.284)** : il annonce en p.281
    une « étude complète et structurée » et les quatre compétences, mais ne fournit ni analyse
    fonctionnelle, ni étude cinématique, ni dessin de définition, ni document de fabrication, ni
    aucun travail chiffré. Seuls 4 documents sont livrés : modèle 3D, vue éclatée, dessin
    d'ensemble, nomenclature.
  - **Aucune loi de came, aucune courbe de levée** n'est étudiée : le profil de came reste
    qualitatif (« la géométrie des corps de came », « l'élément suiveur »).
  - **Les corrigés ne sont pas imprimés** : tous les travaux demandés de l'activité plasturgie
    (p.255–256), les tableaux de points/programmes (p.276, p.278–279), le référentiel de la phase
    40 et la recherche de Cm12 (p.274) sont laissés en pointillés.
  - **La grille d'évaluation** finale (p.288) n'est pas imprimée : elle est renvoyée à un QR-code
    PDF externe. De même, les vidéos (**Vid**), les dessins (**PDF**) et les fichiers .STL
    (**ZIP**) sont hors manuel.
  - **Contrainte d'antériorité** et **moyen d'ablocage** sont annoncés p.252 comme « (Rappel) » :
    ils ne font l'objet d'aucun développement dans cette tranche (l'ablocage n'apparaît que sous
    la forme « Serrage » dans les référentiels de phase et la synthèse isostatisme).
  - **Aucune fin d'ouvrage** : le manuel s'achève p.288 sur la synthèse plasturgie. Il n'y a **ni
    bibliographie, ni annexes, ni table des matières finale, ni glossaire, ni quatrième de
    couverture** dans les pages 286 à 288 — voir § Incertitudes.

## 3. Notes pédagogiques / méthode

### 3.1 La démarche que le manuel impose (p.6, p.8–9)

Le manuel ne propose pas un cours suivi d'exercices : **il est entièrement bâti en activités**, et
c'est la contrainte la plus structurante pour tout contenu tiré de cette fiche.

> Le manuel d'activités traite les thèmes du curriculum officiel en proposant des situations
> déclenchantes et significatives à partir d'un système réel et/ou de son dossier technique, d'un
> sous-système, d'une expérimentation, d'une simulation matérielle, d'une séquence
> audiovisuelle... On amène ainsi l'apprenant à suivre une démarche active adoptée par le
> curriculum afin de structurer ses connaissances et développer ses compétences de vie. (p.6)

> Ce manuel s'appuie sur l'étude des systèmes, sous-systèmes ou objets et sur l'analyse de leurs
> solutions technologiques par des activités. (p.9)

Le cycle d'apprentissage affiché p.9 articule quatre gestes — **Observation, Questionnement,
Expérimentation, Argumentation** — autour d'un « Système ou sous-système » placé au centre. Il se
lit en deux colonnes complémentaires :

| Manuel numérique (colonne « Lien ») | Manuel d'activités (colonne « Labo ») |
| ----------------------------------- | -------------------------------------- |
| Éléments de cours                   | Activités pratiques                    |
| Simulations                         | Manipulation                           |
| Corrections                         | Problème technologique                 |
| Directives et recommandations       | Étude de cas et synthèse               |

⚠️ **Conséquence directe pour la génération** : les **éléments de cours et les corrigés des
activités ne sont PAS dans le manuel papier** — ils vivent dans le manuel numérique, hébergé
ailleurs et accessible par liens « Url » et codes « QR » (p.7, p.8). Le manuel imprimé ne donne
donc, pour la quasi-totalité des activités, **que les énoncés, les documents et les zones de
réponse laissées vides** ; les seuls textes de cours qu'il porte sont les **Synthèses** de fin de
thème et les encadrés insérés dans les activités. Les réponses aux questions transcrites au §2
sont, sauf mention explicite, **absentes de la source** : elles se calculent, elles ne se
recopient pas — et une génération qui prétendrait les citer inventerait.

### 3.2 Ce que le manuel dit de lui-même (p.6–7)

> Le manuel scolaire est conçu de façon à respecter la progression des apprentissages et les
> thèmes du curriculum de technologie en quatrième année sciences techniques de génie mécanique.
> (p.6)

> Le manuel numérique complémente et enrichit son homologue imprimé. […] On y trouve les éléments
> de cours, les corrigés des activités, des animations adaptées, des capsules pédagogiques, des
> modélisations 2D et 3D, des maquettes numériques, des simulations, des programmes textuels et
> graphiques et tous autres fichiers jugés importants d'être utilisés par l'apprenant ou
> l'enseignant. (p.7)

> Ce manuel favorise l'activité pratique, la manipulation et l'étude de cas autour de problèmes
> technologiques. Il propose aussi des ressources hébergées dans un espace numérique, accessible
> en ligne et en téléchargement par des liens « Url » et des codes « QR ». (p.8)

### 3.3 Conventions de notation observées dans tout le manuel

- **Symbole de diamètre** : le manuel n'en imprime qu'un ; cette fiche le rend partout par **`Ø` (U+00D8)**. Les variantes `⌀` (U+2300) et surtout `∅` (U+2205 — le signe mathématique « ensemble vide ») ont été normalisées : elles venaient des lecteurs, pas de la source, et `∅` casse toute recherche en aval.
- **Espaces doubles de la source** : conservés là où le §6.2 les signale, normalisés ailleurs. La règle n'a pas été appliquée uniformément par les dix lecteurs — s'y fier pour un comptage de caractères serait imprudent.

- **Repères de nomenclature entre parenthèses** : une pièce est toujours désignée par son nom
  suivi de son repère — « Sabot (4) », « Levier de commande (12) », « Tige filetée (16) ».
- **Indices de couple cinématique** : une vitesse, une trajectoire ou une rotation relative porte
  en indice le couple des deux pièces concernées — `V(D17/18)` (vitesse du point D de la pièce 17
  par rapport à la pièce 18), `TD(17/18)`, `ω(12/18)`, `α(DED')`.
- **Échelles de tracé** données sous la forme `1 mm → 0,01 m/s`.
- **Chiffres occidentaux 0-9**, **virgule décimale** française, unités SI telles qu'imprimées
  (mm, N, N·m, tr/min, m/s, MPa).
- **Bandeau de compétences** en haut à gauche de chaque page d'activité (`CD 1.3`, `CD 2.3`…) et
  bandeau de thème centré, en couleur propre à chaque thème.

## 4. Chapitrage retenu (→ alimente `manifest/bac-techniques.json`)

L'unité de chapitre est l'**activité** du manuel, non le thème. Les six thèmes font 29 à 87
pages : un chapitre par thème donnerait une section de fiche que la génération devrait charger
en entier pour écrire un seul chapitre, ce que la charte tokens interdit (T-5 — l'unité de
travail est le chapitre, nourri par SA section). L'activité, elle, est l'unité réelle du
manuel : elle a son système support, son dossier technique et son travail demandé. La synthèse
de fin de thème est rattachée au dernier chapitre de son thème.

| #   | slug | notion | manuel élève (code · pages) |
| --- | ---- | ------ | --------------------------- |
| 1 | `01-analyse-fonctionnelle-micro-fraiseuse` | Analyse fonctionnelle interne d'un produit — Activité 1 : micro-fraiseuse. Actigramme A-0, diagramme F.A.S.T., fonctions techniques et solutions constructives | `228462` · p.12–18 |
| 2 | `02-analyse-fonctionnelle-imprimante-3d` | Analyse fonctionnelle interne d'un produit — Activité 2 : imprimante 3D. Chaînes fonctionnelles, F.A.S.T. et dossier technique | `228462` · p.19–30 |
| 3 | `03-analyse-fonctionnelle-micro-tour` | Analyse fonctionnelle interne d'un produit — Activité 3 : micro tour, puis synthèse du thème | `228462` · p.31–40 |
| 4 | `04-communication-technique-perceuse-sensitive` | Communication technique — Activité 1 : perceuse sensitive. Lecture d'un dessin d'ensemble, graphe de montage et de démontage, cotation fonctionnelle, dessin de définition | `228462` · p.41–50 |
| 5 | `05-communication-technique-poupee-mobile` | Communication technique — Activité 2 : poupée mobile. Lecture d'un dessin d'ensemble, graphe de montage et de démontage, cotation fonctionnelle, dessin de définition | `228462` · p.51–59 |
| 6 | `06-communication-technique-pince-de-soudage` | Communication technique — Activité 3 : pince de soudage par point. Lecture d'un dessin d'ensemble et cotation fonctionnelle | `228462` · p.60–74 |
| 7 | `07-communication-technique-machine-essai-traction` | Communication technique — Activité 4 : machine d'essai de traction, puis synthèse du thème | `228462` · p.75–86 |
| 8 | `08-assemblages-tete-universelle-fraiseuse` | Typologie des assemblages — Activité 1 : tête universelle de la fraiseuse. Liaisons mécaniques, assemblages, guidage en rotation | `228462` · p.87–103 |
| 9 | `09-assemblages-extrudeuse-pate-a-savon` | Typologie des assemblages — Activité 2 : extrudeuse de pâte à savon. Liaisons mécaniques, assemblages, guidage en rotation | `228462` · p.104–112 |
| 10 | `10-assemblages-chariot-elevateur` | Typologie des assemblages — Activité 3 : chariot élévateur à 3 roues, puis synthèse du thème | `228462` · p.113–128 |
| 11 | `11-transmission-embrayage-a-disque` | Transmission de puissance — Activité 1 : maquette d'embrayage à disque. Étude d'embrayage | `228462` · p.129–135 |
| 12 | `12-transmission-tour-parallele` | Transmission de puissance — Activité 2 : tour parallèle. Transmission de mouvement, embrayage, freinage, boîte de vitesses, transformation de mouvement | `228462` · p.136–154 |
| 13 | `13-transmission-boite-de-vitesses-engrenages-frein` | Transmission de puissance — Activité 3 : maquette de boîte de vitesses. Engrenages et frein | `228462` · p.155–162 |
| 14 | `14-transmission-fraiseuse-universelle` | Transmission de puissance — Activité 4 : fraiseuse universelle. Étude de frein, boîte de vitesses, transformation de mouvement vis-écrou | `228462` · p.163–180 |
| 15 | `15-transmission-moteur-a-explosion` | Transmission de puissance — Activité 5 : maquette moteur à explosion. Machine thermique, embrayage, boîte de vitesses, synchroniseur | `228462` · p.181–200 |
| 16 | `16-transmission-palan-electrique` | Transmission de puissance — Activité 6 : palan électrique à chaîne. Frein et limiteur de couple, train épicycloïdal, puis synthèse du thème | `228462` · p.201–215 |
| 17 | `17-torsion-banc-d-essai` | Comportement du solide déformable — ouverture du thème (p.216 : séquence, composantes CD 1.7 / CD 2.1, carte du manuel) puis Activité 1 : banc d'essai de torsion | `228462` · p.216–221 |
| 18 | `18-flexion-banc-d-essai` | Comportement du solide déformable — Activité 2 : banc d'essai de flexion | `228462` · p.222–226 |
| 19 | `19-sollicitations-composees-micro-tour` | Comportement du solide déformable — Activité 3 : micro tour, sollicitations composées | `228462` · p.227–232 |
| 20 | `20-sollicitations-composees-touret-a-meuler` | Comportement du solide déformable — Activité 4 : touret à meuler, sollicitations composées | `228462` · p.233–238 |
| 21 | `21-machine-de-torsion-de-limes-dentaires` | Comportement du solide déformable — Activité 5 : machine de torsion de limes dentaires | `228462` · p.239–244 |
| 22 | `22-grue-d-atelier` | Comportement du solide déformable — Activité 6 : grue d'atelier, puis synthèse du thème | `228462` · p.245–251 |
| 23 | `23-plasturgie-bateau-a-pedales` | Obtention des pièces — ouverture de l'AXE 3 et du thème (p.252 : séquence, composantes CD 3.9 / CD 2.6 / CD 2.8 / CD 2.7, carte du manuel) puis Activité : bateau à pédales, plasturgie | `228462` · p.252–256 |
| 24 | `24-projet-maquette-train-epicycloidal` | Obtention des pièces — Projet 1 : maquette de train épicycloïdal (dossier de réalisation guidée) | `228462` · p.257–280 |
| 25 | `25-projet-maquette-mecanisme-a-came` | Obtention des pièces — Projet 2 : maquette de mécanisme à came (dossier volontairement bref : modèle 3D, vue éclatée, dessin d'ensemble et nomenclature), puis les DEUX synthèses de fin de manuel — obtention des pièces (p.285-286) et plasturgie (p.287-288) | `228462` · p.281–288 |

> Les plages ci-dessus alimentent `chapter.manuel = { code, pages }` du manifeste. Le code
> `228462` désigne l'œuvre entière (2 tomes) : la pagination du manuel étant continue,
> une page imprimée y est non ambiguë sans préciser le tome.

## 5. Sources croisées

- **Guide enseignant** : **aucun**. Le catalogue CNP (`suivi/corpus-cnp.json`, 346 documents) ne
  porte, pour la matière 28 en 4ème année secondaire, que des manuels d'activités de rôle
  `eleve` : `228461` (génie électrique, 3 tomes) et `228462` (génie mécanique, 2 tomes). Aucun
  document de rôle `enseignant`. La règle de combinaison du README s'applique donc dans sa
  branche « une seule source disponible ⇒ elle fait référence ».
- **Manuel élève** : `228462` — « TECHNOLOGIE — Génie mécanique — Manuel d'activités — 4ème année
  Sciences Techniques » (CNP), 2 tomes, 288 pages, **source de scope ET de contenu** de cette
  fiche. Le chapitrage du §4 et ses plages de pages en sont tirés.
- **Manuel élève NON revendiqué** : `228461` — « Génie électrique - Manuel d'activités », 3 tomes.
  Seconde spécialité de la même matière, hors périmètre de cette fiche (voir l'avertissement en
  tête). À transcrire dans une fiche distincte, par une autre session.
- **Taybah** : aucun fichier école pour ce niveau/cette matière.
- **Divergences signalées** : sans objet — il n'y a qu'une source, donc aucune divergence
  guide ↔ manuel possible. Les incohérences **internes** au manuel, elles, sont consignées au §6.

## 6. Incertitudes / à revérifier

### 6.1 Ce que la source ne donne pas (et qu'il ne faut donc pas générer)

- **Les composantes numérotées des compétences disciplinaires.** Les bandeaux affichent `CD 1.3`,
  `CD 1.9`, `CD 2.3`… mais le manuel n'imprime **nulle part** le libellé de ces composantes. Ils
  sont transcrits tels quels ; les développer serait une invention. Un guide enseignant les
  porterait — il n'existe pas au corpus.
- **Les corrigés.** Ils sont dans le manuel numérique, pas dans le manuel imprimé (§3.1). Aucune
  réponse d'activité ne figure donc dans cette fiche, sauf là où le manuel imprime lui-même un
  résultat dans son énoncé ou dans une synthèse.
- **La progression trimestrielle.** Le manuel donne un ordre de thèmes, pas un calendrier. Aucun
  découpage par trimestre n'est transcrit, parce qu'aucun n'est imprimé.
- **Le curriculum officiel lui-même.** Le manuel s'y réfère (« le nouveau programme d'étude de
  technologie actuel », p.6) sans le reproduire. Le scope de cette fiche est donc celui du
  manuel, qui en est l'application, et non celui du texte curriculaire.

### 6.3 Contrôle indépendant (R-7) — ce qu'il a trouvé, et ce qui reste dû

Deux contrôleurs à contexte vierge, n'ayant écrit aucune ligne de ce qu'ils relisaient, ont
confronté cette fiche **aux pages du manuel** — page ouverte d'abord, fiche lue ensuite —, chacun
sur une moitié. **105 pages ouvertes sur 288 (36 %)**, dont les six synthèses de fin de thème
vérifiées mot à mot, toutes les formules, et les bornes de chaque chapitre.

| Moitié | Verdict | Substantielles | De forme |
| ------ | ------- | -------------- | -------- |
| p.145–288 | **au-dessus de la barre** | 0 | 6 |
| p.1–144 | **sous la barre** | 3 | 9 |

**Les 18 défauts ont été corrigés.** Les trois substantielles étaient : une **invention** (des
cases à compléter décrites sous deux blocs de la p.16 qui n'en portent pas), un **contresens sur
la source** (« aucune sous-activité 3.x n'est encore imprimée », alors que 3.1 et 3.2 le sont et
sont transcrites ici même), et une **formule annoncée « encadrée »** p.135 qui est en ligne de
texte courant, assortie d'une légende de symboles que le manuel n'imprime pas.

**Ce que le contrôle a confirmé** : aucune formule fausse, aucune plage de chapitre fausse,
aucune activité omise, et — c'est la vérification la plus discriminante — **aucun des 40 constats
du §6.2 testés n'est fabriqué**. Les trois défauts d'impression que cette fiche impute au manuel
(le couple d'embrayage p.212, la cylindrée p.215, les signes manquants p.251) ont été vérifiés à
l'agrandissement : ils sont réels.

⚠️ **Ce qui reste dû.** Le protocole commande la re-lecture intégrale dès trois erreurs
substantielles : elle est **due sur p.1–144** et n'a pas été faite. C'est pourquoi le registre
porte `complete` et non `validee-r7` — la profondeur est acquise sur la totalité de la source, la
validation indépendante ne l'est pas.

### 6.2 Zones incertaines relevées à la transcription

**p.12–40**

- p.12 : le bandeau « THÈME » imprime **TYPOLOGIE DES ASSEMBLAGES**, alors que le bandeau
  « SÉQUENCE » de la même page, l'en-tête courant des p.13–40 et le sommaire p.4 donnent
  « Analyse fonctionnelle interne d'un produit ». Erreur de gabarit de la source (le thème affiché
  est celui de l'AXE 2, p.87-128) — transcrit tel quel, noté `[sic]`.
- p.14 : « Noix du chariot **longitidunal** » (rep. 12) — coquille pour « longitudinal », noté `[sic]`.
- p.14 : rep. 14 « Vis sans tête à six pans creux à téton long **ISO 4728**-M4×16 » — la norme
  usuelle pour une vis sans tête à téton long est ISO 4028 ; transcrit tel qu'imprimé, sans
  correction.
- p.17 vs p.18 : **FT4 porte deux libellés différents** — « Assurer les déplacements relatifs de
  l'outil et de la pièce. » (p.17) puis « Animer la pièce d'un mouvement de translation suivant
  (oy). » (p.18), alors que la p.18 annonce compléter « le diagramme F.A.S.T relatif à la fonction
  technique FT4 ». Contradiction interne de la source, transcrite telle quelle.
- p.16 / p.26 / p.35 : le même encadré « Situation déclenchante » est décliné avec **trois
  formulations différentes** de la même phrase — « satisfaire **aux fonctions** de service » (p.16),
  « satisfaire **une fonction** de service » (p.26), « satisfaire **chaque fonction** de service »
  (p.35). Les trois sont transcrites verbatim, aucune n'est harmonisée.
- p.20 : « **Catre** Micro-SD » — coquille pour « Carte », noté `[sic]`.
- p.24 : rep. 24, la référence moteur est imprimée coupée par un retour à la ligne
  (« SL42S- / TH34-1504A ») ; restituée « SL42STH34-1504A », identique aux rep. 12 et 17.
- p.25 : rep. 37 « Insert  M3x4 » comporte une **double espace** après « Insert » dans la source ;
  de même p.34 rep. 46 « Écrou à encoches  KM-M10 ». Conservées telles quelles.
- p.27 : « **Ficher** G-CODE : » — coquille pour « Fichier », transcrite telle quelle.
- p.39 : la définition de **Transmettre** s'achève sur « … engrenages, courroies, » — énumération
  **inachevée** dans le manuel (virgule finale, pas de point) ; rien n'est repris en p.40.
- p.15, p.21, p.22, p.23, p.33 : les planches de dessin d'ensemble ne portent **aucune cote
  chiffrée** ; seules les échelles sont indiquées. Les listes de repères données ci-dessus sont
  celles lisibles sur les lignes de rappel ; les planches p.21 et p.22 sont denses et un repère
  isolé pourrait avoir échappé au relevé, mais aucun n'a été lu de façon douteuse — aucun `[?]`
  n'a été posé.
- p.18 : la structure de l'arbre F.A.S.T rattache **FT421 à FT427 à la branche FT42** (lecture des
  traits de liaison). Le rendu graphique du manuel place ces sept blocs sur une seule verticale
  partant sous FT41 ; la lecture retenue est celle des connecteurs, pas celle de l'alignement.
- p.26 : sur la capture du pavé de déplacement, **deux des quatre boutons de pas sont masqués par
  la main** du doigt qui touche l'écran — seuls « 0.01mm » et « 10mm » sont lisibles ; les deux
  valeurs intermédiaires sont notées `[?]`, elles ne sont **pas** déduites. Les températures
  « 23/200 » et « 200/200 » (3e ligne de la page) sont, elles, nettes. Les libellés de menu
  partiellement recouverts dans la première capture (« Manual », « Preheat », « Z offset »,
  « Back ») ont été relevés sur la seconde capture de la même page, où ils sont dégagés.

**p.41–64**

- p.42 à p.64 : le bandeau de toutes les pages porte « DÉFINITION DES **ELEMENTS** D'UN PRODUIT »,
  sans accent sur « ELEMENTS » alors que « DÉFINITION » est accentué — transcrit tel quel, noté `[sic]`.
- p.42 : légende de la photo « **Etau** », sans accent (la mise en situation écrit « étau ») — `[sic]`.
- p.43 : annotation de la perspective « **Foureau (4) (crémaillère)** » — la nomenclature p.44 et
  tout le reste du manuel écrivent « Fourreau » — `[sic]`.
- p.43 : le repère **23'** apparaît sur le dessin d'ensemble (et p.47, p.48) alors que la
  nomenclature p.44 ne liste qu'un repère **23** (« Écrou hexagonal », Nbr. 2). Le manuel désigne
  ainsi le second des deux écrous (contre-écrou) sans lui donner de ligne propre — signalé, non corrigé.
- p.48 et p.56 : les deux encadrés « Situation problème » écrivent « la détermination des **côtes**
  d'une pièce » au lieu de « cotes » ; p.56 écrit en outre « leurs chaînes de **côtes** » —
  transcrits tels quels, notés `[sic]`. Le corps des questions, lui, écrit bien « cotes ».
- p.48 : la même phrase encadrée est écrite « chai**n**es de cotes » (sans accent circonflexe) p.48
  et « cha**î**nes de côtes » p.56 — deux graphies pour la même formule, transcrites telles quelles.
- p.48 q.4 et p.57 q.5 : le manuel écrit « la chai**n**e de cotes » / « les chai**n**es de cotes »
  sans accent, alors que les questions 2 et 7 des mêmes pages écrivent « chaîne(s) » — transcrit tel quel.
- p.49 : le repère **8'** désigne le second roulement de la paire repérée **8** (Nbr. 2) à la
  nomenclature ; il n'a pas de ligne propre au tableau — signalé, non corrigé.
- p.49 : l'étiquette de la condition inférieure du schéma est partiellement recouverte par le
  filigrane ; elle se lit **JC** (cohérente avec la question 6 « La condition J<sub>C</sub> ») —
  aucun indice qu'un indice supplémentaire soit imprimé.
- p.53 : l'étape 9 de la préparation laisse le diamètre du foret en pointillés
  (« un foret de diamètre … mm ») — c'est le manuel qui ne le fixe pas, ce n'est pas une illisibilité.
- p.54 : la vis de manœuvre (10) est écrite « 35NiCr6 » à la nomenclature p.51 et « 35 Ni Cr 6 »
  dans la question — même désignation, deux graphies ; les deux sont transcrites telles quelles.
- p.55 : tableau des observations du filogramme, « **Liberer** le **forreau** (7) » — deux coquilles
  dans la même cellule (« Libérer », « fourreau ») — `[sic]`.
- p.57 q.7 : « Reporter les cotes fonctionnelles relatives **aux corps (4)** » — accord fautif pour
  « au corps (4) », pièce unique à la nomenclature — `[sic]`.
- p.60 : les légendes de la photo écrivent « **Eléctrode E1** » / « **Eléctrode E2** » alors que le
  dessin d'ensemble p.61 écrit « Electrode E1 » / « Electrode E2 » — `[sic]` sur les deux
  occurrences de la p.60.
- **p.63 : contradiction interne du manuel.** Le titre imprimé en tête de page est
  « **4. Description de fonctionnement de la pince de soudage par point** » — exactement le titre
  déjà utilisé pour la rubrique 2 de la p.60 — alors que la page ne contient qu'un tableau de
  **nomenclature** (repères 1 à 36, poursuivi p.64 pour 37 à 72). Il s'agit très probablement d'un
  titre erroné : la rubrique attendue est « 4. Nomenclature ». Transcrit tel qu'imprimé, écart signalé.
- p.61 et p.62 : les dessins d'ensemble sont imprimés en rotation de 90° et très denses ; les listes
  de repères données ci-dessus ont été relevées après redressement et agrandissement de l'image.
  Elles sont fiables pour les repères cités, mais **ne prétendent pas à l'exhaustivité** : quelques
  repères de petites vues de détail peuvent manquer.
- p.63 : la matière du repère 2 et du repère 48 se lit « **A-S5U3** » (désignation d'alliage
  d'aluminium de moulage, ancienne norme AFNOR) — lecture confirmée sur les deux lignes.
- Sommaire vs pages : les intitulés « Lecture d'un dessin d'ensemble », « Graphe de montage et de
  démontage », « Cotation fonctionnelle », « Dessin de définition » annoncés au sommaire (p.4) pour
  les sous-activités 1.1–1.4 et 2.1–2.4 **ne sont pas imprimés sur les pages** : celles-ci ne
  portent que « Activité 1.1 », « Activité 1.2 », etc. Seule exception : « Graphe de montage et de
  démontage » figure bien en titre sur p.47 et p.55.
- Découpage annoncé vs pages réelles : le découpage donné au sommaire est confirmé, avec ces
  précisions — l'activité 1.1 court sur **p.45–46** (et non la seule p.45), l'activité 1.3 sur
  **p.48–49**, l'activité 2.1 sur **p.53–54**, l'activité 2.3 sur **p.56–57**, l'activité 2.4 sur
  **p.58–59**. La présentation du support de l'activité 1 occupe **p.42–44**, celle de l'activité 2
  **p.51–52**, celle de l'activité 3 **p.60–64** (et au-delà).

**p.65–86**

- p.65–86 : bandeau courant imprimé « DÉFINITION DES ELEMENTS D'UN PRODUIT » — **« ELEMENTS » sans
  accent** sur toutes les pages de la tranche. Transcrit tel quel `[sic]`.
- p.65, 69, 78, 82 : les pages ne portent **que** « Activité 3.1 / 3.2 / 4.1 / 4.2 » ; les
  sous-titres « Lecture d'un dessin d'ensemble » et « Cotation fonctionnelle » annoncés au sommaire
  p.4 **ne sont pas imprimés sur les pages**. Écart sommaire ↔ page signalé, la page fait foi.
- p.67 : la pièce (7) est appelée « **biellette** » en C.4 ligne 2 et p.73, mais « **levier (7)** »
  en C.4 ligne 4. Incohérence interne de la source, transcrite telle quelle.
- p.68 : « Consulter les **sequences** de montage » — sans accent `[sic]`.
- p.69 : séparateurs décimaux mélangés dans le même énoncé — `0≤Ja≤0,2` (virgule) et
  `a₂ = 54±0.02` (point). Transcrit tel quel.
- p.70 : l'énoncé nomme le sous-ensemble « **(5 ; B1 ; B1' ; 24 ; 27 ; 28)** » alors que les deux
  dessins de la page ne portent aucun repère **27** ni **28** (ils portent 24, 25, 26). Lecture des
  deux repères de l'énoncé confirmée à l'agrandissement — incohérence de la source, non corrigée.
- p.70 : questions 2 et 4 (« La condition Jc est-elle maximale ou minimale ? ») et 3 et 5
  (« Tracer la chaîne de cotes relative à la condition Jc... ») sont quasi identiques ; elles se
  rapportent aux deux dessins, qui représentent deux positions du coulissement. La différence
  n'est pas explicitée par le texte.
- p.73 : « Compléter la vue de droite en coupe D-D sans **details** cachés » — sans accent `[sic]`.
- p.75 : « manomètre gradué en **KN** » — le symbole SI normalisé est kN. Transcrit tel qu'imprimé
  `[sic]`.
- p.77 : nomenclature typographiquement irrégulière — « **Ecrou** » sans accent (rep. 6 et 12) ;
  « **S 185** » (rep. 1, 13, 14, 19, 20) contre « **S185** » (rep. 7 et 8) ; « **Cu sn 8** » avec un
  s minuscule (rep. 18). Transcrit tel quel.
- p.77 : la désignation du rep. 11, « Vis à tête cylindrique à six pans creux **M4-6** », est
  ambiguë (longueur ? classe ?) mais parfaitement lisible — transcrite littéralement.
- p.81 : le graphe de montage de la **machine de traction** contient une boîte « **69** », repère
  qui n'existe pas dans sa nomenclature (1→21) et qui appartient à la pince de soudage (bague de
  guidage). Lecture confirmée à l'agrandissement — erreur de report de la source, non corrigée.
- p.84 : « Démonter l'arbre (15) support du **mors mobile (14)** » — le mors mobile porte le repère
  **(16)** à la nomenclature p.77 ; (14) est la traverse mobile supérieure. `[sic]`.
- p.66, p.69, p.71–73, p.79, p.82–84 : les valeurs de cotes des dessins à compléter sont
  **volontairement absentes** (pointillés `Ø…`, cadres de tolérance vides). Ce n'est pas une
  illisibilité : rien n'est noté `[?]` à ce titre.
- Aucune valeur numérique de la tranche n'est restée illisible : toutes les cotes de la p.74 et de
  la p.82 ont été vérifiées par agrandissement. **Aucun `[?]` dans cette tranche.**

**p.87–112**

- p.87 : dans le tableau « Savoirs et savoir-faire », la ligne « - Conception assistée par ordinateur (CAO): Modélisation en 3D d'un assemblage. » est imprimée **à cheval** sur la frontière des lignes CD 2.2 / CD 3.8 (elle déborde de la cellule bleue de CD 2.2 sans être clairement dans celle de CD 3.8) — rattachement à CD 3.8 = **choix de transcription**.
- p.90 / p.91 : désignations des repères **12**, **40** et **45** imprimées « Roulement…………… » (pointillés) — **valeur absente dans la source**, volontairement, pas illisible.
- p.95 : la question 1 parle des « **quatre** écrous (53) » alors que la nomenclature partielle de la même page donne **Nbr. = 8** pour le repère 53 — contradiction interne de la source, transcrite telle quelle.
- p.97 : observations des repères **59** (« Rondelle plate M8 » → **ISO 4032**) et **60** (« Écrou hexagonal M8 » → **DIN 126**) — apparemment **interverties** : p.91, la même source associe ISO 4032 à l'écrou hexagonal (rep. 31) et DIN 126 à la rondelle plate (rep. 32). Transcrit tel qu'imprimé, marqué `[sic]`.
- p.98 : « **Quelle** est le rôle des rondelles (57) ? » — accord fautif dans la source, noté `[sic]`.
- p.98 : « **peu-t-on** monter l'arbre porte fraise horizontal ? » — coquille de la source, notée `[sic]`.
- p.100 : contradiction interne sur le repère — la situation problème vise « le pignon arbré **(14)** », la question 1 demande l'assemblage « entre l'arbre **(9)** et la roue conique », et le bloc encadré du F.A.S.T. écrit « entre l'arbre **(14)** et la roue conique ». Or la nomenclature p.90 donne (9) = « Roue dentée : Z9=50 dents » et (14) = « Pignon arbré conique Z14=23 dents ». Les trois formulations sont transcrites telles quelles.
- p.101 : le repère **65** porté sur la vue en coupe à compléter n'existe dans **aucune** nomenclature de la tranche (la nomenclature de la tête s'arrête à 64) — transcrit tel quel.
- p.111 : « Démonter le **couvercle (4)** » alors que le repère (4) désigne le « Carter inférieur » dans la nomenclature p.106 (les couvercles y sont les repères 3, 13, 18 et 23) — contradiction interne, transcrite telle quelle.
- p.92 / p.107 : le graphe de caractérisation n'imprime que les abréviations **c, r, dé, a, di** et leurs formes barrées ; **la source ne donne nulle part dans cette tranche la signification de ces abréviations** — elles sont donc transcrites sans être développées.
- p.93 vs p.107 : les indices des degrés de liberté sont imprimés de façon inconstante (**TX TY TZ RX RY RZ** en p.93, **Tx TY Tz Rx Ry Rz** en p.107) — reproduits page par page tels qu'imprimés.
- p.4-5 (sommaire) vs pages : le sommaire annonce des sous-titres (« 1.1 Les liaisons mécaniques », « 1.2 Les assemblages », « 1.3 Les assemblages », « 1.4 Les assemblages », « 1.5 Guidage en rotation », « 2.1 Les liaisons mécaniques », « 2.2 Les assemblages », « 2.3 Guidage en rotation ») qui **ne sont imprimés sur aucune des pages 92 à 112** : celles-ci ne portent que « Activité 1.1 » … « Activité 2.3 » sous le bandeau « TYPOLOGIE DES ASSEMBLAGES - ASSEMBLAGE ». Les titres de la fiche suivent donc la **page**, pas le sommaire.

**p.113–128**

- p.120 vs p.121 : la nomenclature donne `Nbr. = 1` pour la **roue avant (56)**, mais l'encadré de la p.121 parle des « **deux** roues avant (56) » — contradiction interne de la source, transcrite telle quelle.

- p.113 : « batterie 48v » — unité écrite en minuscule (au lieu de 48 V) — noté `[sic]`.
- p.114 / p.120 : cartouches « Echelle: 1:2 » et p.126 « Echelle:2:5 » — « Echelle » sans accent
  dans la source — transcrits tels quels.
- p.115 → p.116 : **la ligne du repère 27 est imprimée deux fois** (dernière ligne de la p.115 et
  première ligne de la p.116, à l'identique : « Arbre d'entrée N27 = 3000 tr/min »). Ce n'est pas
  une erreur de lecture : les deux pages la portent. Il y a donc **54 repères pour 55 lignes**.
- p.116 : la case **Nbr. du repère 51** (« Arbre moteur Nm = 3000 tr/min ») est **vide** dans la
  source — noté `[?]` dans le tableau ; toutes les autres lignes portent une quantité.
- p.115 / p.116 / p.120 : la colonne **Observation est vide sur la totalité des trois
  nomenclatures** ; de nombreuses cases **Matière** le sont aussi (notamment tous les roulements,
  clavettes standard exclues, joints, écrous et anneaux). Choix de transcription : `—` = case
  vide dans la source (aucune valeur n'a été devinée).
- p.116 : incohérence d'accentuation interne à la nomenclature — rep. 30 « **Écrou** hexagonal
  ISO 4032 – M12 - 08 » contre rep. 34 « **Ecrou** hexagonal ISO 4032 – M16 - 08 » (et p.120
  rep. 59 « Ecrou hexagonal M12 ») — noté `[sic]`, transcrit tel quel.
- p.116 : rep. 29 imprimé « Pignon conique **:Z29** = 16 dents » (espace manquant avant le Z,
  contrairement à toutes les autres lignes de denture) — noté `[sic]`.
- p.119 : le tableau h. désigne le repère 37 par « **Pignon** conique (37) », alors que la
  nomenclature p.116 **et** la vue 3D p.113 le désignent « **Roue** conique (37) ».
  **Contradiction interne du manuel** — transcrite telle quelle avec `[sic]`.
- p.118 : « Les vis (39) éliminent les 6 degrés de **libertés** » (pluriel dans la source, et
  « La vis (39) » au singulier à la ligne précédente alors que le repère 39 compte 6 vis) — noté
  `[sic]`.
- p.119 : le schéma cinématique porte « **Courronne** de direction du chariot » (deux « r ») —
  noté `[sic]`.
- p.121 : question d. « … des bagues intérieures et **extérieurs** » (accord masculin dans la
  source) — noté `[sic]`.
- p.123 : dans le graphe FAST, « **Epaulement** » est imprimé sans accent dans les deux branches
  S1 et S2 — noté `[sic]`.
- p.123 → p.124 : **la numérotation des questions repart à 1** en haut de la p.124 alors que la
  p.123 s'arrête à la question 2 de la même activité 3.3. La p.124 n'est pas une nouvelle
  activité (aucune pastille « Activité » n'y est imprimée) : ses questions 1 à 4 prolongent bien
  celles de la p.123. Constat de source, pas une erreur de lecture.
- p.123 : dans le graphe de liaison `40 — 44`, les cinq symboles du bas (`c`, `r`, `dé`, `a`,
  `di`) sont surmontés d'une barre de complément ; la barre est nettement lisible mais le manuel
  n'explicite nulle part la signification des lettres dans cette tranche (aucune légende
  imprimée p.113–128) — transcrit à l'identique, sans interprétation.
- p.117 : l'actigramme A-0 imprime « **Energie** électrique et hydraulique » (E sans accent) —
  noté `[sic]`.
- p.126 : sur le dessin de la nouvelle conception, le repère **1** apparaît **deux fois** (une
  amorce en haut à droite et une en bas à gauche), les deux pointant vers le bâti partie
  supérieure ; les deux roulements neufs sont repérés **R₁** et **R₂** (repères propres au
  dessin, absents de la nomenclature p.115–116).
- p.117 / p.120 : les titres « Les assemblages » (3.1) et « Guidage en rotation » (3.2) donnés au
  sommaire p.5 **ne sont pas imprimés sur les pages elles-mêmes** (bandeau « TYPOLOGIE DES
  ASSEMBLAGES » seul) ; en revanche 3.3 porte bien « LES ASSEMBLAGES » (p.123) et 3.4 « GUIDAGE
  EN ROTATION » (p.125–126) sous le bandeau. Écart sommaire ↔ page signalé ; les titres retenus
  dans cette fiche sont ceux du sommaire, avec mention du bandeau réel.
- p.113–116 : ces quatre pages **ne portent aucun badge de compétence** (CD 2.x / CD 3.x), alors
  que toutes les pages 117 à 128 portent « CD 2.2 / CD 3.8 ». Constat, pas une illisibilité.
- p.122 : les libellés fins de la copie d'écran du logiciel PyVot0.6 (graduations du cadre
  « Cahier des Charges Fonctionnel ») sont à la limite de lisibilité à 150 dpi ; seuls les
  libellés sûrs ont été transcrits (« Efforts sur l'arbre », « Intensité et répartition »,
  « Coût admissible », « Lubrification - Etanchéité », « Mobilité bagues/charge radiale »,
  « très faible », « Intérieure », « Extérieure »). Aucun autre n'a été deviné.

**p.129–162**

- p.129 : « Machines **thérmiques** » (accent aigu parasite) dans le bandeau SÉQUENCE, alors que la
  même expression est correctement orthographiée « thermiques » dans CD 1.9 juste en dessous —
  noté `[sic]`.
- p.129 : la cellule « Savoirs et savoir-faire » est **fusionnée** entre les lignes CD 1.3 et
  CD 2.3 dans l'imprimé ; ma restitution en tableau Markdown duplique la référence — choix de
  transcription signalé.
- p.131 et p.139 : **aucune cote chiffrée** n'est portée sur les dessins d'ensemble, alors que les
  énoncés p.135 (« D = … ; d = … ») et p.141 (« Relever les valeurs de "R" et "r" ») en demandent
  le relevé. Le relevé se fait donc à la règle, converti par l'échelle du cartouche (3:10 p.131,
  1:2 p.139). Les valeurs de D, d, R, r ne sont **pas** dans le manuel — noté, pas deviné.
- p.137 : la pastille « **Activité 2.1** » n'est suivie d'**aucun sous-titre imprimé** (contrairement
  à 2.2, 2.3, 2.4, 2.5 qui en portent un). Le sommaire p.5 la nomme « Transmission de mouvement ».
  J'ai conservé le titre imprimé (vide) et signalé l'écart plutôt que d'importer le titre du
  sommaire.
- p.139 : « Vue suivant F (3 et 13) — **Echelle reduit** » (accord et accent manquants pour
  « Échelle réduite ») — noté `[sic]`.
- p.141, question e : « Progressif ☐   **Instantanée** ☐ » — accord au féminin alors que la
  question porte sur « le type de cet embrayage » — noté `[sic]`.
- p.145, question b : « Tracer et repérer la trajectoire **TC(12/18)** du point **C(16/18)** » —
  les indices de la trajectoire et du point ne concordent pas (la même question a, juste au-dessus,
  est cohérente : TD(17/18) du point D(17/18)) — noté `[sic]`.
- p.149 : le schéma cinématique porte les roues **Z₁₃** et **Z₁₈**, mais le tableau des nombres de
  dents ne donne que **Z₁ à Z₁₂**. Les dentures de Z₁₃ et Z₁₈ ne sont donc pas fournies dans la
  tranche — constat, pas une lecture douteuse.
- p.150 / p.148 : le tableau des positions de la boîte de vitesses du tour compte **9 positions**
  (p.150) alors que la question f (p.148) demande d'« identifier le nombre de vitesses possibles de
  l'arbre broche » ; le manuel ne préremplit rien — pas de contradiction, mais le nombre 9 est un
  indice imprimé.
- p.150 : les deux rendements sont notés avec la **même lettre η** (« Rendement du système
  poulies-courroies : η = 0,8. Rendement de la boite de vitesse est η = 0,9. ») sans indice
  distinctif — transcrit tel quel. La couche-texte du PDF rend ce caractère par « Ș », l'image
  montre bien un êta grec.
- p.155–160 : la maquette de boîte de vitesses annonce **5 vitesses + marche arrière** (tableaux
  p.160), mais la question B.2 (p.159) demande d'en « déduire le nombre de vitesses possibles » —
  cohérent, simplement non pré-rempli.
- p.160 : la graduation de l'axe des abscisses saute de **6** à **6,6** puis **7** (au lieu de 6,5)
  — noté `[sic]`.
- p.160, question a : « A partir du graphique (**voir page précédente**) » alors que le graphique
  est imprimé **immédiatement au-dessus, sur la même page** (p.160) ; il n'y a pas de graphique sur
  la p.159 — incohérence de renvoi de la source, signalée.
- p.160 : dans la ligne « M. Arrière », les repères sont notés **Z5, Z6, Z32, Z33, Z34, Z31** ; ce
  sont les **numéros de nomenclature** de la p.157 (et non des variables Z indépendantes comme dans
  le tableau p.149). Transcription littérale conservée.
- p.161, Fig.3 : « **Machoires** » (sans cédille) — noté `[sic]`.
- p.162, question 8 : « Compléter, au crayon et **au instruments** » (au lieu de « aux
  instruments ») — noté `[sic]`.
- p.130, 133, 140, 148, 155, 158 : le manuel écrit alternativement « **boite** » / « **boîte** » et
  « boîte des vitesses » / « boîte de vitesses » ; j'ai conservé chaque graphie telle qu'imprimée
  sans uniformiser.
- p.132, nomenclature rep. 14 : « Bague de la butée » (Nbr. 2), alors que le § Fonctionnement p.130
  appelle « butée d'embrayage (14) » ; désignations transcrites toutes deux telles quelles, sans
  arbitrage.
- Aucune page manquante ni saut de numérotation dans la tranche : les pages 129 à 162 se suivent et
  chacune porte son folio imprimé.

**p.163–200**

- p.167 : la question 7.a désigne « la **bobine (21)** », alors que la nomenclature p.165 donne
  **21 = Arbre moteur** et **22 = Bobine** (la classe A de la question 5 p.166 contient d'ailleurs
  bien le repère 22). **Contradiction interne de la source** — transcrite telle quelle `[sic]`,
  non corrigée.
- p.166 : la 4<sup>e</sup> ligne du tableau des mouvements est libellée « **Bride moteur (10)** »,
  alors que la nomenclature p.165 donne **10 = Flasque**. **Contradiction interne de la source** —
  transcrite telle quelle `[sic]`.
- p.177 / p.178 : le dessin d'ensemble de la table longitudinale porte les repères **47** et
  **48** (vérifiés à l'agrandissement), mais la nomenclature p.178 **s'arrête au repère 46** —
  aucune ligne 47/48 sur la page, et aucune page de continuation. **Nomenclature incomplète dans
  la source.**
- p.172 : « **Faiseuse** Milko » — coquille pour « Fraiseuse » — noté `[sic]`.
- p.169 : « Les commandes des baladeurs sont **ramennées** dans le même plan » — coquille pour
  « ramenées » — noté `[sic]`.
- p.174 : le symbole du rendement est imprimé « **Ŋ** » (glyphe de substitution) au lieu de
  « η » ; la valeur **0,8** est nette. Transcrit `Ŋ = 0,8` avec la mention `[sic]`.
- p.172 : « \* Combinaison des **levier** » (singulier au lieu de « leviers ») — noté `[sic]`.
- p.173 : « compléter le tableau **si dessous** » (pour « ci-dessous ») — noté `[sic]`.
- p.169, p.177, p.184, p.185, p.193 : cartouches imprimés « **Echelle** » sans accent (contre
  « Échelle » p.164) — transcrits tels quels `[sic]`.
- p.176 : encart « Zone d'**etude** » sans accent (contre « Zone d'étude » p.163 et p.168) —
  noté `[sic]`.
- p.189 : « Que peut-**t**-on dire » — trait d'union surnuméraire — noté `[sic]`.
- p.198 : « le rapport de vitesse de cet **engrainement** » (pour « engrènement ») — noté `[sic]`.
- p.171 : la ligne **51** de la nomenclature est imprimée avec « … » en colonne Nbr. et
  « ……………………………. » en Désignation : **case volontairement vide**, à remplir par l'élève avec la
  vis de pression introduite à la question 5.b p.175 (où le repère 51 apparaît sur le dessin).
  Ce n'est pas une illisibilité.
- p.186 : les nombres de dents des repères **7** (« Z = …. ») et **8** (« Z = ….dents ») sont
  imprimés en pointillés — **volontairement laissés à compléter** par l'élève (ils sont
  précisément l'objet de la question B.2 p.197). Ce n'est pas une illisibilité.
- p.172 : les six lignes de la plaque des vitesses sont lues sur la **photographie** de la machine
  (agrandissement ×2,5) : 50 | 128, 240 | 92, 68 | 180, 910 | 352, 653 | 1700, 1280 | 490. La
  photo est nette, mais il s'agit d'un relevé sur photo et non d'un tableau typographié :
  à revérifier si une valeur devait être utilisée telle quelle dans un exercice.
- p.163 et p.187, p.200 : les QR-codes étiquetés **Vid** / **PDF** ne sont pas décodés (contenu
  externe non transcrit).
- p.166 : le schéma cinématique partiel du frein (en bas à droite) est une **ébauche à compléter**
  sans légende imprimée ; seules la classe **A** et trois amorces en pointillés sont visibles —
  décrit, non recopié.
- **Écart au sommaire (p.5)** : le découpage annoncé attribue « 4.1 Étude de frein p.166 »,
  « 4.2 Boite de vitesses p.168 », « 4.3 Transformation de mouvement p.176 », « 5.1 Machine
  thermique p.187 », « 5.2 Étude d'embrayage p.192 », « 5.3 Boite de vitesses p.196 »,
  « 5.4 Synchroniseur p.199 » — **toutes ces pages d'ouverture sont confirmées sur les pages
  elles-mêmes**. Deux nuances : (a) pour l'activité 4, le bloc **présentation du frein**
  (p.163–165) précède le titre « Activité 4.1 » qui n'apparaît qu'en p.166 ; (b) pour l'activité
  5.2, le titre « Activité 5.2 » ouvre bien la p.192 mais sur une **« Présentation de
  l'embrayage »** (fonctionnement + nomenclature + dessin p.193) : la « Situation déclenchante /
  Travail demandé » ne commence qu'en **p.194**.

**p.201–215**

- p.205 : repère 22, observation imprimée « **6005 2RSL** » — vraisemblablement une coquille pour
  « 6005 2RS1 » (comparer aux repères 4 et 6) ; transcrit tel quel, noté `[sic]`.
- p.205 : repères 13 et 20 portent littéralement « **Z13= ?** » et « **Z20 = ?** » — ce ne sont pas
  des valeurs illisibles mais les **inconnues volontaires** de l'activité 6.2 (question 2, p.209).
- p.205 : le rendu de la couche-texte donne « autolubri¿ante » et « ¿xation » (repères 12, 18, 23,
  33) ; **l'image imprime bien** « autolubrifiante », « Vis de fixation », « Disque fixe de
  friction » — il s'agit d'un artefact de ligature « fi », pas d'une coquille de la source.
- p.208 : la colonne du diagramme FAST est titrée « **Proceusseurs/Composants** » — coquille pour
  « Processeurs » ; transcrit tel quel, noté `[sic]`.
- p.208–210 : le bandeau de page imprime « **Train épicycloidal** » (sans tréma) alors que le corps
  du manuel écrit « épicycloïdal » (p.201, 202, 213) ; transcrit tel quel, noté `[sic]`.
- p.209 : l'étiquette de liaison imprimée est « **Adhèrence** » (accent grave) au lieu de
  « Adhérence » ; transcrit tel quel, noté `[sic]`.
- p.210 et p.211 : le symbole du rendement est rendu par le glyphe « **ŋ** » (eng) au lieu de la
  lettre grecque **η** (eta) — substitution de police, visible à la fois dans « Le rendement du
  palan ŋ = 0.75 » (p.210) et dans le titre « b. Rendement ŋ » (p.211), alors que les formules de
  la p.211 utilisent bien η ; noté `[sic]`, transcrit η dans les formules.
- p.211 : le titre de l'encadré est « **2. Synthèse assemblage** » alors que la synthèse porte
  intégralement sur la transmission de puissance — vraisemblablement un reliquat du thème
  précédent ; transcrit tel quel, noté `[sic]`.
- p.211 : l'organigramme imprime « Sans/Avec **modification de vitesses angulaire** » (accord
  fautif : « vitesses angulaire ») ; transcrit tel quel, noté `[sic]`.
- p.211 : « **Boite de vitesses** » est imprimé sans accent circonflexe ; transcrit tel quel.
- p.212 : la formule du couple transmissible par embrayage à friction plane imprime
  « Ct = (2/3) . n . f . **N** . (R³−r³)/(R²−r²) » alors que la légende qui suit définit
  « **F** : Effort presseur des surfaces de friction en N » — **incohérence de la source** entre la
  formule et sa légende (le « N » y tient la place de l'effort presseur F). Les trois autres
  formules de la même page (embrayage conique, limiteur, frein) utilisent bien F. Transcrit tel
  quel, noté `[sic]`.
- p.214 : « Le déplacement linéaire "x" de la crémaillère pour une rotation θ **en degrés** :
  x = R .θ » — la relation imprimée n'est homogène qu'avec θ en radians ; transcrite telle quelle,
  sans correction.
- p.215 : la formule portée **sur la figure** est « Cylindrée = **π.D⁴**/4 · course » (exposant 4)
  alors que le texte de la même page donne correctement « V = π.D²/4 . L » ; transcrit tel quel,
  noté `[sic]`.
- p.201 / p.203 / p.204 : le manuel écrit « chaine » sans accent circonflexe dans le corps du texte
  et dans le titre du support (p.201–202), mais « **chaîne** » dans les cartouches des dessins
  d'ensemble (p.203, p.204) et à la p.210 ; les deux graphies sont conservées telles qu'imprimées.
- p.202 : « Le palan électrique à chaine est composé **d' :** » — apostrophe suivie du deux-points ;
  transcrit tel quel.
- p.206 : « **Quelle est** le type de commande de frein ? » (accord fautif au féminin) ; transcrit
  tel quel, noté `[sic]`.
- p.209 : « La couronne planétaire (37) **bloqué** » (accord fautif) ; transcrit tel quel.
- p.202 : sur le schéma cinématique, les repères sont regroupés (37+38+39, 9+10, 16+17, 20+26) ;
  aucune cote ni valeur numérique n'y est portée — rien d'illisible, mais rien d'exploitable
  numériquement non plus.
- p.203–204 : les dessins d'ensemble ne portent **aucune cote chiffrée** (seulement les échelles
  1:2 et 5:4 et l'annotation « Jeu ») ; les rayons R et r demandés en 6.1-A.7 doivent donc être
  **relevés graphiquement** par l'élève sur le dessin — le manuel ne les imprime nulle part.

**p.216–251**

- p.216 : « Détermination correcte des différentes types de sollicitations » — accord fautif dans le tableau de la carte du manuel — noté `[sic]`.
- p.216 : « Moments fléchissant » (sans -s) et « Maitrise » (sans accent circonflexe) — noté `[sic]`.
- p.216 vs p.227-251 : **incohérence de titre du thème dans la source** — la page d'ouverture imprime « COMPORTEMENT DES SOLIDES DÉFORMABLES » (pluriel, accentué), les en-têtes courants des p.227 à 251 impriment « COMPORTEMENT DU SOLIDE DEFORMABLE » (singulier, sans accent), et la synthèse p.251 reparle des « solides déformables ». Le découpage fourni à la session annonçait « Comportement du solide déformable » : c'est la variante des en-têtes, pas celle de la page d'ouverture.
- p.217, p.218 : « Eprouvette » sans accent sur les annotations de figure (« Éprouvette » avec accent dans le texte courant) — noté `[sic]`.
- p.219 : « … de trois éprouvettes (acier, laiton et  aluminium),. » — double espace et ponctuation « ,. » — noté `[sic]`.
- p.219 : « Fixer l'autre bout dans la machoire. » (sans accent circonflexe ; « mâchoire » accentué p.220) — noté `[sic]`.
- p.220-221 : séparateur décimal **point** (« 12.5N », « 2.5 + 10 », « 7.5 », « 22.5 ») là où la p.219 emploie la **virgule** (« 2,5 », « 7,5 ») — incohérence de la source, transcrite telle quelle.
- p.221 : « Varier l'intensité de la charge et completer le tableau suivant. » (sans accent) — noté `[sic]`.
- p.221 : « Limite élastique au cisaillement   Reg = 48 N/mm² » — le manuel écrit « Reg » sans indice typographique ici, alors que la synthèse p.250 écrit « R_eg » ; transcription conservée telle qu'imprimée.
- p.222 : titre « Banc d'essais de flexion » (pluriel) contre « Banc d'essai de torsion » (singulier) p.217 — incohérence de la source.
- p.225 : « On déduire le moment de flexion maximal M_fMaxi » — noté `[sic]` (lire « On déduit » / « En déduire »).
- p.226 : « Comparer les valeurs de la flèches trouvées » — noté `[sic]`.
- p.226 : « avec celles de l'étude théoriques » — noté `[sic]`.
- **p.229 : contradiction interne du manuel** — « Puissance du moteur électrique **(13)** : P_m = 0.55 KW », alors que la nomenclature p.227 donne (13) = **Poulie réceptrice** et (21) = **Moteur électrique** ; la ligne suivante réutilise d'ailleurs (13) pour la poulie réceptrice (« D₁₃ = 48 mm »). Le repère correct est vraisemblablement (21) — noté `[sic]`, non corrigé.
- p.229 **et p.242** : le symbole du rendement est imprimé de manière ambiguë (glyphe proche de « ŋ ») ; transcrit **η** partout — noté `[?]` sur le glyphe exact.
- p.232, p.238, p.244 : « Déduire à quelle type de sollicitation est soumise/soumis … » — noté `[sic]` (lire « à quel type »).
- p.238 : « Le coéficient de sécurité est s=2. » — noté `[sic]`.
- p.238 : « En utilisons la condition de résistance à la flexion trouver le diamètre minimal » — noté `[sic]` (lire « En utilisant »).
- p.238 : l'acier est écrit **S275** (sans espace) alors que la nomenclature p.234 écrit **S 275** (avec espace) — incohérence de la source.
- p.239 : « efféctué », « éffectué », « reglage », « Trainard » (annotation de figure) contre « traînard » (texte) — noté `[sic]`.
- p.240 : le dessin d'ensemble porte un repère isolé « **S** » au centre-droit, qui n'apparaît pas dans la nomenclature p.241 (probable repère de section ou d'organe de commande) — noté `[?]`.
- **p.242 : contradiction interne du manuel** — la question A.1 énonce « L'action de la roue **(33)** sur le pignon arbré (39) », mais le sous-item a. demande « Relever le rayon de la roue **(39)** sur le dessin d'ensemble ». Le repère (39) désigne le *pignon arbré*, pas une roue. Transcrit verbatim, non corrigé.
- p.242 : « et en modélise le pignon arbré (39) par la figure ci-contre » — noté `[sic]` (lire « on modélise »).
- p.242 : sur la figure de l'engrènement, le point coté **D** est en périphérie et **C** au-dessous ; sur le modèle de poutre de la même page, **D** désigne l'extrémité droite de la poutre (x = 125 mm) et **C** le point d'application de T (x = 40 mm). Le manuel réutilise donc les lettres C et D avec deux sens différents dans une même page — signalé, non corrigé.
- p.245 : « sa langueur maximale x_max = 1165mm » — noté `[sic]` (lire « longueur »).
- p.246 : la nomenclature de la grue est imprimée **sans** ligne d'en-tête colorée mais avec la ligne « Rep. | Nb. | Désignation | Matière | Observation » **en bas** du tableau (convention du dessin technique) ; ordre des repères de 6 vers 1, restitué tel quel.
- p.247 : « le repère lié à la flèche extensible est pivoté dans angle de θ = 38° par rapport à sa position réelle » — noté `[sic]` (lire « d'un angle »).
- p.249 : « un tube de section carrée supposé constante » — accord fautif — noté `[sic]`.
- p.250 : « Un arbre de section circulaire sollicité à la torsion peut résister en toute sécurité **si**  à cette sollicitation **si** : τ_maxi ≤ R_pg » — répétition de « si » dans la phrase imprimée — noté `[sic]`.
- p.250 : « α : angle relatif de torsion en **rd** ; θ : est exprimé en **rd/mm** » — l'abréviation « rd » est employée ici, alors que trois lignes plus bas le même paragraphe (§ d) écrit « rad/mm ou rad/m » — incohérence de la source, transcrite telle quelle.
- **p.251 : défaut d'impression avéré** — dans la formule du moment idéal de flexion, les signes « − » et « + » sont **absents** (deux blancs subsistent), donnant « Mf_i = (1 ␣ 1/(2λ)) Mf ␣ (1/(2λ)) √(Mf² + Mt²) ». Vérifié par agrandissement de l'image. La forme complète est celle imprimée trois fois dans les activités (p.232, 238, 244). Noté `[sic]`, non corrigé dans la transcription du § 4.b.
- p.251 : « La quantité I_GZ/v est appelée **module de rigidité à la flexion** » — appellation de la source (usuellement « module de flexion ») ; transcrite verbatim.
- p.251 : la phrase « Un arbre est soumis à une sollicitation de flexion-torsion si le moment résultant en G est : » est suivie d'un saut de ligne et de deux phrases, la formule M_G = M_t.x⃗ + M_f.z⃗ étant imprimée **après** la phrase suivante, en petit corps ; l'ordre de lecture imprimé est restitué tel quel.
- p.237 : la question 3 annonce « les figures ci-dessous », mais les deux repères de tracé sont imprimés **en haut de la page suivante (p.238)** ; ce n'est pas une figure manquante, seulement un enjambement de page.
- p.218, p.234, p.246 : plusieurs cellules « Matière » et « Observation » sont **vides à l'impression** (travail d'élève ou information non fournie) ; restituées par *(vide)*, jamais devinées. La nomenclature de la p.227 est en revanche annoncée « **partielle** » et ne porte que trois colonnes (Rep. / Nbr. / Désignation) : elle n'a ni « Matière » ni « Observation ».
- p.234 : le dessin d'ensemble ne porte **aucune cote chiffrée** ; la question 8 de la p.238 (« Relever le diamètre du dessin d'ensemble ») suppose donc une mesure à l'échelle indiquée (2:9) — noté `[?]` sur la valeur attendue, qui n'est pas imprimée.
- p.246 : idem, le dessin d'ensemble de la grue ne porte que **H_maxi = 2519**, **H_mini = 540**, **θ = 38°** et **θ = 35°** comme valeurs chiffrées.

**p.252–288**

- **p.286 : coquille de la source.** Légende de croquis « Montage **de** d'usinage » (« de » surnuméraire) — noté `[sic]`.
- **p.286–288 : écart entre le sommaire et les pages.** Le découpage annoncé (« Synthèse p.285 ;
  p.286-288 = fin de manuel : bibliographie, annexes, tables, quatrième de couverture… ») ne
  correspond pas au manuel. Ce que portent réellement ces pages : **p.286 = suite de la Synthèse
  obtention des pièces** (cotes machines/outils/appareillage, transfert de cotes, métrologie,
  contrôles géométriques) ; **p.287–288 = une seconde synthèse, « 3. Synthèse plasturgie »**
  (classification des plastiques + les six procédés de mise en œuvre). La toute dernière ligne
  imprimée est « Grille d'évaluation des savoirs et savoir-faire de l'apprenant » suivie d'un
  QR-code PDF. **Aucune page de fin d'ouvrage n'existe dans le PDF fourni.**
- **p.257 : en-tête erroné.** La première page du Projet 1 (« Maquette d'un train épicycloïdal »)
  porte encore l'en-tête courant « **PLASTURGIE** » ; l'en-tête passe à « **PROJET** » à partir de
  p.258 et le reste jusqu'à p.288 — y compris sur les deux pages de la synthèse plasturgie
  p.287–288, qui ne sont pas un projet.
- **p.253–288 : en-tête courant « OBTENTION DES PIECES »** — imprimé sans accent sur toutes les
  pages de la tranche, alors que le bandeau d'ouverture p.252 écrit « OBTENTION DES PIÈCES ».
  Noté `[sic]` une seule fois.
- **p.275 : contradiction interne sur le numéro de phase.** Le contrat de phase est intitulé
  « **Phase N° 30** · Désignation : Tournage · Machine-outil : Tour parallèle », mais ses
  opérations (Cm10 = 78, 2Cm11 = Ø8g6, Cm12, gorge Cm13, chanfreins 14 et 15) sont **exactement
  celles de la phase 40** de la feuille d'avant-projet p.274 ; la phase 30 de la FAPF (p.273) est
  un **TARAUDAGE MANUEL**. Transcrit tel quel.
- **p.274 vs p.275 : repères et tolérances divergents pour la même opération.**
  p.274 § g imprime « 2Cm10=Ø8g6 et Cm12= ? » là où p.275 imprime « 2Cm11=Ø8g6 et
  Cm12=57<sup>±0,05</sup> » ; p.274 § h imprime « 2Cm13=6.5<sup>±0,1</sup> et
  Cm13=69<sup>±0,05</sup> » là où p.275 imprime « Cm13=69<sup>±0,1</sup> et
  2Cm13=Ø6,5<sup>±0,1</sup> ». Les deux versions sont transcrites à leur page respective.
- **p.278 : coquille sur un numéro de phase.** La ligne « N° phase **50** » (taraudage manuel de
  la douille) porte comme opération « **Exécution de la phase 40** » — repris de la ligne
  précédente. Noté `[sic]`.
- **p.255 : coquille de la source.** « **Qu'elles** techniques peut-on adopter… » (pour
  *Quelles*) — noté `[sic]`.
- **p.255 : désignation divergente.** La ligne du tableau c. nomme le repère 6 « **Moulure
  (coque) (6)** » alors que la nomenclature p.254 le désigne « Coque ». Transcrit tel quel.
- **p.256 : coquilles de la source.** « La coque du pédalo est **obtenu** par rotomoulage » ;
  « une grande résistance aux pièces **fabriquée** » ; légende de figure « la matière fond et
  **adhére** au moule ». Notées `[sic]`.
- **p.257 et p.281 : coquille de la source.** « **Faite** une étude complète et structurée »
  (pour *Faites*) — sur les deux projets. Noté `[sic]`.
- **p.279 : coquille de la source.** « **On tenant** compte des paramètres… » (pour *En tenant*)
  — noté `[sic]`.
- **p.281 : coquille de la source.** « des transmissions irrégulières, qui sont **utilisés** » —
  noté `[sic]`.
- **p.268 : coquille de la source.** Repère 30 désigné « Douille **taraudé** » (accord manquant)
  — noté `[sic]`.
- **p.286 : coquille de la source.** Légende de figure « Référentiel des **côtes** diamétrales »
  (pour *cotes*) — noté `[sic]`.
- **p.267 / p.269 / p.270 / p.271 / p.272 : cartouches sans accent.** Le titre des dessins est
  imprimé « Maquette train **epicycloïdal** » dans les cartouches, alors que les feuilles
  d'avant-projet p.273–274 écrivent « Maquette train **épicycloïdal** ». Transcrit tel quel.
- **p.258 : lecture du tri croisé.** Les cellules des lignes FC5 et FC6 nomment la fonction de la
  **colonne** et non celle de la ligne (« FC6/1 », « FC5/1 », « FC7/2 »). Ce n'est pas une erreur :
  les points attribués (FC5 = 1, FC6 = 1, FC7 = 2, total 50) sont cohérents avec cette lecture.
  Transcrit verbatim.
- **p.285 : redondance apparente de la source.** Les paragraphes **b. (pièce cylindrique courte)**
  et **c. (pièce cylindrique longue)** énoncent le même triplet de règles (« Centrage long
  (1,2,3,4) élimine Ry, Rz, Ty et Tz / Appui ponctuel (5) élimine Tx / Serrage contre le centrage
  long ») ; le b. se termine en outre par un **tiret vide**. Transcrit tel quel.
- **p.252 : décalage de tableau.** Dans le tableau « Obtention des pièces », les blocs de la
  colonne « Savoirs et savoir-faire » ne sont pas alignés sur les étiquettes CD (le bloc
  « enlèvement de matière » déborde sur la ligne CD 2.6, « Plasturgie: » se lit sur la ligne
  CD 2.8 alors que ses procédés sont sur la ligne CD 2.7). Transcription à la position imprimée.
- **p.259 : notation ambiguë.** La colonne « Niveaux » de FP1 imprime « **r** *(indice i)* de 0,25
  à 4 » alors que le critère d'appréciation en regard est « Rapports de vitesses **r** » (sans
  indice). Transcrit `r_i`.
- **p.263 : valeur non explicitée.** Dans « C₂₈ = F₂₈/₂₇ . R₂₈ = 1080 N.mm ; F₂₈/₂₇ = 30 N », la
  valeur de **R₂₈ n'est pas imprimée** (elle vaut 36 mm par cohérence, mais le manuel ne
  l'affiche pas) — non complété.
- **p.263 : expression de section peu lisible.** L'hypothèse RDM imprime la section de la dent
  sous la forme « S = (k.m) . (π.m/2) » ; la partie « (k.m) » est composée en petit corps —
  lecture retenue `(k.m)`, marquée `[?]` sur ce seul facteur.
- **p.269 : cotes de la semelle.** Les cotes **15±0,2** et **20,5±0,1** sont portées près de la
  coupe C-C et leur rattachement géométrique exact n'est pas déterminable sans le dessin
  d'origine ; les valeurs elles-mêmes sont sûres. Aucune valeur devinée.
- **p.275 : colonnes vides.** Les colonnes **f (mm/dent)** et **Vf (mm/min)** du contrat de phase
  sont laissées **entièrement vides** dans la source (elles ne sont pas illisibles) ; de même les
  valeurs de Vc pour toutes les opérations sauf la première (24 m/mn).
- **p.266 / p.282 : dessins non cotés.** Les perspectives éclatées ne portent que des repères de
  nomenclature, aucune cote — rien n'a été déduit.
- **p.284 : matières manquantes.** Vingt-deux repères sur 29 dans la nomenclature du mécanisme à
  came (1, 3, 4, 6, 7, 10, 12, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29) ont
  leur case **Matière** vide dans la source ; ce n'est pas une illisibilité. Seuls 2, 5, 8, 9, 11,
  13 et 16 portent une matière.
