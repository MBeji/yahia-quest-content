# Re-vérification — lot L02, anglais 9ᵉ (m006–m010)

> Auditeur indépendant, 2026-10-17. Branche `wip/gisement-anglais-9eme`, commit `1ed86c20` (« L02 corrections
> d'audit appliquées »). Base : `audit-anglais-L02.md` et le journal `auteurs-notes/en-L02/CORRECTIONS.md`.
> Je n'ai rien écrit dans `content/` et n'ai fait aucune opération git.

## Verdict

**Prêt à livrer** pour les cinq fichiers du lot L02. Les 14 majeurs et les 11 mineurs sont soldés : corrigés, retirés
ou déclarés. Aucune question modifiée n'a de clé fausse, et aucune fuite ne part du lot.

⚠️ **Restent cinq fuites qui partent d'AUTRES lots et donnent des clés de L02** (§ 3). Elles sont à corriger dans
L03, L04 et L06 avant la livraison commune des missions. Aucun fichier L02 n'est à toucher pour cela.

## 1. Portes

Commandes lancées depuis `/home/user/eng-en`, dont le lien `content` pointe vers `/home/user/wt-en/content` :

- `content:check` : vert (120 matières, 29 864 questions, 1 067 étiquettes).
- `content:qa:strict -- --subject english` : « no suspicious answer keys flagged », aucune erreur.
- `content:tranche -- --subject english --chapters 01,02,05` (135 questions) :
  - clé strictement la plus longue : 0/132 ;
  - positions de la clé : 23 / 29 / 24 / 23 % ;
  - paires proches : 0 ;
  - candidats gabarit : 0.

## 2. Contrôle des correctifs

| défaut | constat au commit `1ed86c20` | verdict |
| --- | --- | --- |
| D-1, D-2, d-1 m006 Q12 | contexte « old friends and neighbours, and it is time to say goodbye » ; « found » rétabli ; options et clé inchangées | OK |
| D-3 m006 Q6 | « her 15-year-old daughter » ; plus de « who » | OK |
| D-4 m007 Q1, Q7, Q8, Q10 (ex-Q11) | « still volunteers today », « still does voluntary work today », « still live next to each other », « is still trying to get one » ; le present perfect n'est plus donné en modèle dans l'énoncé de Q1 | OK |
| D-5 m007 Q10 (for/since) | retirée ; mission à 11 questions | OK |
| D-6 m007 Q5 | « Tom has problems with his ears » | OK |
| D-7 m007 Q11 / m008 Q9 | plus de « laughed at her » dans le lot | OK |
| D-8 m008 Q1 / Q4 | « Her journey started at age seven… » ; Q4 sans « grew » | OK |
| D-9 m008 Q4 | énoncé et explication de l'audit ; plus de « construction » ni de « join » | OK |
| D-10 m009 Q6 | option e « was on the balcony with his toys » ; explication sans « was playing » | OK |
| D-11 m009 Q3 | option d « Then we raised the walls… » | OK |
| D-12 m009 Q7 (because/so) | retirée ; mission à 7 questions | OK |
| D-13 m010 Q2 | énoncé sans « advise » ; options 41 / 43 / 42 / 41 ; explication de l'audit | OK |
| D-14 m010 Q6 | « One of the printed options… was "You must die of cancer." » | OK |
| d-3 m007 Q6 | « getted » (`ed-sur-verbe-irregulier`) ; les trois options officielles sont gardées ; explication juste | OK |
| d-7 m009 Q1 | d « Advice to people who want to build a house » ; f « The history of our town and its old houses » ; explication mise à jour | OK |
| d-8 m009 Q2 | option « were building… in two weeks », muette ; explication mise à jour | OK |
| d-9 m009 Q5 | clé « …that made you so unhappy » (68 caractères, à égalité avec une autre option) | OK |
| d-2, d-4, d-5, d-6, d-10 | déclarés au journal, comme demandé | OK |
| d-11 | soldé par D-13 | OK |
| étiquette `present-avec-marqueur-passe` | libellé élargi en fr, en et ar, entrée seule modifiée ; il nomme désormais exactement l'erreur des sept options de m008 | OK |
| unless (m010 Q5) | gardée, conforme à l'audit | OK |

**Re-résolution à l'aveugle des questions modifiées** — toutes conformes à la clé :

- m006 : Q6 downloads, Q12 is leaving.
- m007 : Q1 has done, Q5 learned, Q6 got, Q7 has done, Q8 have been, Q10 has written.
- m008 : Q1 grew, Q4 began, Q9 was working.
- m009 :
  - Q1 : a, c, e.
  - Q2 : built.
  - Q3 : b, e, d, a, c (ordre unique).
  - Q5 : la mère, raconter.
  - Q6 : c, e, a, d, b (ordre unique).
  - Q7 : was playing.
- m010 : Q2 cherish, Q6 obligation.

Aucun distracteur modifié n'est devenu défendable.

**Fuites à l'intérieur du lot.** J'ai relu chaque énoncé et chaque explication dans l'ordre de la route (difficultés
croissantes, base en tête) et dans l'ordre aléatoire du donjon. Il ne reste aucune fuite. Les mots ajoutés par les
correctifs ne livrent aucune clé :

