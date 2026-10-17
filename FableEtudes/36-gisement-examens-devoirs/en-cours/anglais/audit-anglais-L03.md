# Audit indépendant — lot L03 (anglais 9ᵉ, gisement étude 36)

> Auditeur indépendant, 2026-10-17 (reprise après coupure API ; aucun rapport antérieur n'existait).
> Branche `wip/gisement-anglais-9eme`, commit `a99787bc`. Fichiers audités (aucun modifié) :
> `content/english/04-modals/exercices/06-exams-2001-2023-modals-meaning-and-form.json` (m011),
> `…/04-modals/exercices/07-exams-2009-2026-writing-advise-warn-set-rules.json` (m012),
> `…/08-relative-clauses-comparatives/exercices/06-exams-2002-2026-relative-pronouns.json` (m013),
> `…/08-…/exercices/07-exams-2002-2025-comparative-or-superlative.json` (m014),
> `…/08-…/exercices/08-exams-2002-2026-building-the-comparison.json` (m015).
> Sources : transcriptions officielles, `cours.md` / `resume.md` des chapitres sur `origin/main`, missions et quiz
> publiés, registre `content/misconceptions.json` sur `origin/main`. Les lignes `sources[]` des `chapter.json`
> 04 et 08 sont ajoutées par le pilote à la livraison : non comptées.
> Numérotation : Qn = position dans le fichier (ordre `displayOrder` de la route).

---

## m011 — 04/06 « modals in exam texts: meaning and form » (d2 practice 75/15, 11 q.)

| Q | session | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- | --- |
| 1 | 2022 T | use | b use | OK | modal + base ; banque officielle fidèle |
| 2 | 2022 T | spend | c spend | **à retirer** | « would » non enseigné (04 ni avant) ; même geste et même texte que Q1 |
| 3 | 2023 T | Advice | a | OK | options officielles + « Prohibition » ajouté |
| 4 | 2013 G | Obligation | d | OK (expl. à corriger) | l'explication liste may/might/could et should → fuite vers Q3, Q9, Q10 |
| 5 | 2017 T | build | a | OK | options officielles + « builds » |
| 6 | 2015 T | could | c | réserve | clé par élimination sur le sens (enseigné) ; vote « could / could to » |
| 7 | 2012 T | to | b | **à retirer** | « would like + to » enseigné au 07 seulement (L06, C1) ; leurres = réponses des autres blancs, éliminables à vue |
| 8 | 2005 | can | d | réserve | vote : « can » dans 3 options sur 4 |
| 9 | 2017 G | might | b | réserve | vote « might / might to » ; l'explication livre la clé de Q10 |
| 10 | 2009 G | could | a | OK | — |
| 11 | 2001 | could | b | **à retirer** | rejet de « can » et « will » par la concordance des temps, non enseignée ; doublon du geste de Q6 |

Fidélité aux transcriptions : toutes les phrases citées sont conformes (2022 T ex. 1 ; 2023 T Q4 ; 2013 G Q4 ;
2017 G ex. 1 ; 2017 T ex. 3 ; 2015 T ex. 1 ; 2012 T ex. 1 ; 2009 G ex. 1 ; 2005 ex. 3 ; 2001 ex. 1). Les options
ajoutées (« Prohibition » en Q3, « Advice » en Q4) sont fausses et ne changent pas la clé.

### Points tranchés

- **« would » (Q2) et « would like to » (Q7) — retirés.** Le cours 04 n'enseigne pas *would* (il n'apparaît qu'au 05
  « Going further », hors programme, et au 06 dans *Would you mind*). Q2 est en outre le même geste que Q1 (même
  texte 2022 T, modal + base, leurres -s/-ing/to) : les deux questions de 2022 T se ressemblent parce qu'elles
  testent la même chose ; on garde Q1 (« could », enseigné). *Would like + to + base* n'est enseigné qu'au 07 (cours
  C1 du lot L06) ; et les trois leurres de Q7 (have, certainly, is) sont les réponses des autres blancs de la
  banque 2012 T, agrammaticaux à vue (« would like certainly join ») : la clé sort sans savoir. **Suivi pilote :**
  l'item 2012 T ② peut rejoindre `m022` (07/06, « the gerund or to + base »), qui ne le pose pas encore.
