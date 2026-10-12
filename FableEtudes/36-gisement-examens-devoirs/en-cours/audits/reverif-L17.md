# Re-vérification ciblée — lot L17 (maths 9ᵉ, ch. 18-quadrilateres, missions 36–41), après correctifs

## État d'avancement

- [x] Versions identifiées : auditée = `2db6564f~1`, corrigée = `2db6564f` = arbre de `wt-gis` ; registre lu sur `origin/main` `9a3090c9`
- [x] Diff structurel champ par champ (six fichiers) — écrit
- [x] 36 · 37 · 38 · 39 · 40 · 41 — écrits
- [x] Écarts de l'auteur, doublons neufs, 36-Q4 — écrits
- [x] Étiquettes
- [x] Doublons du publié (toutes les missions et quiz de maths)
- [x] Rendu Chromium `dir=rtl` et figures
- [x] Synthèse — écrite (re-vérification terminée)

Second auditeur indépendant (le premier est injoignable), consigne `gisement-auditeur.md`. Rien n'est modifié dans le
dépôt : seul ce rapport est écrit ; aucune écriture git.

## Diff `2db6564f~1` → `2db6564f` (script, appariement par position ; 36 : ancienne Q7 → Q12, anciennes Q8–Q12 → Q7–Q11)

- 36 : Q3 c + clé + expl. ; Q5 d + expl. ; Q8 (ex-Q9) a + expl. ; Q9 (ex-Q10) quatre options + expl. ; Q10 (ex-Q11) options a–d + clé + expl. ;
  Q11 (ex-Q12) expl. ; Q12 (ex-Q7) d2 → d3, c muette. Q7 (ex-Q8) inchangée.
- 37 : Q2 a (3 → 9) ; Q4 a (4 → 16) ; Q7 quatre options ; Q8 c (4 → 8) ; Q11 énoncé (rappel des trois points) ; expl. associées.
- 38 : Q4 expl. ; Q5 d ; Q7 a muette + expl. ; Q9 b (texte de l'auteur) + expl.
- 39 : Q2 c, d ; Q5 énoncé ; Q6 b, c ; Q8 quatre options + expl. ; Q9 a étiquetée.
- 40 : Q1 figure (graduations) ; Q4 d étiquette ; Q10 d.
- 41 : Q1 b, d ; Q2 d ; Q4 c/d étiquettes ; Q5 b/c étiquettes ; Q7 a, b, c.
- En-têtes, types, ordre (hors 36), autres champs : inchangés.


## Méthode

- Re-résolution à l'aveugle (script qui masque clés, étiquettes et explications) de chaque question retouchée et de ses voisines ;
  coordonnées refaites : 36 (triangle ABD quelconque tiré au hasard pour Q9–Q10 : les seuls parallélogrammes du jeu sont OBEC,
  OECA, OEDC), 38 (A(0,0), D(6 ; 6√11/5), E(216/25 ; 0), F(216/25 ; 6√11/5) : J, K, O sur y = 3√11/5).
- Longueurs mesurées par script sur toutes les questions à choix unique des six fichiers : **aucune clé strictement la plus longue**.
- Libellés lus sur `origin/main:content/misconceptions.json` (`9a3090c9`) : toutes les étiquettes des six fichiers y existent.
- Doublons : `dupscan.py` de l'auteur relancé (2 291 questions publiées de maths, missions + quiz, `origin/main`) + lecture de chaque
  paire ; comparaison intra-lot (63 questions) des jeux d'options.
- Rendu : banc `bench-rtl.mjs` (`BIDI=ancien` = `bidi.ts` de `/home/user/eng-gisement`, identique à `origin/main` du moteur
  `7cd50eb`), Chromium `dir=rtl`, largeurs 400 et 340, sur toutes les questions retouchées : **aucune formule brouillée** ;
  captures relues (36-Q9, 40-Q10 d, 38-Q9 proposé).

## 36 (2013, ordre NOUVEAU : rampe 1,2,2,2,2,2,3,3,3,3,3,3 — émission = ordre du fichier)

| Q | ma réponse (aveugle) | clé | verdict | motif |
|---|---|---|---|---|
| 3 multi | {a,b,d} | {a,b,d} | OK | c « BE = 2 × ED » faux (E milieu) ; 3 vrais / 6 ; b/c ne sont plus équivalents |
| 5 | b (3√5) | b | OK | d 5√3 = facteur sorti inversé : `racine-extraction-facteur-inversee` exact ; vote chiffre par chiffre → 3√3 (faux) |
| 7 (ex-Q8) | c | c | OK | inchangée |
| 8 (ex-Q9) | d (2√5) | d | OK | a 30 = (2/3) × 45 (racine oubliée puis 2/3) : `pythagore-racine-oubliee` exact |
| 9 (ex-Q10) | c | c | OK | vrai 2×2 {(OE)∥(DC) ; (EC)∥(AB)} × {OE = DC ; OC = ED}, prémisses toutes vraies (triangle quelconque), 110/110/110/110 signes ; d muette |
| 10 (ex-Q11) multi | {b,d} | {b,d} | OK | OBEC, OECA ; OBDC, ADEO, ABEC trapèzes ; OEBC croisé (vérifié sur trois triangles aléatoires) |
| 11 (ex-Q12) | d | d | OK | explication sans EO = 3√2 ✓ |
| 12 (ex-Q7) | a | a | OK | d3, en dernier ; c muette ✓ |

- Fuites (ordre nouveau) : la prémisse de Q12 (« (EG) يحمل الموسّط الصادر من E ») est la clé de Q11, émise AVANT : convention.
  Q11 pose « OECA متوازي أضلاع » (clé d de Q10), émise APRÈS : rien n'est livré dans la quête ; dans le donjon, prémisse redonnée
  (convention, mineur). Aucune explication de Q1–Q11 ne livre la clé d'une suivante (Q4 dit (OC) ∥ (BD), prémisse commune à
  b, c de Q7 : pas une clé ; Q9 ne nomme ni OBEC ni OECA).
