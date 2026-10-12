# Rapport de fusion — vocabulaire d'erreurs de l'arabe 9ᵉ (phase 1 des tags, 2026-10-12)

> Mandat : `brief-vocab-fusion.md`. Relecteur indépendant. **Aucun fichier de `content/` modifié, aucune écriture git.**
> Livrables : `vocab-arabe9.json` (ids neufs), `affectations-arabe9.json` (poses machine), `coursePitfalls-arabe9.json` (19 chapitres), ce rapport.
> Chaîne reproductible : `work-F/load.py` (lit A `work-A/data_A.py` + B `work-B/data/*.py`), `work-F/data_compl.py` (compléments 02, 03, 19),
> `work-F/decisions.py` (toutes les décisions de cette relecture), `work-F/build.py` (écrit les trois JSON), `work-F/verify.py` (contrôle indépendant
> des trois JSON contre `content/arabic/` : option présente, jamais la clé, une option au plus une fois, tag connu, C-5, libellés ≤ 160).
> Dernier passage de `verify.py` : **0 erreur**.

## 1. Chiffres finaux

- **Ids neufs retenus : 197** (origine : A 60, A+B 2, A+compl. 1, B 106, B+fusion 1, compl. 26, fusion 1).
- **Ids du registre réutilisés : 17** : `arabe.fi3l.hukm-bil-haraka`, `arabe.i3rab.haraka-bada-harf`, `arabe.i3rab.harf-hala-ukhra`, `arabe.i3rab.jam3-mu2annath-nasb`, `arabe.ishtiqaq.fa3il-maf3ul-ma3na`, `arabe.ishtiqaq.masdar-bada-al-mushtaqq`, `arabe.ishtiqaq.mazid-haraka-al-3ayn`, `arabe.ishtiqaq.wazn-fa3il-lil-mazid`, `arabe.maqsur.al-wa-tanwin`, `arabe.maqsur.muthanna`, `arabe.maqsur.nakira-bila-tanwin`, `arabe.masdar.wazn-fi3l-akhar`, `arabe.nawasikh.mubtada-ba3d-nasikh`, `arabe.sard.3ada-hors-bidaya`, `arabe.sard.a3mal-at-tahawwul`, `arabe.sard.nihaya-hors-nihaya`, `arabe.tamyiz.idafi-tamyizi`.
- **Options posées : 1446** sur 1989 distracteurs des 19 chapitres (**72.7 %**), sur 571 questions sur 663.
- Avant fusion : A 63 + B 119 + compléments 02/03/19 27 = 209 ids neufs ; 18 absorbés par fusion, 2 créés par scission → 197.

### Répartition par chapitre

| chapitre | questions | distracteurs | options posées | % | `piege` du cours | pièges portés | `coursePitfalls` |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 01-i3rab-wal-bina | 35 | 105 | 66 | 62 % | 3 | 2 | 2 |
| 02-an-nawasikh | 35 | 105 | 91 | 86 % | 8 | 8 | 7 |
| 03-al-mansoubat | 35 | 105 | 80 | 76 % | 7 | 7 | 6 |
| 04-al-asalib | 35 | 105 | 70 | 66 % | 12 | 10 | 10 |
| 05-sarf-al-mizan | 35 | 105 | 93 | 88 % | 13 | 12 | 10 |
| 06-al-mushtaqqat | 35 | 105 | 65 | 61 % | 7 | 5 | 5 |
| 07-as-suwar-al-bayania | 35 | 105 | 87 | 82 % | 5 | 5 | 5 |
| 08-al-muhassinat-al-badi3ia | 34 | 102 | 69 | 67 % | 5 | 5 | 5 |
| 09-al-intaj-al-kitabi | 34 | 102 | 85 | 83 % | 14 | 14 | 19 |
| 10-fahm-wa-intaj | 44 | 132 | 123 | 93 % | 9 | 8 | 12 |
| 11-annales-subur | 26 | 78 | 47 | 60 % | 3 | 3 | 3 |
| 12-al-maqsur-wal-manqus-wal-mamdud | 35 | 105 | 59 | 56 % | 7 | 7 | 7 |
| 13-at-tasghir | 35 | 105 | 91 | 86 % | 7 | 7 | 7 |
| 14-an-nisba-wal-masdar-as-sinai | 35 | 105 | 70 | 66 % | 4 | 4 | 5 |
| 15-al-alaqat-bayna-al-jumal | 35 | 105 | 57 | 54 % | 16 | 12 | 16 |
| 16-al-istifham | 35 | 105 | 61 | 58 % | 9 | 8 | 8 |
| 17-ash-shart | 35 | 105 | 74 | 70 % | 11 | 11 | 11 |
| 18-dalalat-az-zaman | 35 | 105 | 81 | 77 % | 10 | 10 | 7 |
| 19-al-adad-wal-madud | 35 | 105 | 77 | 73 % | 11 | 11 | 9 |

### Ids neufs retenus seulement par un `piege` (moins de 3 questions)

