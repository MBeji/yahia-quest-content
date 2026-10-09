# Re-vérification ciblée — tranche SVT-L01 (après le tour de corrections de l'auteur)

Statut : EN COURS — mis à jour après chaque fichier.

Consigne : même méthode que l'audit (résolution à l'aveugle sur ce qui change, rien modifié dans
le dépôt) ; priorité aux défauts INTRODUITS par les correctifs.

## Avancement

- [x] 02/07
- [x] 02/08
- [x] 05/07
- [x] 05/08
- [ ] 07/07 (annoncée inchangée — à confirmer)
- [ ] 07/08
- [ ] Étiquettes (29) et `bio.dig.eau-sans-enzyme`
- [ ] Gates

Méthode : instantané des six fichiers (2026-10-09 13:29) ; diff question par question contre
l'instantané de l'audit (champ par champ : énoncé, SVG, type, difficulté, options, étiquettes,
clé, explication) — le périmètre réel est celui annoncé, 07/07 inchangée (même octet, même
horodatage). Chaque question touchée est ré-affichée SANS clé ni explication et re-résolue avant
lecture de la clé. Figures rendues comme dans l'app depuis arena#1154 : page `dir="rtl"`,
enveloppe `dir="ltr"`, largeur utile 232 px (w-64 moins p-3), échelle ×3 pour l'inspection.

---

## 02/07 — nerf sciatique (2024 ex.5)

