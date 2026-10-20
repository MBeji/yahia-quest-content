# Éveil scientifique 6ᵉ — fiche du couple `6eme-base × eveil-scientifique-6eme` (étude 36, le gisement)

```yaml
# en-tête de provenance — profil source-web (étude 27, D-2) ; carte qui croise plusieurs sites
url: plusieurs pages — voir les fiches de site web-devoir-tn et web-echoexam-edunet-tn
titulaire: plusieurs — voir les fiches de site
consulte_le: 2026-10-20
cgu: voir les fiches de site
robots: autorise (devoir.tn) ; absent (6web.edunet.tn, echoexam.edunet.tn)
autorisation: aucune
tier: T2-prime
snapshot: scratchpad de la session du 2026-10-20, hors git ; empreintes SHA-256 dans gisement.json
```

> **Ce que cette fiche est, et n'est pas.** Le registre du couple `eveil-scientifique-6eme` dans le
> pipeline du gisement ([étude 36](../../../../FableEtudes/36-gisement-examens-devoirs/ETUDE.md)) :
> son échantillon d'abord, puis (étages G3 et G4) sa carte, son écart et ses mesures. Aucune phrase,
> aucun nombre, aucun contexte d'un devoir n'y entre. Elle n'est **pas** une référence de programme :
> le périmètre reste celui des sources officielles du CNP (fiche
> [`programme/6eme-base/eveil.md`](../../programme/6eme-base/eveil.md)).

## 1. Protocole

Le pipeline de l'étude 36, deux régimes : les **sujets d'examen national** — ici l'épreuve d'éveil
scientifique du **concours d'entrée aux collèges pilotes** (« مناظرة الدخول إلى المدارس الإعدادية
النموذجية », 6ᵉ année de base) — sont du corpus officiel (méthode R-2) : transcrits fidèlement sous
`programmes-officiels/examens-nationaux/6eme-base/eveil/`, chaque exercice devient une mission qui le
reprend et le cite ; les **devoirs** sont lus en salle blanche (T2′) — une ligne anonyme par
exercice, et `content-ecole-tn` écrit une mission neuve par archétype distinct sans jamais voir la
source.

Périmètre : l'éveil scientifique **est** une épreuve du concours de 6ᵉ — session 2026, mardi 23
juin, d'après le portail du Ministère (`http://www.echoexam.edunet.tn/index-sujet-6eme.php`, consulté
le 2026-10-20 ; arabe et anglais le lundi 22, français et éveil scientifique le mardi 23,
mathématiques le mercredi 24). Dans l'archive, l'épreuve s'appelle **`svt`** (`/<année>/svt.pdf`).
Le portail ne publie que la session de l'année et renvoie à l'archive : il n'offre rien pour 2011
et 2014.

## 2. Programme en vigueur

Le programme de référence est celui de la fiche validée
[`programme/6eme-base/eveil.md`](../../programme/6eme-base/eveil.md). Rien n'y est redit ici ; ce
qui, dans les sujets les plus anciens, sort du programme actuel se constate à la lecture (étage G2),
comme pour l'anglais, le français et les maths.

## 3. Carte et écart

Écrite le 2026-10-20 (étages G3–G4) ; le détail, les règles et les décisions sont dans `FableEtudes/campagnes/eveil-6eme/PLAN-gisement.md`. Aucune phrase, aucun nombre, aucun contexte d'un devoir n'entre ici.

