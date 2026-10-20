# Rapport auteur M1 — chapitres 09, 12, 01 (missions du gisement)

Sources : transcriptions `examens-nationaux/6eme-base/eveil/` (arrivées en cours de travail ; phrases officielles vérifiées contre elles, PDF pour les figures), cartes de la carte `assign-M1.md`. Gates : `content:check`, `content:qa` (0 erreur), `content:figures:check`, `content:tranche --strict-longest --strict-lessons` (0/124 clé la plus longue), prettier, `gisement:controle` (0 plage de 8 mots) : verts.

## Fichiers (12 missions, 112 questions)
- 09 : `06-exams-2008-2013-schemas-de-loeil-defaut-lentille-legendes` (d3, 9 q) ; `07-exams-2015-2018-hypermetropie-lentille-pupille` (d3, 10 q)
- 12 : `06-exams-2016-2017-refraction-definition-et-rayons` (d3, 9 q) ; `07-exams-2008-2012-reflexion-miroir-rayons-et-definitions` (d3, 9 q)
- 01 : `06-exam-2025-…` (8 q), `07-exams-2019-2021-…` (9), `08-exams-2020-2024-…` (10), `09-exams-2019-2026-…` (9), `10-exams-2008-2024-…` (12), `11-exams-2013-2023-…` (10), `12-devoir-un-feu-…` (9), `13-devoir-experiences-sur-lair` (10)
- `chapter.json` (sources) des trois chapitres.

## Écarts à la carte (à connaître)
- m007 : 10 q au lieu de 11 (la « conclusion 2023 » aurait doublé la correction « 80 % » de 2020 ; remplacée par une question de protocole).
- Matching impossibles (non bijectifs) transformés en `multi` : m008 (2022 type de combustion), m009 (2010 intervenants).
- **12-dhaw : le cours n'enseigne pas « le rayon se rapproche / s'écarte de la normale »** (ni la fiche n'en fait un acquis du cours). m003 et m004 (tracés de réfraction) donnent la règle DANS l'énoncé de chaque question (technique non enseignée) ; ces questions sont donc des lectures de figure. Recommandation : ajouter une phrase au cours du ch.12 (propriété de l'étage « انكسار »), puis relever éventuellement ces questions.
- Défauts d'énoncé corrigés et dits dans l'explication : 2018 lentille de l'hypermétropie (convergente), 2015 verres concaves (on demande le défaut, sans « lire »), 2016 sens eau→air, 2017 mot « الكتلة » → الشفّافيّة, 2026 suie en flamme bleue (énoncés refaits ; les images 1/2 sont, dans le sujet, bleue/jaune — respecté), 2010 chaleur (« مصدر الحرارة » / « حرارة »), 2023 « quart de l'azote » (→ quart de l'air), 2022 azote en multiples (→ cinquième), E-4 (« environ », jamais « toute l'oxygène consommé »).
- 2024 : les graduations (fixées par l'auteur : cinquièmes de l'air enfermé) ne sont pas celles du sujet (niveau initial à la graduation 1 dans le sujet).
- 2021 (pesée) : protocole refait selon la transcription (ballon pesé avant/après transfert de 2 L d'air dans la bouteille).
- Recouvrements assumés avec des questions publiées (le sujet les impose) : m010 (2013 sèche-cheveux, glace) et m006 (2019, 2021) ; m010#1–2 (buée) avec 01/01-pratique#4 et l'exemple du cours ; m009 intrus 2019 (deux questions parallèles). Paires proches signalées par la tranche (5, parallèles voulues : pesée 2,6/1,3 ; deux intrus ; grille lentille/justification 2013 ; reformulations 2025).
- Questions d'examen redonnant un contexte du cours : buée de la vitre, mission m010.

## Étiquettes
Utilisées : `eveil.vision.{myopie-et-hypermetropie-inversees, lentilles-inversees, cristallin-et-vitre-confondus}`, `eveil.lum.{oeil-emet-la-lumiere, phenomenes-lumineux-confondus}`, `eveil.air.{dilatation-contraction-inversees, azote-entretient-combustion, air-confondu-avec-oxygene, reactifs-et-produits-inverses, co-et-co2-confondus}`, `eveil.gaz.test-mal-associe` (jamais sur multi/ordering/matching ; options à deux erreurs muettes).
**Ids proposés (absents du registre, non posés)** :
- `eveil.vision.role-cornee-et-retine-confondus` (m001, fonction de la rétine)
- `eveil.vision.pupille-liee-a-la-distance` (m002, taille de la pupille et distance)
- `eveil.vision.image-sur-la-retine-pour-l-hypermetrope` (m002, C09#6/#7)
- `eveil.lum.rayon-refracte-non-devie` et `eveil.lum.rayon-du-mauvais-cote-de-la-normale` (m003/m004)
- `eveil.lum.rayon-perpendiculaire-mal-trace` (m004, retour sur lui-même)
- `eveil.air.aspiration-au-lieu-de-contraction` (m006, « le gaz froid mange l'eau »)
- `eveil.air.dilatation-confondue-avec-consommation-oxygene` (m006/m010/m012)
- `eveil.air.suie-attribuee-a-la-combustion-complete` (m008)
- `eveil.air.air-comprime-disparait` (m012)

## Doubles résolutions
Chaque question résolue deux fois (données de la transcription, puis re-lecture de la figure) ; figures tracées par calcul (rayons de l'œil, réfraction avec normale, miroir) et rendues en PNG pour contrôle visuel ; légendes en arabe simples, hors trait.

## Doutes
Rendu bidi des chiffres isolés dans les libellés (« الصورة 1 ») à confirmer au rendu réel du moteur ; clés V1 respectées (seules les quatre valeurs permises : 1/5, 1,3 g, eau 2/3 non utilisée, 120 j non utilisé).
