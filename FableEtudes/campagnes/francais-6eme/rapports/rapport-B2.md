# Rapport B2 — french-6eme, chapitres 03-accepter-les-autres et 04-sentraider-pour-reussir

Fichiers : `content/french-6eme/03-accepter-les-autres/` et `04-sentraider-pour-reussir/` (chapter.json, cours.md, resume.md, quiz.json, exercices/01-pratique … 05-entrainement).

- 70 questions (35 par chapitre : quiz 5 + 5 exercices × 6). Types ch.03 : 23 QCM, 5 multi, 2 ordering, 2 matching, 3 short_answer ; ch.04 : 23 QCM, 2 multi, 3 ordering, 3 matching, 4 short_answer. Aucun short_answer dans un quiz.
- Étiquetage des distracteurs de QCM : ch.03 44/69 (64 %), ch.04 53/69 (77 %). Aucune étiquette sur multi/ordering/matching ; options à deux erreurs et valeurs de remplissage laissées muettes.
- coursePitfalls : ch.03 6 ids, ch.04 6 ids (chacun montré en `::: piege` et porté par un distracteur). Le cours 04 montre 8 pièges (deux de plus, non déclarés car aucun distracteur du chapitre ne les porte : proverbe lu au sens propre, texte documentaire pris pour un récit — à arbitrer par l'auditeur : ajouter un distracteur ou retirer le piège).
- Contrôles : content:check OK (arbre isolé, voir ci-dessous), content:qa 0 erreur 0 avertissement, tranche : clé la plus longue 0/46, paires proches 0, patron de notion 0 en recul, prettier OK, rendu renderLesson/renderSummary propre (aucun `**`, `:::` ni `_` résiduel).
- Reprises du cahier 121615 déclarées (champ `manuel`) : ch.03 03-revision (p.34 ex.3, p.41 ex.2), 05-entrainement (p.32 ex.1a une phrase, p.41 ex.1) ; ch.04 03-revision (p.45 ex.2 et 3 une phrase chacun, p.47 ex.4a, p.51 ex.1 et 3), 05-entrainement (p.49 ex.1d phrase 1, p.50 ex.4 sur 5 phrases). Reprise du manuel 121614 : ch.04 02-boss (p.69 jeu 4, proverbes).
- Écarts / doutes pour l'auditeur :
  1. Les contrôles ont été lancés sur un arbre isolé (liens vers mes deux chapitres seulement) parce que `content:check` global échoue tant que 05-sauver-la-nature (autre auteur) n'a pas son quiz.json.
  2. Cahier M4 p.46 ex.3 (ordre « tournent à gauche ») non repris : l'ordre attendu est une déduction du lecteur ; remplacé par une variante à 4 phrases sans cette étape.
  3. Cahier M4 p.50 ex.4 : 5 des 6 phrases (une seule colonne par phrase, bijection exigée par `matching`).
  4. Textes de lecture : textes originaux (Yassine/Hanen, Nour/Walid, Hutché en deux phrases) ; « Le jeu du Petit Poucet » et « Un bouquet de bienvenue » (lecture-action) ne sont pas enseignés (pas d'exercice du cahier, pas de fait de langue).
  5. `fr.lexique.mot-voisin-du-meme-champ` sert aussi à « avoir la paix / lire en paix » (ch.03) et au choix amitié / amical / ami (ch.04) ; le libellé est un peu large pour ces deux cas.
  6. Des textes d'exercice emploient l'imparfait en support (« se moquait ») : support seulement, jamais ciblé.
  7. Le `matching` du ch.03 05-entrainement porte sur les mots de la boîte à mots (variante, non tracée).

## Corrections après audit (audit-B2.md)

Contrôles relancés sur le corpus réel (8 chapitres) : content:check OK (1066 chapitres), content:qa 0 erreur 0 avertissement, tranche clé la plus longue 0/46 et paires proches 0, prettier OK, rendu des cours propre. Tous les correctifs de l'auditeur ont été appliqués tels quels ; aucun refusé.

- C-1 (04 revision q6, « pas » défendable) → prompt « Complète avec « plus » ou « jamais » » + explication de l'auditeur.
- C-2 (04 defi q3, « pas toujours » contredit la phrase) → option remplacée par « J'ai jamais fini… » (ne-oublie) + explication.
- M-1 (03 cours lecture, réponse modèle sans indice) → ancrage « Alors il reste à l'écart de leurs jeux » et exemple « il boite. Alors il reste à l'écart ».
- M-2 (03 defi q1, rang d'option) → option c « Le pêcheur regarde le lac calme. » + explication sans rang.
- M-3 (03 defi q5, proverbe non enseigné) → puce « proverbe » ajoutée au cours 03 ; option b remplacée (muette).
- M-4 (03 entrainement q1, accord faux dans l'explication) → explication corrigée.
- M-5 (03 quiz q5, forme « en criant ») → « en criant » retiré partout, options a/c/d de l'auditeur ; longueurs 39/48/44/48, la clé reste à égalité (non strictement la plus longue, tranche 0/46).
- M-6 (03 boss q5) → option d « vivre en paix avec tout le monde » (voisin-du-meme-champ) + explication.
- M-7 (04 cours l.31, astérisque littéral) → balisage corrigé.
- M-8 (04 cours, documentaire absent) → court documentaire en deux rubriques inséré avec sa phrase de liaison.
- M-9 (04, deux pièges sans distracteur) → defi q2 remplacée par le proverbe « L'union fait la force » (sens-figure-lu-au-propre), defi q5 option d « Ce texte raconte l'histoire d'un enfant… » (informatif-pris-pour-narratif), 2 ids ajoutés à coursePitfalls (8).
- M-10 (04 defi q1, rang d'option) → explication reformulée.
- M-11 (04 defi q4, phrase absente du récit) → phrase insérée dans le prompt.
- M-12 (04 entrainement q5) → « amical » muet, « amicalement » remplacé par « entraide » (voisin-du-meme-champ), explication.
- Mineurs : 03 rev q1 option d étiquetée ; 03 rev q2 données du cahier rétablies (« blanc », fin de phrase) ; passé composé « avoir et être » (cours 03 l.67) ; « l'adjectif épithète… le » ; puce verbe introducteur ajoutée ; 03 defi q6 « oublient ou déplacent » ; 03 entrainement q6 → « honteux » / « paraissent » sans acceptedAnswers ; 04 cours vérification « Mon frère range toujours… » ; « La mère crie » ; cas-limite du participe ; étiquettes TEMPS sur « remplissez » et « choisissent » ; RECIT sur boss q4 option b ; « Au carrefour, » dans la variante p.46 ; doubles espaces avant « (verbe… ) » supprimés.
- Non fait (hors de mon périmètre) : mineur 03-9, ajout des modules 03 et 04 pour `fr.lexique.sens-figure-lu-au-propre` dans `vocab-french-6eme.json` / `map-vocab.md` (fichiers de l'autre agent) ; mineur 03-8 toléré par l'auditeur ; mineur 04-8 (données raccourcies des reprises p.51) accepté tel quel.

## Missions du gisement (lot M2)

Fichiers (6 missions, 38 questions) :
- ch.03 : `06-exams-2010-2023-epithete-attribut-et-etre` (d2, 5 q), `07-exams-2016-2017-recit-faire-accepter` (d3, 7 q), `08-devoir-lire-ordre-titre-portrait` (d2, 8 q, devoir en salle blanche).
- ch.04 : `06-exams-2018-2024-phrase-negative` (d2, 5 q), `07-exams-2020-2025-verbes-comme-finir` (d2, 6 q), `08-exams-2015-2021-recit-entraide` (d3, 7 q).
- `chapter.json` : ligne `sources[]` des examens ajoutée aux deux chapitres, ligne « devoirs publics » ajoutée au 03.
- Contrôles : content:check OK, content:qa 0 erreur 0 avertissement, tranche (--fresh --strict-longest) clé la plus longue 0/72, paires proches 0, gabarits 0 ; prettier OK ; `content:gisement:controle` sur le devoir : 0 plage de 8 mots.
- Correction annexe : l'intitulé de section du cours 04 « Les verbes comme finir au passé composé et au futur » recoupait mot pour mot une source web (garde anti-verbatim) ; devenu « … : passé composé et futur ».

Items écartés ou réduits :
- C11#8 (2016, « La veille, vous … tristes ») écarté (E7).
- m009 : 5 questions au lieu de 8 (item 2016 conj. 2 écarté ; le tableau 2016 gram. 1a fusionné en un seul matching parce que les deux QCM attribut/épithète étaient des quasi-doublons). Pour 2023 le second verbe (durera) est donné ; la 2e question porte sur le nom du temps de « J'ai été ».
- m012 : la variante 2018 avec « plus » a été retirée (quasi-doublon à 0,79 de la précédente) ; 5 questions.
- m013 : 6 questions au lieu de 8 (le 2e QCM de 2021 aurait redemandé `04/quiz#3`) ; les formes en -er (ébauché, grimpé, laissera) sont données.
- m014 : le multi « éléments exigés » de 2015 retiré (doublon de celui de la mission 03) ; 7 questions.
- Hors scope non ciblés : accord des participes, pronoms compléments (« nous » dans « La peur nous broie » reste devant le verbe, dit dans l'énoncé).

Notions données dans l'énoncé (non enseignées par le cours) :
- « demeure » est un verbe d'état comme rester (m009, 2020) ;
- « toujours » veut dire « à chaque fois » (m012, 2021) ;
- l'article est « de » dans toutes les réponses (m012, 2019) ;
- titre, portrait et ordre du texte vs ordre des faits : définis dans l'énoncé des questions du devoir (m011) ;
- les cinq temps du récit sont rappelés dans m014 (cours 04).

Doutes pour l'auditeur :
1. Les questions 2023 « à quel temps est conjugué J'ai été » et la variante 2021 avec « encore » ne sont pas des items officiels : elles sont signalées « d'après » dans l'énoncé.
2. Dans m012 (2021 q2), « plus » reste un distracteur à surveiller malgré la précision sur « toujours ».
3. m010 : les distracteurs étiquetés `fr.production.hors-sujet` (répliques hors sujet) sont éliminables à la lecture de la situation ; c'est voulu (lire la consigne), mais l'auditeur peut juger la difficulté faible.
4. m011 : les deux `ordering` du devoir sont jumeaux (ordre du texte puis ordre des faits) ; seule la seconde, chronologique, est proche de `fr.lecture.ordre-chronologique-non-respecte` (non posable sur un ordering).
5. Le devoir `m011` a des distracteurs muets (noms et verbes à la place de l'adjectif) faute d'étiquette exacte.

## Corrections après audit des missions (audit-M2.md)

Tous les correctifs de l'auditeur sont appliqués avec ses textes exacts ; aucun refusé. Contrôles : content:check OK, content:qa 0 erreur 0 avertissement, tranche clé la plus longue 0/72, prettier OK. Le fichier du devoir est désormais `08-devoir-lire-ordre-titre-portrait.json` (nom pris dans l'arbre).

- C-1 (m012 q1) : options c « ne nous broie toujours » (negation-sens-inexact) et d « ne jamais nous broie » (negation-mal-placee), explication de l'auditeur.
- C-2 (m012 q5, « Veux-tu du pain ? ») : options « Non, je ne pas veux de pain. » (negation-mal-placee) et « Non, je ne veux de pain. » (muette), explication de l'auditeur.
- M-1 : explications sans rang pour m011 q7, m010 q7, m014 q2, q5, q7.
- M-2 : texte sur Karim redonné en tête des questions 2, 3 et 4 du devoir. Conséquence attendue : le contrôle « paires proches » signale 7 couples (0,45 à 0,90) entre les questions du devoir, tous dus au texte partagé ; ils sont voulus (le donjon tire les questions au hasard) et non bloquants.
- M-3 : les deux short_answer de m013 supprimées ; la mission garde 4 questions (2025, 2021, 2020, 2022).
- M-4 : m014 q3 remplacée par la variante « s'écrie » (Mon chat ! Te voilà enfin !).
- M-5 : m010 q1, trois répliques plausibles mais muettes, explication de l'auditeur.
- M-6 : explication de m009 q2 réécrite.
- Mineurs : « D'après le concours 2023 » (m009 q2) et « D'après le concours 2021, avec « encore » » (m012 q3) ; consigne officielle du tableau de 2020 mot pour mot ; consignes de rédaction ajoutées à m014 q1, q4, q6 et m010 q5 ; option « m'a envahi » de m013 remplacée par « m'envahit » (F5) ; explication de m011 q8 corrigée.