| item corrigé | ma réponse (aveugle) | clé | verdict |
|---|---|---|---|
| Q2 a (grammaire) | d | d | OK — « فأصدر أمرًا » : sujet = النّخاع |
| Q4 a (réécrite par l'auteur), d, explication | c | c | OK |
| Q6 (mcq) | a | a | OK, une réserve mineure (ci-dessous) |
| Figures Q1–Q4 (pattes) | — | — | OK |

- **Q4 a** : la réécriture de l'auteur est la bonne. Mon texte de l'audit (« الألياف الحسّيّة … مقطوعة،
  فلا تنقل الأمر الحركيّ … ») était VRAI à la lettre (les fibres sensitives sont coupées, et elles ne
  portent jamais l'ordre moteur) : défaut de mon correctif, bien vu. La nouvelle option affirme
  « هي التي تنقل الأمر الحركيّ » : fausse, et c'est exactement l'erreur de
  `bio.nerv.sensitif-et-moteur-confondus`. d (« أفقد عضلات السّاق … قدرتها على التّقلّص ») : fausse
  (cours 02 : la stimulation du bout lié à la jambe fait contracter le muscle), ne nie aucune
  prémisse. Plus aucune option contredite par « انثنت كلّ الأطراف ما عدا السّاق اليمنى ». Longueurs :
  clé c 76, a 95, d 72, b 71. L'explication réfute les trois distracteurs, sans lettre d'option.
- **Q6** : le doublon avec Q5 est levé (plus aucune option ne recopie la clé de Q5) ; clé a = 63 car.,
  c = 67 ; a et c (deux formes « deux sortes de fibres ») face à b et d (deux formes « فقط ») : la forme
  ne départage plus. Explication exacte.
- **Figures** (rendues à 232 px et ×3) : pattes postérieures allongées vers le bas et pattes
  antérieures relevées comme au Doc 6 ; coupure sur la cuisse droite du dessin (lacune entre deux
  bouts marqués) ; C sur le bout proximal (Q3, Q4), P sur le bout distal (Q2), aiguille au pied droit
  (Q1). viewBox 0 0 300 300, tout dedans, textes C/P en `middle`, arabe dans `<title>` seulement,
  aucun élément interdit, aucune clé marquée. La jambe « ممدودة » de Q4 est désormais celle du dessin.

**[MINEUR, introduit par mon correctif] Q6 — « نستنتج » et une clé qui va au-delà des données.**
Les deux résultats montrent qu'il y a des fibres motrices et des fibres sensitives ; ils ne montrent
pas que CHAQUE bout contient les deux — c'est l'anatomie (cours 01 : l'axone court tout le long du
nerf) qui le dit. L'option c (le découpage par bouts) est donc compatible avec les deux résultats,
fausse seulement par les acquis. Correctif : fin de l'énoncé « ماذا نستنتج عن ألياف عصب النّسا؟ » →
« ماذا نستنتج، بالاعتماد على هاتين النّتيجتين وعلى مكتسباتك، عن ألياف عصب النّسا؟ » (reprend le
« بالاعتماد على مكتسباتك » du sujet officiel ; ne nie aucune prémisse, ne désigne aucune option).

Rendu : champs modifiés sans chiffre ni lettre latine (sauf C/P des énoncés, non isolés, ordre juste).

---

## 02/08 — hypothèses, stimulations, coupes de moelle (2021 ex.4)

Ex-Q3 supprimée ; Q3, Q4, Q5 = ex-Q4, Q5, Q6. Plus aucun doublon avec 02/07 Q2.

| item corrigé | ma réponse (aveugle) | clé | verdict |
|---|---|---|---|
| Q2 e + explication | {a,c,d,f} | {a,c,d,f} | OK |
| Q3 b étiquetée `cause-sans-temoin` | (clé inchangée a) | a | OK — libellé exact |
| Q4 figure (fibres de Y, X à droite) | {a,d,f} | {a,d,f} | OK, un défaut cosmétique introduit |
| Q5 énoncé, a, c, étiquettes, explication | b | b | OK |
| En-tête d4, rampe 2,2,3,3,3 | — | — | à replier en boss d3 (mineur) |

- **Q2** : e « امتنعت الضّفدعة (ب) بإرادتها عن ثني ساقها » est fausse (un réflexe est involontaire, cours
  01/02), plausible, ne nie aucune prémisse ; l'explication la réfute (« وأمّا الإرادة فلا دخل لها في
  فعل انعكاسيّ »). Le compte de bonnes réponses (4 sur 6) ne se déduit pas de la forme.
- **Q5** : la figure est désormais nécessaire. Les trois hypothèses qu'aucune expérience n'a écartées
  (récepteurs, fibres sensitives, centre) sont proposées, et seule la comparaison X/Y désigne la moelle.
  a et c ne nient aucune prémisse et ne sont pas établies par les données (« الأرجح بالاعتماد على مقارنة
  الرّسمين X وY ») ; étiquette `cause-sans-temoin` exacte sur les deux (accuser un élément qu'aucun témoin
  ne désigne, alors que le témoin X désigne la moelle). Clé b = 74 car., a 74, c 80, d 69. Explication
  juste, sans les comptes de Q4. Rendu Chromium de « الرّسمين X وY، » : ordre juste.
- **Q4, figure** (rendue à 232 px et ×3, comparée au PDF C05 p. 4) : X passe à droite et Y à gauche
  comme au PDF ; zone 1 de Y garnie d'une vingtaine de fibres ondulées fines (plus que X, comme au PDF),
  une seule cellule étoilée plus petite ; X : cinq grandes cellules ; zone 2 : X serrée, Y clairsemée
  avec traits et points. Clé {a, d, f} inchangée et toujours vraie ; explication cohérente avec la
  nouvelle figure. viewBox 0 0 340 214, textes X/Y/1/2 en `middle`, aucun élément interdit.

**[MINEUR, introduit] Q4/Q5 — deux fibres de Y sortent du cadre de la coupe.** Dans le groupe
`translate(14,28)`, les tracés « M34.0 12.0 C40.4 7.6 36.0 -1.8 42.5 -6.1 » et « M80.0 14.0 C87.1 9.6
83.9 -0.7 91.0 -5.1 » montent jusqu'à y = −6,1 et −5,1 : ils dépassent du bord supérieur du cadre
(rendu ×3 : deux traits au-dessus de la bordure, à côté de la lettre Y). Correctif (rendu vérifié :
tout rentre dans le cadre, rien ne touche la lettre) : les remplacer, dans le SVG de Q4 ET de Q5, par
« M34.0 20.0 C40.4 15.6 36.0 6.2 42.5 1.9 » et « M80.0 22.0 C87.1 17.6 83.9 7.3 91.0 2.9 ».

**[MINEUR] En-tête d4 (⭐⭐⭐⭐, challenge 300/60) avec 2 questions d2 sur 5 : à replier en boss d3.** Après la
suppression de l'ex-Q3, la mission a moins de d3 (3/5) que 02/07, de la même famille et classée boss
(4/6) ; les défis publiés du chapitre sont tout en d3 ; l'exercice officiel pèse 4,5 points, entre le
3 points de 02/07 (boss) et le 8 points de 05/08 (défi). Correctif : `difficulty: 3`, `mode: "boss"`,
`xpReward: 120`, `rewardCoins: 30`, et dans le titre « ⭐⭐⭐⭐ » → « ⭐⭐⭐ ». Rampe 2,2,3,3,3 compatible.

Fuite (donjon, préexistante, inhérente) : la clé de Q5 (« رغم سلامة النّاقل الحركيّ والعضلة ») et son
explication donnent, par complément, la clé de Q3 si Q5 sort avant ; ordre quête correct. Aucun
correctif exigé.

---

## 05/07 — appareil digestif, sucs, villosité (2021 ex.2)

| item corrigé | ma réponse (aveugle) | clé | verdict |
|---|---|---|---|
| Q4 d + pièges de l'explication | c | c | OK |
| Q5 c + explication | {a,d,e} | {a,d,e} | OK |

- **Q4** : vrai plan 2×2 — « الخميلة » (a, d) / « الخملة المعويّة » (b, c), « امتصاص » (a, c) /
  « استحلاب » (b, d) : le vote est nul ; d, à double erreur, est muette. Clé 42 car., b 46.
  L'explication nomme les deux confusions ; « وهي أصغر منها بكثير » renvoie bien à la microvillosité.
- **Q5** : c « كلّ المغذّيات تعبرها إلى الدّم، ولا وعاء لمفاويّ فيها » est fausse (chylifère jaune axial
  sur la figure, lipides surtout vers la lymphe — cours 05), plausible, ne contredit plus « مجهريّة ».
  La phrase contraire au sujet officiel a disparu ; l'explication réfute b, c et f
  (« نواتج نهائيّة للهضم … ولا تُفكَّك أثناء عبورها » : juste au niveau du cours).
- Figure de la villosité inchangée (octet pour octet hors `<title>`). Aucun chiffre ni lettre latine
  dans les champs modifiés.

Aucun défaut introduit.

---

## 05/08 — huile d'olive, maltose, devenir du glucose (2022 ex.4)

| item corrigé | ma réponse (aveugle) | clé | verdict |
|---|---|---|---|
| Q1 en lignes, d, clé, explication | {a,c,d,f} | {a,c,d,f} | OK |
| Q2 explication | d | d | OK |
| Q4 énoncé complété, a, d, explication | c | c | OK |
| Q5 a, c étiquetées `specificite-enzyme-ignoree` | b | b | OK — libellé exact |
| Q6 f, explication, histogramme | {a,c,e,f} | {a,c,e,f} | OK — fuite vers Q7 levée |
| Q7 en lignes, b étiquetée, explication | c | c | étiquette de b à retirer (ci-dessous) |

- **Q1** : 4 justes sur 6. a/b et e/f restent des paires contraires, mais c et d se jugent chacune
  sur les données : le compte ne se lit plus sur la forme. d est vraie (aucun des deux résultats ne
  porte de maltose ; PDF C04 p. 3 idem). La phrase ajoutée à l'explication est juste.
- **Q2** : la nouvelle phrase (« … يفكّك النّشا إلى سكّر الشّعير، ولا يفكّك سكّر الشّعير ») ne contredit
  plus Q3, Q8, Q9 ; juste au niveau du cours 05.
- **Q4** : « محلول من سكّر الشّعير وزيت الزّيتون والعصارتين » reprend mot pour mot le sujet officiel
  (C04 p. 3 : « محلولا من سكّر الشّعير وزيت الزّيتون والعصارة المعثكليّة والعصارة المعويّة »). Il donne
  enfin à l'explication le « المحلول » auquel elle renvoie : mon correctif parlait d'une solution que
  l'ancien énoncé ne nommait pas (défaut de mon texte, réparé par l'auteur). a et d ne nient plus
  aucune prémisse et sont fausses par les données : le tube 1 est déjà aqueux et garde de l'huile ;
  il a digéré tout le maltose sans (س). Clé c 60 car., a 60, d 66, b 56 ; aucun vote.
