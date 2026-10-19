# Rapport — lot B3 (maths 6ᵉ) : 13, 14, 15, 22, 24 + neuf 26

Contrôles (depuis `/home/user/eng-deliver`) : `content:check` ✓ · `content:qa --subject math-6eme` 0 erreur sur mes chapitres (3 avertissements « valeur canonique non répétée » : le garde ne reconnaît pas les nombres groupés par U+00A0 — 800 000 ; 29 531,25 ; 31 893,75 ; les 4 erreurs et avertissements restants sont dans d'autres lots : 01, 09, 12, 16) · `content:figures:check` ✓ · `content:tranche --chapters 13,14,15,22,24,26 --fresh --strict-longest --strict-lessons` : clé strictement la plus longue 0 ; patron de notion 0 en recul · prettier ✓ · rendu `renderLesson`/`renderSummary` des 6 cours ✓ (aucun `**`/`:::`/`$$` résiduel, aucun `<em>`). Détail : `auteurs-notes/B3/NOTES.md`.

## Écarts trouvés et corrigés
- **13** : × de deux fractions absent (M1) ; le cours enseignait fraction d'une quantité / unités / tout depuis une partie, mais quiz et exercices ne testaient que « a/b × n » ; piège « 0,75 سا = 75 د » non déclaré. → section « ضرب كسر في كسر » au patron (figure 12 carreaux), titre élargi (slug intact), résumé, 21 questions.
- **14** : échelle jamais exercée ; pourcentage à base inconnue (§3.2) jamais exercé et absent du cours hors cas limite ; « الرّابع التّناسبي » absent ; 2 sections ajoutées (quatrième proportionnelle en 3 méthodes ; valeur originale inconnue par passage à 1 %, jamais ÷ 1,08 ; pas de produit en croix) ; 22 questions.
- **15** : cours complet mais exercices limités aux heures entières (minutes, comparaison, vitesse moyenne, unités, horaires non testés) ; phrase « heure d'arrivée » ajoutée ; un `**…**` coupé sur deux lignes (rendu cassé, pré-existant) recollé ; 21 questions.
- **22** : × d'une durée (indicateur officiel) jamais exercée, ni secondes, cascade, départ = arrivée − durée, jour suivant, heures décimales ; 21 questions dont 2 horloges SVG.
- **24** : déjà aligné ; manquaient entier à dénominateur (ex. 7), galette (ex. 8), non-unicité en choix multiple ; option 05-Q3 « 5/5 ولكنّها لا تساوي 1 » (même valeur que la clé) remplacée ; `**` coupé du cours recollé ; 16 questions dont 2 `multi`.
- Aucune donnée fautive des errata reprise ; rien de ⛔ (pas d'aire à l'échelle, pas de ÷ de fractions, pas de 180°, pas de moyenne).

## Questions ajoutées / remplacées
13 : +21 · 14 : +22 · 15 : +21 · 22 : +21 · 24 : +16 (+1 option remplacée) · 26 : 35. Aucun exercice > 12 questions ; en-têtes, id et ordre intacts ; questions ajoutées en fin de tri avec difficulté ≥ au maximum du fichier.

## Reprises déclarées (`manuel`)
13/03-revision ex. 4, ex. 5 ب, ex. 9 · 14/04-defi guide 502603 T2 sit. 2 (p.180, 184–186) · 15/03 ex. 7, 04 ex. 6 et 9, 05 ex. 5 (leçons 51, 53) · 22/04 ex. 5, ex. 8 · 26 : 01 ص 81, 02 ص 53, 03 ص 120, 04 ص 102–103, 05 guide T2 sit. 1.

## Chapitre neuf 26
`displayOrder` **26** : les ordres 1–24 sont contigus, aucune valeur libre « juste après 15 » ; placé en fin de sujet (26 plutôt que 25 pour laisser 25 au chapitre du lot B5). Renuméroter à l'intégration si on le veut après le 15.

## Ids d'étiquettes proposés (aucun inventé dans les fichiers)
`math.frac.produit-fractions-denominateur-conserve` (2/3 × 3/4 = 6/3 ; ch. 13, ≥ 4 questions) · `math.prop.vitesse-moyenne-des-vitesses` (moyenne de 24 et 48 ; ch. 15, ≥ 3) · `math.prop.vitesse-unite-de-temps-non-convertie` (km ÷ nombre de minutes ; ch. 15) · `math.mes.echelle-unites-non-uniformisees` (cm/m non unifiés ; ch. 14, ≥ 4) · `math.stat.graduation-comptee-comme-unite` (compter les traits ; ch. 26, ≥ 3).

## Doutes pour l'auditeur
- Ch. 14 passe à **10 sections** (> ~8 notions, course-explanation R-13) : proposer de scinder « السلّم » (déjà soulevé par la fiche §2 sexies, écart 11).
- Ch. 26 : paires proches (≈ 22) = questions successives sur **un même document** (même figure, même préambule) par construction ; compétence empruntée `math.stat.effectifs-frequences` (registre orienté 9ᵉ) ; catégories en lettres أ ب ج د (pas de prose arabe dans les figures) ; la 04-defi utilise les lectures corrigées au R-7 (pas les étiquettes parasites).
- Ch. 22 : lecture d'horloge sans aiguille des secondes ; deux horloges dessinées par script (2 h 45, 8 h 20), aiguille des heures épaisse, précisée dans l'énoncé.
- Ch. 13 : 02-boss Q10 ≈ cours (rectangle 3/4 × 2/3) — mêmes nombres que l'exemple 1 ; volontaire (rappel).
- Un script de gabarit a produit les options (`key` placée aléatoirement) ; positions de clé sur les nouvelles questions : 13 → 20/27/27/27 %, 26 → 15/31/27/27 %.
