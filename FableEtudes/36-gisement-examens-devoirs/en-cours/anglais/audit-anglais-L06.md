# Audit indépendant — lot L06 (anglais 9ᵉ, chapitre `07-reported-speech`)

Auditeur indépendant, 2026-10-17. Périmètre : `cours.md` (C1–C3), `resume.md` (R1–R3), `chapter.json` (`sources[]`),
missions `07/06` (m022), `07/07` (m023), `07/08` (m024), branche `wip/gisement-anglais-9eme` (commit `4315b156` + arbre
de travail). Skills invoqués : `content-audit`, puis `prof-anglais-9eme`. Sources lues : transcriptions officielles des
sessions citées, `PLAN.md` (§ 1, § 6), `assign-anglais-L06.md`, registre `english.*` sur `origin/main`, les exercices et
quiz publiés du 07 et du 06, et les missions des autres lots (pour les fuites).

Gates (moteur `/home/user/eng-en`) : `content:check` vert (le `09/13` de L04 est corrigé) ; `content:qa -- --subject
english` : aucune clé suspecte ; `content:tranche -- --chapters 07-reported-speech` : clé strictement la plus longue
3/61 (m024 Q5, Q6, Q8), 0 paire proche, 0 gabarit. Les correctifs ci-dessous ont été appliqués à une COPIE du corpus
(scratchpad) : `build.ts --check --content-dir <copie>` est vert, et la clé n'est plus jamais strictement la plus
longue (0/32 questions à options dans L06). Le rendu du cours a été vérifié avec `renderLesson` du moteur.

## 1. Cours et résumé

C1, C2, C3, R1, R2 et R3 sont insérés tels quels, aux bons emplacements. `chapter.json` : la ligne `sources[]` est
exacte, et rien d'autre n'a changé.

| bloc | justesse | cohérence chapitre / SB | exemples ≠ items d'examen | rendu |
| --- | --- | --- | --- | --- |
| C1 (`propriete` verbe + to + base) | OK | OK (intend, du 03, cité) | OK (join the club, buy a new map) | OK |
| C2 (tableau 3 colonnes + paragraphe) | OK | OK | OK (voir § 3 pour « help ») | OK |
| C3 (« One root, several words ») | réserve : la règle est incomplète (D2) | OK, la ligne 🎯 est exacte (dérivation chaque année depuis 2022 : 2022 G/T, 2023 G, 2024 T, 2025 G/T, 2026 G/T) | OK. La racine *slow* de la vérification est celle de l'item 2023 G, écarté de la mission, avec une autre phrase : accepté | **défaut D1** |
| R1, R2, R3 | OK | ils reprennent le cours | — | OK |

Le tableau de C3 rend correctement : le gras à l'intérieur d'un mot (`develop**ment**`) passe dans le rendu du moteur.
Le reste de C3 a les défauts D1 et D2.

## 2. Re-résolution (36 questions, à l'aveugle)

### m022 — `06-exams-2002-2025-the-gerund-or-to-base.json` (d3 boss 120/30)

| Q | session | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- | --- |
| 1 | 2003 | reading | b reading | OK (mineur) | « A girl describes » : le sexe de la narratrice est inventé (m2) |
| 2 | 2002 | helping | c | OK | même geste que 07 quiz Q4 (enjoy + -ing), mais phrase officielle : réserve m10 |
| 3 | 2015 G | having | a | OK | |
| 4 | 2022 T | working | d | OK | le leurre officiel « making » a été écarté à raison (« passion for making with her hands » se défend) ; la fuite par m011 Q1 est corrigée côté L03 |
| 5 | 2016 T | hearing | a | OK | |
| 6 | 2024 T | offering | c | réserve (m3) | *begin* + -ing n'est pas enseigné ; la question se résout par élimination, et l'explication l'enseigne |
| 7 | 2022 G | Being | a | **défaut D9** | distracteur « Beeing » |
| 8 | 2025 T | having | b | OK | énoncé paraphrasé, mais fidèle |
| 9 | 2019 T | of / constructing | c | OK | plan 2×2 exact (chaque valeur deux fois) |
| 10 | 2025 G | removing (`short_answer`) | removing | OK | variantes complètes ; expectedMistakes justes et étiquetés |
| 11 | 2023 T | to protect | a | OK (mineur m1) | l'explication cite « need », qui donne la clé de Q12 |
| 12 | 2018 G | to wake | a | **défaut D11** | « woke » cumule deux erreurs et porte une étiquette |

