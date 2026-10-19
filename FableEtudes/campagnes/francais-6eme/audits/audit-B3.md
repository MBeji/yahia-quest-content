# Audit B3 — french-6eme, `05-sauver-la-nature` et `06-etre-en-forme`

> Auditeur indépendant (opus), 2026-10-19. Branche `wip/francais-6eme-un-passage` (worktree `wt-fr6b`).
> Grilles appliquées : skill `content-audit`, la grille du français 9ᵉ (`prompt-francais-auditeur.md` → `gisement-auditeur.md`) et `course-quality.md`.
> Autorité : la fiche `programme/6eme-base/francais.md` (§ 2.5, § 2.6, § 2.10), le PLAN (F1–F7) et le PDF du cahier 121615, relu aux pages reprises (58, 65, 67, 70, 72, 79).
> Méthode : les 70 questions (quiz + 5 exercices × 2 chapitres) ont été re-résolues à l'aveugle, sans la clé. J'ai lu le rapport et les notes de l'auteur seulement après. Rien n'a été modifié dans `content/`, et je n'ai fait aucune écriture git.

## 0. Gates et rendu

| Contrôle | Résultat |
| --- | --- |
| `content:check` (global, `eng-deliver`) | ✓ `french-6eme: 8 chapters, 40 exercises, 240 questions`. Pas besoin de copie isolée : le chargement est complet. |
| `content:qa -- --subject french-6eme` | ✓ aucune clé suspecte |
| `content:tranche … --chapters 05…,06… --fresh --strict-longest` | ✓ clé strictement la plus longue : 0/54. Positions : a 31 % · b 26 % · c 24 % · d 19 %. ⚠ 4 paires proches et 6 groupes gabarit (voir § 5). Patron de notion : 0 en recul. |
| `renderLesson` / `renderSummary` (vitest jetable, environnement **jsdom** : sous `node`, `sanitizeSvg` refuse sans DOM et la planche sort vide) | ✓ 7 sections et 7 cartes par chapitre. La figure Tulmac est rendue (1 figure). |
| Chromium 360 px (CSS `.lesson-content` + `.lesson-table` du moteur) | ✓ pas de débordement de page. ⚠ **les tableaux de conjugaison à 5 colonnes se cassent au milieu des mots** : « pren/drai », « mettr/ai », « nou/s ». Voir m-1. La figure fait 294 × 147 px : lisible, mais voir M-9. |

Les fichiers jetables (test vitest, scripts de capture) ont été supprimés du moteur. Les captures restent dans le scratchpad de l'auditeur.

## 1. Synthèse

70 questions re-résolues. **Toutes les clés sont justes**, et aucune question n'a deux réponses défendables. J'ai une réserve sur `05/02-boss` q6 (voir m-9).

| Chapitre | Questions | Critiques | Majeurs | Mineurs |
| --- | --- | --- | --- | --- |
| 05-sauver-la-nature | 35 | 0 | 7 | 9 |
| 06-etre-en-forme | 35 | 0 | 7 | 8 |

Les deux plus gros défauts tiennent à des **diagnostics faux dans le cours et dans les explications** :
- « prit copie le présent » : le présent de *prendre* est *il prend* ;
- « je ferrai = conjugaison régulière » : la forme régulière serait *fairai*.

S'y ajoutent **cinq items qui recopient un exemple ou une vérification du cours**, **trois notions testées sans être enseignées** (*détériorer*, *résumer*, *gentille*) et **deux réponses de dialogue reconnaissables à leur forme**.

## 2. Re-résolution — tableau (✓ = ma réponse = la clé)

**05** — quiz q1 c ✓ · q2 b ✓ · q3 d ✓ · q4 a ✓ · q5 c ✓ | 01 q1 a ✓ · q2 c ✓ · q3 b ✓ · q4 d,a,b,c ✓ · q5 d ✓ · q6 a,b,c ✓ | 02 q1 a ✓ · q2 b ✓ · q3 d ✓ · q4 a ✓ · q5 « donnent » ✓ · q6 b ✓ (réserve m-9) | 03 q1 l1r1…l4r4 ✓ · q2 c ✓ · q3 d ✓ · q4 c ✓ · q5 « passe » ✓ · q6 « va » ✓ | 04 q1 b ✓ · q2 a ✓ · q3 c ✓ · q4 a,b,c ✓ · q5 d,a,b,c ✓ · q6 d ✓ | 05 q1 a ✓ · q2 b ✓ · q3 c ✓ · q4 d ✓ · q5 b ✓ · q6 a ✓.

**06** — quiz q1 b ✓ · q2 a ✓ · q3 c ✓ · q4 d ✓ · q5 a ✓ | 01 q1 b ✓ · q2 a ✓ · q3 c ✓ · q4 a ✓ · q5 c,a,d,b,e ✓ · q6 b ✓ | 02 q1 a ✓ · q2 c ✓ · q3 d ✓ · q4 b ✓ · q5 a ✓ · q6 d,a,b,c ✓ | 03 q1 a,b ✓ · q2 a ✓ · q3 c ✓ · q4 b ✓ · q5 a,b,c ✓ · q6 « est allée » ✓ | 04 q1 a ✓ · q2 c ✓ · q3 b ✓ (notion non enseignée, M-11) · q4 d ✓ · q5 c,d ✓ · q6 d,a,b,c ✓ | 05 q1 a ✓ · q2 l1r1…l4r4 ✓ · q3 d ✓ · q4 c ✓ · q5 b ✓ · q6 a ✓.

