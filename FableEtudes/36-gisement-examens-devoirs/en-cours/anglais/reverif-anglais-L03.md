# Re-vérification — lot L03 (anglais 9ᵉ, gisement étude 36)

> Auditeur indépendant, 2026-10-17. Branche `wip/gisement-anglais-9eme`, commit `c2399779` (« L03 corrections
> d'audit »). Base : `audit-anglais-L03.md` et le journal `auteurs-notes/en-L03/CORRECTIONS.md`. Aucun fichier
> de `content/` modifié, aucune écriture git.
> Fichiers : `04-modals/exercices/06-exams-2005-2023-modals-meaning-and-form.json` (m011, 8 q.),
> `04-modals/exercices/07-exams-2011-2026-writing-advise-warn-set-rules.json` (m012, 10 q.),
> `08-…/exercices/06-exams-2002-2026-relative-pronouns.json` (m013, 8 q.),
> `08-…/exercices/07-exams-2002-2025-comparative-or-superlative.json` (m014, 7 q.),
> `08-…/exercices/08-exams-2002-2026-building-the-comparison.json` (m015, 12 q.), et `content/misconceptions.json`.
> Numérotation : Qn = position dans le fichier corrigé.

## 1. Gates

| gate | résultat |
| --- | --- |
| `content:check` | ✓ 120 matières, 29 874 questions, 1 069 étiquettes |
| `content:qa:strict -- --subject english` | ✓ 0 erreur, aucune clé suspecte |
| `content:tranche -- --subject english --chapters 04,08` | ✓ clé strictement la plus longue 0/106 ; positions a 29 % · b 23 % · c 26 % · d 22 % ; 1 paire proche, **hors L03** (`08/09-devoir…` #5 ↔ #7, lot L05) ; 2 candidats gabarit (ci-dessous) |

**Candidats gabarit** : m012 Q2 ↔ 09/15 Q3 (« What exactly must the article do? ») et m012 Q5 ↔ 09/15 Q1
(« sound arguments »). C'est le cadre voulu par la règle R3 du plan, appliqué à des consignes et des fonctions
différentes (conseiller / expliquer ; mettre en garde / persuader) : **parallèle justifié, pas un doublon.**
À transmettre à L04 : 09/15 Q1 cite « State at least three sound arguments » et a exactement trois clés, le défaut
déjà corrigé ici en m012 Q5.

## 2. Questions modifiées re-résolues à l'aveugle

Toutes les clés sont justes : 0 divergence.

| mission | Q | ma réponse | clé | verdict |
| --- | --- | --- | --- | --- |
| m011 | 1 | use | b | OK (plus de « working » dans l'énoncé) |
| m011 | 3 | Obligation | d | OK (l'explication ne nomme plus d'autre modal clé) |
| m011 | 5 | could | c | OK (must / was able / could / can't ; « could » une seule fois) |
| m011 | 6 | can | d | OK (is / may to / had to / can) |
| m011 | 7 | might | b | OK (should / might / are / have to ; plus de « could » dans l'explication) |
| m012 | 1 | a | a | OK |
| m012 | 3 | c | c | OK (consigne exacte, leurre « I hope… ») |
| m012 | 5 | b, d, e, f | b, d, e, f | OK (4 clés, plus de nombre annoncé ; consigne exacte) |
| m012 | 6 | c, a, d, b | c, a, d, b | OK (consigne exacte) |
| m012 | 8 | l1-r4, l2-r2, l3-r1, l4-r3 | idem | OK : appariement unique (calories → poids, vaisseaux → cœur) |
| m012 | 9 | a | a | OK |
| m013 | 1 | which | c | OK (définition dans l'énoncé ; d2, en tête) |
| m013 | 2 | who | a | OK (« that he ») |
| m013 | 3 | which | d | OK (glose « he is the subject ») |
| m013 | 4 | which | b | OK (« that they » étiqueté) |
| m013 | 5 | who | c | OK (« she ») |
| m013 | 7 | who | d | OK (« that they ») |
| m014 | 1 | more | d | OK (« At a young age » retiré) |
| m014 | 3 | biggest | c | OK (« big » officiel rétabli) |
| m014 | 4 | fun | b | OK |
| m014 | 5 | more | a | OK |
| m014 | 6 | less | c | OK |
| m014 | 7 | the most | d | OK : trois bienfaits → superlatif ; « the more » n'est plus défendable |
| m015 | 1 | biggest | d | OK (forme seule) |
| m015 | 2 | bigger | a | OK (plan 2×2) |
| m015 | 4 | better | a | OK (formes données, énoncé autonome) |
| m015 | 6 | newest | b | OK |
| m015 | 7 | tall | c | OK |
| m015 | 8 | more fashionable | idem | OK (variante « far more fashionable » ; plus de forme annoncée) |
| m015 | 9 | wisest | b | OK (« their own takes the place of the ») |
| m015 | 12 | largest | d | OK |

## 3. Suivi des défauts de l'audit

**Critiques (3/3 levés).** L'appariement de m012 (2019 G) est corrigé ; m014 2024 T et 2016 G (doubles réponses)
sont retirées.

**Majeurs (24/24 levés).**
- **m011.** Retrait de 2022 T « would », 2012 T « would like to » et 2001 ; fuite Q1 vers m022 ; votes Q5, Q6,
  Q7 ; explication Q3.
- **m012.** Q5 (nombre annoncé), Q1 et Q9 (doublons, option à deux erreurs).
- **m013.** Votes ; Q1 (2026 G) avec sa définition ; Q3 (2024 G) avec sa glose ; fuite vers Q5 corrigée côté
  L01 (01/06 Q6 dit « her 15-year-old daughter »).
- **m014.** Fuite vers m008 (énoncé retiré avec 2024 T) ; 2008 ; 2017 G.
- **m015.** short_answer ; Q4 autonome ; Q9 ; votes Q2, Q6, Q12 ; doublon Q1.

**Mineurs (12/12 levés).** Titres et fichiers 2005–2023 et 2011–2026 ; explication m011 Q1 ; citations m012 ;
« that they » étiqueté. Les points jugés acceptables sont laissés en l'état : clé la plus courte (who, use, build),
m012 Q10, m013 relative non déterminative, m015 « newer ».

## 4. Les trois écarts déclarés par l'auteur

- **m013, 2026 G : « what » devient « whose ».** **Accepté.** Avec « what » (4), la clé « which » (5) était
  strictement la plus longue. « whose » (5) l'égale sans la dépasser. Il est déjà un leurre officiel de 2025 T
  (Q2) et son rejet se fait par le sens, que l'explication donne (« would show possession »), sans règle hors
  programme. « whose » reste muet, comme il convient (le cours le range en « Going further »).
- **m014, 2023 G : « At a young age » retiré ; intro de 2025 G reformulée.** **Accepté.** La fuite est réelle :
  `09/11` Q5 a pour clé « At » dans « ___ a young age, children are capable of… ». L'énoncé garde
  « … children are capable of handling (much / more / most) than we may believe », qui suffit (indice « than »).
  La nouvelle intro de 2025 G (« A text on household chores explains: ») ne fuit pas vers `07/08` Q4
  (« communicating ___ » → clearly), vérifié.
- **m015, short_answer : l'explication cite la réponse.** **Accepté.** C'est le texte demandé par l'audit :
  l'explication n'est montrée qu'après la réponse, et une explication qui ne nomme pas la forme juste
  n'enseigne rien.

## 5. Étiquettes

Registre relu : `content/misconceptions.json` de la branche.

- **`english.comp.degre-sans-comparaison` (créée).** Textes fr, en et ar conformes à l'audit. Elle porte sur
  trois questions distinctes, sans aucun `multi` ni `matching` :
  - m014 Q4 : « funnier », « funniest », « most fun » ;
  - m014 Q6 : « least » ;
  - m015 Q7 : « taller », « tallest ».

  Chaque option n'exécute qu'une erreur ; « more tall » à deux erreurs reste muet. **OK.**
- **`english.comp.much-many-au-lieu-du-comparatif` (créée).** Elle porte sur trois questions distinctes :
  - m014 Q1 : « much », « many » ;
  - m014 Q5 : « much » ;
  - m014 Q6 : « much ».

  Chaque option n'exécute qu'une erreur. **OK.**
  **[MINEUR]** Dans le libellé `ar`, la virgule arabe entre deux mots latins « (than، sooner…) » coupe le segment
  de gauche à droite : à l'affichage RTL, l'ordre peut s'inverser. Remplacer par une virgule latine :
  « (than, sooner…) », comme dans les libellés existants (« (yesterday, last…, ago) »).
- **`english.rel.sujet-en-double` (élargie à « that »).** Les trois libellés sont conformes. Les étiquettes
  publiées sur who / which restent exactes. Elle porte « that he » (m013 Q2) et « that they » (m013 Q4, Q7). **OK.**
- `what-comme-relatif` est inchangée, et « when » et « where » restent muets : conforme (l'élargissement était
  optionnel).

Toutes les autres étiquettes des cinq missions sont relues option par option : chacune nomme exactement l'erreur
exécutée.

## 6. Fuites, dans les deux sens

J'ai contrôlé les fuites par script, dans les deux sens. Le script cherche la phrase officielle avec sa clé dans
l'énoncé, l'explication et les options de chaque question de `content/english/` (missions et quiz). Je les ai aussi
contrôlées à la lecture.

- **L03 → autres lots : aucune** (m011 → m022 et m014 → m008 sont levées).
- **Autres lots → L03 : une fuite reste ouverte.**
  - **[MAJEUR, hors L03, lot L06]** `07-reported-speech/exercices/07-exams-2007-2023-pronouns-in-exam-texts.json`
    Q2 écrit encore « A mother writes about her daughter, **who** chats… ». Cela donne la clé de m013 Q5
    (« My daughter, ___ is 15 »). Correctif inchangé : « A mother writes about her teenage daughter and the
    Internet: ».
  - 01/06 Q6 est corrigée.
- **À l'intérieur de L03 : aucune fuite.** Notamment m011 Q6 ↔ m015 Q7 (girafe : chaque énoncé cache le blanc de
  l'autre), m013 Q8 ↔ m015 Q12 (tigres), m013 Q1 ↔ m015 Q9 (2026 G), m014 Q5 ↔ m015 Q12, et m012 Q1 ↔ Q5
  (mineur, déjà signalé).

## 7. Nouveaux défauts (manqués à l'audit)

**[MAJEUR] m012 Q7 et Q10 : les explications désignent une option par sa place.** Les options sont mélangées à
l'affichage. J'aurais dû le relever à l'audit.

- Q7 : « The **first** sentence gives advice… The **last** one describes… ». Explanation de remplacement :
  « The sentence with "should" and "because" gives advice (should + base verb) and its reason: tired students
  study badly. One sentence has "because" but only describes what some students do. Another gives advice without
  any reason. Another describes a problem and its result and gives no advice to the reader. »
- Q10 : « Only the **first** line is well formed. » Remplacer cette phrase par : « Only "You mustn't leave the
  machines on…" is well formed. »

**[MINEUR] m012 Q3 : « …and the last one expresses a wish ».** C'est une énumération, pas une position, mais ce
texte venait de mon propre correctif. Remplacer par « …and the sentence with "hope" expresses a wish, not
regret. »

**[MINEUR] Registre `gisement.json` (`…/sources-externes/web-9eme-base-english/`).** Seuls les noms de fichiers
ont été mis à jour. Il faut encore retirer les sessions des questions supprimées et mettre `etapes` au nombre de
questions de chaque mission. Codes déduits de l'ordre du plan : C01 = 2026 G … C42 = 2001.

| mission | sources à retirer | `etapes` | note à ajouter |
| --- | --- | --- | --- |
| m011 | `C28#2` (2012 T), `C42#2` (2001) | 8 | — |
| m012 | `C33#5` (2009 G) | 10 | — |
| m014 | `C06#3` (2024 T), `C10#3` (2022 T), `C15#4` (2019 G), `C21#4` (2016 G), `C31#4` (2010 G) | 7 | écart R6 de 2024 T et 2016 G (double réponse « more » / « many ») |

À vérifier contre `plan-examens-v2.json` avant d'écrire.

## 8. Bilan et verdict

- **Questions re-vérifiées :** 45, dont 31 modifiées et re-résolues à l'aveugle.
- **Clés fausses :** 0.
- **Défauts de l'audit :** tous levés (3 critiques, 24 majeurs, 12 mineurs).
- **Écarts de l'auteur :** 3, tous acceptés.
- **Étiquettes :** 2 créées et 1 élargie, conformes. Un mineur de rendu dans le libellé `ar` de
  `much-many-au-lieu-du-comparatif`.
- **Nouveaux défauts L03 :** 1 majeur (explications ordinales de m012 Q7 et Q10) et 2 mineurs (m012 Q3, registre).
- **Hors L03 :** 1 fuite ouverte (07/07 Q2, lot L06, vers m013 Q5) et 1 défaut à transmettre à L04 (09/15 Q1).

**Verdict : livrable après deux retouches d'explication (m012 Q7 et Q10)**, sans re-audit ; un contrôle à vue des
deux phrases suffit. Le registre et la virgule du libellé `ar` peuvent suivre dans le même commit. La fuite de
07/07 Q2 relève de L06 et ne bloque pas L03.
