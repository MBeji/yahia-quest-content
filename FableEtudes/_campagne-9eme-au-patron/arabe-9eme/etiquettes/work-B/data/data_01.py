NEW.update({
"arabe.i3rab.jarr-jazm-khalt":(
 "تخلطُ بين الجرِّ والجزمِ: الجرُّ للأسماءِ وحدَها والجزمُ للأفعالِ المضارعةِ وحدَها؛ فاسألْ أوّلًا: أهي اسمٌ أم فعلٌ؟",
 "Tu confonds جرّ et جزم : le جرّ ne touche que les noms, le جزم que les verbes au présent ; demande d'abord : nom ou verbe ?",
 "You mix up جرّ and جزم: genitive belongs to nouns only, jussive to present-tense verbs only; first ask: noun or verb?"),
"arabe.i3rab.harf-ghayr-munasib":(
 "تختارُ حرفَ الإعرابِ غيرَ المناسبِ: المثنّى ألفٌ (رفعًا) وياءٌ، وجمعُ المذكّرِ واوٌ (رفعًا) وياءٌ، والأسماءُ الخمسةُ واوٌ وألفٌ وياءٌ",
 "Tu prends la mauvaise lettre de déclinaison : duel ا (rafʿ) / ي ; pluriel masculin و (rafʿ) / ي ; cinq noms و (rafʿ), ا (naṣb), ي (jarr)",
 "You pick the wrong declension letter: dual ا (nominative) / ي; masculine plural و (nominative) / ي; five nouns و (nom.), ا (acc.), ي (gen.)"),
"arabe.i3rab.mamnu3-sabab-khalt":(
 "تعلّلُ جرَّ «مساجدَ» و«أحمدَ» بالفتحةِ بسببٍ آخرَ (مثنّى، جمعِ مذكّرٍ، أسماءٍ خمسةٍ): الفتحةُ نيابةً عن الكسرةِ للممنوعِ من الصّرفِ وحدَه",
 "Tu expliques la fatha au génitif de مساجدَ ou أحمدَ par une autre cause (duel, pluriel masculin, cinq noms) : seul le ممنوع من الصرف l'a pour la kasra",
 "You explain the genitive fatha of مساجدَ or أحمدَ by another cause (dual, masculine plural, five nouns): only a diptote takes a fatha for the kasra"),
"arabe.i3rab.mabni-mu3rab-khalt":(
 "تخلطُ بين المُعرَبِ (يتغيّرُ آخرُه بموقعِه) والمبنيِّ (يلزمُ حالةً): الماضي مبنيٌّ وإن تغيّر آخرُه مع الضّميرِ، والمنقوصُ والمقصورُ مُعرَبانِ بعلامةٍ مقدَّرةٍ",
 "Tu confonds مُعرَب (fin variable selon la fonction) et مبني (forme unique) : le passé est مبني même si sa fin varie avec le pronom ; manqus et maqsur : مُعرَب",
 "You confuse مُعرَب (ending changes with function) and مبني (one fixed form): the past tense is مبني even if its ending shifts; manqus and maqsur are مُعرَب"),
"arabe.i3rab.mu3tall-3alama-zahira":(
 "تكتبُ علامةً ظاهرةً على ما آخرُه حرفُ علّةٍ (يسعى ← فتحةٌ، القاضي ← كسرةٌ، يسعَ ← سكونٌ): تُقدَّرُ العلامةُ على الألفِ والياءِ، ويُجزمُ المعتلُّ بحذفِ حرفِه",
 "Tu écris une marque visible sur une lettre faible finale (يسعى ← fatha, القاضي ← kasra, يسعَ ← sukûn) : elle est sous-entendue sur ا et ي ; au jazm elle tombe",
 "You write a visible mark on a final weak letter (يسعى ← fatha, القاضي ← kasra, يسعَ ← sukun): it is implied on ا and ي; in the jussive the letter drops"),
"arabe.i3rab.af3al-khamsa-3alama":(
 "تعربُ الأفعالَ الخمسةَ (يجتهدونَ، ينجحونَ) بالضمّةِ أو بالواوِ كجمعِ المذكّرِ: علامةُ رفعِها ثبوتُ النّونِ، ونصبُها وجزمُها بحذفِها",
 "Tu déclines les cinq verbes (يجتهدونَ، ينجحونَ) par la damma ou par و comme le pluriel masculin : le rafʿ = maintien du ن ; naṣb et jazm = chute du ن",
 "You inflect the five verbs (يجتهدونَ، ينجحونَ) with a damma or a و like the masculine plural: nominative = kept ن; accusative and jussive = dropped ن"),
})
R="arabe.i3rab."
PG['01']=[(1,[],"« في البيتِ رجلٌ » : aucun distracteur n'oppose une phrase à particule initiale ; 01#1 ne contient aucune phrase commençant par une préposition ou une particule interrogative"),
 (2,[R+"jarr-jazm-khalt"],""),
 (3,[R+"haraka-bada-harf"],"id du registre 6ᵉ (الأسماء الخمسة comme le duel et le pluriel masculin : lettres, pas voyelles)")]
