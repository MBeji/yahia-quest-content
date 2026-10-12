# Compléments 02, 03, 19 (fusion 2026-10-12). Format : NEWC[id]=(ar,fr,en) ; AC(id,ch,'f#q','opts') ; PGC[ch][k]=[ids]
NEWC={}; ASC=[]; PGC={}
def AC(i,ch,q,opts):
    for o in opts: ASC.append((i,ch,q,o))
# ============================ CH 02 — النواسخ ============================
NEWC['arabe.nawasikh.nasikh-musnad']=(
 "تعدُّ النّاسخَ هو المسندَ (كادَ مسندٌ والطّفلُ مسندٌ إليه): المسندُ هو الخبرُ (يبكي)، والنّاسخُ يعيّنُ زمانَ الإسنادِ؛ انزعْه تبقَ جملةٌ تامّةٌ",
 "Tu prends le ناسخ pour le مسند (كادَ مسند, الطّفل مسند إليه) : le مسند est le خبر (يبكي), le ناسخ date l'attribution ; retire-le, la phrase reste",
 "You take the ناسخ for the مسند (كادَ as مسند): the مسند is the خبر (يبكي); the ناسخ only dates the attribution; remove it and the sentence stands")
NEWC['arabe.nawasikh.kull-nasikh-madi']=(
 "تحسبُ كلَّ ناسخٍ ماضيًا لأنّ أصلَه ماضٍ: «ستكونُ» مضارعٌ، «كُنْ» أمرٌ، «يكادُ» مضارعٌ، و«عسى» ماضيةٌ في الصّيغةِ مستقبليّةٌ في الزّمانِ",
 "Tu prends tout ناسخ pour un passé car son origine l'est : ستكونُ est un présent, كُنْ un ordre, يكادُ un présent, عسى est passé de forme mais futur de sens",
 "You take every ناسخ for a past because its root is: ستكونُ is a present, كُنْ an order, يكادُ a present; عسى is past in form but future in time")
NEWC['arabe.nawasikh.zaman-min-al-fi3l-al-thani']=(
 "تحكمُ على الزّمانِ من المضارعِ بعدَ النّاسخِ وحدَه (كانتِ الفرقةُ تعزفُ: حاضرٌ): النّاسخُ يعيّنُ الزّمانَ، وبعدَ «كانَ» فالمضارعُ حدثٌ استمرَّ في الماضي",
 "Tu dates le fait d'après le seul مضارع qui suit le ناسخ (كانتِ الفرقةُ تعزفُ : présent) : le ناسخ fixe le temps ; après كانَ, le مضارع a duré dans le passé",
 "You date the event from the مضارع after the ناسخ alone (كانتِ الفرقةُ تعزفُ: present): the ناسخ sets the time; after كانَ the مضارع went on in the past")
NEWC['arabe.nawasikh.laysa-harf']=(
 "تعدُّ «ليسَ» حرفَ نفيٍ أو تعلِّلُ فعليّتَها بالنّفيِ أو الانقضاءِ أو الموقعِ: الدّليلُ أنّ ضميرَ الفاعلِ يتّصلُ بها (لستُ كما كنتُ)",
 "Tu prends ليسَ pour une particule, ou prouves qu'elle est verbe par la négation, l'achèvement ou la place : la preuve est le pronom sujet attaché (لستُ)",
 "You take ليسَ for a particle, or prove it is a verb by negation, completion or position: the proof is the attached subject pronoun (لستُ)")
NEWC['arabe.nawasikh.tabdil-bila-taghyir']=(
 "تعدُّ ناسخَينِ بمعنًى واحدٍ لأنّ الاسمَ والخبرَ لم يتغيّرا (كانَ وصارَ، ظلَّ وأصبحَ): لكلِّ ناسخٍ دلالتُه، فإذا بدّلتَه تبدّلَ المعنى؛ «صارَ» حالةٌ جديدةٌ",
 "Tu crois deux ناسخ interchangeables car nom et خبر restent (كانَ/صارَ، ظلَّ/أصبحَ) : chacun a son sens, le changer change la phrase ; صارَ = état nouveau",
 "You treat two ناسخ as interchangeable since noun and خبر stay (كانَ/صارَ، ظلَّ/أصبحَ): each has its sense, swapping changes it; صارَ = a new state")
