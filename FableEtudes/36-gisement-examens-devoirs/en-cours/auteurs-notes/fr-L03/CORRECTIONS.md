# Corrections L03 après audit à l'aveugle

Générateurs : /tmp/claude-0/fr-gis/L03/gen_m013..m017.py (réécrivent les fichiers). Contrôles : content:check, content:qa:strict (0 erreur), content:tranche 05+06, lot-lint, rendu renderLesson/renderSummary du 05 (vitest jetable, supprimé).

## Cours, résumé, registre
- 05/cours.md : ligne « espérer que / être sûr que + indicatif » dans le bloc propriete du § Subjonctif présent ; bloc propriete « choix de l'auxiliaire » après le temps de l'auxiliaire (§ Temps simples et composés).
- 05/resume.md : une incise sur espérer / être sûr / opinion affirmative (puce Subjonctif) ; une phrase sur l'auxiliaire (puce Temps composés).
- misconceptions.json : `fr.mode.subjonctif-abusif` créée (fr/en/ar du rapport d'audit). Posée sur m013 Q2 (batte), Q3 (soit), Q10 (soit capable ; s'en aperçoive) : 3 questions, jamais sur un multi.

## m013 (10 q.) : titre sans « conditionnel » ; rappels retirés de Q2, Q10, Q11 ; Q3 glose « le présent et le futur conviennent tous deux » ; Q5 « phrase abrégée » ; ancienne Q6 remplacée par 2003 a (puissent) ; ancienne Q8 retirée.
## m014 (10 q.) : Q4 option d « C'était … viendrai » ; Q6 glose « pièces de métal d'un moteur » ; Q8 formule « Dans le sujet officiel, … ».
## m015 (12 q.) : Q2 et Q10 consigne « au temps qui convient » (Q10 : annoncer donné, déclaré, [sic]) ; Q11 remplacée par 2019 G (m'avait appris ; options apprenait [anteriorite-non-marquee], apprendrait, aurait appris).
## m016 (8 q.) : Q3 (2015 G) et Q5 (2011 G a) retirées ; consignes officielles rétablies (Q1, Q2, Q4, Q6, Q8, Q10) ; Q7 = phrase officielle 2011 G avec « sera de retour … publiera » donnés, option c étiquetée anteriorite-non-marquee.
## m017 (8 q.) : Q1 retirée ; Q2 options accord (étiquette fr.accord.pp-avoir-avec-sujet) ; Q4 « a aidés » ; Q6 sans « au passé composé » ; Q7 « regarda / dit », options regardé/dis ; Q3 gardée.

## Écarts à déclarer
1. Clé la plus courte (structurel, admis par l'audit) : m014 Q4 ; m015 Q2 (désormais « présenta »), Q3, Q6, Q7 ; m017 « Aujourd'hui, Léna les aide » (a aidés). Clé la plus longue : une seule, m017 « Pendant longtemps » (ont mené ; ont travaillé), gardée sur décision du pilote (lot-lint et tranche la signalent ; structurel).
2. Paire proche 0,50 : m016 Q1 ↔ Q2 (même session 2025, même consigne officielle rétablie) : exercice parallèle voulu, données différentes.
3. Risque de défendabilité accepté sur avis d'audit : m016 Q1 « finira ; montera » (deux futurs simples après « quand ») une fois la règle retirée, couvert par la consigne officielle « selon le cas » et le modèle du cours 06 ; m015 Q11 « m'apprenait » (imparfait de l'enseignement antérieur) ; m017 Q6 options « invitait » (imparfait, jugé faux avec « Hier soir »).
4. Fuite mineure déclarée : m015 Q11 (« avait appris ») et Q12 (« avait apprises ») portent le même verbe ; Q12 teste l'imparfait/passé simple et l'accord, non la forme du plus-que-parfait.
5. m013 Q6 (2003 a) : « puissent » figure aussi dans Q9 (triple 2018) ; accepté par l'audit.

## Corrections R1–R4, R6 (re-vérification)
- R1 : gisement.json relu juste avant l'écriture, seules les entrées C19#4, C03#4, C02#4, C05#4 modifiées (etapes 10 / 8 / 8 ; sources et notes de C03#4 et C05#4 comme prescrit) ; JSON revalidé.
- R2 : m016, question 2006 : prompt entier remplacé (consigne officielle « au mode et au temps qui conviennent », une seule question). Texte vérifié contre 2006-unique.md.
- R3 : m015 Q11 : explication remplacée par le texte du rapport.
- R4 : m015 Q9 (2012 G) : consigne officielle « aux temps qui conviennent » + « débarquer » déclaré (vérifié contre 2012-generale.md).
- R6 : m013 Q2 (« présente le fait comme attendu ») et m017 (accord félicité) : « Angel » retiré.
- Aucune clé, option ni étiquette modifiée. Gates : content:check vert ; qa:strict 4 erreurs (ch. 03, autre lot, ignorées) ; tranche 05+06 inchangée (1 clé la plus longue structurelle m017, 1 paire proche 0,50 déclarée) ; lot-lint idem. R5 non faite.
