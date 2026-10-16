# Journal du lecteur — français 9ᵉ, lot C31 à C36 (2010 et 2009 générale/technique ; 2008 et 2007 épreuve unique)

Lecture du 2026-10-16, à la suite du lot C01-C06 (conventions communes : `JOURNAL-lecture-C01-C06.md` § 0).
Les six PDF sont des scans sans couche texte (`pdftotext` : 4 octets pour C31-C32, quelques centaines pour les
autres, uniquement le bandeau du site) : lecture en vision, 150 DPI. Les six sha256 égalent ceux de `docs.json`.

## 0. CONVENTIONS (reprises du lot C01-C06 + ajouts)

- Grain, n°exo, chapitres, étages : inchangés (compréhension = 1 ligne n°1 ; une ligne par question numérotée de
  langue, n°exo = n° imprimé + 1 ; essai = dernière ligne, `08+09`, + `06` si récit, + `04` si dialogue exigé).
- **Barème décimal** : quand le total d'une question de langue est décimal (1,5 ; 2,5 ; 0,5), la colonne barème
  porte la valeur imprimée avec virgule (le validateur l'accepte) ; la compréhension et l'essai restent entiers.
- **RÈGLE DU PILOTE (texte support)** : le texte support n'est JAMAIS transcrit en entier. La section « Texte
  support » ne contient que : la référence (auteur, œuvre, éditeur, année si imprimés), le nombre de lignes
  imprimées (approximatif), un résumé neutre de 3 à 5 phrases écrit par le lecteur, les glossaires imprimés (mots
  courts), au plus deux citations d'une phrase dont une question a besoin (aucune n'était nécessaire ici : les
  questions sont autonomes), et la mention « Texte intégral : PDF officiel, sha256 au registre ». Consignes,
  questions et barèmes restent mot pour mot. Les transcriptions C31-C35 écrites avant la règle ont été réduites à
  cette forme ; C01-C06 (autre lot de ce journal) sont à reprendre à part par le pilote.
- Bandeau « www.edunet.tn » / logo NBMI : ajout du site de diffusion, noté dans l'en-tête, non transcrit.
- Épreuve unique (2008, 2007) : `filiere: unique`, un seul sujet, 2 h.

## 1. Documents lus

| id | session | filière | sha256 (= registre) | pages | lecture | lignes | transcription |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C31 | 2010 | générale | 47973b5398e6ad6d4126d93604e6b11edc1b790cee55b25a5ec903a3fab0a27a | 4 | vision | 6 | `french/2010-generale.md` |
| C32 | 2010 | technique | 7e0185ed92392dd0dcf931a148cd4667f16cb6f97ecf766027b3cdfc83320d0e | 4 | vision | 5 | `french/2010-technique.md` |
| C33 | 2009 | générale | b445e8d2354f1c6132ef0eb503196a2af04f4e3b865828a7ac781289a7f62808 | 4 | vision | 6 | `french/2009-generale.md` |
| C34 | 2009 | technique | 1fe9d1fbb21ed9460228896cef9265bc27a25825cdd7b7700e9bdffdbb68f747 | 4 | vision | 5 | `french/2009-technique.md` |
| C35 | 2008 | unique | 279de41de3280a8392ca2ae63907fa567d01bd5752a2222057ff0acd6fb4b6b8 | 4 | vision | 6 | `french/2008-unique.md` |
| C36 | 2007 | unique | a7ae8114a2f198b1da9f2b54cb24e7006a0a5525c15b1c4f1af622743e9f85be | 4 | vision | 6 | `french/2007-unique.md` |

Transcriptions sous `/home/user/wt-fr/content/programmes-officiels/examens-nationaux/9eme-base/french/`. Lignes :
`lines/C3{1..6}.tsv` + `.meta` (34 lignes ; `content:gisement:lignes --subject french --grade 9eme-base --content
/home/user/wt-fr/content` : 34 valides, 0 fautive). Snapshots : `/tmp/claude-0/frlec/snapshots/C3{1..6}.txt`.

## 2. Format de l'épreuve par session