NEWC['arabe.nawasikh.ma-zala-nafy']=(
 "تقرأُ «ما زالَ» وأخواتِها نفيًا لأنّ في أوّلِها «ما»: «ما» جزءٌ من الفعلِ تنفي الانقطاعَ لا الحالةَ، فالحالةُ باقيةٌ (ما زالَ الصّفُّ هادئًا)",
 "Tu lis ما زالَ et ses sœurs comme une négation à cause de ما : il fait partie du verbe et nie l'interruption, pas l'état, qui demeure (ما زالَ الصّفُّ هادئًا)",
 "You read ما زالَ and its sisters as negations because of ما: it is part of the verb and negates the break, not the state, which lasts (ما زالَ الصّفُّ هادئًا)")
NEWC['arabe.nawasikh.muqaraba-shuru3-raja2-khalt']=(
 "تخلطُ بين المقاربةِ (كادَ: قَرُبَ ولم يقعْ) والشّروعِ (أخذَ: بدأَ فعلًا) والرّجاءِ (عسى: ممكنٌ في المستقبلِ): اسألْ هل وقعَ الحدثُ أو بدأَ؟",
 "Tu confonds مقاربة (كادَ : proche, non advenu), شروع (أخذَ : commencé) et رجاء (عسى : possible plus tard) : demande si le fait a eu lieu ou commencé",
 "You mix up مقاربة (كادَ: near, not happened), شروع (أخذَ: begun) and رجاء (عسى: possible later): ask whether the event happened or began")
NEWC['arabe.nawasikh.sayrura-daymuma-khalt']=(
 "تخلطُ بين الصّيرورةِ والدّيمومةِ: اسألْ هل الحالةُ التي يذكرُها الخبرُ جديدةٌ (صارَ، أصبحَ، أمسى…) أم باقيةٌ كانَ عليها قبلُ (ظلَّ، ما زالَ…)؟",
 "Tu confonds صيرورة et ديمومة : demande si l'état dit par le خبر est nouveau (صارَ، أصبحَ، أمسى…) ou persistant, déjà là avant (ظلَّ، ما زالَ…)",
 "You mix up صيرورة and ديمومة: ask if the state named by the خبر is new (صارَ، أصبحَ، أمسى…) or lasting, already there before (ظلَّ، ما زالَ…)")
NEWC['arabe.nawasikh.kana-qad-wal-mudari3-khalt']=(
 "تخلطُ بين «كانَ + قد + ماضٍ» (حدثٌ انقضى في الماضي البعيدِ) و«كانَ + مضارعٌ» (حدثٌ استمرَّ في الماضي)، أو تسوّي بينهما لأنّ «كانَ» ماضيةٌ فيهما",
 "Tu confonds كانَ + قد + passé (fait achevé dans un passé lointain) et كانَ + مضارع (fait qui a duré), ou les égales car كانَ est passé dans les deux",
 "You mix up كانَ + قد + past (completed in the distant past) and كانَ + مضارع (went on in the past), or equate them because كانَ is past in both")
NEWC['arabe.nawasikh.sighat-kana-khalt']=(
 "تخلطُ بين دلالاتِ صيغِ «كانَ»: الماضي انقضاءُ الكينونةِ، والمضارعُ المرفوعُ عدمُ انقضائِها، والأمرُ طلبُها، و«ليسَ» نفيُها",
 "Tu confonds le sens des formes de كانَ : passé = être achevé, مضارع مرفوع = non achevé, impératif = être demandé, et ليسَ = être nié",
 "You mix up what the forms of كانَ say: past = being completed, مضارع مرفوع = not completed, imperative = being requested, and ليسَ = being denied")
