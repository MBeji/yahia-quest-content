# Consigne commune — lecteur du manuel SVT 3ème sec Sciences expérimentales (225333)

Ton rôle : lire un manuel officiel du CNP (Tunisie) et écrire une fiche de programme **à profondeur de génération**. Des auteurs écriront ensuite des cours et des exercices **uniquement** à partir de ta fiche, sans rouvrir le manuel.

Règles de fidélité :
- Rien d'inventé.
- « [?] » pour ce qui est illisible.
- Encadrés et synthèses recopiés verbatim.
- Tout complément de ta part est marqué « (complément du lecteur) ».

## Source
« Sciences de la vie et de la Terre — 3ème année de l'enseignement secondaire — Section Sciences expérimentales », CNP. Un seul ouvrage de 336 pages imprimées, découpé en trois fichiers PDF qui se suivent :

| Fichier | Pages imprimées | Page physique du PDF |
| --- | --- | --- |
| `/root/.cache/yqa-manuels/225333P01.pdf` | 1 à 138 | = page imprimée |
| `/root/.cache/yqa-manuels/225333P02.pdf` | 139 à 233 | = page imprimée − 138 |
| `/root/.cache/yqa-manuels/225333P03.pdf` | 234 à 336 | = page imprimée − 233 |

Dans la fiche, cite toujours les **pages imprimées**. Ne copie jamais ces PDF ailleurs ni dans git. Ne lis que les pages de ta plage.

Structure d'un chapitre (préface) : page de présentation du thème ; page de présentation du chapitre avec ses objectifs ; situation problème ; préacquis ; activités (documents, manipulations, analyse et interprétation de résultats expérimentaux) ; synthèse ; exercices. En fin de partie : « recherche » et glossaire.

## Méthode : une seule lecture par page
1. **Couche texte**, page par page : `pdftotext -layout -f N -l N <pdf> -`. La prose y est fiable. Les schémas, graphiques, tableaux et légendes de figures y sont dégradés ou absents.
2. **Image (L3)** : `pdftoppm -r 110 -png -f N -l N <pdf> $S/img-<LOT>-N`, puis lis le PNG avec Read. Supprime tes PNG à la fin.
   - `$S` = /tmp/claude-0/-home-user-yahia-quest-content/21ea1c87-32e5-565e-921d-d3c4fb5536c8/scratchpad/svt
   - Un manuel de SVT est fait de documents : **toute page qui porte un document** (schéma, photo légendée, graphique, tableau de résultats, protocole expérimental) se lit aussi à l'image, ainsi que toute synthèse et tout encadré.
   - Pour un graphique, relève les axes, les unités et les valeurs lisibles. Pour un tableau, recopie toutes les données. Pour un schéma, recopie toutes les légendes.
3. **Sondage** : au moins 1 page sur 10, parmi les plus denses, confrontée en entier au PNG et comparée à ce que donne la couche texte. Note la page et les écarts substantiels (0 attendu).

## Modèle de forme
La fiche SVT de 1ère secondaire (même discipline, même collection CNP) : /home/user/yahia-quest-content/content/programmes-officiels/programme/1ere-sec/svt.md. Lis-en une section de chapitre en entier : tu en reprends les rubriques et le niveau de détail. Pour le niveau de détail attendu sur les activités et les documents, regarde aussi une section de /home/user/yahia-quest-content/content/programmes-officiels/programme/bac-sciences-exp/chimie.md.

## Ce que tu écris pour chaque chapitre
Une section titrée :
`## T<thème>.<n> Chapitre NN — <Titre exact du manuel> (p.X–Y, transcrit à profondeur de génération)`

Elle contient :
- **Présentation et objectifs du chapitre**, verbatim.
- **Situation problème** et **préacquis**, résumés fidèlement.
- **Activités**, une par une : titre, chaque document (nature, données complètes, légendes), consigne et questions.
- **Synthèse** : verbatim, avec ses schémas bilan décrits.
- **Exercices** : chaque exercice décrit (énoncé, données, demande). Pour les QCM du manuel, recopie les items et les propositions.
- **Concepts / notions**.
- **Vocabulaire officiel** : les termes que le manuel imprime, et le glossaire de fin de partie pour les termes du chapitre.
- **Bornes de scope** : ✅ INCLUS / ⛔ EXCLU (relève d'un autre chapitre ou niveau).

Numéros de chapitre de 01 à 17, dans l'ordre du livre :
- **Thème 1, T1.1 à T1.9** : ch.01 Malnutrition, 02 Besoins nutritionnels, 03 Digestion, 04 Respiration, 05 Aliments contaminés, 06 Microorganismes au service de la production, 07 Milieu intérieur, 08 Excrétion urinaire, 09 Régulation de la glycémie.
- **Thème 2, T2.1 à T2.5** : ch.10 Des caractères aux gènes, 11 Mécanisme de l'expression, 12 Génie génétique, 13 Origine de la diversité, 14 Transmission.
- **Thème 3, T3.1 à T3.3** : ch.15 Structure et composition du globe, 16 Tectonique des plaques, 17 Évolution biologique.

Les pages de début données par les sommaires imprimés sont **à vérifier** (celle de la géologie semble décalée). Confirme chaque plage à la page près d'après les pages de titre de chapitre.

Les pages de thème (présentation, sommaire de thème, recherche, glossaire, calendrier géologique) de ta plage se résument dans tes notes. Le contenu scientifique d'une page de thème qui sert un chapitre va dans la section de ce chapitre.

## Fichiers à écrire (dans `$S`, nulle part ailleurs)
- `lot-<LOT>.md` : les sections de fiche, prêtes à coller.
- `lot-<LOT>-notes.md` :
  - (a) les plages exactes de chaque chapitre et des pages de thème ;
  - (b) les pages lues par barreau (texte / image) ;
  - (c) le sondage (pages, écarts) ;
  - (d) les incertitudes, les coquilles de la source [sic] et les pages illisibles ;
  - (e) un **slug proposé** par chapitre (`NN-mots-cles`, ascii, minuscules) et une notion d'une ligne.

Ne modifie AUCUN fichier du dépôt.

## Ta réponse finale
Un résumé court :
- les chapitres faits ;
- les plages confirmées ;
- le nombre d'encadrés et de synthèses recopiés verbatim ;
- le nombre de documents décrits ;
- le sondage ;
- tes doutes.
