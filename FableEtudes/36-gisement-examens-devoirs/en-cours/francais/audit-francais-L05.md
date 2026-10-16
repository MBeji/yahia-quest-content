# Audit indépendant — lot L05, français 9ᵉ (gisement, étude 36)

Auditeur indépendant, 2026-10-16. Branche `wip/gisement-francais-9eme` (arbre `/home/user/wt-fr`, tête
`94009199`). Consigne suivie : `content-ingest/references/gisement-auditeur.md` (en entier), skills
`content-audit` puis `prof-francais-9eme`. Les fichiers `*-devoir-*` d'autres agents sont hors périmètre.

Périmètre : 5 missions, 50 questions, plus la ligne `sources[]` de 4 `chapter.json`.

| mission | fichier | q. |
| --- | --- | ---: |
| m023 | `03-voix-active-et-passive/exercices/06-examens-2007-2023-voix-active-et-passive.json` | 11 |
| m024 | `13-les-accords/exercices/06-examens-2007-2026-changer-le-sujet-et-accorder.json` | 8 |
| m025 | `13-les-accords/exercices/07-examens-2001-2015-tout-et-participe-passe.json` | 11 |
| m026 | `04-discours-direct-et-indirect/exercices/06-examens-2002-2025-production-recit-avec-dialogue.json` | 10 |
| m027 | `08-types-de-textes-et-production-ecrite/exercices/06-examens-2005-2026-production-reussite-et-portrait.json` | 10 |

Gates (moteur `/home/user/eng-svtses`, lien `content` → `wt-fr/content`) :

- `content:check` : vert (120 matières, 29 626 questions).
- `content:qa:strict` : 0 erreur ; aucun avertissement sur `french/` (les 506 avertissements sont hors lot).
- `content:tranche --subject french --chapters 03,04,08,13` :
  - clé strictement la plus longue : 0/162 ;
  - positions 25/25/27/24 % ;
  - les 3 paires proches et les 2 candidats gabarit sont tous hors lot (01, 03/01–04, 08 quiz).

Clé strictement la plus courte : m023 Q9, m025 Q6, m026 Q1, m027 Q6. Elles sont dispersées et liées à
la langue : ce n'est pas un indice de forme.

`sources[]` : la ligne R8 a été ajoutée aux 4 `chapter.json`. Elle est identique à celle des 9 autres
chapitres du gisement : OK.

Étiquettes :

- aucune sur un `multi`, un `ordering` ou un `matching` ;
- les 18 étiquettes `fr.*` employées existent toutes sur `origin/main:content/misconceptions.json` ;
- aucune famille nouvelle n'est proposée.

Aucune figure.

---

## m023 — `03/06` actif ↔ passif (d2, 11 q.)