NEWC['arabe.nawasikh.dalalat-al-nasikh-khalt']=(
 "تخلطُ بين دلالاتِ النّواسخِ: كانَ كينونةٌ، ليسَ نفيُها، صارَ وأخواتُها صيرورةٌ، ظلَّ وأخواتُها ديمومةٌ، كادَ مقاربةٌ، أخذَ شروعٌ، عسى رجاءٌ",
 "Tu confonds les sens des ناسخ : كانَ être, ليسَ non-être, صارَ… devenir, ظلَّ… durée, كادَ proximité, أخذَ commencement, عسى espoir",
 "You mix up the senses of the ناسخ: كانَ being, ليسَ non-being, صارَ… becoming, ظلَّ… duration, كادَ nearness, أخذَ onset, عسى hope")
PGC['02']={1:['arabe.nawasikh.nasikh-musnad'],2:['arabe.nawasikh.kull-nasikh-madi'],3:['arabe.nawasikh.zaman-min-al-fi3l-al-thani'],
 4:['arabe.nawasikh.laysa-harf'],5:['arabe.nawasikh.tabdil-bila-taghyir'],6:['arabe.nawasikh.ma-zala-nafy'],
 7:['arabe.nawasikh.muqaraba-shuru3-raja2-khalt'],8:['arabe.nawasikh.tabdil-bila-taghyir']}
C='02'
AC('arabe.nawasikh.nasikh-musnad',C,'02#1','ac')
for q in ['quiz#1:a','01#5:b','05#2:a','02#4:b','04#6:c','06#4:c','06#3:c']:
    a,b=q.split(':'); AC('arabe.nawasikh.kull-nasikh-madi',C,a,b)
for q in ['01#6:b','quiz#4:b','02#4:c','06#4:b']:
    a,b=q.split(':'); AC('arabe.nawasikh.zaman-min-al-fi3l-al-thani',C,a,b)
AC('arabe.nawasikh.laysa-harf',C,'04#5','abd')
AC('arabe.nawasikh.tabdil-bila-taghyir',C,'02#6','b'); AC('arabe.nawasikh.tabdil-bila-taghyir',C,'06#5','c')
for q in ['01#3:a','02#5:a','04#4:a']:
    a,b=q.split(':'); AC('arabe.nawasikh.ma-zala-nafy',C,a,b)
for q in ['01#4:a','04#6:a','05#4:abd','05#6:c','06#3:a','06#4:a','06#6:d','quiz#5:ac']:
    a,b=q.split(':'); AC('arabe.nawasikh.muqaraba-shuru3-raja2-khalt',C,a,b)
for q in ['01#2:b','01#3:b','02#2:acd','02#5:b','04#4:b','05#3:b','05#5:abc','06#1:d','quiz#3:b']:
    a,b=q.split(':'); AC('arabe.nawasikh.sayrura-daymuma-khalt',C,a,b)
for q in ['01#6:ad','02#3:a','04#3:acd','05#6:b','06#2:b','quiz#4:a']:
    a,b=q.split(':'); AC('arabe.nawasikh.kana-qad-wal-mudari3-khalt',C,a,b)
for q in ['quiz#2:abc','01#5:cd','04#1:bcd','05#2:b','02#3:d','quiz#4:d']:
    a,b=q.split(':'); AC('arabe.nawasikh.sighat-kana-khalt',C,a,b)
for q in ['01#1:abd','01#2:cd','01#3:c','01#4:cd','02#5:c','02#6:cd','04#4:c','05#2:c','05#3:c','06#1:a','06#3:d','06#5:bd','06#6:ab','quiz#3:cd','quiz#5:d']:
    a,b=q.split(':'); AC('arabe.nawasikh.dalalat-al-nasikh-khalt',C,a,b)
AC('arabe.jumla.isnad-far3i-la-yura',C,'04#2','ab')
AC('arabe.jumla.markaba-li-tul',C,'04#2','d')
def M(i,ch,specs):
    for s in specs.split():
        a,b=s.split(':'); AC(i,ch,a,b)
# ============================ CH 03 — المنصوبات (الزمان) ============================
NEWC['arabe.zaman.wazifa-min-al-ma3na']=(
 "تحكمُ على وظيفةِ المركّبِ الدّالِّ على الزّمانِ من معناه أو موضعِه: اسألْ بمَ يتعلّقُ: بفعلٍ ← مفعولٌ فيه، يُتمُّ مبتدأً بلا فعلٍ ← خبرٌ، يصفُ الهيأةَ ← حالٌ",
 "Tu fixes la fonction du groupe de temps par son sens ou sa place : rattaché à un verbe → مفعول فيه ; complète un مبتدأ sans verbe → خبر ; décrit l'état → حال",
 "You set a time phrase's function by its meaning or place: tied to a verb → مفعول فيه; completes a مبتدأ with no verb → خبر; describes a state → حال")
