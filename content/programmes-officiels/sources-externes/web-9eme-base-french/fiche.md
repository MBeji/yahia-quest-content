# Français 9ᵉ — fiche du couple `9eme-base × french` (étude 36, le gisement)

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

> **Ce que cette fiche est, et n'est pas.** Le registre du couple `french` dans le pipeline du
> gisement ([étude 36](../../../../FableEtudes/36-gisement-examens-devoirs/ETUDE.md)) : son
> échantillon, puis sa carte, son écart et ses mesures. Aucune phrase, aucun nombre, aucun
> contexte d'un devoir n'y entre. Elle n'est **pas** une référence de programme : le périmètre
> reste celui du manuel officiel.

## 1. Protocole

Le pipeline de l'étude 36, deux régimes : les **sujets d'examen national** sont du corpus
officiel (méthode R-2) — transcrits fidèlement sous `programmes-officiels/examens-nationaux/`,
chaque exercice devient une mission qui le reprend et le cite ; les **devoirs** sont lus en salle
blanche (T2′) — une ligne anonyme par exercice, et `prof-francais-9eme` écrit une mission neuve par archétype
distinct sans jamais voir la source.

## 2. Échantillon — fixé le 2026-09-28, avant l'ouverture de tout document

- **examens** : toutes les sessions de l'archive du Ministère (`9web.edunet.tn`, épreuve
  « francais »), filières générale et technique, et filière unique (2001-2008) — **41 sujets** (generale : 17, technique : 17, unique : 7),
  sessions 2001 à 2026 ; C39 (2004, unique) : introuvable(s) sur l'archive (404) ;
- **devoirs, vague 1** : un par créneau de `devoir.tn` (8 créneaux), le plus récent d'une
  année scolaire 2012-2013 ou postérieure, collège pilote et ordinaire en alternance quand le site
  en range, au plus deux devoirs par auteur ; une vague de plus tant que la précédente apporte
  ≥ 30 % d'archétypes neufs (étude 36, D-4).

| id | créneau | collège (selon le site) | année | site | auteur ou établissement (tel que le site le nomme) | SHA-256 (16 premiers caractères) |
| --- | --- | --- | --- | --- | --- | --- |
| D01 | DC1 | pilote | 2014-2015 | devoir.tn | mr-m | `d089e69565a4b7a8…` |
| D02 | DS1 | ordinaire | 2018-2019 | devoir.tn | chihaoui-sofine | `ae892b7f68286395…` |
| D03 | DC2 | ordinaire | 2018-2019 | devoir.tn | boughanmi-walid | `ecf6d0e434c4528d…` |
| D04 | DS2 | ordinaire | 2019-2020 | devoir.tn | E-P-A-Q-Chebbi-Fahs | `20281b6948d71aa5…` |
| D05 | DC3 | ordinaire | 2013-2014 | devoir.tn | atef-yousfi | `37648c8e345aaf03…` |
| D06 | DS3 | ordinaire | 2017-2018 | devoir.tn | boughanmi-walid | `dbfbd526deb3eb53…` |
| D07 | DC4 | pilote | 2017-2018 | devoir.tn | Gassoumi-Mohamed-Lazhar | `4770544a172f7a07…` |
| D08 | DC5 | pilote | 2015-2016 | devoir.tn | mr-gsoumi-mohamed-lazhar | `24cf0ec6d351c79a…` |

Liste machine des examens (sessions, fichiers officiels, empreintes) : [`gisement.json`](./gisement.json).
L'URL du fichier d'un devoir reste hors git (la fiche pointe la page de liste).

## 3. Carte et écart — examens 2001–2026

Écrit au planificateur du 2026-10-16 (étude 36, étapes G3 et G4). **Matière : les seuls sujets officiels**
de l'examen national : 41 sujets lus (`C01`–`C42`, sans `C39` : 2004, introuvable ; 2014 n'est pas dans
l'archive), 226 lignes (41 compréhensions, 144 questions de langue, 41 productions). Aucun devoir, aucun
corrigé de tiers, aucun site tiers dans cette section. « Format actuel » = 2021–2026 (12 sujets) ;
« formats anciens » = 2001–2020 (29 sujets). Le plan qui en sort :
`FableEtudes/36-gisement-examens-devoirs/en-cours/francais/plan-examens-v1.json` et `PLAN.md` (même dossier).

### 3.1 Architecture de l'épreuve — les créneaux

