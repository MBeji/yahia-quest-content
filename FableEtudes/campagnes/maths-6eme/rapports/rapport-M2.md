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
