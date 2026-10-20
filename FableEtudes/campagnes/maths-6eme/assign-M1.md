# Carte d'affectation M1 — maths 6ᵉ, chapitres `06`, `07`, `13` (missions du gisement)

> Lot auteur du passage unique (PLAN-gisement.md § 4). 9 missions, 64 questions. Skills : `content-ecole-tn`, puis `prof-math-6eme` (calibre les étages, jamais plus que le programme) ; consignes `content-ingest/references/gisement-auteur-examen.md` (missions 🏛️ : la transcription de la session citée, `content/programmes-officiels/examens-nationaux/6eme-base/math/<année>-unique.md`) et `gisement-auteur-devoir.md` (missions 📝 : la carte seule, jamais le devoir). Écris en arabe (`contentLanguage` du sujet). Ne touche à aucun autre chapitre que les tiens ; les autres lots écrivent en parallèle. Nom de fichier : `exercices/<fichier>` ci-dessous.

**Règles communes** (PLAN-gisement.md § 1) : une mission d'examen reprend UN problème entier d'une session, découpé en étapes notées ; chaque question dit sa session (« مناظرة 2023 ») et redonne les données et la phrase OFFICIELLES de la transcription qu'elle lit (valeurs, unités, décimaux à trois chiffres tels qu'imprimés, tableau refait lisible) ; un « أثبتُ أنّ… » devient « quelle valeur / quelle justification » (jamais la clé dans le titre ni dans l'énoncé) ; types natifs : `numeric` pour les valeurs, QCM pour le choix d'étape, la justification et la décision, `ordering` pour un raisonnement ou les étapes d'une construction ; une CONSTRUCTION n'est pas notable : on note les longueurs du plan (échelle) et l'ordre des étapes ; figures refaites en SVG, vraies, sans donner la clé ; π = 3,14 ; aucune algèbre littérale, ni Pythagore, ni somme des angles d'un triangle, ni calcul d'intérêt, ni partage « somme et écart / somme et rapport » (◐) ; jamais de corrigé de site tiers : l'explication est la tienne, re-résolue par deux chemins ; au plus 12 questions ; étage d3 = `boss` 120/30, d2 = `practice` 75/15. Étiquettes : `misconceptionTag` du registre `math.*` sur le distracteur qui EXÉCUTE l'erreur du « piège » de la ligne, jamais sur un multi, un ordering ni un matching ; un id qui manque se signale (on ne touche ni `content/misconceptions.json` ni `content/competences/`). `chapter.json` : ajoute à `sources[]` — missions d'examen : « Sujets officiels du concours d'entrée aux collèges pilotes (6ᵉ année de base), Ministère de l'Éducation (corpus officiel, reprise citée, étude 36) — transcriptions : programmes-officiels/examens-nationaux/6eme-base/math/ » ; missions de devoir : « Calibré sur des devoirs publics (étude 36, T2′, aucune reprise) — carte : programmes-officiels/sources-externes/web-6eme-base-math/fiche.md ». Numéros de fichiers : à la suite de `05-entrainement` (06, 07, …), `displayOrder` à la suite ; les missions de chaque chapitre dans l'ordre de la carte. Gates à chaque chapitre : `content:check`, `content:qa -- --subject math-6eme` (0 erreur), `content:tranche -- --subject math-6eme --changed --fresh --strict-longest`.

**Étiquettes déjà en usage dans tes chapitres** : `06` : `math.num.ppmc-par-addition` (Tu additionnes les deux nombres au lieu de chercher leur mul); `math.num.ppmc-remplace-par-le-produit` (Tu prends le produit des deux nombres : c'est bien un multip); `math.num.divisibilite-un-seul-critere` (Tu n'appliques qu'un des deux critères : être divisible par ); `math.num.multiple-et-diviseur-confondus` (Tu confonds multiple et diviseur : le multiple contient le n); `math.num.multiple-suivant-pas-ignore` (Tu ajoutes 1 pour passer au multiple suivant : on avance du ); `math.num.multiple-precedent-au-lieu-du-suivant` (Tu donnes le multiple précédent au lieu du suivant : relis l) | `07` : `math.num.divisibilite-un-seul-critere` (Tu n'appliques qu'un des deux critères : être divisible par ); `math.num.critere-divisibilite-mal-choisi` (Tu appliques le critère d'un autre diviseur : celui de 9 ne ); `math.num.extremum-demande-ignore` (Ta réponse convient, mais ce n'est pas la plus petite (ou la); `math.num.reste-superieur-ou-egal-au-diviseur` (Tu laisses un reste plus grand que le diviseur : dans une di); `math.alg.reponse-a-l-autre-inconnue` (Tu donnes une autre grandeur que celle demandée — l'autre in) | `13` : `math.frac.multiplication-les-deux-termes-multiplies` (Tu multiplies le numérateur ET le dénominateur : la fraction); `math.num.operation-inverse-appliquee` (Tu fais l'opération contraire de celle demandée : une additi); `math.frac.multiplication-denominateur-multiplie` (Tu multiplies le dénominateur : pour multiplier une fraction); `math.frac.fraction-d-un-nombre-etape-oubliee` (Tu n'as fait qu'une moitié du calcul : prendre 3/5 d'un nomb); `math.frac.add-numerators-and-denominators` (Tu additionnes numérateurs entre eux et dénominateurs entre ); `math.frac.numerateur-denominateur-inverses` (Tu échanges le numérateur et le dénominateur : le numérateur).


## Chapitre `06-multiples-communs`

### m001 → `exercices/06-exam-2023-p1-multiples-et-recettes.json` · d3 boss 120/30 · 6 questions · régime **examen**

- Titre de travail (à écrire en arabe : « 🏛️ مناظرة 2023 · المسألة 1 ⭐⭐⭐: … ») : Concours 2023 · problème 1 · multiples communs, puis prix d'un billet ⭐⭐⭐
- Registre : id `C04#1a` ; sources `C04#1a, C04#1b`
- Source : C04 (session 2023), problème 1 — transcription `2023-unique.md`
- Phrases officielles à reprendre (questions numérotées du sujet) :
  - 1) ما هو العدد الجملي للكراسي ؟
  - 2) أحدّد بالدّينار ثمن بيع التّذكرة الواحدة من الصّنف ①.
