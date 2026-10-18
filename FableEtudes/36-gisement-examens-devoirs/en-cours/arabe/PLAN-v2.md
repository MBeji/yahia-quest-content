# Gisement 9ᵉ × arabe — plan de la vague 2 : sessions 2002–2019 et devoirs (G3–G4, étude 36)

Écrit le 2026-10-18 par le planificateur. La vague 1 ([`PLAN.md`](./PLAN.md), 32 missions `m001`–`m032`,
publiées) n'est pas réécrite : ses règles R1–R6 restent en vigueur, et rien de ce qu'elle pose ne se
redemande ici.

Entrées : les 26 sujets lus de 2002 à 2019 (`C13`–`C39`, sans `C37` 2004 et `C40` 2001, introuvables ; 2014
absente de l'archive), leurs transcriptions (`content/programmes-officiels/examens-nationaux/9eme-base/arabic/`,
texte support résumé, intégral au PDF officiel), les 108 lignes et les trois journaux de lecture ; les six
devoirs `D01`–`D06` (63 lignes, `JOURNAL-lecture-devoirs.md`) ; le contenu `content/arabic/` (identique à
`origin/main`, 32 missions de la vague 1 comprises), le manifeste `9eme-base.json` et les `cours.md`.
Modèles : le plan v1 et le plan anglais (`../anglais/PLAN.md`).

Sorties :

- carte et écart : `content/programmes-officiels/sources-externes/web-9eme-base-arabic/fiche.md` § 3.4 (ajout
  « vague 2 ») et une ligne au § 4 ;
- plan : [`plan-examens-v2.json`](./plan-examens-v2.json) — 6 missions d'examen (`m033`–`m038`, lot `L06`),
  1 mission de devoirs (lot `L07`, clé `devoirs`), le sort de ce qui est écarté (`ecartes`, `devoirs.ecartes`),
  la mesure des signatures (`devoirs.signatures`) et deux propositions au pilote (`propositionsPilote`) ;
- registre : `…/web-9eme-base-arabic/gisement.json` — 7 missions `planifiee` (id = la source de base ;
  `sources` liste toutes les sources fusionnées ; `note` donne l'id du plan) ; les missions publiées et la
  section `documents` ne sont pas touchées ;
- affectations : [`assign-arabe-L06.md`](./assign-arabe-L06.md), [`assign-arabe-devoirs.md`](./assign-arabe-devoirs.md).

## 1. Ce que les lecteurs ont constaté — vérifié

Vérifié sur les lignes et les transcriptions, sans écart :

- **Générales 2009–2019 et épreuves uniques 2002–2008 (16 sujets)** : une page, « الإنشاء العربي » (2008 :
  « العربية », même nature), 2 h, coefficient 2, **un seul sujet de production**, sans texte, compréhension ni
  langue, sans barème. Quinze sont des **dialogues argumentatifs** à transcrire (« اُنْقُلِ الحِوَارَ… ») ; le
  seizième (2002) demande de décrire un comportement puis d'exposer ses arguments, sans dialogue.
- **Techniques 2009–2019 (10 sujets)** : texte narratif (expositif en 2011), questions 14 points, « تحرير فقرة »
  6 points. Sur 92 lignes, 66 de compréhension (chapitre 10), 10 productions (09), **14 lignes entièrement `HP`**
  (duel et accord, conjugaison avec les pronoms, pluriels, complément absolu, expressions figées, emploi de mots),
  2 mêlées (l'état du 03 en 2019, la défense du 04 en 2015) ; 2012, 2011, 2010 et 2009 n'ont aucune question
  de langue.
- **Devoirs (6, tous `devoir.tn`, collèges ordinaires)** : la seule source de la vague pour la grammaire au
  programme — 18 (10 lignes), 03 (5), 15, 13, 14 (4 chacun), 04, 12, 16, 17 (3), 05, 19 (2) ; 3 lignes tout
  `HP`, 1 mêlée. Un seul (D02, 2023-2024) relève du programme révisé ; les cinq autres sont gardés (décision du
  pilote), le plafond par auteur est tenu (Chabbi : D03 et D05).

## 2. Règles de la vague 2

Les règles R1–R6 de la v1 (unité = la question officielle ; 6 à 12 questions ; production convertie en
préparation fermée ; rien de `HP` ; pas de « سبر » au 11 ; étage de la ligne la plus haute) s'appliquent. S'y
ajoutent :

**V1 — Une session ancienne ne donne rien si elle redit la vague 1.** Le critère est l'archétype : une session
dont toutes les questions ont déjà leur geste dans une mission publiée est écartée entière, sans compensation
par le volume. C'est le cas de la plupart (§ 5).

**V2 — Production : une mission par archétype neuf, sujets fusionnés.** Le dialogue où le seul narrateur
argumente (« مُرَكِّزًا عَلَى الحُجَجِ الَّتِي اعْتَمَدْتَهَا ») est déjà la mission `m012` (2020) : huit sujets
anciens en sont la copie. Trois archétypes manquent à la vague 1 :
- le **dialogue à deux voix**, où la consigne exige les arguments de **chacun** (2013, 2011), les **deux avis**
  (2007) ou ceux de **l'autre partie** (2005, le père) → `m033` ; c'est le plan en neuf jalons que le cours 09
  enseigne (§ الإنتاج (1)) et qu'aucun sujet récent n'interroge ;
- la **modification (تعديل) d'une position dans un dialogue** (2018, 2006, 2008 ; et le paragraphe de 2018 T, qui
  demande de partager une responsabilité) → `m034` ; `m015` (2025) nuance dans un texte suivi, pas dans un
  dialogue, et jamais sous condition ;
- en filière technique, le paragraphe qui exige **à la fois des arguments et des conseils**, dans une **forme
  imposée** (discours du père, lettre, demande à une institution : 2017, 2016, 2012, 2011) → `m035` ; `m017` et
  `m018` ne distinguent jamais l'argument du conseil ni ne fixent de forme.
Chaque question dit sa session (« مناظرة 2013 ») et redonne la consigne officielle qu'elle travaille ; rien n'y
note la rédaction.

**V3 — Compréhension : trois textes, une mission chacun.** Les dix textes techniques posent les consignes de
`m005`–`m011` (titre, synonymes ou contraires, indices, cause, solutions, avis). Trois apportent un geste que la
vague 1 n'a pas, et ce sont les plus riches : **2015 T** (ordre des huit étapes d'un procédé, sens d'une
expression imagée), **2017 T** (répartir des traits entre deux groupes de personnages, la cause juste parmi des
fausses, choisir un facteur et le justifier), **2011 T** (le seul texte expositif à thèse : cause principale et
indice, critique d'une explication à cause unique). Placement au chapitre 10 (fichiers 18–20). Les textes ne
sont pas transcrits (filtre du 2026-10-16) : l'auteur les lit au **PDF officiel** (URL et sha256 au registre ;
copies de lecture hors git sous `/tmp/claude-0/arlec2/src/`) et n'en cite qu'**une à deux phrases par
question**, avec la référence de l'auteur telle qu'imprimée.

