# Gisement 9ᵉ × SVT : plan des missions d'examen, vague 2 (G3–G4, étude 36)

Écrit le 2026-10-14 par le planificateur. Périmètre : les sessions anciennes `C07`–`C24` (2019 à 2001,
sans 2004, introuvable, ni 2014, hors échantillon), soit **17 sujets et 72 exercices**. La synthèse de
lecture dit « 18 sessions » : il y en a 17 (2001–2003, 2005–2013, 2015–2019).

**Entrées.** Transcriptions `content/programmes-officiels/examens-nationaux/9eme-base/sciences-vie-terre/`,
lignes et méta `lecture-9eme/svt/lines/`, les trois journaux de lecture, `SYNTHESE-C07-C24.md`, le contenu
`content/sciences-vie-terre/` (identique à `origin/main` : patron `01`–`06`, quiz, 27 missions d'examen de
la vague 1), le plan de la vague 1 (`plan-examens-v1.json`) et le plan arabe (règle du découpage par question).

**Sorties.**

- carte et écart : `…/web-9eme-base-sciences-vie-terre/fiche.md` § 3 (sujets officiels seulement ; contrôle local
  `content:gisement:controle` contre les 18 transcriptions de la session : 0 plage de 8 mots, 0 donnée reprise ;
  ce rapport aussi) ;
- plan : [`plan-examens-v2.json`](./plan-examens-v2.json) : 16 missions (`m028`–`m043`), 3 lots, et le
  sort de chaque exercice et de chaque item écarté (`ecartes`, `itemsEcartes`, `horsProgramme`) ;
