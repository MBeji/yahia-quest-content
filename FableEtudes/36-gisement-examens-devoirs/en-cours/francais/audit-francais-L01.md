# Audit indépendant — lot L01, français 9ᵉ, chapitre 09 (missions 06–11)

Auditeur indépendant, 2026-10-16. Branche `wip/gisement-francais-9eme`, commit `adad1273`. Périmètre :
`content/french/09-comprehension-production-ecrite/exercices/06…11` + `chapter.json` (`sources[]`).
Sources lues : transcriptions 2026 G, 2025 G, 2023 G, 2026 T, 2024 T, 2025 T, 2019 G, 2015 T, 2009 T, 2011 T ;
missions publiées 09/01–05, quiz 09, 08/01, 08/04, 08/05 ; registre `misconceptions.json` (`origin/main`).
Aucun fichier audité modifié, aucune écriture git.

Gates (moteur `/home/user/eng-svtses`, contenu = ce worktree) : `content:check` vert ; `content:tranche
--chapters 09` : clé strictement la plus longue 0/71, aucune paire proche, 1 groupe gabarit (§ 8) ;
`content:qa --strict` : **1 erreur hors lot** — `french-1ere-sec/06-oeuvre-integrale-la-nouvelle/cours`,
recouvrement de 9 mots avec `web-9eme-base-french` (anti-verbatim). Rien dans `sources-externes/` n'est versionné
par cette branche : sans doute les instantanés locaux des devoirs ; à vérifier avant le push (si la CI la voit,
`content-ci` sera rouge).

Méthode : chaque question re-résolue à l'aveugle avant lecture de la clé ; chaque citation recherchée mot pour mot
dans la transcription ; chaque correctif vérifié par script (longueurs, citations littérales, clé ni strictement
la plus longue ni strictement la plus courte).

**Clés fausses : 0.** Les défauts viennent des fuites entre questions (paires « case + justification » posées en
deux questions alors que le donjon tire au hasard), de deux énoncés qui livrent la clé, de quatre explications qui
désignent les options par leur rang, et d'une paraphrase fausse du texte.

---

## m001 — `06-examen-2026-g-comprehension-artiste-avant-le-concert.json` (8 q.)

| Q | ma réponse | clé | verdict | motif |
|---|---|---|---|---|
| 1 multi | a, c, e | a, c, e | réserve | le distracteur « pas décidé » revient en Q7 ; citations de l'explication pas littérales |
| 2 | b | b | réserve | l'explication confirme « gorge sèche » = effet du trac (option de Q1) |
| 3 matching | l1-r1, l2-r2, l3-r3 | idem | **majeur** | « l'agitation nerveuse » n'est pas un sentiment ; agitation et trac se prouvent par le même malaise ; « long chemin » repris en Q4 |
| 4 | b | b | réserve | l'énoncé cite « fière d'avoir parcouru ce long chemin » : il donne la paire fierté de Q3 |
| 5 | b | b | OK | fidèle (« la peur disparut subitement » après « Bonsoir ») ; question ajoutée utile |
| 6 | c | c | **majeur** | même geste que Q8 (qualité prouvée par une attitude) ; énoncé à la 3ᵉ personne qui cite « en m'efforçant » |
| 7 matching | l1-r1, l2-r2, l3-r3 | idem | OK | « volonté sans faille » = persévérance défendable (elle explique le long parcours) ; « pas décidé » = détermination |
| 8 | c | c | **majeur** | « seule, debout sur la scène » décrit la situation, pas une action courageuse ; option a reprend « estomac noué » (clé de Q1) |

**Fragments répétés (point signalé).** « cent pas » n'apparaît qu'en Q1 : rien à faire. « pas décidé » : Q1 (leurre)
et Q7 (clé) — à retirer de Q1. « long chemin » : Q3 (clé) et énoncé de Q4 — à retirer de Q4.

**Questions ajoutées (Q4, Q5, Q6).** Q4 et Q5 sont fidèles et utiles (origine du parcours ; moment où la peur
cède). Q6 fait double emploi avec Q8 : la supprimer. La mission passe à 7 questions (R7 : 6 à 12).

### Correctifs m001

- **Q1** option b → `"« Le public était venu nombreux »"`. Explication → « Le malaise se voit dans le corps et les
  gestes de Prodige : elle fait « nerveusement les cent pas », elle sent « mon estomac noué et contracté » et
  « ma gorge était nouée et sèche ». Que le public soit venu nombreux est un fait, pas un signe de malaise ; les
  applaudissements n'arrivent qu'une fois Prodige sur scène. »