`arabe.adad.3aksiyya-3-10` (2 Q), `arabe.badi3.did-ma3ruf-ghayr-madhkur` (1 Q), `arabe.badi3.maqama-bi-saj3-faqat` (2 Q), `arabe.hadhf.hukm-min-mawqi3-al-baqi` (1 Q), `arabe.hijaj.aqwal-bila-jumal-sardiyya` (1 Q), `arabe.hijaj.dahd-bila-dalil` (1 Q), `arabe.hijaj.faqra-muqatta3a` (1 Q), `arabe.hijaj.hadhf-al-fatiha-wal-khatm` (1 Q), `arabe.hijaj.haqiqa-ka-qadiyya` (1 Q), `arabe.hijaj.istifham-hijaji-khalt` (1 Q), `arabe.hijaj.khatima-sardiyya-mansiyya` (1 Q), `arabe.hijaj.mahdhuda-bila-badila` (1 Q), `arabe.hijaj.shahid-naw3-mustaqill` (1 Q), `arabe.hijaj.tadarruj-wa-rawabit-khalt` (1 Q), `arabe.i3rab.jarr-jazm-khalt` (2 Q), `arabe.intaj.khatima-mawdu3-jadid` (1 Q), `arabe.ishtiqaq.af3al-tafdil-wa-lawn-khalt` (2 Q), `arabe.ishtiqaq.fa3il-mubalagha-wa-sifa` (1 Q), `arabe.ishtiqaq.mim-ala-maftuha` (2 Q), `arabe.istifham.hal-makan-al-hamza` (1 Q), `arabe.istifham.jarr-min-al-harf-wahdah` (2 Q), `arabe.istifham.rutba-al-harf` (1 Q), `arabe.jumla.markaba-li-tul` (2 Q), `arabe.jumla.naw3-bi-fi3l` (1 Q), `arabe.manqus.hadhf-ya-ta3mim` (2 Q), `arabe.manqus.maqsur-bi-hadhf-ya` (1 Q), `arabe.mazid.af3ala-ja3liyya-daiman` (2 Q), `arabe.mazid.fa33ala-takthir-aw-ja3liyya` (2 Q), `arabe.mazid.if3alla-if3aalla-khalt` (2 Q), `arabe.mazid.mutawa3a-ittikhadh-khalt` (1 Q), `arabe.mazid.tad3if-laysa-ziyada` (2 Q), `arabe.nawasikh.laysa-harf` (1 Q), `arabe.nawasikh.nasikh-musnad` (1 Q), `arabe.nawasikh.tabdil-bila-taghyir` (2 Q), `arabe.nida.adat-bil-masafa` (1 Q), `arabe.nida.mudaf-marfu3` (1 Q), `arabe.nida.nudba-istighatha` (2 Q), `arabe.nida.rukn-thalith` (2 Q), `arabe.nida.tanwin-al-munada` (1 Q), `arabe.nisba.fa3ila-fath-ma-qabl` (2 Q), `arabe.nisba.kull-iyya-masdar-sina3i` (2 Q), `arabe.nisba.ya-bi-surat-al-khatt` (2 Q), `arabe.rabt.amma-bila-fa` (1 Q), `arabe.rabt.aw-takhyir-daiman` (1 Q), `arabe.rabt.bal-bila-nazar-fil-ula` (2 Q), `arabe.rabt.fa-wajh-wahid` (1 Q), `arabe.rabt.hatta-jam3-daiman` (1 Q), `arabe.rabt.imma-amma-khalt` (2 Q), `arabe.rabt.kull-ay-tafsir` (1 Q), `arabe.shart.fa-al-rabt-mahdhufa` (1 Q), `arabe.shart.in-madi-ka-lau` (2 Q), `arabe.shart.ism-shart-ghayr-munasib` (2 Q), `arabe.shart.jazm-fi-ghayr-mawdi3ih` (2 Q), `arabe.sura.ma3na-asli-badal-tahlil` (1 Q), `arabe.sura.majaz-bi-makan-al-kalima` (2 Q), `arabe.talab.kull-la-nahy` (2 Q), `arabe.tasghir.mushaddad-harf-wahid` (2 Q), `arabe.zaman.lau-halla-akhbar` (2 Q), `arabe.zaman.mafoul-fihi-bila-sigha` (2 Q) — 59 ids, tous énoncés par un piège du cours et portés dans le chapitre de ce piège (C-5).

## 2. Compléments 02, 03, 19 (ce que A n'avait pas fait)

Lu : `cours.md` (blocs `::: piege`) et les 105 items des trois chapitres ; ids A, B et registre réutilisés d'abord.

