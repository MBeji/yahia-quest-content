# Rapport M1 — maths 6ᵉ, missions du gisement des chapitres 06, 07, 13 (étude 36)

Auteur : lot M1 (9 missions, 64 questions). Carte : `assign-M1.md`. Consigne : `prompt-auteur-missions.md`. Aucun fichier hors des missions et des `sources[]` des trois `chapter.json`. Pas de git.

## Fichiers (tous sous `content/math-6eme/`)

| fichier | mission | étage | q. | problème repris |
| --- | --- | --- | ---: | --- |
| `06-multiples-communs/exercices/06-exam-2023-p1-multiples-et-recettes.json` | m001 | d3 boss 120/30 | 6 | concours 2023, problème 1 |
| `06-multiples-communs/exercices/07-exam-2020-p2-jouets-restes-egaux.json` | m002 | d3 boss | 8 | concours 2020, problème 2 |
| `06-multiples-communs/exercices/08-exam-2018-p1-costumes-restes-et-benefice.json` | m003 | d3 boss | 8 | concours 2018, problème 1 |
| `06-multiples-communs/exercices/09-devoir-multiples-communs-intervalle.json` | m004 | d3 boss | 8 | devoir, salle blanche (carte seule) |
| `07-criteres-divisibilite/exercices/06-devoir-chiffres-manquants-plusieurs-criteres.json` | m005 | d2 practice 75/15 | 6 | devoir, salle blanche |
| `13-multiplication-fraction-entier/exercices/06-exam-2025-p1-bouquets-trois-clients.json` | m006 | d3 boss | 8 | concours 2025, problème 1 |
| `13-multiplication-fraction-entier/exercices/07-exam-2016-p1-cadeau-fraction-et-remise.json` | m007 | d3 boss | 7 | concours 2016, problème 1 |
| `13-multiplication-fraction-entier/exercices/08-exam-2015-p1-robe-deux-options.json` | m008 | d3 boss | 6 | concours 2015, problème 1 |
| `13-multiplication-fraction-entier/exercices/09-exam-2009-p1-chauffe-eau-installation-economie.json` | m009 | d3 boss | 7 | concours 2009, problème 1 |

`displayOrder` = numéro de fichier (6 à 9) ; les `NN` ont été revérifiés avant écriture (le plus grand existant était `05-entrainement` dans les trois dossiers). Dans chaque fichier, les questions sont triées par difficulté croissante (d2 puis d3), l'ordre du sujet étant conservé à difficulté égale : une question d'étape peut donc venir avant la question officielle qui la précède dans le sujet.

`chapter.json` : `sources[]` complété (ligne « Sujets officiels du concours d'entrée… » au 06 et au 13 ; ligne « Calibré sur des devoirs publics… » au 06 et au 07). Le 07 a été touché en dernier, sur l'état courant du fichier (aucune autre ligne modifiée).

## Données officielles reprises et recalculées (script, deux chemins)

Toutes les valeurs ont été recalculées par script, y compris celles que le sujet donne à prouver : 2023 (119, 2023 seul multiple de 119 dans ]2005 ; 2035[, écart 1500 / 100 billets = 15 d) ; 2020 (2/5 ↔ 1920, 4800, 2880, 4807, N = 9618, troisième genre 1938) ; 2018 (N = 605, coût 49 280 d, tissu 20 204,8 d) ; 2025 (total 216, client 2 = 72, couleurs 24/36/48, fleur blanche 2 d) ; 2016 (27,200 ; 13,600 ; 68 d ; payé 57,800 ; remise 10,200 ; taux 15 %) ; 2015 (46 ; 115 ; 161 ; 138,125 ; écart 22,875) ; 2009 (1560 ; 1800 ; 37,120 ; 32 %). Tous les distracteurs ont été vérifiés faux ; ceux qui portent une étiquette exécutent bien l'erreur du libellé. Les décimaux à trois chiffres sont gardés tels qu'imprimés (18,600 ; 162,500 ; 78,880 …).

## Ce qui a été donné dans l'énoncé (technique ou donnée non enseignée par le cours du chapitre)

- **Pourcentage** : le pourcentage n'est enseigné qu'au `14` (et au `26`), après les missions des `06` et `13`. Chaque question qui calcule un pourcentage rappelle « 41 % (15 %) d'un nombre = 41/100 (15/100) de ce nombre » ; les deux questions « quel taux » (2016, 2009) rappellent « un pourcentage est une fraction de dénominateur 100, par exemple 1/4 = 25/100 = 25 % » (exemple choisi pour ne pas livrer la clé 15 ni 32).
- **Produit de nombres sans diviseur commun** : « 11, 19, 23 n'ont, deux à deux, aucun diviseur commun autre que 1, donc leur plus petit multiple commun est leur produit » (m002 Q3, Q8), idem pour 13 et 23 (m003), 8 et 9 (devoir). Le calcul du produit reste à faire par l'élève.
- **Clés d'étapes intermédiaires redonnées** (inévitable quand une étape dépend d'une autre) : m006 Q4 à Q7 donnent les trois sommes 60, 72, 84 (le 72 est la clé de Q3) ; m007 Q6 et Q7 donnent le prix 68 d (clé de Q5) et Q7 le payé 57,800 (clé de Q3) ; m008 Q3 donne le tissu 46 d (clé de Q2) et Q6 la clé 161 d de Q4. Partout ailleurs j'ai repris la donnée brute du sujet (m002 Q4/Q5/Q8, m003 Q6/Q7/Q8, m006 Q3/Q8, m007 Q5, m008 Q4, m009 Q3/Q5), de sorte que le tirage au hasard du donjon ne livre pas la clé d'une autre question.
- Aucune lettre, aucune algèbre littérale : les inconnues sont dites en mots.