CP['01']=[R+"jarr-jazm-khalt",R+"haraka-bada-harf"]
C='01'
A(R+"mabni-mu3rab-khalt",C,"quiz#1","acd","R1")
A(R+"jarr-jazm-khalt",C,"quiz#2","c","R1 : « الجزم يختصّ بالأفعال »")
A(R+"haraka-bada-harf",C,"quiz#3","a")
A(R+"harf-ghayr-munasib",C,"quiz#3","bd")
A(R+"mabni-mu3rab-khalt",C,"quiz#4","abd")
A(R+"mamnu3-sabab-khalt",C,"quiz#5","acd")
A(R+"mabni-mu3rab-khalt",C,"01#3","bcd")
A(R+"haraka-bada-harf",C,"01#6","a")
A(R+"harf-ghayr-munasib",C,"01#6","cd")
A(R+"haraka-bada-harf",C,"02#1","a")
A(R+"harf-ghayr-munasib",C,"02#1","bc")
A("arabe.fi3l.hukm-bil-haraka",C,"02#2","bc","R1 : « لم أداة جزم تجزم المضارع »")
A(R+"mabni-mu3rab-khalt",C,"02#3","acd","R1 : « الماضي مبنيّ دائمًا … المضارعة معربة »")
A(R+"mamnu3-sabab-khalt",C,"02#4","acd")
A(R+"harf-ghayr-munasib",C,"02#5","ad")
A(R+"haraka-bada-harf",C,"02#5","b")
A(R+"jarr-jazm-khalt",C,"02#6","a","R1 : « الجرّ خاصّ بالأسماء »")
A(R+"mamnu3-sabab-khalt",C,"04#3","acd")
A(R+"haraka-bada-harf",C,"04#4","ac","R1 : « تجرّ بالياء نيابةً عن الكسرة … وليس بالكسرة »")
A(R+"mu3tall-3alama-zahira",C,"04#5","a","R1 : « الفتحة المقدّرة على الألف منعًا للتعذّر »")
A("arabe.fi3l.hukm-bil-haraka",C,"04#5","d","R1 : « لن حرف نصب لا جزم »")
A(R+"jam3-mu2annath-nasb",C,"04#6","a","R1 : « جمع المؤنث السالم ينصب بالكسرة »")
A(R+"harf-ghayr-munasib",C,"04#6","cd")
A(R+"mabni-mu3rab-khalt",C,"05#1","bc")
A(R+"haraka-bada-harf",C,"05#2","a")
A(R+"mamnu3-sabab-khalt",C,"05#2","c")
A(R+"harf-ghayr-munasib",C,"05#2","d")
A("arabe.fi3l.hukm-bil-haraka",C,"05#3","ab","R1 : « لا يُجزم لأنّ الجزم يكون بأدوات الجزم كـ لم »")
A(R+"mabni-mu3rab-khalt",C,"05#4","acd")
A(R+"af3al-khamsa-3alama",C,"05#6","ad","R1 : « ينجحون … مرفوع بثبوت النون »")
A(R+"harf-ghayr-munasib",C,"05#6","c")
A(R+"af3al-khamsa-3alama",C,"06#1","bcd","R1 : « معاملته كفعل صحيح الآخر … أو الخلط بجمع المذكر السالم »")
A(R+"mu3tall-3alama-zahira",C,"06#2","bc","R1 : « جزمه بالسكون كالصحيح الآخر »")
A(R+"haraka-bada-harf",C,"06#3","c","R1 : « رفعه بالضمة ونسيان أنه جمع مذكر سالم »")
A(R+"mabni-mu3rab-khalt",C,"06#4","bcd","R1 : « ظنّ أنّ ثبات آخر المنقوص والمقصور يعني البناء »")
A(R+"mu3tall-3alama-zahira",C,"06#5","b","R1 : « الخطأ الشائع: إثبات كسرة ظاهرة على المنقوص »")
A(R+"af3al-khamsa-3alama",C,"04#1","c","R1 : « مبنيّ على السكون لاتصاله بنون النسوة » — ثبوت النون ليس علامة هذا الفعل")
A(R+"mabni-mu3rab-khalt",C,"06#6","bd","R1 : « الخطأ الشائع: عدّ كلّ تغيّرٍ في الآخر إعرابًا »")
PREC+=["ch01 — `arabe.i3rab.haraka-bada-harf` (voyelle donnée au duel / pluriel masculin / cinq noms : registre 6ᵉ) l'emporte sur `arabe.i3rab.harf-ghayr-munasib` (nouveau) quand l'option est une VOYELLE (الضمّة، الكسرة) ; `harf-ghayr-munasib` quand c'est une MAUVAISE LETTRE (و au lieu de ا, ي au lieu de و…).",
"`arabe.i3rab.mu3tall-3alama-zahira` (marque visible sur ا/ي final ou السكون au lieu de la chute de la lettre faible) vs `arabe.fi3l.hukm-bil-haraka` (registre 6ᵉ : on juge le verbe d'après sa voyelle et on ignore l'outil لن/لم) : si l'option nie l'outil → `hukm-bil-haraka` ; si elle ignore la nature du verbe/nom à lettre faible → `mu3tall-3alama-zahira`.",
"`arabe.i3rab.mabni-mu3rab-khalt` (confusion maʿrab/mabni, y compris maqsur/manqus pris pour mabni) ≠ `arabe.sinf.mabni-ka-mu3rab` (ch12 : un nom mabni rangé parmi maqsur/manqus/mamdud) : sens inverses."]
SANS+=["ch01 n°1 (juger la phrase par sa première lettre : « في البيتِ رجلٌ » est nominale) : aucun distracteur dans le chapitre n'oppose une phrase à particule initiale ; 01#1 est un classement simple de « العِلمُ نورٌ ». Le piège est enseigné mais pas testé."]
LT3+=["ch01 `04#1` b/c/d (le verbe + نون النسوة, mabni sur le sukûn) — 1 question ; `04#2` a/c/d (محلّ du موصول) — 1 question ; `06#3` b (فاعل pour نائب فاعل) — 1 question.",
"ch01 `01#2` b/c/d et `01#5` a/b/c (marque originelle de rafʿ / jarr) — 2 questions ; `01#4` b/c/d (fonction de الطالبَ) ; `05#5` a/c/d (pourquoi la damma est sous-entendue sur القاضي) — 1 question ; `01#1` a/c/d ; `quiz#2` a/b."]

NEW["arabe.i3rab.af3al-khamsa-3alama"]=(
 "تخلطُ في رفعِ الأفعالِ الخمسةِ (يجتهدونَ، ينجحونَ): علامتُه ثبوتُ النّونِ لا الضمّةُ ولا الواوُ؛ ولا يُرفعُ «يكتبْنَ» بثبوتِ النّونِ لأنّه مبنيٌّ مع نونِ النّسوةِ",
 "Tu te trompes sur le rafʿ des cinq verbes (يجتهدونَ، ينجحونَ) : marque = ن maintenu, ni damma ni و ; et يكتبْنَ n'a pas de ن maintenu, il est مبني avec ن النسوة",
 "You get the nominative of the five verbs wrong (يجتهدونَ، ينجحونَ): the mark is the kept ن, not a damma or و; and يكتبْنَ has no kept ن, it is built with the feminine ن")
