# Re-vérification ciblée : lot L12 (m033–m037)

Auditeur de L12. Objet : les correctifs appliqués par l'auteur au commit `03440b15` dans les cinq fichiers
du lot (05/09, 05/10, 05/11, 11/10, 12/11), contre `audit-svt-L12.md`. Rapport écrit au fil de l'eau ;
aucune écriture dans `content/` ni dans git.

Périmètre vérifié : les cinq fichiers du lot au commit `03440b15` (arbre de travail propre sur ces cinq
fichiers). Le journal de l'auteur (`auteurs-notes/svt-L12/CORRECTIONS.md`) a été lu pour ses écarts déclarés.

## m033 (05/09, 8 q.)

Textes de l'audit retrouvés **mot pour mot** : glose neutre en Q1 (phrase seule), Q2 et Q4 ; Q1 a et ajout
à l'explication ; Q3 (jour 100, clé 45, explication) ; Q5 b et phrase d'explication ; Q7 sans les deux
parenthèses, Q7 d ; Q8 a et phrase sur les aliments protecteurs.

Re-résolution à l'aveugle : Q1 b · Q2 c · Q3 45 · Q4 a · Q5 d · Q6 a, b, c · Q7 b · Q8 c : **toutes
conformes**. Q1 a est réfutée par le tube 1 témoin ; Q5 b (deux courbes « sans lien ») est réfutée par la
simultanéité des variations ; Q8 a (protides « protecteurs ») est réfutée par le cours 04. Aucune clé
strictement la plus longue ni la plus courte.

- **[MINOR] Fuite d'explication vers Q2 (préexistante, manquée à l'audit).** Les explications de Q7 et Q8
  disent « والعنصر (×) ليس سكّرًا ولا دهنيّة » : dans le donjon, après Q7 ou Q8, Q2 se réduit aux acides
  aminés. Sur la route, Q2 (d2) passe avant : pas d'effet. Correctif exact : Q7, remplacer « والعنصر (×) ليس
  سكّرًا ولا دهنيّة حتّى يُحصر في دور الطّاقة » par « ولا شيء في المقارنة يحصر دور العنصر (×) في الطّاقة » ;
  Q8, supprimer la dernière phrase « والعنصر (×) ليس سكّرًا ولا دهنيّة. » (le raisonnement tient sans elle).

## m034 (05/10, 8 q.)

Q2 et Q8 de l'audit supprimées ; les questions sont renumérotées (Q3 → Q2, …, Q10 → Q8). Textes retrouvés
mot pour mot : Q4 (ex-Q5 : énoncé, a, c), Q5 (ex-Q6 : les cinq items), Q7 (ex-Q9 : a), Q8 (ex-Q10 : mcq
calcium, options, étiquettes, explication), Q2 (ex-Q3 : « ونترات الفضّة لا تكشف عن السّكّر » ; « مختزلة »
retiré), Q7 (« فيه سكّر »).

Re-résolution : Q1 b · Q2 c · Q3 d · Q4 a · Q5 a-b-c-d-e · Q6 c · Q7 b · Q8 c : **toutes conformes**.

**Écart 4 : Q8, mcq officiel du calcium.** Fidèle : la transcription 2015, ex. 1, item 3, donne exactement
« نكشف عن أملاح الكلسيوم بإضافة : أ. محلول فهلنق السّاخن ب. ماء اليود ج. أكسلات الأمونيوم د. نترات الفضّة », dans
cet ordre ; la clé du sujet est ج, celle du fichier c. Ce n'est **pas un doublon** : aucune question du chapitre
04, de son quiz ni du chapitre 05 n'a la clé « calcium → oxalate » (04/05-tadrib Q1 a la clé « chlorures →
nitrate d'argent », 04/01-tamrin Q1 « amidon → eau iodée », mêmes quatre réactifs). Aucune fuite vers Q2 :
l'explication ne dit pas ce que révèle Fehling.
- **[MINOR] Étage honnête.** Item de rappel pur, du niveau des QCM d1–d2 de la vague 1, marqué d3.
  Correctif : `"difficulty": 2` (question neuve : aucune identité à préserver ; le compilateur la placera
  après Q2).

