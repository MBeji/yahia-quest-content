# Re-vérification — anglais 9ᵉ, lot L01 (après correction)

Objet : le commit `2c2f369f` (« L01 corrections d'audit appliquées »), comparé à `5847f87e` sur les cinq fichiers
`content/english/09-reading-comprehension-writing/exercices/06-` à `10-exam-*.json`. Le journal
`auteurs-notes/en-L01/CORRECTIONS.md` n'a servi qu'à repérer les corrections : chacune a été vérifiée sur le
diff et sur les fichiers. Je n'ai rien écrit dans `content/` et je n'ai fait aucune opération git.

## 1. Les corrections, une à une

| point | appliqué | juste | contrôle |
| --- | --- | --- | --- |
| M1 — 8 explications de verdict | oui, mot pour mot | oui | chaque explication donne le verdict et la méthode, sans dire de quoi parle la phrase ; l'explication de chaque preuve est inchangée et enseigne le contenu |
| M2 — explication de Q1 (m001, m003, m005) | oui | oui | m001 ne cite plus « give, save and spend » ni « salary for chores » ; m003 ne cite plus « set an example » ni « confidence » ; m005 ne cite plus « unpaid » et s'appuie sur « female mechanic », pas sur « young » |
| M3 — m001 Q2, énoncé | oui | oui | « explains how his children get money » ne souffle plus le verdict |
| M4 — m001 Q6, m002 Q3 | oui | oui | les citations sont vérifiées mot à mot sur le PDF (2026 G § 1, 1ʳᵉ et 4ᵉ phrases ; 2025 G § 3, 1ʳᵉ et 3ᵉ phrases) ; trois options sur quatre sont dans la citation, la clé n'y est plus seule |
| M5 — m004 Q5, explication | oui | oui | ne dit plus de quoi parle « it » (Q10) |
| m1 — m004 Q5, option c | oui | oui | « I'm trying new things » (PDF § 3 : « I'm trying new things with my own garden, too. ») ; longueurs 39/30/21/21, la clé n'est plus strictement la plus courte ; ce leurre ne prouve rien sur les cours |
| m3 — m001 Q7, « the funds » | oui | oui | « spend funds » est au § 1 ; longueurs 12/9/12/9 ; l'explication est juste |
| m4 — m005 Q6 | oui | oui | la phrase sur l'ordre est supprimée |
| m6 — m005 Q8 | oui | oui | la citation est mot pour mot celle du PDF (2024 T § 1) ; elle contient trois options (manager, unpaid, apprentice) ; Q6 garde « an … apprentice », donc rien ne fuit de Q6 vers Q8 |
| m7 — étiquette m001 Q1 | oui | oui | elle est posée sur « raised funds to help the homeless » (id `c` dans le fichier ; « b » dans mon rapport suivait la lettre du sujet) ; libellé exact |
| 4ᵉ options ajoutées | gardées et déclarées (décision du pilote) | — | aucun énoncé ne prétend donner les options du sujet ; les cinq ajouts sont faux et n'ouvrent aucune double réponse |
| m5 (m002 Q2), m005 Q3 | déclarés | — | conformes à l'audit |

## 2. Re-résolution des questions modifiées

Toutes les questions modifiées ont été résolues à l'aveugle avant de lire la clé. La clé est juste partout.

- m001 : Q1 b (taught… money values) ; Q2 False ; Q4 True ; Q6 lavish ; Q7 the doors.
- m002 : Q3 ritual.
- m003 : Q1 used music to affect people's lives ; Q2 False ; Q4 True.
- m004 : Q2 True ; Q4 False ; Q5 « that's completely fun ». « I'm trying new things » parle de son jardin, pas des
  cours : ce leurre est indéfendable.
- m005 : Q1 A young female mechanic ; Q2 False ; Q4 True ; Q6 1999 / 2006 / 1992 ; Q8 unpaid.

## 3. Fuites, recherchées après les corrections

- **Du verdict vers la preuve** : il n'en reste aucune. Les 8 explications de verdict disent seulement « a
  sentence of paragraph N says the same / the opposite ». Toutes les options de preuve viennent du paragraphe
  désigné, donc la phrase n'en désigne aucune.
- **De la preuve vers le verdict** : les énoncés de preuve restent neutres. Le seul reste vient du donjon, qui
  peut montrer la preuve avant le verdict. Il est inhérent au découpage voulu et je l'avais déjà accepté.
- **De Q1 vers la suite** : aucune clé n'est livrée. Deux échos faibles demeurent, sans gravité :
  - m001 Q6 cite « I refuse to spend funds on their wants », ce qui dément le distracteur b de Q8 (et
    l'explication de Q1, « gladly pay for his children's needs », le faisait déjà). Cela écarte un leurre, pas
    une clé : acceptable.
  - L'explication de m005 Q1, « her own business, where she trains women and men », fait écho au mot « train »
    de la preuve 2b (Q5, « where more women can train to be mechanics »). Former des clients n'est pas souhaiter
    que d'autres femmes deviennent mécaniciennes, donc le verdict n'est pas livré. Correctif **facultatif** :
    remplacer `and her own business, where she trains women and men.` par `and her own business, Caroline's Cars.`
    Le nom figure au § 2 du PDF. Ce correctif ne crée aucune fuite vers Q3 (pas de date) ni vers Q6.
- **Nouvelles citations** : celles de m001 Q6, m002 Q3 et m005 Q8 ne donnent la clé d'aucune autre question.
  « weekly Wednesday » figurait déjà dans l'énoncé de m002 Q3, et « unpaid » n'apparaît qu'en Q8, la dernière
  question.

## 4. Contrôles

`content:check` sur l'arbre partagé échoue, sur un fichier hors L01 :
`09-…/exercices/13-exams-2018-2026-the-right-word-in-context.json`, `questions.10.correctOption must match one of
the option ids`. C'est le lot d'un autre auteur, à signaler à son orchestrateur.

Pour juger L01, j'ai relancé les trois outils du moteur sur une copie du corpus dans mon scratchpad, sans ce
fichier :
- `content:check` : 120 matières validées, 0 erreur ;
- `content:qa:strict` : 0 erreur, aucun avertissement sur `english` ;
- `content:tranche --chapters 09` : pour L01, les seules clés strictement les plus longues sont les 4 « False »
  (faux positifs, admis dans l'audit) ; aucune paire proche ni aucun gabarit ne concerne L01. La paire
  `08/07#2 ↔ 09/11#5` et les deux gabarits `04/07 ↔ 09/15` relèvent d'autres lots.

## Verdict

**Prêt à livrer.** Les 5 majeurs et les mineurs retenus sont appliqués et justes. Clés fausses : 0. Citations
nouvelles fidèles au PDF : 3/3. Aucune nouvelle fuite de clé. Reste un correctif facultatif sur l'explication de
m005 Q1, qui n'empêche pas la livraison. Hors L01, le fichier 13 du ch. 09 bloque `content:check` sur la
branche : il devra être corrigé avant la PR commune.
