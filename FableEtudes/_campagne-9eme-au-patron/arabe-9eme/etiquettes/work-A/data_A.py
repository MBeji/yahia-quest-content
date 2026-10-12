# -*- coding: utf-8 -*-
# Source de données unique des deux livrables (partie A). Exécuté par build_A.py.
# Structure :
#   PIEGES[ch][k]      = (section, citation courte)       k = rang du k-ième bloc `::: piege` du cours.md
#   NOID_REASON[(ch,k)] = raison (piège sans id)
#   IDS[id]            = {new, ar, fr, en, uses:[{ch, pg:[k..], carriers:[(fichier, q, option, note)]}], note}
#   PRECEDENCE, UNDER3, DOUBTS, STATUS

STATUS = "EN COURS — chapitres traités : 15, 04, 16, 17, 18"

PIEGES = {}
NOID_REASON = {}
IDS = {}
PRECEDENCE = []
UNDER3 = []
DOUBTS = []


def NEW(i, ar, fr, en, uses, note=''):
    assert i not in IDS, i
    IDS[i] = dict(new=True, ar=ar, fr=fr, en=en, uses=uses, note=note)


def REUSE(i, why, uses, note=''):
    assert i not in IDS, i
    IDS[i] = dict(new=False, why_reused=why, uses=uses, note=note)


def U(ch, pg, *carriers, half=''):
    return dict(ch=ch, pg=list(pg), carriers=list(carriers), half=half)


# =====================================================================================
# CHAPITRE 15 — العلاقات بين الجمل (16 pièges)
# =====================================================================================
PIEGES['15'] = {
    1: ('§ الجملة في النص', 'الأطفالُ يلعبونَ في السّاحةِ: «فعليّةٌ، لأنّ فيها فعلًا» + عدّ الجملة الطويلة مركّبةً'),
    2: ('§ رتبة الجملة', 'الحكمُ على الرّتبةِ بشكلِ الجملةِ: «ذلكَ الشّيخُ كريمٌ» ابتدائيّةٌ'),
    3: ('§ رتبة الجملة', 'عدُّ كلِّ مقطعٍ بينَ فاصلتَينِ جملةً اعتراضيّةً (وقد فازَ = حالٌ)'),
    4: ('§ حرف الاستئناف وحرف العطف', 'تسميةُ الواوِ أو الفاءِ أو «ثمّ» حرفَ عطفٍ دائمًا'),
    5: ('§ حروف الجمع', 'قراءةُ الواوِ ترتيبًا لأنّ الأحداثَ تتتابعُ + كلُّ فاءٍ ترتيبُ أحداثٍ'),
    6: ('§ حروف الجمع', 'اختيارُ «ثمّ» لذكرِ النّتيجةِ + عدُّ كلِّ «حتّى» حرفَ جمعٍ'),
    7: ('§ أو وإمّا وأم', 'حملُ «أو» على التّخييرِ دائمًا'),
    8: ('§ أو وإمّا وأم', 'الجوابُ بـ«نعم» أو «لا» عن سؤالٍ فيه «أم»'),
    9: ('§ بل ولكن', 'قراءةُ «بل» إضرابًا دائمًا'),
    10: ('§ بل ولكن', 'استعمالُ أداةِ الاستدراكِ حينَ تكونُ الثّانيةُ هي المتوقَّعَ'),
    11: ('§ أمّا وإذا وإذن وأي', 'حذفُ الفاءِ بعدَ المبتدأِ في «أمّا» + الخلطُ بينَ «إمّا» و«أمّا»'),
    12: ('§ أمّا وإذا وإذن وأي', 'عدُّ كلِّ «إذا» فجئيّةً'),
    13: ('§ أمّا وإذا وإذن وأي', 'عدُّ كلِّ «أيْ» تفسيرًا'),
    14: ('§ الحذف والجملة المختزلة', 'إتمامُ «الصّدقَ الصّدقَ!» بتغييرِ ما نطقَه المتكلّمُ'),
    15: ('§ الحذف في الفعليّة والاسميّة', 'تسميةُ المنجَزِ («البابَ: المفعولُ به») بدلَ المحذوفِ'),
    16: ('§ الحذف في الفعليّة والاسميّة', 'افتراضُ أنّ الباقيَ في الجوابِ هو الخبرُ دائمًا'),
}

NOID_REASON[('15', 8)] = "isolé : aucun distracteur ne met un « نعم / لا » en réponse à une question en « أم » (les 35 items sont des QCM sur le sens ; seul le `verifie` du cours le teste)."
NOID_REASON[('15', 12)] = "isolé : aucun distracteur ne prend un « إذا » conditionnel pour une فجئيّة (le seul item sur « فإذا », 03#4, ne porte pas ce sens ; l'erreur inverse y est testée)."
NOID_REASON[('15', 14)] = "isolé : aucun item ne demande de compléter « الصّدقَ الصّدقَ » ; l'erreur n'existe que dans le cours."
NOID_REASON[('15', 15)] = "isolé : les items demandent « ما المحذوف ؟ » avec des options de la forme « الفعل والفاعل… », jamais « المفعول به » comme réponse-à-la-place-du-manquant ; erreur de forme d'exercice que le QCM ne peut pas reconstruire."

# ---- sentence type / degree (domaine jumla) ----------------------------------------
NEW('arabe.jumla.naw3-bi-fi3l',
    'تحكمُ بأنّ الجملةَ فعليّةٌ لأنّ فيها فعلًا أو لأنّها تبدأُ بـ«كانَ»: النّوعُ يُقرأُ من أوّلِ مكوّنٍ، والنّاسخُ يُبقيها اسميّةً',
    "Tu dis « verbale » parce qu'il y a un verbe ou qu'elle commence par كان : le type se lit au 1er composant, et un ناسخ la laisse nominale",
    "You call it verbal because it holds a verb or starts with كان: the type comes from the first component, and a ناسخ keeps it nominal",
    [U('15', [1], ('04', 3, 'a', "R1 : « تبدأ بالفعل كانت » — le ناسخ pris pour un verbe"), half="1re moitié : « فعليّة لأنّ فيها فعلًا »")])

NEW('arabe.jumla.markaba-li-tul',
    'تعدُّ الجملةَ مركّبةً لأنّها طويلةٌ أو فيها جارٌّ ومجرورٌ ونعتٌ: المركّبةُ ما شغلَ أحدَ مكوّناتِها إسنادٌ فرعيٌّ (فعلٌ وفاعلُه)',
    "Tu juges une phrase composée parce qu'elle est longue ou a un complément prépositionnel : elle l'est si un composant est un إسناد فرعيّ (verbe + sujet)",
    "You call a sentence compound because it is long or has a prepositional phrase: it is compound only if a component is itself a clause (إسناد فرعيّ)",
    [U('15', [1], ('01', 1, 'b', "R1 : l'explication dit « متمّمان لا إسناد فيهما »"), half="2e moitié : « طويلة ⇒ مركّبة »")])

NEW('arabe.jumla.isnad-far3i-la-yura',
    'تعدُّ الجملةَ بسيطةً لأنّك ترى فعلًا واحدًا: الخبرُ أو الحالُ أو المفعولُ به إذا كان جملةً (يلعبونَ في الحديقةِ) إسنادٌ فرعيٌّ يجعلُها مركّبةً',
    "Tu juges une phrase simple parce que tu ne vois qu'un verbe : un خبر, un حال ou un complément qui est une phrase (يلعبون في الحديقة) la rend composée",
    "You call a sentence simple because you see one verb: a خبر, حال or object that is itself a clause (يلعبون في الحديقة) makes it compound",
    [U('15', [], ('05', 1, 'a', "R2 : مفعول به = جملة « إنّ التمرين سيبدأ غدًا »"),
                 ('05', 1, 'b', "R2 : خبر = جملة « يلعبون في الحديقة »"),
                 ('05', 1, 'd', "R2 : حال = جملة « يقرأ في المكتبة »"),
                 ('04', 3, 'b', "R1 : « خبرها تسير ببطء فعل وليس فيها إسناد ثانٍ »"))])

# ---- rang de la phrase dans le texte (domaine rabt) ---------------------------------
NEW('arabe.rabt.rutba-bi-shakl-la-bil-unsur',
    'تحكمُ على رتبةِ الجملةِ بشكلِها (اسميّة/فعليّة) أو موضعِها، لا بما يردُّها إلى ما قبلَها: حرفِ استئنافٍ أو ضميرِ غيبةٍ أو اسمِ إشارةٍ',
    "Tu juges le rang d'une phrase (ابتدائيّة/استئنافيّة) par sa forme ou sa place, pas par ce qui la relie à la précédente : حرف استئناف, ضمير غيبة, اسم إشارة",
    "You judge a sentence's rank by its form or place, not by what links it to the previous one: a حرف استئناف, a third-person pronoun or a demonstrative",
    [U('15', [2], ('quiz', 1, 'a', "R1 : نوع (اسمية) لا رتبة"),
                  ('quiz', 1, 'c', "R1 : موضعها من النص"),
                  ('01', 2, 'a', "R1 : « لأنّها جملة اسمية »"),
                  ('01', 2, 'c', "اسم الإشارة « تلك » غير مرئيّ"),
                  ('01', 2, 'd', "R1 : « لأنّها الجملة الثانية »"),
                  ('04', 1, 'b', "R2 : تحتوي « ثمّ »"),
                  ('04', 1, 'c', "R2 : تحتوي « هذا »"),
                  ('04', 1, 'd', "R2 : تحتوي « هو »"))])

NEW('arabe.rabt.i3tirad-wal-hal-khalt',
    'تعدُّ كلَّ مقطعٍ بينَ فاصلتَينِ أو مبدوءٍ بواوٍ جملةً اعتراضيّةً: الحالُ والمفعولُ فيه لهما وظيفةٌ، والاعتراضيّةُ وحدَها بلا وظيفةٍ',
    "Tu prends tout segment entre deux virgules (ou en و) pour une اعتراضيّة : un حال ou un مفعول فيه a une fonction, seule l'اعتراضيّة n'en a pas",
    "You take any segment between two commas (or starting with و) for an اعتراضيّة: a حال or مفعول فيه has a function; only the اعتراضيّة has none",
    [U('15', [3], ('quiz', 2, 'a', "R1 : « كلُّ مقطعٍ يقعُ بينَ فاصلتَينِ »"),
                  ('quiz', 2, 'b', "تعريف الحال (« تصفُ هيئةَ الفاعلِ »)"),
                  ('02', 1, 'a', "R2 : « وهو يبتسمُ » حال"),
                  ('02', 1, 'b', "R2 : « حينَ دقَّ الجرسُ » مفعول فيه"),
                  ('02', 1, 'd', "R2 : « وقد أنهَوا الامتحانَ » حال"),
                  ('05', 3, 'b', "R1 : « لأنّها بدأتْ بالواوِ »"))])

# ---- nom de la particule ---------------------------------------------------------------
NEW('arabe.rabt.ism-al-harf-min-shaklih',
    'تسمّي أداةَ الرّبطِ (و، ف، ثمّ، أم) حرفَ عطفٍ من شكلِها أو معناها لا ممّا تربطُه: جملتانِ مستقلّتانِ ← استئنافٌ، وعنصرانِ بوظيفةٍ ← عطفٌ',
    "Tu nommes la particule (و ف ثمّ أم) selon sa forme ou son sens, pas selon ce qu'elle relie : 2 phrases ← استئناف ; 2 éléments de même fonction ← عطف",
    "You name a particle (و، ف، ثمّ، أم) by its shape or meaning, not by what it links: two independent sentences ← استئناف; two same-function items ← عطف",
    [U('15', [4], ('05', 2, 'a', "R1 : « تربط بين فعلين متتابعين » ≠ عنصرين بوظيفة واحدة"),
                  ('05', 2, 'c', "R1 : nom tiré du sens « جمع بدون ترتيب »"),
                  ('01', 3, 'b', "R1 : « حرف استئناف لأنّه يفيد الجمع… »"),
                  ('02', 5, 'd', "nom « عطف » pour أم (sens juste)"))],
    note="Dans une question « nom + raison » (01#3, 05#2, 02#5), l'id du NOM prime quand la raison donnée est vraie mais ne peut pas fonder le nom ; voir §3.")

