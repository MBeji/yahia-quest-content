# Anglais 9ᵉ — fiche du couple `9eme-base × english` (étude 36, le gisement)

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

> **Ce que cette fiche est, et n'est pas.** Le registre du couple `english` dans le pipeline du
> gisement ([étude 36](../../../../FableEtudes/36-gisement-examens-devoirs/ETUDE.md)) : son
> échantillon, puis sa carte, son écart et ses mesures. Aucune phrase, aucun nombre, aucun
> contexte d'un devoir n'y entre. Elle n'est **pas** une référence de programme : le périmètre
> reste celui du manuel officiel.

## 1. Protocole

Le pipeline de l'étude 36, deux régimes : les **sujets d'examen national** sont du corpus
officiel (méthode R-2) — transcrits fidèlement sous `programmes-officiels/examens-nationaux/`,
chaque exercice devient une mission qui le reprend et le cite ; les **devoirs** sont lus en salle
blanche (T2′) — une ligne anonyme par exercice, et `prof-anglais-9eme` écrit une mission neuve par archétype
distinct sans jamais voir la source.

## 2. Échantillon — fixé le 2026-09-28, avant l'ouverture de tout document

- **examens** : toutes les sessions de l'archive du Ministère (`9web.edunet.tn`, épreuve
  « anglais »), filières générale et technique, et filière unique (2001-2008) — **41 sujets** (generale : 17, technique : 17, unique : 7),
  sessions 2001 à 2026 ; C39 (2004, unique) : introuvable(s) sur l'archive (404) ;
- **devoirs, vague 1** : un par créneau de `devoir.tn` (6 créneaux), le plus récent d'une
  année scolaire 2012-2013 ou postérieure, collège pilote et ordinaire en alternance quand le site
  en range, au plus deux devoirs par auteur ; une vague de plus tant que la précédente apporte
  ≥ 30 % d'archétypes neufs (étude 36, D-4).

| id | créneau | collège (selon le site) | année | site | auteur ou établissement (tel que le site le nomme) | SHA-256 (16 premiers caractères) |
| --- | --- | --- | --- | --- | --- | --- |
| D01 | DC1 | ordinaire | 2019-2020 | devoir.tn | mme-sarah-baatour | `1dfb73041fe47f0a…` |
| D02 | DS1 | ordinaire | 2023-2024 | devoir.tn | Tadris.TN | `673debaa23e7d1b8…` |
| D03 | DC2 | ordinaire | 2019-2020 | devoir.tn | mme-nadia-belghith-abid | `1680cba9d58d4395…` |
| D04 | DS2 | ordinaire | 2018-2019 | devoir.tn | mr-bechir-fraoua | `7a288af5582bc86b…` |
| D05 | DC3 | ordinaire | 2018-2019 | devoir.tn | mr-bechir-fraoua | `58dad30618ab5320…` |
| D06 | DS3 | ordinaire | 2012-2013 | devoir.tn | galbi-maweheb | `9bf659ecf8f41b8a…` |

Liste machine des examens (sessions, fichiers officiels, empreintes) : [`gisement.json`](./gisement.json).
L'URL du fichier d'un devoir reste hors git (la fiche pointe la page de liste).

## 3. Carte et écart — examens 2001–2026

Écrit au planificateur du 2026-10-16 (étude 36, étapes G3 et G4). **Matière : les seuls sujets officiels**
de l'examen national : 41 sujets lus (`C01`–`C42`, sans `C39` : 2004, introuvable ; 2014 n'est pas dans
l'archive), 205 lignes (41 compréhensions, 123 exercices de langue, 41 productions), et, pour la langue, chaque
blanc relu un à un dans les transcriptions. Aucun devoir, aucun corrigé de tiers, aucun site tiers dans cette
section. « Format actuel » = 2021–2026 (12 sujets) ; « formats anciens » = 2001–2020 (29 sujets). Le plan qui en
sort : `FableEtudes/36-gisement-examens-devoirs/en-cours/anglais/plan-examens-v1.json` et `PLAN.md` (même dossier).

### 3.1 Architecture de l'épreuve — les créneaux

