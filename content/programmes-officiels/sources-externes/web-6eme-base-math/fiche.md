# Maths 6ᵉ — fiche du couple `6eme-base × math-6eme` (étude 36, le gisement)

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

> **Ce que cette fiche est, et n'est pas.** Le registre du couple `math-6eme` dans le pipeline du
> gisement ([étude 36](../../../../FableEtudes/36-gisement-examens-devoirs/ETUDE.md)) : son
> échantillon d'abord, puis (étages G3 et G4) sa carte, son écart et ses mesures. Aucune phrase,
> aucun nombre, aucun contexte d'un devoir n'y entre. Elle n'est **pas** une référence de
> programme : le périmètre reste celui des sources officielles du CNP (fiche
> [`programme/6eme-base/maths.md`](../../programme/6eme-base/maths.md)).

## 1. Protocole

Le pipeline de l'étude 36, deux régimes : les **sujets d'examen national** — ici l'épreuve de
mathématiques du **concours d'entrée aux collèges pilotes** (« مناظرة الدخول إلى المدارس الإعدادية
النموذجية », 6ᵉ année de base) — sont du corpus officiel (méthode R-2) : transcrits fidèlement sous
`programmes-officiels/examens-nationaux/6eme-base/math/`, chaque exercice devient une mission qui le
reprend et le cite ; les **devoirs** sont lus en salle blanche (T2′) — une ligne anonyme par
exercice, et `content-ecole-tn` écrit une mission neuve par archétype distinct sans jamais voir la
source.

Périmètre : les mathématiques **sont** une épreuve du concours de 6ᵉ — session 2026, mercredi 24
juin, d'après le portail du Ministère (`http://www.echoexam.edunet.tn/index-sujet-6eme.php`, consulté
le 2026-10-19 ; arabe et anglais le lundi 22, français et éveil scientifique le mardi 23,
mathématiques le mercredi 24). Le portail ne publie que la session de l'année et renvoie à
l'archive : il n'offre rien pour 2011 et 2014.

## 2. Programme en vigueur

Le programme de référence est celui de la fiche validée
[`programme/6eme-base/maths.md`](../../programme/6eme-base/maths.md). Rien n'y est redit ici ; ce
qui, dans les sujets les plus anciens, sort du programme actuel se constate à la lecture (étage
G2), comme pour l'anglais et le français.

## 3. Carte et écart

Écrite le 2026-10-19 (étages G3–G4) ; le détail et les règles sont dans `FableEtudes/campagnes/maths-6eme/PLAN-gisement.md`. Aucune phrase, aucun nombre, aucun contexte d'un devoir n'entre ici.

**Les 17 sujets du concours** (1 h, trois problèmes rédigés 6 + 6 + 8, aucun QCM) donnent 119 lignes : argent (fraction, %, remise), trajet (vitesse, durée, horaire), géométrie longue (aires, contour, échelle). Chapitres les plus sollicités : 14 et 13 (fractions, pourcentages), 5 et 4 (décimaux), 20 (aires), 22 et 15 (durées, vitesse), 19, 21, 25 (contours) ; jamais 1, 7, 12, 23, 26. **Les 9 devoirs** (124 lignes, évaluation par critère) ajoutent les multiples sans intervalle, les critères de divisibilité à plusieurs chiffres, la monnaie en millimes et des constructions guidées.