### m023 — `07-exams-2007-2023-pronouns-in-exam-texts.json` (d2 practice 75/15)

| Q | session | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- | --- |
| 1 | 2013 T | him | a | **défaut D12** | explication fausse sur himself |
| 2 | 2012 T | them | b | **défaut D5** ; étiquette m4 | fuite vers m013 Q4 (« her daughter, who ») ; étiquette inexacte sur themselves |
| 3 | 2007 | his | c | OK | « he » reste muet, à raison (il faut le possessif) |
| 4 | 2023 T | them | a | OK | |
| 5 | 2021 T | me | d | **défaut D4** | fuite vers m008 Q6 (« I gained ») ; la citation omet aussi « I did, » |
| 6 | 2018 T | them | b | OK | |
| 7 | 2018 T | own | a | **défaut D8** | *own* n'est pas enseigné ; la glose de l'énoncé donne la clé ; « ourselves » s'élimine à vue |
| 8 | 2010 G | me | c | **défaut D7** | « like myself » se défend en anglais courant |
| 9 | 2015 G | himself | b | OK | les étiquettes de myself, herself et him sont exactes |
| 10 | 2021 G | itself | c | OK | |
| 11 | 2019 G | themselves | d | OK (voir § 3) | clé donnée par 09/13 Q11 (lot L04) : **D6** |
| 12 | 2009 T | myself | a | OK | |

### m024 — `08-exams-2011-2026-one-root-several-words.json` (d3 boss 120/30)

| Q | session | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- | --- |
| 1 | 2011 G | careful | b | OK | 07/01 Q1 affiche « Be careful » : mot courant, ce n'est pas une fuite |
| 2 | 2019 G | social | a | OK | |
| 3 | 2018 G | advise | c | **défaut D3** ; m5 | fuite vers m010 Q1 (« you will regret it ») ; « advisor » s'élimine à vue |
| 4 | 2025 G | clearly | b | OK | |
| 5 | 2024 T | construction | a | **D10** + D2 | clé strictement la plus longue ; la règle de C3 (« before a noun → adjective ») désigne « constructed » |
| 6 | 2025 T | employment | c | **D10** + D2 | clé strictement la plus longue |
| 7 | 2026 T | plumbers | d | OK | |
| 8 | 2026 G | environmentalist | b | **D10** | clé strictement la plus longue |
| 9 | 2022 T | choice | b | OK (m6) | « choosing » est un leurre officiel acceptable ; l'explication doit être reprise |
| 10 | 2022 G | famous (`short_answer`) | famous | OK (m7) | « famed » est juste et serait refusé |
| 11 | 2022 G | exciting (`short_answer`) | exciting | OK (m8) | |
| 12 | 2025 G | entertainment (`short_answer`) | entertainment | OK | |

Fidélité : toutes les phrases et toutes les options officielles correspondent aux transcriptions. Il n'y a ni item HP ni
item écarté. Les étages et la rampe sont honnêtes (m022 et m024 : 1→3 ; m023 : 1→2). Les titres respectent le format
et ne livrent aucune clé. Aucune explication ne désigne une option par sa place.

## 3. Points imposés par l'orchestrateur

**3.1 « protect » dans m022 (Q11) face à C3 (protect → protection) : accepté.** La question teste decide + to + base ;
la racine n'y est pas dérivée. Le cours n'affiche ni « to protect » ni aucune option de Q11. Aucune fuite.

