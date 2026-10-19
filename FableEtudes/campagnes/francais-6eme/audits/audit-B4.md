# Audit B4 — french-6eme, `07-profiter-du-temps-libre` et `08-autres-modes-de-vie`

> Auditeur indépendant (opus), 2026-10-19. Branche `wip/francais-6eme-un-passage` (worktree `wt-fr6b`).
> Grilles appliquées : skill `content-audit`, grille du français 9ᵉ (`prompt-francais-auditeur.md`) et `course-quality.md`. Décisions F1–F9 du PLAN.
> Autorité : la fiche `programme/6eme-base/francais.md` (§ 2.7, § 2.8, § 2.10). PDF relus aux pages reprises : cahier 121615 p.85, 87, 93, 94, 97, 99, 103, 108 ; manuel 121614 p.132.
> Méthode : j'ai re-résolu à l'aveugle les 70 questions (quiz + 5 exercices × 2), sans regarder la clé. J'ai lu le rapport de l'auteur seulement après. Rien n'a été modifié dans `content/`, aucune écriture git.

## 0. Gates et rendu

| Contrôle | Résultat |
| --- | --- |
| `content:check` (global) | ✓ `french-6eme: 8 chapters, 40 exercises, 240 questions`. Pas besoin de copie isolée. |
| `content:qa -- --subject french-6eme` | ✓ aucune clé suspecte |
| `content:tranche … --chapters 07…,08… --fresh --strict-longest` | ✓ clé strictement la plus longue : 0/51. Positions a 31 % · b 20 % · c 22 % · d 27 %. 0 paire proche. 4 groupes gabarit inter-chapitres (§ 6). Patron de notion : 0 en recul. |
| `renderLesson` / `renderSummary` (vitest jetable, jsdom) | 8 sections par cours et 8 cartes par résumé ✓. Mais **204 tirets bas littéraux** s'affichent dans les deux cours (M-1). Résumés propres. |
| Chromium 360 px (CSS `.lesson-content` du moteur) | Pas de débordement de page (scrollWidth 360). **Trois tableaux de 4 colonnes dans le cours 07** (F9), cassés au milieu des mots : « dison/s », « écrivon/s », « Fémi/nin », « neuv/e », « gentill/e » (M-2). Certains tableaux de 3 colonnes cassent aussi (m-1). |

Le test vitest jetable a été supprimé du moteur (`git status` propre). Les captures et les cours corrigés de référence restent dans mon scratchpad : `/tmp/claude-0/-home-user/973107ae-1cd3-5286-9aad-458ef39f3138/scratchpad/b4/`.

## 1. Synthèse

70 questions re-résolues. **Toutes les clés sont justes.** Une seule question a deux réponses défendables : `08/03-revision` q5, où « parti **par** taxi » se dit aussi (C-1).

| Chapitre | Questions | Critiques | Majeurs | Mineurs |
| --- | --- | --- | --- | --- |
| 07-profiter-du-temps-libre | 35 | 0 | 8 | 9 |
| 08-autres-modes-de-vie | 35 | 1 | 9 | 6 |
| commun aux deux (rendu) | — | — | 1 | 1 |

Les défauts lourds :
- **le rendu** : 118 et 86 tirets bas littéraux. C'est la variante « tiret bas » du défaut récurrent des astérisques ;
- **les trois tableaux de 4 colonnes** du cours 07 (F9) ;
- **deux règles fausses** dans les cours : « _je_ et _tu_ ont **toujours** la même forme au présent », et « **Seuls** les verbes en -er (et _aller_) perdent le s » ;
- **un pronom complément ciblé dans le cours 08** (« _Leur_ : il désigne les élèves », F1) ;
- **quatre notions testées sans être enseignées** : *rentrer* + être, *débarquer*, *décoller/atterrir*, *se quitter/se retrouver* ;
- **deux doublons** : *neuf → neuve*, *ils peuvent* ;
- **une fuite entre questions** (*débarquer*) ;
- **trois clés reconnaissables à leur forme**, et **trois items du boss ou du défi qui recopient le cours**.

## 2. Re-résolution — tableau (✓ = ma réponse = la clé)