# ---- sens des particules de jonction ----------------------------------------------------
NEW('arabe.rabt.waw-tartib',
    'تجعلُ الواوَ للتّرتيبِ لأنّ الأحداثَ تتتابعُ: الواوُ جمعٌ بلا ترتيبٍ ولا تراخٍ، والتّرتيبُ من معنى الفعلَينِ لا من الحرفِ',
    "Tu fais de و un marqueur d'ordre parce que les faits se suivent : و réunit sans ordre ni délai ; l'ordre vient du sens des verbes, pas de la particule",
    "You treat و as marking order because the events follow each other: و joins without order or delay; the order comes from the verbs, not the particle",
    [U('15', [5], ('quiz', 3, 'b', "R1 : الواو « مع الترتيب »"),
                  ('quiz', 3, 'c', "الواو « مع الترتيب والتراخي » (= ثمّ)"),
                  ('05', 2, 'b', "R1 : « تفيد الترتيب بين الحدثين » ; l'explication : « الواو لا ترتّب أصلًا »"),
                  ('01', 3, 'd', "R1 : الواو « الترتيب والتراخي » (nom juste, sens faux)"), half="1re moitié : « الواو ترتيب لأنّ الأحداث تتتابع »")])

NEW('arabe.rabt.fa-wajh-wahid',
    'تقرأُ كلَّ فاءٍ ترتيبَ أحداثٍ أو سببًا ونتيجةً: للفاءِ ثلاثةُ وجوهٍ، منها تفصيلُ ما أُجمِلَ (اختلفوا، فمنهم من… ومنهم من…)',
    "Tu lis chaque ف comme un ordre d'événements ou une cause : ف a trois emplois, dont le détail d'un ensemble global (اختلفوا، فمنهم… ومنهم…)",
    "You read every ف as event order or cause: ف has three uses, including detailing something stated globally (اختلفوا، فمنهم… ومنهم…)",
    [U('15', [5], ('01', 5, 'b', "R1 : « ليس حدثًا لاحقًا »"),
                  ('01', 5, 'c', "R1 : « ولا نتيجةً له »"), half="2e moitié : « كلّ فاء ترتيب أحداث »")])

NEW('arabe.rabt.natija-bi-ghayr-al-fa',
    'تعبّرُ عن النّتيجةِ بـ«ثمّ» أو الواوِ أو «أي»: السّببُ والنّتيجةُ للفاءِ؛ «ثمّ» تقولُ مهلةً، والواوُ جمعًا بلا ترتيبٍ، و«أي» شرحًا',
    "Tu exprimes la conséquence avec ثمّ, و ou أي : cause et conséquence relèvent de ف ; ثمّ dit un délai, و une simple réunion, أي une explication",
    "You express a result with ثمّ, و or أي: cause and effect belong to ف; ثمّ marks a delay, و plain joining, أي an explanation",
    [U('15', [6], ('05', 4, 'a', "R2 : « ثمّ عادَ إلى بيتِه »"),
                  ('05', 4, 'c', "R2 : الواو"),
                  ('05', 4, 'd', "R2 : « أي »"),
                  ('02', 2, 'c', "R1 : « السّبب والنّتيجة » attribué à ثمّ"), half="1re moitié : « ثمّ لذكر النتيجة »")])

NEW('arabe.rabt.hatta-jam3-daiman',
    'تعدُّ كلَّ «حتّى» حرفَ جمعٍ: التي تصحُّ بـ«إلى أنْ» (سهرَ حتّى طلعَ الفجرُ) تحدّدُ النّهايةَ، وجمعُ المستبعَدِ جملةٌ تامّةٌ لا تصحُّ بها «إلى أنْ»',
    "Tu prends chaque حتّى pour une réunion : si إلى أنْ convient (سهر حتّى طلع الفجر), elle marque le terme ; réunir l'improbable exige une phrase complète",
    "You take every حتّى as joining: if إلى أنْ fits (سهر حتّى طلع الفجر) it marks an endpoint; joining the improbable takes a full sentence",
    [U('15', [6], ('02', 3, 'a', "R2 : « حتّى الفجرِ » (اسم مفرد = غاية)"),
                  ('02', 3, 'c', "R2 : « حتّى أتقنَ الخطّةَ »"),
                  ('02', 3, 'd', "R2 : « حتّى بلغْنا القمّةَ »"), half="2e moitié : « كلّ حتّى حرف جمع »")])

NEW('arabe.rabt.fa-thumma-bila-tartib',
    'تقرأُ الفاءَ أو «ثمّ» جمعًا بلا ترتيبٍ كالواوِ: تبديلُ الجملتَينِ معهما يقلبُ المعنى، لأنّ ما بعدَهما يأتي بعدَ ما قبلَهما',
    "Tu lis ف ou ثمّ comme و, une réunion sans ordre : avec elles, inverser les deux phrases change le sens, car la seconde vient après la première",
    "You read ف or ثمّ like و, joining with no order: swapping the two sentences changes the meaning, since the second comes after the first",
    [U('15', [], ('01', 4, 'a', "R2 : فاء السببية — l'élève croit l'inversion sans effet"),
                 ('01', 4, 'b', "R2 : ثمّ — idem"),
                 ('01', 4, 'c', "R2 : فاء الترتيب — idem"),
                 ('01', 5, 'd', "فاء التفصيل prise pour « جمع بدون أيّ ترتيب »"),
                 ('02', 2, 'b', "« ترتيب الحدثين » censé se perdre en passant de ثمّ à ف"))])

# ---- أو / إمّا / أم ------------------------------------------------------------------------
NEW('arabe.rabt.aw-takhyir-daiman',
    'تحملُ «أو» على التّخييرِ دائمًا: في الإخبارِ هي للشّكِّ (كُسرتْ ساقُه، أو التوتْ قدمُه)، والتّخييرُ يكونُ في الطّلبِ فقط',
    "Tu prends toujours « أو » pour un choix laissé à l'autre : dans une affirmation elle dit le doute (كُسرت ساقه أو التوت قدمه) ; le choix vient avec la demande",
    "You always read « أو » as offering a choice: in a statement it expresses doubt (كُسرت ساقه أو التوت قدمه); choice belongs to requests",
    [U('15', [7], ('03', 1, 'a', "R1 : « التّخييرُ يكونُ في الطّلبِ »"))])

# ---- بل / الاستدراك ------------------------------------------------------------------------
NEW('arabe.rabt.bal-bila-nazar-fil-ula',
    'تحدّدُ معنى «بل» دونَ أن تنظرَ في الجملةِ الأولى: إضرابٌ إن تراجعَ عنها المتكلّمُ، تقريرٌ إن كانت منفيّةً وبقيتْ، تأكيدٌ إن بقيتْ والثّانيةُ أقوى',
    "Tu fixes le sens de بل sans regarder la 1re phrase : إضراب si l'on s'en dédit ; تقرير si elle est négative et reste vraie ; تأكيد si elle reste vraie, renforcée",
    "You fix the meaning of بل without checking the first sentence: إضراب if it is retracted; تقرير if it is negative and stands; تأكيد if it stands, strengthened",
    [U('15', [9], ('quiz', 4, 'a', "R1 : إضراب alors que « لم يتأخّر » reste vrai"),
                  ('quiz', 4, 'b', "تأكيد alors que la 1re est négative"),
                  ('02', 4, 'b', "إضراب (« بل رأيتُ أخاه ») lu comme تقرير"),
                  ('02', 4, 'c', "تأكيد lu comme تقرير"),
                  ('02', 4, 'd', "إضراب (« أخذَ الكعكَ ») lu comme تقرير"))])

NEW('arabe.rabt.istidrak-bi-ma-yuwafiq',
    'تستدركُ بـ«لكنْ» وأخواتِها بما هو متوقَّعٌ (اجتهدَ، لكنّه نجحَ): الاستدراكُ يأتي بخلافِ المتوقَّعِ، وإلّا فالرّبطُ بالفاءِ',
    "Tu emploies لكنّ et ses sœurs pour dire ce qu'on attend (اجتهد لكنّه نجح) : l'استدراك apporte le contraire de l'attendu, sinon on relie par ف",
    "You use لكنّ and its sisters for what is expected (اجتهد لكنّه نجح): the استدراك brings the opposite of what is expected; otherwise link with ف",
    [U('15', [10], ('05', 5, 'a', "R2 : « تدرّبَ… لكنّه تحسّنَ »"),
                   ('05', 5, 'b', "R2 : « انكسرَ… بيدَ أنّه تناثرَ »"),
                   ('05', 5, 'd', "R2 : « أعدَّ… غيرَ أنّه سلّمَه في موعدِه »"))])

# ---- أمّا / إمّا / أي -----------------------------------------------------------------------
NEW('arabe.rabt.amma-bila-fa',
    'تحذفُ الفاءَ بعدَ المبتدأِ في «أمّا» (أمّا كريمٌ نجحَ): الفاءُ من قالبِ التّفصيلِ: أمّا + مبتدأٌ + فـ + خبرٌ',
    "Tu supprimes la ف après le مبتدأ dans « أمّا » (أمّا كريم نجح) : elle fait partie du moule du détail : أمّا + مبتدأ + ف + خبر",
    "You drop the ف after the مبتدأ in « أمّا » (أمّا كريم نجح): it is part of the pattern: أمّا + مبتدأ + ف + خبر",
    [U('15', [11], ('04', 4, 'c', "R1 : « حذفُ الفاءِ يُسقطُ جزءًا من القالبِ »"), half="1re moitié : « حذف الفاء بعد المبتدأ »")])

NEW('arabe.rabt.imma-amma-khalt',
    'تخلطُ بينَ «إمّا» و«أمّا»: «إمّا» اختيارٌ بينَ أمرَينِ لا يجتمعانِ وتتكرّرُ، و«أمّا» تفصيلٌ لمُجْمَلٍ يتبعُها مبتدأٌ ثمّ فاءٌ',
    "Tu confonds إمّا et أمّا : إمّا choisit entre deux possibilités incompatibles et se répète ; أمّا détaille un ensemble, suivi d'un مبتدأ puis de ف",
    "You confuse إمّا and أمّا: إمّا picks between two incompatible options and repeats; أمّا details a whole, followed by a مبتدأ then ف",
    [U('15', [11], ('04', 4, 'a', "R1 : « إمّا للاختيار لا للتفصيل »"),
                   ('03', 3, 'a', "R1 : « إمّا … وإمّا » proposé pour le تفصيل"), half="2e moitié : « لا تخلط بين إمّا وأمّا »")])

NEW('arabe.rabt.kull-ay-tafsir',
    'تعدُّ كلَّ «أيْ» تفسيرًا: «أيْ بُنيَّ» نداءٌ للقريبِ و«أيُّ الطّريقَينِ؟» استفهامٌ؛ التّفسيرُ جملةٌ تشرحُ ما قبلَها بعبارةٍ أوضحَ',
    "Tu prends tout « أيْ » pour une explication : أيْ بُنيَّ est un appel, أيُّ الطريقين؟ une question ; l'explication reprend plus clairement la phrase précédente",
    "You take every « أيْ » as an explanation: أيْ بُنيَّ calls someone near, أيُّ الطريقين؟ asks a question; explaining restates the previous clause more clearly",
    [U('15', [13], ('04', 2, 'a', "R1 : « أيْ بُنيَّ » = حرف نداء"),
                   ('04', 2, 'b', "R1 : « أيُّ الطريقين » = اسم استفهام"))])

