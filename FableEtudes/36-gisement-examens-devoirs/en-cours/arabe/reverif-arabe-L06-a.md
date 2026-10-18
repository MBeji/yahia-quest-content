# Re-vérification L06-a — arabe 9ᵉ, vague 2 (m033, m034, m035, chapitre 09)

- **Base** : commit `ddae9924`, branche `wip/gisement-arabe-9eme-anciennes`.
- **Journal de l'auteur** : `auteurs-notes/ar-L06-a/CORRECTIONS.md`.
- **Audit de départ** : `audit-arabe-L06-a.md`. Les numéros Qn sont ceux des fichiers.
- **Méthode** : comparaison `git diff 65c359c8 ddae9924` sur `content/arabic/09-al-intaj-al-kitabi/`, rapportée
  aux textes exacts de l'audit. Aucun fichier de `content/` n'a été modifié, aucune opération git.

## Application des correctifs

| point | fichier · question | appliqué | constat |
|---|---|---|---|
| M1 | m035 Q5 | oui | 4 jalons. Les ids ont été renommés : a = الحجج, b = النصائح, c = الأطروحة, d = الاستنتاج. Clé `c a b d`, soit thèse → arguments → conseils → conclusion, conforme au cours. Item b et explication conformes au rapport. |
| M2 | m034 Q3 | oui | b (concession défaite, `ta3dil-ila-radd-aw-taqrir`), clé « وينهضُ بالمجتمعِ » et explication identiques au rapport. |
| M3 | m034 Q2 | oui | Quatre options concrètes et l'explication, identiques au rapport. Fuite vers Q3 : voir R1. |
| M4 | m033 Q7 | oui | Énoncé « بينَ الأمرَينِ ويُسندُهما », d muet, fin d'explication identique au rapport. |
| M5 | m035 Q6 | oui | Énoncé « أيُّ الاقتراحاتِ الآتيةِ … يصلحانِ », leurre a remplacé. |
| m1 | m033 Q9 | oui | « نعم حرّروا البلادَ » dans l'explication. |
| m2 | m033 Q2 | oui | Leurre c « الجرس … » et explication. |
| m3 | m035 Q7 | oui | l3 « تقبّلْ منّي أصدقَ التحيّاتِ … » et explication « تحيّةٌ ». |
| m6 | m033 Q3 (`matching`) | oui | r1 à r3 réécrits. Le journal dit « Q1 », c'est bien Q3 du fichier. |
| m7 | m035 Q1 | oui | a et c muets. |
| m8 | cours 09 § الإنتاج (3) | oui | Voir plus bas. |

## Re-résolution des questions touchées

| question | ma réponse | clé | verdict |
|---|---|---|---|
| m033 Q3 (`matching`) | l1-r1, l2-r2, l3-r3 | idem | OK — appariement par le sens, l'écho lexical a disparu |
| m033 Q7 | b | b | OK |
| m034 Q2 | d | d | OK, mais fuite vers Q3 (R1) |
| m034 Q3 | c | c | OK |
| m035 Q5 (`ordering`) | c a b d | idem | OK — ordre unique |
| m035 Q6 | c | c | OK |
| m035 Q7 (`matching`) | l1-r1, l2-r2, l3-r3 | idem | OK |

**m033 Q7** : grille 2×2 nette, aucune clé par union de moitiés (d n'emprunte aucun mot à b).

| option | argument sur le danger | invitation à la coexistence |
|---|---|---|
| b (clé) | oui | oui |
| d | oui (« العقوبة ») | non |
| a | non (ordres) | oui |
| c | non | non |

**m034 Q2**
- a rejoint le frère.
- b rejette toute sa position.
- c parle d'un bénéfice du projet hors de la consigne.
- d donne le rôle des arts pour les jeunes.
- La clé ne recopie plus la consigne.

**m034 Q3**
- b concède puis défait la concession (« الفنَّ كلَّه يلبّي كلَّ ما يطلبُه الشبابُ »).
- c concède puis corrige avec « غيرَ أنّ ».
- Il n'y a plus de discriminant de connecteur commun avec m015 Q3 ni avec m013 Q4.

**m035 Q5** : thèse d'abord, selon le cours (« لا مقدّمةَ منفصلةَ »). Les conseils viennent après les arguments,
comme le dit l'étiquette « المبنيّةُ على الحججِ ». La conclusion ferme. L'item b ne fuit plus vers Q4 : il n'y a
plus « التدريجيّ ».

**m035 Q6**
- d : la clôture menace.
- a : l'ouverture est froide et la clôture autoritaire.
- b : il n'y a pas de clôture.
- L'énoncé ne contient plus de duel.

**m035 Q7** : l3 est une salutation de clôture. Elle ne reprend plus la clôture de la clé de Q6.

**Indices de forme** (longueurs sans signes de vocalisation) :
- m033 Q7 : a 82, b 78, c 70, d 77 ;
- m034 Q2 : a 74, b 81, c 70, d 78 ;
- m034 Q3 : a 81, b 93, c 92, d 79 ;
- m035 Q6 : a 102, b 84, c 89, d 110.

Aucune clé n'est strictement la plus longue. Le vote par composantes ne reconstruit aucune clé.

## Fuites — un constat

**R1 (mineur) — m034 Q2 → Q3.** Le défaut vient de mes propres correctifs M2 et M3.
- L'explication de Q2 dit : « والقولُ إنّ كلَّ ما يُعرَضُ من فنٍّ يلبّي حاجاتِ الشبابِ يردُّ موقفَه كلَّه بدلَ
  تعديلِه ».
- C'est exactement ce que fait la seconde moitié du leurre b de Q3 (« غيرَ أنّ الفنَّ كلَّه يلبّي كلَّ ما يطلبُه
  الشبابُ »).