NEWC['arabe.zaman.mafoul-fihi-bila-sigha']=(
 "تعيّنُ زمانَ الحدثِ بالمفعولِ فيه وحدَه وتُهملُ صيغةَ الفعلِ (ننتظرُ منذُ ساعةٍ: انتهى): الصّيغةُ تقولُ الانقضاءَ أو عدمَه، والمفعولُ فيه يقولُ متى",
 "Tu dates le fait par le seul مفعول فيه en oubliant la forme du verbe (ننتظرُ منذُ ساعةٍ : fini) : la forme dit achevé ou non, le مفعول فيه dit quand",
 "You date the event from the مفعول فيه alone, ignoring the verb form (ننتظرُ منذُ ساعةٍ: over): the form says finished or not, the مفعول فيه says when")
NEWC['arabe.zaman.tartib-bi-tartib-al-kalam']=(
 "ترتّبُ الأحداثَ بترتيبِ ذكرِها في الكلامِ: التّرتيبُ في الزّمنِ تعيّنُه الأداةُ (قبلَ، بعدَ) والحالُ «وكانَ قد فعل» الّتي تسبقُ فعلَها وإن ذُكرتْ بعدَه",
 "Tu ordonnes les faits dans l'ordre où ils sont dits : l'ordre réel vient de l'outil (قبلَ، بعدَ) et de la حال « وكانَ قد فعل », antérieure même dite après",
 "You order events as they are mentioned: the real order comes from the tool (قبلَ، بعدَ) and from the حال « وكانَ قد فعل », earlier even when said later")
NEWC['arabe.zaman.adat-tazamun-asbaqiyya-khalt']=(
 "تخلطُ بين أدواتِ الزّمنِ: «قبلَ (أن، ما)» أسبقيّةُ الحدثِ الرّئيسيِّ، «بعدَ (أن، ما)» لاحقيّتُه، «عندما، حينَ، بينما، لمّا + ماضٍ» تزامنُ الحدثَينِ",
 "Tu confonds les outils de temps : قبلَ (أن، ما) = le principal avant, بعدَ (أن، ما) = après, عندما، حينَ، بينما، لمّا + passé = en même temps",
 "You mix up the time tools: قبلَ (أن، ما) = main event before, بعدَ (أن، ما) = after, عندما، حينَ، بينما، لمّا + past = at the same time")
NEWC['arabe.zaman.adat-zaman-3illiyya']=(
 "تقرأُ بين الحدثَينِ علاقةَ سببٍ ونتيجةٍ: أدواتُ الزّمنِ (قبلَ، بعدَ، حينَ) تقولُ ترتيبَ الوقوعِ أو التّزامنَ، والعلّيّةُ لـ«لأنّ» لا لها",
 "Tu lis une cause entre les deux faits : les outils de temps (قبلَ، بعدَ، حينَ) disent l'ordre ou la simultanéité ; la cause relève de لأنّ",
 "You read cause and effect between the two events: time tools (قبلَ، بعدَ، حينَ) give order or simultaneity; cause belongs to لأنّ")
NEWC['arabe.zaman.hal-waw-la-tuhaddid']=(
 "تحكمُ على قيمةِ الحالِ بالواوِ (واوٌ واحدةٌ فقيمةٌ واحدةٌ): يعيّنُها ما بعدَها: مضارعٌ ← حالةٌ غيرُ منقضيةٍ مزامنةٌ، «قد» + ماضٍ ← حالةٌ انقضتْ قبيلَ الفعلِ",
 "Tu juges la valeur de la حال par le و (même و, même valeur) : ce qui suit décide — مضارع : simultanée, non achevée ; قد + passé : achevée juste avant",
 "You judge the حال's value by its و (same و, same value): what follows decides — مضارع: simultaneous, unfinished; قد + past: finished just before")