- **Trois parties sur 20, toujours dans le même ordre** : compréhension d'un texte narratif d'une page
  (extrait de roman ou de récit, chapeau et notes de vocabulaire), langue, production écrite (« Essai »
  jusqu'en 2017 environ).
- **Générale** (2 h) : 7 + 6 + 7 ; **technique** (1 h) : 8 + 6 + 6 ; **épreuve unique** 2001–2008 (2 h) :
  7 + 6 + 7, sauf 2001 et 2002 (6 + 7 + 7).
- **Langue, 6 points** : trois questions en technique, quatre en générale. Depuis 2018 la première est
  presque toujours lexicale (synonyme, sens en contexte) ; la dernière de la générale est un exercice
  d'orthographe grammaticale (homophones ou adverbes en -ment). Entre les deux : une transformation de
  phrase (subordination, passif, négation, pronoms) et une conjugaison.
- **Compréhension** : en générale, trois ou quatre questions ouvertes (relever, justifier par un indice,
  qualités, sentiments, raisons) ; en technique, cases à cocher à justifier par une phrase du texte, puis
  deux questions de relevé. Avant 2010, plus factuelle (qui, où, quoi) ; depuis 2018, centrée sur les
  qualités, les sentiments et les raisons d'un personnage.
- **Production** : générale « une vingtaine de lignes », technique « une dizaine » ; elle impose presque
  toujours un récit au passé, avec un dialogue rapporté ou un portrait.

### 3.2 Fréquence par chapitre (questions de langue, 144 lignes)

Une ligne de langue qui mobilise deux chapitres compte pour chacun. Les compréhensions (41) vont toutes
au 09 ; les productions (41) au 08 et au 09, avec le 06 pour 35 d'entre elles (récit au passé), le 04
pour 10 (dialogue imposé), le 15 pour une (lettre, 2011 technique).

| chapitre | format actuel (2021–2026) | formats anciens (2001–2020) | **total** | ce que les sujets font faire |
| --- | ---: | ---: | ---: | --- |
| 01 types et formes | 3 | 7 | **10** | forme négative (technique surtout), une fois l'affirmative ; voix passive classée aussi au 03 |
| 02 subordonnées | 8 | 27 | **35** | cause, but, conséquence d'intensité par subordination ; pronom relatif selon la fonction ; subordonnée ↔ groupe prépositionnel ; connecteurs de cause ; temps, concession |
| 03 voix passive | 1 | 6 | **7** | actif ↔ passif, temps conservé, sans agent, sujet « on » ; aucune depuis 2023 |
| 04 discours rapporté | 0 | 0 | **0** | jamais en langue ; seulement le dialogue imposé dans dix productions |
| 05 modes et temps | 8 | 29 | **37** | subjonctif ou indicatif selon le verbe introducteur ; transposition (présent, imparfait, futur, passé composé) |
| 06 temps du récit | 8 | 16 | **24** | choix entre passé simple, imparfait et plus-que-parfait ; futur simple / futur antérieur ; présent / passé composé |
| 07 lexique | 13 | 12 | **25** | synonyme et emploi ; sens en contexte (QCM en technique) ; autre sens du mot ; jamais de figure de style |
| 08 types de textes | 1 | 0 | **1** | connecteurs temporels d'un récit (2024 technique) |
| 11 groupe nominal | 2 | 4 | **6** | enrichir un GN (épithète, complément du nom, relative) ; relative → adjectif |
| 12 pronoms | 4 | 11 | **15** | remplacer un groupe par le pronom (le, lui, leur, en, y, à lui, de lui) |
| 13 accords | 3 | 9 | **12** | changer le sujet et accorder ; « tout » ; participe passé |
| 14 homophones et -ment | 6 | 11 | **17** | quand / quant / qu'en, sans / s'en, ni / n'y, quel / qu'elle ; adverbes en -ment |
| 15 presse et lettre | 0 | 0 | **0** | une production seulement (lettre à un ami, 2011 technique) |

Lecture : 05, 02, 07 et 06 portent près des deux tiers de la langue sur 26 ans. Le passif et la négation ont
reculé (une ligne de passif depuis 2021) ; les adverbes en -ment, le futur antérieur et la subordination de
cause, de but ou d'intensité sont devenus réguliers depuis 2017. Part hors programme : nulle (0 ligne sur
226) ; le futur antérieur est au programme (chapitre 05, cours et description du chapitre).

### 3.3 Archétypes et étages

- **Langue** : 48 lignes d1, 88 d2, 8 d3. Les archétypes se répètent d'une session à l'autre : sur 144
  questions, 19 familles (§ 3.4) couvrent tout. Le plus haut niveau : une même phrase simple vers deux
  rapports logiques, la conjugaison qui dépend de l'ordre de deux actions, l'enrichissement de plusieurs
  groupes nominaux d'un paragraphe.
- **Compréhension** : 29 d1, 12 d2 ; toujours le même geste, justifier une réponse par un indice textuel.
- **Production** : 39 d3, 2 d2 ; trois archétypes : récit avec dialogue rapporté (10 sujets, générale),
  récit d'une réussite ou d'une rencontre avec portrait (25), présenter un projet ou un métier et le
  justifier (6, dont une lettre).
- **Vocabulaire des consignes** : « relève », « justifie … par un indice textuel », « coche et
  justifie », « réécris en remplaçant », « transforme », « construis une phrase complexe », « conjugue au
  temps qui convient », « selon le cas », « complète par ».
