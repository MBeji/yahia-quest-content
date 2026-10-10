# Re-vérification ciblée — tranche SVT-L01 (après le tour de corrections de l'auteur)

Statut : TERMINÉ (2026-10-09) — 35 questions, 0 clé fausse, 0 critique, 0 majeur, 7 mineurs (bilan en fin de rapport).

Consigne : même méthode que l'audit (résolution à l'aveugle sur ce qui change, rien modifié dans
le dépôt) ; priorité aux défauts INTRODUITS par les correctifs.

## Avancement

- [x] 02/07
- [x] 02/08
- [x] 05/07
- [x] 05/08
- [x] 07/07 (inchangée — confirmé)
- [x] 07/08
- [x] Étiquettes (29) et `bio.dig.eau-sans-enzyme`
- [x] Gates

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

Fuites en avant, ordre de quête : l'explication réécrite de Q4 (« وهي تنقل السّيالة نحو النّخاع لا
منه ») redit, après Q1 à Q3, les deux sens que Q5 synthétise. C'est la classe « Q1–Q3 → Q5 » déjà jugée
inhérente à l'audit. L'explication de Q5 (« ينقل في الاتّجاهين ») écarte b et d de Q6 ; reste à
départager a et c (« chaque bout », par les acquis — voir la réserve ci-dessus). Partiel et inhérent
à l'enchaînement officiel : pas de correctif.

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
- Fuite partielle, ordre de quête : l'explication de Q4, inchangée sur ce point (« إلى الدّم
  واللّمف »), écarte d'avance la nouvelle c de Q5. C'est une option sur six, que la figure de Q5
  réfute aussi (chylifère axial) ; la clé n'est pas livrée. Acceptée, sans correctif.

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
digestion ») ne nomme pas cette erreur. Ses usages publiés portent sur autre chose : 05-tadrib Q6 d
et quiz Q2 c appellent « digestion » un passage dans le sang, alors que b décrit un découpage, pas un
passage. Deux chemins mènent en outre à b : tout
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

---

## 07/07 — digestion des protides, milieu intérieur, nerfs crâniens (2024 ex.1)

Inchangée : même empreinte md5 que l'instantané de l'audit (`f3006181…`), même horodatage (10-02 07:28).
Verdicts de l'audit maintenus ; ses quatre étiquettes sont revues plus bas.

---

## 07/08 — cœur, phases du cycle, circulation (2020 ex.3)

| item corrigé | ma réponse (aveugle) | clé | verdict |
|---|---|---|---|
| Q1 figure A+B numérotée | 1→r4, 2→r1, 3→r2, 4→r3 | idem | OK |
| Q3 figure A | d | d | OK |
| Q5 figures A+B, explication | a | a | OK |
| Cœurs redessinés (A et B) | — | — | OK pour la science des phases ; un défaut de paroi (ci-dessous) |