- Les deux questions sont d2, et Q2 précède Q3 sur la route. Un élève qui a lu l'explication de Q2 écarte b,
  et Q3 se réduit à une seule option restante (a et d tombent déjà par « لا ردَّه كلَّه »).

Correctif proposé, vérifié : on change le leurre b de **Q2**, la clé reste `d`.
- b → « استهزاؤُكَ بالمشروعِ دليلٌ على أنّكَ لا تفهمُ الفنَّ أصلًا، فلا صوابَ في شيءٍ من قولِكَ يا أخي ».
  Étiquette `arabe.hijaj.dahd-bila-dalil`, dont le libellé dit : réfuter en visant la personne.
- Dans l'explication, remplacer « والقولُ إنّ كلَّ ما يُعرَضُ من فنٍّ يلبّي حاجاتِ الشبابِ يردُّ موقفَه كلَّه
  بدلَ تعديلِه » par « والقولُ إنّ الأخَ لا يفهمُ الفنَّ ولا صوابَ في شيءٍ من قولِه يجرّحُه ويردُّ موقفَه كلَّه
  بدلَ تعديلِه ».
- Longueurs : a 74, b 80, c 70, d 78. La clé n'est pas la plus longue.
- Le leurre n'emprunte rien à Q3 et ne redit pas m012 Q3 a (« كلامُكَ ساذجٌ »).

Je n'ai trouvé aucune autre fuite :
- la ligne de cours « اختمْها بتحيّةٍ أو دعاءٍ » enseigne la règle de Q6 sans en recopier une option ;
- l'exemple « الماءُ موردٌ نادرٌ … » n'est pas une option de m035.

## Ligne de cours m8

- **Texte** : identique au rapport. Il est inséré à la l. 833, dans le bloc `::: methode` du § « ✍️ الإنتاجُ (3) »,
  après la « حالةٌ حدّيّةٌ » existante. Langue correcte, aucune clé recopiée. Pas de puce au résumé : c'est
  accepté, la puce était facultative.
- **Rendu** (`renderLesson`, lang `ar`, Chromium 340 px avec `src/styles.css`) :
  - « حججًا ونصائحَ », « لماذا؟ » et les guillemets s'affichent dans le bon ordre RTL ;
  - les deux paragraphes « حالةٌ حدّيّةٌ » et « حالةٌ حدّيّةٌ ثانيةٌ » s'affichent **à la suite**, sans saut de
    paragraphe ;
  - la cause est dans le moteur, pas dans la ligne : après une liste numérotée dans un bloc typé, le moteur
    émet « `<p></ol></p>` » et laisse les paragraphes suivants hors de `<p>`. Le même défaut existe déjà dans ce
    cours, dans le bloc `propriete` de la l. 43, qui contient deux paragraphes ;
  - la lecture reste possible, puisque l'étiquette en gras ouvre la seconde phrase. Réserve à transmettre au
    moteur, sans correctif de contenu exigé dans ce lot.

## Gates (`/home/user/eng-ar`, lien `content` → `wt-ar2`)

- `content:check` : rc 0 (120 matières, 29 928 questions). Les états transitoires de L06-b au chapitre 10 ont
  été ignorés.
- `content:qa:strict` : 0 erreur, aucun avertissement sur `arabic/09`.
- `content:tranche -- --subject arabic --chapters 09` :
  - 0/86 clé strictement la plus longue ;
  - positions de clé 22/26/26/27 % ;
  - 0 paire proche ;
  - 0 candidat gabarit.
- **Rendu Chromium `dir=rtl`** des questions modifiées (m033 Q3, Q7 ; m034 Q2, Q3 ; m035 Q5, Q6, Q7) :
  correct, aucun débordement.

## Verdict

**Conforme sous réserve d'un correctif mineur.**
- M1 à M5 sont appliqués et vérifiés, de même que m1, m2, m3, m6, m7 et m8. Aucune clé fausse.
- Reste **R1**, une fuite de m034 Q2 vers Q3 introduite par mes propres correctifs. Correctif exact donné
  ci-dessus, à appliquer.
- Une fois R1 appliqué, le lot peut être publié sans nouvel audit, avec un simple contrôle de diff.
- Réserve pour le moteur : les paragraphes qui suivent une liste dans un bloc typé ne sont pas séparés.

## Verdict du pilote (2026-10-18)

R1 appliqué par le pilote (m034 Q2 : leurre b et explication), clé `d` inchangée ; gates verts. **L06-a prêt à livrer.**
