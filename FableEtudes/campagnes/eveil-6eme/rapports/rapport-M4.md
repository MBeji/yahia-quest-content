# Rapport M4 — missions du gisement, chapitres 07 · 11 · 08 (éveil 6ᵉ)

Auteur : agent M4. Transcriptions lues d'abord sur la branche `wip/eveil-6eme-lot-a` (absentes de l'arbre au départ), PDF vus pour 2019 (aiguilles) et 2021 (quatre aimants). Abréviations des directions : celles du cours 07 (ش ج ق غ ; ش ق ش غ ج ق ج غ). Boussoles dont le nord n'est pas en haut : nord marqué ش.

## Fichiers (tous `practice`/`boss` selon la carte ; `displayOrder` 6 à la suite)

| fichier | étage | q. | lignes reprises |
| --- | --- | ---: | --- |
| `07/exercices/06-exams-2017-2026-poles-force-attraction-et-repulsion.json` | d2 75/15 | 9 | C01#3 C01#4 C03#5 C03#6 C08#5 C08#6 C10#4b |
| `07/…/07-exams-2009-2025-types-de-poles-aiguille-formes-et-matieres.json` | d3 120/30 | 12 | C06#14 C18#3b C04#10 C04#11 C02#13 C05#6 C05#7 C02#14 |
| `07/…/08-exams-2019-2026-directions-le-nord-nest-pas-en-haut.json` | d3 | 11 | C01#13 C01#14 C03#10 C03#11 C05#10 C08#4 |
| `07/…/09-exams-2010-2026-boussole-en-voiture-et-boussole-artisanale.json` | d3 | 12 | C06#4 C06#5 C06#6 C17#1a C05#11 C01#15 C02#15 |
| `11/…/06-exams-2008-2018-quel-effet-du-courant.json` | d2 | 7 | C10#4a C19#5a C09#9 C14#4a C15#4b |
| `11/…/07-exams-2012-2016-depot-metallique-la-cuillere-et-la-plaque.json` | d3 | 8 | C11#5a-c C15#4a C12#3b |
| `11/…/08-exams-2009-2018-electrolyse-de-leau-gaz-et-electrodes.json` | d3 | 7 | C14#5a C18#3a C09#10 |
| `11/…/09-devoir-circuit-en-panne-et-electroaimants.json` (devoir, salle blanche) | d3 | 8 | D07#6 D07#8 D07#10 D08#5 (carte seule) |
| `08/…/06-exams-2010-2018-chute-poids-et-masse.json` | d2 | 10 | C09#3 C17#3a-b C12#3a C11#6b |

Total 84 questions (carte : 86). Écarts : m037 7 au lieu de 8 (la 3ᵉ phrase de 2013 « l'effet thermique dépend du fil » n'est pas enseignée : remplacée par des énoncés du cours, hors reprise) ; m038 8 au lieu de 9 (les deux blancs 2012 « effet chimique » / « courant » fusionnés en une question). `chapter.json` : `sources[]` complétés (exam ×3 chapitres, devoir au 11).

## Croisement E-12
Les trois chapitres sont déjà mis à niveau (cours au patron, 5 fichiers de 7-9 q., sonnette E-7b au 11, huit directions V5 au 07, plaquettes sans objet ici). Croisement refait question par question : les gestes d'examen (corriger l'énoncé, justifier, lire une figure) sont neufs ; les faits partagés sont redemandés sous une autre forme. Recoupements assumés : m041 (08) reste proche du patron (E-1 conseille de la couper en premier) ; la question « boussole dans la voiture » (07/03-revision#6) est remplacée par un multi (« tout ce qui dévie l'aiguille ») ; l'ordering « utiliser une boussole » reformule la méthode du cours sans reprendre l'exemple du Hady.

## Défauts d'énoncé corrigés (et dits dans l'explication)
2016 nitrate d'argent → sulfate de cuivre ; 2015 solution de sucre → sel (schéma d'électrolyse corrigé) ; 2013 « eau de mer » → solution de sel ; 2013 énoncé 1 (tube ①) laissé JUSTE, énoncé 2 faux (anode au + ) ; 2025 aimant « en anneau » → aimant cylindrique ; 2022 « nord-est » traité comme FAUX (clé : nord-sud) ; 2018 « الكتلة » → الوزن ; 2016 : ni 1/6 ni satellite ; 2013 : rapport 2 : 1 jamais demandé (on compare seulement les volumes) ; boussoles des sujets 2026, 2024, 2022, 2021, 2019 refaites avec le nord marqué ش (jamais « haut = nord »). Figures exactes à 45° ; la figure 2019 vue au PDF (aiguille 2 fausse).

## Étiquettes
Employées (registre existant) : `eveil.aim.{attraction-forte-au-milieu, poles-identiques-s-attirent, attire-tous-les-metaux, attire-seulement-au-contact, juge-par-forme-couleur-legerete}`, `eveil.elec.{effets-du-courant-confondus, fermer-et-ouvrir-confondus, electroaimant-permanent, conducteurs-liquides-confondus, gaz-electrolyse-inverses}`, `eveil.gaz.test-mal-associe`, `eveil.poids.{chute-en-ligne-oblique, masse-et-poids-confondus, masse-change-avec-le-lieu, certains-objets-sans-poids}` ; jamais sur multi/ordering/matching ; options à deux erreurs muettes.

**Ids manquants à créer (laissés muets, rien d'inventé)** :
1. `eveil.aim.nord-lu-en-haut-de-la-page` (« tu lis le haut de la feuille comme le nord ») — distracteurs naïfs des m035/m036 (≥ 12 questions) ; le 07 propose déjà `eveil.aim.est-ouest-inverses` (B4).
2. `eveil.aim.un-seul-pole` (un morceau d'aimant / l'aiguille n'a qu'un pôle) — m033 Q4, m034 Q3/Q4/Q11.
3. `eveil.aim.support-magnetique-ignore` (aiguille sur support en fer) — m036 Q11.
4. `eveil.elec.electrode-pole-confondus` (électrode reliée au mauvais pôle) — m038 Q4/Q5/Q6.
5. `eveil.elec.lampe-accusee-a-tort` (incriminer un composant en bon état) — m040 (Q4-Q8).

## Doutes / à arbitrer
- Lettre de l'Est « ق » : celle du cours (V5 n'en fixe pas ; le guide p.176 imprime « شـ ») — à confirmer.
- 2021 (quatre aimants) : le ش inscrit sur le premier aimant est posé comme son pôle nord (énoncé de la reprise).
- m034 Q forme : l'élève relie 4 formes dont l'aiguille ; m036 « multi » remplace la question libre 2021 (3).
- Paires proches restantes (Jaccard ≥ 0,45, 6) : exercices parallèles voulus (mêmes figures, gestes différents).

## Gates (depuis `/home/user/eng-deliver`)
`content:check` ✓ · `content:qa -- --subject eveil-scientifique-6eme` ✓ « no suspicious answer keys » (0 avertissement) · `content:figures:check` ✓ · `content:tranche … --fresh --strict-longest --strict-lessons` ✓ (clé la plus longue 0/107 ; positions 27/27/19/26 % ; patron 0 en recul) · prettier write puis check ✓ · `content:gisement:controle` sur le devoir : 0 plage de 8 mots, 0 exercice source repris à 3 données. Rendu Chromium des figures (QCM visuels, boussoles, roses) relu à l'image ; légendes en `text-anchor="middle"`. Double résolution des clés faite à la main sur les figures (rotation du repère vérifiée pour chaque orientation du nord).
