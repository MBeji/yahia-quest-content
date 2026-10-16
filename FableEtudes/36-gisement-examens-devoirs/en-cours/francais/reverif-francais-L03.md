# Re-vérification — lot L03, français 9ᵉ (m013–m017)

Auditeur indépendant, 2026-10-16. J'ai relu l'état `HEAD` de `/home/user/wt-fr` (branche
`wip/gisement-francais-9eme`). Les corrections L03 sont réparties sur deux commits :
- `84a5eb5f` : cours, résumé, `misconceptions.json`, m013, m014, m015 ;
- `d5b946ad` : m016 et m017.

Pour les fichiers du lot, l'arbre de travail est identique à `HEAD`. J'ai aussi lu le journal
`auteurs-notes/fr-L03/CORRECTIONS.md`. Je n'ai rien écrit dans `content/` ni dans git.

Sources relues :
- les transcriptions de toutes les sessions citées ;
- le manuel élève CNP `121905P00` (téléchargé depuis le CNP, texte extrait), pages 79, 103–104 et 178–181 ;
- `misconceptions.json` (`fr.*`).

**Gates.** Moteur `/home/user/eng-svtses`, lié à `wt-fr/content` :
- `content:check` : vert (120 matières, 1067 étiquettes) ;
- `content:qa:strict` : 4 erreurs, toutes dans `french/03-voix-active-et-passive/exercices/06-examens-2007-2023-…`, un
  fichier non suivi d'un autre lot. Ce n'est **pas L03**. Aucun avertissement sur les chapitres 05 et 06 ;
- `content:tranche -- --subject french --chapters 05,06` : 106 questions.
  - Clé strictement la plus longue : 1 sur 106 (m017 Q2, déclarée).
  - Positions des clés : a 24, b 27, c 26, d 29.
  - Une paire proche : m016 Q1 ↔ Q2, à 0,50 (déclarée, voir § 5).
  - Deux groupes « gabarit » : c'est la consigne officielle « au mode et aux temps qui conviennent », reprise
    d'un sujet à l'autre, avec des données toutes différentes. **Ce n'est pas un gabarit.**

## 1. Correctifs de l'audit : appliqués ?

