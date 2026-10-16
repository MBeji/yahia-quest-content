# Re-vérification ciblée — L11 (m028–m032), après le commit `43530690`

Auditeur indépendant (même consigne que `audit-svt-L11.md`). Lecture seule : aucune écriture dans
`content/` ni dans git. Rapport écrit au fil de l'eau.

Périmètre : diff `818fdb66..43530690` sur les cinq missions et sur `cours.md`/`resume.md` de 01 et 02
(fichiers `NN-devoir-*` et autres lots ignorés). Journal de l'auteur lu (`auteurs-notes/svt-L11/CORRECTIONS.md`).

## Contrôles automatiques

- `content:check` : 0 erreur. `content:qa` / `qa:strict` : aucun avertissement ni erreur sur les cinq
  missions ni sur les cours/résumés 01–02 (la seule erreur stricte signalée par l'auteur est dans un
  `devoir`, hors périmètre).
- `content:tranche` (01, 02, 03, 07, 13) : clé strictement la plus longue 0/453 ; paires proches : aucune
  dans L11 (celles listées sont un `devoir` du 07 et deux paires publiées).
- Indices de forme mesurés question par question : aucune clé strictement la plus longue ni la plus
  courte dans les cinq missions (m028 Q5 : clé 30 ex aequo ; m029 Q4 61 [46–73], Q5 64 [56–71], Q6 68 ex
  aequo ; m030 Q5 37 [29–44] ; m031 Q7 55 [44–57] ; m032 Q1 52 [29–61]).

## Re-résolution à l'aveugle (questions retouchées et voisines)

| mission | questions (nouvelle numérotation) | mes réponses | clés | verdict |
| --- | --- | --- | --- | --- |
| m028 (6) | Q1–Q6 | 1-corps/2-dendrite/3-axone ; 4-conjonctif/5-faisceau/6-fibre ; (أ) grise/(ب) nerf/(ج) blanche ; c ; a ; d | identiques | OK |
| m029 (9) | Q1–Q9 | {a,b,d} ; {a,b,d,f} ; c ; a ; d ; b ; b ; d ; a | identiques | OK (2 fuites, ci-dessous) |
| m030 (6) | Q1–Q6 | paires de l'audit ; c ; {a,c} ; a ; d ; b | identiques | OK |
| m031 (7) | Q1–Q7 | c ; {a,b,f} ; a ; 1-veines pulm./2-aorte/3-OG ; 4-art. pulm./5-VCS/6-VD ; d ; b | identiques | OK (1 fuite, ci-dessous) |
| m032 (6) | Q1–Q6 | c ; ovul.→pilule, fécond.→préservatif, nidation→DIU ; C,A,B,D ; 1→4 cellules, 2→المضغة, 3→œuf, 4→morula, 5→2 cellules ; a ; d | identiques | OK |

**Clés fausses : 0.** Multi : m029 Q1 3/6, Q2 4/6 ; m030 Q3 2/6 ; m031 Q2 3/6.

## Écarts déclarés par l'auteur — jugement

1. **m028 Q3 sans « علمًا أنّ… »** : **accepté.** Le cours 01 enseigne désormais « بنية العصب » ; la
   phrase aurait doublonné le cours et rapproché la clé. Énoncés de Q3/Q4 allégés : Q3 décrit (ب) par
   « كتل مستديرة … تفصل بينها مساحة داكنة » (il faut appliquer le cours) ; Q4 ne redécrit plus les coupes
   et son explication n'en donne plus la place. Plus de fuite Q4 → Q3.
2. **Lettres أ ب ج dans le SVG de m028 Q3/Q4** : **accepté**, ordre juste (ج à gauche, ب au milieu, أ à
   droite), rendu propre. Taille : `font-size="13"` dans un `viewBox` de 336 → ≈ 9 px à 232 px, lisible
   (facultatif : 16).
3. **m029 Q1 sans scénario** : **accepté** (« … عند الإنسان وعند الحيوان ؟ ») ; ne désigne aucune option,
   ne fuit plus vers Q5.
4. **Longueurs** (m029 Q6 « عصبيّة » ajouté aux quatre chemins ; m029 Q4 clé allongée ; m030 Q5 options
   allongées) : **acceptés** ; re-mesurés ci-dessus, rien de vrai n'est devenu faux (« ألياف عصبيّة حسّيّة »,
   « المنبّه الخارجيّ الذي يتأثّر به », « الأشعّة المتوازية » : re-vérifiés).
