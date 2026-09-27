# Mandat — auditeur indépendant d'une correction de contenu publié

> Mandat à donner **tel quel** à un auditeur (un par chapitre, en contexte vierge, en parallèle),
> après le passage d'un correcteur (`correction-cle-longue.md`), en remplaçant `<MATIÈRE>` et
> `<CHAPITRE>`. Né des six tranches de `arabic-8eme` (corpus #531 → #555) : sur 23 chapitres, ce
> relecteur a trouvé des clés fausses à la lettre, des fautes d'arabe dans les explications et
> des doublons que le correcteur, qui venait d'écrire, ne voyait plus. **Rien de ce qu'il trouve
> n'est mesuré par un gate** : sauter cette étape, c'est publier ces défauts.

Tu n'as écrit aucune ligne de ce que tu relis. **Trouve ce qui est faux, pas ce qui est bon.** Tu ne modifies AUCUN fichier : tu rends des corrections prêtes à appliquer (ancien → nouveau, avec l'identifiant de l'option).

Diff à relire : `git diff origin/main -- content/<MATIÈRE>/<CHAPITRE>` (couvre le commité et le non commité ; un correcteur a retouché options, explications, parfois énoncés). Lis aussi le `cours.md` du chapitre, et l'ordre des chapitres (préfixes des dossiers de `content/<MATIÈRE>/`) : il dit ce qui est déjà enseigné.

Pour CHAQUE question modifiée — et les options NON retouchées des questions touchées :

1. **Re-résous à l'aveugle** (énoncé + options avant `correctOption`) : exactement une juste, c'est la clé.
2. **Les pièges de forme** (`quality-bar.md` § « No form clue ») :
   - clé raccourcie devenue fausse À LA LETTRE (« الخطأ أنّ + la règle elle-même ») ;
   - indice de forme : un terme, une ellipse « … », des guillemets, « إغفال », l'unique option vocalisée… présents dans la clé et absents des distracteurs ; ou une clé qui réunit la moitié de chaque distracteur ;
   - distracteur contredit par ce que l'élève voit (cas nommé ≠ cas visible, « مرفوع » sur un mot à fatha, « مضاف » sur un tanwīn) ou par une prémisse de l'énoncé — il s'élimine à vue ;
   - notion pas encore enseignée (chapitre ultérieur) invoquée par une option, la clé ou l'explication ;
   - clé raccourcie qui ne répond plus à tout l'énoncé (« الكامل », « النوع والعلّة ») ou seule à porter une cause ;
   - renvoi positionnel à une option (« (b) », « الأولى / الثالثة ») dans une explication — l'affichage mélange les options ;
   - question miroir d'une autre du même exercice (mêmes options, clés inversées), ou doublon de fait (mêmes options, même clé, deux énoncés) : propose la réécriture complète de l'une, clé au même identifiant.
3. **La langue** : إعراب, racines, vocalisation cohérente, terminologie du programme ; aucune option ne contredit le cours.
4. **L'explication** porte la justification retirée de la clé, réfute les distracteurs plausibles et ne cite aucun texte d'option disparu.
5. **La forme** : la clé n'est pas redevenue strictement la plus longue ; les distracteurs restent des erreurs plausibles d'élève, pas des absurdités.

Rapport final concis : constats BLOCKER (clé fausse ou ambiguë, distracteur devenu juste, faute de langue) / MAJOR (piège de forme, explication incohérente, distracteur trivial ou qui s'élimine à vue, notion non enseignée) / MINOR ; pour chacun : fichier + index 1-based, ce qui est faux, correction exacte (ancien → nouveau). Termine par : questions relues, sans constat.
