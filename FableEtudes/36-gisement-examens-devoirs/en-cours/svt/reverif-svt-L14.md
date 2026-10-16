# Re-vérification ciblée — gisement SVT 9ᵉ, devoirs, lot L14

Auditeur indépendant. Objet : le commit `ae44e275` (`/home/user/wt-svtses`), comparé à `278d46db`, qui applique
`audit-svt-L14.md`. J'ai lu le journal `auteurs-notes/svt-L14/CORRECTIONS.md`, transmis par le coordinateur. Je
n'ai ouvert aucune source de devoir. Aucune écriture dans `content/` ni dans git.

Rapport écrit au fil de l'eau (état : terminé).

## Contrôles outillés

- `content:gisement:controle` sur les six fichiers : **✓ 41 textes, aucune reprise de 8 mots ni de 6 mots, aucune
  donnée commune avec un devoir source.**
- `content:check` : ✓, 120 matières validées.
- `content:qa:strict --subject sciences-vie-terre` : 0 erreur (1 avertissement préexistant).
- `content:tranche` (ch. 02, 03, 07, 09, 11, 13) : clé strictement la plus longue 0/507. Paires proches de 07/10 :
  Q1↔Q4 0,53, Q1↔Q3 0,52, Q3↔Q4 0,47.
- Figures rendues dans Chromium, 232 px, conteneur `dir="ltr"` :
  - **07/10** (Q1 à Q4) et **13/08** (Q6) : SVG identiques octet pour octet à ceux de l'audit. Rendu propre, figures
    vraies, aucune clé marquée. La valeur 2,0 g/L à 140 min, nouvelle donnée de 07/10 Q5, est bien celle de la courbe.
  - **11/11** : la seule modification est le premier « الحيض » (x = 48, `start`). Il ne touche plus l'axe, ne
    chevauche ni la courbe ni « يوم 1 ». Les trois prompts portent la même figure (Q1, Q4, Q7).
- Rendu bidi dans Chromium `dir="rtl"` des nouvelles chaînes à chiffres : liste « في الدّقائق 0 و15 و40 و70 و100
  و140 و180 », « 31 − 14 = 17، أي في اليوم 17 ✓ » et « 15 + 14 = 29 يومًا ✓ ». L'ordre affiché est l'ordre source.

## Mes textes, tels qu'appliqués

Les correctifs M1 à M12 et les mineurs 1 à 7, 9, 10 et 11 sont repris au mot près, sauf les écarts ci-dessous.
Je les ai relus dans le fichier.

## Re-résolution à l'aveugle (questions retouchées et voisines)