- Étapes prévues :
  - q1 (« ما هو العدد الجملي للكراسي ؟ ») : le nombre de chaises est un multiple de 17 ET de 7, donc de 119 ; liste des multiples de 119 voisins de l'intervalle [2005 ; 2035] ; seul 2023 (119 × 17) convient — QCM du multiple commun, QCM de la liste dans l'intervalle, QCM de la conclusion « un seul nombre » — 3 q (résultat 2023).
  - q2 (tableau des deux matchs) : écart de billets du premier genre entre les deux matchs (238 − 138), écart des recettes (21 420 − 19 920), prix d'un billet du premier genre — QCM de ce que l'on compare, numérique de l'écart de recettes, numérique du prix — 3 q (résultat 15 d). Le second genre est vendu en totalité les deux fois : son nombre ne change pas, il disparaît de l'écart.
- Pièges (étiquette à porter par un distracteur) :
  - oublier la contrainte d'intervalle — ligne C04#1a (d3)
  - diviser la recette par le nombre total de billets — ligne C04#1b (d3)
- Ne pas redemander : `06/02-boss#2`, `06/02-boss#4`, `06/03-revision#3`, `06/03-revision#6`, `06/04-defi#1`, `06/04-defi#3`, `06/05-entrainement#2`, `06/05-entrainement#5`, `04/05-entrainement#7`
- Note : Deux moitiés indépendantes : la q1 n'est pas utilisée par la q2 (le nombre de chaises sert d'énoncé, pas de donnée du calcul du prix). Placement au `06` malgré la règle du chapitre le plus avancé (14) : l'étape neuve est le multiple commun dans un intervalle (E-placement). L'énoncé officiel dit « عدد محصور بين 2005 و 2035 » : l'intervalle est ouvert, 2023 est le seul multiple de 119 qui y tombe (1904 et 2142 sortent).

### m002 → `exercices/07-exam-2020-p2-jouets-restes-egaux.json` · d3 boss 120/30 · 8 questions · régime **examen**

