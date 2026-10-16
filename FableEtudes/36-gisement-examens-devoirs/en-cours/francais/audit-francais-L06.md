# Audit indépendant — lot L06, français 9ᵉ (gisement, étude 36 — devoirs en salle blanche)

Auditeur indépendant, 2026-10-16. Arbre `/home/user/wt-fr`, branche `wip/gisement-francais-9eme`.

Consignes suivies :
- `content-ingest/references/gisement-auditeur.md` ;
- skill `content-audit` ;
- grille `prompt-francais-auditeur.md`, appliquée à des missions de devoir.

Sur demande expresse de l'orchestrateur, j'ai lu :
- les cartes `assign-francais-devoirs.md` ;
- les notes d'auteur `auteurs-notes/fr-L06/NOTES.md` ;
- les instantanés `/tmp/claude-0/devoirs-snapshots/french/D0*.txt`, pour le contrôle de salle blanche.

Rien n'a été écrit dans `content/` ni dans git.

Périmètre : 6 missions, 40 questions.

| mission | fichier | étage | q. |
| --- | --- | --- | ---: |
| 02/10 | `02-propositions-subordonnees/exercices/10-devoir-subordonnee-de-temps-et-rapport-temporel.json` | d3 boss | 7 |
| 02/11 | `02-propositions-subordonnees/exercices/11-devoir-but-crainte-fausse-cause-correlation.json` | d2 | 6 |
| 06/09 | `06-concordance-des-temps/exercices/09-devoir-simultaneite-anteriorite-et-valeur-du-conditionnel.json` | d2 | 8 |
| 03/07 | `03-voix-active-et-passive/exercices/07-devoir-passif-quand-c-est-possible.json` | d2 | 6 |
| 15/06 | `15-article-de-presse-et-lettre/exercices/06-devoir-lettre-argumentative-et-article-sur-un-exploit.json` | d3 boss | 7 |
| 11/07 | `11-groupe-nominal-et-attribut/exercices/07-devoir-une-expansion-trois-formes.json` | d2 | 6 |

## Gates (lecture seule, moteur `/home/user/eng-svtses`, lien `content` → `wt-fr/content`)

- `content:check` : vert (120 matières, 29 626 questions, 1 067 étiquettes).
- `content:qa:strict` : 0 erreur, et aucun avertissement sur les 6 fichiers. Les 506 avertissements sont tous hors lot.
- `content:tranche --subject french --chapters 02,03,06,11,15` :
  - clé strictement la plus longue : 2/260, aucune dans le lot ;
  - positions des clés : 26/25/25/25 % ;
  - 6 paires proches, **aucune n'implique un fichier `NN-devoir-*`** : les paires retouchées ont disparu ;
  - les 5 groupes « gabarit » signalés ne touchent aucun fichier du lot. Les doublons de gabarit trouvés ci-dessous l'ont été à la main : l'outil ne les voit pas, parce que les énoncés diffèrent.
- `content:gisement:controle --sources …/devoirs-snapshots/french <6 fichiers>` : 40 textes contrôlés, 0 plage de 8 mots ou plus, 0 plage de 6 mots ou plus, 0 exercice source dont on reprenne 2 ou 3 données. ✓
- **Contrôle manuel de salle blanche**, sur les mots-clés de chaque mission comparés aux 8 instantanés (`grep`). Trois rapprochements que l'outil ne voit pas :
  1. **06/09 Q5**, transposition probable. D02 : « Quand il (ouvrir) les yeux, le train (arriver) déjà… » (imparfait ou plus-que-parfait). La mission : « Quand Karim arriva à la gare, le train ___ (partir)… ». Même objet, même cadre, même temps visé.
  2. **06/09 Q6 l1**. D06 : « Pourriez-vous me graver ce CD ? », dans l'exercice même de la carte (valeurs du conditionnel). La mission : « Pourriez-vous baisser la musique, s'il vous plaît ? ». Même tournure, même univers musical.
  3. **15/06 Q4–Q5**. « Kasserine » est l'en-tête de D07 et D08 (« Collège pilote Ibn Rochd Kasserine »). Un exploit sportif est aussi le sujet d'essai de D04 et D07, mais c'est le thème de la carte : on le garde.

  Les autres missions (02/10, 03/07, 11/07, la lettre de 15/06) n'ont aucun personnage, lieu, objet ni phrase commun avec les sources.

---

## 02/10 — subordonnée de temps et rapport temporel (d3, 7 q.)

