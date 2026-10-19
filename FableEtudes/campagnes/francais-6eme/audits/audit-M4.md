# Audit M4 — missions du gisement, french-6eme `07` et `08` (m025–m033)

> Auditeur indépendant (opus), 2026-10-19. Grilles : `prompt-auditeur.md`, `content-audit`, la carte `assign-M4.md`, `PLAN-gisement.md` (R1–R10, E1–E8).
> Les transcriptions et les PDF officiels ont été relus. J'ai vu en image les pages 1 de 2022 et de 2025 et la page 2 de 2025.
> J'ai re-résolu à l'aveugle les 74 questions des 9 fichiers avant de lire le rapport de l'auteur. Rien n'a été modifié sous `content/`, aucune écriture git.

## 0. Gates

| Contrôle | Résultat |
| --- | --- |
| `content:check` | ✓ french-6eme : 73 exercices, 502 questions |
| `content:qa -- --subject french-6eme` | ✓ (l'erreur du 02 a disparu) |
| `content:tranche … 07, 08 --fresh --strict-longest` | ✓ clé strictement la plus longue : 0/110 ; positions 27/24/25/24 %. ⚠ 19 paires proches (§ 3), 10 groupes gabarit |
| `content:gisement:controle` (devoir m033) | ✓ 0 plage ≥ 8 mots, 0 ≥ 6, 0 exercice source à 2 ou 3 données |
| Rendu | ✓ aucun `_` ni `*` dans les 9 fichiers |
| `short_answer` | aucune dans ce lot |
| Étiquettes | toutes au registre. **Hors carte, à ajouter par le pilote** : M7 `fr.accord.verbe-non-accorde-au-sujet`, `fr.dialogue.ponctuation-oubliee`, `fr.dialogue.verbe-introducteur-inadapte`, `fr.pronom.possessif-accorde-au-possesseur`, `fr.recit.contradiction-non-vue` ; M8 `fr.accord.verbe-non-accorde-au-sujet`, `fr.conj.futur-conditionnel-1re-personne`, `fr.conj.futur-mal-forme`, `fr.lettre.registre-melange`, `fr.phrase.negation-mal-placee`, `fr.temps.indicateur-de-temps-ignore`. Leurs libellés nomment bien l'erreur. |

## 1. Synthèse

74 questions re-résolues : toutes les clés actuelles sont justes. Pourtant, **3 questions ont deux réponses défendables ou une clé contraire à la consigne officielle** (critiques), et **9 paires d'items jumeaux se donnent la réponse** l'une à l'autre.

| Mission | q | Crit. | Maj. | Min. |
| --- | --- | --- | --- | --- |
| m025 `07/06` | 7 | 0 | 2 | 2 |
| m026 `07/07` | 6 | 0 | 1 | 1 |
| m027 `07/08` | 9 | 0 | 2 | 1 |
| m028 `07/09` | 9 | 0 | 0 | 1 |
| m029 `08/06` | 10 | 2 | 0 | 1 |
| m030 `08/07` | 10 | 0 | 4 | 1 |
| m031 `08/08` | 7 | 0 | 3 | 1 |
| m032 `08/09` | 8 | 1 | 0 | 2 |
| m033 `08/10` | 8 | 0 | 1 | 1 |

## 2. Critiques

### C-1 — `08/06` q8 (2017, enrichir) : l'option d respecte aussi la consigne
« Ce matin, … dans la classe, à l'école » contient un complément de temps et un complément de lieu : c'est bien « au moins deux compléments non essentiels de sens différents ». Remplacer d :
- `Hier matin, dès huit heures, les élèves ont souhaité la bienvenue à Caroline.` (deux compléments de temps, sans étiquette). Longueurs 75/75/80/77, la clé (75) n'est pas la plus longue.
- Explication : `Il faut deux compléments qui disent des choses différentes : ici le moment (ce matin) et la manière (avec gentillesse), tous deux non essentiels. Dans la classe et à l'école disent deux fois le lieu, hier matin et dès huit heures deux fois le moment, et à toute sa famille ajoute un complément essentiel du verbe.`

### C-2 — `08/06` q10 (2009, déplacer) : l'option b ne déplace que des compléments non essentiels
« Je me mets pieds nus, à travers la scène, à danser » revient à placer les deux compléments non essentiels avant « à danser ». Elle répond donc littéralement à « déplace seulement des compléments non essentiels ». Remplacer b par `À travers la scène, pieds nus, je me mets.` (`fr.complement.essentiel-non-essentiel-confondus` : le complément essentiel disparaît). Longueurs 52/42/51/51.
- Prompt, fin : `Quelle réécriture déplace les compléments non essentiels et reste une phrase correcte ?`
- Explication, fin : `En revanche, « à danser » complète le verbe se mettre : le placer en tête, le séparer du verbe ou le supprimer rend la phrase fausse.`

### C-3 — `08/09` q7 (2025, Q3 b, doute n° 3) : la clé n'est pas « trouvée dans le texte »
La consigne officielle, citée par q6 et reprise par « Même question », demande un contraire « **trouvé dans le texte** ». *Apparait* n'est pas dans le texte. *Surgit* y est (« Une tête à la chevelure hérissée surgit… », et le sujet le reprend en conjugaison 2) : c'est la réponse attendue. Écarter *surgit* rend la clé contraire à la consigne. Remplacer c par `surgit` (clé). Longueurs 9/8/6/8.
- Explication : `Disparaître, c'est cesser d'être visible. Le texte emploie surgir (« Une tête … surgit ») : apparaître tout à coup. C'est le contraire demandé, pris dans le texte. Se coucher et s'éteindre disent à peu près la même chose que disparaître pour le soleil, et ralentir parle de vitesse.`

## 3. Paires proches et fuites (le donjon tire au hasard)

Sur les 19 paires signalées, **les tableaux** (08/06 q1–q6, et 07/06 q1 ↔ 08/06 q1) **et 08/08 q6 ↔ q7** (présent → passé composé, puis futur) **ne fuient pas**. Ce sont des exercices parallèles voulus, sur des phrases officielles différentes.

**Fuient** : l'énoncé de l'une affiche la clé de l'autre. Correctif uniforme : garder les deux questions mais **laisser tous les blancs vides dans les deux énoncés** et nommer le blanc visé (textes vérifiés, plus aucune clé visible).

| Paire | Fuite | Énoncé corrigé |
| --- | --- | --- |
| 07/06 q6 ↔ q7 | q6 affiche « écris », q7 affiche « Écoute » | q6 : `(Concours 2018) Conjugaison, question 2. La maîtresse dit à ses élèves : « Ecoutez puis écrivez la phrase ! » Elle s'adresse maintenant à Ousman seul : « … puis … la phrase ! » Quel verbe complète le premier blanc ?` · q7 : la même phrase, avec `Quel verbe complète le second blanc ?` |
| 07/07 q4 ↔ q5 | q5 affiche « vieille » | q5 : `(Concours 2019) Même réécriture : « Elle était très …, car … visage était couvert de plis … » Quels mots complètent le deuxième et le dernier blanc ?` |
| 07/08 q1 ↔ q2 | q2 nomme la réponse « non » ; q1 donne elle-même l'indice (« Lucile raconte qu'elle a levé la main sans y penser ») | q1 : `(Concours 2022) Compréhension, question 1 : « Lucile a exprimé à sa professeure exactement ce qu'elle voulait. » Oui ou non : quelle réponse est juste ?` · q2 : `(Concours 2022) Toujours à la question 1 : quels passages du texte permettent de répondre ? Choisis TOUS les bons.` (options et clé inchangées) |
| 08/07 q1 ↔ q2 | q2 affiche « Nous, nous pouvons » | q2 : `(Concours 2026) Même réécriture : « …, … … même commencer dès ce soir ! » … les filles. Quelle forme du verbe s'écrier complète le dernier blanc ?` |
| 08/07 q3 ↔ q4 | chacune affiche la clé de l'autre | q3 : `(Concours 2021) Conjugaison, question 3 : « Parlant à sa fille, la maman dit : « Tu peux garder le chat mais tu t'occuperas de lui. » » Que dit-elle en parlant à ses deux enfants ? « Vous … garder le chat mais … de lui. » Quelle forme complète le premier blanc ?` · q4 : `(Concours 2021) Même consigne : « Vous … garder le chat mais … de lui. » Quelle forme complète le second blanc ?` |
| 08/07 q5 ↔ q6 | q6 affiche « Allez » | q6 : `(Concours 2016) Même phrase : « … où vous …, ce n'est pas notre affaire. » Quelle forme de vouloir complète le second blanc ?` |
| 08/07 q9 ↔ q10 | q10 affiche « est allé » | q10 : `(Concours 2018) Même phrase : « La semaine dernière, le grand-père de Sophie … à l'école mais il … raconter ses aventures. » (Le participe de vouloir est voulu.) Quels mots complètent le second blanc ?` |
| 08/08 q1 ↔ q2 | q2 affiche « sont remontés » | q2 : `(Concours 2024) Même réécriture : « Les phoques … à la surface. Ils … de drôles de pirouettes. » Quelle forme complète le second blanc ?` |
| 08/08 q3 ↔ q4 | q4 affiche « nous sommes repassés » | q4 : `(Concours 2019) Même phrase : « À la fin de la séance, nous … par la place de la gare routière, mais nous … le vieillard. » Quelle forme complète le second blanc ?` |

