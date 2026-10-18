# Anglais 6ᵉ — fiche du couple `6eme-base × english-6eme` (étude 36, le gisement)

```yaml
# en-tête de provenance — profil source-web (étude 27, D-2) ; carte qui croise plusieurs sites
url: plusieurs pages — voir les fiches de site web-devoir-tn et web-echoexam-edunet-tn
titulaire: plusieurs — voir les fiches de site
consulte_le: 2026-10-18
cgu: voir les fiches de site
robots: autorise (devoir.tn) ; absent (6web.edunet.tn, echoexam.edunet.tn)
autorisation: aucune
tier: T2-prime
snapshot: scratchpad de la session du 2026-10-18, hors git ; empreintes SHA-256 dans gisement.json
```

> **Ce que cette fiche est, et n'est pas.** Le registre du couple `english-6eme` dans le pipeline
> du gisement ([étude 36](../../../../FableEtudes/36-gisement-examens-devoirs/ETUDE.md)) : son
> échantillon, puis sa carte, son écart et ses mesures. Aucune phrase, aucun nombre, aucun
> contexte d'un devoir n'y entre. Elle n'est **pas** une référence de programme : le périmètre
> reste celui du guide officiel `541608P00` (fiche `programme/6eme-base/anglais.md`).
> État des lieux et plan du passage : `FableEtudes/campagnes/anglais-6eme/` (ETAT, PLAN).

## 1. Protocole

Le pipeline de l'étude 36, deux régimes : les **sujets d'examen national** — ici l'épreuve
d'anglais du **concours d'entrée aux collèges pilotes** (« مناظرة الدخول إلى المدارس الإعدادية
النموذجية », 6ᵉ année de base) — sont du corpus officiel (méthode R-2) : transcrits fidèlement sous
`programmes-officiels/examens-nationaux/6eme-base/english/`, chaque exercice devient une mission
qui le reprend et le cite ; les **devoirs** sont lus en salle blanche (T2′) — une ligne anonyme par
exercice, et `content-ecole-tn` (avec `content-langue-anglais`) écrit une mission neuve par
archétype distinct sans jamais voir la source.

Périmètre (D-10) : l'anglais **est** une épreuve du concours de 6ᵉ — session 2026, lundi 22 juin,
2ᵉ séance, d'après le portail du Ministère (`http://www.echoexam.edunet.tn/index-sujet-6eme.php`,
consulté le 2026-10-18 ; épreuves : arabe, anglais, français, éveil scientifique, maths).

Placement (décision D2 du pilote, 2026-10-18) : le manifeste de la 6ᵉ n'a que les sept unités ; une
mission de **reading** ou de **writing** va au chapitre de l'unité dont relève le **thème** du texte
ou de la consigne ; une mission de langue, au chapitre qui enseigne la notion.

## 2. Programme en vigueur — « Learn and Grow » (décision D7, vérifiée le 2026-10-18)

- **Manuel actuel** : « Learn and Grow — Year 6 Basic Education » (CNP), guide enseignant
  `541608P00`. Le PDF du guide servi par le CNP (`https://www.cnp.com.tn/arabic/PDF/541608P00.pdf`)
  porte en métadonnées `CreationDate: 2023-01-20` (Adobe InDesign 18.0) ; le manuel élève ne figure
  pas sur le site du CNP (codes `1416xx` en 404) mais il est vendu en librairie comme manuel CNP de 6ᵉ.
