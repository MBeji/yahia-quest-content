# Audit L06-a — arabe 9ᵉ, vague 2 (m033, m034, m035, chapitre 09)

Auditeur indépendant. Grille : `gisement-auditeur.md` + `prompt-francais-auditeur.md`, avec les substitutions de
`prompt-arabe-auditeur-v2.md`. Skills chargés dans l'ordre : `content-audit`, puis `prof-arabe-9eme`.
Arbre : `/home/user/wt-ar2/content/arabic/09-al-intaj-al-kitabi/exercices/` (branche
`wip/gisement-arabe-9eme-anciennes`, commit `65c359c8`). Fichiers :
`14-examens-2005-2013-hiwar-hijaji-hujaj-at-tarafayn.json` (m033), `15-examens-2006-2018-ta3dil-al-mawqif-fi-al-hiwar.json`
(m034), `16-examens-2011-2017-technique-hujaj-wa-nasa2ih.json` (m035). Aucune note d'auteur L06 n'existe dans
`auteurs-notes/`. Aucun fichier audité n'a été modifié.

**Numérotation.** Les numéros « Qn » de ce rapport sont ceux du **fichier**, qui diffèrent de ceux de la carte.
- m033 : fichier Q1 = carte Q2, Q2 = carte Q9, Q3 = carte Q1, Q4 = carte Q3, Q5 = carte Q5, Q6 = carte Q8,
  Q7 = carte Q4, Q8 = carte Q6, Q9 = carte Q7.
- m034 : fichier Q1 = carte Q2, Q2 = carte Q1 (écart), Q3 = carte Q3, Q4 = carte Q8, Q5 = carte Q4,
  Q6 = carte Q5, Q7 = carte Q6, Q8 = carte Q7.
- m035 : même ordre que la carte.

## Gates

- `content:check` : vert (120 matières, 29 929 questions).
- `content:qa:strict` : 0 erreur. Aucun avertissement sur `arabic/09`.
- `content:tranche -- --subject arabic --chapters 09` : 0/86 clé strictement la plus longue ; positions de clé
  22/26/26/27 % ; 0 paire proche ; 0 candidat gabarit.
- `isolateLtrRuns` : aucune chaîne des trois fichiers n'est modifiée (pas de séquence LTR hors années).
- **Chromium `dir=rtl`** (chromium-1194, 340 px) :
  - rendus vérifiés : les trois titres, m033 Q3 (`matching`) et Q8 (`ordering`), m034 Q8 (`ordering`),
    m035 Q5 (`ordering`) et Q6, ainsi que les chaînes de remplacement proposées ci-dessous ;
  - ordre logique conservé ; « 2005–2013 » se lit correctement en RTL ; guillemets « » et « ؛ » sont à leur
    place ;
  - aucun débordement : `scrollWidth` = 360 pour une fenêtre de 360.

## m033 — حوار حجاجيّ بحجج الطرفين (d3, boss 120/30, 9 questions)

| Q | type | ma réponse | clé | verdict | motif |
|---|---|---|---|---|---|
| 1 | qcm | c | c | OK | موقف + تبرير en phrase ; leurres généralisation / thèse du narrateur / titre |
| 2 | qcm | b | b | réserve | clé juste ; leurre c recyclé d'une mission publiée (m2) |
| 3 | matching | l1-r1, l2-r2, l3-r3 | idem | réserve | appariement lexical (m6) |
| 4 | multi | a, b, e | a, b, e | OK | c refus sans raison ; d, f répliques du narrateur |
| 5 | multi | a, b, d | a, b, d | OK | frontière nette (voir ci-dessous) |
| 6 | qcm | d | d | OK | seul plan où le père argumente après la plainte |
| 7 | qcm | b | b | **MAJEUR** | gabarit de m012 Q3 ; énoncé « بينَ ذلك » (M4) |
| 8 | ordering | c a e b f d | idem | réserve | ordre unique ; même squelette que m012 Q5 et 09/02 Q4 (m9) |
| 9 | qcm | d | d | mineur | l'explication cite « حقًّا » alors que l'option dit « نعم » (m1) |