- **Combinaisons** : conjugaison + concordance (05 + 06) dans 24 lignes ; subordonnée + groupe nominal
  (02 + 11) dans 6 ; changement de sujet + pronoms (13 + 12) dans 3.

### 3.4 Écart avec le contenu existant

Contenu croisé : `content/french/` (15 chapitres au patron, publiés ; quatre exercices de six questions et
un quiz par chapitre, trois sujets types au 10). **Aucune question existante ne reprend une phrase d'un
sujet officiel** : le patron enseigne chaque notion sur des phrases inventées. L'écart est donc de deux
sortes : (1) la forme d'examen (la phrase et le texte officiels, la consigne telle qu'elle tombe) manque
partout ; (2) certaines variantes réelles des sujets ne sont pas posées par le patron. Croisement par
famille (le détail question par question est dans la liste « ne pas redemander » de chaque mission du
plan) :

| famille (chapitre) | sessions | déjà posé par le patron ou le quiz | variantes des sujets que l'existant ne pose pas |
| --- | ---: | --- | --- |
| négation qui garde le sens (01) | 6 | quelqu'un, tout le monde, encore à quelqu'un | toujours → jamais, partitif après négation, affirmative |
| cause, but, intensité (02) | 9 | valeur de « tellement … que », « pour que » + subjonctif | une même phrase vers deux rapports ; but à sujet identique |
| pronom relatif selon la fonction (02) | 8 | dont, où, que | auquel, autour duquel, auxquelles, à qui |
| la cause autrement (02) | 10 | « faute de », articulateurs de conséquence | grâce à / à cause de selon le jugement, comme en tête, que / parce que |
| temps et concession (02) | 7 | dès que, jusqu'à ce que, après que | subordonnée ↔ groupe prépositionnel, gérondif, bien que ↔ malgré |
| voix passive (03) | 7 | transformations simples, on, temps conservé | pronom complément devenu sujet, adverbe, sans agent → on |
| mode après le verbe introducteur (05) | 7 | il faut que, je ne pense pas que, de peur que | espérer / souhaiter / douter / craindre / être sûr dans une même phrase |
| transposition (05) | 8 | aucune | irréguliers, périphrase, verbe passif pris pour un passé composé |
| imparfait, passé simple, plus-que-parfait (06) | 10 | arrière-plan / premier plan | quatre à six verbes d'un récit officiel à choisir ensemble |
| futur simple ou antérieur (06) | 8 | dès que, valeur d'antériorité | quand, lorsque, une fois que, après que dans des phrases à deux actions |
| présent ou passé composé (06) | 7 | « hier, j'ai rencontré » | indicateurs de durée, pronom avant l'auxiliaire, transposition depuis « Hier soir » |
| sens en contexte (07) | 8 | gâter, jouer ; sens en contexte en 09 | lever, couronner, louer, témoigner, franchir |
| synonyme et autre sens (07) | 13 | sens figuré, exercer / pratiquer | synonyme d'une locution, autre sens du même mot |
| adverbes en -ment (14) | 6 | prudent, évident, élégant, récent, hardi | -iment, -ument, -ément, quotidiennement, groupe prépositionnel → adverbe |
| homophones (14) | 11 | une vingtaine de blancs simples | qu'en + gérondif, qu'en + préposition, sans s'en, quel(le)s que soi(en)t |
| pronoms compléments (12) | 12 | lui, y, en, ordre des pronoms | de lui, à elle, laisser faire, regarder + infinitif + pronom |
| changer le sujet (13) | 6 | je → elles, Karim → Salma | paragraphes entiers avec attributs, possessifs, pronom repris |
| tout et participe passé (13) | 7 | « tout » adverbe, participe avec avoir | tout devant un féminin à voyelle, participe de souffrir, compatir |
| groupe nominal (11) | 3 | relative → adjectif, expansions | enrichir plusieurs GN d'un paragraphe selon une indication |

**Compréhension** : le 09 n'a aucune question sur un texte officiel ; ses textes sont inventés et courts.
**Production** : le 08 et le 09 enseignent thèse, arguments, schéma narratif, portrait ; aucun ne part
d'une consigne d'examen. Le 04 n'a aucune question d'examen (le discours rapporté n'est demandé qu'en
production) ; le 15 non plus. **Le 10 (sujets types)** reste tel quel : ses trois sujets sont inventés et
le plan ne compose pas de sujet complet (chaque question officielle a déjà sa mission).

**Bilan de l'écart** : 27 missions d'examen (plan v1), dont 5 de compréhension, 3 de production préparée et
19 de langue ; rien de ce que le patron pose déjà n'est redemandé ; aucune famille d'examen ne reste sans
mission. Les devoirs, lus en salle blanche, sont traités à part (§ 5 du plan, lot `L06`).

## 4. Mesures — à la lecture