**07** — quiz q1 a ✓ · q2 d ✓ · q3 b ✓ · q4 c ✓ · q5 a ✓ (doublon M-9) | 01 q1 d ✓ · q2 a,b ✓ · q3 a ✓ · q4 c ✓ · q5 d ✓ · q6 b ✓ | 02 q1 a ✓ · q2 a,c ✓ · q3 b ✓ · q4 d ✓ · q5 a ✓ · q6 c ✓ | 03 q1 d ✓ · q2 b ✓ · q3 a ✓ · q4 c ✓ · q5 b,c,a ✓ · q6 a,b ✓ | 04 q1 « écrivez » ✓ · q2 l1r2 l2r4 l3r1 l4r3 ✓ · q3 b,e,d,a,c ✓ · q4 a,b,d ✓ · q5 d ✓ · q6 a ✓ | 05 q1 b ✓ · q2 a ✓ · q3 d ✓ · q4 **6** ✓ · q5 « complément de temps » ✓ · q6 c ✓.

**08** — quiz q1 a ✓ · q2 a ✓ · q3 a ✓ · q4 c ✓ · q5 d ✓ | 01 q1 a,b,c ✓ · q2 b ✓ · q3 a ✓ · q4 c ✓ · q5 d ✓ · q6 d ✓ | 02 q1 a ✓ · q2 a,b ✓ · q3 b ✓ · q4 d ✓ · q5 a ✓ · q6 c ✓ | 03 q1 c ✓ · q2 d ✓ · q3 l1r3 l2r1 l3r2 ✓ · q4 d ✓ · **q5 a ou b (C-1)** · q6 b ✓ | 04 q1 « peuvent » ✓ · q2 ✓ · q3 b,d,a,c ✓ · q4 a,b,e ✓ · q5 b ✓ · q6 c ✓ | 05 q1 d ✓ · q2 ✓ · q3 b ✓ · q4 c ✓ · q5 « débarquer » ✓ · q6 a ✓.

