# Carte d'usage — vocabulaire d'erreurs de l'arabe 9ᵉ, PARTIE A (grammaire 101908, 8 chapitres)

> Statut : EN COURS — chapitres traités : 15, 04, 16, 17, 18

Livrable jumeau : `vocab-arabe9-A.json` (ids NEUFS seulement). Ce fichier est généré à partir d'un jeu de données unique ; chaque distracteur cité a été relu dans le corpus (l'extrait est celui du JSON, pas une recopie à la main).

## 0. Conventions

- **Référence d'un distracteur** : `CC:F#N→o` = chapitre `CC` (15, 04, 16, 17, 18, 02, 03, 19), fichier `F` (`quiz` = `quiz.json` ; `01`…`06` = le préfixe numérique du fichier de `exercices/`), question `N` (rang **1-based dans le fichier**, qui est aussi le `qN` du compilateur : tous les fichiers sont déjà triés par `difficulty`), option `o` (`a`…`d`).
- Les 8 chapitres ont chacun 35 questions (quiz 5 + 5 exercices × 6), toutes `mcq`, **aucune option n'est encore taguée**.
- « Porte » : le distracteur est **reconstructible** (portes R1/R2/R3 du schéma) pour cet id. Un distracteur n'est cité que pour UN id (le script refuse un doublon) ; les cas où deux ids se touchent sont arbitrés au §3.
- « Q » = nombre de questions DISTINCTES qui ont au moins un distracteur porteur (seuil du registre : ≥ 3, ou un `piege` du cours).
- Les libellés sont dans `vocab-arabe9-A.json` ; la colonne « libellé » ci-dessous ne donne que l'arabe, pour relecture rapide.

## 1. Synthèse des ids

**63 ids neufs, 0 ids réutilisés** à ce stade (EN COURS — chapitres traités : 15, 04, 16, 17, 18).

| id | statut | chapitres | Q | `piege` |
| --- | --- | --- | --- | --- |
| `arabe.hadhf.hukm-min-mawqi3-al-baqi` | neuf | 15 | 1 | 15: n°16 |
| `arabe.istifham.ghaya-min-al-shakl` | neuf | 16 | 3 | 16: n°2 |
| `arabe.istifham.hal-makan-al-hamza` | neuf | 16 | 1 | 16: n°7 |
| `arabe.istifham.harf-ism-khalt` | neuf | 16 | 3 | — |
| `arabe.istifham.harf-jawab-yunaqid` | neuf | 16 | 3 | 16: n°3 |
| `arabe.istifham.ism-ghayr-munasib` | neuf | 16 | 4 | 16: n°4 |
| `arabe.istifham.jarr-min-al-harf-wahdah` | neuf | 16 | 2 | 16: n°8 |
| `arabe.istifham.markab-jarr-khabar-aw-mutammim` | neuf | 16 | 4 | 16: n°9 |
| `arabe.istifham.rutba-al-harf` | neuf | 16 | 1 | 16: n°1 |
| `arabe.istifham.wazifa-bila-jawab` | neuf | 16 | 5 | 16: n°5 |
| `arabe.jumla.isnad-far3i-la-yura` | neuf | 15 | 2 | — |
| `arabe.jumla.markaba-li-tul` | neuf | 15 | 1 | 15: n°1 |
| `arabe.jumla.naw3-bi-fi3l` | neuf | 15 | 1 | 15: n°1 |
| `arabe.nida.adat-bil-masafa` | neuf | 04 | 1 | 04: n°2 |
| `arabe.nida.mudaf-marfu3` | neuf | 04 | 1 | 04: n°4 |
| `arabe.nida.mustaghath-wa-lah-khalt` | neuf | 04 | 3 | 04: n°5 |
| `arabe.nida.nasb-al-marfu3` | neuf | 04 | 3 | — |
| `arabe.nida.nudba-istighatha` | neuf | 04 | 2 | 04: n°6 |
| `arabe.nida.rukn-thalith` | neuf | 04 | 2 | 04: n°1 |
| `arabe.nida.shakl-nahwi-khalt` | neuf | 04 | 4 | — |
| `arabe.nida.tanwin-al-munada` | neuf | 04 | 1 | 04: n°3 |
| `arabe.rabt.amma-bila-fa` | neuf | 15 | 1 | 15: n°11 |
| `arabe.rabt.aw-takhyir-daiman` | neuf | 15 | 1 | 15: n°7 |
| `arabe.rabt.bal-bila-nazar-fil-ula` | neuf | 15 | 2 | 15: n°9 |
| `arabe.rabt.fa-thumma-bila-tartib` | neuf | 15 | 3 | — |
| `arabe.rabt.fa-wajh-wahid` | neuf | 15 | 1 | 15: n°5 |
| `arabe.rabt.hatta-jam3-daiman` | neuf | 15 | 1 | 15: n°6 |
| `arabe.rabt.i3tirad-wal-hal-khalt` | neuf | 15 | 3 | 15: n°3 |
| `arabe.rabt.imma-amma-khalt` | neuf | 15 | 2 | 15: n°11 |
| `arabe.rabt.ism-al-harf-min-shaklih` | neuf | 15 | 3 | 15: n°4 |
| `arabe.rabt.istidrak-bi-ma-yuwafiq` | neuf | 15 | 1 | 15: n°10 |
| `arabe.rabt.kull-ay-tafsir` | neuf | 15 | 1 | 15: n°13 |
| `arabe.rabt.natija-bi-ghayr-al-fa` | neuf | 15 | 2 | 15: n°6 |
| `arabe.rabt.rutba-bi-shakl-la-bil-unsur` | neuf | 15 | 3 | 15: n°2 |
| `arabe.rabt.waw-tartib` | neuf | 15 | 3 | 15: n°5 |
| `arabe.shart.fa-al-rabt-mahdhufa` | neuf | 17 | 1 | 17: n°4 |
| `arabe.shart.imkan-istintaj-khalt` | neuf | 17 | 5 | 17: n°10,11 |
| `arabe.shart.imtina3-ghayr-maqru2` | neuf | 17 | 3 | — |
| `arabe.shart.in-madi-ka-lau` | neuf | 17 | 2 | 17: n°8 |
| `arabe.shart.ism-shart-ghayr-munasib` | neuf | 17 | 2 | 17: n°6 |
| `arabe.shart.jazm-fi-ghayr-mawdi3ih` | neuf | 17 | 2 | 17: n°2 |
| `arabe.shart.lau-3ala-zahiriha` | neuf | 17 | 4 | 17: n°9 |
| `arabe.shart.lau-lil-mumkin` | neuf | 17 | 3 | 17: n°3 |
| `arabe.shart.man-ma-shart-daiman` | neuf | 17 | 3 | 17: n°5 |
| `arabe.shart.mudari3-marfu3-ba3d-adat` | neuf | 17 | 3 | 17: n°2 |
| `arabe.shart.ra2isi-bi-tartib-al-dhikr` | neuf | 17 | 2 | 17: n°1 |
| `arabe.shart.wazifa-bila-ra2isi` | neuf | 17 | 4 | 17: n°7 |
| `arabe.shart.wujub-shart-khalt` | neuf | 17 | 7 | — |
| `arabe.talab.dua-min-shakl-al-jumla` | neuf | 04 | 3 | 04: n°7 |
| `arabe.talab.hukm-bi-natija` | neuf | 04 | 3 | 04: n°9 |
| `arabe.talab.kull-la-nahy` | neuf | 04 | 2 | 04: n°11 |
| `arabe.talab.ma3na-bila-maqam` | neuf | 04 | 4 | 04: n°12 |
| `arabe.talab.sigha-amr-khalt` | neuf | 04 | 3 | — |
| `arabe.zaman.ba3d-in-an-kay-waqi3` | neuf | 18 | 7 | 18: n°9 |
| `arabe.zaman.harf-ma3na-khalt` | neuf | 18 | 6 | — |
| `arabe.zaman.lau-halla-akhbar` | neuf | 18 | 2 | 18: n°5,6 |
| `arabe.zaman.nafy-zaman-khalt` | neuf | 18 | 7 | 18: n°5,8 |
| `arabe.zaman.nahiya-lan-khalt` | neuf | 18 | 3 | — |
| `arabe.zaman.qad-sin-sawfa-khalt` | neuf | 18 | 8 | 18: n°7 |
| `arabe.zaman.sayaq-khass-bil-sigha` | neuf | 18 | 4 | 18: n°4 |
| `arabe.zaman.sayaq-khass-khalt` | neuf | 18 | 4 | — |
| `arabe.zaman.sigha-ma3na-khalt` | neuf | 18 | 7 | 18: n°1 |
| `arabe.zaman.zaman-min-al-sigha` | neuf | 18 | 3 | 18: n°2,3,10 |

## 2. Fiches par id

### Domaine `hadhf`

#### `arabe.hadhf.hukm-min-mawqi3-al-baqi` — NEUF

- **AR** : تحكمُ على الباقي في الجوابِ من موقعِه (فتقولُ: خبرٌ) لا من الجملةِ الكاملةِ التي يعيدُها السّؤالُ: «مَن في القاعةِ؟ — المعلّمُ» الباقي مبتدأٌ
- **FR** : Tu juges le reste de la réponse d'après sa place (« خبر ») et non d'après la phrase complète que rétablit la question : مَن في القاعة؟ — المعلّم : مبتدأ
- **EN** : You judge what's left in the answer from its position ("khabar") not from the full sentence the question restores: مَن في القاعة؟ — المعلّم is a مبتدأ
- **Chapitres / piège** : ch15 — piège n°16 (§ الحذف في الفعليّة والاسميّة) « افتراضُ أنّ الباقيَ في الجوابِ هو الخبرُ دائمًا »
- **Q distinctes** : 1
- **Distracteurs porteurs** :
  - `15:04#6→a` « المحذوفُ المبتدأُ، والباقي «الحارسُ» خبرٌ » — R1 : « لا نحكمُ على الحارسُ بأنّه خبرٌ لمجرّد أنّه الجوابُ »

### Domaine `istifham`

#### `arabe.istifham.ghaya-min-al-shakl` — NEUF

- **AR** : تحكمُ على غايةِ السّؤالِ من علامةِ الاستفهامِ أو من النّفيِ وحدِهما، لا ممّا يعلمُه السّائلُ: يعلمُ ← تذكيرٌ، وينتظرُ ولا يعلمُ ← استخبارٌ عن متوقَّعٍ
- **FR** : Tu juges le but d'une question d'après le « ? » ou la négation seuls, non d'après ce que sait celui qui la pose : il sait ← rappel ; il attend ← fait attendu
- **EN** : You judge a question's aim from the "?" or the negation alone, not from what the asker knows: knows ← reminder; expects without knowing ← expected event
- **Chapitres / piège** : ch16 — piège n°2 (§ المثبتة والمنفيّة) « الحكم على غاية السائل من علامة الاستفهام وحدها »
- **Q distinctes** : 3
- **Distracteurs porteurs** :
  - `16:01#4→a` « الاستخبار عن مجهول » — R1 : « الاستخبار عن مجهول » alors que la mère sait
  - `16:01#4→b` « الاستخبار عن حصول شيء متوقَّع » — R1 : « متوقَّع » alors que la mère sait
  - `16:03#2→a` « التذكير بشيء معلوم » — R1 : « تذكير » alors que le marchand ignore
  - `16:04#2→b` « تذكير بمعلوم، والجواب «بَلَى، وَصَلَتْ» » — R1 : « تذكير بمعلوم » alors que le voyageur ignore

#### `arabe.istifham.hal-makan-al-hamza` — NEUF

- **AR** : تضعُ «هل» مكانَ الهمزةِ في جملةِ التّسويةِ (سيّانِ عندي هلْ حضرتَ أمْ غبتَ): التّسويةُ تقتضي همزةَ الاستفهامِ ثمّ «أم»
- **FR** : Tu mets « هل » à la place de la hamza dans une phrase de تسوية (سيّان عندي هل حضرتَ أم غبتَ) : la تسوية exige la hamza interrogative puis « أم »
- **EN** : You use « هل » instead of the hamza in a تسوية sentence (سيّان عندي هل حضرتَ أم غبتَ): the تسوية needs the interrogative hamza followed by « أم »
- **Chapitres / piège** : ch16 — piège n°7 (§ الاستفهام والتسوية) « استعمال «هل» مكان الهمزة في التسوية »
- **Q distinctes** : 1
- **Distracteurs porteurs** :
  - `16:02#4→a` « سَوَاءٌ عَلَيَّ هَلْ قَبِلْتَ أَمْ رَفَضْتَ » — R1 : « لا تقوم هل مقام الهمزة في هذا التركيب »

#### `arabe.istifham.harf-ism-khalt` — NEUF

- **AR** : تخلطُ بينَ حرفَي الاستفهامِ وأسمائِه: الهمزةُ و«هل» تسألانِ عن مضمونِ الجملةِ ويُجابُ بنعم أو لا، والاسمُ يسألُ عن عنصرٍ ويُجابُ بكلمةٍ
- **FR** : Tu confonds les particules (أ، هل) et les noms interrogatifs : les premières interrogent tout le contenu (réponse نعم/لا), le nom un élément (réponse : un mot)
- **EN** : You confuse the particles (أ، هل) with interrogative nouns: particles question the whole content (answer نعم/لا), a noun questions one element (answer: a word)
- **Chapitres / piège** : ch16 — (pas de piège ; erreur récurrente dans les items)
- **Q distinctes** : 3
- **Distracteurs porteurs** :
  - `16:quiz#1→a` « «مَنْ» وَ«مَا» » — R2 : « مَن وما » donnés pour interroger le contenu
  - `16:quiz#1→b` « «كَيْفَ» وَ«أَيْنَ» » — R2 : « كيف وأين »
  - `16:quiz#1→d` « «مَتَى» وَ«كَمْ» » — R2 : « متى وكم »
  - `16:01#1→a` « مَتَى نَجَحَ أَخُوكَ؟ » — R2 : « متى » pour une question de contenu
  - `16:01#1→c` « كَيْفَ نَجَحَ أَخُوكَ؟ » — R2 : « كيف »
  - `16:01#1→d` « أَيْنَ نَجَحَ أَخُوكَ؟ » — R2 : « أين »
  - `16:03#1→a` « اسم مكان (المدينة التي سافر إليها) » — R2 : réponse attendue = lieu pour une question en أ
  - `16:03#1→b` « ظرف زمان (وقت سفره ويوم عودته) » — R2 : réponse attendue = temps
  - `16:03#1→c` « عدد (الأيّام التي قضاها مسافرًا) » — R2 : réponse attendue = nombre

#### `arabe.istifham.harf-jawab-yunaqid` — NEUF

- **AR** : تتبعُ حرفَ الجوابِ بجملةٍ تناقضُه: بعدَ سؤالٍ منفيٍّ «نعم» تُثبِتُ النّفيَ فيتبعُها نفيٌ، و«بلى» تُبطِلُه فيتبعُها إثباتٌ (بلى، كتبتُه)
- **FR** : Tu fais suivre ta réponse d'une phrase qui la contredit : après une question négative, نعم confirme le négatif (phrase négative), بلى l'annule (affirmative)
- **EN** : You follow your answer with a clause that contradicts it: after a negative question, نعم confirms the negative (negative clause), بلى cancels it (affirmative)
- **Chapitres / piège** : ch16 — piège n°3 (§ الجواب: نعم وبلى) « الجواب بـ«نعم، قرأتُها» عن سؤال منفيّ »
- **Q distinctes** : 3
- **Distracteurs porteurs** :
  - `16:quiz#2→b` « نَعَمْ، كَتَبْتُهُ » — R1 : « نعم، كتبتُه »
  - `16:quiz#2→c` « لَا، كَتَبْتُهُ » — R1 : « لا، كتبتُه »
  - `16:quiz#2→d` « بَلَى، لَمْ أَكْتُبْهُ » — R1 : « بلى، لم أكتبْه »
  - `16:02#1→b` « بَلَى، لَمْ أَفْقِدْهَا » — R1 : « بلى، لم أفقدْها »
  - `16:02#1→d` « نَعَمْ، فَقَدْتُ حَقِيبَتِي » — R1 : « نعم، فقدتُ حقيبتي » se contredit
  - `16:04#2→c` « استخبار عن متوقَّع، والجواب «نَعَمْ، وَصَلَتْ» » — R1 : « نعم، وصلت » se contredit

#### `arabe.istifham.ism-ghayr-munasib` — NEUF

- **AR** : تختارُ اسمَ الاستفهامِ على غيرِ نوعِ المجهولِ (ما عن شخصٍ، متى عن مكانٍ): مَن للعاقلِ، وما لغيرِه، وأينَ للمكانِ، ومتى للزّمانِ، وكيفَ للهيئةِ، وكَمْ للعددِ
- **FR** : Ton nom interrogatif ne va pas avec l'inconnu (ما pour une personne, متى pour un lieu) : مَن personne, ما chose, أين lieu, متى temps, كيف manière, كم nombre
- **EN** : You pick an interrogative noun that doesn't fit the unknown (ما for a person, متى for a place): مَن person, ما thing, أين place, متى time, كيف manner, كم number
- **Chapitres / piège** : ch16 — piège n°4 (§ أسماء الاستفهام) « السؤال عن شخص بـ«ما» »
- **Q distinctes** : 4
- **Distracteurs porteurs** :
  - `16:01#5→a` « مَا » — R1 : « ما » pour un شخص — le piège du cours
  - `16:01#5→c` « أَيْنَ » — R1 : أين pour un شخص
  - `16:01#5→d` « كَمْ » — R1 : كم pour un شخص
  - `16:01#3→b` « مَتَى » — متى pour le lieu
  - `16:01#3→c` « كَيْفَ » — كيف pour le lieu
  - `16:01#3→d` « مَنْ » — مَن pour le lieu
  - `16:05#2→a` « الكيفيّة » — sens de كيف donné à كم
  - `16:05#2→b` « التعيين بين عدّة أشياء » — sens de أيّ donné à كم
  - `16:05#2→c` « الظرفيّة الزمانيّة » — sens de متى donné à كم
  - `16:05#6→a` « أَيْنَ » — أين pour le temps
  - `16:05#6→c` « كَيْفَ » — كيف pour le temps
  - `16:05#6→d` « كَمْ » — كم pour le temps

#### `arabe.istifham.jarr-min-al-harf-wahdah` — NEUF