| Q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 matching | jusqu'à ce que → antériorité ; pendant que → simultanéité ; aussitôt que → postériorité | idem | OK | rapport lu depuis la principale, comme le cours |
| 2 ordering | feu → dîner → lune | c b a | OK | ordre unique |
| 3 dès le lever | « Dès que le jour se lève » | c | OK | |
| 4 avant que + parte | parte | b | **défaut** | gabarit de 02/01 Q5, sur la liste « ne pas redemander » |
| 5 après l'arrivée | « Après que le car est arrivé » | d | OK | c « soit arrivé » muet : voir étiquettes |
| 6 avant de servir | « Avant qu'il serve » | b | OK | grille 2×2 propre (avant/après × subj./ind.), a à deux erreurs et muet |
| 7 avant que, quelle affirmation | brouillard d'abord, la principale précède | c | OK (réserve) | les explications de Q1 et Q2 donnent la règle (voir m4) |

## 02/11 — but, crainte, fausse cause, corrélation (d2, 6 q.)

| Q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 multi | a, c (de crainte que, de peur que) | a, c | OK | |
| 2 ___ le chien l'éclabousse | de peur que | a | OK (mineur) | redit Q1 (m3) |
| 3 pour le repos du bébé | dorme | c | **défaut** | seul le mode varie : gabarit de 02/02 Q5 et de 02/06 Q8, sur la liste |
| 4 Lina, cadeau | de peur que + voie | b | **défaut** | « de leur mère » est ajouté aux deux seules options « pour que » : marqueur |
| 5 sous prétexte que | indicatif | d | OK (mineur) | reprend l'exemple du cours (réveil) |
| 6 corrélation | Plus on monte, plus l'air est frais | a | OK (mineur) | la liste du rappel omet « moins… plus… », la forme de d |

## 06/09 — simultanéité, antériorité, valeur du conditionnel (d2, 8 q.)

| Q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 pendant que | fait | b | OK | d « fasse » muet : étiquette existante possible |
| 2 avant que vienne | vienne | c | **défaut** | même gabarit que 02/10 Q4 et 02/01 Q5 ; Q3 = Q1 + Q2 |
| 3 prend ; pleuve | d | d | OK | grille 2×2 propre |
| 4 avant que sache | sache | a | OK | |
| 5 le train … depuis dix minutes | était parti | c | **défaut** | salle blanche (D02) ; « venait de partir » mal étiqueté ; l'explication cite « partit », qui n'est pas une option |
| 6 matching | demande adoucie / condition / futur du passé | idem | **défaut** | salle blanche (D06, « Pourriez-vous ») ; les trois valeurs sont celles de 05 quiz Q5, 05/02 Q3 et 05/04 Q3 |
| 7 comprit ; avait mangé | d | d | **défaut** | clone de 06/02 Q1 (liste) ; a, qui porte deux erreurs, est étiqueté |
| 8 Vous auriez dû | reproche adouci | c | OK | valeur enseignée au ch. 05 (« un ordre, une demande ou un reproche atténués ») |

## 03/07 — passif quand c'est possible (d2, 6 q.)

| Q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 laquelle peut | la fresque | a | **défaut** | miroir de 03 quiz Q3 et de 03/04 Q3, posé seul (liste) ; son explication livre aussi Q3 a |
| 2 multi | a, d | a, d | OK | |
| 3 transformation correcte | les maçons / le mur | b | OK | mais livre Q6 (« téléphoner à ») |
| 4 gardiennes / visiteurs | c | c | **défaut** | le vote case par case reconstruit la clé ; b porte deux erreurs et une étiquette |
| 5 avaient détruit | d | d | **défaut** | « violents », présent dans la seule option a, l'élimine à vue |
| 6 téléphonées | pas de COD | a | **défaut** | fuite depuis Q3 c : même verbe, même erreur |

## 15/06 — lettre argumentative et article sur un exploit (d3, 7 q.)

| Q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 thèse | « Je suis persuadée… » | b | OK (mineur) | gabarit de 09 quiz Q7 |
| 2 argument | « on y apprend à monter de vrais robots » | c | OK | mais livré par Q7 d |
| 3 exemple | jeudi dernier, quatre élèves… | a | OK | |
| 4 titre | Rim Chatti, 17 ans, au sommet… | d | **défaut** | « en peu de mots » et clé strictement la plus courte ; lieu (Kasserine) |
| 5 chapeau | a | a | **défaut** | l'explication désigne une option par son rang (« le dernier ») ; même lieu |
| 6 brouillon | raconte au lieu de défendre | b | OK (mineur) | a est démenti par l'énoncé (phrases visiblement courtes) |
| 7 ordering | c d e b a | idem | **défaut** | d recopie la clé de Q2 ; ordre unique : OK |

Aucune préparation n'exige de rédiger (contrôle ch. 15) ✓.

## 11/07 — une expansion, trois formes (d2, 6 q.)