**Reprises du cahier et du manuel (champ `manuel`)**, confrontées au PDF :
- 07 `03-revision` : p.85 ex.2a (chevreau, ordre 2-3-1 ✓) ; p.87 ex.1 (« J'… la vérité » ✓) et ex.2 (« Dis-moi ton avis sur ce film » ✓) ; p.94 ex.4a (« couloirs animé… affiches multicolore » ✓).
- 07 `05-entrainement` : p.93 ex.1, « un manteau neuf → la robe … » ✓.
- 08 `01-pratique` : p.97 ex.1 (Philippe, Sabrine ✓) ; p.99 ex.3 (robe et Champs-Élysées, le père à son fils ✓).
- 08 `03-revision` : p.97 ex.2 (taxi ✓, voir C-1) ; p.99 ex.3 (« Vous ne … pas savoir » ✓) ; p.103 ex.1b (phoques ✓) ; p.108 ex.2 (hirondelles, Madame Dupont ✓).
- 08 `05-entrainement` : manuel p.132 ex.3 (intrus, sous-ensemble des six mots ✓), ex.4 (contraires, mot pour mot ✓), ex.5 (proverbe ✓, distracteurs changés).
- Pages et items justes. **Mineur (m-2)** : `07/01-pratique` q2 reprend presque mot pour mot le cahier p.85 ex.1a (Catherine, la colonie, le chevreau), mais le fichier ne porte pas de champ `manuel`. Ajouter à `01-pratique.json` : `"manuel": { "code": "121615P00", "pages": "85", "items": ["ex. 1a p.85"] }`.

**Bornes F1/F5** :
- Aucune question ne cible un pronom complément, le gérondif, une relative ou ne…rien/que.
- Le cours 08 cible *leur* (M-11).
- Accord avec *avoir* : aucune question ne le cible. Seule l'option `08/02-boss` q4 b « ont rentrés » l'exécute en passant (M-14).

## 3. Commun aux deux cours

### M-1 — 204 tirets bas affichés tels quels (rendu)
Le moteur n'ouvre l'italique `_…_` que devant une lettre ou un chiffre (`UNDERSCORE_ITALIC`, `markdown.ts` l.110). Il le ferme bien après une ponctuation. Quatre formes cassent donc dans ces cours :
1. **`_« … »_`** : l'italique ouvre devant « (40 cas dans le cours 07, 31 dans le cours 08) ;
2. **`_-ons_`, `_-ent_`, `_-eau_`, `_-er_`, `_-re_`, `_-ille_`, `_-a_`, `_-as_`** : l'italique ouvre devant un tiret ;
3. **les titres de bloc** (`::: exemple conjuguer _« écrire… »_ … avec _nous_`) : le titre est échappé en texte brut, sans aucun formatage (l.319) ;
4. **l'italique dans du gras** (`**_gentil_ avec _cousine_**`, `**Présent, _nous_**`) et le gras qui suit un `_` (`_« **Le Hanami…`).

L'élève voit par exemple « _« Après le goûter, Lina lit… »_ » avec les tirets. Le même défaut existe dans les chapitres 01, 02, 05 et 06 : respectivement 27, 37, 16 et 10 occurrences de `_«`/`_-` dans les sources. **À signaler au pilote.**

**Correctif côté contenu** (mécanique, vérifié : 0 tiret bas et 0 astérisque restant au rendu des deux cours, et la forme résiste à Prettier) :
- `_« ` → `« _` et ` »_` → `_ »` (exemple : `« _Après le goûter, Lina lit un roman dans le jardin._ »`) ;
- `_-ons_` → `-_ons_` (et de même pour toutes les terminaisons) ;
- dans toute ligne `::: exemple …` : supprimer tous les `_` (le titre reste en texte simple) ;
- dans tout `**…**` qui contient des `_` : supprimer les `_` (`**gentil avec cousine**`, `**Présent, nous**`, `**Tu et vouloir**`) ;
- cours 08 l.363 : `« **Le Hanami au Japon** : au printemps, … des masques et des costumes. »`, sans italique.

Fichiers de référence, prêts à comparer avec `diff` (seuls ces changements de rendu y figurent) : `/tmp/claude-0/-home-user/973107ae-1cd3-5286-9aad-458ef39f3138/scratchpad/b4/fix/07-profiter-du-temps-libre-cours.md` et `…/b4/fix/08-autres-modes-de-vie-cours.md`.

**Correctif moteur conseillé** : autoriser `«` et `-` après le `_` ouvrant dans `UNDERSCORE_ITALIC`, c'est-à-dire `(?=[\p{L}\p{N}«-])`. Cela répare tout le corpus d'un coup. C'est une décision du pilote, au même titre que le suivi de F9.

### m-1 — tableaux de 3 colonnes qui cassent aussi à 360 px
F9 ne suffit pas toujours. Avec `overflow-wrap: anywhere`, des tableaux de 3 colonnes coupent aussi des mots :
- cours 07, tableau de la lettre : « d'interpe/llation », « paragraph/es », « Signatur/e » ;
- cours 08 : « narra/tion » et « descr/iption » (tableau narration/description), « chaussur/es » (participe employé seul), « Partici/pe ».

Mineur, en attendant le suivi moteur (`overflow-wrap: normal` sur `.lesson-table`). Si l'on veut corriger côté contenu :
- cours 08, tableau narration/description → 2 colonnes : `| Phrase | Elle… |` avec les lignes `raconte une action` / `montre le lieu` / `dit comment est l'air` / `raconte une action` ;
- cours 07, tableau de la lettre → 2 colonnes : `| Partie | Exemple |`, avec la place dans la 1ʳᵉ cellule : `**Lieu et date** (en haut, à droite)`, `**Formule d'interpellation** (à gauche, avec une virgule)`, `**Corps** (en paragraphes)`, `**Formule d'adieu** (après le corps)`, `**Signature** (tout en bas)`.

## 4. Chapitre 07 — majeurs

### M-2 — trois tableaux de 4 colonnes (F9)
Ils sont cassés à 360 px (capture `tbl-07-1.png`, `tbl-07-3.png`). Scissions exactes, toutes à 3 colonnes au plus :

l.68-76 (présent et passé composé) → deux tableaux :
```
|            | dire       | lire       |
| ---------- | ---------- | ---------- |
| je         | **dis**    | **lis**    |
| tu         | **dis**    | **lis**    |
| il, elle   | **dit**    | **lit**    |
| nous       | **disons** | **lisons** |
| vous       | **dites**  | **lisez**  |
| ils, elles | **disent** | **lisent** |


| sujet      | écrire         |
| ---------- | -------------- |
| je / j'    | **écris**      |
| tu         | **écris**      |
| il, elle   | **écrit**      |
| nous       | **écrivons**   |
| vous       | **écrivez**    |
| ils, elles | **écrivent**   |
```
puis une ligne de prose sous les deux tableaux : `Passé composé, avec _avoir_ : _j'ai dit_, _j'ai lu_, _j'ai écrit_.`

l.118-125 (futur et impératif) → deux tableaux :
```
| verbe  | futur, je       | futur, ils        |
| ------ | --------------- | ----------------- |
| dire   | je **dirai**    | ils **diront**    |
| lire   | je **lirai**    | ils **liront**    |
| écrire | j'**écrirai**   | ils **écriront**  |

| verbe  | impératif, tu | impératif, nous / vous    |
| ------ | ------------- | ------------------------- |
| dire   | **dis**       | **disons** · **dites**    |
| lire   | **lis**       | **lisons** · **lisez**    |
| écrire | **écris**     | **écrivons** · **écrivez** |
```
La phrase pont l.127 reste juste. *Tu liras* figure déjà dans l'ancrage et dans l'exemple.

l.167-174 (adjectifs) → 2 colonnes, sur le modèle du manuel p.110 (singulier · pluriel dans chaque case) :
```
| Masculin (sing. · plur.) | Féminin (sing. · plur.)  |
| ------------------------ | ------------------------ |
| neuf · neufs             | neu**ve** · neu**ves**   |
| beau · beau**x**         | **belle** · **belles**   |
| vieux · vieux            | **vieille** · **vieilles** |
| bon · bons               | bon**ne** · bon**nes**   |
| gentil · gentils         | genti**lle** · genti**lles** |
| gros · gros              | gros**se** · gros**ses** |
```

### M-3 — règle fausse : « Seuls les verbes en -er (et aller) le perdent » (`cours.md` l.138)
*Ouvre*, *offre*, *cueille* perdent aussi le s. Remplacement de la dernière phrase du piège : `Les verbes en _-er_ (et _aller_) le perdent ; _dire_, _lire_ et _écrire_, eux, le gardent.`

### M-4 — `04-defi` q3 recopie l'exemple du cours (l.284-293)
Mêmes morceaux : « Tunis, le 3 mai », « Je t'embrasse », « Sami », « J'aime jouer au football et lire des bandes dessinées ». Pour le **doute n° 5** : seule, la question est juste et son ordre est unique, mais c'est une question de mémoire. Le doublon avec `06/01-pratique` q5 disparaît avec l'appariement décidé par le pilote. Remplacer les options (ordering, sans étiquette) :
- a `À très bientôt, je vous embrasse.` · b `Bizerte, le 14 juillet` · c `Yasmine` · d `Je vais au club de natation tous les matins. Et vous, que faites-vous ?` · e `Chers grands-parents,`
- ordre `b, e, d, a, c` (unique : lieu et date, interpellation, corps, adieu, signature). L'explication actuelle reste juste.

### M-5 — `05-entrainement` q1 : copie du cours et clé reconnaissable à sa forme
L'énoncé est mot pour mot l'exemple du cours (l.337, « la personne qui reçoit la lettre »). Surtout, la clé « le destinataire » est la seule option sans complément (« de la lettre », « du quartier »). Remplacer :
- prompt : `Sami poste une lettre pour sa cousine Lina. Comment appelle-t-on Sami, la personne qui envoie la lettre ?`
- options : a `le destinataire` (`fr.lexique.mot-voisin-du-meme-champ`) · b `l'expéditeur` (clé) · c `le facteur` (`fr.lexique.mot-voisin-du-meme-champ`) · d `le lecteur` (sans étiquette). Longueurs 15/12/10/10.
- explication : `Celui qui envoie la lettre est l'expéditeur. Le destinataire la reçoit et le facteur la distribue : ces mots sont du même thème, mais ils nomment d'autres personnes. Le lecteur est celui qui lit.`

### M-6 — `05-entrainement` q2 : copie du cours et clé reconnaissable à sa forme
« Synonyme de *se divertir* » est la question du `::: verifie` (l.354), aussi présente dans la définition, le piège et le résumé. La clé est la seule option sans complément (« en classe », « en route », « beaucoup »). Remplacer :
- prompt : `Dans « Le dimanche, Sami se distrait avec ses cousins : ils jouent aux cartes. », quel verbe a le même sens que « se distrait » ?`
- options : a `s'amuse` (clé) · b `s'ennuie` (`fr.lexique.contraire-pour-synonyme`) · c `se dispute` · d `se dépêche`. Longueurs 7/8/10/10.
- explication : `Se distraire, c'est passer un moment agréable : dans cette phrase, « s'amuse » dit la même chose. « S'ennuie » dit le contraire ; « se dispute » et « se dépêche » ont un autre sens.`

### M-7 — `03-revision` q6 (multi) : deux distracteurs éliminés à vue
« Dans les couloirs » et « il admire » ne sont pas des adjectifs : la question se réduit à trouver les deux adjectifs. Pour reprendre le cahier p.94 ex.4a en entier (toutes les formes viennent de ses paires) :
- prompt : `« Laurent aime l'odeur du métro souterrain. L'enfant aime aussi l'éclairage vive des stations et le claquement brusque des portières. Dans les couloirs animé, il admire les affiches multicolore. » Quels adjectifs sont mal accordés ? Choisis TOUS les bons.`
- options : a `souterrain` · b `vive` · c `brusque` · d `animé` · e `multicolore` ; `correct: ["b","d","e"]`.
- explication : `« Éclairage » est masculin : on écrit vif ; vive est le féminin, comme neuve pour neuf. « Couloirs » est masculin pluriel : animés. « Affiches » est féminin pluriel : multicolores, car un adjectif en -e prend seulement le s. « Souterrain » et « brusque » s'accordent bien avec « métro » et « claquement », masculins singuliers.`
- cours l.192, ajouter au `::: propriete`, après « … (_un livre rouge, une guitare rouge_). » : ` Comme _neuf → neuve_ : _vif → vive_.`

### M-8 — pièges du cours sans étiquette dans `coursePitfalls`
Les ids existent, ils sont tous sur la carte M7 et ils sont déjà portés par un distracteur. Ajouter à `chapter.json` → `coursePitfalls` :
- `fr.conj.forme-irreguliere-regularisee` (piège l.89 « Vous disez » ; `01-pratique` q3 b) ;
- `fr.lecture.deduction-sans-indice` (piège l.246 « Yassine est le cousin » ; `03-revision` q4 a) ;
- `fr.lexique.contraire-pour-synonyme` (piège l.345 ; `05-entrainement` q2 b, actuel et corrigé) ;
- `fr.texte.injonctif-non-reconnu` (piège l.401 ; `05-entrainement` q3 a, b).

### M-9 — doublon : quiz q5 et `05-entrainement` q6 (*neuf → neuve*)
Mêmes quatre formes (neuve / neuf / neufe / neufs ou neuves). Le 05 q6 est la reprise du cahier p.93 : c'est donc le quiz qu'il faut changer (il recopie en plus l'ancrage du cours « une guitare neuve »).
- prompt : inchangé (`Quelle phrase accorde bien l'adjectif ?`)
- options : a `Sami a pêché une grosse truite.` (clé) · b `Sami a pêché une gros truite.` (`fr.accord.adjectif-non-accorde`) · c `Sami a pêché une grose truite.` (`fr.accord.feminin-adjectif-mal-forme`) · d `Sami a pêché une grosses truite.` (sans étiquette). Longueurs 31/29/30/32.
- explication : `Truite est un nom féminin singulier : gros double son s et prend un e, ce qui donne grosse. « Grose » oublie de doubler la consonne, « gros » n'est pas accordé, et « grosses » porte un s du pluriel alors qu'il n'y a qu'une truite.`

## 5. Chapitre 07 — mineurs

- **m-3** `cours.md` l.402 : le piège porte « ✗ ✓ » sans diagnostic. Après « … parmi ceux qui disent comment faire. », insérer : `✗ On se fie au sujet du texte au lieu de regarder à quoi il sert.` Même défaut au cours 08 l.374 (même ajout).
- **m-4** `cours.md` l.382 : « _Le nombre pensé_ » est cité entre guillemets comme un texte, mais ce n'est pas celui du manuel p.116 (5 lignes A–E, nombres de 1 à 30, têtes 2/1/16/8/4). La version du cours est une adaptation (4 listes, 1 à 15). Titre d'exemple : `::: exemple reconnaître un jeu inspiré du « Nombre pensé » du manuel : …`.
- **m-5** quiz q1 : « Les enfants de Sami » (Sami est un enfant dans tout le chapitre) → `Les amis de Sami`, partout dans l'énoncé et l'explication.
- **m-6** `02-boss` q4 a « tu lira » porte `fr.conj.futur-mal-forme`. Or le futur est bien formé, c'est la personne qui est fausse. Retirer l'étiquette (option muette) : `fr.accord.verbe-non-accorde-au-sujet` n'est pas sur la carte M7.
- **m-7** `02-boss` q5 : « Dis-moi ce que tu fais » n'est pas un conseil. Prompt : `Sami demande à son ami de lui raconter sa journée. Quelle phrase est un impératif bien écrit ?`
- **m-8** `05-entrainement` q5 (short_answer) : le moteur ne retire pas l'article (`normalizeRecallText`). Ajouter `"acceptedAnswers": ["le complément de temps", "un complément de temps"]`.
- **m-9** `04-defi` : q1 à q3 sont à d2 et aucune question n'est à d4 pour un défi ⭐⭐⭐⭐ (même constat pour le défi 08). Le calibrage est généreux.
- **m-10** `retenir` l.55 et résumé, puce 1 : « [le complément de temps] s'accorde avec le temps du verbe » prête à confusion avec l'accord grammatical. Remplacer par `et le temps du verbe doit lui correspondre`.
- **m-11** Complétude manuel (axe 7) : les mots-outils *mais, pourtant, cependant* (manuel p.105) sont enseignés, mais aucune question ne les teste.
- Copies tolérées au quiz et en pratique : quiz q3 (« Hier, Lina a … une carte postale », la phrase du piège l.89), quiz q4 (« Écris-moi vite », l'ancrage l.110), `02-boss` q1 (« dans deux jours », le cas-limite l.37).

## 6. Chapitre 08 — critique et majeurs

### C-1 — deux réponses défendables : `03-revision` q5 (« Le touriste est parti … taxi »)
Dans le cahier p.97 ex.2, les trois blancs se partagent *en, par, de*, ce qui force « en taxi ». Isolée, la phrase admet aussi « par taxi » (*se rendre à l'hôtel par taxi* se dit). De plus, le cours l.12 donne justement *par* parmi les mots qui introduisent un complément de manière. Remplacer l'option b :
- options : a `en` (clé) · b `à` · c `de` · d `dans`. Longueurs 2/1/2/4.
- explication : `On part en taxi, comme en train ou en avion : « en taxi » répond à « comment ? », c'est un complément de manière. On dit « à pied » ou « à vélo », mais pas « à taxi » ; « de taxi » ne se dit pas, et « dans » demanderait un article (dans un taxi).`

### M-10 — règle fausse : « Retiens que _je_ et _tu_ ont toujours la même forme au présent » (`cours.md` l.81)
C'est faux pour *être*, *avoir* et *aller* (je suis / tu es…). Remplacement de la dernière phrase du piège : `Retiens qu'avec _vouloir_ et _pouvoir_, _je_ et _tu_ ont la même forme.`

### M-11 — pronom complément ciblé dans le cours (F1) : « _Leur_ : il désigne les élèves » (l.251, l.269-271)
Le pas 2 de l'exemple fait analyser *leur*, un pronom complément. Remplacements :
- l.251 : `Le gardien du phare montre la lampe aux élèves. Il explique qu'elle tourne toute la nuit pour guider les bateaux. Les élèves écoutent avec attention, puis ils montent au sommet. Les enfants admirent la mer.`
- l.269-271 :
```
1. **Il explique** : _il_ remplace _le gardien_ ← masculin singulier, c'est le seul homme de l'histoire.
2. **Elle tourne** : _elle_ remplace _la lampe_ ← féminin singulier, et c'est la lampe qui guide les bateaux.
3. **Ils montent** et **les enfants admirent** : _ils_ et _les enfants_ désignent les élèves ← même pluriel, même groupe.
```
- `::: verifie` l.284 : `Dans « _Les enfants regardent le gardien. Il sourit._ », que désigne _il_ ?` (le corrigé reste juste).

### M-12 — notion testée sans être enseignée : *rentrer* avec être (`02-boss` q4)
Le cours l.133 dresse la liste des verbes qui se conjuguent avec être, et *rentrer* n'y est pas (ni dans les cours 01 à 06). Remplacements :
- l.133 : `✓ _Aller_, _partir_, _arriver_, _sortir_, _rentrer_, _tomber_, _rester_ et _revenir_ se conjuguent avec **être** : _elle est allée_.`
- `resume.md`, puce 3 : `_aller, partir, arriver, sortir, rentrer, tomber, rester, revenir_ prennent **être**`

### M-13 — notions testées sans être enseignées et fuite : `05-entrainement` q2 et q5
- Le cours n'enseigne pas q2 (contraires *décoller/atterrir*, *embarquer/débarquer*, *se quitter/se retrouver*). Seul *embarquer* est défini.
- **Fuite** : q2 apparie *embarquer ↔ débarquer*, et q5 demande ensuite *débarquer*. La route suit `displayOrder` : q2 donne toujours la clé de q5.
- L'explication de q5 ne nomme pas la clé.

Correctifs :
- cours l.302, dans la `::: definition`, après « … pour partir. » : ` Son contraire est **débarquer** : descendre à l'arrivée. Un avion **décolle** au départ et **atterrit** à l'arrivée.`
- q2 (sous-ensemble fidèle de l'ex.4 p.132) : gauche l1 `partir` · l2 `décoller` · l3 `se quitter` ; droite r1 `atterrir` · r2 `se retrouver` · r3 `arriver` ; paires l1r3, l2r1, l3r2. Explication : `Partir s'oppose à arriver, décoller à atterrir, et se quitter à se retrouver.`
- q5, explication : `Débarquer, c'est descendre d'un bateau ou d'un avion à l'arrivée. C'est le contraire d'embarquer (monter à bord) : le préfixe dé- annonce l'action inverse.`

### M-14 — option à deux erreurs étiquetée : `02-boss` q4 b « Les touristes ont rentrés hier soir. »
L'option exécute deux erreurs : le mauvais auxiliaire et l'accord avec *avoir*, ce qui touche la borne F5. Remplacer : `Les touristes ont rentré hier soir.` (`fr.conj.auxiliaire-mal-choisi`). Longueurs 36/35/37/37, la clé n'est pas strictement la plus longue. Explication : `Rentrer se conjugue avec être, comme aller ou revenir : sont rentrés. Le participe s'accorde avec le sujet masculin pluriel : rentrés. Les autres phrases oublient l'accord, emploient l'auxiliaire avoir ou écrivent l'infinitif.`

### M-15 — doublon : quiz q3 (« Mes cousins … prendre le bateau ») et `04-defi` q1 (« Mes parents ne … pas venir »)
Même fait : *ils peuvent*. *Veulent* n'est testé nulle part. Remplacer `04-defi` q1 :
- prompt : `Écris la forme du verbe vouloir qui complète la phrase : « Les voyageurs … visiter la médina avant de partir. » (présent)`
- `answerKey.text` : `veulent` ; `expectedMistakes` : `[{ "text": "voulent", "misconceptionTag": "fr.conj.forme-irreguliere-regularisee" }]`
- explication : `Les voyageurs se remplace par ils. Au pluriel, vouloir change de radical (veul-) et prend la terminaison -ent, comme peuvent pour pouvoir.`

### M-16 — clé reconnaissable à sa forme : `04-defi` q6 (doute n° 3)
L'indice du texte tranche bien. Mais la clé « Pour ne pas effrayer les mouettes. » est la seule option qui ne commence pas par « Parce que », et elle recopie le texte. Remplacer l'option c : `Parce qu'ils ne veulent pas effrayer les mouettes.` Longueurs 42/40/50/50. Explication : `Le texte dit que les élèves descendent sans bruit « pour ne pas effrayer les mouettes » : ils ne veulent pas faire peur aux oiseaux. Les mouettes ne les ont pas effrayés (c'est l'inverse), et le texte ne parle ni d'un ordre du guide ni de fatigue.`

### M-17 — `05-entrainement` q4 recopie le `::: verifie` du cours (l.382)
Même « Matériel : carton, ciseaux », mêmes étapes (« Découpe », « Colle »), en mode boss. Remplacer :
- prompt : `« Ingrédients : deux œufs, un verre de lait, de la farine. 1. Casse les œufs dans un bol. 2. Ajoute le lait et la farine. 3. Mélange bien. » Quel est le type de ce texte ?`
- options : a `Un récit qui raconte un goûter en famille.` · b `Un texte qui informe sur l'histoire des crêpes.` · c `Un texte qui dit comment préparer une recette.` (clé) · d `Une lettre à un ami pour lui parler de ses loisirs.`. Étiquette `fr.texte.injonctif-non-reconnu` sur a, b, d. Longueurs 42/47/46/51.
- explication : `Une liste d'ingrédients, des étapes numérotées et des verbes à l'impératif (casse, ajoute, mélange) : c'est un texte qui dit comment faire. Il ne raconte rien, n'informe pas sur l'histoire des crêpes et ne s'adresse pas à un ami.`

### M-18 — `coursePitfalls` incomplets, et trois ids hors de la carte M8
- À ajouter à `coursePitfalls` (08) : `fr.reprise.substitut-ne-correspond-pas` (piège l.275 ; `03-revision` q6 a, c), `fr.lexique.contraire-pour-synonyme` (piège l.322 ; `05` q5, expectedMistakes), `fr.texte.injonctif-non-reconnu` (piège l.373 ; `05` q4).
- **Au pilote** : `fr.reprise.substitut-ne-correspond-pas`, `fr.lexique.sens-figure-lu-au-propre` (`05` q6 c, d) et `fr.lecture.cause-consequence-inversees` (`04` q6 b) sont posés sans figurer dans la carte M8. Leur libellé nomme exactement l'erreur : il faut les ajouter à la ligne M8 de `map-vocab.md` et `vocab-french-6eme.json`. Même chose pour `fr.lecture.personnage-confondu` au M7 (`07/03` q3 b, c).

## 7. Chapitre 08 — mineurs

- **m-12** `01-pratique` q6 : la clé « le voyageur » est la seule option sans complément (« de location », « du quartier »). Options : a `la voiture` (`fr.lexique.mot-voisin-du-meme-champ`) · b `le voyou` · c `les voyelles` · d `le voyageur` (clé). Longueurs 10/8/12/11. Dans l'explication, remplacer « Voyou et voyelle » par `Voyou et voyelles`.
- **m-13** `cours.md` l.102 : « le dernier mot change de forme » est faux (les derniers mots sont *grands-parents*, *elle*, *tard*). Remplacer par `le participe passé change de forme`.
- **m-14** Copies tolérées au quiz et en pratique : quiz q1 (l'exemple Karim–Kairouan mot pour mot), quiz q2 (« Tu … visiter Rome »), `01-pratique` q5 (« Sarra est … à Rome », l'ancrage et le piège).
- **m-15** La section « Lire un récit de voyage et une bande dessinée » enseigne *vignette, bulle, onomatopée* sans figure et sans question qui les teste. Une petite planche SVG de deux vignettes (bulle et onomatopée) servirait l'axe Illustration.
- **m-16** Doute n° 4 de l'auteur : « Petit à petit, l'oiseau fait son nid » est un exemple maison, pas du manuel. C'est acceptable : la notion de proverbe est celle de p.132 ex.5, et l'exercice utilise bien le proverbe du manuel.

## 8. Gabarits et paires (`content:tranche`)

- « quel groupe est le complément de lieu / de temps / de manière » (06↔07, 06↔08), « quelle phrase contient un complément de… » (06↔07) : **acceptables**. Les cadres sont parallèles, mais chaque item vise une notion différente (lieu, temps, manière), conformément au cahier (p.70, p.85, p.97).
- « quel mot a le même sens que » (05↔07) : réglé par M-6, la nouvelle q2 a un autre cadre.
- Dans le chapitre 07, `01` q2 et `02` q2 sont deux multi « quels groupes sont des compléments de temps ? ». C'est un gabarit (mineur), toléré parce que les textes et les pièges diffèrent (*depuis Sousse*, *à Yassine*).

## 9. Doutes de l'auteur — verdicts

1. **Phrase « avec avoir, le participe ne s'accorde pas avec le sujet » (cours 08 l.137, et l.184)** : **acceptable, à garder.**
   - La fiche range ce constat en ✅ (§ 2.8 Bornes : « constat que _avoir_ ne s'accorde pas avec le sujet »). C'est l'« Attention ! » du manuel p.125, vérifié au PDF.
   - La phrase est vraie (le participe ne s'accorde **jamais** avec le sujet de *avoir*). Elle ne dit rien du COD antéposé, et F5 interdit seulement de **cibler** cet accord.
   - Condition : aucune option ne doit exécuter l'accord avec *avoir*, d'où M-14.
2. **07/03-revision q1** : **clé unique.**
   - « Dites-moi ton avis » mêle *vous* et *ton* : c'est incohérent face à plusieurs personnes.
   - « Disez » et « Disons-moi » sont impossibles.
   - Les possessifs sont enseignés au chapitre 02.
3. **Lettres et textes courts maison** : un indice tranche à chaque fois.
   - 07/03 q3 : la signature, « Chère Lina », « Tunis ».
   - 07/03 q4 : « chez mon oncle ».
   - 07/04 q5 : « viens passer les vacances chez moi ».
   - 08/04 q6 : « pour ne pas effrayer les mouettes ». Cette clé se repère toutefois à sa forme, voir M-16.
4. **Nombre pensé** :
   - Les listes du cours sont justes (A = bit 1, B = bit 2, C = bit 4, D = bit 8). 11 est bien dans A, B et D.
   - Calcul de 07/05 q4 : B ∩ C = {6, 7, 14, 15}, moins A (impairs) donne {6, 14}, moins D donne {6}. Clé 6, réponse unique ✓, énoncé correct.
   - Seule réserve : le cours présente cette adaptation comme « le texte » du manuel (m-4).
5. **07/04-defi q3 seule** : **juste, ordre unique**, mais elle recopie l'exemple du cours. À remplacer (M-4).

## 10. Verdict

**À corriger.** Le correctif tient en quatre blocs :
- **C-1** (une option) ;
- **le rendu** (M-1, mécanique) et **les tableaux F9** (M-2) ;
- **les deux règles fausses et le pronom *leur*** (M-3, M-10, M-11) ;
- **les items** (M-4 à M-7, M-9, M-12 à M-17), avec les `coursePitfalls` (M-8, M-18).

Toutes les clés actuelles sont justes. Chaque texte de remplacement ci-dessus a été vérifié : une seule réponse, la clé n'est pas strictement la plus longue, et aucune fuite vers une autre question du chapitre.