- **AR** : تقرأُ معنى مركّبِ الجرِّ من حرفِ الجرِّ وحدَه (لِمَنْ سلّمتَ؟ سببيّةٌ لأنّ فيها «لـ»): الذي يعيّنُ المعنى هو السّياقُ والجوابُ لا الحرفُ
- **FR** : Tu lis le sens d'un مركّب جرّ d'après la seule préposition (لِمَنْ سلّمتَ؟ = cause parce qu'il y a لـ) : le contexte et la réponse le fixent, pas la préposition
- **EN** : You read a prepositional phrase's meaning from the preposition alone (لِمَنْ سلّمتَ؟ = cause because of لـ): context and the answer fix it, not the preposition
- **Chapitres / piège** : ch16 — piège n°8 (§ اسم الاستفهام المقترن بحرف الجرّ) « قراءة المعنى من حرف الجرّ وحده »
- **Q distinctes** : 2
- **Distracteurs porteurs** :
  - `16:02#5→b` « مفعول لأجله » — R1 : « مفعول لأجله » — il ne demande pas de cause
  - `16:04#5→b` « لِمَنْ سَلَّمْتَ الدَّفْتَرَ؟ » — R1 : « لِمَنْ سلّمتَ » pris pour une سببيّة

#### `arabe.istifham.markab-jarr-khabar-aw-mutammim` — NEUF

- **AR** : تعاملُ مركّبَ الجرِّ دونَ النّظرِ إلى وجودِ الفعلِ: بعدَ فعلٍ هو متمّمٌ له، وفي جملةٍ بلا فعلٍ هو خبرٌ مقدّمٌ والاسمُ بعدَه مبتدأٌ مؤخَّرٌ لا فاعلٌ
- **FR** : Tu traites le مركّب جرّ sans voir s'il y a un verbe : avec verbe, c'est son complément ; sans verbe, un خبر مقدّم suivi d'un مبتدأ مؤخّر, pas d'un فاعل
- **EN** : You treat a prepositional phrase without checking for a verb: with a verb it is its complement; with none, a fronted خبر followed by a مبتدأ, not a subject
- **Chapitres / piège** : ch16 — piège n°9 (§ مركّب الجرّ خبرًا مقدّمًا) « عدّ الاسم بعد مركّب الجرّ فاعلًا («مِنْ أَيِّ مَدِينَةٍ أَنْتَ؟») »
- **Q distinctes** : 4
- **Distracteurs porteurs** :
  - `16:quiz#5→a` « مفعول به » — R1 : « مفعول به » dans une phrase sans verbe
  - `16:quiz#5→b` « مفعول لأجله » — R1 : « مفعول لأجله » dans une phrase sans verbe
  - `16:quiz#5→d` « حال » — R1 : « حال » dans une phrase sans verbe
  - `16:02#5→d` « خبر مقدّم » — R1 : « لا خبرًا مقدّمًا لأنّ في الجملة فعلًا »
  - `16:02#6→a` « فِي أَيِّ بَلَدٍ تَسْكُنُ؟ » — R1 : verbe présent « تسكن » ⇒ complément
  - `16:02#6→b` « فِي أَيِّ بَلَدٍ وُلِدْتَ؟ » — R1 : verbe présent « وُلدتَ »
  - `16:02#6→d` « فِي أَيِّ بَلَدٍ دَرَسْتَ؟ » — R1 : verbe présent « درستَ »
  - `16:03#6→a` « أنّ حرف الجرّ «لـ» جاء في أوّلها » — raison = la préposition « لـ » en tête
  - `16:03#6→c` « أنّ اسم الاستفهام «مَن» جاء بعد الحرف » — raison = le nom interrogatif « مَن »
  - `16:03#6→d` « أنّ اسم الإشارة جاء بعد المركّب » — raison = le démonstratif
- **Note** : Le piège n°9 (« أنتَ فاعل ») n'a pas de porteur littéral : l'id est porté par le même geste (ignorer l'absence de verbe). À signaler à l'orchestrateur.

#### `arabe.istifham.rutba-al-harf` — NEUF

- **AR** : تقدِّمُ حرفَ الاستئنافِ على الهمزةِ أو تؤخِّرُه عن «هل» (وَأَتَقْبَلُ، هَلْ وَتَقْبَلُ): الهمزةُ قبلَه، و«هل» بعدَه: أَوَ تَقْبَلُ؟ وَهَلْ تَقْبَلُ؟
- **FR** : Tu mets و/ف avant la hamza ou après « هل » (وَأَتَقْبَلُ، هَلْ وَتَقْبَلُ) : la hamza précède le connecteur, « هل » le suit : أَوَ تَقْبَلُ؟ وَهَلْ تَقْبَلُ؟
- **EN** : You put the connector before the hamza or after « هل » (وَأَتَقْبَلُ، هَلْ وَتَقْبَلُ): the hamza comes before it, « هل » after: أَوَ تَقْبَلُ؟ وَهَلْ تَقْبَلُ؟
- **Chapitres / piège** : ch16 — piège n°1 (§ حرفا الاستفهام) « تقديم حرف الاستئناف على الهمزة أو تأخيره عن «هل» (وَأَتَقْبَلُ، هَلْ وَتَقْبَلُ) »
- **Q distinctes** : 1
- **Distracteurs porteurs** :
  - `16:04#1→a` « وَأَتَسْمَعُنِي؟ » — R1 : واو قبل الهمزة
  - `16:04#1→b` « هَلْ وَتَسْمَعُنِي؟ » — R1 : واو بعد « هل »

#### `arabe.istifham.wazifa-bila-jawab` — NEUF

- **AR** : تحدّدُ وظيفةَ اسمِ الاستفهامِ من موقعِه في الصّدارةِ لا من العنصرِ الذي يحلُّ محلَّه في الجوابِ: «ما اشتريتَ؟» ← تفّاحًا: مفعولٌ به لا مبتدأٌ
- **FR** : Tu fixes la fonction du nom interrogatif d'après sa place en tête, non d'après l'élément qui le remplace dans la réponse : ما اشتريتَ؟ ← تفّاحًا : مفعول به
- **EN** : You fix an interrogative noun's function from its place at the front, not from the element replacing it in the answer: ما اشتريتَ؟ ← تفّاحًا: مفعول به
- **Chapitres / piège** : ch16 — piège n°5 (§ وظيفة اسم الاستفهام) « الحكم على الوظيفة من الترتيب («ما» مبتدأ لأنّها أوّل الجملة) »
- **Q distinctes** : 5
- **Distracteurs porteurs** :
  - `16:quiz#4→a` « مبتدأ » — R1 : « مبتدأ لمجرّد أنّها في أوّل الجملة »
  - `16:quiz#4→c` « مفعول به » — fonction étrangère à la réponse « نشيط »
  - `16:quiz#4→d` « حال » — fonction étrangère à la réponse
  - `16:02#2→a` « مبتدأ، لأنّها تتصدّر الجملة والمبتدأ أوّل ما يقع في الجملة » — R1 : « مبتدأ لأنّها تتصدّر الجملة »
  - `16:02#2→b` « فاعل، لأنّها تسبق الفعل فتكون هي من قام بالشراء » — R1 : « فاعل لأنّها تسبق الفعل »
  - `16:02#2→d` « خبر مقدّم، لأنّ اسم الاستفهام يتقدّم دائمًا على المبتدأ » — R1 : « خبر مقدّم لأنّ الاسم يتقدّم دائمًا »
  - `16:01#6→a` « خبر » — fonction étrangère à la réponse « مبتسمًا »
  - `16:01#6→b` « مفعول مطلق » — idem
  - `16:01#6→c` « مفعول به » — idem
  - `16:03#4→b` « مفعول فيه للزمان » — مفعول فيه للزمان alors que la réponse est un lieu
  - `16:03#4→c` « خبر مقدّم » — idem
  - `16:03#4→d` « مفعول به » — idem
  - `16:04#3→a` « «كَيْفَ جَرَى الحِصَانُ؟» — «جَرَى مُسْرِعًا نَحْوَ الإِصْطَبْلِ» » — paire « مسرعًا » = حال, non مطلق
  - `16:04#3→c` « «كَيْفَ الحِصَانُ بَعْدَ السِّبَاقِ؟» — «الحِصَانُ مُتْعَبٌ جِدًّا» » — paire « متعب » = خبر
  - `16:04#3→d` « «كَيْفَ أَصْبَحَ الحِصَانُ؟» — «أَصْبَحَ نَشِيطًا جِدًّا» » — paire « نشيطًا » = خبر كان

### Domaine `jumla`

#### `arabe.jumla.isnad-far3i-la-yura` — NEUF

- **AR** : تعدُّ الجملةَ بسيطةً لأنّك ترى فعلًا واحدًا: الخبرُ أو الحالُ أو المفعولُ به إذا كان جملةً (يلعبونَ في الحديقةِ) إسنادٌ فرعيٌّ يجعلُها مركّبةً
- **FR** : Tu juges une phrase simple parce que tu ne vois qu'un verbe : un خبر, un حال ou un complément qui est une phrase (يلعبون في الحديقة) la rend composée
- **EN** : You call a sentence simple because you see one verb: a خبر, حال or object that is itself a clause (يلعبون في الحديقة) makes it compound
- **Chapitres / piège** : ch15 — (pas de piège ; erreur récurrente dans les items)
- **Q distinctes** : 2
- **Distracteurs porteurs** :
  - `15:05#1→a` « قالَ المدرّبُ للّاعبينَ إنّ التّمرينَ سيبدأُ غدًا » — R2 : مفعول به = جملة « إنّ التمرين سيبدأ غدًا »
  - `15:05#1→b` « الأطفالُ الصّغارُ يلعبونَ في الحديقةِ العامّةِ مساءً » — R2 : خبر = جملة « يلعبون في الحديقة »
  - `15:05#1→d` « رأيتُ الولدَ النّشيطَ يقرأُ في المكتبةِ الكبيرةِ » — R2 : حال = جملة « يقرأ في المكتبة »
  - `15:04#3→b` « اسميّةٌ بسيطةٌ، لأنّ خبرَها «تسيرُ ببطءٍ» فعلٌ وليس فيها إسنادٌ ثانٍ » — R1 : « خبرها تسير ببطء فعل وليس فيها إسناد ثانٍ »

#### `arabe.jumla.markaba-li-tul` — NEUF

- **AR** : تعدُّ الجملةَ مركّبةً لأنّها طويلةٌ أو فيها جارٌّ ومجرورٌ ونعتٌ: المركّبةُ ما شغلَ أحدَ مكوّناتِها إسنادٌ فرعيٌّ (فعلٌ وفاعلُه)
- **FR** : Tu juges une phrase composée parce qu'elle est longue ou a un complément prépositionnel : elle l'est si un composant est un إسناد فرعيّ (verbe + sujet)
- **EN** : You call a sentence compound because it is long or has a prepositional phrase: it is compound only if a component is itself a clause (إسناد فرعيّ)
- **Chapitres / piège** : ch15 — piège n°1 (§ الجملة في النص) « الأطفالُ يلعبونَ في السّاحةِ: «فعليّةٌ، لأنّ فيها فعلًا» + عدّ الجملة الطويلة مركّبةً » [moitié couverte : 2e moitié : « طويلة ⇒ مركّبة »]
- **Q distinctes** : 1
- **Distracteurs porteurs** :
  - `15:01#1→b` « فعليّةٌ مركّبةٌ » — R1 : l'explication dit « متمّمان لا إسناد فيهما »

#### `arabe.jumla.naw3-bi-fi3l` — NEUF

- **AR** : تحكمُ بأنّ الجملةَ فعليّةٌ لأنّ فيها فعلًا أو لأنّها تبدأُ بـ«كانَ»: النّوعُ يُقرأُ من أوّلِ مكوّنٍ، والنّاسخُ يُبقيها اسميّةً
- **FR** : Tu dis « verbale » parce qu'il y a un verbe ou qu'elle commence par كان : le type se lit au 1er composant, et un ناسخ la laisse nominale
- **EN** : You call it verbal because it holds a verb or starts with كان: the type comes from the first component, and a ناسخ keeps it nominal
- **Chapitres / piège** : ch15 — piège n°1 (§ الجملة في النص) « الأطفالُ يلعبونَ في السّاحةِ: «فعليّةٌ، لأنّ فيها فعلًا» + عدّ الجملة الطويلة مركّبةً » [moitié couverte : 1re moitié : « فعليّة لأنّ فيها فعلًا »]
- **Q distinctes** : 1
- **Distracteurs porteurs** :
  - `15:04#3→a` « فعليّةٌ مركّبةٌ، لأنّها تبدأُ بالفعلِ «كانتِ» وفيها إسنادٌ فرعيٌّ » — R1 : « تبدأ بالفعل كانت » — le ناسخ pris pour un verbe

### Domaine `nida`

#### `arabe.nida.adat-bil-masafa` — NEUF

- **AR** : تختارُ أداةَ النّداءِ بالمسافةِ الحسّيّةِ وحدَها: القربُ والبعدُ حسًّا أو معنًى، ومَن بجانبِك قد يُنادى بـ«أيا» إن كان بعيدًا معنًى
- **FR** : Tu choisis l'outil d'appel d'après la seule distance physique : proche ou lointain se mesure aussi au sens ; qui est à côté de toi peut être appelé par أيا
- **EN** : You choose the vocative particle by physical distance alone: near or far is also a matter of attention; someone beside you can be called with أيا
- **Chapitres / piège** : ch04 — piège n°2 (§ أدوات النداء) « ربط الأداة بالمسافة الحسّيّة وحدها »
- **Q distinctes** : 1
- **Distracteurs porteurs** :
  - `04:05#1→c` « لأنّ الزّميل قريب حسًّا ومعنًى » — R1 : « قريب حسًّا ومعنًى » — l'élève ne compte que la distance physique

#### `arabe.nida.mudaf-marfu3` — NEUF

- **AR** : تضمُّ المضافَ في المنادى المركّبِ الإضافيّ لأنّه علمٌ (يا عبدُ اللهِ) أو تكسرُه: العلمُ المفردُ وحدَه يُضمُّ، والمضافُ يُنصَبُ: يا عبدَ اللهِ
- **FR** : Tu mets le مضاف d'un منادى annexé à la damma, comme un nom propre (يا عبدُ اللهِ), ou à la kasra : seul le علم مفرد prend la damma ; le مضاف est à l'accusatif
- **EN** : You give the مضاف of an annexed vocative a damma because it is a name (يا عبدُ اللهِ), or a kasra: only a single-word name takes damma; the مضاف is accusative
- **Chapitres / piège** : ch04 — piège n°4 (§ حكم المنادى: النصب) « ضمّ المضاف لأنّه علم («يا عبدُ اللهِ») »
- **Q distinctes** : 1
- **Distracteurs porteurs** :
  - `04:02#2→a` « يَا حَارِسُ البُسْتَانِ، افْتَحِ البَابَ » — R1 : « الضمّة للعلم المفرد… » — « يا حارسُ البستانِ »
  - `04:02#2→c` « يَا حَارِسِ البُسْتَانِ، افْتَحِ البَابَ » — R1 : « الكسرة ليست حكم المنادى »

#### `arabe.nida.mustaghath-wa-lah-khalt` — NEUF

- **AR** : تخلطُ بينَ المستغاثِ والمستغاثِ له والمستغاثِ منه: المستغاثُ مَن تناديه (لامُه مفتوحةٌ)، وله مَن تستغيثُ لأجلِه (مكسورةٌ)، ومنه ما تستغيثُ بسببِه (بـ«مِنْ»)
- **FR** : Tu confonds مستغاث, مستغاث له et مستغاث منه : le مستغاث est celui que tu appelles (lam fatha), le له celui pour qui (kasra), le منه ce qui menace (par مِنْ)
- **EN** : You mix up مستغاث (who you call, lam fatha), مستغاث له (who it is for, kasra) and مستغاث منه (what threatens, with مِنْ)
- **Chapitres / piège** : ch04 — piège n°5 (§ الاستغاثة) « عدّ المستغاث له هو المستغاث »
- **Q distinctes** : 3
- **Distracteurs porteurs** :
  - `04:01#6→a` « الشّرطة مستغاث، واللّصوص مستغاث له » — R1 : اللصوص (منه) pris pour مستغاث له
  - `04:01#6→b` « الشّرطة مستغاث منه، واللّصوص مستغاث » — R1 : المستغاث pris pour مستغاث منه et inversement
  - `04:01#6→d` « الشّرطة مستغاث له، واللّصوص مستغاث منه » — R1 : الشرطة (المستغاث) pris pour مستغاث له
  - `04:02#5→a` « يَا لِلمُسْعِفِينَ لَلمُصَابِينَ » — R1 : لامان inversés
  - `04:02#5→c` « يَا لَلمُسْعِفِينَ لَلمُصَابِينَ » — R1 : « يوحّدهما » — deux lam fatha
  - `04:02#5→d` « يَا لِلمُسْعِفِينَ لِلمُصَابِينَ » — R1 : « يوحّدهما » — deux lam kasra
  - `04:06#3→a` « المستغاث بلام مكسورة، والمستغاث له بلام مفتوحة، والمستغاث منه بـ«مِنْ» » — R1 : lam kasra au مستغاث, fatha au له
  - `04:06#3→c` « المستغاث بلام مفتوحة، والمستغاث له بـ«مِنْ»، والمستغاث منه بلام مكسورة » — R1 : « مِنْ » donné au مستغاث له
  - `04:06#3→d` « المستغاث بـ«مِنْ»، والمستغاث له بلام مفتوحة، والمستغاث منه بلام مكسورة » — R1 : « مِنْ » donné au مستغاث

#### `arabe.nida.nasb-al-marfu3` — NEUF

- **AR** : تنصبُ العلمَ المفردَ أو النّكرةَ المقصودةَ أو المعرَّفَ بـ«ال» في النّداءِ: هذه الثّلاثةُ تُضمُّ (يا سامرُ، يا ولدُ)؛ النّصبُ للمضافِ وللموصوفِ
- **FR** : Tu mets à l'accusatif le علم مفرد, la نكرة مقصودة ou le défini en ال : ces trois prennent la damma (يا سامرُ، يا ولدُ) ; le نصب va au مضاف et au موصوف
- **EN** : You make a one-word name, intended indefinite or ال-noun accusative: these three take damma (يا سامرُ، يا ولدُ); accusative is for the مضاف and the موصوف
- **Chapitres / piège** : ch04 — (pas de piège ; erreur récurrente dans les items)
- **Q distinctes** : 3
- **Distracteurs porteurs** :
  - `04:quiz#2→a` « علم مفرد، مثل «سامر» » — R2 : علم مفرد ← « ينصب »
  - `04:quiz#2→b` « نكرة مقصودة، مثل «ولد» » — R2 : نكرة مقصودة ← « ينصب »
  - `04:quiz#2→c` « اسم معرّف بالألف واللام بعد «أيُّها»، مثل «التّلميذ» » — R2 : معرّف بأل ← « ينصب »
  - `04:04#2→d` « يَا أَيُّهَا المُسَافِرَ، اسْتَرِحْ » — R1 : « المعرّف بالألف واللام من حالات الرفع »
  - `04:06#2→c` « لأنّ العلم يُنصب دائمًا إذا نُودي » — R1 : « العلم ينصب دائمًا إذا نودي »

#### `arabe.nida.nudba-istighatha` — NEUF

- **AR** : تخلطُ النّدبةَ بالاستغاثةِ أو بالنّداءِ العاديّ لأنّ صاحبَها في شدّةٍ: النّدبةُ تتفجّعُ (وا + مندوبٌ بألفٍ وهاءٍ)، لا تطلبُ عونًا ولا تنبِّهُ
- **FR** : Tu confonds ندبة, استغاثة et appel ordinaire parce que l'auteur souffre : la ندبة se lamente (وا + مندوب en ـاه), elle ne demande pas d'aide et n'alerte pas
- **EN** : You confuse ندبة, استغاثة and a plain call because the speaker suffers: ندبة laments (وا + مندوب ending in ـاه), it asks for no help and does not alert
- **Chapitres / piège** : ch04 — piège n°6 (§ النّدبة) « عدّ النّدبة استغاثة لأنّ صاحبها في شدّة »
- **Q distinctes** : 2
- **Distracteurs porteurs** :
  - `04:04#1→a` « يَا لَلقَوْمِ لِلوَلَدِ » — R1 : « يا لَلقومِ لِلولدِ » = استغاثة
  - `04:04#1→b` « يَا وَلَدُ، تَعَالَ » — R1 : نداء عاديّ « يا ولدُ »
  - `04:04#1→c` « أَيَا وَلَدُ، تَعَالَ » — R1 : نداء عاديّ « أيا ولدُ »
  - `04:05#3→a` « حرف نداء للاستغاثة ومستغاث » — R1 : حرف نداء للاستغاثة + مستغاث
  - `04:05#3→b` « حرف ندبة ومستغاث » — حرف ندبة صحيح mais « مستغاث »
  - `04:05#3→d` « حرف نداء للاستغاثة ومندوب » — R1 : حرف نداء للاستغاثة + مندوب

#### `arabe.nida.rukn-thalith` — NEUF

- **AR** : تعدُّ ما بعدَ المنادى ركنًا ثالثًا في جملةِ النّداءِ: ركناها حرفُ نداءٍ ومنادًى فقط، وما يقولُه المتكلّمُ بعدَهما جملةٌ أخرى
- **FR** : Tu comptes ce qui suit le منادى comme un troisième pilier : la phrase d'appel n'a que deux piliers, حرف نداء et منادى ; la suite est une autre phrase
- **EN** : You count what follows the منادى as a third pillar: a vocative sentence has only two, حرف نداء and منادى; what comes next is another sentence
- **Chapitres / piège** : ch04 — piège n°1 (§ النداء) « عدّ ما بعد المنادى ركنًا ثالثًا »
- **Q distinctes** : 2
- **Distracteurs porteurs** :
  - `04:quiz#1→d` « منادى وما يُطلب منه » — R1 : « منادى وما يُطلب منه » ; l'explication : « جملة أخرى لا ركن ثالث »
  - `04:01#3→d` « «بَائِعَ الزُّهُورِ» و«أَعْطِنِي بَاقَةً» » — R1 : « أعطني باقةً » prise pour un ركن

#### `arabe.nida.shakl-nahwi-khalt` — NEUF

- **AR** : تسمّي المنادى بغيرِ شكلِه النّحويّ: اسألْ هل هو اسمُ شخصٍ في كلمةٍ؟ هل قُصدَ به معيَّنٌ؟ هل فيه «ال»؟ هل هو مضافٌ؟ هل وُصفَ ولم يُقصَدْ؟
- **FR** : Tu nommes mal la forme du منادى : est-il un nom propre d'un mot, vise-t-il quelqu'un de précis, a-t-il ال, est-il annexé, est-il décrit et non visé ?
- **EN** : You label the vocative with the wrong grammatical form: ask if it is a one-word name, aims at someone specific, has ال, is annexed, or is described and unaimed
- **Chapitres / piège** : ch04 — (pas de piège ; erreur récurrente dans les items)
- **Q distinctes** : 4
- **Distracteurs porteurs** :
  - `04:02#1→a` « علم مفرد » — R1 : « ليست علمًا مفردًا لأنّها ليست اسم شخص »
  - `04:02#1→c` « نكرة موصوفة غير مقصودة » — R1 : « قصد معيّنًا ولم يصفه »
  - `04:02#1→d` « معرّف بالألف واللام » — R1 : « خالية من الألف واللام »
  - `04:02#4→a` « علم مفرد: اسم شخص يُنادى به وحده بلا إضافة ولا وصف » — R1 : علم مفرد pour « يا سائقًا كريمًا »
  - `04:02#4→b` « مركّب إضافيّ: مضاف يليه مضاف إليه يُنادى بهما معًا » — R1 : مركّب إضافيّ pour « يا سائقًا كريمًا »
  - `04:02#4→d` « نكرة مقصودة: نكرة قُصد بها معيَّن فدلّت عليه » — R1 : نكرة مقصودة pour une نكرة غير مقصودة
  - `04:04#3→a` « الأوّل علم مفرد فيُرفع، والثّاني مركّب إضافيّ فيُنصب » — R1 : types intervertis
  - `04:04#3→c` « الأوّل نكرة موصوفة غير مقصودة فيُنصب، والثّاني علم مفرد فيُرفع » — R1 : types mal nommés
  - `04:04#3→d` « الأوّل نكرة مقصودة فيُرفع، والثّاني معرّف بالألف واللام فيُنصب » — R1 : types mal nommés
  - `04:06#2→a` « لأنّه نكرة موصوفة غير مقصودة بالنّداء » — R1 : « علم معيَّن » pris pour نكرة موصوفة
  - `04:06#2→b` « لأنّه معرّف بالألف واللام » — R1 : « عبد خالٍ من الألف واللام »

#### `arabe.nida.tanwin-al-munada` — NEUF

- **AR** : تنوِّنُ المنادى لأنّه نكرةٌ (يا ولدٌ، يا حارسٌ البستانِ): المنادى المضمومُ لا يُنوَّنُ ولا يجتمعُ التّنوينُ مع الإضافةِ؛ ينوَّنُ الموصوفُ المنصوبُ فقط
- **FR** : Tu mets le tanwin au منادى car il est indéfini (يا ولدٌ) : à la damma il n'en a pas, et il ne va pas avec l'annexion ; seul le موصوف منصوب en porte
- **EN** : You put tanwin on the vocative because it is indefinite (يا ولدٌ): a damma-vocative takes no tanwin, none with annexation; only the described accusative has it
- **Chapitres / piège** : ch04 — piège n°3 (§ حكم المنادى: الرفع) « تنوين المنادى النكرة («يا ولدٌ») » [moitié couverte : geste commun : tanwin sur un منادى]
- **Q distinctes** : 1
- **Distracteurs porteurs** :
  - `04:02#2→b` « يَا حَارِسٌ البُسْتَانِ، افْتَحِ البَابَ » — R1 : « التّنوين لا يجتمع مع الإضافة » — seul porteur ; le piège du cours (« يا ولدٌ ») n'a pas de porteur exact

### Domaine `rabt`

#### `arabe.rabt.amma-bila-fa` — NEUF

- **AR** : تحذفُ الفاءَ بعدَ المبتدأِ في «أمّا» (أمّا كريمٌ نجحَ): الفاءُ من قالبِ التّفصيلِ: أمّا + مبتدأٌ + فـ + خبرٌ
- **FR** : Tu supprimes la ف après le مبتدأ dans « أمّا » (أمّا كريم نجح) : elle fait partie du moule du détail : أمّا + مبتدأ + ف + خبر
- **EN** : You drop the ف after the مبتدأ in « أمّا » (أمّا كريم نجح): it is part of the pattern: أمّا + مبتدأ + ف + خبر
- **Chapitres / piège** : ch15 — piège n°11 (§ أمّا وإذا وإذن وأي) « حذفُ الفاءِ بعدَ المبتدأِ في «أمّا» + الخلطُ بينَ «إمّا» و«أمّا» » [moitié couverte : 1re moitié : « حذف الفاء بعد المبتدأ »]
- **Q distinctes** : 1
- **Distracteurs porteurs** :
  - `15:04#4→c` « أمّا سالمٌ نجحَ، وأمّا ليلى أعادتِ السّنةَ » — R1 : « حذفُ الفاءِ يُسقطُ جزءًا من القالبِ »

#### `arabe.rabt.aw-takhyir-daiman` — NEUF

- **AR** : تحملُ «أو» على التّخييرِ دائمًا: في الإخبارِ هي للشّكِّ (كُسرتْ ساقُه، أو التوتْ قدمُه)، والتّخييرُ يكونُ في الطّلبِ فقط
- **FR** : Tu prends toujours « أو » pour un choix laissé à l'autre : dans une affirmation elle dit le doute (كُسرت ساقه أو التوت قدمه) ; le choix vient avec la demande
- **EN** : You always read « أو » as offering a choice: in a statement it expresses doubt (كُسرت ساقه أو التوت قدمه); choice belongs to requests
- **Chapitres / piège** : ch15 — piège n°7 (§ أو وإمّا وأم) « حملُ «أو» على التّخييرِ دائمًا »
- **Q distinctes** : 1
- **Distracteurs porteurs** :
  - `15:03#1→a` « تخييرُ المتكلّمِ للمخاطَبِ بينَ الحدثَينِ » — R1 : « التّخييرُ يكونُ في الطّلبِ »

#### `arabe.rabt.bal-bila-nazar-fil-ula` — NEUF

- **AR** : تحدّدُ معنى «بل» دونَ أن تنظرَ في الجملةِ الأولى: إضرابٌ إن تراجعَ عنها المتكلّمُ، تقريرٌ إن كانت منفيّةً وبقيتْ، تأكيدٌ إن بقيتْ والثّانيةُ أقوى
- **FR** : Tu fixes le sens de بل sans regarder la 1re phrase : إضراب si l'on s'en dédit ; تقرير si elle est négative et reste vraie ; تأكيد si elle reste vraie, renforcée
- **EN** : You fix the meaning of بل without checking the first sentence: إضراب if it is retracted; تقرير if it is negative and stands; تأكيد if it stands, strengthened
- **Chapitres / piège** : ch15 — piège n°9 (§ بل ولكن) « قراءةُ «بل» إضرابًا دائمًا »
- **Q distinctes** : 2
- **Distracteurs porteurs** :
  - `15:quiz#4→a` « الإضرابُ عن الجملةِ الأولى والتّراجعُ عنها » — R1 : إضراب alors que « لم يتأخّر » reste vrai
  - `15:quiz#4→b` « تأكيدُ الجملةِ الأولى بجملةٍ ثانيةٍ أقوى منها » — تأكيد alors que la 1re est négative
  - `15:02#4→b` « رأيتُ سعيدًا في المكتبةِ، بل رأيتُ أخاه » — إضراب (« بل رأيتُ أخاه ») lu comme تقرير
  - `15:02#4→c` « أهانَ الرّجلُ جارَه، بل ضربَه » — تأكيد lu comme تقرير
  - `15:02#4→d` « أخذَ الطّفلُ الحلوى، بل أخذَ الكعكَ » — إضراب (« أخذَ الكعكَ ») lu comme تقرير

#### `arabe.rabt.fa-thumma-bila-tartib` — NEUF

- **AR** : تقرأُ الفاءَ أو «ثمّ» جمعًا بلا ترتيبٍ كالواوِ: تبديلُ الجملتَينِ معهما يقلبُ المعنى، لأنّ ما بعدَهما يأتي بعدَ ما قبلَهما
- **FR** : Tu lis ف ou ثمّ comme و, une réunion sans ordre : avec elles, inverser les deux phrases change le sens, car la seconde vient après la première
- **EN** : You read ف or ثمّ like و, joining with no order: swapping the two sentences changes the meaning, since the second comes after the first
- **Chapitres / piège** : ch15 — (pas de piège ; erreur récurrente dans les items)
- **Q distinctes** : 3
- **Distracteurs porteurs** :
  - `15:01#4→a` « اشتدّتِ العاصفةُ، فأُغلقَ الميناءُ » — R2 : فاء السببية — l'élève croit l'inversion sans effet
  - `15:01#4→b` « أنهى الحارسُ جولتَه، ثمّ أغلقَ البوّابةَ » — R2 : ثمّ — idem
  - `15:01#4→c` « فتحَ الباعةُ دكاكينَهم، فازدحمَ السّوقُ » — R2 : فاء الترتيب — idem
  - `15:01#5→d` « الجمعُ بينَ الجملتَينِ بدونِ أيِّ ترتيبٍ » — فاء التفصيل prise pour « جمع بدون أيّ ترتيب »
  - `15:02#2→b` « ترتيبَ الحدثَينِ » — « ترتيب الحدثين » censé se perdre en passant de ثمّ à ف

#### `arabe.rabt.fa-wajh-wahid` — NEUF

- **AR** : تقرأُ كلَّ فاءٍ ترتيبَ أحداثٍ أو سببًا ونتيجةً: للفاءِ ثلاثةُ وجوهٍ، منها تفصيلُ ما أُجمِلَ (اختلفوا، فمنهم من… ومنهم من…)
- **FR** : Tu lis chaque ف comme un ordre d'événements ou une cause : ف a trois emplois, dont le détail d'un ensemble global (اختلفوا، فمنهم… ومنهم…)
- **EN** : You read every ف as event order or cause: ف has three uses, including detailing something stated globally (اختلفوا، فمنهم… ومنهم…)
- **Chapitres / piège** : ch15 — piège n°5 (§ حروف الجمع) « قراءةُ الواوِ ترتيبًا لأنّ الأحداثَ تتتابعُ + كلُّ فاءٍ ترتيبُ أحداثٍ » [moitié couverte : 2e moitié : « كلّ فاء ترتيب أحداث »]
- **Q distinctes** : 1
- **Distracteurs porteurs** :
  - `15:01#5→b` « ترتيبُ الأحداثِ بحسبِ وقوعِها في الزّمنِ » — R1 : « ليس حدثًا لاحقًا »
  - `15:01#5→c` « ترتيبُ السّببِ والنّتيجةِ بينَ الجملتَينِ » — R1 : « ولا نتيجةً له »

#### `arabe.rabt.hatta-jam3-daiman` — NEUF

- **AR** : تعدُّ كلَّ «حتّى» حرفَ جمعٍ: التي تصحُّ بـ«إلى أنْ» (سهرَ حتّى طلعَ الفجرُ) تحدّدُ النّهايةَ، وجمعُ المستبعَدِ جملةٌ تامّةٌ لا تصحُّ بها «إلى أنْ»
- **FR** : Tu prends chaque حتّى pour une réunion : si إلى أنْ convient (سهر حتّى طلع الفجر), elle marque le terme ; réunir l'improbable exige une phrase complète
- **EN** : You take every حتّى as joining: if إلى أنْ fits (سهر حتّى طلع الفجر) it marks an endpoint; joining the improbable takes a full sentence
- **Chapitres / piège** : ch15 — piège n°6 (§ حروف الجمع) « اختيارُ «ثمّ» لذكرِ النّتيجةِ + عدُّ كلِّ «حتّى» حرفَ جمعٍ » [moitié couverte : 2e moitié : « كلّ حتّى حرف جمع »]
- **Q distinctes** : 1
- **Distracteurs porteurs** :
  - `15:02#3→a` « سهرَ الجيرانُ حتّى الفجرِ » — R2 : « حتّى الفجرِ » (اسم مفرد = غاية)
  - `15:02#3→c` « تدرّبَ الفريقُ حتّى أتقنَ الخطّةَ » — R2 : « حتّى أتقنَ الخطّةَ »
  - `15:02#3→d` « واصلْنا السّيرَ حتّى بلغْنا القمّةَ » — R2 : « حتّى بلغْنا القمّةَ »

#### `arabe.rabt.i3tirad-wal-hal-khalt` — NEUF

- **AR** : تعدُّ كلَّ مقطعٍ بينَ فاصلتَينِ أو مبدوءٍ بواوٍ جملةً اعتراضيّةً: الحالُ والمفعولُ فيه لهما وظيفةٌ، والاعتراضيّةُ وحدَها بلا وظيفةٍ
- **FR** : Tu prends tout segment entre deux virgules (ou en و) pour une اعتراضيّة : un حال ou un مفعول فيه a une fonction, seule l'اعتراضيّة n'en a pas
- **EN** : You take any segment between two commas (or starting with و) for an اعتراضيّة: a حال or مفعول فيه has a function; only the اعتراضيّة has none
- **Chapitres / piège** : ch15 — piège n°3 (§ رتبة الجملة) « عدُّ كلِّ مقطعٍ بينَ فاصلتَينِ جملةً اعتراضيّةً (وقد فازَ = حالٌ) »
- **Q distinctes** : 3
- **Distracteurs porteurs** :
  - `15:quiz#2→a` « كلُّ مقطعٍ يقعُ بينَ فاصلتَينِ في الجملةِ » — R1 : « كلُّ مقطعٍ يقعُ بينَ فاصلتَينِ »
  - `15:quiz#2→b` « جملةٌ تصفُ هيئةَ الفاعلِ حينَ يقومُ بالفعلِ » — تعريف الحال (« تصفُ هيئةَ الفاعلِ »)
  - `15:02#1→a` « استقبلَ الحارسُ، وهو يبتسمُ، الزّوّارَ » — R2 : « وهو يبتسمُ » حال
  - `15:02#1→b` « وصلَ الأستاذُ، حينَ دقَّ الجرسُ، إلى القسمِ » — R2 : « حينَ دقَّ الجرسُ » مفعول فيه
  - `15:02#1→d` « عادَ التّلاميذُ، وقد أنهَوا الامتحانَ، إلى بيوتِهم » — R2 : « وقد أنهَوا الامتحانَ » حال
  - `15:05#3→b` « جملةٌ حاليّةٌ، لأنّها بدأتْ بالواوِ ووقعتْ بينَ مكوّنَينِ » — R1 : « لأنّها بدأتْ بالواوِ »

#### `arabe.rabt.imma-amma-khalt` — NEUF

- **AR** : تخلطُ بينَ «إمّا» و«أمّا»: «إمّا» اختيارٌ بينَ أمرَينِ لا يجتمعانِ وتتكرّرُ، و«أمّا» تفصيلٌ لمُجْمَلٍ يتبعُها مبتدأٌ ثمّ فاءٌ
- **FR** : Tu confonds إمّا et أمّا : إمّا choisit entre deux possibilités incompatibles et se répète ; أمّا détaille un ensemble, suivi d'un مبتدأ puis de ف
- **EN** : You confuse إمّا and أمّا: إمّا picks between two incompatible options and repeats; أمّا details a whole, followed by a مبتدأ then ف
- **Chapitres / piège** : ch15 — piège n°11 (§ أمّا وإذا وإذن وأي) « حذفُ الفاءِ بعدَ المبتدأِ في «أمّا» + الخلطُ بينَ «إمّا» و«أمّا» » [moitié couverte : 2e moitié : « لا تخلط بين إمّا وأمّا »]
- **Q distinctes** : 2
- **Distracteurs porteurs** :
  - `15:04#4→a` « إمّا سالمٌ فنجحَ، وإمّا ليلى فأعادتِ السّنةَ » — R1 : « إمّا للاختيار لا للتفصيل »
  - `15:03#3→a` « إمّا أن تدرسَ وإمّا أن ترسبَ » — R1 : « إمّا … وإمّا » proposé pour le تفصيل

#### `arabe.rabt.ism-al-harf-min-shaklih` — NEUF

- **AR** : تسمّي أداةَ الرّبطِ (و، ف، ثمّ، أم) حرفَ عطفٍ من شكلِها أو معناها لا ممّا تربطُه: جملتانِ مستقلّتانِ ← استئنافٌ، وعنصرانِ بوظيفةٍ ← عطفٌ
- **FR** : Tu nommes la particule (و ف ثمّ أم) selon sa forme ou son sens, pas selon ce qu'elle relie : 2 phrases ← استئناف ; 2 éléments de même fonction ← عطف
- **EN** : You name a particle (و، ف، ثمّ، أم) by its shape or meaning, not by what it links: two independent sentences ← استئناف; two same-function items ← عطف
- **Chapitres / piège** : ch15 — piège n°4 (§ حرف الاستئناف وحرف العطف) « تسميةُ الواوِ أو الفاءِ أو «ثمّ» حرفَ عطفٍ دائمًا »
- **Q distinctes** : 3
- **Distracteurs porteurs** :
  - `15:05#2→a` « حرفُ عطفٍ، لأنّها تربطُ بينَ فعلَينِ متتابعَينِ في النّصِّ » — R1 : « تربط بين فعلين متتابعين » ≠ عنصرين بوظيفة واحدة
  - `15:05#2→c` « حرفُ عطفٍ، لأنّها تفيدُ الجمعَ بينَ الحدثَينِ بدونِ ترتيبٍ » — R1 : nom tiré du sens « جمع بدون ترتيب »
  - `15:01#3→b` « حرفُ استئنافٍ، لأنّه يفيدُ الجمعَ بينَ الأحداثِ بدونِ ترتيبٍ » — R1 : « حرف استئناف لأنّه يفيد الجمع… »
  - `15:02#5→d` « حرفُ عطفٍ يفيدُ طلبَ تعيينِ أحدِ الأمرَينِ » — nom « عطف » pour أم (sens juste)
- **Note** : Dans une question « nom + raison » (01#3, 05#2, 02#5), l'id du NOM prime quand la raison donnée est vraie mais ne peut pas fonder le nom ; voir §3.

#### `arabe.rabt.istidrak-bi-ma-yuwafiq` — NEUF

- **AR** : تستدركُ بـ«لكنْ» وأخواتِها بما هو متوقَّعٌ (اجتهدَ، لكنّه نجحَ): الاستدراكُ يأتي بخلافِ المتوقَّعِ، وإلّا فالرّبطُ بالفاءِ
- **FR** : Tu emploies لكنّ et ses sœurs pour dire ce qu'on attend (اجتهد لكنّه نجح) : l'استدراك apporte le contraire de l'attendu, sinon on relie par ف
- **EN** : You use لكنّ and its sisters for what is expected (اجتهد لكنّه نجح): the استدراك brings the opposite of what is expected; otherwise link with ف
- **Chapitres / piège** : ch15 — piège n°10 (§ بل ولكن) « استعمالُ أداةِ الاستدراكِ حينَ تكونُ الثّانيةُ هي المتوقَّعَ »
- **Q distinctes** : 1
- **Distracteurs porteurs** :
  - `15:05#5→a` « تدرّبَ اللّاعبُ كثيرًا، لكنّه تحسّنَ » — R2 : « تدرّبَ… لكنّه تحسّنَ »
  - `15:05#5→b` « انكسرَ الزّجاجُ، بيدَ أنّه تناثرَ على الأرضِ » — R2 : « انكسرَ… بيدَ أنّه تناثرَ »
  - `15:05#5→d` « أعدَّ الطّالبُ مشروعَه، غيرَ أنّه سلّمَه في موعدِه » — R2 : « أعدَّ… غيرَ أنّه سلّمَه في موعدِه »

#### `arabe.rabt.kull-ay-tafsir` — NEUF

- **AR** : تعدُّ كلَّ «أيْ» تفسيرًا: «أيْ بُنيَّ» نداءٌ للقريبِ و«أيُّ الطّريقَينِ؟» استفهامٌ؛ التّفسيرُ جملةٌ تشرحُ ما قبلَها بعبارةٍ أوضحَ
- **FR** : Tu prends tout « أيْ » pour une explication : أيْ بُنيَّ est un appel, أيُّ الطريقين؟ une question ; l'explication reprend plus clairement la phrase précédente
- **EN** : You take every « أيْ » as an explanation: أيْ بُنيَّ calls someone near, أيُّ الطريقين؟ asks a question; explaining restates the previous clause more clearly
- **Chapitres / piège** : ch15 — piège n°13 (§ أمّا وإذا وإذن وأي) « عدُّ كلِّ «أيْ» تفسيرًا »
- **Q distinctes** : 1
- **Distracteurs porteurs** :
  - `15:04#2→a` « أيْ بُنيَّ، أحسنْ إلى جيرانِكَ » — R1 : « أيْ بُنيَّ » = حرف نداء
  - `15:04#2→b` « أيُّ الطّريقَينِ أقصرُ؟ » — R1 : « أيُّ الطريقين » = اسم استفهام

#### `arabe.rabt.natija-bi-ghayr-al-fa` — NEUF

- **AR** : تعبّرُ عن النّتيجةِ بـ«ثمّ» أو الواوِ أو «أي»: السّببُ والنّتيجةُ للفاءِ؛ «ثمّ» تقولُ مهلةً، والواوُ جمعًا بلا ترتيبٍ، و«أي» شرحًا
- **FR** : Tu exprimes la conséquence avec ثمّ, و ou أي : cause et conséquence relèvent de ف ; ثمّ dit un délai, و une simple réunion, أي une explication
- **EN** : You express a result with ثمّ, و or أي: cause and effect belong to ف; ثمّ marks a delay, و plain joining, أي an explanation
- **Chapitres / piège** : ch15 — piège n°6 (§ حروف الجمع) « اختيارُ «ثمّ» لذكرِ النّتيجةِ + عدُّ كلِّ «حتّى» حرفَ جمعٍ » [moitié couverte : 1re moitié : « ثمّ لذكر النتيجة »]
- **Q distinctes** : 2
- **Distracteurs porteurs** :
  - `15:05#4→a` « أنهى الصّيّادُ عملَه، ثمّ عادَ إلى بيتِه » — R2 : « ثمّ عادَ إلى بيتِه »
  - `15:05#4→c` « ارتفعَ الموجُ، وغابتِ الشّمسُ » — R2 : الواو
  - `15:05#4→d` « غابَ التّلميذُ، أي لم يحضرِ الدّرسَ » — R2 : « أي »
  - `15:02#2→c` « الدّلالةَ على أنّ الثّاني نتيجةُ الأوّلِ » — R1 : « السّبب والنّتيجة » attribué à ثمّ

#### `arabe.rabt.rutba-bi-shakl-la-bil-unsur` — NEUF

- **AR** : تحكمُ على رتبةِ الجملةِ بشكلِها (اسميّة/فعليّة) أو موضعِها، لا بما يردُّها إلى ما قبلَها: حرفِ استئنافٍ أو ضميرِ غيبةٍ أو اسمِ إشارةٍ
- **FR** : Tu juges le rang d'une phrase (ابتدائيّة/استئنافيّة) par sa forme ou sa place, pas par ce qui la relie à la précédente : حرف استئناف, ضمير غيبة, اسم إشارة
- **EN** : You judge a sentence's rank by its form or place, not by what links it to the previous one: a حرف استئناف, a third-person pronoun or a demonstrative
- **Chapitres / piège** : ch15 — piège n°2 (§ رتبة الجملة) « الحكمُ على الرّتبةِ بشكلِ الجملةِ: «ذلكَ الشّيخُ كريمٌ» ابتدائيّةٌ »
- **Q distinctes** : 3
- **Distracteurs porteurs** :
  - `15:quiz#1→a` « أن تبدأَ باسمٍ لا بفعلٍ، فتكونَ جملةً اسميّةً » — R1 : نوع (اسمية) لا رتبة
  - `15:quiz#1→c` « أن تقعَ في وسطِ النّصِّ لا في أوّلِه ولا في آخرِه » — R1 : موضعها من النص
  - `15:01#2→a` « ابتدائيّةٌ، لأنّها جملةٌ اسميّةٌ تبدأُ بمبتدأٍ » — R1 : « لأنّها جملة اسمية »
  - `15:01#2→c` « ابتدائيّةٌ، لأنّ اسمَ الإشارةِ لا يدلُّ على جملةٍ قبلَها » — اسم الإشارة « تلك » غير مرئيّ
  - `15:01#2→d` « استئنافيّةٌ، لأنّها الجملةُ الثّانيةُ في هذا النّصِّ » — R1 : « لأنّها الجملة الثانية »
  - `15:04#1→b` « ثمّ عادَ الجنودُ إلى الثّكنةِ » — R2 : تحتوي « ثمّ »
  - `15:04#1→c` « أعرفُ هذا الطّريقَ جيّدًا » — R2 : تحتوي « هذا »
  - `15:04#1→d` « هو أقدمُ مدارسِ المدينةِ » — R2 : تحتوي « هو »

#### `arabe.rabt.waw-tartib` — NEUF

- **AR** : تجعلُ الواوَ للتّرتيبِ لأنّ الأحداثَ تتتابعُ: الواوُ جمعٌ بلا ترتيبٍ ولا تراخٍ، والتّرتيبُ من معنى الفعلَينِ لا من الحرفِ
- **FR** : Tu fais de و un marqueur d'ordre parce que les faits se suivent : و réunit sans ordre ni délai ; l'ordre vient du sens des verbes, pas de la particule
- **EN** : You treat و as marking order because the events follow each other: و joins without order or delay; the order comes from the verbs, not the particle
- **Chapitres / piège** : ch15 — piège n°5 (§ حروف الجمع) « قراءةُ الواوِ ترتيبًا لأنّ الأحداثَ تتتابعُ + كلُّ فاءٍ ترتيبُ أحداثٍ » [moitié couverte : 1re moitié : « الواو ترتيب لأنّ الأحداث تتتابع »]
- **Q distinctes** : 3
- **Distracteurs porteurs** :
  - `15:quiz#3→b` « الجمعُ بينَ الأحداثِ مع التّرتيبِ » — R1 : الواو « مع الترتيب »
  - `15:quiz#3→c` « الجمعُ مع التّرتيبِ والتّراخي » — الواو « مع الترتيب والتراخي » (= ثمّ)
  - `15:05#2→b` « حرفُ استئنافٍ، لأنّها تفيدُ التّرتيبَ بينَ الحدثَينِ » — R1 : « تفيد الترتيب بين الحدثين » ; l'explication : « الواو لا ترتّب أصلًا »
  - `15:01#3→d` « حرفُ عطفٍ، لأنّه يفيدُ التّرتيبَ والتّراخيَ بينَ الحدثَينِ » — R1 : الواو « الترتيب والتراخي » (nom juste, sens faux)

### Domaine `shart`

#### `arabe.shart.fa-al-rabt-mahdhufa` — NEUF

- **AR** : تحذفُ فاءَ الرّبطِ لأنّ المعنى مفهومٌ (إنْ تعبتَ ارتحْ): الجوابُ الاسميُّ أو الأمرُ أو النّهيُ لا يلي الشّرطَ مباشرةً، ويلزمُه «فـ» (فارتحْ)
- **FR** : Tu supprimes la ف de liaison car le sens est clair (إنْ تعبتَ ارتحْ) : nominale, ordre ou défense ne suivent pas la condition seuls, il faut « ف » (فارتحْ)
- **EN** : You drop the linking ف as the meaning is clear (إنْ تعبتَ ارتحْ): a nominal clause, order or ban cannot follow the condition alone; it needs « ف » (فارتحْ)
- **Chapitres / piège** : ch17 — piège n°4 (§ فاء الربط) « ترك الفاء لأنّ المعنى مفهوم (إنْ تعبتَ ارتحْ) »
- **Q distinctes** : 1
- **Distracteurs porteurs** :
  - `17:05#2→b` « إنْ رأيتَ دخانًا اتّصلْ بالإطفاءِ » — R1 : « حذف الفاء خطأ »

#### `arabe.shart.imkan-istintaj-khalt` — NEUF

- **AR** : تخلطُ الافتراضَ بالاستنتاجِ لأنّ الأداةَ واحدةٌ: في الاستنتاجِ الثّانويُّ معلومٌ أو مسلَّمٌ به ويُستخرَجُ منه رئيسيٌّ مجهولٌ، وفي الإمكانِ يُنتظَرُ
- **FR** : Tu confonds hypothèse et déduction car l'outil est le même : en déduction le secondaire est connu ou admis et livre un principal inconnu ; sinon il est attendu
- **EN** : You confuse hypothesis and inference as the tool is the same: in inference the secondary is known or assumed and yields an unknown main one; else it is awaited
- **Chapitres / piège** : ch17 — piège n°10 (§ الاستنتاج) « الخلط بين الافتراض والاستنتاج لأنّ الحرف واحد » ; n°11 (§ أوظّف) « الحكم على المعنى من الأداة وحدها »
- **Q distinctes** : 5
- **Distracteurs porteurs** :
  - `17:quiz#5→b` « إنْ نجحتَ في الامتحانِ أهديتُكَ كتابًا جديدًا » — إنْ + إمكان pris pour استنتاج
  - `17:04#6→b` « إنْ نجحتَ فأخبرْنا » — R1 : « حدثان ممكنان لم يقع ثانويّهما بعد »
  - `17:04#6→c` « متى جاءَ الصّيفُ سافرْنا إلى البحرِ » — R1 : « متى جاء الصيف… » — إمكان
  - `17:05#6→d` « «لو» تدلُّ على امتناعٍ، و«إنْ» تدلُّ على استنتاجٍ من حدثٍ معلومٍ سابقٍ » — R1 : « وليس استنتاجًا لأنّ البدء لم يقع بعد »
  - `17:05#5→d` « كلاهما حدثٌ ممكنٌ لم يقعْ بعدُ، ولا يُعلمُ منهما شيءٌ » — R1 : « وليست الجملة وعدًا بحدث ممكن »
  - `17:04#5→a` « حرفُ «إنْ» نفسُه » — P11 : le temps déduit du seul حرف « إنْ »

#### `arabe.shart.imtina3-ghayr-maqru2` — NEUF

- **AR** : لا تقرأُ الامتناعَ حينَ يكونُ الحدثُ قد فاتَ: ما عُلِمَ أنّه لم يقعْ يُقالُ بـ«لو» + ماضٍ + لامٍ في الجوابِ، و«إنْ» و«إذا» و«متى» تتركُه ممكنًا
- **FR** : Tu ne lis pas l'impossibilité quand le fait est manqué : ce qu'on sait non advenu se dit « لو » + passé + لام au jawab ; إنْ، إذا et متى le laissent possible
- **EN** : You miss the impossibility when the event is already lost: what is known not to have happened takes « لو » + past + لام; إنْ, إذا and متى leave it possible
- **Chapitres / piège** : ch17 — (pas de piège ; erreur récurrente dans les items)
- **Q distinctes** : 3
- **Distracteurs porteurs** :
  - `17:quiz#3→a` « إنْ » — R1 : « إنْ » pour un train déjà manqué
  - `17:quiz#3→b` « إذا » — R1 : « إذا »
  - `17:quiz#3→c` « متى » — R1 : « متى »
  - `17:03#4→a` « إنْ يَزُرْنا خالي نُكرِمْهُ » — R1 : إمكان (« إنْ يزرنا ») donné pour امتناع
  - `17:03#4→d` « متى يَزُرْنا خالي نُكرِمْهُ » — R1 : إمكان (« متى يزرنا ») donné pour امتناع
  - `17:03#6→a` « «إنْ»، ومضارعٌ مجزومٌ بعدَها، وفاءُ الرّبطِ في الجوابِ » — R1 : قرائن الإمكان pour « لو دقّقتَ… »
  - `17:03#6→d` « «إذا»، ومضارعٌ مرفوعٌ بعدَها، وجملةٌ اسميّةٌ في الجوابِ » — R1 : قرائن الاستنتاج pour « لو دقّقتَ… »

#### `arabe.shart.in-madi-ka-lau` — NEUF

- **AR** : تقرأُ الماضيَ بعدَ «إنْ» كأنّه حدثٌ لم يقعْ كما في «لو»: «إنْ» تتركُ الحالةَ ممكنةً، و«لو» وحدَها تقولُ إنّها لم تقعْ، والفعلُ ماضي الصّيغةِ فيهما
- **FR** : Tu lis le passé après « إنْ » comme un fait non advenu, comme avec « لو » : إنْ laisse le cas possible, seul لو dit qu'il n'a pas eu lieu
- **EN** : You read the past after « إنْ » as not having happened, as with « لو »: إنْ leaves the case possible, only لو says it did not occur (past verb in both)
- **Chapitres / piège** : ch17 — piège n°8 (§ افتراض الممكن) « عدّ الماضي بعد «إنْ» دليلًا على أنّ الحدث لم يقع كما في «لو» »
- **Q distinctes** : 2
- **Distracteurs porteurs** :
  - `17:04#1→c` « لا فرقَ بينهما في المعنى، لأنّ الفعلَ ماضي الصّيغةِ في الجملتَينِ » — R1 : « لا فرق بينهما لأنّ الفعل ماضي الصيغة »
  - `17:05#6→b` « «لو» و«إنْ» كلتاهما تدلُّ على امتناعٍ لم يتحقّقْ في الماضي » — R1 : « كلتاهما تدلّ على امتناع »

#### `arabe.shart.ism-shart-ghayr-munasib` — NEUF

- **AR** : تختارُ اسمَ الشّرطِ على غيرِ ما يُعلَّقُ عليه الحدثُ: مَن للعاقلِ، وما ومهما لغيرِه، ومتى وإذا للزّمانِ، وحيثما وأينما وأنّى للمكانِ، وكيفما للهيئةِ
- **FR** : Ton nom de condition ne va pas avec ce dont dépend l'événement : مَن personne, ما/مهما chose, متى/إذا temps, حيثما/أينما/أنّى lieu, كيفما manière
- **EN** : Your conditional noun doesn't fit what the event depends on: مَن person, ما/مهما thing, متى/إذا time, حيثما/أينما/أنّى place, كيفما manner
- **Chapitres / piège** : ch17 — piège n°6 (§ أسماء الشرط العشرة) « اختيار الاسم بحسب الكلمة الأقرب لا المعنى (ما يتأخّر، متى/أينما) »
- **Q distinctes** : 2
- **Distracteurs porteurs** :
  - `17:05#1→a` « الظّرفيّةُ المكانيّةُ » — R1 : « متى » prise pour المكان
  - `17:05#1→c` « الكيفيّةُ والهيئةُ والحالُ » — R1 : « متى » prise pour الهيئة
  - `17:05#1→d` « العاقلُ » — R1 : « متى » prise pour العاقل
  - `17:02#6→c` « أنّ «كيفما» ظرفُ زمانٍ، وأنّه يحدّدُ وقتَ السّماعِ ويصفُ الفاعلَ » — R1 : « كيفما ظرف زمان »

#### `arabe.shart.jazm-fi-ghayr-mawdi3ih` — NEUF

- **AR** : تجزمُ المضارعَ في غيرِ موضعِه: الرّئيسيَّ المتقدّمَ على الشّرطِ (تنجحْ إنْ راجعتَ) أو ما بعدَ «إذا» (إذا يصلْ)؛ فالجزمُ يلي أداةً جازمةً و«إذا» ليست منها
- **FR** : Tu mets le jazm où il n'a pas lieu : sur le principal placé avant la condition (تنجحْ إنْ راجعتَ) ou après إذا (إذا يصلْ), qui n'est pas un outil de jazm
- **EN** : You apply the jussive where it doesn't belong: on a main verb before the condition (تنجحْ إنْ راجعتَ) or after إذا (إذا يصلْ), which is no jussive tool
- **Chapitres / piège** : ch17 — piège n°2 (§ حرف الشرط «إنْ») « ترك المضارع مرفوعًا بعد «إنْ» + جزم الرئيسيّ المتقدّم » [moitié couverte : 2e moitié : « جزم الرئيسيّ المتقدّم »]
- **Q distinctes** : 2
- **Distracteurs porteurs** :
  - `17:02#1→c` « تنجحْ إنْ تُراجِعْ دروسَكَ » — R1 : « جزم الرئيسيّ المتقدّم خطأ »
  - `17:03#5→a` « إذا يَصِلْ أخي نَفرَحْ » — R1 : « فيها جزم بعد إذا »

#### `arabe.shart.lau-3ala-zahiriha` — NEUF

- **AR** : تقرأُ جملةَ «لو» على ظاهرِها: المثبتُ بعدَها لم يقعْ، والمنفيُّ (لَمْ، ما، لَما) وقعَ؛ اقرأْها على عكسِها: لو أخذتُ المظلّةَ لَما ابتللتُ ← لم آخذْها وابتللتُ
- **FR** : Tu lis une phrase en « لو » au premier degré : l'affirmatif n'a pas eu lieu, le nié (لَمْ، ما، لَما) a eu lieu ; لو أخذتُ المظلّةَ لَما ابتللتُ ← mouillé
- **EN** : You read a « لو » sentence at face value: the affirmative did not happen, the negated (لَمْ، ما، لَما) did; لو أخذتُ المظلّةَ لَما ابتللتُ ← got wet
- **Chapitres / piège** : ch17 — piège n°9 (§ افتراض الممتنع) « قراءة الماضي بعد «لو» على أنّه حدث وقع »
- **Q distinctes** : 4
- **Distracteurs porteurs** :
  - `17:01#2→a` « ركبَها ووصلَ في الوقتِ » — R1 : « قراءة الماضي على أنّه حدث وقع »
  - `17:01#2→b` « ركبَها ولم يصلْ في الوقتِ » — R2 : lecture à moitié littérale
  - `17:01#2→d` « لم يركبْها لكنّه وصلَ في الوقتِ » — R2 : lecture à moitié littérale
  - `17:02#3→b` « أخذَ المظلّةَ ولم يبتلَّ » — R2 : « أخذ المظلة ولم يبتلّ »
  - `17:02#3→c` « أخذَها وابتلَّ » — R2 : « أخذها وابتلّ »
  - `17:02#3→d` « لم يأخذْها ولم يبتلَّ » — R1 : « النفي في الجواب يعني أنّه لم يبتلّ »
  - `17:04#4→a` « لم يُهمِلْها ولم يرسبْ » — R1 : « الخطأ الشائع : لم يهملها ولم يرسب »
  - `17:04#4→b` « لم يُهمِلْها ورسبَ » — R2 : lecture à moitié littérale
  - `17:04#4→d` « أهملَها ولم يرسبْ » — R2 : lecture à moitié littérale
  - `17:05#4→a` « وقوعُ الحادثِ، لأنّ السّائقَ كانَ منتبهًا للطّريقِ جيّدًا » — R1 : « قرأ النفي على ظاهره »
  - `17:05#4→c` « وقوعُ الحادثِ، لأنّ السّائقَ لم ينتبهْ للطّريقِ » — R1 : « قرأ النفي على ظاهره »

#### `arabe.shart.lau-lil-mumkin` — NEUF

- **AR** : تستعملُ «لو» لحدثٍ ما يزالُ ممكنًا أو للمستقبلِ (لو جاءَ غدًا) كما في اللّهجةِ: «لو» لما لم يتحقّقْ قبلَ القولِ مع ماضٍ أو «لَمْ»، والممكنُ لـ«إنْ»
- **FR** : Tu emploies « لو » pour un fait encore possible ou futur (لو جاءَ غدًا) comme en dialecte : « لو » vise ce qui n'a pas eu lieu avant ; le possible va à إنْ
- **EN** : You use « لو » for a still-possible or future event (لو جاءَ غدًا) as in dialect: « لو » is for what did not happen before speaking; the possible takes إنْ
- **Chapitres / piège** : ch17 — piège n°3 (§ حرف الشرط «لو») « استعمال «لو» في حدث ما يزال ممكنًا (لو جاء الأستاذ غدًا) »
- **Q distinctes** : 3
- **Distracteurs porteurs** :
  - `17:05#6→a` « «لو» تدلُّ على افتراضِ ممكنٍ في المستقبلِ، و«إنْ» تدلُّ على امتناعٍ ف… » — R1 : « لو » = افتراض ممكن في المستقبل
  - `17:02#2→a` « مضارعٌ مثبتٌ مجزومٌ أو فعلُ أمرٍ » — « لو » + مضارع مجزوم / أمر
  - `17:02#2→b` « مضارعٌ منفيٌّ بـ«لَنْ» يدلُّ على المستقبلِ » — R1 : « لو » + مضارع منفيّ بـ« لن »
  - `17:02#2→c` « مضارعٌ مسبوقٌ بالسّينِ يدلُّ على المستقبلِ » — R1 : « لو » + السين
  - `17:04#1→a` « جملةُ «إنْ» تتحدّثُ عن الماضي، وجملةُ «لو» تتحدّثُ عن المستقبلِ » — « إنْ » = الماضي، « لو » = المستقبل

#### `arabe.shart.man-ma-shart-daiman` — NEUF

- **AR** : تعدُّ كلَّ «مَنْ» و«ما» في أوّلِ الكلامِ اسمَ شرطٍ: اسمُ الشّرطِ في الصّدارةِ ومضارعُه مجزومٌ؛ وبعدَ فعلٍ أو ناسخٍ (إنّ، كانَ) هما موصولانِ
- **FR** : Tu prends tout « مَنْ » ou « ما » pour un nom de condition : il est en tête avec un présent مجزوم ; après un verbe ou un ناسخ (إنّ، كانَ) ce sont des relatifs
- **EN** : You take every « مَنْ » or « ما » as a conditional noun: it stands first with a jussive verb; after a verb or a ناسخ (إنّ، كانَ) they are relatives
- **Chapitres / piège** : ch17 — piège n°5 (§ اسم شرط أم اسم موصول ؟) « عدّ كلّ «مَنْ» و«ما» في أوّل الكلام اسمَي شرط »
- **Q distinctes** : 3
- **Distracteurs porteurs** :
  - `17:quiz#4→a` « إنّ مَنْ يَتعلّمُ يَرتقي » — R1 : « إنّ مَنْ… » — مَن بعد ناسخ
  - `17:quiz#4→b` « كانَ مَنْ تعلّمَ مرتاحًا » — R1 : « كانَ مَنْ… » — بعد ناسخ
  - `17:quiz#4→d` « يَرتقي مَنْ يَتعلّمُ بصبرٍ » — R1 : « يرتقي مَنْ… » — بعد فعل
  - `17:01#5→a` « كانَ ما كتبَهُ الطّالبُ واضحًا » — R1 : « كانَ ما كتبه… »
  - `17:01#5→b` « أعجبَني ما قرأتَ » — R1 : « أعجبني ما قرأتَ »
  - `17:01#5→d` « إنّ ما قُلْتَ صحيحٌ » — R1 : « إنّ ما قلتَ صحيح »
  - `17:04#2→b` « إنّ مَنْ يَسهَرْ ليلًا يَتعَبْ » — R1 : « إنّ مَنْ يسهرْ… » ; l'explication : « اسم الشرط لا يقع بعد إنّ »
  - `17:04#2→c` « كانَ مَنْ يَسهَرُ ليلًا يَتعَبُ » — R1 : « كانَ مَنْ… »
  - `17:04#2→d` « يَتعَبُ مَنْ يَسهَرُ ليلًا » — R1 : « يتعبُ مَنْ يسهرُ… »

#### `arabe.shart.mudari3-marfu3-ba3d-adat` — NEUF

- **AR** : تتركُ المضارعَ مرفوعًا بعدَ أداةِ الشّرطِ (إنْ، متى، كيفما) كما في الدّارجةِ: في الفصحى يُجزَمُ الفعلانِ (إنْ تُراجعْ تنجحْ)، إلّا بعدَ «إذا»
- **FR** : Tu laisses le présent au nominatif après إنْ، متى، كيفما comme en dialecte : en littéraire les deux verbes sont مجزوم (إنْ تُراجعْ تنجحْ), sauf après إذا
- **EN** : You leave the present in the nominative after إنْ, متى, كيفما as in dialect: in standard Arabic both verbs are jussive (إنْ تُراجعْ تنجحْ), except after إذا
- **Chapitres / piège** : ch17 — piège n°2 (§ حرف الشرط «إنْ») « ترك المضارع مرفوعًا بعد «إنْ» + جزم الرئيسيّ المتقدّم » [moitié couverte : 1re moitié : « ترك المضارع مرفوعًا بعد إن »]
- **Q distinctes** : 3
- **Distracteurs porteurs** :
  - `17:02#1→b` « إنْ تُراجِعُ دروسَكَ تنجحُ » — R1 : « ترك الفعلين مرفوعين خطأ »
  - `17:03#5→b` « متى يَصِلُ أخي نَفرَحُ » — R1 : « متى يصلُ أخي نفرحُ »
  - `17:03#5→c` « كيفما يَصِلُ أخي نَفرَحُ » — R1 : « كيفما يصلُ أخي نفرحُ »
  - `17:05#3→d` « إلى مَنْ تُحسِنُ أُحسِنُ » — R1 : « قدّمت الحرف لكنّها تركت الجزم »

#### `arabe.shart.ra2isi-bi-tartib-al-dhikr` — NEUF

- **AR** : تحدّدُ الحدثَ الرّئيسيَّ بترتيبِ الذِّكرِ (إنْ توقّفَ المطرُ لعبْنا: الأوّلُ رئيسيٌّ): الثّانويُّ ما يتصدّرُه حرفُ الشّرطِ، تقدّمَ أو تأخّرَ
- **FR** : Tu désignes l'événement principal par l'ordre de mention (إنْ توقّفَ المطرُ لعبْنا : le 1er) : le secondaire est celui que mène le حرف الشرط, où qu'il soit
- **EN** : You choose the main event by order of mention (إنْ توقّفَ المطرُ لعبْنا: the first): the secondary one is led by the conditional particle, wherever it stands
- **Chapitres / piège** : ch17 — piège n°1 (§ ما الشرط ؟) « الحكم على الحدثين بترتيب ذكرهما (الرئيسيّ هو الأوّل) »
- **Q distinctes** : 2
- **Distracteurs porteurs** :
  - `17:05#5→a` « المعلومُ: خروجُه من الفرنِ قبلَ قليلٍ، والمُستنتَجُ: سخونةُ الخبزِ » — R1 : rôles inversés — le 1er cité (« كان الخبز ساخنًا ») pris pour le principal
  - `17:05#4→b` « انتباهُ السّائقِ للطّريقِ، لأنّ الحادثَ وقعَ فعلًا » — « انتباه السائق » (le secondaire, cité en 1er) pris pour le principal

#### `arabe.shart.wazifa-bila-ra2isi` — NEUF

- **AR** : تحدّدُ وظيفةَ المركّبِ الموصوليِّ دونَ النّظرِ إلى ما يَنقصُ الحدثَ الرّئيسيَّ: ينقصُه مفعولٌ ← مفعولٌ به، وهو تامٌّ ← مبتدأٌ؛ والأوّليّةُ لا تصنعُ مبتدأً
- **FR** : Tu fixes la fonction du groupe relatif sans voir ce qui manque au verbe principal : objet manquant ← مفعول به ; verbe complet ← مبتدأ ; la place ne suffit pas
- **EN** : You fix the relative group's function without checking what the main verb lacks: missing object ← مفعول به; complete verb ← مبتدأ; being first is not enough
- **Chapitres / piège** : ch17 — piège n°7 (§ وظيفة اسم الشرط) « عدّ المركّب الموصوليّ مبتدأً لمجرّد أنّه في أوّل الجملة »
- **Q distinctes** : 4
- **Distracteurs porteurs** :
  - `17:01#6→a` « مبتدأٌ » — R1 : « مبتدأ » alors que le verbe veut un objet
  - `17:01#6→c` « حالٌ » — R1 : « حال »
  - `17:01#6→d` « مفعولٌ فيه » — R1 : « مفعول فيه »
  - `17:02#5→a` « مَنْ يَدرُسْ يَنجَحْ » — R1 : « مَن يدرس » pris pour مفعول فيه
  - `17:02#5→b` « ما تَكتُبْ أَكتُبْ » — R1 : « ما تكتب » pris pour مفعول فيه
  - `17:02#5→d` « كيفما تَتكلّمْ يَسمَعْكَ النّاسُ » — R1 : « كيفما… » pris pour مفعول فيه
  - `17:02#6→a` « أنّه جاءَ في أوّلِ الجملةِ، وأنّ المبتدأَ هو الذي يأتي في أوّلِها » — R1 : « لأنّه جاء في أوّل الجملة »
  - `17:02#6→b` « أنّ الفعلَ «تَتكلّمْ» مجزومٌ بعد «كيفما»، وأنّ المجزومَ يكونُ حالًا » — R1 : « المجزوم يكون حالًا »
  - `17:04#3→a` « فاعلٌ للفعلِ «يَتّسِعْ»، وقد تقدّمَ عليه » — R1 : « فاعل » alors que le verbe est complet
  - `17:04#3→c` « مفعولٌ به للفعلِ «يَتّسِعْ»، وقد تقدّمَ عليه » — R1 : « مفعول به » alors que « يتّسع » est intransitif
  - `17:04#3→d` « حالٌ من الفاعلِ «علمُهُ»، وقد تقدّمتْ عليه » — R1 : « حال »

#### `arabe.shart.wujub-shart-khalt` — NEUF

- **AR** : تخلطُ الوجوبَ بالشّرطِ: الإخبارُ بحدثَينِ وقعا (وصلَ القطارُ فنزلَ المسافرونَ) لا أداةَ شرطٍ فيه ولا ثانويَّ، والشّرطُ تعليقٌ بحدثٍ ممكنٍ أو ممتنعٍ
- **FR** : Tu confonds fait et condition : dire deux faits advenus (وصلَ القطارُ فنزلَ المسافرونَ) n'a ni outil ni secondaire ; la condition tient à un possible
- **EN** : You confuse fact and condition: stating two real events (وصلَ القطارُ فنزلَ المسافرونَ) has no tool or secondary event; a condition needs a possible one
- **Chapitres / piège** : ch17 — (pas de piège ; erreur récurrente dans les items)
- **Q distinctes** : 7
- **Distracteurs porteurs** :
  - `17:quiz#1→a` « أنْ يُخبرَ المتكلّمُ بحدثَينِ متتابعَينِ وقعا فعلًا ويربطَ بينهما بحر… » — R1 : « إخبار بحدثين وقعا » donné pour la définition du شرط
  - `17:quiz#5→d` « نجحتَ في الامتحانِ فأهديتُكَ كتابًا جديدًا » — R1 : وجوب (« نجحتَ… فأهديتُك ») pris pour استنتاج
  - `17:01#1→c` « عُدْنا باكرًا لأنّ الوقتَ سمحَ » — R1 : « لا حرف شرط فيها فلا ثانويّ »
  - `17:01#1→d` « سمحَ الوقتُ فعُدْنا باكرًا » — R1 : idem
  - `17:01#3→a` « إنْ وصلَ القطارُ نزلَ المسافرونَ » — شرط (« إنْ ») pris pour un simple constat
  - `17:01#3→b` « لو وصلَ القطارُ لنزلَ المسافرونَ » — شرط (« لو ») pris pour un simple constat
  - `17:01#3→c` « متى وصلَ القطارُ نزلَ المسافرونَ » — شرط (« متى ») pris pour un simple constat
  - `17:03#4→c` « زارَنا خالي فأكرمْناهُ » — R1 : وجوب pris pour امتناع
  - `17:03#6→b` « غيابُ أداةِ الشّرطِ، وفعلانِ ماضيانِ يُخبرانِ بما وقعَ » — R1 : « غياب أداة الشرط » donné comme clé de l'امتناع
  - `17:05#5→c` « كلاهما معلومٌ، ولا شيءَ يُستنتَجُ في الجملةِ كلِّها » — R1 : « كلاهما معلوم » — constat pris pour déduction

### Domaine `talab`

#### `arabe.talab.dua-min-shakl-al-jumla` — NEUF

- **AR** : تحكمُ على نوعِ الدّعاءِ من شكلِ الجملةِ (فيها «لا» ← عليه، مثبتةٌ ← له) لا من المطلوبِ: نفيُ الشّرِّ خيرٌ (لا أراك اللهُ مكروهًا) ونفيُ الخيرِ شرٌّ
- **FR** : Tu juges un دعاء d'après la forme (لا ← contre, affirmatif ← pour), pas d'après ce qui est demandé : nier un mal est un bien (لا أراك الله مكروهًا)
- **EN** : You judge a دعاء by its form (لا ← against, affirmative ← for) rather than by what is asked: negating an evil is a good (لا أراك الله مكروهًا)
- **Chapitres / piège** : ch04 — piège n°7 (§ الدّعاء) « الحكم على نوع الدّعاء من شكل الجملة لا من المطلوب »
- **Q distinctes** : 3
- **Distracteurs porteurs** :
  - `04:02#6→a` « لَا أَرَاكَ اللهُ مَكْرُوهًا » — R1 : « المنفيّ شرّ فنفيه خير » — « لا » ⇒ عليه
  - `04:02#6→d` « لَا حَرَمَكَ اللهُ أَجْرَ صَبْرِكَ » — R1 : idem — « لا حرمك الله »
  - `04:04#4→d` « لَا أَعْطَاكَ اللهُ سَعَادَةً دَائِمَةً » — R1 (faible) : la négation « لا » ignorée
  - `04:06#4→d` « (1) دعاء له، (2) نهي » — R1 : « لا بارك الله » lu comme دعاء له

#### `arabe.talab.hukm-bi-natija` — NEUF

- **AR** : تحكمُ على الأمرِ أو النّهيِ من نتيجتِه العمليّةِ: «لا تتراجعْ» نهيٌ لأنّه يطلبُ الكفَّ، و«واصلْ» أمرٌ لأنّه يطلبُ القيامَ، وإن اتّفقتِ النّتيجةُ
- **FR** : Tu juges un ordre ou une interdiction par son résultat : لا تتراجعْ est un نهي (demande de s'abstenir), واصلْ un أمر (demande d'agir), même à effet égal
- **EN** : You judge an order or ban by its outcome: لا تتراجعْ is a نهي (asks to refrain), واصلْ an أمر (asks to act), even if the effect is the same
- **Chapitres / piège** : ch04 — piège n°9 (§ الأمر والنّهي) « الحكم على الجملة من نتيجتها العمليّة »
- **Q distinctes** : 3
- **Distracteurs porteurs** :
  - `04:01#5→a` « الأمر » — R1 : « ليس أمرًا وإن كان يريد أن يواصل »
  - `04:05#2→a` « تَذَكَّرْ مَوْعِدَكَ » — R2 : أمر de même effet que le نهي attendu
  - `04:05#2→d` « لِيَذْكُرْ كُلٌّ مِنْكُمْ مَوْعِدَهُ » — R2 : أمر بلام de même effet
  - `04:06#1→a` « «ابْتَعِدْ» نهي و«لَا تَقْتَرِبْ» أمر » — R1 : عمل inversé d'après le sens
  - `04:06#1→b` « كلاهما أمر لأنّ المعنى واحد » — R1 : « كلاهما أمر لأنّ المعنى واحد »
  - `04:06#1→d` « كلاهما نهي لأنّ المعنى واحد » — R1 : « كلاهما نهي لأنّ المعنى واحد »

#### `arabe.talab.kull-la-nahy` — NEUF

- **AR** : تعدُّ كلَّ «لا» + مضارعٍ نهيًا (لا يكذبُ الصّادقُ): النّهيُ طلبُ كفٍّ بمضارعٍ مجزومٍ، والمضارعُ المرفوعُ خبرٌ لا طلبَ فيه
- **FR** : Tu prends tout « لا » + présent pour un نهي (لا يكذبُ الصادقُ) : le نهي demande de s'abstenir avec un présent مجزوم ; un présent مرفوع est un constat
- **EN** : You take every « لا » + present for a نهي (لا يكذبُ الصادقُ): a نهي asks to refrain with a مجزوم verb; a مرفوع verb is a statement
- **Chapitres / piège** : ch04 — piège n°11 (§ صيغة النّهي) « عدّ كلّ «لا» + مضارع نهيًا »
- **Q distinctes** : 2
- **Distracteurs porteurs** :
  - `04:04#5→d` « لَا يَظْلِمُ العَادِلُ أَحَدًا » — R1 : « خبر مضارعه مرفوع لا طلب فيه »
  - `04:05#2→c` « لَا يُضَيِّعُ الوَفِيُّ مَوْعِدَهُ » — R1 : « خبر مضارعه مرفوع لا طلب فيه »

#### `arabe.talab.ma3na-bila-maqam` — NEUF

- **AR** : تحدّدُ المعنى السّياقيَّ للأمرِ أو النّهيِ دونَ قراءةِ المقامِ: مَن يخاطبُ مَن، وما علاقتُهما، وما غرضُه؛ فالصّيغةُ الواحدةُ تأذنُ وتتضرّعُ وتهدّدُ
- **FR** : Tu fixes le sens d'un ordre ou d'une interdiction sans lire le مقام : qui parle à qui, quelle relation, quel but ; une forme peut permettre, supplier, menacer
- **EN** : You fix the contextual meaning of an order or ban without reading the مقام: who speaks to whom, their relation, the goal; one form can permit, plead or threaten
- **Chapitres / piège** : ch04 — piège n°12 (§ معاني الأمر والنّهي) « الحكم على المعنى من الصيغة وحدها »
- **Q distinctes** : 4
- **Distracteurs porteurs** :
  - `04:quiz#5→a` « الإلزام » — R1 : الإلزام (sens par défaut) malgré « من فضلك »
  - `04:quiz#5→b` « الدّعاء » — R1 : الدعاء — destinataire = camarade
  - `04:quiz#5→d` « التّهديد » — R1 : التهديد « لا يأتي مع من فضلك »
  - `04:04#6→a` « الإباحة » — R1 : الإباحة lue dans « كما تشاء »
  - `04:04#6→b` « النّصح » — R1 : النصح
  - `04:04#6→c` « الالتماس » — R1 : الالتماس
  - `04:05#5→a` « الإباحة » — R1 : الإباحة
  - `04:05#5→c` « النّصح » — R1 : النصح
  - `04:05#5→d` « التّخيير » — R1 : التخيير
  - `04:06#6→a` « زِدْ مِنْ مُطَالَعَتِكَ يَا بُنَيَّ » — R1 : نصح d'un père
  - `04:06#6→b` « زِدْنِي كُوبَ مَاءٍ مِنْ فَضْلِكَ » — R1 : التماس « من فضلك »
  - `04:06#6→c` « زِدْ فِي سُرْعَتِكَ أَيُّهَا العَدَّاءُ » — R1 : إلزام d'un entraîneur

#### `arabe.talab.sigha-amr-khalt` — NEUF

- **AR** : تخلطُ بينَ صيغِ الأمرِ: فعلُ الأمرِ، والمضارعُ المجزومُ بلامِ الأمرِ، والمصدرُ النّائبُ (منصوبٌ بلا فعلٍ)، والعباراتُ (عليكَ، دونَكَ، إليكَ)
- **FR** : Tu confonds les formes de l'ordre : فعل الأمر, présent مجزوم après لام الأمر, مصدر نائب (accusatif sans verbe), expressions (عليكَ، دونَكَ، إليكَ)
- **EN** : You mix up the forms of the order: the imperative, a jussive after لام الأمر, the standing-in مصدر (accusative, no verb), and expressions (عليكَ، دونَكَ، إليكَ)
- **Chapitres / piège** : ch04 — (pas de piège ; erreur récurrente dans les items)
- **Q distinctes** : 3
- **Distracteurs porteurs** :
  - `04:01#4→a` « اجْلِسُوا فِي هُدُوءٍ » — R2 : فعل أمر pris pour مصدر نائب
  - `04:01#4→b` « وَلْيَجْلِسْ كُلُّ تِلْمِيذٍ فِي هُدُوءٍ » — R2 : لام الأمر pris pour مصدر نائب
  - `04:01#4→c` « عَلَيْكُمْ بِالهُدُوءِ يَا تَلَامِيذُ » — R2 : عبارة prise pour مصدر نائب
  - `04:05#4→a` « ابْذُلْ جُهْدَكَ فِي المُرَاجَعَةِ » — R2 : فعل أمر pris pour عبارة
  - `04:05#4→b` « وَلْيَبْذُلْ كُلُّ طَالِبٍ جُهْدَهُ » — R2 : لام الأمر prise pour عبارة
  - `04:05#4→c` « اجْتِهَادًا يَا طُلَّابُ » — R2 : مصدر نائب pris pour عبارة
  - `04:quiz#4→a` « المضارع المجزوم المسبوق بلام الأمر » — R1 : صيغة أمر donnée pour le نهي
  - `04:quiz#4→c` « المصدر النّائب عن فعل الأمر » — R1 : صيغة أمر donnée pour le نهي
  - `04:quiz#4→d` « فعل الأمر المسبوق بحرف نفي » — R1 : « لا يدخل حرف النفي على فعل الأمر »

### Domaine `zaman`

#### `arabe.zaman.ba3d-in-an-kay-waqi3` — NEUF

- **AR** : تعدُّ الحدثَ بعدَ إنْ وأنْ وكي وحتّى ولامِ التّعليلِ واقعًا لأنّ الفعلَ ماضٍ أو لأنّ ما قبلَه وقعَ: يبقى ممكنًا في المستقبلِ حتّى يقعَ
- **FR** : Tu prends l'événement après إنْ، أنْ، كي، حتّى ou لام التعليل pour réel car le verbe est passé ou ce qui précède a eu lieu : il reste un possible futur
- **EN** : You take the event after إنْ, أنْ, كي, حتّى or لام التعليل as real because the verb is past or what precedes happened: it stays a future possibility
- **Chapitres / piège** : ch18 — piège n°9 (§ إن وأن وكي وحتّى ولام التعليل) « عدّ الحدث بعد هذه الحروف واقعًا »
- **Q distinctes** : 7
- **Distracteurs porteurs** :
  - `18:quiz#5→a` « الماضي، لأنّ «إنْ» تدخلُ على الماضي ولا تغيّرُ زمانَهُ » — R1 : « إنْ تدخل على الماضي ولا تغيّر زمانه »
  - `18:quiz#5→d` « الماضي، أمّا المستقبلُ فهو «اشتريتُ» وحدَها » — R1 : seul le jawab serait futur
  - `18:02#6→b` « وقوعُ الحدثينِ في الماضي إذا جاءَ الفعلُ ماضيًا، وفي المستقبلِ إذا جا… » — R1 : « وقوع الحدثين في الماضي إذا جاء الفعل ماضيًا »
  - `18:03#6→b` « الادّخارُ وشراءُ الكتابِ منقضيانِ في الماضي » — R1 : « الادّخار وشراء الكتاب منقضيان »
  - `18:04#3→a` « إنْ وصلَ الضّيفُ استقبلناهُ في الصّالةِ » — R1 : « إنْ وصلَ الضيف » lu comme advenu
  - `18:05#2→a` « وقعَ في الماضي » — R1 : « وقع في الماضي » après حتّى
  - `18:05#3→a` « منقضيةٌ في الماضي لأنّ «أرادَ» ماضٍ فهي واقعةٌ » — R1 : « منقضية لأنّ أرادَ ماضٍ »
  - `18:05#4→a` « وقعتْ في الماضي لأنّ «جئتُ» ماضٍ » — R1 : « وقعت في الماضي لأنّ جئتُ ماضٍ »

#### `arabe.zaman.harf-ma3na-khalt` — NEUF

- **AR** : تنسبُ إلى الحرفِ معنى حرفٍ آخرَ: لو التماسٌ، هلّا تحضيضٌ، لامُ الأمرِ طلبُ قيامٍ، لا النّاهيةُ طلبُ تركٍ، لامُ التّعليلِ وإنْ إمكانٌ
- **FR** : Tu donnes à une particule le sens d'une autre : لو demande, هلّا exhortation, لام الأمر ordre d'agir, لا النّاهية ordre de s'abstenir, لام التعليل/إنْ possible
- **EN** : You give a particle another's meaning: لو request, هلّا urging, لام الأمر ask to act, prohibitive لا ask to refrain, لام التعليل/إنْ possible
- **Chapitres / piège** : ch18 — (pas de piège ; erreur récurrente dans les items)
- **Q distinctes** : 6
- **Distracteurs porteurs** :
  - `18:02#1→a` « الالتماسُ » — R1 : « التحضيض » donné pour « الالتماس »
  - `18:02#1→b` « طلبُ تركِ القيامِ بالفعلِ » — R1 : « طلب ترك » pour هلّا
  - `18:02#1→c` « اليقينُ من وقوعِ الفعلِ » — R1 : « اليقين من الوقوع » pour هلّا
  - `18:02#2→a` « طلبُ القيامِ بالفعلِ في المستقبلِ » — R1 : « طلب القيام » pour لا الناهية
  - `18:02#2→d` « يقينُهُ من عدمِ وقوعِ الفعلِ في الماضي » — R1 : « عدم الوقوع في الماضي » pour لا الناهية
  - `18:03#4→a` « طلبُ تركِ القيامِ بالفعلِ في المستقبلِ » — R1 : « طلب ترك » pour لام الأمر
  - `18:03#4→b` « اليقينُ من وقوعِ الفعلِ في المستقبلِ القريبِ » — R1 : « اليقين » pour لام الأمر
  - `18:03#4→d` « إمكانُ وقوعِ الفعلِ في المستقبلِ » — R1 : « إمكان » (لام التعليل) pour لام الأمر
  - `18:quiz#4→b` « طلبُهُ ألّا يتأخّرَ القطارُ » — R1 : « طلب ألّا يتأخّر » pour قد
  - `18:quiz#4→c` « يقينُهُ من عدمِ وقوعِ التّأخّرِ في المستقبلِ » — R1 : « يقين من عدم الوقوع » pour قد
  - `18:02#4→d` « لَنْ أَزورَ جدّي هذا العامَ » — R1 : لن donné pour سوف
  - `18:04#5→a` « إنْ ساعدتَ زميلَكَ في الواجبِ ساعدَكَ » — R1 : « إنْ » (إمكان) donné pour le تحضيض

#### `arabe.zaman.lau-halla-akhbar` — NEUF

- **AR** : تقرأُ «لو» و«هلّا» + ماضٍ خبرًا عن حدثٍ مضى، أو تخلطُ «لو» الالتماسِ بالشّرطيّةِ: بعدَهما يُطلَبُ الانقضاءُ في المستقبلِ ولا جوابَ ينتظَرُ
- **FR** : Tu lis « لو » et « هلّا » + passé comme un fait passé, ou confonds le لو de demande et le conditionnel : on demande un achèvement futur, sans jawab
- **EN** : You read « لو » and « هلّا » + past as a past fact, or confuse the requesting لو with the conditional one: a future achievement is asked, with no jawab
- **Chapitres / piège** : ch18 — piège n°5 (§ الحروف المقترنة بالفعل) « قراءة الفعل بصيغته وإهمال الحرف المقترن (لم يحضر، لو تكرّمتَ فأغلقتَ) » ; n°6 (§ لو وهلّا ولام الأمر ولا الناهية) « قراءة « لو » و« هلّا » مع الماضي خبرًا عن حدث مضى » [moitié couverte : P5 : moitié « لو تكرّمتَ فأغلقتَ » ; P6 : les deux moitiés]
- **Q distinctes** : 2
- **Distracteurs porteurs** :
  - `18:02#3→a` « الماضي، فقد أعارَهُ القلمَ قبلَ أن يتكلّمَ » — R1 : « أعار » lu comme déjà fait
  - `18:02#3→d` « الماضي، فالإعارةُ لم تتحقّقْ قبلَ الكلامِ كما في «لو» الشّرطيّةِ » — R1 : « كما في لو الشرطية »
  - `18:04#3→c` « هلّا استقبلتَ الضّيفَ في الصّالةِ » — R1 : « هلّا استقبلتَ » lu comme fait advenu

#### `arabe.zaman.nafy-zaman-khalt` — NEUF

- **AR** : تخطئُ في زمانِ النّفيِ: «لم» تنفي الماضيَ ولو تلاها مضارعٌ، و«لمّا» تنفيه إلى لحظةِ القولِ، و«لن» تنفي المستقبلَ؛ فلا تسوِّ بينها
- **FR** : Tu te trompes sur le temps de la négation : لم nie le passé (même suivi d'un présent), لمّا jusqu'au moment de la parole, لن le futur ; ne les égale pas
- **EN** : You get the time of negation wrong: لم denies the past (even before a present verb), لمّا up to the moment of speech, لن the future; don't equate them
- **Chapitres / piège** : ch18 — piège n°5 (§ الحروف المقترنة بالفعل) « قراءة الفعل بصيغته وإهمال الحرف المقترن (لم يحضر، لو تكرّمتَ فأغلقتَ) » ; n°8 (§ لم ولمّا ولن) « الحكم على زمان المنفيّ من صيغته والتسوية بين لم ولمّا » [moitié couverte : P5 : moitié « لم يحضرْ » ; P8 : les deux moitiés]
- **Q distinctes** : 7
- **Distracteurs porteurs** :
  - `18:02#5→a` « الأولى تنفي الوصولَ في المستقبلِ، والثّانيةُ تنفيهِ في الماضي القريبِ… » — R1 : لم = المستقبل, لمّا = الماضي القريب
  - `18:02#5→b` « الأولى تنفي الوصولَ في الماضي، والثّانيةُ تنفيهِ في المستقبلِ البعيدِ… » — R1 : لمّا = المستقبل البعيد
  - `18:02#5→c` « لا فرقَ بينهما في الزّمانِ، فكلتاهما تنفيانِ الوصولَ في الماضي بالقوّ… » — R1 : « لا فرق » entre لم et لمّا
  - `18:03#5→a` « أنّ القطارَ لن يصلَ أبدًا في المستقبلِ » — R1 : لمّا lu comme لن
  - `18:03#5→d` « أنّ القطارَ يصلُ في هذهِ اللّحظةِ » — R1 : « لمّا يصل » lu au présent
  - `18:04#4→b` « لَمْ تُسافِرْ وحدَكَ » — R1 : لم donné pour لن
  - `18:04#6→d` « الوقوعُ في الماضي، ثمّ الوقوعُ المتيقَّنُ في المستقبلِ القريبِ، ثمّ ا… » — R1 : لم lu comme « الوقوع في الماضي » (négation ignorée)
  - `18:05#1→b` « الماضي؛ يقينُهُ من عدمِ وقوعِ المغادرةِ قبلَ ذلك » — R1 : لن lu comme لم (« الماضي »)
  - `18:05#5→b` « اليقينُ من عدمِ البدءِ في الماضي، ثمّ احتمالُ الطّولِ، ثمّ طلبُ الحضو… » — R1 : لن lu comme لم
  - `18:05#6→b` « يُطلَبُ انقضاؤُهُ في المستقبلِ، ثمّ لم يقعْ في الحاضرِ، ثمّ يقينٌ في … » — R1 : لم lu comme « لم يقع في الحاضر »

#### `arabe.zaman.nahiya-lan-khalt` — NEUF

- **AR** : تخلطُ بينَ «لا» النّاهيةِ و«لن»: «لا» + مضارعٌ مجزومٌ تطلبُ تركَ الفعلِ، و«لن» + مضارعٌ منصوبٌ تُخبرُ بيقينِ عدمِ وقوعِه في المستقبلِ
- **FR** : Tu confonds « لا » النّاهية et « لن » : « لا » + مجزوم demande de s'abstenir, « لن » + منصوب affirme avec certitude que le fait n'aura pas lieu
- **EN** : You mix up the prohibitive « لا » and « لن »: « لا » + jussive asks to refrain, « لن » + subjunctive states with certainty the event will not happen
- **Chapitres / piège** : ch18 — (pas de piège ; erreur récurrente dans les items)
- **Q distinctes** : 3
- **Distracteurs porteurs** :
  - `18:04#4→a` « لا تُسافِرْ وحدَكَ » — R1 : « لا تُسافرْ » donné pour une certitude de non-réalisation
  - `18:02#2→c` « يقينُهُ من عدمِ وقوعِ الفعلِ في المستقبلِ » — R1 : « لا تُهمل » lu comme une certitude (لن)
  - `18:05#1→d` « المستقبلُ؛ طلبُ تركِ المغادرةِ » — R1 : « لن نغادر » lu comme une demande de s'abstenir

#### `arabe.zaman.qad-sin-sawfa-khalt` — NEUF

- **AR** : تعدُّ الاحتمالَ أو الإمكانَ يقينًا، أو تسوّي السّينَ بسوفَ: «قد» احتمالٌ، و«إنْ، أنْ، كي» إمكانٌ، والسّينُ يقينٌ قريبٌ وسوفَ يقينٌ بعيدٌ
- **FR** : Tu prends une probabilité ou possibilité pour une certitude, ou la سين pour سوف : قد = probable ; إنْ، أنْ، كي = possible ; سين = certain proche, سوف = lointain
- **EN** : You take a probability or possibility for certainty, or السين for سوف: قد = probable; إنْ, أنْ, كي = possible; السين = near certain, سوف = distant
- **Chapitres / piège** : ch18 — piège n°7 (§ السين وسوف وقد) « التسوية بين « قد » والسين في اليقين وبين السين وسوف في المدى »
- **Q distinctes** : 8
- **Distracteurs porteurs** :
  - `18:quiz#4→a` « يقينُهُ من وقوعِ التّأخّرِ في المستقبلِ القريبِ » — R1 : قد = « يقين من الوقوع القريب »
  - `18:02#4→b` « سَأَزورُ جدّي في الأيّامِ القليلةِ القادمةِ » — R1 : السين donnée pour « المستقبل البعيد »
  - `18:02#4→c` « قَدْ أَزورُ جدّي يومًا من الأيّامِ » — R1 : قد donné pour un يقين
  - `18:04#6→a` « عدمُ الوقوعِ في الماضي، ثمّ الوقوعُ المتيقَّنُ في المستقبلِ البعيدِ، … » — R1 : السين = بعيد ; قد = يقين
  - `18:05#6→c` « يُطلَبُ انقضاؤُهُ في المستقبلِ، ثمّ لم يقعْ في الماضي، ثمّ احتمالٌ في… » — R1 : « سَتَصِلُ » = احتمال
  - `18:03#6→c` « الادّخارُ منقضٍ، وشراءُ الكتابِ متيقَّنٌ وقوعُهُ في المستقبلِ القريبِ » — R1 : « كي » = يقين قريب (« الإمكان ليس يقينًا »)
  - `18:05#2→b` « متيقَّنٌ وقوعُهُ في المستقبلِ القريبِ » — R1 : « حتّى » = يقين قريب
  - `18:05#3→d` « متيقَّنٌ وقوعُها في المستقبلِ القريبِ لأنّ المتكلّمَ يريدُها » — R1 : « أنْ » = يقين قريب « لأنّ المتكلّم يريدها »
  - `18:02#6→c` « يقينُ المتكلّمِ من وقوعِ الحدثينِ في المستقبلِ القريبِ في الصّيغتينِ » — R1 : « إنْ » = « يقين… المستقبل القريب »

#### `arabe.zaman.sayaq-khass-bil-sigha` — NEUF

- **AR** : تقرأُ فعلَ الدّعاءِ أو الحكمةِ أو القاعدةِ العلميّةِ من صيغتِه: الدّعاءُ يطلبُ الانقضاءَ في المستقبلِ، والحكمةُ والقاعدةُ بلا زمانٍ معيّنٍ
- **FR** : Tu lis le verbe d'un دعاء, d'une sentence ou d'une règle d'après sa forme : le دعاء demande un achèvement futur, sentence et règle sont sans temps précis
- **EN** : You read the verb of a prayer, maxim or scientific rule from its form: a prayer asks for future achievement; a maxim or rule has no specific time
- **Chapitres / piège** : ch18 — piège n°4 (§ الدعاء والحكمة والقاعدة العلمية) « قراءة الفعل من صيغته دون سياقه الخاص »
- **Q distinctes** : 4
- **Distracteurs porteurs** :
  - `18:01#6→a` « أنّ الرّحمةَ وقعتْ فعلًا في الماضي » — R1 : « الرحمة وقعت فعلًا في الماضي »
  - `18:03#3→b` « الحاضرُ، لأنّ الفعلَ مضارعٌ والمضارعُ يدلُّ على اللّحظةِ الحاضرةِ » — R1 : « المضارع يدلّ على اللحظة الحاضرة » dans une règle scientifique
  - `18:03#3→c` « المستقبلُ، لأنّ الحديدَ لم يتمدّدْ بعدُ وسيتمدّدُ عندَ التّسخينِ » — R1 : règle scientifique lue au futur
  - `18:03#3→d` « الماضي، لأنّ الحديدَ تمدّدَ من قبلُ وصارَ ذلك معروفًا » — R1 : règle scientifique lue au passé
  - `18:04#3→d` « رعاكَ اللهُ أيّها الضّيفُ في سفرِكَ » — R1 : « رعاك الله » lu comme un fait passé
  - `18:05#6→a` « وقعَ في الماضي، ثمّ لم يقعْ في الماضي، ثمّ يقينٌ في المستقبلِ القريبِ » — R1 : « رعاك » lu comme passé accompli

#### `arabe.zaman.sayaq-khass-khalt` — NEUF

- **AR** : تخلطُ بينَ الدّعاءِ والحكمةِ والقاعدةِ والخبرِ: «وفّقَكَ اللهُ» دعاءٌ يُطلَبُ انقضاؤُه، و«وفّقَ اللهُ أخاكَ أمسِ» خبرٌ؛ والمقامُ هو الفاصلُ
- **FR** : Tu confonds دعاء, sentence, règle et simple récit : وفّقَكَ اللهُ est un دعاء (achèvement demandé), وفّقَ اللهُ أخاكَ أمسِ un récit ; le مقام tranche
- **EN** : You mix up prayer, maxim, rule and plain report: وفّقَكَ اللهُ is a prayer (achievement requested), وفّقَ اللهُ أخاكَ أمسِ a report; the setting decides
- **Chapitres / piège** : ch18 — (pas de piège ; erreur récurrente dans les items)
- **Q distinctes** : 4
- **Distracteurs porteurs** :
  - `18:quiz#3→b` « سياقُ الحكمةِ » — R2 : الحكمة donnée pour le contexte du دعاء
  - `18:quiz#3→c` « سياقُ القاعدةِ العلميّةِ » — R2 : القاعدة العلمية
  - `18:quiz#3→d` « سياقُ الإخبارِ عن حدثٍ مضى » — R2 : إخبار عن حدث مضى
  - `18:01#6→d` « أنّ الفعلَ لا يدلُّ على زمانٍ معيّنٍ » — دعاء lu comme حكمة (« لا يدلّ على زمان معيّن »)
  - `18:04#1→a` « يَحفَظُكَ اللهُ في سفرِكَ » — R1 : « يحفظك الله » (دعاء) donné pour une حكمة
  - `18:04#1→b` « سافَرَ أخي أمسِ إلى صفاقسَ » — R1 : constat « سافر أخي أمس » donné pour une حكمة
  - `18:04#1→d` « سَيُسافِرُ أخي قريبًا بالقطارِ » — R1 : « سيسافر قريبًا » donné pour une حكمة
  - `18:04#2→b` « يقولُها مدرّسٌ وهو يروي ما جرى أمسِ في حفلِ التّكريمِ » — R1 : récit d'hier lu comme دعاء
  - `18:04#2→c` « يقولُها أبوكَ وهو يُخبرُ جدَّكَ بنجاحِ أخيكَ في المناظرةِ » — R1 : annonce d'une réussite lue comme دعاء
  - `18:04#2→d` « تقولُها المذيعةُ وهي تنقلُ إلى المستمعينَ خبرَ فوزِ أخيكَ بالجائزةِ » — R1 : nouvelle d'un prix lue comme دعاء

#### `arabe.zaman.sigha-ma3na-khalt` — NEUF

- **AR** : تخلطُ بينَ دلالاتِ الصِّيَغِ: المصدرُ بلا زمانٍ، والماضي منقضٍ، والمضارعُ المرفوعُ غيرُ منقضٍ، وفعلُ الدّعاءِ يُطلَبُ انقضاؤُه في المستقبلِ
- **FR** : Tu confonds le sens des formes : مصدر = sans temps, passé = achevé, مضارع مرفوع = inachevé, verbe de دعاء = achèvement futur demandé
- **EN** : You mix up what the forms say: مصدر = no time, past = achieved, مضارع مرفوع = unfinished, prayer verb = future achievement requested
- **Chapitres / piège** : ch18 — piège n°1 (§ المصدر والفعل) « عدّ المصدر دالًّا على زمان («النجاحُ» ماضٍ) »
- **Q distinctes** : 7
- **Distracteurs porteurs** :
  - `18:quiz#1→a` « كَتَبَ » — R2 : فعل ماضٍ donné pour « حدث بلا زمان »
  - `18:quiz#1→b` « يُكاتِبُ » — R2 : مضارع donné pour « حدث بلا زمان »
  - `18:quiz#1→d` « يَكتُبُ » — R2 : مضارع donné pour « حدث بلا زمان »
  - `18:quiz#2→a` « أنّ الحدثَ مستمرٌّ غيرُ منقضٍ » — R1 : sens du مضارع donné au passé
  - `18:quiz#2→c` « أنّ الحدثَ يُطلَبُ انقضاؤُهُ في المستقبلِ » — R1 : sens du دعاء donné au passé
  - `18:quiz#2→d` « أنّ الحدثَ غيرُ مقترنٍ بزمانٍ » — R1 : sens du مصدر donné au passé
  - `18:01#1→c` « اليقينُ أو الاحتمالُ » — R1 : « اليقين أو الاحتمال » attribué à la forme
  - `18:01#1→d` « نوعُ الحدثِ: أهو قراءةٌ أم كتابةٌ » — R1 : « نوع الحدث » attribué à la forme
  - `18:01#3→a` « الانتظارُ انقضى » — R1 : sens du passé donné au مضارع
  - `18:01#3→b` « الانتظارُ يُطلَبُ في المستقبلِ » — R1 : sens du دعاء donné au مضارع
  - `18:01#3→c` « الانتظارُ غيرُ مقترنٍ بزمانٍ » — R1 : sens du مصدر donné au مضارع
  - `18:01#6→c` « أنّ الرّحمةَ مستمرّةٌ في هذهِ اللّحظةِ » — sens du مضارع (« مستمرّة في هذه اللحظة ») donné au verbe de دعاء
  - `18:03#1→a` « نَجَحَ — يَنجَحُ » — R1 : pas de مصدر dans la paire
  - `18:03#1→c` « نَجاحٌ — يَنجَحُ » — R1 : مضارع pris pour l'achèvement
  - `18:03#1→d` « نَجاحٌ — إنْجاحٌ » — R1 : « إنجاح » (مصدر مزيد) pris pour un verbe / un fait qui a un temps — seul porteur du piège n°1
  - `18:03#2→a` « الصّيغةُ: الحدثُ منقضٍ؛ والسّياقُ: الزّمانُ الحاضرُ » — R1 : sens du passé donné au مضارع « يتدرّب »
- **Note** : Piège n°1 (« النجاحُ ماضٍ ») : le porteur littéral est 03#1→d ; le geste inverse (donner au verbe la propriété du مصدر) fournit les autres.

#### `arabe.zaman.zaman-min-al-sigha` — NEUF

- **AR** : تقرأُ زمانَ الفعلِ من صيغتِه وحدَها: الماضي يقولُ «انقضى» والمضارعُ «لم ينقضِ»، والزّمانُ يعيّنُه السّياقُ (أمسِ، الآنَ، غدًا)
- **FR** : Tu lis le temps du verbe dans sa seule forme : le passé dit « achevé », le مضارع « inachevé » ; le temps vient du contexte (أمسِ، الآنَ، غدًا)
- **EN** : You read a verb's time from its form alone: the past says "achieved", the مضارع "unfinished"; the time comes from context (أمسِ، الآنَ، غدًا)
- **Chapitres / piège** : ch18 — piège n°2 (§ صيغة الماضي) « الحكم على الزمان من الصيغة وحدها (« اشتريتُ » ماضٍ) » ; n°3 (§ المضارع المرفوع) « قراءة المضارع حاضرًا دائمًا » ; n°10 (§ أوظّف) « أن تبدأ بالصيغة دائمًا » [moitié couverte : P2 + P3 + P10 : un seul geste, lire le temps à la forme]
- **Q distinctes** : 3
- **Distracteurs porteurs** :
  - `18:01#1→b` « الزّمانُ الماضي أو الحاضرُ أو المستقبلُ » — R1 : « الزمان الماضي أو الحاضر أو المستقبل » attribué à la forme
  - `18:01#2→b` « سافرَ » — R1 : « سافر » censé fixer le temps
  - `18:01#2→d` « لا شيءَ: فصيغةُ الفعلِ وحدَها تكفي » — R1 : « فصيغة الفعل وحدها تكفي »
  - `18:03#2→b` « الصّيغةُ: الزّمانُ الحاضرُ؛ والسّياقُ: الحدثُ غيرُ منقضٍ » — R1 : « الصيغة : الزمان الحاضر »

## 3. Règles de précédence (quand deux ids se touchent)

- **Questions « nom + raison » (15:01#3, 15:05#2, 15:02#5)** — `rabt.ism-al-harf-min-shaklih` prime quand la raison donnée est VRAIE mais ne peut pas fonder le nom (« جمع بدون ترتيب » pour dire عطف) ; `rabt.waw-tartib` quand la raison est fausse en soi (الواو « ترتيب » ou « ترتيب وتراخٍ »). Nom faux ET raison fausse : muet.
- **Rang / fonction** — `rabt.rutba-bi-shakl-la-bil-unsur` dès que les options se partagent entre ابتدائيّة et استئنافيّة ; `rabt.i3tirad-wal-hal-khalt` dès qu'une option oppose l'اعتراضيّة à une fonction (حال، مفعول فيه، خبر).
- **Conséquence / permutation** — `rabt.natija-bi-ghayr-al-fa` quand la question demande « quel outil dit la conséquence ? » ; `rabt.fa-thumma-bila-tartib` quand elle demande « si on permute ou remplace, que devient le sens ? ».
- **بل** — `rabt.bal-bila-nazar-fil-ula` ne couvre que les trois sens إضراب / تقرير / تأكيد pris l'un pour l'autre ; بل ↔ استدراك (15:quiz#4→c) reste muet (< 3).
- **أمّا / إمّا** — `rabt.amma-bila-fa` (فاء absente) et `rabt.imma-amma-khalt` (mauvais outil) ne se cumulent jamais : l'option qui fait les deux (15:04#4→d) est muette.
- **Type / degré d'une phrase (jumla)** — une option fausse à la fois sur le type et sur le degré (15:04#3→c) est muette ; `jumla.naw3-bi-fi3l` ne vaut que si le TYPE est la seule erreur, `jumla.isnad-far3i-la-yura` que si le DEGRÉ l'est.
- **Nasb / noms de forme (nida)** — `nida.nasb-al-marfu3` quand l'option affirme un RÉGIME erroné (« ينصب ») ; `nida.shakl-nahwi-khalt` quand elle affirme un NOM de forme erroné (« نكرة موصوفة… ») ; les deux à la fois (04:04#3→d, 04:04#2→b) : muet.
- **Voyelle posée sur le مضاف** — damma ou kasra : `nida.mudaf-marfu3` ; tanwin : `nida.tanwin-al-munada`.
- **استغاثة / ندبة** — l'option qui change le NOM de l'acte (استغاثة ↔ ندبة ↔ نداء) : `nida.nudba-istighatha` ; celle qui garde l'acte mais redistribue les rôles ou les lam : `nida.mustaghath-wa-lah-khalt`.
- **Amr / nahy** — `talab.hukm-bi-natija` pour « quelle phrase est un نهي / un أمر ? » avec des distracteurs de même effet pratique ; `talab.sigha-amr-khalt` pour « quelle FORME ? ». Un « لا » + présent مرفوع pris pour نهي : `talab.kull-la-nahy` ; un « لا » + passé de دعاء jugé sur la forme : `talab.dua-min-shakl-al-jumla`.
- **Sens contextuel** — `talab.ma3na-bila-maqam` ne s'applique qu'aux questions de مقام (quel sens prend l'ordre ici ?) et à toutes leurs options fausses.
- **Istifham : catégorie avant détail** — `istifham.harf-ism-khalt` quand l'élève se trompe de CATÉGORIE (nom pour particule ou l'inverse) ; `istifham.ism-ghayr-munasib` quand il est dans la bonne catégorie (les noms) mais prend le mauvais nom.
- **Question mixte but + réponse (16:04#2)** — option juste en réponse mais fausse en but : `istifham.ghaya-min-al-shakl` ; juste en but mais réponse qui se contredit : `istifham.harf-jawab-yunaqid` ; juste en but, réponse cohérente mais pour l'état inverse (04#2→d) : muet.
- **Fonction** — sur un NOM interrogatif (ما، كيف، أين) : `istifham.wazifa-bila-jawab` ; sur un مركّب جرّ (حرف + اسم) : `istifham.markab-jarr-khabar-aw-mutammim` pour le couple verbe / sans verbe, `istifham.jarr-min-al-harf-wahdah` pour le sens tiré de la préposition. Une option étrangère aux deux (16:02#5→c « مفعول فيه ») reste muette.
- **Shart : deux sens miroirs** — `shart.lau-lil-mumkin` quand لو est employé pour un fait encore possible / futur ; `shart.imtina3-ghayr-maqru2` quand إنْ / إذا / متى sont employés pour un fait que l'on sait déjà manqué.
- **Lecture de لو** — `shart.lau-3ala-zahiriha` quand l'élève lit les événements d'une phrase en « لو » à l'endroit (affirmatif = advenu, négatif = non advenu) ; `shart.in-madi-ka-lau` quand c'est le passé après « إنْ » qui est lu comme non advenu (ou « les deux phrases se valent »).
- **Faits vs hypothèse** — `shart.wujub-shart-khalt` dès qu'un des deux termes de la confusion est un simple constat sans outil de condition ; `shart.imkan-istintaj-khalt` quand les deux options sont des conditionnelles (إمكان contre استنتاج).
- **مَن / ما** — `shart.man-ma-shart-daiman` pour la NATURE (condition ou relatif) ; `shart.wazifa-bila-ra2isi` pour la FONCTION du groupe ; `shart.ism-shart-ghayr-munasib` seulement pour le couple nom / sens (personne, chose, temps, lieu, manière).
- **Jazm** — `shart.mudari3-marfu3-ba3d-adat` quand le jazm manque là où il est dû ; `shart.jazm-fi-ghayr-mawdi3ih` quand il est posé là où il n'est pas dû (principal antéposé, après إذا). Une option qui cumule un nasb (02#1→d) reste muette.
- **Temps lu à la forme (ch.18)** — `zaman.zaman-min-al-sigha` dès que la phrase est ordinaire (أمس / الآن / غدًا) et que l'élève décide à la forme ; `zaman.sayaq-khass-bil-sigha` quand la phrase est un دعاء, une حكمة ou une règle scientifique (même si l'option fautive est « حاضر لأنّه مضارع » : 18:03#3→b).
- **Deux familles de « contextes particuliers »** — `zaman.sayaq-khass-bil-sigha` : le contexte est reconnu mais le verbe est mal daté ; `zaman.sayaq-khass-khalt` : on se trompe de contexte (دعاء pris pour حكمة, récit pris pour دعاء).
- **Particules de futur** — `zaman.ba3d-in-an-kay-waqi3` : l'événement est lu comme ADVENU ; `zaman.qad-sin-sawfa-khalt` : il est lu comme CERTAIN (ou سين = سوف). Même option, deux erreurs (18:05#3→a ne dit que « advenu ») : suivre le texte de l'option.
- **Négation** — `zaman.nafy-zaman-khalt` quand la question porte sur le TEMPS (لم، لمّا، لن) ; `zaman.nahiya-lan-khalt` quand elle oppose demander de s'abstenir (لا + مجزوم) et affirmer l'impossibilité (لن).
- **Sens des particules** — `zaman.harf-ma3na-khalt` est un repli : il ne s'emploie que si ni `qad-sin-sawfa-khalt`, ni `nafy-zaman-khalt`, ni `nahiya-lan-khalt`, ni `lau-halla-akhbar` ne s'appliquent. `zaman.sigha-ma3na-khalt` est l'équivalent pour les FORMES (مصدر / ماضٍ / مضارع / دعاء).

## 4. Pièges sans id

| chapitre | piège | raison |
| --- | --- | --- |
| 15 | n°8 (§ أو وإمّا وأم) « الجوابُ بـ«نعم» أو «لا» عن سؤالٍ فيه «أم» » | isolé : aucun distracteur ne met un « نعم / لا » en réponse à une question en « أم » (les 35 items sont des QCM sur le sens ; seul le `verifie` du cours le teste). |
| 15 | n°12 (§ أمّا وإذا وإذن وأي) « عدُّ كلِّ «إذا» فجئيّةً » | isolé : aucun distracteur ne prend un « إذا » conditionnel pour une فجئيّة (le seul item sur « فإذا », 03#4, ne porte pas ce sens ; l'erreur inverse y est testée). |
| 15 | n°14 (§ الحذف والجملة المختزلة) « إتمامُ «الصّدقَ الصّدقَ!» بتغييرِ ما نطقَه المتكلّمُ » | isolé : aucun item ne demande de compléter « الصّدقَ الصّدقَ » ; l'erreur n'existe que dans le cours. |
| 15 | n°15 (§ الحذف في الفعليّة والاسميّة) « تسميةُ المنجَزِ («البابَ: المفعولُ به») بدلَ المحذوفِ » | isolé : les items demandent « ما المحذوف ؟ » avec des options de la forme « الفعل والفاعل… », jamais « المفعول به » comme réponse-à-la-place-du-manquant ; erreur de forme d'exercice que le QCM ne peut pas reconstruire. |
| 04 | n°8 (§ أبنية الدّعاء) « تغيير حركة ما بقي عند الاختزال («نجاحٌ باهرٌ») » | isolé : aucun distracteur n'est un دعاء réduit remis au nominatif (« نجاحٌ باهرٌ ») ; presque-porteur : 04:04#4→b (« سعادتُكَ دائمةٌ », phrase nominale), mais l'erreur y est « phrase nominale », pas « voyelle changée ». |
| 04 | n°10 (§ صيغ الأمر) « حصر الأمر في فعل الأمر («صبرًا يا أهلَ الحيّ») » | isolé : aucun item ne demande « est-ce un أمر ? » d'un مصدر ou d'une expression ; les questions sur les formes (01#4, 05#4) demandent de reconnaître la forme, et leurs distracteurs sont les trois autres formes. |
| 16 | n°6 (§ الاستفهام وعدم اليقين) « ختم جملة عدم اليقين بعلامة استفهام » | isolé : aucun item ne propose de ponctuation ni de « ؟ » en fin de phrase d'incertitude (les options de 02#3 et 05#1 sont des phrases nues ou des composants) ; l'erreur n'existe que dans le cours. |

## 5. Erreurs vues < 3 fois (non retenues)

- **« المختزلة » mal définie (courte / incompréhensible / lettre ou voyelle supprimée)** — 15:quiz#5→a,b,c (R1 : l'explication nomme les trois) ; 15:01#6→a,b,d (phrases complètes prises pour des réponses réduites) — 1 seule question reconstructible (quiz#5) ; 01#6 n'a pas de chemin d'erreur net.
- **Oubli du فاعل / نائب الفاعل : on croit que le verbe est seul omis** — 15:05#6→b,c,d (R2) ; 15:02#6→d — 2 questions (05#6, 02#6). À reprendre si un autre chapitre de hadhf apparaît.
- **Verbe au passif traité comme actif (« الفعل والفاعل »)** — 15:02#6→a,c — 1 question.
- **ناسخ « كان » de la question ignoré : on lit « صعبًا » comme خبر/مبتدأ marfu3 ou comme complément** — 15:03#6→a,b,c (R1 : « ونصبُه دليلٌ… ») — 1 question (3 distracteurs) ; l'id hukm-min-mawqi3-al-baqi ne dit pas le nasb.
- **« إمّا » initial supprimé ou remplacé par « أو » / « ثمّ » au lieu de la répéter** — 15:04#5→b,c,d — 1 question (la `حالة حدّيّة` du cours, pas un piège).
- **Mauvais couple de composants autour de l'اعتراضيّة** — 15:03#5→a,c,d — 1 question ; erreur d'analyse, pas d'idée fausse.
- **بل confondu avec لكنّ (استدراك)** — 15:quiz#4→c — 1 question.
- **« فإذا » : on y lit la ف de cause + إذا** — 15:03#4→a (R1 : « والفاء هنا جزء من فإذا وليست فاء السبب ») — 1 question.
- **أم lue avec le sens de أو (شك / تخيير)** — 15:02#5→a (aussi name), 15:02#5→b — 1 question.
- **لام الأمر sans جزم : le présent reste marfu3 / mansub / kasra après « ليـ »** — 04:02#3→b,c,d (R2) — 1 question. (Proche de `arabe.tawjih.nahy-marfu3` mais celui-ci dit « لا » النّاهية.)
- **« الله + présent marfu3 » pris pour un دعاء (calque du dialecte : الله يحفظك)** — 04:quiz#3→d (R1) ; 04:05#6→d (R1) — 2 questions (3 avec 04:04#4→a, mais l'explication de celui-ci nomme « phrase complète » et non l'erreur de dialecte). À reprendre : la meilleure candidate du chapitre.
- **« لا » + verbe passé (لا بارك الله) lu comme un نهي** — 04:06#4→b,c (R1 : « الماضي بعده يجعلها نفيًا ») — 1 question.
- **« يا » + « ال » collés (يا المسافرُ)** — 04:04#2→a (b cumule avec le نصب) — 1 question ; la `propriete` du cours l'énonce (« فلا نقول يا الطالبُ ») sans piège.
- **Nombre de formes d'ordre compté sur les verbes (06#5)** — 04:06#5→a,b,d — 1 question.
- **Phrase d'appel prise pour une phrase verbale / nominale (فعل وفاعل، مبتدأ وخبر)** — 04:quiz#1→a,b — 1 question.
- **Le منادى réduit à son premier mot (« يا » + « بائع »)** — 04:01#3→b (R1 : « ركن واحد وإن كان كلمتين ») — 1 question ; couvert par le `verifie` du cours.
- **Dua pris pour un أمر ou pour un نداء** — 04:01#2→b,c ; 04:quiz#3→b,c — 2 questions, mais sans chemin d'erreur net.
- **Lecture de la liste des outils d'appel (qui est pour proche / lointain)** — 04:01#1→a,c,d — 1 question de pure mémoire.
- **« بلى » donné à une question positive (ou à une question en اسم استفهام)** — 16:01#2→b,c ; 16:03#3→a,b,d — 2 questions ; la `propriete` du cours l'énonce (« لا يصحّ أحضرتَ؟ — بلى ») sans piège.
- **La تسوية crue portée par la hamza ou par « أم » seules (et non par سيّان / سواء)** — 16:05#3→b ; 16:05#5→a,b — 2 questions (R1 pour les deux).
- **« وهل أ… » : cumul de « هل » et de la hamza** — 16:04#1→d (R1 : « الجمع بين هل والهمزة خطأ في الرتبة ») — 1 question ; autre geste que l'ordre du connecteur.
- **Marque d'إعراب de « أيّ » (damma / kasra / tanwin au lieu de la fatha de المفعول به)** — 16:04#4→a,b,c (R1) — 1 question.
- **Fonction du groupe entier après un verbe d'incertitude : « فاعل » au lieu de مفعول به** — 16:05#4→a (R1 : « ليس فاعلًا لأنّ فاعل أعرف هو أنا ») — 1 question.
- **Sens d'un مركّب جرّ pris d'après la préposition de la question (إلى / من / في)** — 16:03#5→a,b,c — 1 question.
- **Un مركّب جرّ jugé « non remplaçable » alors qu'il se remplace (متى، أين، كيف)** — 16:04#6→a,b,d (R2) — 1 question.
- **Le composant porteur de l'incertitude confondu avec le nom interrogatif (« أيّ ») ou le reste de la phrase** — 16:05#1→a,c,d — 1 question.
- **« أيّ » seul parmi les noms lié à l'annexion : on en prête l'obligation à مَن / كيف / كم** — 16:quiz#3→a,b,c — 1 question.
- **Place de la ف de liaison ou « ثمّ » mis à la place de la ف** — 17:05#2→c,d (R1) — 1 question.
- **Le مفعول الشرط réduit à l'événement sans le حرف, ou étendu au début du principal** — 17:03#1→a,b,d — 1 question ; le `verifie` du cours le travaille.
- **Type de la phrase principale lu depuis le verbe du شرط (« أضاء ») ou depuis la forme du شرط** — 17:03#3→a,c (+ b : ف prise pour l'amr) — 1 question. Proche de `arabe.jumla.naw3-bi-fi3l` (type par présence d'un verbe) mais le verbe est hors de la proposition analysée : non réutilisé.
- **Nom de condition qui ne tient pas la صدارة : « تُحسِنْ إلى مَنْ أُحسِنْ » ; ou relatif conservé en fin de transformation** — 17:05#3→a,b — 1 question.
- **Facteur qui fixe le temps de « إنْ » : le حرف lui-même, la forme du verbe, la place du principal** — 17:04#5→c,d (a est classé dans `imkan-istintaj-khalt`) — 1 question.
- **« إنْ تُراجِعَ » : nasb au lieu de jazm (confusion إنْ / أنْ)** — 17:02#1→d (R1) — 1 question.
- **Bascule du sens de « مَن » selon que le verbe suivant est marfu3 ou majzum (la différence est dite « pas de différence » ou « de temps »)** — 17:02#4→a,c,d — 1 question (le piège n°5 est porté par `man-ma-shart-daiman` ailleurs).
- **« أيّ » seul adapté au عاقل / غير عاقل ; mauvais nom de condition pour « أيّ »** — 17:03#2→b,c,d — 1 question de mémoire.
- **Rôles inversés dans une déduction (le conclu pris pour le donné)** — 17:05#5→a (classé sous `ra2isi-bi-tartib-al-dhikr` car l'ordre de mention est la cause lisible) — voir doutes.
- **Ce qui s'est perdu / ce que dit « لو » dans un couple لو … إنْ** — 17:05#6→a,d — 1 question.
- **Lecture du seul contexte, en oubliant ce que dit la forme (« يكتب التلميذ الدرس أمسِ » pris pour un fait achevé)** — 18:01#4→a (R1 : « في الماضي لكنّ الحدث غير منقضٍ ») — 1 question ; geste inverse de `zaman-min-al-sigha`.
- **Mots de temps lus sans la forme : au passé on propose « الآنَ », « غدًا », « بعد ساعة » (01#5→a,b,d)** — 18:01#5→a,b,d — 1 question ; aucun chemin d'erreur net (le présent n'est pas « lu au passé »).
- **Nafy, « إنْ + ماضٍ » ou question d'une phrase à la fois « achevée au passé » : options 01#4→c,d** — 18:01#4→c,d — 1 question.
- **Durée de الدعاء : le même verbe, deux contextes — options b/c/d de 04#2 sont classées sous `sayaq-khass-khalt`** — — — voir doutes.
- **Rôles inversés entre ce que dit la forme et ce que dit le contexte** — 18:03#2→a (classé A1), 18:03#6→a — 1–2 questions.

## 6. `coursePitfalls` proposés par chapitre

Colonne C-5 : ✓ = au moins un distracteur du chapitre porte l'id (cité au §2) ; ✗ = aucun.

### Chapitre 15 — `15-al-alaqat-bayna-al-jumal`

| id | C-5 (porté par un distracteur du chapitre ?) | piège du cours qui l'énonce | porteurs dans ce chapitre |
| --- | --- | --- | --- |
| `arabe.jumla.markaba-li-tul` | ✓ | n°1 (§ الجملة في النص) « الأطفالُ يلعبونَ في السّاحةِ: «فعليّةٌ، لأنّ فيها فعلًا» + عدّ الجملة الطويلة مركّبةً » | 15:01#1→b |
| `arabe.jumla.naw3-bi-fi3l` | ✓ | n°1 (§ الجملة في النص) « الأطفالُ يلعبونَ في السّاحةِ: «فعليّةٌ، لأنّ فيها فعلًا» + عدّ الجملة الطويلة مركّبةً » | 15:04#3→a |
| `arabe.rabt.rutba-bi-shakl-la-bil-unsur` | ✓ | n°2 (§ رتبة الجملة) « الحكمُ على الرّتبةِ بشكلِ الجملةِ: «ذلكَ الشّيخُ كريمٌ» ابتدائيّةٌ » | 15:quiz#1→a, 15:quiz#1→c, 15:01#2→a, 15:01#2→c, 15:01#2→d, 15:04#1→b, 15:04#1→c, 15:04#1→d |
| `arabe.rabt.i3tirad-wal-hal-khalt` | ✓ | n°3 (§ رتبة الجملة) « عدُّ كلِّ مقطعٍ بينَ فاصلتَينِ جملةً اعتراضيّةً (وقد فازَ = حالٌ) » | 15:quiz#2→a, 15:quiz#2→b, 15:02#1→a, 15:02#1→b, 15:02#1→d, 15:05#3→b |
| `arabe.rabt.ism-al-harf-min-shaklih` | ✓ | n°4 (§ حرف الاستئناف وحرف العطف) « تسميةُ الواوِ أو الفاءِ أو «ثمّ» حرفَ عطفٍ دائمًا » | 15:05#2→a, 15:05#2→c, 15:01#3→b, 15:02#5→d |
| `arabe.rabt.fa-wajh-wahid` | ✓ | n°5 (§ حروف الجمع) « قراءةُ الواوِ ترتيبًا لأنّ الأحداثَ تتتابعُ + كلُّ فاءٍ ترتيبُ أحداثٍ » | 15:01#5→b, 15:01#5→c |
| `arabe.rabt.waw-tartib` | ✓ | n°5 (§ حروف الجمع) « قراءةُ الواوِ ترتيبًا لأنّ الأحداثَ تتتابعُ + كلُّ فاءٍ ترتيبُ أحداثٍ » | 15:quiz#3→b, 15:quiz#3→c, 15:05#2→b, 15:01#3→d |
| `arabe.rabt.hatta-jam3-daiman` | ✓ | n°6 (§ حروف الجمع) « اختيارُ «ثمّ» لذكرِ النّتيجةِ + عدُّ كلِّ «حتّى» حرفَ جمعٍ » | 15:02#3→a, 15:02#3→c, 15:02#3→d |
| `arabe.rabt.natija-bi-ghayr-al-fa` | ✓ | n°6 (§ حروف الجمع) « اختيارُ «ثمّ» لذكرِ النّتيجةِ + عدُّ كلِّ «حتّى» حرفَ جمعٍ » | 15:05#4→a, 15:05#4→c, 15:05#4→d, 15:02#2→c |
| `arabe.rabt.aw-takhyir-daiman` | ✓ | n°7 (§ أو وإمّا وأم) « حملُ «أو» على التّخييرِ دائمًا » | 15:03#1→a |
| `arabe.rabt.bal-bila-nazar-fil-ula` | ✓ | n°9 (§ بل ولكن) « قراءةُ «بل» إضرابًا دائمًا » | 15:quiz#4→a, 15:quiz#4→b, 15:02#4→b, 15:02#4→c, 15:02#4→d |
| `arabe.rabt.istidrak-bi-ma-yuwafiq` | ✓ | n°10 (§ بل ولكن) « استعمالُ أداةِ الاستدراكِ حينَ تكونُ الثّانيةُ هي المتوقَّعَ » | 15:05#5→a, 15:05#5→b, 15:05#5→d |
| `arabe.rabt.amma-bila-fa` | ✓ | n°11 (§ أمّا وإذا وإذن وأي) « حذفُ الفاءِ بعدَ المبتدأِ في «أمّا» + الخلطُ بينَ «إمّا» و«أمّا» » | 15:04#4→c |
| `arabe.rabt.imma-amma-khalt` | ✓ | n°11 (§ أمّا وإذا وإذن وأي) « حذفُ الفاءِ بعدَ المبتدأِ في «أمّا» + الخلطُ بينَ «إمّا» و«أمّا» » | 15:04#4→a, 15:03#3→a |
| `arabe.rabt.kull-ay-tafsir` | ✓ | n°13 (§ أمّا وإذا وإذن وأي) « عدُّ كلِّ «أيْ» تفسيرًا » | 15:04#2→a, 15:04#2→b |
| `arabe.hadhf.hukm-min-mawqi3-al-baqi` | ✓ | n°16 (§ الحذف في الفعليّة والاسميّة) « افتراضُ أنّ الباقيَ في الجوابِ هو الخبرُ دائمًا » | 15:04#6→a |

### Chapitre 04 — `04-al-asalib`

| id | C-5 (porté par un distracteur du chapitre ?) | piège du cours qui l'énonce | porteurs dans ce chapitre |
| --- | --- | --- | --- |
| `arabe.nida.rukn-thalith` | ✓ | n°1 (§ النداء) « عدّ ما بعد المنادى ركنًا ثالثًا » | 04:quiz#1→d, 04:01#3→d |
| `arabe.nida.adat-bil-masafa` | ✓ | n°2 (§ أدوات النداء) « ربط الأداة بالمسافة الحسّيّة وحدها » | 04:05#1→c |
| `arabe.nida.tanwin-al-munada` | ✓ | n°3 (§ حكم المنادى: الرفع) « تنوين المنادى النكرة («يا ولدٌ») » | 04:02#2→b |
| `arabe.nida.mudaf-marfu3` | ✓ | n°4 (§ حكم المنادى: النصب) « ضمّ المضاف لأنّه علم («يا عبدُ اللهِ») » | 04:02#2→a, 04:02#2→c |
| `arabe.nida.mustaghath-wa-lah-khalt` | ✓ | n°5 (§ الاستغاثة) « عدّ المستغاث له هو المستغاث » | 04:01#6→a, 04:01#6→b, 04:01#6→d, 04:02#5→a, 04:02#5→c, 04:02#5→d, 04:06#3→a, 04:06#3→c, 04:06#3→d |
| `arabe.nida.nudba-istighatha` | ✓ | n°6 (§ النّدبة) « عدّ النّدبة استغاثة لأنّ صاحبها في شدّة » | 04:04#1→a, 04:04#1→b, 04:04#1→c, 04:05#3→a, 04:05#3→b, 04:05#3→d |
| `arabe.talab.dua-min-shakl-al-jumla` | ✓ | n°7 (§ الدّعاء) « الحكم على نوع الدّعاء من شكل الجملة لا من المطلوب » | 04:02#6→a, 04:02#6→d, 04:04#4→d, 04:06#4→d |
| `arabe.talab.hukm-bi-natija` | ✓ | n°9 (§ الأمر والنّهي) « الحكم على الجملة من نتيجتها العمليّة » | 04:01#5→a, 04:05#2→a, 04:05#2→d, 04:06#1→a, 04:06#1→b, 04:06#1→d |
| `arabe.talab.kull-la-nahy` | ✓ | n°11 (§ صيغة النّهي) « عدّ كلّ «لا» + مضارع نهيًا » | 04:04#5→d, 04:05#2→c |
| `arabe.talab.ma3na-bila-maqam` | ✓ | n°12 (§ معاني الأمر والنّهي) « الحكم على المعنى من الصيغة وحدها » | 04:quiz#5→a, 04:quiz#5→b, 04:quiz#5→d, 04:04#6→a, 04:04#6→b, 04:04#6→c, 04:05#5→a, 04:05#5→c, 04:05#5→d, 04:06#6→a, 04:06#6→b, 04:06#6→c |

### Chapitre 16 — `16-al-istifham`

| id | C-5 (porté par un distracteur du chapitre ?) | piège du cours qui l'énonce | porteurs dans ce chapitre |
| --- | --- | --- | --- |
| `arabe.istifham.rutba-al-harf` | ✓ | n°1 (§ حرفا الاستفهام) « تقديم حرف الاستئناف على الهمزة أو تأخيره عن «هل» (وَأَتَقْبَلُ، هَلْ وَتَقْبَلُ) » | 16:04#1→a, 16:04#1→b |
| `arabe.istifham.ghaya-min-al-shakl` | ✓ | n°2 (§ المثبتة والمنفيّة) « الحكم على غاية السائل من علامة الاستفهام وحدها » | 16:01#4→a, 16:01#4→b, 16:03#2→a, 16:04#2→b |
| `arabe.istifham.harf-jawab-yunaqid` | ✓ | n°3 (§ الجواب: نعم وبلى) « الجواب بـ«نعم، قرأتُها» عن سؤال منفيّ » | 16:quiz#2→b, 16:quiz#2→c, 16:quiz#2→d, 16:02#1→b, 16:02#1→d, 16:04#2→c |
| `arabe.istifham.ism-ghayr-munasib` | ✓ | n°4 (§ أسماء الاستفهام) « السؤال عن شخص بـ«ما» » | 16:01#5→a, 16:01#5→c, 16:01#5→d, 16:01#3→b, 16:01#3→c, 16:01#3→d, 16:05#2→a, 16:05#2→b, 16:05#2→c, 16:05#6→a, 16:05#6→c, 16:05#6→d |
| `arabe.istifham.wazifa-bila-jawab` | ✓ | n°5 (§ وظيفة اسم الاستفهام) « الحكم على الوظيفة من الترتيب («ما» مبتدأ لأنّها أوّل الجملة) » | 16:quiz#4→a, 16:quiz#4→c, 16:quiz#4→d, 16:02#2→a, 16:02#2→b, 16:02#2→d, 16:01#6→a, 16:01#6→b, 16:01#6→c, 16:03#4→b, 16:03#4→c, 16:03#4→d, 16:04#3→a, 16:04#3→c, 16:04#3→d |
| `arabe.istifham.hal-makan-al-hamza` | ✓ | n°7 (§ الاستفهام والتسوية) « استعمال «هل» مكان الهمزة في التسوية » | 16:02#4→a |
| `arabe.istifham.jarr-min-al-harf-wahdah` | ✓ | n°8 (§ اسم الاستفهام المقترن بحرف الجرّ) « قراءة المعنى من حرف الجرّ وحده » | 16:02#5→b, 16:04#5→b |
| `arabe.istifham.markab-jarr-khabar-aw-mutammim` | ✓ | n°9 (§ مركّب الجرّ خبرًا مقدّمًا) « عدّ الاسم بعد مركّب الجرّ فاعلًا («مِنْ أَيِّ مَدِينَةٍ أَنْتَ؟») » | 16:quiz#5→a, 16:quiz#5→b, 16:quiz#5→d, 16:02#5→d, 16:02#6→a, 16:02#6→b, 16:02#6→d, 16:03#6→a, 16:03#6→c, 16:03#6→d |

### Chapitre 17 — `17-ash-shart`

| id | C-5 (porté par un distracteur du chapitre ?) | piège du cours qui l'énonce | porteurs dans ce chapitre |
| --- | --- | --- | --- |
| `arabe.shart.ra2isi-bi-tartib-al-dhikr` | ✓ | n°1 (§ ما الشرط ؟) « الحكم على الحدثين بترتيب ذكرهما (الرئيسيّ هو الأوّل) » | 17:05#5→a, 17:05#4→b |
| `arabe.shart.jazm-fi-ghayr-mawdi3ih` | ✓ | n°2 (§ حرف الشرط «إنْ») « ترك المضارع مرفوعًا بعد «إنْ» + جزم الرئيسيّ المتقدّم » | 17:02#1→c, 17:03#5→a |
| `arabe.shart.mudari3-marfu3-ba3d-adat` | ✓ | n°2 (§ حرف الشرط «إنْ») « ترك المضارع مرفوعًا بعد «إنْ» + جزم الرئيسيّ المتقدّم » | 17:02#1→b, 17:03#5→b, 17:03#5→c, 17:05#3→d |
| `arabe.shart.lau-lil-mumkin` | ✓ | n°3 (§ حرف الشرط «لو») « استعمال «لو» في حدث ما يزال ممكنًا (لو جاء الأستاذ غدًا) » | 17:05#6→a, 17:02#2→a, 17:02#2→b, 17:02#2→c, 17:04#1→a |
| `arabe.shart.fa-al-rabt-mahdhufa` | ✓ | n°4 (§ فاء الربط) « ترك الفاء لأنّ المعنى مفهوم (إنْ تعبتَ ارتحْ) » | 17:05#2→b |
| `arabe.shart.man-ma-shart-daiman` | ✓ | n°5 (§ اسم شرط أم اسم موصول ؟) « عدّ كلّ «مَنْ» و«ما» في أوّل الكلام اسمَي شرط » | 17:quiz#4→a, 17:quiz#4→b, 17:quiz#4→d, 17:01#5→a, 17:01#5→b, 17:01#5→d, 17:04#2→b, 17:04#2→c, 17:04#2→d |
| `arabe.shart.ism-shart-ghayr-munasib` | ✓ | n°6 (§ أسماء الشرط العشرة) « اختيار الاسم بحسب الكلمة الأقرب لا المعنى (ما يتأخّر، متى/أينما) » | 17:05#1→a, 17:05#1→c, 17:05#1→d, 17:02#6→c |
| `arabe.shart.wazifa-bila-ra2isi` | ✓ | n°7 (§ وظيفة اسم الشرط) « عدّ المركّب الموصوليّ مبتدأً لمجرّد أنّه في أوّل الجملة » | 17:01#6→a, 17:01#6→c, 17:01#6→d, 17:02#5→a, 17:02#5→b, 17:02#5→d, 17:02#6→a, 17:02#6→b, 17:04#3→a, 17:04#3→c, 17:04#3→d |
| `arabe.shart.in-madi-ka-lau` | ✓ | n°8 (§ افتراض الممكن) « عدّ الماضي بعد «إنْ» دليلًا على أنّ الحدث لم يقع كما في «لو» » | 17:04#1→c, 17:05#6→b |
| `arabe.shart.lau-3ala-zahiriha` | ✓ | n°9 (§ افتراض الممتنع) « قراءة الماضي بعد «لو» على أنّه حدث وقع » | 17:01#2→a, 17:01#2→b, 17:01#2→d, 17:02#3→b, 17:02#3→c, 17:02#3→d, 17:04#4→a, 17:04#4→b, 17:04#4→d, 17:05#4→a, 17:05#4→c |
| `arabe.shart.imkan-istintaj-khalt` | ✓ | n°10 (§ الاستنتاج) « الخلط بين الافتراض والاستنتاج لأنّ الحرف واحد » ; n°11 (§ أوظّف) « الحكم على المعنى من الأداة وحدها » | 17:quiz#5→b, 17:04#6→b, 17:04#6→c, 17:05#6→d, 17:05#5→d, 17:04#5→a |

### Chapitre 18 — `18-dalalat-az-zaman`

| id | C-5 (porté par un distracteur du chapitre ?) | piège du cours qui l'énonce | porteurs dans ce chapitre |
| --- | --- | --- | --- |
| `arabe.zaman.sigha-ma3na-khalt` | ✓ | n°1 (§ المصدر والفعل) « عدّ المصدر دالًّا على زمان («النجاحُ» ماضٍ) » | 18:quiz#1→a, 18:quiz#1→b, 18:quiz#1→d, 18:quiz#2→a, 18:quiz#2→c, 18:quiz#2→d, 18:01#1→c, 18:01#1→d, 18:01#3→a, 18:01#3→b, 18:01#3→c, 18:01#6→c, 18:03#1→a, 18:03#1→c, 18:03#1→d, 18:03#2→a |
| `arabe.zaman.zaman-min-al-sigha` | ✓ | n°2 (§ صيغة الماضي) « الحكم على الزمان من الصيغة وحدها (« اشتريتُ » ماضٍ) » ; n°3 (§ المضارع المرفوع) « قراءة المضارع حاضرًا دائمًا » ; n°10 (§ أوظّف) « أن تبدأ بالصيغة دائمًا » | 18:01#1→b, 18:01#2→b, 18:01#2→d, 18:03#2→b |
| `arabe.zaman.sayaq-khass-bil-sigha` | ✓ | n°4 (§ الدعاء والحكمة والقاعدة العلمية) « قراءة الفعل من صيغته دون سياقه الخاص » | 18:01#6→a, 18:03#3→b, 18:03#3→c, 18:03#3→d, 18:04#3→d, 18:05#6→a |
| `arabe.zaman.lau-halla-akhbar` | ✓ | n°5 (§ الحروف المقترنة بالفعل) « قراءة الفعل بصيغته وإهمال الحرف المقترن (لم يحضر، لو تكرّمتَ فأغلقتَ) » ; n°6 (§ لو وهلّا ولام الأمر ولا الناهية) « قراءة « لو » و« هلّا » مع الماضي خبرًا عن حدث مضى » | 18:02#3→a, 18:02#3→d, 18:04#3→c |
| `arabe.zaman.nafy-zaman-khalt` | ✓ | n°5 (§ الحروف المقترنة بالفعل) « قراءة الفعل بصيغته وإهمال الحرف المقترن (لم يحضر، لو تكرّمتَ فأغلقتَ) » ; n°8 (§ لم ولمّا ولن) « الحكم على زمان المنفيّ من صيغته والتسوية بين لم ولمّا » | 18:02#5→a, 18:02#5→b, 18:02#5→c, 18:03#5→a, 18:03#5→d, 18:04#4→b, 18:04#6→d, 18:05#1→b, 18:05#5→b, 18:05#6→b |
| `arabe.zaman.qad-sin-sawfa-khalt` | ✓ | n°7 (§ السين وسوف وقد) « التسوية بين « قد » والسين في اليقين وبين السين وسوف في المدى » | 18:quiz#4→a, 18:02#4→b, 18:02#4→c, 18:04#6→a, 18:05#6→c, 18:03#6→c, 18:05#2→b, 18:05#3→d, 18:02#6→c |
| `arabe.zaman.ba3d-in-an-kay-waqi3` | ✓ | n°9 (§ إن وأن وكي وحتّى ولام التعليل) « عدّ الحدث بعد هذه الحروف واقعًا » | 18:quiz#5→a, 18:quiz#5→d, 18:02#6→b, 18:03#6→b, 18:04#3→a, 18:05#2→a, 18:05#3→a, 18:05#4→a |

## 7. Couverture et doutes