Toujours trois parties sur 20 : Compréhension / Langue / Essai (le mot « Essai » remplace « Production écrite »
jusqu'en 2010 au moins). Générale 2 h (7+6+7), technique 1 h (8+6+6), épreuve unique 2 h (7+6+7). Texte support
plus court en technique ; vocabulaire glosé en page 1 en 2010 (technique), 2009, 2008, 2007.

| session | texte | compréhension | langue | essai |
| --- | --- | --- | --- | --- |
| 2010 G | dialogue grand-père / petit-fils | coche + phrase, réaction, exemples (7) | actif/passif 1 ; relatifs 1 ; subordonnées à compléter 2 ; passé simple/imparfait 2 | récit avec dialogue (7) |
| 2010 T | fable (boulanger et arbre) | cases, relation justifiée, mots à placer (8) | pronoms personnels 2 ; futur simple 2 ; que/parce que 2 | raconter une amitié (6) |
| 2009 G | récit d'un fils de mécanicien | relevés d'indices (7) | relatifs 2 ; grâce à/à cause de 2 ; imparfait 1 ; qu'elle/quel/quelle 1 | récit avec dialogue (7) |
| 2009 T | défi tracteur contre chevaux | cases, phrases à compléter (8) | mots d'une liste 2 ; futur simple 2 ; que/parce que 2 | paragraphe sur son futur métier (6) |
| 2008 U | enfance d'un garçon surnommé | écrire la réponse, relevé, sentiment (7) | actif/passif 1,5 ; relatifs 1,5 ; pronoms personnels 2 ; quel/qu'elle 1 | portrait physique et moral (7) |
| 2007 U | deux amis aux destins opposés | coche, vrai/faux, projet (7) | passif 2 ; bien que 1 ; passé composé et changement de sujet 2,5 ; quand/quant 0,5 | retrouvailles et portrait (7) |

## 3. Notions par chapitre (34 lignes)

| chapitre | lignes |
| --- | --- |
| 02 subordonnées | relatives (C31, C33, C35), complétives (C31), que/parce que (C32, C34), grâce à/à cause de (C33), bien que (C36) |
| 03 voix passive | C31, C35, C36 (jamais dans C01-C06 : notion tombée depuis, voir § 5) |
| 04 discours | essais C31, C33 (dialogue intégré) |
| 05/06 temps | passé simple/imparfait (C31), futur simple (C32, C34), imparfait (C33), passé composé (C36) |
| 07 lexique | C34 (mots d'une liste) |
| 12 pronoms | C32, C35 (pronoms personnels pour éviter les répétitions) |
| 13 accords | C36 (changement de sujet) |
| 14 homophones | quand/quant (C36), quel/qu'elle (C33, C35) |
| 01, 11, 15 | jamais |

**HP : aucun** (0 ligne sur 34) : toutes les notions entrent dans les 14 chapitres actuels. Le passif et la
concession (« bien que ») sont bien au programme (chapitres 03 et 02).

## 4. Ce qui a vieilli ou diffère des sessions récentes

- Intitulé « Essai » (anciennement) au lieu de « Production écrite ».
- Format de réponses : réponses sur lignes seulement, pas de cases en 2008 ; barèmes à demi-points.
- Fréquence : le passif est demandé à chaque session 2010-2007 (3 sur 6 ici) mais pas de 2024 à 2026 ; en revanche
  les adverbes en -ment, le futur antérieur et la subordination cause/but/conséquence apparaissent depuis 2024.
- Compréhension plus nettement factuelle (relevés, vrai/faux) avant 2010 qu'en 2024-2026 (justification et
  qualités).
- Aucune consigne n'est devenue fausse. Une consigne est **incohérente à l'impression** : C34 langue 2 demande le
  futur simple pour des verbes donnés à l'imparfait ou au passé composé (la correction attendue reste ambiguë) ;
  à ne pas reprendre telle quelle. C33 langue 3 : transposer des présents à l'imparfait, reprise possible.

## 5. Doutes et difficultés

- « grâce à / à cause de » (C33) classé `02` (cause, locutions prépositionnelles du cours de subordination).
- C35 : notes 2 à 4 du texte coupées en bas de page 1 de la copie diffusée (marquées [illisible] dans la
  transcription) ; le reste est net malgré une résolution plus faible.
- Un filtre de contenu a bloqué ma première sortie (texte littéraire) ; règle du pilote appliquée, aucun texte
  support reproduit dans les fichiers finaux.
