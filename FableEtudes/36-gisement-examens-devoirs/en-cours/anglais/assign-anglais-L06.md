# Lot L06 — chapitre `07-reported-speech` (contenu publié : « Word Building & Linking Words ») — plan v2

Décisions du pilote du 2026-10-16 sur le PLAN § 6 : P1, P2 et P3 acceptées. Un seul auteur pour le 07 (aucun
autre lot n'y touche : L06 tourne en parallèle de L01–L05). **Ordre imposé : d'abord les trois textes de cours
(C1–C3) et les deux lignes du résumé, puis les trois missions**, qui s'appuient sur eux. Les textes ci-dessous
sont à insérer **tels quels** (l'auteur ne corrige qu'une coquille évidente et la signale au rapport). Aucun
exemple du cours n'est un item d'examen : les missions ne reprennent ni ces exemples ni ces racines.

`chapter.json` du 07 : ajouter à `sources[]`, si elle manque, exactement « Sujets officiels de l'examen national
de fin d'études de l'enseignement de base (9ᵉ), Ministère de l'Éducation (corpus officiel, reprise citée,
étude 36) — transcriptions : programmes-officiels/examens-nationaux/9eme-base/english/ ». Rien d'autre (titre et
description inchangés ; l'écart de nommage 06/07 du manifeste est noté en suivi par le pilote, on n'y touche pas).

## Textes de cours

### C1 — `cours.md`, § « 🏊 The gerund » : verbe + to + base (P1)

Emplacement : entre la fin du bloc `::: methode` (orthographe des formes en -ing, se termine par la ligne
« Edge case: two vowels… (_play → playing_). » puis `:::`) et le début du bloc `::: verifie` de la même
section. Insérer, précédé et suivi d'une ligne vide :

```markdown
::: propriete
Not every verb takes the gerund. After **decide**, **want**, **need**, **hope**, **learn** and **would like**, the next verb takes **to + base**, as after **intend** (_I intend to study medicine_): _She decided **to join** the club._ — _We need **to buy** a new map._

Edge case: after a **preposition**, it is always the gerund, whatever the verb before: _She thought **of joining** the club._

:::
```

Puis remplacer le bloc `::: retenir` de la section (ligne « Gerund = verb + ing: subject, after like / enjoy /
finish / hate / dislike, after a preposition — double, drop the e, or no change. ») par :

```markdown
::: retenir
Gerund = verb + ing: subject, after like / enjoy / finish / hate / dislike, after a preposition — double, drop the e, or no change. But decide / want / need / hope / learn / would like + **to + base**.

:::
```

Source : manuel SB p. 97 (Module 4 Lesson 5, encadré « The gerund ») et SB p. 52 (Module 2 Lesson 5, encadré
« Subject + intend to + bare infinitive ») ; exigence : examens 2023 technique et 2018 générale (forme verbale
après decide / need).

### C2 — `cours.md`, § « 🪞 Reflexive pronouns » : les pronoms compléments (P2)

Emplacement : remplacer le tableau à deux colonnes de la section (en-tête « | Subject | Reflexive pronoun | »,
sept lignes) par le tableau ci-dessous, suivi d'une ligne vide puis du paragraphe :

```markdown
| Subject | Object pronoun | Reflexive pronoun     |
| ------- | -------------- | --------------------- |
| I       | me             | myself                |
| you     | you            | yourself / yourselves |
| he      | him            | himself               |
| she     | her            | herself               |
| it      | it             | itself                |
| we      | us             | ourselves             |
| they    | them           | themselves            |

After a verb or a preposition, a pronoun takes its **object** form: _The teacher helped **us**._ — _Sami played with **them**._ When the object is the **same person** as the subject, the object form becomes the reflexive one: _We helped **ourselves**._
```

Source : manuel SB p. 33 (Module 2 Lesson 1, tableau des pronoms personnels et possessifs) et SB p. 38 (Module 2
Lesson 2, réfléchis) ; exigence : neuf sessions d'examen demandent le pronom complément (2002 à 2023).

### C3 — `cours.md`, nouvelle section « 🔧 One root, several words » (P3)

