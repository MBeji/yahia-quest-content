# Carte d'affectation M3 — français 6ᵉ, chapitres 05, 06 (missions du gisement)

> Lot auteur du passage unique (PLAN.md ; PLAN-gisement.md § 4). 10 missions. Skills : `content-ecole-tn`, puis `content-langue-francais` pour le registre de langue, `prof-francais-college` pour calibrer les étages `d3` seulement (sans en reprendre le programme de 7ᵉ–8ᵉ) ; consignes `content-ingest/references/gisement-auteur-examen.md` (missions d'examen, avec la transcription de chaque session citée : `content/programmes-officiels/examens-nationaux/6eme-base/french/<année>-unique.md`) et `gisement-auteur-devoir.md` (missions 📝 : la carte seule, jamais le devoir). Ne touche à aucun autre chapitre que les tiens ; les autres lots écrivent en parallèle. **Deux auteurs en parallèle** (un par chapitre : 05 / 06), chapitres disjoints.

**Règles communes** (PLAN-gisement.md § 1) : chaque question dit sa session (« Concours 2023 ») et redonne la phrase OFFICIELLE de la transcription (consigne et énoncé tels qu'imprimés, coquilles incluses) ; une réécriture « Réécris … » devient « quelle réécriture est correcte ? » (QCM de formes) ou un matching/ordering ; un blanc `HP:` est DONNÉ rempli, jamais demandé ; une forme d'un verbe d'un chapitre ultérieur est donnée dans les options quand elle n'est pas la cible ; jamais de corrigé de site tiers : l'explication est la tienne, re-résolue. Étiquettes : vocabulaire `fr.*` du lot A (`vocab-french-6eme.json`), sur les distracteurs qui disent l'erreur du « piège » de la ligne, jamais sur multi/ordering/matching ; les ids neufs ou élargis que tu poses vont dans `content/misconceptions.json`. `chapter.json` : ajoute à `sources[]` la ligne « Sujets officiels du concours d'entrée aux collèges pilotes (6ᵉ année de base), Ministère de l'Éducation (corpus officiel, reprise citée, étude 36) — transcriptions : programmes-officiels/examens-nationaux/6eme-base/french/ » (missions d'examen).

**Ordre de travail** : (1) les ids d'étiquette neufs que tu poses ; (2) les missions, dans l'ordre de la carte ; (3) gates à chaque chapitre : `content:check`, `content:qa -- --subject french-6eme` (0 erreur), `content:tranche -- --subject french-6eme --changed --fresh --strict-longest`. Numéros de fichiers : à la suite de `05-entrainement` (06, 07, …) ; `displayOrder` à la suite.


## Chapitre `05-sauver-la-nature`

### Missions (gisement)

#### m015 → `exercices/06-exams-2008-2026-complements-essentiels-ou-non.json` · d2 practice 75/15 · 8 questions · régime **examen**

- Titre : « 🏛️ Concours 2008–2026 · supprimer, relever : complément essentiel ou non essentiel ⭐⭐ »
- Registre : id `C01#6` ; sources `C01#6, C03#5, C15#5, C17#4, C19#4`
- Sources (base en premier) : C01 (2026) ex. 6 ; C03 (2024) ex. 5 ; C15 (2012) ex. 5 ; C17 (2010) ex. 4 ; C19 (2008) ex. 4
- Items :
  - 2026 gram. 1 : « On se regarde en souriant. Mme Guégan a souvent des idées bizarres. » et « Pablo nous rejoint là-bas. » — « supprime les compléments non essentiels » : deux QCM de la réécriture correcte (leurre : supprimer un complément essentiel) — 2 q.
    - piège (étiquette à porter par un distracteur) : supprimer aussi un complément essentiel — ligne C01#6 (d2)
  - 2024 gram. 1 : « Sans prévenir, le phoque a plongé dans l'eau sombre des profondeurs. » — QCM « quel groupe est non essentiel » (la consigne est ambiguë sur « dans l'eau … » : ne demander que « Sans prévenir ») — 1 q.
    - piège (étiquette à porter par un distracteur) : supprimer un complément essentiel — ligne C03#5 (d2)
  - 2012 gram. 1 : « Rami regarde les enfants sans dire un seul mot. » — « relève un complément essentiel, un complément non essentiel » : matching — 1 q.
    - piège (étiquette à porter par un distracteur) : confondre les deux types de complément — ligne C15#5 (d2)
  - 2010 gram. 1 : « Au milieu du silence général, Benjamin tire la couverture. » — matching essentiel / non essentiel ; QCM « la phrase sans son complément non essentiel » — 2 q.
    - piège (étiquette à porter par un distracteur) : confondre les deux types de complément — ligne C17#4 (d2)
  - 2008 gram. 1 : « A la récréation, Nicolas et ses copains feront des tas de photos. » — QCM « quel est le groupe verbal », QCM « quel est le complément non essentiel » — 2 q.
    - piège (étiquette à porter par un distracteur) : confondre complément non essentiel et essentiel — ligne C19#4 (d2)
- Ne pas redemander : `05/quiz#1`, `05/01-pratique#1`, `05/02-boss#1`, `05/02-boss#6`, `05/03-revision#1`
- Note : Famille « complément essentiel / non essentiel » du `05`. Les compléments de lieu, de temps, de manière sont nommés dans la mission de tableau du `08` (cumul). Le gérondif « en souriant » (2026) est un complément non essentiel qu'on ne NOMME pas (F1).

#### m016 → `exercices/07-exams-2008-2023-prendre-et-mettre.json` · d2 practice 75/15 · 8 questions · régime **examen**

- Titre : « 🏛️ Concours 2008–2023 · prendre, mettre et leurs dérivés : présent, passé composé, futur ⭐⭐ »
- Registre : id `C04#9` ; sources `C04#9, C06#9, C07#11, C17#7, C19#7`
- Sources (base en premier) : C04 (2023) ex. 9 ; C06 (2021) ex. 9 ; C07 (2020) ex. 11 ; C17 (2010) ex. 7 ; C19 (2008) ex. 7
- Items :
  - 2023 conj. 2 : « Claudine a mis du temps pour se rétablir ; enfin elle a repris la marche. » au présent — QCM « met … reprend » (le d de « reprend ») — 2 q.
    - piège (étiquette à porter par un distracteur) : mal conjuguer le verbe dérivé au présent — ligne C04#9 (d2)
  - 2021 conj. 1 : « Ce matin, j'ai pris mon courage à deux mains et j'ai abordé le chat. » à commencer par « Demain matin, je … » — QCM « prendrai … aborderai » — 2 q.
    - piège (étiquette à porter par un distracteur) : conserver le passé composé — ligne C06#9 (d2)
  - 2020 conj. 3 : « … ils le déplacent, le rafraîchissent et lui mettent des engrais » au passé composé — QCM « ont mis » (le participe irrégulier) ; la partie « ils l'ont déplacé, rafraîchi » est donnée — 2 q.
    - piège (étiquette à porter par un distracteur) : mal former le participe passé irrégulier — ligne C07#11 (d3)
  - 2010 conj. 1 : « Benjamin prend le colis et l'installe au fond du jardin. » au passé composé — QCM « a pris » — 1 q.
    - piège (étiquette à porter par un distracteur) : mal former le participe de prendre — ligne C17#7 (d2)
  - 2008 conj. 1 : « La maîtresse prend le portable et le garde chez elle. » au passé composé — QCM « a pris » (leurre : « a prendu ») — 1 q.
    - piège (étiquette à porter par un distracteur) : mal former le participe de prendre — ligne C19#7 (d2)
- Ne pas redemander : `05/quiz#2`, `05/quiz#3`, `05/01-pratique#2`, `05/01-pratique#5`, `05/01-pratique#6`, `05/02-boss#2`, `05/03-revision#2`, `05/05-entrainement#5`
- Note : Famille « prendre / mettre » du `05`. F5 : le participe passé avec « avoir » ne s'accorde jamais ici (aucune phrase où le complément précède). C18#8 (impératif de prendre) est au `02`, C19#8 (futur de prendre et d'aller) au `06`.

#### m017 → `exercices/08-exams-2012-2025-accord-du-verbe-avec-son-sujet.json` · d2 practice 75/15 · 9 questions · régime **examen**

- Titre : « 🏛️ Concours 2012–2025 · changer de sujet : l'accord du verbe ⭐⭐ »
- Registre : id `C02#8` ; sources `C02#8, C05#9, C12#7, C14#7, C15#9`
- Sources (base en premier) : C02 (2025) ex. 8 ; C05 (2022) ex. 9 ; C12 (2015) ex. 7 ; C14 (2013) ex. 7 ; C15 (2012) ex. 9
- Items :
  - 2025 conj. 1 : « Xavier et ses compagnons prennent une navette et vont à Tikal. » devient « Mes compagnons et moi … une navette et … à Tikal. » — QCM « prenons », QCM « allons » — 2 q.
    - piège (étiquette à porter par un distracteur) : employer la terminaison de la troisième personne — ligne C02#8 (d2)
  - 2022 conj. 1 : « La professeure annonce : « Je veux créer un club de théâtre. » » devient « Les professeurs … : « Nous … créer un club de théâtre. » » — QCM « annoncent » (« voulons » est donné) — 1 q.
    - piège (étiquette à porter par un distracteur) : garder la terminaison du singulier — ligne C05#9 (d2)
  - 2015 conj. 1 : « François s'approche et jette un coup d'œil par la fenêtre. » en remplaçant « François » par « nous » — QCM « nous nous approchons », QCM « nous jetons » — 2 q.
    - piège (étiquette à porter par un distracteur) : garder la forme de la troisième personne — ligne C12#7 (d2)
  - 2013 conj. 1 : « Quand ils rentrent de l'école, les enfants se dépêchent de faire leurs devoirs. » en remplaçant « les enfants » par « nous » — QCM « nous rentrons », QCM « nous nous dépêchons » (« nos devoirs » est donné) — 2 q.
    - piège (étiquette à porter par un distracteur) : garder la forme de la troisième personne — ligne C14#7 (d2)
  - 2012 conj. 2 : « Rami fixe ses amis d'un œil sévère et se met à leur parler. » en remplaçant « Rami » par « vous » — QCM « vous fixez … vos amis », QCM « vous vous mettez » — 2 q.
    - piège (étiquette à porter par un distracteur) : garder la forme de la troisième personne — ligne C15#9 (d2)
- Ne pas redemander : `05/quiz#4`, `05/01-pratique#3`, `05/02-boss#3`, `05/02-boss#4`, `05/02-boss#5`, `05/03-revision#3`, `05/03-revision#5`, `05/03-revision#6`
- Note : Famille la plus fréquente de la langue d'examen (« réécris en remplaçant X par Y »). Les verbes pronominaux (s'approcher, se dépêcher, se mettre) ne sont pas nommés au cours : ils servent à l'accord, le pronom réfléchi est visible dans les options. Aller (`06`) et vouloir (`08`) : formes données quand elles ne sont pas la cible.