NEWC['arabe.zaman.qad-madi-ihtimal']=(
 "تقرأُ «قد» مع الماضي احتمالًا (وقد انتهتْ: ربّما انتهتْ): «قد» + ماضٍ علامةُ انقضاءٍ، والاحتمالُ لـ«قد» + مضارعٍ",
 "Tu lis قد + passé comme une probabilité (وقد انتهتْ : peut-être) : قد + passé marque l'achèvement ; la probabilité, c'est قد + مضارع",
 "You read قد + past as a probability (وقد انتهتْ: maybe): قد + past marks completion; probability is قد + مضارع")
NEWC['arabe.zaman.qimat-al-hal-khalt']=(
 "تخطئُ في قيمةِ الحالِ: اقرأْ صيغتَها هي لا صيغةَ الفعلِ الرّئيسيِّ (مضارعٌ ← غيرُ منقضيةٍ، «قد» + ماضٍ ← انقضتْ قبيلَه)، ثمّ صيغةَ الفعلِ الرّئيسيِّ",
 "Tu te trompes de valeur de la حال : lis SA forme, pas celle du verbe principal (مضارع → non achevée ; قد + passé → achevée juste avant), puis celle du verbe",
 "You misread the حال's value: read its OWN form, not the main verb's (مضارع → unfinished; قد + past → finished just before), then the main verb's form")
PGC['03']={1:['arabe.zaman.wazifa-min-al-ma3na'],2:['arabe.zaman.mafoul-fihi-bila-sigha'],3:['arabe.jumla.ra2isi-bi-tartib-al-dhikr'],
 4:['arabe.zaman.tartib-bi-tartib-al-kalam'],5:['arabe.zaman.qimat-al-hal-khalt'],6:['arabe.zaman.hal-waw-la-tuhaddid'],7:['arabe.zaman.tartib-bi-tartib-al-kalam']}
C='03'
M('arabe.zaman.wazifa-min-al-ma3na',C,'02#6:acd 04#6:abc 04#2:d 05#4:d quiz#2:acd 06#1:a 06#5:bcd 06#4:d quiz#5:d')
M('arabe.zaman.mafoul-fihi-bila-sigha',C,'02#3:a 01#2:b')
M('arabe.zaman.zaman-min-al-sigha',C,'01#2:a 02#3:d')
M('arabe.jumla.ra2isi-bi-tartib-al-dhikr',C,'02#1:a 06#3:a 04#3:d')
M('arabe.zaman.tartib-bi-tartib-al-kalam',C,'01#4:a 02#2:b 06#2:b')
M('arabe.zaman.adat-tazamun-asbaqiyya-khalt',C,'01#3:bc 01#4:b 02#5:ab 04#2:a 04#3:a 05#3:ab 05#4:c 05#5:acd 06#2:c 06#6:ab quiz#3:bcd')
M('arabe.zaman.adat-zaman-3illiyya',C,'01#3:d 01#4:c 02#2:d 05#3:c')
M('arabe.zaman.hal-waw-la-tuhaddid',C,'02#4:a 04#4:b 05#2:c 05#6:bd 04#5:ab 05#4:b')
M('arabe.zaman.qad-madi-ihtimal',C,'02#4:c 04#4:c 05#6:a')
M('arabe.zaman.qimat-al-hal-khalt',C,'04#4:d 01#5:abd 01#6:bcd 06#4:ab quiz#4:abc quiz#5:ac 02#4:d 05#2:bd 04#5:d 04#2:b')
# ============================ CH 19 — العدد والمعدود ============================
NEWC['arabe.adad.naw3-bil-shakl']=(
 "تحكمُ على نوعِ العددِ بجذرِه أو بوزنِه لا بمعناه: الأصليُّ يقولُ الكمَّ (كم؟)، والرّتبيُّ يقولُ الرّتبةَ ولو لم يكنْ على فاعِل (الأولى، العشرونَ)",
 "Tu juges le type du nombre par sa racine ou sa forme, pas son sens : le أصليّ dit combien, le رتبيّ dit le rang, même hors de فاعِل (الأولى، العشرون)",
 "You judge a number's type by its root or form, not its meaning: the أصليّ says how many, the رتبيّ the rank, even when not on فاعِل (الأولى، العشرون)")