Emplacement : entre la fin de la section « 🏷️ Compound nouns » (bloc `::: retenir` « Main word last, kind
first… » et son `:::`) et le titre « ## 🏊 The gerund — a verb that works as a noun ». Insérer, précédé et suivi
d'une ligne vide :

```markdown
## 🔧 One root, several words — noun, adjective or adverb

Rania worked hard all year. Her teacher writes three sentences on the board: _Rania is a ___ pupil. — She passed her exam ___. — Her ___ makes her parents proud._ Each missing word comes from the same root, **success** — but not in the same form.

How do you know which form the gap needs?

> 🎯 The book teaches compound nouns; the national exam goes one step further. Every year since 2022, its language part asks for the right form of a word built on a root — in a choice of three forms or with a word in brackets.

::: definition
Many English words are built on a **root** and a **suffix** (an ending). The suffix tells the **class** of the word: a **noun** names, an **adjective** describes a noun, an **adverb** tells **how** an action is done.

:::

| Class                      | Suffix                                            | Root → word                                                       |
| -------------------------- | ------------------------------------------------- | ----------------------------------------------------------------- |
| noun (a thing, an action)  | **-ment**, **-tion**                              | develop → develop**ment**, protect → protec**tion**                |
| noun (a person)            | **-er**, **-ist**                                 | teach → teach**er**, science → scient**ist**                       |
| adjective                  | **-al**, **-ful**, **-ous**                       | nature → natur**al**, help → help**ful**, danger → danger**ous**   |
| adjective (a feeling)      | **-ing** (what causes it), **-ed** (who feels it) | a bor**ing** film, a bor**ed** pupil                               |
| adverb (how?)              | adjective + **-ly**                               | quick → quick**ly**, natural → natural**ly**                       |

::: exemple
Fill the three gaps about Rania, step by step:

1. _a ___ pupil_: the gap comes **before a noun**, so it needs an **adjective** → _success_ + **-ful** → _a **successful** pupil_.
2. _She passed her exam ___._: the gap tells **how** she passed → an **adverb**, the adjective + **-ly** → _**successfully**_.
3. _Her ___ makes her parents proud_: after _her_ and before the verb, the gap is the **subject** → a **noun**: _Her **success** makes her parents proud._

:::

> ⚠️ **Common mistake**: _She speaks English very **good**._ ✗ — an adjective cannot tell **how** someone does something. You need the adverb: _She speaks English very **well**._ ✓ Some words also change more than their ending: _good → well_, _succeed → success_, _believe → belief_.

::: propriete
Look at the words **around** the gap: after _a, the, his, her_ or as the subject of a verb → **noun**; before a noun, or after _be, become, feel_ → **adjective**; next to a verb, telling how → **adverb**.

Edge case: the **-ly** adverb is built on the **adjective**, not on the noun: _nature → natural → naturally_ (one **l** from _-al_, one from _-ly_).

:::

::: verifie
Complete with the right form of the word in brackets: "The museum guide was very (help) ___, and he spoke (slow) ___ about the (protect) ___ of old buildings."

---

_The museum guide was very **helpful**, and he spoke **slowly** about the **protection** of old buildings._ — after _very_ and _be_, the gap describes the guide: an adjective in **-ful**; the second gap tells **how** he spoke: adjective + **-ly**; after _the_, the third gap is a noun in **-tion**.

:::

::: retenir
Noun: -ment, -tion, -er, -ist · adjective: -al, -ful, -ous, -ing / -ed · adverb: adjective + -ly — the words around the gap choose the class.

:::
```

Suffixes retenus : ceux que les sujets exigent réellement (15 sessions, 2010–2026) — nom en **-ment** (2025 G,
2025 T), **-tion** (2024 T), **-er / -ist** de personne (2026 T, 2026 G), adjectif en **-al** (2026 G, 2019 G,
2010 G), **-ful** (2011 G), **-ous** (2022 G), **-ing / -ed** (2022 G, 2020 G, 2013 G, 2025 T), adverbe en **-ly**
(2025 G ×2, 2023 G, 2022 G, 2011 G) ; changements de forme : choose → choice (2022 T), advise → advice (2018 G),
beauty → beautiful (2022 G). Aucun autre suffixe (‑ness, ‑ity, ‑able…) : aucun sujet ne le demande.
Source : manuel SB p. 78 (Module 3 Lesson 5, « Noun formation 2 », noms composés) ; section déclarée au-delà
du manuel par la ligne 🎯.