- **Q5 (2011), frontière « argument du père » contre « argument du narrateur » : indiscutable.**
  - a, b et d restreignent le rôle de la femme à la famille, en accord avec « عَدَّ ذَلِكَ تَجَاوُزًا لِدَوْرِ الْمَرْأَةِ ».
  - c (droit égal) et e (Constitution) défendent la thèse du narrateur.
  - f (les affiches) est hors sujet.
  - « العمل النيابي » (b) correspond bien à « الاِنْتِخَابَاتِ التَّشْرِيعِيَّةِ » de la transcription.
  - Trois clés sur six : rien ne laisse deviner leur nombre.
- **Q9 (2007), complément contre redite et contradiction : la frontière tient.**
  - a contredit l'éloge (il déprécie les martyrs).
  - b redit l'éloge sans rien ajouter : avis insuffisant, mais pas faux. Le piège de la carte est respecté.
  - c rejette sur l'État seul le devoir que fixe la consigne.
  - d concède (« نعم حرّروا البلادَ ») puis ajoute « حفاظ … ودعم ». C'est la seule option qui complète l'éloge
    sans le défaire.
  - Défaut : l'explication cite une concession absente de l'option (m1).
- **Q7, écart à la carte Q4 : l'écart est insuffisant.**
  - L'auteur a remplacé « simple redite de la thèse » par « ordres sans argument », pour s'éloigner de m012.
  - Les quatre rôles restent pourtant ceux de m012 Q3 : blâme (c), approbation du camarade (d, ≈ m012 Q3 b),
    absence d'argument (a), argument général (b).
  - La question redit donc m012 Q3 sur un autre sujet. Correctif en M4 : une vraie grille 2×2 propre à la
    double exigence de 2013 (avertir des dangers ET inviter à la coexistence).
- **Fidélité des citations** : 2005, 2007, 2011 et 2013 sont conformes aux transcriptions, mot pour mot.
- **Étiquettes** : toutes exactes (Q1 a/b/d, Q2 a, Q6 a/b, Q7 a/c/d, Q9 a). Aucune sur `multi`, `ordering` ou
  `matching`. Si M4 est appliqué, la nouvelle option d reste muette.

## m034 — تعديل الموقف في الحوار (d3, boss 120/30, 8 questions)

| Q | type | ma réponse | clé | verdict | motif |
|---|---|---|---|---|---|
| 1 | qcm | a | a | réserve | même cadre que m012 Q2 et 09/04 Q3 ; voulu par la carte (m9) |
| 2 | qcm | d | d | **MAJEUR** | la clé recopie la consigne ; gabarit de m015 Q1 conservé (M3) |
| 3 | qcm | c | c | **MAJEUR** | discriminant « غيرَ أنّ » contre connecteur de conclusion = m015 Q3 et m013 Q4 (M2) |
| 4 | qcm | d | d | réserve | même cadre que m015 Q4 ; voulu par la carte (m9) |
| 5 | qcm | b | b | OK | la condition « إذا أحسن المرء استثمارها » est gardée ; d pose une condition étrangère |
| 6 | multi | a, b, c | a, b, c | OK | d rejette tout, e approuve tout, f est hors sujet |
| 7 | qcm | d | d | réserve | même cadre que m015 Q4 et m034 Q4 (m9) |
| 8 | ordering | c a e b f d | idem | OK | ordre unique ; la concession et la correction précèdent les arguments (cours l. 775) |

- **Q3, connecteur de rectification contre « إذن » : la frontière est indiscutable**, mais la question est un
  doublon.
  - Le cours enseigne la différence l. 498–507 : « غيرَ أنّ » marque le استدراك, « إذن » le استنتاج.
  - « قد تكونُ بعضُ الأعمالِ … بعيدةً …، إذن فالفنُّ يرقى » est illogique : b est indéfendable et la clé est
    juste.
  - Ce discriminant est cependant déjà testé deux fois au même chapitre :
    - m015 Q3 (`10-…`), « قد يكونُ … غيرَ أنّ » contre « بناءً على ذلك » ;
    - m013 Q4 (`08-…`), « قد يبدو … غيرَ أنّ » contre « وخلاصةُ القولِ » ou « ومعنى ذلك ».
  - La carte prévient pourtant : « une question qui redirait une de m015 sur un autre sujet est un doublon ».
  - Correctif en M2 : remplacer le leurre « إذن » par une concession qui se défait. C'est le piège propre au
    dialogue d'تعديل que nomme la carte : « arguments qui ne défont pas la concession ».
