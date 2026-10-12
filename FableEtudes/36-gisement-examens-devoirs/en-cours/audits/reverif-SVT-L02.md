# Re-vérification ciblée — lot SVT-L02 (ch. 03-al-ibsar, missions 07 à 11), après correctifs

## État d'avancement

- [x] Version auditée identifiée et diff structurel aveugle (auditée → arbre actuel)
- [x] Section 07 — écrite
- [x] Section 08 — écrite
- [x] Section 09 — écrite
- [x] Section 10 — écrite
- [x] Section 11 — écrite
- [x] Étiquette neuve `bio.vis.difference-non-montree` (en attente, non posée) — vérifiée
- [x] Synthèse et verdicts — écrites (re-vérification terminée)

Auditeur indépendant, même consigne que `audit-SVT-L02.md`. Version auditée = ma copie des cinq fichiers prise
pendant l'audit (`/tmp/audit-svt-l02/tranche/`, tailles 27929/38515/24690/10574/30534 octets, identiques aux
fichiers audités). Rien n'est modifié dans le dépôt.

## Méthode

- Diff structurel AVEUGLE (énoncés, options, figures, type, difficulté ; sans clé, explication ni étiquette) :
  touchées = 07 Q1, Q2, Q3 (énoncé + figure), Q4 (options a, b, e) ; 08 Q1 (énoncé, figure, option a), Q2, Q3
  (énoncé + figure), Q4 (énoncé, figure, options a, c, d, e) ; 09 Q3 (énoncé, option d), Q4 (difficulté) ;
  10 Q1 (options a, c, d), Q3 (option d) ; 11 Q1–Q5 (figure), Q6 (énoncé + figure). Explications changées en
  plus : 07 Q1, Q3 ; 08 Q1, Q4 ; 09 Q1, Q2 ; 10 Q1, Q3. En-têtes inchangés (09 reste boss d3 120/30).
- Figures : diff ligne à ligne des SVG — **seules des suppressions** de `<text>` « أ »/« ب » (13 figures) et le
  `<title>` de 11 Q6 (« مقطعات » → « مقاطع ») ; aucun trait, point ni coordonnée déplacé.
- Questions touchées re-résolues à l'aveugle avant lecture de leur clé ; rendu Chromium `dir=rtl` (harnais
  `RichField`, `bidi.ts` d'arena `origin/main`) de toutes les questions des cinq fichiers ; `check-figures.mjs`
  et `check-overflow.mjs` : **17 figures, 0 défaut, 0 texte hors viewBox** ; `splitMathRuns` n'isole toujours
  que « (1) »/« (2) » (09 Q2, Q4) ; balayage notation/renvois (dont « الجدول », arabe dans `<text>`) : **0**.

## 07 (4 questions, practice d2, rampe 1,2,2,2)

