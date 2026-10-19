# Français 6ᵉ — fiche du couple `6eme-base × french-6eme` (étude 36, le gisement)

```yaml
# en-tête de provenance — profil source-web (étude 27, D-2) ; carte qui croise plusieurs sites
url: plusieurs pages — voir les fiches de site web-devoir-tn et web-echoexam-edunet-tn
titulaire: plusieurs — voir les fiches de site
consulte_le: 2026-10-19
cgu: voir les fiches de site
robots: autorise (devoir.tn) ; absent (6web.edunet.tn, echoexam.edunet.tn)
autorisation: aucune
tier: T2-prime
snapshot: scratchpad de la session du 2026-10-19, hors git ; empreintes SHA-256 dans gisement.json
```

> **Ce que cette fiche est, et n'est pas.** Le registre du couple `french-6eme` dans le pipeline
> du gisement ([étude 36](../../../../FableEtudes/36-gisement-examens-devoirs/ETUDE.md)) : son
> échantillon, puis sa carte, son écart et ses mesures. Aucune phrase, aucun nombre, aucun
> contexte d'un devoir n'y entre. Elle n'est **pas** une référence de programme : le périmètre
> reste celui des sources officielles du CNP (fiche `programme/6eme-base/francais.md`).

## 1. Protocole

Le pipeline de l'étude 36, deux régimes : les **sujets d'examen national** — ici l'épreuve de
français du **concours d'entrée aux collèges pilotes** (« مناظرة الدخول إلى المدارس الإعدادية
النموذجية », 6ᵉ année de base) — sont du corpus officiel (méthode R-2) : transcrits fidèlement sous
`programmes-officiels/examens-nationaux/6eme-base/french/`, chaque exercice devient une mission qui
le reprend et le cite ; les **devoirs** sont lus en salle blanche (T2′) — une ligne anonyme par
exercice, et `content-ecole-tn` écrit une mission neuve par archétype distinct sans jamais voir la
source.

Périmètre (D-10) : le français **est** une épreuve du concours de 6ᵉ — session 2026, mardi 23 juin,
1ʳᵉ séance, d'après le portail du Ministère (`http://www.echoexam.edunet.tn/index-sujet-6eme.php`,
consulté le 2026-10-19 ; épreuves : arabe et anglais le lundi 22, français et éveil scientifique le
mardi 23, mathématiques le mercredi 24).

## 2. Programme en vigueur

Le programme de référence est celui de la fiche validée
[`programme/6eme-base/francais.md`](../../programme/6eme-base/francais.md) (collection « Un pas de
plus… vers le collège », guide `521612`, manuel de lecture `121614`, cahier d'activités `121615`,
fichier-classe `521616`). Rien n'y est redit ici ; la date d'entrée en vigueur et ce qui, dans les
sujets les plus anciens, sort du scope se constatent à la lecture (étage G2), comme pour l'anglais.

## 3. Carte et écart — écrits le 2026-10-19 (étages G3 et G4, 238 lignes : 185 d'examen, 53 de devoirs)

Lignes validées par `content:gisement:lignes` (238 valides, 0 fautive). Aucune phrase, aucun nombre, aucun contexte d'un devoir n'entre ici : la carte des devoirs dit des familles de gestes.

**Format de l'épreuve** (17 sessions, 2008 à 2026) : une heure, 20 points, un texte narratif ; Compréhension 6 + Grammaire 3 + Conjugaison 3 + Production écrite 8. Barème par question imprimé seulement en 2024, 2022, 2021 et 2020. Pas d'orthographe-dictée.

**Chapitres portés par les lignes d'examen** (une ligne peut en porter plusieurs) :