- **Q2, écart à la carte Q1 : écart justifié dans son principe, remplacement à reprendre.**
  - La carte Q1 (« ce qu'exige تعديل موقفه ») redisait m015 Q1 mot pour mot. Il fallait s'en écarter.
  - Le remplacement garde cependant le cadre de m015 Q1 au niveau des catégories : accepter tout, rejeter tout,
    hors sujet, clé.
  - Sa clé recopie le texte de la consigne citée dans l'énoncé (« تبرزُ دورَ الفنونِ في الرقيِّ بالنشءِ
    والنهوضِ بالمجتمعِ »). C'est une consigne qui fixe la réponse.
  - Correctif en M3 : des arguments concrets, la clé paraphrasée.
- **Graphie « أَخَاكَ » (2018 G) : ce n'est pas une coquille.** Dans « مَا إِنْ بَلَغَ أَخَاكَ عَزْمُ أَحَدِهِمْ »,
  le sujet est « عَزْمُ » et « أَخَاكَ » est un مفعول به منصوب. La graphie est juste et doit être citée telle quelle.
  Le rapport de l'auteur n'a pas à la signaler comme une faute.
- **Citations** : 2006, 2008, 2018 G et 2018 T sont conformes. « انْقُلِ » (2018 G) suit la transcription,
  qui ne porte pas de ضمّة sur l'alif.
- **Étiquettes** : exactes. `haqiqa-ka-qadiyya` en Q4 c (description donnée pour une thèse) est acceptable.
  Q3 b reçoit `arabe.hijaj.ta3dil-ila-radd-aw-taqrir` si M2 est appliqué.

## m035 — تحرير فقرة: حجج ونصائح (d2, practice 75/15, 9 questions)

| Q | type | ma réponse | clé | verdict | motif |
|---|---|---|---|---|---|
| 1 | qcm | b | b | mineur | étiquettes a et c inexactes (m7) |
| 2 | multi | a, c, d | a, c, d | OK | frontière nette (voir ci-dessous) |
| 3 | qcm | a | a | OK | — |
| 4 | qcm | c | c | réserve | fuite depuis Q5 b « الإقلاع التدريجيّ » (corrigée par M1) |
| 5 | ordering | c a e b d | idem | **MAJEUR** | clé contraire au cours (M1) |
| 6 | qcm | c | c | **MAJEUR** | duel « الزوجَينِ الآتيَينِ » pour quatre options ; leurre a morbide (M5) |
| 7 | matching | l1-r1, l2-r2, l3-r3 | idem | mineur | fuite vers Q6 (formule de clôture, m3) |
| 8 | qcm | d | d | OK | registre de la demande |
| 9 | multi | a, b, f | a, b, f | OK | c porte sur la personne, d sur l'institution, e contredit la demande |

- **Q2, frontière « argument » contre « conseil » : indiscutable avec la définition de l'énoncé.**
  - L'énoncé définit les deux : la الحجّة répond à « لماذا؟ », la النصيحة est « توجيه إلى ما ينبغي فعله ».
  - a, c et d donnent une raison.
  - b et f sont des impératifs.
  - e, « من الأفضلِ تأجيلُ … », est déclaratif par la forme mais conseil par le sens. La définition le tranche
    et l'explication le dit (« ولو بدا بعضُها بصيغةِ الخبرِ »).
  - c (« من يشتري كلَّ ما يعرضُه الإشهارُ ينفقُ … ») est la plus proche de la frontière. Elle énonce une
    conséquence, donc une raison : clé recevable.
- **Q6, registre de la lettre : la frontière tient.**
  - c et d ont la même ouverture amicale.
  - d se clôt sur une menace (« سيصيبُكَ مكروهٌ »), qui contredit la visée (protéger le jeune homme).
  - a est grossier, b n'a pas de clôture.
  - « أخي العزيزَ » est bien vocalisé : المنادى المضاف est منصوب تقديرًا et son نعت est منصوب.
  - Défauts : la langue de l'énoncé et le leurre a (M5).
- **Notion « نصيحة » : la définition dans l'énoncé suffit pour l'autonomie ; une ligne de cours est recommandée**
  (m8).
  - La définition figure en Q2, Q4 et Q7.
  - Q3 et Q5 emploient le mot sans le définir, mais s'y résolvent sans lui : la clé de Q3 se reconnaît comme
    « حجّة », et les étiquettes de Q5 décrivent leur contenu.
  - Le cours 09 ne contient ni « نصيحة » ni « نصائح » ni « رسالة ». Les manques recoupent trois sessions
    (2012 T, 2016 T, 2017 T) et touchent six questions sur neuf, plus les conventions de la lettre (Q6, Q7).
  - Recommandation : une « حالة حدّيّة » dans § « الإنتاج (3) ». Le texte est en m8.