- **Q6** : f « مجموع النّسبتين يساوي 100 في كلّ مرّة » est vraie ; ni f ni l'explication ne disent plus
  où va le glucose. Q6 fait l'analyse (somme constante) et Q7 garde la déduction (passage
  intestin → veine = absorption), comme 3a/3b du sujet. Histogramme rendu à 232 px (page rtl,
  enveloppe ltr) : graduations à gauche de l'axe, sans chevauchement ; valeurs et hauteurs exactes ;
  aucune clé marquée ; viewBox 0 0 320 240, ancres `middle` seulement, rien d'interdit.
- **Rendu** des lignes neuves (Q1, Q7) et de l'explication de Q6 dans Chromium `dir=rtl`, positions
  des glyphes mesurées : de droite à gauche, 80, 50, 10 / 20, 50, 90 / « 80 + 20 = 100 … », soit l'ordre
  source ; « (س) » et « الأنبوب 1: … + … » sont justes. `splitMathRuns` laisse ces lignes en prose.

**[MINEUR, introduit par mon correctif] Q7 b — étiquette `bio.dig.absorption-dans-la-digestion` à
retirer.** b (« يُفكَّك الجليكوز … إلى مغذّيات أبسط منه: ظاهرة الهضم ») exécute « le glucose se
digère encore », en ignorant la montée dans la veine. Le libellé (« Tu ranges l'absorption dans la
digestion ») ne nomme pas cette erreur. Ses usages publiés sont l'inverse : 05-tadrib Q6 d et
quiz Q2 c appellent « digestion » un passage dans le sang. Deux chemins mènent en outre à b : tout
ce qui se passe dans l'intestin serait digestion, ou le glucose serait encore décomposable. C'est
le cas d'ambiguïté de `content-schema.md` : l'option reste muette. `unites-structurales-confondues`
ne convient pas non plus (confusion entre catégories). Correctif : supprimer le `misconceptionTag`
de Q7 b ; l'explication, qui nomme l'erreur, reste telle quelle.

**[MINEUR, préexistant, manqué à l'audit] Q7 — marqueur de forme.** Les trois distracteurs finissent
par « ظاهرة … » (الإفراز، الهضم، التّخزين) ; seule la clé finit par « الامتصاص المعويّ ». Correctif :
c → « يمرّ الجليكوز من المعي الدّقيق إلى دم الوريد: ظاهرة الامتصاص ». Vérifié : 60 car., b 67, a et
d 59 ; aucune prémisse niée, aucune fuite ; l'explication (« وهذه الظّاهرة هي الامتصاص المعويّ »)
reste juste ; ni chiffre ni latin.

`bio.dig.eau-sans-enzyme` : **absente de l'arbre** — voir « Étiquettes ».