- **« could » au passé (Q6, Q11).** Aucun cours ne pose *could* = passé de *can*. **Q6 reste** : elle se résout par
  le sens enseigné (must = obligation et sans passé, can't contredit « amazed », could = possibilité) ; il suffit
  que l'explication dise le passé en une phrase. **Q11 sort** : « can » et « will » n'y sont écartés que par la
  concordance des temps (*believed* → *could*, *will* → *would*), notion non enseignée, et « She believed she can
  change… » se défend en anglais courant ; c'est en outre le même geste que Q6.
- **Indice de forme Q9 (« should » contre « might »).** « should » est le leurre officiel, faux par le sens (un
  inconvénient, pas un conseil) : il reste. Le défaut est ailleurs : « might » figure dans deux options (might,
  might to) et le vote donne la clé. Même défaut en Q6 (could, could to), Q8 (can, cans, can to) et Q11 (retirée) :
  le patron « clé + to » est systémique dans la mission.
- **Ordre.** Les deux items de la session de base (2022 T) restent en tête ; le tri par difficulté ne déplace que
  2017 G et 2009 G vers la fin (d3). Conforme (« la mission garde l'ordre » de la base). Accepté.

### Défauts et correctifs

**[MAJEUR] Q2 — notion non enseignée + doublon de geste.** Retirer la question.

**[MAJEUR] Q7 — notion non enseignée au 04, leurres éliminables à vue.** Retirer la question (renvoi à `m022`).

**[MAJEUR] Q11 — clé qui repose sur la concordance des temps (non enseignée), « can » défendable.** Retirer.

Après retrait : 8 questions (6 d2, 2 d3), étage d2 inchangé, rampe 2→3 honnête.

**[MAJEUR] Q6 — vote « could / could to » ; passé de could non dit.** Options et explication :

- options : `a` « must » (`english.modal.must-sans-passe-ni-futur`) · `b` « was able » (`english.modal.to-oublie`) ·
  `c` « could » (clé) · `d` « can't » (muet) ;
- explanation : « He tells a story in the past and speaks of the sites that were possible for him to visit. Could +
  base verb says what is possible, and it also works in a past story: the sites I could visit. "Must" has no past
  form and would mean an obligation, "can't" would say he was not able to visit them, which "amazed" contradicts,
  and "was able" loses the "to" that able always keeps. »

  Vérifié : « was able » n'exécute qu'une erreur (le sens « capacité passée » convient, le *to* manque) ; clé
  5 lettres, ni la plus longue (« was able », 8) ni la plus courte (« must », 4) ; « could » n'apparaît qu'une fois.

**[MAJEUR] Q8 — vote : « can » dans trois options.** Options et explication :

- options : `a` « is » (`english.verb.be-avec-base-verbale`) · `b` « may to » (`english.modal.to-en-trop`) ·
  `c` « had to » (`english.modal.fonction-confondue`) · `d` « can » (clé) ;
- explanation : « Can + base verb says what is possible for a giraffe: it can be up to 6 meters. "May to" adds a
  "to" that a modal never takes, and "is be" puts two verbs where one modal is needed. "Had to" would be a past
  obligation, which makes no sense for a fact about giraffes. »

  Vérifié : « may » a le sens juste (possibilité), seule l'erreur *to* reste ; « is » exécute exactement
  « be devant la base verbale » ; clé 3 lettres, pas la plus courte (« is », 2) ; aucune valeur répétée.

**[MAJEUR] Q9 — vote « might / might to » ; l'explication livre la clé de Q10.** Options et explication :

- options : `a` « should » (`english.modal.fonction-confondue`) · `b` « might » (clé) · `c` « are »
  (`english.verb.be-avec-base-verbale`) · `d` « have to » (`english.modal.must-pour-possibilite`) ;
- explanation : « The sentence lists a disadvantage: perhaps the photos do not match the real product. That is a
  possibility, so might + base verb. "Should" would give advice, "have to" would say the photos are obliged to be
  different, and "are be" puts two verbs where one modal is needed. »

  Vérifié : clé 5 lettres, ni la plus courte (« are », 3) ni la plus longue (« have to », 7) ; l'explication ne
  nomme plus « could » (clé de Q10) ; les trois leurres n'exécutent qu'une erreur chacun.

**[MAJEUR] Q4 — l'explication liste les modaux clés d'autres questions** (« may, might or could », « should » :
clés de Q9, Q10 et Q3, tirées au hasard dans le donjon). Explanation : « "Have to" + base verb is one of the two
ways of saying obligation, with must: stopping is necessary, the kids have no choice. A prohibition would forbid
the action, a possibility would only mean "perhaps", and advice would leave the kids free to choose. »

**[MAJEUR] Q1 — fuite vers `m022` (07/06 Q4).** L'énoncé cite « her passion for **working** with her hands », or
`m022` Q4 (même phrase 2022 T) demande justement « passion for ___ » → *working*. Énoncé de remplacement :
« (Exam 2022, technical) A text about a young welder says that she uses her hands "to fabricate works of art and
things people could ___ ." Which word completes the sentence? » (options et clé inchangées).

**[MINEUR] Q1 — explication imprécise** (« A modal takes no -s and no -ing ending » : c'est le verbe après le modal
qui n'en prend pas). Remplacer par : « After the modal "could" the verb stays in its base form: things people could
use. The verb after a modal takes no -s and no -ing ending, so "uses" and "making" are wrong. "Ability" is a noun,
not a verb, so it cannot follow a modal. »

**[MINEUR] Clé la plus courte** en Q1 et Q5 (base verbale nue face à ses formes fléchies) : inhérent au geste
« modal + base », non reconnaissable au vote ; acceptable une fois Q8 corrigée (2 clés sur 8).

Étiquettes de m011 : `base-verbale-deformee`, `to-en-trop`, `s-sur-le-modal`, `must-sans-passe-ni-futur`,
`must-pour-possibilite`, `fonction-confondue` — chacune exacte sur l'option qui la porte (vérifié option par
option ; « making » n'exécute que l'erreur -ing, *could make* étant juste).