- **Citations** : 2011 T, 2012 T, 2016 T et 2017 T sont conformes. 2011 T ne demande pas de « نصائح ». La
  mission ne lui en prête pas : Q8 et Q9 portent sur le registre et les مبرّرات. Correct.

## Défauts classés

### Critiques — 0

Aucune clé fausse : 26 questions re-résolues à l'aveugle, 26 accords.

### Majeurs — 5

**M1. m035 Q5 (`ordering`) — la clé contredit le cours ; ordre non unique.**
- La clé place c (« جملةٌ تذكرُ أنّ الرجلَ ما زال يدخّنُ … ») avant a (la thèse).
- Le cours 09 § « الإنتاج (3) » enseigne le contraire : « فقرةٌ واحدةٌ: لا مقدّمةَ منفصلةَ فيها », et « جملةُ
  الأطروحةِ تفتتحُ الفقرةَ ». Les missions publiées m017 Q3 et Q7 et 09/05 Q5 suivent aussi le cours.
- Un élève qui applique le cours met a en tête. Q5 b annonce en plus « الإقلاع التدريجيّ », qui donne la clé de
  Q4.

Correctif :
- Supprimer l'item `c`.
- `answerKey` → `{"order": ["a", "e", "b", "d"]}`.
- Item b → « النصائحُ المبنيّةُ على الحججِ: ما ينبغي أن يفعلَه الرجلُ ليتركَ التدخينَ ».
- Explication → « الفقرةُ الحجاجيّةُ كتلةٌ واحدةٌ لا مقدّمةَ منفصلةَ فيها، فتفتتحُها جملةُ الأطروحةِ. وبعدَها تأتي
  الحججُ، ثمّ النصائحُ لأنّها تُبنى على الحججِ فلا تسبقُها، وتُختَمُ الفقرةُ باستنتاجٍ يؤكّدُ الأطروحةَ ويدعو
  إلى العملِ بها. »
- Vérifié : ordre unique, pas de fuite vers Q4, rendu Chromium correct.

**M2. m034 Q3 — doublon de discriminant avec m015 Q3 et m013 Q4.**

Correctif :
- b → « قد تبعدُ بعضُ الأعمالِ الفنيّةِ عن اهتماماتِ الشبابِ يا أخي، غيرَ أنّ الفنَّ كلَّه يلبّي كلَّ ما يطلبُه
  الشبابُ », étiquette `arabe.hijaj.ta3dil-ila-radd-aw-taqrir`.
- c (clé) → « قد تبعدُ بعضُ الأعمالِ الفنيّةِ عن اهتماماتِ الشبابِ يا أخي، غيرَ أنّ الفنَّ يرقى بالنشءِ وينهضُ
  بالمجتمعِ ». « يشدُّ المجتمعَ » est peu idiomatique et reprenait m013.
- Explication → « التعديلُ في الحوارِ يبدأُ بإقرارٍ بالصوابِ الجزئيِّ ثمّ استدراكٍ بأداةٍ مثلِ «غيرَ أنّ» يصحّحُ
  الخللَ دونَ أن يهدمَ ما أُقِرَّ به. وذلك في الردِّ الذي أقرَّ ببعدِ بعضِ الأعمالِ ثمّ بيّنَ أنّ الفنَّ يرقى
  بالنشءِ وينهضُ بالمجتمعِ. أمّا النفيُ القاطعُ فيردُّ الموقفَ كلَّه، وأمّا موافقةُ الأخِ على كلِّ ما قالَ
  فتقبلُه كلَّه، وأمّا الردُّ الذي يجعلُ الفنَّ كلَّه يلبّي كلَّ ما يطلبُه الشبابُ بعدَ الإقرارِ ببعدِ بعضِه
  فينقضُ إقرارَه بنفسِه ويعودُ ردًّا للموقفِ كلِّه. »

