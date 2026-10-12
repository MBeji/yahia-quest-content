# Carte d'usage — vocabulaire d'erreurs de l'arabe 9ᵉ, PARTIE B (11 chapitres)

> Statut : chapitres traités : 01, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14. Généré par script à partir d'un jeu de données unique ; chaque distracteur cité est relu dans le corpus (extrait du JSON). Aucun fichier de `content/` n'est modifié.

Livrable jumeau : `vocab-arabe9-B.json` (ids NEUFS seulement).

## 0. Conventions

- Référence d'un distracteur : `CC:F#N→o` = chapitre `CC`, fichier `F` (`quiz` ou le préfixe numérique du fichier de `exercices/`), question `N` (rang 1-based dans le fichier, = `qN` du compilateur), option `o`. Toutes les questions sont `mcq`, aucune option n'était taguée.
- « Q » = nombre de questions DISTINCTES (tous chapitres B confondus) qui ont au moins un distracteur porteur. Un distracteur n'est cité que pour UN id (le script refuse un doublon).
- Notes entre « » après un distracteur : extrait littéral de l'explication ou des options, vérifié par script (voyelles ignorées) ; « R1 (paraphrase de l'explication) » = l'explication dit cela mais sans citation littérale ; sans note = R2/R3 (jeu de distracteurs construit sur l'erreur, ou calcul juste avec un geste inversé). Tous les distracteurs porteurs sont listés (pas seulement 2 à 5 exemples) pour permettre l'application mécanique.
- Réutilisation : « registre » = id déjà dans `content/misconceptions.json` ; « A » = id de `vocab-arabe9-A.json`.

## 1. Synthèse des ids

**119 ids neufs, 15 ids réutilisés** (parmi les ids effectivement utilisés).

Couverture : 862 distracteurs taguables sur 1149 (75 %), répartis sur 337 questions sur 383 ; 72 pièges sur 77 ont au moins un id porté par un distracteur du chapitre (les autres : voir § 4).

| id | statut | chapitres | Q | `piege` |
| --- | --- | --- | --- | --- |
| `arabe.badi3.did-ma3ruf-ghayr-madhkur` | neuf | 08 | 1 | 08: n°1 |
| `arabe.badi3.fasila-khalt` | neuf | 08 | 4 | — |
| `arabe.badi3.harf-akhir-aw-haraka-khalt` | neuf | 08 | 3 | — |
| `arabe.badi3.maqama-bi-saj3-faqat` | neuf | 08 | 2 | 08: n°4 |
| `arabe.badi3.saj3-bi-tashabuh-al-bina2` | neuf | 08 | 4 | — |
| `arabe.badi3.saj3-mutakallaf-3ala-hisab-al-ma3na` | neuf | 08 | 4 | 08: n°3 |
| `arabe.badi3.saj3-yatlub-kalimatayn-mutashabihatayn` | neuf | 08 | 5 | 08: n°2 |
| `arabe.badi3.takrir-saj3-fi-kull-jumla` | neuf | 08 | 3 | 08: n°5 |
| `arabe.badi3.tibaq-saj3-khalt` | neuf | 08 | 7 | — |
| `arabe.badi3.tibaq-saj3-yajtami3an` | neuf | 08 | 3 | — |
| `arabe.fahm.jawab-min-kharij-al-nass` | neuf | 11 | 4 | 11: n°1 |
| `arabe.fahm.tafsil-ka-fikra-amma` | neuf | 11 | 3 | — |
| `arabe.fi3l.hukm-bil-haraka` | réutilisé (registre) | 01 | 3 | — |
| `arabe.hijaj.aqwal-bila-jumal-sardiyya` | neuf | 09 | 1 | 09: n°11 |
| `arabe.hijaj.arkan-khalt` | neuf | 09, 10, 11 | 24 | — |
| `arabe.hijaj.awwal-ra2y-muthbat` | neuf | 09 | 2 | 09: n°2; 09: n°6 |
| `arabe.hijaj.da3ima-dahida-khalt` | neuf | 10 | 4 | — |
| `arabe.hijaj.dahd-bila-dalil` | neuf | 09 | 1 | 09: n°13 |
| `arabe.hijaj.faqra-muqatta3a` | neuf | 09 | 1 | 09: n°14 |
| `arabe.hijaj.hadhf-al-fatiha-wal-khatm` | neuf | 09 | 1 | 09: n°14 |
| `arabe.hijaj.haqiqa-ka-qadiyya` | neuf | 09 | 1 | 09: n°1 |
| `arabe.hijaj.hukm-ra2yi-la-hijaji` | neuf | 10 | 3 | 10: n°8 |
| `arabe.hijaj.i3adat-al-utruha-hujja` | neuf | 09, 10 | 3 | 09: n°3; 10: n°3 |
| `arabe.hijaj.iqna3-ta2thir-khalt` | neuf | 09, 10 | 4 | 09: n°7; 10: n°7 |
| `arabe.hijaj.istidrak-khalt` | neuf | 09, 10 | 3 | 09: n°9; 10: n°5 |
| `arabe.hijaj.istifham-hijaji-khalt` | neuf | 09 | 1 | 09: n°10 |
| `arabe.hijaj.istintaj-dakhil-al-sayrura` | neuf | 09, 10 | 2 | 09: n°6; 10: n°1 |
| `arabe.hijaj.jumla-ula-hiya-al-utruha` | neuf | 10 | 1 | 10: n°1 |
| `arabe.hijaj.khatima-sardiyya-mansiyya` | neuf | 09 | 1 | 09: n°12 |
| `arabe.hijaj.khutta-la-tuwafiq-al-matlub` | neuf | 09 | 4 | — |
| `arabe.hijaj.ma3ayir-taqyim-khati2a` | neuf | 10 | 3 | — |
| `arabe.hijaj.mahdhuda-bi-lisan-al-katib` | neuf | 10 | 4 | 10: n°2 |
| `arabe.hijaj.mahdhuda-bila-badila` | neuf | 09 | 1 | 09: n°13 |
| `arabe.hijaj.mahdhuda-muthbata-khalt` | neuf | 09, 10 | 5 | — |
| `arabe.hijaj.mithal-hujja-kafiya` | neuf | 09, 10, 11 | 8 | 09: n°3; 10: n°3 |
| `arabe.hijaj.mu2ashshir-ghayr-munasib` | neuf | 09, 10, 11 | 13 | — |
| `arabe.hijaj.naw3-al-hujja-khalt` | neuf | 09, 10 | 11 | — |
| `arabe.hijaj.shahid-naw3-mustaqill` | neuf | 09 | 1 | 09: n°4 |
| `arabe.hijaj.sigha-ghayr-amina` | neuf | 10 | 5 | 10: n°2 |
| `arabe.hijaj.ta3lil-tafsir-khalt` | neuf | 09, 10 | 4 | 09: n°8; 10: n°5 |
| `arabe.hijaj.tadarruj-wa-rawabit-khalt` | neuf | 09 | 1 | 09: n°5 |
| `arabe.hijaj.taqsim-al-binya-khalt` | neuf | 10 | 4 | — |
| `arabe.hijaj.tarikhi-waqi3i-khalt` | neuf | 09, 10 | 10 | 09: n°4; 10: n°4 |
| `arabe.hijaj.utruha-ism-aw-su2al` | neuf | 09, 10, 11 | 5 | 09: n°2 |
| `arabe.hijaj.wazifa-min-al-mawdu3` | neuf | 10 | 3 | 10: n°7 |
| `arabe.i3rab.af3al-khamsa-3alama` | neuf | 01 | 3 | — |
| `arabe.i3rab.haraka-bada-harf` | réutilisé (registre) | 01 | 7 | 01: n°3 |
| `arabe.i3rab.harf-ghayr-munasib` | neuf | 01 | 7 | — |
| `arabe.i3rab.jam3-mu2annath-nasb` | réutilisé (registre) | 01, 11 | 2 | 11: n°2 |
| `arabe.i3rab.jarr-jazm-khalt` | neuf | 01 | 2 | 01: n°2 |
| `arabe.i3rab.mabni-mu3rab-khalt` | neuf | 01 | 8 | — |
| `arabe.i3rab.mamnu3-sabab-khalt` | neuf | 01 | 4 | — |
| `arabe.i3rab.mu3tall-3alama-zahira` | neuf | 01 | 3 | — |
| `arabe.intaj.khatima-mawdu3-jadid` | neuf | 11 | 1 | 11: n°3 |
| `arabe.ishtiqaq.af3al-tafdil-wa-lawn-khalt` | neuf | 06 | 2 | 06: n°5 |
| `arabe.ishtiqaq.fa3il-maf3ul-ma3na` | réutilisé (registre) | 05, 06, 11, 12 | 13 | 05: n°11; 12: n°5 |
| `arabe.ishtiqaq.fa3il-mubalagha-khalt` | neuf | 06, 11 | 6 | — |
| `arabe.ishtiqaq.fa3il-mubalagha-wa-sifa` | neuf | 06 | 1 | 06: n°3 |
| `arabe.ishtiqaq.makan-ka-fa3il-aw-maf3ul` | neuf | 06, 12 | 7 | — |
| `arabe.ishtiqaq.masdar-bada-al-mushtaqq` | réutilisé (registre) | 05, 12 | 4 | — |
| `arabe.ishtiqaq.mazid-haraka-al-3ayn` | réutilisé (registre) | 06 | 7 | 06: n°2 |
| `arabe.ishtiqaq.mim-ala-maftuha` | neuf | 06 | 2 | 06: n°7 |
| `arabe.ishtiqaq.min-fi3l-akhar` | réutilisé (registre) | 05 | 1 | — |
| `arabe.ishtiqaq.sifa-mushabbaha-khalt` | neuf | 06 | 13 | — |
| `arabe.ishtiqaq.wazn-ala-khalt` | neuf | 06 | 4 | — |
| `arabe.ishtiqaq.wazn-fa3il-lil-mazid` | réutilisé (registre) | 06 | 1 | 06: n°1 |
| `arabe.jidhr.alif-ka-harf-asli` | neuf | 12 | 3 | 12: n°6 |
| `arabe.jidhr.harf-zaid-fil-jidhr` | neuf | 12 | 3 | — |
| `arabe.jidhr.ya-min-al-fi3l-al-mazid` | neuf | 12 | 2 | 12: n°6 |
| `arabe.lugha.ma3na-mashhur-bila-siyaq` | neuf | 10 | 5 | 10: n°6 |
| `arabe.mamdud.hamza-ila-ya-bila-asl` | neuf | 12 | 3 | — |
| `arabe.mamdud.hamza-ta2nith-tubqa` | neuf | 12 | 2 | 12: n°4 |
| `arabe.mamdud.nawa3-al-hamza-khalt` | neuf | 12, 14 | 5 | — |
| `arabe.mamdud.qalb-kull-hamza-waw` | neuf | 12 | 1 | 12: n°4 |
| `arabe.manqus.hadhf-ya-ta3mim` | neuf | 12 | 2 | 12: n°3 |
| `arabe.manqus.maqsur-bi-hadhf-ya` | neuf | 12 | 1 | 12: n°7 |
| `arabe.maqsur.al-wa-tanwin` | réutilisé (registre) | 12 | 2 | — |
| `arabe.maqsur.hamza-fi-muthanna-wal-jam3` | neuf | 12 | 5 | — |
| `arabe.maqsur.muthanna` | réutilisé (registre) | 12 | 2 | — |
| `arabe.maqsur.muthanna-thulathi-ya-daiman` | neuf | 12 | 1 | 12: n°2 |
| `arabe.maqsur.muthanna-waw-ghayr-al-asl` | neuf | 12 | 3 | — |
| `arabe.maqsur.nakira-bila-tanwin` | réutilisé (registre) | 12 | 1 | 12: n°1 |
| `arabe.masdar.wazn-fi3l-akhar` | réutilisé (registre) | 05 | 1 | — |
| `arabe.mazid.af3ala-ja3liyya-daiman` | neuf | 05 | 2 | 05: n°2 |
| `arabe.mazid.fa33ala-takthir-aw-ja3liyya` | neuf | 05 | 2 | 05: n°3 |
| `arabe.mazid.if3alla-if3aalla-khalt` | neuf | 05 | 2 | 05: n°9 |
| `arabe.mazid.istaf3ala-talab-daiman` | neuf | 05 | 3 | 05: n°10 |
| `arabe.mazid.ma3na-bila-nazar-fil-jidhr` | neuf | 05 | 16 | — |
| `arabe.mazid.min-nafs-al-jidhr-dun-ma3na` | neuf | 05 | 4 | — |
| `arabe.mazid.mutawa3a-bila-fi3l-sabiq` | neuf | 05 | 7 | 05: n°4; 05: n°5; 05: n°8 |
| `arabe.mazid.mutawa3a-ittikhadh-khalt` | neuf | 05 | 1 | 05: n°7 |
| `arabe.mazid.tad3if-laysa-ziyada` | neuf | 05 | 2 | 05: n°1 |
| `arabe.mazid.tafa3ala-musharaka-daiman` | neuf | 05 | 3 | 05: n°6 |
| `arabe.mazid.wazn-ma3na-wahid` | neuf | 05 | 4 | 05: n°12 |
| `arabe.mazid.wazn-qarib-khalt` | neuf | 05 | 4 | — |
| `arabe.nawasikh.ism-khabar-maqlub` | réutilisé (registre) | 11 | 2 | — |
| `arabe.nawasikh.mubtada-ba3d-nasikh` | réutilisé (registre) | 11 | 1 | — |
| `arabe.nisba.fa3ila-fath-ma-qabl` | neuf | 14 | 2 | 14: n°2 |
| `arabe.nisba.idafa-bada-al-na3t` | neuf | 14 | 4 | — |
| `arabe.nisba.kull-iyya-masdar-sina3i` | neuf | 14 | 2 | 14: n°3 |
| `arabe.nisba.mahdhuf-la-yustaradd` | neuf | 14 | 3 | 14: n°1 |
| `arabe.nisba.mamdud-wa-mahdhuf-khalt` | neuf | 14 | 5 | — |
| `arabe.nisba.masdar-sina3i-nisba-khalt` | neuf | 14 | 6 | — |
| `arabe.nisba.min-kalima-ukhra` | neuf | 14 | 3 | — |
| `arabe.nisba.mutabaqa-na3t` | neuf | 14 | 7 | — |
| `arabe.nisba.radd-waw-bila-mahdhuf` | neuf | 14 | 4 | — |
| `arabe.nisba.ta2-tubqa` | neuf | 14 | 7 | 14: n°1 |
| `arabe.nisba.tasghir-khalt` | neuf | 14 | 6 | — |
| `arabe.nisba.ya-bi-surat-al-khatt` | neuf | 14 | 2 | 14: n°4 |
| `arabe.sard.a3mal-at-tahawwul` | réutilisé (registre) | 09 | 1 | — |
| `arabe.sinf.akhir-khalt` | neuf | 12 | 5 | — |
| `arabe.sinf.mabni-ka-mu3rab` | neuf | 12 | 3 | — |
| `arabe.sura.athar-al-sura-khalt` | neuf | 07 | 3 | — |
| `arabe.sura.isti3ara-li-ghiyab-al-ada` | neuf | 07 | 6 | 07: n°3 |
| `arabe.sura.ma3na-asli-badal-tahlil` | neuf | 07 | 1 | 07: n°4 |
| `arabe.sura.majaz-bi-makan-al-kalima` | neuf | 07 | 2 | 07: n°1 |
| `arabe.sura.majaz-ka-haqiqa` | neuf | 07, 11 | 6 | — |
| `arabe.sura.qalb-al-tarafayn` | neuf | 07 | 8 | 07: n°2 |
| `arabe.sura.rukn-baqi-khalt` | neuf | 07 | 7 | — |
| `arabe.sura.rukn-ghayr-munasib` | neuf | 07 | 9 | — |
| `arabe.sura.sura-hujja-tuthbit` | neuf | 07, 08 | 10 | 07: n°5 |
| `arabe.sura.tashbih-isti3ara-khalt` | neuf | 07 | 7 | — |
| `arabe.tasghir.alif-hukm-khalt` | neuf | 13 | 3 | — |
| `arabe.tasghir.asl-al-musaghghar-khalt` | neuf | 13 | 5 | — |
| `arabe.tasghir.harf-asli-yasqut` | neuf | 13 | 4 | 13: n°4 |
| `arabe.tasghir.kull-musaghghar-sighar` | neuf | 13 | 5 | 13: n°6 |
| `arabe.tasghir.ma3na-bi-ghayr-qarina` | neuf | 13 | 9 | 13: n°7 |
| `arabe.tasghir.mushaddad-harf-wahid` | neuf | 13 | 2 | 13: n°3 |
| `arabe.tasghir.sighat-al-tasghir-khalt` | neuf | 13 | 6 | — |
| `arabe.tasghir.ta2nith-fil-3add` | neuf | 13 | 3 | 13: n°2 |
| `arabe.tasghir.ta2nith-tuhdhaf-aw-tuzad` | neuf | 13 | 5 | — |
| `arabe.tasghir.tariq-ta3bir-khalt` | neuf | 13 | 4 | — |
| `arabe.tasghir.wazn-bi-ghayr-al-3adad` | neuf | 13 | 7 | 13: n°1 |
| `arabe.tasghir.ya-ba3d-al-thani-ta3rif` | neuf | 13 | 1 | 13: n°5 |

## 2. Fiches par id

### Domaine `badi3`

#### `arabe.badi3.did-ma3ruf-ghayr-madhkur` — NEUF

- **AR** : تعدُّ كلمةً طباقًا لأنّ ضدَّها معروفٌ ولو لم يُذكرْ (الصّدقُ منجاةٌ ← الكذبُ): الطّباقُ جمعٌ للمعنيَين المتقابلَين في الكلامِ الواحدِ
- **FR** : Tu comptes un tibāq parce que le contraire est connu, même absent (الصّدقُ منجاةٌ ← الكذبُ) : le tibāq réunit les deux sens opposés dans la même phrase
- **EN** : You count a word in a tibaq because its opposite is well known even if absent (الصّدقُ منجاةٌ ← الكذبُ): tibaq puts both opposite meanings in the same sentence
- **Chapitres / piège** : ch08 — piège n°1 « عدُّ كلمةٍ طباقًا لأنّ ضدَّها معروفٌ ولو لم يُذكرْ. قال تلميذٌ عن «الصّدقُ منجاةٌ»: «فيها طباقٌ، فضدُّ الصّدقِ… »
- **Q distinctes** : 1
- **Distracteurs porteurs** :
  - `08:02#2→a` « صوابٌ، لأنّ الطّباقَ يكفي فيه أن يكونَ لأحدِ المعنيَين ضدٌّ معروفٌ في … » — R1 : « فلا بدّ من ذكرهما معًا »

#### `arabe.badi3.fasila-khalt` — NEUF

- **AR** : تخطئُ في تحديدِ الفاصلةِ (أوّلُ الجملةِ أو فعلُها أو عبارةٌ): الفاصلةُ آخرُ كلمةٍ في الجملةِ، منها تبدأُ مقارنةُ الحرفِ الأخيرِ
- **FR** : Tu te trompes sur la fāṣila (début de phrase, verbe, groupe) : c'est le dernier mot de la phrase, d'où part la comparaison de la dernière lettre
- **EN** : You misidentify the fasila (start of the clause, its verb, a phrase): it is the clause's last word, where the comparison of the final letter starts
- **Chapitres / piège** : ch08 — (pas de piège ; erreur récurrente dans les items)
- **Q distinctes** : 4
- **Distracteurs porteurs** :
  - `08:01#1→a` « «العلمُ» و«العملُ» » — R1 (paraphrase de l'explication) :  الفاصلة آخر كلمة في كل جملة 
  - `08:01#1→c` « «يُنيرُ» و«يبني» » — R1 (paraphrase de l'explication) :  الفاصلة آخر كلمة في كل جملة 
  - `08:01#1→d` « «يُنيرُ العقلَ» و«يبني الأملَ» » — R1 (paraphrase de l'explication) :  الفاصلة آخر كلمة في كل جملة 
  - `08:04#1→d` « أن تقارنَ أوّلَ كلمةٍ في كلٍّ منهما بأوّلِ كلمةٍ في الأخرى »
  - `08:04#2→d` « لا سجعَ فيها، لأنّ الجملَ الثّلاثَ تبدأُ بأفعالِ أمرٍ مختلفةٍ » — R1 : « بدء الجمل بأفعال أمر مختلفة لا يمنع السجع لأنّه يُنظر إلى الأواخر »
  - `08:06#5→a` « فيه سجعٌ واحدٌ يجمعُ المقطعَ كلَّه، لأنّ فواصلَ الجملِ الخمسَ تنتهي كل… » — R1
  - `08:06#5→c` « لا سجعَ فيه، لأنّ الجملَ تتفاوتُ في طولِها وفي عددِ كلماتِها تفاوتًا ظ… » — R1
  - `08:06#5→d` « فيه سجعٌ بين الجملتَين الأخيرتَين فقط، لأنّ «نَزَلْتَ» و«وَافَيْتَ» تش… » — R1

#### `arabe.badi3.harf-akhir-aw-haraka-khalt` — NEUF

- **AR** : تخلطُ بين الحرفِ الأخيرِ وحركتِه أو ما قبلَه (أحدٌ/الصّمدُ، السّلامَ/الطّعامَ): السّجعُ في الحرفِ الأخيرِ ولا عبرةَ بالحركةِ ولا بالتّنوينِ
- **FR** : Tu confonds la dernière lettre avec sa voyelle ou la lettre d'avant (أحدٌ/الصّمدُ، السّلامَ/الطّعامَ) : le saj' ne regarde que la dernière lettre, hors voyelle
- **EN** : You confuse the final letter with its vowel or the letter before (أحدٌ/الصّمدُ، السّلامَ/الطّعامَ): saj' concerns the last letter; vowel and tanwin don't count
- **Chapitres / piège** : ch08 — (pas de piège ; erreur récurrente dans les items)
- **Q distinctes** : 3
- **Distracteurs porteurs** :
  - `08:01#4→a` « لا سجعَ بينهما، لأنّ إحداهما منوّنةٌ والأخرى غيرُ منوّنةٍ في آخرِها تم… » — R1 : « الحركة … فلا عبرة بها »
  - `08:02#3→d` « فيه طباقانِ وسجعٌ لأنّ الفاصلتَين «الأمنَ» و«الخوفَ» تنتهيانِ بالفتحةِ… » — R1 : « اتّفاق الحركة في الآخر لا يصنع سجعًا »
  - `08:04#2→b` « الفواصلُ الثّلاثُ تنتهي بالألفِ قبلَ الميمِ، فالحرفُ الأخيرُ فيها هو ا… » — R1 : « الألف التي قبل الميم ليست الحرف الأخير »

#### `arabe.badi3.maqama-bi-saj3-faqat` — NEUF

- **AR** : تعدُّ كلَّ نصٍّ مسجوعٍ مقامةً (مثلٌ، مقدّمةُ كتابٍ، خطبةٌ): السّجعُ مقوِّمٌ واحدٌ، وتحتاجُ المقامةُ إلى السّندِ والبطلِ المحتالِ والواقعةِ في مجلسٍ
- **FR** : Tu prends tout texte rimé pour une maqāma (proverbe, préface, sermon) : le saj' n'est qu'un trait ; il faut aussi l'isnād, le héros filou et la scène unique
- **EN** : You take every rhymed text for a maqama (proverb, preface, sermon): saj' is only one trait; you also need the isnad, a trickster hero and a single-session scene
- **Chapitres / piège** : ch08 — piège n°4 « عدُّ كلِّ نصٍّ مسجوعٍ مقامةً. قال تلميذٌ عن المثلِ «مَن جدَّ وجدَ، ومَن زرعَ حصدَ»: «مقامةٌ، لأنّ فيه سجعًا». … »
- **Q distinctes** : 2
- **Distracteurs porteurs** :
  - `08:01#6→a` « «مَن جدَّ وجدَ، ومَن زرعَ حصدَ، ومَن صبرَ ظفرَ…» » — R1 : « فيه سجع لا سند »
  - `08:02#4→a` « مقدّمةُ كتابٍ قديمٍ مسجوعةُ الجملِ كلِّها، تحمدُ اللهَ ثمّ تعرضُ موضوع… » — R1 : « سجع بلا سند ولا بطل … مرسلة بلا سند »
  - `08:02#4→b` « خطبةٌ مسجوعةٌ تدعو إلى الصّبرِ على الشّدائدِ، تتخلّلُها آياتٌ وأحاديثُ… » — R1 : « سجع بلا سند ولا بطل … مرسلة بلا سند »
  - `08:02#4→d` « قصّةٌ حديثةٌ بأسلوبٍ مرسَلٍ تحكي عن محتالٍ ينجحُ في خداعِ النّاسِ ثمّ … » — R1 : « سجع بلا سند ولا بطل … مرسلة بلا سند »

#### `arabe.badi3.saj3-bi-tashabuh-al-bina2` — NEUF

- **AR** : تجدُ سجعًا لأنّ الجملتَين متشابهتانِ في البناءِ أو الطّولِ أو المعنى أو تكرّرَ فيهما لفظٌ: لا سجعَ بلا اتّفاقِ حرفِ الفاصلتَين الأخيرِ
- **FR** : Tu vois du saj' car les phrases se ressemblent par la construction, la longueur, le sens ou un mot répété : pas de saj' sans même dernière lettre des fāṣila
- **EN** : You see saj' because the clauses match in structure, length, meaning or a repeated word: no saj' without the same final letter in the clause-endings
- **Chapitres / piège** : ch08 — (pas de piège ; erreur récurrente dans les items)
- **Q distinctes** : 4
- **Distracteurs porteurs** :
  - `08:quiz#3→a` « «العلمُ نورٌ يُضيءُ الدّروبَ، والجهلُ ظلامٌ يُخفي الطّريقَ» » — R1 : « تشابه بناء الجملتين أو تقابل معنييهما لا يصنع سجعًا »
  - `08:quiz#3→b` « «مَن صبرَ على الشّدائدِ ظفرَ، ومَن تأنّى في الأمورِ سلمَ» » — R1 : « تشابه بناء الجملتين أو تقابل معنييهما لا يصنع سجعًا »
  - `08:quiz#3→c` « «يكتبُ سامي دروسَه في الصّباحِ، ويقرأُ كتبَه في المساءِ» » — R1 : « تشابه بناء الجملتين أو تقابل معنييهما لا يصنع سجعًا »
  - `08:01#5→b` « فيه سجعٌ، لأنّ الجملتَين متقاربتانِ في الطّولِ وفيهما فعلانِ ماضيانِ » — R1 : « تقارب الجملتين في الطول أو تشابههما في البناء لا يصنع سجعًا »
  - `08:01#5→c` « فيه سجعٌ، لأنّ الجملتَين متشابهتانِ في البناءِ والمعنى معًا » — R1 : « تقارب الجملتين في الطول أو تشابههما في البناء لا يصنع سجعًا »
  - `08:02#3→b` « فيه طباقٌ واحدٌ فقط («الخيرَ» ↔ «الشّرَّ») وسجعٌ لأنّ الجملتَين متماثل… » — R1 (paraphrase de l'explication) :  تماثل الجملتين في البناء وتكرار حصد لا يصنع سجعًا 
  - `08:02#3→c` « فيه سجعٌ لأنّ «حصدَ» تكرّرتْ في الجملتَين، وليس فيه طباقٌ لأنّ الجملتَ… » — R1 (paraphrase de l'explication) :  تماثل الجملتين في البناء وتكرار حصد لا يصنع سجعًا 
  - `08:05#4→c` « يبقى السّجعُ لأنّ «جمعَ» و«حصدَ» متقاربتانِ في المعنى ومتشابهتانِ في ا… » — R1 : « تقارب الفعلين في المعنى لا يصنع سجعًا »

#### `arabe.badi3.saj3-mutakallaf-3ala-hisab-al-ma3na` — NEUF

- **AR** : تضحّي بالمعنى من أجلِ السّجعِ (غيّرتَ الفكرةَ أو حشوتَ كلامًا لا صلةَ له): السّجعُ يُطربُ إذا جاءَ غيرَ متكلَّفٍ، وإلّا بقيَ الأسلوبُ مرسَلًا
- **FR** : Tu sacrifies le sens au saj' (idée changée, mots sans rapport ajoutés) : le saj' plaît quand il vient sans effort, sinon on garde un style libre (مرسَل)
- **EN** : You sacrifice meaning for saj' (changing the idea or padding with unrelated words): saj' pleases when effortless, otherwise keep a plain (مرسَل) style
- **Chapitres / piège** : ch08 — piège n°3 « التّضحيةُ بالمعنى في سبيلِ السّجعِ. كتبَ تلميذٌ عن القراءةِ: «القراءةُ غذاءُ العقلِ، وأجملُ ما في اللّيلِ ضوءُ… »
- **Q distinctes** : 4
- **Distracteurs porteurs** :
  - `08:quiz#5→a` « أن يغيّرَ فكرتَه لتوافقَ الفاصلةَ الثّانيةَ التي جاءتْه » — R1 : « تغيير الفكرة أو حشو كلمات لا صلة لها فتضحية بالمعنى »
  - `08:quiz#5→b` « أن يُتمَّ الجملةَ بكلماتٍ لا صلةَ لها بفكرتِه ما دامتِ الفاصلتانِ متوا… » — R1 : « تغيير الفكرة أو حشو كلمات لا صلة لها فتضحية بالمعنى »
  - `08:04#3→a` « أن يُبقيَ الجملتَين كما هما، لأنّ الفاصلتَين متوافقتانِ والسّجعُ هو ال… » — R1 : « تُبقي التكلّف أو تزيده »
  - `08:04#3→c` « أن يغيّرَ فاصلةَ الجملةِ الثّانيةِ ليزولَ السّجعُ وتبقى الجملةُ كما هي… » — R1 : « تُبقي التكلّف أو تزيده »
  - `08:04#3→d` « أن يزيدَ جملةً ثالثةً مسجوعةً بالحاءِ أيًّا كانَ معناها ليقوّيَ الإيقا… » — R1 : « تُبقي التكلّف أو تزيده »
  - `08:04#6→a` « اختيارُ فاصلتَين متوافقتَين أوّلًا، فبناءُ المعنى حولَهما، فالقراءةُ ب… » — R1 : « تقديم الفاصلتين على المعنى »
  - `08:05#5→b` « أن يحذفَ الحجّةَ ويكتفيَ بالسّجعِ لأنّه أطربُ للأذنِ وأبقى في الذّاكرة… » — R1 (paraphrase de l'explication) :  ليس صحيحًا أنّ السجع يغني عن الحجّة 

#### `arabe.badi3.saj3-yatlub-kalimatayn-mutashabihatayn` — NEUF

- **AR** : تشترطُ في السّجعِ تشابهَ الكلمتَين (الحرفَ الأوّلَ أو العددَ أو الكلمةَ كلَّها): السّجعُ توافقُ الفاصلتَين في الحرفِ الأخيرِ وحدَه
- **FR** : Tu exiges au saj' que les deux mots se ressemblent (première lettre, nombre de lettres, mot entier) : le saj' ne demande que la dernière lettre identique
- **EN** : You require the two rhyme words to look alike (first letter, letter count, whole word): saj' only needs the same last letter
- **Chapitres / piège** : ch08 — piège n°2 « طلبُ اتّفاقِ الكلمتَين كلِّهما بدلَ الحرفِ الأخيرِ. قال تلميذٌ: «لا سجعَ في «مَن جدَّ وجدَ، ومَن زرعَ حصدَ»، ل… »
- **Q distinctes** : 5
- **Distracteurs porteurs** :
  - `08:quiz#2→b` « الكلمةُ بجميعِ حروفِها في كلٍّ منهما » — R1 : « لا يُطلب أن تتّفق الكلمتان في جميع حروفهما »
  - `08:quiz#2→c` « الحرفُ الأوّلُ في كلٍّ منهما » — R1 : « لا يُطلب أن تتّفق الكلمتان في جميع حروفهما »
  - `08:quiz#2→d` « عددُ الحروفِ في كلٍّ منهما » — R1 : « لا يُطلب أن تتّفق الكلمتان في جميع حروفهما »
  - `08:01#4→b` « لا سجعَ بينهما، لأنّ الكلمتَين تختلفانِ في أحرفِهما الأولى وفي عددِها » — R1 : « لا يُطلب أن تتّفق الكلمتان في بقية حروفهما »
  - `08:01#4→d` « بينهما سجعٌ، لأنّ الكلمتَين متساويتانِ في عددِ حروفِهما كلِّها » — R1 : « لا يُطلب أن تتّفق الكلمتان في بقية حروفهما »
  - `08:04#1→c` « أن تعدَّ كلماتِ كلٍّ منهما لتتأكّدَ من تساويها »
  - `08:04#2→a` « فاصلتانِ فقط تتوافقانِ هما «السّلامَ» و«الطّعامَ» لتشابهِ حروفِهما، أم… » — R1 : « تشابه الكلمات في حروفها لا يُشترط »
  - `08:05#2→b` « «الصّدقِ» و«الصّبرِ» » — R1 : « التشابه في غير الحرف الأخير لا يصنع سجعًا »
  - `08:05#2→c` « «الأملِ» و«الأمنِ» » — R1 : « التشابه في غير الحرف الأخير لا يصنع سجعًا »
  - `08:05#2→d` « «الفجرِ» و«النّجمِ» » — R1 : « التشابه في غير الحرف الأخير لا يصنع سجعًا »

#### `arabe.badi3.takrir-saj3-fi-kull-jumla` — NEUF

- **AR** : تسجعُ كلَّ جملةٍ في الفقرةِ أو تزيدُ جملًا مسجوعةً: الإكثارُ يُثقلُ ويُخفي الحجّةَ؛ والكتابُ يقولُ «أحيانًا»، موضعٌ أو موضعانِ يخدمانِ فكرةً مهمّةً
- **FR** : Tu mets du saj' dans chaque phrase ou en ajoutes : l'excès alourdit et masque l'argument ; le manuel dit « parfois » — un ou deux endroits clés
- **EN** : You put saj' in every sentence or add more: excess weighs down and hides the argument; the book says "sometimes" — one or two key spots
- **Chapitres / piège** : ch08 — piège n°5 « الإكثارُ: أن تكونَ كلُّ جملةٍ في الفقرةِ مسجوعةً. فقرةٌ كلُّها محسِّناتٌ تُثقلُ القارئَ وتُخفي الحجّةَ، والكتا… »
- **Q distinctes** : 3
- **Distracteurs porteurs** :
  - `08:quiz#5→d` « أن يُكثرَ من السّجعِ في بقيّةِ الجملِ ليعوّضَ هذا النّقصَ » — R1 : « كثرة السجع في بقية الجمل تُثقل الأسلوب »
  - `08:04#6→c` « كتابةُ المعنى أوّلًا، فإضافةُ سجعٍ في كلِّ جملةٍ من الفقرةِ، فالقراءةُ… » — R1 : « سجع كل جملة … ختم الجمل كلها بفاصلة واحدة »
  - `08:04#6→d` « اختيارُ ضدَّين أوّلًا، فكتابةُ المعنى حولَهما، فختمُ الجملِ كلِّها بفا… » — R1 : « سجع كل جملة … ختم الجمل كلها بفاصلة واحدة »
  - `08:05#5→a` « أن يزيدَ عددَ الجملِ المسجوعةِ ليقتنعَ القارئُ بقوّةِ الأسلوبِ في كلِّ… » — R1 : « فالإكثار منها يُثقل القارئ ويُخفي الحجّة »

#### `arabe.badi3.tibaq-saj3-khalt` — NEUF

- **AR** : تخلطُ بين الطّباقِ والسّجعِ: الطّباقُ جمعٌ لمعنيَين متضادَّين، والسّجعُ توافقُ الفاصلتَين في الحرفِ الأخيرِ وأثرُه الإيقاعُ
- **FR** : Tu confonds tibāq et saj' : le tibāq réunit deux sens opposés, le saj' est l'accord de la dernière lettre des fāṣila et son effet est le rythme
- **EN** : You confuse tibaq and saj': tibaq joins two opposite meanings, saj' is the match of the final letter of clause-endings and its effect is rhythm
- **Chapitres / piège** : ch08 — (pas de piège ; erreur récurrente dans les items)
- **Q distinctes** : 7
- **Distracteurs porteurs** :
  - `08:quiz#1→a` « توافقُ الفاصلتَين أو الفواصلِ في الحرفِ الأخيرِ » — R1 : توافق الفواصل = السجع ، المقارنة بالأداة = تشبيه
  - `08:quiz#1→b` « ذكرُ المعنى نفسِه بلفظَين مختلفَين في الجملةِ الواحدةِ » — R1 : توافق الفواصل = السجع ، المقارنة بالأداة = تشبيه
  - `08:quiz#1→d` « مقارنةٌ بين شيئَين تُذكرُ فيها الأداةُ ووجهُ الشّبَهِ » — R1 : توافق الفواصل = السجع ، المقارنة بالأداة = تشبيه
  - `08:01#3→b` « جمعَ في كلامِه بين معنيَين متضادَّين » — R1 : جمع متضادين = المعنى البلاغي، توافق الفاصلتين سجع
  - `08:01#3→c` « وافقَ بين فاصلتَين في حرفِهما الأخيرِ » — R1 : جمع متضادين = المعنى البلاغي، توافق الفاصلتين سجع
  - `08:01#3→d` « قارنَ بين شيئَين ثمّ شبّهَ أحدَهما بالآخرِ » — R1 : جمع متضادين = المعنى البلاغي، توافق الفاصلتين سجع
  - `08:04#4→b` « لا طباقَ فيه، لأنّ «أضحكَ» و«أبكى» تنتهيانِ بحرفَين مختلفَين » — R1 (paraphrase de l'explication) :  اختلاف حرفي آخرهما يمنع السجع لا الطباق 
  - `08:04#5→a` « يُحدثُ إيقاعًا موسيقيًّا خفيفًا بتوافقِ الفاصلتَين في الحرفِ الأخيرِ ب… » — R1 (paraphrase de l'explication) :  الإيقاع أثر السجع ولا سجع هنا 
  - `08:05#4→d` « يتحوّلُ السّجعُ إلى طباقٍ لأنّ «جمعَ» تخالفُ «حصدَ» في الحرفِ الأخيرِ … » — R1 : « ولا يتحوّل اختلاف الحرف الأخير إلى طباق »
  - `08:06#3→b` « الطّباقُ يُحدثُ الإيقاعَ بتوافقِ الفاصلتَين، والسّجعُ يُبرزُ الفرقَ بي… » — R1 : « الإيقاع من أثر السجع لا الطباق »
  - `08:06#3→d` « الطّباقُ والسّجعُ كلاهما يُحدثانِ الإيقاعَ، ولا أثرَ لهما في إبرازِ ال… » — R1 : « الإيقاع من أثر السجع لا الطباق »
  - `08:06#6→a` « لأنّ فواصلَ أبياتِها تنتهي كلُّها بحرفٍ واحدٍ في آخرِ كلِّ بيتٍ منها ت… » — R1 : « اتّفاق الأواخر فسجع لا طباق »

#### `arabe.badi3.tibaq-saj3-yajtami3an` — NEUF

- **AR** : تثبتُ الطّباقَ وتنفي السّجعَ أو العكسَ وهما معًا (الأفراحُ/الأتراحُ: ضدّانِ وفاصلتانِ بالحاءِ): افحصِ الضدَّين ثمّ الحرفَ الأخيرَ كلًّا على حدةٍ
- **FR** : Tu retiens le tibāq sans le saj' (ou l'inverse) alors que les deux sont là (الأفراحُ/الأتراحُ) : vérifie d'abord les contraires, puis la dernière lettre
- **EN** : You keep tibaq without saj' (or the reverse) when both are present (الأفراحُ/الأتراحُ): check the opposites first, then the final letter
- **Chapitres / piège** : ch08 — (pas de piège ; erreur récurrente dans les items)
- **Q distinctes** : 3
- **Distracteurs porteurs** :
  - `08:02#1→a` « طباقٌ بين «الأفراحِ» و«الأتراحِ» فقط، لأنّ الفاصلتَين لا تتّفقانِ في ا… » — R1 : « فمن أنكر أحدهما أخطأ »
  - `08:02#1→b` « سجعٌ بين الفاصلتَين فقط، لأنّه لا تقابلَ بين معنى «الأفراحِ» ومعنى «ال… » — R1 : « فمن أنكر أحدهما أخطأ »
  - `08:02#1→c` « لا طباقَ ولا سجعَ، فالأسلوبُ مرسَلٌ لأنّ الجملتَين تختلفانِ في المعنى … » — R1 : « فمن أنكر أحدهما أخطأ »
  - `08:02#5→a` « «العدلُ يبني العمرانَ، والظّلمُ يهدمُ الدّولَ» » — R1 : « فيها طباق ولا سجع … سجع ولا طباق … لا هذا ولا ذاك »
  - `08:02#5→b` « «العدلُ يبني العمرانَ، والإحسانُ يملأُ الأوطانَ» » — R1 : « فيها طباق ولا سجع … سجع ولا طباق … لا هذا ولا ذاك »
  - `08:02#5→c` « «العدلُ يبني العمرانَ، والإحسانُ يملأُ القلوبَ» » — R1 : « فيها طباق ولا سجع … سجع ولا طباق … لا هذا ولا ذاك »
  - `08:06#4→a` « يُطفئُ الهمّةَ » — R1 (paraphrase de l'explication) :  فيها طباق لكنّ فاصلتها … فلا سجع … سجع لكنّها لا تضادّ … لا طباق ولا سجع 
  - `08:06#4→b` « يُضيءُ الأملَ » — R1 (paraphrase de l'explication) :  فيها طباق لكنّ فاصلتها … فلا سجع … سجع لكنّها لا تضادّ … لا طباق ولا سجع 
  - `08:06#4→d` « يُوهنُ العزيمةَ » — R1 (paraphrase de l'explication) :  فيها طباق لكنّ فاصلتها … فلا سجع … سجع لكنّها لا تضادّ … لا طباق ولا سجع 

### Domaine `fahm`

#### `arabe.fahm.jawab-min-kharij-al-nass` — NEUF

- **AR** : تجيبُ من رأيِك أو من الحياةِ لا من قرائنِ النّصِّ (الفقرُ مؤلمٌ فالكاتبُ حزينٌ): المصحِّحُ يطلبُ قرينةً من السّندِ وإلّا فجوابُك رأيُك لا فهمُك
- **FR** : Tu réponds d'après ton avis ou la vie, non le texte (la pauvreté est pénible donc l'auteur est triste) : il faut un indice du support, sinon c'est une opinion
- **EN** : You answer from your own view or real life, not the text (poverty hurts so the author is sad): you need a clue from the passage, else it is mere opinion
- **Chapitres / piège** : ch11 — piège n°1 « الجواب من خارج النصّ. قول «الكاتب حزين لأنّ الفقر مؤلم» صحيحٌ في الحياة وخاطئٌ هنا: النصّ لا يشكو الفقر بل **ي… »
- **Q distinctes** : 4
- **Distracteurs porteurs** :
  - `11:01#2→b` « سخريةٌ من العمّال وأصحاب الحرف » — R1 : « لا حزن على ضياعٍ لم يُذكر »
  - `11:01#2→c` « حيادٌ تامّ لا موقف فيه » — R1 : « لا حزن على ضياعٍ لم يُذكر »
  - `11:01#2→d` « حزنٌ وأسًى على ضياع العمل » — R1 : « لا حزن على ضياعٍ لم يُذكر »
  - `11:02#3→b` « استفهامٌ حقيقيّ يطلب الكاتبُ به جوابًا يجهله » — R1 : « ولا يدلّ على شكّه فهو مقتنعٌ متفائل »
  - `11:02#3→c` « استفهامٌ يدلّ على شكّ الكاتب في قدرة الإنسان » — R1 : « ولا يدلّ على شكّه فهو مقتنعٌ متفائل »
  - `11:02#3→d` « استفهامٌ للتمنّي والترجّي » — R1 : « ولا يدلّ على شكّه فهو مقتنعٌ متفائل »
  - `11:03#1→d` « ينبغي للفنون أن تنغلق على ذاتها حفاظًا على أصالتها » — R1 : « يناقض موقف الكاتب تمامًا »
  - `11:03#5→b` « الفنونُ الأجنبيّة أرقى دائمًا من فنوننا فيجب اتّباعها كما هي » — R1 : « يناقض الأطروحة … يؤيّد الانغلاق الذي ذمّه النصّ »
  - `11:03#5→c` « ينبغي منعُ كلّ تأثيرٍ أجنبيّ خوفًا على الهويّة » — R1 : « يناقض الأطروحة … يؤيّد الانغلاق الذي ذمّه النصّ »
  - `11:03#5→d` « الهويّةُ مفهومٌ متغيّر لا قيمة للحفاظ عليه » — R1 : « يناقض الأطروحة … يؤيّد الانغلاق الذي ذمّه النصّ »

#### `arabe.fahm.tafsil-ka-fikra-amma` — NEUF

- **AR** : تعدُّ تفصيلةً أو مثالًا أو إشارةً عابرةً الفكرةَ العامّةَ للنّصِّ: الفكرةُ العامّةُ جملةٌ جامعةٌ تضمُّ الموضوعَ وموقفَ الكاتبِ
- **FR** : Tu prends un détail, un exemple ou une allusion pour l'idée générale du texte : c'est une phrase qui réunit le thème et la position de l'auteur
- **EN** : You take a detail, an example or a passing remark for the text's main idea: it is one sentence combining the theme and the author's stance
- **Chapitres / piège** : ch11 — (pas de piège ; erreur récurrente dans les items)
- **Q distinctes** : 3
- **Distracteurs porteurs** :
  - `11:quiz#1→b` « العاملُ يكسب قوته كلّ يوم » — R1 : « تفصيلان جزئيّان … إشارة عابرة »
  - `11:quiz#1→c` « المصانعُ تُبنى بسواعد العمّال » — R1 : « تفصيلان جزئيّان … إشارة عابرة »
  - `11:quiz#1→d` « الكسلُ صفةٌ ذميمة في بعض الناس » — R1 : « تفصيلان جزئيّان … إشارة عابرة »
  - `11:01#1→b` « الحرفيُّ البسيط رفض الإحسان مرّةً واحدة » — R1
  - `11:01#1→c` « بعضُ الناس يحتقرون المهن اليدويّة » — R1
  - `11:01#1→d` « المرءُ يأكل من كدّ يمينه كلّ يوم » — R1
  - `11:02#1→b` « التلوّثُ يخنق هواءَ المدن الكبرى » — R1
  - `11:02#1→c` « الإنسانُ نجح في قهر الفضاء واستكشافه » — R1
  - `11:02#1→d` « الفقرُ ينهش أجسادَ ملايين البشر » — R1

### Domaine `fi3l`

#### `arabe.fi3l.hukm-bil-haraka` — RÉUTILISÉ (REGISTRE)

- **AR** : تحكمُ على الفعلِ بحركةِ آخرِه أو تخلطُ بينَ «لن» و«لم»: الأداةُ هي الّتي تحكم، «لن» تنصبُ و«لم» تجزم
- **FR** : Tu juges le verbe par sa voyelle finale ou tu confonds « لن » et « لم » : c'est l'outil qui décide — لن، أن، كي، حتّى : naṣb ; لم : jazm
- **Chapitres / piège** : ch01 — (pas de piège ; erreur récurrente dans les items)
- **Q distinctes** : 3
- **Distracteurs porteurs** :
  - `01:02#2→b` « فعل مضارع مرفوع بالضمّة » — R1 : « لم أداة جزم تجزم المضارع »
  - `01:02#2→c` « فعل مضارع منصوب بالفتحة » — R1 : « لم أداة جزم تجزم المضارع »
  - `01:04#5→d` « السكون لأنّ «لن» تجزم المضارع » — R1 : « لن حرف نصب لا جزم »
  - `01:05#3→a` « فعل مضارع مرفوع بالضمّة » — R1 : « لا يُجزم لأنّ الجزم يكون بأدوات الجزم كـ لم »
  - `01:05#3→b` « فعل مضارع مجزوم بالسكون » — R1 : « لا يُجزم لأنّ الجزم يكون بأدوات الجزم كـ لم »

### Domaine `hijaj`

#### `arabe.hijaj.aqwal-bila-jumal-sardiyya` — NEUF

- **AR** : تكتبُ أقوالًا متتاليةً بلا جملٍ سرديّةٍ («— … — بل …»): لا يُعرفُ من يتكلّمُ؛ الجملةُ السّرديّةُ (فابتسمَ وردَّ:) تعيّنُ المتكلّمَ وتنقلُ الكلامَ
- **FR** : Tu enchaînes des répliques sans phrase narrative (« — … — بل … ») : on ne sait pas qui parle ; la phrase narrative (فابتسمَ وردَّ :) nomme le locuteur
- **EN** : You string replies together with no narrative sentence ('— … — بل …'): nobody knows who speaks; a narrative sentence (فابتسمَ وردَّ:) names the speaker
- **Chapitres / piège** : ch09 — piège n°11 « أقوالٌ متتاليةٌ بلا جملٍ سرديّةٍ: «— المراجعةُ المنتظمةُ أجدى. — بل ليلةُ الامتحانِ تكفي.» لا يُعرفُ من يتكلّم… »
- **Q distinctes** : 1
- **Distracteurs porteurs** :
  - `09:06#5→b` « — الفوزُ أهمُّ من الروحِ الرياضيّةِ. — بل الروحُ الرياضيّةُ أهمُّ منه.… » — R1 : « أقوال متتالية بلا جملة سردية فلا يُعرف من يتكلم »

#### `arabe.hijaj.arkan-khalt` — NEUF

- **AR** : تخلطُ بين أركانِ النّصِّ الحجاجيِّ: الأطروحةُ رأيٌ، والحجّةُ سببٌ عامٌّ، والمثالُ واقعةٌ ملموسةٌ، والاستنتاجُ خلاصةٌ تختمُ الكلامَ
- **FR** : Tu confonds les éléments du texte argumentatif : thèse (avis), argument (raison générale), exemple (fait concret), conclusion (bilan final)
- **EN** : You mix up the parts of an argumentative text: thesis (opinion), argument (general reason), example (concrete fact), conclusion (closing summary)
- **Chapitres / piège** : ch09, ch10, ch11 — (pas de piège ; erreur récurrente dans les items)
- **Q distinctes** : 24
- **Distracteurs porteurs** :
  - `09:quiz#1→a` « واقعةٌ ملموسةٌ محسوسةٌ تُذكرُ لتوضيحِ حجّةٍ ما » — R1 (paraphrase de l'explication) :  الواقعة = المثال، السبب = الحجة، النتيجة = الاستنتاج 
  - `09:quiz#1→c` « سببٌ عامٌّ يُقامُ دليلًا على رأيٍ » — R1 (paraphrase de l'explication) :  الواقعة = المثال، السبب = الحجة، النتيجة = الاستنتاج 
  - `09:quiz#1→d` « نتيجةٌ يُختَمُ بها النصُّ بعدَ عرضِ الحججِ والأمثلةِ » — R1 (paraphrase de l'explication) :  الواقعة = المثال، السبب = الحجة، النتيجة = الاستنتاج 
  - `09:quiz#3→b` « أطروحةٌ يدافعُ عنها المتكلّمُ ويريدُ إقناعَنا بها »
  - `09:quiz#3→d` « استنتاجٌ يختمُ الكلامَ بخلاصةٍ مستخلَصةٍ »
  - `09:01#2→c` « إذن لنجعلْ من المطالعةِ عادةً يوميّةً لا نتخلّى عنها »
  - `09:01#3→b` « التدخينُ يضرُّ بالمدخّنِ وبمن حولَه » — R1 : « سبب جاء بعد لأنّ أي حجة لا أطروحة »
  - `09:06#1→a` « الأطروحةُ: (1) و(2)؛ سيرورةُ الحجاجِ: (3) و(4)؛ الاستنتاجُ: (5) » — R1 : « لا تُضمّ (2) إلى الأطروحة لأنها سبب »
  - `09:06#3→a` « الفنُّ يُهذّبُ الذوقَ ويقرّبُ بينَ الشعوبِ ويُخفّفُ عن النفسِ ثقلَها » — R1 : « حجج تسند الأطروحة لا هي الأطروحة »
  - `10:quiz#1→a` « الجملةُ (1) » — R1 : أطروحة / حجة / مثال
  - `10:quiz#1→b` « الجملةُ (2) » — R1 : أطروحة / حجة / مثال
  - `10:quiz#1→c` « الجملةُ (3) » — R1 : أطروحة / حجة / مثال
  - `10:quiz#2→c` « الولدُ الذي يُصغي إليه أبوه يصارحُه بمشكلاتِه »
  - `10:quiz#3→a` « الطفلُ يقلّدُ ما يراهُ » — R1 : « سببان عامّان … أطروحة »
  - `10:quiz#3→b` « الطفلُ لا يميّزُ بين الصوابِ والخطأِ » — R1 : « سببان عامّان … أطروحة »
  - `10:quiz#3→d` « ينبغي أن نحدّدَ ساعاتِ مشاهدةِ التلفازِ للأطفالِ » — R1 : « سببان عامّان … أطروحة »
  - `10:quiz#4→d` « نحتاجُ إلى تعلّمِ لغةٍ أجنبيّةٍ »
  - `10:01#1→a` « الأطروحةُ »
  - `10:01#1→b` « الاستنتاجُ »
  - `10:01#2→b` « من (1) إلى (4) »
  - `10:01#3→b` « كلُّ يدٍ تمتدُّ بالعونِ تخفّفُ من وطأةِ الحاجةِ » — R1 : « حجّة تدعم رأيه لا الرأي نفسه »
  - `10:02#1→c` « ينبغي أن نُكثرَ من حصصِ المكتبةِ في المعهدِ »
  - `10:02#2→a` « يجبُ أن يبيعَ المقصفُ الحلوياتِ »
  - `10:02#2→c` « يجبُ أن يمنعَ المقصفُ الحلوياتِ »
  - `10:03#1→d` « جارُ الكاتبِ يتبرّعُ بدمِه كلَّ ثلاثةِ أشهرٍ »
  - `10:03#2→b` « التعليمُ عن بُعدٍ أفضلُ من الحضورِ في القسمِ »
  - `10:03#2→d` « الحضورُ في القسمِ أجدى »
  - `10:04#4→d` « يجبُ أن نشجّعَ العملَ الجماعيَّ في المشاريعِ المدرسيّةِ »
  - `10:05#2→a` « تربيةُ الحيواناتِ الأليفةِ في البيتِ عبءٌ لا فائدةَ منه »
  - `10:05#2→b` « تربيةُ الحيواناتِ الأليفةِ مفيدةٌ للطفلِ »
  - `10:06#2→b` « من يغشُّ يبني نجاحَه على جهدِ غيرِه » — R1 : « حجّة تخدم رأيه »
  - `10:06#3→b` « السياحةُ وحدَها تكفي لإنعاشِ اقتصادِنا كلِّه »
  - `10:06#3→c` « يجبُ أن نُنوّعَ مصادرَ الدخلِ في بلادِنا »
  - `11:01#6→c` « رأيتُ ذات يومٍ نجّارًا يصنع بابًا جميلًا » — R1 : « مثالٌ جزئيّ محسوس »
  - `11:02#6→b` « إنّ التعاونَ بين الأمم ضرورةٌ لا غنى عنها في عصرنا » — R1 : « تكراران للحجّة … معلومة جانبيّة »
  - `11:02#6→c` « لا يمكن لدولةٍ واحدة أن تحلّ المشكلات الكونيّة بمفردها » — R1 : « تكراران للحجّة … معلومة جانبيّة »
  - `11:02#6→d` « التعاونُ الدوليّ مفهومٌ يدرسه طلّابُ العلوم السياسيّة » — R1 : « تكراران للحجّة … معلومة جانبيّة »
  - `11:03#1→b` « النغمُ الأندلسيّ جمع بين شجن الشرق ورقّة الغرب » — R1 : « مثالان جزئيّان يخدمان الأطروحة لا هي »
  - `11:03#1→c` « العمارةُ الإسلاميّة أبدعت طرزًا معماريّة خالدة » — R1 : « مثالان جزئيّان يخدمان الأطروحة لا هي »

#### `arabe.hijaj.awwal-ra2y-muthbat` — NEUF

- **AR** : تعدُّ الرّأيَ الأوّلَ أو الجملةَ الأولى هي الأطروحةَ المثبتةَ لأنّها جاءت أوّلًا: الورودُ لا يحدّدُ شيئًا، بل موقفُ الكاتبِ: أيردُّ الرّأيَ أم يدافعُ عنه؟
- **FR** : Tu prends le 1ᵉʳ avis ou la 1ʳᵉ phrase pour la thèse défendue : l'ordre ne décide rien, c'est la position de l'auteur : il réfute cet avis ou le défend ?
- **EN** : You take the first opinion or sentence for the defended thesis: order decides nothing, the author's stance does — does he reject this view or defend it?
- **Chapitres / piège** : ch09 — piège n°2 « صياغةُ الأطروحةِ عنوانًا أو سؤالًا: «المراجعةُ» أو «هل تنفعُ المراجعةُ؟» ليستا أطروحةً، فلا رأيَ فيهما يُقبلُ … » (deux erreurs); ch09 — piège n°6 « عدُّ أوّلِ جملةٍ في النصِّ أطروحتَه دائمًا: في هذا النصِّ الجملةُ الأولى هي المدحوضةُ والمثبتةُ جاءتْ بعدَها؛ … » (deux erreurs)
- **Q distinctes** : 2
- **Distracteurs porteurs** :
  - `09:quiz#2→b` « الرأيُ الذي يرِدُ أوّلًا في النصِّ مهما كانَ موقفُ الكاتبِ منه » — R1 : « ليس الورود أولًا هو الذي يجعل الأطروحة مدحوضة »
  - `09:01#3→a` « التدخينُ حرّيّةٌ شخصيّةٌ يمارسُها الإنسانُ كما يشاءُ » — R1 : « يردّ رأي بعضهم »

#### `arabe.hijaj.da3ima-dahida-khalt` — NEUF

- **AR** : تخلطُ بين الحجّةِ الدّاعمةِ للأطروحةِ والدّاحضةِ لها: الدّاعمةُ تسندُ الرّأيَ، والدّاحضةُ سببٌ عامٌّ يُبطلُه وتأتي غالبًا بعد «غيرَ أنّ»
- **FR** : Tu confonds l'argument qui soutient une thèse et celui qui la réfute : l'un appuie l'avis, l'autre est une raison qui le ruine, souvent après « غيرَ أنّ »
- **EN** : You confuse a supporting argument with a refuting one: one backs the view, the other is a reason that undoes it, often after « غيرَ أنّ »
- **Chapitres / piège** : ch10 — (pas de piège ; erreur récurrente dans les items)
- **Q distinctes** : 4
- **Distracteurs porteurs** :
  - `10:quiz#4→a` « الترجمةُ الآليّةُ تكفي » — R1 : « حجّةُ كريمٍ التي تدعمُ رأيَه »
  - `10:02#2→b` « التلاميذُ يحبّونَ الحلوياتِ ويُقبلونَ عليها » — R1 : « حجّتُها التي تدعمُه لا التي تدحضُه »
  - `10:03#2→c` « التلميذُ في بيتِه تُلهيه الشاشاتُ والضجيجُ » — R1 : « حجّة داحضة لها يسوقها الكاتب »
  - `10:06#3→a` « السياحةُ تجلبُ العملةَ الصعبةَ » — R1 : « حجّة تدعم المدحوضة لا تدحضها »

#### `arabe.hijaj.dahd-bila-dalil` — NEUF

- **AR** : تدحضُ بالسّخريةِ أو بتشويهِ الرّأيِ (كلامُكَ ساذجٌ، أو تضيفُ إليه ما لم يقلْه): الدّحضُ دليلٌ يهدمُ الرّأيَ كما قيلَ لا تجريحٌ لصاحبِه
- **FR** : Tu réfutes par la moquerie ou en déformant l'avis (كلامُكَ ساذجٌ) : réfuter, c'est une preuve contre l'avis tel qu'il fut dit, pas viser la personne
- **EN** : You rebut by mockery or by distorting the view (كلامُكَ ساذجٌ): rebuttal is evidence against the view as stated, not an attack on the person
- **Chapitres / piège** : ch09 — piège n°13 « السخريةُ بدلَ الحجّةِ: «كلامُكَ ساذجٌ» ليس حجّةً داحضةً؛ الدحضُ يكونُ بدليلٍ يهدمُ الرأيَ لا بتجريحِ صاحبِه. و… » (trois erreurs ; les deux premières partagent un id)
- **Q distinctes** : 1
- **Distracteurs porteurs** :
  - `09:05#6→a` « أنتَ تزعمُ أنّ الرياضةَ تضيّعُ الوقتَ وتفسدُ الأخلاقَ، وهذا كلامُ الجا… » — R1 : « تشوّهه وتجرّحه … أو أن تسخر منه »
  - `09:05#6→d` « كلامُكَ ساذجٌ لا يستحقُّ الردَّ، فلنتحدّثْ في موضوعٍ آخرَ أحسنَ منه » — R1 : « تشوّهه وتجرّحه … أو أن تسخر منه »

#### `arabe.hijaj.faqra-muqatta3a` — NEUF

- **AR** : تقطّعُ الفقرةَ الحجاجيّةَ إلى نقاطٍ في أسطرٍ منفصلةٍ (أوّلًا … ثانيًا …): الفقرةُ كتلةٌ واحدةٌ تتّصلُ جملُها بمؤشّراتٍ
- **FR** : Tu découpes le paragraphe argumentatif en points sur des lignes séparées (أوّلًا … ثانيًا …) : c'est un bloc dont les phrases s'enchaînent par des connecteurs
- **EN** : You chop the argumentative paragraph into points on separate lines (أوّلًا … ثانيًا …): a paragraph is one block whose sentences are joined by connectors
- **Chapitres / piège** : ch09 — piège n°14 « تقطيعُ الفقرةِ إلى نقاطٍ أو أسطرٍ منفصلةٍ («أوّلًا: … ثانيًا: …» كلٌّ في سطرٍ): الفقرةُ كتلةٌ واحدةٌ تتّصلُ جم… » (deux erreurs)
- **Q distinctes** : 1
- **Distracteurs porteurs** :
  - `09:05#5→c` « نقاطٌ منفصلةٌ تحتَ عناوينَ «أوّلًا» و«ثانيًا» و«ثالثًا»، كلُّ نقطةٍ في… » — R1 : « النقاط المنفصلة تقطّع الفقرة وتحذف الاستنتاج »

#### `arabe.hijaj.hadhf-al-fatiha-wal-khatm` — NEUF

- **AR** : تحذفُ جملةَ الأطروحةِ أو الاستنتاجَ أو المثالَ من الفقرةِ الحجاجيّةِ: تبقى الحجّةُ معلّقةً والفقرةُ بلا بدايةٍ ولا ختمٍ
- **FR** : Tu supprimes la phrase de thèse, la conclusion ou l'exemple du paragraphe argumentatif : l'argument reste en l'air et le paragraphe n'a ni début ni clôture
- **EN** : You drop the thesis sentence, the conclusion or the example from the argumentative paragraph: the argument hangs and the paragraph has neither opening nor close
- **Chapitres / piège** : ch09 — piège n°14 « تقطيعُ الفقرةِ إلى نقاطٍ أو أسطرٍ منفصلةٍ («أوّلًا: … ثانيًا: …» كلٌّ في سطرٍ): الفقرةُ كتلةٌ واحدةٌ تتّصلُ جم… » (deux erreurs)
- **Q distinctes** : 1
- **Distracteurs porteurs** :
  - `09:05#5→d` « حجّتانِ بمثاليهما في كتلةٍ واحدةٍ دونَ جملةِ أطروحةٍ تفتتحُها ودونَ اس… » — R1 : « حذف الأطروحة والاستنتاج »

#### `arabe.hijaj.haqiqa-ka-qadiyya` — NEUF

- **AR** : تعدُّ حقيقةً متّفقًا عليها (أيّامُ الأسبوعِ، تجمّدُ الماءِ) قضيّةً تحتاجُ إلى حجاجٍ: الحجاجُ يقومُ على رأيٍ يمكنُ أن يُردَّ لا على حقيقةٍ ثابتةٍ
- **FR** : Tu prends un fait admis de tous (jours de la semaine, eau qui gèle) pour une question à argumenter : on argumente un avis réfutable, pas un fait établi
- **EN** : You take a fact everyone accepts (days of the week, freezing water) for something to argue: you argue an opinion that can be rejected, not an established fact
- **Chapitres / piège** : ch09 — piège n°1 « عدُّ كلِّ جملةٍ فيها «لأنّ» حجاجًا. «يتبخّرُ الماءُ لأنّ الحرارةَ تُحرّكُ جُزَيْئاتِه» تشرحُ ظاهرةً لا خلافَ ع… » (2ᵉ erreur (le مُخاطَب est toujours un adversaire) : aucun distracteur)
- **Q distinctes** : 1
- **Distracteurs porteurs** :
  - `09:01#1→a` « يتألّفُ الأسبوعُ في التقويمِ المتّبَعِ في بلادِنا من سبعةِ أيّامٍ » — R1 (paraphrase de l'explication) :  حقائق متّفق عليها لا يدخلها حجاج 
  - `09:01#1→b` « يتجمّدُ الماءُ النقيُّ عندَ درجةِ الصفرِ تحتَ الضغطِ العاديِّ » — R1 (paraphrase de l'explication) :  حقائق متّفق عليها لا يدخلها حجاج 
  - `09:01#1→d` « تقعُ تونسُ على الساحلِ الجنوبيِّ للبحرِ الأبيضِ المتوسّطِ » — R1 (paraphrase de l'explication) :  حقائق متّفق عليها لا يدخلها حجاج 

#### `arabe.hijaj.hukm-ra2yi-la-hijaji` — NEUF

- **AR** : تحكمُ على الكاتبِ برأيِك في الموضوعِ أو بجمالِ لغتِه أو بأهمّيّةِ موضوعِه («لا أحبُّ كرةَ القدمِ»، «لغتُه سلسةٌ»): والسّؤالُ عن قوّةِ حججِه
- **FR** : Tu juges l'auteur sur ton avis, sa belle langue ou l'importance du thème (« je n'aime pas le foot ») : la question porte sur la force de ses arguments
- **EN** : You judge the author by your own view, his language or his theme's importance ("I don't like football"): the question is about his arguments' strength
- **Chapitres / piège** : ch10 — piège n°8 « الحكمُ على **الأطروحةِ** لا على **الحجاجِ**: «لم يُوفَّقْ لأنّني لا أحبُّ الدروسَ الخصوصيّةَ» رأيٌ في الموضوعِ… »
- **Q distinctes** : 3
- **Distracteurs porteurs** :
  - `10:03#5→b` « لم يُوفَّقْ؛ لأنّني أفضّلُ البقاءَ في بلدي على السفرِ إلى الخارجِ » — R1 : رأي في الأطروحة لا في الحجاج / مديح بالأسلوب
  - `10:03#5→c` « وُفِّقَ؛ لأنّ لغتَه سلسةٌ وجملَه قصيرةٌ وواضحةٌ تسهّلُ على القارئِ الم… » — R1 : رأي في الأطروحة لا في الحجاج / مديح بالأسلوب
  - `10:05#6→d` « وُفِّقَ؛ لأنّ موضوعَه مهمٌّ ويهمُّ الجميعَ في كلِّ المجتمعاتِ » — R1 : « تعليل بالموضوع لا بالحجاج »
  - `10:06#6→c` « لم يُوفَّقْ؛ لأنّني لا أحبُّ كرةَ القدمِ ولا أرى حاجةً إلى ملعبٍ في ال… » — R1 : « رأي في الموضوع لا في الحجاج »

#### `arabe.hijaj.i3adat-al-utruha-hujja` — NEUF

- **AR** : تعدُّ إعادةَ الأطروحةِ بألفاظٍ أخرى حجّةً («المطالعةُ واجبةٌ»): الحجّةُ سببٌ من خارجِ الأطروحةِ، وليست تكرارًا لها
- **FR** : Tu prends la thèse reformulée pour un argument (« المطالعةُ واجبةٌ ») : l'argument est une raison extérieure à la thèse, pas une répétition
- **EN** : You count the thesis reworded as an argument (« المطالعةُ واجبةٌ »): an argument is a reason from outside the thesis, not a repeat of it
- **Chapitres / piège** : ch09 — piège n°3 « عدُّ إعادةِ الأطروحةِ حجّةً: «يجبُ أن نقرأَ لأنّ القراءةَ واجبةٌ» لا تضيفُ سببًا بل تكرّرُ الرأيَ بألفاظٍ أخرى… » (deux erreurs); ch10 — piège n°3 « عدُّ المثالِ حجّةً: «لاحظْنا في شارعِ المعهدِ …» واقعةٌ واحدةٌ قد تكونُ استثناءً، فلا تُقنعُ وحدَها؛ ولذلك يطل… » (deux erreurs (ids de ch09))
- **Q distinctes** : 3
- **Distracteurs porteurs** :
  - `09:01#2→d` « المطالعةُ واجبةٌ على كلِّ تلميذٍ مهما كانتْ ظروفُه » — R1 : « تعيد الأطروحة بألفاظ أخرى ولا تضيف سببًا »
  - `10:02#1→d` « حصصُ المكتبةِ ضروريّةٌ في كلِّ معهدٍ » — R1 : « إعادةٌ للأطروحةِ بلفظٍ آخرَ لا تضيفُ سببًا »
  - `10:04#4→a` « العملُ الجماعيُّ أفضلُ من العملِ الفرديِّ » — R1 : « يعيد الأطروحة بلفظ آخر »

#### `arabe.hijaj.iqna3-ta2thir-khalt` — NEUF

- **AR** : تحكمُ بالإقناعِ أو التّأثيرِ من تفصيلةٍ (عددٍ مثلًا) لا من القرائنِ الغالبةِ: مشهدٌ مؤثّرٌ واستفهامٌ ونداءٌ ← تأثيرٌ، ودليلٌ يُتحقَّقُ منه ← إقناعٌ
- **FR** : Tu juges « convaincre » ou « toucher » sur un détail (un chiffre), non sur les indices : scène émouvante, appel → toucher ; preuve vérifiable → convaincre
- **EN** : You decide 'persuade' or 'move' from one detail (a number) not the dominant clues: moving scene, question, appeal → move; checkable proof → persuade
- **Chapitres / piège** : ch09 — piège n°7 « الجوابُ بكلمةٍ بلا تعليلٍ: «الغالبُ التأثيرُ» لا يكفي، والمطلوبُ أن تذكرَ **القرائنَ** من النصِّ (نداءٌ، استفه… » (1ʳᵉ erreur (répondre par un seul mot sans les indices) : aucun distracteur); ch10 — piège n°7 « الجوابُ بكلمةٍ بلا قرائنَ، أو الحكمُ بموضوعِ النصِّ: «التأثيرُ لأنّه يتكلّمُ عن المرضِ». والموضوعُ لا يحدّدُ ا… » (id de ch09 pour le second)
- **Q distinctes** : 4
- **Distracteurs porteurs** :
  - `09:01#6→a` « أسرتانِ في حيِّنا تبيتانِ في العراءِ، فأيُّ قلبٍ يحتملُ هذا المشهدَ ال… » — R1 (paraphrase de l'explication) :  تحرّك الوجدان بمشهد مؤلم … العدد تفصيلة 
  - `09:01#6→b` « تخيّلْ دمعةَ أمٍّ تنتظرُ ابنَها على الرصيفِ، أيّها القارئُ، ألا تتألّم… » — R1 (paraphrase de l'explication) :  تحرّك الوجدان بمشهد مؤلم … العدد تفصيلة 
  - `09:01#6→d` « ما أقسى أن يُحرمَ طفلٌ بريءٌ من لقمتِه، يا لَلشقاءِ والحرمانِ! » — R1 (paraphrase de l'explication) :  تحرّك الوجدان بمشهد مؤلم … العدد تفصيلة 
  - `09:02#5→a` « الإقناعُ، لأنّ فيها رقمًا واضحًا هو «ثلاثةُ أطفالٍ» يخاطبُ العقلَ ويقن… » — R1 (paraphrase de l'explication) :  ليس العدد دليلًا يقنع العقل بل تفصيلة في مشهد مؤثر 
  - `09:02#5→c` « الإقناعُ والتأثيرُ بالتساوي، لأنّ فيها عددًا ونداءً معًا » — R1 (paraphrase de l'explication) :  ليس العدد دليلًا يقنع العقل بل تفصيلة في مشهد مؤثر 
  - `09:02#5→d` « الإقناعُ، لأنّ كلَّ فقرةٍ حجاجيّةٍ تخاطبُ العقلَ وحدَه دونَ الوجدانِ » — R1 (paraphrase de l'explication) :  ليس العدد دليلًا يقنع العقل بل تفصيلة في مشهد مؤثر 
  - `10:03#4→a` « الإقناعُ؛ لأنّه يذكرُ رقمًا هو «4 من كلِّ 10» يخاطبُ عقلَ القارئِ بدلي… » — R1 (paraphrase de l'explication) :  الرقم الواحد قرينة إقناع وحيدة لا تغلب 
  - `10:05#3→a` « التأثيرُ؛ لأنّه يبدأُ بتعجّبٍ مؤثّرٍ من حالِ الطفلِ المتعثّرِ » — R1 : « قرينة تأثير وحيدة لا تغلب »

#### `arabe.hijaj.istidrak-khalt` — NEUF

- **AR** : تخلطُ الاستدراكَ بالتّقابلِ أو بالتّوكيدِ (بيدَ أنّ ≠ بينما، إلّا أنّ ≠ إنّ): الاستدراكُ يأتي بخلافِ ما توحي به الجملةُ الأولى
- **FR** : Tu confonds استدراك, تقابل et توكيد (بيدَ أنّ ≠ بينما، إلّا أنّ ≠ إنّ) : l'استدراك apporte le contraire de ce que la 1ʳᵉ phrase laissait attendre
- **EN** : You confuse استدراك, تقابل and توكيد (بيدَ أنّ ≠ بينما، إلّا أنّ ≠ إنّ): استدراك brings the opposite of what the first clause led you to expect
- **Chapitres / piège** : ch09 — piège n°9 « الخلطُ بينَ الاستدراكِ والتقابلِ لأنّ كليهما يضعُ جملتَينِ في مواجهةٍ. «الغنيُّ يشتري ما يشاءُ بينما الفقيرُ ي… »; ch10 — piège n°5 « الجوابُ باسمِ الأداةِ نحويًّا («حرفٌ») أو بـ«تربطُ بين جملتَينِ»: ليس هذا **المعنى** المطلوبَ؛ المطلوبُ العائل… » (ids de ch09 ; la 1ʳᵉ erreur (nommer l'outil par sa nature grammaticale) n'a aucun distracteur)
- **Q distinctes** : 3
- **Distracteurs porteurs** :
  - `09:quiz#5→d` « التوكيدُ، لأنّ «أنّ» تشدّدُ على الخبرِ » — R1 : « وجود أنّ في آخر الأداة لا يجعلها توكيدًا »
  - `09:02#3→b` « ارتفعتِ الحرارةُ «بيدَ أنّ» الإقبالَ على الشاطئِ ضعيفٌ » — R1 (paraphrase de l'explication) :  بيد أنّ ففيها توقّع نقضه ما بعدها 
  - `10:03#3→a` « الاستدراكُ: ما بعدَه ينقضُ ما يُتوقَّعُ من المطالعةِ » — R1 : « وليست استدراكًا لأنّ ما قبلها لا يُتوقَّع منه عكس ما بعدها »

#### `arabe.hijaj.istifham-hijaji-khalt` — NEUF

- **AR** : تخلطُ بين الاستفهامِ الحجاجيِّ (أيُعقلُ أن نهدرَ الماءَ؟) والسّؤالِ الحقيقيِّ: الحجاجيُّ يدفعُ السّامعَ إلى الإقرارِ ولا يطلبُ معلومةً
- **FR** : Tu confonds la question argumentative (أيُعقلُ أن نهدرَ الماءَ ؟) et la vraie : la première pousse l'auditeur à admettre, elle ne demande pas d'information
- **EN** : You mix up the argumentative question (أيُعقلُ أن نهدرَ الماءَ؟) and the real one: the first drives the listener to concede, it asks for no information
- **Chapitres / piège** : ch09 — piège n°10 « الاكتفاءُ بالصيغِ بدلَ الحجّةِ: «لا ريبَ ولا شكَّ أنّ الرياضةَ ضروريّةٌ، واللهِ!» صيغتانِ وقسمٌ ولا سببَ فيها؛… » (1ʳᵉ erreur (formules à la place de l'argument) : aucun distracteur)
- **Q distinctes** : 1
- **Distracteurs porteurs** :
  - `09:04#6→a` « ما رأيُكم في اقتراحِ الأستاذِ: أنُنظّمُ رحلةً أم نؤجّلُها؟ » — R1 (paraphrase de l'explication) :  الأسئلة الأخرى تطلب جوابًا حقيقيًّا 
  - `09:04#6→c` « هل تظنّونَ أنّ الامتحانَ الأوّلَ سيكونُ صعبًا هذه السنةَ؟ » — R1 (paraphrase de l'explication) :  الأسئلة الأخرى تطلب جوابًا حقيقيًّا 
  - `09:04#6→d` « متى يبدأُ الامتحانُ الأوّلُ، وفي أيِّ قاعةٍ سنجلسُ؟ » — R1 (paraphrase de l'explication) :  الأسئلة الأخرى تطلب جوابًا حقيقيًّا 

#### `arabe.hijaj.istintaj-dakhil-al-sayrura` — NEUF

- **AR** : تضمُّ الاستنتاجَ إلى سيرورةِ الحجاجِ أو تجعلُه أطروحةً ثانيةً: الاستنتاجُ ركنٌ مستقلٌّ يستخلصُ ما قالتْه الحججُ ولا يضيفُ حجّةً جديدةً
- **FR** : Tu ranges la conclusion dans la démarche argumentative ou en fais une 2ᵉ thèse : c'est un élément à part qui tire le bilan des arguments sans en ajouter
- **EN** : You put the conclusion inside the argumentation or make it a second thesis: it is a separate part that sums up the arguments without adding a new one
- **Chapitres / piège** : ch09 — piège n°6 « عدُّ أوّلِ جملةٍ في النصِّ أطروحتَه دائمًا: في هذا النصِّ الجملةُ الأولى هي المدحوضةُ والمثبتةُ جاءتْ بعدَها؛ … » (deux erreurs); ch10 — piège n°1 « جعلُ الجملةِ الأولى «الأطروحةَ» دائمًا. في نصٍّ يبدأُ بـ«يظنُّ بعضُهم أنّ …» تكونُ الجملةُ الأولى الأطروحةَ **… » (deux erreurs)
- **Q distinctes** : 2
- **Distracteurs porteurs** :
  - `09:06#1→b` « الأطروحةُ: (1)؛ سيرورةُ الحجاجِ: من (2) إلى (5)؛ لا استنتاجَ في النصِّ » — R1 : « لا تدخل (5) في السيرورة … ولا تُعدّ (5) أطروحة ثانية »
  - `09:06#1→d` « الأطروحةُ: (1) و(5)؛ سيرورةُ الحجاجِ: من (2) إلى (4)؛ لا استنتاجَ في ا… » — R1 : « لا تدخل (5) في السيرورة … ولا تُعدّ (5) أطروحة ثانية »
  - `10:01#2→c` « من (2) إلى (5) » — R1 : « ولا الجملةُ (5) لأنّها استنتاجٌ يبدأُ بـ«إذن» »

#### `arabe.hijaj.jumla-ula-hiya-al-utruha` — NEUF

- **AR** : تجعلُ الجملةَ الأولى وحدَها الأطروحةَ وتضعُ المثبتةَ التي تليها في السّيرورةِ: في نصِّ الأطروحتَينِ تجتمعُ المدحوضةُ والمثبتةُ في ركنِ الأطروحةِ
- **FR** : Tu fais de la 1ʳᵉ phrase la seule thèse et ranges la thèse défendue suivante dans la démarche : réfutée et défendue sont ensemble dans le 1ᵉʳ pilier
- **EN** : You make the first sentence the only thesis and put the defended one after it in the argumentation: refuted and defended belong together to the first pillar
- **Chapitres / piège** : ch10 — piège n°1 « جعلُ الجملةِ الأولى «الأطروحةَ» دائمًا. في نصٍّ يبدأُ بـ«يظنُّ بعضُهم أنّ …» تكونُ الجملةُ الأولى الأطروحةَ **… » (deux erreurs)
- **Q distinctes** : 1
- **Distracteurs porteurs** :
  - `10:01#5→b` « الأطروحةُ: (1)؛ سيرورةُ الحجاجِ: (2) إلى (4)؛ الاستنتاجُ: (5) » — R1 : « هما معًا في ركنِ الأطروحةِ »

#### `arabe.hijaj.khatima-sardiyya-mansiyya` — NEUF

- **AR** : تنسى الخاتمةَ السّرديّةَ في الحوارِ الحجاجيِّ أو تجعلُها حواريّةً: يُختمُ الحوارُ بجملةٍ سرديّةٍ تبيّنُ مآلَه لا بقولٍ آخرَ
- **FR** : Tu oublies la clôture narrative du dialogue argumentatif ou la rends parlée : il finit par une phrase narrative qui dit l'issue, non par une réplique de plus
- **EN** : You forget the narrative closing of an argumentative dialogue or make it spoken: it ends with a narrative sentence giving the outcome, not a line of speech
- **Chapitres / piège** : ch09 — piège n°12 « تركُ أحدِ الطرفَينِ بلا حججٍ: يقولُ «بل ليلةُ الامتحانِ أنفعُ» ثمّ يسكتُ، فيصيرُ الحوارُ تبادلَ أحكامٍ لا حجاج… » (1ʳᵉ erreur (un des deux camps sans arguments) : aucun distracteur)
- **Q distinctes** : 1
- **Distracteurs porteurs** :
  - `09:02#4→d` « مقدّمةٌ سرديّةٌ ← أطروحةُ الأوّلِ وحججُه ونتيجتُه ← أطروحةُ الثاني وحج… » — R1 : « خاتمة حوارية بدل السردية »

#### `arabe.hijaj.khutta-la-tuwafiq-al-matlub` — NEUF

- **AR** : تختارُ خطّةً لا توافقُ القالبَ المطلوبَ (حوارٌ حجاجيٌّ، فقرةٌ، دحضٌ): لكلِّ قالبٍ أركانُه وترتيبُه، فاعرفِ المطلوبَ قبلَ أن تخطِّطَ
- **FR** : Tu prends un plan qui ne correspond pas au format demandé (dialogue, paragraphe, réfutation) : chaque format a ses parties et son ordre ; lis la demande
- **EN** : You pick a plan that doesn't fit the format asked (dialogue, paragraph, refutation): each format has its own parts and order; identify the request first
- **Chapitres / piège** : ch09 — (pas de piège ; erreur récurrente dans les items)
- **Q distinctes** : 4
- **Distracteurs porteurs** :
  - `09:02#4→a` « أطروحةُ الأوّلِ ← أطروحةُ الثاني ← حججُهما معًا ← نتيجةٌ واحدةٌ ← خاتم… » — R1 (paraphrase de l'explication) :  غياب المقدمة وتداخل الأطروحتين / غياب الربط 
  - `09:02#4→b` « مقدّمةٌ سرديّةٌ ← أطروحةُ الأوّلِ وحججُه ← أطروحةُ الثاني وحججُه ← نتي… » — R1 (paraphrase de l'explication) :  غياب المقدمة وتداخل الأطروحتين / غياب الربط 
  - `09:05#5→a` « مقدّمةٌ سرديّةٌ عن يومِ تلميذٍ، ثمّ حوارٌ بينَ شخصَينِ، ثمّ خاتمةٌ سرد… » — R1 : « قالب الحوار الحجاجي المؤطَّر لا الفقرة »
  - `09:06#5→a` « الروحُ الرياضيّةُ أهمُّ من الفوزِ لأنّها تبني الأخلاقَ، وقد قلتُ ذلكَ … » — R1 : « تلخيص … أو وصف مطوَّل بلا حدث ولا شخصيات »
  - `09:06#5→c` « كانتْ ساحةُ المعهدِ واسعةً، أرضُها خضراءُ وأشجارُها عاليةٌ ومقاعدُها خ… » — R1 : « تلخيص … أو وصف مطوَّل بلا حدث ولا شخصيات »
  - `09:06#6→a` « مقدّمةٌ تعرضُ اعتقادَه ← حججٌ تؤيّدُه بأمثلتِها ← أطروحةٌ مثبتةٌ هي رأ… » — R1
  - `09:06#6→d` « مقدّمةٌ سرديّةٌ عن يومِ الامتحانِ ← وصفٌ مطوَّلٌ لقاعةِ الدرسِ ← خاتمة… » — R1

#### `arabe.hijaj.ma3ayir-taqyim-khati2a` — NEUF

- **AR** : تقيّمُ الحجاجَ بمعيارٍ خاطئٍ: المثالُ الشّخصيُّ ليس واجبًا، والاعتراضُ مع ردِّه يقوّي، والتّنوّعُ وحدَه لا يكفي، والرّقمُ الكبيرُ لا يغني عن الصّلةِ
- **FR** : Tu évalues avec un faux critère : exemple personnel non requis, objection + réponse renforce, variété seule insuffisante, gros chiffre sans lien inutile
- **EN** : You assess with a wrong criterion: personal example not required, objection + answer strengthens, variety alone insufficient, big unrelated figure useless
- **Chapitres / piège** : ch10 — (pas de piège ; erreur récurrente dans les items)
- **Q distinctes** : 3
- **Distracteurs porteurs** :
  - `10:03#5→a` « وُفِّقَ؛ لأنّ التجربةَ الشخصيّةَ أقوى الأدلّةِ وأصدقُها، ولا حاجةَ إلى… » — R1
  - `10:05#6→a` « لم يُوفَّقْ؛ لأنّه لم يذكرْ مثالًا من تجربتِه الشخصيّةِ في الموضوعِ » — R1
  - `10:05#6→c` « لم يُوفَّقْ؛ لأنّه ذكرَ اعتراضَ المخالفِ، وذكرُ الاعتراضِ يُضعفُ الأطر… » — R1
  - `10:06#6→b` « وُفِّقَ؛ لأنّ حجّتَيه متنوّعتانِ، والتنوّعُ وحدَه يكفي للإقناعِ » — R1 (paraphrase de l'explication) :  التنوّع وحده لا يكفي … كبر النسبة لا يغني 
  - `10:06#6→d` « وُفِّقَ؛ لأنّ نسبةَ 80% كبيرةٌ، والأرقامُ الكبيرةُ تُقنعُ دائمًا » — R1 (paraphrase de l'explication) :  التنوّع وحده لا يكفي … كبر النسبة لا يغني 

#### `arabe.hijaj.mahdhuda-bi-lisan-al-katib` — NEUF

- **AR** : تصوغُ الأطروحةَ المدحوضةَ بلسانِ الكاتبِ (رأيِه المثبتِ أو رأيِه بصيغةِ النّفيِ): هي رأيُ الخصمِ بلفظِه الموجَبِ، كـ«الفصحى لغةُ الكتبِ وحدَها»
- **FR** : Tu formules la thèse réfutée avec les mots de l'auteur (son avis ou sa négation) : c'est l'avis de l'adversaire en positif : « الفصحى لغةُ الكتبِ وحدَها »
- **EN** : You phrase the refuted thesis in the author's words (his view or its negation): it is the opponent's view in positive form: « الفصحى لغةُ الكتبِ وحدَها »
- **Chapitres / piège** : ch10 — piège n°2 « صوغُ المدحوضةِ بلسانِ الكاتبِ: يجيبُ تلميذٌ عن «الأطروحةِ التي يدحضُها الكاتبُ» بـ«التطوّعُ في متناولِ الجميعِ… » (deux erreurs)
- **Q distinctes** : 4
- **Distracteurs porteurs** :
  - `10:quiz#2→b` « الحوارُ مع الأبناءِ يقوّي الثقةَ بين أفرادِ الأسرةِ » — R1 : « رأيُ الكاتبِ نفسِه بصيغةِ النفيِ لا ما يدحضُه »
  - `10:quiz#2→d` « الحوارُ مع الأبناءِ لا يُضعفُ هيبةَ الأسرةِ » — R1 : « رأيُ الكاتبِ نفسِه بصيغةِ النفيِ لا ما يدحضُه »
  - `10:01#4→a` « الفصحى ليستْ لغةَ الكتبِ وحدَها » — R1 : « رأيُ الكاتبِ نفسِه بصيغةِ النفيِ »
  - `10:04#6→a` « لا تكفي الشهادةُ لإيجادِ عملٍ » — R1 : « رأي الكاتب نفسه بصيغة النفي »
  - `10:06#2→a` « الغشُّ عجزٌ عن الفهمِ وليس ذكاءً » — R1 : « رأيُ الكاتبِ المثبتُ لا المدحوضُ »

#### `arabe.hijaj.mahdhuda-bila-badila` — NEUF

- **AR** : تدحضُ الأطروحةَ ولا تقيمُ أطروحةً بديلةً: الدّحضُ وحدَه هدمٌ بلا بناءٍ؛ المدحوضةُ ثمّ حججٌ داحضةٌ ثمّ بديلةٌ بحجّتِها ثمّ استنتاجٌ
- **FR** : Tu réfutes la thèse sans en poser une de remplacement : réfuter seul, c'est démolir sans bâtir ; thèse réfutée, arguments, thèse de remplacement, conclusion
- **EN** : You refute the thesis without a replacement: refuting alone demolishes without building; refuted thesis, arguments, replacement thesis, conclusion
- **Chapitres / piège** : ch09 — piège n°13 « السخريةُ بدلَ الحجّةِ: «كلامُكَ ساذجٌ» ليس حجّةً داحضةً؛ الدحضُ يكونُ بدليلٍ يهدمُ الرأيَ لا بتجريحِ صاحبِه. و… » (trois erreurs ; les deux premières partagent un id)
- **Q distinctes** : 1
- **Distracteurs porteurs** :
  - `09:06#6→b` « حججٌ داحضةٌ بأمثلتِها ← استنتاجٌ بمؤشّرٍ، دونَ عرضِ اعتقادِه ولا أطروح… » — R1 (paraphrase de l'explication) :  دحض لا يعرض المدحوضة ولا يقيم بديلة 

#### `arabe.hijaj.mahdhuda-muthbata-khalt` — NEUF

- **AR** : تخلطُ بين الأطروحةِ المدحوضةِ (رأيُ الخصمِ الذي يُردُّ) والمثبتةِ (رأيُ الكاتبِ الذي يدافعُ عنه): ابحثْ عن «بل» و«والحقُّ أنّ» و«ليس»
- **FR** : Tu confonds la thèse réfutée (avis de l'adversaire, rejeté) et la thèse défendue (avis de l'auteur) : cherche « بل »، « والحقُّ أنّ »، « ليس »
- **EN** : You mix up the refuted thesis (the opponent's view, rejected) and the defended one (the author's): look for « بل »، « والحقُّ أنّ »، « ليس »
- **Chapitres / piège** : ch09, ch10 — (pas de piège ; erreur récurrente dans les items)
- **Q distinctes** : 5
- **Distracteurs porteurs** :
  - `09:quiz#2→a` « الرأيُ الذي يدافعُ عنه المُحاجُّ ويقيمُ عليه الأدلّةَ »
  - `09:04#3→a` « الشجاعةُ هي أن تزنَ الأمرَ ثمّ تثبتَ » — R1 (paraphrase de l'explication) :  أن تزن الأمر ثمّ تثبت هي المثبتة 
  - `10:01#3→a` « التضامنُ مع الفقراءِ مسؤوليّةُ الدولةِ وحدَها » — R1 : « فهي الأطروحةُ المدحوضةُ »
  - `10:01#4→c` « الفصحى لغةٌ تصلحُ للحياةِ اليوميّةِ » — R1 : « أطروحتُه المثبتةُ »
  - `10:04#6→c` « المهارةُ شرطٌ لإيجادِ العملِ » — R1 : « أطروحته المثبتة »

#### `arabe.hijaj.mithal-hujja-kafiya` — NEUF

- **AR** : تعدُّ المثالَ (واقعةً بعينِها: زميلي، جاري) حجّةً كافيةً: المثالُ يوضّحُ الحجّةَ ولا يغني عنها؛ فالحجّةُ سببٌ عامٌّ وقد تكونُ الواقعةُ استثناءً
- **FR** : Tu prends un exemple (cas précis : mon voisin) pour un argument suffisant : il illustre l'argument, qui est une raison générale, sans le remplacer
- **EN** : You treat an example (one case: my neighbour) as a sufficient argument: it illustrates the argument, a general reason, but cannot replace it
- **Chapitres / piège** : ch09 — piège n°3 « عدُّ إعادةِ الأطروحةِ حجّةً: «يجبُ أن نقرأَ لأنّ القراءةَ واجبةٌ» لا تضيفُ سببًا بل تكرّرُ الرأيَ بألفاظٍ أخرى… » (deux erreurs); ch10 — piège n°3 « عدُّ المثالِ حجّةً: «لاحظْنا في شارعِ المعهدِ …» واقعةٌ واحدةٌ قد تكونُ استثناءً، فلا تُقنعُ وحدَها؛ ولذلك يطل… » (deux erreurs (ids de ch09))
- **Q distinctes** : 8
- **Distracteurs porteurs** :
  - `09:quiz#3→c` « حجّةٌ: سببٌ عامٌّ يُسندُ الرأيَ ويدعمُه » — R1 (paraphrase de l'explication) :  تذكر واقعة عن شخص بعينه … فهي مثال 
  - `09:01#2→b` « قرأَ زميلي كتابًا كلَّ أسبوعٍ فصارَ أبرعَ تلاميذِ القسمِ إنشاءً » — R1 : « واقعة بعينها تصلح مثالًا »
  - `10:quiz#4→c` « ترجمتْ لي الآلةُ جملةً فصارَ معناها عكسَ المقصودِ »
  - `10:02#1→a` « زرتُ مكتبةَ معهدٍ مجاورٍ فرأيتُ التلاميذَ يتبادلونَ الكتبَ في هدوءٍ » — R1 : « واقعة بعينها فهي مثال »
  - `10:04#4→c` « أنجزْنا في أسبوعٍ ما كانَ يُنجزُه فردٌ في شهرٍ » — R1 : « واقعة بعينها … مثال »
  - `10:05#2→d` « الجارةُ الصغيرةُ تُطعمُ قطّتَها كلَّ صباحٍ » — R1 : « واقعة بعينها فهي مثال لا حجة »
  - `10:06#1→a` « الأطروحةُ (1)؛ سيرورةُ الحجاجِ: أربعُ حججٍ (2) و(3) و(4) و(5) دونَ مثا… » — R1 : « من عدّ (3) حجّة جعل الحجج أربعًا »
  - `11:quiz#7→b` « فقد نقل العربُ علومَ اليونان وطوّروها ثمّ نقلتها أوروبا عنهم » — R1 : « وقائع جزئية … أمثلة تخدم الحجّة لا حججٌ بذاتها »
  - `11:quiz#7→c` « تأمّل كيف انتشرت المأكولاتُ الآسيويّة في مدن العالم كلّها » — R1 : « وقائع جزئية … أمثلة تخدم الحجّة لا حججٌ بذاتها »
  - `11:quiz#7→d` « ها هو متحفُ اللوفر يجمع تحفًا من كلّ الحضارات » — R1 : « وقائع جزئية … أمثلة تخدم الحجّة لا حججٌ بذاتها »

#### `arabe.hijaj.mu2ashshir-ghayr-munasib` — NEUF

- **AR** : تختارُ مؤشّرًا لا يوافقُ العلاقةَ المطلوبةَ: نتيجةٌ ← بناءً على ذلك، إذن؛ استدراكٌ ← بيدَ أنّ؛ تقابلٌ ← على العكسِ؛ تفسيرٌ ← معنى ذلك
- **FR** : Tu prends un connecteur qui ne va pas à la relation : conclusion → بناءً على ذلك ; استدراك → بيدَ أنّ ; contraste → على العكسِ ; reformulation → معنى ذلك
- **EN** : You pick a connector that doesn't fit the relation: conclusion → بناءً على ذلك، إذن; استدراك → بيدَ أنّ; contrast → على العكسِ; rewording → معنى ذلك
- **Chapitres / piège** : ch09, ch10, ch11 — (pas de piège ; erreur récurrente dans les items)
- **Q distinctes** : 13
- **Distracteurs porteurs** :
  - `09:quiz#5→a` « الاستنتاجُ، لأنّ ما بعدَه نتيجةٌ تُستخلصُ ممّا قبلَه وتختمُ الكلامَ »
  - `09:quiz#5→c` « التعليلُ، لأنّ ما بعدَه يبيّنُ سببَ ما قبلَه »
  - `09:01#5→c` « التوكيدُ، فهو يشدّدُ على الخبرِ ويقوّيه »
  - `09:01#5→d` « الاستنتاجُ، فما بعدَه نتيجةٌ لما قبلَه »
  - `09:02#3→c` « تراكمتِ الأدلّةُ «إذن» لا مجالَ للشكِّ في صحّةِ الرأيِ »
  - `09:02#3→d` « لا تُسرفْ في استعمالِ الماءِ «لأنّه» ثروةٌ محدودةٌ »
  - `09:05#2→a` « «ليستْ» تعلّلُ الرأيَ بسببٍ، و«إنّ» تفسّرُ معناه بعبارةٍ أوضحَ منه وأب… »
  - `09:05#2→d` « «ليستْ» و«إنّ» كلتاهما تستدركُ على جملةٍ سابقةٍ بما يخالفُ المتوقَّعَ »
  - `09:05#3→a` « بيدَ أنّ » — R1 : بيد أنّ = استدراك، على العكس = تقابل، معنى ذلك = تفسير
  - `09:05#3→b` « على العكسِ من ذلكَ » — R1 : بيد أنّ = استدراك، على العكس = تقابل، معنى ذلك = تفسير
  - `09:05#3→c` « معنى ذلكَ » — R1 : بيد أنّ = استدراك، على العكس = تقابل، معنى ذلك = تفسير
  - `09:06#2→d` « حجّةٌ واقعيّةٌ، والمؤشّرُ للاستنتاجِ »
  - `10:quiz#6→a` « التعليلُ: ما بعدَه سببٌ لذمِّ الإسرافِ » — R1
  - `10:quiz#6→c` « الاستنتاجُ: ما بعدَه نتيجةٌ لذمِّ الإسرافِ » — R1
  - `10:quiz#6→d` « التفسيرُ: ما بعدَه شرحٌ لمعنى الإسرافِ » — R1
  - `10:03#3→b` « التعليلُ: ما بعدَه سببٌ لمطالعةِ المجتهدِ »
  - `10:03#3→c` « الاستنتاجُ: ما بعدَه نتيجةٌ لمطالعةِ المجتهدِ »
  - `10:04#1→b` « الاستنتاجُ: ما بعدَها نتيجةٌ للتواصلِ مع العالمِ »
  - `10:04#1→d` « الاستدراكُ: ما بعدَها يخالفُ المتوقَّعَ من التواصلِ »
  - `10:05#4→a` « رقميّةٌ؛ والمؤشّرُ للتعليلِ »
  - `11:quiz#6→b` « تعليلٌ يُبيّن سبب تسارع التحوّلات » — R1 : « ليست تعليلًا … ولا نتيجة … ولا إضافة »
  - `11:quiz#6→c` « نتيجةٌ مترتّبة على التسارع » — R1 : « ليست تعليلًا … ولا نتيجة … ولا إضافة »
  - `11:quiz#6→d` « إضافةٌ لمعلومةٍ في الاتّجاه نفسه » — R1 : « ليست تعليلًا … ولا نتيجة … ولا إضافة »
  - `11:02#2→b` « تعليلٌ يُبيّن سبب الأزمات » — R1 : « ليست تعليلًا ولا نتيجة ولا تمثيلًا »
  - `11:02#2→c` « نتيجةٌ مترتّبة على الأزمات » — R1 : « ليست تعليلًا ولا نتيجة ولا تمثيلًا »
  - `11:02#2→d` « تمثيلٌ وتوضيحٌ بالأمثلة » — R1 : « ليست تعليلًا ولا نتيجة ولا تمثيلًا »
  - `11:03#6→b` « لأنّ / إذ » — R1 (paraphrase de l'explication) :  لأنّ رابطُ تعليل، نتيجةً لذلك رابطُ نتيجة، علاوةً رابطُ إضافة 
  - `11:03#6→c` « نتيجةً لذلك / ومن ثمّ » — R1 (paraphrase de l'explication) :  لأنّ رابطُ تعليل، نتيجةً لذلك رابطُ نتيجة، علاوةً رابطُ إضافة 
  - `11:03#6→d` « علاوةً على ذلك / كذلك » — R1 (paraphrase de l'explication) :  لأنّ رابطُ تعليل، نتيجةً لذلك رابطُ نتيجة، علاوةً رابطُ إضافة 

#### `arabe.hijaj.naw3-al-hujja-khalt` — NEUF

- **AR** : تُخطئُ في نوعِ الحجّةِ: سلطةٌ (قولُ مختصٍّ)، أو عقليّةٌ (استدلالٌ بلا مرجعٍ)، أو تاريخيّةٌ، أو واقعيّةٌ؛ اسألْ: من أين تستمدُّ الحجّةُ قوّتَها؟
- **FR** : Tu te trompes de type d'argument : autorité (parole d'un expert), raison (déduction sans source), historique ou factuel ; demande d'où l'argument tire sa force
- **EN** : You misname the argument type: authority (an expert's word), reasoning (deduction with no source), historical or factual; ask where the argument draws its force
- **Chapitres / piège** : ch09, ch10 — (pas de piège ; erreur récurrente dans les items)
- **Q distinctes** : 11
- **Distracteurs porteurs** :
  - `09:quiz#4→d` « حجّةٌ عقليّةٌ منطقيّةٌ، لأنّها استدلالٌ دونَ مرجعٍ »
  - `09:01#4→c` « سلطةٌ، لأنّها تستندُ إلى حكمِ مرجعٍ مختصٍّ »
  - `09:01#4→d` « عقليّةٌ منطقيّةٌ، لأنّها استدلالٌ بالعقلِ من مقدّماتٍ »
  - `09:04#1→b` « سلطةٌ، لأنّها تستندُ إلى قولِ مرجعٍ موثوقٍ »
  - `09:04#1→c` « عقليّةٌ منطقيّةٌ، لأنّها استنتاجٌ من مقدّمتَينِ »
  - `09:04#2→d` « هو حجّةٌ عقليّةٌ منطقيّةٌ، لأنّه يعبّرُ عن حكمةٍ عامّةٍ »
  - `10:quiz#5→c` « حجّةٌ رقميّةٌ » — R1 : « لا تذكر عددًا ولا نسبةً »
  - `10:02#3→c` « أحمد »
  - `10:02#3→d` « نادية »
  - `10:02#5→a` « سلطةٌ؛ لأنّها تبدأُ بحكمٍ عامٍّ يسلّمُ به الجميعُ دونَ نقاشٍ » — R1 : « ليست سلطة … ولا واقعية … ولا رقمية »
  - `10:02#5→b` « واقعيّةٌ؛ لأنّها تصفُ ما يحدثُ للمدينةِ حينَ يمشي أهلُها » — R1 : « ليست سلطة … ولا واقعية … ولا رقمية »
  - `10:02#5→c` « رقميّةٌ؛ لأنّها تقارنُ بين فوائدِ المشيِ وفوائدِ غيرِه » — R1 : « ليست سلطة … ولا واقعية … ولا رقمية »
  - `10:02#6→a` « سلطةٌ بقرينةِ «ملتقى التجّارِ»، وواقعيّةٌ بقرينةِ «لاحظتُ» »
  - `10:02#6→c` « تاريخيّةٌ بقرينةِ «قديمًا»، ورقميّةٌ بقرينةِ «الباعةَ الصغارَ» »
  - `10:04#3→a` « رقميّةٌ بقرينةِ «قالَ أحدُ علماءِ النفسِ»، وسلطةٌ بقرينةِ «8 من كلِّ 1… » — R1
  - `10:04#3→b` « سلطةٌ بقرينةِ «قالَ أحدُ علماءِ النفسِ»، وتاريخيّةٌ بقرينةِ «ساعةِ لعب… » — R1
  - `10:04#3→c` « تاريخيّةٌ بقرينةِ «غذاءُ نموِّ الطفلِ»، ورقميّةٌ بقرينةِ «8 من كلِّ 10… » — R1
  - `10:05#4→b` « عقليّةٌ منطقيّةٌ؛ والمؤشّرُ للاستنتاجِ » — R1
  - `10:05#4→c` « تاريخيّةٌ؛ والمؤشّرُ للتفسيرِ » — R1
  - `10:06#4→a` « رقميّةٌ بقرينةِ «1969»، وسلطةٌ بقرينةِ «كلُّ ما يحلُّ مشكلاتِ الناسِ» » — R1
  - `10:06#4→c` « تاريخيّةٌ بقرينةِ «سنةَ 1969»، وسلطةٌ بقرينةِ «كلُّ ما يحلُّ مشكلاتِ ا… » — R1

#### `arabe.hijaj.shahid-naw3-mustaqill` — NEUF

- **AR** : تعدُّ الشّاهدَ (بيتًا أو آيةً أو مثلًا) نوعًا مستقلًّا من الحججِ: الشّاهدُ صورةٌ من حجّةِ السّلطةِ لأنّ قوّتَه من قائلِه
- **FR** : Tu fais du témoin (vers, verset, proverbe) un type d'argument à part : c'est une forme de l'argument d'autorité, car sa force vient de celui qui parle
- **EN** : You treat a quoted line (verse, scripture, proverb) as a separate argument type: it is a form of authority argument, its force coming from its speaker
- **Chapitres / piège** : ch09 — piège n°4 « الخلطُ بينَ الحجّةِ **التاريخيّةِ** والحجّةِ **الواقعيّةِ** لأنّ كلتَيهما «واقعةٌ». المعيارُ زمنُ الواقعةِ ومص… » (deux erreurs)
- **Q distinctes** : 1
- **Distracteurs porteurs** :
  - `09:04#2→c` « هو نوعٌ مستقلٌّ من الحججِ لا يدخلُ في الأنواعِ الخمسةِ » — R1 (paraphrase de l'explication) :  الشاهد صورة من حجة السلطة لا نوع سادس 

#### `arabe.hijaj.sigha-ghayr-amina` — NEUF

- **AR** : تصوغُ الأطروحةَ بغيرِ أمانةٍ: تغيّرُ المدى (كلُّ، كثيرٌ، قليلٌ، وحدَهم)، أو تضيفُ ما لم يقلْه الكاتبُ، أو تحوّلُ حجّةً إلى رأيٍ
- **FR** : Tu reformules la thèse sans fidélité : tu changes sa portée (كلُّ، كثيرٌ، قليلٌ، وحدَهم), ajoutes ce que l'auteur n'a pas dit ou prends un argument pour l'avis
- **EN** : You reword the thesis unfaithfully: you change its scope (كلُّ، كثيرٌ، قليلٌ، وحدَهم), add what the author never said, or take an argument for the opinion
- **Chapitres / piège** : ch10 — piège n°2 « صوغُ المدحوضةِ بلسانِ الكاتبِ: يجيبُ تلميذٌ عن «الأطروحةِ التي يدحضُها الكاتبُ» بـ«التطوّعُ في متناولِ الجميعِ… » (deux erreurs)
- **Q distinctes** : 5
- **Distracteurs porteurs** :
  - `10:01#3→c` « التضامنُ مع الفقراءِ واجبٌ على الأغنياءِ وحدَهم » — R1 : « تغييرٌ لمدى الرأي »
  - `10:01#4→d` « الفصحى لغةٌ صعبةٌ لا يتقنُها إلّا المتخصّصونَ » — R1 : « بما لم يقلْه الخصمُ »
  - `10:03#1→a` « التبرّعُ بالدمِ يُنقذُ ثلاثةَ مرضى في كلِّ مرّةٍ » — R1 (paraphrase de l'explication) :  تحويل قد يُنقذ إلى جزم … لم يقلْه النص 
  - `10:03#1→b` « الأطبّاءُ يشجّعونَ على التبرّعِ بالدمِ » — R1 (paraphrase de l'explication) :  تحويل قد يُنقذ إلى جزم … لم يقلْه النص 
  - `10:04#5→a` « كلُّ الشبابِ يقرؤونَ ما يفيدُهم ويحتاجونَ إلى من يرشدُهم » — R1 : « تغيير المدى إلى كلّ … إلى قليل »
  - `10:04#5→b` « كلُّ الشبابِ لا يقرؤونَ شيئًا ممّا يفيدُهم » — R1 : « تغيير المدى إلى كلّ … إلى قليل »
  - `10:04#5→d` « قليلٌ من الشبابِ يقرؤونَ ما يفيدُهم ويحتاجونَ إلى من يرشدُهم » — R1 : « تغيير المدى إلى كلّ … إلى قليل »
  - `10:04#6→b` « الشهادةُ لا قيمةَ لها في سوقِ العملِ » — R1 : « مبالغة لم يقلها »

#### `arabe.hijaj.ta3lil-tafsir-khalt` — NEUF

- **AR** : تخلطُ بين التّعليلِ والتّفسيرِ: التّعليلُ يجيبُ عن «لماذا؟» بسببٍ (لأنّ، كي، فإنّ)، والتّفسيرُ عن «ماذا يعني؟» بعبارةٍ أوضحَ (أي، معنى ذلك)
- **FR** : Tu confonds التّعليل (« pourquoi ? » : une cause — لأنّ، كي، فإنّ) et التّفسير (« que veut dire ? » : une paraphrase — أي، معنى ذلك)
- **EN** : You confuse التّعليل (answers 'why?' with a cause — لأنّ، كي، فإنّ) and التّفسير (answers 'what does it mean?' with a rewording — أي، معنى ذلك)
- **Chapitres / piège** : ch09 — piège n°8 « الخلطُ بينَ التعليلِ والتفسيرِ لأنّ كلًّا منهما يأتي بعدَ جملةٍ ويتعلّقُ بها. الفرقُ في السؤالِ: التعليلُ يجيب… »; ch10 — piège n°5 « الجوابُ باسمِ الأداةِ نحويًّا («حرفٌ») أو بـ«تربطُ بين جملتَينِ»: ليس هذا **المعنى** المطلوبَ؛ المطلوبُ العائل… » (ids de ch09 ; la 1ʳᵉ erreur (nommer l'outil par sa nature grammaticale) n'a aucun distracteur)
- **Q distinctes** : 4
- **Distracteurs porteurs** :
  - `09:01#5→b` « التفسيرُ، فما بعدَه إعادةٌ لمعنى ما قبلَه بعبارةٍ أوضحَ »
  - `09:04#5→a` « نقتصدُ في استعمالِ الماءِ «لأنّه» ثروةٌ محدودةٌ » — R1 : لأنّ/كي/فإنّ = تعليل
  - `09:04#5→b` « ادّخرْ شيئًا من مصروفِكَ «كي» تواجهَ المصاريفَ الطارئةَ » — R1 : لأنّ/كي/فإنّ = تعليل
  - `09:04#5→d` « لا تُسرفْ في استعمالِ الماءِ «فإنّ» الإسرافَ يُفقرُ صاحبَه » — R1 : لأنّ/كي/فإنّ = تعليل
  - `09:06#2→c` « حجّةُ سلطةٍ، والمؤشّرُ للتعليلِ » — R1 : « ليست تعليلًا لأنها لا تذكر سببًا »
  - `10:04#1→a` « التعليلُ: ما بعدَها سببٌ لتعلّمِ اللغةِ الثانيةِ » — R1 : « أداته هنا كي لا أي »

#### `arabe.hijaj.tadarruj-wa-rawabit-khalt` — NEUF

- **AR** : لا ترى تدرّجَ الحججِ ولا الرّوابطَ بينها (والأهمُّ من ذلك، إذن)، فتعدُّها عشوائيّةً أو تكرارًا: السّيرورةُ مسارٌ يقودُ القارئَ لا أفكارٌ متراصّةٌ
- **FR** : Tu ne vois ni la progression des arguments ni leurs liens (والأهمُّ من ذلك، إذن) et les crois en désordre ou répétés : c'est un parcours, pas un tas d'idées
- **EN** : You miss the progression of arguments and their links (والأهمُّ من ذلك، إذن) and call them random or repeated: a process is a path, not a pile of ideas
- **Chapitres / piège** : ch09 — piège n°5 « تكديسُ الجملِ بلا حجّةٍ: «الغاباتُ جميلةٌ، والغاباتُ لطيفةٌ، والغاباتُ تسرُّ العينَ» ثلاثُ جملٍ ولا سببَ فيها … » (1ʳᵉ erreur (empiler des phrases sans argument) : aucun distracteur ; la 2ᵉ (liens supprimés) n'est portée que par des contre-sens de lecture)
- **Q distinctes** : 1
- **Distracteurs porteurs** :
  - `09:02#1→a` « ترتيبٌ تنازليٌّ من الأقوى إلى الأضعفِ، لأنّ أوّلَ الحججِ هي أقواها » — R1 (paraphrase de l'explication) :  والأهم من ذلك وإذن تصلان بين الحلقات … كل حجة سببًا مختلفًا 
  - `09:02#1→c` « ترتيبٌ عشوائيٌّ، لأنّ الحججَ لا يصلُ بينَها رابطٌ » — R1 (paraphrase de l'explication) :  والأهم من ذلك وإذن تصلان بين الحلقات … كل حجة سببًا مختلفًا 
  - `09:02#1→d` « تكرارٌ لحجّةٍ واحدةٍ بألفاظٍ مختلفةٍ، لأنّ الحججَ الثلاثَ فكرةٌ واحدةٌ » — R1 (paraphrase de l'explication) :  والأهم من ذلك وإذن تصلان بين الحلقات … كل حجة سببًا مختلفًا 

#### `arabe.hijaj.taqsim-al-binya-khalt` — NEUF

- **AR** : تقسّمُ النّصَّ خطأً إلى أطروحةٍ وسيرورةٍ واستنتاجٍ: الأطروحةُ رأيٌ (مدحوضةٌ ومثبتةٌ معًا إن وُجدتا)، والسّيرورةُ حججٌ وأمثلةٌ، والاستنتاجُ ختامٌ
- **FR** : Tu découpes mal thèse, démarche, conclusion : la thèse est un avis (réfutée + défendue si deux), la démarche = arguments et exemples, la conclusion clôt
- **EN** : You split thesis, argumentation and conclusion wrongly: thesis = opinion (refuted + defended if two), argumentation = arguments and examples, conclusion closes
- **Chapitres / piège** : ch10 — (pas de piège ; erreur récurrente dans les items)
- **Q distinctes** : 4
- **Distracteurs porteurs** :
  - `10:01#5→c` « الأطروحةُ: (2)؛ سيرورةُ الحجاجِ: (3) إلى (5)؛ الاستنتاجُ: غائبٌ »
  - `10:01#5→d` « الأطروحةُ: (1) إلى (3)؛ سيرورةُ الحجاجِ: (4)؛ الاستنتاجُ: (5) »
  - `10:01#6→a` « الأطروحةُ؛ لأنّ الجملةَ الأولى لا تقولُ رأيًا يمكنُ الدفاعُ عنه » — R1
  - `10:01#6→b` « سيرورةُ الحجاجِ؛ لأنّ النصَّ لا يذكرُ مثالًا يوضّحُ الحجّةَ » — R1
  - `10:01#6→d` « الأطروحةُ المدحوضةُ؛ لأنّ الكاتبَ لم يعرضْ رأيَ خصمِه » — R1
  - `10:05#1→b` « الأطروحةُ: (1) و(2)؛ سيرورةُ الحجاجِ: (3) و(4)؛ الاستنتاجُ: (5) » — R1 : « من ضمّ (2) إلى الأطروحة … جعل (4) استنتاجًا … ضمّ (5) إلى السيرورة »
  - `10:05#1→c` « الأطروحةُ: (1)؛ سيرورةُ الحجاجِ: (2) و(3)؛ الاستنتاجُ: (4) و(5) » — R1 : « من ضمّ (2) إلى الأطروحة … جعل (4) استنتاجًا … ضمّ (5) إلى السيرورة »
  - `10:05#1→d` « الأطروحةُ: (1)؛ سيرورةُ الحجاجِ: (2) إلى (5)؛ الاستنتاجُ: غائبٌ » — R1 : « من ضمّ (2) إلى الأطروحة … جعل (4) استنتاجًا … ضمّ (5) إلى السيرورة »
  - `10:06#1→c` « الأطروحةُ (1)؛ سيرورةُ الحجاجِ: حجّتانِ (2) و(4) ومثالانِ (3) و(5)؛ ال… »
  - `10:06#1→d` « الأطروحةُ (1) و(2)؛ سيرورةُ الحجاجِ: حجّتانِ (4) و(5) ومثالٌ (3)؛ الاس… »

#### `arabe.hijaj.tarikhi-waqi3i-khalt` — NEUF

- **AR** : تخلطُ بين الحجّةِ التّاريخيّةِ (حدثٌ مؤرَّخٌ من الماضي) والواقعيّةِ (ما نشاهدُه أو نجرّبُه): صيغةُ الماضي في «قالَ» لا تجعلُها تاريخيّةً
- **FR** : Tu confonds l'argument historique (événement daté du passé) et le réel (ce qu'on voit ou vit) : le passé de « قالَ » ne rend pas un argument historique
- **EN** : You confuse the historical argument (a dated past event) with the factual one (what we see or experience): the past tense of « قالَ » doesn't make it historical
- **Chapitres / piège** : ch09 — piège n°4 « الخلطُ بينَ الحجّةِ **التاريخيّةِ** والحجّةِ **الواقعيّةِ** لأنّ كلتَيهما «واقعةٌ». المعيارُ زمنُ الواقعةِ ومص… » (deux erreurs); ch10 — piège n°4 « الخلطُ بين **التاريخيّةِ** و**الواقعيّةِ** لأنّ كلتَيهما «واقعةٌ»: «في سنةِ 1875 أُسّستِ المدرسةُ الصادقيّةُ» … » (id de ch09 ; la 2ᵉ erreur (le شاهد comme type à part) n'a aucun distracteur ici)
- **Q distinctes** : 10
- **Distracteurs porteurs** :
  - `09:quiz#4→a` « حجّةٌ تاريخيّةٌ، لأنّ الطبيبَ قالَ ذلكَ في الماضي » — R1 : « صيغة الماضي في قال لا تجعله تاريخًا »
  - `09:quiz#4→b` « حجّةٌ واقعيّةٌ، لأنّ التلميذَ يرويها عن مشاهدةٍ » — R1 : « صيغة الماضي في قال لا تجعله تاريخًا »
  - `09:01#4→a` « تاريخيّةٌ، لأنّها وقعتْ في الماضي وانتهتْ » — R1
  - `09:04#1→a` « واقعيّةٌ، لأنّها مشاهدةٌ يرويها المتكلّمُ بنفسِه » — R1
  - `09:04#2→b` « هو حجّةٌ تاريخيّةٌ، لأنّ المتنبّي شاعرٌ عاشَ في عصرٍ مضى وانقضى » — R1 : « ليس تاريخيًّا لأنه لا يعرض حدثًا مؤرَّخًا بل قولًا »
  - `09:06#2→b` « حجّةٌ واقعيّةٌ، والمؤشّرُ للتفسيرِ » — R1 : « لا مشاهدة فيها ولا تجربة »
  - `10:quiz#5→a` « حجّةٌ تاريخيّةٌ » — R1
  - `10:quiz#5→b` « حجّةٌ واقعيّةٌ » — R1
  - `10:02#3→b` « ليلى » — R1 : « حجّة ليلى واقعيّة »
  - `10:02#4→b` « تاريخيّةٌ؛ وقرينتُها «العامَ الماضيَ» » — R1 (paraphrase de l'explication) :  لا تدلّ العامَ الماضيَ على التاريخيّة 
  - `10:02#4→d` « تاريخيّةٌ؛ وقرينتُها «رأيتُ بنفسي» » — R1 (paraphrase de l'explication) :  لا تدلّ العامَ الماضيَ على التاريخيّة 
  - `10:02#6→d` « واقعيّةٌ بقرينةِ «قديمًا»، وتاريخيّةٌ بقرينةِ «لاحظتُ» » — R1 : « من عكس النوعين جعل الماضي مشاهدة »
  - `10:06#4→d` « واقعيّةٌ بقرينةِ «وطئَ الإنسانُ»، وعقليّةٌ منطقيّةٌ ببناءِ «كلُّ … وال… » — R1 : « وليست واقعيّة لأنّها ليست مشاهدة المتكلّم »

#### `arabe.hijaj.utruha-ism-aw-su2al` — NEUF

- **AR** : تصوغُ الأطروحةَ عنوانًا أو سؤالًا (ظاهرةُ التّدخينِ، ما حقيقةُ الشّجاعةِ؟): الأطروحةُ جملةٌ تقولُ رأيًا يُقبَلُ أو يُردُّ
- **FR** : Tu formules la thèse en titre ou en question (ظاهرةُ التّدخينِ، ما حقيقةُ الشّجاعةِ ؟) : c'est une phrase qui affirme un avis, acceptable ou réfutable
- **EN** : You phrase the thesis as a title or question (ظاهرةُ التّدخينِ، ما حقيقةُ الشّجاعةِ؟): it is a sentence stating an opinion one can accept or reject
- **Chapitres / piège** : ch09 — piège n°2 « صياغةُ الأطروحةِ عنوانًا أو سؤالًا: «المراجعةُ» أو «هل تنفعُ المراجعةُ؟» ليستا أطروحةً، فلا رأيَ فيهما يُقبلُ … » (deux erreurs)
- **Q distinctes** : 5
- **Distracteurs porteurs** :
  - `09:01#3→c` « ظاهرةُ التدخينِ وانتشارُها في الأماكنِ العامّةِ » — R1 : « عنوان لا رأي فيه »
  - `09:04#3→c` « ما حقيقةُ الشجاعةِ في نظرِ الناسِ؟ » — R1 : « سؤال … لا يقول رأيًا »
  - `09:06#3→c` « ما جدوى الفنِّ في حياةِ الأمّةِ، وهل يستحقُّ كلَّ ما يُنفقُ عليه؟ » — R1 : « سؤال … لا يقول رأيًا »
  - `10:06#2→d` « الغشُّ في الامتحاناتِ » — R1 : « عنوانٌ ليس جملةً تامّةً ولا رأيًا »
  - `11:01#6→b` « هل العملُ مفيدٌ للإنسان أم لا؟ » — R1 : « سؤالٌ لا أطروحة »

#### `arabe.hijaj.wazifa-min-al-mawdu3` — NEUF

- **AR** : تحكمُ على وظيفةِ النّصِّ من موضوعِه (مرضٌ ← تأثيرٌ، لغةٌ ← إقناعٌ): الموضوعُ لا يحدّدُ الوظيفةَ بل القرائنُ؛ فنصٌّ عن المرضِ قد يخاطبُ العقلَ
- **FR** : Tu juges la fonction d'après le sujet (maladie → toucher, langue → convaincre) : seuls les indices décident ; un texte sur la maladie peut viser la raison
- **EN** : You judge a text's function from its topic (illness → move, language → persuade): the topic decides nothing, the clues do; a text on illness may address reason
- **Chapitres / piège** : ch10 — piège n°7 « الجوابُ بكلمةٍ بلا قرائنَ، أو الحكمُ بموضوعِ النصِّ: «التأثيرُ لأنّه يتكلّمُ عن المرضِ». والموضوعُ لا يحدّدُ ا… » (id de ch09 pour le second)
- **Q distinctes** : 3
- **Distracteurs porteurs** :
  - `10:quiz#7→c` « الإقناعُ؛ لأنّه يعالجُ مشكلةً حقيقيّةً في المدينةِ » — R1 : « موضوع النص لا قرينة وظيفته »
  - `10:quiz#7→d` « التأثيرُ؛ لأنّه يتحدّثُ عن نظافةِ الأحياءِ والمدينةِ » — R1 : « موضوع النص لا قرينة وظيفته »
  - `10:03#4→c` « الإقناعُ؛ لأنّ موضوعَه علميٌّ يتعلّقُ باللغةِ وقواعدِها » — R1 (paraphrase de l'explication) :  ليس موضوعه هو ما يحدد الوظيفة 
  - `10:05#3→d` « التأثيرُ؛ لأنّ موضوعَه الأطفالُ والمدرسةُ ومشاعرُهم » — R1 : « الموضوع لا يحدد الوظيفة »

### Domaine `i3rab`

#### `arabe.i3rab.af3al-khamsa-3alama` — NEUF

- **AR** : تخلطُ في رفعِ الأفعالِ الخمسةِ (يجتهدونَ، ينجحونَ): علامتُه ثبوتُ النّونِ لا الضمّةُ ولا الواوُ؛ و«يكتبْنَ» مبنيٌّ مع نونِ النّسوةِ فلا يُرفعُ بثبوتِ النّونِ
- **FR** : Tu te trompes sur le rafʿ des cinq verbes (يجتهدونَ، ينجحونَ) : marque = ن maintenu, ni damma ni و ; يكتبْنَ est مبني avec ن النسوة, sans ن maintenu
- **EN** : You get the nominative of the five verbs wrong (يجتهدونَ، ينجحونَ): the mark is the kept ن, not a damma or و; يكتبْنَ is built with the feminine ن, no kept ن
- **Chapitres / piège** : ch01 — (pas de piège ; erreur récurrente dans les items)
- **Q distinctes** : 3
- **Distracteurs porteurs** :
  - `01:05#6→a` « كلاهما بالضمّة » — R1 : « ينجحون … مرفوع بثبوت النون »
  - `01:05#6→d` « الأوّل بثبوت النون والثاني بالواو » — R1 : « ينجحون … مرفوع بثبوت النون »
  - `01:06#1→b` « الضمّة الظاهرة على آخره » — R1 (paraphrase de l'explication) :  معاملته كفعل صحيح الآخر … أو الخلط بجمع المذكر السالم 
  - `01:06#1→c` « الضمّة المقدّرة » — R1 (paraphrase de l'explication) :  معاملته كفعل صحيح الآخر … أو الخلط بجمع المذكر السالم 
  - `01:06#1→d` « الواو؛ لأنّه جمع مذكّر سالم » — R1 (paraphrase de l'explication) :  معاملته كفعل صحيح الآخر … أو الخلط بجمع المذكر السالم 
  - `01:04#1→c` « فعل مضارع مرفوع بثبوت النون » — R1 : « مبنيّ على السكون لاتصاله بنون النسوة » — ثبوت النون ليس علامة هذا الفعل

#### `arabe.i3rab.haraka-bada-harf` — RÉUTILISÉ (REGISTRE)

- **AR** : تعربُ المثنّى أو الجمعَ المذكّرَ السّالمَ أو الأسماءَ الخمسةَ المضافةَ بالحركات: علاماتُها حروف (الألف، الواو، الياء)
- **FR** : Tu donnes une voyelle comme marque au duel, au pluriel masculin régulier ou aux cinq noms annexés : ils se déclinent par des lettres
- **Chapitres / piège** : ch01 — piège n°3 « نصب الأسماء الخمسة بالفتحة قياسًا على بقيّة الأسماء، فيقال «رأيتُ أخوكَ» أو «رأيتُ أخيكَ». والصواب **أخاكَ** ب… » (id du registre 6ᵉ (الأسماء الخمسة comme le duel et le pluriel masculin : lettres, pas voyelles))
- **Q distinctes** : 7
- **Distracteurs porteurs** :
  - `01:quiz#3→a` « الضمّة »
  - `01:01#6→a` « بالضمّة »
  - `01:02#1→a` « الضمّة »
  - `01:02#5→b` « بالضمّة »
  - `01:04#4→a` « الكسرة لأنّه مضاف إليه مفرد » — R1 : « تجرّ بالياء نيابةً عن الكسرة … وليس بالكسرة »
  - `01:04#4→c` « الكسرة المقدّرة لأنّه مثنّى » — R1 : « تجرّ بالياء نيابةً عن الكسرة … وليس بالكسرة »
  - `01:05#2→a` « الكسرة لأنّه اسم مفرد »
  - `01:06#3→c` « نائب فاعل مرفوع بالضمّة » — R1 : « رفعه بالضمة ونسيان أنه جمع مذكر سالم »

#### `arabe.i3rab.harf-ghayr-munasib` — NEUF

- **AR** : تختارُ حرفَ الإعرابِ غيرَ المناسبِ: المثنّى ألفٌ (رفعًا) وياءٌ، وجمعُ المذكّرِ واوٌ (رفعًا) وياءٌ، والأسماءُ الخمسةُ واوٌ وألفٌ وياءٌ
- **FR** : Tu prends la mauvaise lettre de déclinaison : duel ا (rafʿ) / ي ; pluriel masculin و (rafʿ) / ي ; cinq noms و (rafʿ), ا (naṣb), ي (jarr)
- **EN** : You pick the wrong declension letter: dual ا (nominative) / ي; masculine plural و (nominative) / ي; five nouns و (nom.), ا (acc.), ي (gen.)
- **Chapitres / piège** : ch01 — (pas de piège ; erreur récurrente dans les items)
- **Q distinctes** : 7
- **Distracteurs porteurs** :
  - `01:quiz#3→b` « الألف »
  - `01:quiz#3→d` « النون »
  - `01:01#6→c` « بالألف »
  - `01:01#6→d` « بالياء »
  - `01:02#1→b` « الألف »
  - `01:02#1→c` « الياء »
  - `01:02#5→a` « بالواو »
  - `01:02#5→d` « بالياء »
  - `01:04#6→c` « بالياء لأنّها جمع مذكّر سالم »
  - `01:04#6→d` « بالألف لأنّها من الأسماء الخمسة »
  - `01:05#2→d` « الألف لأنّه مثنّى »
  - `01:05#6→c` « الأوّل بالألف والثاني بالواو »

#### `arabe.i3rab.jam3-mu2annath-nasb` — RÉUTILISÉ (REGISTRE)

- **AR** : تفتحُ تاءَ الجمعِ المؤنّثِ السّالمِ المنصوب، أو تعدُّ كسرتَه جرًّا: يُنصَبُ بالكسرة (رأيتُ الطّالباتِ)
- **FR** : Tu mets la fatha au pluriel féminin régulier à l'accusatif, ou tu prends sa kasra pour un génitif : il est à l'accusatif par la kasra
- **Chapitres / piège** : ch11 — piège n°2 « نصب كلّ منصوب بالفتحة ورفع كلّ مرفوع بالضمّة. في هذا السند وحده ثلاث علامات فرعيّة محتملة، وكلّها تسقط ممّن حف… » (id du registre 6ᵉ ; seul 02#4 b porte la fatha « ظاهرة » sur un pluriel féminin ; les deux autres marques fines (النصب بالياء/الألف) n'ont pas de distracteur)
- **Q distinctes** : 2
- **Distracteurs porteurs** :
  - `01:04#6→a` « بالفتحة لأنّها مفعول به » — R1 (paraphrase de l'explication) :  جمع المؤنث السالم ينصب بالكسرة 
  - `11:02#4→b` « مفعول به منصوب وعلامة نصبه الفتحة الظاهرة » — R1 : « أخطأ بجعلها فتحةً ظاهرة »

#### `arabe.i3rab.jarr-jazm-khalt` — NEUF

- **AR** : تخلطُ بين الجرِّ والجزمِ: الجرُّ للأسماءِ وحدَها والجزمُ للأفعالِ المضارعةِ وحدَها؛ فاسألْ أوّلًا: أهي اسمٌ أم فعلٌ؟
- **FR** : Tu confonds جرّ et جزم : le جرّ ne touche que les noms, le جزم que les verbes au présent ; demande d'abord : nom ou verbe ?
- **EN** : You mix up جرّ and جزم: genitive belongs to nouns only, jussive to present-tense verbs only; first ask: noun or verb?
- **Chapitres / piège** : ch01 — piège n°2 « خلط الجرّ بالجزم. وهما لا يلتقيان أبدًا: **الجرّ للأسماء وحدها، والجزم للأفعال المضارعة وحدها**. فمن قال «الطا… »
- **Q distinctes** : 2
- **Distracteurs porteurs** :
  - `01:quiz#2→c` « الجرّ » — R1 : « الجزم يختصّ بالأفعال »
  - `01:02#6→a` « الجرّ » — R1 : « الجرّ خاصّ بالأسماء »

#### `arabe.i3rab.mabni-mu3rab-khalt` — NEUF

- **AR** : تخلطُ بين المُعرَبِ (يتغيّرُ آخرُه بموقعِه) والمبنيِّ (يلزمُ حالةً): الماضي مبنيٌّ وإن تغيّر آخرُه مع الضّميرِ، والمنقوصُ والمقصورُ مُعرَبانِ بعلامةٍ مقدَّرةٍ
- **FR** : Tu confonds مُعرَب (fin variable selon la fonction) et مبني (forme unique) : le passé est مبني même si sa fin varie avec le pronom ; manqus et maqsur : مُعرَب
- **EN** : You confuse مُعرَب (ending changes with function) and مبني (one fixed form): the past tense is مبني even if its ending shifts; manqus and maqsur are مُعرَب
- **Chapitres / piège** : ch01 — (pas de piège ; erreur récurrente dans les items)
- **Q distinctes** : 8
- **Distracteurs porteurs** :
  - `01:quiz#1→a` « المعربة لا تتغيّر حركة آخرها، والمبنية تتغيّر » — R1
  - `01:quiz#1→c` « المعربة هي الحروف فقط، والمبنية هي الأسماء فقط » — R1
  - `01:quiz#1→d` « المعربة لا تدخل في الجملة الفعلية، والمبنية تدخل في كليهما » — R1
  - `01:quiz#4→a` « كتابٌ »
  - `01:quiz#4→b` « مدرسةٌ »
  - `01:quiz#4→d` « معلّمٌ »
  - `01:01#3→b` « طالب »
  - `01:01#3→c` « كتاب »
  - `01:01#3→d` « شمس »
  - `01:02#3→a` « يكتبُ » — R1 (paraphrase de l'explication) :  الماضي مبنيّ دائمًا … المضارعة معربة 
  - `01:02#3→c` « يدرسُ » — R1 (paraphrase de l'explication) :  الماضي مبنيّ دائمًا … المضارعة معربة 
  - `01:02#3→d` « يلعبُ » — R1 (paraphrase de l'explication) :  الماضي مبنيّ دائمًا … المضارعة معربة 
  - `01:05#1→b` « المعربة اسم دائمًا والمبنيّة فعل دائمًا »
  - `01:05#1→c` « المعربة تُنصب فقط والمبنيّة تُرفع فقط »
  - `01:05#4→a` « الكتابُ »
  - `01:05#4→c` « مدرسةٌ »
  - `01:05#4→d` « تلميذٌ »
  - `01:06#4→b` « القاضي (اسم منقوص) » — R1 (paraphrase de l'explication) :  ظنّ أنّ ثبات آخر المنقوص والمقصور يعني البناء 
  - `01:06#4→c` « المعلّمونَ (جمع مذكّر سالم) » — R1 (paraphrase de l'explication) :  ظنّ أنّ ثبات آخر المنقوص والمقصور يعني البناء 
  - `01:06#4→d` « فتًى (اسم مقصور) » — R1 (paraphrase de l'explication) :  ظنّ أنّ ثبات آخر المنقوص والمقصور يعني البناء 
  - `01:06#6→b` « لا خطأ، الماضي معرب فعلًا » — R1 : « الخطأ الشائع: عدّ كلّ تغيّرٍ في الآخر إعرابًا »
  - `01:06#6→d` « الماضي معرب بعلامات مقدّرة » — R1 : « الخطأ الشائع: عدّ كلّ تغيّرٍ في الآخر إعرابًا »

#### `arabe.i3rab.mamnu3-sabab-khalt` — NEUF

- **AR** : تعلّلُ جرَّ «مساجدَ» و«أحمدَ» بالفتحةِ بسببٍ آخرَ (مثنّى، جمعِ مذكّرٍ، أسماءٍ خمسةٍ): الفتحةُ نيابةً عن الكسرةِ للممنوعِ من الصّرفِ وحدَه
- **FR** : Tu expliques la fatha au génitif de مساجدَ ou أحمدَ par une autre cause (duel, pluriel masculin, cinq noms) : seul le ممنوع من الصرف l'a pour la kasra
- **EN** : You explain the genitive fatha of مساجدَ or أحمدَ by another cause (dual, masculine plural, five nouns): only a diptote takes a fatha for the kasra
- **Chapitres / piège** : ch01 — (pas de piège ; erreur récurrente dans les items)
- **Q distinctes** : 4
- **Distracteurs porteurs** :
  - `01:quiz#5→a` « اسم مقصور »
  - `01:quiz#5→c` « مثنّى »
  - `01:quiz#5→d` « جمع مذكّر سالم »
  - `01:02#4→a` « لأنّه جمع مذكّر سالم »
  - `01:02#4→c` « لأنّه مثنّى »
  - `01:02#4→d` « لأنّه من الأسماء الخمسة »
  - `01:04#3→a` « لأنّه اسم علم مذكّر ثلاثيّ ساكن الوسط، فيُجرّ بالكسرة في الأصل »
  - `01:04#3→c` « لأنّه من الأسماء الخمسة التي تُجرّ بالياء »
  - `01:04#3→d` « لأنّ حرف الجرّ «إلى» يجرّ بالفتحة دائمًا »
  - `01:05#2→c` « الفتحة لأنّه ممنوع من الصرف »

#### `arabe.i3rab.mu3tall-3alama-zahira` — NEUF

- **AR** : تكتبُ علامةً ظاهرةً على ما آخرُه حرفُ علّةٍ (يسعى ← فتحةٌ، القاضي ← كسرةٌ، يسعَ ← سكونٌ): تُقدَّرُ العلامةُ على الألفِ والياءِ، ويُجزمُ المعتلُّ بحذفِ حرفِه
- **FR** : Tu écris une marque visible sur une lettre faible finale (يسعى ← fatha, القاضي ← kasra, يسعَ ← sukûn) : elle est sous-entendue sur ا et ي ; au jazm elle tombe
- **EN** : You write a visible mark on a final weak letter (يسعى ← fatha, القاضي ← kasra, يسعَ ← sukun): it is implied on ا and ي; in the jussive the letter drops
- **Chapitres / piège** : ch01 — (pas de piège ; erreur récurrente dans les items)
- **Q distinctes** : 3
- **Distracteurs porteurs** :
  - `01:04#5→a` « الفتحة الظاهرة على آخره » — R1 : « الفتحة المقدّرة على الألف منعًا للتعذّر »
  - `01:06#2→b` « السكون الظاهر » — R1 : « جزمه بالسكون كالصحيح الآخر »
  - `01:06#2→c` « الفتحة » — R1 : « جزمه بالسكون كالصحيح الآخر »
  - `01:06#5→b` « كسرة ظاهرة على الياء » — R1 : « الخطأ الشائع: إثبات كسرة ظاهرة على المنقوص »

### Domaine `intaj`

#### `arabe.intaj.khatima-mawdu3-jadid` — NEUF

- **AR** : تختمُ بفكرةٍ جديدةٍ خارجَ الموضوعِ («وتجدرُ الإشارةُ إلى أنّ التّلوّثَ موضوعٌ آخرُ»): الخاتمةُ تُغلقُ ما فُتحَ ولا تفتحُ بابًا جديدًا
- **FR** : Tu conclus par une idée nouvelle hors sujet (« la pollution est un autre sujet ») : la conclusion referme ce qui fut ouvert, elle n'ouvre pas une porte nouvelle
- **EN** : You close with a new off-topic idea ("it is worth noting pollution is another topic"): a conclusion closes what was opened, it doesn't open a new door
- **Chapitres / piège** : ch11 — piège n°3 « خاتمة تفتح موضوعًا جديدًا: «وفي الأخير، فإنّ التلوّث أيضًا مشكلة كبرى». الخاتمة تُغلق ما فُتح، ومن فتح فيها با… »
- **Q distinctes** : 1
- **Distracteurs porteurs** :
  - `11:quiz#8→b` « وتجدر الإشارة إلى أنّ التلوّث الصناعيّ موضوعٌ آخر يستحقّ بحثًا مستقلًّ… » — R1 : « يُقحم فكرةً جديدةً خارجة عن الموضوع »

### Domaine `ishtiqaq`

#### `arabe.ishtiqaq.af3al-tafdil-wa-lawn-khalt` — NEUF

- **AR** : تعدُّ «أَحمَر» و«أَعرَج» اسمَ تفضيلٍ: «أَفعَل» للّونِ أو العيبِ صفةٌ مشبّهةٌ لا تُتبَعُ بـ«من»، والتّفضيلُ منهما بـ«أشدُّ احمرارًا»
- **FR** : Tu prends أَحمَر et أَعرَج pour un superlatif : أَفعَل de couleur ou de défaut est une صفة مشبّهة, jamais suivie de « من » ; on compare avec أشدُّ احمرارًا
- **EN** : You take أَحمَر and أَعرَج for comparatives: أَفعَل of colour or defect is a resembling adjective, never followed by « من »; compare with أشدُّ احمرارًا
- **Chapitres / piège** : ch06 — piège n°5 « الخلط بين «أَفعَل» التفضيل و«أَفعَل» اللون. «أحمرُ» في «ثوبٌ أحمرُ» صفة مشبّهة لا تفضيل، ودليله أنّها **لا تُت… »
- **Q distinctes** : 2
- **Distracteurs porteurs** :
  - `06:04#4→a` « يجوز مباشرةً، فيُقال «أَعرَج» على وزن أَفعَل » — R1 (paraphrase de l'explication) :  لا تكون دلالته على لون أو عيب 
  - `06:06#4→b` « «أحمرُ» على وزن أفعل التفضيل » — R1 : « الخطأ الشائع: صوغ أحمر على أنّه تفضيل »

#### `arabe.ishtiqaq.fa3il-maf3ul-ma3na` — RÉUTILISÉ (REGISTRE)

- **AR** : تخلطُ بينَ اسمِ الفاعلِ واسمِ المفعول: اسألْ هل الاسمُ قامَ بالفعل (شادّ) أم وقعَ عليه (مشدود)
- **FR** : Tu prends le nom d'agent pour le nom de patient, ou l'inverse : demande-toi si le nom fait l'action (شادّ) ou la subit (مشدود)
- **Chapitres / piège** : ch05 — piège n°11 « الخلطُ بين اسمِ الفاعلِ واسمِ المفعولِ في حركةِ ما قبلَ الآخرِ: أن يقالَ «المُسْتَخْرَجُ» لمن يطلبُ إخراجَ الش… » (id du registre); ch12 — piège n°5 « اشتقاقُ اسمِ الفاعلِ بدلَ اسمِ المفعولِ: «مُلتقٍ» بدلَ «مُلتقًى». الكلمتانِ تتشابهانِ في الكتابةِ العاديّةِ وت… » (id du registre)
- **Q distinctes** : 13
- **Distracteurs porteurs** :
  - `05:05#5→b` « مُسْتَفْعِل » — R1 (paraphrase de l'explication) :  مُسْتَفْعِل اسم فاعل … الخطأ الشائع 
  - `06:quiz#2→b` « وزن مَفعُول »
  - `06:01#1→a` « مَفعُول (مَنصُور) » — R1 (paraphrase de l'explication) :  مَنصُور اسم مفعول 
  - `06:01#2→b` « كَاتِب » — R1 (paraphrase de l'explication) :  كَاتِب اسم فاعل 
  - `06:02#5→a` « اسم مفعول من الثلاثي »
  - `06:05#2→a` « مَنصور » — R1 (paraphrase de l'explication) :  مَنصور اسم مفعول 
  - `06:05#3→a` « فاهِم (فاعِل) » — R1 (paraphrase de l'explication) :  فاهم اسم فاعل 
  - `06:06#1→b` « مكتوب » — R1 (paraphrase de l'explication) :  مكتوب اسم مفعول … الخلط بين الفاعل والمفعول 
  - `11:quiz#5→b` « اسم مفعول يدلّ على من وقع عليه الفعل » — R1 : « ليس اسم مفعول إذ لم يقع عليه الحدث »
  - `11:01#4→b` « اسم مفعول على وزن مَفعول »
  - `11:02#5→b` « اسم مفعول على وزن مَفعول يدلّ على من وقع عليه الخنق » — R1 : « الأزمات فاعلةٌ لا مفعولة »
  - `11:03#3→b` « على وزن فاعِل، اسم فاعل يدلّ على من قام بالأخذ » — R1 : « لم يأخذ بل أُخذ »
  - `12:05#4→a` « مُلتقٍ » — R1 (paraphrase de l'explication) :  مُلتقٍ اسم الفاعل 

#### `arabe.ishtiqaq.fa3il-mubalagha-khalt` — NEUF

- **AR** : تخلطُ بين اسمِ الفاعلِ وصيغةِ المبالغةِ (غافِر ≠ غفّار، صائم ≠ صوّام): اسمُ الفاعلِ يدلُّ على الفعلِ دونَ كثرةٍ، والمبالغةُ على كثرتِه وشدّتِه
- **FR** : Tu confonds nom d'agent et intensif (غافِر ≠ غفّار، صائم ≠ صوّام) : l'agent dit l'action simple, l'intensif son abondance et sa force
- **EN** : You confuse the agent noun with the intensive (غافِر ≠ غفّار، صائم ≠ صوّام): the agent noun states the action, the intensive its abundance and strength
- **Chapitres / piège** : ch06, ch11 — (pas de piège ; erreur récurrente dans les items)
- **Q distinctes** : 6
- **Distracteurs porteurs** :
  - `06:01#4→a` « فَاعِل (صَائِم) » — R1 (paraphrase de l'explication) :  صَائِم اسم فاعل دون مبالغة 
  - `06:04#5→c` « وزن فَاعِل، اسم فاعل من «وَهَبَ» » — R1 : « واهب اسم فاعل … لا مبالغة »
  - `06:05#2→d` « نَصّار »
  - `06:05#4→a` « عالِم » — R1 (paraphrase de l'explication) :  عالِم اسم فاعل 
  - `06:06#3→b` « غافِر (اسم فاعل) » — R1 : « الخطأ الشائع: عدّ غافِر مبالغةً »
  - `11:02#5→c` « صيغة مبالغة على وزن فعّال »

#### `arabe.ishtiqaq.fa3il-mubalagha-wa-sifa` — NEUF

- **AR** : تعدُّ كلَّ «فَعِيل» أو «فَعُول» صفةً مشبّهةً (عَلِيم، غَيُور، سَمِيع): قد تكونُ مبالغةً؛ الثّبوتُ ← صفةٌ مشبّهةٌ، وكثرةُ الحدثِ ← مبالغةٌ
- **FR** : Tu ranges tout فَعِيل ou فَعُول parmi les صفات مشبّهة (عَلِيم، غَيُور) : ce peut être un intensif ; stabilité → صفة مشبّهة, abondance de l'action → intensif
- **EN** : You file every فَعِيل or فَعُول as a resembling adjective (عَلِيم، غَيُور): it may be an intensive; permanence → adjective, abundance of the action → intensive
- **Chapitres / piège** : ch06 — piège n°3 « عدّ كلّ وصف على وزن «فعيل» صفةً مشبّهة. قد يكون «فعيل» صيغة **مبالغة** كـ«عليم» و«سميع» إذا أُريد كثرة الحدث ل… »
- **Q distinctes** : 1
- **Distracteurs porteurs** :
  - `06:04#2→a` « غَيُور — لأنّه على وزن فَعُول » — R1 : غَيُور وعَلِيم من أوزان المبالغة، وحَذِر مشترك
  - `06:04#2→b` « حَذِر — لأنّه على وزن فَعِل » — R1 : غَيُور وعَلِيم من أوزان المبالغة، وحَذِر مشترك
  - `06:04#2→c` « عَلِيم — لأنّه على وزن فَعِيل » — R1 : غَيُور وعَلِيم من أوزان المبالغة، وحَذِر مشترك

#### `arabe.ishtiqaq.makan-ka-fa3il-aw-maf3ul` — NEUF

- **AR** : تخلطُ اسمَ المكانِ أو الزّمانِ (مَفعَل/مَفعِل: مَجلِس، مَدرسة) باسمِ الفاعلِ أو المفعولِ أو المبالغةِ (جالِس، مَجلُوس، جلّاس) لمجرّدِ الميمِ أو الجذرِ المشتركِ
- **FR** : Tu confonds nom de lieu/temps (مَفعَل / مَفعِل : مَجلِس، مَدرسة) et agent, patient ou intensif (جالِس، مَجلُوس، جلّاس) à cause du م ou de la racine commune
- **EN** : You confuse place/time nouns (مَفعَل / مَفعِل: مَجلِس، مَدرسة) with agent, patient or intensive nouns (جالِس، مَجلُوس، جلّاس) due to the م or the shared root
- **Chapitres / piège** : ch06, ch12 — (pas de piège ; erreur récurrente dans les items)
- **Q distinctes** : 7
- **Distracteurs porteurs** :
  - `06:02#1→d` « اسم زمان »
  - `06:02#4→b` « جَالِس » — R1 (paraphrase de l'explication) :  جَالِس اسم فاعل، مَجلُوس اسم مفعول، جَلَّاس مبالغة 
  - `06:02#4→c` « مَجلُوس » — R1 (paraphrase de l'explication) :  جَالِس اسم فاعل، مَجلُوس اسم مفعول، جَلَّاس مبالغة 
  - `06:02#4→d` « جَلَّاس » — R1 (paraphrase de l'explication) :  جَالِس اسم فاعل، مَجلُوس اسم مفعول، جَلَّاس مبالغة 
  - `06:04#3→d` « «جلستُ في المَجلُوسِ» — مَجلُوس: اسم مكان من «جَلَسَ» » — R1 (paraphrase de l'explication) :  مَجلُوس اسم مفعول إذ يجب أن يكون مَجلِس 
  - `06:05#4→d` « مَعلَم » — R1 : « معلَم اسم مكان »
  - `06:06#1→c` « مَكتَب » — R1 : « مَكتَب اسم مكان »
  - `06:06#6→b` « لا خطأ، «مَدرسة» اسم فاعل » — R1 : « الخطأ الشائع: عدّ كل مبدوء بميم اسم فاعل أو مفعول »
  - `06:06#6→c` « «مَدرسة» اسم مفعول » — R1 : « الخطأ الشائع: عدّ كل مبدوء بميم اسم فاعل أو مفعول »
  - `06:06#6→d` « «مَدرسة» صيغة مبالغة » — R1 : « الخطأ الشائع: عدّ كل مبدوء بميم اسم فاعل أو مفعول »
  - `12:05#2→a` « مُلْقًى » — R1 (paraphrase de l'explication) :  مُلْقًى اسم مفعول من ألقى، لاقٍ اسم فاعل  — l'id vient du ch06
  - `12:05#2→b` « لاقٍ » — R1 (paraphrase de l'explication) :  مُلْقًى اسم مفعول من ألقى، لاقٍ اسم فاعل  — l'id vient du ch06

#### `arabe.ishtiqaq.masdar-bada-al-mushtaqq` — RÉUTILISÉ (REGISTRE)

- **AR** : تضعُ المصدرَ (رَدّ، تنظيم) مكانَ اسمِ الفاعلِ أو اسمِ المفعول: المصدرُ يدلُّ على الحدث، لا على مَن قامَ به أو وقعَ عليه
- **FR** : Tu donnes le masdar (رَدّ، تنظيم) au lieu du nom d'agent ou de patient : le masdar nomme l'action, pas celui qui la fait ou la subit
- **Chapitres / piège** : ch05, ch12 — (pas de piège ; erreur récurrente dans les items)
- **Q distinctes** : 4
- **Distracteurs porteurs** :
  - `05:05#5→c` « اسْتِفْعال »
  - `12:05#3→a` « وِقايةٌ » — R1 (paraphrase de l'explication) :  وقاية مصدر، وقاء ممدود 
  - `12:05#3→b` « وِقاءٌ » — R1 (paraphrase de l'explication) :  وقاية مصدر، وقاء ممدود 
  - `12:05#4→c` « التقاءٌ » — R1
  - `12:05#4→d` « لِقاءٌ » — R1
  - `12:05#2→c` « لِقاءٌ » — R1 : « لِقاءٌ مصدر ممدود »

#### `arabe.ishtiqaq.mazid-haraka-al-3ayn` — RÉUTILISÉ (REGISTRE)

- **AR** : تحكمُ بالميمِ المضمومةِ وحدَها: عينُ الفعلِ هي الفاصل، مكسورةٌ لاسمِ الفاعل (مُشرِق) ومفتوحةٌ لاسمِ المفعول (مُزيَّن)
- **FR** : Pour un verbe augmenté, tu juges par le م initial : c'est la voyelle avant la dernière lettre qui décide — kasra : agent (مُشرِق), fatha : patient (مُزيَّن)
- **Chapitres / piège** : ch06 — piège n°2 « إهمال الشكل في الكتابة، فتصير «مدرس» كلمة غامضة لا يُعرف أمعلّم صاحبها أم متعلّم. وفي الامتحان تُسأل عن الصيغة… » (id du registre : la voyelle est la réponse (مُكرِم / مُكرَم))
- **Q distinctes** : 7
- **Distracteurs porteurs** :
  - `06:quiz#2→d` « ضمّ أوّله وفتح ما قبل آخره » — R1 : « ضمّ أوّله وفتح ما قبل آخره » = patient
  - `06:01#3→a` « اسم مفعول من غير الثلاثي » — R1 (paraphrase de l'explication) :  ولو فُتح ما قبل آخره لصار اسم مفعول 
  - `06:02#1→a` « اسم فاعل من «استَعمَلَ» » — R1 (paraphrase de l'explication) :  ولو كُسر ما قبل الآخر لصار اسم فاعل 
  - `06:04#1→b` « كلتاهما اسم مفعول، والفرق في الإعراب فقط » — R1 (paraphrase de l'explication) :  الفرق الحركي هو المعيار الوحيد 
  - `06:04#1→d` « كلتاهما اسم فاعل لأنّ الفعل السداسي لا يبني اسم مفعول » — R1 (paraphrase de l'explication) :  الفرق الحركي هو المعيار الوحيد 
  - `06:04#6→a` « الطالب مصيب؛ فكلا الكلمتين تبدآن بميم مضمومة فالفرق اعتباطي » — R1 : « فالطالب عكس الحكمين »
  - `06:05#5→b` « اسم فاعل بفتح ما قبل الآخر » — R1 (paraphrase de l'explication) :  ولو كُسر ما قبل الآخر لصار اسم فاعل 
  - `06:06#2→b` « مُكرِم (بكسر الراء) » — R1 : « الخطأ الشائع: كسر ما قبل الآخر »

#### `arabe.ishtiqaq.mim-ala-maftuha` — NEUF

- **AR** : تفتحُ ميمَ اسمِ الآلةِ فيصيرُ مكانًا (مَكنَسة)، أو تعدُّ المكانَ والزّمانَ آلةً (مَوعِد، مَلعَب): ميمُ الآلةِ مكسورةٌ (مِكنَسة، مِفتاح) وميمُ المكانِ مفتوحةٌ
- **FR** : Tu ouvres le م de l'outil (مَكنَسة) ou prends un lieu/temps pour un outil (مَوعِد، مَلعَب) : م d'outil = kasra (مِكنَسة، مِفتاح), م de lieu/temps = fatha
- **EN** : You open the م of an instrument (مَكنَسة) or take a place/time for an instrument (مَوعِد، مَلعَب): instrument م = kasra (مِكنَسة، مِفتاح), place/time م = fatha
- **Chapitres / piège** : ch06 — piège n°7 « فتح الميم في اسم الآلة فتصير اسم مكان: «مَكنَسة» بدل «مِكنَسة». والحركة هنا ليست تفصيلًا: هي التي تقول أهي الأ… »
- **Q distinctes** : 2
- **Distracteurs porteurs** :
  - `06:05#6→a` « مَوعِد (اسم زمان) » — R1 (paraphrase de l'explication) :  مَوعِد اسم زمان، مَلعَب اسم مكان 
  - `06:05#6→c` « مَلعَب (اسم مكان) » — R1 (paraphrase de l'explication) :  مَوعِد اسم زمان، مَلعَب اسم مكان 
  - `06:06#5→b` « اسم مكان، على وزن «مَفعال» » — R1 (paraphrase de l'explication) :  الخطأ الشائع: عدّه اسم مكان؛ المكان يُفتح ميمه 

#### `arabe.ishtiqaq.min-fi3l-akhar` — RÉUTILISÉ (REGISTRE)

- **AR** : تشتقُّ من فعلٍ غيرِ المطلوب: «لَفَّ» ← ملفوف لا «مُلفَّف» (من لفّفَ)، و«استعملَ» ← مُستعمَل لا «معمول»
- **FR** : Tu dérives d'un autre verbe que celui demandé : لفَّ donne ملفوف (pas ملفّف, de لفّفَ), استعملَ donne مستعمَل (pas معمول)
- **Chapitres / piège** : ch05 — (pas de piège ; erreur récurrente dans les items)
- **Q distinctes** : 1
- **Distracteurs porteurs** :
  - `05:05#5→d` « مُفْتَعَل » — R1 (paraphrase de l'explication) :  مُفْتَعَل من افْتَعَلَ لا من اسْتَفْعَلَ 

#### `arabe.ishtiqaq.sifa-mushabbaha-khalt` — NEUF

- **AR** : تخلطُ الصّفةَ المشبّهةَ (كريم، نصير، حسين) باسمِ الفاعلِ أو المفعولِ أو التّفضيلِ: هي صفةٌ ثابتةٌ في صاحبِها لا حدثٌ متجدّدٌ
- **FR** : Tu confonds la صفة مشبّهة (كريم، نصير، حسين) avec l'agent, le patient ou le superlatif : c'est une qualité stable de son porteur, pas une action répétée
- **EN** : You confuse the resembling adjective (كريم، نصير، حسين) with the agent, patient or comparative: it is a stable quality of its bearer, not a recurring action
- **Chapitres / piège** : ch06 — (pas de piège ; erreur récurrente dans les items)
- **Q distinctes** : 13
- **Distracteurs porteurs** :
  - `06:quiz#4→a` « لا فرق بينهما في الدلالة »
  - `06:quiz#4→b` « اسم الفاعل يُبنى من الرباعي فقط، والصفة المشبّهة من الثلاثي »
  - `06:quiz#4→c` « اسم الفاعل يدلّ على صفة ثابتة دائمة، والصفة المشبّهة تدلّ على حدث مؤقّ… »
  - `06:01#1→d` « فَعِيل (نَصِير) » — R1 : « نَصِير صفة مشبّهة »
  - `06:01#2→c` « كَتِيب »
  - `06:01#5→d` « فَعِيل (حَسِين) » — R1 : « حَسِين صفة مشبّهة »
  - `06:02#1→c` « صفة مشبّهة »
  - `06:02#3→a` « كلاهما اسم فاعل » — R1 (paraphrase de l'explication) :  كريم على فعيل صفة مشبّهة تدلّ على الثبوت 
  - `06:02#3→c` « «كاتب» صفة مشبّهة و«كريم» اسم فاعل » — R1 (paraphrase de l'explication) :  كريم على فعيل صفة مشبّهة تدلّ على الثبوت 
  - `06:02#3→d` « كلاهما صفة مشبّهة » — R1 (paraphrase de l'explication) :  كريم على فعيل صفة مشبّهة تدلّ على الثبوت 
  - `06:02#5→d` « صفة مشبّهة » — R1 : « يدلّ على حدث متجدّد لا صفة ثابتة »
  - `06:04#1→c` « «مُستَخدِم» صفة مشبّهة، و«مُستَخدَم» اسم فاعل »
  - `06:04#5→d` « وزن فَعِيل، صفة مشبّهة »
  - `06:05#2→c` « نَصير »
  - `06:05#3→c` « فهيم (فعيل) »
  - `06:05#5→c` « صفة مشبّهة لا فرق فيها »
  - `06:06#2→c` « كريم »

#### `arabe.ishtiqaq.wazn-ala-khalt` — NEUF

- **AR** : تخلطُ بين أوزانِ اسمِ الآلةِ الثّلاثةِ: مِفعَال (مِفتاح)، ومِفعَل (مِبرَد)، ومِفعَلة (مِكنَسة)؛ التّاءُ الأخيرةُ تعيّنُ مِفعَلة وألفُ المدِّ تعيّنُ مِفعَال
- **FR** : Tu mélanges les trois schèmes de l'outil : مِفعَال (مِفتاح), مِفعَل (مِبرَد), مِفعَلة (مِكنَسة) ; la ة finale impose مِفعَلة, l'alif long مِفعَال
- **EN** : You mix the three instrument patterns: مِفعَال (مِفتاح), مِفعَل (مِبرَد), مِفعَلة (مِكنَسة); a final ة means مِفعَلة, a long alif means مِفعَال
- **Chapitres / piège** : ch06 — (pas de piège ; erreur récurrente dans les items)
- **Q distinctes** : 4
- **Distracteurs porteurs** :
  - `06:quiz#5→a` « مِفعَل »
  - `06:quiz#5→b` « مِفعَلة »
  - `06:quiz#5→d` « فَعَّال »
  - `06:01#6→a` « مِبرَد » — R1 : مِبرَد = مِفعَل، مِكنَسة = مِفعَلة، مِقَصّ = مِفعَل
  - `06:01#6→c` « مِكنَسة » — R1 : مِبرَد = مِفعَل، مِكنَسة = مِفعَلة، مِقَصّ = مِفعَل
  - `06:01#6→d` « مِقصَّ » — R1 : مِبرَد = مِفعَل، مِكنَسة = مِفعَلة، مِقَصّ = مِفعَل
  - `06:02#6→b` « مِفعَال » — R1 : « ختمها بالتاء يعيّن وزن مِفعَلة »
  - `06:02#6→c` « مِفعَل » — R1 : « ختمها بالتاء يعيّن وزن مِفعَلة »
  - `06:02#6→d` « فَعَّال » — R1 : « ختمها بالتاء يعيّن وزن مِفعَلة »
  - `06:04#5→a` « وزن مِفعَال، اسم آلة »

#### `arabe.ishtiqaq.wazn-fa3il-lil-mazid` — RÉUTILISÉ (REGISTRE)

- **AR** : تشتقُّ من المزيدِ على وزنِ «فاعِل» (أسرعَ ← سارِع): انطلقْ من المضارع (يُسرِعُ) ← «مُسرِع»
- **FR** : Tu dérives un verbe augmenté sur le schème فاعِل (أسرعَ → سارع) : pars du présent (يُسرِعُ) → مُسرِع
- **Chapitres / piège** : ch06 — piège n°1 « بناء اسم الفاعل من غير الثلاثيّ على وزن «فاعل»، فيقال «داعم» من «أدعم». والصواب أنّ ما زاد على ثلاثة يبدأ بـ**… » (id du registre)
- **Q distinctes** : 1
- **Distracteurs porteurs** :
  - `06:quiz#2→a` « وزن فَاعِل » — R1 : le schème فاعِل pour un verbe augmenté

### Domaine `jidhr`

#### `arabe.jidhr.alif-ka-harf-asli` — NEUF

- **AR** : تعدُّ الألفَ حرفًا من الجذرِ (ر ج ا، ر ع ا، س ا ه): الألفُ في الآخِرِ انقلابٌ عن واوٍ أو ياءٍ، فارجعْ إلى الفعلِ الثّلاثيِّ (رَجَوتُ)
- **FR** : Tu comptes l'alif comme lettre de la racine (ر ج ا، ر ع ا، س ا ه) : l'alif final vient d'un و ou d'un ي ; remonte au verbe trilitère (رَجَوتُ)
- **EN** : You count the alif as a root letter (ر ج ا، ر ع ا، س ا ه): a final alif stands for a و or ي; go back to the three-letter verb (رَجَوتُ)
- **Chapitres / piège** : ch12 — piège n°6 « خطآنِ يتكرّرانِ. الأوّلُ عدُّ الألفِ كما تُرى حرفًا من الجذرِ: جذرُ «المُرتجى» ليس «ر ج ا»، وجذرُ «رُعاة» ليس … » (deux erreurs en un seul bloc)
- **Q distinctes** : 3
- **Distracteurs porteurs** :
  - `12:03#5→b` « س ا ه » — R1
  - `12:04#1→b` « أ و ا » — R1
  - `12:04#5→d` « ر ج ا » — R1 : « الألف الأخيرة منقلبة لا حرف من الجذر »

#### `arabe.jidhr.harf-zaid-fil-jidhr` — NEUF

- **AR** : تُدخلُ حرفًا زائدًا في الجذرِ (الميمُ في المَأوى، التّاءُ في المُرتجى، نونُ التّنوينِ في ساهٍ): الميمُ والتّاءُ والتّنوينُ ليست من الجذرِ
- **FR** : Tu mets une lettre ajoutée dans la racine (le م de المَأوى، le ت de المُرتجى، le ن du tanwin de ساهٍ) : م، ت et le tanwin ne font pas partie de la racine
- **EN** : You put an added letter in the root (the م of المَأوى, the ت of المُرتجى, the tanwin ن of ساهٍ): م، ت and the tanwin are not root letters
- **Chapitres / piège** : ch12 — (pas de piège ; erreur récurrente dans les items)
- **Q distinctes** : 3
- **Distracteurs porteurs** :
  - `12:03#5→d` « س ه ن » — R1 : « التنوين ليس حرفًا من الجذر »
  - `12:04#1→a` « م أ و » — R1 : « الميم زائدة »
  - `12:04#5→c` « ر ت ج » — R1

#### `arabe.jidhr.ya-min-al-fi3l-al-mazid` — NEUF

- **AR** : تأخذُ الياءَ الظّاهرةَ أصلًا للجذرِ (ر ج ي، س ه ي): الخماسيُّ يقلبُ ألفَه ياءً دائمًا فلا يدلُّ على الأصلِ، والأصلُ في الثّلاثيِّ (رَجَوتُ، سَهَوتُ)
- **FR** : Tu prends le ي visible pour une lettre de la racine (ر ج ي، س ه ي) : le verbe à 5 lettres met toujours ي ; lis l'origine dans le trilitère (رَجَوتُ)
- **EN** : You take the visible ي as a root letter (ر ج ي، س ه ي): a 5-letter verb always shows ي; read the origin in the three-letter verb (رَجَوتُ)
- **Chapitres / piège** : ch12 — piège n°6 « خطآنِ يتكرّرانِ. الأوّلُ عدُّ الألفِ كما تُرى حرفًا من الجذرِ: جذرُ «المُرتجى» ليس «ر ج ا»، وجذرُ «رُعاة» ليس … » (deux erreurs en un seul bloc)
- **Q distinctes** : 2
- **Distracteurs porteurs** :
  - `12:03#5→a` « س ه ي » — R1 : « انقلبت ياءً … فالواو هي الأصل »
  - `12:04#5→b` « ر ج ي » — R1

### Domaine `lugha`

#### `arabe.lugha.ma3na-mashhur-bila-siyaq` — NEUF

- **AR** : تختارُ المعنى الأشهرَ للكلمةِ لا المعنى الذي يقتضيه السّياقُ (يَحمِلُ ← يَرفعُ، يَضرِبُ ← يَلطِمُ): انظرْ إلى المفعولِ وحرفِ الجرِّ المجاورَينِ
- **FR** : Tu choisis le sens le plus connu du mot et non celui du contexte (يَحمِلُ ← يَرفعُ، يَضرِبُ ← يَلطِمُ) : regarde l'objet et la préposition voisins
- **EN** : You pick the word's best-known sense instead of the contextual one (يَحمِلُ ← يَرفعُ، يَضرِبُ ← يَلطِمُ): look at the neighbouring object and preposition
- **Chapitres / piège** : ch10 — piège n°6 « اختيارُ المعنى الأشهرِ للكلمةِ لا المعنى الذي يقتضيه السياقُ: من شرحَ «أقامَ الكاتبُ الدليلَ» بـ«سكنَ» أخذَ أش… »
- **Q distinctes** : 5
- **Distracteurs porteurs** :
  - `10:quiz#8→a` « يَرْفَعُ » — R1 : « من معاني حَمَلَ في … »
  - `10:quiz#8→b` « يَتَحَمَّلُ » — R1 : « من معاني حَمَلَ في … »
  - `10:quiz#8→d` « يَنْقُلُ » — R1 : « من معاني حَمَلَ في … »
  - `10:03#6→b` « يَطْرَحُ » — R1 (paraphrase de l'explication) :  من معانيها في أثار سؤالًا / أثار الغبار 
  - `10:03#6→c` « يَرْفَعُ » — R1 (paraphrase de l'explication) :  من معانيها في أثار سؤالًا / أثار الغبار 
  - `10:04#2→b` « يَتَغَيَّرُ » — R1 : « من معاني حالَ في حالَ لونه »
  - `10:05#5→b` « يَلْطِمُ » — R1 : « من معاني ضَرَبَ في … »
  - `10:05#5→c` « يُسَافِرُ » — R1 : « من معاني ضَرَبَ في … »
  - `10:05#5→d` « يَسُكُّ » — R1 : « من معاني ضَرَبَ في … »
  - `10:06#5→a` « يُنَاوِلُ » — R1 : « من معاني سلّم في … »
  - `10:06#5→b` « يُحَيِّي » — R1 : « من معاني سلّم في … »
  - `10:06#5→d` « يَسْتَسْلِمُ » — R1 : « من معاني سلّم في … »

### Domaine `mamdud`

#### `arabe.mamdud.hamza-ila-ya-bila-asl` — NEUF

- **AR** : تردُّ الهمزةَ إلى ياءٍ لا أصلَ لها (حمرايانِ، صحرايانِ، عدّايانِ): تُردُّ إلى أصلِها إن كانت منقلبةً (بِنايانِ)، وهمزةُ التّأنيثِ تصيرُ واوًا
- **FR** : Tu rends la hamza à un ي sans origine (حمرايان، صحرايات، عدّايان) : on la rend à son origine si elle est substituée (بِنايان) ; celle du ta'nîth devient و
- **EN** : You turn the hamza back into a ي with no basis (حمرايان، صحرايات، عدّايان): it goes back to its origin only if substituted (بِنايان); the feminine one becomes و
- **Chapitres / piège** : ch12 — (pas de piège ; erreur récurrente dans les items)
- **Q distinctes** : 3
- **Distracteurs porteurs** :
  - `12:quiz#5→c` « حمرايان »
  - `12:quiz#5→d` « حمرَيان »
  - `12:02#2→b` « صحرايات » — R1
  - `12:04#2→b` « عدّاءان أو عدّايان » — R1 : « يردّها إلى ياء لا أصل لها هنا »

#### `arabe.mamdud.hamza-ta2nith-tubqa` — NEUF

- **AR** : تُبقي همزةَ التّأنيثِ في المثنّى والجمعِ كما تُبقي الأصليّةَ (حمراءانِ، صحراءاتٌ): تُقلبُ واوًا وجوبًا: حمراوانِ، صحراواتٌ
- **FR** : Tu gardes la hamza de ta'nîth au duel et au pluriel comme une hamza originelle (حمراءان، صحراءات) : elle devient و obligatoirement : حمراوان، صحراوات
- **EN** : You keep the feminine-ending hamza in the dual and plural as if it were original (حمراءان، صحراءات): it must become و: حمراوان، صحراوات
- **Chapitres / piège** : ch12 — piège n°4 « قلبُ كلِّ همزةٍ واوًا: «قُرّاوان» و«ابتداوان». القلبُ واجبٌ في **همزةِ التأنيثِ وحدَها**؛ والهمزةُ الأصليّةُ ت… » (deux erreurs en un seul bloc)
- **Q distinctes** : 2
- **Distracteurs porteurs** :
  - `12:quiz#5→a` « حمراءان » — R1 : « فلا إبقاء لها »
  - `12:02#2→a` « صحراءات » — R1

#### `arabe.mamdud.nawa3-al-hamza-khalt` — NEUF

- **AR** : تخلطُ بين أنواعِ همزةِ الممدودِ: التّأنيثُ يُقلبُ واوًا وجوبًا، والمنقلبةُ لها وجهانِ (بِناءانِ، بِنايانِ)، والأصليّةُ تبقى (ابتداءانِ)
- **FR** : Tu confonds les trois hamza du mamdud : ta'nîth → و obligatoire ; substituée → deux formes (بِناءان، بِنايان) ; originelle → elle reste (ابتداءان)
- **EN** : You mix up the three kinds of mamdud hamza: feminine → و compulsory; substituted → two forms (بِناءان، بِنايان); original → it stays (ابتداءان)
- **Chapitres / piège** : ch12, ch14 — (pas de piège ; erreur récurrente dans les items)
- **Q distinctes** : 5
- **Distracteurs porteurs** :
  - `12:02#3→a` « حمراء » — R1 : حمراء/عرجاء/صفراء sont des hamza de ta'nîth
  - `12:02#3→c` « عرجاء » — R1 : حمراء/عرجاء/صفراء sont des hamza de ta'nîth
  - `12:02#3→d` « صفراء » — R1 : حمراء/عرجاء/صفراء sont des hamza de ta'nîth
  - `12:04#2→d` « عدّاءان وجوبًا »
  - `12:04#3→a` « لأنّ همزتَها همزةُ تأنيثٍ زائدةٌ، فهي لا تُقلبُ »
  - `12:04#3→c` « لأنّ همزتَها منقلبةٌ عن واوٍ، فيتعيّنُ فيها الإبقاءُ »
  - `12:04#3→d` « لأنّ الكلمةَ مصدرٌ، والمصادرُ لا تتغيّرُ همزتُها »
  - `14:04#2→b` « ابتداويّ، لأنّ همزتَه منقلبةٌ عن واوٍ » — R1 (paraphrase de l'explication) :  القلب واجب في همزة التأنيث وحدها … الأصلية تبقى 
  - `14:04#2→c` « ابتدايّ، لأنّ الهمزةَ تُحذفُ عند النّسبةِ » — R1 (paraphrase de l'explication) :  القلب واجب في همزة التأنيث وحدها … الأصلية تبقى 
  - `14:04#2→d` « بَدْئيّ، لأنّ النّسبةَ تُردُّ إلى المصدرِ الثلاثيِّ » — R1 (paraphrase de l'explication) :  القلب واجب في همزة التأنيث وحدها … الأصلية تبقى 
  - `14:05#3→b` « كِساويّ فقط، لأنّ القلبَ إلى الواوِ واجبٌ دائمًا » — R1 : « القلب الواجب خاص بهمزة التأنيث »
  - `14:05#3→c` « كَسْويّ، لأنّ الكلمةَ تُردُّ إلى جذرِها دائمًا » — R1 : « القلب الواجب خاص بهمزة التأنيث »
  - `14:05#3→d` « كِسايّ، لأنّ الهمزةَ تُقلبُ ياءً دائمًا » — R1 : « القلب الواجب خاص بهمزة التأنيث »

#### `arabe.mamdud.qalb-kull-hamza-waw` — NEUF

- **AR** : تقلبُ كلَّ همزةٍ واوًا في المثنّى (قُرّاوانِ، ابتداوانِ): القلبُ واجبٌ في همزةِ التّأنيثِ وحدَها، والأصليّةُ تبقى والمنقلبةُ لها وجهانِ
- **FR** : Tu changes toute hamza en و au duel (قُرّاوان، ابتداوان) : seule la hamza de ta'nîth y est obligée ; l'originelle reste, la substituée a deux formes
- **EN** : You turn every hamza into و in the dual (قُرّاوان، ابتداوان): only the feminine hamza must change; an original one stays, a substituted one has two forms
- **Chapitres / piège** : ch12 — piège n°4 « قلبُ كلِّ همزةٍ واوًا: «قُرّاوان» و«ابتداوان». القلبُ واجبٌ في **همزةِ التأنيثِ وحدَها**؛ والهمزةُ الأصليّةُ ت… » (deux erreurs en un seul bloc)
- **Q distinctes** : 1
- **Distracteurs porteurs** :
  - `12:04#2→c` « عدّاوان وجوبًا » — R1 (paraphrase de l'explication) :  القلب الواجب خاص بهمزة التأنيث 

### Domaine `manqus`

#### `arabe.manqus.hadhf-ya-ta3mim` — NEUF

- **AR** : تحذفُ ياءَ المنقوصِ في كلِّ حالٍ (جاءَ القاضِ): لا تُحذفُ إلّا في النّكرةِ رفعًا وجرًّا، وتثبتُ في المعرَّفِ وفي النّصبِ: القاضي، قاضيًا
- **FR** : Tu supprimes le ي du manqus partout (جاءَ القاضِ) : il ne tombe qu'à l'indéfini, nominatif ou génitif ; il reste au défini et à l'accusatif : القاضي، قاضيًا
- **EN** : You drop the manqus ي everywhere (جاءَ القاضِ): it falls only when indefinite, nominative or genitive; it stays when definite or accusative: القاضي، قاضيًا
- **Chapitres / piège** : ch12 — piège n°3 « حذفُ الياءِ من **المعرَّفِ**: «جاء القاضِ». الحذفُ لا يقعُ إلّا في **النكرةِ**؛ وما دخلته «أل» فياؤُه ثابتةٌ: … »
- **Q distinctes** : 2
- **Distracteurs porteurs** :
  - `12:quiz#4→b` « لأنّ المنقوصَ تُحذفُ ياؤُه في جميعِ حالاتِه » — R1 (paraphrase de l'explication) :  تحذف في الرفع والجر نكرةً فقط 
  - `12:quiz#4→c` « لأنّ الياءَ تُحذفُ كلَّما سُبقت بكسرةٍ » — R1 (paraphrase de l'explication) :  تحذف في الرفع والجر نكرةً فقط 
  - `12:03#1→d` « كلُّ اسمٍ حُذفت ياؤُه في جميعِ أحوالِه » — R1 : « حذف الياء لا يقع في كل الأحوال »

#### `arabe.manqus.maqsur-bi-hadhf-ya` — NEUF

- **AR** : تعدُّ «راجٍ» و«قاضٍ» و«تعالٍ» مقصورةً لأنّ الياءَ لا تظهرُ: أدخِلْ «أل»، فإن عادتِ الياءُ فهو منقوصٌ، وإن بقيتِ الألفُ فهو مقصورٌ
- **FR** : Tu prends راجٍ، قاضٍ، تعالٍ pour des maqsur parce que le ي ne se voit pas : ajoute « أل » — si le ي revient c'est un manqus, si l'alif reste c'est un maqsur
- **EN** : You take راجٍ، قاضٍ، تعالٍ for maqsur nouns because no ي shows: add « أل » — if the ي comes back it is a manqus, if the alif stays it is a maqsur
- **Chapitres / piège** : ch12 — piège n°7 « عدُّ «راجٍ» و«قاضٍ» و«تعالٍ» أسماءً مقصورةً لأنّ آخرَها لا يُظهرُ ياءً. الاختبارُ الوحيدُ هو **إدخالُ «أل»**: … »
- **Q distinctes** : 1
- **Distracteurs porteurs** :
  - `12:02#6→a` « مقصورٌ لأنّ آخرَه لا يُظهرُ ياءً » — R1 (paraphrase de l'explication) :  أدخل أل تعد ياؤها 

### Domaine `maqsur`

#### `arabe.maqsur.al-wa-tanwin` — RÉUTILISÉ (REGISTRE)

- **AR** : تجمعُ «ال» والتّنوين (المَقْهًى، السّاعٍ): «ال» تُسقِطُ التّنوين، فالصّوابُ «المَقْهَى»
- **FR** : Tu mets le tanwin sur un nom qui a « ال » (المقهًى، السّاعٍ) : « ال » fait tomber le tanwin — المقهى
- **Chapitres / piège** : ch12 — (pas de piège ; erreur récurrente dans les items)
- **Q distinctes** : 2
- **Distracteurs porteurs** :
  - `12:01#3→a` « إذا ورد معرّفًا بأل »
  - `12:03#6→c` « سلّمتُ على القاضٍ » — R1 : « لا يُجمع بين أل والتنوين »

#### `arabe.maqsur.hamza-fi-muthanna-wal-jam3` — NEUF

- **AR** : تزيدُ همزةً على المقصورِ في المثنّى أو الجمعِ (عَصاءانِ، هُداءانِ، ذِكراءاتٌ): الهمزةُ لا تلحقُ المقصورَ، وألفُه تصيرُ ياءً أو واوًا
- **FR** : Tu ajoutes une hamza au maqsur au duel ou au pluriel (عَصاءان، هُداءان، ذِكراءات) : la hamza ne s'ajoute pas au maqsur, son alif devient ي ou و
- **EN** : You add a hamza to a maqsur in the dual or plural (عَصاءان، هُداءان، ذِكراءات): a maqsur takes no hamza, its alif becomes ي or و
- **Chapitres / piège** : ch12 — (pas de piège ; erreur récurrente dans les items)
- **Q distinctes** : 5
- **Distracteurs porteurs** :
  - `12:quiz#3→a` « عَصاءان »
  - `12:01#4→c` « مُستشفاءان »
  - `12:02#5→c` « المُصطفاؤون »
  - `12:03#3→b` « ذِكراءات »
  - `12:05#1→c` « هُداءان »

#### `arabe.maqsur.muthanna` — RÉUTILISÉ (REGISTRE)

- **AR** : تُبقي الـ«ى» في المثنّى أو تجعلُها ألفًا (فتىانِ، فتاانِ): تصيرُ ياءً (فتَيانِ)، وتعودُ ألفًا مقصورةً في المفرد (فتًى)
- **FR** : Au duel, tu gardes le « ى » ou tu en fais un « ا » (فتىانِ، فتاانِ) : il devient « ي » (فتَيانِ) et redevient « ى » au singulier
- **Chapitres / piège** : ch12 — (pas de piège ; erreur récurrente dans les items)
- **Q distinctes** : 2
- **Distracteurs porteurs** :
  - `12:01#4→a` « مُستشفان » — R1 : l'alif non transformée
  - `12:05#1→d` « هُدان » — R1 : « أهمل ردّ الألف »

#### `arabe.maqsur.muthanna-thulathi-ya-daiman` — NEUF

- **AR** : تقلبُ ألفَ المقصورِ الثّلاثيِّ ياءً (عَصَيانِ): الياءُ الدّائمةُ لما زادَ على ثلاثةِ أحرفٍ، والثّلاثيُّ تُردُّ ألفُه إلى أصلِها (عَصَوانِ)
- **FR** : Tu mets un ي au duel d'un maqsur de trois lettres (عَصَيان) : le ي systématique vaut au-delà de trois lettres ; le trilitère revient à son origine (عَصَوان)
- **EN** : You put a ي in the dual of a three-letter maqsur (عَصَيان): the fixed ي is for four letters or more; a three-letter one goes back to its origin (عَصَوان)
- **Chapitres / piège** : ch12 — piège n°2 « تعميمُ الياءِ على الثلاثيِّ: «عَصَيان» بدل **عَصَوان**. القاعدةُ «ياءً دائمًا» لا تسري إلّا على ما **زاد على ث… »
- **Q distinctes** : 1
- **Distracteurs porteurs** :
  - `12:quiz#3→b` « عَصَيان » — R1 : « عَصَيان خطأ »

#### `arabe.maqsur.muthanna-waw-ghayr-al-asl` — NEUF

- **AR** : تردُّ ألفَ المقصورِ إلى واوٍ دائمًا (هُدوانِ، مُستشفوانِ، ذِكرَواتٌ): ما زادَ على ثلاثةٍ ياءٌ دائمًا، والثّلاثيُّ يتبعُ أصلَه (هُديانِ)
- **FR** : Tu rends l'alif du maqsur à un و par défaut (هُدوان، مُستشفوان، ذِكرَوات) : au-delà de trois lettres c'est toujours ي ; le trilitère suit son origine (هُديان)
- **EN** : You turn the maqsur alif into و by default (هُدوان، مُستشفوان، ذِكرَوات): beyond three letters it is ي; a three-letter one follows its origin (هُديان)
- **Chapitres / piège** : ch12 — (pas de piège ; erreur récurrente dans les items)
- **Q distinctes** : 3
- **Distracteurs porteurs** :
  - `12:01#4→d` « مُستشفوان » — R1 (paraphrase de l'explication) :  ردّ الألف إلى واو في الثلاثي وحده 
  - `12:03#3→a` « ذِكرَوات »
  - `12:05#1→b` « هُدوان » — R1 : « ردّها واوًا على غير أصل »

#### `arabe.maqsur.nakira-bila-tanwin` — RÉUTILISÉ (REGISTRE)

- **AR** : تكتبُ المقصورَ النّكرةَ بلا تنوين (مَبْنَى): النّكرةُ منوّنة، فالصّوابُ «مَبْنًى»
- **FR** : Tu écris le maqsur indéfini sans tanwin (مبنَى) : sans « ال », il porte le tanwin — مبنًى
- **Chapitres / piège** : ch12 — piège n°1 « ظنُّ أنّ المقصورَ «لا ينوَّنُ». التنوينُ يظهرُ عليه **إذا كان نكرةً** — «رأيتُ فتًى» صوابٌ، و«رأيتُ فتى» بلا ت… »
- **Q distinctes** : 1
- **Distracteurs porteurs** :
  - `12:01#3→d` « لا يظهرُ عليه تنوينٌ أبدًا » — R1 : « لا يظهر عليه تنوين أبدًا »

### Domaine `masdar`

#### `arabe.masdar.wazn-fi3l-akhar` — RÉUTILISÉ (REGISTRE)

- **AR** : تعطي مصدرَ فعلٍ آخرَ من الحروفِ نفسِها: حدِّدْ وزنَ الفعلِ أوّلًا (اِنْكَسَرَ على اِنْفَعَلَ ← انكِسار)
- **FR** : Tu donnes le masdar d'un autre verbe de la même racine : trouve d'abord le schème du verbe (انكسرَ : انفعلَ → انكسار)
- **Chapitres / piège** : ch05 — (pas de piège ; erreur récurrente dans les items)
- **Q distinctes** : 1
- **Distracteurs porteurs** :
  - `05:04#4→a` « افْعِلال » — R1 : « يؤخذ مصدر وزن مجاور »
  - `05:04#4→b` « افْعِيلال » — R1 : « يؤخذ مصدر وزن مجاور »
  - `05:04#4→d` « اسْتِفْعال » — R1 : « يؤخذ مصدر وزن مجاور »

### Domaine `mazid`

#### `arabe.mazid.af3ala-ja3liyya-daiman` — NEUF

- **AR** : تحملُ كلَّ «أَفْعَلَ» على الجعليّةِ (أَبْحَرَتِ، أَثْمَرَتِ): انظرْ إلى الجذرِ: فعلٌ ← جعليّةٌ، اسمُ شيءٍ ← صيرورةٌ، اسمُ مكانٍ ← دخولٌ
- **FR** : Tu lis tout أَفْعَلَ comme جعليّة (أَبْحَرَتِ، أَثْمَرَتِ) : regarde la racine — verbe → factitif, nom de chose → devenir, nom de lieu → entrer
- **EN** : You read every أَفْعَلَ as causative (أَبْحَرَتِ، أَثْمَرَتِ): check the root — verb → causative, noun of a thing → becoming, place noun → entering
- **Chapitres / piège** : ch05 — piège n°2 « حملُ كلِّ «أَفْعَلَ» على الجعليّةِ لأنّها أشهرُ معانيه. مَن قرأَ «أَثْمَرَتِ الشّجرةُ» على الجعليّةِ اضطُرَّ إ… »
- **Q distinctes** : 2
- **Distracteurs porteurs** :
  - `05:02#2→a` « أَجْلَسَ » — leurres construits sur l'erreur (R1 : « الخطأ الشائع أن يحمل كل أفعل على الجعلية »)
  - `05:02#2→b` « أَفْهَمَ » — leurres construits sur l'erreur (R1 : « الخطأ الشائع أن يحمل كل أفعل على الجعلية »)
  - `05:05#1→b` « الجعليّةُ: جعلتِ السّفينةُ غيرَها يقومُ بالإبحارِ » — R1 : « الجعلية تحتاج جذر فعل »

#### `arabe.mazid.fa33ala-takthir-aw-ja3liyya` — NEUF

- **AR** : تحملُ كلَّ «فَعَّلَ» على التّكثيرِ أو الجعليّةِ دونَ نظرٍ في المفعولِ: صارَ فاعلًا للجذرِ (فَرَّحَتْني) ← جعليّةٌ، ووقعَ عليه كثيرًا (كَسَّرَ) ← تكثيرٌ
- **FR** : Tu lis tout فَعَّلَ comme تكثير ou جعليّة sans regarder l'objet : sujet de la racine (فَرَّحَتْني) → جعليّة ; il la subit souvent (كَسَّرَ) → تكثير
- **EN** : You read every فَعَّلَ as intensive/causative ignoring the object: it becomes the root's subject (فَرَّحَتْني) → causative; it suffers it (كَسَّرَ) → intensive
- **Chapitres / piège** : ch05 — piège n°3 « قراءةُ كلِّ فعلٍ مضعَّفِ العينِ على التّكثيرِ لأنّه أشهرُ معاني التّضعيفِ. مَن قال إنّ «فَرَّحَتْني الهديّةُ» … »
- **Q distinctes** : 2
- **Distracteurs porteurs** :
  - `05:01#4→a` « المبالغةُ والتّكثيرُ » — R1 (paraphrase de l'explication) :  المبالغة تكون حين يقع فعل الجذر على المفعول 
  - `05:02#3→b` « الجعليّةُ: جعلَ الولدُ الصّحنَ يقومُ بالكسرِ » — R1 (paraphrase de l'explication) :  الخطأ الشائع أن يحمل كل تضعيف على الجعلية أو التكثير 

#### `arabe.mazid.if3alla-if3aalla-khalt` — NEUF

- **AR** : تخلطُ بين «افْعَلَّ» (احْمَرَّ: عنصرانِ) و«افْعَالَّ» (احْمَارَّ: ثلاثةُ عناصرَ): الألفُ الطّويلةُ عنصرٌ ثالثٌ يغيّرُ الوزنَ
- **FR** : Tu confonds افْعَلَّ (احْمَرَّ : 2 éléments) et افْعَالَّ (احْمَارَّ، اصْفَارَّ : 3 éléments) : l'alif long est un troisième élément qui change le schème
- **EN** : You confuse افْعَلَّ (احْمَرَّ: 2 elements) with افْعَالَّ (احْمَارَّ، اصْفَارَّ: 3 elements): the long alif is a third element that changes the pattern
- **Chapitres / piège** : ch05 — piège n°9 « وزنُ «اصْفَارَّ» بـ«افْعَلَّ» لأنّ فيه تضعيفًا في آخرِه كما في «اصْفَرَّ». ويُغري بذلك أنّ الفعلينِ يتّفقانِ ف… »
- **Q distinctes** : 2
- **Distracteurs porteurs** :
  - `05:01#3→c` « ثلاثةُ عناصرَ: الهمزةُ والألفُ وتضعيفُ الرّاءِ » — R1 : « ثلاثة العناصر بالألف الطويلة هي احْمارَّ »
  - `05:04#3→b` « افْعَلَّ: عنصرانِ » — R1 (paraphrase de l'explication) :  يغري بافعلّ … ويكتفى بالتضعيف دون عد الألف 

#### `arabe.mazid.istaf3ala-talab-daiman` — NEUF

- **AR** : تحملُ كلَّ «اسْتَفْعَلَ» على الطّلبِ (اسْتَحْسَنَ، اسْتَأْسَدَ، اسْتَحْجَرَ): الطّلبُ يحتاجُ مَن يُطلَبُ منه شيءٌ، وإلّا فاعتبارٌ أو تشبّهٌ أو تحوّلٌ
- **FR** : Tu lis tout اسْتَفْعَلَ comme طلب (اسْتَحْسَنَ، اسْتَأْسَدَ، اسْتَحْجَرَ) : le طلب suppose quelqu'un à qui l'on demande ; sinon jugement, imitation, changement
- **EN** : You read every اسْتَفْعَلَ as asking (اسْتَحْسَنَ، اسْتَأْسَدَ، اسْتَحْجَرَ): asking needs someone to ask; otherwise it is judging, imitating or changing state
- **Chapitres / piège** : ch05 — piège n°10 « حملُ كلِّ «اسْتَفْعَلَ» على الطّلبِ لأنّه أشهرُ معانيه. مَن قال في «اسْتَحْسَنَ المعلّمُ الجوابَ» إنّه طلبَ ال… »
- **Q distinctes** : 3
- **Distracteurs porteurs** :
  - `05:02#5→a` « الطّلبُ: طلبَ الحُسنَ من التّلميذِ » — R1 : « الطلب هو الخطأ الشائع مع اسْتَفْعَلَ »
  - `05:04#1→a` « اسْتَغْفَرَ » — leurre construit sur l'erreur
  - `05:06#1→a` « الطّلبُ: طلبَ الطّينُ الحجرَ من غيرِه » — R1 : « الخطأ الشائع أن يحمل كل اسْتَفْعَلَ على الطلب »

#### `arabe.mazid.ma3na-bila-nazar-fil-jidhr` — NEUF

- **AR** : تختارُ معنى الوزنِ دونَ النّظرِ في الجذرِ: فعلٌ أو اسمُ شيءٍ أو مكانٌ أو لونٌ أو صفةٌ، وكلٌّ منها يعطي الوزنَ الواحدَ معنًى مختلفًا
- **FR** : Tu choisis le sens du schème sans regarder la racine : verbe, nom de chose, lieu, couleur ou qualité donnent chacun un sens différent au même schème
- **EN** : You pick a pattern's meaning without checking the root: a verb, a thing, a place, a colour or a quality each give the same pattern a different meaning
- **Chapitres / piège** : ch05 — (pas de piège ; erreur récurrente dans les items)
- **Q distinctes** : 16
- **Distracteurs porteurs** :
  - `05:quiz#3→a` « الصّيرورةُ » — R1 (paraphrase de l'explication) :  ولا صيرورة لأن الجذر فعل … ولا دخول لأنه ليس مكانًا 
  - `05:quiz#3→d` « الدّخولُ في المكانِ » — R1 (paraphrase de l'explication) :  ولا صيرورة لأن الجذر فعل … ولا دخول لأنه ليس مكانًا 
  - `05:quiz#4→a` « اعتبارُ الشّيءِ على صفةٍ »
  - `05:quiz#4→b` « التّشبّهُ بالشّيءِ »
  - `05:01#2→b` « كَسَّرَ » — R1 : « الذي يفرّق بينها نوع الجذر »
  - `05:01#2→c` « عَلَّمَ » — R1 : « الذي يفرّق بينها نوع الجذر »
  - `05:01#2→d` « سَبَّحَ » — R1 : « الذي يفرّق بينها نوع الجذر »
  - `05:01#4→b` « الاتّجاهُ في المكانِ » — R1 : « ولا جهة في الجذر … ولا عبارة مألوفة »
  - `05:01#4→d` « اختصارُ عبارةٍ » — R1 : « ولا جهة في الجذر … ولا عبارة مألوفة »
  - `05:01#6→a` « الجعليّةُ: جعلَ الفاعلُ غيرَه يقومُ بما في الجذرِ »
  - `05:01#6→d` « الطّلبُ: طلبَ الفاعلُ شيئًا من فاعلٍ آخرَ »
  - `05:02#2→c` « أَبْحَرَ »
  - `05:02#3→c` « الاتّجاهُ في المكانِ: اتّجهَ الولدُ نحوَ الصّحنِ »
  - `05:02#3→d` « اختصارُ عبارةٍ: قالَ الولدُ بهذا الفعلِ عبارةً مألوفةً »
  - `05:02#5→b` « التّحوّلُ من صفةٍ إلى أخرى: صارَ الجوابُ حسنًا »
  - `05:02#5→d` « التّشبّهُ بالشّيءِ: تشبّهَ المعلّمُ بالحُسنِ »
  - `05:02#6→c` « المشاركةُ: شاركَ الصّيّادُ غيرَه في شيِّ السّمكةِ »
  - `05:02#6→d` « الطّلبُ: طلبَ الصّيّادُ من غيرِه أن يشويَ السّمكةَ »
  - `05:04#1→c` « اسْتَصْغَرَ » — R1 : استصغر/استعظم = اعتبار
  - `05:04#1→d` « اسْتَعْظَمَ » — R1 : استصغر/استعظم = اعتبار
  - `05:05#1→c` « الصّيرورةُ: صارتِ السّفينةُ ذاتَ بحرٍ كثيرٍ »
  - `05:05#2→a` « تَجَلَّدَ المريضُ أمامَ أهلِهِ » — R1 : « يفرّق بينها الجذر »
  - `05:05#2→b` « تَحَجَّرَ الطّينُ تحتَ الشّمسِ » — R1 : « يفرّق بينها الجذر »
  - `05:05#2→d` « تَجَرَّعَ المريضُ الدّواءَ كلَّ صباحٍ » — R1 : « يفرّق بينها الجذر »
  - `05:05#3→a` « الانتسابُ إلى مذهبٍ أو دينٍ »
  - `05:05#3→b` « اتّخاذُ الفاعلِ المفعولَ لنفسِه »
  - `05:05#4→c` « الجعليّةُ: جعلَ الجنديُّ غيرَه يقومُ بالفعلِ »
  - `05:05#4→d` « الطّلبُ: طلبَ الجنديُّ شيئًا من غيرِه »
  - `05:06#1→c` « اعتبارُ الشّيءِ على صفةٍ: وجدَ الطّينَ حجرًا »
  - `05:06#2→a` « تَصَبَّرَ المريضُ على الألمِ ليلةً كاملةً » — R1 : « لا يفرَّق بين الجذر الاسمي والجذر الفعلي »
  - `05:06#2→b` « تَوَسَّدَ الرّاعي ذراعَهُ ونامَ تحتَ الشّجرةِ » — R1 : « لا يفرَّق بين الجذر الاسمي والجذر الفعلي »
  - `05:06#2→c` « تَرَشَّفَ الجدُّ قهوتَهُ صباحَ كلِّ يومٍ » — R1 : « لا يفرَّق بين الجذر الاسمي والجذر الفعلي »

#### `arabe.mazid.min-nafs-al-jidhr-dun-ma3na` — NEUF

- **AR** : تختارُ فعلًا أو كلمةً من الجذرِ نفسِه قبلَ أن تسمّيَ المعنى المطلوبَ (أَمْرَضَ، مَرَّضَ بدلَ تَمارَضَ): لكلِّ وزنٍ معانيه، فسمِّ المعنى أوّلًا
- **FR** : Tu choisis un verbe ou un mot de la même racine avant de nommer le sens demandé (أَمْرَضَ، مَرَّضَ au lieu de تَمارَضَ) : nomme d'abord le sens du schème
- **EN** : You pick a verb or word from the same root before naming the required meaning (أَمْرَضَ، مَرَّضَ instead of تَمارَضَ): name the sense first
- **Chapitres / piège** : ch05 — (pas de piège ; erreur récurrente dans les items)
- **Q distinctes** : 4
- **Distracteurs porteurs** :
  - `05:04#2→a` « أَكْبَرَ » — R1 : « ينظر إلى الجذر وحده فتعد الأفعال الأربعة مترادفة »
  - `05:04#2→b` « تَكَبَّرَ » — R1 : « ينظر إلى الجذر وحده فتعد الأفعال الأربعة مترادفة »
  - `05:04#2→c` « اسْتَكْبَرَ » — R1 : « ينظر إلى الجذر وحده فتعد الأفعال الأربعة مترادفة »
  - `05:04#5→a` « مَرِضَ سامي » — R1 (paraphrase de l'explication) :  يختار وزن الهمزة أو التضعيف دون تسمية المعنى أولًا 
  - `05:04#5→b` « أَمْرَضَ سامي نفسَهُ » — R1 (paraphrase de l'explication) :  يختار وزن الهمزة أو التضعيف دون تسمية المعنى أولًا 
  - `05:04#5→c` « مَرَّضَ سامي نفسَهُ » — R1 (paraphrase de l'explication) :  يختار وزن الهمزة أو التضعيف دون تسمية المعنى أولًا 
  - `05:04#6→a` « مَغْفِرَةُ اللهِ الواسعةُ للعبدِ » — R1 : « كل كلمة من الجذر نفسه تحمل معنى الزيادة »
  - `05:04#6→c` « غُفْرانُ اللهِ للذّنبِ العظيمِ » — R1 : « كل كلمة من الجذر نفسه تحمل معنى الزيادة »
  - `05:04#6→d` « غَفُورٌ رحيمٌ بالعبادِ جميعًا » — R1 : « كل كلمة من الجذر نفسه تحمل معنى الزيادة »
  - `05:06#3→b` « فَهِمْتُ أخي » — R1 : « يختار فعل من الجذر نفسه دون تسمية المعنى »
  - `05:06#3→c` « تَفاهَمْتُ مع أخي » — R1 : « يختار فعل من الجذر نفسه دون تسمية المعنى »
  - `05:06#3→d` « اسْتَفْهَمْتُ أخي » — R1 : « يختار فعل من الجذر نفسه دون تسمية المعنى »

#### `arabe.mazid.mutawa3a-bila-fi3l-sabiq` — NEUF

- **AR** : تحكمُ بالمطاوعةِ دونَ فعلٍ سابقٍ وقعَ على الفاعلِ (تَصَبَّرَ، تَوَسَّدَ، انْبَطَحَ): لا مطاوعةَ بلا «عَلَّمتُه فَتَعَلَّمَ»
- **FR** : Tu conclus à une مطاوعة sans verbe antérieur tombé sur le sujet (تَصَبَّرَ، تَوَسَّدَ، انْبَطَحَ) : pas de مطاوعة sans « عَلَّمتُه فَتَعَلَّمَ »
- **EN** : You call it مطاوعة (undergoing) with no earlier verb that acted on the subject (تَصَبَّرَ، تَوَسَّدَ، انْبَطَحَ): no مطاوعة without « عَلَّمتُه فَتَعَلَّمَ »
- **Chapitres / piège** : ch05 — piège n°4 « حملُ كلِّ «تَفَعَّلَ» على المطاوعةِ لأنّها أشهرُ معانيه. مَن قال في «تَصَبَّرَ المريضُ» إنّه طاوعَ فعلًا وقعَ … » (تَصَبَّرَ); ch05 — piège n°5 « ردُّ كلِّ «تَفَعَّلَ» إلى المطاوعةِ. مَن قال إنّ «تَوَسَّدَ الرّاعي ذراعَهُ» مطاوعةٌ بحثَ عن فعلٍ سابقٍ وقعَ ع… » (تَوَسَّدَ — même erreur que n°4); ch05 — piège n°8 « حملُ كلِّ «انْفَعَلَ» على المطاوعةِ. مَن قال إنّ «انْبَطَحَ الجنديُّ» مطاوعةٌ بحثَ عن فاعلٍ بطحَهُ فلم يجدْ في… » (انْبَطَحَ — même erreur que n°4)
- **Q distinctes** : 7
- **Distracteurs porteurs** :
  - `05:quiz#3→c` « المطاوعةُ »
  - `05:01#6→c` « المطاوعةُ: قبِلَ الفاعلُ أثرَ فعلٍ سابقٍ وقعَ عليه » — R1 : « المطاوعة فعلًا سابقًا وقع على الفاعل »
  - `05:02#4→c` « المطاوعةُ: قبِلَ أثرَ فعلٍ سابقٍ »
  - `05:05#1→d` « المطاوعةُ: قبِلتِ السّفينةُ أثرَ فعلٍ سابقٍ وقعَ عليها » — R1 : « لا فعل سابقًا وقع على السفينة »
  - `05:05#3→c` « المطاوعةُ » — R1 : « المطاوعة تحتاج فعلًا سابقًا »
  - `05:05#4→a` « المطاوعةُ: قبِلَ الجنديُّ أثرَ فعلٍ سابقٍ وقعَ عليه » — R1 : « الخطأ الشائع أن تُرى الفاء فيظن كل فعل بعدها مطاوعة »
  - `05:06#1→d` « المطاوعةُ: قبِلَ الطّينُ أثرَ فعلٍ سابقٍ وقعَ عليه »

#### `arabe.mazid.mutawa3a-ittikhadh-khalt` — NEUF

- **AR** : تخلطُ المطاوعةَ باتّخاذِ المفعولِ لنفسِه (اشْتَوَى الصّيّادُ سمكةً): في المطاوعةِ يقعُ الأثرُ على الفاعلِ، وفي الاتّخاذِ يأخذُ الفاعلُ المفعولَ لنفسِه
- **FR** : Tu confonds مطاوعة et prise de l'objet pour soi (اشْتَوَى الصّيّادُ سمكةً) : en مطاوعة l'effet tombe sur le sujet, en اتّخاذ le sujet prend l'objet pour lui
- **EN** : You confuse مطاوعة with taking the object for oneself (اشْتَوَى الصّيّادُ سمكةً): in مطاوعة the subject undergoes the effect; in اتّخاذ it takes the object
- **Chapitres / piège** : ch05 — piège n°7 « الخلطُ بين المطاوعةِ واتّخاذِ المفعولِ لنفسِه لأنّ الوزنَ واحدٌ. مَن قال إنّ «اشْتَوَى الصّيّادُ سمكةً» مطاوعة… »
- **Q distinctes** : 1
- **Distracteurs porteurs** :
  - `05:02#6→b` « المطاوعةُ: قبِلَ الصّيّادُ أثرَ فعلٍ سابقٍ وقعَ عليه » — R1 : « خلط شائع بين الاتخاذ والمطاوعة »

#### `arabe.mazid.tad3if-laysa-ziyada` — NEUF

- **AR** : تعدُّ التّضعيفَ علامةَ نُطقٍ لا زيادةً (احْمَرَّ: عنصرٌ واحدٌ): هو عنصرُ زيادةٍ كالحرفِ، فللفعلِ عنصرانِ: الهمزةُ وتضعيفُ الرّاءِ
- **FR** : Tu comptes la chadda comme une marque de prononciation, pas un ajout (احْمَرَّ : un seul élément) : c'est un élément ; il y en a donc deux : hamza et chadda
- **EN** : You count the doubling as a pronunciation mark, not an addition (احْمَرَّ: one element): it is an element, so there are two: the hamza and the doubling
- **Chapitres / piège** : ch05 — piège n°1 « عدُّ التّضعيفِ علامةَ نُطقٍ لا زيادةً، فيُقالُ إنّ «احْمَرَّ» فيه عنصرٌ واحدٌ هو الهمزةُ. ويُغري بذلك أنّ التّ… » (la 2ᵉ erreur du bloc (nommer la lettre doublée par sa place dans le mot et non dans la racine) n'a pas d'id : aucun distracteur)
- **Q distinctes** : 2
- **Distracteurs porteurs** :
  - `05:quiz#2→b` « كَتَّبَ » — R1 : « فلا يُظنُّ كَتَّبَ مجرَّدًا »
  - `05:01#3→a` « عنصرٌ واحدٌ: الهمزةُ وحدَها » — R1 : « لا يصح أن يحسب للفعل عنصر واحد بإسقاطه »
  - `05:01#3→d` « لا عنصرَ فيه، فهو فعلٌ مجرَّدٌ » — R1 : « لا يصح أن يحسب للفعل عنصر واحد بإسقاطه »

#### `arabe.mazid.tafa3ala-musharaka-daiman` — NEUF

- **AR** : تعدُّ كلَّ «تَفَاعَلَ» مشاركةً لأنّ اللّفظَ يوحي بالتّبادلِ (تَمارَضَ، فَتَباعَدَا): اسألْ كم طرفًا في الفعلِ؛ المشاركةُ طرفانِ يتبادلانِ
- **FR** : Tu lis tout تَفَاعَلَ comme مشاركة parce que la forme évoque l'échange (تَمارَضَ، فَتَباعَدَا) : combien de parties ? La مشاركة en suppose deux qui échangent
- **EN** : You read every تَفَاعَلَ as mutual action because the form suggests exchange (تَمارَضَ، فَتَباعَدَا): how many parties? Mutual action needs two exchanging
- **Chapitres / piège** : ch05 — piège n°6 « تعميمُ المشاركةِ على كلِّ «تَفَاعَلَ» لأنّ لفظَ التّفاعلِ يُوحي بالتّبادلِ. مَن قال في «تَمارَضَ التّلميذُ» إن… »
- **Q distinctes** : 3
- **Distracteurs porteurs** :
  - `05:quiz#5→c` « تَمارَضَ التّلميذُ ليتغيّبَ » — R1 : « تمارض تظاهر بطرف واحد »
  - `05:02#4→a` « المشاركةُ: شاركَ غيرَه في المرضِ » — R1 : « المشاركة … هي الخطأ الشائع مع تَفَاعَلَ »
  - `05:06#4→a` « مشاركةٌ في «فَتَباعَدَا»، ومشاركةٌ في «تَباعَدَ الصّديقانِ»، لأنّ الفا… » — R1 : « عدد الفاعلين »

#### `arabe.mazid.wazn-ma3na-wahid` — NEUF

- **AR** : تقرأُ الجدولَ قاموسًا يعطي كلَّ وزنٍ معنًى واحدًا (تَفَاعَلَ مشاركةٌ دائمًا): هو قائمةُ ما يجوزُ، يختارُ منها الجذرُ ويحسمُ السّياقُ
- **FR** : Tu lis le tableau comme un dictionnaire à un sens par schème (تَفَاعَلَ = toujours مشاركة) : c'est une liste de possibles ; racine et contexte tranchent
- **EN** : You read the table as a dictionary with one meaning per pattern (تَفَاعَلَ = always mutual): it lists possibilities; the root chooses and context decides
- **Chapitres / piège** : ch05 — piège n°12 « الجوابُ من الوزنِ وحدَه، بأوّلِ معنًى يخطرُ على البالِ. مَن سُئلَ عن «تَباعَدَ» فقال «مشاركةٌ» دائمًا، أو «مطا… »
- **Q distinctes** : 4
- **Distracteurs porteurs** :
  - `05:quiz#1→d` « معنى الوزنِ وحدَه دونَ النّظرِ إلى الجذرِ » — R1 : « قراءة الوزن وحده هي الخطأ الشائع »
  - `05:05#6→a` « فَاعَلَ » — R1 : « قراءة عمود واحد من الجدول »
  - `05:05#6→b` « تَفَعَّلَ » — R1 : « قراءة عمود واحد من الجدول »
  - `05:05#6→d` « انْفَعَلَ » — R1 : « قراءة عمود واحد من الجدول »
  - `05:06#4→c` « مطاوعةٌ في «فَتَباعَدَا»، ومطاوعةٌ في «تَباعَدَ الصّديقانِ»، لأنّ الوز… » — R1 : « الوزن واحد »
  - `05:06#6→a` « «افْتَعَلَ» لا يُفيدُ المشاركةَ في أيِّ فعلٍ من أفعالِه » — R1 : « أن يُحمل الوزن على معنى واحد »
  - `05:06#6→b` « «افْتَعَلَ» يُفيدُ المطاوعةَ وحدَها في جميعِ أفعالِه » — R1 : « أن يُحمل الوزن على معنى واحد »
  - `05:06#6→c` « المشاركةُ لا تكونُ إلّا في وزنِ «فَاعَلَ» وحدَه » — R1 : « أن يُحمل الوزن على معنى واحد »

#### `arabe.mazid.wazn-qarib-khalt` — NEUF

- **AR** : تأخذُ وزنَ فعلٍ مجاورٍ في الجدولِ (افْتَعَلَ بدلَ اسْتَفْعَلَ، انْفَعَلَ بدلَ افْعَوْعَلَ): افصلِ الجذرَ عن عناصرِ الزّيادةِ كلِّها
- **FR** : Tu prends le schème d'un verbe voisin du tableau (افْتَعَلَ pour اسْتَفْعَلَ، انْفَعَلَ pour افْعَوْعَلَ) : sépare la racine de TOUS les éléments ajoutés
- **EN** : You take the pattern of a neighbouring verb in the table (افْتَعَلَ for اسْتَفْعَلَ، انْفَعَلَ for افْعَوْعَلَ): separate the root from ALL the added elements
- **Chapitres / piège** : ch05 — (pas de piège ; erreur récurrente dans les items)
- **Q distinctes** : 4
- **Distracteurs porteurs** :
  - `05:01#1→a` « الهمزةُ والتّاءُ » — R1 : عناصر افتعل / تفاعل / استفعل
  - `05:01#1→b` « التّاءُ والألفُ » — R1 : عناصر افتعل / تفاعل / استفعل
  - `05:01#1→c` « الهمزةُ والسّينُ والتّاءُ » — R1 : عناصر افتعل / تفاعل / استفعل
  - `05:02#1→a` « افْتَعَلَ، لأنّ فيه الهمزةَ في أوّلِه والتّاءَ بعدَ الفاءِ » — R1
  - `05:02#1→b` « أَفْعَلَ، لأنّ فيه الهمزةَ وحدَها في أوّلِه دونَ زيادةٍ أخرى » — R1
  - `05:02#1→d` « انْفَعَلَ، لأنّ فيه الهمزةَ في أوّلِه والنّونَ بعدَها » — R1
  - `05:04#3→c` « افْعَوْعَلَ: ثلاثةُ عناصرَ »
  - `05:04#3→d` « اسْتَفْعَلَ: ثلاثةُ عناصرَ »
  - `05:06#5→a` « افْعَلَّ: الاتّصافُ بلونٍ، أي صارتِ الأرضُ خضراءَ » — R1 : « توزن الكلمة بشكلها العام دون عد العناصر »
  - `05:06#5→b` « اسْتَفْعَلَ: الطّلبُ، أي طلبتِ الأرضُ العُشبَ » — R1 : « توزن الكلمة بشكلها العام دون عد العناصر »
  - `05:06#5→d` « افْتَعَلَ: المطاوعةُ، أي قبِلتِ الأرضُ أثرَ المطرِ » — R1 : « توزن الكلمة بشكلها العام دون عد العناصر »

### Domaine `nawasikh`

#### `arabe.nawasikh.ism-khabar-maqlub` — RÉUTILISÉ (REGISTRE)

- **AR** : تخلطُ بينَ اسمِ النّاسخِ وخبرِه: الخبرُ المتقدّمُ هو الجارُّ والمجرورُ أو الظّرف (في البيتِ، عندي)، والاسمُ هو النّكرةُ بعدَه
- **FR** : Tu confonds le nom et le خبر de l'opérateur : le خبر avancé est le groupe (في البيت، عندي), le nom est le nom indéfini qui suit
- **Chapitres / piège** : ch11 — (pas de piège ; erreur récurrente dans les items)
- **Q distinctes** : 2
- **Distracteurs porteurs** :
  - `11:quiz#4→b` « «الفنونَ» خبر إنّ مرفوع بالضمّة » — R1 : « (b) و(c) عكسا الموقعين »
  - `11:quiz#4→c` « «غذاءُ» اسم إنّ مرفوع بالضمّة » — R1 : « (b) و(c) عكسا الموقعين »
  - `11:03#2→b` « خبر «إنّ» مرفوع بالضمّة »

#### `arabe.nawasikh.mubtada-ba3d-nasikh` — RÉUTILISÉ (REGISTRE)

- **AR** : تسمّي الاسمَ «مبتدأً» بعدَ دخولِ النّاسخ (ليسَ، كانَ، صارَ…): بعدَ النّاسخِ نقولُ اسمَ النّاسخِ وخبرَ النّاسخ
- **FR** : Tu gardes le nom « مبتدأ » après un opérateur (ليس، كان، صار…) : on dit اسم النّاسخ et خبر النّاسخ
- **Chapitres / piège** : ch11 — (pas de piège ; erreur récurrente dans les items)
- **Q distinctes** : 1
- **Distracteurs porteurs** :
  - `11:03#2→c` « مبتدأ مرفوع بالضمّة » — R1 : « دخل عليها الناسخ فأبطل الابتداء »

### Domaine `nisba`

#### `arabe.nisba.fa3ila-fath-ma-qabl` — NEUF

- **AR** : لا تفتحُ ما قبلَ الياءِ في «فَعِيلة» (مَدْنيّ، قَبْليّ، مَدينيّ): تسقطُ التّاءُ والياءُ معًا ويُفتحُ ما قبلَهما: مَدَنيّ، قَبَليّ
- **FR** : Tu n'ouvres pas la lettre devant la ي dans un nom en فَعِيلة (مَدْنيّ، قَبْليّ، مَدينيّ) : ة et ي tombent ensemble, la lettre prend fatha : مَدَنيّ، قَبَليّ
- **EN** : You don't open the letter before the ي in a فَعِيلة noun (مَدْنيّ، قَبْليّ، مَدينيّ): ة and ي both drop and the letter takes fatha: مَدَنيّ، قَبَليّ
- **Chapitres / piège** : ch14 — piège n°2 « الاكتفاءُ بحذفِ التاءِ في «فَعِيلة»: «مدينيّ» و«قبيليّ»، فتتوالى ياءانِ وكسرتانِ ويثقلُ اللفظُ. والأفصحُ على ق… » (aucun distracteur n'offre « مَدينيّ / قَبيليّ » (ياء gardée) ; seule la variante soukoun (مَدْنيّ، قَبْليّ) existe)
- **Q distinctes** : 2
- **Distracteurs porteurs** :
  - `14:04#5→d` « قَبْليّ » — R1 : « قَبْليّ يُسكّن الباء »
  - `14:05#2→c` « مَدْنيّ » — R1 : « مَدْنيّ يُسكّن الدال ولا يجري على الوزن »

#### `arabe.nisba.idafa-bada-al-na3t` — NEUF

- **AR** : تُبقي المضافَ إليه بدلَ أن تصوغَ منه نعتًا (أعمدةُ الرّخامِ، فلسفةُ العلومِ): المطلوبُ نعتٌ منسوبٌ مطابقٌ: أعمدةٌ رُخاميّةٌ
- **FR** : Tu gardes le complément du nom au lieu d'en faire un adjectif (أعمدةُ الرّخامِ، فلسفةُ العلومِ) : on demande l'adjectif de nisba accordé : أعمدةٌ رُخاميّةٌ
- **EN** : You keep the genitive complement instead of making an adjective (أعمدةُ الرّخامِ، فلسفةُ العلومِ): an agreeing nisba adjective is needed: أعمدةٌ رُخاميّةٌ
- **Chapitres / piège** : ch14 — (pas de piège ; erreur récurrente dans les items)
- **Q distinctes** : 4
- **Distracteurs porteurs** :
  - `14:01#6→b` « أعمدةُ الرّخامِ » — R1 : « أعمدة الرخام مركب إضافي لا نعتي »
  - `14:01#6→c` « رُخامُ الأعمدةِ » — R1 : « أعمدة الرخام مركب إضافي لا نعتي »
  - `14:02#6→b` « في فلسفةِ العلومِ » — R1 : « فلسفة العلوم قلب للمعنى »
  - `14:03#5→c` « درسوا هنديّاتِ الكتبِ »
  - `14:03#5→d` « درسوا كتبًا هنديّةً في الهندِ »
  - `14:05#6→c` « في طِبِّ العلومِ »

#### `arabe.nisba.kull-iyya-masdar-sina3i` — NEUF

- **AR** : تعدُّ كلَّ ما انتهى بـ«ـيّة» مصدرًا صناعيًّا (الثّيابُ الدّمشقيّةُ): الفيصلُ الوظيفةُ والمعنى؛ النّسبةُ نعتٌ لمؤنّثٍ ينتسبُ إلى ذاتٍ
- **FR** : Tu prends tout mot en ـيّة pour un masdar sinā'ī (الثّيابُ الدّمشقيّةُ) : fonction et sens décident ; la nisba est l'adjectif d'un féminin tiré d'une entité
- **EN** : You take every ـيّة word for an artificial masdar (الثّيابُ الدّمشقيّةُ): function and meaning decide; a nisba is a feminine adjective from an entity
- **Chapitres / piège** : ch14 — piège n°3 « عدُّ كلِّ ما انتهى بـ«ـيّة» مصدرًا صناعيًّا. «الثّيابُ الدّمشقيّةُ» ليست مصدرًا صناعيًّا: هي نسبةٌ جاءت نعتًا … »
- **Q distinctes** : 2
- **Distracteurs porteurs** :
  - `14:02#5→c` « لا فرقَ بينهما، فكلُّ ما لحقته ـيّة مصدرٌ صناعيٌّ لمعنًى مجرّدٍ » — R1 : « الفيصل في الوظيفة والمعنى لا في اللاحقة »
  - `14:04#4→a` « الأعمدةُ الرّخاميّةُ » — R1 : « الرخاميّة والدمشقيّة والهنديّة … نسب مؤنثة »
  - `14:04#4→b` « الثّيابُ الدّمشقيّةُ » — R1 : « الرخاميّة والدمشقيّة والهنديّة … نسب مؤنثة »
  - `14:04#4→c` « الكتبُ الهنديّةُ » — R1 : « الرخاميّة والدمشقيّة والهنديّة … نسب مؤنثة »

#### `arabe.nisba.mahdhuf-la-yustaradd` — NEUF

- **AR** : لا تردُّ الحرفَ المحذوفَ من الثّلاثيِّ (أَبِّيّ، سَنِّيّ، لِثِّيّ): يُستردُّ قبلَ ياءِ النّسبةِ واوًا: أَبَويّ، سَنَويّ، لِثَويّ
- **FR** : Tu ne rends pas la lettre supprimée du trilitère (أَبِّيّ، سَنِّيّ، لِثِّيّ) : on la restitue en و avant la ي de nisba : أَبَويّ، سَنَويّ، لِثَويّ
- **EN** : You fail to restore the dropped letter of a three-letter noun (أَبِّيّ، سَنِّيّ، لِثِّيّ): it returns as و before the nisba ي: أَبَويّ، سَنَويّ، لِثَويّ
- **Chapitres / piège** : ch14 — piège n°1 « إلصاقُ الياءِ بالاسمِ كما هو: «فاطمةيّ» أو «أبِيّ». التاءُ تسقطُ وجوبًا، والثلاثيُّ المحذوفُ الآخِرِ يستردُّ م… » (deux gestes dans le même bloc : garder la ة, ne pas rendre le محذوف)
- **Q distinctes** : 3
- **Distracteurs porteurs** :
  - `14:01#4→a` « أَبِّيّ »
  - `14:01#4→d` « آبيّ »
  - `14:02#1→c` « سِنِّيّ »
  - `14:04#1→b` « لِثّيّ »

#### `arabe.nisba.mamdud-wa-mahdhuf-khalt` — NEUF

- **AR** : تخلطُ بين الممدودِ (سماء ← سَماويّ أو سَمائيّ) والثّلاثيِّ المحذوفِ الآخِرِ (يَد ← يَدَويّ): الأوّلُ يُبقي المدَّ، والثّاني يردُّ المحذوفَ واوًا
- **FR** : Tu confonds le mamdud (سماء → سَماويّ/سَمائيّ) et le trilitère à lettre supprimée (يَد → يَدَويّ) : le premier garde le مدّ, le second restitue la و
- **EN** : You mix the mamdud (سماء → سَماويّ/سَمائيّ) with the three-letter noun that lost a letter (يَد → يَدَويّ): the first keeps the madd, the second restores the و
- **Chapitres / piège** : ch14 — (pas de piège ; erreur récurrente dans les items)
- **Q distinctes** : 5
- **Distracteurs porteurs** :
  - `14:01#4→c` « أبَائيّ »
  - `14:02#1→d` « سَنائيّ »
  - `14:02#2→a` « سَمَويّ » — R1 : « يعامل الممدود معاملة الثلاثي المحذوف الآخر … »
  - `14:02#2→b` « سَمَيّ » — R1 : « يعامل الممدود معاملة الثلاثي المحذوف الآخر … »
  - `14:02#2→c` « سَماءَويّ » — R1 : « يعامل الممدود معاملة الثلاثي المحذوف الآخر … »
  - `14:03#3→a` « يَداويّ » — R1 : « يعاملان يد معاملة الممدود »
  - `14:03#3→c` « يِدائيّ » — R1 : « يعاملان يد معاملة الممدود »
  - `14:04#1→c` « لِثائيّ »

#### `arabe.nisba.masdar-sina3i-nisba-khalt` — NEUF

- **AR** : تخلطُ بين النّسبةِ (صفةٌ بياءٍ مضاعفةٍ: حُرّيّ، كَيْفيّ) والمصدرِ الصّناعيِّ (معنًى مجرّدٌ بـ«ـيّة»: حُرّيّة، كيفيّة)
- **FR** : Tu confonds la nisba (adjectif en ـيّ : حُرّيّ، كَيْفيّ) et le masdar sinā'ī (idée abstraite en ـيّة : حُرّيّة، كيفيّة)
- **EN** : You confuse the nisba (adjective in ـيّ: حُرّيّ، كَيْفيّ) with the artificial masdar (abstract idea in ـيّة: حُرّيّة، كيفيّة)
- **Chapitres / piège** : ch14 — (pas de piège ; erreur récurrente dans les items)
- **Q distinctes** : 6
- **Distracteurs porteurs** :
  - `14:quiz#1→b` « صيغةٌ صرفيّةٌ تدلُّ على معنًى مجرّدٍ قائمٍ بنفسِه لا بغيرِه »
  - `14:quiz#4→c` « صفةٌ منسوبةٌ إلى صناعةٍ أو حِرفةٍ، ويدلُّ على من يمارسُها في المدينةِ » — R1 : « ليس منسوبًا إلى صناعة »
  - `14:01#5→a` « حُرّيّ » — R1 : « حُرّيّ صفة نسبة »
  - `14:02#5→a` « الأولى مصدرٌ صناعيٌّ لمعنًى مجرّدٍ، والثّانيةُ نسبةٌ مؤنّثةٌ نعتٌ »
  - `14:03#4→c` « موضوعيّ » — R1 : « موضوعيّ صفة نسبة »
  - `14:05#5→c` « كَيْفيّ، ويدلُّ على صفةِ انتسابٍ » — R1 (paraphrase de l'explication) :  كَيْفيّ صفة انتساب 

#### `arabe.nisba.min-kalima-ukhra` — NEUF

- **AR** : تنسبُ إلى كلمةٍ غيرِ المعطاةِ (الطّبيبيّة من الطّبّ، وضعيّ من موضوع): انسبْ إلى الاسمِ المطلوبِ نفسِه لا إلى جمعِه ولا إلى مشتقٍّ منه
- **FR** : Tu fais la nisba d'un autre mot que celui donné (الطّبيبيّة pour الطّبّ، وضعيّ pour موضوع) : prends le nom demandé lui-même, pas son pluriel ni un dérivé
- **EN** : You derive the nisba from another word than the one given (الطّبيبيّة for الطّبّ, وضعيّ for موضوع): use the given noun itself, not its plural or a derivative
- **Chapitres / piège** : ch14 — (pas de piège ; erreur récurrente dans les items)
- **Q distinctes** : 3
- **Distracteurs porteurs** :
  - `14:02#6→c` « في العلومِ الفلاسفيّةِ »
  - `14:03#4→a` « موضوعاتيّ » — R1 (paraphrase de l'explication) :  نسبة إلى الجمع / إلى وَضْع 
  - `14:03#4→d` « وضعيّ » — R1 (paraphrase de l'explication) :  نسبة إلى الجمع / إلى وَضْع 
  - `14:05#6→b` « في العلومِ الطّبيبيّةِ » — R1 : « النسبة إلى الطبيب تغيّر المعنى »

#### `arabe.nisba.mutabaqa-na3t` — NEUF

- **AR** : لا تُطابقُ صفةَ النّسبةِ منعوتَها في النّوعِ أو الإعرابِ (ثوبٌ حريريّةٌ، الكتبَ الهنديّةِ): تتبعُه تذكيرًا وتأنيثًا وتعريفًا وحركةً
- **FR** : Tu n'accordes pas l'adjectif de nisba à son nom en genre ou en cas (ثوبٌ حريريّةٌ، الكتبَ الهنديّةِ) : il suit son nom en genre, définition et cas
- **EN** : You don't make the nisba adjective agree with its noun in gender or case (ثوبٌ حريريّةٌ، الكتبَ الهنديّةِ): it follows the noun in gender, definiteness and case
- **Chapitres / piège** : ch14 — (pas de piège ; erreur récurrente dans les items)
- **Q distinctes** : 7
- **Distracteurs porteurs** :
  - `14:quiz#3→d` « فاطميّة » — R1 (paraphrase de l'explication) :  مؤنثة لا تكون نعتًا لعهد المذكر 
  - `14:01#1→d` « كُوفيّة » — R1 (paraphrase de l'explication) :  كوفيّة مؤنثة لا تكون نعتًا لخطّ 
  - `14:01#3→b` « حريريّة » — R1 (paraphrase de l'explication) :  حريريّة للمؤنث لا لثوب 
  - `14:01#6→d` « أعمدةٌ رُخاميّةً »
  - `14:02#6→a` « في العلومِ الفلسفيّةَ » — R1 (paraphrase de l'explication) :  يطابق منعوته في الجرّ 
  - `14:03#5→b` « درسوا الكتبَ الهنديّةِ » — R1 : « جرّ النعت مع نصب المنعوت خطأ مطابقة »
  - `14:05#6→d` « في العلومِ الطِّبّيّةَ » — R1 : « نصب النعت مع جرّ المنعوت خطأ مطابقة »

#### `arabe.nisba.radd-waw-bila-mahdhuf` — NEUF

- **AR** : تردُّ واوًا إلى اسمٍ لم يُحذفْ منه شيءٌ (كُوفَويّ، بَصْرَويّ، فاطِمويّ): الواوُ لا تُستردُّ إلّا في الثّلاثيِّ المحذوفِ الآخِرِ (أَبَويّ)
- **FR** : Tu ajoutes une و à un nom qui n'a rien perdu (كُوفَويّ، بَصْرَويّ، فاطِمويّ) : la و ne revient que dans le trilitère à lettre supprimée (أَبَويّ)
- **EN** : You add a و to a noun that lost nothing (كُوفَويّ، بَصْرَويّ، فاطِمويّ): the و is restored only in a three-letter noun with a dropped letter (أَبَويّ)
- **Chapitres / piège** : ch14 — (pas de piège ; erreur récurrente dans les items)
- **Q distinctes** : 4
- **Distracteurs porteurs** :
  - `14:quiz#3→c` « فاطِمويّ » — R1 (paraphrase de l'explication) :  ردّ المحذوف واوًا في الثلاثي المحذوف الآخر وحده 
  - `14:01#1→a` « كُوفَويّ » — R1
  - `14:01#3→a` « حَرَويّ »
  - `14:03#2→b` « بَصْرَويّ » — R1

#### `arabe.nisba.ta2-tubqa` — NEUF

- **AR** : تُبقي تاءَ التّأنيثِ قبلَ ياءِ النّسبةِ (فاطمةيّ، كوفةيّ، مدينةيّ): التّاءُ تسقطُ وجوبًا ثمّ تلحقُ الياءُ المضاعفةُ: فاطميّ، كوفيّ
- **FR** : Tu gardes la ة du féminin devant la ي de nisba (فاطمةيّ، كوفةيّ، مدينةيّ) : elle tombe obligatoirement, puis vient la ي doublée : فاطميّ، كوفيّ
- **EN** : You keep the feminine ة before the nisba ي (فاطمةيّ، كوفةيّ، مدينةيّ): it must drop, then the doubled ي is added: فاطميّ، كوفيّ
- **Chapitres / piège** : ch14 — piège n°1 « إلصاقُ الياءِ بالاسمِ كما هو: «فاطمةيّ» أو «أبِيّ». التاءُ تسقطُ وجوبًا، والثلاثيُّ المحذوفُ الآخِرِ يستردُّ م… » (deux gestes dans le même bloc : garder la ة, ne pas rendre le محذوف)
- **Q distinctes** : 7
- **Distracteurs porteurs** :
  - `14:quiz#3→a` « فاطمةيّ » — R1 : « تاء التأنيث تسقط وجوبًا »
  - `14:01#1→b` « كُوفةيّ » — R1 : « إبقاء التاء لا يجوز »
  - `14:02#1→a` « سَنَتيّ » — R1 (paraphrase de l'explication) :  إبقاء التاء لا يجوز 
  - `14:03#2→c` « بَصْرةيّ »
  - `14:04#1→a` « لِثَتيّ »
  - `14:04#5→a` « قَبيلةيّ » — R1 (paraphrase de l'explication) :  قبيلةيّ يُبقي التاء 
  - `14:05#2→a` « مَدينةيّ » — R1 (paraphrase de l'explication) :  مَدينةيّ يُبقي التاء 

#### `arabe.nisba.tasghir-khalt` — NEUF

- **AR** : تخلطُ النّسبةَ بالتّصغيرِ: ياءُ النّسبةِ مضاعفةٌ في الآخِرِ بعد كسرةٍ، وياءُ التّصغيرِ ساكنةٌ بعد الثّاني (مُدَيْنيّ، قُبَيْليّ ليستا نسبتَينِ)
- **FR** : Tu mêles nisba et diminutif : la ي de nisba est doublée, finale, après kasra ; celle du diminutif est sukûn après la 2ᵉ (مُدَيْنيّ، قُبَيْليّ : pas des nisba)
- **EN** : You mix nisba and diminutive: the nisba ي is doubled, final, after a kasra; the diminutive one is silent after the 2nd letter (مُدَيْنيّ ≠ nisba)
- **Chapitres / piège** : ch14 — (pas de piège ; erreur récurrente dans les items)
- **Q distinctes** : 6
- **Distracteurs porteurs** :
  - `14:quiz#2→a` « من الاسمِ مع ياءٍ ساكنةٍ تُزادُ بعد حرفِه الثّاني مع ضمِّ أوّلِه » — R1 : « الياءُ السّاكنةُ … ياءُ التّصغيرِ »
  - `14:03#1→a` « ياءُ التّصغيرِ » — R1
  - `14:03#2→d` « بُصَيْريّ » — R1 : « بُصَيْريّ فيه تصغير لا موضع له »
  - `14:04#5→b` « قُبَيْليّ » — R1 : « قُبَيْليّ تصغير لا نسبة »
  - `14:05#1→d` « جُرَيْديّ » — R1 : « فيه ياء تصغير لا موضع لها »
  - `14:05#2→b` « مُدَيْنيّ » — R1 : « مُدَيْنيّ تصغير »

#### `arabe.nisba.ya-bi-surat-al-khatt` — NEUF

- **AR** : تحكمُ بالنّسبةِ على الصّورةِ المكتوبةِ (الصّحاري، الكُرسيّ، المتنبّي، الرّاعي): انزعِ الياءَ، فإن بقيَ اسمٌ يُنتسَبُ إليه فهي نسبةٌ وإلّا فلا
- **FR** : Tu juges la nisba d'après l'écriture (الصّحاري، الكُرسيّ، المتنبّي، الرّاعي) : retire la ي ; s'il reste un nom d'attache, c'est une nisba, sinon non
- **EN** : You judge a nisba by its spelling (الصّحاري، الكُرسيّ، المتنبّي، الرّاعي): remove the ي; if a noun to attach to remains, it is a nisba, otherwise not
- **Chapitres / piège** : ch14 — piège n°4 « الحكمُ بالعينِ على الصّورةِ المكتوبةِ. «الصّحاري» و«الكُرسيّ» تنتهيانِ بما يشبهُ ياءَ النّسبةِ، ولا نسبةَ فيهم… »
- **Q distinctes** : 2
- **Distracteurs porteurs** :
  - `14:02#3→b` « المتنبّي، الكُرْسيّ، الصّحاري » — R1 : المتنبي/الراعي/الصحاري/الكرسي
  - `14:02#3→c` « البُخاريّ، الرّاعي، الشّاميّ » — R1 : المتنبي/الراعي/الصحاري/الكرسي
  - `14:02#3→d` « الحَفْصيّون، الصّحاري، الكُرْسيّ » — R1 : المتنبي/الراعي/الصحاري/الكرسي
  - `14:02#4→a` « أن ننظرَ في موقعِها من الجملةِ، فإن كانت فاعلًا فهي نسبةٌ » — R1 : « الإعراب وعدد الحروف لا يفرقان »
  - `14:02#4→b` « أن نعدَّ حروفَها، فإن زادت على أربعةٍ فهي نسبةٌ » — R1 : « الإعراب وعدد الحروف لا يفرقان »
  - `14:02#4→d` « أن نُدخلَ عليها أل، فإن قبلتها فهي نسبةٌ » — R1 : « الإعراب وعدد الحروف لا يفرقان »

### Domaine `sard`

#### `arabe.sard.a3mal-at-tahawwul` — RÉUTILISÉ (REGISTRE)

- **AR** : تجعلُ عملًا يلي الحدثَ الطّارئَ (بحثٌ، مساعدةٌ، حلٌّ) بدايةً أو أوّلَ التّحوّلِ أو نهايةً: هو عملٌ داخلَ سياقِ التّحوّل
- **FR** : Tu places une action qui suit l'événement soudain (chercher, aider, résoudre) au début de l'histoire, du تحوّل ou à la fin : elle est dans le تحوّل
- **Chapitres / piège** : ch09 — (pas de piège ; erreur récurrente dans les items)
- **Q distinctes** : 1
- **Distracteurs porteurs** :
  - `09:05#1→c` « «هبَّ الجيرانُ يحملونَ الدلاءَ» » — R1 : « هبّ الجيران … من سياق التحوّل (محاولة الحل) » — emprunt du registre 6ᵉ

### Domaine `sinf`

#### `arabe.sinf.akhir-khalt` — NEUF

- **AR** : تخلطُ بين أصنافِ الآخِرِ: ألفٌ ثابتةٌ ← مقصورٌ، ياءٌ مسبوقةٌ بكسرٍ ← منقوصٌ، همزةٌ بعد ألفٍ ← ممدودٌ؛ فانظرْ إلى الآخِرِ لا إلى المعنى
- **FR** : Tu confonds les trois fins : alif fixe → maqsur ; ي précédé d'une kasra → manqus ; hamza après alif → mamdud. Regarde la fin du mot, pas son sens
- **EN** : You mix up the three endings: fixed alif → maqsur; ي after a kasra → manqus; hamza after an alif → mamdud. Look at the word's end, not its meaning
- **Chapitres / piège** : ch12 — (pas de piège ; erreur récurrente dans les items)
- **Q distinctes** : 5
- **Distracteurs porteurs** :
  - `12:quiz#1→a` « كلُّ اسمٍ مُعربٍ ينتهي بياءٍ ثابتةٍ مسبوقةٍ بكسرٍ لا تتغيّرُ بتغيّرِ ا… » — R1 : définition de l'autre classe
  - `12:quiz#1→c` « كلُّ اسمٍ مُعربٍ ينتهي بهمزةٍ بعد ألفٍ ثابتةٍ لا تتغيّرُ بتغيّرِ الإعر… » — R1 : définition de l'autre classe
  - `12:01#1→b` « الهُدى »
  - `12:01#1→c` « الجوزاء »
  - `12:01#2→a` « المُرتضى »
  - `12:01#2→b` « السّاعي »
  - `12:03#1→c` « كلُّ اسمٍ مُعربٍ ينتهي بألفٍ ثابتةٍ »
  - `12:03#2→a` « مقصورٍ حُذفت ألفُه عندَ الجمعِ »
  - `12:03#2→c` « ممدودٍ قُلبت همزتُه واوًا عندَ الجمعِ »

#### `arabe.sinf.mabni-ka-mu3rab` — NEUF

- **AR** : تعدُّ اسمًا مبنيًّا (مَتى، هُنا، مَن) مقصورًا أو منقوصًا: الأصنافُ الثّلاثةُ للأسماءِ المُعرَبةِ وحدَها، والمبنيُّ لا يتغيّرُ آخرُه
- **FR** : Tu ranges un nom indéclinable (مَتى، هُنا، مَن) parmi maqsur/manqus/mamdud : ces trois classes ne concernent que les noms déclinables (مُعرَبة)
- **EN** : You file an indeclinable noun (مَتى، هُنا، مَن) under maqsur/manqus/mamdud: those classes are only for declinable (مُعرَب) nouns
- **Chapitres / piège** : ch12 — (pas de piège ; erreur récurrente dans les items)
- **Q distinctes** : 3
- **Distracteurs porteurs** :
  - `12:quiz#1→d` « كلُّ اسمٍ مبنيٍّ ينتهي بألفٍ ثابتةٍ لا تتغيّرُ بتغيّرِ الإعرابِ » — R1 : « مبنيّ » dans la définition
  - `12:01#1→d` « هُنا » — R1 : « هنا ظرف مبنيّ »
  - `12:01#2→c` « مَتى »

### Domaine `sura`

#### `arabe.sura.athar-al-sura-khalt` — NEUF

- **AR** : لا تذكرُ ما أضافتْه الصّورةُ إلى المعنى (حياةً، محسوسيّةً، تأثيرًا) وتعلّلُ بشهرةِ الكاتبِ أو غرابةِ كلمةٍ أو بأنّها تشبيهٌ فحسبُ: اقرأ أثرَها في القارئِ
- **FR** : Tu ne dis pas ce que l'image ajoute au sens (vie, concret, émotion) et invoques la célébrité de l'auteur, un mot rare ou le seul fait d'un تشبيه : lis son effet
- **EN** : You don't say what the image adds (life, concreteness, emotion) and rely on the author's fame, a rare word or the mere fact of a simile: read its effect
- **Chapitres / piège** : ch07 — (pas de piège ; erreur récurrente dans les items)
- **Q distinctes** : 3
- **Distracteurs porteurs** :
  - `07:quiz#5→b` « حوّلتِ الكلامَ إلى وصفٍ لليلِ الطّبيعةِ وظلامِه وحدَه »
  - `07:04#4→d` « بقيَ المشبَّهُ «الرّبيعُ»، ولم تُضفِ الصّورةُ شيئًا إلى القولِ الصّريح… »
  - `07:06#4→a` « أعجبَني لأنّه تشبيهٌ، والتّشبيهُ في كلِّ نصٍّ أجملُ من القولِ الصّريحِ… » — R1 : « ليست تعليلات تُبيّن ما أضافته الصورة »
  - `07:06#4→b` « أعجبَني لأنّ كاتبَه مشهورٌ في بلدِنا، فلا بدَّ أن يكونَ كلامُه جميلًا » — R1 : « ليست تعليلات تُبيّن ما أضافته الصورة »
  - `07:06#4→d` « أعجبَني لأنّ كلمةَ «السّرابِ» غريبةٌ لا يعرفُها إلّا القليلُ » — R1 : « ليست تعليلات تُبيّن ما أضافته الصورة »

#### `arabe.sura.isti3ara-li-ghiyab-al-ada` — NEUF

- **AR** : تحكمُ بالاستعارةِ لأنّ الأداةَ غائبةٌ (العلمُ نورٌ): تُحذفُ في الاستعارةِ الأداةُ وأحدُ الطّرفَين؛ فإن ذُكرَ الطّرفانِ فهو تشبيهٌ
- **FR** : Tu conclus à une استعارة car l'outil manque (العلمُ نورٌ) : dans l'استعارة l'outil ET un terme tombent ; si les deux termes sont là, c'est un تشبيه
- **EN** : You call it a metaphor because the particle is missing (العلمُ نورٌ): in an استعارة the particle AND one term drop; if both terms are present it is a simile
- **Chapitres / piège** : ch07 — piège n°3 « الحكمُ بالاستعارةِ لأنّ الأداةَ غائبةٌ. قال تلميذٌ عن «العلمُ نورٌ»: «استعارةٌ، لأنّه لا كافَ فيها». ويُغري بذ… »
- **Q distinctes** : 6
- **Distracteurs porteurs** :
  - `07:quiz#3→a` « استعارةٌ، لأنّ الأداةَ غائبةٌ فيها وفي وجهِ الشّبَهِ » — R1 : « التشبيه يبقى تشبيهًا ما دام طرفاه معًا »
  - `07:quiz#4→a` « تشبيهٌ حُذفتْ أداتُه ووجهُ شبهِه معًا وبقيَ طرفاهُ كاملَين في الكلامِ » — R1 (paraphrase de l'explication) :  فإن بقي الطرفان فهو تشبيه لا استعارة 
  - `07:02#4→a` « كلتاهما استعارةٌ، لأنّ الأداةَ غائبةٌ فيهما معًا » — R1 : « غياب الأداة وحده لا يصنع استعارة »
  - `07:02#4→c` « «الجنديُّ أسدٌ…» استعارةٌ لغيابِ الأداةِ، و«قاتلَ الأسدُ…» تشبيهٌ لذكر… » — R1 : « غياب الأداة وحده لا يصنع استعارة »
  - `07:05#1→d` « إذا حُذفتْ منها أداةُ التّشبيهِ ووجهُ الشّبَهِ معًا في الجملةِ »
  - `07:05#4→a` « «الدّنيا مدرسةٌ كبيرةٌ لأهلِها» » — R1 : « الطرفان مذكوران والأداة غائبة … تشبيه »
  - `07:05#4→d` « «العلمُ كنزٌ لا يفنى» » — R1 : « الطرفان مذكوران والأداة غائبة … تشبيه »
  - `07:06#2→a` « استعارةٌ لأنّ الأداةَ غائبةٌ، ووجهُ الشّبَهِ التّربيةُ والتّعليمُ؛ وأث… » — R1 : « فهي تشبيه ولو غابت الأداة »

#### `arabe.sura.ma3na-asli-badal-tahlil` — NEUF

- **AR** : تشرحُ المعنى الأصليَّ للكلمةِ بدلَ تحليلِ الصّورةِ («الليلُ وقتٌ بين الغروبِ والفجرِ»): بيِّنْ ما أُريدَ به وما جمعَ الطّرفَين وأثرَها في القارئِ
- **FR** : Tu expliques le sens littéral au lieu d'analyser l'image (« la nuit va du coucher à l'aube ») : dis ce qu'elle désigne, le lien entre les termes, son effet
- **EN** : You explain the literal sense instead of analysing the image ("night runs from sunset to dawn"): say what it stands for, the link between the terms, its effect
- **Chapitres / piège** : ch07 — piège n°4 « شرحُ المعنى الحرفيِّ بدلَ تحليلِ الصّورةِ. قال تلميذٌ عن «ولا بدَّ لليلِ أن ينجلي»: «الليلُ وقتٌ بين الغروبِ و… »
- **Q distinctes** : 1
- **Distracteurs porteurs** :
  - `07:06#3→d` « لا ينقصُه شيءٌ، فقد شرحَ المعنى الأصليَّ شرحًا كاملًا » — R1 : « وصف المعنى الأصلي للّيل ولم يحلّل الصورة »

#### `arabe.sura.majaz-bi-makan-al-kalima` — NEUF

- **AR** : تحكمُ بالمجازِ على كلمةٍ لأنّها في شعرٍ أو لأنّها غريبةٌ (سافرَ الشّاعرُ إلى القيروانِ): الحكمُ بمعنى الكلمةِ في جملتِها لا بنوعِ النّصِّ
- **FR** : Tu juges une parole figurée car elle est dans un poème ou rare (سافرَ الشّاعرُ إلى القيروانِ) : c'est son sens dans la phrase qui décide, non le genre du texte
- **EN** : You call a word figurative because it is in a poem or rare (سافرَ الشّاعرُ إلى القيروانِ): judge by its sense in the sentence, not by the type of text
- **Chapitres / piège** : ch07 — piège n°1 « الحكمُ على الكلمةِ من مكانِها لا من معناها. قال تلميذٌ عن «سافرَ الشّاعرُ إلى القيروانِ» في بيتٍ شعريٍّ: «مجاز… »
- **Q distinctes** : 2
- **Distracteurs porteurs** :
  - `07:05#1→a` « إذا كانتْ غريبةً قديمةً لا يعرفُها أكثرُ القرّاءِ اليومَ ولا يستعملونَ… » — R1 : « ولا لأنّها وردت في شعر »
  - `07:05#1→b` « إذا وردتْ في بيتِ شعرٍ أو في قصيدةٍ طويلةٍ كاملةٍ من القصائدِ » — R1 : « ولا لأنّها وردت في شعر »
  - `07:06#1→c` « الخطأُ أنّ المجازَ هو الكلمةُ الغريبةُ، و«سافرَ» كلمةٌ مألوفةٌ يعرفُها… » — R1 : « ولا أنّ كلّ ما في القصيدة مجاز »
  - `07:06#1→d` « لا خطأَ، فكلُّ ما يردُ في القصيدةِ مجازٌ لأنّ الشّعرَ صورٌ كلُّه من أو… » — R1 : « ولا أنّ كلّ ما في القصيدة مجاز »

#### `arabe.sura.majaz-ka-haqiqa` — NEUF

- **AR** : تعدُّ الاستعمالَ المجازيَّ حقيقةً (ضحكتِ الأرضُ، الصّبرُ مفتاحُ الفرجِ): إن لم يصدرِ الفعلُ في معناه الأصليِّ عن فاعلِه فهو مجازٌ بينه وبين الأصلِ شبهٌ
- **FR** : Tu prends un emploi figuré pour littéral (ضحكتِ الأرضُ، الصّبرُ مفتاحُ الفرجِ) : si le sujet ne peut le faire au sens premier, c'est un majāz
- **EN** : You take a figurative use for literal (ضحكتِ الأرضُ، الصّبرُ مفتاحُ الفرجِ): if the subject can't do it in the first sense, it is figurative
- **Chapitres / piège** : ch07, ch11 — (pas de piège ; erreur récurrente dans les items)
- **Q distinctes** : 6
- **Distracteurs porteurs** :
  - `07:quiz#3→c` « حقيقةٌ، لأنّ الصّبرَ يفتحُ الأبوابَ المغلقةَ فعلًا »
  - `07:01#3→b` « «ضحكتِ الأرضُ بالأزهارِ في الرّبيعِ» » — R1 : « فلا أفواه لها تضحك بها »
  - `07:01#3→c` « «ضحكَ الصّباحُ فوقَ الحقولِ المخضرّةِ الواسعةِ» » — R1 : « فلا أفواه لها تضحك بها »
  - `07:01#3→d` « «ضحكتِ الشّمسُ للمدينةِ بعدَ المطرِ» » — R1 : « فلا أفواه لها تضحك بها »
  - `07:04#5→a` « حقيقةٌ، لأنّ الشّاعرَ يتحدّثُ عن متسلّقي الجبالِ ومشقّةِ الطّريقِ فيها » — R1 : « لم يُستعمل في معناه الحقيقيّ »
  - `07:04#6→d` « «اللّيلةُ الظّلماءُ» و«البدرُ» كلاهما على حقيقتِه، فالشّاعرُ يصفُ ليلة… » — R1 : « وهما مجاز لا حقيقة »
  - `07:06#1→a` « الخطأُ أنّ الشّعرَ لا يكونُ فيه مجازٌ أبدًا، فهو كلامٌ يقولُ الحقائقَ … » — R1 : « وليس صحيحًا أنّ الشعر خالٍ من المجاز » (variante : nier tout majāz)
  - `11:03#4→b` « خبرٌ محضٌ لا مجاز فيه ولا صورة » — R1 : « ليس خبرًا خاليًا من المجاز » (استعارة « يجترّ نفسه حتى يذبل »)

#### `arabe.sura.qalb-al-tarafayn` — NEUF

- **AR** : تقلبُ الطّرفَين: المشبَّهُ هو الموصوفُ الذي يدورُ عليه الكلامُ (أمّي، الجنديُّ)، والمشبَّهُ به ما يُوضَّحُ به (الشّمعةُ، الصّخرةُ) ولو كان أشهرَ بالصّفةِ
- **FR** : Tu inverses les termes : le مشبَّه est le décrit dont on parle (أمّي، الجنديُّ), le مشبَّه به ce qui l'éclaire (الشّمعةُ، الصّخرةُ), même plus célèbre
- **EN** : You swap the terms: the مشبَّه is the described subject (أمّي، الجنديُّ), the مشبَّه به what clarifies it (الشّمعةُ، الصّخرةُ), even if better known
- **Chapitres / piège** : ch07 — piège n°2 « قلبُ الطّرفَين. قال تلميذٌ في «الجنديُّ كالصّخرةِ ثباتًا»: «المشبَّهُ هو الصّخرةُ، لأنّها أشهرُ في الثّباتِ». … »
- **Q distinctes** : 8
- **Distracteurs porteurs** :
  - `07:01#1→a` « خالدٌ »
  - `07:02#1→b` « «أطلَّ بدرٌ كالتّلميذِ حُسنًا من نافذةِ القسمِ» » — R1 : « وقلب الطرفين يجعل البدر هو الموصوف »
  - `07:02#3→b` « المشبَّهُ «السّيفُ»، والمشبَّهُ به «الوقتُ»، والأداةُ الكافُ، ووجهُ ال… » — R1 : « قلب الطرفين »
  - `07:02#6→d` « لا خطأَ، فالمشبَّهُ هو الأشهرُ دائمًا في الصّفةِ المشتركةِ بينهما » — R1 : « قاعدة الأشهر هو المشبّه عكس الصواب »
  - `07:04#2→a` « المشبَّهُ «البنيانُ»، والمشبَّهُ به «المؤمنُ»، والأداةُ الكافُ، ووجهُ … » — R1 : « قلب للطرفين »
  - `07:04#3→d` « تجعلُ الحبيبةَ محاربةً تحملُ سيفًا لامعًا في ساحةِ المعركةِ والدّماءِ » — R1 : « الحبيبة ليست محاربة، فالمشبّه به بارق ثغرها لا هي »
  - `07:06#2→b` « تشبيهٌ مشبَّهُه «المدرسةُ» ومشبَّهُه به «الأمُّ»، ووجهُ الشّبَهِ التّر… »
  - `07:06#6→a` « الأداةُ الكافُ، والمشبَّهُ الجبالُ، والمشبَّهُ به السّفنُ، ووجهُ الشّب… »

#### `arabe.sura.rukn-baqi-khalt` — NEUF

- **AR** : تخطئُ في الطّرفِ الباقي من الاستعارةِ: يبقى المشبَّهُ به (بلبلًا يُنشدُ) أو المشبَّهُ (بكتِ الغيومُ) ويُحذفُ الآخرُ، ولا تبقى الأداةُ
- **FR** : Tu te trompes sur le terme resté dans l'استعارة : reste le مشبَّه به (بلبلًا يُنشدُ) ou le مشبَّه (بكتِ الغيومُ), l'autre est omis ; l'outil ne reste jamais
- **EN** : You misidentify the term left in a metaphor: the مشبَّه به (بلبلًا يُنشدُ) or the مشبَّه (بكتِ الغيومُ) stays, the other drops; the particle never stays
- **Chapitres / piège** : ch07 — (pas de piège ; erreur récurrente dans les items)
- **Q distinctes** : 7
- **Distracteurs porteurs** :
  - `07:quiz#3→b` « استعارةٌ، لأنّ المشبَّهَ به محذوفٌ ولم يبقَ إلّا المشبَّهُ » — R1 : « ليس المحذوف هنا المشبّه به »
  - `07:quiz#5→d` « حذفتِ المشبَّهَ به وأبقتْ أداةَ التّشبيهِ في الكلامِ » — R1 (paraphrase de l'explication) :  وقد بقي المشبّه به الليل لا الأداة 
  - `07:01#6→a` « المشبَّهُ، وهو التّلميذُ المنشدُ » — R1 (paraphrase de l'explication) :  المذكور بلبلًا وهو المشبّه به 
  - `07:01#6→b` « أداةُ التّشبيهِ، وهي الكافُ » — R1 (paraphrase de l'explication) :  المذكور بلبلًا وهو المشبّه به 
  - `07:01#6→c` « وجهُ الشّبَهِ، وهو جمالُ الصّوتِ » — R1 (paraphrase de l'explication) :  المذكور بلبلًا وهو المشبّه به 
  - `07:02#2→a` « المشبَّهُ به، وهو «الغيومُ» » — R1 (paraphrase de l'explication) :  المشبّه الغيوم … الجبال مكان البكاء 
  - `07:02#2→b` « وجهُ الشّبَهِ، وهو الفعلُ «بكتْ» » — R1 (paraphrase de l'explication) :  المشبّه الغيوم … الجبال مكان البكاء 
  - `07:02#2→d` « المشبَّهُ به، وهو «الجبالُ» » — R1 (paraphrase de l'explication) :  المشبّه الغيوم … الجبال مكان البكاء 
  - `07:04#4→a` « بقيَ المشبَّهُ به «الرّبيعُ»، وأفادتِ الصّورةُ أنّ الفصلَ حيٌّ فرِحٌ ي… » — R1 : « وليس الربيع مشبّهًا به هنا »
  - `07:04#5→c` « استعارةٌ، حُذفَ فيها المشبَّهُ به (السّعيُ إلى المعالي) وبقيَ المشبَّه… »
  - `07:05#5→b` « حُذفَ المشبَّهُ به والأداةُ ووجهُ الشّبَهِ، وبقيَ المشبَّهُ »

#### `arabe.sura.rukn-ghayr-munasib` — NEUF

- **AR** : تسمّي ركنَ التّشبيهِ باسمٍ آخرَ: المشبَّهُ الموصوفُ، والمشبَّهُ به ما شُبِّه به، والأداةُ الكلمةُ الرّابطةُ، ووجهُ الشّبَهِ الصّفةُ المشتركةُ
- **FR** : Tu nommes mal un pilier du تشبيه : مشبَّه = le décrit, مشبَّه به = la référence, أداة = le mot-lien, وجه الشبه = la qualité commune
- **EN** : You misname a simile element: مشبَّه = the described, مشبَّه به = the reference, أداة = the linking word, وجه الشبه = the shared quality
- **Chapitres / piège** : ch07 — (pas de piège ; erreur récurrente dans les items)
- **Q distinctes** : 9
- **Distracteurs porteurs** :
  - `07:quiz#1→a` « المشبَّهُ، والمشبَّهُ به، وأداةُ التّشبيهِ، وأثرُ الصّورةِ » — R1 (paraphrase de l'explication) :  أثر الصورة / المعنى المجازي / المعنى الحقيقي ليست أركانًا 
  - `07:quiz#1→b` « المشبَّهُ، والمشبَّهُ به، ووجهُ الشّبَهِ، والمعنى المجازيُّ » — R1 (paraphrase de l'explication) :  أثر الصورة / المعنى المجازي / المعنى الحقيقي ليست أركانًا 
  - `07:quiz#1→d` « المشبَّهُ، وأداةُ التّشبيهِ، ووجهُ الشّبَهِ، والمعنى الحقيقيُّ » — R1 (paraphrase de l'explication) :  أثر الصورة / المعنى المجازي / المعنى الحقيقي ليست أركانًا 
  - `07:01#1→c` « الكافُ »
  - `07:01#1→d` « كرمًا »
  - `07:01#2→a` « في »
  - `07:01#2→b` « دُرَرٌ »
  - `07:01#2→c` « منثورةٌ »
  - `07:01#4→a` « الأداةُ «يُشبهُ»، ووجهُ الشّبَهِ «الجبلَ» »
  - `07:01#4→b` « الأداةُ «هو»، ووجهُ الشّبَهِ «رسوخًا» »
  - `07:01#4→d` « الأداةُ «الجبلَ»، ووجهُ الشّبَهِ «يُشبهُ» »
  - `07:02#3→a` « المشبَّهُ «الوقتُ»، والمشبَّهُ به «السّيفُ»، والأداةُ «كالسّيفِ»، ووجه… »
  - `07:02#3→c` « المشبَّهُ «الوقتُ»، والمشبَّهُ به «قطعَكَ»، والأداةُ الكافُ، ووجهُ الش… »
  - `07:02#6→c` « المشبَّهُ هو «تحترقُ»، لأنّها الصّفةُ المشتركةُ بين الطّرفَين » — R1 : « تحترق جزء من وجه الشبه لا مشبّه »
  - `07:04#2→c` « المشبَّهُ «المؤمنُ»، والمشبَّهُ به «بعضُه»، والأداةُ الكافُ، ووجهُ الش… » — R1 : « جعل بعضه مشبّهًا به … إنكار للكاف »
  - `07:04#2→d` « المشبَّهُ «المؤمنُ»، والمشبَّهُ به «البنيانُ»، ولا أداةَ فيه، ووجهُ ال… » — R1 : « جعل بعضه مشبّهًا به … إنكار للكاف »
  - `07:05#2→b` « المشبَّهُ ووجهُ الشّبَهِ » — R1 (paraphrase de l'explication) :  المشبّه والمشبّه به لا بد من ذكرهما 
  - `07:05#2→c` « المشبَّهُ به والأداةُ » — R1 (paraphrase de l'explication) :  المشبّه والمشبّه به لا بد من ذكرهما 
  - `07:05#2→d` « المشبَّهُ والمشبَّهُ به » — R1 (paraphrase de l'explication) :  المشبّه والمشبّه به لا بد من ذكرهما 
  - `07:06#6→c` « لا أداةَ فيه، والمشبَّهُ السّفنُ، والمشبَّهُ به الجبالُ، ووجهُ الشّبَه… » — R1 (paraphrase de l'explication) :  إنكار الأداة … البحر مشبّه به 
  - `07:06#6→d` « الأداةُ الكافُ، والمشبَّهُ السّفنُ، والمشبَّهُ به البحرُ، ووجهُ الشّبَ… » — R1 (paraphrase de l'explication) :  إنكار الأداة … البحر مشبّه به 

#### `arabe.sura.sura-hujja-tuthbit` — NEUF

- **AR** : تعدُّ الصّورةَ أو السّجعَ أو الطّباقَ حجّةً تُثبتُ (لصٌّ صامتٌ، أطروحتي صحيحةٌ لأنّها مسجوعةٌ): الزّينةُ تؤثّرُ وتقرّبُ الفكرةَ ولا تُثبتُ، والإثباتُ للحجّةِ
- **FR** : Tu prends l'image, le saj' ou le tibāq pour une preuve (لصٌّ صامتٌ ; « ma thèse rime donc elle est vraie ») : l'ornement touche, seul l'argument prouve
- **EN** : You take an image, saj' or tibaq for proof (لصٌّ صامتٌ; "my thesis is true because it rhymes"): ornament moves but doesn't prove; proof comes from an argument
- **Chapitres / piège** : ch07 — piège n°5 « عدُّ الصّورةِ حجّةً تُثبتُ الأطروحةَ. قال تلميذٌ: «قولُنا «لصٌّ صامتٌ» دليلٌ على أنّ التّدخينَ مضرٌّ». ويُغري … »
- **Q distinctes** : 10
- **Distracteurs porteurs** :
  - `07:quiz#5→a` « ذكرتْ دليلًا علميًّا يُثبتُ بالأرقامِ أنّ الظّلمَ سينتهي قريبًا » — R1 : « الصورة تؤثّر ولا تُثبت »
  - `07:02#5→a` « الإقناعُ بحجّةٍ علميّةٍ تُثبتُ أضرارَ الإدمانِ على الجسمِ كلِّه » — R1 (paraphrase de l'explication) :  لا خبرًا علميًّا ولا رقمًا ولا واقعة تاريخيّة 
  - `07:02#5→b` « الإقناعُ بحجّةٍ رقميّةٍ تُحصي عددَ المدمنين في البلادِ » — R1 (paraphrase de l'explication) :  لا خبرًا علميًّا ولا رقمًا ولا واقعة تاريخيّة 
  - `07:02#5→d` « الإقناعُ بحجّةٍ تاريخيّةٍ تروي نشأةَ الإدمانِ عبرَ العصورِ » — R1 (paraphrase de l'explication) :  لا خبرًا علميًّا ولا رقمًا ولا واقعة تاريخيّة 
  - `07:04#3→b` « تُثبتُ بالبرهانِ أنّ السّيوفَ أشدُّ لمعانًا من الأسنانِ كلِّها في ساحة… » — R1 (paraphrase de l'explication) :  صورة تؤثّر ولا تقدّم برهانًا ولا وصفًا علميًّا 
  - `07:04#3→c` « تُحوّلُ الكلامَ إلى وصفٍ علميٍّ لأثرِ الضّوءِ في المعادنِ اللّامعةِ » — R1 (paraphrase de l'explication) :  صورة تؤثّر ولا تقدّم برهانًا ولا وصفًا علميًّا 
  - `07:04#4→b` « بقيَ المشبَّهُ «الرّبيعُ»، وأفادتِ الصّورةُ دليلًا علميًّا على أنّ الر… » — R1 : « الصورة تؤثّر ولا تقدّم دليلًا علميًّا »
  - `07:05#6→a` « تُثبتُ الأطروحةَ بالبرهانِ كما تفعلُ الحجّةُ العقليّةُ المنطقيّةُ » — R1 : « وليست الصورة برهانًا، ولا تُحذف من الحجاج، ولا تختص بالشعر »
  - `07:06#2→c` « تشبيهٌ مشبَّهُه «الأمُّ» ومشبَّهُه به «مدرسةٌ»، ووجهُ الشّبَهِ التّربي… » — R1 : « جعل الصورة دليلًا علميًّا وهي لا تُثبت »
  - `07:06#3→c` « أن يذكرَ دليلًا علميًّا على انجلاءِ الليلِ كلَّ صباحٍ »
  - `07:06#5→a` « الخطأُ أنّه حذفَ أداةَ التّشبيهِ، ولا يكونُ التّشبيهُ حجّةً إلّا إذا ذ… » — R1 : « الصورة تؤثّر في الوجدان ولا تُثبت »
  - `07:06#5→c` « لا خطأَ، فكلُّ صورةٍ تردُ في الحجاجِ تُعدُّ برهانًا على الأطروحةِ نفسِ… » — R1 : « الصورة تؤثّر في الوجدان ولا تُثبت »
  - `08:06#2→a` « صحيحٌ، فكلّما كانَ الكلامُ أطربَ للأذنِ كانتِ الأطروحةُ أصحَّ وأقوى حج… » — R1 (paraphrase de l'explication) :  السجع لا يقوم مقام الحجّة … والأسلوب المرسل لا يُثبت شيئًا بذاته 
  - `08:06#2→c` « الأسلوبُ المرسَلُ وحدَه هو الذي يُثبتُ الأطروحةَ لأنّه خالٍ من الزّينة… » — R1 (paraphrase de l'explication) :  السجع لا يقوم مقام الحجّة … والأسلوب المرسل لا يُثبت شيئًا بذاته 
  - `08:06#3→c` « الطّباقُ يُثبتُ أنّ الاجتهادَ يرفعُ صاحبَه، والسّجعُ يبرهنُ على ذلك بت… » — R1 : « كلاهما زينة لا برهان »

#### `arabe.sura.tashbih-isti3ara-khalt` — NEUF

- **AR** : تخلطُ بين التّشبيهِ والاستعارةِ: التّشبيهُ يذكرُ طرفَيه معًا، والاستعارةُ لا يبقى فيها إلّا طرفٌ واحدٌ (بلبلًا يُنشدُ، بكتِ الغيومُ)
- **FR** : Tu confonds تشبيه et استعارة : le تشبيه garde ses deux termes, l'استعارة n'en garde qu'un (بلبلًا يُنشدُ، بكتِ الغيومُ)
- **EN** : You confuse simile and metaphor: a تشبيه keeps both terms, an استعارة keeps only one (بلبلًا يُنشدُ، بكتِ الغيومُ)
- **Chapitres / piège** : ch07 — (pas de piège ; erreur récurrente dans les items)
- **Q distinctes** : 7
- **Distracteurs porteurs** :
  - `07:01#5→a` « «رأيتُ بحرًا يمشي على اليابسةِ» » — R1 : « لم يبقَ إلا طرف واحد … شرط الاستعارة »
  - `07:01#5→c` « «بكتِ الغيومُ فوقَ الجبالِ» » — R1 : « لم يبقَ إلا طرف واحد … شرط الاستعارة »
  - `07:01#5→d` « «أطلَّ بدرٌ من نافذةِ القسمِ» » — R1 : « لم يبقَ إلا طرف واحد … شرط الاستعارة »
  - `07:02#4→d` « كلتاهما تشبيهٌ، لأنّ كلتَيهما تذكرُ الأسدَ في الكلامِ » — R1 : « ذكر المشبّه به وحده ليس تشبيهًا »
  - `07:02#6→b` « العبارةُ استعارةٌ لا تشبيهٌ، فلا مشبَّهَ فيها أصلًا ولا مشبَّهَ به »
  - `07:04#5→b` « تشبيهٌ، لأنّ الطّرفَين مذكوران في البيتِ معًا، وهما الجبالُ والحُفَرُ » — R1 (paraphrase de l'explication) :  ليست تشبيهًا فالجبال والحفر لا يقارن أحدهما بالآخر 
  - `07:05#4→c` « «هو كالجبلِ رسوخًا» » — R1 : « الأركان كلها مذكورة »
  - `07:05#5→c` « حُذفتِ الأداةُ ووجهُ الشّبَهِ فقط، وبقيَ الطّرفانِ معًا »
  - `07:05#5→d` « لم يُحذفْ شيءٌ، وبقيتِ الأركانُ الأربعةُ كلُّها »
  - `07:06#3→b` « أن يقولَ إنّها تشبيهٌ لا استعارةٌ لأنّ في العبارةِ طرفَين مذكورَين معً… » — R1 : « هي استعارة لا تشبيه لأنّ طرفًا واحدًا بقي »

### Domaine `tasghir`

#### `arabe.tasghir.alif-hukm-khalt` — NEUF

- **AR** : تُخطئُ في حكمِ ألفِ الاسمِ عند التّصغيرِ: الزّائدةُ تصيرُ واوًا (عُوَيْمِل)، والثّالثةُ تصيرُ ياءً (كُتَيِّب)، والمنقلبةُ تعودُ إلى أصلِها (سُوَيْعة)
- **FR** : Tu te trompes sur l'alif du nom : alif ajoutée → و (عُوَيْمِل), alif en 3ᵉ lettre → ي (كُتَيِّب), alif substituée → son origine (سُوَيْعة)
- **EN** : You get the alif wrong: added alif → و (عُوَيْمِل), alif as 3rd letter → ي (كُتَيِّب), substituted alif → its origin (سُوَيْعة)
- **Chapitres / piège** : ch13 — (pas de piège ; erreur récurrente dans les items)
- **Q distinctes** : 3
- **Distracteurs porteurs** :
  - `13:02#4→a` « لأنّ الواوَ أخفُّ في النّطقِ من الياءِ في هذا الموضعِ » — R1 (paraphrase de l'explication) :  التأنيث لا يقلب ألفًا 
  - `13:02#4→c` « لأنّ المؤنّثَ تُقلبُ ألفُه واوًا في التّصغيرِ دائمًا » — R1 (paraphrase de l'explication) :  التأنيث لا يقلب ألفًا 
  - `13:04#2→b` « عُيَيْمِل » — R1
  - `13:04#2→d` « عُمَيْل » — R1
  - `13:05#3→b` « دُيَيْبّة » — R1 (paraphrase de l'explication) :  قلب الألف ياء حكم حرف اللين الثالث 

#### `arabe.tasghir.asl-al-musaghghar-khalt` — NEUF

- **AR** : تعودُ من المصغَّرِ إلى كلمةٍ أخرى (كَلْب ← كِلاب أو كَليب أو كَلْبة): انزعْ ياءَ التّصغيرِ وأعدِ الحركةَ فيعودُ المفردُ نفسُه
- **FR** : Défaire le diminutif te mène à un autre mot (pluriel كِلاب, adjectif كَليب, féminin كَلْبة) : retire la ي et rends la voyelle : tu retrouves le singulier
- **EN** : Undoing a diminutive you land on another word (plural كِلاب, adjective كَليب, feminine كَلْبة): remove the ي, restore the vowel, and you get the same singular
- **Chapitres / piège** : ch13 — (pas de piège ; erreur récurrente dans les items)
- **Q distinctes** : 5
- **Distracteurs porteurs** :
  - `13:01#3→b` « كِلاب » — R1 : « ليس جمعًا … لا تاء »
  - `13:01#3→c` « كَلِيب » — R1 : « ليس جمعًا … لا تاء »
  - `13:01#3→d` « كَلْبة » — R1 : « ليس جمعًا … لا تاء »
  - `13:02#3→a` « قِطَط »
  - `13:02#3→c` « قِطّة »
  - `13:05#1→c` « سَمِيكة » — R1 : « صفة … اسم آخر »
  - `13:05#1→d` « سَمَّاك » — R1 : « صفة … اسم آخر »
  - `13:05#5→c` « هَرِيرة »
  - `13:05#6→a` « كَرِيّة، وأصلُها الفعلُ «كَرَّ» »
  - `13:05#6→b` « كُرَيْر، وأصلُها «كُرور» »

#### `arabe.tasghir.harf-asli-yasqut` — NEUF

- **AR** : تُسقطُ حرفًا من الأصلِ أو تتركُ المتماثلَينِ بلا إدغامٍ أو لا تردُّهما إلى مشدَّدٍ (كُتَيْب، دُوَيْبِبة، قُطَيْط ← قِطَط): ارجعْ إلى الأصلِ كاملًا
- **FR** : Tu perds une lettre de l'origine, laisses deux lettres identiques sans les fondre, ou ne les ramènes pas à une doublée (كُتَيْب، دُوَيْبِبة، قُطَيْط ← قِطَط)
- **EN** : You lose a root letter, leave two identical letters unmerged, or fail to restore a doubled one (كُتَيْب، دُوَيْبِبة، قُطَيْط ← قِطَط): recover the whole origin
- **Chapitres / piège** : ch13 — piège n°4 « إسقاطُ حرفِ اللينِ أو تركُ المتماثلَينِ على حالِهما: من قالَ إنّ أصلَ «كُتَيِّب» هو «كَتْب» أسقطَ الياءَ المنق… »
- **Q distinctes** : 4
- **Distracteurs porteurs** :
  - `13:02#3→b` « قَطِيط » — R1 (paraphrase de l'explication) :  المتماثلان يرجعان إلى حرف مشدد 
  - `13:04#3→b` « كُتَيْب » — R1 : « يهمل الحرف الرابع من الأصل »
  - `13:05#3→c` « دُوَيْبِبة » — R1 (paraphrase de l'explication) :  ترك الباءين بلا إدغام خطأ 
  - `13:05#5→d` « هَرَرة » — R1 (paraphrase de l'explication) :  المتماثلان يُرجعان إلى حرف مشدد 

#### `arabe.tasghir.kull-musaghghar-sighar` — NEUF

- **AR** : تحملُ كلَّ مصغَّرٍ على الصِّغَرِ الحسّيِّ (بُنَيَّ، شُوَيْعِر): الصّيغةُ واحدةٌ ومعانيها ستّةٌ: تصغيرٌ، تقليلٌ، تقريبٌ، عطفٌ، حسرةٌ، تحقيرٌ
- **FR** : Tu lis tout diminutif comme une vraie petitesse (بُنَيَّ، شُوَيْعِر) : une forme, six sens : petitesse, atténuation, proximité, tendresse, regret, mépris
- **EN** : You read every diminutive as real smallness (بُنَيَّ، شُوَيْعِر): one form carries six meanings: smallness, reduction, nearness, affection, regret, contempt
- **Chapitres / piège** : ch13 — piège n°6 « طلبُ المعنى في **الصّيغةِ**: أن يُقالَ «كلُّ مصغَّرٍ يدلُّ على الصّغرِ». فـ«بُنَيَّ» في فمِ الأبِ عَطفٌ لا صِغ… »
- **Q distinctes** : 5
- **Distracteurs porteurs** :
  - `13:quiz#4→b` « معنًى واحدٌ هو صِغَرُ الشّيءِ، يُعيّنُه حجمُ الشّيءِ المصغَّرِ »
  - `13:02#5→c` « التّصغيرُ الحقيقيُّ لصِغَرِ حجمِ الشّاةِ » — R1 : « الصيغة مقطوعة من سياقها »
  - `13:02#6→a` « صِغَرُ سِنِّ الشّاعرِ وقِصَرُ قامتِه » — R1 : « لا صغر حسيًّا في شاعر »
  - `13:03#5→c` « التّصغيرُ الحقيقيُّ لصِغَرِ سِنِّ الابنِ » — R1 : « لا الصغر الحسي »
  - `13:05#2→a` « التّصغيرُ الحقيقيُّ لحجمِ البابِ »

#### `arabe.tasghir.ma3na-bi-ghayr-qarina` — NEUF

- **AR** : تعيّنُ معنى التّصغيرِ من الصّيغةِ أو الوزنِ وحدِهما بلا قرينةٍ: انظرْ إلى الاسمِ وعلاقةِ المتكلّمِ به والسّياقِ (ما … إلّا، النّبرةُ)
- **FR** : Tu fixes le sens du diminutif par la forme ou le schème seuls, sans indice : regarde le nom, le lien du locuteur et le contexte (ما … إلّا, le ton)
- **EN** : You fix the diminutive's meaning from form or pattern alone, without a clue: look at the noun, the speaker's tie to it and the context (ما … إلّا, tone)
- **Chapitres / piège** : ch13 — piège n°7 « الحكمُ على الكلمةِ وحدَها بعد اقتطاعِها من النّصِّ. «شُوَيْهَتي» مقطوعةً تصلحُ للتّودّدِ وللحسرةِ معًا؛ ومن أج… »
- **Q distinctes** : 9
- **Distracteurs porteurs** :
  - `13:quiz#4→a` « ستّةُ معانٍ، يُعيّنُها وزنُ الصّيغةِ المستعملةِ وعددُ حروفِها » — R1 : « لا بالوزن »
  - `13:quiz#4→c` « ثلاثةُ معانٍ بعددِ الأوزانِ الثّلاثةِ، يُعيّنُها عددُ الحروفِ » — R1 : « لا بالوزن »
  - `13:01#6→a` « التّحقيرَ من شأنِ القلبِ كلِّه » — R1 : « لا عاطفة للمتكلم فيهما »
  - `13:01#6→b` « العَطْفَ على صاحبِ القلبِ » — R1 : « لا عاطفة للمتكلم فيهما »
  - `13:01#6→c` « تقريبَ الأذينِ من البطينِ » — R1 : « لا عاطفة للمتكلم فيهما »
  - `13:02#2→b` « الحسرةُ على الزّمنِ الذي ضاع » — R1 : « قوله على الأكثر يفصل »
  - `13:02#2→c` « تقريبُ الزّمانِ من لحظةِ الكلامِ » — R1 : « قوله على الأكثر يفصل »
  - `13:02#2→d` « التّحقيرُ من شأنِ الإصلاحِ كلِّه » — R1 : « قوله على الأكثر يفصل »
  - `13:02#5→b` « التّحقيرُ من شأنِ الشّاةِ المذبوحةِ »
  - `13:02#5→d` « التّقليلُ من عددِ ما يملكُه من الشّياهِ »
  - `13:02#6→b` « التّقليلُ من عددِ قصائدِه ودواوينِه »
  - `13:02#6→d` « الحسرةُ على ضياعِ شِعرِه وأدبِه »
  - `13:03#3→a` « التّقليلَ من مدّةِ السّفرِ »
  - `13:03#3→c` « التّحقيرَ من شأنِ الرّكبِ »
  - `13:03#3→d` « الحسرةَ على فواتِ الفجرِ »
  - `13:03#5→b` « التّحقيرُ » — R1
  - `13:03#5→d` « التّقليلُ من شأنِ الخطإِ » — R1
  - `13:03#6→a` « تقريبُ الزّمانِ من لحظةِ الكلامِ » — R1 : « لا زمان … لا صلة عاطفة … لا فقد »
  - `13:03#6→b` « العَطْفُ والتّودّدُ نحوَ الدّراهمِ » — R1 : « لا زمان … لا صلة عاطفة … لا فقد »
  - `13:03#6→d` « الحسرةُ على دراهمَ فقدَها صاحبُها » — R1 : « لا زمان … لا صلة عاطفة … لا فقد »
  - `13:05#2→b` « العَطْفُ والتّودّدُ نحوَ الحارسِ »
  - `13:05#2→d` « الحسرةُ على البابِ المغلقِ »

#### `arabe.tasghir.mushaddad-harf-wahid` — NEUF

- **AR** : تعدُّ الحرفَ المشدَّدَ حرفًا واحدًا (دُبّ ← دُبَيّ): المشدَّدُ حرفانِ، فالاسمُ ثلاثيٌّ على فُعَيْل ويظهرُ الحرفانِ: دُبَيْب
- **FR** : Tu comptes la lettre doublée comme une seule (دُبّ ← دُبَيّ) : elle vaut deux lettres ; le nom est trilitère sur فُعَيْل et les deux apparaissent : دُبَيْب
- **EN** : You count a doubled letter as one (دُبّ ← دُبَيّ): it counts as two, so the noun is three-letter on فُعَيْل and both show: دُبَيْب
- **Chapitres / piège** : ch13 — piège n°3 « عدُّ الحرفِ المشدَّدِ حرفًا واحدًا: من حسِبَ «دُبّ» ثنائيًّا عاملَه معاملةَ «أب» فخرج بـ«دُبَيّ». المشدَّدُ حر… »
- **Q distinctes** : 2
- **Distracteurs porteurs** :
  - `13:03#2→a` « دُبَيّ » — R1 : « ولو عُدّ المشدد حرفًا واحدًا لخرج دُبَيّ »
  - `13:05#3→d` « دُبَيْبة » — R1 : « من عد المشدد حرفًا واحدًا خرج دُبَيْبة »

#### `arabe.tasghir.sighat-al-tasghir-khalt` — NEUF

- **AR** : تُخطئُ في عملَي الصّيغةِ: ضمُّ الأوّلِ ثمّ ياءٌ ساكنةٌ بعد الثّاني (جَبِيل، أَبِيّ، دِرَيْهَم)؛ فتحُ الأوّلِ أو كسرُه أو ياءٌ متحرّكةٌ لا تصنعُ تصغيرًا
- **FR** : Tu te trompes sur les deux gestes : damma sur la 1ʳᵉ lettre puis ي sukûn après la 2ᵉ (جَبِيل، أَبِيّ، دِرَيْهَم) ; fatha, kasra ou ي voyellé n'en font pas
- **EN** : You get the two steps wrong: damma on the 1st letter then a silent ي after the 2nd (جَبِيل، أَبِيّ، دِرَيْهَم); a fatha, kasra or voweled ي is no diminutive
- **Chapitres / piège** : ch13 — (pas de piège ; erreur récurrente dans les items)
- **Q distinctes** : 6
- **Distracteurs porteurs** :
  - `13:quiz#2→a` « بكسرِ الحرفِ الأوّلِ وزيادةِ تاءٍ مربوطةٍ في آخرِ الكلمةِ كلِّها »
  - `13:quiz#2→b` « بفتحِ الحرفِ الأوّلِ وتشديدِ الحرفِ الثّاني وزيادةِ ألفٍ بعدَه »
  - `13:quiz#2→d` « بضمِّ الحرفِ الأخيرِ وزيادةِ واوٍ ساكنةٍ قبلَه مباشرةً »
  - `13:01#1→a` « جَبِيل » — R1 : « فتح الأول لا يصنع تصغيرًا »
  - `13:01#4→b` « شَجِيرة »
  - `13:02#1→d` « دِرَيْهَم » — R1 : « كسر الأول ليس من التصغير »
  - `13:03#2→c` « دَبِيب » — R1 : « دَبِيب »
  - `13:03#4→d` « أَبِيّ » — R1 (paraphrase de l'explication) :  أَبِيّ صفة على وزن فَعِيل لا تصغير 

#### `arabe.tasghir.ta2nith-fil-3add` — NEUF

- **AR** : تعدُّ التّاءَ أو الألفَ والهمزةَ في حروفِ الاسمِ (حَمْراء خماسيّةٌ، ساعة رباعيّةٌ): علامةُ التّأنيثِ خارجَ العدِّ؛ انزعْها وصغِّرْ ثمّ رُدَّها
- **FR** : Tu comptes la ة ou l'alif+hamza parmi les lettres (حَمْراء à 5, ساعة à 4) : la marque du féminin est hors décompte ; ôte-la, diminue, puis remets-la
- **EN** : You count the ة or alif+hamza among the letters (حَمْراء as 5, ساعة as 4): the feminine mark is outside the count; remove it, diminish, then put it back
- **Chapitres / piège** : ch13 — piège n°2 « عدُّ علامةِ التأنيثِ في الحروفِ: مَن حسِبَ «حَمْراء» خماسيّةً كتبَ «حُمَيْرِير»، ومَن حسِبَ «ساعة» رباعيّةً طل… »
- **Q distinctes** : 3
- **Distracteurs porteurs** :
  - `13:01#4→d` « شُجَيْعِرة » — R1 : « وزن الرباعي لا موضع له هنا »
  - `13:02#4→d` « لأنّ الاسمَ خماسيٌّ فوزنُه يقتضي واوًا بعد الياءِ » — R1 : « تاء التأنيث لا تعد … والكلمة ليست خماسية »
  - `13:04#4→b` « حُمَيْرِير » — R1 : « ما يخرج لمن عد الألف والهمزة في الحروف »

#### `arabe.tasghir.ta2nith-tuhdhaf-aw-tuzad` — NEUF

- **AR** : تحذفُ علامةَ التّأنيثِ أو تُبدلُها أو تزيدُها (شُجَيْر، حُمَيْرة، جُبَيْلة): تبقى في آخرِ المصغَّرِ كما هي ولا تُزادُ على المذكّرِ
- **FR** : Tu retires, remplaces ou ajoutes la marque du féminin (شُجَيْر، حُمَيْرة، جُبَيْلة) : elle reste en fin de diminutif et ne s'ajoute pas à un masculin
- **EN** : You drop, swap or add the feminine mark (شُجَيْر، حُمَيْرة، جُبَيْلة): it stays as is at the end of the diminutive and is not added to a masculine
- **Chapitres / piège** : ch13 — (pas de piège ; erreur récurrente dans les items)
- **Q distinctes** : 5
- **Distracteurs porteurs** :
  - `13:01#1→d` « جُبَيْلة »
  - `13:01#4→a` « شُجَيْر » — R1 : « حذف التاء يخرج الكلمة عن مؤنثها »
  - `13:04#4→a` « حُمَيْرة » — R1 (paraphrase de l'explication) :  يبدل همزة التأنيث تاء / يسقطها 
  - `13:04#4→d` « حُمَيْر » — R1 (paraphrase de l'explication) :  يبدل همزة التأنيث تاء / يسقطها 
  - `13:05#1→a` « سَمَك » — R1 : « فبلا تاء فلا يعطي مصغرًا بتاء »
  - `13:05#5→a` « هِرّ » — R1 : « التاء باقية في المصغر »

#### `arabe.tasghir.tariq-ta3bir-khalt` — NEUF

- **AR** : تخلطُ بين طرائقِ التّعبيرِ عن الصّغرِ: اشتقاقيٌّ بصيغةِ التّصغيرِ (شُجَيْرَة)، ومعجميٌّ بكلمةٍ مستقلّةٍ (جَرْو)، وتركيبيٌّ بنعتٍ (حديقةٌ صغيرةٌ)
- **FR** : Tu confonds les voies pour dire « petit » : dérivation par le diminutif (شُجَيْرَة), lexique par un mot propre (جَرْو), syntaxe par un adjectif (حديقةٌ صغيرةٌ)
- **EN** : You mix the ways of saying "small": derivation with the diminutive (شُجَيْرَة), a dedicated word (جَرْو), or an adjective (حديقةٌ صغيرةٌ)
- **Chapitres / piège** : ch13 — (pas de piège ; erreur récurrente dans les items)
- **Q distinctes** : 4
- **Distracteurs porteurs** :
  - `13:quiz#1→a` « نعتٌ يُضافُ إلى الاسمِ ليدلَّ على صِغَرِه، فيبقى الاسمُ كما هو » — R1 : النعت = تركيبي، جرو/شبل = معجمي
  - `13:quiz#1→c` « كلمةٌ مستقلّةٌ وُضعت للدلالةِ على صغيرِ الحيوانِ، كالجَرْوِ والشِّبْلِ » — R1 : النعت = تركيبي، جرو/شبل = معجمي
  - `13:quiz#1→d` « مركّبٌ إضافيٌّ يُضافُ فيه الاسمُ إلى كلمةِ «صغير» أو «صغار» » — R1 : النعت = تركيبي، جرو/شبل = معجمي
  - `13:quiz#5→b` « تَبِعَ العِجْلُ البقرةَ »
  - `13:quiz#5→c` « صغارُ الطّيرِ لا تطيرُ »
  - `13:quiz#5→d` « حولَ البيتِ حديقةٌ صغيرةٌ »
  - `13:03#1→a` « تركيبيًّا، باسمٍ يليه نعتٌ يدلُّ على الصّغرِ »
  - `13:03#1→b` « اشتقاقيًّا، بصيغةٍ تُجعلُ على اسمِ الذّئبِ نفسِه »
  - `13:04#1→a` « معجميًّا »
  - `13:04#1→c` « اشتقاقيًّا بصيغةِ التّصغيرِ »

#### `arabe.tasghir.wazn-bi-ghayr-al-3adad` — NEUF

- **AR** : تختارُ وزنَ المصغَّرِ بغيرِ عددِ الحروفِ (عُصَيْفِر، دُرَيْم): ثلاثةٌ ← فُعَيْل، أربعةٌ ← فُعَيْعِل، خمسةٌ ← فُعَيْعِيل؛ فعُدَّ الحروفَ أوّلًا
- **FR** : Tu choisis le schème du diminutif sans compter les lettres (عُصَيْفِر، دُرَيْم) : 3 → فُعَيْل, 4 → فُعَيْعِل, 5 → فُعَيْعِيل ; compte d'abord
- **EN** : You pick the diminutive pattern without counting letters (عُصَيْفِر، دُرَيْم): 3 → فُعَيْل, 4 → فُعَيْعِل, 5 → فُعَيْعِيل; count first
- **Chapitres / piège** : ch13 — piège n°1 « اختيارُ الوزنِ بحسبِ **المعنى** أو بحسبِ ما يستثقلُه اللّسانُ، لا بحسبِ **عددِ الحروفِ**. فمن قال في «عُصفور»:… »
- **Q distinctes** : 7
- **Distracteurs porteurs** :
  - `13:quiz#3→b` « فُعَيْل » — R1 : « عدد الحروف هو الذي يختار الوزن »
  - `13:quiz#3→c` « فُعَيْعِيل » — R1 : « عدد الحروف هو الذي يختار الوزن »
  - `13:quiz#3→d` « فُعَيْلان » — R1 : « عدد الحروف هو الذي يختار الوزن »
  - `13:01#1→c` « جُبَيْعِل »
  - `13:01#5→a` « فُعَيْل »
  - `13:01#5→c` « فُعَيْعِل »
  - `13:01#5→d` « فُعَيْلِيل »
  - `13:02#1→a` « دُرَيْهِيم » — R1 (paraphrase de l'explication) :  فُعَيْعِيل للخماسي وحده، ودُرَيْم يحذف حرفًا 
  - `13:02#1→b` « دُرَيْم » — R1 (paraphrase de l'explication) :  فُعَيْعِيل للخماسي وحده، ودُرَيْم يحذف حرفًا 
  - `13:04#2→c` « عُوَيْمِيل » — R1 : « فُعَيْعِيل وزن الخماسي »
  - `13:04#3→a` « كُتَيْبِيب »
  - `13:05#4→a` « قُنَيْدِل » — R1 (paraphrase de l'explication) :  وزن الرباعي ينقص حرفًا 
  - `13:05#4→b` « قُنَيْل » — R1 (paraphrase de l'explication) :  وزن الرباعي ينقص حرفًا 
  - `13:05#4→c` « قُنَيْدَال » — R1 (paraphrase de l'explication) :  وزن الرباعي ينقص حرفًا 

#### `arabe.tasghir.ya-ba3d-al-thani-ta3rif` — NEUF

- **AR** : تحكمُ بالتّصغيرِ لوجودِ ياءٍ بعد الحرفِ الثّاني (الوَلِيد، أَمِين): تلك ياءُ مدٍّ في وزنِ فَعِيل، وياءُ التّصغيرِ ساكنةٌ بعد حرفٍ مضمومٍ
- **FR** : Tu juges qu'il y a diminutif dès qu'un ي suit la 2ᵉ lettre (الوَلِيد، أَمِين) : c'est le ي long du schème فَعِيل ; celui du diminutif est sukûn après une damma
- **EN** : You see a diminutive whenever a ي follows the 2nd letter (الوَلِيد، أَمِين): that is the long ي of the فَعِيل pattern; the diminutive ي is silent after a damma
- **Chapitres / piège** : ch13 — piège n°5 « الحكمُ على العَلَمِ بوجودِ ياءٍ بعد الحرفِ الثّاني وحدَها: «الوَلِيد» و«أمِين» و«حَبِيب» فيها هذه الياءُ ولا ت… »
- **Q distinctes** : 1
- **Distracteurs porteurs** :
  - `13:04#5→a` « خالد بن الوَلِيد » — R1 (paraphrase de l'explication) :  فيهما ياء لكنهما على فَعِيل 
  - `13:04#5→c` « قاسم أَمِين » — R1 (paraphrase de l'explication) :  فيهما ياء لكنهما على فَعِيل 

## 3. Règles de précédence

- ch01 — `arabe.i3rab.haraka-bada-harf` (voyelle donnée au duel / pluriel masculin / cinq noms : registre 6ᵉ) l'emporte sur `arabe.i3rab.harf-ghayr-munasib` (nouveau) quand l'option est une VOYELLE (الضمّة، الكسرة) ; `harf-ghayr-munasib` quand c'est une MAUVAISE LETTRE (و au lieu de ا, ي au lieu de و…).
- `arabe.i3rab.mu3tall-3alama-zahira` (marque visible sur ا/ي final ou السكون au lieu de la chute de la lettre faible) vs `arabe.fi3l.hukm-bil-haraka` (registre 6ᵉ : on juge le verbe d'après sa voyelle et on ignore l'outil لن/لم) : si l'option nie l'outil → `hukm-bil-haraka` ; si elle ignore la nature du verbe/nom à lettre faible → `mu3tall-3alama-zahira`.
- `arabe.i3rab.mabni-mu3rab-khalt` (confusion maʿrab/mabni, y compris maqsur/manqus pris pour mabni) ≠ `arabe.sinf.mabni-ka-mu3rab` (ch12 : un nom mabni rangé parmi maqsur/manqus/mamdud) : sens inverses.
- Précédence des ids du chapitre 05 : un id propre à un schème (`af3ala-ja3liyya-daiman`, `fa33ala-takthir-aw-ja3liyya`, `mutawa3a-bila-fi3l-sabiq`, `tafa3ala-musharaka-daiman`, `istaf3ala-talab-daiman`) l'emporte sur `arabe.mazid.ma3na-bila-nazar-fil-jidhr` quand l'option énonce exactement le sens-piège de ce schème ; `ma3na-bila-nazar-fil-jidhr` couvre les autres sens faux d'un même schème.
- `arabe.mazid.wazn-ma3na-wahid` (affirmation générale « un schème = un sens », 05:quiz#1 d, 06#4 c, 06#6) l'emporte sur les ids par schème quand l'option est une règle et non un sens appliqué à un verbe.
- `arabe.mazid.min-nafs-al-jidhr-dun-ma3na` : l'option est un MOT/VERBE de la même racine (pas un sens) ; `arabe.mazid.wazn-qarib-khalt` : l'option est un SCHÈME/élément voisin ; `arabe.masdar.wazn-fi3l-akhar` : l'option est le MASDAR d'un schème voisin.
- `arabe.mazid.if3alla-if3aalla-khalt` ne sert que pour افعلّ/افعالّ ; les autres schèmes confondus relèvent de `wazn-qarib-khalt`.
- ch06 — `arabe.ishtiqaq.mazid-haraka-al-3ayn` (registre) l'emporte sur `arabe.ishtiqaq.fa3il-maf3ul-ma3na` (registre) quand le verbe est augmenté et que l'option ne diffère que par la voyelle avant la dernière lettre (مُكرِم / مُكرَم) ; `fa3il-maf3ul-ma3na` quand c'est un autre schème (فاعل pour مفعول d'un trilitère).
- `arabe.ishtiqaq.sifa-mushabbaha-khalt` (une صفة مشبّهة prise pour agent/patient/superlatif) vs `arabe.ishtiqaq.fa3il-mubalagha-wa-sifa` (فَعِيل/فَعُول rangés dans les صفات alors qu'ils sont des intensifs — 04#2 seul) vs `arabe.ishtiqaq.fa3il-mubalagha-khalt` (agent ↔ intensif).
- `arabe.ishtiqaq.mim-ala-maftuha` (la voyelle du م distingue l'outil du lieu/temps) vs `arabe.ishtiqaq.makan-ka-fa3il-aw-maf3ul` (lieu/temps vs agent/patient/intensif) vs `arabe.ishtiqaq.wazn-ala-khalt` (confusion entre les 3 schèmes de l'outil lui-même).
- Emprunt : `arabe.ishtiqaq.wazn-fa3il-lil-mazid` pour le seul 06:quiz#2 a ; `arabe.ishtiqaq.mazid-haraka-al-3ayn` pour n°2 (la voyelle EST la réponse).
- ch07 — `arabe.sura.qalb-al-tarafayn` quand l'option est le BON jeu de termes dans le mauvais sens (المشبَّه ↔ المشبَّه به) ; `arabe.sura.rukn-ghayr-munasib` quand un autre élément est confondu (أداة, وجه الشبه, ou un mot hors tashbih) ; `arabe.sura.rukn-baqi-khalt` quand la question porte sur ce qui RESTE dans une استعارة.
- `arabe.sura.isti3ara-li-ghiyab-al-ada` (la raison donnée est l'absence d'outil / une seule suppression) l'emporte sur `arabe.sura.tashbih-isti3ara-khalt` (simple étiquette inversée tashbih/isti'āra sans raison fautive).
- `arabe.sura.sura-hujja-tuthbit` (l'image prouve, ou ne doit pas figurer dans l'argumentation) vs `arabe.sura.athar-al-sura-khalt` (l'effet de l'image n'est pas dit : renommée, mot rare, « parce que c'est un tashbih »).
- `arabe.sura.majaz-bi-makan-al-kalima` (jugement par le genre/la rareté) vs `arabe.sura.majaz-ka-haqiqa` (figuré pris pour littéral) : opposés.
- ch08 — `arabe.badi3.saj3-yatlub-kalimatayn-mutashabihatayn` (piège n°2 : on exige la ressemblance des deux mots) vs `arabe.badi3.saj3-bi-tashabuh-al-bina2` (on voit du saj' faute de dernière lettre commune) vs `arabe.badi3.harf-akhir-aw-haraka-khalt` (voyelle/tanwin/lettre précédente prises en compte) : trois façons de mal lire le « dernier caractère ».
- `arabe.badi3.tibaq-saj3-khalt` (définitions ou effets mélangés) vs `arabe.badi3.tibaq-saj3-yajtami3an` (le texte contient les deux — ou aucun — et on n'en retient qu'un) : le second quand l'option nie l'un des deux alors que les deux sont présents.
- `arabe.badi3.saj3-mutakallaf-3ala-hisab-al-ma3na` (sacrifier le sens à la rime) vs `arabe.badi3.takrir-saj3-fi-kull-jumla` (trop de saj') vs `arabe.sura.sura-hujja-tuthbit` (l'ornement prouve ; id de ch07 élargi au saj'/tibāq) : trois excès distincts.
- `arabe.badi3.maqama-bi-saj3-faqat` (texte rimé pris pour maqāma) : les distracteurs de 05#6 qui nient simplement un trait de la maqāma (b, c, d) restent muets.
- ch09 — `arabe.hijaj.arkan-khalt` (définitions des éléments : thèse/argument/exemple/conclusion) cède la place aux ids spécifiques quand l'option est exactement le piège : exemple pris pour argument → `mithal-hujja-kafiya` ; thèse reformulée prise pour argument → `i3adat-al-utruha-hujja` ; conclusion rangée dans la démarche → `istintaj-dakhil-al-sayrura`.
- `arabe.hijaj.tarikhi-waqi3i-khalt` (historique ↔ factuel) l'emporte sur `naw3-al-hujja-khalt` (autorité / raison) ; `naw3-al-hujja-khalt` ne sert que pour les autres confusions de type.
- `arabe.hijaj.ta3lil-tafsir-khalt` (exactement تعليل ↔ تفسير) l'emporte sur `arabe.hijaj.mu2ashshir-ghayr-munasib` (autre relation) ; `istidrak-khalt` (استدراك ↔ تقابل/توكيد) l'emporte aussi sur `mu2ashshir-ghayr-munasib`.
- `arabe.hijaj.khatima-sardiyya-mansiyya` (clôture) l'emporte sur `khutta-la-tuwafiq-al-matlub` (plan global) quand le seul défaut de l'option est la clôture.
- `arabe.hijaj.awwal-ra2y-muthbat` (l'ordre fait la thèse) vs `mahdhuda-muthbata-khalt` (réfutée ↔ défendue inversées sans notion d'ordre) vs `utruha-ism-aw-su2al` (thèse = titre/question) : choisir celui dont le texte de l'option correspond.
- Emprunt au registre 6ᵉ : `arabe.sard.a3mal-at-tahawwul` pour 05#1 c (action de la tentative de solution prise pour l'événement déclencheur) ; 05#1 b/d (états initial et final pris pour le déclencheur) restent muets — le registre n'a pas d'id « état pris pour événement ».
- Pour les séquences du registre 6ᵉ (`arabe.intaj.*`, `arabe.hiwar.*`, `arabe.tafsir.*`) : non réutilisées ici — leur libellé vise la production d'un récit/dialogue en 6ᵉ, pas les éléments du texte argumentatif.
- ch10 — `arabe.hijaj.mahdhuda-bi-lisan-al-katib` (la thèse réfutée écrite avec les mots/le point de vue de l'auteur) vs `arabe.hijaj.mahdhuda-muthbata-khalt` (de ch09 : réfutée et défendue simplement inversées) : le premier quand l'option est l'avis de l'auteur sous forme négative (« ليست… ») ; le second quand l'option est franchement l'autre thèse.
- `arabe.hijaj.taqsim-al-binya-khalt` (découpage global d'un texte en thèse/démarche/conclusion) l'emporte sur `arkan-khalt` ; une option qui n'isole que « la conclusion rangée dans la démarche » prend `istintaj-dakhil-al-sayrura`.
- `arabe.hijaj.da3ima-dahida-khalt` : la question demande un argument qui SOUTIENT (ou RÉFUTE) et l'option est l'argument de l'autre sens ; si l'option est la thèse elle-même, c'est `arkan-khalt`.
- `arabe.hijaj.wazifa-min-al-mawdu3` (fonction jugée d'après le sujet) vs `arabe.hijaj.iqna3-ta2thir-khalt` (fonction jugée d'après un seul indice de l'autre bord) : voir les justifications de l'option.
- `arabe.hijaj.hukm-ra2yi-la-hijaji` (juge d'après ses goûts/le style/le sujet) vs `arabe.hijaj.ma3ayir-taqyim-khati2a` (critère d'évaluation argumentatif mais faux) : le premier ne lit pas l'argumentation du tout, le second la lit avec un mauvais critère.
- Choix de l'ensemble pour les questions de lexique : `arabe.lugha.ma3na-mashhur-bila-siyaq` ne s'applique qu'aux sens RÉELS du verbe mais hors contexte (يطرح، يرفع pour أثار) ; les options sans rapport (يمنع pour يثير ; يقرّب، يسهّل pour يحول) restent muettes.
- ch11 — `arabe.fahm.jawab-min-kharij-al-nass` (réponse hors du texte / contraire à sa logique) vs `arabe.fahm.tafsil-ka-fikra-amma` (détail du texte pris pour l'idée générale) : le premier quand l'option dit autre chose que ce que dit le texte, le second quand elle dit quelque chose de vrai mais partiel.
- Les ids `arabe.hijaj.*` du ch09 sont repris tels quels pour les questions de structure argumentative des annales (mêmes erreurs, mêmes distracteurs).
- `arabe.intaj.khatima-mawdu3-jadid` : seul 11:quiz#8 b ; les deux autres distracteurs de ce quiz (répétition littérale de l'introduction, remerciements personnels) restent muets.
- `arabe.mamdud.hamza-ta2nith-tubqa` > `arabe.mamdud.nawa3-al-hamza-khalt` : une forme concrète qui garde la hamza d'un mot de ta'nîth (حمراءان، صحراءات) prend le premier ; les options qui énoncent une règle fausse sur la catégorie de la hamza (02#3, 04#3) prennent le second.
- `arabe.mamdud.qalb-kull-hamza-waw` : réservé à la hamza NON ta'nîth rendue و d'office (عدّاوان وجوبًا) ; `arabe.mamdud.hamza-ila-ya-bila-asl` : la hamza rendue ي sans origine. Une même option ne porte jamais les deux.
- `arabe.maqsur.hamza-fi-muthanna-wal-jam3` (hamza ajoutée à un maqsur) l'emporte sur `arabe.sinf.akhir-khalt` quand l'option est une forme (عَصاءان) ; `akhir-khalt` ne sert que pour les définitions/classements.
- `arabe.sinf.mabni-ka-mu3rab` (nom indéclinable) l'emporte sur `arabe.maqsur.kull-alif-maqsura-ism` (registre : particules/verbes en ى) : مَتى، هُنا sont des noms.
- `arabe.jidhr.alif-ka-harf-asli` : l'alif est comptée comme racine ; `arabe.jidhr.ya-min-al-fi3l-al-mazid` : un ي est pris pour racine ; `arabe.jidhr.harf-zaid-fil-jidhr` : م، ت ou tanwin comptés. Une option de racine porte l'id de la lettre fautive la plus visible.
- ch13 — Pour un distracteur qui est un schème de diminutif faux : `arabe.tasghir.wazn-bi-ghayr-al-3adad` si le défaut est le NOMBRE de lettres (فُعَيْل pour 4, فُعَيْعِيل pour 4…) ; `arabe.tasghir.sighat-al-tasghir-khalt` si le défaut est le GESTE (fatha/kasra au lieu de la damma, ي voyellé).
- Pour un distracteur « origine du diminutif » faux : marque du féminin → `ta2nith-tuhdhaf-aw-tuzad` ; lettres perdues ou doublées non restaurées → `harf-asli-yasqut` ; pluriel / adjectif / autre mot → `asl-al-musaghghar-khalt`.
- `kull-musaghghar-sighar` (l'option affirme une petitesse réelle ou un sens unique « petit ») l'emporte sur `ma3na-bi-ghayr-qarina` (un des cinq autres sens choisi sans indice).
- `ta2nith-fil-3add` (compter la marque du féminin) vs `ta2nith-tuhdhaf-aw-tuzad` (la perdre ou la changer dans le diminutif) : deux gestes opposés.
- `alif-hukm-khalt` (sort de l'alif) l'emporte sur `wazn-bi-ghayr-al-3adad` quand l'option a le bon nombre de lettres mais une mauvaise lettre à la place de l'alif (عُيَيْمِل).
- ch14 — `arabe.nisba.mamdud-wa-mahdhuf-khalt` (confusion mamdud / trilitère à lettre supprimée) vs `arabe.mamdud.nawa3-al-hamza-khalt` (réutilisé de ch12 : mauvaise catégorie de hamza pour un VRAI mamdud — ابتداء، كِساء، صحراء) : le second ne s'applique que lorsque le nom est un mamdud et que l'option applique la mauvaise règle de hamza.
- `arabe.nisba.mahdhuf-la-yustaradd` (rien n'est restitué : أَبِّيّ، سَنِّيّ) vs `arabe.nisba.radd-waw-bila-mahdhuf` (restitution à tort sur un nom complet : كُوفَويّ) : deux gestes inverses.
- `arabe.nisba.tasghir-khalt` (ياء de diminutif dans une nisba) l'emporte sur `fa3ila-fath-ma-qabl` quand l'option est un schème de diminutif (قُبَيْليّ, مُدَيْنيّ) ; `fa3ila-fath-ma-qabl` ne sert que pour la lettre non ouverte (مَدْنيّ، قَبْليّ).
- `arabe.nisba.mutabaqa-na3t` : mauvais genre/cas de l'adjectif ; `arabe.nisba.idafa-bada-al-na3t` : l'option garde un complément du nom ; `arabe.nisba.min-kalima-ukhra` : l'adjectif est formé sur un autre mot.

## 4. Pièges sans id

- ch01 n°1 (juger la phrase par sa première lettre : « في البيتِ رجلٌ » est nominale) : aucun distracteur dans le chapitre n'oppose une phrase à particule initiale ; 01#1 est un classement simple de « العِلمُ نورٌ ». Le piège est enseigné mais pas testé.
- ch05 n°13 (« أَجْلَسْتُ أخي جالسًا » : garder le mot devenu partie du verbe) : AUCUN distracteur ne conserve ce mot résiduel (06#3 propose seulement d'autres verbes de la racine). Le piège est enseigné mais pas testé : il faut un distracteur neuf (hors périmètre, aucun fichier modifié) — son id candidat serait `arabe.mazid.ibqa2-al-lafz-fi-al-jumla`.
- ch05 n°1, 2ᵉ erreur (nommer la lettre doublée par sa place dans le mot, pas par sa place dans la racine : تَعَلَّمَ ← عين) : aucun distracteur ne la porte.
- ch06 n°4 (intensif bâti sur un verbe augmenté : مُعطَّاء pour مِعطَاء) : aucun distracteur ne propose une telle forme.
- ch06 n°6 (nom de lieu bâti sur مَفعَل à partir d'un verbe augmenté : مَشفى pour مُستَشفى) : aucun distracteur ; 04#3 propose d'autres confusions (ملعب, مفتاح, مجلوس).
- ch09 n°1, 2ᵉ erreur (« le مُخاطَب est toujours un adversaire ») — aucun distracteur.
- ch09 n°5, 1ʳᵉ erreur (empiler des phrases sans argument) — aucun distracteur ; la 2ᵉ (supprimer les liens) n'est approchée que par 02#1 a/c/d (contre-sens de lecture, pas production).
- ch09 n°7, 1ʳᵉ erreur (répondre par un mot sans les indices) — aucun distracteur ; le piège est porté par 01#6/02#5 sous un autre angle (juger d'après un détail).
- ch09 n°10, 1ʳᵉ erreur (formules et serment à la place de l'argument) — aucun distracteur ; l'id attaché ne couvre que la 2ᵉ erreur (question argumentative), et par le sens inverse (04#6 propose des questions réelles).
- ch09 n°12, 1ʳᵉ erreur (laisser un des deux camps sans arguments) — aucun distracteur.
- ch09 n°13, 3ᵉ erreur (« oublier la thèse de remplacement ») est portée par 06#6 b ; la déformation et la moquerie par 05#6 a/d.
- ch10 n°9 (relire le texte pour chaque question) : conseil de méthode, aucun distracteur ne peut le porter.
- ch10 n°4, 2ᵉ erreur (le شاهد comme type indépendant) et n°5, 1ʳᵉ erreur (nommer l'outil par sa nature grammaticale « حرف ») : aucun distracteur.
- ch10 n°7, 2ᵉ erreur (croire les deux fonctions exclusives) : aucun distracteur.
- ch14 n°2 (مَدينيّ / قَبيليّ avec la ياء gardée) : aucun distracteur n'offre la forme-piège ; le piège est porté (faiblement) par la variante au soukoun (04#5 d, 05#2 c) via `arabe.nisba.fa3ila-fath-ma-qabl`.

## 5. Erreurs vues < 3 fois (non retenues)

- ch01 `04#1` b/c/d (le verbe + نون النسوة, mabni sur le sukûn) — 1 question ; `04#2` a/c/d (محلّ du موصول) — 1 question ; `06#3` b (فاعل pour نائب فاعل) — 1 question.
- ch01 `01#2` b/c/d et `01#5` a/b/c (marque originelle de rafʿ / jarr) — 2 questions ; `01#4` b/c/d (fonction de الطالبَ) ; `05#5` a/c/d (pourquoi la damma est sous-entendue sur القاضي) — 1 question ; `01#1` a/c/d ; `quiz#2` a/b.
- ch05 : `01#5` (a, b, c : sens d'un تَفَعَّلَ muet sur la مطاوعة évidente) et `06#4` d, `quiz#5` d : مطاوعة NON reconnue alors qu'un fait antérieur est dans la phrase — 3 questions mais des options hétérogènes (jugées non reconstructibles) ; à reprendre si un auditeur les unifie.
- ch05 : `quiz#5` b, `02#4` d (حصول الفعل متتاليًا) ; `quiz#1` b/c, `quiz#2` a/d : options-bruit sans geste identifiable.
- ch06 `quiz#1` et `05#1` (جامد ↔ مشتقّ) — 2 questions ; `quiz#3` et `01#5` (schème du superlatif et du dérivé voisin) — 2 questions ; `02#2` a/b/c et `01#4` b/c (autres schèmes d'intensif) — 2 questions.
- ch06 `04#3` a/c, `01#3` c/d, `02#2`, `06#4` c/d : options isolées ou erronées (04#2 est ambigu dans le corpus : l'explication traite حَذِر comme intensif, ce qui contredit le tableau du cours — à signaler à l'auditeur).
- ch07 `quiz#2` b/c/d (phrases réellement littérales choisies comme figurées) ; `02#1` c/d ; `04#1` a/b/c (وجه الشبه contraire au contexte) ; `04#6` a/c (sens de الليلة الظلماء / البدر) ; `05#3` a/b/c (ordre des étapes de lecture d'une image) ; `01#6`, `06#6` b : 1 question chacun.
- ch08 `01#2` a/b/c et `01#5` d (tibāq entre mots non opposés : الشتاء/الصوف ، صباحًا/الظهيرة) — 2 questions (`arabe.badi3.tibaq-bila-tadadd`, candidat) ; `04#4` a/c (tibāq entre noms seulement / avec un pronom) ; `quiz#4`, `05#3`, `05#1`, `06#1`, `04#5` b/d, `06#6` b/c/d, `05#6` b/c/d : options isolées ou lacunes de connaissance.
- ch09 `02#2` a/b/c (nature du texte : thèse défendue seule / réfutée seule / implicite) — 1 question.
- ch09 `04#4` a/b/c (استقراء confondu avec استنباط / قياس / سلطة) — 1 question.
- ch09 `05#4` b/c/d et `06#6` a (arguments qui SOUTIENNENT la thèse à réfuter au lieu de la réfuter) — 2 questions (`arabe.hijaj.hujja-da3ima-bada-dahida`, candidat si un 3ᵉ chapitre la reproduit).
- ch09 `05#2` b (rôles de ليست et إنّ inversés) ; `06#4` a/c/d (structure du texte : quel pilier manque) ; `05#1` b/d (états initial/final pris pour le déclencheur) ; `quiz#2` c — 1 question chacun.
- ch10 `04#2` c/d, `03#6` d (antonymes ou mots sans rapport comme synonymes : يقرّب، يسهّل pour يحول ; يمنع pour يثير) — 2 questions.
- ch10 `01#1` d (l'exemple comme 4ᵉ pilier indépendant), `01#2` d (2 phrases seulement), `quiz#7` b : isolées.
- ch10 `05#3` c et `03#4` d (« pas d'expression affective / aucun chiffre dans le texte » : contre-vérités sur le texte) — 2 questions.
- ch11 `quiz#2` b/c/d (nature du texte : récit / description / exposé pour un texte argumentatif) — 1 question ; `quiz#3`, `01#3`, `02#4` c/d (fonction grammaticale) — 3 questions mais options hétérogènes ; `01#5` b/c/d (but de l'exclamation) — 1 question ; `quiz#5` c/d, `01#4` c/d, `03#3` c/d, `02#5` d : types de dérivés voisins, isolés.
- ch11 `quiz#8` c/d (conclusion qui répète l'introduction ou remercie le professeur) — 1 question.
- `02#1` (féminin de أيسر : يَسراء، يَسرى) et `05#6` (schème du féminin de أحمر/أصغر/أعرج) : mauvais schème du féminin (فَعلاء / فُعلى / فَعلى) — 2 questions, ajouter ce schéma ailleurs ou laisser muet.
- `03#4` et `04#4` : source du maqsur confondue (مصدر / اسم مكان / اسم مفعول / جمع فَعلى) — 2 questions.
- `02#4` (صحراء traité comme un nom ordinaire : kasra + tanwin) — 1 question.
- `01#5`, `01#6`, `quiz#2` : options-motifs (pourquoi le ي reste, pourquoi متى n'est pas maqsur) — raisonnements isolés, muets.
- `05#5` b/c/d : mauvais tests de classement (pluriel, nombre de lettres, fonction) — 1 question.
- `01#3` b (« tanwin seulement au nasb »), `quiz#3` d (عصاوان), `03#6` b (القاضيَ) — isolés.
- ch13 `03#4` a/c (أُبَيْو forme intermédiaire, أُبَيْب : lettre supprimée d'un nom ثنائي non rendue) : 1 question.
- ch13 `01#2` (nom de la ياء : نسبة / متكلم / مخاطبة) : 1 question ; `04#6` b-d (motifs) et `04#5` d, `03#2` b, `04#3` c, `05#6` d : sans geste identifiable.
- ch14 `01#2` b/c/d et `05#4` a/b/d : le مَنسوب إليه mal identifié (الموصوف / un autre nom) — 2 questions.
- ch14 `05#1` a/c (نسبة إلى مركّب إضافي : بِلاديّ، بلادجريديّ) — 1 question ; `03#3` b (أَيْديّ, nisba au pluriel), `quiz#5`, `03#6`, `04#3`, `04#6` : options-motifs ou isolées.

## 6. `coursePitfalls` proposés par chapitre

| chapitre | `coursePitfalls` proposés | C-5 (porté par un distracteur du chapitre) |
| --- | --- | --- |
| 01-i3rab-wal-bina | `arabe.i3rab.jarr-jazm-khalt`<br>`arabe.i3rab.haraka-bada-harf` | ✓ (2)<br>✓ (8) |
| 05-sarf-al-mizan | `arabe.mazid.tad3if-laysa-ziyada`<br>`arabe.mazid.af3ala-ja3liyya-daiman`<br>`arabe.mazid.fa33ala-takthir-aw-ja3liyya`<br>`arabe.mazid.mutawa3a-bila-fi3l-sabiq`<br>`arabe.mazid.tafa3ala-musharaka-daiman`<br>`arabe.mazid.mutawa3a-ittikhadh-khalt`<br>`arabe.mazid.if3alla-if3aalla-khalt`<br>`arabe.mazid.istaf3ala-talab-daiman`<br>`arabe.ishtiqaq.fa3il-maf3ul-ma3na`<br>`arabe.mazid.wazn-ma3na-wahid` | ✓ (3)<br>✓ (3)<br>✓ (2)<br>✓ (7)<br>✓ (3)<br>✓ (1)<br>✓ (2)<br>✓ (3)<br>✓ (1)<br>✓ (8) |
| 06-al-mushtaqqat | `arabe.ishtiqaq.wazn-fa3il-lil-mazid`<br>`arabe.ishtiqaq.mazid-haraka-al-3ayn`<br>`arabe.ishtiqaq.fa3il-mubalagha-wa-sifa`<br>`arabe.ishtiqaq.af3al-tafdil-wa-lawn-khalt`<br>`arabe.ishtiqaq.mim-ala-maftuha` | ✓ (1)<br>✓ (8)<br>✓ (3)<br>✓ (2)<br>✓ (3) |
| 07-as-suwar-al-bayania | `arabe.sura.majaz-bi-makan-al-kalima`<br>`arabe.sura.qalb-al-tarafayn`<br>`arabe.sura.isti3ara-li-ghiyab-al-ada`<br>`arabe.sura.ma3na-asli-badal-tahlil`<br>`arabe.sura.sura-hujja-tuthbit` | ✓ (4)<br>✓ (8)<br>✓ (8)<br>✓ (1)<br>✓ (12) |
| 08-al-muhassinat-al-badi3ia | `arabe.badi3.did-ma3ruf-ghayr-madhkur`<br>`arabe.badi3.saj3-yatlub-kalimatayn-mutashabihatayn`<br>`arabe.badi3.saj3-mutakallaf-3ala-hisab-al-ma3na`<br>`arabe.badi3.maqama-bi-saj3-faqat`<br>`arabe.badi3.takrir-saj3-fi-kull-jumla` | ✓ (1)<br>✓ (10)<br>✓ (7)<br>✓ (4)<br>✓ (4) |
| 09-al-intaj-al-kitabi | `arabe.hijaj.aqwal-bila-jumal-sardiyya`<br>`arabe.hijaj.awwal-ra2y-muthbat`<br>`arabe.hijaj.dahd-bila-dalil`<br>`arabe.hijaj.faqra-muqatta3a`<br>`arabe.hijaj.hadhf-al-fatiha-wal-khatm`<br>`arabe.hijaj.haqiqa-ka-qadiyya`<br>`arabe.hijaj.i3adat-al-utruha-hujja`<br>`arabe.hijaj.iqna3-ta2thir-khalt`<br>`arabe.hijaj.istidrak-khalt`<br>`arabe.hijaj.istifham-hijaji-khalt`<br>`arabe.hijaj.istintaj-dakhil-al-sayrura`<br>`arabe.hijaj.khatima-sardiyya-mansiyya`<br>`arabe.hijaj.mahdhuda-bila-badila`<br>`arabe.hijaj.mithal-hujja-kafiya`<br>`arabe.hijaj.shahid-naw3-mustaqill`<br>`arabe.hijaj.ta3lil-tafsir-khalt`<br>`arabe.hijaj.tadarruj-wa-rawabit-khalt`<br>`arabe.hijaj.tarikhi-waqi3i-khalt`<br>`arabe.hijaj.utruha-ism-aw-su2al` | ✓ (1)<br>✓ (2)<br>✓ (2)<br>✓ (1)<br>✓ (1)<br>✓ (3)<br>✓ (1)<br>✓ (6)<br>✓ (2)<br>✓ (3)<br>✓ (2)<br>✓ (1)<br>✓ (1)<br>✓ (2)<br>✓ (1)<br>✓ (5)<br>✓ (3)<br>✓ (6)<br>✓ (3) |
| 10-fahm-wa-intaj | `arabe.hijaj.hukm-ra2yi-la-hijaji`<br>`arabe.hijaj.i3adat-al-utruha-hujja`<br>`arabe.hijaj.iqna3-ta2thir-khalt`<br>`arabe.hijaj.istidrak-khalt`<br>`arabe.hijaj.istintaj-dakhil-al-sayrura`<br>`arabe.hijaj.jumla-ula-hiya-al-utruha`<br>`arabe.hijaj.mahdhuda-bi-lisan-al-katib`<br>`arabe.hijaj.mithal-hujja-kafiya`<br>`arabe.hijaj.sigha-ghayr-amina`<br>`arabe.hijaj.ta3lil-tafsir-khalt`<br>`arabe.hijaj.tarikhi-waqi3i-khalt`<br>`arabe.hijaj.wazifa-min-al-mawdu3`<br>`arabe.lugha.ma3na-mashhur-bila-siyaq` | ✓ (4)<br>✓ (2)<br>✓ (2)<br>✓ (1)<br>✓ (1)<br>✓ (1)<br>✓ (5)<br>✓ (5)<br>✓ (8)<br>✓ (1)<br>✓ (7)<br>✓ (4)<br>✓ (12) |
| 11-annales-subur | `arabe.fahm.jawab-min-kharij-al-nass`<br>`arabe.i3rab.jam3-mu2annath-nasb`<br>`arabe.intaj.khatima-mawdu3-jadid` | ✓ (10)<br>✓ (1)<br>✓ (1) |
| 12-al-maqsur-wal-manqus-wal-mamdud | `arabe.maqsur.nakira-bila-tanwin`<br>`arabe.maqsur.muthanna-thulathi-ya-daiman`<br>`arabe.manqus.hadhf-ya-ta3mim`<br>`arabe.mamdud.hamza-ta2nith-tubqa`<br>`arabe.mamdud.qalb-kull-hamza-waw`<br>`arabe.ishtiqaq.fa3il-maf3ul-ma3na`<br>`arabe.jidhr.alif-ka-harf-asli`<br>`arabe.jidhr.ya-min-al-fi3l-al-mazid`<br>`arabe.manqus.maqsur-bi-hadhf-ya` | ✓ (1)<br>✓ (1)<br>✓ (3)<br>✓ (2)<br>✓ (1)<br>✓ (1)<br>✓ (3)<br>✓ (2)<br>✓ (1) |
| 13-at-tasghir | `arabe.tasghir.wazn-bi-ghayr-al-3adad`<br>`arabe.tasghir.ta2nith-fil-3add`<br>`arabe.tasghir.mushaddad-harf-wahid`<br>`arabe.tasghir.harf-asli-yasqut`<br>`arabe.tasghir.ya-ba3d-al-thani-ta3rif`<br>`arabe.tasghir.kull-musaghghar-sighar`<br>`arabe.tasghir.ma3na-bi-ghayr-qarina` | ✓ (14)<br>✓ (3)<br>✓ (2)<br>✓ (4)<br>✓ (2)<br>✓ (5)<br>✓ (22) |
| 14-an-nisba-wal-masdar-as-sinai | `arabe.nisba.ta2-tubqa`<br>`arabe.nisba.mahdhuf-la-yustaradd`<br>`arabe.nisba.fa3ila-fath-ma-qabl`<br>`arabe.nisba.kull-iyya-masdar-sina3i`<br>`arabe.nisba.ya-bi-surat-al-khatt` | ✓ (7)<br>✓ (4)<br>✓ (2)<br>✓ (4)<br>✓ (6) |

## 7. Notes et doutes

- ch05 : `arabe.mazid.ma3na-bila-nazar-fil-jidhr` est un id « large » (≈ 35 distracteurs) : il dit une erreur de lecture réelle (choisir le sens du schème sans regarder la racine) mais l'auditeur peut préférer le scinder par schème. Les ids par schème restent prioritaires.
- ch06 `04#2` : l'explication classe حَذِر (فَعِل) parmi les intensifs alors que le cours le range avec les صفات مشبّهة ; j'ai tagué a/b/c avec `fa3il-mubalagha-wa-sifa` en suivant le piège n°3 du cours (فَعِيل = intensif possible). À faire arbitrer par l'auditeur.
- ch07/08 relus le 2026-10-12 après le commit 76471b02 de l'audit A4b (le cours 08 a été corrigé pour le السجع « في النثر خاصةً »). Aucun fichier de `content/` modifié par moi.
- Recoupement avec la partie A : `arabe.hijaj.istidrak-khalt` (ch09, lecture : confusion استدراك / تقابل / توكيد) ne fait pas doublon avec `arabe.rabt.istidrak-bi-ma-yuwafiq` (A, production : employer لكنّ pour une suite attendue) ; `arabe.hijaj.mu2ashshir-ghayr-munasib` (connecteur argumentatif non adapté) côtoie `arabe.rabt.natija-bi-ghayr-al-fa` (A, conséquence rendue par ثمّ/و) : à relire ensemble au moment de la fusion. Les chapitres A 02, 03, 19 n'étaient pas encore traités quand j'ai écrit : aucun id B n'a été croisé avec eux.
- Convention de numérotation : `CC:F#N→o` où N est le rang 1-based dans le fichier (les fichiers sont triés par difficulté, rang = qN du compilateur) ; vérifié par script contre les JSON.
- Estimation de couverture : voir le rapport de session (tags attendus ≈ 860 distracteurs sur les 11 chapitres B).
