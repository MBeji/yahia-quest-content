# Journal de lecture des devoirs D01-D09 (6e anglais, vague 1, devoir.tn, école primaire)

Lecteur G2, 2026-10-18. Sources web : rien n'est repris, aucune transcription versionnée. Sorties : `lines/D01..D09.tsv` et `.meta`, snapshots hors dépôt `/tmp/claude-0/devoirs-snapshots/english-6eme/<id>.txt`, rendus à 80 DPI dans `/tmp/claude-0/en6dev/`. Aucune écriture dans `gisement.json`, `content/` ni git. Conventions : § 0 de `lecture-9eme/anglais/JOURNAL-lecture-C01-C06.md` et du journal des devoirs 9e, étendues ci-dessous (§ « Conventions nouvelles »).

## Téléchargement
- Copies lues : `…/scratchpad/snapshots/devoir.tn/D01..D09.pdf` (aucun téléchargement refait). **Les neuf sha256 égalent le registre**, les neuf nombres de pages (3, 3, 3, 2, 2, 2, 4, 4, 2) aussi.
- `pdftotext -layout` : couche texte propre sur les neuf PDF ; vérification en vision (80 DPI) des pages à images ou à tableaux (D01 p. 2, D02 p. 1-2, D03 p. 1-2, D04 p. 1-2, D05 p. 2, D07 p. 3, D09 p. 1-2) : lecture déclarée `mixte`.

| id | créneau | sha256 (début) | pages | lecture | lignes | auteur imprimé | établissement | année imprimée |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D01 | DS1 | 1acac6ef | 3 | mixte | 6 | Mme Nawel Mathlouthi | école privée « Success Academy » (Mourouj 6) | décembre 2020 (2020-2021) |
| D02 | DS1 | c45d35d7 | 3 | mixte | 5 | Wissal MB | école primaire de Birine | décembre 2020 |
| D03 | DS1 | 213b8941 | 3 | mixte | 5 | Faten Messaoudi | école primaire Northern Ouled Youssef | 2020-2021 (premier trimestre) |
| D04 | DS2 | 72890462 | 2 | mixte | 5 | aucun | aucun | aucune |
| D05 | DS2 | 373769c3 | 2 | mixte | 4 | B. Abdeljawed (Samir) | école Hay Jadid | 2e trimestre 2014 |
| D06 | DS2 | 99cd151b | 2 | mixte | 7 | B. Amor Nasra | école F. Hached | mars 2015 |
| D07 | DS3 | 3b762953 | 4 | mixte | 7 | Khaled Mansouri | The Pilot School | mai 2019 |
| D08 | DS3 | c3e7e4f4 | 4 | mixte | 7 | Khaled Mansouri | The Pilot School | mai 2019 |
| D09 | DS3 | 355d230c | 2 | mixte | 5 | aucun | aucun (case vide) | aucune d'épreuve ; 2007 = date d'une lettre dans le texte |

Total : **51 lignes**. `content:gisement:lignes --subject english-6eme --grade 6eme-base` : 9 fichiers, 51 lignes valides, 0 fautive. Contrôle automatique anti-copie (suites de trois mots, archétypes et pièges contre les neuf snapshots) : 0 coïncidence.