- **Trois parties sur 20, toujours dans le même ordre**, une heure : compréhension d'un texte d'une page
  (presse ou site, 150 à 300 mots, trois à cinq paragraphes), langue en **trois exercices exactement**,
  production écrite.
- **Générale** : 6 + 8 + 6 ; **technique** : 8 + 7 + 5 ; **épreuve unique** 2001–2008 : 7 + 8 + 5. Les
  barèmes de langue sont en demi-points (2.5 gardé).
- **Compréhension** : cinq questions presque toujours dans le même ordre — idée générale ou titre (QCM à trois
  options), vrai/faux sur deux énoncés avec renvoi de paragraphe, synonyme ou sens d'une expression, référent
  d'un mot souligné, puis, en générale, une réponse personnelle justifiée (cadre imprimé « If I were… » en
  2026, 2025, 2022, 2020, 2016) et, en technique, un tableau, des mots à relever ou la valeur d'un modal.
- **Langue** : trois gabarits seulement — texte lacunaire à banque (deux mots en trop), texte à options
  entourées, appariement de débuts et de fins de phrases (une partie en trop) ; deux variantes rares : mots
  entre parenthèses à mettre à la forme (2025 G, 2022 G) et formes de dialogue ou d'interview (2002, 2001).
- **Production** : huit à douze lignes (article, post, message, lettre, courriel, dépliant), consigne
  d'anonymat ; mots d'aide imprimés de 2005 à 2015 ; grille de notation imprimée en 2021–2022 seulement.

### 3.2 Fréquence par chapitre (exercices de langue, 123 lignes)

Une ligne mobilise souvent plusieurs chapitres (un texte lacunaire mêle les notions) ; elle compte pour chacun.
Le compte « items » est fait blanc par blanc dans les transcriptions.

| chapitre (slug) | format actuel (2021–2026) | formats anciens (2001–2020) | **lignes** | items au programme | ce que les sujets font faire |
| --- | ---: | ---: | ---: | ---: | --- |
| 01 present tenses | 0 | 9 | **9** | 12 | accord du présent simple, continu avec un repère, auxiliaire oublié |
| 02 past tenses | 12 | 24 | **36** | 35 | prétérit d'un récit (irréguliers, found / founded), past progressive, present perfect avec for / since / ever since |
| 03 future | 0 | 2 | **2** | 2 | will de prédiction ou d'espoir |
| 04 modals | 2 | 7 | **9** | 11 | modal + base, possibilité, capacité ; valeur d'un modal en compréhension |
| 05 conditionals | 1 | 1 | **2** | 2 | if en lacune, will du résultat |
| 06 « passive voice » | 1 | 1 | **2** | 0 | trois passifs, hors programme (voir la note) |
| 07 « reported speech » | 0 | 0 | **0** | 0 | jamais |
| 08 relatives & comparatives | 12 | 15 | **27** | 32 | who / which / that selon l'antécédent ; comparatif ou superlatif selon l'indice ; formes -er / -est / more / as … as |
| 09 reading & writing | 32 | 87 | **119** | — | vocabulaire en contexte, prépositions, connecteurs, appariements |

