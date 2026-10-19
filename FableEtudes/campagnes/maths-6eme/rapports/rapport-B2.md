# Rapport de l'auteur — lot B2 (`math-6eme`, chapitres `07` à `12`)

Mise à niveau des six chapitres servis depuis la fiche validée (`programme/6eme-base/maths.md` §1 bis, §2 quinquies / nonies / decies, §3.2, §4, §6.1) et PLAN § 3 (M1–M4). Notes détaillées (table des écarts par chapitre, puis le fait) : `auteurs-notes/B2/NOTES.md`.

## Bilan chiffré

| chapitre | questions ajoutées | questions modifiées / remplacées | cours / résumé |
| --- | --- | --- | --- |
| `07-criteres-divisibilite` | 17 (quiz +2, 01 +2, 02 +4, 03 +3, 04 +2, 05 +4) | 11 (Q3 quiz, 01-Q5/Q6, 02-Q2/Q3/Q6, 03-Q2/Q4/Q5, 04-Q3/Q5/Q6) + clés rééquilibrées | inchangés (déjà complets) |
| `08-fractions-sens-lecture` | 17 | 3 (02-Q5 options triées, 03-Q5 remplacée par une question à figure, 04-Q4) | cours : 1 correction de rendu (gras coupé par un saut de ligne) |
| `09-fractions-equivalentes` | 15 | 3 (quiz Q2, 02-Q6, 04-Q6) | inchangés |
| `10-comparaison-fractions` | 13 | 4 (02-Q5, 03-Q6, 04-Q3 et Q5 remplacées) | **cours : section neuve** « مقارنة كسر بعدد صحيح » ; résumé +1 puce ; gras corrigé |
| `11-addition-soustraction-fractions` | 17 | 4 (indices « وحّد على N » retirés du d4) | inchangés |
| `12-fractions-decimales` | 17 | 0 | inchangés |
| **total** | **96** | **≈ 25** | |

Tout ajout est **en fin de fichier** avec `difficulty` ≥ au maximum du fichier (les identifiants dérivés du rang après tri ne se décalent pas). Aucun slug, `displayOrder`, id ou nom de fichier d'exercice modifié. Un exercice reste ≤ 12 questions (maximum atteint : 10).

## Écarts trouvés et corrigés, par chapitre

- **07** — aucun écart de cours. Exercices : le **reste lu sans division**, les chiffres manquants à solutions multiples, les plus grand/petit nombres de n chiffres, l'arrangement 4-3-0-5, les multiples communs de 2 et 5 entre deux bornes, le problème de l'âge n'étaient jamais exercés. Défauts : méta-options « لا يمكن المعرفة » (01-Q6, 03-Q2, Q5), **clé la plus longue** (quiz Q3, 02-Q2), étiquette inexacte (02-Q3 : 27, 81, 18), options non triées.
- **08** — cours complet. Jamais exercés : la fraction comme **rapport** (40/60, 15/10), le partage (6/5), le quotient exact vs approché (9 ÷ 7), la lecture en lettres de fractions > 1, les parts égales, un total à déduire (7/24), le diagramme (600/1300). **Aucune figure** dans tout le chapitre ; la demi-droite graduée (03-Q5) n'avait pas de dessin. Option « لا أحد » non idiomatique.
- **09** — cours complet. Clé la plus longue au quiz (Q2) ; séparateur arabe « ؛ » dans des listes de fractions ; jamais exercés : fractions > 1 (72/56), terme manquant au **dénominateur**, توحيد المقامات d'un entier, séries sous contrainte, intrus, conversion دكل → L, figures.
- **10** — **la leçon 40 n'était pas dans `chapter.json`** (`manuel.pages` « 85-88 » seul) et sa comparaison à un **entier** n'était enseignée nulle part. Le gabarit « قارن بين X و Y (وحّد على N) » faisait 29 questions sur 30, avec l'indice de méthode jusqu'au d4 ; méta-options (02-Q5, 03-Q6).
- **11** — cours complet. Les cinq fichiers étaient des calculs isolés : aucun problème (L42 ex. 2, 4, 5, 6, 7 ; L57 ; L48 ; L40 ex. 16 ; épreuve T3 situation 1), indices « (وحّد على N) » au d4, aucune figure.
- **12** — cours complet. Jamais exercés : le « **quand possible** » (11/7, 4/30, 5/108 impossibles ; 3/12, 3/75 après réduction), le piège 21/300, le numérateur décimal, 10 000, les mesures en deux écritures, le rangement mêlé ; gabarit ; aucune figure.
- Errata (§6.1) : aucune donnée fautive reprise (n° 18–19, 25–29, 30–33, 36–37, 56, 58 examinés). L29 ex. 5 (mal posé) et L57 ex. 4 (volume, ⛔) non repris. L31 ex. 12 repris en **variante** (3/10 lu par le rédacteur, non déclaré).

## Reprises déclarées (`manuel`)