**Écart 1 : Q4, « سكّر ذائب » sans « بسيط ».** C'est bien le texte de l'audit, mais il crée un défaut que
l'audit n'avait pas vu :
- **[MAJOR] Q4 : deux réponses défendables.** Lue seule, la question ne dit plus que l'élément ب est simple :
  « سكّر ذائب في الماء » peut être le سكّر الشّعير (soluble, sucre). Avec du maltose, b (« تفكّكه عصارات المعي
  الدّقيق إلى مغذّيات أبسط منه… ») devient juste et la clé a (« لأنّه بسيط ») fausse ; rien dans l'énoncé ne
  tranche. Le correctif de l'audit était défectueux. Correctif exact (énoncé seul ; options inchangées) :
  « (مناظرة 2017) ابتلع شخص 100 غ من مغذٍّ خلويّ ذائب في الماء (العنصر ب)، ثمّ قيست كمّيّة هذا العنصر في
  مواضع من الأنبوب الهضميّ: » (suite inchangée). « مغذٍّ خلويّ » est le terme du cours 05 pour les produits
  finaux de la digestion : b ne nie plus une donnée lue, elle exécute l'erreur nommée par son étiquette (prendre
  un nutriment final pour un aliment à digérer). La clé reste 102 car., seule et non la plus longue. Fuite
  résiduelle vers Q3 (ب n'est pas de l'amidon) : moitié faible du 2×2, déjà admise.

## m035 (05/11, 7 q.)

Q6 et Q9 de l'audit supprimées ; Q7 → Q6, Q8 → Q7. Textes retrouvés mot pour mot : Q2 d et glose ; Q6 b, d
et fin d'explication ; Q7 énoncé et membres droits.

Re-résolution : Q1 a, b, e · Q2 c · Q3 b · Q4 d · Q5 a · Q6 b · Q7 l1-r3, l2-r1, l3-r2 : **toutes conformes**.
L'appariement n'est plus soluble par le produit : chaque séquence de sucs est unique (lipides : sucs
pancréatique et intestinal seuls ; amidon : salive d'abord ; protides : suc gastrique d'abord).

**Écart 2 : glose de Q1 alignée sur la version neutre.** Accepté : la glose d'origine (« سلسلتها من الأحماض
الأمينيّة ») ne fuyait vers aucune clé de cette mission, mais l'alignement est sans effet sur la clé de Q1 et
harmonise le chapitre.

**Écart 3 : Q6 a et c allongées.** Justifié : avec mes textes, la clé b (98) aurait été **strictement la plus
longue** (a 94, c 92) ; mon décompte de l'audit (« 2ᵉ plus longue ») était faux, l'auteur l'a corrigé. Le
remplissage de c est en revanche maladroit :
- **[MINOR] Q6 c : « في الدّم نفسه تمامًا ».** Le « تمامًا » final n'a pas de sens dans cette phrase. Correctif
  exact (105 car. ; clé b 98, a 108, d 97 : la clé reste 3ᵉ sur 4) : « فقد المعي 83 غ وكسب الدّم 88 غ، والفرق 5 غ
  صنعها الدّم بنفسه من مواد أخرى: ظاهرة تركيب المغذّيات في الدّم » (étiquette inchangée). L'ajout de a (« في
  المعي ») est correct.
- **[MINOR] Q6 → Q4, faible.** Les options b et d de Q6 (« عبرت جدار المعي إلى الدّم، أي الامتصاص / الإفراز »)
  désignent l'option d de la définition (Q4). C'est la définition du cours, demandée en d2 : acceptable,
  signalé pour mémoire.

## m036 (11/10, 6 q.)

Q6 de l'audit supprimée ; Q7 → Q6. Textes retrouvés mot pour mot : titre « 🏛️ مناظرتا 2009 و2015 · بطانة الرّحم
وطوراها المتزامنان ⭐⭐ » ; Q2 b, c, d (propositions du sujet 2009) ; Q5 c ; Q6 membres gauches sans jours ;
repère 6 `x2="131" y2="142"`.

Re-résolution : Q1 (1 قناة البيض, 2 المبيض, 3 قمع فالوب, 4 المهبل, 5 العضليّة, 6 البطانة) · Q2 a · Q3 (1 غدّة,
2 وعاء, 3 العضليّة, 4 التّجويف) · Q4 b · Q5 c · Q6 l1-r2, l2-r3, l3-r1 : **toutes conformes**. Q4 ne se
déduit plus de Q6 (les membres gauches ne portent plus de jours, et les paires ne sont pas visibles avant
réponse). Q2 : clé 37 car., 3ᵉ sur 4 (19, 28, 42).

