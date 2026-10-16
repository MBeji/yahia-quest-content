# Gisement 9ᵉ × anglais : plan des missions d'examen et du lot devoirs (G3–G4, étude 36) — v2

> **v2 (2026-10-16)** : décisions du pilote sur le § 6 — P1, P2, P3 acceptées (lot **L06** au 07 : trois
> textes de cours, trois puces du résumé, missions `m022`–`m024`) ; pas de vague 2 de devoirs ; passif écarté ;
> nommage 06/07 du manifeste inchangé (suivi du propriétaire). Les cartes L01–L04 ne changent pas ; seule la
> carte devoirs `D04#4` (L05) voit sa liste « ne pas redemander » renvoyer à `m022`, `m024`.

Écrit le 2026-10-16 par le planificateur. Entrées : les 41 sujets lus (`C01`–`C42`, sans `C39` : 2004,
introuvable ; 2014 absente de l'archive), leurs transcriptions
(`content/programmes-officiels/examens-nationaux/9eme-base/english/`, texte support résumé, texte intégral au PDF
officiel), les 205 lignes et les quatre journaux de `lecture-9eme/anglais/`, les 29 lignes des six devoirs
(`lines/D0*.tsv`, `JOURNAL-lecture-devoirs.md`), le contenu `content/english/` (10 chapitres au patron, publiés),
le manifeste `9eme-base.json` et la fiche programme `programme/9eme-base/anglais.md`. Modèle : le plan français
(même dossier parent, `francais/`).

Sorties :

- carte et écart : `content/programmes-officiels/sources-externes/web-9eme-base-english/fiche.md` § 3
  (sujets officiels seulement) ;
- plan : [`plan-examens-v2.json`](./plan-examens-v2.json) (v1 gardé pour l'historique) — 24 missions d'examen
  (`m001`–`m024`, lots `L01`–`L04` et `L06`), les textes de cours du lot L06 (`coursL06`), 2 missions de devoirs (lot `L05`, clé `devoirs`), le sort de ce qui est écarté (`ecartes`,
  `devoirs.ecartes`) et les trois propositions soumises au pilote (`propositionsPilote`) ;
- registre : `…/web-9eme-base-english/gisement.json` — 26 missions `planifiee` (id = la source de base ;
  `sources` liste toutes les sources fusionnées ; `note` donne l'id du plan) ; la section `documents` n'est pas
  touchée ;
- affectations : [`assign-anglais-L01.md`](./assign-anglais-L01.md) … [`assign-anglais-L04.md`](./assign-anglais-L04.md),
  [`assign-anglais-L06.md`](./assign-anglais-L06.md) (cours et missions du 07), [`assign-anglais-devoirs.md`](./assign-anglais-devoirs.md).

Contrôle local : voir § 8.

## 1. Règles retenues

**R1 — Langue : une mission par famille et par chapitre, sessions fusionnées, au grain de l'item.** Un
exercice de langue anglais n'a pas de famille : un même texte lacunaire teste un temps, un degré, un relatif,
une préposition et trois mots du domaine. Le tri se fait donc **blanc par blanc** : chaque item au programme
rejoint la mission de sa famille, au chapitre de sa notion ; les autres blancs du même texte vont ailleurs ou
sont écartés (la consigne de tri le dit). Douze familles reviennent d'une session à l'autre ; chacune donne une
mission ; la session la plus récente ou la plus riche sert de **base** (la mission en garde l'ordre). Chaque
question **dit sa session** (« Exam 2015, general ») et **redonne la phrase officielle** avec UN blanc, jamais le
texte entier. Titre : « 🏛️ Exams <années> · <sujet en anglais> » (une seule session : « 🏛️ Exam <année>
general|technical · … »), suivi des étoiles de l'étage ; tout le texte visible est en anglais, comme les
exercices publiés. Placement au chapitre **le plus avancé** de la notion testée par l'item (pas de la ligne
entière, qui mêle les notions), avec ces exceptions déclarées : `m006` (accord du présent) reprend un item de deux
lignes que le lecteur range en 09 ; `m010` (will et if) réunit 03 et 05 au 05 ; les deux questions de valeur d'un
modal en compréhension (2023 T, 2013 G) vont à `m011` (04) parce que leur texte n'a pas de mission.

**R2 — Reading : une mission par texte, cinq textes.** Générale 2026, 2025, 2024 ; technique 2026, 2024 :
les plus récents, les cinq gabarits de questions (vrai/faux, tableau, expression imagée, valeur d'un modal,
tableau de dates). La mission cite **une à deux phrases par question**, prises dans le PDF officiel (URL et
sha256 au registre ; copie de lecture locale hors git sous `/tmp/claude-0/enlec/snapshots/`), jamais le texte
entier. Questions ouvertes converties en fermées : vrai/faux → choix puis phrase qui le prouve ; tableau →
`matching` ; « pick out » → QCM de mots du paragraphe désigné ; réponse personnelle → `multi` des raisons que
le texte fonde, **sans noter la forme verbale** du cadre « If I were… » (décision du pilote : ce n'est pas un
conditionnel enseigné, le 2ᵉ conditionnel n'est pas au programme). Les 36 autres textes sont écartés (§ 4).

**R3 — Writing : converti en préparation fermée, quatre archétypes, une mission chacun.** La production
vaut 5 ou 6 points sur 20 et rien dans `content/english/` ne part d'une consigne d'examen. La mission redonne la
consigne officielle et ne demande que ce qui se décide **avant** d'écrire : la tâche exacte (conseiller,
mettre en garde, raconter, décrire, persuader), les arguments ou détails pertinents (`multi`), le modal ou le
temps attendu, l'ordre du plan (`ordering`), la formule d'une lettre ou d'un courriel telle qu'imprimée,
l'anonymat. Rien n'y note la rédaction. Archétypes : conseil, mise en garde et règles (`m012`) ; récit au passé
(`m009`) ; description, persuasion, avis (`m020`) ; lettre et courriel (`m021`).

**R4 — Rien de ce que le patron, les quiz ou une autre mission posent déjà.** Croisement question par
question contre les 41 exercices et les 10 quiz de `content/english/` ; la note de chaque mission nomme les
questions à ne pas redemander (« 02/02 Q3 », « 08 quiz Q4 »…). Le patron n'a que des QCM sur phrases inventées :
ce qui manque partout est la phrase officielle, le texte lacunaire, l'appariement, la consigne de production.
Un item officiel dont le geste est déjà représenté douze fois dans sa mission est écarté.

**R5 — Placement des productions converties.** Au chapitre de l'opération préparée, déclaré : conseiller,
avertir, fixer des règles → 04 (modaux de conseil, d'obligation, d'interdiction) ; raconter au passé → 02 ;
sinon → 09 (description, persuasion, lettre).

**R6 — Consignes ambiguës : reformulées pour une seule réponse et déclarées, ou écartées.**
- 2022 G, exercice 3 (« Recently, … (launch) ») : prétérit et present perfect justes tous deux → écarté.
- 2016 G, exercice 3 (« (wastes / raises / earns) … dollars a year ») : « earns » se défend → écarté.
- 2008, exercice 2 (blanc ⓔ, trois degrés proposés) : l'option « the least » est grammaticale mais
  dément le sens de la phrase ; clé unique par le sens, dit dans l'explication (`m014`).
- 2018 T, exercice 3 (« for / since fourteen years ») : for / since n'est pas un point du cours 02 ;
  l'explication donne la règle en une phrase, déclarée au rapport (`m007`).
- 2021 G, exercice 1 (banque à « if » et « unless ») : « unless » n'est qu'en « Going further » du cours 05 ;
  l'explication dit pourquoi il renverserait le sens, sans règle posée (`m010`).
- 2024 T, « Los Angles », 2010 T, « fourty-five », 2026 G/T, « DOT NOT » : coquilles imprimées citées avec
  [sic], jamais reproduites dans une option.

**R7 — Notions hors chapitres (tranché par le pilote, v2).** Le gérondif (et verbe + to + base), les pronoms
(compléments, réfléchis, possessifs) et la dérivation vont au **07** (contenu publié « Word Building & Linking
Words »), lot **L06** seul : trois textes de cours puis trois missions (`m022`–`m024`). Dans les lots L01–L05,
un item de ces familles n'est jamais la cible d'une question : il est laissé à L06, ou sa forme est donnée dans
l'énoncé quand la phrase sert une autre question. Le passif (non enseigné) est écarté.

**R8 — Taille, étage, en-tête, reprise.** 12 questions au plus ; étage = celui de la ligne la plus haute de la
mission, jamais d1 (d1 → d2), d3 au plus. En-tête : d2 practice 75/15, d3 boss 120/30. Bilan : 17 d2, 7 d3 ;
environ 250 questions d'examen et 16 de devoirs. `chapter.json`, `sources[]` de chaque chapitre touché :
« Sujets officiels de l'examen national de fin d'études de l'enseignement de base (9ᵉ), Ministère de
l'Éducation (corpus officiel, reprise citée, étude 36) — transcriptions :
programmes-officiels/examens-nationaux/9eme-base/english/ ». Étiquettes : la famille `english.*` de
`content/misconceptions.json` sur `origin/main` (par exemple `english.tense.present-perfect-avec-temps-fini`,
`english.modal.to-en-trop`, `english.rel.who-et-which-confondus`, `english.comp.superlatif-sans-the`) ; sinon
distracteurs muets décrits au rapport. Types natifs : `matching` (tableaux, appariements), `ordering` (plan,
ordre des faits), `multi` (« relève deux… », arguments) ; `short_answer` seulement pour une forme unique
(« spent », « more fashionable »), avec ses `acceptedAnswers`.

## 2. Missions par chapitre

| chapitre | NN | mission | sources (base en premier) | étage | q. |
| --- | --- | --- | --- | --- | ---: |
| `01-present-tenses` | 06 | m006 present simple or continuous | 2021 G ; 2019 G, 2015 T, 2013 G, 2012 T, 2011 G, 2011 T, 2010 T, 2006, 2001 | d2 | 12 |
| `02-past-tenses` | 06 | m007 present perfect or simple past | 2024 G ; 2026 T, 2020 G, 2018 G, 2018 T, 2017 T, 2016 T, 2013 T, 2012 G, 2010 T, 2009 T, 2006 | d2 | 12 |
| `02` | 07 | m008 telling the past: simple past or past progressive | 2026 G ; 2025 G, 2024 G, 2024 T, 2023 T, 2021 T, 2019 T, 2016 G, 2015 G, 2010 T, 2005, 2001 | d3 | 12 |
| `02` | 08 | m009 writing prepared: telling a past event | 2023 T ; 2002 | d2 | 8 |
| `04-modals` | 06 | m011 modals: meaning and form | 2022 T ; 2023 T (reading), 2013 G (reading), 2017 G, 2017 T, 2015 T, 2012 T, 2009 G, 2005, 2001 | d2 | 11 |
| `04` | 07 | m012 writing prepared: advise, warn, set rules | 2026 G ; 2026 T, 2024 G, 2022 T, 2019 G, 2016 T, 2011 T, 2009 G | d3 | 11 |
| `05-conditionals` | 06 | m010 will and if | 2018 G ; 2021 G, 2012 G, 2008 | d2 | 6 |
| `08-relative-clauses-comparatives` | 06 | m013 relative pronouns: who, which, that | 2026 G ; 2025 T, 2024 G, 2021 T, 2012 T, 2011 G, 2003, 2002 | d2 | 8 |
| `08` | 07 | m014 comparative or superlative: read the clue | 2025 G ; 2024 T, 2023 G, 2022 T, 2021 G, 2019 G, 2017 G, 2016 G, 2011 G, 2010 G, 2008, 2002 | d2 | 12 |
| `08` | 08 | m015 building the comparison | 2025 G ; 2026 G, 2021 G, 2016 G, 2016 T, 2015 G, 2011 G, 2009 G, 2006, 2005, 2002 | d3 | 12 |
| `09-reading-comprehension-writing` | 06–10 | m001–m005 reading, un texte chacune | 2026 G, 2025 G, 2024 G, 2026 T, 2024 T | d2 | 6–10 |
| `09` | 11 | m016 the right preposition | 2026 T ; 2026 G, 2025 G, 2023 G, 2022 T, 2021 G, 2020 T, 2019 G, 2019 T, 2015 T, 2013 G | d2 | 12 |
| `09` | 12 | m017 linking words | 2023 T ; 2026 G, 2023 G, 2020 G, 2020 T, 2019 T, 2018 T, 2013 T, 2009 G, 2007, 2006 | d2 | 12 |
| `09` | 13 | m018 the right word in context | 2026 T ; 2026 G, 2025 G, 2025 T, 2024 G, 2024 T, 2023 G, 2022 G, 2021 G, 2020 G, 2019 G, 2018 G | d2 | 12 |
| `09` | 14 | m019 matching sentence parts | 2026 G ; 2025 T, 2024 T, 2021 G, 2018 G, 2015 G, 2013 T, 2006, 2003, 2001 | d2 | 10 |
| `09` | 15 | m020 writing prepared: describe, persuade, opinion | 2025 G ; 2025 T, 2021 G, 2021 T, 2020 G, 2017 G, 2015 G, 2001 | d3 | 10 |
| `09` | 16 | m021 writing prepared: letters and e-mails | 2019 T ; 2018 T, 2013 T, 2012 G, 2011 G, 2010 T, 2007, 2005, 2009 G | d3 | 12 |
| `07-reported-speech` | 06 | m022 the gerund or to + base | 2025 T ; 2025 G, 2024 T, 2023 T, 2022 G, 2022 T, 2019 T, 2018 G, 2016 T, 2015 G, 2003, 2002 | d3 | 12 |
| `07` | 07 | m023 pronouns: object, reflexive, possessive | 2023 T ; 2021 T, 2021 G, 2019 G, 2018 T, 2015 G, 2013 T, 2012 T, 2010 G, 2009 T, 2007 | d2 | 12 |
| `07` | 08 | m024 one root, several words | 2022 G ; 2026 G, 2026 T, 2025 G, 2025 T, 2024 T, 2022 T, 2019 G, 2018 G, 2011 G | d3 | 12 |
| `03`, `06`, `10` | — | aucune mission d'examen | `03` : deux items de futur, versés dans `m010` ; `06` : les trois passifs sont hors programme (§ 4) ; `10` : sujets types inventés, le plan ne compose pas de sujet complet | | |

**24 missions d'examen, environ 250 questions**, tirées des 41 sujets : chaque famille au programme a sa mission,
aucune ne répète une autre ni le patron.

## 3. Lots

| lot | chapitres (NN) | missions | parallélisme |
| --- | --- | --- | --- |
| L01 | `09` (06–10) | m001–m005 (5) | avec L02, L03 |
| L02 | `01` (06), `02` (06–08), `05` (06) | m006–m010 (5) | avec L01, L03 |
| L03 | `04` (06–07), `08` (06–08) | m011–m015 (5) | avec L01, L02 |
| L04 | `09` (11–16) | m016–m021 (6) | **après** L01 (même chapitre : un auteur à la fois) ; en parallèle de L02, L03 |
| L05 (devoirs) | `08` (09), `09` (17) | 2 | **après** L03 et L04 |
| L06 | `07` : cours (C1–C3), résumé (R1–R3), missions (06–08) | m022–m024 (3) + cours | avec tous les autres (seul lot au 07) ; cours **avant** missions |

Skill : `prof-anglais-9eme` puis `content-langue-anglais` et `content-ecole-tn` ; consigne :
`gisement-auteur-examen.md` (L01–L04, reprise citée, avec la transcription de chaque session citée) et
`gisement-auteur-devoir.md` (L05, salle blanche : l'auteur ne reçoit que les cartes, jamais un devoir). Le lot
L05 n'a que deux missions : la vague 1 n'apporte pas plus (§ 5).

## 4. Ce qui est écarté, et pourquoi

Le détail machine est dans `plan-examens-v2.json` (`ecartes`, `devoirs.ecartes`).

| écarté | quoi | pourquoi |
| --- | --- | --- |
| 36 compréhensions | tous les textes sauf 2026 G, 2025 G, 2024 G, 2026 T, 2024 T | R2 : mêmes consignes d'un texte à l'autre ; les deux valeurs de modal utiles passent dans `m011` |
| 16 productions | sujets qui répètent un des quatre archétypes | R3 |
| passif (2025 G, 2017 T, 2025 T) | can be found, considered, gets educated | non enseigné en 9ᵉ ; le 06 publié enseigne les fonctions ; 3 sessions |
| dérivation, gérondif, pronoms non retenus | items de suffixe ou de pronom déjà représentés ; « doing » (participe) | `m022`–`m024` en gardent douze chacune |
| let … cross (2002) | let + base | non enseigné (decide / need + to + base sont dans `m022`, cours C1) |
| what / where / who interrogatifs (2023 G, 2026 T) | relatifs libres ou mots interrogatifs | seuls who / which / that sujets sont au programme |
| « so that he would » (2024 G) | would de but | non enseigné |
| « used to » (2010 G) | used to + base | non enseigné en 9ᵉ ; la question de sens de 2024 T reste dans `m005` sans règle |
| « Recently … (launch) » (2022 G), « raises / earns » (2016 G) | — | R6 |
| dialogue de répliques (2002) | fonctions de communication | une session ; fonctions posées par le patron 06 |
| items de même geste | une soixantaine de prépositions, une centaine de choix lexicaux, 27 appariements, prétérits et participes répétés | R4 et taille : chaque geste a déjà douze items |

## 5. Le lot devoirs (L05, salle blanche)

Six devoirs lus (29 lignes ; plafond de deux par auteur tenu : D04 et D05 pour le seul auteur double). Les blocs
d'écoute (D01#1, D03#1, D05#1) ne donnent rien (décision du pilote). Par rapport au plan d'examens ET au
contenu existant, deux signatures sont vraiment neuves, une mission chacune (cartes dans mes mots,
`assign-anglais-devoirs.md`) :

| carte(s) | chapitre (NN) | ce qui est neuf | étage |
| --- | --- | --- | --- |
| D04#1 + D06#1 + D02#1 | `09` (17) | reconnaître le type de texte, corriger une affirmation fausse par le détail juste, transférer dans un tableau, dégager la cause principale | d2 |
| D04#4 + D05#5 + D01#4 + D02#4 | `08` (09) | un même texte où verbes et adjectifs entre parenthèses prennent le temps et le degré qu'exigent les repères (parties de dérivation et de gérondif non reprises, R7) | d3 |

Écartés des devoirs : les textes à trous à banque et les choix d'options (même geste que `m006`–`m008`,
`m014`, `m016`–`m018`), les appariements (`m019`), le courriel de conseils et le discours de mise en garde
(`m012`), la présentation d'une organisation à partir d'images (`m020` ; les images ne passent pas), la
participiale et le participe passif de D03 (hors programme).

**Mesure des signatures neuves (règle des 30 %, D-4).** Signature = famille d'archétype + chapitres de la
ligne (jetons `HP:` ôtés), comparée aux 205 lignes d'examen : **8 signatures neuves sur 29 lignes (28 %)**, dont
3 sont les écoutes ; **hors écoute, 5 sur 26 (19 %)**. Rapportées au plan et au patron, il en reste **2 sur 26
(8 %)**. Sous le seuil de 30 % dans les trois comptes : **pas de vague 2** (décision du pilote, v2). Pour une
vague 2, le plafond exclut Fraoua ; l'alternance pilote / ordinaire a été rompue (D04 et D05 sont d'un collège
pilote d'après leur en-tête, le registre dit ordinaire).

## 6. Notions hors chapitres — tranché par le pilote (v2, 2026-10-16)

Constat (v1) : les slugs `06-passive-voice` et `07-reported-speech` portent « Communicative Functions » et
« Word Building & Linking Words » ; les lecteurs ont jeté `HP:` des notions que le 07 publié enseigne. Le
manifeste n'est pas touché (suivi du propriétaire). Décisions :

| | famille | sessions | décision | réalisation (lot L06, `assign-anglais-L06.md`) |
| --- | --- | ---: | --- | --- |
| **P1** | gérondif + verbe + to + base | 12 | acceptée | cours C1 (bloc `propriete` dans « The gerund » : decide / want / need / hope / learn / would like + to + base ; SB p. 97 et p. 52), résumé R3 ; mission `m022` (07/06, d3, 12 q.) |
| **P2** | pronoms compléments, réfléchis, possessifs | 13 | acceptée | cours C2 (tableau sujet / complément / réfléchi et paragraphe ; SB p. 33 et p. 38), résumé R1 ; mission `m023` (07/07, d2, 12 q.) |
| **P3** | dérivation | 15 | acceptée, section limitée aux suffixes exigés | cours C3 (section « One root, several words », entre Compound nouns et The gerund ; ligne 🎯 qui cite l'examen comme source de l'exigence ; SB p. 78), résumé R2 ; mission `m024` (07/08, d3, 12 q.) |

Suffixes que les sujets exigent réellement (et seuls retenus dans C3) : nom **-ment** (2025 G, 2025 T), **-tion**
(2024 T), **-er / -ist** de personne (2026 T, 2026 G) ; adjectif **-al** (2026 G, 2019 G, 2010 G), **-ful**
(2011 G), **-ous** (2022 G), **-ing / -ed** (2022 G, 2020 G, 2013 G, 2025 T) ; adverbe **-ly** (2025 G, 2023 G,
2022 G, 2011 G) ; changements de forme choose → choice (2022 T), advise → advice (2018 G), beauty → beautiful
(2022 G). Aucun sujet ne demande -ness, -ity ou -able.

Passif (3 sessions) et fonction de communication en langue (1) : écartés.

## 7. Arbitrages pour le propriétaire

Aucun ne bloque l'écriture ; chacun est réversible lot par lot.

1. **Le libellé des chapitres 06 et 07 au manifeste** (« Passive voice », « Reported speech ») ne dit pas leur
   contenu publié : suivi noté par le pilote, rien n'est changé ici.
2. **La production convertie (R3)** plutôt qu'écartée : quatre missions (`m009`, `m012`, `m020`, `m021`) ; leur
   placement (R5) au 02 et au 04 est réversible par leur seul `nn`.
3. **Cinq compréhensions seulement (R2).**
4. **La section C3 va au-delà du manuel** (suffixes) : déclarée par sa ligne 🎯 ; à retirer avec `m024` si le
   propriétaire s'en tient au manuel.

## 8. Contrôle local

`content:gisement:controle` (moteur `/home/user/eng-svtses`), le 2026-10-16, sur la fiche, ce plan, les quatre
affectations d'examen et l'affectation des devoirs :

- **contre les six snapshots de devoirs** (`/tmp/claude-0/devoirs-snapshots/english/`) : **0 plage de 8 mots**
  partout ; une plage de 6 mots sur la fiche (fragment de consigne d'examen, « in the right tense or form », que
  les devoirs reprennent de l'examen) ; 0 ailleurs. Les « données communes » signalées ne sont que des années de
  session (2008–2024), le barème 2.5 et les nombres 10 et 100 (2016 G, cité au registre des écarts) : faux
  positif, comme au français. Salle blanche tenue : aucune affectation de devoir ne porte une phrase, un contexte
  ou un nombre d'un devoir.
- **contre les 41 transcriptions** (copiées en `.txt` hors git) : fiche et plan, 0 plage de 8 mots, une plage
  de 6 (consigne citée sur la fiche ; intitulé de l'examen dans la ligne `sources[]` du plan) ; les affectations
  d'examen portent 4 à 33 plages de 8 mots chacune : ce sont les phrases officielles citées à dessein (corpus
  officiel, reprise citée), que l'auteur doit retrouver ; l'affectation des devoirs, 0.
- `content:check` et `content:qa -- --subject english` : verts (registre lu, garde anti-verbatim des fiches
  comprise).

**v2 (même jour, après les décisions du pilote)** : contre les snapshots de devoirs, **0 plage de 8 mots**
partout, `assign-anglais-L06.md` compris (0 plage de 6 : les textes de cours C1–C3 sont neufs) ; données
communes = années de session et nombres 10, faux positif. Contre les transcriptions : fiche et plan, 0 plage
de 8 mots ; `assign-anglais-L06.md`, 26 plages de 8 mots, toutes des phrases officielles citées à dessein dans
les consignes de tri (aucune dans les textes de cours). `content:check` et `content:qa -- --subject english`
verts.
