# Audit pédagogique indépendant — `education-islamique-5eme`

> **Empreinte** : valide au commit `b053b65` du dépôt privé `MBeji/yahia-quest-content`
> (tip de `main` le 2026-08-03). **Ré-auditer si le contenu a bougé.**
> **Périmètre** : 12 chapitres publiés (`01-sourate-al-burooj` → `12-al-iman-bil-kutub`),
> **420 questions** (12 quiz × 5 + 60 exercices × 6), 12 `cours.md`, 12 `resume.md`.
> **Suite donnée** : les 8 défauts + la retouche de formulation sur les نواقض sont **appliqués
> dans la PR qui apporte ce rapport** (15 lignes sur 12 fichiers, aucune clé retournée, aucune
> modification du texte coranique). Publication en production : dispatch séparé de `apply-content.yml`.
> **Auditeur** : session indépendante, sans participation à l'écriture (PR #105, #106, #108, #109).
> **Révision 2 (2026-08-04)** : le BLOCKER annoncé en révision 1 est **retiré** — il était faux,
> arbitré sur les points de code du corpus KFGQPC قالون. Le sujet passe de « fix-first » à
> « aucun bloquant ».

## Verdict

**Aucun bloquant. Le sujet peut rester en production tel quel** ; les 8 défauts restants méritent
une PR de retouche, aucun n'est urgent.

Sur 420 questions re-résolues, **aucune clé n'est fausse** et aucune explication ne contredit sa
clé. La qualité pédagogique est au-dessus de la barre : les distracteurs encodent des confusions
réelles (فريضة/سنّة/مستحبّ, مبطل/مكروه), les explications citent le guide, les mises en situation
sont justes pour 10-11 ans. Le texte coranique est conforme à la رواية قالون sur les 102 آيات.

Les défauts restants portent tous sur la **typographie du texte révélé** (marqueurs ﴿ ﴾) et sur un
point d'histoire de la sourate — pas sur le texte lui-même.

| Sévérité      | Nombre | Fichiers touchés                                |
| ------------- | ------ | ----------------------------------------------- |
| **BLOCKER**   | **0**  | —                                               |
| **MAJOR**     | 3      | `07-…-mutaffifeen`, `11-as-salat`               |
| **MINOR**     | 5      | 05, 07, 11, 12, 04                              |
| _Couverture_  | —      | 12/20 chapitres (8 manquants, hors périmètre)   |

---

## ~~[BLOCKER] 1 — Le texte coranique diverge de la رواية قالون~~ — **RETIRÉ, l'audit avait tort**

**Ce constat était faux et il est retiré intégralement (2026-08-04).** Il annonçait que
`07-sourate-al-mutaffifeen` publiait `فَاكِهِينَ` au verset 31 là où le guide p.29 imprimerait
`فَكِهِينَ`, et en déduisait une retouche manuelle de l'auteur après son contrôle automatique.
**Les deux affirmations sont fausses.** Le contenu publié est juste ; rien n'est à corriger.

Ce que dit le corpus KFGQPC رواية قالون, entrée 83:31 :

```
فَٰكِهِينَ  =  U+0641 U+064E U+0670 U+0643 U+0650 U+0647 U+0650 U+064A U+0646 U+064E
                          ^^^^^^ alif suscrit — et aucun U+0627 dans le mot
```

L'**alif suscrit** (U+0670) note un **ā long prononcé** écrit sans alif pleine. La lecture قالون est
donc bien _fākihīn_ et حفص lit _fakihīn_ : **le message de commit de la PR #108 énonçait le farsh
dans le bon sens.** Et `فَاكِهِينَ` est la conversion imlāʾī correcte que la méthode du projet
prescrit (`ٰ`→`ا`) — le mot passait le contrôle automatique **pour cette raison exacte**, sans
aucune intervention manuelle.

**D'où venait l'erreur de l'audit** — trois fautes de raisonnement, à consigner :

1. **Avoir lu l'absence d'un alif _pleine_ sur le scan et conclu à l'absence du _son_ long.** Un
   مصحف en rasm ʿuthmānī écrit ce ā par un trait minuscule au-dessus de la lettre, sous le seuil de
   résolution du scan à cette taille d'impression. Agrandir n'a fait qu'agrandir le flou — et
   l'agrandissement a été pris à tort pour une confirmation.