**Figure (Chromium, 232 px).** Le trait du repère 6 s'arrête maintenant dans la bande claire de la muqueuse,
nettement à droite du bord de la musculeuse et à quelques pixels du triangle pointillé de la cavité ; la
cavité n'est pas parmi les noms proposés en Q1 : aucune ambiguïté. Aucun autre élément déplacé.

- **[MINOR] Q2, explication.** « ولا تتكوّن في الرّحم ولا في الطّور اللّوتيني » réfute encore « في الرّحم », qui
  n'est plus dans l'option c. Correctif exact : « …وهي موجودة في المبيض منذ الولادة ولا تتكوّن خلال الطّور
  اللّوتيني… ».
- `gisement.json` : la ligne de m036 cite encore 2017 ex. 1 item 2, l'auteur l'a laissée (« gisement.json non
  touché »). À retirer par l'orchestrateur (item écarté comme doublon de 11/05-tadrib Q3).

## m037 (12/11, 9 q.)

Q1 et Q4 de l'audit supprimées ; renumérotation Q2 → Q1, Q3 → Q2, Q5 → Q3, Q6 → Q4, Q7 → Q5, Q8 → Q6,
Q9 → Q7, Q10 → Q8, Q11 → Q9. Textes retrouvés mot pour mot : Q1 ligne d'avril et e ; Q3 dates nues et étiquette
de c ; Q4 énoncé ; Q6 énoncé ; Q7 énoncé (à un point près : « …دون أن يظهر. وظهر… » au lieu de « ، وظهر » :
sans effet), c et son étiquette, phrase d'explication ; Q8 énoncé ; étiquettes « أفريل » et « ماي » sur la
figure de Q9.

Re-résolution : Q1 a, b · Q2 a, b, c · Q3 23 juin · Q4 a · Q5 juin · Q6 a, b · Q7 d · Q8 a-b-c-d-e · Q9 16 avril
et 16 mai : **toutes conformes**. Q7 tient sans l'épaisseur : selon le cours 11 (§ « إن لم يحدث إلقاح يضمر
الجسم الأصفر »), un corps jaune plus gros qu'au mois précédent n'est pas un corps jaune qui régresse : a est
réfutée, d est seule juste. Q5 n'est plus livrée par Q7, ni Q7 par Q8.

**Figure de Q9 (Chromium, 232 px).** « أفريل » et « ماي » au-dessus de la courbe, lisibles, sans chevauchement
ni lecture comme valeur d'épaisseur. Courbe inchangée (chutes vers le jour 6, plateaux, bandes de règles 1–5).

- **[MAJOR] Fuite d'explication sur la route : Q1 → Q4.** L'explication de Q1 (d2, émise avant Q4)
  dit encore « رسوم أفريل تبيّن جريبات متقاربة الحجم لم ينضج منها شيء » : c'est la clé de Q4 (« لم ينضج أيّ
  جريب »), retirée de l'énoncé mais restée dans l'explication voisine. Correctif exact : remplacer la
  première phrase par « رسوم أفريل تبيّن جريبات ذات تجويف متقاربة الحجم، ولا جسم أصفر ولا بويضة محرّرة: لم تحدث
  إباضة. » (« لم تحدث إباضة » est la prémisse de Q4, pas sa clé).