- **Q2** explication, dernière phrase → « Avoir soif ne cause pas le trac : c'en est un effet. »
- **Q3** `l2` → `"La joie"`, `l3` → `"La peur"`, `r2` → `"« Quelle émotion de penser que tous ces gens étaient là
  pour me voir »"` (r1 et r3 inchangés). Explication → « La fierté se lit dans « fière d'avoir parcouru ce long
  chemin ». La joie éclate dans « Quelle émotion de penser que tous ces gens étaient là pour me voir ». La peur se
  ressent dans le corps : le ventre qui se tord et se serre. Un sentiment se prouve par un indice précis du
  texte. » (citations vérifiées ; la joie et la fierté ne s'échangent pas : « fière » fixe la première paire.)
- **Q4** énoncé → « Prodige se remémore « les grandes étapes de [sa] vie ». D'où est-elle partie, selon le
  texte ? » (« les grandes étapes de ma vie » : littéral.)
- **Q6** : supprimer la question.
- **Q8** options → a `"Elle est nerveuse : « je n'arrivais pas à rester sagement assise »."` (67) ;
  b inchangée (46) ; c `"Elle est courageuse : « En m'efforçant d'ignorer autant que possible le trac »."` (74) ;
  d `"Elle est joyeuse : « Un tonnerre d'applaudissements résonna dans la salle »."` (76). Clé c (ni la plus longue
  ni la plus courte). Explication → « Le courage, c'est agir malgré la peur : elle s'efforce d'ignorer le trac et
  avance. « Nerveuse » est un état, pas une qualité qui aide à réussir. « J'avais très soif » ne montre aucune
  persévérance. Les applaudissements sont un fait extérieur : ils ne prouvent pas que Prodige est joyeuse. »
  (« sagement assise » n'est plus utilisé en Q3 : pas de répétition ; l'ancienne Q6, qui citait la même phrase,
  est supprimée.)

---

## m002 — `07-examen-2025-g-comprehension-portrait-serveuse.json` (8 q.)

| Q | ma réponse | clé | verdict | motif |
|---|---|---|---|---|
| 1 multi | a, d | a, d | OK | le vrai/faux devient `multi` : chaque proposition reste jugée, 2 vraies sur 4 comme au sujet |
| 2 matching | 4 paires | idem | OK | guillemets imbriqués en r2 (mineur, typographie) |
| 3 | b | b | OK | ajout fidèle (comparaison « ballet acrobatique ») et utile ; figures vues au ch. 07 |
| 4 multi | a, c, e | a, c, e | OK | 4ᵉ paragraphe vérifié ; leurres pris aux paragraphes 1, 2 et 5 |
| 5 | b | b | **majeur** | l'énoncé cite « ne serait peut-être pas serveuse toute sa vie » : la clé « Peut-être pas » est recopiée ; clé strictement la plus courte |
| 6 | c | c | mineur | ajout fidèle (« pour cause d'ennui ») ; clé strictement la plus courte (32 contre 37–55) |
| 7 | c | c | **majeur** | paraphrase fausse : « ça ne pressait pas » ne veut pas dire que le narrateur « ne presse pas Tania » |
| 8 | c | c | OK | qualité + indice ; leurres bien construits |

**Questions ajoutées.** Q3 (ballet) : fidèle et utile. Q6 (raison de l'interruption) : fidèle, simple
repérage, acceptable. Q7 : utile une fois l'énoncé corrigé. **Q1 en `multi` : validé.**

### Correctifs m002

- **Q5** énoncé → « Selon le narrateur, Tania restera-t-elle définitivement serveuse ? » ; option b →
  `"Peut-être pas : elle finira probablement ses études un jour."` (60 ; les autres font 56, 58, 60). Explication
  inchangée (elle cite « peut-être pas » et « probablement », qui sont dans le texte).
- **Q6** option c → `"Elle s'ennuyait pendant ses études universitaires."` (50 ; autres : 45, 35, 55).
- **Q7** énoncé → « Selon le narrateur, terminer ses études « ne pressait pas » pour Tania. Pour quelle raison,
  d'après la fin du texte ? » (« ne pressait pas » : littéral.)

---

## m003 — `08-examen-2023-g-comprehension-enfant-face-a-l-incendie.json` (7 q.)

| Q | ma réponse | clé | verdict | motif |
|---|---|---|---|---|
| 1 | c | c | **majeur** | l'explication cite « presque arrivé à la remise » et « il continue d'avancer » : elle donne Q2 ; Q2 donne Q1 en retour |
| 2 | c | c | **majeur** | seule l'option c parle de l'enfant : elle s'élimine à vue ; sa clé « j'avançais » répond à Q1 |
| 3 multi | a, c | a, c | réserve | correct ; l'explication de Q3 et l'énoncé de Q4 se croisent (voir Q4) |
| 4 | c | c | **majeur** | l'énoncé « quand Mme Schaeffer lui ordonne de reculer » donne la clé c de Q3 |
| 5 matching | 3 paires | idem | OK | courage, franchise, altruisme : univoque |
| 6 | b | b | **majeur** | clé « De l'admiration. » strictement la plus courte et seule sans « lui » ; l'explication cite la brigade, donc la clé de Q7 |
| 7 | b | b | **majeur** | aucun leurre ne parle de l'enfant en particulier : élimination à vue |

**Enchaînement Q6–Q7 (point signalé).** Fuite de Q6 vers Q7 par l'explication, plus des leurres de Q7 qui
s'éliminent sans lire. Correctif ci-dessous : les deux questions restent, sans fuite.
**Enchaînement Q1–Q2 :** même défaut que les paires de m004 et m005. Je fusionne Q1 et Q2 en une question 2×2
(action × phrase). La mission passe à 6 questions.

### Correctifs m003

- **Q1 + Q2** → une seule question (garder l'id de Q1, supprimer Q2) :
  énoncé « Dans ce récit, un enfant d'une dizaine d'années voit l'habitat du gardien de l'école prendre feu. En
  voyant les flammes, que fait-il, et quelle phrase du texte le prouve ? » ; options
  a `"Il avance vers la remise : « J'avais peur mais j'avançais quand même. »"` (71, clé) ;
  b `"Il avance vers la remise : « Il faut sauver le gardien ! »"` (58) ;
  c `"Il fuit loin de la remise : « J'avais peur mais j'avançais quand même. »"` (72) ;
  d `"Il fuit loin de la remise : « Il faut sauver le gardien ! »"` (59). Plan 2×2, chaque valeur deux fois, toutes
  muettes. Explication → « Il avance malgré la peur : « J'avais peur mais j'avançais quand même. » Cette phrase
  dit l'action elle-même. « Il faut sauver le gardien ! » dit ce qu'il veut, pas ce qu'il fait, et il le crie plus
  tard. Fuir est le contraire de ce que raconte le texte. »
- **Q3** explication → « Mme Schaeffer agit pour le retenir : elle le saisit par l'épaule et le tire en arrière,
  puis lui ordonne de reculer. « Je l'ai quand même un peu aidée » montre l'enfant qui l'aide, pas Mme Schaeffer
  qui le retient ; l'arrivée des pompiers est une autre scène ; « Il faut sauver le gardien ! » est la réplique de
  l'enfant. »
- **Q4** énoncé → « L'enfant refuse d'obéir à Mme Schaeffer, qui veut l'empêcher d'avancer. Pour quelle
  raison ? »
- **Q6** option b → `"De l'admiration pour lui."` (25 ; autres : 24, 21, 26). Explication → « Le chef des
  pompiers vient voir l'enfant, et lui seul, et lui donne une tape dans le dos : il admire ce qu'il a fait. La
  colère est exclue, et rien ne montre de la pitié ou de la jalousie. »
- **Q7** énoncé → « Après l'incendie, le chef des pompiers vient voir l'enfant. Quelle phrase du texte montre le
  mieux ce que le chef pense de lui ? » ; options a `"« me disant que j'avais sauvé Yves »"` (36) ; b clé inchangée
  (50) ; c inchangée (61) ; d `"« elle n'arrêtait pas de m'engueuler »"` (38). Explication → « Dire qu'il serait
  « heureux de [le] compter dans ses rangs », c'est montrer son estime pour l'enfant. « me disant que j'avais
  sauvé Yves » et « elle n'arrêtait pas de m'engueuler » sont des paroles et des gestes de la directrice, pas du
  chef ; la dernière phrase raconte ce que les pompiers font pour tous les élèves. » (Toutes les citations sont
  littérales. a et d testent le piège « mauvais personnage ».)

---

## m004 — `09-examen-2026-t-comprehension-reve-de-footballeur.json` (7 q.)

| Q | ma réponse | clé | verdict | motif |
|---|---|---|---|---|
| 1 | d | d | **majeur** | l'explication cite « deviendrait footballeur professionnel » = clé de Q2 ; clé la plus courte |
| 2 | b | b | **majeur** | la clé répond à Q1 ; aucun autre leurre ne parle d'avenir ; explication « la deuxième phrase » (rang d'option) |
| 3 | c | c | **majeur** | « Non, à personne. » : clé strictement la plus courte, seul « Non » face à trois « Oui » |
| 4 | b | b | **majeur** | l'énoncé « comment Angel garde son rêve pour lui » donne la clé de Q3, et la clé de Q4 la contient (point signalé : confirmé) |
| 5 | d | d | OK | réaction : enthousiasme + curiosité |
| 6 | b | b | mineur | leurre d « Tous les joueurs du club » nie la prémisse « pour deux joueurs » |
| 7 multi | a, c, e | a, c, e | mineur | leurre d « examens de fin d'année » sans lien avec le texte ; l'explication dit que le match contre l'équipe de France est le rêve d'Angel, ce qui oriente Q1 |

### Correctifs m004 (7 questions conservées)

- **Q1 + Q2** → une question 2×2 (id de Q1) : énoncé « Angel, huit ans, s'entraîne au club de football de
  Saint-Antonin. De quoi rêve-t-il, et quelle phrase du texte le prouve ? » ; options
  a `"D'être footballeur professionnel : « jouerait sur les plus grands stades du monde »"` (83, clé) ;
  b `"D'être footballeur professionnel : « Après la belle victoire de Saint-Antonin »"` (79) ;
  c `"De devenir entraîneur professionnel : « jouerait sur les plus grands stades du monde »"` (86) ;
  d `"De devenir entraîneur professionnel : « Après la belle victoire de Saint-Antonin »"` (82). Explication →
  « Angel imagine qu'il « jouerait sur les plus grands stades du monde » : c'est le rêve d'un footballeur, pas d'un
  entraîneur. « Après la belle victoire de Saint-Antonin » dit seulement quand il fait ce rêve : la phrase ne
  prouve rien sur le rêve lui-même. »
- **Q2 (nouvelle, à la place de l'ancienne Q2)** : énoncé « Le mercredi suivant, à l'entraînement, Angel
  « redescend sur terre ». Que veut dire cette expression ici ? » ; options a `"Il revient à la réalité, avec des
  espoirs modestes."` (51, clé) ; b `"Il tombe pendant l'entraînement et se blesse."` (45,
  `fr.lexique.sens-figure-lu-au-propre`) ; c `"Il abandonne pour toujours son rêve de football."` (48,
  `fr.lecture.deduction-sans-indice`) ; d `"Il rentre chez lui après le match de Saint-Antonin."` (51,
  `fr.lecture.deduction-sans-indice`). Difficulté 2. Explication → « L'expression est au sens figuré : après avoir
  rêvé, Angel revient à la réalité. Le texte le dit aussitôt : s'il peut refaire ses exploits du dernier match, « ce
  sera déjà merveilleux ». Il ne tombe pas, il n'abandonne rien et il est à l'entraînement, pas chez lui. »
- **Q3 + Q4** → une question 2×2 (id de Q3, supprimer Q4) : énoncé « Angel a un rêve qui lui est cher. En parle-t-il
  autour de lui, et quelle phrase du texte le prouve ? » ; options
  a `"Non, il n'en parle à personne : « Il n'en parle à personne, même pas à Charly »"` (79, clé) ;
  b `"Non, il n'en parle à personne : « J'ai une grande nouvelle ! annonce-t-il à ses joueurs. »"` (90) ;
  c `"Oui, il en parle à Charly : « Il n'en parle à personne, même pas à Charly »"` (75) ;
  d `"Oui, il en parle à Charly : « J'ai une grande nouvelle ! annonce-t-il à ses joueurs. »"` (86). Explication →
  « Le texte le dit : « Il n'en parle à personne, même pas à Charly », de peur qu'il se moque de lui. La grande
  nouvelle est annoncée par l'entraîneur, pas par Angel : elle ne dit rien de son silence. »
- **Q4 (nouvelle, après l'actuelle Q5)** : énoncé « « Depuis que Frank a parlé du stage, Angel n'a plus que
  Montilleux en tête. » Qui est Frank ? » ; options a `"L'entraîneur d'Angel."` (21, clé) ; b `"Un camarade d'équipe
  d'Angel."` (29, `fr.lecture.deduction-sans-indice`) ; c `"Le directeur du stage."` (22,
  `fr.lecture.deduction-sans-indice`) ; d `"Le père d'Angel."` (16, `fr.lecture.deduction-sans-indice`).
  Difficulté 2. Explication → « C'est l'entraîneur qui a annoncé le stage à ses joueurs : Frank est donc
  l'entraîneur. Aldo Montini dirigera le stage mais n'a parlé à personne ; aucun camarade ni le père d'Angel
  n'annonce quoi que ce soit. »
- **Q6** option d → `"Les deux plus jeunes joueurs du club."` (37 ; autres : 41, 52, 61), même étiquette
  `fr.lecture.deduction-sans-indice`. Fin de l'explication → « …ni les premiers à réagir, ni deux amis déjà
  choisis, ni les plus jeunes. »
- **Q7** option d → `"participer à un tournoi en Auvergne"` (36). Explication → « L'entraîneur annonce trois
  activités : une formation de professionnel, des balades et des visites entre les entraînements, la rencontre de
  champions ou de futurs champions. Ni match contre l'équipe de France ni tournoi ne sont prévus. »

Ordre final : 2×2 rêve · « redescend sur terre » · 2×2 silence · réaction · Frank · qui participera · activités.

---

## m005 — `10-examen-2024-t-comprehension-amitie-d-ecole.json` (7 q.)

| Q | ma réponse | clé | verdict | motif |
|---|---|---|---|---|
| 1 | c | c | **majeur** | l'explication cite la clé de Q2 ; la clé de Q2 contient « collège » |
| 2 | d | d | **majeur** | même paire 1a/1b : fuite dans les deux sens |
| 3 | c | c | **majeur** | clé = mot pour mot la clé de Q4 ; l'énoncé de Q4 donne la clé de Q3 |
| 4 | b | b | **majeur** | énoncé qui livre Q3 ; explication par rangs (« la deuxième phrase », « la dernière ») |
| 5 multi | a, c | a, c | **majeur** | l'énoncé « habitué du collège » livre la clé de Q1 |
| 6 | a | a | **majeur** | seule la clé reprend « deviné » de l'énoncé ; l'explication cite « Les familles ne se fréquentaient pas » (clé de Q3) |
| 7 | a | a | **majeur** | les leurres b et d recopient la clé de Q6 ; le leurre c recopie la clé de Q3 ; explication par rangs ; « aussi une seconde raison » renvoie à Q6 |

**Retouche « ne se fréquentaient pas » (point signalé).** Le sujet officiel propose « ne se connaissaient pas ».
Le texte dit « ne se fréquentaient pas », et le père de Charles est « une personnalité de la ville » : « ne se
connaissaient pas » est une inférence, la retouche est plus exacte. **Retouche validée**, mais elle rend la clé de
Q3 identique à celle de Q4. Dans le 2×2 ci-dessous, la case dit « ne se voyaient pas » (paraphrase) et la preuve
cite la phrase.
**Enchaînement Q6–Q7 (point signalé)** : fuite confirmée (les leurres de Q7 reproduisent la clé de Q6). Correctif
ci-dessous. La mission passe à 6 questions.

### Correctifs m005

- **Q1 + Q2** → 2×2 (id de Q1) : énoncé « Antoine, le narrateur, raconte comment il est devenu l'ami de Charles
  Descombes. Où sont-ils devenus amis, et quelle phrase du texte le prouve ? » ; options
  a `"Au collège : « le jour où nous nous sommes rencontrés au collège »"` (66, clé) ;
  b `"Au collège : « au début d'un mois d'août accablé de chaleur »"` (61) ;
  c `"À l'école primaire : « le jour où nous nous sommes rencontrés au collège »"` (74) ;
  d `"À l'école primaire : « au début d'un mois d'août accablé de chaleur »"` (69). Explication → « Le narrateur
  connaît Charles « depuis le jour où nous nous sommes rencontrés au collège ». Le mois d'août est celui de la
  rencontre avec Séverine, des années plus tard : il ne prouve rien sur leur amitié. L'école primaire n'est pas
  mentionnée. »
- **Q3 + Q4** → 2×2 (id de Q3, supprimer Q4) : énoncé « Que dit le texte des familles d'Antoine et de Charles, et
  quelle phrase le prouve ? » ; options
  a `"Elles ne se voyaient pas : « nos familles ne se fréquentaient pas »"` (67, clé) ;
  b `"Elles ne se voyaient pas : « son père était une personnalité de la ville »"` (74) ;
  c `"Elles étaient proches : « nos familles ne se fréquentaient pas »"` (64) ;
  d `"Elles étaient proches : « son père était une personnalité de la ville »"` (71). Explication → « Le narrateur
  écrit que « nos familles ne se fréquentaient pas » : elles ne se voyaient pas. Que le père de Charles soit une
  personnalité de la ville dit une différence de rang, pas l'absence de relations. »
- **Q5** énoncé → « Charles est un habitué des lieux, Antoine est nouveau. Que fait Charles en rencontrant Antoine
  le premier jour ? »
- **Nouvelle question (après Q5)** : énoncé « Antoine et Charles se sont retrouvés assis côte à côte, et « il en a
  été ainsi durant toutes les studieuses années » jusqu'au baccalauréat. Que montre ce détail ? » ; options
  a `"Que leur amitié a duré toute leur scolarité."` (44, clé) ; b `"Que Charles aidait Antoine à faire ses
  devoirs."` (47, `fr.lecture.deduction-sans-indice`) ; c `"Qu'ils ont dû changer de pupitre chaque année."`
  (46, `fr.lecture.contraire-du-texte`) ; d `"Que le maître les avait placés côte à côte."` (43,
  `fr.lecture.deduction-sans-indice`). Difficulté 2. Explication → « Ils sont restés voisins de pupitre de leur
  rencontre jusqu'au baccalauréat : leur amitié a duré toute leur scolarité. Le texte ne parle ni de devoirs ni
  d'un maître, et ils n'ont pas changé de place. » (Citation littérale ; l'appel de note ² est omis.)
- **Q6** énoncé → « Dans le dernier paragraphe, le narrateur se demande pourquoi Charles s'est rapproché de lui.
  Quelle est la première raison qu'il suppose ? » ; option a → `"Charles a senti chez Antoine la même exigence que
  lui."` (54 ; autres : 53, 59, 56) ; option b : étiquette → `fr.lecture.deduction-sans-indice` (le texte ne dit
  rien d'un souhait de Charles sur les familles : ce n'est pas le contraire du texte). Explication → « Le narrateur
  suppose que Charles « avait deviné en [lui] une exigence pareille à la sienne ». Rien ne parle d'une rencontre
  des familles ni d'un adulte, et le narrateur ne prête à Charles aucun calcul sur son milieu. »
- **Q7** énoncé → « Dans le dernier paragraphe, le narrateur avance deux hypothèses sur ce qui a rapproché Charles
  de lui. Quelle phrase dit la seconde, introduite par « plus simplement » ? » ; options a clé inchangée (55) ;
  b `"« comme s'il désirait sceller immédiatement un pacte »"` (54) ; c `"« j'étais, moi, fils d'un modeste
  cordonnier »"` (46) ; d `"« Qu'est-ce qui avait bien pu l'inciter à se rapprocher de moi »"` (64). Explication →
  « La seconde hypothèse, « plus simplement », est que Charles « avait été touché par [sa] solitude dans cette
  cour ». Le pacte appartient au premier paragraphe et décrit la rencontre ; le fils de cordonnier dit ce qui
  aurait dû les séparer ; la question est celle que se pose le narrateur, pas sa réponse. »

Ordre final : 2×2 collège · 2×2 familles · actions (multi) · côte à côte · raison 1 · raison 2.

---

## m006 — `11-examens-2009-2025-production-projet-metier-justifier.json` (9 q., d3)

| Q | ma réponse | clé | verdict | motif |
|---|---|---|---|---|
| 1 | c | c | mineur | leurres a et d hors sujet évidents ; consigne citée sans « En classe, » |
| 2 ordering | b d a c | idem | OK | ordre unique (« D'abord » ne peut suivre « En effet ») |
| 3 | b | b | **majeur** | même geste que 08/01 Q3 (« car » / métier rêvé, liste « ne pas redemander ») ; l'énoncé nomme la relation (« la conséquence ») ; rien n'y vient de l'examen 2025 T |
| 4 | d | d | **majeur** | « ouvre le mieux le corps de la lettre » : la prise de nouvelles (a) est une ouverture usuelle, donc défendable ; leurre c = formule de fin (déjà au 15) ; consigne paraphrasée entre guillemets |
| 5 multi | a, c | a, c | mineur | consigne tronquée sans […] ; leurre d hors sujet évident |
| 6 multi | a, b, f | idem | OK | 3 sur 6, pour soi / pour la société |
| 7 | b | b | OK | « le mieux » départage la question ouverte (c), qui n'a pas de bilan |
| 8 | c | c | mineur | consigne paraphrasée ; explication « y réussir » ≠ option « le réussir » |
| 9 | b | b | **majeur** | explication par rangs (« La première phrase… la troisième… la dernière ») ; d est l'opinion adverse, pas « étrangère au sujet » |

**Variété des thèmes (point signalé)** : pâtissier, photographe, mécanicien, maçon (×2, Q6–Q7, même session), jardinier ;
aucun ne reprend vétérinaire (08/01), boulanger (09/04), guide de montagne (09/03), travail en équipe (quiz). Le
correctif de Q3 remplace photographe par infirmier. **Validé.**
**Distracteurs muets (point signalé)** : admis par R8 quand aucune étiquette n'est exacte. Trois étiquettes du
registre conviennent exactement et sont à poser : Q5 d et Q6 c → `fr.production.hors-sujet` ; Q6 e →
`fr.argu.argument-contraire-a-la-these`. Les autres restent muets (Q4 a/c, Q5 b/e, Q6 d, Q7 a/c/d, Q9 d).

### Correctifs m006

- **Q1** consigne → « En classe, ton professeur de français te demande de parler de ton projet d'avenir. Rédige un
  texte d'une dizaine de lignes dans lequel tu décris ton projet tout en donnant les raisons de ton choix. » ;
  option a → `"Décrire mon projet en détail, sans dire pourquoi je l'ai choisi."` (64,
  `fr.lecture.consigne-incomplete`) ; option d → `"Raconter une journée d'école, puis conclure."` (44,
  `fr.production.hors-sujet`). Clé c 56, b 60. Explication → « La consigne demande deux choses : décrire le projet
  ET donner les raisons du choix. Le plan présente donc le projet, justifie, puis conclut. Décrire sans dire
  pourquoi, ou donner des raisons sans dire quel est le projet, ne traite que la moitié de la consigne ; raconter
  une journée d'école sort du sujet. »
- **Q3** (même session) → énoncé « (Examen 2025, technique) Pour décrire son projet tout en donnant les raisons de son
  choix, un élève qui veut devenir infirmier prépare quatre phrases. Laquelle donne une RAISON de son choix, et non
  une description du projet ? » ; options a `"Je travaillerai dans un hôpital, avec des horaires de nuit."` (59) ;
  b `"Je ferai trois ans d'études après le baccalauréat."` (50) ; c `"Soigner les malades me donne le sentiment
  d'être utile."` (55, clé) ; d `"Je porterai une blouse blanche et un badge à mon nom."` (53). Leurres muets.
  Explication → « Une raison dit pourquoi on choisit ce métier : se sentir utile en soignant. Le lieu de travail,
  la durée des études et la tenue décrivent le projet, sans le justifier. La consigne attend les deux, mais il
  faut savoir les distinguer. » (Pas de doublon : 08/01 Q3 et 09/04 Q5 testent un articulateur et une grille
  argumentative.)
- **Q4** consigne → « Après avoir longuement réfléchi, tu décides enfin d'exercer un métier qui te plaît. Tu écris
  alors une lettre à l'un de tes amis pour lui annoncer la bonne nouvelle. » ; question → « Quelle phrase annonce le
  mieux, dès le début du corps de la lettre, la raison pour laquelle tu écris ? » ; option c → `"Je voulais te parler
  du film que j'ai vu samedi."` (48, `fr.production.hors-sujet`). Clé d 68, a 80, b 51. Explication → « Le corps de la
  lettre doit annoncer vite la nouvelle demandée : le choix du métier. Demander des nouvelles est poli mais n'annonce
  rien ; raconter sa journée ou parler d'un film détourne la lettre de son objet. »
- **Q5** consigne → « Rédige un paragraphe d'une dizaine de lignes où tu dis ce qui te plaît le plus dans le métier
  que tu as choisi et que tu exerceras plus tard. » ; étiquette d → `fr.production.hors-sujet`.
- **Q6** étiquettes : c → `fr.production.hors-sujet` ; e → `fr.argu.argument-contraire-a-la-these`.
- **Q8** consigne → « Khalid réussit son métier parce qu'il l'aime. Toi aussi, tu veux exercer un métier que tu
  aimes. Dans un texte d'une quinzaine de lignes, tu justifies ton choix. » ; dans l'explication « aide à bien y
  réussir » → « aide à bien le réussir ».
- **Q9** explication → « Un exemple est un cas concret qui illustre l'argument : le jardinier qui se lève à l'aube
  pour chaque plante montre le soin. « Un travail fait avec soin… » répète l'argument en d'autres mots ;
  « C'est pourquoi je choisirai… » est une conclusion ; « Certains pensent… » rapporte l'opinion adverse, qui
  n'illustre rien. »

---

## Étiquettes

Toutes les étiquettes employées existent sur `origin/main` ; aucune famille nouvelle n'est proposée. Libellés
vérifiés : `deduction-sans-indice`, `contraire-du-texte` et `sens-figure-lu-au-propre` nomment exactement l'erreur
exécutée partout, sauf **m005 Q6 b** (`contraire-du-texte` → `deduction-sans-indice`). Pour m006, trois
étiquettes exactes sont à ajouter sur des distracteurs muets (voir plus haut).

## Divers

- Étages : 06–10 d2 practice 75/15, 11 d3 boss 120/30 ; titres avec étoiles ; rampe croissante : OK.
- `chapter.json` `sources[]` : la ligne « Sujets officiels de l'examen national… étude 36 » est présente : OK.
- Notions : rien qui ne soit enseigné au 09 ou avant (figures et sens figuré au 07) : OK.
- Citations : toutes courtes (≤ 15 mots), littérales au signe près (vérifié par script), sauf les reformulations
  des explications corrigées ci-dessus.

## § 8 — Groupe gabarit 08/05 Q1 × 09/05 Q2 (publiés)

Vrai doublon de fait : même cadre (« Lisez ce passage… À quel type de texte appartient ce passage ? »), un fait divers
dans les deux cas, les quatre mêmes types, même clé (informatif), même étiquette
`fr.texte.informatif-pris-pour-narratif`. La notion est celle du 08. **À toucher** : réécrire 09/05 Q2 sur place
(UUID conservé) pour qu'elle teste le geste du 09 sur le même passage. Proposition vérifiée : énoncé « Lisez ce
texte : [passage inchangé] Quelle phrase résume le mieux l'information principale de ce passage ? » ; options
a `"Un camion s'est renversé à Kairouan sans faire de blessé."` (57, clé ; c fait aussi 57) ; b `"La circulation a été rétablie deux
heures plus tard."` (52, `fr.lecture.detail-pour-idee-principale`) ; c `"Le chauffeur conduisait trop vite à l'entrée
de la ville."` (57, `fr.lecture.deduction-sans-indice`) ; d `"Les pastèques de Kairouan sont transportées par
camion."` (55, `fr.lecture.deduction-sans-indice`) ; explication « L'information principale est l'accident : un
camion renversé à l'entrée de Kairouan, et un chauffeur « sorti indemne ». Le rétablissement de la circulation est
un détail ; le texte ne dit rien de la vitesse ni du transport habituel des pastèques. » Le correctif peut voyager
dans la PR du lot (même chapitre) ; sinon, en faire un ticket séparé. Ne pas toucher 08/05 Q1.

---

## Résumé

- **Questions auditées : 47** (8 + 8 + 7 + 7 + 7 + 9 ; plus 2 questions publiées pour le groupe gabarit).
- **Clés fausses : 0.**
- **Majeurs : 24**, presque tous des **fuites entre questions**. Les paires « case + justification » en deux
  questions (m003 Q1–Q2, m004 Q1–Q2 et Q3–Q4, m005 Q1–Q2 et Q3–Q4) se donnent la clé l'une l'autre : fusion en 2×2.
  À cela s'ajoutent les énoncés qui livrent une clé (m002 Q5, m003 Q4, m004 Q4, m005 Q5), les leurres qui
  reproduisent une autre clé (m005 Q7), les explications par rang (m004 Q2, m005 Q4/Q7, m006 Q9), une paraphrase
  fausse (m002 Q7), des leurres éliminés à vue (m003 Q2, Q7), une clé repérable par sa forme (m003 Q6, m004 Q3),
  un doublon de geste avec 08/01 Q3 (m006 Q3), une question à deux réponses défendables (m006 Q4) et trois défauts
  dans m001 (Q3 sentiment mal nommé, Q6 doublon de Q8, clé faible en Q8).
- **Mineurs : 9** (clés les plus courtes en m002 Q6 et m004 Q1, prémisse niée en m004 Q6, leurres faibles en m004 Q7
  et m006 Q1/Q5, consignes paraphrasées en m006, une étiquette en m005 Q6).
- **Étiquettes** : toutes au registre, une à corriger, trois à ajouter dans m006.
- **Doublons** : m006 Q3 contre 08/01 Q3 (corrigé) ; groupe gabarit 08/05 Q1 × 09/05 Q2 : vrai doublon, réécrire
  09/05 Q2.
- **Points signalés par l'auteur** : répétitions de 2026 G confirmées (« pas décidé » et « long chemin »),
  corrigées ; ajouts de 2026 G et 2025 G fidèles, sauf m002 Q7 (paraphrase fausse) et m001 Q6 (redondante) ;
  `multi` de 2025 G Q1 validé ; retouche « ne se fréquentaient pas » validée, en 2×2 ; enchaînements Q6–Q7 :
  fuites confirmées, corrigées ; 2026 T Q4 : fuite confirmée, fusion 2×2 ; m006 : thèmes variés, muets
  admis, trois étiquettes exactes à ajouter.
- Nombre de questions après correctifs : m001 7, m002 8, m003 6, m004 7, m005 6, m006 9 (toutes dans R7).
- **Verdict : à corriger avant le merge** (aucune clé fausse ; correctifs textuels, sans nouvelle recherche). Hors
  lot : vérifier l'erreur anti-verbatim de `content:qa --strict` sur `french-1ere-sec/06` avant de pousser.
