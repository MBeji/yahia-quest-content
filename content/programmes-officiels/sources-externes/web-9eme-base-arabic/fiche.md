# Arabe 9ᵉ — fiche du couple `9eme-base × arabic` (étude 36, le gisement)

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

> **Ce que cette fiche est, et n'est pas.** Le registre du couple `arabic` dans le pipeline du
> gisement ([étude 36](../../../../FableEtudes/36-gisement-examens-devoirs/ETUDE.md)) : son
> échantillon, puis sa carte, son écart et ses mesures. Aucune phrase, aucun nombre, aucun
> contexte d'un devoir n'y entre. Elle n'est **pas** une référence de programme : le périmètre
> reste celui du manuel officiel.

## 1. Protocole

Le pipeline de l'étude 36, deux régimes : les **sujets d'examen national** sont du corpus
officiel (méthode R-2) — transcrits fidèlement sous `programmes-officiels/examens-nationaux/`,
chaque exercice devient une mission qui le reprend et le cite ; les **devoirs** sont lus en salle
blanche (T2′) — une ligne anonyme par exercice, et `prof-arabe-9eme` écrit une mission neuve par archétype
distinct sans jamais voir la source.

## 2. Échantillon — fixé le 2026-09-28, avant l'ouverture de tout document

- **examens** : toutes les sessions de l'archive du Ministère (`9web.edunet.tn`, épreuve
  « arabe »), filières générale et technique, et filière unique (2001-2008) — **38 sujets** (generale : 15, technique : 17, unique : 6),
  sessions 2002 à 2026 ; C37 (2004, unique), C40 (2001, unique) : introuvable(s) sur l'archive (404) ;
- **devoirs, vague 1** : un par créneau de `devoir.tn` (6 créneaux), le plus récent d'une
  année scolaire 2012-2013 ou postérieure, collège pilote et ordinaire en alternance quand le site
  en range, au plus deux devoirs par auteur ; une vague de plus tant que la précédente apporte
  ≥ 30 % d'archétypes neufs (étude 36, D-4).

| id | créneau | collège (selon le site) | année | site | auteur ou établissement (tel que le site le nomme) | SHA-256 (16 premiers caractères) |
| --- | --- | --- | --- | --- | --- | --- |
| D01 | DC1 | ordinaire | 2021-2022 | devoir.tn | الاستاذ-رمزي-حمدون | `9d78ed7a6c8fd016…` |
| D02 | DS1 | ordinaire | 2023-2024 | devoir.tn | Tadris.TN | `7f90811cce6a24be…` |
| D03 | DC2 | ordinaire | 2013-2014 | devoir.tn | — | `983461cad92ebff3…` |
| D04 | DS2 | ordinaire | 2016-2017 | devoir.tn | — | `10d78d6b6ce48cc3…` |
| D05 | DC3 | ordinaire | 2013-2014 | devoir.tn | — | `536ed53d69246095…` |
| D06 | DS3 | ordinaire | 2018-2019 | devoir.tn | — | `fefba33c8ca4ec80…` |

Liste machine des examens (sessions, fichiers officiels, empreintes) : [`gisement.json`](./gisement.json).
L'URL du fichier d'un devoir reste hors git (la fiche pointe la page de liste).

## 3. Carte et écart — les sujets d'examen 2020–2026 (lus le 2026-10-14)

Lu : les **12 sujets** de 2020 à 2026 (C01–C12, filières générale et technique), **118 lignes**,
tous en vision (scans). Les transcriptions fidèles sont versionnées sous
[`examens-nationaux/9eme-base/arabic/`](../../examens-nationaux/9eme-base/arabic/) ; les sessions
2002–2019 (C13–C40) et les devoirs D01–D06 restent à l'état `echantillon`, non lus. Tout ce qui
suit est dit dans nos mots, depuis les lignes des lecteurs : seules les consignes officielles sont
nommées, aucun devoir n'y entre.

