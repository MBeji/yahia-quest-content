# Re-vérification ciblée L13 (ch.09 NN30–35) — après application de l'audit v2

> 2026-10-01, 16:10Z. Arbre de travail tel quel, aucun fichier du dépôt modifié. md5 (12 car.) conformes : 30=b2e7b75c25b3, 31=2a8f1b387c4b, 32=d1dcc2faea3b, 33=59f7c96c7cdf, 34=bd562eb90f02, 35=f6a05f16ee2e. Libellés lus sur `origin/main` du corpus = **8cab736f** (avancé depuis l'audit : registre 649 → 846, +197 identifiants `bio.*`/`fr.*` seulement, aucun libellé `math.*` modifié ni retiré). `bidi.ts` = `origin/main` du moteur (96c9e5b9), identique à ma copie.

## Verdict
**0 clé fausse, 0 critique, 0 majeur nouveau.**
- 1 mineur à corriger, issu de MON v2 (M-5) : l'étiquette de 33 Q6 d (§ 3, correctif exact vérifié).
- 1 pose limite, issue de MON v2 : 33 Q3 c (§ 3). À garder ou à rendre muette, selon l'arbitrage.
- 2 mineurs acceptés sans correctif (m-a, m-b, § 6).
- 3 observations.

Le reste : **RAS**.

## 1. Re-résolution à l'aveugle et explications
- **Questions dont le texte a changé : exactement 16.** C'est vérifié par un diff complet original → actuel portant sur l'énoncé, la figure et les options.
- **Re-résolution avant lecture de la clé :** 30 Q1 b ; 31 Q4 c, Q7 c, Q8 b ; 32 Q3 c, Q7 b, Q8 c ; 33 Q3 a, Q4 c, Q5 b, Q6 c ; 34 Q1 a, Q2 b, Q3 d, Q7 b ; 35 Q8 c. **Résultat : 16/16 = clé.** La seule clé déplacée est 34 Q2 c → b, ce qui était attendu.
- **Explications changées : exactement 15** (30 Q1 ; 31 Q4, Q8 ; 32 Q7, Q8 ; 33 Q3, Q4 ; 34 Q1, Q2, Q3, Q7 ; 35 Q3, Q5, Q9, Q12).
  - Par script, 108 égalités numériques recalculées sur les 48 explications : 0 fausse.
  - À la main, les égalités symboliques et les fractions : 31 Q4 et 33 Q4 (3/3,75 = 0,8 ; 3,75/0,75 = 5), 35 Q3, Q5, Q9, et 35 Q12 (BG = BH/3, HG = (2/3) HB, (4/3) HB). Toutes justes.
  - Chaque mécanisme d'erreur produit bien la valeur de son option. Le ✓ n'apparaît jamais à côté d'un distracteur.
- **Autonomie :** chacune des 16 questions donne dans son propre énoncé (ou sa figure) toutes les valeurs qu'elle emploie.
- **Écarts de l'auteur :**
  1. **32 Q8 reformulé** : juste. Clé c = 60, car 189 000 ÷ 3150 = 60. 3150 n'est imprimé nulle part, et `nearPairs` ne trouve aucune paire Q7~Q8.
  2. **34 Q7 « رُسم مضمار سباق على تصميم… »** : juste. Le texte ne renvoie à aucun dessin absent, et `content:qa` (motif de renvoi à une figure) ne lève rien.
  3. **35 Q9 « بدل الجزء [AB] أو [AE] »** : plus exact que mon texte. c = AB/EB remplace [AE], et d = AE/EB remplace [AB] dans le rapport inversé.
  4. **35 Q12 b, étiquette `centre-gravite-milieu-mediane` gardée** : acceptable.
     - Le libellé (« Tu places le centre de gravité au milieu de la médiane ») est exactement la première voie vers 1/2.
     - La seconde voie, HG/HK = 1/2, est juste : G est le milieu de [HK], puisque K = 0, B = 1, G = 2, H = 4.
     - Une option ne porte qu'une étiquette, et celle-ci vise la notion du sujet d'origine.
  5. **Non appliqués : m-8, m-11, m-12, m-14, m-15, m-16.** Tous étaient facultatifs ou tolérés en v2, et 30 Q4 c muette est conforme à v2. Rien à redire.

## 2. Échelle
- **La glose est présente, juste et sans k² dans les cinq énoncés qui emploient l'échelle**, et dans aucun autre :
  - 31 Q8 : 1/1000 → « 1000 cm » ;
  - 32 Q7 et 32 Q8 : 1/1000 → « 1000 cm » ;
  - 33 Q6 : 1/40 → « 40 cm » ;
  - 34 Q7 : 1/10000 → « 10 000 cm », avec une espace insécable dans le nombre.
- Aucun énoncé ne contient « 100 m² », « 10 × 10 » ni « 1000 × 1000 ». Ces calculs ne figurent que dans les explications.
- **32 Q7 et 32 Q8 sont distinctes** : Q7 demande l'aire réelle ; Q8 demande l'aire réelle puis le prix (vrai d3).
- **31,5 est imprimé en Q7 et en Q8** (c'est la clé de Q6) : voir m-a.

## 3. Étiquettes
**81 posées, 21 identifiants**, tous présents dans l'arbre et sur `origin/main`. Décompte :
- **65 inchangées depuis l'original.** C'est 69 − 4 : 34 Q1 c, 34 Q2 a et 34 Q2 b ont été retirées, et 34 Q2 d a été changée.
- **14 nouvelles** (31 Q8 a, c, d ; 32 Q7 a, d ; 32 Q8 a, b ; 33 Q3 c ; 33 Q6 a, b, d ; 34 Q7 a, c, d).
- **2 re-posées** (34 Q2 c et d).

Écart avec ma copie v2 : seules manquent les 16 étiquettes en attente que j'avais posées. 33 Q1 b est un ajout de l'auteur à la liste d'attente, ce qui fait 17.

**Exactes** (libellé = erreur exécutée) :
- `reponse-a-l-autre-inconnue`, résultat intermédiaire ou autre grandeur :
  - 31 Q8 a = 7,5, périmètre du plan ;
  - 31 Q8 d = 7500, 33 Q6 a = 200 et 34 Q7 d = 240 000, résultats laissés en cm ;
  - 32 Q8 a = 6000, prix par cm² de plan.
- `puissance-de-dix-rangs-mal-comptes` : 31 Q8 c = 750, 33 Q6 b = 20 et 34 Q7 c = 24 000 (division par 10) ; 34 Q7 a = 240 (division par 1000).
- `conversion-aire-facteur-errone` (« par 100, pas par 10 : 1 m² = … 10 000 cm² ») : 32 Q7 a = 315, 32 Q7 d = 315 000 et 32 Q8 b = 600. Même pose que 08/19 Q6 c, publiée.
- 34 Q2 c = 10, `pythagore-sans-carres` (BC = 3 + 4, puis 3 + 7) ; 34 Q2 d = 28, `pythagore-racine-oubliee` (3 + 25).
- `thales-formes-melangees` sur 31 Q4 a « 3 » et 33 Q4 d « 5 » : désormais exactes, puisque MN/AD = BM/MA mêle les deux formes.

**▶ À corriger (mineur, ma faute de v2, M-5) — 33 Q6 d « 0,125 »**
- **Le défaut :** l'option porte deux erreurs.
  1. Une division au lieu d'une multiplication : 5 ÷ 40, ce que le libellé décrit exactement.
  2. L'oubli de la conversion : 0,125 est en **cm**, alors que la réponse en m serait 0,00125.
- **La règle :** une option à deux erreurs est muette. C'est aussi le traitement de 32 Q7 c « 31 500 », de même forme (mauvaise opération d'échelle et pas de conversion), et de 08/19 Q6 d « 40 », publiée.
- **Correctif exact, vérifié sur une copie de travail hors dépôt** (`/tmp/audit-l13/fix/33-…json`) :
  - **Option d :** `{"id": "d", "text": "0,125", "misconceptionTag": "math.num.operation-inverse-appliquee"}` → `{"id": "d", "text": "0,125"}`
  - **Explication de Q6 :** remplacer « أو القسمة على السلّم بدل الضرب فيه فنجد 5 ÷ 40 = 0,125. » par « أو القسمة على السلّم بدل الضرب فيه مع ترك النتيجة بالصنتمتر فنجد 5 ÷ 40 = 0,125. »
- **Contrôles faits :**
  - le texte à remplacer n'apparaît qu'une fois ;
  - seuls ces deux champs changent ;
  - les options sont inchangées, donc aucun effet sur la longueur, la somme/différence ou le vote ;
  - le rendu Chromium de 33 est identique à 760 et à 340 px.

**Limite (ma pose de v2) — 33 Q3 c, `thales-sans-verifier-parallelisme`**
- Le libellé, « Tu appliques le théorème sans vérifier que les droites sont parallèles », porte la même croyance que l'option : la configuration suffirait au parallélisme.
- Mais l'option n'« applique » pas le théorème, et la règle exige l'erreur exacte.
- Aucune étiquette existante n'est plus exacte. **Garder, ou rendre muette si l'arbitrage est strict** : il suffit de supprimer la clé `misconceptionTag` de 33 Q3 c, rien d'autre ne change.

**Les 17 en attente : toutes conviennent** (libellés lus sur `origin/main`).
- `segment-mal-choisi` (« Tu prends dans la figure un autre segment… : repère d'abord le bon triangle et ses côtés »), ×14 :
  - 30 Q7 b : HA au lieu de BH ;
  - 31 Q4 d et 31 Q5 a : MA au lieu de BM ;
  - 33 Q1 b : mauvais triangle (AMN), couvert par la seconde moitié du libellé ;
  - 33 Q4 a : BM au lieu de AM ;
  - 34 Q2 a : [AC] au lieu de [BC] ;
  - 34 Q3 a : correspondance D↔A ; 34 Q3 c : [DB] et [EA] entiers ;
  - 34 Q4 d et 34 Q5 d : AE au lieu de CE ;
  - 35 Q1 a : AB pris pour rayon ;
  - 35 Q4 b : AF au lieu de AE ;
  - 35 Q9 c et 35 Q10 a : EB au lieu de AE.
- `position-relative-ignoree`, ×3 :
  - 35 Q2 a : soustraire au lieu d'ajouter ;
  - 35 Q2 d : l'inverse ;
  - 35 Q12 d : G placé du côté de K.

**⚠ État de l'arbre changé pendant la vérification**
- **Les 17 peuvent être posées dès maintenant.** À 16:02:07Z, `content/misconceptions.json` de l'arbre a été réaligné sur `origin/main` : 846 étiquettes, modification indexée, et `segment-mal-choisi` et `position-relative-ignoree` y sont désormais. `content:qa` passe en conséquence de 10 erreurs à **0 erreur** (533 avertissements, aucun sur ch.09).
- **`math.geo.pythagore-reciproque-role` reste introuvable** : ni dans l'arbre, ni sur `origin/main`, ni dans les refs locales, ni sur les branches des PR ouvertes #594 et #607. 30 Q1 a et 33 Q1 c restent donc muettes, à raison.
- **Si son libellé n'est pas encore écrit, proposition** (même patron que `thales-reciproque-role`, compétence `math.geo.pythagore`) :
  - fr : « Tu te trompes sur le rôle de la réciproque : elle prouve qu'un triangle est rectangle à partir de ses longueurs ; quand l'angle droit est donné, c'est le théorème de Pythagore qui donne l'égalité »
  - en : « You mistake what the converse does: it proves that a triangle is right-angled from its side lengths; when the right angle is given, Pythagoras' theorem gives the equality »
  - ar : « تخطئ في دور النظرية العكسية: هي تُثبت أنّ المثلّث قائم انطلاقًا من أطواله، أمّا إذا كانت الزاوية القائمة معطاة فنظرية فيثاغورس هي التي تعطي المساواة »

## 4. Figures et rendu
**Figures**
- **35 Q8 :** le SVG est identique octet pour octet à celui de l'audit (md5 621ea12da96e). Aucune couleur ne désigne la clé : les deux hauteurs (BK) et (CA) sont à l'encre des côtés, et seul le prolongement [EB] de (BF) est en gris.
- **33 Q5 :** « 4 cm » est passé de (166 ; 194) à (120 ; 166). Le rendu Chromium le place juste au-dessus de [BC], près de C, sans collision avec les marques de parallélisme ni avec [AN].
- **34 Q2 :** la figure est inchangée et ne porte que « 3 cm » et « 4 cm », pas BC.
- **Gates de figures :** `content:figures:check` ✓ ; `check-overflow` : 31 figures, 0 texte hors viewBox.

**Rendu arabe** (ordre visuel contrôlé par programme en Chromium `dir=rtl`, à 760 et 340 px, sur 1 263 segments)
- **Énoncés et options : 0 chaîne brouillée.** Les 87 lignes d'énoncé sans mot arabe sont toutes acceptées par `isDisplayEquation`, y compris les nouvelles lignes de 34 Q2.
- Les grandeurs avec unité (« 1000 cm » et autres) sont posées en ordre RTL et se lisent juste de droite à gauche. C'est le comportement du moteur, comme dans les missions publiées.
- Les chiffres groupés le sont tous par espace insécable.
- Aucune paire de nombres séparée par la virgule arabe.
- **Seul reste m-16**, dans les explications de 31 Q8, 32 Q7, 33 Q6 et 34 Q7 : « 1 m = 100 cm » et « 1 m² = 10 000 cm² ». Accepté, non appliqué.
- Mes textes v2 de 32 Q7 et Q8 (« 1000 cm ، أي 10 m ») ne produisent plus de segment mixte.

## 5. Étages, rampes, titres, doublons, gates
- **Étages et rampes** : honnêtes et non décroissants ; ordre d'émission = ordre du fichier ; aucune fuite en avant dans la route quête.

  | Mission | Étage | Récompense | Rampe (difficulté des questions) |
  |---|---|---|---|
  | 30 | d2 practice ⭐⭐ | 75/15 | 1,2,2,2,2,2,2 |
  | 31 | d3 boss | 120/30 | 1,2,2,2,2,2,3,3 |
  | 32 | d3 boss | 120/30 | 1,2,2,2,2,3,3,3 |
  | 33 | d2 practice ⭐⭐ | 75/15 | 1,1,2,2,2,2 |
  | 34 | d2 practice ⭐⭐ | 75/15 | 1,2,2,2,2,2,3 |
  | 35 | d3 boss ⭐⭐⭐ | 120/30 | dix fois 2, puis 3, 3 |

- **Titres** : ceux de 30 (« … والوضعية النسبية لمستقيمين … ») et de 35 (« … والتناظر المركزي ») ne donnent aucun résultat. Les étoiles des titres de 30, 33 et 34 suivent l'étage.
- **Doublons**
  - `nearPairs` : 0 sur la tranche (2 132 items de maths).
  - `content:tranche --chapters 09` : aucun item de 30–35 dans les paires, les clés les plus longues ou les gabarits.
  - 34 Q2 est nouvelle : jeu d'options {7, 8, 10, 28} et parcours « AB puis BC » uniques dans tout le corpus de maths.
  - 33 Q3 c/d s'écartent de 30 Q4 c/d.
- **Indices de forme**
  - Clé strictement la plus longue : 0/48.
  - Option égale à la somme ou à la différence de deux autres : aucune.
  - Votes en plan 2×2 parfait : 30 Q1, 30 Q4, 33 Q1, 33 Q3, 34 Q1, 35 Q2, 35 Q4, 35 Q6, 35 Q8.
  - 34 Q3 et 35 Q9 : pas de majorité qui reconstruise la clé.
  - Aucune option ne nie une prémisse, et aucune n'est vraie sous les données : 34 Q1 c, 34 Q3 a, b, c (b donne 1/2 = 1/2 ≠ 2), 33 Q3 c, d et 30 Q1 d ont été recalculées.
- **Gates (lecture seule, arbre actuel)** :
  - `content:check` : code de sortie 0 ;
  - `content:qa` : 0 erreur, aucun avertissement sur 30–35 ;
  - `content:figures:check` ✓ ;
  - `check-overflow` ✓.

## 6. Ce que les correctifs ont introduit (mes textes compris)
- **33 Q6 d** : étiquette sur une option à deux erreurs, voir § 3. **Seul correctif recommandé.**
- **m-a (mineur, accepté) — 32 Q8 imprime 31,5, la clé de Q6** : effet de MON M-4, qui a remplacé l'impression de 3150 (clé de Q7).
  - La fuite ne joue qu'au donjon : dans la route quête, Q6 passe avant Q8.
  - Le nombre de restitutions relevées par le script, coïncidences numériques comprises, est inchangé (28 → 28). Les anciennes restitutions de « 5 » (clé de l'ancienne 34 Q2) dans 34 Q4, Q6 et Q7 ont disparu.
  - Même classe que 32 Q7, et que 08/19 Q7-Q8, publiées.
  - C'est inévitable si Q8 doit rester autonome sans imprimer 3150. Garder.
- **m-b (mineur, accepté) — options de Q4→Q5 proportionnelles**
  - En 31 : les options de Q5 valent exactement 3 fois celles de Q4. Les options de Q4 sont celles de l'original (l'ancienne question demandait BM/BA). MON M-11, qui fait maintenant demander MN/AD, rend seulement le lien plus visible.
  - En 33 : 3 options de Q5 sur 4 valent 4 fois celles de Q4.
  - C'est un échafaudage « rapport puis longueur », comme 08/20 Q4→Q5 publiée (où 2 options sur 4 seulement sont proportionnelles).
  - Pas de correctif : la seule retouche à une seule erreur (31 Q5 « 0,75 » → « 2 ») rendrait la clé « 2,25 » strictement la plus longue (longueurs 1, 4, 1, 1, vérifié).
- **Observations, sans correctif :**
  1. **« CE = 8 » (34 Q4–Q6)** vaut la nouvelle clé de 34 Q2, mais c'est une autre grandeur. 34 Q6 et Q7 impriment BC = 5, intermédiaire de Q2 (donjon seulement, même classe que m-13).
  2. **« 1000 cm » passe à la ligne entre le nombre et l'unité** dans les énoncés de 31 Q8 et 32 Q7 à 760 px. Ce sont mes gloses. C'est la convention du corpus : 485 « nombre + espace + unité » dans les énoncés publiés, 0 espace insécable. Cela relève donc du moteur, pas du contenu.
  3. **Titre de 35 : « فيثاغورس وعكسه »** (présent dès l'original). Il nomme la réciproque alors que l'énoncé de Q5 ne la nomme pas, ce qui écarte seulement « ليس قائمًا ». C'est une convention publiée (18/19 Q1, 09/16 Q4) : on garde. Facultatif : retirer « وعكسه ».

## Chiffre
- 16 questions re-résolues à l'aveugle : 16/16.
- 15 explications changées revérifiées, dont 108 égalités numériques sur 48 questions : 0 fausse.
- 81 étiquettes posées et 17 en attente contrôlées, plus 2 places pour la nouvelle étiquette.
- 3 figures et 31 contrôles de débordement ; 6 en-têtes.

| Catégorie | Nombre | Détail |
|---|---|---|
| Clés fausses | 0 | |
| Critiques | 0 | |
| Majeurs | 0 | |
| Mineur à corriger | 1 | 33 Q6 d, retirer l'étiquette (correctif exact au § 3) |
| Limite | 1 | 33 Q3 c, selon l'arbitrage |
| Mineurs acceptés | 2 | m-a, m-b |

**RAS pour le reste — la tranche peut partir** après le correctif de 33 Q6 d. À la livraison :
- poser les 17 étiquettes en attente, possible dès maintenant dans l'arbre ;
- créer `math.geo.pythagore-reciproque-role` pour 30 Q1 a et 33 Q1 c.
