# Journal du lecteur — français 6ᵉ, devoirs D01 à D09 (devoir.tn, école primaire, vague 1)

Étape G2, lecture du 2026-10-19. Sources web, salle blanche : **aucune transcription versionnée** ; snapshots texte hors dépôt
`/tmp/claude-0/devoirs-snapshots/french-6eme/D01..D09.txt` (contrôle anti-copie local), rendus d'images hors dépôt
`/tmp/claude-0/fr6g/render-d/`. Sorties versionnées : `lines/D01..D09.tsv` + `.meta`, `signatures-devoirs.tsv` (mesure des
signatures, § 6) et ce journal, **sans phrase, nom, nombre ni contexte des devoirs**. Conventions : § 0 de
`JOURNAL-lecture-C01-C06.md` (grain, rang, placement F4, jetons HP, étages) et ajouts des lots C07–C19, étendues aux devoirs
par le § 0 du journal des devoirs de l'anglais 6ᵉ. Aucune écriture git, `gisement.json` et `content/french-6eme/` intacts.

## 0. Conventions fixées (premier lot des devoirs du français 6ᵉ)

- **Créneau** : le registre note T1, T2, T3 ; le validateur n'admet que DC/DS : **T1 → DS1, T2 → DS2, T3 → DS3**
  (même correspondance que l'anglais 6ᵉ). Exception : D09 réunit des épreuves de deux trimestres, le créneau suit chaque
  épreuve imprimée (DS2 pour les trois premières lignes, DS3 ensuite) ; le pilote l'écrira par ligne dans `lignes.tsv`.
- **Grain** : une ligne par exercice ou question **numérotée imprimée** ; une question à sous-parties (a, b, c) reste UNE ligne.
  Une question sans numéro imprimé mais comprise dans la suite (D05, sixième) prend son rang. Un exercice dont la consigne n'est pas
  imprimée (D07, cinquième de la langue : lignes vides) n'a **pas** de ligne.
- **Rang** : n°exo unique par document, dans l'ordre de l'épreuve : compréhension, puis grammaire, puis conjugaison, puis
  production en dernier (D09 : la production est placée en dernier alors qu'elle précède l'épreuve de lecture suivante dans le PDF).
- **Épreuves sans partie** : D02 et D05 sont de la compréhension seule, D03, D06 et D08 de la production seule, D04 de la langue
  seule ; D01 et D07 mêlent compréhension et langue sans production notée à part.
- **Production** : une ligne par consigne de rédaction, étage `d3` quand la rédaction est libre et longue (D06, D08, D09),
  `d2` pour une rédaction courte à minimum de phrases (D03, comme la production guidée de l'anglais). Une question de compréhension
  qui demande de rédiger (D01 n°4) reste en compréhension.
- **Barème** : celui de l'imprimé quand il porte sur la ligne : D03 = 10 (note imprimée), D06 = 10, D09 production = 20 (total
  imprimé de l'épreuve). `-` partout ailleurs : D02, D05, D09 (lectures) n'impriment qu'un tableau de critères ou un total, D04 un total
  d'ensemble, D08 des maxima par critère sans total, D01 et D07 rien.
- **Chapitres** : règle F4 et jetons du § 0 des lots C ; compréhension = un seul slug, le module du thème du texte (D01 02, D02 02,
  D05 03, D07 05, D09 lecture du 2ᵉ trimestre 05 et lecture du 3ᵉ trimestre 02) ; production = module du thème de la consigne
  (D03 01, D06 04, D08 08, D09 07). La structure imposée (récit, lettre, description, dialogue) n'ajoute rien : la lettre de D08 est
  dite à l'archétype, son prérequis est le projet du 07 mais la ligne reste placée au 08. Langue : item par item, cumul des notions.
- **Jeton HP nouveau** : aucun. Réemployés : `HP:imparfait` (D04 n°2), `HP:pronom-complement` (D07 n°9).
- **Étages** : compréhension `d1` pour une coche, un relevé ou un appariement sans inférence (huit lignes en tout) ; `d2` dès qu'il
  y a justification, cause, lexique ou avis ; langue `d2` pour un tableau, un classement ou une à trois réponses, `d3` pour au moins
  trois réponses mêlant deux notions (D01 n°10, D04 n°2 et n°4, D07 n°8) ; aucun `d4`.
- **Signature** (mesure demandée, § 6) : *famille* = notion × forme du geste, **chapitres** de la ligne sans jetons HP. Détail
  des familles au § 6.

## 1. Documents lus

Copies de `/tmp/claude-0/fr6g/devoirs/` : **les neuf sha256 égalent le registre et `docs.json`**, les neuf nombres de pages aussi.
`pdftotext` : vide pour D01 (scan, quatre pages lues en vision à 110 DPI, le texte et les deux dernières pages vérifiés), couche texte
propre pour D02 à D09, contrôlée en vision (60 à 70 DPI) sur les pages de tableaux, d'images ou de numérotation douteuse (D02 p. 1,
D03 p. 1, D04 p. 1, D05 p. 3, D06 p. 1, D07 p. 2, D08 p. 1, D09 p. 2, 8 et 10) : lecture `mixte`.

| id | créneau | rubrique registre | sha256 (début) | pages | lecture | lignes | année imprimée | écrit sur |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D01 | DS1 | Langue | 7bd918b5 (oui) | 4 | vision | 13 | 2022/2023 | compréhension + grammaire + conjugaison |
| D02 | DS1 | Lecture | 6fc23df6 (oui) | 3 | mixte | 7 | 2014/2015 | compréhension |
| D03 | DS1 | Production écrite | cac0ec47 (oui) | 2 | mixte | 1 | 2014/2015 | production |
| D04 | DS2 | Langue | 42bd74bf (oui) | 2 | mixte | 4 | 2019/2020 | grammaire + conjugaison |
| D05 | DS2 | Lecture | ee350f1b (oui) | 3 | mixte | 8 | 2019/2020 | compréhension |
| D06 | DS2 | Production écrite | 6e9161af (oui) | 2 | mixte | 1 | 2019/2020 | production |
| D07 | DS3 | Lecture | 414f7e5f (oui) | 2 | mixte | 9 | non datée | compréhension + grammaire + conjugaison |
| D08 | DS3 | Production écrite | bad9475f (oui) | 1 | mixte | 1 | non datée | production |
| D09 | DS2 puis DS3 | Lecture | ecb16428 (oui) | 10 | mixte | 9 | 2010/2011 | trois épreuves de français (§ 2) |

Total : **53 lignes**. `content:gisement:lignes --subject french-6eme --grade 6eme-base` : 9 fichiers, 53 lignes valides,
**0 fautive**. `content:gisement:plan` sur les neuf fichiers (créneaux DS1 à DS3) : 53 lignes, 52 missions littérales (le plan
ne regroupe que les archétypes identiques mot pour mot, d'où la mesure par famille du § 6), 0 hors programme, 9 lots.
Contrôle anti-copie des archétypes et pièges contre les neuf snapshots (suites de trois mots) : **ne subsistent que des termes de
consigne génériques** (vrai ou faux, au passé composé, complément essentiel, son ou sont, passage descriptif, extraire du support…),
aucune expression des énoncés ni des textes.

## 2. Écarts au registre et particularités

- **D01** : classé « Langue », c'est une épreuve « lecture + langue » ; l'imprimé date 2022/2023 (registre : 2024) ; épreuve
  « unitaire n°1 » de plateforme, cohérente avec le créneau T1. Aucun barème.
- **D03 et D08** : même gabarit national de « fiche d'évaluation des acquis » (production seule, critères C1 à C7, tableau de
  maîtrise) ; D03 est datée 2014/2015 (registre : sans année), D08 n'est pas datée ni signée.
- **D04, D05, D06** : l'imprimé confirme la **même main** (même école et même enseignant, année 2019/2020, deuxième trimestre) pour
  la langue, la lecture et la production : voir § 7 (plafond par auteur). Coquilles d'impression sans effet : « 2er trimestre »,
  consigne annonçant plus d'exemples qu'il n'y en a.
- **D07** : rubrique Lecture, mais contenu mixte (compréhension de cinq questions, grammaire et conjugaison de quatre exercices, plus un
  cinquième sans consigne) ; sans date, signature ni barème.
- **D09** : PDF **composite** de dix pages : lecture-compréhension du 2ᵉ trimestre (texte en tête sur deux pages, trois questions
  numérotées 1, 2, 4), production écrite du 3ᵉ trimestre (consigne, grille de critères), **épreuve d'éveil scientifique en arabe**
  (trois pages, hors matière : aucune ligne), lecture-compréhension du 3ᵉ trimestre (questions 1, 2, 3, une seconde « 2 » puis 7, la
  numérotation lacunaire laisse penser à un extrait de feuille plus longue ; texte en page 9), page 10 vide. Trois « Total 20 » imprimés. Une seule main n'est pas prouvée
  (deux en-têtes d'école, dont l'un vide) : les en-têtes de l'éveil scientifique et de la dernière lecture portent le même nom d'établissement.
- **Dates** : D01 est la seule épreuve récente du lot (2022/2023) ; D09 est la plus ancienne (2010/2011).
- **Créneaux** : concordants avec T1, T2, T3 pour D01, D02, D03 (imprimé « 1ᵉʳ trimestre »), D04, D05, D06 (« 2ᵉ trimestre »),
  D08 et D09 (« 3ᵉ trimestre ») ; D07 repose sur le seul classement du site (aucun trimestre imprimé).

## 3. Format des devoirs

| id | parties et points imprimés | questions | durée estimée |
| --- | --- | --- | --- |
| D01 | lecture + langue ; aucun point | 6 compréhension, 4 grammaire, 3 conjugaison | 60 min |
| D02 | lecture-compréhension, note sur 20 mais sans barème par question | 7 | 45 min |
| D03 | production, critères C1, C2, C5, C6, C7, **10 points** | 1 consigne (rédaction minimale imposée) | 45 min |
| D04 | langue, tableau de **6 points** d'ensemble | 4 exercices non numérotés | 30 min |
| D05 | lecture, tableau de critères C2, C3, C4, C6 (maxima : 12,5) | 8 | 45 min |
| D06 | production, critères C1 à C5, C7, **10 points** annoncés (les maxima additionnés en font davantage) | 1 consigne à trois volets | 45 min |
| D07 | lecture + langue ; aucun point | 5 compréhension, 4 langue (+ 1 sans consigne) | 45 min |
| D08 | production, critères C1 à C7 (maxima additionnés : 20), total non imprimé | 1 consigne (lettre) | 45 min |
| D09 | trois épreuves de 20 points chacune (barème par critère) | 3 + 1 production + 5 | 135 min |

Aucun devoir ne comporte d'orthographe-dictée. La langue reste à l'état de grammaire et de conjugaison par exercices courts ;
la compréhension suit le modèle du concours : relevé, vrai/faux justifié, lexique (synonymes, contraires), avis personnel.

## 4. Notions par chapitre (nombre de lignes portant le chapitre, sur 53)

| chapitre | devoirs | examens (C01–C19, 185 lignes) |
| --- | ---: | ---: |
| 01 | 8 | 43 |
| 02 | 22 | 37 |
| 03 | 10 | 23 |
| 04 | 5 | 33 |
| 05 | 13 | 46 |
| 06 | **1** | 40 |
| 07 | **1** | 29 |
| 08 | **1** | 36 |
| `HP:` | 2 | 11 |

- **02** (22 lignes) est surreprésenté par thème : quatre devoirs de compréhension (D01, D02, D09 lecture du 3ᵉ trimestre) et les
  possessifs / démonstratifs de D01 ; **05** par la compréhension de D07 et D09 ; **03** par D05 seul. Les chapitres **06, 07, 08**
  n'apparaissent presque pas : compléments de lieu, de temps, de manière, accord de l'adjectif, dire/lire/écrire, vouloir/pouvoir et
  participe passé avec être ne sont **jamais** testés dans ces devoirs (une ligne chacun : accord de l'adjectif dans une correction, thème
  de la production de loisirs, thème de la production de découverte).
- Langue testée : nature des mots (D01), déterminants possessifs et démonstratifs (D01), accord du verbe avec son sujet (D01, D07),
  négation ne… plus / ne… jamais (D04), son/sont (D04), correction d'accords et de confusions (D04), compléments essentiel et non
  essentiel (D07), impératif (D01), temps (présent, passé composé, futur : D01, D04, D07).
- **Homophones** : seul D04 en teste (son/sont, et/est dans une correction) ; les examens C01–C19 n'en ont aucun.

## 5. `HP:` et programme ancien

- **Part HP : 2 lignes sur 53 (4 %)**, aucune entièrement HP : D04 n°2 (`HP:imparfait`, un repère de temps du contexte impose l'imparfait, non
  enseigné en 6ᵉ) et D07 n°9 (`HP:pronom-complement`, placement du pronom devant l'auxiliaire). Les phrases de D07 contiennent aussi un
  pronom adverbial « en » conservé mais non évalué : aucun jeton.
- **Programme** : D01 `en vigueur` (2022/2023) ; D02, D03, D05, D06, D08, D09 `en vigueur` (aucune notion hors fiche : relevés,
  lexique, récit, lettre, négation…) malgré des dates anciennes ; D04 et D07 `mixte` (une notion HP chacun) ; aucun devoir « ancien »
  au sens fort, comme les examens C07–C19.
- Au regard de l'anglais (76 % de lignes HP, programme entièrement ancien), le français 6ᵉ est **stable** : les devoirs recoupent la fiche.

## 6. Mesure des signatures (règle des 30 % de signatures neuves)

Définition : **famille** (notion × forme du geste, tableau ci-dessous) + **chapitres de la ligne sans jetons HP**, comparée aux
**185 lignes d'examen** C01–C19 classées par le même procédé (72 à 98 signatures distinctes selon la mesure). Fichier ligne à ligne :
`signatures-devoirs.tsv` (famille, signature, trois drapeaux « neuve »).

Familles : compréhension `CR-releve` (relevé, citation d'indices), `CR-vf` (vrai/faux, coche, avec ou sans justification),
`CR-explication` (cause, motif, sentiment), `CR-lexique` (synonymes, contraires, sens d'une expression), `CR-avis` (avis, hypothèse,
conseil, réplique imaginée), `CR-appariement`, `CR-ordre` (remise en ordre d'événements), `CR-titre`, `CR-redaction` (court paragraphe en
compréhension) ; langue `L-temps`, `L-transformation-sujet` (changer de sujet, de genre ou de nombre avec accords), `L-impératif`,
`L-complement`, `L-tableau-fonctions`, `L-negation`, `L-determinant`, `L-adjectif`, `L-pronom`, `L-infinitif`, `L-nature` (nature des mots),
`L-homophone`, `L-correction` ; production `P-recit`, `P-lettre`.

| mesure | lignes neuves | signatures distinctes neuves |
| --- | ---: | ---: |
| **strict** (famille + chapitres, compréhension comprise) | 19 sur 53 (**35 %**) | 16 sur 34 (47 %) |
| **mixte** (compréhension : famille seule ; langue et production : famille + chapitres) | 15 sur 53 (**28 %**) | 14 sur 27 (51 %) |
| **gabarit** (famille seule) | 10 sur 53 (**19 %**) | 8 sur 20 (40 %) |

La mesure **mixte** est la plus juste : en compréhension, le chapitre ne dit que le thème du texte, qui change d'un sujet à l'autre
sans changer le geste, alors que le chapitre d'une ligne de langue est la notion. Elle donne **28 %, juste sous le seuil de 30 %**.
Le strict (35 %) surestime (ex. D07 n°1 et D09 n°1, vrai/faux déjà vu sous un autre thème).

Par devoir (mixte) : D01 3 neuves sur 13, D02 1 sur 7, D03 1 sur 1, D04 3 sur 4, D05 3 sur 8, D06 **0 sur 1**, D07 2 sur 9,
D08 1 sur 1, D09 1 sur 9.

**Geste réellement absent des examens** (famille neuve au niveau gabarit : 10 lignes, 8 familles) : **appariement** (D02 n°5, D09 n°4),
**remise en ordre d'événements** (D05 n°5), **titre à choisir** (D05 n°7), **court paragraphe en compréhension** (D01 n°4), **nature des
mots** (D01 n°7, D05 n°3), **homophone son/sont** (D04 n°3), **correction d'erreurs soulignées** (D04 n°4), **lettre à un
correspondant** (D08 n°1). Les autres lignes neuves ne le sont que par une combinaison de chapitres : changement de sujet avec accord
sur un seul chapitre (D07 n°7), changement de sujet et de temps (D07 n°8), déterminants articles et possessifs (D01 n°9), conjugaison avec
repère de temps (D04 n°2), production courte à choix de sujet (D03 n°1).

Inversement, les examens ont quatre familles que les devoirs n'ont pas : tableau de fonctions, adjectif, pronoms, infinitif.

**Au regard du planificateur** : les devoirs couvrent surtout des gestes déjà vus (lexique, vrai/faux, relevé, avis) : 38 lignes sur 53
n'ont pas de signature neuve (mesure mixte) ; 10 lignes portent un geste absent des examens, réparties en huit familles qui se
rattachent aux chapitres 01, 02, 03, 04 et 08. Le seuil de 30 % est frôlé (28 %), pas franchi : une vague 2 de devoirs ne se justifie
pas sans nouvelle famille.

## 7. Plafond par auteur (au plus deux)

- **D04, D05 et D06 portent la même main** (même école, même enseignant, deuxième trimestre 2019/2020, registre `barhoumi-mounir` pour D04
  et D05, `ecole-primaire-brahmia` pour D06) : **trois devoirs, plafond dépassé**. À ne retenir que deux sur trois. Conseil du lecteur :
  **écarter D06** (production sans signature neuve, déjà couverte par les récits d'examen au chapitre 04) et garder D04 (trois signatures
  neuves : son/sont, correction d'erreurs, conjugaison avec repère) et D05 (trois signatures neuves : nature des mots, remise en ordre,
  titre).
- D01 (plateforme), D02, D03, D07, D08 : un seul devoir chacun. D03 et D08 partagent un gabarit national sans main commune démontrée.
- D09 : une seule fiche du registre, plusieurs épreuves d'un même millésime ; compte pour un.
- **Vague 2** : exclure la main de D04 à D06 ; les devoirs sans signature ne se comptent pas.

## 8. Difficultés

- **Rang des questions numérotées de façon irrégulière** (D09 : 1, 2, 4 puis 1, 2, 3, 2, 7 ; D05 : sixième sans numéro) : les n°exo suivent
  le rang d'ordre, pas la numérotation imprimée, comme dans les lots d'examens.
- **D09 composite** : un id pour plusieurs épreuves ; si le pilote veut isoler les épreuves, scinder en D09a (2ᵉ trimestre), D09b (production),
  D09c (3ᵉ trimestre). L'éveil scientifique n'a aucune ligne.
- **Thème de D09 n°4 à n°8** : texte dont le thème peut relever du 02 (communication par lettre, retenu) ou du 01 (travail) ; À trancher à l'étape G3 si une mission en est tirée.
- **Barème de D06** : les maxima par critère (3, 1,5, 1,5, 3, 1,5, 1) additionnés dépassent les 10 points annoncés ; la ligne reprend les 10 imprimés.
- **D04 n°2** : la clé dépend de l'interprétation du repère de temps (imparfait ou passé composé) ; aucun corrigé : à confirmer à l'écriture.
- **D01** : un petit nombre de filigranes de plateforme traversent le texte ; sans effet sur la lecture.
