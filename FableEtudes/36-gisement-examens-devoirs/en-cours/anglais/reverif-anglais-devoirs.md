# Re-vérification — lot L05, anglais 9ᵉ (devoirs en salle blanche)

Auditeur indépendant, 2026-10-17. Arbre `/home/user/wt-en`, commit de correction `83cb6f1c`. Il ne touche que les deux fichiers du lot :
- 08/09 : +51 / −102 lignes ;
- 09/17 : 50 lignes changées.

Références :
- audit `audit-anglais-devoirs.md` ;
- journal de l'auteur `auteurs-notes/en-devoirs/CORRECTIONS.md`.

Rien n'a été écrit dans `content/` ni dans git.

## Gates (moteur `/home/user/eng-en`)

- `content:check` : vert. 120 matières, 29 872 questions : 2 de moins qu'à l'audit, ce qui correspond aux deux suppressions.
- `content:qa:strict` : 0 erreur. Aucun avertissement sur `english/08` ou `english/09` : les 506 avertissements sont tous hors lot.
- `content:tranche --chapters 08,09` :
  - clé strictement la plus longue : 12/189, aucune dans le lot ;
  - positions des clés : 22/25/29/24 % ;
  - paires proches : 15 au total, dont 12 dans le fichier 17 (contre 12 sur 22 à l'audit). Toutes sont des paires « même texte, tâche distincte », justifiées au point 2 de l'audit.
- `content:gisement:controle` (2 fichiers) : 13 textes ; 0 plage de 6 ou 8 mots ; 0 donnée commune. ✓

## Correctifs : appliqués et justes

| défaut | état | contrôle |
| --- | --- | --- |
| C1 — 08/09 Q4 recently/hired | ✓ texte de l'audit, mot pour mot | clé « has taken » unique ; vote : have ×2, has ×1, sans aux. ×1 ; taken ×2, took ×2. Le vote ne désigne pas la clé |
| M1 — 08/09 Q1 doublon du quiz 01 | ✓ question « What time (you / open) ___ … every morning? » | clé « do you open » ; 3 étiquettes exactes ; longueurs 11/15/8/13 |
| M2 — 08/09 Q2 vote | ✓ « soft » | softer ×2, more soft ×2 ; than ×2, sans ×2 ; c et d muettes |
| M4 — 08/09 Q5 doublon de 08/05 Q5 | ✓ paire bake / smaller, d3 | bake ×2, bakes ×2 ; smaller ×2, more small ×2 ; clé c (15) ni la plus longue ni la plus courte |
| M5 — 08/09 Q6 doublon de 02/04 Q4 | ✓ supprimée | l'incohérence 1962/2015 du récit disparaît ; le piège « present perfect avec un repère fini » reste en Q3 b, Q6 a, Q7 b et e |
| M6 — 09/17 Q1 horaires | ✓ supprimée, avec la phrase des horaires | voir « Texte du 17 » |
| M7 — 09/17 piège « nier » | ✓ options de l'ex-Q5, devenue Q4 | seeds ×2, tomatoes ×2 ; autumn ×2, spring ×2 ; la négation est muette, l'explication la traite |
| m1 — ex-Q7, devenue 08/09 Q6 | ✓ « traditional » et étiquette sur a | voir « Étiquette » |
| m2 — ex-Q8, devenue 08/09 Q7 | ✓ « Complete the sentence. » retiré | — |
| m4 — 09/17 Q1 (ex-Q2) | ✓ « first morning » | Thirty ×2, Ninety ×2 ; morning ×2, week ×2 ; la nouvelle explication est juste |
| m6 — 09/17 Q6 a | ✓ « free » retiré | longueurs 51 / **46** / 37 / 50 |

**Étiquette de 08/09 Q6 a** : « has had / the most traditional » porte `english.tense.present-perfect-avec-temps-fini`. L'option n'a qu'une erreur : « Before 2015 » est un temps fini, et le degré est juste. Le libellé (« present perfect avec un temps fini… : il faut le prétérit ») nomme exactement cette erreur ✓. L'option c, qui a deux erreurs, reste muette ✓.

**Texte du 17** :
- le texte est identique dans les 6 énoncés ;
- il égale le texte d'origine moins la seule phrase `The library is open from nine to noon, except on Fridays.` (contrôle par script) ;
- il fait 105 mots de corps, sans résidu d'horaire (« nine » ne subsiste que dans « ninety ») ;
- les références « The first sentence » et « The second sentence » des explications (Q2, Q4) restent exactes.

## Re-résolution (questions modifiées, à l'aveugle)

- **08/09**, toutes exactes :
  - Q1 do you open ✓ ;
  - Q2 softer than ✓ ;
  - Q4 has taken ✓ ;
  - Q5 bakes / smaller ✓ ;
  - Q6 had / the most traditional ✓ ;
  - Q7 a, c, f ✓.
- **09/17**, toutes exactes :
  - Q1 thirty / first week ✓ ;
  - Q4 new seeds in autumn ✓ ;
  - Q6 seeds twice as expensive ✓.
- **Questions non touchées** : options, clés et explications identiques à l'audit (vérifié par script).

Étages :
- 08/09 : 7 questions, rampe 1-2-2-2-3-3-3, boss 120/30 ✓ ;
- 09/17 : 6 questions, rampe 1-2-2-2-2-3, practice 75/15 ✓.

Indice de forme : seule la clé de 08/09 Q3 (« built ») est la plus courte, sans changement depuis l'audit et une seule fois dans la mission. Ce n'est pas un défaut.

## Fuites, dans les deux sens, avec m001–m024

- **Des fichiers vers les missions d'examen** : les formes neuves (do you open, softer, has taken, smaller, traditional) et le texte du 17 n'apparaissent dans aucune mission d'examen de 01 à 09 (recherche par `grep`). Les explications ne donnent que des règles générales du cours, jamais la clé exacte d'un item d'examen.
- **Des missions d'examen vers les fichiers** : aucune ne pose les données des questions neuves. Leurs explications (m006, m007, m014, m015) énoncent les mêmes règles générales, sans clé directe.
- **À l'intérieur des fichiers** :
  - plus de règle répétée trois fois ;
  - aucune explication ne résout une autre question du même fichier ;
  - 08/09 Q7 a (« every Saturday ») reste une phrase distincte de Q5 (« usually … than »).

## Verdict

**Prêt à livrer.** Le critique et les 7 majeurs sont soldés, les mineurs proposés aussi. Les clés sont justes, les grilles propres, aucun vote ne désigne une clé, et les étiquettes sont exactes. Le texte du 17 est fidèle, il n'y a aucune fuite et les gates sont verts.

Il reste deux points pour la livraison :
- au rapport de livraison, justifier les 12 paires proches du fichier 17 (texte partagé, tâches distinctes) ;
- le pilote ajoute la ligne T2′ dans `sources[]` des `chapter.json` 08 et 09.
