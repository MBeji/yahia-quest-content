# Audit indépendant — anglais 9ᵉ, lot L04 (gisement, étude 36)

Périmètre : `content/english/09-reading-comprehension-writing/exercices/11-` à `16-exams-*.json` (m016–m021),
branche `wip/gisement-anglais-9eme` (worktree `/home/user/wt-en`, commit `420eda53`). Ligne `sources[]` du
`chapter.json` 09 : conforme à PLAN R8.

Sources lues : les transcriptions des 33 sessions citées (parties II et III) ; `cours.md` et `resume.md` de 01 à 10 sur
`origin/main` (et le 07 de la branche, cours L06) ; `misconceptions.json` sur `origin/main` ; la fiche programme
`programme/9eme-base/anglais.md` ; PLAN.md ; les missions des lots L02, L03, L06 pour les fuites croisées. Les notes
d'erreurs muettes de l'auteur (`/tmp/claude-0/en-gis/L04/muets-*.json`) n'ont été ouvertes qu'après la re-résolution
des six fichiers.

Moteur (`/home/user/eng-en`) : `content:check` vert ; `content:qa -- --subject english --strict` : aucun signal ;
`content:tranche --chapters 09` : 12/123 clés strictement les plus longues (8 dans L04, § 4), une paire proche à
0,45 et deux groupes gabarit (§ 5). Schéma `matching` (`src/shared/content/schema.ts` l. 943) : « matching needs
>= 2 left items and as many right items » — l'intrus officiel ne peut pas entrer.

**68 questions re-résolues à l'aveugle (12 + 12 + 12 + 10 + 10 + 12). 0 clé fausse.** Toutes les phrases citées
sont fidèles aux transcriptions (seule réserve : le cadre de 2019 T, m021 Q1, m3).

## 1. Re-résolution à l'aveugle

### m016 — `11-exams-2013-2026-the-right-preposition.json` (d2, practice 75/15)

| Q | session | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- | --- |
| 1 | 2026 T | at | a | OK | « by » (ajouté à la banque) ne se défend pas sans « offered » |
| 2 | 2026 G | in | c | OK | |
| 3 | 2025 G | on | b | OK | |
| 4 | 2025 G | for | a | **réserve** | l'énoncé dit « look after others » : clé de Q8 (M1) |
| 5 | 2023 G | At | c | OK | clé donnée par 08/07 Q2 (L03) et par l'énoncé de Q12 (M2, M3) |
| 6 | 2019 G | for | d | **réserve** | l'énoncé dit « turned off for a short time » : il donne sa propre clé (M4) ; explication de « about » fausse (m1) |
| 7 | 2021 G | of | c | OK | |
| 8 | 2020 T | after | b | OK | |
| 9 | 2019 G | about | b | OK | gérondif après préposition : enseigné au 07 (« The gerund ») |
| 10 | 2019 T | at | a | OK | |
| 11 | 2015 T | from | b | réserve | explication de « for » fausse (m2) |
| 12 | 2013 G | of | c | réserve | « won a poetry competition at twelve » modèle « at » + âge pour Q5 (M2) ; « proud of » fuit depuis m024 Q9 (M3) |

**Remplacement de 2022 T par 2019 G (Q6) : justifié.** « starting (from / in / at) 1997 » a deux clés : « starting in
1997 » est aussi correct que « starting from 1997 » (R6). Le blanc de 2019 G, exercice 1 (banque « from / for /
about » + « at » ajouté), est fidèle à la transcription, à clé unique ; le titre (« 2013–2026 ») reste juste.

### m017 — `12-exams-2006-2026-linking-words.json` (d2)

| Q | session | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- | --- |
| 1 | 2023 T | However | a | réserve | « However » non enseigné (M5) ; « Besides » ajouté se défend mal sans « Gilbert has got big plans » (m3) |
| 2 | 2026 G | While | b | OK | explication trop absolue sur « However » (m4) |
| 3 | 2023 T | but | a | OK | |
| 4 | 2023 G | But | d | OK | leurre officiel « After » conservé |
| 5 | 2020 G | when | b | OK | |
| 6 | 2020 T | Besides | c | réserve | « Besides » non enseigné (M5) |
| 7 | 2019 T | But | b | OK | |
| 8 | 2018 T | Besides | a | réserve | « Besides » non enseigné (M5) |
| 9 | 2013 T | But | c | **réserve** | « hasn't got his ladder » donne la clé de m007 Q6 (M6) |
| 10 | 2009 G | Although | a | réserve | « Although » non enseigné (M5) |
| 11 | 2007 | So | b | OK | |
| 12 | 2006 | so | a | **réserve** | contexte ajouté qui donne m006 Q12 et m007 Q8 (M7) |

### m018 — `13-exams-2018-2026-the-right-word-in-context.json` (d2)