- **Entrée en vigueur : non datée par une source officielle.** Indices concordants d'une entrée en
  **2022-2023** : la date de fabrication du guide (janvier 2023), et le changement de forme des
  sujets du concours (2 pages jusqu'en 2022, 3 en 2023, 4 en 2024–2026 ; le texte 2026 recoupe
  l'unité IV « Caring »). Le lecteur marque donc, à la lecture, ce qui sort du scope des 35 encadrés
  dans les sessions **2008–2022** (programme probablement antérieur) ; ces sessions restent dans
  l'échantillon (D3 : toutes les sessions).
- **« First year of English » est faux pour le programme actuel** : le guide lui-même renvoie à
  l'anglais de la 4ᵉ année (p. 40, unité IV leçon 5 : « The teacher uses the Year 4 audio ») ; le
  Ministère a annoncé l'anglais dès la **4ᵉ année primaire à la rentrée 2019-2020**
  (Business News, 2019-03-24, `https://businessnews.com.tn/2019/03/24/article-1159404/1159404/`), et
  les documents du projet PARLE (2024) décrivent l'anglais enseigné dès la 4ᵉ. La 6ᵉ est donc la
  **troisième** année d'anglais (A1). À corriger dans `english-6eme/subject.json` et dans la fiche
  programme au lot E (le scope, lui, ne change pas : le guide fait foi).

## 3. Échantillon — fixé le 2026-10-18, avant l'ouverture de tout document

- **examens** : toutes les sessions de l'archive du Ministère (`http://6web.edunet.tn/`, « مواضيع
  المناظرات الوطنية منذ 2008 », épreuve « anglais ») — **17 sujets**, sessions 2008 à 2026, filière
  unique ; **C13 (2014) et C16 (2011) introuvables** (404). Les 17 PDF sont des scans (lecture
  vision, é36 D-8).
- **devoirs, vague 1** (décision D4 du pilote) : la rubrique 6ᵉ Anglais de `devoir.tn` range
  **41 épreuves** par trimestre (13 · 13 · 15), dont 34 sans nom ni année. Neuf retenues, **trois
  par trimestre**, les signées et les plus récentes d'abord, les anonymes en complément (rang le
  plus haut d'abord), au plus deux par auteur (le plafond n'est vérifiable que pour les signées) ;
  une vague de plus tant que la précédente apporte ≥ 30 % de signatures neuves (étude 36, D-4).

| id | créneau | année | site | auteur ou établissement (tel que le site le nomme) | SHA-256 (16 premiers caractères) |
| --- | --- | --- | --- | --- | --- |
| D01 | T1 | 2020-2021 | devoir.tn | nawel-mathlouthi | `1acac6ef9dee2e26…` |
| D02 | T1 | 2020-2021 | devoir.tn | ecole-primaire-de-birine | `c45d35d757aba9e9…` |
| D03 | T1 | 2020-2021 | devoir.tn | faten-msdi | `213b8941ce7827c7…` |
| D04 | T2 | — | devoir.tn | anonyme | `72890462767aeab8…` |
| D05 | T2 | — | devoir.tn | anonyme | `373769c320c48f18…` |
| D06 | T2 | — | devoir.tn | anonyme | `99cd151ba9adbf03…` |
| D07 | T3 | 2018-2019 | devoir.tn | khaled-mansouri (école « le pilote ») | `3b762953ccdbb54f…` |
| D08 | T3 | 2018-2019 | devoir.tn | khaled-mansouri (école « le pilote ») | `c3e7e4f494a7663e…` |
| D09 | T3 | — | devoir.tn | anonyme | `355d230cff9b1bc1…` |

Écartée du T1 par le plafond « les plus récentes d'abord » : la seule autre signée (sabrine-bhar,
2019-2020). Les devoirs signés sont **antérieurs** à « Learn and Grow » (2018–2021) : le lecteur
marque ce qui sort du scope ; une vague 2 privilégiera des devoirs postérieurs à 2022 s'il s'en
trouve.

Liste machine (sessions, fichiers officiels, empreintes, rang du devoir dans sa page) :
[`gisement.json`](./gisement.json). L'URL du fichier d'un devoir reste hors git (la fiche pointe la
page de liste du trimestre et le rang de l'épreuve).

## 4. Carte — à la lecture

## 5. Écart avec le contenu existant — à la lecture

## 6. Mesures — à la lecture