- **36-Q4 : ne pas changer.** Ses options {3, 3√2, 6, 6√2} sont celles de 20/03-revision Q4 (clé 3√2, demi-diagonale d'un carré),
  et elle partage {3, 3√2, 6} et la clé 6 avec 09/40 Q1 (diamètre = 2 × rayon) : deux notions différentes de la droite des milieux,
  pas un doublon. La lecture de BD = AB sur la figure reste le mineur accepté par l'audit.

**Verdict 36 : 0 clé fausse ; les trois majeurs (Q7→Q12, Q10, Q11) sont levés ; rien à reprendre.**

## 37 (2016)

| Q | ma réponse | clé | verdict | motif |
|---|---|---|---|---|
| 2 | b (3√2) | b | OK | a 9 = 18/2 `racine-confondue-avec-moitie` exact ; d 18 racine oubliée ; c 6√2 hypoténuse |
| 4 | b (4√2) | b | OK | a 16 = 32/2 (même étiquette, exacte) ; d 32 ; c 8√2 |
| 7 | d | d | OK | vrai 2×2 {(EF)∥(DG) ; (EF)⊥(AC)} × {EF = DG ; EF = FO} ; EF = FO = DG = 2, (DG) ⊥ (AC) vérifiés ; c muette ; d 132 < b 146 |
| 8 | b (2√2) | b | OK | c 8 = AC (`segment-mal-choisi`) |
| 11 | d | d | OK | le rappel « نذكّر … » glose a, b, d à égalité : neutre ; G sur deux hauteurs ⇒ centre ortho. |

- Q2 et Q4 ont désormais exactement le même gabarit (x²/2, clé, ×√2 de l'hypoténuse, x²) : mineur déjà accepté par l'audit
  (officiel 1b et 2b), aggravé mais sans effet sur une clé. Rien à reprendre.

**Verdict 37 : 0 clé fausse ; majeurs Q4, Q7, Q11 levés.**

## 38 (2018)

| Q | ma réponse | clé | verdict | motif |
|---|---|---|---|---|
| 4 (expl.) | a | a | OK | phrase des 360° ajoutée dans l'explication seulement ✓ |
| 5 | d | d | OK | d (texte de l'auteur) finit comme les trois autres ; a/d symétriques (DHE ↔ BHF) : pas de vote |
| 7 | d | d | OK | a muette ✓ ; réciproque ajoutée à l'explication ✓ |
| 9 | a | a | **MAJEUR (neuf)** | **la clé a = b ∪ d** : voir ci-dessous |

- **MAJEUR 38-Q9 — vote terme à terme introduit par la réécriture de b.** La nouvelle b ne garde que « (JO) ∥ (AE) في المثلّث ADE »
  et d que « (JK) ∥ (DF) في المثلّث ADF », chacune suivie de « وهذا يكفي » : la clé a est exactement leur réunion (+ la donnée
  (DF) ∥ (AE)). L'élève la choisit sans géométrie (défaut que l'audit a classé majeur en 36-Q10, 37-Q7, 41-Q7). En outre les
  deux « وهذا يكفي » recréent le gabarit de 37-Q9 b que l'audit demandait de différencier.
  Correctif (plan 2×2 — 1er parallélisme {(JK) ∥ (DF) dans ADF juste ; (KO) ∥ (AE) dans AFE faux} × 2nd {(JO) ∥ (AE) dans ADE juste ;
  (JO) ∥ (DF) dans ADF faux}, la donnée (DF) ∥ (AE) dans a et d) ; a et c inchangées :
  - b : « (KO) ∥ (AE) في المثلّث AFE، و (JO) ∥ (AE) في المثلّث ADE، فالمستقيمان (KO) و (JO) منطبقان » — `math.geo.segment-mal-choisi`
    (O n'est pas sur un côté de AFE : même erreur que c) ;
  - d : « (KO) ∥ (AE) في المثلّث AFE، و (JO) ∥ (DF) في المثلّث ADF، و (DF) ∥ (AE)، فالمستقيمان (KO) و (JO) منطبقان » — muette
    (deux erreurs) ;
  - explication : remplacer la phrase « الخطأ الشائع: … دون الآخر. » par « الخطأ الشائع: تطبيق خاصيّة المنتصفين في مثلّث لا يحمل
    المنتصفين معًا: النقطة O ليست على ضلع من المثلّث ADF، ولا على ضلع من المثلّث AFE. »
  Vérifié : toutes les affirmations de parallélisme sont VRAIES dans la figure et dans tout quadrilatère ADFE à (DF) ∥ (AE)
  (J, K, O à mi-hauteur), seules les justifications de b, c, d sont fausses ; longueurs a 104 · b 89 · c 109 · d 104 (clé non
  strictement la plus longue) ; chaque fait dans deux options ; rendu Chromium `dir=rtl` 400 et 340 px : 0 inversion ; plus aucun
  « وهذا يكفي » ni règle fausse : le gabarit diffère de 37-Q9.

**Verdict 38 : 0 clé fausse ; 1 majeur neuf (Q9).**

## 39 (2019 ex.3)

| Q | ma réponse | clé | verdict | motif |
|---|---|---|---|---|
| 2 | b (5) | b | OK | {√7, 5, 25/2, 12} : 25/2 moitié (étiquette exacte), 12 = 4 × 3 muette |
| 5 multi | {b,c,f} | {b,c,f} | OK | « مخالفة لـ B و C » rend le rectangle non dégénéré ✓ |
| 6 | d | d | OK | vrai 2×2 {HM, HK} × {², sans} ; a `segment-mal-choisi`, c `racine-et-carre-confondus` exacts ; 12/11/11/12 |
| 8 | a | a | OK | b `pythagore-sans-carres`, c `hypotenuse-mal-choisie` exactes, d muette ; plus de forme de E à reconnaître |
| 9 | c | c | OK | a `ordre-inverse-a-tort` exact (ajout de (12/5)² aux deux membres) |

**Verdict 39 : 0 clé fausse ; majeurs Q2, Q6, Q8 levés.**

## 40 (2019 ex.4)

| Q | ma réponse | clé | verdict | motif |
|---|---|---|---|---|
| 1 (figure) | b | b | OK | graduations −4 et 2 seules ; B, C, O, I, J recalculés (unité 37,81 px) exacts |
| 4 | a | a | OK | d `racine-et-carre-confondus` exact |
| 10 | d | d | OK | d 104 < b 116 ; KH = 1, HE = 2√2, KE² = 9 vérifiés ; rendu de « وHE = 2√2 » : ordre juste |

**Verdict 40 : 0 clé fausse ; majeur Q10 levé.**

## 41 (2020)

| Q | ma réponse | clé | verdict | motif |
|---|---|---|---|---|
| 1 | c (2√5) | c | OK | {2√3, 10, 2√5, √6} ; √6 = √(4 + 2) `pythagore-sans-carres` exact |
| 2 | b (4√5) | b | OK | d 40 = 80/2 étiquette exacte |
| 4 | a | a | OK | c `thales-rapport-inverse` (HC/HA pris égal à 4) ; d muette ✓ |
| 5 | d | d | **mineur (explication)** | voir ci-dessous |
| 7 | d | d | OK | 2×2 de l'audit ; prémisses vraies ; a muette ; 116/116/111/111 |

- **MINEUR 41-Q5 — explication fausse sur c.** Elle dit « أو قلب النسبة فنجد HB = 4 × 2√5 = 8√5 » : inverser la proportion
  (HB/HI = 1/4) donne HB = BI/5 = 2√5/5 (option b), jamais 8√5 ; 8√5 = 4 × BI (la longueur entière multipliée par 4), c'est
  pourquoi c est devenue muette. Correctif : remplacer ce membre par « أو ضرب طول [BI] كلّه في 4 فنجد HB = 4 × 2√5 = 8√5 »
  (même tournure que 41-Q4 pour 16√5 ; vérifié 4 × 2√5 = 8√5 ; rendu sans inversion).

**Verdict 41 : 0 clé fausse ; majeurs Q1, Q7 levés ; 1 mineur (Q5 explication).**

## Écarts de l'auteur

| écart | jugement | motif |
|---|---|---|
| 36-Q11 (→ Q10) multi à deux clés {OBEC, OECA} au lieu de {OBEC} | **accepté** | un `multi` exige ≥ 2 bonnes réponses (schéma) ; OEDC retiré (posé en Q6, Q9) ; OECA n'est posé que par Q11, émise après (donjon : prémisse redonnée, convention) ; 2 vrais / 6 non déductible |
| 38-Q5 d finit par « إذن A و H و F على استقامة واحدة » | **accepté** | le texte de l'audit faisait de d la seule option sans la conclusion commune (marqueur de forme) ; d 123 < a 126 |
| 38-Q9 b « … وهذا يكفي » dans ADE | **à reprendre (majeur)** | l'objection de l'auteur au texte de l'audit est juste (si (KO) ∥ (AD) et J ∈ (AD), J ∉ (KO) : option qui se réfute d'elle-même), mais son texte rend la clé = b ∪ d. Texte : section 38 |
| 39-Q8 explication « وبالنشر نجد HK² = a² − (32/5)a + 16 » | **accepté** | E n'est pas défini dans l'énoncé de Q8 (autonomie) ; aucune clé suivante livrée (Q9 et Q10 donnent la forme canonique en prémisse) |
| Doublons : 39-Q2 {√7, 5, 25/2, 12}, 41-Q1 {2√3, 10, 2√5, √6}, 37-Q4 {16, 4√2, 8√2, 32} | **acceptés** | vérifié : les textes de l'audit partageaient 3 options avec 09/40 Q2 (et même clé 5, mêmes données 4 et 3 : vrai doublon), 20/19 Q4, 09/37 Q6 ; les nouveaux en partagent ≤ 2 (37-Q4 : 3 avec 20/09-devoir-pyramide Q1 {4√2, 8, 8√2, 16}, clé 8 ≠ 4√2, autre problème : pas un doublon) |

## Doublons neufs trouvés par l'auteur

- **37-Q2** (3 → 9) : l'ancien jeu {3, 3√2, 6√2, 18} partageait 3 options et la clé 3√2 avec 20/03-revision Q4 (même calcul 6/√2) :
  vrai quasi-doublon, bien vu ; le nouveau en partage 2 → **accepté**.
- **37-Q8** (4 → 8) : accepté sur le fond (09/37 Q6 et 20/10 Q4 ne partagent plus 3 options). ⚠️ Au critère même de l'auteur
  (≥ 3 options communes) le nouveau jeu {2, 2√2, 8, 4√2} touche encore 04/16-devoir Q2 {2, 4√2, 2√2, 7√2} et 12/20-examen-2026 Q1
  {2, 2√2, 3√2, 8}, même clé 2√2 — mais ce sont une équation et une puissance, sans rapport avec la droite des milieux : **pas un
  doublon**, rien à faire (le journal « scan propre » est inexact sur ce point).
- **41-Q2** (80 → 40) : {4√3, 4√5, 12, 40} ne partage plus que 4√5 et 12 avec 09/35 Q3 (mêmes données 8 et 4, même clé 4√5, même
  piège 12 ; habillage différent : diagonale du rectangle contre hypoténuse). Sous le seuil fixé par l'audit (≤ 2 options) et venu
  de l'officiel 2020 : **accepté** (résiduel signalé, mineur).

## Étiquettes posées, déplacées ou retirées (libellés de `origin/main`)

| option | étiquette | verdict |
|---|---|---|
| 36-Q5 d « 5√3 » | `racine-extraction-facteur-inversee` | exact (√45 = 3√5) |
| 36-Q8 a « 30 » | `pythagore-racine-oubliee` | exact (AE² = 45 pris pour AE, puis 2/3) |
| 36-Q9 a, b | `condition-suffisante-supposee` | exact ; d muette (deux erreurs) ✓ |
| 36-Q12 c, 38-Q7 a, 41-Q4 d, 41-Q5 c | retirées | justes (transfert de centre de gravité ; deux erreurs) |
| 37-Q2 a « 9 », 37-Q4 a « 16 », 39-Q2 c « 25/2 », 41-Q1 b « 10 », 41-Q2 d « 40 » | `racine-confondue-avec-moitie` | exact (moitié de 18, 32, 25, 20, 80) |
| 37-Q7 a | `segment-mal-choisi` | exact (FO au lieu du côté opposé DG) ; b `condition-suffisante-supposee` exact ; c muette ✓ |
| 37-Q8 c « 8 » | `segment-mal-choisi` | exact (AC pris pour NF) |
| 38-Q9 b (actuelle) | `condition-suffisante-supposee` | exact, mais l'option est à reprendre (b proposée : `segment-mal-choisi`, d muette) |
| 39-Q6 a / c | `segment-mal-choisi` / `racine-et-carre-confondus` | exacts ; b muette ✓ |
| 39-Q8 b / c | `pythagore-sans-carres` / `hypotenuse-mal-choisie` | exacts ; d muette ✓ |
| 39-Q9 a | `ordre-inverse-a-tort` | exact |
| 40-Q4 d | `racine-et-carre-confondus` | exact |
| 41-Q1 d « √6 » | `pythagore-sans-carres` | exact (√(4 + 2)) |
| 41-Q4 c | `thales-rapport-inverse` | exact |
| 41-Q5 b | `reponse-a-l-autre-inconnue` | exact (HI au lieu de HB) |
| 41-Q7 b, c | `condition-suffisante-supposee` | exacts ; a muette ✓ |

Aucun id neuf ; les 863 ids d'`origin/main` couvrent toutes les étiquettes des six fichiers. Remarque (mineur, sans correctif
exigé) : `racine-confondue-avec-moitie` porte désormais 6 options du lot (37-Q2, Q4 ; 39-Q2 ; 40-Q4 ; 41-Q1, Q2) — la « moitié » est
devenue le remplissage standard des questions de Pythagore du lot, jamais juste.

## Doublons du publié (2 291 questions de maths d'`origin/main`, missions + quiz)

Questions réécrites : 36-Q3, Q5, Q8, Q9, Q10 ; 37-Q2, Q4, Q7, Q8, Q11 ; 38-Q5, Q9 ; 39-Q2, Q6, Q8, Q9 ; 40-Q10 ; 41-Q1, Q2, Q7 :
aucune ne partage 3 options **et** sa clé avec une question publiée du même calcul ; 36-Q5 et 36-Q8 ne partagent plus que 2 options
avec 18/32-examen-2008 Q2, Q7. Paires résiduelles lues et jugées ci-dessus (37-Q4, 37-Q8, 41-Q2, 36-Q4). Intra-lot : aucun jeu de
plus de 2 options communes ; gabarits répétés 37-Q2/Q4 et 41-Q1/Q2 (officiel), acceptés.

## Rendu et figures

- Toutes les questions retouchées rendues (énoncés, options, explications) dans Chromium `dir=rtl` à 400 px : 0 formule brouillée ;
  formules coupées en fin de ligne (« و OC / = ED ») lues dans l'ordre — comportement du moteur, pas un défaut.
- Seule figure modifiée : 40-Q1 (graduations −4 et 2 seules, flèches d'axes, I et J placés à l'unité 37,81 px) : exacte.
- Textes de remplacement de ce rapport (38-Q9 b, d, explication ; 41-Q5 explication) rendus à 400 et 340 px : 0 inversion.

## Synthèse

- **Clés fausses : 0** (toutes les questions retouchées et leurs voisines re-résolues à l'aveugle ; 36-Q10 vérifiée sur triangles aléatoires).
- **Majeurs de l'audit : 14 / 14 levés.**
- **Majeur restant (neuf) : 38-Q9** — clé = réunion des distracteurs b et d (réécriture de b par l'auteur). Texte exact ci-dessus
  (b, d, explication).
- **Mineur restant : 41-Q5 explication** (« قلب النسبة » → « ضرب طول [BI] كلّه في 4 »). Résiduels acceptés : 37-Q2/Q4 et 41-Q1/Q2
  gabarits jumeaux, 41-Q2 ≈ 09/35 Q3 (2 options), sur-emploi de `racine-confondue-avec-moitie`, 36-Q4 (figure).
- Écarts de l'auteur : 4 acceptés (36-Q11, 38-Q5 d, 39-Q8, trio de doublons), 1 à reprendre (38-Q9 b). Doublons neufs : 3 acceptés.
  36-Q4 : ne pas changer.
- **Verdict : livrable après la reprise de 38-Q9 (et, de préférence, de l'explication de 41-Q5).** Après ces deux retouches, aucune
  nouvelle re-vérification n'est nécessaire au-delà d'un contrôle verbatim des textes et des gates.