| item corrigé | ma réponse (aveugle) | clé | verdict |
| --- | --- | --- | --- |
| Q1 (énoncé : positions, figure sans lettres, piège de l'explication) | c | c | OK |
| Q2 (énoncé : positions, figure) | a, c, e | a, c, e | OK |
| Q3 (énoncé : positions, « طول الليف », figure, explication) | b | b | OK |
| Q4 (a, b, e : « أليافًا ») | a, b, c, f | a, b, c, f | OK |

- **Écart 1 (Q1, « من الوثيقة … منها »)** : « الليف (أ) في الجهة اليمنى من الوثيقة والليف (ب) في الجهة اليسرى منها » —
  juste (le ليف (أ) est bien à droite, le (ب) à gauche), accord « منها » ↔ « الوثيقة » correct, et l'argument de
  l'auteur tient : « من الرّسم » aurait été ambigu juste après « رسمين ». Meilleur que mon texte.
- **Écart 2 (Q2, Q3 : « : … » sans parenthèse imbriquée)** : mon insertion « (الليف (أ) …) » aurait imbriqué deux
  parenthèses ; la forme « …(أ) و(ب): الليف (أ) في الجهة اليمنى من الرّسم والليف (ب) في الجهة اليسرى منه » se lit
  d'un trait (rendu vérifié). Meilleur que mon texte.
- **Écart 3 (Q3, « طول الليف » deux fois)** : « … موازٍ لطول الليف، والمقطع العرضيّ مستواه عموديّ على طول الليف » ;
  plus d'homonymie محور (axe/axone) ; l'explication est alignée (« موازيًا لطول الليف … عموديًّا على طول الليف »).
  Aucune option ne change de statut : a et d restent réfutées par la figure.
- **Q1 explication** : mon texte appliqué tel quel ; relu : « عكس العنصرين، أي تسمية الحلقة محورًا والنّقطة السّوداء
  غمدًا » décrit bien l'erreur de d (2 = محور, 3 = غمد ; et 1 = محور par la même inversion dans (أ)). OK.
- **Q4** : tanwīn juste dans a, b, e ; longueurs vrais 32/39/74/76, faux 67/73 : aucun indice créé.
- **Figures** : les deux `<text>` retirés, rien d'autre ne bouge (diff). Cosmétique : les deux accolades restent
  sans lettre (elles désignent encore la rangée haute et le cercle haut-gauche, et l'énoncé dit le côté) — à
  garder ou à retirer au choix, sans effet sur aucune réponse.
- Fuites : inchangées (redondance 1أ → 1ب du sujet, déjà arbitrée). Rien d'introduit.

**Verdict 07 : OK.**

## 08 (4 questions, practice d2, rampe 1,2,2,2)

| item corrigé | ma réponse (aveugle) | clé | verdict |
| --- | --- | --- | --- |
| Q1 (contexte « تمثّل الوثيقة », option a « réflexe/réflexe », figure, explication) | d | d | OK |
| Q2 (« من العناصر التّالية », figure) | l1-r5 l2-r3 l3-r2 l4-r6 l5-r4 l6-r1 | idem | OK |
| Q3 (contexte, figure) | a | a | OK |
| Q4 (multi refait, énoncé de contexte réécrit, explication) | a, b, d, e | a, b, d, e | OK |

- **Q1** : grille recomptée sur le texte final — (أ) انعكاسيّ a, d / إراديّ b, c ; (ب) انعكاسيّ a, c / إبصار b, d : chaque
  valeur deux fois ; c double erreur muette ; b garde `reflexe-pris-pour-volontaire` (exacte) ; clé d 47 car. (a 55,
  c 53, b 45). a n'est plus réfutée par la légende : il faut savoir que (ب) est une sensation consciente sans
  effecteur. Piège de l'explication appliqué tel quel : juste, et ne dit rien du trajet moteur (pas de fuite vers Q4).
- **Q2** : « أنسب كلّ عنصر من العناصر التّالية إلى ما يوافقه في الرّسم المعنيّ. » — plus de renvoi au tableau absent ;
  appariement unique, chaque élément de droite garde deux partenaires plausibles.
- **Q4 (nouveau multi, clé {a, b, d, e}, 4/6)** : d « في الرّسمين معًا تنشأ السّيالة العصبيّة الحسّيّة في مستقبلات حسّيّة »
  est **vraie et enseignée** (ch. 02 : « الوخز يُنبّه المستقبلات الحسّيّة في الجلد ← تنشأ هناك السّيالة العصبيّة الحسّيّة » ;
  ch. 03, étape 2 : « نشأة السّيالة … في مستوى الشّبكيّة، إثر تنبيه المستقبلات الحسّيّة ») et ne nomme ni la peau ni la
  rétine. **Le nombre de bonnes réponses ne se déduit pas de la forme** : une seule paire exclusive reste (b/f, sens
  du trajet moteur) ; c et e ne s'excluent plus (il faut savoir que (ب) n'a pas de trajet moteur) ; a et d sont
  indépendants. Longueurs : vrais 59/68/70/70, faux 69/71 — l'option la plus longue (c, 71) est fausse ; d,
  seule de son gabarit, n'est pas désignée par la forme (le gabarit commun « في الرّسم … تنتقل » porte deux vraies et
  deux fausses).