| Q | ma réponse | clé | verdict | motif |
| --- | --- | --- | --- | --- |
| 1 de laine | GP / complément du nom | d | OK | rappel nature/fonction légitime, mais voir Q2 |
| 2 que sa fille a tricoté | relative / complète manteau | a | **défaut** | emploie nature/fonction sans définition, alors que le cours ne les définit pas (autonomie) |
| 3 matching | CdN / relative / épithète | idem | OK | |
| 4 pommes juteuses | juteuses | d | **défaut** | clone de 11/06 Q8 (couleurs brillantes), sur la liste |
| 5 geste coléreux | de colère | b | OK (mineur) | distracteurs faibles ; clé la plus courte |
| 6 assiette à soupe | à soupe | a | OK (mineur) | clé la plus courte pour la 2ᵉ fois ; transpose l'exemple du cours (tasse à café) |

---

## Défauts classés

### Critique : 0

Aucune clé fausse, aucun distracteur défendable. Les 40 questions ont été re-résolues à l'aveugle ; les `multi`, `matching` et `ordering` ont été vérifiés énoncé par énoncé ou paire par paire.

### Majeurs (17)

**M1 — 02/10 Q4, « ne pas redemander » violé.** La question (« Avant que le car ___ » : part / parte / partira / partirait) reprend le gabarit de 02/01 Q5 (« jusqu'à ce qu'il ___ jour » : fait / fasse / fera / ferait) : même rapport, même grille de quatre modes. La règle « avant que + subjonctif » est déjà travaillée en Q6 (transformation, grille 2×2).
Correctif : **supprimer Q4**. La mission passe à 6 questions (rampe 2-2-2-3-3-3 conservée).

**M2 — 02/11 Q3, doublon de gabarit (liste).** Seul le mode varie (dort / dormirait / dorme / dormira) : c'est 02/02 Q5 (« de peur qu'on ne l'___ ») et 02/06 Q8 (« pour que … reconnaisse »). Remplacement (d2), qui porte sur le *ne* explétif enseigné dans le cas-limite du cours (§ but) :
- Énoncé : `Tarek ferme la fenêtre : il ne veut pas que la pluie entre dans la chambre. Quelle phrase garde ce sens ?`
- Options :
  - a (clé, 52) `Tarek ferme la fenêtre de peur que la pluie n'entre.`
  - b (56, muette) `Tarek ferme la fenêtre de peur que la pluie n'entre pas.`
  - c (47, `fr.logique.rapport-logique-confondu`) `Tarek ferme la fenêtre pour que la pluie entre.`
  - d (52, `fr.mode.subjonctif-oublie`) `Tarek ferme la fenêtre de peur que la pluie entrera.`
- Explication : `Tarek veut éviter que la pluie entre : c'est une crainte, exprimée par « de peur que » suivi du subjonctif. Le « ne » placé devant le verbe est explétif : il ne nie rien. Ajouter « pas » renverserait le sens, comme si Tarek craignait que la pluie n'entre pas. « Pour que » ferait de l'entrée de la pluie un but recherché, et le futur « entrera » ne suit pas « de peur que ».`
- Vérifications : la clé n'est ni la plus longue ni la plus courte. Une seule réponse juste : « pour que la pluie n'entre pas » serait juste, d'où son absence. Aucune fuite vers Q1, Q2 ou Q4.

**M3 — 02/11 Q4, marqueur dans les distracteurs.** Les deux options « pour que » (a, c) ajoutent « de leur mère », absent de l'énoncé : un élève les écarte sans rien savoir.
Correctif :
- a → `Lina cache le cadeau pour que son frère le voit avant l'anniversaire.` (69, muette) ;
- c → `Lina cache le cadeau pour que son frère le voie avant l'anniversaire.` (69, étiquette gardée).

La clé b (72) est ex æquo avec d (72) : elle n'est pas strictement la plus longue. Le vote reste nul (2 × de peur que / 2 × pour que ; 2 × voie / 2 × voit).

**M4 — 06/09 Q2, doublon.**
- « avant que + vienne », avec la grille vient / viendrait / vienne / viendra, est le gabarit de 02/10 Q4 (M1) et de 02/01 Q5.
- Dans la mission même, Q3 = Q1 + Q2 : l'explication de Q2 donne le second blanc de Q3, et Q4 refait « avant que » une troisième fois.

Correctif : **supprimer Q2**. La mission passe à 7 questions.

