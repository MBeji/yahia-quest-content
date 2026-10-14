# Corrections L05 après audit à l'aveugle (2026-10-14)

Appliquées dans `/home/user/wt-argis/content/arabic/` (générateurs du scratchpad, puis prettier).

## Critiques
- C-1 13 Q7 : énoncé « وزن صيغة التصغير », option فُوَيْعِلٌ remplacée par فُعَيِّلٌ (`alif-hukm-khalt`), explication de l'audit reprise.
- C-2 14 Q4 : énoncé « اختر كلَّ كلمةٍ هي صفةُ نسبةٍ », explication de l'audit (sans « إلى المدينة »).

## Majeurs
- M1 12 : ancienne Q6 (règle) remplacée par le duel de « الأَعْلَى » (accepté), placée avant la grille Q5 ; M-m1 : Q4 (duel de السماء) passée à d2.
- M2 05/07 Q3 : explication de l'audit.
- M3 05/08 Q5 : explication réécrite. **Écart** : le texte de l'audit contient la clé « اكْتِفَاءٌ », interdit dans l'explication d'une short_answer ; version sans la clé ni le mécanisme de Q7.
- M4 05/08 Q1 : **écart** : au lieu de « معنى فاعل » (dont la clé « المشاركة » est donnée par l'énoncé de Q4 : fuite arrière), la question demande le **وزن** de « سَاهَمَ » (فَاعَلَ), d1, sans nommer le sens.
- M5 13 Q1, Q3, Q6 : explications de l'audit ; **écart** : retrait des clés littérales « فُنَيْنٌ » et « شُوَيْعِرٌ » (short_answer).
- M6 14 Q3 : emploi correct de la nisba (العلم الوطنية = faute d'accord), options de l'audit.
- M7/M8 14 Q4/Q5 : explication de Q5 réécrite **sans** la clé « مَدِينَةٌ » (écart, même motif que M3).
- M9 06 Q4 : demande officielle rétablie (مصدر « أَحْلُمُ », clé حُلْمٌ, تَحَلُّمٌ étiqueté) — décision du pilote.
- M10 06 : items gardés (décision du pilote). Ajout au `cours.md` du 06 d'une section « تذكير: مصدر الفعل المزيد » (règle + renvoi au ch.05, exemple, `verifie`) et d'une ligne au `resume.md`. **Exception consignée** : les items de nom d'action du 06 relèvent du ch.05 par la règle du plan ; maintenus au 06 car le sujet 2026-T Q7 est un tableau unique.
- M11 01 Q2 : remplacée par الَّذِي (مبني) / يَعْمَلُ (مُعرَب), grille 2×2.
- M12 01 Q6 : option c = « مفردٌ رُفعَ بالواوِ … مثنّى رُفعَ بالألفِ ».
- M13 01 Q7 : `multi` remplacé par QCM 2×2. **Écart** : chaque option porte un suffixe descriptif (الاسمانِ مجروران بالياء…) pour que la clé ne soit pas strictement la plus longue en caractères bruts (ين = ان + un sukūn).

## Mineurs
- m2 05/08 Q4, m3 05/08 Q6, m4 13 Q4, m6 14 Q1 : textes de l'audit.
- m10 01 Q3 : d1 et placée en tête.
- m9 01 Q1 : **non appliqué** (l'option proposée « وَحِيدَتَانِ… منصوبٌ بالألفِ » doublerait le mot de l'option a) ; l'option d (جمع مؤنث) est gardée.
- m5 (13 Q5), m7 (14 Q5), m8 (12 Q3) : doublons tolérables, gardés (décision du pilote).

## Contrôles
content:check vert · content:qa 0 erreur · lot-lint propre · 0 clé strictement la plus longue (caractères bruts) sur mes QCM, tranche 05/12/13/14 à 0 % (01 et 06 : alertes sur du publié) · prettier OK · renderLesson/renderSummary du 06 sans erreur.

## Re-vérification (reverif-arabe-L05.md) — appliqué
- R-1 : corps de la section du 06/cours.md remplacé mot pour mot (propriete + exemple « حَاوَرَ » + verifie « تَعَارَفَ », sans « الفصل الخامس ») ; ligne du resume.md remplacée. **Écart** : le gate qa (é35 C-2) refuse une section qui s'ouvre sur sa règle ; ajout d'une phrase d'ancrage d'une ligne (question) avant le bloc.
- R-2 : 06 Q4 option d « حِلْمٌ » + explication. R-3 : 01 Q5 d et 05/08 Q4 d. R-4 : 01 Q2 option d « وَحِيدَتَا… » + explication. R-5 : exemples 12 Q5, 13 Q6, 13 Q7. R-6 : 14 Q2.
- Mesures : aucune clé ni la plus longue ni la plus courte sur les options remplacées. Résidu hors périmètre : 13 Q4 (فُعَيْلٌ) est la plus courte en caractères bruts seulement (non retouchée, non signalée par l'auditeur).
- Contrôles : content:check vert, qa 0 erreur, lot-lint propre, prettier OK, tranche 05/12/13/14 à 0 %, renderLesson/renderSummary du 06 : section, exemple, verifie et ligne du résumé présents dans le HTML.