**3.2 « help themselves » (m023 Q11) face à l'exemple de C2 « We helped ourselves » : accepté.** La phrase et la
personne diffèrent : la question demande l'accord avec *people*, donc *themselves*. Aucune option de Q11 ne figure dans
le cours. Le cours enseigne la règle, il ne pose pas l'item. Il n'y a rien à changer. (« help oneself » veut aussi dire
« se servir », ce qui est sans effet ici.)

**3.3 `short_answer` de m024 et de m022.**
- **Variantes acceptées.** removing, exciting et entertainment n'ont pas de variante juste : *entertaining*
  signifierait « recevoir des invités », il est faux. Ajouter `"acceptedAnswers": ["famed"]` à m024 Q10 : « Many
  famed faces » est un anglais correct, construit sur la racine (m7). Aucune variante ne serait fausse, et aucune
  n'égale une erreur déclarée.
- **expectedMistakes absents de fame, excite et entertain : acceptable.** Le schéma exige une étiquette par erreur
  attendue (vérifié par `build --check` : une entrée sans `misconceptionTag` est refusée), et le registre n'a
  d'étiquette exacte que pour une seule de ces erreurs. Ajouter cette seule entrée à m024 Q11 :
  `"expectedMistakes": [{ "text": "exciteing", "misconceptionTag": "english.spell.suffixe-sans-regle-orthographique" }]`
  (le libellé cite « e muet qui tombe (leaving) » : c'est exact). *fameous*, *fame*, *excited*, *entertaining* et
  *entertain* n'ont pas d'étiquette exacte, et l'explication traite déjà chacune de ces erreurs.

**3.4 Clés strictement les plus longues (3/61) : corrigées par D10, mesure après correctif 0.**

**3.5 Options.**
- **« Beeing » (m022 Q7) : rejeté (D9).** C'est un non-mot dans une question qui teste la forme. Il crée un indice de
  forme : deux options en *-ing* désignent la bonne paire, et la question devient une question d'orthographe. Le motif
  donné par l'explication (« the silent e does not exist in be ») ne correspond pas à l'erreur, qui est un *e* ajouté.
  Avec les trois seules options officielles, « Being » deviendrait strictement la plus longue ; d'où le remplacement par
  « To being ».
- **« choosing » pour « her choice » (m024 Q9) : accepté.** C'est le leurre officiel. Sans complément, « her
  choosing » ne nomme pas la décision. Seule l'explication est à reprendre : *choose* peut s'employer sans objet (m6).
- Les autres options ajoutées sont justes et plausibles : 2002 « help », 2015 G « have / to have / has »,
  2021 T « her », 2023 T « they », 2018 T « their / him », 2010 G « my / mine », 2026 T « plumber », 2022 T « chosen ».
  Exceptions : « advisor » (m5), « ourselves » (D8), « woke » (D11), « myself » (D7).

## 4. Défauts et correctifs (textes vérifiés : longueurs, clé unique, aucune fuite, `build --check` vert sur copie)

### Critiques : 0 clé fausse.

### Majeurs

**D1 — C3 : soulignés bruts au rendu.** Le moteur ne met pas en italique un `_…_` qui contient `___` ou qui commence
par `-`. L'élève verrait `_Rania is a ___ pupil. …_`, `_a ___ pupil_`, `_**successfully**_`, `_-al_`. Remplacements
dans `cours.md`, vérifiés par `renderLesson` (aucun souligné brut ne reste hors des blancs) :
- `writes three sentences on the board: _Rania is a ___ pupil. — She passed her exam ___. — Her ___ makes her parents proud._ Each`
  → `writes three sentences on the board: "Rania is a ___ pupil." — "She passed her exam ___." — "Her ___ makes her parents proud." Each`
- `1. _a ___ pupil_: the gap` → `1. "a ___ pupil": the gap`
- `2. _She passed her exam ___._: the gap tells **how** she passed → an **adverb**, the adjective + **-ly** → _**successfully**_.`
  → `2. "She passed her exam ___.": the gap tells **how** she passed → an **adverb**, the adjective + **-ly** → **successfully**.`
- `3. _Her ___ makes her parents proud_: after` → `3. "Her ___ makes her parents proud": after`
- dans l'Edge case : `(one **l** from _-al_, one from _-ly_)` → `(one **l** from **-al**, one from **-ly**)` (voir D2
  pour le texte complet de la ligne).