**V4 — Devoirs : une mission par signature neuve au regard des examens, du plan ET du patron.** Signature =
chapitres de la ligne (jetons `HP` ôtés) + famille d'archétype. Mesure au § 4.

**V5 — `HP`.** Aucune mission. Une notion qui tombe dans `01-i3rab-wal-bina` ou `06-al-mushtaqqat` sans y être
déjà posée est **proposée** au pilote, jamais planifiée (§ 6).

**Étages et en-têtes.** Dialogues de la générale : d3 (lignes d3 ; conversion comme `m012`–`m016`) ;
paragraphe technique : d2 (comme `m017`, `m018`) ; compréhension : d2 ; devoir : d3 (ligne D02#12). En-têtes :
d2 practice 75/15, d3 boss 120/30 ; titres de la v1 (« 🏛️ مناظرة … » / « 🏛️ مناظرات … ») ; `sources[]` du
`chapter.json` touché : la ligne du § 3 de la v1 si elle manque.

## 3. Missions

| mission | chapitre (NN) | sources (base en premier) | archétype | étage | q. | lot |
| --- | --- | --- | --- | --- | ---: | --- |
| `m033` | `09` (14) | 2013 G ; 2011 G, 2007, 2005 | dialogue à deux voix : arguments de chacun, de l'autre partie, les deux avis | d3 | 9 | L06 |
| `m034` | `09` (15) | 2018 G ; 2006, 2008, 2018 T | modifier une position dans un dialogue : concéder, corriger, thèse sous condition | d3 | 8 | L06 |
| `m035` | `09` (16) | 2017 T ; 2016 T, 2012 T, 2011 T | arguments **et** conseils dans une forme imposée (discours, lettre, demande) | d2 | 9 | L06 |
| `m036` | `10` (18) | 2015 T | récit d'un savoir-faire : expression imagée, synonymes, peine et plaisir, ordre des étapes | d2 | 8 | L06 |
| `m037` | `10` (19) | 2017 T | consommation : contraires, traits répartis entre deux groupes, cause juste, facteur justifié | d2 | 8 | L06 |
| `m038` | `10` (20) | 2011 T | texte expositif à thèse : cause principale et indice, domaines, autres causes | d2 | 8 | L06 |
| `D02#11` | `12` (07) | D02#11 + D02#12 (salle blanche) | le nom manqus en emploi ; participe actif d'un verbe défectueux | d3 | 7 | L07 |

**7 missions, environ 57 questions** ; aucun chapitre de langue n'en reçoit d'examen (les sessions anciennes
n'en ont pas au programme), un seul en reçoit de devoir.

## 4. Lots

| lot | chapitres (NN) | missions | consigne | parallélisme |
| --- | --- | --- | --- | --- |
| L06 | `09` (14–16), puis `10` (18–20) | `m033`–`m038` (6) | `gisement-auteur-examen.md` (reprise citée) + transcriptions + PDF officiels pour les trois textes | avec L07 |
| L07 (devoirs) | `12` (07) | `D02#11` (1) | `gisement-auteur-devoir.md` (salle blanche : l'auteur ne reçoit que la carte) | avec L06 |

Skill : `prof-arabe-9eme`, puis `content-ecole-tn`, `content-engine`, `content-interactif`. Prompt commun :
`prompt-arabe-auteur.md` (v1), à ceci près que l'arbre de travail et le moteur sont ceux que l'orchestrateur
désigne, et que **L06 lit trois PDF officiels** (C22, C18, C28) pour les textes de compréhension. Le lot L07 n'a
qu'une mission : la vague n'apporte pas plus (§ 4 bis).

### 4 bis. Le lot devoirs et la mesure des signatures neuves (règle des 30 %)

63 lignes, dont 3 tout `HP` (D01#4, #7, #8) : **60 lignes comptées**.

- **Au regard des 226 lignes d'examen (C01–C39)** : **15 signatures neuves (25 %)** — D01#9, D04#16 (production
  qui doit employer des outils de liaison et des incises), D02#7, #8, #9 (phrase réduite, appel, souhait réduit :
  les examens n'ont jamais interrogé que l'ordre et la défense au 04), D02#11, #12 (manqus), D03#2 (comparer
  deux images d'un texte), D04#9, D05#4, D05#5, D06#4 (proposition de temps et ordre des événements, 03 + 18),
  D04#10 (كان + قد), D04#15 (13 + 14), D05#3 (17 + 18).
- **Au regard du plan (v1 + v2) et du patron** : **3 (5 %)** — D02#11, D02#12, D03#2. Les douze autres ont leur
  geste dans une mission ou au patron (`m024`, `m023`, `m019` ; patron 02 : la transformation en كان + قد cinq
  fois ; patron 04 : la réduction du souhait, les formes de l'appelé ; `m029`, `m030` pour le 13 + 14).
- **Mission** : D02#11 + D02#12 → `12` (07), le nom manqus en emploi (écrire ses formes selon le cas et la
  détermination ; le participe actif d'un verbe défectueux est manqus, le passif ne l'est pas) ; le patron 12 n'a
  sur le manqus que sept QCM, presque tous de reconnaissance, et `m026` n'y touche pas. D03#2 est écarté : une ligne,
  attachée au texte du devoir.
- **Conclusion** : sous 30 % dans les deux comptes → **pas de vague 3** (proposition P2 au pilote).

## 5. Ce qui est écarté, et pourquoi

Détail machine : `plan-examens-v2.json` (`ecartes`, `devoirs.ecartes`).

| écarté | quoi | pourquoi |
| --- | --- | --- |
| **sessions entières** 2019 G, 2017 G, 2016 G, 2015 G, 2012 G, 2010 G, 2009 G, 2003 | dialogue où seul le narrateur argumente | V1 : `m012` (2020) en pose toutes les décisions ; « الحجج والأمثلة » (2010, 2009) : argument et exemple déjà distingués (`m014` Q5, 09/01 Q2) |
| **session entière** 2002 | décrire un comportement, puis argumenter | une session, sans dialogue ; la description n'est pas au 09 |
| **compréhension** de 2019, 2018, 2016, 2013, 2012, 2010, 2009 T (45 lignes) | titre, synonymes ou contraires, indices, cause, solutions, avis | V3 : mêmes consignes que `m005`–`m011` et que les trois textes retenus ; perdus et assumés : le basculement du récit (2012), trois types de justification (2016, proche de la répartition de 2017) |
| paragraphes 2019, 2015, 2013 T | valeur d'une activité, des métiers manuels | moule de `m017`, `m018` |
| paragraphes 2010 T, 2009 T | rapport d'activité, présentation d'un projet | non argumentatifs : hors du 09 révisé |
| **sessions entières** 2010 T, 2009 T, 2019 T, 2018 T (sauf son paragraphe, dans `m034`), 2016 T (sauf son paragraphe, dans `m035`), 2013 T, 2012 T (sauf son paragraphe) | — | conséquence des lignes ci-dessus |
| 14 lignes tout `HP` + parties `HP` de 2 lignes | duel et accord (4 : dossier 01, déjà `m032`), conjugaison, pluriels, complément absolu, expressions, emploi de mots | décision du pilote ; rien à proposer pour le 01 (déjà posé) |
| 2019 T 3 ج (état), 2015 T 3 أ (défense) | parties au programme | déjà `m024` (7 sessions techniques) et `m020` |
| 2004, 2001 | — | introuvables ; le corrigé 2004 n'est pas repris |
| devoirs : 57 lignes sur 60 | compréhension, langue, productions | § 4 bis : leur geste est dans une mission ou au patron |

## 6. Propositions au pilote

| | objet | constat | recommandation |
| --- | --- | --- | --- |
| **P1** | D01#8 (`HP:mushtaqqat` : masculin, féminin, schème et racine de dérivés à racine faible ou redoublée) → `06-al-mushtaqqat` | aucune mission du 06 ne le pose (`m031` : participes et nom d'action) ; mais racine et schème sont denses au 05 (`m027`, `m028`, patron), le féminin est un acquis de 7ᵉ–8ᵉ, une seule ligne d'un devoir antérieur à la révision | **non** |
| **P2** | vague 3 de devoirs | 5 % (plan et patron), 25 % (examens seuls) | **non** ; si elle s'ouvre : devoirs du programme révisé seulement (2023-2024 et après), Chabbi exclu par le plafond |

Rien d'autre ne tombe dans `01` ou `06` sans y être déjà posé : les quatre lignes de duel (2019, 2018, 2017,
2015 T) ont `m032`.

## 7. Arbitrages (réversibles lot par lot)

1. **Huit sessions générales et une unique écartées entières** (V1) : c'est le cœur du « profondeur avant
   volume » ; leurs sujets restent cités au registre, une mission pourrait les reprendre si le propriétaire veut
   un entraînement par sujet.
2. **`m034` mêle un dialogue (générale) et un paragraphe (2018 T)** : l'opération (partager une responsabilité,
   nuancer) prime la forme ; retirer la question 8 rend la mission purement « dialogue ».