## Adaptations de forme

- « أثبتُ أنّ … » devenu « quelle valeur » ou « quelle justification » (2023 q1 et q2, 2025 q1, 2018 q1) ; la clé n'est ni dans le titre ni dans l'énoncé (titres : notions, jamais un résultat).
- Tableaux de 2023 et de 2025 refaits en tableaux Markdown lisibles ; pas de figure SVG (aucune figure dans ces problèmes).
- Question « unicité » de 2023 : formulée sans livrer 2023 ; la question officielle (« ما هو العدد الجملي للكراسي ») reste numérique.
- Aucun `short_answer` (pas d'`acceptedAnswers` à porter) ; `ordering` dans m002, m004, m005, m006, m009 (sans nombre-clé dans les marches), `multi` dans m005.

## Étiquettes employées (registre `math.*`, aucune sur multi/ordering/matching, options à deux erreurs laissées muettes)

`math.num.ppmc-par-addition` (24 ; 2023), `math.num.divisibilite-un-seul-critere` (17 ; mult. de 23 seul ; 0 dans 8▢5), `math.num.extremum-demande-ignore` (238 ; 240 et 360 ; 5 ; 840), `math.num.multiple-et-diviseur-confondus` (2020), `math.num.multiple-precedent-au-lieu-du-suivant` (600, devoir), `math.num.operation-inverse-appliquee` (somme/différence, 4/3, 8/5, 3/7, 480, 64 400, 33 800, 186 875, 9610, « multiplier au lieu de diviser »), `math.alg.reponse-a-l-autre-inconnue` (résultats intermédiaires : 216, 27 200, 115, 1560, 24,375), `math.prop.pourcentage-base-erronee` (fraction ou % pris sur le prix de vente ; remise rapportée au prix payé ; économie rapportée à la nouvelle facture), `math.prop.pourcentage-recopie-comme-resultat` (162,5 − 15), `math.frac.numerateur-denominateur-inverses` (100/41 ; 2/5 pour 5/2 ; « Prix ÷ remise »), `math.frac.comparaison-a-l-unite-inversee` et `math.frac.fraction-d-un-nombre-etape-oubliee` (5/2 lu comme < 1, ou comme « ×5 » seul), `math.num.critere-divisibilite-mal-choisi` (critère de 3 pris pour 9 : chiffres 0 et 6 dans 2▢4).

**Manques** (aucun id inventé) : « oublier la contrainte d'intervalle » (2023 q1 — 119 au lieu de 2023 ; 2020 — 9614 ; devoir D02) ; « diviser la recette par le nombre total de billets » (2023) ; « appliquer la fraction du client aux seules autres parts » (2025, la valeur 48) ; « calculer la fraction du coût au lieu de retrouver le tout » (2009, 2016, par `operation-inverse-appliquee` seulement quand le libellé colle) ; « ne pas vérifier l'unicité » (devoir D02/D03). Ces erreurs reviennent dans plusieurs questions de la campagne et n'ont pas d'entrée au registre : à envisager pour la suite.

## Contrôles

- `content:check` : verte (121 matières). `content:qa -- --subject math-6eme` : 0 erreur ; aucun avertissement sur mes fichiers (les 3 restants sont au `14`).
- `content:figures:check` : verte. `prettier --check` : verte (fichiers de mission et `chapter.json`).
- `content:tranche -- --subject math-6eme --chapters 06,07,13 --fresh --strict-longest` : clé strictement la plus longue 0 sur 104 ; positions de clé a 23 · b 28 · c 27 · d 26 ; **aucune paire proche (≥ 0,45) ne nomme mes fichiers** ; aucun candidat gabarit ; 0 cours en recul.
- `lot-lint.mjs` sur les 9 fichiers : rien à signaler.
- Devoirs (`content:gisement:controle`, m004 et m005) : **0 plage de 8 mots**, 0 exercice source dont on reprenne 3 données ; m004 Q2 et Q8 portent « 2 données communes » avec un exercice source (« à regarder » du contrôle) — ce sont des entiers de petite taille que j'ai inventés (j'ai déjà changé les nombres de ces deux questions sans jamais ouvrir le devoir) ; à juger par l'orchestrateur.

## Doutes à signaler