Vérifié :
- longueurs sans signes : a 81, b 93, c 92, d 79. La clé n'est pas strictement la plus longue.
- Le vote par composante ne désigne pas la clé : « كلّ » apparaît en a et b, « يرقى » seulement en c.
- b est indéfendable : il se contredit.
- Aucune fuite vers Q4–Q8.

**M3. m034 Q2 — la clé recopie la consigne citée ; le cadre de m015 Q1 demeure.**

Correctif : énoncé inchangé ; options et explication réécrites, la clé reste `d`.
- a → « الشبابُ اليومَ لا يهتمّونَ إلّا بهواتفِهم يا أخي، فلا جدوى من دارٍ للفنونِ في حيِّنا », étiquette
  `arabe.hijaj.ta3dil-ila-radd-aw-taqrir`.
- b → « كلُّ ما يُعرَضُ من فنٍّ اليومَ يلبّي حاجاتِ الشبابِ ومطامحَهم، فلا صوابَ في شيءٍ من قولِكَ يا أخي »,
  étiquette `arabe.hijaj.ta3dil-ila-radd-aw-taqrir`.
- c → « تشييدُ الدارِ يوفّرُ لعمّالِ البناءِ في حيِّنا شغلًا أشهرًا عديدةً، فهو مشروعٌ نافعٌ », muette.
- d (clé) → « في دارِ الفنونِ يتعلّمُ أطفالُ الحيِّ الرسمَ والموسيقى، فتتهذّبُ أذواقُهم وينفعونَ مجتمعَهم ».
- Explication → « تطلبُ التعليمةُ تعديلَ موقفِ الأخِ بإبرازِ دورِ الفنونِ في الرقيِّ بالنشءِ والنهوضِ بالمجتمعِ،
  فالحجّةُ الصالحةُ تبيّنُ ما تقدّمُه دارُ الفنونِ للناشئةِ: يتعلّمُ الأطفالُ الرسمَ والموسيقى فتتهذّبُ أذواقُهم
  وينفعونَ مجتمعَهم، فيصحّحُ بها الراوي قولَ أخيهِ. أمّا القولُ إنّ الشبابَ لا يهتمّونَ إلّا بهواتفِهم فينضمُّ
  إلى استهزاءِ الأخِ، والقولُ إنّ كلَّ ما يُعرَضُ من فنٍّ يلبّي حاجاتِ الشبابِ يردُّ موقفَه كلَّه بدلَ تعديلِه،
  وأمّا تشغيلُ عمّالِ البناءِ فنفعٌ للمشروعِ لا صلةَ له بدورِ الفنونِ الذي طلبتِ التعليمةُ إبرازَه. »

Vérifié :
- longueurs : a 74, b 81, c 70, d 78. La clé n'est pas la plus longue.
- Aucune option ne recopie la consigne.
- Pas de fuite vers Q3 : l'ancienne phrase « دونَ أن يُنكرَ كلَّ ما فيه » est retirée.

**M4. m033 Q7 — redit m012 Q3 ; énoncé « يجمعُ بينَ ذلك ».**

Correctif :
- Fin de l'énoncé : « أيُّ الردودِ الآتيةِ يجمعُ بينَ ذلك بحجّةٍ عامّةٍ؟ » → « أيُّ الردودِ الآتيةِ يجمعُ بينَ
  الأمرَينِ ويُسندُهما بحجّةٍ عامّةٍ؟ ».
- d → « من رفعَ يدَه على زميلِه عرّضَ نفسَه للعقوبةِ وخسرَ ثقةَ أساتذتِه، فاحذرْ أن تعودَ إلى ذلك ». Retirer son
  étiquette : l'option a un argument, mais pas d'invitation à la coexistence.
- Fin de l'explication : « والردُّ الذي يبيحُ الردَّ القاسيَ يدعمُ موقفَ الصديقِ بدلَ أن يعدِّلَه. » → « والردُّ
  الذي يخوّفُه من العقوبةِ ينبّهُ إلى خطرٍ لكنّه لا يدعوه إلى التعايشِ السلميِّ، فلا يبلغُ إلّا نصفَ ما تطلبُه
  التعليمةُ. ».

On obtient une grille 2×2 :

| option | argument sur le danger | invitation à la coexistence |
|---|---|---|
| b (clé) | oui | oui |
| d | oui | non |
| a | non (ordres) | oui (« عاملْ زملاءَكَ بالتي هي أحسنُ ») |
| c | non | non (muette) |