3. **Les productions non argumentatives (rapport, projet) écartées** comme hors du 09 révisé.

## 8. Contrôle local

`content:gisement:controle` (moteur `/home/user/eng-svtses`), le 2026-10-18, sur la fiche (§ 3.4 et § 4), ce
plan, `assign-arabe-L06.md` et `assign-arabe-devoirs.md` :

- **contre les six snapshots de devoirs** (`/tmp/claude-0/devoirs-snapshots/arabic/`) : **0 plage de 8 mots, 0
  de 6 mots** dans les quatre textes ; « données communes » 2 sur la fiche, le plan et L06 : des années de session
  (2013, 2016, 2018, 2019) et des numéros de fichier ou de chapitre, faux positif ; l'affectation des devoirs :
  0. Salle blanche tenue : aucune phrase, aucun contexte, aucun nombre d'un devoir dans la carte.
- **contre les 38 transcriptions** (copiées en `.txt` hors git) : fiche et plan, **0 plage de 8 mots, 0 de 6** ;
  données communes = années de session ; `assign-arabe-L06.md`, 25 plages de 8 mots (la plus longue 41) : ce sont
  les consignes officielles citées à dessein (corpus officiel, reprise citée), que l'auteur doit retrouver ;
  l'affectation des devoirs, 0.
- `content:check -- --content-dir /home/user/wt-ar2/content` : vert (120 sujets). `content:qa --subject
  arabic` sur le même arbre (lancé depuis une copie de liens du moteur, sans toucher au lien `content` de
  `eng-svtses`) : 0 erreur, 1 avertissement préexistant (`11-annales-subur` sans domaine) ; garde
  anti-verbatim des fiches comprise.

## Décisions du pilote (2026-10-18)

P1 (D01#8 au dossier 06) : **non**. P2 (vague 3 de devoirs) : **non** (25 % / 5 % de signatures neuves, sous 30 %).
Les trois arbitrages réversibles du § 7 sont acceptés tels que proposés.