1. **Placement au `13` de missions qui font du pourcentage** (2016, 2015, 2009) : exception E-3 acceptée par le pilote ; la règle du pourcentage est donnée dans l'énoncé, mais le pourcentage reste « plus avancé » que le cours du `13`. Même remarque pour le 41 % de 2018 au `06`.
2. **m002 Q7 vs Q8 et m003 Q3 vs Q6** : même structure « restes égaux » dans deux missions du `06` (2020 et 2018) ; angles différents (2020 : trois diviseurs, intervalle de 100 ; 2018 : deux diviseurs, intervalle de 6, multiple juste sous l'intervalle). Les « ne pas redemander » du `06` (`05#5`, `04#2`, `04#6`…) ne sont reprises ni en nombres ni en cadre ; le devoir reprend « ppcm de trois nombres » avec d'autres nombres que `04-defi#2`.
3. **m004 Q1** : après avoir vu que `04-defi#2` (ppcm de 4, 6, 10) et `01-pratique#6` (ppcm de 5 et 6) sont à ne pas redemander, la première question demande le plus petit multiple commun de 5, 8, 6 **supérieur à 700** (multiple suivant, étiquette `multiple-precedent-au-lieu-du-suivant` sur 600) plutôt que le ppcm seul.
4. **m008 Q6** : les options décrivent les choix (« شراء القماش وخياطته / شراء الفستان الجاهز ») et non « الخيار الأوّل / الثاني », car le contrôle de QA refuse qu'une explication désigne une option par son rang ; l'énoncé garde l'appellation officielle.
5. **m005** : toutes les questions sont d2 (en-tête practice 75/15) ; l'ordering ne porte ni valeur ni chiffre.
6. Les trois warnings restants de `content:qa` (« valeur canonique non répétée », au `14`) ne sont pas à moi.

## Corrections après audit (audit-M1-M2.md, décisions E-11 et E-12)

- **E-11 (M-1)** : `07-exam-2020-p2-…` et `08-exam-2018-p1-…` quittent le 06 (copie puis suppression) : `13-multiplication-fraction-entier/exercices/10-exam-2020-p2-jouets-restes-egaux.json` (displayOrder 10) et `11-exam-2018-p1-costumes-restes-et-benefice.json` (displayOrder 11) ; le plus grand NN du 13 était 09. Le devoir du 06 est renuméroté `09-devoir-…` → `07-devoir-multiples-communs-intervalle.json` (displayOrder 7). Registre `gisement.json` : `C07#2a` et `C09#1a` passent au chapitre 13 (`fichier`, `nn` 10 et 11), `D02#1` à `07-devoir-…` (`nn` 7). `sources[]` du 06 (2023 + devoir) et du 13 (examen) restent cohérentes. Je n'avais posé aucun rappel de fraction ; le rappel de pourcentage est gardé.
- **E-12 (C-1)** : aucune réécriture en toutes lettres (correctif moteur). **M-3** appliqué : devoir du 07, Q3 devient `4▢1` (441), options 1 (critère mal choisi), 4 (clé), 7 (critère mal choisi), 9 muette.
- **M-2** : 2023 Q4 option « aucun multiple » → « deux multiples au moins, car 30 > 17 et 7 » ; 2020 Q7 « 4811 » → « 9626 » (reste ajouté une fois par diviseur) ; devoir 06 Q7 « 98 » → « 112 » (reste 4 au lieu de 2) ; 2025 Q5 option « aucune erreur » → « sa division est juste mais 30 d est le prix du bouquet rouge » ; 2009 Q6 option « aucune erreur » → « diviser seulement par 100 » (muette, l'étiquette `pourcentage-base-erronee` disparaît avec l'option). Explications complétées comme proposé.
- **M-5** : devoir 06 Q6 (comptage de multiples communs, doublon de `06/04-defi#3`) remplacé par « combien de multiples de 12 entre 700 et 1000 qui ne sont pas multiples de 20 » (clé 20, recalculée : 25 − 5).
- **Mineurs** : session ajoutée en tête des deux `ordering` sans session (2020, 2009) ; 2018 Q3 option 7/11 étiquetée `numerateur-denominateur-inverses` ; 2015 Q4 distracteur faible « 48,5 » remplacé par « 69 » (÷2 sans ×5, étiquette `fraction-d-un-nombre-etape-oubliee`) ; étiquette `reponse-a-l-autre-inconnue` posée sur 9614 (2020 Q7) et 108 (devoir 06 Q7). L'id neuf `contrainte-d-intervalle-ignoree` du vocabulaire visait précisément « 4811 » et « 98 », options que l'audit fait retirer : il n'est donc pas posé dans mes fichiers.
- Contrôles refaits : `content:check`, `content:qa` (0 erreur sur mes fichiers ; l'erreur restante est au 21), `prettier --check`, `lot-lint` (rien), `content:tranche` (clé la plus longue 0, positions a 23 · b 29 · c 28 · d 24, aucune paire proche sur mes fichiers), `content:gisement:controle` sur le devoir du 06 et celui du 07 (0 plage de 8 mots, 0 source à 3 données ; « 2 données communes » toujours sur Q2 et Q8 du devoir 06, petits entiers). `content:gisement:lignes` demande un fichier de lignes : non applicable ici.