- **02-an-nawasikh** (8 pièges, 8 portés) — 11 ids `arabe.nawasikh.*` neufs, repris du brouillon A `ch02_labels_draft.json` (N1–N12, libellés resserrés ≤ 160) :
  `nasikh-musnad` (p1), `kull-nasikh-madi` (p2, 7 Q), `zaman-min-al-fi3l-al-thani` (p3, généralisé : temps lu sur le مضارع qui suit le ناسخ, y compris après عسى), `laysa-harf` (p4),
  `tabdil-bila-taghyir` (p5 + p8 : N5 et N8 du brouillon fusionnés, même erreur « deux ناسخ interchangeables »), `ma-zala-nafy` (p6), `muqaraba-shuru3-raja2-khalt` (p7, 8 Q),
  `sayrura-daymuma-khalt` (9 Q), `kana-qad-wal-mudari3-khalt` (6 Q), `sighat-kana-khalt` (6 Q), `dalalat-al-nasikh-khalt` (repli, 15 Q : n'est posé que si aucun des précédents ne dit l'option).
  Réutilisés A : `jumla.isnad-far3i-la-yura`, `jumla.markaba-li-tul` (04#2). Muets : 02#1→b (المسند/المسند إليه inversés, isolé), 05#1→a,c,d (verbes ordinaires pris pour ناسخ, 1 Q), options à double erreur (04#6→d, 05#6→d…).
- **03-al-mansoubat** (7 pièges, 7 portés) — 8 ids neufs + 1 de scission : `zaman.mafoul-fihi-bila-sigha` (p2), `zaman.tartib-bi-tartib-al-kalam` (p4 + p7), `zaman.adat-tazamun-asbaqiyya-khalt` (11 Q),
  `zaman.adat-zaman-3illiyya` (4 Q), `zaman.hal-waw-la-tuhaddid` (p6), `zaman.qad-madi-ihtimal` (3 Q ; l'inverse exact de `zaman.qad-sin-sawfa-khalt` de A, dont le libellé « قد = probable » aurait conforté l'erreur),
  `zaman.qimat-al-hal-khalt` (p5, 10 Q), `zaman.hal-wa-mafoul-fihi-khalt` (scission, 6 Q). Le piège 1 va à `jumla.wazifa-bila-ta3alluq` (fusion, § 3), le piège 3 à `jumla.ra2isi-bi-tartib-al-dhikr` (fusion avec l'id A de ch17).
  Réutilisé A : `zaman.zaman-min-al-sigha` (01#2→a, 02#3→d).
- **19-al-adad-wal-madud** (11 pièges, 11 portés) — 8 ids `arabe.adad.*` neufs : `naw3-bil-shakl` (p1), `siyaghat-al-rutbi-khalt` (p2), `3aksiyya-3-10` (p4), `juz2an-hukm-wahid` (p5),
  `thabat-al-3aqd-ta3mim` (p6), `murakkab-mazji-i3rab` (p7 + p9 ; couvre aussi اثنا/اثنتا عشر), `hukm-al-ma3dud-khalt` (p8, p9, p10, p11 : la forme du معدود selon la tranche), `wazifat-al-3adad-wal-ma3dud` (4 Q).
  Réutilisés du registre (libellé exact) : `tamyiz.idafi-tamyizi` (p3 : مائةِ ألفٍ / ثلاثينَ ألفًا = لترُ زيتٍ / لترًا زيتًا), `i3rab.harf-hala-ukhra` (p10 : العقد figé sur ـين), `i3rab.haraka-bada-harf` (marque du عقد par une voyelle).
  Muets : 01#1→d, 01#3, 01#4, 01#6→a,b, 03#2→b,d, 03#3→d, 05#1, 05#4, 05#5→a, 05#6, 02#3→d (erreurs isolées ou options à double erreur).

## 3. Décisions de fusion, retraits, scissions

### 3.1 Fusions et renommages (l'ancien id disparaît, ses options suivent le nouvel id)

- `arabe.shart.ra2isi-bi-tartib-al-dhikr` (A, ch17, 2 Q) → **`arabe.jumla.ra2isi-bi-tartib-al-dhikr`** : même erreur que le piège 3 de ch03 (« عدُّ الحدثِ الذي تليه الأداةُ حدثًا رئيسيًّا ») ; domaine élargi (حرف الشرط + أداة الزمن), libellé réécrit, 5 Q (17 + 03).
- `arabe.rabt.istidrak-bi-ma-yuwafiq` → **`arabe.rabt.istidrak-khalt`** : doublon de sens avec `arabe.hijaj.istidrak-khalt` (B) : même règle (le استدراك apporte le contraire de l'attendu), A en production, B en lecture.
- `arabe.hijaj.istidrak-khalt` → **`arabe.rabt.istidrak-khalt`** : fusionné avec `arabe.rabt.istidrak-bi-ma-yuwafiq` (A).
- `arabe.rabt.natija-bi-ghayr-al-fa` → **`arabe.rabt.mu2ashshir-ghayr-munasib`** : cas particulier (conséquence dite par ثمّ / و / أي) du même geste que `arabe.hijaj.mu2ashshir-ghayr-munasib` (B) : prêter à un connecteur une relation qu'il ne dit pas.
- `arabe.hijaj.mu2ashshir-ghayr-munasib` → **`arabe.rabt.mu2ashshir-ghayr-munasib`** : fusionné avec `arabe.rabt.natija-bi-ghayr-al-fa` (A) ; domaine `rabt` (أدوات الرّبط) ; les options où le استدراك est en jeu (clé ou option) passent à `arabe.rabt.istidrak-khalt` (14 options).
- `arabe.mazid.wazn-ma3na-wahid` → **`arabe.mazid.ma3na-bila-nazar-fil-jidhr`** : même erreur que l'id large de B (choisir un sens du schème sans examiner racine et phrase) vue de l'autre côté (« un schème = un sens ») ; le libellé fusionné dit les deux.
- `arabe.hijaj.awwal-ra2y-muthbat` → **`arabe.hijaj.mahdhuda-muthbata-khalt`** : cas particulier (l'ordre de mention) de la confusion المدحوضة / المثبتة ; le libellé fusionné le nomme.
- `arabe.hijaj.jumla-ula-hiya-al-utruha` → **`arabe.hijaj.taqsim-al-binya-khalt`** : 1 question : c'est un mauvais découpage (la thèse défendue rangée dans la démarche), déjà dit par `taqsim-al-binya-khalt`.
- `arabe.hijaj.istintaj-dakhil-al-sayrura` → **`arabe.hijaj.taqsim-al-binya-khalt`** : 2 questions : mauvais découpage (conclusion rangée dans la démarche) ; le libellé fusionné le nomme.
- `arabe.mamdud.qalb-kull-hamza-waw` → **`arabe.mamdud.nawa3-al-hamza-khalt`** : cas particulier (une des trois hamza traitée comme une autre) de `nawa3-al-hamza-khalt`, dont le libellé dit déjà la règle de chacune.
- `arabe.mamdud.hamza-ta2nith-tubqa` → **`arabe.mamdud.nawa3-al-hamza-khalt`** : cas particulier (une des trois hamza traitée comme une autre) de `nawa3-al-hamza-khalt`, dont le libellé dit déjà la règle de chacune.
- `arabe.mamdud.hamza-ila-ya-bila-asl` → **`arabe.mamdud.nawa3-al-hamza-khalt`** : cas particulier (une des trois hamza traitée comme une autre) de `nawa3-al-hamza-khalt`, dont le libellé dit déjà la règle de chacune.
- `arabe.maqsur.muthanna-thulathi-ya-daiman` → **`arabe.maqsur.radd-alif-bila-3add`** : erreur symétrique de `muthanna-waw-ghayr-al-asl` (même règle : compter les lettres avant de rendre l'alif) ; 1 question.
- `arabe.maqsur.muthanna-waw-ghayr-al-asl` → **`arabe.maqsur.radd-alif-bila-3add`** : fusionné avec `muthanna-thulathi-ya-daiman` ; libellé symétrique.
- `arabe.jidhr.ya-min-al-fi3l-al-mazid` → **`arabe.jidhr.alif-ka-harf-asli`** : même erreur (lettre visible prise pour la lettre de racine au lieu de remonter au trilitère) que `alif-ka-harf-asli` ; même piège 12 n°6.
- `arabe.tasghir.ya-ba3d-al-thani-ta3rif` → **`arabe.tasghir.sighat-al-tasghir-khalt`** : même règle (damma + ي sukûn ; le ي long de فَعِيل n'est pas un diminutif) que `sighat-al-tasghir-khalt`, qui cite déjà أَبِيّ et جَبِيل ; 1 question.
- `arabe.istifham.markab-jarr-khabar-aw-mutammim` → **`arabe.jumla.wazifa-bila-ta3alluq`** : même règle que le piège n°1 de ch03 (« اسألْ عمّا يتعلّقُ به المركَّبُ: أفعلٌ هو أم مبتدأٌ ») : un seul id, domaine `jumla`.
- `arabe.zaman.wazifa-min-al-ma3na` → **`arabe.jumla.wazifa-bila-ta3alluq`** : (complément 03) fusionné avec l'id A de ch16 ; les options où la حال est en jeu passent à un id propre, `arabe.zaman.hal-wa-mafoul-fihi-khalt`.
- `arabe.ishtiqaq.fa3il-mubalagha-wa-sifa` : libellé élargi à فَعِل (حَذِر), sinon l'option 06:04#2→b n'était pas dite (doute B-2).

Aucun id n'a été **retiré** pour seuil : après fusion, chaque id neuf est porté par ≥ 3 questions distinctes **ou** énoncé par un `piege` et porté dans le chapitre de ce piège (§ 1, dernière liste : 59 ids dans ce second cas).

### 3.2 Libellés réécrits (avant → après, FR ; AR et EN réécrits en parallèle, voir `vocab-arabe9.json`)

- `arabe.shart.ra2isi-bi-tartib-al-dhikr` (avant) : Tu désignes l'événement principal par l'ordre de mention (إنْ توقّفَ المطرُ لعبْنا : le 1er) : le secondaire est celui que mène le حرف الشرط, où qu'il soit
  - **après `arabe.jumla.ra2isi-bi-tartib-al-dhikr`** : Tu prends pour principal le fait dit en premier ou celui que mène l'outil : c'est celui de la phrase sans outil (حرف الشرط, أداة الزمن), où qu'elle soit
- `arabe.rabt.istidrak-bi-ma-yuwafiq` (avant) : Tu emploies لكنّ et ses sœurs pour dire ce qu'on attend (اجتهد لكنّه نجح) : l'استدراك apporte le contraire de l'attendu, sinon on relie par ف
- `arabe.hijaj.istidrak-khalt` (avant) : Tu confonds استدراك, تقابل et توكيد (بيدَ أنّ ≠ بينما، إلّا أنّ ≠ إنّ) : l'استدراك apporte le contraire de ce que la 1ʳᵉ phrase laissait attendre
  - **après `arabe.rabt.istidrak-khalt`** : Tu vois un استدراك où il n'y en a pas, ou le manques : il dit le contraire de ce que la 1re phrase faisait attendre (لكنّ، غيرَ أنّ) ; pas un contraste (بينما)
- `arabe.rabt.natija-bi-ghayr-al-fa` (avant) : Tu exprimes la conséquence avec ثمّ, و ou أي : cause et conséquence relèvent de ف ; ثمّ dit un délai, و une simple réunion, أي une explication
- `arabe.hijaj.mu2ashshir-ghayr-munasib` (avant) : Tu prends un connecteur qui ne va pas à la relation : conclusion → بناءً على ذلك ; استدراك → بيدَ أنّ ; contraste → على العكسِ ; reformulation → معنى ذلك
  - **après `arabe.rabt.mu2ashshir-ghayr-munasib`** : Tu confonds les sens des connecteurs : cause لأنّ، إذ ; conséquence ف، إذن، بناءً على ذلك ; délai ثمّ ; explication أي ; contraste بينما ; ajout علاوةً على ذلك
- `arabe.mazid.wazn-ma3na-wahid` (avant) : Tu lis le tableau comme un dictionnaire à un sens par schème (تَفَاعَلَ = toujours مشاركة) : c'est une liste de possibles ; racine et contexte tranchent
- `arabe.mazid.ma3na-bila-nazar-fil-jidhr` (avant) : Tu choisis le sens du schème sans regarder la racine : verbe, nom de chose, lieu, couleur ou qualité donnent chacun un sens différent au même schème
  - **après `arabe.mazid.ma3na-bila-nazar-fil-jidhr`** : Tu donnes au schème un sens sans voir racine ni phrase : un schème a plusieurs sens ; la racine (verbe, chose, lieu, couleur, qualité) et le contexte tranchent
- `arabe.hijaj.awwal-ra2y-muthbat` (avant) : Tu prends le 1ᵉʳ avis ou la 1ʳᵉ phrase pour la thèse défendue : l'ordre ne décide rien, c'est la position de l'auteur : il réfute cet avis ou le défend ?
- `arabe.hijaj.mahdhuda-muthbata-khalt` (avant) : Tu confonds la thèse réfutée (avis de l'adversaire, rejeté) et la thèse défendue (avis de l'auteur) : cherche « بل »، « والحقُّ أنّ »، « ليس »
  - **après `arabe.hijaj.mahdhuda-muthbata-khalt`** : Tu confonds thèse réfutée (avis de l'adversaire, souvent dit en premier) et défendue (avis de l'auteur) : l'ordre ne décide pas ; cherche بل، والحقُّ أنّ، ليس
- `arabe.hijaj.jumla-ula-hiya-al-utruha` (avant) : Tu fais de la 1ʳᵉ phrase la seule thèse et ranges la thèse défendue suivante dans la démarche : réfutée et défendue sont ensemble dans le 1ᵉʳ pilier
- `arabe.hijaj.istintaj-dakhil-al-sayrura` (avant) : Tu ranges la conclusion dans la démarche argumentative ou en fais une 2ᵉ thèse : c'est un élément à part qui tire le bilan des arguments sans en ajouter
- `arabe.hijaj.taqsim-al-binya-khalt` (avant) : Tu découpes mal thèse, démarche, conclusion : la thèse est un avis (réfutée + défendue si deux), la démarche = arguments et exemples, la conclusion clôt
  - **après `arabe.hijaj.taqsim-al-binya-khalt`** : Tu découpes mal le texte : la thèse est un avis (réfutée + défendue ensemble s'il y en a deux) ; démarche = arguments et exemples ; la conclusion est à part
- `arabe.jidhr.ya-min-al-fi3l-al-mazid` (avant) : Tu prends le ي visible pour une lettre de la racine (ر ج ي، س ه ي) : le verbe à 5 lettres met toujours ي ; lis l'origine dans le trilitère (رَجَوتُ)
- `arabe.jidhr.alif-ka-harf-asli` (avant) : Tu comptes l'alif comme lettre de la racine (ر ج ا، ر ع ا، س ا ه) : l'alif final vient d'un و ou d'un ي ; remonte au verbe trilitère (رَجَوتُ)
  - **après `arabe.jidhr.alif-ka-harf-asli`** : Tu prends l'alif ou le ي visibles pour des lettres de la racine (ر ج ا، ر ج ي) : l'alif final vient d'un و ou d'un ي ; remonte au trilitère (رَجَوتُ ← ر ج و)
- `arabe.tasghir.ya-ba3d-al-thani-ta3rif` (avant) : Tu juges qu'il y a diminutif dès qu'un ي suit la 2ᵉ lettre (الوَلِيد، أَمِين) : c'est le ي long du schème فَعِيل ; celui du diminutif est sukûn après une damma
- `arabe.tasghir.sighat-al-tasghir-khalt` (avant) : Tu te trompes sur les deux gestes : damma sur la 1ʳᵉ lettre puis ي sukûn après la 2ᵉ (جَبِيل، أَبِيّ، دِرَيْهَم) ; fatha, kasra ou ي voyellé n'en font pas
  - **après `arabe.tasghir.sighat-al-tasghir-khalt`** : Tu reconnais ou formes mal le diminutif : damma sur la 1re lettre, ي sukûn après la 2e (جُبَيْل) ; le ي long de فَعِيل (أَمِين), fatha ou kasra n'en font pas
- `arabe.istifham.markab-jarr-khabar-aw-mutammim` (avant) : Tu traites le مركّب جرّ sans voir s'il y a un verbe : avec verbe, c'est son complément ; sans verbe, un خبر مقدّم suivi d'un مبتدأ مؤخّر, pas d'un فاعل
- `arabe.zaman.wazifa-min-al-ma3na` (avant) : Tu fixes la fonction du groupe de temps par son sens ou sa place : rattaché à un verbe → مفعول فيه ; complète un مبتدأ sans verbe → خبر ; décrit l'état → حال
  - **après `arabe.jumla.wazifa-bila-ta3alluq`** : Tu fixes la fonction d'un groupe (جارّ ومجرور، ظرف) par son sens ou sa place sans voir s'il y a un verbe : verbe → son متمّم ; sinon → خبر, le nom est مبتدأ
- `arabe.ishtiqaq.fa3il-mubalagha-wa-sifa` (avant) : Tu ranges tout فَعِيل ou فَعُول parmi les صفات مشبّهة (عَلِيم، غَيُور) : ce peut être un intensif ; stabilité → صفة مشبّهة, abondance de l'action → intensif
  - **après `arabe.ishtiqaq.fa3il-mubalagha-wa-sifa`** : Tu ranges tout فَعِيل, فَعُول ou فَعِل parmi les صفات مشبّهة (عَلِيم، غَيُور، حَذِر) : ce sont aussi des intensifs ; stabilité → صفة, abondance → intensif

### 3.3 Options re-taguées (l'id posé ne disait pas exactement l'erreur)

- `03:02#6→c` → `arabe.zaman.hal-wa-mafoul-fihi-khalt` — la حال est en jeu (clé ou option)
- `03:05#4→d` → `arabe.zaman.hal-wa-mafoul-fihi-khalt` — la حال est en jeu (clé ou option)
- `03:06#1→a` → `arabe.zaman.hal-wa-mafoul-fihi-khalt` — la حال est en jeu (clé ou option)
- `03:06#4→d` → `arabe.zaman.hal-wa-mafoul-fihi-khalt` — la حال est en jeu (clé ou option)
- `03:06#5→b` → `arabe.zaman.hal-wa-mafoul-fihi-khalt` — la حال est en jeu (clé ou option)
- `03:06#5→c` → `arabe.zaman.hal-wa-mafoul-fihi-khalt` — la حال est en jeu (clé ou option)
- `03:06#5→d` → `arabe.zaman.hal-wa-mafoul-fihi-khalt` — la حال est en jeu (clé ou option)
- `03:quiz#2→c` → `arabe.zaman.hal-wa-mafoul-fihi-khalt` — la حال est en jeu (clé ou option)
- `03:quiz#5→d` → `arabe.zaman.hal-wa-mafoul-fihi-khalt` — la حال est en jeu (clé ou option)
- `05:05#5→d` → `arabe.mazid.wazn-qarib-khalt` — « مُفْتَعَل » pour le patient d'اسْتَخْرَجَ : c'est le schème voisin du tableau (افْتَعَلَ pour اسْتَفْعَلَ), exactement le libellé de `wazn-qarib-khalt` ; `arabe.ishtiqaq.min-fi3l-akhar` (6ᵉ : dériver d'un autre verbe) ne le disait pas
- `07:05#2→b` → `arabe.sura.tashbih-isti3ara-khalt` — « quel pilier peut tomber ? » : ôter un des deux termes fait une استعارة — c'est la règle de `tashbih-isti3ara-khalt`, pas un pilier mal nommé
- `07:05#2→c` → `arabe.sura.tashbih-isti3ara-khalt` — « quel pilier peut tomber ? » : ôter un des deux termes fait une استعارة — c'est la règle de `tashbih-isti3ara-khalt`, pas un pilier mal nommé
- `07:05#2→d` → `arabe.sura.tashbih-isti3ara-khalt` — « quel pilier peut tomber ? » : ôter un des deux termes fait une استعارة — c'est la règle de `tashbih-isti3ara-khalt`, pas un pilier mal nommé
- `09:05#1→b` → `arabe.sard.3ada-hors-bidaya` — « كانَ الحيُّ نائمًا » (situation initiale) pris pour le حدث قادح : libellé 6ᵉ exact
- `09:05#1→d` → `arabe.sard.nihaya-hors-nihaya` — « عادَ الهدوءُ… » (état final) pris pour le حدث قادح : libellé 6ᵉ exact
- `09:05#2→d` → `arabe.rabt.istidrak-khalt` — le استدراك est la clé ou l'option
- `09:05#3→a` → `arabe.rabt.istidrak-khalt` — le استدراك est la clé ou l'option
- `09:06#1→a` → `arabe.hijaj.taqsim-al-binya-khalt` — question de découpage (أطروحة / سيرورة / استنتاج), pas de nature d'un élément
- `09:06#2→b` → `arabe.hijaj.naw3-al-hujja-khalt` — argument d'autorité pris pour « واقعيّة » : ce n'est pas la confusion تاريخيّة / واقعيّة
- `09:quiz#4→b` → `arabe.hijaj.naw3-al-hujja-khalt` — argument d'autorité pris pour « واقعيّة » : ce n'est pas la confusion تاريخيّة / واقعيّة
- `09:quiz#5→a` → `arabe.rabt.istidrak-khalt` — le استدراك est la clé ou l'option
- `09:quiz#5→c` → `arabe.rabt.istidrak-khalt` — le استدراك est la clé ou l'option
- `10:01#1→a` → `arabe.hijaj.taqsim-al-binya-khalt` — question de découpage (أطروحة / سيرورة / استنتاج), pas de nature d'un élément
- `10:01#1→b` → `arabe.hijaj.taqsim-al-binya-khalt` — question de découpage (أطروحة / سيرورة / استنتاج), pas de nature d'un élément
- `10:01#2→b` → `arabe.hijaj.taqsim-al-binya-khalt` — question de découpage (أطروحة / سيرورة / استنتاج), pas de nature d'un élément
- `10:04#1→d` → `arabe.rabt.istidrak-khalt` — le استدراك est la clé ou l'option
- `10:quiz#5→b` → `arabe.hijaj.naw3-al-hujja-khalt` — argument d'autorité pris pour « واقعيّة » : ce n'est pas la confusion تاريخيّة / واقعيّة
- `10:quiz#6→a` → `arabe.rabt.istidrak-khalt` — le استدراك est la clé ou l'option
- `10:quiz#6→c` → `arabe.rabt.istidrak-khalt` — le استدراك est la clé ou l'option
- `10:quiz#6→d` → `arabe.rabt.istidrak-khalt` — le استدراك est la clé ou l'option
- `11:02#2→b` → `arabe.rabt.istidrak-khalt` — le استدراك est la clé ou l'option
- `11:02#2→c` → `arabe.rabt.istidrak-khalt` — le استدراك est la clé ou l'option
- `11:02#2→d` → `arabe.rabt.istidrak-khalt` — le استدراك est la clé ou l'option
- `11:quiz#6→b` → `arabe.rabt.istidrak-khalt` — le استدراك est la clé ou l'option
- `11:quiz#6→c` → `arabe.rabt.istidrak-khalt` — le استدراك est la clé ou l'option
- `11:quiz#6→d` → `arabe.rabt.istidrak-khalt` — le استدراك est la clé ou l'option

### 3.4 Options rendues muettes

- `01:05#1→b` — distracteurs absurdes (« المعربة تُنصب فقط… », « المعربة هي الحروف فقط ») : aucune erreur d'élève reconstructible (R1–R3)
- `01:05#1→c` — distracteurs absurdes (« المعربة تُنصب فقط… », « المعربة هي الحروف فقط ») : aucune erreur d'élève reconstructible (R1–R3)
- `01:quiz#1→c` — distracteurs absurdes (« المعربة تُنصب فقط… », « المعربة هي الحروف فقط ») : aucune erreur d'élève reconstructible (R1–R3)
- `01:quiz#1→d` — distracteurs absurdes (« المعربة تُنصب فقط… », « المعربة هي الحروف فقط ») : aucune erreur d'élève reconstructible (R1–R3)
- `06:04#1→d` — « le verbe de six lettres ne forme pas de nom de patient » : croyance fausse que `mazid-haraka-al-3ayn` (6ᵉ) ne dit pas
- `11:03#2→b` — `nawasikh.ism-khabar-maqlub` (6ᵉ) parle d'un خبر avancé (في البيت) suivi d'un nom indéfini : ce n'est pas le cas ici ; 2 questions, sous le seuil pour un id neuf
- `11:quiz#4→b` — `nawasikh.ism-khabar-maqlub` (6ᵉ) parle d'un خبر avancé (في البيت) suivi d'un nom indéfini : ce n'est pas le cas ici ; 2 questions, sous le seuil pour un id neuf
- `11:quiz#4→c` — `nawasikh.ism-khabar-maqlub` (6ᵉ) parle d'un خبر avancé (في البيت) suivi d'un nom indéfini : ce n'est pas le cas ici ; 2 questions, sous le seuil pour un id neuf
- `12:05#2→c` — « لِقاءٌ » pour un nom de lieu : `masdar-bada-al-mushtaqq` (6ᵉ) ne parle que du nom d'agent / de patient ; erreur isolée

## 4. Points du mandat

- **Doublons A/B nommés au mandat** : `arabe.hijaj.istidrak-khalt` + `arabe.rabt.istidrak-bi-ma-yuwafiq` → **`arabe.rabt.istidrak-khalt`** ; `arabe.hijaj.mu2ashshir-ghayr-munasib` + `arabe.rabt.natija-bi-ghayr-al-fa` → **`arabe.rabt.mu2ashshir-ghayr-munasib`**. Partage : `istidrak-khalt` dès que le استدراك est la clé ou l'option (B avait mis la moitié de ces options sous `mu2ashshir`), `mu2ashshir-ghayr-munasib` pour les autres relations ; `hijaj.ta3lil-tafsir-khalt` (pièges 09 n°8, 10 n°5) reste prioritaire sur `mu2ashshir` pour le couple تعليل / تفسير.
- **Autres quasi-doublons fusionnés** : mamdud (3 ids → `nawa3-al-hamza-khalt`), maqsur au duel (2 → `radd-alif-bila-3add`), racine (2 → `jidhr.alif-ka-harf-asli`), diminutif (2 → `sighat-al-tasghir-khalt`), thèse réfutée/défendue (2 → `mahdhuda-muthbata-khalt`), découpage (3 → `taqsim-al-binya-khalt`), sens du schème (2 → `ma3na-bila-nazar-fil-jidhr`), fonction « verbe ou pas » (A 16 + compl. 03 → `jumla.wazifa-bila-ta3alluq`), événement principal (A 17 + compl. 03 → `jumla.ra2isi-bi-tartib-al-dhikr`). Comparés aux 122 `arabe.*` du registre : aucun id neuf ne redit un id existant ; trois erreurs du 19 et deux du 09 passent au registre (§ 2, § 3.3).
- **Ids larges** (toutes leurs options relues, § 5) :
  - `arabe.mazid.ma3na-bila-nazar-fil-jidhr` (40 options après fusion avec `wazn-ma3na-wahid`) : **gardé**, libellé réécrit (« un schème a plusieurs sens ; racine ET contexte tranchent ») ; l'ancien ne parlait que de la racine alors que استحسن / اشتوى / استنجد se tranchent au contexte. Une option sortie (05:05#5→d, § 3.3). Les ids par schème (`af3ala-ja3liyya-daiman`, `istaf3ala-talab-daiman`, `tafa3ala-musharaka-daiman`, `mutawa3a-bila-fi3l-sabiq`…) restent prioritaires.
  - `arabe.hijaj.arkan-khalt` (35 options) : **gardé** (chaque option confond deux des quatre éléments, le libellé les nomme) ; les 4 options qui portent sur le **découpage** passent à `taqsim-al-binya-khalt`.
  - `arabe.rabt.mu2ashshir-ghayr-munasib` : 14 options passent à `istidrak-khalt`, libellé réécrit en table relation → connecteur (il manquait cause, délai, ajout).
  - `arabe.hijaj.naw3-al-hujja-khalt` (24) et `arabe.hijaj.tarikhi-waqi3i-khalt` : 3 options « autorité prise pour واقعيّة » sorties de `tarikhi-waqi3i` (qui ne dit que historique/réel et le passé de « قال ») vers `naw3-al-hujja`.
  - `arabe.sura.rukn-ghayr-munasib` (18) : gardé ; 07:05#2→b,c,d (quel pilier peut tomber) passent à `tashbih-isti3ara-khalt`.
  - `arabe.tasghir.ma3na-bi-ghayr-qarina` (22), `arabe.i3rab.mabni-mu3rab-khalt` (18 après 4 options absurdes rendues muettes), `arabe.nawasikh.dalalat-al-nasikh-khalt` (23, repli de ch02) : gardés, chaque option dit l'erreur nommée.
- **Doute B-4 (réutilisations du 6ᵉ)** :
  - `arabe.ishtiqaq.mazid-haraka-al-3ayn` : **gardé** sur 7 options (la règle « voyelle avant la dernière lettre » est exactement l'enjeu) ; 06:04#1→d rendue muette (croyance « le verbe de six lettres n'a pas de nom de patient », que le libellé ne dit pas).
  - `arabe.fi3l.hukm-bil-haraka` : **gardé** sur ses 5 options de ch01 (« لن تجزم », مجزوم/مرفوع/منصوب confondus : c'est l'outil qui décide).
  - `arabe.sard.a3mal-at-tahawwul` : **gardé** sur 09:05#1→c (la réaction des voisins prise pour le حدث قادح = action du تحوّل placée à son début) ; les deux autres options de la même question reçoivent `sard.3ada-hors-bidaya` et `sard.nihaya-hors-nihaya`, exacts.
  - Sortis : `arabe.ishtiqaq.min-fi3l-akhar` (→ `mazid.wazn-qarib-khalt`), `arabe.nawasikh.ism-khabar-maqlub` (muet : le libellé parle d'un خبر avancé), `masdar-bada-al-mushtaqq` sur un nom de lieu (muet).
- **Doute B-2 — `06:exercices/04-defi.json#2` (حَذِر)** : **ni l'item ni l'explication ne sont faux.** Le prémisse de B est inexact : le cours range bien حَذِر parmi les صيغ المبالغة (tableau « صيغ المبالغة », ligne فَعِل : « حَذِر، يَقِظ »), et l'usage grammatical classique en fait l'exemple-type du cinquième schème d'intensif (فَعِل) ; ce qui est vrai, c'est que فَعِل figure AUSSI dans la définition de la صفة مشبّهة (« فَعِل، فَعْلان، فَعِيل، أَفعَل، فَعَل »). L'explication (« مشترك ؛ يُعدّ في الغالب صيغة مبالغة ») est donc juste, mais l'item repose sur un schème ambigu : **recommandation** (hors périmètre) — remplacer « حَذِر » par un intensif non ambigu (صَبُور ou سَمِيع) pour que l'option b ne soit plus défendable. Le tag reste posé (`fa3il-mubalagha-wa-sifa`, libellé élargi à فَعِل), le 9ᵉ ne disposant pas du manuel (06 = révision hors livre).

## 5. Échantillon vérifié

- **Toutes les options des 8 ids larges** relues une à une (mazid.ma3na-bila-nazar-fil-jidhr, hijaj.arkan-khalt, rabt.mu2ashshir-ghayr-munasib, hijaj.naw3-al-hujja-khalt, sura.rukn-ghayr-munasib, tasghir.ma3na-bi-ghayr-qarina, i3rab.mabni-mu3rab-khalt, nawasikh.dalalat-al-nasikh-khalt) : ≈ 200 options ; corrections : § 3.3 et § 3.4.
- **Tirage aléatoire de 76 options hors ids larges, 4 par chapitre sur les 19** (graine 20261012) : pour chacune, option fausse ? id exact ? → **76 options fausses, 73 ids exacts, 3 limites mais gardés** :
  `08:exercices/06#2→c` (« seul le style libre prouve » sous `sura.sura-hujja-tuthbit` : l'erreur est bien « le style prouve », mais en sens inverse),
  `08:exercices/04#3→c` (sous `saj3-mutakallaf-3ala-hisab-al-ma3na` : l'option garde la phrase hors sujet, elle sacrifie bien le sens, mais au saj' déjà retiré),
  `14:exercices/04#2→c` (« ابتدايّ » sous `mamdud.nawa3-al-hamza-khalt`, libellé illustré au duel alors que l'item est une نسبة ; la règle « l'originelle reste » est la même).
- Compléments 02/03/19 : 248 poses, toutes écrites option par option sur le texte des items.
- Contrôle machine (`verify.py`) des 1446 poses : option présente, jamais la clé, une option au plus une fois, tag au registre ou au vocabulaire ; `coursePitfalls` : 19 chapitres, chaque id énoncé par un piège du chapitre et porté par une pose du chapitre.

## 6. `coursePitfalls` et pièges sans id

Chaque chapitre a au moins un `coursePitfalls` porté (aucun chapitre sans piège taggable). Pièges **sans id porté dans leur chapitre** (12) : 01-i3rab-wal-bina n°1, 04-al-asalib n°8, 04-al-asalib n°10, 05-sarf-al-mizan n°13, 06-al-mushtaqqat n°4, 06-al-mushtaqqat n°6, 10-fahm-wa-intaj n°9, 15-al-alaqat-bayna-al-jumal n°8, 15-al-alaqat-bayna-al-jumal n°12, 15-al-alaqat-bayna-al-jumal n°14, 15-al-alaqat-bayna-al-jumal n°15, 16-al-istifham n°6.
Raisons (relevées par A et B, vérifiées) : aucun distracteur ne reconstruit l'erreur — 15 n°8 (« نعم/لا » après أم), 15 n°12 (إذا فجائيّة), 15 n°14 (« الصّدقَ الصّدقَ » à compléter), 15 n°15 (nommer le présent au lieu du manquant), 16 n°6 (« ؟ » après لا أدري), 04 n°8 (دعاء réduit au nominatif), 04 n°10 (أمر par مصدر ou expression), 05 n°13 (mot résiduel dans أجلستُ أخي جالسًا), 06 n°4 et n°6 (intensif / nom de lieu bâtis sur un verbe augmenté), 01 n°1 (phrase jugée à sa 1re lettre), 10 n°9 (conseil de méthode). Pour les tagger, il faut un distracteur neuf (hors périmètre de cette phase).

## 7. Doutes restants

- **Taux de pose 72,7 %** : élevé ; il vient surtout des chapitres de lecture (10 : 93 %, 05 : 88 %) où presque chaque distracteur est construit sur une confusion nommée. Les ids larges gardés (§ 4) sont des replis exacts, pas des étiquettes vagues, mais un relecteur pédagogique peut préférer laisser muettes leurs options les plus faibles.
- **Options à double erreur** : la règle suivie dans les compléments (muette) n'a pas été appliquée systématiquement aux poses A et B ; quelques-unes restent (p. ex. `09:exercices/06#2→d` « واقعيّة + استنتاج » sous `mu2ashshir`). Sans effet sur C-5, à revoir au moment de poser.
- **`jumla.wazifa-bila-ta3alluq`** réunit l'id A de ch16 (مركّب جرّ en tête de question) et le piège 1 de ch03 (groupe de temps) : même règle, mais la précédence avec `istifham.wazifa-bila-jawab` (nom interrogatif) reste à respecter à la pose (A § 3).
- **Chapitres 07 et 08** relus par B après l'audit A4b ; aucune pose n'y vise une option disparue (contrôle machine), mais un nouvel audit des items invaliderait des lignes de `affectations-arabe9.json` : relancer `work-F/build.py` + `verify.py` avant d'appliquer.
- Les libellés AR sont vocalisés aux endroits où la حركة est l'enjeu ; une relecture d'un arabisant natif sur les 26 libellés neufs des compléments, les 2 de scission et les 10 réécrits reste souhaitable.