### 3.1 L'architecture de l'épreuve

| filière, sessions | durée, coefficient | parties (barème) | texte support |
| --- | --- | --- | --- |
| générale, format actuel (2023–2026, 4 sujets) | 2 h, coef. 2 | **دراسة نصّ حجاجيّ** (10) = ❖ الفهم وبناء المعنى (4 questions, 4 pts) + ❖ الوعي بنظام اللّغة (6 questions à 1 pt, une leçon du manuel chacune, souvent en deux sous-items) ; **إنتاج نصّ حجاجيّ** (10, environ 25 lignes) | argumentatif (2023, 2025, 2026) ; narratif à visée argumentative (2024) |
| générale 2020 (format ancien) | 2 h, coef. 2 | « الإنشاء العربي » : un sujet unique de production (dialogue argumentatif), sans texte ni compréhension ni langue | — |
| technique (2020–2026, 7 sujets) | 1 h, coef. 1 | **الأسئلة** (14 : environ quatre questions de compréhension puis trois de langue) ; **تحرير فقرة** (6, environ 10 lignes) | narratif ou descriptif, jamais argumentatif |

La générale a la même ossature de 2023 à 2026 (la partie de langue s'intitule « اللّغة » en 2024).
La technique garde la sienne de 2020 à 2026, mais sa langue porte surtout sur des **acquis de
7ᵉ–8ᵉ** : sur 2023–2026, des 26,5 points de langue, 10 vont à des questions entièrement hors du
programme de 9ᵉ (`HP` : compléments absolu et de but, pluriels, accord et conjugaison avec les
pronoms, passif, prépositions) et 9 à des questions mêlées ; en 2020–2022, 8,5 points sur 17 sont `HP`.

### 3.2 Par chapitre du manuel

Une question qui mobilise deux chapitres compte dans chacun ; « questions » = questions notées
(lignes du lecteur).

| chapitre | générale 2023–26 | technique 2023–26 | technique 2020–22 | étage | ce qu'on y fait faire |
| --- | --- | --- | --- | --- | --- |
| `10` فهم وبناء معنى | 16 (4 sur 4 sujets) | 16 (4 sur 4) | 17 (3 sur 3) | d1–d2, d3 rare | synonyme **en contexte** (9 textes sur 11), thèse réfutée ou défendue, structure argumentative, indices (قرائن), titre ou thème (technique), **avis justifié** (11 sur 11) |
| `09` حجاج وإنتاج | 4 productions + 10 questions de compréhension argumentative | 4 paragraphes + 4 avis | 3 paragraphes + 3 avis | d3–d4 (production), d2 | réfuter, nuancer, blâmer et convaincre ; type d'argument et indicateur ; dialogue argumentatif (2020) |
| `16` الاستفهام | 5 (4 sur 4) | — | — | d2–d3 | réponse elliptique et **fonction de l'élément omis** ; interrogation négative et sa réponse (بلى) ; question sur un constituant ; interrogatif d'objet |
| `17` الشّرط | 5 (4 sur 4) | — | — | d2–d3 | introduire un outil jussif et **ajuster la phrase** ; outil **imposé par le sens** (possible, impossible, temps) ; لولا ; condition remise au présent |
| `05` معاني صيغ الزّيادة | 5 (3 sur 4) | — | 1 | d2–d3 | schème et sens de l'augmentation d'un verbe du texte ; produire une phrase à sens imposé (réciprocité, effort) ; mots de même sens qu'une forme |
| `18` دلالة الزّمان | 2 | — | 1 | d2 | nature et valeur temporelle d'une particule jointe au verbe ; futur probable ou certain lointain ; négation du futur |
| `15` العلاقات بين الجمل | 3 (2 sur 4) | — | — | d2–d3 | relever une **incise**, son type, les fonctions qu'elle sépare ; connecteurs de reprise ; connecteur de rectification |
| `12` المقصور والمنقوص والممدود | 3 (2 sur 4) | — | — | d2–d3 | duel et pluriel **vocalisés** de noms du texte ; nom mamdud dérivé d'un verbe |
| `13` التّصغير | 2 (2 sur 4) | — | — | d2 | diminutif d'un nom ou d'un adverbe de temps, schème, sens |
| `14` النّسبة والمصدر الصّناعيّ | 2 (2 sur 4) | — | — | d1–d3 | nom abstrait d'un adjectif ; même mot en nom de relation puis en nom abstrait |
| `19` العدد والمعدود | 1 (2025) | — | — | d3 | nombres composés **écrits en lettres**, accordés au dénombré |
| `02` النّواسخ | 1 (2024) | — | — | d3 | auxiliaire verbal remplacé par une particule, cas à ajuster |
| `04` الأساليب | — | — | 1 (2022) | d2 | formuler un ordre et une interdiction |
| `03` المفعول فيه والحال | — | 5 | 2 | d2 | fonction d'un groupe ; **enrichir** une phrase d'un état ou d'un complément de temps (toujours mêlé, dans la même consigne, à des compléments `HP`) |
| `06` المشتقّات (révision) | — | 3 | 1 | d2–d3 | tableau de dérivation vocalisé : participes actif et passif, nom d'action, de verbes simples et augmentés |
| `01` الإعراب والبناء (révision) | — | 3 | 1 | d3 | passer au duel et accorder (l'accord lui-même est `HP`) |
| `07`, `08` | — | — | — | — | jamais interrogés directement (un sens de phrase symbolique en 2024, lu comme compréhension) |

**Consignes officielles qui reviennent** : ايتِ بمرادف / صِلْ بالمرادف حسب السّياق ؛ صُغْ بعبارتك
الأطروحة ؛ حدّد نوع الحجّة ومعنى المؤشّر ؛ قسّم النّصّ وفق بنيته الحجاجيّة ؛ أَبْدِ رأيك وعلّله ؛
أجب إجابة مختزلة وعيّن وظيفة المحذوف ؛ أدخِلْ / اجعلْ … وغيّر ما يجب تغييره ؛ كوّن جملة شرطيّة ؛
أكمل تعمير الجدول (مشكولًا) ؛ صُغِ التّصغير ؛ اشتقّ … واستعمله في جملة ؛ أثْرِ / أغْنِ الجملة
بالمطلوب. Le geste dominant de la langue est **produire ou transformer sur le texte** (vocaliser,
ajuster l'accord, employer dans une phrase), non reconnaître.

**Pièges qui reviennent** (nos mots) : confondre la thèse avec la thèse adverse, un argument ou la conclusion (2023, 2025, 2026) ;
avis sans justification argumentée (les 11 textes) ; synonyme hors contexte (9) ; oublier le jussif ou le
subjonctif après l'outil (4) ; outil de condition contraire au sens demandé (3) ; mauvais traitement
de l'alif ou de la hamza finale (2) ; confondre sens de la forme augmentée et sens lexical (3) ;
complément de lieu pris pour un complément de temps (2025) ; inverser les voyelles des deux participes (2).

### 3.3 Écart avec le contenu existant (562 questions, toutes des QCM à réponse unique)

Recherche par archétype dans les questions des chapitres (`exercices/*.json`, état de `main` au
2026-10-14) :

| archétype d'examen | sujets | questions existantes du chapitre qui le travaillent |
| --- | --- | --- |
| synonyme **en contexte** d'un mot d'un texte (10) | 9 sur 11 | 4 sur 36, aucune sur un texte officiel |
| découper un texte selon sa structure argumentative (10) | 1 | 3, sans appariement ni mise en ordre |
| avis justifié (10) | 11 sur 11 | présent (le mot « رأي » dans 19 sur 36) |
| analyser la consigne d'une production, planifier le texte (09) | 12 sur 12 | **0** sur 29 |
| nuancer (تعديل) une position, par opposition à réfuter (09) | 1 | **0** |
| réponse elliptique et fonction de l'élément omis (16) | 2 | **0** au chapitre 16 (l'ellipse n'est traitée qu'au 15) |
| لولا et corrélation (17) | 1 | **0** (« لو » : 11) |
| écrire un nombre en lettres, accord du composé (19) | 1 | **0** de production ; la reconnaissance du composé est dense (19 sur 30) |
| duel et pluriel vocalisés de maqsur et mamdud (12) | 2 | présent (8 et 12 sur 30) |
| diminutif et sens de proximité d'un adverbe de temps (13) | 2 | présent (6) |
| particule et valeur temporelle (18) | 3 | « سوف » 2, « لن » 5 : mince |
| incise et fonctions qu'elle sépare (15) | 1 | 3 |
| enrichir une phrase d'un complément de temps (03) | 5 | 10 sur le complément de temps, mais aucune consigne d'enrichissement |
| tableau de dérivation avec le nom d'action (06) | 4 | 5 sur le nom d'action |
| appariement, mise en ordre, plusieurs réponses | consignes « صِلْ », « قسّم », « اختر ثلاث » | **0** : aucun type natif autre que le QCM dans toute la matière |

**Les trous réels** : (1) la **production** n'a aucune préparation sur une consigne d'examen —
les 29 questions du chapitre 09 travaillent la notion, jamais l'analyse d'un sujet ; (2) le
**synonyme en contexte** et l'**avis justifié**, présents dans presque chaque texte, ne sont jamais
travaillés sur un texte officiel ; (3) la **réponse elliptique** du chapitre 16 et l'**écriture des
nombres** du 19 ; (4) les consignes de **transformation** (« غيّر ما يجب تغييره ») se réduisent
partout à un choix entre phrases déjà écrites. **Pas des trous** : la reconnaissance des schèmes
(05 : 24 questions sur 30), du diminutif, du maqsur et du mamdud, du complément de temps et de
l'état, déjà travaillés à d2–d4 en quantité supérieure aux sujets.

### 3.4 Vague 2 — sessions 2002–2019 et devoirs D01–D06 (lus le 2026-10-18)

Lu : **26 sujets** de 2002 à 2019 (C13–C39 ; 2004 et 2001 introuvables, 2014 absente de l'archive), **108
lignes**, tous en vision ; transcriptions versionnées au même dossier, texte support résumé (intégral au PDF
officiel). Et les **six devoirs** de la vague 1 de devoirs (63 lignes, salle blanche : rien n'en est transcrit
ici). Le plan qui en sort : `FableEtudes/36-gisement-examens-devoirs/en-cours/arabe/PLAN-v2.md`.

**L'épreuve ancienne.** Générale 2009–2019 et épreuve unique 2002–2008 (16 sujets) : « الإنشاء العربي »
seul, 2 h, coefficient 2, une page, un sujet de production sans texte, compréhension ni langue, sans barème.
Quinze sujets sont des **dialogues argumentatifs** à transcrire ; le seizième (2002) fait décrire puis
argumenter. Technique 2009–2019 (10 sujets) : l'ossature de 2020 (questions 14 + « تحرير فقرة » 6), texte
narratif (expositif en 2011) ; sur 92 lignes, 66 de compréhension, 10 paragraphes, **14 entièrement `HP`**
(duel et accord, conjugaison avec les pronoms, pluriels, complément absolu, expressions) et 2 mêlées ; la
langue au programme se réduit à l'état (03, 2019) et à la défense (04, 2015) ; 2012, 2011, 2010 et 2009 n'ont
aucune question de langue.

**Les archétypes de production**, par consigne officielle :

| archétype | sessions | déjà posé par la vague 1 ? |
| --- | --- | --- |
| dialogue où seul le narrateur argumente (« مُرَكِّزًا عَلَى الحُجَجِ الَّتِي اعْتَمَدْتَهَا ») | 2019, 2017, 2016, 2015, 2012, 2010, 2009, 2003 | oui : la mission de 2020 (même consigne) |
| dialogue à deux voix : arguments de chacun (« كُلٌّ مِنْكُمَا »), les deux avis, ou ceux de l'autre partie | 2013, 2011, 2007, 2005 | **non** (le cours 09 l'enseigne, aucun sujet récent ne le pose) |
| modifier une position (« تَعْدِيلِ مَوْقِفِهِ »), parfois sous condition | 2018, 2008, 2006 ; paragraphe 2018 T | **non** en dialogue (2025 nuance dans un texte suivi) |
| décrire un comportement puis argumenter | 2002 | sans objet (hors du 09) |
| paragraphe : arguments **et** conseils, forme imposée (discours, lettre, demande) | 2017, 2016, 2012, 2011 T | **non** |
| paragraphe : persuader de la valeur d'une activité | 2019, 2015, 2013 T | oui (paragraphes techniques 2020–2026) |
| rapport, présentation d'un projet | 2010, 2009 T | sans objet (non argumentatif) |

**La compréhension technique** reprend les consignes de 2020–2026 (titre, synonymes ou contraires en contexte,
indices, cause, solutions, avis justifié). Gestes absents de la vague 1 : ordonner les étapes d'un procédé
(2015), répartir des traits entre deux groupes de personnages (2017), choisir un facteur et le justifier
(2017), cause principale et indice dans un texte expositif, critique d'une explication unique (2011).

**Les devoirs** (nos mots, aucune phrase ni aucun nombre des documents) : compréhension et production au même
format que la générale actuelle ; la langue porte surtout sur le 18 (10 lignes), le 03 (5), le 15, le 13 et le
14 (4 chacun) ; un seul devoir relève du programme révisé. Au regard des 226 lignes d'examen, **15 signatures
sur 60 sont neuves (25 %)** ; au regard des missions et du patron, **3 (5 %)** : le nom manqus en emploi et le
participe d'un verbe défectueux (une mission au 12), et une comparaison attachée au texte d'un devoir (écartée).
Sous 30 % : pas de vague 3 recommandée.

**Écart retenu** : trois archétypes de production (deux voix ; modification d'une position en dialogue ;
arguments et conseils dans une forme imposée), trois textes de compréhension (2015, 2017, 2011 T), le manqus
en emploi. **Écarté** : huit sujets généraux et 2002 entiers, sept textes techniques, deux paragraphes non
argumentatifs, tout `HP` (le duel du dossier 01 a déjà sa mission).

## 4. Plan — les sujets deviennent des missions

Plan écrit le 2026-10-14 (règles, lots, écarts : `FableEtudes/36-gisement-examens-devoirs/en-cours/arabe/PLAN.md`) :
**32 missions** à l'état `planifiee` dans [`gisement.json`](./gisement.json), en cinq lots —
11 de compréhension (une par texte, chapitre 10), 7 de production convertie (chapitre 09),
14 de langue (au chapitre de la notion, questions de plusieurs sessions regroupées). Treize
questions entièrement `HP` ne sont pas placées.

**Contrôle local de cette fiche** (`content:gisement:controle` contre les 12 transcriptions) :
0 plage de 8 mots, 0 de 6 mots ; les seules données communes sont des années et le « 256 » de SHA-256 (en-têtes), sans objet.

**Vague 2** (plan du 2026-10-18, `…/arabe/PLAN-v2.md`) : **7 missions** `planifiee` de plus — 3 de production
convertie (09), 3 de compréhension (10), 1 de devoirs en salle blanche (12) ; le reste des sessions 2002–2019
et des devoirs est écarté, raisons au plan (§ 5).

## 5. Mesures — à la lecture
