# Notes auteur — lot B3 (13, 14, 15, 22, 24 + neuf 26)

## 13-multiplication-fraction-entier

### Table des écarts (avant)
- M1 : aucune section ni question « كسر × كسر » (cours, résumé, quiz, exercices).
- Le cours enseignait fraction d'une quantité, conversions d'unités, du jeu part→tout, mais les 5 exercices et le quiz n'exerçaient que « a/b × n » (≈ 100 % des questions) : notions de la leçon 47 (ex. 4 fraction × décimal, ex. 5 conversions, ex. 7-9 tout depuis une partie, ex. 2/3 fraction d'une quantité) non exercées.
- coursePitfalls : le `::: piege` « 0,75 سا = 75 د » (math.mes.duree-convertie-en-base-cent) n'était pas déclaré ni porté par un distracteur.
- Pas de donnée fautive (errata n° 34 = ch. 13/15 : « 1/5 » du lait — non repris) ; pas de ⛔ ; pas d'explication par la place d'une option.
- Ambiguïtés du manuel §6.4 non reprises : ex. 6 (7/5 largeur), ex. 11 (eau), ex. 13 (deux taux).

### Fait
- cours : titre élargi (slug inchangé), section « ضرب كسر في كسر » au patron (ancrage tablette 3/4 puis 2/3 ; figure 12 carreaux ; exemple ; piège « on garde le dénominateur » ; propriété avec cas limite entier = n/1 ; verifie ; retenir), placée après « كسر من كميّة ». Résumé : puce ajoutée.
- quiz 5 → 7 (fraction d'une quantité, fraction × fraction). Exercices +3/+4/+4/+4/+4 questions en fin de tri (diff ≥ max du fichier), dont 2 `numeric`, 1 `ordering`.
- Reprise manuel déclarée sur 03-revision : ex. 4 (2/3 × 3,45), ex. 5 ب (4/5 km), ex. 9 (5/3, +8 m).
- chapter.json : titre/description élargis, source fiche ajoutée, coursePitfalls + math.mes.duree-convertie-en-base-cent.

## 14-proportionnalite-pourcentage

### Table des écarts (avant)
- Échelle (leçon 14) : section au cours mais **aucune question** (quiz + 5 exercices) ; pourcentage à base inconnue (§3.2 ✅, leçon 37 ex. 5) : seulement une « حالة حدّيّة » dans la section hausse/remise, **jamais exercé** ; quatrième proportionnelle (مذكرة 32, terme officiel « الرّابع التّناسبي ») : terme absent, une seule méthode (retour à l'unité) ; fraction → % hors 15/20, 18/24 ; hausse/remise peu exercée.
- Pas de donnée fautive reprise (errata n° 47–50 concernent ex. 7/8/9 de la leçon 37 — non repris : ni la facture 145,800/184,680, ni le crédit) ; incohérences §6.4 (taxes 45 %, « الكلفة الجمليّة ») non reprises ; pas de produit en croix ni d'aire à l'échelle (⛔/◐) ; pas de 180°.
- coursePitfalls : pas de piège « base erronée » (math.prop.pourcentage-base-erronee) alors que la leçon 37 le travaille.
- 8 notions → le chapitre passe à **10 sections** : au-delà du seuil de ~8 notions de course-explanation R-13 (question de curriculum à signaler : scinder « السلّم » — déjà posée par la fiche §2 sexies, écart 11).

### Fait
- cours : + section « الرّابع التّناسبي — ثلاث طرق » (coefficient, facteur entre colonnes, colonne intermédiaire ; piège additif ; synthèse après les deux méthodes déjà possédées, R-7) ; + section « القيمة الأصليّة المجهولة » (passage à 1 %, jamais ÷ 1,08 ; piège base erronée ; cas > 100 % et nombre total inconnu). Résumé : 2 puces. Intro et 🏆 ajustés.
- quiz 5 → 7 (échelle, base inconnue). Exercices +3/+4/+4/+5/+4 (échelle ×5, base inconnue ×4, quatrième proportionnelle ×3, fraction → % ×3, hausse).
- Reprise déclarée : 04-defi ← guide 502603 T2 situation 2 (p.180, corrigé p.184–186) en 4 étapes `numeric` (largeur 22,5 m ; aire 843,75 m² ; prix 29 531,25 d ; coût 31 893,75 d), mêmes données (plan 2 erroné du guide non utilisé).
- chapter.json : description, source fiche, coursePitfalls + math.prop.pourcentage-base-erronee.

## 15-vitesse-distance-temps

### Table des écarts (avant)
- Cours complet (8 sections). Mais exercices : **uniquement** vitesse/distance/temps en heures entières ; non exercés : durée en minutes (1 question), comparer deux mouvements (1 question triviale), vitesse moyenne de plusieurs étapes (0), changement d'unité (0), horaires (0), vitesse comme coefficient d'un tableau (0).
- Piège « 20 د = 0,20 سا » (math.mes.duree-convertie-en-base-cent) présent au cours, non déclaré ni porté.
- Le cours ne dit pas comment obtenir l'heure d'arrivée (testée par les exercices du manuel 51-7, 53-4) : ajout d'une phrase au propriete de la dernière section (8 h 40…, 13 h 25 + 2 h 50 = 16 h 15).
- Erratum n° 60 (80 م/س → 80 كم/س) : pas repris ; n° 34/35 (1/5 de lait, ch. 13/15) : pas repris. 51-10 (« piéton 12 km/h ») non repris.
- Rendu : un `**…**` coupé sur deux lignes dans l'exemple de la dernière section (pré-existant) cassait le gras — recollé.

### Fait
- Quiz 5 → 7 ; exercices +3/+4/+4/+4/+4. Reprises déclarées (mêmes données) : 03-revision ex. 7 (51) cycliste المحمّديّة–زغوان ; 04-defi ex. 6 et ex. 9 (53) ; 05-entrainement ex. 5 (53).
- chapter.json : description, source, coursePitfalls + math.mes.duree-convertie-en-base-cent.

## 22-durees

### Table des écarts (avant)
- Cours complet (8 sections, tout §2 sexies de la fiche couvert : ×, 3 unités, cascade, fractions d'heure, 10,5 h, départ = arrivée − durée, jour suivant, notation س/دق/ث).
- Exercices/quiz : la **multiplication d'une durée** (indicateur officiel + titre de la leçon) n'était **jamais exercée** ; secondes (3 unités) jamais ; emprunt en cascade jamais ; départ = arrivée − durée jamais ; passage au jour suivant jamais ; durée en heures décimales (1,5 h) jamais ; lecture d'horloge avec minutes jamais (une seule horloge à l'heure juste).
- Pas de donnée fautive ; pas d'ambiguïté du manuel reprise (ex. 7 « durée de travail du chauffeur » écarté).

### Fait
- quiz 5 → 7 ; exercices +2/+3/+4/+4/+4 : × d'une durée (5), 3 unités (4), cascade (2), jour suivant, départ/arrivée (4), heures décimales (3), 2 questions avec **horloge SVG** (2 h 45 ; 8 h 20), reprises déclarées 04-defi ex. 5 (horloge qui retarde) et ex. 8 (laboureur 10 h 30 × 80 آر).
- Prompts reformulés en situations pour éviter les paires proches avec les « احسب : … » existants.

## 24-decomposition-fractions

### Table des écarts (avant)
- Chapitre déjà aligné sur la fiche (écrit depuis la lecture du 2026-09-23) : tafkīk, composition, terme manquant, entier à dénominateur, partie entière/fractionnaire, deux groupes (7/53 ≠ 4/28 + 3/25), budget.
- Lacunes d'exercices : écrire un entier avec le dénominateur d'une fraction (ex. 7, `3/5 + 8`) peu exercé ; non-unicité du partage (ex. 8 ب, ex. 5) seulement par QCM de dénombrement ; galette (ex. 8) jamais exercée ; fractions > 1 en composition de plusieurs termes.
- 05-entrainement Q3 : option « 5/5 ولكنّها لا تساوي 1 » = la même valeur que la clé « 1 » avec un bandeau faux → deux lectures défendables ; remplacée par « 5 » (muette). Les tags de pièges du cours restent portés ailleurs.

### Fait
- quiz 5 → 7 ; exercices +2/+3/+3/+3/+3, dont 2 `multi` (décompositions valides de 13/15 ; partages valides de 15 parts), 3 `numeric`. Cours/résumé inchangés (déjà au patron, fiche respectée : jamais « عدد مختلط », jamais « 1 ¾ »).

## 26-diagrammes-batons (chapitre neuf)

- `displayOrder` : **26**. Les ordres 1–24 sont contigus (le ch. 15 est 16, le ch. 16 est 17) : aucune valeur libre « juste après 15 » sans modifier un existant. Placé en **fin de sujet** ; 26 (et non 25) pour ne pas heurter le chapitre neuf `25-perimetre-figure-composee` du lot B5. Au pilote de renuméroter à l'intégration s'il veut le placer après le ch. 15.
- Source : fiche §3.2 (✅ critère مع 1 du T2), §4 (leçon sans chapitre), §1 bis T2 sit. 1 (p.179, 182–183), §2 quinquies/sexies/nonies (ص 53 ex. 9, ص 81 ex. 2, ص 102–103 leçon 34, ص 120 ex. 15). ص 10–13 (moyenne mensuelle) et la moyenne (◐, Q-4) **non reprises** ; aucune médiane/mode.
- Cours : 5 sections au patron (lire, fraction/% d'une barre, barre manquante, construire, deux séries), 5 figures SVG générées (barres à partir des valeurs, vraies par construction), pièges portés par `coursePitfalls`.
- Quiz 5 ; 5 exercices (d1, d3, d2, d4, d3) × 6 questions ; reprises déclarées : 01 ← ص 81 ex. 2 (pluies) ; 02 ← ص 53 ex. 9 (familles) ; 03 ← ص 120 ex. 15 (âges) ; 04 ← ص 102–103 pb 2 أ/ب (graduations parasites de l'erratum n° 44 non redessinées ; valeurs relues au R-7 : 900/750/600/500 et 650/500/450/300) ; 05 ← guide 502603 T2 sit. 1 (p.179, 183 : 35 % ↔ 21 mm, 40 % ↔ 24 mm, 25 % ↔ 15 mm). 1 QCM visuel (4 mini-diagrammes). Axe de la T2 « عدد التلاميذ » (incohérent avec des %) non repris : l'axe est en mm.