**Plan** : 38 missions (32 d'examen, un problème entier chacune, 17 sessions sur 17 ; 6 de devoirs en salle blanche), 326 questions, quatre lots M1 (06, 07, 13), M2 (14, 15), M3 (21, 22), M4 (19, 20, 25). Écarts : problèmes à énoncé défectueux (2017 P3, 2009 P2, 2013 P2, 2020 P3), cibles ◐ (intérêt, somme-écart, somme-rapport) et sept problèmes sains redondants. Registre : `gisement.json`, `missions`.

## 4. Échantillon — fixé le 2026-10-19, avant la lecture de tout document

- **examens** : toutes les sessions de l'archive du Ministère (`http://6web.edunet.tn/`, « مواضيع
  المناظرات الوطنية منذ 2008 », épreuve « math ») — **19 sessions interrogées (2008 à 2026), 17
  sujets téléchargés** (2 pages chacun), filière unique ; **C13 (2014) et C16 (2011) introuvables** :
  404 sur `6web.edunet.tn/<année>/math.pdf` et sur `www.echoexam.edunet.tn/<année>/math.pdf`, et le
  portail de la session ne lie que la session 2026 (comme pour l'anglais et le français). Les 17 PDF
  sont à lire par vision (scans, é36 D-8). Ids dans l'ordre de l'anglais et du français : C01
  (2026), C02 (2025), C03 (2024), C04 (2023), C05 (2022), C06 (2021), C07 (2020), C08 (2019), C09
  (2018), C10 (2017), C11 (2016), C12 (2015), C13 (2014), C14 (2013), C15 (2012), C16 (2011), C17
  (2010), C18 (2009), C19 (2008).
- **devoirs, vague 1** : **devoir.tn n'a pas de rubrique « Devoirs » pour les mathématiques de 6ᵉ
  primaire** (les rubriques `Devoirs` n'existent que pour Anglais, Dictée, Langue, Lecture,
  Production écrite et Éveil scientifique). Les évaluations de maths sont rangées sous
  `الـرياضـيـات/تقييمات/`, **un dossier par trimestre** (25 · 43 · 20 PDF), en pratique des
  « modèles » numérotés, presque tous sans nom ni année ; en plus, `إختبار-تجريبي` (concours blancs,
  hors vague : à considérer en vague 2 ou comme séries) et `مناظرات` (reprises de sujets officiels
  2013, non retenues : le portail du Ministère fait foi). Neuf retenues, **trois par trimestre**, les
  signées et les plus récentes d'abord, les anonymes en complément (numéro de modèle le plus haut
  d'abord), au plus deux par auteur, un seul si possible (diversité).

| id | créneau | rubrique | année | site | auteur ou établissement (tel que le site le nomme) | SHA-256 (16 premiers caractères) |
| --- | --- | --- | --- | --- | --- | --- |
| D01 | T1 | تقييمات | 2018-2019 | devoir.tn | Salah Samaali (école El Arich) | `8f36be3d47e48ce2…` |
| D02 | T1 | تقييمات | 2019-2020 (fichier : 2020-2021) | devoir.tn | anonyme (modèle n°23) | `c65fc0cde6459932…` |
| D03 | T1 | تقييمات | 2019-2020 | devoir.tn | anonyme (modèle n°24) | `b7a9b23eed1a6dfd…` |
| D04 | T2 | تقييمات | 2015-2016 | devoir.tn | Sami Mliani (école rue d'Espagne, Bizerte), modèle n°15 | `72660e3242004c75…` |
| D05 | T2 | تقييمات | — | devoir.tn | anonyme (modèle n°40) | `759acfcbaf80c50c…` |
| D06 | T2 | تقييمات | 2019-2020 | devoir.tn | anonyme (modèle n°39) | `fafb23245291e045…` |
| D07 | T3 | تقييمات | — | devoir.tn | anonyme (modèle n°21) | `3ded8e18ab7df605…` |
| D08 | T3 | تقييمات | — | devoir.tn | anonyme (modèle n°20 ; feuille au nom « Salah », même mise en page que D01) | `52de91170d416358…` |
| D09 | T3 | تقييمات | juin 2015 | devoir.tn | anonyme (modèle n°19) | `b0f70e1a5c9ce3a5…` |

Écartés par la règle : en T2, l'examen du 2ᵉ trimestre 2018-2019 du même Salah Samaali que D01 (signé
et plus récent que D04, mais deuxième du même auteur : écarté pour la diversité, le plafond de deux
l'aurait permis) ; en T1, les modèles n°1 à n°22 ; en T2, les modèles n°38 et en dessous ; en T3,
les modèles n°18 et en dessous. D01 et D08 sont peut-être de la même main (à confirmer à la lecture ;
deux au plus, plafond respecté). Les années viennent de l'en-tête ou du nom de fichier, notées telles
quelles ; la plupart des devoirs sont **antérieurs** au programme actuel (2015-2020) : le lecteur
marque ce qui sort du scope, et une vague 2 privilégiera des devoirs récents s'il s'en trouve. D02
compte 14 pages (plusieurs situations d'évaluation). Les devoirs sont rédigés en arabe.

Liste machine (sessions, fichiers officiels, empreintes, rang du devoir dans sa page) :
[`gisement.json`](./gisement.json). L'URL du fichier d'un devoir reste hors git (la fiche pointe la
page de liste du trimestre et le rang de l'épreuve).
