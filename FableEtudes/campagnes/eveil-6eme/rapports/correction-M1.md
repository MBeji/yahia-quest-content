# Correction M1 — missions du gisement, éveil 6ᵉ (`09` 06–07, `12` 06–07, `01` 06–13)

Décisions du pilote appliquées. Aucun défaut refusé. Pas de git. Questions : m001 7, m002 8, m003 8, m004 5, m005 6, m006 6, m007 7, m008 5, m009 7, m010 5, m011 8, m012 6 (78). Aucune mission sous 4 questions : pas de coupe. `gisement.json` : `etapes` mis à jour (12 missions).

## Défauts

| défaut | sort |
| --- | --- |
| C-1 (m001, numérotation 2013) | appliqué : SVG de Q5 « الرسم 1 » ; Q4 et Q8 supprimées (M-1) |
| C-2 (m002 Q9) | appliqué (prompt sans renvoi à une figure) |
| C-3 (m003 Q9) | appliqué : SVG de l'option c et explication de l'auditeur, rendu vérifié |
| C-4 (m005 Q3, Q7 « كمّيّة ») | appliqué ; note ajoutée au prompt de Q3 avant « صِل… » (et non après le deux-points) ; étiquette de Q7 déplacée sur a, b muette |
| C-5 (m006 Q4) | appliqué : items b/c fusionnés, ids renumérotés a–d, `order` a,b,c,d |
| M-1 (m001) | appliqué : Q4, Q8 supprimées, Q6 remplacée (texte de l'auditeur) |
| M-2 (m001 Q9) | appliqué (option c concave + point sur la rétine, explication sans place d'option) |
| M-3 (m001 Q7) | appliqué |
| M-4, M-5, M-6, M-7 (m002) | appliqués : Q3 et Q5 supprimées, Q2/Q6/Q8 réécrites |
| M-8 (m003 Q1–Q3) | appliqué ; Q2 : option b supprimée, ids renumérotés a–c, clé c |
| M-9 / point 1 (réfraction) | appliqué, texte exact : `propriete`, 2ᵉ `verifie` (air → eau), puce de `resume.md` ; en plus, la figure du cours reçoit la normale « ن » pointillée et sa légende la nomme (rendu vérifié). Aucune question 01–05 ni le quiz du ch. 12 ne traite du sens de la déviation par rapport à la normale (grep « يقترب / يبتعد / الناظم » : 0) |
| rappels m003 Q7–Q9, m004 | appliqué : remplacés par « الخطّ المنقّط هو الناظم. » (m004 Q9 supprimée) |
| M-10 (m003 Q6) | appliqué (supprimée) |
| M-11, M-12 (m004) | appliqués : Q1, Q3, Q4, Q9 supprimées (5 q gardées, décision du pilote) |
| M-13, M-14, m-6 (m005) | appliqués (Q1 option d ; Q5 et Q8 supprimées ; légendes Q3/Q4 permutées, rendu vérifié) |
| M-15, M-15 bis (m006) | appliqués : Q1, Q5, Q7 supprimées, Q2 autonome avec le SVG de l'ancienne Q1 (placé après la description de la situation) |
| M-16, M-17, m-9 (m007) | appliqués. m-9 : la phrase est ajoutée à la fin de la `propriete` de « 🌡️ » du cours `01` sous la forme « وحين يسخن الهواء… » (l'amorce « حالة للانتباه » y figure déjà) |
| M-18 (m008) | appliqué |
| M-19, M-20, m-10 (m009) | appliqués |
| M-21 (m010) | appliqué |
| M-22, M-23 (devoirs) | appliqués |
| mineurs m-1…m-5, m-7, réserves | aucun correctif exigé par l'auditeur ; m-4 : id proposé ci-dessous |

## Adaptations (mes ajouts, à valider)

- m002 Q6 : j'ai retiré de l'explication « فتناسب قصر النّظر » (texte de l'auditeur) : elle livrait la clé de Q7 (verre concave = myopie).
- m006 Q3 (ex-Q3) : le prompt ne disait plus rien de la situation depuis la suppression de Q1 ; j'y ai ajouté une phrase de décor (flacon, tube dans l'eau colorée).
- m010 Q6 : la parenthèse de l'explication disait « remplacée par le cinquième » ; réécrite « remplacée par une affirmation générale ».
- m011 : titre sans « et le tirage » (la question du tirage est supprimée) ; le nom de fichier ne change pas.

## Vérifications

- Clé jamais la plus longue (tranche 0/94). Paire proche restante : m002 Q3 ↔ Q8 (Jaccard 0,57), l'objet lointain (ex-Q4) et l'objet proche (ex-Q10) : exercice parallèle voulu, même cadre, autres données ; l'auditeur l'avait accepté (m-5).
- Positions de clé sur les 87 questions touchées : a 38 %, b 22 %, c 25 %, d 15 % (avertissement non bloquant, non rééquilibré).
- Étiquettes : seuls des ids du registre ; aucune sur multi/ordering/matching.
- **Id proposé** (non créé) : `eveil.vision.pupille-selon-la-distance` — « Tu crois que la pupille change de taille selon la distance de l'objet : c'est la quantité de lumière qui la fait varier » (m002 Q8, options c et d, aujourd'hui muettes).
- Résidu à noter : m003 Q7 (ex-Q7, air → eau) et m004 Q6 sont deux fois « le rayon entre dans l'eau et se rapproche de la normale » (dessin 2017 / dessin 2009) ; l'auditeur les a gardées.

## Rendus Chromium (360 px, RTL)

Revus : m001 Q4 (« الرسم 1 », rayons derrière la rétine) et Q7 (4 plans lentille × lieu), m003 Q9 (sortie parallèle / plus penchée vers la normale / retour / continue), figure du cours `12` (normale « ن » et légendes lisibles), m005 Q3/Q4 (« إناء 2 » dans le bocal, « ماء وثلج » dessous), m007 Q1 (« ماء ملوّن » entière). Les autres figures n'ont pas changé.
**m016** (`03/exercices/07-exams-2015-2024-deux-circuits-deux-couleurs.json`, figures de Q1 et Q2 ; le fichier a 5 questions, la « Q3 » du pilote correspond à l'un de ces deux schémas) : rien de faux au rendu ; Q1 tubes coagulé/décanté cohérent avec la clé ; Q2 schémas orientés gauche → droite sur une page RTL (flèches claires, légendes « الوعاء 1/2/3/4 » lisibles). À signaler seulement : sens de lecture LTR.

## Gates (depuis `/home/user/eng-deliver`)

`content:check` ✓ · `content:qa -- --subject eveil-scientifique-6eme` ✓ (0 clé suspecte) · `content:figures:check` ✓ · `content:tranche … --chapters 09-oeil-vision,12-dhaw,01-air --fresh --strict-longest --strict-lessons` ✓ (0 recul de patron) · `content:gisement:controle -- --sources /tmp/claude-0/devoirs-snapshots/eveil-scientifique-6eme` sur `12-` et `13-` : 0 plage ≥ 8 mots ✓ · `programme:check` ✓ · prettier `--write` puis `--check` ✓.
Décision de programme renvoyée à l'humain : aucune.
