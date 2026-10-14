# Notes de l'auteur T23-I (maths 9e, chapitre 09, missions 42 à 46)

- 42 (d2, 7 q.) : D16#1. Le cube est hors du cours avant le chapitre 09 (géométrie de l'espace plus loin) : le triangle rectangle ACG est DONNÉ dans l'énoncé.
- 43 (d4, 8 q.) : D16#2. Données 4 ± √7 (produit 9, pas 1) pour ne pas retomber sur les paires inverses des examens ; le piège « inverse sans renverser » passe par CH = 9 / BH. Radical imbriqué posé comme « quel nombre a pour carré … » (vérification par carré, enseignée).
- 44 (d3, 7 q.) : D17#4. Le cercle (HP) n'est PAS un item : l'angle droit se prouve par la réciproque de Pythagore seule. Le centre de gravité est marqué HP au plan, mais le cours 08-thales l'enseigne (§ مركز ثقل المثلّث, avec le cas du triangle rectangle) et les devoirs 11 et 12 du chapitre l'utilisent : je l'ai gardé car c'est le piège de la carte. À trancher : si l'orchestrateur le veut hors mission, retirer Q5 à Q7 (la mission reste valide à 4 questions).
- 45 (d3, 6 q.) : D22#1. Le rapport d'aires k² n'est enseigné qu'au chapitre 13 (après le 09) : il n'est jamais donné ; l'élève calcule les deux aires par (base × hauteur)/2, le piège « rapport des longueurs/périmètres pris pour celui des aires » reste exécuté (option 3).
- 46 (d2, 6 q.) : D23#1. « Longueurs spatiales » : le pavé et ses deux triangles rectangles sont donnés ; l'étape de la relation à trois termes est posée en question (AB² + BC² + CG²).
- Plafond : 6 à 8 questions par mission (la carte en annonce 3 à 11 « étapes » : regroupées).
- Étiquettes muettes (erreur exécutée sans id exact au registre) : 42 Q7 « 1/√3 » ; 46 Q4 « 4 < x² < 9 » (posée sur carre-conserve-l-ordre faute de mieux, voir etiquettes/T23-I.json) ; 43 Q3 intervalle vide « 18/13 < CH < 9/7 » posé sur inverse-conserve-l-ordre.
- Réécritures après dupscan : divisibilité de 42 Q2 (28 divise D), cube d'arête 7, A(−9 ; 12), 44 Q4 et Q5 : options changées contre le publié.

## Tour de corrections (audit T23-I appliqué)
- M1 à M10 et mineurs appliqués par script depuis le § 7 de l'audit (champs remplacés tels quels, figures SVG43 et SVG46 insérées ; 43 Q1/Q4 et 46 Q5/Q6 portent SVG43 / SVG46 ; 44 Q5 sans le point G, 44 Q6 étiquette « L » à x = 138). Titres de 44 (m7) et 45 (M10) changés. Familles neuves marquées « écartées » dans etiquettes/T23-I.json.
- Vérifié à part (sympy et coordonnées) : toutes les clés des nouveaux textes, chaque distracteur faux, figure 43 (AB ⟂ AC en A, H à 256,4 px, AH = 77,8 px), pas de somme/différence d'options, dupscan et recoupement contre tout le publié, y compris wt-m21 (47-51) : aucun doublon d'options.
- ÉCART : 46 Q4 option a de l'audit (« 0 ≤ x² < 13 ») est VRAIE (x² < 9 < 13), donc un faux distracteur. Remplacée par « −2 < x² < 3 » (bornes recopiées sur x², erreur réelle, fausse pour x = 2,5), explication ajustée. Aucun autre texte d'audit défectueux trouvé.
- Les fichiers ne sont plus régénérables par build.py (corrections appliquées directement aux JSON).