| Q | session | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- | --- |
| 1 | 2026 T | earn | a | OK | |
| 2 | 2026 G | caused | b | OK | |
| 3 | 2025 G | contribute | c | OK | « participate (to) » : candidat à l'étiquette proposée (§ 3) |
| 4 | 2025 T | test | d | OK | « job », « car » éliminables par la nature du mot : ce sont les mots de la banque officielle |
| 5 | 2024 G | reason | a | OK | |
| 6 | 2024 T | join | b | OK | « [sic] » dans l'énoncé, jamais dans une option : conforme à R6 |
| 7 | 2023 G | important | c | OK | |
| 8 | 2022 G | protectors | a | OK | |
| 9 | 2021 G | reduce | b | OK | |
| 10 | 2020 G | inspiration | a | OK | |
| 11 | 2019 G | role | c | **réserve** | « help themselves » donne la clé de m023 Q11 (L06) (M8) |
| 12 | 2018 G | wish | b | **à remplacer** | « I wish + clause » non enseigné (M9) |

### m019 — `14-exams-2001-2026-matching-sentence-parts.json` (d2)

| Q | session | mon appariement | clé | verdict | motif |
| --- | --- | --- | --- | --- | --- |
| 1 | 2026 G | 1c 2a 3e 4b (officiel) | idem | **réserve** | l'énoncé « pupils trained as anti-violence ambassadors » donne la paire 1 (M10) |
| 2 | 2025 T | 1c 2a 3e 4b | idem | OK | |
| 3 | 2024 T | 1d 2b 3e 4c | idem | OK | |
| 4 | 2021 G | 1c 2e 3a 4b | idem | OK | intrus officiel « that these old patients didn't love him » perdu (§ 2.5) |
| 5 | 2018 G | 1b 2e 3a 4c | idem | OK | |
| 6 | 2015 G | 1c 2f 3a 4b 5d | idem | OK | |
| 7 | 2013 T | 1c 2a 3e 4b | idem | OK | |
| 8 | 2006 | 1b 2d 3a 5c | idem | OK | exemple ④ + ⓕ donné, non compté : fidèle |
| 9 | 2003 | 1d 2a 3b 4c | idem | OK | consigne « Match by meaning. Match each… » redoublée (m5) |
| 10 | 2001 | 1c 2f 3a 4d | idem | réserve | appariement unique ; la note « one ending » est fausse : le sujet a **deux** répliques en trop (m6) |

(Lettres = colonnes B officielles ; tous les appariements de la clé du fichier coïncident.)

### m020 — `15-exams-2001-2025-writing-describe-persuade-opinion.json` (d3, boss 120/30)

| Q | session | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- | --- |
| 1 | 2025 G | a, c, e | a, c, e | réserve | nombre de bonnes réponses devinable : « at least three » + 3 clés, même gabarit que 04/07 Q5 (M11) |
| 2 | 2025 G | c | c | OK | |
| 3 | 2025 T | d | d | OK | gabarit voisin de 04/07 Q2 (§ 5) |
| 4 | 2021 G | b | b | OK | |
| 5 | 2021 T | a, b, d, f | a, b, d, f | OK | 4 sur 6, non devinable |
| 6 | 2020 G | l1-r3, l2-r1, l3-r4, l4-r2 | idem | OK | appariement unique |
| 7 | 2017 G | d | d | **ERREUR d'énoncé** | sans la consigne « DO NOT WRITE YOUR NAME OR SIGN », l'option signée se défend (M12) |
| 8 | 2015 G | a | a | OK | |
| 9 | 2001 | b | b | réserve | étiquette `phrase-hors-sujet` sur une option qui ne choisit pas (m7) |
| 10 | 2001 | c, b, a, d | idem | réserve | ordre unique, mais d3 non justifié (§ 2.6) ; « would » non enseigné (m8) |

Distracteurs : tous indéfendables. Q1 b (population), d (l'influenceur), f (ailleurs) ; Q5 c (récit), e (conseil au
lecteur) ; Q8 b (liste des mots d'aide), c et d (comptes rendus au passé, qui n'incitent pas).

### m021 — `16-exams-2005-2019-writing-letters-and-emails.json` (d3, boss 120/30)

| Q | session | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- | --- |
| 1 | 2019 T | c | c | réserve | la clé recopie la consigne citée ; cadre amputé de « Wahid / Wahida » (m3) |
| 2 | 2019 T | a, c | a, c | réserve | 2 sur 6, indéfendables ; d et e sont absurdes, aucune erreur d'élève (m9) |
| 3 | 2018 T | d | d | OK | |
| 4 | 2013 T | b | b | OK | étiquettes `to-en-trop`, `base-verbale-deformee` exactes ; « I advise you join » muet, juste |
| 5 | 2012 G | l1-r2, l2-r4, l3-r1, l4-r3 | idem | **réserve** | appariement de culture générale, non unique : un train est aussi bon marché et confortable (M13) |
| 6 | 2012 G | c | c | OK | étiquettes `double-marque`, `comparatif-et-superlatif-confondus` exactes |
| 7 | 2011 G | d | d | OK | |
| 8 | 2010 T | b, c, a, d | idem | OK | ordre unique : remerciement, puis l'ordre de la liste de Linda |
| 9 | 2010 T | a | a | OK | |
| 10 | 2007 | b | b | réserve | d3 non justifié (§ 2.6) |
| 11 | 2005 | c | c | OK | `cause-et-consequence-inversees` sur « noisy, so … cars » : exact |
| 12 | 2009 G | a | a | réserve | la clé est le cadre recopié de l'énoncé ; consigne d'anonymat absente de l'énoncé ; d3 non justifié (M14) |