NEWC['arabe.adad.siyaghat-al-rutbi-khalt']=(
 "تخطئُ في صوغِ الرّتبيِّ: من 2 إلى 10 على فاعِل (السّابعُ)، وفي المركّبِ الجزءُ الأوّلُ وحدَه (الخامسَ عشرَ)، والعقودُ بلفظِها؛ لا «ال» وحدَها ولا ياءُ نسبةٍ",
 "Tu formes mal le رتبيّ : 2 à 10 sur فاعِل (السّابع) ; dans 11–19, le 1er terme seul (الخامس عشر) ; les dizaines gardent leur forme ; ni « ال » seul ni ـيّ",
 "You form the رتبيّ wrongly: 2–10 on فاعِل (السّابع); in 11–19 only the first part changes (الخامس عشر); tens keep their form; not just « ال », not ـيّ")
NEWC['arabe.adad.3aksiyya-3-10']=(
 "تطابقُ العددَ من 3 إلى 10 معدودَه مطابقةً مباشرةً (ثلاثةُ مجلّاتٍ) قياسًا على «مجلّةٌ واحدةٌ»: المطابقةُ هنا عكسيّةٌ: ثلاثُ مجلّاتٍ، ثلاثةُ كتبٍ",
 "Tu accordes directement le nombre de 3 à 10 (ثلاثةُ مجلّاتٍ), comme مجلّةٌ واحدةٌ : ici l'accord est inverse : ثلاثُ مجلّاتٍ، ثلاثةُ كتبٍ",
 "You make 3–10 agree directly with the noun (ثلاثةُ مجلّاتٍ), as with مجلّةٌ واحدةٌ: here agreement is reversed: ثلاثُ مجلّاتٍ، ثلاثةُ كتبٍ")
NEWC['arabe.adad.juz2an-hukm-wahid']=(
 "تطبّقُ حكمًا واحدًا على جزأيِ العددِ من 13 إلى 19 (أربعةَ عشرةَ، أربعَ عشرَ لاعبًا): الأوّلُ يطابقُ عكسيًّا والثّاني مباشرةً، و11 و12 مباشرةٌ في الجزأينِ",
 "Tu appliques une seule règle aux deux termes de 13–19 (أربعةَ عشرةَ ou أربعَ عشرَ لاعبًا) : le 1er s'accorde à l'inverse, le 2e directement ; 11 et 12 : direct",
 "You apply one rule to both parts of 13–19 (أربعةَ عشرةَ or أربعَ عشرَ لاعبًا): the first agrees inversely, the second directly; 11 and 12: both direct")
NEWC['arabe.adad.thabat-al-3aqd-ta3mim']=(
 "تعمّمُ ثباتَ العقدِ على غيرِه (خمسةٌ وعشرونَ طالبةً، ثلاثةَ عشرَ لا يتغيّرُ): العقدُ وحدَه لازمُ الصّيغةِ، والآحادُ وأجزاءُ المركّبِ تطابقُ بحسبِ قاعدتِها",
 "Tu étends la forme fixe de la dizaine au reste (خمسةٌ وعشرونَ طالبةً) : seule la dizaine est fixe ; unités et termes de 13–19 s'accordent selon leur règle",
 "You extend the fixed form of the tens to the rest (خمسةٌ وعشرونَ طالبةً): only the tens are fixed; units and the parts of 13–19 follow their own rule")
NEWC['arabe.adad.murakkab-mazji-i3rab']=(
 "تُعربُ المركّبَ من 11 إلى 19 (ورتبيَّه) بحسبِ موضعِه (أحدُ، الخامسةِ عشرةَ): هو مبنيٌّ على فتحِ الجزأينِ «في محلِّ…»، إلّا «اثنا/اثنتا» فكالمثنّى بلا نونٍ",
 "Tu déclines le composé 11–19 (ordinal compris) selon sa place : il est مبنيّ sur fatha des deux termes, « في محلّ » ; seul اثنا/اثنتا se décline en duel sans ن",
 "You decline the compound 11–19 (ordinals too) by position: it is مبنيّ on fatha in both parts, « في محلّ »; only اثنا/اثنتا declines as a dual, without ن")