**Les 17 sujets du concours** (une heure, sur 20, 2 à 3 situations de supports suivis de consignes courtes, aucun QCM) donnent 203 lignes : `01-air` (combustion, oxygène, propriétés) est le chapitre le plus sollicité, devant `07-aimants-boussole` (surtout les directions lues avec un nord qui n'est pas en haut), `03-sang-circulation`, `05-milieu-chaines-alimentaires`, `04-nutrition` et `02-respiration` ; `06`, `08`, `09`, `11` et `12` ne sortent qu'en 2018 ou avant 2017 ; `10` peu. **Les 9 devoirs** (99 lignes, 72 hors le jumeau D01 et la copie D09) sont dominés par un même scénario de combustion au premier trimestre ; aucun sur l'œil ni la lumière.

**Plan** : 41 missions (34 d'examen, 192 lignes sur 203, 17 sessions sur 17 ; 7 de devoirs en salle blanche), 390 questions, quatre lots M1 (09, 12, 01), M2 (02, 03, 10), M3 (04, 06, 05), M4 (07, 11, 08). Écarts : énoncés défectueux corrigés dans la reprise (cinquième d'oxygène, suie en flamme bleue, lentille de l'hypermétropie, sens air/eau, sérum, chaînes « غذاء لـ »), notions ◐ jamais ciblées (zones de la flamme, ganglions, tache aveugle, satellites, pesticides). Registre : `gisement.json`, `missions`. Les « ne pas redemander » sont provisoires : les 12 chapitres sont mis à niveau sur la fiche après le plan.

## 4. Échantillon — fixé le 2026-10-20, avant l'ouverture de tout document

- **examens** : toutes les sessions de l'archive du Ministère (`http://6web.edunet.tn/`, « مواضيع
  المناظرات الوطنية منذ 2008 », épreuve « svt ») — **19 sessions interrogées (2008 à 2026), 17
  sujets téléchargés** (2 à 4 pages chacun : 3 pour 2008, 2 pour 2009–2018 sauf 2019 à 2026 qui en
  ont 4), filière unique ; **C13 (2014) et C16 (2011) introuvables** : 404 sur
  `6web.edunet.tn/<année>/svt.pdf` et sur `www.echoexam.edunet.tn/<année>/svt.pdf`, et le portail de
  la session ne lie que la session 2026 (comme pour l'anglais, le français et les maths). Les 17 PDF
  sont à lire par vision (scans, é36 D-8). Ids dans l'ordre des autres couples : C01 (2026), C02
  (2025), C03 (2024), C04 (2023), C05 (2022), C06 (2021), C07 (2020), C08 (2019), C09 (2018), C10
  (2017), C11 (2016), C12 (2015), C13 (2014), C14 (2013), C15 (2012), C16 (2011), C17 (2010), C18
  (2009), C19 (2008).
- **devoirs, vague 1** : devoir.tn range l'éveil scientifique de 6ᵉ sous `الإيقاظ العلمي/`, avec
  **deux** dossiers d'épreuves, à la différence des maths (qui n'ont que `تقييمات`) : `Devoirs`
  (**3** épreuves, hors trimestre : le devoir de synthèse n°1 Tadris.TN 2023-2024, et les examens des
  1ᵉʳ et 2ᵉ trimestres 2018-2019 de Salah Samaali, école El Arich) et `تقييمات`, **un dossier par
  trimestre** (16 · 24 · 7 « modèles » numérotés, soit 47 PDF), presque tous sans nom ni année. À
  côté : `تجريبي` (2 concours blancs) et `تمارين` (3 séries de révision) — hors vague, séries
  éventuelles d'une vague ultérieure. Neuf retenues, **trois par trimestre**, les signées et les plus
  récentes d'abord, les anonymes en complément (numéro de modèle le plus haut d'abord, un modèle daté
  passant avant un modèle sans date), au plus deux par auteur, un seul si possible (diversité).

| id | créneau | rubrique | année | site | auteur ou établissement (tel que le site le nomme) | SHA-256 (16 premiers caractères) |
| --- | --- | --- | --- | --- | --- | --- |
| D01 | T1 | Devoirs | 2023-2024 | devoir.tn | tadris-tn (Devoir de synthèse n°1 (2023-2024)) | `38041aa656cc71a2…` |
| D02 | T1 | Devoirs | 2018-2019 | devoir.tn | salah-samaali (école El Arich) (Examen du 1ᵉʳ trimestre (2018-2019)) | `7ef90d47cc98a6f1…` |
| D03 | T1 | تقييمات | — | devoir.tn | anonyme (modèle n°16) | `834b2423c5238428…` |
| D04 | T2 | تقييمات | 2019-2020 | devoir.tn | anonyme (modèle n°23, 2019-2020) | `a726a125b011adff…` |
| D05 | T2 | تقييمات | — | devoir.tn | anonyme (modèle n°22) | `a8325ca554fda83e…` |
| D06 | T2 | تقييمات | — | devoir.tn | anonyme (modèle n°21) | `7416759ced7092e5…` |
| D07 | T3 | تقييمات | — | devoir.tn | anonyme (modèle n°7) | `545152192efec723…` |
| D08 | T3 | تقييمات | — | devoir.tn | anonyme (modèle n°6) | `98cbaee4f8a7eaf0…` |
| D09 | T3 | تقييمات | — | devoir.tn | anonyme (modèle n°5) | `a00bd6fdefd41625…` |

Écartés par la règle : en T2, l'examen du 2ᵉ trimestre 2018-2019 du même Salah Samaali que D02
(signé et daté, mais deuxième du même auteur : écarté pour la diversité) ; en T1, les modèles n°15 et
en dessous ; en T2, le modèle n°1 (nom de fichier irrégulier, sans date) et les modèles n°20 et en
dessous ; en T3, les modèles n°4 et en dessous (le n°4 porte 2005-2006 dans son en-tête, bien avant
le programme actuel). D07 et D09 sortent de la même école (plafond de deux respecté) ; D08 a le
même gabarit que le modèle n°3. Les années viennent de l'en-tête ou du nom de fichier, notées telles
quelles ; la plupart des devoirs sont **antérieurs** au programme actuel : le lecteur marque ce qui
sort du scope, et une vague 2 privilégiera des devoirs récents s'il s'en trouve. Les devoirs sont
rédigés en arabe ; D01 (13 pages) et D09 (15 pages) réunissent plusieurs situations.

Liste machine (sessions, fichiers officiels, empreintes, rang du devoir dans sa page) :
[`gisement.json`](./gisement.json). L'URL du fichier d'un devoir reste hors git (la fiche pointe la
page de liste et le rang de l'épreuve).