**M5 — 06/09 Q5, salle blanche et étiquette.** Le cadre « Quand … , le train (verbe) » au plus-que-parfait est celui de D02 (exercice de la carte D02#5). Par ailleurs :
- « venait de partir » marque bien l'antériorité, donc l'étiquette `anteriorite-non-marquee` est fausse ;
- l'explication commente « partit », qui n'est pas une option.

Remplacement (d2) :
- Énoncé : `Dans un récit au passé : « Quand Karim arriva au cinéma, le film ___ (commencer) depuis dix minutes. » Quelle forme convient ?`
- Options :
  - a (19, muette) `venait de commencer`
  - b (10, `fr.temps.recit-discours-melanges`) `a commencé`
  - c (clé, 14) `avait commencé`
  - d (10, `fr.temps.anteriorite-non-marquee`) `commençait`
- Explication : `Le début du film est achevé avant l'arrivée de Karim : une action déjà accomplie se met au plus-que-parfait, « avait commencé ». « Commençait » présenterait le début comme encore en cours ; « a commencé » est un temps du discours, qui ne convient pas à ce récit ; « venait de commencer » dirait que le film vient juste de commencer, ce que dément « depuis dix minutes ».`
- « film » et « cinéma » sont absents des 8 instantanés.

**M6 — 06/09 Q6, salle blanche et valeurs déjà posées.**
- l1 « Pourriez-vous baisser la musique » transpose « Pourriez-vous me graver ce CD ? » (D06, exercice de la carte).
- l2 « Si nous avions… » est le cas « si + condition » de 05 quiz Q5.
- La liste interdisait ces valeurs posées.

La carte demandait le **conseil**. Le cours 05 l'enseigne comme « ordre … atténué » : on le rétablit ainsi, et la condition passe par un complément, sans « si ».
- l1 → `Il vaudrait mieux que tu relises ta lettre avant de l'envoyer.` (62)
- l2 → `Avec un peu plus de temps, nous finirions le puzzle.` (52)
- l3 inchangée : `Samia pensait qu'elle arriverait avant la nuit.`
- r3 → `Un conseil, c'est-à-dire un ordre adouci` (40). r1 et r2 sont inchangées. Les paires restent l1→r3, l2→r1, l3→r2.
- Explication : `« Il vaudrait mieux que tu relises… » adoucit un ordre : c'est un conseil. Avec « avec un peu plus de temps », finir le puzzle dépend d'une condition qui n'est pas remplie : c'est un fait imaginaire. Dans « Samia pensait qu'elle arriverait », le verbe principal est au passé et « arriverait » est le futur vu depuis ce moment passé, sans aucune hypothèse.`
- « vaudrait » et « puzzle » sont absents des instantanés. Aucune fuite vers Q8 : « reproche » n'apparaît nulle part.

**M7 — 06/09 Q7, clone de 06/02 Q1 (liste) et étiquette sur une option à deux erreurs.** La grille passé simple/imparfait × imparfait/plus-que-parfait, dans une phrase en « Quand … », est celle de 06/02 Q1 (« entra … avait emprunté »). De plus, a (« comprenait ; mangeait ») porte deux erreurs et une étiquette.

Remplacement (d3). Il oppose action accomplie et action en cours au même moment passé :
- Énoncé : `Dans un récit au passé : « Quand Salma rentra, son frère ___ (terminer) déjà ses devoirs, et sa sœur ___ (terminer) encore les siens. » Quelles formes conviennent, dans l'ordre ?`
- Options :
  - a (25, muette) `terminait ; avait terminé`
  - b (29, muette) `avait terminé ; avait terminé`
  - c (21, `fr.temps.anteriorite-non-marquee`) `terminait ; terminait`
  - d (clé, 25) `avait terminé ; terminait`
- Explication : `Le frère a fini avant le retour de Salma, et « déjà » le confirme : action accomplie, plus-que-parfait, « avait terminé ». La sœur travaille encore à ce moment, et « encore » le dit : action en cours, imparfait, « terminait ». L'imparfait au premier blanc laisse l'action antérieure inachevée ; le plus-que-parfait au second dirait que la sœur avait déjà fini, ce que dément « encore ».`
- Vote nul à chaque blanc. La clé n'est ni la plus longue ni la plus courte.

**M8 — 03/07 Q1, miroir de 03 quiz Q3 et de 03/04 Q3, posé seul.** C'est exactement ce que la carte exclut. Son explication (« répondre à … complément indirect ») livre aussi Q3 a.

Remplacement (d1, neuf : même verbe, la construction décide) :
- Énoncé : `Le verbe « manquer » se construit de plusieurs façons. Dans quelle phrase peut-on le mettre à la forme passive ?`
- Options :
  - a (clé, 30) `Le joueur a manqué le penalty.`
  - b (30, `fr.voix.passif-sans-cod`) `Le joueur a manqué à ses amis.`
  - c (30, `fr.voix.passif-sans-cod`) `Le joueur a manqué de souffle.`
  - d (29, `fr.voix.passif-sans-cod`) `Le joueur a manqué deux fois.`
- Explication : `Seul « manquer le penalty » a un COD, qui peut devenir sujet : « Le penalty a été manqué par le joueur. » « À ses amis » et « de souffle » sont introduits par une préposition : ce ne sont pas des COD. Dans « a manqué deux fois », aucun complément d'objet ne suit le verbe.`

**M9 — 03/07 Q3 → Q6, fuite.** Q3 c (« Le médecin a été téléphoné ») et son explication (« téléphoner à … transformation impossible ») résolvent Q6, qui porte sur le même verbe et la même erreur. Q2 e emploie aussi « téléphoner à ».

Q6, remplacement (d3) :
- Énoncé : `Un élève écrit : « Sa tante a été succédée par Ali. » à partir de « Ali a succédé à sa tante. » Quelle est son erreur ?`
- Options :
  - a (clé, 58) `Le verbe n'a pas de COD, donc la phrase n'a pas de passif.`
  - b (58, `fr.voix.temps-non-conserve`) `Le temps n'est pas conservé : il fallait « est succédée ».`
  - c (52, `fr.accord.pp-etre-non-accorde`) `Le participe « succédée » devrait rester invariable.`
  - d (55, muette) `Le complément d'agent devrait ouvrir la phrase passive.`
- Explication : `« Succéder à » est suivi d'un complément introduit par « à » : « sa tante » n'est pas un COD et ne peut pas devenir sujet. L'accord « succédée » et le temps « a été » suivent bien les règles du passif ; c'est la transformation elle-même qui est impossible.`
- « succéder » est absent du chapitre 03 et des instantanés.

**M10 — 03/07 Q4, vote et étiquette.**
- Le vote reconstruit la clé : « visiteurs » sujet ×3, « prévenus » ×2.
- b (« Les gardiennes ont été prévenus ») porte deux erreurs (rôles + accord) et l'étiquette `roles-inverses`.

Correctif : b → `Les gardiennes ont été prévenues par les visiteurs.` (51), étiquette `fr.voix.roles-inverses` gardée, qui est alors la seule erreur. Le vote sur le participe devient « prévenues » ×2, qui n'est pas la clé. Longueurs : 51 / 51 / clé 50 / 49.

**M11 — 03/07 Q5, marqueur.** « par les violents orages » n'apparaît que dans a, qui s'élimine à vue (et c'est la plus longue). Le plus-que-parfait est le seul temps neuf face à 03/06 : on le garde. Sans marqueur, la clé (avaient + détruites) serait strictement la plus longue ; on change donc l'axe du temps :
- a → `Les récoltes auraient été détruites par les orages.` (51, `fr.voix.temps-non-conserve`) ;
- c → `Les récoltes auraient été détruite par les orages.` (50, muette) ;
- b (49) et d (clé, 50) inchangées.

La grille 2×2 est exacte (avaient/auraient × détruites/détruite), le vote nul, et la clé n'est ni la plus longue ni la plus courte.

Explication, dernière phrase → `Mettre « être » au conditionnel, « auraient été », ou laisser le participe sans accord sont deux erreurs distinctes.`

**M12 — 15/06 Q7 → Q2, fuite.** d « D'abord, on y apprend à monter de vrais robots… » recopie la clé de Q2.
- d → `D'abord, on y apprend à programmer, ce que le cours de technologie ne permet pas.`
- e → `Par exemple, mercredi dernier, mon groupe a programmé son robot pour qu'il suive un petit parcours.`

L'ordre c d e b a reste unique, et l'explication est inchangée.

**M13 — 15/06 Q4, clé trouvable par la forme.** « Quel titre nomme le fait principal **en peu de mots** ? », et la clé (45) est strictement la plus courte.
Correctif : a → `Un samedi pas comme les autres` (30, muette, titre vague). La clé n'est plus la plus courte.

**M14 — 15/06 Q4–Q5, lieu.**
- « Kasserine » est l'en-tête de deux devoirs sources (D07, D08).
- Le Jebel Chambi est en outre une zone militaire fermée depuis 2013 : une lycéenne seule au sommet à 6 h n'est pas plausible.

Correctif, dans la fiche des deux énoncés et dans toutes les options : `Jebel Chambi, près de Kasserine` → `Jebel Zaghouan, au sud de Tunis` (même longueur, 31 caractères).
- Q4 b → `Le Jebel Zaghouan, un massif magnifique à découvrir un jour` (59).
- Q4 d (clé) → `Rim Chatti, 17 ans, au sommet du Jebel Zaghouan` (47).
- Q5 b → `Que s'est-il passé samedi sur la montagne, au sud de Tunis ? Vous le saurez en lisant la suite de cet article.` (110).
- Q5 a (clé) reste à 116 ; c (118) est toujours la plus longue.
- Dans l'explication de Q5 : `(le Jebel Zaghouan, au sud de Tunis)`.
- « Zaghouan » et « Tunis » sont absents des instantanés.

**M15 — 15/06 Q5, explication par le rang.** « … et le dernier omet l'acteur et le lieu » désigne une option par sa place, alors que les options sont mélangées.
→ `… et celui qui parle d'« une jeune fille » sans la nommer omet l'acteur précis et le lieu.`

**M16 — 11/07 Q4, clone de 11/06 Q8 (liste).** « des pommes qui ont beaucoup de jus » → juteux / juteusement / juteuse / juteuses a la même grille que « couleurs brillantes » (brillants / brillamment / brillent / brillantes).

Remplacement (d2) : on part du complément du nom, et on ajoute un paronyme.
- Énoncé : `On remplace le complément du nom par un adjectif épithète de même sens : « des fêtes de famille ». Quelle expression convient ?`
- Options (toutes muettes, faute d'étiquette d'accord de l'épithète) :
  - a (19) `des fêtes familiaux`
  - b (19) `des fêtes familials`
  - c (clé, 20) `des fêtes familiales`
  - d (20) `des fêtes familières`
- Explication : `Une fête de famille est une fête familiale : l'adjectif « familial » dit la même chose que le complément du nom. Épithète de « fêtes », féminin pluriel, il prend -es : « familiales ». « Familiaux » est le masculin pluriel, et « familials » n'existe pas. « Familières » vient de « familier », « que l'on connaît bien » : le sens change.`
- La clé est ex æquo avec d, donc pas strictement la plus longue. Vote : radical « familial » ×3, mais genre 2/2 et pluriel en -s/-x non décisif.

**M17 — 11/07 Q2, notion employée sans définition.** Q2 demande « nature » et « fonction », mais seul l'énoncé de Q1 les définit. Le cours 11 ne les définit nulle part : son tableau fond les deux (« groupe prépositionnel **complément du nom** »). Au donjon, Q2 peut sortir seule. Correctif : **une ligne de cours** (voir § Notions).

### Mineurs (11)

- **m1 — 02/11 Q5**, exemple du cours recyclé. Le cours 02 a : « Il a raté le bus, sous prétexte que son réveil n'a pas sonné ». La mission : « Rayan … sous prétexte que son réveil est tombé en panne ». Remplacement :
  - Énoncé : `Nadia n'a pas rendu son exposé. Elle affirme que son imprimante est tombée en panne, mais le professeur n'en croit rien. Quelle phrase unique rend ce doute ?`
  - a (76) `Nadia n'a pas rendu son exposé parce que son imprimante est tombée en panne.`
  - b (85) `… sous prétexte que son imprimante soit tombée en panne.`
  - c (74) `… puisque son imprimante est tombée en panne.`
  - d (clé, 84) `… sous prétexte que son imprimante est tombée en panne.`
  - Les étiquettes et l'explication restent, avec « soit tombée ».
- **m2 — 02/11 Q6** : la liste du rappel omet la forme de l'option d. Énoncé → `Une corrélation relie deux faits qui évoluent ensemble : « plus… plus… », « moins… moins… », « plus… moins… » ou « moins… plus… ». Faits : « On monte en altitude. » / « L'air devient frais. » Quelle phrase les relie en gardant le sens ?`
- **m3 — 02/11 Q2** : redit Q1 (« de peur que » = but à éviter). Acceptable en d1 d'ouverture ; si une question doit tomber, c'est celle-ci.
- **m4 — 02/10 Q1 et Q2 → Q7** : les explications énoncent la lecture du rapport depuis la principale et l'effet de « avant que ». C'est une règle du cours appliquée, pas une clé : toléré, comme L04 m12. Q1 l3 (« aussitôt que » → postériorité) recoupe le piège du cours et 02/02 Q2, mais seulement comme une paire d'un appariement.
- **m5 — 11/07 Q5 et Q6** : la clé est la plus courte deux fois de suite, et Q6 transpose l'exemple travaillé du cours (« tasse de café / tasse à café »). Q6 d → `une assiette soupe` (18, muette). Explication, dernière phrase → `« Sans soupe » renverse le sens, et « une assiette soupe », sans préposition, n'est pas un complément du nom.` La clé (20) n'est plus la plus courte.
- **m6 — 11/07 Q5** : « après la colère » et « contre la colère » sont faibles (sens absurde). Toléré en d2.
- **m7 — 15/06 Q1** : même gabarit que 09 quiz Q7 (thèse contre « Je vais parler un peu de… »). Le destinataire change, la tâche non. Toléré : c'est l'archétype de la carte.
- **m8 — 15/06 Q6** : a (« phrases trop longues ») est démenti par le brouillon cité, et c (« passé composé exclu ») est absurde. Toléré.
- **m9 — 15/06 Q2** : d est la seule option sans « Tu devrais l'essayer » ; seul un distracteur s'en distingue. Toléré.
- **m10 — 02/11 Q5 a et c** : `rapport-logique-confondu` sur « parce que / puisque ». Ces options disent une cause, alors que la vraie relation est une cause donnée pour fausse. Le libellé est approximatif mais défendable : à garder.
- **m11 — 03/07 Q3 d** : « Cette visite a été parlée » reprend le geste de l'accroche du cours (« Cet exploit est parlé par tout le monde »). C'est un distracteur, donc toléré.

---

## Notions données dans l'énoncé et adaptations — tranchées

1. **Corrélation (02/11 Q6) : légitime.**
   - Elle n'est enseignée nulle part (01 à 15). La 9ᵉ française n'en a pas de leçon : la définition doit rester dans l'énoncé.
   - Elle ne désigne pas la clé : les quatre options emploient les formes listées, et seul le sens des faits départage.
   - Seul défaut : la liste est incomplète (m2).
   - Pas de ligne de cours nécessaire.
2. **Nature / fonction (11/07 Q1) : le rappel est légitime, mais une ligne de cours est nécessaire**, à cause de Q2 (M17).
   - `content/french/11-groupe-nominal-et-attribut/cours.md`, § « 🏰 Le groupe nominal étendu », juste après la ligne « Chaque expansion se rattache à un nom, le **noyau** du GN : c'est lui qu'elle précise. » :
     `Pour analyser une expansion, on donne sa **nature** — ce qu'elle est : adjectif, groupe prépositionnel, proposition subordonnée relative — puis sa **fonction** — le rôle qu'elle joue auprès du nom : épithète, complément du nom ; la relative, elle, complète son antécédent. _De la voiture_ : nature, groupe prépositionnel ; fonction, complément du nom _capot_.`
   - `resume.md` du même chapitre, puce à ajouter :
     `- **Nature / fonction** : la nature dit ce qu'est l'expansion (adjectif, groupe prépositionnel, relative), la fonction le rôle qu'elle joue auprès du nom (épithète, complément du nom, complément de l'antécédent).`
   - L'exemple « de la voiture » est déjà dans le cours : il ne livre pas « de laine ».
   - Le rappel de Q1 peut rester : il ne désigne pas la clé.
   - Cette ligne relève d'une PR de cours (pilote), pas des fichiers de l'auteur.
3. **Fiche de faits (15/06 Q4 et Q5) : légitime.** Ce sont des données (la carte dit « à partir de faits donnés »), pas une notion. Elle est redonnée dans chaque énoncé, donc les deux questions se lisent seules. Elle ne désigne pas la clé, à deux réserves près : la longueur en Q4 (M13) et le lieu (M14).
4. **« Conseil » traité comme une atténuation (06/09 Q6 et Q8).**
   - Le cours 05 enseigne « un ordre, une demande ou un **reproche** atténués ». Q8 (« Vous auriez dû », reproche adouci) est donc juste et enseignée.
   - En revanche, l'auteur a remplacé le conseil de la carte par la politesse en Q6. C'est la valeur déjà posée (05/02 Q3), et elle transpose D06.
   - Le conseil s'enseigne bien comme « ordre adouci » : le correctif M6 le rétablit (« Il vaudrait mieux que tu… » → « Un conseil, c'est-à-dire un ordre adouci »).
5. **Verbe « avoir » (D07#3) non repris : justifié.** La propriété du cours 03 limite les cas sans passif aux verbes transitifs indirects, intransitifs, pronominaux, et à ceux qui changent de sens. « Avoir » n'y figure pas : l'exiger serait tester une notion non enseignée.
   Si le pilote veut l'ajouter un jour, il faut d'abord une ligne de cours, hors de ce lot. Dans la propriété du § « 🚫 Quand la transformation passive est impossible », ajouter `_avoir_ (au sens de posséder)` à la liste des verbes qui n'ont pas de passif.

## Étiquette proposée `fr.mode.subjonctif-apres-apres-que` — rejetée, prendre `fr.mode.subjonctif-abusif`

Règle de création : au moins 3 questions distinctes, une seule erreur, aucune option `multi`, `ordering` ni `matching`. Elle n'est **pas** remplie :

| placement proposé | erreur exécutée | recevable ? |
| --- | --- | --- |
| 02/10 Q5 c « Après que le car soit arrivé » | subjonctif après « après que », seule erreur | oui |
| 02/10 Q6 a « Après qu'il serve le thé » | rapport inversé ET subjonctif : deux erreurs | non, à laisser muette |
| 02/11 Q5 b « sous prétexte que … soit tombé » | subjonctif après « sous prétexte que », pas « après que » | non pour cet identifiant |

L'identifiant étroit ne compte donc qu'une question. En revanche, la famille « subjonctif après un déclencheur de l'indicatif » compte **4 placements propres** : 02/10 Q5 c, 02/11 Q5 b, 06/09 Q1 d (« Pendant que Sofia fasse ») et 06/09 Q3 c (« prenne ; pleuve », une seule erreur, au premier blanc). C'est exactement `fr.mode.subjonctif-abusif`, déjà employé en `05/06`. Son libellé actuel ne cite que des verbes : on l'**élargit** aux conjonctions, sans rien retirer, et son emploi en 05/06 reste exact.

- **fr** : `Tu mets le subjonctif après un verbe ou une conjonction qui appelle l'indicatif (espérer que, être sûr que, penser que ou croire que à la forme affirmative ; après que, pendant que, sous prétexte que) : ils présentent le fait comme réel, attendu ou affirmé.`
- **en** : `You use the subjunctive after a verb or conjunction that takes the indicative (espérer que, être sûr que, affirmative penser que or croire que; après que, pendant que, sous prétexte que): they present the fact as real, expected or claimed.`
- **ar** : `تستعمل subjonctif بعد فعل أو أداة ربط تستدعي indicatif (espérer que، être sûr que، penser que وcroire que في الإثبات؛ après que، pendant que، sous prétexte que): هذه العبارات تقدّم الحدث واقعًا أو منتظرًا أو مُدّعًى.`

La version arabe de l'auteur est fautive : la « صيغة شرطية » est le conditionnel. Celle-ci suit le registre des entrées `fr.*` (« تستعمل subjonctif بعد ما يستدعي indicatif »).

Placements, à ajouter par l'auteur après la modification du registre par le pilote :
- 02/10 Q5 c ;
- 02/11 Q5 b (ou la nouvelle b de m1) ;
- 06/09 Q1 d ;
- 06/09 Q3 c.

Les autres étiquettes manquantes signalées par l'auteur :
- « adjectif épithète non accordé » : options muettes en 11/07 Q4, et une seule question ; aucune famille à créer ;
- « sens changé par la préposition » : 11/07 Q5 et Q6, soit 2 questions, en dessous du seuil ; options muettes.

## Étiquettes employées — contrôle

Les 20 identifiants employés existent sur le registre. Libellés confrontés à l'erreur exécutée :
- Justes : `subjonctif-oublie` (15 options), `rapport-temporel-confondu`, `passif-sans-cod`, `pp-etre-non-accorde`, `temps-non-conserve`, `argu.*`, `presse.*`, `gn.complement-nom-ou-verbe`, `subord.completive-relative-confondues`, `valeur.forme-sans-contexte`, `lettre.registre-melange`.
- À retirer ou corriger :
  - 06/09 Q5 a « venait de partir » (`anteriorite-non-marquee` faux) : remplacé (M5) ;
  - 06/09 Q7 a (deux erreurs, étiquetée) : remplacé (M7) ;
  - 03/07 Q4 b (deux erreurs) : corrigé (M10).
- Aucune étiquette sur une option `multi`, `ordering` ou `matching` ✓.

## Résumé

- **Questions auditées :** 40, toutes re-résolues à l'aveugle (multi, matching, ordering et grilles 2×2 case par case).
- **Clés fausses :** 0. **Critiques :** 0.
- **Majeurs :** 17. Ils se répartissent ainsi :
  - doublons de gabarit avec la liste « ne pas redemander » : 02/10 Q4, 02/11 Q3, 06/09 Q2, 06/09 Q7, 03/07 Q1, 11/07 Q4 ;
  - salle blanche : 06/09 Q5, 06/09 Q6, lieu de 15/06 ;
  - marqueurs et vote : 02/11 Q4, 03/07 Q4, 03/07 Q5, 15/06 Q4 ;
  - fuites : 03/07 Q3 → Q6, 15/06 Q7 → Q2 ;
  - explication par le rang : 15/06 Q5 ;
  - notion sans définition : 11/07 Q2.
- **Mineurs :** 11.
- **Effectifs après correctifs :** 02/10 → 6 questions (Q4 supprimée), 06/09 → 7 (Q2 supprimée), les autres sont inchangés. Toutes les missions restent dans la fourchette 6–8 et sous le plafond de leur carte.
- **Étiquette proposée :** rejetée (1 placement propre). Élargir `fr.mode.subjonctif-abusif` (fr, en, ar ci-dessus) et la placer en 4 endroits.
- **Ligne de cours nécessaire :** chapitre 11, nature/fonction (texte exact ci-dessus).
- **Gates :**
  - `check` : vert ;
  - `qa:strict` : 0 erreur, 0 avertissement sur le lot ;
  - `tranche` : 0 clé strictement la plus longue et 0 paire proche dans le lot ;
  - `gisement:controle` : 0 plage.
- **Verdict : à corriger avant fusion** (fix-first). Tous les textes de remplacement ont été vérifiés par script : longueur de la clé, réponse unique, vote, fuites. Les nouveaux noms et lieux sont absents des 8 instantanés.
