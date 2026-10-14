# Rapport — correction « clé la plus longue », SVT 9ᵉ, chapitres 09 · 10 · 11

(rédigé au fil de l'eau ; mandat `correction-cle-longue.md`)

## Chapitre 09 — `09-al-ikhraj` : 60 % (33/55) -> 0 % (0/55)

- Parade 1 (clé raccourcie, distracteurs recalibrés de même forme) sur les 33 questions ; la justification passe à l'explication, complétée quand la clé a perdu une partie (400 mL, causes du chronique, expérience du lapin, etc.).
- Paires proches (2) résolues : `02-tamrin` Q3 réécrite (ملح الطّعام 6/6/10 : filtré, ré-absorbé en partie ; clé `a`, tags conservés) ; `03-boss` Q3 réécrite (60 mL/min -> 86,4 L ; clé `c`).
- Fautes préexistantes corrigées : `01-tamrin` Q2 — énoncé « وما يطرحه كلّ منها » alors que les options ne listent que les organes (énoncé ramené à « ما أعضاء الإخراج الأربعة عند الإنسان؟ ») ; distracteurs contredits par l'énoncé remplacés (`04-defi` Q1 d, Q3 d, `06` Q1 d, Q3 d, `03-boss` Q6 b/c/d, etc.).
- Laissé : `06-defi-concours` Q2 option d « لا يمكن الحكم » (défendable à la marge, préexistante) ; répartition des positions de clé a 42 % · b 40 % · c 11 % · d 7 % (préexistante, ordre des options interdit de bouger).

## Chapitre 10 — `10-an-nudj-al-jinsi` : 66 % (33/50) -> 0 % (0/50)

- Parade 1 sur les clés longues (justification passée à l'explication : rôle hormonal, « +39/+28 », 24 h de l'ovule, etc.), parade 2 (distracteurs de même forme) sur les clés nues courtes (lieux, parties du spermatozoïde).
- Distracteurs préexistants contredits par l'énoncé remplacés : `03-boss` Q5 c/d (« المتوسّط (12-15) » / « متأخّر » pour un garçon de 9 ans), `03-boss` Q6 d, `06` Q6 d (« الجدول » alors que l'énoncé n'a pas de tableau), `05-tadrib` Q2 c (organes féminins dans une question sur le mâle).
- Doublon de fait repéré (préexistant, non flaggé par l'outil) : `quiz` Q4 ↔ `01-tamrin` Q6 (« أين يقع الإلقاح؟ », même clé) — distracteurs différenciés, pas réécrit.
- Positions de clé a 28 % · b 48 % · c 20 % · d 4 % (préexistant).

## Chapitre 11 — `11-ad-dawra-al-jinsiya` : 54 % (30/56) -> 0 % (0/56)

- Parade 1 sur les clés-justifications (expériences sur la souris, courbe de température, endomètre), justification reportée à l'explication ; parade 2 pour les clés nues (phases, durées) avec distracteurs de même forme (inversions : `01-tamrin` Q3/Q4/Q5, `03-boss` Q4, `06` Q3/Q6).
- Distracteurs préexistants contredits par l'énoncé remplacés : `06` Q4 c (« le saignement survient dans les deux cas » alors que l'énoncé dit le contraire), `04-defi` Q1 c, `04-defi` Q6 b (« الهرمونات ترتفع » contre la prémisse « من نقصان »).
- Doublons de fait préexistants (non flaggés par l'outil, clés différenciées mais non réécrits) : `quiz` Q5 ↔ `04-defi` Q2, `quiz` Q6 ↔ `04-defi` Q3, `quiz` Q7 ↔ `04-defi` Q4, `quiz` Q10 ↔ `02-tamrin` Q3 — à trancher par l'auditeur.
- Positions de clé a 36 % · b 46 % · c 14 % · d 4 % (préexistant).

## Contrôles finaux

- `content:check` : 120 matières validées, 0 erreur. `content:qa:strict` (SVT) : 0 erreur, 7 avertissements tous hors 09–11 (renvois par lettre en 02/04/05, domaine de `07-annales-subur`). `prettier --check` vert.
- `content:tranche` : 09 = 0/55, 10 = 0/50, 11 = 0/56 ; paires proches 0.
- Missions d'examen `07…09-examen-*` non touchées ; aucun fichier hors `{09,10,11}/quiz.json` et `exercices/0[1-6]-*.json`.

## Suites appliquées (audit `audit-09-11.md`)

Tout est appliqué : le BLOCKER, les 10 MAJOR et tous les MINOR. Chaque texte de l'auditeur a été vérifié avant écriture : résolution à l'aveugle, longueurs, indices de forme, cohérence avec le cours. Trois textes ont été corrigés :

- **B09-1 (09 `06` Q2)** : l'énoncé devient « شخص سليم » et `d` est remplacé par l'erreur franche proposée. Mais avec le nouveau `d`, la clé serait restée le seul « لا » face à trois « نعم », soit l'indice de polarité relevé en 12–14. `c` devient donc un « لا » à raison fausse : « لا: التّوازن يُقاس بالشّرب وحده والفارق صغير جدًّا ». Il y a désormais deux « نعم » et deux « لا ».
- **m10-1 (10 `01-tamrin` Q6)** : le nouvel énoncé dit que le pavillon a capté l'ovule, ce qui élimine à vue « في جريب المبيض ». `c` devient « في عنق الرّحم ». L'explication réfute aussi le col et le vagin.
- **m09-4 (09 `06` Q6, appliqué malgré « sans urgence »)** :
  - `b` devient « الخلل في قلّة الشّرب؛ ويكفي أن يشرب المريض أكثر » ;
  - `d` devient « الخلل في الحالبين؛ ويكفي علاج الكلية لتدفع البول بقوّة » (bon lieu, mauvais traitement) ;
  - l'explication est récrite. L'analogie de la cécité est supprimée. Elle dit maintenant que moins de 400 mL par jour est un signe d'insuffisance, pas une valeur normale.

Le reste est appliqué tel que proposé :

- **Récrits** : M09-1 à M09-4, M10-1, M10-2, M11-1 à M11-4. Les questions `quiz` Q5, Q7 et Q10 du 11 sont entièrement réécrites, la clé au même identifiant et les étiquettes conservées.
- **Corrigés** : m09-1 à m09-3, m10-2 à m10-7, m11-1 à m11-5 (l'étiquette est retirée de 11 `04-defi` Q1 `c`).
- **Non fait** : l'étiquette « possible » de m11-4 n'a pas été ajoutée, car le mandat interdit de toucher aux étiquettes.

**Explications.** Toutes les explications que j'avais allongées en queue ont été récrites en phrases complètes, sans fragments ni redites. Cela concerne environ 35 questions sur les trois chapitres. Les ajouts redondants sont supprimés (10 `02-tamrin` Q5, 10 `04-defi` Q5, 11 `quiz` Q9).

**`cours.md` du 09** : « السّامة » devient « السّامّة ».

**Points restants, non modifiés (hors mandat) :**
- `resume.md` du 09 porte la même faute (« السّامة »).
- L'énoncé de 10 `06` Q3 dit « ويومين بعدها », ce que le cours ne dit pas. À vérifier dans le manuel.

**Contrôles :**
- `content:check` : vert.
- `content:qa:strict` : 0 erreur, 6 avertissements, aucun dans 09–11.
- `tranche --chapters 09,10,11` : 0/161 clé la plus longue, 0 paire proche.
- `prettier --check` : vert.