- Titre de travail (à écrire en arabe : « 🏛️ مناظرة 2020 · المسألة 2 ⭐⭐⭐: … ») : Concours 2020 · problème 2 · fraction et écart, puis restes égaux ⭐⭐⭐
- Registre : id `C07#2a` ; sources `C07#2a, C07#2b`
- Source : C07 (session 2020), problème 2 — transcription `2020-unique.md`
- Phrases officielles à reprendre (questions numérotées du sujet) :
  - 1. ما هو عدد اللّعب من الصّنف الأوّل ؟
  - 2. ما هو عدد اللّعب من الصّنف الثّالث ؟
- Étapes prévues :
  - q1 (« ما هو عدد اللعب من الصنف الأوّل ؟ ») : premier genre = 3/5 du second ; l'écart 1920 vaut donc 2/5 du second ; 1/5 = 960 ; second 4800 ; premier 2880 — 4 q (résultat 2880 ; le second genre 4800 sert à la q2).
  - q2 (« ما هو عدد اللعب من الصنف الثّالث ؟ ») : le total N est compris entre 9600 et 9700 et laisse le reste 4 dans les divisions par 11, 19 et 23 ; N − 4 est un multiple commun de 11, 19, 23 (produit 4807, ces trois nombres sont premiers entre eux) ; 4807 × 2 = 9614 donc N = 9618 ; troisième genre = 9618 − 2880 − 4800 = 1938 — 4 q (QCM de ce qui est multiple, numérique du multiple commun, du total, du troisième genre).
- Pièges (étiquette à porter par un distracteur) :
  - prendre l'écart pour le plus petit des effectifs — ligne C07#2a (d3)
  - oublier d'ajouter le reste au multiple commun — ligne C07#2b (d4)
- Ne pas redemander : `06/05-entrainement#5`, `06/04-defi#2`, `06/05-entrainement#2`, `06/02-boss#6`, `08/02-boss#5`, `08/04-defi#2`, `13/04-defi#4`
- Note : Piège de la q2 : oublier d'ajouter le reste (le multiple commun lui-même vaut 9614, qui est aussi dans l'intervalle). Le reste 4 est le même pour les trois diviseurs : c'est ce qui permet de passer par le multiple commun. Placement au `06` (étape neuve = restes égaux dans un intervalle), pas au `13` malgré la fraction de la q1.

### m003 → `exercices/08-exam-2018-p1-costumes-restes-et-benefice.json` · d3 boss 120/30 · 8 questions · régime **examen**

- Titre de travail (à écrire en arabe : « 🏛️ مناظرة 2018 · المسألة 1 ⭐⭐⭐: … ») : Concours 2018 · problème 1 · restes égaux, bénéfice fractionnaire, pourcentage du coût ⭐⭐⭐
- Registre : id `C09#1a` ; sources `C09#1a, C09#1b`
- Source : C09 (session 2018), problème 1 — transcription `2018-unique.md`
- Phrases officielles à reprendre (questions numérotées du sujet) :
  - 1. أُحسب عدد البدلات الرّياضيّة المنتجة في اليوم.
  - 2. إبحث عن ثمن شراء القماش.
- Étapes prévues :
  - q1 (nombre de survêtements par jour) : N compris entre 602 et 608, reste 7 dans la division par 23 ET par 13 ; N − 7 est un multiple commun de 23 et 13 (299, premiers entre eux) ; 598 est le seul multiple de 299 près de l'intervalle, donc N = 605 — 3 q.
  - q2 (prix d'achat du tissu) : vente 77 440 d avec un bénéfice égal aux 4/7 du coût ; la vente vaut donc 11/7 du coût ; coût = 77 440 × 7/11 = 49 280 d ; le tissu coûte 41 % du coût de production = 20 204,8 d — 5 q (écriture « vente = coût + 4/7 du coût », coût, 1 % ou 41/100, tissu).
- Pièges (étiquette à porter par un distracteur) :
  - chercher un multiple commun sans ajouter le reste — ligne C09#1a (d3)
  - appliquer la fraction du bénéfice au prix de vente — ligne C09#1b (d4)
- Ne pas redemander : `06/05-entrainement#5`, `06/04-defi#3`, `06/03-revision#6`, `14/02-boss#8`, `14/04-defi#11`, `14/05-entrainement#10`, `08/04-defi#2`
- Note : La q1 reprend la structure de la mission du concours 2020 (restes égaux) : l'auteur du lot garde deux angles différents (là, le reste commun à TROIS diviseurs ; ici, à deux, suivi d'un bénéfice fractionnaire). Piège de la q2 : appliquer la fraction du bénéfice au prix de vente au lieu du coût. Les 41 % portent sur le coût de production, pas sur la vente.

