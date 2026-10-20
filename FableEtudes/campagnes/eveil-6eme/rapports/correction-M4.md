# Correction du lot M4 (éveil 6ᵉ) — chapitres 07, 11, 08

Source : `audits/audit-M4.md` + décisions du pilote. Aucun défaut refusé ; aucune décision « à l'humain » renvoyée.

## Défauts appliqués

### 07/06 (9 → 6 q)
- q3, q7, q9 supprimées (doublon patron, fuites vers q5/q6 et q8). q5 : étiquette retirée de l'option c (deux erreurs, muette). q6 : renvoi « (الجدول نفسه) » retiré. q4 : option a (dessin fautif) retirée, ids renommés a-c, clé a.

### 07/07 (12 → 7 q)
- q1, q2, q3, q5, q10 supprimées. q9 : option a retirée (ids renommés, clé a) et explication adaptée. Reste ≥ 5 : la mission est gardée.

### 07/08 (11 → 10 q)
- CRITIQUE : SVG 2019 (q4, q11) remplacé à l'identique du correctif (montagne sur l'axe à droite, cascade en bas à droite) ; q4 clé d (الشلّال), explication de l'auditeur (ne nomme plus forêt/campement). Rendu Chromium 360 px RTL vérifié ; rotation refaite (nord à gauche : sud à droite, ouest en bas : sud-ouest = bas droite = cascade).
- q10 supprimée. q1 : énoncé du sujet rétabli (sans « السند نفسه »). q7 : option c retirée (ids renommés, clé b).

### 07/09 (12 → 11 q)
- CRITIQUE : SVG 2010 remplacé (flèche أ→ب verticale, forêt→départ verticale). q5 : options a-d et explication de l'auditeur, clé b. q9 : énoncé sans renvoi, options et explication, clé a (ancienne b). Rotation refaite : 1 = ش ق, 2 = ش, 3 = ج غ, 4 = ج ; rendu vérifié.
- q8 supprimée (doublon `07/03-revision#6`). q2 : renvoi retiré. q4 : explication « في صباح بارد كثير الضباب… ». (Le `prompt` de q4 ne contenait pas « في يوم بارد » : la correction porte sur l'explication.)

### 11 (m037 coupée, renumérotation)
- m037 (`06-exams-2008-2018…`) : fichier supprimé. Missions suivantes renumérotées : `06-exams-2012-2016-depot-metallique-…` (displayOrder 6), `07-exams-2009-2018-electrolyse-…` (7), `08-devoir-circuit-en-panne-…` (8). Seuls ces fichiers/displayOrder changent (décision du pilote, écart assumé à la règle 3).
- 11/06 (ex-07, 8 → 5 q) : q1, q2, q6 supprimées ; q5 : note de remplacement déplacée de l'énoncé vers l'explication ; q7 : option d remplacée (cuivre/ graphite, muette) et explication adaptée (sa phrase sur le bois ne tenait plus) ; q8 : option b remplacée par la version à deux erreurs (muette), explication « محلول السكّر العازل ». Option d de q7 allongée (« الموصولان بالمولّد ») pour que la clé ne soit plus strictement la plus longue (0/81 à la tranche). Légendes manuel (محلال، مصعد، مهبط) des figures q5/q6 non ajoutées : voir « adapté ».
- 11/07 (ex-08, 7 → 5 q) : q4, q7 supprimées ; q2 options c et d remplacées, étiquetées `eveil.elec.gaz-electrolyse-inverses` (id du registre).
- 11/08 (ex-09 devoir, 8 → 6 q) : q1, q3 supprimées ; CRITIQUE q2 : clous tous de 110 (six substitutions, identique au correctif, rendu vérifié) ; q5 : explication de l'auditeur.

### 08 (m041 coupée)
- Fichier `06-exams-2010-2018-chute-poids-et-masse.json` supprimé ; ligne « Sujets officiels… » retirée de `08-poids/chapter.json`.

### gisement.json
- m037 et m041 : `statut: "ecartee"`, sans champ `fichier`, raison ajoutée à la note (« coupée à l'audit M4 : trop mince après retrait des redites (E-1) » / « …redemande le patron mis à niveau (E-1) »). Les trois missions du 11 suivantes : `fichier` et `nn` (6, 7, 8) mis à jour.

## Adapté / non appliqué
- Légendes manuel q5/q6 (mineur de 11/07) : q6 supprimée ; sur q5 (circuit au montage inversé) étiqueter مصعد/مهبط par la connexion réelle livrerait la réponse (ملعقة = مصعد), donc non ajoutées. Sans effet sur la clé (l'auditeur le dit).
- Mineurs « accepté » de l'auditeur (07/08 explications à repère complet, 11/09 q8 prémisse) : inchangés, comme il le demande.

## Ids d'étiquettes proposés (registre non touché)
- `eveil.aim.nord-lu-en-haut-de-la-page` (07/08 q1, q2, q5, q6, q8, q11 ; 07/09 q1, q2, q7) ; `eveil.aim.est-ouest-inverses` (07/09 q5, q9 ; inexistant au registre, à créer) ; `eveil.aim.distance-ou-ecran-renforce` (07/07 q6, écran épais) ; `eveil.aim.un-seul-pole` (07/07 q4, q11) ; `eveil.aim.support-magnetique-ignore` (07/09 q11) ; `eveil.elec.electrode-pole-confondus` (11/06 q4) ; `eveil.elec.lampe-accusee-a-tort` (11/08 q6-q8).

## Gates (depuis eng-deliver)
- `content:check` ✓ (121 sujets) · `content:qa` ✓ · `content:figures:check` ✓ · `programme:check` ✓ (26 warnings préexistants, hors lot).
- `content:tranche … --fresh --strict-longest --strict-lessons` ✓ : clé la plus longue 0/81 ; positions a 29 / b 25 / c 20 / d 25 % ; patron 0 en recul. 7 paires proches, non bloquantes, toutes des parallèles voulus (même figure ou même méthode de rotation) : 07/08 #1↔#5 (0,74 : l'énoncé 2026 de l'auditeur rétabli reprend la citation du sujet, questions sur deux flèches différentes), #3↔#8, #4↔#10, #7↔#8 ; 07/09 #1↔#2, #2↔#7 ; 11/07 #1↔#2.
- `content:gisement:controle -- --sources …/eveil-scientifique-6eme …/11-…/08-devoir-circuit-en-panne-et-electroaimants.json` ✓ : 0 plage ≥ 8 mots, 0 plage ≥ 6, 0 exercice source à ≥ 2 données communes.
- Prettier `--write` puis `--check` ✓ sur tous les fichiers touchés.

## Bilan : 84 → 50 questions (07 : 34 en 4 missions ; 11 : 16 en 3 missions ; 08 : plus de mission d'examen).