- registre : `…/web-9eme-base-sciences-vie-terre/gisement.json` : 16 missions `planifiee` (id = la source de
  base, comme les 27 de la vague 1 ; `sources` liste toutes les sources fusionnées ; `note` donne l'id du plan) ;
- affectations : [`assign-svt-L11.md`](./assign-svt-L11.md), [`assign-svt-L12.md`](./assign-svt-L12.md),
  [`assign-svt-L13.md`](./assign-svt-L13.md).

## 1. Règles retenues

**R1 : l'unité reste l'exercice officiel.** Un exercice long (seconde partie, d3–d4) qui n'a pas de jumeau
donne sa mission entière : 2019 ex. 4, 2015 ex. 4, 2005 ex. 4.

**R2 : une famille posée par plusieurs sessions donne une seule mission.** Les familles de la synthèse
(§ 4) sont traitées comme telles : la session la plus riche sert de **base** (la mission en garde l'ordre),
les autres n'apportent que leurs questions **neuves** (autre donnée, autre figure, autre raisonnement).
Chaque question dit sa session (« مناظرة 2013 ») et garde les données de sa session. Le titre devient
« 🏛️ مناظرات <années> · <sujet> ».

**R3 : un QCM se découpe item par item.** Un QCM de quatre ou huit items balaie trois à huit chapitres ; le
placer entier à son chapitre le plus avancé enverrait un item de vision au chapitre de l'excrétion (c'est ce
qu'a fait la vague 1). Chaque item va donc au chapitre de sa notion, et il **rejoint la mission de ce
chapitre** s'il apporte un fait ou une figure que le chapitre ne pose pas encore. Sur 72 items, 16 sont
gardés, 1 est hors programme, 55 sont écartés : le patron et les quiz posent déjà presque tous ces faits
(la plupart des quiz ont d'ailleurs été écrits d'après ces annales). Une mission peut s'appuyer sur un
chapitre antérieur au sien : un item du 04 peut rejoindre une mission du 05 (`m034`).

**R4 : rien de ce que le patron, les quiz ou la vague 1 demandent déjà.** Le croisement est fait question
par question contre les 84 missions du patron, les 14 quiz et les 27 missions d'examen ; chaque note du
plan nomme les questions existantes à ne pas redemander (« 05/08 Q6–Q7 », « patron 01-tamrin Q2 »…).

**R5 : taille 6 à 12 questions.** Une consigne ouverte (« légender », « compléter », « rédiger ») devient une
ou plusieurs questions fermées, comme en vague 1. Une mission qui n'atteint pas 6 questions neuves n'existe
pas : ses questions vont dans une mission voisine ou sont écartées (frottis 2012, organes et fonctions
2007).

**R6 : hors programme.** Les cinq secondes parties de génétique (2001, 2002, 2003, 2006, 2008) ne sont pas
placées ; l'item du nombre de chromosomes (2005, ex. 1, item 4) est écarté. Les « globules polaires » des
dessins de 2006 ex. 3 sont définis dans l'énoncé (comme en 11/09 et 12/07) et aucune question ne porte sur
eux. Les deux fonctions des gonades (2007 ex. 2) et le rachitisme (2006) sont au programme (cours 10 et 04) :
écartés comme doublons, pas comme HP.

**R7 : modernisation et clés ambiguës.** Une terminologie d'époque se remplace par celle du manuel actuel ;
la mission le dit dans l'énoncé de la question concernée (« بلغة الكتاب المدرسيّ الحاليّ : … ») et l'auteur le
reporte dans son rapport. Une clé ambiguë se reformule pour n'avoir qu'une réponse, sinon l'item est écarté.
Les cas du plan : « الأساخ » → « الأسناخ » (2010), « كحول دهنيّة » → « غليسيرول » (2012), « مثكلة » → « المعثكليّة »
(2019), couleurs de l'artère pulmonaire inversées sur la figure de 2019 (redessinée), unités mixtes de 2005
(normalisées), propositions imprécises de 2002 ex. 1 item 1 (réécrites), lexique de 2010 ex. 2 (choix
réécrits). Les autres clés ambiguës de la synthèse tombent avec leurs items (§ 4).

**R8 : étage.** Celui de la ligne la plus haute de la mission, jamais d1 (d1 → d2). Bilan : 9 d2, 4 d3
(`m034`, `m035`, `m040`, `m042`), 3 d4 (`m033`, `m037`, `m041`).

## 2. Missions par chapitre

| chapitre | NN | mission | sources (base en premier) | étage | questions |
| --- | --- | --- | --- | --- | ---: |
| `01-wadhifat-al-ittisal` | 07 | m028 coupes de tissu nerveux, neurone | 2018 ex. 3 ; items 2019-1, 2016-5, 2013-4, 2002-1 | d2 | 9 |
| `02-al-af3al-al-in3ikasiya` | 09 | m029 propriétés et intérêt du réflexe, sensation consciente | 2013 ex. 2 (q3–q4) ; 2007 ex. 3 ; 2016 ex. 3 (q2) ; item 2019-2 ; 2010 ex. 2 (1ᵉʳ paragraphe) | d2 | 9 |
| `03-al-ibsar` | 12 | m030 œil et appareil photographique, lentille divergente | 2003 ex. 3 ; 2017 ex. 2 (q1 et une ligne) | d2 | 7 |
| `05-al-hadm` | 09 | m033 protides : digestion, absorption, croissance | 2019 ex. 4 | d4 | 8 |
| `05-al-hadm` | 10 | m034 le devenir de l'amidon | 2017 ex. 4 ; 2009 ex. 4 ; 2007 ex. 4 (q3) ; item 2015-3 | d3 | 10 |
| `05-al-hadm` | 11 | m035 les deux rôles de l'intestin grêle | 2016 ex. 4 ; 2011 ex. 4 (q1, q4) ; 2012 ex. 2 (q1–q2) ; item 2012-1 | d3 | 9 |
| `07-ad-dawaran` | 09 | m031 cœur de mouton, valvules, trois phases | 2011 ex. 3 ; 2015 ex. 2 (q1–q2) ; items 2008-3, 2012-2 | d2 | 8 |
| `08-at-tanaffus` | 12 | m038 de l'alvéole à l'hématie | 2019 ex. 3 ; 2005 ex. 3 ; 2006 ex. 2 (q3) ; 2002 ex. 3 (q2) ; 2016 ex. 2 (q1) ; item 2010-3 | d2 | 10 |
| `08-at-tanaffus` | 13 | m039 modèle de la cloche | 2018 ex. 2 ; item 2016-7 | d2 | 6 |
| `08-at-tanaffus` | 14 | m040 muscle, cœur et respiration à l'effort | 2005 ex. 4 | d3 | 7 |
| `09-al-ikhraj` | 10 | m041 gaz et glucose à l'entrée et à la sortie des organes | 2015 ex. 4 | d4 | 8 |
| `09-al-ikhraj` | 11 | m042 liquides du rein, fonctions du néphron | 2010 ex. 4 (q1, q3) ; 2008 ex. 3 (q2) ; items 2019-4, 2012-4, 2013-7 | d3 | 9 |
| `09-al-ikhraj` | 12 | m043 unités structurales et fonctionnelles | 2005 ex. 2 ; 2007 ex. 1 ; 2001 ex. 3 | d2 | 7 |
| `11-ad-dawra-al-jinsiya` | 10 | m036 endomètre et synchronie | 2015 ex. 3 ; 2009 ex. 3 (q1–q2) ; items 2017-2, 2009-4 | d2 | 7 |
| `12-takawwun-al-janin` | 11 | m037 calendrier, ovaire, épaisseur, grossesse | 2018 ex. 4 ; 2013 ex. 5 (q2–q3) | d4 | 11 |
| `13-tandhim-al-wiladat` | 07 | m032 trois événements, stades de l'œuf, prévention | 2003 ex. 2 ; 2006 ex. 3 (q1, q4) ; 2019 ex. 2 (q1–q3) | d2 | 8 |
| `04`, `06`, `10`, `14` | — | aucune | voir § 4 | | |

**16 missions, environ 133 questions**, tirées de 36 des 52 exercices placables hors QCM et de 16 items de
QCM. Chapitre 09 (16 placables) : trois missions seulement, une par variante réelle — les gaz et le glucose
de trois organes (2015, le seul exercice où le rein, l'intestin et le muscle se comparent), l'identification
des liquides des vaisseaux rénaux (2010, le seul où l'on raisonne sur le sang qui entre et sort du rein) et
la synthèse des unités (2001, 2005, 2007). Les quatre tableaux plasma / urine primitive / urine définitive
(2008, 2011, 2013, 2016) répètent des valeurs que le patron 09/02-tamrin, le quiz et 09/09 posent déjà : ils
ne donnent que la fonction par substance (2008) et trois items.

## 3. Lots

| lot | chapitres (NN) | missions | parallélisme |
| --- | --- | --- | --- |
| L11 | `01` (07), `02` (09), `03` (12), `07` (09), `13` (07) | m028–m032 (5) | avec L12 et L13 |
| L12 | `05` (09–11), `11` (10), `12` (11) | m033–m037 (5) | avec L11 et L13 |
| L13 | `08` (12–14), `09` (10–12) | m038–m043 (6) | avec L11 et L12 |

Chapitres disjoints : trois auteurs en parallèle. Skill : `prof-svt-9eme` puis `content-ecole-tn` ;
consigne : `gisement-auteur-examen.md` (reprise citée). `chapter.json` : la ligne `sources[]` des sujets
officiels manque encore à `01` et `13` (les autres chapitres l'ont depuis la vague 1).

**Pour les prompts d'auteur** (repartir de `plan/prompt-svt-L05.md`, en changeant trois points) :

1. Supprimer « Chaque exercice officiel donne sa propre mission, même s'il ressemble à un autre » : en
   vague 2, la ligne d'affectation dit ce qui est fusionné et ce qui est écarté (« consigne de tri »).
   L'auteur lit les questions désignées, pas l'exercice entier quand la ligne le restreint.
2. Mission fusionnée : chaque question nomme sa session (« مناظرة 2013 ») et redonne ses données ; la
   mission suit l'ordre de la session de base ; titre « 🏛️ مناظرات … · … » suivi des étoiles de l'étage.
3. Ajouter la règle R4 (liste « ne pas redemander » de chaque ligne, à vérifier sur `origin/main`) et la
   règle R7 (modernisation dite dans l'énoncé et dans le rapport).

Le reste du prompt de la vague 1 vaut tel quel : figures refaites d'après le PDF, plans 2×2, étiquettes
`bio.*` lues sur `origin/main`, tableaux une rangée par ligne, aucune lettre latine comme repère dans une
question à options, gates `content:gates -- --tranche`.

## 4. Ce qui est écarté, et pourquoi

Le détail machine (source par source, item par item) est dans `plan-examens-v2.json`
(`horsProgramme`, `ecartes`, `itemsEcartes`).

| écarté | quoi | pourquoi |
| --- | --- | --- |
| hors programme | 2008, 2006, 2003, 2002, 2001 ex. 4 (génétique, 8 points chacun) ; 2005 ex. 1 item 4 (chromosomes) | hors des 14 chapitres du manifeste |
| double circulation à légender | 2017 ex. 3, 2013 ex. 3, 2008 ex. 2, 2001 ex. 1 ; et les parties de 2016 ex. 2, 2009 ex. 5, 2006 ex. 2, 2002 ex. 3 non reprises dans m038 | sept sessions posent le même geste (légender, flécher, colorer) que 07/08 (2020), 08/08 (2024) et patron 07/03-boss |
| gaz du sang 2009 ex. 5 | deux échantillons de sang d'un organe | mêmes valeurs que 2015 ex. 4 (m041) |
| tableaux du néphron | 2016 ex. 5, 2013 ex. 4, 2011 ex. 5, 2002 ex. 2 ; 2008 ex. 3 q1 | mêmes valeurs que patron 09/02-tamrin et le quiz 09 ; présence / absence : 09/09 Q4 |
| vision | 2009 ex. 2 (deux yeux, défauts, correction) ; 2011 ex. 2 (légende de l'œil, iris) ; 2010 ex. 2 (voie visuelle) | 03/11 (2021) ; patron 03/01-tamrin et quiz 03 ; 03/08 et patron 03/04-defi |
| frottis 2012 ex. 3 | coloration, cellules, rôles, plasma | doublon de 2005 ex. 3 (versé dans m038) ; plasma : patron 06/03-boss Q6 |
| ovaire 2010 ex. 3 | structures, phases, ordre | 11/08 (2022) |
| 2012 ex. 4 (8 points) | coupes utérines, calendrier, hypothèses, trajet de l'œuf | ses trois parties sont dans m036, m037 (avec 11/09) et m032 (avec 12/07) |
| organes et fonctions 2007 ex. 2 | gonades, nerf optique, nerf sciatique, cœur | patron 10/01-tamrin Q5, 01/02-tamrin Q4–Q5 |
| villosité 2001 ex. 2 | légende, nutriments, voies | 05/07 (2021), patron 05/04-defi, quiz 05 Q9 |
| repos / effort 2010 ex. 4 q4 | fréquence cardiaque, oxygène et glucose consommés | mêmes mesures que 2005 ex. 4 (m040) |
| 55 items de QCM | voir `itemsEcartes` | 3 répètent un item gardé (2016 n°3, 2010 n°2, 2005 n°8) ; 51 redemandent un fait que le patron, un quiz ou la vague 1 posent déjà — 12 d'entre eux ont en outre une clé ambiguë, un énoncé flou ou un terme d'époque (2018 n°2, 2017 n°1 et n°4, 2013 n°6, 2011 n°2, 2009 n°2 et n°3, 2008 n°4, 2006 n°1 et n°2, 2002 n°3 et n°4) ; 1 n'a que sa clé ambiguë pour motif (2018 n°3, « tubes urinaires ») |

**Sans mission d'examen après la vague 2 : 04, 06, 10, 14.** Leur matière d'examen est faite d'items de QCM
déjà posés par le patron et les quiz (vitamines, rachitisme, aliments énergétiques ; plaquettes, plasma ;
maturation dans l'épididyme, acrosome ; sida) ou d'exercices placés plus loin (le frottis de 2005 est dans
m038). Ce n'est pas un trou de couverture.

## 5. Points de la lecture corrigés au plan

- **« حسيرة » et « طامسة ».** La synthèse les donne pour « hypermétrope et myope » ; l'item 2 de 2011 ex. 1
  n'a une seule clé (l'image en avant de la rétine) que si « حسيرة » désigne l'œil **myope**, et le quiz 03
  (Q7) appelle « طامس » le **hypermétrope**. Sans effet sur le plan (ces items et 2009 ex. 2 sont écartés),
  mais à corriger dans la synthèse si elle resservait. Les missions n'emploient que « قصر البصر » et « طول البصر ».
- **Placement de 2007 ex. 2** : le lecteur l'a placé au 11 ; ses notions (fonctions des gonades) sont du 10.
  Sans effet (écarté).
- **`lignes.tsv` du registre** n'a encore que les 27 lignes de la vague 1 : les 72 lignes de `lecture-9eme/svt/lines/C07…C24.tsv`
  restent à y concaténer (étape G2, à faire avant la livraison du premier lot).

## 6. Arbitrages pour le propriétaire

Aucun ne bloque l'écriture ; les trois choix les plus engageants sont réversibles lot par lot.

1. **Fusionner les sessions qui se répètent (R2) plutôt qu'une mission par exercice comme en vague 1.**
   Une mission par exercice aurait donné 52 missions, dont une trentaine de quasi-gabarits (sept
   circulations à légender, quatre tableaux du néphron, cinq tubes de digestion). La fusion en donne 16.
2. **Découper les QCM et en écarter 55 items sur 72 (R3–R4).** L'alternative serait un « QCM d'annales »
   par axe du programme (communication, nutrition, reproduction), qui reposerait des faits déjà posés : je
   ne la propose pas.
3. **Trois missions sont les plus discutables au regard de « la profondeur avant le volume »** : m043
   (unités structurales, proche de 08/07 et 09/09), m032 (événements de la reproduction, proche de 12/09 et
   du patron 13) et m031 (valvules, proche de 07/08). Elles apportent chacune un geste que l'existant n'a
   pas (synthèse à trois systèmes, appariement événement ↔ moyen de prévention, coupe de cœur de mouton) ;
   si le propriétaire préfère les retirer, L11 passe à 3 missions et L13 à 5, sans toucher aux autres.
