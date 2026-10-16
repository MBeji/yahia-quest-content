# Gisement 9ᵉ × français : plan des missions d'examen et du lot devoirs (G3–G4, étude 36)

Écrit le 2026-10-16 par le planificateur. Entrées : les 41 sujets lus (`C01`–`C42`, sans `C39` : 2004,
introuvable ; 2014 absente de l'archive), leurs transcriptions
(`content/programmes-officiels/examens-nationaux/9eme-base/french/`), les 226 lignes et les sept journaux de
`lecture-9eme/francais/`, les 45 lignes des huit devoirs (`lines/D0*.tsv`, `JOURNAL-lecture-devoirs.md`), le
contenu `content/french/` (15 chapitres au patron, publiés) et le manifeste `9eme-base.json`. Modèles : le
plan arabe (production convertie, compréhension par texte) et le plan SVT vague 2 (missions fusionnées,
liste « ne pas redemander »).

Sorties :

- carte et écart : `content/programmes-officiels/sources-externes/web-9eme-base-french/fiche.md` § 3
  (sujets officiels seulement) ;
- plan : [`plan-examens-v1.json`](./plan-examens-v1.json) — 27 missions d'examen (`m001`–`m027`, lots
  `L01`–`L05`), 6 missions de devoirs (lot `L06`, clé `devoirs`), et le sort de ce qui est écarté
  (`ecartes`, `devoirs.ecartes`) ;
- registre : `…/web-9eme-base-french/gisement.json` — 33 missions `planifiee` (id = la source de base,
  comme en SVT ; `sources` liste toutes les sources fusionnées ; `note` donne l'id du plan) ;
- affectations : [`assign-francais-L01.md`](./assign-francais-L01.md) … [`assign-francais-L05.md`](./assign-francais-L05.md),
  [`assign-francais-devoirs.md`](./assign-francais-devoirs.md).

Contrôle local (`content:gisement:controle`, contre les 41 transcriptions et les 8 snapshots de devoirs) :
0 plage de 8 mots partout (fiche, ce rapport, affectations) ; 0 plage de 6 mots sur la fiche ; contre les
devoirs, 0 plage de 6 mots partout (salle blanche tenue). Les plages de 6 à 7 mots des affectations d'examen
sont des phrases officielles citées à dessein (corpus officiel, reprise citée). Les « données communes » ne
sont que des années de session (2004, 2008, 2010…), que les textes citent aussi ; la partie de la fiche écrite
avant ce plan (§ 2) les déclenche déjà seule. Faux positif.

## 1. Règles retenues

**R1 — Langue : une mission par famille et par chapitre, sessions fusionnées.** Sur 144 questions de
langue, 19 familles reviennent d'une session à l'autre (négation, cause / but / intensité, pronom
relatif, futur antérieur, homophones…). Chaque famille donne **une** mission au chapitre de sa notion ; la
session la plus récente ou la plus riche sert de **base** (la mission en garde l'ordre), les autres
n'apportent que leurs variantes réelles. Chaque question **dit sa session** (« Examen 2022, générale ») et
redonne la phrase officielle. Titre : « 🏛️ Examens <années> · <sujet> » suivi des étoiles de l'étage.
Le placement suit le chapitre **le plus avancé** de la ligne dans l'ordre du manifeste (05 + 06 → 06 ;
13 + 12 → 13), avec deux exceptions déclarées : les relatives classées `11 + 02` par deux lecteurs vont au
02 avec les autres relatives (le 02 enseigne le choix du pronom selon la fonction, le 11 la relative comme
expansion) ; le mode après le verbe introducteur reste au 05 même quand la ligne dit `05 + 06` (c'est un
choix de mode, pas de temps).

**R2 — Compréhension : une mission par texte, cinq textes.** Les questions d'un texte ne se séparent pas.
Décision du pilote : cinq sessions récentes et représentatives, dont le texte intégral est transcrit —
générale 2026, 2025, 2023 ; technique 2026, 2024. La mission cite **une à deux phrases par question**, prises
dans la transcription ou le PDF officiel (URL au registre), jamais le texte entier. Les questions ouvertes
deviennent fermées : `multi` pour « relève deux indices », `matching` qualité ↔ indice ou sentiment ↔ indice,
QCM de la phrase justificative après une case cochée. Les 36 autres compréhensions sont écartées (§ 4).

**R3 — Production : convertie en préparation fermée, en trois missions groupées.** Elle vaut 6 ou 7 points
sur 20 et rien dans `content/french/` ne part d'une consigne d'examen ; l'écarter laisserait un tiers de
l'épreuve sans trace. Elle ne se note pas automatiquement : la mission redonne la consigne officielle et ne
demande que ce qui se décide **avant** d'écrire — la tâche exacte (récit + portrait, dialogue + thèse de
chacun, projet + raisons), l'argument ou la qualité pertinente (`multi`), l'action qui montre une qualité,
le verbe introducteur qui dit l'objection, la ponctuation du dialogue, le temps du récit et celui des
répliques, l'ordre du plan (`ordering`), la fin. Rien n'y note la rédaction. Les 41 consignes se rangent en
trois archétypes ; une mission par archétype évite 41 gabarits :
`m026` (récit avec dialogue, 10 sujets cités), `m027` (réussite, rencontre et portrait, 9 sujets cités et la
question de connecteurs temporels de 2024 T), `m006` (projet ou métier justifié, 5 sujets dont la lettre de
2011 T).