- **Écart 4 (Q4 : explication et énoncé reformulés)** : l'auteur a retiré « مستقبلات الجلد » de MON explication —
  à juste titre : elle donnait la paire l3–r2 de Q2 (« خلايا حسّيّة في الجلد ») à qui tire Q4 avant Q2 au donjon
  (**défaut de mon correctif**, repris de l'explication d'origine). Texte final relu : « تتّجه من الجلد نحو المركز
  العصبيّ » ne départage pas r2 et r5 (les deux disent « الجلد ») ; « الرّسم العلويّ/السّفليّ » au lieu de « (أ)/(ب) »
  évite l'avertissement QA ; rien n'y nomme les centres (Q3) ni les fonctions (Q1). Énoncé « يبيّن الرّسم العلويّ (أ)
  والرّسم السّفليّ (ب) في الوثيقة وظيفتين للاتّصال بالوسط. … تصف السّيالة العصبيّة » : grammatical (verbe singulier
  devant sujets coordonnés), positions dites, et « السّيالة » (au lieu de « مسارات السّيالة ») couvre le nouveau d
  (origine). Paires proches : `content:tranche` (ch. 03, lecture seule) ne signale aucune paire ≥ 0,45 touchant
  07–11.
- **Figures Q1–Q4** : `<text>` « أ »/« ب » retirés, rien d'autre ne bouge ; les contextes disent « (أ) في الأعلى …
  (ب) في الأسفل » (Q1–Q3) ou « العلويّ (أ) … السّفليّ (ب) » (Q4). Rendu Chromium : OK.

**Verdict 08 : OK** (les deux majeurs sont levés ; aucun défaut introduit).

## 09 (5 questions, boss d3 120/30 maintenu par arbitrage, rampe 2,2,2,2,3)

| item corrigé | ma réponse (aveugle) | clé | verdict |
| --- | --- | --- | --- |
| Q1 (explication : renfort cornéen rattaché au laser du cours) | b | b | OK |
| Q2 (explication reformulée) | d | d | OK |
| Q3 (énoncé « والعينَ نفسها », option d) | a | a | OK |
| Q4 (difficulté 3 → 2) | l1-r1 l2-r2 l3-r3 | idem | OK |

- **Q3** : grille recomptée sur le texte final — رسم 1 « على الشّبكيّة » commun aux quatre (donné par la prémisse
  « عينًا سليمة ») ; رسم 2 أمام a, c / خلف b, d ; مقلوب a, b / معتدل c, d : chaque valeur deux fois ; d (خلف + معتدل)
  est la double erreur, **muette** (vérifié) ; b garde `myopie-hypermetropie-inversees`, c `image-redressee-par-l-oeil`,
  toutes deux exactes ; aucune option ne nie plus la prémisse ; longueurs 82/81/82/81. Énoncé : « والعينَ نفسها » juste,
  « (1) »/« (2) » isolés et bien ordonnés (Chromium).
- **Q1** : ma phrase appliquée telle quelle ; relue : « … وهو ما يعزّز الحكم نفسه: فالإصلاح الحديث لقصر البصر يجعل
  الجزء المركزيّ من القرنيّة أكثر تسطّحًا. » — cohérente avec le tableau du cours, ne livre ni la propriété près/loin
  (Q2), ni la position de l'image (Q3), ni le type de lentille (Q4).
- **Écart 5 (Q2, « أمّا » doublé)** : mon remplacement aurait mis deux « أمّا » de suite (la phrase précédente en
  contenait déjà un) — **défaut de mon correctif**, corrigé par l'auteur : « صاحبها يبصر الأجسام القريبة بوضوح،
  ويتشوّش إبصاره للأجسام البعيدة دون أن ينعدم. أمّا الإبصار الجيّد عن بعد وغير الواضح عن قرب فخاصّيّة العين التي
  نقص قطرها. » — correct, et toujours sans fuite.
