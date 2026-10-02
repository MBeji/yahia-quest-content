# Audit indépendant — lot L18 (maths 9ᵉ, ch. 20 `orthogonalite-espace`, missions 22 à 26)

> Rapport écrit fichier par fichier (une coupure de session reste possible : les sections présentes sont complètes).
> **Valide pour** : arbre de travail du dépôt contenu tel que lu le 2026-10-02 (md5 : 22 `7d688099…`, 23 `cc361ca5…`,
> 24 `f4038d67…`, 25 `fc5cab76…`, 26 `ee3432d7…`) ; registre et missions publiées lus sur `origin/main` = `65b25590` ;
> moteur de rendu `src/shared/lib/bidi.ts` d'`origin/main` = `dc19a816` (arena#1150 inclus).
> Aucun fichier du dépôt n'a été modifié : les correctifs ont été appliqués à des COPIES hors dépôt, puis passés à
> `lot-lint.mjs`, au rendu Chromium `dir=rtl` (découpage `splitMathRuns` / `isDisplayEquation` du moteur, ordre visuel
> mesuré caractère par caractère et comparé au texte source) et au contrôle DOMPurify des figures.

## Méthode (commune aux cinq fichiers)

1. **Aveugle** : énoncés et options dumpés SANS `correctOption` / `answerKey` / `misconceptionTag` / explication ;
   chaque question résolue à la main puis recalculée par script (sympy, `Fraction`, coordonnées du cube et de la pyramide,
   produits vectoriels pour les plans) ; la clé du fichier n'a été lue qu'ensuite.
2. **Fidélité** : chaque donnée confrontée à la transcription officielle de sa session.
3. **Programme** : cours du ch. 20 et des chapitres antérieurs du manifeste (15 → 01 → 19 → 02 → 16 → 17 → 03 → 04 → 07 → 12
   → 08 → 09 → 18 → 20) lus sur `origin/main`, plus la fiche programme officielle (`programme/9eme-base/maths.md`, ch. 13 du manuel :
   la règle 1 du أحوصل ne donne la perpendicularité que pour « les droites du plan **passant par le pied** », la définition exige
   deux sécantes « **في نفس النقطة** »).
4. **Rendu** : 100 % des lignes (titre, énoncés, options, explications) rendues en Chromium 1194, page `dir=rtl`, avec le découpage
   du moteur `dc19a816` ; écarts entre ordre affiché et ordre source listés puis vérifiés à l'œil (captures ×2).
5. **Figures** : SVG passés à DOMPurify avec la configuration du moteur (`sanitizeSvg`), boîte englobante comparée au `viewBox`,
   vérité géométrique recalculée (coordonnées).