# ---- الحذف ---------------------------------------------------------------------------------
NEW('arabe.hadhf.hukm-min-mawqi3-al-baqi',
    'تحكمُ على الباقي في الجوابِ من موقعِه (فتقولُ: خبرٌ) لا من الجملةِ الكاملةِ التي يعيدُها السّؤالُ: «مَن في القاعةِ؟ — المعلّمُ» الباقي مبتدأٌ',
    "Tu juges le reste de la réponse d'après sa place (« خبر ») et non d'après la phrase complète que rétablit la question : مَن في القاعة؟ — المعلّم : مبتدأ",
    "You judge what's left in the answer from its position (\"khabar\") not from the full sentence the question restores: مَن في القاعة؟ — المعلّم is a مبتدأ",
    [U('15', [16], ('04', 6, 'a', "R1 : « لا نحكمُ على الحارسُ بأنّه خبرٌ لمجرّد أنّه الجوابُ »"))])

# ---- à consolider en fin de passe -----------------------------------------------------------
UNDER3 = [
    ("« المختزلة » mal définie (courte / incompréhensible / lettre ou voyelle supprimée)",
     "15:quiz#5→a,b,c (R1 : l'explication nomme les trois) ; 15:01#6→a,b,d (phrases complètes prises pour des réponses réduites)",
     "1 seule question reconstructible (quiz#5) ; 01#6 n'a pas de chemin d'erreur net."),
    ("Oubli du فاعل / نائب الفاعل : on croit que le verbe est seul omis",
     "15:05#6→b,c,d (R2) ; 15:02#6→d",
     "2 questions (05#6, 02#6). À reprendre si un autre chapitre de hadhf apparaît."),
    ("Verbe au passif traité comme actif (« الفعل والفاعل »)",
     "15:02#6→a,c",
     "1 question."),
    ("ناسخ « كان » de la question ignoré : on lit « صعبًا » comme خبر/مبتدأ marfu3 ou comme complément",
     "15:03#6→a,b,c (R1 : « ونصبُه دليلٌ… »)",
     "1 question (3 distracteurs) ; l'id hukm-min-mawqi3-al-baqi ne dit pas le nasb."),
    ("« إمّا » initial supprimé ou remplacé par « أو » / « ثمّ » au lieu de la répéter",
     "15:04#5→b,c,d",
     "1 question (la `حالة حدّيّة` du cours, pas un piège)."),
    ("Mauvais couple de composants autour de l'اعتراضيّة",
     "15:03#5→a,c,d",
     "1 question ; erreur d'analyse, pas d'idée fausse."),
    ("بل confondu avec لكنّ (استدراك)",
     "15:quiz#4→c",
     "1 question."),
    ("« فإذا » : on y lit la ف de cause + إذا",
     "15:03#4→a (R1 : « والفاء هنا جزء من فإذا وليست فاء السبب »)",
     "1 question."),
    ("أم lue avec le sens de أو (شك / تخيير)",
     "15:02#5→a (aussi name), 15:02#5→b",
     "1 question."),
]


# =====================================================================================
# CHAPITRE 04 — النداء والدعاء والأمر والنهي (12 pièges)
# =====================================================================================
PIEGES['04'] = {
    1: ('§ النداء', 'عدّ ما بعد المنادى ركنًا ثالثًا'),
    2: ('§ أدوات النداء', 'ربط الأداة بالمسافة الحسّيّة وحدها'),
    3: ('§ حكم المنادى: الرفع', 'تنوين المنادى النكرة («يا ولدٌ»)'),
    4: ('§ حكم المنادى: النصب', 'ضمّ المضاف لأنّه علم («يا عبدُ اللهِ»)'),
    5: ('§ الاستغاثة', 'عدّ المستغاث له هو المستغاث'),
    6: ('§ النّدبة', 'عدّ النّدبة استغاثة لأنّ صاحبها في شدّة'),
    7: ('§ الدّعاء', 'الحكم على نوع الدّعاء من شكل الجملة لا من المطلوب'),
    8: ('§ أبنية الدّعاء', 'تغيير حركة ما بقي عند الاختزال («نجاحٌ باهرٌ»)'),
    9: ('§ الأمر والنّهي', 'الحكم على الجملة من نتيجتها العمليّة'),
    10: ('§ صيغ الأمر', 'حصر الأمر في فعل الأمر («صبرًا يا أهلَ الحيّ»)'),
    11: ('§ صيغة النّهي', 'عدّ كلّ «لا» + مضارع نهيًا'),
    12: ('§ معاني الأمر والنّهي', 'الحكم على المعنى من الصيغة وحدها'),
}
NOID_REASON[('04', 8)] = "isolé : aucun distracteur n'est un دعاء réduit remis au nominatif (« نجاحٌ باهرٌ ») ; presque-porteur : 04:04#4→b (« سعادتُكَ دائمةٌ », phrase nominale), mais l'erreur y est « phrase nominale », pas « voyelle changée »."
NOID_REASON[('04', 10)] = "isolé : aucun item ne demande « est-ce un أمر ? » d'un مصدر ou d'une expression ; les questions sur les formes (01#4, 05#4) demandent de reconnaître la forme, et leurs distracteurs sont les trois autres formes."

NEW('arabe.nida.rukn-thalith',
    'تعدُّ ما بعدَ المنادى ركنًا ثالثًا في جملةِ النّداءِ: ركناها حرفُ نداءٍ ومنادًى فقط، وما يقولُه المتكلّمُ بعدَهما جملةٌ أخرى',
    "Tu comptes ce qui suit le منادى comme un troisième pilier : la phrase d'appel n'a que deux piliers, حرف نداء et منادى ; la suite est une autre phrase",
    "You count what follows the منادى as a third pillar: a vocative sentence has only two, حرف نداء and منادى; what comes next is another sentence",
    [U('04', [1], ('quiz', 1, 'd', "R1 : « منادى وما يُطلب منه » ; l'explication : « جملة أخرى لا ركن ثالث »"),
                  ('01', 3, 'd', "R1 : « أعطني باقةً » prise pour un ركن"))])

NEW('arabe.nida.adat-bil-masafa',
    'تختارُ أداةَ النّداءِ بالمسافةِ الحسّيّةِ وحدَها: القربُ والبعدُ حسًّا أو معنًى، ومَن بجانبِك قد يُنادى بـ«أيا» إن كان بعيدًا معنًى',
    "Tu choisis l'outil d'appel d'après la seule distance physique : proche ou lointain se mesure aussi au sens ; qui est à côté de toi peut être appelé par أيا",
    "You choose the vocative particle by physical distance alone: near or far is also a matter of attention; someone beside you can be called with أيا",
    [U('04', [2], ('05', 1, 'c', "R1 : « قريب حسًّا ومعنًى » — l'élève ne compte que la distance physique"))])

NEW('arabe.nida.tanwin-al-munada',
    'تنوِّنُ المنادى لأنّه نكرةٌ (يا ولدٌ، يا حارسٌ البستانِ): المنادى المضمومُ لا يُنوَّنُ ولا يجتمعُ التّنوينُ مع الإضافةِ؛ ينوَّنُ الموصوفُ المنصوبُ فقط',
    "Tu mets le tanwin au منادى car il est indéfini (يا ولدٌ) : à la damma il n'en a pas, et il ne va pas avec l'annexion ; seul le موصوف منصوب en porte",
    "You put tanwin on the vocative because it is indefinite (يا ولدٌ): a damma-vocative takes no tanwin, none with annexation; only the described accusative has it",
    [U('04', [3], ('02', 2, 'b', "R1 : « التّنوين لا يجتمع مع الإضافة » — seul porteur ; le piège du cours (« يا ولدٌ ») n'a pas de porteur exact"),
                  half="geste commun : tanwin sur un منادى")])

NEW('arabe.nida.mudaf-marfu3',
    'تضمُّ المضافَ في المنادى المركّبِ الإضافيّ لأنّه علمٌ (يا عبدُ اللهِ) أو تكسرُه: العلمُ المفردُ وحدَه يُضمُّ، والمضافُ يُنصَبُ: يا عبدَ اللهِ',
    "Tu mets le مضاف d'un منادى annexé à la damma, comme un nom propre (يا عبدُ اللهِ), ou à la kasra : seul le علم مفرد prend la damma ; le مضاف est à l'accusatif",
    "You give the مضاف of an annexed vocative a damma because it is a name (يا عبدُ اللهِ), or a kasra: only a single-word name takes damma; the مضاف is accusative",
    [U('04', [4], ('02', 2, 'a', "R1 : « الضمّة للعلم المفرد… » — « يا حارسُ البستانِ »"),
                  ('02', 2, 'c', "R1 : « الكسرة ليست حكم المنادى »"))])

NEW('arabe.nida.nasb-al-marfu3',
    'تنصبُ العلمَ المفردَ أو النّكرةَ المقصودةَ أو المعرَّفَ بـ«ال» في النّداءِ: هذه الثّلاثةُ تُضمُّ (يا سامرُ، يا ولدُ)؛ النّصبُ للمضافِ وللموصوفِ',
    "Tu mets à l'accusatif le علم مفرد, la نكرة مقصودة ou le défini en ال : ces trois prennent la damma (يا سامرُ، يا ولدُ) ; le نصب va au مضاف et au موصوف",
    "You make a one-word name, intended indefinite or ال-noun accusative: these three take damma (يا سامرُ، يا ولدُ); accusative is for the مضاف and the موصوف",
    [U('04', [], ('quiz', 2, 'a', "R2 : علم مفرد ← « ينصب »"),
                 ('quiz', 2, 'b', "R2 : نكرة مقصودة ← « ينصب »"),
                 ('quiz', 2, 'c', "R2 : معرّف بأل ← « ينصب »"),
                 ('04', 2, 'd', "R1 : « المعرّف بالألف واللام من حالات الرفع »"),
                 ('06', 2, 'c', "R1 : « العلم ينصب دائمًا إذا نودي »"))])

NEW('arabe.nida.shakl-nahwi-khalt',
    'تسمّي المنادى بغيرِ شكلِه النّحويّ: اسألْ هل هو اسمُ شخصٍ في كلمةٍ؟ هل قُصدَ به معيَّنٌ؟ هل فيه «ال»؟ هل هو مضافٌ؟ هل وُصفَ ولم يُقصَدْ؟',
    "Tu nommes mal la forme du منادى : est-il un nom propre d'un mot, vise-t-il quelqu'un de précis, a-t-il ال, est-il annexé, est-il décrit et non visé ?",
    "You label the vocative with the wrong grammatical form: ask if it is a one-word name, aims at someone specific, has ال, is annexed, or is described and unaimed",
    [U('04', [], ('02', 1, 'a', "R1 : « ليست علمًا مفردًا لأنّها ليست اسم شخص »"),
                 ('02', 1, 'c', "R1 : « قصد معيّنًا ولم يصفه »"),
                 ('02', 1, 'd', "R1 : « خالية من الألف واللام »"),
                 ('02', 4, 'a', "R1 : علم مفرد pour « يا سائقًا كريمًا »"),
                 ('02', 4, 'b', "R1 : مركّب إضافيّ pour « يا سائقًا كريمًا »"),
                 ('02', 4, 'd', "R1 : نكرة مقصودة pour une نكرة غير مقصودة"),
                 ('04', 3, 'a', "R1 : types intervertis"),
                 ('04', 3, 'c', "R1 : types mal nommés"),
                 ('04', 3, 'd', "R1 : types mal nommés"),
                 ('06', 2, 'a', "R1 : « علم معيَّن » pris pour نكرة موصوفة"),
                 ('06', 2, 'b', "R1 : « عبد خالٍ من الألف واللام »"))])

