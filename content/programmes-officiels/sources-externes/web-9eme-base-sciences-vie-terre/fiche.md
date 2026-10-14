# SVT 9ᵉ — fiche du couple `9eme-base × sciences-vie-terre` (étude 36, le gisement)

```yaml
# en-tête de provenance — profil source-web (étude 27, D-2) ; carte qui croise plusieurs sites
url: plusieurs pages — voir les fiches de site web-devoir-tn et web-echoexam-edunet-tn
titulaire: plusieurs — voir les fiches de site
consulte_le: 2026-09-28
cgu: voir les fiches de site
robots: autorise (devoir.tn) ; absent (9web.edunet.tn)
autorisation: aucune
tier: T2-prime
snapshot: scratchpad de la session du 2026-09-28, hors git ; empreintes SHA-256 dans gisement.json
```

> **Ce que cette fiche est, et n'est pas.** Le registre du couple `sciences-vie-terre` dans le pipeline du
> gisement ([étude 36](../../../../FableEtudes/36-gisement-examens-devoirs/ETUDE.md)) : son
> échantillon, puis sa carte, son écart et ses mesures. Aucune phrase, aucun nombre, aucun
> contexte d'un devoir n'y entre. Elle n'est **pas** une référence de programme : le périmètre
> reste celui du manuel officiel.

## 1. Protocole

Le pipeline de l'étude 36, deux régimes : les **sujets d'examen national** sont du corpus
officiel (méthode R-2) — transcrits fidèlement sous `programmes-officiels/examens-nationaux/`,
chaque exercice devient une mission qui le reprend et le cite ; les **devoirs** sont lus en salle
blanche (T2′) — une ligne anonyme par exercice, et `prof-svt-9eme` écrit une mission neuve par archétype
distinct sans jamais voir la source.

## 2. Échantillon — fixé le 2026-09-28, avant l'ouverture de tout document

- **examens** : toutes les sessions de l'archive du Ministère (`9web.edunet.tn`, épreuve
  « svt »), filière générale et filière unique (2001-2008) — **23 sujets** (generale : 16, unique : 7),
  sessions 2001 à 2026 ; C21 (2004, unique), C25 (2032, generale) : introuvable(s) sur l'archive (404) ;
- **devoirs, vague 1** : un par créneau de `devoir.tn` (6 créneaux), le plus récent d'une
  année scolaire 2012-2013 ou postérieure, collège pilote et ordinaire en alternance quand le site
  en range, au plus deux devoirs par auteur ; une vague de plus tant que la précédente apporte
  ≥ 30 % d'archétypes neufs (étude 36, D-4).

| id | créneau | collège (selon le site) | année | site | auteur ou établissement (tel que le site le nomme) | SHA-256 (16 premiers caractères) |
| --- | --- | --- | --- | --- | --- | --- |
| D01 | DC1 | pilote | 2016-2017 | devoir.tn | chayeb-ahlem | `0fa324e69a84d9a9…` |
| D02 | DS1 | ordinaire | 2021-2022 | devoir.tn | mr-hajri-taoufik | `44cf41ea92f43c09…` |
| D03 | DC2 | ordinaire | 2020-2021 | devoir.tn | ecole-l-etoile | `84b6fdeae8beb046…` |
| D04 | DS2 | ordinaire | 2020-2021 | devoir.tn | l-etoile | `dad1b8079178f83f…` |
| D05 | DC3 | ordinaire | 2015-2016 | devoir.tn | mme-latifa-habchi | `c2237d7b1558f604…` |
| D06 | DS3 | ordinaire | 2022-2023 | devoir.tn | létoile | `b75459fef76b8290…` |

Liste machine des examens (sessions, fichiers officiels, empreintes) : [`gisement.json`](./gisement.json).
L'URL du fichier d'un devoir reste hors git (la fiche pointe la page de liste).