| Q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 dévorer | a été dévorée | b | réserve | clé reconstituable au vote (M1) |
| 2 secourir | On a secouru | d | **défaut** | « La victime a secouru quelqu'un » nie la prémisse « le sujet sera on » ; vote |
| 3 dévisager | a été dévisagé … par | a | réserve | vote |
| 4 bouleverser | bouleverse | c | réserve | vote ; « a bouleversé » écarté par la règle du cours (temps conservé), pas par le sens |
| 5 expliquer | est mal expliquée | d | réserve | vote |
| 6 on cachait | était caché | a | réserve | vote (« était » ×2, seul « par on » isolé) |
| 7 encercler | était encerclé | b | réserve | vote ; l'énoncé montre « encerclé par » |
| 8 caresser | est doucement caressée | c | réserve | vote |
| 9 j'ai été ridiculisé | on m'a ridiculisé | d | réserve | vote ; option a à deux erreurs (pronom tonique ET place) mais étiquetée |
| 10 a lu | ont été lues | a | réserve | vote |
| 11 m'a enthousiasmé | J'ai été enthousiasmé | c | réserve | vote ; cadre faux (le narrateur est l'écrivain, Pierre le scientifique) |

Fidélité : les 11 phrases sont conformes aux transcriptions (2023 G a, b ; 2016 G ; 2015 G a, b ; 2011
G b ; 2010 G b ; 2008 a, c ; 2007 a, b). Le titre « 2007–2023 » est juste. Aucun doublon : aucune des
phrases ne se trouve dans `content/french/` hors de ce fichier. Les éléments de la liste « ne pas
redemander » sont tous respectés.

## m024 — `13/06` changer le sujet et accorder (d3, 8 q.)

| Q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 Léna → Sami | instituteur généreux … le | a | OK (mineur) | 2×2 propre ; le genre de Sami n'est dit que dans l'explication |
| 2 Angel → Nadia | heureuse … impatiente | b | OK (réserve) | 2×2 propre ; « impatientes » peu plausible |
| 3 émerveillé | émerveillés | b | **défaut** | redemande 11 quiz Q5 / 11/02 Q6 (liste) ; l'examen donnait l'adjectif déjà accordé |
| 4 un fameux boulanger | une fameuse boulangère | c | OK | 2×2 propre |
| 5 Salem et Selma | seuls … Ils | c | OK (mineur) | 2×2 propre ; recoupe 11 quiz Q5 (groupe mixte → masculin pluriel) |
| 6 Moi → les enfants | restaient … leurs | d | OK | 2×2 propre |
| 7 matching 2020 T | débordante / longues / unique | — | OK | unique par genre et nombre |
| 8 multi Sonia | a, c, e | — | OK (mineur) | paire miroir sérieux / sérieuse |

**Point signalé (m024 sans étiquette ; clé au vote ?).** J'ai vérifié chaque grille case par case.
Les Q1, Q2, Q4, Q5 et Q6 sont des plans 2×2 où chaque valeur de case apparaît exactement deux fois. Le
vote est nul partout. En Q3, les quatre formes se répartissent deux contre deux sur le e et sur le s.
**Aucune clé ne se trouve au vote.** Comme toutes les options sont muettes, l'option à deux erreurs
l'est aussi : conforme.

Fidélité :

- 2025 T, 2026 T (« il » minuscule, tel quel), 2023 T, 2018 T et 2007 b : conformes.
- 2020 T : l'examen demande de **choisir** parmi « longues, débordante, émerveillés, unique »,
  adjectifs déjà accordés. La Q7 le fait fidèlement. La Q3 le transforme en exercice d'accord.

## m025 — `13/07` « tout » et participe passé (d2, 11 q.)

| Q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 tout près | tout | b | OK (mineur) | citation : « tous » (2ᵉ blanc officiel) retiré sans marque ; « tout près » est l'exemple du cours |
| 2 Tous … Tous | Tous … Tous | d | OK | 2×2 propre |
| 3 tout inquiets / tout petit | tout … tout | a | **défaut** | explication : la voyelle invoquée pour un adjectif masculin |
| 4 tout le monde / Tous | tout … Tous | c | **défaut** | explication : « tout » de « tout le monde » appelé pronom ; majuscule au 1er blanc ; coupe sans marque |
| 5 toutes les / Tous ses | toutes … Tous | b | OK (mineur) | 2ᵉ phrase réécrite sans le dire |
| 6 applaudi / gardé | ont applaudi … ont gardé | a | OK | 2×2 propre |
| 7 les a rattrapés | les a rattrapés | d | **défaut** | clé reconstituable au vote ; « les est rattrapés » de remplissage |
| 8 tout émue / toute contente | tout … toute | a | OK (mineur) | « Elle est tout émue » est l'exemple du cours ; même contraste que 13/05 Q2 |
| 9 souffert / vécues | souffert … vécues | c | OK | 2×2 propre |
| 10 compati / engagée | compati … engagée | b | OK | 2×2 propre |
| 11 levé / intéressés | s'est levé … les a intéressés | c | OK (mineur) | « les a intéressés » = même fait que Q7 |

Fidélité : les données sont celles de 2015 G, 2012 G, 2003, 2006, 2013 G, 2001 et 2005. Le corrigé
officiel de 2005 donne « Il les a rattrapés ». Trois coupes ou réécritures ne sont pas marquées (m6).
Le titre « 2001–2015 » est juste.

## m026 — `04/06` production : récit avec dialogue (d3, 10 q.)

| Q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 plan 2025 G | récit + paroles + fin | a | OK (mineur) | « au fils » : le genre du narrateur n'est pas donné |
| 2 réplique du père | il faut aussi te former | c | OK | distracteurs indéfendables |
| 3 réplique du narrateur 2021 G | b | b | OK | |
| 4 argument 2015 G | des musiciens vivent de leur art | d | OK (mineur) | 2022 G cité mais non utilisé ; « un parent » (2022 : « tes parents ») |
| 5 verbe de l'objection | rétorqua | b | OK | |
| 6 incise 2002 | « Maman, dis-je, ce … » | a | OK | le vote départage a et d, il ne reconstruit pas la clé |
| 7 temps 2010 G | **b ou c** | c | **critique** | narration au passé composé (b) défendable ; non enseigné au 04 |
| 8 multi 2023 G | b, c, e | — | OK (mineur) | coupes de la consigne sans « […] » |
| 9 ordering 2013 G | d b e a c | — | OK (mineur) | ordre unique ; l'explication emploie « schéma narratif » (cours 08) |
| 10 ordering 2012 G | b d a e c **ou** b d c e a | — | **critique** | deux ordres défendables |

Fidélité : les consignes de 2025 G, 2021 G, 2015 G, 2009 G, 2002 ([…] marqué), 2010 G, 2013 G et 2012 G
sont conformes ; celle de 2023 G est coupée sans marque (m8). Le titre « 2002–2025 » est juste.

**Point signalé — production convertie en QCM : chaque distracteur est-il indéfendable ?** Oui pour
Q1–Q6 et Q8 : chaque distracteur omet une tâche, contredit la consigne, sort du sujet ou viole une
règle du cours 04. **Non pour Q7 et Q10** (C1, C2).

## m027 — `08/06` production : réussite et portrait (d3, 10 q.)

| Q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 tâche double 2026 G | a | a | OK | |
| 2 qualité montrée par l'action | c | c | OK (mineur) | même geste que 08/02 Q6 (action révélatrice face au signalement) |
| 3 sentiment 2018 G | b | b | OK | |
| 4 artisan au travail 2023 T | a | a | OK | |
| 5 plan 2024 T | d | d | OK (mineur) | l'explication (« comparer l'ami d'autrefois et celui d'aujourd'hui ») annonce Q7 |
| 6 changement d'attitude 2005 | c | c | OK | |
| 7 multi 2007 | b, d | — | OK | |
| 8 multi 2026 T | b, d, f | — | OK | |
| 9 ordering 2024 G | d b e a c **ou** d e b a c | — | **critique** | deux ordres défendables ; « travaillé aux travaux » |
| 10 matching 2024 T | Pendant / Quand / Deux ans plus tard / chaque dimanche | — | OK (mineur) | relative officielle coupée ; « intervalle » non enseigné |

Fidélité : les consignes de 2026 G, 2026 T, 2024 G (« A ta grande joie », tel quel), 2024 T, 2020 G,
2018 G, 2023 T, 2007 et 2005 ([…] marqué) sont conformes. Le titre « 2005–2026 » est juste.

**Point signalé — Q10, rôles des indicateurs de temps.** Les rôles ne sont pas dans l'énoncé : ils sont
dans l'**explication**. La question se résout par la syntaxe : « Pendant » se met devant un GN, « Quand »
devant une proposition, et « chaque dimanche » placé en tête de « …, nous sommes allés dans des lycées
différents » n'a pas de sens.

Trois des quatre rôles sont **déjà enseignés avant le 08** :

- cours `02-propositions-subordonnees`, § « Le complément circonstanciel de temps : six façons de dire
  « quand » » ;
- la définition y dit « situe une action à un **moment**, en indique la **durée** ou en marque la
  **répétition** » ;
- un `::: verifie` y porte sur « tous les matins » (répétition) ;
- guide CNP 521902, circonstancielles de temps, p. 17 et 19 (`programme/9eme-base/francais.md`, l. 421) ;
- le 08 ajoute « indicateurs de temps qui s'enchaînent : d'abord, puis, le lendemain, enfin ».

Seul le mot « intervalle » n'est enseigné nulle part. **Décision : ni ligne de cours, ni retrait.** Il
suffit de reformuler l'explication avec les mots du cours (m9).

**Point signalé — paragraphe 2024 T à la chronologie étrange.** La transcription (II.2) le donne tel quel :

- « Pendant les années collège, j'étais timide » ;
- « à dix-sept ans, j'ai rencontré Séverine » ;
- « deux ans plus tard, lycées différents ».

L'étrangeté est dans le sujet officiel, pas dans la mission : on garde les données. Seul écart : l2 a
perdu « qui est devenue mon amie », qui donne son référent au « nous » de l3 (m9).

---

## Défauts classés

Les textes de remplacement ci-dessous ont été vérifiés par script, avec trois contrôles :

- longueur : aucune clé ne devient strictement la plus longue ;
- vote : chaque case d'un 2×2 compte exactement deux options ;
- unicité de la réponse et absence de fuite vers une autre question.

« Muette » veut dire : sans `misconceptionTag`.

### Critiques (3)

**C1 — m026 Q7 (`04/06`), distracteur défendable et notion non enseignée au 04.**

Le défaut :

- « Raconte ce qui s'est passé » se rédige aussi bien au passé composé qu'au passé simple. Un récit à la
  première personne au passé composé et à l'imparfait est du français correct, et un correcteur
  l'accepte.
- L'option b est donc défendable.
- Le choix du temps de la narration n'est pas enseigné au 04. Le 04 enseigne seulement : « dans un
  dialogue, les temps sont ceux de celui qui parle, au moment où il parle ».

Correctif : fixer la narration dans l'énoncé et ne demander que les répliques.

Énoncé →
`(Examen 2010, générale) Consigne : « L'un de tes camarades de classe a un comportement bizarre et ne s'intéresse plus à ses études. Tu décides de l'aider. Raconte ce qui s'est passé en intégrant un dialogue dans ton récit. » Ton récit est écrit au passé simple et à l'imparfait. À quels temps écris-tu les répliques du dialogue ?`

Options :

| option | texte | long. | étiquette |
| --- | --- | ---: | --- |
| a | `Au passé simple et à l'imparfait, comme la narration qui les entoure.` | 69 | `fr.temps.recit-discours-melanges` |
| b | `Au plus-que-parfait et au conditionnel, comme dans le discours indirect.` | 72 | muette |
| c (clé) | `Au présent, au passé composé ou au futur, selon le moment où l'on parle.` | 72 | — |
| d | `Au passé simple seulement, car chaque réplique dit une action terminée.` | 71 | muette |

La clé n'est pas strictement la plus longue.

Explication →
`Le récit est au passé simple (actions) et à l'imparfait (décor, durée). Les répliques, elles, reproduisent ce que dit le personnage au moment où il parle : ses temps sont ceux de la conversation, présent, passé composé ou futur. Le passé simple appartient à la narration, pas à la parole ; le plus-que-parfait et le conditionnel viennent de la transposition au discours indirect, pas du dialogue.`

**C2 — m026 Q10 (`04/06`), deux ordres défendables.**

Le défaut : en plus de la clé b d a e c, l'ordre b d **c** e **a** se lit sans heurt.

- « Essaie une fois : je suis sûr qu'ils t'accueilleront » répond à « Les autres se moqueraient de ma
  jambe ».
- « Tu crois vraiment qu'ils m'accepteront ? » appelle ensuite « Viens jouer avec nous : je resterai
  près de toi ».

Correctif : la dernière réplique répond par « Oui » à la question de Nabil.

- Option c → `« Oui, j'en suis sûr : personne ne se moquera de toi », lui promis-je.`
- Avec cette réplique, l'ordre est unique :
  - le narrateur et Nabil alternent ;
  - b ouvre l'échange ;
  - d répond au « Pourquoi » ;
  - c, un « Oui », exige une question juste avant elle : il ne peut suivre que e ;
  - a tombe donc en 3ᵉ position.
- L'ordre (`answerKey`) est inchangé : b d a e c.

Explication →
`Les répliques alternent entre le narrateur et Nabil, et chacune répond à la précédente. Le narrateur ouvre avec sa question sur la solitude de Nabil ; Nabil y répond en disant sa crainte des moqueries ; le narrateur lui propose alors de jouer avec le groupe ; Nabil doute et pose une question ; le « Oui » du narrateur y répond et ferme l'échange.`

**C3 — m027 Q9 (`08/06`), deux ordres défendables.**

Le défaut : en plus de la clé d b e a c, l'ordre d **e b** a c se lit aussi.

- Le directeur peut parler devant le collège, puis on entre dans la salle.
- « Après son discours » reste possible deux phrases plus loin.

Le correctif ancre le discours sur l'estrade décrite en b, et corrige « travaillé aux travaux ».

Option e →
`Monté sur cette estrade, le directeur prit la parole et remercia tous ceux qui avaient participé aux travaux.`

L'ordre devient unique :

- e suit b, car « cette estrade » renvoie à b ;
- a suit e, à cause de « son discours » ;
- d ouvre le récit ;
- c le ferme.

L'ordre (`answerKey`) est inchangé : d b e a c.

Explication →
`Le récit suit le déroulement de la journée. Il s'ouvre sur l'arrivée devant le collège ; en entrant, le narrateur découvre la salle, de l'estrade jusqu'au fond ; « cette estrade » renvoie à celle qu'il vient de décrire : le discours du directeur vient donc ensuite ; « Après son discours » amène la rencontre avec l'élève douée ; la sortie de la salle ferme le récit.`

Dans l'énoncé, `A ta grande joie` → `À ta grande joie` (accent typographique).

### Majeurs (6)

**M1 — m023 (`03/06`), clé reconstituable au vote sur les 11 questions.**

Le défaut :

- Chaque distracteur ne change qu'un trait de la clé : le temps, l'accord, les rôles, « par on » ou
  « de / par ».
- Le vote trait par trait rend donc la clé partout. Aucune option n'a deux erreurs.
- C'est le défaut M6 de L04 (m020), ici sur toute la mission.

Correctif : sur chaque question, un plan 2×2 avec une option à deux erreurs, muette. Le temps fautif
est pris au plus-que-parfait quand c'est nécessaire, pour que la clé ne devienne pas la plus longue.

Vote recalculé : nul dans chaque case. Longueurs : aucune clé n'est strictement la plus longue. Q2 et
Q9 ont la clé la plus courte (24 contre 25 ; 29 contre 30), ce qui tient à la langue.

Les autres options et les clés ne changent pas.

- **Q1.** Remplacements :
  - c → `La remise avait été dévorée par les flammes.` (44, garde `fr.voix.temps-non-conserve`) ;
  - d → `La remise avait été dévoré par les flammes.` (43, muette).
  - Longueurs : clé 40 / 39 / 44 / 43.
  - Explication → `Le COD « la remise » devient sujet et le sujet « les flammes » devient complément d'agent. « Ont dévoré » est un passé composé : « être » se met au passé composé, « a été », et le participe s'accorde avec le nouveau sujet, féminin singulier : « dévorée ». « avait été » passe au plus-que-parfait ; « dévoré » oublie l'accord ; « avait été dévoré » cumule les deux erreurs.`
- **Q2.** Le défaut supplémentaire de cette question : l'option b, « La victime a secouru quelqu'un »,
  **nie la prémisse** de l'énoncé, qui dit que le sujet sera « on ». Elle s'élimine à vue.
  - Remplacements :
    - a → `On avait secouru la victime.` (28, garde `fr.voix.temps-non-conserve`) ;
    - b → `On avait secourue la victime.` (29, muette).
  - Longueurs : clé 24 / 28 / 29 / 25.
  - Explication → `« A été secourue » est un passé composé passif : le verbe actif reste au passé composé, « a secouru », avec « on » pour sujet. Le COD « la victime » est placé après le verbe : le participe, conjugué avec « avoir », reste invariable. « avait secouru » passe au plus-que-parfait ; « secourue » accorde le participe avec un COD placé après lui ; « avait secourue » cumule les deux erreurs.`
- **Q3.** Remplacements :
  - b → `Il avait été dévisagé avec surprise par les enfants.` (52, garde l'étiquette) ;
  - c → `Il avait été dévisagé avec surprise des enfants.` (48, muette ; l'étiquette `roles-inverses` est retirée).
  - Longueurs : clé 48 / 52 / 48 / 44.
  - Explication → `Le pronom COD « l' » (l'inconnu) devient le sujet « il », et « les enfants » passe en complément d'agent. « Ont dévisagé » est un passé composé : « a été dévisagé », au masculin singulier comme « il ». « avait été » passe au plus-que-parfait. « des enfants » est incorrect : « de » n'introduit le complément d'agent qu'après un verbe de sentiment ou d'attitude, et « dévisager » prend « par ».`
- **Q4.** Remplacement :
  - d → `La narratrice a bouleversé l'expérience de la guerre.` (53, muette).
  - Longueurs : clé 51 / 53 / 51 / 53.
  - Explication → `Le complément d'agent « par l'expérience de la guerre » devient sujet et le sujet « la narratrice » devient COD. « Est bouleversée » est un présent passif : le verbe actif reste au présent, « bouleverse ». « a bouleversé » passe au passé composé ; « La narratrice bouleverse l'expérience de la guerre » inverse les rôles ; la même phrase au passé composé cumule les deux erreurs.`
- **Q5.** Remplacement :
  - c → `La leçon a été mal expliqué par la maîtresse.` (45, muette).
  - Longueurs : clé 44 / 43 / 46 / 45.
  - Explication → `« La leçon » (COD) devient sujet, « la maîtresse » complément d'agent, et « explique » est au présent : « est expliquée », avec l'adverbe « mal » entre l'auxiliaire et le participe, accordé au féminin singulier. « expliqué » n'est pas accordé ; « a été » est un passé composé ; « a été mal expliqué » cumule les deux erreurs.`
- **Q6.** Remplacement :
  - d → `Laurent a été caché par on au moment du déclic de l'appareil photo.` (67, muette).
  - Longueurs : clé 60 / 67 / 60 / 67.
  - Explication → `Le sujet actif est « on » : la phrase passive n'a pas de complément d'agent. « Cachait » est à l'imparfait, donc « était caché ». « par on » est impossible ; « a été caché » est un passé composé ; « a été caché par on » cumule les deux erreurs.`
- **Q7.** Remplacement :
  - c → `Un mur qui s'était subitement dressé a été encerclé par lui.` (60, muette ; l'étiquette `temps-non-conserve` est retirée).
  - Longueurs : clé 59 / 59 / 60 / 60.
  - Énoncé → `(Examen 2016, générale) Un garçon, bouleversé en classe, perd connaissance. Mets à la forme passive, en gardant le temps : « Un mur qui s'était subitement dressé l'encerclait. » (« l' » désigne ce garçon.)`
    - L'ancien énoncé, « se retrouve encerclé par un obstacle », montrait la forme passive attendue.
    - Le nouveau cadre est celui du résumé de 2016 G.
  - Explication → `Le pronom COD « l' » devient le sujet « il » et le groupe « un mur… » devient complément d'agent. « Encerclait » est à l'imparfait : « était encerclé ». La relative « qui s'était subitement dressé » ne change pas. « a été encerclé » passe au passé composé ; les phrases où « un mur » reste sujet donnent l'action au garçon : elles inversent les rôles.`
- **Q8.** Remplacement :
  - b → `La surface des bassins était doucement caressés par les gouttes.` (64, muette).
  - Longueurs : clé 62 / 62 / 64 / 64.
  - Explication → `Le COD « la surface des bassins » devient sujet ; son noyau est « surface » : le participe s'accorde avec lui, au féminin singulier, et l'adverbe se glisse entre « est » et « caressée ». « caressés » s'accorde avec « bassins », qui n'est que le complément du nom ; « était » change le temps ; « était doucement caressés » cumule les deux erreurs.`
- **Q9.** L'option a actuelle, « on a ridiculisé moi », porte deux erreurs (pronom tonique ET place)
  sous l'étiquette `place-apres-verbe`.
  - Remplacement :
    - a → `À l'école, je me ridiculisais.` (30, muette).
  - Le 2×2 croise le temps (passé composé / imparfait) et le sujet (« on » / forme pronominale « je »).
  - Longueurs : clé 29 / 30 / 33 / 30.
  - Explication → `« J'ai été ridiculisé » est un passé composé passif sans agent : le sujet actif est « on », le temps reste un passé composé, et le sujet passif « je » devient COD, sous la forme du pronom « m' » placé devant l'auxiliaire. « on me ridiculisait » passe à l'imparfait ; « je me suis ridiculisé » est une forme pronominale, où le garçon est lui-même l'auteur de l'action ; « je me ridiculisais » cumule les deux erreurs.`
- **Q10.** Remplacements :
  - c → `Toutes mes œuvres avaient été lu par Pierre.` (44, muette) ;
  - d → `Toutes mes œuvres avaient été lues par Pierre.` (46, garde `fr.voix.temps-non-conserve`).
  - Longueurs : clé 42 / 40 / 44 / 46.
  - Explication → `Le COD « toutes mes œuvres » devient sujet, au féminin pluriel. « A lu » est un passé composé : « ont été » ; le participe s'accorde avec le sujet : « lues ». « lu » n'est pas accordé ; « avaient été » passe au plus-que-parfait ; « avaient été lu » cumule les deux erreurs.`
- **Q11.** Remplacement :
  - d → `Je suis enthousiasmée par le projet de Pierre.` (46, muette).
  - Longueurs : clé 46 / 45 / 47 / 46.
  - Énoncé → `(Examen 2007) Un conteur raconte la visite de Pierre, son ami d'enfance devenu informaticien : « Le projet de Pierre m'a enthousiasmé. » Passe cette phrase au passif.`
    - Dans le texte, c'est le narrateur qui est l'écrivain, le conteur.
    - Pierre est le scientifique.
    - L'ancien cadre, « parle d'un ami écrivain », était faux.
  - Explication → `Le pronom COD « m' » représente le conteur : il devient le sujet « je ». « A enthousiasmé » est un passé composé : « ai été », et le participe est au masculin singulier, comme le conteur. Le groupe « le projet de Pierre » devient complément d'agent. « suis enthousiasmé » est un présent ; « enthousiasmée » met un féminin alors que le conteur est un homme ; « suis enthousiasmée » cumule les deux erreurs.`

Bilan de M1 :

- les étiquettes `roles-inverses` (Q4 b, Q7 d) et `par-on` (Q6 b) restent ;
- l'étiquette `place-apres-verbe` sort de la mission ;
- les pièges « par on », « de / par » et « rôles inversés » demeurent.

**M2 — m024 Q3 (`13/06`), item déjà posé et item officiel altéré.**

Le défaut :

- « Accorde l'attribut » avec les 4 formes de l'adjectif est le geste de 11 quiz Q5 (« Sami et Lina sont
  (fier) ») et de 11/02 Q6. Ces deux items sont sur la liste « ne pas redemander ».
- L'examen 2020 T ne demandait pas d'accorder : les adjectifs y étaient donnés déjà accordés.

Correctif : **supprimer Q3**, et rendre l'item officiel entier à la Q7, en matching à 4 paires.

- Q7, ajouter :
  - l4 `Tous ceux qui l'ont vu, sont restés …` ;
  - r4 `émerveillés` ;
  - la paire `["l4","r4"]` dans `answerKey.pairs`.
- Q7, explication →
  `« Imagination » est féminin singulier : « débordante ». « Heures » est féminin pluriel : « longues ». « Tous ceux » est masculin pluriel : « émerveillés ». « Bateau » est masculin singulier : « unique », qui a la même forme au masculin et au féminin. « Longues » ne va qu'à un féminin pluriel, « débordante » qu'à un féminin singulier, « émerveillés » qu'à un masculin pluriel : il ne reste qu'un adjectif pour « bateau ».`
- L'appariement est unique :
  - « unique » est la seule forme possible pour « bateau » ;
  - « débordante » va donc à « imagination ».
- m024 passe à 7 questions (Q1–Q2 en d2, puis d3).

**M3 — m025 Q3 (`13/07`), explication fausse dans son motif.**

Le défaut :

- L'explication dit : « Devant « inquiets », qui commence par une voyelle, il reste invariable, même si
  le sujet est pluriel. »
- La voyelle ne joue que devant un adjectif **féminin**. Devant un masculin, « tout » adverbe est
  toujours invariable : « tout contents » aussi.
- Un élève en tirerait « tous contents ».

Explication →
`Dans les deux cas, « tout » signifie « tout à fait » et modifie un adjectif : c'est un adverbe. Devant un adjectif masculin, l'adverbe « tout » reste invariable, au singulier comme au pluriel : « tout inquiets », « tout petit ». « tous » et « toute » l'accordent à tort.`

La règle du féminin n'est pas reprise ici : elle donnerait la clé de Q8.

**M4 — m025 Q4 (`13/07`), explication fausse et majuscule fautive.**

Le défaut :

- Dans « tout le monde », « tout » est un **adjectif indéfini** qui détermine le nom « monde ». Ce
  n'est pas « le pronom tout ».
- Le 1ᵉʳ blanc est au milieu de la phrase (« surprend … le monde ») : la majuscule est fautive.
- La citation coupe « par son sérieux et son application » sans le marquer.

Correctifs :

- Énoncé → `(Examen 2003) Complète par « tout » accordé : « Au collège, l'enfant surprend … le monde par son sérieux et son application. Ses professeurs ne cessent de l'encourager. … sont satisfaits de ses résultats. »`
- Options (clé inchangée) :
  - a `tous … Tous` ;
  - b `tout … Tout` ;
  - c `tout … Tous` (clé) ;
  - d `tous … Tout`.
  - Longueurs 11 partout ; 2×2 inchangé.
- Explication → `Dans « tout le monde », « tout » est un adjectif indéfini devant le nom « monde », masculin singulier : « tout ». La phrase suivante commence par un pronom qui remplace « ses professeurs », masculin pluriel : « Tous sont satisfaits ». Les autres écritures mettent « tout le monde » au pluriel ou laissent « tout » invariable devant le verbe.`

**M5 — m025 Q7 (`13/07`), clé reconstituable au vote et option de remplissage.**

Le défaut :

- Le trait « avoir » se retrouve dans 3 options sur 4 et le pluriel masculin dans 2 sur 4 : le vote
  rend « rattrapés ».
- « Il les est rattrapés » est du remplissage.

Correctif :

- b → `Il les a rattrapée à la Prairie.` (32, muette).
- 2×2 genre × nombre : rattrapé / rattrapés / rattrapée / rattrapées.
- Longueurs : clé 32 / 31 / 32 / 33.
- Explication → `« Rattraper » se conjugue avec « avoir ». Le COD « les » est placé avant le verbe et représente des garçons, masculin pluriel : le participe s'accorde avec lui, « rattrapés ». « rattrapé » oublie l'accord ; « rattrapées » met un féminin ; « rattrapée » met un féminin et oublie le pluriel.`

**M6 — m023 Q2, option qui nie la prémisse.** Ce défaut est traité dans M1 Q2, mais il est compté à
part parce qu'il élimine une option à vue, même sans vote.

### Mineurs (11)

- **m1 — m024 Q1** : le genre de Sami n'est donné que dans l'explication.
  - Énoncé → `… en la commençant par « Sami », un prénom de garçon. Quelle réécriture est correcte ?`
  - Explication, début → `Sami est un homme : il faut changer tout ce qui désigne Léna.`
- **m2 — m024 Q2** : « impatientes » (pluriel) est peu plausible. Le remplacer par « impatient »
  rendrait la clé strictement la plus longue (88 contre 87 / 86 / 85) : **à garder**.
- **m3 — m024 Q5** : recoupe 11 quiz Q5 (groupe mixte → masculin pluriel). Le planificateur l'a
  assigné, et le pronom « Ils / Elles » et le verbe y ajoutent quelque chose : à garder.
- **m4 — m024 Q8** : la paire miroir « une femme sérieux / sérieuse » assure une bonne réponse sur
  deux. C'est inhérent à une réécriture de paragraphe : toléré.
- **m5 — m025, recoupements internes et avec le publié** :
  - Q1 (« tout près ») et Q8 (« tout émue ») sont des exemples du cours 13 ;
  - Q8 reprend le contraste de 13/05 Q2 (consonne / voyelle devant un féminin) et de 13 quiz Q2 ;
  - le pronom « Tous » revient en Q2 et Q4, le déterminant « Tous » en Q2 et Q5 ;
  - « les a + participe masculin pluriel » revient en Q7 et Q11.
  - Tous ces items ont été assignés par la consigne de tri. À garder, mais si la mission doit perdre
    une question, ce sera Q11 (seconde moitié).
- **m6 — m025, citations** :
  - Q1 : le blanc « tous » est supprimé sans marque.
    → `« Quand l'inconnu commença à jouer … près des arbres, […] les oiseaux s'arrêtèrent de faire du bruit. »`
  - Q5 : la 2ᵉ phrase est réécrite. Ajouter `(phrase adaptée du sujet)` après la citation.
  - Q4 : voir M4.
- **m7 — m026 Q1, option a** : « au père et au fils », alors que le genre du narrateur n'est pas donné.
  - a → `Un récit qui pose la situation, fait parler ton père et toi, puis conclut.` (74 ; la clé
    reste la plus courte, comme avant).
  - Explication : « des répliques du fils et du père » → `des répliques de toi et de ton père`.
- **m8 — m026, citations et cadre** :
  - Q4 : « un parent s'y oppose ». En 2022, ce sont « tes parents ».
    → `Dans ces deux sujets, un adolescent veut exercer un métier artistique et ses parents s'y opposent.`
  - Q8 : la consigne 2023 G est coupée sans marque.
    → `« Ta sœur […] vient d'accomplir un exploit […]. Lors d'une discussion en famille, elle tient à s'attribuer, à elle seule, tout le mérite de cet exploit. Toi, tu insistes sur l'importance de la contribution des autres (parents, enseignants, entraîneur, ami(e), etc.) […]. »`
  - Q9 : l'explication emploie « schéma narratif » et « élément modificateur », notions du cours 08,
    dans une mission du 04.
    → `Le récit suit l'ordre des faits. Il s'ouvre sur la situation de départ : Karim, fatigué et distrait ; « Un matin » introduit l'événement qui change tout, la maladie du père ; « alors » ouvre la proposition d'aide, qui est le moment du dialogue ; il en découle la solution : Karim peut travailler le soir sans abandonner ses études ; « Aujourd'hui » donne la situation finale.`
- **m9 — m027 Q10** :
  - l2 a perdu la relative officielle.
    → `… j'ai eu dix-sept ans, j'ai rencontré Séverine qui est devenue mon amie.`
  - Explication, avec les mots du cours 02 →
    `« Pendant » se place devant un groupe nominal et dit la durée : toutes les années du collège. « Quand » introduit une proposition, avec son verbe conjugué, et situe le moment : dix-sept ans. « Deux ans plus tard » situe un moment par rapport au fait précédent. « Chaque dimanche » dit la répétition, en fin de phrase, après le verbe.`
- **m10 — m027, recoupements** :
  - Q2 = geste de 08/02 Q6 (action révélatrice face au signalement), avec en plus le contraste
    « nommer / montrer » ;
  - Q4 combine les indices de 08 quiz Q3 et 08/01 Q4 ;
  - l'explication de Q5 annonce le principe de Q7 (opposer autrefois et maintenant).
  - Ces items ont été assignés et apportent quelque chose : à garder.
- **m11 — Étages et notions, m026 et m027** :
  - la plupart des questions annoncées d2 dans ces boss d3 sont de vrais d2 (une tâche à repérer) ;
    l'étage d3 tient par Q6–Q10 ;
  - m026 Q3, Q4 et Q8 emploient la notion d'argument, enseignée au 09 (après le 04). Elles restent
    résolubles par la lecture de la consigne, et ce choix est assumé par PLAN.md R5.
  - Rien à corriger.

---

## Points signalés par l'auteur — tranchés

1. **m027 Q10, rôles des indicateurs.**
   - Les rôles ne sont pas dans les énoncés, ils sont dans l'explication.
   - Moment, durée et répétition sont enseignés au cours 02, § « Le complément circonstanciel de
     temps » (définition, et `::: verifie` « tous les matins »).
   - Source : guide CNP 521902, p. 17 et 19 (circonstancielles de temps).
   - Le 08 enseigne aussi l'enchaînement des indicateurs de temps dans un récit.
   - **Ni ligne de cours, ni retrait.** Seul « intervalle » est à reformuler (m9).
2. **Productions converties en QCM.**
   - Q1–Q6 et Q8 de m026, et Q1–Q8 de m027 : distracteurs indéfendables (tâche omise, consigne
     contredite, hors sujet, signalement, décor).
   - Trois items ont **deux réponses défendables** : m026 Q7 (narration au passé composé), m026 Q10
     et m027 Q9 (deux ordres). Ce sont les critiques C1–C3.
3. **m024 sans étiquette, et clé au vote.**
   - m024 : les plans 2×2 sont propres, le vote est nul partout, aucune clé n'est au vote.
   - Le vote touche en revanche **m023 en entier** (M1) et **m025 Q7** (M5), qui n'étaient pas signalés.
4. **Paragraphe 2024 T.** La chronologie est celle du sujet officiel (II.2). Les données sont fidèles,
   sauf la relative « qui est devenue mon amie », coupée (m9).
5. **Fidélité aux transcriptions.**
   - Toutes les données sont conformes.
   - Coupes ou réécritures non marquées : m025 Q1, Q4 et Q5 ; m026 Q8 ; m027 Q10 l2.
   - Cadres faux : m023 Q7 (forme passive montrée) et Q11 (rôles des personnages).
6. **Étiquettes.**
   - Aucune sur `multi`, `ordering` ou `matching`.
   - Les 18 étiquettes employées existent sur `origin/main`.
   - Une seule étiquette porte sur une option à deux erreurs : m023 Q9 a, retirée par M1.
   - Aucune famille nouvelle.

Défauts des lots précédents recherchés :

- **Question qui donne la clé d'une autre** : seulement l'explication de m027 Q5 vers Q7 (m10). Mon
  correctif M3 évite d'en créer une (Q3 → Q8).
- **Consigne qui fixe la réponse** : m023 Q7 (« encerclé par »), corrigé en M1.
- **« Dans le même texte »** : aucun cas.
- **Option désignée par sa lettre ou son rang** : aucun cas.
- **Distracteur lui aussi juste** : m026 Q7 (C1).

## Résumé

- **Questions auditées :** 50, toutes re-résolues à l'aveugle. Plus les 4 lignes `sources[]`.
- **Clés fausses :** 0.
- **Critiques :** 3. Deux réponses défendables dans m026 Q7, m026 Q10 et m027 Q9.
- **Majeurs :** 6.
  - m023 : vote sur les 11 questions et Q2 qui nie sa prémisse ;
  - m024 Q3 : déjà posée, à supprimer et à fondre dans la Q7 ;
  - m025 Q3 et Q4 : explications fausses ;
  - m025 Q7 : vote.
- **Mineurs :** 11. Citations coupées, cadres, recoupements assignés par la consigne, étages.
- **Étiquettes :** conformes. La seule sur deux erreurs (m023 Q9 a) disparaît avec M1.
- **Doublons :** m024 Q3 avec 11 quiz Q5 et 11/02 Q6. Les autres recoupements sont mineurs et assignés
  par la consigne.
- **Gates :** `check` vert, `qa:strict` 0 erreur (rien sur `french/`), `tranche` 0/162 clé la plus
  longue.
- **Verdict : à corriger avant fusion** (fix-first). Après correctifs :
  - m024 passe de 8 à 7 questions ;
  - les autres effectifs ne changent pas ;
  - les textes de remplacement sont vérifiés (longueur, vote, unicité, fuites).