| réf. audit | objet | appliqué | juste (contre la transcription) |
| --- | --- | --- | --- |
| M1 | cours 05 + résumé : espérer / être sûr + indicatif ; rappels retirés (m013 Q2, ex-Q10, ex-Q11) | oui, mot pour mot | oui (2017 G 3b, 2018 G 3, 2006 3b) |
| M2 | cours 05 + résumé : choix de l'auxiliaire | oui, mot pour mot | oui (voir § 3) |
| M3 | m013 ex-Q8 (revienne) retirée | oui | — |
| M4 | m013 Q6 → 2003 a (puissent) | oui, texte exact, clé b | oui : 2003, 3a, mot pour mot |
| M5 | m014 Q6 : glose « pièces de métal d'un moteur » | oui | oui (note imprimée 1 de 2009 G ; PDF vérifié par l'audit) |
| M6 | m015 Q2 et Q10 : consigne « au temps qui convient », annonça déclaré, [sic] | oui | oui (2024 G 3, 2023 G 3b) |
| M6 | m015 Q11 → solution de rechange 2019 G (m'avait appris) | oui (rechange choisie) | oui (2019 G 3, mot pour mot ; « découvrais » déclaré) — explication à reprendre, R3 |
| M7 | m016 : consignes officielles Q1, Q2, ex-Q4, ex-Q8, ex-Q10 ; ex-Q3 et ex-Q5 retirées ; ex-Q7 cadre 2011 G rétabli et étiqueté | oui | oui (2025 G, 2026 G a, 2023 G a, 2019 G, 2011 G) |
| M7 | m016 ex-Q6 (2006) : première ligne | oui, mais la question finale de l'ancien texte reste : double question (R2) | — |
| M8 | m017 : ex-Q1 retirée ; ex-Q2 options d'accord ; ex-Q4 « a aidés » ; ex-Q6 sans « au passé composé » ; ex-Q7 « regarda / dit » | oui, mot pour mot | oui (2026 T, 2025 T, 2019 T, 2017 T) |
| m1 | m013 : titre sans « conditionnel » | oui | — |
| m2 | m013 Q5 : « phrase abrégée » | oui | oui (2006 3a) |
| m4 | m013 Q3 : glose « le présent et le futur conviennent tous deux » | oui | oui (2013 G 2b, « aux temps qui conviennent ») |
| m7 | m014 Q4 : d « C'était … viendrai » | oui | oui (2012 T) |
| m8 | m014 Q8 : formule adoucie | oui | oui (2009 T : imparfait et passé composé donnés) |

## 2. Re-résolution à l'aveugle (les cinq fichiers en entier, 48 questions)

| mission · Q | ma réponse | clé | verdict |
| --- | --- | --- | --- |
| m013 Q1 | ouvre ; soient | b | OK (cases 2/2) |
| m013 Q2 | battra | d | OK : plus de rappel, « batte » redevient un vrai piège |
| m013 Q3 | sera | a | OK |
| m013 Q4 | comprenne | c | OK |
| m013 Q5 | saisisse | d | OK |
| m013 Q6 | puissent | b | OK |
| m013 Q7 | Bamban craint que je sois sérieux. | a | OK |
| m013 Q8 | … doute que Bamban soit capable … | b | OK |
| m013 Q9 | remportera ; puissent ; fasse | d | OK (3 cases, 2/2 chacune) |
| m013 Q10 | est capable ; s'en aperçoive | c | OK (2×2) |
| m014 Q1–Q3 | viennent · s'étalent · font | c · a · d | OK |
| m014 Q4 | C'est … viens de recevoir | b | OK : la première case vote 2/2 ; la clé est la plus courte (structurel, déclaré) |
| m014 Q5–Q10 | suffisait · se mettaient ; rugissaient · se sentira ; s'endormira · continuera · dis ; veux ; hurle · était caché ; allait | c d a b d c | OK |
| m015 Q1 | avais ; venait | a | OK |
| m015 Q2 | présenta | c | OK : « avait présenté » et « présentera » ne sont plus éliminés par la consigne |
| m015 Q3–Q9 | se rendit ; découvrit · allais ; aimais · pris ; étais · hurla ; rougit · entra ; engagea · entendis ; se rapprochait · souffrait ; fournissait | b d b a d c a | OK (Q9 : voir R4) |
| m015 Q10 | se mettaient | d | OK : « s'étaient mis » et « se mettront » sont de nouveau en jeu |
| m015 Q11 | avait appris | b | OK. Risque « m'apprenait » accepté (§ 5). Explication inexacte : R3 |
| m015 Q12 | répétait ; avait apprises | c | OK |
| m016 Q1 | aura fini ; montera | d | OK |
| m016 Q2 | aura ; aura réalisé | b | OK (le piège de l'ordre d'écriture est intact) |
| m016 Q3 | aura préparé ; fera | c | OK (« ferait » vivant) |
| m016 Q4 | aura rattrapé | d | OK, mais double question (R2) |
| m016 Q5 | rapportera ; aura vécu | a | OK (« sera de retour » rétabli : « vivra » n'est plus défendable) |
| m016 Q6 | aurons évalué ; pourrez | c | OK (« évaluions » est le vrai piège) |
| m016 Q7 | irai ; sera sorti | d | OK |
| m016 Q8 | ouvrirai ; aurai obtenu | b | OK |
| m017 Q1 | … l'ont félicité et lui ont fait … | d | OK (2×2, cases 2/2) |
| m017 Q2 | ont mené ; ont travaillé | c | OK (clé la plus longue, structurelle) |
| m017 Q3 | aide ; sont | a | OK (une seule erreur par distracteur) |
| m017 Q4 | ont réussi ; sont venus | d | OK |
| m017 Q5 | … dès qu'on a ouvert le bal, Pedro a invité … | b | OK (aucune option tout au passé simple) |
| m017 Q6 | nous a regardés ; a dit | c | OK (2×2) |
| m017 Q7 | a excellé ; s'est passionné ; a remporté | a | OK (3 cases 2/2) |
| m017 Q8 | Je lui ai embrassé … je suis allé … | b | OK (le narrateur est un garçon, 2002) |

**Bilan.**
- Aucune clé fausse ; chaque question a une seule réponse juste.
- Aucune consigne ne fixe la réponse : toutes les consignes qui tuaient des distracteurs ont été remplacées.
- Il reste trois consignes non officielles, en m015 Q6 (2016 G), Q8 (2020 G) et Q12 (2026 G). Elles
  n'éliminent aucune option, car toutes les options sont aux temps nommés : voir R5, facultatif.
- **Fuites.**
  - Q3, Q9 et Q10 de m013 énoncent dans leurs explications des règles du cours (opinion niée, être sûr
    que). L'audit l'avait admis, et la règle figure désormais au cours.
  - « puissent » apparaît en Q6 et en Q9 (m013). Le verbe « apprendre » revient en m015 Q11 et Q12. Ces deux
    reprises sont déclarées (§ 5).
  - Aucune question ne livre la clé d'une autre.
- **Doublons avec les missions publiées.** La liste « ne pas redemander » est respectée.

## 3. Ajouts au cours et au résumé du 05, comparés au manuel cité

**Subjonctif.** Le manuel (p. 180, encadré) range au subjonctif :
- la volonté (vouloir, *souhaiter*, exiger, il faut que) ;
- le sentiment (regretter…) ;
- le doute ;
- la possibilité ;
- l'opinion à la forme négative ou interrogative.

L'exercice 6 (p. 181) oppose « nous pensons que / il considère que + indicatif » et « je ne crois pas que + subjonctif ».
La ligne ajoutée (« espérer que » et « être sûr que » gardent l'indicatif ; « J'espère qu'il viendra », mais
« Je souhaite qu'il vienne ») prolonge cette opposition **sans la contredire** : le manuel ne range « espérer »
nulle part au subjonctif. L'incise du résumé est cohérente avec la ligne du cours.

**Auxiliaire.** Le manuel (p. 79 et p. 103–104) dit « auxiliaire être ou avoir ». Il fait accorder le participe des
verbes pronominaux et de « revenir » avec le sujet, mais ne donne pas de liste.

Le bloc ajouté est **juste et cohérent** :
- les pronominaux et les verbes de mouvement ou de changement d'état prennent « être » ;
- avec un COD, « sortir », « monter » et « descendre » reprennent « avoir ».

C'est un complément au manuel, pas un écart. La phrase du résumé le reprend fidèlement. `content:qa:strict` ne
signale rien sur le cours du 05.

## 4. Étiquette `fr.mode.subjonctif-abusif`

- **Libellés** : fr, en et ar reprennent mot pour mot le libellé proposé par l'audit (élargi à l'opinion
  affirmative). L'arabe parle bien de *subjonctif*, non de conditionnel.
- **Où elle est posée** : m013 Q2 a (`batte`), Q3 b (`soit`), Q10 a (`soit capable ; s'en aperçoive`), soit
  **3 questions distinctes**. Les trois sont des `qcm` : aucune n'est `multi`, `ordering` ou `matching`. Elle
  n'est posée nulle part ailleurs dans le corpus.
- **La bonne erreur ?** Oui. Chacune de ces options a pour **seule** erreur le subjonctif après espérer, croire
  (forme affirmative) ou être sûr. En Q10, l'autre case (`s'en aperçoive`) est juste. L'option croisée d
  (`soit capable ; s'en aperçoit`), qui porte deux erreurs, reste muette, comme il se doit. Q9 n'est pas
  étiquetée, ce qui est conforme à l'audit.
- **Autres étiquettes du lot** : toutes exactes.
  - `fr.accord.pp-avoir-avec-sujet` (m017 Q1 a, « l'ont félicités » accordé avec le sujet pluriel) : le
    libellé correspond.
  - `fr.accord.pp-avoir-cod-avant-oublie` (m017 Q6 a, m015 Q12 b).
  - `fr.temps.anteriorite-non-marquee` (m015 Q11 a ; m016 Q1 a, Q2 a, Q3 a, Q4 a, Q5 c).
  - `fr.temps.recit-discours-melanges` (m017 Q5 a).

## 5. Écarts déclarés par l'auteur

1. **Clé la plus courte, et une clé la plus longue.**
   - Clé la plus courte : m014 Q4 ; m015 Q2, Q3, Q6, Q7 (4 sur 12, l'effet structurel du couple passé simple,
     déjà admis en m9) ; m017 Q3. **Accepté.**
   - Clé la plus longue : m017 Q2 (décision du pilote, structurelle). **Accepté** : c'est 1 sur 106 dans la
     tranche, et Q3, de même structure, a la clé la plus courte.
2. **Paire proche m016 Q1 ↔ Q2 (0,50)** : même consigne officielle de 2025 G, mais autres verbes et autre piège
   (Q2 joue sur l'ordre d'écriture). C'est un exercice parallèle voulu. **Accepté.**
3. **Risques de défendabilité.**
   - m016 Q1 (« finira ; montera ») : la consigne officielle « selon le cas » et la règle du cours 06 (action
     achevée avant une autre au futur, donc futur antérieur) tranchent. **Accepté.**
   - m015 Q11 (« m'apprenait ») : l'imparfait est grammaticalement possible avec « une année auparavant ». Il
     ne marque pourtant pas l'achèvement que demande le cours (« action déjà achevée par rapport à un moment du
     passé »), et le sujet officiel attend le plus-que-parfait. **Accepté**, à condition de corriger
     l'explication, qui donne un mauvais motif (R3).
   - m017 Q5 (« invitait ») : l'imparfait ne convient pas à un fait unique de la soirée après « dès que ».
     **Accepté.**
4. **Fuite m015 Q11 / Q12 (même verbe, « apprendre »)** : Q12 met au plus-que-parfait toutes ses options. Si
   l'élève voit Q12 d'abord, cela l'oriente un peu vers la forme de Q11, sans lui donner le motif
   d'antériorité. Q12 teste la personne et l'accord. **Accepté** (fuite mineure).
5. **« puissent » en m013 Q6 et Q9** : déjà accepté par l'audit ; Q9 exige en plus le choix du mode pour trois
   verbes. **Accepté.**

## 6. Registre `gisement.json` (même état à `HEAD` et dans l'arbre de travail)

| mission | `fichier` | `etapes` registre / fichier | `sources` | verdict |
| --- | --- | --- | --- | --- |
| m013 (`C19#4`) | 05/06-examens-2003-2018-mode-apres-le-verbe-introducteur.json ✓ | **11 / 10** | 7 sessions, toutes utilisées ✓ | **à corriger** |
| m014 (`C24#4`) | 05/07-examens-2009-2016-transposer-present-imparfait-futur.json ✓ | 10 / 10 ✓ | 8 sessions, toutes utilisées ✓ | OK |
| m015 (`C05#4`) | 06/06-examens-2010-2026-imparfait-passe-simple-plus-que-parfait.json ✓ | 12 / 12 ✓ | **`C23#4` (2015 G) ne donne plus de question ; `C15#4` (2019 G) manque** | **à corriger** |
| m016 (`C03#4`) | 06/07-examens-2006-2026-futur-simple-ou-futur-anterieur.json ✓ | **10 / 8** | **`C23#4` (2015 G) ne donne plus de question** | **à corriger** |
| m017 (`C02#4`) | 06/08-examens-2002-2026-present-ou-passe-compose.json ✓ | **9 / 8** | 7 sessions, toutes utilisées ✓ | **à corriger** |

## 7. Défauts restants

**R1 — registre (mineur, obligatoire).** Dans `content/programmes-officiels/sources-externes/web-9eme-base-french/gisement.json`.

> ⚠ Ce fichier est modifié en ce moment par un autre agent, dans l'arbre de travail : ne toucher qu'aux cinq
> entrées L03.

- Mission `C19#4` : `"etapes": 11` → `"etapes": 10`.
- Mission `C03#4` :
  - `"etapes": 10` → `"etapes": 8` ;
  - retirer `"C23#4"` de `sources` ;
  - dans `note`, remplacer `(C03#4, C01#4, C07#4, C13#4, C15#4, C23#4, C29#3, C37#4)` par
    `(C03#4, C01#4, C07#4, C13#4, C15#4, C29#3, C37#4 ; C23#4 lu, écarté)`.
- Mission `C02#4` : `"etapes": 9` → `"etapes": 8`.
- Mission `C05#4` :
  - dans `sources`, remplacer `"C23#4"` par `"C15#4"` ;
  - dans `note`, remplacer `C23#4` par `C15#4` dans la liste et ajouter `; C23#4 lu, écarté` avant la parenthèse
    fermante.

**R2 — m016 Q4 (2006), double question (mineur, obligatoire).**

Ce défaut vient de mon correctif M7, qui ne remplaçait que la première ligne. Remplacer le `prompt` entier par :

```
(Examen 2006) Conjugue le verbe entre parenthèses au mode et au temps qui conviennent.
« La maîtresse pense que cet élève poursuivra normalement ses études une fois qu'il (rattraper) son retard. »
Quelle forme convient pour « rattraper » ?
```

C'est la consigne officielle de 2006 (§ 3). Elle n'élimine aucune option : « aurait rattrapé » et « avait
rattrapé » restent en jeu. Les options, la clé (d) et l'explication ne changent pas.

**R3 — m015 Q11, explication (mineur, obligatoire).**

Le défaut tient à deux motifs inexacts :
- avec « une année auparavant », l'imparfait ne ferait **pas** coïncider l'enseignement avec la classe de Marie ;
- le conditionnel n'exige pas « si » : le cours 05 lui donne aussi la valeur de futur par rapport au passé.

Remplacer l'`explanation` par :

```
« Une année auparavant » situe l'enseignement avant le moment du récit (« quand j'étais dans la classe de Marie ») : l'action est achevée à ce moment, d'où le plus-que-parfait, « m'avait appris » (auxiliaire « avoir » à l'imparfait + participe passé). L'imparfait « m'apprenait » montrerait l'apprentissage en cours de déroulement, sans marquer qu'il était achevé avant ce moment ; « apprendrait » et « aurait appris » sont des conditionnels, alors que rien n'est ici imaginaire, soumis à une condition ou à venir par rapport au passé. Le piège courant : un temps simple pour l'action déjà accomplie ; c'est le temps composé qui marque l'antériorité.
```

Ce texte ne contient aucune forme d'une autre question (Q12 porte « répétait ; avait apprises »).

**R4 — m015 Q9 (2012 G), verbe donné sans le dire (mineur, obligatoire par cohérence avec M6).**

« débarqua » est un verbe à conjuguer dans le sujet officiel (« Jeff (débarquer) »), comme « annonça » en Q10,
qui est déclaré. La consigne officielle est « aux temps qui conviennent ». Remplacer la première ligne du `prompt`
par :

```
(Examen 2012, générale) Conjugue les verbes entre parenthèses aux temps qui conviennent. Le sujet officiel faisait aussi conjuguer « débarquer », donné ici.
```

Toutes les options sont à l'imparfait ou au passé simple : aucune n'est éliminée. La clé (a) et l'explication
ne changent pas.

**R5 — facultatif : consignes officielles en m015 Q6, Q8 et Q12.**

Elles ne tuent aucune option, d'où le statut facultatif. Si l'auteur veut une fidélité complète, voici les
premières lignes de `prompt` à reprendre :

- Q6 : `(Examen 2016, générale) Conjugue les verbes entre parenthèses au mode et au temps qui conviennent.`
- Q8 : `(Examen 2020, générale) Conjugue les verbes entre parenthèses aux temps qui conviennent.`
- Q12 : `(Examen 2026, générale) Conjugue les verbes entre parenthèses au mode et aux temps qui conviennent.`

**R6 — facultatif, deux explications.**

- **m013 Q2** : remplacer `l'espoir, lui, porte sur un fait donné pour réel.` par `l'espoir, lui, présente le fait
  comme attendu.`. Ce sont les mots du cours ajouté.
- **m017 Q1** : remplacer `le COD « l' » (Angel, masculin singulier)` par `le COD « l' » (masculin singulier)`.
  Le nom « Angel » ne figure pas dans l'énoncé.

## Verdict

- **Clés fausses : 0.**
- Correctifs de l'audit : tous appliqués, à la lettre.
- Étiquette `fr.mode.subjonctif-abusif` : conforme (3 questions, aucune en `multi`, `ordering` ou `matching`).
- Ajouts au cours et au résumé du 05 : justes et cohérents avec le manuel `121905`.
- Écarts déclarés : 5, tous acceptés (le 3ᵉ sous réserve de R3).
- Gates des chapitres 05 et 06 : vertes. Les 4 erreurs de `qa:strict` viennent du chapitre 03, un autre lot.

**À corriger**, sur des points mineurs et mécaniques :
- R1, le registre (`etapes` de m013, m016 et m017 ; `sources` de m015 et m016) ;
- R2, la double question de m016 Q4 ;
- R3, l'explication de m015 Q11 ;
- R4, la déclaration de « débarquer » en m015 Q9.

R5 et R6 sont facultatifs. Une fois R1 à R4 appliqués tels quels, le lot est **prêt à livrer**, sans nouvelle
re-vérification : aucune clé, aucune option et aucune étiquette ne change.

## Verdict du pilote (2026-10-16)

R1–R4 et R6 appliqués (journal fr-L03/CORRECTIONS.md), registre contrôlé contre les fichiers (etapes 10/10/12/8/8). **L03 prêt à livrer.**