## Conventions nouvelles (le premier lot des devoirs 6e les fixe)
- **Créneau** : le registre note T1, T2, T3 (trimestres du primaire) et le validateur n'accepte que DC/DS : correspondance **T1 → DS1, T2 → DS2, T3 → DS3** (épreuves de fin de trimestre, imprimées « exam », « term test » ou « test n° » de décembre, mars-avril, mai). À retenir pour le pilote dans `lignes.tsv`.
- **Grain** : une ligne par exercice numéroté imprimé ; la compréhension écrite est une ligne n°1 ; la dernière ligne est la production quand il y en a une. **Cas nouveau** : les rubriques nommées « Writing » de D03, D04, D06 et D09 ne contiennent que des exercices de langue (remise en ordre, grille, orthographe) : une ligne par exercice, aucune ligne de production dans ces quatre devoirs ; D05 n'a ni compréhension écrite ni production.
- **Écoute** (D03 : 4 points, D05 : trois consignes) : une ligne n°1, notée « sans objet » dans l'archétype (l'appli n'a pas d'audio) ; les chapitres suivent le thème (règle D2) ; le script est imprimé dans les deux devoirs. Étapes = nombre de consignes ou de questions numérotées.
- **Barème** : celui de l'imprimé ; `-` quand rien n'est imprimé (D04, D05, D09 en entier). Décimaux gardés (1.5, 2.5).
- **Étage** : `d1` application directe (retrouver, choisir, apparier, nommer) ; `d2` correction ou justification, remise en ordre de questions, appariement sur plusieurs notions, production guidée ; `d3` jamais (aucune production libre longue). Aucun `d4`.
- **Chapitres** : une ligne prend les chapitres d'**unité** dont au moins un item teste la notion ou le thème (01 loisirs, -s du présent, possessifs, on/in ; 02 can, how many, nourriture ; 03 météo et mois ; 05 fêtes ; 06 vêtements et nombres ; 07 a/an/the, salutations, carte postale de ville), puis un jeton `HP:` pour chaque notion ou thème hors guide testé par au moins un item. Lecture et production : chapitre de l'unité du thème, à défaut `HP:theme-hors-unites` (règle D2).
- **Mots-clés HP fixés** : `HP:theme-hors-unites` (thèmes absents des sept unités : famille, identité et nationalité, corps, maison, objets de classe, ferme, actions illustrées) ; `HP:present-continuous` ; `HP:have-got` ; `HP:demonstratives` (this/these) ; `HP:there-is-are` ; `HP:question-words` (how old, what, who, where, when hors « how many ») ; `HP:word-order` (remise en ordre de mots : toujours ajouté aux exercices de ce type, avec les chapitres de la notion visée) ; `HP:spelling` (correction ou remise en ordre de lettres) ; `HP:opposites-synonyms` ; `HP:days-of-week` ; `HP:pronunciation` (intrus au son).
- Hors HP, rangé en unité : « how many » → 02, « can » → 02, nombres → 06, vêtements et couleurs de vêtements → 06, météo et mois → 03, adjectifs possessifs → 01 (liés à 04 aussi, 01 retenu).