Vérifié : longueurs a 82, b 78, c 70, d 77. d n'emprunte aucun mot à b, donc pas de clé par union de moitiés.

**M5. m035 Q6 — duel incohérent et leurre morbide.**
- Énoncé : « أيُّ الزوجَينِ الآتيَينِ يصلحُ افتتاحًا للرسالةِ وختامًا لها؟ » met au duel quatre options.
  → « أيُّ الاقتراحاتِ الآتيةِ يجمعُ افتتاحًا وختامًا يصلحانِ للرسالةِ؟ ».
- a souhaite la mort du jeune homme (« كنتُ أنتظرُ خبرَ موتِك ») : leurre absurde et déplacé pour l'âge.
  → « افتتاحٌ: «إلى الشابِّ المصابِ، أكتبُ إليكَ لأنّ أمَّكَ ألحّتْ عليَّ»؛ ختامٌ: «هذا ما عندي، وعليكَ أن تفهمَ
  ولا تناقشْني» ».
- Explication : « وليس يناسبُها افتتاحٌ فظٌّ أو ختامٌ آمرٌ » reste juste.
- Vérifié : longueurs a 102, b 84, c 89, d 110 ; rendu Chromium correct.

### Mineurs

- **m1. m033 Q9, explication.** Elle cite une phrase absente de l'option. « («حقًّا حرّروا البلادَ») » →
  « («نعم حرّروا البلادَ») ».
- **m2. m033 Q2, leurre c.** « وكانتْ ساحةُ المعهدِ واسعةً تحيطُ بها أشجارٌ عاليةٌ … » reprend le leurre c de
  09/06 Q5 (« كانتْ ساحةُ المعهدِ واسعةً … وأشجارُها عاليةٌ »).
  - c → « وكانَ الجرسُ قد رنَّ منذُ دقائقَ، والتلاميذُ يتّجهونَ إلى أقسامِهم مسرعينَ ».
  - Explication : « ووصفُ الساحةِ إطارٌ لا ينقلُ الكلامَ » → « ووصفُ رنينِ الجرسِ وحركةِ التلاميذِ إطارٌ لا ينقلُ
    الكلامَ ».
  - Remarque : la clé b reste l'option la plus courte (20 caractères). La forme est inhérente à la notion
    (verbe de parole et deux-points). Réserve, pas de correctif.
- **m3. m035 Q7 → Q6, fuite.** l3 « أسألُ اللهَ أن يديمَ عليكَ نعمةَ الصحّةِ، ودمتَ سالمًا » reprend la clôture de
  la clé de Q6.
  - l3 → « تقبّلْ منّي أصدقَ التحيّاتِ، وإلى لقاءٍ قريبٍ يا صديقي ».
  - Explication : « والثالثةُ دعاءٌ يُختَمُ به الكلامُ » → « والثالثةُ تحيّةٌ يُختَمُ بها الكلامُ ».
- **m4. m035 Q5 b → Q4, fuite.** Traitée par M1.
- **m5. m035 Q2 → Q3, fuite légère.** L'explication de Q2 classe « شراءُ الضروريِّ أوّلًا وتأجيلُ الكماليّاتِ »
  comme conseils, ce qui écarte Q3 d. Ce leurre s'élimine de toute façon (impératif). Aucun correctif exigé.
- **m6. m033 Q3 (`matching`), appariement par mots.** Il se fait par écho lexical : « كلٌّ » ↔ « كلٍّ »,
  « كلا الرّأيين » ↔ « رأيانِ », « اِروِ الحادثة … أبوك » ↔ « روايةُ الحادثةِ … الأبِ ». Correctif facultatif :
  - r1 → « يتقاسمُ فيه المتحاورانِ الحججَ، فيعرضُ هذا أسبابَه وذاكَ أسبابَه » ;
  - r2 → « يُعرَضُ فيه الموقفانِ، والثقلُ لما يسندُ موقفَ الراوي من حججٍ » ;
  - r3 → « يُركَّزُ فيه ما يحتجُّ به الوالدُ بعدَ سردِ ما وقعَ، لا ما يحتجُّ به الراوي ».
