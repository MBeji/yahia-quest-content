# Re-vérification — tranche T23-G2 (ch. 04, missions 29 → 33, après correctifs de l'auteur)

Périmètre : `/home/user/wt-m22/content/math/04-equations-inequations/exercices/29…33-devoir-*.json`, arbre tel quel. Rien n'est modifié, aucune
écriture git. Registre des étiquettes relu sur `origin/main` (re-fetch : empreinte md5 8ef25a0e… identique à celle de l'audit).

## 1. Re-résolution à l'aveugle (avant lecture des clés ; sympy)

Questions retouchées et voisines :
- 29 : Q5 [−1 ; 5[ · Q6 {0 ; 7} · Q7 x ≥ 0 · Q8 9 · Q9 k = 8.
- 30 : Q5 x ≤ −2 − √3 · Q6 2 ((√15 + 3)/6 ≈ 1,145).
- 31 : Q1 (√7 − 2)/3 · Q2 2√7/3 · Q3 2 ≤ x ≤ 5 · Q5 1/(√7 − 3) < 1/(√7 − 1) (seule vraie : −2,82 / 0,61 / 1,55 / 0,27) · Q8 2.
- 32 (chaîne refaite, T = x² − 2x − 24 = (x − 1)² − 25 = (x − 6)(x + 4)) : Q1 5 · Q2 x ≤ 3 · Q3 (x − 6)(x + 4) · Q4 {−4 ; 6} ·
  Q5 −6 ≤ x − 6 ≤ −3 · Q6 premier négatif, second positif · Q7 {−4} · Q8 produits −24, −42, −12, −21 → −42 ≤ T ≤ −12 (encadrement exact
  sur [0 ; 3] : −25 ≤ T ≤ −21 ; T(0) = −24, T(1) = −25, T(3) = −21) · Q9 {6}.
- 33 : Q2 {−6 ; 3} · Q3 x > 1 · Q4 (x + 4)(x − 1) = 14 · Q5 x ≥ 4/3 · Q6 x = 4.

Clés du fichier : toutes identiques (29 b b b c d b b d d ; 30 b c b b c c ; 31 b a d c a d c a ; 32 c d b b c c c d b ; 33 c d c d b c).
**0 clé fausse.** Chaque distracteur recalculé : tous faux (32 Q8 b : T(1) = −25 < −24 ; c : T(3) = −21 > −24 ; a positif).

## 2. Mes textes, mot pour mot

Conformes à l'audit : 29 Q5 (phrase), Q6 (options + phrase), Q7 (énoncé, options, étiquettes, explication), Q8–Q9 (ligne ajoutée, étiquette b,
phrase k = 7) ; 30 Q5 (étiquette a), Q6 (√15, clé c, explication) ; 31 Q1, Q3 (b + phrase), Q5 (c + étiquette + explication) ; 33 Q2 (étiquette a),
Q4 (a + phrase), Q5 (énoncé, options, étiquettes, explication) ; 33 Q6 (énoncé, options, explication ; options réordonnées, clé c — sans effet,
l'ordre est mélangé à l'affichage).

## 3. Écarts de l'auteur — jugement

| Écart | Verdict |
|---|---|
| 32 Q1 → 3(x + 1) = 7x − 17, clé 5 (a 7/2 transposition : −4x = −14 ✓ ; b 9/2 distribution partielle : 4x = 18 ✓ ; d 20 coefficient non divisé ✓) | OK — n'est plus la même expression que Q2, n'égale aucune racine de T ; « 7x − 17 » absent du publié |
| 32 Q2 étiquettes (a muette, c transposition) + phrase « ومن جمع الخطأين وجد x ≥ 3/2 » | OK (m1 appliqué) |
| 32 Q3–Q9 sur T = (x − 6)(x + 4) | OK. Q3 : c (x − 26)(x + 24) = 1 ± 25 ✓, a/d ✓, plus de miroir avec 08/17 Q3 (aucune occurrence publiée de x² − 2x − 24, (x − 1)² − 25, (x − 6)(x + 4)). Q4 c {4 ; 6} exécute l'étiquette (x + 4 lu 4) ✓. Q5 b « −5 … −2 » = 5 soustrait ✓, d vide (m9, accepté). Q8 : texte et explication justes, seule option vraie ; b exécute exactement `produit-conserve-l-ordre-sans-signe` ✓. Q7 {−4}, Q9 {6} : explications justes (3(−4 + 1) = −9 ≥ −37 ✓ ; T(6) = 0 × 10 ✓) |
| 31 Q8 : explication réécrite sans « 1/n ≥ 1/2 » | OK — elle compare des nombres (« مقلوب n يفوق 1/2 … عندما يكون n أصغر من 2 أو مساويًا له ») ; énoncé à ligne de formule « −6 ≤ n ≤ 6 » : rendu correct |
| 33 Q3 : phrase pour l'option muette x ≥ 1 (« وهو يقبل عرضًا معدومًا ») | OK (m6 appliqué, étiquette retirée) |
| 31 Q1 livre la moitié du calcul de Q2 | OK — Q1 émise avant Q2 (d2 / d2, ordre de fichier) ; Q2 reste à faire (somme + simplification), aucune clé livrée |

## 4. Étiquettes (libellés `origin/main`, option par option)

Toutes celles posées ou déplacées nomment exactement l'erreur exécutée :
29 Q6 c, Q7 a/c, Q8 a, Q9 b ; 30 Q5 a, Q6 b (15 − 3 au lieu de 15 − 9) / d ; 31 Q1 a/c, Q3 b (inverser en gardant l'ordre → 5 ≤ x ≤ 2), Q5 b/c ;
32 Q1 a/b/d, Q2 b/c, Q3 a, Q4 c/d, Q7 a (x ≥ 3 garde 6) / b (« un nombre imposé reste dans son intervalle »), Q8 b, Q9 c/d (crochet mal lu) ;
33 Q2 a/c, Q3 b, Q5 c/d, Q6 a (« une longueur est strictement positive ») / b / d. Options à deux erreurs muettes : 29 Q6 d, Q7 d ; 32 Q2 a, Q9 a ;
33 Q4 a, Q5 a. Aucune étiquette fausse restante.

## 5. Fuites, vote, longueurs, programme, doublons, rendu

- Fuites : aucune explication ne livre la clé d'une question suivante (vérifié question par question ; 33 Q4 « x = 3 » ne touche plus aucune clé ;
  32 Q8 porte sur [0 ; 3], Q9 sur ]−4 ; 6]). Énoncés qui redonnent la clé d'une question émise avant (29 Q3/Q8/Q9, 30 Q2, 32 Q4/Q7/Q9, 33 Q2/Q5/Q6) :
  convention acceptée. Plus aucun renvoi à une autre question (« آخر », « رأينا » supprimés).
