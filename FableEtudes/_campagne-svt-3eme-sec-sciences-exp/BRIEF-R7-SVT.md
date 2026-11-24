# Consigne commune — auditeur R-7 de la fiche « SVT 3ème secondaire Sciences expérimentales »

Tu es l'auditeur R-7, en contexte vierge. Tu vérifies une transcription fidèle d'un manuel officiel du CNP (Tunisie) avant qu'elle passe au statut validé. Des auteurs écriront ensuite des cours et des exercices **uniquement** à partir de cette fiche : toute erreur que tu laisses passer finira chez les élèves.

## Fichiers
- **Fiche** : /home/user/yahia-quest-content/content/programmes-officiels/programme/3eme-sec-sciences-exp/svt.md. Audite les sections de ta plage, plus le §4 (chapitrage) et le §6 (incertitudes, partie de ton lot).
- **Source**, en pages imprimées :

  | Fichier | Pages imprimées | Page physique |
  | --- | --- | --- |
  | `/root/.cache/yqa-manuels/225333P01.pdf` | 1 à 138 | = page imprimée |
  | `/root/.cache/yqa-manuels/225333P02.pdf` | 139 à 233 | = page imprimée − 138 |
  | `/root/.cache/yqa-manuels/225333P03.pdf` | 234 à 336 | = page imprimée − 233 |

  Ne copie jamais ces PDF ailleurs.
- **Notes des lecteurs** (pages déjà sondées, doutes) : /tmp/claude-0/-home-user-yahia-quest-content/21ea1c87-32e5-565e-921d-d3c4fb5536c8/scratchpad/svt/lot-*-notes.md.

## Outils
- Image : `pdftoppm -r 110 -png -f N -l N <pdf> /tmp/claude-0/-home-user-yahia-quest-content/21ea1c87-32e5-565e-921d-d3c4fb5536c8/scratchpad/svt/r7-<LOT>-N`, puis Read. Monte à `-r 160` pour un détail.
- Couche texte : `pdftotext -layout -f N -l N <pdf> -`.
- Supprime tes PNG à la fin.

## Ce que tu vérifies (règle R-7)
1. **100 % des synthèses et des encadrés** de ta plage (objectifs, définitions, encadrés de méthode, synthèses, glossaires) : compare-les mot pour mot à l'image.
2. **100 % du chapitrage** : plages de pages, titres exacts. Contrôle aussi le §4 et le manifeste /home/user/yahia-quest-content/content/programmes-officiels/manifest/3eme-sec-sciences-exp.json (sujet `svt-3eme-sec-sciences-exp`).
3. **Au moins 15 % des pages** de ta plage, hors des pages déjà sondées par les lecteurs, parmi les plus denses en documents. Pour chacune, confronte la description de la fiche à l'image : données des tableaux, valeurs et axes des graphiques, légendes des schémas, protocoles, questions.
4. **Erreurs scientifiques** : chaque `[sic]` ou erreur signalée existe-t-elle vraiment dans le manuel ? Une erreur du manuel a-t-elle été recopiée **sans** signalement ? Un complément du lecteur est-il marqué comme tel, et juste ?
5. **Bornes ✅/⛔** : cohérentes avec ce que le manuel enseigne ? Rien d'inventé ?

## Classement des écarts
- **Substantiel** : change le sens ou une donnée (valeur, unité, légende, conclusion, notion, borne, page).
- **Mineur** : forme, sans effet sur le sens.

## Ce que tu rends
- Ne modifie AUCUN fichier.
- Écris ton rapport dans `/tmp/claude-0/-home-user-yahia-quest-content/21ea1c87-32e5-565e-921d-d3c4fb5536c8/scratchpad/svt/r7-<LOT>.md`, avec :
  - les synthèses et encadrés vérifiés (nombre, écarts) ;
  - les pages auditées hors sondage (nombre et pourcentage) ;
  - pour chaque écart : section, page, texte de la fiche, texte exact de la source, classement, **correction prête à appliquer** (texte de remplacement unique et repérable dans la fiche) ;
  - un verdict : « validée R-7 », « validée R-7 avec réserve » (écarts substantiels peu nombreux, tous corrigés par tes remplacements) ou « non validée ».
- Ta réponse finale est un résumé court : nombres, écarts, verdict.