### m004 → `exercices/09-devoir-multiples-communs-intervalle.json` · d3 boss 120/30 · 8 questions · régime **devoir (salle blanche)**

- Titre de travail (arabe : « ⭐ تمرين موجّه / ⚔️ زعيم الفرض ⭐⭐⭐: … ») : Multiple commun dans un intervalle : trouver, encadrer, prouver l'unicité ⭐⭐⭐
- Registre : id `D02#1` ; sources `D02#1, D02#7, D03#1, D05#1a, D05#1b, D04#6a, D01#11a, D01#11b, D08#8e`
- Cartes : devoir A (T1, école primaire), exercice(s) 11a, 11b ; devoir B (T1, école primaire), exercice(s) 1, 7 ; devoir C (T1, école primaire), exercice(s) 1 ; devoir D (T2, école primaire), exercice(s) 6a ; devoir E (T2, école primaire), exercice(s) 1a, 1b ; devoir G (T3, école primaire), exercice(s) 8e — cartes anonymes
- Gestes lus (archétype des lecteurs, sans nombre) :
  - D02#1 (d3) : établir qu’une masse est l’unique multiple commun dans un intervalle
  - D02#7 (d3) : trouver le plus petit multiple commun puis établir une masse dans un intervalle
  - D03#1 (d3) : établir qu’une masse est le multiple commun situé dans un intervalle donné
  - D05#1a (d2) : trouver un nombre sous une borne multiple commun de trois nombres
  - D05#1b (d2) : encadrer un nombre entre deux multiples communs consécutifs
  - D04#6a (d3) : trouver un nombre dans un intervalle divisible par trois diviseurs simultanément
  - D01#11a (d1) : donner le plus petit multiple commun de deux nombres premiers entre eux
  - D01#11b (d2) : trouver un nombre sous une borne de même reste dans deux divisions
  - D08#8e (d2) : trouver un nombre de même reste dans deux divisions
- Étapes prévues :
  - Un plus petit multiple commun de deux nombres premiers entre eux (donné par le produit) puis d'un troisième nombre : trouver le multiple commun de trois nombres sous une borne (le plus grand possible), puis l'encadrer entre deux multiples communs consécutifs — QCM, numérique — 3 q.
  - « Montrer qu'un nombre est le seul multiple commun dans un intervalle » : lister les multiples communs voisins (celui d'avant et celui d'après sortent de l'intervalle) puis conclure à l'unicité — QCM de la justification, ordering des trois temps (multiple commun, liste, conclusion) — 3 q.
  - Un nombre qui laisse le même reste dans deux divisions et qui est compris sous une borne : on cherche un multiple commun puis on lui ajoute le reste — QCM, numérique — 2 q. Un des trois nombres est un multiple d'un autre dans l'une des questions (le plus petit multiple commun est alors le plus grand des deux).
- Pièges (étiquette à porter par un distracteur) :
  - ne pas vérifier l’unicité dans l’intervalle — ligne D02#1 (d3)
  - ne pas vérifier l’unicité dans l’intervalle — ligne D02#7 (d3)
  - ne pas vérifier l’unicité dans l’intervalle — ligne D03#1 (d3)
  - ne pas retenir le plus grand multiple possible — ligne D05#1a (d2)
  - prendre des multiples non communs — ligne D05#1b (d2)
  - ne tester que deux critères sur trois — ligne D04#6a (d3)
  - ignorer la condition sur le reste — ligne D01#11b (d2)
  - oublier le reste — ligne D08#8e (d2)