NEW('arabe.nida.mustaghath-wa-lah-khalt',
    'تخلطُ بينَ المستغاثِ والمستغاثِ له والمستغاثِ منه: المستغاثُ مَن تناديه (لامُه مفتوحةٌ)، وله مَن تستغيثُ لأجلِه (مكسورةٌ)، ومنه ما تستغيثُ بسببِه (بـ«مِنْ»)',
    "Tu confonds مستغاث, مستغاث له et مستغاث منه : le مستغاث est celui que tu appelles (lam fatha), le له celui pour qui (kasra), le منه ce qui menace (par مِنْ)",
    "You mix up مستغاث (who you call, lam fatha), مستغاث له (who it is for, kasra) and مستغاث منه (what threatens, with مِنْ)",
    [U('04', [5], ('01', 6, 'a', "R1 : اللصوص (منه) pris pour مستغاث له"),
                  ('01', 6, 'b', "R1 : المستغاث pris pour مستغاث منه et inversement"),
                  ('01', 6, 'd', "R1 : الشرطة (المستغاث) pris pour مستغاث له"),
                  ('02', 5, 'a', "R1 : لامان inversés"),
                  ('02', 5, 'c', "R1 : « يوحّدهما » — deux lam fatha"),
                  ('02', 5, 'd', "R1 : « يوحّدهما » — deux lam kasra"),
                  ('06', 3, 'a', "R1 : lam kasra au مستغاث, fatha au له"),
                  ('06', 3, 'c', "R1 : « مِنْ » donné au مستغاث له"),
                  ('06', 3, 'd', "R1 : « مِنْ » donné au مستغاث"))])

NEW('arabe.nida.nudba-istighatha',
    'تخلطُ النّدبةَ بالاستغاثةِ أو بالنّداءِ العاديّ لأنّ صاحبَها في شدّةٍ: النّدبةُ تتفجّعُ (وا + مندوبٌ بألفٍ وهاءٍ)، لا تطلبُ عونًا ولا تنبِّهُ',
    "Tu confonds ندبة, استغاثة et appel ordinaire parce que l'auteur souffre : la ندبة se lamente (وا + مندوب en ـاه), elle ne demande pas d'aide et n'alerte pas",
    "You confuse ندبة, استغاثة and a plain call because the speaker suffers: ندبة laments (وا + مندوب ending in ـاه), it asks for no help and does not alert",
    [U('04', [6], ('04', 1, 'a', "R1 : « يا لَلقومِ لِلولدِ » = استغاثة"),
                  ('04', 1, 'b', "R1 : نداء عاديّ « يا ولدُ »"),
                  ('04', 1, 'c', "R1 : نداء عاديّ « أيا ولدُ »"),
                  ('05', 3, 'a', "R1 : حرف نداء للاستغاثة + مستغاث"),
                  ('05', 3, 'b', "حرف ندبة صحيح mais « مستغاث »"),
                  ('05', 3, 'd', "R1 : حرف نداء للاستغاثة + مندوب"))])

NEW('arabe.talab.dua-min-shakl-al-jumla',
    'تحكمُ على نوعِ الدّعاءِ من شكلِ الجملةِ (فيها «لا» ← عليه، مثبتةٌ ← له) لا من المطلوبِ: نفيُ الشّرِّ خيرٌ (لا أراك اللهُ مكروهًا) ونفيُ الخيرِ شرٌّ',
    "Tu juges un دعاء d'après la forme (لا ← contre, affirmatif ← pour), pas d'après ce qui est demandé : nier un mal est un bien (لا أراك الله مكروهًا)",
    "You judge a دعاء by its form (لا ← against, affirmative ← for) rather than by what is asked: negating an evil is a good (لا أراك الله مكروهًا)",
    [U('04', [7], ('02', 6, 'a', "R1 : « المنفيّ شرّ فنفيه خير » — « لا » ⇒ عليه"),
                  ('02', 6, 'd', "R1 : idem — « لا حرمك الله »"),
                  ('04', 4, 'd', "R1 (faible) : la négation « لا » ignorée"),
                  ('06', 4, 'd', "R1 : « لا بارك الله » lu comme دعاء له"))])

NEW('arabe.talab.hukm-bi-natija',
    'تحكمُ على الأمرِ أو النّهيِ من نتيجتِه العمليّةِ: «لا تتراجعْ» نهيٌ لأنّه يطلبُ الكفَّ، و«واصلْ» أمرٌ لأنّه يطلبُ القيامَ، وإن اتّفقتِ النّتيجةُ',
    "Tu juges un ordre ou une interdiction par son résultat : لا تتراجعْ est un نهي (demande de s'abstenir), واصلْ un أمر (demande d'agir), même à effet égal",
    "You judge an order or ban by its outcome: لا تتراجعْ is a نهي (asks to refrain), واصلْ an أمر (asks to act), even if the effect is the same",
    [U('04', [9], ('01', 5, 'a', "R1 : « ليس أمرًا وإن كان يريد أن يواصل »"),
                  ('05', 2, 'a', "R2 : أمر de même effet que le نهي attendu"),
                  ('05', 2, 'd', "R2 : أمر بلام de même effet"),
                  ('06', 1, 'a', "R1 : عمل inversé d'après le sens"),
                  ('06', 1, 'b', "R1 : « كلاهما أمر لأنّ المعنى واحد »"),
                  ('06', 1, 'd', "R1 : « كلاهما نهي لأنّ المعنى واحد »"))])

NEW('arabe.talab.kull-la-nahy',
    'تعدُّ كلَّ «لا» + مضارعٍ نهيًا (لا يكذبُ الصّادقُ): النّهيُ طلبُ كفٍّ بمضارعٍ مجزومٍ، والمضارعُ المرفوعُ خبرٌ لا طلبَ فيه',
    "Tu prends tout « لا » + présent pour un نهي (لا يكذبُ الصادقُ) : le نهي demande de s'abstenir avec un présent مجزوم ; un présent مرفوع est un constat",
    "You take every « لا » + present for a نهي (لا يكذبُ الصادقُ): a نهي asks to refrain with a مجزوم verb; a مرفوع verb is a statement",
    [U('04', [11], ('04', 5, 'd', "R1 : « خبر مضارعه مرفوع لا طلب فيه »"),
                   ('05', 2, 'c', "R1 : « خبر مضارعه مرفوع لا طلب فيه »"))])

NEW('arabe.talab.ma3na-bila-maqam',
    'تحدّدُ المعنى السّياقيَّ للأمرِ أو النّهيِ دونَ قراءةِ المقامِ: مَن يخاطبُ مَن، وما علاقتُهما، وما غرضُه؛ فالصّيغةُ الواحدةُ تأذنُ وتتضرّعُ وتهدّدُ',
    "Tu fixes le sens d'un ordre ou d'une interdiction sans lire le مقام : qui parle à qui, quelle relation, quel but ; une forme peut permettre, supplier, menacer",
    "You fix the contextual meaning of an order or ban without reading the مقام: who speaks to whom, their relation, the goal; one form can permit, plead or threaten",
    [U('04', [12], ('quiz', 5, 'a', "R1 : الإلزام (sens par défaut) malgré « من فضلك »"),
                   ('quiz', 5, 'b', "R1 : الدعاء — destinataire = camarade"),
                   ('quiz', 5, 'd', "R1 : التهديد « لا يأتي مع من فضلك »"),
                   ('04', 6, 'a', "R1 : الإباحة lue dans « كما تشاء »"),
                   ('04', 6, 'b', "R1 : النصح"),
                   ('04', 6, 'c', "R1 : الالتماس"),
                   ('05', 5, 'a', "R1 : الإباحة"),
                   ('05', 5, 'c', "R1 : النصح"),
                   ('05', 5, 'd', "R1 : التخيير"),
                   ('06', 6, 'a', "R1 : نصح d'un père"),
                   ('06', 6, 'b', "R1 : التماس « من فضلك »"),
                   ('06', 6, 'c', "R1 : إلزام d'un entraîneur"))])

NEW('arabe.talab.sigha-amr-khalt',
    'تخلطُ بينَ صيغِ الأمرِ: فعلُ الأمرِ، والمضارعُ المجزومُ بلامِ الأمرِ، والمصدرُ النّائبُ (منصوبٌ بلا فعلٍ)، والعباراتُ (عليكَ، دونَكَ، إليكَ)',
    "Tu confonds les formes de l'ordre : فعل الأمر, présent مجزوم après لام الأمر, مصدر نائب (accusatif sans verbe), expressions (عليكَ، دونَكَ، إليكَ)",
    "You mix up the forms of the order: the imperative, a jussive after لام الأمر, the standing-in مصدر (accusative, no verb), and expressions (عليكَ، دونَكَ، إليكَ)",
    [U('04', [], ('01', 4, 'a', "R2 : فعل أمر pris pour مصدر نائب"),
                 ('01', 4, 'b', "R2 : لام الأمر pris pour مصدر نائب"),
                 ('01', 4, 'c', "R2 : عبارة prise pour مصدر نائب"),
                 ('05', 4, 'a', "R2 : فعل أمر pris pour عبارة"),
                 ('05', 4, 'b', "R2 : لام الأمر prise pour عبارة"),
                 ('05', 4, 'c', "R2 : مصدر نائب pris pour عبارة"),
                 ('quiz', 4, 'a', "R1 : صيغة أمر donnée pour le نهي"),
                 ('quiz', 4, 'c', "R1 : صيغة أمر donnée pour le نهي"),
                 ('quiz', 4, 'd', "R1 : « لا يدخل حرف النفي على فعل الأمر »"))])

UNDER3 += [
    ("لام الأمر sans جزم : le présent reste marfu3 / mansub / kasra après « ليـ »",
     "04:02#3→b,c,d (R2)",
     "1 question. (Proche de `arabe.tawjih.nahy-marfu3` mais celui-ci dit « لا » النّاهية.)"),
    ("« الله + présent marfu3 » pris pour un دعاء (calque du dialecte : الله يحفظك)",
     "04:quiz#3→d (R1) ; 04:05#6→d (R1)",
     "2 questions (3 avec 04:04#4→a, mais l'explication de celui-ci nomme « phrase complète » et non l'erreur de dialecte). À reprendre : la meilleure candidate du chapitre."),
    ("« لا » + verbe passé (لا بارك الله) lu comme un نهي",
     "04:06#4→b,c (R1 : « الماضي بعده يجعلها نفيًا »)",
     "1 question."),
    ("« يا » + « ال » collés (يا المسافرُ)",
     "04:04#2→a (b cumule avec le نصب)",
     "1 question ; la `propriete` du cours l'énonce (« فلا نقول يا الطالبُ ») sans piège."),
    ("Nombre de formes d'ordre compté sur les verbes (06#5)",
     "04:06#5→a,b,d",
     "1 question."),
    ("Phrase d'appel prise pour une phrase verbale / nominale (فعل وفاعل، مبتدأ وخبر)",
     "04:quiz#1→a,b",
     "1 question."),
    ("Le منادى réduit à son premier mot (« يا » + « بائع »)",
     "04:01#3→b (R1 : « ركن واحد وإن كان كلمتين »)",
     "1 question ; couvert par le `verifie` du cours."),
    ("Dua pris pour un أمر ou pour un نداء",
     "04:01#2→b,c ; 04:quiz#3→b,c",
     "2 questions, mais sans chemin d'erreur net."),
    ("Lecture de la liste des outils d'appel (qui est pour proche / lointain)",
     "04:01#1→a,c,d",
     "1 question de pure mémoire."),
]


