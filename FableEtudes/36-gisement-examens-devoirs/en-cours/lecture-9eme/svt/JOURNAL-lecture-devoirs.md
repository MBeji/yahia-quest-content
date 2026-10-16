# Journal de lecture des devoirs D01-D06 (9e SVT, vague 1, devoir.tn)

Lecteur G2, 2026-10-16. Aucune écriture dans `gisement.json` ni `lignes.tsv` ; aucune écriture git. Sources PDF et rendus hors dépôt : `/tmp/claude-0/svtdev/src/`, `/tmp/claude-0/svtdev/render/` ; snapshots texte (contrôle anti-copie) : `/tmp/claude-0/devoirs-snapshots/svt/<id>.txt`.

## Téléchargement
- Le registre ne porte pas de champ `fichier` pour les devoirs : le PDF a été retrouvé depuis la `page` (lien `.pdf` correspondant à l'année et à l'auteur du registre dans le dossier `base/Doc/…/Sciences-SVT/Devoirs/`). `curl -g`, `CURL_CA_BUNDLE=/root/.cache/yqa-ca/ca-bundle.pem`, jamais `-k`. Le serveur coupe parfois la connexion (curl 35) : relance simple, réussie.
- Les six SHA-256 téléchargés sont identiques à ceux du registre.

| id | créneau | année | pages | sha256 (début) | lecture | lignes |
|----|---------|-------|-------|----------------|---------|--------|
| D01 | DC1 | 2016-2017 | 3 | 0fa324e69a84 | vision, 150 DPI | 4 |
| D02 | DS1 | 2021-2022 | 4 | 44cf41ea92f4 | vision, 150 DPI | 2 |
| D03 | DC2 | 2020-2021 | 7 | 84b6fdeae8be | vision, 150 DPI | 3 |
| D04 | DS2 | 2020-2021 | 4 | dad1b8079178 | vision, 150 DPI | 3 |
| D05 | DC3 | 2015-2016 | 2 | c2237d7b1558 | vision, 150 DPI | 3 |
| D06 | DS3 | 2022-2023 | 4 | b75459fef76b | vision, 150 DPI | 3 |

`pdftotext` donne un texte arabe inexploitable ; tout est lu en vision (150 DPI).

## Constats par document
- D01 : en-tête confirme le collège pilote. Le dessin du document 2 (exercice 4) est absent du PDF et la question 1 de l'exercice 4 n'est pas posée (la numérotation commence à 2) : lisibilité partielle, sans effet sur les lignes.
- D02, D03, D04, D06 : l'en-tête de chacun nomme le MÊME enseignant et la même école (« Najma »), alors que le registre les range sous trois étiquettes différentes (`mr-hajri-taoufik`, `ecole-l-etoile`, `l-etoile`, `létoile`). Quatre devoirs d'un seul auteur dans une vague de six : le plafond de deux par auteur est dépassé ; à corriger au registre (champ `auteur`, et éventuellement `college`).
- D03 : 7 pages = 4 d'énoncé + 3 de corrigé du même devoir (le registre dit 7 pages, c'est exact).
- D05 : durée imprimée de 30 minutes, trois exercices de rappel.
- Aucun exercice hors programme : aucune ligne `HP:`. Chapitres absents des six devoirs : 04, 06, 14.
- Rien d'inventé ni de deviné : tout item était lisible.

## Anti-copie
Archétypes et pièges rédigés dans mes mots, sans nombre de deux chiffres ni mot-nombre (contrôle `chk.py` : 0 problème sur les 18 lignes), sans personnage, objet, animal ni lieu.