**Reprises du cahier (champ `manuel`)**, confrontées au PDF 121615 :
- 05 `03-revision` : p.58 ex.2 (Guy, 4 compléments et marge ✓) ; p.65 ex.1 (« Sébastien a fini ses devoirs et … ses leçons » ✓) ; p.67 ex.2 (« toutes les plantes est/sont ravies » ✓), ex.3 (voir m-6) et ex.4 (vol d'oiseaux, équipe ✓).
- 06 `03-revision` : p.70 ex.1 (Josette ✓) et ex.3 (« Au gymnase, les jeunes sportifs… » ✓) ; p.72 ex.2 (« Quand feras-tu… », « Tu n'as pas fait… » ✓) ; p.79 ex.2a (adjectifs ✓, deux phrases interverties, sans incidence).
- Pages et items justes. La question variante de chaque fichier ne porte pas le champ ✓.

**Bornes F1/F5** : aucune question ne cible les pronoms compléments, le gérondif, les relatives ou ne…rien/que. Aucun accord du participe avec *avoir* ✓. Le conditionnel apparaît seulement comme distracteur (`prendrais`, `ferais`, avec l'étiquette élargie par le pilote `fr.conj.futur-conditionnel-1re-personne`) et il est **nommé** dans deux explications. C'est admis par la carte, mais à surveiller.

## 3. Majeurs — chapitre 05

### M-1 — diagnostic faux : « prit copie le présent »
Le présent de *prendre* est *il prend*, sans t. *Prit* n'est pas calqué sur le présent : l'élève ajoute un *t* par analogie avec *fait, dit, écrit*. Pour *mettre* (*il met*), le diagnostic tient ; pour *prendre*, la leçon enseigne un fait faux. Le libellé du registre `fr.conj.participe-passe-mal-termine` dit la même chose (« en le calquant sur le présent (… il a prit …) ») : **signalé au pilote**, à reformuler.

Remplacements exacts :
- `cours.md` l.94 → `« Nous avons **prit** », « il a **mit** » ✗ On ajoute un _t_ final, comme dans _il a fait_ ou _il a dit_. ✓ Le participe de _prendre_ est **pris** et celui de _mettre_ est **mis** : ils se terminent par **-is**, jamais par _-it_.`
- `quiz.json` q2, explication : remplacer `Écrire « prit » copie la terminaison du présent, et` par `« Prit » ajoute un t qui n'existe pas dans ce participe, et`.
- `exercices/01-pratique.json` q2 : remplacer `« Prit » copie la terminaison du présent.` par `« Prit » ajoute un t qui n'existe pas dans ce participe.`
- `exercices/02-boss.json` q2 : remplacer `« apprit » copie le présent.` par `« apprit » ajoute un t qui n'existe pas dans ce participe.` (Si M-5 est appliqué, cette question est remplacée de toute façon.)

### M-2 — règle fausse dans la définition de l'accord sujet-verbe (`cours.md` l.128)
« on encadre le verbe dans _c'est… qui_ » est faux : c'est le **sujet** que *c'est… qui* encadre. De plus, la mise en relief est une notion de 9ᵉ (`fr.phrase.emphase-qui-que`).

Remplacement de la phrase : `Pour trouver le sujet, on pose la question **qui est-ce qui + verbe ?** : _Qui est-ce qui prépare ? Nicole._`

### M-3 — notion testée sans être enseignée : *détériorer* (`exercices/05-entrainement.json` q2)
Le mot vient du lexique du guide p.136, mais il n'est ni dans le cours 05 ni dans les cours antérieurs.
- Ajout dans `cours.md` l.234, en fin de puce : `- **recycler** : transformer un déchet pour en faire un autre objet ; **protéger** : mettre à l'abri du danger ; **détériorer** : abîmer, mettre en mauvais état ;`
- Pour la même q2 (mineur) : retirer l'étiquette `fr.lexique.contraire-pour-synonyme` de l'option d « respecter », qui n'est pas un contraire. Explication : `Détériorer veut dire abîmer, mettre en mauvais état. Réparer et protéger disent presque le contraire ; respecter veut dire autre chose : faire attention à quelqu'un ou à quelque chose.`

### M-4 — notion testée sans être enseignée : résumer (`exercices/04-defi.json` q1)
« Quelle phrase résume le mieux ce texte ? » n'est enseigné par aucun cours de 01 à 05 : `grep résum` ne trouve rien. Ajout d'une puce dans le `::: propriete` de la section « Raconter en insérant un passage descriptif » (après la puce « l'ordre des événements ») : `- **Résumer** un récit, c'est dire en une phrase ce qui se passe dans **toute** l'histoire (qui fait quoi), sans s'arrêter sur un détail.` Miroir dans `resume.md`, dernière carte, à la fin : ` ; résumer, c'est dire l'essentiel de toute l'histoire en une phrase.`

### M-5 — gabarit répété : le passé composé de *prendre*
Les questions `01-pratique` q2, `02-boss` q2 et `03-revision` q2, plus le quiz q2, suivent le même schéma : forme en -it / présent / futur / clé en -is. Les deux dernières questions emploient **le même verbe (*apprendre*)**. Remplacer `02-boss.json` q2 :
- prompt : `Complète : « La semaine dernière, le maire ___ aux enfants de planter des arbres. » (permettre)`
- options : a `a permit` (`fr.conj.participe-passe-mal-termine`) · b `a permis` (clé) · c `permettra` (`fr.temps.indicateur-de-temps-ignore`) · d `permet` (`fr.temps.indicateur-de-temps-ignore`). Longueurs 8/8/9/6 : la clé n'est pas la plus longue, et une seule forme est juste.
- explication : `« La semaine dernière » situe l'action dans le passé : passé composé, avec l'auxiliaire « avoir » au présent puis le participe. « Permettre » se conjugue comme « mettre » : le participe est « permis », en -is. « A permit » ajoute un t qui n'existe pas, « permettra » est le futur et « permet » le présent.`

### M-6 — doublon : `02-boss` q4 (« La classe entière va ») et `03-revision` q6 (« Mon équipe va »)
Les deux questions portent sur la même notion (nom collectif), avec le même verbe et la même réponse. Remplacer `02-boss.json` q4 :
- prompt : `Complète : « Toute la classe ___ fière de la plage propre. » (être, au présent)`
- options : a `est` (clé) · b `sont` (`fr.accord.nom-collectif-au-pluriel`) · c `es` (`fr.accord.verbe-non-accorde-au-sujet`) · d `êtes` (`fr.accord.verbe-non-accorde-au-sujet`). Longueurs 3/4/2/4.
- explication : `« Toute la classe » est un nom collectif au singulier, même s'il désigne plusieurs élèves : le verbe reste au singulier, à la 3e personne : est. « Sont » est le pluriel, qu'on emploie à tort parce qu'on pense aux élèves ; « es » et « êtes » sont les formes de « tu » et de « vous ».`

### M-7 — pièges du cours sans étiquette ou que rien ne porte (doute n° 3)
Quatre ids existent déjà au registre, avec un libellé qui nomme exactement l'erreur. Ils ne sont simplement pas dans la carte du module M5 : **c'est au pilote de les ajouter à `vocab-french-6eme.json` et à `map-vocab.md`** (M5). Aucun id neuf n'est nécessaire.

| Piège (cours 05) | Id existant | Distracteur qui le portera |
| --- | --- | --- |
| *pourtant* / *donc* (l.252) | `fr.logique.rapport-logique-confondu` (« … conséquence (donc), opposition (pourtant) … ») | `05-entrainement` q4 a « c'est pourquoi » (aujourd'hui sans étiquette) |
| liste de détails au lieu d'un portrait (l.301) | `fr.portrait.signalement` | aucun aujourd'hui → réécrire `05-entrainement` q6, ci-dessous |
| réponse non rédigée, « Parce que 100 litres » (l.201, piège que l'auteur n'a pas listé) | `fr.lecture.reponse-non-redigee` | `05-entrainement` q3 d « Parce que 100 litres. » (aujourd'hui sans étiquette) |
| répétition du nom (l.347) | aucun id exact | **pas d'id neuf** : la notion est celle du cours 01 (« Éviter les répétitions »). Transformer le piège en puce de `::: propriete` : `- On évite de répéter le même nom : on le remplace par un mot de remplacement (_elle_, _la fillette_, _mon amie_).` Supprimer le bloc `::: piege` des l.346-348. |

Ajouter les trois ids à `coursePitfalls` (05). Réécrire `05-entrainement.json` q6, dont les trois distracteurs « hors sujet » s'éliminent aussi à vue :
- prompt : `Tu termines le portrait de ton chien Rex par son caractère. Quelle phrase choisis-tu ?`
- options : a `Il est fidèle et m'attend chaque soir devant la porte.` (clé) · b `Il a une tête, une queue, des oreilles et quatre pattes.` (`fr.portrait.signalement`) · c `Rex est le chien de notre famille depuis deux ans.` (sans étiquette : c'est la présentation) · d `Il a le poil noir et une petite tache blanche au front.` (sans étiquette : c'est le physique). Longueurs 54/56/50/55. Une seule phrase dit le caractère.
- explication : `La dernière étape du portrait dit le comportement ou le caractère : « fidèle », « m'attend devant la porte ». La phrase sur la tête, la queue et les pattes fait seulement une liste ; les deux autres présentent Rex ou décrivent son physique, des étapes qui viennent avant.`
- q3 : passer l'étiquette de l'option a (« plus longue … plus agréable ») à `fr.lecture.deduction-sans-indice`. Le texte ne dit rien de la durée : ce n'est pas le contraire du texte.

## 4. Majeurs — chapitre 06

### M-8 — diagnostic faux : « je ferrai » (`cours.md` l.100)
*Ferrai* (double r) n'est pas une conjugaison régulière : la forme régulière serait *fairai*, et c'est ce qu'exécute l'étiquette `fr.conj.forme-irreguliere-regularisee`. Remplacement : `« Demain, **j'allerai** et **je fairai** » ✗ On conjugue ces deux verbes comme les verbes réguliers, à partir de l'infinitif. ✓ Ils changent de radical : _j'**ir**ai_, _je **fer**ai_.`
Pour la même section (mineur), le cas-limite l.107 est vide de sens. Remplacement : `- Cas-limite : au futur, on n'entend plus l'infinitif : _j'irai_ vient de _aller_, _je ferai_ vient de _faire_.`

### M-9 — figure Tulmac et `02-boss` q6 (doute n° 4)
**Rendu à 360 px** : lisible. En revanche, « 2. la clairière » mord sur le trait de l'ellipse et « 4. dedans » le déborde.
**Vérité de la figure** : « 3. dehors » et « 4. dedans » sont posés sous **deux cases différentes**, alors que le cours parle de l'extérieur puis de l'intérieur **des mêmes** cases. Rien ne montre un intérieur, et la route en pointillés (le premier élément du texte du cahier) n'est pas nommée.
**Désigne-t-elle une clé ?** Oui, indirectement. Son ordre 1-2-3-4 (forêt, clairière, dehors, dedans) est exactement la clé de `02-boss` q6, qui reprend aussi les trois phrases du `::: verifie` (l.327). Le boss devient une question de mémoire.

1. Remplacer le SVG du cours (vérifié en Chromium à 360 px, aucun texte ne déborde) :
```
<svg viewBox="0 0 240 140">
<rect x="4" y="4" width="232" height="132" rx="8" fill="#bbf7d0" stroke="#1f2937" stroke-width="2"/>
<text x="12" y="20" font-size="10" fill="#1f2937">1. la forêt</text>
<path d="M12 124 L88 84" fill="none" stroke="#1f2937" stroke-width="2" stroke-dasharray="4 3"/>
<text x="16" y="108" font-size="9" fill="#1f2937" transform="rotate(-28 16 108)">la route</text>
<ellipse cx="156" cy="80" rx="74" ry="48" fill="#fef9c3" stroke="#1f2937" stroke-width="2"/>
<text x="156" y="46" font-size="10" text-anchor="middle" fill="#1f2937">2. la clairière</text>
<rect x="104" y="62" width="18" height="16" fill="#fdba74" stroke="#1f2937" stroke-width="1.5"/>
<rect x="150" y="58" width="56" height="44" fill="#fdba74" stroke="#1f2937" stroke-width="2.5"/>
<rect x="156" y="64" width="44" height="32" fill="#fff7ed" stroke="#1f2937" stroke-width="1"/>
<path d="M160 74 Q178 90 196 74" fill="none" stroke="#1f2937" stroke-width="2"/>
<text x="166" y="114" font-size="9" text-anchor="middle" fill="#1f2937">3. dehors : les murs</text>
<text x="178" y="72" font-size="8" text-anchor="middle" fill="#1f2937">4. dedans</text>
</svg>
```
   Légende : `::: figure On décrit le village de Tulmac de loin à près : la forêt, la clairière, les murs d'une case, puis son intérieur (le hamac)`
2. Remplacer `02-boss.json` q6 (ordering) par un QCM sur un autre lieu. Cette question porte le piège « inventaire » (M-10) :
   - prompt : `Tu décris la bibliothèque de ton école. Quel passage suit un ordre, de loin à près ?`
   - options : a `La bibliothèque se trouve au fond de la cour. Sa porte est verte. À l'intérieur, des livres couvrent les murs.` (clé) · b `Il y a des livres. Il y a une porte. Il y a une cour.` (`fr.description.inventaire`) · c `À l'intérieur, des livres couvrent les murs. La bibliothèque se trouve au fond de la cour. Sa porte est verte.` (`fr.description.inventaire`) · d `Nous traversons la cour. Nous ouvrons la porte verte. Nous prenons un livre.` (`fr.texte.description-narration-confondues`). Longueurs 110/53/110/76 : la clé n'est pas strictement la plus longue.
   - explication : `On part de ce qui est loin (la cour, la porte) pour finir à l'intérieur. La liste en « il y a » ne suit aucun ordre, le passage qui commence par l'intérieur va de près à loin, et le dernier raconte des actions au lieu de décrire.`

### M-10 — pièges du cours sans étiquette (doute n° 3, suite)
| Piège (cours 06) | Id existant | Porteur |
| --- | --- | --- |
| ordre des parties de la lettre (l.254) | `fr.lettre.parties-mal-placees` (carte M7 ; à étendre à M6 : texte 18 et cahier p.78 ex.1) | `04-defi` q1 b « Tunis, le 5 mars. » et c « Je t'embrasse bien fort. » (aujourd'hui sans étiquette) |
| inventaire pour décrire un lieu (l.315) | `fr.description.inventaire`. Libellé à élargir (même id) : `Tu décris en inventaire, dans l'ordre où les objets viennent : une description suit un ordre (de loin à près, de l'extérieur à l'intérieur, premier plan → arrière-plan) et un regard.` | nouveau `02-boss` q6 (M-9) |
| « se porter comme un charme » (l.203) | `fr.lexique.sens-figure-lu-au-propre`, déjà sur la carte M6 et déjà porté par `01-pratique` q6 a | ajouter l'id à `coursePitfalls`. Le faux exemple du piège ne lit pas au propre. Remplacement : `« Se porter comme un charme, c'est porter un bijou porte-bonheur » ✗ On lit l'expression mot à mot, au sens propre. ✓ Une expression se comprend **en entier**, dans la phrase où elle est employée : ici elle veut dire « être en très bonne santé ».` |

### M-11 — notion testée sans être enseignée : *gentil → gentilles* (`exercices/04-defi.json` q3)
Le cours 06 enseigne trois règles : +e, -e inchangé, -eux → -euse. Le doublement de la consonne (*gentille*) relève du M7 (cahier p.93). Un élève qui applique la règle du cours choisit le distracteur d « gentiles ». Remplacer :
- prompt : `Complète : « Mes sœurs sont ___ et mes frères sont ___. » (curieux, joyeux)`
- options : a `curieux – joyeux` (`fr.accord.adjectif-non-accorde`) · b `curieuses – joyeux` (clé) · c `curieuses – joyeuses` (`fr.accord.adjectif-non-accorde`) · d `curieuxes – joyeux` (`fr.accord.feminin-adjectif-mal-forme`). Longueurs 16/18/20/18.
- explication : `« Sœurs » est féminin pluriel : curieux se termine par -eux, il devient curieuse, puis prend un s : curieuses. « Frères » est masculin pluriel : joyeux se termine déjà par x et ne change pas. « Curieux » oublie le féminin, « joyeuses » s'accorde avec le mauvais nom, « curieuxes » ajoute un e sans changer la terminaison.`

### M-12 — indice de forme : la réplique juste est la seule différente (`quiz` q5, `02-boss` q5)
Dans le quiz, la clé « Sami crie : « Au secours ! » » est la seule option sans « je glisse ». Au boss, la clé « Rania dit : « Regarde l'acrobate ! » » est la seule sans « bien … qui monte ». La clé se reconnaît à son contenu, sans lire la ponctuation.
- `quiz.json` q5 : a `Sami crie : « Au secours, je glisse ! »` (clé) · b `Sami crie : « au secours, je glisse ! »` (sans étiquette : c'est la majuscule) · c `Sami crie, « Au secours, je glisse ! »` (`fr.dialogue.ponctuation-oubliee`) · d `Sami crie : au secours, je glisse !` (`fr.dialogue.ponctuation-oubliee`). Longueurs 39/39/38/35, sans clé strictement la plus longue. Explication : `Pour écrire une parole, on ouvre avec deux-points et guillemets, puis la réplique commence par une majuscule et garde sa ponctuation avant le guillemet fermant. Il manque à chacune des trois autres versions la majuscule, les deux-points ou les guillemets.`
- `02-boss.json` q5 : a `Rania dit : « Regarde bien l'acrobate qui monte ! »` (clé) · b `Rania dit : « regarde bien l'acrobate qui monte ! »` (sans étiquette) · c `Rania dit, « Regarde bien l'acrobate qui monte ! »` (`fr.dialogue.ponctuation-oubliee`) · d `Rania dit : regarde bien l'acrobate qui monte !` (`fr.dialogue.ponctuation-oubliee`). Longueurs 51/51/50/47. Explication : même modèle que le quiz.

### M-13 — fuite par élimination entre `05-entrainement` q1 et q2 (doute n° 1)
Les trois distracteurs de q1 sont mot pour mot les définitions d'hygiène, de forme et d'entraînement que l'appariement q2 relie à leur mot. Si le donjon tire q2 avant q1, la clé « régime » sort par élimination. Remplacer q1 :
- prompt : `Lequel de ces sports est un sport collectif ?`
- options : a `le handball` (clé) · b `le cyclisme` · c `l'athlétisme` · d `la natation`. Les trois avec `fr.lexique.mot-voisin-du-meme-champ`. Longueurs 11/11/12/11.
- explication : `Un sport collectif se joue en équipe : le handball, comme le football ou le volley-ball. Le cyclisme, l'athlétisme et la natation se pratiquent seul : ce sont des sports individuels.`
- La notion « le régime » reste vérifiée dans le `::: verifie` du cours.

### M-14 — doublon de gabarit : `05-entrainement` q4 et `02-boss` q4
Mêmes verbes (*aller*, *faire*), même personne (*nous*), même futur, mêmes distracteurs (*allerons*, *fairons*). Remplacer `05-entrainement` q4 :
- prompt : `Quelle phrase est correcte ?`
- options : a `Hier, elles sont allées au stade ; demain, elles feront du vélo.` (clé) · b `Hier, elles ont allé au stade ; demain, elles feront du vélo.` (`fr.conj.auxiliaire-mal-choisi`) · c `Hier, elles sont allées au stade ; demain, elles fairont du vélo.` (`fr.conj.forme-irreguliere-regularisee`) · d `Hier, elles sont allé au stade ; demain, elles feront du vélo.` (`fr.accord.pp-etre-non-accorde`). Longueurs 64/61/65/62.
- explication : `« Hier » demande le passé composé : « aller » prend « être » et s'accorde avec « elles », féminin pluriel : elles sont allées. « Demain » demande le futur : « faire » devient fer- : elles feront. « Ont allé » se trompe d'auxiliaire, « fairont » conjugue « faire » comme un verbe régulier et « allé » oublie l'accord.`

## 5. Copies du cours et paires proches (doutes n° 1 et 2)

**Items qui recopient le cours** (majeur pour le boss et le défi, mineur pour le quiz et la pratique) : le quiz devient de la mémoire.

| Item | Copie de | Correctif |
| --- | --- | --- |
| 06 `02-boss` q1 | `::: verifie` l.164 mot pour mot | prompt `Complète : « La championne est ___ et ses frères sont ___. » (heureux, joyeux)`. Options et étiquettes inchangées : a `heureuse – joyeux` · b `heureux – joyeux` · c `heureuse – joyeuse` · d `heureuse – joyeuxs` (17/16/18/18). Explication : `« La championne » est féminin singulier : heureux devient heureuse. « Frères » est masculin pluriel : joyeux se termine déjà par x et ne change pas. « Heureux » oublie le féminin, « joyeuse » s'accorde avec « la championne » au lieu de « frères », et « joyeuxs » ajoute un s qui n'existe pas.` |
| 06 `04-defi` q6 | `::: exemple` du cirque (l.351-357) | options : a `La salle est grande, avec des tapis bleus et des cordes.` · b `Yassine monte à la corde et crie : « Je touche le plafond ! »` · c `Quand il redescend, toute la classe applaudit.` · d `Mercredi, Yassine va au gymnase avec sa classe.` Ordre d, a, b, c. Explication : `Le début présente le personnage, le moment et le lieu. Le passage descriptif montre la salle avant l'action. La réplique fait entendre Yassine pendant qu'il grimpe. La fin dit le résultat : la classe applaudit quand il redescend.` |
| 05 `04-defi` q5 | `::: exemple` de la plage (l.337-343), comme le quiz q5 | options : a `Les branches des arbres sont couvertes de sacs en plastique.` · b `Ils décrochent les sacs avec un long bâton.` · c `Le soir, le jardin public est propre et ils sont contents.` · d `Mercredi, Rami et ses cousins vont au jardin public.` Ordre d, a, b, c. Explication sur le modèle actuel. |
| 06 `02-boss` q6 | `::: verifie` l.327 + la figure | M-9 |
| 05 quiz q1, 05 `01-pratique` q4 (Pilou), 06 quiz q1 (« à Tunis »), 06 `01-pratique` q5 (lettre Sami/Walid) | `verifie` ou exemple du cours | mineur. Pour 06 `01-pratique` q5, voir aussi le gabarit commun avec 07 `04-defi` q3 ci-dessous. |

**Paires proches (Jaccard)** :
- 05 `04-defi` q1↔q2 et q1↔q3 (même texte, Léa et la tortue) : **voulues et sans fuite**. Chaque énoncé porte son texte, et aucune clé ni explication ne donne la clé d'une autre question : résumé, cause et inférence sont trois savoir-faire distincts.
- 06 `04-defi` q1↔q2 (même lettre) : **voulue, sans fuite**.
- 06 `05-entrainement` q1↔q2 (définitions) : **fuite par élimination** → M-13.

**Gabarits** :
- « Écris le verbe entre parenthèses au présent » ×4 : **acceptable**. Le cadre est celui du cahier p.67 ex.4, et chaque item vise un cas distinct : plusieurs sujets, nom + complément, nom collectif, participe avec *être*. Le vrai doublon de ce groupe est le M-6, qui est en QCM.
- 06 `01-pratique` q5 ↔ 07 `04-defi` q3 (« Remets dans l'ordre les parties d'une lettre à un ami », lot B4) : **doublon inter-chapitres** (Sami/Walid contre Sami/Lina, mêmes cinq parties). La lettre est le projet du M7. Au M6, je propose de transformer q5 en appariement partie ↔ rôle, sur le modèle du cahier p.78 ex.1, en variante sans champ `manuel` :
  - prompt : `Relie chaque partie de la lettre de Sami à son rôle.`
  - gauche : l1 `Sfax, le 3 avril` · l2 `Cher Walid,` · l3 `Écris-moi vite. Je t'embrasse.` · l4 `Sami`
  - droite : r1 `le lieu et la date` · r2 `la formule d'appel` · r3 `la formule de fin` · r4 `la signature`
  - paires : l1r1, l2r2, l3r3, l4r4. Explication : `Le lieu et la date ouvrent la lettre ; la formule d'appel nomme le destinataire ; la formule de fin dit au revoir avec affection ; la signature, tout en bas, dit qui écrit.`
- Les autres groupes (« complément de lieu / de temps / de manière » contre 07 et 08, « même sens que ») : cadres parallèles sur des notions différentes, acceptables.

## 6. Mineurs

- **m-1 (rendu, transversal)** — Le moteur applique `overflow-wrap: anywhere` à `.lesson-content` (styles.css l.647). Hérité par les cellules, il casse les tableaux de conjugaison à 5 colonnes au milieu des mots à 360 px (« pren/drai », « nous/ pren/dron/s »). Le même tableau existe dans les 6 premiers cours. Correctif de contenu, vérifié en Chromium : scinder en deux tableaux à 3 colonnes (`| Sujet | prendre | mettre |` au passé composé, puis au futur ; de même pour *aller*/*faire*). Ou bien, côté moteur : `overflow-wrap: normal` sur `.lesson-table td, th`. **À arbitrer par le pilote.**
- **m-2** — 05 `cours.md` l.185 : « au futur (_tu économiseras_) ». Dans le texte, *tu économiseras* est la conséquence, pas le conseil. Remplacer par `ou au **futur** (_tu fermeras le robinet_)`.
- **m-3** — 05 `cours.md` `::: verifie` l.264-268 : « La mer est sale ; … donc elle est propre à nouveau » se contredit. Remplacement : énoncé `Complète avec _pourtant_ ou _donc_ : « Les enfants ont ramassé tous les déchets de la plage, ______ elle est propre à nouveau. »` ; réponse `Le deuxième morceau est la **conséquence** du ramassage : on écrit **donc**. On écrit _pourtant_ quand l'idée s'oppose : _Les enfants ont ramassé les déchets ; pourtant, la plage reste sale._`
- **m-4** — 05 `resume.md` carte 3 : « Nom collectif : singulier (… _un vol d'oiseaux passe_) » range sous « nom collectif » un cas que le cours et la carte d'étiquettes classent « nom le plus proche ». Remplacer la fin par : `Nom collectif : singulier (_La famille est contente_) ; le verbe s'accorde avec le mot noyau, pas avec le mot voisin (_un vol d'oiseaux **passe**_).`
- **m-5** — 05 `03-revision` q3, explication : « « Est » s'accorde avec « la petite chèvre », le mot qui précède » est inexact, puisque le mot qui précède le verbe est *plantes*. Remplacer par : `« Est » irait avec un sujet singulier, comme « la petite chèvre » du début de la phrase, mais ce n'est pas le sujet de « ravies ».`
- **m-6** — 05 `03-revision` q4 reprend l'**exemple corrigé** du cadre du cahier (p.67 ex.3), pas un item. Prendre l'item 2 :
  - prompt : `Réunis en une seule phrase : « L'aigle a de grandes griffes. Le vautour aussi. »`
  - options : a `L'aigle et le vautour a de grandes griffes.` (`fr.accord.sujets-multiples-verbe-singulier`) · b `L'aigle et le vautour avons de grandes griffes.` (`fr.accord.verbe-non-accorde-au-sujet`) · c `L'aigle et le vautour ont de grandes griffes.` (clé) · d `L'aigle et le vautour as de grandes griffes.` (`fr.accord.verbe-non-accorde-au-sujet`). Longueurs 43/47/45/44.
  - explication : `Deux sujets reliés par « et » forment un sujet pluriel : le verbe avoir se met à la 3e personne du pluriel, ont. « A » n'accorde le verbe qu'avec un seul sujet ; « avons » et « as » sont les formes de « nous » et de « tu ».`
- **m-7** — Étiquettes :
  - 06 `04-defi` q2 a « Léa est malade… » → `fr.lecture.personnage-confondu` (l'action est attribuée à un autre personnage), au lieu de `contraire-du-texte`.
  - 06 `01-pratique` q2 d « sont allées » et `02-boss` q3 c « est allées » : le participe est accordé, mais avec le mauvais genre ou le mauvais nombre. `fr.accord.pp-etre-non-accorde` (« tu n'accordes pas ») n'est pas exact : à rendre muettes.
  - 06 `01-pratique` q4 d « mûree » (deux e) : `feminin-adjectif-mal-forme` est approximatif, la rendre muette.
  - 05 quiz q2 c « prendu » peut recevoir `fr.conj.forme-irreguliere-regularisee`.
- **m-8** — 06 `04-defi` q5 : « … près du ruisseau demain » n'est pas naturel. Prompt : `« Demain, dans la forêt, Tulmac marchera avec courage près du ruisseau. » Quels groupes sont des compléments de lieu ?` (options et clé inchangées).
- **m-9 (réserve sur une 2ᵉ réponse)** — Pour 05 `02-boss` q6 (« Le maire parle de la pollution aux habitants », clé « deux »), comme pour `01-pratique` q1 et l'exemple du cours (*Sarra a parlé…*), la clé suit le critère des **questions** (manuel p.76, Remarque ; cahier p.58 ex.2). Pourtant, le **test de suppression** que le cours donne aussi laisse « Le maire parle. » sensé. C'est l'ambiguïté même du manuel. Ajouter le cas-limite au `::: propriete` l.43 : `- Cas-limite : avec _parler_, _offrir_, _donner_, un groupe qui répond à _à qui ?_ ou _de quoi ?_ est essentiel même si la phrase semble tenir sans lui : c'est la question qui décide.`
- **m-10** — Étalonnage : 05 `04-defi` q6 (paraphrase littérale de « il continuera son combat ») et 06 `04-defi` q1 (« formule d'appel ») sont des d2 faciles, alors qu'ils sont étiquetés d3 dans un défi d4.
- **m-11** — 06 `cours.md` : les mots-outils du texte 18 (*près de, à proximité de, environ, presque*) sont absents, ce qui rend le cours un peu plus mince que le manuel. Ajout possible l.192 : `… ; pour dire une distance ou une quantité approchée : **près de**, **à proximité de**, **environ**, **presque**.`
- **m-12** — Le doute n° 5 (compléments de temps et de manière au 06) est **acceptable**. Ils ne sont ni nommés ni enseignés : ils n'apparaissent que comme groupes qui répondent à « quand ? » ou « comment ? », pour montrer ce qui n'est pas un lieu. Aucune question ne demande de les identifier. C'est conforme au § 2.10 (lieu/temps/manière sont ✅ dans l'année).

## 7. Axes du cours (une ligne par axe)

- **05** :
  - clarté : bonne, mais deux énoncés faux (M-1, M-2) ;
  - compréhension : les 7 sections ont les 7 temps dans l'ordre. Exemples, pièges et vérifications re-résolus, faux sauf M-1, M-2 et m-3 ;
  - exhaustivité : M-3 et M-4 ;
  - expérience : squelette complet, 7 cartes en miroir (m-4) ;
  - illustration : aucune notion spatiale, aucune figure requise.
- **06** :
  - clarté : bonne ;
  - compréhension : 7 temps présents. Exemples re-résolus justes, mais le piège « ferrai » a un diagnostic faux (M-8) et le faux exemple « charme » ne lit pas au propre (M-10) ;
  - exhaustivité : M-11, m-11 ;
  - expérience : complète ;
  - illustration : une figure, juste dans l'ordre mais fausse dans sa composition « dehors / dedans » (M-9).

## 8. Verdict

**À corriger.** Il n'y a aucune clé fausse et aucune double réponse ferme. Les points à traiter avant l'armement :
- les quatre énoncés faux du cours et des explications (M-1, M-2, M-8, et le faux exemple de M-10) ;
- trois notions non enseignées (M-3, M-4, M-11) ;
- deux indices de forme (M-12) ;
- deux doublons de gabarit (M-5, M-14) et un doublon de notion (M-6) ;
- une fuite par élimination (M-13) ;
- la figure (M-9) ;
- les copies du cours au boss et au défi (§ 5).

Côté pilote :
- ajouter à la carte M5/M6 cinq ids existants : `fr.logique.rapport-logique-confondu`, `fr.portrait.signalement`, `fr.lecture.reponse-non-redigee`, `fr.description.inventaire` (libellé élargi), et `fr.lettre.parties-mal-placees` étendu au M6 ;
- reformuler le libellé de `fr.conj.participe-passe-mal-termine` (« prit » n'est pas calqué sur le présent) ;
- trancher m-1 (tableaux à 5 colonnes, transversal) ;
- arbitrer le doublon « lettre » entre 06 et 07 (lot B4).

## 9. Re-vérification (2026-10-19, commit `edef30bf` comparé à `d6f3e076`)

**Méthode** : j'ai re-résolu à l'aveugle les **27 questions modifiées**, avant de lire leurs clés : 11 au 05 et 16 au 06, dont le nouveau 06 boss q6 (bibliothèque) et le nouvel appariement 06 01 q5 (lettre). J'ai ensuite relu le diff complet des cours, des résumés et des `chapter.json`, les libellés modifiés de `misconceptions.json` et la carte.

**Clés** : 27/27 conformes à mes réponses.
- 05 : quiz q2 b · 01 q2 c · 02 q2 b · 02 q4 a · 03 q3 d · 03 q4 c · 04 q5 d,a,b,c · 05 q2 b · q3 c · q4 d · q6 a.
- 06 : quiz q5 a · 01 q2 a · 01 q4 a · 01 q5 l1r1…l4r4 · 02 q1 a · q3 d · q5 a · q6 a · 04 q1 a · q2 c · q3 b · q5 c,d · q6 d,a,b,c · 05 q1 a · q4 a.
- Aucune double réponse et aucun indice de forme : `tranche` donne 0/55 clé strictement la plus longue.

**Gates** (sur `eng-deliver`, lien vers `wt-fr6b/content`) :
- `content:check` ✓ (french-6eme 240 questions) ;
- `content:qa` ✓ ;
- `content:tranche --fresh --strict-longest` (05, 06) : clé la plus longue 0 %, patron de notion 0 en recul ;
- 3 paires proches restantes : les défis sur un même texte ou une même lettre, voulus et sans fuite. La paire de définitions a disparu ;
- 5 groupes gabarit, tous jugés acceptables au § 5. Le groupe « parties d'une lettre » avec 07 a disparu.

**Rendu, Chromium 360 px** (jsdom, CSS du moteur) :
- 4 tableaux par cours, **0 mot coupé** (contrôle mot par mot des cellules), aucun défilement de page ;
- la conjugaison est scindée en tableaux à 3 colonnes. F9 est respecté ;
- la nouvelle figure Tulmac fait 294 px, aucun texte ne déborde de l'ellipse ni du cadre. « Dehors » et « dedans » sont sur la même case, la route est nommée, la légende dit quoi voir ;
- elle ne désigne plus aucune clé, puisque le boss q6 porte maintenant sur la bibliothèque.

| Défaut | État |
| --- | --- |
| M-1 « prit » / présent (cours + 3 explications + libellé du registre) | ✓ corrigé ; libellé reformulé (« par analogie avec un autre verbe ») |
| M-2 « c'est… qui » | ✓ |
| M-3 *détériorer* (cours + étiquette d + explication) | ✓ |
| M-4 résumer (cours + résumé) | ✓ |
| M-5 05 boss q2 (*permettre*) | ✓ |
| M-6 05 boss q4 (« Toute la classe est ») | ✓ |
| M-7 ids + 05 entr q3/q4/q6 + répétition devenue règle | ✓ (`coursePitfalls` 05 : 9 ids) |
| M-8 « fairai » + cas-limite | ✓ |
| M-9 figure + 06 boss q6 | ✓ |
| M-10 lettre, inventaire, « charme » | ✓ (`coursePitfalls` 06 : 9 ids) |
| M-11 *curieuses* | ✓ |
| M-12 indices de forme 06 quiz q5 / boss q5 | ✓ |
| M-13 fuite par élimination | ✓. **L'écart signalé n'en est pas un** : M-13 était classé dans les majeurs du **06** (le fichier `05-entrainement.json` du chapitre 06). L'auteur l'a appliqué au bon endroit. |
| M-14 06 entr q4 | ✓ |
| § 5 copies du cours (06 boss q1, 06 défi q6, 05 défi q5) + lettre en appariement | ✓ |
| m-1 tableaux | ✓ (F9) |
| m-2 à m-9, m-11 | ✓ |
| m-10 étalonnage | **non appliqué, accepté**. La rampe 2-2-3-3-3-3 du défi est honnête dans l'ensemble, et les deux items restent les plus faciles de leur étage. Ce mineur n'est pas bloquant. |
| m-12 | rien à faire (jugement) |

**Mineurs résiduels** (introduits ou laissés par les corrections ; non bloquants, textes exacts) :
- r-1 — 06 `04-defi` q5 : l'énoncé dit « marchera », l'explication dit encore « Tulmac marche où ? ». Remplacer par `On pose « où ? » : Tulmac marchera où ? Dans la forêt, près du ruisseau. « Avec courage » répond à « comment ? » et « demain » à « quand ? ».`
- r-2 — 05 `05-entrainement` q3 : l'option a est maintenant une déduction sans indice, mais l'explication parle encore de « deux phrases qui disent le contraire du texte ». Remplacer la fin par : `… ; la phrase inventée, celle qui dit le contraire du texte et le chiffre seul ne le font pas.`
- r-3 — 05 `04-defi` q5, explication : « présente le personnage » → `présente les personnages` (Rami et ses cousins).
- r-4 (carte, pilote) — `fr.portrait.signalement` est rangé au module **06** dans `vocab-french-6eme.json` et `map-vocab.md` (« Ajouts du pilote »). Or il est déclaré et porté au chapitre **05** (`coursePitfalls`, 05 entr q6), puisque le portrait est le canevas du M5 (guide p.141). Il faut l'ajouter au module 05.

**Verdict final : prêt.** Tous les critiques et majeurs sont corrigés, et aucune clé n'est fausse. Les quatre mineurs résiduels (r-1 à r-4) peuvent être corrigés au passage, sans nouvel audit.