**D2 — C3 `propriete` : la règle se contredit avec l'exemple et avec m024.** « after _a, the…_ → noun » contredit
l'exemple « a ___ pupil » (un adjectif). « before a noun → adjective » désigne « constructed » en m024 Q5 (« the ___
industry ») et un adjectif en Q6 (« ___ opportunities »), alors que les deux clés sont des noms qui disent l'espèce
(nom composé). Remplacer le bloc entier par :

```markdown
::: propriete
Look at the words **around** the gap: after _a, the, his, her_ when no noun follows the gap, or as the subject of a verb → **noun**; before a noun, or after _be, become, feel_ → **adjective**; next to a verb, telling how → **adverb**.

Edge case: before a noun, a **noun** can also say what kind, as in a compound noun: a _history lesson_ is a kind of lesson. And the **-ly** adverb is built on the **adjective**, not on the noun: _nature → natural → naturally_ (one **l** from **-al**, one from **-ly**).

:::
```
(Rendu vérifié. « history lesson » n'apparaît dans aucun sujet transcrit.)

**D3 — m024 Q3 : fuite vers m010 Q1 (05/06), qui demande « will regret ».** Je reprends le correctif de L02, vérifié
(m010 Q2 cite elle-même « because if you don't, then… », donc aucune nouvelle fuite). Nouveau `prompt` :
`(Exam 2018, general) A grown-up remembers the first day of school and speaks to the reader now: "I ___ everyone to cherish those days because if you don't, then…" Advice is the noun, a piece of guidance, and advise is the verb, to give advice.`

**D4 — m023 Q5 : fuite vers m008 Q6 (02/07), qui demande « gained ».** La proposition de L02 (« A woman talks about her
work… and what her jobs taught her: ») retire le « I » de la citation. Sans lui, « her » se défend : la phrase
pourrait parler de la femme. Elle n'est donc **pas** reprise. Nouveau `prompt` :
`(Exam 2021, technical) A woman talks about her work as a car mechanic. She says: "That job made ___ a much stronger person today."`
Nouvelle `explanation` : `The woman is speaking about herself, so the person who became stronger is the speaker, I, and after the verb made the pronoun takes its object form: me. It and them stand for things or for several people, and her would be another woman.`

**D5 — m023 Q2 : fuite vers m013 Q4 (08/06), qui demande « who ».** La proposition de L03 (« A mother writes about her
teenage daughter and the Internet: ») est vérifiée : elle ne contient pas « who ». Je préfère cependant « parent » :
la transcription ne dit pas qui écrit, et m013 Q4 dit « A father ». Nouveau `prompt` :
`(Exam 2012, technical) A parent writes about a teenage daughter and the Internet: "She talks about school life with her friends and shares songs with ___."`
Dans la même question, retirer l'étiquette de `themselves` (m4).

**D6 — Fuite qui part du lot L04 (09/13 Q11) vers m023 Q11.** Son énoncé cite « …helping people who may not be able
to help themselves. ». À corriger par L04, avec ce `prompt` :
`(Exam 2019, general) A text explains why volunteering is valuable. Which word completes the sentence? "It gives you the satisfaction of playing a ___ in someone else's life."`
« role » reste la seule réponse : « playing a game / a responsibility in someone else's life » est faux.

**D7 — m023 Q8 : « like myself » se défend.** Le réfléchi après *like* est un usage courant reconnu (« people like
myself »). Remplacer l'option `d` « myself » par `{ "id": "d", "text": "I" }`. Elle reçoit l'étiquette de la famille
(a) si celle-ci est retenue (§ 5), sinon elle reste muette. Nouvelle `explanation` :
`After the preposition like, the pronoun takes its object form: like me. My needs a noun after it, mine replaces a noun that belongs to the speaker, and I is the subject form, which cannot follow a preposition.`
(« everyone lived like I, » sans verbe est faux ; clé « me », 2 lettres, et non la plus longue.)

**D8 — m023 Q7 : *own* n'est enseigné nulle part.** L'énoncé le définit (« stresses that the house belongs to the
couple alone ») : la règle est donnée, puis appliquée directement. De plus, « ourselves » s'élimine à vue après « our ».
Correctif :
1. `cours.md`, § Possessives, bloc `propriete` : après la ligne « Edge case: a plural noun… (_it's_ means _it is_). »,
   ajouter une ligne vide puis
   `To stress that a thing belongs to its owner and nobody else, put **own** between the possessive adjective and the noun: _Lina has her **own** room._`
   (rendu vérifié ; facultatif : ajouter à la puce Possessives du résumé « ; **own** stresses "nobody else's" (_her own room_) »).
2. Nouveau `prompt` : `(Exam 2018, technical) A couple tell how they built the house where they now live. Complete the sentence: "Building our ___ house was a dream that we achieved."`
3. Supprimer l'option « ourselves ». Il reste les trois options officielles own / one / self (clé de 3 lettres, non
   la plus longue).
4. Nouvelle `explanation` : `Own stands between a possessive adjective and a noun to stress that the thing belongs to its owner and nobody else: our own house. One counts things, and self is only the end of a reflexive pronoun (ourselves), never a word placed before a noun.`
   (L'ancienne disait « self is not a word on its own », ce qui est faux : *self* est un nom.)

**D9 — m022 Q7 : distracteur « Beeing » (§ 3.5).** Remplacer l'option `d` par `{ "id": "d", "text": "To being" }`
(muette). Nouvelle `explanation` :
`The gap is the subject of the verb is, and a verb used as a subject takes the gerund: Being close to nature. Be is the bare verb, Been is the past participle, and To being mixes to with the -ing form.`
(« To be close to nature… » serait juste, mais n'est pas proposé ; longueurs Being 5 / To being 8.)

**D10 — m024 : trois clés strictement les plus longues.** Les clés officielles ne peuvent pas être raccourcies. On
ajoute donc à chaque question un 4ᵉ distracteur, de même longueur ou plus long, faux par une règle enseignée :
- **Q5** : ajouter `{ "id": "d", "text": "constructively" }` (14 > 12). Pas *constructing* : la règle du cours sur le
  gérondif devant un nom (« a swimming pool ») le rendrait défendable. `explanation` :
  `After the and before the noun industry, the gap names the kind of industry, so it is a noun: construction, from the verb construct with the ending -tion. Constructed and constructs are verb forms, and constructively, with -ly, is an adverb: it tells how an action is done and cannot name the kind of industry.`
- **Q6** : ajouter `{ "id": "d", "text": "employments" }` (11 > 10). Le pluriel est un réflexe d'élève après « more and
  more ». `explanation` :
  `The gap names the situation of having a job, so it is a noun in -ment, from the verb employ: employment opportunities. An employer and an employee are people, a boss and a worker, not a kind of opportunity, and the word that says what kind stays singular, as in a toothbrush, a brush for your teeth.`
  (*toothbrush* est l'exemple de la vérification du § Compound nouns.)
- **Q8** : ajouter `{ "id": "d", "text": "environmentalism" }` (égalité à 16). Il exécute le piège déclaré « nom de
  chose pour une personne ». `explanation` :
  `The gap follows the adjective determined and is the subject of has become, so it names a person: a noun in -ist. Environmental is an adjective and environmentally is an adverb, and neither can be the subject of a verb; environmentalism, with -ism, names the idea of protecting nature, not the girl who does it.`

**D11 — m022 Q12 : « woke » cumule deux erreurs (pas de to, passé marqué deux fois) et porte une étiquette.**
Remplacer l'option `c` par le leurre officiel `{ "id": "c", "text": "wake" }`, muet ou étiqueté selon la décision du
§ 5 (b). On obtient un plan 2×2 exact : to wake / to waking / wake / waking. Nouvelle `explanation` :
`Need is followed by to + base: need to wake. Didn't already marks the past, so the verb stays in its base form after to. The -ing form copies the gerund list, the bare wake forgets the to, and to waking mixes the two patterns.`

**D12 — m023 Q1 : explication fausse.** « himself would only fit if the wife were buying the present for herself » :
dans ce cas, ce serait *herself*. Nouvelle `explanation` :
`The gap follows the verb buy and names the person who receives the present, so the pronoun takes its object form: him. He is the subject form, his needs a noun after it, and himself could only point back to a man who is the subject, but the subject here is his wife.`

### Mineurs

- **m1** — m022 Q11 : l'explication cite « need », clé de Q12, qui suit. Nouvelle `explanation` :
  `Decide is followed by to + base: deciding to protect. The -ing in deciding belongs to decide itself and does not change the form that follows. The -ing form copies the gerund list, the bare form forgets the to, and the -ed form is a past form.`
- **m2** — m022 Q1 : « A girl describes her aunt Emily » : le sujet ne dit pas que c'est une fille. Remplacer par
  `A pupil describes Aunt Emily, who lives alone in a small village.`
- **m3** — m022 Q6 : *begin* + -ing n'est pas au cours. La question se résout par élimination (offer, offered et
  to offering sont faux selon les règles enseignées), et l'explication enseigne *begin*. Acceptable ; signalé.
- **m4** — m023 Q2 : `english.pron.reflechi-mal-forme` sur « themselves » est inexacte. L'erreur est un réfléchi là
  où le sujet n'est pas l'objet, pas un mauvais réfléchi. Laisser l'option muette.
- **m5** — m024 Q3 : « advisor » (suffixe -or, non enseigné ; « I advisor » s'élimine à vue). Supprimer l'option et
  garder les trois options officielles. Nouvelle `explanation` :
  `After the subject I, the gap needs a verb in the present: advise. Advice is a noun, so it cannot follow I. Advised is a past form, but the speaker is giving the advice now.`
- **m6** — m024 Q9 : nouvelle `explanation` :
  `After her, the gap needs a noun, the thing she decided: choice, a word built on choose that changes more than its ending. Choose is the verb and chosen is the participle; choosing is the -ing form of the verb and would need to say what she chose (her choosing a new job), so alone it cannot name her decision.`
- **m7** — m024 Q10 : ajouter `"acceptedAnswers": ["famed"]`.
- **m8** — m024 Q11 : ajouter l'expectedMistake `exciteing` étiqueté (§ 3.3).
- **m9** — C3 : le piège « very good → well » n'a pas d'étiquette au registre, et aucun distracteur étiqueté ne
  l'exécute (seul m024 Q4 « clear », muet). Le texte vient du pilote ; une famille « classe de mot confondue »
  pourrait réunir m024 Q1, Q2, Q4, Q5 et Q8. Je la suggère sans la créer : l'auteur ne l'a pas proposée.
- **m10** — Doublons de geste, sans doublon de question : m022 Q2 (enjoys helping) face à 07 quiz Q4 (enjoys drawing) ;
  m022 Q10 (in + remove, e muet) face à 07/02 Q6 (before + leave). Ce sont les phrases officielles et la consigne de
  tri les impose : réserve, sans correctif.
- **m11** — C3 : la chute de l'e muet devant -ous (fame → famous) n'est montrée qu'implicitement (nature → natural ;
  gérondif). Facultatif.
- **Hors lot (préexistant, pour suivi)** : le moteur émet `<p></table></p>` après chaque tableau du cours, y compris
  ceux déjà publiés. Dans le § Gerund, `_**Skiing** can be dangerous._`, `_**After eating**, we went out._` et la
  réponse `_**Running** is…_` s'affichent avec leurs soulignés bruts. Aucun de ces textes n'appartient à L06.

## 5. Deux familles d'étiquettes proposées par l'auteur

**(a) Pronom sujet après un verbe ou une préposition : RETENUE.** Elle a au moins 3 questions distinctes, et chaque
placement exécute exactement l'erreur :
m023 Q1 « he » (buy he), Q2 « they » (with they), Q4 « they » (without they), Q6 « they » (all of they) et, après D7,
Q8 « I » (like I). m023 Q3 « he » reste muet : le blanc demande un possessif, pas un complément.

```json
"english.pron.sujet-apres-verbe-ou-preposition": {
  "subject": "english",
  "labels": {
    "fr": "Tu mets le pronom sujet (I, he, she, we, they) après un verbe ou une préposition : il faut la forme complément (me, him, her, us, them).",
    "en": "You use a subject pronoun (I, he, she, we, they) after a verb or a preposition: it needs the object form (me, him, her, us, them).",
    "ar": "تستعمل ضمير الفاعل (I وhe وshe وwe وthey) بعد فعل أو حرف جرّ: يلزم ضمير المفعول (me وhim وher وus وthem)."
  }
}
```

**(b) « -ing ou base verbale après decide, want, need, hope, learn, would like » : REJETÉE.**
1. Elle n'a que deux placements : m022 Q11 (protecting, protect) et Q12 (waking, wake après D11). J'ai cherché un
   troisième dans tous les exercices et quiz de `content/english/`. Le seul item proche, m011 Q7 (04/06, « would like
   ___ join »), n'a pour distracteurs que have, certainly et is. Le reprendre en choix de forme (« to join / joining /
   join ») est exclu : *join* est l'exemple de C1, et m011 figure sur la liste « ne pas redemander ».
2. Son libellé réunit deux erreurs différentes : le gérondif étendu à tort, et le *to* oublié.

Solution de repli, laissée au choix du pilote : élargir l'étiquette existante `english.modal.to-oublie`, qui a déjà
6 fichiers placés, pour couvrir la moitié « base verbale ». On pose ensuite cette étiquette sur m022 Q11 « protect »
et Q12 « wake ». Les distracteurs en -ing restent muets. Libellés élargis :
- fr : `Tu oublies le to de ought to, have to, be able to, be unable to ou intend to, ou après decide, want, need, hope, learn ou would like : ces formes le gardent toujours.`
- en : `You drop the to of ought to, have to, be able to, be unable to or intend to, or after decide, want, need, hope, learn or would like: these forms always keep it.`
- ar : `تحذف to من ought to وhave to وbe able to وbe unable to وintend to، أو بعد decide وwant وneed وhope وlearn وwould like: هذه الصيغ تحتفظ بها دائمًا.`

## 6. Bilan

| fichier | questions | clés fausses | majeurs | mineurs |
| --- | ---: | ---: | ---: | ---: |
| cours / résumé (C1–C3, R1–R3) | — | — | 3 (D1, D2, D8-cours) | 2 (m9, m11) |
| m022 (07/06) | 12 | 0 | 2 (D9, D11) | 4 (m1, m2, m3, m10) |
| m023 (07/07) | 12 | 0 | 5 (D4, D5, D7, D8, D12) | 1 (m4) |
| m024 (07/08) | 12 | 0 | 2 (D3, D10 ×3 questions) | 4 (m5, m6, m7, m8) |
| hors lot (L04, 09/13 Q11) | — | — | 1 (D6) | — |

Questions auditées : 36. Clés fausses : 0. Questions à reprendre : 15 (m022 Q7, Q11, Q12, Q1 ; m023 Q1, Q2, Q5,
Q7, Q8 ; m024 Q3, Q5, Q6, Q8, Q9, Q10/Q11 en ajout). Étiquettes : la famille (a) est retenue avec 5 placements ; la
famille (b) est rejetée, avec une solution de repli ; l'étiquette de m023 Q2 est à retirer. Doublons : aucun doublon de
question ; deux doublons de geste acceptés (m10). Fuites : trois partent de L06 (D3, D4, D5), une y arrive depuis L04
(D6), et celle de m011 vers m022 Q4 est corrigée côté L03.

**Verdict : à corriger avant publication.** Les clés sont toutes justes ; les correctifs ont été vérifiés sur une copie
du corpus (`content:check` vert, aucune clé strictement la plus longue, rendu du cours propre).