#### m018 → `exercices/09-exam-2024-lecture-une-fin-tragique.json` · d2 practice 75/15 · 9 questions · régime **examen**

- Titre : « 🏛️ Concours 2024 · lecture : une fin tragique ⭐⭐ »
- Registre : id `C03#1` ; sources `C03#1, C03#2, C03#3, C03#4`
- Sources (base en premier) : C03 (2024) ex. 1 ; C03 (2024) ex. 2 ; C03 (2024) ex. 3 ; C03 (2024) ex. 4
- Items :
  - Q1 : « Malgré les différences, une amitié solide s'est nouée entre Virginia et le narrateur. Cite deux de ces différences. » (milieu, religion) — multi « coche les deux différences » — 1 q.
    - piège (étiquette à porter par un distracteur) : citer des ressemblances ou des faits sans lien — ligne C03#1 (d1)
  - Q2 : « Quels sentiments éprouvent les deux enfants lors de la rencontre avec le phoque ? Justifie à chaque fois ta réponse par un indice du texte. » (la peur, puis la fascination) — QCM du sentiment 1, QCM de son indice, QCM du sentiment 2, QCM de son indice — 4 q.
    - piège (étiquette à porter par un distracteur) : donner un indice qui ne correspond pas au sentiment — ligne C03#2 (d2)
  - Q3 a : synonymes de « Le cri __strident__ … a dû __effrayer__ le phoque » ; Q3 b : contraires de « la piste __tortueuse__ qui __grimpe__ jusqu'à l'école » — un QCM par mot (le leurre est un mot de nature différente) — 3 q parmi les quatre mots (au choix de l'auteur, les deux contraires obligatoires).
    - piège (étiquette à porter par un distracteur) : choisir un mot de nature ou de sens inadaptés — ligne C03#3 (d2)
  - Q4 : « De même que les phoques, plusieurs espèces animales sont menacées de disparition. A ton avis, quelles sont les causes de cette disparition ? » — multi « quelles causes » (filets, pollution, chasse ; leurre : des conséquences) — 1 q.
    - piège (étiquette à porter par un distracteur) : citer des conséquences au lieu de causes — ligne C03#4 (d2)
- Ne pas redemander : `05/04-defi#1`, `05/04-defi#2`, `05/04-defi#3`, `05/04-defi#6`
- Note : Compréhension d'un texte récent (R2). Texte intégral : PDF officiel `/tmp/claude-0/fr6g/src/2024-francais.pdf` (sha256 au registre) ; citation utile : « Triste journée pour moi et pour Virginia ! » Sujet sensible (un petit phoque mort) : l'auteur garde le ton du texte, aucun détail cru ajouté. Les extraits du `05` défi (#1 à #3, #6) lisent un mini-récit de l'auteur : autre geste.

#### m019 → `exercices/10-exams-2012-2024-recit-emotions-et-description.json` · d3 boss 120/30 · 8 questions · régime **examen**

- Titre : « 🏛️ Concours 2012–2024 · préparer un récit : décrire les émotions et le lieu ⭐⭐⭐ »
- Registre : id `C03#11` ; sources `C03#11, C09#12, C15#11`
- Sources (base en premier) : C03 (2024) ex. 11 ; C09 (2018) ex. 12 ; C15 (2012) ex. 11
- Items :
  - 2024 : « A l'école, les deux enfants racontent à leurs camarades la scène tragique du phoque et de son petit trouvés morts sur la plage… Raconte en huit phrases au moins l'histoire en décrivant les émotions des deux enfants. Intègre dans ton récit un court dialogue. » — multi « quelles phrases décrivent une émotion » ; QCM « quelle phrase montre la tristesse par un geste plutôt que par le mot » ; ordering — 3 q.
    - piège (étiquette à porter par un distracteur) : omettre les émotions ou le dialogue — ligne C03#11 (d3)
  - 2018 : « Comme ces arbres, tes camarades et toi, vous décidez d'organiser une action contre la pollution de votre environnement. Raconte, en huit phrases au moins, ce que vous avez fait en intégrant un dialogue et une description dans ton récit. » — QCM « quel passage décrit le lieu pollué (et non l'action) » ; ordering des quatre moments (début, description, dialogue, fin) — 3 q.
    - piège (étiquette à porter par un distracteur) : oublier le dialogue ou la description — ligne C09#12 (d3)
  - 2012 : « Emir est maintenant l'ami des oiseaux. Un jour, son petit frère Amine rentre à la maison avec un oiseau enfermé dans une cage. Emir demande à son frère de le libérer. Rédige un récit pour raconter ce qui s'est passé. Intègre un court dialogue… (au moins huit phrases) » — QCM « quel portrait de l'oiseau captif convient » ; QCM de la réplique d'Emir qui convainc — 2 q.
    - piège (étiquette à porter par un distracteur) : oublier le dialogue ou la progression du récit — ligne C15#11 (d3)
- Ne pas redemander : `05/quiz#5`, `05/01-pratique#4`, `05/04-defi#4`, `05/04-defi#5`, `05/05-entrainement#6`
- Note : Archétype « raconter avec un passage descriptif (émotions, lieu, animal) ». Le patron prépare le passage descriptif par phrase isolée : ici c'est la consigne officielle complète, avec dialogue.


## Chapitre `06-etre-en-forme`

### Missions (gisement)

#### m020 → `exercices/06-exams-2008-2026-aller-et-faire.json` · d2 practice 75/15 · 11 questions · régime **examen**

- Titre : « 🏛️ Concours 2008–2026 · aller et faire : présent, passé composé, futur ⭐⭐ »
- Registre : id `C01#9` ; sources `C01#9, C09#9, C12#9, C14#8, C14#9, C17#9, C18#9, C19#8`
- Sources (base en premier) : C01 (2026) ex. 9 ; C09 (2018) ex. 9 ; C12 (2015) ex. 9 ; C14 (2013) ex. 8 ; C14 (2013) ex. 9 ; C17 (2010) ex. 9 ; C18 (2009) ex. 9 ; C19 (2008) ex. 8
- Items :
  - 2026 conj. 1 : « J'éclate de rire. Gordon m'imite. Ensuite, dans les rangs, ça fait comme une vague. » au passé composé — QCM « a fait » (les deux autres verbes sont donnés) — 1 q.
    - piège (étiquette à porter par un distracteur) : oublier l'auxiliaire ou mal former le participe — ligne C01#9 (d2)
  - 2018 conj. 1 : « Le désert a fait fuir les hommes jusqu'au jour où les arbres ont envahi l'endroit. » au futur — QCM « fera … envahiront » — 1 q.
    - piège (étiquette à porter par un distracteur) : laisser le passé composé — ligne C09#9 (d2)
  - 2015 conj. 3 : « Les enfants apportent des cadeaux et vont chez le petit aveugle. » au futur — QCM « apporteront », QCM « iront » — 2 q.
    - piège (étiquette à porter par un distracteur) : mal former le futur du verbe irrégulier — ligne C12#9 (d2)
  - 2013 conj. 2 : « Les enfants vont se mettre à la fenêtre et attendent leurs parents. » au futur — QCM « iront se mettre … attendront » — 1 q.
    - piège (étiquette à porter par un distracteur) : mal former le futur du verbe irrégulier — ligne C14#8 (d2)
  - 2013 conj. 3 : « Ce soir, Sylvie prépare un rapide souper. Ensuite, elle va rejoindre François devant le petit écran. » avec « Hier soir » — QCM « a préparé », QCM « est allée » (l'accord) — 2 q.
    - piège (étiquette à porter par un distracteur) : oublier l'accord du participe avec être — ligne C14#9 (d2)
  - 2008 conj. 2 : « Les enfants vont dans la cour et prennent des photos. » au futur — QCM « iront … prendront » — 1 q.
    - piège (étiquette à porter par un distracteur) : mal former le futur d'un verbe irrégulier — ligne C19#8 (d2)
  - 2009 conj. 3 : « Abdel fait équipe avec Ludovic. » au futur — QCM « fera » (le radical irrégulier) — 1 q.
    - piège (étiquette à porter par un distracteur) : laisser le présent ou mal former le radical — ligne C18#9 (d1)
  - 2010 conj. 3 : « Je vais très bien. Je prépare une surprise. » en remplaçant « je » par « nous » — QCM « Nous allons … nous préparons » — 2 q.
    - piège (étiquette à porter par un distracteur) : garder la forme du singulier — ligne C17#9 (d2)
- Ne pas redemander : `06/quiz#2`, `06/quiz#3`, `06/01-pratique#2`, `06/01-pratique#3`, `06/02-boss#3`, `06/02-boss#4`, `06/03-revision#3`, `06/03-revision#4`, `06/03-revision#6`, `06/04-defi#4`, `06/05-entrainement#4`
- Note : Famille « aller / faire » du `06`. C09#11 (passé composé d'aller et de vouloir) est au `08` (vouloir / pouvoir), C16 non applicable. Les verbes en -er et « prendre » du même exercice sont donnés. Onze questions.

#### m021 → `exercices/07-exams-2009-2025-accord-de-ladjectif.json` · d2 practice 75/15 · 10 questions · régime **examen**

- Titre : « 🏛️ Concours 2009–2025 · changer le nom, changer le sujet : l'accord de l'adjectif ⭐⭐ »
- Registre : id `C02#6` ; sources `C02#6, C05#8, C09#6, C10#5, C14#5, C14#6, C15#6, C18#5`
- Sources (base en premier) : C02 (2025) ex. 6 ; C05 (2022) ex. 8 ; C09 (2018) ex. 6 ; C10 (2017) ex. 5 ; C14 (2013) ex. 5 ; C14 (2013) ex. 6 ; C15 (2012) ex. 6 ; C18 (2009) ex. 5
- Items :
  - 2025 gram. 2 : « Après un long moment, une tête à la chevelure hérissée apparait. » devient « Après une … attente, une tête aux cheveux … apparait. » — QCM « longue », QCM « hérissés » — 2 q.
    - piège (étiquette à porter par un distracteur) : oublier l'accord de l'adjectif avec le nom changé — ligne C02#6 (d2)
  - 2018 gram. 1 : « Les racines de l'arbre sont solides et fortes. » avec l'expression soulignée remplacée par « l'arbre » — QCM « solide et fort » — 1 q.
    - piège (étiquette à porter par un distracteur) : laisser les adjectifs au pluriel ou au féminin — ligne C09#6 (d2)
  - 2017 gram. 2 : « Caroline est muette mais elle est intelligente. » à commencer par « Bruno et Juliette » — QCM « muets … intelligents » (sujets mêlés : masculin pluriel) — 1 q.
    - piège (étiquette à porter par un distracteur) : oublier l'accord au masculin pluriel avec sujets mêlés — ligne C10#5 (d3)
  - 2013 gram. 2 : « Deux petites têtes rondes apparaissent … » avec « têtes » remplacé par « visages » — QCM « petits … ronds » — 1 q.
    - piège (étiquette à porter par un distracteur) : laisser les adjectifs au féminin — ligne C14#5 (d2)
  - 2013 gram. 3 : « Chers parents, vous nous manquez beaucoup. » avec « parents » remplacé par « maman » — QCM « Chère maman » (cher / chère), QCM « tu nous manques » — 2 q.
    - piège (étiquette à porter par un distracteur) : garder la forme du pluriel pour un destinataire unique — ligne C14#6 (d3)
  - 2012 gram. 2 : « Les premiers oiseaux arrivent après un long voyage. » avec « oiseaux » → « hirondelles », « voyage » → « traversée » — QCM « premières … longue » — 1 q.
    - piège (étiquette à porter par un distracteur) : laisser les adjectifs au masculin — ligne C15#6 (d2)
  - 2009 gram. 2 : « Les enfants entrent sur scène, un peu angoissés. » à commencer par « Violeta » — QCM « angoissée » — 1 q.
    - piège (étiquette à porter par un distracteur) : oublier le féminin de l'adjectif — ligne C18#5 (d2)
  - 2022 gram. 3 : « Pensive, madame Leroux dit : « C'est une idée fabuleuse. » » avec « madame » → « monsieur » et « idée » → « choix » — QCM « un choix fabuleux » ; « pensif » est DONNÉ (`HP:adjectif-if-ive`) — 1 q.
    - piège (étiquette à porter par un distracteur) : garder la forme du féminin — ligne C05#8 (d2)
- Ne pas redemander : `06/quiz#4`, `06/01-pratique#4`, `06/02-boss#1`, `06/04-defi#3`, `06/05-entrainement#5`
- Note : Famille « accord de l'adjectif avec le nom » du `06` (modèles heureux/heureuse, fier/fière, cher/chère). La consonne doublée (nul/nulle, bon/bonne, gros/grosse) est au `07`. Écartés : C04#7 et C06#6 (changer le genre du sujet : le participe pronominal s'accorde, `HP:pc-pronominal`).

#### m022 → `exercices/08-exam-2023-lecture-un-combat-victorieux.json` · d2 practice 75/15 · 9 questions · régime **examen**

- Titre : « 🏛️ Concours 2023 · lecture : un combat victorieux ⭐⭐ »
- Registre : id `C04#1` ; sources `C04#1, C04#2, C04#3, C04#4`
- Sources (base en premier) : C04 (2023) ex. 1 ; C04 (2023) ex. 2 ; C04 (2023) ex. 3 ; C04 (2023) ex. 4
- Items :
  - Q1 : « Qu'est-ce qui était le plus difficile pour Claudine ? a. Avant l'opération … b. Après l'opération … » — QCM avant (le regard des autres), QCM après (rester immobile et réapprendre à marcher) ; leurre : confondre les deux moments — 2 q.
    - piège (étiquette à porter par un distracteur) : confondre les deux moments — ligne C04#1 (d2)
  - Q2 : « Claudine acceptait son handicap. Relève dans le texte deux indices qui le montrent. » — multi des deux indices ; QCM « quelle phrase montre le contraire » — 2 q.
    - piège (étiquette à porter par un distracteur) : relever des phrases qui montrent le contraire — ligne C04#2 (d2)
  - Q3 a : synonymes de « Je souffrais d'__une déviation__ de la colonne vertébrale » et de « Je suis restée __confinée__ au lit » ; Q3 b : « Trouve dans le texte le contraire du nom __interdiction__ et du verbe __maltraiter__ » — un QCM par mot — 4 q.
    - piège (étiquette à porter par un distracteur) : chercher le contraire hors du texte ou de mauvaise nature — ligne C04#3 (d2)
  - Q4 : « Si tu étais à la place de Claudine, comment réagirais-tu positivement face au comportement des gens ? » — QCM « quelle réaction positive se place dans la situation de Claudine » (leurre : une réaction générale) — 1 q.
    - piège (étiquette à porter par un distracteur) : rester général sans se placer dans la situation — ligne C04#4 (d2)
- Ne pas redemander : `06/04-defi#1`, `06/04-defi#2`
- Note : Compréhension d'un texte récent (R2). Texte intégral : PDF officiel `/tmp/claude-0/fr6g/src/2023-francais.pdf` (sha256 au registre) ; citation utile : « Mais c'était un plaisir de réapprendre. » Les deux lignes du `06` qui lisent une lettre (défi#1, #2) sont un autre geste.

#### m023 → `exercices/09-exams-2023-2025-recit-reactions-et-gardien.json` · d3 boss 120/30 · 8 questions · régime **examen**

- Titre : « 🏛️ Concours 2023, 2025 · préparer un récit : décrire les réactions et rapporter les répliques ⭐⭐⭐ »
- Registre : id `C02#11` ; sources `C02#11, C04#11`
- Sources (base en premier) : C02 (2025) ex. 11 ; C04 (2023) ex. 11
- Items :
  - 2023 : « Claudine est maintenant guérie. Après une longue absence, elle est de retour à l'école. Elle est devenue une nouvelle personne. Ecris un récit de huit phrases au moins pour raconter la scène et décrire la réaction de ses camarades. Intègre dans ton récit un court dialogue. » — multi « quelles phrases décrivent la réaction des camarades » ; QCM de la réplique correctement ponctuée ; ordering du récit (arrivée, regards, réplique, réponse) — 4 q.
    - piège (étiquette à porter par un distracteur) : omettre le dialogue ou les réactions — ligne C04#11 (d3)
  - 2025 : « L'homme qui apparait soudain est le gardien de la pyramide. Furieux, il ordonne aux enfants de quitter immédiatement le lieu. Ces derniers le supplient de les laisser passer la nuit à cet endroit. Raconte … en décrivant le gardien et en rapportant le dialogue qui s'est déroulé entre lui et les enfants. » — QCM du portrait du gardien (aspect, geste, voix) ; QCM des verbes introducteurs (« ordonne », « supplient ») ; ordering des quatre répliques — 4 q.
    - piège (étiquette à porter par un distracteur) : décrire sans dialogue ou dialoguer sans ponctuation — ligne C02#11 (d3)
- Ne pas redemander : `06/quiz#5`, `06/02-boss#5`, `06/02-boss#6`, `06/04-defi#6`, `06/05-entrainement#6`
- Note : Archétype « répliques + passage descriptif » : correspond à la section du cours `06` « Raconter avec des répliques et un passage descriptif ». C02#11 relève du thème 08 (voyage) mais l'archétype décide du placement (choix du pilote : production regroupée par archétype).

#### m024 → `exercices/10-devoir-devoir-corriger-les-erreurs.json` · d3 boss 120/30 · 8 questions · régime **devoir** (salle blanche)

- Titre : « 📝 Corriger les erreurs : son ou sont, est ou et, accords ⭐⭐⭐ »
- Registre : id `D04#4` ; sources `D04#4, D04#3`
- Cartes : devoir F (épreuve de langue du 2ᵉ trimestre, école primaire), exercice 4 — carte anonyme ; devoir F (même épreuve), exercice 3 — carte anonyme
- Items :
  - Corriger des erreurs soulignées dans de courtes phrases (confusion être / conjonction « et », accord de l'adjectif, accord du verbe avec son sujet) : QCM « quelle correction est juste » (leurre : corriger sans distinguer le verbe être de la conjonction) ; multi « quels mots soulignés sont fautifs » ; QCM « pourquoi cette correction » — 5 q.
    - piège (étiquette à porter par un distracteur) : corriger sans distinguer le verbe être de la conjonction — ligne D04#4 (d3)
  - Compléter de courtes phrases par « son » ou « sont » (test de remplacement par « était / étaient » rappelé dans l'explication) — QCM de trois blancs, dont un leurre qui confond possessif et verbe être — 3 q.
    - piège (étiquette à porter par un distracteur) : confondre possessif et verbe être — ligne D04#3 (d2)
- Ne pas redemander : `03/01-pratique#5`, `03/01-pratique#6`, `03/03-revision#1`, `03/03-revision#3`, `03/04-defi#2`, `03/04-defi#6`, `03/05-entrainement#1`, `03/05-entrainement#5`, `04/01-pratique#6`, `04/03-revision#3`, `04/03-revision#4`
- Note : Salle blanche. Cartes de DEUX exercices du même devoir (un auteur, deux signatures voisines) : la correction d'erreurs est un geste absent des examens ; « son / sont » est déjà très présent au `03`, la carte demande donc de le replacer dans un texte de correction, sans nouvelle règle. Placement au chapitre le plus avancé de l'exercice (la correction cumule 04, 05 et 06). D04#2 (temps imposé par le contexte) est écarté : déjà couvert (04/quiz#3, 03/03-revision#2).

