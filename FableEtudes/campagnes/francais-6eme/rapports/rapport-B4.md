# Rapport B4 — chapitres 07-profiter-du-temps-libre et 08-autres-modes-de-vie

Fichiers : `content/french-6eme/07-profiter-du-temps-libre/` et `08-autres-modes-de-vie/` (chapter.json, cours.md, resume.md, quiz.json, exercices 01 à 05).

## Chiffres
- 2 chapitres, 12 fichiers JSON de questions, 70 questions (5 de quiz + 30 d'exercices par chapitre).
- Cours : 8 sections par chapitre, patron de notion complet (ancrage, définition, tableau, exemple raisonné, piège, propriété avec cas-limite, vérifie, retenir) ; résumés à 8 puces (bijection).
- Types : 07 = 25 QCM, 4 multi, 2 ordering, 1 matching, 2 short_answer, 1 numeric ; 08 = 26 QCM, 3 multi, 3 matching, 2 short_answer, 1 ordering.
- Étiquetage des distracteurs QCM : 07 = 50/75 (67 %), 08 = 47/78 (60 %). Jamais sur multi, ordering, matching.
- coursePitfalls : 6 par chapitre, chacun montré dans un bloc `::: piege` et porté par au moins un distracteur (content:qa vert).
- Contrôles (sur un miroir du corpus limité à mes deux dossiers, les autres chapitres étant en cours d'écriture) : `content:check` vert ; `content:qa` et `qa:strict` 0 erreur 0 avertissement ; `content:tranche --fresh --strict-longest --strict-lessons` : clé la plus longue 0/51, 0 paire proche, 0 gabarit, patron de notion 0 en recul ; prettier --check vert ; rendu `renderLesson` / `renderSummary` vérifié par un test jetable (supprimé).

## Reprises du cahier 121615 déclarées (champ `manuel`)
- 07/03-revision : p.85 ex.2a (ordering), p.87 ex.1 et ex.2, p.94 ex.4a (multi).
- 07/05-entrainement : p.93 ex.1 (un item, QCM « neuf → neuve »).
- 08/01-pratique : p.97 ex.1 (multi), p.99 ex.3 (deux items).
- 08/03-revision : p.97 ex.2, p.99 ex.3, p.103 ex.1b, p.108 ex.2.
- 08/05-entrainement (manuel 121614, jeux p.132) : ex.3 (intrus), ex.4 (contraires, matching), ex.5 (proverbe).
Tous les autres items sont des variantes (non tracées), notamment toutes les lettres et tous les récits.

## Écarts à la fiche et choix
- Aucun fait « à arbitrer » ni ⛔ n'est enseigné ou ciblé (F1) ; F5 respecté : aucune question sur l'accord avec avoir. Le cours 08 contient une seule phrase de cas-limite reprenant le constat du manuel p.125 (« avec avoir, le participe ne s'accorde pas avec le sujet »), rangé ✅ aux bornes du §2.8 : l'auditeur peut la retirer si F5 doit être lu plus strictement.
- Le cahier p.108 ex.1 (mélange avoir, imparfait) et p.98 ex.2 (capitales) ne sont pas repris (voir `auteurs-notes/B4/NOTES.md`).
- Aucun id manquant au registre `fr.*` : tout est posé avec les ids existants. Pistes pour une campagne suivante (non ouvertes, seuil de 3 questions non atteint) : « veux/peux avec nous » (terminaison de la mauvaise personne), « par taxi » (préposition de manière).
- `exercices/04-defi` : seuls ordering, matching, multi et short_answer ont des clés non étiquetables ; la part muette vient surtout des distracteurs de conjugaison à autre personne (veulent, pouvons…), laissés muets selon la règle R3.

## Doutes pour l'auditeur
1. 07/03-revision #1 (« Dites-moi votre avis ») : bien vérifier qu'aucune autre option n'est défendable.
2. 07/05 #4 (nombre pensé) : listes de 1 à 15 originales (code binaire), calcul revérifié (6 = 2 + 4).
3. 08/04-defi #6 et 07/03-revision #4 : questions de lecture sur textes courts maison ; vérifier qu'un indice du texte tranche.
4. 08 cours section 7 : proverbe « Petit à petit, l'oiseau fait son nid » et comparaisons animales (taureau, lapin, escargot, gazelle) venues du vocabulaire du manuel p.132 ; le proverbe « Tous les chemins mènent à Rome » n'est que dans l'exercice 05 (reprise).
5. Gabarits : la structure « quel groupe est le complément de temps / de manière » revient dans les deux chapitres (notions parallèles) ; formulations variées pour limiter l'effet de gabarit.

## Corrections après audit
Appliqués avec les textes exacts de l'auditeur (audit-B4.md) : C-1 (07/08 03 q5, option « par » remplacée par « à »), M-2 (trois tableaux de 4 colonnes scindés en tableaux de 3 colonnes au plus, ainsi que le tableau de la lettre et le tableau narration/description en 2 colonnes), M-3 et M-10 (deux règles fausses), M-4 à M-7, M-9, M-11 (leur retiré de l'exemple et du verifie), M-12 (rentrer ajouté au cours et au résumé), M-13 (contraires enseignés au cours, q2 réduite à 3 paires, q5 sans fuite), M-14 à M-17, m-2 à m-8, m-10, m-12, m-13, M-8 et M-18 (coursePitfalls : 10 au 07, 9 au 08). Les cours gardent les italiques corrigés par le pilote ; aucun fichier de référence de l'auditeur n'a été copié.

Écart : `fr.lexique.contraire-pour-synonyme` (coursePitfalls 08) n'est pas compté par le gate quand il ne figure que dans `expectedMistakes` d'une question libre ; j'ai donc remplacé 08/01-pratique q6 (famille de « voyage », étiquette mot-voisin) par « contraire de lointain » portant l'étiquette sur deux distracteurs. La famille de mots reste testée par 05 q1.

Non appliqués (jugés facultatifs, sans effet sur les gates) : m-9 (calibrage d4 des défis), m-11 (test des mots-outils), m-15 (planche SVG de BD), copies tolérées m-14.

Contrôles sur le corpus réel : `content:check` vert (french-6eme : 8 chapitres, 240 questions) ; `content:qa -- --subject french-6eme` vert ; `content:tranche … --fresh --strict-longest` : clé la plus longue 0/51, 0 paire proche, 0 recul de patron, 3 gabarits inter-chapitres avec le 06 (lieu/temps, acceptables) ; `prettier --check` vert ; rendu `renderLesson`/`renderSummary` : 0 `_` et 0 `*` dans le texte rendu des deux cours et des deux résumés (test jetable supprimé).

## Missions du gisement (lot M4)
Fichiers (`content/french-6eme/`), 144 questions au total, `chapter.json` : ligne « Sujets officiels du concours… » ajoutée aux deux chapitres, ligne « Calibré sur des devoirs publics… » au 08.
- 07 : `06-exams-2012-2018-quand-dire-et-ecrire` (m025, d2, 7 q) ; `07-exams-2010-2026-adjectifs-au-feminin` (m026, d2, 6 q) ; `08-exam-2022-lecture-lucile-sur-les-planches` (m027, d2, 9 q) ; `09-exams-2008-2022-recit-suite-ou-realisation-scene` (m028, d3, 9 q).
- 08 : `06-exams-2009-2025-complements-tableau-enrichir-deplacer` (m029, d2, 10 q) ; `07-exams-2008-2026-vouloir-et-pouvoir` (m030, d2, 10 q) ; `08-exams-2012-2024-passe-compose-avec-etre` (m031, d2, 7 q) ; `09-exam-2025-lecture-pyramide-maya` (m032, d2, 8 q) ; `10-devoir-ecrire-une-lettre-lointaine` (m033, d3, 8 q, nom corrigé par le pilote).

Écarts à la carte :
- Nombre de questions : m026 (6 au lieu de 8), m031 (7 au lieu de 8), m032 (8 au lieu de 9) : les items à deux blancs ou deux questions jumelles (leak par l'ordre d'émission) sont fondus en une question.
- Les tableaux à quatre colonnes sont des `matching` : aucune étiquette possible (m025 q1, m029 q1 à 6). Le piège de ces lignes est porté par les QCM voisins.
- m033 : l'ordering des parties de la lettre est remplacé par l'ordre des paragraphes du corps (les parties sont déjà demandées par 07/04-defi q3, « ne pas redemander »). Salle blanche respectée (carte seule, contextes inventés) ; `content:gisement:controle` : 0 plage de 8 mots, 0 exercice source repris.
- Production (m028) : questions fermées sur la préparation ; pour 2008 le contexte du récit est donné en une phrase.

Notions données dans l'énoncé (non enseignées au chapitre) :
- E6 : « au féminin, l'adjectif s'écrit nulle » (m026 q1) ; participes couvert et emballée donnés (ch08, m026 q5-q6) ;
- radical pourr- du futur de pouvoir (m030 q7) ; participe voulu (m030 q10) ;
- temps imparfait de « allais » et passé simple de « suivit » signalés comme non évalués (m029 tableaux 2019 et 2015) ;
- orthographe imprimée « apparait / disparait » (2025) citée telle quelle.

Items écartés : aucun de la carte ; C11#8 et C01#7 restent écartés (E7, plan). Option « avoir + accord » évitée partout (F5) : « ont fait », « n'avons pas trouvé » sans accord.

Doutes pour l'auditeur :
- m029 tableau 2019 : « les mains dans les poches » classé complément de manière (réponse du sujet, construction absolue) ; 2009 « un peu angoissés » idem.
- m027 q4-q5 et m032 q1, q8 : questions d'opinion converties en QCM d'arguments ancrés dans le texte ; vérifier qu'une seule réponse est défendable.
- m032 q7 : le contraire de « disparait » est « apparait » ; « surgit » n'est volontairement pas proposé.
- Paires proches (Jaccard ≥ 0,45, 19 couples) : toutes dans une même mission de langue (tableaux, formes d'un même verbe, deux blancs d'une même réécriture), données officielles différentes : exercices parallèles voulus, non réécrits.
- Un seul rouge de `content:qa` : `02/07-exams-2009-2026-imperatif-fais-parler` Q11 (explication qui désigne une option par son rang), hors de mon périmètre.

Contrôles : `content:check` vert ; `content:qa` : seule erreur ci-dessus (chapitre 02) ; `content:tranche … --fresh --strict-longest` : clé la plus longue 0/110, positions 27/24/25/24 % ; `prettier --check` vert.

## Corrections après audit des missions
Tous les correctifs de `audits/audit-M4.md` sont appliqués avec les textes de l'auditeur ; aucun refusé.
- Critiques : C-1 (08/06 q8, option d remplacée par « Hier matin, dès huit heures… »), C-2 (08/06 q10, option b « À travers la scène, pieds nus, je me mets. » étiquetée, prompt et explication reformulés), C-3 (08/09 q7, la clé devient « surgit », pris dans le texte).
- Fuites : blancs vides dans les deux énoncés et blanc visé nommé pour 07/06 (écoute / écris), 07/07 (q5), 07/08 (q1, q2), 08/07 (q2, q3-q4, q6, q10), 08/08 (q2, q4).
- Majeurs : 07/06 q3 supprimée (la mission passe à 6 questions) ; 07/08 q5 option b remplacée (« Parce que Lucile lui a dit qu'elle adorait le théâtre ») ; 08/08 q6 b devient « ont arrivé » (F5) ; 08/10 q1 option b « Tu salues Malek et tu lui donnes de tes nouvelles. ».
- Mineurs : consignes reprises mot pour mot (« remplis le tableau suivant… », parenthèse « (Intègre un court dialogue dans ton récit). »), explications de 07/06 q4 et 07/08 q8, étiquette de 08/09 q8 a retirée.
- Contrôles : `content:check` vert (501 questions) ; `content:qa -- --subject french-6eme` vert ; `content:tranche … --fresh --strict-longest` : clé la plus longue 0/109, positions 27/24/26/24 % ; `prettier --check` vert. Paires proches restantes : 17, toutes sans fuite (tableaux de 08/06, 07/06 q5-q6 et 08/08 q3-q4, q6-q7 sont à blancs vides ou sur des phrases officielles différentes).