2. **Avoir pris le scan pour juge d'un point de _vocalisation_.** Le scan fait autorité sur le
   squelette consonantique et le périmètre ; sur un farsh vocalique, c'est le corpus qui tranche —
   ce que `content-ecole-tn/SKILL.md` §144 dit déjà.
3. **Avoir déduit un comportement humain d'un message de commit.** La « correction manuelle après
   contrôle » n'a jamais été observée : elle a été inférée du seul fait que le commit énonçait le
   point de farsh. Le mot avait été injecté par script depuis le fichier vérifié.

Règle qui en sort, applicable à tout écart coranique futur : **dumper les points de code des deux
côtés avant de déclarer une divergence.** C'est instantané et sans appel.

---

## [MAJOR] 2 — Du texte inventé présenté entre ﴿ ﴾

**Fichier** : `07-sourate-al-mutaffifeen/exercices/05-entrainement.json` — question
« ماذا يقول المجرمون عن المؤمنين حين يرونهم؟ »

La clé ﴿إِنَّ هَٰؤُلَاءِ لَضَالُّونَ﴾ est juste (v. 32). Mais les **trois distracteurs** sont des
fins de verset **inventées**, présentées entre **﴿ ﴾** — les marqueurs typographiques réservés à la
révélation :

- ﴿إِنَّ هَٰؤُلَاءِ لَصَادِقُونَ﴾
- ﴿إِنَّ هَٰؤُلَاءِ لَفُقَرَاءُ﴾
- ﴿إِنَّ هَٰؤُلَاءِ لَغَافِلُونَ﴾

Pour un élève qui mémorise la sourate, trois options sur quatre **ressemblent à du Coran**.

**Correction proposée** : retirer les ﴿ ﴾ des quatre options (garder les mots, en guillemets
ordinaires « … » ou sans marque), et laisser les ﴿ ﴾ à l'explication qui cite le vrai verset.

> _Contrôle de portée_ : les 335 fragments ﴿…﴾ du sujet ont été testés mécaniquement comme
> sous-chaînes exactes du texte validé. **Ces trois-là sont les seuls** cas de texte non coranique
> présenté ainsi dans les chapitres de sourate.

---

## [MAJOR] 3 — Un hadith présenté entre ﴿ ﴾

**Fichier** : `11-as-salat/cours.md:92`

```
﴿فَذَلِكَ مِثْلُ الصَّلَوَاتِ الْخَمْسِ يَمْحُو اللهُ بِهِنَّ الْخَطَايَا﴾
```

C'est un **hadith** (celui du fleuve à la porte, البخاري/مسلم), pas une آية. Les ﴿ ﴾ lui donnent le
statut de parole révélée.

Ce n'est pas une habitude : ailleurs l'auteur applique correctement la convention — `12-al-iman-bil-kutub/cours.md:55`
met le حديث جبريل entre **« »**, et `04-adab-al-hadith` fait de même pour ses deux hadiths. **Dérapage
isolé, une seule occurrence dans tout le sujet.**

**Correction proposée** : passer en guillemets « … », comme les autres hadiths du sujet.

---

## [MAJOR] 4 — Une classification contestée enseignée comme certaine

**Fichiers** : `07-sourate-al-mutaffifeen/cours.md:7`, `resume.md:3`, `chapter.json` (description)

Le contenu affirme sans réserve : **سورة المطفّفين … سورةٌ مكّيّة**.

Or le guide CNP consacre à ce point un paragraphe entier (p.30, أسباب النزول, citant
**التفسير المنير — الزحيلي** et **القرطبي**) :

> « وهي آخر سورة نزلت بمكة، وهي **مكية** في قول **ابن مسعود والضحاك ومقاتل**، ويقال إنها أول سورة
> نزلت بالمدينة، وهي **مدنية** في قول **الحسن وعكرمة** … وهذا على أن السورة مدنية، أو قرأها عليهم
> بعد قدومه إن كانت مكية. »