**R4 — Rien de ce que le patron, les quiz ou une autre mission posent déjà.** Le croisement est fait
question par question contre les 60 exercices et les 15 quiz de `content/french/` ; la note de chaque
mission nomme les questions à ne pas redemander (« 14/02 Q5 », « 06 quiz Q3 »…). Un item officiel dont le
geste et la variante sont déjà posés est écarté même si sa phrase est neuve (adverbe de « prudent », « On a
placé Saada », relatifs « qui / que / où » simples…).

**R5 — Placement des productions converties.** Par la règle du chapitre le plus avancé, les trois iraient au
09 (le 09 vient après le 04 et le 08 dans le manifeste). Elles vont au chapitre de **l'opération qu'elles
préparent** : le dialogue inséré dans un récit au 04 (cours : « Le dialogue dans le récit », « Le rôle du
dialogue dans le récit ») ; le récit et le portrait au 08 (« Le schéma narratif », « Le portrait ») ; la
justification d'un choix au 09 (« Justifier son point de vue »). Raisons : le 09 porte déjà les cinq
compréhensions, le 04 n'a aucune question d'examen sans cela, et le 08 enseigne exactement ces gestes.
Réversible : `m026` et `m027` peuvent passer au 09 sans autre changement que leur `nn`.

**R6 — Consignes ambiguës ou incohérentes : reformulées pour une seule réponse et déclarées dans
l'énoncé, ou écartées.**
- 2023 G, langue 2 b (passif sans agent → actif) : la seule réponse est avec « on » ; l'énoncé le dit (`m023`).
- 2009 T, langue 2 (verbes donnés à l'imparfait et au passé composé, à « mettre au futur simple ») : l'énoncé
  donne l'infinitif et le dit (`m014`).
- 2013 G, langue 2 b (« Je crois que l'enfant (être) heureux… » : présent ou futur) :
  l'énoncé situe l'action dans l'avenir, sinon l'item est écarté (`m013`).
- 2016 G, langue 4 (conjugaison du récit, cinq verbes, la consigne laisse choisir) : le passé simple et
  l'imparfait attendus sont uniques une fois le verbe isolé dans sa phrase (`m015`) ; la question 3 de la
  même session (« enrichissez… ») est reprise sans ambiguïté (`m011`).
- 2025 G, langue 2 b (but : deux phrases à sujets différents) : clé « pour que … y reviennent », sans
  ambiguïté ; 2021 G, langue 2 b (même sujet) : la clé est le groupe infinitif, dit dans l'explication (`m007`).
- 2022 T, langue 3 a (« qui a été confectionnée » → adjectif) : pas d'adjectif univoque, écarté.
- 2020 G, langue 2 b (subordonnant de temps à trouver) : plusieurs subordonnants conviennent ; QCM où un
  seul subordonnant de temps est proposé parmi des subordonnants d'autres rapports (`m010`).
- 2023 G, langue 1 et 3 b : « dans la cours » (coquille imprimée) se cite avec [sic] ; 2012 G, langue 3,
  « … t-il » (trait d'union imprimé fautif) aussi.
- **Futur antérieur** : au programme. `05-modes-et-temps-verbaux/chapter.json` le nomme (« du futur simple
  et du futur antérieur ») et le cours lui consacre la section « Le futur simple et le futur antérieur » ;
  les doutes des lecteurs (C07, C29) tombent. La mission (`m016`) est au 06 parce que le choix dépend de
  l'ordre de deux actions.

**R7 — Taille, étage, en-tête.** 6 à 12 questions ; une consigne ouverte devient une ou plusieurs questions
fermées sur les phrases de la session. Étage = celui de la ligne la plus haute de la mission, jamais d1 (d1
→ d2) ; les productions converties sont d3 (on n'y rédige plus). En-tête : d2 practice 75/15, d3 boss 120/30.
Bilan : 17 d2, 10 d3 ; environ 260 questions d'examen et 45 de devoirs.

**R8 — Reprise et citation.** Sujets officiels (corpus officiel, R-2) : reprise fidèle des phrases et des
consignes. `chapter.json`, `sources[]` de chaque chapitre touché : « Sujets officiels de l'examen national
de fin d'études de l'enseignement de base (9ᵉ), Ministère de l'Éducation (corpus officiel, reprise citée,
étude 36) — transcriptions : programmes-officiels/examens-nationaux/9eme-base/french/ ». Barèmes décimaux
sans objet pour les missions. Étiquettes d'erreur : lire sur `origin/main` les `fr.*` existantes (par
exemple `fr.temps.passe-simple-imparfait`) avant d'en employer une ; sinon distracteurs muets et erreurs
décrites au rapport.

## 2. Missions par chapitre

| chapitre | NN | mission | sources (base en premier) | étage | q. |
| --- | --- | --- | --- | --- | ---: |
| `01-types-et-formes-de-phrases` | 06 | m012 négation qui garde le sens | 2024 T ; 2023 T, 2017 T, 2015 T, 2012 T, 2011 T | d2 | 9 |
| `02-propositions-subordonnees` | 06 | m007 cause, but, conséquence d'intensité | 2024 G ; 2025 G, 2022 G, 2021 G, 2017 G, 2019 G, 2006, 2002 | d3 | 10 |
| `02` | 07 | m008 pronom relatif selon la fonction | 2018 G ; 2009 G, 2008, 2005, 2001, 2012 G, 2010 G | d3 | 10 |
| `02` | 08 | m009 dire la cause autrement | 2012 G ; 2009 G, 2001, 2003, 2013 G, 2013 T, 2021 T, 2019 T, 2010 T, 2009 T, 2002 | d2 | 10 |
| `02` | 09 | m010 temps et concession : subordonnée ou groupe | 2022 T ; 2020 G, 2019 T, 2017 G, 2013 G, 2003, 2007, 2002 | d3 | 9 |
| `03-voix-active-et-passive` | 06 | m023 de l'actif au passif et retour | 2023 G ; 2016 G, 2015 G, 2011 G, 2010 G, 2008, 2007 | d2 | 11 |
| `04-discours-direct-et-indirect` | 06 | m026 production préparée : récit avec dialogue | 2025 G ; 2023 G, 2022 G, 2021 G, 2015 G, 2013 G, 2012 G, 2010 G, 2009 G, 2002 | d3 | 10 |
| `05-modes-et-temps-verbaux` | 06 | m013 le mode après le verbe introducteur | 2017 G ; 2018 G, 2013 G, 2010 G, 2006, 2003, 2005 | d3 | 11 |
| `05` | 07 | m014 transposer : présent, imparfait, futur | 2015 T ; 2013 T, 2012 T, 2011 T, 2016 T, 2009 G, 2010 T, 2009 T | d2 | 10 |
| `06-concordance-des-temps` | 06 | m015 imparfait, passé simple, plus-que-parfait | 2024 G ; 2022 G, 2021 G, 2016 G, 2010 G, 2020 G, 2026 G, 2015 G, 2023 G, 2012 G | d2 | 12 |
| `06` | 07 | m016 futur simple ou futur antérieur | 2025 G ; 2026 G, 2023 G, 2020 G, 2019 G, 2015 G, 2011 G, 2006 | d3 | 10 |
| `06` | 08 | m017 présent ou passé composé | 2026 T ; 2025 T, 2020 T, 2019 T, 2017 T, 2007, 2002 | d2 | 9 |
| `07-lexique-et-figures-de-style` | 06 | m018 sens d'un mot en contexte | 2026 T ; 2025 T, 2024 T, 2023 T, 2021 T, 2020 T, 2019 T, 2018 T | d2 | 12 |
| `07` | 07 | m019 synonyme en contexte et autre sens | 2024 G ; 2022 T, 2026 G, 2025 G, 2023 G, 2022 G, 2021 G, 2020 G, 2019 G, 2018 G, 2016 G, 2016 T, 2015 G | d2 | 10 |
| `08-types-de-textes-et-production-ecrite` | 06 | m027 production préparée : réussite et portrait | 2026 G ; 2026 T, 2024 G, 2024 T (+ langue 2), 2020 G, 2018 G, 2023 T, 2007, 2005 | d3 | 10 |
| `09-comprehension-production-ecrite` | 06–10 | m001–m005 compréhension, un texte chacune | 2026 G, 2025 G, 2023 G, 2026 T, 2024 T | d2 | 7–8 |
| `09` | 11 | m006 production préparée : projet ou métier justifié | 2025 T ; 2019 G, 2015 T, 2009 T, 2011 T | d3 | 9 |
| `11-groupe-nominal-et-attribut` | 06 | m011 enrichir le groupe nominal | 2026 G ; 2016 G, 2022 T | d3 | 8 |
| `12-reprises-et-pronoms-complements` | 06 | m022 le pronom qui remplace le groupe | 2006 ; 2003, 2001, 2008, 2011 G, 2011 T, 2012 T, 2016 T, 2017 T, 2015 T, 2010 T, 2021 T | d2 | 12 |
| `13-les-accords` | 06 | m024 changer le sujet et accorder | 2025 T ; 2026 T, 2023 T, 2018 T, 2007, 2020 T | d3 | 8 |
| `13` | 07 | m025 « tout » et participe passé | 2015 G ; 2012 G, 2006, 2003, 2013 G, 2001, 2005 | d2 | 11 |
| `14-homophones-et-adverbes-en-ment` | 06 | m020 former l'adverbe en -ment | 2025 G ; 2024 G, 2023 G, 2017 G, 2005, 2002 | d2 | 10 |
| `14` | 07 | m021 homophones en contexte | 2026 G ; 2020 G, 2011 G, 2007, 2022 G, 2013 G, 2021 G, 2019 G, 2018 G, 2009 G, 2008 | d2 | 12 |
| `10`, `15` | — | aucune mission d'examen | `10` : sujets types inventés, pas de sujet complet recomposé (chaque question officielle a déjà sa mission) ; `15` : une seule production (lettre, 2011 T), versée dans `m006` | | |

**27 missions d'examen, environ 260 questions**, tirées de 41 sujets : chaque famille de langue posée par les
examens a sa mission, aucune ne répète une autre ni le patron.

## 3. Lots

| lot | chapitres (NN) | missions | parallélisme |
| --- | --- | --- | --- |
| L01 | `09` (06–11) | m001–m006 (6) | avec L02–L05 |
| L02 | `02` (06–09), `11` (06), `01` (06) | m007–m012 (6) | avec L01, L03–L05 |
| L03 | `05` (06–07), `06` (06–08) | m013–m017 (5) | avec L01, L02, L04, L05 |
| L04 | `07` (06–07), `14` (06–07), `12` (06) | m018–m022 (5) | avec L01–L03, L05 |
| L05 | `03` (06), `13` (06–07), `04` (06), `08` (06) | m023–m027 (5) | avec L01–L04 |
| L06 (devoirs) | `02` (10–11), `06` (09), `03` (07), `15` (06), `11` (07) | 6 | **après** L02, L03 et L05 (mêmes chapitres : un auteur à la fois) |

Chapitres disjoints entre L01 et L05 : cinq auteurs en parallèle, puis L06. Skill : `prof-francais-9eme`
puis `content-ecole-tn` ; consigne : `gisement-auteur-examen.md` (L01–L05, reprise citée, avec la
transcription de chaque session citée) et `gisement-auteur-devoir.md` (L06, salle blanche : l'auteur ne
reçoit que les cartes, jamais un devoir).

**Pour les prompts d'auteur** (repartir du prompt SVT vague 2, en changeant) :
1. la ligne d'affectation dit ce qui est fusionné, gardé et écarté (« consigne de tri ») : l'auteur lit les
   questions désignées, pas le sujet entier ;
2. chaque question d'une mission fusionnée nomme sa session et redonne la phrase officielle ; une mission de
   compréhension cite une à deux phrases par question, jamais le texte entier, avec la référence de l'œuvre
   telle qu'imprimée ;
3. liste « ne pas redemander » de chaque ligne, à vérifier sur `origin/main` ;
4. reformulation déclarée dans l'énoncé (R6) et reportée au rapport ; coquilles imprimées citées avec [sic] ;
5. types natifs là où la consigne l'appelle : `multi` (« relève deux… »), `matching` (qualité ↔ indice),
   `ordering` (plan d'une production, ordre d'un récit) ; `short_answer` seulement pour une forme unique
   (un adverbe, un pronom), avec ses `acceptedAnswers` ;
6. gates `content:gates -- --tranche`, `CATALOGUE.md` régénéré.

## 4. Ce qui est écarté, et pourquoi

Le détail machine est dans `plan-examens-v1.json` (`ecartes`, `devoirs.ecartes`).

| écarté | quoi | pourquoi |
| --- | --- | --- |
| 36 compréhensions | tous les textes sauf 2026 G, 2025 G, 2023 G, 2026 T, 2024 T | R2 : mêmes consignes d'un texte à l'autre ; avant 2011 et en 2015–2017, le texte n'est transcrit qu'en résumé |
| les productions non citées | sujets qui répètent un des trois archétypes | R3 : trois missions groupées citent les sujets représentatifs |
| 2022 T, langue 3 a | relative → adjectif sans équivalent univoque | R6 |
| 2003, langue 3 b | « si » + imparfait → conditionnel | 05/01 Q5, 02 quiz Q5 |
| 2011 G, langue 1 a | « On a placé… » → passif | 01/04 Q6 |
| négations de « encore » de 2023 T et 2012 T | répètent 2024 T b | 01/04 Q4 |
| relatifs simples (2018 T ; 2001 a ; 2010 G a) | qui, que, où | 02/01, 02/05 Q5, 11/02 Q2 |
| adverbes de « prudent » (2023 G) et « élégant » (2002) | — | 14 quiz Q3, 14/02 Q5 |
| mots à placer d'une liste (2013 T, 2009 T, langue 1) | texte à trous de vocabulaire | aucun lexique neuf, simple lecture du paragraphe |
| synonymes transparents | inventés, emmenions, haussa, ai regardé, doucement ; pupitre, confectionner | aucun piège de sens ; taille de `m018`–`m019` |
| blancs d'homophones simples | « Quand » en tête, « quel » + nom | une vingtaine au patron 14 |

## 5. Le lot devoirs (L06, salle blanche)

Huit devoirs lus (45 lignes). Le lecteur compte 19 signatures neuves sur 45 par rapport aux sujets
d'examen ; **par rapport au plan d'examens ET au contenu existant**, il en reste six vraiment neuves, une
mission chacune (cartes dans mes mots, `assign-francais-devoirs.md`) :

| carte(s) | chapitre (NN) | ce qui est neuf | étage |
| --- | --- | --- | --- |
| D01#3 + D01#4 + D03#4 | `02` (10) | classer des expressions de temps par rapport, puis groupe infinitif ou nominal → subordonnée avec dès que / après que / avant que, au bon mode | d3 |
| D05#2 + D05#3 + D08#4 + D08#3 | `02` (11) | but ou crainte, complément de but → subordonnée, « sous prétexte que » construit, corrélation | d2 |
| D03#6 + D02#5 + D06#3 | `06` (09) | pendant que / avant que (indicatif / subjonctif), imparfait ou plus-que-parfait d'antériorité, valeur du conditionnel | d2 |
| D07#3 + D04#3 | `03` (07) | trier une série mêlée (passivable ou non) puis transformer | d2 |
| D06#4 + D04#6 | `15` (06) | lettre argumentative à un ami et article sur un exploit, en préparation fermée | d3 |
| D03#3 + D02#3 + D03#2 + D02#4 | `11` (07) | une expansion sous trois formes (complément du nom, relative, adjectif), nature et fonction | d2 |

Écartés des devoirs : **les adjectifs de couleur** (D02#6, D03#5) — le patron 13 en pose déjà six questions,
composés et noms de couleur compris ; la personnification (D08#2 : 07 quiz Q5, 07/04 Q5) ; synonymes et
mots à choisir (07 : `07/06`–`07/07`) ; subjonctif après le verbe principal (`05/06`) ; futur antérieur
(`06/07`) ; homophones et adverbes (`14/06`–`14/07`) ; reprises (patron 12) ; but, cause, conséquence
(`02/06`) ; « tout » (`13/07`) ; les essais de portrait et d'exploit (`08/06`) ; les huit compréhensions
(textes de devoirs, non repris).

**Une vague 2 de devoirs vaut-elle la peine ? Non.** La règle des 30 % (D-4) compte les signatures neuves
par rapport aux examens ; rapportée à ce que le plan et le patron couvrent, la vague 1 n'apporte que 6
missions sur 45 lignes (≈ 13 %), et ce qui reste rare aux examens (négation, discours rapporté, 04, 08, 15)
est enseigné au patron et repris par `m012`, `m026`, `m027` et la carte `15/06`. Le seul trou réel serait le
discours indirect en exercice de langue, qu'aucun examen ne demande depuis 2001 : il ne justifie pas une
vague de neuf devoirs. À rouvrir seulement si l'audit des missions trouve un chapitre sans matière.

## 6. Arbitrages pour le propriétaire

Aucun ne bloque l'écriture ; chacun est réversible lot par lot.

1. **La production convertie (R3)** plutôt qu'écartée : trois missions (`m006`, `m026`, `m027`) et la carte
   devoir `15/06`. Si le propriétaire préfère l'écarter, ces quatre missions tombent sans toucher au reste.
2. **Le placement des productions au 04 et au 08 (R5)** plutôt qu'au 09 par la règle du chapitre le plus
   avancé.
3. **Cinq compréhensions seulement (R2).** Une mission par texte pour les 41 sujets donnerait 41 missions de
   même gabarit ; une seconde vague sur les textes 2018–2022 (texte intégral transcrit) reste possible si
   l'usage montre que les élèves les redemandent.