NEWC['arabe.adad.hukm-al-ma3dud-khalt']=(
 "تعطي المعدودَ حكمَ مجالٍ آخرَ: بعدَ 3–10 جمعٌ مجرورٌ (ثلاثةُ أقلامٍ)، وبعدَ 11–99 مفردٌ منصوبٌ (ستّةَ عشرَ كتابًا)، وبعدَ المئاتِ والآلافِ مفردٌ مجرورٌ",
 "Tu donnes au معدود la règle d'un autre cas : 3–10 → pluriel مجرور (ثلاثةُ أقلامٍ) ; 11–99 → singulier منصوب (ستّةَ عشرَ كتابًا) ; 100, 1000 → singulier مجرور",
 "You give the counted noun another range's rule: 3–10 → plural مجرور (ثلاثةُ أقلامٍ); 11–99 → singular منصوب (ستّةَ عشرَ كتابًا); 100, 1000 → singular مجرور")
NEWC['arabe.adad.wazifat-al-3adad-wal-ma3dud']=(
 "تخطئُ في العلاقةِ بين العددِ والمعدودِ: 1 و2 نعتانِ، والمعدودُ مضافٌ إليه بعدَ 3–10 والمئاتِ والآلافِ، وتمييزٌ بعدَ 11–99؛ والعددُ نفسُه لا يكونُ تمييزًا",
 "Tu te trompes de relation nombre/معدود : 1 et 2 sont نعت ; le معدود est مضاف إليه après 3–10, 100, 1000, تمييز après 11–99 ; le nombre lui-même n'est pas تمييز",
 "You get the number/noun relation wrong: 1 and 2 are نعت; the noun is مضاف إليه after 3–10, 100, 1000, and تمييز after 11–99; the number itself is never تمييز")
PGC['19']={1:['arabe.adad.naw3-bil-shakl'],2:['arabe.adad.siyaghat-al-rutbi-khalt'],3:['arabe.tamyiz.idafi-tamyizi'],4:['arabe.adad.3aksiyya-3-10'],
 5:['arabe.adad.juz2an-hukm-wahid'],6:['arabe.adad.thabat-al-3aqd-ta3mim'],7:['arabe.adad.murakkab-mazji-i3rab'],8:['arabe.adad.hukm-al-ma3dud-khalt'],
 9:['arabe.adad.murakkab-mazji-i3rab','arabe.adad.hukm-al-ma3dud-khalt'],10:['arabe.i3rab.harf-hala-ukhra','arabe.adad.hukm-al-ma3dud-khalt'],11:['arabe.adad.hukm-al-ma3dud-khalt']}
C='19'
M('arabe.adad.naw3-bil-shakl',C,'quiz#1:acd 01#1:ab 03#1:acd 04#1:abc')
M('arabe.adad.siyaghat-al-rutbi-khalt',C,'01#2:bcd 02#5:bd 03#6:b quiz#2:abd')
M('arabe.tamyiz.idafi-tamyizi',C,'04#2:bcd')
M('arabe.adad.3aksiyya-3-10',C,'quiz#3:bcd 03#2:a')
M('arabe.adad.juz2an-hukm-wahid',C,'02#1:bcd 05#3:ab 04#4:a 04#5:c 04#6:b')
M('arabe.adad.thabat-al-3aqd-ta3mim',C,'02#2:a 04#3:a 05#3:c')
M('arabe.adad.murakkab-mazji-i3rab',C,'03#5:ac 02#3:a quiz#4:abc 04#4:c 02#4:abd 04#5:bd 04#6:a')
M('arabe.adad.hukm-al-ma3dud-khalt',C,'01#5:bcd 03#3:bc 03#4:abc 04#3:d 04#4:d 02#2:b 04#6:c')
M('arabe.adad.wazifat-al-3adad-wal-ma3dud',C,'05#2:bcd quiz#5:acd 02#3:c 05#5:d')
M('arabe.i3rab.harf-hala-ukhra',C,'01#6:d 02#2:c 04#3:b 03#6:a')
M('arabe.i3rab.haraka-bada-harf',C,'02#6:a 05#5:b')
