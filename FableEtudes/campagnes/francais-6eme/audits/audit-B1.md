# Audit B1 — french-6eme, `01-travailler-pour-sepanouir` et `02-communiquer-avec-les-autres`

> Auditeur indépendant (opus), 2026-10-19. Branche `wip/francais-6eme-un-passage` (worktree `wt-fr6b`), état des fichiers vers 09:00.
> Grilles appliquées : skill `content-audit`, grille français 9ᵉ (`prompt-francais-auditeur.md`), `course-quality.md`.
> Autorité : fiche `programme/6eme-base/francais.md` (§ 2.1, § 2.2, § 2.10), PLAN F1–F7, PDF 121615 (cahier) et 121614 (manuel) relus aux pages reprises (p. 4, 7-10, 12, 19, 23-26 du cahier ; p. 23 et 39 du manuel).
> Méthode : les 70 questions ont été re-résolues à l'aveugle (quiz + 5 exercices × 2 chapitres, clés masquées) avant toute lecture des clés, du rapport et des notes de l'auteur. Rien n'a été modifié dans `content/`, aucune écriture git.

## 0. Gates et rendu

| Contrôle | Résultat |
| --- | --- |
| `content:check` (global, `eng-deliver`) | ✓ `french-6eme: 8 chapters, 40 exercises, 240 questions` ; 121 matières validées |
| `content:qa -- --subject french-6eme` | ✓ aucune clé suspecte, 0 erreur |
| `content:tranche … --chapters 01…,02… --fresh --strict-longest` | ✓ clé strictement la plus longue 0/49 ; positions a 20 % · b 33 % · c 22 % · d 24 % ; paires proches 0 ; gabarits 0 ; patron de notion 0 en recul |
| Rendu `renderLesson` / `renderSummary` (vitest jetable, supprimé ; `git status` du moteur propre) | ⚠️ **un défaut** : cours 01 l.259, astérisques littéraux (M-2). Le reste est propre : 8 sections par cours, tableaux, blocs `definition` / `exemple` / `piege` / `verifie` / `retenir`, 8 cartes de résumé par chapitre |
| Chromium 360 px | aucune figure SVG dans les 4 fichiers. Pas de débordement de page ; deux tableaux sont plus larges que la colonne (cours 01, tableau des temps : 353 px ; cours 02, tableau de l'impératif à 6 colonnes : 452 px) et défilent dans leur cadre (`.lesson-table` est en `display:block; overflow-x:auto`) : conforme |

## 1. Re-résolution : synthèse

70 questions re-résolues. **Toutes les clés sont justes.** Trois questions du chapitre 01 ont **une deuxième réponse défendable** (C-1 à C-3). Aucune explication ne désigne une option par sa lettre ou son rang.

| Chapitre | Questions | Critiques | Majeurs | Mineurs |
| --- | --- | --- | --- | --- |
| 01-travailler-pour-sepanouir | 35 | 3 | 3 | 8 |
| 02-communiquer-avec-les-autres | 35 | 0 | 3 | 8 |

## 2. Critiques (deux réponses défendables)

### C-1 — `01/quiz.json` q5 (contradiction, magasin fermé)

Clé b (« Les clients attendent devant la porte. »). Mais **d** « Le vendeur emballe des cadeaux dans la boutique. » ne contredit pas « Le magasin est fermé depuis midi » : un vendeur peut travailler dans une boutique fermée au public. De plus, **a** « à quatre heures » peut se lire 4 h du matin, donc avant midi.

Remplacements (texte d'option seulement, ids et étiquettes inchangés) :

- a : `Une cliente achète un bouquet à quatre heures.` → `Une cliente achète un bouquet à quatre heures de l'après-midi.`
- d : `Le vendeur emballe des cadeaux dans la boutique.` → `Le vendeur accueille des clients dans la boutique.`
- `explanation` : `Si le magasin est fermé depuis midi, aucun client n'y entre l'après-midi : personne n'y achète, n'y est servi ni n'y est accueilli. Seule la phrase où les clients attendent devant la porte reste cohérente ; les trois autres supposent que le magasin est ouvert.`

Vérifié : une seule réponse (b) ; la clé (38 car.) n'est pas la plus longue (a 62, d 50, c 34) ; aucune fuite.

### C-2 — `01/exercices/04-defi.json` q4 (multi, Nour horticultrice)

Clé [b, c]. Mais « Elle ne touche jamais aux plantes » (c) contredit **aussi** a « Nour est horticultrice… » : le cours enseigne justement le métier comme premier point à vérifier (« le **métier** du personnage », verifie Walid coiffeur / moteurs). La paire [a, c] est défendable, et l'explication se contredit (« les deux autres phrases (le métier…) sont compatibles »).

Remplacements :

- c : `Elle ne touche jamais aux plantes.` → `Sa serre ne contient aucune rose.`
- `explanation` : `Si Nour fait pousser des roses dans sa serre chaque matin, sa serre ne peut pas être vide de roses : « Sa serre ne contient aucune rose » contredit la deuxième phrase. Le métier d'horticultrice reste compatible (elle peut cultiver d'autres plantes), comme le retour du soir.`

Vérifié : c ne contredit plus que b (une horticultrice peut ne pas cultiver de roses) ; d reste neutre ; une seule paire, [b, c].

### C-3 — `01/exercices/01-pratique.json` q6 (ordering, journée du facteur)

Clé d, b, f, c, a, e (ordre du cahier p. 8). Le critère de l'énoncé (fait → maintenant → à venir) fixe les trois blocs mais pas l'ordre **dans** un bloc. Dans le présent, « Il distribue le courrier. Maintenant, il va de maison en maison. » est aussi lisible que l'ordre clé ; le moteur refuse pourtant tout autre ordre.

Remplacement du `prompt` :

> Remets dans l'ordre la journée du facteur : ce qui est déjà fait, puis ce qui se passe maintenant, puis ce qui arrivera. Dans chaque moment, la phrase qui porte l'indicateur de temps vient en premier.

Ajout à la fin de l'`explanation` : ` Dans chaque moment, la phrase qui porte l'indicateur (de bon matin, maintenant, le soir) ouvre le groupe.`

Vérifié : passé d (« De bon matin ») puis b ; présent f (« Maintenant ») puis c ; futur a (« Le soir ») puis e : ordre unique, inchangé ; la reprise du cahier (ex. 3b p. 8) garde ses données.

## 3. Majeurs

### M-1 — `01/cours.md` l.149 (piège des trois temps) — exemple faux dans le diagnostic

Le piège porte sur « _a vérifié_ » mais la parenthèse décompose « (_a_ + _desserré_) », vestige de l'encadré p. 14. L'élève lit une décomposition qui ne correspond pas au verbe.

Remplacement : `(_a_ + _desserré_)` → `(_a_ + _vérifié_)`.

### M-2 — `01/cours.md` l.259 — rendu : astérisques affichés

`(_sans \**s'\**arrêter_)` sort en HTML `<em>sans *<em>s'*</em>arrêter</em>` : l'élève voit « sans \*s'\*arrêter ».

Remplacement : `(_sans \**s'\**arrêter_)` → `(_sans s'arrêter_)`.

### M-3 — `01/exercices/05-entrainement.json` q3 (Sylvie) — deux distracteurs éliminés d'emblée, étiquettes sans objet

L'énoncé ne cite que Sylvie : « hôtesse de l'air » et « animatrice dans un village de vacances » ne viennent d'aucune donnée de la question (le texte « Témoignages » n'est pas fourni) et s'éliminent à vue ; `fr.lecture.personnage-confondu` ne peut pas s'exécuter sans autre personnage dans l'énoncé.

Remplacements :

- `prompt` : `Joël est animateur dans un village de vacances. Sylvie, elle, a vendu des chaussures dans un grand magasin pendant les vacances ; elle rêve d'être bibliothécaire un jour. Quel métier Sylvie a-t-elle vraiment exercé ?`
- options : a `animatrice dans un village de vacances` [`fr.lecture.personnage-confondu`] · b `vendeuse de chaussures` (clé) · c `bibliothécaire` [`fr.lecture.deduction-sans-indice`] · d `vendeuse de livres` (muette)
- `explanation` : `Le texte dit que Sylvie a vendu des chaussures : c'est le métier qu'elle a exercé. Bibliothécaire n'est qu'un rêve pour plus tard, animateur est le métier de Joël, et rien ne dit qu'elle a vendu des livres.`

Vérifié : une seule réponse (b) ; clé 22 car., pas la plus longue (a 38) ni seule à porter un trait ; chaque étiquette nomme l'erreur exécutée (attribuer le métier de Joël ; prendre un rêve pour un fait).

### M-4 — `02/resume.md` carte 1 et `02/cours.md` l.53 (retenir) — « suit le nom » se lit comme une règle de place fausse

Le résumé dit « ils **suivent** le nom (_cet ordinateur_, _cette imprimante_) » : un élève de 11 ans comprend « se placent après le nom », le contraire de la définition. La carte de révision enseigne donc une erreur (grille : erreur reprise dans le résumé).

Remplacements :

- `resume.md`, carte 1 : `- **Les déterminants démonstratifs** — ils montrent et se placent devant le nom : _ce_ (masculin), _cet_ (masculin devant voyelle ou h muet), _cette_ (féminin), _ces_ (pluriel) ; on les choisit d'après le nom (_cet ordinateur_, _cette imprimante_).`
- `cours.md` l.53 : `_ce_ (masculin), _cet_ (masculin devant voyelle), _cette_ (féminin), _ces_ (pluriel) : le démonstratif montre, se place devant le nom et se choisit d'après lui.`

### M-5 — `02/cours.md` l.213 (retenir) et `02/resume.md` carte 4 — la règle du s de l'impératif est généralisée au-delà du manuel (doute 1)

Le `::: propriete` (l.169-173) est fidèle à l'encadré p. 30, limité aux modèles (« -ir comme _choisir_, -re comme _faire_, _prendre_ »). Mais le `retenir` (« un _s_ **sinon** ») et le résumé (« un _s_ **pour les autres** ») en font une règle générale, fausse pour des verbes usuels : _ouvrir_, _offrir_, _cueillir_ (_ouvre_, _offre_, _cueille_), _avoir_ (_aie_), _savoir_ (_sache_). Le piège est réel pour l'élève : « Ouvre la fenêtre » est une consigne courante, et « Ouvres » serait appris comme juste. Aucune question ne teste ces verbes (vérifié), donc aucune clé n'est fausse ; le défaut est dans la règle à retenir.

Remplacements :

- `cours.md` l.213 : `À l'impératif, pour _tu_ : pas de _s_ pour les verbes en _-er_ et pour _aller_ (_cherche, va_) ; un _s_ pour les verbes en _-ir_ comme _choisir_ et en _-re_ comme _faire_, _prendre_ (_choisis, fais, prends_).`
- `resume.md`, carte 4 : `- **Le s de l'impératif (tu)** — pas de _s_ pour un verbe en _-er_ et pour _aller_ (_cherche, utilise, va_) ; un _s_ pour les verbes en _-ir_ comme _choisir_ et en _-re_ comme _faire_, _prendre_ (_choisis, fais, prends_).`
- Recommandé (cas limite exigé par l'axe 2, sans question à ajouter) : dernière puce du `::: propriete` l.172, à ajouter après celle des verbes en -ir/-re : `- attention : _ouvrir_ s'écrit comme un verbe en _-er_ : **ouvre** la fenêtre, sans _s_.`

### M-6 — `02/exercices/05-entrainement.json` q2 (ordering, gestes de Sandra) — deux ordres défendables (doute 2)

Clé b, e, d, a, c. Le manuel (jeu 2 p. 39) n'imprime pas de corrigé. Si allumer → saisir … éteindre sont forcés, « imprime » puis « enregistre » est un ordre réel et défendable (on peut imprimer un document avant de l'enregistrer). Le cours (l.392) fixe l'ordre par décret, mais l'élève qui raisonne sur la réalité est refusé.

Remplacements :

- a : `Sandra imprime son document.` → `Sandra imprime le document enregistré.`
- `explanation` : `Il faut d'abord allumer la machine, puis saisir le texte. On l'enregistre, et c'est ce document enregistré qu'on imprime. On éteint l'ordinateur à la fin, quand il ne sert plus.`
- le champ `manuel.items` passe à `["jeu 1 p. 39"]` (la phrase modifiée fait de q2 une variante, qui ne porte pas le champ).

Vérifié : a suppose d ; ordre unique b, e, d, a, c.

## 4. Mineurs

### Chapitre 01

- **m-1** `01/cours.md` l.45 — « Un mot qui refuse le déterminant… n'est pas un nom » est faux pour le nom propre, que le cours vient de présenter sans déterminant (_Hédi_). Remplacement : `Un verbe comme _saluer_ ou _courir_ refuse le déterminant (on ne dit pas _« le courir »_) : ce n'est pas un nom, il ne va donc dans aucune colonne des noms.`
- **m-2** `01/exercices/02-boss.json` q5 et `05-entrainement.json` q4 (short_answer) — l'explication ne nomme pas la réponse. Remplacements : q5 `Dans « nous avons pris », « avons » est l'auxiliaire et « pris » porte le sens : il vient de prendre, un infinitif en -re.` ; q4 `Beaucoup dit une grande quantité ; son contraire, peu, dit une petite quantité : il y a peu de médecins.`
- **m-3** `01/exercices/05-entrainement.json` q2 (doute 3) — `fr.lexique.mot-voisin-du-meme-champ` sur _souvent_, _toujours_, _parfois_ : ces mots disent la fréquence, pas la soudaineté ; ils ne sont pas du même champ que la clé (_soudain_). Rendre les trois distracteurs **muets**.
- **m-4** `01/exercices/04-defi.json` q5 — option d « Quatre » étiquetée `fr.reprise.substitut-ne-correspond-pas` : quatre suppose deux erreurs (compter le public ET le prénom) ; la rendre muette.
- **m-5** `01/exercices/05-entrainement.json` q6 — l'option b « Elle commencent… » mêle un pronom faux et un verbe désaccordé ; pour que `fr.accord.verbe-non-accorde-au-sujet` nomme exactement l'erreur : b → `Elles commence par préparer les tables.` (39 car. ; clé 41, égalée par c : pas de fuite).
- **m-6** `01/exercices/03-revision.json` q5 — les trois légendes sont réécrites (« Un jour, en enlevant… », « Il dégage… ») alors que l'exercice déclare la reprise « ex. 2a p. 9-10 ». Rétablir le texte du cahier (vérifié sur le PDF) : a `L'homme dégage le coffret ; il est plein d'or. « Quelle merveille ! » dit le brave homme.` · b `Chaque matin, Jean va à la forêt. Il coupe du bois pour le vendre.` · c `Un jour qu'il commence à enlever la terre pour retirer la racine morte d'un arbre, le bonhomme trouve un coffret.` L'ordre b, c, a reste unique. Les autres reprises du lot (q2, q3, q4 de ce fichier ; `01-pratique` ; jeu 4 p. 23) ont des données conformes au PDF, simplement raccourcies.
- **m-7** `01/cours.md` piège jardinier / horticulteur (l.424-428) — aucun item ne le teste. Le laisser, ou réutiliser le couple dans une prochaine mission.
- **m-8** `01/exercices/03-revision.json` q3 (doute 3) — distracteurs muets acceptables ; c'est pourtant exactement le cas du libellé `fr.lexique.mot-voisin-du-meme-champ` (« le boulanger pour le facteur », même item du cahier p. 12) : étiquetage possible sur a, b, c. `04-defi.json` q2 : muets justes (aucune erreur reconstructible sur comptable / bibliothécaire).

### Chapitre 02

- **m-9** `02/cours.md` l.190 et `02/exercices/02-boss.json` q3 — « _aller_ fait exception » : son infinitif finit en -er et le manuel le range avec les verbes en -er ; il suit donc la règle. Cours l.190 : `3. _aller_ suit la même règle que les verbes en _-er_ → pas de _s_ : **Va** au club.` ; q3 `explanation` : `Aller suit la règle des verbes en -er : à l'impératif, à la 2e personne du singulier, il s'écrit « va », sans s. « Vas » ajoute un s, « tu va » garde le sujet, et « allez » s'adresse à plusieurs personnes.`
- **m-10** `02/exercices/01-pratique.json` q4 et `02-boss.json` q4 (short_answer) — l'explication ne nomme pas la réponse. q4 (01) : `Deux garçons possèdent plusieurs magazines : plusieurs propriétaires et plusieurs objets donnent leurs, avec un s.` ; q4 (02) : `Faire est irrégulier : à la 2e personne du pluriel, il ne prend pas -ez. On écrit faites, une forme à apprendre.`
- **m-11** `02/exercices/02-boss.json` q6 — énoncé maladroit (« inviter ton ami et toi »). Remplacement : `Tu proposes à ton ami de faire une recherche avec toi. Que dis-tu ?`
- **m-12** `02/exercices/05-entrainement.json` q5 — énoncé mal construit. Remplacement : `Dans la notice pour fabriquer la Une, quelle consigne adressée à l'élève (tu) est correcte ?`
- **m-13** `02/exercices/01-pratique.json` q6 — « Regarde le bâtiment neuf. » double l'énoncé. Remplacement : `Complète : « Regarde … hôpital, il est tout neuf ! »`
- **m-14** `02/exercices/05-entrainement.json` q4 — `fr.lecture.personnage-confondu` sur duplicateur / maquettiste / responsable financier : l'erreur est de prendre un autre rôle du même document, ce que nomme exactement `fr.lexique.mot-voisin-du-meme-champ` (son libellé cite « le maquettiste pour le secrétaire de rédaction »). Retaguer les trois.
- **m-15** `02/cours.md` piège « composer avant décrocher » (l.407-411) — aucun item ne le teste.
- **m-16** Rendu : le tableau de l'impératif (6 colonnes, 452 px) défile dans son cadre à 360 px. Conforme, à surveiller seulement.

## 5. Contrôles du prompt

- **Cours, notions de la fiche (§ 2)** : M1 GN (déterminants, noms propre/commun), pronoms personnels, trois temps, conjugué/infinitif, infinitif après à/de/par/pour/sans, substituts, structure du récit et non-contradiction, lexique des métiers et mots-outils des textes 1-3 : tout est enseigné, fidèle aux encadrés p. 13, 14, 17. M2 démonstratifs/possessifs (p. 29), impératif (p. 30, trois personnes, sans sujet, règle du s), a/à (p. 34), schéma du récit du cahier (p. 20, 22), métiers du journal (p. 35-37), boîte à mots (p. 38), mots-outils : tout est enseigné. Patron des sept temps présent dans les 16 sections ; exemples, pièges et vérifications re-résolus : seuls M-1 et M-5 sont faux ou trop larges.
- **F1** : aucun pronom complément, gérondif, relative ni ne…rien/que ciblé. Un gérondif apparaît en support (01 révision q5, « en enlevant » ; 02 boss q5, « en faisant ») : admis. **F5** : sans objet (aucun participe avec _avoir_ accordé).
- **`coursePitfalls`** : les 12 ids sont chacun montrés dans un `::: piege` et portés par au moins un distracteur (vérifié question par question).
- **Étiquettes** : toutes au registre ; aucune sur `multi`/`ordering`/`matching` ; défauts : m-3, m-4, m-5, m-14, M-3.
- **Reprises** : champs `manuel` confrontés au PDF (cahier p. 4, 7-8, 9-10, 12, 19, 23, 24, 25-26 ; manuel p. 23, 39) : pages et items justes, données conformes, sauf m-6 et M-6 (variantes). `01/05-entrainement` n'a pas de `code` : il hérite de 121614P00 du chapitre, ce qui est juste.
- **Âge et langue** : registre adapté à 11-12 ans ; français correct, hors m-11 et m-12. _Disquette_ (cahier p. 19) est daté mais repris du cahier : laissé.

## 6. Doutes de l'auteur — tranchés

1. **s de l'impératif** : le `::: propriete` est juste et fidèle au manuel ; le `retenir` et le résumé généralisent à tort (« sinon », « les autres »), et _ouvre_ est un vrai piège pour l'élève → **M-5**, avec la ligne _ouvrir_ recommandée comme cas limite.
2. **Sandra, enregistrer avant imprimer** : non unique dans la réalité → **M-6**, rendu unique par « le document enregistré ».
3. **Étiquettes mot-voisin (05 q2)** : non, ce n'est pas le même champ → muettes (**m-3**). 03 q3 et 04 q2 : les muets sont acceptables (**m-8**).
4. **Tableau des métiers** : tout ce qui est testé est enseigné (cours, tableau l.394-409 et verifie l.376) ou donné dans l'énoncé (documents de 04 q2 et 02/05 q4). Règle d'or respectée sur les deux chapitres.
5. **Impératif négatif** : aucune question ne le cible (vérifié). Constat pour le pilote : la fiche le range au tableau C (Fichier-classe seul), alors que le **cahier p. 21 ex. 3** (« Transforme ces phrases à la forme affirmative ou négative », « Ne lisez pas ces magazines ») est un exercice dédié. Selon sa règle (1), il serait ✅. La phrase d'exemple du cours (l.146) est donc légitime ; une question pourra s'y ajouter si F1 est révisé.

## 7. Verdict

**À corriger.** 3 critiques (C-1 à C-3, chapitre 01), 6 majeurs (M-1 à M-6), 16 mineurs. Toutes les clés actuelles sont justes ; chaque correctif a un texte de remplacement vérifié ci-dessus. Après correction : relancer `content:check`, `content:qa` et `content:tranche --strict-longest` (aucun remplacement ne fait de la clé l'option la plus longue).

## 8. Re-vérification (2026-10-19, après les corrections de l'auteur)

Base : section « Corrections après audit » de `rapports/rapport-B1.md` ; décisions F8 et F9 du `PLAN.md`. Fichiers relus sur la branche wip. Rien n'a été modifié sous `content/`, aucune écriture git.

### 8.1 État de chaque défaut

| Défaut | État |
| --- | --- |
| C-1 quiz 01 q5 | ✓ corrigé (texte de l'audit) ; re-résolu : seule b reste cohérente |
| C-2 01/04-defi q4 | ✓ corrigé ; re-résolu : une seule paire, [b, c] |
| C-3 01/01-pratique q6 | ✓ corrigé ; re-résolu : ordre unique d, b, f, c, a, e |
| M-1, M-2 cours 01 | ✓ (« a + vérifié » ; « sans s'arrêter » s'affiche sans astérisque) |
| M-3 01/05 q3 (Sylvie) | ✓ ; re-résolu : b seule ; étiquettes justes |
| M-4 démonstratifs (résumé, retenir) | ✓ |
| M-5 s de l'impératif | ✓ retenir l.239, résumé, ligne _ouvrir_ ajoutée au `::: propriete` |
| M-6 02/05 q2 (Sandra) | ✓ « le document enregistré » ; `items` = `jeu 1 p. 39` ; re-résolu : ordre unique |
| m-1, m-3, m-4, m-5, m-6 (vérifiés mot pour mot sur le PDF p. 9-10), m-8, m-9, m-11 à m-14 | ✓ corrigés et re-résolus |
| m-7, m-15 | aucune action : ce sont des constats, accepté |
| m-16 | remplacé par F9 (voir 8.3) |
| **m-2, m-10** (explications des `short_answer`) | **appliqués, mais à annuler** : voir 8.2 |

Les 19 questions modifiées (11 au chapitre 01, 8 au chapitre 02, dont 4 où seule l'étiquette change) ont été re-résolues à l'aveugle. Toutes les clés sont justes et chaque question n'a qu'une réponse.

Une précision sur le rapport de l'auteur : il écrit « étiquettes retaguées sur 03 q3 et 05 q4 du chap. 02 ». En réalité, 03 q3 est au chapitre 01 (m-8) ; seule 05 q4 est au chapitre 02. Les fichiers sont justes.

### 8.2 Écart sur les `short_answer` : il existe bien une règle contraire, et j'avais tort

`content-engine/references/content-schema.md` (tableau `short_answer`, champ `explanation`) dit : « même barre que `mcq`, **mais elle ne doit pas contenir la réponse littérale** (l'indice la révélerait) ». Le moteur le confirme. `revealHint` (`quest.server.ts` l.944-968, RPC `consume_hint`) sert l'`explanation` comme **indice consommable avant la réponse**. Une explication qui contient « prendre », « peu », « leurs » ou « faites » donne donc la clé à l'élève qui dépense un indice. L'argument du pilote (« l'explication s'affiche après la réponse ») ne tient pas pour ce chemin. Mes constats m-2 et m-10 étaient faux. Il faut **rétablir les textes d'origine**, qui enseignent sans livrer la réponse :

- `01/exercices/02-boss.json` q5 : `Dans un verbe en deux mots, le premier est l'auxiliaire et c'est le second qui donne le sens : on remonte du participe à l'infinitif, qui se termine par -re.`
- `01/exercices/05-entrainement.json` q4 : `Beaucoup dit une grande quantité ; son contraire dit une petite quantité, avec un mot court de trois lettres que les mots-outils du module font retenir.`
- `02/exercices/01-pratique.json` q4 : `Deux garçons possèdent plusieurs magazines : le possessif correspond à plusieurs propriétaires (eux) et à plusieurs objets, et il prend la marque du pluriel.`
- `02/exercices/02-boss.json` q4 : `Ce verbe est irrégulier : à cette personne, il ne prend pas la terminaison -ez des autres verbes. C'est une forme à apprendre.`

`content:qa` ne contrôle pas cette règle. Si on veut un garde-fou, c'est au moteur de l'ajouter.

### 8.3 F9 : les tableaux scindés ne suffisent pas, le correctif doit venir du moteur

Mesure faite dans Chromium à 360 px, avec les règles réelles de `src/styles.css` (`.lesson-content { overflow-wrap: anywhere; word-break: break-word }` et `.lesson-table` en `display:block`), en repérant les mots dont les rectangles tombent sur deux lignes :

- **Cours 01** : des mots sont coupés dans 6 des 9 tableaux, dont des tableaux à 2 et 3 colonnes. Exemples : en-tête « Déterminant » (« Détermina / nt »), « Singulier », « tiendra », « horticulteur », « esthéticienne ».
- **Cours 02** : 5 mots coupés dans 4 tableaux (« Démonstratif », « Utilisons », « Choisissons », « Donc », « perturbateur »).

La cause n'est pas le nombre de colonnes. `overflow-wrap: anywhere`, hérité par les cellules, rend leur largeur minimale nulle : le tableau ne défile jamais, il se comprime et coupe les mots. Contre-épreuve : en ajoutant **`overflow-wrap: normal; word-break: normal` sur `.lesson-table td, th`** (le « suivi moteur » déjà inscrit en F9), il n'y a **plus aucun mot coupé** dans les deux cours, et la page garde 360 px de large. Les tableaux scindés de l'auteur tiennent alors dans la colonne de 328 px. F9 ne peut donc pas être tenu par le contenu de B1 (il faudrait réécrire 10 tableaux, et la mesure dépend de la police). Je recommande le correctif moteur ; la scission de l'auteur reste juste et inoffensive.

Les résumés n'ont pas de tableau et rien n'y est coupé. Aucun `*`, `:::` ni `_` résiduel dans le rendu des 4 fichiers (vitest jetable, supprimé ; `git status` du moteur propre).

### 8.4 Gates

`content:check` ✓ (`french-6eme: 8 chapters, 40 exercises, 240 questions`) · `content:qa -- --subject french-6eme` ✓ aucune clé suspecte · `content:tranche … 01…,02… --fresh --strict-longest` ✓ : clé la plus longue 0/49, positions 20/33/22/24 %, paires proches 0, gabarits 0, patron de notion 0 en recul.

### 8.5 Verdict final

**Prêt après une dernière retouche** : rétablir les 4 explications de `short_answer` (8.2). Il ne reste ni critique ni majeur dans le contenu. F9 (mots coupés à 360 px) dépend du correctif moteur décrit en 8.3, pas de B1.