| fichier | Q | ma réponse | clé | verdict |
| --- | --- | --- | --- | --- |
| 03/13 | Q1 | a, b, c | idem | OK — l'explication ne nomme plus les méninges |
| 03/13 | Q2 | b | b | OK |
| 03/13 | Q3 | a, b, c, f | idem | OK — l'explication ne dit plus « عدسة » |
| 03/13 | Q4 | c | c | OK |
| 03/13 | Q7 | c | c | OK — plus de redite de Q2 ; dans le cours, « النّخاع » seul désigne la moelle épinière |
| 02/10 | Q1 | b, d, e | idem | OK |
| 02/10 | Q2 | b | b | OK — autonome ; la scène (épine) ne recopie aucune option de Q1 |
| 02/10 | Q3 | d | d | OK — retrait de la main |
| 02/10 | Q4 | c | c | OK — autonome (éternuement), d est un faux critère plausible |
| 02/10 | Q5 | a, b, c | idem | OK — « طرفه السّفليّ » englobe le muscle de la cuisse |
| 02/10 | Q6 | l1-r1, l2-r2, l3-r3 | idem | OK — trois profils distincts, plus de redite de Q5 |
| 07/10 | Q1 | c (70) | c | OK |
| 07/10 | Q3 | 30 | 30 | OK — instants de mesure donnés |
| 07/10 | Q4 | b (1,7) | b | OK |
| 07/10 | Q5 | c | c | OK — 2,0 / 1,0 à 140 min ; ne répète plus 2,7 |
| 09/13 | Q2 | l1-r2, l2-r4, l3-r3, l4-r1 | idem | OK |
| 09/13 | Q4 | d | d | OK |
| 09/13 | Q6 | c | c | OK — d est la réabsorption (définie en Q2, r4), simple élimination par le savoir |
| 11/11 | Q1 | a | a | OK — n'annonce plus de durée de cycle |
| 11/11 | Q4 | b (30) | b | OK |
| 11/11 | Q5 | b (17) | b | OK — 31 − 14 = 17 ; couple absent du sujet |
| 11/11 | Q6 | b (29) | b | OK — 15 + 14 = 29, de J16 à J29 = 14 jours ; autonome |
| 11/11 | Q7 | d (J29) | d | OK — J24 au pic, J8 et J16 bas avant l'ovulation, J29 en descente ; clé unique |
| 13/08 | Q3 | a | a | OK |
| 13/08 | Q5 | b | b | OK, mineur résiduel (clé la plus courte, voir écart 2) |
| 13/08 | Q6 | d | d | OK — plus de rappel qui désigne la clé |
| 13/08 | Q7 | a | a | OK |
| 13/08 | Q8 | a, c | idem | OK, mineur résiduel (option correcte c la plus longue d'un caractère) |

**Clés fausses : 0.**

Fuites et autonomie, toutes les explications relues dans l'ordre d'émission :
- aucune explication ne donne la clé d'une question suivante ;
- aucun énoncé ne renvoie à une autre question ;
- 13/08 Q8 ne reprend plus aucune clé de Q5 à Q7.

Seule reste la règle « les règles suivent la chute des hormones », dans l'explication de 13/08 Q6 puis dans la clé de
Q7. C'est un fuite de règle, enseignée au cours 11, et non de réponse : acceptée comme à l'audit.

## Étiquettes (décisions du pilote)

- **`bio.contra.regles-supprimees-par-la-pilule`** : créée avec le libellé fr/ar/en proposé (restreint à la pilule
  combinée et aux jours d'arrêt). Posée sur 13/08 Q6 b et Q7 b, deux distracteurs qui exécutent exactement cette
  erreur. ✓
- **`bio.circ.artere-sang-oxygene`** : libellé élargi (« oxygène, nutriments » ; l'artère du cœur vers un organe, la
  veine retour au cœur). Posée sur 07/10 Q5 a et b. ✓ Les 9 autres placements du corpus ont été relus, et le libellé
  reste exact pour chacun :
  - `07-ad-dawaran/quiz` Q2 ;
  - `07/06-defi-concours` Q4 ;
  - `07/01-tamrin` Q3 ;
  - `07/03-boss` Q2 ;
  - `07/08-examen-2020` Q6 ;
  - `09/10-examen-2015` Q1 ;
  - `10/07-examen-2021` Q2 et Q3 ;
  - `08/12-examens-2019` Q9.

  Tous définissent artère ou veine par l'oxygène qu'elles portent, ou inversent le sens dans la petite circulation.
  Ce dernier cas est couvert par la seconde moitié du libellé, comme avant l'élargissement.
- **`bio.cycle.compte-depuis-l-ovulation`** : non créée. 11/11 Q4 d (15) et Q6 d (14) restent sans étiquette, ce qui
  est permis et ne constitue pas un défaut.

## Écarts déclarés par l'auteur

1. **09/13 Q5 : étiquettes non posées sur un `multi` — écart fondé.** `schema.ts` (`wireOptionSchema`, `.strict()`)
   refuse `misconceptionTag` sur les options `multi`, `ordering` et `matching`. Mon mineur 8 était impossible, tout
   comme l'étiquette `efficacite-vaut-protection-ist` que j'avais proposée sur 13/08 Q8 e. C'est mon erreur, à
   retirer de l'audit.
2. **13/08 Q5 : clé la plus courte — mineur, non bloquant.** Par ma mesure sans diacritiques, la clé fait 45
   caractères contre 49 à 51 ; un seul cas dans le lot. Correctif proposé, vérifié :
   - texte : b = « لا تحدث الإباضة، لأنّ التّغيّر الدّوريّ للهرمونين يغيب » ;
   - longueurs : 51 / **49** / 50 / 49, ni la plus courte ni la plus longue ;
   - sens inchangé et conforme au cours 13 ; aucune fuite vers Q8.
3. **03/13 Q7 : la clé n'a plus « الشّوكيّ » — accepté.** Le cours 01 emploie « النّخاع » seul pour la moelle
   épinière (« في داخل النّخاع »), le bulbe y est « البصلة الشّوكيّة ». Aucune lecture concurrente. Longueurs 57 / 48
   / 47 / 47 : la clé n'est ni la plus longue ni la plus courte.
4. **11/11 : clé trois fois en position b — accepté.** Les options sont mélangées à chaque affichage
   (`shuffleOptions`). La lettre n'est pas visible : simple rangement, sans indice.
5. **07/10 : paires proches 0,47 à 0,53 — accepté et justifié.** Même document, contexte imposé par l'autonomie,
   trois lectures distinctes (pic intestinal, délai entre pics, hausse sanguine). À citer comme exercice parallèle
   voulu au rapport de tranche.

## Mineurs restants (non bloquants)

1. **13/08 Q5**, option b, texte exact :
   - avant : « لا تحدث الإباضة، لأنّ التّغيّر الدّوريّ يغيب تمامًا » ;
   - après : « لا تحدث الإباضة، لأنّ التّغيّر الدّوريّ للهرمونين يغيب ».
2. **13/08 Q8**, option c, texte exact :
   - avant : « تعود الإباضة إلى الحدوث بعد أن تتوقّف المرأة نهائيًّا عن تناول الأقراص » ;
   - après : « تعود الإباضة بعد أن تتوقّف المرأة نهائيًّا عن تناول الأقراص ».
   - Longueurs : 51 / 66 / 56 / 45 / 40 / 60, la plus longue devient b, qui est fausse.
   - Le défaut vient de mon propre texte.

## Bilan

- Questions re-résolues : 28 (retouchées et voisines) ; clés fausses : 0.
- Majeurs restants : 0. Mineurs restants : 2, textes exacts ci-dessus, non bloquants.
- Contrôle anti-copie : ✓.
- **Verdict : livrable.** Les deux mineurs peuvent être appliqués sans nouvel audit.

## Suite donnée par le pilote (2026-10-16)

Mineurs 1 (13/08 Q5 b) et 2 (13/08 Q8 c) appliqués mot pour mot. **L14 prêt à livrer.**
