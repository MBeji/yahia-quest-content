# Rapport B4 — anglais 6ᵉ, chapitre `07-around-the-world` (2026-10-18)

## Fichiers (tout sous `content/english-6eme/07-around-the-world/`)

- **Créés** : `exercices/06-exam-2025-reading-trip-to-tunisia.json` (m018, d2, 6 q.), `exercices/07-exams-2013-2025-greetings-articles-directions.json` (m019, d2, 5 q.), `exercices/08-devoir-a-postcard-from-my-town.json` (m021, d2, 6 q.), `exercices/09-lets-pronounce-plural-s-and-y.json` (D6, d1, 4 q.).
- **Modifiés** : `quiz.json`, `exercices/01…05` (étiquettes ; réécritures listées ci-dessous), `cours.md` (+ section `## 🔊 Let's pronounce — the s of the plural and the y at the end`, avant le mot final : le 07 passe à 9 sections), `resume.md` (+ une puce « Pronunciation »), `chapter.json` (2 lignes `sources[]` au texte exact + `coursePitfalls` des 7 ids de la carte ; pas de `coursePattern`, pas de `manuel`).
- `content/misconceptions.json` : non touché. Aucun id neuf posé. Pas de git.
- Rendu : vitest jetable (supprimé) sur `renderLesson(cours.md, en)` : 9 sections, section de prononciation rendue (2 tables, bloc `verifie` plié, aucun `:::` ni `| ---` résiduel) ; `renderSummary(resume.md, en)` : 9 cartes, dernière = « Pronunciation » avec ses `<strong>`.

## Taux d'étiquetage (distracteurs de `mcq`)

| | avant | après |
| --- | --- | --- |
| 07 existant (quiz + 5 exercices, 105 distracteurs) | 0 / 105 | **55 / 105 = 52 %** |
| m018 reading 2025 | — | 9 / 15 = 60 % |
| m019 examens 2013–2025 | — | 3 / 9 = 33 % (+ 3 `expectedMistakes` taguées sur la `short_answer`) |
| m021 devoir (carte postale) | — | 6 / 12 = 50 % |
| 09 prononciation | — | 12 / 12 = 100 % |
| **chapitre entier** | 0 % | **85 / 153 = 56 %** |