## Écarts au registre
- **Auteurs** : le registre dit « anonyme » pour D04, D05, D06, D09. L'imprimé signe **D05 (B. Abdeljawed, école Hay Jadid, 2014)** et **D06 (B. Amor Nasra, école F. Hached, mars 2015)** ; seuls **D04 et D09** n'ont ni nom ni établissement. Le registre note `auteur: ecole-primaire-de-birine` pour D02 : l'imprimé donne l'enseignante (Wissal MB) et l'école.
- **Années** : D05 = 2014 et D06 = 2015 (registre : null) ; D04 non datable ; D09 : la seule date (2007) est celle d'une lettre dans le texte, non de l'épreuve ; D02 imprime décembre 2020, le registre dit 2021 (fin d'année scolaire, convention des devoirs 9e). Date de création des PDF (août 2016 pour D05, D06 et D09 ; décembre 2019 pour D04) = date de numérisation, pas d'écriture.
- **D01** : une école privée de soutien (« Success Academy ») rangée dans la rubrique primaire : pas d'effet sur le contenu.
- **D07 et D08** : le registre déduit « école pilote » du nom de fichier ; l'imprimé imprime bien « The Pilot School » ; même enseignant, même session de mai 2019, numérotés 15 et 14 sur la page de liste, sans numéro imprimé.
- **D02** : note imprimée sur 20 alors que 4 + 5 + 3 = 12 points. **D03** : note sur 12, cohérent. **D04, D05, D09** : aucun barème.
- Créneaux : D01 « test n°1 » (décembre), D02 « test n°1 » (décembre), D03 « premier trimestre », D05 « 2nd Term », D06 « Second Term test », D04 « test n2 » (supposé T2, d'après le registre), D07 et D08 « English Exam » de mai, D09 « test n° 3 » : concordants avec T1/T2/T3 pour les sept datés ou numérotés ; D04 repose sur le seul classement du site.
- Coquilles d'impression dans les énoncés (D01 « ciblings », D04 « Englich », D08 « a old », D09 « Who I in the kitchen ? », « QUETIONS ») : sans effet sur les lignes.
- Pages : D01 filigrane de l'école ; D03 le script d'écoute est en dernière page ; D05 le script est en tête de la page 1.

## Plafond par auteur (au plus deux)
Les « quatre anonymes » du registre se réduisent à **deux sur l'imprimé** (D04, D09), sans lien établi : présentation, sections et exercices différents (D04 en sections « Reading / Language / Writing » sur des vêtements et le corps, D09 en lettre de vacances et exercices de maison), PDF sans métadonnée d'auteur. Même si D04 et D09 venaient d'une même main, le plafond de deux serait respecté. **Auteurs identifiés** : Mathlouthi (D01), Wissal MB (D02), Messaoudi (D03), Abdeljawed (D05), Amor Nasra (D06), **Mansouri (D07 et D08 : deux, plafond atteint)**. Aucun auteur n'a plus de deux devoirs. Pour la vague 2 : exclure Mansouri.

## Programme : « Learn and Grow » ou ancien ?
- **Ancien, sans exception.** Les devoirs datés vont de 2014 à 2021 ; D09 porte la date 2007 dans son texte ; D04 n'est pas daté. Les sept unités du guide (loisirs, forme, saisons, entraide, fêtes, achats, tour du monde) ne sont jamais le sujet d'un devoir : on y trouve identité et famille, nationalités, corps, vêtements et couleurs, jours, routine, maison, fable, carte postale de ville. Seuls les recoupements partiels (vêtements, nombres, routine et loisirs, météo, how many, can, a/an) rattachent des lignes aux unités. Toutes les `.meta` portent `programme: ancien`.
- Pas de contre-indication de date : D01 à D03 (2020-2021) sont antérieurs à 2022-2023, première année possible de « Learn and Grow ».

## Format des devoirs
- **Synthèses de 6 + 8 + 6 = 20** : D06 (4 questions de compréhension, 3 exercices de langue 3 + 3 + 2, production en trois exercices 3 + 2 + 1), D07 (6 + 8 + 6, avec une carte postale guidée de 4 points), D08 (6 + 8 + 6, réponse à une carte postale modèle de 4 points). D01 : 8 + 6 + 6 = 20 (compréhension, langue en quatre exercices, production d'un paragraphe de 6 points).
- **Épreuves courtes** : D02 (4 + 5 + 3 = 12 sous une note sur 20), D03 (4 d'écoute + 5 de langue + 3 = 12 sur 12), D04, D05 et D09 sans barème (deux à quatre exercices).
- **Production écrite** : D01 (paragraphe de présentation), D02 (courriel), D07 (carte postale à compléter), D08 (carte postale en réponse) ; aucune dans les cinq autres.
- **Écoute** : D03 et D05 (script imprimé dans les deux), jamais de bande son jointe.

## Notions par chapitre (nombre de lignes sur 51)
- **01-entertaining-myself** : 9 (D06-3, D07-1/2/3/6, D08-1/2/3/6). **02-keeping-fit** : 3 (D04-5, D07-5, D07-6). **03-having-fun-in-the-seasons** : 3 (D08-5, D09-1, D09-5). **04-caring** : **0**. **05-celebrations** : 1 (D06-1). **06-going-shopping** : 9 (D02-3, D04-1/3/4, D05-1/4, D06-2/6, D08-5). **07-around-the-world** : 4 (D03-5, D06-3, D07-7, D08-7).
- Chapitres **jamais travaillés** : 04-caring, et très peu 05 et 03. Ne ressort pas du tout : l'impératif, le superlatif, le comparatif, will/won't, should/must et le simple past : les devoirs de cette liste n'enseignent pas les structures du guide.
- **Part HP** : **39 lignes sur 51 portent un jeton HP (76 %)**, dont 25 entièrement HP et 14 mixtes (unité + HP). Détail des jetons : `theme-hors-unites` 18, `present-continuous` 7, `word-order` 5, `spelling` 5, `question-words` 5, `opposites-synonyms` 3, `demonstratives` 2, `have-got` 2, `there-is-are` 2, `days-of-week` 1, `pronunciation` 1. Les devoirs récents (2020-2021, D01 à D03) sont les plus hors guide ; D07 et D08 (2019) sont les plus proches des unités.
- **Archétypes dominants** : lire un petit texte puis cocher, corriger, compléter (7 devoirs sur 9) ; apparier questions et réponses (D05, D07, D08, D09) ; remettre en ordre des mots ou des lettres (D01, D03, D04, D06, D07, D09) ; contraire et synonyme (D06, D08, D09) ; carte postale de ville (D07, D08).

## Difficultés
- Aucune illisibilité. D05 et D09 n'ont aucun barème : la répartition des points est inconnue. D05 : « Mike likes English » dans une question d'écoute d'un texte qui ne nomme pas Mike ; rapproche l'écoute d'un script non fiable.
- Rattachement des lignes de langue mêlant structures hors guide et unités : voir les jetons multiples ; les appariements de phrases (D08-5, D09-3) cumulent trois ou quatre jetons.
- Anti-copie : archétypes et pièges rédigés en français dans mes mots, sans nombre, nom propre, objet ni contexte de la source.