| chapitre | 2021–2026 | 2008–2020 | devoirs | ce que testent les sujets |
| --- | ---: | ---: | ---: | --- |
| `01-travailler-pour-sepanouir` | 12 | 31 | 8 | le temps de la phrase (présent, passé composé, futur) avec un repère de temps ; verbes en -er et verbes hors liste ; pronoms personnels ; infinitif après préposition (une fois) ; nature des mots dans les devoirs ; aucun texte d'examen, aucune consigne de production |
| `02-communiquer-avec-les-autres` | 15 | 22 | 22 | démonstratifs et possessifs (changer le nom, changer la personne), **impératif d'un ordre rapporté (onze lignes)**, pluriel des noms ; textes 2026, 2020, 2013, 2008 (écrans, Internet, portable) ; quatre lectures de devoir sur la communication |
| `03-accepter-les-autres` | 5 | 18 | 10 | épithète / attribut (tableau), être au futur et au passé composé, accord des adjectifs épithètes ; peu de langue, trois textes anciens (2017, 2016, 2009) et deux productions « faire accepter » |
| `04-sentraider-pour-reussir` | 13 | 20 | 5 | négation ne… plus / ne… jamais (huit lignes), verbes comme finir au passé composé et au futur, récits d'entraide (2021, 2020, 2019, 2015) ; « et / est » jamais testé |
| `05-sauver-la-nature` | 19 | 27 | 13 | complément essentiel / non essentiel (relever, supprimer, déplacer), **prendre et mettre** (le verbe le plus fréquent), accord du verbe avec son sujet ; textes 2024, 2018, 2012 ; deux devoirs de lecture sur la nature |
| `06-etre-en-forme` | 16 | 24 | 1 | aller et faire (présent, passé composé, futur), accord de l'adjectif avec le nom ; le complément de lieu seulement dans un tableau ; texte 2023 ; **aucune lettre en examen** |
| `07-profiter-du-temps-libre` | 11 | 18 | 1 | complément de temps (en tableau), consonne doublée (nul/nulle, bon/bonne), dire/lire/écrire presque jamais (deux lignes) ; texte 2022 ; trois « suites » de scène (2010, 2009, 2008) |
| `08-autres-modes-de-vie` | 13 | 23 | 1 | complément de manière (en tableau), vouloir/pouvoir, passé composé avec être ; texte 2025 ; une lettre à un ami lointain dans les devoirs |

**Hors programme** : 11 lignes d'examen sur 185 portent un jeton `HP:` (aucune n'est `HP:` seule) ; sept lignes de langue sont entièrement ou principalement hors guide (`HP:negation-personne`, `HP:pc-pronominal`, `HP:cod`, `HP:voix-passive`, `HP:discours-indirect`, `HP:pronom-complement`). Les sujets 2008–2026 restent conformes à la fiche : aucune session n'est ancienne au sens fort.

**Archétypes d'examen** : compréhension (67 lignes : relevé et justification, synonymes puis contraires dans chaque session, avis ou hypothèse dans chaque session), langue (101 : réécriture sous consigne « remplace X par Y », tableau de fonctions, ordre rapporté → impératif, changement de temps), production (17 : récit d'au moins huit phrases avec dialogue ou répliques).

**Devoirs (vague 1)** : 53 lignes, 2 portent un jeton `HP:` (4 %). Mesure de la règle des 30 % : 28 % de lignes à signature neuve (mesure mixte), 35 % en strict, 19 % au niveau gabarit. Gestes absents des examens : appariement, remise en ordre, titre, nature des mots, son/sont, correction d'erreurs, lettre. Les chapitres 06, 07 et 08 n'y apparaissent presque pas (une ligne chacun). `D04`, `D05` et `D06` ont la même main : `D06` est écarté (plafond de deux par auteur). **Pas de vague 2** (décision du pilote).

**Écart avec le contenu existant** : le patron (8 chapitres × 36 questions, écrit de zéro et audité) n'a **aucune** phrase officielle, aucune réécriture sous consigne d'examen, aucun tableau de fonctions à quatre colonnes, aucun texte à lire (hors mini-récits de l'auteur), aucune consigne de rédaction : c'est ce que le gisement apporte.

**Plan** : [`PLAN-gisement.md`](../../../../FableEtudes/campagnes/francais-6eme/PLAN-gisement.md) et `plan-missions-v1.json` — **27 missions d'examen et 6 de devoirs (278 questions)**, au statut `planifiee` dans `gisement.json` ; chaque mission nomme les questions existantes à ne pas redemander. Compréhension : cinq textes (2026, 2025, 2024, 2023, 2022). Production : six archétypes, les 17 consignes reprises. Langue : 94 lignes sur 101. Devoirs : onze lignes sur 53.

## 4. Échantillon — fixé le 2026-10-19, avant l'ouverture de tout document

- **examens** : toutes les sessions de l'archive du Ministère (`http://6web.edunet.tn/`, « مواضيع
  المناظرات الوطنية منذ 2008 », épreuve « francais ») — **19 sessions interrogées (2008 à 2026), 17
  sujets téléchargés**, filière unique ; **C13 (2014) et C16 (2011) introuvables** (404, comme en
  anglais). Les 17 PDF sont à lire par vision (scans, é36 D-8). Ids dans l'ordre de l'anglais :
  C01 (2026), C02 (2025), C03 (2024), C04 (2023), C05 (2022), C06 (2021), C07 (2020), C08 (2019), C09 (2018), C10 (2017), C11 (2016), C12 (2015), C13 (2014), C14 (2013), C15 (2012), C16 (2011), C17 (2010), C18 (2009), C19 (2008).