- Manuel 102609 : `07` — 01 (L26 ex. 3أ, L25 ex. 4ج), 02 (L26 ex. 4, 7ب ; L25 ex. 7, 9), 03 (L26 ex. 3ج, 7ب ; L25 ex. 6), 04 (L26 ex. 4, 6, 7ب ; L25 ex. 10), 05 (L25 ex. 2, 9 ; L26 ex. 8). `08` — 01 (L18 ex. 4, 7), 02 (L18 ex. 8 ; L40 ex. 1), 03 (L40 ex. 2), 04 (L18 ex. 9), 05 (L18 ex. 6ب, 10). `09` — 01 (L28 ex. 6), 02 (ex. 5, 7), 04 (ex. 13), 05 (ex. 3, 5, 6). `10` — 01 (L40 ex. 8أ), 02 (L40 ex. 9, 8ب, 10), 03 (L29 ex. 7, 8), 04 (L40 ex. 13 ; L29 ex. 2, 9), 05 (L40 ex. 10, 8د). `11` — 01 (L42 ex. 3), 02 (L42 ex. 4, 5, 6), 03 (L42 ex. 2 ; L48 pb 2), 05 (L57 ex. 8 ; L42 ex. 7, 3 ; L40 ex. 16). `12` — 01 (L31 ex. 7), 02 (L31 ex. 6أ, 8 ; L40 ex. 12ب), 03 (L31 ex. 3, 4, 10ب), 04 (L31 ex. 7 ; L40 ex. 12ب), 05 (L31 ex. 6أ, 10أ, 7 ; L40 ex. 12أ).
- **Épreuve officielle du guide** : `11/04-defi` — `manuel {code 502603, pages 189-194, items T3 sit. 1 أ / ب}` (les trois frères : 8/21 puis 1000 m²). `content:qa` accepte le code ; la couverture `content:audit` ne le mesure pas encore (manifeste hors périmètre).
- Quand la leçon 40 / 48 sort de l'intervalle de pages du chapitre, `pages` est omis (sinon `content:qa` avertit) et les items disent « L40 ex. N ».

## Étiquettes : ids proposés (aucun inventé)

Les options concernées sont **muettes** dans le contenu ; à ouvrir au registre par le pilote si l'auditeur confirme le seuil.

1. `math.frac.rapport-denominateur-mal-choisi` — « تأخذ مقامًا غير العدد الذي طُلبت المقارنة به : في «أ بالنسبة إلى ب» المقام هو ب، لا الكلّ دائمًا ». Muette dans ≥ 5 questions de `08` (quiz Q7, 02-Q7, Q8, 04-Q9, 05-Q7).
2. `math.frac.complement-lu-a-l-envers` — « الجزء الناقص الأكبر يعطي الكسر الأصغر، لا الأكبر ». `10` : 02-Q5, 04-Q9, quiz Q7 (3 questions).
3. `math.frac.numerateur-compare-a-l-entier` — « تقارن البسط وحده بالعدد الصحيح : 16/5 < 4 لأنّ 4 = 20/5 ». `10` : 02-Q7 et le piège du cours (sous le seuil de 3 questions, mais c'est un piège de cours nommé).
4. `math.mes.unites-capacite-non-converties` — « تقارن لترات بدكل دون تحويل : 6 دكل = 60 ل ». `08` 03-Q8 (40/6), `09` 04-Q8 (75/40).
5. (07, 02-Q3) retirées : `critere-divisibilite-mal-choisi` sur 27, 81, 18 était inexacte ; l'erreur réelle (lire « ÷ 3 » en omettant « mais pas ÷ 9 ») n'a pas d'id et n'est pas récurrente.

## Contrôles

`content:check` ✓ (121 matières) · `content:qa -- --subject math-6eme` : **0 erreur** sur mes chapitres (les avertissements restants appartiennent à `14`, `16`, `18`) · `content:figures:check` ✓ · `content:tranche … --fresh --strict-longest` : **0/81** clés strictement les plus longues, « patron de notion » 0 en recul · `prettier --check` ✓ sur mes fichiers (les JSON d'origine n'étaient pas formatés : leur diff est plus grand que le contenu) · rendu `renderLesson` / `renderSummary` des six cours : aucun `**`, `:::`, `$$` ni `_` italique ouvert (deux gras coupés par un saut de ligne dans `08` et `10` corrigés). Toutes les valeurs numériques nouvelles recalculées à part (`fractions.Fraction`). Chiffres latins, virgule décimale, U+00A0 dans les nombres ≥ 5 chiffres.

## Doutes pour l'auditeur

- **PGCD (09)** : la fiche exclut le « PGCD formalisé » (§3.2) mais garde « le plus grand diviseur commun cherché parmi les diviseurs ». Cours et `04-defi` Q2 l'emploient sans algorithme : conservés, à trancher.
- **Paires proches (tranche, Jaccard ≥ 0,45)** : 07 uniquement (02-Q6 ↔ 04-Q2 ↔ 05-Q5 « plus grand / plus petit chiffre » ; quiz Q3 ↔ 01-Q6 ; restes en quiz/02/04) et 10 (01-Q8 ↔ 02-Q7). Ce sont des savoir-faire parallèles à données différentes, voulus ; les deux premiers existaient avant le lot.
- **Figures** : 11 figures neuves en question (carré en 8 triangles, demi-droites en quarts à 3/4 et 7/4, rectangle en 9 parts inégales, diagramme des familles, bande de 12 parts, grille 6 × 6, deux bandes 3 → 6, grille 4 × 4 bordée, bandes 5/6 et 5/7, bande bicolore, grille de 100) + 1 en cours (`10`, zoom 8 → 9 en tiers). Vérifiées par capture ; la lettre arabe « أ » des deux demi-droites n'a pas de glyphe dans le navigateur de la machine (rendu minuscule) — à regarder avec une police arabe.
- **Variantes non déclarées** : 11 (02-Q9 peintre 1/2 + 1/3 + 1/4 ; 04-Q7 réservoir 3/5 → 11/15), 12 (04-Q8 bibliothèque 440 livres sous lecture 3/10 de L31 ex. 12).
- **Notation du manuel RTL** : toutes les opérations reprises (L42 ex. 3, 5, L57) sont écrites LTR, avec le sens vérifié (résultats positifs).
- **Clé** : sur les 81 questions neuves ou modifiées, positions a 10 · b 15 · c 27 · d 29 (compensation volontaire d'un existant très chargé en a/b ; chaque chapitre entier reste entre 6 et 15 par lettre).