- **[MINOR] Q1, explication désaccordée.** Elle réfute « اقتصار مبيض ماي على جريبات غير ناضجة » (l'ancien e)
  et ne réfute pas le nouvel e. Correctif exact : remplacer « أو اقتصار مبيض ماي على جريبات غير ناضجة » par « أو
  ظهور بويضة خارج المبيض في أفريل ».
- **[MINOR] Q7, explication.** « الخطأ الشّائع: … دون النّظر إلى الجسم الأصفر والسّمك » cite l'épaisseur, que
  l'énoncé ne donne plus. Correctif exact : « …دون النّظر إلى حجم الجسم الأصفر. »

---

## Contrôles

- Indices de forme : 0 clé strictement la plus longue dans les cinq fichiers ; 6 clés strictement les plus
  courtes sur 26 mcq (m034 Q2, Q4 ; m035 Q3, Q5 ; m037 Q4, Q5), toutes à 7 caractères ou moins de l'option
  suivante, sans marqueur : niveau du hasard.
- Étiquettes : toutes existantes ; la nouvelle (m037 Q7 c, `bio.cycle.uterus-autonome`) nomme exactement
  l'erreur ; m034 Q8 a, b, d `bio.alim.reactifs-confondus` justes.
- Gates : `content:check` vert. `content:qa` et `content:tranche` échouent en ce moment sur
  `09-al-ikhraj/exercices/10-…json`, fichier d'un autre lot en cours de modification dans l'arbre partagé
  (hors périmètre) : je n'ai pas pu les relancer ; les cinq fichiers L12 se chargent et sont conformes au
  schéma (`content:check`), et le journal de l'auteur rapporte qa et tranche verts au commit.

## Bilan

| mission | q. | clés fausses | majeurs restants | mineurs restants |
| --- | ---: | ---: | ---: | ---: |
| m033 | 8 | 0 | 0 | 1 |
| m034 | 8 | 0 | 1 | 1 |
| m035 | 7 | 0 | 0 | 2 |
| m036 | 6 | 0 | 0 | 1 |
| m037 | 9 | 0 | 1 | 2 |
| **total** | **38** | **0** | **2** | **7** |

Écarts déclarés : (1) m034 Q4 « سكّر ذائب » : conforme à mon texte, mais **mon texte était défectueux** (deux
réponses défendables) : correctif « مغذٍّ خلويّ ذائب في الماء ». (2) glose neutre de m035 Q1 : acceptée.
(3) m035 Q6 a et c allongées : justifié (sinon clé strictement la plus longue, erreur de mon décompte) ;
remplissage « نفسه تمامًا » à reformuler. (4) m034 Q8 calcium : fidèle mot pour mot au sujet 2015, pas un
doublon ; étage d2 plutôt que d3.

**Verdict : presque prêt. Deux majeurs courts à appliquer (m034 Q4 énoncé, m037 Q1 explication), puis
fusion possible sans nouvel audit ; les mineurs peuvent suivre dans la même passe.**

## Résumé court

Re-vérification L12 (38 questions après suppressions, toutes re-résolues). **Clés fausses : 0.** Textes de
l'audit appliqués mot pour mot ; figures (repère 6, étiquettes de mois) bonnes en Chromium. **Majeurs
restants : 2.**
1. m034 Q4 (ex-Q5), énoncé : remplacer « 100 غ من سكّر ذائب في الماء (العنصر ب) » par « 100 غ من مغذٍّ خلويّ
   ذائب في الماء (العنصر ب) » : avec « سكّر » seul, ب peut être du maltose et b devient défendable (défaut de
   mon propre correctif).
2. m037 Q1, explication : remplacer « رسوم أفريل تبيّن جريبات متقاربة الحجم لم ينضج منها شيء، ولا جسم أصفر ولا
   بويضة محرّرة: لم تحدث إباضة. » par « رسوم أفريل تبيّن جريبات ذات تجويف متقاربة الحجم، ولا جسم أصفر ولا بويضة
   محرّرة: لم تحدث إباضة. » (elle livrait la clé de Q4 sur la route).

**Mineurs restants : 7**, textes exacts dans le rapport : m033 Q7/Q8 explications (« ليس سكّرًا ولا دهنيّة ») ;
m034 Q8 `difficulty` 2 ; m035 Q6 c « …صنعها الدّم بنفسه من مواد أخرى: ظاهرة تركيب المغذّيات في الدّم » et la
fuite Q6 → Q4 (pour mémoire, pas de correctif) ; m036 Q2 explication (« ولا تتكوّن خلال الطّور اللّوتيني ») ;
m037 Q1 explication (« أو ظهور بويضة خارج المبيض في أفريل ») et Q7 explication (« …دون النّظر إلى حجم الجسم
الأصفر. »). Écarts : 2, 3 et 4 acceptés ; le 1 est conforme à mon texte, qu'il faut corriger. Reste aussi à retirer
2017 ex. 1 item 2 de `gisement.json`. **Verdict : presque prêt. Appliquer les deux majeurs, puis fusion possible
sans nouvel audit.**

## Suite donnée par le pilote (2026-10-16)

Majeurs 1 (m034 Q4 « مغذٍّ خلويّ ») et 2 (m037 Q1 explication) appliqués mot pour mot ; mineurs : m033 Q7
(remplacement) et Q8 (phrase retirée), m034 calcium en `difficulty: 2` **et déplacé en 3ᵉ position** pour garder
la rampe non décroissante (2, 2, 2, 3…), m035 Q6 c (105 car. ; a 108, b clé 98, d 97), m036 Q2, m037 Q1 et Q7
explications. `content:check` vert, prettier propre. Source 2017 ex. 1 item 2 de m036 retirée du registre à la
livraison. **L12 prêt à livrer.**