5. **m031 Q7 réduite, Q2 reformulée** : **acceptés.** Q7 ne donne plus le lieu des valvules (fuite vers
   Q6 supprimée) ; Q2 n'énonce plus de rôle de valvule.
6. **m032 Q1, explication** (« الخلط بين الإباضة والحيض لأنّهما يقعان في الدّورة نفسها ») : **accepté**,
   exact et cohérent avec le nouveau distracteur b.

## Ajouts de cours — rendu et clés

- Rendu par `renderLesson` / `renderSummary` du moteur (alias `@` → `src`), puis Chromium `dir=rtl` :
  le bloc `propriete` « بنية العصب » de 01 sort en carte « خاصّيّة » avec ses trois termes en gras ; la
  phrase du résumé 01 et les deux modifications de 02 (étape 1 de l'exemple, puce du résumé) s'affichent
  sans ordre brouillé (aucun nombre ni symbole latin dans ces phrases).
- Clés : le bloc 01 donne la règle (fibres en حزم, نسيج رابط entre elles) **sans** dire quelle coupe est
  un nerf ni ce que désignent les repères 4–6 : m028 Q2 et Q3 restent à résoudre. L'exemple 02
  (« ملامسة الطّعام لسان الرّضيع ») ne fournit la clé d'aucune question de m029 (Q2 f le reprend comme
  fonction, ce qui est le but : l'option est désormais vraie sans débat).
- Remarque (mineur, facultatif) : le bloc 01 est une règle sans figure ni exemple ; un croquis de coupe
  de nerf servirait la question m028 Q3, mais rien ne l'exige pour ce lot.

## Défauts restants

- **[MAJOR] m029 Q4 → Q3 (fuite créée par le déplacement).** L'explication de Q4 (récepteur) dit
  « أمّا تحويل السّيالة الحسّيّة إلى سيالة حركيّة فمن عمل المركز العصبيّ » = clé de Q3 (« تنشأ السّيالة
  الحركيّة في مستوى : المركز العصبيّ »). Explication de remplacement (vérifiée : ne nomme ni le centre
  ni le sens des fibres) :
  > يتأثّر المستقبل الحسّيّ بالمنبّه (لمس، حرارة، ضوء…) فيحوّله إلى سيالة عصبيّة حسّيّة: به يبدأ مسار الرّسالة العصبيّة. فهو لا يحوّل سيالة إلى أخرى، وليس هو الليف الذي ينقل السّيالة في العصب، ولا العضو الذي ينفّذ الاستجابة. الخطأ الشائع: نسبة دور عنصر آخر من المسار إلى المستقبل لأنّه أوّل العناصر المذكورة.
- **[MAJOR] m029 Q6 → Q3 (même cause).** L'explication de Q6 (douleur) dit « النّخاع الشّوكيّ، وهو المركز
  الذي يولّد أمر الانسحاب » = clé de Q3. Remplacement (vérifié : ne dit plus où naît le message moteur) :
  > الوخز ينبّه مستقبلات الجلد فتنشأ سيالة حسّيّة تحملها ألياف حسّيّة نحو النّخاع الشّوكيّ، ثمّ تتابع طريقها من النّخاع إلى قشرة المخّ حيث تُحلَّل، فينشأ الإحساس الشّعوريّ بالألم. الخطأ الشائع: جعل الألياف الحركيّة ناقلة نحو المركز؛ أو جعل قشرة المخّ أوّل محطّة بعد المستقبلات؛ أو وضع العضلة، وهي آخر عنصر في الحلقة الانعكاسيّة، قبل قشرة المخّ.
- **[MAJOR] m031 Q1 → Q2 (préexistant, manqué au premier audit).** Fin de l'explication de Q1 :
  « … فيُفتح السّينيّ ويُغلق الأذينيّ البطينيّ، وهذه حالة الانقباض البطينيّ لا الأذينيّ » = deux des trois
  vraies de Q2 (a, b), en nommant la phase. Remplacer la dernière phrase par :
  > الخطأ الشائع: عكس حالة الصمّامين في هذا الطّور، فيُفتح السّينيّ ويُغلق الأذينيّ البطينيّ.

  (re-vérifié : décrit l'erreur sans nommer la phase ; même niveau d'information que l'option a de Q1,
  résidu déjà accepté.)
- **[MINOR] m029, règle des fibres répétée.** Q4 option c (« الليف الذي ينقل السّيالة الحسّيّة … نحو
  المركز ») et l'explication de Q6 énoncent la règle « sensitif → vers le centre », que Q7 et Q8
  appliquent sur figure. C'est une règle du cours, pas une clé : pas de correctif exigé.

## Questions publiées du chapitre 02 (« شمّ رائحة طعام ») — tranché : à reformuler

`02/01-tamrin` Q5 et `quiz` Q8 prennent la salivation à l'odeur d'un mets comme réflexe. La clé
(glande salivaire) resterait juste même pour un réflexe conditionnel, mais 01-tamrin Q5 a une option
étiquetée « لا يوجد عضو منفّذ: هذا ليس فعلًا انعكاسيًّا » qu'un élève appliquant le critère du cours 01
(« هل يفعله مولود جديد ؟ ») peut défendre ; et les deux items contredisent désormais l'exemple du cours.
Reformulation alignée sur le cours (clé c inchangée dans les deux ; re-résolues : c seule ; aucune clé
la plus longue) :

- **01-tamrin Q5** — énoncé :
  > عند ملامسة الطّعام لسان الرّضيع يسيل لعابه. أين العضو المنفّذ هنا؟

  option d « الأنف » → « اللّسان » (sans étiquette ; même erreur qu'avant : le lieu du récepteur pris
  pour l'effecteur). Longueurs : a 43, b 14, c 17 (clé), d 7. Explication :
  > الغدّة اللّعابيّة. العضو المنفّذ ليس دائمًا عضلة: حين يكون غدّةً يكون الفعل إفرازًا لا حركة، والقوس هو هو بعناصره الخمسة. واللّسان هنا موضع المستقبلات الحسّيّة، أي أوّل الحلقة لا آخرها.
- **quiz Q8** — énoncé :
  > ملامسة الطّعام لسان الرّضيع تُحدث إفراز اللّعاب. ما العضو المنفّذ في هذا القوس الانعكاسي؟

  option b « المستقبلات الحسّيّة بالأنف » → « المستقبلات الحسّيّة باللّسان » ; explication inchangée.
  Longueurs : a 10, b 28, c 16 (clé), d 15.
- **04-defi Q4** (gencive anesthésiée, odeur → salive) : **à garder** ; la conclusion (« l'anesthésie
  n'a supprimé que les récepteurs de la gencive ») est vraie que le réflexe olfactif soit inné ou
  conditionnel, et aucune option ne joue sur ce point.

## Figures (Chromium, colonne 232 px, `dir=rtl`)

m028 Q1–Q5 (lettres أ ب ج, taquets de la flèche 5), m029 Q7–Q8, m030 Q4–Q5, m031 Q4–Q6 (repères 7 et 8
désormais séparés : 8 dans la cavité basse gauche vers la valvule auriculo-ventriculaire, 7 côté droit
vers la base du vaisseau), m032 Q3 et Q4 (appariement à cinq paires : numéros 3-5-1 / 4-2, aucun
ordre chronologique, aucun chevauchement nouveau) : toutes lisibles, aucune ne marque une clé.

## Résumé

- **Clés fausses : 0** (34 questions re-résolues).
- **Majeurs restants : 3**, tous des explications qui livrent une clé voisine — m029 Q4 → Q3, m029 Q6 → Q3
  (créées par l'arrivée de l'ex-m028 Q8 dans m029), m031 Q1 → Q2 (préexistante). Textes exacts ci-dessus.
- **Mineurs : 2** — règle des fibres répétée dans m029 (pas de correctif exigé) ; taille des lettres
  du SVG de m028 (facultatif). Hors lot : reformuler `02/01-tamrin` Q5 et `quiz` Q8 (textes ci-dessus) ;
  garder `04-defi` Q4.
- Les six écarts de l'auteur sont acceptés ; les ajouts de cours se rendent bien et ne livrent aucune clé.
- **Verdict : prêt après les trois remplacements d'explication** (aucune question à restructurer).

## Suite donnée par le pilote (2026-10-16)

Les trois majeurs appliqués mot pour mot (m029 Q4 et Q6 explications, m031 Q1 dernière phrase). Questions
**publiées** du ch. 02 reformulées selon les textes de ce rapport (fichiers vérifiés identiques à `main` avant
retouche) : `01-tamrin` Q5 (énoncé, option d « اللّسان », explication) et `quiz` Q8 (énoncé, option b) ;
`04-defi` Q4 gardée. Lettres de m028 laissées à 9 px (facultatif). `content:check` vert, prettier propre.
**L11 prêt à livrer.**
