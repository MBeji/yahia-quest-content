# Mandat — corriger la fuite « clé la plus longue » d'un chapitre publié

> Mandat à donner **tel quel** à un correcteur (un par chapitre, en parallèle), en remplaçant
> `<MATIÈRE>`, `<CHAPITRE>` et `<NN>`. Né de la correction d'`arabic-8eme` (corpus #531) : ses
> quatre pièges sont ceux que l'audit B3 y a trouvés. La chaîne complète : correcteurs →
> un auditeur par chapitre en contexte vierge (mandat de la méthode, § B3) → arbitrage →
> `npm run content:gates -- --tranche` → PR → dispatch d'`apply-content.yml`. Méthode : § B2.

Deux clones côte à côte : le corpus (ici) et le moteur `../engine`, où se lancent les `npm run …` (`content/` y est le lien vers le corpus — méthode, Phase 0.1). Tu édites UNIQUEMENT `content/<MATIÈRE>/<CHAPITRE>/quiz.json` et `content/<MATIÈRE>/<CHAPITRE>/exercices/*.json`. Aucun git, aucun commit, aucun autre fichier.

**Le défaut.** Dans la plupart des questions, la bonne réponse (`correctOption`) est STRICTEMENT l'option la plus longue : elle porte sa justification, les distracteurs sont nus. Les options sont mélangées à l'affichage : seule la LONGUEUR fuit. Liste : `cd ../engine && npm run -s content:tranche -- --subject <MATIÈRE> --chapters <NN>` (réfs 1-based dans `questions`).

**Parades**, question par question (lis d'abord `.claude/skills/content-engine/references/quality-bar.md` du corpus, et le `cours.md` du chapitre) :
1. *Préférée* — raccourcir la clé à la réponse nue et laisser la justification à l'`explanation` (qui la porte déjà, sinon l'y ajouter en une phrase).
2. Quand la clé ne peut pas raccourcir — étoffer les distracteurs d'une justification de MÊME forme, FAUSSE sans ambiguïté, qui reste l'erreur plausible que le distracteur encodait déjà.

Objectif : la clé n'est plus strictement la plus longue dans aucune question touchée ; taux du chapitre ≤ 20 %. Question impossible à corriger sans risque → la laisser et dire pourquoi.

**Les quatre pièges que la relecture de la tranche 1 a attrapés — à éviter activement :**
- **La clé raccourcie doit rester VRAIE À LA LETTRE.** « الخطأ أنّ «كاد» للمقاربة » dit que l'erreur EST la règle : faux. Relis chaque clé raccourcie comme un élève qui la prend au mot (forme correcte : « الخطأ إغفال أنّ… »).
- **Ne crée pas un indice lexical.** Si tu introduis un terme (synonyme du cours, « مطابق », « في محلّ »…) dans des clés, mets-le AUSSI dans des distracteurs — sinon « l'option qui dit X est la bonne » remplace la fuite de longueur.
- **Un distracteur étoffé ne doit pas se contredire.** « بدل مرفوع » d'un mot visiblement منصوب, « مبتدأ مرفوع » sur un mot à fatha : l'élève l'élimine à vue. Fais-le se tromper sur UNE chose (la nature de la fonction), cohérent pour le reste (le cas visible).
- **Jamais de renvoi positionnel.** Une explication ne dit jamais « الأولى / الثالثة / الأخيرة » pour désigner une OPTION : l'affichage les mélange. Cite le texte. (Les phrases numérotées de l'ÉNONCÉ restent permises.) Corrige ceux que tu croises dans ton chapitre.

**Interdits absolus** : ne change jamais un `id` d'option, `correctOption`, l'ordre des options ou des questions ; n'ajoute/supprime aucune question ni option ; ne touche ni `misconceptionTag`, ni `difficulty`, ni `competencies`, ni `prompt` (sauf faute manifeste ou contradiction avec le cours : la signaler). Arabe correct, vocalisé comme l'existant, chiffres occidentaux, guillemets «».

**Vérification avant de rendre** : re-résous À L'AVEUGLE chaque question touchée (une seule juste, c'est la clé) ; `npm run -s content:check`, `npm run -s content:qa:strict -- --subject <MATIÈRE> 2>&1 | tail -3` (0 erreur), `npm run -s content:tranche -- --subject <MATIÈRE> --chapters <NN>` (taux final).

**Rapport (concis)** : taux avant → après ; pour chaque question touchée : réf, parade, ancien → nouveau (options et explication) ; questions laissées et pourquoi ; tout défaut préexistant repéré ; sorties des trois commandes.