- Vote : aucune clé reconstructible (29 Q6, Q7 et 32 Q9 équilibrés ; 32 Q4 → {4 ; 6}, un distracteur). Clé jamais strictement la plus longue (script).
- Programme : aucune inéquation à inconnue au dénominateur (31 Q8 reformulée ; 31 Q3 est un encadrement de l'inverse, savoir du cours 17) ;
  formes canoniques données partout où un trinôme est factorisé.
- Doublons : `dupscan` adapté (publié `origin/main` + intra-lot) — plus aucun recouvrement réel avec le publié (30 Q6 : options 0/1/2/7 communes à
  des items sans rapport ; 04/26 Q3 est un `multi` sur 3x − 3 ≥ 0). Intra-mission : 32 Q7 et Q9 gardent les quatre mêmes options ({−4}, {6},
  {−4 ; 6}, ∅) avec des clés et des conditions différentes (inéquation / crochets) — mineur déjà accepté à l'audit.
- Rendu `dir=rtl` (banc Chromium, `bidi.ts` du moteur) : aucune formule brouillée ; signalements 29 Q2 et 32 Q3 = artefacts de saut de ligne
  (déjà vérifiés à l'audit), 33 Q4 « 14 m² » = moteur (m12). `content:qa` : 0 erreur.

## 6. Bilan

38 questions · **0 clé fausse · 0 majeur restant** · mineurs restants, tous acceptés sans correctif exigé :
- 32 Q7/Q9 mêmes quatre options (clés et savoirs différents) ;
- encadrements vides en distracteurs (31 Q4 b, 31 Q6 c, 31 Q3 b, 32 Q5 d), fidèles à l'erreur étiquetée ;
- 31 Q7 : réunion d'intervalles non enseignée par un cours (hors tranche, cours 04 ou 17) ;
- « 14 m² » / « 24 m² » : rendu moteur, ordre de lecture exact.
**Verdict : livrable.**