- Ne pas redemander : `06/01-pratique#5`, `06/01-pratique#6`, `06/02-boss#2`, `06/02-boss#3`, `06/03-revision#3`, `06/04-defi#1`, `06/04-defi#2`, `06/05-entrainement#2`, `06/05-entrainement#3`, `06/05-entrainement#5`
- Note : Salle blanche. Gestes absents des missions d'examen : multiple commun de TROIS nombres sous une borne, encadrement entre deux multiples communs consécutifs, preuve d'unicité dans un intervalle. Les deux versions d'un même devoir (A et B) ne comptent qu'une fois. Les lignes D01#1 et D01#2 (écart entre deux effectifs, `HP:somme-difference`) ne sont pas reprises.


## Chapitre `07-criteres-divisibilite`

### m005 → `exercices/06-devoir-chiffres-manquants-plusieurs-criteres.json` · d2 practice 75/15 · 6 questions · régime **devoir (salle blanche)**

- Titre de travail (arabe : « ⭐ تمرين موجّه / ⚔️ زعيم الفرض ⭐⭐: … ») : Compléter les chiffres manquants pour deux, trois ou quatre critères à la fois ⭐⭐
- Registre : id `D08#8a` ; sources `D08#8a, D08#8b, D08#8d`
- Cartes : devoir G (T3, école primaire), exercice(s) 8a, 8b, 8d — cartes anonymes
- Gestes lus (archétype des lecteurs, sans nombre) :
  - D08#8a (d1) : compléter un nombre pour qu’il soit divisible par deux critères
  - D08#8b (d2) : compléter les chiffres manquants pour une divisibilité par trois et par neuf
  - D08#8d (d2) : compléter deux chiffres manquants pour une divisibilité par quatre critères
- Étapes prévues :
  - Un nombre dont un chiffre manque : le compléter pour qu'il soit divisible par deux critères à la fois (2 et 5, 5 et 3) — QCM, multi (« tous les chiffres possibles ») — 2 q.
  - Un nombre dont un chiffre manque : divisibilité par 3 puis par 9 (le même chiffre convient-il aux deux ?) — QCM, numérique — 2 q.
  - Un nombre à DEUX chiffres manquants : divisibilité simultanée par quatre critères (2, 3, 5, 9) ; commencer par le chiffre des unités (0), puis le chiffre des dizaines (somme à compléter) — ordering des étapes, numérique du plus petit nombre possible — 2 q.
- Pièges (étiquette à porter par un distracteur) :
  - ne tester que la divisibilité par trois — ligne D08#8b (d2)
  - oublier un des critères — ligne D08#8d (d2)
- Ne pas redemander : `07/01-pratique#8`, `07/02-boss#6`, `07/02-boss#7`, `07/04-defi#2`, `07/04-defi#5`, `07/04-defi#6`, `07/05-entrainement#5`, `07/05-entrainement#9`, `07/05-entrainement#10`
- Note : Salle blanche. Le patron du `07` demande souvent UN chiffre manquant pour UN critère ; le geste neuf est DEUX chiffres manquants et les critères cumulés (2, 3, 5, 9). Le critère de 4 (deux derniers chiffres) n'est pas au programme : ne pas l'utiliser. La ligne D09#1 (feuille de calcul mental, pas de mission) n'est pas reprise.


## Chapitre `13-multiplication-fraction-entier`

### m006 → `exercices/06-exam-2025-p1-bouquets-trois-clients.json` · d3 boss 120/30 · 8 questions · régime **examen**

- Titre de travail (à écrire en arabe : « 🏛️ مناظرة 2025 · المسألة 1 ⭐⭐⭐: … ») : Concours 2025 · problème 1 · trois sommes et une fraction du total ⭐⭐⭐
- Registre : id `C02#1a` ; sources `C02#1a, C02#1b`
- Source : C02 (session 2025), problème 1 — transcription `2025-unique.md`
- Phrases officielles à reprendre (questions numérotées du sujet) :
  - 1) أثبتُ أنّ المبلغ الّذي دفعه الحريف الثّاني يساوي 72 د.
  - 2) أحسبُ بالدّينار ثمن بيع الزّهرة البيضاء الواحدة.
