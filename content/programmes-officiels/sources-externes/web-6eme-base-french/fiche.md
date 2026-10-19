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

## 3. Carte et écart — à la lecture

Écrits après la lecture des documents (étages G2 à G4) : carte des lignes d'examen et de devoirs par
chapitre, hors-programme, archétypes, écart avec le contenu publié, plan des missions.

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
