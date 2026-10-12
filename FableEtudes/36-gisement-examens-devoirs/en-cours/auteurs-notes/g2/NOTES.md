# Notes auteur T23-G2 (math 9e, chapitre 04, missions 29 a 33)

- Lu : consigne auteur devoir, pieges audit examen, prof-math-9eme, cours 04 (+ titres des cours 02/03/17/19), 2 devoirs publies du ch.04 (forme), registre des etiquettes (ids sur main).
- Ordre du manifeste : 15, 01, 19, 02, 16, 17, 03, 04 -> valeur absolue, radicaux, ordre/encadrement, calcul litteral sont enseignes avant ch.04.
- Non enseigne : trinome par forme canonique (ch03 = identites + facteur commun seulement) -> la forme canonique est DONNEE dans l'enonce (precedent : devoir 12).
- HP respectes : aucune inequation-produit ni inequation-quotient a inconnue ; le quotient n'intervient que par comparaison d'inverses de nombres donnes et images d'intervalles (ch17).
- Carte D21#3 annonce 4 etapes : decomposee en 6 questions (plancher anti-rush 6, consigne 6 a 8).
- Mission 31 (d4) : tags de difficulte de question plafonnes a 3 (schema).

## Livraison
- Fichiers : 29 (d3, 9 q), 30 (d3, 6 q), 31 (d4, 8 q), 32 (d3, 9 q), 33 (d3, 6 q) ; chapter.json deja porteur de la ligne de sources (rien modifie).
- Double resolution : sympy (chk.py) pour chaque cle et pour la fausseté des distracteurs a valeur numerique ; relecture a la main pour les distracteurs d'intervalles/encadrements (verifies faux, pas seulement differents : ex. 32 Q8, 31 Q3/Q4/Q6).
- Etiquettes : uniquement des ids de main ; options laissees muettes quand le libelle n'est pas l'erreur executee. Aucune famille neuve a proposer (pas de JSON etiquettes ecrit).
- Gates : aucune erreur nommant ces fichiers ; clé-plus-longue : aucun des 5 fichiers ; dupscan adapte (ch.04 29-33) : aucun doublon d'options a 4/4, restes = 3 petits entiers en commun (bruit) et formulations de consigne generiques.

## Tour de corrections (audit-T23-G2.md)
- M1..M10 + m1..m8, m10 appliques ; m9/m11/m12/m13/m14 : aucun changement de contenu (m11 = cours a completer hors tranche).
- Ecarts / defauts des textes de remplacement de l'audit :
  * 32 Q1 (m3) : la cle proposee (4) coincidait avec une racine de T (4) -> equation 3(x+1)=7x-17 (cle 5, options 7/2, 9/2, 5, 20).
  * 32 chaine T (m4) : T = x^2-2x-24 = (x-6)(x+4) retenue ; tout recalcule (Q3..Q9) ; encadrement sur [0;3] : produits -24,-42,-12,-21 ; vrai T dans [-25;-21] ; options toutes verifiees fausses sauf la cle. Q5 : piege « 5 au lieu de 6 » (au lieu de 3 au lieu de 4). Q7 -> {-4}, Q9 intervalle ]-4;6] -> {6}.
  * 31 Q8 (M8) : texte de l'auditeur garde pour l'enonce ; explication reecrite sans « 1/n >= 1/2 » ni n <= 2 a inconnue (comparaison de nombres 1/n calcules seulement).
  * 33 Q3 : phrase ajoutee « وهو يقبل عرضًا معدومًا » pour expliquer l'option muette.
- Verifs : sympy (chk2.py), absence dans tout origin/main des nouvelles expressions (git grep), dupscan ch.04, banc RTL : seuls artefacts connus (saut de ligne, « 14 m² »).