## 2. Points à trancher (questions de l'orchestrateur)

### 2.1 m016, prépositions : une ligne de cours est nécessaire

Aucun cours (01–10 sur `origin/main`) n'enseigne la préposition qu'appelle un mot ; le manuel non plus (fiche :
« Prepositions of Location… annoncées au plan : aucun contenu dans SB ni AB », M2-L2 ; « les prépositions ne sont
pas explicitées », M4-L4 p. 91). Mais le manuel les **donne comme lexique** : « To look after » (plan SB p. 6),
« approve of, disapprove of, dispose of » (Word list SB p. 97), « I'm interested in » (SB p. 99), « To take part in »
(lexique du guide, M6-L1, p. 40). Les douze questions testent donc une connaissance qu'aucune page de l'app ne
pose : l'explication l'apprend après coup, ce qui ne suffit pas à la règle « tout ce que teste une question est
enseigné » (MAJEUR, M15). Une ligne suffit, au 09, dans la section « 📚 Word meaning from context », à la fin du bloc
`::: propriete` (après le paragraphe « Edge cases: … »), texte exact :

```markdown
A word often brings its **own preposition**, and it is rarely the one French or Arabic would choose: learn the word and its preposition as one block — _take part **in**_, _look **after**_ (= take care of), _approve **of**_, _interested **in**_ (Student's Book p. 6, p. 97, p. 99).
```

et, au `resume.md`, à la fin de la puce « **Meaning from context** » :

```markdown
; a word often brings its own preposition (_take part in, look after, interested in_): learn the block.
```