PRECEDENCE += [
    "**Questions « nom + raison » (15:01#3, 15:05#2, 15:02#5)** — `rabt.ism-al-harf-min-shaklih` prime quand la raison donnée est VRAIE mais ne peut pas fonder le nom (« جمع بدون ترتيب » pour dire عطف) ; `rabt.waw-tartib` quand la raison est fausse en soi (الواو « ترتيب » ou « ترتيب وتراخٍ »). Nom faux ET raison fausse : muet.",
    "**Rang / fonction** — `rabt.rutba-bi-shakl-la-bil-unsur` dès que les options se partagent entre ابتدائيّة et استئنافيّة ; `rabt.i3tirad-wal-hal-khalt` dès qu'une option oppose l'اعتراضيّة à une fonction (حال، مفعول فيه، خبر).",
    "**Conséquence / permutation** — `rabt.natija-bi-ghayr-al-fa` quand la question demande « quel outil dit la conséquence ? » ; `rabt.fa-thumma-bila-tartib` quand elle demande « si on permute ou remplace, que devient le sens ? ».",
    "**بل** — `rabt.bal-bila-nazar-fil-ula` ne couvre que les trois sens إضراب / تقرير / تأكيد pris l'un pour l'autre ; بل ↔ استدراك (15:quiz#4→c) reste muet (< 3).",
    "**أمّا / إمّا** — `rabt.amma-bila-fa` (فاء absente) et `rabt.imma-amma-khalt` (mauvais outil) ne se cumulent jamais : l'option qui fait les deux (15:04#4→d) est muette.",
    "**Type / degré d'une phrase (jumla)** — une option fausse à la fois sur le type et sur le degré (15:04#3→c) est muette ; `jumla.naw3-bi-fi3l` ne vaut que si le TYPE est la seule erreur, `jumla.isnad-far3i-la-yura` que si le DEGRÉ l'est.",
    "**Nasb / noms de forme (nida)** — `nida.nasb-al-marfu3` quand l'option affirme un RÉGIME erroné (« ينصب ») ; `nida.shakl-nahwi-khalt` quand elle affirme un NOM de forme erroné (« نكرة موصوفة… ») ; les deux à la fois (04:04#3→d, 04:04#2→b) : muet.",
    "**Voyelle posée sur le مضاف** — damma ou kasra : `nida.mudaf-marfu3` ; tanwin : `nida.tanwin-al-munada`.",
    "**استغاثة / ندبة** — l'option qui change le NOM de l'acte (استغاثة ↔ ندبة ↔ نداء) : `nida.nudba-istighatha` ; celle qui garde l'acte mais redistribue les rôles ou les lam : `nida.mustaghath-wa-lah-khalt`.",
    "**Amr / nahy** — `talab.hukm-bi-natija` pour « quelle phrase est un نهي / un أمر ? » avec des distracteurs de même effet pratique ; `talab.sigha-amr-khalt` pour « quelle FORME ? ». Un « لا » + présent مرفوع pris pour نهي : `talab.kull-la-nahy` ; un « لا » + passé de دعاء jugé sur la forme : `talab.dua-min-shakl-al-jumla`.",
    "**Sens contextuel** — `talab.ma3na-bila-maqam` ne s'applique qu'aux questions de مقام (quel sens prend l'ordre ici ?) et à toutes leurs options fausses.",
]


# =====================================================================================
# CHAPITRE 16 — الاستفهام (9 pièges)
# =====================================================================================
PIEGES['16'] = {
    1: ('§ حرفا الاستفهام', 'تقديم حرف الاستئناف على الهمزة أو تأخيره عن «هل» (وَأَتَقْبَلُ، هَلْ وَتَقْبَلُ)'),
    2: ('§ المثبتة والمنفيّة', 'الحكم على غاية السائل من علامة الاستفهام وحدها'),
    3: ('§ الجواب: نعم وبلى', 'الجواب بـ«نعم، قرأتُها» عن سؤال منفيّ'),
    4: ('§ أسماء الاستفهام', 'السؤال عن شخص بـ«ما»'),
    5: ('§ وظيفة اسم الاستفهام', 'الحكم على الوظيفة من الترتيب («ما» مبتدأ لأنّها أوّل الجملة)'),
    6: ('§ الاستفهام وعدم اليقين', 'ختم جملة عدم اليقين بعلامة استفهام'),
    7: ('§ الاستفهام والتسوية', 'استعمال «هل» مكان الهمزة في التسوية'),
    8: ('§ اسم الاستفهام المقترن بحرف الجرّ', 'قراءة المعنى من حرف الجرّ وحده'),
    9: ('§ مركّب الجرّ خبرًا مقدّمًا', 'عدّ الاسم بعد مركّب الجرّ فاعلًا («مِنْ أَيِّ مَدِينَةٍ أَنْتَ؟»)'),
}
NOID_REASON[('16', 6)] = "isolé : aucun item ne propose de ponctuation ni de « ؟ » en fin de phrase d'incertitude (les options de 02#3 et 05#1 sont des phrases nues ou des composants) ; l'erreur n'existe que dans le cours."

NEW('arabe.istifham.rutba-al-harf',
    'تقدِّمُ حرفَ الاستئنافِ على الهمزةِ أو تؤخِّرُه عن «هل» (وَأَتَقْبَلُ، هَلْ وَتَقْبَلُ): الهمزةُ قبلَه، و«هل» بعدَه: أَوَ تَقْبَلُ؟ وَهَلْ تَقْبَلُ؟',
    "Tu mets و/ف avant la hamza ou après « هل » (وَأَتَقْبَلُ، هَلْ وَتَقْبَلُ) : la hamza précède le connecteur, « هل » le suit : أَوَ تَقْبَلُ؟ وَهَلْ تَقْبَلُ؟",
    "You put و/ف before the hamza or after « هل » (وَأَتَقْبَلُ، هَلْ وَتَقْبَلُ): the hamza comes before the connector, « هل » after it: أَوَ تَقْبَلُ؟ وَهَلْ تَقْبَلُ؟",
    [U('16', [1], ('04', 1, 'a', "R1 : واو قبل الهمزة"),
                  ('04', 1, 'b', "R1 : واو بعد « هل »"))])

NEW('arabe.istifham.ghaya-min-al-shakl',
    'تحكمُ على غايةِ السّؤالِ من علامةِ الاستفهامِ أو من النّفيِ وحدِهما، لا ممّا يعلمُه السّائلُ: يعلمُ ← تذكيرٌ، وينتظرُ ولا يعلمُ ← استخبارٌ عن متوقَّعٍ',
    "Tu juges le but d'une question d'après le « ? » ou la négation seuls, pas d'après ce que sait celui qui la pose : il sait ← rappel ; il attend sans savoir ← demande d'un fait attendu",
    "You judge a question's purpose from the \"?\" or the negation alone, not from what the asker knows: knows ← reminder; expects without knowing ← asks about an expected event",
    [U('16', [2], ('01', 4, 'a', "R1 : « الاستخبار عن مجهول » alors que la mère sait"),
                  ('01', 4, 'b', "R1 : « متوقَّع » alors que la mère sait"),
                  ('03', 2, 'a', "R1 : « تذكير » alors que le marchand ignore"),
                  ('04', 2, 'b', "R1 : « تذكير بمعلوم » alors que le voyageur ignore"))])

NEW('arabe.istifham.harf-jawab-yunaqid',
    'تتبعُ حرفَ الجوابِ بجملةٍ تناقضُه: بعدَ سؤالٍ منفيٍّ «نعم» تُثبِتُ النّفيَ فيتبعُها نفيٌ، و«بلى» تُبطِلُه فيتبعُها إثباتٌ (بلى، كتبتُه)',
    "Tu fais suivre le mot de réponse d'une phrase qui le contredit : après une question négative, نعم confirme la négation (suivie d'un nié), بلى l'annule (suivie d'un affirmé)",
    "You follow the answer word with a clause that contradicts it: after a negative question, نعم confirms the negation (then a negative), بلى cancels it (then an affirmative)",
    [U('16', [3], ('quiz', 2, 'b', "R1 : « نعم، كتبتُه »"),
                  ('quiz', 2, 'c', "R1 : « لا، كتبتُه »"),
                  ('quiz', 2, 'd', "R1 : « بلى، لم أكتبْه »"),
                  ('02', 1, 'b', "R1 : « بلى، لم أفقدْها »"),
                  ('02', 1, 'd', "R1 : « نعم، فقدتُ حقيبتي » se contredit"),
                  ('04', 2, 'c', "R1 : « نعم، وصلت » se contredit"))])

NEW('arabe.istifham.ism-ghayr-munasib',
    'تختارُ اسمَ الاستفهامِ على غيرِ نوعِ المجهولِ (ما عن شخصٍ، متى عن مكانٍ): مَن للعاقلِ، وما لغيرِه، وأينَ للمكانِ، ومتى للزّمانِ، وكيفَ للهيئةِ، وكَمْ للعددِ',
    "Tu choisis un nom interrogatif qui ne correspond pas à l'inconnu (ما pour une personne, متى pour un lieu) : مَن personne, ما chose, أين lieu, متى temps, كيف manière, كم nombre",
    "You pick an interrogative noun that doesn't fit the unknown (ما for a person, متى for a place): مَن person, ما thing, أين place, متى time, كيف manner, كم number",
    [U('16', [4], ('01', 5, 'a', "R1 : « ما » pour un شخص — le piège du cours"),
                  ('01', 5, 'c', "R1 : أين pour un شخص"),
                  ('01', 5, 'd', "R1 : كم pour un شخص"),
                  ('01', 3, 'b', "متى pour le lieu"),
                  ('01', 3, 'c', "كيف pour le lieu"),
                  ('01', 3, 'd', "مَن pour le lieu"),
                  ('05', 2, 'a', "sens de كيف donné à كم"),
                  ('05', 2, 'b', "sens de أيّ donné à كم"),
                  ('05', 2, 'c', "sens de متى donné à كم"),
                  ('05', 6, 'a', "أين pour le temps"),
                  ('05', 6, 'c', "كيف pour le temps"),
                  ('05', 6, 'd', "كم pour le temps"))])

NEW('arabe.istifham.harf-ism-khalt',
    'تخلطُ بينَ حرفَي الاستفهامِ وأسمائِه: الهمزةُ و«هل» تسألانِ عن مضمونِ الجملةِ ويُجابُ بنعم أو لا، والاسمُ يسألُ عن عنصرٍ ويُجابُ بكلمةٍ',
    "Tu confonds les deux particules (أ، هل) et les noms interrogatifs : les particules interrogent le contenu de la phrase (réponse نعم/لا), le nom un élément (réponse = un mot)",
    "You confuse the two interrogative particles (أ، هل) with interrogative nouns: particles question the whole content (answer نعم/لا), a noun questions one element (answer = a word)",
    [U('16', [], ('quiz', 1, 'a', "R2 : « مَن وما » donnés pour interroger le contenu"),
                 ('quiz', 1, 'b', "R2 : « كيف وأين »"),
                 ('quiz', 1, 'd', "R2 : « متى وكم »"),
                 ('01', 1, 'a', "R2 : « متى » pour une question de contenu"),
                 ('01', 1, 'c', "R2 : « كيف »"),
                 ('01', 1, 'd', "R2 : « أين »"),
                 ('03', 1, 'a', "R2 : réponse attendue = lieu pour une question en أ"),
                 ('03', 1, 'b', "R2 : réponse attendue = temps"),
                 ('03', 1, 'c', "R2 : réponse attendue = nombre"))])

NEW('arabe.istifham.wazifa-bila-jawab',
    'تحدّدُ وظيفةَ اسمِ الاستفهامِ من موقعِه في الصّدارةِ لا من العنصرِ الذي يحلُّ محلَّه في الجوابِ: «ما اشتريتَ؟» ← تفّاحًا: مفعولٌ به لا مبتدأٌ',
    "Tu fixes la fonction du nom interrogatif d'après sa place en tête de phrase et non d'après l'élément qui le remplace dans la réponse : ما اشتريتَ؟ ← تفّاحًا : مفعول به",
    "You fix an interrogative noun's function from its place at the front, not from the element that replaces it in the answer: ما اشتريتَ؟ ← تفّاحًا: مفعول به, not مبتدأ",
    [U('16', [5], ('quiz', 4, 'a', "R1 : « مبتدأ لمجرّد أنّها في أوّل الجملة »"),
                  ('quiz', 4, 'c', "fonction étrangère à la réponse « نشيط »"),
                  ('quiz', 4, 'd', "fonction étrangère à la réponse"),
                  ('02', 2, 'a', "R1 : « مبتدأ لأنّها تتصدّر الجملة »"),
                  ('02', 2, 'b', "R1 : « فاعل لأنّها تسبق الفعل »"),
                  ('02', 2, 'd', "R1 : « خبر مقدّم لأنّ الاسم يتقدّم دائمًا »"),
                  ('01', 6, 'a', "fonction étrangère à la réponse « مبتسمًا »"),
                  ('01', 6, 'b', "idem"),
                  ('01', 6, 'c', "idem"),
                  ('03', 4, 'b', "مفعول فيه للزمان alors que la réponse est un lieu"),
                  ('03', 4, 'c', "idem"),
                  ('03', 4, 'd', "idem"),
                  ('04', 3, 'a', "paire « مسرعًا » = حال, non مطلق"),
                  ('04', 3, 'c', "paire « متعب » = خبر"),
                  ('04', 3, 'd', "paire « نشيطًا » = خبر كان"))])