Sous les 60 % de la carte, volontairement (E7) : je n'ai posé `mot-voisin-du-meme-champ` que sur `young` (opposé de new, indice dans l'énoncé) et sur bow / touch / kiss (« to say hello when you meet »). Muets assumés : salutations par pays (quiz#2, 01#4, 05#2), pays-et-monuments (02#2, 03#2, 03#3), lectures de chiffres ou de textes (02#3 b-c, 04#4, 05#4, 05#6), « Let's to travel / Let's travelling / prefer travel / prefer to travelling » (aucun libellé de la liste ne les nomme ; `modal.to-en-trop` et `spell.suffixe-sans-regle-orthographique` auraient convenu mais ne sont pas dans la liste de la carte), « from » (m019#2, aucun id).

## Défauts `content:tranche` (07)

- clé strictement la plus longue : 5/35 → **0/51** ; paires proches : 8 → **0** ; gabarit « three of these… » : ×2 → **0** ; positions de clé 13/13/12/13.
- Réécrits (même difficulté, même rang) : quiz inchangé ; 01#1 (phrase au lieu de l'espace de directions), 01#2 (le mot du lieu : travels ___ Tabarka by car), 01#3 (verbe greet), 02#1 (consigne positive, clé plus courte), 03#2 (France → England), 03#3 (distracteurs allongés), 04#1 (consigne positive a/an), 04#2 (clé plus courte), 04#4 (nouvelles données : routes Tunis–Sousse / Gabes, comparatif), 05#1 (de « east » à la place à l'écran), 05#3 (superlatif des trois moyens de transport), 05#6 (clé raccourcie). Les paires 04#4↔05#4 et 04#4↔quiz#5 sont levées par 04#4 ; 01#1↔05#1↔quiz#1 par 01#1 et 05#1 ; quiz#2↔01#3 par 01#3 ; quiz#3↔01#2 par 01#2 ; 02#4↔05#3 par 05#3.
- `lot-lint` : rien à signaler (les 9 fichiers). `content:check`, `content:qa -- --subject english-6eme` : 0 erreur. `content:gisement:controle` sur m021 : aucune plage ≥ 8 mots, aucune donnée commune.

## Missions

- **m018** (reading 2025) : 6 q. (3 QCM d'abord, puis `ordering` des 4 événements — l'item d'examen —, 2 QCM de compréhension écrits sur le texte : pourquoi lire tous les livres, idée principale). Texte lu en vision (PDF 2025 p.1-2), au plus 1–2 phrases citées par question. Étages 1,1,1,2,2,2. Rien de 07/03-revision#2.
- **m019** (2013–2025) : 5 q. au lieu de 6 (voir écarts) : old/new (2016), from (2015), 2×2 an old garage / a big garden (2013), `short_answer` north (2018, explication sans le mot), `ordering` en 5 groupes du mot « People around the world have different ways of greeting each other » (2025).
- **m021** (devoir, salle blanche ; carte seule, contextes inventés : Leila, Omar, Port Salma) : formules d'ouverture et de clôture (QCM), position sud-ouest sur la carte (QCM), `matching` 4 × 4 (lieu, position, monument, temps), phrase hors sujet (QCM), `multi` des informations à donner (4 justes sur 6), How about + -ing (QCM). Aucun nombre ni phrase de source.
- **D6 prononciation** : 4 QCM d'écoute écrite, consignes variées, /z/ et /s/ du pluriel puis /ai/ et /i/ du y final ; chaque distracteur porte `english.sound.lettre-pour-son` ; mots d'exercice distincts de ceux du cours (pas de clé qui fuit d'une question à l'autre).

## Items écartés, notions données, écarts à la carte

- **Écartés** : right ≠ left (déjà exclu), interested / interesting (HP), small ≠ big (2016 : contraires hors guide). Le « is » de « There is five rooms » (2013) est donné corrigé (« There are ») : there is / are est hors guide.
- **Donnés dans l'énoncé** (m021) : la règle d'une carte postale (Dear + lecteur, vœu d'adieu + auteur) ; « south-west » se lit par analogie avec le « north-west » du cours.
- **Écarts** : (1) m019 compte **5 questions** : les cinq items de la carte, chacun une seule question ; aucun sixième item sain n'existait sans fuite (une 6ᵉ question sur les directions ou le « greeting » aurait livré la clé du `short_answer` ou de l'`ordering`) ; (2) titre m019 « Exams **2013**–2025 » (la carte disait 2009 : les sessions fusionnées vont de 2013 à 2025, et le nom du fichier le dit) ; (3) m018 pose des `english.read.*` et m021 un `english.func.*`, absents de la liste « 07 » de la carte mais présents dans `map-vocab.md` ; (4) 01#1, 01#2, 01#3, 04#1, 05#1, 05#3 réécrits : les « Ne pas redemander » de m019 (01#1, 01#3, 04#1) pointent donc d'anciens contenus, la notion a/an, directions et salutations reste couverte ailleurs.

## Doutes pour l'auditeur

1. `a-an-selon-la-lettre` posé sur « a egg » et « an cape » : lettre et son coïncident, le libellé dit « d'après la lettre » ; j'ai lu l'étiquette comme « a / an mal choisi ».
2. `directions-confondues` sur les lettres E / N / S (03#1) et sur « north » de 04#6 (le texte dit south) ; « east » et « north-west » de 04#6 laissés muets.
3. `mot-voisin` : bow / touch / kiss peuvent être contestés comme « façons de dire bonjour » ; l'énoncé dit « the general action, in any way ».
4. `func.fonction-mal-identifiee` sur « Let's go swimming » et « How about a picnic » pris pour un adieu (m021#1).
5. m019#3 : l'option « a old … an big » (deux erreurs) et m021#2 « At the top, on the right » restent muettes (plan 2×2 complet).
6. 09#3 : « key » (ey, /i/ long) est un piège de lettres, non enseigné dans la section ; il est expliqué dans la réponse.
7. Le cours 07 dit que le y final dit /i/ dans un mot long et /ai/ dans un mot court, July étant l'exception du guide ; aucune autre exception (reply, apply) n'est posée en question.