**Mineur** : 08/09 q1 ↔ q2. La consigne officielle (« deux détails qui le montrent ») présuppose « vrai ». C'est le texte du sujet lui-même : accepté.

## 4. Majeurs (hors fuites)

- **m025 q3 — redemande `07/quiz#1`** (« quel groupe est le complément de temps », leurre de lieu), alors que la carte l'interdit. De plus, la phrase est inventée mais étiquetée « (Concours 2016) ». **Supprimer q3.** La mission garde 6 questions ; aucune variante proposée ne redemanderait rien et n'afficherait la clé de q2.
- **m027 q5 — l'option b se défend.** Au moment où la mère réagit (« C'est une idée fabuleuse ! »), Lucile n'a pas encore dit que c'était une erreur. « Elle n'a pas compris que c'était une erreur » peut donc expliquer l'enthousiasme. Remplacer b par `Parce que Lucile lui a dit qu'elle adorait le théâtre.` (`fr.lecture.deduction-sans-indice`). Longueurs 98/54/81/60.
- **m031 q6 b « ont arrivés » — deux erreurs dans une option étiquetée**, dont l'accord avec *avoir* (borne F5). Remplacer par `ont arrivé` (`fr.conj.auxiliaire-mal-choisi`). Longueurs 11/10/12/12.
- **m033 q1 — ordre des paragraphes non unique.** L'option b met « tu poses une question à Malek » en premier, alors que le cours du 07 (l.304) place la question en dernier. Remplacer b par `Tu salues Malek et tu lui donnes de tes nouvelles.` L'ordre b, d, a, c devient unique : salut et nouvelles, la ville, puis les lieux, puis l'invitation.
- Les fuites du § 3 comptent comme majeurs : 07/06, 07/07 et 07/08 une chacune ; 08/07 quatre ; 08/08 deux.

## 5. Mineurs

- **Fidélité des consignes** (R1, mot pour mot) :
  - 08/06 q1 : la consigne de 2025 est « Remplis le tableau suivant avec des éléments de la phrase ci-dessus. » et non « Lis la phrase et remplis le tableau. ».
  - 07/06 q1 et 08/06 q2–q6 : l'officiel dit « remplis le tableau **suivant** ».
  - 07/09 q4 et q6 : « (Intègre un court dialogue dans ton récit). », point hors de la parenthèse, comme l'imprimé.
- **07/06 q4**, explication : « dites va avec vous » ne correspond à aucune option. Remplacer par `et disons va avec nous`.
- **07/08 q8**, explication : `Murmurer, c'est presque le contraire (parler très bas) ; oublier et cacher ont un autre sens.`
- **08/09 q8** : l'option a s'appuie sur le texte (« L'idée plut aux deux garçons »). Son étiquette `deduction-sans-indice` est donc fausse : à rendre muette.
- **08/09**, doute n° 2 : q1 et q8 ont une seule réponse ✓.
- **08/10** : q4 (description ou action) refait le geste du quiz 08 q5, de 02 q6 et de 04 q5. C'est toléré pour un devoir de préparation.
- **« Ne pas redemander » touché par mes correctifs B4** : le quiz 07 q5 (grosse) et la mission m026 q6 (grosse valise), puis 08/04-defi q1 (veulent) et m030 q8 (veulent). Chaque mission reprend la phrase officielle, et toutes les formes d'adjectif et de *vouloir* sont déjà prises ailleurs. J'accepte ces chevauchements : le geste diffère (réécriture officielle contre QCM ou saisie).
- **m031 et 08/quiz q4** : *sont arrivés* deux fois (oiseaux migrateurs contre garçons). C'est une reprise officielle : accepté.

## 6. Doutes de l'auteur

1. **« les mains dans les poches » (2019) et « un peu angoissés » (2009)** : acceptés comme compléments de manière. Ce sont les réponses attendues par le sujet (seule case restante du tableau, seul groupe qui répond à « comment ? »), et c'est cohérent avec le test du cours. En grammaire savante, ce sont une construction absolue et un adjectif détaché ; ce n'est pas exigible en 6ᵉ.
2. **Questions d'opinion converties en QCM** :
   - m027 q9 : réponse unique ✓ ;
   - m027 q5 : non, l'option b se défend (§ 4) ;
   - m032 q1 et q8 : réponse unique ✓ (retirer l'étiquette de q8 a).
3. **m032 q7** : non. Le contraire « trouvé dans le texte » est *surgit* (C-3).
4. **Missions raccourcies, items fusionnés** : accepté. Les jumeaux restés séparés (m026 q4–q5, m030, m031) doivent recevoir le même traitement anti-fuite (§ 3).

## 7. Verdict

**À corriger** :
- 3 critiques (C-1 à C-3) ;
- les 9 énoncés à blancs vides du § 3 ;
- 4 majeurs (m025 q3, m027 q5, m031 q6, m033 q1).

Tous les textes ci-dessus sont vérifiés : une seule réponse, clé jamais strictement la plus longue, aucune clé visible dans un autre énoncé. La salle blanche du devoir est respectée.