- **Comparaison au PDF** C06 p. 2 (recadrages des phases à 400 dpi). **B** = phase de la
  page 2, celle des étiquettes 3 et 4 : oreillettes étroites à paroi épaisse (22 u, paroi 20 u)
  ouvertes sur des ventricules larges (cavités continues), valvules A-V pendantes et ouvertes,
  sigmoïdes fermées en zigzag. **A** = phase des étiquettes 1 et 2 : oreillettes larges (36 u,
  paroi 8 u), A-V fermées (chevron qui barre le passage), sigmoïdes ouvertes (arcs collés à la paroi
  de l'artère), ventricules étroits à paroi épaisse (VD 20 u, VG 28 u). Les deux artères débouchent
  sur leur ventricule (aorte → VG, pulmonaire → VD) ; veines caves → OD, veines pulmonaires → OG.
- **Convention de Q3** (« الصمّام المغلق خطًّا يسدّ الممرّ … المفتوح ملتصقًا بالجدار ») : respectée
  dans A ; dans B, les valves A-V ouvertes prolongent la paroi de l'orifice et laissent le passage libre.
- **Explications** : Q3 (« جدارا البطينين سميكان وتجويفاهما ضيّقان ») et Q5 (« البطينان واسعان رقيقا
  الجدار … الأذينتان … أضيق ممّا في الرّسم A وجدارهما أسمك ») décrivent exactement les nouveaux
  dessins. « تنفتح الصمّامات الأذينيّة-البطينيّة في الانقباض الأذينيّ وفي الانبساط العامّ معًا » est vrai :
  la distinction repose sur les oreillettes, et Q5 ne se résout que par elles.
- **Forme** : Q3 a un vrai 2×2 (phase × état des valves) avec quatre options de 82 car. ; Q5 a un vrai 2×2
  (phase × état des oreillettes), clé a 77 car. à égalité avec d. Aucune figure ne marque de clé ;
  les `<title>` ne nomment ni phase ni état de valve. Q3 reprend à l'identique le groupe A de Q5.
- **Rendu** à 232 px (page rtl, enveloppe ltr) et ×3 : numéros 1–4 lisibles, cercle « 1 » dans le
  viewBox (bord à 330), lettres A/B en `middle`, rien d'interdit, arabe dans `<title>` seulement.

**[MINEUR] Q1 et Q5, cœur B — ventricules sans paroi en bas des côtés, et VG pas plus épais que le VD.**
Calculé sur les tracés : les cavités des deux ventricules sortent du contour du cœur de 3,9 u au plus,
entre y = 182 et y = 203 (repère du groupe) ; la paroi y tombe à zéro (défaut préexistant, conservé par
le redessin). Les parois latérales valent 8 u à gauche comme à droite. L'ancien B avait 10 contre 7 ;
le PDF montre le VG plus épais, et l'explication de Q1 l'enseigne (« وجداره أسمك من جدار البطين
الأيمن »). Correctif, dans le groupe `translate(6,30)` des SVG de Q1 ET de Q5 :
- « V124 H78 V178 Q78 204 51 204 Q24 204 24 178 V124 » → « V124 H78 V154 Q78 190 51 190 Q24 190 24 154 V124 » ;
- « V124 H92 V178 Q92 204 119 204 Q146 204 146 178 V124 » → « V124 H92 V154 Q92 190 117 190 Q142 190 142 154 V124 » ;
- bosses : « M24 159 Q35 166 24 173 Z » → « M24 136 Q35 143 24 150 Z » ; « M146 159 Q135 166 146 173 Z »
  → « M142 136 Q131 143 142 150 Z » ; supprimer les deux `<path>` « M24 177 Q35 184 24 191 Z » et
  « M146 177 Q135 184 146 191 Z ».

Vérifié par script : chaque chaîne apparaît une seule fois par SVG ; plus aucun point hors du cœur ;
paroi minimale 6,2 u (VD) et 9,3 u (VG) ; parois latérales VD 8 u, VG 12 u. Les cavités de B
(54 × 66 et 50 × 66) restent plus grandes que celles de A (42 × 52 et 34 × 52), à paroi plus mince ; les
bosses ne touchent pas les valves. Rendu dans Chromium à 232 px et ×3 : conforme, numéros intacts.

Rendu des champs modifiés : dans l'explication de Q5, « الرّسم B … الرّسم A » se lit dans l'ordre source
(positions mesurées) ; `splitMathRuns` les laisse en prose.

---

## Étiquettes (29) et `bio.dig.eau-sans-enzyme`

Chaque étiquette relue sur l'option, l'énoncé, l'explication et les usages publiés de la même
étiquette. Le test : l'erreur du libellé, et elle seule, mène-t-elle de l'énoncé à CETTE option ?
Les 29 sont toutes sur des QCM. Le `.strict()` d'arena#1147, sur `main` mais pas dans le clone local
(#1142), refuse une étiquette sur une option multi, matching ou ordering : un script confirme
qu'aucune n'en porte ici.

| fichier | options (étiquette) | verdict |
|---|---|---|
| 02/07 | Q1 d, Q3 d (`cerveau-dans-l-arc-reflexe`) ; Q2 c, Q3 c, Q4 a texte neuf, Q5 a (`sensitif-et-moteur-confondus`) | 6 exactes |
| 02/08 | Q1 a, b, c (`reflexe-pris-pour-volontaire`, `inne-pris-pour-acquis`, `vitesse-comme-critere`) ; Q3 b, Q5 a, c (`cause-sans-temoin`) ; Q5 d (`cerveau-dans-l-arc-reflexe`) | 7 exactes |
| 05/07 | Q2 d (`specificite-enzyme-ignoree`) ; Q3 c (`bile-avec-enzymes`) | 2 exactes |
| 05/08 | Q2 a (`cause-sans-temoin`) ; Q2 b, Q5 a, c (`specificite-enzyme-ignoree`) ; Q2 c, Q3 c (`enzyme-agit-seule`) ; Q3 a (`unites-structurales-confondues`) ; Q4 b (`bile-avec-enzymes`) | 8 exactes |
| 05/08 | Q7 b (`absorption-dans-la-digestion`) | **à retirer** (section 05/08) |
| 07/07 | Q1 c (`specificite-enzyme-ignoree`) ; Q2 c, d (`valeur-d-une-autre-grandeur` : 70 % = compartiment cellulaire, 21 % = interstitiel seul) ; Q3 d (`nerfs-craniens-et-rachidiens-confondus`) | 4 exactes |
| 07/08 | Q6 b (`artere-sang-oxygene`) | 1 exacte |

Bilan : 28 exactes, 1 à retirer. Sur 05/08 Q7 b, je tranche pour le retrait. Mon audit avait proposé
cette étiquette ; c'est un défaut de mon correctif. `specificite-enzyme-ignoree` sur « tel suc agit
sur tel aliment » suit ses usages publiés (amylase sur l'albumine, trypsine sur l'amidon). Pour
05/08 Q5 a et c, l'explication nomme l'erreur : « دون النّظر إلى المادّة التي تعمل عليها ».

### `bio.dig.eau-sans-enzyme` — non appliquée, et mon libellé était inexact sur deux poses

**État constaté** : l'étiquette n'existe nulle part. Le registre `content/misconceptions.json`
(indexé comme dans l'arbre, modifié le 10-02 à 07:07) n'a pas d'entrée `bio.dig.eau-sans-enzyme`.
Aucune des quatre options ne la porte. `git log --all -S` ne la trouve que dans la copie de mon
rapport d'audit (point de sauvegarde 9bcf5e2b). Le point (4) n'est donc pas fait. Tant mieux, car
mon libellé avait un défaut :

| pose | erreur exécutée | verdict avec mon libellé |
|---|---|---|
| 05/08 Q3 b « فكّك الماء وحده … دون حاجة إلى أنزيم » | l'eau digère seule | exacte (R1 : « والماء وحده لا يكفي … أو الاستغناء عن الأنزيم ») |
| 05/08 Q4 a, texte neuf « يضيف ماءً … فيتمّ بفضله تفكيك الزّيت كلّه » | ajouter de l'eau à un tube déjà aqueux, où les enzymes sont là, achève la digestion | **inexacte** : « الماء وحده … لا بدونه » est une croyance voisine. L'explication nomme l'erreur réelle (« أو الظنّ أنّه يزيد الماء، والمحلول مائيّ أصلًا ») |
| 05/08 Q5 d « الماء المقطّر » | même erreur | **inexacte** (« أو الظنّ أنّ زيادة الماء تتمّم التّفكيك ») |
| 05-al-hadm/03-boss Q3 c « أنّ الماء يهضم اللّحم » | — | **refusée** : l'explication ne nomme pas l'erreur (R1 manque) et l'option contredit l'énoncé (« لم يتغيّر في الماء ») : elle s'élimine à vue. À laisser muette (publiée, hors tranche) |

**[MINEUR, défaut de mon correctif] Correctif** : un libellé qui nomme la croyance commune aux trois
poses de 05/08, c'est-à-dire attribuer la digestion à l'eau. Il tient en une phrase adressée à l'élève,
sans `competency` (comme les autres `bio.dig.*`), sans chiffre ni latin :

```json
"bio.dig.eau-sans-enzyme": {
  "subject": "bio",
  "labels": {
    "fr": "Tu attribues la digestion à l'eau : elle ne découpe les molécules que si une enzyme facilite son action, et en ajouter à un milieu déjà aqueux ne digère rien de plus.",
    "en": "You credit water with the digestion: it splits molecules only when an enzyme facilitates its action, and adding more to an already watery medium digests nothing more.",
    "ar": "تنسب الهضم إلى الماء: الماء لا يفكّك الجزيئات إلّا بتيسير من أنزيم، وإضافته إلى وسط مائيّ أصلًا لا تزيد الهضم شيئًا."
  }
}
```

Poses : 05/08 Q3 b, Q4 a et Q5 d. Cela fait trois questions distinctes, toutes dans la même mission :
le seuil « ≥ 3 questions distinctes » de `content-schema.md` est atteint à la lettre. Pas de pose sur
03-boss Q3 c. Sur chaque pose, l'explication nomme l'erreur (R1) et l'option n'en porte qu'une. Dans
Q4 et Q5, l'énoncé donne le milieu aqueux : « محلول » en Q4 ; en Q5, les deux sucs, et
l'explication le dit.

---

## Gates (lecture seule, clone moteur local détaché à #1142, `content` lié au dépôt de contenu)

- `build.ts --check` : sortie 0 (120 matières, 853 étiquettes au registre).
- `qa.ts --subject sciences-vie-terre` : 0 erreur, 7 avertissements, aucun sur les six fichiers.
- `tranche.ts --chapters 02-…,05-…,07-…` : aucune paire proche ne touche les six fichiers. Clé
  strictement la plus longue : 0 sur les 24 QCM des six fichiers (les 64 % mesurés sont ceux des
  chapitres publiés). La répartition des positions est sans objet, les options étant mélangées à
  l'écran.
- Scan des six fichiers : rampes non décroissantes, en-têtes conformes à l'étage (sauf 02/08, voir plus
  haut), aucune option non-QCM portant un champ autre que `id`/`text` (règle `.strict()` de `main`).

---

## Bilan

**Clés.** Chaque question touchée a été re-résolue à l'aveugle avant lecture de la clé : 02/07 Q2,
Q4, Q6 ; 02/08 Q2 à Q5 ; 05/07 Q4, Q5 ; 05/08 Q1 à Q7 ; 07/08 Q1, Q3, Q5. **Aucune divergence.**
Dans les questions touchées, aucune option ne nie plus de prémisse et aucune clé n'est strictement la
plus longue. Les plans 2×2 n'ont plus de vote (05/07 Q4, 07/08 Q3 et Q5), et la forme ne départage plus
02/07 Q6. La fuite 05/08 Q6 → Q7 est levée.

**Défauts nouveaux, classés.** Critiques : **0**. Majeurs : **0**. Mineurs : **7**.

| # | où | défaut | origine | correctif |
|---|---|---|---|---|
| 1 | 02/07 Q6 | « نستنتج » : la clé va au-delà des deux résultats | mon correctif | fin d'énoncé (section 02/07) |
| 2 | 02/08 Q4, Q5 | deux fibres de Y hors du cadre | redessin | 2 tracés, dans les 2 SVG (section 02/08) |
| 3 | 02/08 | en-tête d4 avec 2 questions d2 sur 5 | suppression de l'ex-Q3 | boss d3, 120/30, ⭐⭐⭐ |
| 4 | 05/08 Q7 b | étiquette `absorption-dans-la-digestion` inexacte et ambiguë | mon correctif | la retirer |
| 5 | 05/08 Q7 | marqueur de forme : seule la clé n'a pas « ظاهرة » | préexistant, manqué à l'audit | c → « يمرّ الجليكوز من المعي الدّقيق إلى دم الوريد: ظاهرة الامتصاص » |
| 6 | 07/08 Q1, Q5 | cœur B : ventricules sans paroi en bas des côtés ; VG pas plus épais que le VD | préexistant + redessin | 4 remplacements et 2 suppressions, dans les 2 SVG (section 07/08) |
| 7 | registre + 05/08 Q3 b, Q4 a, Q5 d | `bio.dig.eau-sans-enzyme` non appliquée ; mon libellé inexact sur Q4 a et Q5 d ; 03-boss Q3 c refusée | mon correctif | libellé élargi, 3 poses (section Étiquettes) |

**Mes correctifs, à charge.** Cinq défauts viennent de textes que j'avais fournis. Deux ont été
attrapés et réparés par l'auteur : 02/07 Q4 a, vraie à la lettre, et l'« المحلول » de l'explication de
05/08 Q4, absent de l'ancien énoncé. Trois sont relevés ici : n° 1, 4 et 7. Les correctifs de ce
rapport sont tous vérifiés par script, et dans Chromium pour ceux qui se rendent.

**Chiffre final.** 35 questions (02/07 : 6 · 02/08 : 5 · 05/07 : 5 · 05/08 : 9 · 07/07 : 4 · 07/08 : 6).
0 clé fausse, 0 critique, 0 majeur, 7 mineurs. 9 questions à retoucher : 02/07 Q6 ; 02/08 Q4, Q5 ;
05/08 Q3, Q4, Q5, Q7 ; 07/08 Q1, Q5. S'y ajoutent l'en-tête de 02/08 et une entrée au registre.
Étiquettes : 28 sur 29 exactes, 1 à retirer, 1 nouvelle à créer avec 3 poses. Gates verts.
Aucun de ces mineurs ne fausse une clé. Tous sont des remplacements exacts, déjà vérifiés : après
application, un passage des gates suffit (`build --check` valide la nouvelle entrée du registre et
ses trois poses), sans nouvelle re-vérification de fond.
