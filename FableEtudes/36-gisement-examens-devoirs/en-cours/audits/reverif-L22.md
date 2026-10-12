# Re-vérification ciblée — L22 (18/42, 07/25, 12/22)

Arbre `wt-m22` tel quel ; comparaison champ à champ avec les copies corrigées de l'audit (bloc-notes), puis re-résolution, gates, banc `dir=rtl`, doublons. Notes des auteurs non ouvertes (consigne auditeur) ; seul écart déclaré par l'orchestrateur : point final en 07 Q6.

## 1. Application mot pour mot

Script de comparaison (chaque champ de chaque question, en-têtes compris) entre les trois fichiers et les copies où l'audit
avait appliqué ses textes : **tout est identique**, à une seule différence près. Dans 18 Q7, la figure reprise de Q8 porte le
`<title>` « المثلّث ABC وشبه المنحرف EFCB » au lieu de « شبه المنحرف EFCB داخل المثلّث ABC » ; le tracé est identique octet pour
octet. C'est un écart neutre : l'arabe reste dans `<title>`, aucune clé n'est en jeu. Le « point final en 07 Q6 » était déjà
dans le texte de l'audit (« … و[1100 ; 1300[. ») : aucun écart réel.

## 2. Re-résolution (questions retouchées et voisines)

| Fichier | Q | ma réponse | clé | verdict |
| --- | --- | --- | --- | --- |
| 18/42 | 5, 6 | 18, 12 | c, a | OK — Q6 définit maintenant F |
| 18/42 | 7 | 60 × 40 ÷ 2 − 18 × 12 ÷ 2 = 1092 | c (1092) | OK — 1200, 984 (= 1200 − 216), 840 (= 1200 − 360) faux et exécutés |
| 18/42 | 8 | 40 − 12 = 28 | d (28) | OK — 12, 15, 35 (= EB) faux ; aucune somme ou différence de deux options ne vaut 28 |
| 18/42 | 9 | 10,92 | c | OK |
| 07/25 | 3, 4 | 1000, [500 ; 700[ | a, d | OK — Q4 définit la classe modale, sans tableau annoncé |
| 07/25 | 5 | 190 | b | OK — 70 = 30 + 40, 140 = 70 + 30 + 40, 40 ; 190 n'est la somme ou la différence d'aucune paire |
| 07/25 | 6 | 120/200 = 60 % | c | OK — l'énoncé en classes rend 75 % exactement « classe commençant au seuil » |
| 07/25 | 7 | 690 | a | OK |
| 07/25 | 8 | ≈ 640 (642,86) | d | OK — 560 (≈ 557, depuis la borne haute) ; plus de marqueur de forme |
| 12/22 | 1 | (x + 2)/2 = 1 + x | c | OK — l'explication nomme les équations, plus aucun rang |
| 12/22 | 3 | (2 − √2)² | c | OK — plan 2×2 {2 ; 3} × {+ ; −}, plus de vote possible |
| 12/22 | 4 | (OJ) (milieu (0 ; 4), médiatrice x = 0) | d | OK — O, J et (AB) faux ; le rappel couvre les quatre options |

**Clés fausses : 0/21.**

## 3. Rampes, en-têtes, fuites

- Rampes : 18 = 1,1,2,2,2,2,2,3,3 ; 07 = 1,1,1,1,2,2,3,3 ; 12 = 1,2,2,2. Toutes sont non décroissantes, donc l'ordre
  d'émission est celui du fichier.
- En-têtes inchangés : d3/boss/120/30/42 ; d3/boss/120/30/25 ; d2/practice/75/15/22.
- Fuites :
  - 18 Q7 ne redonne que AO = 40 (clé de Q3), EF = 18 (clé de Q5) et AK = 12 (clé de Q6), toutes antérieures. BC = 60 est
    une donnée.
  - Ni l'énoncé ni l'explication de 18 Q7 n'écrivent 28 ou 10,92.
  - Aucune autre explication ne résout une question suivante ; aucun ✓ ne suit un distracteur.

## 4. Étiquettes ajoutées (libellés relus sur `origin/main`)

| Question | Option | Étiquette | Jugement |
| --- | --- | --- | --- |
| 18 Q7 | 1200 | `reponse-a-l-autre-inconnue` | exacte : « un résultat intermédiaire » |
| 18 Q7 | 984 | `aire-triangle-sans-moitie` | exacte |
| 18 Q8 | 12 | `reponse-a-l-autre-inconnue` | exacte : AK est un résultat intermédiaire |
| 07 Q5 | 70, 140 | `classes-concernees-incompletes` | exacte |
| 07 Q6 | 40 % | `reponse-a-l-autre-inconnue` | exacte : « l'autre inconnue » |
| 07 Q8 | 560 | `interpolation-mal-posee` | exacte : « point de départ » |

Les étiquettes restées muettes sont celles prévues : 18 Q7 840 ; 18 Q8 15 et 35 ; 18 Q9 109,2 et 4,68.

## 5. Figure 07 Q7 et rendu `dir=rtl`

- Tableau vertical rendu dans Chromium (340 px) : net, aucun chevauchement. Classes à droite, effectifs à gauche, comme le dit
  l'énoncé.
- Banc `bench-rtl` à 360 et 600 px sur les trois fichiers : aucune formule à lettres brouillée. Seule reste « 468 cm² » dans
  l'explication de 18 Q9 : c'est un cas du moteur, l'ordre de lecture est exact, ce n'est pas un défaut de contenu (déjà noté
  à l'audit).

## 6. Gates et doublons

- `content:check` vert. `content:qa:strict` : 0 erreur, aucun avertissement sur les trois fichiers.
- `content:tranche` 18/07/12 : la clé n'est jamais strictement la plus longue sur la tranche. Une seule paire proche :
  12/22 Q2 ↔ 12/15 Q4 (Jaccard 0,45), déjà jugée non-doublon (autres points, autres options).
- Scan de tout le publié de maths, quiz compris : aucun quasi-doublon.
  - 18 Q7 n'a plus aucune sœur : le gabarit de 18/26 Q5 est levé.
  - 07 Q5 ne partage que 2 valeurs d'options avec 07/17 Q4 (énoncés sans rapport, Jaccard 0,04).
  - 07 Q6 ↔ 07/15 Q6 : autres données, autre seuil.
  - 12 Q4 ↔ 20/22 Q3 : 2 options communes ((OJ), O), autres points, autre clé.
- Entre les trois missions : aucun doublon.

## Verdict

0 clé fausse ; 0 majeur restant ; 0 mineur restant. Seul écart d'application : le `<title>` de la figure de 18 Q7, neutre.
**Livrable.**