NEW('arabe.istifham.hal-makan-al-hamza',
    'تضعُ «هل» مكانَ الهمزةِ في جملةِ التّسويةِ (سيّانِ عندي هلْ حضرتَ أمْ غبتَ): التّسويةُ تقتضي همزةَ الاستفهامِ ثمّ «أم»',
    "Tu mets « هل » à la place de la hamza dans une phrase de تسوية (سيّان عندي هل حضرتَ أم غبتَ) : la تسوية exige la hamza interrogative puis « أم »",
    "You use « هل » instead of the hamza in a تسوية sentence (سيّان عندي هل حضرتَ أم غبتَ): the تسوية needs the interrogative hamza followed by « أم »",
    [U('16', [7], ('02', 4, 'a', "R1 : « لا تقوم هل مقام الهمزة في هذا التركيب »"))])

NEW('arabe.istifham.jarr-min-al-harf-wahdah',
    'تقرأُ معنى مركّبِ الجرِّ من حرفِ الجرِّ وحدَه (لِمَنْ سلّمتَ؟ سببيّةٌ لأنّ فيها «لـ»): الذي يعيّنُ المعنى هو السّياقُ والجوابُ لا الحرفُ',
    "Tu lis le sens d'un مركّب جرّ d'après la seule préposition (لِمَنْ سلّمتَ؟ = cause parce qu'il y a لـ) : le contexte et la réponse le fixent, pas la préposition",
    "You read a prepositional phrase's meaning from the preposition alone (لِمَنْ سلّمتَ؟ = cause because of لـ): context and the answer fix it, not the preposition",
    [U('16', [8], ('02', 5, 'b', "R1 : « مفعول لأجله » — il ne demande pas de cause"),
                  ('04', 5, 'b', "R1 : « لِمَنْ سلّمتَ » pris pour une سببيّة"))])

NEW('arabe.istifham.markab-jarr-khabar-aw-mutammim',
    'تعاملُ مركّبَ الجرِّ دونَ النّظرِ إلى وجودِ الفعلِ: بعدَ فعلٍ هو متمّمٌ له، وفي جملةٍ بلا فعلٍ هو خبرٌ مقدّمٌ والاسمُ بعدَه مبتدأٌ مؤخَّرٌ لا فاعلٌ',
    "Tu traites le مركّب جرّ sans regarder s'il y a un verbe : après un verbe c'est son complément ; sans verbe c'est un خبر مقدّم, et le nom suivant un مبتدأ مؤخّر, non un فاعل",
    "You treat a prepositional phrase without checking for a verb: after a verb it is its complement; in a verbless sentence it is a fronted khabar and the next noun a delayed mubtada, not a subject",
    [U('16', [9], ('quiz', 5, 'a', "R1 : « مفعول به » dans une phrase sans verbe"),
                  ('quiz', 5, 'b', "R1 : « مفعول لأجله » dans une phrase sans verbe"),
                  ('quiz', 5, 'd', "R1 : « حال » dans une phrase sans verbe"),
                  ('02', 5, 'd', "R1 : « لا خبرًا مقدّمًا لأنّ في الجملة فعلًا »"),
                  ('02', 6, 'a', "R1 : verbe présent « تسكن » ⇒ complément"),
                  ('02', 6, 'b', "R1 : verbe présent « وُلدتَ »"),
                  ('02', 6, 'd', "R1 : verbe présent « درستَ »"),
                  ('03', 6, 'a', "raison = la préposition « لـ » en tête"),
                  ('03', 6, 'c', "raison = le nom interrogatif « مَن »"),
                  ('03', 6, 'd', "raison = le démonstratif"))],
    note="Le piège n°9 (« أنتَ فاعل ») n'a pas de porteur littéral : l'id est porté par le même geste (ignorer l'absence de verbe). À signaler à l'orchestrateur.")

UNDER3 += [
    ("« بلى » donné à une question positive (ou à une question en اسم استفهام)",
     "16:01#2→b,c ; 16:03#3→a,b,d",
     "2 questions ; la `propriete` du cours l'énonce (« لا يصحّ أحضرتَ؟ — بلى ») sans piège."),
    ("La تسوية crue portée par la hamza ou par « أم » seules (et non par سيّان / سواء)",
     "16:05#3→b ; 16:05#5→a,b",
     "2 questions (R1 pour les deux)."),
    ("« وهل أ… » : cumul de « هل » et de la hamza",
     "16:04#1→d (R1 : « الجمع بين هل والهمزة خطأ في الرتبة »)",
     "1 question ; autre geste que l'ordre du connecteur."),
    ("Marque d'إعراب de « أيّ » (damma / kasra / tanwin au lieu de la fatha de المفعول به)",
     "16:04#4→a,b,c (R1)",
     "1 question."),
    ("Fonction du groupe entier après un verbe d'incertitude : « فاعل » au lieu de مفعول به",
     "16:05#4→a (R1 : « ليس فاعلًا لأنّ فاعل أعرف هو أنا »)",
     "1 question."),
    ("Sens d'un مركّب جرّ pris d'après la préposition de la question (إلى / من / في)",
     "16:03#5→a,b,c",
     "1 question."),
    ("Un مركّب جرّ jugé « non remplaçable » alors qu'il se remplace (متى، أين، كيف)",
     "16:04#6→a,b,d (R2)",
     "1 question."),
    ("Le composant porteur de l'incertitude confondu avec le nom interrogatif (« أيّ ») ou le reste de la phrase",
     "16:05#1→a,c,d",
     "1 question."),
    ("« أيّ » seul parmi les noms lié à l'annexion : on en prête l'obligation à مَن / كيف / كم",
     "16:quiz#3→a,b,c",
     "1 question."),
]


PRECEDENCE += [
    "**Istifham : catégorie avant détail** — `istifham.harf-ism-khalt` quand l'élève se trompe de CATÉGORIE (nom pour particule ou l'inverse) ; `istifham.ism-ghayr-munasib` quand il est dans la bonne catégorie (les noms) mais prend le mauvais nom.",
    "**Question mixte but + réponse (16:04#2)** — option juste en réponse mais fausse en but : `istifham.ghaya-min-al-shakl` ; juste en but mais réponse qui se contredit : `istifham.harf-jawab-yunaqid` ; juste en but, réponse cohérente mais pour l'état inverse (04#2→d) : muet.",
    "**Fonction** — sur un NOM interrogatif (ما، كيف، أين) : `istifham.wazifa-bila-jawab` ; sur un مركّب جرّ (حرف + اسم) : `istifham.markab-jarr-khabar-aw-mutammim` pour le couple verbe / sans verbe, `istifham.jarr-min-al-harf-wahdah` pour le sens tiré de la préposition. Une option étrangère aux deux (16:02#5→c « مفعول فيه ») reste muette.",
]


# =====================================================================================
# CHAPITRE 17 — الشرط (11 pièges)   [libellés lus dans ch17_labels_draft.json]
# =====================================================================================
import json as _json
_D17 = _json.load(open('/tmp/claude-0/-home-user/8ff73c67-6eab-5a69-a66d-d237b8d69142/scratchpad/ar9/tags/work-A/ch17_labels_draft.json', encoding='utf-8'))


def _N17(i, key, uses, note=''):
    NEW(i, _D17[key]['ar'], _D17[key]['fr'], _D17[key]['en'], uses, note)


PIEGES['17'] = {
    1: ('§ ما الشرط ؟', 'الحكم على الحدثين بترتيب ذكرهما (الرئيسيّ هو الأوّل)'),
    2: ('§ حرف الشرط «إنْ»', 'ترك المضارع مرفوعًا بعد «إنْ» + جزم الرئيسيّ المتقدّم'),
    3: ('§ حرف الشرط «لو»', 'استعمال «لو» في حدث ما يزال ممكنًا (لو جاء الأستاذ غدًا)'),
    4: ('§ فاء الربط', 'ترك الفاء لأنّ المعنى مفهوم (إنْ تعبتَ ارتحْ)'),
    5: ('§ اسم شرط أم اسم موصول ؟', 'عدّ كلّ «مَنْ» و«ما» في أوّل الكلام اسمَي شرط'),
    6: ('§ أسماء الشرط العشرة', 'اختيار الاسم بحسب الكلمة الأقرب لا المعنى (ما يتأخّر، متى/أينما)'),
    7: ('§ وظيفة اسم الشرط', 'عدّ المركّب الموصوليّ مبتدأً لمجرّد أنّه في أوّل الجملة'),
    8: ('§ افتراض الممكن', 'عدّ الماضي بعد «إنْ» دليلًا على أنّ الحدث لم يقع كما في «لو»'),
    9: ('§ افتراض الممتنع', 'قراءة الماضي بعد «لو» على أنّه حدث وقع'),
    10: ('§ الاستنتاج', 'الخلط بين الافتراض والاستنتاج لأنّ الحرف واحد'),
    11: ('§ أوظّف', 'الحكم على المعنى من الأداة وحدها'),
}

_N17('arabe.shart.ra2isi-bi-tartib-al-dhikr', 'S1',
     [U('17', [1], ('05', 5, 'a', "R1 : rôles inversés — le 1er cité (« كان الخبز ساخنًا ») pris pour le principal"),
                   ('05', 4, 'b', "« انتباه السائق » (le secondaire, cité en 1er) pris pour le principal"))])

_N17('arabe.shart.mudari3-marfu3-ba3d-adat', 'S2',
     [U('17', [2], ('02', 1, 'b', "R1 : « ترك الفعلين مرفوعين خطأ »"),
                   ('03', 5, 'b', "R1 : « متى يصلُ أخي نفرحُ »"),
                   ('03', 5, 'c', "R1 : « كيفما يصلُ أخي نفرحُ »"),
                   ('05', 3, 'd', "R1 : « قدّمت الحرف لكنّها تركت الجزم »"),
                   half="1re moitié : « ترك المضارع مرفوعًا بعد إن »")])

_N17('arabe.shart.jazm-fi-ghayr-mawdi3ih', 'S2b',
     [U('17', [2], ('02', 1, 'c', "R1 : « جزم الرئيسيّ المتقدّم خطأ »"),
                   ('03', 5, 'a', "R1 : « فيها جزم بعد إذا »"),
                   half="2e moitié : « جزم الرئيسيّ المتقدّم »")])

_N17('arabe.shart.lau-lil-mumkin', 'S3',
     [U('17', [3], ('05', 6, 'a', "R1 : « لو » = افتراض ممكن في المستقبل"),
                   ('02', 2, 'a', "« لو » + مضارع مجزوم / أمر"),
                   ('02', 2, 'b', "R1 : « لو » + مضارع منفيّ بـ« لن »"),
                   ('02', 2, 'c', "R1 : « لو » + السين"),
                   ('04', 1, 'a', "« إنْ » = الماضي، « لو » = المستقبل"))])

_N17('arabe.shart.fa-al-rabt-mahdhufa', 'S4',
     [U('17', [4], ('05', 2, 'b', "R1 : « حذف الفاء خطأ »"))])

_N17('arabe.shart.man-ma-shart-daiman', 'S5',
     [U('17', [5], ('quiz', 4, 'a', "R1 : « إنّ مَنْ… » — مَن بعد ناسخ"),
                   ('quiz', 4, 'b', "R1 : « كانَ مَنْ… » — بعد ناسخ"),
                   ('quiz', 4, 'd', "R1 : « يرتقي مَنْ… » — بعد فعل"),
                   ('01', 5, 'a', "R1 : « كانَ ما كتبه… »"),
                   ('01', 5, 'b', "R1 : « أعجبني ما قرأتَ »"),
                   ('01', 5, 'd', "R1 : « إنّ ما قلتَ صحيح »"),
                   ('04', 2, 'b', "R1 : « إنّ مَنْ يسهرْ… » ; l'explication : « اسم الشرط لا يقع بعد إنّ »"),
                   ('04', 2, 'c', "R1 : « كانَ مَنْ… »"),
                   ('04', 2, 'd', "R1 : « يتعبُ مَنْ يسهرُ… »"))])