- **Q4 en d2** : rampe 2,2,2,2,3 non décroissante, ordre d'émission inchangé. **En-tête boss d3 avec la seule Q5
  en d3** : décision d'arbitrage, que je prends acte ; la règle (« un en-tête d3 dont toutes les questions seraient
  d1–d2 est malhonnête ») n'est pas enfreinte.
- **Point 4 (figure, arbitrée)** : l'allongement reporté sur le segment postérieur ne rend aucune option vraie et
  aucune clé fausse : Q1 (« القطر … ازداد ») vrai sur la figure comme sur le scan, a/d (« نقص ») faux ; Q3 (image devant
  la rétine de l'œil long) conforme ; Q4 l3 se réfère à l'œil sain du dessin 1. Rien à signaler.

**Verdict 09 : OK** (majeur levé ; mineurs appliqués ; deux de mes textes reformulés à raison par l'auteur — Q2 —
ou repris tels quels — Q1, Q3).

## 10 (4 questions, boss d3, rampe 2,3,3,3)

| item corrigé | ma réponse (aveugle) | clé | verdict |
| --- | --- | --- | --- |
| Q1 (options a, c, d ; explication) | b | b | OK · **réserve mineure (introduite par mon texte)** |
| Q3 (option d ; explication) | a | a | OK |

- **Q1, grille (iris | rétine) × (muscles moteurs | nerf optique)** recomptée sur le texte final : 1ʳᵉ case
  « تلف الشّبكيّة اليسرى » b, d / « تلف القزحيّة اليسرى » a, c ; 2ᵉ case « تلف العصب البصريّ المتّصل بها » b, c /
  « تلف العضلات المحرّكة للعين اليسرى » a, d — chaque valeur deux fois, textes identiques d'une option à l'autre ;
  a double erreur muette ; aucune option ne nomme plus un élément que l'énoncé déclare sain ; longueurs 55/50/50/55
  (clé non la plus longue) ; iris et muscles sont au cours (rôles enseignés), hypothèses fausses non réfutables
  à vue. Explication (mon texte, appliqué tel quel) relue : « المتّصل بها » y renvoie bien à « الشّبكيّة اليسرى »,
  « تلفهما » (duel : iris et muscles) correct, rien sur le rôle de la rétine (pas de fuite vers Q3/Q4). OK.
- **[MINEUR — défaut de mon correctif, hérité de l'option d'origine]** dans c « تلف القزحيّة اليسرى، أو تلف العصب
  البصريّ المتّصل بها », le pronom « بها » renvoie à l'antécédent féminin le plus proche, « القزحيّة » : « le nerf
  optique rattaché à l'iris », description anatomique fausse (l'option d'origine avait le même défaut avec
  « القرنيّة »). Sans effet sur la clé (c reste fausse par l'iris), mais un énoncé faux dans la moitié « juste » de
  la case. Correctif — remplacer la 2ᵉ case par un nom sans pronom, à l'identique dans b et c (grille préservée) :
  b « تلف الشّبكيّة اليسرى، أو تلف العصب البصريّ الأيسر » ; c « تلف القزحيّة اليسرى، أو تلف العصب البصريّ الأيسر »
  (a et d inchangées). Vérifié : cases b, d / a, c et b, c / a, d, chaque valeur deux fois ; longueurs a 55, b 46,
  c 46, d 55 (clé non la plus longue, à égalité avec c) ; `splitMathRuns` : aucun run ; rendu Chromium `dir=rtl`
  correct. L'explication garde « العصب البصريّ المتّصل بها » (référent : la rétine) — juste, à laisser ; l'énoncé de
  Q2 aussi (« تلف الشّبكيّة اليسرى، أو تلف العصب البصريّ المتّصل بها ») — juste, et il ne recopiera plus mot pour mot
  la clé de Q1.
- **Q3** : d « تحليل السّيالة العصبيّة الحسّيّة والتّعرّف على الأشياء » ne se réfute plus par « في المخّ » ; fausse
  comme rôle de la rétine (cours : analyse aux مراكز الإبصار) ; longueurs 44/44/51/48. Explication (mes deux
  retouches appliquées telles quelles) relue : « فإذا عجزت عن ذلك لم تنشأ سيالة، فغابت في العصب السّليم وغاب
  الإبصار » (« غابت » → « سيالة », correct) ; « وتحليل السّيالة ليس من عمل الشّبكيّة » : f de Q4 n'est plus livré ;
  restent, inévitables, b (rôle de la rétine = clé de Q3) — chaînage du sujet déjà arbitré.
- Q2, Q4 inchangés. Rendu Chromium des quatre questions : OK.

**Verdict 10 : réserve mineure** (majeur levé ; un mineur dans MON texte de Q1 c, correctif ci-dessus).

## 11 (6 questions, boss d3, rampe 2,2,2,3,3,3)

| item corrigé | ma réponse (aveugle) | clé | verdict |
| --- | --- | --- | --- |
| Q1–Q5 (figures : « أ »/« ب » retirés) | Q1 b, e, f · Q2 c · Q3 d · Q4 b, d · Q5 b | idem | OK |
| Q6 (énoncé « مقاطع … لأعين شابّين », figure, `<title>` « مقاطع ») | c | c | OK |

- Figures : diff = suppression du seul `<text>` de chaque figure (et des deux en Q6) + `<title>` de Q6 ; rien ne bouge.
  Chaque énoncé nomme le jeune et le côté de chaque œil ; Q6 dit les rangées (« الصّفّ العلويّ للشّابّ (أ) والصّفّ
  السّفليّ للشّابّ (ب) ») : rien n'est perdu avec les lettres. Rendu Chromium : OK.
- Q6 : mon texte appliqué tel quel ; relu : « يبيّن الرّسم مقاطع أماميّة خلفيّة لأعين شابّين » — pluriel juste pour
  quatre coupes, accord correct ; options, clé, étiquettes (a, d `myopie-hypermetropie-inversees`) inchangées ; grille
  (أ) لامّة a, b / مفرّقة c, d ; (ب) مفرّقة a, c / لامّة b, d intacte.
- Explications, clés et étiquettes de 11 : inchangées (vérifié). La propriété près/loin n'apparaît toujours dans
  aucune explication avant Q5.
- **Point 4 (figure, arbitrée)** : le rapport 1,9 des cristallins de (ب) ne rend aucune option vraie ni aucune clé
  fausse : Q3 (« متقارب … الجسم البلّوريّ في العين اليسرى أكثر سمكًا ») vraie, c (« … في العين اليمنى ») fausse ; en Q4 la
  figure ne montre que la rangée (ب), les deux hypothèses restent possibles ; en Q6 le cristallin droit de (ب),
  identique à ceux de (أ), va dans le sens de la clé (œil droit de (ب) sain). Rien à signaler.

**Verdict 11 : OK.**

## Étiquette neuve `bio.vis.difference-non-montree` (en attente, non posée)

- `pending-tags/SVT-L02.json` relu : libellés fr/en/ar **identiques** à ceux de mon audit ; absente du registre
  d'`origin/main` (edb6e795, 858 entrées ; aucun identifiant voisin) ; aucun des cinq fichiers ne la porte (les deux
  options sont muettes jusqu'à la livraison) — conforme.
- Placements contrôlés sur les textes FINAUX (inchangés depuis l'audit) : 11 Q2 b « قصر البصر، لأنّ تحدّب الجسم البلّوريّ
  في العين اليمنى أكبر منه في العين اليسرى » — le défaut est juste, la différence de cristallin lue n'existe pas sur la
  rangée (أ) (cristallins rx 4,2/4,2) : libellé exact ; 11 Q3 a « القطر الأماميّ الخلفيّ في العين اليمنى أكبر، والجسم
  البلّوريّ في العين اليسرى أكثر سمكًا » — globes de même longueur (83/83), une seule erreur (la moitié cristallin est
  juste) : libellé exact. Grilles : 11 Q2 a et 11 Q3 b (doubles erreurs) restent muettes ; 11 Q3 c (côté inversé)
  muette — cohérent. Libellé arabe relu : duel « الرّسمين … لا يُظهرانه … بينهما » correct ; la virgule arabe entre
  parenthèses sépare des mots arabes (prose), pas une notation : sans risque bidi.
- Étiquettes existantes : 13 placements sur 5 identifiants, tous présents sur `origin/main` avec des libellés
  inchangés ; aucun retrait, aucun ajout depuis l'audit (08 Q1 b et 09 Q3 b, c conservés sur les options réécrites
  autour d'eux).

## Gates (lecture seule, arbre partagé, moteur `scripts/content` identique à arena `origin/main`)

`content:check` vert (120 matières, 28 303 questions, dont les cinq fichiers) ; `content:qa --strict` : aucune ligne
sur 03-al-ibsar 07–11 ; `content:tranche --subject sciences-vie-terre --chapters 03-al-ibsar` : aucune clé
strictement la plus longue ni aucune paire ≥ 0,45 touchant 07–11 (les signalements restants portent sur le quiz et
les missions 01–06 publiés) ; `check-figures` / `check-overflow` : 17 figures, 0 défaut.

## Synthèse et chiffre final

- **23 questions relues** ; 20 touchées par le tour de corrections (dont 18 re-résolues à l'aveugle avant lecture de
  la clé — 07 Q1–Q4, 08 Q1–Q4, 09 Q3–Q4, 10 Q1, Q3, 11 Q1–Q6 — et 2 dont seule l'explication a changé, 09 Q1–Q2).
- **0 clé fausse · 0 critique · 0 majeur** ; les 4 majeurs de l'audit sont levés (08 Q2, 08 Q4, 09 Q3, 10 Q1) et les
  17 mineurs appliqués.
- **1 mineur introduit — par MON texte** (hérité de l'option d'origine) : 10 Q1 c, « المتّصل بها » renvoie à l'iris.
  Correctif vérifié (script, grille, longueurs, Chromium) : b « تلف الشّبكيّة اليسرى، أو تلف العصب البصريّ الأيسر » et
  c « تلف القزحيّة اليسرى، أو تلف العصب البصريّ الأيسر » (a, d, clé b, explication et énoncé de Q2 inchangés).
- **Deux de mes correctifs étaient défectueux, l'auteur les a corrigés à juste titre** : 08 Q4, mon explication
  gardait « مستقبلات الجلد », qui livre la paire l3–r2 de 08 Q2 au donjon ; 09 Q2, mon remplacement doublait « أمّا ».
  Les cinq écarts de l'auteur à mes textes (07 Q1 « من الوثيقة … منها », 07 Q2–Q3 sans parenthèse imbriquée, 07 Q3
  « طول الليف », 08 Q4 explication/énoncé, 09 Q2) sont justes et meilleurs que mes textes.
- Cosmétique, au choix : les accolades orphelines de la figure de 07 (Q1–Q3).
- Arbitrages pris acte : 09 boss d3 avec Q4 en d2 (rampe 2,2,2,2,3) ; figures de 09 et 11 telles quelles — aucune ne
  rend une option vraie ni une clé fausse.

**Verdicts : 07 OK · 08 OK · 09 OK · 10 réserve mineure (10 Q1 b/c, une expression à remplacer) · 11 OK.**
Livrable après le correctif de 10 Q1 (ou en l'état, le défaut étant sans effet sur la clé) ; étiquette neuve à
créer au registre dans le même commit que ses deux placements (11 Q2 b, 11 Q3 a).