### Résumé — `resume.md`

R1 — remplacer la puce « - **Reflexive pronouns** — … » par :

```markdown
- **Object and reflexive pronouns** — after a verb or a preposition: **me, you, him, her, it, us, them** (_Sami played with them_). When the object is the subject: **myself, yourself / yourselves, himself, herself, itself, ourselves, themselves** (_He hurt himself_), or "with no help" (_I made it myself_).
```

R2 — insérer, entre la puce « - **Compound nouns** — … » et la puce « - **The gerund** — … », la puce :

```markdown
- **One root, several words** — the suffix gives the class: noun **-ment, -tion, -er, -ist**; adjective **-al, -ful, -ous, -ing / -ed**; adverb = adjective + **-ly** (_success → successful → successfully_). The words around the gap choose the class.
```

R3 — à la fin de la puce « - **The gerund** — … » (après « (_waiting, playing_). »), ajouter :

```markdown
 But **decide, want, need, hope, learn, would like** + **to + base**: _She decided to join the club._
```

## Missions

- mission fusionnée **m022** : session **2025 technique** (`content/programmes-officiels/examens-nationaux/9eme-base/english/2025-technique.md`), partie II (language), exercice 2 imprimé ; session **2025 générale** (`…/2025-generale.md`), exercice 3 ; session **2024 technique** (`…/2024-technique.md`), exercice 1 ; session **2023 technique** (`…/2023-technique.md`), exercice 2 ; session **2022 générale** (`…/2022-generale.md`), exercice 2 ; session **2022 technique** (`…/2022-technique.md`), exercice 1 ; session **2019 technique** (`…/2019-technique.md`), exercice 1 ; session **2018 générale** (`…/2018-generale.md`), exercice 3 ; session **2016 technique** (`…/2016-technique.md`), exercice 3 ; session **2015 générale** (`…/2015-generale.md`), exercice 1 ; session **2003** (`…/2003-unique.md`), exercice 3 ; session **2002** (`…/2002-unique.md`), exercice 3 → chapitre `07-reported-speech`, fichier `exercices/06-exams-2002-2025-the-gerund-or-to-base.json`, `displayOrder` 6 — étage **d3** (boss 120/30), 12 questions au plus ; titre : « 🏛️ Exams 2002–2025 · the gerund or to + base in exam texts ⭐⭐⭐ » ; base : session 2025 technique (la mission en garde l'ordre ; chaque question dit sa session et redonne la phrase officielle) ; archétype : « choisir ou produire la forme du verbe qu'exige le mot qui précède : gérondif après une préposition, après like / enjoy / begin, en sujet ou devant un nom ; to + base après decide / need » ; piège : « to + base après une préposition ; base verbale en sujet ; gérondif après decide ou need » ; consigne de tri : 2025 T (base) : « …without (have - to have - having) to worry about finding a job. » → having. 2025 G (forme à mettre) : « There is simply no point in (remove) ........ technology from your teen… » → removing (`short_answer`). 2024 T (banque) : « Recently, we have begun ........ complete plumbing, heating, cooling and electrical services… » → offering (la banque n'offre que la forme en -ing ; l'explication dit que « begin » accepte aussi to + base, sans le proposer en option). 2022 G : « (Be / Being / Been) close to nature is not just loving its… » → Being (sujet). 2022 T (banque) : « Megan discovered her passion for ........ with her hands… » → working (leurre officiel « making »). 2019 T (banque) : « Welders use different ways ........ producing cars and ships, building electronics, and ........ bridges. » → of ; constructing (une question, deux blancs : la préposition puis le gérondif parallèle). 2016 T : « He was born with (hear / heard / hearing) problems. » → hearing (gérondif + nom). 2015 G (banque) : « They swim and do aerobics before ........ a healthy lunch. » → having. 2003 : « She likes ③ ........ and gardening… » (read – reading - reads) → reading. 2002 : « She enjoys (④ helping – helps – to help) children. » → helping. 2023 T : « It means deciding (protecting / protect / to protect) the environment. » → to protect (ligne de cours C1). 2018 G : « I didn't need (wake / to wake / waking) up to my alarm clock. » → to wake (C1). Écarté dans la mission : 2002 « let school children (to cross – crossing – cross) » (let + base, non enseigné) ; 2019 T « no women (doing / done / do) this job » (participe, pas gérondif) ; 2016 T, 2022 G, 2015 G ont d'autres blancs déjà posés ailleurs. Ne pas redemander : 07/01 Q6, 07/02 Q6, 07/04 Q3, 07/05 Q2–Q3, 07 quiz Q4 ; 06 quiz Q1, Q3 ; 03/02 Q2, 03/04 Q2, 03 quiz Q4 (thinking of + -ing) ; 03/01 Q5, 03/02 Q5, 03/05 Q6, 03 quiz Q5 (intend to) ; m011 (2012 T « would like … join ») ; m016 (2019 G « nervous about meeting ») ; les exemples du cours C1 (join the club, buy a new map).
- mission fusionnée **m023** : session **2023 technique** (`…/2023-technique.md`), partie II (language), exercice 2 imprimé ; session **2021 technique** (`…/2021-technique.md`), exercice 3 ; session **2021 générale** (`…/2021-generale.md`), exercice 2 ; session **2019 générale** (`…/2019-generale.md`), exercice 3 ; session **2018 technique** (`…/2018-technique.md`), exercices 1 et 3 ; session **2015 générale** (`…/2015-generale.md`), exercice 3 ; session **2013 technique** (`…/2013-technique.md`), exercice 2 ; session **2012 technique** (`…/2012-technique.md`), exercice 2 ; session **2010 générale** (`…/2010-generale.md`), exercice 1 ; session **2009 technique** (`…/2009-technique.md`), exercice 2 ; session **2007** (`…/2007-unique.md`), exercice 1 → chapitre `07-reported-speech`, fichier `exercices/07-exams-2007-2023-pronouns-in-exam-texts.json`, `displayOrder` 7 — étage **d2** (practice 75/15), 12 questions au plus ; titre : « 🏛️ Exams 2007–2023 · pronouns in exam texts: object, reflexive, possessive ⭐⭐ » ; base : session 2023 technique ; archétype : « choisir le pronom complément, réfléchi ou possessif qu'exigent la fonction et la personne dans une phrase officielle » ; piège : « pronom sujet après un verbe ou une préposition ; complément là où le sujet et l'objet sont la même personne ; mauvaise personne du réfléchi » ; consigne de tri : 2023 T (base) : « Plants are green, and without (them / him / her) the earth wouldn't be such a lovely… » → them. 2021 T : « That job made (it / me / them) a much stronger person today. » → me. 2021 G : « …a bike can pay for (yourself / itself / herself) when compared to the price of bus tickets. » → itself. 2019 G : « …helping people who may not be able to help (themselves / yourself / yourselves). » → themselves. 2018 T, exercice 1 (banque) : « All of ........ have access to the internet. » → them (leurre officiel « they »). 2018 T, exercice 3 : « Building our (own / one / self) house was a dream that we achieved. » → own. 2015 G : « Then he would answer (myself / himself / herself) … » → himself. 2013 T : « …his wife is going to buy (he / his / him) a lovely present. » → him. 2012 T : « …and shares songs with (they / her / them). » → them. 2010 G (banque) : « I have always thought everyone lived like ⓕ........ » → me. 2009 T : « …and look at ⓑ........ in the mirror… » (yourself – himself - myself) → myself. 2007 (banque) : « …we are only concerned about ⓔ........ future. » → his (adjectif possessif ; leurre officiel « him »). Écarté dans la mission : 2008 « He threw ⓐ........ » (himself : répète 2015 G), 2015 G banque « take ........ to the beach », 2007 ⓓ « give ........ pocket money » et ex. 3 ⓓ, 2002 ①/⑤ : même geste. Ne pas redemander : 07/01 Q1, 07/02 Q4–Q5, 07/04 Q6, 07/05 Q1, 07 quiz Q2 ; les exemples du cours C2 (helped us, played with them, helped ourselves).
- mission fusionnée **m024** : session **2022 générale** (`…/2022-generale.md`), partie II (language), exercice 3 imprimé ; session **2026 générale** (`…/2026-generale.md`), exercice 2 ; session **2026 technique** (`…/2026-technique.md`), exercice 2 ; session **2025 générale** (`…/2025-generale.md`), exercices 2 et 3 ; session **2025 technique** (`…/2025-technique.md`), exercice 2 ; session **2024 technique** (`…/2024-technique.md`), exercice 2 ; session **2022 technique** (`…/2022-technique.md`), exercice 2 ; session **2019 générale** (`…/2019-generale.md`), exercice 3 ; session **2018 générale** (`…/2018-generale.md`), exercice 3 ; session **2011 générale** (`…/2011-generale.md`), exercice 3 → chapitre `07-reported-speech`, fichier `exercices/08-exams-2011-2026-one-root-several-words.json`, `displayOrder` 8 — étage **d3** (boss 120/30), 12 questions au plus ; titre : « 🏛️ Exams 2011–2026 · one root, several words: noun, adjective or adverb ⭐⭐⭐ » ; base : session 2022 générale ; archétype : « choisir ou produire, d'après les mots autour du blanc, la classe du mot tiré d'une racine (nom, adjectif, adverbe) et son suffixe » ; piège : « adjectif là où il faut l'adverbe ; verbe ou racine nue là où il faut le nom ; nom de chose pour une personne » ; consigne de tri : 2022 G (base, forme à mettre) : « Many (fame) ........ faces are helping out… » → famous ; « Music has always been seen as an (excite) ........ subject. » → exciting (`short_answer` pour les deux). 2026 G : « This determined (environmental / environmentally / environmentalist) has become one of the country's… » → environmentalist. 2026 T : « …the place is filled with younger (plumb / plumbers / plumbing), roofers and builders… » → plumbers. 2025 G, exercice 3 : « They are hooked up to a tablet or laptop for (entertain) ........ » → entertainment (`short_answer`) ; exercice 2 : « …relationship skills like communicating (clear/ clearer/ clearly), negotiating… » → clearly. 2025 T : « Technical education creates more and more (employer - employment - employee) opportunities. » → employment. 2024 T : « Her father was involved in the (constructed / constructs / construction) industry… » → construction. 2022 T : « Joan is proud of her (choose / choice / choosing)… » → choice. 2019 G : « …while developing important (social / society / socially) skills… » → social. 2018 G : « I (advice / advise / advised) everyone to cherish those days… » → advise (verbe ; l'autre moitié de la phrase est posée dans m010). 2011 G : « …but you just need to be (careful – carefully – care). » → careful. Écarté dans la mission (même suffixe déjà représenté) : 2025 G « (significant) », 2022 G « (involve) », « (great) », « (beauty / beautiful / beautifully) », 2023 G « (slowly / slow / slower) », 2020 G « (challenge / challenging / challenged) », 2013 G « (interested / interesting / interest) », 2010 G « (physically / physics / physical) », 2025 T « (educated / educating / educate) » (forme passive, non enseignée), 2016 G « (habit / habitat / inhabitant) » (choix lexical). Ne pas redemander : 07/01 Q2, 07/02 Q2, 07/04 Q1, Q5, 07/05 Q5, 07 quiz Q3 (mots composés) ; 06 quiz Q5 (interested) ; m014 (2011 G « fun ») ; m018 ; les exemples du cours C3 (success, develop, protect, teach, science, nature, help, danger, bore, quick, the museum guide).

Contrôles de l'auteur : gates comme les autres lots (`content:check`, `content:qa -- --subject english`, `content:tranche -- --subject english --chapters 07-reported-speech`) ; `content:qa` relit aussi `cours.md` et `resume.md`.
