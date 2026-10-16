# Corrections L01 (suite à audit-francais-L01.md)

Générateurs : /tmp/claude-0/fr-gis/L01/m001..m006.py.
- m001 (7 q.) : Q1 option « pas décidé » -> « Le public était venu nombreux » ; Q2 expl. ; Q3 joie/peur/fierté ; Q4 énoncé « grandes étapes de [sa] vie » ; ancienne Q6 supprimée ; Q8 refait.
- m002 : Q5 énoncé + option b ; Q6 option c ; Q7 énoncé.
- m003 (6 q.) : Q1+Q2 fusionnées (2x2) ; Q3 expl. ; Q4 énoncé ; Q6 option b + expl. ; Q7 refaite.
- m004 (7 q.) : 2x2 rêve, « redescend sur terre », 2x2 silence, réaction, Frank, participants, activités.
- m005 (6 q.) : 2x2 collège, 2x2 familles, actions, côte à côte, raison 1, raison 2 ; étiquette Q6 b -> deduction-sans-indice.
- m006 (9 q.) : Q1 consigne + options a/d ; Q3 remplacée (infirmier) ; Q4 reformulée ; consignes Q5, Q6, Q8 rétablies ; Q9 expl.
- 09/05 Q2 (publiée) réécrite sur place (fichier identique à origin/main avant) ; 08/05 non touché.
- Clés des 2x2 déplacées (helper place()) pour répartir les positions.

## Écarts à l'audit
1. m001 Q8 : clé « m'efforçant d'ignorer… » (sans « En ») : avec « En » elle faisait 79 car. contre 76, donc strictement la plus longue.
2. m006 : les 3 étiquettes sur options de `multi` (Q5 d, Q6 c, Q6 e) NON posées : le schéma les refuse (essayé : « Unrecognized key misconceptionTag »). Restent muettes.
3. m006 Q4 : option « Je t'embrasse… » remplacée par « Je voulais te parler du film… » (étiquette hors-sujet, comme l'audit).
4. m001 Q2/Q3/Q8 etc. : citations vérifiées littérales par script (hors consignes inventées). Une expl. « marche d'un pas décidé » corrigée en « avance « d'un pas décidé » ».
5. m005 « côte à côte » : citation sans l'appel de note ² (« studieuses² années »).
6. m004 Frank = entraîneur : déduit (camarades nommés Charly, Théo, Loïc ; l'entraîneur est le seul à annoncer le stage).
7. m006 Q3 : infirmier (déjà cité au 08/04 Q5 et 08/01) : suivi de l'audit, geste différent (raison vs description).

## Suite (reverif-francais-L01.md)
- m002 Q7 : nouvel énoncé et options du rapport (salaire / fatigue / équilibre-harmonie / promotion).
- m003 Q1 b, d : « Je fixais cette porte » à la place de « Il faut sauver le gardien ! » ; Q2 e : « la chaleur était devenue insupportable » ; explications ajustées. Q6 : l'explication cite « Ils ont éteint l'incendie, puis ils ont emmené Yves ».
- m004 Q5 (Frank) supprimée : 6 questions.
- m006 Q3 : thème agriculteur, options du rapport.
- 09/05 Q2 : option a « Un camion s'est renversé à Kairouan, chauffeur indemne. ».
- Écart : m006 Q7 (conclusion, pas citée au rapport) : la clé était strictement la plus courte (82 car.) ; elle devient « …précieux pour moi comme pour les autres. » (88, entre 84 et 92).
- Remesure : aucune clé strictement la plus longue ni la plus courte dans 05 et 06-11. Gates : check vert, qa:strict 0, tranche 0/67, lot-lint rien.