- **m7. m035 Q1, étiquettes.** `arabe.hijaj.khutta-la-tuwafiq-al-matlub` sur a (le fils parle à la place du
  père) et c (le père s'adresse aux citoyens) ne nomme pas l'erreur : le libellé parle d'un plan qui ne
  correspond pas au format demandé, pas d'une inversion du locuteur ou du destinataire. Aucune étiquette
  `arabe.*` ne convient. Les rendre muettes.
- **m8. Cours 09, ligne recommandée.** Dans § « ✍️ الإنتاجُ (3) », bloc `::: methode`, ajouter après la
  « حالةٌ حدّيّةٌ » existante :
  > **حالةٌ حدّيّةٌ ثانيةٌ**: إذا طلبَ الموضوعُ «حججًا ونصائحَ» ففرّقْ بينَهما: **الحجّةُ** سببٌ عامٌّ يجيبُ عن
  > «لماذا؟»، و**النصيحةُ** توجيهٌ إلى ما ينبغي فعلُه، وأقواها ما بُنيَ على حجّةٍ: «الماءُ موردٌ نادرٌ، فأغلقِ
  > الحنفيّةَ وأنتَ تغسلُ أسنانَكَ». وإذا طلبَ رسالةً فافتتحْها بنداءٍ يناسبُ المخاطَبَ واختمْها بتحيّةٍ أو دعاءٍ.

  L'exemple est différent de toutes les options de m035 : aucune clé n'est recopiée. Le reflet dans
  `resume.md` est facultatif. Les définitions restent dans les énoncés (autonomie dans le donjon).
- **m9. Réserves de gabarit, sans correctif exigé.** Toutes ces questions sont prescrites par la carte.
  - m033 Q8 et m034 Q8 (`ordering`) reprennent le squelette de m012 Q5 et de 09/02 Q4 : introduction, première
    voix, liaison, seconde voix, issue. Chacune ajoute un découpage propre au lot : la conclusion du père, ou la
    concession avant les arguments. Recevable.
  - m034 Q4 et Q7 suivent le cadre de m015 Q4 : thèse adverse, renversement total, titre ou description, clé.
    Q5 s'en distingue par la condition.
  - m033 Q1 et m034 Q1 suivent le cadre de m012 Q2. La carte de m034 range pourtant « 09/04 Q3, 09/05 Q6
    (exposer fidèlement la thèse adverse) » dans « ne pas redemander », tout en prescrivant sa Q2 (devenue
    Q1). La contradiction est au planificateur ; je n'exige rien.
- **Étages et titres** :
  - m033 : d3, 120/30, rampe 1-1-2-2-2-2-3-3-3 ;
  - m034 : d3, 120/30, rampe 1-2-2-2-3-3-3-3 ;
  - m035 : d2, 75/15, rampe 1 puis 2.
  Titres ⭐ conformes, aucun ne livre de clé. Aucun « اكتب » dans les items. Aucun chiffre indien. Aucun
  passage long recopié.

## Résumé

- **26 questions auditées. 0 clé fausse.**
- **5 défauts majeurs** :
  - M1 : m035 Q5, ordre contraire au cours ;
  - M2 : m034 Q3, doublon du discriminant « غيرَ أنّ » contre connecteur de conclusion, déjà testé dans
    m015 Q3 et m013 Q4 ;
  - M3 : m034 Q2, clé qui recopie la consigne ;
  - M4 : m033 Q7, gabarit de m012 Q3 ;
  - M5 : m035 Q6, duel incohérent et leurre morbide.
- **9 mineurs ou réserves.**
- **Étiquettes** : toutes exactes sauf m035 Q1 a et c (à rendre muettes). Aucune sur `multi`, `ordering` ou
  `matching`.
- **Doublons** : M2, M3, M4 et m2 avec la vague 1. Les autres sont des réserves prescrites par la carte.
- **Points prioritaires tranchés** :
  - frontières des `multi` m035 Q2 et m033 Q5 : indiscutables ;
  - m033 Q9 (carte Q7) : juste ;
  - m034 Q3 : frontière juste, mais doublon ;
  - m035 Q6 : registre juste, mais langue de l'énoncé fautive ;
  - écarts : celui de m034 est justifié mais le remplacement est à reprendre ; celui de m033 est insuffisant ;
  - « نصيحة » : une ligne de cours est recommandée ;
  - rendu RTL : correct.

**Verdict : à corriger avant publication.** Appliquer M1 à M5, m1 à m3 et m7. Re-vérification ciblée ensuite :
m033 Q7, m034 Q2 et Q3, m035 Q5, Q6 et Q7.
