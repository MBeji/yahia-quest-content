# Re-vérification L06-b — m036–m038 (ch. 10), après corrections

J'ai re-vérifié le commit `a7751f47` de la branche `wip/gisement-arabe-9eme-anciennes` (arbre `/home/user/wt-ar2`) contre
`audit-arabe-L06-b.md` et le journal `auteurs-notes/ar-L06-b/CORRECTIONS.md`. Les citations ont été confrontées aux PDF
`C22`, `C18` et `C28`, lus en vision pendant l'audit. Je n'ai rien écrit dans `content/` et je n'ai fait aucune opération git.

## Gates

- `content:check` : vert.
- `content:qa:strict` : 0 erreur, aucun avertissement sur les fichiers 18, 19 et 20.
- `content:tranche --chapters 10` :
  - clé strictement la plus longue : 0/123 ;
  - positions de clé équilibrées (a 31, b 29, c 33, d 30) ;
  - 0 paire proche, 0 gabarit.
- Rendu `dir=rtl` rejoué en Chromium 1194 à 360 px, sur les 24 questions passées par `isolateLtrRuns` (aucune chaîne modifiée).
  - Les deux `multi` de m037 (Q4, Q5) et m038 Q7 (« … » dans les options a et c) s'affichent dans l'ordre du texte source.
  - Les options « ؛ » de m037 Q8 aussi.
  - Aucun défaut.

## Correctifs, un par un

| Réf. | Lieu | Appliqué | Contrôle |
|---|---|---|---|
| C1 | m036 Q8 | oui | L'énoncé et les options a et f ne parlent plus de distance : la fuite vers Q4 est fermée. Clé a, c, e re-résolue : juste. |
| C2 | m036 Q6, explication | oui | « من مكانه البعيد » a été retiré. |
| C3 | m036 Q7 | oui | La citation s'arrête à « غُبَارًا » (conforme au PDF), l'explication a été réécrite, la question reste en d3. Clé c re-résolue : juste. Le 2×2 est équilibré. |
| C4 | m036 Q3, Q4, Q5 ; `2015-technique.md` l. 51 | oui | « كَوْمَةٌ », « وَهُنَالِكَ » et « وَتَصْنَعُ مِنْهُ خَالَتَايَ عَجِينَةً مُتَمَاسِكَةً » sont conformes à C22. La transcription est corrigée. |
| C5 | m037 Q4 et Q5 | oui | Les deux questions ont des options disjointes (Q4 : مماطلة، تقليد، ألم، انبهار ; Q5 : كثرة الطلبات، حيرة، شكوى، مسؤوليّة), les 8 traits officiels sont employés. Clés re-résolues : a, c dans les deux, justes. Les deux citations de chacune sont conformes à C18, élisions comprises. Plus de miroir, et plus de fuite vers Q8. |
| C6 | m037 Q8 | oui | Le 2×2 facteur × justification est équilibré : chaque demi-réponse figure deux fois. d, qui cumule deux erreurs, est sans étiquette. Clé c juste ; l'explication dit que les deux facteurs se défendent. |
| C7 | m037 Q2 ; `2017-technique.md` l. 44–45 | oui | « جملةُ الامتحانِ: «بَذَلْتُ جَهْدِي… » est conforme au PDF (جَهدي), et la transcription est alignée. |
| C8 | m037 Q1 | oui | L'énoncé ne désigne plus les leurres, et le mot « طلبات » n'y figure pas. Clé c juste. |
| C9 | m038, l'ancienne Q7 (aujourd'hui Q6) | oui | Les options sont nues, l'explication mentionne les « services au sens large », la question passe en d2 et les questions ont été retriées (ordre des difficultés : 1, 1, 2, 2, 2, 2, 3, 3, non décroissant). Clé b, d, f juste. |
| C10 | m038, l'ancienne Q5 (aujourd'hui Q7) | oui | L'énoncé dit « تسارع التغيّر التكنولوجي » ; l'option a porte un « … » conforme à C28 ; le « … » n'est donc plus propre à la clé. Clé c juste. |
| C11 | m038 Q2 | oui | La glose « المفضيَ » est ajoutée. |
| C12 | m038 Q8 | oui | Les options d (« النموّ السكّانيّ ») et e (« تراجع دخل الأسر… ») sont remplacées et l'explication est alignée. Clé a, d, f juste : e est désormais sans ambiguïté une conséquence. |
| mineurs | m036 Q1 d, m036 Q2, étiquettes de m037 Q7 a et m038 Q4 d | oui | Le leurre facultatif de m038 Q4 n'a pas été remplacé, comme l'auteur l'a déclaré : c'était optionnel, et ce n'est pas un défaut. |

Re-résolution des questions modifiées : m036 Q1, Q2, Q4, Q5, Q7, Q8 ; m037 Q1, Q2, Q4, Q5, Q7, Q8 ; m038 Q2, Q5 à Q8. **Aucune clé fausse.**

Vote et fuites :
- Aucun vote par demi-réponse : les 2×2 de m036 Q7 et m037 Q8 sont équilibrés.
- Les deux `multi` de m037 ont des options disjointes.
- Les seules fuites restantes sont celles jugées inhérentes à l'officiel à l'audit : m038 Q1/Q4, et m037 Q7 → Q1 sur « طلبات كثيرة ».
- Le tri de m038 ne crée aucune nouvelle fuite. L'explication de l'actuelle Q6 (domaines) ne touche ni la clé de Q7 ni celle de Q8.

## Restes (deux mineurs, nés des retouches)

1. **m036 Q1, explication** : elle commente encore l'ancien leurre (« ولا ماشيةٌ ») et rien sur « حياةُ القريةِ ». Remplacer
   `وليس في النصِّ بلّورٌ ولا ماشيةٌ.` par
   `و«حياةُ القريةِ» أوسعُ من النصِّ، إذ لا يصفُ منها إلّا صنعةَ الخالتَينِ؛ وليس في النصِّ بلّورٌ.`
2. **m036 Q2, explication** : elle garde « بعدَ الفراغِ من أصعبِ المراحلِ », que l'énoncé corrigé a retiré parce que le texte ne le dit pas.
   Remplacer `وقد جاءتْ بعدَ الفراغِ من أصعبِ المراحلِ.` par
   `وقد جاءتْ بعدَ الفراغِ من تشكيلِ الأواني، وهو عملٌ يتطلّبُ انتباهًا شديدًا.`

Ces deux remplacements ne touchent que les explications. Ils ne changent ni les options ni la longueur des clés, et ils ne fuient vers aucune question : « حياة القرية » et « انتباه » n'apparaissent dans aucune autre clé.

## Verdict

**Conforme, sous réserve de deux mineurs.** Les 12 correctifs et les mineurs de l'audit sont appliqués et exacts, et les citations sont fidèles aux PDF. Il n'y a aucune clé fausse, aucun majeur restant, les gates sont verts et le rendu RTL est propre. Les deux explications de m036 Q1 et Q2 sont à aligner (texte exact ci-dessus) ; une fois faites, aucune nouvelle passe d'audit n'est nécessaire, et le lot peut être armé.

## Verdict du pilote (2026-10-18)

Les deux retouches d’explication de m036 (Q1, Q2) appliquées par le pilote ; gates verts. **L06-b prêt à livrer.**