**Hors chapitres** (jetons `HP:` des lecteurs, harmonisés) : dérivation (classe de mot tirée d'une racine)
dans 15 sessions, dont cinq des six derniers sujets ; gérondif et forme verbale après un verbe ou une
préposition dans 12 ; pronoms (compléments, réfléchis, possessifs) dans 13 ; passif dans 3 ; fonction de
communication dans 1. Aucune ligne n'est entièrement hors chapitres.

**Note sur les slugs 06 et 07.** Le manifeste nomme `06-passive-voice` « Passive voice » et
`07-reported-speech` « Reported speech » ; le contenu publié de ces deux chapitres est autre :
« Communicative Functions » (06) et « Word Building & Linking Words » (07 : mots interrogatifs, possessifs,
réfléchis, adjectifs et noms composés, gérondif, connecteurs). Le manuel de 9ᵉ n'enseigne ni le passif ni le
discours rapporté. Conséquence pour la carte : le gérondif, les réfléchis et les possessifs, jetés `HP:` par
les lecteurs, sont enseignés au 07 publié (et au manuel, SB p. 33, 38 et 97) ; les trois passifs rangés au 06
sont, eux, hors programme.

### 3.3 Archétypes et étages

- **Langue** : 9 lignes d1, 112 d2, 2 d3. Un même blanc teste tour à tour un temps, un degré, un relatif,
  une préposition ou un mot du domaine : les familles se lisent **item par item**, non par exercice.
- **Compréhension** : 17 d1 (technique, repérage seul), 24 d2 ; toujours le même geste, justifier par le
  texte.
- **Production** : 17 d3 (générale), 24 d2 ; quatre archétypes : conseiller, mettre en garde ou fixer des
  règles (23 sujets) ; décrire, persuader ou donner un avis (une dizaine) ; lettre ou courriel à un
  correspondant (une dizaine, cadres « Dear … » / « Yours, » imprimés) ; récit au passé (2 sujets).
- **Vocabulaire des consignes** : « fill in » (banque), « circle » (options), « match » (appariement), « put … in
  the right tense or form » (mots entre parenthèses), « tick », « pick out », « refers to » ; en générale, la
  dernière question de compréhension demande une réponse personnelle justifiée.

### 3.4 Écart avec le contenu existant

Contenu croisé : `content/english/` (10 chapitres au patron, publiés ; quatre exercices de six questions et un
quiz par chapitre, trois sujets types au 10). **Aucune question existante ne reprend une phrase d'un sujet
officiel**, et toutes sont des QCM : ni appariement, ni texte lacunaire à banque, ni préparation de production,
ni formule de lettre. Croisement par famille (le détail question par question est dans la liste « ne pas
redemander » de chaque mission du plan) :

| famille (chapitre) | sessions | déjà posé par le patron ou le quiz | ce que l'existant ne pose pas |
| --- | ---: | --- | --- |
| présent simple ou continu (01) | 10 | -s, do / does, at the moment, usually, verbes d'état | sujet éloigné du verbe, auxiliaire oublié dans un texte suivi |
| present perfect ou prétérit (02) | 12 | just, already, lately, ever, ago, since + année | for / since / ever since dans un texte, participe d'un irrégulier en banque |
| récit au passé (02) | 12 | prétérit régulier ou irrégulier, past progressive | found / founded, forme à produire entre parenthèses, verbes d'un récit suivi |
| will et if (03, 05) | 4 | if + présent, will + base, ordre des propositions | will d'espoir, must pris pour une prédiction, if face à unless |
| modaux (04) | 10 | can, must, should, might, had to, mustn't | might face à should, would like to face à modal + base, valeur d'un modal cité |
| relatifs (08) | 8 | who / which / that sujet | which qui reprend une idée, who face à whose, that après un superlatif |
| comparatif ou superlatif (08) | 12 | -er than, the -est, as … as | one of the most, much / more / most, sans degré (fun) |
| formes de la comparaison (08) | 11 | orthographe -er / -est | as much … as, much better, larger d'après un indice lointain |
| prépositions (09) | 30 et plus | aucune | toute la famille |
| connecteurs (09) | 14 | because, so, therefore, while, whereas, but | besides, although, however face à so |
| vocabulaire en contexte (09) | 41 | mot inventé à deviner | choix entre mots du même domaine, construction du verbe |
| appariements (09) | 37 | aucun | toute la famille |
| production (02, 04, 09) | 41 | phrase-titre, unité, ordre d'un paragraphe | consigne officielle, tâche exacte, formules de lettre, règles de dépliant |

**Compréhension** : le 09 et le 10 n'ont aucune question sur un texte officiel ; leurs textes sont inventés et
courts. **Le 10 (sujets types)** reste tel quel : le plan ne compose pas de sujet complet.

**Bilan de l'écart** : 21 missions d'examen (plan v1), dont 5 de compréhension, 4 de production préparée et 12
de langue ; rien de ce que le patron pose déjà n'est redemandé. Restent sans mission, en attente de l'arbitrage
du pilote : la dérivation, le gérondif et les pronoms (`PLAN.md` § 6). Les devoirs, lus en salle blanche, sont
traités à part (§ 5 du plan, lot `L05`).

## 4. Mesures — à la lecture
