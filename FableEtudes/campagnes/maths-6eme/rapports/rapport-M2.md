# Rapport M2 — maths 6ᵉ, chapitres 14 et 15 (missions du gisement)

Fichiers créés (9 missions, 74 questions, conformes à la carte) — tous d3 boss 120/30 sauf le devoir (d2 practice 75/15) :

| fichier | session | q. |
| --- | --- | ---: |
| 14/exercices/06-exam-2026-p1-marchand-caisses-hausse-5-pourcent.json | 2026 P1 | 7 |
| 14/exercices/07-exam-2024-p2-club-musique-trois-tranches.json | 2024 P2 | 7 |
| 14/exercices/08-exam-2021-p1-machine-agricole-contributions.json | 2021 P1 | 10 |
| 14/exercices/09-exam-2019-p1-tableau-numerique-remise-25.json | 2019 P1 | 9 |
| 14/exercices/10-devoir-plan-et-carte-a-l-echelle.json | devoir (carte seule) | 7 |
| 15/exercices/06-exam-2026-p2-camion-voiture-reservoir.json | 2026 P2 | 8 |
| 15/exercices/07-exam-2023-p3-cycliste-montee-descente.json | 2023 P3 | 9 |
| 15/exercices/08-exam-2021-p2-voiture-camion-pause.json | 2021 P2 | 9 |
| 15/exercices/09-exam-2017-p1-fermier-lait-fraction-du-trajet.json | 2017 P1 | 8 |

`chapter.json` (14 et 15) : ligne `sources[]` des sujets officiels ajoutée ; ligne « devoirs publics » ajoutée au 14 seulement.

Vérifications : toutes les valeurs recalculées par script (assertions dans le générateur) ; chaque problème re-résolu par deux chemins (ex. 2021 P2 : vitesse 72 km/h et règle des cinquièmes ; 2026 P1 : 115 vérifié par recette 9450). `content:check` vert, `content:qa -- --subject math-6eme` 0 erreur (3 avertissements préexistants sur 14/03 et 14/04), `content:figures:check` vert, `content:tranche --strict-longest` : clé la plus longue 0 %, `lot-lint` 0 point, prettier vert, `content:gisement:controle` (devoir) : 0 plage de 8 mots.

Données données dans l'énoncé (prémisses officielles du « أثبتُ أنّ ») : 60 km (2026 P2, avant la question de la voiture), 3,2 km (2023 P3, utilisé comme donnée dans la question de la vitesse de descente). Données non officielles ajoutées pour que la question se lise seule : 144 km donné aux étapes 2021 P2 (q5, q6) ; « 1 hm = 100 m » et « 1 km = 100 000 cm » rappelés dans le devoir (hm non enseigné avant le 20).

Étiquettes employées (toutes du registre) : operation-inverse-appliquee, pourcentage-recopie-comme-resultat, pourcentage-base-erronee, numerateur-denominateur-inverses, duree-convertie-en-base-cent, duree-retenue-de-soixante-non-faite. Aucune étiquette manquante ; options à deux erreurs laissées muettes (2021 P1 « 100 % − 150 d », 2019 P1 grille 2×2, 2026 P2 « (60 − 20) × 2 ÷ 5 »). Pièges sans id au registre, donc options muettes : mauvaise tranche (2024), « 3/2 lu comme part du total » (2017), pause comptée dans le roulage, écart attribué à la table (2019), fraction de capacité confondue avec les litres.

Doutes / choix :
- Paires proches (Jaccard ≥ 0,45, 37 au 14 et 29 au 15 : au-dessus de 0,8 seules 06#2/#3 en 14 et 07#2/#3 en 15) : chaînes d'un même problème qui redonnent les mêmes données officielles (règle R1) ; non bloquant.
- Le résultat 210 d de 2019 P1 q1 coïncide avec la réponse finale : les questions intermédiaires ne le donnent pas (le reste se redérive à partir de 30 d le kilo).
- 2024 P2 q7 et 2021 P1 q1 sont des QCM de raisonnement ajoutés pour porter le piège « mauvaise tranche / deux restes » sans étiquette disponible.
- Aucun `short_answer` ni `ordering` : aucune étape du lot ne s'y prêtait (mission 14/10 sans construction).
- `content/CATALOGUE.md` non régénéré (aucun chapitre neuf).

## Corrections après audit (audit-M1-M2.md, partie M2)

- M-2 : 14/07 Q4 réécrite en « pourquoi pas la deuxième tranche ? » (quatre raisons, muettes, clé non la plus longue) ; Q7 : option « لا خطأ » remplacée par « diviser par 8 d » et par « le quotient n'est pas 136 » (muettes), clé complétée (« قسم على ثمن ساعة أمين، وساعات ياسمين في شريحة أرخص »).
- M-4 : 14/10 Q1 devient « 1 cm sur la carte représente combien de km ? » (2 km ; 0,2 / 20 / 200 en distracteurs, muets).
- M-6 : 15/06 Q6, option 60 km/h → `math.alg.reponse-a-l-autre-inconnue` ; l'option de remplissage 1200 devient 3 km/h (60 ÷ 20) ; 15/06 Q2 : « 1000 km » → « 1 km ».
- Mineurs : 14/09 Q8 « 125 % » étiqueté `operation-inverse-appliquee`, « 175 % » → « 100 % » ; 15/09 Q8 option « 6 h 43 » (impossible) → « 6 h 23 » muette, étiquette retirée, explication adaptée ; 14/06 Q3 et 14/10 Q3 (étapes redondantes) deviennent des questions de différence (200 caisses d'écart ; 13 km − 8 km = 5 km) ; 14/08 Q8 recalibrée d2 et placée avant le QCM de structure (rampe respectée) ; 15/07 : figure du parcours أ–ب–ج redessinée en SVG (ب–ج plus court que أ–ب, sans cote) dans Q2 et Q3, option Q9 « 12 > 10 » (fausse à vue) remplacée par « 48 min > moitié de 114 » ; coïncidences 210 d (14/09) et 12 min (15/08 Q9) laissées (données du sujet, déjà acceptées par l'audit) ; 15/08 Q1 laissée en QCM (toléré).
- Ids neufs du vocabulaire posés : `math.mes.trajet-aller-retour-ignore` (14/10 Q5 « 21 km »), `math.prop.vitesse-unite-de-temps-non-convertie` (15/09 Q1 « 2400 km »), `math.frac.rapport-denominateur-mal-choisi` (15/09 Q4 « 3/2 »), `math.mes.temps-d-arret-mal-compte` (15/09 Q6, les trois options fausses).
- Contrôles après correction : `content:check` ✓, `content:qa` 0 erreur (5 avertissements, hors de mes fichiers), `content:figures:check` ✓, `content:tranche --strict-longest` 0 % des deux chapitres, `lot-lint` 0 point, prettier ✓, `content:gisement:controle` (14/10) 0 plage de 8 mots. Nombres de questions inchangés (74).