Choix vérifiés : les exemples sont ceux du manuel ; un seul (« take part in ») est la clé d'une question de m016
(Q2) — c'est un enseignement, pas une fuite ; aucun ne donne une autre clé du lot. Ajouter au `sources[]` du 09 :
« Student's Book 141906, Module 1 plan (to look after) SB p. 6 ; Word list SB p. 97 (approve of, dispose of) ;
Module 5 Lesson 5 (I'm interested in) SB p. 99 ».

### 2.2 Étiquette proposée « préposition calquée du français ou de l'arabe »

Contrôles : uniquement des QCM (aucune `multi`, `ordering`, `matching`) ; pas de doublon : les deux étiquettes
existantes du domaine sont propres à une expression (`english.func.mind-suivi-d-une-preposition`,
`english.func.kind-for-au-lieu-de-kind-of`) ; aucune `english.*` générique sur les prépositions.

Une seule erreur par option, et l'erreur doit **être** le calque. Je l'ai vérifiée option par option (les notes de
l'auteur se trompent sur trois sources françaises) :

| question | option | calque | verdict |
| --- | --- | --- | --- |
| Q4 care ___ themselves | with | arabe « يعتني بـ » | **tag** |
| Q4 | of | « take care of » raccourci (note de l'auteur), ou « s'occuper de » : deux origines | muet |
| Q5 ___ a young age | In | arabe « في سنّ مبكّرة » (le français dit « à un jeune âge » → *at* : la note « dans/à » est fausse) | **tag** |
| Q7 as part ___ | from | arabe « جزء من » (et non « partir de ») | **tag** |
| Q7 | for | « pour » ne traduit rien ici | muet |
| Q10 laughed ___ her | of | français « rire de » | **tag** |
| Q10 | on | arabe « ضحك على » | **tag** |
| Q11 protect ___ irritation | of | français « protéger de » | **tag** |
| Q11 | for | « pour » : pas la préposition de « protéger » | muet |
| Q12 proud ___ her | with | arabe « فخور بـ » | **tag** |
| Q2 take part ___ | of | contamination de « part of » ; le français dit « prendre part à » | **rejeté** (muet) |
| Q9 nervous ___ meeting | with | « nerveux avec » n'existe ni en français ni en arabe (« متوتّر من ») | **rejeté** (muet) |

**Verdict : famille acceptée, sur 6 questions (Q4, Q5, Q7, Q10, Q11, Q12), 7 options** ; Q2 et Q9 restent muettes.
Extension possible : m018 Q3 « participate » (« participer à » → *to*) exécute la même erreur.

Identifiant : `english.prep.preposition-calquee`. Textes définitifs :

- **fr** : « Tu prends la préposition qu'appellerait le mot en français ou en arabe (laugh of sur « rire de », proud with sur « فخور بـ ») : en anglais, chaque mot impose la sienne (laugh at, proud of). »
- **en** : « You use the preposition the French or Arabic word would take (laugh of from « rire de », proud with from Arabic): in English each word takes its own (laugh at, proud of). »
- **ar** : « تستعمل حرف الجرّ الذي تأخذه الكلمة في العربية أو الفرنسية، مثل proud with على قياس «فخور بـ»: في الإنجليزية لكلّ كلمة حرف جرّها، فنقول proud of وlaugh at. »

(Si le libellé fr ne doit pas porter d'arabe, écrire « proud with calqué sur l'arabe ».) Le libellé arabe ne met
aucune virgule arabe entre deux runs latins et place chaque mot latin entre mots arabes : à rendre une fois en
Chromium `dir=rtl` avec le reste de la tranche.

### 2.3 m017 : « Although » n'est pas au cours, ni « However », ni « Besides »

Constat élargi : `grep -w` sur les dix `cours.md` de `origin/main` : **However, Besides et Although ne sont enseignés
nulle part** (le 09 et le 10 n'enseignent que because / so / therefore / as a result / that's why / but / while /
whereas / and / also). La fiche le confirme : « although/but/however comme connecteurs formels » non enseignés ;
« moreover, besides, in addition apparaissent dans AB A4 sans être enseignés » (AB p. 71) ; « however » figure parmi
les mots d'aide du Writing two, SB p. 116. Sont touchées : Q1 (clé However), Q6 et Q8 (clé Besides), Q10 (clé
Although), et comme leurres Q1, Q2, Q4, Q6, Q8, Q11. MAJEUR (M5). La parenthèse de l'explication de Q10 (« This
linker is not in the course ») déclare le défaut sans le corriger.

Correctif : trois retouches de la section « 🔗 Linking ideas » du cours 09 (aucune nouvelle section) :

1. tableau, lignes « contrast » et « addition » :

```markdown
| contrast    | but, however, while, whereas, although | Salah is talkative, whereas his twin is quiet.      |
| addition    | and, also, besides                     | Walking is free. It is also good for the heart.     |
```

2. dans `::: propriete`, après le paragraphe « Edge case: _while_ and _whereas_ … », ajouter :

```markdown
**However,** and **Besides,** open a new sentence, followed by a comma: _The bus is cheap. However, it is slow._ (contrast) · _The bus is cheap. Besides, it is fast._ (one more point in the same direction). **Although** works like _while_: it opens the first idea, and a comma closes it — _Although the bus is cheap, many people drive._
```

3. `::: retenir` : « **but / however / while / whereas / although** → contrast · **and / also / besides** → addition »
   à la place de « **but / while / whereas** → contrast » ; même retouche dans la puce « **Linkers** » du `resume.md`
   (« **but / however / while / whereas / although** + opposite ideas · **and / also / besides** add »).

Vérifié : les exemples (bus) ne reprennent aucune phrase d'examen ni de mission ; ils n'appliquent la règle à
aucun item de m017 (le blanc reste à trouver par le sens) ; sources : SB p. 116 (however), AB p. 71 (addition) ;
« although » est au-delà du manuel, à déclarer dans la PR (l'examen l'exige, 2009 G). La phrase de Q10 « (This
linker is not in the course: the sentence shows how it works.) » est alors à supprimer.

Q2, explication (m4) : « "However" … stands between two sentences » est trop absolu (« However many children… »
est grammatical au sens de « no matter how many »). Remplacer la dernière phrase par : « "However", as a contrast
linker, opens a new sentence and is followed by a comma; it cannot join the two parts of this sentence. »

### 2.4 m018 : « I wish » et « Los Angles »

- **« I wish » (Q12) : à remplacer (MAJEUR, M9).** La consigne de tri le dit « fonction du manuel, Module 6 » ; la
  fiche dit l'inverse : la cellule Grammar « 2- I wish + clause » de la carte M6-L5 est **inexistante** dans le
  manuel (« la cellule n'a que I hope that + clause ») et le manuel « N'enseigne PAS : I wish » (M5-L4, M6-L5) ; le
  cours 06 n'enseigne que « I hope that ». La question teste donc « wish + could », structure hors cours, et le
  contexte ajouté (« longs for those days, but she cannot go back ») paraphrase le sens de la clé : il élimine
  « imagine » par la définition de « wish » au lieu de le faire par la phrase. Remplacement dans la même session
  (2018 G, exercice 3, même texte), vérifié unique et sans fuite (« shy » n'apparaît dans aucun autre fichier
  `english`) :
  - prompt : `(Exam 2018, general) A grown-up remembers her first day at school. Which word completes the sentence?\n"I was very quiet at school. I was ___ and didn't know who to talk to."`
  - options (officielles) : `safe` · `shy` (clé) · `indifferent`
  - explication : `"Shy" describes someone who feels uneasy with others and does not dare to speak, which matches "very quiet" and "didn't know who to talk to". "safe" means out of danger, and "indifferent" would mean that she did not care about the others, while the sentence shows that she wanted to talk but did not know to whom.`
  - difficulty 2 (la mission devient toute d2, conforme à son étage d2).
- **« Los Angles » [sic] (Q6)** : conforme à R6 (coquille citée avec [sic] dans l'énoncé, jamais dans une option ;
  l'explication la signale). « enrol » et « finish » sont indéfendables. OK.

### 2.5 m019 : intrus perdu ; 2001

**Adaptation acceptée**, avec réserve. Le schéma exige autant d'éléments à droite qu'à gauche ; la consigne de tri
prévoyait sinon une question « which part in B is extra? » par appariement, ce qui doublerait la mission (plafond 10)
et ne demanderait rien que l'appariement ne donne déjà. Coût réel : l'intrus officiel était un vrai piège dans au
moins quatre sujets (2021 G « that these old patients didn't love him » contre « that they did not have much
entertainment » ; 2015 G « to rich people » ; 2013 T « and protects eyes » ; 2003 « he was coughing » après « He
said »), et sans lui la dernière paire se déduit par élimination. La note de chaque énoncé le déclare. À signaler
au moteur (suivi, hors lot) : accepter `rights.length ≥ lefts.length` rendrait l'intrus.

**2001 (Q10)** : appariement unique, avec ou sans les répliques en trop : la réplique 1 doit être une question
(« What time does your day start? », « How old are you? » écartée par « Late! Never before 10 o'clock ») ; « How
often » → fréquence (« Five days a week ») ; « How many hours » → durée (« About 4 hours a day ») ; loisirs → « I
drive my sports car… ». Mais le sujet imprime **deux** répliques en trop (b « How old are you? », e « I hate
flying. ») : la note « one ending that fits none of the beginnings » est fausse et « ending » ne convient pas à une
réplique (m6). Remplacer, dans le prompt de Q10, la parenthèse par :
`(The exam also printed two lines that fit none of the gaps; they are left out here.)`

### 2.6 m020 et m021 : writings convertis

- **Distracteurs** : tous indéfendables après correction de m020 Q7 (M12) et de m021 Q5 (M13).
- **Bonnes réponses des `multi`** : m020 Q1 3/6, m020 Q5 4/6, m021 Q2 2/6. Q1 est devinable : la consigne citée
  dit « at least three sound arguments » et la clé en compte trois, comme 04/07 Q5 (même consigne « at least 3 »,
  même 3/6) (M11). Correctif vérifié — option f devient un argument recevable, 4 sur 6 :
  - f : `Holidays in Tunisia cost less than in most of Europe.` (53 car. ; la plus longue reste a, 55) ;
  - clé : `["a", "c", "e", "f"]` ;
  - explication : `To persuade tourists, an argument must give them a reason to come: warm beaches, Roman sites to visit, a warm welcome with good food, and prices lower than in most of Europe. The number of inhabitants is a fact that gives no reason to travel, and the number of followers is about the writer, not about the destination.`
- **difficulty 3 d'un `ordering` de 4 phrases (m020 Q10) : non justifié.** L'ordre est entièrement porté par les
  marqueurs : seule phrase sans connecteur en tête, « First », « Then », « For these reasons » ; aucune décision de
  sens. → difficulty 2. Même constat pour m021 Q10 (conseil évident face à trois options extrêmes) et Q12 (la clé
  recopie le cadre de l'énoncé) → difficulty 2.
- **Étage** : après ces baisses, m020 n'a plus aucune question d3 pour une mission d3 boss. Correctif minimal :
  m020 Q1 et Q5 (`multi` à 6 énoncés, tout-ou-rien, sans nombre annoncé après le correctif M11) passent en
  difficulty 3 ; m021 garde Q11 en d3 (lien logique entre deux mots d'aide, piège de l'inversion cause/effet). Si
  l'orchestrateur préfère, m020 descend en d2 practice 75/15 (contraire à la ligne du plan, arbitrage au pilote).
- m020 Q10, « would » (m8) : « I would prefer » / « I would choose » emploient un « would » non enseigné (PLAN § 4). Remplacer
  c par `I prefer to live in the city.` et d par `For these reasons, the city is my choice.` ; l'ordre c, b, a, d reste
  unique.

### 2.7 Paire proche et gabarits ; doublons avec m012 et m022–m024

- **08/07 Q2 ↔ 09/11 Q5 (0,45)** : même phrase officielle (2023 G), deux blancs différents (« more », « At ») : pas un
  doublon, mais une **fuite** : l'énoncé de 08/07 Q2 (L03) imprime « At a young age », clé de m016 Q5 (M2).
  Correctif pour L03, vérifié (la clé « more » reste unique par « than ») :
  `(Exam 2023, general) A text about children and chores says: "…children are capable of handling (much / more / most) than we may believe." Which word completes the sentence?`
- **04/07 Q2 ↔ 09/15 Q3** (« What exactly must the article do? ») : même cadre de tâche, autres sujets et autres
  verbes de tâche (conseiller / expliquer une importance) ; le savoir-faire est voulu parallèle (R3). **Pas un
  doublon** ; mineur : varier le cadre de 09/15 Q3, prompt fin : `…Which plan answers the task?` à la place de
  `What exactly must the article do?` (options et clé inchangées, vérifié).
- **04/07 Q5 ↔ 09/15 Q1** (« Which of these points are sound arguments… », 3 sur 6, « at least 3 ») : gabarit
  identique jusqu'au nombre de clés → **majeur** (M11), corrigé par le passage à 4 sur 6 ci-dessus.
- **Doublons et fuites avec m012 (04/07) et m022–m024 (07/06–08)**, recherche par 6-grammes et par phrases-clés sur
  tous les fichiers `english` de la branche :
  - m012 : aucun doublon d'item ; seulement les deux gabarits ci-dessus.
  - **m023 Q11 (07/07)** demande « help ___ » → themselves (2019 G) ; **m018 Q11 imprime « helping people who may not
    be able to help themselves »** : fuite de L04 vers L06 (M8).
  - **m024 Q9 (07/08)** imprime « Joan is proud of her ___ » : fuite de L06 vers m016 Q12 (M3).
  - m022 : aucun recoupement.
  - Autres recoupements (même texte d'examen dans deux missions, blancs différents, sans fuite) : m016 Q8 / m017 Q6
    (2020 T) ; m016 Q5 / m018 Q7 (2023 G) ; m017 Q1 / 02/07 Q5 (2023 T) ; m018 Q2 / 02/07 Q1 (2026 G) ; m016 Q6 /
    01/06 Q2 (2019 G). OK.

### 2.8 Clés plus longues d'un mot (8 cas)

11#8 « after » (for, at), 11#9 « about » (with, at), 11#11 « from » (of, for), 12#10 « Although » (But, And), 13#1
« earn » (pay, buy), 13#8 « protectors » (loggers, offenders), 13#9 « reduce » (ruin, waste), 13#10 « inspiration »
(relation, dedication). **Tous acceptés** : les huit sont des options **officielles**, imprimées telles quelles
(aucune ajoutée par l'auteur) ; un mot seul, à trois options (hasard 33 %), sans parenthèse ni marque ; L04 en
compte 8 sur 51 QCM simples (16 %), sous le hasard, et sans pente (aucune clé n'est la plus longue de façon
répétée dans un même exercice au-delà du hasard : m018 4/12 à trois options). Réécrire des options officielles
serait infidèle. Seul 12#10 tient à la notion non enseignée (M5), réglée par le cours.

## 3. Défauts classés

### Critique

Aucune clé fausse. Un énoncé à deux réponses défendables :

- **M12 — m020 Q7 (2017 G)** : la consigne « DO NOT WRITE YOUR NAME OR SIGN » n'est pas dans l'énoncé ; « …Your loving
  son/daughter, Karim Ben Salah » se défend alors (on signe un discours). Prompt de remplacement, vérifié (la clé d
  reste unique ; aucune autre question de m020 sur l'anonymat) :
  `(Exam 2017, general) You give a speech to thank your parents after the national exam. The exam says: "DO NOT WRITE YOUR NAME OR SIGN." The frame starts with "Dear Mum and Dad," and ends with "Your loving son/daughter". Which ending is right for the speech?`

### Majeurs

- **M1 — m016 Q4 → Q8 (fuite interne)** : « chores teach children to look after others » donne « look after », clé de
  Q8. Prompt : `(Exam 2025, general) A text explains that household chores teach children useful skills. Which word completes the sentence?` (+ la phrase officielle inchangée).
- **M2 — fuites vers m016 Q5 (« At » + âge)** : (a) m016 Q12 : « who won a poetry competition at twelve ». Prompt :
  `(Exam 2013, general) A text presents Jane Parker, a creative girl who won a citywide poetry competition. Which word completes the sentence?` ;
  (b) 08/07 Q2 (L03) : correctif au § 2.7.
- **M3 — m024 Q9 (L06) → m016 Q12** : « Joan is proud of her ___ » donne « proud of ». Correctif pour L06, vérifié
  (après « her », seul le nom « choice » convient ; l'explication de m024 ne cite pas « proud ») :
  `(Exam 2022, technical) Joan left her job as a waitress to follow a training program in construction. Complete the sentence: "…her ___ and has become an active member in her community."`
- **M4 — m016 Q6, la question donne sa clé** : « lights are turned off for a short time ». Prompt :
  `(Exam 2019, general) A text presents Earth Hour, an evening event when people switch off unnecessary lights. Which word completes the sentence?`
- **M5 — m017 : However, Besides, Although non enseignés** : correctif de cours au § 2.3.
- **M6 — m017 Q9 → m007 Q6 (signalé par L02, vérifié)** : « because he hasn't got his ladder » donne « got ». Le texte
  proposé par L02 (« …because he hasn't … his ladder. ») est juste mais met une ellipse de plus dans une phrase à
  blanc ; je retiens la coupe, vérifiée (« But » reste seul : le métier de peintre fait attendre le travail ; « So »
  et « Also » restent faux ; l'explication ne cite pas « got ») :
  `(Exam 2013, technical) A short text about Jim, a painter who loses his ladder. Which word fits the gap?\n"Jim is a painter. ___ he isn't working today…"`
- **M7 — m017 Q12 → m006 Q12 et m007 Q8 (signalé par L02, vérifié)** : « have been close friends… while Dave is
  moving » donne « have been » et « is leaving ». Le contexte proposé par L02 est repris, mais il ne suffit pas : la
  phrase officielle citée (« Dave and Jenny have been an important part… ») et l'explication (« Because they have
  been important… ») impriment encore « have been », la clé de m007 Q8. Correctif complet, vérifié (« so » reste
  seul : l'importance de l'autre rend l'adieu difficile) :
  - prompt : `(Exam 2006, unique) A text about two old friends and neighbours, Dave and Jenny, who must say goodbye. Which word fits the gap?\n"…an important part of each other's lives; ___ it's difficult to say goodbye."`
  - explication : `They mean a lot to each other, so saying goodbye is hard: the second part is a consequence of the first, so "so". "but" would oppose the two ideas, and "until" would give a time limit that the sentence does not need.`
- **M8 — m018 Q11 → m023 Q11 (L06)** : « help themselves ». Phrase citée coupée, vérifiée (« role » reste seul) :
  `"It gives you the satisfaction of playing a ___ in someone else's life."` ; l'explication ne cite pas
  « themselves » : rien d'autre à toucher.
- **M9 — m018 Q12, « I wish » non enseigné** : remplacement au § 2.4.
- **M10 — m019 Q1 donne sa paire 1** : « pupils trained as anti-violence ambassadors ». Prompt :
  `(Exam 2026, general) A paragraph about a Kent primary school that fights violence among pupils. Match each sentence beginning with the part that completes it. (The exam also printed one ending that fits none of the beginnings; it is left out here.)`
- **M11 — m020 Q1, nombre devinable et gabarit de 04/07 Q5** : correctif au § 2.6.
- **M13 — m021 Q5 (2012 G), appariement non unique** : les qualités sont imprimées, les moyens de transport sont de
  l'auteur, et « cheap » ou « comfortable » vont aussi au train. Colonne B de remplacement, vérifiée (une seule
  bijection : cheap → ticket d'un dinar, comfortable → sièges et climatisation, long distances → traverse le pays,
  sightseeing → s'arrête où l'on veut) :
  - r1 `the train, which crosses the whole country` · r2 `the public bus, with a one-dinar ticket` · r3 `a hired car that stops wherever you like` · r4 `a taxi with soft seats and air conditioning` ; clé inchangée (l1-r2, l2-r4, l3-r1, l4-r3) ;
  - explication : `The public bus has the cheapest ticket. A taxi with soft seats and air conditioning is the most comfortable way. The train crosses the whole country, so it is good for long distances. A hired car can stop at any place on the road, so it allows sightseeing.`
- **M14 — m021 Q12** : la consigne d'anonymat que vise la question n'est pas dans l'énoncé, et la clé recopie le cadre.
  Prompt, vérifié (a reste seule ; b viole la consigne, c n'est pas l'élève, d ne respecte pas le cadre) :
  `(Exam 2009, general) You write to your pen-friend, a heavy smoker, to warn him against the dangers of smoking. The exam says: "DO NOT WRITE YOUR NAME OR SIGN THE LETTER." The frame starts with "Dear Chris(tine)" and ends with "Your friend" and "Karim(a)". How do you end the letter?` ; difficulty 2.
- **M15 — m016 : prépositions non enseignées** : ligne de cours au § 2.1.

### Mineurs

- **m1 — m016 Q6, explication** : « "about" does not fit before a duration » est faux (« about an hour » existe).
  Remplacer par : `"For" + a length of time says how long something lasts: the lights stay off for one hour. "from" would need an end point ("from 8 to 9"), "at" names a single moment on the clock, and "about" alone only means "roughly": "turn off" still needs "for" to say how long the lights stay off.`
- **m2 — m016 Q11, explication** : « "for" would mean the equipment is meant to give irritation » est faux. Remplacer
  par : `"Protect something from" a danger means to keep the danger away from it: good equipment keeps irritation and injuries away from the eyes. "protect … of" copies the French "protéger de", and "protect … for" would name the person or the purpose the protection is for, not the danger.`
- **m3 — fidélité des cadres et contextes** : m021 Q1 omet la signature imprimée du cadre (« Yours, » / « Wahid /
  Wahida ») : écrire `…ends with "Yours," and "Wahid / Wahida".` ; m017 Q1 gagnerait la phrase officielle qui précède
  (« Gilbert has got big plans. ») pour que « Besides » (ajouté) tombe par le sens : citer
  `"Gilbert has got big plans. He wants to be a welder. ___, he lived in poverty with his grandmother in Spain."`
- **m4 — m017 Q2, explication de « However »** : § 2.3.
- **m5 — m019 Q9** : supprimer « Match by meaning. » (consigne redoublée).
- **m6 — m019 Q10** : note de l'intrus fausse (§ 2.5).
- **m7 — m020 Q9** : `english.write.phrase-hors-sujet` sur c (« The city and the countryside are two different
  places ») : l'option est dans le sujet, elle ne choisit pas ; le libellé ne nomme pas l'erreur → la laisser muette.
- **m8 — m020 Q10** : « would » (§ 2.6) et difficulty 3 → 2.
- **m9 — m021 Q2** : d (« television on all night ») et e (« lights on in the garden all day ») ne sont l'erreur
  d'aucun élève. Remplacer d par `Wash the dishes under running water.` et e par `Leave the charger plugged in when the phone is full.` (deux gaspillages courants, faux ; 36 et 52 car., les clés 44 : aucune n'est la plus longue) ; dans l'explication, remplacer
  « a television left on all night, lights on in the daytime » par « dishes washed under running water, a charger
  left plugged in ». Clé inchangée (a, c), 2 sur 6.
- **m10 — difficulty** : m021 Q10 et Q12 → 2 ; m020 Q1 et Q5 → 3 (§ 2.6).
- **m11 — m020 Q3** : cadre « What exactly must the article do? » identique à 04/07 Q2 (§ 2.7).

## 4. Étiquettes `english.*`

Existantes, toutes relues sur `origin/main` :

- `english.link.connecteur-de-mauvais-type` (m017, 15 options) : exact pour chaque option portée (un connecteur d'un
  autre rapport) ; « However » de Q2, bon type mais mauvaise construction, est à juste titre muet ;
- `english.link.cause-et-consequence-inversees` (m021 Q11 b) ; `english.modal.to-en-trop`,
  `english.verb.base-verbale-deformee` (m021 Q4) ; `english.comp.double-marque`,
  `english.comp.comparatif-et-superlatif-confondus` (m021 Q6) : exacts ;
- `english.write.phrase-hors-sujet` (m020 Q9 c) : à retirer (m7).

Famille proposée : `english.prep.preposition-calquee`, **acceptée sur 6 questions / 7 options** (§ 2.2).

## 5. Résumé

- **Questions auditées : 68 ; clés fausses : 0.**
- **Critique : 1** — m020 Q7 (consigne d'anonymat absente : deux réponses défendables).
- **Majeurs : 14** — fuites : m016 Q4→Q8, m016 Q6 (sa propre clé), m016 Q12 et 08/07 Q2 (L03) → m016 Q5, m024 Q9
  (L06) → m016 Q12, m017 Q9 → m007 Q6, m017 Q12 → m006 Q12 et m007 Q8 (le correctif de L02 ne suffit pas : la
  phrase citée et l'explication impriment encore « have been »), m018 Q11 → m023 Q11, m019 Q1 (sa paire 1) ; notions
  non enseignées : prépositions (une ligne de cours au 09, SB p. 6, 97, 99), However / Besides / Although (trois
  retouches de « Linking ideas »), « I wish » (m018 Q12 remplacée par « shy », 2018 G) ; m020 Q1 (nombre devinable,
  gabarit de 04/07 Q5) ; m021 Q5 (appariement non unique) ; m021 Q12.
- **Mineurs : 11** — deux explications fausses (m016 Q6, Q11), cadres, note de l'intrus de 2001 (deux répliques en
  trop, pas une), étiquette de m020 Q9, « would », distracteurs absurdes de m021 Q2, difficultés.
- **Points tranchés** : 2022 T → 2019 G justifié ; intrus de m019 perdu : adaptation acceptée, déclarée ; 2001
  unique ; `ordering` de 4 phrases en d3 non justifié (→ d2, étage de m020 porté par ses deux `multi`) ; 8 clés plus
  longues d'un mot : acceptées (options officielles).
- **Étiquette** : `english.prep.preposition-calquee` acceptée (Q4, Q5, Q7, Q10 ×2, Q11, Q12) ; Q2 et Q9 rejetées.
- **Doublons** : aucun doublon d'item ; un gabarit majeur (04/07 Q5 ↔ 09/15 Q1), un mineur (04/07 Q2 ↔ 09/15 Q3) ;
  quatre fuites croisées avec L02, L03, L06.
- **Verdict : à corriger avant merge.** Les correctifs tiennent dans les fichiers du lot, deux retouches de cours au
  09 (`cours.md`, `resume.md`, `sources[]`), une entrée au registre des étiquettes, et trois retouches hors lot
  (08/07 Q2 pour L03, m024 Q9 pour L06 ; m023 n'a rien à changer).