- Étapes prévues :
  - q1 (« أثبتُ أنّ المبلغ الّذي دفعه الحريف الثّاني يساوي 72 د ») : les deux autres clients paient 60 + 84 = 144 d, soit 2/3 du total ; 1/3 du total = 72 d (donc total 216 d) — QCM de la fraction du total que représentent les deux autres, numérique du total, numérique du client 2 — 3 q.
  - q2 (prix d'une fleur blanche, 12 fleurs par bouquet) : chaque couleur est comptée deux fois dans les trois sommes ; 216 ÷ 2 = 108 d pour un bouquet de chaque couleur ; jaune = 108 − 60 = 48, rouge = 108 − 72 = 36, blanc = 108 − 84 = 24 ; une fleur blanche = 24 ÷ 12 = 2 d — QCM de ce que vaut la somme des trois bouquets, numériques des trois prix, numérique de la fleur — 5 q.
- Pièges (étiquette à porter par un distracteur) :
  - appliquer la fraction aux seules autres parts — ligne C02#1a (d3)
  - chercher le prix d'un seul type sans exploiter les trois sommes — ligne C02#1b (d4)
- Ne pas redemander : `13/02-boss#9`, `13/04-defi#7`, `13/04-defi#8`, `08/02-boss#5`, `08/04-defi#2`, `12/04-defi#8`, `04/05-entrainement#7`
- Note : Le tableau est refait en SVG ou en tableau lisible, les trois sommes sont données (60 d, 1/3 du total, 84 d). Aucune lettre, aucun calcul littéral : raisonnement par addition des trois sommes. Piège de la q1 : appliquer 1/3 aux deux autres clients (24 d) au lieu de la fraction 2/3. `04/05-entrainement#7` pose déjà les sommes deux à deux (masses) : la nouveauté est la fraction du total qui donne la troisième somme.

### m007 → `exercices/07-exam-2016-p1-cadeau-fraction-et-remise.json` · d3 boss 120/30 · 7 questions · régime **examen**

- Titre de travail (à écrire en arabe : « 🏛️ مناظرة 2016 · المسألة 1 ⭐⭐⭐: … ») : Concours 2016 · problème 1 · retrouver le prix, puis le taux de remise ⭐⭐⭐
- Registre : id `C11#1a` ; sources `C11#1a, C11#1b`
- Source : C11 (session 2016), problème 1 — transcription `2016-unique.md`
- Phrases officielles à reprendre (questions numérotées du sujet) :
  - 1. ما ثمن الهديّة ؟
  - 2. أُحدِّدُ النّسبة المائويّة للتّخفيض بالنّسبة إلى الثّمن الأصلي للهديّة.
- Étapes prévues :
  - q1 (« ما ثمن الهديّة ؟ ») : le premier frère donne 18,600 d ; le second donne les 2/5 du prix ; ensemble 45,800 d ; donc 2/5 du prix = 27,200 d ; 1/5 = 13,600 d ; prix = 68 d — QCM de ce que vaut 2/5, numérique du 1/5, numérique du prix — 3 q.
  - q2 (taux de remise) : le père ajoute 12 d pour compléter ; prix payé = 45,800 + 12 = 57,800 d ; remise = 68 − 57,800 = 10,200 d ; taux = 10,2 ÷ 68 = 15 % (rapporté au prix d'origine) — QCM du prix payé, numérique de la remise, numérique du taux — 4 q.
- Pièges (étiquette à porter par un distracteur) :
  - calculer la part fractionnaire au lieu de retrouver le tout — ligne C11#1a (d3)
  - rapporter la remise au prix payé plutôt qu'au prix initial — ligne C11#1b (d3)
- Ne pas redemander : `13/02-boss#9`, `11/05-entrainement#7`, `14/02-boss#8`, `14/04-defi#11`, `08/04-defi#2`, `04/03-revision#6`
- Note : Placement au `13` (étape neuve = retrouver le tout depuis une fraction à deux contributeurs), le taux de remise de la q2 est de niveau `14` mais déjà au patron. Piège de la q2 : rapporter la remise au prix payé (57,8) au lieu du prix d'origine. Les décimaux à trois chiffres (18,600) sont gardés tels qu'imprimés.

### m008 → `exercices/08-exam-2015-p1-robe-deux-options.json` · d3 boss 120/30 · 6 questions · régime **examen**

- Titre de travail (à écrire en arabe : « 🏛️ مناظرة 2015 · المسألة 1 ⭐⭐⭐: … ») : Concours 2015 · problème 1 · deux façons d'obtenir une robe ⭐⭐⭐
- Registre : id `C12#1a` ; sources `C12#1a, C12#1b`
- Source : C12 (session 2015), problème 1 — transcription `2015-unique.md`
- Phrases officielles à reprendre (questions numérotées du sujet) :
  - 1- أحسُبُ كلفة الفستان حسب الخيار الأوّل.
  - 2- أيّ الخيارين أقلّ كلفة ؟
- Étapes prévues :
  - q1 (« أحسُبُ كلفة الفستان حسب الخيار الأوّل ») : tissu 2,5 m × 18,400 d = 46 d ; façon = 5/2 du prix du tissu (fraction supérieure à 1) = 115 d ; coût = 161 d — QCM de la lecture « 5/2 du prix » (plus grand que le tissu), numériques tissu, façon, total — 4 q.
  - q2 (« أيّ الخيارين أقلّ كلفة ؟ ») : remise de 15 % sur 162,500 d = 24,375 d ; prix 138,125 d ; comparaison avec 161 d : le second choix est le moins cher — numérique de la remise, du prix, QCM de la comparaison — 2 q.
- Pièges (étiquette à porter par un distracteur) :
  - lire la fraction supérieure à un comme inférieure au coût de départ — ligne C12#1a (d3)
  - retirer la remise de la mauvaise base avant de comparer — ligne C12#1b (d2)
- Ne pas redemander : `13/05-entrainement#6`, `13/05-entrainement#10`, `13/03-revision#10`, `14/04-defi#2`, `14/04-defi#3`, `14/03-revision#9`, `05/05-entrainement#6`, `05/05-entrainement#7`
- Note : Exception de placement déclarée : le chapitre le plus avancé de la lecture serait `14` (remise de 15 %), déjà bien servi au patron ; l'étape neuve est la fraction supérieure à 1 d'une quantité (5/2 du prix), au `13`. Piège de la q1 : lire 5/2 comme moins que le tissu. Piège de la q2 : retirer la remise de la mauvaise base. Décimaux à trois chiffres gardés (18,400 ; 162,500).

### m009 → `exercices/09-exam-2009-p1-chauffe-eau-installation-economie.json` · d3 boss 120/30 · 7 questions · régime **examen**

- Titre de travail (à écrire en arabe : « 🏛️ مناظرة 2009 · المسألة 1 ⭐⭐⭐: … ») : Concours 2009 · problème 1 · le prix retrouvé par une petite fraction, puis l'économie en pourcentage ⭐⭐⭐
- Registre : id `C18#1a` ; sources `C18#1a, C18#1b`
- Source : C18 (session 2009), problème 1 — transcription `2009-unique.md`
- Phrases officielles à reprendre (questions numérotées du sujet) :
  - ① ابحث عن الكلفة الجمليّة لشراء وتركيب السخّان.
  - ② حدّد النّسبة المائويّة للمبلغ المقتصد بالنسبة إلى قيمة الاستهلاك السّابق.
- Étapes prévues :
  - q1 (coût total d'achat et de pose) : la pose coûte 240 d, soit 2/13 du prix du chauffe-eau ; 1/13 = 120 d ; prix = 1560 d ; coût total = 1560 + 240 = 1800 d — QCM, numériques — 4 q.
  - q2 (taux d'économie sur la facture bimestrielle) : avant 116 d, après 78,880 d ; économie = 37,120 d ; part de l'ancienne facture = 37,12 ÷ 116 = 32 % — numérique de l'économie, QCM de la base du pourcentage (l'ancienne facture), numérique du taux — 3 q.
- Pièges (étiquette à porter par un distracteur) :
  - calculer la fraction du coût au lieu de retrouver le prix — ligne C18#1a (d2)
  - rapporter l'économie à la nouvelle dépense — ligne C18#1b (d3)
- Ne pas redemander : `13/02-boss#9`, `14/03-revision#6`, `14/05-entrainement#9`, `14/quiz#7`, `04/05-entrainement#5`, `08/02-boss#5`
- Note : Piège de la q1 : calculer 2/13 de 240. Piège de la q2 : rapporter l'économie à la nouvelle facture. Le prix du chauffe-eau (1560) n'est pas nécessaire pour la q2 : l'énoncé les enchaîne sans les lier, l'auteur garde les deux questions indépendantes.