- **devoirs, vague 1** (décision D4 du pilote) : **devoir.tn n'a pas de rubrique « Français » unique
  en 6ᵉ primaire** (la rubrique `Français/Devoirs/…` renvoie à la page de la classe). Le français y
  est éclaté en quatre rubriques, chacune avec ses pages de trimestre : **Langue** (2 · 3 · 1
  épreuves), **Lecture** (9 · 14 · 8), **Production écrite** (9 · 14 · 8) et **Dictée** (2 · 2 · pas
  de page de 3ᵉ trimestre), soit 72 entrées, dont un doublon (le devoir de synthèse n°1 Tadris.TN,
  rangé en Langue et en Lecture, T1). Les rubriques sont mises en commun par trimestre. Neuf
  retenues, **trois par trimestre**, les signées et les plus récentes d'abord, les anonymes en
  complément (numéro d'épreuve le plus haut d'abord ; à égalité, Langue, Lecture, Production écrite,
  Dictée), au plus deux par auteur ; une vague de plus tant que la précédente apporte ≥ 30 % de
  signatures neuves (étude 36, D-4).

| id | créneau | rubrique | année | site | auteur ou établissement (tel que le site le nomme) | SHA-256 (16 premiers caractères) |
| --- | --- | --- | --- | --- | --- | --- |
| D01 | T1 | Langue | 2024 | devoir.tn | tadris-tn | `7bd918b52573354f…` |
| D02 | T1 | Lecture | 2014 | devoir.tn | ecole-primaire-el-hajeb-kairwan | `6fc23df643b7e23b…` |
| D03 | T1 | Production écrite | — | devoir.tn | anonyme | `cac0ec4777d05350…` |
| D04 | T2 | Langue | 2020 | devoir.tn | barhoumi-mounir (école primaire Brahmia) | `42bd74bfb0053dc4…` |
| D05 | T2 | Lecture | 2020 | devoir.tn | barhoumi-mounir | `ee350f1b94c42118…` |
| D06 | T2 | Production écrite | 2020 | devoir.tn | ecole-primaire-brahmia | `6e9161afc35f0a1d…` |
| D07 | T3 | Lecture | — | devoir.tn | anonyme | `414f7e5fe5f358b9…` |
| D08 | T3 | Production écrite | — | devoir.tn | anonyme | `bad9475f1302bf16…` |
| D09 | T3 | Lecture | — | devoir.tn | anonyme | `ecb16428f4b70543…` |

Écartées par la règle : en T1, la production écrite n°05 (2012-2013) et n°06 (2014-2015), datées mais
sans signature, donc anonymes de rang plus bas que la n°09 ; en T2, la dictée n°02 (2019-2020, école
Brahmia, quatrième des signées de 2019-2020 à égalité d'année), la lecture n°13 (2018-2019, Barhoumi)
et les trois épreuves de 2015 (Hcini, Jledi), plus anciennes ; en T3, aucune épreuve n'est signée ni
datée : la règle retient les numéros les plus hauts, d'où l'absence de la rubrique Langue ce
trimestre-là (une seule épreuve, n°01). Le plafond de deux par auteur n'a joué nulle part (Barhoumi :
deux retenues en T2). Les devoirs signés sont **antérieurs** au programme
actuel pour la plupart (2014–2020) ; seul D01 (2023-2024) est récent : le lecteur marque ce qui sort
du scope, et une vague 2 privilégiera des devoirs récents s'il s'en trouve. D03 porte dans son
en-tête 2014/2015 (la page de liste ne donne rien), noté en remarque.

Liste machine (sessions, fichiers officiels, empreintes, rang du devoir dans sa page) :
[`gisement.json`](./gisement.json). L'URL du fichier d'un devoir reste hors git (la fiche pointe la
page de liste du trimestre et le rang de l'épreuve).
