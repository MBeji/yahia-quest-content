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