_N17('arabe.shart.ism-shart-ghayr-munasib', 'S6',
     [U('17', [6], ('05', 1, 'a', "R1 : « متى » prise pour المكان"),
                   ('05', 1, 'c', "R1 : « متى » prise pour الهيئة"),
                   ('05', 1, 'd', "R1 : « متى » prise pour العاقل"),
                   ('02', 6, 'c', "R1 : « كيفما ظرف زمان »"))])

_N17('arabe.shart.wazifa-bila-ra2isi', 'S7',
     [U('17', [7], ('01', 6, 'a', "R1 : « مبتدأ » alors que le verbe veut un objet"),
                   ('01', 6, 'c', "R1 : « حال »"),
                   ('01', 6, 'd', "R1 : « مفعول فيه »"),
                   ('02', 5, 'a', "R1 : « مَن يدرس » pris pour مفعول فيه"),
                   ('02', 5, 'b', "R1 : « ما تكتب » pris pour مفعول فيه"),
                   ('02', 5, 'd', "R1 : « كيفما… » pris pour مفعول فيه"),
                   ('02', 6, 'a', "R1 : « لأنّه جاء في أوّل الجملة »"),
                   ('02', 6, 'b', "R1 : « المجزوم يكون حالًا »"),
                   ('04', 3, 'a', "R1 : « فاعل » alors que le verbe est complet"),
                   ('04', 3, 'c', "R1 : « مفعول به » alors que « يتّسع » est intransitif"),
                   ('04', 3, 'd', "R1 : « حال »"))])

_N17('arabe.shart.in-madi-ka-lau', 'S8',
     [U('17', [8], ('04', 1, 'c', "R1 : « لا فرق بينهما لأنّ الفعل ماضي الصيغة »"),
                   ('05', 6, 'b', "R1 : « كلتاهما تدلّ على امتناع »"))])

_N17('arabe.shart.lau-3ala-zahiriha', 'S9',
     [U('17', [9], ('01', 2, 'a', "R1 : « قراءة الماضي على أنّه حدث وقع »"),
                   ('01', 2, 'b', "R2 : lecture à moitié littérale"),
                   ('01', 2, 'd', "R2 : lecture à moitié littérale"),
                   ('02', 3, 'b', "R2 : « أخذ المظلة ولم يبتلّ »"),
                   ('02', 3, 'c', "R2 : « أخذها وابتلّ »"),
                   ('02', 3, 'd', "R1 : « النفي في الجواب يعني أنّه لم يبتلّ »"),
                   ('04', 4, 'a', "R1 : « الخطأ الشائع : لم يهملها ولم يرسب »"),
                   ('04', 4, 'b', "R2 : lecture à moitié littérale"),
                   ('04', 4, 'd', "R2 : lecture à moitié littérale"),
                   ('05', 4, 'a', "R1 : « قرأ النفي على ظاهره »"),
                   ('05', 4, 'c', "R1 : « قرأ النفي على ظاهره »"))])

_N17('arabe.shart.imkan-istintaj-khalt', 'S10',
     [U('17', [10, 11], ('quiz', 5, 'b', "إنْ + إمكان pris pour استنتاج"),
                        ('04', 6, 'b', "R1 : « حدثان ممكنان لم يقع ثانويّهما بعد »"),
                        ('04', 6, 'c', "R1 : « متى جاء الصيف… » — إمكان"),
                        ('05', 6, 'd', "R1 : « وليس استنتاجًا لأنّ البدء لم يقع بعد »"),
                        ('05', 5, 'd', "R1 : « وليست الجملة وعدًا بحدث ممكن »"),
                        ('04', 5, 'a', "P11 : le temps déduit du seul حرف « إنْ »"))])

_N17('arabe.shart.wujub-shart-khalt', 'S11',
     [U('17', [], ('quiz', 1, 'a', "R1 : « إخبار بحدثين وقعا » donné pour la définition du شرط"),
                  ('quiz', 5, 'd', "R1 : وجوب (« نجحتَ… فأهديتُك ») pris pour استنتاج"),
                  ('01', 1, 'c', "R1 : « لا حرف شرط فيها فلا ثانويّ »"),
                  ('01', 1, 'd', "R1 : idem"),
                  ('01', 3, 'a', "شرط (« إنْ ») pris pour un simple constat"),
                  ('01', 3, 'b', "شرط (« لو ») pris pour un simple constat"),
                  ('01', 3, 'c', "شرط (« متى ») pris pour un simple constat"),
                  ('03', 4, 'c', "R1 : وجوب pris pour امتناع"),
                  ('03', 6, 'b', "R1 : « غياب أداة الشرط » donné comme clé de l'امتناع"),
                  ('05', 5, 'c', "R1 : « كلاهما معلوم » — constat pris pour déduction"))])

_N17('arabe.shart.imtina3-ghayr-maqru2', 'S12',
     [U('17', [], ('quiz', 3, 'a', "R1 : « إنْ » pour un train déjà manqué"),
                  ('quiz', 3, 'b', "R1 : « إذا »"),
                  ('quiz', 3, 'c', "R1 : « متى »"),
                  ('03', 4, 'a', "R1 : إمكان (« إنْ يزرنا ») donné pour امتناع"),
                  ('03', 4, 'd', "R1 : إمكان (« متى يزرنا ») donné pour امتناع"),
                  ('03', 6, 'a', "R1 : قرائن الإمكان pour « لو دقّقتَ… »"),
                  ('03', 6, 'd', "R1 : قرائن الاستنتاج pour « لو دقّقتَ… »"))])

UNDER3 += [
    ("Place de la ف de liaison ou « ثمّ » mis à la place de la ف",
     "17:05#2→c,d (R1)",
     "1 question."),
    ("Le مفعول الشرط réduit à l'événement sans le حرف, ou étendu au début du principal",
     "17:03#1→a,b,d",
     "1 question ; le `verifie` du cours le travaille."),
    ("Type de la phrase principale lu depuis le verbe du شرط (« أضاء ») ou depuis la forme du شرط",
     "17:03#3→a,c (+ b : ف prise pour l'amr)",
     "1 question. Proche de `arabe.jumla.naw3-bi-fi3l` (type par présence d'un verbe) mais le verbe est hors de la proposition analysée : non réutilisé."),
    ("Nom de condition qui ne tient pas la صدارة : « تُحسِنْ إلى مَنْ أُحسِنْ » ; ou relatif conservé en fin de transformation",
     "17:05#3→a,b",
     "1 question."),
    ("Facteur qui fixe le temps de « إنْ » : le حرف lui-même, la forme du verbe, la place du principal",
     "17:04#5→c,d (a est classé dans `imkan-istintaj-khalt`)",
     "1 question."),
    ("« إنْ تُراجِعَ » : nasb au lieu de jazm (confusion إنْ / أنْ)",
     "17:02#1→d (R1)",
     "1 question."),
    ("Bascule du sens de « مَن » selon que le verbe suivant est marfu3 ou majzum (la différence est dite « pas de différence » ou « de temps »)",
     "17:02#4→a,c,d",
     "1 question (le piège n°5 est porté par `man-ma-shart-daiman` ailleurs)."),
    ("« أيّ » seul adapté au عاقل / غير عاقل ; mauvais nom de condition pour « أيّ »",
     "17:03#2→b,c,d",
     "1 question de mémoire."),
    ("Rôles inversés dans une déduction (le conclu pris pour le donné)",
     "17:05#5→a (classé sous `ra2isi-bi-tartib-al-dhikr` car l'ordre de mention est la cause lisible)",
     "voir doutes."),
    ("Ce qui s'est perdu / ce que dit « لو » dans un couple لو … إنْ",
     "17:05#6→a,d",
     "1 question."),
]


PRECEDENCE += [
    "**Shart : deux sens miroirs** — `shart.lau-lil-mumkin` quand لو est employé pour un fait encore possible / futur ; `shart.imtina3-ghayr-maqru2` quand إنْ / إذا / متى sont employés pour un fait que l'on sait déjà manqué.",
    "**Lecture de لو** — `shart.lau-3ala-zahiriha` quand l'élève lit les événements d'une phrase en « لو » à l'endroit (affirmatif = advenu, négatif = non advenu) ; `shart.in-madi-ka-lau` quand c'est le passé après « إنْ » qui est lu comme non advenu (ou « les deux phrases se valent »).",
    "**Faits vs hypothèse** — `shart.wujub-shart-khalt` dès qu'un des deux termes de la confusion est un simple constat sans outil de condition ; `shart.imkan-istintaj-khalt` quand les deux options sont des conditionnelles (إمكان contre استنتاج).",
    "**مَن / ما** — `shart.man-ma-shart-daiman` pour la NATURE (condition ou relatif) ; `shart.wazifa-bila-ra2isi` pour la FONCTION du groupe ; `shart.ism-shart-ghayr-munasib` seulement pour le couple nom / sens (personne, chose, temps, lieu, manière).",
    "**Jazm** — `shart.mudari3-marfu3-ba3d-adat` quand le jazm manque là où il est dû ; `shart.jazm-fi-ghayr-mawdi3ih` quand il est posé là où il n'est pas dû (principal antéposé, après إذا). Une option qui cumule un nasb (02#1→d) reste muette.",
]


# =====================================================================================
# CHAPITRE 18 — دلالة صيغ الفعل والحروف المقترنة به على الزمان (10 pièges)
# libellés lus dans ch18_labels_draft.json
# =====================================================================================
_D18 = _json.load(open('/tmp/claude-0/-home-user/8ff73c67-6eab-5a69-a66d-d237b8d69142/scratchpad/ar9/tags/work-A/ch18_labels_draft.json', encoding='utf-8'))


def _N18(i, key, uses, note=''):
    NEW(i, _D18[key]['ar'], _D18[key]['fr'], _D18[key]['en'], uses, note)


PIEGES['18'] = {
    1: ('§ المصدر والفعل', 'عدّ المصدر دالًّا على زمان («النجاحُ» ماضٍ)'),
    2: ('§ صيغة الماضي', 'الحكم على الزمان من الصيغة وحدها (« اشتريتُ » ماضٍ)'),
    3: ('§ المضارع المرفوع', 'قراءة المضارع حاضرًا دائمًا'),
    4: ('§ الدعاء والحكمة والقاعدة العلمية', 'قراءة الفعل من صيغته دون سياقه الخاص'),
    5: ('§ الحروف المقترنة بالفعل', 'قراءة الفعل بصيغته وإهمال الحرف المقترن (لم يحضر، لو تكرّمتَ فأغلقتَ)'),
    6: ('§ لو وهلّا ولام الأمر ولا الناهية', 'قراءة « لو » و« هلّا » مع الماضي خبرًا عن حدث مضى'),
    7: ('§ السين وسوف وقد', 'التسوية بين « قد » والسين في اليقين وبين السين وسوف في المدى'),
    8: ('§ لم ولمّا ولن', 'الحكم على زمان المنفيّ من صيغته والتسوية بين لم ولمّا'),
    9: ('§ إن وأن وكي وحتّى ولام التعليل', 'عدّ الحدث بعد هذه الحروف واقعًا'),
    10: ('§ أوظّف', 'أن تبدأ بالصيغة دائمًا'),
}