- « started », « worked in building », « study » ;
- « found » : c'est le prétérit de *find*, qui ne donne pas « founded », clé de m008 Q10 ;
- « get » : c'est la base, alors que la clé de m007 Q6 est le participe.

## 3. Fuites qui partent d'autres lots vers L02 (à corriger hors lot)

J'ai confronté les fichiers déjà écrits des lots L03, L04 et L06 aux clés de L02. Cinq énoncés donnent une clé de
L02. Aucune ne se corrige dans L02, puisque la phrase officielle de L02 est la question elle-même. Correctifs proposés
pour leurs auteurs :

1. **L06, m024 (07/08) Q3** : l'énoncé finit par « …then you will regret it », ce qui donne la clé de m010 Q1. Remplacer
   par `"I ___ everyone to cherish those days because if you don't, then…"` (la fin n'est pas nécessaire à la question
   de dérivation).
2. **L04, m017 (09/12) Q9** : « because he hasn't got his ladder » donne la clé de m007 Q6. Remplacer par
   `"Jim is a painter. ___ he isn't working today because he hasn't … his ladder."`, ou par une phrase sans le
   participe, déclarée.
3. **L04, m017 (09/12) Q12** : le contexte ajouté « who have been close friends for years while Dave is moving to another
   city » donne la forme de m006 Q12 (is leaving) et celle de m007 Q8 (have been). Remplacer le contexte par
   `(Exam 2006, unique) A text about two old friends and neighbours, Dave and Jenny, who must say goodbye. Which word fits the gap?`
   La phrase officielle (« Dave and Jenny have been an important part… ») reste : c'est le texte du sujet, accepté.
4. **L03, m014 (08/07) Q1** : « After graduating, she began a new job in building and became one of the… » donne la clé
   de m008 Q4 (began) et le prétérit de m008 Q5 (became). Remplacer par
   `(Exam 2024, technical) A text about a woman builder says that, after college, she rose to the top of her trade: "…one of the (much / more / most) successful women in the industry." Which word completes the sentence?`
5. **L06, m023 (07/07) Q5** : « with each job I gained very useful knowledge » donne la clé de m008 Q6. Remplacer par
   `(Exam 2021, technical) A woman talks about her work as a car mechanic and what her jobs taught her: "That job made ___ a much stronger person today."`

Pour chaque proposition, la question visée reste soluble sans la partie retirée : le mot à trouver dépend de la seule
proposition citée. Il faut vérifier chaque correctif dans la re-vérification de son lot.

## 4. Résumé

- **Clés fausses : 0** sur les 48 questions restantes.
- **Majeurs ouverts dans L02 : 0.**
- **Mineurs ouverts dans L02 : 0** ; d-2, d-4, d-5, d-6 et d-10 sont déclarés.
- **Étiquettes :** libellé élargi ; les autres restent exactes.
- **Doublons :** gabarit m007 Q5 / Q6 levé ; m008 Q2 / m009 Q2 différenciées.
- **Portes :** vertes.
- **Verdict : prêt à livrer (L02)**, avec cinq correctifs à faire dans L03, L04 et L06 avant la livraison commune.