**État de la lecture (lue le 2026-09-29, versionnée le 2026-10-02).** Six sujets d'examen sont lus et
transcrits : les sessions 2026, 2025, 2024, 2022, 2021 et 2020 (`C01` à `C06`, tous au programme en
vigueur) — transcriptions sous `programmes-officiels/examens-nationaux/9eme-base/sciences-vie-terre/`,
et [`lignes.tsv`](./lignes.tsv) en tient une ligne anonyme par exercice (27 lignes ; la colonne des
chapitres y donne les slugs du manifeste). Les dix-sept autres sessions (`C07` à `C24`, de 2019 à
2001 : le programme en vigueur se vérifie d'abord) et les six devoirs restent à lire ; la carte, l'écart
et les mesures ci-dessous s'écrivent quand la lecture est complète.

**Mise à jour (2026-10-14).** Les sessions 2019 à 2001 sont lues et transcrites (`C07` à `C24`, sauf
`C21`, 2004, introuvable sur l'archive ; 2014 n'est pas dans l'échantillon) : 17 sujets, 72 exercices, dont 5 entièrement hors programme. Les six
devoirs restent à lire : la carte ci-dessous ne parle que des sujets officiels.

## 3. Carte et écart — vague 2 (2001–2019)

Écrit au planificateur du 2026-10-14 (étude 36, étapes G3 et G4). **Matière : les seuls sujets officiels**
de l'examen national (23 sessions disponibles, 2001 à 2026 ; 99 exercices). Aucun devoir, aucun corrigé,
aucun site tiers. Les chiffres « vague 1 » sont ceux des sessions `C01`–`C06` (2020–2026, 27 exercices,
tous placés, 27 missions sur `main`) ; « vague 2 » ceux de `C07`–`C24` (72 exercices, 67 placables).
Le plan qui en sort : `FableEtudes/36-gisement-examens-devoirs/en-cours/svt/plan-examens-v2.json` et
`PLAN-v2.md` (même dossier).

### 3.1 Architecture du sujet — les créneaux

- **Durée une heure, sur 20 points, coefficient 2** (1 en 2001). L'épreuve s'intitule « العلوم الطبيعية »
  de 2001 à 2008, « علوم الحياة والأرض » ensuite.
- **Première partie, 12 points = trois exercices de 4 points.** Le premier est presque toujours un
  **QCM de quatre items** (« عيّن الإجابة الصّحيحة ») ou, en 2005, 2013 et 2016, **huit phrases à
  compléter par un choix** : 15 sessions sur 17 en vague 2 (pas en 2007 ni en 2001), 6 sur 6 en vague 1. Ces items balaient
  trois à huit chapitres : c'est l'unique créneau qui touche les chapitres 04, 10, 13 et 14.
- **Seconde partie, 8 points** : un exercice long (2001–2003, 2005–2008, 2010, 2012, 2015, 2017–2020, 2022,
  2026) ou deux exercices (5 + 3 en 2009, 2011, 2016, 2024 ; 4 + 4 en 2013, 2025 ; 4,5 + 3,5 en 2021).
  C'est là que se trouvent les exercices d3–d4 : expériences de digestion, gaz et glucose du sang,
  effort musculaire, calendrier et cycle.
- **Génétique** : la seconde partie entière (8 points) en 2001, 2002, 2003, 2006 et 2008 ; hors du
  programme en vigueur (aucun des 14 chapitres du manifeste), donc non placée.

### 3.2 Fréquence par chapitre (2001–2026)

« Mobilisé » : nombre d'exercices qui font appel au chapitre ; « placé » : chapitre le plus avancé de
l'exercice, dans l'ordre du manifeste (un QCM multi-chapitres est compté une fois, à son chapitre le plus
avancé).

| chapitre | mobilisé v1 | mobilisé v2 | **total** | placé v1 | placé v2 | ce que les sujets font faire |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| 01 fonction de communication | 8 | 16 | **24** | 0 | 1 | sens de l'influx, neurone et ses parties, substances grise et blanche, coupes de tissu nerveux, nerfs |
| 02 actes réflexes | 4 | 7 | **11** | 2 | 3 | arc réflexe (légende, ordre, rôles, propriétés, intérêt) ; nerf sectionné et hypothèses (2021, 2024 seulement) |
| 03 vision | 6 | 13 | **19** | 5 | 5 | défauts de vision et lentilles ; trajet visuel ; œil et appareil photographique ; iris, rétine |
| 04 besoins alimentaires | 1 | 9 | **10** | 0 | 0 | toujours en appoint : énergie des nutriments, vitamines, test du calcium, carence |
| 05 digestion | 7 | 19 | **26** | 2 | 8 | tubes à essai (salive, suc gastrique, sucs intestinal et pancréatique), absorption (courbes, tableaux, anse ligaturée), villosité |
| 06 sang | 2 | 19 | **21** | 0 | 2 | frottis (2005, 2012), plasma, transport des gaz ; surtout en appoint de 07–09 |
| 07 circulation | 7 | 22 | **29** | 2 | 3 | cœur en coupe, valvules et phases, double circulation à légender, sens et couleur du sang |
| 08 respiration | 6 | 20 | **26** | 5 | 12 | alvéole et échanges, gaz du sang, modèle de la cloche, effort et énergie |
| 09 excrétion | 4 | 18 | **22** | 3 | 16 | plasma / urine primitive / urine définitive, néphron, liquides des vaisseaux rénaux, unités structurales |
| 10 maturité sexuelle | 4 | 5 | **9** | 1 | 1 | gamètes, lieux de formation et de maturation |
| 11 cycle sexuel | 5 | 11 | **16** | 3 | 6 | ovaire (structures, ordre), endomètre (phases, synchronie), calendrier et datation de l'ovulation |
| 12 formation de l'embryon | 4 | 8 | **12** | 4 | 6 | stades de l'œuf et lieux ; épaisseur utérine, absence de règles, grossesse ; courbes de température |
| 13 régulation des naissances | 0 | 3 | **3** | 0 | 3 | moyen qui empêche chaque événement (ovulation, fécondation, nidation) |
| 14 MST | 0 | 1 | **1** | 0 | 1 | agent du sida (un item de QCM, 2017) |

Lecture : 07, 05, 08, 01 et 09 sont les plus interrogés sur 26 ans ; 13 et 14 ne le sont presque pas. La
vague 2 place beaucoup en 08 et 09 parce que les grands exercices de seconde partie (circulation + gaz
+ rein, 2010 et 2015) et les QCM finissent par un item d'excrétion.

### 3.3 Étages

| | d1 | d2 | d3 | d4 |
| --- | ---: | ---: | ---: | ---: |
| vague 1 (27 exercices) | 0 | 13 | 9 | 5 |
| vague 2 (67 placables) | 7 | 49 | 7 | 4 |

Les sessions anciennes sont plus plates : surtout « légender, compléter, nommer » en première partie ;
le raisonnement (analyser, interpréter, émettre une hypothèse, rédiger) est en seconde partie. Un exercice
d'examen n'est jamais d1 dans le portail : une ligne d1 devient d2.

### 3.4 Archétypes et sessions (2001–2026)

| famille | sessions | remarque |
| --- | --- | --- |
| QCM / phrases à compléter multi-chapitres | 21 sessions | items à 0,5 ou 1 point, un fait chacun |
| arc réflexe : légende, ordre, rôles, propriétés, intérêt, sensation consciente | 2020, 2016, 2013, 2010, 2007 | le nerf sectionné et les hypothèses n'apparaissent qu'en 2021 et 2024 |
| coupes microscopiques de tissu nerveux, unité commune | 2022, 2018 | |
| défauts de vision, lentille correctrice | 2026, 2021, 2017, 2009 (+ items 2011) | |
| trajet visuel, centre, hypothèses de lésion | 2025, 2020, 2010 | |
| œil et appareil photographique, structure de l'œil | 2011, 2003 | |
| digestion expérimentale en tubes | 2022, 2019, 2017, 2011, 2009, 2007 | amidon (salive, suc gastrique), protides, sucre de malt ; six variantes d'un même montage |
| absorption : anse ligaturée, courbes intestin / veine, tableaux | 2022, 2019, 2017, 2016, 2011 | |
| tableau digestif, villosité, voies d'absorption | 2021, 2012, 2001 | |
| frottis sanguin | 2012, 2005 | |
| cœur : coupe, valvules, phases | 2020, 2015, 2011 (+ items 2019, 2012, 2008) | |
| double circulation à légender, sens, couleur ou gaz dominant | 2024, 2017, 2016, 2010, 2009, 2008, 2001 | la famille la plus répétée hors QCM |
| alvéole, structure pulmonaire, adaptations, hémoglobine | 2019, 2013, 2006, 2002 | |
| modèle de la cloche (mécanique ventilatoire) | 2018 | |
| gaz et glucose du sang selon l'organe | 2015, 2009 | mêmes valeurs de gaz dans les deux sessions |
| repos et effort ; énergie | 2026, 2020, 2010, 2005 | 2010 et 2005 : mêmes mesures |
| unités structurales et fonctionnelles (alvéole, néphron, neurone, villosité) | 2025, 2007, 2005, 2001 | |
| tableaux plasma / urine primitive / urine définitive | 2016, 2013, 2011, 2008 (+ items 2006, 2005) | mêmes valeurs d'une session à l'autre |
| courbes ou prélèvements le long du néphron ; liquides des vaisseaux rénaux | 2025, 2024, 2010 | |
| ovaire : structures, ordre, phases | 2022, 2010 | |
| endomètre : phases, synchronie avec l'ovaire | 2015, 2012, 2009 | |
| calendrier des règles, datation de l'ovulation, absence de règles | 2021, 2018, 2012 | |
| épaisseur de l'endomètre (tableau, courbe), grossesse | 2018, 2013 | |
| courbes de température | 2024 | |
| stades de l'œuf, lieux, trois événements et leur prévention | 2026, 2025, 2019, 2006, 2003 | |
| génétique mendélienne (hors programme) | 2008, 2006, 2003, 2002, 2001 | non placée |

**Combinaisons de chapitres** (hors QCM) : 06 + 07 + 08 (circulation et gaz : sept sessions) ; 06 + 07 + 08 +
09 (grands exercices de 2010 et 2015) ; 11 + 12 (2012, 2013, 2018, 2024, 2025) ; 01 + 02 (arc réflexe) ;
01 + 08 + 09 (unités, 2001 et 2005) ; 04 + 05 (protides et croissance, 2019) ; 04 + 07 + 08 (effort, 2005).

**Vocabulaire des consignes.** Première partie : « عيّن الإجابة الصّحيحة », « أتمم الفراغ … من الإجابات
المقترحة », « أكتب البيانات », « سمّ », « أتمم الجدول », « حدّد / جسّم بسهام », « لوّن », « اشطب العبارة
الخاطئة », « رتّب ». Seconde partie : « قارن », « حلّل », « فسّر », « استنتج », « علّل », « اقترح فرضيّة »
(2007, 2012, 2018), « اقترح تجربة » (2017), « أنجز رسما » (2017), « حرّر فقرة » (2005, 2007, 2012,
2017, 2018 ; avec mots imposés en 2005 et 2012).

**Hors programme et modernisation.** Hors programme : les cinq secondes parties de génétique, l'item du
nombre de chromosomes (2005, exercice 1, item 4). Terminologie d'époque à moderniser selon le manuel
actuel : « عين حسيرة / طامسة » (2009, 2011), « الإخصاب » pour « الإلقاح » (2008), « الأساخ الرّئويّة »
(2010), « الدّم المترسّب » (2002), « جرثومة » pour le virus du sida (2017), « كحول دهنيّة » pour le
glycérol (2012) ; sécrétion du néphron (urée, acide urique ou ammoniac selon les sessions ; le manuel
actuel : l'ammoniac) ; unités mixtes (2005) ; convention de couleur inversée du vaisseau pulmonaire
(2019) ; coquille « مثكلة » (2019). Clés ambiguës relevées à la lecture : 2002 (items 3 et 4), 2006
(items 1 et 2), 2008 (item 4), 2009 (items 2 et 3), 2010 (item 3), 2013 (item 6), 2017 (item 1), 2018
(items 2 et 3) — reformulées pour n'avoir qu'une réponse, ou écartées (détail au plan).

### 3.5 Écart avec le contenu existant

Croisement par **archétype** (la SVT n'a pas de registre fermé de compétences) avec les 14 chapitres
`content/sciences-vie-terre/01…14` : missions du patron (`01`–`06`), quiz du chapitre, et missions d'examen
de la vague 1 (`07`…). Règle : une mission de la vague 2 ne redemande pas ce qu'une de ces missions
demande déjà, et une famille posée par plusieurs sessions ne donne qu'une mission.

| famille | déjà couvert par | décision vague 2 |
| --- | --- | --- |
| QCM multi-chapitres | les quiz et le patron reprennent déjà la plupart des faits (iris, rétine-film, tuniques de l'œil, fécondation dans l'oviducte, dispositif intra-utérin, vitamine D, voie lymphatique des lipides, filtration des protides…) | QCM découpés item par item (72 items en vague 2) ; un item rejoint la mission de sa notion s'il apporte un fait ou une figure absents (16 items) ; un est hors programme ; les 55 autres sont écartés |
| coupes de tissu nerveux | 03/07 (2022), patron 01 | **01/07** : 2018 + quatre items de QCM (01 n'a aucune mission d'examen) |
| arc réflexe | patron 02 (ordre des cinq éléments ×3), 03/08 (2020) | **02/09** : propriétés, intérêt, sensation consciente, coupe de moelle (2013, 2007, 2016, 2019, 2010) — sans la légende ni l'ordre |
| défauts de vision | 03/09, 03/11, patron 03 | 2009 écarté (doublon de 2021) ; 2017 réduit à la lentille lue sur son profil |
| œil et appareil photo | patron 03 (une question) | **03/12** : 2003 + 2017 |
| trajet visuel | 03/08, 03/10, patron 03 | 2010 (paragraphe) écarté |
| digestion de l'amidon en tubes | patron 05, 05/08 (sucre de malt) | **05/10** : 2017 + 2009 + 2007 |
| protides, absorption, croissance | — | **05/09** : 2019 |
| anse ligaturée, rôles de l'intestin | 05/07, 05/08 | **05/11** : 2016 + 2011 + 2012 |
| frottis sanguin | patron 06, quiz 06 | 2005 versé dans 08/12 (lecture de figure) ; 2012 écarté |
| cœur, valvules, phases | 07/08 (2020), 08/08 (2024), patron 07 | **07/09** : coupe de cœur de mouton (2015) + tableau des trois phases (2011) + deux items |
| double circulation à légender | 07/08, 08/08, patron 07 | sept sessions, aucune mission propre : un item (2016) versé dans 08/12, le reste écarté |
| alvéole, hémoglobine | 08/07 (2025), patron 08 | **08/12** : 2019 + 2005 + 2006 + 2002 + 2010 + 2016 |
| modèle de la cloche | patron 08 (sans le modèle) | **08/13** : 2018 + un item |
| effort | 08/10 (2026), 08/11 (2020) | **08/14** : 2005 (fréquence cardiaque, débit, rythme respiratoire) ; 2010 (mêmes mesures) écarté |
| gaz et glucose selon l'organe | patron 08 (consommation d'O₂) | **09/10** : 2015 entier ; 2009 écarté (mêmes valeurs) |
| tableaux du néphron | patron 09 (02-tamrin a les valeurs de 2011), quiz 09, 09/09 | quatre sessions sans mission propre ; **09/11** garde les liquides des vaisseaux rénaux (2010), les fonctions par substance (2008) et trois items |
| unités structurales | 08/07 (deux structures), 09/09, patron 01 | **09/12** : synthèse 2005 + 2007 + 2001 |
| ovaire, ordre des structures | 11/08 (2022) | 2010 écarté |
| endomètre et synchronie | patron 11 (faits) | **11/10** : 2015 + 2009 + deux items |
| calendrier, épaisseur, grossesse | 11/09 (2021), 12/10 (2024) | **12/11** : 2018 + 2013 ; 2012 écarté (ses parties sont dans 11/10, 12/11, 13/07) |
| stades de l'œuf, trois événements, prévention | 12/07, 12/09, patron 12 et 13 | **13/07** : 2003 + 2006 + 2019 (la seule mission d'examen du 13) |
| frottis, organes et fonctions (2007), sida (2017) | patron 06, 10, 14 | écartés |

**Ce qui reste sans mission d'examen après la vague 2** : 04, 06, 10 et 14. Leur matière d'examen est faite
d'items de QCM que le patron et les quiz posent déjà, ou d'exercices placés plus loin (06 dans 08 et 09).
Ce n'est pas un trou : le patron de ces chapitres couvre les mêmes faits.

## 4. Mesures — à la livraison