_N18('arabe.zaman.sigha-ma3na-khalt', 'A1',
     [U('18', [1], ('quiz', 1, 'a', "R2 : فعل ماضٍ donné pour « حدث بلا زمان »"),
                   ('quiz', 1, 'b', "R2 : مضارع donné pour « حدث بلا زمان »"),
                   ('quiz', 1, 'd', "R2 : مضارع donné pour « حدث بلا زمان »"),
                   ('quiz', 2, 'a', "R1 : sens du مضارع donné au passé"),
                   ('quiz', 2, 'c', "R1 : sens du دعاء donné au passé"),
                   ('quiz', 2, 'd', "R1 : sens du مصدر donné au passé"),
                   ('01', 1, 'c', "R1 : « اليقين أو الاحتمال » attribué à la forme"),
                   ('01', 1, 'd', "R1 : « نوع الحدث » attribué à la forme"),
                   ('01', 3, 'a', "R1 : sens du passé donné au مضارع"),
                   ('01', 3, 'b', "R1 : sens du دعاء donné au مضارع"),
                   ('01', 3, 'c', "R1 : sens du مصدر donné au مضارع"),
                   ('01', 6, 'c', "sens du مضارع (« مستمرّة في هذه اللحظة ») donné au verbe de دعاء"),
                   ('03', 1, 'a', "R1 : pas de مصدر dans la paire"),
                   ('03', 1, 'c', "R1 : مضارع pris pour l'achèvement"),
                   ('03', 1, 'd', "R1 : « إنجاح » (مصدر مزيد) pris pour un verbe / un fait qui a un temps — seul porteur du piège n°1"),
                   ('03', 2, 'a', "R1 : sens du passé donné au مضارع « يتدرّب »"))],
     note="Piège n°1 (« النجاحُ ماضٍ ») : le porteur littéral est 03#1→d ; le geste inverse (donner au verbe la propriété du مصدر) fournit les autres.")

_N18('arabe.zaman.zaman-min-al-sigha', 'A2',
     [U('18', [2, 3, 10], ('01', 1, 'b', "R1 : « الزمان الماضي أو الحاضر أو المستقبل » attribué à la forme"),
                          ('01', 2, 'b', "R1 : « سافر » censé fixer le temps"),
                          ('01', 2, 'd', "R1 : « فصيغة الفعل وحدها تكفي »"),
                          ('03', 2, 'b', "R1 : « الصيغة : الزمان الحاضر »"),
                          half="P2 + P3 + P10 : un seul geste, lire le temps à la forme")])

_N18('arabe.zaman.sayaq-khass-bil-sigha', 'A3',
     [U('18', [4], ('01', 6, 'a', "R1 : « الرحمة وقعت فعلًا في الماضي »"),
                   ('03', 3, 'b', "R1 : « المضارع يدلّ على اللحظة الحاضرة » dans une règle scientifique"),
                   ('03', 3, 'c', "R1 : règle scientifique lue au futur"),
                   ('03', 3, 'd', "R1 : règle scientifique lue au passé"),
                   ('04', 3, 'd', "R1 : « رعاك الله » lu comme un fait passé"),
                   ('05', 6, 'a', "R1 : « رعاك » lu comme passé accompli"))])

_N18('arabe.zaman.sayaq-khass-khalt', 'A4',
     [U('18', [], ('quiz', 3, 'b', "R2 : الحكمة donnée pour le contexte du دعاء"),
                  ('quiz', 3, 'c', "R2 : القاعدة العلمية"),
                  ('quiz', 3, 'd', "R2 : إخبار عن حدث مضى"),
                  ('01', 6, 'd', "دعاء lu comme حكمة (« لا يدلّ على زمان معيّن »)"),
                  ('04', 1, 'a', "R1 : « يحفظك الله » (دعاء) donné pour une حكمة"),
                  ('04', 1, 'b', "R1 : constat « سافر أخي أمس » donné pour une حكمة"),
                  ('04', 1, 'd', "R1 : « سيسافر قريبًا » donné pour une حكمة"),
                  ('04', 2, 'b', "R1 : récit d'hier lu comme دعاء"),
                  ('04', 2, 'c', "R1 : annonce d'une réussite lue comme دعاء"),
                  ('04', 2, 'd', "R1 : nouvelle d'un prix lue comme دعاء"))])

_N18('arabe.zaman.lau-halla-akhbar', 'A5',
     [U('18', [5, 6], ('02', 3, 'a', "R1 : « أعار » lu comme déjà fait"),
                      ('02', 3, 'd', "R1 : « كما في لو الشرطية »"),
                      ('04', 3, 'c', "R1 : « هلّا استقبلتَ » lu comme fait advenu"),
                      half="P5 : moitié « لو تكرّمتَ فأغلقتَ » ; P6 : les deux moitiés")])

_N18('arabe.zaman.qad-sin-sawfa-khalt', 'A6',
     [U('18', [7], ('quiz', 4, 'a', "R1 : قد = « يقين من الوقوع القريب »"),
                   ('02', 4, 'b', "R1 : السين donnée pour « المستقبل البعيد »"),
                   ('02', 4, 'c', "R1 : قد donné pour un يقين"),
                   ('04', 6, 'a', "R1 : السين = بعيد ; قد = يقين"),
                   ('05', 6, 'c', "R1 : « سَتَصِلُ » = احتمال"),
                   ('03', 6, 'c', "R1 : « كي » = يقين قريب (« الإمكان ليس يقينًا »)"),
                   ('05', 2, 'b', "R1 : « حتّى » = يقين قريب"),
                   ('05', 3, 'd', "R1 : « أنْ » = يقين قريب « لأنّ المتكلّم يريدها »"),
                   ('02', 6, 'c', "R1 : « إنْ » = « يقين… المستقبل القريب »"))])

_N18('arabe.zaman.nafy-zaman-khalt', 'A7',
     [U('18', [5, 8], ('02', 5, 'a', "R1 : لم = المستقبل, لمّا = الماضي القريب"),
                      ('02', 5, 'b', "R1 : لمّا = المستقبل البعيد"),
                      ('02', 5, 'c', "R1 : « لا فرق » entre لم et لمّا"),
                      ('03', 5, 'a', "R1 : لمّا lu comme لن"),
                      ('03', 5, 'd', "R1 : « لمّا يصل » lu au présent"),
                      ('04', 4, 'b', "R1 : لم donné pour لن"),
                      ('04', 6, 'd', "R1 : لم lu comme « الوقوع في الماضي » (négation ignorée)"),
                      ('05', 1, 'b', "R1 : لن lu comme لم (« الماضي »)"),
                      ('05', 5, 'b', "R1 : لن lu comme لم"),
                      ('05', 6, 'b', "R1 : لم lu comme « لم يقع في الحاضر »"),
                      half="P5 : moitié « لم يحضرْ » ; P8 : les deux moitiés")])

_N18('arabe.zaman.ba3d-in-an-kay-waqi3', 'A8',
     [U('18', [9], ('quiz', 5, 'a', "R1 : « إنْ تدخل على الماضي ولا تغيّر زمانه »"),
                   ('quiz', 5, 'd', "R1 : seul le jawab serait futur"),
                   ('02', 6, 'b', "R1 : « وقوع الحدثين في الماضي إذا جاء الفعل ماضيًا »"),
                   ('03', 6, 'b', "R1 : « الادّخار وشراء الكتاب منقضيان »"),
                   ('04', 3, 'a', "R1 : « إنْ وصلَ الضيف » lu comme advenu"),
                   ('05', 2, 'a', "R1 : « وقع في الماضي » après حتّى"),
                   ('05', 3, 'a', "R1 : « منقضية لأنّ أرادَ ماضٍ »"),
                   ('05', 4, 'a', "R1 : « وقعت في الماضي لأنّ جئتُ ماضٍ »"))])

_N18('arabe.zaman.nahiya-lan-khalt', 'A9',
     [U('18', [], ('04', 4, 'a', "R1 : « لا تُسافرْ » donné pour une certitude de non-réalisation"),
                  ('02', 2, 'c', "R1 : « لا تُهمل » lu comme une certitude (لن)"),
                  ('05', 1, 'd', "R1 : « لن نغادر » lu comme une demande de s'abstenir"))])

_N18('arabe.zaman.harf-ma3na-khalt', 'A10',
     [U('18', [], ('02', 1, 'a', "R1 : « التحضيض » donné pour « الالتماس »"),
                  ('02', 1, 'b', "R1 : « طلب ترك » pour هلّا"),
                  ('02', 1, 'c', "R1 : « اليقين من الوقوع » pour هلّا"),
                  ('02', 2, 'a', "R1 : « طلب القيام » pour لا الناهية"),
                  ('02', 2, 'd', "R1 : « عدم الوقوع في الماضي » pour لا الناهية"),
                  ('03', 4, 'a', "R1 : « طلب ترك » pour لام الأمر"),
                  ('03', 4, 'b', "R1 : « اليقين » pour لام الأمر"),
                  ('03', 4, 'd', "R1 : « إمكان » (لام التعليل) pour لام الأمر"),
                  ('quiz', 4, 'b', "R1 : « طلب ألّا يتأخّر » pour قد"),
                  ('quiz', 4, 'c', "R1 : « يقين من عدم الوقوع » pour قد"),
                  ('02', 4, 'd', "R1 : لن donné pour سوف"),
                  ('04', 5, 'a', "R1 : « إنْ » (إمكان) donné pour le تحضيض"))])

UNDER3 += [
    ("Lecture du seul contexte, en oubliant ce que dit la forme (« يكتب التلميذ الدرس أمسِ » pris pour un fait achevé)",
     "18:01#4→a (R1 : « في الماضي لكنّ الحدث غير منقضٍ »)",
     "1 question ; geste inverse de `zaman-min-al-sigha`."),
    ("Mots de temps lus sans la forme : au passé on propose « الآنَ », « غدًا », « بعد ساعة » (01#5→a,b,d)",
     "18:01#5→a,b,d",
     "1 question ; aucun chemin d'erreur net (le présent n'est pas « lu au passé »)."),
    ("Nafy, « إنْ + ماضٍ » ou question d'une phrase à la fois « achevée au passé » : options 01#4→c,d",
     "18:01#4→c,d",
     "1 question."),
    ("Durée de الدعاء : le même verbe, deux contextes — options b/c/d de 04#2 sont classées sous `sayaq-khass-khalt`",
     "—",
     "voir doutes."),
    ("Rôles inversés entre ce que dit la forme et ce que dit le contexte",
     "18:03#2→a (classé A1), 18:03#6→a",
     "1–2 questions."),
]


PRECEDENCE += [
    "**Temps lu à la forme (ch.18)** — `zaman.zaman-min-al-sigha` dès que la phrase est ordinaire (أمس / الآن / غدًا) et que l'élève décide à la forme ; `zaman.sayaq-khass-bil-sigha` quand la phrase est un دعاء, une حكمة ou une règle scientifique (même si l'option fautive est « حاضر لأنّه مضارع » : 18:03#3→b).",
    "**Deux familles de « contextes particuliers »** — `zaman.sayaq-khass-bil-sigha` : le contexte est reconnu mais le verbe est mal daté ; `zaman.sayaq-khass-khalt` : on se trompe de contexte (دعاء pris pour حكمة, récit pris pour دعاء).",
    "**Particules de futur** — `zaman.ba3d-in-an-kay-waqi3` : l'événement est lu comme ADVENU ; `zaman.qad-sin-sawfa-khalt` : il est lu comme CERTAIN (ou سين = سوف). Même option, deux erreurs (18:05#3→a ne dit que « advenu ») : suivre le texte de l'option.",
    "**Négation** — `zaman.nafy-zaman-khalt` quand la question porte sur le TEMPS (لم، لمّا، لن) ; `zaman.nahiya-lan-khalt` quand elle oppose demander de s'abstenir (لا + مجزوم) et affirmer l'impossibilité (لن).",
    "**Sens des particules** — `zaman.harf-ma3na-khalt` est un repli : il ne s'emploie que si ni `qad-sin-sawfa-khalt`, ni `nafy-zaman-khalt`, ni `nahiya-lan-khalt`, ni `lau-halla-akhbar` ne s'appliquent. `zaman.sigha-ma3na-khalt` est l'équivalent pour les FORMES (مصدر / ماضٍ / مضارع / دعاء).",
]
