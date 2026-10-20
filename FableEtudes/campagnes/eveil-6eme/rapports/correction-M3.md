# Correction M3 — éveil 6ᵉ, chapitres 04, 06, 05

Tous les défauts de `audits/audit-M3.md` sont appliqués, avec les décisions du pilote. Aucun refusé. Pas de git.

## Défaut par défaut

| défaut | traitement |
| --- | --- |
| C-1 `06/06` Q4, Q5 | supprimées (décision pilote) |
| M-1 `04/06` Q7 | supprimée |
| M-2 `04/08` Q6 | supprimée |
| M-3 `04/09` (devoir m026) | fichier supprimé ; registre m026 → `ecartee` (note « coupée à l'audit M3 : redemande le patron (E-1) », champ `fichier` retiré) ; ligne « Calibré sur des devoirs publics… » retirée de `04/chapter.json` (plus aucune mission de devoir au chapitre) |
| M-4 `06/06` Q3, `06/07` Q3 | supprimées |
| M-5 `06/06` Q9 | supprimée (`06/06` : 5 q) |
| M-6 `06/07` Q9 | supprimée (`06/07` : 7 q) |
| M-7 `05/06` Q4 | supprimée |
| M-8 `05/06` Q1 | supprimée (`05/06` : 9 q) |
| M-9 `05/07` Q7 | supprimée |
| M-10 `05/07` Q8 | supprimée |
| M-11 `05/07` Q6 supprimée, Q12 remplacée par le texte de l'auditeur (clé a, sans étiquette) | appliqué |
| M-12 `05/08` Q8 | remplacée par le texte de l'auditeur (étiquettes b `eau-polluee-seulement-si-bue`, c `virus-et-bacterie-confondus`, d muette) |
| M-13 `05/08` Q10 | matching remplacé par le QCM de l'auditeur (d2, muette) |
| M-14 `05/07` Q3, Q11 | cours 05 complété (voir ci-dessous) ; Q11 gardée |
| M-15 `05/09` Q1 | remplacée par le QCM de l'auditeur (d1, option d étiquetée `eveil.eco.fleche-lue-a-l-envers`) |
| M-16 `05/09` Q6, Q7 | supprimées (`05/09` : 5 q) |
| m-1 `04/06` Q2 | `acceptedAnswers: ["سوء تغذية"]` |
| m-2 `04/06` Q6 | prémisse « متقاعد قليل الحركة » retirée |
| m-3 `04/07` Q6 | explication remplacée |
| m-4 `04/08` Q1, Q9 | phrase sur la coquille ajoutée aux deux explications |
| m-5 `05/06` Q10 | précision sur le sens des flèches du sujet ajoutée à l'explication |
| m-6 `06/06` Q6 | précision sur le sac redessiné ajoutée |
| m-7 `05/08` Q4 | « الإفادة التّالية » (singulier) |
| m-8 cours 05 | phrase sur la place des bactéries ajoutée (propriété de la section des mfakkikat) et au résumé |

Comptes finaux : `04/06` 9 q, `04/07` 9, `04/08` 8 ; `06/06` 5, `06/07` 7 ; `05/06` 9, `05/07` 9, `05/08` 12, `05/09` 5.

## Cours 05 (milieu / vivant)

Nouvelle section en tête, « 🏞️ الوسط البيئيّ: عناصر حيّة وعناصر غير حيّة », au patron (ancrage, définition d'après le guide p.143 relu à l'image, tableau, exemple résolu de l'واحة, piège, propriété, vérifie, retenir) + puce dans `resume.md`. Exemple choisi : une forêt de chênes (غزال، نمل، فطر ; تراب، ماء المطر، هواء، ضوء، حرارة), exemple résolu : une oasis, vérifie : un milieu marin. Contrôle : aucun de ces mots (غابة، بلّوط، غزال، نمل، واحة، رمل، تراب) ne figure dans le quiz ni dans les exercices 01–09 ; `05/07` Q3 (maillons de 2021) et Q11 restent donc non redonnées.

## Transcription

`examens-nationaux/6eme-base/eveil/2023-unique.md` l. 27, relue à l'image (page 1 du PDF) : « جبن وبيض وخبز وزبدة وخسّ وبرتقال وزيت زيتون » → ajouté l'œuf, et « fromage blanc » corrigé en « fromage » (le PDF imprime جبن).

## Gates

`content:check` ✓ · `content:qa -- --subject eveil-scientifique-6eme` ✓ · `content:figures:check` ✓ · `content:tranche` (04, 05, 06, `--fresh --strict-longest --strict-lessons`) ✓ : clé la plus longue 0/90, positions 26/26/28/21 %, patron 0 en recul, 1 paire proche 0,45 (`04/06` #7↔#8, exercice parallèle voulu déjà accepté) · `content:gisement:controle` sur `05/09` ✓ (0 plage ≥ 8 mots ; 2 plages à 6 mots indicatives, q1 et q4) — `04/09` n'existe plus · `programme:check` ✓ (26 warnings préexistants) · prettier `--check` ✓.

## Notes pour le pilote

- Statut du registre : j'ai écrit `ecartee` (forme des entrées de mission des autres couples, ex. math 9ᵉ), pas `ecarte` (forme des documents) ; aucun contrôle ne valide cette valeur.
- Étiquette proposée (inchangée, déjà au rapport M3) : `eveil.nutri.proteines-protegent` ; ses options (`04/07` Q6 et Q7) restent muettes. La mission `04/09` qui la portait aussi est coupée : compter ≥ 3 options n'est plus vrai (2 restantes), à juger.
- Aucune décision de programme renvoyée « à l'humain » par l'audit en dehors de celles déjà tranchées.