6. `lot-lint.mjs` (moteur `dc19a816`) sur les cinq fichiers : **0 point à regarder**.
7. Balayages mécaniques sur les cinq fichiers : aucun chiffre arabo-indien, aucun LaTeX ni `$`, aucun radicande arabe, aucune virgule
   arabe dans une notation, séparateurs de milliers en U+00A0, aucune référence « الشكل التالي / المقابل / المجاور » sans figure (le piège de
   passe « على الشكل التالي » n'apparaît pas), toutes les coches « ✓ » placées après la valeur ou l'énoncé de la CLÉ, aucun texte arabe dans les
   `<text>` des figures, aucune balise hors `svg/title/path/circle/g/text`.

---

## Mission 22 — `22-examen-2009-generale-ex1-qcm-symetrie-equation-divisibilite-cube.json`

En-tête : « 🏛️ مناظرة 2009 · التمرين 1 ⭐⭐: أسئلة اختيار من متعدّد — نقطتان متناظرتان وحلّ معادلة وقابلية القسمة ومستقيم عمودي على مستوٍ في مكعّب »
— format conforme, le sujet nomme des notions et aucun résultat ; `difficulty` 2, `practice`, 75/15, `displayOrder` 22 : conformes.
Rampe 1,1,2,2,2,2 : non décroissante. **Étage d2 honnête** (deux étapes d1 d'amorce, quatre items d2 dont un raisonnement spatial).

| Q | ma réponse (aveugle) | clé du fichier | verdict | motif |
|---|---|---|---|---|
| Q1 (numeric, d1) | 48 | 48 | réserve | clé juste (1+1+1+3+3+5+5+7+7+9+6 = 48, séparateurs U+00A0) ; la dernière phrase de l'explication oriente Q5 (mineur M22-3) |
| Q2 (numeric, d1) | 45 | 45 | réserve | clé juste ; question sur un angle d'un carré **sans figure** (majeur M22-2) |
| Q3 (mcq, d2) | O (d) | d | réserve | A(−2 ; √2 − 1), B(2 ; 1 − √2) : les deux coordonnées s'opposent ⇒ symétrie centrale de centre O ; (OI)/(OJ)/I recalculés faux ; options muettes alors qu'une étiquette existante convient (mineur M22-4) |
| Q4 (mcq, d2) | 1 (b) | b | OK | x = (√2/2) × √2 = 1 ; 1/2 = division au lieu du produit, √2 = (√2)² lu 2√2, 2 = arrêt à 2x = 2 : étiquettes exactes |
| Q5 (mcq, d2) | 12 (c) | c | OK | somme 48 (multiple de 3, pas de 9), 96 multiple de 4, unités 6 : divisible par 12 seulement ; étiquettes conformes au registre (9 et 18 : critère de 3 pris pour celui de 9 — porte R1, l'explication le nomme ; 15 : un seul des deux critères) |
| Q6 (mcq, d2) | (ACQ) (a) | a | **réserve majeure** | clé juste (normale à (ACQ) ∥ (BD), les trois autres plans faux) ; mais le rappel de l'énoncé et l'explication reposent sur une règle hors cours et contraire à la définition du cours (majeur M22-1) |

### Défauts

**Critique** : aucun (6 clés justes sur 6).

**M22-1 — majeur — Q6 : rappel hors cours, explication contraire à la définition du cours, ✓ mal placé au rendu.**
- Le rappel « نذكّر أنّ مستقيمًا عموديًّا على مستوٍ يعامد كلّ مستقيمات هذا المستوي » n'est pas la règle du cours : le cours (et le
  أحوصل du manuel, règle 1) ne donne la perpendicularité qu'avec les droites du plan **passant par le pied**. Dans le vocabulaire du
  cours, deux droites perpendiculaires se coupent ; (BD) et (CQ) ne sont pas coplanaires, le rappel est donc **faux** tel qu'il est lu
  et il fait appel à une orthogonalité de droites non coplanaires que rien n'enseigne.
- Il est en outre **insuffisant** : le critère du cours (définition + règle 2) exige deux sécantes « في نفس النقطة » où passe la droite ;
  (AC) et (CQ) se coupent en C, qui n'est pas sur (BD). L'explication (« يكون المستقيم عموديًّا على مستوٍ إذا عامد مستقيمين متقاطعين » …
  « (AC) و(CQ) متقاطعان في C ») supprime justement « في نفس النقطة », que le cours répète comme condition indispensable — elle enseigne
  le contraire de la leçon. Même défaut dans la réfutation de (ACR) : « (BD) ليس عموديًّا على (CR) » oppose deux droites non coplanaires.
- Le rappel n'oriente que faiblement la clé (il désigne les plans qui contiennent une arête verticale : (ACQ), (BAS), (BCQ)).
- Rendu : `splitMathRuns` isole « (ACQ) ✓ » d'un seul tenant ; en `dir=rtl` la coche s'affiche **avant** (ACQ) (« … عمودي على ✓ (ACQ) »)
  alors que la source la place après.
- La propriété est démontrable avec le seul cours : O centre du carré, (BD) ⟂ (AC) en O ; QB = QD (diagonales de deux faces) donc
  la médiane (QO) du triangle isocèle QBD est aussi hauteur : (BD) ⟂ (QO) en O ; (AC) et (QO) sécantes en O dans (ACQ).

Correctif exact (vérifié : clé inchangée, aucune prémisse niée, rendu Chromium conforme, `lot-lint` muet) :
- `prompt` : **supprimer** la ligne `\nنذكّر أنّ مستقيمًا عموديًّا على مستوٍ يعامد كلّ مستقيمات هذا المستوي.` (le reste inchangé, figure comprise).
- `explanation` → remplacer par :

```
لتكن O مركز المربّع ABCD، أي نقطة تقاطع قطريه؛ وهي من (AC) فهي من المستوي (ACQ). قطرا المربّع متعامدان، فالمستقيم (BD) عمودي على (AC) في O. والقطعتان [QB] و[QD] قطران لوجهين من المكعّب فهما متقايستان، فالمثلّث QBD متقايس الضلعين قمّته Q، وموسّطه (QO) ارتفاع له أيضًا: (BD) عمودي على (QO) في O. إذن (BD) يعامد في النقطة نفسها O مستقيمين متقاطعين (AC) و(QO) من المستوي (ACQ)، فهو عمودي على هذا المستوي ✓.
ولو كان (BD) عموديًّا على (BCQ) لعامد (BC) المارّ من B، والمثلّث BCD قائم في C لا في B؛ وكذلك (BAS): المثلّث BAD قائم في A لا في B.
أمّا (ACR) فيحوي (AC) العمودي على (BD) في O، لكنّ مستقيمًا واحدًا لا يكفي: لو كان (BD) عموديًّا على (ACR) لعامد (OR) في O، والمثلّث ODR قائم في D لأنّ الحرف (DR) عمودي على مستوي القاعدة، فزاويته عند O حادّة.
```
(Vérifications : (BD) ∩ (BCQ) = B et (BD) ∩ (BAS) = B, d'où la réfutation par l'angle en B ; (BD) ∩ (ACR) = O ∈ (AC), (OR) ⊂ (ACR),
triangle ODR rectangle en D ⇒ angle DOR aigu ⇒ (BD) non perpendiculaire à (OR). Les étiquettes `perpendiculaire-au-plan-deux-secantes`
des trois distracteurs restent exactes.)

**M22-2 — majeur (règle 13 du skill : question sur un angle d'une figure, sans `<svg>`) — Q2.** Correctif : ajouter à la fin du `prompt`
`\n` puis cette figure (rendue : vraie, dans le `viewBox`, aucun angle ni mesure portés, arabe seulement dans `<title>`) :

```
<svg viewBox="0 0 200 180"><title>مربّع ABCD وقطره [BD]</title><path d="M40 30 L40 150 L160 150 L160 30 Z" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/><path d="M40 150 L160 30" fill="none" stroke="#0f6e56" stroke-width="2.5" stroke-linecap="round"/><g fill="#0f172a"><circle cx="40" cy="30" r="3.2"/><circle cx="40" cy="150" r="3.2"/><circle cx="160" cy="150" r="3.2"/><circle cx="160" cy="30" r="3.2"/></g><g font-size="15" font-weight="700" direction="ltr" paint-order="stroke" stroke="#ffffff" stroke-width="4" stroke-linejoin="round"><text x="28" y="26" text-anchor="middle" fill="#0f172a">A</text><text x="28" y="166" text-anchor="middle" fill="#0f172a">B</text><text x="172" y="166" text-anchor="middle" fill="#0f172a">C</text><text x="172" y="26" text-anchor="middle" fill="#0f172a">D</text></g></svg>
```

**M22-3 — mineur — Q1 : l'explication prépare Q5.** « هذا المجموع هو الذي نستعمله في معياري القسمة على 3 وعلى 9، أمّا القسمة على 4 فيكفي
فيها آخر رقمين. » nomme exactement les trois critères utiles à Q5, dont celui de 4 qui ne sert qu'à l'option 12 (la clé). Correctif :
**supprimer** cette phrase (l'explication se termine sur « فمجموع أرقام العدد هو 48 ✓. »).

**M22-4 — mineur — Q3 : étiquettes manquantes.** `math.vec.symetrie-axiale-signe-mal-place` (sur `origin/main` depuis #622 — absente de
l'arbre de travail de l'auteur, d'où sa déclaration « aucune étiquette ») dit mot pour mot l'erreur de (OI) et de (OJ) : « Par rapport à un
axe, une seule coordonnée change de signe … ; changer les deux signes, c'est la symétrie par rapport à O », et l'explication la nomme déjà
(porte R1). Correctif : `"misconceptionTag": "math.vec.symetrie-axiale-signe-mal-place"` sur les options `a` (المستقيم (OI)) et `b`
(المستقيم (OJ)). L'option « النقطة I » (ajoutée) reste muette : remplissage sans geste reconstructible — toléré.

### Contrôles sans constat
- **Fidélité** : toutes les données = transcription 2009 (A, B ; x/√2 = √2/2 ; 11133557796 ; cube ABCDSPQR et position des sommets).
  Q1 (somme des chiffres) est une étape de décomposition de la sous-question 3, Q2 une question dérivée déclarée ; options ajoutées
  (I, 18, (ACR)) sans déformation. Repère donné avec son orientation (I sur l'axe des abscisses, J sur celui des ordonnées).
- **Programme** : critères de 3, 4, 5 et de 12 enseignés au ch. 15 ; « 9 et 18 exigent une somme multiple de 9 » est donné dans
  l'explication (le ch. 15 enseigne « 9 ⟹ 3 », pas le critère de 9 lui-même, acquis antérieur) ; symétries par (OI), (OJ), O : méthode du
  ch. 18 (« مناظر A بالنسبة إلى محور الفواصل = (xA ; −yA) … ») et ch. 01 ; équation : ch. 04.
- **Indices de forme** : aucune clé strictement la plus longue ; pas d'option somme ou différence de deux autres ; pas de valeur répétée.
- **Doublons** : Q3 a le gabarit de 14/04 Q4 (« par rapport à quel élément ? ») mais données et clé différentes ((OJ) là, O ici) ;
  Q5 reprend le gabarit classique (12/15 Q6, 03/15 Q4, 12/13 Q4) avec un nombre et une clé différents : pas de doublon de fait.
- **Rendu** : toutes les lignes conformes à la source sauf « (ACQ) ✓ » (traité en M22-1) ; la ligne « 11 133 557 796 » n'est pas posée en
  bloc par `isDisplayEquation` mais s'affiche dans l'ordre (U+00A0 de classe CS).
- **Figure Q6** : vraie (cube en perspective cavalière, arêtes cachées issues de A en pointillés, sommets conformes à la transcription) ;
  [BD] surligné = la droite de l'énoncé, pas la clé ; dans le `viewBox` ; DOMPurify ne retire que l'attribut `unicode-bidi` des `<g>`
  (motif commun à tout le corpus, sans effet sur des étiquettes d'une lettre).

**Verdict partiel 22** : 6 questions, 0 clé fausse ; à reprendre : Q6 (majeur), Q2 (majeur), Q1 et Q3 (mineurs).

---

## Mission 23 — `23-examen-2010-generale-ex5-pyramide-ao-perpendiculaire-hauteur-plan-droite.json`

En-tête : « 🏛️ مناظرة 2010 · التمرين 5 ⭐⭐: هرم قاعدته مستطيل — ارتفاعه والتعامد مع مستوٍ ومع مستقيم » — conforme (notions, aucun
résultat) ; d2, `practice`, 75/15, `displayOrder` 23 : conformes. Rampe 1,2,2,2,3 : non décroissante. **Étage d2 honnête** ; la seule
question d3 (Q5) ne l'est pas aujourd'hui (deux de ses trois vraies sont annoncées par Q3 et Q4, cf. M23-1) — elle le devient avec le correctif.
Configuration recalculée : A(0,0,0), B(b,0,0), C(b,d,0), D(0,d,0), O(0,0,h).
NB : dans le fichier, les deux questions `multi` sont **Q2 et Q5** (le mandat les désignait « Q1, Q4 ») ; c'est sur elles que porte le contrôle
« nombre de bonnes réponses non déductible ».

| Q | ma réponse (aveugle) | clé du fichier | verdict | motif |
|---|---|---|---|---|
| Q1 (mcq, d1) | [OA] (d) | d | OK | (AO) ⟂ (ABD) donné ⇒ [OA] hauteur ; l'explication définit la hauteur d'une pyramide quelconque (le cours ne la définit que pour la pyramide régulière) et use de l'unicité (règle 6) |
| Q2 (multi, d2) | {a, e, f} | {a, e, f} | OK | toute paire de droites du plan passant par A convient (AB/AD, AD/AC, AB/AC) ; AB∥CD, AD∥BC et « (AB) seul » ne suffisent pas ; le nombre de bonnes réponses n'est ni annoncé ni déductible de la forme |
| Q3 (mcq, d2) | c | c | réserve | clé juste ; explication qui désigne les options par leur RANG (M23-2) ; deux options muettes ont une étiquette existante exacte (M23-3) ; distracteur d faible (M23-4) |
| Q4 (mcq, d2) | b | b | réserve | clé juste ; explication par RANG d'option (M23-2) ; étiquettes de a et c exactes ; d (double erreur, mauvais plan) muet : toléré |
| Q5 (multi, d3) | {a, d, e} | {a, d, e} | **réserve majeure** | clé juste ; mais d « (AO) ⟂ (AC) » et e « (AB) ⟂ (AOD) » sont posés comme vrais par les énoncés de Q3 et Q4 (M23-1) |

### Défauts

**Critique** : aucun (5 clés justes sur 5).

**M23-1 — majeur — fuite : Q3 et Q4 livrent deux des trois bonnes réponses de Q5 (d3).** L'énoncé de Q3 (« أيّ الحجج التالية تثبت أنّ (AO)
عمودي على المستقيم (AC) ؟ ») affirme l'option d de Q5, celui de Q4 (« … تثبت أنّ (AB) عمودي على المستوي (AOD) ؟ ») affirme l'option e,
et l'option a, « (AD) ⟂ (AOB) », en est le symétrique immédiat. En route quête (Q3, Q4 émises avant Q5) le « bilan » d3 se répond par relecture.
Correctif exact (vérifié : vraies/fausses recalculées en coordonnées, démontrables avec les règles 2, 3 et 6 du cours, aucune n'est annoncée
ailleurs, mélange « droite ⟂ plan » / « droite ⟂ droite » conservé parmi les vraies comme parmi les fausses, rendu conforme, `lot-lint` muet) :
- option `d` : `(AO) عمودي على (AC)` → `(BC) عمودي على (OB)` ;
- option `e` : `(AB) عمودي على المستوي (AOD)` → `(CD) عمودي على المستوي (AOD)` ;
- `answerKey.correct` inchangé `["a","d","e"]` ; `explanation` → :

```
الصحيحة ثلاث. (AD) عمودي على المستوي (AOB): فهو يعامد (AO) بحسب المعطيات و(AB) لأنّ ABCD مستطيل، وهما متقاطعان في A ومحتويان في (AOB). وبالطريقة نفسها (AB) عمودي على المستوي (AOD).
ومن النقطة D يمرّ مستقيم واحد عمودي على (AOD)، وهو يوازي (AB) لأنّ مستقيمين عموديين على المستوي نفسه متوازيان؛ والموازي لـ (AB) المارّ من D هو (DC)، إذن (CD) عمودي على المستوي (AOD). وبالمثل، العمودي على (AOB) المارّ من B يوازي (AD)، فهو (BC)؛ و(BC) عمودي على (AOB) في B، فهو يعامد (OB) المارّ من B.
أمّا الخاطئة فثلاث: (AC) لا يعامد (AD) لأنّ قطر المستطيل يصنع مع كلّ ضلع زاوية حادّة، فلا يكون (AC) عموديًّا على (AOD)؛ والزاوية BAC حادّة لأنّ المثلّث ABC قائم في B، فـ (AB) لا يعامد (AC)؛ والمثلّث OAC قائم في A، فزاويته عند O حادّة و(AO) لا يعامد (OC).
```
(Contrôles : normale de (AOD) ∥ (CD), normale de (AOB) ∥ (BC), (BC)·(OB) = 0 ; (AC) non ⟂ (AOD), (AB)·(AC) ≠ 0, (OA)·(OC) = h² ≠ 0.
Ni « (CD) ⟂ (AOD) » ni « (BC) ⟂ (OB) » n'existent dans les missions publiées du ch. 20. Alternative acceptable : supprimer Q5, question dérivée.)

**M23-2 — majeur — explications qui nomment les options par leur rang** (les options sont mélangées à l'affichage) : Q3 « أمّا الحجّة الأولى …
والثانية … والرابعة … », Q4 « الحجّة الأولى … والثالثة … والرابعة … ». Correctifs exacts (remplacement du seul second paragraphe) :
- Q3 : `أمّا الحجّة الأولى فخاطئة لأنّ تقاطع مستقيمين لا يعني تعامدهما. والثانية لا تكفي: العمودية على مستقيم واحد (AB) من المستوي لا تعطي العمودية على باقي مستقيماته. والرابعة خاطئة لأنّ قطر المستطيل يصنع مع كلّ ضلع زاوية حادّة.`
  → `أمّا حجّة التقاطع فخاطئة لأنّ تقاطع مستقيمين لا يعني تعامدهما. وحجّة العمودية على (AB) وحده لا تكفي: العمودية على مستقيم واحد من المستوي لا تعطي العمودية على باقي مستقيماته. وحجّة القطر خاطئة لأنّ قطر المستطيل يصنع مع كلّ ضلع زاوية حادّة.`
  (si M23-4 est appliqué, la dernière phrase devient `وحجّة المستقيمين المتوازيين (AB) و(DC) لا تكفي كذلك: المتوازيان لا يعطيان إلّا اتّجاهًا واحدًا.`)
- Q4 : `الحجّة الأولى لا تكفي … والثالثة تستعمل … والرابعة تستعمل …` (tout le second paragraphe) →
  `حجّة المستقيم الواحد (AD) لا تكفي لأنّها تستعمل مستقيمًا واحدًا فقط من المستوي (AOD). وحجّة (AD) و(BC) تستعمل مستقيمين متوازيين فلا يعطيان إلّا اتّجاهًا واحدًا، والمستقيم (BC) ليس من المستوي (AOD) أصلًا. وحجّة المثلّث OAB تستعمل المستوي (OAB) لا (AOD)، وتفترض أنّ (AB) عمودي على (OB)، والمثلّث OAB قائم في A لا في B فزاويته عند B حادّة.`

**M23-3 — mineur — Q3 : deux options muettes ont une étiquette EXISTANTE exacte** (contrairement à la déclaration « ces étiquettes manquent ») :
- `a` « (AO) و(AC) متقاطعان في A، وكلّ مستقيمين متقاطعين في الفضاء متعامدان » → `math.geo.intersection-prise-pour-perpendicularite`
  (« Se couper ne suffit pas : deux droites ne sont perpendiculaires que si l'angle formé est DROIT » ; même emploi publié en 09/29 Q1) ;
- `b` « (AC) و(AB) مستقيمان في المستوي نفسه، و(AO) عمودي على (AB) الذي يمرّ من A » → `math.esp.perpendiculaire-au-plan-deux-secantes`
  (« Être perpendiculaire à UNE droite du plan … ne suffit pas » — c'est l'erreur que l'auteur étiquette déjà en Q4 a ; l'explication la nomme : porte R1).

**M23-4 — mineur — Q3 d faible** : « قطر المستطيل عمودي على كلّ ضلع من أضلاعه » est une propriété absurde, écartée sans la notion. Correctif proposé
(vérifié : faux comme argument, la clé n'est pas la plus longue — c 72 car., d 93 —, rendu conforme) : `d` →
`(AC) مستقيم من المستوي (ABD)، و(AO) عمودي على المستقيمين المتوازيين (AB) و(DC) من هذا المستوي` avec
`"misconceptionTag": "math.esp.perpendiculaire-au-plan-deux-secantes"` (variante « deux parallèles » du libellé), et la phrase d'explication indiquée en M23-2. Cette tournure « عمودي على المستقيمين المتوازيين » est celle du `::: verifie` du cours et de 20/18 Q1 c ; elle décrit le raisonnement fautif de l'élève, pas une propriété enseignée.

### Contrôles sans constat
- **Fidélité** : ABCD rectangle, (AO) ⟂ (AB) et (AD), questions 1a (→ Q2), 1b (→ Q3), 2 (→ Q4) = transcription 2010 ; Q1 et Q5 dérivées
  (déclarées). Le passage de 1a en multi « quelles paires suffisent » élargit la sous-question sans la déformer.
- **Programme** : définition « deux sécantes en un même point » et règle 1 (droites passant par le pied) : ch. 20 ; Q2–Q4 n'emploient que cela.
- **Doublons** : 20/18 (2013 ex5) Q1 a le même schéma « quelle justification de (SA) ⟂ (ABD) » mais en QCM simple ; le multi à six paires
  (dont AD/AC et AB/AC) change l'angle ; 20/18 Q2 et Q3 établissent le même fait (droite verticale ⟂ (AC)) avec des options et des pièges
  différents (sommet de l'angle droit contre type d'argument) : voisinage d'annales, pas doublon de fait.
- **Figures** : vraies (base parallélogramme en perspective = rectangle, [OA] verticale et arêtes cachées en pointillés comme dans la
  transcription) ; Q4–Q5 marquent les angles droits OAB et OAD, qui sont des DONNÉES de ces deux énoncés ; Q1–Q3 n'en marquent aucun
  (Q2 en serait orientée) ; rien ne déborde du `viewBox` ; seul `unicode-bidi` est retiré par DOMPurify.
- **Rendu** : conforme, hors la coche « ✓ » collée à une formule isolée (constat transversal T1, fin de rapport).

**Verdict partiel 23** : 5 questions, 0 clé fausse ; à reprendre : Q5 (majeur), Q3 et Q4 (majeur, rangs d'options), Q3 (mineurs : étiquettes, d).

---

## Mission 24 — `24-examen-2012-generale-ex1-qcm-inequation-puissances-symetrie-cube.json`

En-tête : « 🏛️ مناظرة 2012 · التمرين 1 ⭐⭐: أسئلة اختيار من متعدّد — متراجحة وقابلية القسمة ونقطتان متناظرتان ومثلّث في مكعّب » — conforme ;
d2, `practice`, 75/15, `displayOrder` 24 : conformes. Rampe 1,2,2,2,3 : non décroissante. **Étage d2 honnête.** Q5 en d3 est surcotée
(mineur M24-3).

| Q | ma réponse (aveugle) | clé du fichier | verdict | motif |
|---|---|---|---|---|
| Q1 (mcq, d1) | 2x < 6 (a) | a | OK | 6x − 4x < 1 + 5 ; plan 2×2 (10x = 4x non changé de signe, −4 = −5 non changé de signe, double erreur muette) : vote terme à terme équilibré ; étiquettes exactes |
| Q2 (mcq, d2) | ]−∞ ; 3[ (b) | b | **réserve majeure** | clé juste ; plan 2×2 équilibré (bornes −∞/+∞ 2-2, valeurs 3/−3 2-2, conservé par le correctif) ; mais le mécanisme écrit pour c (« 2x < −6 ») n'est produit par aucune erreur nommée et contredit Q1 ; étiquette de c inexacte (M24-1) |
| Q3 (mcq, d2) | 14 (c) | c | OK | 2²⁰¹⁰(1 + 2 + 4) = 7 × 2²⁰¹⁰ = 14 × 2²⁰⁰⁹ ; ni 3 ni 5 en facteur ; 10 et 12 : un seul des deux critères (étiquettes exactes), 15 officiel muet |
| Q4 (mcq, d2) | (1 ; 0) (d) | d | **réserve majeure** | clé juste ; doublon de fait de 09/18 Q4 publiée (M24-2) |
| Q5 (mcq, d3) | قائم في H (b) | b | réserve | EH = a, HC = a√2, EC = a√3 ; (EH) ⟂ (HD) et (HG) sécantes en H ⇒ (EH) ⟂ (DCG) ⇒ (EH) ⟂ (HC) : démontrable par le seul cours ; c'est l'exemple résolu du cours (même triangle EHC, mêmes lettres) : d3 surcoté (M24-3) ; d muette contre l'usage du chapitre (M24-4) |

### Défauts

**Critique** : aucun (5 clés justes sur 5).

**M24-1 — majeur — Q2 : explication fausse sur le distracteur c et étiquette inexacte.** L'explication attribue ]−∞ ; −3[ à « الخطأ في إشارة
الثابت عند نقله فنكتب 2x < −6 » : or transposer −5 sans changer son signe donne 1 − 5 = −4, donc 2x < −4 et ]−∞ ; −2[ — c'est exactement
l'option c de Q1 et ce que dit l'explication de Q1. Aucune erreur unique nommée ne produit 2x < −6 ; l'étiquette
`math.alg.transposition-sans-changer-signe` de c ne décrit donc pas l'erreur exécutée. Le distracteur officiel ]−∞ ; −3[ a pourtant une cause
exécutable : en rassemblant x à droite, −6 < −2x, puis (−6) ÷ (−2) pris pour −3 avec le changement de sens ⇒ x < −3 ; d (]−3 ; +∞[) = cette
erreur plus l'oubli du changement de sens (double, muette). Correctif exact (options officielles conservées ; vérifié par calcul ; rendu conforme) :
- option `c` : `"misconceptionTag": "math.alg.transposition-sans-changer-signe"` → `"math.int.produit-signes-negatifs"` (« تخطئ في إشارة الجداء أو خارج
  القسمة … », porte R1 : l'explication ci-dessous la nomme) — ou, à défaut, c muette ;
- `explanation` : remplacer la dernière ligne
  `الخطأ الشائع: قلب اتّجاه التراجح دون سبب فنجد ]3 ; +∞[؛ أو الخطأ في إشارة الثابت عند نقله فنكتب 2x < −6 بدل 2x < 6، فنجد ]−∞ ; −3[. أمّا ]−3 ; +∞[ فتجمع الخطأين.` par
  `الخطأ الشائع: قلب اتّجاه التراجح دون سبب فنجد ]3 ; +∞[. ومن جمع حدود x في الطرف الأيمن يصل إلى −6 < −2x، ثمّ يقسم على −2 فيقلب الاتّجاه ويجد 3 > x، وهي النتيجة نفسها؛ فإن أخطأ في إشارة خارج القسمة فوجد −3 بدل 3 وصل إلى x < −3 أي ]−∞ ; −3[، وإن نسي فوق ذلك قلب الاتّجاه وجد ]−3 ; +∞[.`

**M24-2 — majeur — Q4 : doublon de fait de la mission publiée 09/18 (2025 technique) Q4.** Même tâche (centre de la symétrie qui échange deux
points dont les ordonnées valent ±2 et dont les abscisses ont pour somme 2), même clé (1 ; 0) = I, deux distracteurs identiques ((2 ; 0)
`milieu-sans-moitie`, O), même explication (milieu). Le passage « O, I ou J ? » → « coordonnées de K » ne change que l'habillage ; seuls les
radicaux diffèrent. Le gabarit voisin (« coordonnées du symétrique d'un point par rapport à un point ») est lui-même déjà publié une douzaine
de fois (09/27 Q1, 12/07 Q6, 18/07 Q3, 18/08 Q3, 18/17 Q3, 18/21 Q2…). Correctif : **écarter Q4** (précédent de la consigne : 10 Q3 et 13 Q5
écartés pour ce seul motif) **et retirer « ونقطتان متناظرتان » du titre**, qui annoncerait une notion absente : `🏛️ مناظرة 2012 · التمرين 1 ⭐⭐: أسئلة اختيار من متعدّد — متراجحة وقابلية القسمة ومثلّث في مكعّب` (le slug `…-symetrie-…` peut être corrigé tant que le fichier n'est pas publié). La mission garde 4 questions (rampe 1,2,2,3 — ou 1,2,2,2 avec M24-3) et ses trois autres sous-questions officielles.

**M24-3 — mineur — Q5 : d3 surcoté.** La question est l'exemple résolu de la section « قطر متوازي المستطيلات » du cours (« المستقيم (EH) عمودي على
(HD) وعلى (HG) … فالمثلّث EHC قائم في H ») avec les mêmes lettres : un élève qui a lu le cours répond par reconnaissance. Correctif : `"difficulty": 3` → `2`
(rampe 1,2,2,2 sans Q4, 1,2,2,2,2 avec elle ; aucun réordonnancement, la mission reste d2).

**M24-4 — mineur — Q5 d « قائم في E » muette, contrairement à l'usage du chapitre.** Les options « angle droit au mauvais sommet » portent
`math.geo.hypotenuse-mal-choisie` dans quatre missions publiées du ch. 20 (02 Q2, 03 Q6, 07 Q6, 08 Q3) et l'explication de Q5 nomme le geste
(« ولا يكون قائمًا في E لأنّ وتره سيكون [HC]، وهو ليس أطول الأضلاع » : porte R1). Correctif : option `d`
`"misconceptionTag": "math.geo.hypotenuse-mal-choisie"`.

### Contrôles sans constat
- **Fidélité** : inéquation, somme de puissances, A(1 − √3 ; −2) / B(1 + √3 ; 2), cube et tracé de [HC], [EC] en pointillés = transcription
  2012 ; Q1 est l'étape intermédiaire de la sous-question 1 ; l'ajout de « متعامد » au repère est sans effet sur le calcul de milieu.
- **Programme** : inéquations (ch. 04), puissances (ch. 16), critères de 12 et 15 (ch. 15), milieu en repère (ch. 12/18), règle « deux sécantes au
  même point » + règle 1 (ch. 20). « Ni 3 ni 5 dans 7 × 2²⁰¹⁰ » repose sur la décomposition en facteurs premiers (acquis antérieur, même argument
  publié en 12/12 Q3).
- **Étiquettes Q5** : « متقايس الأضلاع » et « متقايس الضلعين وليس قائمًا » restent muettes à juste titre (aucune étiquette ne nomme une erreur de
  longueurs dans le cube).
- **Doublons** : Q3 partage trois options {12, 14, 15} avec 12/12 Q3 (2011, 3²⁰⁰⁹ + 3²⁰¹¹, clé 15) — annales voisines qui recyclent leur cadre ;
  ici le calcul et la clé (14) diffèrent et `content:tranche` (Jaccard < 0,45, aucune paire ni gabarit pour 22–26) ne la relève pas : acceptable,
  à surveiller. La « question k après facteur commun » a bien été écartée.
- **Figure Q5** : vraie (cube conforme à la transcription, [HC] et [EC] cachés en pointillés, triangle CEH teinté = la scène, pas la clé ; l'angle
  en H dessiné ≈ 98° ne suggère pas l'angle droit) ; dans le `viewBox`.
- **Rendu** : conforme, hors coche « ✓ » collée à une formule isolée (T1) ; « 2²⁰¹⁰ = 2 × 2²⁰⁰⁹ » (chiffres et opérateurs linéaires, non isolés
  par conception du moteur) se lit dans l'ordre source de droite à gauche.

**Verdict partiel 24** : 5 questions, 0 clé fausse ; à reprendre : Q2 (majeur), Q4 (majeur, à écarter), Q5 (mineurs : étage, étiquette de d).

---

## Mission 25 — `25-examen-2017-generale-ex1-qcm-diagramme-repere-divisibilite-pyramide.json`

En-tête : « 🏛️ مناظرة 2017 · التمرين 1 ⭐⭐: أسئلة اختيار من متعدّد — مخطّط دائري وإحداثيّات منتصف وقابلية القسمة وارتفاع هرم منتظم » — conforme ;
d2, `practice`, 75/15, `displayOrder` 25 : conformes. Rampe 1,1,2,2,2,2,3 : non décroissante. **Étage d2 honnête** (Q7 en d3 justifiée :
demi-diagonale, Pythagore et simplification littérale).

| Q | ma réponse (aveugle) | clé du fichier | verdict | motif |
|---|---|---|---|---|
| Q1 (numeric, d1) | 72 | 72 | OK | 360 − 162 − 126 = 72 ; unité (degré) dite dans l'énoncé ; figure : seuls AOB et BOC sont marqués |
| Q2 (mcq, d1) | (0 ; −1) (b) | b | OK | repère (O, B, C) : B(1 ; 0), C(0 ; 1), A symétrique de C par rapport à O ; (−1 ; 0) = coordonnées échangées (étiquette exacte, porte R1) ; (0 ; 1) et (−1 ; −1) muettes |
| Q3 (numeric, d2) | 20 | 20 | OK | 72/360 = 1/5 = 20 % ; consigne « اكتب النسبة المائوية دون الرمز % » explicite ; vérification 45 % + 35 % + 20 % = 100 % juste |
| Q4 (mcq, d2) | (1/2 ; −1/2) (d) | d | réserve | M milieu de [AB] avec A(0 ; −1), B(1 ; 0) ; étiquette de b approximative (M25-2) |
| Q5 (numeric, d2) | 5 | 5 | OK | 7² = 49 → 9, 9 − 4 = 5 (vérifié : N mod 10 = 5) |
| Q6 (mcq, d2) | 15 (c) | c | réserve | N = 20172015 × 20172019 : 5 et 9 divisent N, N impair, N mod 100 = 85 ; étiquettes exactes ; le critère de 25 n'est enseigné nulle part et l'explication l'emploie sans le dire (M25-3) |
| Q7 (mcq, d3) | a√2/2 (a) | a | réserve | OA = a√2/2, SO² = a² − a²/2 ; démontrable par le cours (définition de la pyramide régulière + règle 1 + Pythagore) ; figure à l'échelle exacte de la solution (M25-1) ; distracteurs muets alors qu'une étiquette existante convient (M25-4) |

### Défauts

**Critique** : aucun (7 clés justes sur 7).

**M25-1 — mineur — Q7 : figure dessinée à l'échelle de la solution.** En perspective cavalière, les longueurs verticales et frontales sont vraies :
SO dessiné = 165 − 73,1 = 91,9 px, AB = 130 px, rapport 0,707 = √2/2 exactement ; un élève qui compare [SO] à [AB] lit la clé (les autres
options valent 0,866, 1 et 1,414). Correctif exact dans le `prompt` de Q7 (vérifié : figure vraie, SO/AB = 0,785, à égale distance de a√2/2 et
de a√3/2, rien hors du `viewBox`, étiquette « a » de [SA] à 10 px du segment comme avant) : remplacer les **7** occurrences de `73.1` (sommet S :
`M157.5 73.1 …` ×6 et `cy="73.1"`) par `63`, `y="64.1"` (étiquette S) par `y="54"`, et `x="108.5" y="119.8"` (étiquette a de [SA]) par
`x="103" y="121"`.

**M25-2 — mineur — Q4 : étiquette approximative sur b.** (1/2 ; 1/2) vient, dit l'explication, de « إهمال إشارة ترتيبة A » : (−1 + 0)/2 calculé comme
(1 + 0)/2. `math.vec.quadrant-signes-confondus` (« tu te trompes de quadrant ») décrit une lecture de quadrant, pas ce geste ;
`math.int.signe-ignore-dans-somme` (« تهمل إشارة العدد النسبي في الجمع ») le nomme exactement. Correctif : option `b`
`"misconceptionTag": "math.int.signe-ignore-dans-somme"`.

**M25-3 — mineur — Q6 : critère de 25 non enseigné, utilisé sans être dit.** Le cours du ch. 15 ne redonne que les critères de 2, 3, 4, 5
(celui de 25 est un acquis antérieur selon la fiche programme), et « رقمي آحاده وعشراته 85 » n'est pas justifié. Correctif exact (rendu conforme : la
ligne de calcul est posée en bloc LTR) — remplacer `ولا يقبل القسمة على 25 لأنّ رقمي آحاده وعشراته 85.` par :

```
ولا يقبل القسمة على 25: يقبلها عدد إذا كان العدد المكوّن من رقمَي عشراته وآحاده 00 أو 25 أو 50 أو 75. والرقمان الأخيران من N يُحسبان من الرقمين الأخيرين للعدد 20172017، وهما 17:
17² − 4 = 289 − 4 = 285
فالرقمان الأخيران من N هما 85.
```

**M25-4 — mineur — Q7 : distracteurs muets alors qu'une étiquette existante convient.** `math.alg.reponse-a-l-autre-inconnue` (« تعطي مقدارًا غير
المطلوب — المجهول الآخر أو نتيجة وسيطة ») est exactement l'erreur des trois : a√3/2 = hauteur de la face SAB, a = arête [SA], a√2 = diagonale AC
(résultat intermédiaire) ; l'explication nomme chacune (porte R1, et R2 : tout le jeu repose sur « autre grandeur de la figure ») ; précédent
publié dans le même chapitre : 20/04 Q5 étiquette ainsi la hauteur de face (a√3)/2. Correctif : `"misconceptionTag":
"math.alg.reponse-a-l-autre-inconnue"` sur `b`, `c` et `d`. (La déclaration « aucune étiquette ne convient » ne tient pas.)

### Contrôles sans constat
- **Fidélité** : 162°, 126°, secteurs 7/8/9 et position de A, B, C ; carré de centre O, repère (O, B, C), M milieu de [AB] ; 20172017² − 4 ;
  pyramide régulière d'arête de base a et SA = a = transcription 2017. Adaptations déclarées sans déformation : angle manquant (Q1) puis
  probabilité en saisie numérique (Q3) ; Q2 (A) et Q5 (chiffre des unités) sont des étapes ; options officielles (1/2 ; 0), (√2/2 ; √2/2),
  a√3/2, a√2/2, a√2, 6, 15 conservées, 12 remplacé par 18 et 25 (déclaré).
- **Programme** : probabilité = part du disque (ch. 07) ; symétrique par rapport à O et milieu (ch. 12, 18) ; différence de deux carrés
  (ch. 03) ; critères de 3, 5, 15 (ch. 15), celui de 9 appliqué dans l'explication (acquis, comme en 22) ; pyramide régulière (ch. 20).
- **Fuites** : l'explication de Q3 contient 72 (clé de Q1) et celle de Q6 le 85 (donc la clé de Q5), mais ces questions sont émises APRÈS
  celles dont elles reprennent le résultat (d1 → d2, et Q5 avant Q6 à difficulté égale) ; aucun énoncé ne livre une autre clé.
- **Doublons** : Q3 (72° → 20 %) recoupe 07/08 Q4 (72° → 20 %, QCM 30/25/20/72) ; ici l'angle se déduit de deux données et la réponse se tape :
  angle changé, pas doublon de fait. Q5–Q6 ont le gabarit de 12/15 Q5–Q6 (2021, 11 111 111² − 16, clé 15) mais d'autres options ({6, 18, 15, 25}
  contre {9, 10, 12, 15}) et une autre étape (chiffre des unités contre factorisation) : acceptable. `content:tranche` ne relève aucune paire.
- **Figures** : diagramme circulaire vrai (A à 0°, B à 162°, C à 288°, arcs de 162° et 126°, angle COA non marqué) — un diagramme circulaire est
  proportionnel par nature et l'est aussi dans le sujet officiel : la part « un cinquième » visible n'est pas un défaut ; carré et repère vrais
  (diagonales porteuses des axes, flèches en B et C, M au milieu de [AB]) ; aucun débordement ; seul `unicode-bidi` est retiré par DOMPurify.
- **Rendu** : conforme hors T1 (coche « ✓ » après une formule isolée) ; « 20 % » s'affiche « % 20 » dans la prose arabe, ordre de lecture
  conforme à la source.

**Verdict partiel 25** : 7 questions, 0 clé fausse ; à reprendre (mineurs) : Q7 (figure, étiquettes), Q4 (étiquette), Q6 (critère de 25).

---

## Mission 26 — `26-examen-2019-generale-ex1-qcm-intervalle-equation-inequation-cube.json`

En-tête : « 🏛️ مناظرة 2019 · التمرين 1 ⭐⭐: أسئلة اختيار من متعدّد — الانتماء إلى مجال ومعادلة ومتراجحة ومستقيم عمودي على مستوٍ في مكعّب » —
conforme ; d2, `practice`, 75/15, `displayOrder` 26 : conformes. Rampe 1,1,2,2,2,2 : non décroissante. **Étage d2 honnête** (deux calculs
d'amorce d1, quatre QCM d2 ; Q6 est l'application directe « arête verticale ⟂ face », d2 par l'élimination de trois plans).

| Q | ma réponse (aveugle) | clé du fichier | verdict | motif |
|---|---|---|---|---|
| Q1 (numeric, d1) | 5 | 5 | réserve | 10³/(25 × 8) = 5 ; « الأسّ » au lieu du terme du cours « الدليل » (mineur M26-2) |
| Q2 (numeric, d1) | −2 | −2 | OK | 1 − 3 = −2 ; saisie d'un négatif admise par le type `numeric` |
| Q3 (mcq, d2) | \|2π − 2\| (b) | b | réserve | 3√3 = √27 > 5 ; 4 < 2π − 2 < 5 (3 < π < 3,5) ; c = 5 exclu ; (√3 + 1)² = 4 + 2√3 > 6 ; étiquettes de c et d exactes ; a muette alors qu'une étiquette existante convient (M26-3) |
| Q4 (mcq, d2) | 20/7 (d) | d | OK | 3x = 20 − 4x ⇒ 7x = 20 ; vérification 12/7 = 12/7 juste ; 5 = distribution partielle, −20 = transposition sans changement de signe : exactes ; 20/3 (terme oublié) muette |
| Q5 (mcq, d2) | ]−∞ ; −1] (a) | a | OK | 2x ≤ (1 − √3)(1 + √3) = −2 ⇒ x ≤ −1 ; plan 2×2 équilibré (−∞/+∞ 2-2, −1/−2 2-2) ; étiquettes exactes ; remplacement du distracteur officiel ]−∞ ; √3] fondé (aucune cause exécutable) |
| Q6 (mcq, d2) | (HFG) (c) | c | réserve | (BF) ⟂ (FE) et (FG) sécantes en F ⇒ (BF) ⟂ (EFGH) ; clé et étiquettes justes ; réfutation de (ACG) hors cours (M26-1) |

### Défauts

**Critique** : aucun (6 clés justes sur 6). **Majeur** : aucun.

**M26-1 — mineur — Q6 : réfutation de (ACG) fondée sur une règle non enseignée.** « والمستوي (ACG) يحوي (CG) الموازي لـ (BF)، ومستقيمان متوازيان لا
يتعامدان » suppose qu'une perpendiculaire à un plan est perpendiculaire à TOUTES ses droites (ici (CG), qui ne passe par aucun pied) — même écart
au cours qu'en M22-1. Argument conforme : B et F ne sont pas dans (ACG) (plan diagonal x = y), (BF) ∥ (CG) ⊂ (ACG), donc (BF) ne coupe pas ce plan,
or une perpendiculaire à un plan le coupe (définition du cours). Correctif exact (rendu conforme) : remplacer
`والمستوي (ACG) يحوي (CG) الموازي لـ (BF)، ومستقيمان متوازيان لا يتعامدان.` par
`والمستوي (ACG) يحوي (CG) الموازي لـ (BF)، والنقطتان B و F ليستا منه، فالمستقيم (BF) لا يقطع هذا المستوي أصلًا، والمستقيم العمودي على مستوٍ يقطعه في نقطة.`

**M26-2 — mineur — Q1 : vocabulaire.** Le cours des puissances (ch. 16, 35 occurrences) dit « الدليل » et énonce ce même piège (« الظنّ أنّ الدليل
السالب يجعل العدد سالبًا »). Correctif : `الخطأ الشائع: الظنّ أنّ الأسّ السالب يعطي عددًا سالبًا.` → `الخطأ الشائع: الظنّ أنّ الدليل السالب يعطي عددًا سالبًا.`

**M26-3 — mineur (facultatif) — Q3 a « 3√3 » muette.** Le distracteur officiel ne se choisit que par une comparaison au jugé de 3√3 et de 5 ;
`math.num.comparaison-radical-et-entier` (« تقارن جذرًا بعدد صحيح بالتخمين: قارن مربّعَي العددين ») le nomme exactement. Correctif : option `a`
`"misconceptionTag": "math.num.comparaison-radical-et-entier"` et, dans l'explication, `العدد 3√3 يساوي √27 وهو أكبر من √25 = 5، فهو خارج المجال.` →
`العدد 3√3 يساوي √27 وهو أكبر من √25 = 5، فهو خارج المجال؛ والخطأ الشائع مقارنة 3√3 بالعدد 5 تقديرًا بدل مقارنة مربّعيهما 27 و 25.` (porte R1).

### Contrôles sans constat
- **Fidélité** : a = 3√3, b = |2π − 2|, c = 5⁻² × 2⁻³ × 10³, équation (3/5)x = (4/5)(5 − x), inéquation 2x/(1 + √3) ≤ 1 − √3, cube ABCDEFGH
  et position des sommets = transcription 2019 ; ajouts déclarés (d = (√3 + 1)², 20/3, ]−∞ ; −2], [−2 ; +∞[, (ACG)) sans déformation ; Q1 et Q2
  sont les étapes de calcul des sous-questions 1 et 3. La figure officielle épaississait le triangle HFG — c'est-à-dire la clé — : ne pas
  l'avoir reprise est juste.
- **Programme** : puissances à exposant négatif (ch. 16), identité (a − b)(a + b) (ch. 03), encadrement de π et intervalles (ch. 17), valeur absolue (ch. 19),
  équations/inéquations (ch. 04), règle 2 du ch. 20.
- **Fuites** : Q1 (5) et Q2 (−2) sont les étapes de Q3 et Q5, émises avant elles ; aucune explication ne résout une question émise après.
- **Doublons** : Q6 partage le cadre « (XY) ⟂ quel plan ? » avec 22 Q6 (même tranche) et 20/03 Q5 (publiée) ; droites, plans, clés et raisonnements
  diffèrent (arête/face ici, diagonale/plan diagonal en 22, (AB)/(ADH) en 03) : pas doublon de fait. Q3, Q4 et Q5 n'ont pas d'équivalent publié.
- **Figure Q6** : vraie (cube conforme à la transcription, [BF] surligné = la droite de l'énoncé), aucun plan désigné, dans le `viewBox`.
- **Rendu** : conforme hors T1 ; « 10³ = 5³ × 2³ » (chiffres et opérateurs linéaires, non isolés par conception) se lit dans l'ordre source.

**Verdict partiel 26** : 6 questions, 0 clé fausse ; à reprendre (mineurs) : Q6, Q1, Q3 (facultatif).

---

## T1 — constat transversal (moteur, mineur) : la coche « ✓ » collée à une formule isolée se lit AVANT la formule

`splitMathRuns` étend le run mathématique jusqu'au premier caractère arabe ou de ponctuation de prose : dans « … عمودي على (ACQ) ✓. », le run isolé
est « (ACQ) ✓ » ; affiché de gauche à droite dans l'isolat, la coche se retrouve à DROITE de la formule, donc lue avant elle en `dir=rtl`
(« … على ✓ (ACQ) »). Mesuré en Chromium sur la tranche : 22 Q6 ; 23 Q2, Q3, Q4, Q5 ; 24 Q1, Q2, Q4 ; 25 Q2, Q4, Q7 ; 26 Q2, Q3, Q5, Q6 (la coche
reste à côté de la bonne valeur : aucune ambiguïté de clé). Le même découpage touche **785 runs dans 189 fichiers publiés** de `math` : correctif
à porter au moteur (laisser un « ✓ » final, et l'espace qui le précède, hors du run, comme la ponctuation de prose depuis arena#1138), pas au
contenu. Les textes de remplacement proposés dans ce rapport n'introduisent pas ce motif ; les occurrences restantes relèvent du moteur.

## Familles muettes (seuil : 3 questions distinctes, tranche + publié)

Aucune étiquette NOUVELLE n'est nécessaire : chaque famille déclarée muette a soit une étiquette EXISTANTE exacte, soit moins de trois occurrences.
- « reconnaître axe / centre » (22 Q3) → `math.vec.symetrie-axiale-signe-mal-place` existe (M22-4).
- « sécantes ⟹ perpendiculaires » et « une seule perpendiculaire dans le plan » (23 Q3) → `math.geo.intersection-prise-pour-perpendicularite`
  et `math.esp.perpendiculaire-au-plan-deux-secantes` existent (M23-3) ; « diagonale ⟂ côtés » : 1 occurrence, à remplacer (M23-4).
- « hauteur de la face prise pour celle de la pyramide » (25 Q7) : 2 occurrences (avec 20/04 Q5), couverte par `math.alg.reponse-a-l-autre-inconnue`
  comme dans le précédent publié (M25-4).
- « angle droit au mauvais sommet » (24 Q5 d) : `math.geo.hypotenuse-mal-choisie` par l'usage du chapitre (M24-4).
- 23 Q1 (arêtes latérales prises pour la hauteur), 22 Q3 « I », 25 Q2 (0 ; 1) et (−1 ; −1), 25 Q4 (1/2 ; 0) et (√2/2 ; √2/2), 26 Q4 20/3,
  24 Q5 a et c, et les doubles erreurs voulues (23 Q4 d, 24 Q1 d, 24 Q2 d, 26 Q5 d) : remplissage, erreur ambiguë ou double — muettes à bon droit.

## Bilan

| mission | questions | clés fausses | questions à reprendre | défauts (crit. / maj. / min.) |
|---|---|---|---|---|
| 22 (2009 ex.1) | 6 | 0 | Q1, Q2, Q3, Q6 | 0 / 2 / 2 |
| 23 (2010 ex.5) | 5 | 0 | Q3, Q4, Q5 | 0 / 2 / 2 |
| 24 (2012 ex.1) | 5 | 0 | Q2, Q4 (à écarter), Q5 | 0 / 2 / 2 |
| 25 (2017 ex.1) | 7 | 0 | Q4, Q6, Q7 | 0 / 0 / 4 |
| 26 (2019 ex.1) | 6 | 0 | Q1, Q3, Q6 | 0 / 0 / 3 |
| **total** | **29** | **0** | **16** | **0 / 6 / 13** (+ T1 moteur) |

**Chiffre final : 29 questions auditées, 0 clé fausse, 16 questions à reprendre** — dont 7 pour un défaut majeur (22 Q2, 22 Q6, 23 Q3, 23 Q4,
23 Q5, 24 Q2, 24 Q4) ; les cinq étages d2/`practice` 75/15 sont honnêtes, les rampes non décroissantes, aucun titre ne livre de résultat.
Tous les textes de remplacement ont été appliqués à des copies hors dépôt puis revérifiés (clé recalculée, aucune prémisse niée, clé jamais
strictement la plus longue, `lot-lint` muet, rendu Chromium conforme, figures dans leur `viewBox`).