Le guide **ne tranche pas** et rattache le سبب نزول à l'arrivée du Prophète ﷺ à Médine. Le contenu
efface la divergence. Les deux autres sourates publiées (البروج، الانشقاق) sont incontestablement
مكّيّة — le défaut ne concerne que celle-ci.

**Atténuation** : **aucune des 420 questions** ne s'appuie sur cette classification (vérifié). Le
défaut est cantonné au cours, au résumé et à la description du chapitre.

**Correction proposée** (au choix, selon ce qu'on veut charger sur des élèves de 10-11 ans) :
soit « **وهي آخر سورة نزلت بمكّة، وقيل أوّل ما نزل بالمدينة** », soit simplement retirer l'étiquette
et garder « عدد آياتها 36، وترتيبها في المصحف 83 ».

---

## [MINOR]

| #   | Fichier · locator                                     | Défaut                                                                                                                                                                                     | Correction                                                            |
| --- | ----------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------- |
| 5   | `05-al-wudoo/exercices/05-entrainement.json` Q1        | Négation non emphasée : « أيّ هذه **ليست** من نواقض الوضوء؟ ». L'auteur met bien la négation en gras dans les 2 autres cas réels du sujet — slip isolé.                                    | Passer `ليست` en gras.                                                |
| 6   | `07-…-mutaffifeen/quiz.json` Q5 · `12-…-kutub/quiz.json` Q4 | Questions taguées **d3** dans un quiz. La barre veut le quiz en d1–2 (il ne fait que jauger la compréhension).                                                                          | Retaguer d2.                                                          |
| 7   | `12-al-iman-bil-kutub/cours.md:20-22`                  | آل عمران est annoncée « **الآيتان 3 و4** » mais le v.4 est coupé après ﴿وَأَنْزَلَ الْفُرْقَانَ﴾ sans marque d'élision.                                                                    | Ajouter « … » ou annoncer « الآية 3 وأوّل الآية 4 ».                  |
| 8   | `04-adab-al-hadith/cours.md:62`                        | L'أثر d'ابن عبّاس est reformulé : le guide p.50 a « **أحنق** », le contenu écrit « **أشدّ حَنَقًا** ». Les paroles rapportées se transmettent telles quelles.                              | Rétablir « أحنق » avec la glose du guide « (أشدّ غيظًا) ».            |
| 9   | `11-as-salat/exercices/02-boss.json` Q2                | Option « تمسّ **بنية** الصلاة » non vocalisée : se lit aussi bien بِنْية (structure — sens voulu) que بِنِيَّة (avec intention — sens inverse). Le reste du chapitre est vocalisé.        | Écrire « تمسّ **بِناء** الصلاة » (lève l'ambiguïté sans vocalisation). |

---

## Ce qui a été vérifié et qui est JUSTE

Un audit qui ne dit que les défauts ment par omission. Les points suivants ont été **re-vérifiés
contre la source primaire** (scans du guide CNP 511505), pas seulement relus :

**Texte coranique** (contre les pages du guide, qui impriment le rasm قالون prescrit)

- **سورة البروج** — 22 آية vérifiées une à une contre p.20. Conforme, **y compris le point de farsh
  قالون ﴿وَهْوَ الْغَفُورُ الْوَدُودُ﴾ (v.14)** là où حفص lit ﴿وَهُوَ﴾ — et la subtilité inverse au
  v.13, où ﴿إِنَّهُ هُوَ يُبْدِئُ﴾ garde bien le ḍamma.
- **سورة الانشقاق** — 25 آية vérifiées contre p.25. Conforme, **y compris ﴿وَيُصَلَّىٰ سَعِيرًا﴾ (v.12)**,
  là où حفص lit ﴿وَيَصْلَىٰ﴾.
- **سورة المطفّفين** — **36 آيات sur 36 conformes.** Le v.31 (`فَاكِهِينَ`), d'abord signalé à tort
  comme divergent, est **juste** : arbitré sur les points de code du corpus قالون (voir le constat
  retiré ci-dessus).
- **البقرة 177 — ﴿وَالنَّبِيئِينَ﴾ avec hamza** : **correct**, le guide p.65 l'imprime ainsi. C'est
  précisément le point que l'auteur déclarait avoir sorti de sa vérification automatique et relu
  « à l'œil » — il avait raison.
- **النساء 136** et le **حديث جبريل (مسلم 1/28-29)** : exacts, mot pour mot, contre p.65.
- **الذاريات 24-27** (ضيف إبراهيم) : exact contre p.51.
- **المائدة 6** (آية الوضوء) : exact contre p.68.
- **L'arbitrage آل عمران 3-4 vs 2,3,4** de la PR #109 est **corroboré** : la page de contenu p.65 ne
  cite effectivement pas آل عمران du tout et développe le chapitre avec النساء 136, البقرة 177 et
  حديث جبريل — exactement ce que fait le chapitre 12.

**Hadiths**

- `04-adab-al-hadith` : « **الْكَلِمَةُ الطَّيِّبَةُ صَدَقَةٌ** » (متّفق عليه) et
  « **اتَّقُوا النَّارَ وَلَوْ بِشِقِّ تَمْرَةٍ، فَمَنْ لَمْ يَجِدْ فَبِكَلِمَةٍ طَيِّبَةٍ** » (البخاري)
  — libellés **et attributions** conformes à p.50.
- `09-ikram-ad-dayf` : « **مَنْ كَانَ يُؤْمِنُ بِاللهِ وَالْيَوْمِ الْآخِرِ فَلْيُكْرِمْ ضَيْفَهُ** »
  conforme à p.51, ainsi que le récit des hôtes d'Abyssinie.

**Fiqh malikite** (le plus exposé aux erreurs de mémoire — tout est conforme)

- **الوضوء** vs p.68-69 : les **7 فرائض** (avec **الدَّلك** et **الفَور والموالاة**, les deux que le
  mذhab malikite range en فرائض et qu'un auteur travaillant de tête aurait mis en سنن), les 8 سنن,
  les 10 مستحبّات, les 5 مكروهات, les 6 نواقض, la كيفية et le تنبيه sur le سَلَس. **Rien à redire.**
- **الصلاة** vs p.75-76 : les **12 مبطلات** et les مكروهات. Toutes les questions qui s'appuient
  dessus sont justes, **y compris la distinction fine « عمدًا أو سهوًا » vs « عمدًا » seul** —
  `02-boss` Q1 (l'élève qui mange par oubli) et Q3 (« كثيره ويسيره ») sont exactes au mot près.

**Mesures transverses** (mesurées, pas estimées, sur les 420 questions)

| Contrôle                                          | Résultat                                                          |
| ------------------------------------------------- | ----------------------------------------------------------------- |
| Fuite par la longueur de la clé (mesure stricte)  | **6,0 %** (25/420) — hasard ≈ 25 %. Un seul exercice à 50 %.       |
| Équilibre des clés                                | **108 / 104 / 106 / 102** (a/b/c/d) — annonce de l'auteur exacte.  |
| Chiffres arabo-hindis                             | **0**                                                             |
| Résidu LaTeX / `$…$`                              | **0**                                                             |
| Méta-options (« لا شيء ممّا سبق »…)               | **0**                                                             |
| Récompenses hors table canonique                  | **0**                                                             |
| Titres sans indicateur ⭐                          | **0**                                                             |
| Doublons réels de questions                       | **0**                                                             |
| `content:check` · `content:qa:strict`             | ✓ · ✓ **0 erreur, 0 warning** sur ce sujet                        |

> **Faux positif écarté** : un premier passage a relevé 84 « rampes de difficulté décroissantes ».
> Vérification faite dans le moteur — `src/shared/content/sql-builder.ts:374` **retrie les questions
> par difficulté à l'émission**. L'ordre dans le fichier est donc invisible pour l'élève : ce n'est
> pas un défaut et ces 84 lignes ne sont pas comptées.
>
> **Faux positif écarté** : l'énoncé « أيُّ الجُمَل يُلخّص الدرس تلخيصًا أمينًا؟ » revient dans 7
> chapitres, mais avec un contenu différent à chaque fois — c'est un **gabarit de clôture**, pas un
> doublon. Tout au plus un peu formulaire.

---

## Décision d'auteur réexaminée : les نواقض الوضوء (`05-al-wudoo`)

**Rappel de la décision** (PR #106) : les نواقض sont détaillés pour les 4 qui concernent un élève de
10-11 ans ; les 2 autres — **مسّ الذكر بتلذّذ** et **مسّ المرأة بشهوة** — sont nommés en une ligne
sans développement.

### Verdict : **CONFIRMÉE.** À garder telle quelle, avec une retouche de formulation.

Le guide p.69 énumère bien **6** نواقض : (1) ما خرج من السبيلين, (2) النوم الثقيل,
(3) غياب العقل والإدراك, (4) مسّ الذكر بتلذّذ, (5) مسّ المرأة بشهوة, (6) الشكّ. L'auteur détaille
1, 2, 3, 6 et nomme 4 et 5.

Ce qui rend l'arbitrage solide, vérifié point par point :

1. **Rien n'est caché.** Les 6 sont nommés dans le cours (ligne 68). Un élève curieux, ou un parent,
   trouve la liste complète.
2. **Le cours n'annonce jamais un nombre.** La ligne 61 définit les نواقض sans dire « elles sont
   quatre » — donc pas de contre-vérité.
3. **Aucune question ne porte sur le nombre** de نواقض (vérifié sur les 35 questions du chapitre).
   C'était le vrai risque de ce découpage : une question « كم عدد نواقض الوضوء؟ » aurait été piégée
   par une liste de 4. Elle n'existe pas. En regard, la question qui existe — « كم عدد **فرائض**
   الوضوء؟ » — attend bien **7**, le compte complet.
4. **Les 2 نواقض non développés n'apparaissent dans aucune question** (0 occurrence dans les 6
   fichiers du chapitre). Aucun élève n'est évalué sur ce qu'on a choisi de ne pas lui enseigner.
5. **C'est conforme au cadre du guide lui-même**, qui situe explicitement l'élève dans la
   « مرحلة النموّ من التاسعة إلى الثانية عشرة » (p.8) et construit la valeur à partir de situations
   vécues.

**Seule retouche demandée** : la ligne 68 écrit « ويذكر الدليل ناقضين آخرين **يُفصّلان في مرحلةٍ
لاحقة** ». Cette promesse d'un traitement ultérieur n'est adossée à rien dans le programme.
Préférer une formule qui constate sans promettre :
« ويذكر الدليل ناقضين آخرين — **مسّ الذكر بتلذّذ ومسّ المرأة بشهوة** — لا نُفصّلهما في هذه السنة. »

---

## Couverture du niveau (hors périmètre d'audit, pour mémoire)

`npm run content:audit` : **12/20 chapitres (60 %)**. Manquent
`13-al-mouhafadha-ala-mumtalakat`, `14-adh-dhann-bil-ghayr`, `15-qawl-al-maroof`,
`16-sourate-al-infitar`, `17-az-zakat`, `18-at-tawadu`, `19-al-ithar`, `20-al-ulfa-wal-itilaf`
— soit toute la **الفترة 3** (sauf الإيمان بالكتب) et toute la **الفترة 4**, dont la **زكاة**, qui
est l'une des trois عبادات attendues à ce niveau, et **سورة الانفطار**, la 4ᵉ sourate au programme.

Ce n'est pas un défaut du contenu écrit — c'est l'état de la campagne. Signalé parce que le niveau
ne peut pas être **scellé** (`sealed: true`) tant qu'il n'est pas complet.

---

## Chemin de correction

Les 8 défauts sont tous des retouches en place, **UUID-safe** : aucun renommage de dossier, aucun
déplacement de question entre tags de difficulté, aucune clé à retourner, **et aucune modification
du texte coranique**.

Rien n'étant bloquant, la correction peut attendre le prochain lot de la campagne plutôt que de
partir en PR isolée.

1. PR sur `MBeji/yahia-quest-content` (branche `claude/...`).
2. `npm run content:check` + `npm run content:qa:strict` (0 erreur attendu, comme aujourd'hui).
3. **Merge ≠ publication.** Dispatcher `apply-content.yml` après le merge, sinon rien ne change en
   production.
